---
schema: strategy-research-record-v1
title: "Continuous Wavelet Transform Band-Pass Mean-Reversion and HMM Volatility Stress Risk Overlay in Commodity Futures"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - wavelet-analysis
  - continuous-wavelet-transform
  - hidden-markov-model
  - regime-detection
  - risk-overlay
  - commodity-futures
  - crude-oil
  - mean-reversion
status: research-only
confidence: medium
source_as_of: 2026-09-06
sources:
  - "Tommaso Zeri, Wavelet-Based Signal Extraction and Regime Detection in Commodity Futures: A Rigorous Walk-Forward Study, GitHub repository tommasozeri/Wavelet-strategy-analysis, commit 6d766d411aeb2820203a329571b3da908f18b5ba, September 6, 2026. Stable URL: https://github.com/tommasozeri/Wavelet-strategy-analysis"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Continuous Wavelet Transform Band-Pass Mean-Reversion and HMM Volatility Stress Risk Overlay in Commodity Futures

## Provenance

- **Primary Source:** Tommaso Zeri, *"Wavelet-Based Signal Extraction and Regime Detection in Commodity Futures: A Rigorous Walk-Forward Study"*, GitHub repository `tommasozeri/Wavelet-strategy-analysis`, commit `6d766d411aeb2820203a329571b3da908f18b5ba`, published September 6, 2026 (`source-reported`).
  - GitHub Repository URL: [https://github.com/tommasozeri/Wavelet-strategy-analysis](https://github.com/tommasozeri/Wavelet-strategy-analysis)
  - Canonical Commit SHA: `6d766d411aeb2820203a329571b3da908f18b5ba`
  - Primary Pipeline Code: [`src`](https://github.com/tommasozeri/Wavelet-strategy-analysis/blob/6d766d411aeb2820203a329571b3da908f18b5ba/src) (53,498-byte standalone Python pipeline)
  - Primary Research Report: [`wavelet_trading_report.pdf`](https://github.com/tommasozeri/Wavelet-strategy-analysis/blob/6d766d411aeb2820203a329571b3da908f18b5ba/wavelet_trading_report.pdf) (17-page LaTeX PDF monograph)
- **Verification Integrity:** Both the complete standalone Python pipeline (`src`) and the full 17-page technical research monograph (`wavelet_trading_report.pdf`) were directly retrieved and audited. Every equation, algorithm step, parameter default, cross-validation table (Tables 1–6), rolling window evaluation, bootstrap confidence interval, and negative finding traces directly to the author's primary code and report text. No secondary search snippets, blog summaries, or model-generated synthetic summaries were used to reconstruct the strategy logic or empirical claims.
- **Repository Deduplication Audit:** A comprehensive audit of all existing records in `alpha-strategy-research` confirmed zero existing records matching `tommasozeri`, `Wavelet-strategy-analysis`, or this CWT+HMM commodity futures architecture. Related records in the repository (`learnable-wavelet-transformer-long-short-equity-wavelsformer-2026-09-03.md`, `crude-oil-crack-spread-seasonally-adjusted-mean-reversion-stop-lockout-2026-09-12.md`, `coffee-commodity-weather-stress-lagged-overlay-2026-09-12.md`) explore distinct frameworks (learnable neural wavelet transforms on equities, cointegrated refinery crack spreads with harmonic deseasonalization, and satellite weather-stress overlays on agricultural futures); none implement continuous Morlet wavelet band-pass reconstruction, Torrence-Compo red-noise significance scaling, or Hidden Markov Model volatility stress overlays on commodity futures.

## Economic mechanism

### Source-reported

1. **Geophysics to Finance Translation and Time-Frequency Decomposition:** The Continuous Wavelet Transform (CWT) using the complex Morlet wavelet decomposes a non-stationary time series across both time and frequency simultaneously. In physical commodity markets (specifically WTI crude oil), inventory accumulation, shipping logistics, refining cycles, and seasonal demand swings have historically been hypothesized to generate quasi-cyclical oscillatory patterns at intermediate frequencies (e.g., 20–60 trading days) rather than instantaneous point mean-reversion (`source-reported`).
2. **Cyclicality vs. Volatility Decoupling (The Core Negative Finding):** Wavelet spectral energy does not equate to mean-reverting cyclicality. Severe market shocks (e.g., the April 2020 COVID-19 demand collapse and negative-price event, or the 2022 Russia/Ukraine conflict) inject massive power across a wide continuum of wavelet scales. Because the CWT is an energy decomposition, a sharp V-shaped price dislocation appears as elevated spectral power even though the event is a single, non-repeating structural trend. Consequently, using elevated wavelet significance to size up mean-reversion bets fails catastrophically: it increases exposure precisely when the market is trending strongly rather than oscillating (`source-reported`).
3. **Latent-State Volatility Concordance:** An independent two-state Gaussian Hidden Markov Model (HMM) fitted on return volatility demonstrates a 0.61 full-sample correlation with causal wavelet power, confirming that elevated spectral energy clusters in high-volatility market regimes rather than stationary cycles (`source-reported`).
4. **Asymmetric Risk Overlay Mechanism:** When HMM-detected stress probability ($P(\text{stressed})$) is used not as a directional trigger, but as a non-directional risk-reduction overlay ($\kappa = 1.0$, scaling exposure by $1 - P(\text{stressed})$), its efficacy diverges sharply across underlying asset structures:
   - *Diversified Mean-Reversion Ensemble:* Improves Sharpe, Calmar, and maximum drawdown simultaneously (Sharpe 0.43 $\to$ 0.61, Calmar 0.17 $\to$ 0.23, Max DD 8.4% $\to$ 4.9%) because a market-neutral or sign-flipping mean-reversion book has no persistent directional drift; reducing exposure during turbulent spikes avoids extreme adverse excursion days without incurring substantial opportunity cost (`source-reported`).
   - *Directional Buy-and-Hold:* Severely degrades risk-adjusted performance (Sharpe 0.24 $\to$ 0.08, Calmar 0.12 $\to$ 0.03) because post-crisis recoveries in commodities typically occur while volatility remains high; de-risking during elevated volatility systematically forfeits the bulk of the subsequent rebound (`source-reported`).

### Research interpretation

The primary thesis is that spectral band-pass filtering alone cannot generate standalone directional alpha in commodity futures due to cone-of-influence endpoint distortion and trend-shock contamination. However, multi-band ensemble aggregation eliminates single-band selection data snooping, and non-directional volatility-regime risk gating provides genuine downside protection for sign-flipping mean-reversion books without impairing structural drift.

## Signal

### Formation timestamp
Signals are evaluated at the close of each daily trading bar ($t$) and executed on the following trading day ($t+1$) with a 1-day execution lag (`pos_lag = np.roll(positions, 1)`) (`source-reported`).

### Lookback
- **CWT Warm-up and Refit Cadence:** Expanding causal window with initial warm-up period of `MIN_HISTORY_DAYS = 504` trading days (~2 years). Recomputed every `REFIT_EVERY_DAYS = 5` trading days, held flat between refits (`source-reported`).
- **Wavelet Basis Specification:** Morlet mother wavelet with non-dimensional frequency parameter $\omega_0 = 6$. Scale resolution $dj = 1/12$ (12 sub-octaves per octave). Smallest scale $s_0 = 2 \cdot dt$ ($dt = 1$ trading day). Spanning $J = \lfloor 7 / dj \rfloor = 84$ total scales (`source-reported`).
- **Band Periods:** Primary band spans 20 to 60 trading days ($s \in [20, 60]$). Multi-band ensemble spans four discrete bands: (5, 20), (10, 30), (20, 60), and (60, 120) trading days (`source-reported`).
- **Causal Endpoint Reconstruction:** At each refit day $i$, the CWT is computed on normalized returns $dat\_norm[:i+1]$. The inverse CWT band-pass filter reconstructs the series over the target band, and only the terminal value at the last observation ($filtered[-1]$) is recorded (`source-reported`).
- **Rolling Z-Score:** Filtered series is normalized by trailing rolling mean and standard deviation over `Z_LOOKBACK = 60` trading days:
  $$z_t = \frac{x'_t - \mu_{60}(x'_t)}{\sigma_{60}(x'_t)}$$
  (`source-reported`).
- **HMM Latent State:** Two-state Gaussian HMM (`HMM_N_STATES = 2`) with diagonal covariance fitted on expanding windows of normalized returns (`HMM_MIN_HISTORY_DAYS = 504`, `HMM_REFIT_EVERY_DAYS = 5`). Stressed state identified as the component with higher diagonal variance $\sigma_k^2$ (`source-reported`).

### Entry
Discretionary mean-reversion rule with hysteresis on rolling z-score:
- Enter short position ($state = -1$) when $z_t > 1.0$ (`Z_ENTRY = 1.0`) (`source-reported`).
- Enter long position ($state = 1$) when $z_t < -1.0$ (`-Z_ENTRY = -1.0`) (`source-reported`).

### Exit
- Exit long position to flat ($state = 0$) when $z_t > -0.2$ (`-Z_EXIT = -0.2`) (`source-reported`).
- Exit short position to flat ($state = 0$) when $z_t < 0.2$ (`Z_EXIT = 0.2`) (`source-reported`).

### Holding period
Variable holding period determined by z-score mean reversion to the $\pm 0.2$ exit band (`source-reported`). Average round trips reported as 45 trades over 3,188 trading days for the primary band, implying an average holding period of ~30 to 45 trading days (`source-reported`).

### Significance weighting & position sizing
1. **Continuous Significance Scaling:** Rather than a binary filter, position size is scaled continuously by the ratio of the band's scale-averaged wavelet power to the Torrence-Compo red-noise significance threshold at 80% confidence (`GATE_SIG_LEVEL = 0.80`), capped at 1.0:
   $$strength_t = \min\left(1.0, \frac{\bar{P}_{\text{band}, t}}{P_{\text{crit}, 0.80, t}}\right)$$
   $$pos_{\text{gated}, t} = pos_{\text{base}, t} \times strength_t$$
   (`source-reported`).
2. **Volatility Targeting:** Sized inversely to 20-day trailing realized volatility to target an annualized volatility of 20% (`VOL_TARGET_ANN = 0.20`, `VOL_LOOKBACK = 20`), lagged by 1 day and capped at a maximum leverage of 2.0x (`MAX_LEVERAGE = 2.0`):
   $$size_t = \min\left(2.0, \frac{0.20}{\sigma_{\text{ann}, 20, t-1}}\right)$$
   $$pos_{\text{sized}, t} = pos_{\text{gated}, t} \times size_t$$
   (`source-reported`).
3. **Four-Band Ensemble:** Equal-weighted linear aggregation across all four frequency bands:
   $$pos_{\text{ens}, t} = \frac{1}{4} \sum_{k=1}^4 pos_{\text{sized}, k, t}$$
   (`source-reported`).
4. **Risk-Reduction Overlay:** De-risking scaling factor applied to strategy exposure based on causal HMM stressed-state probability:
   $$scale_t = 1.0 - \kappa \cdot \min(1.0, \max(0.0, P(\text{stressed})_t))$$
   with reduction factor $\kappa = 1.0$ (`RISK_OVERLAY_REDUCTION = 1.0`) (`source-reported`).

## Required data

- **Instrument:** WTI Crude Oil Futures (`CL=F`) traded on NYMEX, referenced via Yahoo Finance (`source-reported`).
- **Macro Drivers (for coherence and cross-wavelet comparison):** US 10-year Treasury yield (`^TNX`), US Dollar Index (`DX-Y.NYB`), CBOE Volatility Index (`^VIX`), S&P 500 Index (`^GSPC`) (`source-reported`).
- **Venue:** NYMEX / CME Group (`source-reported`).
- **Market type:** Commodity futures, continuous front-month contract (`source-reported`).
- **Timeframe:** Daily bars (`dt = 1.0` trading day) (`source-reported`).
- **Fields:** Adjusted Close price. Transformed into log-returns $\Delta \ln(P_t)$ to guarantee stationarity for pycwt AR(1) estimation (`source-reported`).
- **Point-in-time / Availability Lag:** CWT refit and HMM fitting use expanding causal windows strictly up to day $i$, with terminal observation held flat for 5 days. Next-day execution lag applied (`pos_lag = np.roll(positions, 1)`) (`source-reported`).
- **Missing-data & Outlier Handling:** Settlement prices $\le 0$ (such as the negative settlement on 2020-04-20) are flagged as non-positive contract-mechanic artifacts and forward-filled/back-filled (`close.mask(bad).ffill().bfill()`) (`source-reported`).
- **Funding / Borrow:** Commodity futures margin model; no borrow fee modeled for short positions (`source-reported`).
- **Transaction Costs:** 2 basis points round-trip execution cost modeled per unit of position turnover (`COST_BPS = 2`) (`source-reported`).

## Execution assumptions

- **Signal-to-order timing:** 1-day execution lag. Signal calculated at date $t$ close is applied to date $t+1$ returns (`source-reported`).
- **Order type:** Market on close / open assumed (`source-reported`).
- **Fill model:** Full fill assumed at continuous price index (`source-reported`).
- **Fees & Slippage:** 2 bps round-trip transaction cost deducted from gross returns upon position changes (`trades * 2e-4`) (`source-reported`). Slippage beyond 2 bps is omitted (`data gap`).
- **Leverage:** Max 2.0x leverage cap enforced by volatility-targeting layer (`source-reported`).
- **Overlay Execution Friction:** In the author's reference script, the HMM risk overlay is applied directly to net-of-cost daily returns (`ret_net * scale`), treating continuous rebalancing as friction-free (`source-reported` operational limitation; classified as `research-proposed` area for execution remediation).

## Evidence

### Source-reported

All empirical metrics below are extracted directly from Tommaso Zeri's primary research report (`wavelet_trading_report.pdf`, Sections 7.1–7.7, Tables 1–6) and pipeline code (`src`), evaluated on WTI crude oil futures (`CL=F`) from January 2, 2014 to September 4, 2026 (3,188 trading days, net of 2 bps round-trip transaction cost):

#### 1. Primary Band Strategy vs. Buy-and-Hold Benchmark (Table 1)
| Asset / Strategy | Sharpe Ratio | Annualized Return | Annualized Volatility | Maximum Drawdown |
| :--- | :---: | :---: | :---: | :---: |
| Wavelet Strategy (20–60d) | -0.02 | -0.1% | 4.7% | 19.9% |
| Buy & Hold (`CL=F`) | 0.24 | 11.2% | 47.1% | 90.7% |

*Interpretation:* The single-band directional wavelet strategy shows zero standalone edge in isolation, but reduces volatility to one-tenth and drawdown to one-fourth of buy-and-hold (`source-reported`).

#### 2. Out-of-Sample Band Selection Instability (Table 2)
Single split with training through 2021-05-28 and test on untouched remainder:
| Band Period | Train Sharpe | Test Sharpe | Test Ann. Return | Test Max Drawdown |
| :--- | :---: | :---: | :---: | :---: |
| 5–20 days | 0.18 | 0.74 | 3.7% | 5.8% |
| 10–30 days | -0.07 | 0.85 | 4.8% | 4.8% |
| 20–60 days | -0.43 | 0.49 | 2.5% | 8.8% |
| 60–120 days | 0.40 | 0.13 | 0.6% | 10.8% |

*Instability finding:* The band chosen *ex ante* on training Sharpe (60–120 days) was the *worst* performer out-of-sample (Test Sharpe 0.13, 90% bootstrap CI [-0.42, 0.73] straddling zero). In rolling 9-window annual validation (2016–2024), the *ex-ante* chosen band ranked in the top half of test results in only 4 of 9 windows, statistically indistinguishable from pure luck (`source-reported`).

#### 3. Four-Band Equal-Weight Ensemble (Table 3)
| Strategy | Sharpe Ratio | Annualized Return | Annualized Volatility | Maximum Drawdown | 90% Bootstrap CI | $P(\text{Sharpe} > 0)$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| 4-Band Ensemble | 0.43 | 1.4% | 3.3% | 8.4% | [0.02, 0.83] | 96% |

*Result:* The 4-band ensemble outperformed the *ex-ante* picked single band in 6 of 9 rolling windows (average test Sharpe 0.38 vs. 0.12), and its 90% block-bootstrap confidence interval strictly excluded zero (`source-reported`).

#### 4. Macroeconomic Cross-Wavelet Gating (Table 4)
| Variant / Driver | Sharpe Ratio | Ann. Return | Max Drawdown | Train Sharpe | Test Sharpe |
| :--- | :---: | :---: | :---: | :---: | :---: |
| No gate | 0.13 | 1.7% | 55.9% | -0.61 | 0.99 |
| Self-significance gate | -0.02 | -0.1% | 19.9% | -0.43 | 0.49 |
| USD Index (`DX-Y.NYB`, xwt) | -0.15 | -0.6% | 25.6% | -0.66 | 0.92 |
| US 10Y Yield (`^TNX`, xwt) | -0.34 | -1.9% | 34.5% | -0.63 | 0.91 |
| VIX (`^VIX`, xwt) | -0.10 | -0.5% | 24.9% | -0.53 | 1.04 |
| S&P 500 (`^GSPC`, xwt) | -0.03 | -0.2% | 25.7% | -0.46 | 1.13 |

*Result:* No macroeconomic cross-wavelet driver produced a positive full-sample Sharpe ratio (`source-reported`).

#### 5. Directional HMM Regime Gating Failure (Table 5)
| Gating Variant | Sharpe Ratio | Ann. Return | Max Drawdown | Train Sharpe | Test Sharpe |
| :--- | :---: | :---: | :---: | :---: | :---: |
| No gate | 0.13 | 1.7% | 55.9% | -0.61 | 0.99 |
| Wavelet self-sig. gate | -0.02 | -0.1% | 19.9% | -0.43 | 0.49 |
| HMM regime gate only | -0.26 | -1.8% | 36.8% | -0.53 | 0.32 |
| HMM $\times$ wavelet gate | -0.17 | -0.6% | 16.6% | -0.44 | 0.26 |

*Result:* Using HMM stress directionally to size up mean-reversion trades consistently degrades Sharpe into deep negative territory (`source-reported`).

#### 6. Non-Directional Risk Overlay Performance ($\kappa = 1.0$, Table 6)
| Base Exposure | Overlay Signal | Sharpe Ratio | Ann. Return | Max Drawdown | Calmar Ratio |
| :--- | :--- | :---: | :---: | :---: | :---: |
| Buy & Hold | None | 0.24 | 11.2% | 90.7% | 0.12 |
| Buy & Hold | Wavelet strength | 0.03 | 0.9% | 72.8% | 0.01 |
| Buy & Hold | HMM stress | 0.08 | 2.3% | 75.9% | 0.03 |
| Ensemble (4-band) | None | 0.43 | 1.4% | 8.4% | 0.17 |
| Ensemble (4-band) | Wavelet strength | 0.70 | 1.2% | 5.8% | 0.21 |
| Ensemble (4-band) | HMM stress | 0.61 | 1.1% | 4.9% | 0.23 |

*Result:* The HMM stress overlay reduces maximum drawdown in 8 of 9 rolling annual windows on the ensemble, increasing Calmar from 0.17 to 0.23. On buy-and-hold, the same overlay degrades Calmar from 0.12 to 0.03 (`source-reported`).

### Independently reproduced

Not independently reproduced. All figures and empirical tables reflect direct extraction from Tommaso Zeri's primary repository codebase (`tommasozeri/Wavelet-strategy-analysis`, commit `6d766d411aeb2820203a329571b3da908f18b5ba`).

### Negative evidence

- **Directional Wavelet Alpha Failure:** Standalone continuous wavelet band-pass mean-reversion produces zero statistically significant alpha on WTI crude oil (Sharpe -0.02, bootstrap CI straddles zero). The hypothesis that physical commodity cycles yield direct directional predictability is falsified (`source-reported`).
- **Data Snooping in Band Selection:** Single train-period band selection suffers from severe parameter instability; the *ex-ante* optimal band consistently underperformed out-of-sample (`source-reported`).
- **Directional Volatility Gating Penalty:** Increasing mean-reversion position size during elevated wavelet strength or HMM stress produces severe negative Sharpe (-0.17 to -0.26) due to non-cyclical trend contamination during macro shocks (`source-reported`).
- **Macro Coherence Inefficacy:** None of the four macro cross-wavelet drivers (USD, 10Y yield, VIX, S&P 500) generated positive full-sample alpha (`source-reported`).
- **Asymmetric Degradation on Directional Exposures:** Risk-reduction overlays applied to buy-and-hold destroy risk-adjusted returns by forfeiting post-crisis recovery rallies (`source-reported`).

## Falsification plan

1. **Multi-Commodity Robustness Audit:** Replicate the 4-band ensemble + HMM stress risk overlay across four adjacent commodity futures: Brent Crude (`BZ=F`), Natural Gas (`NG=F`), Gold (`GC=F`), and Copper (`HG=F`). If the net Sharpe ratio fails to exceed 0.20 net of 5 bps transaction costs across at least 3 of 4 markets, falsify the framework as WTI-specific overfitting (`research-defined falsification threshold`).
2. **Pre-Trade Execution Friction Test:** Re-implement the HMM risk overlay directly inside the pre-trade position-sizing module (`size_by_volatility`) so that continuous rebalancing incurs modeled bid-ask spread and turnover costs. If transaction costs reduce the ensemble + HMM overlay Calmar ratio below 0.15, falsify the risk overlay as an artifact of frictionless cash-flow scaling (`research-defined falsification threshold`).
3. **Calm Regime Ablation:** Exclude the extreme volatility shock years (2020 COVID shock and 2022 Russia/Ukraine conflict). If the 4-band ensemble Sharpe in the quiet 2016–2019 regime drops below 0.10, falsify the thesis that spectral band-pass filters capture steady-state cyclicality rather than non-linear tail avoidance (`research-defined falsification threshold`).
4. **Band-Count Ablation:** Remove any two of the four frequency bands. If the ensemble Sharpe drops by more than 50% or maximum drawdown doubles, falsify the ensemble as fragile multi-collinear curve fitting (`research-defined falsification threshold`).

## Crypto portability

adapted

The economic mechanism and statistical toolkit port to crypto assets with substantial structural modifications:
- **Portability Classification:** `adapted` (`unproven` in production crypto environments).
- **Continuous 24/7 Session Structure:** Commodity futures observe daily settlement closes; crypto perpetual markets operate 24/7/365 without weekends. Daily bar aggregation must be fixed to a standard UTC boundary (e.g., 00:00 UTC) to prevent artificial phase shift in CWT convolutions (`research interpretation`).
- **Liquidation Cascades & Trending Displacement:** Crypto markets exhibit frequent cascading liquidations and momentum trends that severely exacerbate the "cyclicality vs. volatility" failure mode. Directional wavelet mean-reversion without tight structural stops is hazardous in crypto (`research interpretation`).
- **HMM Volatility Regime Portability:** The two-state HMM volatility classifier ports directly to crypto daily log-returns (e.g., BTC and ETH perpetuals). The negative correlation between volatility and directional post-rebound gains is even stronger in crypto, suggesting that HMM de-risking will similarly harm buy-and-hold crypto while potentially protecting delta-neutral basis or statistical arbitrage ensembles (`research interpretation`).
- **Funding Rate Friction:** Perpetual futures incur 8-hour funding rates. Holding short or long mean-reversion positions across multi-week periods requires factoring cumulative funding cash flows into net returns (`research interpretation`).

## Limitations

- **Low Absolute Return:** While the 4-band ensemble achieves a 0.43 Sharpe (0.61 with HMM overlay) and low maximum drawdown (4.9%), its annualized net return is only 1.1% to 1.4% at 1x leverage, requiring modest operational leverage for meaningful capital deployment (`source-reported`).
- **Cone-of-Influence Distortion:** Boundary effects at the edges of the CWT cone of influence unavoidably degrade the signal-to-noise ratio of real-time causal filter endpoints (`source-reported`).
- **Overlay Friction Gap:** The primary pipeline scales post-cost daily returns directly rather than modeling execution turnover at the order level (`source-reported`).
- **Single-Asset Empirical Sample:** Evaluated primarily on WTI crude oil futures; cross-commodity generalizability is not formally demonstrated in the primary report (`source-reported`).
- **Not Independently Reproduced:** No independent reproduction in our internal research stack has been performed.

## Implementation status

not-implemented

This record serves strictly as a normalized research capture. No implementation of the CWT pipeline, Morlet filter, rolling z-score mean reversion, or HMM stress overlay exists in `nautilus-quant-system`, PyBroker, or NautilusTrader.

## Adoption boundary

research-only

This strategy capture represents third-party quantitative research and empirical falsification analysis. Its presence in this repository does not constitute:
- Validated or profitable alpha
- Approval for strategy implementation
- Approval for paper trading, testnet, or live deployment

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]`
- `[[crude-oil-crack-spread-seasonally-adjusted-mean-reversion-stop-lockout-2026-09-12]]`
- `[[coffee-commodity-weather-stress-lagged-overlay-2026-09-12]]`
- `[[learnable-wavelet-transformer-long-short-equity-wavelsformer-2026-09-03]]`

## Sources

1. Tommaso Zeri. *"Wavelet-Based Signal Extraction and Regime Detection in Commodity Futures: A Rigorous Walk-Forward Study."* GitHub repository `tommasozeri/Wavelet-strategy-analysis`, commit `6d766d411aeb2820203a329571b3da908f18b5ba`, published September 6, 2026.
   - Public Repository: [https://github.com/tommasozeri/Wavelet-strategy-analysis](https://github.com/tommasozeri/Wavelet-strategy-analysis)
   - Pipeline Implementation: [`src`](https://github.com/tommasozeri/Wavelet-strategy-analysis/blob/6d766d411aeb2820203a329571b3da908f18b5ba/src)
   - Full Research Report: [`wavelet_trading_report.pdf`](https://github.com/tommasozeri/Wavelet-strategy-analysis/blob/6d766d411aeb2820203a329571b3da908f18b5ba/wavelet_trading_report.pdf)
