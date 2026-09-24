---
schema: strategy-research-record-v1
title: GPT Zero-Shot Generated Formulaic Factors for the Chinese Futures Cross-Section (Cheng, Zhou & Liu)
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: low
source_as_of: 2025-09-28
sources:
  - https://arxiv.org/abs/2509.23609
  - https://arxiv.org/html/2509.23609v1
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# GPT Zero-Shot Generated Formulaic Factors for the Chinese Futures Cross-Section (Cheng, Zhou & Liu)

## Provenance

**Primary source (identity):** Yuhan Cheng, Heyang Zhou, Yanchu Liu, *"Large Language Models and Futures Price Factors in China."* arXiv `2509.23609`, DataCite DOI `10.48550/arXiv.2509.23609`. Landing page `https://arxiv.org/abs/2509.23609` and full HTML `https://arxiv.org/html/2509.23609v1` both read directly on 2026-09-24.

- **Authors (exact arXiv byline, 3 names):** Yuhan Cheng; Heyang Zhou; Yanchu Liu. **No affiliations, emails, or funding statements are printed anywhere on the landing page or in the v1 full text** → affiliation `data gap`.
- **Version/date:** **v1 only** — *Sun, 28 Sep 2025 03:24:10 UTC (164 KB)*; landing comments field `46 pages; 1 figure`; **no journal-ref, no external journal DOI, no MSC/other DOI** → **preprint only, not peer reviewed** (publication status verified on the landing page 2026-09-24). Primary categories printed on the landing page: Pricing of Securities (`q-fin.PR`); Machine Learning (`cs.LG`).
- **Sample period (source-reported, with an internal contradiction):** §4 *"Factors and Data"* states daily data **2010/01/04 → 2023/04/07**, signal/history data *"up to 2017/12/29"*, in-sample backtest **2018/01/02 → 2023/04/07**; §5.2 defines **"Out-of-Sample" = 2023/05/04 → 2024/10/31** (chosen as the period after GPT's stated April-2023 training cutoff). The OOS window **ends 2024/10/31, i.e. more than 18 months past the stated data end of 2023/04/07** → recorded as a source contradiction, not silently repaired. Table 2/3 notes additionally say *"historical data from 2010 to 2021 used for reference"*, conflicting with §4's 2017/12/29 cut → second contradiction.
- **Universe (source-reported):** **104 leading and secondary continuous contracts** — *"all stock index futures and liquid commodity futures in China"* — daily market data from the **Wind financial database**; fields `futuresname, date, basis, spot price, futures premium and discount, open, high, low, close, volume, amount, return`. §4 notes *"some futures data do not span the entire period"*, with contract codes/listing dates in Online Appendix Table A1; inclusion/liquidity/listing-date rules are not otherwise stated → `data gap`.
- **Transaction cost treatment (read from Methods §3.2 + results §5.1, not from the abstract):** exactly one cost number appears in v1 — **"transaction fees (i.e., 0.025%)"** (§5.1), used to produce the starred (`*`) columns of Tables 2/3/5/7/8/10. **The fee basis (per side vs round trip, applied to what base — traded notional, turnover, or equity) is never stated** → `underspecified`. **Spread, slippage, market impact, bid-ask, latency, margin/financing, borrow/short availability, daily price-limit (limit-up/limit-down) non-fill days, and continuous-contract roll cost are not stated anywhere in v1** (verified by full-text search) → `data gap`, explicitly **not** inferred as zero-cost. The paper's claim that *"the impact of transaction costs remains negligible"* (§5.2) is a source-reported assertion.
- **Core performance numbers:** all anchored to specific tables below (Tables 1–11 plus Online Appendix Tables A1–C5), gross and `*`-fee-adjusted pairs as printed. Sharpe ratio **definition (risk-free rate, annualization factor) is never stated** → Sharpe scale `underspecified`.
- **Publication/preprint status:** preprint only (see version row). **No code, model, or data availability statement exists in v1** (full-text search for `github` / `code is available` / `data are available` / `repository` returns only arXiv page chrome); factor formulas are given only as **natural-language construction notes in Online Appendix B**. Reproduction requires the commercial Wind database → **not independently reproducible as published**.

**Repository-wide source-identity dedup (2026-09-24, ripgrep `--hidden` over ALL tracked `*.md` including `.mimo-worktrees` plus `coverage_manifest.csv`):** `2509.23609`, `10.48550/arXiv.2509.23609`, exact title *"Large Language Models and Futures Price Factors in China"*, `Heyang Zhou`, `Yanchu Liu`, `GPT-generated factor`, `Cheng and Tang`, `AlphaEvolve`, `zero-shot.*factor` → **zero source-identity hits**. The pattern `Yuhan Cheng` produced 4 matches, all inside the single unrelated record `crypto-perpetual-futures-170-predictor-zoo-log-basis-price-volume-two-factor-spanning-2026-09-23.md` (SSRN `abstract_id=6795783`, *Cao/Luo/Cheng/Dong*, "Anatomy of Cryptocurrency Perpetual Futures Returns") — a **different paper, different DOI, different author list order and mechanism**; not this source identity. `IPCA` hits 6 existing records (all different sources: Kelly-IPCA used as benchmark in equity/crypto captures) and `Chinese futures` hits 1 record (`path-signature-decomposition-segmented-levy-area-futures-pair-trading-2026-09-03.md`, a Levy-area pair-trading mechanism) — neither shares source identity or normalized rule.

**Material distinction vs the existing LLM/alpha-factor family** (dedup contract axes, stated explicitly because the family is well populated): *source identity* is different for every record below; *mechanism* differs — this record is **zero-shot formula generation with no data exposure, no RL/search loop, and no agent scaffold** (a single frozen GPT-4 dialogue producing Python formulas over column semantics) versus multi-agent/generative pipelines (`alphalogics-market-logic-multi-agent-factor-generation-2026-09-05`, `alphaschema-trading-semantic-plan-space-surrogate-guided-factor-mining-2026-09-05`, `alphacfg-grammar-guided-mcts-tree-lstm-formulaic-alpha-2026-09-05`, `alphar1-context-aware-alpha-screening-llm-reasoning-grpo-2026-09-03`, `factorengine-program-level-knowledge-infused-factor-mining-2026-09-05`, `favor-hypothesis-grounded-agentic-factor-validation-topk-portfolio-2026-09-24`, `beyond-prompting-agentic-factor-investing-composite-long-short-2026-09-24`, `llm-strategy-discovery-leakage-safe-search-deflated-eval-2026-09-04`); *universe* differs — **Chinese stock-index and commodity futures daily cross-section** versus equity cross-sections and crypto; *signal construction* differs — **daily top/bottom-decile futures ranking on basis/premium-discount/OHLC/volume formulas** versus equity characteristic sorting or hypothesis-testing agents; *data dependency* differs — **zero-shot (the LLM never sees return data) with a training-cutoff-defined OOS window** versus trained/feedback-driven discovery.

## Economic mechanism

### Source-reported

The authors position GPT-4 as an *"artificial financial analyst"* that, **without ever seeing actual market data** (zero-shot; only the data-schema/column names are disclosed in the prompt), writes Python that constructs a new factor column from at least two of `{basis, spot, futures premium/discount, open, high, low, close, volume, amount}`. The stated rationale is that the LLM's pretraining embeds financial-theory priors (momentum, liquidity, basis/term-structure sentiment, volatility composites) and that China's under-researched futures market benefits from cheap, fast, data-free factor ideation (§1, §3.1). Claimed channels for the surviving factors include basis-vs-spot expectation signals, momentum–liquidity composites, and premium/discount sentiment (§6.3). A *"manual review"* enforces novelty, a *"forward-looking bias check"* removes look-ahead code, and factors producing *"sparse or aberrant outputs"* (division by zero, infinite loops, memory overflow) are excluded (§3.1). The paper claims GPT-generated factors deliver *"substantial annualized returns and impressive Sharpe ratios, outperforming traditional IPCA models"* (§8) and that performance is *"not contingent upon the model's pre-trained knowledge"* because evaluation windows postdate the April-2023 training cutoff (§5.2).

### Research interpretation

Falsifiable hypothesis: **a frozen LLM's prior over financial-variable constructions is a usable factor-specification prior — formulas sampled from that prior, selected without seeing returns, produce cross-sectional daily long-short risk-adjusted returns in Chinese futures that survive realistic costs and exceed both simple commodity/futures baselines (carry, momentum, seasonality) and a selection-luck null.** Component roles: *signal* = one GPT-written formulaic score per factor (40 retained); *portfolio* = daily cross-sectional top/bottom-decile sorts (no regime layer, no confirmation filter, no stop — this is a pure cross-sectional ranking strategy); *benchmark* = IPCA-5 (Kelly, 2017) with instruments aligned to the GPT-visible features. The economically decisive question is **not** whether any single formula backtests well — with ~40 retained formulas plus ≥80 robustness variants and four portfolio constructions, large maxima are expected under the null — but whether the *library as a whole*, with selection accounted for, beats a search-aware null. Alternative explanations that must be excluded before accepting the mechanism: (i) selection luck / multiple testing, (ii) Chinese-futures microstructure effects (price limits, thin far-month contracts, roll artifacts) inflating sorts, (iii) cost model too thin, (iv) in-window polarity setting contaminating the OOS claim (see Negative evidence).

## Signal

Source-reported normalized construction:

- **Panel/formation timestamp:** daily cross-section of the 104 contracts; factor values computed from same-day fields; **the paper never states the signal-to-execution timestamp (same-day close vs next-day open vs next session), the exchange session/timezone, or the price used for fills** → execution timing `underspecified`.
- **Lookback:** factor-specific. Formula families described in Online Appendix B use rolling windows of **5, 7, 10, 20 days** (e.g., 5/20-day moving-average difference, 7-day rolling means, 10-day volatility) plus same-day OHLCV/basis/spot/premium-discount terms. Warm-up and endpoint inclusivity not stated → `data gap`.
- **Single-factor long entry:** daily rank by factor value; **long top 10%** of futures by factor value.
- **Single-factor short entry:** **short bottom 10%** by factor value. (Long-only variant: top decile only.)
- **Polarity (multi-factor):** each factor's sign is fixed *statically* from the historical long-short return of that factor in a first segment — **in-sample sign window 2010/01/04 → 2017/12/29** (Table 5 note) — or adjusted *dynamically* daily using cumulative historical returns (§3.2). For the **OOS multi-factor static portfolio the sign window is printed as 2023/05/04 → 2023/12/31** (Table 10 note), which lies **inside** the OOS evaluation window 2023/05/04 → 2024/10/31 → in-window selection, see Negative evidence.
- **Multi-factor aggregation:** signals are standardized, combined with those polarities into a composite score, then *"the average factor value for each futures is computed using the updated values"* (§3.2). **Standardization transform (z-score / min-max / rank), weighting (equal vs other), and deduplication of overlapping factors are not stated** → `underspecified`.
- **Exit / holding period / re-entry:** **not stated.** Daily ranking implies daily rebalancing and an implicit ~1-day hold, but no exit rule, no stop, no holding-period cap, and no overlap/turnover treatment appear anywhere in v1 → `underspecified`.
- **Position sizing:** **not stated** — nothing specifies equal-weight within the decile, notional per contract, leverage, margin, or capital base. Top/bottom 10% of 104 ≈ ~10 contracts per side (research-computed from the stated universe). → `data gap`.
- **Parameters:** decile cut 10%/10% (source); 40 formulas retained from the GPT stream (source); fee 0.025% (source, basis unstated); IPCA-5 chosen as best of IPCA 1–5 **on the same evaluation data** (source, §3.2 — benchmark-selection caveat). **No parameter is reported as cross-validated.** Any operational detail above marked `data gap`/`underspecified` is **not** filled in by this record.
- **Benchmarks:** IPCA-5 alpha for Tables 4/6/9/11; significance stars `***/**/*` = 1%/5%/10%, **but the regression frequency, test statistic, and Newey–West/HAC treatment are never stated** → `underspecified`.
- **IC definition:** Spearman IC mean and IR over **2010/01/04 → 2023/04/07** (Table 1 note) — i.e., **the IC table ends before the OOS window; no OOS IC is reported**.

## Required data

- **Instrument/universe:** 104 Chinese leading (主力) and secondary (次主力) **continuous** futures contracts — all CFFEX stock-index futures plus liquid commodity futures (SHFE/DCE/CZCE per Table A1 listing dates; venue names not itemized in the text → `data gap`).
- **Market type:** exchange-traded futures (daily bars); no options, no perps.
- **Vendor/fields:** Wind daily `basis, spot, futures premium and discount, open, high, low, close, volume, amount, futures name, return`.
- **Roll treatment:** contracts are *"continuous"* series, but **the roll rule (back/forward adjust, roll date, volume-threshold switch between leading/secondary contract) is never stated** → `data gap`; roll artifacts could dominate cross-sectional ranks.
- **Timeframe:** daily bars; session timezone and settlement-price convention not stated → `data gap`.
- **Point-in-time:** Table A1 gives listing dates; late-listed contracts enter the cross-section over time, but no minimum-history filter, liquidity filter, or universe-stability rule is stated → survivorship/listing-selection risk `data gap`.
- **Missing data:** *"some futures data do not span the entire period"*; no missing/stale/suspended-day handling or imputation policy stated (imputation unknown, not assumed).
- **Cost-related fields:** no fee schedule, tick size, tick value, margin rate, or daily price-limit table is included → `data gap`.
- **Availability:** commercial (Wind); no sample file, no code released with v1.

## Execution assumptions

Source-reported:

- Rebalance cadence: daily re-ranking (implied by *"Futures are ranked daily"*, §3.2); exact order timing/price `underspecified`.
- Cost: single **0.025%** *"transaction fee"* producing starred columns; **basis (side/base) unstated** → `underspecified`.
- Fill model, latency, partial fills, bid-ask spread, slippage, market impact, participation limits, capacity: **not stated** → `data gap`.
- Chinese-specific frictions — **daily price-limit days where the sort cannot be filled**, no-trade/holiday handling, margin financing, short-sale availability on every contract, delivery-month constraints, and continuous-series roll cost: **not stated** → `data gap` (never treated as zero).
- Leverage/margin/borrow: not stated → `data gap`.

Scout assumptions: **none added.** This record does not impute a fill price, a spread, or a sizing rule the source does not give.

## Evidence

### Source-reported

All figures below are **source-reported, not verified by us**, and trace to `https://arxiv.org/html/2509.23609v1` (v1, 2025-09-28), with the exact table named for each. Equities/futures asset class: **Chinese futures**, not crypto.

- **Table 1 (Spearman IC/IR, 2010/01/04–2023/04/07):** Factor 34 **IC 0.3021 / IR 1.2645** (best), Factor 22 **0.1673 / 0.6756**, Factor 9 **0.1326 / 0.6152**, Factor 7 **IC −0.5821 / IR −3.5624** (worst).
- **Table 2 (In-sample long-short, 2018/01/02–2023/04/07; gross / `*` fee-adjusted):** Factor 22 **7.4961 / Sharpe 8.8570 / MDD 0.1444** (`*`: 6.4980 / 8.3447 / 0.1528); Factor 9 **3.4037 / 7.9222 / 0.1138** (`*`: 2.8851 / 7.2588 / 0.1253); Factor 17 **1.9102 / 8.2322 / 0.0298**; Factor 7 **−0.9983 / −27.3291 / 1.0000**; Factor 34 **−0.9688 / −18.0299 / 1.0000**.
- **Table 5 (In-sample multi-factor):** static long-only **0.6528 / Sharpe 2.26 / MDD 0.2704**; static long-short **0.8111 / 3.0218 / 0.1623**; dynamic (long-only-referenced) long-only **0.5553 / 2.4939 / 0.2452**, dynamic long-short **0.7121 / 2.6781 / 0.2189** (§5.1 narrative citing Table 5).
- **Table 4 (In-sample single-factor alpha vs IPCA-5):** Factor 9 long-short **0.2551\*\*\***, long-only **0.6112\*\*\***; Factor 28 **0.2281\*\*\***; Factor 22 **0.3812\*\*\*** (LS) / **1.1835\*\*\*** (LO); Factor 31 **0.2316\*\*\***; Factor 18 long-only **1.3927\*\*\***; Factor 7 long-short **−1.1335\*\*\*** (§5.1 narrative citing Table 4).
- **Table 6 (In-sample multi-factor alpha vs IPCA-5):** static **0.1330\*\*\***, dynamic (long-only base) **0.1468\*\*\***, dynamic (long-short base) **0.1248\*\*\*** (§5.1 narrative citing Table 6).
- **Table 7 (Out-of-sample long-short, 2023/05/04–2024/10/31; gross / `*` fee-adjusted):** Factor 34 **22.1293 / Sharpe 13.5809 / MDD 0.0266** (`*`: 19.4221 / 13.0439 / 0.0276); Factor 22 **15.1197 / 8.8804 / 0.0743** (`*`: 13.2302 / 8.4870 / 0.0767); Factor 9 **4.5350 / 8.0580 / 0.0393** (`*`: 3.8837 / 7.4743 / 0.0417); Factor 28 **2.9793 / 5.7651 / 0.1318**; Factor 18 **0.8360 / 4.8589 / 0.0904**; Factor 1 **2.7739 / 7.0879 / 0.0740**; Factor 40 **−0.1702 / −1.1562 / 0.2310**; Factor 7 **−0.9947 / −28.8507 / 0.9993**.
- **Table 9 (Out-of-sample alpha vs IPCA-5):** Factor 1 **0.3200\*\*\*** (LS) / **0.5953\*\*\*** (LO); Factor 22 **0.7067\*\*\*** / **1.1717\*\*\***; Factor 4 **0.1360\*\*\*** / **0.4508\*\*\***; Factor 21 **0.0969\*\*** / **0.2108\*\***; Factor 26 **−0.1723\*\*\*** / **−0.2779\*\***; Factor 23 **−0.0749** / **−0.2268\***.
- **Table 10 (Out-of-sample multi-factor, 2023/05/04–2024/10/31; gross → `*` fee-adjusted):** static long-only **0.8473 / 2.4147 / 0.1836 → 0.6290 / 1.9468 / 0.2059**; static long-short **1.5955 / 3.4423 / 0.1489 → 1.2892 / 3.0069 / 0.1722**; dynamic (long-short referenced) long-only **0.7690 / 2.7765 / 0.0972 → 0.3629 / 1.4100 / 0.1108**, long-short **1.2948 / 3.6335 / 0.1072 → 0.8075 / 2.3292 / 0.1802**; dynamic (long-only referenced) long-only **1.0309 / 3.5529 / 0.0902 → 0.7900 / 2.9348 / 0.0958**, long-short **2.1175 / 4.0800 / 0.0981 → 1.7070 / 3.5962 / 0.1056**.
- **Table 11 (Out-of-sample multi-factor alpha):** static **0.2911\*\*\*** (LO) / **0.3022\*\*\*** (LS); dynamic long-only base **0.1578\*\*\*** / **0.1754\*\*\***; dynamic long-short base **0.3244\*\*\*** / **0.3418\*\*\***.
- **Fee sensitivity worked example (§5.1):** Factor 1 in-sample long-short annualized return **2.8014 → 2.3534** after 0.025%; Factor 5 **0.0125 → −0.1074** (sign flip).
- **Robustness (§7 / Online Appendix C):** *other LLMs* (Table C1): GPT-4o *"slight improvements"* over GPT-4 with *"differences not substantial"*; Copilot shows *"relatively high"* probability of negative returns; Claude *"extreme variations"* and *"severe losses"*. *Temperature* (10 dialogues × 5 factors; Tables C2/C3): Factor1-2 **24.3286 / Sharpe 16.4453 / MDD 0.0436** versus Factor2-2 **−0.5450**, Factor3-3 **−0.5642** (MDD > 0.64), Factor6-4 **−0.4757 / MDD 0.5878**, Factor6-1 **13.2776 / 13.8652**. *Simplified prompts* (Table C4): factors degrade and GPT reverts to *"well-known technical indicators such as RSI and MACD"*; printed examples include Simple7 *"9.35% return, Sharpe 12.36"* (units inconsistent with the annualized-return scale used elsewhere) and negatives such as Simple5 **−0.18 / Sharpe −0.81 / MDD 30.29%**. *Specific prompts* (Table C5): Statistical1 **13.6568**, Statistical5 **33.9494**, Trend2 **0.723 / 2.288 / 0.1372**, with the authors themselves flagging Trend1/Trend5 outliers as possibly *"not … reliable or replicable"*.
- **Benchmark:** IPCA-5 selected as best of IPCA 1–5 on the same data (§3.2); IPCA training window = polarity window, test window = backtest window (§3.2).

### Independently reproduced

not independently reproduced. This run consisted of directly reading the arXiv landing page and the v1 full HTML (methods §3, data §4, results §5, robustness §7, Online Appendices A–C), locating every quoted figure in its printed table, full-text searching v1 for cost/fill/roll statements, and running a repository-wide source-identity dedup. **We did not recompute a single backtest, fetch Wind/exchange data, re-implement any of the 40 formulas, or run any portfolio simulation.** The sign counts in Negative evidence are counts of cells printed in the source's own tables, not a re-run.

### Negative evidence

1. **Fee-adjusted sign flips contradict "negligible cost" (our count of the source's own Table cells):** in-sample long-short — only **17 of 40** factors stay positive after the paper's own 0.025% fee (**23 of 40 turn negative**); in-sample long-only **16/40** positive; out-of-sample long-short **25/40**; out-of-sample long-only **21/40**. The paper's §5.1/§5.2 wording (*"majority … remain stable"*, *"impact … remains negligible"*) describes magnitude changes, not sign survival.
2. **Narrative-vs-table contradiction inside the source:** §5.1 states *"28 factors exhibited positive returns, while 12 displayed negative"* for Table 2; our count of the 40 printed Table-2 gross annualized returns gives **27 positive / 13 negative** (zero exact zeros; near-zero Factor 5 +0.0125 and Factor 8 +0.0076 both counted positive).
3. **The best-IC factor is the worst in-sample trade:** Factor 34 has the top IC (0.3021) yet an in-sample long-short **annualized −0.9688, Sharpe −18.0299, MDD 1.0000** (full loss), then an out-of-sample **+22.1293 / Sharpe 13.5809 / MDD 0.0266**. IC and tradable PnL disagree in sign over the same construction; Factor 7 loses ~100% in **both** windows (MDD 1.0000 / 0.9993).
4. **Massive uncorrected multiple testing:** 40 retained formulas + 10 dialogues × 5 + 4 specific-prompt families × 5 + ≥15 simplified-prompt factors ≈ **≥120 formula draws**, each run as single-factor × {long-short, long-only} and multi-factor × {static, dynamic} × {long-only, long-short} (+ fee/no-fee). **No deflated Sharpe, Sharpe-ratio t-test, White reality-check, or any selection-adjusted inference appears anywhere in v1**; headline maxima (Sharpe 8.9–16.4) are selected maxima.
5. **Sharpe scale is uninterpretable as printed:** values of 7–16+ on daily futures decile portfolios with no stated risk-free rate or annualization → `underspecified`; the same table prints Factor 34 at Sharpe −18.03 with MDD 1.0000, confirming the metric is not a conventional Sharpe.
6. **"Out-of-sample" hygiene problems:** (a) the OOS multi-factor static polarity window **2023/05/04 → 2023/12/31 is inside the OOS evaluation window 2023/05/04 → 2024/10/31** (Table 10 note) — sign selection uses part of the tested period; (b) §4's stated data end **2023/04/07** is incompatible with an evaluation window running to **2024/10/31**; (c) §4's *"data up to 2017/12/29"* conflicts with Table 2/3 notes' *"historical data from 2010 to 2021"*; (d) the OOS definition rests on GPT-4's April-2023 cutoff, yet factor retention involved **human manual novelty review and exclusion of 'sparse or aberrant' outputs** with no date bound and no disclosure of how many candidates were screened out.
7. **The IC table never touches the OOS window:** Table 1's IC/IR spans 2010/01/04 → 2023/04/07 only; **no out-of-sample IC is reported**, so the paper's central predictive-power evidence is in-window.
8. **Cost model omits every futures-specific friction:** no spread, slippage, impact, latency, **daily price-limit non-fill days**, margin/financing, borrow/short constraints, delivery-month rules, or **continuous-contract roll cost**; the single 0.025% fee has an unstated basis.
9. **Benchmark weakened by selection:** IPCA-5 was chosen as the best of IPCA 1–5 **on the same data** used to claim superiority (§3.2); alpha regression details (frequency, test statistic, HAC) unstated.
10. **Editorial/structural defects in v1:** the Table 3 (long-only) note describes the **long-short** construction (*"long positions in the top 10% … and short positions in the bottom 10%"*); the introduction's section map (Sections 4/5/6/7/8/9/10) does not match the actual numbering (3/4/5/6/7/8).
11. **Prompt/session instability is admitted by the source's own robustness section:** performance ranges from Sharpe 16.4 to strongly negative across temperature runs, yet §7.2 concludes dialogues *"do not significantly affect"* performance; simplified prompts collapse to RSI/MACD.
12. **Reproducibility blocked:** no code, no formulas beyond natural-language appendix notes, commercial Wind data, undisclosed universe-inclusion rules, undisclosed roll rule.
13. Single **preprint v1, not peer reviewed**, sample ends 2024-10-31; no second-vendor or cross-market replication in the source.

## Falsification plan

All thresholds and replication choices below are **research-proposed** operationalizations; all pass/fail cutoffs are **research-defined falsification thresholds** (none are source-reported).

- **F1 — Independent replication gate (research-defined):** rebuild the universe from a second daily futures source (official exchange daily files and/or a second vendor) with an explicitly documented leading/secondary contract and roll rule; reproduce the 40 Appendix-B formulas mechanically; fail if fewer than **30 of 40** single-factor long-short series correlate at **ρ ≥ 0.9** with the paper's printed annualized-return sign pattern (gross, same windows).
- **F2 — Cost ladder (research-defined):** 0 / 2.5 / 5 / 10 / 20 bp **per side** plus explicit roll cost and price-limit-day fill rules; fail the headline claim if the OOS (2023-05→2024-10) **static long-short multi-factor net Sharpe falls below 1.0 at 5 bp/side**, or if any of the three multi-factor OOS books changes sign at 10 bp/side.
- **F3 — Selection-adjusted inference (research-defined):** compute Deflated Sharpe Ratio (Bailey–López de Prado) over the **entire generated library** (~120 formula draws × portfolio variants, including robustness variants), accounting for non-normality and number of trials; **fail if DSR < 0.95** for the best single factor and for the best multi-factor book.
- **F4 — Placebo / null library (research-defined):** 1,000 date-shuffled (circular-shift) reruns of the full selection pipeline; the true best-net Sharpe must exceed the **95th percentile** of the placebo distribution (**|z| ≥ 2.0**) or the mechanism is judged selection luck.
- **F5 — OOS hygiene audit (research-defined):** re-run with **every** selection decision (factor retention, polarity, multi-factor weighting, benchmark choice) frozen **before 2023-05-04**; fail if the frozen OOS static long-short multi-factor **net** Sharpe (5 bp/side) drops below **0.5**, or if the in-window-frozen vs pre-frozen results differ by more than **0.5 Sharpe**.
- **F6 — IC/PnL consistency (research-defined):** compute Spearman rank IC **strictly inside 2023-05→2024-10**; fail the predictability claim if fewer than **60%** of factors with positive full-sample IC have positive OOS IC, or if OOS mean IC t-statistic (Newey–West, lag ≥ 5) is below **2.0** for the library median.
- **F7 — Baseline competition (research-defined):** on the same universe/windows/costs, run carry/basis, cross-sectional momentum, and seasonal factors (plus an IPCA-5 benchmark re-implemented without same-data model selection); fail the *"LLM prior adds value"* mechanism if the best GPT factor or multi-factor book does not exceed the **best simple baseline by ≥ 0.30 net Sharpe** at 5 bp/side.
- **F8 — Execution-timing sensitivity (research-defined):** compare same-session-close vs next-session-open entry with next-bar fill; fail if any headline book loses **> 50%** of its net Sharpe under next-session fills, or if price-limit days are excluded and performance changes by **> 0.30 Sharpe**.
- **F9 — Generation stability (research-defined):** regenerate the library in **≥ 5** fresh GPT-4 dialogues/temperature runs (the source's own protocol, extended); fail the *"reliable prior"* claim if the **median** library-level net Sharpe across runs is **≤ 0** or if fewer than **50%** of runs produce any factor with net Sharpe ≥ 1.0 after DSR correction.
- **F10 — Universe/venue transport (research-proposed):** port the identical formula templates to a second futures market (e.g., US/global commodity futures) without re-tuning; this tests whether the effect is a China-microstructure artifact (price limits, thin secondary contracts) versus a general factor prior. Action on failure: reclassify the mechanism as market-structure-specific, not LLM-prior alpha.
- **Action on failure:** any F1–F9 failure ⇒ the record's hypothesis is rejected for our purposes and no candidate-pool entry should be proposed; failures are recorded back into this record's Negative evidence.

## Crypto portability

**unproven.** The source demonstrates nothing in crypto. At mechanism level the required inputs partially exist: perp–spot **basis** and premium/discount map naturally onto the formula templates, and volume/OHLCV are ubiquitous. Porting risks are material: (i) **no daily price limits** but far higher intraday vol — cost ladder must be crypto-native (maker/taker + spread + funding); (ii) **24/7 sessions** make the daily bar/UTC-day boundary and the top/bottom-decile cutoff a new free parameter; (iii) **8-hour funding accrual** interacts with a daily-rebalanced long-short book and is absent from the source; (iv) **venue fragmentation / continuous-series construction**: perp index marks, listing churn, and thin far contracts change what "continuous" means; (v) **cross-sectional breadth** — only a handful of liquid crypto perps can hold a 10-decile sort with meaningful per-name size; (vi) LLM-prior novelty may already be arbitraged in crypto's 24/7, highly-scraped factor culture. Crypto portability is a hypothesis, not evidence, and confers no trading approval.

## Limitations

- `not independently reproduced` — no backtest, no data fetch, no formula re-implementation was performed.
- `underspecified`: execution timestamp/price, holding/exit/stop rules, position sizing, standardization and multi-factor weighting, fee basis, Sharpe definition, alpha-regression statistics, universe-inclusion rules, continuous-contract roll rule, session timezone/settlement convention.
- `data gap`: spread/slippage/impact/latency/margin/borrow/**price-limit non-fill days**/roll cost (searched in full text — absent, not zero), author affiliations, code/data availability, number of formulas screened before the retained 40, missing-data policy.
- Source contradictions preserved rather than repaired: data end 2023/04-07 vs OOS end 2024/10/31; 2017/12/29 signal cut vs "2010 to 2021" table notes; 28/12 narrative vs 27/13 table count; Table-3 note describing the long-short construction; introduction's section map mismatching the body.
- Selection/multiplicity: ~120 formula draws, four portfolio constructions, fee/no-fee variants, and a data-selected IPCA-5 benchmark, with **zero** multiple-testing correction; performance maxima are selected maxima and Sharpe magnitudes (7–16) are not interpretable without the missing definition.
- Single unreviewed preprint (v1, 2025-09-28); sample ends 2024-10-31; commercial Wind data and absent code block reproduction; no second vendor, no cross-market replication, no capacity/liquidity analysis.
- `confidence: low` refers to our **research interpretation and tradeability assessment** (single preprint, internal contradictions, no code, thin cost model, uncorrected selection), **not** to misreading the source — every quoted figure was located in its printed table/section of the pinned v1.

## Implementation status

`not-implemented`. Nothing in this record has been implemented in our research stack: no factor formulas were coded, no Chinese-futures data was acquired, no portfolio was simulated, no Qlib full backtest, no production card, and no Paper/Testnet/Live activity of any kind. The record is normalized research material only.

## Adoption boundary

Presence in this repository means **only** that a source-traceable research capture exists. It does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; or approved for implementation, paper trading, testnet, or live trading. Those stages are separate, downstream, and gated.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` — authoritative schema contract (read for this run; `kb_search` for a v2 specification returned 0 results).
- `[[quant/alphalogics-market-logic-multi-agent-factor-generation-2026-09-05]]` — nearest family: LLM/multi-agent formulaic factor generation, different source, different universe and mechanism.
- `[[quant/alphaschema-trading-semantic-plan-space-surrogate-guided-factor-mining-2026-09-05]]`
- `[[quant/alphacfg-grammar-guided-mcts-tree-lstm-formulaic-alpha-2026-09-05]]`
- `[[quant/alphar1-context-aware-alpha-screening-llm-reasoning-grpo-2026-09-03]]`
- `[[quant/factorengine-program-level-knowledge-infused-factor-mining-2026-09-05]]`
- `[[quant/llm-strategy-discovery-leakage-safe-search-deflated-eval-2026-09-04]]` — supplies the deflated-evaluation framing used in F3/F4.
- `[[quant/favor-hypothesis-grounded-agentic-factor-validation-topk-portfolio-2026-09-24]]` and `[[quant/beyond-prompting-agentic-factor-investing-composite-long-short-2026-09-24]]` — adjacent LLM factor-discovery captures on equity universes.

Wiki Brain queries this run (`GPT LLM generated factors futures`, `Chinese futures cross-sectional factor momentum`, `LLM alpha factor discovery multi-agent`) returned the records above; **none of them carries this source identity** (`arXiv:2509.23609` / "Large Language Models and Futures Price Factors in China"). No Wiki link above is fabricated; all paths were returned by `kb_search`.

## Sources

1. Yuhan Cheng, Heyang Zhou, Yanchu Liu, *"Large Language Models and Futures Price Factors in China."* arXiv preprint **arXiv:2509.23609v1 [q-fin.PR, cs.LG]**, submitted **Sun, 28 Sep 2025 03:24:10 UTC** (164 KB; comments "46 pages; 1 figure"; **no journal-ref, not peer reviewed**), DataCite DOI `10.48550/arXiv.2509.23609` — https://arxiv.org/abs/2509.23609 (landing page read 2026-09-24).
2. Same paper, **full HTML v1** used for all methods/tables quoted here — https://arxiv.org/html/2509.23609v1 (read in full 2026-09-24). Provenance anchors: §3.1 prompt/generation protocol; §3.2 portfolio construction and IPCA-5 benchmark; §4 universe (104 contracts, Wind, 2010/01/04–2023/04/07) and windows; §5.1 fee statement (0.025%) and Tables 2–6; §5.2 OOS definition (2023/05/04–2024/10/31) and Tables 7–11; §7 and Online Appendix Tables C1–C5 robustness; Online Appendix A (contract list) and B (40 factor construction notes).
