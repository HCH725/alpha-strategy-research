---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Uncle Sam ADX10-gated CCI15 +100 recross above HMA200, derived BTC-USDT 1d long-flat"
created: 2026-10-25
updated: 2026-10-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-25
sources:
  - https://www.tradingview.com/script/TIh5nqlf-ADX-CCI-MA-Uncle-Sam/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Uncle Sam ADX10 / CCI15 / HMA200 trend-confirmed +100 recross — independently specified long-flat derivative

## Provenance

**Directly inspected primary source:** UncleSamTrading, "ADX + CCI + MA - Uncle Sam", public TradingView open-source strategy page published **2024-07-01**, stable script ID **TIh5nqlf**, read 2026-10-25: https://www.tradingview.com/script/TIh5nqlf-ADX-CCI-MA-Uncle-Sam/ . The public description, rather than a complete recovered Pine code listing, is the source of verified source-native facts here. No Pine version or immutable source-code hash is claimed. The immutable *derived specification* is frozen below and does not float with later page edits.

**Source-native facts from the author's page:** Long entry requires ADX above threshold (default 20), CCI crossing above +100, and price above an optional MA filter. Short entry requires CCI crossing below -100, ADX above threshold and price below the MA. Defaults stated: CCI period 15; ADX length 10; MA type HMA; MA length 200; MA source close. The page describes percentage stop-loss 1% and take-profit 5%, and an optional two-candle MA-based early exit. It does not establish all Pine fill/stop priority, position-state, ADX seeding, MA toggle default, precise intrabar fills, fees, or original backtest reproducibility. The prose's placeholder backtest-market/timeframe is not evidence of an actual market test. No performance statistic is adopted.

**Explicitly independent derived strategy, NOT a lossless reproduction:** The researcher fixes the MA filter ON, selects LONG/FLAT only on Binance BTC-USDT spot 1d, specifies exact Wilder ADX / CCI / HMA calculations and warmup, replaces the author's protective stop/limit semantics with **completed-close threshold exits** at -1% / +5%, disables the optional MA early exit, fixes position size/cash and no DCA, adopts a same-close MARKET *research simulator* fill convention and disclosed fixed research fee. These choices can change trade events, exits and economic outcomes. They are not attributed to the author or passed off as source-native. This derived strategy has no stop order that protects against intrabar gaps. It does not claim to reproduce TradingView results.

**Immutable identity:** TradingView:TIh5nqlf / UncleSamTrading / public description 2024-07-01 / derived-spec-v1-20261025 / ADX(10) Wilder >20 AND CCI(15,hlc3) crosses +100 AND close > HMA(200,close) / BTC-USDT Binance spot 1d / LONG-FLAT / close-evaluated -1%/+5% exit / 0.001 BTC fixed / no DCA / MARKET close-fill research model. A different smoothing, exit timing, market, side, threshold or MA toggle constitutes a different strategy identity.

**Dedup at main dc3b0093716d93bf1051abab24be112c3b0d06e6:** Exact TradingView script ID TIh5nqlf and UncleSamTrading returned no current-main code-search match or open PR match; all ten open research/* PRs were checked by title/body and none cited this script or its exact combined rule. Nearest main families were inspected: cci-ema-rsi-cross-trailing-stop (CCI gate + dual RSI cross + EMA + trailing stop), cci-threshold-extreme-reversal (CCI extreme-zone reversals without ADX/HMA), forven-adx-trend-di-cross (ADX plus directional-index cross without CCI/HMA), and freqtrade-strategy004-adx-cci-dual-stoch-recross (CCI < -100 washout + dual Stochastic recross, not +100 momentum cross above HMA). This source and its three-way HMA/ADX/CCI +100 entry with close-threshold exits are materially different, not a trivial parameter variant.

## Economic mechanism

The source combines strong trend (ADX), positive CCI momentum threshold recross and MA price regime. The derivative tests whether positive CCI acceleration while price is above a slow Hull average leads to a bounded close-observed exit. No positive expectancy or robustness claim follows from this hypothesis.

## Signal — frozen derived arithmetic

**Input:** A contiguous series of completed, finite, positive Binance BTC-USDT spot UTC daily OHLCV bars indexed t=0,1,..., with high >= max(open,close), low <= min(open,close), volume >= 0, and strictly consecutive 86400-second UTC open-time stamps. Reject a malformed/missing/duplicate/partial row before computing signals. No adjusted future prices, non-OHLCV features or fitted model.

**HMA(200) of close:** Define WMA_n(X)[t] = sum(j*X[t-n+j], j=1..n) / (n(n+1)/2), oldest weight 1, newest weight n. Define D[t] = 2*WMA_100(close)[t] - WMA_200(close)[t]. Define HMA200[t] = WMA_14(D)[t], using integer half length 100 and floor(sqrt(200)) = 14. Undefined until enough prefix bars exist; do not fill with zeros.

**CCI(15):** Typical price P[t] = (high[t]+low[t]+close[t])/3. M[t] = mean(P[t-14..t]); MAD[t] = mean(abs(P[k]-M[t]) for k=t-14..t). CCI[t] = (P[t]-M[t])/(0.015*MAD[t]); if MAD is exactly zero, set CCI=0 (declared derived tie rule). Compare unrounded values; no indicator lag or future index.

**Wilder ADX(10), fixed seed:** For t>=1, up = high[t]-high[t-1], down = low[t-1]-low[t]; +DM=up iff up>down and up>0 else 0; -DM=down iff down>up and down>0 else 0. TR=max(high-low, abs(high-prev_close), abs(low-prev_close)). Seed Wilder RMA10(TR,+DM,-DM) at t=10 with the arithmetic mean of values at t=1..10; thereafter RMA[t]=(9*RMA[t-1]+value[t])/10. +DI=100*RMA(+DM)/RMA(TR), -DI likewise; if TR denominator is zero, both DI=0. DX=100*abs(+DI-(-DI))/(+DI+(-DI)), or 0 if denominator zero. Seed ADX at t=19 as the arithmetic mean of DX[t=10..19]; thereafter ADX[t]=(9*ADX[t-1]+DX[t])/10. Do not use a library's alternate EWM initialization without reproducing these exact values. ADX is a magnitude filter, not a directional sign.

**Entry edge on completed bar t:** CCI[t-1] <= 100 AND CCI[t] > 100 AND ADX[t] > 20 AND close[t] > HMA200[t]. Strict >20, >100, >HMA; exact equalities do not pass. No entry merely because CCI remains above +100; a new upward crossing is necessary. Only when FLAT and warmup complete.

**Exit while LONG:** Evaluate from the bar after the actual filled BUY onward: close[t] <= filled_entry_price * 0.99 OR close[t] >= filled_entry_price * 1.05. Exit exactly the filled 0.001 BTC at the modeled completed close. Both thresholds use the filled gross entry price, not cost-adjusted breakeven, HMA, ATR or prior-bar extremes. A single close cannot meet both thresholds for positive entry price. No CCI/ADX/HMA/opposite-signal exit, trailing, timed liquidation, stop/limit order, intrabar touch or optional MA early exit. This is an explicitly **derived close-threshold exit**, not the author's original 1% stop / 5% take-profit order behavior.

**Warmup/state:** Require 240 completed daily bars before any order; first eligible decision t=240 (241st bar). At least HMA200 and ADX10/CCI15 plus prior CCI are available. Seed all indicator recursions from prefix only. The first eligible bar may enter only on an actual t-1-to-t crossing. No forced terminal exit; a remaining long is marked at final observed close separately.

## Direction, position, risk, execution precedence

- Binance BTC-USDT **spot**, one market, one 1d frame; LONG or FLAT only. No short, futures, leverage, funding exposure, borrow, shared-capital multi-asset portfolio or hedge.
- Initial model cash 10,000 USDT. Fixed BUY quantity 0.001 BTC, one position maximum; SELL exactly filled inventory. No pyramiding, BO/SO safety orders, DCA, partial take-profit, compounding, dynamic quantity, multiple concurrent positions or same-bar reversal.
- Controller state FLAT / BUY_PENDING / LONG / SELL_PENDING; maintain filled unit, gross fill price, quote cash and complete event ledger. At most one action per bar. Evaluate a LONG exit before any entry; an exit bar cannot re-enter. While LONG ignore entry crosses. A new entry requires a fresh CCI cross after becoming FLAT. Cooldown=0 *full* intervening bars, but never re-enter on the exit bar.
- BUY only if quote cash covers 0.001*observed close*(1+0.001), and valid fill/cost data exist. SELL only if 0.001 BTC inventory actually filled. Reject/skip an unaffordable or failed order without phantom cash/position; do not replay a skipped crossing later without a fresh edge. No borrowing or negative spot inventory. Reconcile actual simulator fill event before updating controller state; never assume an action request equals a fill.
- Exit threshold risk is evaluated only once at completed close and is **not an exchange-side stop**, so loss may exceed 1% during gaps or between bars. No guaranteed fill, live risk protection or real-time performance claim. No terminal forced liquidation.

## Pinned Hummingbot execution/data model — Gate 5 evidence

**Fixed baseline:** package label 20260920, VERSION dev-2.17.0, HCH725/hummingbot commit **8b0e067e80ab62f10846d518dcb5a8218527ddb3**. GitHub connector reads this cycle verified the exact commit, hummingbot/VERSION, Binance spot candle constants/parser, BacktestingEngineBase, OrderExecutorSimulator and OrderExecutorConfig at that commit. The separately accepted Alpha PR #414 records prior independent 902/902 package-wheel/source byte identity and a representative primitive check; **wheel bytes and event assertions were not re-run here**. The label/version alone would not prove binary identity.

- **Data:** hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py declares 1d support; binance_spot_candles.py maps BTC-USDT to BTCUSDT and parses REST kline open timestamp plus OHLCV. Require raw gap/finite/complete-bar checks before feature preparation; a supported interval name does not establish raw data integrity.
- **Controller/executor:** hummingbot/strategy_v2/backtesting/backtesting_engine_base.py simulate_execution() iterates prepared rows, updates controller state, obtains controller.determine_executor_actions() and sends CreateExecutorAction into simulate_executor(). hummingbot/strategy_v2/executors/order_executor/data_types.py declares OrderExecutorConfig with connector_name=binance, trading_pair=BTC-USDT, side=BUY/SELL, amount=Decimal("0.001"), execution_strategy=MARKET, leverage=1 and price=None. A dedicated controller for these indicator and cash-state rules remains **not implemented**.
- **Fill semantics:** hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py MARKET branch selects the first supplied candle's timestamp, prices the fill at that candle's close, sets filled_amount_quote=amount*close and cum_fees_quote=trade_cost*notional, then terminates as POSITION_HOLD. This is a specific *simulator* path, not proof of real post-close execution or support for arbitrary next-open/maker/intrabar orders. On absent candle/price, fail closed; do not substitute synthetic prices.
- **Position/economics:** BacktestPositionHold._process_order() nets BUY and SELL units, computes gross realized PnL against actual recorded average entry, and add_executor() accumulates cum_fees_quote on both sides. Research fee pin trade_cost=0.001 (0.1% of filled quote notional **per side**) is an explicit assumption, **not** an observed Binance rate and **not** the source's unstated fee. Quote cash debits gross BUY notional+fee, credits gross SELL notional-fee. Net realized quote PnL = gross realized PnL minus accumulated two-side fees; avoid treating gross ledger PnL as fee-net. Spot funding is **not applicable**, not an invented perpetual zero funding observation.
- **Timestamp:** Binance kline T[t] is the bar **open** timestamp. Decision is available only at E[t]=T[t]+86400 seconds UTC after the completed daily bar; record E[t] as effective model decision and close-fill event time despite the simulator's open-stamped row. Same-close fill at E[t] is a backtest convention that cannot be guaranteed live. No unverified spread, impact, latency, precision, min-notional, partial-fill or exchange rejection behavior is silently asserted. No real trading or testnet use is authorized.
- **Capability boundary:** The pinned one-pair daily Binance spot OHLCV + MARKET-close simulator + POSITION_HOLD gross/fee netting path is evidenced; multi-asset synchronization, futures funding/margin, live close execution, intrabar TP/SL and actual exchange economics are **not** claimed. The derived exit avoids unsupported intrabar TP/SL entirely and evaluates only close-observed predicates.

## Six-gate proposal — independent Hermes Auditor decision required

1. **Deterministic:** Exact Wilder ADX10 seeds, CCI15 HLC3/MAD tie, HMA200 weighted sums, +100 edge, ADX/HMA comparisons and threshold exits are frozen; no hidden model or parameter fit.
2. **Direction:** Binance spot LONG/FLAT, shorts expressly disabled; author originally describes both directions.
3. **Complete orders/risk:** Three-way entry and -1%/+5% completed-close exit, exit-first priority, disabled optional MA exit, no intrabar stop/limit/TP/trailing/timed exit.
4. **State:** 0.001 BTC, 10,000 USDT, one position, no DCA/pyramiding/concurrency, exact cash/fill reconciliation, no same-bar reentry, skip/failure rules.
5. **Pinned engine:** Specific pinned Binance 1d OHLCV, CreateExecutorAction, MARKET OrderExecutor close-fill, POSITION_HOLD netting, both-side modeled fees and effective close timestamp, with explicit economic limitations; prior accepted package mapping referenced, not re-proven.
6. **Causality:** 240 completed bars warmup, prefix-only smoothing, strict UTC open+86400 availability, fail-closed missing rows and no future/repainting/unfinished HTF data.

Frontmatter PASS is **the Scout's proposed eligibility**, not independent approval. Hermes Auditor must verify source facts, exact pinned-engine applicability and all six gates at this immutable PR head before any merge. If a gate fails, the PR must not enter PASS-only main.

## Evidence

**Source-reported:** UncleSamTrading TradingView page, published 2024-07-01, provides ADX/CCI/MA concept, listed default lengths/types and 1%/5% risk thresholds. No source-native backtest, source Pine hash, or original intrabar fill reconstruction is claimed.

**Independently reproduced this cycle:** None. Static primary-page inspection and GitHub-pinned Hummingbot code-path inspection only; no Hummingbot/Qlib run, TradingView reproduction, event parity test, performance metric, fee observation, Paper/Testnet/Live order or deployment. Prior PR #414 engine primitive evidence is historical.

**Limitations/falsification:** If original Pine uses materially different entry/MA/risk rules, this remains a distinct declared derivative, never a lossless reproduction. If the specified Hummingbot commit/package cannot actually produce the declared daily close-fill + position/cash ledger under a dedicated controller, Gate 5 fails and the PR must not merge. An exchange-side 1% stop/5% limit strategy is not equivalent to this completed-close model. One representative Qlib/Hummingbot event-level parity validation of any newly unverified implementation/execution primitive is required **before** mass Qlib screening; not performed here.

## Implementation and adoption

Research record only. Dedicated controller, executable Qlib recipe and trading deployment: **not implemented**. Adoption: **not approved**. Approval scope: **research-only**. No new admission registry, execution workflow, strategy code or pipeline artifact is created.

## References

- TradingView primary source: https://www.tradingview.com/script/TIh5nqlf-ADX-CCI-MA-Uncle-Sam/ (UncleSamTrading; published 2024-07-01; inspected 2026-10-25).
- Pinned engine commit: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Earlier independent package/primitive evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
