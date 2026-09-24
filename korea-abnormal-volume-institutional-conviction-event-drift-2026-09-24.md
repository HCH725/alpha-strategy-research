---
schema: strategy-research-record-v1
title: "Korea Abnormal-Volume Event Drift: Market-Cap-Normalized Institutional-Conviction Quartiles after HVRP Events"
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - event-study
  - high-volume-return-premium
  - investor-identity
  - korea-equities
  - volume-anomaly
status: research-only
confidence: medium
source_as_of: 2025-12-24
sources:
  - "Sungwoo Kang, 'Sources and Nonlinearity of High Volume Return Premium: An Empirical Study on the Differential Effects of Investor Identity versus Trading Intensity (2020-2024)', arXiv:2512.14134v2 [q-fin.TR], v1 Tue 16 Dec 2025 06:32:04 UTC (253 KB), v2 Wed 24 Dec 2025 06:48:56 UTC (267 KB). https://arxiv.org/abs/2512.14134"
  - "Pinned full text (v2 HTML, LaTeXML): https://arxiv.org/html/2512.14134v2 — fetched and read in full 2026-09-24 (414,641 bytes HTML; 106,175 characters extracted text)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions:
  - "Source-internal numeric contradiction (v2): the Conclusion reports the institution-led Q4-Q1 day+50 CAR spread as '7.47 percentage points (12.12% - 4.65%)' — which matches printed Tables 6 and 7 — while Section 5 (Discussion) reports 'the Q4-Q1 CAR spread is 10.12 percentage points (10.07% - (-0.05%))' and calls it 'highly significant'. The values 10.07% and -0.05% appear in no printed table, and no significance test for the quartile spread is printed anywhere; the two spread figures are never reconciled."
---

# Korea Abnormal-Volume Event Drift: Market-Cap-Normalized Institutional-Conviction Quartiles after HVRP Events

## Provenance

- **Primary source:** Sungwoo Kang, *"Sources and Nonlinearity of High Volume Return Premium: An Empirical Study on the Differential Effects of Investor Identity versus Trading Intensity (2020-2024)"*, `arXiv:2512.14134v2 [q-fin.TR]`. URL: https://arxiv.org/abs/2512.14134
- **Version pinned:** v2 (last revised Wed 24 Dec 2025 06:48:56 UTC, 267 KB); v1 Tue 16 Dec 2025 06:32:04 UTC (253 KB). Full text pinned to `https://arxiv.org/html/2512.14134v2` (HTML header/footers print `arXiv:2512.14134v2 [q-fin.TR] 24 Dec 2025` and `License: CC BY 4.0`), fetched and read in full on 2026-09-24. All numbers below are attributed to this pinned v2 only.
- **Author list (exactly as printed):** sole author **Sungwoo Kang**, Department of Electrical and Computer Engineering, Korea University, 145 Anam-ro, Seongbuk-gu, Seoul 02841, Republic of Korea; email `krml919@korea.ac.kr` (printed in the author block).
- **Publication status:** preprint only. The arXiv record has no Comments, no Journal reference, no publisher DOI field; DataCite DOI `10.48550/arXiv.2512.14134` resolves (HTTP 302 → abs page, verified 2026-09-24). Peer-review status not stated in source. Category `q-fin.TR`.
- **Sample / universe (v2, §3.1):** January 1, 2020 – December 31, 2024; all stocks listed on the Korea Exchange (KOSPI and KOSDAQ analyzed in detail separately). Exclusions: (1) delisted stocks and stocks under administrative issues, (2) stocks priced below 1,000 won, (3) stocks with zero trading volume for two or more consecutive days, (4) stocks with outstanding-share changes in the 20 trading days before the event date.
- **Data (v2 §3.1 and Data Availability Statement):** daily prices/volume/outstanding shares via Daishin Securities' Creon Plus DataReader API; investor-type net-purchase data (institutional, foreign, retail) via the `pykrx` library from official Korea Exchange data. The Data Availability Statement says data are available from the providers "upon reasonable request and with permission of the data providers" with ToS restrictions; **no code, no repository, no replication package** anywhere in v2 (`github` hits are only arXiv chrome).
- **Transaction-cost treatment (primary-source full-text scan of pinned v2):** `slippage` 0, `bid-ask` 0, `latency` 0, `commission` 0, `transaction cost` 0, `trading cost` 0, `market impact` 0, `borrow` 0, `win rate` 0, `Sharpe` 0, `drawdown` 0, `backtest` 0; the 3 `fee` hits are "feedback" wording, the 3 `cost` hits are "cost of capital"/a cited sentence about implementation costs/margin-loan costs, the 5 `turnover` hits are literature review. **No fee, spread, slippage, borrow, fill, capacity, or P&L model exists anywhere — recorded as `data gap`, never as zero cost.**
- **Rendering artifact:** the arXiv landing-page abstract contains unrendered LaTeX macros `+\institutionLedQFourDayPlusFiftyCAR` and `+\institutionLedQOneDayPlusFiftyCAR` in place of the Q4 and Q1 numbers; the values are recoverable from printed Tables 6/7 (12.12% and 4.65%) and the Conclusion prose.
- **Source-identity dedup (this run, 2026-09-24):** hidden-inclusive repository scan of **2,517 `*.md` files** plus `coverage_manifest.csv` (5,808 lines) for `2512.14134`, the exact title ("Sources and Nonlinearity"), "High Volume Return Premium", `HVRP`, `LVRP`, "Chae and Kang", "Sungwoo Kang", "Donghak", "institutional buying intensity", "volume return premium", "abnormal volume event", `pykrx`, `Creon`, `Institution-Led` → **zero source-identity hits**. The only "Sungwoo Kang" hits are a **different paper**: `arXiv:2512.18648v3` (matched-filter order-flow normalization), already captured as `order-flow-matched-filter-normalization-investor-segmentation-2026-09-02.md`. `KOSDAQ`/`Korea Exchange` matches are two unrelated records (Korea PEAD via DART filings; KRX leveraged-ETF closing rebalance) with different sources and mechanisms, and `crypto-cross-sectional-abnormal-volume-disagreement-2026-08-31.md` is sourced to Garfinkel et al. (DOI `10.1111/fima.12491`) on crypto disagreement — all distinct.
- **Four-axis distinction vs the same-author sibling record (`arXiv:2512.18648`, same market, same period):** (1) *mechanism* — that record derives a signal-processing matched filter for continuous order flow; this record is an event-study test of the High Volume Return Premium with an identity×intensity double sort; (2) *signal construction* — continuous cross-sectional z-scored composite factor with daily rebalance vs an `ADTV>5` volume-shock event trigger, argmax investor-type classification, and within-type intensity quartiles; (3) *horizon* — daily rebalanced long-short quintiles vs a 50-trading-day post-event CAR window; (4) *material data dependency* — both use KRX investor-type flows, but this record additionally depends on the event-study scaffolding of An et al. (2006) (dependent-event exclusion, [-50,+50] windows, forward-return nearest-trading-day rule). Different canonical source identities, materially distinct constructions → independent record.
- **Wiki Brain linkage:** `kb_search` for "high volume return premium institutional conviction Korea" returned 0 results; a broader "abnormal volume event study investor type flow drift" search returned only unrelated event families (spin-off drift, token unlock, Form 4). **No related Wiki page is asserted for this mechanism; none fabricated.** No Wiki Brain write, no Kanban, no backtest performed.
- **Primary-source checksum summary:** landing page + v2 HTML full text opened and read (all sections including appendices); authors, version/date, sample, universe, and cost treatment verified directly from the primary source as listed above; every quantitative claim in this record is located to a specific printed table or named section of pinned v2.

## Economic mechanism

### Source-reported

The paper re-examines the **High Volume Return Premium (HVRP)** — the persistence of positive abnormal returns after abnormally high trading-volume days — on 2020–2024 Korean data, following An et al. (2006)'s 2001–2003 design. Its stated contributions: (a) classify each abnormal-volume event by the **leading investor identity** (institutions / foreigners / retail via an argmax of net-buy ratios), (b) quantify **trading intensity** per event with two competing normalizations — net buy ÷ total trading value ("participation") vs net buy ÷ market capitalization ("conviction") — and (c) show that only the market-cap normalization yields a monotone intensity→50-day-CAR relationship for institution- and foreign-led events, while retail-led events stay near zero at all intensity levels (noise-trader reading). The source frames three ex-ante hypotheses (§2.5): H1 identity heterogeneity (informed institutional/foreign events show persistent positive CAR; retail events dissipate), H2 regime moderation (COVID shock amplifies; the Donghak Ant Movement temporarily makes retail-led events persistent), H3 nonlinearity (linear dominance-score correlation fails; monotone quartile pattern emerges only with market-cap normalization). Source-reported claims are recorded below as third-party claims, gross, market-adjusted, and are not our results.

### Research interpretation

Falsifiable hypothesis in our terms: **the end-of-day disclosure of investor-type net flows on a >5× volume-shock day contains informed-accumulation information that the market underreacts to, producing positive post-event drift concentrated in events where institutions (or foreign investors) buy a large fraction of the firm's market cap.** Component roles: *trigger* = abnormal-volume event (`ADTV>5`); *classifier* = leading investor identity (argmax net-buy ratio); *strength filter* = within-type intensity quartile under market-cap normalization (Q4 = highest conviction); *evaluation horizon* = 50 trading days, market-adjusted. The source tests none of these components as an ablation, and does not rule out competing mechanisms — attention/visibility effects (Merton), short-horizon liquidity provision, size/momentum exposure, or the pure mechanical fact that a +6% event-day jump is followed by partial continuation for any large-move event. Whether the Q4-minus-Q1 spread survives after excluding the event-day return itself is **not printed per quartile** (data gap) and is the decisive question for tradability.

## Signal

Source-specified elements (all `source-reported` from pinned v2 §3.2):

- **Formation timestamp:** event day *t*; `ADTV_{i,t} = Vol_{i,t} / (mean of Vol_{i,t-j}, j=1..20)`; event when `ADTV > 5`. Leading-investor classification uses day-*t* full-day investor-type net-purchase ratios (available only after market close *t* via KRX/pykrx publication).
- **Dependent-event rule:** events within 50 trading days after an initial event are treated as dependent and excluded; final sample 26,604 independent events (from ~73,500 raw `ADTV>5` events; Tables 1–2).
- **Classification:** argmax over institution / foreign / retail net-buy ratio (measured as % of total trading value for classification purposes only).
- **Intensity:** quartiles Q1–Q4 computed **within each investor type** over the intensity distribution including sign, under Spec A (net buy ÷ total trading value) and Spec B (net buy ÷ market capitalization); Spec B is the paper's favored "conviction" measure.
- **Evaluation (not a trading rule):** event study over [-50, +50] trading days with market-adjusted abnormal return `AR_{i,t} = R_{i,t} − R_{M,t}`; Method 2 forward returns use the trading day closest to the target within an 80%–150% of-horizon band (e.g., 20-day → closest close in days 16–30).

Not specified by the source (`underspecified` / `data gap`): **no entry rule, no exit rule, no holding/turnover rule, no position sizing, no order type, no signal-to-execution timing, no stop, no re-entry rule anywhere in v2** — the entire trading layer is absent, so any operationalization below is ours:

- **Research-proposed entry:** long-only, buy at the **next trading-day open after day *t*** (earliest point at which day-*t* volume and investor-type flows are both observable), target events classified institution-led (or foreign-led) with intensity in Q4; hold 50 trading days; equal-weight across concurrent events with non-overlapping 50-day windows (the source excludes only *forward* dependent events).
- **Research-proposed short side (if used):** Q1 institution-led events as the short candidate — but the source never tests a short leg, and it notes Korean short-selling bans during 2020–2021, so short feasibility is regime-dependent.
- Parameters `ADTV=5`, 50-day dependence window, quartile count = 4 are `source-reported`. The market index used for `R_M` is **not stated** (KOSPI vs KRX all-share vs equal-weight — data gap); the date/source of the market-cap denominator is **not stated** (data gap); tie / all-three-negative net-flow argmax cases are **not addressed** (data gap).

## Required data

- **Instrument / universe:** all KRX-listed common stocks (KOSPI + KOSDAQ), 2020-01-01 → 2024-12-31, after the four §3.1 exclusions (`source-reported`).
- **Venue / vendor:** Korea Exchange official investor-type daily net-purchase statistics via `pykrx`; daily prices/volume/shares via Daishin Securities Creon Plus DataReader API (commercial, ToS-restricted) (`source-reported`).
- **Fields:** daily OHLCV, outstanding shares, market capitalization, total trading value, investor-type (institutional / foreign / retail) net buy value, market index returns for the market-adjusted model (index identity unstated), delisting/administrative-status flags.
- **Point-in-time:** investor-type flows and volume of day *t* become observable only after close *t*; any real-time rule must execute no earlier than open *t+1* (`research-proposed`).
- **Missing-data / survivorship:** zero-volume ≥2 consecutive days excluded; delisted stocks excluded — the source does not state whether the delisting exclusion is point-in-time or ex-post over the full sample (data gap; ex-post exclusion would bias CAR upward).
- **Costs:** fees, spread, slippage, borrow, impact, capacity — all omitted from the source (data gap, see Provenance scan).

## Execution assumptions

The source states **no execution assumptions whatsoever**: no order type, no fill model, no latency, no signal-to-order delay, no fees, no spread, no slippage, no participation/capacity cap, no leverage, no borrow/short-availability treatment, no failure handling. All reported CARs are **gross, market-adjusted event-study returns, not portfolio returns**; they are `source-reported` and not net of anything because no cost model exists (data gap, never zero).

Material assumptions for any tradable reading (all `research-proposed`): enter next-day open, market-or-limit-at-open with no partial-fill modeling assumed (itself optimistic for small-cap events); cost ladder applied in F2 below; no borrow assumed for the long-only core rule. **Critical tradability gap:** the headline Q4 day+50 CAR of 12.12% is a [-50,+50] cumulative figure that *includes* the 9.75% event-day AAR and the pre-event window; the per-quartile CAR(0) needed to isolate post-entry drift is **not printed** (data gap). For orientation only, our arithmetic on printed Table 4 cells (full sample, labelled *our count, not a rerun*) gives post-event-day accumulation = CAR(+50) − CAR(0) = 3.09% − 2.06% = **1.03 pp over 50 trading days** for all 26,604 events — the per-quartile equivalents are unknown.

## Evidence

### Source-reported

All figures below are from pinned `arXiv:2512.14134v2`, gross, market-adjusted, and **not independently reproduced**:

- **Table 1 (descriptive):** this study 2,753,106 stock-day observations (2020–2024), ADTV mean 1.379, median 0.686, std 8.292, skewness 139.268, kurtosis 43,503.08, max 3,789.10 vs the original study's 65,490 obs / max 14.439.
- **Table 2:** only 2.68% of observations exceed `ADTV>5` (~73,500 raw events); 26,604 independent events after the 50-day dependent-event exclusion.
- **Table 4 (full-sample event study vs An et al. 2006):** 2020–2024 day-0 AAR **6.15%*** (t = 118.81)**; CAR at −10 −4.46%, −1 −4.09%, 0 +2.06%, +10 2.33%, +25 2.71%, **+50 3.09%**; original study day-0 AAR 5.056% (t = 83.66), CAR+50 3.672%; sample note "1,360 → 26,604 events". (`*p<0.10, **p<0.05, ***p<0.01` per table note.)
- **Table 5 (size):** day-0 AAR large 4.41% (t 10.79***), mid 6.06% (25.19***), small 6.19% (115.92***); day+50 CAR 1.43% / 4.00% / 3.07% — source reads this as mid-cap dominance.
- **Table 6 (market-cap normalization; the core claim):** Institution-led, 2,831 events (Q1 708 / Q2 914 / Q3 501 / Q4 708): day-0 AAR 4.17 / 5.95 / 8.14 / **9.75%**; day+20 CAR −1.37 / 1.70 / 2.60 / 9.85; **day+50 CAR 4.65 / 4.99 / 9.02 / 12.12%** (monotone). Foreign-led, 9,416 events (2,354 each): day+50 CAR −0.33 / 3.29 / 7.85 / **13.30%**. Retail-led, 15,512 events (3,878 each): day+50 CAR 0.56 / 0.01 / 0.88 / **0.65%** (flat, near zero). **No t-stats or significance markers are printed for any quartile CAR in Tables 6–7.**
- **Table 7 (normalization horse race):** institution-led Spec A (trading value) day+50 CAR 6.88 / 12.77 / 7.46 / **3.64%** (broken monotonicity, Q2>Q4) vs Spec B (market cap) 4.65 / 4.99 / 9.02 / **12.12%**; foreign Spec A 5.16 / 6.22 / 7.09 / 5.64 vs Spec B −0.33 / 3.29 / 7.85 / 13.30; retail Spec A 6.21 / 2.02 / −1.44 / −4.71 (inverted) vs Spec B 0.56 / 0.01 / 0.88 / 0.65 (flat).
- **Tables 8–10 (linear baseline, Method 2):** dominance-score vs forward-return correlations are near zero at 5/20/60 days across large/mid/small caps — |r| ≤ 0.0861 with all p > 0.06 (e.g., small-cap 20-day r = 0.0000, p = 1.000, n = 25,753). Source-reported **null** for the simple implementable linear signal.
- **Table 12 (regimes):** bull-market day-0 AAR 6.47% (t 101.87***) and CAR+50 3.84% vs bear 5.47% (61.58***) and 1.50%; Table 14 (COVID Feb–Apr 2020) day-0 6.31% (t 20.62***), CAR+50 3.12%; Table 15 (Donghak retail-led, Mar 2020–Dec 2021) day-0 6.24% (t 43.64***), CAR+50 **3.53%** with only `*` (t = 1.77) at day +50; Table 16 full-period retail-led day-0 5.72 / CAR+50 0.52 vs Donghak 6.24 / 3.53; Table 17 summary rows.
- **Conclusion prose:** institution-led pooled day+50 CAR 7.74%, foreign-led 6.03%, retail 0.52%; Q4−Q1 institution spread **7.47 pp (12.12 − 4.65)**. **Section 5 prose instead says 10.12 pp (10.07% − (−0.05%)) "highly significant" — recorded as a source-internal contradiction in frontmatter.**

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **No cost / fill / P&L model anywhere** (full-text keyword scan, Provenance): all CARs are gross; nothing nets fees, spread, slippage, borrow, or impact — data gap, never zero.
2. **The source proposes no strategy**: no entry, exit, sizing, or holding rule exists in v2; this is an event study, not a backtest. No Sharpe, drawdown, turnover, win rate, or capacity figure is printed anywhere.
3. **Headline CAR includes the uncapturable event-day jump:** Q4's 12.12% includes the 9.75% day-0 AAR and the pre-event window; per-quartile CAR(0) is not printed, so post-entry drift is unquantified (data gap). Full-sample post-day-0 accumulation is only ~1.03 pp / 50 days (our count on Table 4).
4. **No inference on the core claim:** Tables 6–7 print no t-stats, CIs, or stars for quartile CARs or the Q4−Q1 spread, yet the Discussion calls the spread "highly significant" and the Conclusion "statistically robust" — unsupported by any printed test (and numerically contradicted, frontmatter).
5. **The simple implementable signal fails in-sample:** the linear dominance score that could actually be traded daily shows |r| < 0.09 with all p > 0.06 at every horizon and size (Tables 8–10). The source's rescue — "linear failure validates nonlinear type-conditioned quartiles" — is a post-hoc-adjacent interpretation (H3a was stated ex ante in §2.5, but nothing is pre-registered).
6. **In-sample hypothesis setting:** hypotheses, sample, quartile construction, and regime definitions (COVID/Donghak dates, bull/bear 20% rule) are all chosen and tested on the same 2020–2024 data; no out-of-sample period, no pre-registration, no replication sample.
7. **Zero multiplicity control** across a large printed grid (3 investor types × 2 normalizations × 4 quartiles × 3 horizons × multiple regime subsamples).
8. **Event-count inconsistency:** classified event totals 2,831 + 9,416 + 15,512 = **27,759 > 26,604** independent events; the Table 6 footnote says totals differ "due to data filtering" but the sum exceeds the stated sample and is never reconciled. Quartile sizes are also unequal (institution Q3 = 501 vs 708/914/708) with no explanation.
9. **Survivorship risk:** delisted stocks are excluded and the exclusion's timing (point-in-time vs ex-post) is unstated; delisting returns are never mentioned.
10. **Market-adjustment index unspecified** (`R_M` undefined), market-cap denominator timing unspecified, argmax tie/all-negative cases unhandled — reconstruction requires choices the source does not license.
11. **Short side untested and partly infeasible:** only long-side CARs are reported; the source itself notes Korean short-selling bans during 2020–2021, overlapping the first two sample years.
12. **Regime results are marginal where they are newest:** the Donghak retail-transformation claim rests on day+50 CAR 3.53% with only 10% significance (t = 1.77); Table 17's "Donghak (All)" and "Donghak (Retail)" rows print identical day-0/CAR values, leaving the all-events row ambiguous.
13. **Competing mechanisms not horse-raced:** attention/visibility, generic large-move continuation, size/momentum exposure, and liquidity provision are cited in the literature review but never pitted against the conviction story.
14. **Internal documentation drift:** Table 3's section map and Table 4's caption ("vs 2024 Re-examination" for a 2020–2024 sample) do not match the body numbering — minor, but it weakens cross-referencing.
15. **Data/replication dependency:** commercial Creon Plus API + provider ToS restrictions, no code or replication package, single-author non-peer-reviewed preprint.
16. **Same-author convergent-claim concern:** the sibling `arXiv:2512.18648` (also uncaptured-independent here) argues market-cap normalization for institutional flow from theory; the two papers share author, market, and period, so they are not independent corroborating sources.

## Falsification plan

All thresholds below are `research-defined falsification thresholds`; all operational rules are `research-proposed` (none are source-specified).

- **F1 — Point-in-time replication with entry actually possible:** rebuild events from KRX/`pykrx` official data; enter at day *t+1* open, long-only institution-led Q4 (market-cap-normalized), hold 50 trading days, market-adjusted. **Fail if** post-entry (ex-day-0) Q4−Q1 CAR spread < 3.0 pp with stock- and date-clustered t < 2.0.
- **F2 — Cost ladder:** apply 0/5/10/25 bp per-side plus Korean securities transaction tax and a 20%-ADV participation cap. **Fail if** net 50-day Q4 edge < 1.0 pp or annualized net Sharpe < 0.5 at 10 bp.
- **F3 — Survivorship-safe sample:** retain point-in-time members including subsequent delisters with delisting returns. **Fail if** the Q4 day+50 CAR drops by more than 50% vs the source's 12.12% reading.
- **F4 — Inference audit of the core claim:** bootstrap/cluster-robust CI for Q4−Q1 and a monotonicity test (e.g., Jonckheere–Terpstra or slope on quartile index) across investor types. **Fail if** p ≥ 0.05 for institutions or the pattern is non-monotone in the replication.
- **F5 — Baseline horse race:** compare the Q4 rule against (a) all-event `ADTV>5` drift, (b) size- and 20-day-momentum-matched controls, (c) the source's own linear dominance score. **Fail if** incremental post-entry edge over (a)–(c) is < 1.5 pp / 50 days.
- **F6 — Label-shuffle placebo:** permute investor-type labels across events daily 1,000 times preserving flow marginals. **Fail if** the true spread's |z| < 2.0 vs the null distribution.
- **F7 — Frozen forward test:** pre-register the F1 rule and evaluate 2025+ data untouched. **Fail if** two consecutive years show non-positive post-cost spread or the spread retains < 50% of the in-sample level.
- **F8 — Normalization ablation:** repeat with deciles, terciles, and net-buy÷ADTV variants. **Fail if** market-cap normalization does not dominate trading-value normalization out-of-sample (the paper's H3c claim).
- **F9 — Multiplicity:** Benjamini–Hochberg q < 0.10 across the full replicated grid of types × normalizations × horizons. **Fail if** the headline cell does not survive.
- **F10 — Regulation/regime split:** evaluate 2020–2021 (short-ban) vs 2022–2024 separately. **Fail if** the long-only Q4 effect is present in only one half.

A failure of F1, F4, or F7 materially kills the tradable hypothesis; failures trigger `rejected` status with no unconstrained retuning rescue.

## Crypto portability

**unproven.** The mechanism depends on exchange-published, exchange-mandated investor-identity net-flow tags (KRX institutional/foreign/retail classifications) on a single continuous equity venue — data that does not exist in crypto. Speculative analogues only: exchange-reported taker-size buckets, Binance ranked-trader/pixel categories, on-chain entity labeling (custody vs retail deposits), or large-player leaderboard feeds; none reproduces the regulatory identity split. Additional breaks: 24/7 sessions erase the close/after-hours publication clock that sets the entry time; venue fragmentation splits any single venue's "market cap" denominator; perp funding, borrow scarcity, and liquidation cascades are unmodeled; the 50-trading-day event horizon and 1,000+-stock cross-section have no clean crypto equivalent. Crypto portability is not authorization to trade anything.

## Limitations

- `underspecified`: market index for `R_M`; market-cap denominator timing; argmax tie rules; quartile boundary values; per-quartile CAR(0); delisting-exclusion timing; independent-event backward overlap; institutional category composition inside "institutional" in KRX stats.
- `data gap`: all cost/fill/capacity/borrow fields; any risk metric (Sharpe/drawdown/turnover); any significance test on the headline spread; post-entry drift by quartile.
- `not independently reproduced`; `unproven` beyond a single in-sample Korean 2020–2024 window; preprint-only, single author, no code.
- Incremental-write threshold satisfied: no prior record in this repository covers the HVRP event-drift × investor-identity × normalization mechanism (source-identity dedup zero hits), and the mechanism differs materially on four axes from the same-author sibling record (Provenance).

## Implementation status

`not-implemented`. No component of this record exists in our research stack: no event scanner, no KRX flow ingestion, no backtest, no production card, no Qlib run, no Paper/Testnet/Live wiring. Nothing in this repository's downstream systems has been touched by this capture.

## Adoption boundary

This record is research material only. Its presence here does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; or approved for implementation, paper trading, testnet, or live trading. Every operational rule above is `research-proposed` / `research-defined`, not source-reported.

## Related Wiki records

`kb_search` for this mechanism ("high volume return premium institutional conviction Korea"; "abnormal volume event study investor type flow drift") found no Wiki Brain page matching this record's mechanism; broader hits were unrelated event-study families (spin-off drift, token unlock, Form 4). **No Wiki links are asserted for this mechanism; none fabricated.** Repo-adjacent but source-distinct sibling: `order-flow-matched-filter-normalization-investor-segmentation-2026-09-02.md` (different arXiv source, four-axis distinction in Provenance).

## Sources

1. Sungwoo Kang, "Sources and Nonlinearity of High Volume Return Premium: An Empirical Study on the Differential Effects of Investor Identity versus Trading Intensity (2020-2024)", arXiv:2512.14134v2 [q-fin.TR], v1 16 Dec 2025, v2 24 Dec 2025. https://arxiv.org/abs/2512.14134
2. Pinned v2 full text (all table/section provenance above): https://arxiv.org/html/2512.14134v2 — fetched and read 2026-09-24.
3. (Referenced only for distinction, not used for any claim in this record:) Sungwoo Kang, "Optimal Signal Extraction from Order Flow: A Matched Filter Perspective on Normalization and Market Microstructure", arXiv:2512.18648v3. https://arxiv.org/abs/2512.18648
