---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "blackcat1402 Inverse Fisher RSI5 WMA9 -0.5/+0.5 BTC-USDT spot 1d long-flat — independent derivative"
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
source_as_of: 2025-04-15
sources:
  - https://www.tradingview.com/script/IpEGZL45-blackcat-L2-Ehlers-Inverse-Fisher-RSI/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# blackcat1402 Inverse Fisher RSI5/WMA9 threshold long-flat — independent derived strategy

## Provenance

**First-party public source:** blackcat1402, *[blackcat] L2 Ehlers Inverse Fisher RSI*, TradingView stable script **IpEGZL45**, published **2020-11-21**, release notes updated **2025-04-15**, inspected **2026-10-26**: https://www.tradingview.com/script/IpEGZL45-blackcat-L2-Ehlers-Inverse-Fisher-RSI/ . The page labels the indicator open-source but the publicly retrievable page text did **not** expose the complete Pine source/revision hash. Its prose describes RSI-based inverse Fisher compression, an IFish fast line, a trigger slow line, normalization against RSI high/low, and customizable buy/sell crossing lines. Its April 2025 notes list default **hl2**, alpha **0.1**, RSI length **5**, WMA length **9**, and buy/sell reference levels **±0.5**. The author publishes an **indicator**, not a complete executable strategy with fills, position sizing, or costs.

**Independent derivative, explicitly NOT source-native or lossless Pine:** This record independently chooses the *exact* Wilder RSI seed and recursion, applies a researcher-defined 0.1 centered-RSI scale, applies WMA9 to that scaled series, uses the mathematical inverse-Fisher/tanh map, assigns **-0.5 upward cross** to long entry and **+0.5 downward cross** to long exit, and defines spot/1d, sizing, costs, execution clock, risk, and order state. Although the page's numeric defaults inspire this configuration, the public prose does not prove its internal RSI normalization, alpha semantics, WMA placement, IFish/Trigger relation, or precise buy/sell predicates. In particular **the source's highest/lowest RSI normalization and separate trigger line are NOT reproduced**; their omission changes potential signals. No claim of original Pine trade-event equivalence or reproduced source statistics is made. All unspecified or modified behavior is research-defined, not silently attributed to the author.

**Immutable research identity:** `TV:IpEGZL45:blackcat1402:2020-11-21:update-2025-04-15 | independent-derived-v1 | HL2-WilderRSI5:seed-SMA5 | x=0.1*(RSI-50):WMA9:tanh | cross-up(-0.5) entry:cross-down(+0.5) exit | BinanceSpot:BTC-USDT:UTC-1d:LONG-FLAT:0.001BTC | completed-close-MARKET:trade_cost-0.001 | 2026-10-26`. Any changed indicator formula, trigger, execution time, venue, size or cost is a new derivative.

**Dedup on connected GitHub main:** Snapshot `2b6542df32e628c3deb6dde90f0cef5e77d397c0` (2026-10-26): untruncated recursive tree contained **350** root-level strategy Markdown files, static README count **350**. GitHub exact-source `IpEGZL45` search of main and all PRs returned zero; 10 open `research/*` PRs were checked and none has this TradingView URL or these rules. Nearest mechanisms are main `fisher-zero-cross-reversal-btcusdt-1d-2026-10-09.md` (Fisher transform of normalized hl2, **zero-line two-sided** reversal, not inverse Fisher of RSI5 with two asymmetric thresholds) and `freqtrade-strategy003-rsi-fisher-mfi-washout-ema-gated-long-flat-btcusdt-5m-2026-10-21.md` (unsmoothed RSI14 tanh in a multi-indicator MFI/EMA/Stochastic washout with ROI/stop; not this standalone WMA9 threshold-cross regime). Distinct primary source, signal formula, gating, exits, and risk/state. Count equality is not an independent re-audit of all 350 historical PASS frontmatters.

## Economic mechanism

**Source-reported:** Nonlinear inverse Fisher compression of RSI emphasizes oscillator extremes; source documentation mentions adjustable ±0.5 reference lines and an additional trigger. No verified executable position/cost model or independently replicated performance is provided.

**Derived hypothesis:** An upward recross of -0.5 by a WMA-smoothed RSI inverse-Fisher oscillator signals recovery from bearish momentum; hold until the oscillator, having reached above +0.5, subsequently crosses below +0.5. This deliberately asymmetric recovery/rollover model may hold through large losses when the +0.5 region is never reached. No protective stop is supplied.

## Signal

**Market and point-in-time data:** One Binance spot `BTC-USDT` UTC daily (1d) OHLCV series, sorted by unique exchange **open** timestamp `T[t]`, with consecutive timestamps exactly 86,400 seconds apart. Validate finite positive O/H/L/C, `H>=max(O,C)`, `L<=min(O,C)`, and finite volume >= 0. No duplicate, missing, synthetic, interpolated, or forward-filled candle. Candle `t` is usable only at `D[t]=T[t]+86400`, after it is fully completed. `P[t]=(H[t]+L[t])/2` (hl2) is the sole indicator input.

**Exact independently specified oscillator:** For `t>=1`, `d[t]=P[t]-P[t-1]`, `g[t]=max(d[t],0)`, `l[t]=max(-d[t],0)`. For `t=5`, seed `G[5]=sum(g[1..5])/5`, `L[5]=sum(l[1..5])/5`. For `t>5`, `G[t]=(4*G[t-1]+g[t])/5` and `L[t]=(4*L[t-1]+l[t])/5`. Define `RSI[t]=50` when `G=L=0`, `100` when `L=0<G`, otherwise `100-100/(1+G/L)`. Then `x[t]=0.1*(RSI[t]-50)` (the 0.1 scaling is a **researcher-defined mapping**, not a verified source-alpha formula). For `t>=13`, `v[t]=(sum(k*x[t-9+k],k=1..9))/45` (WMA9: oldest weight 1, newest weight 9). `IFish[t]=tanh(v[t])=(exp(2*v[t])-1)/(exp(2*v[t])+1)`. Use unrounded double precision for indicators, Decimal for order quantities/cash. No min/max RSI normalization, separate Trigger line, fitting, other smoothing, divergence, lookahead, or intra-candle decisions.

**Warmup and initial state:** Require **60** consecutive completed valid daily bars before any order; first possible decision at `t=59`, with both `IFish[t-1]` and `IFish[t]` defined. Start FLAT with 10,000 USDT cash, zero BTC, no inferred historical exposure and no pending orders. If the first eligible IFish is already above the entry threshold, do not synthesize a prior crossing.

**Entry:** On fully completed candle `t`, `entry[t] = IFish[t-1] <= -0.5 AND IFish[t] > -0.5`. Only when FLAT, no pending order and no same-bar exit, submit one MARKET BUY for exactly 0.001 BTC at the historical completed-candle close, conditional on actual available USDT >= `0.001*C[t]*(1+0.001)`. Do not enter on a persistent above-threshold level. No short leg.

**Exit:** On fully completed candle `t`, `exit[t] = IFish[t-1] >= +0.5 AND IFish[t] < +0.5`. Only when confirmed LONG and no pending order, submit one MARKET SELL for the entire confirmed BTC quantity at the historical completed-candle close. Strict downward crossing only; equality alone does not exit. If the oscillator never first reaches +0.5, there is no indicator exit. No forced liquidation at the end of sample; mark remaining inventory only at the final actual completed close for reporting, not as a fabricated sell.

**Priority and fill-confirmed state:** Evaluate exit before entry; no same-bar exit/reentry. FLAT -> BUY_PENDING -> LONG only on confirmed full BUY fill; LONG -> SELL_PENDING -> FLAT only on confirmed full SELL fill. At most one pending order and one position. Rejected/unfilled BUY clears pending, remains FLAT, and waits for a fresh future upward cross; no automatic retry on the same signal. Rejected/unfilled SELL remains LONG and retries once at the next valid completed bar regardless of IFish, without duplicate simultaneous orders. If partial fills, precision/lot violations, unknown fee or missing actual fill price cannot be represented reliably, hold/abort the research run rather than assume a full fill. No fixed cooldown beyond no same-bar reentry and fresh-entry-cross requirement.

**Explicitly disabled:** shorting, derivatives, margin/leverage, funding, pyramiding, BO/SO/DCA, multiple simultaneous positions, shared capital, dynamic sizing/compounding, intrabar/maker/limit/next-open orders, separate trigger-line cross, RSI extrema normalization, discretionary entries/exits, SL, TP, trailing stop, time exit, higher/lower-timeframe filters, end-of-sample forced sale, and any undeclared controller default. No stop is a risk limitation, not a guarantee.

**Invalid-data behavior:** Missing/gapped/duplicate OHLCV, unavailable actual close, nonfinite indicator, missing fee/cash, ambiguous fill or invalid timestamp makes the research run invalid; never substitute a fabricated price or silently drop a candle.

## Required data

Only one real Binance spot BTC-USDT UTC 1d OHLCV feed with >=60 consecutive fully completed candles, and pinned Hummingbot simulated order/fee/position records. No external series, order-book data, futures mark/funding, fitted model, cross-asset clock or lower-timeframe fill prices. No source-reported performance data is treated as independently reproduced.

## Execution assumptions

**Pinned engine directly inspected through GitHub app on 2026-10-26:** admission package `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. Immutable `hummingbot/VERSION` reports `dev-2.17.0`; `binance_spot_candles/constants.py` permits `1d`; `binance_spot_candles.py::_parse_rest_candles` reads exchange row[0] as candle **open timestamp** and row[1..5] as OHLCV. This run re-read `backtesting_engine_base.py`, `order_executor_simulator.py`, `order_executor/data_types.py`, and `backtesting_data_provider.py`. Package-to-source wheel byte identity is supported by prior independently reviewed Alpha PR **#414** (902/902 wheel byte-identical as reported there), **not independently rehashed this cycle**; bounded primitive review also exists in merged PR **#417**.

**Controller/executor path:** A future minimal strategy-specific ControllerV2/backtesting controller (not implemented or deployed by this record) computes only completed-bar IFish and emits `CreateExecutorAction` for `OrderExecutorConfig` on connector `binance`, pair `BTC-USDT`, side BUY/SELL, amount `Decimal("0.001")`, `position_action` OPEN/CLOSE as appropriate, `execution_strategy=MARKET`, `price=None`, `leverage=1`. `BacktestingEngineBase` runs controller updates and executor actions, then `OrderExecutorSimulator.simulate` MARKET path selects the first supplied historical row's **actual close**, `filled_amount_quote=Q*close`, `cum_fees_quote=trade_cost*filled_amount_quote`, and `CloseType.POSITION_HOLD`. `BacktestPositionHold` matches opposite-side base fills, tracks average cost and gross PnL, and accumulates quote fees separately. A mere config/API name is not proof of full live order execution; this is the specific inspected historical close-fill and position-cost path.

**Causal clock fence:** Raw candle rows carry `T[t]` = OPEN timestamp while simulator uses that row's CLOSE. The derivative's *effective* decision and fill time is `D[t]` = UTC candle close, after data availability; never claim an order at the raw `T[t]` using future close. Same-completed-row close fills are an **idealized historical backtest convention**, not guaranteed real-world same-close execution. A future implementation must preserve this economic clock mapping before downstream use. No future candle, next-open quote or fabricated trade price is used.

**Fees and ledger:** Research-assumed `trade_cost=0.001` per side (0.1% of observed filled quote notional), **not** a verified Binance fee tier. Simulated slippage/spread/latency is **not modeled**, not asserted to be zero in reality. Initial 10,000 USDT unborrowed cash; a confirmed BUY at P reduces cash by `Q*P*(1+0.001)`; a confirmed SELL at P increases cash by `Q*P*(1-0.001)`; net realized quote PnL of a completed round trip is `Q*(P_sell-P_buy)-0.001*Q*(P_sell+P_buy)`. Do not confuse gross position PnL with net-of-fee cash economics. Spot has no perpetual funding leg (**not applicable**, not fabricated zero realized funding). Real exchange tick/lot/notional precision, live fee tier, slippage and partial fills are not independently verified.

**Source-code safeguards:** `BacktestingEngineBase` defaults terminated-executor retention to a 3600-second window; daily state must set `terminated_executors_window=None` or use a persistent confirmed-fill ledger, or older fills may be invisible. `BacktestingDataProvider.get_price_by_type` may fall back to `Decimal("1")` on missing prices; this strategy must reject missing actual closes rather than accept that fabricated fallback. `prepare_market_data` can drop NaN rows; validate candle continuity before running so a missing day cannot be compressed into a false RSI/WMA window. Confirmed order fills, not submitted actions, determine position/cash state.

## Evidence

**Primary-source facts verified:** TradingView first-party page, blackcat1402, 2020-11-21 publication and 2025-04-15 update, open-source indicator description and default hl2 / 0.1 / RSI5 / WMA9 / ±0.5 settings. Full Pine bytes were not retrieved; no claim of exact source oscillator, native orders, or author performance replication.

**Independent researcher specification:** Exact Wilder RSI5 on hl2, WMA9 of 0.1-centered RSI, tanh, asymmetric threshold crossings, Binance spot UTC 1d, 60-bar warmup, completed-close MARKET model, 0.001 BTC single position, fill-confirmed state, explicit fee/cash accounting and disabled risk features. These are derived choices, not facts about the original Pine.

**Six HB_READY gates for independent Hermes Auditor:** (1) exact indicator/seed/thresholds and frozen state with no fitted parameters; (2) Binance spot LONG/FLAT, SHORT off; (3) complete entry/exit with absent stops/targets/trailing/time exits declared; (4) one unit, no DCA/concurrency, explicit pending/rejection/retry/re-entry rules; (5) real pinned GitHub source paths for Binance spot 1d candles, MARKET close-fill, fees, controller action loop, POSITION_HOLD ledger, cost and clock hazards, with no new primitive; (6) 60 completed daily bars, no future leakage, effective close-time decision/fill and strict gap handling. This is a **candidate PASS proposal subject to independent audit**, not self-approval, strategy implementation, Qlib parity, profitability, Survivor certification, or Paper/Testnet/Live authorization.

**Limitations:** The source's RSI-extrema normalization and separate IFish/Trigger line are deliberately not reconstructed; full Pine code/revision unavailable. Same-bar-close historical fills, fee assumption, no protective stop, no live precision/funding/slippage verification and no source-event parity constrain interpretation. No backtest, model-specific implementation, strategy-specific Hummingbot/Qlib event-level parity, or performance statistics were produced. Representative Qlib/Hummingbot parity of any newly introduced execution primitive is required before large-scale Qlib screening; this proposal claims only the previously inspected bounded historical spot close-fill primitive.
