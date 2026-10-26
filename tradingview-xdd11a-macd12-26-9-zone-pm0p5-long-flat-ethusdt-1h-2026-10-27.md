---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "xdd11a MACD 12/26/9 both-line ±0.5 zone-gated long-flat — independent ETH-USDT spot 1h derivative"
created: 2026-10-27
updated: 2026-10-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
  - derived
status: research-only
confidence: medium
source_as_of: 2025-03-08
sources:
  - https://www.tradingview.com/script/nXAGBlDH-MACD-Crossover-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# xdd11a MACD 12/26/9 both-line ±0.5 zone-gated long-flat — independent ETH-USDT spot 1h derivative

## Provenance

**Primary first-party TradingView source:** xdd11a, *MACD Crossover Strategy*, published **2025-03-08**, stable script ID **nXAGBlDH**: https://www.tradingview.com/script/nXAGBlDH-MACD-Crossover-Strategy/ . Public description inspected **2026-10-27**. The author explicitly describes MACD fast 12, slow 26, signal 9 defaults; an "important zone" bounded by -0.5 and +0.5; bullish/bearish MACD-line-versus-signal-line crosses as long/short entries when inside that zone; and closing positions on the opposite cross. The publication is labeled open-source, but complete Pine bytes, Pine version, zone predicate's exact line-membership convention, order-fill timing, cost defaults and any implicit Pine order settings were **not retrieved**. Those unknowns are not attributed to the author.

**Independent derivative, NOT source-native or a Pine reconstruction.** The researcher separately fixes: Binance ETH-USDT **spot UTC 1h**, LONG/FLAT only (source short leg disabled); both current MACD and signal line must each be within the inclusive [-0.5,+0.5] absolute-price-unit zone on long entry; the opposite bearish cross closes a long **without any zone requirement**; EMA seed and equality behavior; 120-bar flat warmup; same-completed-bar historical MARKET close-fill model; one fixed 0.01 ETH position; no SL/TP/trailing/DCA; 10,000 USDT starting modeled cash; and 0.1% hypothetical fee per filled side. Each is a researcher-authored decision, may change the source trade-event set, and is never described as an original Pine default.

**Immutable research identity:** TV:nXAGBlDH | xdd11a | publication:2025-03-08 | independent-derivative-v1:2026-10-27 | Binance:ETH-USDT:spot:UTC1h | EMA12/26 MACD, EMA9 signal, SMA-seeded | both-lines-absolute-zone[-0.5,+0.5] gated bullish cross entry | unconditional bearish cross exit | LONG/FLAT:0.01ETH | 120-bar warmup | historical-completed-close MARKET | fee=0.001 per side. Any change to a decision-critical element is a different revision, not a silent edit.

**Dedup, current main snapshot 548f2ad8d58377a3c0c82e63f02d38fb738a4448:** GitHub connector search found no nXAGBlDH, xdd11a, or MACD "important zone" record on main; open research/* PR titles and primary-source descriptions contain no such source. Closest main family *macd-signal-cross-reversal-btcusdt-1d-2026-10-09.md* is ungated, two-sided and reverses on every MACD cross; *forven-macd-cross-adx-regime-long-flat-ethusdt-1h-2026-10-19.md* uses EMA5/13/3 with ADX>=20 plus EMA200 regime gating. This candidate has a **both-line bounded absolute MACD zone** with standard 12/26/9 and no ADX/EMA200 regime, producing a materially different entry-event set; not a mere rename or timeframe change. Code search is not a proof of exhaustive absence of all paraphrases. Main tree had 374 root strategy Markdown records and README declared 374; sample PASS frontmatter reads do not constitute a fresh audit of every existing record.

## Economic mechanism

### Source-reported

The author attempts to select MACD crossovers close to a bounded oscillator zone, rather than following every momentum cross. The author's two-sided short/long signals and opposite-cross exits are source description, **not** the executable strategy proposed below. No source backtest result is treated as independently reproduced.

### Research interpretation

This derivative tests whether requiring **both** MACD lines to be near zero in absolute ETH-USDT quote units before a bullish cross improves fee-net expectancy versus ungated 12/26/9 bullish crosses, while retaining a simple ungated bearish-cross exit. Absolute thresholds are price-scale dependent; transfer to BTC, SOL, another price regime or another quote denomination would be a separately declared research revision, not presumed portability.

## Signal

All clauses below are the frozen, independent derivative specification; none is a claim about uninspected Pine internals.

1. **Data:** chronological completed Binance ETH-USDT spot UTC **1h** OHLCV candles indexed t=0,1,...; use close C[t] for indicators and simulated fills. Each bar has finite positive O/H/L/C with L<=min(O,C)<=max(O,C)<=H and finite nonnegative volume. Consecutive Binance open timestamps differ by exactly 3600 seconds; missing, duplicated, partial, zero-priced or invalid rows abort the segment before feature merge, with no forward-fill/interpolation/dropna gap concealment.
2. **EMA:** for any length n, first defined at index n-1 as SMA(C[0..n-1]); for t>=n, EMA_n[t] = (2/(n+1))*C[t] + (1-2/(n+1))*EMA_n[t-1]. All arithmetic chronological float64, no rounded indicator thresholds or adaptive fit. EMA12 first valid at t=11, EMA26 at t=25.
3. **MACD:** M[t] = EMA12[t]-EMA26[t], valid from t=25. Signal G[t] = EMA9(M)[t] with first seed equal to SMA(M[25..33]) at t=33, then EMA recursion alpha=0.2 from t=34. Histogram M-G is diagnostic only, not an order condition.
4. **Cross:** bullish[t] iff M[t]>G[t] AND M[t-1]<=G[t-1]; bearish[t] iff M[t]<G[t] AND M[t-1]>=G[t-1]. Previous equality qualifies for a later strict cross; current equality fires neither side. Comparisons are exact on computed float64 outputs, without epsilon or rounding.
5. **Entry zone:** zone[t] iff -0.5<=M[t]<=+0.5 AND -0.5<=G[t]<=+0.5. Both bounds inclusive; no requirement that the previous bar's MACD lines were in the zone. This both-line rule is a **researcher definition** resolving the public description's unspecified "within zone" predicate.
6. **Warmup:** bars t=0..119 are completed-data warmup, with FLAT initial state, no inferred pre-window inventory, no simulated orders. First eligible decision is t=120, requiring current and prior valid M and G.
7. **Entry:** on eligible completed bar t, if FLAT, no pending order, bullish[t] AND zone[t] AND cash sufficient for Q*C[t]*(1+f), issue one MARKET BUY of Q=Decimal("0.01") ETH. Full historical simulated fill at the observed completed close C[t]; never earlier than the close-availability instant E[t]. An entry rejected for cash/invalid price is skipped and never queued or fabricated.
8. **Exit:** if LONG from a **prior** bar, bearish[t] alone triggers one MARKET SELL of the entire filled 0.01 ETH at the observed completed close C[t], **regardless of zone**. No RSI, stop-loss, take-profit, trailing, time limit, volatility cap, trend exit, or source short order is active. A long can remain underwater indefinitely until bearish cross; that is an explicit risk, not an implicit stop.
9. **Priority and state:** exit first, entry second, but bullish and bearish crosses are mutually exclusive; no same-bar round-trip. Once SELL fully fills, state returns FLAT; no entry on the exit bar and no stale-signal re-entry. Fresh bullish+zone cross on a later completed bar may re-enter. A bullish cross while LONG is a hold-no-op, a bearish cross while FLAT is a no-op, and neither is queued. At most one pending order. An unresolved partial/rejected/ambiguous fill stops that research segment rather than assuming a fill, balance or subsequent position.
10. **End:** final open position is marked at the last actually observed completed close with unrealized PnL reported separately; no invented liquidation or future-bar fee. No lookahead, centered filters, repainting, intrabar high/low stop assumptions, negative shifts, future extrema, ML artifact, cross-market alignment or higher-timeframe candle dependencies.

**Direction/disabled behavior:** Binance unleveraged ETH-USDT spot LONG/FLAT only. Short/borrow/perpetual funding/margin/leverage, DCA/safety orders, pyramiding, averaging, scale-in/out, partial exits, simultaneous positions, multi-pair shared capital, maker queue, intrabar order execution, stops/targets, cooldown timers and discretionary re-entry are disabled. No hidden Hummingbot controller defaults are adopted.

**Cash/cost ledger:** begin with 10,000 USDT and zero ETH. On full BUY at observed price P debit Q*P*(1+f), on full SELL credit Q*P*(1-f), where Q=0.01 ETH and f=0.001 each side. Track full precision Decimal cash/quantity/fees, entry price, realized and unrealized gross PnL and separately fee-net PnL. A SELL never creates negative ETH. No reinvested/percentage-of-equity position sizing. Actual exchange tick/lot/min-notional validation is not claimed; reject unsupported precision or missing trading-rule data for any future executable path rather than silently rounding into a different order.

## Required data

Only the pinned Binance SpotCandles ETH-USDT **1h** historical OHLCV feed; close is a real observed value, never a default/placeholder. REST kline timestamp T[t] is **bar open**, not when the close was available. Define decision and historical simulated fill effective time E[t]=T[t]+3600 seconds after the full candle completes. Validate strictly monotone contiguous timestamps and exclude any incomplete final candle. Historical close fill at E[t] is a bounded research-model convention, **not** a claim a live order sent after E[t] could execute at C[t]. Controller/ledger event timestamps based on T[t] must be normalized to E[t] before event-level comparisons. Restarted segments reset FLAT and require fresh 120-bar warmup.

## Execution assumptions

**Pinned engine/source actually inspected through connected GitHub app 2026-10-27:** Hummingbot package **20260920**, VERSION **dev-2.17.0**, source commit **HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3**. Inspected pinned VERSION; BinanceSpotCandles constants and REST parser; strategy_v2/backtesting/backtesting_engine_base.py and backtesting_data_provider.py; executors_simulator/order_executor_simulator.py; executors/order_executor/data_types.py. Prior independent reviewed PR #414 reports 902/902 wheel/source byte identity and a representative validation for this pinned package, **not freshly reproduced this cycle**.

**Bounded model path:** BinanceSpotCandles INTERVALS contains **1h**; its REST parser maps row[0] to **open timestamp** and row[1..5] to actual O/H/L/C/V. BacktestingDataProvider requests historical candles with an explicit interval; prevalidate continuity/price before BacktestingEngineBase.prepare_market_data(), which can otherwise merge_asof/dropna and conceal invalid data. BacktestingEngineBase.simulate_execution() iterates prepared rows, update_state(row) sets current observed close and features, then controller.determine_executor_actions() emits CreateExecutorAction with OrderExecutorConfig. This proposed derivative requires a **not-yet-implemented minimal strategy-specific controller** for the declared MACD/zone/state machine; an API accepting a config does not mean that controller exists.

**Order and accounting path:** OrderExecutorConfig: connector_name="binance", trading_pair="ETH-USDT", side=BUY or SELL, amount=Decimal("0.01"), execution_strategy=MARKET, price=None, leverage=1, explicit OPEN/CLOSE position_action. The pinned OrderExecutorSimulator MARKET branch fills on the first supplied historical candle at its **actual close**, sets filled_amount_quote=Q*close and cum_fees_quote=trade_cost*Q*close, and terminates with CloseType.POSITION_HOLD. BacktestPositionHold nets opposing BUY/SELL, uses weighted cost for same-direction additions (disabled here), tracks gross realized PnL and accumulates quote fees separately. Use trade_cost=0.001 per filled side, with independent cash/fee reconciliation and durable position/fill state. The default one-hour terminated-executor view can expire between bars; use a durable position-hold/ledger or the pinned terminated_executors_window=None option rather than infer FLAT from an expired view. Pinned final-tick executor/position flush exists.

**Boundaries:** Spot funding is **not applicable**; no fabricated zero-funded futures accounting. 0.1% per-side fee is an explicit hypothetical research parameter, not a verified Binance customer tier. No modeled slippage/spread, maker queue, partial fills, market impact, exchange lot/precision or real order-book liquidity is claimed. The native historical close-fill model and raw-open-timestamp caveat are explicit. BacktestingDataProvider.get_price_by_type has a Decimal("1") fallback: it **must not** be used to fill missing data; reject absent/invalid actual close. No strategy backtest, paper/testnet/live trading, or Qlib parity is claimed. Before a new execution primitive is used in mass screening, representative event-level Qlib/Hummingbot capability parity must be established separately.

### Six-gate HB_READY assessment — Scout-proposed PASS, independent audit required

1. **Deterministic:** SMA-seeded EMA12/26 and EMA9 signal, explicit current/prior strict-cross/equality, two-line inclusive ±0.5 absolute zone, 120-bar warmup, no fitted or hidden state.
2. **Direction:** ETH-USDT spot LONG/FLAT; short leg explicitly disabled.
3. **Entry/exit/risk:** gated bullish cross BUY; ungated bearish cross full SELL; no SL/TP/trailing/time or other exits, with downside exposure acknowledged.
4. **Position/state:** one 0.01 ETH position, 10,000 USDT cash ledger, no DCA/concurrency/cooldown, full-fill pending guard, fresh-cross-only re-entry and no same-bar round-trip.
5. **Pinned compatibility:** directly inspected immutable 1h Binance spot data path, OrderExecutor MARKET historical close-fill, POSITION_HOLD netting, per-side fee accounting, raw timestamp and precision limits; missing data fail closed.
6. **Causality:** 120 completed bars warmup, prefix-only recursive indicators, bar-open timestamps explicitly normalized to completion time, no future input or intrabar fill claim.

**PASS in frontmatter is a Scout proposal only.** Independent Hermes Auditor must independently verify the source facts, six gates and exact PR head before any merge.

## Evidence

### Source-reported

xdd11a's 2025-03-08 TradingView page reports MACD 12/26/9 defaults, ±0.5 "important zone", gated bullish/bearish cross entries and opposite-cross exits. Complete Pine code, exact native zone membership, fill timing, source sizing and commission were **not available** in the inspected public page. No original strategy performance statistics are reproduced.

### Independently reproduced

**None.** No TradingView Pine replay, Hummingbot/Qlib backtest, profitability estimate, Sharpe, drawdown, OOS, Survivor or HB Certified result. This Scout inspected the pinned Hummingbot **source code path**, not installed wheel bytes or executed controller tests; prior independent package mapping is cited, not rerun.

### Negative evidence

No original Pine source/version bytes; no claim that original two-sided strategy was ported losslessly; no production controller or actual market fill, cost, exchange precision or funding proof; no claim that the same-completed-close model is a tradable post-close price; no Qlib event parity. Zone interpretation, one-sided mapping, venue/timeframe, EMA seeding, no stops and fees are **independent researcher choices**, not facts invented about the author.

## Falsification plan

Under separate downstream authorization, replay a representative pinned Hummingbot and Qlib tape with equal MACD/signal, zone-edge ±0.5 ties, bullish crosses outside/inside zone, bearish exits outside zone, 120-bar warmup, missing candle, fee-net ledger, insufficient cash, end-of-run inventory and timestamp normalization. Compare gated versus ungated MACD entry events at the same costs. Any unexplained event divergence blocks downstream parity/certification; fee-net underperformance falsifies the research hypothesis. **No such replay was run here.**

## Crypto portability

ETH-USDT spot 1h and the absolute ±0.5 zone are a deliberate independent research scope, not a TradingView author-verified crypto setting or HB_READY whitelist. BTC/other pairs, 1d/4h, short, isolated futures 3x/5x, and BO/SO 6/6/6 are optional separately specified downstream experiments, **not admission prerequisites**. Absolute MACD price units make unmodified cross-market thresholds especially suspect.

## Limitations

No full original Pine bytes or source revision hash were retrieved. An absolute MACD zone can suppress nearly all signals at some ETH price regimes. Close-only bearish-cross exits offer no protective stop, and modeled close fills are idealized. The record is a precise independently derived **research-only** specification, not an executable Hummingbot controller, profitability assertion or approval for trading.

## Implementation status

**not-implemented.** Minimal strategy-specific controller and reproducible execution artifact may be required only after downstream selection. HB_READY admission is not Qlib implementation admission; no new registry, compiler, runner or control plane is introduced.

## Adoption boundary

**research-only; adoption: not-approved; approval_scope: research-only.** Hermes Auditor GitHub Webhook Review alone owns source-fact remediation, exact-head PASS merge or NOT_LOSSLESS close. The existing signed webhook receiver alone owns post-merge README count reconciliation. No merge, approval, README edit, Qlib/Hummingbot execution, container change, trading or cron action is authorized by this record.

## Related Wiki records

None created or modified. Existing MACD family records cited in Provenance are dedup comparisons, not dependencies.

## Sources

- First-party TradingView: https://www.tradingview.com/script/nXAGBlDH-MACD-Crossover-Strategy/ (xdd11a, published 2025-03-08; description inspected 2026-10-27).
- Immutable Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independent pinned package/source mapping: https://github.com/HCH725/alpha-strategy-research/pull/414
- Canonical policy: https://github.com/HCH725/alpha-strategy-research/blob/548f2ad8d58377a3c0c82e63f02d38fb738a4448/.github/HB_READY_REVIEW.md
