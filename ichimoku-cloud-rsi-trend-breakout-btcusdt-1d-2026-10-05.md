---
schema: strategy-research-record-v1
title: Ichimoku Cloud and RSI trend-breakout reversal system on BTCUSDT 1d bars
created: 2026-10-05
updated: 2026-10-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-09-21
sources:
  - https://github.com/fmzquant/strategies
  - https://www.fmz.com/strategy/427447
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}entry
  - https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}rsi
  - https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}rma
  - https://www.tradingview.com/pine-script-reference/v5/#var_time
  - https://www.tradingview.com/pine-script-docs/v5/language/declaration-statements/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Strategy prose states the long entry fires when Tenkan-sen crosses above Kijun-sen and the short entry when it crosses below, but the pinned code contains no crossing test at all: it uses the level comparisons tenkan > kijun and tenkan < kijun."
  - "Strategy prose states that Chikou Span must be above / below the cloud, but the pinned code never compares the Chikou span to the cloud; it uses ta.mom(close, cs_offset-1) > 0 / < 0, i.e. close against its own value 25 bars earlier."
  - "Strategy prose Advantage item 5 asserts the rule is 'Risk managed by stop profit/loss' and the Risk / Optimization sections repeatedly discuss stop profit/loss, but the pinned code contains no stop loss, take profit, trailing stop or time exit of any kind; the Optimization block proposes adding them as future work."
  - "Strategy prose states 'Close position when reverse signal occurs'. In the pinned code the only strategy.close calls are guarded by not short_entry and not long_entry, which are false at the declared input defaults (Long Entry = true, Short Entry = true), so neither call ever places an order; the executable exit path is the opposite-side strategy.entry reversal."
---

# Ichimoku Cloud and RSI trend-breakout reversal system on BTCUSDT 1d bars

## Provenance

Immutable GitHub source (this is the primary source actually read end to end):

- Repository URL: https://github.com/fmzquant/strategies
- Full commit SHA: `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit date 2025-04-30 03:10:28Z, subject `update`). Confirmed as the repository head at research time by `GET https://api.github.com/repos/fmzquant/strategies/commits/HEAD`, which returned exactly this SHA.
- Exact file path: `一目均衡表与RSI组合策略Ichimoku-Cloud-and-RSI-Combination-Strategy.md` (the non-ASCII filename is preserved verbatim; percent-encoded blob URL recorded under Sources).
- Git blob SHA of that path inside that commit: `94882de296ae79a5df7e81a52a00c1cd673a1513`, blob size 7679 bytes.
- Relevant source URL recorded inside the artifact: https://www.fmz.com/strategy/427447

Primary-source checksums pinned 2026-10-05 from a shallow clone of that single commit:

- File 7679 bytes, SHA-256 `102e6614d54d852c5166b09aec43e58be272ba3173fc890ff5f177afb609ed45`, 6408 characters, 212 lines.
- Whitespace-collapsed variant 5569 characters, SHA-256 `3b715dc1982cb0482d062e3a75857ee914fa5f97b61db61ef6de01077c622d9f`.
- The fenced Pine block alone: 2664 characters, 77 newline characters, SHA-256 `5acacf1527654da1783f7c0933c8a76240a23b88ed9be6665b2061b00fc2478a`.
- The blob was additionally downloaded through the GitHub Git Data API and compared byte-for-byte against the local clone: identical.

Artifact structure as printed: `> Name` (一目均衡表与RSI组合策略Ichimoku-Cloud-and-RSI-Combination-Strategy), `> Author` = ChaoZhang, `> Strategy Description` (a Chinese section set and an English set inside one `[trans]` block, no image), `> Strategy Arguments` table (8 rows), `> Source (PineScript)` fenced block preceded by an FMZ `/*backtest ...*/` header, `> Detail` = https://www.fmz.com/strategy/427447, `> Last Modified` = 2023-09-21 10:52:13.

Licence and rights: the pinned Pine block prints `// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/` and the author credit `// © Coinrule`. The mirror repository ships no LICENSE file, so the redistribution status of the mirror as a whole is not stated in source; this record therefore cites and normalizes the rule and reproduces no source code block.

FMZ landing page read directly on 2026-10-05 (HTTP 200, no login required for the description layer): HTML `<title>` `Ichimoku Cloud and RSI Combination Strategy | FMZ`, author account `ChaoZhang`, `Created: 2023-09-21 10:52:13`, `Last modified: 3 years ago`, `Copy: 3`, `Hits: 1641`, and the literal gate `Login to view full source`, so the complete source is publicly reachable only through the GitHub mirror at the pinned SHA. The landing shows no performance table, no equity curve and no trade list: the artifact contains no `![IMG]` block, and the only five `fmz.com/upload/asset/*.png` references in the page payload are payment/UI icons (Balance, Voucher, Stripe, USDT, Paypal).

FMZ backtest header printed verbatim inside the pinned artifact:

```text
start: 2022-09-14 00:00:00
end: 2023-09-20 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
```

Provenance gaps (stated, not repaired): no DOI, no version tag, no repository, no test suite, no issue tracker entry, no peer-review statement and no performance output anywhere; peer-review status is not stated in source.

Pre-write dedup (2026-10-05): a hidden-inclusive search of the whole working tree for `ichimoku`, `Ichimoku`, `一目均衡` and `427447` returned 0 matches. `gh pr list --state open` returned `[]` and `git ls-remote --heads origin 'research/*'` returned only the seven already-closed or already-merged branches of PRs #5, #6, #7, #9, #10, #12 and #17, so the dedup set of open `research/*` PRs is empty. `origin/main` was at `ada0718` and contains four strategy records, from FMZ strategy ids 430857 (Bookstaber volatility system), 427070 (Gann HiLo Activator), 440338 (P-Signal erf reversal) and 430552 (VIDYA momentum trend) — none of them shares this artifact's source identity, and none implements an Ichimoku cloud state machine. The three closed research PRs used other sources and other mechanisms: LazyBear Wave Trend (PR #6), FMZ 435513 + 430773 golden/dead moving-average crosses (PR #10) and FMZ 433919 MACD histogram zero-cross (PR #17). Five-axis distinction against all of them: mechanism, signal construction, universe, horizon and material data dependency differ (this record is a cloud-breakout plus RSI-side filter on `1d` BTCUSDT).

## Economic mechanism

### Source-reported

The source states the mechanism only descriptively; it gives no behavioural, structural or risk-premium channel.

- Overview: "This strategy combines Ichimoku Cloud and Relative Strength Index (RSI) indicators to determine trend direction and enter positions when a trend starts. It generates trading signals when the three Ichimoku lines align in valid combinations together with RSI signals."
- Strategy Logic, as printed: (1) calculate Tenkan-sen, Kijun-sen, Chikou Span lines of Ichimoku Cloud; (2) calculate RSI values; (3) go long when Tenkan-sen crosses above Kijun-sen, Chikou Span above cloud, price breaks out above cloud, and RSI below 50; (4) go short when Tenkan-sen crosses below Kijun-sen, Chikou Span below cloud, price breaks down cloud, and RSI above 50; (5) close position when reverse signal occurs.
- "Specifically, it combines Ichimoku Cloud's trend analysis with RSI's overbought-oversold gauge. Entry signals are generated when Ichimoku lines align in trend start formation, and RSI shows no overbought-oversold condition. RSI filters help avoid false breakout during consolidation. Exits follow Ichimoku reverse FORMATION completely."
- Advantages, as printed: combining RSI improves entry accuracy; Ichimoku Cloud has strong trend following capacity; signals are simple and intuitive; customizable parameters fit different cycles; "Risk managed by stop profit/loss".
- Risks, as printed: Ichimoku Cloud may lag, causing false breakouts; requires parameter optimization, otherwise inaccurate signals; long holding introduces overnight risk; RSI prone to false signals; risks of being trapped on reversals. "Risks can be managed via parameter optimization, stop profit/loss tuning, limiting holding period etc."
- Optimization, as printed: test different line and RSI parameters; introduce trailing stop loss; evaluate limiting trading hours; study parameter preferences across products; test adding re-entry and pyramiding rules; compare different stop profit/loss strategies.
- Summary, as printed: "Pros are simple intuitive signals and high ROI; Cons are lags and trapped risks."

Four of those printed statements contradict the pinned code and are recorded in frontmatter `contradictions`: the crossing claim, the Chikou-versus-cloud claim, the stop-profit/loss claim, and the "close on reverse signal" claim. In every case the pinned code is the executable and unambiguous text.

### Research interpretation

Falsifiable mechanism hypothesis: daily BTC returns exhibit short-horizon trend persistence, and a close that sits above the displaced Tenkan/Kijun midpoint range while price is also above the displaced 52-bar cloud marks a confirmed local drift; the 25-bar price momentum term is a lagged Chikou-style confirmation that the current close is higher than it was one cloud offset ago; the RSI(14) side filter then enters only while RSI is still on the non-extended side of its midpoint, i.e. it buys strength that has not yet been labelled overbought and sells weakness that has not yet been labelled oversold. Candidate behavioural channels are slow diffusion of directional information in a 24/7 market with no closing auction, and anchoring of new entrants to the cloud as a visible support/resistance reference. This is a ported technical-analysis hypothesis: the source supplies no economic rationale and no evidence, so the mechanism is research interpretation, not source-reported fact.

Component roles, stated plainly because the source offers no composite structure:

- Regime / trend state: the four-level Ichimoku comparison set — `tenkan` versus `kijun`, `close` versus the displaced cloud envelope (`ss_high` / `ss_low`), and `close` versus `close[25]`.
- Entry signal: the AND of that regime with the RSI-side filter and the calendar gate.
- Confirmation filter: `RSI < 50` for the long leg and `RSI > 50` for the short leg, a dead-band-free 50-level test rather than the classic 30/70 bands.
- Risk / exit: none. The source declares no stop, target, trailing or time exit; the only exit is the opposite-side entry.

No component is assumed to contribute alpha; ablation is required by the falsification plan. `bullish` and `bearish` are mutually exclusive by construction, and because the two `strategy.close` calls are unreachable at the declared input defaults, once the first entry fills the system is always long or always short: a full-time directional exposure rule rather than a conditional-allocation rule. That property is derived from the pinned code, not asserted by the prose.

## Signal

Everything below is read from the pinned Pine block. Nothing in this section is `research-proposed`.

**Formation timestamp and tradability**

- Decision series: completed `1d` bars of the pinned instrument (the `period: 1d` value in the pinned backtest header).
- Inputs at decision bar `t`: `close[t]`, `close[t-25]`, `high` and `low` over the windows enumerated below, `tenkan[t]`, `kijun[t]`, `senkouA[t-25]`, `senkouB[t-25]`, `RSI[t]`, and `time[t]`.
- Order timing: the only two order-creating commands are `strategy.entry` market orders; the declaration sets `process_orders_on_close=true`, so an order created while evaluating bar `t` fills at the close of bar `t`. This is exactly a completed-bar decision with same-bar-close execution; there is no next-bar-open fill anywhere in the rule.
- Intra-bar recalculation: `calc_on_every_tick` and `calc_on_order_fills` are absent from the pinned declaration (token count 0 in the Pine block). Official v5 documentation states both default to `false`, i.e. exactly one evaluation per completed bar. Recorded as source-declared-by-language-default.
- Calendar gate, exact: `timePeriod = time >= timestamp(syminfo.timezone, 2022, 6, 1, 0, 0)`. The built-in `time` variable is documented as "Current bar time in UNIX format … the timestamp based on the time of the bar's open". `timestamp(timezone, ...)` and `timestamp(syminfo.timezone, ...)` are first-party reference overloads, and `syminfo.timezone` is documented as "Timezone of the exchange of the chart main series", so the time zone is resolved from the pinned instrument rather than left to a chart default. On Binance, daily klines open at 00:00 UTC (verified below), so the gate first opens on the `2022-06-01` daily bar; a hypothetical exchange time zone west of UTC would move the gate by at most one daily bar, bounded under F7.

**Lookback, formulas and warmup**

- Declared inputs, verbatim: `ts_bars = input.int(9, minval=1, title="Tenkan-Sen Bars")` → 9; `ks_bars = input.int(26, minval=1, ...)` → 26; `ssb_bars = input.int(52, minval=1, ...)` → 52; `cs_offset = input.int(26, minval=1, ...)` → 26; `ss_offset = input.int(26, minval=1, ...)` → 26; `long_entry = input(true, title="Long Entry")` → true; `short_entry = input(true, title="Short Entry")` → true; `showDate = input(defval=true, title='Show Date Range')` → true (inert: the identifier occurs only on its declaration line). `lengthRSI = 14` is a literal, not an input.
- Cloud primitives, exact: `middle(len) => math.avg(ta.lowest(len), ta.highest(len))`, where the first-party reference states that the one-argument overload of `ta.lowest` "uses low as a source series" and of `ta.highest` "uses high as a source series", and that "na values in the source series are ignored". `math.avg` is documented as "Average" of the given series. Therefore `tenkan = (lowest(low,9) + highest(high,9)) / 2` over bars `t-8..t`, `kijun` over `t-25..t`, `senkouB` over `t-51..t`, and `senkouA = (tenkan + kijun) / 2` at `t`.
- Cloud envelope, exact: `ss_high = math.max(senkouA[ss_offset-1], senkouB[ss_offset-1])` and `ss_low = math.min(...)` with `ss_offset-1 = 25`.
- Chikou-style term, exact: `cs_cross_bull = ta.mom(close, cs_offset-1) > 0` with `cs_offset-1 = 25`. The reference defines `ta.mom` as "source - source[length]", i.e. `close[t] - close[t-25]`.
- RSI, exact: `RSI = ta.rsi(close, 14)`. The reference prints the implementation `u = math.max(x - x[1], 0)`, `d = math.max(x[1] - x, 0)`, `rs = ta.rma(u, y) / ta.rma(d, y)`, `res = 100 - 100 / (1 + rs)`, and `ta.rma` is documented as "the exponentially weighted moving average with alpha = 1 / length" whose printed example seeds with `ta.sma(src, length)`. Both remarks state the functions "calculate on the length quantity of non-na values", so `RSI` first becomes defined at bar index 13 (index 14 under an `na`-only first difference).
- Warmup, derived from the pinned code because the source declares none: `tenkan` from index 8, `kijun` from 25, `senkouA` from 25, `senkouB` from 51, `senkouA[25]` from 50, `senkouB[25]` from 76, `ta.mom(close,25)` from 25, `RSI` from 13/14. The two `math.max` / `math.min` envelope calls are the only places where an `na` operand meets a language function whose `na` rule the reference does not print: under `na` propagation `ss_high` / `ss_low` first define at index 76, under an `na`-ignoring reading at index 50. Both readings therefore agree from index 76 onward.
- Earliest tradable bar: the calendar gate requires `time >= 2022-06-01 00:00 UTC`. On the pinned full-history Binance USDT-M `BTCUSDT` 1d series (first bar 2019-09-08) that is bar index 997, which is more than 900 bars past the latest of the warmup bounds above, so every gate-eligible bar is identical under both `na` readings and under both RSI first-index readings. Research-computed, not source-reported; see Evidence.
- `max_bars_back` is not declared; the deepest history reference is `senkouB[25]` combined with a 52-bar window, i.e. 76 bars.

**Entry**

- Long entry: `bullish and long_entry and RSI < 50 and timePeriod`, expanded: `tenkan > kijun` AND `close - close[25] > 0` AND `close > ss_high` AND `RSI < 50` AND `time >= 2022-06-01 00:00` (exchange time zone) AND `long_entry == true`.
- Short entry: `bearish and short_entry and RSI > 50 and timePeriod`, expanded: `tenkan < kijun` AND `close - close[25] < 0` AND `close < ss_low` AND `RSI > 50` AND the same gate AND `short_entry == true`.
- Both conditions are mutually exclusive — `tenkan > kijun` and `tenkan < kijun` cannot hold together — so conflict priority is provably irrelevant, and at most one entry order can be created per bar.
- Ties: `tenkan == kijun` satisfies neither leg; `close == close[25]` satisfies neither leg; equality with the 50 RSI level satisfies neither leg. Equality therefore produces no order, which is fully defined.
- Both `when=` conditions are evaluated per completed bar; official reference text for `strategy.entry` makes the order not be created when `when` is false.

**Exit**

- The pinned code contains exactly four order commands: two `strategy.entry` and two `strategy.close`. Censuses over the whole Pine block: `strategy.exit` 0, `strategy.stop` 0, `strategy.order` 0, `strategy.cancel` 0, `strategy.close_all` 0, `strategy.position_avg_price` 0, `strategy.position_size` 0.
- `strategy.close("Long", when = bearish and not short_entry)` and `strategy.close("Short", when = bullish and not long_entry)` are unreachable at the declared input defaults, because `short_entry` and `long_entry` default to `true`. The record pins the defaults printed by the artifact's `Strategy Arguments` table (`Long Entry|true`, `Short Entry|true`); the calls are recorded as source-declared inputs, not as research choices.
- Therefore the only executable exit is the opposite-side `strategy.entry`. Official reference text for `strategy.entry` states that an order in the opposite direction of the current market position reverses that position, and official documentation states the reversed position size equals the order size, so one same-bar-close fill closes the open trade and opens the opposite trade at the new order's 30%-of-equity size.
- Stop loss: none. Take profit: none. Trailing stop: none. Time limit or maximum holding period: none. Flat / all-cash state after the first entry: unreachable.

**Holding period, overlap and re-entry**

- Holding period: unbounded and determined entirely by the persistence of the regime; the source states no maximum or expected holding period.
- Maximum same-side concurrency: 1. `pyramiding` is not written in the declaration (token count 0), so the value comes from the language default, and both official statements of that default describe the same observable rule even though they print different numbers: the v5 reference states "The maximum number of entries allowed in the same direction. If the value is 0, only one entry order in the same direction can be opened, and additional entry orders are rejected … The default is 0", while the declaration-statements page prints "The default argument is 1". Under each document's own definition the result is identical — one open same-side entry, further same-side entries rejected — so the record records `pyramiding` as source-declared-by-language-default with that behavioural convergence stated rather than silently picking one number, and F3 forces the executing engine to confirm it.
- Same-direction re-entry: rejected while the position is open; to return to the original side the rule must first pass through an opposite-side entry, so a same-side add is unreachable rather than merely discouraged.
- Cooldown: none declared, and Pine's v5 strategy declaration exposes no cooldown field. Because every trigger is a per-bar boolean with mutually exclusive legs, cooldown semantics are provably irrelevant rather than missing.
- Re-entry after a full exit: the "exit" is itself an entry, so there is no flat interval other than the bars before the first entry.

**Parameters, sizing and pyramiding**

- Pinned declaration, read from the source and normalized to one line for readability (the source prints it across eight lines): `strategy("Ichimoku Cloud with RSI (By Coinrule)", overlay=true, initial_capital=1000, process_orders_on_close=true, default_qty_type=strategy.percent_of_equity, default_qty_value=30, commission_type=strategy.commission.percent, commission_value=0.1)`. So the code-declared values are `overlay=true` (display only), `initial_capital=1000`, `process_orders_on_close=true`, `default_qty_type=strategy.percent_of_equity`, `default_qty_value=30`, `commission_type=strategy.commission.percent`, `commission_value=0.1`.
- Declaration parameters the code leaves unset, each recorded as source-declared-by-language-default with the official page that documents it: `pyramiding` (default discussed above, with the 0-versus-1 documentation conflict recorded), `currency=currency.NONE` ("in which case the chart's currency is used"), `slippage=0`, `calc_on_order_fills=false`, `calc_on_every_tick=false`, `close_entries_rule="FIFO"` (irrelevant: no id-scoped close command ever fires), `max_bars_back` auto-detected, `use_bar_magnifier=false`, `backtest_fill_limits_assumption` not applicable (no price-dependent orders exist).
- Sizing: each entry order is 30% of current strategy equity at order time → compounding, not fixed.
- Two official pages disagree on two unset defaults and both conflicts are recorded rather than resolved: (i) `pyramiding` — 0 versus 1, immaterial here for the convergence reason above; (ii) `margin_long` / `margin_short` — the v5 reference prints "Optional. Default is 0, in which case the strategy does not enforce any limits on position size" while the declaration-statements page prints "The default margin_long and margin_short arguments are 100 … 100% margin is equivalent to 1:1 leverage". Materiality analysis for this rule: the order size is capped by construction at 30% of current equity, and 30% of equity is always fully collateralised under the 100% margin reading, so both readings produce identical fills at every equity level; F3 forces the executing engine to confirm it.
- Direction: both sides explicit. The short leg makes spot inapplicable, so the declared market type is perpetual (see Required data).

**Reconstruction status**

Every field required to replay the rule — indicator variant, source prices, lookback, smoothing, thresholds, comparison direction, state transitions, conflict priority, direction, entry, exit, risk semantics, sizing, pyramiding, concurrency, cooldown, timeframe, fill timing and warmup — is explicit either in the pinned source or in official first-party documentation of the pinned source's own language defaults. The residual `underspecified` items are: the exact Binance contract (perpetual versus dated future), the exchange time zone of the `2022-06-01` gate to within one daily bar, the `na` rule of `math.max` / `math.min` (bounded below the gate by more than 900 bars), the account currency under `currency.NONE`, and the cost/latency/fill-failure model. None of them alters the signal, and all are recorded as `data gap` or bounded `underspecified` rather than filled.

## Required data

- Instrument: BTCUSDT on Binance USDT-margined futures, taken verbatim from the pinned header `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`. Single pair, single instrument, no basket, no ranking, no cross-sectional step.
- Market type: perpetual. The source explicitly runs on a margined futures venue and the rule shorts, so a margined long/short instrument is required. The artifact does not distinguish the perpetual from a dated future, which is `data gap`; it is immaterial to an OHLCV-only signal but must be pinned before any execution work.
- Spot applicability: not applicable to the short leg, because spot would require naked shorting. The long leg alone could run on spot, but that would be a modified strategy and is not proposed.
- Venue: Binance only. No cross-venue state, no venue-selection rule, no listing or survivorship rule (the artifact states none).
- Timeframe: exactly one decision timeframe, `1d`, from `period: 1d`. The same header prints `basePeriod: 1h`; the pinned script contains 0 `request.*` calls and 0 `security(` calls, so no lower- or higher-timeframe series is referenced by the rule and there is no multi-timeframe dependency to align. `use_bar_magnifier` is at its documented `false` default, so no lower-timeframe data is used for fills either.
- Fields used: `high`, `low` and `close` of the decision bar and of lags up to 76 bars back, plus bar `time` for the calendar gate. `open` occurs 0 times in the Pine block, and `volume` occurs 0 times in the whole artifact, so neither enters the rule.
- Fields not required and not used, each absent from the pinned artifact: open interest, funding, mark or index price, basis, order book or depth, trade or aggressor feed, liquidation feed, on-chain data, options or Greeks, sentiment or news, macro series, cross-venue state, borrow data, margin state.
- Point-in-time: every input at bar `t` is contemporaneous or lagged (`close[t-25]`, `senkouA[t-25]`, `senkouB[t-25]`, `RSI[t]`, `time[t]`); there is no future reference, no negative shift, no future extrema, no full-sample normalization, no `timenow` (0 occurrences), and no `security` call of any kind, so the pinned rule contains no look-ahead leakage. The displaced `plot(..., offset=ss_offset-1)` and `plot(close, offset=-cs_offset+1)` calls are chart rendering only and touch no order.
- Timestamp and timezone: bar open time compared with `timestamp(syminfo.timezone, 2022, 6, 1, 0, 0)`. `syminfo.timezone` is the exchange time zone of the chart's main series, and the pinned instrument is a Binance symbol whose daily bars open at 00:00 UTC (verified on public klines), so the gate boundary is the 2022-06-01 00:00 UTC daily open. Residual: a non-UTC exchange time zone would move the gate by at most one daily bar; bounded under F7, recorded `underspecified`.
- Missing data: no gap, halt or stale-bar handling is specified anywhere in the source → `data gap`. Imputation would be `research-proposed` and is not proposed here.
- Funding, fee and spread needs: only a commission is declared. Word-boundary census of the 6408-character artifact gives commission 0 (the tokens are `commission_type` / `commission_value`, counted separately in the Pine block as 3), slippage 0, fee 0, funding 0, leverage 0, margin 0, spread 0, impact 0, turnover 0, capacity 1 (inside the prose phrase "strong trend following capacity"), open interest 0, liquidat 0. These are `data gap`, never a modeled zero.

## Execution assumptions

Source-declared (quoted or read from the pinned declaration):

- Order type: market order, created only by `strategy.entry`. There is no limit order, no stop order and no conditional order anywhere in the rule (the reference states `strategy.close` "always generates market orders", and those calls never fire anyway).
- Fill model: `process_orders_on_close=true` → the order created while evaluating bar `t` is filled at the close of bar `t`; `calc_on_every_tick` and `calc_on_order_fills` default to `false` per official documentation, so there is exactly one evaluation per completed bar. Completed-bar decision with same-bar-close execution.
- Signal-to-order delay: none. The order is created and filled in the same completed-bar close.
- Reversal semantics: an opposite-direction `strategy.entry` produces one fill that closes the open trade and opens the opposite trade at the order size (30% of equity at order time), per official `strategy.entry` documentation.
- Position limits: one position at a time; 30% of current equity per entry; `pyramiding` at its documented default (one open same-side entry); no scaling, grid or martingale layer.
- Leverage and margin: absent from the declaration; the two documented defaults are both recorded above and converge for a 30%-of-equity order, so the source assumes no borrowed-funds dependency and no unsupported leverage effect.
- Shorting and borrow: the source assumes a margined futures venue. Borrow availability is not addressed → `data gap`; spot shorting is explicitly out of scope.
- Costs: `commission_type=strategy.commission.percent`, `commission_value=0.1` is declared, i.e. 0.1% per side per filled order. No slippage, no spread, no market-impact and no funding model appears anywhere in the artifact → `data gap`. The source's own simulated results therefore embed undeclared engine defaults, which the source never states; this record does not adopt them as a validated zero-cost assumption.
- Latency: not modeled in source → `data gap`.
- Participation and capacity: not modeled in source → `data gap`; tested by the research-defined gate F10.
- Failure handling (partial fills, rejects, downtime): not addressed in source → `data gap`. The pinned rule places whole market orders only, and no partial-fill-dependent condition exists.
- Scout-vs-source split: every item above marked source-declared comes from the pinned declaration, the pinned code or official TradingView documentation. Nothing in this section is a Scout-added execution rule; every pass/fail cutoff used later is labeled `research-defined`.

## Evidence

### Source-reported

The artifact prints no performance result of any kind. Word-boundary census over the pinned 6408-character artifact: sharpe 0, drawdown 0, cagr 0, return 0, win rate 0, annualized 0, trade 0, trades 0, fee 0, funding 0, leverage 0, margin 0, spread 0, impact 0, turnover 0, equity 0, curve 0, roi 1, profit 4 (all inside "stop profit/loss" prose), stop loss 1, trailing 1, backtest 1 (inside the `/*backtest*/` header). There is no `**backtest**` image block, no equity curve, no trade list, no table and no figure anywhere in the artifact, and the landing page shows none either.

What the source does report:

- Configuration only, from the pinned header: backtest start 2022-09-14 00:00:00, end 2023-09-20 00:00:00, `period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`.
- Parameter defaults as listed under Signal, plus the eight exposed Strategy parameters (Show Date Range, Tenkan-Sen Bars, Kijun-Sen Bars, Senkou-Span B Bars, Chikou-Span Offset, Senkou-Span Offset, Long Entry, Short Entry) confirmed in the artifact table.
- One qualitative performance claim, verbatim: "Pros are simple intuitive signals and high ROI", carrying no sample, no metric, no baseline and no figure → unverifiable as printed and recorded as a bare claim, not as evidence.
- Landing metadata read 2026-10-05: Created 2023-09-21 10:52:13, Last modified "3 years ago", Copy 3, Hits 1641.
- Research-computed, not printed: the header window spans 2022-09-14 to 2023-09-20, i.e. about 371 calendar days and therefore roughly 371 daily bars on a 24/7 market; this is our arithmetic on the printed dates and must not be read as a source-reported sample size.

No source-reported figure in this record comes from any other paper, article or repository; every claim is attributed to the single pinned artifact above.

### Independently reproduced

not independently reproduced

Only the following were performed: SHA-256 and git-blob checksumming of the pinned artifact and of its Pine block, whitespace-normalization digests, a whole-artifact and Pine-block term census, enumeration of `strategy.*` call sites, reading of the public FMZ landing page, bar-index arithmetic for the warmup bounds, a read-only reachability check of the `ta.rsi` degenerate divisor against public Binance USDT-M `BTCUSDT` 1d klines (2585 bars, 2019-09-08 to 2026-10-05), and a check that those daily klines open exactly on the UTC day boundary. No market data was used to evaluate the strategy, no backtest was run, no Pine or third-party code was executed, and no performance statistic was recomputed from data.

### Negative evidence

1. The artifact prints zero performance numbers, so there is nothing to reproduce: sharpe, drawdown, cagr, return, win rate and trade counts are all 0 occurrences.
2. The single performance claim ("high ROI") is unaccompanied by any sample, metric or baseline, so it cannot be checked as printed.
3. The only configured backtest window is about one year (2022-09-14 to 2023-09-20) on a single instrument, with no train/test split, no out-of-sample section and no walk-forward.
4. No slippage, spread, impact or funding model at all; only a declared 0.1% commission, so any edge claim is only partly priced.
5. No risk layer of any kind: stop loss, take profit, trailing stop and time exit are all absent from the code, while the source's own prose claims the rule is "Risk managed by stop profit/loss" and its Optimization block proposes adding a trailing stop as future work (contradiction 3).
6. The source's own Risks block states the rule "Requires parameter optimization, otherwise inaccurate signals", "RSI prone to false signals" and "Risks of being trapped on reversals".
7. The source's own Summary block presents the rule as a template with "Cons are lags and trapped risks".
8. Prose claims a Tenkan/Kijun crossing entry; the code uses a level test (contradiction 1).
9. Prose claims a Chikou-versus-cloud condition; the code uses a 25-bar price momentum test (contradiction 2).
10. Prose claims the position is closed by a reverse Ichimoku formation; in the code the reverse formation closes only the opposite side's entry id, and both `strategy.close` calls are dead at the declared defaults (contradiction 4).
11. The `Show Date Range` input is inert: `showDate` is declared and never read, while the real gate uses a hard-coded `2022-06-01` timestamp, so the advertised date-range control does nothing.
12. The RSI filter direction is counter-intuitive — long only while `RSI < 50`, short only while `RSI > 50` — so the rule deliberately enters on the weak side of the 50 level and never uses the 30/70 levels its own prose evokes.
13. After the first entry the system is never flat, so it carries permanent long-or-short exposure with no cash fallback and no drawdown control.
14. Holding period is unbounded and the only exit requires the opposite regime plus the opposite RSI side, so a position can persist for an arbitrary number of bars if the two never coincide.
15. The lookback mix is asymmetric (a short 9-bar Tenkan against a 52-bar Senkou B and a 25-bar displacement), which mechanically makes the cloud lag far more than the trigger line.
16. The full source is behind a login on the FMZ landing and is publicly reachable only through a third-party mirror repository, leaving a single point of provenance.
17. The mirror repository ships no LICENSE file, so the redistribution status of the mirror as a whole is not stated in source; only the script's own MPL-2.0 notice and `© Coinrule` credit are printed inside the block.
18. Authorship is layered and unverified: the mirror records `Author: ChaoZhang`, the code prints `// © Coinrule`, and neither identity is independently confirmed; peer-review status is not stated in source.
19. There is no repository, no version tag, no test suite, no issue tracker and no changelog for the rule; the FMZ landing shows a single "Last modified" timestamp.
20. FMZ landing statistics (Copy 3, Hits 1641 as read 2026-10-05) show weak community adoption, and no third-party study of this exact artifact was identified.
21. The base-K-line field `basePeriod: 1h` sits next to a `1d` decision period; although the script contains no `request.*` call and therefore no cross-timeframe dependency, a reader could mistake the header for a multi-timeframe design.
22. The `2022-06-01` gate timezone is resolved from `syminfo.timezone` rather than written literally, so a non-UTC exchange time zone would move the first eligible bar by at most one daily bar; `underspecified`, gated by F7.
23. The exact Binance contract (perpetual versus dated future) is not distinguished by the source, and no missing-data, halt or partial-fill handling is specified.
24. The `na` handling of `math.max` / `math.min` is not printed in the first-party reference, so the first defined bar of the cloud envelope is either 50 or 76; both are more than 900 bars before the gate, so the tradable sequence is identical, but the ambiguity itself is a documented first-party gap.
25. `pyramiding` and `margin_long` / `margin_short` defaults are stated inconsistently by two official pages; both conflicts are recorded rather than chosen, and both converge for this rule's parameters (see Signal).
26. No independent replication, no competing study and no contrary external evidence specific to this artifact was found; absence of contrary literature is not evidence of robustness.

## Falsification plan

All thresholds below are `research-defined falsification threshold` values chosen by this Scout; none of them is source-reported. All test inputs (data vendor, sample window, benchmark definitions, cost model) are `research-proposed` test scaffolding and are not part of the strategy rule.

- **F1 — Semantic reconstruction gate.** Threshold: an independent reimplementation of the pinned rule must reproduce, on a reference OHLCV series, the identical `tenkan`, `kijun`, `senkouA`, `senkouB`, `ss_high`, `ss_low`, `RSI` and `bullish` / `bearish` series and an identical ordered list of entry bars and sides (exact match, zero differing bars, first possible entry at the bar where the gate first opens). Action: any mismatch means the record is not 1:1 reconstructible and must be withdrawn from admission review rather than repaired by interpretation.
- **F2 — Causality and repaint audit.** Threshold: every input used at bar `t` must be dated at or before `t` (`close[t-25]`, `senkouA[t-25]`, `senkouB[t-25]`, `RSI[t]`, `time[t]`), with zero occurrences of future bars, negative shifts, `timenow`, session recalculation, or any lower-timeframe request. Action: any future reference found ⇒ NOT_LOSSLESS, close the record.
- **F3 — Engine-default audit gate.** Threshold (research-defined): the executing engine must confirm every recorded declaration and language default end to end — order size exactly 30% of equity (`percent_of_equity` 30, compounding), fill price equal to the decision bar's close, 0.1% commission on both the entry and the reversing fill, 0 ticks slippage, once-per-bar evaluation, same-side entries rejected while a position is open under the resolved `pyramiding` default, and identical fills under both `margin_long` / `margin_short` documented defaults. Action: fail if any recorded value differs from the record, or if `pyramiding` resolves to something other than "one open same-side entry, no adds"; fail ⇒ pin the discrepancy in writing and keep research-only, no adoption.
- **F4 — Cost ladder.** Threshold (research-defined): apply 0 / 1 / 2 / 5 / 10 bps per side plus a commission leg and, for the perpetual, a funding accrual leg; fail if net annualized return turns non-positive at 2 bps per side or net Sharpe falls to 0 or below at 5 bps per side. Action: fail ⇒ the edge is cost-dependent, record remains research-only and must not be proposed for any adoption.
- **F5 — Parameter perturbation.** Threshold (research-defined): sweep `Tenkan-Sen Bars` over 5, 9, 13, 21, `Kijun-Sen Bars` over 13, 26, 52, `Senkou-Span B Bars` over 26, 52, 104, `Chikou-Span Offset` over 13, 26, 52 and the RSI window over 7, 14, 21 with everything else frozen; fail if the sign of net return over the full sample flips for the published cell or if fewer than half of the swept cells produce positive net return. Action: fail ⇒ parameter-lottery diagnosis, no adoption.
- **F6 — Regime breakdown.** Threshold (research-defined): split the sample into thirds by trailing 60-day realized volatility (low / mid / high) and, separately, by a 60-day ADX(14) trend-strength tercile; fail if net Sharpe is negative in at least two of three terciles in either split. Action: fail ⇒ the rule requires a regime gate that the source does not contain, so it cannot be admitted as-is and must stay research-only.
- **F7 — Gate and warmup sensitivity.** Threshold (research-defined): run the frozen rule with the calendar gate resolved at UTC and again shifted by one daily bar, and with the cloud-envelope `na` rule set to each of its two readings; fail if the entry sequence differs on any bar other than the single displaced gate bar, or if total net PnL differs by more than 5% between the two gate readings. Action: fail ⇒ the result depends on an unpinned boundary convention, record must be re-pinned from source before any adoption.
- **F8 — Always-in-market placebo.** Threshold (research-defined): compare against buy-and-hold BTCUSDT on the identical window and against 1000 random flip sequences that preserve the observed holding-time distribution; fail if the observed net Sharpe does not exceed the 95th percentile of the placebo distribution. Action: fail ⇒ no evidence that the regime-flip timing carries information.
- **F9 — Filter ablation.** Threshold (research-defined): re-run with the RSI side filter removed, with the `close[25]` momentum term removed, and with the cloud condition removed, all other parameters frozen; fail if no ablated variant is worse than the full rule by at least 0.2 net Sharpe after costs at 2 bps per side. Action: fail ⇒ the added components are decorative and the record is a generic trend rule, keep research-only.
- **F10 — Capacity and liquidity.** Threshold (research-defined): fail if required notional at 30% of equity exceeds 5% of the trailing 30-day median daily volume of the instrument. Action: fail ⇒ capacity-capped, record the ceiling and block any size scaling.
- **F11 — Out-of-sample requirement.** Threshold (research-defined): at least 5 years of 1d BTCUSDT bars with a frozen chronological split and no re-tuning; fail if out-of-sample net Sharpe is 0 or below. Action: fail ⇒ reject for adoption; do not rescue by re-tuning.
- **F12 — Multiplicity control.** Threshold (research-defined): apply Benjamini-Hochberg at q = 0.10 across the full F5 × F11 cell family; fail if the published cell does not survive. Action: fail ⇒ treat the published configuration as one draw among many, no adoption.
- **F13 — Frozen forward window.** Threshold (research-defined): forward test from 2026-10-05 to 2027-10-04 with every parameter frozen; fail if forward net Sharpe at 2 bps per side is 0 or below. Action: fail ⇒ reject; no parameter may be changed to re-run it.

Global no-retuning rule: `Tenkan 9`, `Kijun 26`, `Senkou B 52`, `Chikou offset 26`, `Senkou offset 26`, `RSI 14` with the 50 level, the cloud-breakout and momentum AND-set, the reversal-only exit, `pyramiding` at its documented default, 30% percent-of-equity compounding sizing, `process_orders_on_close` same-bar-close fills, 0.1% commission, the single `1d` timeframe, the BTCUSDT perpetual instrument and the `2022-06-01` gate are frozen. No gate may be rescued by changing a parameter, widening a window, switching vendor, dropping a cost leg or re-defining a metric after seeing results.

## Crypto portability

`direct` — with a narrow meaning. The cited source itself configures the rule on Binance USDT-margined BTCUSDT futures at `period: 1d`, so the instrument, venue and market type are already crypto and no porting change is required to express the rule. `direct` refers only to mechanism, signal and instrument applicability; it is explicitly not a claim of crypto performance, which is `unproven` because the artifact prints no result.

Portability-relevant facts:

- The rule consumes only `high`, `low`, `close` and bar time, all available on any 24/7 crypto venue; there is no session, holiday or opening-auction dependency, and the one calendar test is a plain bar-time comparison.
- No funding, open interest, mark or index price, liquidation feed, order book, aggressor side, on-chain data or options input is used, so none of those crypto-specific inputs can invalidate the signal.
- Shorting requires a margined instrument; the source already uses a futures venue, so the perpetual is the natural target and spot is out of scope for the short leg.
- The calendar gate is evaluated in the exchange time zone of the symbol, so on a 24/7 venue the boundary is a plain UTC daily open rather than a session boundary.
- Risks that remain crypto-specific and unmodeled by the source: perpetual funding accrual (never mentioned, `data gap`), the choice of mark versus last price for valuation (`data gap`), contract specification and tick-size differences between venues (`data gap`), listing and delisting churn for anything other than BTCUSDT (`data gap`), venue fragmentation and custody risk (`data gap`), and liquidity or market-impact differences at 30%-of-equity sizing (`data gap`).
- Timestamp and candle boundaries are exchange-defined UTC daily bars on Binance; the record does not assume any other boundary convention, and the one-bar gate sensitivity is bounded under F7.

Crypto portability is not authorization to trade and not evidence that the mechanism survives in crypto.

## Limitations

- `not independently reproduced`. Nothing in this record has been recomputed from data as a performance claim.
- `data gap`: no slippage, latency, funding, spread, impact, fill-failure, missing-data, capacity, exact-contract, account-currency or performance statement.
- `underspecified`: the exact Binance contract; the `2022-06-01` gate time zone to within one daily bar; the `na` rule of `math.max` / `math.min` (bounded more than 900 bars below the gate); whether the FMZ backtest engine's `basePeriod: 1h` field influenced any published number (the script itself makes no cross-timeframe call).
- `unproven`: profitability, robustness, regime robustness, cross-instrument robustness, capacity and forward performance.
- Source-quality limitation: a single community mirror entry with no repository, no tests, no versioning, no peer review and a layered, unverified authorship; the landing hides the full source behind a login.
- Reproducibility limitation: because FMZ hides the full source and prints no results, the only immutable, publicly auditable artifact is the mirror at the pinned SHA, and there is no way to verify the claim of high ROI.
- Identification limitation: the rule is price-only and unfalsified; nothing in the source separates cloud-trend timing from a beta or from a drawdown-carrying always-in-market exposure.
- Publication-bias limitation: a public strategy mirror selects for presentable, not for robust, and Copy 3 suggests little demonstrated community reuse.
- Incremental-write check: this is the first record in the repository for this source identity, no Wiki Brain page exists for it, and no open `research/*` PR covers it, so this is not ordinary duplicate material.
- A four-item contradiction set is recorded in frontmatter. All four are prose-versus-code conflicts inside one artifact, and in every case the pinned code is the executable and unambiguous text, so none of them leaves the signal itself ambiguous.

## Implementation status

`not-implemented`. Nothing has been implemented in our research stack. No Pine was executed, no backtester was run, no Hummingbot package or `dev-2.17.0` backtest was attempted, no Qlib job was created, no indicator was coded, and no Paper, Testnet or Live workflow was touched. The only artifacts produced by this run are this Markdown record and the read-only verification scripts behind it.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. Presence of this record does not mean: passed LOSSLESS HB_READY review; merged to `main`; entered Hermes Wiki Brain; entered any candidate pool; completed a Hummingbot or Qlib full backtest; became a survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for Paper; approved for Testnet; approved for Live. HB_READY itself, if it were ever granted, means semantic and backtest expressibility only. No record may promote itself by wording, evidence count, confidence or schedule behavior.

## Related Wiki records

No Wiki Brain page exists for this source identity, and this run writes none. The following existing pages were checked on disk and are related by mechanism family or by execution and validation discipline rather than by source identity; none of them shares the Ichimoku Cloud + RSI source, the cloud-breakout signal, or the BTCUSDT `1d` single-pair scope:

- [[quant/crypto-perpetual-supertrend-wpr-trend-following-cost-gate-falsification-2026-09-12]]
- [[quant/tradingview-volume-weighted-supertrend-dual-confirmation-2026-09-16]]
- [[quant/tradingview-proborsa-rsi-supertrend-double-dip-strategy-2026-08-24]]
- [[quant/tradingview-choppiness-donchian-breakout-filter-2026-09-16]]
- [[quant/crypto-perpetual-regime-aligned-right-tail-trend-cost-hurdle-2026-09-13]]
- [[quant/crypto-walk-forward-window-optimization-double-oos-momentum-2026-09-04]]
- [[quant/gt-score-anti-overfitting-objective-multi-metric-gate-2026-09-05]]

## Sources

- https://github.com/fmzquant/strategies — pinned commit `7853bb2bf262c4567ac238d3552d97f0e50cb801`, path `一目均衡表与RSI组合策略Ichimoku-Cloud-and-RSI-Combination-Strategy.md`, git blob `94882de296ae79a5df7e81a52a00c1cd673a1513`; the complete primary source read end to end on 2026-10-05, SHA-256 `102e6614d54d852c5166b09aec43e58be272ba3173fc890ff5f177afb609ed45`.
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E4%B8%80%E7%9B%AE%E5%9D%87%E8%A1%A1%E8%A1%A8%E4%B8%8ERSI%E7%BB%84%E5%90%88%E7%AD%96%E7%95%A5Ichimoku-Cloud-and-RSI-Combination-Strategy.md — percent-encoded form of the same pinned file.
- https://www.fmz.com/strategy/427447 — FMZ landing page, read 2026-10-05; confirms title, author account, creation timestamp, English and Chinese description, exposed parameters, and that the full source requires login.
- https://www.tradingview.com/pine-script-reference/v5/#fun_strategy — official first-party language reference used only for declaration-parameter semantics and defaults (`pyramiding` 0 with its rejection rule, `default_qty_type` / `default_qty_value`, `initial_capital`, `currency` `currency.NONE`, `slippage` 0, `commission_*`, `process_orders_on_close`, `close_entries_rule` "FIFO", `calc_on_order_fills` / `calc_on_every_tick` defaults false, `margin_long` / `margin_short` printed as 0, `max_bars_back`, `use_bar_magnifier`).
- https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}entry — official first-party documentation for pyramiding rejection of same-direction entries, for opposite-direction entries reversing the position, and for the `when` argument.
- https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}rsi , https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}rma — official first-party documentation for the printed `pine_rsi` implementation (`rs = ta.rma(u, y) / ta.rma(d, y)`, `res = 100 - 100 / (1 + rs)`), for the `ta.rma` seeding via `ta.sma(src, length)`, and for the "length quantity of non-na values" remarks used to derive warmup.
- https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}mom , https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}lowest , https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}highest , https://www.tradingview.com/pine-script-reference/v5/#fun_math{dot}avg — official first-party documentation for `source - source[length]`, for the one-argument `ta.lowest` / `ta.highest` overloads (low / high as source, `na` ignored) and for `math.avg`.
- https://www.tradingview.com/pine-script-reference/v5/#var_time , https://www.tradingview.com/pine-script-reference/v5/#fun_timestamp , https://www.tradingview.com/pine-script-reference/v5/#var_syminfo{dot}timezone — official first-party documentation that `time` is the bar's open time in UNIX milliseconds, that `timestamp(timezone, ...)` and `timestamp(syminfo.timezone, ...)` are reference overloads, and that `syminfo.timezone` is "Timezone of the exchange of the chart main series".
- https://www.tradingview.com/pine-script-docs/v5/language/declaration-statements/ — official first-party documentation used only for the `process_orders_on_close = true` fill semantics, the once-per-bar execution rule when the calculation flags are false, and the conflicting `pyramiding` (1) and `margin_long` / `margin_short` (100) default statements recorded above.
