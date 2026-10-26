---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Uptrick Volume Weighted Bands VWMA20 EMA20 hybrid EMA4 ATR14 band-cross long-flat BTC-USDT 1d independent derivative
created: 2026-10-27
updated: 2026-10-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-10-31
sources:
  - https://www.tradingview.com/script/N5H4qGLa-Uptrick-Volume-Weighted-Bands/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Uptrick Volume Weighted Bands — independently specified VWMA/EMA/ATR breakout long-flat

## Provenance

**First-party TradingView public indicator:** Uptrick, *Uptrick: Volume Weighted Bands*, public script ID **N5H4qGLa**, published **2025-10-31**, https://www.tradingview.com/script/N5H4qGLa-Uptrick-Volume-Weighted-Bands/ . Its first-party English description was read directly on **2026-10-27**. The accessible page labels the script **open-source** and explains the calculation and buy/sell triggers. The full Pine source bytes, original input defaults, exact Pine version, source revision hash and original executable order semantics were **not** obtained. Publication date and stable ID, not a claimed Pine hash, identify this source snapshot.

**Verified source-described facts only:** calculate a VWMA and EMA of price over a configurable lookback, average those two lines, smooth the hybrid with a further EMA, then construct upper/lower bands by adding/subtracting an ATR multiple. The primary Buy/Sell labels occur when **close crosses above upper** / **close crosses below lower**. The author also describes *optional* z-score/RSI take-profit and pullback buy-back modules, visual modes, and discretionary stop/partial-profit guidance. These are not verified to be executed orders. The source discusses long-to-short reversals; it is an indicator, not a verified Pine strategy backtest. No source-reported performance is adopted.

**Independently designed executable derivative, NOT lossless/source-native Pine:** The following are researcher-defined choices, not attributed to Uptrick: Binance BTC-USDT spot UTC 1d; close and Binance base volume; VWMA20 and EMA20, blended 50/50, EMA4 smoothing, Wilder ATR14 and 1.5× symmetrical bands; precise SMA seeds, strict cross equality, 100-bar warmup, contiguous-feed rejection; Long/Flat only (short disabled); next-row close-fill after prior-completed-row signal; 0.001 BTC per full trade, 10,000 USDT initial cash, hypothetical 0.1% per-side fee, zero additional simulated slippage, one position, full-fill pending states; all stop/TP/trailing/partial/buy-back/time/DCA legs disabled. Changing any of these creates a different derivative. The author's suggested lower-band stop and optional partial TP are **not** silently represented as source-native executed orders.

**Frozen identity:** TV:N5H4qGLa:Uptrick:2025-10-31 | independent-v1:2026-10-27 | VWMA20(close,volume)+EMA20(close) 50/50 -> EMA4; WilderATR14×1.5; strict close upper-cross long / lower-cross flat | BinanceSpot BTC-USDT UTC1d | signal-completed-s, MARKET-close-fill-s+1 | Q0.001 BTC | fee0.001/side | no adds.

**Dedup 2026-10-27:** GitHub app current main SHA 732443e98b6e6be3368930c7c9407de8d9c2509e, 366 root strategy records and README 366. Main code search for N5H4qGLa and Uptrick found no match; ten open PRs, including their research/* heads and source URLs, were checked, with no same-source candidate. The closest main Garman-Klass adaptive VWMA breakout uses a VWMA plus price standard deviation dynamically scaled by Garman-Klass OHLC volatility, **not** this VWMA+EMA hybrid, extra EMA smoothing and Wilder ATR bands; EHMA fixed-percentage bands and EMA8/50 percentage hysteresis likewise have materially different signal construction. This is not a mere parameter variant of those families. Count equality alone is not a full independent audit of all pre-existing frontmatter.

## Economic mechanism

### Source-reported

The author's described hybrid volume-sensitive/price-sensitive centerline aims to balance VWMA participation with EMA responsiveness, while ATR-based bands adapt breakout thresholds to volatility. An upper close-cross is a bullish signal, a lower close-cross a bearish signal. Optional take-profit/buy-back markers are not binding order rules in this derived strategy. No independently reproduced source returns or trade statistics are claimed.

### Research interpretation

A long-flat **fresh-cross trend breakout**: a price close must escape a hybrid VWMA/EMA center by 1.5 current ATR to enter; the opposite lower-band escape closes the position. This differs from a level-retested state strategy and from a standard Bollinger/VWMA channel. Volatility expansion may delay entry/exit and whipsaws remain possible. There is no profit guarantee.

## Signal

**Data contract:** one Binance BTC-USDT spot 1d UTC stream, each candle indexed t=0,1,... by strictly consecutive opening timestamps T[t] separated by exactly 86,400 seconds. Require finite O,H,L,C >0; H>=max(O,C), L<=min(O,C), H>=L, and finite base-volume V>=0. Require complete closed bars only; reject duplicates, gaps, NaNs, non-finite calculations, impossible OHLC and missing actual closes rather than interpolate or substitute prices. Validate the entire requested range before the backtester can silently drop rows. Reject any rolling VWMA window with sum(volume)=0.

**Researcher-pinned indicator mathematics (IEEE-754 binary64 arithmetic; not asserted to match unavailable Pine initialization):**
1. VWMA20[t] = sum(C[i]×V[i], i=t-19..t) / sum(V[i], i=t-19..t), first defined t=19.
2. EMA20[19] = arithmetic mean(C[0..19]); for t>=20, EMA20[t] = (2/21)×C[t] + (19/21)×EMA20[t-1].
3. Hybrid B[t] = (VWMA20[t]+EMA20[t])/2, defined t>=19.
4. EMA4(B)[22] = arithmetic mean(B[19..22]); for t>=23, M[t]=(2/5)×B[t]+(3/5)×M[t-1], with M[22] the seed.
5. TR[0]=H[0]-L[0]; TR[t]=max(H[t]-L[t],abs(H[t]-C[t-1]),abs(L[t]-C[t-1])) for t>=1. ATR14[13]=mean(TR[0..13]); ATR14[t]=(13×ATR14[t-1]+TR[t])/14 for t>=14.
6. U[t]=M[t]+1.5×ATR14[t]; D[t]=M[t]-1.5×ATR14[t]. U>=D whenever ATR is nonnegative. There is no other volatility/volume/RSI/z-score filter.

**Strict event predicates on fully completed bar s:**
- BUY[s] iff C[s-1] <= U[s-1] AND C[s] > U[s].
- SELL[s] iff C[s-1] >= D[s-1] AND C[s] < D[s].
- Equality at the *current* threshold is not a cross; previous equality followed by strict escape is. Persistently above/below a band is not a repeated trigger. A price between the rails generates no action.
- No repainting, higher/lower-timeframe series, future pivots, ML training, optional indicators or discretionary inputs.

**Warmup:** the first 100 consecutive valid fully completed bars t=0..99 are for initialization only. First eligible completed signal bar is s=99, with action/fill no earlier than t=100. Earlier events are discarded, never replayed. A missing prehistory or indicator seed is a hard data failure.

**Direction and state machine:** BTC-USDT Binance spot LONG/FLAT; initial FLAT, cash 10,000 USDT, base 0. The states are FLAT, BUY_PENDING, LONG, SELL_PENDING. At the close of s, record the signal; at the *next* valid row t=s+1, a strategy-specific controller may submit exactly one MARKET action based only on completed information <=s. If FLAT and BUY[s], BUY 0.001 BTC. If LONG and SELL[s], SELL the full confirmed 0.001 BTC. A BUY signal while LONG or SELL while FLAT is a no-op. Pending states suppress additional orders. The first-row MARKET simulator full-fill must be confirmed in the following update before the ledger changes state; do not equate a CreateExecutorAction with inventory. If any fill fails, is partial, missing, nonpositive, over-sized, or would cause negative cash, **abort** this research replay without fictitious fills or hidden retries. No re-entry on the exit row; only a fresh subsequent BUY cross while FLAT, with zero additional cooldown. The opposite signal takes priority over entry if an unexpected conflict occurs, otherwise abort as an invalid signal invariant.

**Explicitly disabled:** short/borrow/futures/perpetuals, leverage >1, multi-pair exposure, pyramiding, concurrent orders/positions, BO/SO/DCA, safety orders, partial closes, compounding, protective/intrabar stops, stop-limit, take-profit, trailing, time exit, optional z-score/RSI profit markers, buy-back module, extra filters, maker/limit orders, next-open fill, discretionary overrides, end-of-sample forced liquidation. If still LONG at the final valid close, retain inventory and mark it at that **observed** close; do not fabricate a closing SELL.

## Required data

Only actual Binance BTC-USDT spot UTC 1d OHLCV (base volume) and the above deterministic indicators. No order book, funding rate, settlement mark/index price, cross-asset shared cash, external volume source, non-OHLCV input or future candle. Trading decisions use historical completed closes and base volumes, not tick/intrabar data.

## Execution assumptions

**Pinned Hummingbot capability evidence (directly inspected through GitHub connector 2026-10-27):** HCH725/hummingbot at commit **8b0e067e80ab62f10846d518dcb5a8218527ddb3**, package label **20260920**, repository VERSION **dev-2.17.0**. The connected GitHub app read the pinned BinanceSpotCandles REST parser and constants, BacktestingEngineBase, BacktestingDataProvider, OrderExecutorSimulator and OrderExecutorConfig. Prior independently audited Alpha PR #414 documents representative source/package and MARKET/POSITION_HOLD capability; this Scout did **not** rehash an installed wheel/image or create a candidate controller.

- **Data:** BinanceSpotCandles uses /api/v3/klines and supports interval 1d; row[0] is **open timestamp**, row[1..5] observed O,H,L,C,V. The model's BacktestingDataProvider loads candles, and BacktestingEngineBase.prepare_market_data uses backward merge_asof and dropna; a prospective implementation MUST prevalidate contiguous complete candles and warmup rather than allow dropped/misaligned rows.
- **Controller/executor:** a future strategy-specific DirectionalTradingController can submit CreateExecutorAction with OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),position_action=OPEN/CLOSE,execution_strategy=MARKET,price=None,leverage=1). The pinned BacktestingEngineBase performs update_state(row) then determine_executor_actions(), dispatching OrderExecutorConfig to OrderExecutorSimulator. This is a verified reusable engine path, **not** a pre-existing implementation of this candidate.
- **Fill semantics:** pinned OrderExecutorSimulator MARKET uses the first supplied row and its **actual close** as the full-fill price; filled_amount_quote=0.001×actual close, cum_fees_quote=trade_cost×filled_amount_quote, close_type=POSITION_HOLD. It does not establish real exchange post-close execution, slippage, partial-fill handling, fee tier, lot/tick precision or liquidity. The chosen idealized historical fill is intentionally a derivative of the indicator signal, not a source-native Pine fill assertion.
- **Position and fees:** pinned BacktestPositionHold nets confirmed BUY/SELL base inventory and computes gross matched realized quote PnL; cum_fees_quote is separate. Keep a persistent fill-confirmed cash/position ledger; set terminated_executors_window=None to avoid the default one-hour history view dropping daily fills. Start cash 10,000 USDT. At BUY fill Pb, debit 0.001×Pb×(1+0.001); at SELL Ps, credit 0.001×Ps×(1-0.001). Matched net quote PnL = 0.001×(Ps-Pb) - 0.001×0.001×(Pb+Ps); mark open inventory using actual last C. trade_cost=0.001 per side is a **research hypothesis**, not verified Binance fee. Simulator adds no modeled slippage; do not assert zero actual slippage. Spot funding is **not applicable**, not a synthetic zero perpetual-funding series.
- **Missing-price guard:** BacktestingDataProvider.get_price_by_type can fall back to Decimal("1") for a missing price. This derivative explicitly rejects that fallback; require an actual validated close before an action or ledger event.
- **Effective time and causality:** Binance T[t] is candle **open**. Signal on completed s is available only at T[s]+86400 = T[s+1]. Submit action at row t=s+1 using **only <=s**. The simulator fills at actual C[t], which is not known until T[t]+86400. Record modeled fill/equity economic time as **T[t]+86400**, never claim T[t] already knew C[t]. The engine's open-timestamp row label is a simulation index, not evidence of intrabar knowledge or actual tradability at that close. Never use C[t] for a decision made before the row completes. Require a one-full-bar decision-to-fill lag and strict input-prefix invariance.
- **Scope boundary:** proven engine primitives are historical spot 1d candle ingestion, one full MARKET close-fill per action, POSITION_HOLD netting and explicit fee bookkeeping. This is a **bounded expressibility proposal**, not a controller implementation, Qlib parity, backtest, realistic exchange economics, or trading authorization. A new unverified execution primitive requires one representative capability check before mass Qlib screening.

## Evidence

### Source-reported

The 2025-10-31 Uptrick TradingView page explicitly describes VWMA/EMA average, additional EMA smoothing, ATR-multiple bands, close crossing upper/lower bands for primary signals, and optional profit/buy-back modules. It does not establish an independently verified executable Pine strategy, original input defaults, fill timing, fees or results.

### Independently reproduced

No strategy trade replay, Qlib/Hummingbot backtest, performance, Pine signal parity or installed package hash was independently reproduced this cycle. Pinned source files were inspected via GitHub connector, and prior independently reviewed #414 is referenced only for reusable MARKET/hold capability, not candidate certification.

### Six-gate submission, for independent Auditor decision

1. **Determinism:** complete binary64 VWMA20, SMA-seeded EMA20 and EMA4, Wilder ATR14, 1.5× bands, strict crosses, priority, fixed warmup and data validity.
2. **Direction:** spot BTC-USDT LONG/FLAT; short/futures explicitly disabled.
3. **Entry/exit/risk:** fresh upper cross entry, fresh lower cross exit, one-row delayed close-fill, all other risk legs explicitly disabled; no hidden Pine orders.
4. **Position:** full 0.001 BTC, 10k cash, no DCA/concurrency/pyramiding, pending/full-fill confirmations, no retry on failure, zero cooldown but fresh-cross-only re-entry.
5. **Pinned model:** actual Binance spot 1d REST data, pinned controller/action/MARKET/POSITION_HOLD code, full-fill and fee/position ledger, missing-price guards and no false funding/real-fill claims.
6. **Causality:** 100 closed-bar warmup, s→s+1 signal/action/fill separation, close-effective economic clock, contiguous data and no future-dependent indicator state.

**HB_READY PASS is a Scout proposal pending independent review.** It is not a profitability or Qlib parity claim and does not certify source-native Pine equivalence.

## Falsification plan

Independently verify the source's upper/lower crossing description and all researcher changes, inspect pinned simulator timestamp and fee semantics, test warmup seeds, strict crossing/equality, consecutive-bar gap abort, no duplicate entries, full-fill confirmation, source-indicator vs derivative signal differences, and fee-inclusive cash. Before any mass Qlib screening on a new execution path, demonstrate representative event-level Qlib/Hummingbot parity. No such test or trading is performed in this Scout.

## Crypto portability

The BTC-USDT 1d spot choice is a bounded research implementation target, **not** an HB_READY admission whitelist or the author's chart requirement. Other assets, timeframes, leverage, futures, DCA or new execution paths require separate explicit semantics and evidence.

## Limitations

Inaccessible full Pine, unknown source defaults/version, independent numeric seeds and fills, disabled source-advised risk modules, unbounded loss until lower-band exit, idealized close-fill, unknown real slippage/fees/precision, no implemented controller, no profitability/OOS/Survivor/HB Certified/Qlib parity or live authorization.

## Implementation status

**not-implemented** — no dedicated executable strategy/controller, Qlib recipe, deployed artifact or backtest. This is not a second HB_READY admission gate.

## Adoption boundary

**research-only; adoption: not-approved; approval_scope: research-only.** Independent Hermes Auditor GitHub Webhook Review owns source-fact remediation, exact-head PASS merge or NOT_LOSSLESS close. Scout must not approve/merge/close, modify main/README, trade or deploy; the existing signed webhook receiver alone owns post-merge README count synchronization.

## Related Wiki records

None claimed; no private Wiki data read.

## Sources

1. Uptrick, *Uptrick: Volume Weighted Bands*, TradingView open-source indicator, published 2025-10-31, stable ID N5H4qGLa: https://www.tradingview.com/script/N5H4qGLa-Uptrick-Volume-Weighted-Bands/
2. Pinned Hummingbot source commit: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
3. Prior independent engine primitive audit: https://github.com/HCH725/alpha-strategy-research/pull/414
