---
schema: strategy-research-record-v1
title: "Retail Investor Horizon Conditioning of Post-Earnings Announcement Drift: StockTwits Self-Reported Holding-Period Long-Short within Quarterly Earnings-Surprise Bins"
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - pead
  - retail-investor-horizon
  - stocktwits
  - event-study
  - equity-cross-section
  - long-short-equity
  - us-equities
status: research-only
confidence: medium
source_as_of: 2025-12-04
sources:
  - https://arxiv.org/abs/2512.00280
  - https://arxiv.org/pdf/2512.00280v2
  - https://doi.org/10.48550/arXiv.2512.00280
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Retail Investor Horizon Conditioning of Post-Earnings Announcement Drift: StockTwits Self-Reported Holding-Period Long-Short within Quarterly Earnings-Surprise Bins

## Provenance

- **Primary source (only source used for every number below):** arXiv `2512.00280`, Domonkos F. Vamossy (single author; affiliation and email printed on the paper: Department of Economics, University of Pittsburgh, `d.vamossy@pitt.edu`), *Retail Investor Horizon and Earnings Announcements*, primary category `q-fin.PR`.
- **Landing / version (arXiv abs page read 2026-09-23):** submission history shows exactly two versions — `[v1] Sat, 29 Nov 2025 02:10:22 UTC (658 KB)` and `[v2] Thu, 4 Dec 2025 22:35:24 UTC (650 KB)`; arXiv API returns **no `journal_ref` and no publisher DOI** → publication status is **preprint only / `not stated in source`**. The DOI `https://doi.org/10.48550/arXiv.2512.00280` resolved HTTP 200 to the arXiv abs page on 2026-09-23; it is the DataCite arXiv auto-DOI, not a journal DOI.
- **Primary-source checksum (performed 2026-09-23):** PDF `https://arxiv.org/pdf/2512.00280v2`, **57 pages, 1,120,030 bytes, SHA-256 `43a5fa9bfee0f76eb47b5576c4baf1f457f07d2e5b1fa2e90f34fb27cecc64b4`**; embedded metadata `/arXivID = https://arxiv.org/abs/2512.00280v2`, `/Author = Domonkos F. Vamossy`, `/Title = Retail Investor Horizon and Earnings Announcements`. Extracted with `pypdf` and read end-to-end: §1 Introduction, §2 measure of retail horizon + §2.1 Sample Construction + §2.2 Descriptive Statistics + §2.3 Measure Stability, §3 model and simulation, §4 Methodology (Eq. 15, A1–A4), §5.1–§5.5 Primary Findings, §6.1–§6.4 Discussion, §7 Conclusion, Tables 1–12, Figures 1–5, Appendices A–C, references.
- **Author list exactly as source:** exactly one author, Domonkos F. Vamossy (title page, PDF metadata and arXiv API all agree; no co-author appears anywhere).
- **Version/date inconsistency inside the source (recorded verbatim, not reconciled):** the arXiv stamp on the pinned PDF reads `arXiv:2512.00280v2 [q-fin.PR] 4 Dec 2025`, while the manuscript title page is dated `December 8, 2025` (a manuscript date later than its own v2 posting date). Both dates are carried as printed; `source_as_of` uses the verifiable arXiv v2 posting date `2025-12-04`.
- **Sample period (three places agree):** Table 1 note `We cover 2010 - 2021 June`; Figure 4 and Figure 5 captions `From January 2010 until June 2021`; abstract `self-reported holding periods from StockTwits (2010–2021)`. → **data as-of = June 2021**; nothing after June 2021 is in the source.
- **Universe / sample construction (Table 1, §2.1, all `source-reported`):** start from `180,556` quarterly earnings announcements for `5,419` I/B/E/S tickers → matched to CRSP on ticker + announcement date → `142,025` → filters (i) price 5 days before announcement > $5, (ii) SUE non-missing, (iii) pre-announcement price ≥ |forecasted EPS| and ≥ |actual EPS| → `130,496` → drop firm-quarters with multiple announcements in a quarter → `128,982` → drop those lacking abnormal returns over `[−30, 90]` → `123,880` firm-quarter observations (`5,383` tickers) → merge StockTwits activity in `[−90, −1]`: `51,065,435` posts by `693,965` users on `5,143` tickers → `117,389` announcements → restrict to users **self-reporting an investment horizon**: `20,605,979` posts by `132,958` users on `5,082` tickers → **final `104,919` earnings announcements** (analysis `N = 104,919` = `53,354` Long-Term + `51,565` Short-Term, Table 2). Universe = US listed common stocks with I/B/E/S earnings and CRSP prices. **No point-in-time index-membership rule, no liquidity/listing filter beyond the $5 price rule, and no delisting/survivorship treatment is stated anywhere in the source** → `data gap` / `underspecified`.
- **Transaction-cost / slippage / spread / funding / fill treatment (read §4 Methodology, §5.5 Trading Strategy, Appendix A robustness list, plus a keyword scan of the complete extracted text):** `transaction cost` 0, `bid-ask` / `bid ask` 0, `slippage` 0, `commission` 0, `borrow` 0, `short sale` / `shortability` 0, `liquidity` 0, `capacity` 0, `fee`/`fees` 0 (the single `fee` substring sits inside the word *feedback* in a reference title), `spread` 1 (the phrase `horizon-based spreads` in the Table 6 discussion — portfolio spreads, not bid-ask), `participation` 0, `market impact` 0, `turnover` 16 (all refer to the descriptive *institutional* turnover covariate, Table 2 note: `lagged churn rate calculated from holding changes between t−2 and t−1` of 13F firms — **not** strategy turnover). The term `zero-cost` appears 5× and means **self-financing long–short notation only**. Recorded as **`not stated in source` (`data gap`)** — the absence is an observation about the pinned v2 document, **not** an inference that costs are zero.
- **No code / replication package:** a full-text scan for `github`, `code is available`, `codes are available`, `replication` returned **0 hits** → reproducibility gap (`data gap`).
- **Pre-write deduplication (2026-09-23, whole repository, not `git log -20`):** identity index rebuilt over **910 tracked `*.md`** (524 distinct arXiv IDs, 870 DOIs, 2,865 URLs, 175 TradingView URLs, 24 SSRN IDs, 685 GitHub URLs) plus `coverage_manifest.csv`; `git grep` across **every tracked file** for `2512\.00280`, `Retail Investor Horizon`, `Vamossy`, `10\.48550/arXiv\.2512\.00280`, `StockTwits` → **0 hits for this source identity**, filename absent. The only `StockTwits` string in the repository is a passing future-work bullet in `crypto-cross-sectional-max-daily-return-lottery-momentum-2026-08-31.md` naming a *StockTwits/Augmento crypto sentiment index* — different platform usage, different source, different mechanism (crypto lottery momentum, not horizon classification). `git log --oneline -20` was inspected separately as a convenience glance only and does not substitute for the repository-wide search.
- **Material distinction from adjacent mechanism neighbors (dedup statement):** the repository already holds earnings-event records — `korea-pead-staggered-tranche-long-only-asymmetry-falsification-2026-09-13.md` (Korean PEAD, long-only staggered tranches, SUE-driven, different market and source), `earnings-announcement-premium-jump-risk-decay-falsification-2026-09-13.md` (unconditional hold-through-the-print premium, jump-risk study), `anomaly-pre-release-drift-predicted-signal-decile-portfolios-2026-09-23.md` (trading *before* the release using predicted anomaly ranks), and `earnings-call-speaker-weighted-sentiment-cross-section-2026-09-23.md` (speaker-role-weighted FinBERT sentiment on S&P 500). This record differs on at least one required dimension from each: **signal construction** (cross-sectional *retail-horizon composition* label, not SUE sign, not announcement presence, not transcript sentiment) and **material data dependency** (StockTwits user-profile self-reported holding period, a data field none of the above uses). It is a new source identity (`arXiv:2512.00280`).

## Economic mechanism

### Source-reported

The author's stated story: retail investors are not a monolith; their *investment horizon* determines how earnings news is processed. Users self-report a Holding Period on StockTwits (`day trader`, `swing trader` = short-term; `position trader`, `long-term investor` = long-term), so firms can be labelled by which cohort predominates. Announcements dominated by long-horizon investors show a **larger immediate reaction and pronounced post-earnings announcement drift** (underreaction / slow incorporation of fundamental news), whereas short-horizon-dominated announcements behave like **sentiment-driven overreaction**: elevated pre-announcement chatter precedes weaker subsequent performance and giveback (abstract, §1, §6.2). The paper formalises this in a rational-expectations model with horizon-differentiated investors (§3, simulation in Figure 2), argues that short-horizon posters emphasise technical cues (`break`, `target`) while long-horizon posters emphasise fundamentals (`EPS`, `financials`) (§1), and tests an **optimism-bias channel** in which above-median pre-announcement valence depresses the day 0–1 reaction and predicts negative drift, with the long-horizon label offsetting that reversal (§6.2, Table 7).

### Research interpretation

Falsifiable restatement: **the cross-sectional composition of retail attention conditions the speed of price discovery at earnings.** With news sign/size neutralised inside quarterly earnings-surprise bins, the wedge between long-horizon-dominated and short-horizon-dominated names should carry a positive abnormal-return spread over days `[2, 75]` and over the following month, because the long-horizon cohort underreacts (drift) while the short-horizon cohort overreacts (giveback). Component roles (`research interpretation`):

```text
Regime / conditioning: 11 earnings-surprise bins, breakpoints recomputed each quarter (neutralises news quality)
Primary signal: Long-Term vs Short-Term dominance label from StockTwits self-reported holding period over [−90, −1]
Confirmation variant (source, not required): bullish-only pre-announcement sentiment subsample (Figure 4b, Table 7)
Return construction: within-bin equal-weighted long LT − short ST, aggregate equal-weight across bins; FF5 adjustment with Newey–West (6 lags)
```

Competing explanation that must be tested rather than assumed away: the horizon label is **systematically correlated with firm characteristics** — Long-Term names are smaller (mean market cap 7,639.1 vs 18,477.2 $m), less volatile (0.023 vs 0.029), lower on institutional turnover (0.198 vs 0.270), covered by fewer analysts (6.7 vs 11.3), less dispersive (0.064 vs 0.101), and later in the sample (mean year 2016.8 vs 2014.8) (Table 2 Panel B). The reported FF5 alpha therefore has to survive size/attention/quality double-sorts before the horizon mechanism is credited (`research-defined falsification threshold`, below). The source itself concedes the label "may proxy for correlated firm characteristics such as attention or growth narratives" (§7).

## Signal

All items below are `source-reported` unless explicitly marked `research-proposed` or `underspecified`.

- **Horizon label formation:** count **unique StockTwits investors** who post about the ticker in the window **90 to 1 calendar days before the earnings announcement** (§2), split by profile Holding Period — short-term = `day trader` or `swing trader`; long-term = `position trader` or `long-term investor` (§2). Compute the share of long-term investors; **firms with a long-term share above 50% are designated predominantly long-term**, otherwise short-term (§2). Minor ambiguity carried as printed: the source phrases the denominator as "the total sample" rather than explicitly "LT + ST posters" → `underspecified` (denominator almost certainly LT+ST, but not stated verbatim).
- **Earnings surprise (Eq. 15):** `s_t,k = (e_t,k − ê_t,k) / p_t−5,k`, where `ê` is the **median I/B/E/S forecast made in the last 30 trading days** before the announcement and `p_t−5` is the share price 5 trading days before the announcement.
- **Surprise bins:** 11 groups — negative surprises into quintiles 1–5, zero surprise into bin 6, positive surprises into quintiles 7–11; **breakpoints determined separately each quarter** (§2.2, Figure 5 note). Positive surprises are roughly twice as prevalent, so bins 7–11 hold about twice the observations of bins 1–5; short-horizon announcements over-populate the extreme tails (quantiles 1 and 11, Table 2 Panel C).
- **Monthly trading rule (§5.5):** at the **end of month `t−1`**, identify all stocks with an earnings announcement (during `t−1`), assign each to one of the eleven surprise bins, and **within each bin go long stocks predominantly followed by Long-Term retail investors and short stocks predominantly followed by Short-Term retail investors**; each bin-level portfolio is **equal-weighted across firms**, and the aggregate strategy return is **the equal-weighted return across all stocks in all bins**; the portfolio is **rebalanced monthly** using the latest announcements and updated horizon classifications; returns are measured in month `t`.
- **Event-study construction (§4):** abnormal returns from a market model estimated on `[t−300, t−46]` (Eq. A1–A2); `CAR` summed in trading days (Eq. A3); `BHAR` on raw returns (Eq. A4); alternative expected-return models substitute FF3 / Carhart / FF5 factor sums (Appendix A.1, Tables 8–10). Event windows: `[0, 1]`, `[2, 75]`, `[0, 75]`, plus robustness `[2, 40]` and `[2, 60]` (Table 11).
- **Statistical protocol:** Table 4 dependent variables **winsorized at the 1st and 99th percentiles**; standard errors clustered by firm **and** by announcement day (Table 4 notes); Table 6 uses **Newey–West with 6 lags** on **136 monthly observations** — the exact monthly regression span is **not stated** (the documented window 2010-01 → 2021-06 would allow up to 138 months) → `underspecified`, recorded as printed.
- **Holding period / exit:** **no maximum holding period, no stop, no re-entry rule and no exit trigger is specified for the monthly strategy** beyond the monthly rebalance itself → `underspecified`. Treatment of a stock announcing more than once in the same month, or carrying two labels inside one month, is **not stated** → `data gap`.
- **Label stability (Table 3, `source-reported`):** Long-Term labels persist into `[0, 45]` / `[46, 90]` `72.2%` / `65.65%` of the time; Short-Term `77.09%` / `77.08%`; at firm level `70.1%` of Long-Term firms' announcements stay Long-Term and `69.0%` for Short-Term; **`73.63%` of firms switch label at least once** (11.27% always Long-Term, 15.10% always Short-Term).
- `research-proposed` operationalisations (none of these appear in the source): execute at the next session close after month-end formation with market orders; participation cap ≤ 10% of 20-day ADV; skip (hold cash) any name with < 95% data availability in the formation window; treat a missing label as "no position" rather than imputing.

## Required data

- **Instrument / universe:** US listed common stocks with I/B/E/S quarterly earnings announcements and CRSP daily returns; `$5` pre-announcement price floor; sample `2010-01` → `2021-06` (`source-reported`).
- **Venue / market type:** US cash equities (NYSE/AMEX/NASDAQ per CRSP); long-short on common stock — **no futures/options/perpetual component**.
- **Timeframe:** daily CRSP bars for event-time windows (trading days); **calendar-day** `[−90, −1]` lookback for the horizon label (the two clocks differ in the source and are recorded as printed); monthly portfolio formation/rebalance.
- **Fields:** I/B/E/S actual EPS, consensus median forecast (30-day lookback), announcement dates; CRSP prices, returns, market index, one-month T-bill; size, volatility, institutional ownership (13F quarter-end fraction), institutional turnover (13F lagged churn), abnormal short interest, analyst count, forecast dispersion, pre-event BHAR `[−30, −1]`; StockTwits messages with user identifiers, **profile Holding Period / Approach / experience level**, bullish-bearish tags and StockTwits sentiment score, likes, follower counts; message valence over `[−90, −1]` extracted with the Vamossy and Skog [2025] procedure (§2.2).
- **Point-in-time / availability:** `source-reported` that only users with **explicitly stated** trading styles are used (§2.1). **Not stated:** whether profile Holding Period fields are read as-of the message date or as-of the (later) download — a retro-fitted profile field would leak future self-description into the label → `data gap` / look-ahead risk **unaddressed by the source**. Post-June-2021 availability of the StockTwits self-report field is `not stated in source`.
- **Timestamps / timezone:** StockTwits timestamp timezone and the treatment of out-of-order or deleted posts are `not stated in source` → `data gap`; CRSP/I/B/E/S alignment follows standard US trading sessions (`source-reported` by implication of "trading day" event time).
- **Missing data:** announcements lacking abnormal returns over `[−30, 90]` and firm-quarters with multiple announcements are dropped (Table 1); **no imputation rule is stated anywhere** (`source-reported` by silence → `underspecified`).
- **Funding / fee / spread needs:** **not stated in source** (verified keyword scan above) — must be supplied by any replication as `research-proposed`.

## Execution assumptions

- **Signal-to-order timing:** formation at end of month `t−1` (`source-reported`, §5.5); **execution price (close of `t−1` vs next session), order type, fill model, latency, partial-fill and failure handling are not stated** → `data gap`.
- **Fees / spread / slippage / impact / capacity:** **`not stated in source` (`data gap`)** — no cost line exists in the pinned v2 document (keyword scan above). The reported alphas must therefore be read as **gross, with cost treatment unknown, not as zero-cost**.
- **Borrow / shorting:** the strategy shorts Short-Term-dominated names, which are the *larger*, higher-volatility, higher-turnover cohort (Table 2 Panel B). **Borrow availability, borrow fee, stock-loan recall and short-sale restriction handling are not addressed anywhere in the source** → `data gap`.
- **Leverage / margin:** `zero-cost` notation only; no leverage, margin or financing assumption is stated → `data gap`.
- **Turnover / capacity of the traded portfolio:** **strategy turnover is never reported** (the `Turnover` column in Table 2 is institutional 13F churn used as a covariate) → `data gap`; with monthly rebalancing of an event-driven, equal-weighted long–short whose long leg sits in smaller, less liquid names, turnover is the binding unknown.
- `research-proposed` fill assumptions for any future test: market orders at the next session close, no partial-fill modelling beyond the ADV participation cap listed under Signal, borrow fee charged on the short leg at a flat annual rate to be chosen at test time.

## Evidence

### Source-reported

Every figure below is `source-reported`, drawn **only** from arXiv `2512.00280v2` (SHA-256 `43a5fa9b…7cecc64b4`), each with its table/section anchor. These results have **not** been independently reproduced.

- **Table 6 — monthly FF5 regressions of the zero-cost horizon long–short, Newey–West with 6 lags, `Observations 136`:** Overall portfolio **α = 0.2948 %/month (SE 0.1223, p<0.05)**; Top-3-bin portfolio **α = 0.3810 %/month (SE 0.1363, p<0.01)**. Loadings, Overall: Mkt-RF **−0.1664 (0.0481, p<0.01)**, SMB 0.0561 (0.0760, ns), HML **0.2481 (0.0478, p<0.01)**, RMW **0.3280 (0.1126, p<0.01)**, CMA −0.1230 (0.1238, ns). Top-3: Mkt-RF −0.1732*** (0.0545), HML 0.2116*** (0.0510), RMW 0.3585** (0.1422), SMB 0.0465 ns, CMA −0.1773 ns. Bin-level α (Columns 3–13): Bin 1 −0.1039 (0.7572), Bin 2 −0.3288 (0.5837), Bin 3 0.3422 (0.4924), Bin 4 0.1595 (0.3070), Bin 5 0.2142 (0.3148), **Bin 6 0.8011 (0.4579, p<0.10)**, Bin 7 −0.0312 (0.1971), Bin 8 0.0735 (0.3208), **Bin 9 0.4784 (0.2163, p<0.05)**, Bin 10 0.3636 (0.3424), Bin 11 0.2998 (0.3587).
- **§5.5 prose (anchor: text around Table 6):** the overall portfolio delivers "an alpha of roughly **30 bps per month**", the Top-3-bin portfolio "nearly **40 bps per month**"; bin-level alphas are "mostly positive but imprecise", with **Bin 6 and Bin 9** the two standouts.
- **Abstract (anchor: abstract, p. 1):** "A zero-cost strategy exploiting this heterogeneity, going long on long-horizon stocks and short on short-horizon stocks, yields risk-adjusted alphas of **0.43% per month**." See Negative evidence — this abstract figure could not be located in any table or body text of v2.
- **Table 4 Panel A — immediate reaction, BHAR `[0, 1]`, winsorized 1/99, clustered SE (firm & day):** Column 1 (no controls/FE) **0.0053 (0.0005, p<0.01)**; Column 2 (full controls + firm & year-quarter FE) **0.0021 (0.0006, p<0.01)**; Column 3 (matching weights + FE) **0.0016 (0.0009, p<0.10)**; negative-surprise subsamples Column 4 **0.0045 (0.0010, p<0.01)**, Column 5 **0.0015 (0.0012, ns)**, Column 6 **−0.0002 (0.0017, ns)**; positive-surprise subsamples Column 7 **0.0052 (0.0007, p<0.01)**, Column 8 **0.0028 (0.0008, p<0.01)**, Column 9 **0.0035 (0.0012, p<0.01)**. Observations `104,919 / 104,703 / 75,080 / 33,722 / 33,155 / 24,820 / 63,395 / 62,977 / 43,751`.
- **Table 4 Panel B — delayed reaction, BHAR `[2, 75]`:** Col 1 **0.0283 (0.0022, p<0.01)**, Col 2 **0.0208 (0.0021, p<0.01)**, Col 3 **0.0161 (0.0028, p<0.01)**, Col 4 0.0277*** (0.0034), Col 5 **0.0181 (0.0039, p<0.01)**, Col 6 0.0137*** (0.0053), Col 7 0.0283*** (0.0025), Col 8 **0.0218 (0.0027, p<0.01)**, Col 9 0.0192*** (0.0037).
- **Table 4 Panel C — total reaction, BHAR `[0, 75]`:** Col 1 0.0341*** (0.0023), Col 2 0.0231*** (0.0023), Col 3 0.0181*** (0.0031), Col 5 0.0190*** (0.0042), Col 8 0.0256*** (0.0029).
- **Table 5 — by earnings-surprise group (Column-2 style specification):** Panel A `[0,1]` Long-Term coefficients across groups −5…+5 = `0.0007, −0.0024, −0.0010, −0.0017, 0.0019, 0.0056*, 0.0022, 0.0039**, 0.0033, 0.0053**, 0.0043*`; Panel B `[2,75]` = `0.0147, 0.0319***, 0.0208**, 0.0125, 0.0109*, 0.0190**, 0.0040, 0.0203***, 0.0270***, 0.0317***, 0.0252***` (prose range: **1.47 pp in the most negative bin to 3.17 pp in the +4 bin**); Panel C `[0,75]` = `0.0140, 0.0294**, 0.0198*, 0.0071, 0.0127*, 0.0253***, 0.0066, 0.0245***, 0.0306***, 0.0390***, 0.0311***`.
- **Figure 4 / §5.4 (anchor: Figure 4 panel (a) + prose):** the LT−ST cumulative BHAR "drifts only mildly during the first two trading weeks, but then accelerates sharply. Between trading days 20 and 75 the strategy earns an additional **three percentage points**" — **the source writes this as approximate prose with no table anchor** → recorded as source prose, not a table value. Panel (b): the drift appears **exclusively among bullish firms**, "with little to no effect for bearish firms" (§5.4).
- **Table 2 (sample split):** N = 104,919 full / 53,354 Long-Term / 51,565 Short-Term. Long-Term vs Short-Term means: market cap **7,639.1 vs 18,477.2** ($m, normalized difference −0.12, t −19.35), volatility **0.023 vs 0.029** (t −35.35), institutional turnover **0.198 vs 0.270** (t −43.98), institutional ownership 0.694 vs 0.706 (t −6.95), past 3-month return 0.024 vs 0.029, abnormal short interest ≈0 vs ≈0 (t −5.12), pre-announcement valence `[-30,−1]` **0.512 vs 0.537** (t −53.40), valence SD **0.072 vs 0.153** (t −143.84), mean year **2016.784 vs 2014.780** (t 107.50), SUE t −2.07, analyst count **6.706 vs 11.288**, forecast dispersion 0.064 vs 0.101.
- **Table 1 (sample funnel):** as listed under Provenance (180,556 → 142,025 → 130,496 → 128,982 → 123,880 → 117,389 → **104,919**; posts 51,065,435 → 20,605,979; users 693,965 → 132,958; tickers 5,143 → 5,082).
- **Table 3 (label stability):** as listed under Signal (72.2% / 65.65% / 77.09% / 77.08%; firm-level 70.1% / 69.0%; 73.63% of firms switch at least once).
- **Table 7 (optimism-bias mechanism):** above-median pre-announcement valence coefficients range **−0.31 to −0.73 pp** in `[0,1]`, **−1.89 to −4.90 pp** in `[2,75]` (p<0.01 in all but one case), **−2.65 to −5.42 pp** in `[0,75]`; the `Long-Term × Valence` interaction is positive and precisely estimated at **+1.29 to +3.25 pp** (Panel B), **+1.06 to +3.25 pp** (Panel C) and **+0.24 to +0.54 pp** (Panel A). Example coefficients, Panel A Column 2: Valence −0.0036*** (0.0008), `LT×Valence` 0.0034*** (0.0010).
- **Appendix robustness (as described in the source):** Tables 8–10 redo Table 4 with FF3 / Carhart / FF5 expected returns ("results are little changed"); Table 11 uses `[2,40]` and `[2,60]` windows ("point estimates and significance levels remain in line"); Table 12 varies propensity-score matching (5/10 neighbours, calipers 0.001/0.01/0.1); additional winsorization tests. **These appendix tables were read as present and described by the author; exact appendix coefficients are not reproduced here** → `underspecified` at coefficient level for this record.
- **§6.1 momentum control:** pre-event `[−30,−1]` BHAR series "move closely together, with the long-horizon group only marginally ahead", absorbed by the `[−30,−1]` return control.

### Independently reproduced

`not independently reproduced`.

### Negative evidence

Source-carried (all inside arXiv `2512.00280v2`):

1. **Abstract–table inconsistency (verified by full-text token scan):** the abstract's `0.43% per month` appears **nowhere else in v2** — the only other `0.43` string in the whole document is a `0.43 pp` regression coefficient in §5.3 (group +5). Table 6 reports **0.2948** (Overall) and **0.3810** (Top-3), and §5.5 prose says "roughly 30 bps" / "nearly 40 bps". The headline number is therefore **not traceable to any table or body passage in the pinned version** → recorded as printed, not reconciled.
2. **No immediate-reaction differential for negative news once controls/matching are applied:** Table 4 Panel A Column 5 `0.0015 (ns)` and Column 6 `−0.0002 (ns)` vs Column 8 `0.0028***` / Column 9 `0.0035***`; Table 5 Panel A shows all five negative-surprise groups insignificant. The optimism-bias/underreaction story is therefore **asymmetric in the immediate window** (§5.3 concedes this), even though the `[2,75]` drift survives on both sides (Col 5 `0.0181***`, Col 8 `0.0218***`).
3. **Bin-level alpha heterogeneity:** in Table 6 only Bin 6 (`0.8011*`, p<0.10) and Bin 9 (`0.4784**`) are significant; the rest cluster near zero with large SEs (e.g. Bin 3 SE 0.4924). The aggregate result leans on two of eleven bins and on aggregation across noisy bins.
4. **Modest statistical strength of the headline alpha:** Overall α `0.2948` with SE `0.1223` ⇒ t ≈ 2.41, significant only at the 5% level over **136 monthly observations**; no multiple-testing adjustment for the eleven bin-level regressions plus the Top-3 variant is reported → `data gap`.
5. **Strong factor tilts behind the alpha:** the Overall portfolio loads Mkt-RF −0.1664***, HML +0.2481***, RMW +0.3280*** — i.e. a defensive, value, profitability tilt; the "alpha" is the residual of a portfolio that is systematically long small-value-quality names and short growth names (§5.5 describes this as a "defensive profile").
6. **Label noise:** 73.63% of firms switch LT/ST at least once and Long-Term retention falls to 65.65% in `[46,90]` (Table 3) — the independent variable is unstable at firm level.
7. **Characteristic overlap / proxy risk (author's own caveat, §7):** horizon identification "relies on observational data from a single social media platform, which may proxy for correlated firm characteristics such as attention or growth narratives"; Table 2 shows the label is entangled with size, volatility, turnover, analyst coverage, sentiment valence and calendar time.
8. **Complete absence of cost, borrow, turnover and capacity treatment** (verified keyword scan above) despite a **monthly-rebalanced, equal-weighted long–short** whose long leg is in smaller names; `zero-cost` denotes self-financing only. Gross-vs-net status of the reported alphas is therefore `not stated in source`.
9. **Pre-existing pre-event momentum difference** (§6.1, Figure 5): the long-horizon group is "marginally ahead" over `[−30,−1]`; controlled for, but the trend is real and the control is a linear covariate, not a design fix.
10. **Sample ends June 2021** (Table 1, Figure 4/5 captions) — the window excludes the post-2021 meme/zero-commission regime entirely; no out-of-sample or post-2021 evidence exists in the source.
11. **No code or replication package** (0 hits for github/code/replication) → independent reproduction must be built from scratch, including re-deriving the horizon labels from raw StockTwits profile data.
12. **Date inconsistency:** manuscript title page `December 8, 2025` vs arXiv v2 stamp `4 Dec 2025` (Provenance).

External / adjacent leads (recorded as **leads only; no numbers taken from them**):

- Our own existing Wiki/staging record `quant/earnings-announcement-premium-jump-risk-decay-falsification-2026-09-13` (linked below) records, from `JonathanBeck1/falsification-campaign` at commit `79c3a2a…`, that an unconditional earnings-announcement premium failed its out-of-sample gate and that **plain SUE-conditioned PEAD was "evaluated and killed in T07"** in that campaign. **This Scout did not open T07's primary files**, so no statistic from it is imported here; it is flagged because it is direct contrary evidence against the *unconditioned* version of the drift this record conditions.
- Independent replication attempts of *this specific* horizon-conditioned construction: **none identified in the reviewed sources; absence is not evidence of no negative result.**

## Falsification plan

Each threshold below is a `research-defined falsification threshold`; each operational choice not in the source is `research-proposed`.

1. **F1 — Post-2021 out-of-sample replication (regime test).** Rebuild horizon labels and the monthly LT−ST-within-SUE-bin portfolio for `2021-07` onward (`research-proposed` window, same >50% rule, `[−90,−1]` calendar-day lookback, equal weights, monthly rebalance, next-session-close execution). *Fail if:* the aggregate FF5 α is ≤ 0 or has Newey–West |t| < 2 → the effect is treated as sample-bound to 2010–2021 and the record's hypothesis is rejected for the current regime.
2. **F2 — Cost stress (the source models none).** Re-run F1 net of per-side cost `κ ∈ {10, 20, 30, 50}` bps (`research-proposed` grid) including a short-borrow fee assumption. *Fail if:* net α ≤ 0 at `κ = 20` bps → the claim of an investable premium is rejected even if gross alpha survives.
3. **F3 — Label-shuffle placebo.** Within each bin-month, permute LT/ST labels 500 times (`research-proposed`). *Fail if:* the real α does not exceed the 95th percentile of the shuffled distribution (`p ≥ 0.05`) → the spread is attributed to portfolio construction noise rather than horizon.
4. **F4 — Confound ablation (size / attention / quality).** Double-sort or re-run with size, volatility, analyst count, forecast dispersion, institutional turnover, total StockTwits post count and calendar-year fixed effects. *Fail if:* the horizon indicator's coefficient drops below |t| = 2 → the label is a proxy for size/attention, and the mechanism claim is rejected even if raw spreads persist.
5. **F5 — Increment over plain PEAD (baseline/control).** Compare against an SUE-bin-only long–short with no horizon label (classic drift) on the same sample and windows. *Fail if:* the horizon overlay adds `< 10` bps/month of FF5 α (`research-defined`) over the SUE-only baseline → the horizon conditioning is redundant, and the record collapses into the ordinary PEAD family (which our own linked record reports was killed elsewhere).
6. **F6 — Data-availability gate (feasibility, not economics).** Measure StockTwits profile Holding-Period coverage in the replication window. *Fail if:* fewer than 95% of otherwise-eligible announcements receive a label (`research-defined`) → mark the hypothesis **untestable with available data** rather than failed or confirmed; do not fill the gap with imputation (imputation is not specified by the source).
7. **F7 — Mechanism-level asymmetry check.** Re-estimate Table 4/5 immediacy by news sign. *Fail if (mechanism variant):* the negative-news immediate differential becomes significant at |t| ≥ 2 and comparable in magnitude to the positive-news differential (`research-defined`) → the optimism-bias/underreaction story (which predicts no immediate differential under negative news) is materially weakened even if the portfolio α survives.
8. **Action on failure:** any of F1–F5 failing moves this record's practical status to *rejected-for-implementation* in a later review; F6 failing records a data blocker only; failures must be reported with the same table anchors used above.

## Crypto portability

**Portability classification: `unproven`.**

- **No direct mapping of the required data:** the mechanism is built on (i) quarterly EPS surprises versus a median analyst consensus (I/B/E/S) and (ii) a **self-reported holding-period field in user profiles**. Crypto assets have no I/B/E/S-equivalent consensus for most tokens, and the dominant crypto social surfaces (X, Telegram, Discord, farcaster-style feeds) do **not** expose a structured Holding-Period profile field → the primary signal variable does not exist as-is (`source-reported` absence; the source tests no crypto evidence whatsoever).
- **Event structure differs:** earnings are discrete, pre-scheduled, after-hours binary events producing overnight gaps; crypto trades 24/7 with continuous price discovery and liquidation cascades, so `[0,1]` / `[2,75]` trading-day windows and month-end formation do not carry over without redesign (`research-proposed`).
- **Short leg and financing:** shorting crypto perps introduces funding rate dynamics, isolated/cross margin, liquidation risk and venue-specific borrow — none modelled by the source (`research-proposed` risks, untested).
- **Possible adapted analogues (all `research-proposed`, untested, not evidence):** proxy horizon composition from on-chain holding-period distributions (entity-level holding time, coin-days destroyed) or from platform-native staking/lockup status; scheduled protocol events (unlocks, upgrades, fee-switch votes) as the "announcement"; token-team treasury reports or L1 ecosystem revenue disclosures as the surprise term. Because neither the data dependency nor the mechanism has been demonstrated in crypto, portability must be recorded `unproven`, not `adapted` or `direct`.

## Limitations

- `data gap` — **transaction costs, spread, slippage, commissions, market impact, borrow fees, capacity, portfolio turnover, order type, fill model, leverage/margin and latency are all absent from the source** (verified keyword scan), so the reported alphas are gross with unknown treatment; do not read them as net or as zero-cost.
- `data gap` — **borrow availability and shortability of the short leg are never discussed**, even though the strategy shorts the higher-volatility cohort.
- `data gap` — **point-in-time integrity of the StockTwits profile field is unaddressed** (retro-fitted profile self-description would leak); StockTwits timestamp timezone and deleted-post handling are unstated; strategy turnover is unreported.
- `underspecified` — no exit rule, no holding-period cap, no handling of multiple/overlapping announcements within a month, ambiguous label denominator ("total sample"), unstated monthly regression span behind Table 6's `Observations 136`, and appendix robustness described but not coefficient-extracted here.
- `not independently reproduced` — all numbers are third-party, single-author preprint claims (`preprint only`, arXiv v2, no journal_ref, no code release).
- Internal inconsistency — abstract `0.43%/month` versus Table 6 `0.2948` / `0.3810` and §5.5 "30–40 bps"; manuscript date `December 8, 2025` versus arXiv stamp `4 Dec 2025`.
- Identification — Long-Term vs Short-Term labels are entangled with size, volatility, analyst coverage, sentiment valence and calendar time (Table 2); fixed effects attenuate but do not eliminate the proxy concern (author's own §7 caveat); 73.63% of firms switch labels (Table 3); bin-level alphas are mostly imprecise; no multiple-testing adjustment.
- Sample / regime — US equities only, `2010-01` → `2021-06`, no post-2021 evidence, no delisting/survivorship treatment stated, no out-of-sample partition reported for the monthly strategy (the source's regression is single-sample).
- Source quality — single-author, non-peer-reviewed preprint with no replication package; publication bias and result-selection risk are unquantifiable.

## Implementation status

`implementation_status: not-implemented`.

Nothing has been implemented in our research stack: no label pipeline, no portfolio construction, no backtest, no Wiki Brain write, no candidate-pool entry, no Qlib run, and no Paper/Testnet/Live activity. This document is a normalized research capture of a third-party preprint only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

Presence of this record in the staging repository does **not** mean it passed Research Intake Review, entered Hermes Wiki Brain, entered the production candidate pool, completed Qlib full-backtest validation, became a frozen survivor or leaderboard entry, or is profitable / validated alpha / approved for implementation, paper trading, testnet or live trading. No wording, evidence count or confidence value in this record promotes it; any later adoption decision must be explicit, separately reviewed, and based on this record plus current sources.

## Related Wiki records

Links below were retrieved with `kb_search` on 2026-09-23 (no link is invented):

- `[[quant/earnings-announcement-premium-jump-risk-decay-falsification-2026-09-13]]` — records an independent pre-registered falsification of the unconditional earnings-announcement premium (and states plain SUE-conditioned PEAD was "evaluated and killed in T07"); direct adjacent negative evidence for the *unconditioned* drift family.
- `[[quant/news-event-tag-drift-rumor-resolution-placebo-adjusted-momentum-2026-09-02]]` — event-tag drift and placebo-adjusted abnormal-return dynamics across quantified disclosures.
- `[[quant/finsmart-market-aligned-reinforcement-learning-sentiment-alpha-2026-09-02]]` — social/media sentiment alpha whose own notes describe an ephemeral post-earnings drift component.
- `[[quant/crowd-trading-signals-social-media-crypto-short-term-predictability-2026-09-11]]` — the only other StockTwits-adjacent record (crypto crowd-trading via a Stockpulse database; different source, different market, different signal).
- `[[quant/strategy-research-record-spec-v1]]` — the canonical schema contract used for this record.

Adjacent records in this repository (distinct sources and mechanisms, listed for dedup traceability): `korea-pead-staggered-tranche-long-only-asymmetry-falsification-2026-09-13.md` (Korean SUE-driven long-only PEAD), `earnings-announcement-premium-jump-risk-decay-falsification-2026-09-13.md` (unconditional print-holding premium), `anomaly-pre-release-drift-predicted-signal-decile-portfolios-2026-09-23.md` (pre-release trading of predicted anomalies), `earnings-call-speaker-weighted-sentiment-cross-section-2026-09-23.md` (speaker-role FinBERT sentiment cross-section).

## Sources

1. Domonkos F. Vamossy, *Retail Investor Horizon and Earnings Announcements*, arXiv preprint `arXiv:2512.00280v2 [q-fin.PR]`. Landing page with full submission history (`[v1] Sat, 29 Nov 2025 02:10:22 UTC`; `[v2] Thu, 4 Dec 2025 22:35:24 UTC`), read 2026-09-23: https://arxiv.org/abs/2512.00280
2. Same work, pinned full text actually read for this record: `https://arxiv.org/pdf/2512.00280v2` — **57 pages, 1,120,030 bytes, SHA-256 `43a5fa9bfee0f76eb47b5576c4baf1f457f07d2e5b1fa2e90f34fb27cecc64b4`**, retrieved and parsed 2026-09-23; all sample, universe, cost-treatment and performance claims in this record come from this file with the section/table anchors given above.
3. DataCite arXiv auto-DOI (not a journal DOI): https://doi.org/10.48550/arXiv.2512.00280 — resolved HTTP 200 to the arXiv abs page on 2026-09-23.
