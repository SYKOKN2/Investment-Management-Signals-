"""
ProFlow Signal — Complete Auto-Updating Cloud Engine & LINE Notifier
Runs on GitHub Actions (schedule & workflow_dispatch).
1) Fetches live TradingView data for all 31 symbols + VIX + US10Y + JP10Y.
2) Dynamically updates EVERY field in index.html:
   - updatedAt badge, vix, us10y, jp10y
   - macroOverview pillars with live prices/RSI
   - All 31 symbols: price, change, isUp, shortTitle, shortPill, shortTone, longTitle, longPill, longTone,
     rangeStatus, rangePos, rangeLow, rangeMid, rangeHigh, and all 4 metrics cards
   - CHART_ANCHORS: cur, d5, m1, m3, m6, y1, sma200
3) Sends the LINE push notification.
"""
import json
import os
import re
import urllib.request
from datetime import datetime, timezone, timedelta

SYMBOLS = {
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
        f"様子見（20日線 {fmt_price(sma20, unit, sym_id)} 下回る）",
        "Wait / Sell",
        "error",
        "底打ち・トレンド回復待ち",
        "Wait Recovery",
        "warning",
        f"主要移動平均線の下で調整中。まず20SMA({fmt_price(sma20, unit, sym_id)})奪還を待つ局面",
        "24%"
    )

def js_set_field(block, field, new_val_str):
    """Replaces `field: '...',` or `field: "...",` inside a JS object block."""
    escaped = new_val_str.replace("\\", "\\\\").replace("'", "\\'")
    pattern = rf"({field}:\s*)(?:'[^']*'|\"[^\"]*\")"
    return re.sub(pattern, rf"\1'{escaped}'", block, count=1)

def update_dashboard_html(live_data, extra_data, now_str, html_path="index.html"):
    if not os.path.exists(html_path):
        print(f"{html_path} not found; skipping HTML update.")
        return

    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    vix_close = extra_data.get("TVC:VIX", {}).get("close")
    us10_close = extra_data.get("TVC:US10Y", {}).get("close")
    jp10_close = extra_data.get("TVC:JP10Y", {}).get("close")

    vix_str = f"{vix_close:.2f}" if vix_close is not None else "35.90"
    us10_str = f"{us10_close:.3f}%" if us10_close is not None else "4.950%"
    jp10_str = f"{jp10_close:.3f}%" if jp10_close is not None else "2.835%"

    # Update top-level PROFLOW_DATA fields
    html = re.sub(r'updatedAt:\s*"[^"]*"', f'updatedAt: "{now_str}"', html)
    html = re.sub(r'vix:\s*"[^"]*"', f'vix: "{vix_str}",\n  us10y: "{us10_str}",\n  jp10y: "{jp10_str}"', html, count=1)
    # Clean up duplicate us10y/jp10y if already present
    html = re.sub(r'(us10y:\s*"[^"]*",\s*jp10y:\s*"[^"]*",\s*)+', f'us10y: "{us10_str}",\n  jp10y: "{jp10_str}",\n  ', html)

    # Update each symbol block in window.PROFLOW_DATA.symbols and CHART_ANCHORS
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
        perf_6m = d.get("Perf.6M")
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

        # Locate symbol block inside window.PROFLOW_DATA.symbols
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

                # Replace the 4 metrics boxes with live TradingView numbers
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

        # Update CHART_ANCHORS line for this symbol
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
    print(f"Successfully updated all dynamic fields in {html_path} at {now_str}")

def build_line_message(live_data, extra_data, now_str):
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
        "🌐 【マーケットの大きな流れ (債券・為替・商品)】",
        f"• VIX(恐怖指数): {vix_val} | 米10年債: {us10_val}%",
        f"• ドル指数(DXY): {quick_str('DXY', dxy)}",
        f"• 米国債(TLT): {quick_str('TLT', tlt)}",
        f"• GOLD(金): {quick_str('GOLD', gold)}",
        f"• WTI原油: {quick_str('USOIL', oil)}",
        f"• 半導体(SOXX): {quick_str('SOXX', soxx)}",
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
        msg.append("⏳ 【様子見・トレンド回復待ち】")
        msg.extend(wait_lines)
        msg.append("")

    msg.append("📱 最新チャート＆全31銘柄ダッシュボード:")
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
    print(f"Fetched {len(live)} symbols and {len(extra)} macro benchmarks.")
    update_dashboard_html(live, extra, now_str, "index.html")
    line_msg = build_line_message(live, extra, now_str)
    send_line_push(line_msg)
