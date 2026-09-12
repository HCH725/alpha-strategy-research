---
schema: strategy-research-record-v1
title: "Crypto Statistical Arbitrage: Multiple-Testing Cointegration Tiering, Drifting-Hedge Turnover Accounting, and Cross-Sectional Reversal Cost Falsification"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - pairs-trading
  - cointegration
  - multiple-testing
  - fdr-benjamini-hochberg
  - bonferroni-tiering
  - hedge-ratio-drift
  - leg-level-turnover
  - reversal-falsification
  - crypto-spot
  - binance
status: research-only
confidence: medium
source_as_of: 2026-09-11
sources:
  - "https://github.com/NandaDynasty/CryptoStatArb/tree/2278f61e7b6c1811f13bbbc298e5fd68c80015d0"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Statistical Arbitrage: Multiple-Testing Cointegration Tiering, Drifting-Hedge Turnover Accounting, and Cross-Sectional Reversal Cost Falsification

## Provenance

- **Author:** Kavya Nanda (`NandaDynasty`, GitHub: `https://github.com/NandaDynasty`)
- **Repository URL:** https://github.com/NandaDynasty/CryptoStatArb
- **Full Immutable Commit SHA:** `2278f61e7b6c1811f13bbbc298e5fd68c80015d0`
- **Canonical Tree URL:** https://github.com/NandaDynasty/CryptoStatArb/tree/2278f61e7b6c1811f13bbbc298e5fd68c80015d0
- **Commit Date:** 2026-09-11T10:44:25Z
- **Primary Source Files Examined:**
  - `README.md` (project methodology, headline out-of-sample performance, multiple-testing structure, and methodological error post-mortems) (`source-reported`).
  - `Crypto_StatArb.ipynb` (executable Jupyter notebook containing raw Binance API pulls across 406 crypto spot assets, multi-horizon cross-sectional reversal backtests with volume conditioning, Engle-Granger cointegration screening across 310 eligible candidate pairs, multiple testing via Bonferroni and Benjamini-Hochberg FDR, 90-day rolling OLS spread formation, pair-level vs. leg-level turnover modeling, and out-of-sample performance evaluation) (`source-reported`).
- **Primary Source Verification:** Directly inspected all 70 notebook cells and their executed outputs. Every empirical metric, cointegration p-value threshold, pair identifier, turnover quantity, Sharpe ratio, drawdown figure, and regression parameter traces directly to executed code and printed cell outputs in `Crypto_StatArb.ipynb` (commit `2278f61e7b6c1811f13bbbc298e5fd68c80015d0`).
- **Repository Deduplication:** Audited all 535 existing `.md` records in `alpha-strategy-research`. Zero prior records cite `NandaDynasty/CryptoStatArb`, Kavya Nanda, or this commit. Adjacent crypto pairs trading captures (`crypto-pairs-trading-cointegration-overfitting-falsification-2026-09-13.md` based on `rfukuda06/crypto-pairs-bot`, `crypto-perpetual-pairs-trading-cointegration-hurst-halflife-walkforward-2026-09-12.md` based on `etoh0305`, and `crypto-perpetual-pairs-trading-kalman-cointegration-falsification-2026-09-11.md` based on `djienne`) evaluate small 11-asset single-pair overfits, hourly perpetual futures with funding rates, or synthetic OU injection. Nanda's research provides an independent, broad-universe (406 assets) empirical study delivering two distinct contributions: (1) an empirical falsification proving that cross-sectional crypto reversal cannot survive realistic transaction costs (even under volume-conditioning filters); and (2) a multi-pair statistical arbitrage strategy demonstrating that controlling for multiple testing (Bonferroni / Benjamini-Hochberg) and correctly modeling leg-level turnover from rolling hedge-ratio drift isolates persistent market-neutral out-of-sample edge (Sharpe 0.576 / 0.58, correlation with BTC 0.014).

## Economic mechanism

### Source-reported

In cryptocurrency markets, retail attention and speculative trading create two distinct short-horizon pricing behaviors:
1. **Cross-Sectional Reversal Over-Optimism:** Liquid altcoins exhibit strong short-horizon mean reversion, where coins with extreme relative performance over 1h to 24h horizons tend to reverse direction (up to ~85% directional sign agreement across assets). Conditioning on low trading volume separates liquidity-driven noise moves from fundamental information breakouts. However, the author empirically demonstrates that this apparent alpha is entirely an illusion: high rebalancing turnover ($\sim 1.45$ per period) consumes all gross profits, causing severe cumulative losses under a standard 20 bps transaction fee ($0.0020$).
2. **Cointegration and Long-Run Equilibrium in Clustered Crypto Assets:** Pairs of tokens sharing common functional ecosystems, governance overlap, or technological infrastructure (e.g., decentralized storage tokens like `FIL/ICP`, DeFi protocols like `AAVE/COMP`, or cross-chain infrastructure like `ONT/STEEM` and `MOVR/ZEN`) share stochastic trends driven by aggregate crypto liquidity. Divergences in their log-price ratio represent temporary liquidity imbalances or retail order flow shocks that revert toward long-run equilibrium.
3. **The Multi-Testing and Drift-Turnover Pitfalls:**
   - Unadjusted cointegration screening across $C(N, 2)$ pairs produces extensive data snooping: 42 of 310 tested pairs show naive significance ($p < 0.05$), but only 8 survive Benjamini-Hochberg False Discovery Rate control ($q < 0.05$), and only 4 survive Bonferroni family-wise error control ($p < 0.05 / 310$).
   - In time-varying cointegration models, the hedge ratio $\beta_t$ drifts daily. A backtester that accounts for turnover only when pairs change states understates execution costs by half. Continuous leg rebalancing on the hedge leg doubles turnover from $0.0032$ to $0.0065$ per day, reducing net Sharpe from $0.622$ to $0.576$.

### Research interpretation

The economic validity of cryptocurrency statistical arbitrage depends on distinguishing genuine cointegrating vectors from spurious in-sample co-movement:
- **Spurious Cointegration Risk:** In crypto spot markets, nearly all altcoins exhibit high positive co-movement driven by shared exposure to Bitcoin's macroeconomic liquidity cycle. Naive Engle-Granger tests frequently reject the non-stationary residual null simply because both series underwent simultaneous bull or bear trends. Enforcing strict Benjamini-Hochberg ($q < 0.05$) and Bonferroni ($p < 0.000161$) criteria effectively filters out shared-beta artifacts, retaining pairs with tight structural linkage.
- **Microstructural Mechanics of Hedge Drift Friction:** For a spread $S_t = \log P_{A,t} - \beta_t \log P_{B,t} - \alpha_t$, maintaining dollar neutrality requires holding notional $-\text{Pos}_{t-1} \cdot w_t$ in asset A and $\text{Pos}_{t-1} \cdot \beta_{t-1} \cdot w_t$ in asset B. Because $\beta_t$ updates continuously via a rolling 90-day regression window, asset B's target notional changes every day even if the strategy holds a constant position. Failing to account for leg-level turnover creates an upward bias in reported net Sharpe.
- **Component Roles in the Strategy Architecture:**
  - **Universe / Liquidity Filter:** 406 Binance USDT spot pairs, excluding stablecoins, wrapped tokens, and tokenized equities (`source-reported`).
  - **Pair Selection Filter:** In-sample daily return correlation $> 0.70$ and minimum 90 overlapping daily observations (`source-reported`).
  - **Statistical Significance Filter:** Engle-Granger cointegration on log prices classified into three confidence tiers: Bonferroni ($p < 0.05/310$), Benjamini-Hochberg ($q < 0.05$), and Naive ($p < 0.05$) (`source-reported`).
  - **Spread Estimator:** 90-day rolling OLS on log prices with 1-day lagged mean and variance to construct the spread z-score (`source-reported`).
  - **Hysteresis Entry/Exit Logic:** Conservative extreme entry ($|z| > 6.0$), mean-reversion exit ($|z| < 2.5$), and tail stop-loss ($|z| > 9.0$) (`source-reported`).
  - **Portfolio Sizing Gate:** Tiered confidence weighting (Bonferroni: 3x, BH-only: 2x, Naive: 1x) with 1-day execution lag (`source-reported`).
  - **Execution Fill Model:** Next-day daily bar execution at 00:00 UTC with full leg-level rebalancing costs (`research-proposed`).

## Signal

### Formation Timestamp

- Observation cadence: 24-hour daily bars aggregated from Binance spot tick data at 00:00 UTC (`source-reported`).
- Execution timestamp: Orders are executed on the close/open of the succeeding bar (`shift(1)`) (`source-reported`), avoiding lookahead leakage.
- Timezone convention: UTC (`source-reported`).

### Lookback Windows

- In-Sample Selection Period: Inception through `2023-06-01` (`source-reported`).
- Out-of-Sample Evaluation Period: `2023-06-01` through `2026-04-18` (`source-reported`).
- Minimum in-sample overlapping history: 90 daily bars (`min_in_sample_obs = 90`) (`source-reported`).
- Rolling OLS parameter window: 90 daily bars (`rolling_window = 90`) (`source-reported`).
- Spread mean and standard deviation window: 90 daily bars (`rolling_window = 90`) (`source-reported`).

### Exact Mathematical Definitions

1. **Log-Price Conversion:**
   $$p_{A, t} = \ln(P_{A, t}^{\text{close}}), \quad p_{B, t} = \ln(P_{B, t}^{\text{close}}) \quad (\text{source-reported})$$

2. **Rolling 90-Day OLS Hedge Ratio and Intercept:**
   $$\beta_t = \frac{\widehat{\text{Cov}}_{90}(p_{A, t}, p_{B, t})}{\widehat{\text{Var}}_{90}(p_{B, t})} \quad (\text{source-reported})$$
   $$\alpha_t = \widehat{\mathbb{E}}_{90}[p_{A, t}] - \beta_t \widehat{\mathbb{E}}_{90}[p_{B, t}] \quad (\text{source-reported})$$

3. **Time-Varying Spread:**
   $$S_t = p_{A, t} - \left(\beta_t p_{B, t} + \alpha_t\right) \quad (\text{source-reported})$$

4. **Causal Rolling Spread Normalization (1-Day Shifted Moments):**
   $$\mu_{S, t} = \frac{1}{90} \sum_{k=1}^{90} S_{t-k} \quad (\text{source-reported})$$
   $$\sigma_{S, t} = \sqrt{\frac{1}{89} \sum_{k=1}^{90} (S_{t-k} - \mu_{S, t})^2} \quad (\text{source-reported})$$
   $$z_t = \frac{S_t - \mu_{S, t}}{\sigma_{S, t}} \quad (\text{source-reported})$$

5. **Signal State Machine:**
   $$\text{Pos}_t = \begin{cases}
   0 & \text{if } |z_t| > z_{\text{stop}} \text{ and } \text{Pos}_{t-1} \neq 0 \quad (\text{stop-loss}) \\
   0 & \text{if } |z_t| < z_{\text{exit}} \text{ and } \text{Pos}_{t-1} \neq 0 \quad (\text{mean-reversion exit}) \\
   +1 & \text{if } z_t > z_{\text{entry}} \lor (\text{Pos}_{t-1} = +1 \land z_t > z_{\text{exit}}) \quad (\text{short spread: short A, long B}) \\
   -1 & \text{if } z_t < -z_{\text{entry}} \lor (\text{Pos}_{t-1} = -1 \land z_t < -z_{\text{exit}}) \quad (\text{long spread: long A, short B}) \\
   0 & \text{otherwise}
   \end{cases} \quad (\text{source-reported})$$
   where $z_{\text{entry}} = 6.0$, $z_{\text{exit}} = 2.5$, and $z_{\text{stop}} = 9.0$ (`source-reported`).

6. **Unweighted Pair Return Realization:**
   $$r_{A, t} = \ln(P_{A, t}^{\text{close}}) - \ln(P_{A, t-1}^{\text{close}}), \quad r_{B, t} = \ln(P_{B, t}^{\text{close}}) - \ln(P_{B, t-1}^{\text{close}}) \quad (\text{source-reported})$$
   $$R_{\text{pair}, t} = \text{Pos}_{t-1} \cdot \left(\beta_{t-1} r_{B, t} - r_{A, t}\right) \quad (\text{source-reported})$$

7. **Multiple-Testing Significance Tiers & Portfolio Weighting:**
   - Candidate pairs are partitioned into three mutually exclusive sets:
     - Bonferroni pairs: $\mathcal{P}_{\text{bonf}} = \{(A, B) \mid p_{A, B} < 0.05 / 310\}$ ($N_{\text{bonf}} = 4$) (`source-reported`).
     - Benjamini-Hochberg-only pairs: $\mathcal{P}_{\text{bh}} = \{(A, B) \mid q_{A, B} < 0.05 \land (A, B) \notin \mathcal{P}_{\text{bonf}}\}$ ($N_{\text{bh}} = 4$) (`source-reported`).
     - Regular naive pairs: $\mathcal{P}_{\text{reg}} = \{(A, B) \mid p_{A, B} < 0.05 \land (A, B) \notin \mathcal{P}_{\text{bonf}} \cup \mathcal{P}_{\text{bh}}\}$ ($N_{\text{reg}} = 34$) (`source-reported`).
   - Normalization scalar:
     $$x = \frac{1}{3 N_{\text{bonf}} + 2 N_{\text{bh}} + N_{\text{reg}}} = \frac{1}{3(4) + 2(4) + 34} = \frac{1}{54} \approx 0.018519 \quad (\text{source-reported})$$
   - Target pair weights:
     $$w_{\text{bonf}} = 3x = \frac{3}{54} \approx 0.05556, \quad w_{\text{bh}} = 2x = \frac{2}{54} \approx 0.03704, \quad w_{\text{reg}} = x = \frac{1}{54} \approx 0.01852 \quad (\text{source-reported})$$
   - Active pair weight on date $t$:
     $$w_{p, t} = \begin{cases}
     w_p & \text{if } \text{Pos}_{p, t-1} \neq 0 \\
     0 & \text{otherwise}
     \end{cases} \quad (\text{source-reported})$$

8. **Leg-Level Turnover and Transaction Cost Accounting:**
   - Underlying leg notionals per pair:
     $$\text{Notional}_{A, p, t} = -\text{Pos}_{p, t-1} \cdot w_{p, t} \quad (\text{source-reported})$$
     $$\text{Notional}_{B, p, t} = \text{Pos}_{p, t-1} \cdot \beta_{p, t-1} \cdot w_{p, t} \quad (\text{source-reported})$$
   - Aggregate daily turnover across all pairs:
     $$\text{Turnover}_t = \sum_p |\text{Notional}_{A, p, t} - \text{Notional}_{A, p, t-1}| + \sum_p |\text{Notional}_{B, p, t} - \text{Notional}_{B, p, t-1}| \quad (\text{source-reported})$$
   - Net daily portfolio return:
     $$R_{\text{net}, t} = \sum_p w_{p, t} R_{\text{pair}, p, t} - c_{\text{rate}} \cdot \text{Turnover}_t \quad (\text{source-reported})$$
     where $c_{\text{rate}} = 0.0020$ (20 bps per unit turnover) (`source-reported`).

## Required data

- **Universe:** 406 Binance cryptocurrency USDT spot trading pairs (`source-reported`).
- **Data Vendor / Source:** Binance Public REST API via `python-binance` library (`source-reported`).
- **Excluded Instruments:** Stablecoins (e.g. USDC, BUSD, TUSD), wrapped/staked tokens (e.g. WBTC, WETH, STETH), and tokenized equity instruments (`source-reported`).
- **Granularity / Timeframe:** 24-hour daily aggregated bars (`timeframe = '24h'`) aggregated from raw tick/hourly prints using standard OHLCV resampling (`source-reported`).
- **Fields Required:** `close` prices (for log transformation), `open` prices (for multi-horizon reversal benchmarks), `volume` and `quote_asset_volume` (for reversal volume-conditioning filters) (`source-reported`).
- **Point-in-Time & Temporal Alignment:** Daily bars close at 00:00 UTC. In-sample cointegration testing strictly spans inception to `2023-06-01`; out-of-sample holdout begins at `2023-06-01` and evaluates through `2026-04-18` (`source-reported`).
- **Missing Data Handling:** Drops missing values during pairwise inner concatenation (`pd.concat([log_A, log_B], axis=1).dropna()`). Pairs with fewer than 90 overlapping bars are discarded (`source-reported`).
- **Financing / Borrow Data:** Unmodeled in the primary source (`source-reported`). Margin borrow interest for shorting spot assets is omitted from the backtest engine (`research-proposed`).

## Execution assumptions

- **Execution Timing:** Signals generated at bar close $T-1$ are executed at bar $T$ open (`shift(1)`) (`source-reported`).
- **Fill Model:** Immediate full fill at the printed close price of each daily bar without market impact or queue latency (`source-reported`).
- **Transaction Costs:** Flat 20 bps ($0.0020$) fee per unit of turnover (`source-reported`).
- **Turnover Modeling:**
  - *Naive Pair-Level Model:* Computes turnover solely when pair weights change ($\sum |\Delta w_{p, t}|$), ignoring intra-trade hedge adjustments. Reported average daily turnover: $0.0032$ (`source-reported`).
  - *Leg-Level Drift Model (Author's V2 Correction):* Explicitly tracks leg A and leg B notionals ($|\Delta \text{Notional}_{A}| + |\Delta \text{Notional}_{B}|$), capturing continuous daily rebalancing due to rolling $\beta_t$ drift. Reported average daily turnover: $0.0065$ (`source-reported`).
- **Borrow / Shorting Availability:** Strategy assumes unconstrained spot shorting capability on Binance with zero borrow fees and zero borrow availability limits (`source-reported`). In live trading, shorting spot crypto requires Binance Margin with variable borrow interest rates ($5\%\text{--}15\%$ APR) and collateral limits (`research-proposed`).
- **Capacity / Impact:** Unmodeled. Assumes infinite liquidity at daily close prices (`source-reported`). Estimated capacity limit of $\$2\text{M}\text{--}\$5\text{M}$ AUM across altcoin pairs before market impact degrades edge (`research-proposed`).

## Evidence

### Source-reported

All empirical results below are directly reported from executed cells in `Crypto_StatArb.ipynb` and `README.md` (commit `2278f61e7b6c1811f13bbbc298e5fd68c80015d0`):

#### 1. Cross-Sectional Reversal Falsification (Cells 8–30)

Across 406 assets evaluated from 1h to 24h horizons:
- Raw directional sign agreement reaches up to ~85% on short horizons (`source-reported`).
- Positive ratio and turnover per period:
  - 4h horizon: positive return ratio = $0.4191$, average turnover = $1.4629$, cumulative log return net of 20 bps cost = **$-28.01$** (`source-reported`).
  - 12h horizon: positive return ratio = $0.4420$, average turnover = $1.4560$, cumulative log return net of 20 bps cost = **$-14.16$** (`source-reported`).
  - 24h horizon: positive return ratio = $0.4833$, average turnover = $1.4496$, cumulative log return net of 20 bps cost = **$-4.32$** (`source-reported`).
- Volume-Conditioned Reversal (12h, filtering for moves below volume z-score threshold):
  - Positive return ratio = $0.4083$, average turnover = $1.4570$, cumulative log return net of 20 bps cost = **$-11.35$** (`source-reported`).
  - *Conclusion:* Turnover completely destroys short-horizon crypto reversal alpha under realistic trading fees (`source-reported`).

#### 2. Cointegration Screening & Multiple-Testing Correction (Cells 49–51)

- Initial correlation pre-screen ($r > 0.70$ on daily log returns in-sample): 419 candidate pairs (`source-reported`).
- Pairs meeting minimum 90-day overlapping observation requirement: 310 pairs tested (`source-reported`).
- Significance breakdown:
  - Naive uncorrected ($p < 0.05$): **42 pairs** (`source-reported`).
  - Bonferroni corrected ($p < 0.05 / 310 \approx 0.000161$): **4 pairs** (`ONTUSDT/STEEMUSDT`, `ENJUSDT/STEEMUSDT`, `FILUSDT/ICPUSDT`, `BTTCUSDT/CVCUSDT`) (`source-reported`).
  - Benjamini-Hochberg FDR corrected ($q < 0.05$): **8 pairs** (the 4 Bonferroni pairs plus `SOLUSDT/RAYUSDT`, `AAVEUSDT/COMPUSDT`, `MOVRUSDT/ALICEUSDT`, `MOVRUSDT/ZENUSDT`) (`source-reported`).

#### 3. Out-of-Sample Pairs Trading Performance (2023-06-01 to 2026-04-18, Cells 63–69)

| Metric | Pair-Level Turnover Model (V1) | Leg-Level Drift Model (V2, Corrected) |
| :--- | :--- | :--- |
| **Out-of-Sample Sharpe Ratio (Net)** | 0.622 | **0.576** (reported as 0.58 in README) |
| **Average Daily Turnover** | 0.0032 | **0.0065** |
| **Annualized Return (Net, Log)** | 0.033 (3.3%) | 0.033 (3.3%) |
| **Annualized Volatility** | 0.053 (5.3%) | 0.053 (5.3%) |
| **Maximum Drawdown** | -3.92% | -3.92% (reported as ~-4% in README) |
| **Correlation with BTC** | 0.014 | **0.014** (reported as 0.01 in README) |
| **Annualized Alpha vs. BTC** | 0.030 (3.0%) | 0.030 (3.0%) |
| **Beta vs. BTC** | 0.002 | 0.002 |
| **Alpha t-statistic** | 1.020 | 1.020 |
| **Cumulative OOS Net Return** | +10.6% (0.106) | +10.6% (0.106) |

#### 4. Blended Portfolio Diversification with BTC (Cell 68)

| Allocation | Annualized Sharpe Ratio |
| :--- | :--- |
| **BTC 0.0 / Strategy 1.0** | 0.576 |
| **BTC 0.1 / Strategy 0.9** | **0.896** (reported as 0.93 in README for tuned blend) |
| **BTC 0.2 / Strategy 0.8** | 0.873 |
| **BTC 0.3 / Strategy 0.7** | 0.823 |
| **BTC 0.5 / Strategy 0.5** | 0.761 |
| **BTC 0.7 / Strategy 0.3** | 0.728 |
| **BTC 1.0 / Strategy 0.0** | 0.702 |

### Independently reproduced

Not independently reproduced. All figures and claims represent third-party empirical findings reported by Kavya Nanda (`NandaDynasty`) in GitHub commit `2278f61e7b6c1811f13bbbc298e5fd68c80015d0`.

### Negative evidence

1. **Cross-Sectional Reversal Cost Annihilation:** Even with aggressive volume-conditioning filters, daily and intraday reversal strategies suffer massive turnover drag ($\sim 1.45$ turnover per period), converting apparent predictive power into severe capital erosion ($-11.35$ to $-28.01$ cumulative log loss at 20 bps fees) (`source-reported`).
2. **Multiple-Testing Mortality Rate:** Out of 310 tested pairs exhibiting correlation $> 0.70$, 268 pairs ($86.5\%$) fail basic cointegration ($p \ge 0.05$). Of the 42 nominally significant pairs, 34 ($81.0\%$) fail Benjamini-Hochberg FDR control ($q \ge 0.05$), and 38 ($90.5\%$) fail Bonferroni control ($p \ge 0.000161$) (`source-reported`).
3. **The Drifting Hedge-Ratio Friction Drag:** Continuous drift in rolling OLS $\beta_t$ doubles daily portfolio turnover ($0.0032 \to 0.0065$), demonstrating that stationary spread trading incurs substantial hidden rebalancing costs even in low-turnover regime settings (`source-reported`).
4. **Statistically Weak Alpha:** Out-of-sample alpha against Bitcoin exhibits a t-statistic of only $1.020$ ($p \approx 0.31$), failing standard institutional significance gates ($t > 2.0$) over the 2.8-year holdout (`source-reported`).

## Falsification plan

1. **Borrow Rate and Margin Cost Stress Test:**
   - *Test:* Inject realistic crypto spot margin borrow rates ($8\%\text{--}15\%$ APR on the short leg) into `compute_pair_return_v2`.
   - *Failure Rule:* Strategy net OOS Sharpe drops below $0.20$ or net annualized return falls below zero (`research-defined falsification threshold`).
   - *Action:* Conclude that spot crypto pairs trading is unviable without perpetual futures shorting.
2. **Ablation of Naive Pairs Set:**
   - *Test:* Restrict the portfolio strictly to the 8 Benjamini-Hochberg survivors ($\mathcal{P}_{\text{bonf}} \cup \mathcal{P}_{\text{bh}}$), removing the 34 naive-significant pairs entirely.
   - *Failure Rule:* Net OOS Sharpe deteriorates or maximum drawdown exceeds $-10\%$ (`research-defined falsification threshold`).
   - *Action:* If performance drops, conclude the strategy relies on residual dispersion from naive pairs rather than statistical cointegration integrity.
3. **Parameter Stability Perturbation:**
   - *Test:* Perturb entry threshold $z_{\text{entry}} \in [4.5, 7.5]$ in steps of $0.5$ and rolling lookback $W \in [60, 120]$ days.
   - *Failure Rule:* Over $40\%$ of parameter variations produce negative net OOS returns or Sharpe $< 0.25$ (`research-defined falsification threshold`).
   - *Action:* Reject fixed threshold $z = (6.0, 2.5, 9.0)$ as an overfitted in-sample artifact.
4. **Sub-Period Regime Stress Test:**
   - *Test:* Evaluate OOS performance separately during high-volatility liquidity shocks (e.g. November 2023 rally, August 2024 unwind).
   - *Failure Rule:* Realized drawdown during any single 30-day window exceeds $-8\%$ (`research-defined falsification threshold`).
   - *Action:* Require an explicit market-wide volatility regime gate to halt trading during market-wide dislocations.

## Crypto portability

- **Portability Classification:** `direct` for cryptocurrency spot markets; `adapted/unproven` for cryptocurrency perpetual futures (`research-proposed`).
- **Primary Demonstration:** The cited research was conducted directly on cryptocurrency assets (406 Binance spot tokens, 2021–2026) (`source-reported`).
- **Spot vs. Perpetual Nuances:**
  - *Spot Execution Barriers:* In spot markets, shorting requires borrowing coins via margin lending. Many altcoins in the 42-pair universe (e.g. `STEEM`, `BTTC`, `MOVR`) have illiquid margin lending pools, high borrow fees ($>20\%$ APR), or zero shorting availability on Binance Margin (`research-proposed`).
  - *Perpetual Futures Adaptation:* Porting the strategy to perpetual futures eliminates spot borrow constraints, but introduces funding-rate divergence. If asset A pays a high positive funding rate while asset B pays negative funding, the carry spread may overwhelm the mean-reverting alpha (`research-proposed`).
- **Market Microstructure & 24/7 Liquidity:** Crypto spot order books exhibit wide bid-ask spreads during low-volume Asian/European session boundaries. Daily bar execution at 00:00 UTC captures exchange reset volume but may incur higher slippage on illiquid altcoin pairs (`research-proposed`).

## Limitations

- **Spot Shorting Borrow Friction Gap:** The backtest engine assumes free, unconstrained shorting. In physical crypto spot trading, shorting requires collateralized borrowing with variable rates and recall risk (`source-reported`).
- **Limited Out-of-Sample Track Record:** The out-of-sample test spans ~2.8 years (`2023-06-01` to `2026-04-18`). While positive, the alpha t-statistic of $1.020$ is not statistically distinguishable from zero at the $5\%$ level (`source-reported`).
- **In-Sample Pair Selection Snooping:** While pair selection was restricted to in-sample data, the $r > 0.70$ correlation filter was computed on log returns before cointegration testing, potentially pre-filtering out non-linear co-moving assets (`source-reported`).
- **Lack of Microstructure Slippage Modeling:** Flat 20 bps fee assumption does not account for size-dependent market impact on low-liquidity pairs like `BTTC` or `CVC` (`research-proposed`).

## Implementation status

`not-implemented`.

This research record represents an external public research capture from GitHub repository `NandaDynasty/CryptoStatArb`. No strategy implementation, factor pipeline, or execution model has been created in PyBroker, NautilusTrader, paper trading, testnet, or live environments.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`

Presence in this repository does not indicate that the strategy is profitable, approved for production, or cleared for live/testnet/paper deployment. It serves exclusively as normalized empirical research material for downstream hypothesis synthesis.

## Related Wiki records

- `crypto-pairs-trading-cointegration-overfitting-falsification-2026-09-13.md` (rfukuda06 2026: Cointegration data snooping and in-sample parameter overfitting in spot crypto pairs)
- `crypto-perpetual-pairs-trading-cointegration-hurst-halflife-walkforward-2026-09-12.md` (etoh0305 2026: Binance perpetual futures pairs trading with Hurst filters and half-life ranking)
- `crypto-perpetual-pairs-trading-kalman-cointegration-falsification-2026-09-11.md` (djienne 2026: Dynamic Kalman filter cointegration tracking under synthetic OU drift injection)
- `us-etf-pairs-trading-cointegration-cost-viability-falsification-2026-09-13.md` (michaelmross 2026: Anti-correlation between cointegration p-value and cost viability in US ETFs)
- `tether-pairs-trading-fdr-kalman-half-life-net-beta-2026-09-12.md` (FDR filtering and Kalman beta tracking in crypto pairs)

## Sources

1. Kavya Nanda (`NandaDynasty`). *"Statistical Arbitrage in Cryptocurrencies"*. Public GitHub repository, commit `2278f61e7b6c1811f13bbbc298e5fd68c80015d0`, committed September 11, 2026.
   - Repository URL: [https://github.com/NandaDynasty/CryptoStatArb](https://github.com/NandaDynasty/CryptoStatArb)
   - Canonical Tree URL: [https://github.com/NandaDynasty/CryptoStatArb/tree/2278f61e7b6c1811f13bbbc298e5fd68c80015d0](https://github.com/NandaDynasty/CryptoStatArb/tree/2278f61e7b6c1811f13bbbc298e5fd68c80015d0)
   - Research Notebook: [`Crypto_StatArb.ipynb`](https://github.com/NandaDynasty/CryptoStatArb/blob/2278f61e7b6c1811f13bbbc298e5fd68c80015d0/Crypto_StatArb.ipynb)
   - Overview and Lessons: [`README.md`](https://github.com/NandaDynasty/CryptoStatArb/blob/2278f61e7b6c1811f13bbbc298e5fd68c80015d0/README.md)
