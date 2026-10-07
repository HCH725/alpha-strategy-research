---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Octa-EMA ribbon with Ichimoku-variant filter long system on BTCUSDT 1d bars
created: 2026-10-07
updated: 2026-10-07
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-12-11
sources:
  - https://www.fmz.com/strategy/434982
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
  - "The prose says a buy fires when 'all 8 EMAs are in an uptrend arrangement and the price is above the Ichimoku cloud', and a sell fires 'when the EMA arrangement flips to a downtrend'. The pinned code uses only the ema(11)-vs-ema(34) ordering flip plus the avg(ema11, ema34)-above-cloud conjunction for entries, and a bare ema(11)-below-ema(34) close for exits; full 8-EMA stacked alignment is never tested and price-vs-cloud is never tested. The code governs."
  - "The prose calls the sell leg a downtrend signal, but the code is long-only: the only live exit is `strategy.close('long')` and no short entry exists anywhere. There is no short side in code — contradiction resolved by recording short as explicitly disabled per code."
  - "The prose claims the strategy 'can run effectively in hourly, 4-hour or daily timeframes', but the pinned FMZ backtest block fixes `period: 1d` on `BTC_USDT`. This record pins the single decision timeframe `1d`; no other timeframe is admitted."
---

# Octa-EMA ribbon with Ichimoku-variant filter long system on BTCUSDT 1d bars

## Provenance

Primary source read end to end (FMZ strategy page mirror plus live re-verification):

- FMZ strategy: https://www.fmz.com/strategy/434982 (`Octa-EMA-and-Ichimoku-Cloud-Quantitative-Trading-Strategy`, page author ChaoZhang; Pine header comment `//Fukuiz`, strategy title `Fukuiz Octa-EMA + Ichimoku`, `//@version=5`).
- Last modified (as printed on the page): 2023-12-11.
- FMZ backtest block pinned on the page: `start: 2022-12-04 00:00:00`, `end: 2023-12-10 00:00:00`, `period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]` — single pair, 1d decision timeframe.
- Live verification this run (2026-10-07): the page re-fetched over HTTPS (811778 bytes) carries the same title (`Octa-EMA and Ichimoku Cloud Quantitative Trading Strategy`), the same author (`ChaoZhang`), the same strategy id (`strategy/434982`) and the `Fukuiz Octa` strategy title, corroborating the mirror as the same artifact.
- Mirror executable block: one `strategy()` declaration (`process_orders_on_close=true`, no `calc_on_every_tick`, no `calc_on_order_fills`, no `pyramiding`), twelve `input.*` declarations (ribbon toggle, eight EMA lengths, three plot toggles, four Ichimoku integers, six window integers), eight `ta.ema` assignments, display-only plot/fill lines, the Ichimoku-variant assignments, dead state-machine booleans (`buycond`/`sellcond`/`bullish`/`bearish`/`buy`/`sell` — computed, never read by any order), and exactly two live order calls: one `strategy.entry(id='long', direction=strategy.long, when=period())` under `if buy2`, one `strategy.close(id='long', when=period())` under `if sell2`.

Licence and rights: this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

Pre-write dedup (2026-10-07): a working-tree search for `434982`, `fukuiz` and `octa` returned 0 matches. Closest records on `main`: `ichimoku-cloud-adx-trend-filter-btcusdt-1d-2026-10-06.md` (Coinrule Ichimoku with ADX/DMI filter, different source and different filter construction), `ema-20-50-cross-btcusdt-1h-2026-10-06.md` (Forven pure 20/50 cross, 1h, no cloud filter), `ema-cloud-7-20-trend-btcusdt-1d-2026-10-07.md` (7/20 alignment, two-sided, no Ichimoku construction), `ehma-range-band-breakout-btcusdt-1d-2026-10-05.md` (EHMA channel, no Ichimoku). Five-axis distinction: mechanism differs (ema11/ema34 ordering flip AND avg-above-custom-cloud conjunction, long-only, versus ADX/DMI-gated cloud, pure two-average cross, dual-threshold alignment, or EHMA channel), signal construction differs (non-standard SenkouA/SenkouB variant below — no other record uses it), source identity differs (FMZ 434982 Fukuiz versus Coinrule/Forven/rwestbrookjr/0xLetoII-lineage sources), direction differs from the two-sided records (long-only), and the window-gating covers both legs (unlike the Forven record where exits stay live outside the window). `gh pr list --state open` shows only PR #36 (reconstruction lane, no `research/*` collision).

## Economic mechanism

### Source-reported

- As printed: eight EMAs (5/11/15/18/21/24/28/34) form a trend ribbon ("Octa-EMA"); the Ichimoku cloud judges trend direction and support/resistance. Double-indicator filtering is claimed to cut false signals; the cloud keeps trading with the trend. No sample, no metric, no baseline, no figure and no performance number of any kind is printed anywhere in the artifact. Nothing numerical is recorded below.

### Research interpretation

Falsifiable mechanism hypothesis: on a single 24/7 crypto instrument, demanding that the mid-ribbon average sit above a slow cloud before accepting a medium-fast ordering flip buys a two-scale persistence filter — the ema(11)-over-ema(34) flip marks the turn, while the avg-above-cloud leg refuses turns that fire underneath an established slow congestion zone, so entries cluster on flips with room above the slow structure; losing the ema(11)/ema(34) ordering cuts the trade without waiting for slow-structure breakdown. The bet is continuation after a filtered turn, not mean reversion. This is a ported technical-analysis hypothesis: the source supplies no behavioural argument, no sample and no evidence, so the mechanism is research interpretation, not source-reported fact.

Component roles, stated plainly:

- Primary signal: the ema(11)-vs-ema(34) ordering flip (strict inequalities; equality fires neither leg).
- Noise filter: the avg(ema11, ema34)-above-both-cloud-lines conjunction on entries only; exits are unfiltered.
- Trend / regime filter: none beyond the Ichimoku-variant slow structure itself.
- Direction gate: long-only by construction — no short rule exists in source.

## Signal

Everything below is read from the verified Pine block at pinned source defaults. Nothing in this section is `research-proposed`.

**Formation timestamp and tradability**

- Decision series: completed `1d` bars of `Futures_Binance BTC_USDT` (record-pinned single decision timeframe; the script contains 0 `request.*`, 0 `security(`, 0 `timeframe` references, 0 `input.timeframe` — so exactly one decision timeframe is declared by this record, `1d`, with no multi-timeframe dependency).
- Inputs at decision bar `t`: `close[t]`, `high[t]`/`low[t]` (cloud Donchian legs only), `high[t-1..t-8]`/`low[t-1..t-8]` (Donchian windows), `high[t-1..t-25]`/`low[t-1..t-25]`, `high[t-1..t-51]`/`low[t-1..t-51]`, `Tenkan[t-26]`, `Kijun[t-26]`, `SenkouA[t-26]`. `open` and `volume` are never read by the trading logic.
- Order timing: the live order calls are one `strategy.entry` and one `strategy.close`, both market orders (no `limit`/`stop` arguments anywhere — 0 occurrences of each; 0 `strategy.exit`, 0 `strategy.order`, 0 `strategy.stop`, 0 `strategy.cancel`), and the declaration sets `process_orders_on_close=true`. Per official first-party documentation this is exactly a completed-bar decision with same-bar-close execution; no next-bar-open fill exists anywhere in the rule.
- Recalculation: neither `calc_on_every_tick` nor `calc_on_order_fills` appears in the declaration (0 occurrences of each); both default to `false` per official documentation. Recorded as source-declared-by-language-default; no intrabar re-evaluation can create a second order on the same bar.
- Window gate: both legs carry `when=period()` with `period() => time >= start and time <= end`, `start = timestamp(2017, 1, 1, 00, 00)`, `end = timestamp(2023, 12, 31, 23, 59)` at pinned defaults. The rule is live only inside that window (both entries AND exits — unlike the Forven window precedent where exits stay live). No session, weekday, or hour gate of any kind (`dayofweek`, `dayofmonth`, `hour`, `timenow`, `time(` occur 0 times in executable code).

**Lookback, formulas and warmup**

- Parameters as declared: EMA lengths 5/11/15/18/21/24/28/34 over `close`; `conversionPeriods = 9`, `basePeriods = 26`, `laggingSpan2Periods = 52`, `displacement = 26`.
- Formulas, exact (source-variant Ichimoku, recorded as read — this is NOT the textbook cloud):
  - `ema1..ema8 = ta.ema(close, 5/11/15/18/21/24/28/34)`; only `ema2` (11) and `ema8` (34) feed orders; ema1/3/4/5/6/7 feed display only.
  - `middleDonchian(Length) = math.avg(ta.highest(Length), ta.lowest(Length))` over high/low.
  - `Tenkan = middleDonchian(9)`; `Kijun = middleDonchian(26)`.
  - `SenkouA = middleDonchian(52)`, used displaced as `SenkouA[26]`.
  - `SenkouB = (Tenkan[26] + Kijun[26]) / 2` — a Tenkan/Kijun-average variant, not the textbook highest/lowest-52 average; pinned as read.
  - `fukuiz = math.avg(ema2, ema8)`; `white = ema2 > ema8`; `sell2 = ema2 < ema8`.
  - `buy2 = white and fukuiz > SenkouA[26] and fukuiz > SenkouB`.
- Dead code, explicitly excluded: `buycond = white and white[1] == 0`, `sellcond`, `bullish = ta.barssince(buycond) < ta.barssince(sellcond)`, `bearish`, `buy`, `sell` — a six-line state machine that no order call reads. The record's rule uses `buy2`/`sell2` only; the dead booleans change no event.
- Warmup, derived from the pinned code because the source declares none: the longest causal chain is `SenkouA[26]` = 52-bar Donchian read 26 bars back = 78 bars; `SenkouB` needs 26 + 26 = 52 bars; EMAs need at most 34. Strict comparisons against unsettled inputs evaluate to no-order, so the earliest possible order is the first bar on which `buy2` holds with settled inputs (no later than 78 daily bars in).

**Entry**

- Long entry: `if buy2` → `strategy.entry(id='long', direction=strategy.long, when=period(), comment='BUY')`. Omits `qty` (uses declaration sizing, recorded under Execution assumptions), omits `limit`/`stop` (market order).
- Short entry: none exists — short is explicitly disabled per code (0 short calls; the prose downtrend leg has no code counterpart — contradiction 2).

**Exit**

- Pinned code census: 1 `strategy.entry`, 1 `strategy.close`, 0 `strategy.close_all`, 0 live `strategy.exit`, 0 `strategy.order`, 0 `strategy.stop`, 0 `strategy.cancel`, 0 `strategy.risk.*`, 0 `strategy.position_*`.
- Signal exit: `if sell2` → `strategy.close(id='long', when=period(), comment='SELL')` where `sell2 = ema2 < ema8` (strict; `ema2 == ema8` holds neither entry nor exit — the tie case is defined, not ambiguous).
- Opposite-signal exit: not applicable (no opposite signal exists in a long-only rule).
- Stop loss: none. Take profit: none. Trailing stop: none. Time limit / maximum holding period: none. Flat state is reachable before the first entry and after every ordering-loss exit; the system is otherwise long-or-flat, never short.
- Window-end behavior (explicit, from code): because the close leg is also `when=period()`-gated and no terminal `close_all` exists, a position still open on the last in-window bar stays open past the window end in a faithful replay. Downstream must reproduce this (hold past window) rather than invent a window-end flatten.
- A `strategy.close` on a flat position (e.g. a `sell2` bar with no open entry) is a deterministic no-op.

**Holding period, overlap and re-entry**

- Holding period: unbounded, determined entirely by waiting for the next ema(11)-below-ema(34) bar; the source states no maximum or expected holding period.
- Maximum same-side concurrency: 1. `pyramiding` is not written in the declaration (0 occurrences), so the value comes from the language default — one open same-side entry, further same-side entries rejected (the same default-convergence the PASS reviews of earlier records accepted; the executing engine must confirm it).
- Same-direction re-entry: after an exit the system is flat, so the next `buy2` bar opens a fresh position; while positioned, further `buy2` bars are rejected under the default above, and orders fill on the same bar they are created, so no unfilled order survives into the next bar. No cooldown exists. No opposite-side entry exists, so no reversal path is needed.
- No `position_size`, `position_avg_price`, `openprofit` or `opentrades` reference exists anywhere in the block (verified by full read), so no position-aware state conditions any signal or exit. The dead `barssince` state machine feeds no order.

**Conflict priority (explicit, from source code order)**

- Entry versus exit can co-fire on one bar (a bar with `buy2` true requires `ema2 > ema8`; `sell2` requires `ema2 < ema8` — mutually exclusive on the same bar, so no entry/exit conflict is possible and no priority rule is needed).
- The `buy2` and `sell2` blocks are each single-`if` guards over mutually exclusive strict inequalities; every bar reduces to exactly one of {enter-or-hold-long, close, nothing}. Nothing is left to implementer choice.

## Required data

- OHLCV `1d` klines of one pair (`BTC_USDT`); the rule reads `close`, `high`, `low` only (`open`/`volume` never read).
- Deterministic first-party `ta.ema` over close (lengths 5/11/15/18/21/24/28/34), `ta.highest`/`ta.lowest` Donchian legs, `math.avg`, and one `timestamp` window. No funding, OI, mark/index price, liquidation, trade feed, order book, on-chain, options, sentiment, macro, or cross-venue state anywhere in the rule.

## Execution assumptions

- Research market (explicitly labeled house overlay, not source-native): `BTCUSDT`, `1d` decision timeframe. The source backtest block identifies `Futures_Binance BTC_USDT` at `period: 1d` — no price-series substitution is performed. The prose multi-timeframe remark is generic author patter contradicted by the pinned executable provenance (contradiction 3); the record does not follow it.
- Source sizing (`default_qty_type=strategy.cash`, `default_qty_value=1000`, `initial_capital=10000`, `commission_value=0.25` percent) and the absent source cost model are event-neutral: replaced downstream by the standard house execution overlay (Base 6% + Safety 6% + 6%, Isolated, 3x/5x, pinned Binance fees plus realized funding). The overlay changes no signal, event, direction, or exit.
- Engine: completed-bar decision with same-bar-close execution under the pinned Hummingbot baseline (`20260920` / `dev-2.17.0`), matching the source `process_orders_on_close=true` market-order semantics 1:1.

## Evidence

### Source-reported

- No backtest screenshot with readable numbers is embedded in the artifact; the prose claims a "stable and reliable" trend system with no figure, table, or metric. Census: zero exact empirical numbers on the page — none are recorded here.

### Independently reproduced

- Not independently reproduced.

### Negative evidence

- None known. The closed PR #6 (LazyBear Wave Trend) and PR #10 (golden/dead cross) concern different constructions and sources (see dedup above).

## Falsification plan

1. Filter ablation: drop the avg-above-cloud conjunction (trade every ema11/ema34 flip) and separately drop the flip (hold whenever avg is above cloud); if either ablation matches or beats the full rule, the claimed two-scale filter carries no edge.
2. Variant swap: replace the non-standard `SenkouB = (Tenkan[26]+Kijun[26])/2` with the textbook `(highest(52)+lowest(52))/2` displaced 26; a rule whose sign depends on this idiosyncratic variant is curve-fit to the author's code, not signal.
3. Dead-code census: verify the six dead state-machine booleans feed no order in the downstream port; any live use of them is an implementation bug, not a strategy property.
4. Window-edge accounting: verify entries/exits fire only inside 2017-01-01→2023-12-31 and that a position open at the window end is carried (not force-flattened); any deviation is an implementation bug.

## Crypto portability

The rule ports cleanly to 24/7 crypto bars: no session calendar, no gap logic, no dividends/splits, no exchange-timezone call beyond the fixed backtest window. One port note: both legs are window-gated and there is no terminal flatten, so on 24/7 bars the rule simply holds a window-end position until the next ordering-loss bar — downstream must not invent a session or window-end close. Crypto 1d whipsaws of the ema11/ema34 pair through repeated flips in range-bound regimes exercise the exit-then-immediate-re-entry path often — expected behavior, not a bug.

## Limitations

1. No protective stop exists in source; tail risk on vertical adverse moves is borne fully by the ordering-loss exit. Recorded as explicitly absent per source — must not be "repaired" with an invented stop.
2. The eight EMA lengths and four Ichimoku integers are pinned as read; any other parameter set is a different, unpinned rule.
3. Source reports no performance numbers, so there is no source claim to reproduce or refute — only the rule semantics above.
4. The six dead state-machine booleans and the display-only ribbon plots are carried as read dead code, not as live signal.
5. The fixed 2017→2023 window gates both legs; it is backtest scope, not signal, but unlike the Forven precedent the exits do not stay live outside it.

## Implementation status

- `not-implemented`. No Hummingbot/Qlib/n8n/Paper/Testnet/Live work has been performed from this record.

## Adoption boundary

- `not-approved`, research-only. This record is semantic/backtest expressibility only — not profitability validation, not survivor promotion, and not Paper/Testnet/Live authorization.

## Related Wiki records

- None. No Wiki Brain write was performed for this Scout cycle.

## Sources

- https://www.fmz.com/strategy/434982 (primary source: page, backtest block, and Pine verified live 2026-10-07)
- https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
- https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}entry
- https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}close
- https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}ema
- https://www.tradingview.com/pine-script-docs/concepts/strategies/
