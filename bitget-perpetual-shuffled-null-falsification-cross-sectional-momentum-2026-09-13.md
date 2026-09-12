---
schema: strategy-research-record-v1
title: "Bitget Perpetual Futures: Shuffled-Return Null Falsification of Classic Technical Analysis, Survivorship-Free Cross-Sectional Momentum, and Volatility-Adaptive Market Making"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - scout
  - source-backed
  - crypto-perpetual
  - bitget
  - falsification
  - negative-evidence
  - shuffled-null-hypothesis
  - cross-sectional-momentum
  - market-making
  - walk-forward
status: research-only
confidence: high
source_as_of: 2026-09-12
sources:
  - "https://github.com/MarxMad/Bitget-Alg/tree/fe7b50dbdf519f2db1018a8967504812e0d72ce0"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitget Perpetual Futures: Shuffled-Return Null Falsification of Classic Technical Analysis, Survivorship-Free Cross-Sectional Momentum, and Volatility-Adaptive Market Making

## One-line mental model

An empirical quantitative investigation across 33 Bitget USDT-M perpetuals using shuffled-return null hypothesis testing that falsifies classic single-asset technical analysis as worse than random chance (11 real winners vs. 13.6 expected by noise), demonstrates weak evidence of relative-strength persistence in a survivorship-free 12-major cross-sectional momentum portfolio (walk-forward Sharpe 1.56, +42.9% out-of-sample vs. -0.73 shuffled null mean, $p < 0.10$), and proves that continuous market making at 2.5x realized volatility achieves breakeven volume while inventory skewing is actively harmful.

## Provenance

- **Author:** `MarxMad` / GerryVela (`gerardo.gerry.pedrizco@gmail.com`)
- **Repository URL:** [https://github.com/MarxMad/Bitget-Alg](https://github.com/MarxMad/Bitget-Alg)
- **Full Immutable Commit SHA:** `fe7b50dbdf519f2db1018a8967504812e0d72ce0`
- **Canonical Tree URL:** [https://github.com/MarxMad/Bitget-Alg/tree/fe7b50dbdf519f2db1018a8967504812e0d72ce0](https://github.com/MarxMad/Bitget-Alg/tree/fe7b50dbdf519f2db1018a8967504812e0d72ce0)
- **Commit Date:** 2026-09-12T21:37:42Z
- **Primary Source Files Directly Examined:**
  - `README.md` (overview of methodology, null-hypothesis testing framework, and validation outcomes) (`source-reported`).
  - `strategies/cross_sectional/README.md` (cross-sectional momentum specification, 12-major liquid panel, sizing constraints, and walk-forward statistics) (`source-reported`).
  - `strategies/cross_sectional/core.py` (signal logic, trailing return calculation, ranking, dollar-neutral weight construction, and viability checks) (`source-reported`).
  - `strategies/cross_sectional/strategy.py` (runtime execution loop, order reconciliation, and Bitget API integration) (`source-reported`).
  - `strategies/mm_bitget/README.md` (volatility-adaptive market maker design, 56 asset-day empirical sweep, inventory skewing penalties, and risk scaling laws) (`source-reported`).
  - `strategies/mm_bitget/core.py` (quote calculation at 2.5x rolling 1m volatility, inventory cap, requote drift thresholds, and post-only safety guards) (`source-reported`).
  - `strategies/mm_bitget/backtest.py` (verbatim replay of production quoting functions, fill model, and spread vs. adverse selection decomposition) (`source-reported`).
  - `scripts/scan_edges.py` (systematic edge sweep of EMA trend, Donchian breakout, and z-score mean reversion across 33 assets with maker/taker fee hurdles) (`source-reported`).
  - `scripts/significance_check.py` (shuffled-return permutation generator scoring empirical pass counts against synthetic pure-noise null distributions) (`source-reported`).
  - `scripts/walkforward.py` (rolling 90-day train / 30-day test walk-forward validation on single-asset signals against shuffled nulls) (`source-reported`).
  - `scripts/cross_sectional.py` (panel backtesting, parameter sweep, and rolling walk-forward evaluation on real vs. shuffled asset panels) (`source-reported`).
  - `scripts/optimize_mm.py` (in-sample / out-of-sample grid search of volatility multiples, skew factors, and inventory caps on 1-minute historical data) (`source-reported`).
  - `scripts/simulate_mm.py` (historical replay of fixed-spread predecessor market maker establishing negative drift from buying dips and selling rips) (`source-reported`).
- **Primary Source Verification:** All files, commit metadata, code routines, and empirical tables were directly inspected at commit `fe7b50dbdf519f2db1018a8967504812e0d72ce0`. Quantitative statistics, Sharpe ratios, drawdowns, win rates, fee assumptions, and parameters match the source repository exactly.
- **Repository Deduplication Audit:** Thorough search of the `alpha-strategy-research` repository confirmed zero existing records matching `MarxMad`, `Bitget-Alg`, or commit `fe7b50dbdf519f2db1018a8967504812e0d72ce0`. Existing cross-sectional momentum records in the repository (such as `crypto-cross-sectional-momentum-30d-top-quintile-7d-2026-08-31.md` based on Drogen, Hoffstein, & Otte 2023 on Nomics spot data) examine 30-day lookback quintile sorts on spot tokens; this research investigates 168-hour / daily rebalance cross-sectional momentum on Bitget perpetuals paired with shuffled return permutation null hypothesis testing and empirical market making.

## Economic mechanism

### Source-reported

1. **Classic Technical Analysis as Overfitting on Noise:**
   Single-asset technical indicators (trend following via EMA crossovers, breakout trading via Donchian channels, and mean reversion via price z-scores) attempt to forecast the absolute price trajectory of individual crypto contracts. When optimized across historical data, apparent "winning" parameters inevitably emerge. However, because return series are fat-tailed and volatile, mining multiple parameter configurations over dozens of assets generates false positives simply through selection bias. When subjected to a rigorous null control—shuffling return sequences to eliminate time-series autocorrelation while preserving marginal return variance and kurtosis—the identical optimization pipeline identifies more "profitable" assets on noise than on real data. Classic TA in crypto perpetuals is indistinguishable from random chance.

2. **Cross-Sectional Relative-Strength Persistence:**
   In contrast to absolute price direction, relative cross-sectional dispersion among liquid crypto assets exhibits structural persistence over multi-day horizons. When large-cap assets experience divergent fundamental adoption, capital rotation, or narrative momentum, relative winners tend to continue outperforming relative losers over a 7-day window. Longing the top performers while shorting the bottom performers in equal dollar amounts neutralizes broad crypto beta (market direction), leaving exposure concentrated in the relative return spread.

3. **Continuous Market Making and Adverse Selection Cancellation:**
   A naive market maker quoting a fixed percentage spread (e.g., $\pm 0.02\%$) on crypto perpetuals sits outside the narrow natural spread of major contracts (such as BTC, where the book spread is $\approx 0.0001\%$). Orders placed at static distances fill predominantly when toxic flow aggressively sweeps through the order book, creating severe adverse selection (buying falling knives and selling rallies). Quoting half-spreads proportional to realized volatility ($2.5 \times \text{rolling 1m volatility}$) places quotes dynamically where normal inventory fluctuations occur. In expectation, earned bid-ask spread capture exactly offsets adverse selection costs, resulting in statistical breakeven volume generation. Crucially, attempting to skew quotes against inventory to flatten positions causes the market maker to sell at a discount into persistent adverse trends, worsening performance.

### Research interpretation

The primary methodological value of this research is the rigorous operationalization of the **shuffled-return null hypothesis test** for crypto derivatives:
- **Destruction of Causal Structure vs. Preservation of Marginals:** Standard statistical tests often assume Gaussian returns. Shuffling empirical returns randomly destroys time-series dependence (autocorrelation, lead-lag, momentum, mean reversion) while preserving the exact empirical marginal distribution, volatility clustering proxies, and fat-tailed extremes. Any proposed alpha strategy whose in-sample or out-of-sample performance cannot decisively beat the distribution of shuffled runs is an artifact of data snooping.
- **The Negative Mean of the Null:** On pure noise, an active trading strategy suffers from fees, slippage, and turnover drag, generating a strongly negative expected Sharpe ratio (mean $-0.73$). A strategy that produces a positive out-of-sample Sharpe against this hurdle demonstrates that its gross return exceeds transaction friction, though a small sample ($N=10$, $p < 0.10$) must be treated as weak preliminary evidence rather than confirmed alpha.
- **Microstructure Inventory Drag:** The finding that inventory skewing reduces profitability from $+\$7.13$ to $-\$24.35$ highlights that crypto perpetual trends are autocorrelated at short horizons; market makers cannot liquidate adverse inventory by aggressively lowering ask quotes without being penalized by momentum continuation.

## Signal

The repository implements and evaluates three distinct components:

### 1. Falsification of Classic Single-Asset Technical Analysis (EMA Trend, Donchian Breakout, Z-Score Reversion)
- **Universe:** 33 Bitget USDT-M perpetual contracts (`source-reported`).
- **Data Interval:** 1-hour OHLCV bars over 360 calendar days (`source-reported`).
- **Strategy Families Evaluated:**
  - *EMA Trend:* Fast span $\in \{8, 12, 20, 34\}$, Slow span $\in \{48, 100, 150\}$, separation band threshold $\in \{0.0, 0.01\}$ (`source-reported`). Signal $= +1.0$ if $(\text{EMA}_{\text{fast}} - \text{EMA}_{\text{slow}}) / \text{EMA}_{\text{slow}} > \text{band}$, $-1.0$ if $< -\text{band}$, else $0.0$ (`source-reported`).
  - *Donchian Breakout:* Lookback $\in \{20, 40, 60, 100, 150\}$ (`source-reported`). Signal $= +1.0$ if Close $> \text{High}_{\text{rolling}}(L)[-1]$, $-1.0$ if Close $< \text{Low}_{\text{rolling}}(L)[-1]$, forward-filled (`source-reported`).
  - *Z-Score Mean Reversion:* Lookback $\in \{24, 48, 96\}$, entry threshold $\in \{1.5, 2.0, 2.5\}$ (`source-reported`). Signal $= -1.0$ if $z > \text{entry}$, $+1.0$ if $z < -\text{entry}$, else $0.0$ (`source-reported`).
- **Discipline & Selection Rule:** Train on first 66% of sample, test on final 34%. Best parameter set chosen by highest Sharpe on train (minimum 20 trades). Evaluated on test; counted as robust only if Net Return $> 0$ on train, Net Return $> 0$ on test, and Net Edge in bps $> 0$ on test (`source-reported`).
- **Shuffled Return Null:** Returns are randomly permuted per asset; high/low ranges relative to close are shuffled synchronously to preserve candle geometry. The identical search grid is executed on shuffled data across multiple runs (`source-reported`).

### 2. Survivorship-Free Cross-Sectional Relative-Strength Momentum
- **Universe:** 12 established majors liquid at least one year prior: `["BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "XRPUSDT", "DOGEUSDT", "ADAUSDT", "LINKUSDT", "XLMUSDT", "UNIUSDT", "NEARUSDT", "SUIUSDT"]` (`source-reported`). Pre-filtering by current turnover is rejected as lookahead bias (`source-reported`).
- **Signal Formation Timestamp:** Daily rebalance cadence (`hold_hours` = 24), evaluated at 1-hour bar closes (`source-reported`). Research-proposed operational boundary: 00:00 UTC (`research-proposed`).
- **Lookback Window:** 168 hours (7 calendar days) (`source-reported`).
- **Ranking Function:** Trailing 168-hour return $R_{i,t} = P_{i,t} / P_{i,t-168} - 1.0$ (`source-reported`). Requires at least $2K$ valid assets with history; returns empty if history is insufficient (`source-reported`).
- **Portfolio Construction:**
  - Sort valid assets by $R_{i,t}$ (`source-reported`).
  - Long the top $K=3$ strongest assets (`source-reported`).
  - Short the bottom $K=3$ weakest assets (`source-reported`).
  - Dollar-neutral equal weighting: $w_{i} = +1/K$ for longs, $w_{i} = -1/K$ for shorts (`source-reported`).
- **Gross Leverage & Sizing Viability:**
  - Default gross leverage: 2.0x equity (`source-reported`).
  - Weight per leg: $\text{leverage} / 2K = 2.0 / 6 = 0.333 \times \text{equity}$ (`source-reported`).
  - Bitget minimum order size constraint: $\$5.00$ USDT minimum per leg (`source-reported`).
  - Sizing viability rule: Minimum equity required is $\$5.00 \times 2K / \text{leverage} = \$5 \times 6 / 2.0 = \$15.00$; strategy declines to trade below $\$15.00$ equity to prevent unhedged directional imbalance (`source-reported`).
- **Risk Halt:** Halt trading if portfolio session drawdown exceeds 30% (`source-reported`).

### 3. Volatility-Adaptive Continuous Market Making
- **Universe:** High-liquidity Bitget perpetuals (`SOLUSDT`, `ETHUSDT`, `BTCUSDT`, `XLMUSDT`, `SUIUSDT`, `NEARUSDT`, etc.) (`source-reported`).
- **Volatility Estimator:** Mean absolute 1-minute return over rolling 60-minute window: $\text{vol}_t = \frac{1}{60} \sum_{i=0}^{59} |P_{t-i} / P_{t-i-1} - 1|$ (`source-reported`). Mean absolute deviation is preferred over sample standard deviation to reduce sensitivity to crypto minute fat-tail spikes (`source-reported`).
- **Quote Placement:**
  - Half-width: $\text{half} = \text{mid} \times \text{vol}_t \times 2.5$ (`source-reported`).
  - Bid price: $P_{\text{bid}} = \text{mid} - \text{half}$ (`source-reported`).
  - Ask price: $P_{\text{ask}} = \text{mid} + \text{half}$ (`source-reported`).
  - Quote sanity guard: Returns `None` if $P_{\text{bid}} \ge P_{\text{ask}}$ or $P_{\text{bid}} \le 0$ to prevent self-crossing (`source-reported`).
- **Requote Throttling & Drift Threshold:**
  - Evaluation frequency: Every 15 seconds (`source-reported`).
  - Drift barrier: Requote only if new quote drifts by $\ge 0.25 \times \text{vol}_t \times \text{mid}$ from existing resting quote to prevent cancel/replace layering flags (`source-reported`).
- **Execution Order Type:** Post-only limit orders (`source-reported`).
- **Inventory Control:**
  - Hard cap at 10 orders of inventory notional (`max_inventory_orders` = 10) (`source-reported`). If inventory reaches $+10 \times \text{order\_usdt}$, bids are suppressed; if $-10 \times \text{order\_usdt}$, asks are suppressed (`source-reported`).
  - Inventory skew factor: Set strictly to $0.0$ (`source-reported`). Skewing quotes against inventory is empirically verified to degrade performance (`source-reported`).

## Required data

- **Instruments:** USDT-Margined Perpetual Contracts listed on Bitget (`source-reported`).
- **Universe:**
  - Classic TA: 33 active Bitget perpetual contracts (`source-reported`).
  - Cross-Sectional Momentum: 12 pre-defined liquid majors (`BTCUSDT`, `ETHUSDT`, `BNBUSDT`, `SOLUSDT`, `XRPUSDT`, `DOGEUSDT`, `ADAUSDT`, `LINKUSDT`, `XLMUSDT`, `UNIUSDT`, `NEARUSDT`, `SUIUSDT`) established as liquid 1 year prior (`source-reported`).
  - Market Making: Liquid contracts with active top-of-book depth (`source-reported`).
- **Timeframe:**
  - 1-hour OHLCV bars for classic TA sweeps and cross-sectional momentum (`source-reported`).
  - 1-minute OHLCV bars for market maker volatility estimation and backtesting replay (`source-reported`).
  - 15-second requote cycle for live market maker execution (`source-reported`).
- **Required Fields:**
  - Open, High, Low, Close, Volume (`source-reported`).
  - Mid price, live account equity, and current position sizes (`source-reported`).
- **Point-in-Time Discipline:**
  - Cross-sectional momentum rebalances use strictly lagged returns $P_{t-1} / P_{t-169} - 1.0$ formed at bar close $t-1$, entering at the open of bar $t$ (`source-reported`).
  - In market maker backtesting, realized volatility requires $W+1$ closes to compute $W$ returns without lookahead (`source-reported`).
- **Fee and Contract Data:**
  - Maker fee rate: $0.020\%$ ($0.0002$) (`source-reported`).
  - Taker fee rate: $0.060\%$ ($0.0006$) (`source-reported`).
  - Uniform fee schedule across all 787 Bitget contracts; zero maker rebate on futures (`source-reported`).

## Execution assumptions

- **Cross-Sectional Momentum:**
  - Orders executed at bar close / next bar open (`source-reported`).
  - Fill model assumes full fills with 2 bps maker fee when passive rebalancing is modeled, or 6 bps taker fee for aggressive rebalancing (`source-reported`).
  - Minimum trade threshold: $\$5.00$ USDT per leg to satisfy exchange minimum notional constraints (`source-reported`).
  - Turn cost modeled as $\Delta w \times \text{fee}$ (`source-reported`).
- **Market Making:**
  - Post-only limit orders placed simultaneously at bid and ask (`source-reported`).
  - Replay fill model: A resting bid fills if the 1-minute bar's Low trades at or below the bid price; resting ask fills if the bar's High trades at or above the ask price (`source-reported`).
  - Fill queue priority: Assumes fills when price trades through the quote, which is accurate outside the touch but optimistic at the exact touch (`source-reported`).
  - Maker fee of $0.020\%$ paid on every completed fill (`source-reported`).
  - Mark-to-market accounting: Revaluation calculated against the previous bar's close rather than mid-bar fill price to capture inventory drift accurately (`source-reported`).
  - Operational blocker: Bitget returns error `40035 — complete KYC first` on order entry; identity verification is required before live execution (`source-reported`).

## Evidence

### Source-reported

1. **Classic Technical Analysis Falsification (Null Hypothesis Permutation):**
   - Sample: 33 Bitget perpetuals, 1H bars, 360 calendar days (`source-reported`).
   - Grid search: Trend EMA, Donchian breakout, Z-score mean reversion (`source-reported`).
   - Real Data Scan Result: 11 of 33 assets passed the train/test profitability filter (`source-reported`).
   - Shuffled Null Permutation Result: The identical grid search and selection procedure on shuffled returns passed an average of **13.6 assets** across repeated trials (`source-reported`).
   - Statistical Conclusion: The empirical pass rate on real crypto data is worse than expected from pure noise ($11 < 13.6$). Classic technical indicators fail to provide an edge over random coin flips (`source-reported`).
   - Walk-Forward Confirmation: Real walk-forward produced 10 passing assets, falling directly inside the shuffled null range of 4–12 assets (`source-reported`).

2. **Cross-Sectional Momentum Walk-Forward Performance:**
   - Sample: 12 liquid majors over 360 days of 1H data (9 rolling windows of 90-day train / 30-day test) (`source-reported`).
   - Out-of-Sample Total Net Return: **$+42.9\%$** (`source-reported`).
   - Walk-Forward Annualized Sharpe Ratio: **$1.56$** (`source-reported`).
   - Maximum Drawdown: **$-24.1\%$** (`source-reported`).
   - Shuffled Return Null Comparison (10 independent runs of shuffled returns):
     - Null Mean Return: **$-27\%$** (`source-reported`).
     - Null Mean Sharpe: **$-0.73$** (`source-reported`).
     - Null Maximum Sharpe: **$1.27$** (`source-reported`).
     - Null Exceedance: **0 of 10** shuffled null runs reached the real Sharpe of $1.56$ ($p < 0.10$) (`source-reported`).
   - Economic significance: Because trading pure noise incurs turnover fees without signal, the null distribution has a negative mean ($-0.73$). The real strategy's Sharpe of $1.56$ decisively separates from the negative null baseline (`source-reported`).

3. **Market Making Spread Optimization and Adverse Selection:**
   - Evaluated over 56 asset-days of Bitget 1-minute data across `SOLUSDT`, `ETHUSDT`, `BTCUSDT`, and `XLMUSDT` per $\$10$ order size (`source-reported`):
     - *2.0x Volatility:* P&L $-\$0.31$/day, 34% days positive, volume $\$2,713$/day (loses to adverse selection) (`source-reported`).
     - *2.5x Volatility (Optimal):* P&L **$+\$0.02$/day** ($\pm \$0.17$ standard error), 52% days positive, volume **$\$1,652$/day** (breakeven in expectation, maximum volume) (`source-reported`).
     - *3.0x Volatility:* P&L $+\$0.28$/day, 62% days positive, volume $\$1,034$/day (profitable, lower volume) (`source-reported`).
     - *4.0x Volatility:* P&L $+\$0.23$/day, 62% days positive, volume $\$444$/day (lower volume) (`source-reported`).
   - Non-Overlapping In-Sample vs. Out-of-Sample Stability:
     - Training half spread capture: **$+\$218.05$** (`source-reported`).
     - Test half spread capture: **$+\$218.94$** (`source-reported`).
     - Across 10 symbols, earned spread capture is stable to within one dollar ($\$1$) across non-overlapping periods, and is almost exactly cancelled by adverse selection, producing net zero P&L (`source-reported`).
   - Harm of Inventory Skewing:
     - Skew factor $0.0$: **$+\$7.13$** P&L (`source-reported`).
     - Skew factor $0.5$: **$-\$18.88$** P&L (`source-reported`).
     - Skew factor $1.0$: **$-\$24.35$** P&L (`source-reported`).
     - Skewing quotes to unload inventory forces the bot to sell into adverse directional momentum at discounted prices (`source-reported`).
   - Risk and Portfolio Scaling:
     - Volume scales linearly with symbol count ($\$1,949$/day per symbol per $\$10$ order) (`source-reported`).
     - Daily P&L risk scales sublinearly as **$n^{0.82}$** (daily sigma $\$1.81$ per symbol per $\$10$ order) (`source-reported`). Spreading across multiple symbols provides mathematical risk diversification over single-contract sizing (`source-reported`).

### Independently reproduced

Not independently reproduced. This record is a normalized research capture of external public empirical research and implementation from `MarxMad/Bitget-Alg`.

### Negative evidence

- Single-asset technical analysis (trend EMA, Donchian breakout, Z-score mean reversion) is proven to be an empirical failure on crypto perpetuals: 11 real passes vs. 13.6 expected by random chance on shuffled return nulls (`source-reported`).
- Prior fixed-spread market maker (quoting static mid $\pm 0.02\%$) lost $0.025\%\text{--}0.049\%$ of every dollar of volume generated due to severe adverse selection on narrow-spread contracts (`source-reported`).
- Daily volatility risk in market making is substantial: on a small $\$20$ account, a single adverse day can lose up to $\$3.44$ (17.2% of account equity) because daily sigma is $\$1.30\text{--}\$1.81$ per symbol (`source-reported`).
- Cross-sectional momentum empirical significance clears only $p < 0.10$ (not $p < 0.01$), evaluated across a single 360-day market regime, and remains vulnerable to abrupt leadership rotation (`source-reported`).

## Falsification plan

To falsify the proposed cross-sectional momentum and market making hypotheses, the following operational tests are specified:

1. **Permutation Null Significance Test ($N=500$ Shuffled Runs):**
   - *Test:* Run 500 independent shuffled-return permutations of the 12-major 1H dataset, breaking cross-asset and temporal correlation while preserving individual asset marginal return distributions.
   - *Falsification Criterion:* If the real walk-forward Sharpe of 1.56 falls below the 95th percentile of the shuffled distribution ($p \ge 0.05$), the cross-sectional momentum hypothesis is falsified as indistinguishable from random data mining (`research-defined falsification threshold`).

2. **Cross-Regime Directional Stress Test (Bear and Compression Regimes):**
   - *Test:* Evaluate the 168h/24h cross-sectional momentum strategy over an out-of-sample 2022–2023 crypto winter sample and a low-volatility range-bound regime.
   - *Falsification Criterion:* If out-of-sample Sharpe drops below $0.0$ or maximum drawdown exceeds $35\%$, the claim of structural market-neutral dispersion capture is falsified, proving that the 2025–2026 result was an artifact of a persistent macro bull regime (`research-defined falsification threshold`).

3. **Taker Execution and Fee Stress Test:**
   - *Test:* Evaluate cross-sectional momentum rebalances under aggressive taker execution at $0.060\%$ fee plus 5 bps adverse slippage per leg (11 bps one-way, 22 bps round-trip).
   - *Falsification Criterion:* If the net walk-forward return flips negative under realistic taker costs, the strategy is falsified as a non-tradable theoretical construct (`research-defined falsification threshold`).

4. **Market Maker Adverse Selection Stress Test on Out-of-Sample Volatility Regimes:**
   - *Test:* Replay the 2.5x volatility market maker across high-volatility cascade days (e.g., liquidation unwind events with intraday volatility $> 3\times$ baseline).
   - *Falsification Criterion:* If net trading loss exceeds $-0.10\%$ (10 bps) of traded volume over a 30-day continuous window, the breakeven claim is falsified, demonstrating uncompensated tail adverse selection (`research-defined falsification threshold`).

## Crypto portability

- **Portability Status:** Direct (`source-reported`).
- **Venue & Contract Context:** The strategy was designed, implemented, and empirically evaluated directly on Bitget USDT-Margined perpetual futures contracts (`source-reported`).
- **Crypto-Specific Market Dynamics:**
  - *Unified Account Mode:* Bitget Unified v3 API handles cross-margin collateral, whereas v2 endpoints return fatal error 40085 (`source-reported`).
  - *Funding Cost Interaction:* The dollar-neutral momentum portfolio holds long and short perpetual contracts simultaneously. In periods of extreme positive market funding, short positions harvest funding while long positions pay; funding payments must be explicitly accounted for in net performance (`research-proposed`).
  - *24/7 Continuous Trading:* Daily rebalancing at 00:00 UTC occurs without exchange halts; however, weekend liquidity compression may increase slippage during rebalancing (`research-proposed`).
  - *KYC Regulatory Blocker:* Real execution requires complete KYC verification on Bitget; unverified accounts cannot place orders (`source-reported`).

## Limitations

- **Small Shuffled Sample Size:** The primary source ran only 10 shuffled null iterations ($p < 0.10$), which provides directional evidence but lacks rigorous statistical significance ($p < 0.01$) (`source-reported`).
- **Regime Concentration:** Empirical backtest spans 360 days within a single macro cycle (2025–2026); resilience across prolonged bear markets or sustained low-dispersion environments is unproven (`source-reported`).
- **Touch-Fill Optimism in MM Backtest:** The 1-minute bar market maker simulation assumes fills when the bar's extreme touches the quote price, which is optimistic for resting quotes near the touch where queue priority dictates execution (`source-reported`).
- **Single-Venue Implementation:** All empirical results originate from Bitget's order book and fee structure (2 bps maker, 6 bps taker); portability to Binance, Bybit, or Hyperliquid requires re-calibrating quote widths to venue-specific book depth and tick size (`research-proposed`).

## Implementation status

- Frontmatter `implementation_status: not-implemented`.
- No code from this repository has been integrated into the internal research, backtesting, or execution infrastructure.
- No NautilusTrader or PyBroker modules have been developed or run for this strategy family.
- Paper trading, testnet execution, and live trading have not been conducted.

## Adoption boundary

- Frontmatter `status: research-only`.
- Frontmatter `adoption: not-approved`.
- Frontmatter `approval_scope: research-only`.
- A strategy research record being present in this repository represents normalized external research material only. It does not constitute validation, approval, or deployment permission for paper, testnet, or live trading systems.

## Related Wiki records

- `crypto-cross-sectional-momentum-30d-top-quintile-7d-2026-08-31.md` (SSRN Drogen, Hoffstein, & Otte 2023 spot momentum quintile study)
- `crypto-perp-alpha-four-cell-regime-falsification-2026-09-13.md` (Xty2750 multi-regime four-cell falsification on crypto perpetuals)
- `crypto-order-flow-online-sgd-microstructure-horizon-cost-falsification-2026-09-13.md` (Coinbase BTC order flow online SGD cost falsification)
- `crypto-funding-carry-fade-turnover-cost-dissipation-falsification-2026-09-12.md` (Binance funding carry turnover cost dissipation)
- `crypto-pairs-trading-cointegration-overfitting-falsification-2026-09-13.md` (Crypto pairs trading cointegration data snooping)

## Sources

- **Primary Source Code and Research Repository:**
  - Author: `MarxMad` / GerryVela (`gerardo.gerry.pedrizco@gmail.com`)
  - Title: *Bitget-Alg: Bitget perpetuals: market making and cross-sectional momentum, with the significance testing that rejected everything else*
  - Repository URL: [https://github.com/MarxMad/Bitget-Alg](https://github.com/MarxMad/Bitget-Alg)
  - Full Immutable Commit SHA: `fe7b50dbdf519f2db1018a8967504812e0d72ce0`
  - Canonical Tree URL: [https://github.com/MarxMad/Bitget-Alg/tree/fe7b50dbdf519f2db1018a8967504812e0d72ce0](https://github.com/MarxMad/Bitget-Alg/tree/fe7b50dbdf519f2db1018a8967504812e0d72ce0)
  - Commit Timestamp: `2026-09-12T21:37:42Z`
- **Exchange Fee Contract Reference:**
  - Bitget USDT-M Perpetual Instruments API (`/api/v3/market/instruments`): Maker fee $0.020\%$, Taker fee $0.060\%$, no maker rebates on perpetual futures.
