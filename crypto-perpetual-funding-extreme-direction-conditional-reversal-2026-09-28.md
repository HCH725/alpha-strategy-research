---
schema: strategy-research-record-v1
title: "Direction-Conditional Reversal of Funding-Rate Extremes in Crypto Perpetual Futures: Conditional Arbitrage Capacity as a Second Limits-to-Arbitrage State Variable"
created: 2026-09-28
updated: 2026-09-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - funding-rate
  - extreme-event
  - mean-reversion
  - conditional-asymmetry
  - limits-to-arbitrage
  - event-study
  - walk-forward
  - transaction-cost-gap
status: research-only
confidence: medium
source_as_of: 2026-09-26
sources:
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7520320"
  - "https://dx.doi.org/10.2139/ssrn.7520320"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Reference-count conflict: SSRN landing shows heading '0 References' and side link '13 References' while the PDF reference list carries 14 entries - [1] to [11], one corrupted unnumbered entry between [4] and [5] rendering as 'Vishitem[Garcia Senyuma(2026)]...', a '[Shle7)] Shleifer and Vishny (1997)' entry, and '[13] Teruel-Gutierrez and Aparicio Serrano (2026)' with no [12] printed."
  - "Figure 2 versus Table 5 conflict: section 4.8 prints walk-forward out-of-sample Sharpe ratios 'for the baseline' of +9.33 (2023), +7.82 (2024), +12.77 (2025), -7.73 (2026), while Table 5's 'Baseline (no filter)' row prints 4.78 / 5.79 / 0.99 / -6.22; the +12.77 and -7.73 cells instead match the 'Online LR th=0.60' row, whose 2023 cell is printed NA, so no single printed row reproduces the figure."
  - "Up-only Sharpe provenance conflict: section 4.6 asserts up-only Sharpe ratios 'are positive in every year (7.28 to 15.94)' while Table 5 prints only pooled up-only values (9.93 / 10.34 / 8.33) and marks every yearly cell with an em dash, so the 7.28-15.94 range has no printed table provenance."
  - "Event-count conflict: Figure 3 prints yearly event counts 24 / 71 / 45 / 37 / 52 / 30 for 2021-2026 summing to 259, against the 274 events stated in section 3.2 and Table 1; Table 6's 'Exclude 2021' row (129 + 117 = 246) implies 28 events in 2021 and 'Exclude 2022' (98 + 100 = 198) implies 76 in 2022, both disagreeing with Figure 3's 24 and 71."
  - "Unresolved cross-references and corrupted citation labels in the pinned text: section 1 prints '(author?) (Shle7))' for the limits-to-arbitrage citation, section 3.2 prints 'Section ??' where the threshold sensitivity surface is promised, section 4.3 prints 'examined in ?)' for a companion study, and section 4.6's regime-robustness sentence relies on those same broken pointers."
---

# Direction-Conditional Reversal of Funding-Rate Extremes in Crypto Perpetual Futures: Conditional Arbitrage Capacity as a Second Limits-to-Arbitrage State Variable

## Provenance

- **Primary source:** Shek, Helvin. "Conditional Arbitrage Capacity: Evidence from Crypto Perpetual Funding Rates." SSRN working paper.
- **Canonical stable URLs:** landing `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7520320`; DOI `https://dx.doi.org/10.2139/ssrn.7520320`.
- **Author exactly as source:** "Helvin Shek", affiliation line "Independent" (landing and suggested citation both print "Shek, Helvin"); single author, no co-authors, no ORCID printed, no contact address printed.
- **Version / dates (all printed forms preserved, unreconciled):** PDF cover "September 24, 2026"; landing "Date Written: September 24, 2026"; landing "Posted: 26 Sep 2026"; landing "Last revised: 26 Sep 2026"; suggested citation "September 24, 2026". Landing shows "11 Pages".
- **Publication / peer-review status:** SSRN working paper. The landing prints no journal, no issue, no peer-review statement and no preprint banner, so publication and peer-review status are `not stated in source`.
- **License:** landing shows the Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) badge and link. Only printed values, section references and short quoted phrases are normalised here.
- **Landing statistics at read time (2026-09-28):** DOWNLOADS 8, ABSTRACT VIEWS 18, heading "0 Citations", heading "0 References" with side link "13 References" (see frontmatter contradictions).
- **Pinned PDF retrieval:** opened the landing page in a browser session on 2026-09-28, waited for the Cloudflare interstitial to clear, then used the landing "Open PDF in Browser" `Delivery.cfm` link (a stable non-expiring link; no presigned or session-bound URL is stored anywhere in this record): **200,669 bytes, 11 pages, SHA-256 `47ff03399015ae0a643d7e0f3bb3504a170ce82ce04cbdad28a6939d71c64421`**. Text was extracted in-session with pdf.js 3.11.174 to 24,669 characters across 11 pages, and **all 11 pages were read**, including the abstract, sections 1-6, Tables 1-6, Figures 1-3 captions, the reference list counted entry by entry, and the JEL block (G12, G14, G23, C58).
- **JEL / keywords:** G12, G14, G23, C58; keywords "perpetual futures, funding rates, limits to arbitrage, conditional arbitrage capacity, cryptocurrency".
- **Code / data availability:** the pinned text contains no code-availability, data-availability, replication-package or repository statement, and no GitHub/OSF/Zenodo link. Author-on-request availability is `not stated in source`.
- **AI / funding / conflict disclosure:** no AI-use disclosure, no funding statement and no competing-interest statement appears in the pinned text (`data gap`, not "none declared" - the sections are absent).
- **Dedup (pre-write, hidden-inclusive):** `rg -uuu -F` over the whole checkout including `.git/`, `.mimo-worktrees/`, `.agents/`, `.hermes/` and `coverage_manifest.csv` (1,088,787 bytes) for `7520320`, `10.2139/ssrn.7520320`, `ssrn.com/abstract=7520320`, `Helvin Shek`, `Conditional Arbitrage Capacity`, `conditional arbitrage capacity`, `274 events`, `+3.62`, `up-day` and `direction-dependent` returned **zero source-identity hits**; case-insensitive `Shek` hit only unrelated records (`r-and-d-intensity-spy500-...`, `crypto-cross-sectional-nearness-to-52-week-high-...`), case-insensitive `arbitrage capacity` hit only `stablecoin-depeg-primary-arb-...` and `anchored-currency-arbitrage-qubo-...`; positive control `novy-marx` returned 8 files in the same session. `git log --oneline -20` was used as a convenience glance only.
- **Four-axis distinction (source identity and mechanism differ in every pair):**
  - vs `crypto-perpetual-funding-rate-extreme-reversion-volatility-expansion-gating-2026-09-13` (GitHub `cybereow/crypto-market-microstructure` @ `34dbe408...`): that record's mechanism is a quantile crowding fade gated by cascading-liquidation regime drag and volatility expansion with an explicit maker-fill queue; this record's mechanism is a **direction-of-market conditioning state variable** (up-day reversion vs down-day continuation) with no liquidation or fill component, from a different source identity.
  - vs `extreme-negative-funding-contrarian-btc-return-2026-09-06` (AIJMR DOI `10.62127/aijmr.2026.v04i04.1493`): that source tests an **unconditional** contrarian funding-to-BTC-return link on one instrument; this source's entire claim is that the unconditional link is an artefact of averaging two opposite-signed conditional regimes, on three main coins plus a 13-coin extension.
  - vs `crypto-funding-rate-mean-reversion-ema-taker-filter-2026-09-11` (GitHub `Gotodataru/binance-futures-backtest` @ `5ed0d6e3...`): that signal is 8-hour funding mean reversion filtered by an EMA trend filter and taker-volume confirmation; this signal is an hourly z-score extreme event conditioned on the sign of the daily BTC return with a 24-hour horizon - different source, different signal construction, different conditioning variable.
  - vs `crypto-funding-carry-fade-turnover-cost-dissipation-falsification-2026-09-12`, `hyperliquid-funding-rate-contrarian-fade-pre-registered-null-2026-09-19` and `tradingview-oi-funding-zscore-extreme-reversal-2026-09-20`: each carries a different canonical source identity and none tests market direction as the conditioning variable, so the core hypothesis differs in signal construction and material data dependency.

## Economic mechanism

### Source-reported

The author's stated mechanism is a **second, direction-based state variable in the limits-to-arbitrage framework** ("conditional arbitrage capacity"), layered on top of the capital-level channel of Shleifer-Vishny and Brunnermeier-Pedersen. Extreme negative funding means the perpetual trades below spot and longs are compensated; arbitrage capital should push the deviation back. The paper's claim is that this absorption works **only when the market moves with the capital**: on up days the deviation reverts (mean +1.88% over the next 24 hours), on down days it continues (mean -1.74%), a +3.62pp gap that survives block bootstrap, conditional permutation, placebo events, threshold sensitivity, funding-payment adjustment, multiple-testing correction and a seven-shock exogenous event study. The author explicitly frames this as evidence that arbitrage effectiveness depends on capital level **and independently on market direction**, and states the practical reading directly: "extreme negative funding rates should not be treated as a universal buy signal" (section 5.3).

### Research interpretation

Hypothesised mechanism in falsifiable form: a **crowded-position / forced-flow state asymmetry**. Extreme negative funding marks a crowded short-perpetual (or long-spot-hedged) positioning state; when the broad market is rising, the crowded side is being stopped/margined out of a losing trade and its liquidation flow feeds the reversal, so the deviation mean-reverts; when the market is falling, the same crowded side is winning, no forced covering occurs, and the displacement keeps widening (continuation). The conditioning variable (daily market direction) is therefore a proxy for whether the crowded book is under or over margin pressure.

Component roles, preserved rather than collapsed:

```text
Event (source): hourly standardised funding rate < -1.85 sigma with prior hour > -0.5 sigma
Regime / conditioning (source): sign of the daily BTC return -> up day vs down day
Long leg (source-reported direction): up-day events, 24h forward return +1.88%
Short leg (source-reported direction): down-day events, 24h forward return -1.74%
Risk / exit / sizing: NOT specified by the source -> data gap
```

Alternative explanations the source itself raises and tries to reject: signal quality (online logistic-regression confidence conditioning) and latent regime (online infinite HMM, 3 regimes, direction effect positive in all three at +3.20 to +6.76pp). Both are reported as underpowered by the author (section 5.1), so they remain open. Note that neither test addresses a mechanical candidate explanation we consider live: the "up day" label may only be knowable after the daily close, i.e. potentially contemporaneous with (or after) part of the 24-hour measurement window - the source does not define the daily return's timestamp convention, so this is recorded as ambiguity, not as an established look-ahead defect.

## Signal

All items below are `source-reported` unless explicitly labelled `research-proposed` or `underspecified`.

- **Formation timestamp:** an hour `t` in which the standardised funding rate is below -1.85 standard deviations **and** the previous hour's standardised rate was above -0.5 standard deviations (section 3.2). The hourly timestamp convention, exchange timezone and whether the value used is the settled funding rate or an hourly premium/funding estimate are `underspecified` (the source says only "hourly perpetual futures data on Binance, obtained from the exchange's public REST API").
- **Standardisation window:** `underspecified`. The mean and standard deviation used to standardise, their lookback (rolling / expanding / full-sample), and whether they are computed per coin are never stated. The event rule therefore cannot be reconstructed exactly.
- **Lookback:** no prediction lookback beyond the one-hour prior-standardised-rate condition; the standardisation lookback is `data gap`.
- **Direction label:** sign of the BTC daily return (baseline, applied to every coin's events); robustness variants are the BTC 2-day direction and the ETH daily direction (Table 6). Whether "daily" is the current session or the previous session, and its close time, are `underspecified`.
- **Long entry:** up-day events are associated with a +1.88% mean 24-hour forward log return (Table 1/2). No entry price, order type or fill assumption is given - an explicit trade instruction is `research-proposed`: enter at the next hourly open after the event hour, long, exit at +24h.
- **Short entry:** down-day events are associated with a mean 24-hour forward log return of -1.74%; `research-proposed` mirror rule: enter at the next hourly open after the event hour, short, exit at +24h.
- **Exit:** fixed 24-hour forward horizon (event-study measurement). No stop, take-profit or early exit exists in the source; section 5.3 only remarks that down-day positions "require wider stops" without specifying one - stop rule `data gap`.
- **Holding period:** 24 hours, overlapping windows possible (the source acknowledges overlapping forward windows and clusters, using a 24-hour block bootstrap with an effective sample of 228 unique event days).
- **Re-entry / overlap handling:** `underspecified`.
- **Parameters:** event thresholds `-1.85 sigma` and `-0.5 sigma`, explicitly "chosen through a grid search to balance event frequency and signal strength" (section 3.2, in-sample selection, and the promised sensitivity surface is a broken `Section ??` pointer); online-LR confidence threshold `0.60` with a stated plateau over `0.50-0.625` (section 4.6, also selected on reported data); regime count `3` from the online iHMM.
- **Filter variants (source):** momentum (`mom_24h > 0`), low vol (below median), combo (low vol + positive mom), online logistic regression at thresholds 0.35 / 0.60, up-day-only variants of each.
- **Position sizing:** `data gap`. No sizing, leverage, margin, portfolio construction or capital-allocation rule appears anywhere in the 11 pages.
- **Reproducibility verdict:** the **conditional event-study claim** is precisely enough stated to attempt replication only after filling the standardisation and daily-direction conventions; the **tradable rule** is `underspecified` because entry price, order type, sizing, costs and the direction label's timestamp are all absent.

## Required data

- **Instruments / universe:** main sample Binance BTC, ETH, SOL perpetual futures (USD-M style contracts are implied but the contract type is never stated - `underspecified`); extended sample 13 coins over 2025-2026 (Figure 1 prints BTC, ETH, SOL, BNB, XRP, ADA, DOT, LTC, UNI, ATOM, AVAX, DOGE, LINK); plus spot prices for BTC, ETH and SOL for the spot-vs-perpetual check (section 4.7).
- **Venue / market type:** Binance only; perpetual futures (and matching spot), single venue, no cross-venue data.
- **Timeframe:** hourly bars, 49,488 observations per coin 2021-01-01 to 2026-08-31 (SOL 49,368 with two multi-day gaps in early 2022); daily return used for the direction label.
- **Fields needed:** hourly funding rate (or hourly premium series from which funding is standardised), hourly OHLC for the 24-hour forward returns, daily close-to-close returns for the direction label, funding settlement cash flows for the "net of funding" column, and (for the mechanism test) order-book depth, open interest, liquidation flow and arbitrage-capital proxies - the last four are explicitly unavailable to the author (section 5.3).
- **Point-in-time:** no publication-lag or revision discussion; funding settles every 8 hours while the event clock is hourly - the mapping between the 8-hour settlement grid and the hourly series is `underspecified`.
- **Timestamp / timezone:** `data gap` - no timezone, no daily-boundary convention, no treatment of out-of-order or missing hours (the SOL gaps are noted but their handling is not).
- **Missing data:** SOL's two multi-day gaps are reported; imputation or exclusion policy `data gap`.
- **Cost fields:** maker/taker fee, commission, slippage, bid-ask spread, market impact, participation, borrow, latency and turnover are **not observed, not modelled and not mentioned** anywhere in the pinned text (see Execution assumptions). The only cost-adjacent adjustment is "net of funding".

## Execution assumptions

**Source-level cost determination (Methods-level read, not an abstract-only judgment).** The pinned PDF's section 3 "Data and Empirical Design", section 3.2-3.3, all of section 4 (Results, including Tables 1-6 and Figures 1-3) and section 5 "Discussion" were read in full, and a whole-document word scan of the extracted 24,669-character text returned **zero** occurrences of: `transaction cost`, `cost`, `fees`, `fee`, `commission`, `slippage`, `bid-ask`, `turnover`, `latency`, `fill`, `market impact`, `maker`, `taker`, `limit order`, `market order`, `execution`, `backtest`, `order book`, `premium`, `transaction`. The word `spread` appears 3 times, all inside cited literature ("capture the spread", "tighter spreads and higher depth", "reduction in spot spreads"); `liquidity` appears 4 times, all as Brunnermeier-Pedersen funding/market-liquidity prose; `capacity` appears 11 times and is the paper's own term "conditional arbitrage capacity", not a capacity model; `leverage` and `margin` appear once each inside cited references; `stop` appears twice, once as "Hyperliquid backstop" and once as the unquantified section 5.3 remark about wider stops.

Consequences, all recorded as `data gap` and **never** as zero: order type, signal-to-order delay, same-bar vs next-bar execution, fill model, fees, slippage, spread, market impact, participation, capacity, leverage, margin, borrow, funding-cash-flow timing beyond the net-of-funding column, latency, partial fills and failure handling are `data gap`. "Net of funding" (Table 2: +1.91 / -1.68, gap +3.59pp) is the **only** cost-adjacent treatment in the paper.

**Research-proposed evaluation protocol (ours, not the source's):** enter at the next hourly bar open following the event, taker side, hold exactly 24 hours, equal notional per event, no leverage, with a fee/slippage ladder of 0/1/2/5/10 bps per side and the venue's 8-hour funding charged on the held leg; this is labelled `research-proposed` because the source specifies none of it.

## Evidence

### Source-reported

Every figure below is `source-reported`, has not been reproduced by us, and carries its Table/Figure/Section provenance from the pinned PDF (SHA-256 `47ff0339...c64421`).

- **Design (section 3.2, section 3.3):** 274 events main sample (143 up-day / 131 down-day), 532 events in the 13-coin 2025-2026 extension; baseline is a two-cell mean comparison `R_e = alpha + beta * Up_e + epsilon_e` on the 24-hour forward log return; block bootstrap with 24-hour blocks; effective sample 228 unique event days.
- **Table 1 (descriptives):** up-day mean +1.88%, SD 3.68%, positive fraction 0.741, n 143; down-day mean -1.74%, SD 4.74%, positive fraction 0.290, n 131; all events +0.15%, SD 4.59%, positive fraction 0.526, n 274; 13-coin +0.10%, SD 4.52%, positive fraction 0.513, n 532.
- **Table 2 (main result):** gap +3.62pp, block-bootstrap 95% CI [2.60, 4.67], conditional permutation p printed as `0.000`; net of funding +1.91 / -1.68, gap +3.59pp, 95% CI [2.55, 4.64].
- **Table 3 (seven-shock event study, +/-30-day windows):** Terra/LUNA 14 events (7/7) +6.39pp; FTX 11 (6/5) +12.12pp; USDC depeg/SVB 16 (8/8) +9.29pp; BTC spot ETF approval 7 (5/2) +1.42pp; yen carry unwind 20 (12/8) +5.91pp; Trump inauguration 14 (4/10) +3.35pp; market-wide liquidation 7 (2/5) +3.39pp; pooled 89 (44/45) +6.47pp with 95% CI [4.45, 8.86]; one-sided sign test p = 0.00781.
- **Table 4 (year-by-direction):** 2021 +0.57/-1.15 = +1.72pp; 2022 +1.84/-3.45 = +5.29pp; 2023 +2.84/-1.65 = +4.49pp; 2024 +1.81/-0.57 = +2.38pp; 2025 +1.88/-1.05 = +2.92pp; 2026 +1.03/-1.67 = +2.70pp; 12/12 sign test p = 0.000244, Bonferroni-adjusted threshold 0.00417.
- **Figure 1 / section 4.5:** all 13 coins show the same up-vs-down pattern, one-sided sign test p = 0.000122, Bonferroni-adjusted threshold 0.00385; the source concedes the 13 coins share a common market factor so the effective number of independent assets is smaller than 13.
- **Table 5 (out-of-sample Sharpe by method, columns 2023 / 2024 / 2025 / 2026 / Pooled):** baseline 4.78 / 5.79 / 0.99 / -6.22 / 2.04; momentum 7.38 / 8.06 / 1.26 / -10.02 / 4.06; low vol 8.53 / -2.98 / -0.42 / -8.20 / 1.69; combo 7.94 / 0.69 / 3.30 / -12.05 / 3.75; online LR th=0.35 4.78 / 5.56 / 2.30 / -6.22 / 2.47; online LR th=0.60 NA / 11.53 / 12.77 / -7.73 / 4.45; up-only rows print pooled only - momentum 9.93, low vol 10.34, combo 8.33.
- **section 4.6:** online LR th=0.60 pooled OOS Sharpe 4.45 (threshold plateau 0.50-0.625 gives 4.45-7.20), event-level Sharpe 3.11, described as the more conservative measure; online infinite HMM finds 3 regimes with 19 / 181 / 74 events, direction effect positive in all three at +3.20 to +6.76pp, triple-interaction coefficients -0.036 and -0.024.
- **section 4.7:** excluding FOMC / CPI / NFP release days the gap rises to +3.70pp; spot gap +3.94pp vs perpetual +4.00pp with correlation 0.999 between the two return series.
- **section 4.8 / Table 6:** 10 alternative specifications, all with a positive directional difference - baseline (BTC daily sign) 143 / 131 +3.62; BTC 2-day direction 116 / 158 +2.75; ETH daily direction 136 / 138 +3.06; tightened z < -2.5 67 / 62 +4.20; exclude 2021 129 / 117 +3.83; exclude 2022 98 / 100 +3.10; BTC only 52 / 52 +2.74; ETH only 43 / 43 +3.87; SOL only 48 / 36 +4.61; 13-coin pooled (2025-26) 225 / 307 +3.50; threshold sensitivity +3.94pp at z < -2.0, +4.18pp at z < -2.2, +4.20pp at z < -2.5; placebo of 274 randomly drawn hours gives mean gap +0.00035 against the observed +0.03617, which exceeds the 95th percentile of the placebo distribution (number of placebo draws `not stated in source`).
- **section 4.8 / Figure 2:** walk-forward out-of-sample Sharpe labelled "for the baseline": +9.33 (2023), +7.82 (2024), +12.77 (2025), -7.73 (2026), with the source's own sentence "The sign flip in 2026 is a stability concern, not a confirmation."
- **Figure 3:** event timeline 2021-2026 printing 24 / 71 / 45 / 37 / 52 / 30.
- **Overall claim (abstract, section 6):** the asymmetry "is structural rather than a signal-quality or regime-specific artifact" and is proposed as "conditional arbitrage capacity", a second state variable in limits to arbitrage.

### Independently reproduced

not independently reproduced.

Scout-side provenance and internal-arithmetic checks only (these verify that this record quotes the source consistently; they are **not** an empirical reproduction of the study):

- Landing read in a browser session on 2026-09-28 after the Cloudflare interstitial cleared; pinned PDF re-hashed in-session to SHA-256 `47ff03399015ae0a643d7e0f3bb3504a170ce82ce04cbdad28a6939d71c64421` (200,669 bytes, 11 pages); all cited headline literals were presence-checked programmatically against the extracted text with unicode-minus normalisation - only `1.85` "failed" because the PDF's justified text layer prints it as `1 . 85`, which is confirmed as the section 3.2 threshold.
- `143 + 131 = 274`; `104 + 86 + 84 = 274` from Table 6's BTC/ETH/SOL-only rows; `129 + 117 = 246`, so 2021 implies 28 events; `98 + 100 = 198`, so 2022 implies 76; `225 + 307 = 532` matches section 3.2's extended sample; Figure 3's yearly counts sum to **259**, disagreeing with 274.
- `(143 * 1.88 + 131 * -1.74) / 274 = +0.149` reproduces Table 1's "All events +0.15"; `1.88 - (-1.74) = 3.62`; `1.91 - (-1.68) = 3.59`; `0.741 * 143 = 106`, `0.290 * 131 = 38`, `144 / 274 = 0.526` reproduces the pooled positive fraction; Table 4 differences reproduce to the printed values except 2025 where `1.88 - (-1.05) = 2.93` vs printed `2.92` (rounding-level).
- Table 3 row counts sum to `14+11+16+7+20+14+7 = 89`, up `44`, down `45`; the count-weighted mean of the seven printed window gaps is **+6.41pp** against the printed pooled **+6.47pp** (0.06pp difference, consistent with pooling at event level rather than window level, but not verifiable from the printed table).
- Sign-test p-values reproduce as one-sided: `2^-7 = 0.00781`, `2^-12 = 0.000244`, `2^-13 = 0.000122`; Bonferroni thresholds reproduce as `0.05/12 = 0.00417` and `0.05/13 = 0.00385`; the placebo gap `0.03617` matches the headline `+3.62%` gap.
- Whole-document word-scan counts (0 for cost/fee/slippage/turnover/latency/fill/impact/order-type terms, 3 for `spread`, 4 for `liquidity`, 11 for `capacity`) were produced against the pinned text itself.
- SSRN landing, DOI resolution and the CC BY-NC 4.0 badge were read directly; no claim in this record comes from a search-result summary or secondary write-up.

### Negative evidence

1. The source's own most recent walk-forward year is negative: 2026 Sharpe -7.73 (Figure 2) / -6.22 (Table 5 baseline), which the author calls "a stability concern, not a confirmation" (section 4.8).
2. The baseline pooled out-of-sample Sharpe is only 2.04 (Table 5) - far below the 4.45 headline, which comes from a filtered online-LR variant whose 2023 cell is NA.
3. The 2025 baseline cell collapses to 0.99 and low-vol / combo filters are negative in 2024, 2025 and 2026 (Table 5), so filter choices are not stable across years.
4. No transaction cost, fee, commission, slippage, spread, impact, participation, turnover, latency, order-type or fill model appears anywhere in the pinned text (Methods-level read plus whole-document word scan: 0 occurrences) - every cost field is a `data gap`, never zero.
5. No sizing, leverage, margin, portfolio or capital-allocation rule exists in the source, so no Sharpe in the paper can be mapped to a stated book.
6. The 24-hour forward return is an event-study measurement, not an executable rule: entry price, order timing, direction-label timestamp and exit mechanics are all absent (`underspecified`).
7. The event threshold (-1.85 sigma, prior hour > -0.5 sigma) was "chosen through a grid search" on the same sample used for inference (section 3.2), i.e. in-sample threshold selection; the promised sensitivity surface is a broken `Section ??` reference.
8. The online-LR confidence threshold 0.60 was also selected on reported data with a stated plateau (0.50-0.625), adding a second tuned gate on top of the tuned event definition.
9. The standardisation of the funding rate is never defined (window, pooling, rolling vs full sample, settled-funding vs premium), so the event set cannot be reconstructed independently.
10. The daily-direction label's time convention is unstated, so it cannot be ruled out that part of the 24-hour forward window is used to define the conditioning variable - a direct threat to the headline gap.
11. Only 274 events over 68 months (roughly 4 per month) with 228 unique event days; the 24-hour block bootstrap does not obviously cover multi-day event clustering, and the source reports no heteroskedasticity-robust alternative for the headline gap.
12. The placebo reports a mean and a 95th-percentile statement but not the number of draws or the resampling design - the placebo is `underspecified`.
13. Multiplicity: Bonferroni is applied only to the 12-cell and 13-coin sign tests; the 10 robustness specifications, 5 threshold variants, 4 filters, 2 LR thresholds and 6 yearly cells are not jointly corrected, and `conditional permutation p = 0.000` is printed as an exact zero.
14. The seven "exogenous" shocks are hand-selected by the author, use +/-30-day windows, and two of them have tiny cells (BTC ETF 5/2, market-wide liquidation 2/5); the pooled windowed gap (+6.47pp) is nearly double the full-sample gap (+3.62pp), which is what window selection would produce.
15. The confidence and regime tests that carry the paper's "not signal quality, not regime" claim are explicitly described by the author as "underpowered ... suggestive rather than conclusive" (section 5.1).
16. Identification is observational for the full-sample estimate; the event study "does not deliver a clean causal effect" (source, section 5.3).
17. The mechanism variables (arbitrage-capital proxies, liquidation data, order-book depth) are not measured at all - the source states they require data "not available from public APIs at the required frequency" - so "conditional arbitrage capacity" is a label on a pattern, not a measured state variable.
18. The spot-vs-perpetual falsification is near-vacuous by the source's own admission: correlation 0.999 between the two return series "limits the power of this comparison".
19. Data provenance is thin: "hourly perpetual futures data on Binance, obtained from the exchange's public REST API" for 2021-2026 does not name an endpoint, field, or archival method, and Binance's public funding/premium history endpoints do not expose multi-year hourly history without an external archive - reconstruction path is a `data gap`.
20. SOL has two unexplained multi-day gaps (49,368 vs 49,488 hours) with no missing-data policy.
21. The 13-coin extension covers only 2025-2026 and shares one market factor; the source concedes the effective independent N is below 13.
22. Sharpe ratios of 4.45, 8-10 and 9-15.94 for a series with 4.59% event-level standard deviation and ~4 events per month are implausibly large under any standard annualisation, and the annualisation convention is never stated (`data gap`) - the event-level 3.11 is the only figure with a stated basis.
23. The up-only yearly Sharpe range (7.28 to 15.94) and Figure 2's "baseline" series have no matching printed table rows (frontmatter contradictions 2 and 3).
24. Figure 3's yearly event counts (sum 259) contradict section 3.2/Table 1 (274) and Table 6's implied 2021/2022 counts (28/76) (frontmatter contradiction 4).
25. Reference apparatus is corrupted: landing "0 References" heading, "13 References" link, 14 PDF entries, missing `[12]`, a garbled entry between [4] and [5], and body citations printed as `(author?) (Shle7))`, `Section ??` and `examined in ?)` (frontmatter contradictions 1 and 5).
26. Source-quality and independence: SSRN working paper by a single unaffiliated author, 0 citations, 8 downloads at read time, no peer-review statement, no code or data availability statement, no AI/funding/conflict disclosure sections in the pinned text - treat all performance figures as unreviewed third-party claims.
27. Related negative literature already in this repository: the cross-sectional funding-carry falsification records and the retail-microstructure funding-fade null both report funding-based edges failing after costs, so a funding-derived signal starting from zero cost accounting is presumptively fragile.

## Falsification plan

All thresholds below are `research-defined falsification thresholds` (Scout-chosen, not the source's), and all operational rules not printed in the source are `research-proposed`.

- **F1 - Event-set reproduction gate (`research-defined`).** Rebuild the event set from Binance hourly data 2021-01-01 to 2026-08-31 under at least three explicit standardisation conventions. Fail if no convention yields an event count within +/-15% of 274 **and** an up-minus-down gap within +/-1.0pp of +3.62. Failure action: classify the source as non-reproducible and drop the claim.
- **F2 - Direction-timing / look-ahead adjudication (`research-defined`).** Recompute the label using only information available at the event hour (previous-session close-to-close sign, or intraday-to-event-hour sign). Fail if the gap falls below +1.5pp or flips sign; failure action: attribute the headline gap to label look-ahead and reject the mechanism claim.
- **F3 - Implementable-rule gate (`research-proposed` rule, `research-defined` threshold).** Enter next hourly open, exit +24h, taker, equal notional, no leverage. Fail if the implementable up-minus-down gap is below +1.5pp or the up-day-only long has a negative mean after 1 bps per side.
- **F4 - Cost ladder (`research-defined`).** Apply 0 / 1 / 2 / 5 / 10 bps per side plus native 8-hour funding on the held leg. Fail if the up-day-only rule's mean 24-hour return is exhausted at 5 bps per side or if the conditional gap drops below +1.0pp.
- **F5 - Forward frozen test (`research-defined`).** Freeze the rule on 2026-08-31 and evaluate 2026-09-01 through 2027-08-31 out of sample, at least 40 new events. Fail if the mean 24-hour return on up-day events is <= 0 or if the gap's 95% block-bootstrap interval includes 0.
- **F6 - 2026 sign-flip adjudication (`research-defined`).** Extend the source's own walk-forward table through 2026-12-31. Fail (mechanism regime-limited) if 2026 remains negative on the baseline rule.
- **F7 - Standardisation sensitivity (`research-defined`).** Repeat with full-sample, expanding and rolling 90-day z-scores, and with settled funding vs hourly premium. Fail if the gap's sign flips in more than half of the variants.
- **F8 - Threshold surface (`research-defined`).** Evaluate z thresholds -1.5 / -1.85 / -2.0 / -2.2 / -2.5 with the prior-hour condition held fixed. Fail if any threshold produces a negative gap or if the monotone increase the source reports (+3.94 / +4.18 / +4.20) fails to reproduce within +/-0.5pp.
- **F9 - Placebo upgrade (`research-defined`).** At least 10,000 random-hour draws matched on hour-of-week and on multi-day event clustering, same statistic. Fail if the observed gap does not exceed the 95th percentile, or if the source's +0.00035 placebo mean cannot be reproduced within +/-0.001.
- **F10 - Dependence-robust inference (`research-defined`).** Re-run the headline gap with 72-hour and 168-hour bootstrap blocks and with a stationary bootstrap. Fail if no 95% interval excludes zero at the longer block lengths.
- **F11 - Cross-venue replication (`research-defined`).** Repeat on Bybit, OKX and Hyperliquid funding for BTC/ETH over the same window. Fail if the gap's sign does not hold on at least 2 of 3 venues.
- **F12 - Ablation of the conditioning variable (`research-defined`).** Compare the direction-conditioned rule against the unconditional long-after-extreme rule (the literature baseline already collected in this repository). Fail if conditioning improves the gap by less than +1.0pp, i.e. if direction adds nothing beyond the unconditional fade.
- **F13 - Competing-explanation control (`research-defined`).** Add the source's own momentum (24h), realised-volatility and same-window market-return controls in a single regression on the event panel. Fail if the `Up` coefficient falls below +1.0pp or loses significance, i.e. direction was a proxy for volatility or momentum.
- **F14 - Multiplicity control (`research-defined`).** Apply Benjamini-Hochberg at q < 0.10 across the full specification family actually searched (10 robustness specs x 5 thresholds x 4 filters x 2 LR thresholds x 6 yearly cells). Fail if the headline gap does not survive.

## Crypto portability

`direct` - the evidence is itself crypto perpetual futures (Binance BTC/ETH/SOL plus 11 further perpetuals) with matched crypto spot, so no porting step is required for the claim as stated.

Residual portability risks inside that direct setting: single-venue dependence (Binance only; funding grids, premium calculation and liquidation engines differ on Bybit/OKX/Hyperliquid); the 8-hour funding settlement grid against an hourly event clock and undefined daily-boundary timezone; venue fragmentation and index/mark-price conventions; per-contract notional, tick size and minimum-size constraints that the source never addresses; 24/7 sessions so "daily return" has no exchange-defined close; and liquidity/capacity, which the source does not measure at all (USD notional, depth and open interest are `data gap`).

## Limitations

- `underspecified`: standardisation window, hourly-series definition (settled funding vs premium), daily-direction timestamp, entry price, order type, sizing, stop, overlap/re-entry handling, annualisation convention behind every Sharpe.
- `data gap`: all cost, fill, latency, capacity, borrow, leverage and margin fields; all mechanism variables (arbitrage capital, liquidation flow, depth, open interest); missing-data policy; code/data availability; AI/funding/conflict disclosure.
- `not independently reproduced`: every performance, statistical and event-count figure in this record - we verified provenance and internal arithmetic only.
- `unproven`: the "conditional arbitrage capacity" state variable is an interpretation attached to an observed pattern, not a measured quantity; the source's own confidence/regime tests are declared underpowered.
- Sample: 68 months, 274 events, one venue, one direction-label definition, no pre-2021 period, extended cross-asset sample only 2025-2026, and a most-recent-year sign flip.
- Selection: event threshold and model threshold both grid-searched on the reported sample; seven hand-picked shock windows; no pre-registration and no untouched hold-out.
- Source quality: single-author unaffiliated SSRN working paper, 0 citations / 8 downloads at read time, no peer review, corrupted reference apparatus and several unresolved cross-references.
- Publication-bias concern: a null or negative conditional result would be unlikely to be posted in this form; the repo's related funding records already document post-cost failures in adjacent funding signals.
- This record is research material. It contains no independent validation, no backtest, no implementation and no trading approval.

## Implementation status

`implementation_status: not-implemented`. Nothing in this record has been implemented in our research stack: no event-set reconstruction, no signal code, no backtest, no Qlib run, no Paper, Testnet or Live activity, and no Wiki Brain ingestion. The `research-proposed` evaluation protocol above exists only as a falsification specification.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. The presence of this record in the staging repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. Any later adoption or implementation decision must be explicit, separately reviewed and based on this record plus current sources.

## Related Wiki records

Verified adjacent pages returned by a read-only Wiki Brain search this run (no page was written, and no page is linked that was not returned by the search):

- [[quant/crypto-funding-rate-mean-reversion-ema-taker-filter-2026-09-11]]
- [[quant/crypto-funding-carry-fade-turnover-cost-dissipation-falsification-2026-09-12]]
- [[quant/crypto-perpetual-alpha-four-cell-regime-falsification-2026-09-13]]
- [[quant/retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11]]
- [[quant/binance-perpetual-cross-sectional-momentum-taker-cost-falsification-2026-09-13]]

No Wiki Brain page for this specific source identity (SSRN 7520320) or for "conditional arbitrage capacity" was found; that absence is stated rather than filled with an invented link.

## Sources

- Shek, H. (2026). *Conditional Arbitrage Capacity: Evidence from Crypto Perpetual Funding Rates*. SSRN Working Paper. Landing: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7520320 (read 2026-09-28; Posted 26 Sep 2026; Last revised 26 Sep 2026; Date Written 24 Sep 2026; 11 Pages; CC BY-NC 4.0; 0 Citations; 8 downloads / 18 abstract views at read time).
- DOI: https://dx.doi.org/10.2139/ssrn.7520320
- Pinned PDF retrieved through the landing page's "Open PDF in Browser" delivery link on 2026-09-28 (stable non-expiring link; no presigned or session-bound URL retained): 200,669 bytes, 11 pages, SHA-256 `47ff03399015ae0a643d7e0f3bb3504a170ce82ce04cbdad28a6939d71c64421`; text extracted in-session with pdf.js 3.11.174 to 24,669 characters and all 11 pages read.
- Works cited inside the source that its empirical claims lean on (read as part of the pinned PDF's reference list, not independently consulted): Shleifer & Vishny (1997); Brunnermeier & Pedersen (2009); Daniel & Moskowitz (2016); Schmeling, Schrimpf & Todorov (2026, "Crypto carry"); Ruan & Streltsov (2022); Ackerer, Hugonnier & Jermann (2026).
