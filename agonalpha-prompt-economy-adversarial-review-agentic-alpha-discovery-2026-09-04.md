---
schema: strategy-research-record-v1
title: "AgonAlpha: Autonomous Alpha Discovery via Prompt Economy, Adversarial Review, and Scalable Agentic Search"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - llm-agentic
  - factor-discovery
  - adversarial-review
  - mcts
  - cross-sectional-equity
  - options-implied-volatility
status: research-only
confidence: medium
source_as_of: 2026-08-04
sources:
  - https://arxiv.org/abs/2608.11250
  - https://arxiv.org/html/2608.11250v1
  - https://doi.org/10.48550/arXiv.2608.11250
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# AgonAlpha: Autonomous Alpha Discovery via Prompt Economy, Adversarial Review, and Scalable Agentic Search

## Provenance

- **Primary Source:** Weicheng Ye (Department of Physics, The Chinese University of Hong Kong), Youran Sun (Department of Mathematics, University of Maryland), Xingyu Ren (CUHK Physics), Shunyao Yu (CUHK Physics), and Chugang Yi (UMD Math), **"AgonAlpha: Autonomous Alpha Discovery via Prompt Economy and Scalable Agentic Search"**, arXiv preprint `arXiv:2608.11250v1 [cs.AI]`, submitted 4 August 2026. DOI: `10.48550/arXiv.2608.11250`. Stable URL: `https://arxiv.org/abs/2608.11250`. Full-text HTML: `https://arxiv.org/html/2608.11250v1`.
- **External Evaluation Platform:** WorldQuant BRAIN production quantitative platform. The evaluation protocol fixed one uniform environment across all users: U.S. TOP3000 equities, execution delay 1, and backtest evaluation window from 2019-01-01 through 2023-12-31 (5 calendar years).
- **Repository Deduplication:** Repository-wide source identity checks on 2026-09-04 confirmed that `arXiv:2608.11250` and the authors Ye, Sun, Ren, Yu, and Yi do not appear in any existing record. Existing LLM-agentic factor discovery records (`alphacrafter-harness-multi-agent-cross-sectional-equity-alpha-2026-09-03.md`, `aeap-seads-llm-agentic-factor-discovery-formulaic-alpha-2026-09-03.md`, `llm-verifier-guided-strategy-genome-evolution-evoquant-2026-09-04.md`, `alphar1-context-aware-alpha-screening-llm-reasoning-grpo-2026-09-03.md`) focus on self-contained simulator backtests, prompt engineering, genome mutation, or RL reasoning tuning. This record uniquely captures an architecture searching over frozen research artifacts rather than raw formulas alone, incorporating a fresh-context adversarial reviewer with simulation rerun and veto authority, pending-aware Monte Carlo Tree Search (MCTS), and direct empirical validation on an external institutional platform (WorldQuant BRAIN).

## Economic mechanism

### Source-reported

The authors argue that existing automated alpha mining systems suffer from four architectural deficiencies:
1. **Search unit:** Systems treat isolated mathematical formulas as the basic unit of search, discarding the economic hypothesis, alternative rejected directions, and reviewer objections that generated them.
2. **Verification mechanism:** Passive scalar thresholds or self-scoring LLM agents fail to detect data leakage, mismatched expressions, or overfitted constants.
3. **Resource allocation:** Static search schedules cannot adaptively allocate costly platform simulation budgets across competing research lineages or handle asynchronous evaluations in progress.
4. **Evidence preservation:** Incomplete audit trails obscure the real number of trials, creating unadjusted multiple-testing biases.

To resolve this, AgonAlpha formulates alpha discovery as a search over complete research artifacts $A = (H, E, D, R, V)$ where $H$ is the economic hypothesis, $E$ the executable expression, $D$ platform simulation data/evidence, $R$ the search rationale, and $V$ the adversarial review status.

Across its deployments on WorldQuant BRAIN, the system discovered multiple verified alpha mechanisms in the U.S. equity market:
1. **Multi-Tenor Implied Volatility Disagreement:** Persistent elevation of put implied volatility over call implied volatility across multiple tenors (30-, 60-, and 90-day) reflects institutional hedging against downside tail risk and private information leakage, predicting cross-sectional equity underperformance.
2. **Call-Dominant Open Interest Regime Conditioning:** Long-term put/call open interest ratios ($M_{20}(PCR_{270}^{OI}) < 1.0$) identify call-dominant market regimes. Within this state, directional IV skew combined with industry-level skew magnitude and option forward curve slope differences ($90/30$-day forward price deviations) provides strong return predictability.
3. **Relative-Volume Stability:** Normalized volume dispersion ($-\sigma_{40}(V / \text{ADV20})$) isolates stocks with steady institutional participation from those driven by episodic retail attention spikes, capturing the unwinding of speculative overreaction.
4. **Market-Normalized Short Interest with Reversal Timing:** Scaling firm-level short interest by rolling market-wide aggregate short interest isolates idiosyncratic borrowing pressure, which is complemented by short-term price reversal to time entry points.

### Research interpretation

The overarching mechanism is **search over auditable research lineages constrained by fresh-context adversarial verification**.

At the strategy level, the primary alpha driver in the top-performing nodes (such as Node 0019 `pwlL71Ex` and Node 0021 `KPE0LnN1`) is **informed options-market sentiment transmission into underlying cash equity prices**. 
- Option market participants (institutions, informed hedgers) trade ahead of cash equity participants due to leverage and tail-risk protection needs.
- The multi-tenor IV difference ($IV^{put} - IV^{call}$ across 30, 60, and 90 days) captures non-transitory hedging pressure while filtering out single-expiry idiosyncratic noise.
- The regime conditioning filter ($M_{20}(PCR^{OI}_{270}) < 1.0$) acts as an asymmetric state partition: when overall speculative call positioning dominates institutional open interest, stocks whose individual option skew nonetheless indicates high put demand stand out as acute negative divergence candidates.
- The option forward curve term ($|F|^4$) and industry skew magnitude ($|I|^2$) serve as non-linear conviction scalers, heavily weighting assets where implied forward prices diverge from current spots.

## Signal

The system operates at two integrated levels: the agentic discovery loop and the resulting executable alpha expressions.

### 1. Agentic Discovery Architecture

- **Proposer Contract:**
  - Receives ancestor reports, working directory, platform documentation, and sample readings.
  - Generates 16 candidate formulas per node.
  - Runs an internal halving tournament: simulates all candidates, removes near-duplicates violating the hard self-correlation gate ($\rho > 0.85$), ranks survivors by absolute composite platform score $|\text{Score}|$, and eliminates the lower 50% per round ($16 \to 8 \to 4 \to 2 \to 1$).
  - For dollar-neutral cross-sectional alphas, negative-scoring finalists are sign-reflected analytically without re-simulation.
  - Enforces a monotone improvement constraint: winning candidate must exceed the best ancestor score.
  - Role prompt is constrained to 57 physical lines.
- **Reviewer Contract:**
  - Operates in a fresh context on an independent model route with access only to the candidate artifact directory and platform documentation.
  - Audits five specific dimensions (Table 2):
    1. *Evidence integrity:* Verifies that expressions, settings, metrics, and annual tables match platform logs. Any verified fabrication, leakage, or look-ahead immediately sets the scheduler score to 0 (veto).
    2. *Sign logic:* Flags terms whose directional signs contradict the stated economic rationale.
    3. *Constant rationale:* Flags unmotivated numerical coefficients or window parameters.
    4. *Temporal stability:* Flags alphas where annual scores are omitted or the best-to-worst annual fitness ratio exceeds 5.0.
    5. *Selection risk:* Evaluates cross-lineage redundancy and tuning concentration.
  - Role prompt is constrained to 44 physical lines.
- **Two-Level Budget Allocation & Scheduler:**
  - Outer search uses a pending-aware Upper Confidence Bound (UCB) applied to Monte Carlo Tree Search:
    $$\text{UCB}(c) = \frac{Q_{\text{sub}}(c)}{v(c)} + C \sqrt{\frac{\ln(v(p) + \pi(p))}{v(c) + \pi(c)}}$$
    where $Q_{\text{sub}}(c)$ is the sum of verified rewards in the subtree rooted at $c$, $v(c)$ is the completed visit count, $\pi(c)$ is the count of in-flight/pending evaluations, and exploration constant $C = 10.0$.
  - Backpressure rule: each non-root node can have at most one in-flight child ($\pi(c) \le 1$), while the root $\rho$ is exempt to prevent pipeline starvation.

### 2. Discovered Normalized Alpha Expressions

The top five verified alphas reported in the paper (Table 3 and Tables 10–12) follow the normalized logic below:

#### Primary Peak Alpha: Node 0021 (`KPE0LnN1`, `0021-28-forward-pcr-low-quartic`)
- **Signal Logic:**
  $$f_{0021} = H\left[ M_{20}(PCR^{OI}_{270}) < 1.0,\; Z_{\text{sector}}\left\{ \operatorname{sp}_2(S) \cdot |I|^2 \cdot |F|^4 \right\} \right]$$
- **Signal Components:**
  - $PCR^{OI}_{270}$: 270-day put/call open interest ratio. $M_{20}(\cdot)$ is a 20-day simple moving average. The condition $M_{20}(PCR^{OI}_{270}) < 1.0$ serves as a binary gate (call-dominant state).
  - $H(c, x)$: Hold operator; maintains the previous valid value when condition $c$ is false.
  - $S$: Multi-tenor implied volatility skew direction:
    $$S = -M_{48}\left[ \sum_{t \in \{30, 60, 90\}} \left( IV_t^{put} - IV_t^{call} \right) \right]$$
  - $\operatorname{sp}_2(S)$: Signed square operator $\operatorname{sp}_2(x) = \operatorname{sign}(x)|x|^2$, preserving directional skew while penalizing small values.
  - $|I|^2$: Industry-level skew magnitude squared.
  - $|F|^4$: 90-day vs 30-day option forward curve price deviation to the fourth power.
  - $Z_{\text{sector}}\{\cdot\}$: Cross-sectional z-score standardization within each market sector.
- **Execution Settings:** Industry neutralization, decay = 12, truncation = 8%.

#### Core Predecessor: Node 0019 (`pwlL71Ex`, `0019-12-tenor-blend-mean48`)
- **Signal Logic:**
  $$f_{0019} = Z_{\text{sector}}\left[ -M_{48}\left( \sum_{t \in \{30, 60, 90\}} \left( IV_t^{put} - IV_t^{call} \right) \right) \right]$$
- **Execution Settings:** Industry neutralization, decay = 10, truncation = 8%.

#### Aligned Six-Month Option Demand: `A17q5RdR`
- **Signal Logic:**
  $$f^{\text{opt}} = M_{40}\left[ B_{60}\left( IV_{180}^{call} - IV_{180}^{put} \right) \right]$$
  where $B_{60}$ backfills only the contemporaneously aligned call-put spread across a 60-day window.
- **Execution Settings:** Industry neutralization, decay = 0, truncation = 8%.

#### Relative-Volume Stability: `88er8JAl`
- **Signal Logic:**
  $$f^{\text{vol}} = -\sigma_{40}\left( \frac{V}{\text{ADV20}} \right)$$
  where daily volume $V$ is normalized by 20-day average daily volume $\text{ADV20}$, and $\sigma_{40}$ is the 40-day rolling standard deviation.
- **Execution Settings:** Industry neutralization, decay = 2, truncation = 5%.

#### Persistent Short Interest with Reversal Timing: `LL1mdWz6`
- **Signal Logic:**
  $$q = R\left\{ M_{20}\left[ B_{60}^{sub}\left( \frac{SI}{M_{252} \bar{SI}_{mkt}} \right) \right] \right\}$$
  $$f^{\text{SI}} = R\left[ H(\text{observed}, q) + 0.1 \cdot R(-M_5 r) \right]$$
  where $SI$ is short interest, $\bar{SI}_{mkt}$ is cross-sectional average market short interest, $B_{60}^{sub}$ is a 60-day subindustry backfill, and $R(\cdot)$ denotes cross-sectional rank.
- **Execution Settings:** Industry neutralization, decay = 0, truncation = 8%.

### Underspecified items

- Exact intraday timing conventions (e.g., market-on-close vs next-day open auction) are governed by WorldQuant BRAIN's standardized `delay = 1` execution simulator, but specific order execution algorithms (TWAP/VWAP) are abstracted.
- Exact proprietary FASTEXPR field mapping for synthetic option forward curve calculations ($F$) is described mathematically in the paper, but raw vendor data field IDs are specific to BRAIN.

## Required data

- **Universe:** U.S. TOP3000 equities (liquid U.S. common stocks).
- **Timeframe:** Daily bars (end-of-day rebalancing).
- **Evaluation Sample:** 2019-01-01 to 2023-12-31 (5 years in-sample backtest; all submitted alphas entered live out-of-sample forward tracking on WorldQuant BRAIN).
- **Required Data Fields:**
  - Daily equity OHLCV (Open, High, Low, Close, Volume) and 20-day rolling average volume ($\text{ADV20}$).
  - Option implied volatilities across standardized maturities: 30-day, 60-day, 90-day, and 180-day call and put IV ($IV_t^{call}, IV_t^{put}$).
  - Option open interest: 270-day put/call open interest ratio ($PCR_{270}^{OI}$).
  - Synthetic option forward curves: 30-day, 90-day, and 1080-day forward price estimates.
  - Short interest data: bi-weekly/monthly short interest observations ($SI$) and market-wide aggregate short interest ($\bar{SI}_{mkt}$).
  - Sector and subindustry membership matrices.
- **Point-in-Time Protections:** Contradictory timestamp checks and aligned spread calculations ($B_{60}$) ensure options metrics are matched on identical observation dates before backfilling, preventing lookahead leakage from stale quotes.

## Execution assumptions

### Source-reported

- **Execution Delay:** Delay = 1 (trades execute on session $t+1$ following observation at session $t$ close).
- **Portfolio Neutralization:** Industry or sector neutralization applied to eliminate systematic sector bias.
- **Weight Truncation:** Extreme asset weights capped between 3% and 8% to limit idiosyncratic concentration.
- **Weight Decay Filter:** Linear decay filters applied over horizons of 0 to 12 days to reduce high-frequency portfolio turnover.
- **Sizing:** Dollar-neutral long-short cross-sectional equity portfolio ($\sum w_i^+ = 0.5, \sum w_i^- = -0.5$).

### Research interpretation

- The platform's backtest engine incorporates standardized trading friction models. For the five featured alphas, the platform-reported margins range from 47.07 bps (`LL1mdWz6`) to 234.93 bps (`KPE0LnN1`). Because typical institutional execution costs on liquid U.S. equities range between 5 and 15 bps, the high reported margins provide substantial theoretical cushion against turnover decay.
- However, options-surface data coverage is not uniform across all 3,000 equities in the TOP3000 universe. The effective active breadth of options-dependent alphas (`pwlL71Ex`, `KPE0LnN1`) is naturally concentrated in the top 500 to 1,000 most liquid optionable equities.

## Evidence

### Source-reported

All figures below are directly cited from `arXiv:2608.11250v1`, Section 5, Table 3, and Section 5.2/5.5:

1. **Overall System Submissions:**
   - Deployments across 5 independent users and 6 model backends generated 60 total submissions.
   - **17 submissions (28.3%)** received WorldQuant BRAIN's highest evaluation grade: **SPECTACULAR**.
   - All 60 submissions passed platform screening and entered live out-of-sample forward tracking.

2. **Benchmark Results for Five Representative Alphas (Table 3):**
   - **`KPE0LnN1` (Forward PCR low quartic, Node 0021):**
     - Grade: **SPECTACULAR**
     - Fitness: **9.50** (platform maximum across all runs)
     - Sharpe Ratio: **3.48**
     - Annualized Return: **93.15%**
     - Annual Turnover: **7.93%**
     - Maximum Drawdown: **19.50%**
     - Margin: **234.93 bps**
     - Sub-universe Sharpe: **1.76** (passing threshold: 1.51)
     - Self-correlation: **0.6321** (passing limit: 0.70)
     - Annual Fitness Sequence (2019–2023): $(8.43, 2.59, 18.28, 17.19, 4.15)$
   - **`pwlL71Ex` (Multi-tenor IV skew, Node 0019):**
     - Grade: **SPECTACULAR**
     - Fitness: **4.73** | Sharpe: **3.03** | Return: **30.51%** | Turnover: **5.08%** | Drawdown: **11.15%** | Margin: **120.20 bps**
     - Sub-universe Sharpe: **1.43** (limit: 1.31) | Self-correlation: **0.4968** (limit: 0.70)
     - Annual Fitness Sequence: $(2.76, 3.77, 4.96, 9.92, 2.39)$
   - **`A17q5RdR` (Aligned 6m option demand):**
     - Grade: **SPECTACULAR**
     - Fitness: **3.93** | Sharpe: **2.52** | Return: **21.05%** | Turnover: **5.92%** | Drawdown: **8.87%** | Margin: **71.09 bps**
     - Sub-universe Sharpe: **1.34** (limit: 1.25) | Self-correlation: **0.1827** (limit: 0.70)
     - Annual Fitness Sequence: $(2.49, 1.13, 3.94, 10.59, 2.98)$
   - **`LL1mdWz6` (Persistent short interest with reversal timing):**
     - Grade: **SPECTACULAR**
     - Fitness: **2.82** | Sharpe: **2.32** | Return: **18.41%** | Turnover: **7.82%** | Drawdown: **6.91%** | Margin: **47.07 bps**
     - Sub-universe Sharpe: **1.24** (limit: 1.00) | Self-correlation: **0.4173** (limit: 0.70)
     - Annual Fitness Sequence: $(1.02, 7.08, 2.57, 3.83, 0.95)$
   - **`88er8JAl` (Relative-volume stability):**
     - Grade: **SPECTACULAR**
     - Fitness: **2.55** | Sharpe: **1.76** | Return: **26.24%** | Turnover: **9.58%** | Drawdown: **24.21%** | Margin: **54.77 bps**
     - Sub-universe Sharpe: **0.90** (limit: 0.76) | Self-correlation: **0.4498** (limit: 0.70)
     - Annual Fitness Sequence: $(2.71, 1.76, 1.15, 5.34, 3.48)$

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Extreme Calendar Regime Concentration:**
   - In Node 0021 (`KPE0LnN1`), annual fitness swings from 2.59 (2020) to 18.28 (2021) and 17.19 (2022) — a **7.1-fold discrepancy** between best and worst years. Over 40% of the cumulative in-sample PnL is generated during the 2021–2022 market regimes.
   - Node 0022 displays an even more severe **44.7-fold annual fitness collapse**, plunging from 5.81 (2020) and 5.01 (2022) to 0.13 in 2023.
2. **Selection Risk and Exponent Overfitting:**
   - In Node 0021, the choice of quadratic power $|I|^2$ and quartic power $|F|^4$, alongside lookback windows of 20, 48, and 270 days, emerged from tournament grid exploration rather than structural economic derivation.
3. **Failed Research Lineages:**
   - Node 0018 (news volume standard deviation seed) failed completely to produce a viable submission and was discarded due to mismatched secondary metrics and lack of predictive edge.
   - Node 0020 introduced an arbitrary centering constant ($0.35$) that mechanically altered portfolio beta exposure without economic justification, drawing explicit reviewer critique.

## Falsification plan

To falsify the proposed options-implied sentiment and agentic discovery mechanisms:
1. **Exponent and Horizon Perturbation:** Perturb the integer exponents and lookback windows of `KPE0LnN1` (e.g., test $|F|^2$ instead of $|F|^4$, $|I|^1$ instead of $|I|^2$, and adjust the 48-day window to 30d and 60d). If the out-of-sample Sharpe ratio degrades by $>40\%$, the strategy is an overfitted polynomial artefact of the 2021–2022 options regime.
2. **Out-of-Sample Calendar Stress (2024–2026):** Evaluate the frozen formula on live post-2023 U.S. equity data. If the annual Sharpe ratio falls below 1.0 or maximum drawdown exceeds 25%, reject the hypothesis that multi-tenor IV disagreement provides persistent risk-adjusted alpha.
3. **Cross-Sectional Placebo Permutation:** Randomly shuffle the stock-to-option mappings within each sector while preserving individual equity return series. If the permuted strategy produces risk-adjusted returns statistically indistinguishable from zero ($t < 1.96$), confirm that asset-specific option demand is the true informational channel; if positive alpha persists, the expression is merely exploiting sector-level momentum or market beta.
4. **Adversarial Reviewer Ablation:** Run the AgonAlpha search loop without the fresh-context reviewer (proposer self-evaluation only). If the proportion of lookahead-contaminated or duplicate expressions increases significantly and post-submission survival on live tracking drops, verify that the fresh-context reviewer is the necessary gating mechanism.

## Crypto portability

**Portability classification:** `adapted` / `unproven`.

The empirical results were obtained entirely on U.S. equities (TOP3000) using equity options surfaces. Porting this framework to cryptocurrency markets faces major structural obstacles:
1. **Absence of Broad Altcoin Options Surfaces:** In equities, thousands of individual stocks have listed, liquid standardized options contracts. In crypto, liquid options exist almost exclusively for Bitcoin (`BTC`) and Ethereum (`ETH`) on venues like Deribit, with nascent markets for Solana (`SOL`). Cross-sectional equity options alpha cannot be ported directly to an altcoin universe.
2. **Perpetual Funding Rate as Skew Proxy:** An adapted crypto hypothesis must replace options put-call IV skew with cross-sectional **perpetual futures funding rate skew** or basis divergence between spot and perpetual contracts. Highly negative funding rates across multiple funding intervals (e.g. 8h, 24h, 72h) reflect crowded short positioning analogous to heavy put-buying.
3. **Perpetual Open Interest vs Put/Call OI:** The equity open-interest ratio ($PCR_{270}^{OI} < 1.0$) must be adapted using crypto-native positioning indicators, such as top-trader long/short account ratios (Binance) or aggregate perpetual open interest relative to market cap.
4. **Funding Cost Drag:** Crypto perpetual carry incurs continuous funding payments. If an adapted long-short strategy holds high-funding altcoins long against low-funding coins short, funding debits (often 15%–40% annualized during bull markets) will rapidly consume cross-sectional alpha.
5. **Continuous 24/7 Session Structure:** Unlike U.S. equities with discrete closing auctions and `delay = 1` overnight gap structures, crypto trades continuously 24/7/365, requiring synthetic bar definitions (e.g. 00:00 UTC fixes) that may suffer from time-zone liquidity clustering.

## Limitations

- **Proprietary Simulator Dependence:** Backtest results, execution fills, and grades are determined by WorldQuant BRAIN's closed proprietary simulation engine. While this guarantees external adjudication, internal fill algorithms and margin assumptions cannot be independently inspected.
- **Extreme Regime Concentration:** The top-performing alphas depend heavily on the volatile 2021–2022 market regime, exhibiting sharp performance decay in calmer market environments (such as 2023).
- **High-Order Polynomial Tuning:** Discovered alphas contain fitted non-linear terms ($|F|^4$, $|I|^2$, and $\operatorname{sp}_8$ in Node 0022) that carry high selection risk.
- **Shorting Frictions and Borrow Availability:** Although dollar neutrality is assumed, real-world execution of stocks with high short interest (`LL1mdWz6`) incurs borrow fees and locate constraints that are omitted in standard simulation scores.

## Implementation status

`not-implemented`.

This record represents external research capture. No implementation has been created in PyBroker, NautilusTrader, or any internal execution system. No paper trading, testnet verification, or live trading has been authorized or conducted.

## Adoption boundary

`not-approved` / `research-only`.

This artifact is research material in the public staging pool. Presence in this repository does not indicate strategy approval, profitability verification, or suitability for live capital allocation. Any progression toward implementation requires independent replication, leakage-free backtesting on independent data, and formal review.

## Related Wiki records

- `alphacrafter-harness-multi-agent-cross-sectional-equity-alpha-2026-09-03.md`
- `aeap-seads-llm-agentic-factor-discovery-formulaic-alpha-2026-09-03.md`
- `llm-verifier-guided-strategy-genome-evolution-evoquant-2026-09-04.md`
- `alphar1-context-aware-alpha-screening-llm-reasoning-grpo-2026-09-03.md`
- `option-implied-surface-cremers-weinbaum-skew-crash-regimes-2026-09-02.md`
- `options-statistical-arbitrage-graph-learning-synthetic-long-2026-09-02.md`

## Sources

- Weicheng Ye, Youran Sun, Xingyu Ren, Shunyao Yu, and Chugang Yi, "AgonAlpha: Autonomous Alpha Discovery via Prompt Economy and Scalable Agentic Search", arXiv preprint `arXiv:2608.11250v1 [cs.AI]`, August 2026. Stable URL: `https://arxiv.org/abs/2608.11250`. Full-text HTML: `https://arxiv.org/html/2608.11250v1`. DOI: `10.48550/arXiv.2608.11250`.
- Primary evidence tables and formulas directly cited: Table 2 (Adversarial Verification Protocol), Table 3 (Comprehensive BRAIN benchmark for five representative validated alphas), Table 10 (Complete alpha catalog and economic interpretations, part 1 of 3), Table 11 (Complete alpha catalog and economic interpretations, part 2 of 3), Table 12 (Complete alpha catalog and economic interpretations, part 3 of 3), Equations 1–6, and Section 5 evaluation metrics.
