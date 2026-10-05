---
schema: strategy-research-record-v1
title: Perry Kaufman pivot point breakout system on BTCUSDT 1d bars
created: 2026-10-05
updated: 2026-10-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-09-18
sources:
  - https://github.com/hasnocool/tradingview-pine-scripts
  - https://tradingview.com/script/TW0P138b
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}entry
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}close
  - https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}pivothigh
  - https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}pivotlow
  - https://www.tradingview.com/pine-script-docs/v5/concepts/strategies/
  - https://www.tradingview.com/pine-script-docs/v5/language/user-defined-functions/
  - https://www.tradingview.com/pine-script-docs/v5/language/variable-declarations/
  - https://www.tradingview.com/pine-script-docs/migration-guides/to-pine-version-6/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The script description states the rule works 'by buying when the current high is higher than the last pivot high, and selling when the low is lower than the last pivot low', which describes a two-sided breakout system, but the pinned code's default input `orderDirection = LONG` disables the entire short leg: at defaults `strategy.entry('Short', ...)` carries `when = (LONG != LONG) = false` and `strategy.close('Short', ...)` carries `when = (LONG == SHORT) = false`, so no short order can ever be placed and no short close can ever fire. The two-sided behaviour exists only when a chart user changes the input away from its default; the pinned, default-parameter rule is long-only."
  - "The script description states the system 'relies on the good reward to risk ratio', which implies a designed risk/reward structure, but the pinned code contains no stop loss, no take profit, no trailing stop and no time exit of any kind (0 `strategy.exit`, 0 `strategy.stop`, 0 `strategy.order`, 0 `limit`/`stop` arguments); any realized reward-to-risk ratio is emergent from the signal exit, not a rule."
---

# Perry Kaufman pivot point breakout system on BTCUSDT 1d bars

## Provenance

Immutable GitHub source (this is the primary source actually read end to end):

- Repository URL: https://github.com/hasnocool/tradingview-pine-scripts
- Full commit SHA: `69969aeaf271b2f7b5a7632a1bde43069a0cbe26` (commit date 2024-09-18T10:39:33Z). The GitHub `commits/HEAD` API returned this same SHA on 2026-10-05, so it is still the repository head at research time.
- Exact file path: `Pivot Point Breakout.pine` (space in filename preserved verbatim).
- Relevant stable public URL of the mirrored script: https://tradingview.com/script/TW0P138b (`Pivot Point Breakout — Strategy by EduardoMattje`), found by web search on 2026-10-05; its published description is verbatim identical to the mirror file's `Description:` header, which corroborates the mirror rather than replacing it as the immutable artifact.

Primary-source checksums pinned 2026-10-05:

- File 3270 bytes, SHA-256 `8ae846380e83b7f07fa8be845976e03c96051fe1a09df02a5ff9d6a3e30e0910`.
- Independent remote check: the git tree of the pinned commit lists that path as blob `896a42e82880a722180c8c0665c1e3ef72913b6e` with size 3270, and the blob fetched back from the GitHub API by that id is byte-identical to the local artifact (identical SHA-256), so the pinned bytes are the bytes GitHub serves.

Artifact structure as printed: a `Script Name:` line (`Pivot Point Breakout`), an `Author:` line (`EduardoMattje`), a `Description:` paragraph (Perry Kaufman attribution, breakout premise, low-win-rate/high-payoff claim), a `PineScript code:` section with a line-numbered dump, and an `Expand (75 lines)` trailer. The executable Pine block is file lines 88-140 (53 lines: the MPL-2.0 notice, `// (c) EduardoMattje`, `//@version=5`, one `strategy()` declaration, constant/input declarations, two `ta.pivot*` calls, one 8-line user function, two level assignments, the `validTrade` expression, two `if` order blocks, four `plot*` calls). Everything gate-relevant below is read from those 53 lines.

Licence and rights: the pinned Pine block itself prints `// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/` and the author credit `// (c) EduardoMattje`. This record cites and normalizes the rule and reproduces no source code block.

Pre-write dedup (2026-10-05): a search of the current working tree (excluding `.git`) for `pivot`, `kaufman`, `PPB`, `TW0P138b`, `pivothigh`, `pivotlow` and `EduardoMattje` returned 0 matches except the author name inside the already-merged Bookstaber record (a different script by the same author, a different mechanism — see five-axis distinction below); `gh pr list --state open` returned an empty list, so there is no open `research/*` PR to deduplicate against. The same probes in the Wiki Brain returned 0 matches. The dedup set is therefore the four records on `main` (Gann HiLo, VIDYA CMO-adaptive, P-Signal erf, Bookstaber ATR) plus the four closed research PRs (#6 LazyBear Wave Trend, #10 golden/dead cross, #17 MACD histogram, #20 Ichimoku-RSI). Five-axis distinction: mechanism differs (confirmed-pivot-extreme breakout levels versus ATR-standardized 1-bar change sign test / displaced average-band state flip / CMO-adaptive average slope / erf dead-band / oscillator cross / dual-EMA cross / MACD zero-cross / Ichimoku cloud), signal construction differs (last-confirmed-pivot storage with strict `high > level` / `low < level` comparisons, no crossover of two series anywhere), horizon is `1d` (coincides only with Gann HiLo and Bookstaber, whose mechanisms differ), source identity differs in all cases (hasnocool `Pivot Point Breakout.pine` versus FMZ 430857 / 427070 / 430552 / 440338 and the four closed sources), and direction handling differs (long-only at pinned defaults versus two-sided). The two-sided behaviour the prose advertises is explicitly not what is pinned here.

## Economic mechanism

### Source-reported

- Attribution, as printed: "This is a strategy taken from Perry Kaufman's book, Trading Systems and Methods."
- Premise, as printed: "it's a breakout strategy. It works by buying when the current high is higher than the last pivot high, and selling when the low is lower than the last pivot low."
- Expectation, as printed: "It does not have a good success probability, and relies on the good reward to risk ratio.... Definitely not recommended for someone with weak hands." (Third-party mirror pages append further adjectives; they are not source and are ignored.)
- No sample, no metric, no baseline, no figure and no performance number of any kind is printed anywhere in the artifact (census under Evidence).

### Research interpretation

Falsifiable mechanism hypothesis: on a single 24/7 crypto instrument, a bar whose high exceeds the most recently *confirmed* swing high (a pivot with 3 bars of confirmation on each side) marks absorption of resting supply at a level the market has already recognized twice (formation plus confirmation), and such absorptions exhibit short-horizon directional persistence because breakout-driven order flow (stops, momentum ignition) unwinds only partially within one daily bar; the mirror-image breakdown closes the long because a confirmed lower low marks the failure of the same auction. The bet is continuation after confirmed-extreme absorption, not mean reversion and not a moving-average state. The 3-bar confirmation lag is a noise filter bought with 3 bars of delay; the exit is not a level but the mirror-image event (a fresh confirmed breakdown). This is a ported technical-analysis hypothesis: the source supplies the Kaufman attribution but no behavioural argument, no sample and no evidence, so the mechanism is research interpretation, not source-reported fact.

Component roles, stated plainly because the source offers no composite structure:

- Primary signal: strict inequalities of the current bar's extremes against stored confirmed-pivot levels (`high[t] > lastHigh[t]` to enter, `low[t] < lastLow[t]` to exit).
- Confirmation filter: `ta.pivothigh(3, 3)` / `ta.pivotlow(3, 3)` — a pivot is admitted only with 3 bars on each side, so levels update at most on a 3-bar lag and never repaint (a confirmed pivot value never changes after confirmation).
- Trend / regime filter: none.
- Direction gate: the `orderDirection` input, pinned at its default `LONG`, which is what makes the pinned rule long-only and spot-applicable.

## Signal

Everything below is read from the pinned Pine block. Nothing in this section is `research-proposed`. All statements hold at the pinned source defaults (`orderDirection = LONG`, `leftHigh = rightHigh = leftLow = rightLow = 3`, `startDate = 0`, `endDate = 0`); any other input combination is a different, unpinned rule.

**Formation timestamp and tradability**

- Decision series: completed `1d` bars of the pinned instrument (research-pinned single decision timeframe; the script itself is timeframe-agnostic — 0 `request.*` calls, 0 `security(` calls, 0 `timeframe` references, 0 `input.timeframe` — so exactly one decision timeframe is declared by this record, `1d`, with no multi-timeframe dependency to align).
- Inputs at decision bar `t`: `high[t]`, `low[t]` (current extremes) and the stored levels `lastHigh[t]`, `lastLow[t]` (functions of confirmed past highs/lows only). `open` is never read by the trading logic, `close` is never read by the trading logic, and `volume` occurs 0 times in the whole artifact (the four `plot*` calls render levels and pivot markers only and feed no order).
- Order timing: the live order calls at defaults are `strategy.entry` and `strategy.close` market orders (no `limit`/`stop` arguments anywhere — 0 occurrences), and the declaration sets `process_orders_on_close=true`. Official first-party documentation states that when this parameter is true the broker emulator processes orders "on the closing tick of each bar", and the reference adds "If the orders are market orders, the broker emulator executes them before the next bar's open." This is exactly a completed-bar decision with same-bar-close execution; there is no next-bar-open fill anywhere in the rule.
- Recalculation: neither `calc_on_every_tick` nor `calc_on_order_fills` appears in the pinned declaration (0 occurrences of each). Official documentation states both default to `false` and that `calc_on_every_tick` "does not affect the strategy's executions on historical bars". Recorded as source-declared-by-language-default, not as a research-proposed choice; it also means no intrabar re-evaluation can create a second order on the same bar.
- Timezone and date gate: the artifact contains 2 `input.time` declarations (`startDate`, `endDate`, both default 0) combined as `validTrade = (startDate == 0 ? true : time >= startDate) and (endDate == 0 ? true : time <= endDate)`. At the pinned defaults both ternaries take their `true` branches identically on every bar (`0 == 0`), so `validTrade` is identically `true` and no calendar, session or timezone convention can affect any trade. The gate is inert-by-default, recorded exactly as written rather than deleted; `timestamp(` occurs 0 times and `timenow` occurs 0 times.

**Lookback, formulas and warmup**

- Parameters as declared: `var orderDirection = input.string(LONG, "Order direction", options=[BOTH, LONG, SHORT])` → defval `LONG`; four `var input.int(3, ..., minval=0, ...)` pivot lengths → defval 3 each; two `var input.time(0, ...)` dates → defval 0. The `var` keyword on inputs is the same pattern as the already-admitted Bookstaber record: official documentation states `var` initializes "only once, on the first bar if the declaration is in the global scope", and because an input is `const` this changes no value on any bar.
- Pivot extraction, exact: `lowPivot = ta.pivotlow(leftLow, rightLow)` and `highPivot = ta.pivothigh(leftHigh, rightHigh)`, i.e. `ta.pivotlow(3, 3)` / `ta.pivothigh(3, 3)` at defaults — a 7-bar window (3 left + pivot bar + 3 right) with a 3-bar confirmation lag. Both are first-party exact functions of the `high`/`low` series; the rule contains 0 `crossover`, 0 `crossunder`, 0 `ta.cross`, 0 `ta.ema` and 0 division operators in executable code (all 23 `/` characters in the file sit inside `//` comments or the MPL licence URL), so none of the seeding, tie-semantics or zero-divisor blockers that closed earlier PRs arise here.
- Level storage, exact:
```
f_updateLevels(pivot_) =>
    var float pastLevel = na
    if not na(pivot_)
        pastLevel := pivot_
    pastLevel
lastLow := f_updateLevels(lowPivot)
lastHigh := f_updateLevels(highPivot)
```
Official documentation pins the two facts that fix the semantics: a `var` in a local block "is only initialized once ... the first time the local block is executed" and "will preserve its last value on successive bars, until we reassign a new value to it"; and "Each instance of a function call in a script maintains its own, independent history." The two call sites are therefore independent level registers: `lastLow` stores only confirmed low pivots, `lastHigh` only confirmed high pivots, each seeded `na` and each holding its last confirmed value until the next confirmation of its own side. No repainting: a confirmed pivot value never changes after its confirmation bar.
- Derived conditions, exact, at defaults:
  - Long entry condition: `high[t] > lastHigh[t]`, gated by `when = (LONG != SHORT) and validTrade = true`.
  - Long exit condition: `low[t] < lastLow[t]`, via `strategy.close("Long", when = (LONG == LONG) = true)` — note the close carries no `validTrade` gate in the source; at defaults the gate is identically true anyway, so this asymmetry changes nothing at the pinned defaults and is recorded rather than normalized away.
  - Dead at defaults (recorded, never firing): `strategy.close("Short", when = (LONG == SHORT) = false)` and `strategy.entry("Short", ..., when = (LONG != LONG) and ... = false)`.
- Warmup, derived from the pinned code because the source declares none: a 3/3 pivot needs bars 0-6 before its first confirmation can exist, so bars at index 0-5 can never carry a signal (`lastHigh`/`lastLow` are still `na`, and a boolean `na` cannot open an order — official v5-to-v6 migration guide: in v5 a value that must be boolean is evaluated so that `na` "is evaluated as false"; both order calls sit in `if` blocks). Therefore **bar index 6 is the earliest bar on which any order can be created, and then only if a pivot has already confirmed**; an exit can occur only after an entry. `max_bars_back` is not declared; official documentation states the required history buffer is detected automatically, and the rule references no lag beyond the pivot window.
- Same-bar dual-signal accounting (the only bar on which two live calls fire together): `high[t] > lastHigh[t]` and `low[t] < lastLow[t]` can both hold on an outside bar beyond both levels. Script order on such a bar is entry-then-close (`strategy.entry("Long", ...)` is called before `strategy.close("Long", ...)`), and both are market orders filling at the same bar close under `process_orders_on_close=true`. Exhaustive post-bar state: from flat → long is opened and closed on the same tick (one zero-PnL round trip at the documented 0 percent commission and 0-tick slippage defaults); from long → the same-id entry is rejected under the default `pyramiding` rule while the close fires → flat. In both cases the bar ends flat, and the next bar re-enters on a fresh `high > lastHigh`. No third state exists, no priority choice is required, and the round-trip trade is an explicit consequence of call order, not an approximation.

**Entry**

- Long entry: `if high > lastHigh` → `strategy.entry("Long", strategy.long, when=orderDirection != SHORT and validTrade)`; at defaults `when=true`.
- Short entry: source-present but dead at defaults (`when=false` identically). Direction is therefore long-only at the pinned defaults: one live `strategy.entry`, `strategy.long` once, `strategy.short` zero live occurrences.
- The statement omits `qty`. Official reference: `qty` "The default is na, which means that the command uses the default_qty_type and default_qty_value parameters of the strategy declaration statement to determine the quantity" — here `strategy.percent_of_equity` with value `100`.
- The statement omits `limit` and `stop`; official reference: `limit`/`stop` "The default is na, which means the resulting order is not of the limit or stop-limit type", so it is a market order.

**Exit**

- The pinned code contains exactly four order calls: 2 `strategy.entry`, 2 `strategy.close`. Censuses over the whole 3270-byte artifact: `strategy.close_all` 0, `strategy.exit` 0, `strategy.order` 0, `strategy.stop` 0, `strategy.cancel` 0, `strategy.cancel_all` 0, `strategy.risk.*` 0, `limit =` 0, `stop =` 0. At defaults exactly one close is live: `strategy.close("Long", when=true)` on `low < lastLow`.
- Stop loss: none. Take profit: none. Trailing stop: none. Time limit or maximum holding period: none (the date inputs bound *entries* only when set, and are disabled at defaults). Flat state: reachable before the first entry and after every breakdown exit; the system is otherwise long. This directly contradicts the description's implied risk/reward design (contradiction 2).

**Holding period, overlap and re-entry**

- Holding period: unbounded and determined entirely by waiting for the next `low < lastLow` breakdown; the source states no maximum or expected holding period.
- Maximum same-side concurrency: 1. `pyramiding` is not written in the declaration, so the value comes from the language default, and both official statements of that default describe the same observable rule even though they print different numbers: the v5 reference states "The maximum number of entries allowed in the same direction. If the value is 0, only one entry order in the same direction can be opened, and additional entry orders are rejected … The default is 0", while the v5 Strategies page states "The default value is 1, meaning the strategy can open new positions but cannot add to them using orders from strategy.entry() calls." Under each document's own definition the result is identical — one open same-side entry, further same-side entries rejected — and with a single live entry id ("Long") there is no second id that could add on. The record therefore records `pyramiding` as source-declared-by-language-default with that convergence stated rather than silently picking one number, and F3 forces the executing engine to confirm it. This is the same convergence the PASS review of PR #12 accepted.
- Same-direction re-entry: after a breakdown exit the system is flat, so the next `high > lastHigh` bar opens a fresh long; while long, a further entry signal is rejected under the default above, and orders fill on the same bar they are created, so no unfilled order survives into the next bar.
- Cooldown: none declared, and Pine's v5 strategy declaration exposes no cooldown field. A fresh entry requires a fresh `high > lastHigh` event while flat, so cooldown semantics are provably irrelevant rather than missing.

**Parameters, sizing and pyramiding**

- Declared verbatim in the pinned declaration: `strategy("Pivot Point Breakout", "PPB", true, default_qty_type=strategy.percent_of_equity, default_qty_value=100, process_orders_on_close=true)`. The third positional argument is `overlay` (display only) per the official `strategy()` signature; the code-declared trading values are `default_qty_type=strategy.percent_of_equity`, `default_qty_value=100`, `process_orders_on_close=true`.
- Declaration parameters the code leaves unset, each recorded as source-declared-by-language-default with the official page that documents it: `currency=currency.NONE` ("in which case the chart's currency is used"), `slippage=0`, `commission_type=strategy.commission.percent` with `commission_value=0`, `initial_capital=1000000`, `margin_long`/`margin_short` at the v5 default 0 ("the strategy does not enforce any limits on position size"; the 100 default is a v6 change and this script is `//@version=5`), `pyramiding` (convergence above), `calc_on_order_fills=false`, `calc_on_every_tick=false`, `close_entries_rule="FIFO"` (moot: a single live entry id with full closes), `max_bars_back` auto-detected, `backtest_fill_limits_assumption=0` (no price-dependent orders exist) and `use_bar_magnifier=false`.
- Sizing: `strategy.percent_of_equity` with value 100, i.e. each entry is 100 percent of available equity — declared in the code, therefore explicit and compounding.
- Direction: long-only at pinned defaults (see Entry). Spot is therefore the deterministic market type and no margined instrument is required (see Required data).
- Nothing else is declared: `currency`, `slippage`, `commission_*`, `initial_capital`, `margin_*`, `pyramiding`, `close_entries_rule`, `calc_*`, `max_bars_back` and `use_bar_magnifier` all occur 0 times in the artifact.

**Reconstruction status**

Every field required to replay the rule — indicator variant and its parameters, source prices, lookback, smoothing (none — no averaging of any kind is used), thresholds (the stored pivot levels themselves), comparison logic, direction, entry, exit, risk semantics, sizing, pyramiding, concurrency, cooldown, timeframe, fill timing and warmup — is explicit either in the pinned source or in official first-party documentation of the pinned source's own language defaults and functions. The residual `underspecified` items are the exact quote currency of the account under `currency.NONE` and the cost/latency/fill-failure model; neither alters the signal, and both are recorded as `data gap` rather than filled. There is no perpetual-versus-dated question here because the pinned rule is long-only spot.

## Required data

- Instrument: BTCUSDT on spot, research-pinned as the single-pair run of a venue-agnostic rule. The source script declares no venue, no exchange and no symbol (it runs on whatever chart it is attached to); because the pinned default rule never shorts, uses no margin and uses no leverage, spot is deterministically applicable and no futures, perpetual-or-dated, distinction can arise. Single pair, single instrument, no basket, no ranking, no cross-sectional step.
- Market type: spot. Long-only at pinned defaults; naked shorting is never required because the short leg is dead code at defaults.
- Spot applicability: fully applicable — the complete pinned rule (long entries, breakdown closes, 100 percent equity sizing) executes on spot.
- Venue: any venue listing BTCUSDT spot; no venue-selection rule, no listing or survivorship rule (the artifact states none).
- Timeframe: exactly one decision timeframe, `1d`, research-pinned for this record. The pinned script contains 0 `request.*` calls and 0 `security(` calls, so no lower- or higher-timeframe series is referenced by the rule and there is no multi-timeframe dependency to align. `use_bar_magnifier` is at its documented `false` default, so no lower-timeframe data is used for fills either.
- Fields used: `high[t]` and `low[t]` only (current-bar extremes against the stored levels). `open`, `close` and `volume` are never read by the trading logic (the four `plot*` calls render stored levels and pivot markers only).
- Fields not required and not used, each absent from the pinned artifact: open interest, funding, mark or index price, basis, order book or depth, trade or aggressor feed, liquidation feed, on-chain data, options or Greeks, sentiment or news, macro series, cross-venue state, borrow data, margin state. The calendar is gated only by the inert-by-default `validTrade` expression (see Signal).
- Point-in-time: every input at bar `t` is contemporaneous (`high[t]`, `low[t]`) or confirmed-past (stored pivots confirmed at least 3 bars earlier); there is no future reference, no negative shift in any order input, no future extrema, no full-sample normalization, no `timenow` (0 occurrences), and no `security` call of any kind, so the pinned rule contains no look-ahead leakage. The `plot()` calls use `offset=1` and the `plotshape()` calls use `offset=-rightLow`/`-rightHigh`: display-only displacements of drawings that feed no order and change no signal.
- Timestamp and timezone: bar open times of a 1-day BTCUSDT spot series; because the date gate is identically true at defaults and no rule element compares timestamps, the record does not depend on any boundary convention.
- Missing data: no gap, halt or stale-bar handling is specified anywhere in the source → `data gap`. Imputation would be `research-proposed` and is not proposed here. The `na` rules that do matter are the language ones: `ta.pivothigh`/`ta.pivotlow` are `na` until the first confirmation window completes, the level registers are seeded `na`, and a boolean `na` evaluates to `false` in v5 — these are what fix the warmup at bar index 6.
- Funding, fee and spread needs: none specified and none applicable to a spot rule. Word-boundary census of the pinned 3270-byte artifact gives commission 0, slippage 0, fee 0, funding 0, leverage 0, spread 0, capacity 0, turnover 0, roi 0, margin 0, short 4 (two live-at-BOTH code paths plus two input-option strings, all dead at defaults except the long close), equity 1 (the `percent_of_equity` token). Commission 0 and slippage 0 come from language defaults, not from measurement; spread, impact and latency are `data gap`, never a modeled zero.

## Execution assumptions

Source-declared (quoted or read from the pinned declaration, the pinned code, or official first-party documentation of that same language):

- Order type: market orders, created only by the one live `strategy.entry` and the one live `strategy.close` at defaults. There is no limit order, no stop order, no stop-limit, no OCA group and no conditional price order anywhere in the rule (0 `strategy.exit`, 0 `strategy.order`, 0 `limit`/`stop` arguments), so there is no intrabar-path dependence and no maker/taker asymmetry to model. The broker emulator's documented intrabar assumptions are never exercised, because they apply only to price-dependent orders.
- Fill model: `process_orders_on_close=true` → official documentation: orders are processed "on the closing tick of each bar", and for market orders "the broker emulator executes them before the next bar's open". `calc_on_every_tick` and `calc_on_order_fills` default to `false`, so there is exactly one evaluation per completed bar. Completed-bar decision with same-bar-close execution.
- Signal-to-order delay: none. The order is created and filled on the same completed-bar close; the engine's "Order execution delay" override defaults to 0 ticks.
- Dual-signal bar: script-ordered entry-then-close at the same close price (state table under Signal); the position ends flat in all cases.
- Position limits: one position at a time, 100 percent of available equity per position, no same-side add-on (default `pyramiding`, convergence recorded above), no scaling, no grid, no martingale, no hedge, no shorting at defaults.
- Leverage and margin: unset in code → v5 defaults (`margin_long`/`margin_short` 0 → no position-size limit and no margin call); sizing is equity-percentage, so the rule never sizes by leverage and has no leverage-dependent edge. Spot cash only.
- Costs: commission type defaults to `strategy.commission.percent` with `commission_value` default 0, i.e. 0 percent of order cash volume charged on the entry fill and again on the exit fill; `slippage` defaults to 0 ticks per the official reference. No spread, no market-impact model appears anywhere in the artifact → the remaining cost legs are `data gap`; this record does not adopt a validated zero-cost assumption beyond the documented defaults.
- Latency: not modeled in source → `data gap`.
- Participation and capacity: not modeled in source → `data gap`; tested by the research-defined gate F8.
- Failure handling (partial fills, rejects, downtime): not addressed in source → `data gap`. The pinned rule places whole market orders only, and no partial-fill-dependent condition exists.
- Engine-settings overrides a chart user could apply (timeframe, symbol, initial capital, currency, pyramiding, commission, orderDirection, pivot lengths, dates, order size, order execution delay) are not part of the pinned source; the code-declared values plus documented defaults above are the recorded strategy.
- Scout-vs-source split: the venue-agnostic script is evaluated here as one explicit single-pair run (BTCUSDT spot, `1d`); every other item above marked source-declared comes from the pinned declaration, the pinned code, or official TradingView documentation of that language. Nothing in this section is a Scout-added execution rule; every pass/fail cutoff used later is labeled `research-defined`.

## Evidence

### Source-reported

The artifact prints no performance result of any kind. Word-boundary census over the pinned 3270-byte artifact: sharpe 0, drawdown 0, cagr 0, return 0, win rate 0, annualized 0, roi 0, net profit 0, max drawdown 0, profit factor 0, strategy tester 0, open interest 0, commission 0, slippage 0, fee 0, funding 0, leverage 0, spread 0, capacity 0, turnover 0, cooldown 0, pyramiding 0, take profit 0, trailing 0, backtest 0; `time` occurs twice, both inside the `input.time` date declarations; `timeframe` occurs 0 times. There is no equity curve, no trade list, no table and no figure anywhere in the artifact, and a TradingView script page shows none either.

What the source does report:

- Configuration only, from the pinned code: `//@version=5`, `orderDirection` default LONG with BOTH/LONG/SHORT options, pivot lengths 3/3/3/3, dates disabled at defaults, `percent_of_equity` 100, `process_orders_on_close=true`.
- Qualitative claims, verbatim, with no sample, no metric, no baseline and no figure: the Kaufman-book attribution, the breakout premise, "does not have a good success probability", "relies on the good reward to risk ratio", "not recommended for someone with weak hands" — unverifiable as printed and recorded as bare claims, not as evidence.
- Research-computed, not printed: at the pinned defaults the rule is a strict-inequality test of current extremes against 3-bar-confirmed pivot levels, so its trigger rate is set by realized volatility and swing spacing, not by any fixed price distance.

No source-reported figure in this record comes from any other paper, article or repository; every claim is attributed to the single pinned artifact above. Third-party pages that re-host this script's statistics are not cited and contribute no number to this record.

### Independently reproduced

not independently reproduced

Only the following were performed: SHA-256 checksumming of the pinned artifact; a byte-identical re-fetch of the file blob by its id from the GitHub tree and blob APIs; a whole-artifact term and word-boundary census; enumeration of `strategy.*`, `input*`, `ta.*`, `plot*` call sites and of identifier occurrence counts; a same-bar dual-signal state-table walk; reading of the public TradingView script page header (title/author/description match only); and live reading over HTTPS of the official TradingView documentation pages cited under Sources. No market data was downloaded, no backtest was run, no Pine or third-party code was executed, and no statistic was recomputed from data.

### Negative evidence

1. The artifact prints zero performance numbers, so there is nothing to reproduce: sharpe, drawdown, cagr, return, win rate, annualized, roi and trade counts are all 0 occurrences.
2. The performance-sounding prose claims (low success probability, good reward-to-risk reliance) carry no sample, no metric and no baseline, so they cannot be checked as printed.
3. The source's own description advertises two-sided trading while the pinned defaults trade long-only (recorded contradiction 1) — a reader following the prose would expect short trades the pinned rule never takes.
4. The source implies a designed reward-to-risk structure while the code contains no stop, no target and no time exit (recorded contradiction 2).
5. Cost model is zero: commission 0 percent and slippage 0 ticks come from language defaults, with no spread or impact model — so any edge claim is unpriced by the source.
6. Sizing is 100 percent of available equity on every position: full-equity concentration, no cash buffer, no volatility targeting, no risk layer of any kind.
7. Holding is unbounded: with no time exit and no level exit beyond the mirror breakdown, exposure persists indefinitely until the next confirmed breakdown.
8. Every breakdown exit that fires while the breakout condition still holds (and every dual-signal bar) creates a same-tick round trip whose only trace is trade count; at zero modeled cost this is PnL-neutral but trade-list-visible, so cost-blind trade counts overstate activity.
9. The description's "selling" leg exists only as a user-selectable option (BOTH/SHORT), not as pinned behaviour; promoting it would be a rule change.
10. The `plotshape` negative offsets (`-rightLow`, `-rightHigh`) displace drawings into the past; they are display-only, but any re-implementation must not mistake them for signal lags.
11. No train/test split, no out-of-sample section and no walk-forward exists anywhere in the source.

## Falsification plan

All thresholds below are research-defined tests, never substitutes for the execution rules above (which are frozen: LONG default, 3/3/3/3 pivots, dates disabled, percent_of_equity 100 compounding, same-bar-close fills, 0 percent commission, 0-tick slippage, single `1d` timeframe, BTCUSDT spot).

- **F1 — Signal presence.** Threshold: at least 30 long entries and at least 10 breakdown exits on 5 years of `1d` BTCUSDT spot bars; fail ⇒ the rule never trades this instrument/timeframe, record stays research-only.
- **F2 — Dual-signal accounting.** Threshold: enumerate every bar with `high > lastHigh` and `low < lastLow` jointly true and confirm post-bar state is flat in all cases with the round trip recorded; fail ⇒ the call-order determinism claimed above does not replay, pin the discrepancy and keep research-only.
- **F3 — Engine-default audit gate.** Threshold: the executing engine must confirm every recorded declaration and language default end to end — 100 percent equity sizing, same-bar-close fills, 0 percent commission, 0-tick slippage, once-per-bar evaluation, same-side entries rejected while long, per-call-site level registers, `na`-is-false warmup, earliest possible order bar index 6; fail ⇒ pin the discrepancy in writing and keep research-only, no adoption.
- **F4 — Cost ladder.** Threshold: apply 0 / 1 / 2 / 5 / 10 bps per side; fail if net annualized return turns non-positive at 2 bps per side or net Sharpe falls to 0 or below at 5 bps per side ⇒ cost-dependent edge, no adoption.
- **F5 — Parameter perturbation.** Threshold: sweep pivot lengths over 2, 3, 5, 8 (all four jointly) with everything else frozen; fail if the sign of net return flips for the published cell (3, 3, 3, 3) or if fewer than half the cells produce positive net return ⇒ parameter-lottery diagnosis, no adoption.
- **F6 — Regime breakdown.** Threshold: split the sample into thirds by trailing 60-day realized volatility and, separately, by a 60-day simple trend-strength tercile; fail if net Sharpe is negative in at least two of three terciles in either split ⇒ the rule requires a regime gate the source does not contain, no adoption.
- **F7 — Placebo.** Threshold: compare against buy-and-hold BTCUSDT on the identical window and against 1000 random entry-date sequences preserving the observed holding-time distribution; fail if observed net Sharpe does not exceed the 95th percentile of the placebo distribution ⇒ no evidence the breakout timing carries information.
- **F8 — Capacity and liquidity.** Threshold: fail if the required notional (100 percent of equity) exceeds 5 percent of the trailing 30-day median daily volume of BTCUSDT spot ⇒ capacity-capped, record the ceiling and block any size scaling.
- **F9 — Cross-instrument generalization.** Threshold: run the identical frozen rule on ETHUSDT spot and on one further major spot pair chosen before inspection; fail if 0 of 2 produce positive net return after costs at 2 bps per side ⇒ single-asset overfit diagnosis.
- **F10 — Frozen forward window.** Threshold: forward test from 2026-10-05 to 2027-10-04 with every parameter frozen; fail if forward net Sharpe at 2 bps per side is 0 or below ⇒ reject; no parameter may be changed to re-run it.

Global no-retuning rule: `orderDirection LONG`, pivot lengths 3/3/3/3, disabled dates, strict `high > lastHigh` entry, strict `low < lastLow` exit, no stop/take-profit/time exit, `pyramiding` at its documented default (one open same-side entry), `percent_of_equity` 100 compounding sizing, `process_orders_on_close` same-bar-close fills, 0 percent commission and 0 ticks slippage, the single `1d` timeframe and the BTCUSDT spot instrument are frozen. No gate may be rescued by changing a parameter, widening a window, switching venue, dropping a cost leg or re-defining a metric after seeing results.

## Crypto portability

`direct` — with a narrow meaning. The rule consumes only `high` and `low` of daily bars and trades long-only market orders at bar closes with full-equity sizing, all natively available on any 24/7 crypto spot venue; there is no session, holiday or opening-auction dependency, and the only calendar expression in the source is inert at defaults. `direct` refers only to mechanism, signal and instrument applicability; it is explicitly not a claim of crypto performance, which is `unproven` because the artifact prints no result.

Portability-relevant facts:

- No funding, open interest, mark or index price, liquidation feed, order book, aggressor side, on-chain data or options input is used, and none can invalidate the signal; no shorting means no borrow, no margin call and no funding accrual exist anywhere in the pinned rule.
- Risks that remain crypto-specific and unmodeled by the source: spread and market-impact differences for a full-equity market order (`data gap`), venue fee-schedule differences versus the documented 0 percent default (`data gap`), listing and delisting churn for anything other than BTCUSDT (`data gap`), venue fragmentation and custody risk (`data gap`), and stablecoin-peg or quote-currency events (`data gap`).
- Timestamps are exchange-defined UTC daily candles; because the date gate is identically true at defaults, the record does not depend on any boundary convention.

Crypto portability is not authorization to trade and not evidence that the mechanism survives in crypto.

## Limitations

- `not independently reproduced`. Nothing in this record has been recomputed from data.
- `data gap`: no spread, impact, latency or fill-failure model; no missing-data handling; no capacity statement; no account-currency pin; no performance output.
- `underspecified`: the quote currency resolved by `currency.NONE` (chart currency). Nothing else: venue, symbol and timeframe are research-pinned explicitly above, not left open.
- `contested`: the two description-versus-code contradictions in frontmatter; the code at pinned defaults governs.
- The long-only pin follows the source default input, not a Scout preference: changing `orderDirection` to BOTH or SHORT is a rule change outside this record.
- The pivot-confirmation lag means levels — and therefore the first possible signal — trail extremes by 3 bars by construction; late entries after fast vertical moves are the mechanism's known cost, stated here, not a defect to repair.

## Implementation status

- `implementation_status: not-implemented`. No Hummingbot, Qlib, n8n, Paper, Testnet or Live work has been performed from this record.
- Reproduction checklist for a future implementer (all values pinned above): `ta.pivothigh(3, 3)` / `ta.pivotlow(3, 3)` on `1d` BTCUSDT spot bars; per-side last-confirmed-level registers seeded missing; strict `high > lastHigh` long entry and strict `low < lastLow` long close at bar close; 100 percent equity market orders; earliest order bar index 6; dual-signal bars end flat.

## Adoption boundary

- `adoption: not-approved`, `approval_scope: research-only`. This record is a normalized research artifact admitted (if passed) only for LOSSLESS HB_READY semantic expressibility; it is not profitability validation, not survivor promotion, and not Paper, Testnet, Mainnet or live-trading approval.
- Downstream performance work must apply the house execution overlay explicitly and must not misrepresent it as source-native behaviour; F-gates above must run before any adoption discussion.

## Related Wiki records

- Wiki Brain search on 2026-10-05 for `pivot point breakout Kaufman` returned 0 records, and for `EduardoMattje Pivot Point Breakout PPB TW0P138b` returned 0 records. No Wiki record shares this source or mechanism, so none is cited.

## Sources

- https://github.com/hasnocool/tradingview-pine-scripts (`Pivot Point Breakout.pine` @ `69969aeaf271b2f7b5a7632a1bde43069a0cbe26`, blob `896a42e82880a722180c8c0665c1e3ef72913b6e`, 3270 bytes)
- https://tradingview.com/script/TW0P138b
- https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
- https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}entry
- https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}close
- https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}pivothigh
- https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}pivotlow
- https://www.tradingview.com/pine-script-docs/v5/concepts/strategies/
- https://www.tradingview.com/pine-script-docs/v5/language/user-defined-functions/
- https://www.tradingview.com/pine-script-docs/v5/language/variable-declarations/
- https://www.tradingview.com/pine-script-docs/migration-guides/to-pine-version-6/
