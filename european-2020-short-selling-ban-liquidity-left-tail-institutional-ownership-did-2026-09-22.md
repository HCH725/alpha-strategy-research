---
schema: strategy-research-record-v1
title: "2020 European Short-Selling Bans: Liquidity Cost and Left-Tail Support Conditional on Institutional Ownership (Difference-in-Differences)"
created: 2026-09-22
updated: 2026-09-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equities
  - regulatory-event
  - short-selling-ban
  - difference-in-differences
  - liquidity
  - bid-ask-spread
  - left-tail
  - drawdown
  - institutional-ownership
  - adverse-selection
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - "Pasquale Della Corte, Robert Kosowski, Dimitris Papadimitriou, Nikolaos P. Rapanos, 'The Double-Edged Sword of Short-Selling Bans', arXiv:2609.08881v1 [q-fin.TR], September 8, 2026. https://arxiv.org/abs/2609.08881"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# 2020 European Short-Selling Bans: Liquidity Cost and Left-Tail Support Conditional on Institutional Ownership (Difference-in-Differences)

## Provenance

- **Primary source:** Pasquale Della Corte, Robert Kosowski, Dimitris Papadimitriou, Nikolaos P. Rapanos, *"The Double-Edged Sword of Short-Selling Bans"*, `arXiv:2609.08881v1 [q-fin.TR]`, v1 submitted **Tue, 8 Sep 2026 15:21:57 UTC** (submitter shown on the arXiv abs page: Robert Kosowski).
- **Stable URL:** https://arxiv.org/abs/2609.08881 · **DOI:** https://doi.org/10.48550/arXiv.2609.08881
- **Full text read for this record:** https://arxiv.org/html/2609.08881v1 (Sections 1–5, Hypotheses 1–3, Figures 2–4 captions, Tables 1–8, Appendix Tables A.2–A.4 captions/rows) and the abs page (fetched 2026-09-22).
- **Authors and affiliations exactly as the primary source states in its author footnote:** Pasquale Della Corte — Imperial College London and the Centre for Economic Policy Research (CEPR); Robert Kosowski — Imperial College London, CEPR, and the Oxford-Man Institute of Quantitative Finance; Dimitris Papadimitriou — King's College London and the University of Cyprus; Nikolaos P. Rapanos — Imperial College London.
- **Subjects:** Trading and Market Microstructure (`q-fin.TR`) — this is the only subject listed on the abs page. **No `Comments` field and no `Journal reference` field are present on the arXiv abs page as fetched 2026-09-22** → peer-review status and page count are `not stated in source`; license is shown only as arXiv's generic "view license" link → license name `not stated in source`.
- **Sample / universe:** daily bid and ask prices and total return indices from **Datastream**, **2 January 2020 – 2 June 2020**, across **17 European markets** (Austria, Belgium, Denmark, Finland, France, Germany, Greece, Ireland, Italy, Netherlands, Norway, Poland, Portugal, Spain, Sweden, Switzerland, United Kingdom). Micro- and nano-caps (market cap below **USD 250 million**) and observations with negative bid-ask spreads are dropped → **1,922 stocks, more than 200,000 daily observations**, converted to USD with daily spot FX from the same database (`source-reported`, §3.2 and Table 1).
- **Institutional ownership:** percentage of shares outstanding held by institutions **as of December 2019, from Bloomberg** (13Fs, US and international mutual funds, schedule Ds, aggregate institutional stake holdings, and other Bloomberg-collected holdings); securities with ownership below 0% or above 100% are removed (`source-reported`, §3.3). ICB classification codes come from Bloomberg; sovereign CDS spreads from Datastream; the monthly Financial Stress Index of Duprey et al. (2017) enters the IV exercise via the **ECB Data Portal** (Table A.4 caption).
- **Treatment / control:** treatment = stocks traded in **Austria, Belgium, France, Greece, Italy, Spain**; control = **Denmark, Finland, Germany, Ireland, Netherlands, Norway, Poland, Portugal, Sweden, Switzerland, United Kingdom** (named in the Table 2/3/4 and Figure 2 captions). Bans were notified under Article 23 of the EU Short Selling Regulation: **Belgium, France, Spain effective 17 March 2020; Greece, Italy, Austria effective 18 March 2020**; extended after 15 April 2020 and **all lifted on 18 May 2020** (§3.1).
- **Estimation windows:** pre = **17 Feb – 16 Mar 2020**, post = **17 Mar – 15 Apr 2020** (one month each); robustness uses 17 Jan – 16 Mar 2020 and 17 Mar – 15 May 2020 (§3.1, §5.4).
- **Transaction cost / slippage treatment:** the paper proposes **no trading rule and no backtest**; bid-ask spreads are the *outcome* variable of the study, not a modelled execution cost. Any fee, spread-crossing, borrow or market-impact treatment for an implementable strategy is `not stated in source` and must not be read as zero.
- **Repository deduplication audit (2026-09-22, ripgrep across all `*.md` on `origin/main`):** zero hits for `2609.08881`, `The Double-Edged Sword of Short-Selling Bans`, `Della Corte`, `Rapanos`, `short-selling ban`, `short sale ban`, `Beber and Pagano`, `Reg SHO`, `Rule 201`. The single incidental match (`order-flow-matched-filter-normalization-investor-segmentation-2026-09-02.md`, line 108) only notes "regulatory short-sale restrictions" as a borrow assumption and cites a different source (arXiv:2512.18648). Adjacent regulatory/event records — `sp500-index-reconstitution-announcement-drift-decay-falsification-2026-09-13`, `sec-form-10-12b-spinoff-drift-decay-falsification-2026-09-13`, `earnings-announcement-premium-jump-risk-decay-falsification-2026-09-13` — are different events, mechanisms and source identities. No prior record normalises a short-sale-constraint event study or the institutional-ownership conditioning of its effects.
- Schema resolved from the canonical specification `[[quant/strategy-research-record-spec-v1]]` (`schema: strategy-research-record-v1`) and the repository README workflow contract, both re-read this run.

## Economic mechanism

### Source-reported

The paper extends Diamond and Verrecchia (1987) with a regulator who endogenously chooses whether to prohibit short sales in order to avert a sharp price decline, in a single-period economy of informed and noise investors who own the stock with probabilities `h_I` and `h_N`, trading against competitive market makers (`source-reported`, §2).

- **Hypothesis 1:** "Short-selling bans are more likely to be imposed by regulators in markets with low institutional ownership." The model's regulator acts only when `h_I²/h_N < 1` (§2.4).
- **Hypothesis 2:** "Under certain conditions (`h_I > h_N`), short-selling bans lead to a deterioration in liquidity; moreover, the higher the institutional ownership of a stock, the larger the increase in bid-ask spreads." Mechanism: once shorts are banned, the pool of possible sellers contains only existing holders, so a sell order is inferred to be more likely informed; the market maker shades the bid down and the spread widens. A Lemma states the spread rises if and only if `h_I/h_N > 1`; asks are unchanged because buying is not restricted (§2.3–2.4).
- **Hypothesis 3:** "Under certain conditions (`h_I² < h_N`), short-selling bans support the left tail of returns; moreover, the lower the institutional ownership of a stock, the higher this support." The model also predicts **no effect on mean return** and a **lower median return** (no-trade events hide negative news) (§2.4).
- Institutional ownership is used explicitly as an **imperfect proxy** for the share of informed stockholders, justified by Boehmer and Kelley (2009), Bai et al. (2016), Dávila and Parlatore (2023) (`source-reported`, §2.4).

### Research interpretation

Falsifiable mechanism in our own words (`research interpretation`): a **forced-flow constraint interacts with the informedness composition of the holder base**. Banning short sales removes the marginal informed seller's ability to express negative views, which (i) raises adverse-selection cost exactly where informed holders are concentrated → liquidity is paid for, and (ii) truncates the left tail exactly where informed holders are scarce → crash protection is obtained for free but only in noise-dominated names. The tradeable implication is **cross-sectional and conditional, not directional**: the paper's own evidence says the *average* price level is not supported, so a naive "buy the ban" event trade has no source-reported edge; any edge would have to come from the institutional-ownership spread (long/short or execution/liquidity provisioning across the IO terciles) after paying the documented widening in spreads. All of that operationalisation is ours, not the paper's.

## Signal

**The source specifies no entry rule, exit rule, holding period, sizing rule or portfolio construction — it is an event-study identification paper, not a strategy. The Signal section is therefore `underspecified` at source level, and everything concrete below is `research-proposed`.**

`source-reported` (fixed facts a researcher can build on):
- Event timestamp: national regulator notifications, **17 March 2020** (BE/FR/ES) and **18 March 2020** (GR/IT/AT); all bans lifted **18 May 2020** (§3.1). Timezone/intraday release convention of each notification: `not stated in source` (dates only; Appendix Table A.2 collects decision dates and regulator links).
- Estimation design: difference-in-differences, `Ban × Country` interaction, controls = firm size and sovereign CDS spread, stock and time (calendar date) fixed effects for the spread regressions, standard errors clustered by stock and time (Table 2, Table A.3); return regressions cluster by stock (Tables 3–4).
- Cross-sectional conditioning variable: December-2019 Bloomberg institutional ownership, split at **bottom vs top tercile** (Tables 2 and 4).

`research-proposed` operationalisation (for future falsification only, not claimed by the source):
- **Formation timestamp:** at the publicly announced ban notification of a treated country's regulator; trade no earlier than the next venue session open to avoid using intraday information the paper never timestamps.
- **Universe:** same sample construction as the paper (drop micro/nano caps below USD 250m, drop negative-spread prints), point-in-time market cap and ICB industry.
- **Cross-sectional sort:** rank treated-country stocks by the most recent available institutional-ownership snapshot **before** the event (the paper uses Dec-2019; a live version must use only holdings already public at that date).
- **Candidate leg A (liquidity-cost avoidance / tilt):** underweight or hedge the **high-IO** tercile of treated names during the ban window (source-reported cost: spreads widen there by roughly 23–29 bp).
- **Candidate leg B (tail truncation / option-overlay):** in the **low-IO** tercile of treated names, reduce crash-hedge cost during the ban window (source-reported benefit: drawdown wedge ≈ 4.3 pp in Table 4 Panel A).
- **Exit:** on the ban-lift date (18 May 2020 in this episode) or at a fixed horizon; precedence between the two is `research-proposed`, not source-specified.
- **Position sizing, stop, slippage, borrow and cost model:** `research-proposed` / not specified anywhere in the source; the paper reports no portfolio returns at all.

## Required data

- **Instrument / universe:** individual equities listed on the 17 named European markets; exclude micro/nano caps (< USD 250m); keep small (USD 0.25–2bn), mid (2–10bn), large (≥ 10bn) caps (Table 1 definitions).
- **Venue / market type:** respective European cash equity trading venues; the bans covered cash **and** derivatives markets including ADRs and bearish intraday operations, with exemptions for market making, index instruments above country-specific thresholds (initially 20% for BE/GR/IT and 50% for FR/ES; a uniform 50% from 15 April 2020) and delta-neutral convertible-bond arbitrage (§3.1).
- **Fields:** daily bid and ask prices; daily total return indices; FX to USD; market capitalisation; ICB industry code; **institutional ownership percentage (Bloomberg, Dec-2019, point-in-time)**; sovereign CDS spreads; monthly log Financial Stress Index (Duprey et al. 2017, ECB Data Portal); firm volatility = standard deviation of daily returns over a 21-day rolling window (Table A.4 controls).
- **Timeframe:** daily, 2 Jan 2020 – 2 Jun 2020; pre/post windows as in Provenance.
- **Point-in-time:** institutional ownership is Dec-2019 (pre-event) — using a later ownership print would leak; ban dates are public regulator decisions; FX and CDS are same-database daily/monthly series.
- **Missing data:** source drops negative-spread observations and erroneous ownership prints (<0% or >100%); imputation is not described → treat as `not stated in source` beyond those two filters.

## Execution assumptions

- **Source-reported:** none — no order type, fill model, latency, participation cap, leverage, borrow or funding assumption appears anywhere in the paper. Spread widening is measured as an *outcome*, not as an execution model.
- **Source-reported fact that any implementation must internalise:** average bid-ask spreads in ban countries went from **0.72% (pre)** to **1.09% (post)** versus **0.62% → 0.87%** in non-ban countries (Figure 2 Panel A), i.e. quoted liquidity became materially more expensive precisely during the event window.
- **`research-proposed` (our assumptions, to be tested, not the source's):** crossing the quoted half-spread on treated names, one-session signal-to-order delay, no leverage, long-only or market-neutral variants, borrow assumed available for the short leg of an IO-spread construction, costs = observed spread + commission + a slippage buffer. Capacity: `not stated in source` (no volume or depth analysis is performed).

## Evidence

### Source-reported

All figures below are third-party claims from Della Corte, Kosowski, Papadimitriou and Rapanos (`arXiv:2609.08881v1`), with table/figure provenance; units are percentage points of the dependent variable (1 pp = 100 bp). None has been independently reproduced.

**Design-level facts**
- 17 markets, 1,922 stocks, >200k daily observations after filters (§3.2, Table 1). Largest samples: United Kingdom 448 stocks, France 225, Germany 209 (Table 1).

**Liquidity (Hypothesis 2)**
- **Figure 2 Panel A:** mean quoted spread in ban countries 0.72% → 1.09% (pre → post); in non-ban countries 0.62% → 0.87%; relative increase "more than 50%" vs "less than 40%".
- **Appendix Table A.3 (baseline DiD on % bid-ask spread):** `Ban × Country` = **0.116*** (SE 0.040), 0.130*** (0.044), 0.130*** (0.044), 0.120** (0.048) across specs 1–4 → treated-country spreads widened an extra **11.6–13.0 bp**; `Ban` time effect 0.247***/0.246***; stock and time fixed effects; **#obs 77,665–77,667**; R² up to 0.574. The Introduction summarises this as deterioration "by up to 13 basis points".
- **Appendix Table A.4 (IV):** instruments = lagged log Financial Stress Index and lagged monthly sovereign CDS (first stage: CDS 0.005***, FSI 0.263***, R² 0.618–0.620, #obs 207,382–207,418, Stock-Yogo/Kleibergen-Paap and Cragg-Donald diagnostics reported); second stage `Ban (estimated)` = **0.126**, **0.129**, **0.135** (i.e. ≈ 12.6–13.5 bp) with significance markers as printed in Table A.4 Panel B.
- **Table 2 Panel A (low-IO, bottom tercile):** `Ban × Country` = 0.079, 0.077, 0.079, 0.058 (SE 0.053–0.072) — **not significant at conventional levels** (≈ 6–8 bp).
- **Table 2 Panel B (high-IO, top tercile):** `Ban × Country` = **0.229***, **0.285***, **0.285***, **0.278*** (SE 0.066–0.083) — **significant at 1% in all four specs** (≈ 23–29 bp). *Note on wording:* the Introduction quotes "5–8 bp" (low IO) and "22–29 bp" (high IO) as ranges across specifications, while §4.3 quotes "8 bp" and "23–29 bp"; the table rows above are the printed per-column values.

**Returns and left tail (Hypothesis 3)** — dependent variables are percentage mean/median/volatility/maximum drawdown of USD total return indices over the one-month windows; SEs clustered by stock; controls = firm size + sovereign CDS (Table 3 caption).
- **Table 3, `Ban × Country`:** Mean **−0.073** (SE 0.070) and **−0.070** (0.070) — **insignificant**; Median **−0.224***** (0.060) and **−0.215***** (0.061); Volatility **−1.203***** (0.098) and **−1.262***** (0.103); Maximum drawdown **2.757***** (0.562) and **3.105***** (0.570).
- **Sign convention:** §4.4 states "the maximum drawdowns were 310 basis points higher … an increase in the maximum drawdown should be interpreted as support for the left tail", while the Introduction states bans "lower the maximum drawdown (in absolute terms) by 310 basis points". The two statements are consistent only if drawdown is carried as a signed (negative) quantity, so a positive coefficient = shallower drawdown. The paper does not print an explicit sign definition for the drawdown variable in the caption → recorded as a **data gap**; the magnitude (**≈ 276–311 bp** across specs 7–8) and the 1% significance are taken verbatim from Table 3 rows.
- **Table 4 Panel A (low institutional ownership, bottom tercile):** Mean **0.180** (0.117) n.s.; Median **−0.093** (0.106) n.s.; Volatility **−0.670***** (0.147); Maximum drawdown **4.300***** (0.987).
- **Table 4 Panel B (high institutional ownership, top tercile):** Mean **−0.091** (0.133) n.s.; Median **−0.291***** (0.107); Volatility **−1.021***** (0.184); Maximum drawdown **2.077*** (1.116). → the left-tail wedge is roughly **4.3 pp for low-IO names vs ≈ 2.1 pp for high-IO names**, i.e. Hypothesis 3's conditioning direction.
- **Figure 4:** cross-sectional average maximum drawdown (maximum cumulative peak-to-trough decline, expanding window 2 Jan – 16 Mar 2020 vs 17 Mar – 2 Jun 2020) similar pre-event across groups, less pronounced post-event in ban countries.
- **Figure 3 (Hypothesis 1):** average Dec-2019 stock-level institutional ownership is substantially lower in ban countries than elsewhere; the paper calls this **"suggestive evidence"**, not a causal test (§4.1).

**Robustness reported by the source**
- Tables 5–6: stocks matched on market cap and ICB industry → "no qualitative differences".
- Tables 7–8: placebo using only non-ban countries as pseudo-treated → estimates statistically and economically insignificant for spreads, means and maximum drawdowns (parallel-trend support).
- Appendix Tables A.12–A.13: two-month pre/post windows → "qualitatively and quantitatively similar".
- Appendix Table A.8: SEs clustered by stock and country-time → "qualitatively unchanged".
- Appendix Figure A.10: downside risk (volatility of negative daily returns) higher for untreated stocks post-shock; Appendix Figure A.11 matched-sample version "virtually identical".

### Independently reproduced

not independently reproduced.

### Negative evidence

- **No average-price support:** the mean-return DiD is −0.073/−0.070 bp-scale percentage points and **statistically insignificant** (Table 3 cols 1–2); median returns are **significantly lower** by ≈ 21.5–22.4 bp (cols 3–4). The source therefore rejects the popular "short bans lift prices" narrative in this episode (`source-reported`).
- **A real, quantified cost:** ≈ 11.6–13.0 bp additional spread widening (Table A.3), 12.6–13.5 bp under IV (Table A.4), and ≈ 23–29 bp for high-institutional-ownership names (Table 2 Panel B) — any strategy trading these names inside the window pays this, and it is concentrated exactly in the most informed names.
- **Documented by the source as consistent with prior literature:** Beber and Pagano (2013) find bans detrimental to liquidity, slow price discovery and no price support except US financial stocks; Bessler and Vendrasco (2021) confirm 2020 European bans harmed liquidity; Beber, Fabbri, Pagano and Simonelli (2021) find bans increase default probability and volatility; Boehmer, Jones and Zhang (2013) find liquidity worsened in all but the smallest US stocks in 2008; Battalio and Schultz (2011) find US option spreads rose in 2008; Marsh and Payne (2012) find a negative effect on UK market quality (all cited inside `arXiv:2609.08881v1` §1 — claims remain `source-reported` to that paper's literature review).
- **Identification limits acknowledged by the source:** ban timing is endogenous to deteriorating conditions (mitigated, not eliminated, by country-level macro IV); institutional ownership is an "imperfect proxy" for informedness; the model is static, single-asset and does not cover cross-asset/portfolio interactions or the lifting of bans; average spreads are used although spread *dynamics* may differ (§2.5).
- **Sample limits:** one quasi-synchronised episode (COVID, March 2020), six treated countries, one-month windows, 1,922 stocks; no capacity, volume, depth or turnover analysis; no portfolio returns.
- **None identified for:** whether the conditional left-tail effect survives an implementable long/short or overlay construction — the source never attempts one; absence is not evidence of no negative result.

## Falsification plan

All thresholds below are `research-defined falsification threshold`; all constructions are `research-proposed`.

1. **Independent replication of the DiD (mechanism):** rebuild Tables 2–4 on an immutable Datastream/Bloomberg-equivalent snapshot (or on a second ban episode such as the 2007–2009 or Rule-201 intraday episodes). *Fail if:* the `Ban × Country` coefficient on % bid-ask spread is ≤ 0 or its 95% CI includes 0 in the pooled sample, or if the high-IO minus low-IO spread effect is ≤ 0 (i.e. Table 2's conditioning direction does not reproduce).
2. **Left-tail conditioning test:** re-run Table 4 on the same windows with the drawdown sign convention explicitly reconstructed from raw price paths. *Fail if:* the low-IO drawdown wedge is not larger than the high-IO wedge, or if either loses significance at the 5% level after clustering by country-time.
3. **Placebo and pre-trend:** placebo event dates placed 30 and 60 trading days earlier, plus a two-sided event study on daily spreads. *Fail if:* placebo magnitudes reach ≥ 50% of the real-event coefficient or if pre-event leads are jointly significant.
4. **Proxy robustness:** replace Bloomberg total institutional ownership with a 13F-only or lagged-two-quarter measure. *Fail if:* the tercile split sign flips or the conditioning effect disappears (the mechanism rests entirely on this proxy).
5. **Cost stress on any tradable version (IO-spread or hedge-overlay construction):** charge the observed treated-name spread widening (stress: 13 bp baseline, 29 bp for high-IO names) plus commission and a 1-bp slippage buffer, at daily turnover implied by the chosen holding period. *Fail if:* net-of-cost cumulative PnL ≤ 0 or net Sharpe ≤ 0 on held-out episodes.
6. **Capacity/liquidity:** restrict to names with displayed depth above a pre-declared floor (e.g. USD 250k within 10 bp of touch, `research-defined`). *Fail if:* the effect is carried only by names below the floor.
7. **Competing explanation:** control for the simultaneous COVID policy response (PEPP announcement 18 Mar 2020, country fiscal packages) and for country-level volatility. *Fail if:* the ban coefficient collapses once these are absorbed, implying the "ban" proxy is picking up the macro shock rather than the constraint.
8. **Action on failure:** if tests 1–2 fail, retire the mechanism as non-replicated and keep only the liquidity-cost result as a caution; if test 5 fails, record the hypothesis as economically real but untradable after costs (the most likely outcome given the source's own numbers).

## Crypto portability

**Portability: `unproven`.**

- Crypto spot and perpetual markets have **no regulator-imposed short-selling ban**, so the source's event channel cannot be ported directly; an existing repository note (`leveraged-etf-closing-rebalance-predatory-trading-reversal-2026-09-03`) already records that the absence of short bans in crypto perps makes negative liquidity shocks more symmetric than in restricted cash-equity regimes.
- The *mechanism* (a binding constraint on expressive selling interacting with the informed-vs-noise composition of the holder base) is a `research-proposed` analogy to crypto-native constraint events — exchange position/leverage caps, funding-rate caps, withdrawal or listing suspensions, and lender-forced-cover events. **No source in this record supplies crypto evidence for any of those analogues.**
- Porting risks: 24/7 sessions with no regulator calendar (event timestamps become exchange-announcement timestamps with intraday precision that this paper never handles); venue fragmentation and different borrow/funding economics; no Bloomberg-equivalent institutional-ownership print — on-chain holder concentration is **not** the same object as informed ownership; stablecoin/quote-currency effects on USD conversion; and crypto venues lack the paper's quoted-spread data quality in thin books.
- Conclusion: crypto application is a **ported hypothesis, not crypto empirical evidence**, and is `unproven`.

## Limitations

- `underspecified` at source level: no trading rule, no entry/exit/holding/sizing rules, no capacity analysis, no cost model for an implementable strategy. Any Signal section content is `research-proposed`.
- `data gap`: the maximum-drawdown sign convention is described inconsistently between the Introduction ("lower … in absolute terms by 310 bp") and §4.4 ("310 basis points higher … interpreted as support"); magnitude and significance are verbatim from Table 3, the sign must be re-derived from raw paths before any use.
- `data gap`: no `Comments` (page count) and no `Journal reference` on the arXiv abs page as fetched 2026-09-22 → peer-review status `not stated in source`; license shown only as a generic arXiv license link.
- `data gap`: intraday timing of each regulator notification is not given (dates only); Appendix Table A.2 is referenced for decision dates but no release-time convention is stated.
- `not independently reproduced`: every coefficient, figure and robustness result is third-party.
- Identification: single episode, six treated countries, endogenous ban timing (IV uses country-level macro instruments only), matching on market cap and industry cannot rule out time-varying confounds; placebo design covers non-ban countries only.
- Proxy risk: institutional ownership is an acknowledged imperfect proxy for informedness; three countries (Switzerland, Germany, Denmark) show idiosyncrasies that the source discusses and dismisses qualitatively (§4.1).
- Publication-bias and generalisation risk: one crisis window; results are about *intermediate-period* outcomes while uncertainty is unresolved (source's own §2.5 caveat) and do not extend to payoff resolution.
- Incremental-write check: this is a new family (regulatory short-constraint event study with informedness conditioning) relative to the repository's existing event-study records; no prior record shares this mechanism, source identity or signal construction.

## Implementation status

`implementation_status: not-implemented`. Nothing has been implemented in our research stack: no data pipeline for European daily bid/ask plus Bloomberg institutional ownership, no DiD replication, no strategy prototype, no Qlib/candidate-pool entry, no Paper/Testnet/Live activity. This record is a normalised research capture only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this record does **not** mean it passed Research Intake Review, entered Hermes Wiki Brain, entered the production candidate pool, completed Qlib full-backtest validation, became a frozen survivor or leaderboard entry, or received Paper, Testnet or Live approval. Nothing here authorises trading; the paper itself reports no tradable return.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` — canonical schema contract used for this record (read this run; not a strategy claim).
- Repository neighbours (different mechanisms/sources, checked this run, no contradiction):
  - `sp500-index-reconstitution-announcement-drift-decay-falsification-2026-09-13.md` — equity forced-flow event study, index-rebalance mechanism rather than a short-constraint mechanism.
  - `sec-form-10-12b-spinoff-drift-decay-falsification-2026-09-13.md` and `earnings-announcement-premium-jump-risk-decay-falsification-2026-09-13.md` — other corporate-disclosure event studies.
  - `leveraged-etf-closing-rebalance-predatory-trading-reversal-2026-09-03.md` — records the absence of short-selling bans in crypto perps (relevant to the portability section).
  - `order-flow-matched-filter-normalization-investor-segmentation-2026-09-02.md` — mentions short-sale restrictions only as a borrow assumption; different source (arXiv:2512.18648).
- Future retrieval routes: search `short-selling ban`, `institutional ownership`, `left-tail support`, `bid-ask spread DiD`, `2609.08881`.

## Sources

1. Pasquale Della Corte, Robert Kosowski, Dimitris Papadimitriou, Nikolaos P. Rapanos. "The Double-Edged Sword of Short-Selling Bans." arXiv preprint `arXiv:2609.08881v1 [q-fin.TR]`, submitted 8 September 2026. Stable URL: https://arxiv.org/abs/2609.08881 · DOI: https://doi.org/10.48550/arXiv.2609.08881 · Full-text HTML read for this record: https://arxiv.org/html/2609.08881v1 (fetched 2026-09-22) · PDF: https://arxiv.org/pdf/2609.08881v1.
2. Works cited *inside* source 1 (claims attributed to source 1's literature review, not independently read): Diamond and Verrecchia (1987); Beber and Pagano (2013); Boehmer and Kelley (2009); Bai et al. (2016); Dávila and Parlatore (2023); Boehmer, Jones and Zhang (2013); Marsh and Payne (2012); Battalio and Schultz (2011); Bris, Goetzmann and Zhu (2007); Bessler and Vendrasco (2021); Beber, Fabbri, Pagano and Simonelli (2021); Dixon (2021); Brunnermeier and Oehmke (2014); Duprey et al. (2017); Geraci et al. (2018).
