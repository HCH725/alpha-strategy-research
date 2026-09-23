---
schema: strategy-research-record-v1
title: "Beyond Prompting: Agentic-AI Discovered Factor Library Composite Long-Short (US Equity Daily Cross-Section)"
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: low
source_as_of: 2026-04-06
sources:
  - "https://arxiv.org/abs/2603.14288 (arXiv:2603.14288v2 [q-fin.PM], last revised 6 Apr 2026)"
  - "https://arxiv.org/pdf/2603.14288 (pinned primary PDF, 60 pages, 5,047,216 bytes, SHA-256 8fe2b21770af074a0e13667048bc40b3eb85fc03ecde8f5d58938e3aa100e301)"
  - "https://doi.org/10.48550/arXiv.2603.14288 (arXiv-issued DOI, tested 2026-09-24 -> 200 -> arxiv abs)"
  - "https://github.com/allenh16/agentic-factor-investing at full commit cc8bd7d06c26f39dc379157208482fe0da19623e (4 files: README.md, chart_data.json, index.html, project-framework.png)"
  - "https://allenh16.github.io/agentic-factor-investing/ (project homepage cited inside the paper)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Beyond Prompting: Agentic-AI Discovered Factor Library Composite Long-Short (US Equity Daily Cross-Section)

## Provenance

**Primary source (papers).** Allen Yikuan Huang and Zheqi Fan, *"Beyond Prompting: An Autonomous Framework for Systematic Factor Investing via Agentic AI"* (PDF title page renders a shorter variant: *"Beyond Prompting: Autonomous Factor Investing via Agentic AI"* — the metadata/title-page mismatch is itself recorded as source-reported below), `arXiv:2603.14288v2 [q-fin.PM]`.

- **Authors (exactly as source, verified in three places):** abs-page `citation_author` fields `Huang, Allen Yikuan` and `Fan, Zheqi` (2 authors; abs page renders "by Allen Yikuan Huang and 1 other authors"), PDF title block "Allen Yikuan Huang a,b,c, Zheqi Fan b,c,∗", and PDF `/Author` metadata `"Allen Yikuan Huang; Zheqi Fan"`. Affiliations as printed: (a) Guanghua School of Management, Peking University; (b) Division of EMIA, Hong Kong University of Science and Technology; (c) Thrust of FinTech, HKUST Guangzhou. Corresponding email printed in PDF: `zheqi.fan@connect.ust.hk`.
- **Version / date (verified on abs page):** `[Submitted on 15 Mar 2026 (v1), last revised 6 Apr 2026 (this version, v2)]`; PDF metadata `/arXivID …/2603.14288v2`; PDF footer `arXiv:2603.14288v2 [q-fin.PM] 6 Apr 2026`. This record pins **v2**.
- **Publication status:** abs page exposes **no Comments and no Journal reference** (checked 2026-09-24) → **preprint only**. PDF `/License` = `http://arxiv.org/licenses/nonexclusive-distrib/1.0/` (arXiv non-exclusive, not CC).
- **Primary-source checksum performed 2026-09-24:** PDF downloaded from `https://arxiv.org/pdf/2603.14288` — 60 pages, 5,047,216 bytes, SHA-256 `8fe2b21770af074a0e13667048bc40b3eb85fc03ecde8f5d58938e3aa100e301`; extracted text 117,662 characters / 1,708 lines; **§1–§8, Exhibits 1–22, Appendices A–D and References read line-by-line in full** (no reliance on abstract or secondary summaries). DOI `10.48550/arXiv.2603.14288` tested live (HTTP 200 → `https://arxiv.org/abs/2603.14288`).
- **Sample period (PDF §4.1):** CRSP daily stock-level records, **January 2004 through December 2024**; promotion/in-sample selection uses data **through December 2020**; main out-of-sample (OOS) window **January 2021 – December 2024** (N = 1,004 trading days in Exhibits 9/13); §4.1 additionally promises a "post-January 2023 stricter subsample" (never reported anywhere in the paper — see Negative evidence §9).
- **Universe (PDF §4.1, Exhibit 3):** CRSP common stocks on NYSE / AMEX / NASDAQ, minimum price USD 5, minimum 252 observations per stock, target winsorized at 1st/99th percentile by date; sequential screens 39.59M→16.51M observations and 20.37K→**8,052 stocks**. Exchange/session convention (US equity calendar) stated only implicitly; exchange-listing breakdown not reported → `data gap`.
- **Transaction-cost treatment (verified by full-text reads of §7.2, Exhibit 13 caption/formula, §7.3):** a single **flat linear 3 basis points per dollar traded, one-way**, explicitly said to cover "commission and spread"; net series computed as `r_net = r_gross − 0.0003 × Turnover`. **Borrow cost, short availability, price impact beyond the flat bps, latency, capacity/participation, and fill model are absent from the paper** (full-text counts: `borrow` 0, `bid-ask` 0, `slippage` 0, `hard-to-borrow` 0, `commission` appears only inside the 3 bps sentence) → recorded as `data gap`, not inferred as zero.
- **Project homepage / repository:** homepage `https://allenh16.github.io/agentic-factor-investing/` is cited in the PDF (line 28 of the title page and the Data availability statement). The linked GitHub repository `allenh16/agentic-factor-investing` was inspected at immutable commit **`cc8bd7d06c26f39dc379157208482fe0da19623e`** (created 2026-03-14T10:26:08Z, last push 2026-03-14T10:32:10Z, default branch `main`, 3 commits, 4 files: `README.md`, `chart_data.json`, `index.html`, `project-framework.png`). The repository contains **no strategy code and no factor formulas**; `README.md` at that commit is a 26-byte stub (`# agentic-factor-investing`), even though `index.html` tells readers "For methodology and replication, see the project documentation".
- **Repository-wide dedup (deterministic, 2026-09-24):** ripgrep across **all `*.md` files in the repository root, `coverage_manifest.csv`, and all `.mimo-worktrees/…` records** for `2603.14288`, `10.48550/arXiv.2603.14288`, `Beyond Prompting`, `agentic-factor-investing`, `allenh16`, and `agentic factor investing` → **0 hits** (the same sweep also confirmed `strategy-research-record-spec-v2` does not exist in Wiki Brain; canonical spec re-read this run: `quant/strategy-research-record-spec-v1.md`, sha256 `4561578a…ff6fcaa7`). The same authors do appear in this repository on **different source identities** — `llm-augmented-semantic-network-cross-stock-reversal-2026-09-04.md` (`arXiv:2604.19476`) and `crypto-llm-agent-liquidity-scarcity-range-attention-factor-2026-09-01.md` — different papers, different mechanisms, therefore not duplicates of this capture.
- Adjacent agentic/LLM factor-mining records in this repository (`aeap-seads-llm-agentic-factor-discovery-formulaic-alpha-2026-09-03.md`, `alphacfg-grammar-guided-mcts-tree-lstm-formulaic-alpha-2026-09-05.md`, `alphaschema-…`, `alphalogics-…`, `agonalpha-…`, `factorengine-…`, `vst-…`, `agora-…`) are **different source identities with different signal families** (RL / grammar-guided MCTS / plan-space evolution / multi-agent debate / program synthesis); none of them reports this paper's 12-factor turnover/flow library or its US-equity daily decile composite.

## Economic mechanism

### Source-reported

The authors' story (PDF §1, §6.5.2, Exhibit 15) is that an autonomous ReAct/Chain-of-Thought agent proposes **interpretable symbolic price–volume factors** — mostly built from turnover, flow shocks and price-vs-anchor transforms — each jointly accompanied by an economic rationale ("economic regularization"), passes them through a pre-committed in-sample gate (data through 2020), freezes the library, and reports a **blind OOS test over 2021–2024**. Named channels: (i) turnover/flow shocks proxy slow-moving order-imbalance demand and limits-to-arbitrage → short-horizon return **continuation**; (ii) sustained turnover proxies investor attention/crowding with delayed repricing; (iii) market makers and constrained arbitrageurs absorbing inventory gradually, so liquidity-driven price pressure persists; (iv) "Defensive Mean-Reversion": temporarily discounted, below-trend, low-realized-risk names correcting without extreme vol. Signals are combined by a **transparent linear combination** (main benchmark) and a **LightGBM** integrator. Claimed anti-data-mining devices: |t| > 3.0 discovery hurdle (citing Harvey et al., 2016), IS/OOS temporal isolation, frozen OOS library, turnover/cost penalties inside the gate.

### Research interpretation

- **Falsifiable hypothesis:** a daily, always-on cross-section of US equities carries transient order-flow/attention-demand pressure that persists into the next session, monetizable by a daily-rebalanced equal-weight **D10 − D1 decile spread** whose OOS (2021–2024) alpha survives FF6 adjustment and a 3 bps one-way cost drag at ~110 %/day one-way turnover.
- **Component roles (normalized):** Regime: none (always-in). Primary signal: 12 agent-generated turnover/flow/price-anchor factors. Aggregation: linear combination (main; **weights never published**) or LightGBM (**hyperparameters never published**). Execution/risk layer: none — no stop, no sizing rule, no leverage rule exists in the source; daily re-sorting is the only "exit".
- **Critical epistemic boundary:** because **no factor formula is published anywhere** (Exhibit 15's own caption says descriptions are "conceptual and implementation-neutral"), the *specific* strategy is **not reconstructable from the primary source**; only the *family-level* hypothesis (turnover/flow-demand continuation in a broad equity cross-section) is independently testable. Any operationalization below is therefore labeled `research-proposed`.

## Signal

- **Formation timestamp:** factor values computed on day-`t` daily CRSP records; prediction target is the **one-day-ahead (t+1) stock return**; portfolios **rebalanced at each market day** (Exhibit 6 caption). The exact price used for signal and for fills (t close vs t+1 open/close) is **never specified** → `underspecified`.
- **Lookback / primitives (source-reported, §4.2):** ten baseline variables — lagged stock return, market return, absolute stock price, trading volume, volume ratio to recent history, 20-day realized volatility, price-to-moving-average ratio, market volatility, volume growth, and a spread proxy "when quote data are available" — transformed by lags, rolling moments, cross-sectional ranks and arithmetic combinations. Windows other than the 20-day realized vol (e.g., the "recent history" of the volume ratio, the MA length) are **not stated** → `underspecified`.
- **Normalization (source-reported, Eq. 3.3):** per-date cross-sectional winsorization at the 1st/99th percentile followed by a cross-sectional z-score; time-series operators applied strictly within asset history up to `t`.
- **Long entry / short entry:** decile sort on the composite score each day; long D10, short D1 (Appendix B.3, Exhibit 13). **Inconsistent alternative spec:** Exhibit 6 computes single-factor metrics on "long top 50 % / short bottom 50 %" while Exhibits 7/8/13/16 use deciles — portfolio definition is mixed across tables and never reconciled → `underspecified`.
- **Exit / holding period:** H = 1 day by default; robustness reported for H = 1…7 days (Exhibit 16). No stop, no take-profit, no re-entry rule → none specified by source.
- **Composite construction:** `S_i,t ≡ Ê[r_i,t+1 | x_i,t] = M(x_i,t; Θ)` (Eq. B.1). The **linear combination's coefficients are never given**; the LightGBM's depth/leaves/learning rate/λ/γ are described only as "tuned via time-series cross-validation" (Appendix C.4) with **no values** → `underspecified`.
- **The 12 factors:** names come from Exhibit 15 only (Composite Liquidity Demand; Defensive Mean-Reversion Signal; Delayed Flow Persistence; Flow Acceleration- Concave; Flow Shock - Winsorized; Lagged Flow Pressure; Medium-Horizon Attention; Persistent Turnover Intensity; Smoothed Flow Shock; Stable Turnover Trend; Sustained Liquidity Attention; Turnover Volatility Risk), each with a conceptual sentence and **no formula, window, or operator list**. §6.5.2 additionally uses a *different* name set for the same indices (see Negative evidence §3) → **factor identity mapping is ambiguous** → signal `underspecified`, not reproducible.
- **Selection gates:** promote if `t_IC ≥ τ_sig` and `SR_LS ≥ τ_econ`, retire if `t_IC < τ_fail` (Eq. 3.10); **numeric values of τ_sig, τ_econ, τ_fail are never disclosed** → `underspecified`. The |t| > 3.0 hurdle (§6.2) is source-reported but is stated for discovery claims, not as a numeric gate value.
- **Sizing / leverage / breadth:** decile legs are equal-weight means (Appendix B.3 `R_p,t+1 = Σ w_i,t r_i,t+1`, weights not further defined) → **no position-sizing, leverage, or capital-allocation rule exists in the source**; any implementable sizing is `research-proposed`.

## Required data

- **Instrument / universe:** US common stocks on NYSE/AMEX/NASDAQ, price ≥ USD 5, ≥ 252 observations, 8,052 stocks surviving screens (Exhibit 3); CRSP licensed data.
- **Venue / market type:** US equity exchanges, cash spot; long-short with unspecified borrow.
- **Timeframe / fields:** daily OHLC-equivalent close, share volume, market value-weighted return and S&P return (Exhibit 5 lists both), price, and a **turnover construct** — turnover's exact definition (volume/shares outstanding? float?) is **never stated** → `data gap`; a quote/spread proxy is "available" only conditionally.
- **Point-in-time:** standard daily availability assumed; no revisions handling discussed; discovery window 2004–2020, blind OOS 2021–2024 with the agent's state and library frozen (§6.4) — source-reported.
- **Missing data / survivorship:** only the ≥252-observation screen is stated; **delisting returns, suspensions, stale prices, halts, and the treatment of stocks that exit the universe during 2021–2024 are not stated** → `data gap` (Exhibit 4 shows universe counts decline but no attrition policy).
- **Costs/fees fields needed to reproduce the paper's "net":** only the flat 3 bps one-way assumption is provided; borrow/fee schedule, impact model, and fill model are absent (see Execution assumptions).

## Execution assumptions

- **Signal-to-order timing:** not stated (`data gap`). Whether the next-day return starts at t close or t+1 open is never pinned; with ~110 %/day turnover this single ambiguity can dominate net results.
- **Order type / fill model / latency:** not stated (`data gap`).
- **Fees / spread / slippage:** flat **3 bps one-way** covering commission and spread only (§7.2, Exhibit 13: `c_t = 0.0003 × Turnover_t`, `r_net = r_gross − c_t`). `slippage` and `bid-ask` as modelled inputs: 0 occurrences in the paper.
- **Borrow / shorting:** the strategy shorts the bottom decile of ~8,052 names, but **borrow cost, locate availability, hard-to-borrow screens, and recall risk are never mentioned** (`borrow` 0 occurrences) → `data gap`; source-reported "net" results must therefore be treated as **net of a commission/spread proxy only**, not fully net.
- **Impact / capacity / participation:** not stated; equal-weight deciles over a broad universe with no volume/participation cap → `data gap`.
- **Leverage / margin:** not stated → `data gap`.
- **Turnover (source-reported, Exhibit 18):** average daily one-way long-short turnover **105.73 % – 114.43 %** across the 16 OOS quarters — i.e. the book fully turns over more than once per day.
- **Partial fills / failures:** not discussed → `data gap`.
- Everything above is `source-reported` where a value exists and `data gap`/`research-proposed` where the source is silent; no cost or fill assumption in this record was invented to fill a source hole.

## Evidence

### Source-reported

All figures below are **third-party claims from the pinned v2 PDF (or the pinned homepage commit) and have not been reproduced**. Market/universe: **US equities**, OOS **2021-01 → 2024-12**, N = 1,004 trading days unless noted; **gross unless the row says net**.

- **Abstract (pinned PDF):** linear composite long-short delivers **annualized Sharpe 2.75 and return 54.81 %**. (The arXiv landing-page abstract for the *same* v2 instead states **Sharpe 3.11 / return 59.53 %** — see Negative evidence §1.)
- **Exhibit 9, Panel A** (linear composite long-short, OOS full window): cumulative **470.43 %**, annualized return **54.81 %**, annualized vol **16.40 %**, **Sharpe 2.75**, MaxDD **−13.41 %**, N = 1,004. Panel B: all 16 quarters gross-positive (min 2023Q1 1.37 %, max 2021Q4 24.00 %).
- **Exhibit 13, Panel A/B** (decile portfolios, composite score): D1 **−47.01 %** cumulative (Sharpe −0.505) → D10 **+245.72 %** (2.313); **gross** D10−D1 spread **465.07 %** cumulative, Sharpe **2.715**; **net** of 3 bps one-way **305.57 %** cumulative, Sharpe **2.211** (N = 1,004).
- **§7.2 / Exhibit 17 text:** "the strategy achieves a substantial cumulative return (**approximately 75 % net vs. 139 % gross**)" over January 2021 – December 2024 — flatly inconsistent with Exhibit 13 (see Negative evidence §2).
- **Exhibit 18** (quarterly cost/turnover diagnostics): avg daily turnover 105.73–114.43 %; **net returns positive in 14 of 16 quarters**; net-negative quarters **2022Q3 −0.4296 %** and **2023Q1 −0.7221 %**; net Sharpe range **−0.0752 (2023Q1) to 6.0322 (2021Q4)**.
- **Exhibit 6** (single-factor OOS metrics, top-50 %-vs-bottom-50 % portfolios): Factor 1 Sharpe 2.8593 / AnnRet 0.1754 / MaxDD −0.0488; Factor 3 Sharpe 2.4140 / AnnRet 0.2402; Factor 6 Sharpe 2.2597 / AnnRet 0.1543; Factor 8 Sharpe 1.6628 / IC 0.0271 / AnnRet 0.3928; Factor 9 Sharpe 1.9421 / AnnRet 0.1317; **Factor 2 Sharpe −0.1767 / AnnRet −0.0107**; Factor 11 Sharpe 0.6228; Factor 12 Sharpe 0.8362.
- **Exhibit 7** (decile High−Low spreads; caption says "decimal form" — units disputed below): Factor 8 **35.4202** (3.3190), Factor 3 21.9463 (4.8185), Factor 1 16.3258 (5.7073), Factor 6 14.5615 (4.5105), Factor 5 11.6424 (2.8083), Factor 9 12.5857 (3.8764), Factor 10 10.5051 (2.8791), Factor 4 8.1844 (1.3043), Factor 11 8.8706 (1.2432), Factor 12 5.4875 (1.6691), Factor 7 5.4160 (1.4335), **Factor 2 −0.9351 (−0.3526)**.
- **Exhibit 8** (risk-adjusted alphas of single factors; text calls them "annualized … in percentages"): Factor 8 FF6 α 0.318 (t 3.26), Factor 3 0.196 (4.37), Factor 1 0.138 (4.74), Factor 6 0.115 (3.65), Factor 9 0.100 (3.21), Factor 5 0.088 (2.23), Factor 10 0.078 (2.23); **insignificant**: Factor 4 0.057 (0.95), Factor 11 0.053 (0.80), Factor 12 0.022 (0.67), Factor 7 0.022 (0.59), **Factor 2 −0.040 (−1.43)**. Newey–West adjusted t-stats.
- **Exhibit 10** (composite alphas): linear long-short CAPM α 0.425 (t 5.334), FF3 0.417 (5.304), FF5 0.412 (5.315), FF6 0.414 (5.324); linear long-only 0.300 (4.338); LGBM long-short 0.311 (6.904); LGBM long-only 0.250 (3.441). **Unit labeling is internally inconsistent** (see Negative evidence §8).
- **Exhibit 16** (horizon decay, annualized, Newey–West t): Linear H1 **44.87 % (5.42)** → H7 **18.95 % (6.20)**; LGBM H1 **34.24 % (7.23)** → H7 **12.90 % (7.61)**; single-factor examples: Factor 8 H1 35.42 (3.32) → H7 17.05 (4.48); Factor 9 t rises 3.88 → 5.75 from H1 → H7; Factor 2 negative or null at every horizon.
- **Exhibit 19** (agentic vs "traditional" factor pipelines, OOS 2021–2024): agentic **linear 58.80 %** annualized vs traditional linear **30.91 %**; agentic **LightGBM 65.42 %** vs traditional LightGBM **50.84 %** (the 58.80 % disagrees with Exhibit 9's 54.81 % — see Negative evidence §2).
- **§6.2 / §6.4:** discovery hurdle **|t| > 3.0**; all discovery and agent learning finalized on data **prior to December 2020**; OOS agent state and factor library **frozen**; §6.3 states factors are "penalized for excessive turnover and rapid alpha decay" (penalty strength not quantified).
- **Project homepage, pinned commit `cc8bd7d` (`index.html`):** metric card "**Sharpe — Linear 3.82 / Tree 6.02**, Long-short gross, out-of-sample"; a second card "Alpha after factor controls" carries **no number**; `chart_data.json` at the same commit holds 502 plotted points spanning 2021-01-04 → 2024-12-27 with terminal cumulative values **l = +528.05 %, g = +603.60 %**.
- **Data availability / reproducibility claims (PDF):** "Data will be made available on request. Additional interactive results, methodological documentation, and replication details are available at the project homepage"; the homepage's "project documentation" link resolves to the 26-byte README stub; **no code, no formulas, no replication package are public**.

### Independently reproduced

**Not independently reproduced** for all strategy returns, alphas, ICs and Sharpes (CRSP is licensed and no code or factor formula exists in the paper or in the pinned repository).

Our own checks, performed 2026-09-24 and clearly labeled as **research-computed, not source-reported**:

1. Full read-through of the pinned v2 PDF text (117,662 chars) confirming every figure cited above traces to a named Exhibit/section, and confirming **the string `59.53` never appears in the PDF** and no Sharpe-3.11 claim exists there.
2. Landing-page abstracts re-fetched for both `/abs/2603.14288` and `/abs/2603.14288v1` → both report **Sharpe 3.11 / return 59.53 %**, contradicting the v2 PDF abstract (**2.75 / 54.81 %**).
3. `chart_data.json` fetched at pinned commit `cc8bd7d`; from that **sub-sampled (≈ every 2 trading days) published series we computed an approximate annualized Sharpe of ≈ 2.17 (field `l`) and ≈ 2.36 (field `g`)** using `mean/std × √(252/2)`. This reproduces **neither** the paper's 2.75/2.715 **nor** the homepage's 3.82/6.02. Caveat: approximation from a coarse published chart series, **not** a strategy reproduction.
4. Structural re-verification of the repository dedup (see Provenance) and of the canonical spec hash.

### Negative evidence

1. **Four mutually inconsistent headline results for the same strategy/window.** (a) arXiv landing abstract (v2 page **and** v1 page, both fetched 2026-09-24): Sharpe **3.11**, return **59.53 %**; (b) pinned v2 PDF abstract + Exhibit 9 + §8 conclusion: Sharpe **2.75**, annualized **54.81 %**, cumulative **470.43 %**; (c) §7.2 text for the same 2021–2024 window: ≈ **75 % net vs ≈ 139 % gross** cumulative; (d) project homepage pinned commit: gross Sharpe **3.82 / 6.02** with chart series ending **+528.05 % / +603.60 %**. Only one of these can be right; the source never reconciles them.
2. **Exhibit-level contradictions inside the PDF:** Exhibit 13 gross spread **465.07 % / Sharpe 2.715** vs Exhibit 9 **470.43 % / Sharpe 2.75** for what both describe as the same composite D10−D1 spread over the same 1,004 days; Exhibit 19 agentic linear **58.80 % annualized** vs Exhibit 9 **54.81 %**; §7.2's 139 %/75 % vs Exhibit 13's 465 %/306 %.
3. **Factor identity mapping conflicts.** §6.5.2 names Factor 1 "Flow Volatility Imbalance", Factor 2 "**Friction Adjusted Flow Shock**", Factor 7 "**Delayed Turnover Pressure**", Factor 8 "**Price Level Persistence**", Factor 10 "**Medium Horizon Turnover Pressure**"; Exhibit 15 names the same indices Factor 1 "Flow Shock - Winsorized", Factor 2 "**Lagged Flow Pressure**", Factor 7 "**Turnover Volatility Risk**", Factor 8 "**Defensive Mean-Reversion Signal**", Factor 10 "**Sustained Liquidity Attention**". Row-level results (Exhibits 6/7/8/16) therefore cannot be reliably attached to an economic narrative, and the §6.5.2 claim that Factor 2 "adjust[s] volume shocks for estimated trading costs" is unsupported by any published formula.
4. **The strategy is not reconstructable.** No factor formula, no linear-combination weights, no LightGBM hyperparameters, no numeric gate thresholds (τ_sig/τ_econ/τ_fail), no turnover definition; Exhibit 15's caption explicitly says descriptions are "conceptual and implementation-neutral". The public repository (pinned `cc8bd7d`) contains only `README.md` (26-byte stub), `index.html`, `chart_data.json`, `project-framework.png` — **zero code**, despite the homepage pointing readers to "project documentation" for "methodology and replication".
5. **Cost model is a single flat 3 bps one-way** with no borrow, no short-availability screen, no impact model, no latency, no capacity/participation constraints — while running **~106–114 % daily one-way turnover** on a short leg across ~8,000 names. Full-text counts: `borrow` 0, `bid-ask` 0, `slippage` 0, `hard-to-borrow` 0, `latency` 0, `capacity` 0 modelled. The paper's practical-implications bullet nonetheless claims performance "net of realistic transaction costs and turnover constraints".
6. **Execution timing unspecified** (no signal-to-fill convention, no order type, no fill model) — at >100 % daily turnover this omission alone can flip the net result.
7. **Under the paper's own |t| > 3.0 hurdle, most single factors fail OOS:** FF6/CAPM alpha t-stats are |t| ≤ 1.43 for Factors 2, 4, 7, 11, 12 (five of twelve), ≈2.2 for Factors 5 and 10; Factor 2's decile spread is **negative** OOS (−0.9351, t −0.3526) with Sharpe −0.1767 and AnnRet −0.0107. A promoted factor loses money OOS and most promoted factors clear no stated significance bar out of sample.
8. **Unit/attribution ambiguities that cannot be resolved from the source:** Exhibit 7's caption says "All returns are expressed in decimal form", yet its magnitudes (Low 7.6080 → High 23.9337 for Factor 1) are irreconcilable with Exhibit 6's decimal annual returns (0.1754); Exhibits 8/10 call α "annualized … in percentages" with values (0.425, 0.318, 0.138) that cannot be annualized percentages alongside a 54.81 % annualized strategy return — the alpha units are `underspecified`.
9. **An announced robustness check was never delivered:** §4.1 promises "we report the post-January 2023 period as a stricter subsample"; no such table, figure, or number appears anywhere in the 60-page PDF (verified by full-text scan) → unfulfilled claim / `data gap`.
10. **Minor-but-real internal inconsistencies:** title differs between arXiv metadata ("An Autonomous Framework for…") and PDF title page; Appendices D Exhibits 20/21 cover "Factor 1–Factor 11" while the library has 12 factors; single-factor metrics use top/bottom 50 % while all other tables use deciles; Exhibit 20/21 captions specify `log(1+CumRet)` axes that cannot be cross-checked without the underlying data.
11. **Selection-bias magnitude unknowable:** the paper acknowledges "thousands of implicit regressions performed during the discovery process" but never reports the number of candidates evaluated, gate pass-rate, or any deflated-Sharpe/number-of-trials correction (the multi-objective gate is described only qualitatively as "a functional heuristic for the Deflated Sharpe Ratio").
12. **Sample/regime concentration:** a single 4-year OOS path (2021–2024), discovery frozen at 2020 (no walk-forward re-discovery), equal-weight deciles that let microcaps dominate risk, no delisting/attrition policy stated, no cross-market or cross-regime replication, no independent replication by any third party.
13. **Source-quality context:** preprint only (no journal reference), practitioners-oriented social-media coverage thanked in the acknowledgements (QuantML / LLMQuant), 3 GitHub stars, and a project homepage whose only numeric Sharpe claim (3.82/6.02) matches neither the paper nor its own published chart series.

## Falsification plan

Thresholds below are `research-defined falsification thresholds` unless explicitly attributed to the source; all operational choices not given by the source are `research-proposed`.

- **F1 — Reconstruction gate (`research-proposed` implementation, `research-defined` threshold):** re-derive a 12-factor turnover/flow/price-anchor library from the ten published primitives and check whether *any* formula set reproduces Exhibit 6 single-factor Sharpes within ±0.3. **Failure:** no formula set reproduces them → treat the source strategy as non-reconstructable and keep the record research-only.
- **F2 — Internal-consistency gate (`research-defined`):** require the source (or an author clarification) to reconcile the four headline figures (3.11/59.53 %, 2.75/54.81 %, 75/139 %, 3.82/6.02 and +528/+604 %). **Failure:** unreconciled → all headline claims downgrade to unverified.
- **F3 — Cost stress (`research-defined`):** re-run the composite spread with κ ∈ {3, 5, 10} bps one-way **plus** an explicit borrow/funding charge on the short leg (`research-proposed`, source never modelled it). **Failure:** net annualized return ≤ 0 at κ = 5 bps, or net Sharpe < 0.5, on any tested market.
- **F4 — Factor-level ablation (`research-defined`):** drop the five OOS factors with |t| ≤ 1.43 and re-aggregate. **Failure:** composite annualized return falls below 50 % of the source-reported figure → reported alpha depends on alpha-free legs.
- **F5 — Out-of-sample extension (`research-defined`):** freeze the published factor family and evaluate 2025 onward (equities) or an equivalent untouched window. **Failure:** OOS Sharpe < 1.0 after κ = 5 bps costs.
- **F6 — Placebo / multiple-testing (`research-defined`):** 500 date- and label-shuffles of the factor matrix; **failure** if the true decile spread's t-statistic is not in the top 5 % of the null (p ≥ 0.05).
- **F7 — Baseline/controls:** require FF6 (equities) or market+size+momentum-style controls (crypto analog) to leave positive alpha with t ≥ 1.96 (`research-defined`); the source's own Exhibit 8/10 unit ambiguity must be resolved before any α is used.
- **F8 — Execution realism (`research-defined`):** model next-day-open execution, participation caps at a fixed % of ADV (`research-proposed`), and partial-fill/latency slippage; **failure** if headline Sharpe drops by more than half versus the paper's 3-bps-only net.
- **Action on failure:** record remains `research-only` / `not-implemented`; do not advance to the production candidate pool; a passing run must cite the exact table/figure reproduced.

## Crypto portability

**unproven.** The mechanism (broad-cross-sectional, daily-rebalanced, equal-weight, long-short decile spread on turnover/flow primitives) is demonstrated only in US equities with CRSP data and never in crypto.

- **Universe/breadth:** the equity edge depends on ranking thousands of names daily; the investable crypto cross-section with reliable borrow is far thinner and dominated by BTC/ETH.
- **Shorting:** equity shorting cost/borrow is unmodelled even in the source; crypto perp funding and borrow economics are structurally different, and the source provides zero evidence for them.
- **Session/time:** 24/7 sessions, no official close, different candle boundaries and timestamp conventions; the paper's daily "next-day return" and market-day rebalance have no direct crypto analogue.
- **Data quality:** exchange-fragmented volume, wash trading and manipulable turnover proxies directly attack a turnover-based signal family.
- **Venue/contract:** spot vs perpetual vs futures give different return streams; funding, mark/index price and liquidation are not covered by the source.
- Porting the *family-level hypothesis* (flow/attention-demand continuation) to crypto is a legitimate `research-proposed` experiment under F1–F8; it is **not** crypto empirical evidence and must not be labeled `direct`.

## Limitations

- `underspecified`: factor formulas, linear-combination weights, LightGBM hyperparameters, gate thresholds τ, turnover definition, volume-ratio/MA windows, execution timing and fill model, sizing/leverage, alpha units in Exhibits 8/10, Exhibit 7 return units.
- `not independently reproduced`: every source-reported return, Sharpe, IC and alpha (no code exists; CRSP licensed).
- `data gap`: borrow cost and short availability, market impact, capacity/participation, latency, delisting/survivorship/attrition policy, the promised post-Jan-2023 subsample, number of candidates tested / trials count, exchange-listing breakdown.
- `unproven`: crypto portability; cross-regime persistence beyond the single 2021–2024 OOS path; the "traditional AI" baseline comparison (baseline construction underspecified).
- Source-internal contradictions (Negative evidence §1–§3, §9) mean even the *claimed* performance level is uncertain; `confidence: low` therefore refers to our **research interpretation quality given a self-contradictory source**, not to a profitability judgment.

## Implementation status

`implementation_status: not-implemented`. Nothing from this record has been implemented in our research stack: no signal code, no backtest, no Qlib run, no Paper/Testnet/Live activity, no candidate-pool entry, no Wiki Brain record. The source's own implementation is equally unavailable (no public code at pinned commit `cc8bd7d`).

## Adoption boundary

Presence of this record in this repository means only that normalized research material was captured from a public source. It does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. This capture performed no downstream write of any kind.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` — canonical schema this record was validated against (sha256 `4561578a…ff6fcaa7`; no v2 exists).
- `[[quant/alphacfg-grammar-guided-mcts-tree-lstm-formulaic-alpha-2026-09-05]]` — adjacent automated formulaic-alpha discovery, different source and search method (grammar-guided MCTS vs ReAct/CoT agent).
- `[[quant/alphaschema-trading-semantic-plan-space-surrogate-guided-factor-mining-2026-09-05]]` — adjacent automated factor mining, different source and mechanism.
- `[[quant/alphalogics-market-logic-multi-agent-factor-generation-2026-09-05]]` — adjacent interpretable factor generation, different source.
- `[[quant/alphag-opd-reliability-gated-sibling-counterfactuals-symbolic-alpha-factor-discovery-2026-09-05]]` — adjacent symbolic alpha discovery with reliability gating, different source.
- `[[quant/vst-verifiable-structured-transport-agentic-alpha-discovery-2026-09-12]]` and `[[quant/agora-sealed-joint-search-emergent-alpha-scoring-2026-09-12]]` — adjacent agent-to-agent alpha discovery, different sources and mechanisms.
- Same-author but **different source identities** in this repository: `llm-augmented-semantic-network-cross-stock-reversal-2026-09-04.md` (`arXiv:2604.19476`) and `crypto-llm-agent-liquidity-scarcity-range-attention-factor-2026-09-01.md`; also adjacent `aeap-seads-llm-agentic-factor-discovery-formulaic-alpha-2026-09-03.md` and `factorengine-program-level-knowledge-infused-factor-mining-2026-09-05.md` (repository records, distinct sources/mechanisms).
- No existing record shares this record's canonical source identity (`arXiv:2603.14288` / `Beyond Prompting` / `allenh16/agentic-factor-investing`).

## Sources

1. Allen Yikuan Huang and Zheqi Fan, *"Beyond Prompting: An Autonomous Framework for Systematic Factor Investing via Agentic AI"*, `arXiv:2603.14288v2 [q-fin.PM]`, v1 submitted 15 Mar 2026, v2 revised 6 Apr 2026. Abstract: https://arxiv.org/abs/2603.14288 · PDF (pinned, SHA-256 `8fe2b21770af074a0e13667048bc40b3eb85fc03ecde8f5d58938e3aa100e301`, 60 pp., 5,047,216 bytes): https://arxiv.org/pdf/2603.14288 · v1 page (abstract cross-check): https://arxiv.org/abs/2603.14288v1 · DOI: https://doi.org/10.48550/arXiv.2603.14288. All performance figures in this record trace to named Exhibits 6–10, 13, 16–19 or §4.1/§6.2/§6.4/§7.2/§7.3 of that pinned PDF, or to the abstract-vs-PDF contradiction documented in Negative evidence §1.
2. `allenh16/agentic-factor-investing` GitHub repository at immutable commit `cc8bd7d06c26f39dc379157208482fe0da19623e` (files `README.md`, `chart_data.json`, `index.html`, `project-framework.png`): https://github.com/allenh16/agentic-factor-investing/tree/cc8bd7d06c26f39dc379157208482fe0da19623e · pinned `index.html` metric card ("Sharpe Linear 3.82 / Tree 6.02, Long-short gross, out-of-sample") and pinned `chart_data.json` (502 points, 2021-01-04 → 2024-12-27, terminal `l` = +528.05 %, `g` = +603.60 %), both fetched 2026-09-24 from that commit.
3. Project homepage cited by the paper: https://allenh16.github.io/agentic-factor-investing/ (fetched 2026-09-24; "project documentation" link resolves to the 26-byte README stub).
