---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Alorse QQE first trailing-side transition long-flat, previous trail-50 truthy gate"
created: 2026-10-16
updated: 2026-10-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-16
sources:
  - https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/momentum/QQE%20signals.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Alorse QQE first trailing-side transition long-flat, previous trail-50 truthy gate

## Provenance

Full source Pine v4 read directly: https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/momentum/QQE%20signals.pine, immutable repository revision `8fb3837ddcd137f1450c3e82d654ff3df24d54d5`, path `strategies/momentum/QQE signals.pine`. File header credits **colinmck**; Alorse is repository collector/strategy variant author, not asserted sole originator. It declares `pyramiding=0`, capital 1000 USD, source dynamic 10% equity stake, commission 0.01% one way. No timeframe fixed by source and no multi-timeframe calls. No source `process_orders_on_close`; market orders normally next-bar OPEN.

This is **NOT** a duplicate of main `qqe-fast-slow-cross-two-sided` (source from FMZ/Kivanc, QQE factor 4.236, FAST vs SLOW strict cross and two-sided reversal). Alorse's version uses `QQE=4.238`, a different dual-band ratchet/trend conditional, counts first bar of `FastAtrRsiTL` relative to smoothed RSI, uses `FastAtrRsiTL[1]-50` numeric truthiness as a further order gate, and default is **long-flat** (Short order commented out); exit is the QQExshort event, not a short reversal. All these must survive normalization, not be replaced by generic QQE crossover.

## Economic mechanism

Smoothed RSI-volatility trailing-band side change marks a first upward/downward persistence bar. The source numeric plot signal passes the previous trailing level minus 50 to Pine `strategy.when`; this is not the same as asking current RSI or trail to be above/below 50.

## Signal — exact state recurrence and order arguments

- Defaults `RSI_Period=14`, `SF=5`, `QQE=4.238`, `ThreshHold=10` (the latter input is **never used in any active calculation/order**). `src=close`; `Wilders_Period = 2*14−1 = 27`.
- `Rsi = rsi(close,14)`; `RsiMa = ema(Rsi,5)`; `AtrRsi=abs(RsiMa[1]-RsiMa)`; `MaAtrRsi=ema(AtrRsi,27)`; `dar=ema(MaAtrRsi,27)*4.238`. `RSIndex=RsiMa`. `newshortband=RSIndex+dar`, `newlongband=RSIndex-dar`.
- Stateful ratchets with previous bar (carry explicit Pine initialized `longband=0.0`, `shortband=0.0` prior to reassignment): `longband[t] = (RSIndex[t-1]>longband[t-1] AND RSIndex[t]>longband[t-1]) ? max(longband[t-1],newlongband[t]) : newlongband[t]`. `shortband[t] = (RSIndex[t-1]<shortband[t-1] AND RSIndex[t]<shortband[t-1]) ? min(shortband[t-1],newshortband[t]) : newshortband[t]`.
- `cross_1 = cross(longband[1], RSIndex)`, `trend = cross(RSIndex,shortband[1]) ? 1 : cross_1 ? -1 : nz(trend[1],1)`, so the first `cross` has precedence if both could be true. `FastAtrRsiTL = trend==1 ? longband : shortband`.
- Stateful first-side-run counters start `QQExlong=0`, `QQExshort=0` and update per bar: `QQExlong[t] = FastAtrRsiTL[t]<RSIndex[t] ? nz(QQExlong[t-1])+1 : 0`; `QQExshort[t] = FastAtrRsiTL[t]>RSIndex[t] ? nz(QQExshort[t-1])+1 : 0`. Strict comparisons, not cross() alone.
- `qqeLong[t] = QQExlong[t]==1 ? FastAtrRsiTL[t-1]-50 : na`; `qqeShort[t]=QQExshort[t]==1 ? FastAtrRsiTL[t-1]-50 : na`. **Original Pine passes these numeric series as `when`**. The explicitly derived executable boolean normalization is `!na(qqeLong) && qqeLong != 0` for entry, and `!na(qqeShort) && qqeShort != 0` for exit (Pine v4 numeric-to-bool truthy behavior; equality exactly 50 suppresses that one transition; these are not plot-only). If the source's actual Pine compiler rejects numeric when instead of implicitly converting, this boolean cast is a **declared syntax normalization** preserving intended numeric truth semantics; never rewrite it as `FastAtrRsiTL>50` or generic QQE K/D cross.
- Source active order calls: `strategy.entry("Long",true,when=qqeLong)`, `strategy.close("Long",when=qqeShort)`. Short `strategy.entry` is commented out and never active. No price stop, TP, trailing/time exit, risk order, cooldown, DCA or short exposure; `pyramiding=0`, one held long or flat, repeated source-long while positioned suppressed, after flat eligible reentry.
- First-side count equality 1 guarantees the two numerically gated long/short signals cannot fire on the same bar (FastAtrRsiTL<RSIndex and >RSIndex mutually exclusive). No same-bar action ordering hazard.
- Conservative researcher-selected **150 complete bars** flat warmup: RSI14, EMA5, double EMA27, recursive ratchets plus one previous trail. Source calculation itself is past-only; no future, `security` or confirmation delay. The artificial warmup is explicitly a research derivative, not an author input.

## Execution assumptions — bounded spot research derivative and pinned evidence

Market selection: spot `binance BTC-USDT 1h`, one symbol and one candle frame (filename supplies no fixed exchange). Signals calculated on complete t; saved and acted upon strictly on next available simulator candle t+1 **at CLOSE**, preserving source boolean events but NOT Pine native next-open execution or fill prices. Last-row signal remains pending/unfilled. Fixed 100 USDT entry notional from 1000 USDT initial research capital (source 10%-of-current-equity differs; openly derived), SELL exact held base BTC amount, quantize via Binance trade rules and fail rather than invent sub-min order. Synthetic 0.01% each side `trade_cost=0.0001` (numeric source fee model only, not actual Binance VIP/maker tier or slippage). Spot no perpetual funding, leverage/isolated liquidation; house derivatives/DCA are later separately modeled.

Source-matched native Hummingbot snapshot: `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` from 2026-09-20, `hummingbot/VERSION=dev-2.17.0` as mandatory package-version evidence. `BacktestingEngineBase.run_backtesting(...,backtesting_resolution="1h",trade_cost=0.0001)` and `prepare_market_data` load timestamped OHLCV; `simulate_execution` runs cached indicator feature decisions and `controller.determine_executor_actions()` per row, routes `OrderExecutorConfig` `CreateExecutorAction` to `OrderExecutorSimulator`. Native `order_executor_simulator.py` MARKET fills at first row CLOSE, charges `trade_cost*amount_quote`, returns `POSITION_HOLD`. `BacktestPositionHold` nets opposite BUY/SELL, records realized PnL and fees; `BacktestingDataProvider` keys `binance_BTC-USDT_1h`, validates trading rules and quantizes amounts. Existing `controllers/generic/pmm_mister.py` demonstrates native MARKET OrderExecutor action plumbing; QQE-specific signal/controller not implemented yet (`implementation_status: not-implemented`), no new orchestration.

Version-pinned pre-existing tests reviewed, **not run**: `test_backtest_position_hold.py` buy/sell netting and full-close accounting tests, `test_backtesting_final_tick_ledger.py` Binance spot OrderExecutorConfig POSITION_HOLD terminal ledger, `test_backtesting_engine_directional.py` Binance candle/action/engine and adjustable trade cost. No strategy-specific executed backtest or current binary digest claimed.

## Evidence

Original source signal formula and numeric order payload pinned. Not a source-reported profitability claim; no independent realized trade data. This is an executable **declared syntax/execution derivative** only.

## Falsification plan

Generate QQE recurrence from completed close history, verify both first-side counters and exact nonzero previous trail−50 truth rule, plus 4.238 (not 4.236). Compare first eligible signals with source Pine and confirm no shorts, no extra later-bar entries from QQExlong>1, no trade before 150 bars. Explicit t+1 next-close fill, cost, quantity-netting; never claim unchanged source t+1 next-open results.

## Crypto portability

One current-chart close series required, author's test timeframe irrelevant. Other crypto pairs/frames/3x/5x futures plus BO/SO DCA are separate non-admitted execution overlays.

## Limitations

The `when=` numeric series in original Pine v4 is a source-language coercion ambiguity and could be a compile defect; zero and `na` handling must be verified by independent reviewer. Ratchet state and its strict-cross ordering must not be replaced by a generic QQE implementation. No price protective stop; only signal exit, and synthetic spot fee model omits spreads.

## Implementation status

`not-implemented`; no production code/runtimes touched.

## Adoption boundary

`research-only`, `not-approved`. Reviewer independently determines Gate 1 numeric truth semantics and canonical pinned Gate 5 compatibility; reject rather than fabricate missing semantics.

## Sources

- Primary https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/momentum/QQE%20signals.pine
- Hummingbot version https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/VERSION
- Native tests https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3/test/hummingbot/strategy_v2/backtesting
- Policy https://github.com/HCH725/alpha-strategy-research/blob/main/.github/HB_READY_REVIEW.md
