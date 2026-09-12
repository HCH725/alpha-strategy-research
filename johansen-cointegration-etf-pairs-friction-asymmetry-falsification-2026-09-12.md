---
schema: strategy-research-record-v1
title: "Johansen Cointegration Basket and Pairs Trading: Empirical Falsification of Daily Mean-Reversion Alpha under Friction Asymmetry, Net-Exposure Drift, and Volatility-Expanding Z-Score Stops"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - pairs-trading
  - cointegration
  - johansen-test
  - etf-pairs
  - falsification
  - transaction-costs
  - multiple-testing
  - benjamini-hochberg
status: research-only
confidence: high
source_as_of: 2026-09-12
sources:
  - "https://github.com/shaunak-batra/BasketTradingBO/tree/fe031d5151ab00ba2061312ddf58e31964987565"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Johansen Cointegration Basket and Pairs Trading: Empirical Falsification of Daily Mean-Reversion Alpha under Friction Asymmetry, Net-Exposure Drift, and Volatility-Expanding Z-Score Stops

## Provenance

- **Author:** Shaunak Batra (`shaunak-batra`).
- **Title:** "BasketTradingBO — Statistical Arbitrage Basket Trading System with Bayesian Optimization and Multi-Pair Falsification Audit"
- **Primary Source Repository:** [https://github.com/shaunak-batra/BasketTradingBO](https://github.com/shaunak-batra/BasketTradingBO)
- **Immutable Commit SHA:** `fe031d5151ab00ba2061312ddf58e31964987565` (`source-reported`).
- **Date / As-Of:** 2026-09-12 (`source-reported`).
- **License:** MIT License (`source-reported`).
- **Key Audited Artifacts in Repository:**
  - Protocol Configurations: [`config/config.yaml`](https://github.com/shaunak-batra/BasketTradingBO/blob/fe031d5151ab00ba2061312ddf58e31964987565/config/config.yaml), [`config/config_v3.yaml`](https://github.com/shaunak-batra/BasketTradingBO/blob/fe031d5151ab00ba2061312ddf58e31964987565/config/config_v3.yaml) (`source-reported`).
  - 60-Pair Pre-Registered Evaluation Universe: [`config/universe_v3.yaml`](https://github.com/shaunak-batra/BasketTradingBO/blob/fe031d5151ab00ba2061312ddf58e31964987565/config/universe_v3.yaml) (`source-reported`).
  - Johansen Engine & Exposure Verification: [`src/cointegration/engine.py`](https://github.com/shaunak-batra/BasketTradingBO/blob/fe031d5151ab00ba2061312ddf58e31964987565/src/cointegration/engine.py) (`source-reported`).
  - Spread Dynamics & AR(1) Half-Life: [`src/cointegration/spread.py`](https://github.com/shaunak-batra/BasketTradingBO/blob/fe031d5151ab00ba2061312ddf58e31964987565/src/cointegration/spread.py) (`source-reported`).
  - Z-Score State Machine: [`src/strategy/signals.py`](https://github.com/shaunak-batra/BasketTradingBO/blob/fe031d5151ab00ba2061312ddf58e31964987565/src/strategy/signals.py) (`source-reported`).
  - Cash-Accounted Backtest Engine: [`src/backtesting/backtester.py`](https://github.com/shaunak-batra/BasketTradingBO/blob/fe031d5151ab00ba2061312ddf58e31964987565/src/backtesting/backtester.py) (`source-reported`).
  - Walk-Forward Stitching & Filter Validation: [`src/backtesting/walk_forward.py`](https://github.com/shaunak-batra/BasketTradingBO/blob/fe031d5151ab00ba2061312ddf58e31964987565/src/backtesting/walk_forward.py) (`source-reported`).
  - Empirical Audit & Defect Catalog: [`docs/AUDIT.md`](https://github.com/shaunak-batra/BasketTradingBO/blob/fe031d5151ab00ba2061312ddf58e31964987565/docs/AUDIT.md) (`source-reported`).
  - Empirical Findings & Pre-Registered Protocol: [`docs/RESEARCH_V3.md`](https://github.com/shaunak-batra/BasketTradingBO/blob/fe031d5151ab00ba2061312ddf58e31964987565/docs/RESEARCH_V3.md), [`docs/RESULTS_V3.md`](https://github.com/shaunak-batra/BasketTradingBO/blob/fe031d5151ab00ba2061312ddf58e31964987565/docs/RESULTS_V3.md), [`results/v3_universe/summary.md`](https://github.com/shaunak-batra/BasketTradingBO/blob/fe031d5151ab00ba2061312ddf58e31964987565/results/v3_universe/summary.md) (`source-reported`).
- **Repository Deduplication Audit:** A comprehensive audit across all existing markdown strategy records in `alpha-strategy-research` confirmed zero pre-existing records citing `shaunak-batra` or `BasketTradingBO`. Related statistical arbitrage and cointegration records in the repository (such as `sp500-statistical-arbitrage-johansen-ou-ablation-multiple-testing-2026-09-12.md` based on `pdwi2020/p4_stat_arb` commit `3b3cb640`, `crypto-perpetual-pairs-trading-kalman-cointegration-falsification-2026-09-11.md`, and `commodity-soybean-crush-spread-cointegration-stat-arb-2026-09-12.md`) evaluate 4-way OU estimators on five equity sector pairs with Hansen SPA, crypto perpetual funding-rate Kalman tracking, or physical soybean crush margins. Batra's research provides an independent, pre-registered 60-pair multi-family ETF walk-forward falsification study with positive controls (`GLD/IAU` and `SPY/IVV`), a 13-point accounting defect audit, a mathematical breakdown of z-score stop failure under rolling volatility expansion, and an empirical proof of the friction asymmetry barrier.

## Economic mechanism

### Source-reported

Statistical arbitrage via cointegration posits that economically related assets (such as equity index tracking shares, commodity proxies, or industry peers) share a stationary long-term equilibrium relationship. While individual asset prices follow non-stationary $I(1)$ processes, a specific linear combination of their log prices forms a stationary $I(0)$ spread $S_t = \sum_i w_i \log P_{i,t}$, exhibiting mean reversion toward an equilibrium level. When the spread deviates beyond historical standard deviation thresholds, a market-neutral mean-reversion trade is opened (buying the undervalued leg and shorting the overvalued leg), anticipating profit when the spread reverts.

Through systematic walk-forward empirical testing and controlled ablation across 60 ETF pairs from 2012 to 2024, Batra demonstrates three fundamental structural failure modes that falsify the operational profitability of daily cointegration trading:

1. **The Friction Asymmetry Barrier ("The Controls Punchline"):**
   Evaluating two positive controls—pairs guaranteed to share an identical underlying economic asset (`GLD/IAU` for physical gold, and `SPY/IVV` for the S&P 500)—reveals an insurmountable economic barrier. The pipeline successfully identifies cointegration in these pairs (trading 24/26 and 16/26 walk-forward windows). However, because arbitrage is highly efficient, genuine mean-reverting deviations at daily closing frequency are tiny: gross P&L averages only $+0.53\text{ bps}$ (`GLD/IAU`) and $+0.51\text{ bps}$ (`SPY/IVV`) per round-trip trade. Meanwhile, realistic trading costs ($5\text{ bps}$ per side across two legs plus borrow) average $10.3\text{ bps}$ and $10.2\text{ bps}$ per trade. Where cointegration is unambiguous, the tradable spread is twenty times smaller than the transaction cost. Conversely, where spreads are wide enough to pay for trading, cointegration is statistically unstable across out-of-sample periods.
2. **Directional Net-Exposure Drift in Johansen Eigenvectors:**
   The Johansen trace test identifies a cointegrating vector $\beta$, but the mathematics of maximum likelihood vector autoregression does not constrain the signs of the weights. Consequently, in over $50\%$ of traded windows in unconstrained setups, the leading eigenvector yields weights of identical signs (e.g., both positive on `XOM/CVX`, or $+0.58, -0.19, +0.22$ on `TSLA/NFLX/PLTR`). A nominal "spread trade" thus becomes an unhedged $50\%\text{--}60\%$ net directional bet on the broader market. When market crashes occur (such as the February–March 2020 COVID shock or the 2022 tech selloff), these pseudo-spreads suffer catastrophic equity drawdowns ($-51.8\%$ on `XOM/CVX`).
3. **Failure of Z-Score Stops under Volatility Expansion:**
   Standard textbook implementations define stop-loss exits in z-score units (e.g., exit if $|z_t| \ge 4.0$). During an acute structural break or liquidity crash, the raw price divergence explodes, but the trailing 60-day rolling standard deviation $\sigma_L$ expands just as fast. Because the denominator scales concurrently with the numerator, the z-score never reaches the nominal stop threshold (peaking at $3.73$ on `XOM/CVX` in March 2020), holding the full loss until the position loses over $50\%$ of capital.
4. **The Naive Backtester Accounting Defect:**
   Standard naive backtests frequently compute portfolio value as `capital + position_values - costs`. Because opening an asset is an exchange of cash for shares, marking equity to gross position value without deducting the matching cash outlay artificially credits the portfolio with the asset's gross market value on entry, turning random noise into apparent backtest alpha.

### Research interpretation

The findings formalize the boundary between statistical significance and tradable economic alpha at low frequencies:
- In highly liquid exchange-traded products, the continuous presence of Authorized Participants (APs) and intraday high-frequency arbitrageurs rapidly impounds cross-asset pricing efficiency within seconds or minutes. At daily closing bar resolution, the remaining stationary mispricing is compressed to sub-basis-point residual noise.
- Applying leverage does not rescue the strategy: because gross returns ($\sim 0.5\text{ bps}$) and execution costs ($\sim 10.2\text{ bps}$) both scale linearly with traded notional, increasing leverage merely scales a mathematically negative unit expectancy.
- Normalizing deviations by an empirical rolling standard deviation creates a dangerous non-linear feedback loop in tail regimes: standardizing an expanding variance masks catastrophic price divergence. Robust statistical arbitrage architectures must decouple risk truncation (dollar capital stops and holding time stops) from signal generation.

## Signal

The normalized trading strategy operates under a rolling walk-forward protocol with strict pre-trade filtering, cash accounting, and multi-tier risk exits:

### 1. Estimation & Pre-Trade Screening (Walk-Forward Fold)
- **Formation Window ($L_{\text{form}}$):** 504 trading days ($\approx 2$ years) of daily log closing prices (`source-reported`).
- **Trading Window ($L_{\text{trade}}$):** 126 trading days ($\approx 6$ months), non-overlapping out-of-sample execution (`source-reported`).
- **Cointegration Test:** Johansen trace test on log prices with constant in VECM ($\text{det\_order} = 0$), $k_{\text{ar\_diff}} = 1$ lagged difference (`source-reported`).
- **Cointegration Significance Gate:** Trace test must reject the null hypothesis of cointegrating rank $r \le 0$ at the $\alpha = 0.05$ critical threshold (`source-reported`). If unrejected, the fold is discarded ($0$ trades) (`source-reported`).
- **Weight Extraction & Normalization:** Leading eigenvector $w$ corresponding to the largest eigenvalue, normalized such that:
  $$\sum_i |w_i| = 1.0, \quad w_{\text{first non-zero}} > 0 \quad \text{(`source-reported`)}$$
- **Hedged Net-Exposure Gate (`v3.0`):**
  $$\text{net\_exposure} = \frac{|\sum_i w_i|}{\sum_i |w_i|} \le 0.20 \quad \text{(`source-reported`)}$$
  If net exposure exceeds $20\%$, the basket is rejected as a directional bet rather than a market-neutral spread (`source-reported`).
- **Half-Life Gate:** Mean-reversion half-life $h = \ln(0.5) / \ln(\phi)$ estimated via OLS on $dS_t = a + b S_{t-1} + \epsilon_t$, $\phi = 1 + b$ (`source-reported`). The fold is rejected if $h > 126$ trading days (`source-reported`).

### 2. Spread & Z-Score State Machine
- **Spread Definition:**
  $$S_t = \sum_i w_i \log P_{i,t} \quad \text{(`source-reported`)}$$
- **Rolling Z-Score:**
  $$z_t = \frac{S_t - \mu_{L, t}}{\sigma_{L, t}} \quad \text{(`source-reported`)}$$
  computed over trailing window $L = 60$ trading days (`source-reported`). Warm-up utilizes the final 60 bars of the formation window, strictly avoiding future data leakage (`source-reported`).
- **State Machine Transitions:**
  - Flat $\rightarrow$ Long Spread: Triggered when $- \text{stop\_z} < z_t \le - \text{entry\_z}$ (where $\text{entry\_z} = 2.0$, $\text{stop\_z} = 4.0$) (`source-reported`).
  - Flat $\rightarrow$ Short Spread: Triggered when $\text{entry\_z} \le z_t < \text{stop\_z}$ (`source-reported`).
  - Long $\rightarrow$ Flat (Reversion Exit): Triggered when $z_t \ge - \text{exit\_z}$ (where $\text{exit\_z} = 0.5$) (`source-reported`).
  - Short $\rightarrow$ Flat (Reversion Exit): Triggered when $z_t \le \text{exit\_z}$ (`source-reported`).
  - Z-Score Stop Exit: Exit long if $z_t \le - \text{stop\_z}$ ($-4.0$); exit short if $z_t \ge \text{stop\_z}$ ($+4.0$) (`source-reported`).
  - Disarm Invariant: After a stop exit, or if $|z_t| \ge \text{stop\_z}$ while flat, the signal generator is disarmed and cannot open new positions until $|z_t| < \text{entry\_z}$ (`source-reported`).

### 3. Execution & Risk Overrides (`v3.0` Rules)
- **Capital Stop Loss:** Close position immediately if accumulated mark-to-market trade loss reaches or exceeds $10\%$ of entry allocated equity (`stop_loss_fraction: 0.10`) (`source-reported`).
- **Time Stop:** Close position immediately if holding period reaches or exceeds 36 trading days (`max_holding_bars: 36`, approximately $3\times$ median formation half-life of 12.2 days) (`source-reported`).
- **Volatility-Targeted Sizing:**
  $$\text{target\_gross} = \min\left(1.0, \frac{\sigma_{\text{target}}}{\sigma_{\text{formation\_spread}}}\right) \quad \text{(`source-reported`)}$$
  where $\sigma_{\text{target}} = 0.10$ ($10\%$ annualized volatility), capped at $1.0\times$ equity (`max_gross: 1.0`) (`source-reported`).
- **Execution Timing:** Signals calculated at the close of trading day $t$ are executed at the close of day $t + 1$ (`execution_lag: 1`) (`source-reported`).

## Required data

- **Universe Definition:** 60 ETF pairs grouped across 17 economic families (`broad_us_equity`, `precious_metals`, `us_banks`, `regional_banks`, `energy`, `oil_services`, `semiconductors`, `biotech`, `retail`, `real_estate`, `utilities`, `treasury_bonds`, `corporate_bonds`, `high_yield`, `emerging_markets`, `developed_europe`, `developed_asia`) (`source-reported`).
- **Constituent Selection Rule:** All unordered pairs within each economic family; zero pairs across families (`source-reported`).
- **Control Pairs:** `GLD / IAU` (physical gold tracking) and `SPY / IVV` (S&P 500 equity tracking) included as positive controls (`source-reported`).
- **Price Series:** Daily closing prices adjusted for corporate actions and splits (`source-reported`).
- **Sample Window:** 2010-01-01 to 2025-01-01 (15 calendar years; 2010–2011 initial formation window, 2012-01-04 to 2024-12-31 out-of-sample evaluation window spanning 13 years) (`source-reported`).
- **Missing Data Threshold:** Pairs must have at least 1,000 overlapping bars; maximum missing dates capped at $2\%$ (`max_missing_fraction: 0.02`), otherwise skipped (`source-reported`).

## Execution assumptions

- **Order Timing & Lag:** Signals generated at close $t$ fill at close $t+1$ (`execution_lag: 1`) (`source-reported`).
- **Order Type & Execution:** Market-on-close orders at prevailing closing prices (`source-reported`).
- **Trading Friction:** Flat $5.0\text{ bps}$ per side on traded notional ($0.05\%$), capturing commissions, exchange fees, bid-ask half-spread, and market impact for large liquid ETFs (`source-reported`). Total round-trip cost across two legs is $\approx 10.2\text{--}10.3\text{ bps}$ (`source-reported`).
- **Short Borrow Rate:** $50.0\text{ bps}$ annualized ($0.50\% / 252$ per day) assessed on short leg notional (`borrow_bps_annual: 50.0`) (`source-reported`).
- **Leverage Constraint:** Maximum gross leverage capped strictly at $1.0\times$ equity (`max_gross: 1.0`) (`source-reported`).
- **Cash Mark-to-Market Accounting Identity:**
  $$E_t = E_{t-1} + q_{t-1}^\top (P_t - P_{t-1}) - \frac{b}{252} \sum_i \max(-q_{t-1, i}, 0) P_{t-1, i} - c \sum_i |\Delta q_{t, i}| P_{t, i} \quad \text{(`source-reported`)}$$
  Equity changes strictly through mark-to-market P&L, borrow fees, and trading frictions; purchasing or selling shares is a cash exchange with zero instantaneous equity impact (`source-reported`).

## Evidence

### Source-reported

All quantitative figures below are directly reported by Shaunak Batra (`BasketTradingBO`, commit `fe031d5151ab00ba2061312ddf58e31964987565`, September 12, 2026) across the 13-year out-of-sample evaluation (2012-01-04 to 2024-12-31):

#### 1. Pre-Registered 60-Pair ETF Universe Results (Protocol `config_v3.yaml`, Universe `universe_v3.yaml`)
- **Pairs Defined:** 60; Pairs Evaluated: 60; Pairs Skipped for Data: 0.
- **Pairs Traded:** 42 of 60 pairs traded at least once; 18 pairs had zero qualifying cointegrated windows.
- **Walk-Forward Fold Statistics:** 176 of 1,560 possible 6-month folds traded ($11.3\%$). Folds were skipped as not cointegrated 1,276 times, as unhedged (net exposure $> 0.20$) 102 times, and for half-life $> 126\text{ days}$ 6 times.
- **Total Closed Round-Trip Trades:** 542 trades across all pairs.
- **Median Out-of-Sample Sharpe Ratio (Net of Costs):** **$-0.140$** (vs **$-0.019$** with zero frictions).
- **Pairs with Positive Sharpe Ratio:** 14 of 42 net of costs ($33.3\%$ hit rate); 20 of 42 with zero frictions ($47.6\%$).
- **Equal-Weight Portfolio Performance (2012–2024):**
  - Net Total Return (after costs): **$-0.69\%$** total over 13 years.
  - Net Sharpe Ratio: **$-0.389$** (95% block bootstrap CI: $[-0.90, 0.08]$).
  - Net Probabilistic Sharpe Ratio (PSR): **$0.081$** (8.1% probability true Sharpe > 0).
  - Maximum Drawdown: **$-1.02\%$**.
  - Frictionless Total Return: **$+0.31\%$** total over 13 years (Sharpe **$+0.177$**, CI $[-0.35, 0.66]$, PSR **$0.738$**).
- **Multiple-Testing Deflation:** **0 discoveries out of 60 pairs** surviving Benjamini-Hochberg False Discovery Rate control at $10\%$ on $1 - \text{PSR}$.
- **Per-Trade Unit Economics:**
  - Median Gross P&L per Trade: **$-1.2\text{ bps}$** of traded notional.
  - Median Friction Cost per Trade: **$12.1\text{ bps}$** of traded notional.
  - Only 14 of 42 traded pairs generated positive net P&L after costs.

#### 2. The Decisive Empirical Punchline: Positive Control Pairs
- **`GLD / IAU` (Physical Gold Trusts):**
  - Walk-Forward Windows Traded: 24 of 26 ($92.3\%$).
  - Total Closed Trades: 119 round trips.
  - Spread Realized Volatility: $0.6\%$ annualized.
  - Gross P&L per Trade: **$+0.53\text{ bps}$**.
  - Cost per Trade: **$10.3\text{ bps}$**.
  - Net Sharpe Ratio: **$-2.80$** (Frictionless Sharpe: **$+0.22$**).
- **`IVV / SPY` (S&P 500 Index Funds):**
  - Walk-Forward Windows Traded: 16 of 26 ($61.5\%$).
  - Total Closed Trades: 71 round trips.
  - Spread Realized Volatility: $0.3\%$ annualized.
  - Gross P&L per Trade: **$+0.51\text{ bps}$**.
  - Cost per Trade: **$10.2\text{ bps}$**.
  - Net Sharpe Ratio: **$-2.43$** (Frictionless Sharpe: **$+0.21$**).

#### 3. Cost Sensitivity Ablation across 42 Traded Pairs
- **$0\text{ bps}$ per side:** Median Sharpe **$-0.033$** (19 of 42 pairs positive).
- **$5\text{ bps}$ per side (Base Protocol):** Median Sharpe **$-0.140$** (14 of 42 pairs positive).
- **$10\text{ bps}$ per side:** Median Sharpe **$-0.244$** (12 of 42 pairs positive).
- **$20\text{ bps}$ per side:** Median Sharpe **$-0.341$** (8 of 42 pairs positive).

#### 4. Bayesian In-Sample Optimization Breakdown (Round 1 Baskets)
- In-sample Sharpe achieved via Bayesian threshold tuning: **$1.60\text{--}2.20$**.
- Out-of-sample Sharpe realized on tuned parameters: **$-0.61\text{--}0.49$**.
- Out-of-sample positive fold hit rate: $35\%$ for tuned parameters vs $56\%$ for fixed textbook thresholds.
- Deflated Sharpe Ratio (DSR) averaged $0.73\text{--}0.97$, failing to detect the overfitting because non-stationarity altered the underlying data-generating process between formation and execution windows.

### Independently reproduced

`not independently reproduced`.

### Negative evidence

The entirety of Batra's 60-pair ETF study serves as an empirical falsification of daily close cointegration basket trading:
- Daily frequency cointegration stat-arb on liquid ETFs fails completely out-of-sample, generating zero discoveries under false discovery rate control.
- Even under zero transaction costs, the 60-pair portfolio generates an economically negligible $+0.31\%$ total return over 13 years (Sharpe $+0.177$).
- Z-score stops fail systematically during regime shocks: on `XOM/CVX` in 2020, equity fell $-51.8\%$ while the z-score peaked at $3.73$ (below the $4.0$ stop) due to denominator volatility expansion.

## Falsification plan

To falsify the negative conclusion (i.e., to demonstrate conditions under which cointegration stat-arb generates valid economic alpha):
1. **Intraday Bar Resolution & Microstructure Test:** Transition from daily close execution to 5-minute or 15-minute bars, evaluating whether higher-frequency deviations yield gross spreads exceeding execution frictions.
   - Failure metric: If median gross P&L per trade does not exceed $15\text{ bps}$ under realistic maker/taker fees, the intraday frequency hypothesis is rejected (`research-defined falsification threshold`).
2. **Passive Quoting / Spread-Capturing Execution Test:** Replace taker market-on-close execution with passive limit orders posted at the bid/ask, capturing rather than paying the bid-ask half-spread.
   - Failure metric: If passive fills suffer adverse selection exceeding half the bid-ask spread or reduce fill rates below $40\%$, the passive execution hypothesis is rejected (`research-defined falsification threshold`).
3. **Factor-Residual vs Pairwise Cointegration Ablation:** Test Avellaneda-Lee multi-factor residual statistical arbitrage across a broad stock universe.
   - Failure metric: If multi-factor idiosyncratic residuals yield median trade edge $< 10\text{ bps}$ net of turnover friction, factor stat-arb is rejected (`research-defined falsification threshold`).

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Research Interpretation:** Porting cointegration statistical arbitrage to cryptocurrency markets represents a ported research hypothesis, not demonstrated empirical evidence in the source:
  - *Perpetual Funding Rate Asymmetry:* In crypto perpetual pairs (e.g., cross-exchange funding arbitrage or synthetic basis trading), holding cointegrated spreads incurs 8-hour funding rates. If one leg trades at an elevated positive funding rate while the other is neutral, funding drag will rapidly exceed the modest gross mean-reversion edge.
  - *Exchange Fragmentation & Counterparty Risk:* Exploiting cross-venue crypto spreads requires maintaining collateral across multiple centralized or decentralized venues, exposing the strategy to bridge failures, withdrawal freezes, and venue-specific liquidation mechanics.
  - *The Positive Control Barrier in Crypto:* Highly liquid synthetic pairs (such as `WBTC/BTC` or cross-exchange `BTC/USDT`) exhibit ultra-tight spreads where arbitrage is heavily contested by institutional low-latency firms, whereas pairs with wider spreads (altcoin cross pairs) suffer severe cointegration breakdown and liquidation cascades.

## Limitations

- `not independently reproduced`: Research findings represent third-party empirical results audited from the open-source repository commit `fe031d5151ab00ba2061312ddf58e31964987565`.
- `data gap`: Historical price data is based on daily adjusted close prices from Yahoo Finance; intraday order-book depth, bid-ask quotes, and queue dynamics were not modeled.
- `survivorship bias`: The 60 ETF evaluation universe was selected from funds active in 2024. While ETF closure rates are substantially lower than single-equity bankruptcies, surviving funds carry survivorship bias.
- `underspecified`: Limit order execution models, passive fill queues, and intraday liquidity dynamics remain unmodeled.
- `unproven`: Portability to crypto perpetuals, futures calendar spreads, and intraday frequencies remains unproven.

## Implementation status

- `not-implemented`.

This research record documents an external negative research study and does not modify NautilusTrader, PyBroker, or any internal quantitative system. No live, paper, or testnet trading is authorized.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

This document serves as an empirical falsification reference for statistical arbitrage and cointegration research. Ingestion into Hermes Wiki Brain does not constitute validation or approval for trading.

## Related Wiki records

- `[[quant/sp500-statistical-arbitrage-johansen-ou-ablation-multiple-testing-2026-09-12]]` — Evaluates 4-way OU estimators and Hansen SPA multiple testing on S&P 500 sector ETF pairs.
- `[[quant/crypto-perpetual-pairs-trading-kalman-cointegration-falsification-2026-09-11]]` — Documents Kalman-filter cointegration failure and funding friction drag in crypto perpetual pairs.
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]` — Canonical combinatorial purged cross-validation and leakage prevention standards.

## Sources

1. Shaunak Batra (`shaunak-batra`). *"BasketTradingBO — Statistical arbitrage basket trading system with Bayesian optimization"*. Public GitHub repository, commit `fe031d5151ab00ba2061312ddf58e31964987565`, committed September 12, 2026.
   - Repository: [https://github.com/shaunak-batra/BasketTradingBO](https://github.com/shaunak-batra/BasketTradingBO)
   - Commit Tree: [https://github.com/shaunak-batra/BasketTradingBO/tree/fe031d5151ab00ba2061312ddf58e31964987565](https://github.com/shaunak-batra/BasketTradingBO/tree/fe031d5151ab00ba2061312ddf58e31964987565)
   - Readme & Audit: [`README.md`](https://github.com/shaunak-batra/BasketTradingBO/blob/fe031d5151ab00ba2061312ddf58e31964987565/README.md), [`docs/AUDIT.md`](https://github.com/shaunak-batra/BasketTradingBO/blob/fe031d5151ab00ba2061312ddf58e31964987565/docs/AUDIT.md)
   - Protocols & Data Configs: [`config/config.yaml`](https://github.com/shaunak-batra/BasketTradingBO/blob/fe031d5151ab00ba2061312ddf58e31964987565/config/config.yaml), [`config/config_v3.yaml`](https://github.com/shaunak-batra/BasketTradingBO/blob/fe031d5151ab00ba2061312ddf58e31964987565/config/config_v3.yaml), [`config/universe_v3.yaml`](https://github.com/shaunak-batra/BasketTradingBO/blob/fe031d5151ab00ba2061312ddf58e31964987565/config/universe_v3.yaml)
   - Research Memos & Results: [`docs/RESEARCH_V3.md`](https://github.com/shaunak-batra/BasketTradingBO/blob/fe031d5151ab00ba2061312ddf58e31964987565/docs/RESEARCH_V3.md), [`docs/RESULTS_V3.md`](https://github.com/shaunak-batra/BasketTradingBO/blob/fe031d5151ab00ba2061312ddf58e31964987565/docs/RESULTS_V3.md), [`results/v3_universe/summary.md`](https://github.com/shaunak-batra/BasketTradingBO/blob/fe031d5151ab00ba2061312ddf58e31964987565/results/v3_universe/summary.md)
   - Core Python Modules: [`src/cointegration/engine.py`](https://github.com/shaunak-batra/BasketTradingBO/blob/fe031d5151ab00ba2061312ddf58e31964987565/src/cointegration/engine.py), [`src/cointegration/spread.py`](https://github.com/shaunak-batra/BasketTradingBO/blob/fe031d5151ab00ba2061312ddf58e31964987565/src/cointegration/spread.py), [`src/strategy/signals.py`](https://github.com/shaunak-batra/BasketTradingBO/blob/fe031d5151ab00ba2061312ddf58e31964987565/src/strategy/signals.py), [`src/backtesting/backtester.py`](https://github.com/shaunak-batra/BasketTradingBO/blob/fe031d5151ab00ba2061312ddf58e31964987565/src/backtesting/backtester.py), [`src/backtesting/walk_forward.py`](https://github.com/shaunak-batra/BasketTradingBO/blob/fe031d5151ab00ba2061312ddf58e31964987565/src/backtesting/walk_forward.py)
