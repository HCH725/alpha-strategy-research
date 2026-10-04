---
schema: strategy-research-record-v1
title: Golden-dead-cross moving-average trend tracking system on BTCUSDT 1d bars
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
  - https://www.fmz.com/strategy/435513
  - https://www.fmz.com/strategy/430773
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
  - https://www.tradingview.com/pine-script-docs/v5/concepts/strategies/
  - https://www.tradingview.com/pine-script-docs/v5/language/script-structure/
  - https://www.tradingview.com/pine-script-docs/migration-guides/to-pine-version-6/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The artifact's own Strategy Arguments table lists three date-window controls (v_input_bool_2 '특정 기간 백테스트' default true, v_input_1 timestamp(1 Jan 2021), v_input_2 timestamp(1 Jan 2022)) and the pinned code declares useDateFilter, backtestStartDate and backtestEndDate, but the code assigns inTradeWindow = true as a constant, never reads any of the three date inputs, and guards every order with that constant, so the advertised backtest window control is inert and the strategy has no date filter."
  - "The prose states that after going long the strategy 'would lock in profits based on the configured profit target. When the price rise hits the profit target, it would actively lock in profits and exit', i.e. an unconditional fixed-percentage take-profit, but the pinned code declares no take-profit order at all (strategy.exit 0, strategy.limit 0, strategy.stop 0) and its single exit instruction requires a same-bar dead cross in addition to the profit test, so the described take-profit exit does not exist in the code."
  - "The prose advertises 'Timely stop loss, controlling risks' and states that on a dead cross the strategy cuts losses in downtrends, but the pinned exit condition is close > strategy.position_avg_price * longStopPerc with longStopPerc = 1.03, which can only be satisfied while the position is at least 3 percent above its average entry price; a position below that level is never exited by any instruction in the code, so the advertised loss-cutting behaviour is absent."
---

# Golden-dead-cross moving-average trend tracking system on BTCUSDT 1d bars

## Provenance

Immutable GitHub source (this is the primary source actually read end to end):

- Repository URL: https://github.com/fmzquant/strategies
- Full commit SHA: `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit date 2025-04-30T03:10:28Z, i.e. 2025-04-30 11:10:28 +0800, subject `update`). The GitHub `commits/HEAD` API returned this same SHA on 2026-10-05, so it is still the repository head at research time.
- Exact file path: `金叉死叉趋势追踪策略Golden-Dead-Cross-Trend-Tracking-Strategy.md` (the non-ASCII filename is preserved verbatim; percent-encoded blob URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E9%87%91%E5%8F%89%E6%AD%BB%E5%8F%89%E8%B6%8B%E5%8A%BF%E8%BF%BD%E8%B8%AA%E7%AD%96%E7%95%A5Golden-Dead-Cross-Trend-Tracking-Strategy.md )
- Relevant source URL recorded inside the artifact: https://www.fmz.com/strategy/435513

Primary-source checksums pinned 2026-10-05 from a checkout of that exact commit:

- File 9819 bytes, SHA-256 `5b0869c40fcacc8c564e7657580cea40f5bc25144322703aa7317b44f64acf35`, 7434 characters, 193 newlines (194 lines), git blob `7b350392d8a391e0dcae86b0e4c7a7783ca8b0cd`.
- Whitespace-collapsed variant 7267 characters, SHA-256 `a91d5d8a6d75155dc345c6555bc8c9be85412579c6a4052ed233bfe0bde6d6b3`.
- The fenced Pine block alone: 48 lines (34 non-empty), 1725 bytes / 1580 characters, SHA-256 `e580e1bd406da22baf89bd03dd7fb7abb50c35b344fbf11829135b025e8729a1`.
- The Pine block with only the leading `/*backtest …*/` header removed: 1573 bytes / 1428 characters, SHA-256 `dee58bf063268fa439c096d01c07b767ad91b09ea13b42a016fb8580a26eabf1`. This "body" digest is the one used below to compare sibling mirror entries.
- The block is not pure ASCII: it carries the `// © Ta3MooChi` credit line and one Korean comment string, `매매 종료`, inside the never-executed branch.

Artifact structure as printed: `> Name` (金叉死叉趋势追踪策略Golden-Dead-Cross-Trend-Tracking-Strategy), `> Author` = ChaoZhang, `> Strategy Description` (a Chinese section set and an English set inside one `[trans]` block, preceded by one FMZ-hosted PNG), `> Strategy Arguments` table with 8 rows, `> Source (PineScript)` fenced block preceded by an FMZ `/*backtest ...*/` header, `> Detail` = https://www.fmz.com/strategy/435513, `> Last Modified` = 2023-12-15 16:10:24.

Licence and rights: the pinned Pine block prints `// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/` and the author credit `// © Ta3MooChi`. The mirror repository ships no LICENSE file, so the redistribution status of the mirror as a whole is not stated in source; this record therefore cites and normalizes the rule and reproduces no source code block.

FMZ landing page read directly over HTTPS on 2026-10-05 (public, no login for the description layer): type tag `Common strategy`, author account `ChaoZhang`, `Created: 2023-12-15 16:10:24`, `Last modified: 3 years ago`, `Copy: 3`, `Hits: 927`, a comment section headed `All comments` that reports zero comments once HTML comments, style blocks and tags are stripped, the Chinese and English description prose, the eight exposed Strategy parameters, the literal string `Login to view full source`, and a static HTML payload that contains the complete Pine text.

The landing page's server-rendered payload nevertheless contains the complete Pine text: after extracting the `"source"` field and unescaping it, the payload yields 1724 bytes / 47 lines whose content equals the mirror's fenced Pine block after removing that block's single trailing newline (payload SHA-256 `a7dbde119dd8856b8f3d29b99e72c8735e2a74fd03db1f56f444b683f96ce24a`). Consequence: the mirror and the landing page agree byte for byte on the executable text. Unlike some sibling entries, this landing page exposes no editor byte/word/line counter in its static HTML (after tag stripping: `bytes` 0, `words` 0, `UTF-8` 0 occurrences), so there is no counter discrepancy to record.

FMZ backtest header printed verbatim inside the pinned artifact:

```text
start: 2022-12-08 00:00:00
end: 2023-12-14 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
```

Version determination: the block's first directive line is `//@version=5`, the exact annotation form documented by the official script-structure page, which states "A compiler annotation in the following form tells the compiler which of the versions of Pine Script® the script is written in: `//@version=5`. The version number can be 1 to 5. The compiler annotation is not mandatory. When omitted, version 1 is assumed." The code also uses only v5-compatible constructs (`ta.sma`, `ta.crossover`, `ta.crossunder`, `input.int`, `input.bool`, `input.float`, `strategy.close_all`), so the rule is Pine v5 semantics and every language default recorded below is the v5 default.

Sibling entry, recorded so the source identity is not ambiguous (stated, not merged): the same repository contains `黄金交叉追涨杀跌策略Golden-Cross-Trend-Following-Strategy.md` at the same commit (8956 bytes, SHA-256 `596b006cbc162dc96f35a727a185aca16bd5a06d0da193a52fea91bcf57ef084`, git blob `60fd0a51ab9952f95ba1f0b74a876cc7d096fef8`, FMZ strategy 430773, landing `Created : 2023-11-01 17:02:14`) whose Pine body is byte-identical to this one — both header-stripped bodies are 1573 bytes with SHA-256 `dee58bf063268fa439c096d01c07b767ad91b09ea13b42a016fb8580a26eabf1` — and whose only difference is its own FMZ backtest header (`period: 1h`, `basePeriod: 15m`, window 2023-10-01 to 2023-10-31). Because the decision timeframe is material to every signal, this record is pinned to FMZ 435513 with `period: 1d` and to that file's bytes alone; the 1-hour sibling is a different decision horizon of the same script and is not claimed here.

Provenance gaps (stated, not repaired): no DOI, no version tag, no repository, no test suite, no issue tracker entry, no peer-review statement and no performance output anywhere; peer-review status is not stated in source.

Pre-write dedup (2026-10-05): a hidden-inclusive search (`rg -uuu`) of the whole working tree with the probe set `Golden-Dead-Cross`, `Golden Dead Cross`, `435513`, `430773`, `Ta3MooChi`, `金叉死叉`, `黄金交叉`, `longStopPerc`, `trend_ma` returned 0 matches in `main` and 0 matches in both open research PRs (PR #6 `wave-trend-lazybear-wt1-wt2-cross-btcusdt-1h-2026-10-05.md`, PR #7 `p-signal-erf-dead-band-reversal-btcusdt-1h-2026-10-05.md`, fetched for this run). The positive controls `Gann HiLo` and `VIDYA` each returned 4 matches in `main`, so the scan is effective. The loose probe `golden cross` returned exactly one hit, inside PR #6's quotation of the LazyBear Wave Trend prose where "golden cross" names the WT1/WT2 oscillator crossing; the signal construction, source identity and mechanism are different, so there is no material overlap. `git ls-remote origin 'research/*'` returned exactly three refs (the Gann branch, PR #6's `research/hermes-wave-trend-lazybear-20261005-0318`, PR #7's `research/hermes-p-signal-erf-reversal-20261005-0414`). The dedup set is therefore `main` (two records: Gann HiLo, VIDYA) plus those two open PRs.

Five-axis distinction against every member of that dedup set: source identity differs in all four cases (FMZ strategy 435513 / the `fmzquant/strategies` path above, versus the Gann HiLo artifact, the VIDYA artifact, the LazyBear Wave Trend script and the Kharevsky P-Signal script); mechanism differs (a two-line moving-average golden/death cross gated by a third, longer moving-average trend state versus a displaced average-high/average-low band state machine, a CMO-adaptive recursive average whose sign of change drives the trade, a stochastic-momentum oscillator overbought/oversold crossing, and a standardized first difference passed through an error-function dead band); signal construction differs (crossover/crossunder of two simple moving averages of `close` versus a two-state band flip, the sign of a one-bar change of an adaptive average, an oscillator line crossing, and a threshold crossing on a normalized series); direction differs (this rule is long-only, P-Signal and Wave Trend are two-sided); material data dependency does not differ (all are OHLCV-only). Universe (BTCUSDT) and horizon (1d) coincide with the Gann HiLo record and horizon differs from the three 1h records, but the dedup contract requires same source identity plus materially same normalized rule, which is not met.

## Economic mechanism

### Source-reported

The source states the mechanism only descriptively; it gives no behavioural, structural or risk-premium channel.

- Overview, as printed: "The golden dead cross trend tracking strategy determines the timing of entry and exit by calculating the crossovers between short-term and long-term moving averages. At the same time, it also combines the judgment of larger time frame trends. It would only go long when the major trend goes up to avoid going against the trend."
- Strategy Logic, as printed: "When the short-term line goes above the long-term line, a golden cross is formed, indicating an uptrend. When the short-term line goes below the long-term line, a dead cross is formed, indicating a downtrend." … "This strategy also uses an even longer period moving average to determine the direction of the major trend. It would only go long on golden crosses when the major trend is up. After going long, it would lock in profits based on the configured profit target. When the price rise hits the profit target, it would actively lock in profits and exit." … "In downtrends, this strategy uses dead crosses to cut losses. When the short-term MA crosses below the long-term MA forming a dead cross, if the current position already has some profits at that point, it would choose to cut losses and exit to avoid risks associated with downtrends."
- Advantages, as printed: "Accurate entry, tracking strengths"; "Reasonable profit-taking, ensuring partial profits … By setting a fixed percentage as the profit target and actively taking profits when it is reached"; "Timely stop loss, controlling risks … Using dead crosses to determine trend reversal and cut losses in downtrends."
- Risks, as printed: "Inaccurate signal risks … purely relying on simple indicators like golden dead crosses to determine trends can lead to some inaccurate signals. Price action patterns can be more accurate in complex environments." and "Improper profit target and stop loss risks … If profit percentage is too low, it would exit too early leading to lost profits. If stop loss percentage is too high, it may lead to larger losses."
- Optimization Directions, as printed: "Using more indicators like baseline, channel lines to improve trend and key points recognition accuracy" and "Use dynamic profit targets and stop losses instead of fixed percentages, with the ability to adjust based on market changes."
- Conclusion, as printed: "It has the advantages of clear rules, dynamic profit-taking and timely stop losses. But the accuracy of cross signals needs improvement and profit targets and stop loss mechanisms require further optimization, which are the main problems and improvement directions."

Three of those printed statements contradict the pinned code and are recorded in frontmatter `contradictions`: the inert date-window controls, the claimed unconditional fixed-percentage take-profit, and the claimed loss-cutting stop.

The prose also uses illustrative periods ("short-term line usually chooses relatively short periods like 5-day and 10-day", "long-term line usually chooses relatively long periods like 20-day and 60-day") that are not the code's defaults (3 and 19); the defaults are taken from the pinned code and from the artifact's own Strategy Arguments table, not from the prose.

### Research interpretation

Falsifiable mechanism hypothesis: daily BTC returns exhibit short-horizon directional persistence, and the crossing of a 3-day average of `close` over a 19-day average of `close` marks a local change of drift whose confirmation can be gated by the slope of a 100-day average, so that the rule takes the persistence only when the slow trend agrees. Candidate behavioural or structural channels are trend-following herding in a 24/7 market with no closing auction, and slow diffusion of directional information that makes a fast average cross a lagging but non-random marker of a regime change. The profit gate adds a second, separable hypothesis: that gains realised within a holding period are large enough relative to entry that requiring a 3 percent cushion before any exit filters churn at the cost of holding losers. This is a ported technical-analysis hypothesis: the source supplies no economic rationale and no evidence, so the mechanism is research interpretation, not source-reported fact.

Component roles, stated plainly because the source offers no composite structure:

- Regime / trend state: `inTrendMa`, which under the default `use_trend_ma = true` is exactly `trend_ma > trend_ma[1]` with `trend_ma = ta.sma(close, 100)`.
- Primary signal: `longcondition = ta.crossover(short_ma, long_ma)` with `short_ma = ta.sma(close, 3)` and `long_ma = ta.sma(close, 19)`.
- Exit signal: `shortcondition = ta.crossunder(short_ma, long_ma)`, additionally gated by `close > strategy.position_avg_price * 1.03`.
- Confirmation filter: the trend state gates the entry only; it does not gate the exit.
- Risk / exit layer: none beyond the gated `strategy.close_all()`. There is no stop loss, no take profit order, no trailing stop and no time limit anywhere in the code.

No component is assumed to contribute alpha; ablation is required by the falsification plan, in particular gate F8 which isolates whether the 100-day trend filter carries any of the effect.

## Signal

Everything below is read from the pinned Pine block. Nothing in this section is `research-proposed`; the single derived item (warmup) is labelled as derived from the pinned code plus official first-party documentation.

**Formation timestamp and tradability**

- Decision series: completed `1d` bars of the pinned instrument (the `period: 1d` value in the pinned backtest header).
- Inputs at decision bar `t`: `close[t]`, and the lags produced by `ta.sma` and by the `[1]` history reference, i.e. `close[t-1] … close[t-100]` through `trend_ma` and `trend_ma[1]`, plus `strategy.position_avg_price[t]` when a position is open.
- Order timing: both order calls are market orders and the declaration sets `process_orders_on_close = true`. Official v5 reference: "When set to true, generates an additional attempt to execute orders after a bar closes and strategy calculations are completed. If the orders are market orders, the broker emulator executes them before the next bar's open." Official v5 Strategies page: "By default, strategies simulate orders at the close of each bar … Programmers can change this behavior to process orders on the closing tick of each bar by setting process_orders_on_close to true". This is exactly a completed-bar decision with same-bar-close execution; there is no next-bar-open fill anywhere in the rule.
- Intra-bar recalculation: `calc_on_every_tick` and `calc_on_order_fills` are both absent from the declaration. Official v5 reference: both are "Optional. The default is false", and `calc_on_order_fills` "Specifies whether the strategy should be recalculated after an order is filled. If true, the strategy recalculates after an order is filled, as opposed to recalculating only when the bar closes." Recorded as source-declared-by-language-default, not as a research-proposed choice, so there is exactly one evaluation per completed bar.
- Timezone: the rule contains no time comparison that reaches an order. `useDateFilter`, `backtestStartDate` and `backtestEndDate` are declared and listed in the artifact's Strategy Arguments table but are never read; `inTradeWindow` is the constant `true` and is the only "window" expression used. No `timestamp()`, no session and no timezone therefore enters the trading decision, so the timezone question is provably irrelevant rather than unresolved.
- Conditional `na`: during warmup the composite entry condition can evaluate to `na`. The official v5-to-v6 migration guide states for v5 that "'bool' variables have three possible values: they can be true, false, or na … When implicitly cast to 'bool', na is evaluated as false", so no order is placed on such bars.

**Lookback, formulas and warmup**

- `short_ma = ta.sma(close, input.int(3, "단기 이평", minval = 1))` → length 3, a const input (Strategy Arguments row `v_input_int_1 | 3`).
- `long_ma = ta.sma(close, input.int(19, "장기 이평", minval = 1))` → length 19 (row `v_input_int_2 | 19`).
- `trend_ma = ta.sma(close, input.int(100, " 추세 이평", minval = 20, group = "추세 이평"))` → length 100 (row `v_input_int_3 | 100`).
- `ta.sma` official semantics: "function returns the moving average, that is the sum of last y values of x, divided by y", with the reference's own equivalent implementation `pine_sma(x, y) => sum = 0.0; for i = 0 to y - 1; sum := sum + x[i] / y; sum` and the remark "na values in the source series are ignored", so the first defined value is at bar index `length - 1`.
- `up_trend = trend_ma > trend_ma[1]` — one-bar slope test on the 100-day average.
- `use_trend_ma = input.bool(true, title = "추세용 이평 사용", group = "추세 이평")` → `true` (row `v_input_bool_1 | true`), hence `inTrendMa = not use_trend_ma or up_trend` evaluates to `up_trend` under the published defaults.
- `useDateFilter = input.bool(true, …)`, `backtestStartDate = input(timestamp("1 Jan 2021"), …)`, `backtestEndDate = input(timestamp("1 Jan 2022"), …)` → all three declared, rows `v_input_bool_2 | true`, `v_input_1 | timestamp(1 Jan 2021)`, `v_input_2 | timestamp(1 Jan 2022)`, and none of them is read by the code.
- `inTradeWindow = true` — a constant, not a variable.
- `longStopPerc = 1 + input.float(3, "최소수익률%", minval = 1) * 0.01` → 1.03 exactly (row `v_input_float_1 | 3`); the multiplication is performed on the const input, so the result is a const float.
- `longcondition = ta.crossover(short_ma, long_ma)`; official semantics: "The source1-series is defined as having crossed over source2-series if, on the current bar, the value of source1 is greater than the value of source2, and on the previous bar, the value of source1 was less than or equal to the value of source2."
- `shortcondition = ta.crossunder(short_ma, long_ma)`; official semantics: "… on the current bar, the value of source1 is less than the value of source2, and on the previous bar, the value of source1 was greater than or equal to the value of source2."
- Warmup, derived from the pinned code and official documentation because the source declares none: `short_ma` first defined at bar index 2, `long_ma` at 18, `trend_ma` at 99. `ta.crossover`/`ta.crossunder` need both series at `t` and `t-1`, so they can first be non-`na` at index 19. `up_trend` needs `trend_ma[1]`, which is first defined at index 100 (at index 99 the comparison is `na`, `inTrendMa` becomes `na`, and the whole entry condition evaluates to `na`, i.e. false). Therefore **bar index 100, the close of the 101st completed 1d bar, is the earliest possible entry**, and an exit can occur only after an entry. `max_bars_back` is not declared; official documentation states the required history buffer is detected automatically.
- The three `plot()` calls and the color expression are cosmetic and touch no order.

**Entry**

- Long entry: `strategy.entry("long", strategy.long)` placed when `longcondition and inTradeWindow and inTrendMa`.
- Short entry: none. The pinned code contains 0 occurrences of `strategy.short`, no short-side entry and no short-side close; the identifier `shortcondition` is used only as an exit trigger for the long position. The source's own Overview states only "It would only go long when the major trend goes up". The short side is therefore disabled by construction and the direction of the rule is unambiguous: long only.
- Ties and simultaneous signals: `longcondition` and `shortcondition` are mutually exclusive by their documented definitions, because they require opposite strict inequalities between `short_ma` and `long_ma` on the current bar; the equality case satisfies neither. Conflict priority is therefore provably irrelevant. The entry and the exit sit in separate `if` blocks, entry first, which is immaterial because their guards cannot both hold.

**Exit**

- The pinned code contains exactly two order-placing instructions, one `strategy.entry` and `strategy.close_all` inside the gated exit block, plus one unreachable `strategy.close_all` (see below). Census over the whole artifact, comments excluded: `strategy.exit` 0, `strategy.order` 0, `strategy.stop` 0, `strategy.limit` 0, `strategy.close(` 0, `strategy.close_all` 2, `strategy.cancel_all` 1.
- Exit: `if (shortcondition) and (close > strategy.position_avg_price * longStopPerc) and inTradeWindow` → `strategy.close_all()`. Official reference: `strategy.close_all()` "Creates an order to close an open position completely, regardless of the identifiers of the entry orders that opened or added to it. This command always generates market orders." With `process_orders_on_close=true` that market order fills on the closing tick of bar `t`.
- Position test: official reference for `strategy.position_avg_price`: "Average entry price of current market position. If the market position is flat, 'NaN' is returned." When flat the comparison is `na`, the conjunction is `na`, and the condition is evaluated as false, so a death cross while flat creates no order.
- Stop loss: none. Take profit: none (no `strategy.exit`, no `stop=`, no `limit=`). Trailing stop: none. Time limit or maximum holding period: none. If the death cross arrives while the position is below the 3 percent cushion, no exit occurs and the position persists indefinitely.
- Unreachable statements: `if not inTradeWindow and inTradeWindow[1]` guards `strategy.cancel_all()` and `strategy.close_all(comment = "매매 종료")`. `inTradeWindow` is the const `true`, so `not inTradeWindow` is const false and neither statement can ever execute. `strategy.cancel_all()` would in any case be a no-op because the rule creates no pending order.

**Holding period, overlap and re-entry**

- Holding period: unbounded and determined entirely by whether a death cross arrives while the position is at least 3 percent above its average entry price; the source states no maximum or expected holding period.
- Maximum same-side concurrency: 100 open trades. `pyramiding = 100` is declared verbatim. Official reference: pyramiding is "The maximum number of entries allowed in the same direction", and the v5 Strategies page states of `pyramiding = 20` that it allows "up to 20 entries per position with the strategy.entry() command", so 100 allows up to 100 entry trades per position; further same-direction entries are rejected by the engine.
- Same-direction re-entry while a position is open: allowed up to that cap, at most one attempt per bar because the trigger is a per-bar crossover event.
- Re-entry after a full exit: allowed immediately; a later golden cross opens a new position with a fresh pyramiding budget.
- Cooldown: none declared, and Pine's v5 strategy declaration exposes no cooldown field. Because every trigger is a per-bar boolean, a fresh entry additionally requires a new crossover event, and the pyramiding cap bounds the accumulation, absence of a cooldown is deterministic rather than missing, so cooldown semantics are provably irrelevant.

**Parameters, sizing and pyramiding**

- The pinned declaration reads verbatim: `strategy("전략", overlay=true,process_orders_on_close = true, pyramiding = 100)`, i.e. `overlay = true`, `process_orders_on_close = true`, `pyramiding = 100`. No other strategy property is declared.
- Declaration parameters the code leaves unset, each recorded as source-declared-by-language-default with the official page that documents it: `default_qty_type=strategy.fixed` and `default_qty_value=1` ("Optional. The default is strategy.fixed." / "Optional. The default is 1."), `initial_capital=1000000` ("Optional. The default is 1000000."), `currency=currency.NONE` ("Optional. The default is currency.NONE, in which case the chart's currency is used."), `slippage=0` ("Optional. The default is 0."), `commission_type=strategy.commission.percent` with `commission_value=0` ("Optional. The default is strategy.commission.percent." / "Optional. The default is 0."), `calc_on_order_fills=false`, `calc_on_every_tick=false`, `close_entries_rule="FIFO"`, `max_bars_back` auto-detected, `backtest_fill_limits_assumption=0`, `use_bar_magnifier=false`, `margin_long=0` and `margin_short=0`.
- Sizing: each entry order is exactly 1 unit of the base asset (contracts/shares/lots/units, per `strategy.fixed`), independent of equity, so sizing is explicit-in-the-language and fixed rather than compounding. Because `pyramiding = 100`, the nominal notional of one position is bounded at 100 units, which for the pinned BTCUSDT instrument can exceed the initial capital; that is the source's own behaviour under `margin_long = 0`, not a research choice (see Execution assumptions).
- Costs: commission is 0 (percent type, value 0) and slippage is 0 ticks, so the source declares no cost model. Per the repository contract this is recorded explicitly as an unstated cost model rather than as a modeled zero: no fee, spread, impact or funding assumption is added anywhere in this record.
- Account `currency` is absent; the documented default is `currency.NONE`, "in which case the chart's currency is used". Recorded as source-declared-by-language-default.
- Leverage and margin: `margin_long` and `margin_short` are absent. The v5 reference states the default is 0, "in which case the strategy does not enforce any limits on position size", and the official v5-to-v6 migration guide resolves the version question by stating "In v5, the default value of the margin_long and margin_short parameters is 0, which means that the strategy does not check its available funds before creating or managing orders. It can create orders that require more money than is available". Consequence for this rule: no margin mechanism, no forced liquidation and no engine-side position-size cap under v5 semantics, which is what makes a 100-unit fixed-size stack expressible.
- Direction: long only, with the short side disabled by construction (0 occurrences of `strategy.short`). The declared venue is a margined futures venue, so the natural instrument is a perpetual; because the rule never shorts, spot would also support it, but the pinned header configures futures and that is what this record describes.
- `close_entries_rule`, `max_bars_back`, `backtest_fill_limits_assumption`, `use_bar_magnifier`, `risk_free_rate` and `calc_bars_count` are all absent; each has a documented default (`"FIFO"`, automatic, `0`, `false`, `2`, `0`) and none alters a trade: there are no limit or stop orders, no lower-timeframe data, no report-only metric that feeds an order, and a single entry id liquidated in one `strategy.close_all()`.

**Reconstruction status**

Every field required to replay the rule — indicator variant, source price, lookback, smoothing method, threshold, comparison direction, direction, entry, exit, risk semantics, sizing, pyramiding, concurrency, cooldown, timeframe and warmup — is explicit in the pinned source or fixed by a single documented v5 language default. The residual `underspecified` items are the exact quote currency of the account under `currency.NONE`, the precise Binance contract, and the cost/latency/fill-failure model; none of them alters the signal, and all are recorded as `data gap` rather than filled.

## Required data

- Instrument: BTCUSDT on Binance, taken verbatim from the pinned header `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`. Single pair, single instrument, no basket, no ranking, no cross-sectional step.
- Market type: margined futures; the artifact does not distinguish the perpetual from a dated future, which is `data gap`. It is immaterial to an OHLCV-only signal but must be pinned before any execution work. Because the rule is long-only, spot applicability is technically open, but the pinned configuration is futures and no spot variant is proposed here.
- Venue: Binance only. No cross-venue state, no venue-selection rule, no listing or survivorship rule (the artifact states none).
- Timeframe: exactly one decision timeframe, `1d`, from `period: 1d`. The same header prints `basePeriod: 1h`; the pinned script contains 0 `request.*` calls and 0 `security(` calls, so no lower- or higher-timeframe series is referenced by the rule and there is no multi-timeframe dependency to align. Official documentation also states that strategies "cannot run on data for other timeframes. They always use the same timeframe as the chart", and `use_bar_magnifier` is at its documented default `false`, so no lower-timeframe data is used for fills either.
- Fields used: `close` of the decision bar and of lags up to 100 bars back, through three `ta.sma` calls, one `[1]` history reference and two crossover/crossunder comparisons, plus `strategy.position_avg_price` while a position is open. `open`, `high` and `low` are never read by the trading logic (they appear only inside `plot` colour handling, which touches no order); `volume` occurs 0 times in the whole artifact.
- Fields not required and not used, each absent from the pinned artifact: open interest, funding, mark or index price, basis, order book or depth, trade or aggressor feed, liquidation feed, on-chain data, options or Greeks, sentiment or news, macro series, cross-venue state, borrow data, margin state, session or calendar state.
- Point-in-time: every input at bar `t` is contemporaneous (`close[t]`, `short_ma[t]`, `long_ma[t]`, `trend_ma[t]`) or lagged (`trend_ma[t-1]`, the `[1]` terms inside the crossover tests, `position_avg_price`); there is no future reference, no negative shift, no future extrema, no full-sample normalization, no `timenow`, and no `request.*`/`security` call of any kind, so the pinned rule contains no look-ahead leakage.
- Timestamp and timezone: no time value reaches an order (the three declared date inputs are never read), so the record makes no session, holiday or boundary assumption. Bar boundaries are exchange-defined UTC-aligned daily candles on Binance.
- Missing data: no gap, halt or stale-bar handling is specified anywhere in the source → `data gap`. Imputation would be `research-proposed` and is not proposed here.
- Funding, fee and spread needs: the source declares commission 0 and slippage 0; spread, market impact, latency, funding accrual and participation limits are not specified → `data gap`, never a modeled zero.

## Execution assumptions

Source-declared (quoted or read from the pinned declaration):

- Order type: market orders only, created by one `strategy.entry` and one `strategy.close_all`. There is no limit order, no stop order, no OCA group and no conditional order anywhere in the rule, so there is no intrabar-path dependence and no maker/taker asymmetry to model. The broker emulator's documented intrabar assumption ("Because the broker emulator only uses price data from the chart by default, it makes assumptions about intrabar price movement when filling orders") is therefore never exercised, because that assumption applies to price-dependent orders.
- Fill model: `process_orders_on_close=true` → the order created while evaluating bar `t` fills on the closing tick of bar `t`; `calc_on_every_tick` and `calc_on_order_fills` default to `false` per official documentation, so there is exactly one evaluation per completed bar. Completed-bar decision with same-bar-close execution.
- Signal-to-order delay: none. The order is created and filled within the same completed-bar close.
- Position limits: up to 100 open trades per position from `strategy.entry`, each sized at exactly 1 unit; `strategy.close_all` liquidates all of them in one market order.
- Sizing and compounding: `default_qty_type=strategy.fixed`, `default_qty_value=1` → fixed, equity-independent, not compounding, explicit by documented language default.
- Leverage and margin: absent from the declaration; v5 default 0 means no position-size limit and no margin call, and the official migration guide states the strategy "does not check its available funds before creating or managing orders. It can create orders that require more money than is available." Either documented reading is recorded; under v5 the strategy assumes no borrowed funds, no forced liquidation and an exposure that may exceed equity by up to 100 units.
- Shorting and borrow: the short side is never used, so borrow availability is irrelevant; spot shorting is out of scope by construction.
- Costs: commission percent type with value 0 → no commission is charged; `slippage=0` → no tick slippage. The source therefore declares no cost model at all; per contract this gap is recorded explicitly and a later benchmark fee is a runtime assumption, not a source-reported strategy rule.
- Initial capital: `initial_capital = 1000000` in the account currency, which resolves to the chart currency under the documented `currency.NONE` default. Because sizing is fixed in units, initial capital sets the absolute scale of exposure but cannot change the signal, the trade sequence or the unit size.
- Latency: not modeled in source → `data gap`.
- Participation and capacity: not modeled in source → `data gap`; tested by the research-defined gate F11.
- Failure handling (partial fills, rejects, downtime): not addressed in source → `data gap`. The pinned rule places whole market orders only, and no partial-fill-dependent condition exists.
- Engine-settings overrides a chart user could apply (initial capital, currency, order size, commission, margin, pyramiding, execution delay) are not part of the pinned source; the code-declared values plus the documented defaults above are the recorded strategy.
- Scout-vs-source split: every item above marked source-declared comes from the pinned declaration, the pinned code or official TradingView documentation of that language. Nothing in this section is a Scout-added execution rule; every pass/fail cutoff used later is labeled `research-defined`.

## Evidence

### Source-reported

The artifact prints no performance result of any kind. Word-boundary census over the pinned 9819-byte artifact: sharpe 0, sortino 0, drawdown 0, max drawdown 0, cagr 0, roi 0, net profit 0, profit factor 0, win rate 0, annualized 0, strategy tester 0, total closed trades 0, equity 0, margin 0, commission 0, slippage 0, fee 0, fees 0, funding 0, leverage 0, spread 0, impact 0, turnover 0, capacity 0, maker 0, taker 0, latency 0, fill 0, fills 0, borrow 0, liquidation 0, open interest 0, rebalance 0, bootstrap 0, out-of-sample 0, walk-forward 0, survivorship 0, look-ahead 0, repaint 0, cooldown 0, order 0, orders 0, volume 0. The words `profit` (11) and `stop loss` (4) occur only in prose about profit-taking and stop-loss behaviour, `backtest` occurs once (the `/*backtest ...*/` header), the Chinese terms 盈利/止盈/止损 occur only in the Chinese prose, and `pyramiding` occurs once (the declaration). There is no performance table, no equity curve, no trade list and no figure anywhere in the artifact.

What the source does report:

- Configuration only, from the pinned header: backtest start 2022-12-08 00:00:00, end 2023-12-14 00:00:00, `period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`.
- Parameter defaults as listed under Signal, plus the eight exposed Strategy parameters in the artifact's own Strategy Arguments table (`v_input_int_1` 3, `v_input_int_2` 19, `v_input_float_1` 3, `v_input_int_3` 100, `v_input_bool_1` true, `v_input_bool_2` true, `v_input_1` timestamp(1 Jan 2021), `v_input_2` timestamp(1 Jan 2022)), three of which are inert as recorded above.
- Qualitative claims only, verbatim: "Accurate entry, tracking strengths", "Reasonable profit-taking, ensuring partial profits", "Timely stop loss, controlling risks", and "the accuracy of cross signals needs improvement and profit targets and stop loss mechanisms require further optimization". None carries a sample, a metric, a baseline or a figure → unverifiable as printed and recorded as bare claims, not as evidence; two of them are already recorded as contradictions.
- Landing metadata read 2026-10-05: Created 2023-12-15 16:10:24, Last modified "3 years ago", Copy 3, Hits 927, 0 comments. A word-boundary scan of the landing's tag-stripped text for `net profit`, `sharpe`, `roi`, `max drawdown`, `profit factor`, `total closed trades`, `win rate`, `annualized`, `sortino`, `equity curve`, `trade list`, `strategy tester` and `backtest results` returned 0 hits each, and the Chinese performance terms returned 0 hits each.
- Research-computed, not printed: the header window spans 2022-12-08 to 2023-12-14 inclusive, i.e. 371 days between the printed endpoints and 372 calendar days inclusive, which on a 24/7 market is about 372 completed 1d bars; this is our arithmetic on the printed dates and must not be read as a source-reported sample size.

No source-reported figure in this record comes from any other paper, article or repository; every claim is attributed to the single pinned artifact above.

### Independently reproduced

not independently reproduced

Only the following were performed: SHA-256 checksumming of the pinned artifact, of its whitespace-collapsed variant, of its Pine block and of its header-stripped body; git blob hashing; byte-for-byte comparison of the Pine text embedded in the FMZ landing payload against the mirror block after trailing-newline normalisation; byte-identity comparison of the header-stripped bodies of the two sibling mirror entries; extraction and line counting of the Pine block; a whole-artifact term and word-boundary census; enumeration of `strategy.*` call sites; retrieval of the public FMZ landing page over HTTPS; a hidden-inclusive dedup scan with positive controls; and record-side enumeration of the printed header values. No market data was downloaded, no backtest was run, no Pine or third-party code was executed, and no statistic was recomputed from data.

### Negative evidence

1. The artifact prints zero performance numbers, so there is nothing to reproduce: sharpe, sortino, drawdown, cagr, roi, net profit, profit factor, win rate, annualized, strategy tester and total closed trades are all 0 occurrences.
2. The four qualitative performance claims are unaccompanied by any sample, metric or baseline, so they cannot be checked as printed.
3. The only configured backtest window is 2022-12-08 to 2023-12-14, about 372 1d bars on a single instrument, with no train/test split, no out-of-sample section and no walk-forward.
4. The source's own Conclusion states that "the accuracy of cross signals needs improvement and profit targets and stop loss mechanisms require further optimization, which are the main problems and improvement directions."
5. No risk layer of any kind: stop loss, take profit, trailing stop and time exit are absent from the code (`strategy.exit`, `strategy.stop`, `strategy.limit` and `strategy.cancel` all 0 for real order purposes), while the strings `stop loss` and 止损 appear only in prose.
6. The rule can never cut a loss: the only exit requires `close > position_avg_price * 1.03`, so a position that never reaches a 3 percent cushion is held indefinitely, with no instruction in the code capable of closing it.
7. The source's own Optimization Directions block proposes adding more indicators, dynamic profit targets and dynamic stop losses, i.e. the published rule is explicitly presented as a starting point; the Conclusion says exactly that.
8. The rule is long-only with no short side at all (`strategy.short` 0), so it carries no hedging path and its performance in a falling market is realized only as cash.
9. Single indicator family, single parameter cell (3 / 19 / 100) with no sensitivity analysis anywhere in the source; three of the eight declared inputs are inert, so the strategy's real parameter surface is smaller than the artifact advertises.
10. The source's own Risks section states that "purely relying on simple indicators like golden dead crosses to determine trends can lead to some inaccurate signals" and that "Price action patterns can be more accurate in complex environments."
11. Recorded contradiction 1: the date-window inputs and the Strategy Arguments table advertise a start/end control that the code never reads.
12. Recorded contradiction 2: the prose describes an unconditional fixed-percentage take-profit exit that the code does not contain.
13. Recorded contradiction 3: the prose advertises timely stop-loss behaviour that the code's profit gate makes impossible below +3 percent.
14. The full source is behind `Login to view full source` on the FMZ landing and is publicly reachable only through a third-party mirror repository, leaving a single point of provenance.
15. The mirror repository ships no LICENSE file, so the redistribution status of the mirror as a whole is not stated in source; only the script's own MPL-2.0 notice line is printed inside the block.
16. Authorship is layered and unverified: the mirror records `Author: ChaoZhang`, the code prints `// © Ta3MooChi`, the FMZ landing names the `ChaoZhang` account, the strategy's own title inside the code is the untranslated Korean word `전략`, and none of these identities is independently confirmed; peer-review status is not stated in source.
17. There is no repository, no version tag, no test suite, no issue tracker and no changelog for the rule; the FMZ landing shows a single "Last modified" timestamp.
18. FMZ landing statistics (Copy 3, Hits 927, 0 comments as read 2026-10-05) show modest community adoption, and no third-party study of this exact artifact was identified.
19. The base-K-line field `basePeriod: 1h` in the header sits next to a `1d` decision period; although the script contains no `request.*` call and therefore no cross-timeframe dependency, a reader could mistake the header for a multi-timeframe design.
20. Two mirror entries carry byte-identical rule bodies with different FMZ backtest headers (FMZ 435513 at `period: 1d`, FMZ 430773 at `period: 1h`); only the 1d entry is claimed here, but a reader who consults the other landing page would obtain a different decision horizon from identical code.
21. The script's strategy title is `전략` ("strategy"), which conveys no identity, so the artifact must be identified by its FMZ id, its mirror path and its byte digests rather than by the title.
22. Language-default reliance: `default_qty_type`, `default_qty_value`, `initial_capital`, `currency`, `slippage`, `commission_type`, `commission_value`, `calc_on_order_fills`, `calc_on_every_tick`, `close_entries_rule`, `max_bars_back`, `use_bar_magnifier`, `backtest_fill_limits_assumption`, `risk_free_rate`, `calc_bars_count`, `margin_long` and `margin_short` are all absent from the declaration. Each has exactly one documented v5 default and is recorded as source-declared-by-language-default, but a reimplementation that silently adopts different values would not be 1:1. Gated by F3.
23. The two official pages disagree on the `pyramiding` default (the v5 reference prints 0, the v5 Strategies page prints 1); this does not affect this artifact because `pyramiding = 100` is declared explicitly, and the disagreement is recorded only to show that the default was not relied upon.
24. The official reference prints `commission_value` default 0 while the strategy declares no commission at all, so the backtest this record describes is a zero-cost backtest; any positive fee is a research assumption introduced only by gate F4.
25. No independent replication, no competing study and no contrary external evidence specific to this artifact was identified; absence of contrary literature is not evidence of robustness.

## Falsification plan

All thresholds below are `research-defined falsification threshold` values chosen by this Scout; none of them is source-reported. All test inputs (data vendor, sample window, benchmark definitions, cost model) are `research-proposed` test scaffolding and are not part of the strategy rule.

- **F1 — Semantic reconstruction gate.** Threshold: an independent reimplementation of the pinned rule must reproduce, on a reference OHLCV series, the identical `short_ma`, `long_ma` and `trend_ma` series, the identical `na`-availability boundary (first non-`na` entry condition at bar index 100) and an identical ordered list of entry bars and close bars, with zero differing bars. Action: any mismatch means the record is not 1:1 reconstructible and must be withdrawn from admission review rather than repaired by interpretation.
- **F2 — Causality and repaint audit.** Threshold: every input used at bar `t` must be dated at or before `t` (`close[t]`, `short_ma[t]`, `long_ma[t]`, `trend_ma[t]`, `trend_ma[t-1]`, the `[1]` crossover terms, `position_avg_price[t]`), with zero occurrences of future bars, negative shifts, `timenow`, session recalculation, `request.*`, `security`, `calc_on_order_fills=true`, `calc_on_every_tick=true`, `use_bar_magnifier=true` or any lower-timeframe request. Action: any future reference found ⇒ NOT_LOSSLESS, close the record.
- **F3 — Engine-default audit gate.** Threshold (research-defined): the executing engine must confirm every recorded language default end to end — order size exactly 1 unit (fixed, equity-independent), initial capital 1,000,000, account currency equal to the chart currency, slippage 0 ticks, commission 0 percent on both the entry and the closing fill, `close_entries_rule="FIFO"`, `margin_long=0` and `margin_short=0` with no position-size cap and no liquidation, `pyramiding=100`, `process_orders_on_close=true`, `calc_on_order_fills=false`, `calc_on_every_tick=false`, fill price equal to the decision bar's close, and `strategy.close_all` liquidating the whole position in one market order. Action: fail if any recorded default differs from the documented v5 value, or if a v6 (rather than v5) semantics set is applied to this v5 source (the v6 migration guide changes the margin default to 100). Fail ⇒ record is not 1:1 under the pinned baseline and must not be admitted.
- **F4 — Cost ladder.** Threshold (research-defined): apply 0 / 1 / 2 / 5 / 10 bps per side on top of the source's own zero commission and zero slippage, plus a funding accrual leg for the perpetual; fail if net annualized return turns non-positive at 2 bps per side of additional cost, or net Sharpe falls to 0 or below at 5 bps per side. Action: fail ⇒ the edge is cost-dependent, record remains research-only and must not be proposed for any adoption.
- **F5 — Parameter perturbation.** Threshold (research-defined): sweep the triple (short 3, long 19, trend 100) over {(2,13,60), (3,19,100), (5,20,100), (5,30,150), (8,40,200), (3,19,200)} with everything else frozen; fail if the sign of net return over the full sample flips away from the published cell (3,19,100) in more than half of the five non-published cells, or if the published cell is not in the upper half of the six by net return. Action: fail ⇒ parameter-lottery diagnosis, no adoption.
- **F6 — Regime breakdown.** Threshold (research-defined): split the sample into thirds by trailing 60-day realized volatility and, separately, by a 100-day ADX(14) trend-strength tercile; fail if net Sharpe is negative in at least two of three terciles in either split. Action: fail ⇒ the rule requires a regime gate that the source does not contain, so it cannot be admitted as-is and must stay research-only.
- **F7 — Always-in-market placebo.** Threshold (research-defined): compare against buy-and-hold BTCUSDT on the identical window and against 1000 random entry sequences that preserve the observed number of entries and the observed holding-time distribution; fail if the observed net Sharpe does not exceed the 95th percentile of the placebo distribution. Action: fail ⇒ no evidence that the cross timing carries information.
- **F8 — Trend-filter ablation.** Threshold (research-defined): re-run the frozen rule with `use_trend_ma = true` (the published default) and with `use_trend_ma = false`, the source's own declared toggle; fail if the published cell does not beat the untrended cell by more than 0.15 net Sharpe after costs at 2 bps per side, or if only the untrended cell is positive. Action: fail ⇒ the advertised "only when the major trend is up" gate carries no value, the record stays research-only with that finding attached.
- **F9 — Out-of-sample requirement.** Threshold (research-defined): at least 5 years of 1d BTCUSDT bars with a frozen chronological split and no re-tuning; fail if out-of-sample net Sharpe is 0 or below. Action: fail ⇒ reject for adoption; do not rescue by re-tuning.
- **F10 — Cross-instrument generalization.** Threshold (research-defined): run the identical frozen rule on ETHUSDT perpetual and on one further major perpetual chosen before inspection; fail if 0 of 2 produce positive net return after costs at 2 bps per side. Action: fail ⇒ single-asset overfit diagnosis.
- **F11 — Capacity and liquidity.** Threshold (research-defined): fail if the required notional at the 100-unit pyramiding cap exceeds 5 percent of the trailing 30-day median daily volume of the instrument. Action: fail ⇒ capacity-capped, record the ceiling and block any size scaling.
- **F12 — Multiplicity control.** Threshold (research-defined): apply Benjamini-Hochberg at q = 0.10 across the full F5 × F8 × F10 cell family; fail if the published cell does not survive. Action: fail ⇒ treat the published configuration as one draw among many, no adoption.
- **F13 — Unclosed-position gate.** Threshold (research-defined): measure the share of the evaluation sample spent long while the open position is below the 3 percent exit cushion, and the maximum underwater duration so produced; fail if any single position remains below the cushion for more than 25 percent of the sample window or if the maximum drawdown of the rule exceeds 40 percent. Action: fail ⇒ the missing loss-exit (Negative evidence 6) makes the holding path unacceptable as-is, record stays research-only and no stop may be added to "fix" it, because adding one would change the source rule.
- **F14 — Frozen forward window.** Threshold (research-defined): forward test from 2026-10-05 to 2027-10-04 with every parameter frozen; fail if forward net Sharpe at 2 bps per side is 0 or below. Action: fail ⇒ reject; no parameter may be changed to re-run it.

Global no-retuning rule: `short_ma = ta.sma(close, 3)`, `long_ma = ta.sma(close, 19)`, `trend_ma = ta.sma(close, 100)`, `use_trend_ma = true`, `inTradeWindow = true`, `longStopPerc = 1 + 3 * 0.01`, the golden-cross entry and the dead-cross-plus-3-percent `strategy.close_all()` exit, the long-only direction, `pyramiding 100`, fixed 1-unit sizing, `process_orders_on_close` same-bar-close fills, commission 0, slippage 0, initial capital 1,000,000, the single `1d` timeframe and the BTCUSDT perpetual instrument are frozen. No gate may be rescued by changing a parameter, widening a window, switching vendor, dropping a cost leg or re-defining a metric after seeing results.

## Crypto portability

`direct` — with a narrow meaning. The cited source itself is configured on Binance USDT-margined BTCUSDT futures at `period: 1d`, so the instrument, venue and market type are already crypto and no porting change is required to express the rule. `direct` refers only to mechanism, signal and instrument applicability; it is explicitly not a claim of crypto performance, which is `unproven` because the artifact prints no result.

Portability-relevant facts:

- The rule consumes only `close` (and `strategy.position_avg_price` while in a position), available on any 24/7 crypto venue; there is no session, holiday or opening-auction dependency, and no time value enters the decision.
- No funding, open interest, mark or index price, liquidation feed, order book, aggressor side, on-chain data or options input is used, so none of those crypto-specific inputs can invalidate the signal.
- Because the short side is never used, spot, margin and perpetual are all expressible; the pinned header nevertheless configures a margined futures venue, and the perpetual funding accrual that a real perpetual position would incur is never mentioned by the source (`data gap`).
- Risks that remain crypto-specific and unmodeled by the source: perpetual funding accrual, the choice of mark versus last price for valuation (`data gap`), contract specification and tick-size differences between venues (`data gap`), listing and delisting churn for anything other than BTCUSDT (`data gap`), venue fragmentation and custody risk (`data gap`), liquidity and market-impact differences at the 100-unit sizing cap (`data gap`), and the zero-cost assumption the source itself makes (`data gap`).
- Candle boundaries are exchange-defined daily candles; the record does not assume any other boundary convention, and 24/7 trading means a "daily" bar closes at 00:00 UTC on Binance rather than at an exchange session close.

Crypto portability is not authorization to trade and not evidence that the mechanism survives in crypto.

## Limitations

- `not independently reproduced`. Nothing in this record has been recomputed from data.
- `data gap`: no spread, impact, latency, funding, fill-failure or missing-data model, no capacity statement, no exact contract pin, no account-currency pin, no commission or slippage model, no performance output.
- `underspecified`: the precise Binance contract (perpetual versus dated future), the quote-currency detail under `currency.NONE`, and whether FMZ's backtest engine honored the same v5 language defaults as the TradingView reference (the script itself makes no cross-timeframe call).
- `unproven`: profitability, robustness, regime robustness, cross-instrument robustness, capacity and forward performance.
- Source-quality limitation: a single community mirror entry with no repository, no tests, no versioning, no peer review, layered and unverified authorship, a Korean placeholder title, and a landing page that hides the full source behind a login.
- Reproducibility limitation: because FMZ hides the full source and prints no results, the only immutable, publicly auditable artifact is the mirror at the pinned SHA, and there is no way to verify any performance intuition about the rule.
- Identification limitation: the rule is price-only and unfalsified; nothing in the source separates cross timing from a beta or from a drawdown-carrying exposure, and there is no risk layer to bound the loss path.
- Structural limitation: three of the eight advertised inputs are inert and the only exit is profit-gated, so the rule as written is a long-only trend entry with an uncapped holding path (Negative evidence 6, gate F13).
- Publication-bias limitation: a public strategy mirror selects for presentable, not for robust; Copy 3 and 0 comments suggest no demonstrated community reuse.
- Incremental-write check: this is the first record in the repository for this source identity after the 2026-10-04 pool reset, the pre-write probe set returned 0 matches against `main` and both open research PRs, and no Wiki Brain page exists for it, so this is not ordinary duplicate material.
- A three-item contradiction set is recorded in frontmatter. All three are internal to one artifact (controls versus code, prose versus code on take-profit, prose versus code on stop-loss); in every case the pinned code is the executable and unambiguous text, so none of them leaves the signal itself ambiguous.

## Implementation status

`not-implemented`. Nothing has been implemented in our research stack. No Pine was executed, no backtester was run, no Hummingbot package or `dev-2.17.0` backtest was attempted, no Qlib job was created, no indicator was coded, and no Paper, Testnet or Live workflow was touched. The only artifacts produced by this run are this Markdown record and its verification script.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. Presence of this record does not mean: passed LOSSLESS HB_READY review; merged to `main`; entered Hermes Wiki Brain; entered any candidate pool; completed a Hummingbot or Qlib full backtest; became a survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for Paper; approved for Testnet; approved for Live. HB_READY itself, if it were ever granted, means semantic and backtest expressibility only. No record may promote itself by wording, evidence count, confidence or schedule behavior.

## Related Wiki records

No Wiki Brain page exists for this source identity, and this run writes none. The following existing pages were checked on disk and are related by mechanism family or by execution and validation discipline rather than by source identity; none of them shares the golden/death-cross source, the price moving-average crossover signal, or the long-only BTCUSDT 1d scope:

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

- https://github.com/fmzquant/strategies — pinned commit `7853bb2bf262c4567ac238d3552d97f0e50cb801`, path `金叉死叉趋势追踪策略Golden-Dead-Cross-Trend-Tracking-Strategy.md`; the complete primary source read end to end on 2026-10-05, SHA-256 `5b0869c40fcacc8c564e7657580cea40f5bc25144322703aa7317b44f64acf35`.
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E9%87%91%E5%8F%89%E6%AD%BB%E5%8F%89%E8%B6%8B%E5%8A%BF%E8%BF%BD%E8%B8%AA%E7%AD%96%E7%95%A5Golden-Dead-Cross-Trend-Tracking-Strategy.md — percent-encoded form of the same pinned file.
- https://www.fmz.com/strategy/435513 — FMZ landing page of the pinned source, read 2026-10-05; confirms title, type, author account, creation timestamp, description, backtest header, eight exposed parameters, Copy/Hits/comment statistics, the `Login to view full source` gate, and the full Pine text embedded in the page payload.
- https://www.fmz.com/strategy/430773 — sibling FMZ entry of the same script at `period: 1h`, read 2026-10-05; used only to demonstrate that the two mirror bodies are byte-identical and that the difference between them is the decision timeframe, which this record does not claim.
- https://www.tradingview.com/pine-script-reference/v5/#fun_strategy — official first-party v5 reference used for `strategy()` parameter defaults (`pyramiding`, `default_qty_type`, `default_qty_value`, `initial_capital`, `currency`, `slippage`, `commission_type`, `commission_value`, `process_orders_on_close`, `close_entries_rule`, `calc_on_order_fills`, `calc_on_every_tick`, `margin_long`, `margin_short`), for `strategy.entry`, `strategy.close_all`, `strategy.position_avg_price`, `ta.sma`, `ta.crossover` and `ta.crossunder` semantics.
- https://www.tradingview.com/pine-script-docs/v5/concepts/strategies/ — official first-party v5 documentation used for the broker emulator and its intrabar assumption, `calc_on_every_tick`, `calc_on_order_fills`, `process_orders_on_close`, position sizing, commission and slippage behaviour, `strategy.close_all`, and the `pyramiding = 20` "up to 20 entries per position" statement.
- https://www.tradingview.com/pine-script-docs/v5/language/script-structure/ — official first-party documentation of the `//@version=5` compiler-annotation form and of the rule that an omitted annotation defaults to version 1.
- https://www.tradingview.com/pine-script-docs/migration-guides/to-pine-version-6/ — official first-party v5-to-v6 migration guide used for "The when parameter is removed from all applicable strategy.*() functions", for "The default long and short margin percentage for strategies is now 100. In v5, the default value of the margin_long and margin_short parameters is 0, which means that the strategy does not check its available funds before creating or managing orders. It can create orders that require more money than is available", and for the v5 boolean-na rule "When implicitly cast to 'bool', na is evaluated as false".
