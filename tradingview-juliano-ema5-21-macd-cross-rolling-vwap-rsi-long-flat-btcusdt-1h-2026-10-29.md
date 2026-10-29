---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Juliano EMA5/21 and MACD synchronous cross gated by rolling VWAP20 and RSI14, BTCUSDT 1h long-flat (independent derivative)
created: 2026-10-29
updated: 2026-10-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-05-27
sources:
  - https://www.tradingview.com/script/msAmBMBT/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Juliano EMA5/21 + MACD synchronous cross with rolling VWAP20 and RSI14

## Provenance

- **TradingView primary source:** JulianoEinhardt (Juliano Einhardt Ulguim), *EMA5/21 + VWAP + MACD Histogram*, public **open-source indicator**, published **2025-05-27**, stable script ID `msAmBMBT`: https://www.tradingview.com/script/msAmBMBT/ . First-party public description read 2026-10-29. A frozen Pine source revision and full Pine bytes are **not** exposed by the retrieved page; no claim of exact Pine event parity.
- **Source-reported decision rules:** EMA5 crosses above EMA21, close above VWAP, MACD(12,26,9) crosses above signal, RSI14 >40 for bullish signal; inverse EMA/MACD crosses, close below VWAP and RSI14 <60 for bearish signal. Long exit when EMA5 crosses below EMA21 **OR** MACD crosses below its signal; analogous inverse for shorts. The source is an indicator with signals, not an independently verified executable TradingView strategy. Do not attribute execution semantics, VWAP reset, indicator seed, risk controls or performance to the author.
- **Immutable derivative identity:** `TV-msAmBMBT-Juliano-EMA5x21-MACD12x26x9-synchronous-cross-RVWAP20-RSI14gt40-BTCUSDT-spot-1h-long-flat-v1-20261029`. The source identity is the stable TradingView script ID and 2025-05-27 publication; this separately specified derivative version is frozen by this record and its eventual PR commit, **not** by a nonexistent Pine revision hash.
- **Researcher-defined alterations, all event-changing where applicable:** (1) replace unspecified session/anchored VWAP with explicitly **rolling 20 completed 1h bars** of close-volume VWAP; (2) trade only source's bullish four-way conjunction, with short disabled; (3) require the two crossovers to occur on the **same completed candle** and both price/VWAP and RSI filters at that close, not a multi-bar memory; (4) use source-described OR long exit but no other stop/target; (5) fix all indicator seeds, zero-denominator handling and warmup; (6) choose Binance BTC-USDT spot 1h, fixed 0.001 BTC, no DCA, one-bar delayed idealized close fill and an explicit hypothetical fee/ledger. These are research decisions, **not** source-native Pine behavior. No source-reported backtest or original-order equivalence is claimed.
- **Dedup, checked on main SHA `efecb9b0c9fdccf395b6fca3908131bcaeecc842` and 11 open research PRs on 2026-10-29:** exact script ID `msAmBMBT`, author `JulianoEinhardt` and `EMA5/21` returned no main code-search matches; open PRs contain no matching source. The nearest generic EMA, MACD, VWAP and RSI families differ materially: this derivative requires **simultaneous EMA5/21 and MACD12/26/9 bullish CROSS EDGES**, plus rolling volume-weighted price permission and RSI14 >40, not a level-only EMA trend, MACD histogram turn, standalone VWAP reclaim or generic multi-indicator state.

## Economic mechanism

### Source-reported

The author presents the EMA5/21 trend transition and MACD signal crossover as momentum confirmation, with price relative to VWAP and RSI14 as filters. It is a proposed signal-confluence indicator, not evidence of an investable edge.

### Research interpretation

The derivative only buys a **synchronous transition** in short-horizon trend and MACD momentum when the latest close is above a causal volume-weighted reference and RSI is not weak. The strict simultaneous-edge requirement may yield very few trades and is a falsifiable research hypothesis, not an optimized profitability claim. Longs exit on the first opposing EMA or MACD edge. Absence of a protective stop creates potentially unbounded percentage drawdown down to the asset's zero bound.

## Signal

Only continuous, chronologically ordered **completed Binance BTCUSDT spot 1h OHLCV** bars, zero-based index `t`. IEEE float64 indicator calculations in fixed order; all comparisons strict where shown. No fitting, ML, future data or repainting.

1. `EMA_n` for `n=5,21,12,26`: first defined at `t=n-1` as arithmetic mean of `close[0..n-1]`; thereafter `EMA_n[t] = (2/(n+1))*close[t] + (1-2/(n+1))*EMA_n[t-1]`. Missing prior values are invalid, never zero-filled.
2. `macd[t]=EMA12[t]-EMA26[t]` for `t>=25`; `macd_signal[33]=mean(macd[25..33])`; then `macd_signal[t]=(2/10)*macd[t]+(8/10)*macd_signal[t-1]`. No MACD cross before `t=34`.
3. `RSI14`: for `i>=1`, `delta[i]=close[i]-close[i-1]`, `gain=max(delta,0)`, `loss=max(-delta,0)`. Seed Wilder averages at `t=14` with mean gains/losses over `i=1..14`; thereafter `avgG[t]=(13*avgG[t-1]+gain[t])/14`, same for `avgL`. `RSI=100-100/(1+avgG/avgL)`; when `avgL=0,avgG>0` use 100; `avgG=0,avgL>0` use 0; both zero use 50. RSI undefined before 14.
4. **Researcher rolling VWAP20**, not the source's unspecified VWAP: `rvwap20[t]=sum(close[i]*volume[i],i=t-19..t)/sum(volume[i],i=t-19..t)`. Require 20 valid bars and strictly positive summed volume; a zero denominator makes this bar ineligible (no forward-fill, no invented reference).
5. `crossup(a,b,t) = a[t-1] <= b[t-1] AND a[t] > b[t]`; `crossdown(a,b,t) = a[t-1] >= b[t-1] AND a[t] < b[t]`. Valid values required on both bars. Equality is allowed only on the previous bar; current equality is **not** a cross.
6. `BUY[t] = crossup(EMA5,EMA21,t) AND crossup(macd,macd_signal,t) AND close[t] > rvwap20[t] AND RSI14[t] > 40`.
7. `SELL[t] = crossdown(EMA5,EMA21,t) OR crossdown(macd,macd_signal,t)`. This is the source-described **OR** long-exit relationship; VWAP and RSI do not gate exits. Short signals/short entries are disabled, not silently inverted into an exit.
8. State priority: while FLAT and without a pending action, evaluate BUY only; while LONG and without pending action, evaluate SELL only. No simultaneous BUY/SELL is possible because the same pair cannot cross up and down on one bar. No repeated level-based entry after a missed synchronous edge. On a fill bar, suppress fresh signal evaluation to avoid lookahead/instant re-entry. After confirmed SELL fill, FLAT; the next eligible fresh synchronous BUY edge may re-enter, with **zero extra cooldown**.

There is **no** fixed stop-loss, take-profit, trailing stop, time exit, forced end-of-sample liquidation, risk-parity, discretionary override or source-native order default. No DCA, safety orders, partial exits, pyramiding, averaging, hedging, short, futures, leverage, margin, funding or external portfolio dependence. The only position exit is SELL above.

## Required data

- Binance spot `BTC-USDT`, `1h` **real** historical OHLCV: timestamp is candle **open** `T[t]`; signal inputs become available at `E[t]=T[t]+3600 seconds`, after that bar completes. A missing or incomplete final candle is excluded.
- Validate strictly increasing `T[t+1]-T[t]=3600`, no duplicate/missing rows, finite positive OHLC prices, `high>=max(open,close)`, `low<=min(open,close)`, nonnegative finite volume, finite indicator outputs. Any missing or invalid price/volume aborts that contiguous research segment; do not silently fill or manufacture candles.
- **Warmup:** 100 completed bars, indices `0..99`; no decisions/orders until `t=100`. MACD signal, both EMA crosses, RSI and rolling VWAP plus their previous-bar values are then fully defined. No `request.security`, higher/lower-frame alignment, forward shift, future extrema or full-sample normalization.

## Execution assumptions

**PINNED Hummingbot evidence read via connected GitHub app 2026-10-29:** `HCH725/hummingbot` commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3`, `hummingbot/VERSION=dev-2.17.0`, repository's admitted package label `20260920`. Relevant inspected paths at that immutable commit:

- `hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py` plus `constants.py`: `/api/v3/klines`, `1h` interval, timestamp from kline open and OHLCV fields. No book, trades, higher-timeframe or external inputs required.
- `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py`: historical candles provided by `get_candles_df`, `get_price_by_type` has dangerous `Decimal("1")` fallback when price missing: **never rely on this fallback**, validate real positive close before executor dispatch and abort on missing close.
- `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py`: `prepare_market_data` preserves real open/high/low/close/volume columns; `simulate_execution` calls `update_state(row)`, then `controller.determine_executor_actions()`, then dispatches `CreateExecutorAction`; `BacktestPositionHold` tracks `POSITION_HOLD` fills. A future **minimal strategy-specific** controller, not present or claimed implemented here, must materialize the deterministic indicators and the FLAT/LONG/PENDING state. No engine changes are authorized by this record.
- `hummingbot/strategy_v2/executors/order_executor/data_types.py`: `OrderExecutorConfig` accepts `connector_name="binance"`, `trading_pair="BTC-USDT"`, `side=BUY/SELL`, `amount=Decimal("0.001")`, `position_action=OPEN/CLOSE`, `execution_strategy=MARKET`, `price=None`, `leverage=1`.
- `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`: MARKET fills at **first supplied candle's real close**; filled quote `float(amount)*entry_price`, fee quote `trade_cost*filled_quote`; returns `CloseType.POSITION_HOLD`. This is the **actual pinned historical simulation**, not a claim of executable post-close live market orders, actual exchange fill, spread, slippage or funding model.

**Exact event timing:** at decision availability `E[t]`, queue action, do **not** submit on candle `t`. At next candle `t+1` (whose open timestamp equals `E[t]`), dispatch exactly one MARKET executor to the backtesting engine's row `t+1`, resulting in its modeled close price `close[t+1]` (available at `E[t+1]`). No fill at `close[t]` and no claimed next-open fill. The model is deliberately a **one-completed-bar delayed idealized close fill**. It is a simulation convention, not a live execution guarantee; this delayed-close model is part of this derivative's immutable identity. The pending action on the final bar is **not filled**; no fabricated `t+1`. On `t+1` suppress fresh signal decisions, resume on `t+2`. Fail closed on failed/partial/contradictory fills.

**State and accounting:** initial `10000 USDT` cash and zero BTC; one spot long `Q=Decimal("0.001") BTC` or FLAT, one pending action maximum. BUY consumes `Q*P*(1+f)`, SELL credits `Q*P*(1-f)`; ledger BTC changes by exactly `Q`. Fixed hypothetical fee `f=Decimal("0.001")` = 0.1% of quote notional per side, passed as `trade_cost=0.001` to the engine. This is a **declared research fee**, not a verified Binance tier; zero *additional* modeled slippage is an idealization, **not** observed zero slippage. Spot funding is **not applicable**; no statement about perpetual funding. No maker, bracket, intrabar or margin executor is required.

Because the simulator computes quote fills with binary floats and `BacktestPositionHold` can retain tiny base dust, retain a separate Decimal cash/BTC ledger keyed by confirmed executor fills; reconcile base within `1e-12 BTC`, quote/fee within `1e-8 USDT`, and abort on larger discrepancy. These are research diagnostic tolerances, not exchange precision rules. The simulator does not prove tick/lot/min-notional exchange acceptance or actual liquidity. Cash must cover modeled cost; no negative balance or synthetic fill. Retain complete terminated-executor history; do not treat a `POSITION_HOLD` executor as a completed round trip. End-of-sample open long is marked to last real close, with no fabricated liquidation trade.

## Evidence

### Source-reported

Direct first-party TradingView page (2025-05-27) states EMA5/21 cross, MACD(12,26,9) signal cross, price vs VWAP and RSI14 threshold 40/60 for bullish/bearish signals, with EMA **OR** MACD opposing crossover for exits. It does not expose full Pine code, immutable version, executable order settings, VWAP anchor/reset, fees or backtest statistics. Source description is not claimed to establish any of those.

### Independently reproduced

**Not independently reproduced.** No candidate-specific Qlib or Hummingbot run, no historical returns, no fill trace and no event-level parity. The pinned engine's **existing single-spot-candle MARKET/POSITION_HOLD code path** was inspected as bounded compatibility evidence, not as an executed strategy or an implementation artifact. Reuse of that primitive does not assert parity.

### Negative evidence

- This is **not** the source-native indicator or a faithful Pine port: rolling VWAP20, long-only state, exact simultaneous-edge interpretation, explicit initialization, fixed quantity, fee and delayed fill are deliberate researcher choices.
- The source does not provide a measured edge; no trade count, win rate, ROI, Sharpe, MDD, survivor or backtest statistic is claimed.
- A double same-bar cross can be rare; no forced alternative trigger window, lookback latch or threshold adjustment is allowed under this identity.
- Real exchange costs, fill feasibility, liquidity, spread, tick/lot precision, partial fills and funding for futures are not established. Missing prices must fail, never use the provider's 1-USDT fallback.
- A long may remain exposed indefinitely without a stop; this is not a protected trading system.
- No Qlib implementation/parity, Hummingbot controller deployment, Paper/Testnet/Live or adoption permission.

## Falsification plan

When a separate downstream research decision authorizes implementation, build only the minimal strategy-specific controller and deterministic replay. On a continuous 1h fixture verify seed indices, RSI 0/0, zero-volume VWAP guard, exact EMA/MACD simultaneous crosses, equality boundaries, exit OR precedence, delayed fill and pending-final-bar cancellation. Reconcile executor timestamps, close prices, fees and Decimal inventory event-by-event against a separate causal reference ledger. Test absent/malformed candles and floating residuals fail closed. Only after representative Qlib↔Hummingbot **event-level parity** for this execution path may large-scale Qlib screening use it. Test performance and OOS separately; neither is an admission gate.

## Crypto portability

The research derivative is **BTCUSDT spot 1h** only by declaration, not because HB_READY forbids other symbols/frames. Porting to a different coin, frame, exchange, leverage or DCA overlay requires an explicit separate derived experiment and relevant engine/economics verification; no implicit futures or shared-capital portability.

## Limitations

TradingView source's full Pine revision was not accessible, so only the published decision-critical textual facts are attributed to the author. The rolling VWAP20 is deliberately **not** an assertion about the original VWAP. The strict synchronous-cross model, unprotected exit-only risk, idealized next-close fills and fixed fee materially affect results. This record is an auditable hypothesis, not an already profitable, executable, approved or certified strategy.

## Implementation status

`not-implemented`. HB_READY PASS is a claim of **bounded pinned-engine model expressibility**, subject to independent Hermes Auditor verification; it does not mean a strategy-specific controller or Qlib executable exists. Any later implementation must follow the existing GitHub PR/review process and preserve this immutable version.

## Adoption boundary

`status: research-only`; `adoption: not-approved`; `approval_scope: research-only`. No backtest was run and no Paper/Testnet/Live trading, production deployment or capital allocation is approved. Independent Auditor owns exact-head six-gate PASS decision and any merge; Scout cannot self-approve.

## Related Wiki records

None linked. Do not infer Wiki or Survivor status from this HB_READY research proposal.

## Sources

- TradingView first-party publication: https://www.tradingview.com/script/msAmBMBT/ (JulianoEinhardt, 2025-05-27).
- Pinned Hummingbot source evidence: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting
- Pinned Binance Spot feed: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py
