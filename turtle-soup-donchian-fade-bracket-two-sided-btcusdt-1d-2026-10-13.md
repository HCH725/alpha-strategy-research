---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Turtle Soup Donchian-20 false-breakout fade with 2.5N brackets and 10-bar channel exits two-sided on BTCUSDT 1d
created: 2026-10-13
updated: 2026-10-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-13
sources:
  - https://www.fmz.com/strategy/157372
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Turtle Soup Donchian-20 false-breakout fade with 2.5N brackets and 10-bar channel exits two-sided on BTCUSDT 1d

## Provenance

Primary source read end to end (canonical FMZ page plus its embedded executable source, fetched live over HTTPS during this cycle with HTTP 200, 668850 bytes of landing HTML):

- Canonical page: https://www.fmz.com/strategy/157372 — title `【海龟汤策略】反趋势交易策略` (Turtle Soup counter-trend strategy), page byline author `mwh264`. The ZH prose states the lineage plainly: the Turtle Soup rule named by Linda Raschke and Larry Connors in *Street Smarts* as the inverse of the Turtle system — fading, not following, the classic 20-period Donchian break (break of the 20-high is faded short, break of the 20-low is faded long), aimed at short-term false-breakout harvesting rather than week-to-month trend riding. The prose ships strategy characteristics (any timeframe, any pair, any exchange — recorded as venue-flexibility prose, never as engine evidence) and no performance figure of any kind (see Evidence).
- Embedded executable source read in full (the page ships the complete strategy `source` block, not a stub): order-affecting lines are the warmup gate (`records.length <= 50` skip), the volatility read (`TA.ATR(records, 20)`, last value `N`), the four channel reads (`TA.Highest/Lowest(records, 20, ...)` for entries, `TA.Highest/Lowest(records, 10, ...)` for full-side exits), the two flat-side entry legs (ask `sell1 <= lowest20` buys long; bid `buy1 >= highest20` sells short), the adverse scale-in (each side adds while its bet counter is below `max_positions = 4` once price moves a further `0.5*N` against the last unit), the per-unit bracket exits (long unit: stop `entry - 2.5*N`, target `entry + 2.5*N`; short mirrored), and the full-side channel exits (all longs close when bid `>= highest10`; all shorts close when ask `<= lowest10`), plus the exchange-liquidation sync that clears the trackers when the venue holds no position.
- Text census over the embedded block: `TA.ATR(records, 20)` x 1 / `TA.Highest(records, 20` x 1 / `TA.Lowest(records, 20` x 1 / `TA.Highest(records, 10` x 1 / `TA.Lowest(records, 10` x 1 / `max_positions=4` x 2 / `2.5*N` x 8 (four long-bracket plus four short-bracket assignments) / `0.5*N` x 2 (both add legs) / `perform_limited_order` x 10 (2 entries + 2 adds + 2 unit-stops + 2 unit-targets + 2 full-side closes) / `records.length` gate x 2 / `GetRecords` x 1. Unit sizing is coded as `position_unit = account.Stocks / (max_positions * 2)` (one eighth of equity per unit — portable fraction, adopted below). No trailing, no partial, no time exit, no opposite-signal exit ships anywhere — recorded as explicitly absent, never as defaults to assume.
- Immutability fence: the immutable mirror `fmzquant/strategies` was verified at HEAD `7853bb2bf262c4567ac238d3552d97f0e50cb801` (via `git ls-remote` plus a local blobless clone `rev-parse` in-cycle — the same head pin as the merged 1-3-1, Inside-Bar-Failure, Percent-B-MFI and further admissions) and its full 5807-file tree searched for `157372` / `龟汤` / `turtle.soup`: zero hits — no immutable mirror file exists for this strategy. This record therefore pins the live page fetch plus the frozen in-cycle census above; the auditor must re-fetch the canonical page. FMZ-page mutability is fenced in Limitations.
- Licence and rights: the embedded block ships a `strategy_version` learning-use banner and a contact line; this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly five: (1) market/frame pin `BTCUSDT` on Binance USDT-M perpetuals, `1d` frame (the source claims any timeframe/pair/venue and its coded venue defaults reference OKCoin futures — no cross-venue equivalence is claimed beyond the same daily-bar Donchian/ATR mechanics); (2) completed-bar close-confirmed discretization (the source polls live bid/ask every 3 seconds against trailing extremes; this record evaluates entries on completed-bar closes against strictly-prior windows and fills at the close — tick-intrabar touch-then-reclaim paths are scoped out, disclosed here); (3) resting-level fill model with the fixed same-bar order below (the source fires limit orders into live touches; this record freezes daily-bar touch fills, disclosed as an approximation); (4) adopted 50-bar warmup with pre-warmup bars flat by record rule (covers the coded `records.length > 50` gate plus the ATR-20/Donchian-20 seeds with margin — see Required data); (5) house sizing/capital/costs replacing the `Stocks/8` equity stub and the template-library order plumbing (see Execution assumptions). The 20-bar fade entries, the 0.5N adverse scale-in to 4 units per side, the per-unit 2.5N stop/target brackets, the 10-bar full-side channel exits, the two independent concurrent legs, and the bracket-plus-channel-only exit posture are source-native and unmodified.

Pre-write dedup (2026-10-13): case-insensitive working-tree searches for `soup`, `turtle`, `donchian`, `false.break`, `fakeout`, and `turtle.soup` return no strategy record using this source or mechanism. Closest pool records differ in mechanism class: `turtle-system-2-55d-breakout-2n-stop-half-n-add-two-sided-btcusdt-1d-2026-10-12.md` FOLLOWS the 55-day breakout with 2N stops, half-N winner adds, 20-day breakout exits and a single-net state (this record FADES the 20-bar break, scales the loser at 0.5N, brackets every unit at 2.5N, exits the side on the 10-bar channel, and runs two concurrent independent legs — opposite direction, different lengths, different risk, different state); `donchian-20-10-breakout-btcusdt-1h-2026-10-06.md` is a long-only breakout-follow with no coded stops (this record is two-sided fade with per-unit brackets); `inside-bar-failure-fade-time-exit-two-sided-btcusdt-1d-2026-10-13.md` fades inside-bar range contraction with a time exit (this record fades Donchian extremes with bracket-plus-channel exits — different pattern, different risk). Open `research/*` PRs are only #48 (Larry Williams 3-EMA streak long), #49 (Gaussian channel StochRSI breakout long), #63 (SuperTrend flip long), #89 (Chandelier Exit long), and #92 (SSL channel reversal two-sided) — no Turtle, Donchian, or false-breakout overlap in open, merged, or closed PRs. Five-axis distinction: no pool record and no open PR fades confirmed Donchian-20 extremes with adverse 0.5N scale-in, per-unit 2.5N brackets, and 10-bar channel full-side exits on two concurrent legs. Not a trivial parameter variant.

## Economic mechanism

### Source-reported

Positioning against trapped breakout traders: wherever a channel-breakout system enters, resting stops and late breakout entries concentrate just beyond the old extreme; when the break fails, both crowds sit on the wrong side at once. The design therefore waits for the break itself (no anticipation — the extreme must print) and takes the opposite side, averaging the fade up to 4 units as the failure deepens by fixed volatility steps, bracketing every unit so that any single unit can pay at most 2.5N to make 2.5N, and abandoning the whole side only when price reclaims the nearer 10-bar channel (the failure thesis is dead). The prose claims no indicator edge and no regime filter — the edge, as argued, is structural positioning, and the record fails outright whenever the breakout turns out to be real (see Negative evidence).

### Research interpretation

Two-legged false-breakout fade machine, event-driven, two-sided, bracket-and-channel risk. Unlike every breakout-follow record in the pool (Turtle System 2, Donchian-20-10, Dual-Thrust) this system needs the breakout to EXIST before it acts, then bets the other way: clean continuation bars that never look back pay the breakout records and starve this one by construction. Unlike the inside-bar fade there is no contraction pattern and no time exit: the trigger is a 20-bar extreme print, and the exits are price levels only (per-unit brackets plus the side-wide 10-bar reclaim). Unlike oscillator mean-reversion there is no level, no smoothing, no band: the signal is pure Donchian geometry plus one ATR ruler. The scale-in deserves its honesty label: adds go against the trade (averaging down a fade), so every add doubles down on the failure thesis while the per-unit brackets keep each unit's loss capped — the record can lose up to 4 bracketed units per side if the breakout is genuine. This port is research interpretation, not source-reported fact.

## Signal

Frozen parameters (any other value is a different, unpinned rule): `entry_len = 20` / `exit_len = 10` / `N_len = 20` / `add_step = 0.5N` / `bracket = 2.5N` / `max_units = 4` per side / `tick = 0.01 USDT` / `lot = 0.001 BTC`.

Volatility (source-native formula, FMZ `TA.ATR` Wilder form, frozen to completed bars):

```text
TR_t = max(H_t - L_t, |H_t - C_{t-1}|, |L_t - C_{t-1}|)
N_seed = SMA20 of the first 20 TR values
N_t = (19 * N_{t-1} + TR_t) / 20        // N for bar-t decisions uses bars through t
```

Reference levels for bar `t`, frozen from completed bars only (causal — nothing reads bar `t` or later):

```text
LL20(t) = min(L_{t-20..t-1})            // long fade trigger
HH20(t) = max(H_{t-20..t-1})            // short fade trigger
LL10(t) = min(L_{t-10..t-1})            // short side full-exit level
HH10(t) = max(H_{t-10..t-1})            // long side full-exit level
```

State machine (two independent legs; longs and shorts may coexist — source-verbatim dual arrays):

```text
long side flat + close_t <= LL20(t)  -> buy 1 unit at close_t (fill: close_t)
  SL_1 = entry - 2.5 * N_t, TP_1 = entry + 2.5 * N_t
long side k units (k < 4) + close_t <= last_long_entry - 0.5 * N_t
  -> buy 1 unit at close_t, own SL/TP at entry -/+ 2.5 * N_t (at most one add per side per bar)
short side mirrors with close_t >= HH20(t) entries, adds at last_short_entry + 0.5 * N_t,
  SL_i = entry + 2.5 * N_t, TP_i = entry - 2.5 * N_t
```

Exit resolution on bar `t` (fixed order, stop-first, predeclared derivation; brackets arm from the bar AFTER entry, so fresh entries are never evaluated for exit on their entry bar):

```text
(1) per-unit stops of pre-existing units: long unit exits at its SL if low_t <= SL
    (short: high_t >= SL -> exit at SL)
(2) per-unit targets of survivors: long unit exits at its TP if high_t >= TP
    (short: low_t <= TP -> exit at TP)
(3) full-side channel exits of remaining units: all longs exit at HH10(t) if high_t >= HH10(t);
    all shorts exit at LL10(t) if low_t <= LL10(t)
(4) adds on surviving sides (at most one per side, fill at close_t, brackets arm next bar)
(5) fresh-side entries (fill at close_t, brackets arm next bar)
```

Direction: two-sided with independent legs. No always-in-market claim: flat sides before the first signal, after bracket/channel exits, and during warmup are explicit. Re-entry after any flat side needs only the next qualifying close — no cooldown specified, explicitly none, not invented. The source's exchange-liquidation sync has no single-engine-backtest counterpart and is scoped out (disclosed here, never silently kept).

## Required data

- `1d` bars of one pair: `open` (gap awareness only — no order-gating line reads it), `high` (short entries/adds reference via close only; long targets, short stops, long-side channel exits), `low` (long stops, short targets, short-side channel exits), `close` (entries, adds, TR chaining). No volume, funding, OI, mark/index, L2, sentiment, session, or cross-market input anywhere in the signal path.
- Warmup is derivable and exact: the coded gate demands more than 50 records before any order, and the ATR-20 plus Donchian-20 seeds are subsets of it — the first 50 completed `1d` bars are flat by record rule; the first tradable bar is bar 51. Before that, all levels are undefined and the record holds flat — deterministic, no invention.
- No repainting, no negative shift, no full-sample normalization, no unfinished-bar read: every level for bar `t` is a function of bars `< t` (N_t additionally reads bar `t`'s own completed range — pure history reference at decision time, no future).

## Execution assumptions

- Research market: `BTCUSDT` Binance USDT-M perpetual, `1d` decision frame, under the house overlay (declared port; the source's coded venue defaults reference OKCoin futures — no cross-venue equivalence claimed beyond the same daily-bar Donchian/ATR mechanics).
- Order timing (predeclared derivation): completed-bar close fills for entries and adds; resting-level touch fills for per-unit brackets and full-side channel exits with the fixed stop-first same-bar order above; brackets arm from the bar after entry. Compatible with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) on the same first-touch stop-resolution path as the admitted Turtle-System-2, 1-3-1 fixed-1R, and Williams-Fractal fixed-RR records — no maker-touch, queue, or partial-fill claims; limit-order aspiration from the template plumbing is disclosed as approximated by touch fills, with the 3-second live-poll path explicitly scoped out.
- Sizing/capital/costs: the coded `Stocks / 8` equity fraction is preserved as the position-size rule (each unit = 12.5% of equity notional at signal time, Isolated 1x, no borrow — the source states no leverage, so none is claimed); maximum exposure is bounded by record rule at 8 concurrent units (4 long + 4 short). Pinned Binance non-VIP USDT-M fees costed at taker (conservative vs the limit aspiration) plus realized historical funding accrual while positioned (long or short) — no hypothetical zero funding claimed anywhere.
- Concurrency: at most 4 units per side on this single market; no second market, so no portfolio caps, selection, or rollover exist — not-applicable by construction on a non-expiring single perp, disclosed, never silently kept. No house DCA overlay is admitted: the source's own 0.5N scale-in already layers entries, so any house safety-order layering would change trade events and would be a different, unpinned strategy (fenced, same as the 1-3-1 record).

## Evidence

### Source-reported

The strategy page and its embedded source ship no performance table, figure, backtest, win rate, or return claim of any kind — this record therefore carries strictly zero performance figures, source-reported or otherwise. The only numbers on the page are definitional (20/10 channels, ATR-20, 0.5N adds, 2.5N brackets, 4 units, 3-second poll, 50-record gate). The page's view/hit counters are traffic metadata, never performance evidence.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The breakout-following twin is a different, already-admitted record: `turtle-system-2-55d-breakout-2n-stop-half-n-add-two-sided-btcusdt-1d-2026-10-12.md` trades WITH the break (55/20, 2N stops, winner adds, single-net state). This file trades AGAINST the break and must never be read as evidence about that system, nor that file as evidence about this fade.
- The `年化80%，最大回撤16%` (80% annualized, 16% max drawdown) prose visible on the same FMZ page belongs to related strategy #289308 (`海龟策略btc现货版`, a classic Turtle-follow port) — NOT to this Turtle Soup record. It is fenced here so no reviewer mistakes sidebar prose for this file's evidence.
- Turtle Soup Plus One (the next-day reclaim variant documented in liquidity literature) is NOT traded here: the embedded code carries the reclaim stop on the break bar only, with no one-session carry. Listed so no reviewer mistakes this file for the Plus-One variant.
- Discretionary ICT/MSS-gated liquidity-sweep variants (market-structure-shift confirmation, liquidity-pool targets) are NOT this record: this file's confirmation is the completed-bar Donchian print plus fixed ATR arithmetic only.
- Trailing-stop, partial-profit, breakeven-move, time-exit, and opposite-signal-exit legs are absent in source and recorded as explicitly disabled, not as defaults to assume. The complete closing set is exactly: per-unit 2.5N stops/targets plus the side-wide 10-bar channel reclaim exit.
- The fade can lose up to 4 bracketed units per side when a breakout is genuine: averaging down concentrates exposure precisely where the thesis is wrong — downstream must size accordingly. Any downstream overlay (house DCA, drawdown shrink, second market) would change trade events and would be a different, separately specified strategy.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 20/10 lengths / ATR-20 Wilder / 0.5N adverse adds / 2.5N brackets / 4-units-per-side / two independent legs / BTCUSDT 1d / close-confirmed entries with touch-fill brackets are frozen.

- F1 — Fade relevance: a breakout-follow twin (entries inverted to follow the 20-bar break, same brackets, adds flipped to the favorable side, same channel exits, same fills) must not improve net expectancy; fail ⇒ fading adds nothing over following on this geometry.
- F2 — Bracket relevance: removing the per-unit 2.5N stops/targets while keeping entries, adds, and channel exits (same fills otherwise) must not improve net expectancy; fail ⇒ the coded brackets add nothing over their unbracketed twin.
- F3 — Add relevance: single-unit-only per side (no 0.5N adverse adds, same entries/brackets/exits) must not improve net expectancy; fail ⇒ averaging-down adds nothing over its single-unit twin.
- F4 — Exit-length relevance: a 20-bar channel full-side exit twin (same entries, adds, brackets) must not improve net expectancy; fail ⇒ the 10-bar reclaim adds nothing over its slower twin.

## Crypto portability

Perpetuals never expire, so contract rollover is structurally absent (not silently ignored). 24/7 trading removes pit-session gaps; touch-fill levels then bind on volatility jumps only, still deterministic. Shorts are native to USDT-M margin (no uptick rule, no borrow desk). Tick (0.01 USDT) and lot (0.001 BTC) granularity are stated above. Single-market porting drops any multi-market breadth the lineage literature discusses — this record makes no diversification claim and must not be read as the book's system. Funding accrues on both legs while positioned and is flagged realized-accrual, never zero-by-default.

## Limitations

- Completed-bar discretization is an approximation of the 3-second live bid/ask poll, not tick fills; intrabar touch-then-reclaim paths that the source would trade are missed on purpose — fills at close/level are the frozen model.
- One-add-per-side-per-bar and next-bar bracket arming are researcher discretizations where the source follows the live path; same-bar multi-event bars resolve by record rule, disclosed above.
- FMZ-page mutability: no immutable mirror file exists for this strategy at the verified mirror HEAD, so future fetches may differ — the in-cycle byte count (668850), author byline (`mwh264`), and code census above freeze what was actually read.
- Fixed equity-fraction sizing with no drawdown shrink and no stated leverage: deeper adverse runs than a shrink rule would permit — downstream must size accordingly.
- Funding is flagged as realized-accrual, not yet verified against a funding-accounting implementation; representative event-level Qlib/Hummingbot parity is required before any mass screening, not claimed here.

## Implementation status

Not implemented. No code was executed and no Hummingbot/Qlib/n8n run was performed in this cycle; all compatibility statements above refer to the pinned-model path shared with the admitted stop-target records.

## Adoption boundary

Research-only. Not approved for Paper, Testnet, or Live trading. No downstream screening, sizing, or deployment authorization is granted by this record.

## Related Wiki records

None.

## Sources

- https://www.fmz.com/strategy/157372 (primary — canonical FMZ page `【海龟汤策略】反趋势交易策略`, byline `mwh264`, fetched 2026-10-13 over HTTPS with HTTP 200, 668850-byte landing HTML with the complete executable JS source embedded and read end to end; prose lineage credits Raschke/Connors *Street Smarts*; no immutable mirror file — 5807-file tree of `fmzquant/strategies@7853bb2b` searched with zero hits, disclosed above)
