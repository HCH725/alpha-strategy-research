---
schema: strategy-research-record-v1
title: "S&P 500 Statistical Arbitrage with Johansen Basket Cointegration, 4-Way Ornstein-Uhlenbeck Ablation, and Family-Wise Multiple-Testing Deflation"
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
  - ornstein-uhlenbeck
  - kalman-filter
  - regime-switching-hmm
  - multiple-testing
  - hansen-spa
  - white-reality-check
status: research-only
confidence: high
source_as_of: 2026-04-20
sources:
  - "https://github.com/pdwi2020/p4_stat_arb/tree/3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# S&P 500 Statistical Arbitrage with Johansen Basket Cointegration, 4-Way Ornstein-Uhlenbeck Ablation, and Family-Wise Multiple-Testing Deflation

## Provenance

- **Primary Source:** `pdwi2020`, *"P4 — S&P 500 Statistical Arbitrage (Johansen · Kalman-OU · Regime-Switch · Hansen SPA)"*, public quantitative research repository `pdwi2020/p4_stat_arb`, committed April 20, 2026 (`source-reported`).
- **Repository URL:** [https://github.com/pdwi2020/p4_stat_arb](https://github.com/pdwi2020/p4_stat_arb)
- **Immutable Commit SHA:** `3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b`
- **Key Code & Specification Paths Audited:**
  - Configuration & Parameters: [`configs/p4_config.yaml`](https://github.com/pdwi2020/p4_stat_arb/blob/3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b/configs/p4_config.yaml)
  - End-to-End Pipeline & Walk-Forward Driver: [`src/p4/pipeline.py`](https://github.com/pdwi2020/p4_stat_arb/blob/3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b/src/p4/pipeline.py)
  - Johansen Multivariate Cointegration & Basket Extraction: [`src/p4/johansen.py`](https://github.com/pdwi2020/p4_stat_arb/blob/3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b/src/p4/johansen.py)
  - Static Ornstein-Uhlenbeck Parameter Estimator: [`src/p4/ou_estimator.py`](https://github.com/pdwi2020/p4_stat_arb/blob/3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b/src/p4/ou_estimator.py)
  - Kalman Filter Time-Varying OU Tracker: [`src/p4/kalman_ou.py`](https://github.com/pdwi2020/p4_stat_arb/blob/3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b/src/p4/kalman_ou.py)
  - 2-State Gaussian HMM Regime-Switching Estimator & Signal: [`src/p4/regime_switch.py`](https://github.com/pdwi2020/p4_stat_arb/blob/3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b/src/p4/regime_switch.py)
  - Neural Autoencoder & Sequence OU Estimator: [`src/p4/neural_ou.py`](https://github.com/pdwi2020/p4_stat_arb/blob/3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b/src/p4/neural_ou.py)
  - Multiple-Testing Corrections (Bonferroni, BH, BY, Storey, Hansen SPA, White RC): [`src/p4/multiple_testing.py`](https://github.com/pdwi2020/p4_stat_arb/blob/3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b/src/p4/multiple_testing.py)
  - Event-Loop Backtest Engine & Friction Accounting: [`src/p4/backtest.py`](https://github.com/pdwi2020/p4_stat_arb/blob/3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b/src/p4/backtest.py)
  - Portfolio Capacity Scaling & ADV Clipping: [`src/p4/capacity.py`](https://github.com/pdwi2020/p4_stat_arb/blob/3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b/src/p4/capacity.py)
  - S&P 500 4-Way Ablation Benchmark Runner: [`src/p4/run_sp500_ablation.py`](https://github.com/pdwi2020/p4_stat_arb/blob/3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b/src/p4/run_sp500_ablation.py)
  - PCA Eigenportfolio Implementation: [`src/p4/eigenportfolio.py`](https://github.com/pdwi2020/p4_stat_arb/blob/3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b/src/p4/eigenportfolio.py)
  - Comprehensive Empirical Research Memo: [`memo.md`](https://github.com/pdwi2020/p4_stat_arb/blob/3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b/memo.md)
- **License:** MIT License (`source-reported`).
- **Primary Source Verification:** All code paths, configuration dataclasses, empirical ablation logs, and statistical methodologies in commit `3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b` were directly retrieved, inspected, and audited. No secondary search snippets, AI summaries, or marketing claims were used to generate strategy rules or empirical figures.
- **Repository Deduplication Audit:** A full audit of all existing strategy records in `alpha-strategy-research` confirmed zero matching records for `pdwi2020`, `p4_stat_arb`, or this unified 4-way OU ablation and multiple-testing deflation system. Related cointegration records in the repository (`dynamic-johansen-deep-weighted-ensemble-cryptocurrency-pairs-2026-09-05.md`, `crude-oil-crack-spread-seasonally-adjusted-mean-reversion-stop-lockout-2026-09-12.md`, `moving-band-statistical-arbitrage-convex-concave-markowitz-2026-09-05.md`) evaluate crypto perpetual pairs, physical refinery crack spreads, and convex-concave Markowitz optimization; none implement the 4-way OU estimator ablation on large-cap equity proxy pairs, the Hansen SPA / White Reality Check multiple-testing deflation suite, or ADV-constrained portfolio allocation across sector-matched baskets.

## Economic mechanism

### Source-reported

1. **Relative-Value Cointegration & Stationarity Disequilibrium:**
   Classical statistical arbitrage posits that economically related assets (e.g., firms sharing identical industry classifications, supply chains, or revenue exposures) share a common stochastic drift. While idiosyncratic shocks cause relative price divergence, structural forces—such as competitive product substitution, corporate arbitrage, and sector rotation—eventually force log-price linear combinations to mean-revert toward long-run equilibrium:
   $$S_t = \log(P_{1,t}) - \beta \log(P_{2,t}) \sim \mathcal{I}(0)$$
   When extended beyond pairwise relationships to 3-asset baskets, the system utilizes the Johansen likelihood-ratio rank test (Johansen 1988, 1991) to extract the primary cointegrating vector $w \in \mathbb{R}^N$ from vector error-correction specifications (VECM).

2. **Spread Dynamics & Estimator Misspecification:**
   Standard pairs trading assumes that spread deviations follow a static, continuous-time Ornstein-Uhlenbeck (OU) diffusion process:
   $$dS_t = \kappa (\mu - S_t) dt + \sigma dW_t$$
   However, empirical equity spreads frequently exhibit non-stationary drift, parameter shifts across market regimes, or nonlinear mean-reversion speeds. The source structures a 4-way estimator comparison:
   - **Static OU:** Ordinary least squares on lagged spread levels assuming constant speed $\kappa$ and long-run mean $\mu$.
   - **Kalman-OU:** Linear-Gaussian state-space tracking (Harvey 1989) allowing AR(1) autoregressive coefficient $\phi_t$ and level intercept $c_t$ to evolve dynamically under process noise $Q$.
   - **Neural OU:** Lightweight feedforward autoencoder with sequence-anchored latent dynamics designed to capture nonlinear compression.
   - **Regime-Switching OU:** 2-state Gaussian Hidden Markov Model (HMM) solved via Expectation-Maximization (Baum-Welch algorithm) and Viterbi path decoding, decomposing the spread into high-reversion versus persistent drift regimes.

3. **Selection Attrition & The Multiple-Testing Trap:**
   The central philosophical thesis of `p4_stat_arb` is that unconstrained parameter and pair searches across extensive equity panels generate spurious apparent alpha. In-sample backtest winners systematically decay out of sample once subjected to:
   - Execution frictions (bid-ask spread and execution slippage);
   - Asymmetric financing costs (borrow fees on short equity legs);
   - Capacity bottlenecks (ADV participation limits);
   - Formal family-wise error rate (FWER) and false discovery rate (FDR) deflation: Bonferroni inequality, Benjamini-Hochberg (BH), Benjamini-Yekutieli (BY), Storey $q$-values, White's Reality Check (White 2000), and Hansen's Superior Predictive Ability (SPA) test (Hansen 2005).

### Research interpretation

- **Epistemic Null Baseline in Relative Value:**
  The repository models statistical arbitrage not as a static positive-edge alpha capture, but as an empirical attrition gauntlet where the default expectation is total failure under transaction costs and multiple-testing corrections.
- **Adaptive Estimation vs. Overfitting Tradeoff:**
  While Kalman filtering and Neural networks increase model capacity to track non-stationary spreads, they risk overfitting high-frequency noise or lagging abrupt regime shifts. Conversely, 2-state Gaussian HMMs explicitly partition the state space into distinct mean-reverting versus trending phases, suppressing trading activity during volatile trend expansion.
- **Block-Bootstrap Resampling Tied to Physical Half-Life:**
  Calibrating block lengths in Hansen SPA and White RC to twice the estimated OU half-life ($2 \times \tau$) directly preserves the temporal autocorrelation structure of the spread, preventing false rejections of the null hypothesis caused by independent-resampling assumptions.

## Signal

The signal architecture operates under two distinct evaluation pipelines (`source-reported`):

### 1. Main Walk-Forward Z-Score Engine (`source-reported`)

For each candidate pair or Johansen basket:
- **Spread Formulation:**
  - Pair Spread: $S_t = \log(P_{1,t}) - \beta \log(P_{2,t})$ where $\beta$ is estimated via OLS on the formation window (`source-reported`).
  - Basket Spread: $S_t = \sum_{i=1}^N w_i \log(P_{i,t})$ where $w$ is the leading Johansen cointegrating eigenvector normalized such that $\sum_{i=1}^N |w_i| = 1.0$ (`source-reported`).
- **Normalized Z-Score:**
  $$z_t = \frac{S_t - \mu}{\sigma_{\text{stationary}}}$$
  where $\sigma_{\text{stationary}} = \frac{\sigma_{\text{residual}}}{\sqrt{\max(1 - \phi^2, 10^{-8})}}$, $\phi = e^{-\kappa \Delta t}$, and $\mu = \frac{\text{intercept}}{1 - \phi}$ (`source-reported`).
- **State Machine Position Logic:**
  - Entry Long ($+1$): when $z_t \le -z_{\text{entry}}$ (default $z_{\text{entry}} = 2.0$, smoke run $1.8$) (`source-reported`).
  - Entry Short ($-1$): when $z_t \ge z_{\text{entry}}$ (`source-reported`).
  - Exit to Flat ($0$): when $|z_t| \le z_{\text{exit}}$ (default $z_{\text{exit}} = 0.5$) (`source-reported`).
  - Stop-Loss to Flat ($0$): when $|z_t| \ge z_{\text{stop}}$ (default $z_{\text{stop}} = 4.0$) (`source-reported`).
- **Execution Timing:**
  Position changes take effect with a 1-bar execution delay (`position.shift(1)`), trading at next-bar closing prices (`source-reported`).

### 2. 4-Way Ablation Benchmark Signal (`source-reported`)

To strictly isolate the performance of parameter estimators without confounding execution overlays, the S&P 500 ablation uses a pure directional sign rule:
$$\text{Signal}_t = \text{sign}(\mu - S_t)$$
evaluated at daily close (`source-reported`).

### 3. Regime-Filtered Signal (`source-reported`)

When using `src/p4/regime_switch.py`:
1. Spread $S_t$ is modeled via a 2-state Gaussian HMM with EM iterations (`source-reported`).
2. Regime-specific weighted half-lives $\tau_k = \ln(2) / \kappa_k$ are calculated for each regime $k \in \{0, 1\}$.
3. The active high-reversion regime is identified as:
   $$k^* = \arg\min_k \tau_k$$
4. Viterbi states $\hat{k}_t$ are decoded. If $\hat{k}_t \ne k^*$, signal is forced to $0$ (`source-reported`).
5. If $\hat{k}_t = k^*$, trade signal fires based on regime-specific mean $\mu_{k^*}$ and standard deviation $\sigma_{k^*}$ with entry threshold $z_{\text{threshold}} = 2.0$ (`source-reported`).

## Required data

- **Universe Definition (`source-reported`):**
  - **S&P 500 Proxy Universe:** Top 500 equities by portfolio weight from Russell 3000 / IWV holdings (`source-reported`).
  - **ETF Universe (20 liquid instruments):** SPY, QQQ, IWM, DIA, XLK, XLF, XLE, XLU, XLP, XLY, XLI, XLV, XLB, XLC, VNQ, XBI, SMH, KRE, HYG, TLT (`source-reported`).
  - **Smoke Universe (acceptance testing):** 12 liquid equities + 10 ETFs (22 total assets) (`source-reported`).
- **Timeframe:** Daily bars (adjusted close prices, volumes) (`source-reported`).
- **History Window:** Minimum 2016-01-01 through 2025-12-31 (10 years) for full backtests; 2019-01-02 through 2025-12-30 for smoke runs (`source-reported`).
- **Walk-Forward Cadence (`source-reported`):**
  - Formation window: 504 trading days ($\approx 2$ years; smoke run 378 days) (`source-reported`).
  - Validation window: 126 trading days ($\approx 6$ months) (`source-reported`).
  - Test window: 126 trading days ($\approx 6$ months) (`source-reported`).
  - Rolling step: 126 trading days (`source-reported`).
- **Candidate Pair Filtering Hurdles (`source-reported`):**
  - Grouping: Sub-industry match first, sector match fallback (`source-reported`).
  - Minimum correlation: $\rho \ge 0.60$ (`source-reported`).
  - Engle-Granger cointegration significance: $p \le 0.05$ (`source-reported`).
  - Johansen rank test significance: $p \le 0.05$ (`source-reported`).
  - OU half-life sanity bounds: $\tau \in [5.0, 30.0]$ trading days (smoke run $[4.0, 35.0]$ days) (`source-reported`).
  - Minimum stock price: $\$5.00$ (`source-reported`).
  - Minimum Average Daily Traded Volume (ADTV): $\$25,000,000$ USD (`source-reported`).
- **Point-in-Time Limitations:**
  - Constituent lists are drawn from current snapshot holdings rather than historical point-in-time index memberships (`source-reported` caveat).
  - Delisting returns and bankruptcies are not tracked; historical survival is implicitly assumed (`source-reported` caveat).

## Execution assumptions

- **Execution Timing:** All orders executed on the bar following signal generation (`t+1`), utilizing next-day closing prices (`source-reported`).
- **Order Model:** Market-on-close / full execution at daily closing marks (`source-reported`).
- **Transaction Costs (`source-reported`):**
  - Half-spread: $5.0$ bps (`source-reported`).
  - Slippage: $3.0$ bps per unit turnover (`source-reported`).
  - Total round-trip linear execution friction: $8.0$ bps per unit turnover (`source-reported`).
- **Financing & Borrow Costs (`source-reported`):**
  - Short equity borrow fee: $50.0$ bps annualized ($0.50\% / 252$ daily on short notional exposure) (`source-reported`).
- **Ablation Benchmark Cost Penalty (`source-reported`):**
  - Simplified turnover penalty: $5.0$ bps per unit of annualized turnover:
    $$\text{Sharpe}_{\text{net}} = \text{Sharpe}_{\text{gross}} - 0.0005 \times \text{turnover} \times 252$$
    (`source-reported`).
- **Portfolio Sizing & Capacity Limits (`source-reported`):**
  - Base capital: $\$10,000,000$ USD (`source-reported`).
  - Dollar neutrality: Equal dollar weighting across long and short legs (`source-reported`).
  - Capacity cap: Maximum $5.0\%$ of 30-day Average Daily Volume (ADV) per asset (`source-reported`).
  - Pro-rata scaling: If aggregate position sizing exceeds $5.0\%$ ADV on any asset, all portfolio allocations are scaled down proportionally (`source-reported`).
- **Execution Frictions (Crypto Porting):**
  - Crypto taker fee ($4.0$ to $5.0$ bps), perpetual funding rate settlement (8-hour cadence), and liquidation buffers: `research-proposed`.

## Evidence

### Source-reported

All empirical metrics trace directly to `pdwi2020/p4_stat_arb` commit `3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b`, specifically `memo.md`, `README.md`, and `configs/p4_config.yaml`:

1. **S&P 500 Proxy 4-Way OU Ablation (16 Validated Pairs):**
   Evaluated on 16 surviving large-cap proxy pairs across utilities (`AEP/DUK`), materials (`DD/PPG`), banks (`TFC/USB`), and REITs (`EGP/ESS`) over a 2-year window (`source-reported`):

   | Estimator | Median $\kappa$ | Median Net Sharpe | Mean Net Sharpe | $N$ Pairs | Read (`source-reported`) |
   | :--- | :---: | :---: | :---: | :---: | :--- |
   | **Static OU** | $0.025$ | $0.95$ | $1.06$ | 16 | Strong, simple baseline |
   | **Kalman-OU** | $0.113$ | $0.75$ | $0.94$ | 16 | Adaptive, but over-corrects noisy windows |
   | **Neural OU** | $0.042$ | $0.36$ | $0.42$ | 16 | Undertrained / over-parameterized on small sample |
   | **Regime-Switch OU** | $0.049$ | **$1.07$** | $0.98$ | 16 | Top median performance; isolates mean-reversion state |

2. **Full Multiple-Testing Deflation on Real Mixed Universe (22 Assets, 9 Windows):**
   Evaluated on 12 equities + 10 ETFs across 9 walk-forward cycles (`source-reported`):
   - Candidate pairs discovered: 4 (`SMH/XLK`, `GOOGL/META`, `QQQ/SPY`, and second `SMH/XLK` window) (`source-reported`).
   - Basket candidates passing screen: 0 (`source-reported`).
   - Raw positive test-set strategies: 0 / 29 tested (`source-reported`).
   - Least negative test Sharpe: `pair_w01_GOOGL_META` at $-0.235$ (`source-reported`).
   - Worst test Sharpe: `pair_w03_QQQ_SPY` at $-8.359$ (`source-reported`).
   - **Bonferroni Adjustment:** Significance threshold $\alpha / N = 0.05 / 4 = 0.0125$; **0 survivors** (`source-reported`).
   - **Hansen Superior Predictive Ability (SPA):** Null hypothesis cannot be rejected; **0 survivors** (`source-reported`).
   - **White's Reality Check:** Nominated best candidate `GOOGL/META`, with bootstrap $p\text{-value} = \mathbf{0.995}$ (statistically indistinguishable from pure data mining) (`source-reported`).
   - **Aggregate Portfolio Realized P&L:** Total return $= 0.0\%$, net Sharpe $= 0.0$ (because zero strategies satisfied the positive validation hurdle to enter live portfolio allocation) (`source-reported`).

### Independently reproduced

Not independently reproduced. All figures and performance metrics cited above represent third-party reported findings from the repository audit of `pdwi2020/p4_stat_arb` (commit `3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b`). No independent backtest execution has been conducted in our proprietary execution stack.

### Negative evidence

1. **Complete Attrition under Multiple-Testing Deflation:**
   The real mixed-universe walk-forward run demonstrates that pair cointegration established during formation windows frequently evaporates out of sample. With a White Reality Check $p$-value of $0.995$ and zero Hansen SPA survivors, the observed out-of-sample returns are completely explained by chance and data snooping (`source-reported`).
2. **Neural Model Underperformance:**
   Neural OU achieved a median net Sharpe of only $0.36$ compared to $0.95$ for static OLS. The source notes that fitting neural network estimators on $\approx 750$ in-sample observations introduces high variance and parameter instability (`source-reported`).
3. **Turnover & Borrow Cost Sensitivity:**
   Pairs that appear marginally profitable before costs are eliminated once the $8.0$ bps round-trip friction and $50.0$ bps annual borrow cost are applied (`source-reported`).

## Falsification plan

To empirically validate or disconfirm the statistical arbitrage mechanism and determine whether the regime-switching advantage is genuine:

1. **Point-in-Time Survivorship Audit:**
   - *Test:* Replace the static Russell 3000 weight proxy with historical, point-in-time S&P 500 index constituent membership and include delisted companies.
   - *Decision Rule:* If median net Sharpe drops by $> 50\%$ or drops below zero after eliminating survivorship bias, reject the empirical profitability hypothesis (`research-defined falsification threshold`).
2. **Stationary Block Bootstrap Perturbation:**
   - *Test:* Resample daily returns using stationary block bootstrap with block lengths set to $2 \times \tau$.
   - *Decision Rule:* If White's Reality Check $p$-value remains $> 0.20$ across $N \ge 100$ candidate pairs, falsify the hypothesis that the strategy family possesses statistical superiority over random selection (`research-defined falsification threshold`).
3. **Friction Hurdle Stress Test:**
   - *Test:* Scale execution costs from $8.0$ bps up to $16.0$ bps round-trip and borrow costs from $50$ bps to $150$ bps per annum.
   - *Decision Rule:* If net Sharpe drops below $0.0$ across $> 80\%$ of historically cointegrated pairs under doubled frictions, classify the alpha as economically non-viable (`research-defined falsification threshold`).
4. **Regime Persistence Breakdown Test:**
   - *Test:* Evaluate the 2-state Gaussian HMM during major macro transition regimes (e.g., March 2020 liquidity shock, 2022 rate hiking cycle).
   - *Decision Rule:* If the high-reversion regime experiences drawdown $> 20\%$ due to state transition lag, falsify the claim that HMM regime filtering successfully mitigates trend risk (`research-defined falsification threshold`).

## Crypto portability

- **Classification:** `adapted` / `unproven`.
- **Portability Analysis & Structural Differences:**
  1. **Financing vs. Funding Rates:** In US equities, short positions incur explicit stock borrow fees ($50$ bps/year baseline, escalating for hard-to-borrow names). In crypto perpetuals, borrowing costs are replaced by dynamic 8-hour funding rates. If a pair involves a high-funding asset, funding payments can rapidly overwhelm mean-reversion P&L.
  2. **24/7 Continuous Trading:** Traditional equity pairs benefit from overnight settlement and synchronized market-on-close auctions. Crypto perpetuals trade continuously with fragmented liquidity across exchanges (Binance, OKX, Bybit), introducing cross-venue basis risk and execution desynchronization.
  3. **Non-Gaussian Extreme Tail Discontinuities:** Crypto markets experience frequent flash crashes and cascading liquidations. The Gaussian emission assumption in `GaussianHMM` ($\mathcal{N}(\mu, \sigma^2)$) is heavily misspecified for crypto spread distributions; student-t or jump-diffusion emissions would be required (`research-proposed`).
  4. **Stablecoin De-Pegging & Collateral Risk:** Coin-margined vs. USDT-margined contracts introduce cross-currency denominator risk not present in USD-denominated equities.

## Limitations

- `not independently reproduced`: Findings reflect the author's committed logs and have not been executed on internal engines.
- `survivorship bias`: Equities are screened from current constituent weights rather than point-in-time historical tables (`source-reported` limitation).
- `small sample ablation`: The 4-way OU ablation utilizes $N = 16$ pairs over a single 2-year window; confidence intervals between static OU ($0.95$) and regime-switch OU ($1.07$) overlap heavily (`source-reported` limitation).
- `simplified ablation frictions`: The 4-way ablation applies a flat $5.0$ bps turnover penalty rather than the full event-driven execution and borrow cost stack (`source-reported` limitation).
- `model capacity underfitting`: Neural OU exhibits severe underperformance due to limited training samples per pair (`source-reported` limitation).

## Implementation status

- `not-implemented`: This research capture does not modify `nautilus-quant-system`, create a strategy family, or authorize Paper, Testnet, or Live execution.
- No algorithmic code from `p4_stat_arb` has been ingested into NautilusTrader or PyBroker.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- This record serves as normalized research material documenting statistical arbitrage attrition, Johansen basket extraction, and multiple-testing corrections. It does not constitute authorization for deployment or capital allocation.

## Related Wiki records

- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`
- `[[quant/dynamic-johansen-deep-weighted-ensemble-cryptocurrency-pairs-2026-09-05]]`
- `[[quant/moving-band-statistical-arbitrage-convex-concave-markowitz-2026-09-05]]`
- `[[quant/partial-information-regime-filtering-ddpg-ornstein-uhlenbeck-pairs-trading-2026-09-05]]`

## Sources

1. **Primary Source Repository:**
   - Author: `pdwi2020`
   - Repository: `https://github.com/pdwi2020/p4_stat_arb`
   - Commit SHA: `3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b`
   - Date: April 20, 2026
   - Permalinks:
     - [`configs/p4_config.yaml`](https://github.com/pdwi2020/p4_stat_arb/blob/3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b/configs/p4_config.yaml)
     - [`src/p4/pipeline.py`](https://github.com/pdwi2020/p4_stat_arb/blob/3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b/src/p4/pipeline.py)
     - [`src/p4/johansen.py`](https://github.com/pdwi2020/p4_stat_arb/blob/3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b/src/p4/johansen.py)
     - [`src/p4/ou_estimator.py`](https://github.com/pdwi2020/p4_stat_arb/blob/3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b/src/p4/ou_estimator.py)
     - [`src/p4/kalman_ou.py`](https://github.com/pdwi2020/p4_stat_arb/blob/3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b/src/p4/kalman_ou.py)
     - [`src/p4/regime_switch.py`](https://github.com/pdwi2020/p4_stat_arb/blob/3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b/src/p4/regime_switch.py)
     - [`src/p4/neural_ou.py`](https://github.com/pdwi2020/p4_stat_arb/blob/3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b/src/p4/neural_ou.py)
     - [`src/p4/multiple_testing.py`](https://github.com/pdwi2020/p4_stat_arb/blob/3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b/src/p4/multiple_testing.py)
     - [`src/p4/backtest.py`](https://github.com/pdwi2020/p4_stat_arb/blob/3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b/src/p4/backtest.py)
     - [`src/p4/capacity.py`](https://github.com/pdwi2020/p4_stat_arb/blob/3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b/src/p4/capacity.py)
     - [`src/p4/run_sp500_ablation.py`](https://github.com/pdwi2020/p4_stat_arb/blob/3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b/src/p4/run_sp500_ablation.py)
     - [`memo.md`](https://github.com/pdwi2020/p4_stat_arb/blob/3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b/memo.md)
     - [`README.md`](https://github.com/pdwi2020/p4_stat_arb/blob/3b3cb6404ad3a9831dbb7d6b8d509d4aebd5591b/README.md)
2. **Methodological Literature Cited by Source:**
   - Johansen, S. (1988). "Statistical analysis of cointegration vectors." *Journal of Economic Dynamics and Control*, 12(2-3), 231-254.
   - Johansen, S. (1991). "Estimation and hypothesis testing of cointegration vectors in Gaussian vector autoregressive models." *Econometrica*, 59(6), 1551-1580.
   - White, H. (2000). "A reality check for data snooping." *Econometrica*, 68(5), 1097-1126.
   - Hansen, P. R. (2005). "A test for superior predictive ability." *Journal of Business & Economic Statistics*, 23(4), 365-380.
   - Storey, J. D. (2002). "A direct approach to false discovery rates." *Journal of the Royal Statistical Society: Series B*, 64(3), 479-498.
   - Benjamini, Y., and Hochberg, Y. (1995). "Controlling the false discovery rate: a practical and powerful approach to multiple testing." *Journal of the Royal Statistical Society: Series B*, 57(1), 289-300.
   - Benjamini, Y., and Yekutieli, D. (2001). "The control of the false discovery rate under dependency." *Annals of Statistics*, 29(4), 1165-1188.
   - Avellaneda, M., and Lee, J. H. (2010). "Statistical arbitrage in the US equities market." *Quantitative Finance*, 10(7), 761-782.
   - Engle, R. F., and Granger, C. W. (1987). "Co-integration and error correction: representation, estimation, and testing." *Econometrica*, 55(2), 251-276.
