---
schema: strategy-research-record-v1
title: "EverMine: Self-Evolution of Research Capabilities in Long-Horizon Portfolio-Conditioned Alpha Discovery (Binance Spot U60, 10-Minute Bars, Qwen3.8-27B & DeepSeek-V4.1-Flash, arXiv:2609.33524)"
created: 2026-09-30
updated: 2026-09-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - factor-mining
  - formulaic-alpha
  - self-evolving-agents
  - negative-evidence
  - falsification
status: research-only
confidence: medium
source_as_of: 2026-09-27
sources:
  - "https://arxiv.org/abs/2609.33524 (arXiv:2609.33524v1 [cs.AI primary, q-fin.ST], submitted Sun, 27 Sep 2026 12:46:09 UTC; landing read 2026-09-30)"
  - "https://arxiv.org/pdf/2609.33524v1 (pinned v1 PDF, 28 pages, 707793 bytes, SHA-256 073e33c4f79f4896bfa12bda2c9f620d6c4c1948f4eed9b1b86ade964c0d0659, fetched 2026-09-30)"
  - "https://arxiv.org/html/2609.33524v1 (pinned v1 HTML full text, 344083 bytes, SHA-256 3ffba7587ab543969cf94e802e0d388432d3d22be14e9c0d1b6273ce6cc23f80, fetched 2026-09-30)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# EverMine: Self-Evolution of Research Capabilities in Long-Horizon Portfolio-Conditioned Alpha Discovery (Binance Spot U60, 10-Minute Bars, Qwen3.8-27B & DeepSeek-V4.1-Flash, arXiv:2609.33524)

## Provenance

**Primary source identity.** arXiv preprint `arXiv:2609.33524v1 [cs.AI]`, cross-listed to `q-fin.ST`. Title: *EverMine: Dissecting the Self-Evolution of Research Capabilities in Long-Horizon Alpha Research*. Canonical landing URL: `https://arxiv.org/abs/2609.33524`. Canonical DOI: `https://doi.org/10.48550/arXiv.2609.33524` (DataCite, identical to PDF `/DOI`).

**Submission and version history.** Exactly one version submitted: `[v1] Sun, 27 Sep 2026 12:46:09 UTC (385 KB)`; submitter `Siyuan Li [view email]`. Landing metadata indicates `citation_date` = `2026/09/27` and `citation_online_date` = `2026/09/27`. The `Comments` field is empty (`None`), the `Journal-ref` field carries no printed value, and there is no external publisher DOI. Licence: arXiv perpetual non-exclusive distribution license (`http://arxiv.org/licenses/nonexclusive-distrib/1.0/`, confirmed from landing page and PDF `/License` field). Publication status is **arXiv v1 preprint under review; no peer-reviewed venue or conference proceedings statement appears in the pinned metadata or text** (`source_as_of: 2026-09-27`). The landing page displays `(385 KB)` for the source gzipped bundle, whereas the served compiled PDF is 707,793 bytes and the full-text HTML is 344,083 bytes; both represent the identical v1 paper.

**Authors and institutions (three-way match).** Authors are identical across (a) landing metadata, (b) PDF title block, and (c) PDF metadata `/Author` (`Siyuan Li; Jiangfeng Zhang; Rui Yao; Weihua Qiu; Mingyang Xu; Zixuan Yuan`):
- **Siyuan Li** (The Hong Kong University of Science and Technology (Guangzhou), `sli974@connect.hkust-gz.edu.cn`, equal contribution)
- **Jiangfeng Zhang** (The Hong Kong University of Science and Technology (Guangzhou), `jzhang67@connect.hkust-gz.edu.cn`, equal contribution)
- **Rui Yao** (The Hong Kong University of Science and Technology (Guangzhou), `ryao663@connect.hkust-gz.edu.cn`, equal contribution)
- **Weihua Qiu** (The Hong Kong Polytechnic University, `weihua.qiu@connect.polyu.hk`)
- **Mingyang Xu** (Singapore Management University, `mingyang.xu.2026@phdacc.smu.edu.sg`)
- **Zixuan Yuan** (The Hong Kong University of Science and Technology (Guangzhou), `zixuanyuan@hkust-gz.edu.cn`, corresponding author)

**Pinned full-text verification (2026-09-30).**
- PDF: 28 pages, 707,793 bytes, SHA-256 `073e33c4f79f4896bfa12bda2c9f620d6c4c1948f4eed9b1b86ade964c0d0659`. Extraction via `pypdf 6.16.2` yielded 109,256 characters across 28 pages, covering Abstract, Sections 1-7, Ethics and Reproducibility Statement, References (35 items), and Appendices A-C (including Tables 1-6 and Figures 1-4).
- HTML: 344,083 bytes, SHA-256 `3ffba7587ab543969cf94e802e0d388432d3d22be14e9c0d1b6273ce6cc23f80`.
- All tables, equations, and prose passages were read end to end on 2026-09-30.

**Code and implementation artefact.** In the Reproducibility Statement, the authors state: *"The market data used in this work are public and can be obtained from their official source. We will provide the necessary code during review and release the code publicly upon acceptance."* The underlying agent runner utilizes DeepSeek Harness (`https://github.com/deepseek-ai/deepseek-harness`). No dedicated repository URL or immutable commit SHA is provided in v1 for the EverMine benchmark itself -> `data gap`.

**Repository-wide deduplication audit (2026-09-30).** `rg -uuu` over the entire checkout (including `.git`, `.mimo-worktrees`, `.agents`, `.hermes`, and `coverage_manifest.csv`) for `2609.33524`, `EverMine`, `Siyuan Li`, `Jiangfeng Zhang`, `Rui Yao`, `Weihua Qiu`, `Mingyang Xu`, `Zixuan Yuan`, and `Dissecting the Self-Evolution of Research Capabilities` returned zero prior mentions in the repository (`coverage_manifest.csv` returned 0 hits). Positive control `novy-marx` returned 36 files across the checkout, verifying search live status.

**Four-axis distinction against closest existing repository records:**
1. `alphapareto-llm-pool-state-pareto-morl-formulaic-alpha-china-ashare-snp500-arxiv-2609.34188-2026-09-29.md` (source: Zhang et al., arXiv:2609.34188v1): Pareto multi-objective reinforcement learning for formulaic alpha discovery on equity universes (CSI 300 / S&P 500) over daily bars. EverMine evaluates LLM self-evolving research capabilities versus fixed capability baselines on crypto spot assets (Binance U60) at 10-minute bar frequency.
2. `mufasa-self-evolving-multi-agent-symbolic-valuation-discovery-arxiv-2609.32746-2026-09-29.md` (source: Koa et al., arXiv:2609.32746v1): Discovers symbolic equity valuation formulas from quarterly fundamental financial statements. EverMine discovers intraday statistical formulaic alphas from high-frequency crypto order-flow and OHLCV klines.
3. `quantaalpha-institutional-price-volume-correlation-intraday-momentum-2026-09-05.md` (source: Tang et al., 2025): Explores human-like hypothesis induction for equity factors; EverMine implements a state-dependent capability-replacement protocol ($S_t = (\mathrm{Hist}_t, \mathrm{Frontier}_t, \mathrm{Cap}_t)$) to isolate the causal value of capability evolution vs fixed capabilities.
4. `vst-verifiable-structured-transport-agentic-alpha-discovery-2026-09-12.md`: Focuses on verifiable structured transport protocols between agent layers; EverMine investigates long-horizon factor portfolio saturation, sequential screening path dependency, and negative results on capability accumulation.
Source identity, economic mechanism, signal construction, and empirical findings differ across all pairs -> independent record under repository dedup criteria.

## Economic mechanism

### Source-reported

The authors address whether an automated research agent's accumulated capabilities (reusable skills, tools, and research rules) continue to improve research productivity as the factor portfolio evolves. They observe:
1. Long-horizon alpha discovery is state-dependent: adding a new factor $x$ into the incumbent portfolio $\mathrm{Frontier}_t$ alters the remaining predictive space ($\delta(x \mid \mathrm{Frontier}_t) = Q(\mathrm{Update}(\mathrm{Frontier}_t, x)) - Q(\mathrm{Frontier}_t)$).
2. As the portfolio covers more predictive structure, many candidate factors that exhibit high standalone predictive power add zero or negligible marginal information (citing Feng et al., 2020; Green et al., 2017).
3. Self-evolving agents are designed to store research feedback into persistent, editable, and reusable capability states $\mathrm{Cap}_t$ (spanning market mechanism explanations, measurement and representation, portfolio gap identification, test design, belief updating, budget allocation, and engineering tools).
4. The central empirical question is whether accumulated capabilities continue to provide positive marginal returns on an evolving predictive frontier, or whether they fail to outperform fixed baseline capabilities under matched compute and token budgets.

### Research interpretation

EverMine serves as a rigorous negative-evidence and falsification study for automated alpha discovery:
- **Marginal Factor Saturation:** Intraday cross-sectional crypto return prediction exhibits rapid saturation. Once a 30-factor portfolio is populated, 93.6% of subsequent factor submissions yield negligible incremental Information Coefficient (mean net IC gain of only 0.0015 to 0.0080 across hundreds of hours).
- **Cognitive & Operational Overhead of Self-Evolution:** Accumulating rules, editing skills, and modifying research procedures consumes substantial agent context and runtime without improving portfolio search efficiency over an agent operating with fixed initial capabilities ($\mathrm{Cap}_0$).
- **Familiar Formula Exploitation vs Novel Exploration:** In mature factor pools, local parameter tuning of existing formula structures produces positive net IC contributions in 16 of 18 trajectories (accounting for 12.8% to 40.0% of net improvements), outperforming unconstrained exploration of new operator structures.
- **Path Dependency in Sequential Portfolio Ingestion:** The value of an alpha candidate is non-monotonic and order-dependent. In historical state replay, factors that showed positive marginal IC at time $t$ reduce the final portfolio IC when submitted sequentially after other candidates, confirming that portfolio-conditioned factor discovery is path-dependent.

## Signal

The factor representation and portfolio aggregation logic are normalized as follows:

- **Signal formation timestamp:** Rebalanced every 10 minutes at the close of each 10-minute bar. Ten-minute bars are aggregated from ten consecutive 1-minute bars in UTC. Input features are formed strictly from data observed up to bar $t$. Timezone: UTC.
- **Lookback windows:** Rolling operators in the expression tree utilize lookback windows ranging from 1 to 1024 bars (i.e. 10 minutes to ~7.1 days). Lag operator $\mathrm{Ref}(x, n)$ with $n > 0$ strictly references historical bars.
- **Input feature fields:** Seven raw market series per asset:
  - $O$ (Open price, first 1-min open)
  - $H$ (High price, maximum 1-min high)
  - $L$ (Low price, minimum 1-min low)
  - $C$ (Close price, last 1-min close)
  - $V$ (Volume, sum of 1-min volumes)
  - $A$ (Turnover in USDT, sum of 1-min turnovers)
  - $\mathrm{VWAP}$ (Volume-weighted average price, $A / V$)
- **Expression tree grammar:** Candidate alpha factor $k$ is an expression:
  $$\mathbf{x}_t^{(k)} = f_{	heta_k}(\{O, H, L, C, V, A, \mathrm{VWAP}\}_{\le t}) \in \mathbb{R}^{|U_t|}$$
  Leaf nodes: market fields or scalar constants. Internal nodes: elementwise unary and binary operators ($+, -, 	imes, /$, sign, log, abs), rolling time-series operators (moving averages, std, min, max), two-series rolling correlation/covariance, conditional operations, and cross-sectional rank ($\mathrm{CSRank}$) evaluated across active universe $U_t$.
- **Cross-sectional standardization:** At each bar $t$, each candidate factor $k$ and the forward label $y_t$ are standardized across active assets $U_t$ to mean 0 and unit variance:
  $$\widetilde{\mathbf{x}}_t^{(k)} = rac{\mathbf{x}_t^{(k)} - \mu_t^{(k)}}{\sigma_t^{(k)}}, \quad \widetilde{\mathbf{y}}_t = rac{\mathbf{y}_t - \mu_{y,t}}{\sigma_{y,t}}$$
  Positions with missing market values are filled with 0 post-standardization.
- **Forward prediction target:** Next-bar close-to-close percentage return:
  $$y_{i,t} = rac{C_{i,t+1}}{C_{i,t}} - 1, \quad i \in U_t$$
- **Portfolio signal aggregation:** With $K$ active factors and signed weights $\mathbf{w} \in \mathbb{R}^K$:
  $$\mathbf{s}_t(\mathbf{w}) = \sum_{k=1}^K w_k \widetilde{\mathbf{x}}_t^{(k)}$$
- **Portfolio evaluation objective (Information Coefficient):**
  $$\mathrm{IC}(\mathbf{w}) = rac{1}{|\mathcal{T}|} \sum_{t \in \mathcal{T}} \mathrm{Corr}_{i \in U_t}(s_{i,t}, \widetilde{y}_{i,t})$$
- **Portfolio update and weight optimization:** When candidate factor $x$ is evaluated, factor weights are refitted jointly via Lasso-regularized quadratic minimization (following AlphaGen, Yu et al., 2023):
  $$\mathbf{w}^* = rg\min_{\mathbf{w}} \left( \mathbf{w}^	op M \mathbf{w} - 2 \mathbf{c}^	op \mathbf{w} + 1 ight) + \lambda \|\mathbf{w}\|_1, \quad \lambda = 0.005$$
  where $c_k = \mathrm{Corr}(\widetilde{\mathbf{x}}^{(k)}, \widetilde{\mathbf{y}})$ and $M_{jk} = \mathrm{Corr}(\widetilde{\mathbf{x}}^{(j)}, \widetilde{\mathbf{x}}^{(k)})$.
- **Admission and rejection criteria:**
  1. Direct correlation filter: If $|\mathrm{Corr}(\widetilde{\mathbf{x}}, \widetilde{\mathbf{x}}^{(j)})| > 0.99$ for any existing member $j$, candidate is rejected immediately.
  2. Fixed capacity constraint: Capacity is capped at $K_{\max} = 30$ factors. If the refitted pool exceeds 30 members, the member with the smallest absolute weight $|w_k|$ is purged. If the candidate factor is the one purged, the update fails; otherwise, the member is replaced.
- **Directionality:** Signed weights $w_k$ can be positive or negative. The portfolio signal $\mathbf{s}_t$ ranks assets cross-sectionally for relative value.
- **Execution trigger & position-sizing rule:** Underspecified by source (`data gap`). Source evaluates predictive IC only. A standard long-short execution rule is `research-proposed`: at each 10-minute bar, sort assets by $\mathbf{s}_t$; go long top decile (top 6 names) with equal weight $1/6$, go short bottom decile (bottom 6 names) with equal weight $-1/6$, dollar-neutral.
- **Holding period:** 1 bar (10 minutes) nominal rebalance cadence. Exit is executed by rebalancing to the new top/bottom deciles. Stop-loss, take-profit, and max holding time are `data gap` (none specified in source).

## Required data

- **Asset universe:** Binance Spot USDT pairs. Dynamic point-in-time Top-60 ($U_m$) selected on the 1st day of each calendar month $T_m$ by trailing 30-day cumulative turnover:
  $$\mathrm{Turnover}_{i,m} = \sum_{	au \in [T_m - 30\mathrm{d}, T_m)} A_{i,	au}, \quad U_m = \mathrm{Top60}_i \, \mathrm{Turnover}_{i,m}$$
  Inclusion filters: minimum 30 days trading history, presence on at least 20 calendar days in lookback, $\ge 95\%$ 1-minute bar coverage. Stablecoins, leveraged tokens, and wrapper assets are excluded.
- **Venue:** Binance Spot exchange (`data.binance.vision`).
- **Market type:** Crypto spot, USDT quote currency.
- **Timeframe:** 10-minute OHLCV klines aggregated from 1-minute bars in UTC.
- **Temporal split:**
  - In-sample development period: 2025-01-01 00:00 UTC to 2025-12-31 23:50 UTC (52,560 bars; 163 unique assets; 3,153,600 nominal asset-bars; 9,864 missing market positions; 99.6872% market coverage; 99.6852% label coverage).
  - Out-of-sample (OOS) evaluation period: 2026-01-01 00:00 UTC to 2026-06-30 23:50 UTC (26,064 bars; 121 unique assets; 1,563,840 nominal asset-bars; 540 missing market positions; 99.9655% market coverage; 99.9616% label coverage).
  - Full sample: 78,624 bars; 199 unique assets; 4,717,440 nominal asset-bars; 10,404 missing positions; 99.7795% coverage.
- **Point-in-time hygiene:** Monthly universe reconstitution uses only data prior to month start; rolling operations use $\mathrm{Ref}(x, n)$ with $n > 0$; labels use next-bar returns with endpoints clipped to split boundaries.
- **Platform storage:** Qlib backend for trading calendar, instrument index, and binary dataset storage.

## Execution assumptions

Cost and execution parameters were audited from the full text of arXiv:2609.33524v1:

| Operational Parameter | Source Treatment | Classification |
|---|---|---|
| Signal-to-order timing | Bar close observation, next-bar return target | Source-reported (mathematical evaluation) |
| Order type | Not specified | `data gap` (`research-proposed`: market order at bar close) |
| Fill model | Evaluates predictive correlation (IC), no fills simulated | `data gap` (`research-proposed`: immediate fill at $C_{i,t}$) |
| Transaction costs / fees | Not modeled; returns are gross | `data gap` (Binance spot VIP 0 taker: 5-10 bps; VIP 9 taker: 1.2-2 bps) |
| Slippage & spread | Not modeled | `data gap` (`research-proposed`: 2.5 bps half-spread on U60) |
| Market impact / capacity | Turnover measured; execution capacity omitted | `data gap` (`research-proposed`: cap at 1.0% of 10-min volume) |
| Borrow / shorting | Spot long-only or unmodelled synthetic short | `data gap` (`research-proposed`: margin borrow fee 2-5% p.a. or USDT perp) |
| Execution latency | 0 ms assumed in mathematical IC | `data gap` (`research-proposed`: 50-200 ms API latency) |
| Failure handling | Missing data zero-filled post-standardization | Source-reported |

## Evidence

### Source-reported

All figures below are third-party empirical findings from `arXiv:2609.33524v1` across 18 long-horizon trajectories (530.5 active runtime hours, 8,774 candidate-factor evaluations, 8,770 recorded portfolio outcomes, 8,215 submissions after capacity reached). **IC values and differences are reported multiplied by 1,000 (i.e. 60.902 corresponds to IC = 0.060902):**

**Table 1 — End-to-end endpoint portfolio IC results:**

| Sample Period | Model | $n_F$ (Fixed) | $n_E$ (Evolving) | Mean Fixed IC ($	imes 10^3$) | Mean Evolving IC ($	imes 10^3$) | Mean Difference $\Delta$ | 95% Bootstrap Interval |
|---|---|---|---|---|---|---|---|
| **Development** (2025) | Qwen3.8-27B | 6 | 6 | 60.902 | 61.643 | +0.741 | `[-1.181, +2.681]` |
| **Development** (2025) | DeepSeek-V4.1-Flash | 3 | 3 | 68.166 | 68.071 | -0.095 | `[-6.819, +6.624]` |
| **OOS** (2026-H1) | Qwen3.8-27B | 6 | 6 | 88.324 | 87.932 | -0.391 | `[-4.158, +3.180]` |
| **OOS** (2026-H1) | DeepSeek-V4.1-Flash | 3 | 3 | 100.779 | 99.141 | -1.637 | `[-18.227, +13.089]` |

*Note: All four 95% difference bootstrap intervals include zero. Explicit capability self-evolution produces no statistically significant improvement over fixed capabilities.*

**Table 2 — Capability-state replacement at matched checkpoints (Qwen3.8-27B, 6 parent runs, 12 paired blocks):**

| Sample Period | Checkpoint | Paired Blocks | $\Delta Q(\mathrm{Cap}_0)$ ($	imes 10^3$) | $\Delta Q(\mathrm{Cap}_t)$ ($	imes 10^3$) | $\widehat{	au}_{\mathrm{cap}}$ ($	imes 10^3$) | 95% Bootstrap Interval |
|---|---|---|---|---|---|---|
| **Development** | 25% | 12 | +2.034 | +1.628 | -0.405 | `[-1.097, +0.119]` |
| **Development** | 75% | 12 | +0.500 | +0.542 | +0.042 | `[-0.494, +0.573]` |
| **OOS** | 25% | 12 | +3.005 | +1.749 | -1.256 | `[-3.107, +0.197]` |
| **OOS** | 75% | 12 | +0.718 | +0.626 | -0.092 | `[-2.048, +1.574]` |

*Note: Holding research history $\mathrm{Hist}_t$ and current portfolio $\mathrm{Frontier}_t$ identical, accumulated capabilities $\mathrm{Cap}_t$ do not outperform initial capabilities $\mathrm{Cap}_0$.*

**Table 3A — Net IC contributions after pool first reaches capacity ($	imes 10^3$):**

| Model & Condition | New Structures | Parameter Tuning of Existing Structures | Exact Resubmissions | Positive Tuning Runs |
|---|---|---|---|---|
| Qwen3.8-27B Fixed | +0.932 | +0.588 | -0.049 | 4 / 6 |
| Qwen3.8-27B Evolving | +1.657 | +0.567 | -0.022 | 6 / 6 |
| DeepSeek-V4.1-Flash Fixed | +5.910 | +2.009 | +0.076 | 3 / 3 |
| DeepSeek-V4.1-Flash Evolving | +6.736 | +0.996 | +0.050 | 3 / 3 |

*Note: Parameter tuning of familiar formula structures accounts for 12.8% to 40.0% of net improvements and contributes positively in 16 of 18 trajectories.*

**Table 3B — Replay of factors screened out by experience-based rules (Qwen Evolving):**

| Batch | Screened Out | Positive on Original Portfolio | Original Endpoint IC ($	imes 10^3$) | Endpoint IC After Additions ($	imes 10^3$) | Net IC Change |
|---|---|---|---|---|---|
| Batch A | 3 | 2 | 61.14162 | 61.12412 | -0.01749 |
| Batch B | 8 | 2 | 61.18655 | 61.17988 | -0.00666 |

*Note: Candidates showing positive standalone marginal IC at time $t$ reduce final portfolio IC when submitted sequentially, confirming path dependency.*

**Table 6 — Development-period factor-pool IC at joint-budget checkpoints:**
- Qwen3.8-27B Fixed: 20% budget: 0.06013 (6 runs); 50%: 0.06066 (6 runs); 80%: 0.06090 (5 runs).
- Qwen3.8-27B Evolving: 20%: 0.05898 (6 runs); 50%: 0.06039 (6 runs); 80%: 0.06149 (6 runs).
- DeepSeek-V4.1-Flash Fixed: 20%: 0.06319 (3 runs); 50%: 0.06431 (3 runs); 80%: 0.06618 (3 runs).
- DeepSeek-V4.1-Flash Evolving: 20%: 0.06216 (3 runs); 50%: 0.06382 (3 runs); 80%: 0.06442 (3 runs).

**Resource consumption averages (Appendix C.6):**
- DeepSeek Fixed / Evolving: 5.8021 / 16.0003 CPU core-hours; USD 2.3403 / 4.2973 model cost; 1000 / 642 evaluations completed.
- Qwen Fixed / Evolving: 7.2205 / 7.2329 CPU core-hours; USD 9.4538 / 9.3240 model cost; 346.0 / 295.3 evaluations completed.

Source reports these figures; they have not been independently reproduced.

### Independently reproduced

`not independently reproduced`

Direct mathematical verifications of the printed tables were performed on 2026-09-30 without third-party code execution:
1. Recomputed all Table 1 differences: $61.643 - 60.902 = +0.741$; $68.071 - 68.166 = -0.095$; $87.932 - 88.324 = -0.392$ (printed $-0.391$, 0.001 rounding delta); $99.141 - 100.779 = -1.638$ (printed $-1.637$, 0.001 rounding delta).
2. Verified Table 3A row sums against Section 5.1 text: Qwen Fixed $0.932 + 0.588 - 0.049 = 1.471$ (matches printed 0.001471); Qwen Evolving $1.657 + 0.567 - 0.022 = 2.202$ (matches printed 0.002202); DeepSeek Fixed $5.910 + 2.009 + 0.076 = 7.995$ (matches printed 0.007995); DeepSeek Evolving $6.736 + 0.996 + 0.050 = 7.782$ (matches printed 0.007782).
3. Verified Table 5 data completeness percentages: Dev missing $9,864 / 3,153,600 = 0.31278\% \implies 99.6872\%$ coverage; OOS missing $540 / 1,563,840 = 0.03453\% \implies 99.9655\%$ coverage; Total missing $10,404 / 4,717,440 = 0.22054\% \implies 99.7795\%$ coverage. All match printed values exactly.

### Negative evidence

1. **Falsification of self-evolving capability efficacy:** End-to-end evaluation reveals no statistically significant benefit from self-evolving capabilities across both local (Qwen3.8-27B) and API-based (DeepSeek-V4.1-Flash) foundation models; all 95% bootstrap intervals span zero.
2. **Negative point estimates in out-of-sample testing:** In the unseen 2026-H1 period, evolving capability agents underperform fixed agents on mean portfolio IC ($\Delta = -0.391$ for Qwen; $\Delta = -1.637$ for DeepSeek).
3. **Negative point estimates in controlled capability-state replacement:** When branched from identical intermediate checkpoints, accumulated capabilities $\mathrm{Cap}_t$ deliver lower subsequent portfolio IC improvements than the initial baseline $\mathrm{Cap}_0$ at early checkpoints ($\widehat{	au}_{\mathrm{cap}} = -0.405$ in Dev, $-1.256$ in OOS).
4. **Pathological screening side-effects:** Experienced-based screening rules discard candidates that possess positive standalone marginal IC, yet sequential addition of those candidates lowers final portfolio IC due to non-convex factor interactions.
5. **Absence of transaction costs:** All reported portfolio ICs are gross of execution frictions. At 10-minute trading frequency, Binance spot maker/taker fees (2-10 bps) and bid-ask spreads will severely attenuate or completely eliminate realized alpha.
6. **Code repository unavailable:** No open-source code release is provided in v1 preprint (`data gap`), precluding direct code-level replication.

## Falsification plan

Every cutoff below is a `research-defined falsification threshold` (Scout-chosen, not the source's) with an explicit action on failure:

- **F1 — Capability self-evolution replication gate (`research-defined falsification threshold`):** Re-run fixed vs evolving capability runs on the Binance Spot U60 dataset. Fail if the 95% bootstrap difference interval for portfolio IC strictly excludes zero in favor of Evolving by more than $+1.0$ IC unit ($+0.00100$). Action: reject the null finding of EverMine and reclassify self-evolving capabilities as conditionally positive.
- **F2 — Out-of-sample IC decay gate (`research-defined falsification threshold`):** Evaluate the frozen 30-factor portfolio discovered on 2025 data across a prospective forward window (2026-07-01 to 2026-12-31). Fail if mean forward portfolio IC drops below 50% of the in-sample mean ($< 0.030$). Action: classify the 30-factor portfolio as overfitted in-sample artifact.
- **F3 — Transaction-cost viability ladder (`research-proposed`, `research-defined falsification threshold`):** Construct an active long-short decile portfolio from $\mathbf{s}_t(\mathbf{w})$ rebalanced every 10-minute bar. Apply a realistic fee/slippage ladder of 0, 1, 2, 5, and 10 bps per side. Fail if net annualized Sharpe ratio falls below 0.50 at $\le 2$ bps per side, or if daily two-way turnover exceeds 300%. Action: declare the 10-minute signal frequency economically unviable on spot markets.
- **F4 — Execution latency & fill delay gate (`research-proposed`, `research-defined falsification threshold`):** Introduce a 1-bar execution lag (signal formed at bar $t$ close, orders filled at bar $t+1$ close / $t+2$ open) plus 100 ms network latency. Fail if portfolio IC decays by $> 35\%$ under a 1-bar delay. Action: attribute apparent predictive power to short-lived microstructure bounce rather than tradable alpha.
- **F5 — Path-dependency orthogonalization gate (`research-defined falsification threshold`):** Replace sequential factor admission with batch orthogonal Gram-Schmidt regression over candidate batches. Fail if batch-orthogonalized final portfolio IC fails to beat sequential admission IC by at least $0.0020$ ($+2.0$ IC units). Action: attribute portfolio divergence to heuristic pruning rather than signal quality.
- **F6 — Parameter-tuning vs structure-discovery ablation (`research-defined falsification threshold`):** Constrain an agent to execute only parameter tuning on the first 10 discovered formula structures vs unconstrained operator search. Fail if the parameter-tuning agent fails to capture at least 60% of the final portfolio IC achieved by the unconstrained searcher. Action: confirm that formula structure discovery exhibits severe diminishing returns relative to parameter calibration.
- **F7 — Perpetual futures funding & basis stress gate (`research-proposed`, `research-defined falsification threshold`):** Port the factor portfolio to Binance USDT-M perpetual contracts, incorporating 8-hour funding rates. Fail if net funding payments consume $> 25\%$ of gross return. Action: restrict strategy deployment strictly to spot rebalancing.

## Crypto portability

**direct.** The primary source itself is natively designed, implemented, and empirically evaluated on crypto markets (Binance Spot USDT pairs, dynamic Top-60 turnover universe, 10-minute klines). No asset-class translation from equities is required:

- **24/7 session structure:** Evaluated on continuous 10-minute bars without overnight gaps or market close auctions.
- **Dynamic turnover universe:** The dynamic monthly U60 universe handles crypto asset turnover shifts and token life-cycles, though stablecoins and wrapped assets are manually excluded.
- **Spot vs perpetual frictions:** The source uses spot market prices. Porting to USDT perpetual contracts requires modeling 8-hour funding rates, liquidation risks, and mark-price basis disconnections (`research-proposed` consideration).
- **Execution cost burden:** Binance spot fees (0.02% to 0.10% per trade) represent a severe hurdle for 10-minute rebalancing that must be explicitly modeled before production consideration.

## Limitations

- `data gap`: Dedicated code repository and factor definitions are not yet publicly released (under review).
- `not independently reproduced`: All empirical findings, ICs, and bootstrap intervals are source-reported point estimates.
- `underspecified`: Trade execution mechanics, order types, fill assumptions, fee models, slippage, and position sizing are omitted; source evaluates mathematical prediction correlation (IC) only.
- `unproven`: Net economic profitability after exchange fees and bid-ask spreads remains unproven; 10-minute bar rebalancing on crypto spot carries heavy turnover friction.
- Single venue: Empirical evaluation is restricted to Binance Spot; cross-exchange transferability (e.g. Coinbase, OKX, Bybit) is unverified.

## Implementation status

`implementation_status: not-implemented`. No strategy code from this paper has been implemented in our research stack. No Binance API keys used, no live data downloaded, no Qlib run performed, no candidate pool entry created, and no downstream pipeline written. This record is a normalized research capture only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this record in the repository does not authorize implementation, paper trading, testnet, or live trading. It represents research-only knowledge preservation of negative empirical evidence regarding self-evolving agents in factor mining.

## Related Wiki records

Verified on disk in `/Users/hong/.hermes/wiki/quant/`:
- `[[quant/vst-verifiable-structured-transport-agentic-alpha-discovery-2026-09-12]]` — Verifiable structured transport protocols for agentic factor discovery.
- `[[quant/alpharjm-reward-jump-memory-sde-critic-symbolic-alpha-2026-09-11]]` — Symbolic alpha generation with jump memory critic.
- `[[quant/adaptive-alpha-weighting-ppo-llm-generated-alphas-2026-09-05]]` — PPO-based dynamic factor allocation over LLM formulaic alphas.
- `[[quant/crypto-cross-sectional-factor-zoo-iterative-alpha-compression-2026-09-01]]` — Factor zoo compression in crypto cross-sections.
- `[[quant/crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01]]` — Microstructure alpha transfer across digital assets.

Adjacent repository staging records:
- `alphapareto-llm-pool-state-pareto-morl-formulaic-alpha-china-ashare-snp500-arxiv-2609.34188-2026-09-29.md`
- `mufasa-self-evolving-multi-agent-symbolic-valuation-discovery-arxiv-2609.32746-2026-09-29.md`
- `quantaalpha-institutional-price-volume-correlation-intraday-momentum-2026-09-05.md`
- `agora-sealed-joint-search-emergent-alpha-scoring-2026-09-12.md`

## Sources

1. **Primary Paper:** Siyuan Li, Jiangfeng Zhang, Rui Yao, Weihua Qiu, Mingyang Xu, Zixuan Yuan. *"EverMine: Dissecting the Self-Evolution of Research Capabilities in Long-Horizon Alpha Research"*. arXiv preprint `arXiv:2609.33524v1 [cs.AI, q-fin.ST]`, submitted Sun, 27 Sep 2026 12:46:09 UTC (landing prints `(385 KB)`).
   - Canonical landing URL: https://arxiv.org/abs/2609.33524
   - Canonical DOI: https://doi.org/10.48550/arXiv.2609.33524
2. **Pinned Full-Text PDF:** `https://arxiv.org/pdf/2609.33524v1` — 28 pages, 707,793 bytes, SHA-256 `073e33c4f79f4896bfa12bda2c9f620d6c4c1948f4eed9b1b86ade964c0d0659`, retrieved and verified 2026-09-30 (109,256 extracted characters).
3. **Pinned Full-Text HTML:** `https://arxiv.org/html/2609.33524v1` — 344,083 bytes, SHA-256 `3ffba7587ab543969cf94e802e0d388432d3d22be14e9c0d1b6273ce6cc23f80`, retrieved 2026-09-30.
4. **Primary Agent Framework:** DeepSeek-AI. *DeepSeek Harness: Everything is a plugin*. Repository: https://github.com/deepseek-ai/deepseek-harness (2026).
5. **Factor Mining Formulation & Update Algorithm:** Shuo Yu, Hongyan Xue, Ao Xiang, Chaoran Cheng, and Shengli Peng. *Generating Synergistic Formulaic Alpha Collections via Reinforcement Learning*. In Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '23), 2023. DOI: https://doi.org/10.1145/3580305.3599831 (Source of AlphaGen factor tree grammar and Lasso pool update).
6. **Data Source:** Binance Data Vision public spot kline archive: https://data.binance.vision/ (USDT spot pairs, 2025-01-01 to 2026-06-30).
