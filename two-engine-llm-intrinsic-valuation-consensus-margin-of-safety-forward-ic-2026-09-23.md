---
schema: strategy-research-record-v1
title: "Two-Engine LLM Fundamental Valuation with Deterministic Value Compilation: Consensus Margin-of-Safety Cross-Sectional Signal and Forward-Only Evaluation (Alpha Research Paper 9, Vinebot/Buffybot)"
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - llm
  - fundamental-valuation
  - intrinsic-value
  - quality-gate
  - cross-sectional
  - us-equities
  - margin-of-safety
  - forward-only-evaluation
status: research-only
confidence: medium
source_as_of: 2026-06-24
sources:
  - "Bryan Vine, 'The Machine Analyst: Two LLM Fundamental-Valuation Bots, and the Problem of Proving Skill', Alpha Research Paper 9, byline June 24, 2026, https://bryanvine.github.io/alpha-research/paper9.html"
  - "https://github.com/bryanvine/alpha-research — file docs/paper9.html at full commit SHA 48f04c409c01157425ce458537a68a2c586fffaa (2026-06-24T00:41:35Z, commit message 'Paper 9: The Machine Analyst — two LLM fundamental-valuation bots'); byte-identical to repo head 17b8b5e1c79af194f733544517d82e3cf12c2259 (2026-08-23); SHA-256 f99fc6e2c52f0239c8df264720559f72b01907a353a0ab13088f2c8574617790, 31678 bytes (verified 2026-09-23)"
  - "https://github.com/bryanvine/alpha-research/blob/48f04c409c01157425ce458537a68a2c586fffaa/scripts/48_paper9_figures.py (figure script named for Paper 9; the valuation engines themselves are not present in the repository at this commit — see Provenance data gap)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Two-Engine LLM Fundamental Valuation with Deterministic Value Compilation: Consensus Margin-of-Safety Cross-Sectional Signal and Forward-Only Evaluation (Alpha Research Paper 9, Vinebot/Buffybot)

## Provenance

- **Source:** Bryan Vine, *"The Machine Analyst: Two LLM Fundamental-Valuation Bots, and the Problem of Proving Skill"* — Alpha Research, Paper 9 (the ninth paper of a personal research series).
- **Author list (complete, as printed on the source):** Bryan Vine (sole author; page byline `Bryan Vine · June 24, 2026`).
- **Published URL (stable):** https://bryanvine.github.io/alpha-research/paper9.html
- **Repository URL:** https://github.com/bryanvine/alpha-research
- **Immutable provenance:** file path `docs/paper9.html` at **full commit SHA `48f04c409c01157425ce458537a68a2c586fffaa`** (2026-06-24T00:41:35Z, commit message *"Paper 9: The Machine Analyst — two LLM fundamental-valuation bots"*) — the commit that introduced the paper (GitHub commits API, `path=docs/paper9.html`, single history entry).
- **Primary-source checksum (performed 2026-09-23):** three copies were fetched and hashed — (a) the live GitHub Pages file, (b) `docs/paper9.html` at creation commit `48f04c4…`, (c) `docs/paper9.html` at repository head `17b8b5e1c79af194f733544517d82e3cf12c2259` (head as of 2026-09-23, last commit 2026-08-23). All three are **byte-identical**: SHA-256 `f99fc6e2c52f0239c8df264720559f72b01907a353a0ab13088f2c8574617790`, **31,678 bytes**. The published page therefore equals the pinned artifact.
- **Sections read directly from that pinned HTML full text:** header/byline; Abstract; §1 Introduction; §2 *Two bots, one discipline* (§2.1 Vinebot, §2.2 Buffybot); §3 *What the bots see in mid-2026* (Figure 1, Figure 3); §4 *Triangulation* (Figure 2, **Table 1** — the fifteen two-method longs); §5 *The proving problem: why you can't backtest an LLM analyst*; §6 *Verdict*; §7 *Limitations & future work*; References.
- **Version/date:** single public version, byline **June 24, 2026**; no DOI, no revision history on the page → versioning beyond the commit chain is `not stated in source`.
- **Sample / data window as reported:** Vinebot **full-sweep dated 2026-06-23**, Buffybot scan **dated 2026-06-24** (§3); the forward scorecards are described as "**days old**" at writing (§5), i.e. this is a **single cross-sectional snapshot plus a just-started forward window**, not a historical sample. No multi-date valuation history is reported → historical performance sample `data gap`.
- **Universe as reported:** S&P 500 index constituents — **503 names** valued by Vinebot, **485 names** assigned a numeric value by both engines (§3, §4). Index-membership timing (point-in-time membership vs. current membership) `not stated in source`.
- **Transaction-cost treatment (read from §2–§7, not inferred):** full-text scan of the pinned HTML for `transaction cost`, `slippage`, `bid-ask`, `commission`, `borrow`, `fill model`, `market impact`, `latency` → **0 hits**; the single `spread` and `fee` hits are the substrings of "**spread**sheet" (§2.2) and "**fee**d" (§7) → **the source models no trading costs anywhere**. The only cost statements are (i) §7 *"the universe is large-cap and liquid, so capacity is not the binding constraint; the cost is compute — every valuation is tokens"* and (ii) §7 *"the bots must beat [a matched value/quality factor], net of turnover, to have earned the word alpha"* — a **requirement placed on future evidence, not a measured cost model**. Whether any future reported return would be gross or net is therefore `underspecified`.
- **Performance numbers:** every quantitative claim below was located in §3, §4 (**Table 1**), or §5 of the pinned HTML. The source reports **no return, Sharpe, IC, hit rate or drawdown figure** — §5 states *"the live history is days old, so every horizon is essentially unfilled. Any performance number quotable today is noise, and we quote none."* → performance is `data gap / not reported by source`.
- **Publication status:** self-published GitHub-Pages research-series page backed by an open-source repository; **no journal, no peer-review statement, no DOI** → peer-review status `not stated in source`. Source footer: *"Not investment advice."*
- **Supporting code at pinned head:** tree at `48f04c4…` has 126 paths; Paper-9-attributable files are `docs/paper9.html`, `scripts/48_paper9_figures.py`, `docs/figures/p9_fig2_crossbot.png`. **The valuation engines ("Vinebot", "Buffybot") are not present in the repository at this commit** — the source points to externally hosted live instances (`dbot.vineai.tech`, `buffy.bot`) → **engine source code provenance `data gap`**; the deterministic arithmetic is specified in §2 as formulas, not as auditable code in-repo.
- **Model provenance:** §2.1 names *"a frontier model (Claude sonnet for the batch, opus for the day's marquee name)"* — exact model versions, prompts, and the §7-acknowledged non-zero temperature value are `not stated in source`.
- **Repository-wide deduplication audit (2026-09-23, whole repository, not `git log`):** ripgrep across **all existing `*.md` records** (plus `coverage_manifest.csv`) for `paper9.html`, `48_paper9_figures`, `p9_fig2_crossbot`, exact title *"The Machine Analyst"*, `Vinebot`, `Buffybot`, `dbot.vineai.tech`, `buffy.bot`, `Damodaran bot`, `owner-earnings`, `intrinsic-value engine`, `bryanvine` → **zero records for this source identity.** `bryanvine` appears only in five records covering *different papers of the same series* with non-overlapping mechanisms: Paper 1 (volatility risk premium), Paper 2 (crypto funding carry), Paper 3 (crypto statistical arbitrage), Paper 6 (G10 FX carry / roll yield), Paper 8 (on-chain liquidity premia). Papers 4, 5, 7 and 9 of that series were all uncaptured at this run; the hard cap of 1 record/run selected this one. `margin of safety` matched only three incidental, non-valuation uses (vol-target buffer, execution-cost cushion wording). Materially distinct mechanism neighbors are listed under *Related Wiki records* — none shares dual-engine deterministic fundamental valuation.
- **Schema provenance:** structure and frontmatter follow the canonical Wiki Brain contract `quant/strategy-research-record-spec-v1` (`schema: strategy-research-record-v1`, re-read this run, sha256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`); README workflow contract re-read this run.
- **Discovery path:** source-series reconnaissance of an already-captured, high-quality research program (five of its papers are in this repository), reading the uncaptured papers' full text directly rather than any summary.

## Economic mechanism

### Source-reported

- The source's design thesis is **anti-degeneracy**: the flexible component (the LLM) is forbidden the conclusion. *"The language model never outputs a price target"* — it writes a narrative and sets a few assumptions, each **clamped to defensible bounds** (terminal growth `[-3%, r_f]`, beta `[0.5, 2.2]`, margins `[-10%, 70%]`), and **deterministic Python compiles them into value** (§1, §2.1).
- **Vinebot (price everything — Damodaran):** a story plus four value drivers (revenue growth, target operating margin, sales-to-capital reinvestment efficiency, and risk via beta and failure probability) feed a model router: operating firms → **FCFF DCF** (`V_0 = Σ FCFF_t/(1+WACC)^t + TV_H/(1+WACC)^H − net debt`); banks, insurers, lenders, capital-markets firms, regulated utilities and capital-intensive issuers → **residual income** (`V = B_0 + Σ (ROE_t − k_e)·B_{t-1}/(1+k_e)^t`, ROE fading to a durable premium); REITs → **FFO/AFFO**. Margin of safety `(V_0 − P)/P` maps to a STRONG BUY…STRONG SELL rating; coverage marches a sector-balanced batch per day plus a full-sweep job valuing all 503 constituents (§2.1).
- **Buffybot (price almost nothing — Graham–Dodd/Buffett):** a **deterministic quality gate** scores each company 0–100 purely from numbers — level and consistency of returns on capital (**30 + 22** points), margin stability (**16**), balance-sheet strength (**16**), cash conversion (**10**), share-count discipline (**6**) — with **hard disqualifiers** (negative equity, sub-hurdle returns, leverage above a ceiling, recurring losses) sending a name straight to "too hard". Only gate survivors enter the wonderful-business watchlist; the LLM then reads the quality dossier and sets **one number: a conservative normalized owner-earnings growth**; Python capitalizes owner earnings (`net income + D&A − maintenance capex`) at that growth, discounted at the **higher of CAPM cost of equity and a fixed opportunity-cost hurdle**, and flags a buy only at a real margin of safety (§2.2).
- The two engines *"reuses Vinebot's data layer, gateway, store, and serving"*, so the source frames any verdict difference as a controlled experiment in **method**, not plumbing (§2.2).
- **Reported cross-sectional read (mid-2026, §3):** Vinebot rates **57 of 503 (11.3%)** a buy and **367 (73.0%)** a sell; **15.1%** trade below the bot's DCF value; **mean margin of safety −0.36**. Buffybot finds **206 wonderful businesses (41% clear the gate)** but only **23 cheap (4.6% of the 503-name universe)**, with **123 of the 206** outright richly priced. Sector medians of Vinebot's margin of safety are **all negative** — least rich: telecom (≈0%), REITs (−4%), banks (−9%), insurers (−24%), payments and utilities (no figure printed → `data gap` for those two); most rich: semiconductors (−73%), broad technology (−57%), with capital markets, materials, aerospace and energy also named but unnumbered (`data gap`).
- **Triangulation claim (§4):** across the **485** jointly valued names the two margins of safety rank-correlate at **Spearman ρ = 0.71** and agree on cheap-versus-rich **84.5%** of the time (**355 both-rich, 55 both-cheap, 75 disagreements**; the Abstract rounds the agreement to "85%"), yielding **15 two-method longs** (Table 1: PYPL, UHS, IT, CMCSA, ACN, CTSH, GDDY, LULU, SOLV, BR, CF, ADBE, INTU, ACGL, DECK with per-engine margin of safety and Buffybot quality score).
- **The source's own honest null (§4, §7):** *"Agreement is not correctness."* Both engines share yfinance fundamentals, a discounted-cash-flow worldview, and *"the same instinct to penalize a high multiple"*; ρ = 0.71 is *"consistent with both engines being two implementations of the same value factor"*, and Figure 3's value/quality sector tilt *"all but says so"*.
- **Evaluation thesis (§5):** an LLM analyst **cannot be backtested** — a model asked to value a company "as of 2019" already knows the outcome from training data, the contamination is unauditable, and *"a historical replay of an LLM analyst measures memory, not foresight"*. The only valid test is forward: every rating is a tracked **call that opens when the rating bucket changes and stays open until it changes again**, scored on dividend-adjusted return from entry over **7/30/90-day** horizons and since-open, **benchmarked against SPY and direction-adjusted so a correct SELL counts as a win**.

### Research interpretation

Falsifiable hypothesis: a **two-method consensus margin-of-safety rank** — the intersection (or joint rank) of an independent DCF engine and a quality-gated owner-earnings engine over the same point-in-time fundamentals — carries **incremental cross-sectional information about subsequent large-cap equity returns beyond a matched value/quality factor**. Component roles:

```text
Signal: cross-sectional consensus margin of safety
        (source's own watchlist = the 15-name both-cheap intersection, Table 1)
Formation: daily valuation sweep (sector-balanced batch + full sweep); rating bucket change opens/closes a tracked call
Universe: S&P 500 constituents (503 names), US large-cap equities
Portfolio layer: NOT specified by source — long-short/weights/rebalance are research-proposed
Regime filter: none in source
Risk / exit: rating-bucket change closes the call (source); stop/target rules absent → research-proposed if ever operationalized
```

Mechanism class: **cross-sectional underreaction to slow-moving fundamental information**, with the LLM acting as a cheap, disciplined aggregator and deterministic arithmetic preventing hallucinated conclusions. It is *not* a text-sentiment signal and *not* a persona/mention-frequency signal (see Related records). Competing explanations to be tested rather than assumed: (i) the consensus rank is simply **value/quality beta** (the source's stated honest null); (ii) shared-input bias — one fundamentals feed feeds both engines; (iii) threshold artifacts — in Table 1 the Buffybot margin of safety sits at **+0.28…+0.31 for 13 of the 15 names** (only CMCSA +0.78 and ACGL +0.45 differ), which looks threshold-like rather than graded (Scout observation from Table 1, `research-proposed` reading, not a source claim); (iv) index-selection and multiple-comparisons luck at ~500 names re-rated daily.

## Signal

- **Formation timestamp:** engines run on a daily cadence — Vinebot "a sector-balanced batch a day" plus a full-sweep job; the pinned snapshot is **2026-06-23 (Vinebot)** and **2026-06-24 (Buffybot)** (§2.1, §3). Time-of-day, timezone, and publication/availability convention `not stated in source` → **data gap**. Point-in-time: fundamentals come from a **free feed (yfinance / EDGAR)**; §7 flags restatements, mis-mapped sectors and stale TTM figures, with **no revision or lag handling stated** → `data gap`.
- **Long entry:** Vinebot flags a buy when `(V_0 − P)/P` maps into the buy bucket of a STRONG BUY…STRONG SELL scale; Buffybot flags a buy only after the deterministic quality gate passes **and** the owner-earnings margin of safety clears the higher-of-(CAPM, fixed hurdle) discount rate. **Exact rating-bucket cut-offs for both engines are not printed in the source** → `underspecified` (a positive-margin-of-safety reading is the only visible rule).
- **Short entry:** ratings include SELL, but the source defines **no short execution rule**; the "long-short portfolio implied by the ratings" appears only as an *evaluation* object in §5's power analysis → trading-side shorting `underspecified` / not a source rule.
- **Exit / holding:** a call **stays open until the rating bucket changes** (§5). The **7/30/90-day and since-open windows are measurement horizons, not holding rules** → tradable holding period `underspecified`.
- **Re-entry:** not stated (`data gap`); implied by re-rating but never specified.
- **Parameters (all fixed by source, none reported as tuned):** value-driver clamps `terminal growth ∈ [−3%, r_f]`, `beta ∈ [0.5, 2.2]`, `margin ∈ [−10%, 70%]`; model routing by sector/business type; quality-gate weights 30/22/16/16/10/6 with four hard disqualifiers; discount = WACC (Vinebot) and `max(CAPM cost of equity, fixed opportunity-cost hurdle)` (Buffybot); LLM outputs exactly one owner-earnings growth number (Buffybot).
- **Consensus layer:** the 15-name intersection (Table 1) is a **source-reported watchlist**, not a tested portfolio. Turning it into positions, weights, or a continuous dual-rank portfolio is **research-proposed**.
- **Reproducibility verdict:** engine *formulas and clamps* are specified enough to reimplement; rating thresholds, timezone, consensus portfolio construction, and the engine code itself are not → the signal as a whole is **partially specified (reimplementable-with-gaps), not fully reproducible**.

## Required data

- **Instrument / universe:** S&P 500 constituents (503 names), US large-cap common stocks, USD; **point-in-time index membership and rebalance timing not stated** → survivorship/membership `data gap`.
- **Fields:** per-name fundamentals from yfinance/EDGAR (revenue, margins, sales-to-capital inputs, beta, failure probability, ROE/book equity, share count, net income, D&A, maintenance capex, net debt, leverage, equity sign), sector classification, plus the LLM-generated narrative and drivers (stored by the source's own gateway/store, code not public at pinned commit).
- **Reference prices / benchmark:** company price `P` for margin of safety; **dividend-adjusted price series and SPY** for forward scoring (§5).
- **Timeframe:** daily valuation sweeps; forward scoring at 7/30/90 days and since-open; live scorecards update daily.
- **Point-in-time / availability:** free feed TTM fundamentals with acknowledged restatement/staleness issues (§7); no publication-lag model → `data gap`.
- **Missing-data:** handling of stale/missing fundamentals `not stated in source`.
- **Funding / fee / spread / borrow fields:** none required or provided by the source — no cost input exists anywhere in the paper (see Provenance cost scan).
- **Crypto port note:** no on-chain, funding, mark/index, open-interest or options-surface fields apply — the data contract is equity-fundamentals-native.

## Execution assumptions

- **Order type, fill model, signal-to-order delay, next-bar/same-bar, latency, partial fills, leverage/margin, borrow availability, fees, spread, slippage, impact:** **none stated in source** (0 real hits for the cost lexicon in the pinned full text) → every one of these fields is `not stated in source`.
- **Capacity:** source states large-cap and liquid ⇒ capacity not binding; the binding cost it acknowledges is **compute (tokens per valuation)**, with *"alpha per dollar of inference"* declared a real but **unbooked** metric (§7) → cost-of-carry for the signal is compute, not market friction; no number given → `data gap`.
- **Turnover:** the only reference is §7's burden that any edge must beat a matched value/quality factor **"net of turnover"** — required, never measured → `underspecified`.
- **Nondeterminism as an execution risk:** the LLM runs at non-zero temperature, so *"day-to-day rating churn is real and must be measured, not assumed away"* (§7) → bucket-flip frequency is a material, unquantified turnover driver (`data gap`).
- **Anything a researcher would add to trade this** (sizing, weighting, rebalance cadence, borrow, stop rules, order handling) is **research-proposed**, not source-reported.

## Evidence

### Source-reported

All figures below are `source-reported`, traced to the pinned `docs/paper9.html` (`48f04c4…`) sections noted:

- **§3 cross-sectional breadth:** Vinebot 57/503 (11.3%) buy, 367 (73.0%) sell, 15.1% below DCF value, mean margin of safety −0.36; Buffybot 206/503 (41%) pass the quality gate, 23 (4.6%) cheap, 123/206 richly priced; sector medians all negative (telecom ≈0%, REITs −4%, banks −9%, insurers −24%, semiconductors −73%, broad technology −57%).
- **§4 triangulation (Table 1):** 485 jointly valued names, **Spearman ρ = 0.71**, cheap/rich agreement **84.5%** (355 both-rich / 55 both-cheap / 75 disagreements; Abstract rounds to 85%), **15** two-method longs with per-engine margin of safety and quality scores (Table 1 row identities: PYPL +1.65/+0.29/Q85; UHS +1.63/+0.29/Q69; IT +1.18/+0.30/Q94; CMCSA +0.86/+0.78/Q70; ACN +0.73/+0.30/Q89; CTSH +0.61/+0.31/Q81; GDDY +0.59/+0.30/Q82; LULU +0.57/+0.30/Q95; SOLV +0.50/+0.31/Q73; BR +0.44/+0.29/Q75; CF +0.38/+0.30/Q85; ADBE +0.32/+0.28/Q96; INTU +0.31/+0.29/Q79; ACGL +0.31/+0.45/Q85; DECK +0.26/+0.28/Q97).
- **§5 statistical-power argument:** to reject `Sharpe = 0` at `t ≈ 2` needs `T ≈ (2/S)²` years — **~44 years for S = 0.3, ~16 years for S = 0.5** (standalone); breadth via the fundamental law `IR ≈ IC·√N` over ~500 names makes the **cumulative cross-sectional IC of margin of safety vs. forward return** the earliest usable read; a **multi-year forward verdict**, "quite possibly never if there is no edge".
- **§5 performance:** *none* — live history days old, *"we quote none"*. No return, Sharpe, IC, hit rate or drawdown exists in the source → `data gap`.
- **§1 framing of the program:** the series' prior papers are summarized by the source as directional prediction failing and provision-type premia being modest (~0.4 Sharpe) and decaying — these are the source's own recaps of its other papers, **not evidence for this record's signal**.

### Independently reproduced

`Not independently reproduced.` The only verification performed is provenance-level: the pinned commit, repository head, and published page were shown byte-identical (SHA-256 `f99fc6e2…7790`, 31,678 bytes), and Table 1 / §3 / §4 / §5 figures were read from that pinned artifact. The valuation engines are **not in the repository** at the pinned commit, so no independent rerun of the 503-name sweep was possible; no forward scorecard has been observed by this Scout; nothing was run in Qlib, NautilusTrader or any internal stack.

### Negative evidence

- **Source's own (§4, §7):** agreement ≠ correctness — ρ = 0.71 is *"consistent with both engines being two implementations of the same value factor"*, sharing one fundamentals feed, one DCF worldview, and one high-multiple penalty; Figure 3 shows an **implicit value/quality tilt** (every sector median margin of safety is negative, ordered as a textbook value tilt), so the honest null is a **matched value/quality factor, not SPY**, and any edge must survive **net of turnover** — untested.
- **Structural negative evidence (§5):** the standard verification tool of this repository's entire workflow — the historical backtest — is **invalid by construction for an LLM analyst** (training-cutoff hindsight, unauditable, "no window left to widen"); the only uncontaminated data "does not yet exist". This is a hard, pre-declared limit on confirmability, not a stylistic caveat.
- **Power negative evidence (§5):** at plausible standalone Sharpes the required sample is 16–44 years; even with breadth the verdict is multi-year, and **the live sample at publication was days old** — i.e. zero completed evidence at capture time.
- **Selection / multiplicity (§7):** ~500 names re-rated daily is *"a multiple-comparisons machine"*; some calls will look brilliant by luck, so only the cross-sectional IC (not hand-picked winners) is admissible.
- **Data-quality negative evidence (§7):** free-feed fundamentals (restatements, mis-mapped sectors, stale TTM) inject noise the narrative can hide.
- **Nondeterminism (§7):** non-zero temperature ⇒ real day-to-day rating churn; consensus membership stability is unmeasured.
- **Cost/turnover negative evidence:** no cost model exists in the source at all (0 real cost-term hits) — so no claim about net-of-cost viability can be made in either direction.
- **None of the repo's adjacent LLM-signal records corroborate this mechanism** — they are different sources with different constructions (see Related); no independent corroboration was identified. Absence of corroboration is not evidence of no effect.

## Falsification plan

Every threshold below is **`research-defined falsification threshold`** or **`research-proposed`** unless explicitly attributed to the source.

1. **Forward pre-registered IC (source's own design, thresholds research-defined):** freeze both engines' rules and clamps, then accumulate daily dual-engine margin-of-safety ranks vs. 7/30/90-day forward returns. *Reject the predictability claim if the cumulative cross-sectional IC is ≤ 0 or its t-statistic < 2.0 after a pre-declared ≥ 24-month window* (window length and cutoffs chosen by Scout, `research-defined`), with no post-hoc re-clamping.
2. **Matched value/quality control (source's own honest null, §7):** the long-short implied by the consensus rank must add return beyond a matched value/quality factor (e.g. value + profitability/quality combination) after fees. *Reject "alpha" if the incremental alpha is statistically indistinguishable from zero at the 5% level* (`research-defined`) — this is the test the source itself says separates a value tilt from an edge.
3. **Two-method ablation (research-proposed):** Vinebot-only vs. Buffybot-only vs. consensus intersection on the same dates. *Reject the triangulation thesis if the consensus does not improve out-of-sample IC or Information Ratio over the better single engine* (`research-defined`: no improvement over ≥ 24 months).
4. **Contamination probe (source's own future work, §7):** re-value a fixed panel with company identities masked (industry descriptors only). *If the cheapness ranking under masked identity correlates ρ ≥ 0.9 with the unmasked ranking, the engine is reading a generic value template rather than company-specific information* (`research-defined` cutoff, Scout-set).
5. **Nondeterminism / churn stress (research-proposed):** re-run each valuation K = 5 times on the same date and report bucket-flip rate and consensus-set Jaccard overlap. *Reject tradability of the consensus list if mean Jaccard overlap across reruns < 0.8* (`research-defined`).
6. **Turnover and cost ladder (research-proposed):** measure realized turnover of the rating-driven portfolio and charge 5/10/20 bps per unit turnover. *Reject if net-of-20bps Sharpe ≤ 0* (`research-defined`) — the cost ladder exists because the source prices no costs at all.
7. **Membership and data robustness (research-proposed):** repeat under point-in-time index membership and a second fundamentals vendor; *reject if sign of the forward IC flips* (`research-defined`).
8. **No rescue by retuning (source's spirit, Scout-formalized):** clamps, gate weights and model routing are frozen at their published values; a failure under tests 1–6 ends the hypothesis rather than licensing a new parameter search.

## Crypto portability

**`unproven`** — and weakly so.

- The source demonstrates the mechanism **only on US large-cap equities**; it never mentions crypto. Per contract this cannot be labeled `direct`.
- The mechanism requires **discountable cash flows** (FCFF, residual income on book equity, owner earnings = net income + D&A − maintenance capex) and a **quality accounting record** (returns on capital, margin stability, leverage). Most crypto assets have neither corporate cash flows nor standardized accounting, so a literal port is **undefined**, not merely untested; a protocol-revenue/FDV-based analogue would be a **different mechanism** and must be captured as a new hypothesis (`research-proposed`).
- Crypto-specific gaps that would dominate any port: no index-membership governance or audited TTM fundamentals, no common accounting standard (restatement/wash-reward risk), 24/7 repricing vs. daily valuation cadence, free-feed quality far below EDGAR, and venue/quote-currency fragmentation.
- Portability is not authorization to trade; equity applicability itself remains unproven (see Falsification plan).

## Limitations

- **Performance is entirely absent:** the source reports zero returns/Sharpe/IC — this record contains **no evidence the signal makes money**, only evidence about a valuation apparatus' internal agreement (`data gap`, `not independently reproduced`).
- **Single-date cross-section:** n = one snapshot (2026-06-23/24) for every cross-sectional number; no time-series sample exists yet (`data gap`).
- **No peer review, self-published** personal research series; no DOI (`not stated in source`).
- **Engine code absent from the repository** at the pinned commit (only the figure script) → the deterministic compilation cannot be audited as code, only as printed formulas (`data gap`).
- **Underspecified operational fields:** rating-bucket thresholds, timezone/day-boundary, exact model versions and temperature, re-entry, portfolio construction, and every cost/fill/borrow field.
- **Verification impossibility is structural:** historical replay of an LLM analyst is contaminated by training cutoff by the source's own argument (§5) — so the usual repo-style backtest check cannot be run for this family, and any future claim must come from a forward window this Scout has not observed.
- **Confounded by construction risk:** shared fundamentals feed + shared DCF worldview make a shared value/quality load the default explanation (§4).
- **Source-reported breadth figures (57/503 etc.) are a point-in-time market read, not a strategy result** and must not be read as predictive accuracy.
- `unproven` for any profitability claim; `research-proposed` wherever an operational rule was needed and the source stayed silent.

## Implementation status

`implementation_status: not-implemented`. **Nothing has been implemented in our research stack**: no engine was rebuilt, no consensus list was ingested, no backtest, walk-forward, Qlib run, paper trading, testnet or live run occurred. The source itself has only just started its forward clock and reports no completed performance window. This record is documentation of a source, not a working artifact.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. No wording, evidence count, or series reputation in this record promotes it.

## Related Wiki records

Same-series records already in this repository (different papers, non-overlapping mechanisms — none is this source identity):

- `crypto-volatility-risk-premium-variance-swap-estimator-fragility-decay-2026-09-12` (Paper 1: options variance risk premium)
- `crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11` (Paper 2: perpetual funding carry)
- `crypto-statistical-arbitrage-pca-residual-cointegration-falsification-2026-09-12` (Paper 3: crypto stat-arb)
- `g10-fx-carry-fx-value-energy-roll-yield-net-cost-audit-2026-09-23` (Paper 6: FX carry / roll yield — its §5 prose *mentions* Papers 4 and 5 as program summaries, but neither is captured as its own record)
- `autonomous-llm-research-stablecoin-flow-carry-trend-death-2026-09-19` (Paper 8: autonomous strategy search)

Mechanism neighbors (different sources and different signal constructions — why this record is independent):

- `frozen-llm-checkpoint-outlook-score-cross-sectional-us-equity-arxiv-2604.21433-2026-09-22` — a frozen-checkpoint **text outlook score** is backtested; here the LLM is explicitly *forbidden* the output and only sets clamped assumptions, and the source argues backtesting is invalid for this family.
- `llm-persona-consensus-mention-frequency-top50-us-equity-six-factor-2026-09-22` — persona **mention-frequency** consensus (media prominence), not fundamental valuation.
- `small-cap-alpha-beta-separation-uncertainty-aware-llm-portfolio-2026-09-02`, `llm-news-enhanced-cross-sectional-momentum-tilt-2026-09-06`, `llm-strategy-discovery-leakage-safe-search-deflated-eval-2026-09-04` — LLM text/aggregation mechanisms, different sources and universes.
- `crypto-cross-sectional-factor-zoo-iterative-alpha-compression-2026-09-01` — factor-zoo compression in crypto (relevant to the "same value factor" confound, different source).
- `look-ahead-bias-pretrained-financial-forecasting-pit-vintage-arxiv-2609.20554-2026-09-19` — cross-cutting methodological record on training-cutoff look-ahead; this record's source is the mechanism-level instance of that failure mode inside a valuation workflow.

`[[quant/strategy-research-record-spec-v1]]` — authoritative schema specification (read this run). No stable Hermes Wiki Brain page is known for the records above beyond it, so no further Wiki links are asserted.

## Sources

1. Bryan Vine. *"The Machine Analyst: Two LLM Fundamental-Valuation Bots, and the Problem of Proving Skill."* Alpha Research, Paper 9, byline **June 24, 2026**. https://bryanvine.github.io/alpha-research/paper9.html — read in full (Abstract, §1–§7, Table 1, References) on 2026-09-23. Every quantitative claim in this record traces to §2, §3, §4/Table 1, §5 or §7 of that pinned page.
2. Bryan Vine. `alpha-research` repository. https://github.com/bryanvine/alpha-research — file `docs/paper9.html` at full commit `48f04c409c01157425ce458537a68a2c586fffaa` (2026-06-24T00:41:35Z, *"Paper 9: The Machine Analyst — two LLM fundamental-valuation bots"*) and at head `17b8b5e1c79af194f733544517d82e3cf12c2259` (2026-08-23); both byte-identical to the published page (SHA-256 `f99fc6e2c52f0239c8df264720559f72b01907a353a0ab13088f2c8574617790`, 31,678 bytes, verified 2026-09-23). Related paths at that commit: `scripts/48_paper9_figures.py`, `docs/figures/p9_fig2_crossbot.png`. Live instances named by the source: `dbot.vineai.tech` (Vinebot), `buffy.bot` (Buffybot) — **not opened in this run**.
3. Third-party works **cited by** source 2 (listed for provenance only; **not opened, no claim taken from them**): Damodaran (2017) *Narrative and Numbers* / *Investment Valuation* 3rd ed.; Graham & Dodd (1934) *Security Analysis*; Buffett (1986) "Owner Earnings" appendix; Ohlson (1995) *Contemporary Accounting Research*; Grinold (1989) *Journal of Portfolio Management* (and Grinold & Kahn, *Active Portfolio Management* 2nd ed.); Bailey & López de Prado (2014) "The Deflated Sharpe Ratio", *JPM* 40(5); Dhar (2026) "The Damodaran Bot", vasantdhar.substack.com; Vine (2026) Alpha Research Papers 1–8.
