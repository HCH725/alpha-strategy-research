---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: EMA 7/20 cloud-alignment trend system on BTCUSDT 1d bars
created: 2026-10-07
updated: 2026-10-07
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2022-05-17
sources:
  - https://www.fmz.com/strategy/363835
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}entry
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}close
  - https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}ema
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The prose description says the strategy 'closes all trades by the end of the trading day' and is intraday (best on SPY 30m), but the pinned executable block contains no session, date, or end-of-day exit of any kind and the FMZ backtest block pins `period: 1d` on `BTC_USDT`. The code governs: there is no time exit, and the record pins the 1d decision timeframe."
  - "The declaration sets `margin_long=100, margin_short=100` (full-margin, no leverage) while the `i_trdQty` trade-quantity input is never read by any order call; both are source-declared sizing trivia, event-neutral, and replaced downstream by the standard house execution overlay."
---

# EMA 7/20 cloud-alignment trend system on BTCUSDT 1d bars

## Provenance

Primary source read end to end (FMZ strategy page mirror plus live re-verification):

- FMZ strategy: https://www.fmz.com/strategy/363835 (`EMA-Cloud-Intraday-Strategy`, author ChaoZhang mirror of `© rwestbrookjr`, `//@version=5`, MPL-2.0 header).
- Last modified (as printed on the page): 2022-05-17.
- FMZ backtest block pinned on the page: `start: 2022-04-16`, `end: 2022-05-15`, `period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]` — single pair, 1d decision timeframe.
- Live verification this run (2026-10-07): the page re-fetched over HTTPS (728646 bytes, SHA-256 `e5cc7b3624df4017c13d03f8a951621b6100a7490a58bd359732c49dac53ff5d`) embeds the Pine source (unicode-escaped) whose entry/exit block — `longCondition`, both `strategy.entry` lines, `longExit = close[1] < fastEMA`, `shortExit = close[1] > fastEMA`, both `strategy.close` lines, and the two commented-out `strategy.exit` lines — is character-identical to the mirror file (`f00270.md`, 2673 bytes). The executable rule below is read from those verified lines.
- Mirror executable block: 81 non-comment lines — one `strategy()` declaration, three `input.*` declarations, two `ta.ema` assignments, three plot/fill display lines, four signal booleans, two `strategy.entry` calls, two `strategy.close` calls, two commented-out `strategy.exit` lines (comments, not code).

Licence and rights: this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

Pre-write dedup (2026-10-07): a working-tree search for `363835`, `rwestbrookjr` and `EMA Cloud` returned 0 matches; the closest record on `main` is `ema-20-50-cross-btcusdt-1h-2026-10-06.md` (Forven EMA 20/50 pure-crossover, long-only, 1h, window-gated). Five-axis distinction: mechanism differs (close-vs-fast plus fast-vs-slow alignment AND versus a single 20/50 cross event), signal construction differs (two strict-inequality conjunctions with `close[1]`-based fast-average exits versus `ta.crossover`/`ta.crossunder` with a cross-down exit), horizon differs (`1d` versus `1h`), source identity differs (FMZ 363835 rwestbrookjr versus the Forven script), and direction differs (two-sided versus long-only). Also distinguished from the closed PR #6 (LazyBear Wave Trend) and PR #10 (golden/dead cross) by the same construction and source differences. `gh pr list --state open` shows only PR #36 (reconstruction lane, no `research/*` collision).

## Economic mechanism

### Source-reported

- As printed: the 9/20 (defaults overridden to 7/20 by inputs, see Signal) exponential averages form "a colored cloud ... similar to what is seen on the Ichimoku Cloud". Entry is when price closes above a green cloud (fast above slow) or below a red cloud; exit is when price closes against the fast average or at end of day (the end-of-day leg exists only in prose — contradiction 1, the code has no such exit).
- No sample, no metric, no baseline, no figure and no performance number of any kind is printed anywhere in the artifact; the single backtest screenshot carries no readable numbers. Nothing numerical is recorded below.

### Research interpretation

Falsifiable mechanism hypothesis: on a single 24/7 crypto instrument, requiring the close to sit outside a fast/slow EMA alignment (rather than trading every cross of the two averages) buys a persistence filter with positioning instead of lag — a close beyond the fast leg while the fast leg itself leads the slow leg marks drift strong enough to clear both the level and the ordering, and such clears exhibit short-horizon continuation because breakout and trend-following flow unwinds only partially within one daily bar; losing the fast average on the prior close marks the failure of the same auction and cuts the trade. The bet is continuation after alignment absorption, not mean reversion. The 7/20 pair sets a fast trend scale with a hair-trigger exit. This is a ported technical-analysis hypothesis: the source supplies no behavioural argument, no sample and no evidence, so the mechanism is research interpretation, not source-reported fact.

Component roles, stated plainly:

- Primary signal: strict inequalities of the current close against the two EMAs (`close[t] > fastEMA[t]` with `fastEMA[t] > slowEMA[t]` to enter long; mirror for short).
- Noise filter: the alignment leg itself (both inequalities must hold jointly); there is no confirmation lag and no second filter.
- Trend / regime filter: none beyond the 7/20 EMA scale.
- Direction gate: none — both legs are unconditionally live (two-sided rule).

## Signal

Everything below is read from the verified Pine block at pinned source defaults (`i_trdQty = 10` unread, `fastLen = 7`, `slowLen = 20`). Nothing in this section is `research-proposed`.

**Formation timestamp and tradability**

- Decision series: completed `1d` bars of `Futures_Binance BTC_USDT` (record-pinned single decision timeframe; the script is timeframe-agnostic — 0 `request.*`, 0 `security(`, 0 `timeframe` references, 0 `input.timeframe` — so exactly one decision timeframe is declared by this record, `1d`, with no multi-timeframe dependency).
- Inputs at decision bar `t`: `close[t]`, `close[t-1]` (exits only), `fastEMA[t]`, `slowEMA[t]`. `open`, `high`, `low`, `volume` are never read by the trading logic (`volume` occurs 0 times in the whole block; the three plot/fill lines render the two averages and the cloud fill only and feed no order).
- Order timing: the live order calls are two `strategy.entry` and two `strategy.close`, all market orders (no `limit`/`stop` arguments anywhere — 0 occurrences of each; the two `strategy.exit` lines are `//` comments), and the declaration sets `process_orders_on_close=true`. Per official first-party documentation this is exactly a completed-bar decision with same-bar-close execution; no next-bar-open fill exists anywhere in the rule.
- Recalculation: neither `calc_on_every_tick` nor `calc_on_order_fills` appears in the declaration (0 occurrences of each); both default to `false` per official documentation. Recorded as source-declared-by-language-default; no intrabar re-evaluation can create a second order on the same bar.
- No date gate, no session gate, no calendar read of any kind (`dayofweek`, `hour`, `timenow`, `time(` occur 0 times). The rule is always active.

**Lookback, formulas and warmup**

- Parameters as declared: `fastLen = input(title = "Fast EMA Length", defval = 7)` → 7; `slowLen = input(title = "Slow EMA Length", defval = 20)` → 20. (The prose mentions 9/20, but the code defaults — which govern — are 7/20.)
- Formulas, exact: `fastEMA = ta.ema(close, 7)`, `slowEMA = ta.ema(close, 20)` — first-party EMA over close, no variant choice, no smoothing choice, no source-price choice left open.
- Derived conditions, exact:
  - Long entry: `longCondition = (close > fastEMA and fastEMA > slowEMA)`, live via `if (longCondition)` → `strategy.entry("Long_Entry", strategy.long)`.
  - Long exit: `longExit = close[1] < fastEMA`, live via `if (longExit)` → `strategy.close("Long_Entry", when=longExit)` (the `if` and the redundant `when` test the same boolean; both must hold, which is exactly the boolean).
  - Short entry: `shortCondition = (close < fastEMA and fastEMA < slowEMA)` → `strategy.entry("Short_Entry", strategy.short)`.
  - Short exit: `shortExit = close[1] > fastEMA` → `strategy.close("Short_Entry", when=shortExit)`.
- The rule contains 0 `crossover`, 0 `crossunder`, 0 `ta.cross`: all four legs are strict inequalities, so exact equality on any comparison fires neither leg — the tie case is defined, not ambiguous.
- Warmup, derived from the pinned code because the source declares none: the longest lookback is 20 (`slowEMA`); strict comparisons against an unsettled average evaluate to no-order, so the earliest possible order is the first bar on which the inequalities hold with settled inputs (no later than 20 bars in). `max_bars_back` is not declared; no lag beyond `close[t-1]` is referenced.

**Entry**

- Long entry: `strategy.entry("Long_Entry", strategy.long)` on the long conjunction. Short entry: `strategy.entry("Short_Entry", strategy.short)` on the short conjunction. Both omit `qty` (uses the declaration sizing, recorded under Execution assumptions), both omit `limit`/`stop` (market orders).

**Exit**

- Pinned code census: 2 `strategy.entry`, 2 `strategy.close`, 0 `strategy.close_all`, 0 `strategy.exit` (live), 0 `strategy.order`, 0 `strategy.stop`, 0 `strategy.cancel`, 0 `strategy.risk.*`, 0 `strategy.position_*`. The two commented `strategy.exit` trail lines are dead comments, not alternative exits.
- Stop loss: none. Take profit: none. Trailing stop: none. Time limit / maximum holding period: none (the prose end-of-day exit is absent from code — contradiction 1). Flat state is reachable before the first entry and after every fast-average exit; the system is otherwise positioned long or short.
- A `strategy.close` on a flat position (e.g. an exit bar with no open entry) is a deterministic no-op.

**Holding period, overlap and re-entry**

- Holding period: unbounded, determined entirely by waiting for the next `close[1]`-vs-fast-average breakdown; the source states no maximum or expected holding period.
- Maximum same-side concurrency: 1. `pyramiding` is not written in the declaration (0 occurrences), so the value comes from the language default — one open same-side entry, further same-side entries rejected (the same default-convergence the PASS reviews of earlier records accepted; the executing engine must confirm it).
- Same-direction re-entry: after an exit the system is flat, so the next conjunction bar opens a fresh position; while positioned, a further same-side signal is rejected under the default above, and orders fill on the same bar they are created, so no unfilled order survives into the next bar. No cooldown exists. Opposite-side entry while positioned reverses the position (single engine position, two ids) — the reversal path is fully specified by the two live entry legs.
- No `position_size`, `position_avg_price`, `openprofit` or `opentrades` reference exists anywhere in the block (verified by full read), so no position-aware state conditions any signal or exit.

**Conflict priority (explicit, from source code order)**

- Opposite-side entries are mutually exclusive by construction (`close[t]` cannot be both strictly above and strictly below `fastEMA[t]` on the same bar), so no long/short entry conflict is possible and no priority rule is needed there.
- Entry versus same-side exit can co-fire on one bar (e.g. a gap bar with `close[1] < fastEMA[t]` and `close[t] > fastEMA[t] > slowEMA[t]`). Pine evaluates the blocks top to bottom and the entry block precedes the exit block for each side, so the entry is created first and closed on the same bar close — net flat at the same close price. Deterministic and reproducible from source code order, not an interpretation.
- Entry versus opposite-side exit can also co-fire (e.g. long-entry bar while a short is open, with `shortExit` also true). The same top-to-bottom code order decides: the long-entry block runs before the short-exit block, so a flat account ends long, and a short account is reversed to long by the entry while the trailing opposite close finds no position and no-ops. Every combination reduces to exactly one deterministic outcome; nothing is left to implementer choice.

## Required data

- OHLCV `1d` klines of one pair (`BTC_USDT`); the rule reads `close` only.
- Deterministic first-party `ta.ema` over close (lengths 7 and 20). No funding, OI, mark/index price, liquidation, trade feed, order book, on-chain, options, sentiment, macro, or cross-venue state anywhere in the rule.

## Execution assumptions

- Research market (explicitly labeled house overlay, not source-native): `BTCUSDT`, `1d` decision timeframe. The source backtest block identifies `Futures_Binance BTC_USDT` at `period: 1d` — no price-series substitution is performed. The prose `SPY 30m` remark is generic author patter contradicted by the pinned executable provenance (contradiction 1); the record does not follow it.
- Source sizing (`i_trdQty = 10`, unread dead input), full-margin flags (`margin_long/short = 100`), and the absent source cost model are event-neutral: replaced downstream by the standard house execution overlay (Base 6% + Safety 6% + 6%, Isolated, 3x/5x, pinned Binance fees plus realized funding). The overlay changes no signal, event, direction, or exit.
- Engine: completed-bar decision with same-bar-close execution under the pinned Hummingbot baseline (`20260920` / `dev-2.17.0`), matching the source `process_orders_on_close=true` market-order semantics 1:1.

## Evidence

### Source-reported

- One backtest screenshot with no readable numbers; the prose claims best results on SPY 30m with no figure, table, or metric. Census: zero exact empirical numbers on the page — none are recorded here.

### Independently reproduced

- Not independently reproduced.

### Negative evidence

- None known. The closed PRs #6 (LazyBear Wave Trend tie semantics) and #10 (golden/dead cross) concern different constructions and sources (see dedup above).

## Falsification plan

1. Length swap: run entry 20 / exit 7 (inverted) and entry 20 / exit 20 (symmetric); a rule whose sign depends on the exact 7/20 pair rather than on alignment persistence is curve-fit, not signal.
2. Exit-leg ablation: replace `close[1]`-vs-fast exits with opposite-conjunction exits; if performance collapses, the edge lives in the hair-trigger exit timing, and that timing must be re-verified trade by trade in Hummingbot.
3. Always-flat-before-first-signal accounting: verify the backtest holds flat until the first conjunction bar; any deviation is an implementation bug, not a strategy property.
4. Same-bar entry-exit census: count bars where entry and same-side exit co-fire; confirm each nets flat at one close price with no residual position.

## Crypto portability

The rule ports cleanly to 24/7 crypto bars: no session calendar, no gap logic, no dividends/splits, no exchange-timezone call of any kind. One port note: the prose "close by end of day" exit does not exist in code, so on 24/7 bars the rule simply holds until the fast-average exit — downstream must not invent a session close. Crypto 1d trends can whipsaw the 7/20 pair through repeated alignment flips in range-bound regimes, which exercises the exit-then-immediate-re-entry path often — expected behavior, not a bug.

## Limitations

1. No protective stop exists in source; tail risk on vertical adverse moves is borne fully by the fast-average exit. Recorded as explicitly absent per source — must not be "repaired" with an invented stop.
2. The 7/20 defaults are pinned as read; any other length pair is a different, unpinned rule.
3. Source reports no performance numbers, so there is no source claim to reproduce or refute — only the rule semantics above.
4. `margin_long/short = 100` and the dead `i_trdQty` input are carried as read, not as live sizing.

## Implementation status

- `not-implemented`. No Hummingbot/Qlib/n8n/Paper/Testnet/Live work has been performed from this record.

## Adoption boundary

- `not-approved`, research-only. This record is semantic/backtest expressibility only — not profitability validation, not survivor promotion, and not Paper/Testnet/Live authorization.

## Related Wiki records

- None. No Wiki Brain write was performed for this Scout cycle.

## Sources

- https://www.fmz.com/strategy/363835 (primary source: page, backtest block, and embedded Pine verified live 2026-10-07)
- https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
- https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}entry
- https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}close
- https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}ema
- https://www.tradingview.com/pine-script-docs/concepts/strategies/
