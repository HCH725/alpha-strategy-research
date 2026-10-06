---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Richard Bookstaber ATR momentum breakout reversal system on BTCUSDT 1d bars
created: 2026-10-05
updated: 2026-10-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-04-30
sources:
  - https://github.com/fmzquant/strategies
  - https://www.fmz.com/strategy/430857
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}entry
  - https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}atr
  - https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}rma
  - https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}tr
  - https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}change
  - https://www.tradingview.com/pine-script-docs/v5/concepts/strategies/
  - https://www.tradingview.com/pine-script-docs/v5/language/user-defined-functions/
  - https://www.tradingview.com/pine-script-docs/v5/language/variable-declarations/
  - https://www.tradingview.com/pine-script-docs/migration-guides/to-pine-version-6/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The Advantage Analysis states 'Dynamic ATR stop loss can effectively control risks with adaptive stop loss based on market volatility', the Summary states 'ATR stop loss allows it to adapt to market volatility', and the Chinese block states the same two claims, but the pinned code contains no stop loss of any kind: strategy.exit 0, strategy.stop 0, strategy.close 0, strategy.close_all 0, strategy.order 0, 0 limit arguments and 0 stop arguments, so the only exit instruction in the whole rule is an opposite-direction strategy.entry that reverses the position."
  - "The Strategy Logic states that the strategy 'calculates the absolute value of the daily closing price change' (Chinese: '计算每日收盘价变化的绝对值'), but the pinned code computes the signed difference closingChange = ta.change(close, 1) and compares it against the threshold separately for each direction; the only math.abs() call in the artifact sits inside a plot() call that feeds no order."
  - "The Strategy Logic states that 'if the closing price rises more than the ATR upper rail, go long; if the closing price falls more than the ATR upper rail, go short', which describes a price level, while the pinned rule contains no price band at all: it compares the 1-bar close change with the previous bar's scaled ATR (atr[1]), a threshold on a difference rather than a level."
---

# Richard Bookstaber ATR momentum breakout reversal system on BTCUSDT 1d bars

## Provenance

Immutable GitHub source (this is the primary source actually read end to end):

- Repository URL: https://github.com/fmzquant/strategies
- Full commit SHA: `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit date 2025-04-30T03:10:28Z, i.e. 2025-04-30 11:10:28 +0800, subject `update`). The GitHub `commits/HEAD` API returned this same SHA on 2026-10-05, so it is still the repository head at research time.
- Exact file path: `理查德布克斯塔伯动量突破策略Richard-Bookstaber-Momentum-Breakout-Strategy.md` (the non-ASCII filename is preserved verbatim; percent-encoded blob URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E7%90%86%E6%9F%A5%E5%BE%B7%E5%B8%83%E5%85%8B%E6%96%AF%E5%A1%94%E4%BC%AF%E5%8A%A8%E9%87%8F%E7%AA%81%E7%A0%B4%E7%AD%96%E7%95%A5Richard-Bookstaber-Momentum-Breakout-Strategy.md ).
- Relevant source URL recorded inside the artifact: https://www.fmz.com/strategy/430857

Primary-source checksums pinned 2026-10-05 from a checkout of that exact commit:

- File 6779 bytes, SHA-256 `b9831f78243eecddb66047418c466983dfd1413b86255b58b234ea32b28dcb48`, 5373 characters, 160 newline characters.
- Whitespace-collapsed variant 5284 characters, SHA-256 `3fb1294950dc2de1b8e3653e81b813acf48d86d50959969b09809fff1bb05ec7`.
- The fenced Pine block alone: 1155 bytes, 43 newline characters (30 non-blank lines), SHA-256 `d5f72cafd9e5aa0bfa0178760b7c63286508f6c5828c69929087627b5991d452`, git blob `5cd7f8bb01ab0624322622c7ef1e73239ebb55e7`.
- Independent remote check: the git tree of the pinned commit lists that path as blob `6b23f46052ff2f2e28415450d1969b2e16304dea` with size 6779, and the blob fetched back from the GitHub API by that id is byte-identical to the local artifact (identical SHA-256), so the pinned bytes are the bytes GitHub serves.

Artifact structure as printed: `> Name` (理查德布克斯塔伯动量突破策略Richard-Bookstaber-Momentum-Breakout-Strategy), `> Author` = ChaoZhang, `> Strategy Description` (a Chinese section set and an English set inside one `[trans]` block, preceded by one image link), `> Strategy Arguments` table with two rows (`v_input_int_1` default 14 `Average length`, `v_input_float_1` default 2 `Multiplier`), `> Source (PineScript)` fenced block preceded by an FMZ `/*backtest ...*/` header, `> Detail` = https://www.fmz.com/strategy/430857, `> Last Modified` = 2023-11-02 15:12:46. The artifact's own `Strategy Arguments` table and the pinned `input` declarations agree on both values, so there is no table-versus-code conflict to record.

Licence and rights: the pinned Pine block itself prints `// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/` and the author credit `// © EduardoMattje`. The mirror repository ships no LICENSE file, so the redistribution status of the mirror as a whole is not stated in source; this record therefore cites and normalizes the rule and reproduces no source code block.

FMZ landing page read directly on 2026-10-05 over HTTPS (public, no login for the description layer): browser/page title `Richard Bookstaber Momentum Breakout Strategy | FMZ`, heading `Richard Bookstaber Momentum Breakout Strategy`, badge `Common strategy`, `Created: 2023-11-02 15:12:46`, `Last modified: 3 years ago`, `Copy: 3`, `Hits: 1044`, author account `ChaoZhang`, no comment block rendered, the English Overview / Strategy Logic / Advantage / Risk / Optimization / Summary prose identical to the mirror's English block, a rendered `Source / Pine` section showing the `/*backtest*/` header, the MPL-2.0 notice, `// © EduardoMattje` and the `//@version=5` line before the literal string `Login to view full source`, and two exposed Strategy parameters (`Average length` = 14, `Multiplier` = 2) that equal the code defaults. Word-boundary counts over the whole landing HTML: `Net Profit` 0, `Profit Factor` 0, `Sharpe` 0, `Max Drawdown` 0, `ROI` 0, `win rate` 0, `Backtest result` 0 — the landing shows no performance table, no equity curve and no trade list. Two provenance notes, stated rather than repaired: (a) although the UI hides the source behind a login, the page's own JavaScript payload embeds the complete Pine text; that payload was extracted, unescaped and compared with the pinned GitHub Pine block and is byte-identical (both 1155 bytes, both SHA-256 `d5f72cafd9e5aa0bfa0178760b7c63286508f6c5828c69929087627b5991d452`), so the landing page corroborates the mirror rather than replacing it as the immutable artifact; (b) the landing's displayed `Last modified: 3 years ago` (read 2026-10-05) is a relative label that cannot be reconciled with the displayed creation timestamp of 2023-11-02 from the page alone, and is recorded exactly as displayed.

FMZ backtest header printed verbatim inside the pinned artifact:

```text
start: 2022-10-26 00:00:00
end: 2023-11-01 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
```

Provenance gaps (stated, not repaired): no DOI, no version tag, no repository, no test suite, no issue tracker entry, no peer-review statement and no performance output anywhere; peer-review status is not stated in source; three different identities appear for one artifact — the mirror's `Author: ChaoZhang`, the code's own `// © EduardoMattje`, and the published title's attribution to Richard Bookstaber — and none of them is independently confirmed.

Pre-write dedup (2026-10-05): a hidden-inclusive search of the current working tree (excluding `.git`) for `bookstaber`, `430857`, `EduardoMattje`, `Volatility System`, `atrPenetration`, `closingChange`, `averageLength`, `理查德布克斯塔伯` and `momentum breakout` returned 0 matches; the loose probe `atr` returned only a strategy-name example inside `.agents/skills/research-intake-review/SKILL.md` and one dedup sentence inside the already-merged Gann HiLo record, neither of which shares this source or signal. `gh pr list --state open` returned an empty list, so there is no open `research/*` PR to deduplicate against; `git ls-remote --heads origin 'research/*'` returned five refs, all heads of already-closed or already-squash-merged PRs (#5, #6, #7, #9, #10). The same nine identifier probes in the Wiki Brain tree returned 0 matches except one prose mention of "momentum breakouts" inside [[quant/crypto-binance-smallcap-pump-reversal-regime-gated-falsification-2026-09-13]], which is a different source, a different mechanism and a different universe. The dedup set is therefore the three records on `main`: Gann HiLo, VIDYA and P-Signal. Five-axis distinction against all three: mechanism differs (a displaced average-high/average-low band state machine, a CMO-adaptive recursive average, and an error-function dead-band over a standardized price change, versus a volatility-normalized 1-bar close-change sign test), signal construction differs (band flip / sign-of-change-of-an-adaptive-average / erf threshold crossing versus a strict inequality of a signed difference against a lagged ATR multiple — no crossover of two indicator series is involved anywhere in this rule), horizon coincides with the Gann HiLo record (`1d`) and differs from the two `1h` records, source identity differs in all three cases (FMZ strategy 430857 / `fmzquant/strategies` path above, versus FMZ 427070, FMZ 430552 and FMZ 440338), and material data dependency does not differ (all are OHLCV-only). Direction (two-sided) coincides with Gann HiLo and P-Signal but the dedup contract requires same source identity plus materially same normalized rule, which is not met. The two research PRs that were closed as NOT_LOSSLESS (#6, LazyBear Wave Trend `wt1`/`wt2` oscillator cross at 1h, and #10, golden/dead cross of two simple moving averages at 1d) are also distinct in source, in signal construction and in direction handling, and neither is on `main`.

## Economic mechanism

### Source-reported

The source states the mechanism only descriptively; it gives no behavioural, structural or risk-premium channel.

- Overview, as printed: "The momentum breakout strategy is based on the concept proposed by Richard Bookstaber in 1984 that once there is a big volatile movement, the market tends to follow it. Thus, it uses the ATR to measure volatility and issues orders when the current change in the closing price exceeds the threshold calculated by multiplying the ATR by a configurable constant."
- Strategy Logic, as printed: "The strategy first calculates the ATR indicator to measure market volatility. Then it calculates the absolute value of the daily closing price change. When the closing price change exceeds the ATR value by several multiples, trading signals are generated. Specifically, if the closing price rises more than the ATR upper rail, go long; if the closing price falls more than the ATR upper rail, go short." And: "The strategy uses the ATR indicator to dynamically determine the breakout threshold. When market volatility increases, the threshold will rise to reduce erroneous trades. When market volatility decreases, the threshold will decrease to capture breakout opportunities in a timely manner."
- Advantage Analysis, as printed: "Dynamic ATR stop loss can effectively control risks with adaptive stop loss based on market volatility"; "Using breakouts to generate trading signals can capture market trend rotations"; "Large parameter optimization space"; "The strategy logic is simple and clear, easy to understand and implement."
- Risk Analysis, as printed: "ATR indicator reacts slowly to sudden events, may miss the initial breakout"; "Imbalanced between long and short, works significantly better for one side only than for two-way trading"; "Strategy parameters are easy to overfit, actual results may be poor"; "Frequent trading, transaction costs may be high."
- Optimization Directions, as printed: add RSI/MACD trend filters; "add position management module to adjust positions based on market conditions"; optimize parameters per instrument; "combine machine learning techniques to auto-optimize parameters."
- Summary, as printed: "The momentum breakout strategy is simple and direct, generating trading signals from breakouts. ATR stop loss allows it to adapt to market volatility. The strategy relies on parameter optimization for decent results."

Three of those printed statements contradict the pinned code and are recorded in frontmatter `contradictions`: the two ATR stop-loss claims, the "absolute value" description, and the "ATR upper rail" price-level description.

### Research interpretation

Falsifiable mechanism hypothesis: on a single 24/7 crypto instrument, a one-bar change in close whose absolute magnitude exceeds twice the previous bar's average true range marks an atypically large information arrival, and such arrivals exhibit short-horizon directional persistence because order flow unwinds only partially within one daily bar; the rule therefore buys the positive tail and sells the negative tail of the volatility-standardized one-bar return distribution and holds the taken side until a standardized move of the opposite sign of equal size arrives. The bet is momentum continuation of a *standardized first difference*, not mean reversion and not a moving-average state: the threshold is expressed in ATR units, so the rule is scale-adaptive by construction, and the exit is not a level but the mirror-image event. Candidate behavioural channels are herding and stop cascades after a large move, and delayed liquidity replenishment in a market with no closing auction. This is a ported technical-analysis hypothesis: the source supplies the 1984 attribution but no behavioural argument, no sample and no evidence, so the mechanism is research interpretation, not source-reported fact.

Component roles, stated plainly because the source offers no composite structure:

- Primary signal: the sign of `Δclose[t] = close[t] − close[t−1]` gated by the strict inequality `|Δclose[t]| > 2 × ATR₁₄[t−1]` (implemented as two separate signed comparisons rather than an absolute value).
- Volatility normalizer: `ta.atr(14) × 2.0`, evaluated one bar stale (`atr[1]`).
- Trend / regime filter: none. The source lists RSI and MACD filters as future work.
- Risk / exit: none. The only exit is the opposite-direction entry (position reversal); stop loss, take profit, trailing stop and time exit are all absent while the source's own Advantage and Summary text advertises an ATR stop loss.
- Sizing: 100 percent of available equity per position, declared in the strategy declaration, i.e. full-equity concentration with no scaling rule.

No component is assumed to contribute alpha; ablation is required by the falsification plan.

## Signal

Everything below is read from the pinned Pine block. Nothing in this section is `research-proposed`.

**Formation timestamp and tradability**

- Decision series: completed `1d` bars of the pinned instrument (the `period: 1d` value in the pinned backtest header).
- Inputs at decision bar `t`: `close[t]`, `close[t−1]` (through `ta.change`), and `high[t]`, `low[t]`, `close[t−1]` through `ta.atr` → `ta.tr`. `open` is never read by the trading logic and `volume` occurs 0 times in the whole artifact.
- Order timing: the only two order calls are `strategy.entry` market orders, and the declaration sets `process_orders_on_close=true`. Official first-party documentation states that when this parameter is true the broker emulator processes orders "on the closing tick of each bar", and the reference adds "If the orders are market orders, the broker emulator executes them before the next bar's open." This is exactly a completed-bar decision with same-bar-close execution; there is no next-bar-open fill anywhere in the rule.
- Recalculation: neither `calc_on_every_tick` nor `calc_on_order_fills` appears in the pinned declaration (0 occurrences of each). Official documentation states both default to `false` and that `calc_on_every_tick` "does not affect the strategy's executions on historical bars". Recorded as source-declared-by-language-default, not as a research-proposed choice; it also means no intrabar re-evaluation can create a second order on the same bar.
- Timezone: no time value reaches an order. The artifact contains no `timestamp(`, no `time >=` comparison, no date input and no `timenow` (0 occurrences of each); the single standalone `time` token in the artifact sits in the prose phrase "in a timely manner". Timezone conventions are therefore immaterial to the trades, and the inert-date-input problem that affects sibling records does not arise here because there is no date control at all.

**Lookback, formulas and warmup**

- Parameters as declared: `var averageLength = input.int(14, "Average length", 2)` → `defval` 14, `minval` 2; `var multiplier = input.float(2.0, "Multiplier", 0.0, step=0.1)` → `defval` 2.0, `minval` 0.0, `step` 0.1. The official `input.int` / `input.float` signatures are `(defval, title, minval, maxval, step, ...)`, so the positional arguments above are read in that order; the artifact's `Strategy Arguments` table and the landing form both print 14 and 2, i.e. no override. Both inputs carry `var`; official documentation: when the `var` keyword is used "the variable is only initialized once, on the first bar if the declaration is in the global scope", and because an input is `const` this changes no value on any bar.
- `atr = ta.atr(averageLength) * multiplier`, i.e. `ta.atr(14) × 2.0`.
  - Official: "Function atr (average true range) returns the RMA of true range. True range is max(high - low, abs(high - close[1]), abs(low - close[1]))", and the same entry's example computes it as `ta.rma(trueRange, length)` with a `na(high[1]) ? high-low : …` guard, plus the remark that `ta.atr uses ta.tr(true)`. The `ta.tr` entry states: "if true, and previous day's close is NaN then tr would be calculated as current day high-low", so `tr[0] = high[0] − low[0]` and the true-range series is defined from bar index 0.
  - Official `ta.rma` example (the reference's own "the same on pine" block): `sum := na(sum[1]) ? ta.sma(src, length) : alpha * src + (1 - alpha) * nz(sum[1])`, i.e. the recursion is seeded with `ta.sma(src, length)`, and the `ta.rma` / `ta.atr` remarks both state "the function calculates on the length quantity of non-na values". The two statements agree, so the first defined `ta.atr(14)` value is bar index 13, and `atr[1]` is first defined at bar index 14.
- `closingChange = ta.change(close, 1)`: official, "Compares the current source value to its value length bars ago and returns the difference", so `closingChange[t] = close[t] − close[t−1]`, `na` at index 0 and defined from index 1.
- `atrPenetration(int signal)` is declared as a single statement `res = closingChange * signal > atr[1]`. Official user-defined-function rule: "A function's returned value is that of the last value in the function's body", and the multi-line syntax permits a trailing variable declaration, so the function returns that boolean.
- Derived conditions, exact:
  - `longCondition[t] ⇔ (close[t] − close[t−1]) > atr[t−1]` with `atr[t−1] = 2.0 × ATR₁₄[t−1]`.
  - `shortCondition[t] ⇔ −(close[t] − close[t−1]) > atr[t−1]`.
- Warmup, derived from the pinned code and official documentation because the source declares none: `atr[1]` first exists at bar index 14, `closingChange` first exists at index 1, and a boolean that is `na` cannot open an order (official v5→v6 migration guide: in v5 a value that must be boolean is evaluated so that `na` "is evaluated as false"; the same guide documents that a `when` condition must be `true` for an order to be created, and here the condition sits in an `if`). Therefore **bar index 14, the close of the 15th completed 1d bar, is the earliest possible entry**, and an exit can occur only after an entry. `max_bars_back` is not declared; official documentation states the required history buffer is detected automatically, and the rule references exactly one lag.
- Order of strategy calls within a bar: the long `if` block precedes the short `if` block, but the two conditions are mutually exclusive by construction — with `multiplier ≥ 0` the threshold `atr[1] ≥ 0`, so `Δclose > atr[1]` and `−Δclose > atr[1]` cannot hold together (at `multiplier = 0` they reduce to `Δclose > 0` and `Δclose < 0`, still exclusive). At most one order is created per bar and conflict priority is provably irrelevant.

**Entry**

- Long entry: `if (longCondition) strategy.entry(strategy.direction.long, strategy.long)`.
- Short entry: `if (shortCondition) strategy.entry(strategy.direction.short, strategy.short)`.
- The first argument of `strategy.entry` is the order id, and `strategy.direction.long` / `strategy.direction.short` are documented in the v5 reference as constants of `TYPE const string` ("It allows strategy to open only long positions" / "… only short positions"), so the ids are plain strings supplied by a language constant. Their literal values cannot affect trades here: the rule contains 0 `strategy.close`, 0 `strategy.close_all`, 0 `strategy.cancel`, 0 `strategy.exit` and 0 `strategy.order` calls, i.e. no id-scoped command exists to address them.
- Both statements omit `qty`. Official reference: `qty` "The default is na, which means that the command uses the default_qty_type and default_qty_value parameters of the strategy declaration statement to determine the quantity" — here `strategy.percent_of_equity` with value `100`.
- Both statements omit `limit` and `stop`; official reference: `limit`/`stop` "The default is na, which means the resulting order is not of the limit or stop-limit type", so both are market orders.
- Direction: both sides explicit (one `strategy.entry` per side, `strategy.long` once and `strategy.short` once). Neither side is disabled, and no third state is possible after the first signal other than the initial flat state.

**Exit**

- The pinned code contains exactly two order calls, both `strategy.entry`. Censuses over the whole 6779-byte artifact: `strategy.close` 0, `strategy.close_all` 0, `strategy.exit` 0, `strategy.order` 0, `strategy.cancel` 0, `strategy.cancel_all` 0, `strategy.risk.*` 0, `limit =` 0, `stop =` 0.
- Therefore the only exit is the opposite-direction `strategy.entry`. Official documentation for `strategy.entry` states: "By default, when a strategy executes an order from this command in the opposite direction of the current market position, it reverses that position", with the worked example that a short order of 5 shares against an open long of 5 shares "triggers the sale of 10 shares to close the long position and open a new five-share short position". The same single same-bar-close fill performs the close and the new open.
- Stop loss: none. Take profit: none. Trailing stop: none. Time limit or maximum holding period: none. Flat state: reachable only before the first entry signal; after that the system is always long or short until an opposite standardized move occurs. This directly contradicts the source's own ATR stop-loss claims (contradiction 1).

**Holding period, overlap and re-entry**

- Holding period: unbounded and determined entirely by waiting for an opposite standardized 2×ATR move; the source states no maximum or expected holding period.
- Maximum same-side concurrency: 1. `pyramiding` is not written in the declaration, so the value comes from the language default, and both official statements of that default describe the same observable rule even though they print different numbers: the v5 reference states "The maximum number of entries allowed in the same direction. If the value is 0, only one entry order in the same direction can be opened, and additional entry orders are rejected … The default is 0", while the v5 Strategies page states "The default value is 1, meaning the strategy can open new positions but cannot add to them using orders from strategy.entry() calls." Under each document's own definition of the parameter the result is identical — one open same-side entry, further same-side entries rejected — so the record records `pyramiding` as source-declared-by-language-default with that convergence stated rather than silently picking one number, and F3 forces the executing engine to confirm it.
- Same-direction re-entry: unreachable without an intermediate opposite-side order, because a same-side `strategy.entry` while the position is open is rejected under the default documented above, and orders fill on the same bar they are created (`process_orders_on_close=true`), so no unfilled same-id order survives into the next bar to be modified.
- Cooldown: none declared, and Pine's v5 strategy declaration exposes no cooldown field. Because a fresh entry requires a fresh `longCondition`/`shortCondition` event, and while a position is open only the opposite event can act, cooldown semantics are provably irrelevant rather than missing. The engine's separate "Order execution delay" setting is a user override whose default is 0 ticks, i.e. no delay.

**Parameters, sizing and pyramiding**

- Declared verbatim in the pinned declaration: `strategy("Volatility System", overlay=false, margin_long=0, margin_short=0, default_qty_type=strategy.percent_of_equity, default_qty_value=100, process_orders_on_close=true, initial_capital=20000)`. So the code-declared values are `overlay=false` (display only), `margin_long=0`, `margin_short=0`, `default_qty_type=strategy.percent_of_equity`, `default_qty_value=100`, `process_orders_on_close=true`, `initial_capital=20000`.
- Declaration parameters the code leaves unset, each recorded as source-declared-by-language-default with the official page that documents it: `default_qty_type`/`default_qty_value` are set (above), `currency=currency.NONE` ("in which case the chart's currency is used"), `slippage=0`, `commission_type=strategy.commission.percent` with `commission_value=0`, `pyramiding` (default discussed above), `calc_on_order_fills=false`, `calc_on_every_tick=false`, `close_entries_rule="FIFO"` (irrelevant: no id-scoped close command exists), `max_bars_back` auto-detected, `backtest_fill_limits_assumption=0` (no price-dependent orders exist) and `use_bar_magnifier=false` (no lower-timeframe fill data is used despite `basePeriod: 1h`).
- Sizing: `strategy.percent_of_equity` with value 100, i.e. each entry is 100 percent of available equity — declared in the code, therefore explicit, compounding, and equity-dependent. This is the single most consequential sizing fact in the record: the position is always the whole equity base, with no cash buffer and no scaling rule.
- Leverage and margin: `margin_long=0` and `margin_short=0` are written in the code, so no documented-default conflict applies; the v5 reference explains a default of 0 means "the strategy does not enforce any limits on position size". With equity-percentage sizing the exposure is bounded at 100 percent of equity regardless, so the rule has no leverage-dependent element.
- Two official pages disagree on the printed `pyramiding` default (0 versus 1) and on the printed `margin_long`/`margin_short` defaults (0 versus 100, the latter being a v6 change). The margin conflict is immaterial here because both values are code-declared; the pyramiding conflict is recorded above with its behavioral convergence and gated by F3.
- Direction: both sides explicit (see Entry). Spot is not applicable to the short leg, so the declared market type is perpetual (see Required data).
- Nothing else is declared: `currency`, `slippage`, `commission_*`, `pyramiding`, `close_entries_rule`, `calc_*`, `max_bars_back` and `use_bar_magnifier` all occur 0 times in the artifact.

**Reconstruction status**

Every field required to replay the rule — indicator variant and its parameters, source prices, lookback, smoothing, thresholds, comparison logic, direction, entry, exit, risk semantics, sizing, pyramiding, concurrency, cooldown, timeframe, fill timing and warmup — is explicit either in the pinned source or in official first-party documentation of the pinned source's own language defaults and functions. The residual `underspecified` items are the exact quote currency of the account under `currency.NONE`, the precise Binance contract (perpetual versus dated future), and the cost/latency/fill-failure model; none of them alters the signal, and all three are recorded as `data gap` rather than filled.

## Required data

- Instrument: BTCUSDT on Binance USDT-margined futures, taken verbatim from the pinned header `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`. Single pair, single instrument, no basket, no ranking, no cross-sectional step.
- Market type: perpetual. The source explicitly runs on a margined futures venue and the rule shorts, so a margined long/short instrument is required. The artifact does not distinguish the perpetual from a dated future, which is `data gap`; it is immaterial to an OHLCV-only signal but must be pinned before any execution work.
- Spot applicability: not applicable to the short leg, because spot would require naked shorting. The long leg alone could run on spot, but that would be a modified strategy and is not proposed.
- Venue: Binance only. No cross-venue state, no venue-selection rule, no listing or survivorship rule (the artifact states none).
- Timeframe: exactly one decision timeframe, `1d`, from `period: 1d`. The same header prints `basePeriod: 1h`; the pinned script contains 0 `request.*` calls and 0 `security(` calls, so no lower- or higher-timeframe series is referenced by the rule and there is no multi-timeframe dependency to align. The `1h` field is an FMZ backtester data field, not a rule input, and `use_bar_magnifier` is at its documented `false` default, so no lower-timeframe data is used for fills either.
- Fields used: `high[t]`, `low[t]`, `close[t]` and `close[t−1]`. `open` is not read by the trading logic and `volume` occurs 0 times in the whole artifact (the two `plot()` calls render `atr` and `math.abs(closingChange)` only).
- Fields not required and not used, each absent from the pinned artifact: open interest, funding, mark or index price, basis, order book or depth, trade or aggressor feed, liquidation feed, on-chain data, options or Greeks, sentiment or news, macro series, cross-venue state, borrow data, margin state, and the calendar (no time gate exists).
- Point-in-time: every input at bar `t` is contemporaneous (`close[t]`, `high[t]`, `low[t]`) or lagged (`close[t−1]` through `ta.change`, `tr[t−1]` through `atr[1]`); there is no future reference, no negative shift, no future extrema, no full-sample normalization, no `timenow` (0 occurrences), and no `security` call of any kind, so the pinned rule contains no look-ahead leakage. The `plot()` calls use no displacement offset.
- Timestamp and timezone: bar open times of a 1-day BTCUSDT series; because the rule compares no timestamps, no boundary convention affects trades.
- Missing data: no gap, halt or stale-bar handling is specified anywhere in the source → `data gap`. Imputation would be `research-proposed` and is not proposed here. The `na` rules that do matter are the language ones: `ta.change` is `na` on bar 0, `ta.atr` is `na` until index 13, and a boolean `na` evaluates to `false` in v5 — these are what fix the warmup at bar index 14.
- Funding, fee and spread needs: none specified. Word-boundary census of the pinned 6779-byte artifact gives commission 0, slippage 0, fee 0, funding 0, leverage 0, spread 0, capacity 0, turnover 0, roi 0, equity 1 (the `percent_of_equity` token), margin 2 (the two declared `margin_* = 0` values). Commission 0 and slippage 0 come from language defaults, not from measurement; spread, impact, latency and funding are `data gap`, never a modeled zero.

## Execution assumptions

Source-declared (quoted or read from the pinned declaration, the pinned code, or official first-party documentation of that same language):

- Order type: market orders, created only by `strategy.entry`. There is no limit order, no stop order, no stop-limit, no OCA group and no conditional price order anywhere in the rule (0 `strategy.exit`, 0 `strategy.order`, 0 `limit`/`stop` arguments), so there is no intrabar-path dependence and no maker/taker asymmetry to model. The broker emulator's documented intrabar assumptions are never exercised, because they apply only to price-dependent orders.
- Fill model: `process_orders_on_close=true` → official documentation: orders are processed "on the closing tick of each bar", and for market orders "the broker emulator executes them before the next bar's open". `calc_on_every_tick` and `calc_on_order_fills` default to `false`, so there is exactly one evaluation per completed bar. Completed-bar decision with same-bar-close execution.
- Signal-to-order delay: none. The order is created and filled on the same completed-bar close; the engine's "Order execution delay" override defaults to 0 ticks.
- Reversal semantics: an opposite-direction `strategy.entry` reverses the whole open position in one fill at the decision bar's close, per the official `strategy.entry` documentation quoted under Exit; the same fill closes the old side and opens the new side at the new order's size (100 percent of equity).
- Position limits: one position at a time, 100 percent of available equity per position, no same-side add-on (default `pyramiding`, convergence recorded above), no scaling, no grid, no martingale, no hedge.
- Leverage and margin: code-declared `margin_long=0` / `margin_short=0` → no position-size limit and no margin call; sizing is equity-percentage, so the rule never sizes by leverage and has no leverage-dependent edge.
- Shorting and borrow: the source assumes a margined futures venue. Borrow availability and any stock-loan analogue are not addressed → `data gap`, and spot shorting is explicitly out of scope.
- Costs: commission type defaults to `strategy.commission.percent` with `commission_value` default 0, i.e. 0 percent of order cash volume charged on the entry fill and again on the reversing fill; `slippage` defaults to 0 ticks per the official reference. No spread, no market-impact and no funding model appears anywhere in the artifact → the remaining cost legs are `data gap`; this record does not adopt a validated zero-cost assumption beyond the documented defaults, and the source's own Risk Analysis warns that "transaction costs may be high" while its pinned configuration charges none.
- Latency: not modeled in source → `data gap`.
- Participation and capacity: not modeled in source → `data gap`; tested by the research-defined gate F10.
- Failure handling (partial fills, rejects, downtime): not addressed in source → `data gap`. The pinned rule places whole market orders only, and no partial-fill-dependent condition exists.
- Engine-settings overrides a chart user could apply (initial capital, currency, pyramiding, commission, margin, order size, order execution delay) are not part of the pinned source; the code-declared values plus documented defaults above are the recorded strategy.
- Scout-vs-source split: every item above marked source-declared comes from the pinned declaration, the pinned code, or official TradingView documentation of that language. Nothing in this section is a Scout-added execution rule; every pass/fail cutoff used later is labeled `research-defined`.

## Evidence

### Source-reported

The artifact prints no performance result of any kind. Word-boundary census over the pinned 6779-byte artifact: sharpe 0, drawdown 0, cagr 0, return 0, win rate 0, annualized 0, roi 0, net profit 0, max drawdown 0, profit factor 0, strategy tester 0, open interest 0, commission 0, slippage 0, fee 0, funding 0, leverage 0, spread 0, capacity 0, turnover 0, cooldown 0, pyramiding 0, take profit 0, trailing 0; `margin` occurs twice, both inside the declaration; `equity` occurs once, inside `percent_of_equity`; `profit` occurs once, in the prose sentence "stable profits in complex markets"; `trades` occurs twice, in "erroneous trades" and "wrong trades"; `stop loss` occurs three times, all three in prose (contradiction 1); `backtest` occurs once, inside the `/*backtest ...*/` header; the standalone `time` token occurs once, in "in a timely manner". There is no equity curve, no trade list, no table and no figure anywhere in the artifact, and the landing page shows none either (its own metric-word counts are all 0, listed in Provenance).

What the source does report:

- Configuration only, from the pinned header: backtest start 2022-10-26 00:00:00, end 2023-11-01 00:00:00, `period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`.
- Parameter values as listed under Signal, plus the two exposed Strategy parameters (`Average length` 14, `Multiplier` 2) confirmed in the artifact's `Strategy Arguments` table and on the public landing form.
- Qualitative claims, verbatim, with no sample, no metric, no baseline and no figure: "once there is a big volatile movement, the market tends to follow it", "Dynamic ATR stop loss can effectively control risks", "The strategy relies on parameter optimization for decent results", and the Advantage/Risk items quoted under Economic mechanism — unverifiable as printed and recorded as bare claims, not as evidence.
- Landing metadata read 2026-10-05: Created 2023-11-02 15:12:46, Last modified "3 years ago", Copy 3, Hits 1044, no comment block rendered.
- Research-computed, not printed: the header window runs from 2022-10-26 00:00:00 to 2023-11-01 00:00:00, an elapsed span of 371 days, i.e. 372 inclusive daily bars on a 24/7 market when both endpoint days are counted; this is our arithmetic on the printed dates and must not be read as a source-reported sample size.
- Research-computed, not printed: under the pinned defaults the entry inequality is `|Δclose| > 2 × ATR₁₄` of the previous bar, so the rule is a strict-inequality test whose trigger rate is set by realized volatility, not by any fixed price distance.

No source-reported figure in this record comes from any other paper, article or repository; every claim is attributed to the single pinned artifact above.

### Independently reproduced

not independently reproduced

Only the following were performed: SHA-256 checksumming of the pinned artifact, of its Pine block and of a whitespace-normalized variant; a byte-identical re-fetch of the file blob by its id from the GitHub tree and blob APIs; extraction, unescaping and byte-for-byte comparison of the FMZ landing page's embedded Pine payload against the pinned Pine block; a whole-artifact term and word-boundary census; enumeration of `strategy.*`, `input*` and `plot*` call sites and of identifier occurrence counts; reading of the public FMZ landing page; and live reading of the official TradingView pages cited under Sources. No market data was downloaded, no backtest was run, no Pine or third-party code was executed, and no statistic was recomputed from data.

### Negative evidence

1. The artifact prints zero performance numbers, so there is nothing to reproduce: sharpe, drawdown, cagr, return, win rate, annualized, roi and trade counts are all 0 occurrences, and the landing page shows no performance block either.
2. The performance-sounding prose claims carry no sample, no metric and no baseline, so they cannot be checked as printed.
3. The only configured backtest window is 372 daily bars (2022-10-26 00:00:00 to 2023-11-01 00:00:00) on a single instrument, with no train/test split, no out-of-sample section and no walk-forward.
4. Cost model is zero: commission 0 percent and slippage 0 ticks come from language defaults, with no spread, impact or funding model, while the source's own Risk Analysis warns that transaction costs may be high — so any edge claim is unpriced by the source.
5. Sizing is 100 percent of available equity on every position: full-equity concentration, no cash buffer, no volatility targeting, no risk layer of any kind (no stop, no take profit, no time exit, no drawdown control).
6. The strategy contains no stop loss, no take profit, no trailing stop and no time exit, while the source's Advantage and Summary advertise an ATR stop loss (recorded contradiction 1) — the published rule is materially different from the description a reader would take away, and a losing position is held until the opposite 2×ATR event.
7. Holding is unbounded: with no time exit and no level exit, exposure persists indefinitely until an opposite standardized move of the same size arrives.
8. After the first signal the system is long or short, never flat by rule; there is no cash-fallback state and no regime gate.
9. Prose claims the rule uses the absolute value of the close change; the code uses the signed change and tests each direction separately, with `math.abs` confined to a plot (recorded contradiction 2).
10. Prose describes an "ATR upper rail" price level for both directions; no price level exists in the rule, which compares a difference against a lagged ATR multiple (recorded contradiction 3).
11. The threshold uses `atr[1]`, the previous bar's ATR, so the volatility estimate is one bar stale, while the prose implies a current-threshold calculation.
12. The 1984 Richard Bookstaber attribution is asserted in prose and cannot be verified from the artifact; no citation, edition or page is given.
13. Authorship is layered and unverified: the mirror records `Author: ChaoZhang`, the code prints `// © EduardoMattje`, the published title names Richard Bookstaber, and none of these identities is independently confirmed; peer-review status is not stated in source.
14. `pyramiding` is not written in the code; it is recoverable only from official documentation, and two official pages print different default numbers (0 versus 1) even though both describe the same observable behavior — recorded rather than silently chosen, and gated by F3.
15. Commission, slippage, currency, the calculation flags and the close rule are all language defaults rather than code declarations; a consumer that assumes different defaults would misprice or retime every trade.
16. `margin_long=0` / `margin_short=0` mean no position-size limit and no margin call in the pinned manual; the current manual prints 100 for these values as a v6 change, but because the code declares both explicitly there is no unresolved choice here — only the target engine's reading has to be confirmed (F3).
17. The `multiplier` input allows `0.0`; at the pinned default 2.0 the rule is fully deterministic, but a user override of 0 would reduce the test to the sign of the one-bar change and would generate a far denser signal — the record freezes the default.
18. The source has no volume, liquidity, spread or regime filter despite its own Optimization section proposing trend filters, so the rule is presented as a bare single-statistic template.
19. Tail risk is structural: a full-equity position with no stop absorbs the entire adverse move until the opposite 2×ATR event, and the source itself concedes the ATR "reacts slowly to sudden events, may miss the initial breakout".
20. The full source is behind a login on the FMZ landing page and is publicly reachable only through a third-party mirror repository, leaving a single point of provenance (the landing's embedded payload corroborates it byte for byte but is neither immutable nor versioned).
21. The mirror repository ships no LICENSE file, so the redistribution status of the mirror as a whole is not stated in source; only the script's own MPL-2.0 notice is printed inside the block.
22. There is no repository, no version tag, no test suite, no issue tracker and no changelog for the rule; the FMZ landing shows a relative modification label that cannot be reconciled with its creation timestamp from the page alone.
23. FMZ landing statistics (Copy 3, Hits 1044, no comment block, as read 2026-10-05) show limited community adoption, and no third-party study of this exact artifact was identified.
24. The base-K-line field `basePeriod: 1h` sits next to a `1d` decision period; although the script contains no `request.*` call and therefore no cross-timeframe dependency, a reader could mistake the header for a multi-timeframe design.
25. No independent replication, no competing study and no contrary external evidence specific to this artifact was found; absence of contrary literature is not evidence of robustness.
26. Distributional fragility: the signal is the sign of a one-bar difference divided implicitly by a lagged average true range, so it is a single-observation statistic with no smoothing on the numerator — in a volatility-clustering window the sign can flip on noise, producing reversal churn that pays the full spread on both legs while the source's own commission is zero.
27. Warmup documentation was audited rather than assumed: the `ta.atr` entry of the same first-party manual gives both a seeding example (`na(high[1]) ? high-low : …` then `ta.rma(trueRange, length)`) and the remark "calculates on the length quantity of non-na values", and the `ta.rma` example seeds with `ta.sma(src, length)` — the two statements agree, which is what pins the first `atr[1]` at index 14. The sibling `ta.ema` entry of the same manual states a different seeding in its own example, but this rule never calls `ta.ema`, so that divergence cannot reach this record.

## Falsification plan

All thresholds below are `research-defined falsification threshold` values chosen by this Scout; none of them is source-reported. All test inputs (data vendor, sample window, benchmark definitions, cost model) are `research-proposed` test scaffolding and are not part of the strategy rule.

- **F1 — Semantic reconstruction gate.** Threshold: an independent reimplementation of the pinned rule must reproduce, on a reference OHLCV series, the identical `atr`, `closingChange`, `longCondition` and `shortCondition` series to floating-point tolerance and an identical ordered list of entry bars and sides, including the first possible entry at bar index 14, `ta.tr` handling at bar 0 (`high − low`), the `ta.rma` seeding through `ta.sma(src, 14)`, the one-bar lag `atr[1]`, the two strictly signed comparisons, mutual exclusivity of the two conditions, and the same-side-entry rejection implied by the default `pyramiding`. Action: any mismatch means the record is not 1:1 reconstructible and must be withdrawn from admission review rather than repaired by interpretation.
- **F2 — Causality and repaint audit.** Threshold: every input used at bar `t` must be dated at or before `t` (`close[t]`, `close[t−1]`, `high[t]`, `low[t]`, `tr[t−1]`), with zero occurrences of future bars, negative shifts, `timenow`, session recalculation, `calc_on_order_fills=true`, `calc_on_every_tick=true`, `use_bar_magnifier=true` or any lower-timeframe request. Action: any future reference or intrabar dependence found ⇒ NOT_LOSSLESS, close the record.
- **F3 — Engine-default audit gate.** Threshold (research-defined): the executing engine must confirm every recorded declaration and language default end to end — order size exactly 100 percent of available equity (`percent_of_equity` 100, compounding), fill price equal to the decision bar's close, 0 percent commission on both the entry and the reversing fill, 0 ticks slippage, once-per-bar evaluation, same-side entries rejected while a position is open, `margin_long`/`margin_short` 0 with no position-size cap and no liquidation, initial capital 20000 in the chart currency, `close_entries_rule="FIFO"`, and no order-execution delay. Action: fail if any recorded value differs from the record, or if `pyramiding` resolves to something other than "one open same-side entry, no adds"; fail ⇒ pin the discrepancy in writing and keep research-only, no adoption.
- **F4 — Cost ladder.** Threshold (research-defined): apply the declared 0 percent commission plus 0 / 1 / 2 / 5 / 10 bps per side and, for the perpetual, a funding accrual leg; fail if net annualized return turns non-positive at 2 bps per side or net Sharpe falls to 0 or below at 5 bps per side. Action: fail ⇒ the edge is cost-dependent, record remains research-only and must not be proposed for any adoption.
- **F5 — Parameter perturbation.** Threshold (research-defined): sweep `multiplier` over 1.0, 1.5, 2.0, 2.5, 3.0 and `averageLength` over 7, 14, 21, 28, 55 with everything else frozen; fail if the sign of net return over the full sample flips for the published cell (14, 2.0) or if fewer than half of the 25 cells produce positive net return. Action: fail ⇒ parameter-lottery diagnosis, no adoption.
- **F6 — Regime breakdown.** Threshold (research-defined): split the sample into thirds by trailing 60-day realized volatility and, separately, by a 60-day ADX(14) trend-strength tercile; fail if net Sharpe is negative in at least two of three terciles in either split. Action: fail ⇒ the rule requires a regime gate that the source does not contain, so it cannot be admitted as-is and must stay research-only.
- **F7 — Placebo.** Threshold (research-defined): compare against buy-and-hold BTCUSDT on the identical window and against 1000 random side-assignment sequences that preserve the observed holding-time distribution; fail if the observed net Sharpe does not exceed the 95th percentile of the placebo distribution. Action: fail ⇒ no evidence that the breakout timing carries information.
- **F8 — Out-of-sample requirement.** Threshold (research-defined): at least 5 years of 1d BTCUSDT bars with a frozen chronological split and no re-tuning; fail if out-of-sample net Sharpe is 0 or below. Action: fail ⇒ reject for adoption; do not rescue by re-tuning.
- **F9 — Cross-instrument generalization.** Threshold (research-defined): run the identical frozen rule on ETHUSDT perpetual and on one further major perpetual chosen before inspection; fail if 0 of 2 produce positive net return after costs at 2 bps per side. Action: fail ⇒ single-asset overfit diagnosis.
- **F10 — Capacity and liquidity.** Threshold (research-defined): fail if the required notional (100 percent of equity) exceeds 5 percent of the trailing 30-day median daily volume of the instrument. Action: fail ⇒ capacity-capped, record the ceiling and block any size scaling (sizing is fixed at full equity, so scaling would already be a rule change).
- **F11 — Multiplicity control.** Threshold (research-defined): apply Benjamini-Hochberg at q = 0.10 across the full F5 × F9 cell family; fail if the published cell does not survive. Action: fail ⇒ treat the published configuration as one draw among many, no adoption.
- **F12 — Risk-layer ablation.** Threshold (research-defined): because the source contains no stop, take-profit or time exit while advertising one, measure maximum drawdown and the longest single holding period; fail if maximum drawdown exceeds 40 percent on the frozen sample or if any single holding exceeds 180 daily bars. Action: fail ⇒ document the unbounded-exposure failure and keep research-only.
- **F13 — Frozen forward window.** Threshold (research-defined): forward test from 2026-10-05 to 2027-10-04 with every parameter frozen; fail if forward net Sharpe at 2 bps per side is 0 or below. Action: fail ⇒ reject; no parameter may be changed to re-run it.

Global no-retuning rule: `averageLength 14`, `multiplier 2.0`, the lagged threshold `2 × ATR₁₄[t−1]`, the two strictly signed one-bar-change comparisons, the reversal-only exit, no stop/take-profit/time exit, `pyramiding` at its documented default (one open same-side entry), `percent_of_equity 100` compounding sizing, `process_orders_on_close` same-bar-close fills, 0 percent commission and 0 ticks slippage, initial capital 20000, the single `1d` timeframe and the BTCUSDT perpetual instrument are frozen. No gate may be rescued by changing a parameter, widening a window, switching vendor, dropping a cost leg or re-defining a metric after seeing results.

## Crypto portability

`direct` — with a narrow meaning. The cited source itself configures the rule on Binance USDT-margined BTCUSDT futures at `period: 1d`, so the instrument, venue and market type are already crypto and no porting change is required to express the rule. `direct` refers only to mechanism, signal and instrument applicability; it is explicitly not a claim of crypto performance, which is `unproven` because the artifact prints no result.

Portability-relevant facts:

- The rule consumes only `high`, `low` and `close` of daily bars (with `close[t−1]`), all available on any 24/7 crypto venue; there is no session, holiday or opening-auction dependency, and no calendar gate exists to interact with the 24/7 clock.
- No funding, open interest, mark or index price, liquidation feed, order book, aggressor side, on-chain data or options input is used, so none of those crypto-specific inputs can invalidate the signal — although funding accrual is also absent from the cost model, which for a strategy that can hold a perpetual position indefinitely is a real carry cost (`data gap`).
- Shorting requires a margined instrument; the source already uses a futures venue, so the perpetual is the natural target and spot is out of scope for the short leg.
- Risks that remain crypto-specific and unmodeled by the source: perpetual funding accrual (never mentioned, `data gap`), the choice of mark versus last price for valuation (`data gap`), contract specification and tick-size differences between venues (`data gap`), listing and delisting churn for anything other than BTCUSDT (`data gap`), venue fragmentation and custody risk (`data gap`), and liquidity or market-impact differences for a full-equity order (`data gap`).
- Timestamps are exchange-defined UTC daily candles on Binance; because no rule element compares timestamps, the record does not depend on any boundary convention.

Crypto portability is not authorization to trade and not evidence that the mechanism survives in crypto.

## Limitations

- `not independently reproduced`. Nothing in this record has been recomputed from data.
- `data gap`: no spread, impact, latency, funding or fill-failure model; no missing-data handling; no capacity statement; no account-currency pin; no performance output.
- `underspecified`: the exact Binance contract (perpetual versus dated future); the quote currency resolved by `currency.NONE`; whether the FMZ backtest engine's `basePeriod: 1h` field influenced any published number (the script itself makes no cross-timeframe call).
- `unproven`: profitability, robustness, regime robustness, cross-instrument robustness, capacity and forward performance.
- Source-quality limitation: a single community mirror entry with no repository, no tests, no versioning, no peer review and three layered, unverified identities; the landing hides the full source behind a login.
- Reproducibility limitation: because FMZ hides the full source and prints no results, the only immutable, publicly auditable artifact is the mirror at the pinned SHA; the landing's embedded payload corroborates it byte for byte but is neither immutable nor versioned.
- Identification limitation: the rule is a single-observation sign test normalized by one lagged volatility number, with no control for trend, volume, spread or funding regime, so nothing in the source separates a breakout effect from beta, from cost-amplified reversal churn or from a volatility-regime artifact.
- Risk limitation: full-equity sizing with no stop, no take profit and no time exit means the record describes an unhedged always-in-market system after the first signal, which the source's own marketing text does not convey.
- Publication-bias limitation: a public strategy mirror selects for presentable, not for robust, and Copy 3 suggests limited demonstrated community reuse.
- Incremental-write check: this is the first record in the repository for this source identity after the 2026-10-04 pool reset, no open research PR shares it, and no Wiki Brain page exists for it, so this is not ordinary duplicate material.
- A three-item contradiction set is recorded in frontmatter. All three are prose-versus-code conflicts inside one artifact, and in every case the pinned code is the executable and unambiguous text, so none of them leaves the signal itself ambiguous; all three do leave a naive reader's mental model of the rule wrong — in particular the advertised ATR stop loss does not exist — which is why `contested: true` is set.
- Two additional conflicts live in the official documentation rather than in the source (the printed `pyramiding` default and the printed `margin_*` defaults) and are recorded under Signal instead of being resolved by preference; the margin one is neutralized by the code declaration, the pyramiding one is neutralized by the behavioral convergence of both statements and is gated by F3.

## Implementation status

`not-implemented`. Nothing has been implemented in our research stack. No Pine was executed, no backtester was run, no Hummingbot package or `dev-2.17.0` backtest was attempted, no Qlib job was created, no indicator was coded, and no Paper, Testnet or Live workflow was touched. The only artifacts produced by this run are this Markdown record and its verification script.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. Presence of this record does not mean: passed LOSSLESS HB_READY review; merged to `main`; entered Hermes Wiki Brain; entered any candidate pool; completed a Hummingbot or Qlib full backtest; became a survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for Paper; approved for Testnet; approved for Live. HB_READY itself, if it were ever granted, means semantic and backtest expressibility only. No record may promote itself by wording, evidence count, confidence or schedule behavior.

## Related Wiki records

No Wiki Brain page exists for this source identity, and this run writes none. The following existing pages were checked on disk and are related by mechanism family (volatility-normalized breakout and trend following, stop/ratchet design, momentum), by execution and cost discipline, or by overfitting control rather than by source identity; none of them shares the Bookstaber source, the signed one-bar-change-versus-lagged-ATR signal construction, or this exact BTCUSDT daily single-pair scope:

- [[quant/futures-volatility-normalized-tick-size-trend-following-filter-2026-09-02]]
- [[quant/crypto-perpetual-supertrend-wpr-trend-following-cost-gate-falsification-2026-09-12]]
- [[quant/crypto-fer-hurst-adx-regime-gated-amo-kama-momentum-source-code-audit-2026-09-14]]
- [[quant/forex-retail-execution-friction-wide-stop-ratchet-falsification-2026-09-13]]
- [[quant/crypto-adaptive-trailing-stop-volatility-filtered-cointegrated-pairs-trading-2026-09-07]]
- [[quant/btc-30m-wyckoff-squeeze-multilayer-trend-momentum-2026-09-14]]
- [[quant/crypto-walk-forward-window-optimization-double-oos-momentum-2026-09-04]]
- [[quant/backtest-overfitting-pbo-cscv-2026-08-27]]
- [[quant/alpha-research-contract-2026-08-28]]

## Sources

- https://github.com/fmzquant/strategies — pinned commit `7853bb2bf262c4567ac238d3552d97f0e50cb801`, path `理查德布克斯塔伯动量突破策略Richard-Bookstaber-Momentum-Breakout-Strategy.md`; the complete primary source read end to end on 2026-10-05, SHA-256 `b9831f78243eecddb66047418c466983dfd1413b86255b58b234ea32b28dcb48`; the same bytes were re-fetched from the GitHub blob API by blob id `6b23f46052ff2f2e28415450d1969b2e16304dea` (6779 bytes) and are byte-identical.
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E7%90%86%E6%9F%A5%E5%BE%B7%E5%B8%83%E5%85%8B%E6%96%AF%E5%A1%94%E4%BC%AF%E5%8A%A8%E9%87%8F%E7%AA%81%E7%A0%B4%E7%AD%96%E7%95%A5Richard-Bookstaber-Momentum-Breakout-Strategy.md — percent-encoded form of the same pinned file.
- https://www.fmz.com/strategy/430857 — FMZ landing page, read 2026-10-05; confirms title, badge, author account, creation timestamp, statistics, English description, backtest header, the two exposed parameters, the login gate, the absence of any performance block, and an embedded Pine payload that is byte-identical to the pinned Pine block.
- https://www.tradingview.com/pine-script-reference/v5/#fun_strategy — official first-party language reference used for declaration-parameter semantics and defaults (`pyramiding` 0 with its rejection rule, `default_qty_type` `strategy.percent_of_equity` as "a percentage of available equity", `default_qty_value`, `currency` `currency.NONE`, `slippage` 0, `commission_type` / `commission_value` defaults, `process_orders_on_close` default false, `close_entries_rule` "FIFO", `calc_on_order_fills` / `calc_on_every_tick` defaults false, `margin_long` / `margin_short` 0 meaning "does not enforce any limits on position size", `initial_capital`, `max_bars_back` auto-detection, `use_bar_magnifier` default false, `backtest_fill_limits_assumption` 0), and for the constants `strategy.direction.long` / `strategy.direction.short` (`const string`).
- https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}entry — official first-party documentation used for the `qty` default (`na`, i.e. the declaration's `default_qty_type`/`default_qty_value`), the `limit`/`stop` defaults (order is not of the limit or stop-limit type), market-order creation, pyramiding rejection of same-direction entries, and opposite-direction entries reversing the position.
- https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}atr , https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}rma , https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}tr , https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}change — official first-party documentation used for the ATR/RMA definition and its `ta.rma(trueRange, length)` example, the RMA seeding via `ta.sma(src, length)`, the "calculates on the length quantity of non-na values" remark, `ta.atr uses ta.tr(true)` with `handle_na` giving `high − low` on the first bar, and the one-bar change definition.
- https://www.tradingview.com/pine-script-docs/v5/concepts/strategies/ — official first-party documentation used for `process_orders_on_close = true` fill semantics ("the closing tick of each bar"), the once-per-bar execution rule when the calculation flags are false, the printed `pyramiding` default of 1 with "cannot add to them", and the Strategy Tester context.
- https://www.tradingview.com/pine-script-docs/v5/language/user-defined-functions/ — official first-party documentation used for "A function's returned value is that of the last value in the function's body" and the multi-line function syntax ending in a variable declaration.
- https://www.tradingview.com/pine-script-docs/v5/language/variable-declarations/ — official first-party documentation used for the `var` initialization rule ("the variable is only initialized once, on the first bar if the declaration is in the global scope").
- https://www.tradingview.com/pine-script-docs/migration-guides/to-pine-version-6/ — official first-party documentation used for the `when` parameter semantics ("An order is created only if the `when` condition is `true`") and for the v5 treatment of boolean `na` ("na is evaluated as false" when a boolean is required), together with the note that the `margin_long`/`margin_short` default of 100 is a v6 change.
