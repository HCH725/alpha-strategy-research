---
schema: strategy-research-record-v1
title: "GPT-4o Persona-Consensus Mention-Frequency Top-50 US Equity Portfolio with Six-Factor Alpha Attribution and Echo-Chamber Falsification"
created: 2026-09-22
updated: 2026-09-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - llm
  - persona-ensemble
  - cross-sectional
  - us-equities
  - factor-attribution
status: research-only
confidence: medium
source_as_of: 2026-03-31
sources:
  - "Steven Edwards, 'Do LLM \"Crowds\" Produce Investment Signals? An Empirical Test', SSRN Working Paper, Date Written 31 March 2026, posted 29 April 2026, 12 pages. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6543239 ; DOI: https://doi.org/10.2139/ssrn.6543239"
  - "SSRN PDF of the same working paper (the version read for this record): https://papers.ssrn.com/sol3/Delivery.cfm/6543239.pdf?abstractid=6543239&mirid=1"
  - "Quantpedia summary page (discovery aid only; no empirical claim in this record is taken from it): https://quantpedia.com/do-llm-crowds-produce-investment-signals-an-empirical-test/ (posted 4 September 2026)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# GPT-4o Persona-Consensus Mention-Frequency Top-50 US Equity Portfolio with Six-Factor Alpha Attribution and Echo-Chamber Falsification

## Provenance

- **Primary source:** Steven Edwards (affiliation on the paper: `Independent`; author block email printed on the paper), *“Do LLM “Crowds” Produce Investment Signals? An Empirical Test”*, SSRN working paper. Author list is a **single author** (exact as printed in the PDF header and the SSRN abstract page).
- **Version / date:** title page reads `Working Paper March 2026`; SSRN metadata reads `Date Written: March 31, 2026`, `12 Pages`, `Posted: 29 Apr 2026`. Stable identifiers: SSRN abstract id `6543239`, DOI `10.2139/ssrn.6543239`.
- **Publication / peer-review status:** SSRN-hosted working paper; **no journal, venue, or peer-review statement appears anywhere on the abstract page or in the PDF** → `not stated in source`. SSRN page shows `0 References` / `0 Citations` metadata at capture time (self-reported platform counters, not a quality signal).
- **License / redistribution:** SSRN abstract page states `The copyright holder has granted SSRN a license. All rights reserved. No reuse allowed without permission.` → this record **cites and normalizes** the idea and figures with table-level provenance and does not reproduce the paper's text wholesale (public-repository hygiene rule).
- **Stable URLs:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6543239 · https://ssrn.com/abstract=6543239 · http://dx.doi.org/10.2139/ssrn.6543239 · PDF: https://papers.ssrn.com/sol3/Delivery.cfm/6543239.pdf?abstractid=6543239&mirid=1
- **Primary-source checksum (performed 2026-09-22):** the SSRN abstract page and the **full 12-page SSRN PDF** were opened and read directly (PDF: 516,259 bytes, 12 pages, SHA-256 `7f5b09d4410382f476585e3b5fd46ec76ad0907b35dad2a433e89513ad17a95b`). Verified against the PDF: single-author list; Working-Paper-March-2026 / written 31 Mar 2026 / posted 29 Apr 2026 dates; sample period (561 trading days, January 2024 → March 2026; factor regressions `N = 540`); universe (top-50 mention-frequency portfolio drawn from 1,059 unique US-listed tickers named by 100 GPT-4o personas; all 50 constituents are S&P 500 members; weights as of December 2023; benchmarks SPY and RSP); **transaction-cost treatment (no commission, spread, slippage, impact, borrow, or fee assumption is stated anywhere in §3.3 Portfolio Construction, §3.4 Performance Evaluation, Table 2, Table 3, or the table notes** → every cost field in this record is marked `not stated in source`, and whether the reported returns are gross or net of costs is `underspecified` — it is *not* asserted either way); and every performance number quoted below was located in the PDF's Table 2, Table 3, §4.1–§4.3, or Appendix A/Table A1.
- **Deduplication audit (repository-wide, not `git log`):** `ripgrep` across **all existing `*.md` records and `coverage_manifest.csv`** for `6543239`, `abstract_id=6543239`, `Steven Edwards`, `LLM Crowds`, `synthetic consensus`, `wisdom of crowds`, `consensus portfolio`, `mention frequency`, `media prominence`, `echo-chamber` → **zero source-identity hits** (case-insensitive variants for `echo chamber` matched two records whose sources are arXiv `2606.29251` on LLM-compressed financial analysis and a crypto salience-theory record — different sources, different mechanisms, checked). Nearest neighbors and why this record is independent: `llm-persona-ensemble-stock-bond-portfolio-cpi-regime-timing-2026-09-22.md` (Abe et al., arXiv:2411.19515 — persona ensemble used for **40/60 stock-bond allocation timing** via macro-indicator classification; this record's source is a different paper whose cross-sectional **US-equity top-50 mention-frequency ranking** is a different signal construction, different universe, different horizon; Edwards explicitly cites Abe et al. as the closest prior work with only three personas); `digital-twin-finfluencer-belief-elicitation-silent-region-cross-sectional-2026-09-06.md` (finfluencer-replica belief scores, different source and construction); `llm-distilled-kol-consensus-capability-factor-aggregation-2026-09-18.md` (crypto KOL capability-weighted IC consensus, different source and market); `small-cap-alpha-beta-separation-uncertainty-aware-llm-portfolio-2026-09-02.md` (arXiv:2608.12283, small-cap LLM news/macro/technical stack, different source and mechanism). Material distinction therefore rests on: **source identity (SSRN 6543239), signal construction (free-recall persona mention-frequency ranking), universe (S&P 500-membership top-50 US equities), and the paper's own echo-chamber/neutral-control falsification apparatus** — all absent from every existing record.
- **Schema provenance:** structure and frontmatter follow the canonical Wiki Brain contract `quant/strategy-research-record-spec-v1` (`schema: strategy-research-record-v1`), re-resolved and re-read this run; README workflow contract re-read this run.
- **Discovery path:** found via a Quantpedia listing dated 4 September 2026; the Quantpedia page was used **only** to locate the SSRN identifier. All fields in this record come from the SSRN abstract page and the SSRN PDF itself.

## Economic mechanism

### Source-reported

- The paper frames the tested hypothesis in Surowiecki/Galton terms: a sufficiently large, philosophically diverse ensemble of LLM investor personas could reproduce the **information-aggregation dynamics** of a real crowd (conditions: diversity of opinion, independence of participants, aggregation mechanism), such that the consensus portfolio exhibits crowd-wisdom signal quality.
- The author's stated finding is a two-part verdict. (1) **Information aggregation fails**: all personas are queried from one model trained on one corpus, so the independence condition is “violated by construction”; the consensus portfolio reproduces “the most media-prominent US equities,” shares **92% of constituents with a single neutral GPT-4o call**, and converges to ~88% of its final composition with as few as 25 personas — the author reads this as an **echo chamber / coverage-prominence proxy**, consistent with He et al. (2024) on LLM collectives reflecting training-data patterns.
- (2) **Performance is attributed cautiously**: the market-cap-weighted consensus shows ~10% annualised alpha surviving FF5+momentum adjustment, but the author offers three live interpretations — regime-specific mega-cap technology re-rating not captured by standard factors, omitted systematic exposures (e.g. intangible-capital intensity / AI narrative loading), or return-relevant information encoded in the training corpus — and states the data **cannot distinguish among them** from a single market cycle.

### Research interpretation

- Falsifiable mechanism decomposition of the tested strategy:
  - **Signal channel (source-reported construction):** mention frequency across 100 persona free-recall queries proxies **financial-media / analyst-coverage prominence**, which the paper shows is only weakly related to market-cap rank (Spearman r = 0.213, p = 0.141 for GPT-4o).
  - **Independence channel (source-reported finding):** shared-corpus correlation makes ensemble members non-independent, so extra personas add almost nothing beyond one neutral call (92% overlap; saturation by N ≈ 25–30).
  - **Return channel (source-reported result, source-uncertain cause):** only the market-cap weighting produces significant factor-adjusted alpha; equal and conviction weightings — the two weightings that actually express “crowd consensus strength” — produce **no significant alpha**. The economically honest reading is that any residual return is concentrated in the largest holdings during an AI-driven large-cap tech regime rather than in the consensus ranking itself.
- If treated as a hybrid strategy, component roles are: **signal** = top-50 by mention frequency; **weighting** = market-cap (only weighting with significant alpha), equal, or conviction (∝ mentions); **rebalance** = quarterly; **regime filter / stop / sizing overlay** = **none exist in the source** (no filter, stop, or risk overlay is specified). Do not assume any component beyond weighting contributes alpha; the paper's own ablation across three weightings says the ranking alone does not.

## Signal

All of the following is `source-reported` from the SSRN PDF unless marked otherwise.

- **Formation timestamp:** one API query campaign using OpenAI `GPT-4o` (paper states a documented **training-data cutoff of October 2023**); the **exact calendar date(s) on which the 100 queries were executed are not stated** → `data gap`. Backtest start (January 2024) is chosen to be after the stated model cutoff to limit look-ahead.
- **Persona construction:** 100 personas varied across six axes (investment style: value/growth/momentum/income/quantitative/ESG/thematic/sector-specialist; time horizon; geographic focus; sector emphasis; risk appetite; philosophical archetype). Temperature is calibrated to archetype: systematic/rules-based personas `0.2`, GARP example `0.4`, speculative/contrarian `0.7–0.9` (Table 1 shows three representative personas with excerpted prompts). **Full persona specifications and the exact user prompt are not in the paper** — footnote 1: “Python pipeline, full persona specifications, and replication code available from the author on request” → `underspecified` / not publicly retrievable.
- **Pick collection:** each persona asked for exactly 50 US-listed equity selections in structured JSON (ticker, company name, one-sentence rationale); realized dataset = **5,075 picks across 100 personas**, **1,059 unique tickers** (§3.2, §4.1).
- **Selection rule:** rank tickers by **mention frequency** (count of distinct personas naming the ticker); take the **top 50**. Tie-breaking rule `not stated in source` → `underspecified`.
- **Weighting (three schemes):** equal weight `1/N`; conviction weight proportional to mention frequency; market-cap weight proportional to **market capitalisation as of December 2023**. Sector-constrained variants cap each sector's weight within **±5 percentage points of SPY sector weights** (source-reported; results “materially consistent” with unconstrained).
- **Entry / holding / exit / re-entry:** portfolios are **rebalanced quarterly** (§3.3). No stop, take-profit, or tactical exit exists in the source. Intra-quarter trading, execution price convention, rebalance date rule, and treatment of delistings are `not stated in source` → `data gap`.
- **Control and robustness arms (source-reported):** (a) neutral control = single unpersonalised GPT-4o prompt at temperature 0.0; (b) bootstrap ensemble-size analysis, N ∈ {5,10,15,20,25,30,40,50,75,100}, 200 iterations per N; (c) statistical test of overlap against random S&P 500 draws; (d) Appendix A cross-model replication with Claude Sonnet (constituent comparison only — performance comparison omitted by the author because Claude's cutoff overlaps the test window).
- **Parameters:** all thresholds/windows above are fixed as described by the source; **no parameter tuning or search is reported** (the paper does not claim a tuned configuration, and also does not disclose whether alternatives were tried) → treat all values as source-fixed, tuning history `not stated in source`.
- **Reproducibility:** the signal is **partially reconstructable** — logic and headline parameters are in the paper, but persona prompts, full specifications, query date, and code are only “available from the author on request” → the record is **not** presented as independently reproducible.

## Required data

- **Universe / instrument:** 50 US-listed common equities selected as above; all 50 are S&P 500 members “based on available constituent data” (the constituent-data vendor and point-in-time membership rule are `not stated in source` → `data gap`). Benchmarks: SPY (S&P 500 cap-weighted) and RSP (S&P 500 equal-weighted).
- **LLM data:** OpenAI GPT-4o API access with the (unpublished) persona system prompts and user prompt; temperature assignments per persona; JSON pick responses. Full specs not public (see Signal).
- **Market data:** December 2023 market capitalisations for cap weighting; SPY/RSP daily prices for benchmark and rebalanced-portfolio construction; S&P 500 sector weights (as of `not stated in source`) for the ±5pp-constrained variants; S&P 500 constituent membership for the overlap tests.
- **Factor data:** Kenneth French data library **US domestic daily** Fama-French five factors (MKT_RF, SMB, HML, RMW, CMA), momentum (UMD), and the daily risk-free rate used in Sharpe calculations (source-reported; library URL in Sources).
- **Point-in-time / availability:** backtest confined to 561 trading days from **January 2024 to March 2026** (Table 2 caption), explicitly after the stated October 2023 model cutoff; factor regressions use `N = 540` trading days “limited by factor data availability” (Table 3 note).
- **Timestamp / timezone:** `not stated in source` — the paper specifies daily US-equity and US-factor data but never declares a timezone, session close convention, or data-vendor timestamp rule → `data gap`.
- **Missing data / delisting handling:** `not stated in source` → `data gap`.
- **Costs and funding fields:** commissions, bid-ask spread, slippage, market impact, borrow fees, leverage, and funding are **each** `not stated in source` (verified absent from §3.3, §3.4, Table 2/3 and their notes).

## Execution assumptions

- **Source assumptions:** quarterly rebalancing across the fifty constituents; weights per the chosen scheme (equal / conviction / market-cap as of Dec-2023); benchmarks SPY/RSP; risk-free rate from French's library; OLS factor regressions with HC3 heteroskedasticity-robust standard errors (Breusch-Pagan test confirmed heteroskedasticity for the market-cap-weighted regression).
- **Everything below is `not stated in source` (verified by reading the PDF's Methods/Evaluation sections):** order type; market vs limit; fill model; signal-to-order delay; execution price at rebalance; latency; partial fills; **commissions; spread; slippage; market impact; capacity/liquidity participation; borrow or shorting availability (construction weights only long constituents and never mentions a short leg or leverage)**; leverage/margin; fees of any kind.
- Consequently the **gross-vs-net status of every return, Sharpe, drawdown, and alpha figure in this record is `underspecified`** — the source does not say whether costs were applied, and this record does **not** infer that they were omitted (per primary-source cost-judgement rule: when the relevant sections are readable yet silent, mark `not stated in source` rather than presuming a modelling choice).
- **Scout-added assumptions: none.** No execution, cost, timing, or sizing choice in this record is supplied by the Scout; where a cost level is later needed for testing, it appears only inside the Falsification plan and is explicitly labelled `research-proposed`.

## Evidence

### Source-reported

Every figure below is `source-reported` from the SSRN PDF (all “not independently reproduced”), with table/section provenance; US-equity asset class, single sample window Jan 2024 → Mar 2026:

- **Table 2 (Portfolio Performance Metrics, January 2024 to March 2026; 561 trading days; Sharpe uses daily risk-free rate from French's library):** MCap unconstrained — total return **77.8%**, annualised **29.5%**, ann. vol **19.1%**, Sharpe **1.20**, max DD **−21.2%**, Calmar **1.39**; Equal unconstrained — 39.4% / **16.1%** / 14.2% / **0.78** / −17.0% / 0.95; Conviction unconstrained — 38.6% / **15.8%** / 14.6% / **0.74** / −17.8% / 0.89; MCap constrained — 78.6% / 29.7% / 19.6% / 1.18 / −21.5% / 1.38; Equal constrained — 40.0% / 16.3% / 15.7% / 0.73 / −18.9% / 0.86; Conviction constrained — 39.5% / 16.1% / 16.1% / 0.71 / −19.5% / 0.83; **SPY** — 37.4% / **15.3%** / 16.1% / 0.66 / −18.8% / 0.82; **RSP** — 23.6% / **10.0%** / 14.4% / 0.39 / −17.8% / 0.56.
- **Table 3 (Six-Factor Decomposition, FF5 + UMD, HC3 robust SEs, N = 540):** MCap weight — annualised alpha **9.65%**, **t = 3.271**, **p = 0.001**, R² **95.7%**, βMKT **1.125**, βSMB **−0.133**, βHML **−0.228**, βRMW **0.173**, βCMA **0.025**, βUMD **0.059**; Equal weight — alpha **3.39%**, t = 1.236, p = **0.217**, R² 93.0%; Conviction weight — alpha **2.57%**, t = 1.022, p = **0.307**, R² 94.3%.
- **Constituent analysis (§4.1):** MSFT **71** and AAPL **70** mentions (highest); all **50** consensus constituents are S&P 500 members, overlap with random US-equity draws significant at **p < 0.001**; coverage-vs-size divergences INTC (mcap rank 40), NFLX (21), ADBE (81), PYPL (104); Spearman(mention frequency, S&P 500 mcap rank) = **0.213, p = 0.141** for GPT-4o.
- **Neutral control (§4.1):** single neutral GPT-4o call (T = 0.0) shares **92% (46/50)** constituents with the 100-persona ensemble; ensemble-unique = AMD, AVGO, GE, LMT; control-unique = BMY, CMCSA, GS, LOW.
- **Bootstrap (§4.2, 200 draws per N):** mean overlap with full consensus ≈ **88% by N = 25**, **91% by N = 30**, already **66% at N = 5** (range ≈ 45%–88%).
- **Appendix A / Table A1 (cross-model):** GPT-4o vs Claude Sonnet consensus overlap **28 of 50 (56%)**; Spearman(mention, mcap rank) under Claude = **0.574, p < 0.001** vs 0.213 (p = 0.141) under GPT-4o; performance comparison across models explicitly omitted by the author (Claude cutoff overlaps the evaluation window).
- **Abstract-level claim:** market-cap-weighted consensus “returned 29.5% annualised versus 15.3% for SPY, with a statistically significant annualised alpha of approximately 10% … (t = 3.27, p = 0.001)” — consistent with Table 2/Table 3 rows above.

### Independently reproduced

`not independently reproduced`

### Negative evidence

Rich and largely **internal to the same primary source** (all `source-reported`, read in the PDF):

- **The two weightings that express crowd consensus produce no alpha:** equal-weight p = 0.217 and conviction-weight p = 0.307 (Table 3) — only the market-cap weighting is significant, i.e. the “crowd” component itself carries no demonstrated return signal.
- **Independence condition fails by construction:** one model, one corpus; **92% constituent overlap** with a single neutral temperature-0 call; **four** stocks separate the 100-persona ensemble from one plain prompt.
- **Ensemble-size saturation:** ~88% convergence at N = 25 personas — incompatible with slow aggregation of genuinely diverse views (§4.2); marginal personas add nothing.
- **Signal is coverage, not size:** mention frequency is uncorrelated with market-cap rank at conventional levels (r = 0.213, p = 0.141), and divergences track heavy media/analyst coverage (ADBE, NFLX, PYPL, INTC) → the ranking is a media-prominence proxy (§4.1, §5).
- **Author's own practitioner verdict:** “Practitioners should not expect this approach to generate alpha”; residual alpha “most likely reflects concentrated exposure to large-cap technology equities during an AI-driven market re-rating rather than genuine stock selection skill; replication across regimes is required” (abstract, §5, §6).
- **Single-regime, single-model evidence:** one market cycle (Jan 2024 → Mar 2026, a large-cap-tech-led window) and one main model family; the author lists look-ahead mitigation as partial and generalisation as open (§5 Limitations).
- **Drawdown concentration:** the market-cap variant's early-2025 and early-2026 declines are attributed by the source to higher market beta (§4.3), consistent with the regime-beta reading.
- **External contrary/confirming literature identified in the reviewed sources:** none beyond what the paper itself cites (He et al. 2024 on LLM collectives mirroring training data; Romanko et al. 2023 and Abe et al. 2024 as adjacent positive/limited prior work); absence of further contrary sources in this search is **not** evidence that none exist.

## Falsification plan

Labels: thresholds below that the Scout chose are `research-defined falsification threshold`; any operational value not fixed by the source (e.g. cost levels) is `research-proposed`. Nothing here is presented as source-reported.

1. **Regime replication / out-of-sample extension (paper's own priority).** Data: portfolio composition frozen at the source's mention-frequency rule; extend evaluation beyond March 2026 as data accrues, and separately backfill a pre-2024 window using a model snapshot whose cutoff precedes that window. Metric: six-factor alpha t-statistic on the market-cap-weighted portfolio. Failure rule (`research-defined falsification threshold`): out-of-sample |t| < 2.0 with alpha sign unstable across subwindows → reject “alpha as signal” and retain only the regime-beta interpretation. Action: mark hypothesis rejected in an updated record; do not advance to candidate pool.
2. **Neutral-control ablation (persona marginal value).** Data: re-run the full pipeline with (a) the single neutral prompt and (b) N ∈ {1,5,10,25} personas. Metric: difference in annualised return and alpha vs the 100-persona ensemble. Failure rule (`research-defined`): ensemble − control alpha difference not significant at p < 0.05 → conclude persona diversity adds nothing (confirming echo chamber) regardless of headline returns. Action: reject the “crowd” mechanism; keep only prominence/size explanations.
3. **Cost / turnover stress (`research-proposed` cost grid, since the source states no costs).** Data: quarterly-rebalanced top-50 portfolios with 5 / 15 / 30 bps-per-side implementation shortfall plus observed SPY constituent spreads. Metric: net-of-cost six-factor alpha. Failure rule (`research-defined`): net alpha 95% CI includes 0 at the mid cost level (15 bps/side) → reject tradability of the strategy as-is. Action: research-only retention with explicit “not tradable under stated costs” note.
4. **Competing-explanation test: size/sector/tech loading.** Data: re-estimate with industry factors, size×momentum interacted factors, and an AI/tech-theme exposure control (e.g. cap-weighted semiconductor/AI-adjacent basket). Failure rule (`research-defined`): alpha t-stat falls below 2.0 once these controls enter → attribute returns to unmodelled large-cap tech exposure, not stock selection. Action: downgrade any alpha claim to “factor-mis-specification artefact”.
5. **Size/sector-matched placebo.** Data: 10,000 random 50-stock draws from the S&P 500 matched on December-2023 market-cap decile and sector weights, run through the identical quarterly-rebalance, factor-regression pipeline. Failure rule (`research-defined`): consensus portfolio's alpha or Sharpe not in the top decile of the placebo distribution (p ≥ 0.10) → reject selection skill. Action: reject signal, keep record as negative-evidence artifact.
6. **Cross-model and prompt robustness.** Data: repeat pick collection with ≥2 additional model families and ±1 paraphrase of the user prompt; compare constituent Jaccard and resulting alpha. Failure rule (`research-defined`): mean pairwise constituent Jaccard < 0.5 across reruns, or alpha significance flips → reject robustness (signal is model/prompt-specific). Action: reject as stable hypothesis.
7. **Point-in-time / leakage audit.** Verify: actual query date(s) precede no part of the evaluation window in a way that imports post-cutoff knowledge; GPT-4o version actually used and its documented cutoff (the paper asserts October 2023 — re-verify against the deployed model snapshot, since silent model updates are common → `research-proposed` audit step). Failure rule (`research-defined`): any confirmed post-cutoff information path → invalidate the whole backtest. Action: reject outright.
8. **Multi-cycle sample requirement.** Minimum sample (`research-defined`): ≥3 distinct regime segments spanning a large-cap-tech drawdown and a non-tech leadership window; a single-cycle result cannot pass. Action while unmet: status stays `research-only` regardless of headline numbers.

## Crypto portability

**`unproven`**

- The source contains **zero crypto evidence**; it trades US-listed S&P 500 constituents and uses December-2023 equity market caps, SPY sector weights, and Fama-French US equity factors — none of which exist in crypto.
- A port would have to replace: index membership (no canonical crypto “S&P” analog; research-proposed substitutes such as top-N by free-float cap or index-membership of a venue index are **not** source-reported), the coverage-prominence channel (crypto media/CT prominence dynamics differ), and the entire factor-decomposition benchmark (FF5+UMD is inapplicable; a crypto port needs its own benchmark set).
- Market-structure differences that matter: 24/7 sessions and candle boundaries vs US RTH; venue fragmentation and per-venue survivorship/listing effects; no shorting friction comparability (perpetual funding, borrow); stablecoin/quote-currency effects; index-constituent rebalance mechanics vs quarterly equity rebalance.
- The echo-chamber finding itself (personas are non-independent, consensus ≈ prominence) is the part most plausibly portable as a **hypothesis about LLM behaviour**, but as a *trading signal* in crypto it would be a new, untested hypothesis — any crypto version must be registered as a fresh record, not as this record's continuation.

## Limitations

- `not independently reproduced` — no replication by this Scout; replication code is **not public** (“available from the author on request”).
- `data gap` — exact persona prompt texts and full persona specifications, query date(s), tie-breaking rule, execution price/rebalance-date convention, constituent-data vendor, timezone/session convention, delisting/missing-data handling, turnover, and capacity are all absent from the source.
- `not stated in source` — commissions, spread, slippage, impact, borrow, leverage, funding, fees; gross-vs-net status of all performance figures is therefore `underspecified` (not inferred either way).
- `underspecified` — whether any parameter/prompt alternatives were tried (tuning history undisclosed; the three-weighting comparison is a small multiple-comparison set whose “winner” is the market-cap weighting).
- Single market cycle (Jan 2024 → Mar 2026) that coincides with an atypical large-cap technology regime; single main model family (Appendix A adds Claude for constituents only).
- Source-quality: SSRN working paper, single independent author, **peer-review status `not stated in source`**; citation counters were 0/0 at capture time; SSRN license permits no reuse without permission (cite/normalize only).
- Statistical caveats as disclosed by the source: factor regressions use N = 540 days with HC3 SEs; the abstract's “approximately 10%” alpha corresponds to Table 3's 9.65% (t = 3.271) — quoted with table provenance rather than rounded freely.
- The record documents a **tested-and-mostly-falsified** hypothesis: presence of this record is not evidence the strategy works.

## Implementation status

`implementation_status: not-implemented`.

No part of this strategy has been implemented in our research stack: no signal pipeline, no backtest, no Qlib run, no production card, no Wiki Brain ingestion, no candidate-pool entry, no Paper, Testnet, or Live activity exists for this record. The only computation performed by this Scout was reading and checksum-verifying the primary source and searching this repository for duplicates.

## Adoption boundary

`status: research-only` · `adoption: not-approved` · `approval_scope: research-only`.

This record being present in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. No wording, evidence count, or confidence value in this record promotes it.

## Related Wiki records

No related Hermes Wiki Brain page was identified by this run's pre-write searches (`kb_search` on “LLM persona ensemble portfolio” and “wisdom of crowds LLM stock selection consensus” returned only an unrelated microstructure-alpha record and zero results respectively) → **no Wiki link is asserted** (links are not fabricated). Nearest related *repository* records (for retrieval, not endorsement) are listed in the Provenance deduplication audit: `llm-persona-ensemble-stock-bond-portfolio-cpi-regime-timing-2026-09-22.md`, `digital-twin-finfluencer-belief-elicitation-silent-region-cross-sectional-2026-09-06.md`, `llm-distilled-kol-consensus-capability-factor-aggregation-2026-09-18.md`, `small-cap-alpha-beta-separation-uncertainty-aware-llm-portfolio-2026-09-02.md`.

## Sources

- Steven Edwards, *“Do LLM “Crowds” Produce Investment Signals? An Empirical Test”*, SSRN Working Paper (written 31 March 2026; posted 29 April 2026; 12 pages). Abstract page: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6543239 · https://ssrn.com/abstract=6543239 · DOI: https://doi.org/10.2139/ssrn.6543239 · PDF read for this record: https://papers.ssrn.com/sol3/Delivery.cfm/6543239.pdf?abstractid=6543239&mirid=1 (516,259 bytes, 12 pages, SHA-256 `7f5b09d4410382f476585e3b5fd46ec76ad0907b35dad2a433e89513ad17a95b`, retrieved 2026-09-22). All performance, parameter, and methodological claims in this record trace to this PDF's §3.1–§3.4, §4.1–§4.4, Tables 1–3, Appendix A/Table A1, and its abstract.
- Quantpedia listing page (discovery aid only; no empirical claim taken from it): https://quantpedia.com/do-llm-crowds-produce-investment-signals-an-empirical-test/ (posted 4 September 2026).
- Data dependencies **as reported by the source** (not fetched by this Scout): Kenneth French data library, US domestic daily factors and risk-free rate — https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ ; OpenAI GPT-4o API with stated October 2023 training cutoff (source-reported); December 2023 market capitalisations and SPY/RSP price series (vendor `not stated in source`).
