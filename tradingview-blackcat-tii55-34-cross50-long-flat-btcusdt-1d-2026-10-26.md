---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "blackcat1402 TII 55/34 fixed-reference intensity cross-50 BTC-USDT spot 1d long-flat — independently derived"
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
source_as_of: 2025-04-19
sources:
  - https://www.tradingview.com/script/sFlOY8ZD-blackcat-L1-M-H-Pee-Trend-Intensity-Index-TII/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# blackcat1402 TII55/34 fixed-reference intensity cross-50 — independently derived BTC-USDT spot 1d long-flat

## Provenance

**Primary source and stable identity.** blackcat1402, *[blackcat] L1 M.H. Pee Trend Intensity Index (TII)*, TradingView stable script ID **sFlOY8ZD**, first published **2021-09-08**, updated **2025-04-19**; public open-source indicator: https://www.tradingview.com/script/sFlOY8ZD-blackcat-L1-M-H-Pee-Trend-Intensity-Index-TII/ . The first-party readable description was inspected **2026-10-26**. It describes a 55-bar SMA reference, deviations of 34 previous/current price observations from today's average, positive/negative deviation aggregation and TII = 100 × sum(positive deviations) / sum(absolute deviations). It also mentions ALMA and HMA noise filtering and an April 2025 release with a three-bar comparison line and buy/sell labels. The accessible page does not expose the actual complete Pine source revision, exact ALMA/HMA settings, label booleans, executable order defaults or source-code hash. No source-native, lossless-Pine or native backtest-equivalence claim is made.

**Independently specified derivative, NOT the published script's trading system.** This research defines a particular *unsmoothed, fixed-current-reference TII* using source-described 55/34 windows, plus researcher-chosen **50 cross-up LONG / level-at-or-below-50 FLAT** triggers, single BTC-USDT spot UTC 1d feed, fixed 0.001 BTC, completed-candle-close historical MARKET fills, explicit research costs, cash checks and order-confirmed state. The original ALMA/HMA filtering, three-bar comparator, labels and alert conditions are intentionally **not** reproduced; their omission changes signals. The TradingView page is an **indicator**, not evidence for these derivative entries/exits, fees, size, market or risk rules. Those are researcher decisions, not source facts. No Pine defaults are invented or attributed to the author.

**Frozen research identity:** TradingView:sFlOY8ZD:blackcat1402:2021-09-08:update-2025-04-19 | independent-derived-v1 | fixed-reference-TII: SMA(close,55)[t], deviations(close[t-33..t], SMA55[t]), zero-denominator-neutral-50 | entry-cross-up-50 | exit-level-le-50 | BinanceSpot:BTC-USDT:UTC-1d:LONG-FLAT:0.001BTC | completed-close-MARKET:assumed-fee-0.001-per-side | created-2026-10-26. Any change to formula, smoothing, comparator, thresholds, market, timing, fee, quantity or state is a different derivative.

**Dedup snapshot:** Connected GitHub main commit **998c163ba298a0343e4fa38d1e16fcb8918e1e3c**: untruncated recursive tree contains **343** root-level strategy Markdown records; README static count **343**. No filename containing TII/trend-intensity; GitHub default-branch code search for script ID sFlOY8ZD or TII found no exact match; prose search for "Trend Intensity Index" found only an unrelated reference to ADX trend intensity. The 10 open research/* PRs (#48, #49, #63, #89, #92, #251, #304, #331, #350, #353) are other strategies. Exact-source PR search returned no matches; another blackcat1402 script appears in historical PR #233 but is an **Ehlers Decycler**, not TII. The closest "quantifiedtrader-intraday-intensity" record measures **volume-weighted intrabar close location**, not 34 closing-price deviations against one current 55-SMA. This TII mechanism is neither that volume intensity nor a trivial SMA crossover: the 34 deviations can produce different transitions at the same SMA/price crossing. Count equality is not independent six-gate re-audit of all prior records.

## Economic mechanism

### Source-reported

The indicator is intended to measure how strongly recent prices cluster above versus below a current longer-term moving-average reference, with a bounded 0–100 positive-deviation share. Its author uses additional smoothing/filtering not reconstructed here. The first-party page supplies no independently reproduced profits or executable risk/fill model.

### Research interpretation

The **derived** hypothesis is that the balance of the past 34 closing-price deviations relative to today's 55-bar mean changes regime when its positive-magnitude share rises above 50%. It enters on that transition and exits when positive deviation mass no longer exceeds negative deviation mass. It is an unsmoothed breadth-of-deviations trend-intensity regime model, not an ALMA/HMA or three-bar-label clone. Choppy mean crossings and downside without a stop are expected falsifiers.

## Signal

**Data validation and clock.** Use a single Binance BTC-USDT **spot UTC 1d** historical OHLCV series, ascending by unique exchange candle **opening** timestamp T[t]. Valid adjacent daily opens differ by exactly 86,400 seconds. Each row must contain finite actual O/H/L/C > 0, H >= max(O,C), L <= min(O,C), and finite nonnegative volume; no synthetic bars, duplicate/gapped timestamps, interpolation or forward filling. The decision for row t occurs **only at completion time D[t] = T[t] + 86,400 seconds**, never at the raw open timestamp. Candle t must be complete before its close enters any signal. No non-OHLCV or multi-asset inputs.

**Precisely defined independent formula.** For t >= 54, A[t] = (1/55) × sum(C[j], j=t-54..t). The SAME current A[t] is compared with each of the **34** closes C[j] for j=t-33..t (including t): P[t] = sum(max(C[j]-A[t],0)); N[t] = sum(max(A[t]-C[j],0)). Define TII[t] = 100×P[t]/(P[t]+N[t]) when P+N > 0; when all 34 deviations are exactly zero, set TII[t] = 50 (researcher-defined neutral, never an assumed Pine behavior). No ALMA, HMA, other smoothing, three-bar comparator, stochastic, external feature, lookahead, fitted model, rounding, or intrabar trigger. Use full floating precision for indicators and Decimal for order quantity/cash ledger. All comparisons use unrounded TII.

**Warmup:** 90 **consecutive fully completed valid** UTC daily candles; the first decision is on the 90th completed bar, t=89, and requires both TII[t] and TII[t-1]. Start FLAT with 10,000 USDT cash, zero BTC, zero pending orders and no inferred position from pre-warmup signals. A neutral value of exactly 50 does not enter.

**Entry on a completed bar:** EntryCross[t] = TII[t-1] <= 50 AND TII[t] > 50. When confirmed FLAT, no pending order and no exit on this bar, send exactly one BUY for 0.001 BTC at the completed bar's historical close only if available cash >= 0.001×C[t]×(1+0.001). No other entry. A continuous TII>50 level without a new cross cannot re-enter.

**Exit on a completed bar:** When confirmed LONG and no pending order, send exactly one SELL for the confirmed remaining BTC quantity if TII[t] <= 50. This is a **level** exit, not an unverified original Pine crossing; equality exits. No protective stop, fixed target, trailing stop or time exit. Exit takes priority over any entry; same-bar reversal/re-entry is disabled. If the sample ends LONG, mark inventory at the last **actual** observed completed close for reporting only; do not fabricate a closing fill.

**Fill/state machine:** pending BUY is not LONG; pending SELL is not FLAT. Only confirmed full fills from the pinned simulated executor/position ledger change held base quantity and cash. One pending order maximum. A rejected/failed/unfilled BUY clears pending, remains FLAT and may re-enter only on a **new** later cross-up; never retry automatically. A rejected/failed/unfilled SELL leaves LONG and is retried at the **next valid completed bar** irrespective of a recovered TII; no duplicate simultaneous SELL. Successful SELL returns FLAT, with no fixed cooldown but no same-bar re-entry; next BUY needs a fresh future cross-up. For the pinned MARKET historical simulator, full same-row close fills are an idealized model behavior, not evidence that live orders always fill; if a fill cannot be confirmed, retain pending and do not assume it. No partial-fill path is claimed; a partial fill or unsupported precision/lot constraint must hold/abort the research run rather than be treated as full.

**Explicitly disabled:** SHORT, perpetuals, margin, leverage, funding, maker/limit/next-open orders, multiple pairs, shared capital, pyramiding, BO/SO/DCA, position scaling, compounding, dynamic size, cooldown beyond the fresh-cross rule, SL/TP/trailing, intrabar stops, discretionary exit, external alerts, higher/lower timeframe dependencies, hidden controller defaults, and end-of-sample forced liquidation. Zero SL is an intentionally absent protective stop, not a claim of safe risk.

**Data/price failure:** Missing/invalid actual close, broken timestamps, missing fee/cash inputs, or an undefined fill/accounting state makes the run invalid; stop without price fallback or fabricated fill. A true flat-market TII denominator zero is handled solely by the explicit neutral 50 formula, not by fabricating market data.

## Required data

Exactly one Binance spot BTC-USDT UTC 1d candle stream (real open timestamps, actual O/H/L/C/V), 90 completed consecutive valid rows before trading, and the pinned engine's actual fill records. Formula uses closes only; other OHLCV fields are validation inputs. No order book, mark price, external ML/model artifact, multiple timeframe, futures funding, cross-asset synchronization or next-open/intrabar price series.

## Execution assumptions

**Pinned executable-model source inspected via the connected GitHub app, 2026-10-26:** Hummingbot package identifier **20260920**, source **HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3**, repository VERSION **dev-2.17.0** (hummingbot/VERSION read at that immutable commit). Package identifier is the canonical admission contract; the installed wheel/image binary digest was **not** independently matched to the source commit this cycle. Existing independently reviewed engine-path evidence: Alpha PR #414 and #417; this Scout re-read the named pinned source paths rather than treating an API name as sufficient.

**Real bounded engine path and timestamps:** In hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py, Binance spot REST /api/v3/klines supports **1d**. In binance_spot_candles.py, _parse_rest_candles reads row[0] as **open** timestamp and row[1..5] as OHLCV. In hummingbot/strategy_v2/backtesting/backtesting_engine_base.py, run_backtesting initializes connector trading rules, candle feed, controller and a configurable backtesting_resolution; simulate_execution processes rows through update_state → determine_executor_actions → simulate_executor. The intended minimal strategy-specific controller is **not yet implemented**; it must compute the above fixed-reference TII from only completed bars, gate actions on D[t], enforce one pending order and cash, and confirm fills before changing state. This is an expressibility proposal on an inspected engine path, not a claim of a completed controller or tested TradingView replay.

**Order/fill path:** In hummingbot/strategy_v2/executors/order_executor/data_types.py, OrderExecutorConfig supports connector_name="binance", trading_pair="BTC-USDT", side BUY/SELL, amount=Decimal("0.001"), position_action OPEN/CLOSE, execution_strategy=MARKET, price=None, leverage=1. In hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py, MARKET chooses the first supplied historical row, fills at that row's **actual close**, books filled_amount_quote = quantity×close, cum_fees_quote = trade_cost×notional and returns CloseType.POSITION_HOLD. The BacktestPositionHold path in backtesting_engine_base.py matches opposite-side base fills, tracks weighted average cost, gross realized/unrealized PnL and **separate** quote fees. This path does not model a future live exchange order book, spread, slippage, latency, partial fills or precise minimum-notional enforcement.

**Critical causal limitation:** The raw Binance candle row is timestamped at its **OPEN**, although the historical simulator fills at its **CLOSE**. For this independent derivative the economic decision/fill time must be **D[t]**, the completed bar's end; never claim that a trade filled at T[t] with future close knowledge. The pinned engine's same-row-close simulation is a **completed-close historical research convention**, not a real-time executable-at-close guarantee. A future Replay/controller must demonstrate this effective-clock mapping before using the record for new execution capabilities; an implementation that timestamps a close-driven decision at raw T[t] is noncausal and outside this proposal.

**Fee, cash and accounting:** Explicit **research-assumed** trade_cost=0.001 (0.1% of filled quote notional per side) passed to the pinned simulator, not a verified Binance tier or source-reported commission. Start unborrowed cash 10,000 USDT. On confirmed BUY of Q BTC at observed Pbuy, cash decreases Q×Pbuy×1.001; on confirmed SELL at observed Psell, cash increases Q×Psell×0.999. Net round-trip realized quote PnL = Q×(Psell-Pbuy) - 0.001×Q×(Pbuy+Psell). Do not confuse the engine's gross position realized PnL with net-of-fee PnL; separately include all booked fees. Spot perpetual funding is **not applicable**, not hypothetical zero funding. No futures leverage, margin, settlement mark, or liquidation is claimed. Real fees, slippage, lot/precision constraints and exchange execution remain unverified.

**Engine safeguards verified in source:** BacktestingEngineBase defaults terminated_executors_window to 3600 seconds; a 1d state machine must use terminated_executors_window=None or a full persistent confirmed-fill ledger so older fills are not invisible to the controller. The provider's get_price_by_type can default to Decimal("1") for absent prices: **never** accept that fabricated price; abort on missing actual close. prepare_market_data uses dropna: validate consecutive rows **before** the engine so an omitted bar cannot silently compress the 34/55-day windows. The fill ledger and position holds are updated across engine ticks; an order submission is not a fill confirmation.

## Evidence

### Source-reported

TradingView first-party sFlOY8ZD, blackcat1402, published 2021-09-08, updated 2025-04-19: 55-bar average, prior 34 price deviations, ratio of positive deviations to total absolute deviations; ALMA/HMA smoothing and a three-bar comparison/labels are mentioned. No source-reported exact executable derivative rules, stop/target, cost, 0.001 BTC size, BTC market or historical profit reproduction.

### Independently reproduced

**No backtest, signal-by-signal Pine reproduction, PnL, Qlib/Hummingbot event-level parity, fee schedule or live fill reproduced.** Connected GitHub source inspection verified the bounded pinned Binance spot 1d data parser, controller/executor sequencing, MARKET close-fill/fee path, position-hold cost accounting, missing-price fallback and timestamp hazard. The TII derivative formula and state are a fully specified research proposal; neither a source-native equivalence nor actual strategy-specific executable test is asserted.

### Negative evidence

The accessible first-party page does not expose complete Pine revision bytes, exact ALMA/HMA inputs, comparison/label booleans, Pine fill settings or position/risk defaults. The derivative intentionally **does not** claim to replicate those. Its 50 threshold, entry/exit conditions, neutral handling, spot 1d clock, size, fee and no-stop decision are researcher-defined and materially alter potential trade events. The main count 343/343 is static bookkeeping agreement, not a full 343-file frontmatter re-audit. No main/open research PR with the same script ID or fixed-reference TII55/34 cross-50 mechanism was found.

**Six-gate evidence for independent Auditor (PASS proposal, not self-audit):** (1) complete 55/34 fixed-reference formula, neutral denominator, precision, 90-bar warmup and threshold priority; (2) Binance spot LONG/FLAT with SHORT prohibited; (3) explicit cross-up entry, level exit and all disabled risk legs; (4) one confirmed 0.001 BTC position, pending/failure/retry/fresh-cross state, no DCA/concurrency; (5) directly inspected pinned source commit and actual 1d Binance feed, OrderExecutor MARKET close fill, POSITION_HOLD accounting, research fee/cash and explicit unsupported real-economics/clock constraints; (6) 90 completed bars, only past/current closes, D[t] decision clock, no repainting or future candles. Independent reviewer must reject if any required engine capability or causal convention cannot be demonstrated for the declared path.

## Falsification plan

After independent admission and separate selection, verify flat-window TII=50, threshold equality, cross-up vs repeated >50, level exit, failed BUY, failed SELL retry, pending fills, no same-bar re-entry, 55/34 boundary, malformed/missing UTC daily rows, source ALMA/HMA divergence, open-timestamp versus effective completed-close time, fee-inclusive cash/PnL and end-of-sample held inventory. Reuse existing verified engine primitives; perform representative Qlib↔Hummingbot event-level capability validation **only if** the selected execution/data path is new or unverified before mass screening. Profitability, OOS and Hummingbot certification are downstream, not HB_READY criteria.

## Crypto portability

This frozen research identity is BTC-USDT **spot 1d** only. Single pair, 1d, OHLCV and completed-close are **not** blanket admission requirements. Seven-coin 1h/4h/1d, isolated 3×/5× futures and BO/SO 6/6/6 are optional later research experiments. Changing market, leverage, funding, DCA or fill conventions is a separately disclosed derivative, never silently source-native.

## Limitations

No readable complete original Pine revision or hash; no original ALMA/HMA/three-bar signal parity; no verified actual Binance fee, slippage, precision or wheel digest; no implemented controller, backtest, Qlib parity, Survivor claim or trading permission. The absence of a stop can lead to severe losses. Historical same-bar close fills are idealized and must not be represented as live achievable; an open-time decision using the row's close would invalidate causality. The 50 threshold is a testable independent hypothesis, not author-specified.

## Implementation status

**not-implemented.** This PR adds only the research record. No controller, Qlib recipe, data pipeline, test, backtest, environment change, deployment or trading action is created. Later executable materialization, if selected, is a separate engineering step and not a second HB_READY admission flag.

## Adoption boundary

**status: research-only; implementation_status: not-implemented; adoption: not-approved; approval_scope: research-only.** The independent Hermes Auditor GitHub Webhook Review owns source-fact remediation, exact-head PASS merge or NOT_LOSSLESS close. This Scout does not approve, merge, close, modify README or run trading/backtests.

## Related Wiki records

None asserted. No Wiki edit.

## Sources

- Primary TradingView script: https://www.tradingview.com/script/sFlOY8ZD-blackcat-L1-M-H-Pee-Trend-Intensity-Index-TII/
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Pinned Binance spot parser: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py
- Pinned backtesting engine: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/backtesting_engine_base.py
- Pinned MARKET executor simulator: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py
- Existing independent engine audit evidence: https://github.com/HCH725/alpha-strategy-research/pull/414 and https://github.com/HCH725/alpha-strategy-research/pull/417
