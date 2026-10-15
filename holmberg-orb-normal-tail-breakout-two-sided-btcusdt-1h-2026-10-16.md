---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Holmberg normal-tail ORB threshold breakout two-sided on BTCUSDT 1h bars
created: 2026-10-16
updated: 2026-10-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2012-02-02
sources:
  - https://ideas.repec.org/p/hhs/umnees/0845.html
  - http://www.econ.umu.se/DownloadAsset.action?contentId=196616&languageId=3&assetKey=ues845
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Holmberg normal-tail ORB threshold breakout two-sided on BTCUSDT 1h bars

## Provenance

Primary sources read end to end during this cycle (2026-10-16), pinned:

- RePEc record page (fetched live this cycle, HTTP 200, 40449 bytes): `Holmberg, Ulf & Lönnbark, Carl & Lundström, Christian, 2012`, `Assessing the profitability of intraday opening range breakout strategies`, `Umeå Economic Studies` No. 845, date `2012-02-02`, `11 pages`, `freedownload=1`. Abstract (verbatim): `An investor that trades on the ORB strategy seeks to identify large intraday price movements and trades only when the price moves beyond some predetermined threshold. We present an ORB strategy based on normally distributed returns to identify such days`. Keywords include `Bootstrap; Crude oil futures; Contraction-Expansion principle; Efficient market hypothesis; Martingales; Technical Analysis`. A 2013 journal entry by the same authors is listed on the same record (not read; nothing is adopted from it).
- Working paper PDF (fetched live this cycle from the record's download URL, 237045 bytes, SHA-256 `3bbf81e2f9bfb11f1e2622077b3c064ffc541e697fa57729ba55767b375cbeee`, 11 pages, read end to end): notation `Pto/Pth/Ptl/Ptc` = day-`t` open/high/low/close; thresholds `ψtu=(1+ρ)Pto`, `ψtl=(1−ρ)Pto` (§2); entry `if the price crosses it from below (above) a momentum investor acts, i.e. takes a long (short) position` (§2); tail rule `ρα=μˆ+σˆqα` as eq. (1) with `μˆ,σˆ` estimated on `Rtc=log(Ptc/Pto)` and `qα` the inverse standard normal CDF at `α`; exit `all positions are closed at the end of the trading day` (§2); risk posture `no type of money management techniques such as a stop loss, trailing loss, profit stop are considered` (§2); execution assumption `a perfect order fill at the threshold price, a zero bid ask spread, as well as zero commissions` (§2, explicitly NOT adopted — see derivation); sample `U.S. crude oil futures prices obtained from Commodity Systems Inc covering the period March 30, 1983 to January 26, 2011` (6976 obs, §3, nearby-contract roll around the 20th per Pelletier 1997); cost note `A reasonable estimate is 0.04%, or 0.08% round trip` (§4); subperiod caveat `this finding is not robust to time and to a large extent explained by the most recent (and most volatile) period` (§3); lineage `In pioneering the ORB strategy Crabel (1990) presented the so-called Contraction-Expansion (C-E) principle` (§1, cited by the paper — no Crabel rule is adopted here).
- Licence and rights: this record cites and normalizes the rule (short quoted declarations only for gate evidence) and reproduces no source block beyond single-line facts.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the paper's test. The paper evaluates two one-sided threshold portfolios on crude-oil daily bars with perfect threshold fills. Researcher-declared adaptations are exactly seven: (1) market pin `BTCUSDT` Binance futures `1h` (the paper trades US crude futures — venue/frame pin disclosed, never a source claim); (2) continuous monitoring → completed-`1h`-bar touch with next-bar-open market fills (the paper's perfect-threshold fill is unmodellable on the pinned engine — deviation disclosed, never an advantage claim); (3) `ρ` frozen to the paper's full-sample `α=5%` numerals (`ρ_L=0.011996`, `ρ_S=0.011621` — the paper estimates `ρ` ex post from its own sample, so re-estimating on BTC would be leakage; the numbers are pinned constants, never re-estimated); (4) `α=5%` pinned among the paper's five tested levels (researcher choice — conventional middle, N=439/497 full-sample trades; the other four levels are different, unpinned rules); (5) first-touch-single-side-per-day (the paper counts long/short legs as separate portfolios, which would need unverified hedge-mode to co-hold — so the day's first touched side takes the single unit, later opposite touches are ignored, same-bar double-touch resolved by `sign(close−O)`); (6) trading day = UTC day with exit at the `23:00–00:00 UTC` bar close (the paper closes `at the end of the trading day`); (7) house sizing/costs with modeled funding while held (the paper assumes zero spread/commission in-test — recorded as absent portable economics, never as evidence). The `ψ=(1±ρ)·open` construction, the normal-tail `ρ` numerals, the momentum-continuation mapping, the day-end exit, and the no-stop/no-target posture are source-pinned.

Pre-write dedup (2026-10-16): working-tree case-insensitive searches for `holmberg`, `lonnbark`, `lundstrom`, `crude`, `contraction-expansion`, `threshold-breakout`, `fair game`, `martingale`-as-strategy return zero strategy records using this source, sample, or normal-tail-threshold construction (`martingale` hits are prose mentions only; `orb`-letter hits are English words such as `absorb`; `opening range` hits are Dual Thrust's open-anchored rails, NR7's cited Crabel bibliography, and REI's background prose — five-axis distinction in Signal and Negative evidence 7). Open `research/*` PRs are only #48, #49, #63, #89, #92 (Larry Williams streak, Gaussian-channel StochRSI, SuperTrend flip, Chandelier Exit, SSL channel) — none is a normal-tail threshold ORB.

## Economic mechanism

### Source-reported

Contraction-Expansion harvesting through normal-tail thresholds: calm (contraction) days print normally distributed open-to-close returns, so a day whose price travels beyond the `α`-tail move `ρ_α` is unlikely under the martingale null; conditioned on that breach, momentum continuation (`E[Ptc|Pt+δ>ψtu]>Pt+δ`, §2) carries price further toward the close, and the paper's bootstrap test (Brock et al. 1992 procedure, §2) rejects zero expected returns on both legs full-sample. The authors stress the long-volatility character: `ORB is a directional strategy in the sense that either a long or a short position is established and hence it is basically long volatility` (§3).

### Research interpretation

Open-anchored II intraday-expansion day trade, two-sided first-touch. Unlike every trailing/rolling breakout record (Donchian/Turtle/Darvas/pivots/R-Breaker grid) no level is inherited from any prior bar — each UTC day starts from a blank slate: two rails at fixed `±ρ` percent around that day's own 00:00 UTC open, and the first rail touched decides the day's single side. Unlike Dual Thrust (open-anchored rails scaled by the prior day's range with a reversal book) the rails here are volatility-blind constants from a 1983–2011 crude-oil normal tail, and the book always goes flat at day-end instead of reversing. Unlike the Alexander 5% filter (trailing-extremum close-reversal, multi-day holds, long-flat) the anchor is the day open, the horizon is hours, exits are calendar-fixed, and shorts are native. The bet, as derived, is purely that a `1.2%`-from-open BTC move before 23:00 UTC continues toward the midnight close often enough to matter — never on a level break of history, an indicator cross, volume, calendar, or funding.

## Signal

Exact rule as pinned (any other `ρ`, `α`, frame, fill, book, or tie treatment is a different, unpinned rule):

- Day frame: UTC day `D`. `O[D]` = open of the `00:00–01:00 UTC` `1h` bar. Thresholds `ψu[D] = O[D] × 1.011996`, `ψl[D] = O[D] × 0.988379` (paper Table 2 full-sample `α=5%`: long `ρ=1.1996%`, short `ρ=−1.1621%`).
- Entry scan (completed `1h` bars only, chronological): the first bar `t` of day `D` closing `01:00–23:00 UTC` with `high[t] ≥ ψu[D]` → long at the next bar's open; with `low[t] ≤ ψl[D]` → short at the next bar's open. One entry per day maximum: bars after the entry bar are never evaluated, opposite-side touches are ignored (no flip, no add).
- Same-bar double-touch tie-break (pinned researcher rule): if the first touching bar has `high[t] ≥ ψu[D]` AND `low[t] ≤ ψl[D]`, side = long iff `close[t] ≥ O[D]`, else short (exact equality → long; measure-zero on live tape, disclosed convention).
- Final-bar void: a touch occurring only on the `23:00–00:00 UTC` bar yields no entry (no bar remains to enter and exit within day `D`).
- Exit to flat: the full unit closes at the close of the `23:00–00:00 UTC` bar (same-bar-close market fill). Days with no touch stay flat (the paper likewise holds no position on no-trigger days).
- Exits/risk: day-end close only. No stop, no target, no trailing — explicitly none by paper rule (`no type of money management techniques ... are considered`, §2).
- Direction: two-sided first-touch (long leg and short leg are both native; at most one fires per day). Shorts are native to USDT-M margin (no uptick rule, no borrow desk).
- Re-entry: the next UTC day re-arms independently (no cooldown specified — explicitly none, not invented; days are independent by construction).

## Required data

- Completed `1h` bars of BTCUSDT: `open` (day anchor `O[D]` plus entry fills), `high`/`low` (threshold-touch detection), `close` (tie-break leg plus exit fill). No volume, funding-signal, OI, mark/index price, order-book, on-chain, sentiment, macro, calendar, session-template, or cross-asset state is read anywhere.
- Single decision timeframe `1h` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; thresholds are pinned constants, never estimated at runtime).
- Warmup: none structurally (no trailing window, no indicator, no normalization — every input is the current day's own prints). Any UTC day whose `00:00 UTC` open is missing is flat by record rule; missing intraday bars are skipped on available completed bars only — prices are never fabricated. No repaint path (thresholds fixed at 00:00 UTC from a completed open; touches read completed bars only).

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (the paper trades US crude-oil futures — venue/frame adaptation disclosed, never a source claim).
- Order timing (predeclared derivation): completed-bar touch decision with next-bar-open market entries, day-end exit at the final bar's close — compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) on the same verified primitives as the admitted `ehlers-decycler` (next-open entries) and `r-breaker-7-level` (same-bar-close exits) PASS records. No maker-touch, queue, multi-asset sync, lower/multi-timeframe alignment, non-OHLCV input, or intrabar-path-dependent fill is required. At most one entry plus one exit per day.
- Sizing/capital/costs: single 100%-equity unit per firing day, no adds, no leverage concept beyond the house overlay (the paper ships no portable economics — zero-spread/zero-commission test assumption recorded as absent, never as evidence). Derived evaluation carries pinned house taker fees both legs plus modeled funding while held — the hold window spans the `08:00`/`16:00 UTC` funding stamps on firing days, so funding is never zero-claimed. No Safety-Order/DCA event participates regardless of downstream campaign settings.
- Concurrency: one single-asset engine position at a time (first-touch side only); no second leg is constructed anywhere — no hedge-mode requirement exists by construction. No shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

With exact table/section provenance (Umeå ES No. 845, read end to end this cycle): sample `March 30, 1983 to January 26, 2011`, 6976 daily crude-oil futures bars (Table 1: mean `0.02`, sd `0.72`, min `−6.06`, max `9.90`, skew `0.16`, kurt `10.26`, JB `30668` — percent units); full-sample `α=5%` long `ρ=1.1996, N=439, freq=0.6036, R̄=0.2180, p=0.0000` and short `ρ=−1.1621, N=497, freq=0.5714, R̄=0.1784, p=0.0000` (Table 2); tightening-α monotone (success rate and mean rise down the tail, §3, Fig. 3); cost note `0.04%` one-way / `0.08%` round trip (§4); subperiod non-robustness with the 2001-10-12–2011-01-26 volatile period driving results (§3). No number beyond these is carried; exact empirical figures require traceable table provenance and are otherwise omitted.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Subperiod fragility fenced, admitted plainly: 1983-03-30–1992-06-29 long `α=5%` prints `N=159, freq=0.5157, R̄=0.0711, p=0.1350` (Table 2 — insignificant), and the authors state the result `is not robust to time`; this record ports the full-sample numerals anyway, disclosed, never cherry-picking the volatile subperiod's larger prints (2001–2011 long `α=5%`: `N=138, freq=0.6522, R̄=0.3405, p=0.0004`).
2. Ex-post `ρ` fenced: the paper states `The values of the ρ's ... are derived from the sample. We thus check ex post` (§3) — the numerals are in-sample calibrations on 1983–2011 crude, and BTC's daily scale (`σ≈3–4%` vs the paper's `0.72%`) fires far more often; no recalibration is performed because that would be a different, unpinned rule.
3. Fill-lag derivation disclosed: the paper assumes `a perfect order fill at the threshold price` (§2); this record enters up to one hour late at the next `1h` open — a declared friction (gap-against-entry on continuations), never paper-native.
4. First-touch derivation disclosed: the paper counts long/short legs as separate portfolios (both can fire the same day); this record takes only the first side to keep a single engine position without hedge-mode — the discarded opposite leg is a declared cost of executability, and F3 prices the flip-book alternative.
5. No-stop posture disclosed: adverse excursion after entry has no guardrail before the midnight exit by paper rule — the principal risk, carried over exactly.
6. Session mismatch disclosed: crude pit/electronic sessions vs a 24/7 UTC-day mapping — the `00:00 UTC` open is a researcher session pin, never a paper session.
7. Overlap fences, admitted plainly: pool `dual-thrust-open-range` anchors rails at `open ± k·(prior-day range)` with a reversal-only book (range-adaptive rails, never flat); pool `r-breaker-7-level` trades a seven-level prior-day `HLC` grid with latch-gated flips and an always-in-market book (grid + flips, never flat); pool `bitcoin-intraday-first-last-halfhour` trades a morning-sign into a 30-minute hold (sign timing, never a level); pool `alexander-fama-blume-5pct-filter` reverses on closes against a trailing extremum with multi-day holds, long-flat (trailing anchor, never open-anchored, never intraday-flat). Shared `open`/`breakout` vocabulary is not shared signal.
8. No hidden variants admitted: the other four tested `α` levels, any re-estimated `ρ`, any other frame, fill, book, or tie-break is a different, unpinned rule. A reviewer must not pick among these to rescue or reshape the record.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `ρ_L=0.011996` / `ρ_S=0.011621` / `α=5%` pin / first-touch single side / `sign(close−O)` tie-break / final-bar void / next-open entries / midnight same-close exit / no-stop posture / `1h` BTCUSDT are frozen.

- F1 — Continuation relevance: a fade twin (short on upper touch, long on lower touch — same grid, fills, exits) must not improve net expectancy; fail ⇒ the paper's momentum mapping adds nothing over fading it on this market.
- F2 — Tail-level relevance: an `α=1%` twin (`ρ=1.6889%` / `−1.6513%`, the paper's adjacent tested level — same machine) must not improve net expectancy; fail ⇒ the tighter tail ports better and the `5%` pin points the wrong way.
- F3 — Book relevance: a flip-book twin (opposite touch flips instead of day-end flat — R-Breaker-style book on the identical grid) must not improve net expectancy; fail ⇒ the day-end flat destroys value and the first-touch-flat derivation is the wrong port.
- F4 — Trigger relevance: an always-long twin (long every UTC day at the `01:00` open, same midnight exit, same costs) must not improve net expectancy; fail ⇒ the threshold trigger adds nothing over unconditional day-long exposure.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (declared port of a US crude-oil futures sample). The rule reads completed hourly bars only, so no pit-session, gap, or roll logic ports — but crude session structure vs 24/7 crypto is a real mismatch, fenced above via the UTC-day pin. Fixed percent thresholds need no pip recalibration across assets, yet BTC's `3–4%` daily scale vs crude's `0.72%` means far hotter firing cadence — unclaimed and undisguised. The rule is two-sided first-touch, so a spot-only deployment expresses only long-firing days while short-firing days stay venue-gated (never silently converted) — a spot-only variant would be a different, unpinned claim. No funding-dependent leg, no stablecoin assumption. No warmup history is consumed (thresholds need only the current day's open). Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- No price stop, no time stop before midnight: adverse excursion after a touch entry has no guardrail beyond the `23:00–00:00 UTC` close, by the paper's prescribed design.
- Crude-calibrated thresholds on a 4–5× more volatile asset: most BTC days touch at least one rail, so the machine trades far more often than the paper's 439/497-in-6976 cadence, paying taker + funding far more often — disclosed, not tuned away.
- Whipsaw by design: an opening spike that reverses still pays a full day-trip (entry near the extreme, exit at midnight); the fixed rails offer no band or hysteresis, by the prescribed design.
- First-touch blindness: the discarded opposite leg on double-touch days could be the day's real move; the single-side rule buys engine simplicity with missed reversals, by the declared derivation.
- Next-open lag: the paper fills at the threshold; this record can enter up to an hour late, systematically worse on straight-line expansion days.
- Venue-portability residual: prints, fees, funding, and margin mechanics beyond the house model are unclaimed, disclosed.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior and never part of this admission — no Safety-Order/DCA event is admitted in this record's version. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- RePEc record (Holmberg, Lönnbark & Lundström (2012), Umeå Economic Studies No. 845, 2012-02-02, abstract/keywords/sample-frame verified from the fetched bytes): https://ideas.repec.org/p/hhs/umnees/0845.html
- Working paper PDF read end to end this cycle (237045 bytes; SHA-256 `3bbf81e2f9bfb11f1e2622077b3c064ffc541e697fa57729ba55767b375cbeee`; §2 rule/threshold/exit/risk text, eq. (1), Table 1 descriptives, Table 2 full-sample and subperiod rows, §3–§4 caveats, Crabel-1990 C-E lineage): http://www.econ.umu.se/DownloadAsset.action?contentId=196616&languageId=3&assetKey=ues845
