---
schema: strategy-research-record-v1
title: "Event-Driven Mean-Variance Optimization for Multi-Asset Perpetual Funding Rate Arbitrage with Adaptive Volatility Filters"
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - funding-rate
  - delta-neutral
  - arbitrage
  - mean-variance-optimization
  - event-driven
  - binance
status: research-only
confidence: medium
source_as_of: 2025-10-01
sources:
  - "Chakrabandh Rittiplang and Chaiyaporn Khemapatapan, 'Development of an Event-Driven Portfolio Management Algorithm for Funding Rate Arbitrage Strategies to Enhance Sharpe Ratio in Cryptocurrency Markets', Journal of Science and Technology Kasetsart University (JSTKU), Vol. 15, No. 2, pp. 101–112 (Published August 20, 2026). DOI: 10.56825/jstku.2026.1524724. URL: https://doi.org/10.56825/jstku.2026.1524724. PDF: https://ph03.tci-thaijo.org/index.php/JSTKU/article/download/4724/3449"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Event-Driven Mean-Variance Optimization for Multi-Asset Perpetual Funding Rate Arbitrage with Adaptive Volatility Filters

## Provenance

- **Primary source identity:** Chakrabandh Rittiplang and Chaiyaporn Khemapatapan (Department of Computer Engineering, College of Engineering and Technology, Dhurakij Pundit University, Bangkok 10210, Thailand), *"Development of an Event-Driven Portfolio Management Algorithm for Funding Rate Arbitrage Strategies to Enhance Sharpe Ratio in Cryptocurrency Markets"*, *Journal of Science and Technology Kasetsart University* (JSTKU), Vol. 15, No. 2 (May–August 2026), pp. 101–112. Received 2026-03-26, revised 2026-05-19, accepted 2026-05-25, published 2026-08-20.
- **Canonical digital identifiers:** DOI `10.56825/jstku.2026.1524724`; article landing page: `https://ph03.tci-thaijo.org/index.php/JSTKU/article/view/4724`; direct galley PDF bitstream: `https://ph03.tci-thaijo.org/index.php/JSTKU/article/download/4724/3449`.
- **Primary-source verification:** Full-text PDF (12 pages, 44,187 bytes text extraction) downloaded directly and inspected on 2026-09-23. All mathematical formulas (Equations 1–4), optimization constraints, 4-layer event filters, baseline specifications, performance tables (Tables 1–7), statistical significance tests, sensitivity ranges, and author-reported negative findings were extracted directly from the peer-reviewed full text.
- **Repository deduplication audit:** Full ripgrep across all `*.md` files in this repository for `10.56825`, `jstku`, `Rittiplang`, `Khemapatapan`, and exact phrase *"Event-Driven Portfolio Management Algorithm for Funding Rate"* yielded zero hits. Existing repository records covering funding carry (e.g. `crypto-perpetual-funding-rate-carry-spot-perp-2026-08-31.md`, `crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11.md`, `cross-venue-funding-carry-patient-rebalance-vs-active-harvesting-2026-09-12.md`, `crypto-funding-carry-plus-cross-sectional-dispersion-binance-perp-2026-09-17.md`) analyze static cross-venue carry, single-asset cash-and-carry, or pure cross-sectional rank sorts; none investigate event-driven mean-variance optimization with spike-triggered rebalancing and multi-layer volatility gating across a multi-asset basket.

## Economic mechanism

### Source-reported

Perpetual futures contracts utilize periodic funding fee payments (typically settled every 8 hours on centralized venues such as Binance) between long and short contract holders to tether the derivative price to the spot index. Under typical bullish market conditions, long traders pay short traders a positive funding fee. A delta-neutral funding rate arbitrageur maintains simultaneous long spot and short perpetual positions to capture this cash yield while hedging directional price exposure.

The authors highlight two structural limitations in existing funding rate portfolio strategies:
1. **Static Equal-Weighting Vulnerability:** Fixed static allocations (e.g. 1/N equal weighting) cannot respond dynamically when volatility spikes or when specific tokens experience negative funding rates or compressed yield spreads, exposing the basket to unhedged yield drag or idiosyncratic drawdowns.
2. **Machine Learning Predictive Failure:** Common supervised machine learning frameworks (e.g., Ridge regression, XGBoost) attempt to forecast future funding rates. However, funding rate series exhibit strong mean reversion, high noise-to-signal ratios, and market efficiency bounds (where historical features provide negligible out-of-sample predictive power for directional rate changes), causing predictive ML models to underperform static baselines.

The authors propose an **Event-Driven Mean-Variance Optimization (Event-MVO)** architecture. Rather than forecasting future funding rates, the algorithm allocates capital to maximize the portfolio Sharpe ratio using historical rolling covariance and returns, while executing rebalancing only when triggered by specific statistical funding spikes and filtered through a four-layer volatility and turnover gating mechanism.

### Research interpretation

The falsifiable thesis is that cross-sectional variation in perpetual funding yields across diverse cryptocurrency sectors (large-cap, mid-cap, DeFi, PoW, payments) contains structural diversification benefits:
- Rolling covariance structures can dampen portfolio cash-yield variance because funding shocks are not perfectly synchronized across all tokens.
- Restricting reallocation to explicit funding rate dislocation events (spikes $> 60\%$ relative to moving averages) prevents transaction fee drag from eroding the modest per-period cash yield.
- However, the strategy remains a **yield-harvesting cash-and-carry**, not a pure market-neutral anomaly. In prolonged severe bear regimes or market-wide negative funding flip periods, the aggregate basket yield can compress or turn negative. In strong bull regimes where all tokens carry uniformly high positive funding, static buy-and-hold equal weighting can outperform because rebalancing incurs unnecessary turnover costs.

## Signal

The trading logic consists of two coupled subsystems: **Event Detection & Gating** and **Mean-Variance Optimization**.

All specifications below are **source-reported** from Rittiplang & Khemapatapan (2026) unless explicitly labeled `research-proposed`.

### 1. Event Detection & Multi-Layer Filtering (EventHandler)

The algorithm evaluates four decision layers prior to executing any portfolio rebalance:

- **Spike Event Detection (Equation 4):** A potential rebalance event is flagged at any 8-hour funding settlement $t$ if any constituent asset's funding rate deviates by more than 60% from its 21-period moving average:
  $$\text{Spike}_i(t) = 1 \quad \text{if} \quad \frac{|FR_i(t) - MA_{21, i}(t)|}{|MA_{21, i}(t)|} > 0.60$$
  where $MA_{21, i}$ is the 21-period (7-day, given 8h settlement) simple moving average of asset $i$'s funding rate.
- **Layer 1 — Force Rebalance:** If the elapsed duration since the last portfolio rebalance exceeds 45 calendar days, a rebalance is forcibly scheduled regardless of market quietness.
- **Layer 2 — Market Volatility Filter:** If aggregate market funding volatility $\sigma_{\text{market}} < 0.0015$, rebalancing is skipped (the market is deemed too quiescent to justify trading costs).
- **Layer 3 — Adaptive Rebalance Interval:** Rebalancing is constrained by an adaptive minimum cooldown interval conditioned on market volatility:
  - High Volatility ($\sigma > 0.02$): minimum cooldown interval = 96 hours (12 funding periods / 4 days).
  - Medium Volatility: minimum cooldown interval = 144 hours (18 funding periods / 6 days).
  - Low Volatility ($\sigma \le 0.02$): minimum cooldown interval = 216 hours (27 funding periods / 9 days).
- **Layer 4 — Weight Deviation Filter:** The optimization problem produces candidate optimal weights $w^*$. If the total absolute weight turnover $\sum_{i=1}^N |w_i^* - w_i| < 0.07$ (7%), rebalancing is skipped to avoid turnover friction on minor allocations.

### 2. Portfolio Optimization (Equations 1 & 2)

When an event is confirmed and clears Layers 1–4, portfolio weights $w = [w_1, \dots, w_N]^T$ are computed by solving:
$$\max_w S(w) = \frac{w^T \mu}{\sqrt{w^T \Sigma w}}$$
subject to:
$$\sum_{i=1}^N w_i = 1, \quad 0 \le w_i \le 0.40 \quad \forall i$$
- $\mu$: vector of expected funding cash yields per asset, estimated over a rolling lookback window of 90 funding periods (30 days).
- $\Sigma$: covariance matrix of funding cash yields, estimated over the same 90-period lookback window.
- Asset Weight Cap: individual asset weight is strictly capped at $40\%$ ($w_i \le 0.40$) to prevent extreme single-asset concentration risk.
- Solver: Sequential Least Squares Programming (SciPy SLSQP).

### 3. Machine Learning Baseline Implementations (Evaluated by Source)

The paper constructs two ML comparison baselines:
- **Ridge Regression (L2, $\alpha = 1.0$):** Walk-forward validation with 6-month training window and 1-month test window (43 rolling rounds). Features (17 per asset) include moving averages ($MA_7, MA_{14}, MA_{21}$), historical volatilities ($\sigma_7, \sigma_{14}, \sigma_{21}$), trend ($MA_7 - MA_{21}$), and momentum. Predicted return scores $s_i$ are mapped to portfolio weights via Softmax with temperature $T = 1.0$:
  $$w_i = \frac{\exp(s_i / T)}{\sum_j \exp(s_j / T)}$$
  Rebalanced on a fixed monthly schedule.
- **XGBoost Non-linear Ensemble:** $n\_estimators = 100$, $max\_depth = 4$, $learning\_rate = 0.1$, identical 17 features, walk-forward 6:1 validation, Softmax allocation, and monthly rebalancing.

## Required data

- **Universe:** 8 cryptocurrency assets listed on Binance Futures representing distinct market sectors:
  - Large Cap: Bitcoin (BTC), Ethereum (ETH)
  - Payment: Litecoin (LTC)
  - Layer 1 / Smart Contract: Polygon (MATIC), Ethereum Classic (ETC)
  - Decentralized Finance (DeFi) / DEX: Uniswap (UNI), Aave (AAVE), SushiSwap (SUSHI)
- **Market / Venue:** Binance USDT-margined perpetual futures (`Binance Futures REST API`) and Binance spot market.
- **Timeframe:** 8-hour funding intervals (00:00, 08:00, 16:00 UTC), corresponding to 3 intervals per day.
- **Fields:**
  - Realized 8-hour funding rate ($FR$) per contract.
  - Spot price and perpetual contract mark price for delta-neutral rebalancing.
- **Sample Period:** October 2021 to October 2025 (4 years, totaling 35,064 asset-interval data points).
- **Warm-up / Training Boundary:** 6 months initial walk-forward training window, followed by 43 out-of-sample monthly evaluation blocks.
- **Missing Data Handling:** `data gap / not stated in source` regarding API dropouts or missing funding records; historical Binance funding records for these 8 high-liquidity assets are continuous over 2021–2025.

## Execution assumptions

- **Delta-Neutral Structure:** 1x long spot plus 1x short perpetual futures contract per asset.
- **Initial Capital:** 100,000 USDT.
- **Transaction Costs (Source-Reported):** Flat fee of $0.025\%$ (2.5 bps) per traded dollar volume, reflecting Binance VIP/standard taker/maker baseline rates.
- **Execution Timing:** Signals formed at funding rate settlement; portfolio rebalancing executed immediately following funding realization.
- **Execution Modeling Gaps (Source-Reported Limitations):**
  - **Slippage & Market Impact:** `underspecified / omitted in source`. The authors explicitly acknowledge that actual execution slippage, bid-ask spread crossing, and order book depth impact were omitted from the backtest simulation.
  - **Borrow Fees / Margin Financing:** `underspecified in source`. The backtest assumes spot purchases are funded directly from cash equity without borrowing costs; in practical implementations using margin or collateralized loans, borrow interest on spot assets constitutes an additional cash drag.
  - **Liquidation / Margin Rebalancing:** Rebalancing cash between spot and futures margin wallets to prevent perpetual liquidation during sharp market rallies is omitted from the simulation.

## Evidence

### Source-reported

All quantitative performance metrics below are cited directly from Rittiplang & Khemapatapan (2026), Table 2 (Full period performance), Table 3 (Year-by-year summary), Table 4 (Monthly descriptive statistics), Table 5 (Statistical tests), and Table 7 (Sensitivity analysis):

#### 1. Full-Sample Comparative Performance (October 2021 – October 2025, 43 OOS Months)

| Strategy | Annual Return (%) | Sharpe Ratio | Sortino Ratio | Max Drawdown (%) | Calmar Ratio | Total Rebalances |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Static Equal-Weight (1/N)** | 9.66% | 24.90 | 25.10 | 0.86% | 11.19 | 0 |
| **Ridge Regression (ML)** | 9.64% | 24.75 | 25.12 | 0.89% | 10.84 | 43 |
| **XGBoost Ensemble (ML)** | 9.64% | 24.76 | 25.16 | 0.89% | 10.89 | 43 |
| **Event-Driven MVO (Proposed)** | **10.97%** | **30.47** | **26.95** | **0.18%** | **61.51** | **166** |

- **Sharpe Enhancement:** Event-Driven MVO improved the Sharpe ratio from 24.90 to 30.47 (+22.4% relative gain, +5.57 points). Note: The absolute Sharpe ratio magnitude (~25 to 30) reflects the delta-neutral nature of funding rate cash-and-carry strategies, where monthly volatility is exceptionally low ($\sigma_{\text{monthly}} = 0.520\%$).
- **Drawdown Protection:** Maximum drawdown was compressed from 0.86% to 0.18% (a 4.8x reduction).
- **Consistency:** Event-Driven MVO experienced positive returns in 43 out of 43 months (100% positive months), whereas Static, Ridge, and XGBoost each recorded 4 negative months (90.7% positive months).
- **Worst Month:** Minimum monthly return was +0.115% for Event-MVO versus -0.502% for Static Equal-Weight.
- **Monthly Win Rate:** Event-MVO achieved the highest return among the 4 strategies in 27 out of 43 months (62.8%), compared to 7/43 for Static, 5/43 for XGBoost, and 4/43 for Ridge.

#### 2. Regime-by-Regime Breakdown (Table 3)

| Period / Regime | Static Return (%) | Event-MVO Return (%) | Return Diff (%) | Static Sharpe | Event-MVO Sharpe | Sharpe Diff |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Year 1 (Bear Market)** | 4.86% | 8.33% | **+3.47%** | 12.19 | 24.85 | **+12.66** |
| **Year 2 (Recovery)** | 6.40% | 7.17% | **+0.77%** | 36.52 | 37.19 | **+0.67** |
| **Year 3 (Bull Market)** | 14.68% | 13.67% | **-1.01%** | 32.58 | 29.98 | **-2.60** |
| **Year 4 (Mixed Market)** | 8.35% | 8.96% | **+0.61%** | 44.07 | 62.75 | **+18.68** |
| **Average** | 8.57% | 9.53% | **+0.96%** | 31.34 | 38.69 | **+7.35** |

- Event-MVO outperformed Static in 3 out of 4 years (75%).
- Outperformance was largest during Year 1 (Bear Market), where MVO successfully shifted weight away from tokens experiencing negative or collapsing funding yields.
- In Year 3 (Bull Market), Static Equal-Weight outperformed by 1.01% because funding rates across all tokens were uniformly positive, rendering rebalancing turnover friction counterproductive.

#### 3. Statistical Significance Tests (Table 5, $n=43$ months, $m=6$ comparisons)

- **Paired t-test:** $t = 2.483$, raw $p = 0.0171$, Bonferroni-adjusted $p = 0.1027$.
- **Wilcoxon Signed-Rank Test:** $W = 669$, raw $p = 0.0086$, Bonferroni-adjusted $p = 0.0515$.
- **Permutation Test (10,000 iterations):** raw $p = 0.0126$, Bonferroni-adjusted $p = 0.0756$.
- **Monte Carlo Bootstrap (10,000 iterations):** $P(>0) = 99.63\%$, $95\%$ Confidence Interval for mean monthly outperformance $= [0.016\%, 0.125\%]$.
- **Block Bootstrap:** $P(>0) = 92.13\%$ (borderline).
- **Newey-West HAC Test:** $t = 1.588$, raw $p = 0.1198$, Bonferroni-adjusted $p = 0.7187$ (`not statistically significant` under Newey-West serial correlation adjustment).
- **Effect Size:** Cohen's $d = 0.379$ (small effect size).

#### 4. Parameter Sensitivity & Breakeven Fees (Table 7)

- **Spike Threshold (40% to 80%):** Annual return remained bounded between 10.90% and 10.99%, Sharpe between 30.0 and 31.0; outperformed baselines across all settings.
- **Lookback Window (60 to 120 periods):** Annual return between 10.92% and 10.99%, Sharpe between 29.8 and 31.0; outperformed baselines across all settings.
- **Minimum Adaptive Interval (96 to 240 hours):** Stable return 10.97%, Sharpe 30.47; outperformed baselines across all settings.
- **Breakeven Transaction Fee:** 5.4 bps under the Sharpe criterion, and 7.3 bps under the annualized return criterion, providing a >2x safety margin over Binance's baseline fee of 2.5 bps.

### Independently reproduced

`not independently reproduced`.

### Negative evidence

The primary source explicitly documents two substantial negative empirical findings:

1. **Failure of Predictive Machine Learning on Funding Rates:**
   - Both Ridge Regression ($d = -0.15, p = 0.340$) and XGBoost ($d = -0.13, p = 0.403$) generated negligible effect sizes and failed to outperform the naive Static Equal-Weight baseline (annual returns 9.64% vs 9.66%; Sharpe 24.75/24.76 vs 24.90).
   - XGBoost feature importance analysis revealed that the current funding rate (`current_fr`) accounted for approximately 30% of total feature importance, with historical trend, moving average, and momentum features contributing negligible incremental information. The authors conclude that perpetual funding rates behave as noisy, strongly mean-reverting series that cannot be profitably forecasted using standard supervised learning.
2. **Multiple Hypothesis Testing & Serial Correlation Vulnerability:**
   - When adjusting for multiple hypothesis testing across 6 pairwise strategy comparisons ($m=6$), the Bonferroni-adjusted t-test $p$-value rose to $0.1027$, and the Wilcoxon $p$-value rose to $0.0515$, failing conventional $5\%$ significance thresholds.
   - Under Newey-West HAC adjustment, the test statistic was $t = 1.588$ with raw $p = 0.1198$, indicating that monthly outperformance is not statistically significant after accounting for serial autocorrelation.
3. **Bull Market Cost Drag:**
   - In persistent bull regimes (Year 3), Event-MVO underperformed naive buy-and-hold by $-1.01\%$ in annualized return and $-2.60$ in Sharpe ratio due to rebalancing turnover costs when all assets carried positive yields.

## Falsification plan

To falsify the hypothesis that Event-Driven MVO generates genuine economic outperformance over static equal weighting in crypto funding arbitrage:

1. **Cross-Exchange Execution Test:** Replicate the 8-asset basket across OKX, Bybit, and Hyperliquid.
   - *Falsification threshold (`research-defined falsification threshold`):* If Event-MVO fails to generate a statistically significant positive return spread over Static Equal-Weight ($p < 0.05$ under block bootstrap) across at least two independent venues over a minimum 12-month period, falsify venue-invariance.
2. **Realistic Friction Stress Test:** Apply realistic execution slippage (e.g., 2–5 bps per leg for mid-cap tokens like SUSHI, AAVE, ETC) and borrow cost financing (3–8% APR on spot margin).
   - *Falsification threshold (`research-defined falsification threshold`):* If net annualized return falls below 4.0% or net Sharpe falls below 5.0 under 5 bps total round-trip friction, reject the claim that the strategy provides tradable alpha over passive Treasury yields.
3. **Universe Expansion Test:** Expand the universe from 8 hand-selected tokens to the top 30 Binance perpetual contracts by liquidity.
   - *Falsification threshold (`research-defined falsification threshold`):* If the Sharpe advantage (+22.4%) degrades to $< 5\%$ or vanishes across the wider universe, falsify the hypothesis and attribute original performance to survivorship or idiosyncratic selection in the 8-token basket.
4. **Bull-Market Gating Ablation:** Implement an explicit regime filter that suspends rebalancing during verified market-wide high-funding regimes ($\text{FR} > 0.03\%$ per 8h across all assets).
   - *Falsification threshold (`research-defined falsification threshold`):* If an unconstrained static 1/N baseline beats the Event-MVO strategy over a full cycle including bull regimes without this gating overlay, falsify the standalone utility of the 4-layer filter.

## Crypto portability

`direct` — The strategy was formulated, implemented, and tested directly on cryptocurrency perpetual futures and spot data from Binance Futures.

Key cryptocurrency market-structure considerations:
- **Spot vs Perpetual Margin:** True delta-neutral execution requires capital allocation across both spot exchange wallets and perpetual margin accounts. Rapid adverse market moves require collateral rebalancing to prevent perpetual liquidation cascades.
- **Funding Settlement Synchronization:** Binance settles funding every 8 hours, whereas other venues (e.g. dYdX, Hyperliquid) use continuous or 1-hour funding models. The 21-period moving average and 90-period lookbacks must be recalibrated when porting to venues with different settlement intervals (`research-proposed`).
- **Token Delistings & Contract Upgrades:** Mid-cap tokens (e.g. MATIC token migration to POL, or potential delistings of legacy PoW tokens like ETC) present operational contract risks absent from traditional asset carry trades.

## Limitations

- `underspecified / execution gap`: The primary source models a flat 2.5 bps transaction fee but omits actual bid-ask spread crossing, order book slippage, spot margin borrow costs, and wallet rebalancing frictions.
- `small universe`: Limited to 8 pre-selected digital assets on Binance, introducing potential selection bias.
- `multiple testing sensitivity`: Under Bonferroni correction for 6 pairwise tests, parametric significance drops ($p = 0.1027$ for t-test; $p = 0.1198$ for Newey-West HAC), with empirical significance resting primarily on non-parametric Monte Carlo bootstrapping ($P(>0) = 99.63\%$).
- `regime dependency`: The strategy incurs cost drag and underperforms naive equal-weighting during strong bull runs where all funding rates are uniformly elevated.
- `not independently reproduced`: Reported performance metrics reflect author backtests and have not been validated in independent live or paper trading.

## Implementation status

`not-implemented`.

This research record serves solely to capture and normalize external published academic research. No implementation in Qlib, NautilusTrader, Paper, Testnet, or Live execution pipelines has been completed or authorized.

## Adoption boundary

`research-only` / `not-approved`.

The inclusion of this record in the repository does not constitute strategy approval, validation, or endorsement for live capital allocation. Delta-neutral funding carry carries real-world execution risks including exchange counterparty risk, margin liquidation risk during abrupt market gap moves, and variable borrow rates.

## Related Wiki records

- `crypto-perpetual-funding-rate-carry-spot-perp-2026-08-31.md` — Baseline single-asset delta-neutral funding rate carry framework.
- `crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11.md` — Cross-sectional funding carry factor evaluation under net execution costs.
- `cross-venue-funding-carry-patient-rebalance-vs-active-harvesting-2026-09-12.md` — Patient vs active rebalancing dynamics in cross-venue funding harvesting.
- `crypto-funding-carry-plus-cross-sectional-dispersion-binance-perp-2026-09-17.md` — Cross-sectional funding rate dispersion arbitrage on Binance perpetuals.
- `4h-context-funding-alignment-regime-crypto-perpetual-2026-09-06.md` — 4-hour macro context and funding rate alignment regimes.

## Sources

- Chakrabandh Rittiplang and Chaiyaporn Khemapatapan, *"Development of an Event-Driven Portfolio Management Algorithm for Funding Rate Arbitrage Strategies to Enhance Sharpe Ratio in Cryptocurrency Markets"*, *Journal of Science and Technology Kasetsart University* (JSTKU), Vol. 15, No. 2, pp. 101–112 (Published August 20, 2026). DOI: [10.56825/jstku.2026.1524724](https://doi.org/10.56825/jstku.2026.1524724). Stable article URL: `https://ph03.tci-thaijo.org/index.php/JSTKU/article/view/4724`. Galley PDF bitstream: `https://ph03.tci-thaijo.org/index.php/JSTKU/article/download/4724/3449`. Primary text read and verified 2026-09-23.
