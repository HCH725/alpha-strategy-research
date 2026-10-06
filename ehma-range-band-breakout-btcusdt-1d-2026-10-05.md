---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Exponential Hull range-band breakout system on BTCUSDT 1d bars
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
  - https://www.tradingview.com/script/N4zgN11X-EHMA-Range-Strategy/
  - https://www.tradingview.com/pine-script-reference/v4/#fun_strategy
  - https://www.tradingview.com/pine-script-reference/v4/#fun_strategy{dot}entry
  - https://www.tradingview.com/pine-script-reference/v4/#fun_strategy{dot}close
  - https://www.tradingview.com/pine-script-reference/v4/#fun_sqrt
  - https://www.tradingview.com/pine-script-reference/v4/#op_nz
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
  - https://www.tradingview.com/pine-script-docs/language/user-defined-functions/
  - https://www.tradingview.com/pine-script-docs/language/variable-declarations/
  - https://www.tradingview.com/pine-script-docs/concepts/time/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The pinned code exposes a `pos_type` input with options Both/Long/Short, which advertises two-sided trading, but the pinned default is `Long`: at defaults the `if pos_type == \"Both\"` block and the `if pos_type == \"Short\"` block never execute, so no `strategy.short` order can ever be placed and no short close can ever fire. The two-sided behaviour exists only when a chart user changes the input away from its default; the pinned, default-parameter rule is long-only."
  - "The script description claims the range band makes the strategy 'robust against fake signals', which implies a measured property, but the pinned artifact contains no signal count, no whipsaw metric, no baseline and no performance number of any kind (census under Evidence); any realized robustness is emergent from the band width, not a stated rule."
---

# Exponential Hull range-band breakout system on BTCUSDT 1d bars

## Provenance

Immutable GitHub source (this is the primary source actually read end to end):

- Repository URL: https://github.com/hasnocool/tradingview-pine-scripts
- Full commit SHA: `69969aeaf271b2f7b5a7632a1bde43069a0cbe26` (commit date 2024-09-18T10:39:33Z). The GitHub `commits/HEAD` API returned this same SHA on 2026-10-05, so it is still the repository head at research time.
- Exact file path: `EHMA Range Strategy.pine` (spaces in filename preserved verbatim).
- Relevant stable public URL of the mirrored script: https://www.tradingview.com/script/N4zgN11X-EHMA-Range-Strategy/ (`EHMA Range Strategy`), fetched over HTTPS on 2026-10-05; its published description is verbatim identical to the mirror file's `Description:` header (modified version of @borserman's Exponential Hull script, range around the EHMA against fake signals), which corroborates the mirror rather than replacing it as the immutable artifact. The live page shows the author as GoldenPathFN while the mirror header prints `Author: OxLetoII`; both attributions are recorded here as printed, and the identical description identifies them as the same script.

Primary-source checksums pinned 2026-10-05:

- File 3567 bytes, SHA-256 `b79d9baebfb54541fc7a14825843db0cd5e8ca7ac741ad89d5c87b2fdc4d14d5`.
- Independent remote check: the file fetched back from the GitHub contents API at the pinned ref carries blob id `9c557d8ddd27aed8fdb0f4b86345d5e7db73ac63` with size 3567, and those bytes are byte-identical to the local artifact (identical SHA-256), so the pinned bytes are the bytes GitHub serves.

Artifact structure as printed: a `Script Name:` line (`EHMA Range Strategy`), an `Author:` line (`OxLetoII`), a `Description:` paragraph (borserman EHMA attribution, range-band premise, fake-signal claim), a `PineScript code:` section with a line-numbered dump, and an `Expand (75 lines)` trailer. The executable Pine block is file lines 92-148 (57 lines: `//@version=4`, one `strategy()` declaration, four `input()` value declarations, the `borserman_ema` user function, the EHMA/band assignments, three `plot()` calls, four signal booleans, two `input.time` date declarations, the `time_cond` expression, and three `if pos_type == ...` order blocks holding eight order calls). Everything gate-relevant below is read from those 57 lines.

Licence and rights: this record cites and normalizes the rule and reproduces no source code block beyond single-line declarations already quoted for gate evidence.

Pre-write dedup (2026-10-05): a search of the current working tree (excluding `.git`) for `ehma`, `hull`, `borserman`, `leto`, `rangewidth`, `range width` and `N4zgN11X` returned 0 matches; `gh pr list --state open` returned an empty list, so there is no open `research/*` PR to deduplicate against. Two Wiki Brain searches (`EHMA Hull borserman range breakout`, `OxLetoII GoldenPathFN range strategy`) each returned 0 records. The dedup set is therefore the five records on `main` (Gann HiLo, VIDYA CMO-adaptive, P-Signal erf, Bookstaber ATR, Kaufman pivot breakout) plus the four closed research PRs (#6 LazyBear Wave Trend, #10 golden/dead cross, #17 MACD histogram, #20 Ichimoku-RSI). Five-axis distinction: mechanism differs (exponential-Hull smoothing with a symmetric ±2 percent range band versus ATR-standardized change sign / displaced average-band flip / CMO-adaptive slope / erf dead-band / confirmed-pivot storage / oscillator cross / dual-EMA cross / MACD zero-cross / Ichimoku cloud), signal construction differs (strict `close > upper` entry / `close < lower` exit against a custom fully-visible recursion, no crossover of two series and no built-in indicator call anywhere), horizon is `1d` (coincides with Gann HiLo, Bookstaber and Kaufman pivot, whose mechanisms differ), source identity differs in all cases (hasnocool `EHMA Range Strategy.pine` versus FMZ 430857 / 427070 / 430552 / 440338 / hasnocool `Pivot Point Breakout.pine` and the four closed sources), and direction handling differs (long-only at pinned defaults versus the Both/Short options the input offers but the default never takes).

## Economic mechanism

### Source-reported

- Attribution, as printed: "This script is a modified version of @borserman's script for the Exponential Hull Moving Average. All credit for the EHMA goes to him :)"
- Premise, as printed: "this script works with a range around the EHMA (which can be modified), in an attempt to be robust against fake signals. Many times a bar will close below a moving average, only to reverse again the next bar, which eats away at your profits."
- No sample, no metric, no baseline, no figure and no performance number of any kind is printed anywhere in the artifact (census under Evidence).

### Research interpretation

Falsifiable mechanism hypothesis: on a single 24/7 crypto instrument, displacing the entry trigger a fixed 2 percent above a fast-reactingHull-style average (and the exit trigger symmetrically below it) buys hysteresis with band width instead of confirmation lag — a close beyond the band marks order flow strong enough to clear both the average and the noise margin, and such clears exhibit short-horizon directional persistence because stop-driven and breakout-driven flow unwinds only partially within one daily bar; the mirror-image breakdown closes the long because losing the lower band marks the failure of the same auction. The bet is continuation after band absorption, not mean reversion. The exponential Hull construction reacts faster than a simple average of the same nominal length while the band suppresses whipsaw; the 180-bar nominal length sets the trend scale. This is a ported technical-analysis hypothesis: the source supplies the borserman attribution but no behavioural argument, no sample and no evidence, so the mechanism is research interpretation, not source-reported fact.

Component roles, stated plainly because the source offers no composite structure:

- Primary signal: strict inequalities of the current bar's close against the computed bands (`close[t] > upper[t]` to enter, `close[t] < lower[t]` to exit).
- Noise filter: the ±2 percent band itself (`RangeWidth = 0.02`); there is no confirmation lag and no second filter.
- Trend / regime filter: none beyond the 180-bar Hull scale.
- Direction gate: the `pos_type` input, pinned at its default `Long`, which is what makes the pinned rule long-only and spot-applicable.

## Signal

Everything below is read from the pinned Pine block. Nothing in this section is `research-proposed`. All statements hold at the pinned source defaults (`pos_type = "Long"`, `Period = 180`, `RangeWidth = 0.02`, `startDate = 2017-01-01T00:00:00`, `finishDate = 2029-01-01T00:00:00`); any other input combination is a different, unpinned rule.

**Formation timestamp and tradability**

- Decision series: completed `1d` bars of the pinned instrument (research-pinned single decision timeframe; the script itself is timeframe-agnostic — 0 `request.*` calls, 0 `security(` calls, 0 `timeframe` references, 0 `input.timeframe` — so exactly one decision timeframe is declared by this record, `1d`, with no multi-timeframe dependency to align).
- Inputs at decision bar `t`: `close[t]` (current close), the band values `upper[t]` / `lower[t]` (exact functions of `close[t]` and earlier closes only), and bar `time[t]`. `open`, `high`, `low` are never read by the trading logic, `volume` occurs 0 times in the whole artifact (the three `plot()` calls render the EHMA and the two bands only and feed no order).
- Order timing: the live order calls at defaults are one `strategy.entry` and one `strategy.close`, both market orders (no `limit`/`stop` arguments anywhere — 0 occurrences of each), and the declaration sets `process_orders_on_close=true`. Official first-party documentation states that when this parameter is true the broker emulator processes orders "on the closing tick of each bar", and the reference adds "If the orders are market orders, the broker emulator executes them before the next bar's open." This is exactly a completed-bar decision with same-bar-close execution; there is no next-bar-open fill anywhere in the rule.
- Recalculation: neither `calc_on_every_tick` nor `calc_on_order_fills` appears in the pinned declaration (0 occurrences of each). Official documentation states both default to `false`. Recorded as source-declared-by-language-default, not as a research-proposed choice; it also means no intrabar re-evaluation can create a second order on the same bar.
- Date gate: the artifact contains 2 `input.time` declarations (`startDate`, `finishDate`, defaults `timestamp("2017-01-01T00:00:00")` and `timestamp("2029-01-01T00:00:00")`) combined as `time_cond = time >= startDate and time <= finishDate`, and both live order calls carry `and time_cond`. At the pinned defaults the gate admits every bar from 2017-01-01 through 2029-01-01, which covers the full BTCUSDT history and the present; it is an explicit source rule, recorded exactly as written rather than deleted. The `timestamp()` calls omit the timezone argument, so Pine resolves them to the symbol's exchange timezone and the artifact pins no timezone (same boundary convention as the already-admitted Gann HiLo record). `timenow` occurs 0 times. Note the explicit consequence: after `finishDate` both legs stop firing, so a position still open at 2029-01-01 would freeze — source behaviour, stated here, not repaired.

**Lookback, formulas and warmup**

- Parameters as declared: `pos_type = input(defval = "Long", title="Position Type", options=["Both", "Long", "Short"])` → defval `"Long"`; `Period = input(defval=180, title="Length")` → 180; `RangeWidth = input(defval=0.02, step=0.01, title="Range Width")` → 0.02; `sqrtPeriod = sqrt(Period)` → √180 (kept symbolic; IEEE `sqrt` is deterministic across implementers, so no rounding choice is required).
- Recursion, exact, quoted for structure (single-expression function, no hidden state):
  - `alpha = 2 / (y + 1)` with call-site `y` values 90 (`Period / 2`), 180 (`Period`) and √180 (`sqrtPeriod`) — all provably nonzero, so both division operators in the entire executable block (`2 / (y + 1)` and `Period / 2`) have nonzero divisors and no zero-divisor path exists anywhere in the rule.
  - `sum = 0.0` then `sum := alpha * x + (1 - alpha) * nz(sum[1])`: the `nz()` call converts the first-bar `na` history to 0 deterministically, so every call site is fully defined from bar index 0 with no seeding choice. This is a custom recursion written out in the source, not a built-in average: the artifact contains 0 `ta.ema`, 0 `ta.dema`, 0 `ta.tema`, 0 bare `ema(`, and 0 calls to any `ta.*`, `dmi(`, `rsi(`, `atr(`, `sma(`, `wma(`, `hma(`, `vwma(`, `stdev(`, `lowest(` or `highest(` — none of the seeding blockers that closed earlier PRs arise here.
  - `EHMA = borserman_ema(2 * borserman_ema(close, Period / 2) - borserman_ema(close, Period), sqrtPeriod)`: three call sites, each maintaining its own independent history per official user-defined-function documentation (the same per-call-site independence the PASS review of the Kaufman pivot record relied on).
- Bands, exact: `upper = EHMA + (EHMA * RangeWidth)`, `lower = EHMA - (EHMA * RangeWidth)`, i.e. ±2 percent of EHMA at defaults. Multiplications only.
- Derived conditions, exact, at defaults:
  - Long entry condition: `long = close[t] > upper[t]`, live via `strategy.entry("Long", strategy.long, comment="Long", when=long and time_cond)`.
  - Long exit condition: `exit_long = close[t] < lower[t]`, live via `strategy.close("Long", comment="Exit Long", when=exit_long and time_cond)` with no quantity argument, i.e. a full close of that single entry id.
  - Dead at defaults (recorded, never firing): the `if pos_type == "Both"` block (one long pair plus one short pair) and the `if pos_type == "Short"` block (one short pair); string comparison against the `"Long"` default is identically false for both.
- Mutual exclusivity (no same-bar conflict by construction): `upper[t] - lower[t] = 2 * EHMA[t] * 0.02`, strictly positive whenever `EHMA[t] > 0`, which holds for any positive-price series (the recursion smooths closes); `close[t]` therefore cannot satisfy `close > upper` and `close < lower` on the same bar, so entry and exit never fire together, no call-order priority is required, and exact-equality on either band (`==`) fires neither leg — the tie case is defined, not ambiguous. The rule contains 0 `crossover`, 0 `crossunder` and 0 `ta.cross`, so the tie-semantics blocker that closed PR #6 cannot arise.
- Warmup, derived from the pinned code because the source declares none: every series (`borserman_ema` states via `nz`, EHMA, both bands, all four booleans, `time_cond`) is defined from bar index 0 — there is no `na` anywhere in the executable path and no lookback window to fill. The earliest possible order is therefore the first bar on which `time_cond` holds and the signal boolean holds (no indicator warmup beyond the data series itself). `max_bars_back` is not declared; official documentation states the required history buffer is detected automatically, and the rule references no lag beyond contemporaneous `close[t]`/`time[t]`.

**Entry**

- Long entry: `if pos_type == "Long"` → `strategy.entry("Long", strategy.long, comment="Long", when=long and time_cond)`; at defaults the `if` guard is identically true and `when` reduces to the band test plus the date gate.
- Short entry: source-present but dead at defaults (see above). Direction is therefore long-only at the pinned defaults: one live `strategy.entry`, `strategy.long` once live, `strategy.short` zero live occurrences.
- The statement omits `qty`. Official reference: the default is `na`, which means the command uses the declaration's `default_qty_type`/`default_qty_value` — here `strategy.percent_of_equity` with value `100`.
- The statement omits `limit` and `stop`; official reference: the defaults are `na`, so the order is a market order. The `comment="Long"` argument is display-only.

**Exit**

- The pinned code contains exactly eight order calls: 4 `strategy.entry`, 4 `strategy.close`. Censuses over the whole 3567-byte artifact: `strategy.close_all` 0, `strategy.exit` 0, `strategy.order` 0, `strategy.stop` 0, `strategy.cancel` 0, `strategy.cancel_all` 0, `strategy.risk.*` 0, `limit =` 0, `stop =` 0, `strategy.position_*` 0. At defaults exactly one close is live: `strategy.close("Long", ..., when=exit_long and time_cond)` on `close < lower`.
- Stop loss: none. Take profit: none. Trailing stop: none. Time limit or maximum holding period: none (the date inputs bound *both* legs only by the 2017/2029 window, and freeze them after it). Flat state: reachable before the first entry and after every band-breakdown exit; the system is otherwise long. This directly contradicts the description's implied fake-signal robustness as a designed property (contradiction 2).

**Holding period, overlap and re-entry**

- Holding period: unbounded and determined entirely by waiting for the next `close < lower` breakdown; the source states no maximum or expected holding period.
- Maximum same-side concurrency: 1. `pyramiding` is not written in the declaration (0 occurrences), so the value comes from the language default, and both official statements of that default describe the same observable rule even though they print different numbers: the v4 reference states the maximum same-direction entries with default 0 ("only one entry order in the same direction can be opened, and additional entry orders are rejected"), while the Strategies page states default 1 ("the strategy can open new positions but cannot add to them"). Under each document's own definition the result is identical — one open same-side entry, further same-side entries rejected — and with a single live entry id ("Long") there is no second id that could add on. The record therefore records `pyramiding` as source-declared-by-language-default with that convergence stated rather than silently picking one number, and F3 forces the executing engine to confirm it. This is the same convergence the PASS reviews of PR #12 and PR #21 accepted.
- Same-direction re-entry: after a breakdown exit the system is flat, so the next `close > upper` bar opens a fresh long; while long, a further entry signal is rejected under the default above, and orders fill on the same bar they are created, so no unfilled order survives into the next bar.
- Cooldown: none declared, and the strategy declaration exposes no cooldown field. A fresh entry requires a fresh `close > upper` event while flat, so cooldown semantics are provably irrelevant rather than missing.

**Parameters, sizing and pyramiding**

- Declared verbatim in the pinned declaration: `strategy(title="EHMA Range Strategy", process_orders_on_close=true, explicit_plot_zorder=true, overlay=true, initial_capital=1500, default_qty_type=strategy.percent_of_equity, commission_type=strategy.commission.percent, commission_value=0.085, default_qty_value=100)`. `explicit_plot_zorder` and `overlay` are display-only; the code-declared trading values are `initial_capital=1500`, `default_qty_type=strategy.percent_of_equity`, `default_qty_value=100`, `commission_type=strategy.commission.percent`, `commission_value=0.085`, `process_orders_on_close=true`.
- Declaration parameters the code leaves unset, each recorded as source-declared-by-language-default with the official page that documents it: `currency=currency.NONE` ("in which case the chart's currency is used"), `slippage=0` ticks, `calc_on_order_fills=false`, `calc_on_every_tick=false`, `close_entries_rule="FIFO"` (moot: a single live entry id with full closes), `margin_long`/`margin_short` at documented defaults (no position-size enforcement exercised: the rule never sizes by leverage), `pyramiding` (convergence above), `max_bars_back` auto-detected, `backtest_fill_limits_assumption=0` (no price-dependent orders exist) and `use_bar_magnifier=false`.
- Sizing: `strategy.percent_of_equity` with value 100, i.e. each entry is 100 percent of available equity — declared in the code, therefore explicit and compounding.
- Direction: long-only at pinned defaults (see Entry). Spot is therefore the deterministic market type and no margined instrument is required (see Required data).
- Nothing else is declared: `currency`, `slippage`, `margin_*`, `pyramiding`, `close_entries_rule`, `calc_*`, `max_bars_back` and `use_bar_magnifier` all occur 0 times in the artifact.

**Reconstruction status**

Every field required to replay the rule — indicator variant and its parameters, source prices, lookback (none beyond contemporaneous bars — the recursion is `nz`-seeded from bar 0), smoothing (the custom borserman recursion quoted verbatim, no built-in average), thresholds (the ±2 percent bands themselves), comparison logic, direction, entry, exit, risk semantics, sizing, pyramiding, concurrency, cooldown, timeframe, fill timing and warmup — is explicit either in the pinned source or in official first-party documentation of the pinned source's own language defaults and functions. The residual `underspecified` items are the exact quote currency of the account under `currency.NONE`, the exchange timezone of the 2017/2029 date gate, and the cost/latency/fill-failure model beyond the declared 0.085 percent commission; none alters the signal, and all are recorded as `data gap` or boundary convention rather than filled. There is no perpetual-versus-dated question here because the pinned rule is long-only spot.

## Required data

- Instrument: BTCUSDT on spot, research-pinned as the single-pair run of a venue-agnostic rule. The source script declares no venue, no exchange and no symbol (it runs on whatever chart it is attached to); because the pinned default rule never shorts, uses no margin and uses no leverage, spot is deterministically applicable and no futures, perpetual-or-dated, distinction can arise. Single pair, single instrument, no basket, no ranking, no cross-sectional step.
- Market type: spot. Long-only at pinned defaults; naked shorting is never required because the short legs are dead code at defaults.
- Spot applicability: fully applicable — the complete pinned rule (long entries, breakdown closes, 100 percent equity sizing) executes on spot.
- Venue: any venue listing BTCUSDT spot; no venue-selection rule, no listing or survivorship rule (the artifact states none).
- Timeframe: exactly one decision timeframe, `1d`, research-pinned for this record. The pinned script contains 0 `request.*` calls and 0 `security(` calls, so no lower- or higher-timeframe series is referenced by the rule and there is no multi-timeframe dependency to align. `use_bar_magnifier` is at its documented `false` default, so no lower-timeframe data is used for fills either.
- Fields used: `close[t]` and bar `time[t]` only (current-bar close against the computed bands, plus the date gate). `open`, `high`, `low` and `volume` are never read by the trading logic (the three `plot()` calls render the EHMA and the bands only).
- Fields not required and not used, each absent from the pinned artifact: open interest, funding, mark or index price, basis, order book or depth, trade or aggressor feed, liquidation feed, on-chain data, options or Greeks, sentiment or news, macro series, cross-venue state, borrow data, margin state. The calendar is gated only by the explicit 2017/2029 `time_cond` expression (see Signal).
- Point-in-time: every input at bar `t` is contemporaneous (`close[t]`, `time[t]`) or a deterministic function of closes at or before `t` (the recursion reads only `x[t]` and its own prior-bar state); there is no future reference, no negative shift in any order input, no future extrema, no full-sample normalization, no `timenow` (0 occurrences), and no `security` call of any kind, so the pinned rule contains no look-ahead leakage. The `plot()` calls carry no offsets that feed any order.
- Timestamp and timezone: bar open times of a 1-day BTCUSDT spot series compared against the exchange-timezone-resolved 2017-01-01/2029-01-01 defaults; the timezone argument is omitted, so Pine resolves it to the symbol's exchange timezone, and the artifact pins no timezone → `underspecified` boundary convention only (same treatment as the admitted Gann HiLo record).
- Missing data: no gap, halt or stale-bar handling is specified anywhere in the source → `data gap`. Imputation would be `research-proposed` and is not proposed here. There are no `na` paths in the executable rule to handle: `nz()` seeds the recursion, `sqrt(180)` is defined, and every comparison is boolean from bar 0.
- Funding, fee and spread needs: none specified and none applicable to a spot rule. Word-boundary census of the pinned 3567-byte artifact gives sharpe 0, drawdown 0, cagr 0, return 0, profit 0, annualized 0, roi 0, slippage 0, fee 0, funding 0, leverage 0, spread 0, capacity 0, turnover 0, cooldown 0, pyramiding 0, take 0, trailing 0, backtest 0; commission 0 in prose but `commission_value=0.085` declared in code (a priced 0.085 percent, not a zero-cost assumption); margin 0, interest 0, equity 0 in prose but `percent_of_equity` declared once in code. Spread, impact and latency are `data gap`, never a modeled zero.

## Execution assumptions

Source-declared (quoted or read from the pinned declaration, the pinned code, or official first-party documentation of that same language):

- Order type: market orders, created only by the one live `strategy.entry` and the one live `strategy.close` at defaults. There is no limit order, no stop order, no stop-limit, no OCA group and no conditional price order anywhere in the rule (0 `strategy.exit`, 0 `strategy.order`, 0 `limit`/`stop` arguments), so there is no intrabar-path dependence and no maker/taker asymmetry to model. The broker emulator's documented intrabar assumptions are never exercised, because they apply only to price-dependent orders.
- Fill model: `process_orders_on_close=true` → official documentation: orders are processed "on the closing tick of each bar", and for market orders "the broker emulator executes them before the next bar's open". `calc_on_every_tick` and `calc_on_order_fills` default to `false`, so there is exactly one evaluation per completed bar. Completed-bar decision with same-bar-close execution.
- Signal-to-order delay: none. The order is created and filled on the same completed-bar close; the engine's "Order execution delay" override defaults to 0 ticks.
- Dual-signal bar: impossible by construction (mutual exclusivity proven under Signal); there is no entry-then-close ordering to account for.
- Position limits: one position at a time, 100 percent of available equity per position, no same-side add-on (default `pyramiding`, convergence recorded above), no scaling, no grid, no martingale, no hedge, no shorting at defaults.
- Leverage and margin: unset in code → documented defaults (no position-size enforcement exercised by the rule); sizing is equity-percentage, so the rule never sizes by leverage and has no leverage-dependent edge. Spot cash only.
- Costs: `commission_type=strategy.commission.percent` with `commission_value=0.085`, i.e. 0.085 percent of order cash volume charged on the entry fill and again on the exit fill — a source-declared priced cost, not a zero assumption; `slippage` defaults to 0 ticks per the official reference. No spread, no market-impact model appears anywhere in the artifact → the remaining cost legs are `data gap`; this record does not adopt a validated zero-cost assumption beyond the documented defaults.
- Latency: not modeled in source → `data gap`.
- Participation and capacity: not modeled in source → `data gap`; tested by the research-defined gate F8.
- Failure handling (partial fills, rejects, downtime): not addressed in source → `data gap`. The pinned rule places whole market orders only, and no partial-fill-dependent condition exists.
- Engine-settings overrides a chart user could apply (timeframe, symbol, initial capital, currency, pyramiding, commission, pos_type, Period, RangeWidth, dates, order size, order execution delay) are not part of the pinned source; the code-declared values plus documented defaults above are the recorded strategy.
- Scout-vs-source split: the venue-agnostic script is evaluated here as one explicit single-pair run (BTCUSDT spot, `1d`); every other item above marked source-declared comes from the pinned declaration, the pinned code, or official TradingView documentation of that language. Nothing in this section is a Scout-added execution rule; every pass/fail cutoff used later is labeled `research-defined`.

## Evidence

### Source-reported

The artifact prints no performance result of any kind. Word-boundary census over the pinned 3567-byte artifact: sharpe 0, drawdown 0, cagr 0, return 0, profit 0, win 0, annualized 0, roi 0, net profit 0, max drawdown 0, profit factor 0, strategy tester 0, open interest 0, slippage 0, fee 0, funding 0, leverage 0, spread 0, capacity 0, turnover 0, cooldown 0, pyramiding 0, trailing 0, backtest 0; `time` occurs 3 times (twice as bar `time` in `time_cond`, once in a comment); `timeframe` occurs 0 times. There is no equity curve, no trade list, no table and no figure anywhere in the artifact, and a TradingView script page shows none either.

What the source does report:

- Configuration only, from the pinned code: `//@version=4`, `pos_type` default Long with Both/Long/Short options, `Period` 180, `RangeWidth` 0.02, dates 2017-01-01 to 2029-01-01, `percent_of_equity` 100, 0.085 percent commission, `process_orders_on_close=true`.
- Qualitative claims, verbatim, with no sample, no metric, no baseline and no figure: the borserman-EHMA attribution, the range-band premise, "robust against fake signals", "Many times a bar will close below a moving average, only to reverse again the next bar, which eats away at your profits" — unverifiable as printed and recorded as bare claims, not as evidence.
- Research-computed, not printed: at the pinned defaults the rule is a strict-inequality test of the current close against ±2 percent bands of a custom exponential-Hull recursion, so its trigger rate is set by realized volatility relative to the 180-bar Hull scale, not by any fixed price distance.

No source-reported figure in this record comes from any other paper, article or repository; every claim is attributed to the single pinned artifact above. Third-party pages that re-host this script's statistics are not cited and contribute no number to this record.

### Independently reproduced

not independently reproduced

Only the following were performed: SHA-256 checksumming of the pinned artifact; a byte-identical re-fetch of the file blob by its id from the GitHub contents API; a whole-artifact term and word-boundary census; enumeration of `strategy.*`, `input*`, `ta.*`, `plot*`, `timestamp`, `nz`, `sqrt` call sites and of identifier occurrence counts; a same-bar dual-signal impossibility proof from the band arithmetic; reading of the public TradingView script page header (title/description match only); and live reading over HTTPS of the official TradingView documentation pages cited under Sources. No market data was downloaded, no backtest was run, no Pine or third-party code was executed, and no statistic was recomputed from data.

### Negative evidence

1. The artifact prints zero performance numbers, so there is nothing to reproduce: sharpe, drawdown, cagr, return, win rate, annualized, roi and trade counts are all 0 occurrences.
2. The performance-sounding prose claims (fake-signal robustness, profit eaten away by reversals) carry no sample, no metric and no baseline, so they cannot be checked as printed.
3. The source's own input offers Both/Short trading while the pinned default trades long-only (recorded contradiction 1) — a reader following the input options would expect short trades the pinned rule never takes.
4. The source implies designed fake-signal robustness while the code contains no whipsaw counter, no stop, no target and no time exit (recorded contradiction 2).
5. Sizing is 100 percent of available equity on every position: full-equity concentration, no cash buffer, no volatility targeting, no risk layer of any kind.
6. Holding is unbounded: with no time exit and no level exit beyond the mirror breakdown, exposure persists indefinitely until the next band breakdown — and past the 2029 `finishDate` even a breakdown cannot exit it (explicit source behaviour, stated not repaired).
7. `sqrtPeriod = sqrt(Period)` is irrational; it is kept symbolic in this record and any re-implementation must compute IEEE `sqrt(180)` rather than round it, or the outer recursion's alpha differs.
8. The description's short/both legs exist only as user-selectable options, not as pinned behaviour; promoting them would be a rule change.
9. Commission is priced (0.085 percent per fill) but slippage is a 0-tick language default with no spread or impact model — so any edge claim remains partially unpriced by the source.
10. No train/test split, no out-of-sample section and no walk-forward exists anywhere in the source.

## Falsification plan

All thresholds below are research-defined tests, never substitutes for the execution rules above (which are frozen: pos_type Long, Period 180, RangeWidth 0.02, dates 2017-01-01/2029-01-01, percent_of_equity 100 compounding, same-bar-close fills, 0.085 percent commission, 0-tick slippage, single `1d` timeframe, BTCUSDT spot).

- **F1 — Signal presence.** Threshold: at least 30 long entries and at least 10 band-breakdown exits on 5 years of `1d` BTCUSDT spot bars; fail ⇒ the rule never trades this instrument/timeframe, record stays research-only.
- **F2 — Mutual-exclusivity audit.** Threshold: scan the full sample and confirm zero bars carry `close > upper` and `close < lower` jointly true; fail ⇒ the impossibility proof claimed above does not replay, pin the discrepancy and keep research-only.
- **F3 — Engine-default audit gate.** Threshold: the executing engine must confirm every recorded declaration and language default end to end — 100 percent equity sizing, same-bar-close fills, 0.085 percent commission, 0-tick slippage, once-per-bar evaluation, same-side entries rejected while long, per-call-site recursion histories, earliest possible order on the first date-admitted signal bar; fail ⇒ pin the discrepancy in writing and keep research-only, no adoption.
- **F4 — Cost ladder.** Threshold: apply 0 / 1 / 2 / 5 / 10 bps per side on top of the declared 0.085 percent; fail if net annualized return turns non-positive at 2 bps per side or net Sharpe falls to 0 or below at 5 bps per side ⇒ cost-dependent edge, no adoption.
- **F5 — Parameter perturbation.** Threshold: sweep Period over 90, 180, 360 and RangeWidth over 0.01, 0.02, 0.04 (nine cells jointly) with everything else frozen; fail if the sign of net return flips for the published cell (180, 0.02) or if fewer than half the cells produce positive net return ⇒ parameter-lottery diagnosis, no adoption.
- **F6 — Regime breakdown.** Threshold: split the sample into thirds by trailing 60-day realized volatility and, separately, by a 60-day simple trend-strength tercile; fail if net Sharpe is negative in at least two of three terciles in either split ⇒ the rule requires a regime gate the source does not contain, no adoption.
- **F7 — Placebo.** Threshold: compare against buy-and-hold BTCUSDT on the identical window and against 1000 random entry-date sequences preserving the observed holding-time distribution; fail if observed net Sharpe does not exceed the 95th percentile of the placebo distribution ⇒ no evidence the band-breakout timing carries information.
- **F8 — Capacity and liquidity.** Threshold: fail if the required notional (100 percent of equity) exceeds 5 percent of the trailing 30-day median daily volume of BTCUSDT spot ⇒ capacity-capped, record the ceiling and block any size scaling.
- **F9 — Cross-instrument generalization.** Threshold: run the identical frozen rule on ETHUSDT spot and on one further major spot pair chosen before inspection; fail if 0 of 2 produce positive net return after costs at 2 bps per side ⇒ single-asset overfit diagnosis.
- **F10 — Frozen forward window.** Threshold: forward test from 2026-10-05 to 2027-10-04 with every parameter frozen; fail if forward net Sharpe at 2 bps per side is 0 or below ⇒ reject; no parameter may be changed to re-run it.

Global no-retuning rule: `pos_type Long`, Period 180, RangeWidth 0.02, the 2017/2029 date window, strict `close > upper` entry, strict `close < lower` exit, no stop/take-profit/time exit, `pyramiding` at its documented default (one open same-side entry), `percent_of_equity` 100 compounding sizing, `process_orders_on_close` same-bar-close fills, 0.085 percent commission and 0 ticks slippage, the single `1d` timeframe and the BTCUSDT spot instrument are frozen. No gate may be rescued by changing a parameter, widening a window, switching venue, dropping a cost leg or re-defining a metric after seeing results.

## Crypto portability

`direct` — with a narrow meaning. The rule consumes only `close` of daily bars plus bar time and trades long-only market orders at bar closes with full-equity sizing, all natively available on any 24/7 crypto spot venue; there is no session, holiday or opening-auction dependency, and the only calendar expression in the source is the explicit 2017/2029 window that admits the full history. `direct` refers only to mechanism, signal and instrument applicability; it is explicitly not a claim of crypto performance, which is `unproven` because the artifact prints no result.

Portability-relevant facts:

- No funding, open interest, mark or index price, liquidation feed, order book, aggressor side, on-chain data or options input is used, and none can invalidate the signal; no shorting means no borrow, no margin call and no funding accrual exist anywhere in the pinned rule.
- Risks that remain crypto-specific and unmodeled by the source: spread and market-impact differences for a full-equity market order (`data gap`), venue fee-schedule differences versus the declared 0.085 percent (`data gap`), listing and delisting churn for anything other than BTCUSDT (`data gap`), venue fragmentation and custody risk (`data gap`), and stablecoin-peg or quote-currency events (`data gap`).
- Timestamps are exchange-defined UTC daily candles gated by the source's own 2017/2029 window under the exchange-timezone boundary convention noted above.

Crypto portability is not authorization to trade and not evidence that the mechanism survives in crypto.

## Limitations

- `not independently reproduced`. Nothing in this record has been recomputed from data.
- `data gap`: no spread, impact, latency or fill-failure model; no missing-data handling; no capacity statement; no account-currency pin; no performance output.
- `underspecified`: the quote currency resolved by `currency.NONE` (chart currency); the exchange timezone of the 2017/2029 date gate. Nothing else: venue, symbol and timeframe are research-pinned explicitly above, not left open.
- `contested`: the two description-versus-code tensions in frontmatter; the code at pinned defaults governs.
- The long-only pin follows the source default input, not a Scout preference: changing `pos_type` to Both or Short is a rule change outside this record.
- The 180-bar Hull scale means the bands — and therefore the first sensible signals — trail trends by construction; late entries after fast vertical moves are the mechanism's known cost, stated here, not a defect to repair.

## Implementation status

- `implementation_status: not-implemented`. No Hummingbot, Qlib, n8n, Paper, Testnet or Live work has been performed from this record.
- Reproduction checklist for a future implementer (all values pinned above): `borserman_ema` recursion with `alpha = 2 / (y + 1)` and `nz`-seeded state at three independent call sites (`f(close, 90)`, `f(close, 180)`, outer `f(2*inner90 - inner180, sqrt(180))`) on `1d` BTCUSDT spot closes; bands at ±2 percent of EHMA; strict `close > upper` long entry and strict `close < lower` full long close at bar close, both additionally gated by 2017-01-01/2029-01-01 bar time; 100 percent equity market orders; entries and exits mutually exclusive on every bar.

## Adoption boundary

- `adoption: not-approved`, `approval_scope: research-only`. This record is a normalized research artifact admitted (if passed) only for LOSSLESS HB_READY semantic expressibility; it is not profitability validation, not survivor promotion, and not Paper, Testnet, Mainnet or live-trading approval.
- Downstream performance work must apply the house execution overlay explicitly and must not misrepresent it as source-native behaviour; F-gates above must run before any adoption discussion.

## Related Wiki records

- Wiki Brain searches on 2026-10-05 for `EHMA Hull borserman range breakout` and for `OxLetoII GoldenPathFN range strategy` each returned 0 records. No Wiki record shares this source or mechanism, so none is cited.

## Sources

- https://github.com/hasnocool/tradingview-pine-scripts (`EHMA Range Strategy.pine` @ `69969aeaf271b2f7b5a7632a1bde43069a0cbe26`, blob `9c557d8ddd27aed8fdb0f4b86345d5e7db73ac63`, 3567 bytes)
- https://www.tradingview.com/script/N4zgN11X-EHMA-Range-Strategy/
- https://www.tradingview.com/pine-script-reference/v4/#fun_strategy
- https://www.tradingview.com/pine-script-reference/v4/#fun_strategy{dot}entry
- https://www.tradingview.com/pine-script-reference/v4/#fun_strategy{dot}close
- https://www.tradingview.com/pine-script-reference/v4/#fun_sqrt
- https://www.tradingview.com/pine-script-reference/v4/#op_nz
- https://www.tradingview.com/pine-script-docs/concepts/strategies/
- https://www.tradingview.com/pine-script-docs/language/user-defined-functions/
- https://www.tradingview.com/pine-script-docs/language/variable-declarations/
- https://www.tradingview.com/pine-script-docs/concepts/time/
