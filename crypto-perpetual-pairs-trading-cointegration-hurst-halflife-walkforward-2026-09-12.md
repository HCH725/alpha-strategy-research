---
schema: strategy-research-record-v1
title: "Market-Neutral Crypto Perpetual Pairs Trading: Engle-Granger Cointegration, Hurst Anti-Persistence Filter, and Half-Life Ranked Portfolio in Walk-Forward Validation"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - pairs-trading
  - statistical-arbitrage
  - cointegration
  - hurst-exponent
  - half-life
  - walk-forward
  - market-neutral
status: research-only
confidence: medium
source_as_of: 2026-09-04
sources:
  - "GitHub repository: etoh0305/crypto-pairs-trading-research (commit 1c58616b3a8375a394bf9663b4f1727bdecb3c93, paths notebooks/Pairs_Trading_Top300_HalfLife.ipynb and results/fold_results.csv, published September 2026)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Market-Neutral Crypto Perpetual Pairs Trading: Engle-Granger Cointegration, Hurst Anti-Persistence Filter, and Half-Life Ranked Portfolio in Walk-Forward Validation

## Provenance

- **Repository**: `https://github.com/etoh0305/crypto-pairs-trading-research`
- **Full Commit SHA**: `1c58616b3a8375a394bf9663b4f1727bdecb3c93`
- **Exact File Paths**:
  - `notebooks/Pairs_Trading_Top300_HalfLife.ipynb` (executable research notebook with embedded results and look-ahead verification)
  - `results/fold_results.csv` (tabular metrics across all 7 walk-forward folds)
  - `README.md` (project overview and summary table)
  - `data/README.md` (data schema, hourly candle layout, and survivorship-handling documentation)
- **Author**: `etoh0305`
- **Publication / Commit Date**: 2026-09-04
- **License**: MIT License
- **Primary Source Data Span**: 2022-01-01 to 2026-07-31 (Binance USDT perpetual hourly OHLCV candles, universe listing/delisting metadata, and hourly historical funding rates)
- **Out-of-Sample Walk-Forward Span**: 2023-01-01 to 2026-07-01 across 7 non-overlapping 6-month test folds

## Economic mechanism

### Source-reported

The strategy exploits mean-reverting pricing discrepancies across pairwise combinations of USDT-margined cryptocurrency perpetual futures contracts on Binance. The author identifies three sequential economic and statistical mechanisms:

1. **Cointegration Equilibrium**: Crypto asset pairs often share common latent factors (e.g., Layer-1 infrastructure adoption, DeFi capital flows, general crypto market liquidity, common market-making algorithms). When two price series are cointegrated, a stationary linear combination $\ln(P_1) - \alpha - \beta \ln(P_2) = \epsilon$ exists, representing a long-term economic equilibrium. Divergences from this residual spread reflect temporary liquidity imbalances or localized order-flow shocks rather than permanent structural divergence.
2. **Anti-Persistence Filtering via Hurst Exponent**: Standard cointegration tests on large panels suffer from false positives. Estimating the Hurst exponent ($H$) on the residual spread filters out pairs with random-walk ($H \approx 0.50$) or persistent/trending ($H > 0.50$) behavior, retaining only pairs with demonstrated sub-diffusive, anti-persistent dynamics ($H < 0.40$).
3. **Half-Life Ranking for Capital Efficiency**: Pairs that mean-revert quickly incur less exposure time to structural cointegration breakdown, reduce inventory risk, and turn over capital more rapidly. Ranking candidate pairs by their Ornstein-Uhlenbeck / AR(1) estimated half-life ($t_{1/2}$) and capping the active portfolio at the top 300 shortest half-life pairs concentrates capital in high-frequency mean-reverting relationships.

The strategy is strictly market-neutral, scaling leg allocations by the OLS hedge ratio $\beta$ so that broader market directional moves (e.g., Bitcoin rallies or sell-offs) are hedged out.

### Research interpretation

This is an empirical cross-sectional statistical arbitrage research study adapted natively to cryptocurrency perpetual futures. The primary economic rationale is that decentralized market-making, algorithmic cross-venue arbitrage, and sector co-movement constrain the relative valuations of correlated crypto tokens. When idiosyncratic order flow temporarily dislocates one token relative to its cointegrated peer, contrarian liquidity provision harvests the spread as the pricing anomaly mean-reverts.

Crucially, the author's architecture introduces a three-tier funnel:
- **Tier 1 (Statistical existence)**: Vectorized Engle-Granger test ($p < 0.05$, $\beta > 0$).
- **Tier 2 (Time-series quality)**: Hurst anti-persistence filter ($H < 0.40$).
- **Tier 3 (Operational efficiency)**: Half-life ranking cap ($N \le 300$).

The primary hazard in crypto pairs trading is that statistical cointegration over a 12-month formation window is frequently non-stationary out-of-sample: tokenomic inflation, governance token exploits, listing/delisting actions, protocol upgrades, or structural liquidity dry-ups can permanently shatter historical relationships, leading to catastrophic divergence. The Hurst filter and half-life ranking represent explicit defensive screens against this non-stationarity.

## Signal

The signal and trading workflow execute in a 6-month walk-forward rolling cycle:

```text
[12-Month Formation Window (8,760 hours)]
       ↓
Filter 1: Point-in-Time Universe Eligibility (coverage ≥ 98%, active at decision date, flatline filters)
       ↓
Filter 2: Vectorized Engle-Granger Cointegration (p < 0.05, beta > 0, 6 ADF lags)
       ↓
Filter 3: Hurst Exponent Anti-Persistence Filter (H < 0.40 across 25 log-spaced lags)
       ↓
Ranking & Portfolio Cap: Sort by AR(1) Half-Life ascending → Select top 300 shortest half-life pairs
       ↓
[6-Month Out-of-Sample Trading Window (4,380 hours)]
       ↓
Calculate z-score: z_t = (ln(P_1,t) - alpha - beta * ln(P_2,t)) / sigma_u
       ↓
State Machine:
  - Re-arming: pair must visit |z_t| < 2.0 while flat before arming
  - Entry: Long spread if z_t < -2.0; Short spread if z_t > 2.0
  - Exit: Reversion to zero (z_t crosses 0) OR holding time >= round(half_life) OR fold expiration
```

### Mathematical formulation

#### 1. Cointegration parameter estimation
On the formation window $W$ (12 months = 8,760 hourly bars [source-reported]):
- OLS regression of log prices:
  $$\ln(P_{1,t}) = \alpha + \beta \ln(P_{2,t}) + u_t$$
  Enforcing $\beta > 0$ [source-reported].
- Residual standard deviation: $\sigma_u = \sqrt{\frac{\sum u_t^2}{n-2}}$ [source-reported].
- Augmented Dickey-Fuller (ADF) regression on residuals with 6 lags (`MAXLAG = 6` [source-reported]):
  $$\Delta u_t = \rho u_{t-1} + \sum_{k=1}^{6} \gamma_k \Delta u_{t-k} + \epsilon_t$$
  Test statistic: $t_{\rho} = \hat{\rho} / \text{SE}(\hat{\rho})$.
- MacKinnon p-value calculated for model with constant and $N=2$ variables [source-reported].
- Cointegration criterion: $p < 0.05$ (`ALPHA = 0.05` [source-reported]).

#### 2. Hurst exponent calculation
Computed on residual spread series $S$ across 25 log-spaced lag intervals $\tau \in [2, 1024]$ hours (`LAGS = np.unique(np.round(np.logspace(np.log10(2), np.log10(1024), 25)).astype(int))` [source-reported]):
- Standard deviation of increments: $\sigma(\tau) = \text{std}(S_{t+\tau} - S_t)$.
- OLS slope of $\ln \sigma(\tau)$ against $\ln \tau$:
  $$H = \frac{\text{Cov}(\ln \tau, \ln \sigma(\tau))}{\text{Var}(\ln \tau)}$$
- Anti-persistence filter: $H < 0.40$ (`H_MAX = 0.40` [source-reported]).

#### 3. Half-life calculation
Estimated via discrete AR(1) specification on the spread:
$$\Delta S_t = \lambda S_{t-1} + \epsilon_t$$
$$t_{1/2} = -\frac{\ln 2}{\ln(1 + \hat{\lambda})}$$
Only pairs with $\hat{\lambda} < 0$ and finite $t_{1/2}$ are retained [source-reported].

#### 4. Selection and ranking cap
Candidate pairs clearing $p < 0.05$, $\beta > 0$, and $H < 0.40$ are sorted in ascending order of estimated half-life $t_{1/2}$. The top $N = \min(\text{eligible}, 300)$ pairs are selected for trading (`N_PAIRES = 300` [source-reported]). Parameters $\alpha$, $\beta$, $\sigma_u$, and $t_{1/2}$ are frozen for the subsequent 6-month trading fold [source-reported].

#### 5. Trading state machine and execution rules
On the out-of-sample trading window $t \in [T_{\text{train}}, T_{\text{train}} + 4380]$:
- Standardized spread at bar $t$:
  $$z_t = \frac{\ln(P_{1,t}) - \alpha - \beta \ln(P_{2,t})}{\sigma_u}$$
- **Re-arming condition**: A pair must satisfy $|z_t| < 2.0$ while position is 0 to become `armed = True` (`Z_ENTRY = 2.0` [source-reported]). This prevents entering a pair that is already drifting wide at fold inception.
- **Short spread entry**: If `position == 0` and `armed == True` and $z_t > 2.0$:
  $$\text{position}_{t} = -1 \quad (\text{Short } P_1, \text{ Long } P_2 \text{ with hedge ratio } \beta)$$
  Record entry bar $t_{\text{entry}} = t$; set `armed = False` [source-reported].
- **Long spread entry**: If `position == 0` and `armed == True` and $z_t < -2.0$:
  $$\text{position}_{t} = +1 \quad (\text{Long } P_1, \text{ Short } P_2 \text{ with hedge ratio } \beta)$$
  Record entry bar $t_{\text{entry}} = t$; set `armed = False` [source-reported].
- **Exit triggers** (evaluated at bar $t$, in order of priority):
  1. *Mean reversion*: If $\text{position} == -1$ and $z_t \le 0.0$, OR if $\text{position} == +1$ and $z_t \ge 0.0$ [source-reported].
  2. *Half-life timeout*: If $\text{position} \neq 0$ and holding duration $(t - t_{\text{entry}}) \ge \text{round}(t_{1/2})$ [source-reported].
  3. *Data unavailability*: If $z_t$ is NaN/missing [source-reported].
  4. *Fold termination*: If $t = T_{\text{test}} - 1$ (final bar of 6-month trading fold), all open positions are closed [source-reported].

#### 6. Position sizing and PnL accounting
- Capital allocation: Initial portfolio capital is 100 USD, divided equally across the $N$ selected pairs:
  $$\text{Scale per pair} = \frac{100.0}{N}$$
  Gross notional exposure per pair is 1 unit, normalized by $(1 + \beta)$ [source-reported].
- Spread return for bar $t$:
  $$\Delta S_{\text{return}, t} = \frac{\Delta \ln P_{1,t} - \beta \Delta \ln P_{2,t}}{1 + \beta}$$
- Hourly funding cashflow for bar $t$:
  $$\Delta F_{\text{diff}, t} = \frac{F_{1,t} - \beta F_{2,t}}{1 + \beta}$$
  $$\text{PnL}_{\text{funding}, t} = -\text{position}_t \times \Delta F_{\text{diff}, t}$$
- Fee accounting: Taker fee of 4.5 bps per transaction applied on turnover $|\Delta \text{position}|$:
  $$\text{Fee}_t = -0.00045 \times |\text{position}_t - \text{position}_{t-1}| \quad (\text{FEE} = 0.00045 \text{ [source-reported]})$$
- Net bar PnL: $\text{PnL}_{\text{net}, t} = \text{position}_{t-1} \cdot \Delta S_{\text{return}, t} + \text{PnL}_{\text{funding}, t} + \text{Fee}_t$ [source-reported].

### Operational parameters classification

| Parameter | Value | Provenance Classification | Notes |
|:---|:---|:---|:---|
| `TRAIN_M` | 12 months (8,760 h) | source-reported | In-sample formation window |
| `STEP_M` | 6 months (4,380 h) | source-reported | Out-of-sample trading fold |
| `ALPHA` | 0.05 | source-reported | Cointegration p-value cutoff (MacKinnon) |
| `MAXLAG` | 6 | source-reported | ADF regression lag order |
| `H_MAX` | 0.40 | source-reported | Hurst anti-persistence filter threshold |
| `Z_ENTRY` | 2.0 | source-reported | Entry trigger threshold |
| `Z_EXIT` | 0.0 | source-reported | Mean reversion exit threshold |
| `N_PAIRES` | 300 | source-reported | Portfolio pair cap |
| `FEE` | 0.00045 (4.5 bps) | source-reported | Taker fee per leg turnover |
| `COV_MIN` | 0.98 (98%) | source-reported | Minimum non-NaN bar coverage |
| `MIN_LIVE` | 120 days (2,880 h) | source-reported | Minimum listing age |
| `EXCLUS` | `{"BTCDOMUSDT", "DEFIUSDT", "FOOTBALLUSDT", "BLUEBIRDUSDT", "^1000"}` | source-reported | Index/meme contract exclusions |
| Execution timing | Next-bar open fill after bar close signal | research-proposed | Source applies position decided at $t-1$ to return at $t$ |
| Stop-loss cutoff | $\|z_t\| \ge 4.0$ divergence stop | research-proposed | Source has NO z stop-loss; only timeout/reversion |
| Slippage assumption | 2.5 - 5.0 bps per leg | research-proposed | Source omitted slippage; needed for stress test |
| Bid-ask spread | Quoted half-spread model | research-proposed | Source omitted bid-ask spread |
| FDR correction | Benjamini-Hochberg $q=0.05$ | research-proposed | Source noted p<0.05 lacks FDR correction |

## Required data

- **Instruments**: Binance USDT-margined linear perpetual futures contracts (`.swap` / `USDT`).
- **Timeframe**: 1-hour OHLCV candles (`timestamp`, `open`, `high`, `low`, `close`, `volume`).
- **Funding Rates**: Historical hourly funding rates (`symbol`, `calc_time`, `funding_rate`) matching each contract.
- **Listing & Universe Metadata**: Point-in-time universe table (`universe_full.csv`) containing `symbol`, `last_trade`, `n_live`, and `delisted` status [source-reported].
- **Exclusions**:
  - Index-based perpetuals (`BTCDOMUSDT`, `DEFIUSDT`, `FOOTBALLUSDT`, `BLUEBIRDUSDT`) [source-reported].
  - Multiplier-denominated meme contracts starting with `1000` (e.g., `1000PEPEUSDT`, `1000SHIBUSDT`) [source-reported].
- **Point-in-time and survivorship integrity**:
  - Delisted contracts are explicitly retained in the historical database and truncated at their exact last traded candle (`last_trade`) [source-reported].
  - Contracts are required to have been active from the start of the training window (`W.iloc[:24].notna().any()`) and still alive at the decision timestamp (`last_trade >= decision_time`) [source-reported].
  - Look-ahead test: Cell 18 in the source notebook explicitly tests for look-ahead bias by setting all data after the decision timestamp to NaN and verifying that pair selection and trading PnL are bit-for-bit identical (`ok1 = True`, `ok2 = True`) [source-reported].
- **Missing Data Handling**:
  - Missing hourly candles (e.g., during Binance scheduled maintenance) are forward-filled then back-filled, but only after verifying overall coverage $\ge 98\%$ (`COV_MIN = 0.98`) [source-reported].
  - Flat-line sanity filters: Series with price standard deviation $\le 10^{-6}$ or zero-return frequency $\ge 90\%$ are rejected to prevent degenerate cointegration artifacts [source-reported].

## Execution assumptions

- **Signal-to-order timing**: Signal formed at close of hourly bar $t-1$; executed across the interval leading into bar $t$.
- **Fill model**: Evaluated at hourly close prices without order book simulation [source-reported]. No queue priority, partial fills, or execution latency modeled.
- **Taker fees**: Modeled explicitly at 4.5 bps (0.045%) per side/turnover (`FEE = 0.00045` [source-reported]).
- **Funding payments**: Modeled explicitly using exact historical funding rates accrued each hour [source-reported].
- **Slippage**: Assumed 0.0 bps in primary backtest [source-reported limitation].
- **Bid-ask spread**: Assumed 0.0 bps in primary backtest [source-reported limitation].
- **Market impact / capacity**: Not modeled [source-reported limitation].
- **Shorting / Margin**: Perpetual contracts allow symmetric long and short positions without borrow fees; portfolio modeled with unconstrained margin on $100 nominal capital [source-reported].

## Evidence

### Source-reported

All quantitative figures below trace directly to `notebooks/Pairs_Trading_Top300_HalfLife.ipynb` (outputs of Cells 13, 15, and 18) and `results/fold_results.csv` in repository `etoh0305/crypto-pairs-trading-research` (commit `1c58616b3a8375a394bf9663b4f1727bdecb3c93`):

#### 1. Aggregate composite performance (2023-01-01 to 2026-07-01, 7 folds, 3.5 years)
- **Annualized Sharpe Ratio**: **2.24** (exact: `2.239265`)
- **Annualized Net Return**: **7.79%** (exact: `7.791604%`)
- **Annualized Volatility**: **3.48%** (exact: `3.479537%`)
- **Maximum Drawdown**: **-2.96%** (exact: `-2.964609%`)
- **Positive Folds**: **7 / 7** (100% positive folds)
- **Total Completed Round-Trips**: **16,495**
- **PnL Decomposition on 100 USD Initial Capital**:
  - Gross Spread PnL: **+40.92 USD** (exact: `+40.918163 USD`)
  - Total Taker Fees Paid: **-4.95 USD** (exact: `-4.948500 USD`)
  - Total Historical Funding Cashflow: **-8.70 USD** (exact: `-8.699047 USD`)
  - Net Realized PnL: **+27.27 USD** (exact: `+27.270616 USD`)

#### 2. Detailed per-fold walk-forward breakdown

| Fold Start | Test End | Active Assets | Tested Pairs | Cointegrated ($p<0.05$) | Eligible ($H<0.40$) | Traded ($N$) | Trades | Annualized Sharpe | Net PnL ($) | Gross PnL ($) | Fees ($) | Funding ($) | Median $t_{1/2}$ (h) | Median Hurst |
|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2023-01-01 | 2023-07-02 | 120 | 7,140 | 1,652 | 664 | 300 | 2,242 | 2.67 | +3.96 | +5.36 | -0.67 | -0.73 | 119.39 | 0.373 |
| 2023-07-02 | 2023-12-31 | 129 | 8,256 | 1,443 | 630 | 300 | 2,094 | 0.83 | +1.33 | +3.73 | -0.63 | -1.77 | 126.03 | 0.369 |
| 2024-01-01 | 2024-07-01 | 136 | 9,180 | 1,981 | 875 | 300 | 2,454 | 2.67 | +4.93 | +5.67 | -0.74 | +0.002 | 123.29 | 0.366 |
| 2024-07-01 | 2024-12-30 | 169 | 14,196 | 1,432 | 577 | 300 | 2,321 | 2.85 | +4.70 | +5.62 | -0.70 | -0.22 | 131.43 | 0.370 |
| 2024-12-31 | 2025-07-01 | 203 | 20,503 | 2,769 | 1,173 | 300 | 2,116 | 1.65 | +3.44 | +5.48 | -0.63 | -1.40 | 103.03 | 0.354 |
| 2025-07-01 | 2025-12-30 | 231 | 26,565 | 3,132 | 1,506 | 300 | 2,163 | 1.34 | +2.36 | +4.74 | -0.65 | -1.73 | 97.78 | 0.354 |
| 2025-12-31 | 2026-07-01 | 293 | 42,778 | 7,428 | 3,656 | 300 | 3,105 | 3.86 | +6.55 | +10.33 | -0.93 | -2.85 | 75.70 | 0.342 |

#### 3. Source sanity and consistency audits
- **Look-Ahead Verification**: The author sets future data to NaN and re-runs both pair selection and trade execution; output confirmed bit-for-bit identical results (`AUCUNE FUITE` logged in Cell 18) [source-reported].
- **Fee Sanity Audit**: Average fee paid per round-trip is exactly 9.0 bps (`2 * FEE * 1e4 = 9.0 bp`) [source-reported].
- **Vectorized Engine Parity**: Vectorized batch Engle-Granger compared against `statsmodels.tsa.stattools.coint` across 66 random synthetic series: maximum ADF statistic deviation was $2.0 \times 10^{-8}$, p-value deviation was $6.4 \times 10^{-9}$, and classification disagreement at $p < 0.05$ was exactly 0 [source-reported].

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Substantial Funding Drag**: Funding cashflows systematically drained gross profits in 6 out of 7 folds, totaling -$8.70 USD or **21.3% of total gross spread PnL** (-$8.70 / +$40.92). In fold 2025-12-31, funding costs reached -$2.85 USD against +$10.33 USD gross PnL (27.6% drag).
- **Multiple Testing / False Discovery Hazard**: Across the folds, tested pairs scaled from 7,140 to 42,778. At an unadjusted significance level $\alpha = 0.05$, a purely random un-cointegrated universe would yield between $0.05 \times 7140 = 357$ and $0.05 \times 42778 = 2,139$ spurious cointegration discoveries. The author explicitly notes that no False Discovery Rate (FDR) or family-wise error rate (FWER) correction was applied [source-acknowledged gap].
- **Thin Net Margin per Trade**: Average net profit per completed round-trip trade is:
  $$\frac{27.27 \text{ USD}}{16,495 \text{ trades}} \approx 0.001653 \text{ USD per trade on a } \approx 0.33 \text{ USD allocated position}$$
  This corresponds to approximately **50.1 bps net edge per trade**. Because 9.0 bps are consumed by taker fees and $\approx 5.3$ bps by funding drag, an unmodeled slippage of only $2.5$ bps per leg (5.0 bps round trip) would consume an additional 10% of total edge, and a 15 bps adverse execution error would destroy nearly a third of net profit.
- **Absence of Adverse Divergence Stop-Loss**: The strategy holds diverging pairs until the estimated half-life expires ($t \ge t_{1/2}$). If a pair permanently delinks, the trade absorbs unbounded adverse divergence until the time-stop fires, risking severe drawdown during tail events.
- **Static Beta Exposure**: Hedge ratio $\beta$ is held constant for an entire 6-month out-of-sample trading fold, ignoring crypto market regime shifts and beta drift.

## Falsification plan

The following falsification protocol is designed to test the robustness and boundary limits of the cointegration/Hurst/half-life hypothesis:

1. **Slippage and Bid-Ask Spread Stress Test**:
   - *Protocol*: Apply incremental one-way slippage tiers: 0.0, 2.5, 5.0, 7.5, and 10.0 bps per leg (using realistic order book depth snapshots from Binance USDT perpetuals).
   - *Falsification threshold*: If composite annualized Sharpe drops below 0.75 or net annualized PnL becomes negative at $\le 5.0$ bps one-way slippage (`research-defined falsification threshold`).
2. **False Discovery Rate (FDR) Benjamini-Hochberg Audit**:
   - *Protocol*: Apply the Benjamini-Hochberg procedure at false discovery rate $q = 0.05$ across all $M(M-1)/2$ tested p-values per fold prior to applying Hurst and half-life ranking (`research-proposed`).
   - *Falsification threshold*: If fewer than 25 pairs survive the FDR threshold in $\ge 3$ folds, or if post-FDR walk-forward Sharpe degrades below 1.0 (`research-defined falsification threshold`).
3. **Adverse Divergence Stop-Loss Ablation**:
   - *Protocol*: Test the addition of an explicit z-score stop-loss at $|z_t| \ge 4.0$ (`research-proposed`).
   - *Falsification threshold*: If the stop-loss triggers on $> 35\%$ of trades and degrades overall net PnL by $> 25\%$, indicating that mean-reversion in crypto pairs commonly requires deep excursions before snapping back (`research-defined falsification threshold`).
4. **Hurst Filter Ablation Test**:
   - *Protocol*: Run the walk-forward simulation without the Hurst filter ($H < 0.40$), selecting the top 300 pairs solely by Engle-Granger $p < 0.05$ and half-life ranking.
   - *Falsification threshold*: If omitting the Hurst filter produces equivalent or higher Sharpe and drawdown, falsifying the author's claim that Hurst anti-persistence filtering is an essential alpha-preserving gate (`research-defined falsification threshold`).
5. **Funding Rate Shuffling / Permutation Test**:
   - *Protocol*: Randomly shuffle the hourly funding rates across symbols to evaluate whether the strategy's funding drag is structural (i.e. shorting higher-carry assets) or random.
   - *Falsification threshold*: If actual funding drag is significantly worse ($p < 0.01$) than shuffled funding, proving that the cointegration signal systematically bets against the funding rate carry direction (`research-defined falsification threshold`).
6. **Market Crash / Liquidity Dislocation Stress (2022 LUNA/FTX or March 2023 SVB/USDC Depeg)**:
   - *Protocol*: Evaluate strategy behavior during historical structural collapse events.
   - *Falsification threshold*: Max drawdown exceeding 15% or single-fold loss exceeding 10% on allocated capital (`research-defined falsification threshold`).

## Crypto portability

**Direct**.

The strategy was conceptualized, implemented, and empirically validated natively on cryptocurrency perpetual futures (Binance USDT-margined linear contracts) across the 2022 to 2026 historical period. It explicitly incorporates crypto-native microstructure characteristics:
- **Perpetual Funding Cashflows**: Modeled hourly using Binance's 8-hour funding rate schedules interpolated to hourly timestamps.
- **Continuous 24/7 Session**: 8,760 hourly bars per calendar year without market opens, closes, or weekend auction breaks.
- **Contract Churn & Delistings**: Explicitly accounted for through point-in-time universe filters and truncation at delisting timestamps.
- **Linear USDT Margining**: Both long and short legs settle in USDT, eliminating inverse-contract margin currency convexity risk.

**Crypto-Specific Friction Warning**: Cross-pair funding divergence is a major operational risk. If a pair involves a token with persistent positive funding (e.g., bull market retail long crowding) and a token with persistent negative funding, entering a short-spread position forces the trader to pay funding on both legs, creating severe carry drag.

## Limitations

- **Omission of Execution Microstructure**: The backtest assumes fill-at-close execution. In reality, simultaneously executing two market orders across less liquid altcoin perpetuals incurs bid-ask crossing costs, queue delay, and leg execution risk (partial fills on leg 1 leaving naked directional risk before leg 2 executes).
- **Zero Slippage Modeling**: Across 16,495 round trips, zero slippage was modeled. In volatile crypto markets, 2.5 to 5 bps slippage per side is common, which would significantly impair the 50 bps net profit margin per trade.
- **Multiple Testing Bias**: Evaluating up to 42,778 pairs simultaneously without FDR / Bonferroni adjustment guarantees dozens of spurious cointegrations that appear stationary purely by chance.
- **Static In-Sample Parameters**: OLS regression coefficients ($\alpha, \beta$) and residual standard deviation $\sigma_u$ are frozen for 6 months. Crypto cointegration vectors frequently shift within weeks due to changing market regimes.
- **Lack of Stop-Loss Mechanism**: No divergence stop exists in the author's specification. A pair that experiences fundamental tokenomic failure can run against the position until the half-life timeout occurs, causing tail drawdowns.
- **Equal Capital Allocation**: Capital is divided equally ($100 / N$), ignoring the vastly different volatility, liquidity, and margin requirements across different altcoins.
- **Single Venue**: The empirical study tests only Binance USDT perpetuals; venue-specific liquidations and pricing anomalies may not generalize to Hyperliquid, Bybit, or OKX.

## Implementation status

not-implemented

This document represents external research normalization only. No implementation in NautilusTrader, PyBroker, paper trading, testnet, or live trading has been performed.

## Adoption boundary

This record is research material only. It does not constitute:
- Evidence of live commercial profitability
- Validated alpha ready for capital allocation
- Approval for NautilusTrader or PyBroker production implementation
- Authorization for paper trading, testnet execution, or live deployment

Any future progression requires independent backtesting in NautilusTrader with realistic order book slippage, bid-ask spreads, and FDR multiple-testing corrections.

## Related Wiki records

- `[[quant/cointegration-ecm-var-granger-2026-08-28]]` — theoretical foundation for econometric cointegration, error correction, and vector autoregression.
- `[[quant/crypto-adaptive-trailing-stop-volatility-filtered-cointegrated-pairs-trading-2026-09-07]]` — empirical pairs trading study incorporating volatility filtering and trailing stops.
- `[[quant/crypto-perpetual-pairs-trading-kalman-cointegration-falsification-2026-09-11]]` — Kalman filter dynamic hedge ratio adaptation and cross-asset pairs trading falsification.
- `[[quant/crypto-statistical-arbitrage-pca-residual-cointegration-falsification-2026-09-12]]` — empirical falsification of PCA residual mean-reversion under realistic bid-ask spreads and liquidity tiers.
- `[[quant/copula-cmi-crypto-perpetual-pairs-trading-market-overlay-2026-09-07]]` — non-linear dependence and copula-based crypto pairs trading overlays.
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]` — canonical validation rules for preventing point-in-time leakage and forward-looking data contamination.

## Sources

1. **GitHub Repository**: `https://github.com/etoh0305/crypto-pairs-trading-research`
2. **Immutable Commit SHA**: `1c58616b3a8375a394bf9663b4f1727bdecb3c93`
3. **Primary Implementation & Notebook**: `notebooks/Pairs_Trading_Top300_HalfLife.ipynb`
4. **Primary Empirical Results File**: `results/fold_results.csv`
5. **Project Documentation**: `README.md` and `data/README.md`
6. **Data & Methodology As-Of Date**: 2026-09-04
