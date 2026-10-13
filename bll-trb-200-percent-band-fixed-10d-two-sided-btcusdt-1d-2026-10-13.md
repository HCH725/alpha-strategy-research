---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: BLL TRB-200 1% band fixed-10-day breakout two-sided on BTCUSDT 1d
created: 2026-10-13
updated: 2026-10-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 1992-12-01
sources:
  - http://technicalanalysis.org.uk/support-and-resistance/BrockLakonishokLeBaron1992.pdf
  - https://www.kevinsheppard.com/files/teaching/mfe/advanced-econometrics/Brock_Lakonishok_LeBaron.pdf
  - https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1992.tb04681.x
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# BLL TRB-200 1% band fixed-10-day breakout two-sided on BTCUSDT 1d

## Provenance

Primary source read end to end in its methods (§I.B, journal pp. 1735–1736) and trading-range-break results (§II.C with Table IV, journal pp. 1742–1743):

- Brock, W., Lakonishok, J., LeBaron, B., `Simple Technical Trading Rules and the Stochastic Properties of Stock Returns`, The Journal of Finance 47(5), 1731–1764 (December 1992), DOI `10.1111/j.1540-6261.1992.tb04681.x` (adopted as `source_as_of` 1992-12-01).
- Exact file read: http://technicalanalysis.org.uk/support-and-resistance/BrockLakonishokLeBaron1992.pdf — 35 pages, retrieved 2026-10-13, 4,617,601 bytes, SHA-256 `b02f6dc1c68ff6758fc6c6ac96b3d34fa719ec693a16aaf949d03e8c90a95549`. Full text layer extracted and read (97,809 characters); every rule sentence and every number below is transcribed from those pages — no rule or figure was taken from a secondary summary.
- Same-paper teaching-host locator (the artifact pinned by the sibling VMA record; retrieved 2026-10-13, 350,357 bytes, SHA-256 `9f9c2ab3e02ce9319cab5c5c115c711f6b5fb497b3ab5f19ce5f964245364b7a`, byte-identical to that record's pin): https://www.kevinsheppard.com/files/teaching/mfe/advanced-econometrics/Brock_Lakonishok_LeBaron.pdf
- Bibliographic cross-check (abstract/identity only, never rule text): https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1992.tb04681.x (same title, authors, December 1992, DJIA 1897–1986 sample, bootstrap-extended null tests).
- Licence and rights: the paper is a published journal article — this record cites and normalizes the rule (short phrases and formulas only) and reproduces no figures, tables, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the paper's headline long-horizon trading-range-break rule TRB(200, 0.01) with fixed 10-day holding, ported to one crypto asset with fixed sizing — not a lossless reproduction of the paper's DJIA return-measurement study. Researcher-declared adaptations are exactly six: (1) market pin `BTCUSDT` on Binance USDT-M perpetuals, `1d` frame (the source measures daily DJIA index closes from the first trading day of 1897 to the last trading day of 1986 and runs no portfolio); (2) single-rule pin TRB(200, 0.01) — 200-day close extremes with the 1% penetration band and fixed 10-day holding, chosen on the predeclared longest-horizon rationale (maximal separation from the pool's 20/55-day breakout records; the paper's own most-popular long leg is the 1-200 family) and never on relative performance (the (150, 0.01) row prints a larger buy-sell spread and is deliberately not picked — see Negative evidence 9); (3) closes-only extremes (the source series is the daily index *level* — extremes are extremes of closes, never of intraday highs/lows; the port reads `1d` closes only); (4) next-open market fills with a fixed 10-bar hold and interim-signal suppression ported from the paper's FMA convention (the paper is a signal-following return study, execution-silent beyond signal definition; TRB interim-signal handling is not separately sentenced — see Negative evidence 2); (5) an adopted 200-bar warmup flat by record rule plus house fees/funding treatment replacing the paper's pre-cost return accounting (the paper reports gross-of-cost returns — its leverage illustration is explicitly `before transactions costs`); (6) fixed 100%-equity single position at 1× with no adds (the source ships no sizing concept). The 200-day preceding window, the 1% band, the above-maximum/below-minimum penetration posture, the go-long-breakout/go-short-breakdown direction, the fixed-10-day holding, and the no-stop/signal-only posture are source-faithful. The paper's VMA state rule and FMA crossover rule are fenced, never adopted (see Negative evidence 10).

Pre-write dedup (2026-10-13): working-tree case-insensitive searches for `trading.range.break`, `range.break-out`, `brock`, `lebaron` return only the sibling `bll-vma-1-200-percent-band-two-sided-btcusdt-1d-2026-10-13.md` (the paper's VMA mean-displacement state rule — a separately defined and separately tested rule: persistent above/below-band state with inside-band flat, never an extreme-penetration event with a fixed hold) plus `lakonishok` prose citations inside the turn-of-month and pre-holiday-drift records (Lakonishok–Smidt 1988 seasonal-anomalies survey — a different paper and purely calendar mechanisms). Sweeps for `fixed.10.day`, `10-day hold`, `10.bar hold`, `200-day`, and `local max` return breakout records that all differ in construction (see five-axis below). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `turtle-system-2-55d-breakout-2n-stop-half-n-add-two-sided-btcusdt-1d-2026-10-12.md` breaks 55-day high/low extremes with a 2N stop, half-N adds, and trailing opposite-channel exits (no band, no fixed hold, 55-day horizon); `donchian-20-10-breakout-btcusdt-1h-2026-10-06.md` breaks 20-bar high/low channels with 10-bar trailing exits on a 1h grid (no band, no fixed hold); `darvas-box-breakout-long-btcusdt-1d-2026-10-09.md` crosses frozen 5-bar-formation high/low rails, long-only, unbounded hold; `dual-thrust-open-range-breakout-two-sided-btcusdt-1d-2026-10-10.md` crosses open-anchored prior-day-range lines as an always-in-market reversal (no extremes, no band, no hold); `nr7-price-breakout-long-btcusdt-1d-2026-10-10.md` is contraction-setup-gated (6-bar narrowest range) with an ATR stop, long-only; `starc-band-breakout-latched-two-sided-btcusdt-1d-2026-10-11.md` latches 5-SMA ± 1.33 ATR bands always-positioned (ATR band, no extremes, no hold); `inside-bar-failure-fade-time-exit-two-sided-btcusdt-1d-2026-10-13.md` fades a 2-bar pattern failure with a 3-bar exit (opposite direction logic, pattern-gated). Five-axis distinction: no pool record and no open PR buys a close more than 1% above (or sells more than 1% below) the trailing 200-close maximum (minimum) and then holds exactly ten bars while ignoring every interim signal, two-sided.

## Economic mechanism

### Source-reported

Breakout-through-crowded-levels capture with a whiplash guard: a buy signal fires when the price penetrates the resistance level defined as the local maximum — the paper's rationale is that sellers queued at the old peak create resistance, so a rise above the previous peak means the resistance area is broken; a sell signal mirrors through the support level defined as the local minimum (§I.B). The 1% band exists to kill whiplash signals when price sits near the level (the moving-average statement of the band's purpose, applied `in accordance with the moving average strategy` to the range rule). Buy signals beat sell signals across all six TRB variants with an average 10-day buy-sell spread of 0.86%, and all six reject the zero-spread null (§II.C) — read by the paper as evidence that past-price extremes carry predictive content its four nulls (random walk, AR(1), GARCH-M, Exponential GARCH) cannot reproduce.

### Research interpretation

Long-horizon close-extreme breakout port: the reference is a 200-close trailing maximum/minimum — a slow step function that only ratchets on fresh 200-day closing extremes — so positions begin only after a confirmed >1% close beyond a level that survived two hundred sessions. Unlike high/low channel breakouts (Donchian-20, Turtle-55, Darvas) the rails are extremes of *closes*: a wick that pierces nothing on a closing basis fires nothing, and a grinding drift that never prints a fresh high/low extreme still accumulates a close extreme and still fires — the trigger is closing-level displacement past a closing-level memory, not an intraday excursion. Unlike mean-displacement state-following (the sibling BLL-VMA record) there is no persistent posture: each signal buys exactly ten bars of exposure and then exits into flat even if price keeps running, and any contra signal arriving mid-window is discarded, not reversed. Unlike ATR-band latches (STARC) the band is a fixed ±1% of the level, not a volatility multiple, and unlike always-in-market reversals (Dual Thrust) the book is flat most of the time by construction (the source fires only 146 buys and 124 sells in ninety years). The bet, as derived, is purely on 200-day closing-extreme penetrations persisting ten days on BTCUSDT at daily cadence, never on a cross, oscillator, volume, calendar, or funding anchor.

## Signal

Exact rule as pinned (TRB(200, 0.01) fixed-10-bar-hold event machine — any other lookback, band, hold, or mapping is a different, unpinned rule):

- Inputs at the close of completed bar T: `C_T` and the trailing window `W_T = (C_{T-200} … C_{T-1})` (the 200 closes strictly *preceding* T — the paper's `preceding 50, 150, and 200 days`; the current bar is excluded by source sentence, and exclusion is also forced arithmetically — see Negative evidence 4). `HI_T = max(W_T)`; `LO_T = min(W_T)`. Closes only: no `high`, no `low` enters any comparison.
- Signal (pinned, strict — evaluated on every completed close from bar index 200): `C_T > HI_T × 1.01` → BUY signal; `C_T < LO_T × 0.99` → SELL signal; otherwise nothing. Equality on either leg is measure-zero on live tape and signals nothing by record rule — disclosed tie convention, not a source sentence. Both legs can never fire on one bar (`HI_T × 1.01 > LO_T × 0.99` always since `HI_T ≥ LO_T`), so no dual-fire ordering rule is needed.
- Orders (pinned): a signal firing at close T while the book is flat places one market order at the next bar's open (open T+1): BUY buys 100% equity long; SELL sells 100% equity short. The position then holds exactly ten completed bars and closes in full at the open of bar T+11 (ten full bars of exposure: T+1 … T+10) — the declared causal port of the paper's fixed 10-day post-signal return window. A bar whose evaluation yields no signal places nothing — no adds, no partials, no extensions.
- Interim-signal suppression (pinned FMA-convention port, disclosed derivation): closes evaluated while a 10-bar window is active can compute signals, but every such signal is discarded — never queued, never reversed into, never extending the window. The next order opportunity opens only after the window's exit fill. In particular an opposite-side signal arriving mid-window is ridden through, not reversed (see Negative evidence 8).
- Missing-bar rule (pinned edge case): if any close in `W_T` or `C_T` itself is absent from the `1d` tape, no new entry occurs on that bar — flat stays flat. An already-active window still exits on its scheduled bar-count bar (the exit is count-based, never signal-based).
- Risk legs (pinned absence, not invented): the paper ships no stop/target/trailing concept for TRB — the sole position-closing path is the fixed 10-bar time exit. The derived posture is explicitly no stop, no target, no trailing, no opposite-signal exit; a ten-bar adverse drift is ridden in full by construction.
- Direction: two-sided (source-native posture — buy the upward penetration, sell the downward penetration). The short leg requires margin-short permission, realistic on the pinned perpetual venue. No always-in-market claim: warmup bars, no-signal bars, and post-window bars are explicitly flat.

## Required data

- Completed `1d` closes of BTCUSDT only: the close chain feeds `C_T`, `HI_T`, and `LO_T`; `open` is read solely as the fill price. No `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, or cross-venue state gates any order. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: daily close. One evaluation per completed daily bar; fills land on the next daily bar's open. All signal inputs are completed-bar closes — no provisional close is ever used; the reference window strictly excludes the decision bar, so no future reference and no same-bar extreme-vs-close ambiguity exist.
- Warmup: 200 completed `1d` bars before the first decision (the 200-close extreme seed is the binding constraint). Bars 0–199 are flat by record rule; the first decidable close is bar index 200 and its fill lands on bar 201's open. No signal before the seed window completes may trade. No repainting, no negative shift, no full-sample normalization; the 24/7 tape needs no session template (bar membership is the venue's own daily grid — deterministic).

## Execution assumptions

- Research market: `BTCUSDT` Binance USDT-M perpetual, `1d` decision frame, under the house overlay (declared port; the source venue is the pre-decimalization DJIA cash index — no cross-venue equivalence claimed beyond the same close-extreme penetration mechanics).
- Order timing (declared port of the paper's signal-following return cadence): completed-close decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill: entries and exits are single market orders on different bars by construction (entry at open T+1, exit at open T+11, next possible entry at open T+12 or later), so there is no same-bar dual-fire to sequence.
- Sizing/capital/costs: fixed 100%-equity single position at 1×, no adds, no leverage concept, no compounding concept beyond equity — declared derivative replacing nothing (the paper ships no sizing). The paper reports pre-cost signal-following returns, so derived evaluation must carry the explicit house overlay (pinned house fees at taker on both legs plus realized historical funding accrual across each 10-bar hold — long holds and short holds accrue at the realized rate in their respective directions; no hypothetical zero funding claimed anywhere; warmup, no-signal, and post-window flat spells are genuine non-accrual time). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one position on this single market at any time; re-entry after a window exit needs only the next fresh BUY/SELL signal (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The paper ships the full construction adopted here: resistance as the local maximum and support as the local minimum with the queued-investor rationale; `buying when the price rises above its last peak and selling when the price sinks below its last trough` (§I.B, short-phrase normalization); implementation `in accordance with the moving average strategy` with maximum/minimum prices `determined based on the past 50, 150, and 200 days`, `implemented with and without a one percent band` (§I.B); fixed 10-day holding-period returns following buy and sell signals in the same format as the FMA table (§II.C, Table IV headnote); DJIA daily index levels from the first trading day of 1897 to the last trading day of 1986, ~90 years (§I.A); returns measured as log differences of the index level (Table I headnote, §II.A); the 10-day choice is `arbitrary` with two-week returns tried to `essentially the same results` (fn. 8).

Pinned headline numbers (Table IV, full sample 1897–1986, (200, 0.01) row, transcribed digit-for-digit): N(Buy) 146, N(Sell) 124, Buy mean 0.0072/10-day (t 1.8551), Sell mean −0.0047/10-day (t −1.9795), fraction Buy>0 0.6164, fraction Sell>0 0.4677, Buy−Sell 0.0119/10-day (t 2.7846). Context adopted without porting: six-rule average buy-sell 0.0087 (≈0.86% in prose), all six reject the zero-spread null, six-rule average buy 0.0055 and sell −0.0024, unconditional 10-day mean 0.0017 (Table I, via the §II.B comparison). This record adopts zero performance numbers for BTCUSDT and claims no reproduced performance of any kind.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Return-study ceiling: every tradable-seeming result (spreads, t-ratios, Buy>0 fractions) describes the paper's DJIA signal-following return measurement — none transfers to a single-asset BTCUSDT derivative, and none is adopted as expected performance.
2. Interim-signal port: only the FMA definition sentences that `other signals occurring during this ten-day period are ignored`; the TRB section states fixed 10-day periods `in the same format as Table III` without re-sentencing interim handling. This record pins the FMA ignore rule for TRB windows as a declared derivation — a same-bar re-reading that queues or reverses on interim signals is a different, unpinned rule.
3. Closes-only rails: the source data are daily index *levels* — `HI_T`/`LO_T` are extremes of closes. Any replay using rolling highs/lows (Donchian-style) is a different, unpinned rule, and disputes are decided against such a replay, never patched by inference.
4. Preceding-window force: including the decision bar in its own reference window would make the buy leg unsatisfiable (`C_T > max(…, C_T) × 1.01` is impossible) — the paper's `preceding` exclusion is load-bearing, and this record's strict-exclusion pin follows it exactly.
5. Table IV headnote quirk: the headnote pastes Table III's `(short, long, band)` labels onto six rows that the §II.C prose maps to lookback ∈ {50, 150, 200} × band ∈ {0, 0.01} (`six tests`). This record reads rows as (lookback, band) per the prose; any labeling dispute is decided against this record.
6. Pre-cost accounting: the paper's returns are gross of transactions costs (its leverage illustration is explicitly `before transactions costs`), its cost regime is 1980s equities, and its series carries no dividends (fn. 10 — clean for BTC, which pays none either). Derived evaluation must survive the modern house fee-plus-funding load, disclosed, not assumed.
7. Signal sparsity: 146 buys and 124 sells across ~90 years (~3 signals/year on the DJIA tape). A 2017-onward BTCUSDT tape yields on the order of dozens of events — sampling error dominates any naive performance read, and this record claims none.
8. Contra-signal blindness: a breakdown one day after a breakout entry is discarded by the window rule and the full ten-bar adverse drift is ridden. Fixed-hold discipline and reversal agility are mutually exclusive here by declared pin, not by oversight.
9. Anti-cherry-pick: the (150, 0.01) row prints a larger buy-sell spread (0.0120) than the pinned (200, 0.01) row (0.0119) and is deliberately not picked — the 200-day pin rests on the predeclared longest-horizon rationale, never on the table ordering.
10. Siblings fenced: the paper's VMA persistent-state rule (already a separate pool record) and FMA crossover rule are different mechanisms with different trade events — neither is adopted, cited as support, or smuggled in through shared prose.
11. Subperiod silence: TRB subperiod results are `similar` and `not presented to save space` (fn. 12 carries the paper's own discussion) — no era-specific TRB claim is adopted from anywhere.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 200-close preceding extremes / strict ±1% penetration / fixed 10-bar hold with interim-signal ignore / close decision / next-open fills / single-position two-sided / time-only exit / `1d` BTCUSDT are frozen.

- F1 — Horizon relevance: replacing the pinned 200-day extremes with 150-day extremes (same band, same hold) must not improve net expectancy; fail ⇒ the longest-horizon leg carries no advantage over the paper's own faster neighbor.
- F2 — Band relevance: the no-band TRB-200 twin (penetration at the raw extreme, same hold) must not outperform the pinned 1%-band rule; fail ⇒ the whiplash guard is doing negative work and the pin is decorative.
- F3 — Direction-twin relevance: the fade twin on the identical grid (short penetrations above `HI × 1.01`, long penetrations below `LO × 0.99`, same 10-bar hold) must not outperform the pinned breakout mapping; fail ⇒ the resistance-broken persistence leg does not survive the port.
- F4 — Full-size relevance: replacing fixed 100%-equity sizing with fixed 50%-equity sizing must not improve risk-adjusted expectancy; fail ⇒ the declared size pin is doing unacknowledged work — or the record's size choice is arbitrary leverage in disguise.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid daily close on `1d` closes; extremes and band arithmetic with no venue-specific read). The arithmetic ports across perpetual venues without structural change. The short leg needs margin-short permission: a spot-only deployment expresses the long leg alone (a strict subset with a different event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session template, no cross-venue state. The 24/7 crypto tape prices weekends inside the 200-bar window by construction (200 bars ≈ 200 calendar days, while the source's 200 trading days span ~9.5 calendar months — disclosed calendar port, no equivalence claimed). Extension to other house-universe assets or lookbacks would be a different, unpinned claim.

## Limitations

- Single-asset port: the paper's evidence is a single DJIA index series; single-asset BTCUSDT behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- No executable fill in source: the paper is a signal-following return study with no fill convention; this record fills next open and holds ten bars against the paper's close-anchored 10-day windows. On gapping boundaries the two differ, and the difference is a declared derivation boundary — replication disputes are decided against this record's pin, never patched silently.
- No price stop, no interim exit: adverse excursion inside the ten-bar window has no guardrail and contra signals are discarded; the next decision is days away by construction. This is the source-faithful posture, disclosed as the record's principal risk.
- One-day decision latency: a penetration is acted on at the next open only; an immediate snap-back leaves the full window to be ridden — pinned, not recovered.
- Turnover lumpiness: signals arrive in clusters around trending episodes and vanish for months; cost load concentrates inside windows while flat spells earn nothing — pinned, not smoothed.
- Warmup cost: the first 200 bars are flat by record rule, so any textbook breakout completing inside warmup is deliberately untraded — pinned, not recovered.
- Sparse-event statistics: on the order of dozens of BTCUSDT events over the available tape — any future performance read needs small-sample discipline far beyond this admission record.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Brock, W., Lakonishok, J., LeBaron, B., Simple Technical Trading Rules and the Stochastic Properties of Stock Returns (The Journal of Finance, vol. 47(5), 1731–1764, December 1992 — full text read end to end in §§I.B/II.C with Table IV, retrieved 2026-10-13, 4,617,601 bytes, SHA-256 `b02f6dc1c68ff6758fc6c6ac96b3d34fa719ec693a16aaf949d03e8c90a95549): http://technicalanalysis.org.uk/support-and-resistance/BrockLakonishokLeBaron1992.pdf
- Same-paper teaching-host copy (byte pin cross-referenced with the sibling VMA record, retrieved 2026-10-13, 350,357 bytes, SHA-256 `9f9c2ab3e02ce9319cab5c5c115c711f6b5fb497b3ab5f19ce5f964245364b7a`): https://www.kevinsheppard.com/files/teaching/mfe/advanced-econometrics/Brock_Lakonishok_LeBaron.pdf
- Wiley publisher page (bibliographic cross-check, DOI 10.1111/j.1540-6261.1992.tb04681.x): https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1992.tb04681.x
