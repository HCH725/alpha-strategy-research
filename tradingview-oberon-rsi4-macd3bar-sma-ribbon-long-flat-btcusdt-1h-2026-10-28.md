---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Oberon RSI4/MACD three-bar confluence SMA-ribbon long-flat BTCUSDT 1h (independent derivative)"
created: 2026-10-28
updated: 2026-10-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-08-14
sources:
  - https://www.tradingview.com/script/DWzDv6Do-Scalper-SMA-RSI-MACD-Entry-Exit-Signals-v2/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Oberon RSI4/MACD three-bar confluence SMA-ribbon long-flat BTCUSDT 1h

## Provenance

- **Primary source:** Oberon777, *Scalper SMA-RSI-MACD – Entry/Exit Signals v2*, first-party TradingView public **open-source indicator** page, published **2025-08-14**, stable script ID **DWzDv6Do**; first-party public description inspected **2026-10-28**: https://www.tradingview.com/script/DWzDv6Do-Scalper-SMA-RSI-MACD-Entry-Exit-Signals-v2/
- **Immutable proposed research identity:** `TV:DWzDv6Do|Oberon777|2025-08-14|derived-v1-20261028|BTCUSDT-spot-1h|RSI4-30-recross+MACD12-26-9-bull-cross-within3|SMA5-8-13+EMA200|ATR14-entry1.5R-stop2R-target|tplus1-completed-close|Q0.001-fee0.001`. The identity is fixed by this record and PR head, NOT an immutable hash of TradingView's Pine revision (which is not available in the accessible public text).
- **Source-reported facts:** optional EMA200 plus SMA5/8/13 trend ribbon; RSI4 oversold/overbought pullback and MACD bullish/bearish momentum turn, both within a default three-bar lookback; ATR-multiple stop default 1.5, two possible targets 1R/2R, opposite-signal exit mode, optional session filter; source primarily describes a 1m–5m manual indicator. The first-party description does NOT establish exact original RSI thresholds, MACD lengths, RSI event operator, Pine order fill, or complete indicator code. No original trade events or returns are claimed.
- **Explicit independent derivative, NOT source-native or lossless:** research fixes RSI4 30 upward recross, MACD(12,26,9) line/signal bullish cross, three-completed-bar event conjunction, SMA5>SMA8>SMA13 and close>EMA200, 1h spot long/flat, 2R target, completed-close *signals* for SL/TP/trend failure, next completed-bar close simulated MARKET fills, fixed quantity/cash/fees, and its own ledger. Original manual indicator alerts, shorts, 1m–5m recommendation, intrabar protective SL/TP, optional TP1 partial exit, session restriction, and unspecified original signal logic are NOT silently ported. Every changed decision rule is specified below; source-native event equivalence is explicitly disclaimed.

## Economic mechanism

### Source-reported

The author combines a short RSI pullback, a nearby MACD momentum turn, a trend ribbon and ATR risk distances to identify potential trend-continuation entries. The original is an indicator for manual decisions, not a verified exchange execution strategy.

### Research interpretation

This derivative buys only the **fresh temporal conjunction** of RSI recovery and MACD bullish cross while a short SMA ribbon and EMA200 support the uptrend. A completed-close ATR-distance loss/target or ribbon break triggers a later historical close-fill exit. It may miss moves, enter after the reversal, or experience gaps far beyond its signal-level stop; no protective order or profitability is implied.

## Signal

Single ordered series of Binance **BTCUSDT spot 1h completed** OHLCV, zero-based index `t`. Indicators computed in deterministic float64 arithmetic with explicitly seeded recurrences, no ML, fit or full-sample optimization.

1. `SMA_n(x)[t]=sum(x[t-n+1..t])/n` for `t>=n-1`, otherwise undefined. Compute `SMA5, SMA8, SMA13` on close.
2. `EMA_n(x)[n-1]=SMA_n(x)[n-1]`, then `EMA_n[t]=alpha*x[t]+(1-alpha)*EMA_n[t-1]` for `alpha=2/(n+1)`; undefined before seed. Compute close EMA12, EMA26, EMA200. `MACD[t]=EMA12[t]-EMA26[t]` first valid at `t=25`. Signal `SIG9[33]=mean(MACD[25..33])`; thereafter EMA9 recurrence on MACD. `MACD_BULL[t]=(MACD[t-1]<=SIG9[t-1]) AND (MACD[t]>SIG9[t])`, first eligible at `t>=34`.
3. RSI4: `delta[t]=close[t]-close[t-1]` for `t>=1`; gains `max(delta,0)`, losses `max(-delta,0)`. Seed average gains/losses at `t=4` using deltas 1..4, then Wilder recurrence `avg[t]=(3*avg[t-1]+new[t])/4`. RSI=100-100/(1+avg_gain/avg_loss), except both zero=>50, zero loss and positive gain=>100, zero gain and positive loss=>0. `RSI_RECOVER[t]=(RSI[t-1]<=30) AND (RSI[t]>30)`, first eligible `t>=5`.
4. `RSI_RECENT[t]=any(RSI_RECOVER[k] for k in [t-2,t])` and `MACD_RECENT[t]=any(MACD_BULL[k] for k in [t-2,t])`, treating undefined pre-valid events as false. `CONFLUENCE[t]=RSI_RECENT[t] AND MACD_RECENT[t]`; `FRESH[t]=CONFLUENCE[t] AND NOT CONFLUENCE[t-1]`. A persistent conjunction is NOT repeated as a fresh entry.
5. `TREND[t]=(SMA5[t]>SMA8[t]>SMA13[t]) AND (close[t]>EMA200[t])`; equality fails. No higher timeframe or session filter.
6. `TR[0]=high[0]-low[0]`; for `t>0`, `TR[t]=max(high[t]-low[t], abs(high[t]-close[t-1]), abs(low[t]-close[t-1]))`. `ATR14[13]=mean(TR[0..13])`, then Wilder `ATR14[t]=(13*ATR14[t-1]+TR[t])/14`. ATR frozen at BUY **signal** bar `s`, never recomputed for that trade.
7. **BUY signal** at completed bar `s>=220` iff `FRESH[s] AND TREND[s] AND ATR14[s]>0` and research state FLAT with no pending action. A BUY pending on `s` fills at actual completed bar `b=s+1` close `P_b` (only when that bar exists and full-fill evidence is valid); freeze `stop=P_b-1.5*ATR14[s]` and `target=P_b+3.0*ATR14[s]`. If `stop<=0` or prices/ATR invalid, abort rather than invent a stop. Risk `R=1.5*ATR14[s]`; target=2R.
8. **SELL signal** on completed bar `e>=b+1` iff LONG and no pending action and at least one of: `close[e]<=stop` (STOP), `close[e]>=target` (TARGET), or `close[e]<SMA13[e]` (RIBBON_FAIL). Label priority STOP > TARGET > RIBBON_FAIL, although positive R means STOP and TARGET cannot coincide. Signal is NOT an intrabar stop/limit order. SELL fills full Q at actual completed close `P_{e+1}` if that bar exists. A stop-level breach can fill much worse at the later close; do not cap the loss at R.
9. All other exits (intrabar bracket, protective stop, TP1 partial exit, trailing, opposite short signal, time/session/end-of-data forced close, liquidation, drawdown kill switch) are **disabled**. No silent executor defaults.

## Required data

Only actual Binance spot BTCUSDT 1h open/high/low/close/volume. Before any feature merge/dropna, require strictly increasing hourly open timestamps spaced 3600 seconds, finite positive O/H/L/C, `high>=max(open,close)`, `low<=min(open,close)`, `high>=low`, finite nonnegative volume; missing, duplicate, discontinuous or incomplete bars fail closed. No synthetic candles, zero-price fallback, future fills, external feeds or funding data.

Warmup bars `t=0..219` (220 complete candles) remain FLAT without orders; first decision `t=220` ensures EMA200, MACD signal, ATR and the prior confluence exist. All signals use current and earlier **completed** bars; no repainting, negative shifts or future extrema.

## Execution assumptions

**Pinned Hummingbot evidence, read with GitHub connector 2026-10-28:** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, package label `20260920`, `hummingbot/VERSION=dev-2.17.0`. Read `binance_spot_candles.py`, its `constants.py`, `backtesting_engine_base.py`, `backtesting_data_provider.py`, `order_executor_simulator.py`, `order_executor/data_types.py`, and `executor_simulator_base.py`. Prior independently reviewed bounded engine primitive exercise is in Alpha PR #519; #529/#530/#532/#533 independently audited this research-only MARKET/POSITION_HOLD lane. This record does not claim a dedicated controller already exists or a new wheel/image hash verification.

- **Feed and time:** BinanceSpotCandles REST `/api/v3/klines` parser maps first exchange timestamp to candle OPEN; `1h` exists in the pinned intervals. Bar `t` is available only at `E[t]=T[t]+3600 seconds`, not at its open timestamp.
- **Engine path:** `BacktestingEngineBase.simulate_execution` calls `update_state(row)` then `controller.determine_executor_actions()`, passing `processed_features.loc[i:max_ts]` to `simulate_executor`. A minimal future controller maintains the record's FLAT/LONG/PENDING and frozen ATR state; it queues a signal at completed `s` and emits one `CreateExecutorAction(OrderExecutorConfig)` **only on `s+1`**, never on the signal bar. Config: `connector_name="binance"`, `trading_pair="BTC-USDT"`, `side=BUY/SELL`, `amount=Decimal("0.001")`, `position_action=OPEN/CLOSE`, `execution_strategy=MARKET`, `price=None`, `leverage=1`. No entry/exit decisions on a fill bar.
- **Actual bounded fill:** pinned `OrderExecutorSimulator` MARKET fills at the first supplied row's **real close**, `amount_quote=float(Q)*close`, `cum_fees_quote=trade_cost*amount_quote`, `CloseType.POSITION_HOLD`. Dispatch on next row gives idealized next-completed-close fill, with economic time `E[s+1]`, not a guaranteed real post-close execution. `ExecutorSimulation` exposes fill timestamp/filled quote/terminated evidence. If missing/invalid real close, partial/duplicate/failed/stale/unmatched fill, insufficient cash or a nonexistent last-row successor: fail closed (last-row pending is unfilled and not invented). `BacktestingDataProvider.get_price_by_type` has a `Decimal("1")` missing-price fallback; it is explicitly forbidden for this model.
- **Research ledger:** start `cash=Decimal("10000") USDT`, `inventory=Decimal("0") BTC`, exact `Q=Decimal("0.001") BTC`, one position and at most one pending action. Full confirmed BUY: `cash-=Q*P*(1+f); inventory+=Q`; SELL: `cash+=Q*P*(1-f); inventory-=Q`; `f=Decimal("0.001")` per side is an explicit **hypothetical** quote-notional taker-like fee, NOT verified Binance tier. `trade_cost=0.001`. Gross PnL `Q*(Ps-Pb)`; fees `f*Q*(Pb+Ps)`; net = gross minus fees. No compounding, partial TP, DCA, safety orders, pyramiding, concurrent markets/positions, cooldown or same-bar round trip. Following a SELL fill, re-entry requires a later new FRESH event. Terminal LONG marked only to last actual close; no synthetic liquidation.
- **Precision/positions:** native MARKET uses float quote and `BacktestPositionHold` derives Decimal base from quote/price with exact-zero closure, potentially retaining microscopic dust; native `positions_held` also lags. Research state is **independent confirmed-fill Decimal cash/inventory**, not native exact-zero `is_closed` or gross-only summary. Compare engine-implied base to expected within `1e-12 BTC` and fee/quote within `1e-8 USDT` diagnostic tolerances; above limits abort. Keep complete terminated history (`terminated_executors_window=None` or equivalent). These are research-only precision checks, NOT exchange rounding/lot/tick/min-notional or live acceptance.
- **Scope:** Spot funding is not applicable (not assumed-zero unknown perpetual funding); no futures leverage/margin/liquidation, maker/limit/intrabar executor, slippage modeling beyond explicitly idealized zero additional slippage, real spread/liquidity, exchange minimums or actual fee tier. No unverified engine capability is inferred from an API or candle interval name alone.

## Evidence

### Source-reported

First-party TradingView description identifies Oberon777, publication 2025-08-14, RSI4 pullback, MACD momentum turn within three bars, SMA5/8/13 plus EMA200 optional trend filtering, ATR1.5 stop and 1R/2R target choices. It is a manual indicator; the exact Pine signal and original backtest behavior were not independently retrieved.

### Independently reproduced

No original Pine signal parity, candidate-specific Hummingbot/Qlib backtest, event-level Qlib parity, profitability, OOS, Survivor, HB Certified or exchange fill is claimed. Direct inspection of immutable pinned Hummingbot source plus existing independently audited bounded MARKET/POSITION_HOLD primitive evidence supports only the stated research model. All new RSI/MACD/EMA/ATR event definitions are researcher-selected and reproducible, not source-reported execution facts.

### Six-gate evidence for independent auditor

1. Deterministic float64 SMA/EMA/RSI4/MACD12-26-9/ATR14 seeds, strict cross/tie boundaries, three-bar conjunction edge, trend, frozen ATR, explicit price and fee models.
2. BTCUSDT Binance spot 1h LONG/FLAT only; short/borrow/futures disabled.
3. Complete BUY and three priority SELL conditions, frozen stop/target based on confirmed entry, delayed completed-close fills; no hidden intrabar stop or trailing/TP1.
4. Exact Q/cash, single position/pending, full-fill state, no DCA/pyramiding/concurrency, fresh conjunction re-entry, no last-bar fake fill.
5. Exact pinned Binance spot feed/controller action/MARKET actual-close/POSITION_HOLD/fee and Decimal ledger with fail-closed precision; reuse independently reviewed bounded primitive #519/#529/#530/#532, no new engine primitive or claimed live acceptance.
6. 220 completed bars, decision at E[t], next completed-close fill at E[t+1], no incomplete bar, future leak, synthetic prices or ambiguous intrabar events.

**Dedup (2026-10-28):** GitHub connector current-main searches for `DWzDv6Do`, `Oberon777`, `RSI4 MACD12`, `SMA5 SMA8 SMA13`, and temporal RSI/MACD conjunction returned no matching source/identical rule record; existing RSI-only, MACD-only and RSI-MA-cross families are materially different. GitHub issue/PR search for `DWzDv6Do` returned none. All 10 open `research/*` PR titles were checked and none represent this TradingView script or its 3-bar RSI/MACD + SMA-ribbon conjunction. Baseline main `c7e0c67edb25f2e5937c1a462d6e3819f65aedc2`: README 391, tree 391 root strategy records (excluding both READMEs). The immediately preceding #533 independent review reports full 390/390 PASS census, and its sole added record is presently PASS; this Scout did not re-download/reparse all 391 frontmatters.

## Falsification plan

Under separate future authorization only: test RSI no-change/zero-loss/zero-gain, MACD and EMA first-valid indices, 30 equality, two events separated by exactly 2 vs 3 bars, conjunction false-to-true edge, trend equality, ATR seed and stop/target priority, pending and fill-bar suppression, gaps through stop, missing bar/price fail-closed, Decimal full-fill/dust/fees, last-row pending and point-in-time prefix invariance. Validate a genuinely new Qlib/HB execution primitive with representative event-level parity before mass Qlib screening; none is run here.

## Crypto portability

Explicit independent BTCUSDT spot 1h derivative. Original indicator is primarily 1m–5m manual scalping; no claim of source equivalence, live scalp latency, or automatic port to other markets, timeframes, futures or DCA.

## Limitations

First-party public description is verified, but the complete original Pine text/revision is not independently accessible in this research read. RSI threshold 30, MACD12/26/9, RSI recovery operator, conjunction edge, 1h market, close-triggered 2R bracket, fill timing, position size and costs are **declared researcher choices**, not reconstructed source facts. Historical completed-close MARKET fill is idealized and may be unavailable live; there is no guaranteed stop protection, measured slippage, spread, real fee tier, order minimum validation or performance evidence. The independent auditor must reject if any claimed pinned-model path is not substantiated.

## Implementation status

`implementation_status: not-implemented`. Research-only strategy specification; no dedicated controller, Hummingbot/Qlib execution, container, trading or deployment performed.

## Adoption boundary

`status: research-only`; `adoption: not-approved`; `approval_scope: research-only`. Proposed `hb_ready_status: PASS` is for independent Hermes Auditor GitHub Webhook Review; Scout does not self-approve, merge or close. Existing signed webhook receiver alone reconciles README after a confirmed accepted merge.

## Related Wiki records

No new Wiki/registry entries; similar RSI/MACD families are not asserted equivalent.

## Sources

- https://www.tradingview.com/script/DWzDv6Do-Scalper-SMA-RSI-MACD-Entry-Exit-Signals-v2/ — Oberon777, TradingView first-party public open-source indicator description, 2025-08-14; inspected 2026-10-28.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned source inspected with connected GitHub app.
- https://github.com/HCH725/alpha-strategy-research/pull/519 — independent bounded MARKET/POSITION_HOLD primitive audit.
- https://github.com/HCH725/alpha-strategy-research/pull/529 — independently reviewed pure-research accounting path.
- https://github.com/HCH725/alpha-strategy-research/pull/532 — recent independent bounded execution audit.
