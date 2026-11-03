---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TradingView displaced-Donchian decycler-slope MFI-gated ATR-bracket two-sided on BTCUSDT 1h
created: 2026-11-03
updated: 2026-11-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-11-03
sources:
  - https://www.tradingview.com/script/LkgKT3TG-Displaced-Donchian-Decycler-Trend-Breakout-Strategy-with-MFI/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView displaced-Donchian decycler-slope MFI-gated ATR-bracket two-sided on BTCUSDT 1h

## Provenance

Primary source identity verified end to end (page fetched live and read 2026-11-03; full Pine source read line by line, 141 lines):

- TradingView OPEN-SOURCE SCRIPT `Displaced Donchian Decycler | Trend Breakout Strategy with MFI` by publisher `blitz_algo`, stable URL `https://www.tradingview.com/script/LkgKT3TG-Displaced-Donchian-Decycler-Trend-Breakout-Strategy-with-MFI/` (script ID `LkgKT3TG`). Page header confirms `OPEN-SOURCE SCRIPT`; description confirms the four legs adopted below (displaced Donchian trigger on bars 31–36 back, two-pole Ehlers-style decycler trend filter, smoothed-MFI 50 gate, entry-latched 2/3 ATR stop/target with Donchian-flip close). No invite-only, paywall, or login wall on the logic.
- Pinned declaration (source lines 4–7): `//@version=6`, `strategy("Displaced Donchian Decycler Strategy", shorttitle="DDDS", overlay=true, initial_capital=10000, default_qty_type=strategy.percent_of_equity, default_qty_value=100, commission_type=strategy.commission.percent, commission_value=0.05, pyramiding=0)`. No `process_orders_on_close` argument anywhere (Pine default = next-bar-open market fills); no `calc_on_every_tick`; no `request.*`/`security(`; no `strategy.order` — only `strategy.entry`/`strategy.close`/`strategy.exit`.
- Pinned inputs (defaults frozen, source lines 21–35): `startLen=31, endLen=36, allowLongs=true, allowShorts=true, useDecycler=true, decPeriod=60, slopeBars=3, useMFI=true, mfiLen=14, mfiSmooth=4, atrLen=14, stopMult=2.0, tpMult=3.0` (four remaining inputs are display-only colors/toggles).
- Licence and rights: source header reads `MPL-2.0 / © blitz_locked`; this record cites and normalizes the rule (short phrases and definitional recurrence only) and reproduces no extended prose, figures, or performance numbers.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the source's breakout-plus-filter-plus-bracket construction ported to BTCUSDT 1h with fixed sizing and close-evaluated fills — not a lossless reproduction of the author's chart setup. Researcher-declared adaptations are exactly five: (1) single-asset BTCUSDT Binance USDT-M perpetual venue (the author ships no venue; both legs default enabled so the short permission is genuinely used); (2) fixed 0.01 BTC 1× sizing replacing the author's aggressive 100%-of-equity compounding; (3) completed-bar-close decision with same-bar-close market fills for entries/reversals/flip-closes, and close-evaluated market exits for the ATR bracket (the author ships next-bar-open entries plus intrabar stop/limit — the established close-evaluated conversion class already used by admitted pool records, e.g. the Forven-sibling same-bar-close lane and the PR #414/#590/#592/#594/#596 conversion class cited in an admitted record); (4) explicit research cost overlay of 0.05% per side (the author's declared commission) plus realized funding while in position — never hypothetical zero funding; (5) structural 100-completed-bar warmup (the author ships none — first fully defined signal needs bar 36). The displaced window, decycler recurrence, MFI construction, strict-inequality gates, sticky-state priority, entry latch, bracket multiples, and no-cooldown stance are source-faithful. This record is therefore never evidence that the author's script passes.

Pre-write dedup (2026-11-03): working-tree base is current `main@b9fcff6d` (534 root strategy records). Case-insensitive content searches for `LkgKT3TG`, `blitz_algo`, `DDDS`, and `displaced donchian` return zero strategy records; `decycler` returns only fencing prose plus the single decycler *strategy* `ehlers-decycler-oscillator-cross-long-flat` (a fast-vs-slow oscillator-line cross, long-flat — no Donchian window, no MFI gate, no bracket); the ten Donchian pool records all trade current-window bands (7/20/50, prior- or same-bar) — none displaces a 5-bar slice 32–36 bars back. All 16 open `research/*` PRs enumerated by number/title/branch — none is this script, publisher mechanism, or construction. Nearest pool records differ on every axis: `ehlers-decycler-oscillator-cross` (oscillator cross, no level/slope filter, long-flat, no risk legs); current-window Donchian breakout records (no displacement, no decycler, no MFI-50 gate). Five-axis distinction: no pool record and no open PR conditions exposure on a 32–36-bar-displaced Donchian flip gated by decycler level-plus-slope and smoothed-MFI 50 with an entry-latched 2/3 ATR bracket.

## Economic mechanism

### Source-reported

Mature-range breakout with trend and money-flow confirmation: breaking an older (already settled) range means more than breaking yesterday's noise; the cycle-removed trend line must agree in level and slope; volume-weighted money flow must agree in sign; and every accepted trade carries a volatility-sized stop/target latched at entry so risk scales with the market that printed the signal. (Author's Tips/Warnings framing fenced: trending markets suit it, chop whipsaws it, defaults are aggressive — mechanism only, never adopted as a crypto claim.)

### Research interpretation

Displaced-level breakout, two-sided, hourly cadence. Unlike current-window Donchian records the trigger level is a settled 5-bar slice more than thirty bars old, so fresh micro-structure cannot print its own trigger. Unlike oscillator-cross records there is no cross event anywhere — the state is a sticky latch that only flips on a genuine old-range break, and the decycler is a level-plus-slope filter, never a signal line. Unlike stop-less regime holds every position carries a static entry-latched bracket plus a filtered-flip close. The bet, as derived, is purely that old-range breaks confirmed by detrended level/slope and money flow port to BTCUSDT hourly bars — and whipsaw stretches pay the bracket, disclosed, with no tuning inside this record.

## Signal

Exact rule as pinned (hourly decision on completed `1h` bars; close-evaluated market fills; two-sided — any other window, period, threshold, sizing, or fill is a different, unpinned rule):

- R1 — Measure grid: completed `1h` bars of BTCUSDT only. All references are to completed bars; no provisional intrabar value is ever used.
- R2 — Decycler (two-pole Ehlers-style on `close`, `decPeriod=60`, source lines 45–54): `ang = 0.707·2π/60 = 0.07403687`; `alpha = (cos(ang)+sin(ang)−1)/cos(ang) = 0.07142544`; `decay = 1−alpha = 0.92857456`; `gain = (1−alpha/2)^2 = 0.92984996`; `hp[t] = gain·(C[t]−2·C[t−1]+C[t−2]) + 2·decay·hp[t−1] − decay²·hp[t−2]` with `hp = 0` for `bar_index < 2` (deterministic seed, pinned transient); `dec[t] = C[t] − hp[t]` (constants recomputed independently this cycle, exact match).
- R3 — Displaced Donchian (source lines 59–64): `hh[t] = max(H[t−31..t−35])`, `ll[t] = min(L[t−31..t−35])` (loop `31` to `endLen−1 = 35`); breakout tests use `hh[t−1]`/`ll[t−1]`, so the effective window is `H[t−32..t−36]` / `L[t−32..t−36]` — pinned.
- R4 — Sticky state (source lines 66–74, priority pinned): `var state = 0`; `if H[t] > hh[t−1] → 1`; `if L[t] < ll[t−1] → −1` (the second `if` wins on double-fire — both tests can fire on one violent bar, pinned short-wins); `flipLong = (state == 1 and state[1] != 1)`; `flipShort = (state == −1 and state[1] != −1)` (mutually exclusive by construction — same-bar dual-fire is arithmetically impossible).
- R5 — Filters (source lines 79–85, strict inequalities pinned): `mfi = SMA(ta.mfi(hlc3, 14), 4)`; `atr = ta.atr(14)` (Wilder RMA of true range); `decLong = (C > dec and dec > dec[3])`, `decShort = (C < dec and dec < dec[3])`; `mfiLong = (mfi > 50)`, `mfiShort = (mfi < 50)` (`useDecycler`/`useMFI` pinned enabled — disabling either is a different, unpinned rule).
- R6 — Entries (source lines 87–100, both legs live at defaults): `longSignal = flipLong and decLong and mfiLong`; `shortSignal = flipShort and decShort and mfiShort`; signal-bar market entry of fixed 0.01 BTC 1×, filled at that bar's close (declared conversion of the author's next-open fill). Opposite signal while in position reverses at the same close (net flip, `pyramiding=0` — author's `strategy.entry` netting, pinned).
- R7 — Flip close (source lines 103–106, conditional second path, pinned as-is): long closes (`Flip`) iff `flipShort and not shortSignal`; short closes iff `flipLong and not longSignal` — i.e. only when the Donchian state turns but the new side is filter-blocked; when the new side passes its filters the reversal entry (R6) is the closing path instead.
- R8 — ATR bracket (source lines 93–116, entry-latched, static per trade): `entryATR = atr` of the signal bar, re-latched only on a new signal; long bracket `stop = avg_price − 2·entryATR`, `limit = avg_price + 3·entryATR` (mirror short); evaluated as market exits at completed-bar closes from the first close after the entry bar (declared conversion of the author's intrabar `strategy.exit`, with the source-native one-bar protection gap mirrored — the bracket is not live on the entry bar itself).
- R9 — Risk legs (pinned absence, not invented): no trailing, no time exit, no cooldown, no adds/partials/pyramiding — explicitly none, matching the author's shipped behavior.
- R10 — Warmup and gaps: flat until 100 completed `1h` bars (structural need is bar 36 for `hh[t−1]`; 100 covers MFI-SMA, ATR seeding, and decycler-seed decay — pinned, not recovered). Missing-bar stretches freeze evaluation at the prior target — never backfilled, never forced flat.
- R11 — Invariant identifier: `TV:blitz_algo-LkgKT3TG|DDDS_disp31-35_dec60_slope3_mfi14x4_atr14_2x3|independent-derived-v1|BinanceFutures:BTC-USDT:1h|TWO-SIDED|closeeval-MARKET|fee0.0005|lev1x|size0.01|warmup100|2026-11-03` (any constant, window, threshold, direction, sizing, or cost change is a different derivative).

## Required data

- Completed `1h` bars of BTCUSDT only: `open`/`high`/`low`/`close` (displaced window, state flips, decycler, MFI via `hlc3`, ATR, fill prices). No volume-gated order (volume never enters any predicate), no funding/OI/mark-index read gates any order, no sentiment/macro/on-chain/cross-venue state.
- Single decision grid: one evaluation per completed-bar close; entries/reversals/flip-closes fill at that close; bracket legs are close-evaluated market exits. All inputs are completed-bar values.
- Warmup: flat until 100 completed bars (structural). No repainting, no negative shift, no future reference, no full-sample normalization (every leg is a trailing statistic; boundaries are constants).

## Execution assumptions

- Research market: BTCUSDT Binance USDT-M perpetual, 1×, fixed 0.01 BTC per entry, no adds, no leverage, no compounding concept beyond the position. Both legs default-enabled, so the short permission is genuinely used (unlike long-flat ports that fence the short side).
- Order timing (declared close-evaluated conversion; the author ships next-open entries plus intrabar stop/limit): completed-bar-close decision with same-bar-close market fills for entries/reversals/flip-closes and close-evaluated market exits for the bracket — the same lane primitive admitted Forven-sibling records use, in the PR #414/#590/#592/#594/#596 conversion class cited by an admitted record. No maker-touch, queue, or intrabar-path-dependent fill is claimed. R4's mutual-exclusion proof leaves no ambiguous same-bar fill order; the bracket's one-bar protection gap is mirrored, not fixed.
- Sizing/capital/costs: fixed 0.01 BTC per entry; explicit research cost overlay 0.05% taker fee per side (the author's declared commission) plus realized funding while in position (long or short) — no hypothetical zero funding is claimed anywhere. The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one position at any time (`pyramiding=0`); reversal nets at a single close so overlapping entries are structurally impossible; no cooldown — explicitly none, not invented. Single engine position; no shared portfolio state, no multi-pair logic. Safety orders: explicitly none.

## Evidence

### Source-reported

The script page ships every adopted headline fact quoted in Provenance: the 31–36-back displaced window, the two-pole decycler trend filter with slope check, the smoothed-MFI 50 gate, the entry-latched 2/3 ATR stop/target, the Donchian-flip close, both-legs-enabled defaults, 100%-equity sizing, and 0.05% commission. It ships zero adopted performance numbers for this record: no return, win-rate, drawdown, or trade-count figure from any Strategy-tester tab is adopted anywhere — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Logic checks executed during this scout cycle (independent Python reference of R2–R4 as printed; synthetic tapes only — no real-market replay, no profitability figure):

- Constants: `ang = 0.07403687, alpha = 0.07142544, decay = 0.92857456, gain = 0.92984996` recomputed from the printed formula — exact match to eight decimals.
- Dead-flat 60-bar tape: zero state flips, zero signals (no phantom entry).
- Flat tape plus one +20% high-break bar at bar 60: `flipLong` fires exactly once at bar 60 (`hh[1] = 100 < H = 120`), long state latches.
- Double-fire bar (`H = 120, L = 80` against `hh[1] = ll[1] = 100`): state resolves to −1 (second-if-wins priority verified).
- Flat-tape decycler: `dec == close` exactly (seed transient is identically zero on constant input — deterministic, no NaN path).

### Negative evidence

1. Fill-conversion lag fenced: the derived close-evaluated fills lag the author's next-open entries by up to one full `1h` bar and the bracket exits trade intrabar extremes for close prints — fast reversals give back more than the author's tester would show. This is the coded trade, disclosed, not a tunable parameter here.
2. Whipsaw exposure fenced: in a range-bound tape the displaced latch flips repeatedly while both filters flicker, printing fee-paying round trips against the static bracket — the author's own Tips/Warnings say exactly this. No win-rate or expectancy claim survives it here.
3. Number silence fenced: no tester-tab return, win-rate, profit-factor, drawdown, or trade count from the script page is adopted anywhere, and any dispute over exact magnitudes is decided against this record, never patched by inference.
4. Derivation boundary fenced: the only non-author behavior is the five declared adaptations (venue, fixed sizing, close-evaluated fills, house costs, 100-bar warmup); the displaced window, decycler recurrence, MFI construction, strict gates, state priority, latch, bracket multiples, and no-cooldown stance are source-faithful. This record is therefore never evidence that the author's script passes.
5. Fully exposed inside the bracket: once in a trade, an adverse excursion beyond the static stop that never prints a qualifying close is ridden to the next close by construction — the conversion's cost, disclosed.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `31–36` displacement / `decPeriod 60` / `slopeBars 3` / `mfi 14×4` / `atr 14` / `2×/3×` bracket / strict inequalities / short-wins priority / close-evaluated fills / fixed 0.01 BTC 1× two-sided / BTCUSDT `1h` are frozen.

- F1 — Displacement relevance: a current-window twin (`startLen = 1, endLen = 6`, same filters/bracket/fills) must not improve net expectancy; fail ⇒ the displacement pin adds nothing over an ordinary Donchian break and the mature-range story is decorative.
- F2 — Filter relevance: an unfiltered twin (decycler and MFI gates forced pass, same window/bracket/fills) must not improve net expectancy; fail ⇒ the two filters are fee-burning decoration on a bare displaced flip.
- F3 — Bracket relevance: a flip-only twin (bracket legs removed, exits by reversal/flip-close only) must not improve net expectancy; fail ⇒ the entry-latched 2/3 bracket destroys more expectancy than it protects.
- F4 — Selectivity relevance: buy-and-hold over the same sample must not improve net expectancy; fail ⇒ sitting out non-signal hours costs more in missed drift than it saves in avoided chop.

## Crypto portability

Pinned to BTCUSDT Binance USDT-M perpetual (decision grid completed `1h` bar closes; fills at those closes; no venue-specific read). The arithmetic ports across perpetual venues without structural change (no corporate-action or calendar adjustment exists to recheck; a spot-only deployment expresses the long-leg event set — pinned, not approximated — while the short leg requires a margin venue). Extension to other house-universe assets, timeframes, windows, thresholds, or multiples would be a different, unpinned claim.

## Limitations

- Single-asset port: the author's evidence is a generic chart script with no venue pin; BTCUSDT hourly breakout behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Conversion lag: close-evaluated fills plus close-evaluated bracket deviate from the author's next-open/intrabar execution on every fast bar — the derived event set is its own object, never the author's tester output.
- Double-fire rigidity: simultaneous both-side breaks resolve short-wins by code order, never by bar-internal sequencing — a pinned artifact, not a market claim.
- Seed transient: the `hp = 0` seed makes the first ~60 decycler prints a deterministic warmup artifact — fenced by the 100-bar warmup, never traded.
- Warmup cost: everything before the first 100 completed bars is flat by record rule, so early history is deliberately untraded — pinned, not recovered.
- One-bar protection gap: the bracket is not live on the entry bar by mirrored construction — a gap against the fresh position is taken at the next close, never at the edge.

## Implementation status

not-implemented. No Hummingbot controller/executor has been written for this record; the Execution assumptions section names the exact pinned engine path (package `20260920`, VERSION `dev-2.17.0`, completed-`1h`-close decision, same-bar-close market entries/reversals/flip-closes, close-evaluated market bracket exits, single-asset fixed 0.01 BTC 1× two-sided) that a future implementation must target, with representative event-level Qlib/Hummingbot parity required before any mass screening.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. `hb_ready_status: PASS` here is the Scout's evidence-backed admission proposal for this independent derivative only, pending independent Hermes Auditor exact-head review — not self-approval, not profitability, not Qlib parity, not source-equivalence, not live-tradable. Only the independent reviewer may remediate source-verifiable facts, exact-head merge on six-gate PASS, or close as NOT_LOSSLESS.

## Related Wiki records

None.

## Sources

- blitz_algo (2026). Displaced Donchian Decycler | Trend Breakout Strategy with MFI (Pine v6, `DDDS`, MPL-2.0 / © blitz_locked, 141-line open-source script, defaults as pinned). https://www.tradingview.com/script/LkgKT3TG-Displaced-Donchian-Decycler-Trend-Breakout-Strategy-with-MFI/ (OPEN-SOURCE SCRIPT page plus full source read end to end live 2026-11-03; `source_as_of` is the verification date — no author publication-date claim is adopted)
