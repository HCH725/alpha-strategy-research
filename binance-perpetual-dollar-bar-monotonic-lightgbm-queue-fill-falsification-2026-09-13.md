---
schema: strategy-research-record-v1
title: "Binance USDⓈ-M Perpetual Dollar-Bar Monotonic LightGBM Alpha: Triple-Barrier Labeling, Queue-Aware Maker Fill Collapse, and 0-for-20 Production Gate Falsification"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - machine-learning
  - lightgbm
  - dollar-bars
  - triple-barrier
  - cpcv
  - order-queue-simulation
  - falsification
status: research-only
confidence: high
source_as_of: 2026-09-07
sources:
  - "FelipeCJBoB, 'multi-asset-crypto-alpha-engine', GitHub repository, commit c1b27296abd15cf86100d8127a849a7ac3b81e9d (September 7, 2026), https://github.com/FelipeCJBoB/multi-asset-crypto-alpha-engine"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Binance USDⓈ-M Perpetual Dollar-Bar Monotonic LightGBM Alpha: Triple-Barrier Labeling, Queue-Aware Maker Fill Collapse, and 0-for-20 Production Gate Falsification

## Provenance

- **Primary Source:** Felipe (`FelipeCJBoB`), *"multi-asset-crypto-alpha-engine"*, GitHub repository: `https://github.com/FelipeCJBoB/multi-asset-crypto-alpha-engine`.
- **Immutable Commit SHA:** `c1b27296abd15cf86100d8127a849a7ac3b81e9d` (committed 2026-09-07 00:37:12 UTC).
- **Exact Primary Source Paths:**
  - `docs/ADR-007_medicao_producao_hiperparametro_optuna_15_combos_2026-08-30.md`
  - `docs/ADR-008_auditoria_ml_alpha_institucional_score_quality_walkforward_2026-08-31.md`
  - `docs/SPRINT_LOG.md`
  - `src/execution/fill_simulator.py`
  - `src/features/registry.yaml`
  - `src/data/build_dollar_bars.py`
  - `config/constants.yaml`
  - `audit/n_lifetime.yaml`
- **Data Scope & Universe:** Binance USDⓈ-M perpetual futures covering 5 major contracts: `BTCUSDT`, `ETHUSDT`, `BNBUSDT`, `SOLUSDT`, and `XRPUSDT`. Public S3 tick and kline archives from 2019-12-31 to 2026-08-07 (~6.5 years, 231,552 15-minute equivalent bars, 462,682 triple-barrier labels across both sides). Order queue simulation utilizes raw `bookTicker` (top-of-book tick) and `aggTrades` across the uncorrupted pre-RPI window from 2023-05-16 to 2024-03-30 (60,650 simulated orders).
- **Repository Deduplication:** Audited all existing `.md` records in `alpha-strategy-research`. Zero prior records cite `FelipeCJBoB`, `multi-asset-crypto-alpha-engine`, or this production codebase. Adjacent machine-learning records (`binance-spot-candle-ml-extrema-timing-falsification-2026-09-04.md`, `china-ashare-xgboost-treeshap-behavioral-factor-decomposition-2026-09-04.md`, `crypto-perpetual-volume-spike-momentum-liquidity-inversion-2026-09-13.md`) investigate different markets (spot vs perpetual, A-shares) or single heuristic indicators; none evaluate an institutional dollar-bar LightGBM engine with triple-barrier labeling, queue-position-aware fill simulation, Combinatorial Purged Cross-Validation (CPCV), and Benjamini-Hochberg FDR-corrected multi-gate audit.

## Economic mechanism

### Source-reported

The author hypothesizes that financial markets generate event-driven information clusters that clock-time bars dilute. Resampling trade flows into dollar-value volume bars (dollar bars) normalizes information arrival and restores statistical properties (sub-Gaussian return distributions). By computing technical, volatility, funding rate, and open interest features on dollar bars, applying triple-barrier labeling to separate genuine directional continuation from adverse excursion, and training gradient-boosted decision trees (LightGBM) with monotonic constraints (forcing economic consistency such that higher momentum cannot predict lower expected return), an agent should capture short-to-intermediate directional momentum and carry harvesting in crypto perpetuals. Passive maker execution at the top of the order book is intended to capture the bid-ask spread and avoid the 5 bps taker fee barrier.

### Research interpretation

The hypothesis is that directional price predictability exists in dollar-bar features and can be extracted by regularized machine learning, with passive limit orders neutralizing execution drag. However, the empirical results provide an exemplary, rigorous falsification of this premise:
1. **Execution Reality vs Paper Fills:** Passive maker execution suffers an acute fill rate deficit. While theoretical backtests assume a >60% to 90%+ fill rate when limit prices are touched, real queue reconstruction reveals a fill rate of only 37.3%.
2. **Gross Signal vs Friction Domination:** While gross directional momentum (+1.60 bps) and carry (+2.07 bps) exhibit modest statistical positivity, execution costs (-17.71 bps) completely dominate the payoff, forcing net Sharpe to -0.81 (Layer 1) and -1.18 (Layer 0), underperforming simple Buy & Hold (+0.54).
3. **Out-of-Sample Alpha Absence (0-for-20 Gate Failure):** Out-of-sample AUC across folds collapses to ~0.50 (no discriminative ability). Fold-to-fold IC dispersion is several times larger than the mean IC, single-seed optimization introduces massive selection bias (up to +8.356 Sharpe), and 0 of 20 asset-layer-side combinations pass institutional production gates.

## Signal

### Formation timestamp

Evaluated at the close of each dollar bar (event-driven, variable clock timestamp). Decisions are formed causally; in walk-forward evaluation, an embargo period (measured at 43.75 hours / 175 15-minute equivalent bars) is applied between training and out-of-sample test splits to eliminate serial contamination.

### Lookback windows

- **Dollar Bar Calibrations (source-reported):** 3 resolutions calibrated against target clock-time frequencies:
  - Resolution `R1`: calibrated to ~15-minute average duration.
  - Resolution `R2`: calibrated to ~30-minute average duration.
  - Resolution `R3`: calibrated to ~1-hour average duration.
- **Feature Lookback Windows (source-reported):**
  - Short-term momentum: 1, 2, 4, and 12 dollar bars (`A01`–`A04` log returns; `A05` volatility-normalized return over 4 bars; `A06` over 12 bars).
  - Trend distance: 48-bar Exponential Moving Average (EMA48) normalized by ATR (`A13_dist_ema48_atr`).
  - Relative Strength Index: 14-bar RSI (`B01_rsi_14`) and 48-bar RSI (`B02_rsi_48`).
  - Volatility metrics: 20-bar ATR (`C01`), 48-bar Parkinson volatility (`C04_parkinson_vol_48`), and 48-bar Garman-Klass volatility (`C05_garman_klass_48`).
  - Imbalance & microstructure: 48-bar taker volume imbalance z-score (`D06f_taker_imbalance_z_48`).
  - External derivatives state: expanding funding rate z-score (`E02f_funding_z_expanding`) and 48-bar open interest change z-score (`E10f_oi_change_z_48`).

### Entry rules (source-reported)

1. **Model Prediction:** Two independent binary LightGBM classifiers are fitted per asset and resolution: one for the long side, one for the short side.
2. **Probability Threshold ($\tau$):** Long entry triggers when calibrated probability $P(\text{long}) \ge \tau_{\text{long}}$; short entry triggers when $P(\text{short}) \ge \tau_{\text{short}}$. The threshold $\tau$ is calibrated in-fold to target an annualized signal rate (nominal 1.89%, corresponding to ~2.58 trades/day per backtest path).
3. **Monotonic Constraints (Layer 1 vs Layer 0):** In Layer 1 (`Camada 1`), features have sign constraints enforced during tree splitting (e.g. non-decreasing with momentum, non-increasing with cost-to-ATR ratio). Layer 0 (`Camada 0`) trains unconstrained trees.
4. **Order Placement:** Passive limit order posted at the best bid (for long) or best ask (for short) observed at bar close timestamp.

### Exit rules (source-reported)

Triple-barrier exit logic evaluated on 1-minute mark price series:
1. **Take-Profit (TP):** Price reaches entry $\pm 1.5 \times \text{ATR}_{20}$ (symmetrical geometry calibrated in sweep S1; revised from legacy $2.0 \times \text{ATR}$).
2. **Stop-Loss (SL):** Price reaches entry $\mp 1.5 \times \text{ATR}_{20}$.
3. **Time Stop (TIME):** Position is closed at market if neither barrier is touched within 32 bars (~8 hours at 15m equivalent, matching funding settlement cadence).

### Parameters

- Base asset universe: `[BTCUSDT, ETHUSDT, BNBUSDT, SOLUSDT, XRPUSDT]` (source-reported).
- Label geometry: $\text{tp\_atr\_mult} = 1.5$, $\text{sl\_atr\_mult} = 1.5$, $\text{time\_stop\_bars} = 32$ (source-reported).
- Maker fee: $0.0002$ ($2.0 \text{ bps}$); taker fee: $0.0005$ ($5.0 \text{ bps}$) (Binance VIP 0 schedule, source-reported).
- Round-trip maker cost reference: $0.4942 \text{ probability-weighted}$ or $5.5173 \text{ bps}$ total (source-reported, remeasured on 15 dollar-bar combinations).
- Minimum trades per fold: $\text{MIN\_OCCURRENCES\_ABOVE\_TAU} = 10$ (source-reported).
- Operational risk limits: maximum capital reference $\text{R\$ } 1,000$ (~USD 196.85 at $5.08 \text{ USD/BRL}$); maximum aggregate cross-asset risk limit $1.0\%$ (`aggregate_risk_max`, research-proposed).

### Position sizing (source-reported)

Quantized position sizing calculated via lot size filter (`step_size = 0.001` for BTC) using `Decimal` floor-to-step quantization. Maximum position risk capped at $0.50\%$ of equity per trade. Sizing does not use dynamic Kelly scaling or volatility rebalancing.

## Required data

- **Instruments:** Binance USDⓈ-M Perpetual Contracts (`BTCUSDT`, `ETHUSDT`, `BNBUSDT`, `SOLUSDT`, `XRPUSDT`).
- **Venue:** Binance Futures (USDⓈ-Margined).
- **Timeframe / Sampling:** Raw trade-by-trade ticks (`aggTrades`) aggregated into event-driven dollar bars ($V_{\text{threshold}}$). Mark price klines (1-minute interval) for causal barrier touch resolution.
- **Fields:** OHLCV dollar bars, taker buy volume, 8-hour funding settlement rates (`fundingRate`), premium index (`premiumIndexKlines`), open interest metrics (`sum_open_interest`), and level-1 top-of-book quotes (`bookTicker`: `bestBidPrice`, `bestBidQty`, `bestAskPrice`, `bestAskQty`).
- **Point-in-Time Integrity:** All archives sourced from Binance public dump manifests. Strict causal order enforced; open interest null spikes (`sum_open_interest == 0.0`, 31 historical points) masked to null to avoid $\log(0)$ poisoning in feature $E10f$.
- **Timestamps:** UTC epoch milliseconds. Monotonicity strictly verified; bars resampled strictly using causal right-closed intervals.

## Execution assumptions

- **Order Type:** Passive limit order posted at the top-of-book (best bid/ask) at signal formation time.
- **Queue Fill Model:** Strict first-in-first-out (FIFO) queue priority without cancellation modeled. In `fill_simulator.py`, the order joins the tail of existing depth at the touch price; fill occurs only when subsequent aggressor volume (`aggTrades`) exceeds the prior queue size. Fills evaluated exclusively on pre-RPI historical data (2023-05-16 to 2024-03-30).
- **Fill Rate:** Empirically measured at **37.3%** across 60,650 simulated orders (buy 36.7% / sell 37.9%), creating an acute execution bottleneck relative to the 60% break-even floor.
- **Adverse Selection Markout:** Mid-price slippage at 1m, 5m, and 30m post-fill measured at **-0.586 bps**, **-0.643 bps**, and **-0.590 bps**.
- **Execution Cost Drag:** Round-trip maker fees + adverse selection + barrier touch drag total **-17.71 bps** per round trip across the 6.5-year history.
- **Capital & Leverage:** 1x to 2x nominal leverage bounded by the $1.0\%$ aggregate portfolio risk constraint.

## Evidence

### Source-reported

All empirical metrics below are directly reported by Felipe (`FelipeCJBoB`) in `ADR-007`, `ADR-008`, `SPRINT_LOG.md`, and `audit/n_lifetime.yaml`:

1. **6.5-Year Pooled CPCV Backtest (Sprint 8, 30,623 trades across 5 paths):**
   - Naive Sharpe ratio: **-0.81** (Layer 1 with monotonic constraints) vs **-1.18** (Layer 0 unconstrained). Both are negative.
   - Benchmark Buy & Hold Sharpe: **+0.54** (drastically outperforms both ML variants).
   - Return decomposition (bps per trade):
     - Directional price return: **+1.60 bps**
     - Carry harvesting: **+2.07 bps**
     - Execution cost drag: **-17.71 bps**
     - Total net return: **-14.03 bps**
   - Directional gross Sharpe (without execution drag): **+0.194**.
2. **L2 Order Queue Simulation (Sprint 9, 60,650 orders):**
   - Maker fill probability: **37.3%** (36.7% buy / 37.9% sell). PRD §9.6 explicitly notes that below a 60% fill rate, "the economics of the maker design evaporate."
   - Unconditional adverse selection markouts: 1m = **-0.586 bps**, 5m = **-0.643 bps**, 30m = **-0.590 bps**.
   - Selectivity bias: $P(\text{TP} \mid \text{filled}) = 36.6\%$ vs $P(\text{TP} \mid \text{unfilled}) = 38.3\%$ (gap = -1.72 pp, expected value cost = -1.12 bps).
3. **Optuna Hyperparameter Campaign & Confirmation (ADR-007):**
   - Expanded search (Item 1): 1,800 trials over 6 promising combinations. Screening anomaly: `SOLUSDT/R2` showed extreme apparent in-sample values (best value 22.22 / 8.96 vs p95 of 0.82).
   - Deep multi-seed confirmation (Item 2, 720 confirmations, top-6 candidates across 10 seeds [101..1010]): **0 of 6 combinations pass the double gate**.
     - `BTCUSDT/R3`: median $n_{\text{better}}$ collapsed to 2.5 (ranging from 1 to 5 depending solely on random seed).
     - `SOLUSDT/R2`: confirmed as pure screening noise with a project-record selection bias of **+8.356**.
     - `SOLUSDT/R3`: median $n_{\text{better}} = 3.0$, net edge +27.08 bps, selection bias +0.185.
     - `XRPUSDT/R2`: median $n_{\text{better}} = 2.0$.
     - `XRPUSDT/R3`: median $n_{\text{better}} = 2.5$.
   - Noise calibration test (Item 3, 300 retrains under scrambled noise): False positive rate (FPR) of the double gate under pure noise: `BTCUSDT/R3` = **8.0%**, `ETHUSDT/R1` = **0.0%**, `BNBUSDT/R1` = **0.0%** (all well below the 20% tolerance ceiling, proving that 0-of-6 passing in Item 2 is genuine signal absence, not a broken testing instrument).
4. **Institutional Production Multi-Gate Audit (ADR-008):**
   - Across 20 combinations (5 symbols × 2 layers × 2 sides), exactly **0 of 20 combinations pass all 3 production gates simultaneously** (Data gate: $\ge 10$ usable OOS folds; Model gate: one-sample t-test on out-of-time AUC $>0.5$ at $p < 0.05$; Alpha gate: positive net edge).
   - Out-of-time ROC-AUC clusters tightly at **0.497 to 0.503** (standard error of AUC per fold under $H_0=0.5$ is 0.13 to 0.19 via Hanley-McNeil 1982; individual folds frequently exhibit AUC of exactly 0.500).
   - Information Coefficient (IC) dispersion: fold-to-fold standard deviation massively exceeds the mean IC (e.g. `BTCUSDT/R2` long has mean IC = +0.035 with std = 0.512).
   - Feature attribution divergence: concordance between native LightGBM split gain and SHAP values ranges from **0.00 to 1.00** across combinations; on `XRPUSDT/R3` Layer 1 long, concordance is **0.00** (native gain and SHAP identify completely disjoint #1 features).
5. **Asset-Level & Resolution Disaggregation:**
   - `BNBUSDT`: Gross edge negative across all 3 resolutions (-5.37 bps in R1, -4.63 bps in R2, -6.52 bps in R3; win rates cluster at 50.21%–50.45%).
   - `ETHUSDT`: Gross edge negative across all 3 resolutions (average -6.98 bps).
   - Resolution `R1` (fastest dollar bars, ~15m): Mean gross edge is **-4.27 bps** across all 5 assets (compared to +5.27 bps for R2 and +3.39 bps for R3).
6. **Barrier Geometry & Variance Ratio (AG-466):**
   - Widening barrier multiplier to $m=4$ (128 bars) increased TP rate to ~50.8% and reduced cost drag inversely with asset ATR, but paired t-statistic failed: paired gain $t = 0.624$ (mean difference +5.05 bps), absolute edge $t = 0.915$ (mean net return +6.74 bps).
   - Across 37 valid folds, the standard deviation of return between folds was 44.79 bps, meaning the minimum detectable effect at $t=2.0$ is +14.73 bps. Detecting a +6.74 bps edge would require 177 folds (~5x available history).

### Independently reproduced

Not independently reproduced. All figures, parameters, and tables represent verified third-party empirical findings from commit `c1b27296abd15cf86100d8127a849a7ac3b81e9d` of the public repository.

### Negative evidence

- **Pervasive Friction Invalidation:** Across 6.5 years and 30,623 trades, execution drag (-17.71 bps) overwhelms directional alpha (+1.60 bps) and carry (+2.07 bps).
- **Zero-Gate Survival Rate:** In formal walk-forward evaluation across 5 assets, 2 model architectures, and both trade directions, 0 of 20 setups survive production acceptance criteria.
- **Random Seed Instability:** Top Optuna candidates fluctuate from 1 to 5 wins out of 5 splits simply by altering the random seed of the gradient boosting learner.
- **RPI Liquidity Invisibility:** Following the introduction of Binance Retail Price Improvement (RPI) orders on 2025-11-20, public level-2 books no longer reflect non-algorithmic liquidity, making historical limit fill simulation invalid on contemporary order flow.
- **Dollar Threshold Drift:** Between 2020 and 2024, fixed dollar-bar thresholds experienced an 18.18x volume expansion on BTCUSDT, rendering static bar definitions non-stationary across market regimes.

## Falsification plan

1. **Maker Fill Rate Hurdle (research-defined falsification threshold):** Deploy a testnet or micro-capital execution canary measuring actual passive limit order fill rates over $\ge 500$ orders. If realized fill rate falls below **50.0%** (source-reported baseline is 37.3%), reject passive maker capture and mark execution unviable.
2. **Out-of-Time AUC Significance (research-defined falsification threshold):** On an independent forward window of $\ge 20$ non-overlapping dollar-bar folds, evaluate one-sample t-test of out-of-time ROC-AUC against $H_0: \text{AUC} \le 0.50$. Falsification triggers if $p \ge 0.05$ or mean $\text{AUC} \le 0.51$.
3. **Execution Drag vs Gross Edge Breakeven (research-defined falsification threshold):** In backtest or live paper trading, if total execution friction (maker fees + adverse selection markout + barrier execution gap) exceeds gross alpha ($\text{gross return} + \text{carry}$), reject the model family immediately.
4. **Multi-Seed Stability Audit (research-defined falsification threshold):** Re-train the LightGBM classifier across 10 random seeds on the same dataset. If the inter-seed standard deviation of out-of-sample Sharpe exceeds **0.30**, or if the median $n_{\text{better}}$ falls below 4/5, reject the candidate as an optimization artifact.
5. **Feature Attribution Concordance (research-defined falsification threshold):** Compute top-5 feature attribution by native tree split gain and by SHAP TreeExplainer. If the top-1 feature disagrees or if Spearman rank correlation between gain and SHAP importance is $< 0.50$, reject the model due to structural feature instability.

## Crypto portability

**Direct.** The research was conducted natively on Binance USDⓈ-M perpetual futures contracts.

Crypto-specific structural factors identified by the source:
- **RPI Microstructure Break:** On 2025-11-20, Binance introduced Retail Price Improvement (RPI) orders, which route against retail takers off-book and do not appear in public `bookTicker` or depth snapshots, permanently altering top-of-book execution dynamics.
- **Funding & Open Interest Integration:** The feature registry directly includes 8-hour funding rates ($E01f$, $E02f$) and open interest contracts ($E09f$, $E10f$). Funding rate carry contributed +2.07 bps to gross performance.
- **24/7 Continuous Trading:** Eliminates overnight equity gaps, but introduces continuous regime shifts across Asian, European, and US sessions (modeled via sinusoidal diurnal features $K01$ and session dummies $K04$).
- **Extreme Dollar Volume Drift:** Dollar-bar volume thresholds must be dynamically recalibrated; static thresholds suffer up to 18x volume expansion across crypto market cycles.

## Limitations

- **Not Independently Reproduced:** Relies entirely on the reported code and experimental run logs of `FelipeCJBoB/multi-asset-crypto-alpha-engine`.
- **Pre-RPI Order Queue Restriction:** The 37.3% queue fill rate was measured on pre-November 2025 data (320 daily bookTicker files). Contemporary post-RPI fill rates may be higher or lower depending on retail internalized flow.
- **Negative Empirical Performance:** The strategy is an explicit negative result; neither unconstrained nor monotonic LightGBM models achieve positive net returns after realistic costs.
- **High Fold Return Dispersions:** Fold-to-fold return standard deviations (13.6 to 77.5 bps) dwarf the estimated effect size (+6.74 bps), requiring sample sizes (~177 folds) that exceed available crypto historical data.

## Implementation status

`not-implemented`. This record is an analytical research capture and falsification review. No implementation in PyBroker, NautilusTrader, or live production has been performed.

## Adoption boundary

`research-only`. This strategy is strictly **not approved** for paper trading, testnet deployment, or live capital allocation. The primary source unequivocally establishes that the strategy fails out-of-sample validation and is consumed by execution friction.

## Related Wiki records

- `[[binance-perpetual-order-flow-imbalance-horizon-decay-queue-imbalance-falsification-2026-09-13]]` (Queue dynamics and order flow imbalance on Binance perpetuals)
- `[[binance-spot-candle-ml-extrema-timing-falsification-2026-09-04]]` (Machine learning timing falsification on Binance spot)
- `[[duration-aware-bocpd-lognormal-order-flow-regime-2026-09-11]]` (Microstructure regime switching in order flow)
- `[[tether-pairs-trading-fdr-kalman-half-life-net-beta-2026-09-12]]` (Benjamini-Hochberg FDR control in crypto factor discovery)

## Sources

1. Felipe (`FelipeCJBoB`), *"multi-asset-crypto-alpha-engine"*, GitHub repository, commit `c1b27296abd15cf86100d8127a849a7ac3b81e9d` (September 7, 2026). URL: `https://github.com/FelipeCJBoB/multi-asset-crypto-alpha-engine`.
2. `docs/ADR-007_medicao_producao_hiperparametro_optuna_15_combos_2026-08-30.md`, *multi-asset-crypto-alpha-engine* (Optuna 1,800-trial expanded search, 720 multi-seed confirmations, and noise FPR calibration).
3. `docs/ADR-008_auditoria_ml_alpha_institucional_score_quality_walkforward_2026-08-31.md`, *multi-asset-crypto-alpha-engine* (Institutional ML/Alpha audit, out-of-time AUC Hanley-McNeil test, walk-forward fold degenerate rates, SHAP vs gain concordance, and 0/20 multi-gate failure).
4. `docs/SPRINT_LOG.md`, *multi-asset-crypto-alpha-engine* (Sprints 0–12 run summaries, 6.5-year return decomposition [+1.60 bps direction, +2.07 bps carry, -17.71 bps execution], and 60,650-order queue simulation [37.3% fill rate]).
5. `src/execution/fill_simulator.py`, *multi-asset-crypto-alpha-engine* (FIFO queue position reconstruction using `bookTicker` and `aggTrades`, pre-RPI validity boundary 2025-11-20).
