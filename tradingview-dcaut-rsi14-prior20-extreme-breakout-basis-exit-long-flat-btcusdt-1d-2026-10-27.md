---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "DCAUT RSI14 prior-20 RSI-Donchian breakout and basis exit — independently derived BTC-USDT spot 1d long-flat"
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
source_as_of: 2025-10-11
sources:
  - https://www.tradingview.com/script/5lrkj99Y-RSI-Donchian-Channel-DCAUT/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# DCAUT RSI Donchian momentum breakout — independent long-flat derivative

## Provenance

**Primary first-party source:** TradingView public open-source indicator, DCAUT, *RSI Donchian Channel [DCAUT]*, stable script ID `5lrkj99Y`, published **2025-10-11**, https://www.tradingview.com/script/5lrkj99Y-RSI-Donchian-Channel-DCAUT/ . Its public description was directly inspected on **2026-10-27**. It describes an RSI on configurable price source (default close) using RMA (default), RSI lookback 14 and Donchian RSI channel lookback 20 as the standard swing configuration; upper/lower are rolling RSI maxima/minima and basis is their midpoint. It describes momentum breakouts, basis exits, optional trend/price confirmations, and other *suggested* trading applications. The accessible rendered page did **not** provide the actual Pine source bytes, exact executable alert/order booleans, revision hash or broker fills. The page is an **indicator**, not evidence of a source-native executable strategy or backtest. No source performance is reproduced.

**Independent derived strategy (not lossless Pine):** The researcher specifies a strict breakout above the **preceding** 20 completed RSI observations, exits on a level at/below the preceding 20-observation RSI channel midpoint, and disables all optional source suggestions. In particular, an RSI strictly exceeding an upper channel that already **includes the current RSI** is mathematically impossible; the source's prose does not resolve this Pine detail. The **prior-window convention is explicitly researcher-defined**, not attributed to DCAUT. Also researcher-defined: Binance BTC-USDT spot UTC 1d; long/flat only; fixed 0.001 BTC; initial cash 10,000 USDT; 100 completed-bar warmup; next-row historical close MARKET fill after the preceding completed-row signal; full-fill-only position ledger; hypothetical 0.1% fee each side; no intrabar SL/TP, price confirmation, higher-timeframe trend, width/squeeze filter, volume filter, shorts, DCA or scaling. These choices change source signal and order semantics. They are **not** a reconstructed TradingView strategy.

**Frozen identity:** `TV:5lrkj99Y:DCAUT:2025-10-11 | independent-v1:2026-10-27 | RSI14(close,RMA-seed14), prior-RSI-Donchian20 strict upper breakout, prior-basis level exit | BTC-USDT Binance spot UTC1d | 100-bar warmup | signal s completed -> MARKET close fill s+1 | 0.001 BTC | fee 0.001/side | no adds`. Altering any element is a new derivative, not a parameter-only relabel.

**Dedup checked with connected GitHub app 2026-10-27:** main SHA `e2e6ce843998cb68e417d891347586bd4e0e3c87`; untruncated tree has 368 root strategy Markdown records, README counter 368. Code search for the stable TradingView ID `5lrkj99Y` and source name found no same-source main record; ten open research/* PRs were enumerated and none cites that ID or materially identical RSI-on-RSI-extrema breakout. Price-Donchian breakout records use extrema of **price**, not extrema of the RSI oscillator; existing fixed RSI threshold and RSI/EMA systems do not construct this adaptive oscillator channel. This does not claim a full independent re-audit of every pre-existing PASS frontmatter.

## Economic mechanism

The source's adaptive RSI channel tracks momentum extremes rather than fixed 30/70 RSI levels. This derivative tests a **fresh momentum-extreme continuation** hypothesis: a new 20-bar RSI high initiates long exposure; RSI falling back to/below the midpoint of its *prior* recent range terminates it. No claim of profitability, favorable risk, source-Pine parity, Qlib parity or live feasibility.

## Signal

**Data and clock:** Exactly one historical Binance BTC-USDT **spot** UTC 1d OHLCV feed, strictly ascending consecutive candle open timestamps `T[t]` separated by 86,400 seconds. Require actual finite O,H,L,C > 0; `H >= max(O,C)`, `L <= min(O,C)`, `H >= L`, and finite V >= 0. Reject missing/duplicate/gapped/incomplete bars, missing actual close, nonfinite indicator results, fabricated/forward-filled prices or silently truncated prehistory. Binance's timestamp denotes **bar OPEN**, not availability of that bar's close. Bar t is usable for signal only at `D[t] = T[t] + 86400` seconds. No future, synthetic or other-timeframe data.

**Researcher-fixed RSI14:** `delta[t]=C[t]-C[t-1]` for t>=1, `gain[t]=max(delta[t],0)`, `loss[t]=max(-delta[t],0)`. Seed `AG[14]=mean(gain[1..14])`, `AL[14]=mean(loss[1..14])`; for t>14 `AG[t]=(13*AG[t-1]+gain[t])/14`, `AL[t]=(13*AL[t-1]+loss[t])/14`. `RSI[t]=100*AG[t]/(AG[t]+AL[t])` when denominator positive; if both zero, define RSI=50. If AL=0 and AG>0, RSI=100; if AG=0 and AL>0, RSI=0. These are explicitly pinned derivative conventions; calculate in binary64 without intermediate rounding. No RSI post-smoothing, ML, repainting, divergence pivots or chart-only indicators.

**Causal prior-window rails:** for t>=34 define `U[t]=max(RSI[t-20],...,RSI[t-1])`, `L[t]=min(RSI[t-20],...,RSI[t-1])`, `B[t]=(U[t]+L[t])/2`. Thus every reference rail at t uses RSI observations **strictly before t**, unlike a channel that includes the current observation. A zero-width channel is valid; equality comparisons below remain literal.

**Fresh entry signal on fully completed bar s:** `BREAK[s] = (RSI[s] > U[s]) AND (RSI[s-1] <= U[s-1])`. A continuously high RSI without a fresh cross is not a new signal. At s close, if confirmed FLAT with no pending action, schedule one BUY of exactly 0.001 BTC on the next valid bar t=s+1. Ignore BREAK when LONG or pending. **Exit:** on fully completed s, if confirmed LONG and `RSI[s] <= B[s]`, schedule one SELL for the confirmed entire 0.001 BTC on t=s+1. Equality exits. There is no other exit trigger. EXIT takes precedence over entry if a contradictory state occurs (abort if signals violate the rail invariants).

**Warmup and sample edges:** t=0..98 are initialization-only; the first eligible signal is at completion of t=99, with earliest modeled fill at completion of t=100. A full valid 100-bar prehistory is mandatory and may not be inferred from the first trading event. If the sample ends before a scheduled next-row fill, cancel the unfilled intent without inventing a price or trade. If LONG at the last observed completed close, retain inventory and mark to the **actual** last close; do not invent an exit.

**Order/state contract:** FLAT -> BUY_PENDING -> LONG -> SELL_PENDING -> FLAT, only after confirmed full executor fills. One position, one pending order, no simultaneous or overlapping orders. Before BUY, check that the **actual modeled fill price** and `cash >= 0.001 * price * (1+0.001)` are available; if not, abort the replay rather than assume a fill. BUY cash debit = `0.001*Pbuy*(1+0.001)`; SELL credit = `0.001*Psell*(1-0.001)`. Rejected, missing, partial or mismatched fills, unsupported quantization, negative cash, stale executor views or inconsistent net base exposure are **hard research failures**, not synthetic successful orders or automatic retries. After confirmed SELL, a future new BREAK is required for re-entry; no same-row re-entry and no extra cooldown. An ignored signal is not queued.

**Explicitly disabled:** SHORT/borrow/perpetuals/futures, leverage/margin/funding, additional pairs/shared capital, BO/SO/DCA, pyramiding, partial take-profits, partial closes, compounding, position-dependent size, hard or intrabar stop-loss, fixed TP, trailing/time exits, stop/limit/maker orders, optional source price/trend/volume/squeeze filters, alerts, discretionary overrides, hidden controller defaults and forced end-of-sample liquidation. Lack of a protective stop is an intentional **research risk**, not a recommendation.

## Required data

Actual exchange UTC 1d BTC-USDT spot OHLCV and the model's confirmed fills/costs only. Indicators consume close; other OHLCV columns are validity checks. No higher/lower timeframe synchronization, external signal, order-book snapshots, tick data, settlement mark, perp funding or portfolio-wide accounting is required.

## Execution assumptions

**Pinned real source path inspected through GitHub app 2026-10-27:** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`; `hummingbot/VERSION = dev-2.17.0`; canonical Hummingbot package label `20260920` from this repository's current admission contract. The installed package/wheel/image digest was **not** rehashed; this is pinned **source-model** compatibility, not installed-binary attestation. Previously reviewed Alpha PR #414/#417 provide related representative MARKET/POSITION_HOLD capability evidence, not candidate-specific parity.

- **Real data:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` specifies `/api/v3/klines` and `1d`; `binance_spot_candles.py::_parse_rest_candles` reads row[0] as the candle **open** timestamp, row[1..5] as actual O/H/L/C/base volume. `backtesting_data_provider.py` obtains historical candles. Require an independent preflight on completeness, timestamp continuity, finite actual prices and 100-row warmup before `prepare_market_data()` can drop NA rows or silently shift a signal.
- **Real controller/executor path:** `backtesting_engine_base.py::simulate_execution` iterates `update_state(row) -> controller.determine_executor_actions() -> simulate_executor`. A minimal **strategy-specific** DirectionalTradingController (not implemented in this record) can emit `CreateExecutorAction(OrderExecutorConfig(connector_name="binance", trading_pair="BTC-USDT", side=BUY/SELL, amount=Decimal("0.001"), position_action=OPEN/CLOSE, execution_strategy=MARKET, price=None, leverage=1))`. `order_executor/data_types.py` exposes those exact fields. Do not mistake a CreateExecutorAction for a fill; one pending action and confirmed hold/net inventory must be enforced. Require actual exchange trading rules to preserve 0.001 BTC after quantization; otherwise this run is ineligible.
- **Actual historical fill and position semantics:** `order_executor_simulator.py` MARKET selects the first provided row and uses that row's **observed close**, with `filled_amount_quote = 0.001*close`, `cum_fees_quote = trade_cost*filled_amount_quote`, `CloseType.POSITION_HOLD`. `BacktestPositionHold` in `backtesting_engine_base.py` nets filled BUY/SELL base amounts, uses weighted average acquisition cost, and tracks gross matched realized PnL plus separately accumulated quote fees. Configure `terminated_executors_window=None` so the terminated fill history is not silently pruned between daily rows. Keep a confirmed cash ledger as above; no assertion that the engine automatically enforces spot cash.
- **Bounded fee/economics:** pass `trade_cost=0.001` per filled side as an explicit **hypothetical research fee**; do not assert it is the exchange's actual fee tier. No simulated additional slippage; **not** a claim of zero real slippage, spread or latency. Spot funding is **not applicable**, not a fabricated zero-funding perpetual series. Gross realized `0.001*(Psell-Pbuy)`; matched net `0.001*(Psell-Pbuy) - 0.001*0.001*(Pbuy+Psell)`. No leverage, liquidation, borrow interest or perp mark-price accounting.
- **Crucial causal timing:** At engine row t (open-indexed), controller may inspect **only indicators computed through completed row s=t-1**. A MARKET action at row t is historically priced by the simulator at `C[t]`, which is unavailable until `D[t]`; therefore its **economic fill time must be recorded as D[t]**, never as T[t] or as a tradable price known at T[t]. No decision at T[t] may use C[t] or current-row RSI. This deliberately idealized **one-full-bar-lag historical close-fill derivative** is not a live fill guarantee. Enforce input-prefix invariance and reject any implementation that accesses t's close for t's decision.
- **Missing-price guard:** `BacktestingDataProvider.get_price_by_type` can default to `Decimal("1")` for absent prices; never use that fallback. Demand actual validated close and matching executor filled quote before booking an order. No invented price, funding, partial-fill or fee data.

**Gate 5 boundary:** These inspected source files establish the narrow, existing historical **single-spot-pair 1d candle + MARKET close-fill + POSITION_HOLD + explicit modeled fee** path. This record does not require intrabar/maker/next-open/multi-asset/non-OHLCV paths. A future strategy-specific controller and event-level test are required for downstream materialization and Qlib/Hummingbot parity; those are **not** falsely claimed to exist now. A change requiring an unverified execution primitive must be held for representative capability validation, not passed by API name alone.

## Six-gate evidence

1. **Determinism:** fully specified Wilder RSI seed, zero denominator, strict prior-20 rails, thresholds, warmup and binary64 comparisons; no fitted artifact.
2. **Direction:** Binance spot LONG/FLAT; short, margin and leverage disabled.
3. **Entry/exit/risk:** fresh prior-20 RSI high breakout, RSI <= prior basis exit, all other stop/target/filters expressly disabled.
4. **State:** fixed 0.001 BTC, cash guard, one pending/full-fill position, no DCA/scale, fresh-cross re-entry, explicit failure states.
5. **Pinned model:** named immutable Hummingbot files demonstrate Binance 1d data, OrderExecutor MARKET actual historical close, POSITION_HOLD netting and separate modeled quote fees; actual close and trading-rule checks mandatory.
6. **Causality:** completed-bar-only s, decision at next t using <=s, historical fill economic time D[t], 100-bar warmup, no lookahead/partial higher timeframe or repaint.

## Evidence and limitations

**Source-reported:** DCAUT's 2025-10-11 first-party page supplies RSI14/RMA, RSI Donchian20 and upper/lower/basis concepts, and discusses breakout/basis trading applications. Its full Pine logic, order semantics, default trade sizing, fills and performance were **not** retrieved or reproduced.

**Researcher-derived, not source-native:** prior-window rail shift, precise crossover/level exit, one-bar-lag fill, spot instrument, 0.001 BTC, 100-bar warmup, hypothetical 0.1% fee, and disabled modules. None is silently represented as the author's executed orders. No backtest, Pine trade parity, Qlib parity, package hash attestation, actual exchange fee/slippage, or live-trading authorization has been performed. This PASS is a bounded **engine-expressibility research admission proposal** for independent Hermes Auditor review only.

## Review / adoption

**HB_READY: PASS proposed; independent auditor must verify exact current PR head and all six gates.** Research-only; not implemented, not approved, not a Survivor, not HB Certified. Scout must not merge, approve, trade, backtest, deploy or edit README.
