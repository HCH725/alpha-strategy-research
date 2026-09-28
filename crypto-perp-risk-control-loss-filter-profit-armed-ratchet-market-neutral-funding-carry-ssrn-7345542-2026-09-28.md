---
schema: strategy-research-record-v1
title: "Risk Control as the Durable Edge: Loss Filtering, Profit-Armed Ratchets, and Market-Neutral Carry When Direction Fails (SSRN 7345542)"
created: 2026-09-28
updated: 2026-09-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - risk-management
  - entry-filter
  - trailing-stop
  - funding-carry
  - market-neutral
  - permutation-test
  - negative-result
status: research-only
confidence: medium
source_as_of: 2026-08-26
sources:
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7345542"
  - "https://doi.org/10.2139/ssrn.7345542"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "SSRN landing author line prints 'Alexandr Dashyan' (Independent Researcher) while the PDF title block prints 'Aleksandr Dashyan, Independent Researcher, Yerevan, Armenia' with correspondence alikdashyan1@gmail.com; both spellings preserved, not reconciled."
  - "SSRN landing shows a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 (CC BY-NC-ND 4.0) badge while the PDF p.1 states 'Copyright 2026 Aleksandr Dashyan. All rights reserved' and forbids reproduction, distribution or quotation at length without prior written permission; licence conflict unreconciled, so only short printed values and section references are normalised here."
  - "SSRN landing heading prints '0 References' while the PDF reference list carries 18 numbered entries [1]-[18]; unreconciled."
  - "Four unreconciled date expressions: PDF cover 'Working paper. Preliminary. Comments welcome. This version: August 2026.'; landing 'Date Written: August 01, 2026'; landing 'Posted: 26 Aug 2026'; suggested citation '(August 01, 2026)'; PDF metadata /CreationDate D:20260824174353+04'00' (2026-08-24 17:43:53 +04'00')."
  - "Section 5.1 prose states 'Four of the five filters block sets that won more than that' (baseline 62.8 percent) and Table 1's verdict column marks R5 'cuts winners', but Table 1's own R5 row prints a blocked-set win rate of 58 percent (below the 62.8 percent baseline) and a kept ROI of +28.8 percent (above the +27.7 percent baseline), which by the paper's stated diagnostic means R5 removes losers and raises return; unreconciled internal misclassification."
  - "Table 1 caption says stacking 'removes 660 of about 1,100 trades' (fired calls) while section 5.3's permutation test is run on 'the 1,002 matured trades'; the two denominators are never reconciled in the text."
---

# Risk Control as the Durable Edge: Loss Filtering, Profit-Armed Ratchets, and Market-Neutral Carry When Direction Fails (SSRN 7345542)

## Provenance

- **Primary source.** SSRN preprint, `abstract_id=7345542`, DOI [`10.2139/ssrn.7345542`](https://doi.org/10.2139/ssrn.7345542). Landing page: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7345542>.
- **Exact titles.** Landing title: `Risk Control as the Durable Edge: Loss Filtering, Profit-Armed Ratchets, and Market-Neutral Carry When Direction Fails`. PDF title block: same title, with subtitle `What is left to engineer once the directional signal is a coin flip`.
- **Author (recorded exactly as each surface prints it; the surfaces disagree).** SSRN author line: **Alexandr Dashyan**, affiliation `Independent Researcher`. PDF title block: **Aleksandr Dashyan**, `Independent Researcher, Yerevan, Armenia`, correspondence `alikdashyan1@gmail.com` printed on p.1. The `Alexandr` / `Aleksandr` difference is a source-level discrepancy and is not reconciled here.
- **Dates (printed five ways; not reconciled).** PDF cover (p.1): `Working paper. Preliminary. Comments welcome. This version: August 2026.` Landing: `Date Written: August 01, 2026`, `Posted: 26 Aug 2026`, suggested citation `(August 01, 2026)`. PDF metadata `/CreationDate D:20260824174353+04'00'`, `/Creator Microsoft® Word 2024`, `/Producer Microsoft® Word 2024`, `/Author python-docx` (the PDF `/Author` field literally reads `python-docx`, which is a generation artefact rather than an author name and is recorded as printed).
- **Publication / review status.** SSRN working paper; the landing carries no journal, no issue and no peer-review statement and the PDF prints no peer-review banner, so peer-review status is `not stated in source`.
- **Licence (conflicting, unreconciled).** Landing shows a `Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International` badge; PDF p.1 states `Copyright 2026 Aleksandr Dashyan. All rights reserved.` with an explicit no-reproduction / no-quotation-at-length clause. Because the two surfaces conflict, this record normalises only short printed values, table cells and section references, and reproduces no extended passages.
- **Landing statistics read in a browser session on 2026-09-28** after the Cloudflare interstitial cleared (two reads): `26 Pages`, heading `0 References`, heading `0 Citations`, `DOWNLOADS 29 -> 32`, `ABSTRACT VIEWS 85 -> 86`.
- **Pinned PDF.** Retrieved 2026-09-28 through the landing's `Open PDF in Browser` delivery link (`https://papers.ssrn.com/sol3/Delivery.cfm/7345542.pdf?abstractid=7345542&mirid=1&type=2`, a non-expiring delivery object; **no presigned or session-bound URL is stored anywhere in this record**), **858,809 bytes, 26 pages, SHA-256 `ccf6d175dced6fc19879d1d2ac08d120ca117a4278c3d53665c95bbbe95e6e79`**, text extracted page by page with `pypdf 6.16.2` to **55,254 characters**, all 26 pages read including sections 1-11, Tables 1-4, the captions of Figures 1-11, the `Author Contributions and Use of AI Tools` block, the `Data and Code Availability` block, and the reference list counted entry by entry (18 entries, [1]-[18]). JEL classification printed on p.1: `G11, G17, C58, G14`. Keywords printed on p.1: `risk management, stop-loss rules, trailing stops, momentum crashes, funding carry, market-neutral, dollar-neutral, permutation tests, deflated Sharpe ratio, transaction costs, cryptocurrency perpetual futures, negative results`.
- **Companion works cited by the source with no identifier printed** (identity `not stated in source`): `Dashyan (2026a) Short-horizon directional non-predictability in cryptocurrency perpetual futures: a multi-method negative result under adversarial verification` (PDF ref [6]) and `Dashyan (2026b) Adversarial backtest verification: catching overfitting, beta, collinearity, and look-ahead in a live trading-research program` (PDF ref [7]), both `Working paper`. Whether either is one of the Dashyan papers already captured in this repository cannot be confirmed from the pinned text.
- **Source identity first pinned here.** This paper is already cited, without any identifier, as `Dashyan (2026c)` inside two existing repository records (`crypto-perp-llm-signal-backtest-to-live-gap-anatomy-2026-09-27.md` and `equity-index-tail-flush-reversion-disjoint-band-familywise-2026-09-27.md`). This is the first record to pin it to SSRN `7345542` / DOI `10.2139/ssrn.7345542` with a hashed PDF.
- **Deterministic pre-write source-identity dedup** (hidden-inclusive `rg -uuu` over the whole checkout, including `.git/`, `.mimo-worktrees/`, `.agents/`, `.hermes/` and `coverage_manifest.csv`): `7345542`, `ssrn.7345542`, `10.2139/ssrn.7345542`, `Risk Control as the Durable Edge`, `Durable Edge` (case-sensitive), `Profit-Armed Ratchet`, `Loss Filtering`, `arm-by-trail`, `blocked-set`, `when direction fails`  -  **all zero hits outside this record**; `when direction fails` and `loss filtering` hit exactly one file (the sibling 7353678 record, as the unidentified companion citation described above); case-sensitive `Durable Edge` zero; case-insensitive `durable edge` hits only unrelated prose plus those two Dashyan records. Author tokens `alikdashyan1`, `Aleksandr Dashyan`, `Alexandr Dashyan` hit only the same author's other two records (`7353678`, `7363482`). Positive control `novy-marx` returned 10 files in the same session. `coverage_manifest.csv` (1,088,787 bytes, last written 2026-08-31 and therefore stale) returns 0 for both `7345542` and `7353678`. `git log --oneline -20` was used as a convenience glance only and does not satisfy dedup.
- **Four-axis distinction against adjacent repository records** (source identity and mechanism differ in every pair):
  - `crypto-perp-llm-signal-backtest-to-live-gap-anatomy-2026-09-27.md` (SSRN `7353678`, same author): mechanism there is the anatomy of one directional signal's backtest-to-live gap; mechanism here is three explicitly non-predictive risk-control devices plus a market-neutral sleeve. Different source, different mechanism, same asset class.
  - `equity-index-tail-flush-reversion-disjoint-band-familywise-2026-09-27.md` (SSRN `7363482`, same author): different source, different market (US equity indices), different mechanism (tail-event reversion study).
  - `crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11.md` and `crypto-funding-carry-fade-turnover-cost-dissipation-falsification-2026-09-12.md`: **mechanism-family overlap** on the cross-sectional funding-carry side. Different source identities, but the carry sleeve in this paper belongs to the same economic family, so this record is explicitly **not** treated as independent confirming evidence for that family; the increment here is (a) the two risk-control mechanisms that are new to the repository, and (b) this source's own best-of-grid deflation, out-of-sample split and bootstrap accounting of the carry number.
  - `tradingview-btc-rsi-bollinger-mean-reversion-2026-09-17.md`: shares only the Bollinger vocabulary; there it is a mean-reversion entry signal, here it is a refusal-to-enter filter layered on an unrelated LLM directional book, with a permutation test on blocked trades.

## Economic mechanism

### Source-reported

The paper's premise is a negative one inherited from two unidentified companion papers: short-horizon direction in liquid cryptocurrency perpetual futures is not predictable out of sample, and most apparent directional edges are artefacts. What the paper then documents is three mechanisms that do **not** forecast the next move:

1. **A volatility-extreme entry filter (`R4`).** An entry filter only refuses to open a position. `R4` blocks a long when the one-hour Bollinger reading is above the upper band and blocks a short when it is below the lower band, on a standard 20-period, 2-standard-deviation band, on the reasoning that a call made at a stretched extreme is chasing a move about to snap back. Of five candidate filters tested, only `R4` blocks a set of trades whose win rate is below the book baseline. The paper's stated diagnostic is: a filter helps only if the set it blocks won less often than the 62.8 percent baseline.
2. **A profit-armed ratchet.** An account-level trailing stop that stays disarmed until equity has risen by an arm threshold, then trails a fixed percentage beneath a one-way high-water-mark that never steps back down. The stated behavioural rationale is that a mechanical rule enforcing hold-the-winners / refuse-the-losing-setup overrides the disposition effect (Shefrin and Statman 1985), and the paper situates the device between Kaminski and Lo (2014) on when stop-loss rules stop losses and Han, Zhou and Zhu (2016) / Barroso and Santa-Clara (2015) on taming momentum drawdowns without a new forecast.
3. **A cross-sectional dollar-neutral funding-carry sleeve.** Rank the coins by funding rate, go long the `n` lowest-funding names and short the `n` highest-funding names in equal weight at gross exposure 1.0, perps-only with no spot leg, harvesting the funding spread and fading the crowded names that high funding marks. The paper frames it as the carry family of Koijen, Moskowitz, Pedersen and Vrugt (2018) applied to perpetual-futures funding, competing directly with the cross-sectional momentum of Asness, Moskowitz and Pedersen (2013) and the time-series momentum of Moskowitz, Ooi and Pedersen (2012), with crypto frictions and segmentation from Makarov and Schoar (2020). It reports that momentum looked stronger in sample but did not survive the out-of-sample split, while carry kept its sign.

The paper is explicit that none of the three forecasts anything: `Two of the mechanisms defend a directional book ... the third earns a modest market-neutral return that does not lean on the book at all. None of it amounts to a strategy that reliably makes money.`

### Research interpretation

Component roles (normalised so each can be ablated later):

```text
Regime / entry gate:   refusal to enter when price sits at a stretched 1-hour Bollinger extreme (R4)
Primary signal:        NONE for mechanisms 1 and 2 - they are risk control layered on someone else's
                       directional book (an LLM policy's long/short calls on 20 Binance perps)
Risk / exit:           account-level profit-armed ratchet (arm threshold, then one-way high-water-mark trail)
Alpha candidate:       cross-sectional dollar-neutral funding carry: long low-funding / short high-funding,
                       equal weight, gross 1.0, rebalanced on a 1d/3d/7d grid
```

Falsifiable mechanism hypotheses (Scout interpretation, not source wording):

- **(a) Adverse selection at band extremes.** Entries taken when price is pinned at a Bollinger extreme are, on average, worse than entries taken elsewhere, because they chase an exhausted move; refusing them therefore removes losers rather than winners. Predicted signature: blocked-set win rate below baseline, monotone relation between band position at entry and trade outcome, and survival under a permutation null that re-draws the same number of blocked trades.
- **(b) Path-dependent give-back is harvestable without forecast.** A book whose equity curve front-loads gains and then bleeds has a predictable *shape* even when its direction is unpredictable; arming a trailing stop only after the run has begun converts that give-back into locked equity. Predicted signature: a plateau of arm/trail settings that beats no stop, with failure confined to trails tight enough to be hit by pre-run noise.
- ** (c) Funding as a positioning-pressure proxy.** Cross-sectionally high funding marks crowded longs whose subsequent price fade, plus the funding coupon itself, produces a market-neutral return stream. Predicted signature: positive coupon every year plus a larger, sign-unstable price-spread component; the sleeve should survive cost ladders but lose in low-dispersion regimes.

No component is assumed to contribute alpha; ablation of the three mechanisms is left to the falsification plan below.

## Signal

All three mechanisms are source-reported unless marked otherwise. Items the source does not state are marked `data gap` / `underspecified` and are never silently filled.

### Mechanism 1 - entry filter `R4` (and the four rejected filters)

- **Formation timestamp.** Computed from **one-hour** bars. The exact bar-close timestamp, timezone (exchange vs UTC) and the publication/availability lag are `data gap`; the paper states only that the resolver uses one-minute prices for trade outcomes.
- **Lookback / parameters.** `standard twenty-period, two-standard-deviation band` on the one-hour series. The price input (close vs typical/hl2), warm-up bars, and whether the band is computed on the last closed bar or a live bar are `data gap`.
- **Rule (source-reported).** Block a **long** when the one-hour Bollinger position sits **above the upper band**; block a **short** when it sits **below the lower band**. The filter never closes a position, only refuses an entry.
- **Breadth of the family.** Five candidate filters were tested (Table 1, p.7): `R1 BTC 2% reversal`, `R2 D1 trend conflict`, `R3 funding pay side`, `R4 BB extreme`, `R5 adaptive high-vol`. The definitions of `R1`, `R2`, `R3` and `R5` are **not** given in this paper (`data gap`; the paper points to the companion programme).
- **Effect sizes (source-reported, Table 1, symmetric geometry, trade level, June 2026).** Baseline (no filter) blocks 0, blocked-set win rate 62.8 percent (all trades), kept ROI at 5 percent sizing +27.7 percent. `R1` blocks 21 / 86 percent / +27.9 percent; `R2` 48 / 68 percent / +20.6 percent; `R3` 553 / 64 percent / +14.0 percent; `R4` 143 / 42 percent / +60.1 percent; `R5` 12 / 58 percent / +28.8 percent; all five combined 660 / 62.6 percent kept / +19.8 percent.
- **Account-level effect (source-reported, section 5.2 and Figure 2, native 2-to-1 geometry, 10 percent margin at 8x leverage).** Unfiltered 1,000 dollars to **1,132 dollars (+13.2 percent)** at a 59.8 percent win rate; `R4`-filtered to **1,878 dollars (+87.8 percent)** at a 64.5 percent win rate; worst drawdown **46.4 percent vs 60.5 percent**. On the flat symmetric bracket the same filter turns a **minus 17.9 percent** account into **plus 35.0 percent**. Table 1's kept ROI of +60.1 percent is explicitly **not** comparable to these account numbers (different sizing and geometry, as the paper states).
- **Permutation test (source-reported, section 5.3 and Figure 3).** 1,002 matured trades; `R4` would block 143 across all fired calls, of which 139 matured and enter the test; 20,000 draws each removing a random 139 trades. Null centre **+0.41 percent** (2-to-1) vs actual blocked-set **-0.25 percent**; symmetric geometry **-0.47 percent** vs null **+0.37 percent**; **no draw as extreme, permutation probability below 1 in 10,000** on both geometries.
- **Monotonicity (source-reported, section 5.4 and Figure 4).** Month's short trades sorted by one-hour Bollinger position at entry: band position below zero wins **48.3 percent** and loses **0.18 percent** on average; win rate rises through **70, 74, 85 percent** in the middle bands before easing at the very top.
- **Rejected alternative filter - the model's own confidence (source-reported, section 4).** Trades with stated confidence below 65 won **55.8 percent**; confidence 80 and above won **32.2 percent** and lost **0.72 percent** on average. Of the policy's eight `wait` conditions, **seven** blocked trades that would on average have won.
- **Underspecified.** Tie handling when several coins fire simultaneously, re-entry after a refusal, whether a refusal expires, and the position-sizing consequence of a refused entry are all `data gap`.

### Mechanism 2 - profit-armed ratchet

- **Formation timestamp / simulation granularity.** Account-level rule evaluated on the **daily-close simulated account curve** (the paper's own words: `none of which the daily-close simulation captures`). Whether the trail is marked on closes only or intraday is `data gap` beyond that statement; marked-vs-realised equity is named by the paper as an open live question.
- **Rule (source-reported, section 6.1).** Stay disarmed until equity has risen by an **arm threshold**; only then trail a fixed percentage beneath a **one-way high-water-mark that never steps back down**. After the stop fires the account is flat (no re-entry rule is given; `data gap`).
- **Parameters.** Grid = **7 arm thresholds x 6 trail widths** (Figure 6). Fixed setting used for the four-curve table = **arm +20 percent, trail 10 percent** (Table 2). Plateau result: `any arm of thirty percent or more with any trail, or any arm with a trail of eight percent or more, gives the same 2,926`; failure only at trail 5-6 percent combined with arm <= 20 percent, which locks **1,138** dollars instead.
- **Headline path (source-reported, section 6.2, Figure 5).** Filtered 2-to-1 book: 1,000 -> peak **3,461** on June 5 -> ends **1,878**; ratchet locks **about 2,926 (+192.6 percent)**, recovering **about 66 percent** of the roughly 1,600 dollars given back; a naive **6 percent** trail with no arming is stopped out by the routine **6.9 percent** dip on June 3 at **1,138 dollars (+13.8 percent)**.
- **Four-curve table (source-reported, Table 2, arm +20 / trail 10).** Filtered 2-to-1: peak 3,461, unmanaged end 1,878 (+87.8 percent), lock 2,926 (+192.6 percent), 66 percent recovered. Filtered symmetric: 2,755 -> 1,350 (+35.0 percent) -> 2,364 (+136.4 percent), 72 percent. Unfiltered symmetric: 2,281 -> 821 (-17.9 percent) -> 1,957 (+95.7 percent), 78 percent. Unfiltered 2-to-1: 2,869 -> 1,132 (+13.2 percent) -> **1,080 (+8.0 percent), whipsawed**.
- **Underspecified.** Whether the arm reference is start-of-book equity, prior high-water-mark or a rolling window is stated only as `equity has risen by a set amount`; commission treatment inside the ratchet path, minimum hold time, and interaction with the 95 percent capital cap are `data gap`.

### Mechanism 3 - cross-sectional dollar-neutral funding-carry sleeve

- **Formation timestamp.** Funding **signal lookback** of **1 day or 3 days** (Table 3); rebalance grid **1d / 3d / 7d**. The funding observation used (latest 8-hour print, average over the lookback, or realised accrual) is `data gap` - the paper says `ranks the coins by funding rate` without naming the exact field or its timestamp convention.
- **Rule (source-reported, section 3 and section 7.2).** At each rebalance rank the 20 coins by funding rate; long the `n` lowest-funding names, short the `n` highest-funding names; equal weight; **gross exposure held at 1.0** so the book is dollar-neutral and beta to Bitcoin sits near zero; perps only, no spot leg. Breadth `n` = **3 or 5** names per side. Top configuration = **1-day signal, breadth 3, 3-day rebalance**.
- **Parameters / grid (source-reported, Table 3, all 12 cells, six years, net of 5 bp fee + tiered slippage).** Lookback 1d/breadth 3: rebalance 1d **+0.86 / OOS +0.02 / MaxDD 42% / turnover 0.96**, 3d **+1.01 / +0.90 / 46% / 1.14**, 7d **+0.48 / +0.86 / 76% / 1.22**. Lookback 1d/breadth 5: 1d **+0.58 / +0.12 / 50% / 0.80**, 3d **+0.88 / +0.88 / 50% / 0.97**, 7d **+0.47 / +1.91 / 64% / 1.03**. Lookback 3d/breadth 3: 1d **+0.96 / +0.71 / 61% / 0.53**, 3d **+0.79 / +1.05 / 66% / 0.97**, 7d **+0.44 / +1.19 / 79% / 1.09**. Lookback 3d/breadth 5: 1d **+0.83 / +1.01 / 52% / 0.42**, 3d **+0.76 / +1.83 / 55% / 0.81**, 7d **+0.72 / +2.05 / 62% / 0.95**. Net Sharpes cluster **0.44 to 1.01** (re-verified from the printed table: min 0.44, max 1.01, n=12).
- **Competing factor (source-reported, section 7.1 and Figure 7).** Best cross-sectional momentum configuration (long 30-day winners, short losers): full-period **net Sharpe 1.27**, annualised **47.4 percent**, beta **-0.05**, **t-statistic 3.0**; its **in-sample Sharpe 1.60 collapses to 0.03 after the 2025 cutoff**, worst drawdown **97 percent**. Carry: full-period **1.01**, out-of-sample **0.90**.
- **Turnover.** Table 3 turnover column ranges **0.42 to 1.22** (per-rebalance units are `data gap`: the paper does not define the turnover units or annualisation).
- **Underspecified.** Universe list (the 20 tickers are never printed), listing/delisting handling, funding-field definition, rebalance price/time of day, treatment of partial rebalances when a name is missing, and the exact out-of-sample boundary date (section 7.1 says `after the 2025 cutoff` for momentum; the same date is implied for carry but never restated) are all `data gap`.

## Required data

- **Instruments / universe:** 20 Binance USDT-margined perpetual contracts; **identities not printed** (`data gap`). Same universe used by the directional book and by the carry sleeve.
- **Venue:** Binance (single venue) for both the directional evidence and the carry backtest; the paper names no other venue and no data vendor.
- **Market type:** perpetual futures only; carry is explicitly `perps-only, with no spot leg`.
- **Timeframes:** **1-minute** prices for first-touch trade resolution; **1-hour** bars for the Bollinger entry filter; **15-minute** prices plus realised funding for the six-year carry backtest (2021 through mid-2026); **daily closes** for the simulated account curve and ratchet.
- **Fields:** OHLCV at those resolutions; **funding rate** (realised) per coin; account equity, margin and leverage state; trade records with entry/exit prices, bracket levels, first-touch timestamps and win/loss flags. Order book, depth, trades/aggressor, open interest, options surface and borrow data are **not** used (`not stated in source` as requirements).
- **Point-in-time / availability:** `data gap` - the paper states no timestamp convention for funding publication, no look-ahead protection description and no train/test boundary dates beyond `after the 2025 cutoff` for the factor split and `2021 through mid-2026` for the carry sample.
- **Timestamps / timezone:** `data gap` - no timezone, clock source, alignment or out-of-order handling is stated for any of the four resolutions.
- **Missing data:** `data gap` - no null/stale/suspended/partial-bar policy is stated; no imputation is described (and none should be assumed).
- **External feature feed:** the directional side reads `a large multi-source snapshot of each coin` - vendor list, field list, snapshot cadence and availability lag are all `data gap`, so the directional book's inputs are not reconstructable from this paper.

## Execution assumptions

### Directional book and its two overlays (loss filter, ratchet)

- **Signal-to-order timing:** `data gap`. The paper does not state when a fired call becomes a position relative to its bar.
- **Resolution / fill model:** outcomes resolved on **one-minute prices by an independent first-touch rule** against fixed take-profit / stop-loss brackets. Two bracket geometries: **symmetric** (TP and SL the same distance, breaks even at a 50 percent win rate) and **asymmetric 2-to-1** (TP twice as far as SL, breaks even near a one-in-three win rate) - the 2-to-1 geometry is `the geometry the program traded live`.
- **Sizing / leverage (source-reported, section 3):** illustrative book simulated at **10 percent margin and 8x leverage** (a shade more aggressive than the companion papers' 5 percent and 7 times), **95 percent capital cap**, **at most one open position per coin**, compounding from **1,000 dollars** over **June 2 to June 29, 2026**. Table 1's kept ROI column is instead at the companion sizing of **5 percent margin** on the symmetric geometry.
- **Fees:** **flat 0.1 percent round-trip fee** on the directional side (only friction modelled there).
- **Slippage / spread / latency / gaps / impact:** **not modelled** for the directional side. Word scan of the pinned text: `bid-ask` 0, `latency` 0, `limit order` 0, `market order` 0, `execution` 0, `order book` 0, `premium` 0, `commission` 0. Slippage appears only (i) as an acknowledged live gap for the ratchet (`a live trailing stop faces slippage on the stop itself, gaps through the stop level`), and (ii) as the carry sleeve's explicit model.
- **Order type:** `data gap` - the paper never states market vs limit, and never states whether entries are same-bar or next-bar.
- **Live status:** `The ratchet and loss filter are studied on simulated account curves, not live fills`; a live-vs-backtest reconciliation is `left to follow-on work`.
- **Ratchet-specific:** marked vs realised equity is named as an open operational question (`data gap`).

### Carry sleeve

- **Cost model (source-reported, section 3, section 7.2, section 7.5):** net of a **5 basis point taker fee** plus a **per-coin tiered slippage estimate**; the realistic tiered estimate is stated as **about 5 to 6 basis points per side**; a **maker fee of 2 basis points** instead of the taker 5 lifts net Sharpe from **1.01 to 1.12**; breakeven sweep runs **0 to 30 basis points per side** on top of the fee, with annualised return positive across the whole sweep and **out-of-sample Sharpe positive out to about 15 bp (roughly 0.3) and crossing zero near 20 bp**. The **tiered schedule itself is not printed** (`data gap`).
- **Not modelled:** `capacity ... is not modeled here` and `neither models market impact at size nor the capacity limit` (section 7.5, section 10). Borrow/short-borrow fees, margin financing, funding **paid** on the short leg as a cost line, order type, fill timing, partial fills and latency are all `data gap` (the funding differential itself is the signal and the coupon, and the paper does not decompose it into a cost line).
- **Gross / leverage:** gross exposure held at **1.0** (dollar-neutral); no leverage or margin statement for the sleeve (`data gap` beyond gross 1.0).
- **Rebalance cadence:** 1d / 3d / 7d grid; the headline cell rebalances every **3 days**.

## Evidence

### Source-reported

Every figure below is a third-party claim from the pinned PDF and is **not** independently reproduced. Provenance is given as section / table / figure of the pinned 26-page version.

- **Setting (section 3):** 20 Binance USD-margined perpetuals; an LLM policy issues long/short calls with stated confidence; 1,002 matured calls in June 2026 (of roughly 1,100 fired); trade level vs account level explicitly separated by the paper.
- **Direction is the wrong lever (section 4):** almost all of the book's return is earned June 2-5 while the market fell and the short-leaning book collected beta; after June 6 the win rate is `indistinguishable from a coin flip`. Confidence anti-predictive: <65 confidence **55.8 percent** win rate, >=80 confidence **32.2 percent** and **-0.72 percent** average; **7 of 8** policy wait-gates blocked winners.
- **Entry filter (Table 1, sections 5.2-5.5, Figures 1-4):** baseline win rate **62.8 percent**; `R4` blocked set **42 percent** and **-0.39 percent** average; `R4` account **+13.2 percent -> +87.8 percent**, worst drawdown **60.5 -> 46.4 percent**; symmetric bracket **-17.9 percent -> +35.0 percent**; permutation p **< 1e-4** on both geometries (0 of 20,000 draws as extreme); monotone band-position relation with the losing bucket at **48.3 percent** / **-0.18 percent**; June 20-29 sub-window the filtered book still loses **-25.8 percent** vs **-40.6 percent** unfiltered.
- **Profit-armed ratchet (Table 2, sections 6.2-6.4, Figures 5-6):** peak **3,461**, unmanaged end **1,878**, lock **2,926 (+192.6 percent)**, **66 percent** of the give-back recovered; naive 6 percent trail locks **1,138 (+13.8 percent)**; plateau identical across most of a 7x6 grid, failing only in the tight-trail/low-arm corner; four-curve table as listed above, including the **whipsaw** on the unfiltered 2-to-1 curve (**1,080 vs 1,132**).
- **Carry sleeve (Table 3, sections 7.1-7.7, Figures 7-10):** six-year (2021 - mid-2026, 15-minute data) headline configuration **net Sharpe 1.01**, annualised **39.1 percent**, **out-of-sample Sharpe 0.90**, beta to Bitcoin near zero, **MaxDD 46 percent**, turnover **1.14**; 12-cell grid net Sharpes **0.44-1.01**; momentum comparison **1.27 net / 47.4 percent annualised / beta -0.05 / t 3.0**, in-sample **1.60 -> 0.03 OOS**, worst drawdown **97 percent**; year-by-year decomposition with the funding coupon **6 to 15 percent a year, positive in all six years**, and the price spread **+136 percent in 2021**, **+37 to +39 percent** in the two good recent years, **-19, -23, -29 percent** in 2022, 2023 and 2026; **negative in three of six calendar years**; cost sweep positive across **0-30 bp**, OOS Sharpe zero-crossing near **20 bp**, maker-2bp variant **1.01 -> 1.12**.
- **Selection and serial-dependence accounting (section 7.6):** best-of-12 expected Sharpe under pure selection **about 1.06** versus observed **1.01** (the paper calls this comparison deliberately harsh because the cells are correlated); stationary block bootstrap (blocks of about four days) gives Sharpe **1.01** with **95 percent interval 0.11 to 1.89** and probability of a non-positive Sharpe **about 1.2 percent**.
- **Favourable-window mirage (section 7.7):** on 2024-2026 with 5 names a side rebalanced weekly the same construction shows **net Sharpe 1.62** and **worst drawdown 11 percent**, versus the six-year headline's **46 percent** drawdown; the paper explicitly says the six-year number is the one to believe.
- **Non-complementarity (section 8, Figure 11):** over the exact June window in which the ratchet was locking a windfall, the carry sleeve ended **-4.4 percent**; the paper concludes the two are not reliable hedges for each other.
- **System ceiling (Table 4, section 9):** three mechanisms side by side - loss filter `+13.2% to +87.8%`, ratchet `about $2,926 (+192.6%)`, carry `Net Sharpe 1.01 over six years, OOS 0.90, bootstrap CI 0.11 to 1.89` - with the paper's own statement that the combination is `a bounded, deployable structure rather than an edge that prints`.
- **Cost treatment summary (Methods-level read of sections 3, 5, 6, 7.5 and 10 plus a full-document word scan of the pinned text):** directional side = flat **0.1 percent round-trip fee only**; carry side = **5 bp taker fee + per-coin tiered slippage (~5-6 bp/side) + 0-30 bp breakeven sweep + 2 bp maker variant**; `transaction cost` appears **2** times (keywords, section 7.5), `transaction costs` **1** (Novy-Marx and Velikov prose), `fee` **10**, `fees` **2**, `slippage` **11**, `maker` **1**, `taker` **2**, `round-trip` **1**, `capacity` **3**, `market impact` **1** (the sentence saying impact is *not* modelled), `turnover` **2**, `leverage` **2**, `margin` **5**; `commission` **0**, `bid-ask` **0**, `latency` **0**, `fill`/`fills` **1+1** (both in `not live fills`), `limit order` **0**, `market order` **0**, `execution` **0**, `order book` **0**, `premium` **0**; `borrow` **2** and both are the idiom `borrowed wholesale` / `borrowed from the companion paper`, i.e. **zero occurrences of borrow as a financing cost**. Anything not covered by those models is `data gap`, never zero.
- **Reproducibility apparatus (Data and Code Availability):** two deterministic scripts (plus a third for the favourable-window configuration) reproduce every number; data, scripts and figure code are `available from the author on reasonable request, subject to the terms of the third-party data sources`, with `a companion code repository in preparation` - **no public repository URL, no commit, no dataset identifier is printed** (`data gap`).
- **AI / funding / conflict disclosure:** `Author Contributions and Use of AI Tools` states that all implementation was written in Python with the assistance of **Claude (Anthropic) as a coding assistant under the author's direction**, that Claude is not an author, and that the author is solely responsible. The PDF prints **no funding statement and no competing-interests statement** (missing section, not a declaration of none), and the landing shows only the licence line, the suggested citation and the reference/citation counters - **no competing-interests declaration box appears on either surface**, so funding and competing interests are `not stated in source`.

### Independently reproduced

`Not independently reproduced.`

What was done instead is limited to provenance and internal-consistency checking of the pinned PDF, which is **not** replication of any result:

- Page count (26), byte length (858,809), SHA-256 (`ccf6d175...e79`) and character count (55,254) recomputed locally from the pinned file.
- Re-derived from the paper's own printed dollar endpoints: 1,000 -> 1,132 = **+13.2%**; 1,000 -> 1,878 = **+87.8%**; 1,000 -> 2,926 = **+192.6%**; give-back 3,461 - 1,878 = **1,583** (~`about 1,600`); recovered (2,926 - 1,878)/(3,461 - 1,878) = **66%**; 1,000 -> 1,350 = **+35.0%**, lock 1,000 -> 2,364 = **+136.4%**, recovered (2,364 - 1,350)/(2,755 - 1,350) = **72%**; 1,000 -> 821 = **-17.9%**, lock 1,000 -> 1,957 = **+95.7%**, recovered (1,957 - 821)/(2,281 - 821) = **78%**; 1,000 -> 1,080 = **+8.0%**; 1,000 -> 1,138 = **+13.8%**. All match the printed values.
- Table 3 net-Sharpe column re-read programmatically: min **0.44**, max **1.01**, **n = 12**, matching the paper's stated `cluster between 0.44 and 1.01` and `twelve configurations`.
- Cost-term word scan counts above re-computed from the extracted text.

No trading rule was re-run, no data were re-downloaded, and no performance number was reproduced.

### Negative evidence

1. The directional programme's own engine has no out-of-sample forecast: June's return is described by the source as `a run of short beta that the calendar cut off`, with a post-June-6 win rate `indistinguishable from a coin flip`.
2. The policy's confidence is **anti**-predictive: <65 confidence wins 55.8 percent, >=80 confidence wins 32.2 percent and loses 0.72 percent on average.
3. Seven of the policy's eight wait-gates blocked trades that would on average have won; only one blocked a losing set.
4. The loss filter cannot fix a losing regime: June 20-29 the filtered book still loses **-25.8 percent** (vs -40.6 percent unfiltered).
5. Filtering in general is not helpful: the source concludes that `filtering is not, in general, a good thing` and that it is wrong four times out of five; three of the five candidate filters block clearly above-baseline sets (86 / 68 / 64 percent against the 62.8 percent baseline) and cut the kept return, and stacking all five (660 of ~1,100 trades) gives **+19.8 percent**, well below `R4`'s +60.1 percent.
6. Internal misclassification of `R5` (contradiction #5): its blocked set won **58 percent** (below the 62.8 percent baseline) and its kept ROI **+28.8 percent** (above the +27.7 percent baseline), yet it is printed as `cuts winners`, and the prose claims four of five blocked above-baseline sets.
7. The permutation test speaks only to `the resolved trades of a single month` and `says nothing about the next one` (source's own limitation).
8. The whole filter/ratchet result rests on **one month** (June 2026), a `small sample for an account curve` in a trending-then-chopping regime.
9. A naive 6 percent trail without arming locks **1,138 dollars** - `worse than leaving the position alone` on the filtered book - which is why the arming step exists.
10. The ratchet is **not** universally beneficial: on the unfiltered 2-to-1 curve it locks **1,080 (+8.0 percent)** against an unmanaged **1,132 (+13.2 percent)** (whipsaw).
11. The ratchet has its own configuration risk: it must be armed **above** the curve's pre-run equity or it arms into pre-run noise.
12. The ratchet goes flat after the lock and `cannot make another windfall`; it locks 2,926 against a 3,461 peak, so it cannot catch the top.
13. Cross-sectional momentum, the obvious rival, dies out of sample: **1.60 -> 0.03** after the 2025 cutoff, with a **97 percent** worst drawdown - evidence that in this universe in-sample factor results are unreliable.
14. The carry sleeve is **negative in three of six calendar years** and is in a drawdown in 2026.
15. The carry sleeve's reliable component is small: the funding coupon is only **6 to 15 percent a year**, while the large, sign-unstable **price spread** (+136 percent in 2021, -19/-23/-29 percent in 2022/2023/2026) drives the P&L and `carries crowding risk and drove every one of its losing years`.
16. The bootstrap interval is wide: **0.11 to 1.89**, lower bound barely above zero, P(non-positive) about 1.2 percent.
17. The headline Sharpe is the best of twelve cells; the source's own best-of-12 selection expectation (**~1.06**) is **above** the observed **1.01**, and the paper states the full-period 1.01 `is not the number to lean on`, with the clean read being OOS **0.90**.
18. Favourable-window selection is demonstrated inside the paper: **1.62 net / 11 percent MaxDD** on 2024-2026 weekly 5-wide versus **1.01 / 46 percent** on the full six years.
19. The two mechanisms are **not** complementary: the carry sleeve lost **-4.4 percent** over the exact June window in which the directional/ratchet stack locked a windfall.
20. **Capacity and market impact are not modelled**; the crowded-name spread may be arbitraged away by others running the same screen (source's own stated deployment limit).
21. The overlays are simulated on account curves, not live fills; live trailing stops face stop-level slippage, gaps, and the marked-vs-realised equity question.
22. Table 3's high out-of-sample Sharpes on slow cells (e.g. +2.05, +1.91) rest on **few rebalances** - a small-sample effect the source itself flags.
23. No public code or data artefact: scripts are `available ... on reasonable request` and the repository is `in preparation`; third-party feature/data terms restrict redistribution.
24. The directional book's inputs (the `multi-source snapshot`) are undisclosed, so the directional side is not reconstructable, and it is the substrate both overlays defend.
25. The source prints no funding or competing-interest statement, no venue-independent replication, and no second venue.
26. Adjacent contrary literature already in this repository: `crypto-funding-carry-fade-turnover-cost-dissipation-falsification-2026-09-12.md` (funding carry-fade falsified on turnover-cost grounds), `crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11.md` (cross-sectional funding factor under net costs), `crypto-perp-llm-signal-backtest-to-live-gap-anatomy-2026-09-27.md` (same author: a signal that passes a permutation test still lost money in deployment), `binance-perpetual-cross-sectional-momentum-taker-cost-falsification-2026-09-13.md` and `bitget-perpetual-shuffled-null-falsification-cross-sectional-momentum-2026-09-13.md` (cross-sectional momentum falsified under retail costs / shuffled nulls).
27. None of the three mechanisms predicts anything, which the source states as its own conclusion - so any later framing of this record as an alpha strategy would misstate the source.

## Falsification plan

Every threshold below is **research-defined** (a Scout-chosen failure rule), not a number from the source; every rule that is source-reported is marked as such. All tests are research-proposed until executed.

- **F1 - entry-filter reproduction gate (research-defined).** On an independent sample of at least 6 monthly books from the same venue and bracket geometry, re-run `R4` and require (i) blocked-set win rate below the book baseline in at least 5 of 6 months and (ii) a permutation p < 0.01 pooled across months (10,000 draws of the same blocked-count). **Fail** if either condition misses; action: mark the filter month-luck and drop it from any candidate pool.
- **F2 - entry-extreme monotonicity replication (research-defined).** Recompute win rate by one-hour Bollinger-position bucket on >= 6 months and require a strictly positive rank correlation (Spearman rho > 0, p < 0.05) between band position and win rate for shorts and longs separately. **Fail** if rho <= 0 in either direction.
- **F3 - filter-family multiplicity (research-defined).** Treat the 5 candidate filters x 2 geometries x {trade, account} levels as a family and apply Benjamini-Hochberg at q < 0.10. **Fail** if `R4` does not survive.
- **F4 - filter net-of-cost gate (research-defined).** Add a realistic cost ladder of 0/1/2/5/10/20 bp per side plus a half-spread to the directional account and require the filtered book to beat the unfiltered book after costs in at least 4 of 6 months. **Fail** otherwise (the source models only a flat 0.1 percent round-trip fee).
- **F5 - ratchet replication across independent curves (research-defined).** Apply arm +20 / trail 10 to at least 4 account curves produced by a *different* programme (different signal, same venue class). **Fail** if the ratchet locks below the unmanaged end on at least half of them, or if the plateau in the 7x6 grid shrinks below 50 percent of cells.
- **F6 - ratchet whipsaw guard (research-defined).** Re-run the grid with the arm threshold expressed relative to pre-run equity (peak-to-date rather than start-of-book). **Fail** the mechanism's robustness claim if the failure corner grows beyond the source's tight-trail/low-arm corner.
- **F7 - carry frozen out-of-sample test (research-defined).** Freeze the source's headline cell (1-day funding signal, breadth 3, 3-day rebalance, 5 bp taker + tiered slippage) and evaluate from 2026-10-01 forward for 12 months on the same venue. **Fail** if 12-month net Sharpe <= 0, or if the stationary-block-bootstrap 95 percent interval includes 0 at the 90 percent level.
- **F8 - carry cost ladder (research-defined).** Re-run with 0/1/2/5/10/15/20/30 bp per side plus maker-2bp and taker-5bp variants. **Fail** the headline if net OOS Sharpe < 0.3 at 10 bp per side (the source's own sweep puts the zero-crossing near 20 bp; 10 bp is the Scout's harsher bar).
- **F9 - best-of-grid deflation (research-defined).** Compute a deflated Sharpe ratio over the full searched family actually exercised by the programme: 12 carry cells x 5 entry filters x 4 ratchet curves x 2 geometries. **Fail** if DSR < 0.95 for the carry headline or for `R4`.
- **F10 - point-in-time funding and look-ahead audit (research-defined).** Rebuild funding inputs strictly from the published 8-hour funding prints with their own timestamps and require the rebuilt carry Sharpe to stay within 0.15 of the reported 1.01. **Fail** on any detected look-ahead (that is: any drop > 0.15, or any use of a print unavailable at the rebalance timestamp).
- **F11 - point-in-time universe / survivorship audit (research-defined).** Rebuild the 20-coin universe with delistings and listing dates included from 2021. **Fail** if the rebuilt full-period net Sharpe falls below 0.70 (a 30 percent haircut from the reported 1.01).
- **F12 - leave-one-year-out stability (research-defined).** Recompute the carry sleeve six times, omitting each calendar year. **Fail** if the net Sharpe in any single-year omission falls to <= 0 (the source already reports three losing calendar years, so this tests whether two years carry the whole result).
- **F13 - capacity / participation ceiling (research-defined).** Scale the sleeve's per-name notional from 1x to 100x using a tiered impact model (e.g. impact proportional to participation in the funding-settlement window). **Fail** the deployability claim if net Sharpe drops below 0.5 at 10x the tested size, or if any year flips negative.
- **F14 - live-versus-simulated overlay gate (research-defined).** Run the filter and ratchet on marked-to-market live fills for >= 3 months and require realised P&L within 20 percent of the simulated curve after costs, with no missed trailing-stop executions. **Fail** if divergence exceeds 20 percent or any stop gap-through is unmodelled. Action on any failure: keep the record research-only and do not advance it to a production candidate.

## Crypto portability

**direct.**

The evidence is itself crypto: Binance USD-margined perpetuals, 20 coins, 1-minute / 1-hour / 15-minute data, realised funding, 2021 through mid-2026 for the carry sleeve and June 2026 for the directional overlays. Nothing has to be ported across asset classes.

Residual portability risks even inside this `direct` setting:

- **Single venue.** Everything is Binance; no cross-venue funding or price series, so venue-specific funding microstructure and listing policy are untested elsewhere.
- **Funding grid.** The paper does not state how the 8-hour funding calendar is aligned to the rebalance clock, nor how the funding field is timestamped; on other venues the funding interval and settlement convention differ.
- **Spot vs perpetual.** The sleeve is `perps-only, with no spot leg`, so it inherits liquidation, mark/index-price and auto-deleveraging risks that a spot book would not.
- **24/7 session.** The daily-close account curve and the first-touch resolver assume continuous trading; candle-boundary, maintenance-window and index-price dislocation behaviour are `data gap`.
- **Capacity / crowding.** The source explicitly leaves capacity unmodelled; crowded-name funding screens are a known crowded family (see the repo's carry-fade falsification records).
- **Cost model transport.** The flat 0.1 percent round-trip fee (directional) and the ~5-6 bp/side tiered estimate (carry) are venue- and size-specific and must be re-derived per venue and per AUM.
- **Underlying signal substrate.** The two overlays defend an LLM directional book whose feature snapshot is undisclosed; the overlays can be tested independently of it, but their reported magnitudes are conditional on that book's trade distribution.

## Limitations

- `underspecified`: the 20-ticker universe list; the definitions of filters `R1`, `R2`, `R3`, `R5`; the Bollinger price basis and warm-up; the funding field and its timestamp convention; the arm-threshold reference equity; the slippage tier schedule; turnover units and Sharpe annualisation convention; the exact out-of-sample boundary date; order type, fill timing, latency, and market-impact model.
- `data gap`: timezone / clock conventions for all four bar resolutions; missing-data policy; whether funding received/paid is modelled as realised cash; margin financing cost for the short legs; borrow (zero relevant occurrences); commission (zero occurrences).
- `not independently reproduced`: every performance number in this record is source-reported; only printed arithmetic and term counts were re-derived locally.
- `unproven`: transfer of the entry filter and ratchet to any book other than this programme's June 2026 book; transfer of the carry sleeve to any venue other than Binance; any claim of live profitability (the source states the overlays were not studied on live fills).
- Source-quality limits: SSRN working paper with no peer-review statement; no public code or data artefact (scripts on request, repository `in preparation`); no funding or competing-interests statement in the PDF; licence conflict between the landing and the PDF; single author, independent researcher; AI-assisted implementation (Claude) disclosed with author responsibility.
- Sample-size limits: the filter and ratchet rest on **one month** and **~1,000 resolved trades** of one book; the carry result rests on six years but is negative in half of the calendar years and its steady coupon is 6-15 percent a year.
- Selection limits: the headline carry cell is the best of 12, the winning filter is the best of 5, the ratchet is shown on 4 curves of the same programme; the source applies a best-of-12 deflation and a bootstrap but no formal multiple-testing correction across the whole programme family.
- Interpretation limit: this record covers a **risk-control programme**, not a predictive strategy; reading any of the three mechanisms as standalone alpha would contradict the source.

## Implementation status

`implementation_status: not-implemented`.

No part of this record has been implemented in our research stack. No Binance data were downloaded, no filter, ratchet or carry backtest was run, no NautilusTrader/Qlib/Paper/Testnet/Live workflow was touched, and no result was reproduced. What exists locally is only: the pinned PDF, its extracted text, a term-count scan and an arithmetic re-derivation of printed dollar endpoints, all of which are provenance checks.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

The presence of this record in the repository means only that a normalised, source-traceable research capture exists. It does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed any full backtest; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; or approved for live trading. The source's own conclusion - that none of the three mechanisms reliably makes money - is part of this record and is not overridden by it.

## Related Wiki records

Read-only `kb_search` on the run date returned the following **verified** adjacent pages (query `funding rate carry market-neutral cross-sectional perpetual`, 8 hits; only these three are linked):

- [[quant/crypto-funding-carry-fade-turnover-cost-dissipation-falsification-2026-09-12]]
- [[quant/crypto-hyperliquid-momentum-funding-carry-combo-2026-09-12]]
- [[quant/crypto-perp-vol-scaled-cross-sectional-momentum-factor-2026-09-12]]

A second read-only query (`trailing stop drawdown control risk overlay volatility extreme entry filter`) returned 2 weakly related pages and a third (`backtest-to-live gap Dashyan LLM directional signal Binance`) returned **zero** hits, so no Wiki page for the sibling SSRN 7353678 record exists yet and none is fabricated here. Note that Wiki Brain carries `quant/crypto-funding-rate-cross-sectional-carry-factor-net-costs-*`-style pages only if a search returns them; none was returned for this run's queries, so no such link is asserted.

Adjacent **repository** records (not Wiki pages) that a future reviewer should read together with this one: `crypto-perp-llm-signal-backtest-to-live-gap-anatomy-2026-09-27.md` (SSRN 7353678, same author, cites this paper as an unidentified companion), `equity-index-tail-flush-reversion-disjoint-band-familywise-2026-09-27.md` (SSRN 7363482, same author), `crypto-funding-carry-fade-turnover-cost-dissipation-falsification-2026-09-12.md`, `crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11.md`, `crypto-hyperliquid-momentum-funding-carry-combo-2026-09-12.md`, `hyperliquid-vol-targeted-tsmom-drawdown-calibrated-ratchet-2026-09-12.md`, `crypto-risk-managed-tsmom-crash-state-de-risking-drawdown-control-2026-09-14.md`, `binance-perpetual-cross-sectional-momentum-taker-cost-falsification-2026-09-13.md`.

## Sources

- Dashyan, A. (2026). *Risk Control as the Durable Edge: Loss Filtering, Profit-Armed Ratchets, and Market-Neutral Carry When Direction Fails*. SSRN working paper. Landing page: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7345542>; DOI: <https://doi.org/10.2139/ssrn.7345542>. PDF title block: `Aleksandr Dashyan, Independent Researcher, Yerevan, Armenia`; landing author line: `Alexandr Dashyan`. `Date Written: August 01, 2026`; `Posted: 26 Aug 2026`; PDF cover `This version: August 2026`; PDF metadata `CreationDate D:20260824174353+04'00'`. 26 pages. Landing read 2026-09-28 (Cloudflare interstitial cleared) showing `26 Pages`, `0 References`, `0 Citations`, `DOWNLOADS 29 -> 32`, `ABSTRACT VIEWS 85 -> 86` across two reads. Pinned PDF retrieved 2026-09-28 via the landing's `Open PDF in Browser` delivery link, 858,809 bytes, SHA-256 `ccf6d175dced6fc19879d1d2ac08d120ca117a4278c3d53665c95bbbe95e6e79`, text extracted with `pypdf 6.16.2` to 55,254 characters, all 26 pages read; no presigned or session-bound URL retained.
- Companion works cited by the source with **no identifier printed** (`not stated in source`): Dashyan (2026a), *Short-horizon directional non-predictability in cryptocurrency perpetual futures: a multi-method negative result under adversarial verification*; Dashyan (2026b), *Adversarial backtest verification: catching overfitting, beta, collinearity, and look-ahead in a live trading-research program*. Both `Working paper` (PDF references [6] and [7]).
- Methodological references used by the source for its own tests (listed as the source lists them, PDF [1]-[18]): Asness/Moskowitz/Pedersen (2013); Bailey/Borwein/Lopez de Prado/Zhu (2014); Bailey & Lopez de Prado (2014); Barroso & Santa-Clara (2015); Daniel & Moskowitz (2016); Han/Zhou/Zhu (2016); Kaminski & Lo (2014); Koijen/Moskowitz/Pedersen/Vrugt (2018); Lo (2002); Makarov & Schoar (2020); Moskowitz/Ooi/Pedersen (2012); Novy-Marx & Velikov (2016); Politis & Romano (1994); Shefrin & Statman (1985); Sullivan/Timmermann/White (1999); White (2000).
