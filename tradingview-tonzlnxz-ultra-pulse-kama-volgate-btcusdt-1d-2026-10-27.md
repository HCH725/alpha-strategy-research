---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Tonzlnxz Ultra Pulse KAMA delta-volatility-gated EMA regime — independent BTC-USDT spot 1d long-flat derivative"
created: 2026-10-27
updated: 2026-10-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-27
sources:
  - https://www.tradingview.com/script/kCL9GRtN-Ultra-Pulse-KAMA/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Tonzlnxz Ultra Pulse KAMA delta-volatility-gated EMA regime — independent BTC-USDT spot 1d long-flat derivative

## Provenance

**First-party TradingView identity:** [Ultra Pulse KAMA](https://www.tradingview.com/script/kCL9GRtN-Ultra-Pulse-KAMA/), author **Tonzlnxz**, immutable public script ID **kCL9GRtN**, directly inspected **2026-10-27**. The page displays publication **Feb 24** without a year in the accessible text; a publication year, Pine version, exact revision hash and complete Pine source **were not independently retrieved**. The page labels the indicator open-source, but that label is not evidence of having read the code.

**Visible source-native mechanism, not source-native order rules:** the author describes Kaufman Adaptive Moving Average (KAMA) using an Efficiency Ratio (ER); KAMA **delta** compared with the standard deviation of its recent movements as a volatility gate; optional dual-EMA trend confirmation requiring price above slow EMA and fast EMA above slow EMA for bullish signals (symmetric bearish definition); selectable aggressive/normal/swing modes, optional Heikin-Ashi source, and confirmed-bar signals. The public description does **not** disclose numeric KAMA/EMA/stddev parameters, exact trigger comparison, stateful entry/exit, sizing, risk, fees, or fill timing.

**This is a fully specified, independently researcher-designed executable derivative v1, NOT the author's Pine strategy and NOT a lossless reconstruction.** Every numeric parameter, seed, signal edge, exit, position, market, timeframe, fill and cost rule below is a researcher-defined choice. The TradingView page supplies the mechanism only, not these choices. The optional Heikin-Ashi and alternate preset modes are deliberately **disabled**; no source-reported performance is imported.

**Immutable derived identity:** TV:kCL9GRtN | Tonzlnxz | public-page-as-of:2026-10-27 | derivative:v1:2026-10-27 | BTC-USDT Binance spot UTC 1d | KAMA20 ER20 fast2 slow30 SMA20 seed | delta20 population-stdev gate 1.25 | EMA10/EMA50 dual bullish regime | strict false-to-true entry, negative-gate/regime-failure exit | 0.01 BTC | close-price MARKET research model | 100-bar warmup.

**Dedup at main SHA e287ed4d893e5bdbc6b5b53ec2aaba059bc5510c:** main had 378 root-level strategy Markdown records and README counter 378; 12 sampled root records carried PASS (not a full 378-file status audit). Connected GitHub code/PR search found no kCL9GRtN / Ultra Pulse source identity; all 10 open research/* PR titles and source descriptions were checked. Nearest main KAMA relatives: HPotter KAMA21 prior-close-versus-KAMA two-sided state and SystemsOverFeelings KAMA40 normalized **slope sign flip** with fixed 6%/3% close bracket. This proposal is not a parameter variant of either: it requires a **rolling dispersion-normalized KAMA delta event plus a simultaneous two-EMA/price regime gate**, and it exits on a distinct negative volatility event or failed regime, not a slope zero-flip, price/KAMA side or fixed bracket. Same KAMA mathematical family alone is not duplicate trading logic.

## Economic mechanism

### Source-reported

Efficiency-ratio adaptive smoothing slows in chop and accelerates in directional price action. The author's delta-standard-deviation filter attempts to distinguish unusually strong KAMA movement from ordinary noise; dual EMAs can suppress counter-regime signals. These are descriptive source facts, not verified original trades.

### Research interpretation

A new, testable hypothesis: after the adaptive average's positive movement exceeds its own recent movement dispersion, only a bullish EMA regime permits a long. Exit if the average shows unusually negative movement or the trend regime fails. This is a regime-and-volatility **event** strategy, not a generic KAMA level cross. Profitability is unknown.

## Signal

All rules below are **researcher-authored derivative v1**, fully pinned; t is a zero-based completed daily UTC candle index, C[t] its finite positive close. Evaluate once per completed candle. Indicators use chronological IEEE-754 float64 operations; no whole-sample fitting, optimizers or future data.

1. **KAMA20:** seed K[19] = arithmetic mean(C[0]..C[19]). For each t >= 20, change[t] = abs(C[t]-C[t-20]); noise[t] = sum(abs(C[j]-C[j-1]) for j=t-19..t). ER[t] = change/noise if noise>0, else 0. Fast = 2/(2+1); slow = 2/(30+1); alpha[t] = (ER[t]*(fast-slow)+slow)^2; K[t] = K[t-1] + alpha[t]*(C[t]-K[t-1]). No alternate initialization, source or smoothing.
2. **KAMA movement gate:** D[t] = K[t]-K[t-1] for t>=20. For t>=39 compute mu[t] = sum(D[j] for j=t-19..t)/20 and sigma[t] = sqrt(sum((D[j]-mu[t])^2 for j=t-19..t)/20), i.e. population stdev, current completed D included. If sigma is non-finite or <=0, both directional gates are false. Otherwise POS[t] = (D[t] > 1.25*sigma[t]); NEG[t] = (D[t] < -1.25*sigma[t]); strict comparisons, equality false. No normalization by price and no use of the next candle.
3. **EMA regime:** EMA10 seeded SMA(C[0]..C[9]) at t=9, recursively E10[t]=E10[t-1]+(2/11)*(C[t]-E10[t-1]); EMA50 seeded SMA(C[0]..C[49]) at t=49, recursively E50[t]=E50[t-1]+(2/51)*(C[t]-E50[t-1]). Bull[t] = (C[t] > E50[t] AND E10[t] > E50[t]), both strict. Bull false on equality or undefined inputs.
4. **Entry gate:** G[t] = POS[t] AND Bull[t]. Bars t=0..99 are exactly **100 completed-bar no-trade warmup**, with all indicator/gate histories computed when defined. Start FLAT at t=100; a BUY at t>=100 requires FLAT, G[t]=true, G[t-1]=false, sufficient modeled quote cash, and no pending order. A gate already true at t=99 does **not** create a warmup-edge trade at t=100.
5. **Exit:** If LONG at eligible bar t, SELL the entire actual filled quantity when NEG[t] OR NOT Bull[t]. If both, record NEG as primary reason; no other exit. A LONG may persist when POS falls below its threshold but neither exit predicate holds. On a SELL bar do not also BUY. If flat, an exit predicate is a no-op.
6. **State/re-entry:** Update G[t] on every completed bar, including when LONG, FLAT or pending. After exit, re-enter only on a **new** false-to-true G transition at a later bar, never merely because G remains true. No other cooldown. Rejected/skipped orders are not queued or retro-filled; a fresh later gate edge is required. Pending action prevents duplicate submissions and clears only when the simulator's fill/failure is reconciled.
7. **Trade direction and disabled behavior:** Binance BTC-USDT **spot LONG/FLAT** only; SHORT, borrowing, futures, leverage, margin, pyramiding, scaling, DCA/safety orders, partial close, trailing, fixed stop, fixed take-profit, time stop, intrabar protective orders, discretionary overrides, and end-of-sample forced liquidation are **all disabled**. Thus adverse loss is not bounded by a stop. No multi-market exposure, portfolio synchronization or shared capital.

**Position/economics:** starting research cash 100000 USDT, BTC inventory 0. On a successful BUY acquire **0.01 BTC** at the model close; debit 0.01*C[t] plus 0.1% modeled quote fee. If cash is insufficient, skip the order without changing position. On a successful SELL reduce exactly the filled 0.01 BTC, credit 0.01*C[t] less 0.1% modeled quote fee; one net spot position maximum. Ledger records fill, entry price, gross realized PnL, separate buy/sell fees, net realized PnL, remaining quote cash, inventory and marked-to-last-observed-close unrealized PnL. No reinvestment or fractional sizing. These capital/fee values are research assumptions, not the author's or Binance's live terms.

## Required data

- Single Binance BTC-USDT spot UTC **1d** OHLCV feed, with only completed positive finite closes used for signal arithmetic. Other OHLCV fields are used to validate candle integrity, not as predictive inputs. No Heikin-Ashi, multi-timeframe, funding, mark/index, order book, trade tape, news, fitted model, cross-symbol or other data dependencies.
- Binance REST kline timestamp is **open time** T[t]; the close C[t] and all signals derived from it become available no earlier than E[t]=T[t]+86400 seconds. Enforce unique strictly consecutive daily opens and the full closed-bar condition. An incomplete current candle is excluded; an absent, duplicated, zero/negative or non-finite close, missing interval, unavailable fill price or invalid timestamp **fails the segment closed**, rather than interpolation, forward-fill, synthetic prices or silent skipping.
- The KAMA/EMA/dispersion computations use only the prefix ending at t, with explicit seeds, 100-bar warmup and no repainting, future extrema, negative shift or full-sample normalization. A new data segment must re-warm from FLAT, not stitch unseen signal state.

## Execution assumptions

**Pinned Hummingbot admission model:** package **20260920**, VERSION **dev-2.17.0**, inspected immutable source commit **HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3**. This cycle used only the connected GitHub app to read VERSION and the exact source paths below. Package-to-source byte equivalence is inherited from prior independent pinned-baseline evidence, **not rehashed in this cycle**; no newer build is silently substituted.

- **Feed/data:** hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py explicitly maps 1d; binance_spot_candles.py _parse_rest_candles reads row[0] as open timestamp and row[4] as close. Prevalidate contiguity and completeness **before** BacktestingEngineBase.prepare_market_data() merges features using backward merge_asof and dropna; do not allow dropna to conceal a missing candle.
- **Controller path:** a future **strategy-specific**, not-yet-implemented controller supplies prefix-only KAMA/EMA/gate features and CreateExecutorAction events to BacktestingEngineBase.simulate_execution(), which updates state before determine_executor_actions(). No controller or Qlib implementation is claimed to exist today.
- **Executor/fills:** OrderExecutorConfig with connector_name=binance, trading_pair=BTC-USDT, side BUY or SELL, amount Decimal(0.01), execution_strategy=MARKET, price=None, leverage=1, position_action OPEN on BUY / CLOSE on SELL. The inspected OrderExecutorSimulator MARKET path fills at the **first supplied candle close**, calculates filled_amount_quote=amount*close, cum_fees_quote=trade_cost*notional and CloseType.POSITION_HOLD. Only a single filled action per bar is allowed. Do not interpret a SELL as initiating a naked spot short.
- **Clock/causality boundary:** the simulator's raw timestamp corresponds to candle **open**, while its modeled fill price is the **same completed candle close**. The strategy uses the engine's explicitly **historical same-completed-close accounting convention**, with economic decision/fill availability labeled E[t] in research event output. It does **not** claim a live market order sent after observing C[t] can obtain C[t], or that the raw T[t] is a causal close-signal time. No next-open, intrabar, maker or stop-fill capability is inferred.
- **Position/cost accounting:** BacktestPositionHold nets opposite-side amounts, tracks average entry and gross realized PnL, and aggregates cum_fees_quote; net quote PnL must subtract **both** filled-side fees from gross, and independent cash/inventory accounting must reconcile. trade_cost=0.001 per side is **explicitly hypothetical**, not an exchange-observed rate. Spot funding is **not applicable**, rather than a zero-funded perpetual assumption. No simulated spread/slippage/latency/partial fills or exchange min-notional/precision verification is asserted; future production use requires those checks.
- **Ledger ordering:** update_state refreshes prior executor/position state before the new action, so an in-flight action and the next update/terminal flush must reconcile fills before considering exposure FLAT again. Retain the authoritative executor ledger or disable short terminated-executor pruning; otherwise an old filled action may disappear from a controller's view. Any missing/unconfirmed fill fails closed, not fabricated.

### Six-gate evidence (Scout proposal; independent Auditor still required)

1. **Determinism:** complete KAMA20 ER recurrence/seed, population-stdev20 of delta, 1.25 threshold, EMA10/50 seeds, strict ties, G edges, input validation and 100-bar warmup.
2. **Direction:** only spot BUY to open LONG and SELL to close LONG; SHORT and leverage disabled.
3. **Entry/exit/risk:** exact false-to-true volatility/regime entry; NEG or regime-failure full exit; no stop/TP/intrabar or other hidden defaults.
4. **Position:** 0.01 BTC, 100000 USDT, fee-aware cash ledger, one in-flight action, no DCA/pyramiding/concurrency, deterministic fresh-edge re-entry.
5. **Pinned model:** source-inspected Binance spot 1d candles, OrderExecutor MARKET close-price fill, CreateExecutorAction, POSITION_HOLD netting and fees, with clock/precision/economic limits disclosed; source commit and VERSION pinned.
6. **Causality:** prefix-only completed bars, 100-bar no-trade seed, open-to-close availability correction, no missing-price invention or future lookahead, same-close fill explicitly a research convention.

**PASS is proposed eligibility for the precise derivative's historical model, not a self-approved audit, source-native replication, Qlib parity, profitability or permission to trade.**

## Evidence

### Source-reported

Tonzlnxz, *Ultra Pulse KAMA*, TradingView script kCL9GRtN, public page as inspected 2026-10-27: KAMA ER adaptivity, delta-versus-stdev momentum gate, optional fast/slow EMA regime, optional Heikin-Ashi and bar-confirmation. No numerical parameters, Pine bytes, original strategy orders, fee assumptions or reproducible returns are claimed.

### Independently reproduced

**None.** No Hummingbot/Qlib backtest, event-level parity, real fills, performance figures or live economics reproduced. Pinned Hummingbot source **compatibility inspection** is not a strategy backtest.

### Negative evidence

Original Pine/version and numerical defaults not retrieved; original signal/exit events not known; exact package wheel not rehashed; no dedicated controller; no exchange precision, actual fee, spread/slippage, partial-fill or production cash enforcement; no Qlib/Hummingbot event-level parity. All unverified source details are explicitly replaced by researcher-authored derivative rules, not silently attributed to the author.

## Falsification plan

After separate approved strategy-specific materialization, replay representative closed-candle sequences through pinned Hummingbot and Qlib with identical data, fees and modeled same-close semantics. Compare each POS/NEG/Bull/G transition, BUY/SELL timestamp at E[t], side, price, size, fee, inventory and cash. Resolve event-level divergences before mass Qlib screening. Then compare the frozen derived hypothesis with a KAMA-delta sign-only control under identical costs and sample; poor net expectancy or unstable cross-window behavior rejects the economic hypothesis, **not** the six-gate admission.

## Crypto portability

Only BTC-USDT Binance spot UTC 1d is claimed for this immutable derived version. Other pairs, frames, perpetuals, DCA overlays, real protective orders and leverage change execution/economic assumptions and require explicit separate capability validation; the optional downstream campaign is not an HB_READY entry gate.

## Limitations

This is a TradingView-inspired **independent derivative**, not source-native Pine. The public page describes an indicator rather than complete executable trade rules. Same-completed-close market fills are historical simulator bookkeeping, not attainable guaranteed real executions. A negative delta/regime exit is not a protective stop; severe gaps may exceed any expected loss. Fee/slippage/precision economics are incomplete for trading; no backtest or profit claim exists.

## Implementation status

**not-implemented**: research specification only. A future selected candidate needs a minimal dedicated controller/executable recipe and representative event-level engine parity before screening on an unverified path. No new admission registry, generic compiler or workflow is introduced.

## Adoption boundary

**research-only / not-approved / research-only approval scope**. Independent Hermes Auditor GitHub Webhook Review alone may verify exact-head six-gate PASS and merge; a failure must not be promoted. The existing signed webhook receiver alone owns post-merge README count bookkeeping. No trading, backtest, deployment or other repo modifications are authorized by this record.

## Related Wiki records

None created or changed. Distinct from main KAMA21 price/average state and KAMA40 slope-flip/percentage-bracket records.

## Sources

- Primary: https://www.tradingview.com/script/kCL9GRtN-Ultra-Pulse-KAMA/
- Pinned engine source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Admission contract: https://github.com/HCH725/alpha-strategy-research/blob/e287ed4d893e5bdbc6b5b53ec2aaba059bc5510c/.github/HB_READY_REVIEW.md
