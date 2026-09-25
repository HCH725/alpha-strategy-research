---
schema: strategy-research-record-v1
title: "Disclosed Human-Capital Disruption and Firm-Specific Risk: Earnings-Call Workforce-Disruption Score as a 21/42/63-Trading-Day Idiosyncratic-Volatility State Forecast (US Equities)"
created: 2026-09-25
updated: 2026-09-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-08-14
sources:
  - https://arxiv.org/abs/2608.14859
  - https://arxiv.org/html/2608.14859v1
  - https://doi.org/10.48550/arXiv.2608.14859
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Disclosed Human-Capital Disruption and Firm-Specific Risk: Earnings-Call Workforce-Disruption Score as a 21/42/63-Trading-Day Idiosyncratic-Volatility State Forecast (US Equities)

## Provenance

- **Primary source (the only source used for every number below):** arXiv `2608.14859`, **Ang Zhang** (sole author), *Disclosed Human-Capital Disruption and Firm-Specific Risk*, title-block affiliation **Lindner College of Business, University of Cincinnati**, title-block date line `July 2026`.
- **Author list exactly as source:** exactly one author, `Ang Zhang` (abs page `Authors: Ang Zhang`; title block prints `Ang Zhang` alone above the affiliation line). No co-author, no corresponding-author footnote, no email address appears in the pinned text → `data gap`.
- **Landing / version:** `https://arxiv.org/abs/2608.14859`, **arXiv v1, submitted Fri 14 Aug 2026 19:54:33 UTC (91 KB)**, submission history shows `[v1]` only; `https://arxiv.org/abs/2608.14859v2` returns **HTTP 404** (checked 2026-09-25) → sole version `v1`. Primary category **`Statistical Finance (q-fin.ST)`, no cross-list**. arXiv comment field = `50 pages`. **No `journal-ref` element in the landing page (grep count 0), no publisher DOI beyond the DataCite arXiv DOI, no peer-review statement** → **preprint only**.
- **License (read from the pinned HTML header):** `License: arXiv.org perpetual non-exclusive license` → **not Creative Commons**, therefore the text is cited and normalized rather than reproduced.
- **DataCite DOI:** `10.48550/arXiv.2608.14859` → **HTTP 302 → `https://arxiv.org/abs/2608.14859`** (checked 2026-09-25); it is the arXiv auto-DOI, not a journal DOI.
- **Primary-source checksum (performed 2026-09-25):** pinned HTML `https://arxiv.org/html/2608.14859v1`, **HTTP 200, 511,256 bytes, SHA-256 `70f09d916a94d803b603a9471ca9b07fcee73825baa71bc121af1d95f41ba1c8`**, converted to **122,246 characters / 4,333 lines and read end to end** (Abstract, §1–§9, Appendices A–I, Tables 1–23, Figures 1–5 captions, References). Every field below is either anchored to a section/table of that pinned text or explicitly marked as a gap. Rendering note: the LaTeXML header prints `Document created on July 2026`, later than the 14 Aug 2026 v1 stamp → treated as a conversion artifact, not a version.
- **Code / data availability:** **no code, no GitHub, no replication package and no data-availability statement anywhere in the pinned text** (word scan: `available upon request` 0, `open source` 0, `github` 0 in body, `upon request` 0; the only `replicat*` hit is the phrase `replication of HHQ's outcome design`) → **`data gap`**.
- **Sample period:** corpus of transcripts dated **13 Oct 2005 – 15 May 2025** (§3.1); **annual analysis = fiscal years 2006–2024** (partial 2005 and 2025 boundaries excluded, §3.1); **call-timed analysis capped at calls dated ≤ 31 Dec 2024** so the 2025 CRSP extension can complete forward windows (§3.3); CRSP daily/monthly returns run **through 31 Dec 2025** (§3.2); Execucomp CEO-exit intervals use **calls from 2008–2024** (§3.4).
- **Universe:** initial Compustat `302,028` industrial, consolidated, domestic, standard-format firm-years → `13,705` firm-years with ≥1 linked call (2,872 firms) → **main annual sample FY2006–FY2024 = `13,201` firm-years, `2,870` firms** (Table 1 Panel A). Call-level forward-risk sample = **`44,799` calls**, of which `44,798` link to daily CRSP returns (§3.3). Regression samples: annual idio vol `12,114` obs / `2,315` firms; annual downside & worst-month `11,851` / `2,209`; 42-day call panel `41,787` / `2,527` (restricted `38,357` / `2,389`); 16-block dynamic path `41,559` / `2,510`; CEO-exit intervals `27,691` / `1,411` firms / `715` exits. **No liquidity, size, price or exchange filter is stated** → `underspecified`.
- **Data vendors named by the source:** two public transcript archives — `TPotterer (2023)` (18,755 Motley Fool calls, 2017–2023, concentrated 2019–2022) and `Kurry (2025)` (33,362 calls for S&P 500 constituents and other large U.S. firms, 2005–2025) → combined `49,968` calls, deduplicated to `45,725` linked calls (§3.1); **CRSP** (daily/monthly returns to 2025-12-31); **Compustat / Compustat Quarterly**; **Fama–French daily market, size, value and risk-free factors** (Fama & French 1993); **Execucomp** (`BECAMECEO`, `LEFTOFC`, named-executive rosters); **Harford, He and Qiu (2026)** released labor-shortage files (`39,291` annual firm-years, `138,159` call-quarters); `all-mpnet-base-v2` sentence embeddings; three `microsoft/deberta-v3-base` fine-tunes; labels produced by `Claude Opus 4.8` (§4.3).
- **Transaction-cost treatment (Methods-level read of §3 Data, §4 Measurement, §6 Baseline, §7 Dynamic, §8 Robustness, plus a word-boundary scan of the pinned text):** `transaction cost` **0**, `trading cost` **0**, `slippage` **0**, `bid-ask` **0**, `commission` **0** (all three literal `commission` hits are the citation `U.S. Securities and Exchange Commission`), `fee` **0**, `spread` **0**, `borrow` **0**, `short sell` **0**, `hedge` **0**, `rebalance` **0**, `market timing` **0**, `Sharpe` **0**, `backtest` **0**, `alpha` **0**, `quintile` **0**, `trade` **0**, `tradable` **0**, `invest` **0**, `position` **0**, `order` **0**, `long` **0**, `short` **2** (non-trading prose), `portfolio` **1** (only inside the reference title *private meetings with portfolio firms*), `turnover` **22** (all executive/employee or reference context), `decile` **2** (Spearman / top-decile Jaccard **rank-stability of scores**, not portfolios). → **There is no cost, fill, borrow, capacity, turnover, sizing or P&L model of any kind in the source. Every cost/fill/turnover/capacity/P&L field below is `data gap`, never zero, and nothing in this record is net of cost.**
- **Source/data as-of:** source as-of = arXiv v1, **2026-08-14**; data as-of = **CRSP through 2025-12-31**, annual outcomes through **FY2024**, call-timed outcomes through calls dated **2024-12-31**.
- **Dedup (performed before writing, across the whole repository, hidden directories included):** `find . -name '*.md'` → **2,530 `*.md` files** including `.mimo-worktrees/`, `.agents/`, `.hermes/`, plus `coverage_manifest.csv` (**5,808 lines**). Ripgrep for `2608.14859` (**0**), `Disclosed Human-Capital Disruption` (**0**), `human-capital disruption` case-insensitive (**0**), `Lindner College of Business` (**0**), `HCDisruption` (**0**), `Harford.*He.*Qiu` (**0**), `deberta-v3-base` (**0**), case-sensitive word-boundary `Ang Zhang` (**0**; the 16 case-insensitive filename hits are all `…ang Zhang` surname collisions such as `Jack Yuxiang Zhang`, cleared by context), and `coverage_manifest.csv` for the arXiv ID and exact title (**0**). `all-mpnet-base-v2` hits 3 files, inspected as unrelated embedding-provenance mentions. Filename absent. **Zero exact source-identity hits before and after the write.** New source identity **and** materially distinct mechanism (workforce-disruption construct → forward firm-specific **volatility state**, not a sentiment or return signal) ⇒ not a duplicate.

## Economic mechanism

### Source-reported

The author's stated rationale (§1, §2.2, §2.4): human capital is a productive input and a repository of firm-specific knowledge, but headcount and labor expense record quantities only after the fact. A **material condition or action that constrains, reprices, interrupts or reorganizes the reporting firm's workforce** — labor shortages, skill constraints, attrition and retention pressure, wage/labor-cost pressure, safety and continuity problems, workforce restructuring, consequential leadership transitions — makes the ability to execute a given operating plan less certain, which should widen the distribution of firm outcomes. Four stated predictions (§2.4): (1) disruption is positively related to firm-specific risk and **not** to market beta; (2) the relation is stronger where labor is a more important production input; (3) the signal carries information beyond broad workforce salience and explicit shortage language; (4) risk elevated on **both** sides of the call **without a discontinuity** would characterize a persistent organizational condition rather than a disclosure-date shock. The source explicitly frames the construct as **broader than labor-shortage exposure and narrower than general workforce discussion**, and explicitly *not* a sentiment measure (§4.1): an excerpt stays positive even when management describes a costly workforce adjustment optimistically.

### Research interpretation

Falsifiable statement of the hypothesis we would test: **the call-level disruption score is a text-based proxy for a persistent single-name risk state, and — conditioning on the same firm's realized pre-call risk — a higher score forecasts higher Fama–French three-factor residual (idiosyncratic) volatility over the next 21/42/63 trading days.** Component roles, per README hybrid structure:

```text
Signal:        HCDisruption call-level score (accepted disruption excerpts per 10,000 transcript words)
Baseline:      matched pre-call idiosyncratic-volatility block (the source's own conditioning variable)
Control:       HCExposure broad workforce-discussion frequency + strictly pre-call accounting controls
Regime filter: none specified by the source (none added by us)
Entry/exit:    none specified by the source — see `Signal` and `Execution assumptions`
Risk layer:    none specified by the source
```

The **market-friction channel we are actually betting on is not identified by the source.** A risk-state forecast is only monetizable through an instrument whose payoff is convex to, or directional in, single-name variance (options, variance swaps, a downside/short overlay, or a volatility-risk overlay on an existing book). The source contains **no return-direction evidence and no P&L model**; we therefore treat any implementation as `research-proposed` and treat the *cross-sectional level* implementation as contradicted by the source's own test (§6.3, see Negative evidence). A correlation between a text score and a residual-volatility measure is **not** by itself a mechanism for returns — the missing link (who is paid to bear the extra firm-specific variance, and through which contract) is `underspecified`.

## Signal

Everything in this section is read from the pinned v1; items marked **[research-proposed]** are ours, not the source's.

- **Formation timestamp:** the earnings-call date recorded in the transcript archive. **Event day = the first CRSP trading day on or after the call date**; the maximum realized gap is **4 calendar days** (§3.3). Call-level tests use calls dated **≤ 2024-12-31**.
- **Availability / tradability timestamp:** **`underspecified`.** The source uses two *retrospective* third-party archives (a 2017–2023 Motley Fool scrape and a 2005–2025 S&P 500/large-cap compilation) and **never states a transcript publication timestamp or publication lag**, so the point-in-time availability of the score is not established (§3.1, §8.3). **[research-proposed]** trade only after a transcript with a verifiable publication timestamp is available, and require the result to survive the F1 point-in-time reconstruction.
- **Lookback:** **none** for the call-level score (single call). Annual score: all calls in the half-open fiscal window `(Datadate_{i,t-1}, Datadate_{i,t}]`, numerator = accepted excerpts, denominator = transcript words (eq. 3). Warm-up: a firm-year needs ≥1 linked call; the annual idio-vol outcome needs ≥60 daily observations with the last return within 10 calendar days of the fiscal endpoint (§3.2).
- **Score construction (eq. 1–3, §4.2–§4.4), fully specified by the source:**
  1. **Vocabulary screen** — a workforce-term vocabulary identifies **1,835,450 sentences** in the combined corpus.
  2. **First-stage semantic screen** — `all-mpnet-base-v2` embeddings + a radial-basis SVM trained on **3,110 `Claude Opus 4.8`-labeled sentences**, threshold **0.65** selected on a separate **400-sentence review sample**, **precision 0.922 / recall 0.769** → retains **173,273 sentences across 36,159 calls**.
  3. **Classification unit** — the candidate sentence together with the immediately preceding and following sentences; accepted counts are attributed only to the candidate sentence (§4.2).
  4. **Disruption classifier** — **three** independently initialized `microsoft/deberta-v3-base` models fine-tuned on **729 labeled excerpts (274 disruptions)** and **averaged**; the primary threshold `T_P90` is chosen on a **separate 400-excerpt sample (219 positives)** to achieve **≥90% precision against the Opus labels**; an inclusive max-F1 threshold is the alternative. (Whether the 400-excerpt *evaluation* sample of §4.3 and the 400-excerpt *threshold-selection* sample of §4.3 are the same 400 excerpts is **`underspecified`**.)
  5. **Aggregation** — `HCDisruption_c = 10,000 × (# accepted excerpts) / Words_c`; `HCExposure_c = 10,000 × (# workforce-vocabulary sentences) / Words_c` (eq. 2), computed *before* the disruption classification and used as a control.
  6. **Standardization** — the score is standardized **within each estimation sample** (§3.6). **[research-proposed]** a tradable rule must replace this with an expanding/rolling standardization; sample-specific scaling is a look-ahead device.
- **Robustness definitions the source itself supplies (seven rules, §4.5 / Appendix D):** inclusive threshold, high-confidence threshold, ≥2-of-3 classifier agreement, all-3 agreement, exclusion of explicit labor-shortage passages, exclusion of leadership/succession passages, plus the baseline. Accepted excerpts move **−37% to +72%** while firm-year Spearman correlations with baseline stay in **0.889–0.914** (content-exclusion rules **>0.97**) (§5.2, Table 14).
- **Long entry:** **`not stated in source`** — the source constructs no portfolio and defines no position direction. **[research-proposed]** two candidate implementations, both untested: **(A)** at event day **+2**, initiate a 42-calendar-day single-name long-volatility/convexity position and exit at day **+43**; **(B)** weekly cross-sectional long-low-score / short-high-score on the standardized call-level score of calls in the trailing 5 sessions — **note (B) is directly contradicted by §6.3** (see Negative evidence).
- **Short entry:** **`not stated in source`**. **[research-proposed]** as the mirror leg of (B), subject to the same contradiction and to borrow availability, which the source never models.
- **Exit:** **`not stated in source`**. **[research-proposed]** fixed 42-trading-day horizon; the source's own window definitions (`+2 → +22`, `+23 → +43`, cumulative 42, 63) are the only timing rules available.
- **Holding period / re-entry:** **`not stated in source`**. The source does record that **97.9% of valid 42-day windows end before the next observed call versus only 30.3% of 63-day windows** (§3.3), which is the source's own evidence that a 42-day holding period respects the reporting cycle and a 63-day one does not.
- **Position sizing:** **`not stated in source`**; `data gap`.
- **Parameters:** all fixed by the source (thresholds 0.65 and `T_P90`, windows 21/42/63, ±2-day call buffer, 10,000-word normalization, 60-day / 10-month / 45-day availability rules). **No tuned trading parameter exists in the source.** Any threshold we add (e.g. score ≥ rolling median) is **[research-proposed]**.
- **Fully specified vs underspecified:** the **score** is reconstructable from the paper; the **trade** is `underspecified`/`not stated in source` in every operational dimension.

## Required data

- **Instrument / universe:** US-listed operating companies with earnings calls, Compustat industrial consolidated domestic standard-format, linked to CRSP through the CRSP/Compustat Merged link history with **date-specific ticker matching**; 2,870 firms (annual), 2,389–2,527 firms (call-level).
- **Venue / market type:** US equities (CRSP). **The source never names an exchange, ECN or data venue** → `not stated in source`.
- **Timeframe:** daily returns (risk outcomes), monthly returns (worst-month outcome), 21/42/**63-trading-day** call windows, fiscal-year annual aggregation.
- **Fields required:** CRSP daily and monthly returns (to 2025-12-31); Kenneth French daily MKT/SMB/HML/RF; Compustat fiscal dates and the control set (`log assets`, `Tobin's q`, `ROA`, book leverage, `cash/assets`, plus `sales`, `employment`, `capex`, `R&D`, `debt`, `equity`, industry codes); Compustat Quarterly report dates (used for point-in-time controls); Execucomp named-executive rosters and CEO spells (`BECAMECEO`, `LEFTOFC`); full earnings-call transcripts with ticker, call date, fiscal quarter/year and word counts; the Harford–He–Qiu (2026) released labor-shortage files (comparison only); SEC Item 5.02 filings (the pre-call leakage audit only).
- **Point-in-time:** accounting controls are handled strictly — **latest fiscal-Q4 report date strictly before the call**, same-day and future report dates excluded, fiscal statement no more than 550 days old (§3.3). **Transcript availability is not handled** — the archives are retrospective scrapes whose **coverage varies over time and tilts toward large public firms** (§8.3); no publication timestamp, no revision handling → **`data gap`**, this is the single largest leakage risk.
- **Timestamp / timezone:** call date is a calendar date, mapped to the first CRSP trading day on or after it; **timezone of the recorded call date is `not stated in source`**; out-of-order records are handled by deduplicating on (ticker, call date, quarter) and keeping the longer transcript (§3.1).
- **Missing-data:** transcripts < 500 characters excluded; duplicate (ticker, date) resolved to the longer record, then one record per linked firm-call date (26 alias rows removed); annual idio vol requires ≥60 daily observations and a last return within 10 calendar days of the fiscal endpoint; fiscal-year return requires ≥10 monthly observations, ≥300 days between first and last, and no endpoint gap > 45 days; ten call-covered firm-years with no valid CCM link at the fiscal endpoint **retain missing annual returns rather than borrowing another security's returns** (§3.2). Ratio variables and return-distribution outcomes winsorized at 1/99 percentiles (§3.6).
- **Funding / fee / spread needs:** **omitted entirely** — `data gap`, never treated as zero.

## Execution assumptions

**The source makes no execution assumption of any kind.** Signal-to-order timing, order type, fill model, latency, participation/ADV cap, position limits, leverage/margin, shorting/borrow availability, dividend treatment, fee/spread/slippage/impact model and failure handling are all `not stated in source` → `data gap`. Nothing in the source is net of cost; the source reports **no P&L, no Sharpe, no turnover, no drawdown and no capacity** figure anywhere (word scan above).

**[research-proposed] Execution layer we would impose for any test:**
- signal-to-order: score published at transcript availability → next session **open**, with a mandatory same-day no-trade rule if the transcript publication timestamp is unavailable (feeds F1);
- order: market-on-open for the directional tests; for the convexity test, use quoted two-sided option markets with size capped at **20% of the daily contract volume** (a cap the source never specifies);
- fill: next-bar/open fill with an explicit 0/5/10/20/30 bp per-side ladder plus a separate quoted-spread treatment (feeds F4/F5);
- borrow/shorting: single-name equity borrow is **not available in this repository's data plane** and is assumed unavailable by default (feeds F3 as an additional failure reason);
- latency, partial fills and halts: **not modelled** by us either → `data gap`.

## Evidence

### Source-reported

All figures below are **source-reported, gross of cost** (the source has no cost model), on **US equities**, and have **not been independently reproduced**. Anchors are to the pinned v1 HTML.

**Annual within-firm association — Table 3** (firm + fiscal-year fixed effects, broad-workforce control, `log assets`, `Tobin's q`, `ROA`, book leverage, `cash/assets`, firm-clustered SE, coefficient per within-sample SD):

| Outcome | Coefficient | t | N | Firms |
|---|---|---|---|---|
| Idiosyncratic volatility | 0.0055 (0.00545) | 3.43 | 12,114 | 2,315 |
| Downside deviation | 0.0058 (0.00584) | 3.92 | 11,851 | 2,209 |
| Worst monthly return | −0.0046 (−0.00459) | −3.75 | 11,851 | 2,209 |
| Market beta | −0.0014 | −0.37 | 12,114 | 2,315 |
| FF3 explanatory share | −0.0041 | −2.22 | 12,114 | 2,315 |

Source notes: returns are decimals, so 0.00545 ≈ **0.55 pp**; annualized idio-vol mean **0.318**, so the coefficient is **≈1.7% of the outcome mean** (§6.2).

**Call-timed forward risk — Table 5** (event day = first trading day ≥ call date; days 0/+1 excluded; controls = matched pre-call risk block, broad workforce exposure, strictly pre-call accounting controls, firm FE, outcome-window calendar-quarter FE; SEs two-way clustered by firm × outcome-window quarter; outcomes logged so coefficients are % differences per SD):

| Window | Outcome | Per SD | t | N | Firms |
|---|---|---|---|---|---|
| +2 → +22 | Idiosyncratic volatility | +0.54% | 2.14 | 41,559 | 2,510 |
| +2 → +22 | Downside deviation | +0.36% | 1.38 | 41,559 | 2,510 |
| +23 → +43 | Idiosyncratic volatility | +0.56% | 2.09 | 41,559 | 2,510 |
| +23 → +43 | Downside deviation | +0.62% | 2.30 | 41,559 | 2,510 |
| Cumulative 42 d, all calls | Idiosyncratic volatility | +0.49% | 2.18 | 41,787 | 2,527 |
| Cumulative 42 d, all calls | Downside deviation | +0.42% | 1.86 | 41,787 | 2,527 |
| 42 d ending before next call | Idiosyncratic volatility | +0.50% | 2.05 | 38,357 | 2,389 |
| 42 d ending before next call | Downside deviation | +0.44% | 1.79 | 38,357 | 2,389 |

Also §7.1: at **63 trading days** idio vol is **+0.69%, t = 3.22**, but only **30.3%** of those windows end before the next observed call, which the author himself uses to keep **42 days** as the primary horizon. Appendix **Table 21** (secondary outcomes): 42-day tail-loss magnitude **+0.60%, t = 1.23** (all calls) and **+0.79%, t = 1.68** (restricted); 42-day market beta **0.0010, t = 0.32** and **0.0013, t = 0.46**; excluding leadership/succession passages the 42-day idio-vol coefficient is **+0.46%, t = 1.80** and downside **+0.41%, t = 1.60**.

**Increment beyond labor shortage and generic tone — Table 4** (Panel A: 7,019 common firm-years 2006–2021, firm + year FE; Panel C: log idio vol over the next 42 trading days, adding pre-call risk and outcome-quarter FE):

- Panel A, idio vol: HC alone **0.0081 (4.02)**; HHQ alone **−0.0014 (−0.74)**; HC+HHQ **0.0096 (4.25) / −0.0049 (−2.20)**; HC+HHQ+generic tone **0.0065 (2.97) / −0.0047 (−2.16)**; HC excluding shortage passages **0.0068 (3.28) / −0.0044 (−2.14)**.
- Panel B, market beta: HC **0.0062 (1.30)**, HHQ **0.0124 (2.30)**.
- Panel C, 42-day idio vol: all calls HC alone **0.0049 (2.09)**, N = 41,009; all calls with generic tone **0.0033 (1.59)**; one-call HHQ quarter with HC+HHQ+tone **0.0065 (2.17) / −0.0061 (−2.24)**, N = 23,673; same with shortage passages removed **0.0055 (1.80) / −0.0053 (−1.97)**. Generic tone alone: negative-word coefficient **0.02241 (7.36)**.

**Seven classification rules — Table 15:** idio-vol coefficients **0.005031 (3.16) to 0.006540 (4.24)**; downside deviation **0.005609 (3.73) to 0.006242 (4.00)**; worst monthly return **−0.004900 (−4.12) to −0.004386 (−3.46)**; market beta **−0.002296 to +0.001612, insignificant under every rule**. Appendix **Table 17** sensitivities: two-way firm+year clustering **3.43 → 2.86**; excluding 2020–2021 **0.0053 (2.68), N = 7,358**; FY2006–FY2014 **0.0094 (2.46), N = 3,036**; FY2015–FY2024 **0.0033 (1.95), N = 9,052**; asinh score **0.0056 (3.59)**; winsorized outcome **0.0058 (3.42)**; inclusive threshold **0.0056 (3.32)**; disruption share **0.0060 (3.96)**; positive firm-years only **0.0045 (2.54), N = 7,049**. The extensive-margin indicator in the annual model is **t = 1.12 (ns)** (§6.3).

**Organizational outcomes — Table 6** (Panel A two-way firm × fiscal-year clustered, % points per SD): CEO roster absence **2.091 pp (4.25)** unrestricted / **1.129 pp (2.79)** no-leadership, N = 9,962, 1,458 firms; named-executive roster-exit rate **1.510 pp (4.54)** / **0.962 pp (3.17)**, N = 10,000, 1,466 firms; any roster exit **4.090 pp (4.71)** / **2.786 pp (3.34)**. Panel B (CEO leaves office strictly before the next call, intervals 45–150 days, exactly one active CEO spell, 715 exits, event rate 2.54%): LPM **0.391 pp (2.53)**, N = 27,691, 1,411 firms; cloglog hazard **1.088 [1.029, 1.151]**; conditional Poisson **1.112 [1.009, 1.225]**; excluding intervals with a specific prior Item 5.02 disclosure **0.481 pp (3.82)**, N = 27,506, exits 530, 185 intervals dropped, cloglog **1.127 [1.067, 1.190]**; excluding broad prior/same-day disclosure **0.237 pp (2.50)**, N = 27,290, exits 314, 401 intervals dropped, cloglog **1.145 [1.065, 1.231]**; any-positive indicator **0.949 pp (3.74)**.

**Validation / measurement quality (§4.2, §5.2–§5.4, §8.3):** first-stage screen precision **0.922**, recall **0.769** at threshold 0.65; author-guidance agreement **76%, Cohen's κ = 0.519, precision/recall 0.75** (explicitly *"fidelity to the author-defined boundary rather than out-of-sample performance"*); 100 ticker–calendar-year audit → any-disruption precision **1.00 [0.93, 1.00]**, recall **0.92 [0.87, 0.96]** conditional on the screen; second hard-boundary sample of 120 excerpts → agreement **65.0%, κ = 0.300 [0.134, 0.464]**; stratified audit of rejected sentences → population-weighted miss rate **2.15%**, screen recall ≈ **0.73**.

**Other source-reported structure:** score persistence — lagged standardized score **0.148, t = 4.64** (§6.6). Labor-intensity interaction **0.0085, t = 2.88** (§6.4). Mean score **1.78** excerpts/10k words in labor-intensive vs **0.92** in other FF48 industries (§5.1). HHQ overlap (25,307 common firm-calendar-quarters with exactly one call): **62.2%** of HHQ-positive are HC-positive, **33.8%** of HC-positive are HHQ-positive, continuous correlation **0.476** (**0.406** excluding shortage passages) (§5.3). Pre-call risk path (Figure 3): idio-vol coefficients far **0.63% (2.25)**, middle **0.69% (2.49)**, near **0.85% (3.36)**; downside **0.71/0.80/0.87% (2.47/2.76/3.44)**; **post-minus-pre changes t = 0.59 (idio), −1.03 (downside), −0.36 (tail)** (§7.2).

### Independently reproduced

not independently reproduced

### Negative evidence

1. **Zero trading layer.** Full pinned-text word scan gives `transaction cost` 0, `trading cost` 0, `slippage` 0, `bid-ask` 0, `fee` 0, `spread` 0, `borrow` 0, `hedge` 0, `rebalance` 0, `market timing` 0, `Sharpe` 0, `backtest` 0, `alpha` 0, `trade`/`tradable`/`invest`/`position`/`order`/`long` 0, `quintile` 0, `portfolio` 1 (reference title only), `turnover` 22 (HR context only), `decile` 2 (score rank-stability only). **No cost, fill, borrow, capacity, turnover, sizing or P&L model exists; every such field is `data gap` and nothing is net of cost.**
2. **No return predictability — the source's own null.** Appendix **Table 18**: twelve-month-ahead return **−0.0007, t = −0.13, N = 12,520**; next-year idio vol **0.0017 (0.93)**; next-year total vol **−0.0002 (−0.10)**; employment growth **0.0031 (0.65)**; sales growth **0.0033 (0.45)**; ROA **−0.0009 (−1.14)**; capex/assets **−0.0001 (−0.37)**; absolute sales growth **−0.0176 (−1.79)** at 10% only. §6.6 states plainly that next-year outcomes are *"statistically imprecise"* and that the specifications *"do not detect a common directional change"*. **Any directional long/short reading of this paper has no support in it.**
3. **The cross-sectional level does not work — source's own test.** §6.3: replacing firm fixed effects with **Fama–French 48 industry + year fixed effects yields an idiosyncratic-volatility coefficient close to zero**, and the author writes that *"the annual result is concentrated in changes within a firm over time rather than in a stable cross-sectional ranking of firms."* A cross-sectional quintile/decile implementation on score **levels** is therefore directly contradicted by the source.
4. **No disclosure-date discontinuity and no measured event window.** §7.2: risk is already elevated before the call, *"There is no visible discontinuity at the call date"*, post-minus-pre t = 0.59 / −1.03 / −0.36, and the author characterizes the finding as **persistence, not arrival of a new risk state**. The immediate call-response interval (days **0 and +1**) is **excluded by design**, so the source never measures the only window a fast event trader could use.
5. **Generic tone absorbs part of the call-level effect.** §6.5/§8.2: adding transcript-wide Loughran–McDonald negative + uncertainty frequencies moves the 42-day coefficient from **0.00491 (t = 2.09) to 0.00332 (t = 1.59, insignificant)**; only the one-call-quarter subsample retains t = 2.17. The strongest incremental evidence is the *annual* within-firm regression, not the forecast.
6. **Call-level secondary outcomes are weak.** First-block downside deviation **t = 1.38**; tail-loss magnitude **t = 1.23 / 1.68**; call-level market beta null (**t = 0.32 / 0.46**); leadership-excluded 42-day idio vol drops to **t = 1.80** and downside to **t = 1.60** (Table 21).
7. **Sub-period and clustering fragility.** FY2015–FY2024 **t = 1.95**; excluding 2020–2021 **t = 2.68**; two-way firm+year clustering **t = 2.86** (all above conventional cutoffs but close); the extensive-margin indicator is **t = 1.12 (ns)**; the annual result's second half carries most of the weight.
8. **No out-of-sample protocol for the classifier.** Labels are produced by `Claude Opus 4.8` under author-written criteria; §5.4 states the agreement exercise *"measures fidelity to the author-defined boundary rather than out-of-sample performance."* There is **no held-out-period test, no temporal train/test split of the score, and no second-labeller replication** in the paper.
9. **Measurement error is conditioned upon, not resampled.** §8.3: *"The regression standard errors condition on the estimated score; the seven-rule exercise evaluates plausible classification boundaries but does not resample the complete measurement procedure."* First-stage screen recall ≈ **0.73**; missed sentences cannot be recovered.
10. **Point-in-time transcript availability is unaddressed.** The two archives are retrospective scrapes whose *"coverage … vary in coverage over time"* and *"place greater weight on large public firms"* (§8.3); no publication timestamp, revision policy or availability lag is audited → **publication-lag leakage risk is `data gap`, unquantified.**
11. **Endogeneity acknowledged.** §8.3: *"firms choose what to discuss … Firm fixed effects, calendar-time controls, matched pre-call risk, content exclusions, and public-information screens sharpen the economic interpretation but do not create exogenous variation in human-capital disruption."*
12. **The leakage screen is partial.** The prior-disclosure audit covers **Item 5.02 filings only**; *"other SEC forms, press releases, news reports, and earlier disclosures remain outside the filing screen"* (§7.3), and dropping the broad prior/same-day disclosure set cuts the CEO-exit coefficient from **0.481 pp to 0.237 pp**. Trimming by Cook distance also makes the estimate imprecise (§7.3, Appendix Table 22).
13. **Modest human–machine agreement.** κ = **0.300 [0.134, 0.464]** on 120 hard cases; κ = **0.519** against the author's own 50 guidance excerpts; the construct boundary is a judgement, and Figure 4/Table 14 show rank churn under alternative rules (Spearman 0.889–0.914).
14. **Comparison-measure timing mismatch.** The HHQ labor-shortage comparison aligns a **calendar-year** released measure to this paper's **fiscal-year** measure (exact only for December year-ends) and, at call level, HHQ has *"no call dates and transcript text"* → a quarter-level comparison, explicitly **not a verified same-transcript match** (§3.5, §6.5).
15. **Sample-specific standardization.** All headline coefficients are *per within-estimation-sample SD* (Table 23), so the reported magnitudes are not a real-time, implementable threshold; a tradable rule needs an expanding-window scaling that the source does not provide.
16. **No multiplicity control and no inference suite.** Roughly 23 tables × seven classification rules × several outcomes are reported with **no family-wise or false-discovery correction, no Newey–West/HAC treatment of the score, no bootstrap of the measurement pipeline, and no placebo**; significance is reported from clustered OLS t-statistics only.
17. **Source-quality limits.** Preprint only, **v1, single author, no peer review, no code, no data-availability statement, arXiv non-redistributable licence, single market (US equities), single text pipeline**, and the paper reports **no Sharpe, no drawdown, no turnover and no capacity** because it has no trading model at all.

## Falsification plan

Every threshold below is **[research-defined]** (a Scout-chosen acceptance/failure cutoff) and every operational rule is **[research-proposed]**; none is source-reported.

- **F1 — Point-in-time transcript reconstruction. [research-defined]** Rebuild the score using only transcripts whose verifiable publication timestamp is ≤ the intended order time, with an expanding-window (not full-sample) standardization. **Pass:** 42-day idio-vol coefficient ≥ **0.35% per SD** (70% of the source's 0.50%) with two-way firm × outcome-quarter clustered **|t| ≥ 2.0**. **Fail:** |t| < 2.0 or coefficient ≤ 0 → the signal is a publication-lag artifact; abandon tradability claims.
- **F2 — Competing-explanation horse race. [research-defined]** Jointly enter (a) the score, (b) transcript-wide LM negative + uncertainty frequencies, (c) a raw workforce-word count, (d) the trailing 42-day realized idio vol, and (e) the HHQ labor-shortage measure where available. **Pass:** the score keeps a coefficient ≥ **0.33%** (its tone-controlled level in Table 4 Panel C) with **|t| ≥ 2.0**. **Fail:** the score's t falls below 2.0 once (b)–(e) enter → the "human-capital" construct is not identified separately from generic adverse language and trailing risk.
- **F3 — Cross-sectional tradability test. [research-defined]** **[research-proposed]** Form weekly quintiles of the standardized call-level score over calls in the trailing 5 sessions; measure FF3-alpha and realized idio vol over the next 42 trading days, long Q1 / short Q5, equal notional. **Pass:** H–L alpha **|t| ≥ 2.0** *and* a realized-volatility spread ≥ **0.25 pp annualized**. **Fail (expected on the source's own §6.3):** |t| < 2.0 → the level-ranked implementation is rejected even if F1/F2 pass; only a within-firm change or a volatility-convexity implementation may proceed.
- **F4 — Volatility-convexity implementation. [research-proposed / research-defined]** **[research-proposed]** Enter at event day **+2** a 42-calendar-day single-name long-volatility position, delta-hedged, exit at **+43**, size capped at **20% of contract volume**. **Fail if** any of: net-of-cost mean P&L ≤ 0 at **10 bp** per side; net Sharpe ≤ **0.3**; or the realized 42-day implied-to-realized spread does not exceed a matched no-call control by ≥ **1.0 volatility point**.
- **F5 — Cost ladder. [research-defined]** 0 / 5 / 10 / 20 / 30 bp per side, plus a separate quoted-spread and a 20%-ADV participation run. **Fail** if the chosen implementation is net ≤ 0 at 10 bp, or its one-way turnover exceeds one full round trip per 42-day window.
- **F6 — Placebo. [research-defined]** 1,000 draws of firm-level circular time shifts of the score (random offsets ≥ 60 trading days). **Pass:** the observed 42-day β exceeds the **95th percentile** of the placebo |β| distribution and the placebo mean |β| stays inside ±0.10%.
- **F7 — Event-jump ablation (re-admit days 0/+1). [research-defined]** Re-estimate with the immediate call-response interval **included** and require the incremental post-minus-pre β ≥ **0.20%** with **|t| ≥ 2.0**. **Fail:** the forecast is only persistence already visible pre-call (the source's own §7.2 finding) and offers no post-call entry edge.
- **F8 — Redundancy ablation. [research-defined]** Regress 42-day idio vol on pre-call risk + controls **without** the score. **Fail (i.e. hypothesis weakened)** if adding the score changes R² by < **0.5%** or adds < **0.15%** per SD with |t| < 2.0 → the score is redundant with realized risk.
- **F9 — Multiplicity, sub-period and frozen forward window. [research-defined]** Apply Benjamini–Hochberg **q < 0.10** across the grid {idio vol, downside dev, worst month, beta} × {21, 42, 63 days} × {7 classification rules}; require the sign to hold in **both FY2006–FY2014 and FY2015–FY2024** *and* in a **frozen post-2024-12-31 forward window**. **Fail** if fewer than half the grid cells survive BH, or either sub-period flips sign.
- **F10 — Labeller reproducibility. [research-defined]** Re-label the 729/400 excerpt sets with a **different, non-Opus** labeller under the identical written criteria and re-train. **Pass:** firm-year Spearman ≥ **0.85** with the baseline score **and** annual idio-vol coefficient ≥ **0.0040** with **|t| ≥ 2.5**. **Fail** → the signal is labeller-dependent and must not be built.
- **F11 — Cross-market transport. [research-defined]** Replicate F1 on **STOXX Europe 600, Nikkei 225 and CSI 300** call corpora with the same pipeline. **Fail** if ≥ **2 of 3** markets give |t| < 2.0 → the mechanism is US-specific.

**Action on failure:** any of F1, F2, F6 or F10 failing downgrades `confidence` to `low` and blocks all implementation work; F3 failing eliminates the cross-sectional implementation but does not by itself kill the volatility-convexity branch; F5 failing eliminates the implementation while leaving the paper's research finding intact.

## Crypto portability

**`unproven`**

- **Mechanism does not transfer.** The signal is management's scheduled, analyst-attended quarterly disclosure about *labor* as a production input. Crypto networks and DAOs have no Compustat-like workforce disclosure regime, no Execucomp roster, no equivalent quarterly call ritual, and token-team personnel changes are disclosed opportunistically through unstructured channels → there is **no counterpart input channel** for the mechanism.
- **Clock.** The source's windows are **trading-day** windows (`+2 → +22`, `+23 → +43`, 42/63 days) with an event day defined as the first CRSP trading day on or after the call. Under 24/7 sessions there is no "next trading day", no day 0/+1 buffer, and candles are venue-local rather than exchange-session aligned → window definitions must be re-derived, not copied.
- **Instrument.** Single-name equity options / variance instruments have no crypto analogue at the issuer level; crypto vol products are venue- and tenor-specific, and single-name "tokens" carry additional smart-contract, custody and delisting risk.
- **Market structure.** Funding, mark/index price, liquidation, borrow for shorting, and venue fragmentation are all **absent from a source that models no equity trading costs at all** — porting would start from an already incomplete cost model.
- **Evidence boundary.** The source contains **zero crypto evidence and zero return evidence**; labeling this `direct` or `adapted` would be false. A crypto analogue (e.g. protocol-team-disruption disclosure → forward idio vol of a token) is a **ported hypothesis with no empirical support**, hence `unproven`.

## Limitations

- `data gap` — no transaction cost, slippage, spread, borrow, fill, latency, participation, leverage, dividend, capacity, turnover, sizing or P&L model exists in the source; no execution assumption of any kind is stated.
- `data gap` — no transcript publication timestamp or availability lag; point-in-time tradability of the score is unestablished (the largest single leakage risk).
- `data gap` — no code, no replication package, no data-availability statement, no repository URL or commit; the two transcript archives are third-party and non-reproducible by us.
- `data gap` — exchange/venue, order type, fill model, timezone of the recorded call date, and the exact identity of the 400-excerpt threshold-selection sample.
- `underspecified` — the source standardizes the score *within the estimation sample*, so no real-time threshold can be read off the reported coefficients; the source defines **no** entry, exit, holding, sizing or position rule at all.
- `not independently reproduced` — every number above is source-reported from a single pinned HTML rendering of a v1 preprint.
- `unproven` — no return predictability (Table 18 twelve-month return t = −0.13), no cross-sectional level effect (§6.3 ≈ 0), no P&L, no out-of-sample classifier test, no placebo, no multiplicity control, no second market, no labeller replication.
- Source-quality: **preprint only, single author, no peer review**, measurement error conditioned upon rather than resampled, first-stage screen recall ≈ 0.73, human–machine κ as low as 0.300 at the construct boundary, retrospective transcript archives with time-varying large-firm-skewed coverage, and acknowledged non-exogenous disclosure choice.
- The 63-day horizon is explicitly not clean (only 30.3% of windows end before the next call) and should not be used as a holding-period anchor.
- Scope: single asset class (US equities), single frequency (daily/monthly), sample ends **FY2024 / calls ≤ 2024-12-31**, no capacity or liquidity analysis.

## Implementation status

`implementation_status: not-implemented`

Nothing in this record has been implemented in our research stack. No score pipeline, no classifier training, no transcript ingestion, no Qlib backtest, no production card, no Paper/Testnet/Live artifact exists. The record is a normalized research capture of a preprint; the operational rules in `Signal`, `Execution assumptions` and `Falsification plan` are Scout-authored research proposals that have never been run.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

The presence of this record in the repository does **not** mean it passed Research Intake Review, entered Hermes Wiki Brain, entered `/results/_handoff/candidates.json`, completed Qlib full-backtest validation, became a frozen survivor or leaderboard entry, demonstrated profit, validated alpha, or been approved for implementation, Paper, Testnet or Live trading. Crypto portability is `unproven` and is not authorization to trade. No record may promote itself by wording, evidence count, confidence or schedule behavior.

## Related Wiki records

Wiki Brain `kb_search` was run **four times before writing**: `human capital disruption earnings call firm-specific idiosyncratic risk` → **0 results**; `earnings call text measure idiosyncratic volatility risk state` → 4 results, none mechanism-adjacent (illiquidity-at-risk, STRATA intraday ranking, AlphaSchema factor mining, Avellaneda–Lee residual reversion); `labor shortage workforce disclosure equity firm risk premium textual signal` → **0 results**; `earnings call` → 10 results, of which the two mechanism-adjacent pages below were opened and verified. No other Wiki link is asserted; nothing was written to Wiki Brain.

- [[quant/earnings-announcement-premium-jump-risk-decay-falsification-2026-09-13]] — adjacent on earnings-event volatility/risk compensation; distinct in mechanism (scheduled event-jump premium vs. text-measured persistent organizational-risk state), signal construction (calendar event window vs. two-stage text classifier) and horizon.
- [[quant/single-name-equity-earnings-iv-crush-bid-ask-falsification-2026-09-13]] — adjacent on single-name equity option IV vs. realized around earnings; distinct in mechanism (pre-earnings implied overstatement vs. forward idiosyncratic-volatility state), signal construction and data dependency (quoted option surfaces vs. transcripts).

Four-axis distinction against the closest existing repository records: **mechanism** — disclosed workforce disturbance as an organizational-input shock (vs. FinBERT speaker-weighted post-earnings return signal, vs. LLM metric-attrition long/short, vs. crypto cross-sectional idio-vol pricing, vs. scheduled earnings-jump variance compensation); **signal construction** — workforce vocabulary + `all-mpnet-base-v2`/RBF-SVM screen + 3× `deberta-v3-base` ensemble counted per 10,000 words (vs. sentiment weighting, embedding-ruler delta, realized-variance sorts); **universe/market type** — US Compustat/CRSP firms with earnings calls (vs. S&P 500 return cross-section, S&P 100 metric shifts, crypto spot/perpetual); **horizon/regime** — 21/42/**63**-trading-day forward *idiosyncratic volatility* with days 0/+1 excluded (vs. same-day/next-day post-earnings returns, vs. annual cross-sectional risk premia).

## Sources

- Primary (every figure above): Ang Zhang, *Disclosed Human-Capital Disruption and Firm-Specific Risk*, arXiv:`2608.14859v1` [q-fin.ST], submitted 14 Aug 2026 — landing `https://arxiv.org/abs/2608.14859`; pinned full text `https://arxiv.org/html/2608.14859v1` (511,256 bytes, SHA-256 `70f09d916a94d803b603a9471ca9b07fcee73825baa71bc121af1d95f41ba1c8`, read end to end 2026-09-25); DataCite DOI `https://doi.org/10.48550/arXiv.2608.14859` (HTTP 302 → abs, checked 2026-09-25).
- Data/inputs **named by the primary source** (not independently consulted by this record): `TPotterer (2023)` Motley Fool transcript archive; `Kurry (2025)` S&P 500 / large-cap transcript archive; CRSP; Compustat and Compustat Quarterly; Kenneth French data library (daily MKT/SMB/HML/RF); Execucomp; Harford, He and Qiu (2026) released labor-shortage measures; SEC Item 5.02 filings; `all-mpnet-base-v2`; `microsoft/deberta-v3-base`; `Claude Opus 4.8`.
