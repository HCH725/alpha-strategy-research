---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: VIDYA CMO-adaptive average slope trend system on BTCUSDT 1h bars
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
  - https://www.fmz.com/strategy/430552
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
  - https://www.tradingview.com/pine-script-docs/v5/concepts/strategies/
  - https://www.tradingview.com/pine-script-docs/v5/migration-guides/to-pine-version-5
  - https://www.tradingview.com/pine-script-docs/migration-guides/to-pine-version-6
  - https://www.tradingview.com/pine-script-docs/v5/language/script-structure/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The artifact's own Strategy Arguments table lists Start Time and End Time under a Date Range group and the pinned code carries the comment // Backtest Date Range Inputs //, but the pinned code assigns InDateRange = true unconditionally and never reads StartTime or EndTime, so both declared controls are inert and the strategy has no date filter."
  - "The prose states that VIDYA dynamically adjusts the weighting of an SMA based on CMO values, giving more weight to CMO early in trend changes and more weight to SMA once the trend is established, but the pinned recursion contains no SMA term after initialization and weights the current src against the previous VIDYA value with weight valpha*|vCMO|, which increases with momentum magnitude rather than with trend age."
  - "The pinned source prints the version directive as // @version=5 with a space after //, which is not the documented compiler-annotation form //@version=5; the official rule states that an omitted annotation defaults to version 1, so the printed directive is inert even though the code uses constructs that only exist in Pine v5."
---

# VIDYA CMO-adaptive average slope trend system on BTCUSDT 1h bars

## Provenance

Immutable GitHub source (this is the primary source actually read end to end):

- Repository URL: https://github.com/fmzquant/strategies
- Full commit SHA: `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit date 2025-04-30T03:10:28Z, i.e. 2025-04-30 11:10:28 +0800, subject `update`). The GitHub `commits/HEAD` API returned this same SHA on 2026-10-05, so it is still the repository head at research time.
- Exact file path: `动量趋势跟踪策略Momentum-Trend-Following-Strategy.md` (the non-ASCII filename is preserved verbatim; percent-encoded blob URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E5%8A%A8%E9%87%8F%E8%B6%8B%E5%8A%BF%E8%B7%9F%E8%B8%AA%E7%AD%96%E7%95%A5Momentum-Trend-Following-Strategy.md )
- Relevant source URL recorded inside the artifact: https://www.fmz.com/strategy/430552

Primary-source checksums pinned 2026-10-05 from a checkout of that exact commit:

- File 8079 bytes, SHA-256 `98c9e9f9f2e36210bd717b09a54e6726fd8e1982d5c024f3ff201a635832c1c9`, 6473 characters, 187 newlines, git blob `e10f3b8a2a788c250bcc23bbd4bd13fec2677666`.
- Whitespace-collapsed variant 5649 characters, SHA-256 `8e0822879b0113b4001034296fd05bfd77d86cff0bfe0f0d4f8fa70d246ed694`.
- The fenced Pine block alone: 43 lines (34 non-empty), 1726 bytes/characters, SHA-256 `49d6c33e5e4071a70ee40aebde1f28f376563095623ba4a3141d1bef5865bb59`.
- Independent byte-level confirmation: the GitHub Contents API at `?ref=7853bb2bf262c4567ac238d3552d97f0e50cb801` and the Git Blobs API for `e10f3b8a2a788c250bcc23bbd4bd13fec2677666` both returned 8079 bytes that are byte-for-byte identical to the local checkout, with the same SHA-256.

Artifact structure as printed: `> Name` (动量趋势跟踪策略Momentum-Trend-Following-Strategy), `> Author` = ChaoZhang, `> Strategy Description` (a Chinese section set and an English set inside one `[trans]` block, preceded by one FMZ-hosted PNG), `> Strategy Arguments` table, `> Source (PineScript)` fenced block preceded by an FMZ `/*backtest ...*/` header, `> Detail` = https://www.fmz.com/strategy/430552, `> Last Modified` = 2023-10-30 11:36:26.

Licence and rights: the pinned Pine block itself prints `// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/` and the author credit `// Author = TradeAutomation`. The mirror repository ships no LICENSE file, so the redistribution status of the mirror as a whole is not stated in source; this record therefore cites and normalizes the rule and reproduces no source code block.

FMZ landing page read directly in a browser session on 2026-10-05 (public, no login for the description layer): browser title `Momentum Trend Following Strategy | FMZ`, heading `Momentum Trend Following Strategy`, type `Common strategy`, author account `ChaoZhang` with 1822 followers, `Created: 2023-10-30 11:36:26`, `Last modified: 3 years ago`, `Copy: 1`, `Hits: 1118`, the English Overview / Strategy Logic / Advantage Analysis / Risk Analysis / Optimization Directions / Conclusion prose identical to the mirror's English block, `Comment` section showing `All comments (0)`, a `Source` pane printed as `Pine / UTF-8 / 307bytes / 50words / 12lines / Ln1,Col0` above the literal string `Login to view full source`, and the four exposed Strategy parameters (Start Time, End Time, VIDYA Length, VIDYA Price Source).

The landing page's server-rendered HTML payload nevertheless contains the complete Pine text: after extracting the `"source"` field and unescaping it, the payload yields 35 lines of which all 34 non-empty lines are equal, in order, to the 34 non-empty lines of the mirror's fenced Pine block. Consequence: the mirror and the landing page agree on the executable text, while the landing's own editor byte/line counter (307 bytes, 12 lines) disagrees with the 1726-byte, 43-line block embedded in the same page; the reason for that counter discrepancy is not stated in source and is recorded as printed, not repaired.

FMZ backtest header printed verbatim inside the pinned artifact:

```text
start: 2023-09-29 00:00:00
end: 2023-10-29 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
```

Version determination, stated because the printed directive is malformed: the artifact's line 145 is `// @version=5` (one space after `//`); a byte count over the whole file gives 0 occurrences of `//@version` and 1 occurrence of `// @version`. The official script-structure documentation gives the annotation form as `//@version=5` and states that when the annotation is omitted version 1 is assumed. The intended and only compiling version is nevertheless uniquely determined: the code uses `math.sum`, `math.abs` and `input.int`, which the official v4-to-v5 migration guide lists as constructs introduced in v5 (v4 had `sum()`, `abs()` and `input(…, type=input.integer)`), and it passes a `when` argument to `strategy.entry()` and `strategy.close()`, which the official v5-to-v6 migration guide lists as removed for v6. This record therefore treats the rule as Pine v5 semantics and records the malformed directive as a source defect rather than as an open semantic question.

Provenance gaps (stated, not repaired): no DOI, no version tag, no repository, no test suite, no issue tracker entry, no peer-review statement and no performance output anywhere; peer-review status is not stated in source.

Pre-write dedup (2026-10-05): a hidden-inclusive search (`rg -uuu`) of the whole working tree with the probe set `VIDYA`, `Variable Index Dynamic`, `Momentum[- ]Trend[- ]Following`, `430552`, `动量趋势跟踪`, `TradeAutomation` returned 0 matches, and the same probe set run against the fetched contents of both open research PRs (PR #6 `wave-trend-lazybear-wt1-wt2-cross-btcusdt-1h-2026-10-05.md`, 53963 bytes; PR #7 `p-signal-erf-dead-band-reversal-btcusdt-1h-2026-10-05.md`, 58610 bytes) also returned 0 matches. The positive control `Gann HiLo` returned the tracked record `gann-hilo-activator-state-flip-trend-btcusdt-daily-2026-10-05.md`, so the scan is effective. The loose probe `reversal` returned only that Gann record (execution prose about reversing sizing) and `.git` internals, with no source, signal or universe overlap. `git ls-remote origin 'research/*'` returned exactly three refs: the already-merged Gann branch, PR #6's `research/hermes-wave-trend-lazybear-20261005-0318` and PR #7's `research/hermes-p-signal-erf-reversal-20261005-0414`. The dedup set is therefore `main` (one record: Gann HiLo) plus those two open PRs.

Five-axis distinction against every member of that dedup set: source identity differs in all three cases (FMZ strategy 430552 / `fmzquant/strategies` path above, versus the Gann HiLo artifact, the LazyBear Wave Trend script and the Kharevsky P-Signal script); mechanism differs (volatility-and-momentum-adaptive average slope versus a displaced average-high/average-low band state machine, a stochastic-momentum oscillator overbought/oversold crossing, and a standardized first difference passed through an error-function dead band); signal construction differs (sign of the one-bar change of a recursive adaptive average versus a two-state band flip, an oscillator line crossing, and a threshold crossing on a normalized series); direction differs (this rule is long-only, the other three are two-sided); material data dependency does not differ (all are OHLCV-only). Universe (BTCUSDT) and horizon (1h) coincide with PR #6 and PR #7 but the dedup contract requires same source identity plus materially same normalized rule, which is not met.

## Economic mechanism

### Source-reported

The source states the mechanism only descriptively; it gives no behavioural, structural or risk-premium channel.

- Overview, as printed: "This strategy uses the VIDYA (Variable Index Dynamic Average) indicator to identify the trend direction in cryptocurrency markets and trades based on the trend. It is a quantitative technical trading strategy."
- Strategy Logic, as printed: VIDYA "is based on price momentum and can respond to trend changes faster. Specifically, it combines the Chande Momentum Oscillator (CMO) and Simple Moving Average (SMA). CMO measures the difference between upward and downward momentum to gauge trend strength. SMA smoothes price data. VIDYA dynamically adjusts the weighting of SMA based on CMO values, giving more weight to CMO early in trend changes and more weight to SMA once the trend is established." And: "After calculating VIDYA, the strategy judges the trend direction based on the curve of VIDYA. It goes long when VIDYA rises and closes position when VIDYA falls."
- Advantage Analysis, as printed: rapid response to trend change; combination of trend strength and trend direction "can effectively distinguish strong and weak trends, avoid being misled by false trends in ranging markets"; single-indicator simplicity with "No conflicting or misleading signals from multiple indicators"; longer settings track the main trend; "Good backtest results with positive expected returns."
- Risk Analysis, as printed: "VIDYA may lag in response to sudden market events and miss short-term trading opportunities"; "Long VIDYA settings make it less sensitive to short-term trend changes and can lead to larger drawdowns"; "Pure trend following performs poorly in choppy markets"; "Limited backtest data cannot fully verify robustness. Parameters need iterative optimization and testing in live trading"; "High volatility in crypto markets. Position sizing and stop loss should be carefully controlled for strict risk management."
- Optimization Directions, as printed: add volume or volatility indicators; combine VIDYA with other trend indicators; "Optimize stop loss strategy to exit early when trend reverses"; "Optimize position sizing dynamically based on market conditions"; "Test robustness across different cryptocurrencies and timeframes."
- Conclusion, as printed: the rule "provides a basic framework and approach for building crypto trend strategies, but prudent assessments are still needed for real-world applications."

Two of those printed statements contradict the pinned code and are recorded in frontmatter `contradictions`: the SMA-weighting claim (the recursion contains no SMA term after initialization) and the effective date-range controls (both declared inputs are inert).

### Research interpretation

Falsifiable mechanism hypothesis: short-horizon crypto returns exhibit directional persistence, and the sign of the one-bar change of an average whose smoothing speed is itself scaled by |9-bar CMO| marks the direction of the local drift with an adaptive lag: when momentum is strong the series tracks price closely and flips quickly, when momentum is weak it falls back toward its own previous value and behaves like a slow level. Holding only while that adaptive series is rising, and flatting the moment it falls, is a trend-persistence rule whose exposure is gated by a momentum-scaled responsiveness parameter rather than by a fixed lookback. Candidate behavioural or structural channels are slow diffusion of directional information in a 24/7 market with no closing auction, and herding or positioning feedback that keeps an adaptive average rising after a visible momentum expansion. This is a ported technical-analysis hypothesis: the source supplies no economic rationale and no evidence, so the mechanism is research interpretation, not source-reported fact.

Component roles, stated plainly because the source offers no composite structure:

- Regime / trend state: the recursive VIDYA series, seeded by `ta.sma(src, 50)` and thereafter updated with a momentum-scaled weight.
- Primary signal: the sign of `VIDYA[t] - VIDYA[t-1]`.
- Confirmation filter: none. The source explicitly lists adding volume, volatility and secondary trend filters as future work.
- Risk / exit: none beyond the sign flip itself. There is no stop, no take profit, no trailing stop and no time limit.

No component is assumed to contribute alpha; ablation is required by the falsification plan, in particular gate F8 which isolates whether any edge comes from the 25-unit scale-in rather than from the sign flip.

## Signal

Everything below is read from the pinned Pine block. Nothing in this section is `research-proposed`; the single derived item (warmup) is labelled as derived from the pinned code plus official first-party documentation.

**Formation timestamp and tradability**

- Decision series: completed `1h` bars of the pinned instrument (the `period: 1h` value in the pinned backtest header).
- Inputs at decision bar `t`: `open[t]`, `high[t]`, `low[t]`, `close[t]` (through `src = ohlc4`), `src[t-1]`, and `VIDYA[t-1]`.
- Order timing: both order calls are market orders carrying a `when` argument, and the declaration sets `process_orders_on_close=true`. Official v5 documentation: "By default, strategies simulate orders at the close of each bar … Programmers can change this behavior to process orders on the closing tick of each bar by setting process_orders_on_close to true", and the reference entry adds "If the orders are market orders, the broker emulator executes them before the next bar's open." This is exactly a completed-bar decision with same-bar-close execution; there is no next-bar-open fill anywhere in the rule.
- Intra-bar recalculation: `calc_on_every_tick` and `calc_on_order_fills` are both absent from the declaration. Official v5 documentation states both default to `false`, i.e. the strategy executes strictly once per bar on the closing tick, and that `calc_on_order_fills=false` means no recalculation immediately after an order fills. Recorded as source-declared-by-language-default, not as a research-proposed choice.
- Timezone: the rule contains no time comparison at all. `StartTime` and `EndTime` are declared inputs but are never referenced (`InDateRange` is the constant `true`), so no `timestamp()`, no session and no timezone enters the trading decision. The timezone question is therefore provably irrelevant rather than unresolved.
- The `when` argument: the pinned calls read `strategy.entry("Long", strategy.long, when = VIDYA>VIDYA[1])` and `strategy.close("Long", when = VIDYA<VIDYA[1])`. Two official documents establish that `when` exists in v5: the v4-to-v5 migration guide explains that "The second parameter of strategy.close() is when, which expects a bool argument", and the v5-to-v6 migration guide lists "The when parameter is removed from all applicable strategy.*() functions" among the changes that affect v5 scripts. The v5 reference manual's SYNTAX lines for `strategy.entry` and `strategy.close` omit `when`, which is a documentation gap recorded in Negative evidence rather than an ambiguity in the rule; the parameter's meaning is taken from the reference manual entry that does document it: "Condition of the order. The order is placed if condition is 'true'. If condition is 'false', nothing happens … Default value is 'true'." During warmup the comparison evaluates to `na`, which is not `true`, so no order is placed; the official v5-to-v6 migration guide independently confirms that in v5 "na … [is] considered false" wherever a boolean is required.

**Lookback, formulas and warmup**

- `len` is declared verbatim as `len = input.int(title="VIDYA Length", defval=50, step=5,group="Trend Settings")` → 50, a const input.
- `src` is declared verbatim as `src = input.source(title="VIDYA Price Source",defval=ohlc4, group="Trend Settings")` → `ohlc4`, i.e. `src[t] = (open[t] + high[t] + low[t] + close[t]) / 4`. The artifact's own Strategy Arguments table prints the same default as index 0 of `ohlc4|high|low|open|hl2|hlc3|hlcc4|close`.
- `valpha = 2/(len+1)` = `2/51`, a const float approximately 0.0392156862745098.
- `vud1[t] = src[t] > src[t-1] ? src[t]-src[t-1] : 0` and `vdd1[t] = src[t] < src[t-1] ? src[t-1]-src[t] : 0`. At `t = 0`, `src[t-1]` is `na`, the comparison is `na`, v5 evaluates a `na` condition as false, and both terms are 0.
- `vUD[t] = math.sum(vud1, 9)` and `vDD[t] = math.sum(vdd1, 9)`, official semantics: "Sum of source for length bars back" with "na values in the source series are ignored".
- `vCMO[t] = nz((vUD[t]-vDD[t])/(vUD[t]+vDD[t]))`, i.e. the Chande Momentum Oscillator over a 9-bar window of `ohlc4`, with `nz()` replacing an `na` quotient by 0.
- The recursion, exact:

```text
var VIDYA = 0.0
VIDYA[t] = na(VIDYA[t-1])
             ? ta.sma(src, 50)
             : nz(valpha * math.abs(vCMO[t]) * src[t])
               + (1 - valpha * math.abs(vCMO[t])) * nz(VIDYA[t-1])
```

  Because `var` assigns once on the first bar, `VIDYA[0]` starts as `0.0` but is immediately overwritten by the `na(VIDYA[1])` branch.
- The plot colour expression (`VIDYA > VIDYA[1]` green, `<` red, `=` gray) is cosmetic and touches no order.
- Warmup, derived from the pinned code and official documentation because the source declares none: `ta.sma(src, 50)` is the "Simple moving average of source for length bars back", and the reference manual's own equivalent implementation sums `x[i]` for `i = 0 … 49`, which is `na` until 50 bars of history exist, so the first defined SMA value is at bar index 49. Since `VIDYA[48]` is `na`, bar index 49 also takes the SMA branch, and bar index 50 is the first bar on which `VIDYA[t-1]` is defined and the recursive branch runs. The comparison `VIDYA[t] > VIDYA[t-1]` is therefore `na` at index 49 and first defined at **bar index 50**, so the earliest possible entry is the close of the 51st completed 1h bar. `max_bars_back` is not declared; official documentation states the required history buffer is detected automatically.

**Entry**

- Long entry: `strategy.entry("Long", strategy.long)` placed when `VIDYA[t] > VIDYA[t-1]`, inside `if (InDateRange)` where `InDateRange` is the constant `true`.
- Short entry: none. The pinned code contains 0 occurrences of `strategy.short`, no short-side entry and no short-side close; the source's own Strategy Logic states only "It goes long when VIDYA rises and closes position when VIDYA falls". The short side is therefore disabled by construction and the direction of the rule is unambiguous: long only.
- Ties and simultaneous signals: `VIDYA[t] > VIDYA[t-1]` and `VIDYA[t] < VIDYA[t-1]` are mutually exclusive, and the equality case satisfies neither, so conflict priority is provably irrelevant. Both statements sit in the same `if` block, in entry-then-close order, which is immaterial because their guards cannot both hold.

**Exit**

- The pinned code contains exactly two order calls, `strategy.entry` and `strategy.close`. Census over the whole artifact: `strategy.exit` 0, `strategy.stop` 0, `strategy.cancel` 0, `strategy.order` 0, `strategy.close_all` 1 (unreachable, see below).
- Exit: `strategy.close("Long", when = VIDYA[t] < VIDYA[t-1])`. Official reference: `qty_percent` defaults to 100 and `qty` defaults to `na`, so the call closes 100 percent of the open trades carrying the entry id `Long`, as a market order filled on the closing tick of bar `t` under `process_orders_on_close=true`; with `close_entries_rule` at its documented default `"FIFO"` and a single entry id, the FIFO remark ("a strategy.close call exits from the position starting with the first open trade") is immaterial to the total size closed.
- Stop loss: none. Take profit: none. Trailing stop: none. Time limit or maximum holding period: none.
- Unreachable statement: `if (not InDateRange) strategy.close_all()` — `InDateRange` is the const `true`, so `not InDateRange` is const false and `strategy.close_all` (which "Creates an order to close an open position completely" and "always generates market orders") can never execute.

**Holding period, overlap and re-entry**

- Holding period: unbounded and determined entirely by the sign of the one-bar change of VIDYA; the source states no maximum or expected holding period.
- Maximum same-side concurrency: 25 open trades. `pyramiding=25` is declared verbatim. Official reference: pyramiding is "The maximum number of entries allowed in the same direction", and the v5 Strategies page states of `pyramiding = 20` that it allows "up to 20 entries per position with the strategy.entry() command", so 25 allows up to 25 entry trades per position; further same-direction entries are rejected by the engine.
- Same-direction re-entry while a position is open: allowed up to that cap, one attempt per bar while `VIDYA` is rising.
- Re-entry after a full exit: allowed immediately; a later rise of VIDYA opens a new position with a fresh pyramiding budget.
- Cooldown: none declared. Because every trigger is a per-bar boolean with an explicit pyramiding cap, absence of a cooldown is deterministic rather than missing, so cooldown semantics are provably irrelevant.

**Parameters, sizing and pyramiding**

- All strategy parameters are declared in source with these defaults: `VIDYA Length 50`, `VIDYA Price Source ohlc4`, `Start Time timestamp('01 Jan 2000 08:00')`, `End Time timestamp('01 Jan 2099 00:00')`. The pinned declaration reads verbatim: `strategy(title="VIDYA Trend Strategy", shorttitle="VIDYA Trend Strategy", process_orders_on_close=true, overlay=true, pyramiding=25,  commission_type=strategy.commission.percent, commission_value=.075, slippage = 1, initial_capital = 1000000, default_qty_type=strategy.percent_of_equity, default_qty_value=4)`, i.e. `process_orders_on_close=true`, `overlay=true`, `pyramiding=25`, commission `0.075` percent, `slippage=1`, `initial_capital=1000000`, `default_qty_type=strategy.percent_of_equity`, `default_qty_value=4`.
- Sizing: each entry order is 4 percent of current strategy equity at order time, so sizing is explicit and compounding, not fixed. Because the pyramiding cap is 25, the nominal notional of one position is bounded at roughly 25 x 4 percent = 100 percent of equity at entry time, so the rule's own sizing parameters keep exposure at or below about 1:1 by construction.
- Account `currency` is absent; the documented default is `currency.NONE`, "in which case the chart's currency is used". Recorded as source-declared-by-language-default.
- Leverage and margin: `margin_long` and `margin_short` are absent. The v5 reference manual states the default is 0, "in which case the strategy does not enforce any limits on position size", and the reference remarks for `strategy.margin_liquidation_price` state it "returns na if the strategy does not use margin, i.e., the strategy declaration statement does not specify an argument for the margin_long or margin_short parameter". The current reference manual instead prints default 100; the official v5-to-v6 migration guide resolves the difference by listing "The default long and short margin percentage for strategies is now 100" among the changes that affect v5 scripts, so 100 is a v6 change and the v5 default for this script is 0. Consequence for this rule: no margin mechanism, no forced liquidation and no engine-side position-size cap under v5 semantics. The documentation-version difference is recorded and gated by F3 rather than silently chosen.
- Direction: long only, with the short side disabled by construction (0 occurrences of `strategy.short`). The declared venue is a margined futures venue, so the natural instrument is a perpetual; spot would also support a long-only rule but the pinned header configures futures and that is what this record describes.
- `close_entries_rule`, `max_bars_back`, `backtest_fill_limits_assumption`, `use_bar_magnifier`, `risk_free_rate`, `calc_bars_count` are all absent; each has a documented default (`"FIFO"`, automatic, `0`, `false`, `2`, `0`) and none alters a trade: there are no limit or stop orders, no lower-timeframe data, no report-only metric that feeds an order, and a single entry id.

**Reconstruction status**

Every field required to replay the rule — indicator variant, source price, lookback, smoothing, thresholds, comparison direction, direction, entry, exit, risk semantics, sizing, pyramiding, concurrency, cooldown, timeframe and warmup — is explicit in the pinned source or fixed by a documented language default. The residual `underspecified` items are the result of a division by zero in a degenerate flat-price case (see Negative evidence 21), the exact quote currency of the account under `currency.NONE`, the precise Binance contract, and the cost/latency/fill-failure model; none of them alters the signal, and the last three are recorded as `data gap` rather than filled.

## Required data

- Instrument: BTCUSDT on Binance USDT-margined futures, taken verbatim from the pinned header `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`. Single pair, single instrument, no basket, no ranking, no cross-sectional step.
- Market type: margined futures; the artifact does not distinguish the perpetual from a dated future, which is `data gap`. It is immaterial to an OHLCV-only signal but must be pinned before any execution work. Because the rule is long-only, spot applicability is technically open, but the pinned configuration is futures and no spot variant is proposed here.
- Venue: Binance only. No cross-venue state, no venue-selection rule, no listing or survivorship rule (the artifact states none).
- Timeframe: exactly one decision timeframe, `1h`, from `period: 1h`. The same header prints `basePeriod: 15m`; the pinned script contains 0 `request.*` calls and 0 `security(` calls, so no lower- or higher-timeframe series is referenced by the rule and there is no multi-timeframe dependency to align. Official documentation also states that strategies "cannot run on data for other timeframes. They always use the same timeframe as the chart", and `use_bar_magnifier` is at its documented default `false`, so no lower-timeframe data is used for fills either.
- Fields used: `open`, `high`, `low`, `close` of the decision bar and of the immediately preceding bar, combined as `ohlc4`. Volume is not an input: the token `volume` occurs once in the whole artifact and only inside the Optimization Directions prose.
- Fields not required and not used, each absent from the pinned artifact: open interest, funding, mark or index price, basis, order book or depth, trade or aggressor feed, liquidation feed, on-chain data, options or Greeks, sentiment or news, macro series, cross-venue state, borrow data, margin state, session or calendar state.
- Point-in-time: every input at bar `t` is contemporaneous (`src[t]`) or lagged (`src[t-1]`, `VIDYA[t-1]`); there is no future reference, no negative shift, no future extrema, no full-sample normalization, no `timenow`, and no `request.*`/`security` call of any kind, so the pinned rule contains no look-ahead leakage.
- Timestamp and timezone: no time value enters the trading decision (the two declared timestamp inputs are never read), so the record makes no session, holiday or boundary assumption. Bar boundaries are exchange-defined UTC-aligned 1h candles on Binance.
- Missing data: no gap, halt or stale-bar handling is specified anywhere in the source → `data gap`. Imputation would be `research-proposed` and is not proposed here.
- Funding, fee and spread needs: commission 0.075 percent per executed order and 1 tick of slippage are declared in the source; spread, market impact, latency, funding accrual and participation limits are not specified → `data gap`, never a modeled zero.

## Execution assumptions

Source-declared (quoted or read from the pinned declaration):

- Order type: market orders only, created by one `strategy.entry` and one `strategy.close`. There is no limit order, no stop order, no OCA group and no conditional order anywhere in the rule, so there is no intrabar-path dependence and no maker/taker asymmetry to model.
- Fill model: `process_orders_on_close=true` → the order created while evaluating bar `t` fills on the closing tick of bar `t`; `calc_on_every_tick` and `calc_on_order_fills` default to `false` per official documentation, so there is exactly one evaluation per completed bar. Completed-bar decision with same-bar-close execution.
- Signal-to-order delay: none. The order is created and filled within the same completed-bar close.
- Position limits: up to 25 open trades per position from `strategy.entry`, each sized at 4 percent of equity; `strategy.close` liquidates all of them in one market order.
- Sizing and compounding: `default_qty_type=strategy.percent_of_equity`, `default_qty_value=4` → compounding, explicit in source.
- Leverage and margin: absent from the declaration; v5 default 0 means no position-size limit and no margin call (see Signal, Parameters). The current reference's default of 100 is a v6 change per the official migration guide. Either documented reading is recorded; under v5 the strategy assumes no borrowed funds and no forced liquidation.
- Shorting and borrow: the short side is never used, so borrow availability is irrelevant; spot shorting is out of scope by construction.
- Costs: `commission_type=strategy.commission.percent`, `commission_value=.075` → 0.075 percent of the cash volume charged on every executed order, i.e. on the entry and again on the close, per official documentation that commission applies to "all executed orders"; `slippage=1` → official reference: "Slippage expressed in ticks. This value is added to or subtracted from the fill price of market/stop orders to make the fill price less favorable for the strategy", so one tick of adverse slippage is applied to each market fill.
- Initial capital: `initial_capital = 1000000` in the account currency, which resolves to the chart currency under the documented `currency.NONE` default.
- Latency: not modeled in source → `data gap`.
- Participation and capacity: not modeled in source → `data gap`; tested by the research-defined gate F11.
- Failure handling (partial fills, rejects, downtime): not addressed in source → `data gap`. The pinned rule places whole market orders only, and no partial-fill-dependent condition exists.
- Scout-vs-source split: every item above marked source-declared comes from the pinned declaration, the pinned code or official TradingView documentation. Nothing in this section is a Scout-added execution rule; every pass/fail cutoff used later is labeled `research-defined`.

## Evidence

### Source-reported

The artifact prints no performance result of any kind. Word-boundary census over the pinned 6473-character artifact: sharpe 0, sortino 0, drawdown 0, max drawdown 0, cagr 0, roi 0, net profit 0, profit 0, profit factor 0, win rate 0, annualized 0, strategy tester 0, total closed trades 0, equity 0, fee 0, fees 0, funding 0, leverage 0, margin 0, spread 0, impact 0, turnover 0, capacity 0, maker 0, taker 0, latency 0, fill 0, fills 0, borrow 0, liquidation 0, open interest 0, rebalance 0, bootstrap 0, out-of-sample 0, walk-forward 0, survivorship 0, look-ahead 0, repaint 0, cooldown 0, order 0, orders 0. The substring `backtest` occurs 4 times: once in the `/*backtest ...*/` header, once in the code comment `// Backtest Date Range Inputs //`, and twice in the prose ("Good backtest results with positive expected returns", "Limited backtest data cannot fully verify robustness"). There is no performance table, no equity curve, no trade list and no figure anywhere in the artifact.

What the source does report:

- Configuration only, from the pinned header: backtest start 2023-09-29 00:00:00, end 2023-10-29 00:00:00, `period: 1h`, `basePeriod: 15m`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`.
- Parameter defaults as listed under Signal, plus the four exposed Strategy parameters confirmed both in the artifact table and on the public landing page.
- One qualitative performance claim, verbatim: "Good backtest results with positive expected returns", carrying no sample, no metric, no baseline and no figure → unverifiable as printed and recorded as a bare claim, not as evidence. Its own Risk Analysis immediately qualifies it with "Limited backtest data cannot fully verify robustness."
- Landing metadata read 2026-10-05: Created 2023-10-30 11:36:26, Last modified "3 years ago", Copy 1, Hits 1118, 0 comments. A word-boundary scan of the visible landing text for `net profit`, `sharpe`, `roi`, `max drawdown`, `profit factor`, `total closed trades`, `win rate`, `annualized`, `sortino`, `equity curve`, `trade list` and `strategy tester` returned 0 hits each; `backtest results` returned 1 hit, the same qualitative sentence.
- Research-computed, not printed: the header window spans 2023-09-29 to 2023-10-29 inclusive, i.e. 31 calendar days, which on a 24/7 market is about 744 completed 1h bars; this is our arithmetic on the printed dates and must not be read as a source-reported sample size.

No source-reported figure in this record comes from any other paper, article or repository; every claim is attributed to the single pinned artifact above.

### Independently reproduced

not independently reproduced

Only the following were performed: SHA-256 checksumming of the pinned artifact, of its whitespace-collapsed variant and of its Pine block; git blob hashing and byte-for-byte comparison against two independent GitHub API endpoints at the pinned commit; extraction and line-by-line comparison of the Pine text embedded in the FMZ landing payload; extraction and line counting of the Pine block; a whole-artifact term and word-boundary census; enumeration of `strategy.*` call sites; reading of the public FMZ landing page in a browser; a hidden-inclusive dedup scan with a positive control; and record-side enumeration of the printed header values. No market data was downloaded, no backtest was run, no Pine or third-party code was executed, and no statistic was recomputed from data.

### Negative evidence

1. The artifact prints zero performance numbers, so there is nothing to reproduce: sharpe, sortino, drawdown, cagr, roi, net profit, profit, profit factor, win rate, annualized, strategy tester and total closed trades are all 0 occurrences.
2. The single performance claim ("Good backtest results with positive expected returns") is unaccompanied by any sample, metric or baseline, so it cannot be checked as printed.
3. The only configured backtest window is 2023-09-29 to 2023-10-29, about 744 1h bars on a single instrument, with no train/test split, no out-of-sample section and no walk-forward.
4. The source's own Risk Analysis states "Limited backtest data cannot fully verify robustness. Parameters need iterative optimization and testing in live trading."
5. No risk layer of any kind: stop loss, take profit, trailing stop and time exit are absent from the code (`strategy.exit`, `strategy.stop` and `strategy.cancel` all 0), while the strings `stop loss` appear three times only in prose, twice of them as future work.
6. The source's own Optimization Directions block proposes adding a stop loss, dynamic position sizing, volume and volatility filters, other trend indicators and cross-instrument robustness tests, i.e. the published rule is explicitly presented as a starting framework; the Conclusion says exactly that.
7. The rule is long-only with no short side at all (`strategy.short` 0), so it carries no hedging path and its performance in a falling market is realized only as cash.
8. Single indicator, single parameter cell (`VIDYA Length 50`, `step=5`) with no sensitivity analysis anywhere in the source; the `step=5` declaration shows the input was designed to be tuned.
9. The source's own Risk Analysis states "Pure trend following performs poorly in choppy markets" and that the rule can "lead to larger drawdowns".
10. The source's own Risk Analysis states "VIDYA may lag in response to sudden market events and miss short-term trading opportunities."
11. Recorded contradiction 1: the Date Range inputs and the `// Backtest Date Range Inputs //` comment advertise a start/end control that the code never reads.
12. Recorded contradiction 2: the prose describes an SMA-weighting scheme that the pinned recursion does not contain.
13. Recorded contradiction 3: the version directive is printed in a non-functional form (`// @version=5`), so the artifact does not pin its language version by the documented mechanism even though v5 is the only compiling version.
14. The FMZ landing's own source pane prints `307bytes / 50words / 12lines` while the same page's payload embeds the full 1726-byte, 43-line Pine block; the discrepancy is unexplained in source.
15. The full source is behind `Login to view full source` on the FMZ landing and is publicly reachable only through a third-party mirror repository, leaving a single point of provenance.
16. The mirror repository ships no LICENSE file, so the redistribution status of the mirror as a whole is not stated in source; only the script's own MPL-2.0 notice line is printed inside the block.
17. Authorship is layered and unverified: the mirror records `Author: ChaoZhang`, the code prints `// Author = TradeAutomation`, the FMZ landing names the `ChaoZhang` account, and neither identity is independently confirmed; peer-review status is not stated in source.
18. There is no repository, no version tag, no test suite, no issue tracker and no changelog for the rule; the FMZ landing shows a single "Last modified" timestamp.
19. FMZ landing statistics (Copy 1, Hits 1118, 0 comments as read 2026-10-05) show minimal community adoption, and no third-party study of this exact artifact was identified.
20. The base-K-line field `basePeriod: 15m` in the header sits next to a `1h` decision period; although the script contains no `request.*` call and therefore no cross-timeframe dependency, a reader could mistake the header for a multi-timeframe design.
21. Division-by-zero edge: `vCMO = nz((vUD-vDD)/(vUD+vDD))` divides by an unguarded denominator. The quotient is only consumed by the recursive branch of the VIDYA update, which first runs at bar index 50; a zero denominator there requires 9 consecutive unchanged `ohlc4` values. Official first-party documentation does not state the result of division by zero in Pine v5, so the behaviour of that degenerate case is `underspecified`; the `nz()` wrapper covers the `na` reading but not a hypothetical infinite reading. Gated by F13.
22. Language-default reliance: `calc_on_every_tick`, `calc_on_order_fills`, `close_entries_rule`, `max_bars_back`, `currency`, `use_bar_magnifier`, `risk_free_rate`, `backtest_fill_limits_assumption`, `calc_bars_count`, `margin_long` and `margin_short` are all absent from the declaration. Each has an explicit documented default and is recorded as source-declared-by-language-default, but a reimplementation that silently adopts different values would not be 1:1.
23. The official reference manuals disagree on the `margin_long`/`margin_short` default (v5 prints 0 with "does not enforce any limits on position size"; the current manual prints 100) and on whether `when` appears in the v5 `strategy.entry`/`strategy.close` signatures (migration guides say yes, the v5 reference SYNTAX lines omit it). Both disagreements are documentation-version issues, resolved above with first-party migration-guide evidence, and both are gated by F3.
24. The official reference manuals also disagree on the `pyramiding` default (v5 reference prints 0, current declaration-statement docs print 1), which does not affect this artifact because `pyramiding=25` is declared explicitly; recorded only to show the default was not relied upon.
25. No independent replication, no competing study and no contrary external evidence specific to this artifact was identified; absence of contrary literature is not evidence of robustness.

## Falsification plan

All thresholds below are `research-defined falsification threshold` values chosen by this Scout; none of them is source-reported. All test inputs (data vendor, sample window, benchmark definitions, cost model) are `research-proposed` test scaffolding and are not part of the strategy rule.

- **F1 — Semantic reconstruction gate.** Threshold: an independent reimplementation of the pinned rule must reproduce, on a reference OHLCV series, the identical `VIDYA` series (bitwise-equal after the first defined value at bar index 49), the identical `na`-availability boundary (first defined comparison at bar index 50) and an identical ordered list of entry bars and close bars, with zero differing bars. Action: any mismatch means the record is not 1:1 reconstructible and must be withdrawn from admission review rather than repaired by interpretation.
- **F2 — Causality and repaint audit.** Threshold: every input used at bar `t` must be dated at or before `t` (`src[t]`, `src[t-1]`, `VIDYA[t-1]`), with zero occurrences of future bars, negative shifts, `timenow`, session recalculation, `request.*`, `security`, or bar-magnifier lower-timeframe data. Action: any future reference found ⇒ NOT_LOSSLESS, close the record.
- **F3 — Engine-default audit gate.** Threshold (research-defined): the reimplementation must confirm, from the pinned declaration plus official v5 documentation, each of `calc_on_every_tick=false`, `calc_on_order_fills=false`, `close_entries_rule="FIFO"`, `currency=currency.NONE`, `use_bar_magnifier=false`, `margin_long=0` and `margin_short=0`, and must confirm that `strategy.close` with default `qty_percent=100` liquidates the whole `Long` entry id in one order. Fail if any engine-default value used differs from the documented v5 default, or if a v6 (rather than v5) semantics set is applied to this v5 source. Action: fail ⇒ record is not 1:1 under the pinned baseline and must not be admitted.
- **F4 — Cost ladder.** Threshold (research-defined): apply 0 / 1 / 2 / 5 / 10 bps per side on top of the source's own 0.075 percent commission and one-tick slippage, plus a funding accrual leg for the perpetual; fail if net annualized return turns non-positive at 2 bps per side of additional cost, or net Sharpe falls to 0 or below at 5 bps per side. Action: fail ⇒ the edge is cost-dependent, record remains research-only and must not be proposed for any adoption.
- **F5 — Parameter perturbation.** Threshold (research-defined): sweep `VIDYA Length` over 20, 30, 40, 50, 75, 100, 150 and 200 with everything else frozen; fail if the sign of net return over the full sample flips for the published cell (50) or if fewer than half of the eight cells produce positive net return. Action: fail ⇒ parameter-lottery diagnosis, no adoption.
- **F6 — Regime breakdown.** Threshold (research-defined): split the sample into thirds by trailing 60-day realized volatility and, separately, by a 60-day ADX(14) trend-strength tercile; fail if net Sharpe is negative in at least two of three terciles in either split. Action: fail ⇒ the rule requires a regime gate that the source does not contain, so it cannot be admitted as-is and must stay research-only.
- **F7 — Always-in-market placebo.** Threshold (research-defined): compare against buy-and-hold BTCUSDT on the identical window and against 1000 random sign-flip sequences that preserve the observed holding-time distribution; fail if the observed net Sharpe does not exceed the 95th percentile of the placebo distribution. Action: fail ⇒ no evidence that the VIDYA sign timing carries information.
- **F8 — Scale-in ablation.** Threshold (research-defined): re-run the frozen rule with `pyramiding` set to 1, to 25 (the source value) and to 10, with all other parameters frozen; fail if the published 25-unit cell does not beat the 1-unit cell by more than 0.2 net Sharpe after costs at 2 bps per side, or if only the 25-unit cell is positive while the other two are non-positive. Action: fail ⇒ the apparent edge is a position-sizing artifact rather than a signal, record stays research-only.
- **F9 — Out-of-sample requirement.** Threshold (research-defined): at least 5 years of 1h BTCUSDT bars with a frozen chronological split and no re-tuning; fail if out-of-sample net Sharpe is 0 or below. Action: fail ⇒ reject for adoption; do not rescue by re-tuning.
- **F10 — Cross-instrument generalization.** Threshold (research-defined): run the identical frozen rule on ETHUSDT perpetual and on one further major perpetual chosen before inspection; fail if 0 of 2 produce positive net return after costs at 2 bps per side. Action: fail ⇒ single-asset overfit diagnosis.
- **F11 — Capacity and liquidity.** Threshold (research-defined): fail if the required notional at up to 100 percent of equity exceeds 5 percent of the trailing 30-day median daily volume of the instrument. Action: fail ⇒ capacity-capped, record the ceiling and block any size scaling.
- **F12 — Multiplicity control.** Threshold (research-defined): apply Benjamini-Hochberg at q = 0.10 across the full F5 × F10 cell family; fail if the published cell does not survive. Action: fail ⇒ treat the published configuration as one draw among many, no adoption.
- **F13 — Degenerate-data gate.** Threshold (research-defined): scan the full evaluation sample for any bar whose preceding 9 `ohlc4` values are all identical; fail if any such bar exists and the reimplementation's `vCMO` value there has not been pinned against the reference engine. Action: fail ⇒ the unguarded denominator makes that segment non-reproducible, so the affected window must be excluded and re-declared before any result is accepted.
- **F14 — Frozen forward window.** Threshold (research-defined): forward test from 2026-10-05 to 2027-10-04 with every parameter frozen; fail if forward net Sharpe at 2 bps per side is 0 or below. Action: fail ⇒ reject; no parameter may be changed to re-run it.

Global no-retuning rule: `VIDYA Length 50`, `VIDYA Price Source ohlc4`, the 9-bar CMO window, the `valpha = 2/(len+1)` recursion with its `nz()` guards, the `na`-seeded SMA initialization, the sign-of-one-bar-change entry and exit, the long-only direction, `pyramiding 25`, 4 percent percent-of-equity compounding sizing, `process_orders_on_close` same-bar-close fills, commission 0.075 percent, slippage 1 tick, initial capital 1,000,000, the single `1h` timeframe and the BTCUSDT perpetual instrument are frozen. No gate may be rescued by changing a parameter, widening a window, switching vendor, dropping a cost leg or re-defining a metric after seeing results.

## Crypto portability

`direct` — with a narrow meaning. The cited source itself targets cryptocurrency markets and configures the rule on Binance USDT-margined BTCUSDT futures at `period: 1h`, so the instrument, venue and market type are already crypto and no porting change is required to express the rule. `direct` refers only to mechanism, signal and instrument applicability; it is explicitly not a claim of crypto performance, which is `unproven` because the artifact prints no result.

Portability-relevant facts:

- The rule consumes only `open`, `high`, `low` and `close`, all available on any 24/7 crypto venue; there is no session, holiday or opening-auction dependency, and no time value enters the decision.
- No funding, open interest, mark or index price, liquidation feed, order book, aggressor side, on-chain data or options input is used, so none of those crypto-specific inputs can invalidate the signal.
- Because the short side is never used, spot, margin and perpetual are all expressible; the pinned header nevertheless configures a margined futures venue, and the perpetual funding accrual that a real perpetual position would incur is never mentioned by the source (`data gap`).
- Risks that remain crypto-specific and unmodeled by the source: perpetual funding accrual, the choice of mark versus last price for valuation (`data gap`), contract specification and tick-size differences between venues, which also set the real-world meaning of the declared one-tick slippage (`data gap`), listing and delisting churn for anything other than BTCUSDT (`data gap`), venue fragmentation and custody risk (`data gap`), and liquidity or market-impact differences at up to 100 percent of equity sizing (`data gap`).
- Candle boundaries are exchange-defined 1h candles; the record does not assume any other boundary convention.

Crypto portability is not authorization to trade and not evidence that the mechanism survives in crypto.

## Limitations

- `not independently reproduced`. Nothing in this record has been recomputed from data.
- `data gap`: no spread, impact, latency, funding, fill-failure or missing-data model, no capacity statement, no exact contract pin, no account-currency pin, no performance output.
- `underspecified`: the result of a division by zero in `vCMO` for a degenerate 9-bar flat `ohlc4` window (Negative evidence 21); the precise Binance contract; whether FMZ's backtest engine honored the same v5 language defaults as the TradingView reference (the script itself makes no cross-timeframe call).
- `unproven`: profitability, robustness, regime robustness, cross-instrument robustness, capacity and forward performance.
- Source-quality limitation: a single community mirror entry with no repository, no tests, no versioning, no peer review, layered and unverified authorship, and a landing page that hides the full source behind a login while printing an editor byte count inconsistent with its own embedded payload.
- Reproducibility limitation: because FMZ hides the full source and prints no results, the only immutable, publicly auditable artifact is the mirror at the pinned SHA, and there is no way to verify the claim of good backtest results.
- Identification limitation: the rule is price-only and unfalsified; nothing in the source separates trend persistence from a beta or from a drawdown-carrying exposure, and there is no risk layer to bound the loss path.
- Publication-bias limitation: a public strategy mirror selects for presentable, not for robust; Copy 1 and 0 comments suggest no demonstrated community reuse.
- Incremental-write check: this is the first record in the repository for this source identity after the 2026-10-04 pool reset, the pre-write probe set returned 0 matches against `main` and both open research PRs, and no Wiki Brain page exists for it, so this is not ordinary duplicate material.
- A three-item contradiction set is recorded in frontmatter. All three are internal to one artifact (table/comment versus code, prose versus code, and declared versus functional version directive); in every case the pinned code is the executable and unambiguous text, so none of them leaves the signal itself ambiguous.

## Implementation status

`not-implemented`. Nothing has been implemented in our research stack. No Pine was executed, no backtester was run, no Hummingbot package or `dev-2.17.0` backtest was attempted, no Qlib job was created, no indicator was coded, and no Paper, Testnet or Live workflow was touched. The only artifacts produced by this run are this Markdown record and its verification script.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. Presence of this record does not mean: passed LOSSLESS HB_READY review; merged to `main`; entered Hermes Wiki Brain; entered any candidate pool; completed a Hummingbot or Qlib full backtest; became a survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for Paper; approved for Testnet; approved for Live. HB_READY itself, if it were ever granted, means semantic and backtest expressibility only. No record may promote itself by wording, evidence count, confidence or schedule behavior.

## Related Wiki records

No Wiki Brain page exists for this source identity, and this run writes none. The following existing pages were checked on disk and are related by mechanism family or by execution and validation discipline rather than by source identity; none of them shares the VIDYA source, the adaptive-average sign-flip signal, or the long-only BTCUSDT 1h scope:

- [[quant/crypto-perpetual-supertrend-wpr-trend-following-cost-gate-falsification-2026-09-12]]
- [[quant/tradingview-volume-weighted-supertrend-dual-confirmation-2026-09-16]]
- [[quant/tradingview-choppiness-donchian-breakout-filter-2026-09-16]]
- [[quant/crypto-walk-forward-window-optimization-double-oos-momentum-2026-09-04]]
- [[quant/gt-score-anti-overfitting-objective-multi-metric-gate-2026-09-05]]
- [[quant/sharpe-deflated-multiple-testing-2026-08-27]]
- [[quant/signal-to-executable-pnl-costs-2026-08-28]]
- [[quant/execution-impact-capacity-almgren-square-root-2026-08-28]]
- [[quant/alpha-research-contract-2026-08-28]]

## Sources

- https://github.com/fmzquant/strategies — pinned commit `7853bb2bf262c4567ac238d3552d97f0e50cb801`, path `动量趋势跟踪策略Momentum-Trend-Following-Strategy.md`; the complete primary source read end to end on 2026-10-05, SHA-256 `98c9e9f9f2e36210bd717b09a54e6726fd8e1982d5c024f3ff201a635832c1c9`.
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E5%8A%A8%E9%87%8F%E8%B6%8B%E5%8A%BF%E8%B7%9F%E8%B8%AA%E7%AD%96%E7%95%A5Momentum-Trend-Following-Strategy.md — percent-encoded form of the same pinned file.
- https://www.fmz.com/strategy/430552 — FMZ landing page, read 2026-10-05; confirms title, type, author account, creation timestamp, English description, backtest header, exposed parameters, statistics, the `Login to view full source` gate, and the full Pine text embedded in the page payload.
- https://www.tradingview.com/pine-script-reference/v5/#fun_strategy — official first-party v5 reference used for `strategy()` parameter defaults (`pyramiding`, `calc_on_order_fills`, `calc_on_every_tick`, `default_qty_type`, `default_qty_value`, `initial_capital`, `currency`, `slippage`, `commission_type`, `commission_value`, `process_orders_on_close`, `close_entries_rule`, `margin_long`, `margin_short`), for `strategy.entry`, `strategy.close` and `strategy.close_all` semantics, for `math.sum`, `ta.sma` and `ta.stdev`, and for the `strategy.margin_liquidation_price` remark that a strategy without declared margins does not use margin.
- https://www.tradingview.com/pine-script-docs/v5/concepts/strategies/ — official first-party v5 documentation used for the broker emulator, `calc_on_every_tick`, `calc_on_order_fills`, `process_orders_on_close`, position sizing, FIFO closing, commission and slippage behaviour, and the `pyramiding = 20` "up to 20 entries per position" statement.
- https://www.tradingview.com/pine-script-docs/v5/migration-guides/to-pine-version-5 — official first-party v4-to-v5 migration guide used for the v5 introduction of the `math` namespace and `input.int`, for the statement that `when` is the second parameter of `strategy.close` in v5, and for the `na`-as-false behaviour of boolean conditions.
- https://www.tradingview.com/pine-script-docs/migration-guides/to-pine-version-6 — official first-party v5-to-v6 migration guide used for "The when parameter is removed from all applicable strategy.*() functions" and "The default long and short margin percentage for strategies is now 100", which together pin the v5 meaning of both parameters for this v5 source.
- https://www.tradingview.com/pine-script-docs/v5/language/script-structure/ — official first-party documentation of the `//@version=5` compiler-annotation form and of the rule that an omitted annotation defaults to version 1.
- https://www.tradingview.com/pine-script-reference/v4/#fun_strategy_entry — official first-party reference used only for the documented meaning of the `when` parameter ("The order is placed if condition is 'true'"), which the v5 reference manual omits from its SYNTAX lines.
