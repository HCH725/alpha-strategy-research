---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Aroon-oscillator midline-cross rail-exit two-sided on BTCUSDT 1d bars
created: 2026-10-09
updated: 2026-10-09
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-01-15
sources:
  - https://www.fmz.com/strategy/438795
  - https://www.tradingview.com/pine-script-reference/v2/
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Aroon-oscillator midline-cross rail-exit two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (FMZ canonical strategy page plus its full Pine block via the page-linked public mirror, fetched 2026-10-09):

- Canonical page: https://www.fmz.com/strategy/438795 (`Aroon Oscillator Based Stock Trading Strategy`, FMZ `Common strategy`, author nickname `ChaoZhang`, page `Created: 2024-01-15 14:08:33`, adopted as `source_as_of`). The same author publishes other FMZ strategies, but no pool record or open PR shares this canonical URL or its Aroon-oscillator mechanism (see dedup below).
- Page-embedded backtest header (verbatim substance): `period: 1h`, `basePeriod: 15m`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`, window `2023-12-15 00:00:00` to `2024-01-10 00:00:00`. The window is cited as provenance only: the page ships no returns, win rate, profit factor, trade count, or cost basis anywhere — this record claims no source-reported performance (see Evidence).
- Full Pine `//@version=2` block read in full (by Saucius Finance, `strategy("Aroon Oscillator strategy by Saucius", overlay=false)` — no `process_orders_on_close`, no `pyramiding`, no `calc_on_every_tick`, no `commission_*`, no `initial_capital`/`default_qty_*` lines). Source fills are therefore next-bar-open by Pine v2 default at language-default sizing; this record's same-bar-close execution and house sizing are separately identified researcher adaptations, never presented as source-native (see Execution assumptions).
- Pinned source inputs: `length = input(19)`, `level_middle = input(-25)`, `levelhigh = input(75)`, `levellow = input(-85)`. This record pins all four defaults; retuning any of them would be a different, unpinned rule.
- Text census over the pinned block: 2 `strategy.entry` / 4 `strategy.close` / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `volume` / 0 `open` / 0 `close` price reference (only `high`/`low` feed the indicator). Live order calls are exactly six: `strategy.entry("Long", true, when = entryl)`, `strategy.entry("Short", false, when = crossunder(oscillator, level_middle))`, `strategy.close("Long", when=entrys)`, `strategy.close("Short", when=entryl)`, `strategy.close("Long", when= exitL1)`, `strategy.close("Short", when= exitS1)`; display calls (`plot` x3, `hline` x3) touch no order condition.
- Prose-vs-code exit fact, admitted honestly: the page prose describes exits loosely as "closing long when the oscillator goes above the upper rail and closing short when it goes below the lower rail", but the pinned code closes long on a cross-DOWN-through-75 (`exitL1`, i.e. after the oscillator topped above 75 and turned down) and closes short on a cross-UP-through-(-85) (`exitS1`, i.e. after it bottomed below -85 and turned up). Pinned semantics follow the code, never the loose prose. Likewise the prose's "fast profit taking" promise has no coded target leg — 0 `strategy.exit` — and this record invents none.
- Prose performance language is qualitative only ("good win rate and profitability", "works better than simple trend strategies") with no table, figure, or number — named here as unusable water; no performance claim of any kind enters this record.

Licence and rights: the canonical page is a public FMZ strategy publication by ChaoZhang; the Pine block carries a Saucius Finance byline. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly three: (1) research market/timeframe BTCUSDT `1d` (the script reads only `high`/`low` and is symbol-agnostic; the page header ran 1h BTC_USDT Binance futures while its prose targets stocks/indexes/commodities); (2) same-bar-close fills via `process_orders_on_close=true` (the source fills next-bar-open); (3) an explicit atomic-bar evaluation order — exits before entries, entries reverse opposite positions — which reproduces the source's net position transitions exactly in every reachable state (proven in Negative evidence), specified here because the source leaves same-bar order interaction to broker-emulator ordering. All three adaptations are predeclared here, confined to Provenance, Signal, Execution assumptions, and Limitations, with every original claim kept separate above. Indicator formulas, lookbacks, thresholds, cross semantics, pyramiding default, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-09): working-tree searches for `438795`, `saucius`, and word-boundary `aroon` return zero strategy records using this source, author strategy, or mechanism — the only `aroon` hit is passing dedup prose inside `donchian-20-10-breakout-btcusdt-1h-2026-10-06.md`, which notes a same-family v4 TV-mirror batch killed in a prior cycle: different canonical source identity (that batch was v4 files from another mirror, never merged, present in neither `main` nor any open PR) and different program semantics from this record's pinned v2 four-condition exit machine with asymmetric rails (-25/75/-85). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #58 (17-family reconstruction batch, unmerged, no Aroon file), and #63 (SuperTrend ATR-flip trend long) — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `stochastic-ott-dual-trend-btcusdt-1d-2026-10-06.md` is a price-rank %K/%D stochastic system, not a time-since-extreme oscillator; `williams-r-level-cross-mean-reversion-long` is a bounded momentum level-cross mean-reversion; `dmi-swings-contrarian-adx-btcusdt-1d` is a DMI/ADX directional system. Five-axis distinction: mechanism differs (time-since-high/low persistence oscillator with midline-cross entries AND rail-turn exits, two-sided with reversal), signal construction differs (no pool record evaluates `100*(highestbars(high,20)+19)/19 - 100*(lowestbars(low,20)+19)/19` against asymmetric -25/75/-85 rails), exits differ (opposite-midline-cross OR rail-turn dual close versus band, time, or trailing exits), source identity differs (FMZ 438795 ChaoZhang Jan-2024 versus TV authors or other FMZ IDs), and direction handling differs (symmetric two-sided with reversal versus long-only or gated records).

## Economic mechanism

### Source-reported

Time-since-extreme trend persistence, after Tushar Chande: instead of smoothing prices, the oscillator asks how recently the market printed a fresh high versus a fresh low inside 19 bars. A cross up through the -25 midline means buying pressure has refreshed the high side fast enough to dominate; a cross down means the low side dominates. The asymmetric rails (+75/-85) act as exhaustion turns: a long is closed only after the oscillator first proves extreme persistence above 75 and then turns back down, and a short only after it proves persistence below -85 and turns back up — so positions survive mid-range chop and exit on measured trend fatigue. The author ships no fixed stop, no target, no trailing order: exits are signal-only by construction. Risk guidance is prose-only ("add stop loss strategies", "incorporate volume") and specifies no executable rule.

### Research interpretation

Two-sided persistence harvesting. Unlike Donchian records, the entry level is not a price extreme but a recency score — identical price paths produce different signals depending on where inside the 20-bar window the extremes sit; unlike stochastic records, nothing is normalized by price range, so the oscillator is a pure timing statistic immune to gap-size distortion. The exit pair (opposite-midline-cross OR rail-turn, per side) bounds adverse excursion without any price-level stop: a failed persistence read that falls back across the midline, or an exhausted trend that turns from beyond the rail, is closed on the next eligible bar. No leverage, sizing, or cost edge is embedded in the signal; language-default sizing is replaced by the house overlay (see Execution assumptions).

## Signal

Exact rule as pinned (defaults quoted — inputs unmodified):

- Declaration (derived): `strategy("Aroon Oscillator strategy by Saucius", overlay=false, process_orders_on_close=true)` — the first line is the source verbatim except `process_orders_on_close=true`, which is the predeclared researcher adaptation (source declaration carries no such argument), and except sizing/capital, whose language-default lines are absent in the source and replaced by the house overlay (see Execution assumptions). `pyramiding` is unset (v2 language default 0: no additional same-direction entry while positioned, opposite-direction entry reverses — load-bearing here, pinned explicitly, see Execution assumptions). `calc_on_every_tick` is unset (default false: exactly one evaluation per completed bar) and `calc_on_order_fills` is unset (default false).
- Oscillator (lengths pinned): `upper = 100 * (highestbars(high, length+1) + length)/length` with `length = 19`, i.e. the classic Aroon-Up over a 20-bar window (100 when the window high is the current bar, 0 when it is 19 bars back, in `100/19` steps); `lower` is the mirror on `lowestbars(low, length+1)`; `oscillator = upper - lower` in `[-100, 100]`. Thresholds pinned: `level_middle = -25`, `levelhigh = 75`, `levellow = -85`. The `overlay=false` pane and the lattice-step detail change nothing about order semantics.
- Entry long: `entryl = oscillator[1] < level_middle[1] and oscillator > level_middle` — strict cross up through -25. Live via `strategy.entry("Long", true, when = entryl)`, evaluated on the completed-bar close with same-bar-close execution under the derived declaration.
- Entry short: `strategy.entry("Short", false, when = crossunder(oscillator, level_middle))` — strict cross down through -25. The script also defines an `entrys` variable with identical cross-down semantics, but the executed short-entry call is the `crossunder` form quoted here; both forms are net-identical on a constant threshold and this record pins the executed one.
- Exit long: `strategy.close("Long", when=entrys)` OR `strategy.close("Long", when= exitL1)` with `exitL1 = oscillator[1] > levelhigh[1] and oscillator < levelhigh` — opposite-midline-cross or cross-down-through-75 rail turn, same completed-bar close.
- Exit short: `strategy.close("Short", when=entryl)` OR `strategy.close("Short", when= exitS1)` with `exitS1 = oscillator[1] < levellow[1] and oscillator > levellow` — opposite-midline-cross or cross-up-through-(-85) rail turn.
- Direction: symmetric two-sided by pinned code path; flat is entered only via the exit legs (no standalone flat signal). A short-side instrument is required for the short legs; on a spot-only venue they are inexpressible and the record would not be the same rule (see Crypto portability).
- Evaluation order (predeclared specification, net-transition-identical to the source — proof in Negative evidence): on each completed bar, evaluate both exit legs first, then both entry legs; an entry against an open opposite position reverses it (Pine pyramiding-0 parity). At most one entry and one exit leg can co-fire on any bar (proven), so the order specification only resolves the two reachable cross-side co-firings, where it reproduces the source net exactly.
- Display isolation: `plot` x3 / `hline` x3 calls render the two Aroon lines, the oscillator, and the three rails only — no display call feeds any order condition.

## Required data

- Completed `1d` bars of BTCUSDT: `high` (Aroon-Up path via `highestbars`) and `low` (Aroon-Down path via `lowestbars`). No `open`, no `close` price reference, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d`. The script takes no timeframe input and makes no live `request.*`/`security(`/`timeframe(` call, so it is single-frame by construction; `1d` is adopted as the research frame because it is a campaign timeframe — never presented as anything beyond that (see Limitations).
- Warmup: `highestbars`/`lowestbars` over `length+1 = 20` bars are only full from the 20th completed `1d` bar, and each cross event additionally reads one prior oscillator value, so the first signal-eligible bar is the 21st completed `1d` bar. Pre-warmup bars are flat by language semantics (`na` conditions never open or close anything). No repainting, no negative shift, no future reference, no full-sample normalization; `calc_on_every_tick=false` gives exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT under the house overlay (the rule reads high/low recency only; venue transfer from the page's 1h Binance-futures header — and from prose targeting stocks/indexes/commodities — is never presented as source-native semantics).
- Order timing (predeclared derivation): `process_orders_on_close = true` with `calc_on_every_tick` unset (default false): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. The source's own timing is next-bar-open (declaration carries no such argument — quoted verbatim in Provenance); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill. 0 `strategy.exit` calls, hence no stop/limit order and no same-bar TP/SL ordering ambiguity anywhere in the rule; the only ordering specification is the predeclared exits-before-entries atomic evaluation, proven net-identical to the source (see Negative evidence).
- Sizing/capital: the source declaration codes no sizing, capital, or commission line (language defaults apply in its own backtest), replaced here by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions, never presented as source-native behavior.
- Concurrency: `pyramiding` is unset (v2 default 0: no same-direction add while positioned; opposite-direction entry reverses). The default is load-bearing and therefore pinned explicitly: repeat entry-condition bars during an open same-side position are rejected no-ops, and re-entry is allowed immediately on the next qualifying cross after any exit (no cooldown specified — explicitly none, not invented). `strategy.close` legs with no matching open position are deterministic no-ops. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The canonical page ships the Aroon-Up/Down/oscillator construction (19-period, Up-minus-Down), the asymmetric -25/75/-85 thresholds, the two midline-cross entry rules, the opposite-cross/rail-turn exit pair, the 1h BTC_USDT Binance-futures backtest header with its 2023-12-15–2024-01-10 window, and prose risk guidance. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=` — the opposite-cross/rail-turn close set is the sole exit path by construction, and the prose's stop/volume suggestions are explicitly un-coded optimization wishes, never rules.
2. Entries are mutually exclusive on every bar: `entryl` needs `oscillator[1] < -25 < oscillator` while the short entry needs `oscillator[1] > -25 > oscillator` — no single prior/current pair satisfies both, so no same-bar long/short entry conflict exists to resolve.
3. At most one exit leg co-fires with an entry, and only in two reachable pairs: `entryl` (cross up through -25) can co-fire only `exitS1` (cross up through -85, requiring a sub-(-85)-to-above-(-25) single-bar jump); it can never co-fire `exitL1` (which needs `oscillator[1] > 75`, contradicting `oscillator[1] < -25`) or `entrys`. The short-side mirror holds: `entrys`-form entry co-fires only `exitL1`, never `exitS1` or `entryl`. Two exit legs can never co-fire each other (`exitL1` needs `oscillator[1] > 75`, `exitS1` needs `oscillator[1] < -85`).
4. Both reachable co-firings reproduce the source net exactly: `entryl` + `exitS1` always co-fires `strategy.close("Short", when=entryl)` too, so under source next-open semantics a held short is closed-then-reversed to long, a flat account opens long, and a held long keeps its long (entry rejected under pyramiding 0, closes are no-ops) — net long in all three states; under this record's exits-first atomic order the short-close lands first (flattening or no-op) and the entry then opens (or keeps) the long — net long in all three states. The `entrys`-form + `exitL1` mirror yields net short in all three states. All six reachable combinations were walked with identical nets; the order specification invents no transition.
5. Boundary ties and flat ranges fire nothing: strict cross semantics (equality on either compared bar is not a cross); an oscillator pinned exactly on a rail across consecutive bars holds; `na` warmup bars open and close nothing.
6. Flat-state determinism: all four `strategy.close` legs with no matching open position are no-ops; same-side repeat entries while positioned are rejected under pinned pyramiding 0; opposite-side entries reverse; the seed bars satisfy no order condition by themselves (each cross needs a settled prior bar, the window needs 20 bars).
7. The length, the three asymmetric thresholds, the highestbars/lowestbars construction, the two-sided direction, reversal semantics, and no-stop/no-target/no-cooldown posture are pinned, not removed: retuning 19/-25/75/-85, symmetrizing the rails, adding a stop/target/cooldown/volume filter, or disabling a side would each be a different, unpinned rule — none is admitted here.
8. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT-`1d` research frame, same-bar-close fills, the exits-first atomic evaluation order, and house sizing — all predeclared above; every signal, threshold, default, and risk posture is source-verbatim. This record is therefore never evidence that the original next-bar-open 1h source itself passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: Aroon(19) Up-minus-Down / strict -25 midline-cross entries / opposite-cross-or-rail-turn exits / two-sided with reversal / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Midline relevance: moving entries to Chande's symmetric ±50 lines (same rail-turn exit structure) must not improve net expectancy; fail ⇒ the asymmetric -25 midline adds nothing over the textbook symmetric read.
- F2 — Rail-exit relevance: dropping the 75/-85 rail-turn legs (opposite-midline-cross exits only) must not improve net expectancy; fail ⇒ the exhaustion-turn exits add nothing over plain reversal trading.
- F3 — Construction relevance: replacing the time-since-extreme oscillator with a same-threshold price-rank stochastic (same cross/rail event structure) must not reproduce-or-beat net expectancy; fail ⇒ the record is a threshold-label variant of a plain stochastic cross.

## Crypto portability

Pinned to BTCUSDT under the house overlay. The high/low-recency-only logic ports across perpetual venues without structural change; the short legs require a shortable instrument, so a spot-only deployment cannot express this rule (disabling the short side would be a different, unpinned rule). No funding-dependent leg, no stablecoin-specific assumption, no session, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (`open`/`close` prices are never referenced), so session-gap behavior is simply absent rather than approximated. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing and frame: the source fills next-bar-open on 1h bars; this record executes same-bar-close on `1d` bars. Backtest economics of the two timings and frames differ by construction — the adaptations are disclosed, not hidden, and this record makes no claim about the source timing's performance.
- No price stop: adverse excursion after entry has no guardrail beyond the opposite cross or the rail turn; a vertical-against move exits only when persistence flips or exhausts, which can be far.
- Single-bar jump exits: the rail-turn legs can trigger on one-bar extreme dislocations (window extremes dropping out) rather than genuine fatigue turns — the source provides no confirmation filter and this record invents none.
- Warmup cost: the 20-bar window plus one prior bar for the cross means the system is blind for the first 20 bars of any 1d evaluation window.
- Performance evidence is absent: the canonical page reports no numbers at all (its Dec-2023–Jan-2024 1h header is a run window, not a result, and its praise is qualitative prose); nothing here is calibrated, fitted, or tuned to any backtest.
- Original-venue gap: the page prose targets stocks/indexes/commodities while its header ran crypto futures; this record pins BTCUSDT `1d` as a declared derivation — any resemblance of future results to either original venue would be coincidence, not validation.

## Implementation status

Not implemented. No Hummingbot controller/executor, no Qlib screening, no Paper/Testnet/Live run has been performed from this record. Admission claims pinned-engine expressibility only (see Execution assumptions), subject to independent six-gate review.

## Adoption boundary

Research-only. Not approved for any downstream screening, parity run, or trading authorization. Only a `PASS` under the live six-gate contract may merge this record into `main`; any `NOT_LOSSLESS` finding closes the PR lane without promotion.

## Related Wiki records

None.

## Sources

- Canonical strategy page (fetched 2026-10-09): https://www.fmz.com/strategy/438795
- Pine v2 strategy semantics (declaration defaults, order calls, close-evaluated execution): https://www.tradingview.com/pine-script-reference/v2/
- Pine strategy concepts: https://www.tradingview.com/pine-script-docs/concepts/strategies/
