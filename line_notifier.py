"""
ProFlow Signal — Complete Auto-Updating Cloud Engine, Dynamic Macro Narrative Generator & LINE Notifier
Runs on GitHub Actions twice daily (morning & night) + workflow_dispatch.
1) Fetches live TradingView data for all 33 symbols + VIX + US10Y + JP10Y.
2) Fetches live financial news headlines (Google News / Yahoo Finance RSS) to capture breaking macro/tech catalysts.
3) Dynamically generates a fresh institutional Macro Narrative (regimeTitle, regimeSummary, 4 cross-asset pillars,
   and money-flow rotation bullets) twice a day based on live market moves and news headlines!
4) Updates EVERY field in index.html (header, updatedAt, macroOverview, all symbol prices/RSI/signals/metrics, CHART_ANCHORS).
5) Sends the LINE push notification with the newly generated macro narrative.
"""
import json
import os
import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta

SYMBOLS = {
    "SPYL":   {"tv": "LSE:SPYL",      "name": "SPYL (超低コストS&P)","unit": "USD", "cat": "STOCK"},
    "QQQM":   {"tv": "NASDAQ:QQQM",   "name": "QQQM (低コストNDX)",  "unit": "USD", "cat": "STOCK"},
    "FLIN":   {"tv": "AMEX:FLIN",     "name": "FLIN (インド株)",    "unit": "USD", "cat": "STOCK"},
    "UAE":    {"tv": "NASDAQ:UAE",    "name": "UAE (中東UAE株)",    "unit": "USD", "cat": "STOCK"},
    "CIBR":   {"tv": "NASDAQ:CIBR",   "name": "CIBR (サイバー)",    "unit": "USD", "cat": "STOCK"},
    "XLV":    {"tv": "AMEX:XLV",      "name": "XLV (ヘルスケア)",   "unit": "USD", "cat": "STOCK"},
    "XLP":    {"tv": "AMEX:XLP",      "name": "XLP (生活必需品)",   "unit": "USD", "cat": "STOCK"},
    "RSP":    {"tv": "AMEX:RSP",      "name": "RSP (S&P均等加重)",  "unit": "USD", "cat": "STOCK"},
    "8058":   {"tv": "TSE:8058",      "name": "三菱商事",           "unit": "JPY", "cat": "STOCK"},
    "D05":    {"tv": "SGX:D05",       "name": "DBS銀行",            "unit": "SGD", "cat": "STOCK"},
    "AMZN":   {"tv": "NASDAQ:AMZN",   "name": "Amazon",             "unit": "USD", "cat": "STOCK"},
    "SPCX":   {"tv": "NASDAQ:SPCX",   "name": "SpaceX",             "unit": "USD", "cat": "STOCK"},
    "TSLA":   {"tv": "NASDAQ:TSLA",   "name": "Tesla",              "unit": "USD", "cat": "STOCK"},
    "GOOG":   {"tv": "NASDAQ:GOOG",   "name": "Google",             "unit": "USD", "cat": "STOCK"},
    "IVV":    {"tv": "AMEX:IVV",      "name": "IVV (米S&P500)",     "unit": "USD", "cat": "STOCK"},
    "CSPX":   {"tv": "LSE:CSPX",      "name": "CSPX (LSE S&P)",     "unit": "USD", "cat": "STOCK"},
    "VHVE":   {"tv": "LSE:VHVE",      "name": "VHVE (先進国)",      "unit": "USD", "cat": "STOCK"},
    "VWRA":   {"tv": "LSE:VWRA",      "name": "VWRA (全世界)",      "unit": "USD", "cat": "STOCK"},
    "SOXX":   {"tv": "NASDAQ:SOXX",   "name": "SOXX (米半導体)",    "unit": "USD", "cat": "STOCK"},
    "FGM":    {"tv": "NASDAQ:FGM",    "name": "FGM (独ETF)",        "unit": "USD", "cat": "STOCK"},
    "O39":    {"tv": "SGX:O39",       "name": "OCBC銀行",           "unit": "SGD", "cat": "STOCK"},
    "1364":   {"tv": "TSE:1364",      "name": "1364 (JPX400)",      "unit": "JPY", "cat": "STOCK"},
    "1475":   {"tv": "TSE:1475",      "name": "1475 (TOPIX)",       "unit": "JPY", "cat": "STOCK"},
    "1329":   {"tv": "TSE:1329",      "name": "1329 (日経225)",     "unit": "JPY", "cat": "STOCK"},
    "TLT":    {"tv": "NASDAQ:TLT",    "name": "TLT (米20年超国債)", "unit": "USD", "cat": "MACRO"},
    "IEF":    {"tv": "NASDAQ:IEF",    "name": "IEF (米7-10年国債)", "unit": "USD", "cat": "MACRO"},
    "GOLD":   {"tv": "TVC:GOLD",      "name": "GOLD (金スポット)",  "unit": "USD", "cat": "MACRO"},
    "USOIL":  {"tv": "NYMEX:CL1!",    "name": "WTI原油",            "unit": "USD", "cat": "MACRO"},
    "CPER":   {"tv": "AMEX:CPER",     "name": "CPER (銅ETF)",       "unit": "USD", "cat": "MACRO"},
    "DXY":    {"tv": "TVC:DXY",       "name": "DXY (米ドル指数)",   "unit": "INDEX","cat": "MACRO"},
    "USDJPY": {"tv": "FX:USDJPY",     "name": "USD/JPY (ドル円)",   "unit": "JPY", "cat": "MACRO"},
    "USDSGD": {"tv": "FX_IDC:USDSGD", "name": "USD/SGD (ドルSGD)",  "unit": "SGD", "cat": "MACRO"},
    "SGDJPY": {"tv": "FX_IDC:SGDJPY", "name": "SGD/JPY (SGD円)",    "unit": "JPY", "cat": "MACRO"},
}

EXTRA_TICKERS = ["TVC:VIX", "TVC:US10Y", "TVC:JP10Y"]

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

def fetch_latest_market_headlines(max_items=4):
    """Fetches live market headlines from Google News Business/Markets RSS (no API key required)."""
    headlines = []
    rss_urls = [
        "https://news.google.com/rss/search?q=株式市場+OR+米国株+OR+FRB+OR+日経平均+OR+半導体&hl=ja&gl=JP&ceid=JP:ja",
        "https://news.google.com/rss/headlines/section/topic/BUSINESS?hl=ja&gl=JP&ceid=JP:ja"
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

def build_dynamic_macro_narrative(live_data, extra_data, headlines, now_str):
    """
    1日2回の実行時に、その瞬間のVIX・金利・為替・コモディティ・株の騰落率と最新ニュース見出しから
    プロ目線の『市場の大きな流れ（regimeTitle, regimeSummary, 4 pillars）』を動的に組み立てます。
    """
    vix_d = extra_data.get("TVC:VIX", {})
    us10_d = extra_data.get("TVC:US10Y", {})
    jp10_d = extra_data.get("TVC:JP10Y", {})

    vix = vix_d.get("close") or 26.61
    vix_chg = vix_d.get("change") or 0.0
    us10 = us10_d.get("close") or 4.926
    jp10 = jp10_d.get("close") or 2.835

    dxy_d = live_data.get("DXY", {})
    dxy = dxy_d.get("close") or 104.29
    dxy_rsi = dxy_d.get("RSI") or 70.0

    tlt_d = live_data.get("TLT", {})
    tlt_p = tlt_d.get("close") or 81.69
    tlt_chg = tlt_d.get("change") or 0.0

    gold_d = live_data.get("GOLD", {})
    gold_p = gold_d.get("close") or 3630.0
    gold_rsi = gold_d.get("RSI") or 25.0

    oil_d = live_data.get("USOIL", {})
    oil_p = oil_d.get("close") or 79.61
    oil_1m = oil_d.get("Perf.1M") or -15.0

    uj_d = live_data.get("USDJPY", {})
    uj_p = uj_d.get("close") or 159.06
    usgd_p = live_data.get("USDSGD", {}).get("close") or 1.2914
    sj_p = live_data.get("SGDJPY", {}).get("close") or 123.10

    ivv_d = live_data.get("IVV", {})
    spx_chg = ivv_d.get("change") or 0.0
    qqq_d = live_data.get("QQQM", {}) or live_data.get("CSPX", {})
    ndx_chg = qqq_d.get("change") or 0.0
    soxx_d = live_data.get("SOXX", {})
    soxx_chg = soxx_d.get("change") or 0.0
    soxx_1m = soxx_d.get("Perf.1M") or -10.0

    # Rank top 3 strong performers & bottom 3 weak performers today among STOCK category
    stock_items = [(k, v) for k, v in live_data.items() if SYMBOLS.get(k, {}).get("cat") == "STOCK" and v.get("change") is not None]
    stock_items.sort(key=lambda x: x[1].get("change", 0.0), reverse=True)
    top_gainers = [f"{SYMBOLS[k]['name']}({v['change']:+.1f}%)" for k, v in stock_items[:3]]
    top_losers = [f"{SYMBOLS[k]['name']}({v['change']:+.1f}%)" for k, v in stock_items[-3:]]

    # Determine current macro regime phase
    if vix_chg <= -10.0 or ndx_chg >= 2.5:
        phase_tag = f"VIX急低下({vix:.1f} / {vix_chg:+.1f}%)・ハイテク急反発（ショートカバー）"
        action_bias = "売られすぎ極致(RSI 20台)からの強烈な自律反発が進行中。既に底値で仕込んだコアETF(SPYL/VWRA)の利益を伸ばしつつ、高値飛びつきは避けて押し目を待つ局面"
    elif vix >= 30.0 or spx_chg <= -1.5:
        phase_tag = f"VIX高止まり警戒({vix:.1f})・リスクオフの流動性選別"
        action_bias = "ボラティリティ拡大局面。パニック売りでRSI 30割れに到達した超低コストUCITS ETFや高配当銀行(DBS/OCBC)・商社(8058)を分割指値で冷静に拾う好機"
    else:
        phase_tag = f"米金利{us10:.2f}%・ドル指数{dxy:.1f}下のセクター選別＆恒久的再分配"
        action_bias = "指数全体の乱高下が一服し、機関投資家が割高な一部ハイパースケーラーから実物キャッシュ創出株・超低コスト指数・高配当株へ資金を再配分する局面"

    regime_title = f"【{now_str[:10]} 最新概観】{phase_tag} × 米10年債{us10:.2f}%・原油{oil_p:.1f}ドル"

    news_str = ""
    if headlines:
        news_str = " 📰直近の注目トピック：「" + "」「".join(headlines[:3]) + "」。"

    regime_summary = (
        f"現在（{now_str}更新）の市場は、恐怖指数VIXが {vix:.2f}（前日比 {vix_chg:+.1f}%）、米10年債利回りが {us10:.3f}%、米ドル指数(DXY)が {dxy:.2f}（RSI {dxy_rsi:.0f}）で推移しています。"
        f"直近セッションでは {', '.join(top_gainers)} が相場を牽引する一方、{', '.join(top_losers)} は相対的に上値が重い展開です。"
        f"プロ目線の基本戦略：{action_bias}です。{news_str}"
    )

    pillars = [
        {
            "title": "🏦 債券市場 (Bonds)",
            "status": f"米10年債 {us10:.3f}% / TLT {tlt_p:.2f} ({tlt_chg:+.2f}%)",
            "tone": "success" if tlt_chg >= 0 else "warning",
            "detail": f"米10年債利回りは {us10:.3f}%（日本10年債は {jp10:.3f}%）。WTI原油が {oil_p:.2f}ドル（1ヶ月 {oil_1m:+.1f}%）へ落ち着いたことでインフレ再燃懸念が和らぎ、米長期国債ETF(TLT: {tlt_p:.2f}ドル)は株の変動に対するヘッジ兼・高利回りロックイン枠として機能しています。"
        },
        {
            "title": "💱 為替市場 (FX)",
            "status": f"DXY {dxy:.2f} / USDJPY {uj_p:.2f} / USDSGD {usgd_p:.4f}",
            "tone": "warning" if dxy_rsi >= 68 else "success",
            "detail": f"ドル指数(DXY)は {dxy:.2f}（日足RSI {dxy_rsi:.1f}）。ドル円は {uj_p:.2f}円、SGD円は {sj_p:.2f}円、USD/SGDは {usgd_p:.4f} で推移。米ドルキャッシュは年利4.8%のMMFで運用しつつ、SGD資金はT-Bill(1.86%)より5%配当のDBS/OCBCが優位です。"
        },
        {
            "title": "🪙 コモディティ (Commodities)",
            "status": f"GOLD {gold_p:,.1f} (RSI {gold_rsi:.0f}) / 原油 {oil_p:.2f}",
            "tone": "warning" if gold_rsi <= 32 else "success",
            "detail": f"スポット金(GOLD)は {gold_p:,.2f}ドル（日足RSI {gold_rsi:.1f}）とドル高の逆風を受けて売られすぎ圏に位置し、中長期の逆張り分散ゾーン。WTI原油は {oil_p:.2f}ドルと80ドル前後で推移し、エネルギーコスト低下が株式市場の下支えとなっています。"
        },
        {
            "title": "📉 株式・半導体 (Equities & Rotation)",
            "status": f"S&P500 {spx_chg:+.2f}% / 半導体SOXX {soxx_chg:+.2f}%",
            "tone": "success" if spx_chg >= 0 else "warning",
            "detail": f"直近の米国株はS&P500(IVV)が {spx_chg:+.2f}%、半導体(SOXX)が {soxx_chg:+.2f}%（1ヶ月 {soxx_1m:+.1f}%）。急騰した日の高値飛びつきは避け、超低コストUCITS(SPYL 0.03% / VWRA 0.16%)やNasdaq100(QQQM 0.15%)、三菱商事(8058)の押し目を規律正しく拾う戦略が有効です。"
        }
    ]

    return {
        "regimeTitle": regime_title,
        "regimeSummary": regime_summary,
        "pillars": pillars,
        "topGainers": top_gainers,
        "topLosers": top_losers,
        "headlines": headlines
    }

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

def js_set_field(block, field, new_val_str):
    escaped = new_val_str.replace("\\", "\\\\").replace("'", "\\'")
    pattern = rf"({field}:\s*)(?:'[^']*'|\"[^\"]*\")"
    return re.sub(pattern, rf"\1'{escaped}'", block, count=1)

def update_dashboard_html(live_data, extra_data, narrative, now_str, html_path="index.html"):
    if not os.path.exists(html_path):
        print(f"{html_path} not found; skipping HTML update.")
        return

    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    vix_close = extra_data.get("TVC:VIX", {}).get("close")
    us10_close = extra_data.get("TVC:US10Y", {}).get("close")
    jp10_close = extra_data.get("TVC:JP10Y", {}).get("close")

    vix_str = f"{vix_close:.2f}" if vix_close is not None else "26.61"
    us10_str = f"{us10_close:.3f}%" if us10_close is not None else "4.926%"
    jp10_str = f"{jp10_close:.3f}%" if jp10_close is not None else "2.835%"

    html = re.sub(r'updatedAt:\s*"[^"]*"', f'updatedAt: "{now_str}"', html)
    html = re.sub(r'vix:\s*"[^"]*"', f'vix: "{vix_str}",\n  us10y: "{us10_str}",\n  jp10y: "{jp10_str}"', html, count=1)
    html = re.sub(r'(us10y:\s*"[^"]*",\s*jp10y:\s*"[^"]*",\s*)+', f'us10y: "{us10_str}",\n  jp10y: "{jp10_str}",\n  ', html)

    # Dynamically replace macroOverview block with the newly generated twice-daily narrative!
    macro_js_obj = "macroOverview: " + json.dumps({
        "regimeTitle": narrative["regimeTitle"],
        "regimeSummary": narrative["regimeSummary"],
        "pillars": narrative["pillars"]
    }, ensure_ascii=False, indent=4)
    html = re.sub(r"macroOverview:\s*\{.*?\n  \},\n  symbols:", macro_js_obj + ",\n  symbols:", html, count=1, flags=re.S)

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

def build_line_message(live_data, extra_data, narrative, now_str):
    vix_d = extra_data.get("TVC:VIX", {})
    us10_d = extra_data.get("TVC:US10Y", {})
    dxy = live_data.get("DXY", {})
    tlt = live_data.get("TLT", {})
    gold = live_data.get("GOLD", {})
    oil = live_data.get("USOIL", {})
    uj = live_data.get("USDJPY", {})
    usgd = live_data.get("USDSGD", {})
    sj = live_data.get("SGDJPY", {})
    soxx = live_data.get("SOXX", {})

    def quick_str(sym_id, d):
        c = fmt_price(d.get("close"), SYMBOLS[sym_id]["unit"], sym_id)
        chg = d.get("change")
        rsi = d.get("RSI")
        chg_s = f"{chg:+.2f}%" if chg is not None else "-"
        rsi_s = f"RSI {rsi:.0f}" if rsi is not None else ""
        return f"{c} ({chg_s} / {rsi_s})"

    vix_val = fmt_price(vix_d.get("close"), "USD")
    us10_val = fmt_price(us10_d.get("close"), "USD")

    macro_lines = [
        "🌐 【本日の市場の大きな流れ (自動更新ナラティブ)】",
        f"📌 {narrative['regimeTitle']}",
        f"{narrative['regimeSummary']}",
        "",
        f"• VIX: {vix_val} | 米10年債: {us10_val}% | DXY: {quick_str('DXY', dxy)}",
        f"• 米国債(TLT): {quick_str('TLT', tlt)} | GOLD: {quick_str('GOLD', gold)} | 原油: {quick_str('USOIL', oil)}",
        f"• 為替: USDJPY {fmt_price(uj.get('close'), 'JPY')} | USDSGD {fmt_price(usgd.get('close'), 'SGD', 'USDSGD')} | SGDJPY {fmt_price(sj.get('close'), 'JPY')}",
        ""
    ]

    buy_lines = []
    watch_lines = []
    wait_lines = []

    for sym_id, meta in SYMBOLS.items():
        if meta["cat"] != "STOCK":
            continue
        d = live_data.get(sym_id, {})
        close = d.get("close")
        chg = d.get("change")
        unit = meta["unit"]
        price_str = fmt_price(close, unit, sym_id)
        chg_str = f"{chg:+.2f}%" if chg is not None else "-"
        s_title, s_pill, s_tone, l_title, l_pill, l_tone, _, _ = evaluate_pro_signal(sym_id, d)

        entry = f"• {meta['name']} ({sym_id}): {price_str} {unit} ({chg_str})\n  └ {l_pill} | {s_title}"
        if l_tone == "success" and s_tone == "success":
            buy_lines.append(entry)
        elif l_tone == "success":
            watch_lines.append(entry)
        else:
            wait_lines.append(f"• {meta['name']}: {price_str} ({chg_str})")

    msg = [
        f"📊 【ProFlow 投資シグナル通知】",
        f"🕒 {now_str}",
        ""
    ]
    msg.extend(macro_lines)

    if buy_lines:
        msg.append("🔥 【強い買い・上昇トレンド維持】")
        msg.extend(buy_lines)
        msg.append("")
    if watch_lines:
        msg.append("🎯 【黄金押し目・分割買いゾーン到達】")
        msg.extend(watch_lines)
        msg.append("")
    if wait_lines:
        msg.append("⏳ 【反発模索・押し目待ち】")
        msg.extend(wait_lines)
        msg.append("")

    msg.append("📱 最新チャート＆全銘柄ダッシュボード:")
    msg.append(DASHBOARD_URL)
    return "\n".join(msg)

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
    now_str = datetime.now(tz_sg).strftime("%Y-%m-%d %H:%M GMT+8")
    live, extra = fetch_tradingview_scan()
    headlines = fetch_latest_market_headlines(max_items=4)
    narrative = build_dynamic_macro_narrative(live, extra, headlines, now_str)
    print(f"Fetched {len(live)} symbols, {len(extra)} macro benchmarks, and {len(headlines)} news headlines.")
    update_dashboard_html(live, extra, narrative, now_str, "index.html")
    line_msg = build_line_message(live, extra, narrative, now_str)
    send_line_push(line_msg)
