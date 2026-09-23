---
schema: strategy-research-record-v1
title: "Volatility-Conditional Liquidity Provision Reversal with Stoikov Micro-Price Execution Overlay and Microstructure Boundary Falsification (Alpha Research Paper 5)"
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - microstructure
  - liquidity-provision
  - execution-overlay
  - order-flow-imbalance
  - short-term-reversal
  - volatility-regime
  - us-equities
  - limit-order-book
status: research-only
confidence: medium
source_as_of: 2026-06-17
sources:
  - "Bryan Vine, 'Liquidity Provision as Alpha: Execution, Order Flow, and the Limits of Microstructure', Alpha Research Paper 5, byline June 17, 2026, https://bryanvine.github.io/alpha-research/paper5.html"
  - "https://github.com/bryanvine/alpha-research — file docs/paper5.html at full commit SHA d94009a619b5db0c3b6f22a9b958156b5648659b (2026-06-17T00:47:21Z, commit message 'Paper 5: Liquidity Provision as Alpha'); byte-identical to repo head 17b8b5e1c79af194f733544517d82e3cf12c2259 (2026-08-23); SHA-256 ca17211a5d02a5e8672fc1c39eb93dc836571f032046160dc1642f561a9fcbaf, 19534 bytes (verified 2026-09-23)"
  - "https://github.com/bryanvine/alpha-research/blob/d94009a619b5db0c3b6f22a9b958156b5648659b/alpha_research/factors/microstructure.py"
  - "https://github.com/bryanvine/alpha-research/blob/d94009a619b5db0c3b6f22a9b958156b5648659b/scripts/19_microstructure_core.py"
  - "https://github.com/bryanvine/alpha-research/blob/d94009a619b5db0c3b6f22a9b958156b5648659b/scripts/44_paper5_figures.py"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Volatility-Conditional Liquidity Provision Reversal with Stoikov Micro-Price Execution Overlay and Microstructure Boundary Falsification (Alpha Research Paper 5)

## Provenance

- **Source:** Bryan Vine, *"Liquidity Provision as Alpha: Execution, Order Flow, and the Limits of Microstructure"* — Alpha Research, Paper 5 (the fifth paper of a personal research series).
- **Author list (complete, as printed on the source):** Bryan Vine (sole author; page byline `Bryan Vine · June 17, 2026`).
- **Published URL (stable):** https://bryanvine.github.io/alpha-research/paper5.html
- **Repository URL:** https://github.com/bryanvine/alpha-research
- **Immutable provenance:** file path `docs/paper5.html` at **full commit SHA `d94009a619b5db0c3b6f22a9b958156b5648659b`** (2026-06-17T00:47:21Z, commit message *"Paper 5: Liquidity Provision as Alpha"*).
- **Primary-source checksum (performed 2026-09-23):** three copies were fetched and hashed — (a) the live GitHub Pages file, (b) `docs/paper5.html` at creation commit `d94009a6…`, (c) `docs/paper5.html` at repository head `17b8b5e1c79af194f733544517d82e3cf12c2259` (head as of 2026-09-23). All three are **byte-identical**: SHA-256 `ca17211a5d02a5e8672fc1c39eb93dc836571f032046160dc1642f561a9fcbaf`, **19,534 bytes**.
- **Supporting code files at pinned commit `d94009a6…`:**
  - `alpha_research/factors/microstructure.py` (LOB loading, L1 filtering, feature computation including Cont-Kukanov-Stoikov OFI and Stoikov micro-price).
  - `scripts/19_microstructure_core.py` (core empirical evaluation harness for H1, H2, H3, and H4).
  - `scripts/44_paper5_figures.py` (publication figures generator for `docs/figures/p5_fig1_ofi.png`, `p5_fig2_overlay.png`, `p5_fig3_reversal_vix.png`, and `docs/og-liquidity.png`).
  - `alpha_research/factors/equity_zoo.py` (contains `sig_st_reversal` and `ls_backtest` definitions used by H4).
  - `RESEARCH_LOG.md` (dated 2026-06-17 entry documenting exact parameters, intermediate metrics, and data limitations).
- **Sections read directly from the pinned HTML and repository code:** Title and header/byline; Abstract; §1 Introduction (H1–H4 formulations); §2 Data & leakage control; §3 Method; §4 Experiments & results (§4.1 Order flow explains the present, not the future; §4.2 Standalone market-making is structurally unavailable; §4.3 The micro-price is an execution edge; §4.4 The capturable premium is vol-conditional liquidity provision; Table "Where microstructure pays — and doesn't"); §5 Discussion; §6 Limitations & future work; References; plus full Python source of `alpha_research/factors/microstructure.py` and `scripts/19_microstructure_core.py`.
- **Sample / data window as reported:**
  - LOB microstructure sample: 28 regular-trading days across November–December 2025; **5.24M snapshots** (100ms interval, regular trading hours 14:30–21:00 UTC) on SPY.
  - Reversal and volatility panel: FnSpID US equity price panel (3,983 symbols) spanning 2016-01-01 to 2020-12-31, joined with FRED VIX (`VIXCLS`).
- **Universe as reported:**
  - LOB sample: SPY (SPDR S&P 500 ETF Trust) on US equity markets.
  - Reversal sample: FnSpID equity panel (3,983 US common stocks, filtered with minimum observation fraction `min_obs_frac=0.6`).
- **Repository-wide deduplication audit (2026-09-23):**
  - Audited all existing `.md` records in `alpha-strategy-research`.
  - Zero existing records cite `paper5.html`, `19_microstructure_core.py`, `44_paper5_figures.py`, or commit `d94009a619b5db0c3b6f22a9b958156b5648659b`.
  - Same-author series records currently present cover distinct, non-overlapping mechanisms: Paper 1 (`crypto-volatility-risk-premium-variance-swap-estimator-fragility-decay-2026-09-12.md`), Paper 2 (`crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11.md`), Paper 3 (`crypto-statistical-arbitrage-pca-residual-cointegration-falsification-2026-09-12.md`), Paper 6 (`g10-fx-carry-fx-value-energy-roll-yield-net-cost-audit-2026-09-23.md`), Paper 8 (`autonomous-llm-research-stablecoin-flow-carry-trend-death-2026-09-19.md`), and Paper 9 (`two-engine-llm-intrinsic-valuation-consensus-margin-of-safety-forward-ic-2026-09-23.md`).
  - Adjacent LOB records (e.g. `order-flow-imbalance-predictive-decoupling-cost-falsification-2026-09-12.md` by Tejas Mungale) analyze NASDAQ TotalView ITCH data on single tech stocks (AAPL, MSFT, INTC, NVDA) but lack the Stoikov micro-price execution overlay, lack the vol-conditional reversal strategy, and originate from a different author and repository.
  - Adjacent crypto liquidity-provision records (e.g. `crypto-liquidity-provision-reversal-premium-cross-market-2026-09-01.md` by Farag et al., 2025) study CEX vs AMM DEX interconnectedness in crypto, with completely separate data, methodology, and scope.
  - Conclusion: this record is uniquely source-identified and functionally independent.
- **Canonical schema compliance:** follows `quant/strategy-research-record-spec-v1` (`schema: strategy-research-record-v1`, verified from `/Users/hong/.hermes/wiki/quant/strategy-research-record-spec-v1.md`).

## Economic mechanism

### Source-reported

1. **Reframing Microstructure Alpha (§1, §5):** Limit-order-book microstructure is often treated by algorithmic traders as a source of directional predictive signals or easy passive spread capture. The source evaluates these claims from the seat of a non-colocated market participant and disaggregates them into four distinct hypotheses:
   - **H1 (Spread Capture / Standalone Market Making):** Capturing the bid-ask spread is structurally unavailable to a non-colocated participant. On SPY, the gross half-spread is 0.093 bps (~1 cent on a $600 share). Realized execution requires competing against ultra-low latency HFT firms for queue priority at the touch, exchange maker rebates, and avoiding toxic adverse selection. Without sub-millisecond colocation and fee rebates, passive market making at the touch is structurally unprofitable.
   - **H2 (Order-Flow Imbalance Predictive Decoupling):** Order-Flow Imbalance (OFI; Cont, Kukanov & Stoikov 2014) is powerfully *contemporaneous* (explaining 41% of same-tick mid-quote changes), but has near-zero predictive power for forward mid moves ($R^2 = 0.0009$ at 0.1s, decaying to ~0 by 5s). A marketable taker strategy that trades in the direction of OFI and pays the full bid-ask spread loses −0.18 bps per trade.
   - **H3 (Execution-Cost Overlay via Micro-Price):** While microstructure yields no directional alpha, the imbalance-tilted micro-price (Stoikov 2018) provides a genuine execution edge. When executing a marketable parent order, conditioning the execution timing on the micro-price—crossing immediately when the micro-price indicates an imminent favorable mid shift, or waiting when it indicates a temporary adverse shift—reduces effective execution slippage by ~13% (from 0.093 bps to 0.081 bps).
   - **H4 (Lower-Frequency Volatility-Conditional Liquidity Provision):** The economically harvestable manifestation of liquidity provision for non-HFT participants occurs at lower frequencies (daily/weekly) through short-term reversal (Nagel 2012 "Evaporating Liquidity"). Short-term reversal (buying recent losers and selling recent winners) is the economic act of supplying liquidity to order flow demanders whose inventory shocks push prices temporarily away from fundamentals. When market volatility spikes (elevated VIX), fast-money liquidity providers retreat and risk aversion expands, causing the compensation for supplying liquidity to more than double (Sharpe rises from 0.42 in low-VIX regimes to 1.16 in high-VIX regimes).

### Research interpretation

- **Hypothesis formulation:** Realized alpha from microstructure cannot be extracted as high-frequency directional forecasts or naive passive market making without colocation and exchange rebates. Instead, viable economic capture exists through a **hybrid structural architecture**:
  1. An **execution-layer filter** using high-frequency order-book imbalance (Stoikov micro-price) to minimize implementation friction (slippage reduction);
  2. A **medium-frequency risk-premium capture engine** deploying cross-sectional short-term reversal conditioned on market volatility regimes (Nagel liquidity-provision compensation).
- **Component roles in the hybrid mechanism:**

```text
Regime Filter:       Market volatility regime (FRED VIX relative to historical median cutoff)
Primary Alpha:       21-day cross-sectional short-term equity reversal (liquidity provision to inventory flow)
Portfolio Sizing:    Dollar-neutral, equal-weighted long (top 30% losers) / short (top 30% winners) deciles
Execution Overlay:   Stoikov imbalance-tilted micro-price gating on order arrival (cross if favorable, wait 5s if adverse)
Risk / Cadence:      Periodic 5-day reconstitution; flat 10 bps turnover friction model
```

- **Competing explanations to be tested:**
  - *Small-cap illiquidity bias:* Short-term reversal in equal-weighted equity panels is heavily loaded on micro- and small-cap stocks where real transaction costs, bid-ask bounce, and borrow fees exceed the 10 bps model.
  - *Lead-lag cross-correlation vs true reversal:* Cross-sectional contrarian strategies can earn positive returns due to lead-lag cross-autocorrelations between large-cap and small-cap stocks rather than true own-stock liquidity-provision reversal (Lo and MacKinlay 1990).
  - *Execution overlay latency decay:* Micro-price slippage savings (~0.012 bps) on SPY may be smaller than the round-trip latency jitter of a retail or non-colocated API connection.

## Signal

### Component 1: Stoikov Micro-Price Execution Overlay (H3)

- **Source:** Stoikov (2018) micro-price formula, normalized in `alpha_research/factors/microstructure.py`:
  $$\text{mid}_t = \frac{a_t + b_t}{2}$$
  $$\text{spread}_t = a_t - b_t$$
  $$I_t = \frac{q^b_t}{q^b_t + q^a_t} \in [0, 1]$$
  $$\text{micro}_t = \text{mid}_t + \left(I_t - \frac{1}{2}\right) \cdot \text{spread}_t$$
  where $a_t$ is the best ask price, $b_t$ is the best bid price, $q^b_t$ is best bid size, and $q^a_t$ is best ask size at snapshot $t$.
- **Buy Execution Decision Rule:**
  - If $\text{micro}_t > \text{mid}_t$ ($I_t > 0.5$, buy pressure indicates ask exhaustion): execute immediately as a marketable order paying current ask $a_t$. Effective cost is $(a_t - \text{mid}_t) / \text{mid}_t \times 10{,}000$ bps.
  - If $\text{micro}_t \le \text{mid}_t$ ($I_t \le 0.5$, sell pressure indicates likely mid drop): wait $N_{\text{adv}} = 50$ bars (5.0 seconds at 100ms sampling) and cross at future ask $a_{t+50}$. Effective cost relative to decision mid is $(a_{t+50} - \text{mid}_t) / \text{mid}_t \times 10{,}000$ bps.
- **Sell Execution Decision Rule (`research-proposed`):**
  - Symmetric logic (implied by theory, unstated in source code): if $\text{micro}_t < \text{mid}_t$, cross immediately at $b_t$; if $\text{micro}_t \ge \text{mid}_t$, wait 50 bars and cross at $b_{t+50}$.

### Component 2: Volatility-Conditional Short-Term Reversal Strategy (H4)

- **Signal Formation:**
  - Lookback: $L = 21$ trading days (approx. 1 calendar month of daily returns).
  - Formula: $\text{rev}_{i,t} = -\sum_{k=0}^{20} \ln(1 + R_{i,t-k})$, where $R_{i,t}$ is daily stock return from the FnSpID panel (`alpha_research/factors/equity_zoo.py`).
  - Signal Lag: $\text{rev}_{i,t-1}$ lagged by 1 day (`shift(1)`) to enforce causal execution and prevent look-ahead bias.
- **Cross-Sectional Portfolio Construction:**
  - Universe filtering: minimum observation fraction across sample $\ge 0.60$ (`min_obs_frac=0.6`); minimum cross-section size on rebalance date $\ge 20$ valid names.
  - Quantile split: $q = 0.30$.
    - Long leg: stocks with reversal score $\ge 70\text{th percentile}$ ($s \ge \text{quantile}(0.70)$, the past 1-month losers).
    - Short leg: stocks with reversal score $\le 30\text{th percentile}$ ($s \le \text{quantile}(0.30)$, the past 1-month winners).
  - Sizing: dollar-neutral, gross exposure 1.0. Equal weight across long names ($w_i = +0.5 / N_{\text{long}}$) and short names ($w_j = -0.5 / N_{\text{short}}$).
  - Rebalance cadence: fixed 5-day periodic rebalance (`rebal=5`).
  - Turnover transaction cost: flat 10.0 bps per unit turnover applied at each rebalance.
- **Volatility Regime Split:**
  - Macro indicator: FRED VIX closing level (`VIXCLS`), forward-filled to equity dates.
  - Regime boundary: sample median split ($VIX_{\text{median}} = 16.8$).
  - Low-VIX regime: days where $VIX_t \le 16.8$.
  - High-VIX regime: days where $VIX_t > 16.8$.
- **Active regime-switching allocation (`research-proposed`):**
  - In the source, the regime split is an evaluation filter, not an automated leverage switch. A dynamic strategy allocating $0\times$ exposure in Low VIX and $1\times$ exposure in High VIX is `research-proposed`.

### Component 3: Standalone Microstructure Baselines (Falsified in Source)

- **OFI Taker Strategy (H2):**
  - Signal: $\text{sign}(\text{OFI}_t)$, where $\text{OFI}_t = \Delta b_t^* - \Delta a_t^*$ (Cont-Kukanov-Stoikov 2014 formulation).
  - Order type: marketable order crossing the spread, held for $N_{\text{adv}} = 50$ bars (5.0s).
  - Net return formula: $\text{sign}(\text{OFI}_t) \times \frac{\text{mid}_{t+50} - \text{mid}_t}{\text{mid}_t} \times 10{,}000 - \frac{\text{spread}_t}{\text{mid}_t} \times 10{,}000$ bps.
- **Naive vs Realistic Passive Market Maker (H1):**
  - Naive maker: assumes immediate fill at the quote, capturing half-spread $\frac{\text{spread}_t / 2}{\text{mid}_t} \times 10{,}000$ bps.
  - Realistic 5s mark-to-mid: for bid hits ($d\text{mid}_t < 0$), $\text{PnL} = (\text{mid}_{t+50} - b_t)/\text{mid}_t \times 10{,}000$; for ask lifts ($d\text{mid}_t > 0$), $\text{PnL} = (a_t - \text{mid}_{t+50})/\text{mid}_t \times 10{,}000$.

## Required data

- **LOB Microstructure Data (Order-Book Level):**
  - Instrument: SPY ETF.
  - Venue: US consolidated equity limit order book (source uses raw 10-level snapshots stored locally in parquet format).
  - Resolution: 100ms snapshot sampling, regular trading hours (14:30–21:00 UTC).
  - Required fields: `time`, `symbol`, `bid_price_1`, `bid_size_1`, `ask_price_1`, `ask_size_1`.
  - Data hygiene filters: $a > b$, $b > 0$, finite positive sizes, spread $/ \text{mid} \times 10{,}000 < 50$ bps (filtering crossed/auction/wide quotes), minimum 5,000 valid snapshots per day.
  - Missing data / trade tape: source explicitly flags that trade tape (ITCH messages) is omitted (`data gap`), preventing exact queue-position and realized-spread calculation.
- **Equity Panel Data (Reversal Strategy):**
  - Universe: FnSpID equity panel (3,983 US equity tickers).
  - Period: 2016-01-01 to 2020-12-31 (daily closing prices/returns).
  - Required fields: daily adjusted returns $R_{i,t}$.
  - Look-ahead protections: signal lagged 1 trading day (`shift(1)`).
- **Macro Volatility Data:**
  - Instrument: Cboe Volatility Index (VIX) daily closing series from FRED (`VIXCLS`).
  - Alignment: calendar date forward-filled onto the equity panel trading calendar.

## Execution assumptions

- **Execution Overlay (Component 1 - H3):**
  - Assumed order type: marketable limit / market order crossing the book.
  - Baseline execution cost: immediate market order paying half-spread (source reports 0.093 bps on SPY).
  - Overlay execution cost: micro-price conditioned order (cross now if $\text{micro} > \text{mid}$, else delay 5.0 seconds). Source reports 0.081 bps.
  - Latency assumption: execution logic assumes order arrival and micro-price computation within the 100ms snapshot window. API transport latency and exchange matching engine queue times are `not stated in source` / `research-proposed`.
- **Equity Reversal Strategy (Component 2 - H4):**
  - Assumed order type: daily market-on-close (MOC) or market-on-open (MOO) `not stated in source` (backtest models close-to-close returns with 1-day lag).
  - Transaction cost: flat 10.0 bps per side on turnover (`cost_bps=10.0`). For large caps this is conservative; for micro/small caps in an equal-weighted 3,983-stock universe, 10 bps is highly optimistic (`data gap / limitation`).
  - Borrow and shorting constraints: assumes unrestricted short borrowing at zero borrow fee (`not stated in source` / `research-proposed`).
  - Leverage / margin: gross exposure fixed at 1.0 (0.5 long, 0.5 short); cash financing rate assumed zero (`not stated in source`).
  - Fill model: fill at closing price with zero market impact (`underspecified`).
- **OFI Taker Execution (Component 3 - H2):**
  - Fully crosses bid-ask spread on every signal, pays full spread (averaging ~0.186 bps). Holding period fixed at 5.0 seconds (50 bars).
- **Passive Maker Execution (Component 3 - H1):**
  - Naive model assumes 100% fill probability at touch with zero queue delay.
  - Real-world colocation, cancellation fees, SIP/direct feed latency wedges, and maker rebates are `not stated in source` (structurally recognized as barriers).

## Evidence

### Source-reported

All quantitative figures below trace directly to `docs/paper5.html`, `scripts/19_microstructure_core.py`, `scripts/44_paper5_figures.py`, and `RESEARCH_LOG.md` (commit `d94009a6…`):

- **Order-Flow Imbalance (OFI) Contemporaneous vs Predictive Decoupling (H2):**
  - Contemporaneous $R^2$ of mid-price change ($d\text{mid}$) against OFI: **0.41** (explains 41% of contemporaneous mid-quote variance).
  - Forward predictive $R^2$ of mid-price change against OFI across horizons:
    - $+0.1\text{s}$ (1 bar): **0.0009**
    - $+1.0\text{s}$ (10 bars): **0.0000**
    - $+5.0\text{s}$ (50 bars): **0.0000**
    - $+10.0\text{s}$ (100 bars): **0.0000**
    - $+30.0\text{s}$ (300 bars): **0.0000**
  - Marketable taker strategy on $\text{sign}(\text{OFI})$ holding 5s and paying spread: nets **−0.18 bps** per trade (loses the bid-ask spread).
- **Standalone Market-Making Structural Unavailability (H1):**
  - SPY average half-spread: **0.093 bps** (~1 cent on a $600 share).
  - Naive maker capture: **+0.093 bps** (gross half-spread).
  - 5-second adverse-selection mark-to-mid: **+0.012 bps** (favorable mark, because SPY mid-price behaves as a 100ms martingale; no measurable adverse selection in unweighted book snapshots).
  - Source verdict: this +0.012 bp positive mark is an artifact of assuming fills on demand without queue modeling; the actual half-spread of 0.093 bp is an HFT-only arena governed by colocation and queue priority.
- **Stoikov Micro-Price Execution Overlay (H3):**
  - Immediate market order effective cost: **0.093 bps**.
  - Micro-price-gated overlay effective cost: **0.081 bps**.
  - Net slippage reduction: **13.0%** (shaves ~0.012 bps of execution friction).
- **Volatility-Conditional Short-Term Reversal Liquidity Provision (H4):**
  - Reversal panel: 3,983 US equities, 2016–2020, equal-weighted long-short deciles (top/bottom 30%), 5-day rebalance, net of 10 bps turnover cost.
  - VIX sample median: **16.8**.
  - Annualized Sharpe in Low-VIX regime ($VIX \le 16.8$): **0.42**.
  - Annualized Sharpe in High-VIX regime ($VIX > 16.8$): **1.16**.
  - Conclusion: liquidity provision compensation more than doubles during high-volatility regimes (Nagel evaporating-liquidity premium).

### Independently reproduced

`Not independently reproduced.` The primary source full text (`docs/paper5.html`), core evaluation script (`scripts/19_microstructure_core.py`), figure script (`scripts/44_paper5_figures.py`), and factor definition files (`alpha_research/factors/microstructure.py`, `equity_zoo.py`) were directly inspected and verified byte-identical between the pinned commit `d94009a6…` and repo head `17b8b5e1…` (SHA-256 `ca17211a…`, 19,534 bytes). The raw 5.24M LOB snapshots and FnSpID equity data are external local datasets gitignored from the public repository; no independent backtest was rerun in Qlib, Nautilus, or internal execution engines.

### Negative evidence

- **Directional OFI Trading Fails Net of Costs (§4.1):** Contemporaneous correlation ($R^2 = 0.41$) completely decouples from future prediction ($R^2 \le 0.0009$). Trading order-flow imbalance as a directional alpha signal results in a guaranteed loss of −0.18 bps per transaction after crossing the bid-ask spread.
- **Standalone Market Making is Structurally Inviable for Non-HFTs (§4.2):** Gross half-spread of 0.093 bps cannot support a viable standalone business for a small or non-colocated participant. Queue priority (FIFO queues at 1 cent spread on SPY) means passive limit orders sit at the back of massive depth queues, filling only when adverse selection occurs.
- **Reversal Fragility to Transaction Costs in Small Caps (RESEARCH_LOG.md):** In `RESEARCH_LOG.md`, the author explicitly notes that the short-term reversal signal is equal-weighted across 3,983 stocks, where performance is heavily driven by small-cap names. A flat 10 bps turnover fee is highly optimistic for small-cap names where effective spreads and market impact can exceed 50–100 bps, making the unconditional reversal signal cost-fragile.
- **Absence of Adverse Selection in Snapshots (§2, §6):** The favorable 5-second mark-to-mid (+0.012 bps) confirms that order-book snapshots without trade-level execution timestamps cannot properly model adverse selection, exposing a fundamental measurement limitation in snapshot-based microstructure research.

## Falsification plan

Every threshold below is labeled `research-defined falsification threshold` or `research-proposed`:

1. **Trade-Tape Queue-Position and Adverse Selection Audit (`research-proposed`):**
   - Re-evaluate the passive maker fill model using full tick-level ITCH message data (e.g. Databento NASDAQ ITCH). Model queue priority (orders placed at tail of queue) and calculate realized spread:
     $$\text{RS}_{\Delta t} = q_t \cdot (P_{\text{fill}} - \text{mid}_{t + \Delta t})$$
   - *Falsification threshold (`research-defined falsification threshold`):* If realized spread at $\Delta t = 5\text{s}$ or $\Delta t = 30\text{s}$ is $\le 0$ across all volatility regimes after queue position is accounted for, confirm that standalone market making is strictly negative alpha.
2. **Execution Overlay Net Slippage Test on Broader Universe (`research-proposed`):**
   - Test the Stoikov micro-price execution overlay on mid-cap and small-cap US equities (e.g. Russell 2000 constituents) and liquid crypto perps (BTC, ETH, SOL) over $\ge 6$ months of out-of-sample data.
   - *Falsification threshold (`research-defined falsification threshold`):* If the micro-price overlay fails to reduce effective slippage by at least 5% ($p < 0.05$) after accounting for 50ms–200ms network latency jitter, reject the execution overlay hypothesis as an artifact of zero-latency backtesting.
3. **Reversal Cost-Ladder and Cap-Tier Stress Test (`research-proposed`):**
   - Re-evaluate the 21-day short-term reversal strategy on a modern post-2020 equity universe (2021–2026), segmenting into S&P 500 (large cap), S&P 400 (mid cap), and Russell 2000 (small cap), applying a realistic cost ladder of 5 bps, 15 bps, 30 bps, and 50 bps per turnover unit.
   - *Falsification threshold (`research-defined falsification threshold`):* If the annualized Sharpe ratio of the high-VIX reversal strategy drops below $+0.30$ under a 20 bps cost hurdle or under a large-cap-only universe (S&P 500), reject the tradable viability of the liquidity-provision premium.
4. **VIX Regime Stability / Out-of-Sample Walk-Forward (`research-proposed`):**
   - Evaluate the VIX median split ($VIX > 16.8$) over out-of-sample data (2021–2026).
   - *Falsification threshold (`research-defined falsification threshold`):* If the Sharpe difference between high-VIX and low-VIX regimes ($\text{Sharpe}_{\text{high}} - \text{Sharpe}_{\text{low}}$) is $\le 0.20$ or statistically indistinguishable from zero ($t < 1.96$), falsify Nagel's evaporating-liquidity hypothesis in modern equity markets.

## Crypto portability

**`adapted`** / **`unproven`**

- **Source Scope:** The primary source investigates US equity microstructure (SPY) and US common stocks (FnSpID 2016–2020); it presents no crypto order-book or perp empirical backtests.
- **Portability of Component 1 (Micro-Price Execution Overlay):**
  - *Applicability:* `adapted`.
  - *Mechanism:* Stoikov's micro-price formula ports directly to crypto centralized exchanges (Binance, Bybit, OKX, Coinbase) using top-of-book or multi-level order books.
  - *Frictions:* Crypto perpetual books exhibit much higher tick-size-to-spread granularity than SPY (SPY is tick-constrained at 1 cent; crypto perps often have spreads spanning multiple ticks). Queue priority is less rigid, but API rate limits, WebSocket latency spikes, and exchange engine co-location advantages remain substantial.
- **Portability of Component 2 (Volatility-Conditional Reversal):**
  - *Applicability:* `unproven`.
  - *Mechanism:* Short-term reversal in crypto operates on substantially shorter horizons (hours to days, rather than 21 trading days). As shown in adjacent repository records (and Bryan Vine's own Paper 4 Part B), 7-day crypto reversal delivered a *negative* Sharpe (−0.47) across top-30 tokens, whereas short-horizon trend (CTREND) was positive (+0.53).
  - *Volatility Regime Conditioning:* Replacing VIX with crypto-native implied volatility (e.g. Deribit DVOL index) is necessary. The hypothesis that crypto contrarian liquidity provision pays during volatility spikes requires empirical demonstration; high-volatility events in crypto often trigger liquidation cascades where contrarian positions suffer catastrophic tail risk rather than mean-reverting.
- **Portability Boundary:** Porting is an unproven research hypothesis; this record does not authorize live or paper deployment in crypto markets.

## Limitations

- **Snapshot-Only Order Book Data (§2, §6):** 100ms LOB snapshots lack individual trade prints, order queue positions, and cancellation messages. Realized spread and adverse selection cannot be accurately computed without trade-tape data (e.g. ITCH).
- **Short Microstructure Observation Window:** The LOB study spans only 28 trading days (Nov–Dec 2025) on a single instrument (SPY).
- **Optimistic Reversal Cost Model in Small Caps:** The 10 bps turnover cost assumed in the FnSpID backtest is unrealistic for equal-weighted small-cap equities, where actual round-trip costs and borrow fees frequently erase reversal profits.
- **Dated Reversal Sample Period:** FnSpID price panel terminates in 2020 (2016–2020 sample). The post-2020 market regime (2021–2026) is unmeasured in this paper.
- **Lack of Dynamic Allocation Rule:** The paper documents that reversal Sharpe is 0.42 in low VIX vs 1.16 in high VIX, but does not formulate or test an end-to-end dynamic position-sizing strategy.
- **Execution Overlay Capacity Ceiling:** Gating execution on micro-price saves at most a fraction of the half-spread (~0.012 bps on SPY). For large institutional parent orders, market impact dwarfs this micro-price saving.

## Implementation status

`implementation_status: not-implemented`. No implementation in internal backtest or live trading stacks (Qlib, NautilusTrader, Paper, Testnet, or Live) has been conducted. The strategy is captured solely as a normalized research record.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.
Presence of this record in `alpha-strategy-research` does not constitute approval for live trading, testnet deployment, paper trading, Qlib survivor indexing, or candidate promotion. Promotion requires independent replication with full trade-level order-book data, modern out-of-sample data, and transaction cost stress testing through the ChatGPT Research Intake Review process.

## Related Wiki records

- Same-series records by Bryan Vine in `alpha-strategy-research`:
  - `crypto-volatility-risk-premium-variance-swap-estimator-fragility-decay-2026-09-12.md` (Paper 1: volatility risk premium)
  - `crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11.md` (Paper 2: crypto funding carry)
  - `crypto-statistical-arbitrage-pca-residual-cointegration-falsification-2026-09-12.md` (Paper 3: crypto stat-arb)
  - `g10-fx-carry-fx-value-energy-roll-yield-net-cost-audit-2026-09-23.md` (Paper 6: FX carry and roll yield)
  - `autonomous-llm-research-stablecoin-flow-carry-trend-death-2026-09-19.md` (Paper 8: autonomous research search)
  - `two-engine-llm-intrinsic-valuation-consensus-margin-of-safety-forward-ic-2026-09-23.md` (Paper 9: dual LLM valuation bots)
- Adjacent microstructure and order-flow records:
  - `order-flow-imbalance-predictive-decoupling-cost-falsification-2026-09-12.md` (Tejas Mungale ITCH OFI study on NASDAQ stocks)
  - `passive-market-impact-optimal-execution-mlofi-2026-09-02.md` (multi-level OFI and passive market impact)
  - `equity-order-flow-kyle-lambda-cross-sectional-liquidity-premium-2026-09-03.md` (Kyle's lambda liquidity premium)
- Adjacent liquidity provision and reversal records:
  - `crypto-liquidity-provision-reversal-premium-cross-market-2026-09-01.md` (Farag et al. 2025 JBF crypto liquidity provision)
  - `crypto-cross-sectional-last-day-return-reversal-liquidity-conditioned-2026-08-31.md` (crypto 1-day reversal conditioned on liquidity)
  - `drift-regime-gated-cross-sectional-value-reversal-2026-09-05.md` (drift regime gating on reversal)
- Canonical specification:
  - `[[quant/strategy-research-record-spec-v1]]` (Hermes Wiki Brain schema contract)

## Sources

1. Bryan Vine. *"Liquidity Provision as Alpha: Execution, Order Flow, and the Limits of Microstructure."* Alpha Research, Paper 5, byline **June 17, 2026**. https://bryanvine.github.io/alpha-research/paper5.html — primary source text, read in full on 2026-09-23.
2. Bryan Vine. `alpha-research` repository. https://github.com/bryanvine/alpha-research — file `docs/paper5.html` at full commit `d94009a619b5db0c3b6f22a9b958156b5648659b` (2026-06-17T00:47:21Z, commit message *"Paper 5: Liquidity Provision as Alpha"*) and at head `17b8b5e1c79af194f733544517d82e3cf12c2259`; byte-identical to the published page (SHA-256 `ca17211a5d02a5e8672fc1c39eb93dc836571f032046160dc1642f561a9fcbaf`, 19,534 bytes, verified 2026-09-23). Supporting code paths at this commit: `alpha_research/factors/microstructure.py`, `scripts/19_microstructure_core.py`, `scripts/44_paper5_figures.py`, `alpha_research/factors/equity_zoo.py`, `RESEARCH_LOG.md`.
3. Rama Cont, Arseniy Kukanov, and Sasha Stoikov (2014). "The Price Impact of Order Book Events." *Journal of Financial Econometrics*, 12(1), 47–88. DOI: 10.1093/jjfinec/nbt003 (foundational paper for Order-Flow Imbalance).
4. Sasha Stoikov (2018). "The Micro-Price: A High-Frequency Estimator of Future Prices." *Quantitative Finance*, 18(12), 1959–1966. DOI: 10.1080/14697688.2018.1489139 (foundational paper for imbalance-tilted micro-price).
5. Stefan Nagel (2012). "Evaporating Liquidity." *The Review of Financial Studies*, 25(7), 2005–2039. DOI: 10.1093/rfs/hhs066 (foundational paper for return reversal as liquidity provision compensation rising with VIX).
6. Ciamac Moallemi and Kai Yuan (2016). "A Model for Queue Position Valuation in a Limit Order Book." Working paper, Columbia University (cited in source for queue fill dynamics).
7. Matteo Aquilina, Eric Budish, and Peter O'Neill (2022). "Quantifying the High-Frequency Trading Arms Race." *Quarterly Journal of Economics*, 137(1), 1–64. DOI: 10.1093/qje/qjab032 (cited in source for structural latency barriers in spread capture).
