---
schema: strategy-research-record-v1
title: Target Alignment, Dilution Bound, and Cautious Cross-Sectional Forecast Selection
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-22
sources:
  - https://arxiv.org/abs/2609.26303
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Target Alignment, Dilution Bound, and Cautious Cross-Sectional Forecast Selection

## Provenance

- **Primary Source:** Masoud Soleimani (Department of Information Engineering, University of Pisa, Pisa, Italy, `m.soleimani@ieee.org`), *"Target alignment, dilution and forecast selection when cross-sectional forecasts share a common target"*, arXiv preprint `arXiv:2609.26303v1 [econ.EM]`, submitted 22 September 2026. Journal destination on record: *International Journal of Forecasting*. License: CC BY-NC-ND 4.0.
- **Canonical Identifier / Stable URL:** https://arxiv.org/abs/2609.26303
- **Full-Text HTML Source:** https://arxiv.org/html/2609.26303v1 (primary text, proofs, simulation designs A–G, Sections 1–12, and Appendices A–C directly read in full on 2026-09-24).
- **Canonical DOI:** [10.48550/arXiv.2609.26303](https://doi.org/10.48550/arXiv.2609.26303)
- **Data and Code Availability (as reported by primary source):** Complete replication package announced for public release with persistent identifier upon paper acceptance. Package contains pipeline notebook (panel construction, target geometry, admission and weighting procedures, inference, nested rolling-origin engine, simulation designs A–G, empirical panels, placebo, and positive control); run presets and configuration files; prompt templates and forecaster registry; cached model responses with SHA-256 hashes and access timestamps; generation failure logs; and price rebuild scripts (`source-reported`).
- **Repository Deduplication Audit (pre-write, 2026-09-24):** A complete repository search across all `*.md` files and `coverage_manifest.csv` for `2609.26303`, `Soleimani`, `Target alignment, dilution`, `target-orthogonal decomposition`, and `common-target deviation correlation` returned **zero prior records**. Related forecast combination, LLM factor, and falsification records in the repository (such as `limt-hierarchical-multitask-liquidity-aware-ashare-cross-sectional-apo-2026-09-23.md`, `two-engine-llm-intrinsic-valuation-consensus-margin-of-safety-forward-ic-2026-09-23.md`, `llm-persona-consensus-mention-frequency-top50-us-equity-six-factor-2026-09-22.md`, and `look-ahead-bias-pretrained-financial-forecasting-pit-vintage-arxiv-2609.20554-2026-09-19.md`) study different architectures, single LLM workflows, training-vintage leakage, or multi-task neural networks; none formulate the exact target-orthogonal geometry, the equal-weight dilution bound, the three-way admission rule, or the cross-sectional alignment falsification across LLM ensembles and ETF momentum panels. This record represents an independent, source-verified capture.

## Economic mechanism

### Source-reported

In empirical asset pricing and quantitative forecasting, researchers frequently score units (equities, ETFs, crypto assets) per date against a standardized realized relative outcome $y_t$. Practitioners routinely combine multiple model-generated or rule-based forecasts through equal weighting, relying on the classic diversification heuristic that adding forecasters whose errors differ will offset mistakes and improve accuracy.

The author demonstrates that when forecasts share a common standardized cross-sectional target:
1. **Target-Orthogonal Decomposition (Proposition 1):** Every standardized forecast $s_{it}$ splits exactly into a projection onto the standardized realized target $y_t$ (scaled by its target alignment $\gamma_{it} = \langle s_{it}, y_t \rangle_t$) and a target-orthogonal component $u_{it} = s_{it} - \gamma_{it} y_t$, where $\langle u_{it}, y_t \rangle_t = 0$. Consequently, the forecast correlation matrix decomposes as $C_t = \gamma_t \gamma_t' + K_t$, with $K_t \succeq 0$.
2. **Deviation Correlation Is a Fixed Translation (Proposition 5):** The correlation of forecast errors / deviations from the common target ($\rho^e_{ij,t}$) does not measure pure forecast diversity. Instead, at zero target alignment, $\rho^e_{ij,t} = (1 + \rho^s_{ij,t})/2$, mapping $[-1, 1]$ into $[0, 1]$ and halving dispersion. For small alignments, $\rho^e_{ij,t} - (1 + \rho^s_{ij,t})/2 = -\frac{1}{4}(\gamma_{it} + \gamma_{jt})(1 - \rho^s_{ij,t}) + O(\gamma^2)$. Deviation correlation is mechanically positive even when raw forecasts are negatively correlated.
3. **The No-Information Hurdle (Corollary 1):** The zero forecast ($w=0$) has relative-score loss $\mathcal{R}(0) \equiv 1.000$. An equal-weight combination of $N$ forecasters with mean pairwise correlation $\bar{\rho}$ outperforms this no-information benchmark ($\mathcal{R}(\mathbf{1}/N) < 1$) if and only if mean alignment exceeds half the composite's squared norm:
   $$\bar{\gamma}_{\mathrm{EW}} > \frac{1}{2} \left[ \bar{\rho} + \frac{1 - \bar{\rho}}{N} \right]$$
   Unless alignment satisfies this hurdle, averaging standardized forecasts merely draws the composite toward zero while accumulating orthogonal variance, yielding worse risk than abstaining.
4. **The Dilution Phenomenon (Proposition 9):** Adding a candidate batch $A$ to an incumbent equal-weight pool $P$ changes relative-score risk by $\Delta_{A|P} = \Delta^{\mathrm{sf}}_{A|P} + \Delta^{\mathrm{scale}}_{A|P}$. When candidate alignment is weak, the scale-free gain $\Delta^{\mathrm{sf}}$ is negligible and bounded by $-\Delta^{\mathrm{sf}}_{A|P} \le (m \bar{g}_A)^2 / (n^2 q_P)$ (decaying quadratically with pool size $n$). Meanwhile, adding an unaligned or negatively correlated candidate reduces the composite's squared norm $q_{P \cup A}$, shrinking the composite toward zero. Unscaled equal-weight admission rewards this *scale dilution* as an apparent risk reduction even when the candidate has zero predictive information.

### Research interpretation

The falsifiable hypothesis is that **in high-dimensional cross-sectional asset return forecasting (including LLM-generated persona ensembles and traditional momentum/reversal factor pools), apparent improvements from equal-weight ensembling are frequently artifacts of scale dilution rather than true target alignment; when evaluated against a zero-information benchmark and tested under scale-free admission, multi-agent LLM ensembles and mechanical factor pools fail to demonstrate genuine out-of-sample predictive edge**.

Furthermore, because forecast correlation mechanically embeds alignment ($C = \gamma \gamma' + K$), selecting "diverse" forecasters by minimizing forecast correlation preferentially selects unaligned or counter-predictive forecasters, causing diversity-seeking heuristic selection to rank candidates backwards relative to true incremental value.

Operational portfolio mapping, long-short portfolio deciles, execution triggers, fee schedules, and trading models below are not provided by the paper's purely forecasting-theoretic evaluation and are `research-proposed`.

## Signal

### Source-Reported Mathematical Signal & Estimation Formulation

1. **Cross-Sectional Normalization:**
   At date $t$, let $r_t \in \mathbb{R}^{M_t}$ denote the realized cross-sectional return vector and $x_{it} \in \mathbb{R}^{M_t}$ the raw forecast vector of forecaster $i \in \{1, \dots, N\}$ across common support $\mathcal{M}_t^*$ ($M_t = |\mathcal{M}_t^*| \ge 20$). Standardize with zero mean and unit $L_2$ norm:
   $$s_{it} = \frac{x_{it} - \bar{x}_{it}\mathbf{1}}{\hat{\sigma}_{x_i,t}}, \quad y_t = \frac{r_t - \bar{r}_t\mathbf{1}}{\hat{\sigma}_{r,t}}, \quad \|s_{it}\|_t = \|y_t\|_t = 1$$
   where $\langle a, b \rangle_t = M_t^{-1} a' b$. Missing forecasts are not imputed; dates with degenerate target variance ($\hat{\sigma}_{r,t} \le 10^{-8}$) or zero forecast dispersion ($\hat{\sigma}_{x_i,t} \le 10^{-8}$) are excluded (`source-reported`).
2. **Relative-Score Loss:**
   For a composite forecast $s_{w,t} = \sum_i w_i s_{it}$, the date loss is $\|s_{w,t} - y_t\|_t^2 = 1 - 2 w' \gamma_t + w' C_t w$. Time-aggregated risk is $\mathcal{R}(w) = 1 - 2 g_w + q_w$, where $g_w = w' \bar{\gamma}$ is mean alignment and $q_w = w' \bar{C} w$ is composite squared norm (`source-reported`).
3. **Three-Way Cautious Admission Rule:**
   For incumbent pool $P$ of size $n$ and candidate family $\{A_j\}$, compute incremental loss differences $d_{j,t} = \ell_{P \cup A_j, t} - \ell_{P,t}$ and sample mean $\hat{\Delta}_j = \sum_t a_t d_{j,t}$. Compute Newey–West HAC standard errors with lag $\lfloor 4(T/100)^{2/9} \rfloor$. Let critical value $c$ be the $(1 - \alpha)$ quantile of $\max_j |Z_j|$ under the estimated HAC correlation matrix ($\alpha = 0.05$).
   - **Admit:** $\hat{\Delta}_j + c \cdot \widehat{SE}_j < -\delta$ (statistically significant risk reduction exceeding practical margin $\delta$).
   - **Reject:** $\hat{\Delta}_j - c \cdot \widehat{SE}_j > 0$ (statistically significant risk increase).
   - **Undecided:** otherwise (abstain from admission).
   Greedy forward selection begins with the candidate exhibiting highest history alignment, admitting the smallest $\hat{\Delta}$ at each step, and halts when no candidate is admitted (`source-reported`).
4. **Scale-Free Variant:**
   To prevent dilution admission, the scale-free rule evaluates candidates solely on the correlation gain $\Delta^{\mathrm{sf}}_{A|P} = \rho_P^2 - \rho_{P \cup A}^2$, where $\rho_P = g_P / \sqrt{q_P}$, using scale-free margin $\delta^{\mathrm{sf}}$ (`source-reported`).
5. **Alternative Ensembling Benchmarks Evaluated:**
   - Equal weight, all $N$ forecasters (`source-reported`).
   - Partially egalitarian LASSO (peLASSO, Diebold & Shin 2019): non-negative LASSO on aggregated moments with equal weighting on active support (`source-reported`).
   - Shrunk ridge weights: non-negative quadratic weights on shrunk joint correlation matrix $\widetilde{R} = (1 - \lambda)\widehat{R} + \lambda R_0$ (`source-reported`).
   - Ridge projection: unconstrained regression weights $(\widetilde{C} + \eta I)^{-1} \widetilde{\gamma}$ (`source-reported`).
   - Exhaustive combinatorial search across all $2^N - 1$ possible subsets on history risk (`source-reported`).

### Operational Trade-Execution Mapping (`research-proposed`)

The primary source evaluates relative-score forecasting accuracy and top-minus-bottom quintile spread diagnostics; it does not specify an order-execution engine, rebalance execution timestamp, or trading fee schedule. The following lifecycle is `research-proposed` for empirical validation and falsification:
1. **Universe & Cadence:** At the close of each rebalance period $t$ (weekly for equities, monthly for ETFs), compute composite cross-sectional standardized scores $\hat{s}_{w,t}$ across eligible liquid assets.
2. **Position Sizing:** Rank assets by $\hat{s}_{w,t}$. Construct a dollar-neutral long-short portfolio: long top quintile (equal or score-weighted), short bottom quintile, with total gross leverage fixed at $1.0\times$.
3. **Execution Timing:** Form signals strictly at bar close; submit market-on-open (MOO) or VWAP orders on next bar open ($t+1$) to avoid same-bar execution leakage.
4. **Transaction Cost Barrier:** Deduct 5 bps one-way taker fee plus 5 bps slippage assumption (`research-proposed`).
5. **Lifecycle Status:** Because the primary paper reports pure statistical forecasting metrics without live order routing, the strategy lifecycle is **underspecified** for direct execution.

## Required data

- **Asset Universe:**
  - *Empirical Panel 1:* 60 US large-cap equities (fixed end-of-sample panel, January 2021 to June 2026; median common support 60, minimum 49) (`source-reported`). Note: conditioned on survival at end of sample (`source-reported`).
  - *Empirical Panel 2:* 42 cross-asset ETFs (country equities, US sectors, broad indices, real estate, fixed income; 2005 to 2026; 256 monthly dates, 16 outer origins, 196 test dates; not screened on survival) (`source-reported`).
- **Target Data:** Point-in-time cross-sectional returns: 5-day forward return for equities, 21-day forward relative return for ETFs (`source-reported`).
- **Forecaster Feature Sets (Panel 1):**
  - Price-only subset: trailing 1-, 3-, and 12-month returns (`source-reported`).
  - Price-plus-volatility subset: trailing 1-, 3-, 12-month returns plus 63-day realized volatility and 6-month maximum drawdown (`source-reported`).
- **Forecaster Architectures (Panel 1):**
  - 4 LLM lineages: `gpt-5-nano`, `deepseek-v4-flash`, `Llama-3.1-8B-Instruct`, `gemini-3.5-flash-lite` (`source-reported`).
  - 3 personas: momentum, value reversal, macro defensive (`source-reported`).
  - Total LLM forecasters: $4 \text{ models} \times 3 \text{ personas} \times 2 \text{ feature subsets} = 24$ forecasters (`source-reported`).
- **Mechanical Control Signals (Panel 1 & 2):** 9 deterministic rules: 1-month reversal, 3-month momentum, 12-month momentum, 12–1 month momentum, low volatility, low drawdown, and three persona-emulation rules (`source-reported`).
- **Missing Data Handling:** Strictly no imputation. Forecasters with zero variance or missing outputs are excluded for that date. Dates with fewer than 20 common-support assets are excluded (`source-reported`).

## Execution assumptions

- **Source-Reported Execution Assumptions:** None. The paper investigates relative-score forecast verification, correlation geometry, and forecast selection; it does not execute live market orders, simulate order-book fills, or model bid-ask spreads.
- **Signal-to-Order Timing (`research-proposed`):** Signals generated on weekly/monthly closing prices; orders placed on next-session open ($t+1$).
- **Fill Model (`research-proposed`):** Volume-weighted average price (VWAP) or arrival price with zero delay beyond next-open auction.
- **Costs & Fees (`research-proposed`):** US equity / ETF commission and slippage modeled at 5 bps one-way; short borrow cost modeled at 50 bps annualized for general collateral.
- **Turnover Drag:** High-frequency rank churn in 5-day equity rebalancing generates substantial turnover; net returns must be audited against transaction costs (`research-proposed`).

## Evidence

### Source-reported

All figures below are directly cited from Masoud Soleimani (`arXiv:2609.26303v1`, September 2026, Tables 5, 6, 8, 9, 10, 11, 12, Sections 8–10, Appendices B–C) and have **not** been independently reproduced.

#### 1. Retrospective LLM Stress Test (Panel 1: 24 Forecasters on 60 US Equities, 157 Out-of-Sample Test Dates, 2023–2026)
- **Geometry & Alignment (Table 8):**
  - Mean target alignment across 24 LLMs: $\bar{\gamma} = 0.006$ [95% bootstrap CI: $-0.010, 0.020$] — statistically indistinguishable from zero.
  - Mean forecast correlation $\bar{\rho}^s = 0.300$ [$0.284, 0.317$].
  - Mean deviation correlation $\bar{\rho}^e = 0.645$ [$0.637, 0.654$].
  - Departure from zero-alignment benchmark $\bar{\rho}^e - (1 + \bar{\rho}^s)/2 = -0.005$ [$-0.008, -0.002$]. Across all 276 pairs, deviation correlation is almost perfectly linear in forecast correlation ($R^2 = 0.9999$). While 29% of pairwise forecast correlations are negative, **0% of deviation correlations are negative**.
  - Equivalent ensemble size $N_{\mathrm{eff}}$: 3.03 from forecast correlation vs 1.52 from deviation correlation.
  - Time variation of alignment accounts for 5.9% of the trace of $K^{\mathrm{pool}}$.
  - Equal-weight risk in-sample: 1.318, missing the Corollary 1 hurdle by margin $m = -0.159$ [$-0.177, -0.142$].
  - In-sample attainable risk by any linear combination: 0.994.
  - Joint zero-alignment tests: bootstrap Wald $p = 0.065$, simultaneous max-$|t|$ $p = 0.25$ (the asymptotic Wald $p=0.0001$ is proven invalid due to severe over-rejection under dependence).
- **Out-of-Sample Risk & Portfolio Spreads (Table 9, 157 Test Dates):**
  - *No-information baseline ($w=0$):* Risk $\equiv 1.000$.
  - *Equal weight, all 24:* Risk = 1.292; difference vs no-information = $+0.292$ [$0.247, 0.337$]; top-minus-bottom quintile spread = $+0.36\%$ per 5 days ($t = 1.4$).
  - *Three-way equal weight selection:* Selected pool size = 2.0; Risk = 1.079; difference vs equal weight = $-0.213$ [$-0.262, -0.164$]; difference vs no-information = $+0.079$ [$0.055, 0.103$]; spread = $+0.19\%$ ($t = 1.0$).
  - *Pairwise batch selection:* Selected pool size = 2.3; Risk = 1.063; vs no-information = $+0.063$ [$0.042, 0.084$]; spread = $+0.23\%$ ($t = 1.1$).
  - *peLASSO (Diebold & Shin 2019):* Selected pool size = 3.3; Risk = 1.247; vs no-information = $+0.247$ [$-0.123, 0.371$]; spread = $+0.50\%$ ($t = 2.1$).
  - *Exhaustive search (best history subset):* Selected pool size = 6.0; Risk = 1.033; vs no-information = $+0.033$ [$0.016, 0.050$]; spread = $+0.24\%$ ($t = 1.1$).
  - *Minimum deviation correlation selection:* Selected pool size = 2.0; Risk = 1.089; vs no-information = $+0.089$ [$0.062, 0.116$]; spread = $+0.17\%$ ($t = 0.8$).
  - *Shrunk ridge weights:* Risk = 1.019; vs no-information = $+0.019$ [$0.006, 0.032$]; spread = $+0.14\%$ ($t = 0.6$).
  - *Raw affine weights:* Risk = 1.020; vs no-information = $+0.020$ [$0.006, 0.034$]; spread = $+0.24\%$ ($t = 1.0$).
  - *Ridge projection:* Risk = 1.000; vs no-information = $0.000$ [$-0.001, 0.002$]; spread = $-0.10\%$ ($t = -0.5$). The projection effectively abstains (sum of weights = 0.018, gross exposure = 0.11).
  - **Key finding:** **Zero out of 20 tested combination/selection methods beat the no-information forecast out-of-sample.** No top-minus-bottom return spread achieves statistical significance under the Bonferroni cutoff ($|t| \le 2.1$ vs required $3.0$).
- **Cross-Panel Admission & Pure Dilution Demonstration (Table 10):**
  - When value-reversal LLM batch (8 models) is added to the 9-signal mechanical pool under equal weighting: admitted at all 6/6 origins with sample $\hat{\Delta} = -0.130$ and test $\Delta = -0.114$ ($t = -9.8$). However, scale-free component $\hat{\Delta}^{\mathrm{sf}} = -0.0001$ and scale-mismatch component $\hat{\Delta}^{\mathrm{scale}} = -0.130$. The apparent gain is **100% pure scale dilution** from adding uncorrelated noise that shrinks composite variance. Under scale-free admission, 0/6 batches are admitted.
- **Date-Shifted Placebo (50 Random Target Shifts, Section 9.6):**
  - Target circularly shifted across dates, destroying alignment while preserving cross-sectional forecast correlation.
  - Actual mean alignment ($0.0061$) sits in the middle of the placebo distribution (mean $0.0042$, placebo-calibrated $p = 0.55$). Rejection of zero alignment by bootstrap Wald occurs in 22% of placebos, confirming tests are oversized without true signal.

#### 2. Cross-Asset ETF Panel (Panel 2: 42 ETFs, 9 Mechanical Signals, 196 Test Dates, 2005–2026, Table 12)
- Mean target alignment: $\bar{\gamma} = -0.011$. Best individual signal (12–1 momentum): $\bar{\gamma} = 0.033$ ($t = 1.82$). Bootstrap Wald $p = 0.37$, max-$|t|$ $p = 0.20$.
- Mean forecast correlation $\bar{\rho}^s = 0.149$, deviation correlation $\bar{\rho}^e = 0.564$ (benchmark 0.575).
- Equal weighting risk = 1.283 (vs no-info $+0.283, t=9.4$).
- Three-way selection risk = 1.076 ($t=5.7$ vs no-info); exhaustive search risk = 1.061 ($t=5.2$); shrunk affine weights = 1.035 ($t=3.1$); ridge projection = 1.001 ($t=0.5$).
- **Key finding:** Zero combination methods beat the no-information benchmark. Cautious selection eliminates dilution losses relative to full equal weighting (reducing risk from 1.283 to 1.076), but neither individual signals nor composites produce genuine predictive alpha.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Failure of Equal-Weight Ensembling:** Full equal weighting of 24 LLM forecasters generates out-of-sample relative-score risk of 1.292, performing **29.2% worse than a zero-information forecast** ($t = 1.4$, not significant). Averaging noisy, correlated forecasters inflates portfolio risk rather than diversifying it.
2. **Failure of Diversity-Seeking Selection:** Heuristic selection based on minimum forecast correlation ranks candidates backwards (Spearman correlation between history selection metric and future incremental risk is $-0.39$ to $-0.96$ in exchangeable designs, and up to $0.074$ pick regret). Because forecast correlation embeds alignment ($C = \gamma \gamma' + K$), the most "uncorrelated" candidate is systematically the least aligned.
3. **Pure Dilution Exploitation:** In equal-weight admission, zero-information candidates that are uncorrelated with the pool are admitted 24% to 62% of the time, because shrinking composite scale masquerades as variance reduction.
4. **Complete Absence of Predictive Alpha in Evaluated LLM Ensembles:** Neither GPT-5-nano, DeepSeek-v4-flash, LLaMA-3.1-8B, nor Gemini-3.5-flash-lite under momentum, value reversal, or defensive personas achieved statistically significant alignment with 5-day forward equity returns (bootstrap Wald $p = 0.065$, max-$|t|$ $p = 0.25$, top-bottom quintile spread $t = 1.4$).
5. **Absence of Alpha in Monthly Cross-Asset ETF Momentum/Reversal:** The 9 standard mechanical signals across 42 ETFs produced mean alignment $\bar{\gamma} = -0.011$ over 2005–2026, failing to improve on the no-information benchmark across 16 rolling test origins.

## Falsification plan

To falsify the primary paper's conclusions (which claim that cross-sectional LLM/factor combinations suffer from dilution and fail to beat no-information), the following operational tests must be executed:

1. **Real-Time Out-of-Sample Alignment Hurdle:**
   - *Protocol:* Evaluate candidate factor/LLM ensembles on strictly point-in-time, forward-walking crypto or equity panels that postdate model training cutoffs.
   - *`research-defined falsification threshold`:* The candidate ensemble must achieve out-of-sample relative-score risk $\mathcal{R}(w) < 1.000$ with Newey–West HAC $t$-statistic exceeding $2.576$ ($p < 0.01$) against the no-information baseline, and bootstrap Wald $p < 0.01$. If $\mathcal{R}(w) \ge 1.000$, the ensemble is falsified as uninformative.
2. **Scale-Free Incremental Contribution Audit:**
   - *Protocol:* For any multi-signal or multi-agent factor composite, decompose incremental risk into $\Delta^{\mathrm{sf}}$ and $\Delta^{\mathrm{scale}}$.
   - *`research-defined falsification threshold`:* Any candidate signal whose apparent equal-weight risk improvement is driven by scale mismatch ($|\Delta^{\mathrm{scale}}| / |\Delta| > 0.80$) while scale-free alignment contribution is negligible ($|\Delta^{\mathrm{sf}}| < 0.001$) must be rejected as **pure dilution**, not alpha.
3. **Positive Control Benchmark:**
   - *Protocol:* Inject synthetic signal with known alignment $a \in [0.02, 0.10]$ into the candidate pool.
   - *`research-defined falsification threshold`:* If the selection procedure fails to recover planted signals with precision $>0.80$ at $a \ge 0.06$, classify the selection engine as statistically under-powered.
4. **Net Transaction Cost & Turnover Barrier:**
   - *Protocol:* Map cross-sectional ranks into dollar-neutral quintile long-short portfolios with 5 bps one-way taker fee and 5 bps slippage.
   - *`research-defined falsification threshold`:* Net annualized Sharpe ratio must exceed $1.00$ with annualized turnover $< 500\%$. If transaction costs consume $>50\%$ of gross spread, reject the operational strategy.

## Crypto portability

**unproven** / **adapted**

The primary paper analyzes US large-cap equities (daily/weekly) and global ETFs (monthly). The mathematical geometry (Propositions 1–9) is distribution-free and applies directly to any standardized cross-sectional panel. However, portability of the empirical findings and signal-combination frameworks to cryptocurrency markets remains **unproven** and must be treated as research interpretation:

1. **Perpetual Futures Cross-Section:** In crypto perpetual futures (e.g., Binance, Bybit top 50/100 perps), cross-sectional return dispersion is 3–5$\times$ larger than US equities, and idiosyncratic momentum/reversal shocks are pronounced. Applying the target-orthogonal decomposition to crypto cross-sections would test whether crypto factor combinations also suffer from dilution.
2. **Funding-Rate & Basis Distortions:** Crypto perpetual returns include 8-hour funding rates. If funding payments correlate with cross-sectional scores, uncalibrated equal weighting could inadvertently harvest or pay funding drag.
3. **24/7 Continuous Trading & Candle Boundary Alignment:** Crypto lacks synchronous session opens/closes. Standardizing cross-sections across arbitrary UTC 00:00 boundaries induces boundary leakage unless timestamp alignment is strictly controlled.
4. **Survivor Bias & Liquidity Shifts:** Fast listing and delisting of crypto tokens violate the fixed-universe assumptions of Panel 1. Dynamic forecaster availability must be enforced.

## Limitations

- `underspecified`: The paper develops a forecasting and evaluation methodology; it does not specify an executable portfolio execution model, position rebalancing thresholds, fill models, or trading fee schedules.
- `not independently reproduced`: All numerical results are source-reported from `arXiv:2609.26303v1`.
- `data gap`: Retrospective LLM forecasts were generated in 2026 from historical prompts. Although point-in-time inputs were supplied, training data for LLaMA, GPT, Gemini, and DeepSeek overlap partially with the test window (training cutoffs Dec 2023 to Apr 2026). The author explicitly notes this is a stress-test of the geometry, not a real-time trading backtest.
- `survival conditioning in Panel 1`: The 60-stock equity panel was fixed at the end of the sample, conditioning on survival. (Panel 2 ETFs were not screened on survival).
- `negative result`: The primary empirical finding is a rigorous null result: neither 24 LLM configurations nor 9 standard factor rules beat the zero-information forecast out-of-sample once evaluated without dilution artifacts.

## Implementation status

No implementation in the research stack has been completed. `implementation_status: not-implemented`.

## Adoption boundary

Research material only. Presence in this repository does not mean this record has passed ChatGPT Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib full-backtest validation, become a frozen survivor or leaderboard entry, demonstrated profitable or validated alpha, or received approval for implementation, Paper, Testnet, or Live trading.

## Related Wiki records

- `[[quant/limt-hierarchical-multitask-liquidity-aware-ashare-cross-sectional-apo-2026-09-23]]` — Multi-task cross-sectional prediction with adaptive portfolio optimization.
- `[[quant/two-engine-llm-intrinsic-valuation-consensus-margin-of-safety-forward-ic-2026-09-23]]` — Two-engine LLM intrinsic valuation and cross-sectional forward IC analysis.
- `[[quant/look-ahead-bias-pretrained-financial-forecasting-pit-vintage-arxiv-2609.20554-2026-09-19]]` — Look-ahead bias and training vintage leakage in financial foundation models.
- `[[quant/pca-factor-model-error-decomposition-out-of-subspace-arxiv-2609.20550-2026-09-20]]` — Principal component error decomposition in high-dimensional factor models.

## Sources

1. Masoud Soleimani. *"Target alignment, dilution and forecast selection when cross-sectional forecasts share a common target."* arXiv preprint `arXiv:2609.26303v1 [econ.EM]`, submitted 22 September 2026. Target journal: *International Journal of Forecasting*. License: CC BY-NC-ND 4.0.
   - Stable arXiv landing URL: https://arxiv.org/abs/2609.26303
   - Full-text HTML URL: https://arxiv.org/html/2609.26303v1
   - Canonical DOI: [10.48550/arXiv.2609.26303](https://doi.org/10.48550/arXiv.2609.26303)
