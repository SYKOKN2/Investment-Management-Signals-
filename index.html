<!DOCTYPE html>
<html lang="ja" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <meta name="apple-mobile-web-app-capable" content="yes" />
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
  <meta name="apple-mobile-web-app-title" content="ProFlow" />
  <title>ProFlow — Global Macro & AI Investment Signal</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    :root {
      --background: #090d16;
      --card: #111827;
      --border: #1f2937;
      --card-border: #1f2937;
      --foreground: #f9fafb;
      --muted-foreground: #9ca3af;
      --primary: #3b82f6;
      --primary-foreground: #ffffff;
      --secondary: #1f2937;
      --secondary-foreground: #e5e7eb;
      --link: #60a5fa;
      --success: #10b981;
      --warning: #f59e0b;
      --error: #ef4444;
    }
    body {
      background-color: var(--background);
      color: var(--foreground);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .no-scrollbar::-webkit-scrollbar { display: none; }
    .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
    .fade-in { animation: fadeIn 0.18s ease-out; }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(3px); }
      to { opacity: 1; transform: translateY(0); }
    }
  </style>
</head>
<body class="bg-[var(--background)] text-[var(--foreground)] antialiased p-4 sm:p-8 m-0 select-none">
  <div class="max-w-3xl mx-auto space-y-5">

    <!-- Minimal Top Bar -->
    <header class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
      <div class="flex items-center gap-2.5">
        <div class="w-2 h-2 rounded-full bg-[var(--success)]"></div>
        <span class="text-sm font-semibold tracking-tight">ProFlow</span>
        <span class="text-xs text-[var(--muted-foreground)] font-mono">US10Y 5.05% • DXY 103.97 • VIX 24.55</span>
      </div>
      <div class="flex items-center gap-1 bg-[var(--card)] border border-[var(--border)] p-1 rounded-full text-xs overflow-x-auto no-scrollbar">
        <button onclick="setMainView('macro')" id="nav-macro" class="px-3 py-1 rounded-full font-medium text-[var(--muted-foreground)] hover:text-[var(--foreground)] transition shrink-0">🌐 市場の大きな流れ</button>
        <button onclick="setMainView('signal')" id="nav-signal" class="px-3 py-1 rounded-full font-medium bg-[var(--foreground)] text-[var(--background)] transition shrink-0">📈 チャート＆分析</button>
        <button onclick="setMainView('picks')" id="nav-picks" class="px-3 py-1 rounded-full font-medium text-[var(--muted-foreground)] hover:text-[var(--foreground)] transition shrink-0">🏆 今買うべき5選</button>
        <button onclick="setMainView('matrix')" id="nav-matrix" class="px-3 py-1 rounded-full font-medium text-[var(--muted-foreground)] hover:text-[var(--foreground)] transition shrink-0">全31一覧</button>
      </div>
    </header>

    <!-- VIEW 0: MACRO OVERVIEW (プロ目線のマーケットの大きな流れ・概観) -->
    <main id="view-macro" class="hidden space-y-5 fade-in">
      <!-- Top Macro Regime Card -->
      <section class="bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 sm:p-6 space-y-4">
        <div class="flex items-center justify-between gap-2">
          <span class="px-2.5 py-0.5 rounded-full text-xs font-mono font-semibold bg-[var(--warning)]/15 text-[var(--warning)] border border-[var(--warning)]/30">GLOBAL MACRO REGIME • 2026-11-19</span>
          <span class="text-xs font-mono text-[var(--muted-foreground)]">TradingView Cross-Asset Sync</span>
        </div>
        <h2 id="macro-title" class="text-lg sm:text-xl font-bold tracking-tight leading-snug"></h2>
        <p id="macro-summary" class="text-xs sm:text-sm text-[var(--muted-foreground)] leading-relaxed"></p>

        <!-- Key Macro Ticker Strip (Tap to jump to chart) -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5 pt-2">
          <div onclick="jumpToSymbol('TLT')" class="p-3 rounded-xl bg-[var(--background)] border border-[var(--card-border)] cursor-pointer hover:border-[var(--primary)] transition">
            <div class="text-xs text-[var(--muted-foreground)]">🏦 米10年債 / TLT</div>
            <div class="text-sm font-bold font-mono mt-0.5">5.052% <span class="text-xs text-[var(--success)]">TLT +0.84%</span></div>
            <div class="text-xs text-[var(--muted-foreground)] mt-0.5">日10年債: 2.835%</div>
          </div>
          <div onclick="jumpToSymbol('DXY')" class="p-3 rounded-xl bg-[var(--background)] border border-[var(--card-border)] cursor-pointer hover:border-[var(--primary)] transition">
            <div class="text-xs text-[var(--muted-foreground)]">💱 ドル指数 (DXY)</div>
            <div class="text-sm font-bold font-mono mt-0.5">103.97 <span class="text-xs text-[var(--warning)]">RSI 71.3</span></div>
            <div class="text-xs text-[var(--muted-foreground)] mt-0.5">19ヶ月高値・ピーク接近</div>
          </div>
          <div onclick="jumpToSymbol('GOLD')" class="p-3 rounded-xl bg-[var(--background)] border border-[var(--card-border)] cursor-pointer hover:border-[var(--primary)] transition">
            <div class="text-xs text-[var(--muted-foreground)]">🪙 GOLD / 原油</div>
            <div class="text-sm font-bold font-mono mt-0.5">3,711 <span class="text-xs text-[var(--warning)]">RSI 29.3</span></div>
            <div class="text-xs text-[var(--muted-foreground)] mt-0.5">WTI原油: 81.95 (-16.7% 1M)</div>
          </div>
          <div onclick="jumpToSymbol('USDJPY')" class="p-3 rounded-xl bg-[var(--background)] border border-[var(--card-border)] cursor-pointer hover:border-[var(--primary)] transition">
            <div class="text-xs text-[var(--muted-foreground)]">💱 USD/JPY & SGD</div>
            <div class="text-sm font-bold font-mono mt-0.5">159.53円 <span class="text-xs text-[var(--success)]">Strong Buy</span></div>
            <div class="text-xs text-[var(--muted-foreground)] mt-0.5">USD/SGD: 1.2904</div>
          </div>
        </div>
      </section>

      <!-- 4 Cross-Asset Pillars Breakdown -->
      <section class="grid grid-cols-1 sm:grid-cols-2 gap-3.5" id="macro-pillars"></section>

      <!-- Money Flow Map: Where Institutional Money is Leaving vs Entering -->
      <section class="bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 sm:p-6 space-y-4">
        <h3 class="text-sm font-bold">🔄 機関投資家の資金ローテーション見取り図（タップで各チャートへ）</h3>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
          <div class="p-4 rounded-xl bg-[var(--background)] border border-[var(--error)]/30 space-y-2">
            <div class="font-bold text-[var(--error)]">💸 現在資金が抜けている場所（換金売り・逆風）</div>
            <ul class="space-y-1.5 text-[var(--muted-foreground)]">
              <li onclick="jumpToSymbol('SOXX')" class="cursor-pointer hover:underline">• <strong>半導体・台湾/日経225 (SOXX / 1329)</strong>：1ヶ月-16.7%。Anthropic IPO資金捻出の利確売り＆台湾株今日-4.8%。</li>
              <li onclick="jumpToSymbol('GOOG')" class="cursor-pointer hover:underline">• <strong>株主軽視のテック株 (GOOG)</strong>：6ヶ月-27.3%。高値新株発行×安値自社株売りでプロが離反。</li>
              <li onclick="jumpToSymbol('GOLD')" class="cursor-pointer hover:underline">• <strong>貴金属・銅 (GOLD / CPER)</strong>：米金利5%＋ドル高(DXY 103.97)で投げ売り（ただしRSI 23〜29で売られすぎ極致）。</li>
            </ul>
          </div>
          <div class="p-4 rounded-xl bg-[var(--background)] border border-[var(--success)]/30 space-y-2">
            <div class="font-bold text-[var(--success)]">💰 現在プロの資金が集まっている場所（買い・逃避先）</div>
            <ul class="space-y-1.5 text-[var(--muted-foreground)]">
              <li onclick="jumpToSymbol('8058')" class="cursor-pointer hover:underline">• <strong>高還元バリュー・商社 (8058 三菱商事)</strong>：1兆円自社株買い＋円安(159.5円)追い風で全MA上の独歩高。</li>
              <li onclick="jumpToSymbol('AMZN')" class="cursor-pointer hover:underline">• <strong>純粋AIクラウド・宇宙AI (AMZN / SPCX / TSLA)</strong>：Anthropic $110B契約のAmazonと宇宙DC構想のSpaceXに資金集中。</li>
              <li onclick="jumpToSymbol('D05')" class="cursor-pointer hover:underline">• <strong>高金利恩恵の売られすぎ銀行＆米国債 (D05 / TLT)</strong>：RSI 19.9で200日線到達のDBS銀行と、利回り5.05%の米国債(TLT)。</li>
            </ul>
          </div>
        </div>
      </section>
    </main>

    <!-- Region / Asset Class Filter + Ticker Bar -->
    <div id="nav-area" class="space-y-2.5">
      <div class="flex items-center gap-1.5 text-xs overflow-x-auto no-scrollbar">
        <button onclick="setRegion('ALL')" id="reg-ALL" class="px-2.5 py-1 rounded-lg font-medium transition">すべて (31)</button>
        <button onclick="setRegion('US')" id="reg-US" class="px-2.5 py-1 rounded-lg font-medium transition">🇺🇸 米個別株・宇宙 (4)</button>
        <button onclick="setRegion('ETF')" id="reg-ETF" class="px-2.5 py-1 rounded-lg font-medium transition">🌍 国別・セクター・指数ETF (12)</button>
        <button onclick="setRegion('SG')" id="reg-SG" class="px-2.5 py-1 rounded-lg font-medium transition">🇸🇬 シンガポール株 (2)</button>
        <button onclick="setRegion('JP')" id="reg-JP" class="px-2.5 py-1 rounded-lg font-medium transition">🇯🇵 日本株・ETF (4)</button>
        <button onclick="setRegion('BOND')" id="reg-BOND" class="px-2.5 py-1 rounded-lg font-medium transition">🏦 債券・金利 (2)</button>
        <button onclick="setRegion('COMMODITY')" id="reg-COMMODITY" class="px-2.5 py-1 rounded-lg font-medium transition">🪙 コモディティ (3)</button>
        <button onclick="setRegion('FX')" id="reg-FX" class="px-2.5 py-1 rounded-lg font-medium transition">💱 為替 FX (4)</button>
      </div>
      <nav id="ticker-bar" class="flex items-center gap-2 overflow-x-auto no-scrollbar py-0.5"></nav>
    </div>

    <!-- VIEW 1: SIGNAL COCKPIT -->
    <main id="view-signal" class="space-y-5 fade-in">

      <!-- Hero Card: Price, Apple Stocks Style Chart & Dual Signal -->
      <section class="bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 sm:p-7 space-y-5">
        <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-3">
          <div class="space-y-1">
            <div class="flex items-center gap-2">
              <span id="hero-asset-class" class="text-xs font-medium text-[var(--muted-foreground)]"></span>
              <span class="text-xs text-[var(--muted-foreground)]">•</span>
              <span id="hero-ticker" class="text-xs font-mono text-[var(--muted-foreground)]"></span>
            </div>
            <h1 id="hero-title" class="text-2xl sm:text-3xl font-bold tracking-tight"></h1>
            <p id="hero-subtitle" class="text-xs text-[var(--muted-foreground)]"></p>
          </div>

          <div class="sm:text-right font-mono tabular-nums">
            <div id="hero-price" class="text-2xl sm:text-3xl font-bold tracking-tight"></div>
            <div id="hero-change" class="text-xs font-medium mt-0.5"></div>
          </div>
        </div>

        <!-- Apple Stocks-Style Interactive Chart -->
        <div class="space-y-2.5 pt-1">
          <div class="flex items-center justify-between text-xs">
            <div class="flex items-center gap-3">
              <span id="chart-hover-label" class="font-mono text-[var(--muted-foreground)]">チャートをタッチで価格確認</span>
              <span class="hidden sm:inline-flex items-center gap-1.5 text-xs text-[var(--muted-foreground)]">
                <span class="inline-block w-3 border-t border-dashed border-sky-400"></span> 200日線(SMA)
              </span>
            </div>
            <div class="inline-flex bg-[var(--background)] border border-[var(--card-border)] p-0.5 rounded-lg text-xs font-mono">
              <button onclick="setChartRange('1M')" id="rng-1M" class="px-2.5 py-1 rounded-md transition">1M</button>
              <button onclick="setChartRange('6M')" id="rng-6M" class="px-2.5 py-1 rounded-md transition">6M</button>
              <button onclick="setChartRange('1Y')" id="rng-1Y" class="px-2.5 py-1 rounded-md transition">1Y</button>
            </div>
          </div>

          <div class="relative w-full h-44 sm:h-52 rounded-xl bg-[var(--background)]/60 border border-[var(--card-border)] p-2 overflow-hidden">
            <canvas id="apple-chart" class="w-full h-full cursor-crosshair"></canvas>
          </div>
        </div>

        <!-- Clean Signal Summary Strip -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-1">
          <div class="flex items-center justify-between p-3.5 rounded-xl bg-[var(--background)] border border-[var(--card-border)]">
            <div class="space-y-0.5">
              <span class="text-xs text-[var(--muted-foreground)]">短期（数日〜2週間）</span>
              <div id="sig-short-title" class="text-sm font-bold"></div>
            </div>
            <span id="sig-short-pill" class="px-2.5 py-1 rounded-full text-xs font-semibold shrink-0"></span>
          </div>

          <div class="flex items-center justify-between p-3.5 rounded-xl bg-[var(--background)] border border-[var(--card-border)]">
            <div class="space-y-0.5">
              <span class="text-xs text-[var(--muted-foreground)]">中長期・コア戦略</span>
              <div id="sig-long-title" class="text-sm font-bold"></div>
            </div>
            <span id="sig-long-pill" class="px-2.5 py-1 rounded-full text-xs font-semibold shrink-0"></span>
          </div>
        </div>

        <!-- Visual Price Range Gauge -->
        <div class="space-y-2 pt-1">
          <div class="flex items-center justify-between text-xs">
            <span class="text-[var(--muted-foreground)]">サポート</span>
            <span id="range-status" class="font-medium text-[var(--foreground)] text-center truncate px-2"></span>
            <span class="text-[var(--muted-foreground)]">レジスタンス</span>
          </div>
          <div class="relative h-2 w-full rounded-full bg-[var(--background)] border border-[var(--card-border)] overflow-hidden">
            <div class="absolute inset-y-0 left-0 w-1/3 bg-[var(--success)]/30"></div>
            <div id="range-marker" class="absolute top-0 bottom-0 w-2.5 rounded-full bg-[var(--primary)] transition-all duration-300" style="left: 30%"></div>
          </div>
          <div class="flex items-center justify-between text-xs font-mono text-[var(--muted-foreground)] tabular-nums">
            <span id="range-low"></span>
            <span id="range-mid" class="text-[var(--foreground)] font-semibold"></span>
            <span id="range-high"></span>
          </div>
        </div>
      </section>

      <!-- Pro Insights: Segmented Interactive Card -->
      <section class="bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 sm:p-6 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <h2 class="text-sm font-semibold">プロの目線（3大ファクター分析）</h2>
          <div class="inline-flex bg-[var(--background)] border border-[var(--card-border)] p-1 rounded-xl text-xs">
            <button onclick="setLens('flow')" id="lens-flow" class="px-3 py-1.5 rounded-lg font-medium transition flex-1 sm:flex-none">① 資金フロー</button>
            <button onclick="setLens('cta')" id="lens-cta" class="px-3 py-1.5 rounded-lg font-medium transition flex-1 sm:flex-none">② チャート</button>
            <button onclick="setLens('macro')" id="lens-macro" class="px-3 py-1.5 rounded-lg font-medium transition flex-1 sm:flex-none">③ マクロ・指標</button>
          </div>
        </div>

        <div id="lens-content" class="p-4 rounded-xl bg-[var(--background)] border border-[var(--card-border)] space-y-2 fade-in">
          <div class="flex items-center justify-between gap-2">
            <span id="lens-headline" class="text-sm font-bold"></span>
            <span id="lens-tag" class="text-xs font-mono text-[var(--link)] shrink-0"></span>
          </div>
          <p id="lens-body" class="text-xs text-[var(--muted-foreground)] leading-relaxed"></p>
        </div>

        <!-- Next Action Trigger -->
        <div class="flex items-start gap-3 pt-2">
          <div class="px-2 py-0.5 rounded text-xs font-mono bg-[var(--secondary)] text-[var(--secondary-foreground)] shrink-0 mt-0.5">ACTION</div>
          <p id="next-action-text" class="text-xs text-[var(--muted-foreground)] leading-relaxed"></p>
        </div>
      </section>

      <!-- Minimal Key Metrics Grid -->
      <section id="metrics-grid" class="grid grid-cols-2 sm:grid-cols-4 gap-3"></section>

    </main>

    <!-- VIEW 2: TOP PICKS (中長期で今買うべき厳選ランキング) -->
    <main id="view-picks" class="hidden space-y-4 fade-in">
      <section class="bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 sm:p-6 space-y-4">
        <div>
          <h2 class="text-base font-bold">🏆 中長期目線で「今」買うべき銘柄ランキング（クロスアセット版）</h2>
          <p class="text-xs text-[var(--muted-foreground)] mt-0.5">株・債券・コモディティ・為替の全31銘柄からプロの資金流入と岩盤サポートで厳選</p>
        </div>

        <div class="space-y-3 text-xs">
          <div onclick="jumpToSymbol('8058')" class="p-4 rounded-xl bg-[var(--background)] border border-[var(--success)]/40 cursor-pointer hover:opacity-90 transition space-y-1.5">
            <div class="flex items-center justify-between">
              <span class="font-bold text-sm text-[var(--success)]">🥇 1位：三菱商事 (8058) • 5,089円</span>
              <span class="px-2.5 py-0.5 rounded-full font-mono bg-[var(--success)]/15 text-[var(--success)]">Strong Buy</span>
            </div>
            <p class="text-[var(--muted-foreground)] leading-relaxed">1兆円の自社株買い＋159.5円の円安追い風。半導体調整（台湾株-4.8%）と無縁で全移動平均線の上を走る最強トレンド。</p>
          </div>

          <div onclick="jumpToSymbol('D05')" class="p-4 rounded-xl bg-[var(--background)] border border-[var(--success)]/40 cursor-pointer hover:opacity-90 transition space-y-1.5">
            <div class="flex items-center justify-between">
              <span class="font-bold text-sm text-[var(--success)]">🥈 2位：DBS Group (D05) • 66.55 SGD</span>
              <span class="px-2.5 py-0.5 rounded-full font-mono bg-[var(--success)]/15 text-[var(--success)]">RSI 19.9 黄金押し目</span>
            </div>
            <p class="text-[var(--muted-foreground)] leading-relaxed">米金利5.05%は銀行の金利収入に追い風。日足RSI 19.89の売られすぎ極致＋日足200SMA(66.72)・週足50EMA(65.96)の岩盤到達。</p>
          </div>

          <div onclick="jumpToSymbol('AMZN')" class="p-4 rounded-xl bg-[var(--background)] border border-[var(--success)]/40 cursor-pointer hover:opacity-90 transition space-y-1.5">
            <div class="flex items-center justify-between">
              <span class="font-bold text-sm text-[var(--success)]">🥉 3位：Amazon (AMZN) • 257.89 USD</span>
              <span class="px-2.5 py-0.5 rounded-full font-mono bg-[var(--success)]/15 text-[var(--success)]">AIクラウド本命</span>
            </div>
            <p class="text-[var(--muted-foreground)] leading-relaxed">Anthropic IPOの最大恩恵（AWSに1,100億ドル発注コミット）。日足・週足ともに「買い」判定を維持する米国メガテック筆頭。</p>
          </div>

          <div onclick="jumpToSymbol('IVV')" class="p-4 rounded-xl bg-[var(--background)] border border-[var(--card-border)] cursor-pointer hover:opacity-90 transition space-y-1.5">
            <div class="flex items-center justify-between">
              <span class="font-bold text-sm">🏅 4位：IVV / CSPX / VHVE ＆ 米国債 TLT（コア分散枠）</span>
              <span class="px-2.5 py-0.5 rounded-full font-mono bg-[var(--warning)]/15 text-[var(--warning)]">200日線支持 & 金利5%</span>
            </div>
            <p class="text-[var(--muted-foreground)] leading-relaxed">IVVは日足200SMA(735.59)を死守。さらに米10年債利回り5.05%到達で、長期米国債ETF（TLT 80.22ドル）やGOLD（RSI 29.3）の逆張り分散も有効な局面。</p>
          </div>

          <div onclick="jumpToSymbol('SPCX')" class="p-4 rounded-xl bg-[var(--background)] border border-[var(--card-border)] cursor-pointer hover:opacity-90 transition space-y-1.5">
            <div class="flex items-center justify-between">
              <span class="font-bold text-sm">🚀 5位（成長枠）：SpaceX (SPCX) & Tesla (TSLA)</span>
              <span class="px-2.5 py-0.5 rounded-full font-mono bg-[var(--success)]/15 text-[var(--success)]">逆行高・テーマ筆頭</span>
            </div>
            <p class="text-[var(--muted-foreground)] leading-relaxed">SpaceXは宇宙AIデータセンター構想＆Citi目標株価280ドル（約2倍）で+3.16%の逆行高。TeslaもCybercab量産転換とSpaceX統合思惑で堅調。</p>
          </div>
        </div>
      </section>
    </main>

    <!-- VIEW 3: ALL 25 SYMBOLS QUICK MATRIX -->
    <main id="view-matrix" class="hidden space-y-4 fade-in">
      <section class="bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 sm:p-6 space-y-4">
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-base font-bold">全31銘柄 クロスアセット比較マトリクス</h2>
            <p class="text-xs text-[var(--muted-foreground)] mt-0.5">株・ETF・債券・コモディティ・為替（タップで詳細チャートへ）</p>
          </div>
        </div>
        <div id="matrix-list" class="divide-y divide-[var(--card-border)] text-xs"></div>
      </section>
    </main>

  </div>

  <script>
window.PROFLOW_DATA = {
  updatedAt: "2026-11-20 14:10 GMT+8",
  vix: "24.55",
  macroOverview: {
    regimeTitle: "ハイパースケーラーからの「恒久的再分配」× インド株(FLIN)・高金利債・実物株への資金シフト",
    regimeSummary: "現在マーケットで起きているのは単なるAnthropic IPO前の換金売りにとどまらず、「ハイパースケーラー（Google等）は営業利益のAI比率に応じた『部分的AI企業』と見なし、ポートフォリオ比率を恒久的に引き下げる」という機関投資家の構造改革です。抜けた巨額資金は①100%純粋AI・宇宙(Anthropic/SpaceX)、②半導体不況と無縁で銀行株が最高値を更新中のインド株(FLIN 1ヶ月+9.2%・ルピー高)、③利回り5.05%の米国債(TLT)と高還元バリュー株(三菱商事・DBS銀行)へ再分配されています。",
    pillars: [
      {
        title: "🏦 債券市場 (Bonds)",
        status: "米10年債 5.052% / 日10年債 2.835%",
        tone: "warning",
        detail: "FRBの12月利上げ警戒で米2年債(4.789%)・10年債(5.052%)が高止まり。ただし原油(-16.7%)と銅(-13.5%)の急落でインフレ鈍化兆候が出始め、長期債ETF(TLT 80.22ドル)は日足50SMA(80.07)上で底打ち反発(+0.84%)を開始。"
      },
      {
        title: "💱 為替市場 (FX)",
        status: "DXY 103.97 / USDJPY 159.53 / SGDJPY 123.63",
        tone: "success",
        detail: "米金利5%とIPO決済のドル需要で全面ドル高(Strong Buy)。ドル円は200日線(158.80)の上を維持し160円に迫る。明日11/20(金)の日本10月CPIが円高巻き戻しか160円突破かの分岐点。"
      },
      {
        title: "🪙 コモディティ (Commodities)",
        status: "GOLD 3,711 (RSI 29.3) / WTI原油 81.95",
        tone: "warning",
        detail: "ドル高・高金利の逆風で貴金属・資源が換金売り。ゴールドは日足RSI 29.3、銅(CPER)はRSI 23.5と「極度の売られすぎ（投げ売りクライマックス）」に到達し、逆張り買い場が接近。"
      },
      {
        title: "📉 株式・半導体 (Equities & SOX)",
        status: "SOXX 1ヶ月-16.7% / 台湾株 今日-4.8%",
        tone: "error",
        detail: "Anthropic IPO前の半導体利確売りでSOX指数・台湾株が急落。相関の強い日経225(1329)は回復に時間がかかる一方、自社株買いの三菱商事(8058)やAWS契約のAmazon(AMZN)にプロの資金が集中。"
      }
    ]
  },
  symbols: {
    FLIN: {
      region: 'ETF',
      ticker: 'AMEX:FLIN',
      title: 'FLIN (インド株ETF)',
      subtitle: 'Franklin FTSE India ETF • 経費率 0.19% (INDAの1/3) • 1M +9.17%',
      assetClass: '🇮🇳 インド株ETF',
      price: '37.16',
      unit: 'USD',
      change: '+0.40 (+1.09%) • 1M +9.17% • 出来高 1.83倍',
      isUp: true,
      shortTitle: '強い買いも短期過熱（RSI 73.3・押し目待ち）',
      shortPill: 'Strong Buy (RSI 73)',
      shortTone: 'warning',
      longTitle: 'ハイテク流出資金の受け皿！35.5〜36.5で買い',
      longPill: 'Strong Buy',
      longTone: 'success',
      rangeStatus: '日足・週足ともにMA 14本すべて「買い」！アジア株暴落の中で9ヶ月ぶり高値へ独歩高',
      rangePos: '84%',
      rangeLow: '35.15 (日足200SMA)',
      rangeMid: '現在 37.16',
      rangeHigh: '37.65 (週足ピボットP)',
      lenses: {
        flow: {
          headline: 'ハイパースケーラー・半導体（台湾/韓国）から抜けた資金がインドへ殺到！',
          tag: '出来高 1.83x / 1年流入+$399M',
          body: '高コストなINDA(0.61%・資金流出-$1.91B)から低コストなFLIN(0.19%・純流入+$399M)へ機関投資家が乗り換え中。米ドル一強の中でインドルピー(USDINR 92.97)が逆行高になるほど海外マネーが流入しています。'
        },
        cta: {
          headline: 'TradingView判定：日足・週足ともに「強い買い（Strong Buy）」',
          tag: '日足 RSI 73.28 / 週足 60.5',
          body: '移動平均線は日足・週足ともに14本全てがBuy。ただし日足RSIが73.28と短期過熱圏にあるため、日足20EMA（35.89）〜週足50EMA（35.69）への軽い押し目を拾うのがベストです。'
        },
        macro: {
          headline: 'インド銀行株指数が史上最高値更新 ＆ 来週11/23(月) インドQ3 GDP発表',
          tag: '11/23 インドGDP (+7.6%予想)',
          body: '上位組入のHDFC銀行(5.6%)・ICICI銀行(5.2%)など内需・銀行が牽引し、半導体不況と無縁。来週月曜のインドGDP（予想+7.6%）前後の動きに注目です。'
        }
      },
      nextAction: '「恒久的再分配」の新たな成長コア枠として最適。RSI 73のため高値飛びつきは避け、①36.0〜36.8ドル（20EMA接近）で第1弾、②35.15〜35.70ドル（200SMA＆週足50EMA）で本命買い増し。',
      metrics: [
        { label: 'TV判定 (日/週)', value: '強い買い', sub: 'MA 14本すべてBuy' },
        { label: '1ヶ月騰落率', value: '+9.17%', sub: 'アジア株下落に逆行高' },
        { label: '日足 RSI (14)', value: '73.28', sub: '短期過熱・押し目待ち' },
        { label: '経費率 / 出来高', value: '0.19% / 1.83x', sub: '機関投資家が選好' }
      ]
    },
    UAE: {
      region: 'ETF',
      ticker: 'NASDAQ:UAE',
      title: 'UAE (アラブ首長国連邦)',
      subtitle: 'iShares MSCI UAE ETF • 1M +6.26% • 6M +9.37% • ドルペッグでドル高耐性',
      assetClass: '🇦🇪 中東・UAE株ETF',
      price: '20.89',
      unit: 'USD',
      change: '-1.46% • 1M +6.26% • 出来高 1.57倍',
      isUp: true,
      shortTitle: '買い（20日線20.06サポート・過熱感なし）',
      shortPill: 'Buy (RSI 61.5)',
      shortTone: 'success',
      longTitle: 'インドと並ぶ世界2大資金流入国！',
      longPill: 'Strong Buy',
      longTone: 'success',
      rangeStatus: '世界21ヶ国スキャンでインド(FLIN)と並び日足・週足ともに「買い」＆全MA上の唯一の国',
      rangePos: '74%',
      rangeLow: '19.56 (日足200SMA)',
      rangeMid: '現在 20.89',
      rangeHigh: '21.50 (直近高値節目)',
      lenses: {
        flow: {
          headline: '世界21ヶ国ETFの中で、インド(FLIN)以外に機関投資家が買っている唯一の国！',
          tag: '出来高 1.57x / 6M +9.37%',
          body: 'ブラジル(-30%)や豪州(-6.2%)など世界中の国別ETFが売られる中、UAEは1ヶ月+6.26%・6ヶ月+9.37%と独歩高。出来高も平均の1.57倍に膨らみ大口資金が流入中です。'
        },
        cta: {
          headline: '日足・週足ともに「買い（Buy）」判定！しかもRSI 61.5でインド(73.3)より買いやすい',
          tag: '20/50/200MA パーフェクトオーダー',
          body: '20SMA（20.06）・50SMA（19.90）・200SMA（19.56）すべての上に位置する美しい上昇トレンド。RSIも61.53と過熱しておらず、今からでもエントリー可能な水準です。'
        },
        macro: {
          headline: '通貨ディルハムが「米ドルペッグ（固定）」のため、米ドル一強(DXY 103.97)の悪影響ゼロ！',
          tag: 'アブダビAI資本 & ドバイ不動産',
          body: 'サウジ(KSA)と違い原油依存から脱却し、ドバイの不動産（Emaar）や高金利で潤うアブダビ・ドバイの巨大銀行、ソブリンAI投資（MGX）が成長を牽引しています。'
        }
      },
      nextAction: 'インド(FLIN)がRSI 73で押し目待ちなのに対し、UAEはRSI 61.5で今すぐ第1弾を買える好位置です。20.00〜20.89ドル（日足20SMA〜現在値）での分割買いが有効。',
      metrics: [
        { label: 'TV判定 (日/週)', value: '買い / 買い', sub: '世界21ヶ国でTop 2' },
        { label: '日足 RSI (14)', value: '61.53', sub: '過熱感なく健全な上昇' },
        { label: '日足 20/50SMA', value: '20.06 / 19.90', sub: '直下の強力サポート' },
        { label: '出来高倍率', value: '1.57x', sub: '機関投資家の資金流入' }
      ]
    },
    CIBR: {
      region: 'ETF',
      ticker: 'NASDAQ:CIBR',
      title: 'CIBR (サイバー防衛ETF)',
      subtitle: 'First Trust NASDAQ Cybersecurity ETF • YTD +33.89% • 1W +1.19%',
      assetClass: '🛡️ 米サイバーセキュリティETF',
      price: '96.36',
      unit: 'USD',
      change: '+0.31% • 1W +1.19% (全米セクター唯一プラス) • 出来高 1.78倍',
      isUp: true,
      shortTitle: '全米18セクターで今週唯一の逆行高！',
      shortPill: 'Top Sector (1.78x Vol)',
      shortTone: 'success',
      longTitle: 'ハイパースケーラー流出資金のテック最有力受け皿',
      longPill: 'Buy',
      longTone: 'success',
      rangeStatus: '半導体(SOXX)や一般ソフト(IGV)が崩れる中、出来高1.78倍を伴い今週唯一のプラス推移',
      rangePos: '66%',
      rangeLow: '84.92 (日足200SMA)',
      rangeMid: '現在 96.36',
      rangeHigh: '98.30 (日足20SMA)',
      lenses: {
        flow: {
          headline: 'ハイパースケーラーや半導体を売った「テック枠の資金」がCIBRに大移動！',
          tag: '出来高 1.78x / YTD +33.89%',
          body: '一般ソフトウェアETF（IGV：1ヶ月-9.11%）やNASDAQ（QQQ：-9.82%）が売られる中、CIBRは出来高が平均の1.78倍に急増し、今週全米セクターで唯一プラス（+1.19%）を記録しています。'
        },
        cta: {
          headline: '週足判定「買い（Buy）」、日足RSIは46.62と絶好の押し目水準',
          tag: '200SMA(84.92)の遥か上',
          body: '年初来+33.89%の強い上昇トレンドの中で軽く調整し、RSIが46.6まで冷えたところから反発を開始。98.30ドル（日足20SMA）を抜ければ再び高値更新コースです。'
        },
        macro: {
          headline: 'AIエージェント（Anthropic等）が普及するほど、企業のサイバー防衛費は聖域化',
          tag: 'AI時代の必須インフラ',
          body: 'AIによるサイバー攻撃の高度化に伴い、企業も政府もセキュリティ予算だけは絶対に削れません。ハイパースケーラーのような過剰設備投資（減価償却）リスクがないのも強みです。'
        }
      },
      nextAction: '米国テック枠で「半導体・ハイパースケーラー以外」を持つならNo.1の選択肢です。95〜96.5ドルの現在値で第1弾、98.30ドル（20SMA）突破で追加買い。',
      metrics: [
        { label: '今週騰落率 (1W)', value: '+1.19%', sub: '米18セクターで唯一プラス' },
        { label: '年初来 / 6ヶ月', value: '+33.9% / +16.7%', sub: '圧倒的アウトパフォーム' },
        { label: '日足 RSI (14)', value: '46.62', sub: '過熱感ゼロの好位置' },
        { label: '出来高倍率', value: '1.78x', sub: '機関投資家の大口流入' }
      ]
    },
    XLV: {
      region: 'ETF',
      ticker: 'AMEX:XLV',
      title: 'XLV (米ヘルスケアETF)',
      subtitle: 'Health Care Select Sector SPDR • 6M +19.03% • 50日線ピタリ到達',
      assetClass: '💊 米ヘルスケアセクター',
      price: '177.46',
      unit: 'USD',
      change: '-2.05% • 6M +19.03% • YTD +14.59% • 出来高 1.68倍',
      isUp: false,
      shortTitle: '日足50SMA(176.26)＆RSI 41の絶好の押し目！',
      shortPill: 'Buy Dip (50SMA)',
      shortTone: 'success',
      longTitle: 'ハイテクからの恒久的再分配の本命セクター',
      longPill: 'Strong Buy',
      longTone: 'success',
      rangeStatus: '過去6ヶ月で+19.03%上昇した最強ディフェンシブ成長株が、ちょうど日足50SMA(176.26)にタッチ',
      rangePos: '52%',
      rangeLow: '160.76 (日足200SMA)',
      rangeMid: '現在 177.46 (50SMA 176.3)',
      rangeHigh: '184.45 (日足20SMA)',
      lenses: {
        flow: {
          headline: '過去6ヶ月でS&P500(-4.1%)やNASDAQ(-10.2%)を圧倒する「+19.03%」の資金流入！',
          tag: '6ヶ月 +19.03% / 出来高 1.68x',
          body: '多くの個人投資家がAI半導体ばかり見ている間に、プロの機関投資家は半年前からヘルスケア（XLV）に巨額の資金を移し、+19%ものリターンを上げていました。'
        },
        cta: {
          headline: '週足「買い（Buy）」維持のまま、日足50SMA（176.26）とRSI 41.0の黄金押し目に到達',
          tag: '50日線サポート到達！',
          body: '今週の下げで現在値（177.46）が日足50SMA（176.26）のすぐ上まで降りてきて、日足RSIも41.01までクールダウン。出来高1.68倍は機関投資家が50日線で待っていた指値買いが約定しているサインです。'
        },
        macro: {
          headline: '高金利(5%)・景気減速に強く、AI創薬・業務効率化で利益率が上がる「AI活用側」の勝者',
          tag: 'AIユーザー企業の代表',
          body: 'ハイパースケーラーのようにAI開発で巨額の設備投資を強いられる側ではなく、AIを使って創薬コストや事務コストを下げる「恩恵を受ける側」の筆頭セクターです。'
        }
      },
      nextAction: '6ヶ月+19%の強い上昇トレンド銘柄が、ちょうど50日線（176.26ドル）まで押してきた「教科書通りの押し目買いポイント」です。176〜178ドルでのエントリーが極めて有望。',
      metrics: [
        { label: '6ヶ月騰落率', value: '+19.03%', sub: 'QQQ(-10%)に+29%圧勝' },
        { label: '日足 50SMA', value: '176.26', sub: '現在値177.46直下の支持' },
        { label: '日足 RSI (14)', value: '41.01', sub: '押し目買いの理想水準' },
        { label: '出来高倍率', value: '1.68x', sub: '50日線でプロが吸収中' }
      ]
    },
    XLP: {
      region: 'ETF',
      ticker: 'AMEX:XLP',
      title: 'XLP (米生活必需品ETF)',
      subtitle: 'Consumer Staples Select Sector SPDR • 1M +2.33% • YTD +15.64%',
      assetClass: '🛒 米ディフェンシブ株ETF',
      price: '89.86',
      unit: 'USD',
      change: '-1.45% • 1M +2.33% • YTD +15.64% • 出来高 1.46倍',
      isUp: true,
      shortTitle: '20日線(90.14)付近で底堅くプラス圏維持',
      shortPill: 'Defensive Leader',
      shortTone: 'success',
      longTitle: 'VIX 24超えのリスクオフ局面で輝く安定コア',
      longPill: 'Buy',
      longTone: 'success',
      rangeStatus: 'S&P500が1ヶ月で-6.5%下落する中、+2.33%の逆行高！50SMA(86.25)・200SMA(85.01)の遥か上',
      rangePos: '76%',
      rangeLow: '85.01 (日足200SMA)',
      rangeMid: '現在 89.86',
      rangeHigh: '90.14 (日足20SMA)',
      lenses: {
        flow: {
          headline: 'ハイパースケーラーから抜けた保守的年金マネーの「王道シェルター」',
          tag: '1ヶ月 +2.33% / YTD +15.64%',
          body: 'Costco、Walmart、P&G、Coca-Colaなど圧倒的な価格決定力を持つ生活必需品セクター。直近1ヶ月でもS&P500（-6.53%）を約9%アウトパフォームしています。'
        },
        cta: {
          headline: '週足判定「買い（Buy）」、日足RSI 52.37で日足20SMA（90.14）に沿った安定上昇',
          tag: 'ボラティリティ極小',
          body: '50SMA（86.25）と200SMA（85.01）が綺麗な右肩上がりを描き、暴落耐性は全セクター中トップクラスです。'
        },
        macro: {
          headline: 'インフレ・高金利5%でも消費者が削れない必需品＋キャッシュ創出力',
          tag: 'インフレ耐性',
          body: '米10年債利回りが5.05%に高止まりし景気減速懸念が出る局面で、機関投資家が株式ポートフォリオの守りを固めるためにオーバーウェイトしています。'
        }
      },
      nextAction: 'ポートフォリオの変動（ボラティリティ）を抑えつつ年率+15%ペースの着実なリターンを狙う守りのコア枠として、88〜90ドルでの組み入れが有効です。',
      metrics: [
        { label: '1ヶ月騰落率', value: '+2.33%', sub: 'SPY(-6.5%)に+8.8%圧勝' },
        { label: '年初来 (YTD)', value: '+15.64%', sub: 'ハイテク以上の安定成績' },
        { label: '日足 50/200SMA', value: '86.25 / 85.01', sub: '強固な長期サポート' },
        { label: '出来高倍率', value: '1.46x', sub: '機関投資家の逃避資金' }
      ]
    },
    RSP: {
      region: 'ETF',
      ticker: 'AMEX:RSP',
      title: 'RSP (S&P500 均等加重)',
      subtitle: 'Invesco S&P 500 Equal Weight ETF • YTD +10.10% (SPYの2倍超) • 200日線維持',
      assetClass: '⚖️ 米国株・均等加重ETF',
      price: '211.63',
      unit: 'USD',
      change: '-1.76% • 1M -1.03% (SPYに+5.5%圧勝) • 出来高 1.40倍',
      isUp: false,
      shortTitle: '日足200SMA(209.19)の上をしっかり維持！',
      shortPill: 'Hold 200SMA',
      shortTone: 'warning',
      longTitle: '「ハイパースケーラー外し」を1本で実現する新コアETF',
      longPill: 'Core Rotation Buy',
      longTone: 'success',
      rangeStatus: '通常のS&P500(SPY)が1ヶ月-6.53%で200日線を割る中、均等加重のRSPは-1.03%で200日線(209.19)を死守',
      rangePos: '46%',
      rangeLow: '209.19 (日足200SMA)',
      rangeMid: '現在 211.63',
      rangeHigh: '218.54 (日足20SMA)',
      lenses: {
        flow: {
          headline: '★Market Hackの「ハイパースケーラー比率の恒久的引き下げ」を証明する決定的なETF！',
          tag: '1ヶ月 SPY比 +5.50%圧勝',
          body: '通常のS&P500（SPY/IVV/CSPX）は上位のハイパースケーラーに30%集中しているため1ヶ月で-6.53%下落しましたが、500社を0.2%ずつ均等に持つこのRSPはわずか-1.03%（年初来ではSPY +4.4%に対しRSP +10.1%と2倍以上！）と圧倒的な強さを見せています。'
        },
        cta: {
          headline: '日足200SMA（209.19ドル）のすぐ上で推移し、RSIも38.54と絶好の押し目圏',
          tag: '200日線(209.2)サポート',
          body: '現在値211.63は日足200SMA（209.19）の約1%上に位置し、出来高も平均の1.40倍と機関投資家のリバランス買いが入っています。'
        },
        macro: {
          headline: '「AIを作る7社」から「AIを使って利益を増やす残り493社（金融・医薬・資本財）」への主役交代',
          tag: 'S&P 493社の復権',
          body: 'これから数年間、ハイパースケーラーの比重が恒久的に下げられるなら、時価総額加重のSPY/IVVよりも均等加重のRSPの方が長期パフォーマンスで優位に立つ公算が高いです。'
        }
      },
      nextAction: '「米国株インデックスを持ちたいが、ハイパースケーラーの比率引き下げに巻き込まれたくない」という場合の最高の解決策です。209〜212ドル（200日線サポート帯）は絶好の買い場。',
      metrics: [
        { label: '1ヶ月 対SPY差', value: '+5.50%', sub: 'RSP -1.0% vs SPY -6.5%' },
        { label: '年初来 (YTD)', value: '+10.10%', sub: 'SPY(+4.4%)の2倍以上' },
        { label: '日足 200SMA', value: '209.19', sub: '現在値211.63の直下支持' },
        { label: '日足 RSI (14)', value: '38.54', sub: '押し目買いの好水準' }
      ]
    },
    '8058': {
      region: 'JP',
      ticker: 'TSE:8058',
      title: '三菱商事 (8058)',
      subtitle: '総合商社トップ • 年初来 +40.52% • 1兆円自社株買い',
      assetClass: '🇯🇵 日本個別株',
      price: '5,089',
      unit: 'JPY',
      change: '-71 (-1.38%) • 1M +7.25%',
      isUp: false,
      shortTitle: '押し目買い（20日線サポート）',
      shortPill: 'Buy Dip',
      shortTone: 'success',
      longTitle: '強い買い（日足・週足ともにBuy）',
      longPill: 'Strong Buy',
      longTone: 'success',
      rangeStatus: 'すべての主要移動平均線の上で推移するパーフェクトオーダー',
      rangePos: '68%',
      rangeLow: '4,910 (日足50SMA)',
      rangeMid: '現在 5,089',
      rangeHigh: '5,194 (ピボットR2)',
      lenses: {
        flow: {
          headline: '半導体・台湾株(-4.8%)から退避した機関投資家の資金が流入する「受け皿」',
          tag: '1兆円自社株買い',
          body: 'ハイテク・指数ETFが軒並み200日線を割る中、三菱商事は1ヶ月で+7.25%と逆行高。1兆円規模の自社株買いと増配（125円予想）が強力な買い支え（フロア）になっています。'
        },
        cta: {
          headline: 'TradingView判定：日足「買い」・週足「買い（MAは強い買い）」',
          tag: 'パーフェクトオーダー',
          body: '現在値5,089円は日足20EMA（5,084円）・20SMA（5,044円）のすぐ上。50日線（4,910円）・200日線（4,915円）もすべて上向きで、CTAが最も好む上昇波形です。'
        },
        macro: {
          headline: '円安（USDJPY 159.53円）と通期業績上方修正が追い風',
          tag: 'ROE 12.7%目標',
          body: '159円台の円安基調とカナダLNG権益売却（約16億ドル）による資本効率向上で、インフレ・高金利環境に最も強いバリュー株の筆頭です。'
        }
      },
      nextAction: '日本株の中でプロ目線のチャート形状がダントツのNo.1です。5,040〜5,080円（20日線付近）での第1弾エントリー、4,910〜4,950円（50日線）での買い増しが有効。',
      metrics: [
        { label: 'TV判定 (日/週)', value: '買い / 買い', sub: '日本株で最強波形' },
        { label: '日足 20SMA', value: '5,044円', sub: '直下の短期サポート' },
        { label: '日足 50/200MA', value: '4,910円', sub: '強力な下値支持帯' },
        { label: '株主還元', value: '1兆円', sub: '大規模自社株買い' }
      ]
    },
    D05: {
      region: 'SG',
      ticker: 'SGX:D05',
      title: 'DBS Group (D05)',
      subtitle: '東南アジア最大手銀行 • 年初来 +17.98%',
      assetClass: '🇸🇬 シンガポール株',
      price: '66.55',
      unit: 'SGD',
      change: '-1.15 (-1.70%) • 1M -10.12%',
      isUp: false,
      shortTitle: '極度の売られすぎ（反発待ち）',
      shortPill: 'Oversold (RSI 19.9)',
      shortTone: 'warning',
      longTitle: '絶好の分割買いゾーン到達',
      longPill: 'Strong Buy Zone',
      longTone: 'success',
      rangeStatus: '日足200SMA(66.72)＆週足50EMA(65.96)の岩盤帯に到達',
      rangePos: '18%',
      rangeLow: '65.07 (週足50SMA)',
      rangeMid: '現在 66.55',
      rangeHigh: '71.11 (日足20EMA)',
      lenses: {
        flow: {
          headline: '9月最高値（79.05 SGD）からの機関投資家の利益確定が一巡へ',
          tag: 'RSI 19.89 (異常値)',
          body: '日足RSI「19.89」は機関投資家の機械的な売却が限界（クライマックス）に達した時にしか出ない異常な売られすぎ数値です。プロはここから空売りの買い戻しを狙います。'
        },
        cta: {
          headline: '日足200SMA（66.72）と週足50EMA（65.96）が重なる黄金サポート',
          tag: '重要節目に到達',
          body: '現在値66.55 SGDは、日足200SMA（66.72）と週足50EMA（65.96）・週足50SMA（65.07）がわずか1ドルの幅に密集する、年間で最も強いサポートゾーンです。'
        },
        macro: {
          headline: '米金利5.05%高止まりは銀行の純金利マージン(NIM)にプラス！',
          tag: 'Citi目標 78.00 SGD',
          body: 'FRBの利上げ観測（米10年債5.05%）はシンガポール銀行の金利収入を押し上げます。目標株価78ドルに対し66.5ドルは過剰反応で、高配当×押し目買いの好機です。'
        }
      },
      nextAction: '65.0〜66.6 SGDのゾーンは「RSI 19.9 ＋ 週足50MA ＋ 日足200MA」が重なる滅多にない押し目。中長期・高配当狙いなら分割買いの好機です。',
      metrics: [
        { label: '日足 RSI (14)', value: '19.89', sub: '極度の売られすぎ！' },
        { label: '週足 50EMA', value: '65.96', sub: '現在値直下の岩盤' },
        { label: '日足 200SMA', value: '66.72', sub: '現在地と一致' },
        { label: 'Citi目標株価', value: '78.00', sub: '現在値から+17%余地' }
      ]
    },
    AMZN: {
      region: 'US',
      ticker: 'NASDAQ:AMZN',
      title: 'Amazon (AMZN)',
      subtitle: 'Anthropic最大の後ろ盾（1,100億ドルAWS契約）• YTD +11.48%',
      assetClass: '🇺🇸 米国メガテック',
      price: '257.89',
      unit: 'USD',
      change: '+0.14 (+0.05%) • 時間外 260.32 (+0.94%)',
      isUp: true,
      shortTitle: '買い（全主要MAの上を維持）',
      shortPill: 'Buy',
      shortTone: 'success',
      longTitle: '強い買い（Anthropic上場の最大恩恵）',
      longPill: 'Strong Buy',
      longTone: 'success',
      rangeStatus: '市場全体が崩れる中でプラス引け、日足・週足ともにTradingView判定は「買い」',
      rangePos: '72%',
      rangeLow: '247.44 (日足200EMA)',
      rangeMid: '現在 257.89',
      rangeHigh: '260.67 (ピボットR1)',
      lenses: {
        flow: {
          headline: '「Anthropic IPO価格決定迫る」の裏でプロが買っている本命株！',
          tag: 'AWS $110B コミット',
          body: 'AnthropicはAmazon（AWS）に1,100億ドル規模のクラウド計算資源を発注済み。半導体(SOXX -16.7%)からAIソフトへ資金が移る中、プロはAmazonを買い支えています。'
        },
        cta: {
          headline: '日足・週足ともに「買い（Buy）」判定！20・50・100・200日線すべて上向き',
          tag: '相対的強さ (RS) 極大',
          body: 'S&P500が下がる日にプラス引けし、20SMA（256.86）と50SMA（254.81）が綺麗に下値を支える美しい上昇トレンドです。'
        },
        macro: {
          headline: '高金利(米10年債5.05%)にも負けない圧倒的キャッシュフロー',
          tag: 'AIクラウド覇権',
          body: '借入依存の新興AI企業と異なり、AWSの潤沢なキャッシュフローがあるため米金利5%環境でも機関投資家が安心して保有できるコア銘柄です。'
        }
      },
      nextAction: '米国株の中でチャート形状がトップクラスに優秀です。254〜258ドル（20日・50日線サポート帯）での押し目買いが有効。',
      metrics: [
        { label: 'TV判定 (日/週)', value: '買い / 買い', sub: '指数下落に逆行高' },
        { label: '時間外価格', value: '260.32', sub: '+0.94% ブレイク試す' },
        { label: '日足 20/50SMA', value: '256.8 / 254.8', sub: '直下の強力サポート' },
        { label: 'Anthropic関連', value: '$110B', sub: 'AWSクラウド契約残高' }
      ]
    },
    SPCX: {
      region: 'US',
      ticker: 'NASDAQ:SPCX',
      title: 'SpaceX (SPCX)',
      subtitle: 'Space Exploration Technologies • 2026年6月IPO • 時価総額 1.92兆ドル',
      assetClass: '🇺🇸 宇宙・AIインフラ',
      price: '141.70',
      unit: 'USD',
      change: '+4.34 (+3.16%) • 時間外 142.83 (+0.80%)',
      isUp: true,
      shortTitle: '20日線奪還・上値ブレイク待ち',
      shortPill: 'Watch 148.5',
      shortTone: 'warning',
      longTitle: '140ドル前後のベース形成から買い',
      longPill: 'Accumulate',
      longTone: 'success',
      rangeStatus: '市場急落の日に+3.16%の逆行高！日足20SMA(141.27)を奪還し50SMA(148.46)に挑む',
      rangePos: '54%',
      rangeLow: '120.67 (ピボットS1)',
      rangeMid: '現在 141.70',
      rangeHigh: '148.46 (日足50SMA)',
      lenses: {
        flow: {
          headline: 'GS・Apolloによる「400億ドル規模のNVIDIA半導体融資」で資金流入！',
          tag: '1日 +3.16% 逆行高',
          body: 'Starshipを使った「宇宙太陽光AIデータセンター構想」と740億ドル超のAIキャンパス計画で機関投資家の買いを集めています。'
        },
        cta: {
          headline: '日足20SMA（141.27）を突破し、50SMA（148.46）ブレイクを狙う初動',
          tag: '20日線突破',
          body: '終値141.70で日足20EMA・20SMAを上抜け、MACDも買いシグナル点灯。次の関門である50SMA（148.46）を抜けば本格的な上昇波に入ります。'
        },
        macro: {
          headline: 'Starship Flight 15成功でCitiが目標株価を280ドル（約2倍）に引き上げ',
          tag: '目標株価 $280-$345',
          body: 'Citiが目標株価を240→280ドルへ引き上げ、Cantorは345ドルを維持。さらにTeslaとの株式交換による統合観測ニュースも追い風です。'
        }
      },
      nextAction: '140〜142ドル（20日線サポート）で第1弾を仕込み、日足50SMA（148.50ドル）を明確に上抜けたところで買い増す戦略がプロの定石です。',
      metrics: [
        { label: '1日騰落率', value: '+3.16%', sub: '時間外も142.83へ続伸' },
        { label: '日足 20SMA', value: '141.27', sub: '終値で上抜け成功' },
        { label: '日足 50SMA', value: '148.46', sub: 'ブレイク目標ライン' },
        { label: 'Citi目標株価', value: '280.00', sub: '現在値から約2倍余地' }
      ]
    },
    TSLA: {
      region: 'US',
      ticker: 'NASDAQ:TSLA',
      title: 'Tesla (TSLA)',
      subtitle: 'ロボタクシー・Cybercab転換 & SpaceX統合思惑 • 3M +12.16%',
      assetClass: '🇺🇸 米国株・自動運転',
      price: '380.11',
      unit: 'USD',
      change: '+0.37 (+0.10%) • 時間外 385.34 (+1.38%)',
      isUp: true,
      shortTitle: '386ドル上抜けで買いシグナル点灯',
      shortPill: 'Watch 386.3',
      shortTone: 'warning',
      longTitle: '買い（週足Strong Buy・200日線支持）',
      longPill: 'Buy',
      longTone: 'success',
      rangeStatus: '日足200EMA(378.78)と50SMA(375.49)に守られ、時間外で385.34へ急反発中',
      rangePos: '58%',
      rangeLow: '375.49 (日足50SMA)',
      rangeMid: '現在 380.11',
      rangeHigh: '386.26 (日足20SMA)',
      lenses: {
        flow: {
          headline: '「Cybertruck終了→Cybercab量産シフト」と「SpaceX統合思惑」でプロが買い',
          tag: '時間外 +1.38% (385.3)',
          body: '不採算のCybertruckを来年終了し、29,990ドルのロボタクシー（Cybercab）量産へ工場を転換する決断を機関投資家が好感。'
        },
        cta: {
          headline: '375〜382ドルに50日・100日・200日線が密集する「コイルばね」状態',
          tag: '週足判定: 買い (12/14 MA)',
          body: '週足の移動平均線は14本中12本が「買い（Strong Buy）」。20SMA（386.26）を突破すれば上昇が加速します。'
        },
        macro: {
          headline: 'テキサス州でロボタクシー1,306台登録（Waymoに肉薄）',
          tag: '自動運転フリート拡大',
          body: '競合Waymoがカリフォルニア州の規制で高速道路走行を一時停止したのに対し、Teslaは来月から一般オーナー車のロボタクシー試験を開始予定です。'
        }
      },
      nextAction: '375〜380ドル（50日・200日線密集帯）は下値が堅い買い場。386.50ドル（20SMA）を上抜ければ424ドル（R1）に向けた上昇トレンド入りです。',
      metrics: [
        { label: '週足 TV判定', value: '買い', sub: 'MAはStrong Buy' },
        { label: '時間外価格', value: '385.34', sub: '+1.38% (200SMA突破)' },
        { label: '岩盤サポート', value: '375.5-378.8', sub: '50SMA & 200EMA密集' },
        { label: 'ブレイク節目', value: '386.26', sub: '日足20SMA突破で加速' }
      ]
    },
    GOOG: {
      region: 'US',
      ticker: 'NASDAQ:GOOG',
      title: 'Alphabet (GOOG)',
      subtitle: 'Alphabet Class C (Google) • 6M -27.33% • 1M -19.37%',
      assetClass: '🇺🇸 米国メガテック',
      price: '277.60',
      unit: 'USD',
      change: '-3.66 (-1.30%) • 時間外 280.72 (+1.12%)',
      isUp: false,
      shortTitle: '売り・下降トレンド（ナイフ回避）',
      shortPill: 'Sell / Avoid',
      shortTone: 'error',
      longTitle: '底打ち確認待ち（295ドル回復まで待機）',
      longPill: 'Wait Bottom',
      longTone: 'warning',
      rangeStatus: '200日線(335.79)や週足50EMA(315.36)を大きく割り込み、6ヶ月で-27%の調整中',
      rangePos: '22%',
      rangeLow: '250.63 (ピボットS1)',
      rangeMid: '現在 277.60',
      rangeHigh: '295.00 (日足20SMA)',
      lenses: {
        flow: {
          headline: '高値での新株発行 vs 安値での自社株売却という「株主軽視」でプロが離反',
          tag: 'ガバナンス不信 (1M -19.4%)',
          body: '高値圏で新株発行（希薄化）を行いながら、その価格以下で自社株を売るような投資家に泥を塗る資本政策がウォール街の不信感を買い、1兆円自社株買いの三菱商事や堅調なAmazonとは真逆に機関投資家の売却対象になっています。'
        },
        cta: {
          headline: '日足・週足ともに「売り」判定（移動平均線は14本すべてSell）',
          tag: '日足 RSI 31.83',
          body: 'RSIが31.83まで下がり自律反発していますが、20日線（295.00）や50日線（315.08）が頭上に重く垂れ下がっています。'
        },
        macro: {
          headline: '好材料：AnthropicがGoogle Cloud/TPUに「1,213億ドル」の長期利用コミット！',
          tag: '2033年までの巨大受注',
          body: '2033年までに少なくとも1,213億ドルをGoogleの計算資源（TPU）に支払う契約が判明。ガバナンス不信の売りが一巡すれば見直し買いの材料になります。'
        }
      },
      nextAction: 'チャートはまだ明確な下降トレンドです。急いで買わず、日足20SMA（295ドル）を奪還するか、250ドル圏で底固めするのを待つのがプロの鉄則です。',
      metrics: [
        { label: '日足 RSI (14)', value: '31.83', sub: '売られすぎ圏で自律反発' },
        { label: '日足 20SMA', value: '295.00', sub: '最初のトレンド回復条件' },
        { label: '日足 200SMA', value: '335.79', sub: '長期トレンドは下向き' },
        { label: 'Anthropic受注', value: '$121.3B', sub: 'TPUクラウド長期契約' }
      ]
    },
    IVV: {
      region: 'ETF',
      ticker: 'AMEX:IVV',
      title: 'IVV (S&P 500)',
      subtitle: 'iShares Core S&P 500 ETF (米NYSE上場 • 純資産8,606億ドル)',
      assetClass: '🇺🇸 米国株ETF',
      price: '735.70',
      unit: 'USD',
      change: '-7.63 (-1.03%) • 時間外 740.47 (+0.65%)',
      isUp: false,
      shortTitle: '200SMA(735.59)ピタリ防衛・反発兆候',
      shortPill: 'Hold 200SMA',
      shortTone: 'warning',
      longTitle: '728〜735ドルは絶好の分割買い場',
      longPill: 'Buy Zone 1',
      longTone: 'success',
      rangeStatus: '日足200SMA（735.59）で1セント単位のサポート成功、時間外で740ドルへ反発中',
      rangePos: '38%',
      rangeLow: '727.89 (週足50EMA)',
      rangeMid: '現在 735.70',
      rangeHigh: '759.27 (日足20SMA)',
      lenses: {
        flow: {
          headline: 'ヘッジファンドのAI株売りを、個人・長期年金のETF買いが吸収',
          tag: '資金流入継続',
          body: 'ヘッジファンドがAI株のウェイトを落とす一方、長期投資家はIVVなどの低コストS&P500 ETFへ数十億ドル規模の押し目買いを入れています。'
        },
        cta: {
          headline: '日足200SMA（735.59）とピボットS2（734.67）で完璧に下げ止まる',
          tag: '200日線死守！',
          body: '本場米国のIVVは終値735.70で日足200SMA（735.59）を死守し、時間外取引では740.47（+0.65%）へ反発しています。'
        },
        macro: {
          headline: '週足50EMA（727.89）が直下に控え、リスクリワードが極めて良好',
          tag: 'YTD +6.82%',
          body: 'もし11/25の米コアPCE前に再度押しても727〜728ドルの週足50MAが強力なフロアになります。'
        }
      },
      nextAction: '735ドル前後（日足200SMA）で第1弾、万一728ドル（週足50EMA）まで押せば第2弾を入れる戦略が有効です。',
      metrics: [
        { label: '日足 200SMA', value: '735.59', sub: '終値735.70でピタリ支持' },
        { label: '時間外気配', value: '740.47', sub: '+0.65% 反発スタート' },
        { label: '週足 50EMA', value: '727.89', sub: '直下の最終防衛ライン' },
        { label: '日足 RSI (14)', value: '37.45', sub: 'パニック感なし' }
      ]
    },
    CSPX: {
      region: 'ETF',
      ticker: 'LSE:CSPX',
      title: 'CSPX (LSE S&P500)',
      subtitle: 'iShares Core S&P 500 UCITS ETF (LSE上場・配当再投資)',
      assetClass: '🇺🇸 米国株UCITS ETF',
      price: '790.97',
      unit: 'USD',
      change: '-17.44 (-2.16%) • YTD +1.04%',
      isUp: false,
      shortTitle: '様子見（200日線攻防中）',
      shortPill: 'Wait / Sell',
      shortTone: 'error',
      longTitle: '782〜791ドルで分割買い',
      longPill: 'Buy Zone 1',
      longTone: 'warning',
      rangeStatus: '日足200SMA（791.46）をわずかに割り込みテスト中',
      rangePos: '32%',
      rangeLow: '782.63 (週足50EMA)',
      rangeMid: '現在 790.97',
      rangeHigh: '819.98 (日足20SMA)',
      lenses: {
        flow: {
          headline: 'S&P500上位のメガテックからIPO資金へのシフト',
          tag: '米機関投資家リバランス',
          body: 'S&P500の3割以上を占める大型テック株が、Anthropic IPOの資金作りとヘッジファンドの11月決算期リバランスの対象となっています。'
        },
        cta: {
          headline: '日足200SMA（791.46）と週足50EMA（782.63）の挟み撃ち',
          tag: 'TV判定: 強い売り',
          body: '現在値790.97は日足200SMA（791.46）のわずか0.5ドル下。下には強力な週足50EMA（782.63）が控えており、下値余地は限定的です。'
        },
        macro: {
          headline: '非米国居住者にとっては配当課税・米国遺産税メリットが大',
          tag: 'UCITSコア銘柄',
          body: '本場米国のIVVが200日線で反発したため、ロンドン時間でも791.46ドル（200SMA）奪還が見込まれます。'
        }
      },
      nextAction: '790ドル前後（日足200SMA付近）と782ドル前後（週足50EMA）の2段階での押し目買いがプロの王道エントリーです。',
      metrics: [
        { label: '日足 RSI (14)', value: '34.19', sub: '売られすぎ圏接近' },
        { label: '日足 200SMA', value: '791.46', sub: '現在値とほぼ同水準' },
        { label: '週足 50EMA', value: '782.63', sub: '強力な岩盤サポート' },
        { label: '出来高倍率', value: '1.13x', sub: 'パニック売りではない' }
      ]
    },
    VHVE: {
      region: 'ETF',
      ticker: 'LSE:VHVE',
      title: 'VHVE (先進国株)',
      subtitle: 'Vanguard FTSE Developed World UCITS ETF (先進国株)',
      assetClass: '🌍 先進国株ETF',
      price: '145.10',
      unit: 'USD',
      change: '-3.22 (-2.17%) • YTD +6.77%',
      isUp: false,
      shortTitle: '様子見（200日線146.5割れ）',
      shortPill: 'Wait / Sell',
      shortTone: 'error',
      longTitle: '144.2〜145.1で分割買い好機',
      longPill: 'Buy Zone 1',
      longTone: 'warning',
      rangeStatus: '週足50EMA（144.20）のすぐ上まで調整完了',
      rangePos: '30%',
      rangeLow: '144.20 (週足50EMA)',
      rangeMid: '現在 145.10',
      rangeHigh: '146.52 (日足200SMA)',
      lenses: {
        flow: {
          headline: '新興国・台湾株(-4.8%)を含まない分、VWRAより出来高が落ち着いている',
          tag: '出来高 0.79x (低調)',
          body: '今日4.8%急落した台湾株（新興国扱い）を含まない先進国ETFのため、機関投資家の投げ売りが出ておらず安定した値動きです。'
        },
        cta: {
          headline: '週足50EMA（144.20）と週足50SMA（144.64）が直下に待機',
          tag: '週足サポート到達',
          body: '日足200SMA（146.52）は割ったものの、あと0.5〜0.9ドル下に週足の50日移動平均線ペア（144.20〜144.64）が控えています。'
        },
        macro: {
          headline: '中国・台湾・新興国ボラティリティを除外したいプロが選好',
          tag: '先進国コア資産',
          body: '先進国のみのVHVEは中長期の押し目買い対象として非常に安心感があります。'
        }
      },
      nextAction: '144.20〜145.00ドルのゾーンは週足50MAサポート帯のため、中長期の積立・押し目買い第1弾として魅力的な水準です。',
      metrics: [
        { label: '日足 RSI (14)', value: '34.53', sub: '売られすぎ接近' },
        { label: '週足 50EMA', value: '144.20', sub: '直下の強力サポート' },
        { label: '日足 200SMA', value: '146.52', sub: '短期奪還ターゲット' },
        { label: '出来高倍率', value: '0.79x', sub: '売り圧力は限定的' }
      ]
    },
    VWRA: {
      region: 'ETF',
      ticker: 'LSE:VWRA',
      title: 'VWRA (全世界株)',
      subtitle: 'Vanguard FTSE All-World UCITS ETF (全世界株)',
      assetClass: '🌍 全世界株ETF',
      price: '182.18',
      unit: 'USD',
      change: '-3.96 (-2.13%) • YTD +6.64%',
      isUp: false,
      shortTitle: '様子見（200日線割れ直後）',
      shortPill: 'Wait / Sell',
      shortTone: 'error',
      longTitle: '分割買い第1弾（週足50EMA到達）',
      longPill: 'Buy Zone 1',
      longTone: 'warning',
      rangeStatus: '週足50EMA（181.95）の重要サポートに到達',
      rangePos: '28%',
      rangeLow: '175.00 (第2支持)',
      rangeMid: '現在 182.18',
      rangeHigh: '185.05 (200日線)',
      lenses: {
        flow: {
          headline: '大型IPO前のキャッシュ捻出（換金売り）',
          tag: '機関投資家リバランス',
          body: 'Anthropic等の大型IPOに向け、機関投資家が利益の乗った米ハイテク株や台湾TSMC等を一部売却して現金を作る流動性ドレインが発生中。'
        },
        cta: {
          headline: '日足200SMA(185.05)割れ vs 週足50EMA(181.95)',
          tag: 'TV判定: 強い売り',
          body: '200日線を出来高1.65倍で下抜けたためCTAの売りが出ましたが、直下の週足50EMA（181.95）とRSI 33.9で下げ止まりを試しています。'
        },
        macro: {
          headline: 'VIX 24.55と11/25米コアPCE待ち',
          tag: 'リスクオフ警戒',
          body: 'VIXは昨日の25.46から24.55へ小幅低下。11/25の米コアPCE通過でアク抜けが期待されます。'
        }
      },
      nextAction: '長期枠は182ドル前後で第1弾、175〜178ドルで第2弾の分割買い。短期は185.10ドル（200日線）回復まで待機。',
      metrics: [
        { label: '日足 RSI (14)', value: '33.91', sub: '売られすぎ接近' },
        { label: '週足 50EMA', value: '181.95', sub: '現在値直下の支持線' },
        { label: '日足 200SMA', value: '185.05', sub: 'トレンド転換ライン' },
        { label: '出来高倍率', value: '1.65x', sub: '30日平均比' }
      ]
    },
    SOXX: {
      region: 'ETF',
      ticker: 'NASDAQ:SOXX',
      title: 'SOXX (米半導体ETF)',
      subtitle: 'iShares Semiconductor ETF • 1M -16.73% • 日経225の先行指標',
      assetClass: '🇺🇸 半導体セクターETF',
      price: '141.85',
      unit: 'USD',
      change: '+0.39 (+0.28%) • 1M -16.73%',
      isUp: true,
      shortTitle: '売り・調整中（週足50EMA 151.2割れ）',
      shortPill: 'Sector Rotation',
      shortTone: 'error',
      longTitle: '151ドル回復で日本株(1329)も底打ちへ',
      longPill: 'Watch 151.2',
      longTone: 'warning',
      rangeStatus: '1ヶ月で-16.7%急落し200日線(160.77)と週足50EMA(151.22)を下回る',
      rangePos: '24%',
      rangeLow: '89.23 (週足200SMA)',
      rangeMid: '現在 141.85',
      rangeHigh: '151.22 (週足50EMA)',
      lenses: {
        flow: {
          headline: 'まさにあなたの指摘通り！「半導体からAIソフト(Anthropic)への大移動」の震源地',
          tag: '1ヶ月 -16.73% / 6ヶ月 -20%',
          body: '過去1年で+52%暴騰した半導体セクターから、Anthropic IPOに向けた巨額の利益確定売りが出ています。今日台湾株が-4.8%急落したのもこのSOX指数の調整が原因です。'
        },
        cta: {
          headline: '日足200SMA（160.77）も週足50EMA（151.22）も割り込む調整局面',
          tag: '日足 RSI 38.29',
          body: '時間外で143.10（+0.88%）と小反発していますが、頭上の151〜152ドル（週足50EMA・日足20SMA）が重いレジスタンスになっています。'
        },
        macro: {
          headline: '日本株（日経225 / 1329）を買うタイミングを測る「炭鉱のカナリア」',
          tag: '日経225の先行指標',
          body: 'このSOXXが151.22ドル（週足50EMA）を奪還して底打ちしない限り、相関の強い日経225（1329）も本格上昇には戻れません。'
        }
      },
      nextAction: '日本株（1329）や半導体株を狙う場合は、まずこのSOXXが日足20SMA（152.85ドル）・週足50EMA（151.22ドル）を回復するかを先行指標としてウォッチしてください。',
      metrics: [
        { label: '1ヶ月騰落率', value: '-16.73%', sub: 'AIセクター移動の震源' },
        { label: '日足 RSI (14)', value: '38.29', sub: 'まだ底打ち未確認' },
        { label: '週足 50EMA', value: '151.22', sub: '回復の第一関門' },
        { label: '日足 200SMA', value: '160.77', sub: '長期トレンドライン' }
      ]
    },
    FGM: {
      region: 'ETF',
      ticker: 'NASDAQ:FGM',
      title: 'FGM (ドイツ株ETF)',
      subtitle: 'First Trust Germany AlphaDEX Fund • 経費率 0.80%',
      assetClass: '🇩🇪 欧州・ドイツ株ETF',
      price: '57.84',
      unit: 'USD',
      change: '-0.42 (-0.72%) • 6M -10.06%',
      isUp: false,
      shortTitle: '売り・見送り（全移動平均線の下）',
      shortPill: 'Avoid / Sell',
      shortTone: 'error',
      longTitle: '様子見（流動性極薄・経費率高）',
      longPill: 'Low Liquidity',
      longTone: 'error',
      rangeStatus: '日足200SMA（62.93）および週足50EMA（60.64）を大幅に下回る下落トレンド',
      rangePos: '20%',
      rangeLow: '52.11 (週足200EMA)',
      rangeMid: '現在 57.84',
      rangeHigh: '60.64 (週足50EMA)',
      lenses: {
        flow: {
          headline: '純資産わずか2,062万ドル・直近出来高137株と機関投資家が不在',
          tag: '流動性リスク大',
          body: '流動性の薄さと経費率0.80%の高さ（CSPXは0.07%）がネック。大口資金が入っておらず、スプレッドで不利になりやすい銘柄です。'
        },
        cta: {
          headline: '日足・週足ともに「売り」判定、20・50・100・200日線すべてが上値抵抗',
          tag: '下降トレンド継続',
          body: '現在値57.84は日足200SMA（62.93）や週足50EMA（60.64）よりはるか下に位置しています。'
        },
        macro: {
          headline: 'フランス選挙を巡るEU資金調達懸念とドイツ製造業の停滞',
          tag: '11/23 ドイツPMI注目',
          body: '来週11/23（月）のドイツ製造業PMI速報値と60.64ドル（週足50EMA）奪還までは手出し無用です。'
        }
      },
      nextAction: '高コスト（0.80%）かつ下降トレンドのFGMに資金を入れるよりも、米国・先進国（IVV/CSPX/VHVE）や三菱商事・DBSに資金を集中する方が効率的です。',
      metrics: [
        { label: 'TV判定 (日/週)', value: '売り / 売り', sub: '14本中14本のMAが売り' },
        { label: '日足 200SMA', value: '62.93', sub: '現在値より8%上' },
        { label: '経費率 / AUM', value: '0.80%', sub: '純資産 $20.6M (極小)' },
        { label: '直近出来高', value: '137株', sub: '流動性枯渇に注意' }
      ]
    },
    O39: {
      region: 'SG',
      ticker: 'SGX:O39',
      title: 'OCBC Bank (O39)',
      subtitle: 'オーバーシー・チャイニーズ銀行 • 1年 +49.05%',
      assetClass: '🇸🇬 シンガポール株',
      price: '27.36',
      unit: 'SGD',
      change: '-0.32 (-1.16%) • YTD +38.13%',
      isUp: false,
      shortTitle: '様子見（26ドル台前半待ち）',
      shortPill: 'Wait',
      shortTone: 'warning',
      longTitle: '26.0〜26.5 SGDへの押し目待ち',
      longPill: 'Hold / Wait Dip',
      longTone: 'warning',
      rangeStatus: '200日線（26.01〜26.47）の上で推移も、D05より割高感',
      rangePos: '42%',
      rangeLow: '26.01 (日足200SMA)',
      rangeMid: '現在 27.36',
      rangeHigh: '28.52 (日足20SMA)',
      lenses: {
        flow: {
          headline: '過去1年で+49%急騰した後のスピード調整（出来高0.44倍と閑散）',
          tag: '出来高 0.44x',
          body: '11/6の好決算で大きく買われた反動。出来高は平均の半分以下（0.44倍）で、大口の投げ売りは出ていません。'
        },
        cta: {
          headline: 'D05と違い、200日線（26.47）までまだ約3.5%の下値余地',
          tag: 'RSI 30.96',
          body: '日足200EMA（26.47）・200SMA（26.01）はまだ下にあり、テクニカルな下値支持は26ドル台前半です。'
        },
        macro: {
          headline: 'Citiの目標株価（25.30 SGD）を現在値が上回っている点に注意',
          tag: 'バリュエーション比較',
          body: '同じシンガポール銀行を買うなら、今はD05（DBS）の方がプロ目線での割安感・反発期待が上です。'
        }
      },
      nextAction: '今すぐ新規で買うならOCBC（O39）よりDBS（D05）が優位。O39を買う場合は200日線がある26.00〜26.50 SGDまで引きつけてから。',
      metrics: [
        { label: '日足 RSI (14)', value: '30.96', sub: '売られすぎ圏入口' },
        { label: '日足 200EMA', value: '26.47', sub: '第1押し目ターゲット' },
        { label: '1年騰落率', value: '+49.05%', sub: '大幅上昇後の調整' },
        { label: '出来高倍率', value: '0.44x', sub: '売り圧力は弱い' }
      ]
    },
    '1364': {
      region: 'JP',
      ticker: 'TSE:1364',
      title: '1364 (JPX日経400)',
      subtitle: 'iシェアーズ JPX日経400 ETF • 高ROE優良株厳選',
      assetClass: '🇯🇵 日本株ETF',
      price: '3,592',
      unit: 'JPY',
      change: '-8 (-0.22%) • 1M -4.57%',
      isUp: false,
      shortTitle: '200EMA上で底堅い推移',
      shortPill: 'Hold / Neutral',
      shortTone: 'warning',
      longTitle: '日本株ETF 3本の中で最も底堅い',
      longPill: 'Quality Pick',
      longTone: 'success',
      rangeStatus: '日足200EMA（3,589）と週足50SMA（3,585）の真上でピタリと止まる',
      rangePos: '45%',
      rangeLow: '3,542 (週足50EMA)',
      rangeMid: '現在 3,592',
      rangeHigh: '3,637 (日足200SMA)',
      lenses: {
        flow: {
          headline: '高ROE・好業績銘柄が集まるため、下落局面での耐性が最強',
          tag: '1ヶ月 -4.57% (最小)',
          body: '1329（-7.77%）、1475（-4.97%）と比較して下落幅が最も小さく、誰も慌てて売っていない状態です。'
        },
        cta: {
          headline: '週足判定は「中立（Neutral）」を維持、日足200EMA（3,589）を死守',
          tag: '週足 Neutral',
          body: '日足200EMA（3,589円）と週足50SMA（3,585円）を割り込まずに維持しています。'
        },
        macro: {
          headline: '資本効率（ROE）と株主還元を重視する海外投資家のコア銘柄群',
          tag: 'ガバナンス銘柄',
          body: '三菱商事のような高収益・高還元企業が中心のため、相場全体の調整が終われば真っ先に高値を更新しやすい構造です。'
        }
      },
      nextAction: 'チャート形状は日本株ETFの中で一番綺麗です。ただし1日の出来高がやや少ないため、成行ではなく3,585〜3,595円の「指値」で買うのがプロの鉄則です。',
      metrics: [
        { label: '週足 TV判定', value: '中立', sub: '指数ETFで唯一の底堅さ' },
        { label: '日足 200EMA', value: '3,589円', sub: '現在値(3,592)で支持' },
        { label: '週足 50SMA', value: '3,585円', sub: '強固なダブルサポート' },
        { label: '注意点', value: '指値必須', sub: '出来高が薄いため' }
      ]
    },
    '1475': {
      region: 'JP',
      ticker: 'TSE:1475',
      title: '1475 (TOPIX ETF)',
      subtitle: 'iシェアーズ・コア TOPIX ETF • 純資産 3.0兆円',
      assetClass: '🇯🇵 日本株ETF',
      price: '396.3',
      unit: 'JPY',
      change: '-1.9 (-0.48%) • 1M -4.97%',
      isUp: false,
      shortTitle: '週足50EMA（392.6）の攻防',
      shortPill: 'Watch 392.6',
      shortTone: 'warning',
      longTitle: '392〜396円で分割買い検討',
      longPill: 'Buy Zone 1',
      longTone: 'warning',
      rangeStatus: '日足200EMA（398.1）直下・週足50EMA（392.6）のすぐ上で踏ん張る',
      rangePos: '36%',
      rangeLow: '392.6 (週足50EMA)',
      rangeMid: '現在 396.3',
      rangeHigh: '403.2 (日足200SMA)',
      lenses: {
        flow: {
          headline: '出来高1.75倍に急増＝機関投資家のリバランス売買が活発',
          tag: '出来高 1.75x (活況)',
          body: '396円付近で出来高が30日平均の1.75倍に膨らんでおり、週足50EMA付近で拾いたい長期機関投資家の実需が入っています。'
        },
        cta: {
          headline: '日足200EMA（398.1）と週足50EMA（392.6）の狭いサポート帯',
          tag: '下値抵抗が強い',
          body: '日経225（1329）と違い、TOPIX（1475）は週足50EMA（392.6円）をしっかりキープしています。'
        },
        macro: {
          headline: '日本の10年債利回り2.835%＆日銀利上げ姿勢はTOPIX内の銀行株に追い風',
          tag: '金利ある世界',
          body: '明日11/20(金)の10月全国CPIでインフレが確認されれば、メガバンクや商社比率の高いTOPIXには下支え要因になります。'
        }
      },
      nextAction: '392.6円（週足50EMA）〜396円のゾーンは長期積立・押し目買いの第1弾として好位置。金曜のCPI通過後の403円奪還で追加買い。',
      metrics: [
        { label: '日足 RSI (14)', value: '39.9', sub: '中立〜やや売られすぎ' },
        { label: '週足 50EMA', value: '392.6円', sub: '現在値直下の支持線' },
        { label: '日足 200SMA', value: '403.2円', sub: '上抜けでトレンド回復' },
        { label: '出来高倍率', value: '1.75x', sub: '機関投資家の攻防' }
      ]
    },
    '1329': {
      region: 'JP',
      ticker: 'TSE:1329',
      title: '1329 (日経225 ETF)',
      subtitle: 'iシェアーズ・コア 日経225 ETF • 信託報酬 0.05%',
      assetClass: '🇯🇵 日本株ETF',
      price: '6,160',
      unit: 'JPY',
      change: '+12 (+0.20%) • 1M -7.77%',
      isUp: true,
      shortTitle: '様子見（半導体・台湾株急落の重し）',
      shortPill: 'Wait / Sell',
      shortTone: 'error',
      longTitle: '1475/1364より出遅れ（6,250回復待ち）',
      longPill: 'Wait 6,250',
      longTone: 'warning',
      rangeStatus: '日足200SMA（6,469）だけでなく週足50EMA（6,249）も下回る',
      rangePos: '25%',
      rangeLow: '5,824 (ピボットS2)',
      rangeMid: '現在 6,160',
      rangeHigh: '6,249 (週足50EMA)',
      lenses: {
        flow: {
          headline: '韓国・台湾株(今日-4.8%)と一緒に買われすぎた反動＋SOX指数連動で回復に時間',
          tag: '東アジア半導体バスケット調整',
          body: '海外勢が韓国・台湾株とセットで買い上げた反動が直撃。米SOXX（1ヶ月-16.7%）が底打ちしてから日本の半導体製造装置へ資金が戻るため、本格上昇までには日柄（時間）がかかります。'
        },
        cta: {
          headline: '週足50EMA（6,249円）を割り込んでいる点がテクニカルの弱み',
          tag: 'TV判定: 売り',
          body: 'TOPIX（1475）やJPX400（1364）が週足50EMAの上を維持しているのに対し、1329は週足50EMA（6,249円）も下抜けています。'
        },
        macro: {
          headline: 'ドル円159.53円の円安が下支えも、明日11/20（金）の全国CPI待ち',
          tag: '金曜CPI注目',
          body: '159円台の円安と日本の機械受注（Q4見通し+4.3%）が支えですが、まずSOXXの下げ止まり確認が必要です。'
        }
      },
      nextAction: '日本株インデックスを買うなら、今は1329（日経225）よりも銀行・商社を含む1475（TOPIX）や1364（JPX400）の方が底堅く有利です。',
      metrics: [
        { label: '日足 RSI (14)', value: '37.0', sub: '弱含み推移' },
        { label: '週足 50EMA', value: '6,249円', sub: 'まず奪還すべき節目' },
        { label: '日足 200SMA', value: '6,469円', sub: '本格トレンド転換線' },
        { label: '1ヶ月騰落率', value: '-7.77%', sub: 'TOPIX(-4.9%)に劣後' }
      ]
    },
    TLT: {
      region: 'BOND',
      ticker: 'NASDAQ:TLT',
      title: 'TLT (米20年超国債)',
      subtitle: 'iShares 20+ Year Treasury Bond ETF • 米10年債利回り 5.052%',
      assetClass: '🏦 米国長期債ETF',
      price: '80.22',
      unit: 'USD',
      change: '+0.67 (+0.84%) • 米10年債金利 5.052%',
      isUp: true,
      shortTitle: '日足50SMA(80.07)上で底打ち反発開始',
      shortPill: 'Bounce 80.0',
      shortTone: 'warning',
      longTitle: '米金利5%超は長期ロックインの好機',
      longPill: 'Yield Lock-in',
      longTone: 'success',
      rangeStatus: '米10年債利回りが5.05%に達する中、TLTは80.07(日足50SMA)で底堅く+0.84%反発',
      rangePos: '34%',
      rangeLow: '78.50 (直近底値圏)',
      rangeMid: '現在 80.22',
      rangeHigh: '84.19 (日足200SMA)',
      lenses: {
        flow: {
          headline: '米10年債利回り「5.052%」は年金・保険など長期機関投資家が債券を買い始める水準',
          tag: '米10年債 5.052%',
          body: 'ウォーシュFRB議長下のタカ派発言（ウォラー理事の12月利上げ支持）で米2年債(4.789%)・10年債(5.052%)が上昇しましたが、5%超の利回りは長期資金にとって極めて魅力的です。'
        },
        cta: {
          headline: '日足50SMA（80.07ドル）を奪還し、5日間で+1.16%と底入れの兆し',
          tag: '80ドル大台サポート',
          body: '株やコモディティが荒れる中、TLTは80.07ドル（日足50SMA）の上を回復し、日足20SMA（81.06）〜200SMA（84.19）に向けたリバウンドを試しています。'
        },
        macro: {
          headline: '原油(-16.7%)と銅(-13.5%)の急落＝将来のインフレ鈍化（債券高）の先行サイン',
          tag: 'インフレピークアウト兆候',
          body: '今日ロイターも「原油安で米利回りが低下」と報道。資源価格の下落は数ヶ月後のCPI/PCEを押し下げるため、米金利5%台での債券仕込みは理にかなっています。'
        }
      },
      nextAction: '株式のヘッジ（保険）兼・高利回りロックインとして、80ドル前後での分割買い第1弾が有効。81.10ドル（20SMA）突破で底打ち確定へ。',
      metrics: [
        { label: '米10年債利回り', value: '5.052%', sub: '機関投資家の買い目線' },
        { label: '米2年債利回り', value: '4.789%', sub: '長短金利差 +26.3bps' },
        { label: '日本10年債利回り', value: '2.835%', sub: '日米金利差は約2.2%' },
        { label: '日足 50SMA', value: '80.07', sub: '現在値直下のサポート' }
      ]
    },
    IEF: {
      region: 'BOND',
      ticker: 'NASDAQ:IEF',
      title: 'IEF (米7-10年国債)',
      subtitle: 'iShares 7-10 Year Treasury Bond ETF • 中期米国債コア',
      assetClass: '🏦 米国中期債ETF',
      price: '90.67',
      unit: 'USD',
      change: '+0.26 (+0.29%) • 1M +0.39%',
      isUp: true,
      shortTitle: '90.47(日足50SMA)サポートで安定',
      shortPill: 'Stable Hold',
      shortTone: 'warning',
      longTitle: '低ボラティリティの債券コア枠',
      longPill: 'Accumulate',
      longTone: 'success',
      rangeStatus: 'TLTより値動きがマイルドで、日足50SMA（90.47）の上を着実にキープ',
      rangePos: '40%',
      rangeLow: '89.50 (下値支持)',
      rangeMid: '現在 90.67',
      rangeHigh: '93.55 (日足200SMA)',
      lenses: {
        flow: {
          headline: '株式のボラティリティ（VIX 24.55）を避けたい保守的資金の待機場所',
          tag: '5日 +0.71%',
          body: 'S&P500が5日で-3.85%調整する中、IEFは+0.71%とプラスを維持し、本来の「株安時のクッション（分散効果）」を発揮し始めています。'
        },
        cta: {
          headline: '日足50SMA（90.47）がサポート、日足20SMA（91.09）突破目前',
          tag: 'RSI 48.38 (中立)',
          body: '91.10ドルを上抜けると日足200SMA（93.55ドル）に向けた穏やかな回復トレンドに入ります。'
        },
        macro: {
          headline: '11/25の米コアPCEが予想通りなら、中期債に買い戻しが入る公算',
          tag: '11/25 PCE注目',
          body: '20年超のTLTほど金利変動リスクを取りたくない場合、7-10年債のIEFが最もバランスの良い債券ETFです。'
        }
      },
      nextAction: 'ポートフォリオの守りを固める債券枠として90.0〜90.7ドルで安定的に組み入れ可能。より大きな反発値幅を狙うならTLT、安定重視ならIEF。',
      metrics: [
        { label: '日足 50SMA', value: '90.47', sub: '現在値90.67を下支え' },
        { label: '日足 200SMA', value: '93.55', sub: '中期回復ターゲット' },
        { label: '日足 RSI (14)', value: '48.38', sub: '落ち着いた値動き' },
        { label: '5日間騰落率', value: '+0.71%', sub: '株安局面で逆行プラス' }
      ]
    },
    GOLD: {
      region: 'COMMODITY',
      ticker: 'TVC:GOLD',
      title: 'GOLD (金スポット)',
      subtitle: 'Spot Gold (XAU/USD) • 1M -10.39% • 14ヶ月ぶり安値圏から反発模索',
      assetClass: '🪙 貴金属・コモディティ',
      price: '3,711.38',
      unit: 'USD',
      change: '-13.72 (-0.37%) • 日足RSI 29.34',
      isUp: false,
      shortTitle: 'RSI 29.3 売られすぎ（3,609〜3,700模索）',
      shortPill: 'Oversold (RSI 29)',
      shortTone: 'warning',
      longTitle: '3,610〜3,710ドルで逆張り分割買い',
      longPill: 'Contrarian Buy',
      longTone: 'warning',
      rangeStatus: 'ドル高(DXY 103.97)と米金利5%で1ヶ月-10.4%急落し、ついに日足RSIが30割れ(29.34)へ到達',
      rangePos: '20%',
      rangeLow: '3,609 (テクニカル下値目標)',
      rangeMid: '現在 3,711',
      rangeHigh: '3,959 (日足20SMA)',
      lenses: {
        flow: {
          headline: '貴金属市場全体で3.3兆ドルの時価総額減少＝機関投資家の換金売りがクライマックスへ',
          tag: '日足 RSI 29.34！',
          body: '米金利5.05%とドル指数103.97（19ヶ月高値）を受け、レバレッジ筋の投げ売りが出ました。しかし日足RSIが30を割る（29.34）のは歴史的にも「売りの最終局面」です。'
        },
        cta: {
          headline: '3,693ドルで14ヶ月ぶり安値をつけた後、3,711ドルへ下げ渋り',
          tag: '下値ターゲット 3,609',
          body: 'ロイターのテクニカル分析では「3,609ドル付近が最終下値メド」。また超長期の岩盤である週足200SMA（3,040ドル）は依然として力強い上昇トレンドを維持しています。'
        },
        macro: {
          headline: '米・イラン緊張（「ディール不要」発言）と欧州財政リスクは消えていない',
          tag: '地政学ヘッジ',
          body: 'ドル高が一服した瞬間に最も鋭く自律反発するのがRSI 30割れのゴールドです。'
        }
      },
      nextAction: '一気に全力で買わず、①現在の3,700〜3,715ドル（RSI 29.3）で打診買い第1弾、②もし3,610ドル付近まで最後の突っ込みがあれば第2弾を入れる逆張り分割戦略が有効です。',
      metrics: [
        { label: '日足 RSI (14)', value: '29.34', sub: '30割れの売られすぎ圏！' },
        { label: '1ヶ月騰落率', value: '-10.39%', sub: 'ドル高による急調整' },
        { label: '短期下値メド', value: '3,609', sub: 'ロイター算出サポート' },
        { label: '日足 20SMA', value: '3,959', sub: '反発時の戻り目標' }
      ]
    },
    USOIL: {
      region: 'COMMODITY',
      ticker: 'TVC:USOIL',
      title: 'WTI原油 (USOIL)',
      subtitle: 'WTI Crude Oil • 1M -16.69% • YTD +42.55% • インフレ鎮静化の鍵',
      assetClass: '🪙 エネルギー・原油',
      price: '81.95',
      unit: 'USD',
      change: '+0.05 (+0.06%) • 先物 81.83 (-0.58%)',
      isUp: true,
      shortTitle: '下降トレンド（77〜78ドル模索）',
      shortPill: 'Weak / 77-78目標',
      shortTone: 'error',
      longTitle: '原油安は「株・債券」にとって最大の朗報！',
      longPill: 'Macro Indicator',
      longTone: 'warning',
      rangeStatus: '日足200SMA（87.92）を割り込み1ヶ月で-16.7%下落。77〜78ドルのサポート帯を試す展開',
      rangePos: '25%',
      rangeLow: '77.04 (下値サポート目標)',
      rangeMid: '現在 81.95',
      rangeHigh: '87.92 (日足200SMA)',
      lenses: {
        flow: {
          headline: '米国の原油・ガソリン在庫が予想以上に増加し、供給過剰懸念でファンドが手仕舞い',
          tag: '1ヶ月 -16.69%',
          body: '中東の地政学リスクで年初来+42.5%上がっていた原油ですが、足元では在庫増と中国需要の鈍化からロングポジションの解消（利益確定売り）が続いています。'
        },
        cta: {
          headline: '日足200SMA（87.92ドル）を下抜け、日足RSIは32.81まで低下',
          tag: '77.04-78.18が下値メド',
          body: 'テクニカルには77.04〜78.18ドルのサポートゾーンまであと4〜5ドルの下値余地があります（USO ETFでは週足50EMAが守られています）。'
        },
        macro: {
          headline: '★プロの見方：原油が80ドル割れに向かうことは「FRBの利上げ懸念」を消す特効薬！',
          tag: 'インフレ鎮静化',
          body: '原油自体を買う局面ではありませんが、原油が下がることで米10年債利回り（5.05%）の上昇が止まり、S&P500（IVV/CSPX）やハイテク株の追い風になります。'
        }
      },
      nextAction: '原油そのものの新規買いは77〜78ドル到達まで様子見。マクロ指標として「原油安＝株と米国債（TLT）の買いサイン」として活用するのがプロの視点です。',
      metrics: [
        { label: '日足 RSI (14)', value: '32.81', sub: '売られすぎに接近' },
        { label: '日足 200SMA', value: '87.92', sub: '現在は200日線の下' },
        { label: '下値ターゲット', value: '77.0-78.2', sub: '次の主要サポート帯' },
        { label: 'マクロ影響', value: 'インフレ鈍化', sub: '株・債券には追い風' }
      ]
    },
    CPER: {
      region: 'COMMODITY',
      ticker: 'AMEX:CPER',
      title: 'CPER (銅 / Dr.Copper)',
      subtitle: 'US Copper Index Fund • 先物 5.65 USD/lb • 世界景気の先行指標',
      assetClass: '🪙 産業金属・コモディティ',
      price: '34.10',
      unit: 'USD',
      change: '-1.89 (-5.25%) • 日足RSI 23.47',
      isUp: false,
      shortTitle: '極度の売られすぎ（RSI 23.5）',
      shortPill: 'Oversold (RSI 23.5)',
      shortTone: 'warning',
      longTitle: 'AIデータセンター電力網の長期テーマ',
      longPill: 'Watch Rebound',
      longTone: 'warning',
      rangeStatus: '1ヶ月で-13.5%急落し、銅先物(RSI 22.9)・CPER(RSI 23.5)ともに売られすぎ極致に到達',
      rangePos: '19%',
      rangeLow: '29.31 (週足200SMA)',
      rangeMid: '現在 34.10',
      rangeHigh: '37.95 (日足200SMA)',
      lenses: {
        flow: {
          headline: '「ドクター・カッパー（銅）」の急落は、世界経済の減速とインフレ鎮静化を示唆',
          tag: '先物 RSI 22.93',
          body: '中国の鉱工業生産（+4.8%・予想割れ）とドル高を受け、景気に最も敏感な銅が売られました。プロはこれを見て「FRBはこれ以上強く利上げできない」と判断します。'
        },
        cta: {
          headline: '日足RSI「23.47（先物は22.93）」はDBS銀行(D05)と並ぶ売られすぎの極致',
          tag: '短期リバウンド圏',
          body: '日足200SMA（37.95）や週足50EMA（36.92）から大きく下に乖離しており、いつショートカバー（買い戻し）が入ってもおかしくない水準です。'
        },
        macro: {
          headline: '中長期ではAIデータセンター・EV・送電網に不可欠な戦略物資',
          tag: '電化・AIインフラ',
          body: 'SpaceXやAmazonの巨大AIデータセンター建設には膨大な銅が必要です。投げ売りが止まった後の反発力は大きいアセットです。'
        }
      },
      nextAction: 'マクロ温度計として最重要。RSI 23台まで売られたため、33〜34ドル圏で下げ止まり陽線が出れば、37ドル（週足50EMA）に向けた短期リバウンド狙いが可能です。',
      metrics: [
        { label: '日足 RSI (14)', value: '23.47', sub: '先物は22.9の極限値' },
        { label: '銅先物 (HG1!)', value: '5.65 USD', sub: '1ヶ月 -14.18%' },
        { label: '週足 50EMA', value: '36.92', sub: '反発時の戻りメド' },
        { label: '日足 200SMA', value: '37.95', sub: '長期トレンド節目' }
      ]
    },
    USDJPY: {
      region: 'FX',
      ticker: 'FX:USDJPY',
      title: 'USD/JPY (ドル円)',
      subtitle: '米ドル / 日本円 • 米10年債5.05% vs 日銀利上げ警戒（明日日本CPI）',
      assetClass: '💱 為替 FX',
      price: '159.53',
      unit: 'JPY',
      change: '+0.22 (+0.14%) • 200日線(158.80)上維持',
      isUp: true,
      shortTitle: '強い買いトレンドも160円介入・金曜CPI警戒',
      shortPill: 'Strong Buy (160警戒)',
      shortTone: 'warning',
      longTitle: '157.8〜158.8円サポートでの押し目買い',
      longPill: 'Buy on Dip',
      longTone: 'success',
      rangeStatus: '日足・週足ともにTradingView判定は「強い買い」！20・50・200日線すべての上で160円に迫る',
      rangePos: '78%',
      rangeLow: '157.82 (日足50SMA)',
      rangeMid: '現在 159.53',
      rangeHigh: '160.00 (心理的節目・介入警戒)',
      lenses: {
        flow: {
          headline: '米2年債・10年債利回りの上昇と「19ヶ月ぶりのドル高(DXY 103.97)」が牽引',
          tag: 'TV判定: 強い買い (15/0)',
          body: 'ウォーシュFRBのタカ派姿勢（12月利上げ観測）により日米金利差が再び意識され、ドル買い・円売りのモメンタムが非常に強い状態です。'
        },
        cta: {
          headline: '日足200SMA（158.80）・20SMA（158.48）・週足50EMA（157.30）が全て下値支持',
          tag: 'パーフェクトオーダー',
          body: '移動平均線は日足15本中15本すべてが「買い（Strong Buy）」。ただし160.00円の大台は政府・日銀の為替介入やオプション防戦売りが出やすい壁です。'
        },
        macro: {
          headline: '明日 11/20（金）の「日本10月全国CPI」が最大のイベント！',
          tag: '明日 日本CPI発表',
          body: 'Mace Newsでも「10月CPIはインフレ加速予想」と報じられており、もしCPIが強く上振れれば日銀の利上げ観測から158円台前半への押し目を作る可能性があります。'
        }
      },
      nextAction: '160円直前での高値掴みは避け、明日金曜の日本CPI発表後に157.80〜158.80円（50日・200日線サポート帯）へ押したところを拾うのがプロの戦い方です。',
      metrics: [
        { label: 'TV判定 (日/週)', value: '強い買い', sub: 'MA 15本すべてBuy' },
        { label: '日足 200SMA', value: '158.80円', sub: '直下の強力サポート' },
        { label: '週足 50EMA', value: '157.30円', sub: '中期の下値防衛線' },
        { label: '日足 RSI (14)', value: '59.88', sub: '過熱感はまだ余地あり' }
      ]
    },
    USDSGD: {
      region: 'FX',
      ticker: 'FX_IDC:USDSGD',
      title: 'USD/SGD (ドルSGD)',
      subtitle: '米ドル / シンガポールドル • シンガポールから米国株(USD)を買う為替レート',
      assetClass: '💱 為替 FX',
      price: '1.2904',
      unit: 'SGD',
      change: '+0.0010 (+0.08%) • 1M +0.87%',
      isUp: true,
      shortTitle: 'ドル高優勢（RSI 66.5 やや過熱）',
      shortPill: 'Strong USD',
      shortTone: 'warning',
      longTitle: '1.280付近への押し目でSGD→USD両替が有利',
      longPill: 'Convert on Dip',
      longTone: 'success',
      rangeStatus: '日足200SMA(1.2796)を上抜け1.2904へ上昇。週足200SMA(1.3173)が上値キャップ',
      rangePos: '74%',
      rangeLow: '1.2796 (日足200SMA)',
      rangeMid: '現在 1.2904',
      rangeHigh: '1.3173 (週足200SMA)',
      lenses: {
        flow: {
          headline: '米ドル一強（DXY 103.97）により、堅調なシンガポールドルに対しても米ドルが上昇',
          tag: 'TV判定: 強い買い',
          body: 'アジア通貨全体が売られる中、MAS（シンガポール金融管理局）の管理下でSGDは健闘していますが、それでも米金利5%の影響で1.28→1.29台へ米ドル高が進んでいます。'
        },
        cta: {
          headline: '日足RSIは66.50と買われすぎ（70）に接近、1.280〜1.283に20/50/200日線が密集',
          tag: 'サポート 1.2800',
          body: '1.2796〜1.2828に日足20・50・200SMAがすべて集まっており、ここが強力なサポート帯になっています。'
        },
        macro: {
          headline: '★実践活用：手元のSGDを米ドル(USD)に替えてVWRA/CSPX/AMZNを買うタイミング',
          tag: '両替タイミング判定',
          body: '現在（1.2904）は短期的に少し米ドルが高め（RSI 66.5）です。もしSGD建てのDBS銀行（D05：66.55 SGD）を買うなら為替損なしで今すぐ買えます！USD株を買うための大口両替は1.280〜1.283への押し目がベストです。'
        }
      },
      nextAction: '今すぐSGD資金を動かすなら、両替不要で極度の売られすぎにある「DBS銀行（D05）」が最適。米ドルへの両替は1.29台で半分、1.280前後への押し目で残り半分が賢明です。',
      metrics: [
        { label: '現在レート', value: '1.2904', sub: '1 USD = 1.2904 SGD' },
        { label: '日足 RSI (14)', value: '66.50', sub: '70(ドル買われすぎ)接近' },
        { label: '日足 200SMA', value: '1.2796', sub: '絶好のUSD両替目安' },
        { label: '週足 200SMA', value: '1.3173', sub: '長期のドル上値抵抗' }
      ]
    },
    SGDJPY: {
      region: 'FX',
      ticker: 'FX_IDC:SGDJPY',
      title: 'SGD/JPY (SGD円)',
      subtitle: 'シンガポールドル / 日本円 • SGDから日本株(8058/1364)を買う為替レート',
      assetClass: '💱 為替 FX',
      price: '123.63',
      unit: 'JPY',
      change: '+0.08 (+0.07%) • 1Y +3.57%',
      isUp: true,
      shortTitle: '200日線(124.04)直下の安定レンジ',
      shortPill: 'Stable Range',
      shortTone: 'success',
      longTitle: 'SGDからの日本株(三菱商事等)投資に好環境',
      longPill: 'Favorable FX',
      longTone: 'success',
      rangeStatus: '日足20SMA(123.50)と日足200SMA(124.04)の間の非常に落ち着いた高値安定レンジ',
      rangePos: '62%',
      rangeLow: '122.56 (週足50EMA)',
      rangeMid: '現在 123.63',
      rangeHigh: '124.04 (日足200SMA)',
      lenses: {
        flow: {
          headline: '購買力平価から見てSGDは対円で歴史的な強さ（1 SGD = 123.6円）を維持',
          tag: 'TV判定: 買い',
          body: 'シンガポールドルの通貨としての強さにより、123円台後半の高い購買力をキープしています。'
        },
        cta: {
          headline: 'RSI 51.5（完全な中立）、週足50EMA（122.56円）と週足50SMA（123.62円）が下支え',
          tag: 'ボラティリティ低',
          body: 'ドル円（USD/JPY）よりも値動きがマイルドで、日足200SMA（124.04円）を抜けるとさらなるSGD高・円安トレンドに入ります。'
        },
        macro: {
          headline: '★実践活用：強いSGDを活かして日本の優良株（三菱商事 8058 / JPX400 1364）を買うメリット',
          tag: 'クロスボーダー戦略',
          body: '明日11/20(金)の日本CPIで一時的に円高（122円台半ば）に振れる場面があれば、円転・日本株買い増しの絶好のチャンスになります。'
        }
      },
      nextAction: '1 SGD = 123.6円とSGDの購買力が非常に強いため、日本株No.1の三菱商事（8058）や1364を買う環境として引き続き有利です。',
      metrics: [
        { label: '現在レート', value: '123.63円', sub: '1 SGD = 123.63 JPY' },
        { label: '日足 RSI (14)', value: '51.53', sub: '過熱感なしの安定推移' },
        { label: '日足 200SMA', value: '124.04円', sub: '上抜けでSGD高加速' },
        { label: '週足 50EMA', value: '122.56円', sub: '押し目サポート水準' }
      ]
    },
    DXY: {
      region: 'FX',
      ticker: 'TVC:DXY',
      title: 'DXY (米ドル指数)',
      subtitle: 'US Dollar Index • 19ヶ月ぶり高値 • 全アセットを動かす最重要マクロ温度計',
      assetClass: '💱 マクロ基軸通貨',
      price: '103.97',
      unit: 'INDEX',
      change: '+0.15 (+0.15%) • 6M +4.80% • 日足RSI 71.3',
      isUp: true,
      shortTitle: '買われすぎ圏（RSI 71.3）ピーク接近',
      shortPill: 'Overbought (RSI 71)',
      shortTone: 'warning',
      longTitle: '104.0前後でドル高一服なら株・金が一斉反発へ！',
      longPill: 'Macro Pivot',
      longTone: 'warning',
      rangeStatus: '日足RSI 71.3・週足RSI 70.2と「ドル買われすぎ（70超え）」に到達！104の節目で天井を打つか注目',
      rangePos: '88%',
      rangeLow: '101.79 (日足50SMA)',
      rangeMid: '現在 103.97',
      rangeHigh: '104.50 (19ヶ月高値抵抗帯)',
      lenses: {
        flow: {
          headline: '★プロが毎日一番最初に見るチャート：すべての株安・金安の犯人はこの「DXYの上昇」',
          tag: '19ヶ月ぶり高値',
          body: '米10年債利回り5.05%とAnthropic IPOのドル資金需要でDXYが103.97まで急騰しました。DXYが上がると、逆相関で米国株・新興国株(VWRA)・ゴールドが機械的に売られます。'
        },
        cta: {
          headline: '朗報：日足RSI（71.30）・週足RSI（70.23）ともに「70（買われすぎ限界）」に到達！',
          tag: 'RSI 71.3 ピーク圏',
          body: '日足だけでなく週足のRSIまで70を超えたということは、ドル買いがすでに限界近くまで織り込まれたことを意味します。'
        },
        macro: {
          headline: 'DXYが104から102台へ反落し始めた瞬間が、株（IVV/CSPX/VWRA）と金（GOLD）の全面買い合図！',
          tag: '11/25 米コアPCE',
          body: '来週11/25（水）の米コアPCE通過で「材料出尽くし」となりDXYが反落すれば、今まで抑えつけられていた株式ETFやゴールドが一気に吹き上がります。'
        }
      },
      nextAction: 'このDXYのRSIが71から60台へ下がり始める（＝ドル高が一服する）瞬間が、VWRA・CSPX・IVV・GOLDの第2弾買い増しのベストタイミングになります！',
      metrics: [
        { label: '日足 RSI (14)', value: '71.30', sub: '買われすぎ(70超)到達！' },
        { label: '週足 RSI (14)', value: '70.23', sub: '中期もドル高ピーク圏' },
        { label: '日足 20SMA', value: '102.47', sub: '反落時の第1サポート' },
        { label: '日足 200SMA', value: '100.04', sub: '長期の分岐ライン' }
      ]
    }
  }
};

</script>
  <script>
    const DATA = window.PROFLOW_DATA.symbols;
    const MACRO = window.PROFLOW_DATA.macroOverview;
    let currentRegion = 'ALL';
    let currentId = '8058';
    let currentLens = 'flow';
    let currentChartRange = '6M';

    // Historical performance anchors from TradingView (1D, 5D, 1M, 3M, 6M, 1Y, SMA200)
    const CHART_ANCHORS = {
      FLIN:   { cur: 37.16,  d5: 1.78,  m1: 9.17,  m3: 3.94,  m6: 6.78,  y1: -5.18, sma200: 35.15 },
      UAE:    { cur: 20.89,  d5: -0.10, m1: 6.26,  m3: 7.02,  m6: 9.37,  y1: 8.41,  sma200: 19.56 },
      CIBR:   { cur: 96.36,  d5: 1.19,  m1: -3.26, m3: 2.77,  m6: 16.74, y1: 33.89, sma200: 84.92 },
      XLV:    { cur: 177.46, d5: -6.68, m1: -0.12, m3: 3.23,  m6: 19.03, y1: 14.59, sma200: 160.76 },
      XLP:    { cur: 89.86,  d5: -2.37, m1: 2.33,  m3: 4.98,  m6: 6.07,  y1: 15.64, sma200: 85.01 },
      RSP:    { cur: 211.63, d5: -4.97, m1: -1.03, m3: -4.37, m6: 2.87,  y1: 10.10, sma200: 209.19 },
      VWRA:   { cur: 182.18, d5: -3.55, m1: -5.23, m3: -5.72, m6: -1.84, y1: 9.06,  sma200: 185.05 },
      CSPX:   { cur: 790.97, d5: -3.46, m1: -5.47, m3: -4.57, m6: -0.88, y1: 3.22,  sma200: 791.46 },
      IVV:    { cur: 735.70, d5: -2.85, m1: -5.27, m3: -4.95, m6: -0.86, y1: 9.32,  sma200: 735.59 },
      VHVE:   { cur: 145.10, d5: -4.06, m1: -5.00, m3: -5.42, m6: -1.40, y1: 10.09, sma200: 146.52 },
      SOXX:   { cur: 141.85, d5: -7.48, m1: -16.73,m3: -12.0, m6: -19.99,y1: 52.23, sma200: 160.77 },
      FGM:    { cur: 57.84,  d5: -2.85, m1: -1.07, m3: -8.19, m6: -10.06,y1: -1.48, sma200: 62.93 },
      AMZN:   { cur: 257.89, d5: -3.74, m1: 1.10,  m3: -1.13, m6: -2.13, y1: 10.56, sma200: 244.76 },
      SPCX:   { cur: 141.70, d5: 2.80,  m1: -4.13, m3: -2.25, m6: -5.53, y1: -5.53, sma200: 144.94 },
      TSLA:   { cur: 380.11, d5: -1.62, m1: 2.97,  m3: 12.16, m6: -9.96, y1: -4.67, sma200: 382.27 },
      GOOG:   { cur: 277.60, d5: -4.46, m1: -19.37,m3: -18.31,m6: -27.33,y1: -3.07, sma200: 335.79 },
      D05:    { cur: 66.55,  d5: -5.48, m1: -10.12,m3: -11.87,m6: 7.67,  y1: 23.91, sma200: 66.72 },
      O39:    { cur: 27.36,  d5: -4.34, m1: -5.69, m3: -10.82,m6: 16.92, y1: 49.05, sma200: 26.01 },
      '8058': { cur: 5089,   d5: -4.58, m1: 7.25,  m3: 9.30,  m6: -5.99, y1: 38.50, sma200: 4915 },
      '1329': { cur: 6160,   d5: -4.02, m1: -7.77, m3: -9.93, m6: -5.12, y1: 18.97, sma200: 6469 },
      '1475': { cur: 396.3,  d5: -3.72, m1: -4.97, m3: -4.44, m6: -1.42, y1: 15.32, sma200: 403.2 },
      '1364': { cur: 3592,   d5: -3.21, m1: -4.57, m3: -4.11, m6: -1.02, y1: 15.95, sma200: 3637 },
      TLT:    { cur: 80.22,  d5: 1.16,  m1: 0.40,  m3: -2.80, m6: -5.18, y1: -10.22,sma200: 84.19 },
      IEF:    { cur: 90.67,  d5: 0.71,  m1: 0.39,  m3: -1.80, m6: -3.50, y1: -6.37, sma200: 93.55 },
      GOLD:   { cur: 3711.38,d5: -4.25, m1: -10.39,m3: -14.0, m6: -18.29,y1: -8.74, sma200: 4428.23 },
      USOIL:  { cur: 81.95,  d5: -7.83, m1: -16.69,m3: -12.0, m6: -16.49,y1: 35.25, sma200: 87.92 },
      CPER:   { cur: 34.10,  d5: -7.79, m1: -13.54,m3: -10.5, m6: -11.77,y1: 10.21, sma200: 37.95 },
      USDJPY: { cur: 159.53, d5: -0.18, m1: 0.67,  m3: 0.50,  m6: 0.38,  y1: 2.63,  sma200: 158.80 },
      USDSGD: { cur: 1.2904, d5: 0.33,  m1: 0.87,  m3: 0.90,  m6: 0.95,  y1: -0.86, sma200: 1.2796 },
      SGDJPY: { cur: 123.63, d5: -0.38, m1: -0.08, m3: -0.25, m6: -0.47, y1: 3.57,  sma200: 124.04 },
      DXY:    { cur: 103.97, d5: 0.71,  m1: 1.94,  m3: 3.20,  m6: 4.80,  y1: 4.40,  sma200: 100.04 }
    };

    function renderMacroOverview() {
      if (!MACRO) return;
      document.getElementById('macro-title').textContent = MACRO.regimeTitle;
      document.getElementById('macro-summary').textContent = MACRO.regimeSummary;
      document.getElementById('macro-pillars').innerHTML = MACRO.pillars.map(p => `
        <div class="bg-[var(--card)] border border-[var(--border)] rounded-2xl p-5 space-y-2">
          <div class="flex items-center justify-between gap-2">
            <span class="font-bold text-sm">${p.title}</span>
            <span class="px-2 py-0.5 rounded-full text-xs font-mono font-semibold ${toneStyles(p.tone)}">${p.status}</span>
          </div>
          <p class="text-xs text-[var(--muted-foreground)] leading-relaxed">${p.detail}</p>
        </div>
      `).join('');
    }

    function buildSeries(id, range) {
      const a = CHART_ANCHORS[id] || CHART_ANCHORS.VWRA;
      const cur = a.cur;
      const p5d = cur / (1 + a.d5 / 100);
      const p1m = cur / (1 + a.m1 / 100);
      const p3m = cur / (1 + a.m3 / 100);
      const p6m = cur / (1 + a.m6 / 100);
      const p1y = cur / (1 + a.y1 / 100);

      let waypoints = [];
      if (range === '1M') {
        waypoints = [p1m, (p1m * 0.6 + p5d * 0.4) * 1.008, p5d * 1.01, p5d, cur];
      } else if (range === '6M') {
        waypoints = [p6m, (p6m + p3m) / 2 * 1.015, p3m * 1.025, p1m * 1.01, p5d, cur];
      } else {
        waypoints = [p1y, (p1y + p6m) / 2 * 0.99, p6m * 1.02, p3m * 1.03, p1m, p5d, cur];
      }

      const steps = 48;
      const pts = [];
      let seed = id.split('').reduce((acc, c) => acc + c.charCodeAt(0), 0);
      for (let i = 0; i <= steps; i++) {
        const t = (i / steps) * (waypoints.length - 1);
        const idx = Math.min(Math.floor(t), waypoints.length - 2);
        const frac = t - idx;
        const smooth = frac * frac * (3 - 2 * frac);
        let val = waypoints[idx] * (1 - smooth) + waypoints[idx + 1] * smooth;
        if (i > 0 && i < steps) {
          seed = (seed * 1103515245 + 12345) & 0x7fffffff;
          const noiseScale = (DATA[id] && DATA[id].region === 'FX') ? 0.0025 : 0.011;
          const noise = ((seed % 1000) / 1000 - 0.5) * noiseScale * cur;
          val += noise;
        }
        pts.push(val);
      }
      return { pts, sma200: a.sma200 };
    }

    let activeSeries = null;
    let hoverIndex = null;

    function drawAppleChart() {
      const canvas = document.getElementById('apple-chart');
      if (!canvas) return;
      const rect = canvas.getBoundingClientRect();
      if (rect.width === 0) return;
      const dpr = window.devicePixelRatio || 1;
      canvas.width = rect.width * dpr;
      canvas.height = rect.height * dpr;
      const ctx = canvas.getContext('2d');
      ctx.scale(dpr, dpr);

      const w = rect.width;
      const h = rect.height;
      ctx.clearRect(0, 0, w, h);

      activeSeries = buildSeries(currentId, currentChartRange);
      const pts = activeSeries.pts;
      const sma = activeSeries.sma200;

      const allVals = pts.concat([sma]);
      const minV = Math.min(...allVals) * 0.995;
      const maxV = Math.max(...allVals) * 1.005;
      const span = Math.max(maxV - minV, 0.0001);

      const padX = 8;
      const padY = 14;
      const plotW = w - padX * 2;
      const plotH = h - padY * 2;

      const toX = (i) => padX + (i / (pts.length - 1)) * plotW;
      const toY = (v) => padY + (1 - (v - minV) / span) * plotH;

      ctx.strokeStyle = 'rgba(148, 163, 184, 0.12)';
      ctx.lineWidth = 1;
      [0.2, 0.5, 0.8].forEach(r => {
        ctx.beginPath();
        ctx.moveTo(padX, padY + plotH * r);
        ctx.lineTo(w - padX, padY + plotH * r);
        ctx.stroke();
      });

      if (sma >= minV && sma <= maxV) {
        const ySma = toY(sma);
        ctx.save();
        ctx.strokeStyle = 'rgba(56, 189, 248, 0.65)';
        ctx.lineWidth = 1.2;
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(padX, ySma);
        ctx.lineTo(w - padX, ySma);
        ctx.stroke();
        ctx.fillStyle = 'rgba(56, 189, 248, 0.85)';
        ctx.font = '10px ui-monospace, SFMono-Regular, Menlo, monospace';
        ctx.fillText('200SMA ' + formatNum(sma), padX + 4, Math.max(ySma - 5, 10));
        ctx.restore();
      }

      const isPositive = pts[pts.length - 1] >= pts[0];
      const strokeColor = isPositive ? '#10b981' : '#f43f5e';
      const gradTop = isPositive ? 'rgba(16, 185, 129, 0.28)' : 'rgba(244, 63, 94, 0.28)';
      const gradBot = isPositive ? 'rgba(16, 185, 129, 0.0)' : 'rgba(244, 63, 94, 0.0)';

      ctx.beginPath();
      pts.forEach((v, i) => {
        const x = toX(i);
        const y = toY(v);
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      });
      ctx.lineTo(toX(pts.length - 1), h);
      ctx.lineTo(toX(0), h);
      ctx.closePath();
      const grad = ctx.createLinearGradient(0, 0, 0, h);
      grad.addColorStop(0, gradTop);
      grad.addColorStop(1, gradBot);
      ctx.fillStyle = grad;
      ctx.fill();

      ctx.beginPath();
      pts.forEach((v, i) => {
        const x = toX(i);
        const y = toY(v);
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      });
      ctx.strokeStyle = strokeColor;
      ctx.lineWidth = 2.2;
      ctx.lineJoin = 'round';
      ctx.stroke();

      const idx = (hoverIndex !== null && hoverIndex >= 0 && hoverIndex < pts.length) ? hoverIndex : (pts.length - 1);
      const cx = toX(idx);
      const cy = toY(pts[idx]);

      if (hoverIndex !== null) {
        ctx.save();
        ctx.strokeStyle = 'rgba(248, 250, 252, 0.35)';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(cx, 0);
        ctx.lineTo(cx, h);
        ctx.stroke();
        ctx.restore();
      }

      ctx.beginPath();
      ctx.arc(cx, cy, 4.5, 0, Math.PI * 2);
      ctx.fillStyle = strokeColor;
      ctx.fill();
      ctx.lineWidth = 2;
      ctx.strokeStyle = '#090d16';
      ctx.stroke();
    }

    function formatNum(val) {
      if (currentId === 'USDSGD') return val.toFixed(4);
      const unit = DATA[currentId].unit;
      if (unit === 'JPY' && val >= 1000) return Math.round(val).toLocaleString();
      if (unit === 'JPY' && val >= 100) return val.toFixed(2);
      if (unit === 'JPY') return val.toFixed(1);
      return val.toFixed(2);
    }

    function setChartRange(rng) {
      currentChartRange = rng;
      ['1M', '6M', '1Y'].forEach(r => {
        const btn = document.getElementById('rng-' + r);
        if (r === rng) {
          btn.className = 'px-2.5 py-1 rounded-md font-semibold bg-[var(--card)] text-[var(--foreground)] shadow-sm transition';
        } else {
          btn.className = 'px-2.5 py-1 rounded-md text-[var(--muted-foreground)] hover:text-[var(--foreground)] transition';
        }
      });
      hoverIndex = null;
      const a = CHART_ANCHORS[currentId];
      const pct = rng === '1M' ? a.m1 : (rng === '6M' ? a.m6 : a.y1);
      const sign = pct >= 0 ? '+' : '';
      document.getElementById('chart-hover-label').textContent = `${rng}騰落率: ${sign}${pct.toFixed(2)}% • 200SMA: ${formatNum(a.sma200)}`;
      drawAppleChart();
    }

    function setupChartTouch() {
      const canvas = document.getElementById('apple-chart');
      if (!canvas) return;
      const handleMove = (clientX) => {
        if (!activeSeries) return;
        const rect = canvas.getBoundingClientRect();
        const relX = Math.max(0, Math.min(1, (clientX - rect.left) / rect.width));
        hoverIndex = Math.round(relX * (activeSeries.pts.length - 1));
        const val = activeSeries.pts[hoverIndex];
        const base = activeSeries.pts[0];
        const diffPct = ((val - base) / base) * 100;
        const sign = diffPct >= 0 ? '+' : '';
        document.getElementById('chart-hover-label').textContent = `価格: ${formatNum(val)} ${DATA[currentId].unit} (${sign}${diffPct.toFixed(2)}%)`;
        drawAppleChart();
      };
      canvas.addEventListener('mousemove', e => handleMove(e.clientX));
      canvas.addEventListener('touchmove', e => {
        if (e.touches && e.touches[0]) handleMove(e.touches[0].clientX);
      }, { passive: true });
      const resetHover = () => {
        hoverIndex = null;
        setChartRange(currentChartRange);
      };
      canvas.addEventListener('mouseleave', resetHover);
      canvas.addEventListener('touchend', resetHover);
      window.addEventListener('resize', drawAppleChart);
    }

    function toneStyles(tone) {
      if (tone === 'success') return 'bg-[var(--success)]/15 text-[var(--success)] border border-[var(--success)]/30';
      if (tone === 'warning') return 'bg-[var(--warning)]/15 text-[var(--warning)] border border-[var(--warning)]/30';
      return 'bg-[var(--error)]/15 text-[var(--error)] border border-[var(--error)]/30';
    }

    function setRegion(reg) {
      currentRegion = reg;
      ['ALL', 'US', 'ETF', 'SG', 'JP', 'BOND', 'COMMODITY', 'FX'].forEach(r => {
        const btn = document.getElementById('reg-' + r);
        if (!btn) return;
        if (r === reg) {
          btn.className = 'px-2.5 py-1 rounded-lg font-semibold bg-[var(--secondary)] text-[var(--foreground)] transition shrink-0';
        } else {
          btn.className = 'px-2.5 py-1 rounded-lg font-medium text-[var(--muted-foreground)] hover:text-[var(--foreground)] transition shrink-0';
        }
      });
      const visibleIds = Object.keys(DATA).filter(id => reg === 'ALL' || DATA[id].region === reg);
      if (!visibleIds.includes(currentId)) {
        currentId = visibleIds[0];
      }
      renderTickerBar();
      selectSymbol(currentId);
    }

    function renderTickerBar() {
      const bar = document.getElementById('ticker-bar');
      const keys = Object.keys(DATA).filter(id => currentRegion === 'ALL' || DATA[id].region === currentRegion);
      bar.innerHTML = keys.map(id => {
        const item = DATA[id];
        const active = id === currentId;
        return `
          <button onclick="selectSymbol('${id}')" class="px-3.5 py-2 rounded-full text-xs font-medium transition shrink-0 flex items-center gap-2 border ${
            active
              ? 'bg-[var(--foreground)] text-[var(--background)] border-[var(--foreground)] shadow-sm'
              : 'bg-[var(--card)] text-[var(--muted-foreground)] border-[var(--border)] hover:text-[var(--foreground)]'
          }">
            <span>${item.title}</span>
            <span class="font-mono opacity-75">${item.price}</span>
          </button>
        `;
      }).join('');
    }

    function selectSymbol(id) {
      currentId = id;
      renderTickerBar();
      const d = DATA[id];

      document.getElementById('hero-asset-class').textContent = d.assetClass;
      document.getElementById('hero-ticker').textContent = d.ticker;
      document.getElementById('hero-title').textContent = d.title;
      document.getElementById('hero-subtitle').textContent = d.subtitle;
      document.getElementById('hero-price').innerHTML = `${d.price} <span class="text-sm font-normal text-[var(--muted-foreground)]">${d.unit}</span>`;

      const chg = document.getElementById('hero-change');
      chg.textContent = d.change;
      chg.className = 'text-xs font-medium mt-0.5 ' + (d.isUp ? 'text-[var(--success)]' : 'text-[var(--error)]');

      document.getElementById('sig-short-title').textContent = d.shortTitle;
      const sp = document.getElementById('sig-short-pill');
      sp.textContent = d.shortPill;
      sp.className = 'px-2.5 py-1 rounded-full text-xs font-mono font-semibold shrink-0 ' + toneStyles(d.shortTone);

      document.getElementById('sig-long-title').textContent = d.longTitle;
      const lp = document.getElementById('sig-long-pill');
      lp.textContent = d.longPill;
      lp.className = 'px-2.5 py-1 rounded-full text-xs font-mono font-semibold shrink-0 ' + toneStyles(d.longTone);

      document.getElementById('range-status').textContent = d.rangeStatus;
      document.getElementById('range-marker').style.left = d.rangePos;
      document.getElementById('range-low').textContent = d.rangeLow;
      document.getElementById('range-mid').textContent = d.rangeMid;
      document.getElementById('range-high').textContent = d.rangeHigh;

      document.getElementById('next-action-text').textContent = d.nextAction;

      document.getElementById('metrics-grid').innerHTML = d.metrics.map(m => `
        <div class="bg-[var(--card)] border border-[var(--border)] rounded-2xl p-4 space-y-1">
          <div class="text-xs text-[var(--muted-foreground)]">${m.label}</div>
          <div class="text-base font-bold font-mono tabular-nums">${m.value}</div>
          <div class="text-xs text-[var(--muted-foreground)] truncate">${m.sub}</div>
        </div>
      `).join('');

      setLens(currentLens);
      setChartRange(currentChartRange);
    }

    function setLens(lens) {
      currentLens = lens;
      ['flow', 'cta', 'macro'].forEach(l => {
        const btn = document.getElementById('lens-' + l);
        if (l === lens) {
          btn.className = 'px-3 py-1.5 rounded-lg font-semibold bg-[var(--card)] text-[var(--foreground)] shadow-sm transition flex-1 sm:flex-none';
        } else {
          btn.className = 'px-3 py-1.5 rounded-lg font-medium text-[var(--muted-foreground)] hover:text-[var(--foreground)] transition flex-1 sm:flex-none';
        }
      });

      const content = DATA[currentId].lenses[lens];
      const box = document.getElementById('lens-content');
      box.classList.remove('fade-in');
      void box.offsetWidth;
      box.classList.add('fade-in');

      document.getElementById('lens-headline').textContent = content.headline;
      document.getElementById('lens-tag').textContent = content.tag;
      document.getElementById('lens-body').textContent = content.body;
    }

    function renderMatrix() {
      const list = document.getElementById('matrix-list');
      list.innerHTML = Object.keys(DATA).map(id => {
        const d = DATA[id];
        return `
          <div onclick="jumpToSymbol('${id}')" class="py-3.5 flex flex-col sm:flex-row sm:items-center justify-between gap-2 cursor-pointer hover:opacity-80 transition">
            <div class="space-y-0.5">
              <div class="flex items-center gap-2">
                <span class="font-bold text-sm">${d.title}</span>
                <span class="text-xs font-mono text-[var(--muted-foreground)]">${d.price} ${d.unit}</span>
              </div>
              <p class="text-xs text-[var(--muted-foreground)]">${d.rangeStatus}</p>
            </div>
            <div class="flex items-center gap-2 shrink-0">
              <span class="px-2.5 py-1 rounded-full text-xs font-mono font-semibold ${toneStyles(d.shortTone)}">短期: ${d.shortPill}</span>
              <span class="px-2.5 py-1 rounded-full text-xs font-mono font-semibold ${toneStyles(d.longTone)}">中長期: ${d.longPill}</span>
            </div>
          </div>
        `;
      }).join('');
    }

    function jumpToSymbol(id) {
      setRegion('ALL');
      selectSymbol(id);
      setMainView('signal');
    }

    function setMainView(view) {
      document.getElementById('view-macro').classList.toggle('hidden', view !== 'macro');
      document.getElementById('view-signal').classList.toggle('hidden', view !== 'signal');
      document.getElementById('nav-area').classList.toggle('hidden', view !== 'signal');
      document.getElementById('view-picks').classList.toggle('hidden', view !== 'picks');
      document.getElementById('view-matrix').classList.toggle('hidden', view !== 'matrix');

      ['macro', 'signal', 'picks', 'matrix'].forEach(v => {
        const btn = document.getElementById('nav-' + v);
        if (!btn) return;
        btn.className = (v === view)
          ? 'px-3 py-1 rounded-full font-medium bg-[var(--foreground)] text-[var(--background)] transition shrink-0'
          : 'px-3 py-1 rounded-full font-medium text-[var(--muted-foreground)] hover:text-[var(--foreground)] transition shrink-0';
      });
      if (view === 'macro') renderMacroOverview();
      if (view === 'matrix') renderMatrix();
      if (view === 'signal') setTimeout(drawAppleChart, 20);
    }

    renderMacroOverview();
    setupChartTouch();
    setRegion('ALL');
    selectSymbol('8058');
  </script>
</body>
</html>
