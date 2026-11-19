"""
ProFlow Signal — Cloud Batch Analyzer & Cross-Asset LINE Push Notifier (Runs on GitHub Actions 24/7)
PCがスリープ中でもクラウド上で定期起動し、TradingViewのScanner APIから全25銘柄（株・ETF・債券・コモディティ・為替）の
最新価格・RSI・移動平均線を取得して：
1) プロ目線のマーケット概観（金利・ドル指数DXY・原油・金・VIX）
2) 今買うべき強い買いシグナル銘柄・岩盤サポート到達銘柄
をスマホのLINEへプッシュ通知します。
"""
import json
import os
import re
import urllib.request
from datetime import datetime, timezone, timedelta

SYMBOLS = {
    # 株式・ETF (16銘柄)
    "8058": {"tv": "TSE:8058",    "name": "三菱商事",         "unit": "JPY", "cat": "STOCK"},
    "D05":  {"tv": "SGX:D05",     "name": "DBS銀行",          "unit": "SGD", "cat": "STOCK"},
    "AMZN": {"tv": "NASDAQ:AMZN", "name": "Amazon",           "unit": "USD", "cat": "STOCK"},
    "IVV":  {"tv": "AMEX:IVV",    "name": "IVV (米S&P500)",   "unit": "USD", "cat": "STOCK"},
    "SPCX": {"tv": "NASDAQ:SPCX", "name": "SpaceX",           "unit": "USD", "cat": "STOCK"},
    "TSLA": {"tv": "NASDAQ:TSLA", "name": "Tesla",            "unit": "USD", "cat": "STOCK"},
    "VWRA": {"tv": "LSE:VWRA",    "name": "VWRA (全世界)",    "unit": "USD", "cat": "STOCK"},
    "CSPX": {"tv": "LSE:CSPX",    "name": "CSPX (LSE S&P)",   "unit": "USD", "cat": "STOCK"},
    "VHVE": {"tv": "LSE:VHVE",    "name": "VHVE (先進国)",    "unit": "USD", "cat": "STOCK"},
    "1364": {"tv": "TSE:1364",    "name": "1364 (JPX400)",    "unit": "JPY", "cat": "STOCK"},
    "1475": {"tv": "TSE:1475",    "name": "1475 (TOPIX)",     "unit": "JPY", "cat": "STOCK"},
    "1329": {"tv": "TSE:1329",    "name": "1329 (日経225)",   "unit": "JPY", "cat": "STOCK"},
    "O39":  {"tv": "SGX:O39",     "name": "OCBC銀行",         "unit": "SGD", "cat": "STOCK"},
    "GOOG": {"tv": "NASDAQ:GOOG", "name": "Google",           "unit": "USD", "cat": "STOCK"},
    "SOXX": {"tv": "NASDAQ:SOXX", "name": "SOXX (米半導体)",  "unit": "USD", "cat": "STOCK"},
    "FGM":  {"tv": "NASDAQ:FGM",  "name": "FGM (独ETF)",      "unit": "USD", "cat": "STOCK"},
    # 債券・コモディティ・為替 (9銘柄)
    "TLT":    {"tv": "NASDAQ:TLT",    "name": "TLT (米20年超国債)", "unit": "USD", "cat": "MACRO"},
    "IEF":    {"tv": "NASDAQ:IEF",    "name": "IEF (米7-10年国債)", "unit": "USD", "cat": "MACRO"},
    "GOLD":   {"tv": "TVC:GOLD",      "name": "GOLD (金スポット)",  "unit": "USD", "cat": "MACRO"},
    "USOIL":  {"tv": "NYMEX:CL1!",    "name": "WTI原油",            "unit": "USD", "cat": "MACRO"},
    "CPER":   {"tv": "AMEX:CPER",     "name": "CPER (銅ETF)",       "unit": "USD", "cat": "MACRO"},
    "DXY":    {"tv": "TVC:DXY",       "name": "DXY (米ドル指数)",   "unit": "IDX", "cat": "MACRO"},
    "USDJPY": {"tv": "FX:USDJPY",     "name": "USD/JPY (ドル円)",   "unit": "JPY", "cat": "MACRO"},
    "USDSGD": {"tv": "FX_IDC:USDSGD", "name": "USD/SGD (ドルSGD)",  "unit": "SGD", "cat": "MACRO"},
    "SGDJPY": {"tv": "FX_IDC:SGDJPY", "name": "SGD/JPY (SGD円)",    "unit": "JPY", "cat": "MACRO"},
}

COLUMNS = [
    "close", "change", "change_abs", "Recommend.All", "RSI",
    "SMA20", "EMA20", "SMA50", "EMA50", "SMA200", "EMA200",
    "EMA50|1W", "SMA50|1W", "volume", "average_volume_30d_calc"
]

DASHBOARD_URL = "https://sykokn2.github.io/Investment-Management-Signals-/?v=macro"

def fetch_tradingview_scan():
    url = "https://scanner.tradingview.com/global/scan"
    payload = {
        "symbols": {"tickers": [v["tv"] for v in SYMBOLS.values()]},
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
    for row in res.get("data", []):
        tv_ticker = row["s"]
        vals = row["d"]
        mapped = dict(zip(COLUMNS, vals))
        for k, v in SYMBOLS.items():
            if v["tv"] == tv_ticker:
                out[k] = mapped
    return out

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

def evaluate_pro_signal(sym_id, d):
    """TradingViewの最新テクニカル値からプロ目線のシグナルを自動判定"""
    close = d.get("close")
    rsi = d.get("RSI")
    sma20 = d.get("SMA20")
    sma50 = d.get("SMA50")
    sma200 = d.get("SMA200")
    ema50_1w = d.get("EMA50|1W")
    unit = SYMBOLS[sym_id]["unit"]

    if close is None:
        return "⚪ 取得中", "データ待機"

    # 1. 極度の売られすぎ（RSI 30以下＝D05, GOLD, CPERなど）
    if rsi is not None and rsi <= 30:
        return "🟢 売られすぎ黄金押し目", f"RSI {rsi:.1f} (投げ売り限界圏)"

    # 2. パーフェクトオーダー（20/50/200日線すべての上＝8058, AMZN, USDJPYなど）
    if sma20 and sma50 and sma200 and close >= sma20 and close >= sma50 and close >= sma200:
        if rsi is not None and rsi >= 70:
            return "🟠 上昇過熱 (RSI 70超)", f"RSI {rsi:.1f} ピーク警戒"
        return "🟢 強い買い (Strong Buy)", f"全MA上維持 (20SMA {fmt_price(sma20, unit, sym_id)})"

    # 3. 日足200SMAまたは週足50EMA付近（±1.8%以内）の岩盤サポート到達（IVV, VWRA, CSPX, VHVE, 1475, 1364など）
    near_200d = sma200 and abs(close - sma200) / sma200 <= 0.018
    near_50w = ema50_1w and abs(close - ema50_1w) / ema50_1w <= 0.018
    if near_200d or near_50w:
        sup = f"200日線({fmt_price(sma200, unit, sym_id)})" if near_200d else f"週足50EMA({fmt_price(ema50_1w, unit, sym_id)})"
        return "🟡 分割買い第1弾 (Buy Zone 1)", f"{sup} サポート攻防"

    # 4. 20日線または50日線突破の初動（SPCX, TSLA, TLT, IEFなど）
    if (sma20 and close >= sma20) or (sma50 and close >= sma50):
        return "🟢 押し目買い・反発初動", f"短期MAサポート回復"

    # 5. 下降トレンド・見送り（GOOG, 1329, SOXX, FGMなど）
    return "🔴 様子見 (Wait)", f"20日線({fmt_price(sma20, unit, sym_id)})回復待ち"

def build_line_message(live_data, now_str):
    # マクロ概観セクション（債券・為替・コモディティ・半導体）
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

    macro_lines = [
        "🌐 【マーケットの大きな流れ (債券・為替・商品)】",
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
        sig_label, reason = evaluate_pro_signal(sym_id, d)

        entry = f"• {meta['name']} ({sym_id}): {price_str} {unit} ({chg_str})\n  └ {sig_label} | {reason}"
        if sig_label.startswith("🟢"):
            buy_lines.append(entry)
        elif sig_label.startswith("🟡") or sig_label.startswith("🟠"):
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
        msg.append("🔥 【今買うべき・買いシグナル点灯】")
        msg.extend(buy_lines)
        msg.append("")
    if watch_lines:
        msg.append("🎯 【分割買い第1弾・岩盤サポート到達】")
        msg.extend(watch_lines)
        msg.append("")
    if wait_lines:
        msg.append("⏳ 【様子見・トレンド回復待ち】")
        msg.extend(wait_lines)
        msg.append("")

    msg.append("📱 市場の大きな流れ＆全25銘柄チャート:")
    msg.append(DASHBOARD_URL)
    return "\n".join(msg)

def send_line_push(message_text):
    token = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN", "").strip()
    user_id = os.environ.get("LINE_USER_ID", "").strip()

    if not token:
        print("LINE_CHANNEL_ACCESS_TOKEN が未設定のため、LINE通知をスキップしました。")
        print("--- 送信予定だったメッセージ ---\n" + message_text)
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

def main():
    tz_sg = timezone(timedelta(hours=8))
    now_str = datetime.now(tz_sg).strftime("%Y-%m-%d %H:%M GMT+8")

    live = fetch_tradingview_scan()
    print(f"Fetched live TradingView data for {len(live)} symbols.")

    if os.path.exists("signals_data.js"):
        with open("signals_data.js", "r", encoding="utf-8") as f:
            text = f.read()
        text = re.sub(r'updatedAt:\s*"[^"]*"', f'updatedAt: "{now_str}"', text)
        with open("signals_data.js", "w", encoding="utf-8") as f:
            f.write(text)

    line_msg = build_line_message(live, now_str)
    send_line_push(line_msg)

if __name__ == "__main__":
    main()
