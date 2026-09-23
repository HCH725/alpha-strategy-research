---
schema: strategy-research-record-v1
title: "Bitcoin/Ether bubble-end crash timing with JLS–LPPL critical-time fits and PSY explosive-root dating (arXiv 2607.21826)"
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - bitcoin
  - ether
  - bubble-detection
  - lppl-jls
  - psy-explosive-root
  - crash-timing
  - regime-detection
status: research-only
confidence: medium
source_as_of: 2018-01-16
sources:
  - "Marco Bianchetti, Camilla Ricci, Marco Scaringi, 'Are cryptocurrencies real financial bubbles? Evidence from quantitative analyses', arXiv:2607.21826v1 [q-fin.RM; cross-lists econ.GN, q-fin.CP, q-fin.GN, q-fin.ST], submitted 23 Jul 2026 21:25:51 UTC. https://arxiv.org/abs/2607.21826 ; PDF 901,862 bytes, 14 pp., SHA-256 2dcc49b3e09c2ea7943c59d1035f100b09dda49f26a4a3a65fa023ee0ce9e29c, retrieved 2026-09-23. Abs-page journal-ref: a version published in Risk, 26 January 2018 (https://www.risk.net/comment/5388551/forecasting-crypto-crashes-with-bubble-analysis)."
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin/Ether Bubble-End Crash Timing with JLS–LPPL Critical-Time Fits and PSY Explosive-Root Dating

## Provenance

- **Primary source (identity):** Marco Bianchetti (Intesa Sanpaolo, Financial and Market Risk Management, *and* University of Bologna), Camilla Ricci (Intesa Sanpaolo, Financial and Market Risk Management), Marco Scaringi (Intesa Sanpaolo, Financial and Market Risk Management), *"Are cryptocurrencies real financial bubbles? Evidence from quantitative analyses."* Author line, order and affiliations taken verbatim from PDF p.1; corresponding author `marco.bianchetti(at)unibo.it`.
- **Version / date (abs page + PDF, both read 2026-09-23):** arXiv `2607.21826v1`, submission history `[v1] Thu, 23 Jul 2026 21:25:51 UTC (881 KB)`; Comments field: *"First version 23rd December 2017"*; PDF cover: **"First version 23rd December 2017 / This version 24th February 2018"**. Abs-page `journal-ref`: *"A version of this paper was published in Risk, 26 January 2018"* (https://www.risk.net/comment/5388551/forecasting-crypto-crashes-with-bubble-analysis). No arXiv DOI/journal DOI on the abs page (`doi` cell not present); no license cell present.
- **Primary-source checksum (pinned artifact read in full):** `https://arxiv.org/pdf/2607.21826v1` → HTTP 200, **901,862 bytes, 14 pages, SHA-256 `2dcc49b3e09c2ea7943c59d1035f100b09dda49f26a4a3a65fa023ee0ce9e29c`**, retrieved 2026-09-23. The arXiv `/html/` endpoint returns an "HTML not available" notice for this item, so **the entire methods and results sections (§3.1–§3.3, §4.1–§4.2, Table 1, §5) were read from that PDF** — every field below is cited to a PDF page/section. The Risk.net published version was **not opened this run → content equivalence between the 2018 Risk piece and this PDF is `data gap`.**
- **Field-by-field primary-source verification:** (a) complete author list exactly as above ✓; (b) version/date: arXiv v1 2026-07-23 wrapping a document last revised 2018-02-24 ✓; (c) sample period **1 December 2016 → 16 January 2018** (§3.3, §4.1, §4.2) ✓; (d) universe **BTC daily + ETH daily spot price series, two assets only** (§3.3, §4.1, §4.2) ✓; (e) transaction-cost treatment — **full-text keyword scan of all 14 pages**: `transaction cost` 0, `trading cost` 0, `slippage` 0, `bid-ask` 0, `commission` 0, `Sharpe` 0, `liquidation` 0, `rebalance` 0; the single `backtest` hit is the provenance of the *Sornette bounds* (§3.3: constraints "established through both mathematical considerations and backtesting on known past bubbles"), and both `fee` hits are the substring inside "feedback". **The source contains no trading rule and no backtest**, so cost modeling is `not applicable / not stated in source`; every cost assumption in this record is Scout-generated and labeled `research-proposed` (Scout observation of the pinned PDF, not author wording) ✓; (f) core performance numbers — **the source reports no P&L, Sharpe, CAGR, drawdown, hit rate or lead-time statistic of any kind**; its quantitative outputs are *detection dates, signal counts and confidence windows* (Table 1) plus prose descriptions of crash magnitudes (§4.1, §4.2) → all marked below with Table/§ provenance, everything else `data gap` ✓; (g) publication status — arXiv preprint of a 2018 working document with a Risk.net (trade press) journal-ref; **academic peer-review status `data gap / not stated in source`** ✓.
- **Repository-wide source-identity dedup (2026-09-23, ripgrep over ALL `*.md`):** `2607.21826`, the exact title *"Are cryptocurrencies real financial bubbles"*, `Bianchetti`, `Camilla Ricci`, `Marco Scaringi`, `LPPL`, `Sornette`, `Johansen, Ledoit`, `log-periodic`, `log periodic`, `PSY model`, `Phillips, Shi`, `super-exponential`, `datestamp.*bubble`, `Corbet`, `MacDonell`, `Financial Crisis Observatory`, `risk.net/comment/5388551` → **zero hits; this source identity is not in the repository.** `coverage_manifest` / `coverage_manifest.csv` not present.
- **Mechanism neighbors checked and confirmed distinct (each a different source + different signal):** `bitcoin-pi-cycle-top-bottom-moving-average-oscillator-2026-09-23.md` (moving-average ratio oscillator), `bitcoin-halving-clock-time-based-cycle-top-timing-2026-09-03.md` (calendar halving clock), `bitcoin-onchain-cumulative-value-days-destroyed-cvdd-floor-2026-09-01.md`, `bitcoin-onchain-market-cap-to-thermocap-ratio-2026-09-01.md`, `tradingview-bitcoin-metcalfe-active-address-deviation-2026-09-23.md` (on-chain / network valuation bands — different data dependency), `bitcoin-options-dealer-gamma-exposure-gex-regime-2026-09-01.md` (options-surface regime), `crypto-perpetual-liquidation-cascade-early-warning-taker-flow-variance-2026-09-01.md` (order-flow variance precursor, 5-minute leverage data), `sp500-statistical-arbitrage-johansen-ou-ablation-multiple-testing-2026-09-12.md`, `dynamic-johansen-deep-weighted-ensemble-cryptocurrency-pairs-2026-09-05.md`, `crypto-perpetual-pairs-trading-kalman-cointegration-falsification-2026-09-11.md` (**Johansen *cointegration* test — same surname family as Johansen-Ledoit-Sornette but a different object entirely: stationarity of a spread, not a super-exponential critical-point fit**). Materially distinct in at least **source identity, mechanism (endogenous super-exponential herding critical point / explosive-root regime dating vs price-ratio, on-chain, options or order-flow channels) and signal construction (rolling-window LPPL calibration + sequential ADF sup-statistic)**.

## Economic mechanism

### Source-reported

§3.1 states the mechanism directly: a positive bubble "lies in the unsustainable pace of the asset market price growth fed by self-reinforcing over-optimistic anticipation" — expectations of future earnings rather than present reality drive a divergence between market price and fundamental value; in a bubble regime the price "becomes unstable and very sensitive to exogenous factors, such as upcoming news with a negative consequence … that may lead to a collapse." Two detection traditions are then used side by side:

- **JLS / LPPL (agent-based / critical phenomena):** a bubble regime is "a super-exponential path generated by imitation and herding behaviour of investors and traders creating positive feedback," decorated by oscillations "describing instabilities generated by tension and competition between fundamentalists and noise traders," leading to "a finite-time singularity at some future critical time, interpreted as the forecast of a possible crash or rebound" (§3.1). The authors note the method is "regularly applied by the Financial Crisis Observatory at ETH Zurich" (§3.1, ref [29]).
- **PSY (statistical):** the Phillips–Shi–Yu sequential test "looks for a possible explosive behaviour of the time series" and "is able to give indications about the initial and final dates of a period of exuberance" (§3.1).

Prior crypto applications the authors build on (§3.2): MacDonell used JLS to forecast the 4 December 2013 Bitcoin crash; Malhotra et al. applied PSY sequential ADF to 2013–2014 BTC; Corbet et al. found BTC and ETH bubbles with PSY; Fantazzini et al. review Bitcoin modelling tools. Stated outcome (§5): the combined approach "consistently revealed strong bubble signals, often confirmed by actual crashes observed in the crypto-markets."

### Research interpretation

This is a **defensive / exit-timing hypothesis, not a cross-sectional alpha**: the source never converts its detections into a trade, so all operationalization below is `research-proposed`.

- **H1 (JLS channel, localization):** during a speculative episode the daily BTC/ETH price path is approximately a log-periodic super-exponential approach to a critical time *t_c*; a **cluster of Sornette-bounded valid fits** emitted at date *t* forecasts elevated crash hazard over the following days-to-weeks. Component role: *crash-time localization*.
- **H2 (PSY channel, regime):** a right-tail explosive-root regime (BSADF / BSADF* above its 95% Monte-Carlo critical value) dates the **on/off state** of exuberance; entering the state raises conditional crash risk, and its duration bounds how long a defensive tilt should stay engaged. Component role: *regime gate*.
- **H3 (conjunction — `research-proposed`):** JLS *and* PSY firing together (the source repeatedly reports them "coherently", §4.1, §4.2, §5) has higher precision than either alone.
- Named friction/behavioral channel: herding + positive feedback + finite liquidity into a rising market, then forced unwind when exogenous negative news arrives (the source attributes the Dec-2017/Jan-2018 crashes to "recurring negative news of China and South Korea regarding restrictions for cryptos", §4.1, §5). No cost channel is modeled by the source (see Execution assumptions).

## Signal

Source-reported items cite §3.3 / Table 1; anything else is `research-proposed` or `underspecified`.

- **Formation timestamp (source-reported):** for **each date** in the rolling sample the pipeline runs many calibrations: JLS uses a **fixed window length of 72 points for Bitcoin and 69 points for Ether**, moved forward with a **one-point step**; at each step **20 windows** are tested keeping the right extremum fixed and varying the left extremum (**52–72 points BTC, 49–69 points ETH**); each window is calibrated and the count of valid signals tallied (§3.3).
- **Validity filter (source-reported):** a countable "valid bubble signal" is a JLS fit satisfying the **"Sornette bounds"** — parameter constraints "established through both mathematical considerations and backtesting on known past bubbles" [29] (§3.3). The non-linear, oscillating fit is solved by **genetic-algorithm global optimization** rather than a local optimizer (§3.3).
- **PSY detector (source-reported):** ADF test statistic plus **Monte-Carlo simulation for the confidence levels**; two flavours, **BSADF and BSADF\***; multiple-time-window strategy "the same presented in [24], [32]" (§3.3). Figures 2–3 plot the statistic against the **95% critical value** (figure captions, pp.9, 11).
- **Reported output format (Table 1 caption, p.12):** JLS cells = **average signal date ± 1 standard deviation in days (number of signals)**; PSY cells = **time window and confidence level**, `(*) = 50–70% (low), (**) = 70–90% (medium), (***) = 90–100% (high)`.
- **Evaluation cadence implied by the source:** daily price series, recalibrated each day (§3.3). Exact clock/timezone of the "daily" close is **not stated → `data gap`** (BTC is a Bloomberg composite average, ETH comes from Etherscan — see Required data).
- **Trade rule: `underspecified` — the source specifies no long/short trigger, no exit, no holding period, no position sizing, no stop, no re-entry rule anywhere in §3–§5.** Illustrative operationalization, entirely **`research-proposed`**: at each daily close, flag BTC/ETH when (a) ≥ *K* valid JLS signals cluster within the last *W* days, and/or (b) BSADF has printed above its 95% critical value for *D* consecutive days; reduce/exit the long (optionally fade via perp) on the flag and re-enter when BSADF falls back below the critical value. **Values of *K*, *W*, *D*, cluster definition, sizing and re-entry buffer are all `research-proposed`** — the source fixes only the Sornette-bounds validity filter and the 95% PSY critical value.
- **Warm-up:** 72-point window ⇒ roughly the first ~72 daily observations cannot produce a full-length BTC fit (`research-proposed` reading of §3.3).
- **Ties / simultaneous signals / delistings / missing bars:** `data gap`.

## Required data

- **BTC:** daily USD price, **1 Dec 2016 → 16 Jan 2018**, source per paper: **Bloomberg `XBTUSD Curncy`**, "an average from the world's leading Bitcoin exchanges" (§4.1). Replicating with a free composite index is possible but is a **`research-proposed` substitution that changes source fidelity**.
- **ETH:** daily price, same window, source per paper: **Etherscan** (§4.2, described by the authors as "an exchange supplying daily prices" — quoted as written).
- **Fields actually used by the signal:** daily price only (the LPPL fit and the ADF statistic are price-series objects). Market caps, traded volumes, gold/EURUSD volatilities and BTC/ETH correlations appear only in the descriptive Figure 1 (Coinmarketcap, Bloomberg XAU/EURUSD sources) and are **not** inputs to either detector.
- **Point-in-time / availability:** no fundamental value is observable or used — "divergence from fundamental value" is an interpretation; both detectors are fit on price alone (§3.1–§3.3). No look-ahead beyond the rolling right extremum is described, but the exact as-of convention of each daily calibration is **`underspecified`** (whether date *t*'s close may enter the fit that labels date *t* is not stated).
- **Timezone / session / 24-7 convention:** `data gap`. **Missing-data / stale-bar policy:** `data gap`.
- **For any executable version (`research-proposed`):** daily candles on a single clock (or perp/futures OHLCV if the short leg is taken on a perpetual), plus fee/funding schedules — none of which the source uses.

## Execution assumptions

- **Source: none.** No order type, fill model, signal-to-order delay, latency, participation cap, leverage/margin, borrow, funding, capacity or failure handling is stated anywhere in the pinned PDF → **`not stated in source`** (full-text scan: 0 hits for transaction cost / trading cost / slippage / bid-ask / commission / Sharpe / liquidation / rebalance). The document's own disclaimer states it "is not intended to influence any investment decisions or promote any product or service" (PDF p.2).
- Because the source reports **detection dates only**, cost treatment for any tradable reading is entirely **`research-proposed`**: next-bar (daily-close signal → next session) market execution `research-proposed`; round-trip cost ladder **5 / 10 / 20 bps `research-defined falsification threshold`**; short leg via perpetual introduces **funding and liquidation risk absent from the source** (`research-proposed`).
- **No claimed capacity, no claimed fill rate, no claim of net-of-cost profitability exists in the source → `data gap`.**

## Evidence

### Source-reported

All figures below are `source-reported` (third-party claims), none reproduced by us; provenance = Table 1 (p.12), §4.1 (p.7), §4.2 (pp.9–11), §5 (p.12) of the pinned PDF.

- **Bitcoin JLS clusters (Table 1, Bitcoin row; columns OLS / GLS / MLE):** OLS **15Dec2017 ± 9 days (52 signals)** and **19Jan2018 ± 7 days (36)**; GLS **11Dec2017 ± 4 days (29)** and **23Jan2018 ± 4 days (15)**; MLE **14Dec2017 ± 3 days (50)**. *Column mapping method:* cells are emitted in the header order `OLS GLS MLE BSADF BSADF*` by the PDF text layer, and that mapping is independently corroborated for the Ether row by §4.2/§5 prose ("a second weaker signal is found by **JLS-GLS only** around 12th January 2018", which is exactly the date sitting in the second JLS cell of the Ether row).
- **Bitcoin PSY windows (Table 1):** BSADF **11Dec2016 – 06Jan2017 (`**` medium)** and **5May2017 – today (`***` high)**; BSADF* **21Mar2017 – 02May2017 (`**` medium)**. §4.1 prose: "PSY shows that the bubble period started in **May 2017** and is still alive in **January 2018**."
- **Bitcoin price paths the source says the signals anticipated (§4.1):** a first clear JLS signal group "around the half of December 2017, anticipating the large crash (**~30%**) observed in the second half of the month"; a second broader group anticipating "the other flash crash observed in the first half of January"; the early-September-2017 slump is quantified as "**~28% in two weeks**".
- **Ether JLS clusters (Table 1, Ether row):** OLS **12Jun2017 ± 2 days (6)**; GLS **12Jun2017 ± 3 days (6)** and **12Jan2018 ± 1 day (56)**; MLE **15Jun2017 ± 4 days (15)**. §4.2 prose: "All the three versions of JLS coherently find a bubble signal around **mid-June 2017**, corresponding to the crash observed on **12th June**", plus the weaker GLS-only 12Jan2018 signal.
- **Ether PSY windows (Table 1):** BSADF **26Feb2017 – 20Jul2017 (`***` high)** and **13Dec2017 – today (`**`)**; BSADF* **06Dec2017 – 14Mar2017 (`**`)** and **25Mar2017 – 23May2017 (`*` low)**. §4.2 prose describes "two distinct bubble periods, one in **March–September 2017**, and another one started in **December 2017 and still alive**."
- **Related magnitudes stated in prose (§4.2):** the Dec-2017 BTC ~30% crash caused "a limited **~20% Ether slump** lasting just a few days", with BTC/ETH correlation "nearly zero in that period"; ETH's December 2017 rally is called "the crazy rally of December 2017 (**~200%**)".
- **Method-reproduction claim (§3.3):** "For both JLS and PSY implementations, we could reproduce previous results available in the literature [31], [32]" (source-reported, no metrics given).
- **Not reported anywhere in the pinned PDF:** P&L, return, Sharpe, CAGR, maximum drawdown, turnover, hit rate, false-positive rate, alarm budget, lead-time distribution, out-of-sample split, multiple-testing correction, transaction costs → **all `data gap / not stated in source`.**

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **The source's own in-sample miss (§4.1):** "JLS does **not** reveal valid bubble signals around the slump observed in early September 2017 (~28% in two weeks)" — the authors attribute it to exogenous information (Chinese ICO restrictions). A ~28% two-week crash passed unflagged inside a 14-month sample: an admitted false negative on the very event class the mechanism claims to detect.
- **The PSY gate does not localize the exit:** BTC's high-confidence BSADF window starts **5May2017 and never closes within the sample** ("still alive in January 2018", §4.1), i.e. it is "on" for over eight months spanning both the run-up and the crash — as an *exit-timing* trigger it provides no date. Worse, the BTC BSADF* window **21Mar–02May2017 (Table 1) closes before the most dangerous phase**, so the two PSY variants disagree about when the exuberance ends.
- **Effectively one event per asset:** every BTC JLS confirmation clusters in **Dec 2017 – Jan 2018** and the ETH confirmations are **12Jun2017 + 12Jan2018** — the evidence base is ≈2–3 episodes, with no statistical power and **no accounting of how many non-crash dates also emitted valid signals** (Table 1 lists clusters, not the full alarm set → `data gap`).
- **No out-of-sample at all:** the dataset stops **2018-01-16**, chosen right after the last crash the paper cites; §4.1 itself concedes the second signal group anticipates crashes "and possibly other crashes in the future (we remind that our data set stops at 16th January 2018)" — i.e. the tail of the analysis is explicitly open-ended and untested.
- **Revision-timing caution (Scout reading of source-reported dates):** first version **23 Dec 2017**, this version **24 Feb 2018** — the January-2018 signal cells (19/23Jan2018, 12Jan2018) therefore belong to a revision written *after* those dates. In-sample honesty of the December clusters cannot be separated from hindsight without a frozen-2017-12-23 rerun (test 9 below).
- **Fitting multiplicity:** ~20 windows × ~410 daily steps × 3 JLS calibrations × 2 assets, plus sequential PSY, with **no multiple-testing / false-discovery control reported anywhere** (`data gap`); GA global optimization over a multi-modal LPPL surface adds researcher degrees of freedom that are not stress-tested (`research-proposed` concern).
- **Self-declared novelty:** "The JLS-GLS approach has been used in this work, **to our knowledge, for the first time**" (§3.3) — the calibration carrying the only January ETH signal is the least-established variant.
- **Publication/verification:** preprint of an 2018 industry document with a trade-press journal-ref; **not independently reproduced, not peer-reviewed as far as the pinned record shows** (`data gap`).

## Falsification plan

Thresholds not fixed by the source are labeled **`research-defined falsification threshold`**; operational choices are **`research-proposed`**.

1. **Point-in-time replication of Table 1:** rebuild daily BTC (Bloomberg-composite-equivalent) and ETH 2016-12-01→2018-01-16, run the frozen pipeline (window 72/69, 1-point step, 20 sub-windows, Sornette bounds, GA, ADF + Monte-Carlo 95%). **Fail** if the three BTC JLS clusters and the two ETH clusters do not reproduce within their reported ±s.d. (±9 / ±7 / ±4 / ±4 / ±3 / ±2 / ±3 / ±4 / ±1 days) (`research-defined`).
2. **Out-of-sample extension (H1/H2):** apply the frozen pipeline to 2018-01-17 → present for both assets. **Fail** if, at an alarm budget of **≤1 false alarm per asset-year (`research-defined`)**, the detectors catch **fewer than half of all ≥30% peak-to-trough drawdowns (`research-defined`)** or the median lead time over the crashes they do catch is **≤0 days (`research-defined`)**.
3. **Placebo / synthetic control:** run the identical pipeline on volatility-matched geometric-Brownian and on sign-shuffled daily series (200 draws, `research-proposed`). **Fail** if the real series' count of valid JLS clusters does not exceed the **95th percentile of the placebo distribution (`research-defined`)**.
4. **False-positive audit:** export *every* valid-signal date and *every* day BSADF sits above the critical value (not just Table 1 clusters). **Fail** if **fewer than 50% of flagged days are followed by a ≥10% drawdown within 30 days (`research-defined`)**.
5. **Multiple-fitting correction:** control FDR across all window fits and both detectors at **Benjamini–Hochberg q ≤ 0.10 (`research-defined`)**. **Fail** if the Dec-2017/Jan-2018 clusters do not survive correction.
6. **Ablation of the conjunction (H3):** compare JLS-only, PSY-only and the AND-rule on the same flagged-day table. **Fail H3** if conjunction precision does not exceed the better single detector by **>0 percentage points at equal recall (`research-defined`)** — i.e. PSY contributes no localization beyond JLS.
7. **Economic gate (only if converted into a trade, `research-proposed`):** daily-close signal → next-session execution, round-trip cost ladder **5 / 10 / 20 bps (`research-defined`)**. As a *defensive* rule the metric is avoided drawdown minus whipsaw cost: **fail** if cumulative avoided loss is **≤ the round-trip cost of the rule's own switches at 10 bps (`research-defined`)**, or net expectancy ≤0 at 20 bps → downgrade to non-tradable.
8. **Vendor robustness:** repeat with an independent BTC daily series (free composite instead of `XBTUSD Curncy`, `research-proposed`). **Fail** if any reproduced signal date shifts by **more than ±5 days (`research-defined`)** — the mechanism should not be vendor-specific.
9. **Revision-honesty check:** freeze inputs at **2017-12-23** (the source's own first-version date) and report what the pipeline could have signalled by then, separately from the Feb-2018 revision. **Fail the "real-time" reading** if the January-2018 cells are the only ones that survive exclusion of post-2017-12-23 information (`research-defined`).
10. **Action on failure:** any failed test downgrades the affected hypothesis to rejected; **no retuning** of window lengths, Sornette bounds, GA settings or critical values to rescue a failed threshold (retuning voids the test — `research-defined` anti-overfit rule).

## Crypto portability

**direct.** The source is itself BTC/ETH daily-spot research; no porting step is required. Crypto-specific risks still apply: 24/7 candles with an unstated timezone and two different data vendors (Bloomberg composite vs Etherscan close) whose daily boundaries may not align; fragmented "the price of Bitcoin" across venues; a crash gap can overshoot a fitted critical time *t_c* so the realized entry/exit price is worse than the signal date implies; the short leg needs perpetuals (funding, borrow and liquidation risk entirely absent from the source); the 72/69-point window is a fixed calendar lookback that may not match today's volatility clock; and the whole evidence base is one 2016–2018 regime of two assets. Portability ≠ authorization to trade.

## Limitations

- `data gap` — **no trading rule, no backtest, no P&L, no Sharpe/CAGR/MDD/turnover/hit-rate/lead-time statistics** in the pinned PDF; the source's quantitative outputs are detection dates and confidence windows only.
- `data gap` — transaction costs, fees, spread, slippage, impact, borrow, funding and leverage are **absent from the source** (full-text scan, Scout observation); any cost figure used later is `research-proposed`.
- `data gap` — timezone/session convention of "daily" closes, missing-data policy, exact as-of convention of each daily calibration, and the full alarm set behind Table 1's clusters.
- `data gap` — the Risk.net published version (26 Jan 2018) was not opened; equivalence with the arXiv PDF is unverified; academic peer-review status unknown.
- `underspecified` — all operational fields of a tradable rule (trigger direction, entry, exit, holding period, sizing, stop, re-entry) are **not specified by the source**; every value proposed here is `research-proposed`.
- `unproven` — sample ≈ 2–3 crash episodes across 2 assets, 14 months, no out-of-sample, no placebo, no multiple-testing correction, no independent replication (and none performed by us).
- `not independently reproduced` — every date, count, confidence band and crash magnitude is source-reported.
- Internal tension recorded: BTC BSADF runs 5May2017→end-of-sample while BSADF* ends 02May2017 (Table 1); §4.2 prose says an ETH bubble period runs "March–September 2017" while Table 1's BSADF windows are 26Feb–20Jul and 13Dec–14Mar — prose/table wording does not line up exactly.
- Publication-bias/selection: trade-press journal-ref, preprint posting in 2026 of a 2018 document, single institution (plus one university affiliation), disclaimer of investment purpose.

## Implementation status

`not-implemented.` No replication, LPPL/PSY calibration code, backtest, prototype or data pipeline exists in our research stack; nothing has been wired to Qlib, Paper, Testnet or Live. This record is normalized research material only.

## Adoption boundary

Presence in this repository does **not** mean: passed Research Intake Review, entered Hermes Wiki Brain, entered the production candidate pool, completed Qlib full-backtest validation, became a frozen survivor or leaderboard entry, profitable, validated alpha, or approved for implementation / paper / testnet / live trading. `status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

## Related Wiki records

- Real Wiki link (read-only this run; **no Wiki writes performed**): [[quant/strategy-research-record-spec-v1]]
- Filename neighbors below are **plain filenames, NOT Wiki links, and were not written or modified this run** — read only for dedup: `bitcoin-pi-cycle-top-bottom-moving-average-oscillator-2026-09-23.md` (MA-ratio top/bottom timing), `bitcoin-halving-clock-time-based-cycle-top-timing-2026-09-03.md` (calendar cycle timing), `bitcoin-onchain-cumulative-value-days-destroyed-cvdd-floor-2026-09-01.md`, `bitcoin-onchain-market-cap-to-thermocap-ratio-2026-09-01.md`, `tradingview-bitcoin-metcalfe-active-address-deviation-2026-09-23.md` (on-chain valuation bands), `bitcoin-options-dealer-gamma-exposure-gex-regime-2026-09-01.md` (options-driven regime), `crypto-perpetual-liquidation-cascade-early-warning-taker-flow-variance-2026-09-01.md` (flow-variance crash precursor), `sp500-statistical-arbitrage-johansen-ou-ablation-multiple-testing-2026-09-12.md` and `dynamic-johansen-deep-weighted-ensemble-cryptocurrency-pairs-2026-09-05.md` (**Johansen cointegration — a different object from Johansen-Ledoit-Sornette bubble fits**).

## Sources

1. Marco Bianchetti, Camilla Ricci, Marco Scaringi, *"Are cryptocurrencies real financial bubbles? Evidence from quantitative analyses,"* arXiv preprint `arXiv:2607.21826v1 [q-fin.RM]`, submitted 23 July 2026. Stable URL: https://arxiv.org/abs/2607.21826 . Abs page (authors, dateline, submission history, Comments, journal-ref, subjects) read 2026-09-23.
2. Full-text PDF of the same item: https://arxiv.org/pdf/2607.21826v1 — **901,862 bytes, 14 pages, SHA-256 `2dcc49b3e09c2ea7943c59d1035f100b09dda49f26a4a3a65fa023ee0ce9e29c`**, retrieved 2026-09-23; read in full (§1–§5, Figures 1–3 captions, Table 1 p.12, references). Every methods/performance statement in this record traces to §3.1–§3.3 (pp.5–7), §4.1 (p.7), §4.2 (pp.9–11), Table 1 (p.12) or §5 (p.12) of that PDF. arXiv `/html/` endpoint unavailable for this item.
3. Abs-page journal-ref (not opened this run; content equivalence `data gap`): Risk, 26 January 2018 — https://www.risk.net/comment/5388551/forecasting-crypto-crashes-with-bubble-analysis
4. Dedup anchors referenced above (existing repository records, read-only): the filenames listed in "Related Wiki records".
