---
schema: strategy-research-record-v1
title: "VST: Verifiable Structured Transport for Auditable Agent-to-Agent Alpha Discovery"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - agentic-alpha-discovery
  - multi-agent-systems
  - speculative-execution
  - verifiable-structured-transport
  - formulaic-alpha
  - china-a-shares
  - csi1000
  - transactional-verification
status: research-only
confidence: high
source_as_of: 2026-09-07
sources:
  - "Yuqi Li, Siyuan Liu, and Bingjun Liu, 'VST: Verifiable Structured Transport for Auditable Agent-to-Agent Alpha Discovery', arXiv:2609.07065v1 [cs.AI], submitted September 7, 2026. Stable URLs: https://arxiv.org/abs/2609.07065, https://arxiv.org/html/2609.07065v1, https://arxiv.org/pdf/2609.07065, DOI: 10.48550/arXiv.2609.07065"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# VST: Verifiable Structured Transport for Auditable Agent-to-Agent Alpha Discovery

## Provenance

- **Primary Source:** Yuqi Li, Siyuan Liu, and Bingjun Liu (Panda AI, `{libubai, liusiyuan, liubingjun}@pandaai.online`), *"VST: Verifiable Structured Transport for Auditable Agent-to-Agent Alpha Discovery"*, arXiv preprint `arXiv:2609.07065v1 [cs.AI]`, submitted September 7, 2026 (`source-reported`).
  - Abstract URL: [https://arxiv.org/abs/2609.07065](https://arxiv.org/abs/2609.07065)
  - Full-Text HTML URL: [https://arxiv.org/html/2609.07065v1](https://arxiv.org/html/2609.07065v1)
  - Full-Text PDF URL: [https://arxiv.org/pdf/2609.07065](https://arxiv.org/pdf/2609.07065)
  - Canonical DOI: [10.48550/arXiv.2609.07065](https://doi.org/10.48550/arXiv.2609.07065)
  - License: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) (`source-reported`).
- **Verification Integrity:** The complete full-text manuscript and mathematical derivations of `arXiv:2609.07065v1` were directly retrieved and audited. Every equation, envelope schema field, multi-horizon prediction head, four-level short-circuit validation gate ($L_1$--$L_4$), transactional commit/rollback rule, ablation metric, and out-of-sample empirical statistic traces directly to the text, Equations (1)--(16), Tables 1--9, and Appendices A--B of `arXiv:2609.07065v1`. No search-result snippets, secondary summaries, or model-generated synthetic aggregations were used to formulate strategy mechanics or empirical findings.
- **Repository Deduplication Audit:** A comprehensive audit of all records in `alpha-strategy-research` confirmed zero existing records matching `arXiv:2609.07065`, the title, Yuqi Li, Siyuan Liu, Bingjun Liu, or Verifiable Structured Transport. While co-author Yuqi Li previously co-authored an unrelated work on plan-space semantic representations (`alphaschema-trading-semantic-plan-space-surrogate-guided-factor-mining-2026-09-05.md` based on Yi et al. 2026, arXiv:2607.26642), that earlier record focused on offline LightGBM surrogate evaluation over discrete AST semantic tuples $(e, c, Q, d, o)$ without inter-agent communication protocols, multi-horizon trajectory forecasting, speculative execution, or transactional verification gates. VST constitutes a distinct, independent research capture.

## Economic mechanism

### Source-reported

1. **The Serial Communication Bottleneck in Multi-Agent Alpha Mining:**
   Contemporary multi-agent alpha discovery frameworks (such as coupled dual-loop systems where a research report agent coordinates an alpha-mining loop and an evaluation-optimization loop) spend the vast majority of wall-clock runtime waiting for sequential agent-to-agent (A2A) feedback cycles rather than in raw inference execution (`source-reported`). In each cycle, an AlphaMiner proposes candidate factor expressions, three independent AlphaEvaluator instances perform backtesting and write diagnostic briefs, while an EvaluationMiner proposes metric-set and portfolio adjustments evaluated by three FactorMetricsEvaluators. When iterated over hundreds or thousands of cycles, inter-agent coordination through free-form natural language imposes severe structural limitations:
   - Hand-offs lack immutable contracts and cannot be deterministically replayed as causal trajectories.
   - The system cannot forecast future multi-cycle guidance states.
   - Speculative acceleration is impossible without exact, leak-proof state rollback mechanisms.
   - Evaluator prompts risk being anchored or contaminated by unverified speculative forecasts, destroying the statistical independence of the quality gate.

2. **The VST Architecture and Verify-Then-Commit Discipline:**
   VST replaces the untyped prose communication channel with a four-part architectural paradigm (`source-reported`):
   - **Structured Inter-Agent Transport (C1):** Every message is wrapped in a three-layer packet: an `A2AEnvelope` (identity, deterministic unicast routing, causal state addressability, and visibility typing), a native typed body payload $x_{f(m)}$, and an immutable transactional provenance block $p$ (tracking origin $\in \{\text{observed}, \text{speculative}\}$, transaction ID, and commit status).
   - **Multi-Horizon Trajectory Prediction (C2):** A single shared-encoder policy (gpt-oss-120b with LoRA adaptation) equipped with four specialized typed heads directly forecasts the accumulated structured guidance bundle $\widehat{B}_{t,k}$ that the two miners would receive over the next $k \ge 2$ ordinary cycles ($k \in \mathcal{K} = \{2, 4, \dots, K_{\max}\}$), along with a calibrated success confidence $q_{t,k}$ and epistemic uncertainty $u_{t,k}$. The bundle forecasts:
     - $\widehat{A}_{t,k}^{\alpha}$: Report advice string to AlphaMiner;
     - $\widehat{\bar{R}}_{t,k}^{\alpha}$: Aggregated evaluator brief to AlphaMiner;
     - $\widehat{A}_{t,k}^{\mathrm{eval}}$: Report advice string to EvaluationMiner;
     - $\widehat{\bar{R}}_{t,k}^{\mathrm{eval}}$: Aggregated evaluator brief to EvaluationMiner.
   - **Transactional Verification and Leap Control (C3):** Rather than blindly accepting predictions, the controller opens a scratch transaction, executes real miners and blinded evaluators on the speculative guidance, and subjects the resulting outputs to a 4-level short-circuit validation gate:
     - $L_1$: Bundle legality and route policy;
     - $L_2$: Actual-output executability and cross-loop referential consistency;
     - $L_3$: Blinded evaluator risk (worst-case severity aggregation);
     - $L_4$: Empirical development quality gate ($Q_{\alpha,d}$ and $Q_{m,d}$).
     If all four levels pass, the speculative leap is committed atomically ($C_t = 1$), skipping $k-1$ ordinary feedback cycles. If any level fails, the mutable scratch state is rolled back completely ($C_t = 0$), restoring prior state $S_t$ with zero trajectory corruption, while retaining the failed trial as a negative training sample for the predictor.
   - **Separated Skill Co-Evolution (C4):** The predictor's skill library evolves via transactional reinforcement learning ($r_t$) while evaluator diagnostic rubrics evolve independently. Evaluator prompts never receive predictor tokens, horizons, confidences, or speculative flags, preventing reward-hacking and forecast anchoring by construction.

3. **Core Architectural Insight:**
   A critical empirical finding of the authors' ablation study is that *structured transport does not improve predictive accuracy over an equal-information free-text channel* (both achieve an identical 0.975 committed leap hit rate). Rather, the value of structured transport is *correctness, deterministic replayability, and leakage prevention by construction*, enabling auditable speculative acceleration and out-of-sample search robustness without sacrificing predictive fidelity.

### Research interpretation

- **Structural Guardrails as an Overfitting Antidote:**
  In automated quantitative research, LLM-based generators frequently overfit in-sample validation metrics when granted unconstrained feedback loops. By forcing all multi-agent hand-offs through rigid visibility contracts and enforcing a four-level gate that includes blinded evaluator risk and cross-loop referential consistency, VST prevents exploratory shortcuts (e.g., metric manipulation or portfolio cherry-picking) from leaking across loop boundaries.
- **Speculative Decoupling vs. Monolithic Search:**
  Treating multi-cycle guidance as a speculative transaction decouples factor generation speed from evaluator verification thoroughness. Evaluators maintain rigorous, compute-heavy backtesting standards while the predictor skips uninformative intermediate iteration cycles, concentrating computational budget on semantically validated state transitions.
- **Generalization Across Market Regimes:**
  The paper demonstrates that while individual factors generated under VST exhibit lower raw correlation (IC) than aggressive genetic programming or MCTS baselines, they experience substantially lower out-of-sample degradation. The multi-agent search converges toward structural economic expressions rather than transient in-sample noise anomalies.

## Signal

The signal generation pipeline produces an ensemble cross-sectional alpha ranking across tradeable equities by executing formulaic alpha expressions discovered and selected through the VST-guided dual loop (`source-reported` framework; specific factor execution and portfolio weights `research-proposed`):

1. **Factor Expression Space and Primitives (`source-reported`):**
   - Candidate alpha factors $f(x)$ are symbolic mathematical expressions over price-volume tensor data generated by AlphaMiner (interfaced through Qlib).
   - Operators include time-series rolling operators (`ts_mean`, `ts_std`, `ts_corr`, `ts_rank`, `ts_decay_linear`), cross-sectional operators (`cs_rank`, `cs_zscore`), and element-wise arithmetic operators.
   - Candidate validity filter (`source-reported`): A factor expression is admitted to the active factor pool if and only if it achieves backtest Sharpe $\ge 1.0$ and annualized excess return $\ge 0.05$ on the validation split.

2. **The 4-Channel Speculative Guidance Target (`source-reported`, Eq. 4--5):**
   The trajectory predictor forecasts the accumulated miner guidance bundle $\widehat{B}_{t,k} = (\widehat{A}_{t,k}^{\alpha}, \widehat{\bar{R}}_{t,k}^{\alpha}, \widehat{A}_{t,k}^{\mathrm{eval}}, \widehat{\bar{R}}_{t,k}^{\mathrm{eval}})$ across horizons $k \in \{2, 4, \dots, K_{\max}\}$:
   - Aggregator dispatch ($\mathrm{Aggregate}(Z_{t+1:t+k}|_{B})$, Appendix A):
     - Set-valued fields: Accumulate additions/removals in cycle order; resolve repeated promote/demote decisions by recency weighted by supporting cycle count.
     - Numeric/bounded categorical fields: Retain latest value clipped to declared schema range.
     - String advice fields: Retain most recent committed text.
   - Routing constraint (`source-reported`): Packets are addressed strictly to `alpha_miner` (mapping $\widehat{A}_{t,k}^{\alpha} \to \texttt{rr\_advise}$, $\widehat{\bar{R}}_{t,k}^{\alpha} \to \texttt{failure\_feedback}$) and `evaluation_miner` (mapping $\widehat{A}_{t,k}^{\mathrm{eval}} \to \texttt{rr\_advise}$, $\widehat{\bar{R}}_{t,k}^{\mathrm{eval}} \to \texttt{evaluator\_feedback}$).

3. **Four-Level Verification Gate ($L_1$--$L_4$, `source-reported`, Eq. 10--14):**
   A speculative transition from parent state $S_t$ across horizon $k_t$ is committed ($C_t = 1$) if and only if all four short-circuit gates pass:
   - **$L_1$ (Legality and Route Policy):**
     $$V_1 = \mathbf{1}\left[\widehat{B}_{t,k} \models \mathcal{S}_B \wedge \mathrm{targets}(\widehat{B}_{t,k}) = \{\texttt{alpha\_miner}, \texttt{evaluation\_miner}\}\right]$$
     Rejects malformed fields, stale parent IDs, $k < 2$, or any evaluator-targeted routing.
   - **$L_2$ (Output Validity and Cross-Loop Consistency):**
     $$V_2 = \mathbf{1}\left[O_t^\alpha \models \mathcal{S}_\alpha \wedge O_t^{\mathrm{eval}} \models \mathcal{S}_{\mathrm{eval}} \wedge \mathrm{CrossConsistent}(O_t^\alpha, O_t^{\mathrm{eval}}, S_t)\right]$$
     Verifies: (i) every factor evaluated in $O_t^{\mathrm{eval}}$ exists in $O_t^\alpha$; (ii) metric set named in $O_t^{\mathrm{eval}} \subseteq$ admissible metrics at $S_t$; (iii) portfolio in $O_t^{\mathrm{eval}}$ contains only executable alpha factors passing alpha-side syntax checks.
   - **$L_3$ (Blinded Evaluator Risk):**
     $$V_3 = \mathbf{1}\left[\mathrm{RiskAgg}(E_{t,1:3}^\alpha) \le \tau_\alpha \wedge \mathrm{RiskAgg}(E_{t,1:3}^{\mathrm{metrics}}) \le \tau_m\right]$$
     $\mathrm{RiskAgg}$ aggregates the 3 independent evaluator instances using worst-case severity (a single critical finding cannot be averaged away by two lenient ones; $\tau_\alpha, \tau_m$ `source-reported` development thresholds).
   - **$L_4$ (Empirical Development Quality Gate):**
     $$V_4 = \mathbf{1}\left[\min_{d} Q_{\alpha,d}(O_t^\alpha) \ge \tau_g \wedge \min_{d} Q_{m,d}(O_t) \ge \tau_p\right]$$
     Evaluated on development splits $d \in \{\text{train-gate}, \text{leap-valid}\}$, where $Q_{\alpha,d}$ combines IC/RankIC stability and $Q_{m,d}$ evaluates return, risk, monotonicity, and cost proxies.
   - **Commit Action:** $C_t = \prod_{\ell=1}^4 V_\ell$. If $C_t = 1$, atomic state commit; if $C_t = 0$, scratch namespace deleted, rollback to $S_t$, execute 1 baseline cycle.

4. **Composite Portfolio Selection (`source-reported`):**
   - Candidate portfolios are constructed from the factor pool using cross-sectional quantile grouping (10 groups).
   - Portfolio selection rule (`source-reported`): Rank candidate portfolios strictly on development-split (test segment) backtest Sharpe ratio and select the top-$K$ portfolios ($K \in \{5, 10, 20\}$).
   - Cross-sectional position weighting (`research-proposed`): Long top decile (Group 10), short bottom decile (Group 1), equal-weighted within quantile bins, rebalanced daily at market open.

## Required data

- **Asset Universe:** China A-Share CSI 1000 index constituents (`ZZ1000`), representing 1,000 liquid small-to-mid capitalization listed equities (`source-reported`).
- **Data Splits (`source-reported`):**
  - Disjoint temporal partitions: Training split (alpha factor mining and supervised adapter training), Validation split (evaluator self-check, candidate gate filtering, top-$K$ selection), Test split (meta-review optimization horizon and portfolio development ranking), and Holdout split (strictly isolated out-of-sample performance evaluation).
  - *Provenance Note:* Exact calendar date boundaries are specified inside `config_formal_v1.yaml` (part of the experimental software configuration) rather than printed as explicit strings in the paper text; the text guarantees all splits are non-overlapping and holdout is never touched by any agent, gate, or horizon selection (`source-reported`).
- **Data Fields (`source-reported` via Qlib platform):**
  - Daily OHLCV price-volume bars: `open`, `high`, `low`, `close`, `volume`, `amount`, and backward-adjusted factor data (`adj_factor`).
  - Cross-sectional return benchmark: CSI 1000 index daily return series.
- **Point-in-Time Integrity:** All factor inputs use strictly point-in-time adjusted closing and opening prices; no look-ahead or forward-fill across temporal splits (`source-reported`).

## Execution assumptions

- **Execution Model (`source-reported`):** Standard Qlib 10-group backtest evaluator.
- **Gross Evaluation Baseline (`source-reported`):** All performance metrics reported in the primary paper are *gross of transaction costs, slippage, and turnover constraints*. The authors explicitly state that net-of-cost evaluation on small/mid-cap equities (CSI 1000) will suffer significant friction from spreads, market impact, and China's sell-side stamp duty (0.05% to 0.10%), noting this as an explicit limitation (`source-reported`).
- **Operational Trading Rules (`research-proposed` implementation specification):**
  - Rebalance frequency: Daily at the market open using the prior day's close-generated alpha signals (`research-proposed`).
  - Execution price: VWAP over the first 30 minutes or open price (`research-proposed`).
  - Commission and slippage model (`research-proposed`): 5 bps one-way trading fee + 5 bps execution slippage + 10 bps stamp duty on sells.
  - Position limits (`research-proposed`): 100% gross exposure, dollar-neutral (100% long Group 10, 100% short Group 1), maximum single-stock weight capped at 1.0%.

## Evidence

### Source-reported

1. **Out-of-Sample Holdout Factor Performance (Table 2, Matched Budget of 500 Valid Factors, `source-reported`):**
   Across the untouched holdout partition, VST (OURS / M4) is the *only* method among eight examined to achieve a positive median annualized return and positive median Sharpe ratio:
   - **OURS (M4):** Valid factors $n=499$; Fraction with Sharpe $>1$: $0.313$ (31.3%); Median Annualized Return: $\mathbf{+0.059}$ (+5.9%); Median Sharpe: $\mathbf{+0.346}$; 95% Bootstrap CI: $[+0.207, +0.508]$ (entirely $>0$).
   - **B1 Alpha101 (Kakushadze 2016):** $n=14$; $P(\text{sh}>1)=0.000$; Med. AnnRet: $-0.078$; Med. Sharpe: $-0.396$; 95% CI: $[-0.91, +0.51]$.
   - **B2 GP (gplearn / AlphaGen):** $n=500$; $P(\text{sh}>1)=0.116$; Med. AnnRet: $-0.144$; Med. Sharpe: $-0.593$; 95% CI: $[-0.64, -0.52]$.
   - **B3 DSO/DSR (Petersen et al. 2021):** $n=500$; $P(\text{sh}>1)=0.010$; Med. AnnRet: $-0.287$; Med. Sharpe: $-1.648$; 95% CI: $[-1.71, -1.65]$.
   - **B4 AlphaGen (Yu et al. 2023):** $n=200$; $P(\text{sh}>1)=0.188$; Med. AnnRet: $-0.001$; Med. Sharpe: $-0.006$; 95% CI: $[-0.32, +0.13]$.
   - **B5 AlphaMCTS (Shi et al. 2025):** $n=500$; $P(\text{sh}>1)=0.160$; Med. AnnRet: $-0.015$; Med. Sharpe: $-0.056$; 95% CI: $[-0.30, +0.06]$.
   - **B6 AlphaAgent (Tang et al. 2025):** $n=500$; $P(\text{sh}>1)=0.220$; Med. AnnRet: $-0.005$; Med. Sharpe: $-0.021$; 95% CI: $[-0.21, +0.11]$.
   - **B7 Alpha-GPT (Wang et al. 2025):** $n=500$; $P(\text{sh}>1)=0.224$; Med. AnnRet: $-0.031$; Med. Sharpe: $-0.159$; 95% CI: $[-0.32, +0.01]$.
   - **Probability of Superiority $\hat{P}(\text{OURS} > \text{baseline})$:** $0.56$ vs B4, $0.58$ vs B5, $0.57$ vs B6, $0.57$ vs B7, $0.66$ vs B2, $0.87$ vs B3, $0.64$ vs B1.
   - *Benchmark Excess Return Gap:* Median excess return over CSI 1000 benchmark remains negative for all methods, with OURS suffering the smallest shortfall ($-0.028$).

2. **Portfolio-Level Out-of-Sample Performance (Table 3, `source-reported`):**
   Selected strictly by development-split (test split) Sharpe among 852 committed composite portfolios:
   - **Development-Top 20 Portfolios:** Median holdout Sharpe: $\mathbf{+0.71}$ (mean $+0.87$); Median holdout Annualized Return: $\mathbf{+13.3\%}$; Fraction with Sharpe $>0$: $80\%$; Fraction with Sharpe $>1$: $45\%$.
   - **Development-Top 10 Portfolios:** Median holdout Sharpe: $+0.48$; Median holdout Annualized Return: $+10.8\%$; $P(\text{sh}>0)=80\%$; $P(\text{sh}>1)=40\%$.
   - **Development-Top 5 Portfolios:** Median holdout Sharpe: $+0.26$; Median holdout Annualized Return: $+6.6\%$; $P(\text{sh}>0)=80\%$; $P(\text{sh}>1)=20\%$.
   - **All 852 Portfolios (Population Reference):** Median holdout Sharpe: $-0.23$; Median holdout Annualized Return: $-4.8\%$; $P(\text{sh}>0)=42\%$; $P(\text{sh}>1)=13\%$.
   - *Selection Signal Integrity:* Spearman rank correlation between test Sharpe and holdout Sharpe across all 852 portfolios is $+0.19$ (Pearson $+0.21$). Top quartile portfolios achieve holdout median Sharpe $+0.17$ vs bottom quartile $-0.43$.

3. **Matched Budget Top-$K$ Factors by Validation Sharpe (Table 4, `source-reported`):**
   - At $K=50$: GP reaches median Sharpe $+0.576$ vs OURS $+0.493$ ($P(\text{sh}>1)=0.388$).
   - At $K=100$: OURS leads with median Sharpe $\mathbf{+0.406}$ ($P(\text{sh}>1)=0.374$) vs GP $+0.423$, AlphaMCTS $+0.251$, AlphaGen $-0.069$.
   - At $K=200$: OURS leads with median Sharpe $\mathbf{+0.282}$ ($P(\text{sh}>1)=0.352$) vs AlphaMCTS $+0.236$, AlphaAgent $-0.001$, AlphaGen $-0.006$, GP $-0.369$.

4. **Multi-Metric Auxiliary Evaluation (Table 6, `source-reported`):**
   - Test Split: OURS Sharpe $+0.467$, AnnRet $+0.055$, ExcRet $-0.029$, IC $+0.016$, ICIR $+0.190$, IR $-0.432$. (AlphaMCTS achieves highest test Sharpe $+0.857$, IC $+0.042$).
   - Holdout Split: OURS achieves highest Sharpe ($\mathbf{+0.346}$), highest AnnRet ($\mathbf{+0.059}$), smallest excess return shortfall ($-0.028$), best IR ($-0.333$); Holdout IC is $+0.028$ (vs AlphaMCTS $+0.048$, AlphaGen $+0.037$) and ICIR is $+0.335$ (vs AlphaMCTS $+0.413$, AlphaGen $+0.356$).
   - *Key Interpretation:* VST produces factors with lower raw IC than AlphaMCTS or AlphaGen, but with superior risk-adjusted stability and substantially less out-of-sample drawdown decay.

5. **Transport Representation Ablation (Table 7 & 8, `source-reported`):**
   - Comparing full structured transport (`S-full`, 1646 rounds) against equal-information free-text transport (`S-off`, 1100 rounds):
     - Committed-leap hit rate: $0.9754$ (typed) vs $0.9749$ (free-text).
     - Mean committed horizon: $2.47$ (typed) vs $2.37$ (free-text).
     - LLM calls per round: $10.89$ (typed) vs $10.80$ (free-text).
     - Offline representation-probe alignment: $0.0528 \pm 0.0053$ (typed) vs $0.0547 \pm 0.0053$ (free-text).
     - Factor quality under same-round control ($\le 1100$ rounds): Holdout median Sharpe is $+0.098$ (typed) vs $+0.171$ (free-text); at top-100 development-ranked: $+0.274$ (typed) vs $+0.864$ (free-text).
     - *Verified Leap Breakdown:* Out of 1646 rounds, 1636 reached predictor transactions; 1308 committed, 33 rolled back, 295 were single-cycle fallbacks ($k < 2$). Net skipped guidance cycles: $\sum_t (k_t - 1) \approx 1924$.
     - *Rollback Distribution:* Gate $L_1$ rejected 0; Gate $L_2$ rejected 0; Gate $L_3$ (blinded evaluator risk) rejected 6; Gate $L_4$ (empirical development quality) rejected 27.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Turnover and Cost Friction Vulnerability (`source-reported`):** All empirical returns are reported gross of transaction costs. In small/mid-cap equities (CSI 1000), transaction costs, bid-ask spreads, and China's sell-side stamp duty create an estimated drag of 15--25 bps per rebalance. For high-turnover daily factor ensembles, net alpha may be substantially compressed or eliminated.
- **Population Median Inversion (`source-reported`):** Across the entire population of 852 candidate portfolios generated during the run, the unselected median holdout Sharpe is negative ($-0.23$), and median annualized return is $-4.8\%$. The strategy's positive return is strictly conditional on development-split ranking and selection; an unguided or un-gated ensemble fails out of sample.
- **Selection Benchmark Inflation Hazard (`source-reported`):** The expected maximum Sharpe achievable by chance over $N=852$ trials under normal return assumptions is $\mathrm{SR}_0 \approx 1.36$ on the development scale. While top-20 selected portfolios cleared this hurdle ($1.50$--$1.98$), deflated Sharpe corrections for selection breadth will substantially discount the reported $+0.71$ holdout Sharpe.
- **Null Predictive Advantage of Structured Typing (`source-reported`):** Structured transport confers zero measurable improvement in predictor hit rate ($0.9754$ vs $0.9749$) or raw factor quality over free-text communication. Adopting VST is unjustified if motivated purely by forecasting accuracy rather than governance, replay auditability, and safety.

## Falsification plan

1. **Transaction Cost and Stamp Duty Stress Test (`research-proposed`):**
   - *Test:* Apply realistic China A-share execution frictions (5 bps commission + 5 bps bid-ask half-spread + 10 bps stamp duty on sell legs) across the top-20 development-selected portfolios on the holdout split.
   - *Research-defined falsification threshold:* If net-of-cost median holdout Sharpe drops below $0.00$ or net annualized return becomes negative, falsify the tradability claim.
2. **Post-2024 Prospective Out-of-Sample Holdout (`research-proposed`):**
   - *Test:* Execute the frozen top-20 portfolios over a strictly out-of-sample temporal window spanning 2024-01-01 to 2026-08-31.
   - *Research-defined falsification threshold:* If fewer than 50% of the selected portfolios generate positive returns ($P(\text{sh}>0) < 0.50$) or if median Sharpe decays to $\le 0.10$, reject temporal persistence.
3. **Speculative Leakage Injection Test (`research-proposed`):**
   - *Test:* Artificially inject speculative forecast tokens and predictor horizon metadata into the prompt context of the six evaluators.
   - *Research-defined falsification threshold:* If evaluator rejection rate at $L_3$ decreases by $>30\%$ under identical factor inputs, confirm that unblinded evaluators suffer from forecast anchoring and reject gate independence.
4. **Randomized Guidance Placebo Test (`research-proposed`):**
   - *Test:* Replace the predictor's four-channel bundle $\widehat{B}_{t,k}$ with randomly sampled guidance strings and permuted evaluator briefs.
   - *Research-defined falsification threshold:* If the randomized controller achieves a commit rate $>50\%$ through gates $L_1$--$L_4$, reject the selectivity of the verification gate.

## Crypto portability

- **Portability Classification:** Adapted / Unproven (`research-interpretation`).
  The primary source evaluates VST strictly on China A-share equity panels (CSI 1000). The mechanism has not been demonstrated on cryptocurrency data.
- **Portability Adaptations & Crypto Frictions:**
  - *24/7 Continuous Trading:* Unlike equity markets with daily open/close auctions, crypto assets trade continuously. The multi-agent feedback loop must anchor feedback transitions to fixed temporal epochs (e.g., UTC 00:00 funding boundaries or 8-hour intervals).
  - *Perpetual Funding Rate Dynamics:* Factor expressions in crypto perpetuals must incorporate funding rate differentials and basis drift. High-turnover long/short factors risk severe attrition from perpetual funding imbalances.
  - *Cross-Venue Liquidity Fragmentation:* Crypto liquidity is fragmented across Binance, OKX, Bybit, and decentralized venues. Execution assumptions must model venue-specific maker/taker fees and order-book depth rather than idealized uniform fills.
  - *High Idiosyncratic Volatility & Cascades:* Liquidation cascades and extreme kurtosis violate the Gaussian assumptions underlying standard Sharpe evaluations, requiring Sortino, Omega, or CVaR metrics in gate $L_4$.

## Limitations

- **Gross Returns Only (`source-reported`):** All empirical performance metrics omit transaction costs, slippage, and market impact, which are particularly severe in small-cap stocks.
- **Single-Run Observational Evaluation (`source-reported`):** All results derive from a single end-to-end run under a fixed random seed; run-to-run variance across independent training runs is unmeasured.
- **Adaptive Validation Hazard on Leap Gate (`source-reported`):** Gate $L_4$ repeatedly evaluates candidate leaps on the internal leap-validation split across 1341 transactions, creating an uncorrected multi-testing optimization hazard.
- **Descriptive Speedup without Matched Leap-Disabled Baseline (`source-reported`):** The reported skip of 1924 guidance cycles is a descriptive tally; actual wall-clock speedup isolated from hardware and API variations was not measured in a controlled experiment.
- **Safety by Construction Rather than Empirical Adversarial Audit (`source-reported`):** Visibility leakage prevention and rollback correctness are established structurally by architecture design rather than verified through adversarial fault injection.

## Implementation status

`not-implemented`. This record is a research capture of an external academic discovery framework. No implementation in PyBroker, NautilusTrader, paper trading, testnet, or live trading has been performed.

## Adoption boundary

`research-only` / `not-approved`.
Inclusion in this repository signifies normalized research documentation and provenance capture. It does not constitute validation of trading profitability, implementation authorization, or approval for capital deployment.

## Related Wiki records

- `[[alphaschema-trading-semantic-plan-space-surrogate-guided-factor-mining-2026-09-05]]` (Co-author Yuqi Li's prior plan-space semantic factor framework).
- `[[goant-quality-diversity-multi-agent-microstructure-alpha-discovery-2026-09-12]]` (Quality-diversity multi-agent alpha factor search architecture).
- `[[alpharjm-reward-jump-memory-sde-critic-symbolic-alpha-2026-09-11]]` (Stochastic return-guided symbolic alpha factor discovery).
- `[[alphalogics-market-logic-multi-agent-factor-generation-2026-09-05]]` (Market logic-driven multi-agent factor mining).
- `[[quantaalpha-institutional-price-volume-correlation-intraday-momentum-2026-09-05]]` (Formulaic price-volume alpha discovery).

## Sources

- Yuqi Li, Siyuan Liu, and Bingjun Liu, *"VST: Verifiable Structured Transport for Auditable Agent-to-Agent Alpha Discovery"*, arXiv preprint `arXiv:2609.07065v1 [cs.AI]`, submitted September 7, 2026.
  - Abstract URL: [https://arxiv.org/abs/2609.07065](https://arxiv.org/abs/2609.07065)
  - Full-Text HTML URL: [https://arxiv.org/html/2609.07065v1](https://arxiv.org/html/2609.07065v1)
  - Full-Text PDF URL: [https://arxiv.org/pdf/2609.07065](https://arxiv.org/pdf/2609.07065)
  - Canonical DOI: [10.48550/arXiv.2609.07065](https://doi.org/10.48550/arXiv.2609.07065)
