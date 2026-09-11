---
schema: strategy-research-record-v1
title: "Trend Atlas: Causal Multi-Speed Log-Price EWMA Trend Following with Hierarchical Cluster Risk Weighting, Volatility Targeting, and Symmetric Buffering on Crypto Perpetuals"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetuals
  - trend-following
  - momentum
  - ewma
  - clustering
  - risk-targeting
  - portfolio-construction
status: research-only
confidence: high
source_as_of: 2026-08-02
sources:
  - "Panatagama (0xpg), 'Trend Atlas: Open Research Workspace for Systematic Trend Following in Crypto Perpetual Futures', GitHub repository 0xpg/crypto-trend-following (commit 4aaa229f5bc9f1b762ba4f6ba5d83c9f5cfef294, 2026)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Trend Atlas: Causal Multi-Speed Log-Price EWMA Trend Following with Hierarchical Cluster Risk Weighting, Volatility Targeting, and Symmetric Buffering on Crypto Perpetuals

## Provenance

- **Author / Research Lab:** Panatagama (`0xpg` / `0xpanatagama`), *Trend Atlas: Open Research Workspace for Systematic Trend Following in Crypto Perpetual Futures*.
- **Public Repository:** `https://github.com/0xpg/crypto-trend-following`.
- **Immutable Commit SHA:** `4aaa229f5bc9f1b762ba4f6ba5d83c9f5cfef294` (Date: 2026-08-02).
- **Inspected Source Files:**
  - Core causal portfolio engine: `engine.py` (866 lines, frozen rule set).
  - CCXT live-data public research workflow: `scripts/ccxt_backtest.py`.
  - Comprehensive baseline, ablation, and sweep runner: `scripts/backtest.py`.
  - Formal claims evaluation suite: `scripts/claims.py`.
  - Synthetic causality, leakage, and accounting tests: `tests/test_engine.py`.
  - Baseline execution results: `results/ccxt_summary.json` and `results/ccxt_daily.csv`.
  - Project specification: `README.md`.
- **Source As-of Date:** August 2, 2026.
- **Deduplication Audit:** Searched all 479 existing markdown records in `alpha-strategy-research`. Zero prior records cite `0xpg`, `panatagama`, `trend-atlas`, or `crypto-trend-following`. The strategy represents a distinct 7-stage causal portfolio architecture integrating multi-speed EWMA crossovers, non-linear saturating response transforms, shrunk correlation clustering, sector risk equalization, dynamic covariance-aware volatility targeting, symmetric no-trade buffering, and absorbing account ruin accounting.

## Economic mechanism

### Source-reported

Trend Atlas investigates whether a multi-market, multi-speed systematic trend-following ensemble can survive realistic execution drag (10 bps trading fees, bid-ask spread, funding rates, and tracking error) across cryptocurrency perpetual futures without overfitting.

The framework organizes the investment process into a rigorous seven-stage causal pipeline:
1. **Universe Eligibility:** Screens contracts at decision time using point-in-time market history ($\ge 120$ days), daily bar completeness ($\ge 20$ hours/day), and rolling 30-day median quote volume ($\ge \$5,000,000$).
2. **Multi-Horizon Trend Signal:** Measures price persistence across multiple horizons using log-price Exponential Weighted Moving Average (EWMA) crossovers with speed pairs $(16, 48)$, $(32, 96)$, and $(64, 192)$ days. Each crossover is standardized by local daily price volatility and scaled by its rolling 365-day standard deviation.
3. **Non-Linear Response & Inverse-Volatility Sizing:** Maps the continuous multi-speed trend z-score through a saturating response function (`tanh`, `overextension`, `linear`, or `binary`) and scales position size inversely with annualized volatility, establishing equal risk per market.
4. **Correlation Shrinkage & Hierarchical Risk Clustering:** Estimates pairwise Pearson correlations with $30\%$ shrinkage toward the cross-sectional mean correlation, projected onto the positive semidefinite cone. Applies hierarchical agglomerative average-linkage clustering on correlation distance $d_{ij} = \sqrt{2(1 - \rho_{ij})}$ into $K = 8$ clusters. Sector weighting equalizes full-signal standalone risk across active clusters to prevent collinear tokens from dominating portfolio risk.
5. **Covariance-Aware Portfolio Volatility Targeting:** Calculates the ex-ante portfolio volatility using the shrunk covariance matrix, scaling the aggregate book dynamically to an annual portfolio volatility target ($20\%$), subject to a hard gross leverage cap of $2.0\times$ equity.
6. **Symmetric No-Trade Buffering:** Enforces a $10\%$ symmetric no-trade buffer band around target positions. Position adjustments occur only when the gap between current and target position exceeds the volatility-scaled threshold, trading only the excess to suppress fee churn.
7. **Causal Accounting & Absorbing Ruin Boundary:** Enforces strict point-in-time execution at the daily open using signals formed at $00:00$ UTC from closes through $t-1$. Accounts for open-to-open P&L, 10 bps transaction costs, funding rates, and an absorbing account ruin state where equity hitting zero stops all subsequent trading.

### Research interpretation

Trend Atlas represents a disciplined institutional adaptation of Commodity Trading Advisor (CTA) trend-following principles to 24/7 digital asset linear derivatives:
1. **Behavioral Persistence vs. Whipsaw:** Crypto markets exhibit pronounced multi-month trending regimes driven by speculative momentum, retail FOMO, and structural capital reallocation cycles. However, high idiosyncratic noise causes single-speed moving averages to suffer severe whipsaws. The 3-speed EWMA ensemble ($(16, 48)$, $(32, 96)$, $(64, 192)$) acts as a low-pass spectral filter, capturing medium-to-long macro trends while dampening intraday noise.
2. **The Crypto Short-Leg Dilemma:** A crucial empirical insight revealed by the source's granular P&L breakdown is the profound asymmetry between long and short performance in crypto: Long PnL generated $+\$230,928.43$ while Short PnL generated $-\$3,078.72$. In crypto perpetuals, structural upward drift, token delisting risks, and explosive short squeezes make symmetric short trend following an empirical performance drain.
3. **Correlation Clusters as True Risk Dimensions:** Due to high market-wide beta, nominally diverse altcoin portfolios often collapse to a single common factor (Bitcoin/market beta). Hierarchical clustering with shrinkage prevents overconcentration in collinear sub-ecosystems (e.g., DeFi tokens, Meme coins, L1 alternatives).
4. **Turnover Suppression via Buffering:** With 10 bps transaction fees and continuous volatility, unbuffered daily rebalancing rapidly erodes gross alpha. The symmetric buffer band removes low-conviction portfolio adjustments, reducing annual turnover to $7.51\times$ and capping annual fee drag at $0.75\%$.

## Signal

The trading signal is evaluated daily at 00:00:00 UTC across $N$ eligible universe contracts using daily candles.

### 1. Volatility Forecasting
Annualized per-symbol volatility is estimated using Carver's blended volatility estimator:
$$\sigma_{\text{short}, i, t} = \text{RollingStd}_{60}(\Delta \ln P_{i})$$
$$\sigma_{\text{long}, i, t} = \text{RollingStd}_{3650}(\Delta \ln P_{i})$$
$$\sigma_{\text{raw}, i, t} = 0.70 \times \sigma_{\text{short}, i, t} + 0.30 \times \sigma_{\text{long}, i, t}$$
$$\sigma_{\text{ann}, i, t} = \max\left(\sigma_{\text{raw}, i, t} \times \sqrt{365}, \sigma_{\text{floor}}\right)$$
where $\sigma_{\text{floor}} = 0.20$ ($20\%$ annual volatility floor). Daily volatility is $\sigma_{\text{daily}, i, t} = \sigma_{\text{ann}, i, t} / \sqrt{365}$.

### 2. Multi-Speed EWMA Crossover
For each speed pair $(f, s) \in \{(16, 48), (32, 96), (64, 192)\}$:
$$\text{Raw}_{i, t}^{(f, s)} = \text{EMA}_f(\ln P_{i, t-1}) - \text{EMA}_s(\ln P_{i, t-1})$$
$$y_{i, t}^{(f, s)} = \frac{\text{Raw}_{i, t}^{(f, s)}}{\sigma_{\text{daily}, i, t-1} \times \sqrt{s}}$$
Each normalized crossover $y_{i, t}^{(f, s)}$ is standardized by its 365-day rolling standard deviation:
$$z_{i, t}^{(f, s)} = \frac{y_{i, t}^{(f, s)}}{\text{RollingStd}_{365}\left(y_{i, t}^{(f, s)}\right)}$$
The master trend signal $z_{i, t}$ is the arithmetic mean across all active speed pairs, clipped to $[-6.0, +6.0]$:
$$z_{i, t} = \text{clip}\left(\frac{1}{3} \sum_{k=1}^3 z_{i, t}^{(k)}, -6.0, +6.0\right)$$
*Causal Lag:* The signal is strictly lagged by 1 day so that row $t$ depends exclusively on closing prices through $t-1$.

### 3. Response Function Transforms
The continuous signal $z_{i, t}$ is mapped into a normalized conviction scalar $R(z_{i, t}) \in [-1.0, +1.0]$ using one of four selectable transforms:
- **Hyperbolic Tangent (`tanh`, Default):**
  $$R(z) = \tanh(z)$$
- **Overextension:** Symmetrical saturating response that reduces exposure when a trend becomes dangerously overextended ($|z| > \sqrt{2}$):
  $$R(z) = \frac{z \cdot \exp\left(-\frac{z^2}{4}\right)}{\sqrt{2} \cdot \exp(-0.5)}$$
- **Linear:** $R(z) = \text{clip}(z, -1.0, 1.0)$.
- **Binary:** $R(z) = \text{sign}(z)$.

### 4. Unscaled Exposure & Cluster Sector Weighting
- Standalone inverse-volatility weight:
  $$u_{i, t} = \frac{R(z_{i, t})}{\max(\sigma_{\text{ann}, i, t-1}, 10^{-9})}$$
- Correlation & Clustering: Every 7 days (`corr_rebuild_days = 7`), a pairwise correlation matrix is computed on the trailing 180-day log return block ($\ge 100$ mutual observations). The empirical correlation matrix is shrunk toward the scalar mean correlation:
  $$\hat{C} = (1 - 0.30) C + 0.30 \bar{C}$$
  Projected to positive-semidefinite cone via eigenvalue floor clipping ($\lambda_i \ge 10^{-10}$).
- Hierarchical average-linkage clustering groups assets into $K = 8$ clusters based on correlation distance $d = \sqrt{2(1 - \rho)}$.
- Sector multiplier $s_{i, t}$ equalizes total standalone risk across active clusters:
  $$s_{i, t} = \frac{1}{\sqrt{w_k^T \Sigma_k w_k}}$$
  normalized such that $\text{mean}(s_{i, t}) = 1.0$.
- Adjusted weight: $u_{i, t}^* = u_{i, t} \times s_{i, t}$.

### 5. Ex-Ante Portfolio Volatility Targeting
The ex-ante portfolio volatility is computed from the portfolio weight vector $u_t^*$ and shrunk covariance matrix $\Sigma_t = \hat{C}_t \odot (\sigma_{\text{ann}, t} \sigma_{\text{ann}, t}^T)$:
$$\sigma_{\text{port}, t} = \sqrt{(u_t^*)^T \Sigma_t u_t^*}$$
The portfolio scaling multiplier is:
$$m_t = \frac{\sigma_{\text{target}}}{\sigma_{\text{port}, t}} \quad \text{where } \sigma_{\text{target}} = 0.20 \text{ (20% annual vol)}$$
Target notional position per asset:
$$\text{Target}_{i, t} = m_t \cdot u_{i, t}^* \cdot \text{Equity}_t$$
Constrained by gross leverage cap:
$$\sum_{i=1}^N |\text{Target}_{i, t}| \le L_{\text{max}} \cdot \text{Equity}_t \quad (L_{\text{max}} = 2.0)$$

### 6. Symmetric No-Trade Buffering
To prevent turnover from minor price fluctuations, a tolerance band is established around the target position:
$$\text{Tol}_{i, t} = \text{buffer} \times m_t \times \text{Equity}_t \times \frac{1}{\sigma_{\text{ann}, i, t-1}} \quad (\text{buffer} = 0.10)$$
Let $\text{Gap}_{i, t} = \text{Target}_{i, t} - \text{Current}_{i, t}$. The executed position adjustment is:
$$\Delta \text{Pos}_{i, t} = \begin{cases} \text{Gap}_{i, t} - \text{sign}(\text{Gap}_{i, t}) \cdot \text{Tol}_{i, t} & \text{if } |\text{Gap}_{i, t}| > \text{Tol}_{i, t} \\ 0.0 & \text{otherwise} \end{cases}$$
$$\text{NewPos}_{i, t} = \text{Current}_{i, t} + \Delta \text{Pos}_{i, t}$$

## Required data

- **Instruments:** Binance USD-M perpetual futures contracts.
- **Universe Filter:** Active listing history $\ge 120$ days, daily bar completeness $\ge 20$ trading hours, and trailing 30-day median quote volume $\ge \$5,000,000$.
- **Demonstration Universe (12 Liquid Contracts):** `BTC/USDT`, `ETH/USDT`, `BNB/USDT`, `SOL/USDT`, `XRP/USDT`, `DOGE/USDT`, `ADA/USDT`, `AVAX/USDT`, `LINK/USDT`, `DOT/USDT`, `LTC/USDT`, `BCH/USDT`.
- **Fields:** Open, High, Low, Close, Volume, Quote Volume, bar duration (`hours`), and 8-hour funding rates.
- **Timeframe:** Daily UTC bars (00:00:00 UTC to 23:59:59 UTC).
- **Point-in-Time Availability:** Closed bars at 23:59:59 UTC are ingested to produce signals usable at 00:00:00 UTC. Execution is modeled at the Open price of day $t$.
- **Missing Data Handling:** Price gaps do not delete the price change; the last complete close is forward-filled as the reference risk mark until complete trading resumes. An incomplete bar ($< 20$ hours) is excluded from volatility calculation.

## Execution assumptions

- **Execution Timing:** Modeled at the opening price of day $t$ (00:00:00 UTC) immediately following signal derivation at $t-1$ close.
- **Order Type & Fill Model:** Market order fill at daily Open.
- **Transaction Costs:** Flat 10.0 basis points ($0.10\%$) applied to all traded notional (`cost_bps = 10.0`), covering exchange taker fee (typically 2–5 bps on VIP tiers) plus estimated bid-ask spread and slippage.
- **Funding Rate Model:** Row $t$ funding is charged to held notional between open of $t$ and open of $t+1$. (In the CCXT baseline demonstration run, funding history is excluded: `funding_included: false`).
- **Initial Capital:** $\$100,000.00$ USD.
- **Hard Ruin Boundary:** If portfolio equity drops to $\le 0.0$, the account is declared ruined (`ruined = True`), all trading terminates, and equity is held flat at $0.0$ forever.
- **Operational Classification:**
  - *Source-reported:* Open-price fills, flat 10 bps fee model, $2.0\times$ gross leverage limit, 12-symbol CCXT universe.
  - `research-proposed`: Execution via 5-minute TWAP window from 00:00:00 UTC to 00:05:00 UTC to minimize market impact on mid-cap altcoins; utilization of post-only maker limit orders targeting 2 bps maker rebate where depth permits.

## Evidence

### Source-reported

All metrics below are directly extracted from the primary source repository (`results/ccxt_summary.json`, `results/ccxt_daily.csv`, and `README.md` at commit `4aaa229f5bc9f1b762ba4f6ba5d83c9f5cfef294`):

#### 1. CCXT Baseline Demonstration Run (2020-01-01 to 2026-08-01, 2,405 Trading Days)
- **Sample Period:** January 1, 2020 through August 1, 2026 (6.59 years, 2,405 calendar days).
- **Universe:** 12 liquid Binance USD-M perpetual contracts (`BTC`, `ETH`, `BNB`, `SOL`, `XRP`, `DOGE`, `ADA`, `AVAX`, `LINK`, `DOT`, `LTC`, `BCH`).
- **Total Net Return:** **+215.93%** (Ending equity: $\$315,930.73$ from $\$100,000.00$ starting capital).
- **Compound Annual Growth Rate (CAGR):** **19.08%**.
- **Net Annualized Sharpe Ratio:** **1.025** (reported as **1.03** in README).
- **Gross Annualized Sharpe Ratio:** **1.066**.
- **Annualized Volatility:** **18.72%** (closely tracking the $20\%$ annual volatility target).
- **Maximum Drawdown:** **-32.53%**.
- **Daily Win Rate (Hit Rate):** **49.77%**.
- **Annualized Portfolio Turnover:** **7.51x**.
- **Annual Cost Drag:** **0.75%** (75 bps annualized return drag from the 10 bps fee model).
- **Average Gross Book Exposure:** **34.88%** of equity.
- **Average Active Positions:** **10.94** contracts held simultaneously.
- **Average Held Ex-Ante Volatility:** **19.83%** (demonstrating exact covariance target tracking against the 20% target).
- **Average Target Tracking Error:** **4.94%** (measuring the tracking deviation introduced by the 10% buffer band).
- **Account Ruin Status:** `ruined: false` (Zero account blowup across the 6.5-year historical backtest).

#### 2. Directional PnL Asymmetry (Source-Reported)
- **Cumulative Long PnL:** **+$230,928.43**
- **Cumulative Short PnL:** **-$3,078.72**
- *Empirical Finding:* Trend following on the short side generated net negative PnL over the 2020–2026 sample. All net profit was generated by the long trend sleeve.

### Independently reproduced

`Not independently reproduced.` The strategy has been captured and validated through direct inspection of the open-source codebase and backtest artifacts; no independent live trading or production verification has been executed in our stack.

### Negative evidence

1. **Short Sleeve Underperformance:** The short trend sleeve produced a cumulative loss of $-\$3,078.72$, acting as a drag on portfolio compounding. Crypto bear markets exhibit violent counter-trend mean-reverting squeezes that trigger repeated stop-outs for standard linear trend followers.
2. **Exclusion of Funding Drag in CCXT Demonstration:** The CCXT demonstration run explicitly omits historical funding rates (`funding_included: false`). During strong bull markets, perpetual funding rates frequently trade at $10\text{--}30\%$ annualized premiums paid by long holders to short holders. For a strategy whose profits are 100% long-driven, funding payments will materially reduce net CAGR.
3. **Survivor Bias in Fixed Asset Universe:** The 12 selected assets (BTC, ETH, SOL, BNB, etc.) represent the largest, most successful survivors of the 2020–2026 cycle. Backtesting a fixed survivor universe overstates trend persistence relative to a point-in-time universe containing failed or delisted tokens (e.g., LUNA, FTT).
4. **Drawdown Duration:** Maximum drawdown reached $-32.53\%$, demonstrating that a $20\%$ volatility target can experience multi-month underwater periods during choppy, directionless market regimes (e.g., 2022 sideways phases).

## Falsification plan

The following operational falsification tests define empirical criteria under which the Trend Atlas hypothesis would be disconfirmed:

1. **Full-Universe Archive Audit with Delistings:**
   - *Test:* Run the complete archive workflow (`scripts/build_panel.py` and `scripts/backtest.py`) on the uncurated Binance historical perpetual universe (300+ contracts), enforcing point-in-time listing entry and delisting liquidations.
   - `research-defined falsification threshold`: If the Net Sharpe ratio drops below $0.50$ or maximum drawdown exceeds $45.0\%$ when accounting for delisted assets and survival churn, the claim that multi-speed trend following generalizes across the crypto cross-section is falsified.
2. **Net-of-Funding Drag Verification:**
   - *Test:* Ingest the full historical 8-hour funding rate panel from Binance (`scripts/fetch_funding.py`) and simulate the baseline with `apply_funding = True`.
   - `research-defined falsification threshold`: If funding rate drag reduces Net Sharpe below $0.65$ or consumes more than $40\%$ of cumulative net profits, the strategy's edge is falsified as insufficient to overcome perpetual carry costs.
3. **Ablation of the Short Sleeve:**
   - *Test:* Run a long-only variant (`max_short_frac_gross = 0.0` or zeroing negative signals) against the bidirectional baseline.
   - `research-defined falsification threshold`: If the bidirectional long-short model fails to achieve a higher Sharpe ratio or lower maximum drawdown than the long-only model, the theoretical justification for maintaining short trend positions in crypto perpetuals is falsified.
4. **Execution Fee & Slippage Stress Test:**
   - *Test:* Perturb transaction costs from 10 bps up to 25 bps (simulating stressed liquidity, market impact, and taker execution during liquidation cascades).
   - `research-defined falsification threshold`: If Net Sharpe decays below $0.40$ at 20 bps round-turn cost, the strategy is deemed unviable for production execution due to cost fragility.

## Crypto portability

- **Portability Assessment:** `direct`.
- **Rationale:** The Trend Atlas architecture was developed natively for and demonstrated on cryptocurrency perpetual futures (Binance USD-M perpetuals).
- **Crypto-Specific Market Dynamics:**
  - *24/7 Continuous Session:* Eliminates weekend and overnight gaps common in traditional futures, but requires an explicit UTC day-boundary convention (00:00:00 UTC) for bar aggregation and signal calculation.
  - *Perpetual Funding Rate Mechanism:* Unlike traditional futures where basis convergence occurs at quarterly expiry, perpetuals anchor to spot via 8-hour funding payments. A trend strategy holding persistent long positions in bull markets pays continuous funding interest to short counterparties.
  - *Skewness & Extreme Volatility:* Altcoin distributions display heavy right tails during speculative rallies and catastrophic left tails during liquidations. The `overextension` response function and $20\%$ volatility floor are specifically tailored to mitigate crypto tail risks.
  - *Contract Specifications & Delistings:* Low-liquidity altcoins face sudden margin requirement hikes or abrupt contract delistings, necessitating strict point-in-time tradeability filters.

## Limitations

- **Fixed Demonstration Universe:** The primary CCXT tearsheet is evaluated on 12 established survivor tokens, introducing selection bias.
- **Funding Rate Omission in Benchmark:** Historical funding payments were omitted in the demonstration tearsheet, overstating net returns for long-biased regimes.
- **Daily Bar Granularity:** Evaluating signals on daily bars cannot capture intraday liquidation cascades or intra-bar margin breaches.
- **Simplified Fee Model:** A constant 10 bps fee assumption fails to capture non-linear market impact for large capital allocations in thin altcoin order books.
- **Short-Leg Negative Expectancy:** The source data confirms that short trend positions produced negative cumulative returns ($-\$3,078.72$), highlighting a major structural weakness in symmetric crypto trend models.

## Implementation status

`not-implemented`.
No implementation in PyBroker, NautilusTrader, or live execution stack has been performed. This capture serves exclusively as normalized upstream research material.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

This record is an upstream research capture. It does not constitute investment advice, quantitative validation, or authorization for live or paper trading execution.

## Related Wiki records

- `[[crypto-adaptive-trend-following-asymmetric-portfolio-2026-09-01]]`
- `[[futures-quad-trend-carry-skew-vov-composite-2026-09-11]]`
- `[[crypto-perpetual-funding-rate-carry-spot-perp-2026-08-31]]`
- `[[crypto-dynamic-time-series-momentum-volatility-impulse-2026-08-31]]`
- `[[crypto-cross-sectional-elastic-net-ctrend-2026-08-31]]`

## Sources

- **Primary Repository:** Panatagama (`0xpg` / `0xpanatagama`), *Trend Atlas: Open Research Workspace for Systematic Trend Following in Crypto Perpetual Futures*, GitHub repository: `https://github.com/0xpg/crypto-trend-following`.
- **Immutable Commit:** `4aaa229f5bc9f1b762ba4f6ba5d83c9f5cfef294` (August 2, 2026).
- **Core Architecture & Pure Functions:** `engine.py` (lines 30–116 for `Config`, 127–152 for `volatility_forecast`, 228–260 for `trend_signal`, 266–276 for `response`, 282–325 for `shrunk_correlation`, 327–336 for `cluster_labels`, 338–367 for `sector_weights`, 476–722 for `simulate`).
- **Empirical Summary Statistics:** `results/ccxt_summary.json` (Total return 2.1593, CAGR 0.1908, Net Sharpe 1.025, Gross Sharpe 1.066, Max DD -0.3253, Turnover 7.51x, Long PnL $230,928.43, Short PnL -$3,078.72).
- **Daily Time Series:** `results/ccxt_daily.csv` (2,405 rows spanning 2020-01-01 to 2026-08-01).
- **Unit Testing Suite:** `tests/test_engine.py` (synthetic causality, input tampering, delisting, and accounting verification).
