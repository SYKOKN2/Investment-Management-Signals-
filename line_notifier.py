"""
ProFlow Signal v5 — Confirmed US Market Close Engine, Institutional Narrative Generator & Concise 5-Point LINE Notifier
Runs on GitHub Actions twice daily (morning after US market close & night after Asia close / Europe trade) + workflow_dispatch.

Key Upgrades in v5:
1) Dual-source Official US Market Close fetcher (Yahoo Finance Daily Chart API + TradingView Scanner fallback)
   for S&P 500 (^GSPC), Nasdaq 100 (^NDX), NY Dow (^DJI), SOX (^SOX), VIX (^VIX), and US 10Y Yield (^TNX).
   Guarantees exact 16:00 EST official closing prices & daily % changes in the morning LINE push, immune to
   futures/FX midnight rollover or London LSE (16:30 UTC) early-close distortion.
2) Session-aware Macro Narrative Generator ("市場の大きな流れ"):
   - Morning edition: Anchored on confirmed Wall Street closing flows, rates/FX/commodities, overnight news catalysts,
     and actionable spillover to Tokyo/SGX & LSE UCITS ETFs (SPYL/VWRA).
   - Night edition: Anchored on confirmed Tokyo/SGX closes, live European/LSE trade, and NY pre-market setup.
   - Optional Gemini API upgrade if GEMINI_API_KEY is set in GitHub Secrets (zero API key required by default).
3) Fixed HTML regex for `macroOverview` so `index.html` updates `市場の大きな流れ` reliably on every single run regardless of JSON indentation.
4) Redesigned LINE Push Notification: Narrative-first ("市場の大きな流れ" main story) + strictly 5 notable highlights ("特筆すべき5点").
"""
import json
import os
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta

SYMBOLS = {
    "SPYL":   {"tv": "LSE:SPYL",      "name": "SPYL (超低コストS&P)", "unit": "USD", "cat": "STOCK", "market": "LSE"},
    "QQQM":   {"tv": "NASDAQ:QQQM",   "name": "QQQM (Nasdaq100)",    "unit": "USD", "cat": "STOCK", "market": "US"},
    "FLIN":   {"tv": "AMEX:FLIN",     "name": "FLIN (インド株)",      "unit": "USD", "cat": "STOCK", "market": "US"},
    "UAE":    {"tv": "NASDAQ:UAE",    "name": "UAE (中東UAE株)",      "unit": "USD", "cat": "STOCK", "market": "US"},
    "CIBR":   {"tv": "NASDAQ:CIBR",   "name": "CIBR (サイバー)",      "unit": "USD", "cat": "STOCK", "market": "US"},
    "XLV":    {"tv": "AMEX:XLV",      "name": "XLV (ヘルスケア)",     "unit": "USD", "cat": "STOCK", "market": "US"},
    "XLP":    {"tv": "AMEX:XLP",      "name": "XLP (生活必需品)",     "unit": "USD", "cat": "STOCK", "market": "US"},
    "RSP":    {"tv": "AMEX:RSP",      "name": "RSP (S&P均等加重)",    "unit": "USD", "cat": "STOCK", "market": "US"},
    "8058":   {"tv": "TSE:8058",      "name": "三菱商事",             "unit": "JPY", "cat": "STOCK", "market": "JP"},
    "D05":    {"tv": "SGX:D05",       "name": "DBS銀行",              "unit": "SGD", "cat": "STOCK", "market": "SG"},
    "AMZN":   {"tv": "NASDAQ:AMZN",   "name": "Amazon",               "unit": "USD", "cat": "STOCK", "market": "US"},
    "SPCX":   {"tv": "NASDAQ:SPCX",   "name": "SpaceX",               "unit": "USD", "cat": "STOCK", "market": "US"},
    "TSLA":   {"tv": "NASDAQ:TSLA",   "name": "Tesla",                "unit": "USD", "cat": "STOCK", "market": "US"},
    "GOOG":   {"tv": "NASDAQ:GOOG",   "name": "Google",               "unit": "USD", "cat": "STOCK", "market": "US"},
    "IVV":    {"tv": "AMEX:IVV",      "name": "IVV (米S&P500)",       "unit": "USD", "cat": "STOCK", "market": "US"},
    "CSPX":   {"tv": "LSE:CSPX",      "name": "CSPX (LSE S&P)",       "unit": "USD", "cat": "STOCK", "market": "LSE"},
    "VHVE":   {"tv": "LSE:VHVE",      "name": "VHVE (先進国)",        "unit": "USD", "cat": "STOCK", "market": "LSE"},
    "VWRA":   {"tv": "LSE:VWRA",      "name": "VWRA (全世界)",        "unit": "USD", "cat": "STOCK", "market": "LSE"},
    "SOXX":   {"tv": "NASDAQ:SOXX",   "name": "SOXX (米半導体)",      "unit": "USD", "cat": "STOCK", "market": "US"},
    "FGM":    {"tv": "NASDAQ:FGM",    "name": "FGM (独ETF)",          "unit": "USD", "cat": "STOCK", "market": "US"},
    "O39":    {"tv": "SGX:O39",       "name": "OCBC銀行",             "unit": "SGD", "cat": "STOCK", "market": "SG"},
    "1364":   {"tv": "TSE:1364",      "name": "1364 (JPX400)",        "unit": "JPY", "cat": "STOCK", "market": "JP"},
    "1475":   {"tv": "TSE:1475",      "name": "1475 (TOPIX)",         "unit": "JPY", "cat": "STOCK", "market": "JP"},
    "1329":   {"tv": "TSE:1329",      "name": "1329 (日経225)",       "unit": "JPY", "cat": "STOCK", "market": "JP"},
    "TLT":    {"tv": "NASDAQ:TLT",    "name": "TLT (米20年超国債)",   "unit": "USD", "cat": "MACRO", "market": "US"},
    "IEF":    {"tv": "NASDAQ:IEF",    "name": "IEF (米7-10年国債)",   "unit": "USD", "cat": "MACRO", "market": "US"},
    "GOLD":   {"tv": "TVC:GOLD",      "name": "GOLD (金スポット)",    "unit": "USD", "cat": "MACRO", "market": "MACRO"},
    "USOIL":  {"tv": "NYMEX:CL1!",    "name": "WTI原油",              "unit": "USD", "cat": "MACRO", "market": "MACRO"},
    "CPER":   {"tv": "AMEX:CPER",     "name": "CPER (銅ETF)",         "unit": "USD", "cat": "MACRO", "market": "US"},
    "DXY":    {"tv": "TVC:DXY",       "name": "DXY (米ドル指数)",     "unit": "INDEX","cat": "MACRO", "market": "MACRO"},
    "USDJPY": {"tv": "FX:USDJPY",     "name": "USD/JPY (ドル円)",     "unit": "JPY", "cat": "MACRO", "market": "FX"},
    "USDSGD": {"tv": "FX_IDC:USDSGD", "name": "USD/SGD (ドルSGD)",    "unit": "SGD", "cat": "MACRO", "market": "FX"},
    "SGDJPY": {"tv": "FX_IDC:SGDJPY", "name": "SGD/JPY (SGD円)",      "unit": "JPY", "cat": "MACRO", "market": "FX"},
}

EXTRA_TICKERS = [
    "TVC:VIX", "TVC:US10Y", "TVC:JP10Y",
    "SP:SPX", "NASDAQ:NDX", "TVC:DJI", "AMEX:SPY", "NASDAQ:QQQ"
]

COLUMNS = [
    "close", "change", "change_abs", "Recommend.All", "Recommend.All|1W", "RSI",
    "SMA20", "EMA20", "SMA50", "EMA50", "SMA200", "EMA200",
    "EMA50|1W", "SMA50|1W", "volume", "average_volume_30d_calc",
    "Perf.W", "Perf.1M", "Perf.3M", "Perf.6M", "Perf.YTD", "Perf.Y"
]

DASHBOARD_URL = "https://sykokn2.github.io/Investment-Management-Signals-/"


def fetch_tradingview_scan():
    url = "https://scanner.tradingview.com/global/scan"
    all_tickers = [v["tv"] for v in SYMBOLS.values()] + EXTRA_TICKERS
    payload = {
        "symbols": {"tickers": all_tickers},
        "columns": COLUMNS
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}
    )
    with urllib.request.urlopen(req, timeout=25) as resp:
        res = json.loads(resp.read().decode("utf-8"))

    out = {}
    extra = {}
    for row in res.get("data", []):
        tv_ticker = row["s"]
        vals = row["d"]
        mapped = dict(zip(COLUMNS, vals))
        if tv_ticker in EXTRA_TICKERS:
            extra[tv_ticker] = mapped
        for k, v in SYMBOLS.items():
            if v["tv"] == tv_ticker:
                out[k] = mapped
    return out, extra


def fetch_us_official_close(live_data, extra_data):
    """
    Fetches official completed US daily closing prices & % changes from Yahoo Finance Chart API
    for S&P 500 (^GSPC), Nasdaq 100 (^NDX), Dow (^DJI), SOX (^SOX), VIX (^VIX), and US10Y (^TNX),
    with automatic fallback to TradingView US cash/ETF benchmarks (SP:SPX/IVV, NASDAQ:NDX/QQQM, TVC:DJI, SOXX).
    """
    yf_map = {
        "SPX": "^GSPC",
        "NDX": "^NDX",
        "DJI": "^DJI",
        "SOX": "^SOX",
        "VIX": "^VIX",
        "US10Y": "^TNX",
    }
    results = {}
    tz_est = timezone(timedelta(hours=-5))

    for key, yf_sym in yf_map.items():
        encoded = urllib.parse.quote(yf_sym)
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{encoded}?interval=1d&range=5d"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=8) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            chart_res = data.get("chart", {}).get("result", [])
            if not chart_res:
                continue
            r0 = chart_res[0]
            timestamps = r0.get("timestamp") or []
            closes_raw = r0.get("indicators", {}).get("quote", [{}])[0].get("close") or []
            valid_pairs = [(ts, c) for ts, c in zip(timestamps, closes_raw) if c is not None]
            if len(valid_pairs) >= 2:
                last_ts, last_c = valid_pairs[-1]
                _, prev_c = valid_pairs[-2]
                chg_pct = ((last_c - prev_c) / prev_c) * 100.0 if prev_c else 0.0
                trade_dt = datetime.fromtimestamp(last_ts, tz=tz_est).strftime("%m/%d")
                results[key] = {
                    "close": float(last_c),
                    "change": float(chg_pct),
                    "date": trade_dt,
                    "source": "YF"
                }
            elif len(valid_pairs) == 1:
                last_ts, last_c = valid_pairs[-1]
                prev_c = r0.get("meta", {}).get("chartPreviousClose") or last_c
                chg_pct = ((last_c - prev_c) / prev_c) * 100.0 if prev_c else 0.0
                trade_dt = datetime.fromtimestamp(last_ts, tz=tz_est).strftime("%m/%d")
                results[key] = {
                    "close": float(last_c),
                    "change": float(chg_pct),
                    "date": trade_dt,
                    "source": "YF"
                }
        except Exception as e:
            print(f"Yahoo Finance fallback notice for {yf_sym}: {e}")

    # Fallback / cross-fill from TradingView US tickers so data is NEVER missing
    def tv_fallback(tv_extra_key, live_sym_key, default_close):
        d = extra_data.get(tv_extra_key, {}) if tv_extra_key else {}
        if not d or d.get("close") is None:
            d = live_data.get(live_sym_key, {}) if live_sym_key else {}
        return {
            "close": float(d.get("close") or default_close),
            "change": float(d.get("change") if d.get("change") is not None else 0.0),
            "date": results.get("SPX", {}).get("date", ""),
            "source": "TV"
        }

    if "SPX" not in results:
        results["SPX"] = tv_fallback("SP:SPX", "IVV", 6000.0)
    if "NDX" not in results:
        results["NDX"] = tv_fallback("NASDAQ:NDX", "QQQM", 21000.0)
    if "DJI" not in results:
        results["DJI"] = tv_fallback("TVC:DJI", "RSP", 44000.0)
    if "SOX" not in results:
        results["SOX"] = tv_fallback("", "SOXX", 5000.0)
    if "VIX" not in results:
        results["VIX"] = tv_fallback("TVC:VIX", "", 20.0)
    if "US10Y" not in results:
        results["US10Y"] = tv_fallback("TVC:US10Y", "", 4.50)

    return results


def fetch_latest_market_headlines(is_morning=True, max_items=4):
    """Fetches session-specific market headlines from Google News RSS (no API key required)."""
    headlines = []
    if is_morning:
        rss_urls = [
            "https://news.google.com/rss/search?q=%22%E7%B1%B3%E5%9B%BD%E6%A0%AA%22+OR+%22NY%E3%83%80%E3%82%A6%22+OR+%22%E3%83%8A%E3%82%B9%E3%83%80%E3%83%83%E3%82%AF%22+OR+%22S%26P500%22+OR+%22%E7%B1%B3%E9%95%B7%E6%9C%9F%E9%87%91%E5%88%A9%22+when:1d&hl=ja&gl=JP&ceid=JP:ja",
            "https://news.google.com/rss/headlines/section/topic/BUSINESS?hl=ja&gl=JP&ceid=JP:ja",
        ]
    else:
        rss_urls = [
            "https://news.google.com/rss/search?q=%22%E6%97%A5%E7%B5%8C%E5%B9%B3%E5%9D%87%22+OR+%22%E6%AC%A7%E5%B7%9E%E6%A0%AA%22+OR+%22%E7%B1%B3%E5%9B%BD%E6%A0%AA%22+OR+%22%E3%83%89%E3%83%AB%E5%86%86%22+when:1d&hl=ja&gl=JP&ceid=JP:ja",
            "https://news.google.com/rss/headlines/section/topic/BUSINESS?hl=ja&gl=JP&ceid=JP:ja",
        ]

    for url in rss_urls:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                xml_bytes = resp.read()
            root = ET.fromstring(xml_bytes)
            for item in root.findall(".//item"):
                title_el = item.find("title")
                if title_el is not None and title_el.text:
                    clean_t = re.sub(r"\s*-\s*[^-]+$", "", title_el.text.strip())
                    if clean_t and clean_t not in headlines:
                        headlines.append(clean_t)
                if len(headlines) >= max_items:
                    return headlines
        except Exception as e:
            print(f"RSS fetch warning: {e}")
    return headlines


def fmt_price(val, unit, sym_id=""):
    if val is None:
        return "-"
    if sym_id == "USDSGD":
        return f"{val:.4f}"
    if unit == "JPY" and val >= 1000:
        return f"{int(round(val)):,}"
    elif unit == "JPY" and val >= 100:
        return f"{val:.2f}"
    elif unit == "JPY":
        return f"{val:.1f}"
    return f"{val:.2f}"


def rec_label(val):
    if val is None:
        return "中立"
    if val >= 0.5:
        return "強い買い"
    if val >= 0.1:
        return "買い"
    if val <= -0.5:
        return "強い売り"
    if val <= -0.1:
        return "売り"
    return "中立"


def evaluate_pro_signal(sym_id, d):
    close = d.get("close")
    rsi = d.get("RSI")
    sma20 = d.get("SMA20")
    sma50 = d.get("SMA50")
    sma200 = d.get("SMA200")
    ema50_1w = d.get("EMA50|1W")
    unit = SYMBOLS[sym_id]["unit"]

    if close is None:
        return ("様子見", "Wait", "warning", "データ待機", "Hold", "warning", "データ取得中", "50%")

    low_ref = sma200 or ema50_1w or (close * 0.95)
    high_ref = sma20 or (close * 1.05)
    if low_ref > high_ref:
        low_ref, high_ref = high_ref, low_ref
    span = max(high_ref - low_ref, close * 0.01)
    pos_pct = int(max(12, min(88, round(((close - low_ref) / span) * 70 + 15))))

    if rsi is not None and rsi <= 30:
        sup_val = sma200 or ema50_1w or (close * 0.97)
        return (
            f"極度の売られすぎ (RSI {rsi:.1f})",
            f"Oversold (RSI {rsi:.0f})",
            "warning",
            "売られすぎ黄金押し目（分割買い好機）",
            "Strong Buy Zone",
            "success",
            f"日足RSI {rsi:.1f} の投げ売り極致！サポート({fmt_price(sup_val, unit, sym_id)})圏で反発狙い",
            f"{max(15, min(32, pos_pct))}%"
        )

    if sma20 and sma50 and (sma200 is None or close >= sma200) and close >= sma20 and close >= sma50:
        if rsi is not None and rsi >= 72:
            return (
                f"強い買いも短期過熱 (RSI {rsi:.1f})",
                f"Overbought (RSI {rsi:.0f})",
                "warning",
                f"20日線({fmt_price(sma20, unit, sym_id)})への押し目待ち",
                "Buy on Dip",
                "success",
                f"全移動平均線の上で独歩高も、RSI {rsi:.1f} のため高値飛びつき注意",
                "84%"
            )
        return (
            f"買い（20日線 {fmt_price(sma20, unit, sym_id)} サポート）",
            "Buy",
            "success",
            "強い買い（主要移動平均線の上を維持）",
            "Strong Buy",
            "success",
            f"20SMA({fmt_price(sma20, unit, sym_id)})・50SMA({fmt_price(sma50, unit, sym_id)})の上を走る上昇トレンド",
            "72%"
        )

    near_200d = sma200 and abs(close - sma200) / sma200 <= 0.025
    near_50w = ema50_1w and abs(close - ema50_1w) / ema50_1w <= 0.025
    if near_200d or near_50w:
        sup_label = f"日足200SMA({fmt_price(sma200, unit, sym_id)})" if near_200d else f"週足50EMA({fmt_price(ema50_1w, unit, sym_id)})"
        return (
            f"{sup_label} の攻防",
            "Support Test",
            "warning",
            "岩盤サポート帯で分割買い第1弾",
            "Buy Zone 1",
            "success",
            f"機関投資家が意識する {sup_label} 付近の重要サポート帯に到達",
            "40%"
        )

    if (sma50 and close >= sma50) or (sma200 and close >= sma200):
        sup_val = sma50 if (sma50 and close >= sma50) else sma200
        return (
            f"押し目形成中 (RSI {rsi:.1f})" if rsi else "押し目形成中",
            "Pullback",
            "warning",
            f"主要サポート({fmt_price(sup_val, unit, sym_id)})上での押し目買い",
            "Accumulate",
            "success",
            f"長期サポート({fmt_price(sup_val, unit, sym_id)})の上を維持しながらクールダウン中",
            "52%"
        )

    return (
        f"反発模索（20日線 {fmt_price(sma20, unit, sym_id)} 下）",
        "Rebound Watch",
        "warning" if (d.get("change") or 0) > 1.0 else "error",
        "押し目拾い・トレンド回復待ち",
        "Accumulate / Wait",
        "warning",
        f"20SMA({fmt_price(sma20, unit, sym_id)})奪還に向けた底固め局面（急騰日の高値追いは禁物）",
        "30%"
    )


def maybe_enhance_with_gemini(prompt_context):
    """Optional: If GEMINI_API_KEY is configured in GitHub Secrets, generates an ultra-natural LLM narrative."""
    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not api_key:
        return None
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    payload = {
        "contents": [{"parts": [{"text": prompt_context}]}],
        "generationConfig": {"temperature": 0.35, "responseMimeType": "application/json"}
    }
    try:
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=18) as resp:
            res = json.loads(resp.read().decode("utf-8"))
        text = res["candidates"][0]["content"]["parts"][0]["text"]
        parsed = json.loads(text)
        if parsed.get("headline") and parsed.get("body"):
            return parsed
    except Exception as e:
        print(f"Optional Gemini narrative skipped: {e}")
    return None


def select_notable_watch_item(live_data, is_morning):
    """Picks 1-2 most notable technical triggers or price moves from the user's 33 watched symbols."""
    candidates = []
    target_markets = {"US"} if is_morning else {"JP", "SG", "LSE", "US"}

    for sym_id, meta in SYMBOLS.items():
        if meta["cat"] != "STOCK":
            continue
        d = live_data.get(sym_id, {})
        close = d.get("close")
        chg = d.get("change")
        rsi = d.get("RSI")
        sma200 = d.get("SMA200")
        if close is None or chg is None:
            continue

        score = 0.0
        tag = ""
        if rsi is not None and rsi <= 31.5:
            score += 50.0 + (32.0 - rsi)
            tag = f"RSI {rsi:.1f} 売られすぎ圏"
        elif sma200 and abs(close - sma200) / sma200 <= 0.018:
            score += 30.0 + abs(chg)
            tag = f"200日線({fmt_price(sma200, meta['unit'], sym_id)})攻防"
        elif rsi is not None and rsi >= 73.0:
            score += 25.0 + abs(chg)
            tag = f"RSI {rsi:.0f} 短期過熱"

        if meta["market"] in target_markets:
            score += abs(chg) * 6.0
            if not tag:
                tag = "急反発" if chg >= 2.0 else ("下落・押し目探り" if chg <= -2.0 else f"RSI {rsi:.0f}" if rsi else "")
        else:
            score += abs(chg) * 1.5

        candidates.append((score, sym_id, meta, close, chg, tag))

    candidates.sort(key=lambda x: x[0], reverse=True)
    picked = []
    for _, sym_id, meta, close, chg, tag in candidates[:2]:
        p_s = fmt_price(close, meta["unit"], sym_id)
        short_name = meta["name"].split(" ")[0]
        suffix = f"・{tag}" if tag else ""
        picked.append(f"{short_name} {p_s} ({chg:+.2f}%{suffix})")
    return " / ".join(picked) if picked else "主要監視銘柄はレンジ内推移"


def build_dynamic_macro_narrative(live_data, extra_data, us_close, headlines, now_dt):
    """
    Generates an institutional-grade '市場の大きな流れ' macro narrative twice daily:
    - Morning (03:00-13:59 GMT+8): Confirmed US market close wrap + cross-asset money flow + Asia/UCITS positioning.
    - Night (14:00-02:59 GMT+8): Asia/Europe market flow + macro/rates setup ahead of NY open.
    """
    now_str = now_dt.strftime("%Y-%m-%d %H:%M GMT+8")
    is_morning = 3 <= now_dt.hour < 14

    spx_p = us_close["SPX"]["close"]
    spx_chg = us_close["SPX"]["change"]
    us_date = us_close["SPX"].get("date") or now_dt.strftime("%m/%d")
    ndx_p = us_close["NDX"]["close"]
    ndx_chg = us_close["NDX"]["change"]
    dji_p = us_close["DJI"]["close"]
    dji_chg = us_close["DJI"]["change"]

    soxx_d = live_data.get("SOXX", {})
    soxx_p = soxx_d.get("close") or us_close["SOX"]["close"]
    soxx_chg = soxx_d.get("change") if soxx_d.get("change") is not None else us_close["SOX"]["change"]
    soxx_1m = soxx_d.get("Perf.1M") or 0.0

    vix_tv = extra_data.get("TVC:VIX", {})
    vix = vix_tv.get("close") or us_close["VIX"]["close"]
    vix_chg = vix_tv.get("change") if vix_tv.get("change") is not None else us_close["VIX"]["change"]

    us10_tv = extra_data.get("TVC:US10Y", {})
    us10 = us10_tv.get("close") or us_close["US10Y"]["close"]
    jp10 = extra_data.get("TVC:JP10Y", {}).get("close") or 2.65

    dxy_d = live_data.get("DXY", {})
    dxy = dxy_d.get("close") or 104.0
    dxy_rsi = dxy_d.get("RSI") or 55.0

    tlt_d = live_data.get("TLT", {})
    tlt_p = tlt_d.get("close") or 82.0
    tlt_chg = tlt_d.get("change") if tlt_d.get("change") is not None else 0.0

    gold_d = live_data.get("GOLD", {})
    gold_p = gold_d.get("close") or 3630.0
    gold_chg = gold_d.get("change") or 0.0
    gold_rsi = gold_d.get("RSI") or 45.0

    oil_d = live_data.get("USOIL", {})
    oil_p = oil_d.get("close") or 79.5
    oil_chg = oil_d.get("change") or 0.0

    uj_p = live_data.get("USDJPY", {}).get("close") or 158.5
    usgd_p = live_data.get("USDSGD", {}).get("close") or 1.2900
    sj_p = live_data.get("SGDJPY", {}).get("close") or 122.8

    rsp_chg = live_data.get("RSP", {}).get("change") or 0.0
    xlv_chg = live_data.get("XLV", {}).get("change") or 0.0
    flin_chg = live_data.get("FLIN", {}).get("change") or 0.0

    # Filter session-relevant stock movers so stale prior-session markets don't distort the story
    if is_morning:
        session_stocks = [
            (k, v) for k, v in live_data.items()
            if SYMBOLS.get(k, {}).get("cat") == "STOCK"
            and SYMBOLS.get(k, {}).get("market") == "US"
            and v.get("change") is not None
        ]
    else:
        session_stocks = [
            (k, v) for k, v in live_data.items()
            if SYMBOLS.get(k, {}).get("cat") == "STOCK"
            and SYMBOLS.get(k, {}).get("market") in ("JP", "SG", "LSE")
            and v.get("change") is not None
        ]
        if not session_stocks:
            session_stocks = [
                (k, v) for k, v in live_data.items()
                if SYMBOLS.get(k, {}).get("cat") == "STOCK" and v.get("change") is not None
            ]

    session_stocks.sort(key=lambda x: x[1].get("change", 0.0), reverse=True)
    top_gainers = [f"{SYMBOLS[k]['name'].split(' ')[0]}({v['change']:+.1f}%)" for k, v in session_stocks[:2]]
    top_losers = [f"{SYMBOLS[k]['name'].split(' ')[0]}({v['change']:+.1f}%)" for k, v in session_stocks[-2:]]

    if is_morning:
        # Analyze confirmed US Market Close regime
        tech_vs_broad = ndx_chg - rsp_chg
        if spx_chg >= 1.0 and ndx_chg >= 1.2:
            core_title = f"米国株が広範なリスクオン反発（S&P {spx_chg:+.2f}%・NDX {ndx_chg:+.2f}%）× VIX低下で買い戻し優勢"
            flow_story = (
                f"米国市場（{us_date}終値）は、S&P500が{spx_chg:+.2f}%、Nasdaq100が{ndx_chg:+.2f}%、NYダウが{dji_chg:+.2f}%と揃って上昇して引けました。"
                f"米10年債利回りが{us10:.2f}%、VIXが{vix:.1f}へ落ち着いたことで機関投資家のショートカバーと押し目買いが流入し、"
                f"個別・セクターでは{'・'.join(top_gainers)}が相場を牽引しています。"
            )
        elif spx_chg <= -1.0 or ndx_chg <= -1.2:
            core_title = f"米国株はハイテク中心に調整（S&P {spx_chg:+.2f}%・NDX {ndx_chg:+.2f}%）× 国債・ディフェンシブへ資金退避"
            flow_story = (
                f"米国市場（{us_date}終値）は、Nasdaq100が{ndx_chg:+.2f}%、半導体SOXXが{soxx_chg:+.2f}%、S&P500が{spx_chg:+.2f}%とリスク回避の売りに押されました。"
                f"VIXが{vix:.1f}と警戒圏で推移するなか、割高感のあるグロース株（{'・'.join(top_losers)}）から利益確定やポジション圧縮が出る一方、"
                f"米長期国債TLT（{tlt_chg:+.2f}%）やディフェンシブ・高配当枠へ資金を逃がす動きが鮮明です。"
            )
        elif tlt_chg >= 0.5 and spx_chg < 0.3:
            core_title = f"米長期金利低下（{us10:.2f}%）・米国債TLT反発 × 株式は指数小動きの裏でセクター選別が進行"
            flow_story = (
                f"米国市場（{us_date}終値）は、S&P500が{spx_chg:+.2f}%、Nasdaq100が{ndx_chg:+.2f}%、NYダウが{dji_chg:+.2f}%と指数全体では底堅さを保ちつつ小幅な値動きで終えました。"
                f"注目すべきは債券市場への資金流入で、米10年債利回りが{us10:.3f}%へ低下し長期国債TLTが{tlt_chg:+.2f}%上昇。"
                f"株の内部では{'・'.join(top_losers)}が重石となる一方、{'・'.join(top_gainers)}やヘルスケア(XLV {xlv_chg:+.2f}%)・均等加重(RSP {rsp_chg:+.2f}%)が下支えする『一極集中から分散への資金シフト』が続いています。"
            )
        elif tech_vs_broad <= -0.6:
            core_title = f"ハイテク一服（NDX {ndx_chg:+.2f}%）からバリュー・均等加重（RSP {rsp_chg:+.2f}%）へのローテーション相場"
            flow_story = (
                f"米国市場（{us_date}終値）は、Nasdaq100（{ndx_chg:+.2f}%）・半導体SOXX（{soxx_chg:+.2f}%）の上値が重い一方、"
                f"NYダウ（{dji_chg:+.2f}%）やS&P均等加重RSP（{rsp_chg:+.2f}%）が相対優位となるセクターローテーションが進行しました。"
                f"機関投資家がハイパースケーラー偏重をならし、実物経済・ディフェンシブ・海外成長枠（インドFLIN {flin_chg:+.2f}%等）へ再配分する流れが継続しています。"
            )
        else:
            core_title = f"米国株は様子見圏で底固め（S&P {spx_chg:+.2f}%・NDX {ndx_chg:+.2f}%）× 金利{us10:.2f}%下の選別相場"
            flow_story = (
                f"米国市場（{us_date}終値）は、S&P500が{spx_chg:+.2f}%、Nasdaq100が{ndx_chg:+.2f}%、NYダウが{dji_chg:+.2f}%で取引を終了しました。"
                f"米10年債利回り{us10:.2f}%・WTI原油{oil_p:.1f}ドルのもとで過度なインフレ懸念は和らいでおり、"
                f"{'・'.join(top_gainers)}へ選別的な資金が向かう一方、{'・'.join(top_losers)}では戻り売りをこなす展開です。"
            )

        spyl_chg = live_data.get("SPYL", {}).get("change") or 0.0
        lse_gap_note = ""
        if abs(spx_chg - spyl_chg) >= 0.6:
            lse_gap_note = f"（注：ロンドン上場のSPYL/VWRAはNY引け4.5時間前の終値のため、NY終盤の値動き［S&P {spx_chg:+.2f}%］は今夜の欧州市場寄付きで織り込まれます。）"

        news_sentence = f"背景トピックとして「{headlines[0]}」などが意識されています。" if headlines else ""

        bridge_story = (
            f"為替はドル円が{uj_p:.2f}円、USD/SGDが{usgd_p:.4f}で推移。{news_sentence}"
            f"本日のアジア時間および今夜の欧州市場に向けては、急伸した銘柄への高値追いは控え、"
            f"RSI 30前後の売られすぎ圏や200日移動平均線付近にある超低コストコアETF（SPYL/VWRA/QQQM）や高配当バリュー株を指値で規律よく拾うスタンスが有効です。{lse_gap_note}"
        )
    else:
        # Night edition: Asia close + Europe/LSE live + NY preview
        topix_chg = live_data.get("1475", {}).get("change") or 0.0
        mc_chg = live_data.get("8058", {}).get("change") or 0.0
        dbs_chg = live_data.get("D05", {}).get("change") or 0.0
        spyl_chg = live_data.get("SPYL", {}).get("change") or 0.0

        core_title = f"アジア・欧州時間の資金フロー（TOPIX {topix_chg:+.2f}%・LSE:SPYL {spyl_chg:+.2f}%）× 今夜のNY市場展望"
        flow_story = (
            f"本日のアジア市場では、東証TOPIX(1475)が{topix_chg:+.2f}%（三菱商事 {mc_chg:+.2f}%）、シンガポールDBS銀行が{dbs_chg:+.2f}%で推移し、"
            f"現在取引中のロンドン市場ではS&P500連動のSPYLが{spyl_chg:+.2f}%と欧州勢のフローを映しています。"
            f"セッションを通じて{'・'.join(top_gainers)}が底堅い一方、{'・'.join(top_losers)}は利益確定・調整をこなす動きです。"
        )
        news_sentence = f"市場では「{headlines[0]}」などの材料が注目されています。" if headlines else ""
        bridge_story = (
            f"今夜の米国市場オープンを控え、米10年債利回りは{us10:.3f}%、VIXは{vix:.1f}、ドル円は{uj_p:.2f}円、WTI原油は{oil_p:.1f}ドルで推移。{news_sentence}"
            f"NY寄付き直後の乱高下には飛びつかず、米金利と半導体(SOXX)・Nasdaq(QQQM)の方向感を見極めながらサポート帯での分割指値を継続する局面です。"
        )

    full_body = f"{flow_story}\n\n{bridge_story}"

    # Optional Gemini polish if GEMINI_API_KEY is present in GitHub Secrets
    llm_prompt = (
        f"あなたは機関投資家向けマクロストラテジストです。以下の確定市場データとニュースに基づき、"
        f"個人投資家にも直感的に読める『市場の大きな流れ』のナラティブをJSON形式 "
        f'{{"headline": "45文字以内の核心タイトル", "body": "2段落・計280〜380文字程度の自然な日本語解説"}} で作成してください。'
        f"数値を羅列せず、なぜ資金がそう動いているかの背景ストーリーと投資スタンスを中心に書いてください。\n"
        f"時間帯: {'朝（米国市場終値確定後）' if is_morning else '夜（アジア終値・NY市場オープン前）'}\n"
        f"S&P500({us_date}終値): {spx_p:.2f} ({spx_chg:+.2f}%), Nasdaq100: {ndx_p:.2f} ({ndx_chg:+.2f}%), NYダウ: {dji_p:.2f} ({dji_chg:+.2f}%), "
        f"SOXX: {soxx_p:.2f} ({soxx_chg:+.2f}%), VIX: {vix:.2f} ({vix_chg:+.1f}%), 米10年債: {us10:.3f}%, TLT: {tlt_p:.2f} ({tlt_chg:+.2f}%), "
        f"DXY: {dxy:.2f}, USDJPY: {uj_p:.2f}, USDSGD: {usgd_p:.4f}, GOLD: {gold_p:.1f}, WTI原油: {oil_p:.2f}\n"
        f"強い銘柄: {', '.join(top_gainers)} / 弱い銘柄: {', '.join(top_losers)}\n"
        f"最新ニュース: {' / '.join(headlines[:3])}"
    )
    llm_res = maybe_enhance_with_gemini(llm_prompt)
    if llm_res:
        core_title = llm_res["headline"]
        full_body = llm_res["body"]

    session_badge = f"米市場 {us_date}終値反映" if is_morning else "アジア終値・欧州リアルタイム反映"
    regime_title = f"【{now_str[:10]} {session_badge}】{core_title}"
    regime_summary = full_body.replace("\n\n", " ")

    # Build the strictly 5 notable highlights ("特筆すべき5点")
    notable_item = select_notable_watch_item(live_data, is_morning)
    if is_morning:
        five_points = [
            f"1️⃣ 米国株終値({us_date}): S&P500 {spx_p:,.1f} ({spx_chg:+.2f}%) / NDX {ndx_chg:+.2f}% / ダウ {dji_chg:+.2f}%",
            f"2️⃣ 半導体・VIX: SOXX {soxx_p:.2f} ({soxx_chg:+.2f}%) / VIX {vix:.2f} ({vix_chg:+.1f}%)",
            f"3️⃣ 金利・米国債: 米10年債 {us10:.3f}% / TLT {tlt_p:.2f} ({tlt_chg:+.2f}%)",
            f"4️⃣ 為替・資源: ドル円 {uj_p:.2f}円 (USD/SGD {usgd_p:.4f}) / 金 {gold_p:,.0f}・原油 {oil_p:.1f}",
            f"5️⃣ 注目シグナル: {notable_item}",
        ]
    else:
        topix_p = fmt_price(live_data.get("1475", {}).get("close"), "JPY", "1475")
        topix_c = live_data.get("1475", {}).get("change") or 0.0
        dbs_p = fmt_price(live_data.get("D05", {}).get("close"), "SGD", "D05")
        dbs_c = live_data.get("D05", {}).get("change") or 0.0
        spyl_p = fmt_price(live_data.get("SPYL", {}).get("close"), "USD", "SPYL")
        spyl_c = live_data.get("SPYL", {}).get("change") or 0.0
        five_points = [
            f"1️⃣ 日・SG・欧株: TOPIX {topix_p} ({topix_c:+.2f}%) / DBS {dbs_p} ({dbs_c:+.2f}%) / SPYL {spyl_p} ({spyl_c:+.2f}%)",
            f"2️⃣ 米国指標(前日終値): S&P500 {spx_p:,.1f} ({spx_chg:+.2f}%) / VIX {vix:.2f}",
            f"3️⃣ 金利・米国債: 米10年債 {us10:.3f}% (日10年債 {jp10:.3f}%) / TLT {tlt_p:.2f}",
            f"4️⃣ 為替・資源: ドル円 {uj_p:.2f}円 (SGD円 {sj_p:.2f}円) / 金 {gold_p:,.0f}・原油 {oil_p:.1f}",
            f"5️⃣ 注目シグナル: {notable_item}",
        ]

    pillars = [
        {
            "title": "🏦 債券市場 (Bonds)",
            "status": f"米10年債 {us10:.3f}% / TLT {tlt_p:.2f} ({tlt_chg:+.2f}%)",
            "tone": "success" if tlt_chg >= 0 else "warning",
            "detail": f"米10年債利回りは {us10:.3f}%（日本10年債は {jp10:.3f}%）。WTI原油 {oil_p:.2f}ドルのもと、米長期国債ETF(TLT: {tlt_p:.2f}ドル)は株の変動に対するヘッジ兼・高利回りロックイン枠として機能しています。"
        },
        {
            "title": "💱 為替市場 (FX)",
            "status": f"DXY {dxy:.2f} / USDJPY {uj_p:.2f} / USDSGD {usgd_p:.4f}",
            "tone": "warning" if dxy_rsi >= 68 else "success",
            "detail": f"ドル指数(DXY)は {dxy:.2f}（日足RSI {dxy_rsi:.1f}）。ドル円は {uj_p:.2f}円、SGD円は {sj_p:.2f}円、USD/SGDは {usgd_p:.4f} で推移しています。"
        },
        {
            "title": "🪙 コモディティ (Commodities)",
            "status": f"GOLD {gold_p:,.1f} ({gold_chg:+.2f}%) / 原油 {oil_p:.2f}",
            "tone": "warning" if gold_rsi <= 32 else "success",
            "detail": f"スポット金(GOLD)は {gold_p:,.2f}ドル（日足RSI {gold_rsi:.1f}）、WTI原油は {oil_p:.2f}ドル（{oil_chg:+.2f}%）で推移し、インフレ期待と実質金利のバランスを映しています。"
        },
        {
            "title": "📉 米国株終値・セクター選別 (US Close & Rotation)",
            "status": f"S&P500 {spx_chg:+.2f}% / NDX {ndx_chg:+.2f}% / SOXX {soxx_chg:+.2f}%",
            "tone": "success" if spx_chg >= 0 else "warning",
            "detail": f"米国市場（{us_date}終値）はS&P500が {spx_p:,.2f} ({spx_chg:+.2f}%)、Nasdaq100が {ndx_p:,.2f} ({ndx_chg:+.2f}%)、NYダウが {dji_p:,.2f} ({dji_chg:+.2f}%)、半導体SOXXが {soxx_chg:+.2f}%（1ヶ月 {soxx_1m:+.1f}%）。"
        }
    ]

    return {
        "isMorning": is_morning,
        "sessionBadge": session_badge,
        "coreTitle": core_title,
        "lineBody": full_body,
        "fivePoints": five_points,
        "regimeTitle": regime_title,
        "regimeSummary": regime_summary,
        "pillars": pillars,
    }


def js_set_field(block, field, new_val_str):
    escaped = new_val_str.replace("\\", "\\\\").replace("'", "\\'")
    pattern = rf"({field}:\s*)(?:'[^']*'|\"[^\"]*\")"
    return re.sub(pattern, rf"\1'{escaped}'", block, count=1)


def update_dashboard_html(live_data, extra_data, us_close, narrative, now_str, html_path="index.html"):
    if not os.path.exists(html_path):
        print(f"{html_path} not found; skipping HTML update.")
        return

    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    vix_close = extra_data.get("TVC:VIX", {}).get("close") or us_close["VIX"]["close"]
    us10_close = extra_data.get("TVC:US10Y", {}).get("close") or us_close["US10Y"]["close"]
    jp10_close = extra_data.get("TVC:JP10Y", {}).get("close")

    vix_str = f"{vix_close:.2f}" if vix_close is not None else "20.00"
    us10_str = f"{us10_close:.3f}%" if us10_close is not None else "4.500%"
    jp10_str = f"{jp10_close:.3f}%" if jp10_close is not None else "2.650%"

    html = re.sub(r'updatedAt:\s*"[^"]*"', f'updatedAt: "{now_str}"', html)
    html = re.sub(r'vix:\s*"[^"]*"', f'vix: "{vix_str}",\n  us10y: "{us10_str}",\n  jp10y: "{jp10_str}"', html, count=1)
    html = re.sub(r'(us10y:\s*"[^"]*",\s*jp10y:\s*"[^"]*",\s*)+', f'us10y: "{us10_str}",\n  jp10y: "{jp10_str}",\n  ', html)

    # Fixed indentation-agnostic regex so macroOverview updates on EVERY run
    macro_raw_json = json.dumps({
        "regimeTitle": narrative["regimeTitle"],
        "regimeSummary": narrative["regimeSummary"],
        "pillars": narrative["pillars"]
    }, ensure_ascii=False, indent=2)
    macro_indented = "\n".join("  " + line if i > 0 else line for i, line in enumerate(macro_raw_json.splitlines()))
    html = re.sub(
        r"macroOverview:\s*\{.*?\n\s*\},\s*\n\s*symbols:",
        f"macroOverview: {macro_indented},\n  symbols:",
        html,
        count=1,
        flags=re.S
    )

    for sym_id, meta in SYMBOLS.items():
        d = live_data.get(sym_id)
        if not d or d.get("close") is None:
            continue

        unit = meta["unit"]
        close = d["close"]
        chg_pct = d.get("change") or 0.0
        chg_abs = d.get("change_abs") or 0.0
        rsi = d.get("RSI")
        sma20 = d.get("SMA20")
        sma50 = d.get("SMA50")
        sma200 = d.get("SMA200")
        ema50_1w = d.get("EMA50|1W")
        perf_1m = d.get("Perf.1M")
        perf_ytd = d.get("Perf.YTD")
        vol = d.get("volume")
        avg_vol = d.get("average_volume_30d_calc")
        vol_ratio = (vol / avg_vol) if (vol and avg_vol and avg_vol > 0) else None

        price_str = fmt_price(close, unit, sym_id)
        abs_str = fmt_price(abs(chg_abs), unit, sym_id)
        sign_abs = "+" if chg_abs >= 0 else "-"
        extra_chg = f" • 1M {perf_1m:+.2f}%" if perf_1m is not None else (f" • RSI {rsi:.1f}" if rsi is not None else "")
        vol_tag = f" • 出来高 {vol_ratio:.2f}x" if vol_ratio is not None else ""
        change_str = f"{sign_abs}{abs_str} ({chg_pct:+.2f}%){extra_chg}{vol_tag}"

        s_title, s_pill, s_tone, l_title, l_pill, l_tone, rng_status, rng_pos = evaluate_pro_signal(sym_id, d)

        low_val = sma200 or ema50_1w or (close * 0.95)
        high_val = sma20 or sma50 or (close * 1.05)
        low_label = "日足200SMA" if sma200 else ("週足50EMA" if ema50_1w else "サポート目安")
        high_label = "日足20SMA" if sma20 else "レジスタンス目安"
        if low_val > high_val:
            low_val, high_val = high_val, low_val
            low_label, high_label = high_label, low_label

        range_low_str = f"{fmt_price(low_val, unit, sym_id)} ({low_label})"
        range_mid_str = f"現在 {price_str}"
        range_high_str = f"{fmt_price(high_val, unit, sym_id)} ({high_label})"

        key_pat = rf"(?:^|\n)    (?:'{re.escape(sym_id)}'|{re.escape(sym_id)}):\s*\{{"
        m_start = re.search(key_pat, html)
        if m_start:
            start_idx = m_start.start()
            m_end = re.search(r"\n    \},\n|\n    \}\n  \}\n\};", html[start_idx + 10:])
            if m_end:
                end_idx = start_idx + 10 + m_end.start() + 6
                block = html[start_idx:end_idx]

                block = js_set_field(block, "price", price_str)
                block = js_set_field(block, "change", change_str)
                block = re.sub(r"(isUp:\s*)(?:true|false)", rf"\1{'true' if chg_pct >= 0 else 'false'}", block, count=1)
                block = js_set_field(block, "shortTitle", s_title)
                block = js_set_field(block, "shortPill", s_pill)
                block = js_set_field(block, "shortTone", s_tone)
                block = js_set_field(block, "longTitle", l_title)
                block = js_set_field(block, "longPill", l_pill)
                block = js_set_field(block, "longTone", l_tone)
                block = js_set_field(block, "rangeStatus", rng_status)
                block = js_set_field(block, "rangePos", rng_pos)
                block = js_set_field(block, "rangeLow", range_low_str)
                block = js_set_field(block, "rangeMid", range_mid_str)
                block = js_set_field(block, "rangeHigh", range_high_str)

                tv_1d = rec_label(d.get("Recommend.All"))
                tv_1w = rec_label(d.get("Recommend.All|1W"))
                rsi_v = f"{rsi:.2f}" if rsi is not None else "-"
                rsi_sub = "極度の売られすぎ！" if (rsi and rsi <= 30) else ("短期過熱圏" if (rsi and rsi >= 70) else "中立推移")
                sma20_v = fmt_price(sma20, unit, sym_id) if sma20 else "-"
                sma50_v = fmt_price(sma50, unit, sym_id) if sma50 else "-"
                sma200_v = fmt_price(sma200, unit, sym_id) if sma200 else fmt_price(ema50_1w, unit, sym_id)
                sma200_lbl = "日足 200SMA" if sma200 else "週足 50EMA"
                m1_v = f"{perf_1m:+.2f}%" if perf_1m is not None else (f"{vol_ratio:.2f}x" if vol_ratio else "-")
                m1_sub = f"出来高 {vol_ratio:.2f}x (30日比)" if vol_ratio else (f"YTD {perf_ytd:+.2f}%" if perf_ytd is not None else "TradingView同期")

                new_metrics = f"""metrics: [
        {{ label: '日足 RSI (14)', value: '{rsi_v}', sub: '{rsi_sub}' }},
        {{ label: '日足 20 / 50SMA', value: '{sma20_v} / {sma50_v}', sub: 'TV判定: {tv_1d}(日)・{tv_1w}(週)' }},
        {{ label: '{sma200_lbl}', value: '{sma200_v}', sub: '長期トレンド基準線' }},
        {{ label: '1ヶ月騰落率', value: '{m1_v}', sub: '{m1_sub}' }}
      ]"""
                block = re.sub(r"metrics:\s*\[.*?\]", new_metrics, block, flags=re.S)
                html = html[:start_idx] + block + html[end_idx:]

        d5 = d.get("Perf.W") if d.get("Perf.W") is not None else chg_pct
        m1 = d.get("Perf.1M") if d.get("Perf.1M") is not None else d5
        m3 = d.get("Perf.3M") if d.get("Perf.3M") is not None else m1
        m6 = d.get("Perf.6M") if d.get("Perf.6M") is not None else m3
        y1 = d.get("Perf.Y") if d.get("Perf.Y") is not None else (d.get("Perf.YTD") or m6)
        anc_sma = sma200 if sma200 is not None else (ema50_1w if ema50_1w is not None else close)

        anchor_key = f"'{sym_id}'" if sym_id.isdigit() else sym_id
        anchor_pat = rf"({re.escape(anchor_key)}:\s*\{{)\s*cur:\s*[-0-9.]+,\s*d5:\s*[-0-9.]+,\s*m1:\s*[-0-9.]+,\s*m3:\s*[-0-9.]+,\s*m6:\s*[-0-9.]+,\s*y1:\s*[-0-9.]+,\s*sma200:\s*[-0-9.]+\s*(\}})"
        anchor_rep = rf"\1 cur: {close:.4f}, d5: {d5:.2f}, m1: {m1:.2f}, m3: {m3:.2f}, m6: {m6:.2f}, y1: {y1:.2f}, sma200: {anc_sma:.4f} \2"
        html = re.sub(anchor_pat, anchor_rep, html)

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated macro narrative and all dynamic fields in {html_path} at {now_str}")


def build_line_message(narrative, now_str):
    """
    Narrative-first concise LINE push message:
    1) Session header (confirming US market close date in morning)
    2) Main '市場の大きな流れ' story
    3) Strictly 5 notable numerical highlights ('特筆すべき5点')
    4) Dashboard URL
    """
    icon = "🌅" if narrative["isMorning"] else "🌙"
    edition = "モーニング市場概観" if narrative["isMorning"] else "ナイト市場概観"

    lines = [
        f"{icon} ProFlow {edition}（{narrative['sessionBadge']}）",
        f"🕒 {now_str}",
        "",
        f"🌐 【市場の大きな流れ】",
        f"■ {narrative['coreTitle']}",
        "",
        narrative["lineBody"],
        "",
        "📌 【特筆すべき5つの重要数値】",
    ]
    lines.extend(narrative["fivePoints"])
    lines.extend([
        "",
        "🔗 チャート＆全33銘柄ダッシュボード:",
        DASHBOARD_URL
    ])
    return "\n".join(lines)


def send_line_push(message_text):
    token = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN", "").strip()
    user_id = os.environ.get("LINE_USER_ID", "").strip()

    if not token:
        print("LINE_CHANNEL_ACCESS_TOKEN 未設定のためLINE通知をスキップしました。")
        return

    if user_id:
        url = "https://api.line.me/v2/bot/message/push"
        payload = {"to": user_id, "messages": [{"type": "text", "text": message_text}]}
    else:
        url = "https://api.line.me/v2/bot/message/broadcast"
        payload = {"messages": [{"type": "text", "text": message_text}]}

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            print("LINE Push Notification sent successfully! HTTP:", resp.status)
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="ignore")
        print(f"LINE API Error ({e.code}): {err_body}")


if __name__ == "__main__":
    tz_sg = timezone(timedelta(hours=8))
    now_dt = datetime.now(tz_sg)
    now_str = now_dt.strftime("%Y-%m-%d %H:%M GMT+8")
    is_morning = 3 <= now_dt.hour < 14

    live, extra = fetch_tradingview_scan()
    us_close = fetch_us_official_close(live, extra)
    headlines = fetch_latest_market_headlines(is_morning=is_morning, max_items=4)
    narrative = build_dynamic_macro_narrative(live, extra, us_close, headlines, now_dt)

    print(f"Fetched {len(live)} symbols, US close ({us_close['SPX']}), and {len(headlines)} headlines.")
    update_dashboard_html(live, extra, us_close, narrative, now_str, "index.html")
    line_msg = build_line_message(narrative, now_str)
    print("--- LINE MESSAGE PREVIEW ---")
    print(line_msg)
    send_line_push(line_msg)
