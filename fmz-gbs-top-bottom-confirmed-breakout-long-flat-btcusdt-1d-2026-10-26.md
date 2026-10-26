---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: FMZ GBS TOP BOTTOM Confirmed fractal-level breakout long-flat BTCUSDT 1d independent derivative
created: 2026-10-26
updated: 2026-10-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - fmz
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-04-28
sources:
  - https://www.fmz.com/strategy/449724
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# GBS TOP BOTTOM Confirmed fractal-level breakout — independent long-flat derivative

## Provenance

**Primary source (read directly this cycle):** FMZ public strategy page *GBS TOP BOTTOM Confirmed Strategy*, FMZ ID **449724**, author **ChaoZhang**, page last modified **2024-04-28** (adopted as `source_as_of`): https://www.fmz.com/strategy/449724 . Fetched live 2026-10-26 via HTTPS (646,222 bytes HTML, no login or paywall). The embedded Pine Script v5 block was verified line-by-line in the page bytes: `strategy("GBS TOP BOTTOM Confirmed", overlay=true)`; `var float entryHigh = na`; `entryCondition = high < high[1] and high[1] > high[2]`; `entryHigh := high[1]` on formation; `buyCondition = not na(entryHigh) and high > entryHigh and open < entryHigh`; `var float exitLow = na`; `exitCondition = low > low[1] and low[1] < low[2]`; `exitLow := low[1]` on formation; `sellCondition = not na(exitLow) and low < exitLow and open > exitLow`; `strategy.entry("Buy", strategy.long, when = buyCondition)`; `strategy.close("Buy", when = sellCondition)`. The page's backtest header reads `period: 1d`, `basePeriod: 1h`, `Futures_Binance BTC_USDT`, sample window 2023-04-22–2024-04-27 (sample metadata, not a strategy rule). The local scratch mirror (`GBS高低点确认策略-GBS-TOP-BOTTOM-Confirmed-Strategy.md`) carries the identical rule text and the same detail URL. Do **not** claim Pine-byte identity beyond the verified lines, original fill equivalence, or source performance reproduction.

**Source-native facts:** zero `input.*` calls anywhere (fully fixed, no parameter variants to choose from); long-only book (one `strategy.long` entry leg, one `strategy.close` leg, no short call); pure OHLC geometry (no EMA/RSI/MACD/ATR/BB/crossover/security/request/stop/limit/exit/cancel/calc_on_every_tick anywhere); no sizing, pyramiding, `process_orders_on_close`, warmup, cost or slippage literal (Pine defaults govern the original and are **not** pinned here). The page's own risk section states the strategy lacks a stop-loss mechanism and ignores costs/slippage; no return, win-rate or trade-count performance is reported anywhere on the page.

**Independent derivative, not a source-native/lossless Pine port.** Researcher-declared and materially different: Binance BTC-USDT **spot 1d**, LONG/FLAT only (source is already long-only; no side is repurposed); **completed-close-effective** MARKET fills (the original's default next-bar timing is not reproduced and no timing equivalence is claimed); fixed **0.001 BTC** with 10,000 USDT unborrowed cash instead of any framework-default sizing; the 1h `basePeriod` is unused (daily completed bars only, no intrabar path); 30-bar warmup, cash/fill/fee policy, and EXIT/ENTRY priority below. The 3-bar fractal geometry, most-recent-level memory, open-position breakout predicates, strict comparators and opposite-fractal close are preserved literally.

**Immutable candidate identity (research spec, not a source-code hash):** `FMZ:449724:GBS-TOP-BOTTOM:2024-04-28 | independently-derived-v1:2026-10-26 | Binance BTC-USDT spot 1d | 3-bar fractal memory + open-filtered H/L breakout | LONG buy-leg, fractal-low close | Q=0.001 BTC | close-effective MARKET | fee=0.0001/side | warmup30`. Changing geometry, memory, predicates, market, fills, costs or state requires a separately disclosed revision.

**Dedup check:** `main@66e0f91` has 360 root-level strategy Markdown files and static README count 360; working-tree searches for `GBS`, `449724`, `entryHigh` and `TOP BOTTOM Confirmed` return none. All 10 then-open `research/*` PRs enumerated (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend, #89 Chandelier, #92 SSL channel, #251 Swift 2YMA, #304 forven CCI, #331 AdxSmas, #350 ClucMay, #353 Heracles Keltner-Donchian) — none references this page or a most-recent-fractal-memory breakout rule. Nearest pool neighbors are materially different (see Deduplication).

## Economic mechanism

### Source-reported

Fresh 3-bar high pivots are treated as resistance whose upside break (from an open below the level) marks expansion worth riding; fresh 3-bar low pivots are treated as support whose downside break ends the ride. Breakout persistence of the most recent fractal level, not reversal fade, is the stated thesis. No profit claim is made.

### Research interpretation

A most-recent-memory breakout system with an intrabar-cross precondition: the open must start on the pre-break side, so gap-and-go prints and flat-hover touches do not qualify. Because levels persist until overwritten, stale-level breakouts after long quiet stretches fire by construction. Close-only fills can print below a buy trigger (or above a sell trigger) when the bar reverses into the close — a disclosed research convention, not a source promise.

## Signal

**Market and candle contract:** one continuous UTC-aligned real Binance `BTC-USDT` **spot 1d** OHLCV series. Let `T[t]` be the actual candle *opening* Unix timestamp, `D=86400` seconds, and `C[t]` its actual close. A row is decision-eligible only at or after `T[t]+D`, never at its opening timestamp. Require consecutive daily timestamps, finite positive O/H/L/C, H>=max(O,C), L<=min(O,C), and finite nonnegative volume on every bar used. Missing, duplicated or malformed input **aborts the research run** rather than forward-filling or fabricating a price. This failure fence is researcher-defined, not a source claim. Comparisons need no division, so zero-range bars stay evaluable.

For each completed bar `t` (statements execute in source order — levels update before signals evaluate, so a bar can never fire the level it just formed):

- `eForm[t] := H[t] < H[t-1] and H[t-1] > H[t-2]` (needs `t>=2`); when true set `entryHigh := H[t-1]` (overwrites any prior level, however stale).
- `xForm[t] := L[t] > L[t-1] and L[t-1] < L[t-2]` (needs `t>=2`); when true set `exitLow := L[t-1]`.
- `buy[t] := entryHigh is set and H[t] > entryHigh and O[t] < entryHigh` (strict on both legs; `H==entryHigh` or `O==entryHigh` never fires).
- `sell[t] := exitLow is set and L[t] < exitLow and O[t] > exitLow` (strict; equality never fires).

**Warmup:** 30 consecutive valid, fully completed daily candles from the predetermined sample start (10x the 3-bar structural minimum, covering fractal formation plus the level-memory transient with margin); begin FLAT with both levels unset. Do not trade on the first 30 rows; the first eligible decision is on row index >=30. Do not re-seed levels mid-sample or normalize using full-sample values.

**State and event priority (complete derivative):**

1. One position state `FLAT` or `LONG(Q)`, `Q=Decimal("0.001") BTC`, plus at most one pending order. Confirmed fills, not intents, update state. While pending, no new action.
2. If LONG at a completed bar: first evaluate `sell[t]` — if true, issue exactly one MARKET SELL of full Q at that bar's observed close and return FLAT on confirmed fill (the `buy[t]` print on the same bar, if any, is ignored — no same-bar re-entry). Otherwise hold. There is no same-entry-bar exit.
3. If FLAT at a completed bar: if `buy[t]` is true, issue exactly one MARKET BUY of Q at that bar's observed close, provided `cash>=Q*C[t]*(1+f)` with `f=0.0001`. If insufficient, remain flat and do not assume borrowing. A co-firing `sell[t]` while FLAT is a no-op (no position to close — consistent with the source call order, where the close leg gates no order while flat). On confirmed full BUY, record `entryPrice=C[t]`.
4. After a confirmed SELL, return FLAT; the next completed bar may enter only on a fresh `buy` print. No other cooldown. A repeated `buy` while LONG is a no-op (single-unit, no adds/DCA/pyramiding). A `sell` while FLAT is a no-op. No stop loss, take profit, trailing, time exit, partial exits, leverage, margin, borrowing, compounding, short leg, or hidden executor defaults.
5. Any rejected, missing, partial, unresolved or ambiguous MARKET fill aborts this bounded research run; do not infer a fill, repeat an unconfirmed order, or synthesize cash/position. At the predetermined sample end, mark a remaining LONG at the actual last completed close, with **no invented liquidation**.

## Required data and causality

Exactly one contiguous UTC daily Binance spot OHLCV stream and its real opening timestamps. The rule reads **Open/High/Low only** for triggers (plus Close for fills) — Volume is never order-gating. All references are bars `t-2..t`, complete at decision time; no future data, no unconfirmed intrabar values, no repainting (levels reference only confirmation-complete triples), no full-sample normalization, no model fitting. The 1h `basePeriod` from the source backtest header is deliberately unused. Missing prices block signals and fills rather than defaulting to synthetic prices.

## Execution assumptions and pinned Hummingbot compatibility

**Gate 5 is bounded to a real inspected pinned simulation path, not a deployment claim.** Admission policy identifies Hummingbot package label **20260920**, VERSION **dev-2.17.0**. The inspected source is **HCH725/hummingbot at commit 8b0e067e80ab62f10846d518dcb5a8218527ddb3**; its `hummingbot/VERSION` file reads `dev-2.17.0` (verified this cycle). No package-to-commit byte-match is claimed; the engine claim is limited to this pinned source plus previously reviewed matching research semantics. Sibling PASS records remain path evidence only, never proof of this candidate.

- **Market/data:** BinanceSpotCandles `constants.py` `INTERVALS` bidict includes `1d` (verified this cycle at the pin); `_parse_rest_candles` maps REST `row[0]` to opening timestamp and `row[1..5]` to O/H/L/C/V (verified this cycle at the pin). A strategy-specific controller must compute the declared 3-bar fractal memory, verify contiguous completed bars, and supply a single BTC-USDT spot 1d stream. The engine does not magically implement this breakout signal.
- **Controller/action/executor:** `BacktestingEngineBase.simulate_execution` (line 269) iterates processed rows, calls controller `determine_executor_actions()` (line 284), and routes each `CreateExecutorAction` (line 285) over the current-row forward slice to `simulate_executor` (line 287) — row path verified this cycle at the pin. `OrderExecutorConfig` admits `connector_name="binance"`, `trading_pair="BTC-USDT"`, BUY/SELL, `amount=Decimal("0.001")`, `position_action=OPEN/CLOSE`, `execution_strategy=MARKET`, `price=None` (verified this cycle at the pin; `leverage` defaults to 1). `OrderExecutorSimulator.simulate` fills MARKET orders at the first supplied row's timestamp with that row's `close` as entry price, sets `filled_amount_quote=Q*close` and `cum_fees_quote=trade_cost*Q*close`, and reports `CloseType.POSITION_HOLD` (verified this cycle at the pin). Full fill at one close is an explicit simulator convention, not proof of executable spot fills.
- **Timestamp caveat:** raw Binance daily row timestamps are **open** labels. The engine joins features with backward as-of on timestamp (verified this cycle); that join alone does not establish that a completed close was known at the open. The required derivative controller gates each completed bar until **open+86400s**, and the research event/fill ledger is normalized to that close-effective timestamp while using the simulator's same-row close price. This is a disclosed adaptation away from the original default timing and does not claim a real post-close order could fill at the observed close. No intrabar or lower-timeframe path is assumed.
- **Position and ledger:** `BacktestPositionHold` nets equal-base BUY/SELL ("Buys and sells of the same asset net out automatically. Realized PnL comes from matched buy/sell volume", verified this cycle at the pin), tracking average entry, gross matched realized PnL and accumulated fees separately. The engine's `terminated_executors_window` default is 3600 seconds (`DEFAULT_TERMINATED_EXECUTORS_WINDOW = 60*60`, verified this cycle at the pin) — pin it to `None` and use persistent pending/fill-confirmed controller state so daily positions are never lost to the one-hour view and duplicate orders are never sent. After a 0.001 BTC BUY at `P_b` and SELL at `P_s`, modeled net quote PnL = `0.001*(P_s-P_b) - 0.0001*0.001*(P_b+P_s)`; never misreport gross native PnL as fee-net equity. An open position's marked equity carries the already-paid BUY fee.
- **Costs:** pin simulator `trade_cost=0.0001` per filled side (0.01%, researcher-selected house research input — the source models no costs and no rate is attributed to it). Zero additional modeled slippage is **zero additional modeled slippage**, not evidence of zero spread/latency. Spot funding is inapplicable by construction (no fabricated futures funding). Minimum notional, lot/tick precision, partial fills, liquidity and live viability remain unverified; `BacktestingDataProvider.get_price_by_type` can fall back to `Decimal("1")` (verified this cycle at the pin), which is expressly **forbidden** for trade pricing. Validate the original full candle sequence **before** any engine `dropna` processing.
- **Reused independent path review:** HCH725/alpha-strategy-research PR **#417** (merged 2026-10-24) independently reviewed this same pinned Binance spot 1d / MARKET first-close / POSITION_HOLD fee-ledger research path. That verifies an **engine primitive**, not this new signal, trade series, profitability, package digest or candidate-specific parity. This cycle additionally re-read the pinned VERSION, spot candle constants/parser, engine row/action routing, OrderExecutorSimulator, BacktestPositionHold netting, data-types config and price-fallback guard at the pin.

## Evidence

### Source-reported

FMZ page identity (449724, ChaoZhang, 2024-04-28), 1d decision period header, the fixed 8-line fractal-memory rule quoted in Provenance, long-only book, and the page's own no-stop-loss/no-cost disclaimers. No performance numbers exist on the page to reproduce.

### Independently reproduced

**Rule-logic self-check (stdlib only, not a backtest):** the frozen memory machine plus FLAT/LONG book were executed over hand-constructed bars and 5x400-bar fuzz streams — breakout-after-formation fires; open-above-level prints are blocked; exact-equality ties never fire; round-trip BUY then SELL alternates; pre-formation bars never decide; BUY/BUY and SELL/SELL never repeat across all fuzz seeds. **Engine-code inspection only, not a strategy backtest:** the pinned files above were read line-by-line this cycle (VERSION bytes, `1d` interval entry, REST row mapping, `simulate_execution` row/action routing, MARKET first-row-close fill, quote-notional fee accumulator, POSITION_HOLD ledger, 3600s executor window, `Decimal("1")` fallback guard). The candidate's trade events, FMZ outputs, Qlib/Hummingbot parity and net returns have **not** been independently reproduced. No backtest was executed.

### Negative evidence

No sizing, warmup, cost, fill-timing or framework-default order setting ships in the retrieved source; **source-native/lossless equivalence is unverified** and this record claims none. Stale-level breakouts fire by construction (persistent memory is source-literal). Simulated completed-close fills can print away from trigger levels and are a backtest convention, not a live guarantee. No verified next-open fill, partial fill, market impact, fee schedule, futures funding or venue size permission. None is silently imputed.

## Deduplication

Nearest pool neighbors are **not equivalent**: `quantifiedtrader-fractal-breakout-22-fixed-lag-long-flat-btcusdt-1d-2026-10-26` (merged today) reads a **fixed-lag slot five bars back** (`idx=6`) with **close** comparators (`C>=FH`, `C<=FL`) and explicitly never searches the most recent fractal — this record keeps a **most-recent memory** of a **3-bar** pivot with **high/low-plus-open** breakout predicates, so fresh extremes fire here that never fire there and stale slot extremes fire there that never fire here: different windows, different reference construction, different trigger rails, different predicates. `williams-fractal-ema-band-fixed-rr-two-sided` fades EMA-band-contained pivots with a resting EMA-slow stop plus 1.5R limit OCO book, two-sided — this record has no moving average, no band, no stop/target at all, and a level-touch close exit, long-flat only. `support-resistance-fractal-trailing-breakout-two-sided` averages admitted extremes into an offset dual trailing band on **4h** — this record averages nothing, trails nothing, and trades one raw remembered level on **1d**. Different source, different signal construction, different risk book, different horizon/direction: not a duplicate, paraphrase, or trivial parameter variant.

## Falsification plan

After separate downstream research authorization, compare the frozen rule against (a) the same memory machine with the open-position predicates removed (pure high/low breakout), and (b) a fixed-lag-5-bar close-break ablation on the same grid, on predeclared IS/OOS partitions; verify the predicates actually change entry/exit event times. Any new or unverified execution/data primitive requires representative Qlib/Hummingbot event-level validation before mass screening. Do not tune on OOS. No backtest was run by Scout.

## Crypto portability

Native crypto venue by declaration (Binance BTC-USDT spot 1d); the Futures_Binance header of the source sample is adapted to spot by explicit researcher choice, removing funding by construction rather than observing it. Minimum-notional, precision, liquidity and live viability remain unverified limitations, never assumed. House DCA 6/6/6 and 3x/5x futures are optional **separate downstream experiments**, not prerequisites and not silently part of this frozen version.

## Limitations

- A breakdown that never prints a sub-`exitLow` low leaves the long exposed with no stop, target or time exit; stale remembered levels can trigger entries far from their formation context.
- The original default timing is not reproduced; entries/exits happen at the simulated completion close, which changes events versus the source clock.
- Exact source framework revision, original sizing/cost settings and profitability are unknown. The simulated completed-close fill is a **backtest convention**, not a live execution guarantee.
- The modeled 0.01%-per-side research cost, zero additional modeled slippage, fixed base size and absence of futures funding do not prove actual Binance trade economics. A long can remain exposed through data outages. No Qlib parity, survivor status or trading approval follows from HB_READY.

## Implementation status

`not-implemented`: no dedicated Hummingbot controller, no Qlib executable recipe, no backtest, no deployment. An admitted PASS record is a research specification, not a claim of ready-to-run artifacts.

## Adoption boundary

`research-only`; `not-approved`. No Paper/Testnet/Live or portfolio allocation authorization. Frontmatter PASS is a **Scout-proposed six-gate research eligibility claim**, subject to independent Hermes Auditor review — Hermes Auditor alone determines exact-head PASS merge or NOT_LOSSLESS close. Existing signed webhook receiver alone maintains the post-merge README count.

## Related Wiki records

None claimed.

## Sources

- FMZ primary: https://www.fmz.com/strategy/449724 (GBS TOP BOTTOM Confirmed Strategy, ChaoZhang, last modified 2024-04-28; page directly read 2026-10-26).
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Existing independent package/engine primitive review: https://github.com/HCH725/alpha-strategy-research/pull/417
