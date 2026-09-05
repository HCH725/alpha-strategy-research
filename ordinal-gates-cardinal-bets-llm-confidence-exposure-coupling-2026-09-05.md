---
schema: strategy-research-record-v1
title: "Ordinal Gates, Cardinal Bets: Matching LLM Confidence to the Financial Decision Operator"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - llm-confidence
  - calibration
  - decision-operator
  - exposure-control
  - sentiment-alpha
  - equity-long-short
status: research-only
confidence: medium
source_as_of: 2026-09-01
sources:
  - "https://arxiv.org/abs/2609.00187"
  - "https://arxiv.org/html/2609.00187v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Ordinal Gates, Cardinal Bets: Matching LLM Confidence to the Financial Decision Operator

## Provenance

- **Paper Title:** Ordinal Gates, Cardinal Bets: Matching LLM Confidence to the Financial Decision Operator
- **Authors:** Rayansh Singh and Sara Rezaeimanesh
- **Affiliation:** Michigan State University, East Lansing, MI, USA (`singhr26@msu.edu`, `rezaeima@msu.edu`) [source-reported]
- **Canonical Source Identifier:** arXiv:2609.00187v1 [q-fin.PM, cs.AI, cs.LG, q-fin.TR], submitted August 31, 2026; announced September 1, 2026 [source-reported]
- **Traceable URLs:**
  - Stable Abstract: `https://arxiv.org/abs/2609.00187` [source-reported]
  - Full Text HTML: `https://arxiv.org/html/2609.00187v1` [source-reported]
  - PDF: `https://arxiv.org/pdf/2609.00187v1` [source-reported]
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0) [source-reported]
- **Primary Source Inspection:** Direct verification against the full published HTML text and mathematical proofs of arXiv:2609.00187v1.
- **Repository Deduplication:** Audited the full commit history and all existing records in `alpha-strategy-research`. Zero prior records cite `2609.00187`, Rayansh Singh, Sara Rezaeimanesh, or address the analytical and empirical coupling between LLM confidence calibration, decision operators (ordinal gating vs. cardinal sizing), and downstream exposure controllers.

## Economic mechanism

### Source-reported

1. **Operator-Relative Utility of Confidence Signals:**
   LLM confidence scores are not independently deployable objects: their decision value depends fundamentally on the downstream operator (ordinal vs. cardinal) and exposure controller that consumes them [source-reported].
   - *Ordinal Operators:* Coverage-matched thresholding, top-$k$ selection, abstention, or routing consume only the relative score ranking [source-reported]. For any strictly increasing transformation $\psi$ (such as temperature scaling or Platt scaling), the threshold set $\{C \ge \tau\}$ bijects identically onto $\{\psi(C) \ge t\}$, meaning the accuracy-coverage frontier, every coverage-matched portfolio, and Brier resolution ($\operatorname{RES}(C) = \operatorname{Var}(\mu(C))$) are strictly invariant [source-reported].
   - *Cardinal Operators:* Sizing, capital allocation, and portfolio weighting consume score magnitude [source-reported]. Changing a confidence map alters the magnitude distribution and therefore can invalidate an exposure scale $\kappa$ fitted to the previous score distribution [source-reported].
2. **Resolution Bounds on Selective Prediction:**
   A coverage gate retaining the top-$\varphi$ fraction by confidence achieves an accuracy gain $\Delta_{\mathrm{acc}}(\tau) = P(Z=1 \mid C \ge \tau) - P(Z=1) = \varphi^{-1} \operatorname{Cov}(\mu(C), \mathbf{1}[C \ge \tau])$ [source-reported]. By Cauchy-Schwarz, this gain is strictly bounded by Brier resolution:
   $$|\Delta_{\mathrm{acc}}(\tau)| \le \sqrt{\operatorname{RES}(C) \frac{1-\varphi}{\varphi}}$$
   Across tested LLMs, empirical resolution is tiny ($\operatorname{RES}/\operatorname{UNC} \in [0.07\%, 0.40\%]$), capping the theoretical selective accuracy gain at roughly 4–9 percentage points even under an aggressive 10% coverage floor [source-reported].
3. **Oracle Cardinal Sizing Target vs. Correctness Proxy:**
   Maximizing one-period conditional quadratic utility $\mathbb{E}[h(C) Q] - \frac{\lambda}{2} \mathbb{E}[v(C) h(C)^2]$ (where $Q = D(X) R$, $m(u) = \mathbb{E}[Q \mid C=u]$, and $v(u) = \operatorname{Var}(Q \mid C=u)$) yields the oracle sizing rule [source-reported]:
   $$h^\star(u) = \frac{m(u)}{\lambda v(u)} \propto \frac{\mathbb{E}[Q \mid C=u]}{\operatorname{Var}(Q \mid C=u)}$$
   The cardinal target is conditional signed payoff relative to risk, not correctness probability alone [source-reported]. Correctness probability is used in practical implementations as a lower-variance proxy [source-reported].
4. **Transfer Regret and Map-Scale Coupling:**
   When sizing is restricted to $h(C) = \kappa \phi(C)$, the optimal scale is $\kappa_\phi^\star = \mathbb{E}[Y_\phi]/(\lambda v_\phi)$ [source-reported]. Cross-applying another shape's scale incurs transfer regret [source-reported]:
   $$U_\phi(\kappa_\phi^\star) - U_\phi(\kappa_{\phi'}^\star) = \frac{\lambda}{2} v_\phi (\kappa_{\phi'}^\star - \kappa_\phi^\star)^2 \ge 0$$
   Cross-applying exposure scales fitted to raw confidence distributions to calibrated distributions (or vice-versa) induces large risk-budget errors (e.g. realizing 11.8% volatility vs. an 8.4% target, or running at up to 2.8x intended risk) [source-reported].
5. **Decoupling from Risk Controllers:**
   While matching a correctness map with its own fitted frozen scale improves certainty-equivalent return (CER) by +9.2 pp/yr over a raw frozen system, this benefit drops to +1.6 pp/yr (statistically insignificant, $p=0.195$) under an identical adaptive-volatility controller [source-reported]. The matched gain under frozen scale is largely driven by repairing the risk-target distortion of the frozen controller rather than extracting new orthogonal alpha [source-reported].

### Research interpretation

The core falsifiable thesis is: **Post-hoc recalibration of LLM confidence scores does not generate tradable alpha or improve selective prediction in ordinal rank-based workflows due to rank invariance and negligible Brier resolution; in cardinal sizing workflows, confidence calibration alters score magnitude distributions, requiring joint recalibration of exposure scale $\kappa$ to prevent severe transfer distortion, but the incremental performance edge of matched calibration largely dissolves once dynamic volatility targeting is introduced.**

In financial machine learning, this identifies a critical model-governance failure mode:
1. Quant teams routinely perform temperature scaling or Platt scaling to achieve low Expected Calibration Error (ECE) and assume the resulting signal will improve top-$k$ stock selection. The mathematical invariance proof confirms this is impossible.
2. In position-sizing systems, replacing an LLM prompt, model checkpoint, or calibration map without refitting the portfolio exposure scale creates an unmanaged leverage shock.
3. The headline +9.2 pp/yr CER gain of "matched calibration" is primarily an error-correction mechanism for rigid frozen-scale controllers; an adaptive volatility overlay achieves comparable CER (+6.6 pp/yr raw vs. +8.2 pp/yr calibrated) without requiring complex isotonic recalibration.

## Signal

### Mathematical Formulation

Let $i$ index tickers in the candidate universe and $t$ index daily trading sessions [source-reported].
1. **Direction and Confidence Extraction:**
   For each ticker-day headline bundle, an open-weight instruction-tuned LLM outputs [source-reported]:
   - Direction $D_{i,t} \in \{-1, +1\}$ (predicting positive or negative return) [source-reported].
   - Verbalized confidence score $C_{i,t} \in [0.5, 1.0]$, extracted via greedy regex decoding from an integer prompt 0–100 where 50 indicates total uncertainty ($C = \max(\text{score}, 100-\text{score})/100$) [source-reported].
2. **Confidence Mapping $g_m(C)$:**
   Two maps $m \in \{\text{raw}, \text{correctness}\}$ are evaluated [source-reported]:
   - Raw map: $g_{\text{raw}}(C) = C$ [source-reported].
   - Correctness map: $g_{\text{corr}}(C) = \hat{\mu}(C)$, where $\hat{\mu}: [0.5, 1.0] \to [0, 1]$ is estimated via isotonic regression on the calibration split (2021) targeting the 5-session holding-period return sign $\mathbf{1}[D_{i,t} R_{i, t:t+5} > 0]$ [source-reported]. (Beta and Platt regressions serve as secondary calibrator specifications [source-reported]).
3. **Cohort Position Sizing:**
   The signed single-day cohort position is [source-reported]:
   $$s_{i,t}^{(m)} = D_{i,t} \max\big(0, 2 g_m(C_{i,t}) - 1\big) \in [-1, +1]$$
   where the linear transformation $2 g_m(C) - 1$ maps probability space $[0.5, 1.0]$ to sizing magnitude $[0, 1.0]$, with a zero floor at complete uncertainty $g_m(C) \le 0.5$ [source-reported].
4. **Cohort Aggregation & Holding Horizon:**
   Each position is held for a fixed horizon of $h=5$ trading sessions (weekly cadence) [source-reported].
   The aggregate outstanding unscaled holding is the sum over five overlapping daily entry cohorts [source-reported]:
   $$W_{i,t}^{(m)} = \sum_{\ell=0}^4 s_{i,t-\ell}^{(m)}$$
5. **Exposure Scaling and Portfolio Constraints:**
   - Exposure scale $\kappa_m \ge 0$ is a scalar parameter fitted during the calibration split to target 5% annualized portfolio volatility pre-cost [source-reported].
   - Single-name cap: aggregate holding is clipped to 10% gross portfolio weight [source-reported]:
     $$W_{i,t}^{\text{clipped}} = \operatorname{clip}\big(\kappa_m W_{i,t}^{(m)}, -0.10, +0.10\big)$$
   - Gross portfolio normalization: if total absolute weight exceeds 100%, weights are scaled down uniformly [source-reported]:
     $$w_{i,t}^{(m)} = \frac{W_{i,t}^{\text{clipped}}}{\max\left(1.0, \sum_j |W_{j,t}^{\text{clipped}}|\right)}$$
     ensuring daily gross exposure $\sum_i |w_{i,t}^{(m)}| \le 1.0$ at all times [source-reported].
6. **Execution Timing & Return Accounting:**
   - Headline bundles dated calendar day $D$ are assigned to trading session $T$ strictly following $D$ ($T > D$) [source-reported].
   - Orders enter at session $T$ official open (market-on-open) [source-reported].
   - The 5-session return decomposes into session $T$ open-to-close leg ($R_{i,t}^{(0)}$) plus subsequent four close-to-close legs ($R_{i,t}^{(\ell)}$ for $\ell=1,2,3,4$) [source-reported].

### Operational Parameters Summary

| Parameter | Source-Reported Value | Operational Status |
| :--- | :--- | :--- |
| Candidate Universe | Nasdaq-100 constituents ($\ge 30$ ticker-days in 2021) | [source-reported] |
| Active Universe Size | 61 stocks | [source-reported] |
| Input Text Format | User-role chat template, pipe-joined headlines, $\le 512$ tokens | [source-reported] |
| Decoding Method | Greedy decoding, temperature=0, seed=42 | [source-reported] |
| Confidence Mapping | Isotonic regression on 2021 calibration set | [source-reported] |
| Holding Horizon ($h$) | 5 trading sessions (overlapping daily cohorts) | [source-reported] |
| Target Volatility | 5.0% annualized pre-cost | [source-reported] |
| Per-Name Position Cap | $\pm 10\%$ of portfolio equity | [source-reported] |
| Gross Leverage Cap | $100\%$ (1.0x gross exposure) | [source-reported] |
| Transaction Cost | 5.0 bps (0.0005) one-way per position turnover | [source-reported] |
| Borrow Cost | 0 bps baseline (1%–3% annual tested in robustness) | [source-reported] |
| Risk-Aversion Coeff ($\gamma$) | 3.0 in $\mathrm{CER}_\gamma = 252(\bar{r} - \frac{\gamma}{2}\operatorname{Var}(r))$ | [source-reported] |
| Execution Fill Model | Market-on-open at session $T$ open | [source-reported] |
| Slippage Model | Zero additional slippage beyond 5 bps fee | `[research-proposed]` |
| Missing Headline Action | Zero new cohort entry; existing cohorts mature | `[research-proposed]` |

## Required data

- **Universe Definition:** 61 US equities from the Nasdaq-100 constituent list as of January 2021, filtered for minimum 30 ticker-day headline observations in 2021 calibration [source-reported]. Excludes post-2021 additions and acquired/delisted names without vendor data [source-reported].
- **Market Type & Venue:** US Equity Spot Markets (NASDAQ / NYSE) [source-reported].
- **Data Vendors:**
  - FactSet Professional Newswire: English-language US-equity wire headlines, source prefixes stripped, routine ownership/calendar notices filtered [source-reported].
  - FactSet Equity Prices: Open, High, Low, Close, Volume, adjusted for splits and corporate dividend distributions [source-reported].
- **Observation Frequency:** Daily ticker-level bundles (mean 4.17 headlines per bundle, median 2) [source-reported].
- **Point-in-Time Integrity:** Strict publication timestamp boundary: any headline bundle dated $D$ is traded at session $T$ open ($T > D$), guaranteeing no look-ahead bias and no same-session leakage [source-reported].
- **Model Checkpoints:** 9 open-weight HuggingFace models spanning 7B to 32B parameters across 5 architecture families [source-reported]:
  - Qwen2.5 (7B, 14B, 32B)
  - Gemma-2-9B, Gemma-3-27B
  - Mistral (7B, 24B)
  - Phi-4 (14B)
  - FinLLaMa (8B)
  - Quantization: $\ge 24$B parameters run in int8; $< 24$B run in unquantized float16 [source-reported].
- **Missing Data Handling:** Regex parsing failures on LLM output (2.6%–3.5%) are treated as missing observations and excluded from active signals; never forward-filled or imputed [source-reported].

## Execution assumptions

- **Execution Mechanism:** Simulated programmatic portfolio rebalancing executed at market open [source-reported].
- **Signal-to-Order Latency:** Next-session open execution (overnight news processed before 09:30 EST market open) [source-reported].
- **Order Type:** Market-on-open (MOO) [source-reported].
- **Fill Price:** Exact open price of session $T$ [source-reported].
- **Transaction Costs:** Flat 5.0 bps (0.05%) one-way per unit of turnover charged against portfolio equity [source-reported].
- **Slippage:** Assumed zero beyond the 5 bps fee [source-reported]; sensitivity analysis to 5–25 bps slippage is research-proposed `[research-proposed]`.
- **Borrow & Short Availability:** Short positions assume unconstrained locate availability at 0 bps borrow fee in baseline [source-reported]; sensitivity checks confirm stability under 1%–3% annual short borrow fee [source-reported].
- **Leverage & Margining:** Unleveraged long/short portfolio strictly capped at 1.0x gross leverage (mean realized daily gross exposure was 85.2%, 95th percentile 98.1%, max 99.8%) [source-reported].
- **Capacity:** Large-cap Nasdaq-100 universe provides deep liquidity; unconstrained in paper simulation, estimated institutional capacity $\ge \$100\text{M}$ before market impact degrades 5-session drift `[research-proposed]`.

## Evidence

### Source-reported

1. **Ordinal Decisions & Rank Invariance (Section 5, arXiv:2609.00187v1):**
   - Two-token logit softmax produces extreme overconfidence saturation (vocabulary logits differ by 20+ nats, raw confidence $\approx 0.97$–$0.98$, initial ECE $\approx 0.47$) [source-reported].
   - Temperature scaling calibrates ECE to 0.03–0.04 but strictly preserves rank order [source-reported].
   - Exact bijection confirms 0 discrepancies in coverage-matched selection across all 18 configurations and 20 coverage levels (5% to 100%) [source-reported].
   - Low Brier resolution: $\operatorname{RES}/\operatorname{UNC}$ ranges from $0.07\%$ to $0.40\%$, while base classifier accuracy is weak (50.3%–51.8% vs. 53.8% base rate) [source-reported].
   - Fixed-threshold gating: 0 of 18 configurations survive Romano-Wolf stepdown correction for accuracy tuning, and 0 of 18 survive Holm correction for CER tuning [source-reported].
2. **Cardinal Sizing: Nine-Model Grid Evaluation (Table 1 & Table 6 in HTML, arXiv:2609.00187v1):**
   - Evaluated out-of-sample on 2022–2023 (505 trading sessions, 31,888 ticker-days) with maps and scales fitted on 2021 [source-reported].
   - **Model-Ensemble (Joint):**
     - Raw CER: $+2.7$ pp/yr [source-reported]
     - Matched CER: $+12.0$ pp/yr [source-reported]
     - $\Delta \text{CER}$: $+9.2$ pp/yr (95% CI $[4.1, 14.6]$, joint bootstrap $p < 0.001$) [source-reported]
     - Realized Volatility: falls from $8.8\%$ (raw) to $7.8\%$ (matched) [source-reported]
     - Sharpe Ratio: increases from $0.44$ to $1.64$ [source-reported]
     - Component Attribution: $+9.0$ pp/yr from mean return, $+0.2$ pp/yr from variance reduction [source-reported]
   - **Individual Model Results (Raw CER $\to$ Matched CER, $\Delta \text{CER}$, 95% CI, Volatility):**
     - `Qwen2.5-7B`: $-25.5 \to +14.2$ pp/yr, $\mathbf{+39.7^{**}}$ ($[24.5, 56.1]$), Vol $12.3\% \to 7.3\%$ [source-reported]
     - `Gemma-2-9B`: $+11.5 \to +16.0$ pp/yr, $+4.5$ ($[0.1, 9.2]$), Vol $9.5\% \to 8.7\%$ [source-reported]
     - `Mistral-7B`: $+10.0 \to +11.1$ pp/yr, $+1.1$ ($[-3.6, 5.8]$), Vol $9.3\% \to 8.3\%$ [source-reported]
     - `FinLLaMa`: $+10.0 \to +10.4$ pp/yr, $+0.3$ ($[-1.9, 2.7]$), Vol $11.2\% \to 10.7\%$ [source-reported]
     - `Mistral-24B`: $-0.3 \to +10.3$ pp/yr, $\mathbf{+10.6^{**}}$ ($[4.5, 17.1]$), Vol $9.5\% \to 8.5\%$ [source-reported]
     - `Phi-4`: $-0.8 \to +10.0$ pp/yr, $+10.8$ ($[1.1, 20.4]$), Vol $10.4\% \to 7.8\%$ [source-reported]
     - `Qwen2.5-14B`: $+9.9 \to +10.5$ pp/yr, $+0.6$ ($[-5.9, 7.2]$), Vol $9.1\% \to 8.0\%$ [source-reported]
     - `Gemma3-27B`: $-0.8 \to +14.0$ pp/yr, $\mathbf{+14.8^{**}}$ ($[6.5, 23.7]$), Vol $9.2\% \to 7.8\%$ [source-reported]
     - `Qwen2.5-32B`: $+7.8 \to +9.9$ pp/yr, $+2.1$ ($[-3.9, 8.3]$), Vol $8.9\% \to 8.0\%$ [source-reported]
   - 3 of 9 models individually survive family-wise Holm correction (`Qwen2.5-7B`, `Mistral-24B`, `Gemma3-27B`) [source-reported].
   - Excluding `Qwen2.5-7B`, the ensemble effect remains positive and statistically significant: $+5.5$ pp/yr (95% CI $[1.0, 10.1]$, $p=0.015$) [source-reported].
   - Alternative calibrators: Beta regression gives $+9.4$ pp/yr (CI $[4.9, 14.3]$) with 5 of 9 models Holm-significant [source-reported].
3. **Four-System Factorial Decomposition & Portability Diagnosis (Section 6.1, Table 3):**
   - Applying correctness-map scale $\kappa_c$ to raw map reduces CER in 8 of 9 models and inflates test volatility to $11.8\%$ (vs. $8.4\%$ intended) [source-reported].
   - Applying raw-map scale $\kappa_r$ to correctness map compresses test volatility to $3.3\%$ (vs. $9.8\%$ intended) [source-reported].
   - Model-ensemble map-scale interaction term: $+17.1$ pp/yr [source-reported].
   - Qwen2.5-7B case study: raw system realized $11.7\%$–$13.8\%$ volatility against the $5\%$ calibration target, running at 2.3x–2.8x intended risk [source-reported].
4. **Adaptive-Volatility Controller Interaction (Table 2 & Table 3):**
   - Under online adaptive-volatility controller (re-scaling $\kappa$ in 21-session blocks):
     - Raw system CER: $+6.6$ pp/yr (Sharpe 1.42, Vol 4.9%) [source-reported]
     - Correctness-mapped CER: $+8.2$ pp/yr (Sharpe 1.86, Vol 4.6%) [source-reported]
     - Incremental gain falls to $+1.6$ pp/yr (95% CI $[-0.8, 4.1]$, $p=0.195$, statistically insignificant) [source-reported].
     - Paired test confirms significant controller interaction: $+7.78$ pp/yr (95% CI $[2.01, 15.25]$, $p < 0.001$) [source-reported].
5. **Mechanism Verification (Common-Support & Shuffled Labels, Table 3):**
   - Forcing common trade support (replacing zeros with smallest positive size) yields $+8.5$ pp/yr vs. $+3.9$ pp/yr for gate-only, proving common-support recovers $93\%$ of the gain and magnitude reallocation dominates filtering [source-reported].
   - 300 shuffled-label refits: observed $+9.2$ pp exceeds 299/300 draws ($p=0.0066$, excess $+3.6$ pp); within-date shuffled refits exceed 300/300 draws ($p=0.0033$, excess $+3.2$ pp) [source-reported].
   - Newey-West factor regression against tech, momentum, and volatility terciles leaves an unexplained intercept of $+8.6$ pp/yr (95% CI $[3.2, 14.1]$) [source-reported].
6. **Temporal Walk-Forward Attenuation (2024–2025 Extension, Table 4):**
   - Evaluated across 4 annual walk-forward folds on 12,911 ticker-days (5 models):
     - Isotonic: $\Delta \text{CER} = +1.17$ pp/yr (95% CI $[-0.60, 3.06]$, $p=0.144$, Holm $p=0.144$) [source-reported]
     - Beta: $\Delta \text{CER} = +1.50$ pp/yr (95% CI $[0.30, 2.70]$, $p=0.019$, Holm $p=0.058$) [source-reported]
     - Platt: $\Delta \text{CER} = +0.67$ pp/yr (95% CI $[-0.26, 1.61]$, $p=0.061$, Holm $p=0.123$) [source-reported]
     - Zero calibrators survive family-wise Holm correction [source-reported].
   - Attenuation coincides with Brier resolution collapsing from $0.17\%$–$0.19\%$ (2022–2023) to $0.04\%$–$0.08\%$ (2024–2025) [source-reported].

### Independently reproduced

Not independently reproduced. All empirical findings, bootstrap confidence intervals, and econometric coefficients are third-party results reported by Singh and Rezaeimanesh (2026, arXiv:2609.00187v1). No internal simulation has been conducted in PyBroker or NautilusTrader.

### Negative evidence

1. **Failure of Calibration to Alter Ordinal Decisions:**
   Temperature scaling, Platt scaling, and strictly increasing monotonic transforms have zero ability to alter rank-based decisions or improve top-$k$ stock selection [source-reported].
2. **Extreme Classifier Weakness:**
   Underlying open-weight LLMs have near-random single-session accuracy (50.3%–51.8%), underperforming the unconditioned baseline of 53.8% [source-reported].
3. **Regime & Sector Fragility:**
   Gains are heavily concentrated in the 2022 bear market (+16.2 pp/yr, $p < 0.001$) and non-tech tickers (+13.9 pp/yr, $p = 0.002$); performance during the 2023 tech-led bull market was statistically flat [source-reported].
4. **Decay in Walk-Forward Out-of-Sample Periods:**
   During the 2024–2025 temporal extension, the matched calibration effect drops to +1.17 pp/yr and fails Holm significance, driven by rapid signal erosion and resolution collapse [source-reported].
5. **Redundancy under Adaptive Volatility Targeting:**
   When an adaptive volatility controller is active, the incremental value of matched correctness calibration collapses to +1.6 pp/yr ($p = 0.195$), demonstrating that 83% of the static matched gain (+7.78 of +9.2 pp/yr) was merely repairing the mis-scaling of a rigid frozen controller [source-reported].

## Falsification plan

The following operational empirical tests are designed to disprove or invalidate the strategy hypothesis:

1. **Adaptive Controller Redundancy Benchmark:**
   - *Data:* Full 2021–2023 FactSet / Nasdaq-100 dataset `[research-proposed]`.
   - *Methodology:* Run a paired block-bootstrap comparison between the raw-confidence system with an online 21-day adaptive-volatility controller and the matched-calibration system with frozen-scale control `[research-proposed]`.
   - *Falsification Threshold:* If the CER difference between matched-calibration and the raw adaptive-volatility benchmark is $< +2.0$ pp/yr with two-sided bootstrap $p \ge 0.05$, the hypothesis that confidence calibration provides independent structural alpha is falsified (proving the effect is solely an artifact of controller rigidity) `[research-defined falsification threshold]`.
   - *Action on Failure:* Retire confidence recalibration modules and standardize on adaptive volatility targeting.
2. **Out-of-Sample Walk-Forward Resolution Hurdle:**
   - *Data:* Out-of-sample data covering 2024–2026 across Nasdaq-100 constituents `[research-proposed]`.
   - *Methodology:* Evaluate annual walk-forward folds with rolling 1-year calibration windows `[research-proposed]`.
   - *Falsification Threshold:* If realized Brier resolution $\operatorname{RES}/\operatorname{UNC} < 0.05\%$ or realized out-of-sample CER net of 5 bps costs is $\le 0.0$ pp/yr across two consecutive annual folds, the sentiment alpha signal is deemed dead/decayed `[research-defined falsification threshold]`.
   - *Action on Failure:* Reject deployment of open-weight LLM newswire sentiment models.
3. **Execution Slippage & Latency Stress Test:**
   - *Data:* 2022–2023 evaluation sample `[research-proposed]`.
   - *Methodology:* Sweep round-trip transaction costs from 5 bps up to 25 bps (modeling market impact and spread) and shift execution from market-on-open (09:30 EST) to VWAP over the first 30 minutes (09:30–10:00 EST) `[research-proposed]`.
   - *Falsification Threshold:* If the matched ensemble CER collapses to $\le 0.0$ pp/yr at round-trip transaction friction $\le 12$ bps, the alpha is falsified as an unexecutable friction illusion `[research-defined falsification threshold]`.
   - *Action on Failure:* Reclassify as unviable for live execution.

## Crypto portability

**unproven**

The mechanism originates strictly from US equity newswire analysis (Nasdaq-100) and has not been demonstrated in crypto markets [source-reported]. Any crypto port must be classified as unproven research interpretation `[research-proposed]`.

Portability considerations and structural barriers:
1. **Continuous 24/7 Session Boundaries:**
   US equity trading relies on discrete overnight information accumulation and a synchronized market-on-open (MOO) liquidity pool. Crypto trades continuously 24/7/365 without market open auctions. Establishing an equivalent discrete 5-session cohort structure requires imposing arbitrary UTC cutoff windows (e.g. 00:00 UTC daily rebalancing), introducing execution boundary sensitivity `[research-proposed]`.
2. **Information Feed Fragmentation & Noise:**
   Unlike curated institutional newswires (FactSet), crypto sentiment is dominated by social feeds (Twitter/X, Telegram, Discord) plagued by coordinated spam, sybil campaigns, and bot volume. Empirical LLM Brier resolution on unstructured crypto social feeds is expected to be substantially lower than the already marginal $0.07\%–0.40\%$ observed on FactSet wires `[research-proposed]`.
3. **Perpetual Funding Drag:**
   Holding 5-day directional positions on crypto perpetual futures incurs 8-hour funding payments. In persistent bull or bear regimes, funding rates of 10–30 bps/day would completely consume the +1.6 to +2.7 pp/yr gross CER edge `[research-proposed]`.
4. **Volatility Scaling Extreme:**
   Nasdaq-100 constituent annualized volatility is 15%–25%, whereas altcoin perpetuals exhibit 70%–120% annualized volatility. Sizing rules targeting 5% portfolio volatility would force exposure scale $\kappa$ down by an order of magnitude ($\kappa < 0.05$), severely compressing active capital efficiency `[research-proposed]`.

## Limitations

- **Weak Base Predictor:** Base model directional accuracy is only 50.3%–51.8%, barely differing from random chance.
- **Model Contamination Risk:** All nine evaluated models were released after the 2022–2023 test period; while anonymization tests show no drop, pretraining exposure to macro narratives cannot be ruled out.
- **Zero Ordinal Impact:** Monotone calibration has zero utility for screening, filtering, or ranking tokens/equities.
- **Extreme Bear Market Concentration:** Essentially all excess performance occurred in 2022; the strategy delivered near-zero alpha in 2023.
- **Alpha Decay:** Rapid signal erosion documented in 2024–2025 extension, with Brier resolution falling below 0.08%.
- **Controller Redundancy:** 83% of the matched calibration benefit is captured by simple adaptive volatility targeting.
- **Data Gap:** FactSet wire items lack intraday millisecond timestamps, requiring a full-day execution delay to prevent look-ahead bias.
- **Not Independently Reproduced.**

## Implementation status

not-implemented

This strategy framework has not been implemented or backtested in PyBroker or NautilusTrader. No live data feeds, LLM inference endpoints, or automated broker connections exist in the repository.

## Adoption boundary

research-only

This record is research material only. Its presence in this repository does not constitute:
- validated or profitable alpha;
- approval for implementation;
- authorization for paper trading, testnet execution, or live capital deployment.

## Related Wiki records

- `[[quant/prediction-market-llm-confidence-weighted-value-bet-2026-09-04]]` — LLM confidence-weighted betting on order books; complementary examination of confidence calibration in predictive markets.
- `[[quant/llm-strategy-discovery-leakage-safe-search-deflated-eval-2026-09-04]]` — Methodological audit for leakage, look-ahead bias, and search deflation in LLM strategy discovery.
- `[[quant/regret-driven-portfolio-ftl-llm-hedging-sentiment-gated-2026-09-05]]` — Follow-the-leader online portfolio optimization with sentiment risk gating.
- `[[quant/factorengine-program-level-knowledge-infused-factor-mining-2026-09-05]]` — Program-level factor mining framework for quantitative investment.

## Sources

1. Singh, R., & Rezaeimanesh, S. (2026). "Ordinal Gates, Cardinal Bets: Matching LLM Confidence to the Financial Decision Operator." *arXiv preprint arXiv:2609.00187v1 [q-fin.PM]*, submitted August 31, 2026, announced September 1, 2026. Stable URL: `https://arxiv.org/abs/2609.00187`. Full text HTML: `https://arxiv.org/html/2609.00187v1`.
2. Murphy, A. H. (1973). "A New Vector Partition of the Probability Score." *Journal of Applied Meteorology*, 12(4), 595–600.
3. DeGroot, M. H., & Fienberg, S. E. (1983). "The Comparison and Evaluation of Forecasters." *The Statistician*, 32(1–2), 12–22.
4. FactSet Research Systems (2021–2025). FactSet Professional Newswire & US Equity Pricing Database.
