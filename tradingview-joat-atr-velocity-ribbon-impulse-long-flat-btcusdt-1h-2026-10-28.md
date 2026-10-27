---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: CryptoFlux ATR velocity-onset EMA-ribbon volume-impulse long-flat BTCUSDT 1h (independent derivative)
created: 2026-10-28
updated: 2026-10-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-12-26
sources:
  - https://www.tradingview.com/script/ir84k566-CryptoFlux-Dynamo-JOAT/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# CryptoFlux ATR velocity-onset EMA-ribbon volume-impulse long-flat BTCUSDT 1h

## Provenance

- **TradingView first-party publication:** officialjackofalltrades, *CryptoFlux Dynamo [JOAT]*, open-source Pine Script v6, published **2025-12-26**, public script ID **ir84k566**: https://www.tradingview.com/script/ir84k566-CryptoFlux-Dynamo-JOAT/ . Description directly inspected 2026-10-28; TradingView does not expose an immutable source revision in the publicly indexed page.
- **Identity:** `JOAT-ir84k566-ATR21-EMA13-velocity-onset-EMA8-21-34-volume34-cycle55-BTCUSDT-1h-long-flat-derivative-v1`. This is an **independent researcher-designed derivative**, NOT the source-native CryptoFlux strategy, NOT an event-equivalent port, and NOT a reproduction of the source's published results.
- **Source-native facts actually published:** ATR21 smoothed by EMA13 divided by price; compression below 0.8%, expansion 0.8–1.6%, velocity above 1.6%; EMA ribbon 8/21/34; volume impulse `volume > SMA34(volume)*1.15 OR volume_z > 0.5`; EMA55 cycle deviation greater than +0.15% for bullish alignment. Source also combines MACD 8/21/5, RSI21/MFI21, BB/KC squeeze, four weighted pathways, score >=55, futures short, regime stops/targets, trailing, drawdown kill switch, intrabar calculations and BTC.D optional filter. Those omitted source components are **NOT** silently represented as present here.
- **Researcher-designed changes, fully declared:** (1) select the source's ATR velocity regime **onset edge** as a stand-alone trigger instead of its four-path composite; (2) require the source's bullish EMA ribbon, volume impulse and cycle conditions concurrently; (3) long/flat spot BTCUSDT on completed 1h candles instead of the source's 5m perpetual long/short; (4) exit when velocity regime ends, EMA8<=EMA21 or cycle support fails, instead of source-native ATR brackets/trailing/fail-safe; (5) fixed 0.001 BTC, 10,000 USDT cash, no pyramiding/DCA, and idealized next-completed-bar-close fills instead of source intrabar risk sizing; (6) fully specified causal indicator seeds, 120-bar warmup, and separate Decimal research ledger. These changes **alter trade events**. No source-native equivalence or profitability is claimed.

## Economic mechanism

### Source-reported

The author describes adapting signal strength and risk to ATR-normalized volatility, with EMA ribbon direction, volume participation and cycle alignment as confirmations. The published source's complete composite, futures sizing, trailing and risk controls are not used in this derivative.

### Research interpretation

A volatility-expansion **transition** can identify the start of a high-velocity phase; buying only its first completed-bar appearance when bullish ribbon, volume impulse and EMA55 cycle alignment coincide attempts to filter directionless volatility spikes. Exiting when the phase or confirmation disappears prevents indefinite holding. Failure modes: a transient one-bar volatility spike, whipsaw exits, missing a velocity move that began without confirmation, and large unprotected price gaps. No profitability claim.

## Signal

All calculations use one continuous, chronologically ordered series of Binance spot BTCUSDT **completed 1h OHLCV candles**, zero-based bar index `t`. Deterministic IEEE float64 indicators; no fitted coefficients, stochastic optimization or repainting.

- `TR[0]=high[0]-low[0]`; for `t>0`, `TR[t]=max(high[t]-low[t], abs(high[t]-close[t-1]), abs(low[t]-close[t-1]))`.
- `ATR21[20]=mean(TR[0..20])`; thereafter `ATR21[t]=(20*ATR21[t-1]+TR[t])/21` (Wilder RMA). No ATR values before index 20.
- `SATR13[32]=mean(ATR21[20..32])`; thereafter `SATR13[t]=(2/14)*ATR21[t]+(12/14)*SATR13[t-1]`. `atr_pct[t]=100*SATR13[t]/close[t]`.
- Regime: `COMPRESSION` if `atr_pct<0.8`; `EXPANSION` if `0.8<=atr_pct<=1.6`; `VELOCITY` if `atr_pct>1.6`. Boundaries are explicit; missing/nonpositive close invalidates the research segment.
- For `n in {8,21,34,55}`, `EMA_n[n-1]=SMA(close[0..n-1])`; subsequent `EMA_n[t]=(2/(n+1))*close[t]+(1-2/(n+1))*EMA_n[t-1]`.
- `vmean34[t]=SMA(volume[t-33..t])`; `vstd34[t]=sqrt(sum((volume[i]-vmean34[t])^2 for i=t-33..t)/34)` (population SD). `vz34=(volume-vmean34)/vstd34` if `vstd34>0`, otherwise `vz34=0`. `impulse=(volume>1.15*vmean34) OR (vz34>0.5)`.
- `ribbon=(EMA8>EMA21) AND (EMA21>EMA34)`. `cycle=(close>1.0015*EMA55)`. Exact equality fails these strict tests.
- `onset[t]=(regime[t]==VELOCITY) AND (regime[t-1]!=VELOCITY)`; all required series must be valid on both bars.
- **BUY signal:** `onset AND ribbon AND impulse AND cycle`, only when FLAT and no pending order.
- **SELL signal:** `regime!=VELOCITY OR EMA8<=EMA21 OR NOT cycle`, only when LONG and no pending order.
- No same-bar BUY/SELL conflict: BUY implies VELOCITY, EMA8>EMA21 and cycle=true, making SELL false. No entry on later VELOCITY bars without a new non-velocity-to-velocity edge.
- The source's MACD/RSI/MFI/BB/KC, four-path weighted score, short side, dominance feed, session, drawdown kill switch, intrabar stop/target/trailing, futures leverage, equity-risk sizing and tick recalculation are all **intentionally disabled in this independent derivative**. No hidden stop, TP, time stop or trailing default. The only exit is the explicit SELL signal. No fixed protective stop is claimed.

## Required data

Single Binance BTCUSDT spot `1h` actual OHLCV feed (open only for validity, high/low/previous close for ATR, close for EMA/threshold, volume for impulse), no higher/lower timeframe, order book, OI, funding, mark price, BTC.D or external model. Validate chronological hourly continuity, positive finite prices, high>=max(open,close), low<=min(open,close), high>=low, and finite nonnegative volume **before** any feature dropna; missing, duplicated, zero/nonpositive-price or discontinuous bars **abort** rather than fabricate values.

Warmup: indices `0..119` (120 fully completed bars) remain FLAT with no signals/orders. First eligible decision index 120, which has all EMA55/ATR21-EMA13/volume34 and prior-regime data. No negative shifts, future extrema, forward-fill from missing prices or in-progress candle as complete.

## Execution assumptions

**Pinned benchmark read directly via GitHub connector 2026-10-28:** HCH725/hummingbot commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3`, package label `20260920`, `hummingbot/VERSION=dev-2.17.0`. Paths inspected: `hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py`, `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py`, `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py`, `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`. Prior independently audited bounded MARKET/POSITION_HOLD primitive evidence: Alpha PRs #519 and #529. This is **not** a candidate-specific backtest or proof of an already implemented controller.

- **Feed/time:** BinanceSpotCandles reads real REST kline OHLCV, `timestamp` is candle **open** in seconds; complete bar `t` becomes known only at `E[t]=T[t]+3600s`. `1h` is a supported feed interval. Validate completeness and exact hourly continuity; never interpret `T[t]` as signal availability time.
- **Controller/action:** BacktestingEngineBase iterates rows, `update_state(row)` then `controller.determine_executor_actions()`, and simulates `CreateExecutorAction(OrderExecutorConfig)`. A future minimal dedicated controller (not yet implemented) holds this record's FLAT/LONG/PENDING state and the previously completed signal. On completed bar `t` it **queues** BUY/SELL for `t+1` without placing an action on `t`. At `t+1` it dispatches one `OrderExecutorConfig(connector_name="binance", trading_pair="BTC-USDT", side=BUY/SELL, amount=Decimal("0.001"), position_action=OPEN/CLOSE, execution_strategy=MARKET, price=None, leverage=1)`; no signal is evaluated on the fill bar. On the final available bar, pending actions with no `t+1` remain unfilled and are excluded; never invent a future close.
- **Actual pinned fill semantics:** OrderExecutorSimulator MARKET uses the **first supplied row's real close** as entry_price, `float(config.amount)*entry_price` as filled quote and `trade_cost*amount_quote` as cumulative fee, returning `CloseType.POSITION_HOLD`. Dispatch at `t+1` gives idealized `E[t+1]` close fills, not source-native next-open, intrabar bracket or achievable live post-close order. No price defaulting: BacktestingDataProvider's `Decimal("1")` fallback for missing price is explicitly prohibited; abort if real close absent/nonpositive.
- **Position/state:** Start 10,000 USDT cash, 0 BTC; only one LONG unit `Q=Decimal("0.001")` or FLAT; at most one pending action; no DCA, pyramiding, overlapping position, short, margin, leverage, shared capital, re-entry cooldown or compounding. A confirmed BUY changes FLAT to LONG, confirmed SELL closes exactly Q and changes LONG to FLAT. If insufficient cash, unexpected partial/failed fill, stale executor, contradictory side or unexpected position size: **abort segment**, never silently skip/assume fill. After an exit, a new non-velocity-to-velocity onset is required; no level-based repeated entry.
- **Costs/ledger:** Spot funding is not applicable; do **not** infer perpetual funding=0. Fixed **hypothetical** quote-notional taker-like research fee `f=Decimal("0.001")` (0.1% per side; NOT a verified exchange fee tier), `trade_cost=0.001`; idealized zero additional slippage is a declared model limitation, not observed liquidity. Independent Decimal research inventory/cash ledger per confirmed executor: BUY `cash-=Q*P*(1+f); btc+=Q`; SELL `cash+=Q*P*(1-f); btc-=Q`; net realized round trip `Q*(Ps-Pb)-f*Q*(Pb+Ps)`. Gross PnL and fee totals are kept separate.
- **Float/Decimal boundary:** BacktestPositionHold re-derives base from float-generated quote/price and uses `net_amount_base==0` to decide closure, which can leave tiny residual dust. Its `is_closed`/positions_held are **not** the derivative's authoritative state. Use configured exact Q and independently confirmed full-fill evidence as the Decimal inventory authority; compare engine-implied base to expected with absolute tolerance `1e-12 BTC`, and fee/quote with absolute tolerance `1e-8 USDT`; fail closed above tolerances. Tolerances are diagnostic research boundaries, NOT live order rounding or an engine patch. Preserve full terminated-executor history (`terminated_executors_window=None` or equivalent). No unverified lot/tick/min-notional/exchange balance validation is claimed: this is pure historical research, not exchange-order acceptance.
- No Hummingbot position/triple-barrier executor, DCA executor, stop/limit/maker path, funding engine, liquidation or exchange real-fill semantics are invoked. Reuse only the previously bounded single-frame spot MARKET/POSITION_HOLD path. No claim that an unmaterialized controller already exists.

## Evidence

### Source-reported

TradingView public script description gives the exact ATR21/EMA13 normalization, 0.8/1.6 thresholds, EMA8/21/34 ribbon, volume SMA34 x1.15 OR z>0.5, EMA55 cycle +/-0.15% and the broader native composite/futures/risk architecture. It does **not** give this derivative's onset-only signal, spot 1h execution, close-fill, separate Decimal ledger or exit rule. No source backtest statistic is treated as reproduced.

### Independently reproduced

No Pine-event parity, Hummingbot strategy backtest, Qlib backtest, actual exchange fill, profit/OOS/Survivor/HB Certified or live results. Direct inspection of immutable pinned Hummingbot source and reuse of prior bounded primitive evidence (#519/#529) supports only the explicitly constrained historical execution lane.

### Six-gate evidence for independent auditor

1. **Determinism:** fully specified ATR/RMA/EMA seeds, regime equality, EMA ribbon, volume z-score, cycle, onset edge and strict inequalities; float64; no optimization/model.
2. **Direction:** long/flat Binance BTCUSDT spot; short and futures disabled.
3. **Entry/exit/risk:** onset+ribbon+impulse+cycle BUY; regime/ribbon/cycle failure SELL; no hidden stops/targets/trailing/time exit; source's other legs expressly disabled.
4. **Position:** exact Q/cash, one pending action, one position, no DCA/pyramiding/concurrency/cooldown, fail-closed ledger and fresh onset re-entry.
5. **Pinned model:** exact feed/controller/action/MARKET next-row actual-close/POSITION_HOLD fee and independent Decimal cash/inventory; bounded residual tolerance and explicitly unmodeled exchange acceptance; no unverified intrabar, perpetual or external feed.
6. **Causality:** 120 complete bars warmup; decision at E[t], action/fill at E[t+1], no future bar data or fake price; incomplete/missing data abort.

**Dedup 2026-10-28:** GitHub code search on current main for `ir84k566`, `CryptoFlux Dynamo` and `ATR regime volume impulse EMA ribbon` returned no same-source record; PR search for `ir84k566`/`CryptoFlux` returned none. All ten currently open `research/*` PRs were checked by title/body; none match this TradingView identity or this ATR velocity-onset+ribbon+volume+cycle mechanism. Existing ATR/EMA/volume families are not this 3-regime transition-edge construction; not a trivial parameter variant. Main baseline `a429cf5a78d7b8bac08d278c430a95c8a1f2c829`, 389 root strategy Markdown records, README count 389; 13 spaced frontmatter samples were PASS, not a full 389-file census.

## Falsification plan

Only under later authorization: implement minimal dedicated controller, test ATR/EMA seeds, threshold equality at 0.8/1.6, zero-volume z, missing-bar abort, pending fill/last-bar behavior, volume spike with bearish ribbon, signal/exit exclusivity, executor full-fill/Decimal dust, fee reconciliation and close timestamps. New execution capability requires representative HB↔Qlib event-level parity before mass Qlib screening; none is performed here.

## Crypto portability

This derivative is already specified for BTCUSDT spot 1h. The source's 5m perpetual shorts, funding, leverage, BTC dominance and original risk sizing are **not** ported. Applying to another pair, timeframe, derivatives market, intrabar execution or DCA is a separately declared and revalidated variant, not implicit permission.

## Limitations

Source Pine text itself is not independently recovered from the indexed TradingView page; only the author's detailed public first-party description is verified. Original strategy has substantially different event timing and risk logic. This record's causal formulas and all researcher-selected parameters are fully explicit, but no empirical returns, exchange acceptance, real fills, actual fee tier, real slippage, funding, margin, installed image digest or candidate-specific controller test is claimed. The independent auditor must reject/close if any pinned-path requirement cannot be verified.

## Implementation status

Research record only: `implementation_status: not-implemented`. No strategy controller, container, deployment, backtest, Paper/Testnet/Live or Qlib artifact was created.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. `hb_ready_status: PASS` is a **proposal** for the independent Hermes Auditor GitHub Webhook Review, not Scout self-approval. Auditor alone reviews exact PR head and merges PASS or closes NOT_LOSSLESS; existing signed webhook receiver alone updates README after confirmed merge.

## Related Wiki records

None asserted.

## Sources

- https://www.tradingview.com/script/ir84k566-CryptoFlux-Dynamo-JOAT/ — officialjackofalltrades, public open-source Pine v6 publication, 2025-12-26; description inspected 2026-10-28.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned engine source inspected through connected GitHub app.
- https://github.com/HCH725/alpha-strategy-research/pull/519 — prior bounded MARKET/POSITION_HOLD synthetic primitive evidence.
- https://github.com/HCH725/alpha-strategy-research/pull/529 — prior bounded pure-research execution primitive evidence.
