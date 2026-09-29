---
schema: strategy-research-record-v1
title: "Hierarchical AI Multi-Agent Fundamental Investing: Merrill-Lynch-Clock plus Industry-Momentum Sector Gating, Four Firm-Level Scoring Agents, PPO Agent-Weight Allocation and EWMA Volatility Scaling (CSI 300 constituents, daily, long-only, 2019–2024)"
created: 2026-09-30
updated: 2026-09-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - llm-reasoning
  - multi-agent
  - reinforcement-learning
  - macro-regime
  - cross-sectional
  - equity
status: research-only
confidence: medium
source_as_of: 2025-10-24
sources:
  - "https://arxiv.org/abs/2510.21147 (arXiv:2510.21147v1 [q-fin.PM], submitted Fri, 24 Oct 2025 04:38:37 UTC; landing read 2026-09-30)"
  - "https://arxiv.org/pdf/2510.21147v1 (pinned v1 PDF, 31 pages, 986281 bytes, SHA-256 95186bb4d05aed32af14c5cfda66444083c5908d3c46c7537d2d63c14208cfbc, fetched 2026-09-30)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Section 3.3 states that the framework 'demonstrates robust efficacy, consistently achieving enhanced risk-adjusted returns and reduced volatility relative to baseline strategies', but Table 1 prints Ours STD 18.94 against baseline STDs 13.05 / 13.41 / 13.39 / 8.23 / 12.97 and Table 3 prints Ours STD 28.20 against 17.68 / 11.80 / 17.98 / 15.34 / 18.19 / 21.79, i.e. the proposed system has the HIGHEST annualised volatility of every row in both samples; the same tables also show Ours MDD (-24.58 training, -12.52 testing) worse than KDJ (-17.89, -9.14), RSI (-8.64) and MACD (-11.84) in the respective samples. Unreconciled in the pinned v1 text."
  - "Section 1 claims the framework 'consistently outperforms all benchmark models in both training and testing sample', but MASS — the only state-of-the-art multi-agent baseline and the one named in the abstract — has no row in Table 1 or Table 2 (training sample); it appears only in Table 3 and Table 4 (testing sample). The training-sample dominance claim is therefore unverifiable for the headline baseline."
  - "Section 3.4 says the risk-scaling ablation 'isolates the role of risk management in improving the Sortino Ratio and reducing maximum drawdown', yet Table 5 prints w/o Risk Scaling MDD = -16.49, byte-identical to Full Model MDD = -16.49, while w/o Risk Scaling CR (190.27) exceeds Full Model CR (185.33). The table shows no drawdown reduction from risk scaling and shows it costing 4.94pp of cumulative return."
  - "Table 5 ('Ablation Study of Model Performance') prints a Full Model row (CR 185.33, AR 32.08, Sharpe 1.92, MDD -16.49, Calmar 1.95) that does not match Table 1's Ours row (CR 167.52, AR 34.77, Sharpe 1.84, MDD -24.58, Calmar 1.42) even though both are presented as the complete system, and Table 5's caption states no sample window. Research-computed implied trading-day counts (T = CR x 252 / AR) put Table 1 and Table 2 at T = 1,214 (the stated 2019-01-01 to 2023-12-31 training window) and the six Table 5 rows at T = 1,453-1,456 (consistent with 2019-01-01 to 2024-12-31, i.e. train plus test), but the paper never says so; Table 5's Full Model MDD -16.49 also equals Table 2's Ours-alpha MDD -16.49 while its CR 185.33 equals neither Table 1's 167.52 nor Table 2's 146.10. Unreconciled."
  - "Section 3.3 praises 'MASS, ContestTrade' — the identifier 'ContestTrade' occurs exactly once in the whole pinned document and is never defined, never used for the proposed system (which Section 2.2 calls the 'QuantMental investment framework') and never appears in any table row label. Unexplained name."
  - "Notation conflict: Section 2.1 defines S as the industry-level feature tensor (S in R^{T x ds}) and F as the firm-level tensor (F in R^{N x T x df}), while Appendix Table EC.6 lists 'M, F, S, B' as 'Macro-, Industry-, Firm-, and benchmark-level data', i.e. F = industry and S = firm. Section 2.5 then writes the allocation rule p_t = f_theta(F, S, B, ...) using both symbols, so the inputs to the final portfolio rule are ambiguous as printed."
---

# Hierarchical AI Multi-Agent Fundamental Investing: Merrill-Lynch-Clock plus Industry-Momentum Sector Gating, Four Firm-Level Scoring Agents, PPO Agent-Weight Allocation and EWMA Volatility Scaling (CSI 300 constituents, daily, long-only, 2019–2024)

## Provenance

**Primary source identity.** arXiv preprint `arXiv:2510.21147v1 [q-fin.PM]`, title *Hierarchical AI Multi-Agent Fundamental Investing: Evidence from China's A-Share Market*, landing page `https://arxiv.org/abs/2510.21147`, pinned PDF `https://arxiv.org/pdf/2510.21147v1`. The landing submission history prints exactly one version: `[v1] Fri, 24 Oct 2025 04:38:37 UTC (817 KB)`; submitter `Xiaowei Zhang [view email]`; `citation_date` / `citation_online_date` = `2025/10/24`. The **`Comments` field is absent**, the **Journal-reference field carries no printed value**, and there is **no external/publisher DOI** — the only DOI anywhere in the metadata is the arXiv-issued DataCite DOI `https://doi.org/10.48550/arXiv.2510.21147` (identical to the PDF `/DOI`). The landing `Subjects` line reads `Portfolio Management (q-fin.PM) ; Artificial Intelligence (cs.AI)` with q-fin.PM primary; PDF `/arXivID` = `https://arxiv.org/abs/2510.21147v1`. Licence: the landing licence link and the PDF `/License` field both resolve to `creativecommons.org/licenses/by-nc-nd/4.0/` → **CC BY-NC-ND 4.0** (no derivatives). Publication status therefore is **arXiv v1 preprint only; no peer-review, acceptance or proceedings statement appears anywhere in the pinned metadata or text** (`source_as_of: 2025-10-24` = v1 submission date). The landing prints v1 as `(817 KB)` while the served artefact is 986,281 bytes (≈963 KiB) — two representations of the same document, recorded as printed and **not reconciled**.

**Author list (three-way match).** Exactly eight authors, identical ordering in (a) the landing `citation_author` meta (`He, Chujun` / `Huang, Zhonghao` / `Li, Xiangguo` / `Luo, Ye` / `Ma, Kewei` / `Xiong, Yuxuan` / `Zhang, Xiaowei` / `Zhao, Mingyang`), (b) the PDF page-1 title block and (c) the PDF `/Author` metadata (`Chujun He; Zhonghao Huang; Xiangguo Li; Ye Luo; Kewei Ma; Yuxuan Xiong; Xiaowei Zhang; Mingyang Zhao`): **Chujun He, Zhonghao Huang, Xiangguo Li, Ye Luo, Kewei Ma** (Faculty of Business and Economics, University of Hong Kong; printed emails `skylar@connect.hku.hk`, `huangzh0624@connect.hku.hk`, `u3590480@connect.hku.hk`, `kurtluo@hku.hk`, `u3596913@connect.hku.hk`), **Yuxuan Xiong** (Department of Mathematics, University of Hong Kong, `u3637747@connect.hku.hk`), **Xiaowei Zhang, Mingyang Zhao** (Department of Industrial Engineering and Decision Analytics, Hong Kong University of Science and Technology, `xiaoweiz@ust.hk`, `mingyang.zhao@connect.ust.hk`). No ORCID, no funding statement, no conflict/competing-interest statement, no acknowledgments, no data-availability statement and no code-availability statement appear anywhere in the pinned PDF (census: `github` 0, `orcid` 0, `acknowledg` 0, `competing` 0, `source code` 0, `reproduc` 0) → all of those fields `data gap`.

**Pinned PDF read-back (primary-source checksum, performed 2026-09-30).** 31 pages, 986,281 bytes, SHA-256 `95186bb4d05aed32af14c5cfda66444083c5908d3c46c7537d2d63c14208cfbc`; pypdf 6.16.2 extraction yields 78,376 characters over 31 pages, read end to end: Abstract, §1 (incl. §1.1.1–§1.1.4), §2 (§2.1–§2.5, Algorithm 1), §3 (§3.1–§3.4, Tables 1–5, Figures 2–4 captions), §4, the 32-item reference list, and the e-companion (EC.1 metrics, EC.2.1–EC.2.3 data tables, EC.3 macro-agent configuration selection with Table EC.5, EC.4 notation Table EC.6). PDF `/Title` matches the landing title, `/Producer pikepdf 8.15.1`, `/Creator arXiv GenPDF (tex2pdf:e76afa9)`. A few LaTeX table rows overprint in the text layer (e.g. `KDJ 23.33 4.678.23 4.770.57 0.98-17.890.26`); every quoted cell below was re-split against its column header and re-checked by the arithmetic verifier. The experimental full-text HTML `https://arxiv.org/html/2510.21147v1` was fetched this run at 445,358 bytes and **not** used as the reading copy.

**Implementation artefact.** No repository, artifact, dataset or supplementary code is named anywhere in the pinned document → there is no commit to pin, and reproducibility and public-use rights (beyond the CC BY-NC-ND 4.0 text licence) are `data gap`.

**Repository-wide dedup audit (2026-09-30, hidden-inclusive).** `rg -uuu` over the entire checkout — including `.git`, `.mimo-worktrees`, `.agents`, `.hermes` and `coverage_manifest.csv` (1,088,787 bytes) — for each of `2510.21147`, `Hierarchical AI Multi-Agent Fundamental Investing`, `Chujun He`, `Zhonghao Huang`, `Xiangguo Li`, `Kewei Ma`, `Yuxuan Xiong`, `Xiaowei Zhang`, `Mingyang Zhao`, `QuantMental`, `ContestTrade`, `2505.10278`, `Multi-Agent Simulation Scaling` → **0 files for every token**. `coverage_manifest.csv` → **0** hits for `2510.21147` / `21147` / `hierarchical-ai-multi`. Mechanism-level scan returned only unrelated prose: `Merrill Lynch` 4 files (the DDPG partial-information pairs record `partial-information-regime-filtering-ddpg-ornstein-uhlenbeck-pairs-trading-2026-09-05.md`, the equity-options investor-fears record, and two `.mimo-worktrees` copies), `investment clock` 1 file (`llm-macro-analog-cpi-nowcast-factor-ranking-walkforward-2026-09-22.md`), `industry momentum` 3 files (`lstm-learnable-sector-embeddings-cross-sectional-reversal-2026-09-02.md` plus two worktree copies), `volatility target` 163 files (shared vocabulary only). Positive control `novy-marx` → **33 files before this write** (34 after, the `+1` being this record's own dedup sentence), proving the index is live. Post-write identity re-scan for `2510.21147`, `QuantMental` and `Hierarchical AI Multi-Agent` returns **exactly this one record**. `git log --oneline -20` was inspected only as a convenience glance (head `a596537`, the AlphaPareto record).

**Four-axis distinction against the closest existing records.** `multimarket-senseai-multi-agent-llm-regime-adaptive-equity-selection-2026-09-04.md` (source: Fatouros & Metaxas, arXiv:2604.17327v1) is a multi-agent LLM equity-selection study with regime-rotating agent attribution; it has no formulaic Merrill-clock sector prefilter, no PPO weight policy and no volatility-scaling protective layer. `llm-top-down-gics-sector-allocation-macro-news-sentiment-2026-09-25.md` (source: Quek et al., arXiv:2503.09647v5) makes the *sector* decision with an LLM on S&P 500 in a long-short book, whereas this source derives sector weights from a deterministic macro clock plus industry momentum on CSI 300 in a long-only book. `adaptive-alpha-weighting-ppo-llm-generated-alphas-2026-09-05.md` (source: Chen & Kawashima, arXiv:2509.01393v2) applies PPO to weights over *LLM-generated formulaic alphas*; this source applies PPO to weights over *four role-specialised analysis agents* under a sector constraint, with behaviour cloning, action simulation and a Sharpe-based reference weight from K-means. `rice-alpha-point-in-time-issuer-local-event-graph-llm-stock-scoring-2026-09-29.md` (source: Liu et al., arXiv:2609.34004v1) corrects an LLM score with a point-in-time typed-event graph on Nasdaq-100/HSI weekly books — a graph mechanism, a different universe and a different horizon. `moira-language-driven-hierarchical-reinforcement-learning-pair-trading-2026-09-05.md` (source: Giannouris et al., arXiv:2605.01954v1) uses hierarchical RL to choose *actions in a pairs-trading* problem, not to weight agents inside a single-name cross-sectional book. `llm-macro-analog-cpi-nowcast-factor-ranking-walkforward-2026-09-22.md` (source: Guan & Chen, arXiv:2606.22719v1) makes macro inputs leakage-aware via real-time nowcasts for factor ranking; this source uses raw published macro series with no release-lag treatment. Every pair differs in source identity **and** in at least one of mechanism, signal construction, universe/market type, horizon/regime or material data dependency → independent record under the dedup contract.

## Economic mechanism

### Source-reported

The authors frame the contribution as an **architecture, not a new premium**. §1.1.4 and §2 state that single-technology pipelines under-use unstructured text and macro context, that monolithic end-to-end models are hard to audit, and that existing LLM trading agents "often focus on single-stock trading or lack a comprehensive hierarchical framework for portfolio construction". The organising principle is "a hierarchical, role-differentiated multi-(AI)-agent system that mirrors the top-down investment process" of a macro-fundamental fund, with "a clear separation of responsibilities across levels — alpha generation by specialized agents, portfolio construction via adaptive aggregation, and risk control through exposure management". The claimed causal channel for the top layer is explicit: the macro prefilter "dynamically focus[es] stock pools where the signal-to-noise ratio could be higher", "grounded in financial theory, such as the well-documented industry momentum effect (Moskowitz and Grinblatt 1999): context is set once, then propagated to lower layers", building on the Merrill Lynch investment clock (Merrill Lynch 2004) and industry rotation (Grauer et al. 1990). The allocation layer is claimed to "respond to regime shifts by reallocating emphasis among fundamentals, technicals, and text-driven insights", amplified by an RL policy that "systematically amplifies the influence of agents with superior historical performance". The protective layer is claimed to improve "the Sortino Ratio and reducing maximum drawdown" (§3.4) during "extreme events such as policy shocks or geopolitical crises" (§2).

### Research interpretation

Four separable, individually falsifiable components; the source's own ablation (Table 5) is the only evidence offered that each contributes, and that ablation has no stated period:

- **Regime / sector gate (conditional breadth):** a deterministic Merrill-Lynch-Clock state from (direction of CPI year-over-year growth, PMI above/below 50) assigns prior industry weights, blended at `λ = 0.25` with equal-weighted top-`m` industry momentum; the surviving industry set is the only stock pool seen downstream. Hypothesis: conditioning the cross-section on a macro/industry state raises signal-to-noise enough to beat unconditional stock selection.
- **Primary signals (four role-specialised scorers):** Fundamental (multi-year accounting), Technical (price/volume), News (LLM sentiment over feeds), Report (LLM over disclosures). Hypothesis: heterogeneous, partly text-derived scores carry information that no single structured pipeline captures.
- **Confirmation / aggregation (PPO over agent weights):** a daily PPO policy allocates weight across the four agents, clipped Top-`k`, biased toward a K-means reference weight that maximises expected Sharpe, rewarded for beating an equal-weight baseline, trained with action simulation plus behaviour cloning. Hypothesis: *adaptive* reweighting on realised agent performance beats any fixed blend.
- **Risk / exit (EWMA volatility scaling):** a multiplicative exposure factor `β_t = σ_tgt / σ̂_{t−1}` scales the long-only book down in high volatility, up to a maximum of 1. Hypothesis: the reported Calmar/Sortino gains come from exposure scaling rather than from selection.

No component is *assumed* to contribute alpha; the record deliberately keeps the aggregation and the risk layer separate from the predictive claim (README rule 8: risk management is not alpha).

## Signal

Reconstructed as far as the pinned text allows. Items marked `research-proposed` are Scout choices needed to make the rule executable and are **not** the source's; items marked `underspecified` cannot be recovered from the source at all.

- **Formation timestamp.** Daily, after the market closes. §3.1: "To prevent look-ahead bias, agents' decisions on trading day T are generated exclusively from masked inputs observed up to day T−1"; §2.4.2: "Performance is evaluated out-of-sample by applying the learned policy to the next day's returns, typically using closing prices. After the market is closed, the agent is trained using the updated data and decides the weight allocation for the next day." Timezone and session convention: `underspecified`. Macro release lags (CPI/PMI/M1/M2 publication dates) are **not** addressed: `underspecified`.
- **Lookback.** Per agent: Fundamental "requires extensive financial data spanning up to five years"; News "a shorter horizon of one month"; Technical "across multiple temporal horizons"; Report over the company's disclosure history. Exact windows: `underspecified`. Industry momentum uses a set `N` of look-back windows — the set itself: `underspecified`. Volatility scaling uses an EWMA variance `σ̂²_{t−1} = (1−λ) Σ_j λ^{j−1} r²_{t−j}` over an `n`-day window with decay `λ` — both `underspecified`.
- **Sector gate.** Classify `R_t ∈ {Recovery, Overheating, Stagflation, Recession}` from the sign of `π^YoY_t` and `PMI_t >/< 50`; map to a hand-coded prior industry weight vector `w^macro` (Recovery → technology/industrials/consumer discretionary; Overheating → commodities/energy/materials; Stagflation → utilities/staples/healthcare; Recession → staples/healthcare, "bonds or defensive equities"); compute `M_{j,t} = Σ_{n∈N} w_n R^{(n)}_{j,t}`, rank industries per horizon, keep the top `m` at equal weight `1/m`; combine `w^industry_{j,t} = λ w^macro_{j,t} + (1−λ) w^mom_{j,t}`; the tradable pool is `{i ∈ S^CSI_t : industry(i) ∈ arg top-m w^final}`. **`λ = 0.25` is source-reported** (e-companion EC.3: "the Merrill Lynch Clock:Industry Momentum configuration with a 25:75 weighting was selected for the Macro agent … chosen based on its superior risk-adjusted performance, demonstrated by the highest combined Sharpe and Sortino ratios (2.514) among the evaluated configurations"). `m`, `N` and the horizon weights `w_n`: `underspecified`.
- **Stock scores.** `z^{(a)}_{t,i} = f_{ϕ_a}(X^{(a)}_{i,t−n:t})` for each agent `a`, collected into `z_{t,i}`. Fundamental inputs named: ROE, net profit, revenue, asset-to-debt ratio (plus the EC.2.3 field list). Technical inputs named: EMA momentum, RSI mean reversion, ATR volatility, Bollinger Bands / ADX / Hurst exponent "statistical arbitrage", "Through a weighted ensemble of these signals" — ensemble weights `underspecified`. News: `z^news = f_LLM(News Articles_{i,1:t})` with current volatility in working memory. Report: `z^report = f_LLM(Reports_{i,1:t})` over five areas (investor research/inquiry records, legal enforcement and dishonesty, financial-performance analysis, distribution plans, institutional holding proportions). LLM prompts: `underspecified`.
- **Aggregation.** Final score `P_t = { ρ(z_{t,i}, w^industry_t, w^agent_t) : i ∈ S^ind_t }` — **`ρ` is never defined**. The RL state is `[x^{(a)}_t : a ∈ A]` with each `x^a` encoding `N` days of agent returns plus top-`k` membership frequency, the last action weight and a reference weight `w^{ref*}` obtained by K-means clustering that maximises `E[R] − r_f / sqrt(Var[R])`. Action: `w̃^agent = softmax(π_θ(s)/τ)`, `w^agent = Normalize(TopK(w̃^agent + β_ref w^{ref*}))`. Reward `r_{t,i} = λ_1 ( R_t(w^agent_t) − R_t^def )` — excess over the equal-weight baseline. Training: PPO clipped surrogate + MSE + entropy + behaviour-cloning loss (MSE + cross-entropy against a top-`k`-ranked expert action), with action simulation over expert/specific/uniform/current weight distributions plus `N(0,σ²)` noise; discount `γ` "set to be close to zero". `Top-k`, `τ`, `β_ref`, `γ`, `λ_1`, the `β_PPO/β_MSE/β_Entropy/β_BC` coefficients, the mixture ratios `(α_expert, α_specific, α_uniform, α_current)` and the K-means cluster count: **all `underspecified`**.
- **Portfolio construction.** §2.5: `p_t = f_θ(F, S, B)` with `1ᵀp_t = 1`, `p_t ⪰ 0` — "the nonnegativity enforces **long-only** allocations". The *form* of `f_θ` and the number of names held are `underspecified`; the only concrete book rule in the text is that "each specialized agent can form a stand alone portfolio by investing in the **top decile** of its ranked list", which describes the per-agent diagnostic portfolios, not necessarily the combined book (`research-proposed` default if forced: top decile of the combined score, equal weight, clipped by `β_t`).
- **Risk layer.** `β_t = σ_tgt / σ̂_{t−1}`, tradable weights `p̃_t = β_t p_t`, "reduces positions when market volatility is extreme and gradually increases them when volatility is moderate (up to a maximum scale of 1)". `σ_tgt`: `underspecified`. §2.5 additionally notes "IF contracts can be traded on the China Financial Futures Exchange as a hedging instrument", but the rule actually specified is a scaling-to-cash rule with no short leg; whether index futures are used at all is `data gap`.
- **Cadence.** "At each trading day t, the RL allocates weights" and §2.1 refers to "rebalancing date t" → **daily rebalance** (`research-proposed` reading of an otherwise unstated cadence, since no other frequency appears). Holding period: 1 session for the weight decision; stock-level holding is `underspecified` because `ρ` is undefined.
- **Direction.** **Long-only, no short leg anywhere in the pinned text** (`short sale` / `short-sell` / `shorting` all 0; the sole `hedg` hits are "macro-fundamental based hedge funds" in the motivation and the IF-contract sentence).
- **Exit rules.** None beyond the daily reweighting; no stop, no take-profit, no time-based exit: `not stated in source`.
- **Overall:** the *architecture* is specified; the *executable rule* is **underspecified** at the `ρ` / `f_θ` / Top-k / `m` / `N` / `σ_tgt` level. It cannot be presented as reproducible evidence.

## Required data

- **Universe / instrument:** CSI 300 index constituents, Chinese A-share market, cash equities, CNY-quoted, `S^CSI_t ⊆ {1..n}` at each rebalancing date. Inclusion/exclusion, as-of membership, reconstitution handling, ST/suspension and delisting treatment: **`data gap`** (census: `survivorship` 0, `point-in-time` 0, `delist` 0, `suspension` 0).
- **Venue:** Shanghai and Shenzhen stock exchanges (implied by "the CSI 300 index … top 300 stocks listed on the Shanghai and Shenzhen stock exchanges"); explicit venue-selection rule: not stated. Data vendor: **never named** → `data gap`.
- **Timeframe:** daily bars and daily macro/industry/firm panels; news and reports referenced daily.
- **Fields required (as named by the source):**
  - Macro: M1 money supply, M2 money supply, CPI year-over-year growth, official PMI (EC.2.1).
  - Industry: CSRC industry classification codes for listed companies, industry index daily returns (EC.2.2).
  - Firm price/volume: open, high, low, close, adjusted close, trading volume; MACD, RSI, KDJ, EMA, ATR, Bollinger Bands, ADX, Hurst exponent.
  - Fundamentals (EC.2.3, 30 fields): CapEx, cash & equivalents, close, current assets, current liabilities, dividends paid, EBIT, earnings before tax, EPS, EV/EBIT, EV/EBITDA, FCF, goodwill, gross profit margin, intangible assets, interest expense, market value, net income, operating costs, operating margin, operating profit, operating revenue, paid-in capital, R&D expenses, ROE, ROIC, revenue, shareholders' equity, total assets, total liabilities.
  - Text: "daily news feeds are aggregated from Google and Baidu"; analyst reports covering "Investor Research and Inquiry Records, Legal Enforcement and Dishonesty Details, Company Financial Performance Analysis, Stock Distribution Plans and Institutional Investor Holding Proportions".
  - Benchmark: CSI 300 index level (excess-return tables); risk-free rate `r_f` **assumed to be 0** (EC.1).
- **Point-in-time / availability:** publication timestamps, release lags, revision handling and adjustment conventions are never discussed (`look-ahead` appears once, covering only the T−1 masking sentence). **`data gap`.**
- **Timestamp/timezone:** not stated → `underspecified`.
- **Missing data:** not stated; no imputation rule, no stale/suspended-print handling → `data gap`.
- **Obfuscation (source-reported):** "the firm-level features are deliberately obfuscated prior to their utilization by the scoring agents" and §3.1 "we obfuscate industry & company identifiers before submission to the model in order to prevent information leakage" from Qwen3-32B's pretraining. The obfuscation transform itself: `underspecified`.
- **Funding/fee/spread needs:** none modelled (see Execution assumptions).

## Execution assumptions

Cost determination was made at **Methods level** from §2.2, §2.4, §2.5, §3.1, §3.2, §3.4, EC.1 and EC.3, plus a whole-document term census of the pinned 78,376-character text:

| Term | modelled occurrences | reading |
|---|---|---|
| `transaction cost` | **0** | no cost model exists |
| `slippage` | **0** | `data gap` |
| `bid-ask` / `spread` | **0 / 0** | `data gap` |
| `commission` | 3 | all non-cost: 2× "China Securities Regulatory Commission", 1× literature sentence about human advisers |
| `turnover` | 1 | literature sentence ("commission-driven turnover" by human advisers); no turnover quantity is ever reported |
| `market impact` / `latency` / `fill` / `maker` / `taker` / `order type` / `limit order` | **0** | `data gap`, never zero |
| `liquidity` | 3 | all non-friction: M1/M2 definition, "portfolio adjustments incorporating liquidity conditions", Tobin (1958) reference |
| `capacity` | 3 | all prose ("modeling capacity", "its capacity to generate", "capacity for precise introspection") |
| `funding` | **0** | — |
| `leverage` / `leverage(s)` | 7 | all the *verb* ("leverages firm-level features"); no balance-sheet leverage anywhere |
| `margin` | 4 | "Gross Profit Margin" / "Operating Margin" / "Profit Margin" in EC.2.3 |
| `borrow` | 1 | EC.2.3 gloss "Interest Expense: Cost incurred by an entity for borrowing funds" |
| `participation` | 1 | "the participation puzzle" in the literature review |
| `risk-free` | 7 | EC.1 assumes `R_f = 0` |
| `walk-forward` / `holdout` / `placebo` / `benjamini` / `fdr` / `multiple test` / `deflated` | **0 / 0 / 0 / 0 / 0 / 0 / 0** | no validation hygiene and no multiplicity control |
| `crypto` / `bitcoin` / `perpetual` | **0 / 0 / 0** | zero crypto content |

The one place the source *addresses* cost states the opposite of a model — §2.4: "**Without considering the cost of changing the portfolio**, the objective can be viewed as maximizing the return of the next trading day, so the discount factor is set to be close to zero." Combined with the zero-occurrence census, this means:

- **Signal-to-order timing:** decisions are made after the close on day `T−1` data and applied to day `T` returns, "typically using closing prices"; execution price convention is otherwise `underspecified`.
- **Order type / fill model / partial fills:** `data gap` (never stated, never modelled).
- **Fees / commission / stamp duty / slippage / spread / impact:** **no cost parameter appears anywhere**; reported returns must be treated as **gross of trading costs**, and whether any cost was applied at all is `data gap` / `not stated in source`. The A-share stamp duty on sells, transfer fees and broker commission are never mentioned.
- **Turnover / capacity / liquidity cap:** `data gap` — never reported, never modelled.
- **Leverage / margin / financing:** `data gap`; the rule is long-only with `β_t ≤ 1` implied by "up to a maximum scale of 1", so residual cash is possible but never described.
- **Borrow / shorting:** `data gap` and structurally absent (long-only).
- **Funding (crypto sense):** not applicable — `data gap` for the source's own market.
- **Latency / inference cost:** `data gap`; LLM inference cost for a daily Qwen3-32B call over ~300 names is never reported.
- **Failure handling:** `data gap`.
- **Non-trading assumptions that ARE stated:** risk-free rate fixed at 0 (EC.1); `p_t ⪰ 0` long-only; identifier obfuscation; T−1 input masking.

## Evidence

### Source-reported

All figures below are third-party claims from the pinned v1 PDF, **gross of any transaction cost** (no cost model exists), with the table they are printed in. `AR` = annualised return, `STD` = annualised standard deviation, `DD` = downside deviation, `MDD` = maximum drawdown, all in percent unless noted; Sharpe/Sortino/Calmar use `R_f = 0`.

**Table 1 — Performance in Training Sample (2019-01-01 → 2023-12-31):**

| Strategy | CR | AR | STD | DD | Sharpe | Sortino | MDD | Calmar |
|---|---|---|---|---|---|---|---|---|
| SMA | -1.06 | -0.21 | 13.05 | 9.03 | -0.02 | -0.02 | -46.50 | -0.01 |
| RSI | 18.61 | 3.72 | 13.41 | 9.61 | 0.28 | 0.39 | -28.48 | 0.13 |
| SIGN | 17.93 | 3.59 | 13.39 | 9.31 | 0.27 | 0.39 | -28.82 | 0.12 |
| KDJ | 23.33 | 4.67 | 8.23 | 4.77 | 0.57 | 0.98 | -17.89 | 0.26 |
| MACD | 24.93 | 4.99 | 12.97 | 8.61 | 0.38 | 0.58 | -39.41 | 0.13 |
| **Ours** | **167.52** | **34.77** | **18.94** | **11.41** | **1.84** | **3.05** | **-24.58** | **1.42** |

**Table 2 — Performance of Excess Returns in Training Sample (vs CSI 300):** SMA alpha `-23.11 / -4.62 / 14.20 / 9.85 / -0.33 / -0.47 / -50.55 / -0.09`; RSI alpha `-3.44 / -0.69 / 13.86 / 9.91 / -0.05 / -0.07 / -49.69 / -0.01`; SIGN alpha `-4.12 / -0.82 / 13.88 / 9.64 / -0.06 / -0.09 / -29.35 / -0.03`; KDJ alpha `1.28 / 0.26 / 17.44 / 11.86 / 0.01 / 0.02 / -43.87 / 0.01`; MACD alpha `2.88 / 0.58 / 14.28 / 9.57 / 0.04 / 0.06 / -35.31 / 0.02`; **Ours alpha `146.10 / 30.33 / 16.57 / 10.07 / 1.83 / 3.01 / -16.49 / 1.84`**.

**Table 3 — Performance in Testing Sample (2024-01-01 → 2024-12-31):**

| Strategy | CR | AR | STD | DD | Sharpe | Sortino | MDD | Calmar |
|---|---|---|---|---|---|---|---|---|
| SMA | -1.53 | -1.53 | 17.68 | 10.95 | -0.09 | -0.14 | -17.09 | -0.09 |
| RSI | 0.64 | 0.64 | 11.80 | 7.42 | 0.05 | 0.09 | -8.64 | 0.07 |
| SIGN | 16.53 | 16.53 | 17.98 | 10.66 | 0.92 | 1.55 | -11.89 | 1.39 |
| KDJ | 11.91 | 11.91 | 15.34 | 8.54 | 0.78 | 1.40 | -9.14 | 1.30 |
| MACD | 10.84 | 10.84 | 18.19 | 10.66 | 0.60 | 1.02 | -11.84 | 0.92 |
| MASS | 7.01 | 7.01 | 21.79 | 14.57 | 0.32 | 0.48 | -20.41 | 0.34 |
| **Ours** | **55.41** | **55.41** | **28.20** | **14.90** | **1.96** | **3.72** | **-12.52** | **4.43** |

**Table 4 — Performance of Excess Returns in Testing Sample (vs CSI 300):** SMA alpha `-17.40 / -17.40 / 11.94 / 10.09 / -1.46 / -1.72 / -19.41 / -0.90`; RSI alpha `-15.23 / -15.23 / 17.79 / 14.51 / -0.86 / -1.05 / -24.94 / -0.61`; SIGN alpha `0.66 / 0.66 / 11.49 / 9.15 / 0.06 / 0.07 / -12.20 / 0.05`; KDJ alpha `-3.96 / -3.96 / 14.85 / 11.48 / -0.27 / -0.35 / -15.12 / -0.26`; MACD alpha `-5.03 / -5.03 / 11.18 / 8.77 / -0.45 / -0.57 / -7.43 / -0.68`; MASS alpha `-10.16 / -10.16 / 12.04 / 9.11 / -0.84 / -1.12 / -21.66 / -0.47`; **Ours alpha `39.22 / 39.22 / 17.60 / 10.56 / 2.23 / 3.71 / -6.44 / 6.09`**.

**Table 5 — Ablation Study of Model Performance (caption states NO sample window):** Full Model `185.33 / 32.08 / 16.75 / 10.15 / 1.92 / 3.16 / -16.49 / 1.95`; w/o Risk Scaling `190.27 / 32.93 / 18.05 / 11.10 / 1.82 / 2.97 / -16.49 / 2.00`; w/o Combine Opt. `98.56 / 17.06 / 13.72 / 8.94 / 1.24 / 1.91 / -13.23 / 1.29`; w/o Text Process `143.36 / 24.81 / 16.57 / 10.57 / 1.50 / 2.35 / -17.16 / 1.45`; w/o Structured Data `87.87 / 15.21 / 19.57 / 12.24 / 0.78 / 1.24 / -27.81 / 0.55`; w/o All `14.36 / 2.49 / 4.99 / 3.45 / 0.50 / 0.72 / -13.83 / 0.18`.

**Table EC.5 — Macro-agent configuration selection (training period):** Merrill Lynch Clock : Industry Momentum `25:75` → `89.30 / 17.86 / 22.40 / 10.40 / 0.797 / 1.717 / -41.00 / 0.436`; `50:50` → `88.79 / 17.76 / 22.57 / 11.11 / 0.787 / 1.599 / -41.84 / 0.424`; `75:25` → `63.22 / 12.65 / 15.65 / 9.25 / 0.808 / 1.367 / -16.48 / 0.767`.

**Prose claims with section provenance.** §1: the framework "consistently outperforms all benchmark models in both training and testing sample" and "rigorous backtesting further confirms its capacity to generate robust excess returns with reduced volatility"; §3.3 restates Table 1 as "CR of 167.52%, a Sharpe ratio (SR) of 1.84, a Sortino ratio of 3.05, and a Calmar ratio of 1.42", the excess series as "cumulative return of 146.10%, with SR, Sortino, and Calmar ratios of 1.83, 3.01, and 1.84", and the test result as "a cumulative return of 55.41% in the testing period, outperforming the best baseline by 38.88" (research-computed: `55.41 − 16.53 = 38.88` percentage points vs SIGN). EC.3 selects the `25:75` macro blend because it has "the highest combined Sharpe and Sortino ratios (2.514)" (research-computed: `0.797 + 1.717 = 2.514`). §3.2 lists the eight metrics (CR, AR, STD, DD, Sharpe, Sortino, MDD, Calmar) and EC.1 defines them with `R_f = 0`.

**Statistical content.** There is **no** p-value, t-statistic, confidence interval, standard error, seed, repeated-run dispersion, bootstrap, Newey–West/HAC correction or hypothesis test anywhere in the pinned text (`p-value` 0, `t-stat` 0 — the single `t stat` substring match is the token `t+1` in Algorithm 1 line 5 — `confidence interval` 0, `bootstrap` 0, `seed` 0, `random` 0). Every number above is a single point estimate.

Source reports these results; they have not been independently reproduced.

### Independently reproduced

not independently reproduced

Arithmetic-only checks were run against the pinned PDF (no data, no code, no third-party execution): a 35-row verifier re-derived `Sharpe = AR / STD`, `Sortino = AR / DD` and `Calmar = AR / |MDD|` for every row of Tables 1, 2, 3, 4, 5 and EC.5 at the printed rounding (tolerance 0.015 for the two-decimal tables, 0.006 for the three-decimal EC.5 table) — **exit 0, 0 failures**. The same run confirmed the prose identities `55.41 − 16.53 = 38.88`, `0.797 + 1.717 = 2.514`, and produced two diagnostics that the paper does not print:

1. **Implied trading-day counts** under `T = CR × 252 / AR`: Table 1 → **1,214**, Table 2 → **1,214**, all six Table 5 rows → **1,453–1,456**, Tables 3/4 → **252**. The 1,214 count matches the stated 2019-01-01→2023-12-31 training window and 1,456 matches 2019-01-01→2024-12-31 (train + test), which is why Table 5's Full Model row cannot equal Table 1's Ours row; the 252 count for a 2024-only window is inconsistent with a calendar-2024 A-share session count (research context, not from the source: roughly 242 sessions), i.e. the test tables appear to set `AR = CR` rather than apply the training tables' annualisation.
2. **Geometric annualisation of Table 1's CR over the stated 5-year training window** gives `(1 + 1.6752)^(1/5) − 1 = 21.75%`, against the printed `AR = 34.77%`; the paper states no annualisation convention (EC.1 says only "the average return of the portfolio per year") → convention is `data gap`.

Both diagnostics are **research-computed**, not source-reported.

### Negative evidence

1. No transaction-cost model of any kind: `transaction cost` 0, `slippage` 0, `bid-ask` 0, `spread` 0, `market impact` 0, `latency` 0, `fill` 0, `maker` 0, `taker` 0, `order type` 0 occurrences; the only cost-adjacent sentence is §2.4's explicit "Without considering the cost of changing the portfolio".
2. Turnover is never reported (the single `turnover` hit is a literature sentence about human advisers) on a book that is re-weighted **daily** — the single most important missing number for a daily long-only A-share strategy.
3. Gross-versus-net status of Tables 1–5 is never stated; with no fee, stamp-duty, commission or slippage parameter anywhere, the printed returns are at best gross.
4. Capacity, ADV and liquidity constraints: 0 modelled occurrences; no participation cap, no position limit, no market-impact study.
5. A **single out-of-sample year** (2024-01-01 → 2024-12-31); `walk-forward` 0, `holdout` 0, `placebo` 0 — no second window, no rolling origin, no sub-period split.
6. **Zero statistical inference**: `p-value` 0, `t-stat` 0, `confidence interval` 0, `bootstrap` 0, `seed` 0 — every headline number is a single point estimate with no dispersion.
7. **Zero multiplicity control**: `benjamini` 0, `fdr` 0, `multiple test` 0, `deflated` 0 — despite four independent per-agent parameter searches, a 3-configuration macro-blend selection, an RL hyperparameter search and six ablation contrasts.
8. §3.1 states plainly: "In the training period, parameter search is conducted for each agent independently … parameters `ϕ*_a` are optimized to maximize its standalone annualized Sharpe ratio", then "fixed and directly applied to the testing period" — i.e. in-sample Sharpe maximisation over a 5-year window feeding a 1-year test.
9. EC.3 shows the macro layer itself was selected on the training period by ranking three `λ` configurations on combined Sharpe+Sortino (2.514 vs 2.386 vs 2.175) — another uncorrected selection step.
10. Weak baseline suite: five zero-to-low-parameter technical rules plus the index plus MASS; no size, value, profitability or reversal control, no style regression, and `beta` 0 occurrences — so no attribution of the excess return to anything other than "the system".
11. The strongest single test baseline, `SIGN` (sign of the past-20-day return, CR 16.53, Sharpe 0.92), is parameter-free, while the proposed system carries dozens of tuned quantities; the comparison is therefore between a straw man and a heavily searched pipeline.
12. MASS — the headline state-of-the-art baseline — appears only in the test tables, contradicting §1's claim of dominance "in both training and testing sample".
13. Annualisation convention undocumented and internally inconsistent across tables (research-computed implied T = 1,214 / 1,453–1,456 / 252).
14. Table 5's period is not stated, and its Full Model row does not match Table 1's Ours row (research-computed gaps: CR +17.81pp, Sharpe +0.08, MDD +8.09pp).
15. §3.4's claim that risk scaling reduces maximum drawdown is contradicted by Table 5, where `w/o Risk Scaling` MDD equals `Full Model` MDD exactly (-16.49) while its CR is higher (190.27 vs 185.33) — risk scaling costs 4.94pp of return and shows no drawdown benefit in the printed table.
16. §3.3's "reduced volatility relative to baseline strategies" is contradicted by Tables 1 and 3, where Ours has the **highest** STD of every row (18.94 and 28.20).
17. Drawdown is not uniformly better: Ours MDD (-24.58 training, -12.52 testing) is worse than KDJ in both samples and worse than RSI/MACD/SIGN in the test sample.
18. No point-in-time disclosure: `point-in-time` 0, `survivorship` 0, `delist` 0, `suspension` 0 — CSI 300 constituent membership timing, adjustment and delisting rules are never described.
19. Macro inputs are used without publication-lag treatment; CPI and PMI release with a delay that is never modelled, and the only look-ahead statement is the single T−1 masking sentence.
20. News comes from Google and Baidu with no publication timestamps and no vendor; identifier obfuscation is the *only* stated defence against Qwen3-32B pretraining leakage, with no temporal audit or ablation of that defence.
21. No code, no dataset, no artifact, no repository (`github` 0, `source code` 0, `reproduc` 0) → the result is not independently checkable by construction.
22. Final book construction (`ρ`, `f_θ`), book size, Top-`k`, `m`, `N`, `τ`, `β_ref`, `γ`, `σ_tgt`, EWMA decay, PPO coefficients and agent prompts are all `underspecified`.
23. The test window is calendar 2024 only — a single market regime — and there is **no evidence after 2024-12-31**; `crypto`/`bitcoin`/`perpetual` = 0 occurrences.
24. Licence is CC BY-NC-ND 4.0 (no derivatives), which constrains redistribution of the source text itself; this record therefore cites and normalises rather than reproduces the paper.

## Falsification plan

Every threshold below is a `research-defined falsification threshold` (Scout-chosen, not the source's) with an explicit action on failure. **Global rule: no retuning.** The macro blend `25:75`, the Merrill-Lynch four-regime table, the top-`m` rule, the four agent definitions, the Top-`k` masking, the PPO/BC objective, the `R_f = 0` convention, the long-only constraint, the volatility-target rule, the obfuscation scheme, the Qwen3-32B backbone and the 2019–2023 / 2024 split are frozen as printed; any parameter the source leaves unstated must be **pre-registered before any 2024 result is inspected** and is then frozen too. A failed gate may not be rescued by re-optimising any of them — failure changes the record's status, not the configuration.

- **F1 — Parameter-disclosure gate.** Obtain or pre-register `ρ`/`f_θ` (the final book rule), book size, `m`, the industry lookback set `N`, `Top-k`, `τ`, `β_ref`, `γ`, `λ_1`, `σ_tgt`, EWMA decay and window, PPO/BC coefficients, action-simulation mixture ratios, K-means cluster count, agent prompt templates and the obfuscation transform. Fail if any of these cannot be obtained or must be invented without pre-registration. Action: reproduction is blocked, the `Signal` section stays `underspecified`, and the record remains `research-only` permanently.
- **F2 — Printed-value reproduction.** Re-run the described system on the same splits. Fail if 2024 test CR misses `55.41%` by more than `±3.0`pp, if test Sharpe misses `1.96` by more than `±0.15`, if training CR misses `167.52%` by more than `±5.0`pp, or if training Sharpe misses `1.84` by more than `±0.15`. Action: mark every headline `unverified`; record stays `research-only`.
- **F3 — Data and point-in-time gate.** Rebuild the CSI 300 panel from a named vendor with as-of membership, corporate-action adjustment, suspension and delisting rules, and macro/news publication timestamps. Fail if membership is ex-post, if delisted names are silently dropped, or if no vendor can be identified. Action: no implementation attempt; permanent `research-only`.
- **F4 — Signal-timing gate.** Recompute every agent score strictly from information available before the decision timestamp, including CPI/PMI release lags and news publication times (signal from data through `T−1`, trade at the next session). Fail if out-of-sample 2024 CR falls below **half** the printed value (`< 27.71%`) or Sharpe `< 0.98`. Action: reject the tradable reading; retain only the architectural claim.
- **F5 — Cost ladder and turnover gate (`research-proposed`).** Report annualised turnover first, then reprice at 0 / 1 / 2 / 5 / 10 / 20 / 50 bp per side plus the A-share commission, stamp duty (sells) and transfer fee. Fail if annualised turnover exceeds `500%` of book value, or if net Sharpe at `10 bp` per side falls below `1.00`. Action: reclassify the `55.41% / 1.96` pair as cost-fragile.
- **F6 — Capacity gate (`research-proposed`).** Cap participation at 20% of 20-day ADV per name. Fail if Sharpe degrades by more than `0.30` versus the unconstrained run. Action: mark capacity `unproven` and bound position size explicitly.
- **F7 — Family-wide multiplicity gate.** Apply Benjamini–Hochberg at `q < 0.10` over the full reported family (22 strategy-vs-ours comparisons across Tables 1–4, 5 ablation contrasts in Table 5, 3 macro-`λ` contrasts in Table EC.5 = 30 comparisons), plus a deflated-Sharpe check whose trial count equals the number of configurations actually inspected across the four per-agent searches, the macro selection and the RL hyperparameter search. Fail if the Ours-vs-SIGN and Ours-vs-MASS comparisons do not survive at `q < 0.10`. Action: significance reclassified as selection artefact.
- **F8 — Seed-stability gate.** Ten independent re-runs per configuration varying only LLM decoding and PPO initialisation, data frozen. Fail if Ours fails to beat SIGN in at least `8 of 10` runs, or if `std(CR) > 25%` of the mean. Action: downgrade to `falsified-robustness`.
- **F9 — Component gate.** The full model must beat every ablation on a stated, identical window. Fail if, on any single stated window, any ablation variant matches or beats the full model on cumulative return or on Sharpe. **Currently failing as printed**: Table 5 shows `w/o Risk Scaling` CR `190.27` above `Full Model` `185.33`, identical MDD `-16.49`, and the table carries no period label. Action: until a labelled rerun reverses it, record risk scaling as return-reducing with no demonstrated drawdown benefit, and treat the ablation as period-ambiguous.
- **F10 — Obfuscation and robustness gate (`research-proposed`).** Three alternative identifier-obfuscation schemes plus ±20% perturbation of `λ` (macro blend) and `Top-k`. Fail if the 2024 Sharpe moves more than `20%` in relative terms under any variant. Action: attribute the result to obfuscation/hyperparameter tuning rather than to the mechanism.
- **F11 — Execution-realism gate.** Replace same-close execution with next-session-open execution plus explicit fill confirmation and a one-session delay on changed names. Fail if net Sharpe drops by more than `0.30` versus the printed `1.96`. Action: reject the close-execution assumption.
- **F12 — Exposure/benchmark gate.** Report beta and factor-adjusted alpha versus the CSI 300 index (and a size/value/profitability control). Fail if beta `> 0.90` and benchmark-relative information ratio `< 0.50`. Action: attribute the return to beta, not to the hierarchical design.
- **F13 — Cross-market and crypto replication gate (`research-proposed`).** Frozen settings on (a) a non-Chinese developed-equity panel (e.g. STOXX 600) and (b) a liquid crypto cross-section. Fail if either panel's out-of-sample 12-month CR `≤ 0` or Sharpe `≤ 0`. Action: restrict the claim to large-cap A-shares; crypto portability stays `unproven`.
- **F14 — Frozen forward window.** Evaluate 2025-01-01 onward (the paper's test ends 2024-12-31) with everything frozen. Fail if forward Sharpe `≤ 0` over ≥ 12 months. Action: reject persistence; record as sample-bound.

## Crypto portability

**adapted.** The pinned text contains **0** occurrences of `crypto`, `bitcoin` or `perpetual`; every empirical claim is on Chinese A-share CSI 300 constituents. The *machinery* (macro-regime gate → industry momentum screen → heterogeneous stock scorers → RL weight allocation → volatility scaling) is instrument-agnostic, so this is a **ported hypothesis, not crypto empirical evidence**, and `adapted` does not mean demonstrated:

- **Macro layer does not port:** the Merrill-Lynch states are built from *Chinese* CPI year-over-year, PMI, M1 and M2. There is no crypto analogue of PMI/M1/M2/CPI, so the top layer of the hierarchy would have to be replaced outright — a different signal, not a translation.
- **Universe and breadth:** CSI 300 is a 300-name large-cap pool with an index committee; liquid crypto cross-sections are far narrower and dominated by BTC/ETH beta, so a top-decile long-only selection over a 300-name benchmark does not transfer directly.
- **Session structure:** daily bars, "after the market is closed" decisions and a next-session return assume exchange sessions; 24/7 candles, venue-specific day boundaries and timezone conventions are undefined in the source and matter more in crypto.
- **Rules that do not exist in crypto:** A-share price limits, ST treatment and suspensions have no direct analogue; token delisting and listing churn are far more severe, and the source is silent on all of them anyway.
- **Costs/execution:** no cost model exists at all, so there is nothing to port; crypto taker/maker fees, real spreads and per-venue impact would have to be added from scratch (they are `data gap` here, not zero).
- **Perpetuals/funding/shorting:** no funding, basis, borrow, margin or liquidation mechanics appear anywhere, and the rule is long-only with no short leg.
- **Point-in-time data:** the source's silence on vendor/membership/adjustment would be more damaging in crypto, where survivorship and re-listing effects are larger.

A port would be a new experiment; `crypto portability: adapted` is not authorization to trade.

## Limitations

- `underspecified`: the final book rule `ρ` / `f_θ`, book size, `m`, the industry lookback set `N`, `Top-k`, `τ`, `β_ref`, `γ`, `λ_1`, `σ_tgt`, EWMA decay and window, PPO/BC coefficients, action-simulation mixture ratios, K-means cluster count, Technical-agent ensemble weights, agent prompt templates, the obfuscation transform, rebalance cadence (only "at each trading day t" and "rebalancing date t" appear), execution price and session convention, annualisation convention, MDD windowing, and the period of Table 5.
- `data gap`: data vendor, as-of CSI 300 membership, survivorship, delisting/suspension and adjustment rules, macro/news publication timestamps, order type, fill model, latency, participation, turnover, capacity, leverage/margin, borrow, spread, market impact, LLM inference cost, gross-vs-net labelling, code/data artifact, ORCID/funding/COI/acknowledgments, and public-use rights beyond the CC BY-NC-ND 4.0 text licence.
- `not independently reproduced`: every performance, risk-ratio and ablation number in this record.
- `unproven`: that the *hierarchical design* (rather than the single 2024 test year, the in-sample Sharpe-maximising per-agent searches, the macro-blend selection, the absence of costs, or the weakness of the baseline suite) produces the reported edge — there is no second window, no statistical inference, no multiplicity control, no turnover report and no beta attribution.
- Disclosed asymmetries: Ours has the highest STD in both samples; Ours MDD is worse than KDJ in both samples; risk scaling raises Sharpe but lowers CR and shows no MDD benefit; the excess series (Table 4) has lower volatility than the raw series (Table 3) — the "reduced volatility" claim holds only for the *excess* series, and only against some baselines.
- Six unreconciled printed statements (`contested: true`, see `contradictions`): the volatility/drawdown claim, the training-sample dominance claim, the risk-scaling drawdown claim, the Table 1 vs Table 5 full-model mismatch, the undefined `ContestTrade` identifier, and the §2.1 vs Table EC.6 notation swap.
- Peer-review status: **arXiv v1 preprint only** — no acceptance, journal or proceedings statement exists in the pinned metadata as of 2026-09-30; single out-of-sample year; zero crypto evidence; single market and asset class.

## Implementation status

`implementation_status: not-implemented`. Nothing from this record has been implemented in our research stack: no hierarchical agent system built, no A-share or CSI 300 data pull, no Qwen3-32B agent run, no backtest, no candidate-pool entry, no Paper / Testnet / Live activity, and no write to any downstream system. No third-party code was cloned or executed (none exists in the source). This artifact is a normalized research capture only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this file in the staging repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered `/results/_handoff/candidates.json`; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet, or live trading. Those stages remain separate and gated.

## Related Wiki records

Verified by `kb_search` on 2026-09-30 across three queries (`multi-agent LLM equity portfolio construction`, `macro regime sector rotation equity selection`, `volatility targeting exposure scaling drawdown control portfolio`); no page was fabricated and **no page was written** — each linked path appeared in a returned result set:

- `[[quant/adaptive-alpha-weighting-ppo-llm-generated-alphas-2026-09-05]]` — PPO over LLM-generated formulaic alphas; same RL-weighting family, different source, different weight targets (alphas vs analysis agents), no sector prefilter or risk layer.
- `[[quant/alphalogics-market-logic-multi-agent-factor-generation-2026-09-05]]` — market-logic multi-agent *factor generation*; multi-agent family, different source and different output object (factors vs a portfolio policy).
- `[[quant/continuous-macro-timing-growth-defensive-style-allocation-2026-09-02]]` — macro-conditioned style allocation with walk-forward evidence; shares the macro-timing layer, different source, different mechanism (style timing vs industry prefilter).
- `[[quant/market-regime-routed-specialist-gbt-asymmetric-hysteresis-2026-09-12]]` — regime-routed specialists with volatility targeting; shares the regime + vol-target structure, different source and different model class.
- `[[quant/sentiment-augmented-drl-alpha-reward-ddpg-active-trading-2026-09-05]]` — sentiment-augmented DRL with an excess-alpha reward; shares the DRL-plus-text structure, different source, different reward and no hierarchy.

Adjacent repository records (file paths, **not** verified Wiki pages): `multimarket-senseai-multi-agent-llm-regime-adaptive-equity-selection-2026-09-04.md`, `llm-top-down-gics-sector-allocation-macro-news-sentiment-2026-09-25.md`, `rice-alpha-point-in-time-issuer-local-event-graph-llm-stock-scoring-2026-09-29.md`, `moira-language-driven-hierarchical-reinforcement-learning-pair-trading-2026-09-05.md`, `llm-macro-analog-cpi-nowcast-factor-ranking-walkforward-2026-09-22.md`, `lstm-learnable-sector-embeddings-cross-sectional-reversal-2026-09-02.md`.

## Sources

1. Chujun He, Zhonghao Huang, Xiangguo Li, Ye Luo, Kewei Ma, Yuxuan Xiong, Xiaowei Zhang, Mingyang Zhao. *"Hierarchical AI Multi-Agent Fundamental Investing: Evidence from China's A-Share Market."* arXiv:2510.21147v1 [q-fin.PM], submitted Fri, 24 Oct 2025 04:38:37 UTC (landing prints `(817 KB)`). Landing page: https://arxiv.org/abs/2510.21147 (retrieved 2026-09-30; no Comments field; Journal-reference field empty; no external DOI; Subjects `Portfolio Management (q-fin.PM) ; Artificial Intelligence (cs.AI)`; one version only; submitter `Xiaowei Zhang`).
2. Pinned full text: https://arxiv.org/pdf/2510.21147v1 — 31 pages, 986,281 bytes, SHA-256 `95186bb4d05aed32af14c5cfda66444083c5908d3c46c7537d2d63c14208cfbc`; every table, figure caption, equation, notation entry and e-companion statement cited above was read directly from this PDF on 2026-09-30 (pypdf 6.16.2, 78,376 characters).
3. arXiv full-text HTML for the same v1: https://arxiv.org/html/2510.21147v1 — 445,358 bytes, fetched 2026-09-30, **not** used as the reading copy.
4. arXiv DOI: https://doi.org/10.48550/arXiv.2510.21147 (the only DOI in the pinned metadata); licence `creativecommons.org/licenses/by-nc-nd/4.0/` (CC BY-NC-ND 4.0), confirmed from both the landing licence link and the PDF `/License` field.
5. Baselines and methods as cited by the source (**not fetched** for this record): MASS — Guo et al. (2025), *MASS: Multi-agent simulation scaling for portfolio construction*, arXiv:2505.10278 (described by the source as "open-source"); Merrill Lynch (2004), *The investment clock*, research report; Grauer, Hakansson and Shen (1990), industry rotation, *Journal of Banking & Finance* 14(2–3): 473–489; Moskowitz and Grinblatt (1999), *Do industries explain momentum?*, *Journal of Finance* 54(4): 1249–1290; Ye, Pei, Wang, Chen and Zhu (2020), RL portfolio management with augmented asset-movement prediction states, AAAI; Zhang, Zohren and Roberts (2019), *Deep reinforcement learning for trading*, arXiv:1911.10107 (source of the volatility-scaling form); Shafiullah et al. (2022), behaviour transformers, NeurIPS; Yang, Liu, Zhong, Walid and Zhu (2020), DRL ensemble strategy, ACM ICAIF.
6. Data dependencies named by the source but **with no vendor identified** (listed for provenance only, not fetched): CPI, M1, M2 and PMI macro series; CSRC industry classification codes and industry index daily returns; daily news aggregated from Google and Baidu; analyst/inquiry/legal-enforcement/company-fitness reports. Backbone LLM: Qwen3-32B (named in §3.1 of the paper; exact model release date not stated).
