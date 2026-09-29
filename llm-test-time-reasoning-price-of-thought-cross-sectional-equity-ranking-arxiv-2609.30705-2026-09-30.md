---
schema: strategy-research-record-v1
title: "The Price of Thought: Test-Time Reasoning Effort in LLM Cross-Sectional Equity Ranking - Nonmonotonic Net Returns, Replicated Masked-News Harm, and Stochastic Generation Instability (arXiv:2609.30705)"
created: 2026-09-30
updated: 2026-09-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - llm-trading
  - test-time-compute
  - reasoning-effort
  - cross-sectional-ranking
  - us-equities
  - market-neutral
  - net-of-cost
  - negative-evidence
  - arxiv-preprint
status: research-only
confidence: high
source_as_of: 2026-09-30
sources:
  - "arXiv:2609.30705v1 [cs.AI], 'The Price of Thought: Does Test-Time Reasoning Pay in LLM Trading?', Jiayi Chen and Guiling Wang, submitted Fri 25 Sep 2026 02:28:01 UTC; landing https://arxiv.org/abs/2609.30705 ; pinned PDF https://arxiv.org/pdf/2609.30705v1 (1038149 bytes, SHA-256 c66e22b00491bbdbafa54a87c42c3749b1f61ff325aa9093a09b42e5414c16ea, fetched and read 2026-09-30)"
  - "arXiv HTML full text https://arxiv.org/html/2609.30705v1 (399563 bytes, SHA-256 b586f5ec9da6f05b304360df28387e3a5ec11e023b7334f0af8e3559c581c05e, fetched 2026-09-30)"
  - "arXiv TeX source https://arxiv.org/src/2609.30705v1 (530406 bytes gzip tar, SHA-256 44762e361723bab253957e1e4acab85e5d05bf4d2e8025d836f05bb69db3c0e5, sigconf.tex, methods.tex, results.tex, appendix.tex, figure2.tex inspected 2026-09-30 for exact equations, prompts, and tables)"
  - "arXiv DataCite DOI https://doi.org/10.48550/arXiv.2609.30705 (landing states 'pending registration')"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# The Price of Thought: Test-Time Reasoning Effort in LLM Cross-Sectional Equity Ranking - Nonmonotonic Net Returns, Replicated Masked-News Harm, and Stochastic Generation Instability (arXiv:2609.30705)

## Provenance

**Primary source (authoritative text for every figure below):**
- **Identifier**: `arXiv:2609.30705v1 [cs.AI]`, title exactly *The Price of Thought: Does Test-Time Reasoning Pay in LLM Trading?*.
- **Authors, exactly as printed on title block and PDF metadata**: Jiayi Chen (`jc2693@njit.edu`) and Guiling Wang (`guiling.wang@njit.edu`). Affiliation: Department of Computer Science, New Jersey Institute of Technology, Newark, New Jersey, USA. Exactly two authors; no corporate or secondary co-authors.
- **Version / date**: Single version `v1` -- submission history shows `[v1] Fri, 25 Sep 2026 02:28:01 UTC (518 KB)`, submitter Jiayi Chen. PDF metadata `/CreationDate`: `D:20260928002716+00'00'`.
- **Publication status**: Preprint only; peer review not stated in source. Landing page has no `Comments` field and no `journal-ref`. License: `CC BY 4.0` (Creative Commons Attribution 4.0 International; PDF metadata `/License`).
- **Canonical DOI**: `https://doi.org/10.48550/arXiv.2609.30705` (arXiv DataCite DOI, landing indicates pending registration).
- **Pinned artifacts (fetched and inspected 2026-09-30)**:
  - Pinned PDF: `https://arxiv.org/pdf/2609.30705v1`, 1,038,149 bytes, SHA-256 `c66e22b00491bbdbafa54a87c42c3749b1f61ff325aa9093a09b42e5414c16ea`; 13 pages, 78,114 characters extracted via `pypdf 6.16.2` and read end to end.
  - HTML full text: `https://arxiv.org/html/2609.30705v1`, 399,563 bytes, SHA-256 `b586f5ec9da6f05b304360df28387e3a5ec11e023b7334f0af8e3559c581c05e`.
  - Abstract page: `https://arxiv.org/abs/2609.30705`, 41,220 bytes, SHA-256 `6b2a68132f0ff1414378ecd3d0e38a2659edc62e043202fc37ad3a9289677b84`.
  - TeX source: `https://arxiv.org/src/2609.30705v1`, 530,406 bytes gzip tar, SHA-256 `44762e361723bab253957e1e4acab85e5d05bf4d2e8025d836f05bb69db3c0e5`. Extracted files inspected directly: `sigconf.tex`, `methods.tex`, `results.tex`, `appendix.tex`, `figure2.tex`, `discussion.tex`, `introduction_story_preview.tex`, `related_work.tex`, `references.bib`.
- **Companion code status**: The authors state in Appendix J (p. 13): "The authors retain complete evaluation records and plan to release the evaluation code, prompts, result summaries, evaluator hashes, and artifact manifest in a public GitHub repository." No public repository URL is published at capture date (`data gap`). No third-party code was cloned or executed.
- **Repository deduplication audit (hidden-inclusive, pre-write 2026-09-30)**: `rg -uuu` across the entire checkout including `.git`, `.mimo-worktrees/`, `.agents/`, `.hermes/`, and `coverage_manifest.csv` for `2609\.30705`, `Price of Thought`, `Test-Time Reasoning Pay`, `Jiayi Chen`, and `Guiling Wang` returned **zero files**. Positive control `novy-marx` returned 44 tracked records in the same session.
- **Material distinction from adjacent records**:
  - `alphar1-context-aware-alpha-screening-llm-reasoning-grpo-2026-09-03.md`: Evaluates post-training reinforcement learning (GRPO) to fine-tune reasoning trajectories for formulaic alpha mining on CSI 300 / CSI 500; this paper evaluates inference-time test-time compute controls within frozen models on US equities.
  - `trading-r1-curricular-reinforcement-learning-llm-reasoning-2026-09-05.md`: Evaluates curricular reinforcement learning for single-asset trading policy generation; this paper evaluates cross-sectional multi-asset ranking under frozen prompt and portfolio mappings.
  - `rice-alpha-point-in-time-issuer-local-event-graph-llm-stock-scoring-2026-09-29.md`: Constructs issuer-local event continuation graphs for sentiment correction; this paper studies the pure marginal effect of test-time compute allocation across numerical and raw/masked text inputs.

## Economic mechanism

### Source-reported

The paper examines whether allocating more inference-time reasoning effort (test-time compute) inside large language models improves investment decisions when the surrounding financial system is held strictly constant. In non-financial domains (math, coding, logic), allocating additional test-time compute through extended reasoning chains or search consistently improves benchmark accuracy because correctness is verifiable immediately. In quantitative trading, however, correctness is revealed only later through noisy market prices and after trading frictions.

The paper models the decision chain as:
$$\text{Reasoning effort} \longrightarrow \text{Stock scores} \longrightarrow \text{Holdings} \longrightarrow \text{Net returns}$$

Each link can decouple or invert the apparent benefit of extra computation:
1. Large score movements may leave portfolio rankings unchanged if they occur away from the selection boundary.
2. Minor score fluctuations near the selection boundary can replace long or short constituents with worse-performing assets.
3. Gross performance improvements can be entirely consumed by higher turnover and transaction costs.
4. Stochastic generation variance can render single-call performance gains non-reproducible across independent model invocations.

The authors hypothesize that additional reasoning can alter decisions, shift token expenditures, and change structural formatting compliance without producing a reliable, positive economic return after transaction costs.

### Research interpretation

This paper provides an empirical evaluation and stress-test of the assumption that "more reasoning is always better" in LLM-driven alpha generation. The falsifiable hypothesis under test is whether an increase in test-time reasoning effort ($\text{low}$ vs $\text{baseline}$, or along a progression from $\text{none}$ to $\text{maximum}$) generates a statistically and economically significant positive net return difference:
$$\Delta_{b,a} = \mathbb{E}[R^{\mathrm{net}}_{b,a,\mathrm{low},t} - R^{\mathrm{net}}_{b,a,\mathrm{base},t}] > \epsilon$$
where $\epsilon = 0.25$ bps/day is a pre-declared economic threshold ($2.5$ bp/month or $\approx 0.63\%$ p.a.).

From an alpha-generation standpoint, the paper shows that:
1. **Inference-time reasoning acts as an operational perturbation, not an alpha multiplier**: Increasing reasoning tokens alters the score distribution and constituent selection, but the changes behave like noise or overthinking rather than signal extraction.
2. **Overfitting to narrative noise**: In unstructured text tasks (masked news), extra reasoning traces lead the model to rationalize weak narrative evidence, resulting in statistically significant performance degradation (economic harm).
3. **High stochastic sensitivity**: Tail selection in decile long-short portfolios has zero overlap across independent stochastic runs ($0.0\%$ identical tails across 48 audit dates), demonstrating that LLM ranking outputs possess high sampling variance that destabilizes actual portfolio holdings.
4. **Reliability-performance divergence**: Improving schema compliance (e.g. fewer invalid JSON outputs) does not correlate with improved trading profitability.

## Signal

The trading signal and portfolio mapping are fully specified by the source in Section 3.5, Section 4.1, and Appendix A.

**1. Signal inputs and candidate cross-section (source-reported)**
- **Universe**: 100 liquid US common equities evaluated on each of 241 formation dates in 2024.
- **Opaque asset identifiers**: Each asset is assigned a randomized opaque identifier (e.g., `A0123456789`) on each formation date to prevent historical memorization of ticker symbols.
- **Task splitting**: The 100 candidates on each formation date are deterministically split into 4 independent model tasks of 25 assets each.
- **Information conditions**:
  1. *Numerical*: 16 daily cross-sectional rank features derived from CRSP daily stock files (past returns, momentum over 5, 21, 63, 126, 252 days; volatility over 5, 21, 63 days; downside volatility over 21 days; volume ratio over 21 days; log dollar volume over 21 days; Amihud illiquidity over 21 days; intraday return; trading range; log previous close). Each feature includes current value, 5-day mean, 20-day mean, and 20-day change (64 features per asset, 1,542,400 total values in the 2024 panel). All features end at the preceding trading session close.
  2. *Identifiable news*: Up to 3 most recent articles from EODHD news feed published between 4:00 p.m. ET on the preceding trading session and 9:00 a.m. ET on the formation date (max 9,000 characters per article, 18,000 characters per stock), retaining company names and ticker identifiers.
  3. *Masked news*: Same articles with company names, tickers, explicit dates/years, and publisher labels masked.

**2. Prompt instruction and structured output contract (source-reported)**
- **System instruction**: Casts the model as a conservative cross-sectional equity forecaster, treats text as untrusted data, and requires exactly one structured JSON object.
- **Task request**: Estimate relative return over the next 5 trading sessions, scoring the strongest candidate near $+1.0$ and the weakest near $-1.0$.
- **Output JSON schema**:
```json
{
  "items": [
    {
      "asset": "A0123456789",
      "score": 0.0,
      "confidence": 0.0,
      "materiality": 0.0,
      "uncertainty": 0.0,
      "abstain": false
    }
  ]
}
```
where `score` $\in [-1.0, 1.0]$, `confidence` $\in [0.0, 1.0]$, `materiality` $\in [0.0, 1.0]$, `uncertainty` $\in [0.0, 1.0]$, and `abstain` is boolean.

**3. Downstream signal formula (source-reported)**
For asset $i$ on formation date $d$, the combined trading signal is:
$$s_{i,d} = \begin{cases} 0, & \text{if abstaining or imputed to } 0, \\ q_{i,d} \times (0.5 + 0.5 \cdot c_{i,d}), & \text{otherwise} \end{cases}$$
where $q_{i,d}$ is the model score and $c_{i,d}$ is the model-reported confidence. `materiality` and `uncertainty` are preserved for diagnostics but do not alter position sizing.

**4. Portfolio ranking and construction (source-reported)**
- Rank $s_{i,d}$ descending across the 100 assets on formation date $d$.
- **Long leg**: Buy top 10 assets ($N=10$), equal-weighted ($10\%$ of long capital each).
- **Short leg**: Short bottom 10 assets ($N=10$), equal-weighted ($10\%$ of short capital each).
- **Gross exposure**: $2.0$ ($1.0$ long $+ 1.0$ short per unit capital).
- **Net exposure**: $0.0$ (dollar neutral).
- **Tie breaking / abstentions**: If abstentions leave fewer than 20 eligible assets, fallback ranks all neutralized signals and breaks ties deterministically by asset identifier.
- **Holding period**: 5 trading sessions. The cohort enters at session open on formation date $d$, earns open-to-close return on day 1, and close-to-close returns on sessions 2, 3, 4, and 5.
- **Aggregate portfolio**: The daily portfolio is the simple equal-weighted average of the 5 active overlapping formation cohorts.

**5. Operational rules and execution convention (`research-proposed` where unstated)**
- Order execution at 9:30 a.m. market open; fill at open price on entry day; exit at 4:00 p.m. market close on session 5 (`source-reported`).
- Handling of partial fills or circuit breakers: none modeled by source (`data gap`); `research-proposed` convention is to skip execution if asset halted and re-normalize portfolio weights.


## Required data

- **Universe**: Liquid ordinary common shares listed on NYSE, AMEX, or Nasdaq (CRSP share codes 10 and 11, exchange codes 1, 2, 3). Screened from a fixed liquid panel of 1,000 securities established on December 30, 2022; exactly 100 active common stocks per formation date.
- **Date range**:
  - History / warm-up: CRSP daily files 2020 through 2024 (974,641 security-date rows over 1,005 trading dates from January 4, 2021 to December 31, 2024).
  - Formation window: 241 formation dates from January 10, 2024 to December 23, 2024.
  - Return window: 241 portfolio return dates from January 17, 2024 to December 30, 2024 (ramp-up excludes first 4 cohorts).
  - Stochastic audit sample: 48 clustered formation dates, yielding 68 return dates.
- **Point-in-time constraints**: Strictly causal. All numerical features end at the preceding session's close. All news articles must have timestamps between 4:00 p.m. ET on preceding trading day and 9:00 a.m. ET on formation date.
- **Delisting return cleaning rule**: Combined with delisting returns. When CRSP delisting code is 500-599 (performance-related drop/liquidation) and no delisting return is reported, delisting return is set to $-30\%$; other missing delisting returns remain missing (`source-reported`).
- **Data sources**: CRSP daily stock files via WRDS (prices, returns, volume, open, high, low, shares, exchange codes, delisting); EOD Historical Data (EODHD) licensed news feed.

## Execution assumptions

- **Order timing**: Orders placed at the market open on formation date $d$ (9:30 a.m. ET).
- **Holding horizon**: Exactly 5 trading sessions per cohort; exit at the close of session 5.
- **Fill model**: Fills assumed at open price on entry day and close price on exit day; intermediate days earn close-to-close returns (`source-reported`).
- **Trading costs**: Baseline 10 bps one way ($0.10\%$) applied to all capital bought or sold. Sensitivity ladder tested at 5, 10, 20, and 50 bps one way (`source-reported`).
- **Market impact / slippage**: Linear fee model only; nonlinear price impact, bid-ask spread variations, and order-book depth are not modeled (`data gap`).
- **Borrow / shorting**: Short sales assumed fully available with zero borrow cost, zero hard-to-borrow constraints, and zero short squeeze risk (`data gap`).
- **Inference compute cost**: Expressed as $\text{cost (bps)} = 10{,}000 \cdot C / A$, where $C$ is provider API cost in USD and $A$ is portfolio capital. Measured and reported separately from gross/net market returns.

## Evidence

### Source-reported

All figures below are direct extracts from `arXiv:2609.30705v1` (text, equations, Table 1, Table 2, Table 3, Table 7, Table 8, Table 9, Table 10, Table 11, Figure 2, and Figure 3):

#### 1. Primary low vs baseline reasoning results (241 return dates, 10 bps one-way cost, Table 2 / Figure 2)
The estimand is $\Delta_{b,a} = \mathbb{E}[R^{\mathrm{net}}_{\mathrm{low},t} - R^{\mathrm{net}}_{\mathrm{base},t}]$ in bps/day. Pre-declared economic threshold is $\epsilon = +0.25$ bps/day. Primary inference uses Newey-West HAC standard errors with 5 lags. Holm-adjusted $p$-values control family-wise error across the 3 information conditions within each backbone:
- **DeepSeek-Flash**:
  - *Numerical*: Estimate **$+6.159$ bps/day**, $95\%$ CI $[-7.243, +19.560]$, unadjusted $p = .368$, Holm-adjusted $p = 1.000$. Decision: **inconclusive**.
  - *Identifiable news*: Estimate **$+0.378$ bps/day**, $95\%$ CI $[-9.033, +9.790]$, unadjusted $p = .937$, Holm-adjusted $p = 1.000$. Decision: **inconclusive**.
  - *Masked news*: Estimate **$+1.449$ bps/day**, $95\%$ CI $[-6.768, +9.666]$, unadjusted $p = .730$, Holm-adjusted $p = 1.000$. Decision: **inconclusive**.
- **GPT-5.6 Luna**:
  - *Numerical*: Estimate **$+3.540$ bps/day**, $95\%$ CI $[-2.531, +9.611]$, unadjusted $p = .253$, Holm-adjusted $p = .759$. Decision: **inconclusive**.
  - *Identifiable news*: Estimate **$-0.626$ bps/day**, $95\%$ CI $[-5.905, +4.653]$, unadjusted $p = .816$, Holm-adjusted $p = 1.000$. Decision: **inconclusive**.
  - *Masked news*: Estimate **$+0.040$ bps/day**, $95\%$ CI $[-4.297, +4.378]$, unadjusted $p = .986$, Holm-adjusted $p = 1.000$. Decision: **inconclusive**.
- **Gemini 3.1 Flash-Lite**:
  - *Numerical*: Estimate **$+0.758$ bps/day**, $95\%$ CI $[-6.233, +7.749]$, unadjusted $p = .832$, Holm-adjusted $p = 1.000$. Decision: **inconclusive**.
  - *Identifiable news*: Estimate **$-0.142$ bps/day**, $95\%$ CI $[-8.128, +7.844]$, unadjusted $p = .972$, Holm-adjusted $p = 1.000$. Decision: **inconclusive**.
  - *Masked news*: Estimate **$-1.123$ bps/day**, $95\%$ CI $[-8.418, +6.173]$, unadjusted $p = .763$, Holm-adjusted $p = 1.000$. Decision: **inconclusive**.
- **Summary**: Exactly $0$ of $9$ primary contrasts meet the rule for material benefit ($L > +0.25$ bps/day). All $9$ intervals include zero.

#### 2. Absolute portfolio performance context (241 return dates, 10 bps cost, Table 7)
Metrics report baseline / low reasoning:
- DeepSeek numerical: Net return $-6.376$ / $-0.217$ bps/day; Sharpe $-0.80$ / $-0.14$; Max Drawdown $-32.03\%$ / $-20.52\%$; Turnover $30.83\%$ / $24.48\%$.
- DeepSeek identifiable news: Net return $-4.386$ / $-4.008$ bps/day; Sharpe $-0.59$ / $-0.52$; Max Drawdown $-27.80\%$ / $-24.46\%$; Turnover $31.19\%$ / $27.77\%$.
- DeepSeek masked news: Net return $-5.412$ / $-3.963$ bps/day; Sharpe $-0.69$ / $-0.50$; Max Drawdown $-26.68\%$ / $-28.48\%$; Turnover $30.79\%$ / $27.88\%$.
- GPT numerical: Net return $-3.506$ / $+0.033$ bps/day; Sharpe $-0.46$ / $-0.12$; Max Drawdown $-27.44\%$ / $-23.58\%$; Turnover $26.22\%$ / $26.02\%$.
- GPT identifiable news: Net return $-1.487$ / $-2.113$ bps/day; Sharpe $-0.27$ / $-0.33$; Max Drawdown $-24.94\%$ / $-29.53\%$; Turnover $27.28\%$ / $26.86\%$.
- GPT masked news: Net return $-3.483$ / $-3.442$ bps/day; Sharpe $-0.47$ / $-0.46$; Max Drawdown $-25.96\%$ / $-26.36\%$ Turnover $27.61\%$ / $26.88\%$.
- Gemini numerical: Net return $-4.962$ / $-4.204$ bps/day; Sharpe $-0.57$ / $-0.50$; Max Drawdown $-32.17\%$ / $-34.38\%$; Turnover $26.56\%$ / $26.65\%$.
- Gemini identifiable news: Net return $+1.417$ / $+1.275$ bps/day; Sharpe $+0.04$ / $+0.03$; Max Drawdown $-24.84\%$ / $-23.46\%$; Turnover $27.93\%$ / $29.59\%$.
- Gemini masked news: Net return $+2.122$ / $+0.999$ bps/day; Sharpe $+0.08$ / $-0.00$; Max Drawdown $-30.15\%$ / $-21.77\%$; Turnover $28.38\%$ / $29.51\%$.
- 13 of the 18 individual portfolios operate at negative net returns. Positive annualized returns occur only in Gemini news conditions, with the highest reaching only $2.16\%$ annualized.

#### 3. Four-level reasoning curve and audit harm (DeepSeek, 48 formation dates, 68 return dates, Appendix B / Figure 3a)
- **Numerical**:
  - Low minus None: $-0.529$ bps/day ($95\%$ CI $[-16.954, +15.896]$)
  - Maximum minus Low: $-4.346$ bps/day ($95\%$ CI $[-8.979, +0.286]$)
  - Maximum minus None: $-4.875$ bps/day ($95\%$ CI $[-20.319, +10.569]$)
  - Secondary adjacent steps: high minus low $-2.839$, maximum minus high $-1.507$ bps/day. Monotonically declining with reasoning effort.
- **Identifiable news**:
  - Low minus None: $-8.525$ bps/day ($95\%$ CI $[-18.208, +1.158]$)
  - Maximum minus Low: $+4.472$ bps/day ($95\%$ CI $[-1.595, +10.538]$)
  - Maximum minus None: $-4.053$ bps/day ($95\%$ CI $[-12.949, +4.843]$)
  - Secondary adjacent steps: high minus low $-0.167$, maximum minus high $+4.639$ ($95\%$ CI $[+0.376, +8.903]$). Favorable local step fails to beat zero reasoning.
- **Masked news**:
  - Low minus None: **$-9.016$ bps/day** ($95\%$ CI $[-16.248, -1.784]$) $\longrightarrow$ **statistically significant economic harm**.
  - Maximum minus Low: $+0.770$ bps/day ($95\%$ CI $[-4.812, +6.352]$)
  - Maximum minus None: $-8.246$ bps/day ($95\%$ CI $[-17.641, +1.149]$)
  - Secondary adjacent steps: high minus low $+1.289$, maximum minus high $-0.519$ bps/day. Every positive reasoning level stays below zero reasoning.

#### 4. Stochastic generation instability (48 audit dates, 3 repeated runs, Section 5.3 / Table 10)
- **Masked news individual generation effects**:
  - DeepSeek audit: Gen 1 $-7.490$, Gen 2 $-9.327$, Gen 3 $-10.231$ bps/day (all negative; average within return date $-9.016$ bps/day).
  - GPT audit: Gen 1 $+5.800$, Gen 2 $-6.665$, Gen 3 $-2.371$ bps/day (sign flip; average within return date $-1.079$, $95\%$ CI $[-5.173, +3.015]$; ensemble score portfolio $-0.957$, $95\%$ CI $[-6.814, +4.900]$).
  - Gemini audit: Gen 1 $+1.777$, Gen 2 $+7.918$, Gen 3 $-0.630$ bps/day (sign flip; average within return date $+3.022$, $95\%$ CI $[-3.377, +9.421]$; ensemble score portfolio $+1.609$, $95\%$ CI $[-6.545, +9.764]$).
- **Tail overlap and rank agreement (Table 10)**:
  - GPT numerical: Score $\rho = .946$, Tail Jaccard $= .642$ (none) / $.657$ (low), Identical tails $= .000$.
  - GPT identifiable news: Score $\rho = .899 / .911$, Tail Jaccard $= .591 / .589$, Identical tails $= .000$.
  - GPT masked news: Score $\rho = .905 / .915$, Tail Jaccard $= .567 / .583$, Identical tails $= .000$.
  - Gemini numerical: Score $\rho = .858 / .741$, Tail Jaccard $= .515 / .359$, Identical tails $= .000$.
  - Gemini identifiable news: Score $\rho = .811 / .692$, Tail Jaccard $= .479 / .363$, Identical tails $= .000$.
  - Gemini masked news: Score $\rho = .816 / .669$, Tail Jaccard $= .461 / .355$, Identical tails $= .000$.
  - Exactly **$0.0\%$** of audited formation dates reproduced identical portfolio tails across repeated generation calls.

#### 5. Compute token and dollar expenditures (Table 3)
- DeepSeek-Flash: 16,176 tasks, 801,697,928 prompt tokens, 288,221,145 completion tokens, 268,969,372 reasoning tokens, Cost **$297.52 USD**, invalid tasks $0.00\%$.
- GPT-5.6 Luna: 8,088 tasks, 360,029,538 prompt tokens, 11,992,166 completion tokens, 371,323 reasoning tokens, Cost **$41.98 USD**, invalid tasks $0.99\%$.
- Gemini 3.1 Flash-Lite: 8,088 tasks, 507,532,598 prompt tokens, 17,670,460 completion tokens, 7,928,611 reasoning tokens, Cost **$75.56 USD**, invalid tasks $2.35\%$.
- Total: 32,352 tasks, **$415.05 USD** total inference expenditure.

#### 6. Sensitivity checks and diagnostics
- **Moving-block bootstrap (MBB-5, 50,000 resamples, Table 6)**: All 9 annual contrasts remain inconclusive. DeepSeek masked news audit harm remains significant: $95\%$ CI $[-17.929, -3.477]$ bps/day. Cohort bootstrap gives $[-15.482, -2.281]$ bps/day.
- **Transaction cost sweep (5 to 50 bps, Section E)**: GPT numerical ranges from $+3.530$ (5 bps) to $+3.619$ (50 bps); identifiable news ranges from $-0.647$ to $-0.460$; masked news ranges from $+0.004$ to $+0.332$. All remain inconclusive.
- **Portfolio width sweep (5, 10, 15, 20 names per side, Table 8)**: 35 of 36 exploratory cells show no material benefit. DeepSeek masked news at 20 names per side ($+5.769$ bps/day, unadjusted $p < .05$) has Holm-adjusted $p = 1.000$ across the 36 cells.
- **Minimum detectable effect (Table 9)**: 80% MDE ranges from $6.200$ to $19.156$ bps/day, confirming that annual samples of 241 days have wide sampling uncertainty relative to the $+0.25$ bps/day target.

### Independently reproduced

Not independently reproduced. No LLM API calls were executed, no CRSP or EODHD panels were re-evaluated, and no portfolio returns were recomputed for this record.

Arithmetic and internal consistency verification performed by this Scout:
1. Reconciled net return differences between low and baseline from Table 7 with Table 2 estimates:
   - DeepSeek numerical: $-0.217 - (-6.376) = +6.159$ bps/day (exact match).
   - DeepSeek identifiable news: $-4.008 - (-4.386) = +0.378$ bps/day (exact match).
   - DeepSeek masked news: $-3.963 - (-5.412) = +1.449$ bps/day (exact match).
   - GPT numerical: $+0.033 - (-3.506) = +3.539 \approx +3.540$ bps/day (within $0.001$).
   - GPT identifiable news: $-2.113 - (-1.487) = -0.626$ bps/day (exact match).
   - GPT masked news: $-3.442 - (-3.483) = +0.041 \approx +0.040$ bps/day (within $0.001$).
   - Gemini numerical: $-4.204 - (-4.962) = +0.758$ bps/day (exact match).
   - Gemini identifiable news: $+1.275 - (+1.417) = -0.142$ bps/day (exact match).
   - Gemini masked news: $+0.999 - (+2.122) = -1.123$ bps/day (exact match).
2. Verified DeepSeek 4-level audit decomposition:
   - Numerical: $-0.529 + (-2.839) + (-1.507) = -4.875$ bps/day (exact match to Maximum-None).
   - Identifiable news: $-8.525 + (-0.167) + 4.639 = -4.053$ bps/day (exact match to Maximum-None).
   - Masked news: $-9.016 + 1.289 + (-0.519) = -8.246$ bps/day (exact match to Maximum-None).
3. Verified token expenditure sums:
   - Total tasks: $16{,}176 + 8{,}088 + 8{,}088 = 32{,}352$.
   - Total cost: $\$297.52 + \$41.98 + \$75.56 = \$415.06$ (matches printed $\$415.05$ before rounding).

### Negative evidence

The entire paper constitutes rigorous negative evidence regarding the commercial and practical efficacy of inference-time reasoning in quantitative equity ranking:
1. **Zero material benefit detected**: Across all 9 primary tests on 241 trading days in 2024, not a single combination of model backbone and information condition produced a net return improvement meeting the modest $+0.25$ bps/day threshold.
2. **Statistically significant economic harm**: In the controlled 3-generation audit on masked news, DeepSeek low reasoning caused $-9.016$ bps/day loss ($95\%$ CI $[-16.248, -1.784]$) relative to zero reasoning.
3. **Nonmonotonic performance response**: In DeepSeek, increasing reasoning effort from none to low, high, and maximum yielded declining performance in numerical data and irregular swings in news data; maximum reasoning failed to beat zero reasoning across all three input conditions.
4. **Stochastic generation instability**: Repeated generations produced sign flips in portfolio returns (GPT masked news: $+5.800$ to $-6.665$ bps/day; Gemini masked news: $+7.918$ to $-0.630$ bps/day), and zero audit formation dates achieved identical portfolio constituent tails.
5. **Absolute portfolio loss**: 13 of the 18 evaluated portfolios generated negative net annualized returns after 10 bps trading costs (e.g. DeepSeek numerical baseline: $-6.376$ bps/day, Sharpe $-0.80$, MDD $-32.03\%$).
6. **Guaranteed cost vs uncertain payoff**: Inference costs totaled $\$415.05$ over 32,352 tasks (268.97M reasoning tokens in DeepSeek alone), representing a deadweight operational loss in the absence of incremental alpha.

## Falsification plan

All thresholds below are **research-defined falsification thresholds** unless explicitly attributed to the source. Any failure under these gates confirms the hypothesis that test-time reasoning fails to deliver economic alpha in systematic trading.

- **Gate F1 -- Out-of-sample year replication (`research-defined falsification threshold`)**: Evaluate the identical prompt, JSON schema, and portfolio mapping on calendar year 2025 across the same 100-stock CRSP universe.
  - *Failure condition*: Across the 9 low vs baseline contrasts, the mean net return difference fails to achieve $L > +0.25$ bps/day in at least 7 of 9 conditions, or produces $U < 0$ (statistically significant harm) in any condition.
  - *Action*: Reject the premise that reasoning upgrades baseline trading models.
- **Gate F2 -- Nonmonotonicity confirmation (`research-defined falsification threshold`)**: Test a 4-level reasoning ladder (none, low, high, maximum) on a holdout sample of 50 formation dates.
  - *Failure condition*: The Spearman rank correlation between reasoning effort level and net return difference is negative or non-significant ($p > 0.05$).
  - *Action*: Maintain the prohibition against treating reasoning budget as a monotonic optimization hyperparameter.
- **Gate F3 -- Stochastic tail stability gate (`research-defined falsification threshold`)**: For any LLM score proposed for production deployment, execute 5 stochastic generations on 30 consecutive formation dates.
  - *Failure condition*: Mean Tail Jaccard similarity across generation pairs falls below $0.80$, or fewer than $20\%$ of dates have identical long/short constituent tails.
  - *Action*: Disqualify the strategy from execution as non-deterministic and unhedged against sampling noise.
- **Gate F4 -- Net-of-cost hurdle (`research-defined falsification threshold`)**: Apply a realistic institutional cost ladder ($5, 10, 20, 35$ bps one-way) plus actual API inference expense for an assumed $\$10\text{M}$ capital base.
  - *Failure condition*: Net annualized alpha minus inference expense is $\le 0.0\%$ at 10 bps cost.
  - *Action*: Confirm economic unviability.
- **Gate F5 -- Unmasked vs masked narrative overthinking gate (`research-defined falsification threshold`)**: Compare reasoning impact on unmasked vs masked news text.
  - *Failure condition*: Performance degradation under masked news persists ($U < 0$), confirming that extra reasoning latches onto spurious narrative patterns when entity anchors are removed.
  - *Action*: Reject LLM reasoning over non-standardized or obfuscated textual inputs.

## Crypto portability

Portability status: **`unproven`** (described as research interpretation; the cited primary source contains zero cryptocurrency data, zero perpetual futures, and zero 24/7 session evaluations).

- **Mechanism portability**:
  - The concept of feeding numerical market features (funding rates, order-flow imbalance, rolling volatility, volume ratios) or news/social text into an LLM with adjustable reasoning budgets directly transfers to crypto perpetual markets (`research-proposed`).
  - However, because test-time reasoning failed to generate incremental value on highly liquid US equities, its portability to crypto is subject to severe adverse friction:
    1. *Higher trading fees and turnover*: Crypto perpetuals carry maker/taker fees ($2$ to $5$ bps taker) and funding costs ($8$-hour funding payments). With daily portfolio turnover averaging $24.48\%$ to $31.19\%$ (source-reported in Table 7), aggressive rebalancing would deplete capital even faster.
    2. *Inference latency vs 24/7 continuous trading*: DeepSeek maximum reasoning or multi-step thinking introduces substantial API latency ($5$ to $30+$ seconds per call). In crypto perpetuals, where volatility spikes and liquidations occur on minute timescales, latency risks severe execution slippage.
    3. *Extreme narrative noise*: Crypto social media and news feeds exhibit extreme hype, sybil activity, and coordinated market manipulation. As demonstrated by the paper's masked-news findings, extended reasoning on noisy narrative text amplifies hallucination and reduces net returns.
- **Classification**: Porting this framework to crypto must be classified as adapted/unproven. Any live deployment is completely unproven and unjustified by existing empirical evidence.

## Limitations

- `data gap`: Evaluation code and prompts are retained by authors and planned for GitHub release, but no repository URL is published at the capture date; actual prompt hashes, raw completion logs, and vendor market data are not redistributed.
- `underspecified`: Linear transaction cost model (10 bps) excludes price impact, bid-ask spread dynamics, borrow availability, and short locate fees.
- `unproven`: Prospective profitability is completely unproven; 13 of 18 baseline/low portfolios exhibited negative net returns in 2024.
- `not independently reproduced`: Primary results are derived directly from the pinned primary source text, TeX source, and PDF tables; independent API re-execution was not performed.
- `sample limitation`: Historical backtest restricted to a single calendar year (2024) across 100 large/liquid US equities; findings cannot be assumed identical in other macro regimes or asset classes.
- `provider dependence`: Tested backbones (DeepSeek-Flash, GPT-5.6 Luna, Gemini 3.1 Flash-Lite) reflect provider API states as of early/mid 2026; subsequent provider checkpoint updates or parameter changes may alter behavior.

## Implementation status

`implementation_status: not-implemented`. Nothing from this record has been implemented in our research stack. No LLM scoring pipeline was built, no CRSP or EODHD feeds were fetched, no Qlib candidate card was created, and no NautilusTrader strategy was coded. No paper trading, testnet, or live trading has occurred or is authorized.

## Adoption boundary

This record is research material only. Its presence in this repository does **not** mean:
- Passed Research Intake Review
- Entered Hermes Wiki Brain
- Entered the production candidate pool
- Completed Qlib full backtest validation
- Became a frozen survivor or leaderboard entry
- Validated alpha or profitable strategy
- Approved for implementation, paper trading, testnet, or live trading

Status: `research-only`, `implementation_status: not-implemented`, `adoption: not-approved`, `approval_scope: research-only`.

## Related Wiki records

Verified existing pages in Hermes Wiki Brain (resolved read-only from `/Users/hong/.hermes/wiki/quant/`):
- [[quant/alphar1-context-aware-alpha-screening-llm-reasoning-grpo-2026-09-03]] -- Post-training RL (GRPO) for reasoning trajectories in formulaic alpha screening; distinct from inference-time compute scaling on fixed models.
- [[quant/trading-r1-curricular-reinforcement-learning-llm-reasoning-2026-09-05]] -- Curricular RL fine-tuning for financial trading agents; addresses training-time reasoning rather than inference-time test-time compute.
- [[quant/llm-strategy-discovery-leakage-safe-search-deflated-eval-2026-09-04]] -- Methodology for preventing lookahead leakage and backtest overfitting in LLM strategy discovery.
- [[quant/ordinal-gates-cardinal-bets-llm-confidence-exposure-coupling-2026-09-05]] -- Coupling LLM confidence estimates to position sizing; directly relevant to the score formula $s = q(0.5 + 0.5c)$.
- [[quant/small-cap-alpha-beta-separation-uncertainty-aware-llm-portfolio-2026-09-02]] -- Uncertainty-aware portfolio construction with language models.
- [[quant/sharpe-deflated-multiple-testing-2026-08-27]] -- Deflated Sharpe Ratio and multiple-testing corrections across backtest searches.
- [[quant/signal-to-executable-pnl-costs-2026-08-28]] -- Execution frictions, turnover costs, and latency hurdles in systematic trading.

## Sources

1. Jiayi Chen and Guiling Wang, *The Price of Thought: Does Test-Time Reasoning Pay in LLM Trading?*, `arXiv:2609.30705v1 [cs.AI]`, submitted Fri 25 Sep 2026 02:28:01 UTC, CC BY 4.0. Landing page: https://arxiv.org/abs/2609.30705 (read 2026-09-30).
2. Pinned PDF: https://arxiv.org/pdf/2609.30705v1 -- 1,038,149 bytes, SHA-256 `c66e22b00491bbdbafa54a87c42c3749b1f61ff325aa9093a09b42e5414c16ea`, 13 pages, extracted via `pypdf 6.16.2` (78,114 characters) and read end to end on 2026-09-30. Primary source for all narrative and empirical figures.
3. arXiv HTML full text: https://arxiv.org/html/2609.30705v1 -- 399,563 bytes, SHA-256 `b586f5ec9da6f05b304360df28387e3a5ec11e023b7334f0af8e3559c581c05e`, fetched and inspected 2026-09-30.
4. arXiv TeX source: https://arxiv.org/src/2609.30705v1 -- 530,406 bytes gzip tar, SHA-256 `44762e361723bab253957e1e4acab85e5d05bf4d2e8025d836f05bb69db3c0e5`. Extracted files `sigconf.tex`, `methods.tex`, `results.tex`, `appendix.tex`, and `figure2.tex` directly verified on 2026-09-30 for exact equations, JSON contracts, and table cells.
5. arXiv DataCite DOI: https://doi.org/10.48550/arXiv.2609.30705 (landing states 'pending registration', checked 2026-09-30).
6. Dedup and arithmetic evidence produced by this Scout run: whole-checkout `rg -uuu` identity audit returning zero hits, and python arithmetic verification script confirming exact reconciliation between Table 2 and Table 7 net return differences and DeepSeek 4-level audit decomposition.
