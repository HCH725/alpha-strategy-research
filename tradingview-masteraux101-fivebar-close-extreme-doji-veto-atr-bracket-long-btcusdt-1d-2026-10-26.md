---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: masteraux101 five-bar close-at-extreme count with doji veto and fixed ATR close-bracket, BTC-USDT spot 1d long-flat independent derivative
created: 2026-10-26
updated: 2026-10-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-12-15
sources:
  - https://www.tradingview.com/script/Vufc1HaC/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Five-bar close-at-extreme persistence with doji veto — independent long-flat derivative

## Provenance

**TradingView primary source:** masteraux101, *Simple Candle Strategy* / *Candle Pattern Strategy - Pine Script V6*, published **2025-12-15**, author-stated **version 1.0**, stable script ID **Vufc1HaC**, public/open-source listing: https://www.tradingview.com/script/Vufc1HaC/ . First-party page read 2026-10-26. The description supplies explicit formulas for close-near-high, close-near-low and doji classifications; a 5-bar count, three-doji veto, >=2 matching extreme bars and last-bar confirmation; two-sided signals; and ATR x2 stop / ATR x3 target. It does not expose complete Pine source bytes or strategy fill settings in the available text. Do **not** claim Pine-byte identity, original-order-event equivalence, or source performance reproduction.

**Independent derivative, not a source-native/lossless Pine port.** Source-native *ideas* retained: count last five bars near their respective extremes; skip pattern signals on >=3 dojis; bullish long pattern, bearish opposing pattern; ATR-based risk-distance concept. Researcher-defined and materially different: Binance BTC-USDT **spot 1d**, LONG/FLAT only (original short entry disabled), bearish source signal becomes a long close; fixed 0.001 BTC, 10,000 USDT initial unborrowed cash, fixed ATR14 Wilder from entry, **completed-close-triggered** stop/target instead of any original intrabar/resting bracket, historical same-row close MARKET fills, fixed research fees, explicit data and failed-fill policy, 80-bar warmup, state/priority/re-entry semantics. The source's default 100%-equity sizing and any original short/intrabar behavior are **not** reproduced. No change is attributed silently to the author.

**Immutable candidate identity (research spec, not a source-code hash):** `TV:Vufc1HaC:masteraux101:2025-12-15:v1.0 | independently-derived-v1:2026-10-26 | Binance BTC-USDT spot 1d | last5 CH/CL >=2, last-bar confirmation, doji5<3 | LONG CH, bearish CL exit | ATR14 fixed close stop2/target3 | Q=0.001 BTC | close-effective MARKET | fee=0.001/side | warmup80`. Changing signal counts, geometry, bar timeframe, side, exit, fill, costs, or state requires a separately disclosed revision.

**Dedup check:** `main@ae8eeded13853c6f83946bdb8a0e2829e62a93b3` has 359 root-level strategy Markdown files and static README count 359; GitHub code search for `Vufc1HaC` and `close_at_high_count` returned none. All 10 then-open PRs were enumerated: none references this script or the five-bar **close-at-extreme count plus doji-veto** rule. Nearby main strategies are materially different: `three-white-soldiers-black-crows` uses ordered 3-bar body/position patterns, `1-3-1-red-green` uses a red-then-three-green color sequence, `dual-ema-engulfing-volume` uses engulfing/EMA/volume. This candidate counts near-extreme closes in a five-bar unordered window and applies a >=3 doji veto, not a trivial parameter variation. Count equality alone is not claimed to prove an independent audit of all 359 pre-existing statuses.

## Economic mechanism

### Source-reported
The author proposes that repeated closes near candle highs/lows within a short lookback indicate directional pressure, while frequent dojis imply indecision warranting a skip. The page describes ATR x2/x3 risk brackets, but provides no independently verified profit or backtest outcome.

### Research interpretation
A majority-like count of close-location extremes with a most-recent-bar confirmation may detect short-run persistence without relying on a moving-average trend. The doji veto attempts to avoid mixed indecision. Its benefit is untested; close-only ATR exits can be worse than intended bracket prices during jumps.

## Signal

**Market and candle contract:** one continuous UTC-aligned real Binance `BTC-USDT` **spot 1d** OHLCV series. Let `T[t]` be the actual candle *opening* Unix timestamp, `D=86400` seconds, and `C[t]` its actual close. A row is decision-eligible only at or after `T[t]+D`, never at its opening timestamp. Require consecutive daily timestamps, finite positive O/H/L/C, H>=max(O,C), L<=min(O,C), finite nonnegative volume, and **H>L** on every bar used by the five-bar classifier. Missing, duplicated, zero-range or malformed input **aborts the research run** rather than dividing by zero, dropping/forward-filling, or fabricating a price. This is a deliberately conservative researcher-defined failure fence, not a source claim.

For each completed bar `j`, let `R[j]=H[j]-L[j]>0`:
- `CH[j] := (H[j]-C[j])/R[j] <= 0.10` (source default high proximity 0.90).
- `CL[j] := (C[j]-L[j])/R[j] <= 0.10` (source default low proximity 0.90).
- `DOJI[j] := abs(C[j]-O[j])/R[j] <= 0.10` (source default doji threshold 0.10).

At each completed `t` with five valid bars `t-4..t`, count `nH=sum(CH)`, `nL=sum(CL)`, `nD=sum(DOJI)`. Pattern skip if `nD>=3`. Otherwise `bull := (nH>=2 and CH[t])`; `bear := (nL>=2 and CL[t])`. Exact equality at <= thresholds counts; `nD=3` skips. Since `R[t]>0`, `CH[t]` and `CL[t]` cannot both be true at the 0.10 cutoffs. Pattern skip **does not disable risk exits**. All five bars include the just-completed current bar; no future or shifted reference is used.

**ATR for risk:** Wilder ATR14 on completed daily bars: `TR[0]=H[0]-L[0]`; for `j>=1`, `TR[j]=max(H[j]-L[j], abs(H[j]-C[j-1]), abs(L[j]-C[j-1]))`. `ATR[13]` is the arithmetic mean of `TR[0..13]`; thereafter `ATR[j]=(13*ATR[j-1]+TR[j])/14`. Require finite `ATR[t]>0` for entry. This indicator length, seed, entry-time freeze and all ATR execution semantics are **researcher choices**; the page only specifies ATR x2/x3 distances.

**Warmup:** 80 consecutive valid, fully completed daily candles from the predetermined sample start; begin FLAT with no inferred earlier position. Do not trade on the first 80 rows; the first eligible signal is on row index >=80, using the prior five completed bars and initialized ATR. Do not re-seed ATR mid-sample or normalize using full-sample values.

**State and event priority (complete derivative):**
1. One position state `FLAT` or `LONG(Q)`, `Q=Decimal("0.001") BTC`, plus at most one pending order. Confirmed fills, not intents, update state. While pending, no new action.
2. If LONG, on each *subsequent* completed bar after its entry: first SELL full Q at the observed close if `C[t]<=stop` (close-stop); else if `C[t]>=target` (close-target); else if `bear` and `nD<3` (bearish pattern exit); otherwise hold. Stop/target labels take precedence over bearish exit; exactly one SELL. There is no same-entry-bar exit.
3. If FLAT at the start of a completed bar and `nD<3 and bull`, issue exactly one MARKET BUY Q at that bar's observed close, provided `cash>=Q*C[t]*(1+f)` with `f=0.001`. If insufficient, remain flat and do not assume borrowing. On confirmed full BUY, set `entryPrice=C[t]`, `entryATR=ATR[t]`, **fixed** `stop=entryPrice-2*entryATR`, `target=entryPrice+3*entryATR`; require `stop>0`, `target>entryPrice`. If these conditions fail, no trade and flag invalid setup. These are **close-based** triggers, not intrabar touch orders or guaranteed threshold fills.
4. After a confirmed SELL, return FLAT and prohibit same-bar re-entry; the next completed bar may enter if it independently satisfies bull. No other cooldown. A repeated bull while LONG is a no-op; a bear while FLAT is a no-op. No pyramiding, DCA/BO/SO, safety orders, concurrent trades, partial exits, trailing, time exits, reversal-to-short, leverage, margin, borrowing, compounding, or hidden Hummingbot executor defaults. Original source short leg is disabled.
5. Any rejected, missing, partial, unresolved or ambiguous MARKET fill aborts this bounded research run; do not infer a fill, repeat an unconfirmed order, or synthesize cash/position. At the predetermined sample end, mark a remaining LONG to the actual last completed close, with **no invented liquidation**.

## Required data

Exactly one contiguous UTC daily Binance spot OHLCV stream and its real opening timestamps. No other symbols, sessions, book data, fitted model, lower/higher timeframe, corporate actions, funding series, mark/index price, or synthetic Heikin-Ashi data. All computations are online-prefix deterministic and use `t` and prior completed bars only.

## Execution assumptions — pinned-engine evidence

**Pinned model:** Hummingbot package `20260920`, VERSION `dev-2.17.0`; immutable source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. The connected GitHub app directly re-read this commit's `hummingbot/VERSION`, BinanceSpotCandles `constants.py` / `binance_spot_candles.py`, `strategy_v2/backtesting/backtesting_engine_base.py`, `executors_simulator/order_executor_simulator.py`, `backtesting_data_provider.py`, and `executors/order_executor/data_types.py` on 2026-10-26. Prior independently reviewed Alpha PR #414 provides package/source 902-file wheel-byte correspondence and primitive net/fee evidence; **this Scout did not rehash or execute the installed wheel**, and the present candidate has no implemented controller.

**Actual supported path:** BinanceSpotCandles `INTERVALS` includes `1d`; REST `_parse_rest_candles` maps row[0] to opening timestamp and row[1..5] to actual O/H/L/C/V. `BacktestingEngineBase.simulate_execution` advances prepared rows via `update_state(row)`, then controller `determine_executor_actions()`, then `CreateExecutorAction` -> `simulate_executor`. `OrderExecutorConfig` admits `connector_name="binance"`, `trading_pair="BTC-USDT"`, BUY/SELL, `amount=Decimal("0.001")`, `position_action=OPEN/CLOSE`, `execution_strategy=MARKET`, `price=None`, `leverage=1`. `OrderExecutorSimulator.simulate` uses first supplied row's real `close` for MARKET fill price and row's opening `timestamp` as its label; it sets `filled_amount_quote=Q*close`, `cum_fees_quote=trade_cost*Q*close`, and `CloseType.POSITION_HOLD`. `BacktestPositionHold` nets opposite BUY/SELL amounts, calculates gross realized/unrealized PnL and separately accumulates quote fees. A controller must wait for confirmed full fills and maintain a persistent position/order ledger (or `terminated_executors_window=None`), not mistake the default one-hour terminated-executor view for durable daily position state.

**Causality mapping:** raw Binance daily row timestamp is **open**, but the MARKET simulator consumes its **close**. This derivative defines both the signal decision and the simulated fill as effective only at **open+86400s**; using the raw open label as a real-time signal/fill would be future leakage. Historical same-row close is an **idealized research execution convention**; it is not a claim that a live order sent after candle completion could fill at the historic close. The exact original Pine `process_orders_on_close` is unknown and no source-native equivalence is asserted.

**Costs and accounting:** explicit `trade_cost=0.001` is a **hypothetical** 0.1% fee on each filled side, not a verified Binance tariff. For one round trip `netQuote=Q*(exitClose-entryClose)-f*Q*(entryClose+exitClose)`; the controller cash ledger debits `Q*entryClose*(1+f)` and credits `Q*exitClose*(1-f)`. Gross Hummingbot position PnL must not be mistaken for fee-net equity. MARKET close path has zero **modeled** slippage; real spread, latency, actual fee tier, lot/tick precision, min notional, partial fills and live close execution are **not verified** and are not silently assumed favorable. Spot has no perpetual funding payment; this is **not** an observation of zero funding on futures. No futures margin/funding, maker queue, intrabar bracket, multi-asset shared capital or next-open fill is needed by this specific derivative. Reject missing/invalid real prices; `BacktestingDataProvider.get_price_by_type` can fall back to `Decimal("1")`, which is expressly **forbidden** for trade pricing. Validate the original full candle sequence **before** any engine `dropna` processing.

## Evidence

### Source-reported
TradingView first-party description (2025-12-15, masteraux101, version 1.0, Pine v6) prints the three close-location/body-to-range ratios, 5-bar default, 0.90 high/low proximity, 0.10 doji threshold, 3-doji veto, >=2 matching close-at-extreme count with last-bar confirmation, long/short actions, ATR x2/x3 bracket concept and 100%-equity default. Full executable Pine source bytes and original order-processing details were not retrieved.

### Independently reproduced
No strategy PnL, Pine trade sequence, Hummingbot run, Qlib parity, OOS or survivor statistics independently reproduced. Pinned engine *source paths* were read and previously reviewed engine primitive evidence (#414) reused; no dedicated controller or exchange execution has been tested.

### Negative evidence
GitHub source search found no existing `Vufc1HaC` / five-bar `close_at_high_count` record. The closest admitted candlestick families require ordered color sequences, engulfing or EMA/volume conditions, not this five-bar unordered count with doji-veto. Original Pine source fill mode, ATR length/seed, risk order mechanics and cash rules remain unknown; they are **not invented as author facts**. The independent derivative fully pins these decisions instead. A source-native equivalence claim would fail without the missing Pine bytes.

## Six-gate assessment — Scout proposal, subject to independent Auditor

1. **Deterministic:** all three exact geometry ratios, 5-bar counts, tie operators, skip priority, ATR14 Wilder seed, 80-bar warmup, cash/fill/fee parameters and state are frozen.
2. **Direction:** BTC-USDT spot LONG/FLAT; source SHORT explicitly disabled; no leverage, margin or borrowing.
3. **Entries/exits/risk:** bull entry; subsequent fixed ATR2 close-stop, ATR3 close-target or bear close, with exit-reason priority stop first, then target, then bearish pattern; all other exits and executor defaults explicitly disabled.
4. **Position:** 0.001 BTC full fills, one outstanding order, no adds/DCA/concurrency, no same-bar re-entry, next-bar independent re-entry only, cash affordability and unresolved-fill abort.
5. **Pinned model:** real 1d Binance spot feed, controller/action loop, MARKET close-fill simulator, position-hold netting and separate quote fees examined at immutable Hummingbot commit; bounded modeled costs and explicit economic limitations, no invented missing price/funding.
6. **Causality:** completed bars only, ATR prefix seed, 80-bar warmup, daily open timestamps mapped to completed-close effective time, no repainting, future extrema or full-sample leakage.

PASS here means **expressible research specification**, not a deployed controller, profitable strategy, verified original Pine equivalence, Qlib parity, HB certification or trading authorization.

## Falsification plan

Not executed: on frozen IS data, compare the count+doji-veto mechanism against (a) the same count without the doji veto and (b) last-bar-only CH entries; examine changed trade events and net economics under the identical explicit cost model. Independently test exact CH/CL/doji boundary ties, `nD=3` veto, zero-range abort, bullish/bearish exclusivity, a simultaneous bearish/stop trigger, 80-bar warmup, cash shortage, missing day, rejected/partial fills, no same-bar re-entry, stop/target gaps, and timestamp open-to-close mapping. No OOS retuning.

## Crypto portability

Single-asset BTC-USDT spot 1d is a **research choice**, not an HB_READY whitelist or a claim about the source author's market. Ratio-based candle geometry is price-scale independent, but 24/7 crypto volatility and daily session boundaries change the pattern frequency. House DCA 6/6/6 and 3x/5x futures are optional **separate downstream experiments**, not prerequisites and not silently part of this frozen version.

## Limitations

The original Pine code is not available in this text inspection; all non-source-native execution decisions are explicitly researcher-authored. Close-only stop/target modeling can understate adverse excursions; historical same-row close MARKET fills are idealized and not executable live guarantees. Costs exclude unverified exchange-specific friction. Abort on zero-range/missing data can reduce coverage; this is deliberate and must not be disguised as successful full coverage. No strategy implementation, Qlib/HB event-level parity or independent performance evidence exists. Validate any genuinely new execution primitive with one representative parity check before mass screening; final HB certification requires strategy-specific event-level and economic agreement.

## Implementation status

`not-implemented`: no dedicated Hummingbot controller, no Qlib executable recipe, no backtest, no deployment. An admitted PASS record is a research specification, not a claim of ready-to-run artifacts.

## Adoption boundary

`research-only`; `not-approved`. No Paper/Testnet/Live or portfolio allocation authorization. Hermes Auditor alone determines exact-head PASS merge or NOT_LOSSLESS close. Existing signed webhook receiver alone maintains the post-merge README count.

## Related Wiki records

None claimed.

## Sources

- TradingView primary: https://www.tradingview.com/script/Vufc1HaC/ (masteraux101, 2025-12-15, v1.0, public description directly read 2026-10-26).
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Existing independent package/engine primitive review: https://github.com/HCH725/alpha-strategy-research/pull/414
