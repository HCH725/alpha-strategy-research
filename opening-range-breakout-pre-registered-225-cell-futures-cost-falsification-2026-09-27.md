---
schema: strategy-research-record-v1
title: "Pre-Registered 225-Cell Falsification of Opening-Range Breakout on Nine US Futures at Realistic Costs (SSRN 7428398)"
created: 2026-09-27
updated: 2026-09-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - futures
  - intraday-breakout
  - pre-registration
  - transaction-costs
  - falsification
  - negative-evidence
status: research-only
confidence: medium
source_as_of: 2026-09-27
sources:
  - "Mulham Fetna, 'Opening-Range Breakout Does Not Survive Trading Costs: A Pre-Registered 225-Cell Study on Sixteen Years of Futures Data', SSRN 7428398, DOI 10.2139/ssrn.7428398, Date Written 07 Sep 2026, Posted/Last revised 14 Sep 2026, 9 pages. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7428398 (landing page read directly 2026-09-27)"
  - "github.com/mulhamfetna/trading-strategy-finder pinned at full commit d70580c510c1a1061925958085d9eb66cea9ed93 (2026-09-14T15:18:08Z) - README.md, docs/WS-ORB-PREREGISTRATION.md, docs/WS-ORB-REPORT.md, docs/WS-ORB-PRIOR-ART.md, subprojects/Parametric-Indicators/optimize/verify/claims_orb.py"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "SSRN abstract asserts that 'recent studies report triple-digit annual alphas for it on equity instruments', while the same programme's own pinned prior-art table (docs/WS-ORB-PRIOR-ART.md claims 2 and 3) records alpha of 33%/yr for QQQ and 47%/yr for TQQQ from Zarattini & Aziz 2023 (SSRN 4416622) and flags the vendor triple-digit-style performance claims as refuted (claim 9: 0-3). Both statements are recorded as printed; whether the abstract refers to an additional study outside the pinned prior-art table is not stated in source."
  - "SSRN landing page prints '0 References' while the pinned repository prior-art document enumerates nine verified prior-art sources (Zarattini & Aziz 2023 SSRN 4416622; Zarattini, Barbon & Aziz 2024 SSRN 4729284; Holmberg, Lonnbark & Lundstrom 2013 Finance Research Letters; Mesfin 2026 arXiv 2605.04004; the open QQQ replication; edgeful.com; crosstrade.io; QuantConnect). The paper's own reference list is therefore not visible from SSRN and is unreconciled."
---

# Pre-Registered 225-Cell Falsification of Opening-Range Breakout on Nine US Futures at Realistic Costs (SSRN 7428398)

## Provenance

### Paper (primary source A)

- **Title (SSRN landing heading, verbatim):** `Opening-Range Breakout Does Not Survive Trading Costs: A Pre-Registered 225-Cell Study on Sixteen Years of Futures Data`
- **Author list exactly as source:** `Mulham Fetna` (single author). Affiliation printed on the landing page: `BeInMedia (Nmo AI)`.
- **Stable URL:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7428398
- **DOI:** https://doi.org/10.2139/ssrn.7428398
- **Version / dates (all four expressions preserved, unreconciled):** `Date Written: September 07, 2026`; `Posted: 14 Sep 2026`; `Last revised: 14 Sep 2026`; Suggested Citation `... (September 07, 2026)`. No v1/v2 numbering is printed by SSRN.
- **Length:** `9 Pages`.
- **Publication status:** working paper on SSRN only. No journal, no issue, no peer-review statement anywhere on the landing page, and SSRN prints `0 References` / `0 Citations` -> peer-review status **not stated in source**.
- **Licence:** landing page carries a `Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)` badge.
- **Declarations printed on the landing page:** author is an employee of BeInMedia (Nmo AI), the software house that funded and hosted the research; internally funded by BeInMedia (Nmo AI), Kuwait City, Kuwait, which supplied infrastructure, computing and commercial market-data licensing; no external grants; no third party with a commercial interest influenced design, execution or reporting; historical market price data only, no human/animal subjects.
- **JEL:** G11, G14, C58.
- **Landing statistics observed 2026-09-27 (drifted during the session):** DOWNLOADS 157 -> 159 -> 160; ABSTRACT VIEWS 352 -> 353; `0 References`; `0 Citations`.
- **Read method:** the landing page was opened directly in a browser session on 2026-09-27 after a Cloudflare interstitial, and the full abstract, declarations, licence, JEL, citation block and statistics were read from the rendered page. **The SSRN PDF was not retrieved this run**: the `Delivery.cfm` endpoint returned the PDF once (HTTP 200, `application/pdf`, `content-length` 98001) but every subsequent request returned SSRN's registration/alert gate page (26,376 bytes of HTML), so paper-internal page, section and table numbering **cannot be verified from the PDF this run** -> data gap. Every paper-level number in this record therefore comes from the rendered abstract paragraph, and every methods-level detail comes from the pinned repository documents that the abstract itself names as the programme's evidence base ("All 79 published claims of the underlying research programme, including every number in this paper, re-derive offline from committed evidence by a public verification harness").

### Public verification repository (primary source B)

- **Repository URL:** https://github.com/mulhamfetna/trading-strategy-finder
- **Full commit SHA (pinned for this record):** `d70580c510c1a1061925958085d9eb66cea9ed93`
  - Commit date `2026-09-14T15:18:08Z`, message `Merge pull request #234 from mulhamfetna/dev`, default branch `main`.
  - Repository metadata read via GitHub REST on 2026-09-27: created `2026-05-13T16:57:44Z`, pushed `2026-09-14T15:18:08Z`, public, licence `AGPL-3.0`, 0 stars, 0 forks, 36 open issues, homepage `https://doi.org/10.5281/zenodo.21473312`.
  - README records the Zenodo version DOI `10.5281/zenodo.22229658` (v5.7.1) and the concept DOI `10.5281/zenodo.21473312`.
  - The README at this commit cites both SSRN preprints, including `Fetna, M. (2026). Opening-Range Breakout Does Not Survive Trading Costs ... https://doi.org/10.2139/ssrn.7428398`, which is the link binding source B to source A.
- **Exact file paths pinned at that commit, with git blob SHA and locally recomputed SHA-256 of the bytes fetched from `raw.githubusercontent.com` at that commit:**

| path | git blob SHA | bytes | SHA-256 of fetched bytes |
|---|---|---|---|
| `README.md` | `a2de32b4f0c46eeec4b5a727147882d8fae0275e` | 9,574 | `30836dc5c8a779d2d499bc9860ea80047aeca2981ca6747cfb2118212f4487f9` |
| `docs/WS-ORB-PREREGISTRATION.md` | `d9ac4f902a0fc817123fdd977fc6a2c466933800` | 7,949 | `89702ee3a94cdcfffc0add03c848b6f87ff896ad4878b3a2c151e4e5215383b6` |
| `docs/WS-ORB-REPORT.md` | `0c91a9f25bbb6fac3778856cfec4b7a56d3d6207` | 10,903 | `b57c3e0bcfade848e8da21b5b2a41e0d9ca2a7f1f05bddc42a38319675e15834` |
| `docs/WS-ORB-PRIOR-ART.md` | `9e69b927c563d9f45bd13f419d193101f7e04fac` | 6,122 | `69e7c655fcd92bd0a34cb81b058e7f3e8b24630ae153be38df4afe50a0c725b1` |
| `subprojects/Parametric-Indicators/optimize/verify/claims_orb.py` | `127631da591186f3c349dc2c0685d90260f5e35e` | 5,876 | `6f4d3dc1dc822c17849f583f2a64b4d1b88ed59eb02d9cccaf6d89523615d9f7` |

  The three `git blob SHA` values for `README.md`, `docs/WS-ORB-*` and `claims_orb.py` were read back from the GitHub git/trees and contents APIs at the pinned commit, not from the search index, and the `claims_orb.py` API `size` field (5876) matches the fetched byte count.

### Pre-registration integrity

`docs/WS-ORB-PREREGISTRATION.md` states it was **Filed 2026-08-23 BEFORE any run**, with the rule "Nothing below may be changed after a number has been seen; additions go in a dated Amendment section." The only post-filing addition inside the file is the dated `Pre-run note (2026-08-23, before any P/L) - anchor check result`. The report `docs/WS-ORB-REPORT.md` is dated 2026-08-23 and the repository commit that carries the SSRN citations is 2026-09-14. The git history of the pre-registration file was **not** walked line by line this run -> data gap (test F14 below is the gate for it).

### Pre-write source-identity deduplication (performed before writing, 2026-09-27)

`rg -uuu` over the **entire repository including all hidden paths** (`.mimo-worktrees/`, `.agents/`, `.hermes/`, `.git/`), not `git log`, for `7428398`, `7428478`, `mulham`, `fetna`, `trading-strategy-finder`, `BeInMedia`, `10.5281/zenodo.21473312`, `ORB-GRID-NO-POSITIVE-CELL` -> **exit 1, zero hits**. `coverage_manifest.csv` -> zero hits for the same tokens. A second pass for title fragments (`225-cell`, `Does Not Survive Trading Costs`, `Sixteen Years of Futures Data`, `18:00 ET Globex`, `random-anchor control`, `pre-registered...opening-range`) returned only one non-record local cache file (`.hermes/cache/apply-payload.json`, an intake payload, which itself contains none of the source-identity tokens) and no `*.md` record. `git log --oneline -20` was inspected as a convenience glance only; the latest main head at run time was `89d14a3` (`tradingview-cryptoscopeai-atr-band-ema-mtf-predictor-2026-09-27.md`), which is unrelated. **No existing record carries this source identity**, so no update-vs-create decision was required.

## Economic mechanism

### Source-reported

The paper's stated thesis (SSRN abstract, read 2026-09-27): opening-range breakout (ORB) is "among the most widely taught intraday strategies, and recent studies report triple-digit annual alphas for it on equity instruments"; the study tests "whether any simple, fully specified ORB variant survives realistic futures trading costs". The pinned prior-art document (`docs/WS-ORB-PRIOR-ART.md`) states what the programme believes is actually established: a canonical rule set from Zarattini & Aziz 2023 on QQQ (first 5-minute bar after the 09:30 cash open, enter at the open of the second bar in the first bar's direction, stop at the first bar's opposite extreme, target 10R or flat at the close, commission $0.0005/share, **no slippage modelled**), an in-sample result of +675% net over 2016-01 -> 2023-02 with alpha 33%/yr, a stocks-in-play variant from Zarattini, Barbon & Aziz 2024 on 7,000 US stocks reporting +1,637% with a 5-minute range judged best "reason unclear", an open replication showing gross edge of about 7 cents/share with net P/L crossing zero near 2.2 cents/share entry slippage, one negative index-futures test (Mesfin 2026, arXiv 2605.04004, MNQ), and one peer-reviewed daily-bar crude-oil volatility-threshold study (Holmberg, Lonnbark & Lundstrom 2013) whose edge is concentrated in the high-volatility 2001-2011 subperiod.

The source's own summary of its result (SSRN abstract): zero of 225 cells meet the pre-registered positive bar; the median gross edge is -0.01 ticks per trade; 155 of 225 cells sit within two ticks of zero, so "where the breakout earns anything, it earns it inside the spread"; the largest-dollar surviving cell fails a random-anchor control, "indicating volatility-expansion continuation rather than any information in the session open".

### Research interpretation

Falsifiable mechanism statement, stated as our interpretation rather than as a fact asserted by the source:

- **Primary hypothesis being tested (intraday momentum / breakout continuation anchored to a session-open boundary):** the first minute-level close outside a range formed at the opening of a traded session carries directional information because the open concentrates price discovery, overnight/between-session information arrival and liquidity provision, so the post-open drift continues past the range boundary far enough to pay the round-trip friction.
- **Component roles in the tested object:**
  - Regime/anchor: cash or pit session open (Arm A) versus the 18:00 ET Globex open (Arm B).
  - Primary signal: first 1-minute close beyond the opening-range high/low after the range window completes.
  - Risk/exit: one of three literature-sourced exit families (1R/10R classic, 10%-of-ATR14 stop, 50%-of-range target) plus flat at session close; a fourth volatility-threshold rule (Holmberg 2013) runs as a comparator row without any time window.
  - Cost lens: raw, $10/round-trip, $25/round-trip, with $25/round-trip as the headline cell value.
- **Rival mechanism the source pre-registers and tests (volatility expansion):** if the same range placed at a random minute of the same session earns the same amount, the edge belongs to generic volatility/range expansion rather than to the session open. The pre-registered control (Section 7 of the pre-registration: random-time range with the same N and rules, 20 seeded draws, real anchor must beat the control distribution's 95th percentile) is the discriminating test. The source reports the largest-dollar cell fails it.
- **Interpretation of the null:** the source concludes that ORB "as specified in the public literature is not a trading strategy on these markets at realistic costs", and that what survives - a weak NQ-only tendency for wide 60-minute range breakouts to continue, strongest in high volatility - "is not anchored to the open" and is the same phenomenon its own box strategy already trades. This is a **falsification of one operationalisation of an intraday momentum hypothesis on US index/metal/energy futures**, not a refutation of breakout or momentum mechanisms in general.

No component is assumed to contribute alpha; the source's own controls are the ablation.

## Signal

Everything in this section is **source-reported**, normalised from `docs/WS-ORB-PREREGISTRATION.md` Sections 1-7 at the pinned commit. Nothing here is Scout-generated; where the source leaves a field open it is marked as a gap rather than filled in.

- **Universe (nine instruments, source-reported):** `NQ ES GC SI HG CL NG RTY YM` - four equity indices, three metals, two energy, matching the abstract's "nine liquid U.S. futures markets (equity indices, metals, energy)". One contract always.
- **Arm A - cash/pit-session ORB anchors (source-reported):** 09:30 ET for NQ ES RTY YM; 08:20 ET for GC SI HG; 09:00 ET for CL NG. Session close for the flat rule: 16:00 ET indices; 13:30 ET GC SI; 13:00 ET HG; 14:30 ET CL NG.
- **Pre-run anchor check (source-reported, dated 2026-08-23, before any P/L):** median 1-minute volume by minute-of-day over 2018-2024, largest jump versus the previous 5 minutes inside 07:00-10:30. Confirmed 7/9: NQ 09:30 (x9.2), ES 09:30 (x9.7), RTY 09:30 (x15.7), YM 09:30 (x10.8), GC 08:20 (x3.0), CL 09:00 (x4.6), NG 09:00 (x4.2). **Moved by the pre-registered rule:** SI -> 07:00 (strongest step x5.3; 08:20 only x2.1; a possible DST-split London fix recorded as a blind spot); HG -> 09:00 (x3.6 versus 08:20 x1.1). Evidence path `optimize/orb/data/anchor_check.json`.
- **Arm B - Globex ORB anchor (source-reported):** 18:00 ET for all nine instruments (the engine's session boundary and 4-hour grid origin); flat at 16:59 ET next day; weekends/holidays follow the tape.
- **Opening-range window (source-reported):** N in {5, 15, 30, 60} minutes from the anchor, both arms. OR high/low = max/min of the N one-minute bars. A range is void if any of its bars is missing.
- **Entry (source-reported):** first 1-minute **close** beyond the OR high (long) or below the OR low (short) after the range completes; **fill at the next 1-minute open**; one trade per session per direction-side; the first breakout wins (no re-entry after a stop); no trade if both sides break on the same bar.
- **Exit rules (source-reported):**
  - `R1 classic` - stop at the opposite OR edge (1R), target 10R, flat at session close (attributed to Zarattini & Aziz 2023).
  - `R2 ATR-stop` - stop = 10% of the 14-day ATR from entry, no target, flat at close (attributed to Zarattini et al. 2024).
  - `R3 range-target` - stop at the opposite OR edge, target 50% of the range width (attributed to a practitioner ES rule).
  - `C1 vol-threshold comparator` - Holmberg 2013: no time window; enter when price crosses `(1 +/- rho) * open` with `rho = mu_hat + sigma_hat * q_0.95` from the trailing 60 sessions' open-to-close returns; flat at close. Runs only in Arm A. This is the 9-cell comparator arm.
- **Fill/precedence rules (source-reported):** stops and targets follow the engine gap rule GAP-01/02 - if the 1-minute bar gaps through the line, fill at that bar's **open**, not at the line; stops and targets are evaluated on bar high/low; if both are touched in the same bar the **stop** is assumed first (worst case).
- **Grid size (source-reported):** 9 instruments x 2 arms x 4 windows x 3 rules = 216 cells, plus 9 comparator cells = **225 cells**. The arithmetic checks out against the abstract.
- **Windows (source-reported):** exploration 2010-06-06 -> 2017-12-31 (sign check); confirmation 2018-01-01 -> 2024-12-31 (verdict window); fresh/reserve 2025-01-01 -> 2026-08-07 (reported; the only window untouched by prior in-house work).
- **Verdict rules (source-reported, fixed before any run):** POSITIVE on the confirmation window at $25/round-trip requires mean net P/L per trade > 0 with `t >= 2.5` (Bonferroni across the 12 cells of that instrument-arm, alpha = 0.05/12), exploration-window sign agreement, at least 60% of calendar years positive with no single year above 50% of the total, a leave-one-year-out minimum still above 0, both dumb controls null, and the noise check passed. NEGATIVE requires the minimum detectable effect (80% power, two-sided 5%) to be at or below the instrument's $25 friction per trade. Otherwise UNDERPOWERED, or NULL. "A cell's verdict is final; no rule or window may be added to rescue it."
- **Controls (source-reported):** dumb control 1 = random-time range at a uniformly random minute of the same session, 20 seeded draws, real anchor must beat the control distribution's 95th percentile; dumb control 2 = direction shuffle on a random 50% of days, 20 draws, real must beat p95; noise check = per-cell block bootstrap by session, 1,000 resamples, 95% CI of the net mean, POSITIVE requires the CI to exclude zero; vol-subsumption check = regress daily cell P/L on the deployed FU-14 power forecast and on trailing 20-day realised vol, report variance explained and the net mean within the top/bottom vol tercile, with an edge living only in the top tercile recorded as "volatility exposure, not ORB".
- **Position sizing / leverage:** fixed one contract, no fitting, no compounding rule stated -> sizing beyond "1 contract always" is **not stated in source**.
- **Fully specified or underspecified:** the entry, exit, window, anchor, fill and verdict rules are fully specified in the pinned pre-registration. The commission/fee/spread decomposition behind the $25 round-trip figure is **underspecified** (see Execution assumptions), and the paper's own section/table numbering is **data gap** this run.

## Required data

- **Instrument / universe:** continuous contracts for NQ, ES, GC, SI, HG, CL, NG, RTY, YM (CME/CME-group US futures; the venue/exchange name itself is **not stated in source** - the pre-registration only says "server 16-year tape").
- **Market type:** exchange-traded futures, single-liquid-contract-per-symbol continuous series.
- **Timeframe:** 1-minute bars (the underlying tape is 1-second/1-minute and licensed; see below).
- **Sample:** 2010-06-06 -> 2026-08-07 (the abstract compresses this to "sixteen years of one-minute data (2010-2026)"), split into the fixed exploration / confirmation / fresh windows above.
- **Fields required:** 1-minute OHLCV; minute-of-day label (ET-naive, bars labelled by start); continuous-contract splice/roll flags; 14-day ATR (R2); 60 sessions of open-to-close returns (C1); point values from `optimize/instruments.py` - NQ 20, ES 50, GC 100, SI 5,000, HG 25,000, CL 1,000, NG 10,000, RTY 50, YM 5 (dollars per full-point move); tick sizes (referenced for the "gross edge in ticks" output, values per instrument **not printed in the pinned files** -> data gap); median 1-minute volume by minute-of-day for the anchor check (2018-2024); the deployed FU-14 power forecast and trailing 20-day realised vol for the vol-subsumption regression.
- **Point-in-time / look-ahead:** the study fits no parameters, so train/test leakage through fitting is structurally absent; the windows were fixed in the pre-registration before any run. The anchor check ran before any P/L was computed. The reserve window (2025-01-01 -> 2026-08-07) overlaps the programme's own box-champion selection data, which the pre-registration declares as blind spot 5 and calls irrelevant for ORB parameters (none are fitted).
- **Timestamp / timezone:** Eastern-time-naive labelling; session boundaries in ET; the DST question is raised only for the SI 07:00 anchor. Clock source, precision and out-of-order handling are **not stated in source**.
- **Missing-data policy:** a range is void if any of its bars is missing; otherwise null/stale/suspended handling is **not stated in source** -> data gap.
- **Funding/fee/spread needs:** the only cost inputs are the flat $10 and $25 per round-trip rungs (see below). Exchange fees, clearing, commission, borrow and financing are **not stated in source**.
- **Availability for independent recomputation:** the 1-second/1-minute tape is licensed and lives only on the compute server (`docs/DATA-AND-KNOWLEDGE-MAP.md`); price data is gitignored. The README explicitly splits reproducibility into Tier 1 ("every published number re-derives from committed evidence - anyone, offline") and Tier 2 ("recomputing the evidence from raw prices - server-only"). This record is Tier-1 only -> Tier 2 is a data gap.

## Execution assumptions

Determined from a Methods-level read of the pinned pre-registration Sections 1-8, the pinned report Sections 1-7 and the pinned claims file `claims_orb.py`, plus the SSRN abstract. The SSRN PDF itself could not be opened this run, so anything unique to the paper body is marked as a gap rather than inferred.

- **Signal-to-order timing:** entry order is placed on the 1-minute close that breaks the range and fills at the **next 1-minute open** (one bar of delay), source-reported.
- **Order type:** market-type fills at bar opens for entries; stop/target fills follow the gap rule (fill at the bar open if the bar gaps through the line), source-reported.
- **Fill model:** deterministic bar-based model with stop-first precedence when stop and target are touched in the same bar, explicitly described by the source as conservative by construction at 1-minute resolution (blind spot 3). Partial fills, queue position and order-book interactions are **not modelled / not stated in source** -> data gap.
- **Latency:** no latency model beyond the one-bar delay is **not stated in source** -> data gap.
- **Fees / commission / spread / slippage treatment:** the cost model is a **flat dollar amount per round trip**, reported in three rungs - raw, $10/round-trip, $25/round-trip - with $25/round-trip as the headline for every cell (pre-registration Section 5). The abstract calls this "realistic futures trading costs" but does not decompose it. There is **no explicit commission schedule, exchange/clearing fee schedule, bid-ask spread model, market-impact model, or slippage distribution anywhere in the pinned files** -> data gap, and this must not be read as "no costs modelled": costs are modelled, just not decomposed. The word scan requirement of the contract is satisfied by that statement: spread appears in the report only as an economic phrase ("earns it inside the spread", "the index with the tightest spread"), never as a priced input.
- **Market impact / capacity:** not modelled. The study trades exactly one contract, which is itself a capacity stance; no ADV or participation model is **not stated in source** -> data gap.
- **Leverage / margin / borrow:** one contract, unlevered at the account level, no margin or financing model -> not stated in source.
- **Position limits:** one trade per session per direction-side; no re-entry after a stop; no trade when both sides break on the same bar; source-reported.
- **Holding period:** intraday only - from the breakout to the exit rule or to the session close/flat rule (16:00 / 13:30 / 13:00 / 14:30 ET for Arm A, 16:59 ET next day for Arm B); source-reported.
- **Roll handling:** continuous-contract splice inside a session can fabricate or destroy a breakout on roll days; roll days are flagged but the with/without-roll table is **owed, not delivered** (blind spot 1) -> data gap.
- **Contract-specification drift:** tick sizes and session hours changed over the 16 years; today's values are used throughout (blind spot 4), source-declared.
- **What the source assumes vs what we assume:** everything above is source-reported. Any additional assumption a reader might need to trade this (venue, commission schedule, order type beyond bar-open, latency, capacity) is **research-proposed** if introduced by us; this record introduces none.

## Evidence

### Source-reported

**From the SSRN abstract (landing page read directly 2026-09-27; the paper PDF was not retrieved, so paper-internal table/section provenance for these figures is a data gap):**

- Grid: 225 cells = 9 futures markets x 2 session anchors x 4 opening-range lengths (5/15/30/60 minutes) x 3 exit rules from the literature, plus a volatility-threshold comparator.
- Sample: sixteen years of one-minute data (2010-2026), split into fixed exploration, confirmation and reserve windows.
- **Zero of 225 cells** meet the pre-registered positive bar (`t >= 2.5` at $25 per round-trip, sign agreement across sub-periods, year-by-year stability).
- Gross of costs the grid earns **+$1.57M** on the confirmation window; at $25 per round-trip it loses **-$6.49M**.
- Median gross edge **-0.01 ticks per trade**; **155 of 225 cells** have gross edge within two ticks of zero.
- **28 cells** are negative with statistical power.
- The 5-minute range - the literature's favourite - is the worst window.
- The largest-dollar surviving cell **fails a random-anchor control**, indicating volatility-expansion continuation rather than any information in the session open.
- All 79 published claims of the underlying research programme, including every number in the paper, re-derive offline from committed evidence by a public verification harness.

**From the pinned repository `docs/WS-ORB-REPORT.md` at commit `d70580c510c1a1061925958085d9eb66cea9ed93` (finer provenance than the abstract; Section references are to that file):**

- Report Section 2 table, confirmation window 2018-2024: all 225 cells sum to **-$6,485,272** at $25/round-trip against raw **+$1,565,353**; before costs 118 of 225 cells are positive.
- By rule at $25/rt: R1 1R/10R **-$1,688,718** (0% of cells powered-negative); R2 10%-ATR stop **-$1,883,026** (6%); R3 50%-range target **-$2,724,169** (**33%** powered-negative); C1 vol-threshold **-$189,360** (9 cells; 2 negative at t < -2.5, 7 under-powered).
- By window at $25/rt: 5 min **-$2,322,687** (28% powered-negative); 15 min -$1.71M; 30 min -$1.52M; 60 min -$0.74M (losses shrink as the range widens).
- By arm at $25/rt: cash open **-$3,702,559**; 18:00 Globex **-$2,782,714** (neither anchor is better).
- Report Section 3 verdict table: POSITIVE **0**; NEGATIVE (powered, MDE <= $25/trade) **28**; NEGATIVE (t <= -2) but under-powered **58**; UNDERPOWERED **138**; NULL **1** (CL cash 5-min R3). Median MDE of the grid **$51/trade**, range **$12-$654**.
- Powered-negative cells by instrument: HG 8, YM 4, GC 3, SI 3, NG 3, RTY 3, ES 2, CL 2, NQ 0.
- Report Section 4 instrument grids at $25/rt: NQ **+$548k** over 25 cells (17/25 positive, the only net-positive instrument); ES -$473k; GC -$960k; SI **-$1.40M** (1/25 cells positive after costs; worst cell in the grid, cash 5-min R3, t -6.8); HG -$1.19M (8 powered negatives); CL -$813k (18/25 cells positive before costs, 1 after); NG -$595k; RTY -$750k; YM -$856k.
- NQ detail: best cell cash 15-min R2 at **$47/trade on 1,800 trades, t 1.56, positive in all 7 years**, but -$27k in 2010-2017 (sign disagreement) and MDE $85; Globex 60-min R1 $73/trade (+$123k) and R2 $62/trade (+$106k) with 16-20 ticks gross edge, and **R1 fails the random-anchor control** (random 60-minute ranges earn up to $113/trade); vol terciles high $105-$120/trade, low $50-$84, mid $5-$25; fresh 2025-2026: Globex 60-min R2 +$57k, cash 15-min R2 +$4k, 5-minute cells lost.
- NG detail: the grid's top cell is NG Globex 60-min R3 at **$66/trade, t 1.78, 148 trades, 4/7 years**, beats random anchors, -$2.4k in 2010-2017, MDE $104 - "interesting, unproven ... and on so few trades that one more year decides it".
- Report Section 5 controls table (real $/trade vs random-anchor p95): NQ Globex 60 R1 **72.7 vs 113.4 -> does NOT beat**; NQ cash 15 R2 47.3 vs 30.4 -> beats; NG Globex 60 R3 66.1 vs 2.1 -> beats; NQ Globex 60 R2 62.4 vs 39.1 -> beats. Three of four beat random placement; **none clears the noise bar (t < 2)**; all four earn most in the top volatility tercile.
- Report Section 6 power arithmetic: a $25 effect against a $1,000+ per-trade standard deviation needs about 13,000 trades; a daily strategy gives 1,800 in seven years - so 138 cells are "not proven" rather than "proven absent".
- Report Section 0/6 conclusion: "ORB as defined in the literature is not a trading strategy on these markets at realistic costs"; what survives is "a weak, unproven, NQ-only tendency for wide (60-min) range breakouts to continue, which is the volatility-expansion effect the box strategy already trades."
- Claims ledger `ORB-GRID-NO-POSITIVE-CELL` (in `claims_orb.py`): three checks - V1 definitions held (6/6 synthetic tests, anchors confirmed/moved as prescribed, exactly 225 cells), V2 verdict table reproduces (28 / 58 / 138 / 1 and no POSITIVE, best cell `NG_globex_60_R3` at t = 1.781), V3 falsifier (the best NQ cell does not beat random-anchor p95 and all four control cells sit below t = 2.0). Report header records the claim as `71/71`.
- Provenance note: **every figure in this subsection is `source-reported` third-party output of Fetna / the BeInMedia research programme. None of it is our result.**

**Reported prior art used by the source (`docs/WS-ORB-PRIOR-ART.md`, claims 1-9 with the source's own confidence labels):** Zarattini & Aziz 2023 (SSRN 4416622) QQQ 2016-01 -> 2023-02 +675% net of commission versus buy-and-hold +169%, alpha 33%/yr (p = 0.0025), beta approx 0, Sharpe 1.12, 1,795 trades, 24% win rate, +0.13R/trade, TQQQ variant +1,484% / alpha 47% / Sharpe 1.18, single in-sample window, no OOS, authors hold a commercial day-trading-education interest; Zarattini, Barbon & Aziz 2024 (SSRN 4729284) 7,000 US stocks, filtered +1,637% / Sharpe 2.81 / MDD 12% versus unfiltered +29% / Sharpe 0.48, 5-minute range best "reason unclear"; open QQQ replication with gross edge about 7 cents/share, net crossing zero near 2.2 cents/share entry slippage and Sharpe 0.23 at 2 cents entry plus 4 cents stop slippage, 76% of filtered P/L from 2022 alone; Mesfin 2026 (arXiv 2605.04004) MNQ 09:30-09:55 range, 947 days 2021-12 -> 2025-08, 2-point round-trip friction, fails its own gate in all 5 variants, best long variant +2.82 pts/trade at T = 1.50 with 2024 (+7.04) masking 2022 (-1.42); Holmberg, Lonnbark & Lundstrom 2013 (Finance Research Letters) crude oil 1983-2011 daily OHLC, volatility-scaled threshold, zero costs, returns significantly > 0 but concentrated in 2001-2011. The source also lists refuted claims it refuses to re-cite (instrument-specific best windows, QuantConnect 1.5xATR figures, vendor ES stats, MNQ side-claims, circulated MDD figures).

### Independently reproduced

not independently reproduced (`Not independently reproduced.`)

This run performed only four read-only operations: (a) direct reading of the SSRN landing page in a browser session on 2026-09-27; (b) fetching the five pinned repository files from `raw.githubusercontent.com` at commit `d70580c510c1a1061925958085d9eb66cea9ed93` and recomputing their SHA-256 hashes, plus reading the matching git blob SHAs back from the GitHub git/trees and contents APIs; (c) arithmetic sanity checks on the source's own numbers (9 x 2 x 4 x 3 + 9 = 225; the rule/window/arm subtotals in report Section 2 sum to the printed grid total); (d) repository-wide ripgrep deduplication. **No backtest was run, no price data was downloaded, no claims-ledger replay (`python3 optimize/verify/run.py`) was executed, no test suite was run, and no figure was regenerated.** The verification harness itself is a claim by the source, not evidence produced here.

### Negative evidence

All items below are either reported by the source against its own thesis or structural limitations visible in the pinned files. Absence of a positive result is the finding; absence of an item here is not evidence that no other negative result exists.

1. Zero of 225 pre-registered cells meet the positive bar at $25/round-trip.
2. The grid sums to -$6,485,272 at $25/round-trip against +$1,565,353 gross - friction is the whole story and more.
3. 118 of 225 cells are positive before costs but only 39 after costs at $25/rt (report Section 0/2).
4. Median gross edge is -0.01 ticks per trade; 155 of 225 cells sit within two ticks of zero - the edge, where it exists, is smaller than the spread it must cross.
5. 28 cells are negative **with** power (a friction-sized edge would have been detected), so the null is not purely a power artefact for those cells.
6. The 5-minute window, the literature's favourite, is the worst of the four (-$2,322,687; 28% of its cells powered-negative).
7. The 50%-of-range target (R3), the practitioner rule, is the worst rule (-$2,724,169; 33% powered-negative).
8. Neither anchor works: cash open -$3,702,559, Globex -$2,782,714 - the hypothesis fails on both session definitions.
9. The largest-dollar cell in the grid (NQ Globex 60 R1, +$123k, $72.72/trade) **fails the random-anchor control**: random 60-minute ranges earn up to $113.40/trade, so the session open carries no information there.
10. All four controlled cells earn most in the top volatility tercile, and none clears the noise bar (t < 2) - the source's own pre-registered vol-subsumption reading is "volatility exposure, not ORB".
11. The best NQ cell (cash 15-min R2, +$47/trade, positive in all 7 confirmation years) reverses sign before 2018 (-$27k), failing the pre-registered exploration-window sign check.
12. The grid's top cell (NG Globex 60 R3, t 1.78) rests on 148 trades with MDE $104 - unproven by the source's own bar.
13. 138 of 225 cells are UNDERPOWERED (median MDE $51/trade, range $12-$654): "not proven" is not "proven absent", and 16 years of daily trades cannot resolve a per-trade effect below about $50 against $1,000+ per-trade noise.
14. SI is the grid's worst instrument (-$1.40M, 1/25 cells positive after costs, worst cell t -6.8), and its 07:00 anchor may be a DST artefact of a 12:00 London event.
15. HG carries the most powered negatives (8) and gross edges of -1.4 to +1.1 ticks; its $12.50 tick makes every ORB rule a spread-payer.
16. CL shows the purest "edge inside the spread" pattern: 18/25 cells positive before costs, 1 after.
17. ES, the index with the tightest spread, shows the smallest gross edge (best cell $13/trade, t 0.73, 1.7 ticks).
18. Continuous-contract roll days remain inside the trade books; the with/without-roll table is owed and not delivered (blind spot 1).
19. No pooling across instruments was pre-registered, so the grid-wide -$6.5M is explicitly descriptive, not a test.
20. Today's contract specifications (tick sizes, session hours) are used across all 16 years (blind spot 4).
21. 1-minute data cannot see intra-bar sequencing; the stop-first assumption is conservative by construction (blind spot 3).
22. The prior art's three warnings - edge inside the spread, year concentration, and the 5-minute optimum being an equities artefact - all reproduced on this data, which is corroboration of the failure modes rather than of any edge.
23. The source's own cited positive results are in-sample and uncorrected: Zarattini & Aziz 2023 is a single in-sample window with no out-of-sample test and a declared commercial interest; the open replication puts the QQQ net break-even at about 2.2 cents/share entry slippage and 76% of filtered P/L in 2022 alone.
24. The only prior index-futures test the source found (Mesfin 2026, arXiv 2605.04004) also fails its gate in all five variants, with one strong year masking the rest.
25. The source declares nothing verified exists for metals, energy (beyond daily-bar crude 2013), RTY/YM, or the 18:00 Globex open - i.e. the positive-evidence base for ORB outside equities is essentially empty before this study.
26. Structural: the cost model is a single flat dollar rung with no commission/fee/spread decomposition, so the headline -$6.49M is a scenario, not a measured cost.
27. Structurally: the licensed tape is server-only, so no outside party can reach Tier-2 recomputation today; Tier 1 depends on committed JSON/CSV evidence, which this run did not replay.
28. Employment and funding are concentrated in one software house (BeInMedia / Nmo AI), which the source declares openly; no third-party replication of this specific 225-cell grid was identified.

## Falsification plan

Items F1-F14 are **`research-defined` falsification thresholds**: our tests, not the source's, except where explicitly attributed. Data, sample/regime, metric, decision rule and action are stated for each. Nothing here is authorised to promote the record; a pass only leaves it `research-only`.

- **F1 - Frozen forward replication (source-attributed protocol, our threshold).** Data: the same 225 cells on the same 1-minute tape, extended from 2026-10-01 for at least 24 further months. Metric: number of cells meeting the original pre-registered POSITIVE bar at $25/round-trip. `research-defined` rule: **one or more POSITIVE cells** falsifies this record's "no viable ORB" conclusion; zero keeps it. Action: rewrite Evidence and Limitations either way.
- **F2 - Ledger reproduction gate.** Data: the committed evidence at `d70580c510c1a1061925958085d9eb66cea9ed93` (`optimize/orb/data/grid1/{orb_summary.json,verdicts.csv,controls_top.json}`, `anchor_check.json`). Metric: verdict counts and best-cell t. `research-defined` rule: fail if POSITIVE != 0, NEGATIVE != 28, negative-but-underpowered != 58, UNDERPOWERED != 138, NULL != 1, or best cell is not `NG_globex_60_R3` at t = 1.781 +/- 0.01. Action: withdraw or correct this record immediately.
- **F3 - Pre-registration integrity gate.** Data: git history of `docs/WS-ORB-PREREGISTRATION.md` and the first commit that introduces `optimize/orb/data/grid1/`. Metric: last-modified time of the pre-registration versus first appearance of any P/L output. `research-defined` rule: **any edit to the pre-registration after the first P/L output** (other than the dated 2026-08-23 pre-run anchor note) voids the "pre-registered" claim and downgrades the whole record to an ordinary in-sample backtest. Action: restate Provenance and contested flags.
- **F4 - Cost decomposition completion.** Data: same trade books. Metric: per-cell net P/L under an explicit model of exchange fee + clearing + commission + half-spread + impact, replacing the flat $25/round-trip. `research-defined` rule: if the sign of the grid-wide sum flips to positive at any cost rung between 0 and $25/round-trip, the "friction is the whole story" reading is falsified. Action: restate the mechanism interpretation.
- **F5 - Roll-day audit (the source's own owed table).** Data: the same books with roll-day sessions removed and, separately, only roll days kept. Metric: cell-level verdict-class agreement. `research-defined` rule: if more than 10% of the 225 cells change verdict class, the verdict table is unstable and this record must be marked `underspecified` on that axis. Action: add a contradiction entry.
- **F6 - Anchor validity on independent data.** Data: a second vendor's minute-of-day volume profile for 2018-2024. Metric: the anchor minute selected per instrument. `research-defined` rule: if an independent profile resolves SI or HG differently from 07:00 / 09:00, or moves any of the 7 confirmed anchors, the Arm A results must be recomputed before the record is trusted. Action: restate Signal.
- **F7 - Random-anchor control with more draws.** Data: same cells, 100 (not 20) seeded random-anchor draws per controlled cell. Metric: real $/trade versus the control distribution's p95. `research-defined` rule: the claim "the open carries no information" survives only if NQ Globex 60 R1 **still fails** p95; if it beats p95 in 95 of 100 draws, that claim is falsified. Action: rewrite Economic mechanism.
- **F8 - Vol-subsumption ablation.** Data: daily cell P/L regressed on an independently rebuilt realised-vol forecast (not the deployed FU-14 model). Metric: share of variance explained and net mean by vol tercile. `research-defined` rule: if the top tercile does not dominate, weaken the "volatility exposure, not ORB" interpretation to an open question. Action: rewrite Evidence and Limitations.
- **F9 - Pooled / panel test.** Data: all 225 cells as a panel. Metric: pooled mean net P/L per trade at $25/rt with Newey-West t. `research-defined` rule: pooled `t >= 2.5` with the same sign in the exploration window would falsify the portfolio-level null even if every individual cell stays underpowered. Action: restate the conclusion scope.
- **F10 - Second-vendor replication.** Data: the full grid on an independent 1-minute vendor tape. Metric: cell-level verdict agreement. `research-defined` rule: below **90% agreement**, treat the verdict table as vendor-dependent and mark this record `data gap` on reproducibility. Action: add a contradiction entry.
- **F11 - Power upgrade.** Data: extend the sample until the median MDE of the grid falls to at or below $25/trade (the source estimates about 13,000 trades are needed). Metric: median MDE and the POSITIVE count. `research-defined` rule: if the extended, adequately powered sample yields any POSITIVE cell, the current "0 of 225" is a power artefact and the record's headline is falsified. Action: rewrite Evidence.
- **F12 - Multiplicity sensitivity.** Data: the 225-cell family. Metric: discoveries under Benjamini-Hochberg at `q < 0.10` versus the source's per-instrument Bonferroni (alpha = 0.05/12 within instrument-arm). `research-defined` rule: any BH discovery changes the verdict table and must be reported. Action: restate F1-F2 baselines.
- **F13 - Crypto port test.** Data: the same rule families on crypto perpetuals, with the session anchor chosen `research-proposed` (UTC 00:00 day boundary and a venue-local liquidity open), plus funding-inclusive costs mapped onto the $10 / $25 per round-trip rungs. Metric: POSITIVE count under the original bar. `research-defined` rule: one or more POSITIVE cells would move crypto portability from `unproven` to `adapted`; zero keeps `unproven`. Action: update the Crypto portability section only; this is not trading authorisation.
- **F14 - Cross-implementation consistency.** Data: a second, independent reimplementation of `orb_reference.py` semantics (gap-at-open fill, stop-first, void ranges, session map) against the six committed synthetic-session tests. Metric: per-cell net P/L agreement. `research-defined` rule: more than 1% of cells differing by more than one tick value in net P/L fails the reproduction gate. Action: mark the record `underspecified` on execution.

Action on any failure: correct or withdraw this record in place; **do not** promote it, and do not treat a passing falsification test as evidence of profitability or as approval for Paper, Testnet or Live.

## Crypto portability

**unproven.**

The source's evidence is entirely US index, metal and energy futures on a licensed 1-minute tape, with an explicit cash/pit-session and 18:00 ET Globex session structure. The source contains **zero crypto evidence**, so `direct` is unavailable and `adapted` would overstate the source. The mechanism is a ported hypothesis, not crypto empirical evidence.

Porting risks, concretely:

- **No universal session open:** crypto trades 24/7, so the treatment variable of this study - the session-open boundary - does not exist as a natural object. A UTC 00:00 day boundary, a venue-local listing/liquidity session, or a funding-settlement boundary are all possible anchors, and every one of them is `research-proposed` (see F13).
- **Funding:** perpetual funding is charged on a fixed schedule independent of the breakout, which the source's flat round-trip cost rung does not capture at all.
- **24/7 session structure:** the "flat at session close" exit has no counterpart; an intraday hold must be replaced by an explicit time exit, changing the rule family.
- **Venue fragmentation and liquidity:** nine single-name liquid futures with a documented tick size versus dozens of perp venues with different tick sizes, spreads and depth; the "gross edge in ticks" diagnostic does not transfer without a per-venue tick and spread model.
- **Mark / index price and contract specification:** continuous-contract splice and roll handling have an analog in perp index/spot basis and contract rolls, but the source's roll blind spot (F5) would be worse in crypto.
- **Liquidation / margin / leverage:** not modelled by the source for futures and not modeled for perps either -> data gap.
- **Adjacent repository evidence (different source identity):** `tradingview-hvp-triggered-opening-range-breakout-reversal-2026-09-16.md` records a crypto-adapted ORB that replaces the session open with a Historical Volatility Percentile trigger. That record is a public TradingView script proposal with no comparable falsification evidence, and it does not supply crypto evidence for this study's mechanism.

## Limitations

- **Not independently reproduced.** No backtest, no data, no ledger replay, no test suite was run by this Scout.
- **SSRN PDF not retrieved this run** (`data gap`): paper-internal page, section and table numbering, the printed reference list, and any body-text qualification of the abstract could not be read. Every paper-level figure in this record traces to the rendered SSRN abstract paragraph of 2026-09-27; methods detail traces to the pinned repository documents.
- **Cost decomposition is `underspecified`:** flat $10 and $25 per round-trip rungs only; no commission, exchange fee, clearing, spread, impact or latency model is printed anywhere in the pinned files. "Realistic" is the source's adjective, not a measured cost stack.
- **138 of 225 cells are UNDERPOWERED** by the source's own bar; the source is explicit that "not proven" is not "proven absent". The headline "zero of 225" therefore mixes 28 powered negatives with 138 non-results.
- **The grid-wide -$6.5M is descriptive**, not a test: no pooling across instruments was pre-registered.
- **Roll days unseparated** (`data gap`), **contract-specification drift unmodelled**, **1-minute bars hide intra-bar sequencing**, **SI anchor possibly a DST artefact** - all declared by the source as blind spots 1-5.
- **Tier-2 recomputation is server-only:** the 1-second/1-minute tape is licensed and gitignored; an outside reviewer can only replay committed evidence (Tier 1). This run did not even do that.
- **The verification harness claim (79 claims, 71/71 for ORB, `--selftest` rejecting 5 historical defects) is source-reported and unverified here** - it is a claim about the programme's own rigour, not independent evidence.
- **Concentration of funding, infrastructure and authorship in BeInMedia (Nmo AI)** is declared by the source; no third-party replication of this specific grid was identified (`unproven`).
- **Prior-art base is thin and partly refuted:** the source's own prior-art document refutes several circulating ORB performance claims (0-3 votes) and records the positive claims as single-window, no-out-of-sample, or equities-only.
- **`contested: true`** - two unreconciled items are recorded in the frontmatter: the abstract's "triple-digit annual alphas" versus the pinned prior-art alpha figures, and SSRN's printed `0 References` versus the nine enumerated prior-art sources.
- **Licence split:** the SSRN paper is CC BY-NC-ND 4.0 (non-commercial, no derivatives) while the GitHub repository is AGPL-3.0-or-later; they are different objects and both are recorded as printed. This record quotes and normalises rather than reproduces the paper.
- **Publication status:** SSRN working paper only; peer-review status **not stated in source**; `0 Citations` at read time.

## Implementation status

`implementation_status: not-implemented`.

No implementation in our research stack has been completed. This record was produced by a read-only Scout pass: landing-page reading, pinned-file retrieval and hashing, API provenance checks, arithmetic sanity checks and repository deduplication. **No Qlib full backtest, no Paper, no Testnet, no Live run has occurred for this hypothesis**, and none is implied. The source's own code (`optimize/orb/`, the verification harness, the six synthetic-session tests) was located and pinned but **not executed**.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

The presence of this record in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading.

This record is a **negative-evidence capture**. A falsification result is still research material: it does not authorise trading the surviving cells (NQ 60-minute wide-range continuation, NG Globex 60 R3), and it does not authorise trading ORB anywhere.

## Related Wiki records

Searched `wiki_brain` `kb_search` on 2026-09-27 before writing. The exact-mechanism query `opening-range breakout futures intraday falsification transaction costs` returned **zero pages**, so no existing Wiki page covers this source. The following verified adjacent pages were returned by `pre-registration backtest overfitting falsification futures` and are linked without fabrication:

- `[[quant/crypto-funding-carry-fade-turnover-cost-dissipation-falsification-2026-09-12]]` - pre-registered empirical falsification with a turnover/cost-dissipation framing; different asset class and mechanism.
- `[[quant/crypto-perpetual-order-flow-entropy-microstructure-taker-cost-falsification-2026-09-13]]` - taker-cost falsification on microstructure signals; different signal family.
- `[[quant/ml4t-p1-evidence-execution-truth-2026-09-04]]` - evidence/execution-truth gap distillation covering backtest overfitting and transaction costs.
- `[[quant/crypto-retail-systematic-trading-null-result-adversarial-audit-2026-09-01]]` - null-result anatomy; different market and different failure mode.

Adjacent records in **this repository** (different source identities, kept distinct on the four-axis rule):

- `tradingview-hvp-triggered-opening-range-breakout-reversal-2026-09-16.md` - same ORB family, but a public TradingView script (`kostastrovas`, published 2025-10-26) that **proposes** an HVP-triggered ORB variant adapted to 24/7 crypto. Distinct axes: source identity, universe (crypto vs US futures), signal construction (HVP trigger vs session-open anchor), and evidence class (proposal vs pre-registered falsification).
- `tradingview-orb-vwap-volume-candle-strength-2026-09-25.md` - same ORB family, public TradingView script (`luiscaballero`) that **adds** VWAP/volume/candle-strength confirmations to ORB. Distinct axes: source identity, mechanism (confirmation-filtered entry proposal vs multi-cell cost falsification), and evidence class.
- `mnq-intraday-ohlcv-signals-gross-edge-ceiling-falsification-2026-09-05.md` - arXiv 2605.04004 (Mesfin), which this source's own prior-art document cites as claim 7 (the only direct index-futures ORB test it found). Distinct axes: source identity, universe (MNQ only vs nine instruments), horizon (fixed 09:30-09:55 range vs four window lengths and two anchors), and construct (structural OHLCV-signal ceiling vs pre-registered ORB grid with controls).
- `mnq-vvg-day-classifier-directional-null-arxiv-2605.11423-2026-09-18.md` - same author family, different construct (day-type classifier).
- `spy-intraday-momentum-noise-area-band-vwap-stop-dynamic-sizing-2026-09-23.md` - SSRN 4824172 (Zarattini, Aziz, Barbon), overlapping author lineage with this source's cited prior art (SSRN 4416622 / 4729284) but a different paper, universe (SPY ETF vs futures) and mechanism (time-varying intraday-momentum bands vs ORB grid).

## Sources

1. Mulham Fetna. "Opening-Range Breakout Does Not Survive Trading Costs: A Pre-Registered 225-Cell Study on Sixteen Years of Futures Data." SSRN working paper, Date Written September 07, 2026; Posted 14 Sep 2026; Last revised 14 Sep 2026; 9 pages; JEL G11, G14, C58; licence CC BY-NC-ND 4.0. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7428398 ; DOI https://doi.org/10.2139/ssrn.7428398 . Landing page read directly in a browser session on 2026-09-27 (title, author line, affiliation, four date expressions, full abstract, keywords, licence, funding and employment declarations, JEL, suggested citation, `0 References`, `0 Citations`, 160 downloads / 353 abstract views at last observation). **PDF not retrieved this run - SSRN delivery returned a registration gate; paper-internal section/table provenance is a data gap.**
2. Mulham Fetna / BeInMedia (Nmo AI). `trading-strategy-finder` public verification repository, pinned at full commit **`d70580c510c1a1061925958085d9eb66cea9ed93`** (2026-09-14T15:18:08Z, `Merge pull request #234 from mulhamfetna/dev`), https://github.com/mulhamfetna/trading-strategy-finder . Files read at that commit: `README.md` (blob `a2de32b4f0c46eeec4b5a727147882d8fae0275e`, SHA-256 `30836dc5...f4487f9`), `docs/WS-ORB-PREREGISTRATION.md` (blob `d9ac4f902a0fc817123fdd977fc6a2c466933800`, SHA-256 `89702ee3...15383b6`), `docs/WS-ORB-REPORT.md` (blob `0c91a9f25bbb6fac3778856cfec4b7a56d3d6207`, SHA-256 `b57c3e0b...75e15834`), `docs/WS-ORB-PRIOR-ART.md` (blob `9e69b927c563d9f45bd13f419d193101f7e04fac`, SHA-256 `69e7c655...0c725b1`), `subprojects/Parametric-Indicators/optimize/verify/claims_orb.py` (blob `127631da591186f3c349dc2c0685d90260f5e35e`, size 5876, SHA-256 `6f4d3dc1...15d9f7`). Repository metadata (created, pushed, licence, stars, forks, issues, Zenodo DOI `10.5281/zenodo.21473312`, version DOI `10.5281/zenodo.22229658`) read via the GitHub REST API on 2026-09-27.
3. Prior-art sources **as enumerated inside** source 2's `docs/WS-ORB-PRIOR-ART.md` (not opened independently this run, and therefore reported at one further remove): Zarattini & Aziz 2023, SSRN 4416622; Zarattini, Barbon & Aziz 2024, SSRN 4729284; Holmberg, Lonnbark & Lundstrom 2013, *Finance Research Letters*; Mesfin 2026, arXiv 2605.04004 (already captured in this repository as `mnq-intraday-ohlcv-signals-gross-edge-ceiling-falsification-2026-09-05.md`); the open QQQ replication (`github.com/giovannibrusco/zarattini-2023-orb-qqq`); edgeful.com; crosstrade.io; QuantConnect. Each is labelled with the source's own confidence vote.
