---
schema: strategy-research-record-v1
title: "Drift-Regime-Gated Cross-Sectional Value-Reversal Equity Alpha (Unicorn Edge)"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equity-long-short
  - cross-sectional
  - regime-switching
  - value-reversal
  - market-neutral
  - drift-regime
  - survivorship-bias-audit
status: research-only
confidence: medium
source_as_of: 2025-11-16
sources:
  - "Mainak Singha, 'Discovery of a 13-Sharpe OOS Factor: Drift Regimes Unlock Hidden Cross-Sectional Predictability', arXiv:2511.12490v1 [q-fin.TR], November 16, 2025. DOI: 10.48550/arXiv.2511.12490. https://arxiv.org/abs/2511.12490"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Drift-Regime-Gated Cross-Sectional Value-Reversal Equity Alpha (Unicorn Edge)

## Provenance

- **Paper Title:** Discovery of a 13-Sharpe OOS Factor: Drift Regimes Unlock Hidden Cross-Sectional Predictability
- **Author:** Mainak Singha
- **arXiv Identifier:** arXiv:2511.12490v1 [q-fin.TR]
- **Submission Date:** 16 Nov 2025 17:41:40 UTC
- **Canonical DOI:** [https://doi.org/10.48550/arXiv.2511.12490](https://doi.org/10.48550/arXiv.2511.12490)
- **Canonical URL:** [https://arxiv.org/abs/2511.12490](https://arxiv.org/abs/2511.12490)
- **HTML Full Text:** [https://arxiv.org/html/2511.12490v1](https://arxiv.org/html/2511.12490v1)
- **PDF Primary Source:** [https://arxiv.org/pdf/2511.12490v1](https://arxiv.org/pdf/2511.12490v1)
- **Code Repository:** No public repository link is provided in the primary source text. All formulas, parameters, operational schedules, tables (Tables 1–14), and walk-forward evaluations trace directly to the primary paper.
- **Primary Source Inspection:** The full text, Sections 1 through 7, Equations (1) through (5), and Tables 1 through 14 were inspected directly. Every quantitative figure, threshold, parameter, and empirical table reported below originates from explicit locations in this primary source document.

## Economic mechanism

### Source-reported

The author posits that persistent upward drift fundamentally alters market microstructure and investor behavioral cognition in ways that dramatically amplify the efficacy of simple value and short-term reversal signals:
1. **Microstructure Transformation in Drift Regimes:** During drift regimes—defined at the individual stock level as periods when an individual stock exhibits >60% positive daily return days over a trailing 63-day window—consistent upward price movement attracts momentum traders and trend followers. This influx provides incremental liquidity: trading volume increases by +30%, displayed market depth expands by +45%, and effective bid-ask spreads compress by -20% (source Table 12).
2. **Cross-Sectional Relative Value Distortions:** While increased participation enhances directional price discovery along the primary trend, it creates cross-sectional valuation distortions. Different stocks within the drifting cohort appreciate at uneven rates due to retail herding, cognitive anchoring to recent highs, and institutional constraints (e.g. position limits, benchmark tracking-error restrictions). As a consequence, cross-sectional relative-value dispersions widen temporarily.
3. **Cognitive Overreaction and Reversal:** Investor confirmation bias leads market participants to overweight positive news, driving short-term overshooting. This dynamic creates sharp mean-reverting snapbacks over short horizons (10-day contrarian reversal) among relative laggards versus extended winners.
4. **Regime-Gating Interaction Effect:** Unconditionally, the combined BASE signal (0.7 value + 0.3 reversal) yields a mediocre Sharpe ratio of only 1.2. The interaction effect between the stock-specific drift regime filter and the BASE signal accounts for 53% of the total return contribution and increases the out-of-sample Sharpe ratio more than 10-fold to 13.2 (source Table 8).

### Research interpretation

This strategy is a **hybrid/composite cross-sectional equity alpha**: an asset-specific trend-persistence regime gate applied to a convex combination of price-based value and short-term contrarian reversal.

The economic rationale decomposes into two distinct phases:
1. **Opportunity Identification (Regime Gate):** Rather than conditioning on a market-wide macro state (e.g., VIX or SPY trend), the strategy operates on stock-specific drift ($\text{UpFraction}_{i,t} > 0.60$). This isolates stocks with strong institutional net-accumulation or sustained retail buying pressure, where liquidity is deep and short-selling friction is low.
2. **Relative-Value Sorting:** Within this subset of persistently drifting equities, the strategy goes long relatively undervalued, short-term oversold stocks and short relatively overextended, short-term momentum leaders.

**Critical Research Caveats and Skepticism:**
- **Survivorship Bias Acknowledgment:** The author constructs the universe using *current* (as of 2024) constituents of the S&P 500 across the entire 2004–2024 period. The author explicitly concedes that survivorship bias inflates performance metrics by an estimated 20–30%. In practice, backtesting on survivors across 20 years completely ignores delistings, bankruptcies (e.g. 2008 financial crisis insolvencies), and fallen angels, which severely distorts both short-term reversal and value factors.
- **Extreme Reported Sharpe (13.19):** An out-of-sample Sharpe ratio exceeding 13 in liquid large-cap US equities is extraordinarily anomalous. In quantitative finance, such double-digit Sharpe ratios almost universally stem from subtle lookahead leakage, unmodeled auction fill frictions, or survivor conditioning.
- **Asymmetric Universe Contraction:** During broad market crises, only 8% of stocks qualify for the drift regime. Shorting within a tiny pool of resilient, drifting stocks introduces high idiosyncratic short-squeeze risk.

## Signal

### Formation timestamp

- **Observation Schedule (`source-reported`):** Daily frequency. Preliminary signal calculation at 3:30 PM, final generation at 3:45 PM, order creation at 3:50 PM, broker submission at 3:55 PM US Eastern.
- **Execution Timestamp (`source-reported`):** 4:00 PM US Eastern (America/New_York) at Market-On-Close (MOC), with position reconciliation by 4:30 PM.

### Lookback

- **Value Lookback (`source-reported`):** Daily closing price $P_{i,t}$, computing inverse price $1 / P_{i,t}$.
- **Reversal Lookback (`source-reported`):** Trailing 10 trading days: $r_{i, t-10, t} = \frac{P_{i,t} - P_{i,t-10}}{P_{i,t-10}}$.
- **Drift Regime Window (`source-reported`):** Trailing 63 trading days ($W = 63$).
- **Warm-Up Period (`research-proposed`):** Minimum 63 trading days of continuous daily close data for each stock.

### Entry

1. **Base Signal Construction (`source-reported`):**
   - Value component: Compute inverse price $1 / P_{i,t}$ for each stock, then convert cross-sectionally to percentile rank scores between 0 and 1:
     $$\text{value}_{i,t} = \text{PercentileRank}\left(\frac{1}{P_{i,t}}\right) \in [0, 1]$$
   - Reversal component: Compute trailing 10-day return, negate it to establish a contrarian signal, and standardize cross-sectionally to z-scores with mean 0 and unit variance across the universe:
     $$\text{reversal}_{i,t} = \text{zscore}\left(- \frac{P_{i,t} - P_{i,t-10}}{P_{i,t-10}}\right)$$
   - Convex combination:
     $$\text{BASE}_{i,t} = 0.7 \times \text{value}_{i,t} + 0.3 \times \text{reversal}_{i,t}$$
     where heavier weight on value reflects greater signal stability.

2. **Regime Filter Construction (`source-reported`):**
   - For each stock $i$ at time $t$, calculate the fraction of positive daily return days over the trailing 63 trading days:
     $$\text{UpFraction}_{i,t} = \frac{1}{63} \sum_{k=1}^{63} \mathbb{I}[r_{i,t-k} > 0]$$
   - Define the binary drift regime indicator with threshold $\theta = 0.60$:
     $$\text{REGIME}_{i,t} = \mathbb{I}[\text{UpFraction}_{i,t} > 0.60]$$

3. **Unicorn Edge Gated Signal (`source-reported`):**
   $$\text{EDGE}_{i,t} = \text{BASE}_{i,t} \times \text{REGIME}_{i,t}$$
   Only stocks in the drift regime ($\text{REGIME}_{i,t} = 1$) receive non-zero scores. Approximately 35% of stock-days qualify on average across the 20-year sample (varying from 8% during market crashes to 67% during strong bull regimes).

4. **Portfolio Construction and Weighting (`source-reported` / `research-proposed`):**
   - Filter to all active stocks with non-zero $\text{EDGE}_{i,t}$ scores.
   - Standardize these non-zero scores cross-sectionally to z-scores $z_{i,t}$ ensuring zero mean and unit variance (`source-reported`).
   - Separate stocks into a Long bucket ($z_{i,t} > 0$) and a Short bucket ($z_{i,t} < 0$) (`source-reported`).
   - Normalize within each bucket so that long positions sum to $+50\%$ and short positions sum to $-50\%$, enforcing constant gross exposure of 100% and approximately zero net market exposure (`source-reported`).
   - Intra-bucket weighting function (`research-proposed` specification of author's normalized z-score description):
     $$w_{i,t}^{\text{long}} = +0.50 \times \frac{z_{i,t}}{\sum_{j \in \text{Long}} z_{j,t}} \quad \text{for } z_{i,t} > 0$$
     $$w_{i,t}^{\text{short}} = -0.50 \times \frac{|z_{i,t}|}{\sum_{j \in \text{Short}} |z_{j,t}|} \quad \text{for } z_{i,t} < 0$$
   - Minimum candidate threshold (`research-proposed`): If fewer than 4 stocks qualify for the drift regime on day $t$, allocate 100% of capital to cash to avoid unhedged concentration risk.

5. **Risk Scaling Factor (`source-reported`):**
   Portfolio weights are scaled by factor $s^*$, computed over a 5-year training period and held constant across the 1-year test period:
   $$s^* = \min\left(\frac{12\%}{\text{TrainingVol}}, \frac{15\%}{|\text{TrainingMaxDD}|}\right)$$
   satisfying both a 12% annualized volatility cap and a 15% maximum drawdown constraint.

### Exit

- **Daily Rebalancing (`source-reported`):** Rebalance positions daily at 4:00 PM MOC based on the updated target portfolio weights. Stocks dropping below the 60% drift threshold or switching sides are liquidated or re-weighted.
- **Holding Period (`source-reported`):** Median holding period is 8 trading days. Daily portfolio turnover is 42%.
- **Dynamic Kill-Switch (`source-reported`):**
  - Absolute drawdown from peak: If portfolio drawdown exceeds 30%, shut down all positions immediately.
  - Rolling 63-day performance: If trailing 63-day return falls below -10%, terminate strategy.
  - Reset rule: Kill-switches cannot reset within evaluation periods, preventing emotional re-entry attempts. (Source reports 0 activations across all out-of-sample test windows).

### Parameters

| Parameter | Type | Source / Status | Value | Role |
| :--- | :--- | :--- | :--- | :--- |
| Drift Window $W$ | Fixed integer | `source-reported` | 63 trading days | Lookback window for counting positive daily return days |
| Up-Fraction Threshold $\theta$ | Fixed float | `source-reported` | 0.60 (60%) | Minimum fraction of positive days to qualify for drift regime |
| Value Weight $\alpha$ | Fixed float | `source-reported` | 0.70 (70%) | Convex combination weight for value component |
| Reversal Weight $(1 - \alpha)$ | Fixed float | `source-reported` | 0.30 (30%) | Convex combination weight for 10-day reversal component |
| Reversal Window | Fixed integer | `source-reported` | 10 trading days | Lookback for short-term contrarian return |
| Target Volatility Cap | Fixed float | `source-reported` | 12.0% annual | Upper bound in scaling factor $s^*$ calculation |
| Target MaxDD Cap | Fixed float | `source-reported` | 15.0% peak-to-trough | Upper bound in scaling factor $s^*$ calculation |
| Kill-Switch Absolute DD | Fixed float | `source-reported` | 30.0% from peak | Emergency deactivation trigger |
| Kill-Switch Rolling Return | Fixed float | `source-reported` | -10.0% over 63 days | Emergency deactivation trigger |
| Transaction Cost | Fixed float | `source-reported` | 0.6 bps per unit | Explicit + implicit execution cost charged against returns |
| Min Active Stocks Gate | Operational filter | `research-proposed` | 4 stocks | Minimum qualifying drift stocks required to deploy capital |
| Borrow Fee Assumption | Operational cost | `research-proposed` | 25 bps annualized | General collateral borrow rate for short equity positions |

## Required data

- **Instrument:** US Equities (S&P 500 constituents).
- **Universe:**
  - `source-reported`: Current constituents of the S&P 500 index spanning January 2004 through December 2024 (unadjusted for historical index deletions/additions, introducing survivorship bias).
  - `research-proposed`: Historical point-in-time constituent membership of the S&P 500, filtered for active trading status and minimum 30-day average daily volume ($ADV \ge \$10\text{M}$).
- **Venue:** US primary equity exchanges (NYSE, NASDAQ, BATS).
- **Timeframe:** Daily bars (OHLCV) with full corporate action adjustments (splits, cash dividends).
- **Fields:**
  - Daily unadjusted and adjusted close price $P_{i,t}$.
  - Daily return $r_{i,t} = (P_{i,t} / P_{i,t-1}) - 1$.
  - Intraday price snap at 3:45 PM US Eastern for preliminary signal and order sizing.
- **Point-in-Time:** Prices must be finalized prior to 3:45 PM for 3:55 PM order transmission to the closing auction.
- **Timestamp:** US Eastern Time (America/New_York) aligned to UTC (20:00 UTC during standard time, 19:00 UTC during daylight saving time).
- **Missing Data Handling:** If a stock is halted or missing a close price, exclude it from that day's cross-sectional ranking. Zero imputation of returns is strictly forbidden.

## Execution assumptions

- **Order Type (`source-reported`):** Market-On-Close (MOC) auction orders submitted to the primary listing exchange.
- **Fill Model (`source-reported`):** 100% fill rate assumed at the official 4:00 PM closing auction print.
- **Signal-to-Order Timing (`source-reported`):** Preliminary calculation at 3:30 PM, final generation at 3:45 PM, order creation at 3:50 PM, broker submission at 3:55 PM (5-minute buffer before 4:00 PM close).
- **Transaction Costs (`source-reported`):** 0.6 bps per unit traded (incorporating explicit broker commissions and implicit bid-ask spread crossing).
- **Short Borrow and Margin (`research-proposed`):** Margin requirement of 50% for short positions (Reg T), general collateral borrow rate of 25 bps annualized. Short availability assumed 100% for liquid S&P 500 constituents.
- **Gross Leverage / Market Neutrality (`source-reported`):** Constant 100% gross exposure (50% long, 50% short); net exposure approximately 0%.
- **Capacity Analysis (`source-reported`):** Evaluated via square-root market impact model across AUM levels (source Table 11):
  - $50M AUM: Daily volume participation 2%, impact 3 bps, Net Sharpe 12.1, Net Return 145.2% (Viability: Excellent).
  - $100M AUM: Daily volume participation 4%, impact 8 bps, Net Sharpe 10.8, Net Return 129.6% (Viability: Excellent).
  - $250M AUM: Daily volume participation 10%, impact 15 bps, Net Sharpe 8.3, Net Return 99.6% (Viability: Good).
  - $500M AUM: Daily volume participation 20%, impact 28 bps, Net Sharpe 5.9, Net Return 70.8% (Viability: Acceptable).
  - $1B AUM: Daily volume participation 40%, impact 52 bps, Net Sharpe 2.8, Net Return 33.6% (Viability: Marginal).
  - $2B AUM: Daily volume participation 80%, impact 95 bps, Net Sharpe 0.4, Net Return 4.8% (Viability: Unviable).

## Evidence

### Source-reported

All quantitative figures below are directly reported by Mainak Singha (arXiv:2511.12490v1, November 2025) on US equities across three out-of-sample walk-forward test periods (2010–2011, 2015–2016, 2020–2021):

1. **Walk-Forward Out-of-Sample Performance by Window (source Table 1):**
   - **Window 1 (Post-Crisis Recovery, Train 2005–2010, Test 2010–2011):** Training Sharpe 19.42, Scale Factor $s^* = 0.841$, Realized Test Sharpe 16.89, Annualized Return 206.7%, Annualized Volatility 12.2%, Maximum Drawdown -11.9%.
   - **Window 2 (Stable Markets, Train 2010–2015, Test 2015–2016):** Training Sharpe 27.79, Scale Factor $s^* = 1.327$, Realized Test Sharpe 22.87, Annualized Return 207.2%, Annualized Volatility 9.1%, Maximum Drawdown -0.9%.
   - **Window 3 (COVID Disruption, Train 2015–2020, Test 2020–2021):** Training Sharpe 16.63, Scale Factor $s^* = 1.569$, Realized Test Sharpe 5.11, Annualized Return 62.0%, Annualized Volatility 12.2%, Maximum Drawdown -4.0%.

2. **Combined Out-of-Sample Performance vs S&P 500 Equal-Weight Benchmark (source Table 2):**
   - **OOS Sharpe Ratio:** 13.19 (Unicorn Edge) vs 0.99 (S&P 500 EW) — 13.3x outperformance.
   - **Annualized Return:** 158.6% (Unicorn Edge).
   - **Total Cumulative OOS Return (3 test years):** +10,938% (Unicorn Edge) vs +478% (S&P 500 EW) — 22.9x ratio.
   - **Wealth Multiple:** 110.4x (Unicorn Edge) vs 5.78x (S&P 500 EW) — $1M compounds to $110,376,000 vs $5,779,000 (source Table 3).
   - **Maximum Drawdown:** -11.9% (Unicorn Edge) vs -18.7% (S&P 500 EW).
   - **Daily Win Rate:** 67% (Unicorn Edge) vs 54% (S&P 500 EW).
   - **Best Day:** +4.2% (Unicorn Edge) vs +9.1% (S&P 500 EW).
   - **Worst Day:** -3.1% (Unicorn Edge) vs -8.3% (S&P 500 EW).
   - **Daily Return Skewness:** +0.42 (Unicorn Edge) vs -0.31 (S&P 500 EW).
   - **Correlation to Benchmark:** 0.08.
   - **Median Daily Return:** +0.63% (Unicorn Edge) vs +0.11% (S&P 500 EW).

3. **Factor Risk Decomposition (Fama-French-Carhart, source Table 4):**
   - Market beta: 0.02 ($t = 0.41$, $R^2 = 0.1\%$).
   - SMB beta: 0.03 ($t = 0.52$, $R^2 = 0.2\%$).
   - HML beta: 0.12 ($t = 1.83$, $R^2 = 1.8\%$).
   - UMD (momentum) beta: -0.08 ($t = -1.21$, $R^2 = 0.9\%$).
   - Total model $R^2$: 2.9% (virtually zero systematic exposure).

4. **Component Attribution Analysis (source Table 8):**
   - Value alone in drift regime: Sharpe 5.3 (42.3% return, 27% contribution).
   - Reversal alone in drift regime: Sharpe 4.7 (31.1% return, 20% contribution).
   - Interaction effect (Value + Reversal in regime): Sharpe 7.2 (85.2% return, 53% contribution).
   - Combined BASE signal without regime: Sharpe 1.2.
   - Combined Unicorn Edge with regime: Sharpe 13.2 (158.6% annualized return, 100% total).

5. **Macro Regime Breakdown (source Table 9):**
   - Strong Bull (VIX < 15): Frequency 28%, average stocks in regime 51%, Strategy Sharpe 18.3 vs Benchmark 1.42.
   - Normal (15 $\le$ VIX < 25): Frequency 54%, average stocks in regime 38%, Strategy Sharpe 12.1 vs Benchmark 0.93.
   - Stressed (25 $\le$ VIX < 35): Frequency 14%, average stocks in regime 22%, Strategy Sharpe 7.2 vs Benchmark 0.51.
   - Crisis (VIX $\ge$ 35): Frequency 4%, average stocks in regime 8%, Strategy Sharpe 2.1 vs Benchmark -0.83.

6. **Robustness & Stress Testing (source Table 6 & Table 7):**
   - 1,000 random regime filters: Best Sharpe 1.89, Median Sharpe 0.31 ($p < 0.001$).
   - Random stock assignment: Median Sharpe -0.08 ($p < 0.001$).
   - 50 bps daily return Gaussian noise: Realized Sharpe 7.8.
   - Doubled transaction costs (1.2 bps): Realized Sharpe 9.1.
   - 10 bps execution slippage: Realized Sharpe 6.3.
   - Simulated 2008 liquidity crisis shock (displayed depth cut 50–70%, spreads doubled, 10 bps slippage): Realized Sharpe 4.1.

### Independently reproduced

`not independently reproduced.`

### Negative evidence

- **Severe Survivorship Contamination:** The primary source openly restricts its historical universe to current (2024) constituents of the S&P 500 across 2004–2024. Companies that suffered bankruptcies, delistings, or severe structural decline (e.g., Bear Stearns, Lehman Brothers, Enron, WorldCom, Washington Mutual) are systematically excluded from the historical sample. Because the strategy buys short-term losers and low-price stocks within drifting cohorts, survivorship selection artificially eliminates names that experienced catastrophic continuous downward drift or bankruptcy. The author's estimate that survivorship bias accounts for only "20–30%" of performance is almost certainly an underestimate for a reversal-based strategy.
- **Selective Walk-Forward Sample Windows:** Out of 20 historical years (2004–2024), the author presents out-of-sample results for only three non-contiguous single-year windows (2010–2011, 2015–2016, 2020–2021). All three windows represent explosive post-crisis or post-shock recovery rallies characterized by massive momentum continuity. The paper omits out-of-sample results for full drawdown years (e.g. 2008, 2018, 2022).
- **Lookahead Bias in Intraday MOC Execution:** Calculating a 10-day return and 63-day up-fraction at 3:45 PM US Eastern to submit MOC orders at 3:55 PM assumes that the 3:45 PM price is a perfect proxy for the 4:00 PM close print. Closing auction volume often accounts for 10–25% of total daily volume; price divergence between 3:45 PM and 4:00 PM can introduce significant execution slippage not modeled in a 0.6 bps friction fee.

## Falsification plan

To rigorously test and falsify the reported alpha hypothesis in our quantitative research pipeline:

1. **Point-in-Time Survivorship Audit (`research-defined falsification threshold`):**
   - Reconstruct the exact strategy on the true point-in-time S&P 500 constituent history from 2004 to 2024, including all delisted, bankrupt, and merged entities with accurate terminal liquidation returns.
   - **Threshold:** If the annualized out-of-sample Sharpe ratio drops below 2.0, or annualized returns decline by >50%, conclude that the reported Sharpe 13 is an artifact of survivorship bias and reject the strategy.

2. **Continuous Multi-Cycle Walk-Forward Validation (`research-defined falsification threshold`):**
   - Execute an un-gapped rolling walk-forward test (5-year rolling train, 1-year forward test) across every year from 2009 through 2024 (16 contiguous test years).
   - **Threshold:** If the strategy experiences a drawdown exceeding 25%, or if test-period Sharpe ratios in bear/recessionary regimes (e.g. 2008, 2018, 2022) fall below 0.0, falsify the author's claim of crisis immunity.

3. **Execution Delay MOO Sensitivity Test (`research-defined falsification threshold`):**
   - Shift execution from 4:00 PM MOC (same-day close print) to 9:30 AM Market-On-Open (MOO) the following morning, introducing true overnight gap risk and eliminating same-day closing price lookahead.
   - **Threshold:** If the Sharpe ratio decays by more than 40% under next-day MOO execution, falsify the thesis and classify the edge as an artifact of end-of-day pricing latency.

4. **Fee and Borrow Cost Stress Test (`research-defined falsification threshold`):**
   - Apply realistic institutional costs: 2.0 bps exchange taker/auction fee + 50 bps annualized hard-to-borrow financing drag on short positions.
   - **Threshold:** If net Sharpe ratio drops below 1.5, reject strategy as unviable after institutional friction.

## Crypto portability

- **Portability Status:** `adapted/unproven`.
- **Primary Source Scope:** The source investigates US large-cap equities exclusively and provides zero empirical tests in cryptocurrency markets.

### Portability Mechanics & Severe Structural Differences

1. **Inverse Price ($1/P$) as "Value" is Invalid in Crypto:**
   - In US equities, nominal share price has historically been used as a crude proxy for size or retail neglectedness. In crypto, nominal token price is completely arbitrary and economically meaningless due to tokenomics (circulating supply variations, token splits, and supply denominations ranging from billions to tens of thousands).
   - *Required Adaptation (`research-proposed`):* Replace inverse price with a genuine valuation or fundamental relative-value metric, such as Fully Diluted Valuation (FDV) percentile rank, market-cap rank, or token price-to-fees/revenue ratios.
2. **Perpetual Funding Rate Drag:**
   - In crypto perpetual futures, shorting tokens exhibiting strong upward drift ($\text{UpFraction} > 0.60$) carries extreme negative carry risk. Hot, trending altcoins frequently trade at massive positive funding rates (annualized 30% to 100%+ paid by shorts to longs). Shorting the relatively lagging coins in a drifting crypto cohort can lead to severe funding bleed that overwhelms reversal profits.
3. **Absence of Centralized Closing Auctions:**
   - Crypto trades 24/7 without NYSE-style Market-On-Close (MOC) auctions.
   - *Operational Adaptation (`research-proposed`):* Establish a synthetic daily cutoff at 00:00 UTC, using a 15-minute TWAP execution window (23:45–00:00 UTC) across the top 50 perpetual contracts on Binance and Bybit.

## Limitations

- **Survivorship Bias:** Primary source uses 2024 current constituents for 2004–2024 analysis, systematically removing failed companies and inflating reversal performance.
- **Discontinuous Test Sample:** Walk-forward validation reports only 3 selected single-year bull windows, omitting historical bear markets.
- **Intra-Bucket Sizing Underspecification:** The paper states weights are normalized within long/short buckets based on z-scores, but omits the exact closed-form weighting function (`research-proposed` formula supplied above).
- **Execution Latency Risk:** MOC assumption relies on closing auction prints without modeling closing auction imbalance volatility.
- **Extreme Parameter Sensitivity at Lower Thresholds:** While robust to small variations around $\theta = 0.60$, reducing the threshold to 0.42 collapses the Sharpe ratio from 13.2 to 3.2 (source Table 6), indicating high non-linear sensitivity to the drift definition.

## Implementation status

- `not-implemented` in our research stack.
- No prototype, PyBroker test, or NautilusTrader backtest has been performed.
- Captured strictly as normalized research material for Wiki Brain evaluation.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- Presence of this record does not constitute authorization for paper trading, testnet deployment, or live capital allocation.

## Related Wiki records

- `[[quant/forecast-to-fill-gold-futures-friction-adjusted-kelly-alpha-2026-09-02]]` — Prior research by Mainak Singha evaluating friction-adjusted Kelly sizing and capacity in futures.
- `[[quant/two-level-uncertainty-cross-sectional-ranker-regime-trust-gate-tail-cap-2026-09-05]]` — Cross-sectional ranker regime trust gating under market uncertainty.
- `[[quant/cross-sectional-volatility-regime-gated-residual-mixture-of-experts-2026-09-02]]` — Gated cross-sectional regime architectures in equity portfolios.

## Sources

1. Mainak Singha, "Discovery of a 13-Sharpe OOS Factor: Drift Regimes Unlock Hidden Cross-Sectional Predictability", arXiv preprint `arXiv:2511.12490v1 [q-fin.TR]`, submitted November 16, 2025.
   - Stable arXiv URL: [https://arxiv.org/abs/2511.12490](https://arxiv.org/abs/2511.12490)
   - Full-text HTML: [https://arxiv.org/html/2511.12490v1](https://arxiv.org/html/2511.12490v1)
   - PDF Primary Source: [https://arxiv.org/pdf/2511.12490v1](https://arxiv.org/pdf/2511.12490v1)
   - Canonical DOI: [https://doi.org/10.48550/arXiv.2511.12490](https://doi.org/10.48550/arXiv.2511.12490)
