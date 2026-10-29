---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Vinicius Supertrend + volume + strong-candle + RSI long-flat BTCUSDT 1h (independent derivative)"
created: 2026-10-29
updated: 2026-10-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-04-18
sources:
  - https://www.tradingview.com/script/U98FoYXv/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Vinicius Supertrend / volume / candle-body / RSI long-flat — independent derivative

## Provenance

- **First-party TradingView source:** sidimarvinicius, *Vinicius Setup ATR*, publicly accessible open-source **strategy** page, published/updated **2025-04-18**, stable TradingView script ID **U98FoYXv**: https://www.tradingview.com/script/U98FoYXv/ . Directly inspected 2026-10-29. The accessible public description, not the complete Pine revision, is the verified source; do not attribute exact source Pine execution semantics to this record.
- **Source-reported construction:** Supertrend up/down direction, volume strictly above 1.2 times the previous-20-candle average, strong candle body relative to ATR, RSI filter below 70 for buy and above 30 for sell, optional/displayed support-resistance pivots of five bars on either side, and opposite-signal exits. The page does not establish Supertrend ATR length/multiplier, exact candle-body percentage, RSI length, whether the volume mean includes the current candle, whether candle polarity is mandatory, pivot usage in order predicates, original position state, or Pine fill/fee rules.
- **Explicitly INDEPENDENT DERIVATIVE (NOT source-native/lossless):** this research fixes Supertrend Wilder ATR14×3.0 with its own documented seed/state recurrence; bullish/bearish candle polarity; absolute body >0.5×ATR14; RSI14; inclusive-current-bar SMA20(volume)×1.2; BTC-USDT spot UTC 1h; long/flat only; one fixed 0.001 BTC unit; full opposite-conjunction exit; completed-bar signal and next completed-bar historical close MARKET fill; hypothetical 0.1% per-side fee. Five-left/five-right pivots are **not used** in this derivative because the source's public entry predicate does not establish them as a mandatory gate. Source shorts, pivot-based gating, any protective bracket, and original Pine execution are NOT claimed reproduced.
- **Immutable research identity:** `TV:U98FoYXv|sidimarvinicius|2025-04-18|independent-v1-20261029|BINANCE-BTC-USDT-SPOT-UTC1h|ST14x3-Wilder-SMAseed-DOWNseed|RSI14-Wilder|VOL20-current-gt1.2|BODY-gt0.5ATR|BUY-UP-bull-body-RSIlt70|SELL-DOWN-bear-body-RSIgt30|Q0.001BTC|cash10000USDT|t-signal-to-tplus1-completed-close-MARKET|fee0.001-side|warmup200`. Changing any event, seed, price, fee or state rule creates a new derivative identity, not a silent update.

## Economic mechanism

This derivative takes a long when a fully formed positive Supertrend regime coincides with an unusually active **bullish** candle of ATR-relative strength and non-overbought RSI. It exits only when a similarly strong **bearish** candle, negative Supertrend regime, elevated volume and RSI above 30 all coincide. The strict four-way opposite exit can leave positions unprotected for a long time. It is not a source-equivalent backtest, risk-controlled protective stop, profitability claim or exchange-ready execution strategy.

## Signal — deterministic version 1

Use one ordered series of completed Binance spot BTCUSDT UTC **1h** OHLCV bars, indexed `t=0,1,...`, computed with IEEE float64 deterministic recurrences. All `O,H,L,C,V` are actual observations; no fitted parameters, adaptive tuning, external signals, synthetic bars or future inputs.

1. `TR[0]=H[0]-L[0]`; for `t>=1`, `TR[t]=max(H[t]-L[t],abs(H[t]-C[t-1]),abs(L[t]-C[t-1]))`. `ATR14[13]=mean(TR[0..13])`; for `t>=14`, `ATR14[t]=(13*ATR14[t-1]+TR[t])/14`. Earlier ATR undefined. `ATR14[t]` must be finite and strictly positive to generate a signal.
2. `mid[t]=(H[t]+L[t])/2`; `BU[t]=mid[t]+3*ATR14[t]`, `BL[t]=mid[t]-3*ATR14[t]`. Seed `FU[13]=BU[13]`, `FL[13]=BL[13]`, `ST_DIRECTION[13]=DOWN` (researcher-chosen deterministic seed, not a claim about original Pine). For `t>=14`: `FU[t]=BU[t]` if `BU[t]<FU[t-1] OR C[t-1]>FU[t-1]`, otherwise `FU[t-1]`; `FL[t]=BL[t]` if `BL[t]>FL[t-1] OR C[t-1]<FL[t-1]`, otherwise `FL[t-1]`. If previous direction UP, switch DOWN iff `C[t]<FL[t]`, otherwise stay UP. If previous direction DOWN, switch UP iff `C[t]>FU[t]`, otherwise stay DOWN. Equalities never switch; no same-bar future data.
3. RSI14: `d[t]=C[t]-C[t-1]` for `t>=1`; `gain=max(d,0)`, `loss=max(-d,0)`. Seed `avg_gain[14]=mean(gain[1..14])`, `avg_loss[14]=mean(loss[1..14])`; for `t>14`, `avg[t]=(13*avg[t-1]+new[t])/14`. RSI `100-100/(1+avg_gain/avg_loss)`; if both averages zero set 50; if loss zero/gain positive set 100; if gain zero/loss positive set 0. Undefined before t=14.
4. `VMA20[t]=sum(V[t-19..t])/20` for `t>=19`; no previous-only lag. `VOL_OK[t]=(V[t]>1.2*VMA20[t])` and `VMA20[t]>0`. Equalities fail. `BODY_OK[t]=(abs(C[t]-O[t])>0.5*ATR14[t])`. `BULL_BODY[t]=(C[t]>O[t])`, `BEAR_BODY[t]=(C[t]<O[t])`; doji fails both.
5. `BUY[t]=(ST_DIRECTION[t]==UP) AND VOL_OK[t] AND BODY_OK[t] AND BULL_BODY[t] AND (RSI14[t]<70)`. `SELL[t]=(ST_DIRECTION[t]==DOWN) AND VOL_OK[t] AND BODY_OK[t] AND BEAR_BODY[t] AND (RSI14[t]>30)`. Strict thresholds, no implied RSI crossover or Supertrend flip-edge requirement; persistent valid states may signal on multiple completed bars, subject to position state.
6. Warmup `t=0..199` (200 complete bars) emits **no orders**. At `t>=200`, while FLAT and no pending action, BUY on completed bar `s` queues a single BUY action to the **next** completed bar `s+1`. At that next bar's actual observed CLOSE `P_b`, a verified full fill enters LONG. While LONG and no pending action, SELL on completed bar `e>=b+1` queues a full-size SELL to completed bar `e+1` close. SELL takes priority over BUY when LONG; BUY is ignored when LONG. Signals on the actual fill bar are ignored. No phantom final-row fills.
7. **Risk and disabled behavior:** only the opposite four-way SELL closes a position. Stop-loss, take-profit, trailing, time stop, session guard, intrabar high/low stop triggers, liquidation, forced end-of-data close, pyramiding, partial exits, short entry, borrow, margin, futures, funding and DCA/safety orders are **disabled**. A market gap can cause arbitrary adverse later-close fills; this is explicit risk, not an implicit stop.

## Required data and causality

- Required feed: actual Binance spot `BTC-USDT` 1h candles, open timestamp `T[t]` and finite positive O/H/L/C, finite nonnegative V; `H>=max(O,C)`, `L<=min(O,C)`, `H>=L`; consecutive UTC timestamps separated by exactly 3600 seconds. Missing, duplicate, discontinuous, incomplete, zero/invalid price or bad OHLC bars abort the research replay; no interpolation, synthetic close, future-extrema or missing-price fallback.
- Each bar's values are available only at `E[t]=T[t]+3600 seconds`. `BUY[s]`/`SELL[e]` is decided at E[s]/E[e]; queued MARKET action is dispatched on row s+1/e+1 and receives **historical** observed close at economic time E[s+1]/E[e+1]. The pinned engine's row timestamp is candle-open, so do not mistake its raw fill timestamp for economic availability or a real exchange order at the earlier open. No same-bar decision/fill, partial higher timeframe, repainting, negative shift or future leakage.
- No decision at the last row can fill without an observed successor; an open position is marked to the last actual close for research reporting without fabricating a closing trade.

## Execution assumptions — pinned Hummingbot capability

- **Pinned repository:** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`; canonical package label **20260920**, literal `hummingbot/VERSION=dev-2.17.0` verified via connected GitHub app 2026-10-29. This Scout did not independently rehash a wheel/image; earlier independently reviewed engine/source evidence exists in Alpha PR #414 and representative bounded spot MARKET/POSITION_HOLD research examples in admitted Alpha records. This is an engineering capability citation, **not** a strategy-specific controller implementation or parity result.
- **Real inspected feed path:** `hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py` (blob `5d0c938af574aca5f8dcba5ba28121797eae4dd0`) reads Binance REST `/api/v3/klines` and maps the first exchange kline timestamp as the candle OPEN; `constants.py` (blob `6d505dff42b60b356931df13eeeecd1e28b426f9`) explicitly includes `1h`. The data's actual observed OHLCV is the only model input.
- **Real inspected engine path:** `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` (blob `7d1e552dd7ee62df4f83f10950b8d593cd1106e6`) loops rows through `update_state(row)`, then `controller.determine_executor_actions()`, and routes `CreateExecutorAction` to `simulate_executor` on the supplied row slice. A future **minimal candidate-specific** controller must store the prior completed-bar signal and only emit its action on the next row. There is no implemented controller or executable strategy artifact in this PR.
- **Order path and fills:** `OrderExecutorConfig` in `hummingbot/strategy_v2/executors/order_executor/data_types.py` supports `ExecutionStrategy.MARKET`, `connector_name="binance"`, `trading_pair="BTC-USDT"`, `side=BUY/SELL`, `amount=Decimal("0.001")`, `position_action=OPEN/CLOSE`, `price=None`, `leverage=1`. `order_executor_simulator.py` (blob `3b4e82e91896db9074295ca2a8a087dde2499eab`) MARKET uses the **first supplied row's real close** as fill price, full quote amount `float(Q)*close`, `cum_fees_quote=trade_cost*amount_quote`, and terminates as `CloseType.POSITION_HOLD`. It does not prove live close-price acceptance, partial fills, real slippage, real fees or exchange precision. The source's `get_price_by_type` missing-price `Decimal("1")` fallback (backtesting_data_provider blob `e3d3e087b4da7c0381fac9621d1a04dcb8de81cf`) is forbidden; require a verified real positive close before order creation.
- **Research accounting:** initial `cash=Decimal("10000") USDT`, `inventory=Decimal("0") BTC`; fixed `Q=Decimal("0.001") BTC`, `f=Decimal("0.001")` per side, **hypothetical** quote-notional taker-like cost, `trade_cost=0.001` in simulator. Confirmed full BUY: `cash-=Q*P_buy*(1+f)`, `inventory+=Q`; confirmed full SELL: `cash+=Q*P_sell*(1-f)`, `inventory-=Q`; gross `Q*(P_sell-P_buy)`, fees `f*Q*(P_buy+P_sell)`, net=gross-fees. One position and one pending action max; no compounding, simultaneous orders, reentry on fill bar, cooldown or DCA. If insufficient cash, failed/partial/ambiguous/duplicate fill, missing price, mismatched position, or nonexistent successor, **fail closed**, never invent a fill. Confirm actual terminated executor fill evidence and reconcile against an independent Decimal cash/inventory ledger rather than native gross-only PnL or exact-zero dust state; abort if base deviation >1e-12 BTC or quote/fee deviation >1e-8 USDT. Native `POSITION_HOLD` and netting are bounded backtest constructs, not proof of live inventory accounting.
- **Economic boundaries:** Binance Spot unlevered, so perpetual funding and liquidation are **not applicable**, not a fabricated zero-funding observation. Extra slippage is modeled as zero **only as a disclosed idealized historical assumption**, not real zero spread/slippage. No real Binance fee tier, lot/tick/min-notional validation, maker, limit, next-open, intrabar, multi-asset, margin or Paper/Testnet/Live capability is claimed. Dedicated strategy-specific controller and Qlib event-level parity remain unimplemented and must be validated before large-scale screening of any new execution path.

## Evidence and six-gate assessment (Scout proposal only)

1. **G1 deterministic:** pinned Supertrend bands/state/seed, Wilder ATR14/RSI14, SMA20(volume), body polarity/size, all strict thresholds and warmup; no unknown parameters in the derivative.
2. **G2 direction:** Binance BTC-USDT spot LONG/FLAT only; sell means close long, no shorts.
3. **G3 entry/exit/risk:** full four-way BUY/SELL conditions, deliberately no protective stop/TP/trailing/time exit; the exposure risk is disclosed.
4. **G4 position:** 10k USDT initial cash, one 0.001 BTC position, full-fill-only pending states, no DCA/pyramiding/concurrency/cooldown/partial, re-entry only on a later eligible completed bar.
5. **G5 pinned-engine:** exact package/version/commit and directly inspected Binance 1h data parser, controller action loop, MARKET first-row-real-close fill, POSITION_HOLD, cost and independent inventory ledger; no false real fill/fee/funding or `Decimal("1")` missing-price assumptions. Strategy controller not implemented; bounded historical engine capability only.
6. **G6 causality:** 200 full candles, bar-open timestamps vs end-of-bar data availability explicitly separated, signal t to observed t+1 completed-close fill, no future inputs or fabricated final fill.

**Dedup at main `14086580a973c92742ae3a400751cf6e00120652`:** complete Git tree contains 431 root strategy Markdown records and README static count 431. Sixteen distributed strategy frontmatter samples read as PASS; **not** a 431/431 full frontmatter audit. Connected GitHub main code search for `U98FoYXv` and `sidimarvinicius`, and all-state PR search for both identities returned no match; current open research PRs have different sources. Nearest Supertrend families use state/proximity, RSI50 recross, StochRSI, or adaptive/CHOP/ADX gates, not this author's **Supertrend + 1.2×volume + ATR-relative directional candle + RSI70/30 four-way conjunction and full opposite exit**. No same source or materially identical rules found.

**No independent reproduction:** No original Pine byte/version hash, source-native trade equivalence, Hummingbot/Qlib strategy-specific backtest, event-level parity, profitability, Survivor, OOS, HB Certified or exchange trade is claimed. `hb_ready_status: PASS` is this Scout's **review proposal**, not independent Hermes Auditor approval. The independent Hermes Auditor GitHub Webhook Review alone may source-fact-remediate and exact-head PASS merge, or NOT_LOSSLESS close. Only the existing signed webhook receiver reconciles README count after accepted merge.
