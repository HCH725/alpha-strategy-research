---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: FMZ 123 Reversal timed SMA200-reclaim exit long-flat BTCUSDT 1d independent derivative
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
source_as_of: 2024-11-12
sources:
  - https://www.fmz.com/strategy/471698
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# 123 Reversal timed SMA200-reclaim exit — independent long-flat derivative

## Provenance

**Primary source (read directly this cycle):** FMZ public strategy page *123 Reversal Trading Strategy*, FMZ ID **471698**, publisher **ChaoZhang**, page creation stamp **2024-11-12 15:15:46** (adopted as `source_as_of`): https://www.fmz.com/strategy/471698 . Fetched live 2026-10-26 via HTTPS (721,307 bytes HTML, no login or paywall). The page-embedded Pine Script v5 block was verified in the page bytes: `strategy(\"123 Reversal Trading Strategy\", overlay=true)`; `daysToHold = input(7, title=\"Days to Hold Trade\")`; `maLength = input(200, title=\"Moving Average Length\")`; `ma20 = ta.sma(close, maLength)`; `condition1 = low < low[1]`; `condition2 = low[1] < low[3]`; `condition3 = low[2] < low[4]`; `condition4 = high[2] < high[3]`; `entryCondition = condition1 and condition2 and condition3 and condition4`; `exitCondition = ta.barssince(entryCondition) >= daysToHold or close >= ma20`; `if (entryCondition)` / `strategy.entry(\"Buy\", strategy.long)`; `if (exitCondition)` / `strategy.close(\"Buy\")`. The code block carries an MPL-2.0 header crediting `EdgeTools`. The page's backtest header reads `period: 1d`, `basePeriod: 1d`, `Futures_Binance BTC_USDT`, sample window 2019-12-23–2024-11-11 (sample metadata, not a strategy rule). The local scratch mirror (`基于123点位反转的动态持仓期策略-Dynamic-Holding-Period-Strategy-Based-on-123-Point-Reversal-Pattern.md`) carries the identical rule text and the same detail URL. Do **not** claim Pine-byte identity beyond the verified lines, original fill equivalence, or source performance reproduction.

**Source-native facts:** exactly two `input()` calls with frozen defaults (`daysToHold=7`, `maLength=200` — no variant to choose, pinned as literals); long-only book (one `strategy.long` entry leg, one `strategy.close` leg, no short call, no `close_all`); pure OHLC + `ta.sma` + `ta.barssince` geometry (no EMA/RSI/MACD/ATR/BB/crossover/security/request/stop/limit/exit/cancel/calc_on_every_tick anywhere; page-byte counts `strategy.entry` 1 / `strategy.close` 1 / `stop=` 0 / `limit=` 0 / `crossover` 0 / `security(` 0 / `request.` 0); no sizing, pyramiding, `process_orders_on_close`, warmup, cost or slippage literal (Pine defaults govern the original and are **not** pinned here). No return, win-rate or trade-count performance is reported anywhere on the page.

**Independent derivative, not a source-native/lossless Pine port.** Researcher-declared and materially different: Binance BTC-USDT **spot 1d**, LONG/FLAT only (source is already long-only; no side is repurposed); **completed-close-effective** MARKET fills (the original's default next-bar timing is not reproduced and no timing equivalence is claimed); fixed **0.001 BTC** with 10,000 USDT unborrowed cash instead of any framework-default sizing; the `basePeriod: 1d` equals the decision frame so there is no second execution-granularity frame to fence (daily completed bars only, no intrabar path); 250-bar warmup, cash/fill/fee policy, and ENTRY-then-EXIT source-order priority below. The 4-condition low/high 123 chain, frozen 7/200 literals, `ta.sma`/`ta.barssince` construction, strict/inclusive comparators and time-or-reclaim exit are preserved literally.

**Immutable candidate identity (research spec, not a source-code hash):** `FMZ:471698:123-REVERSAL-TIMED:2024-11-12 | independently-derived-v1:2026-10-26 | Binance BTC-USDT spot 1d | 4-cond L/H 123 + barssince>=7 or C>=SMA200 | LONG buy-leg, timed/reclaim close | Q=0.001 BTC | close-effective MARKET | fee=0.0001/side | warmup250`. Changing pattern, literals, market, fills, costs or state requires a separately disclosed revision.

**Dedup check:** `main@a9e5f43` has 362 root-level strategy Markdown files; working-tree searches for `471698`, `123 Reversal Trading Strategy`, `daysToHold` and `barssince` return only the two 123-family pool neighbors below — no record uses this page, this 4-condition chain, or this timed/reclaim exit. All 11 then-open `research/*` PRs enumerated (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend, #89 Chandelier, #92 SSL channel, #251 Swift 2YMA, #304 forven CCI, #331 AdxSmas, #350 ClucMay, #353 Heracles Keltner-Donchian, #488 Vallentuna2 RoGr75 EMA-buffer) — none references this page or a 123-plus-SMA/time exit rule. Nearest pool neighbors are materially different (see Deduplication).

## Economic mechanism

### Source-reported

A bullish 123 washout is treated as the pullback to buy: four chained lower-low/lower-high prints mark short-term capitulation. The trade is held at most 7 bars or until the close reclaims the 200-day average — whichever comes first — betting the washout resolves upward inside the long-term trend before time decay gives the profit back. No profit claim is made.

### Research interpretation

A time-bounded pullback holder with a trend-reclaim escape hatch, long-only with an explicit flat state. Unlike pure channel-touch systems that buy any fresh extreme, this system requires the full 4-print chain, so isolated single-bar dips never fire. Unlike open-ended holders, every position has a predeclared maximum life (7 completed bars) plus an earlier reclaim exit — overbought highs while flat are no-ops, and washouts printing below an unsettled average are still bought (the gate is the reclaim exit, not a regime filter). Same-bar entry+exit prints net flat by source order. Close-only fills can print away from pattern levels when the bar gaps — a disclosed research convention, not a source promise.

## Signal

**Market and candle contract:** one continuous UTC-aligned real Binance `BTC-USDT` **spot 1d** OHLCV series. Let `T[t]` be the actual candle *opening* Unix timestamp, `D=86400` seconds, and `C[t]` its actual close. A row is decision-eligible only at or after `T[t]+D`, never at its opening timestamp. Require consecutive daily timestamps, finite positive O/H/L/C, H>=max(O,C), L<=min(O,C), and finite nonnegative volume on every bar used. Missing, duplicated or malformed input **aborts the research run** rather than forward-filling or fabricating a price. This failure fence is researcher-defined, not a source claim. Comparisons need no division, so zero-range bars stay evaluable.

For each completed bar `t` (statements execute in source order — entry `if` before exit `if`, so a bar where both fire enters then immediately exits at the same close, ending flat):

- `c1[t] := L[t] < L[t-1]`; `c2[t] := L[t-1] < L[t-3]`; `c3[t] := L[t-2] < L[t-4]`; `c4[t] := H[t-2] < H[t-3]` (needs `t>=4`; all strict — equality on any leg never fires).
- `entry[t] := c1 and c2 and c3 and c4` with frozen literals (no parameter to choose).
- `ma200[t] := SMA(C[t-199..t])` (needs 200 completed closes; `na` until settled — pre-warmup bars never decide).
- `barsSince[t] := t - lastEntryBar` where `lastEntryBar` is the most recent bar with `entry=true`, else undefined (`ta.barssince` semantics: `0` on the entry bar itself, `na` if never fired — `na>=7` is false, never an exit).
- `exit[t] := (barsSince[t] >= 7) or (C[t] >= ma200[t])` (both inclusive — `barsSince==7` and `C==ma` fire).

**Warmup:** 250 consecutive valid, fully completed daily candles from the predetermined sample start (200-bar SMA settlement plus the 5-bar pattern and 7-bar hold transient with margin); begin FLAT with no entry history. Do not trade on the first 250 rows; the first eligible decision is on row index >=250. Do not re-seed levels mid-sample or normalize using full-sample values.

**State and event priority (complete derivative, source order entry-first):**

1. One position state `FLAT` or `LONG(Q)`, `Q=Decimal("0.001") BTC`, plus at most one pending order. Confirmed fills, not intents, update state. While pending, no new action.
2. If FLAT at a completed bar: if `entry[t]` is true, issue exactly one MARKET BUY of Q at that bar's observed close, provided `cash>=Q*C[t]*(1+f)` with `f=0.0001`. If insufficient, remain flat and do not assume borrowing. If `exit[t]` is also true on that same entry bar, immediately issue the matching MARKET SELL at the same close on confirmed BUY fill, ending FLAT (source-order same-bar round trip; two fees apply). A lone `exit[t]` while FLAT is a no-op. On confirmed full BUY, record `entryPrice=C[t]`.
3. If LONG at a completed bar: a co-firing `entry[t]` is a no-op (single-unit, no adds/DCA/pyramiding). If `exit[t]` is true, issue exactly one MARKET SELL of full Q at that bar's observed close and return FLAT on confirmed fill. Otherwise hold. There is no same-entry-bar exit beyond the source-order same-bar case above.
4. After a confirmed SELL, return FLAT with entry history retained for `barssince` continuity (signal-level memory, not position memory); the next completed bar may enter only on a fresh `entry` print. No other cooldown. No stop loss, take profit, trailing, partial exits, leverage, margin, borrowing, compounding, short leg, or hidden executor defaults.
5. Any rejected, missing, partial, unresolved or ambiguous MARKET fill aborts this bounded research run; do not infer a fill, repeat an unconfirmed order, or synthesize cash/position. At the predetermined sample end, mark a remaining LONG at the actual last completed close, with **no invented liquidation**.

## Required data and causality

Exactly one contiguous UTC daily Binance spot OHLCV stream and its real opening timestamps. The rule reads **High/Low for the 123 chain and Close for the average, both exit rails and all fills** — Volume is never order-gating. All references are bars `t-4..t` plus the 200-bar average window, complete at decision time; no future data, no unconfirmed intrabar values, no repainting, no full-sample normalization, no model fitting. The `basePeriod: 1d` from the source header equals the decision frame, so no second frame exists. Missing prices block signals and fills rather than defaulting to synthetic prices.

## Execution assumptions and pinned Hummingbot compatibility

**Gate 5 is bounded to a real inspected pinned simulation path, not a deployment claim.** Admission policy identifies Hummingbot package label **20260920**, VERSION **dev-2.17.0**. The inspected source is **HCH725/hummingbot at commit 8b0e067e80ab62f10846d518dcb5a8218527ddb3**; its `hummingbot/VERSION` file reads `dev-2.17.0` (verified this cycle). No package-to-commit byte-match is claimed; the engine claim is limited to this pinned source plus previously reviewed matching research semantics. Sibling PASS records remain path evidence only, never proof of this candidate.

- **Market/data:** BinanceSpotCandles `constants.py` `INTERVALS` bidict includes `1d` (verified this cycle at the pin); `_parse_rest_candles` maps REST `row[0]` to opening timestamp and `row[1..5]` to O/H/L/C/V (verified this cycle at the pin). A strategy-specific controller must compute the declared 4-condition chain, 200-bar SMA, and `barssince` counter, verify contiguous completed bars, and supply a single BTC-USDT spot 1d stream. The engine does not magically implement this pullback signal.
- **Controller/action/executor:** `BacktestingEngineBase.simulate_execution` iterates processed rows, calls controller `determine_executor_actions()`, and routes each `CreateExecutorAction` over the current-row forward slice to `simulate_executor` — row path verified this cycle at the pin. `OrderExecutorConfig` admits `connector_name="binance"`, `trading_pair="BTC-USDT"`, BUY/SELL, `amount=Decimal("0.001")`, `position_action=OPEN/CLOSE`, `execution_strategy=MARKET`, `price=None` (verified this cycle at the pin; `leverage` defaults to 1). `OrderExecutorSimulator.simulate` fills MARKET orders at the first supplied row's timestamp with that row's `close` as entry price, sets `filled_amount_quote=Q*close` and `cum_fees_quote=trade_cost*Q*close`, and reports `CloseType.POSITION_HOLD` (verified this cycle at the pin). Full fill at one close is an explicit simulator convention, not proof of executable spot fills.
- **Timestamp caveat:** raw Binance daily row timestamps are **open** labels. The engine joins features with backward as-of on timestamp; that join alone does not establish that a completed close was known at the open. The required derivative controller gates each completed bar until **open+86400s**, and the research event/fill ledger is normalized to that close-effective timestamp while using the simulator's same-row close price. This is a disclosed adaptation away from the original default timing and does not claim a real post-close order could fill at the observed close. No intrabar or lower-timeframe path is assumed.
- **Position and ledger:** `BacktestPositionHold` nets equal-base BUY/SELL ("Buys and sells of the same asset net out automatically. Realized PnL comes from matched buy/sell volume", verified this cycle at the pin), tracking average entry, gross matched realized PnL and accumulated fees separately. The engine's `terminated_executors_window` default is 3600 seconds (`DEFAULT_TERMINATED_EXECUTORS_WINDOW = 60*60`, verified this cycle at the pin) — pin it to `None` and use persistent pending/fill-confirmed controller state so daily positions are never lost to the one-hour view and duplicate orders are never sent. After a 0.001 BTC BUY at `P_b` and SELL at `P_s`, modeled net quote PnL = `0.001*(P_s-P_b) - 0.0001*0.001*(P_b+P_s)`; never misreport gross native PnL as fee-net equity. An open position's marked equity carries the already-paid BUY fee.
- **Costs:** pin simulator `trade_cost=0.0001` per filled side (0.01%, researcher-selected house research input — the source models no costs and no rate is attributed to it). Zero additional modeled slippage is **zero additional modeled slippage**, not evidence of zero spread/latency. Spot funding is inapplicable by construction (no fabricated futures funding). Minimum notional, lot/tick precision, partial fills, liquidity and live viability remain unverified; `BacktestingDataProvider.get_price_by_type` can fall back to `Decimal("1")` (verified this cycle at the pin), which is expressly **forbidden** for trade pricing. Validate the original full candle sequence **before** any engine `dropna` processing.
- **Reused independent path review:** HCH725/alpha-strategy-research PR **#417** (merged 2026-10-24) independently reviewed this same pinned Binance spot 1d / MARKET first-close / POSITION_HOLD fee-ledger research path. That verifies an **engine primitive**, not this new signal, trade series, profitability, package digest or candidate-specific parity. This cycle additionally re-read the pinned VERSION, spot candle constants/parser, engine row/action routing, OrderExecutorSimulator, BacktestPositionHold netting, data-types config and price-fallback guard at the pin.

## Evidence

### Source-reported

FMZ page identity (471698, ChaoZhang, 2024-11-12), 1d decision period header with matching 1d basePeriod, the frozen 7/200 literals, the 4-line 123 chain plus time-or-reclaim exit quoted in Provenance, long-only book, and absence of any performance numbers on the page. No performance numbers exist on the page to reproduce.

### Independently reproduced

**Rule-logic self-check (stdlib only, not a backtest):** the frozen chain-plus-hold machine with FLAT/LONG book was executed over hand-constructed bars and 5x400-bar fuzz streams — crafted 4-print washout fires BUY; equality on any chain leg blocks entry; sub-average hold exits exactly 7 bars later; above-average close reclaims the next bar; same-bar entry+exit nets flat at one close; pre-warmup bars never decide; BUY/BUY and SELL/SELL never repeat across all fuzz seeds. **Engine-code inspection only, not a strategy backtest:** the pinned files above were read line-by-line this cycle (VERSION bytes, `1d` interval entry, REST row mapping, `simulate_execution` row/action routing, MARKET first-row-close fill, quote-notional fee accumulator, POSITION_HOLD ledger, 3600s executor window, `Decimal("1")` fallback guard). The candidate's trade events, FMZ outputs, Qlib/Hummingbot parity and net returns have **not** been independently reproduced. No backtest was executed.

### Negative evidence

No sizing, warmup, cost, fill-timing or framework-default order setting ships in the retrieved source; **source-native/lossless equivalence is unverified** and this record claims none. A washout that never reclaims and never ages out within the sample leaves the long exposed with no stop or target. Simulated completed-close fills can print away from pattern levels and are a backtest convention, not a live guarantee. No verified next-open fill, partial fill, market impact, fee schedule, futures funding or venue size permission. None is silently imputed.

## Deduplication

Nearest pool neighbors are **not equivalent**: `combo-123-reversal-fisher-transform-two-sided-btcusdt-4h-2026-10-15` (FMZ 426618) gates its 123 with a Fisher-transform agreement, trades **two-sided** on **4h** with 6 inputs and a 2-entry + `close_all` book — this record has no oscillator, no second side, no `close_all`, trades **long-flat** on **1d** with 2 frozen literals and a 1-entry + 1-close book, so Fisher-disagreement bars fire here that never fire there and short legs fire there that never exist here. `elder-ray-123reversal-combo-two-sided-btcusdt-1h-2026-10-09` (FMZ 432762) gates its 123 with Elder Ray bull-power, trades **two-sided** on **1h** with 7 inputs — this record has no Elder Ray, no second side, a 7-bar time rail and an SMA200 reclaim rail neither neighbor owns, on a different horizon. Different source, different signal construction, different risk book, different horizon/direction: not a duplicate, paraphrase, or trivial parameter variant. The pooled `double-seven-connors-pullback` (FMZ 473246) is the same publisher but a different mechanism (7-day lowest-close touch under SMA200 with channel-high exit — no 123 chain, no time rail).

## Falsification plan

After separate downstream research authorization, compare the frozen rule against (a) the same 123 chain with the 7-bar time rail removed (reclaim-only exit), and (b) the same chain with the SMA reclaim removed (time-only exit), on predeclared IS/OOS partitions; verify each rail actually changes exit event times. Any new or unverified execution/data primitive requires representative Qlib/Hummingbot event-level validation before mass screening. Do not tune on OOS. No backtest was run by Scout.

## Crypto portability

Native crypto venue by declaration (Binance BTC-USDT spot 1d); the Futures_Binance header of the source sample is adapted to spot by explicit researcher choice, removing funding by construction rather than observing it. Minimum-notional, precision, liquidity and live viability remain unverified limitations, never assumed. House DCA 6/6/6 and 3x/5x futures are optional **separate downstream experiments**, not prerequisites and not silently part of this frozen version.

## Limitations

- A breakdown that keeps printing fresh washouts can re-enter immediately after a time exit; a grind that never reclaims and never prints a fresh chain leaves the long exposed with no stop, target or further time exit until bar 7.
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

- FMZ primary: https://www.fmz.com/strategy/471698 (123 Reversal Trading Strategy, ChaoZhang / EdgeTools MPL-2.0, created 2024-11-12; page directly read 2026-10-26).
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Existing independent package/engine primitive review: https://github.com/HCH725/alpha-strategy-research/pull/417
