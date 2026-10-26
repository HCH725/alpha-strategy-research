---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "RevoTheTrader RSI14 / price-Stochastic(14,3,3) / WMA50 confluence long-flat BTC-USDT 1d — independent derivative"
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
source_as_of: 2025-03-14
sources:
  - https://www.tradingview.com/script/ytN19Shr-RSI-Stochastic-WMA-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# RSI14 + price Stochastic(14,3,3) + WMA50 confluence — independent BTC-USDT spot 1d long-flat derivative

## Provenance

- **Primary source, actually read:** RevoTheTrader, *RSI + Stochastic + WMA Strategy*, TradingView public open-source strategy, published **2025-03-14**, stable ID **ytN19Shr**: https://www.tradingview.com/script/ytN19Shr-RSI-Stochastic-WMA-Strategy/ (first-party publication inspected 2026-10-26).
- **Source-reported logic, not inferred from unavailable Pine bytes:** long setup requires RSI **<30**, stochastic **%K crossing above %D**, and **price above WMA**. The published short setup requires RSI **>70**, **%K crossing below %D**, and **price below WMA**. The description names `strategy.entry("LONG", strategy.long)` and `strategy.entry("SHORT", strategy.short)`; it does not establish the exact Pine inputs, stochastic smoothing, order-fill clock, stop/target, pyramiding, or position/accounting defaults. The full Pine code/version bytes were **not retrieved**; do not claim source-native execution or reproduce an undisclosed source revision.
- **Explicitly independent executable derivative:** This record selects **Wilder RSI14 on close, price-based Stochastic high/low 14 with SMA3 of raw %K and SMA3 of smoothed %K for %D, WMA50 of close**, a BTC-USDT Binance spot 1d market, fixed quantity, completed-close historical MARKET fills and a long/flat state machine. It converts the source's *three-part short entry setup* into **long liquidation only** (no short). Every smoothing, window, clock, market, fee, size, no-DCA, exit mapping and risk/state choice not verifiable from source prose is **researcher-defined**, not silently attributed to RevoTheTrader. It does not claim to reproduce the source's native Pine trades.
- **Immutable research identity:** `TradingView:ytN19Shr:RevoTheTrader:published-2025-03-14 | independent-derived-v1:2026-10-26 | close-WilderRSI14 + price-Stoch14/SMA3/SMA3 + close-WMA50 | LONG if RSI<30 AND K-cross-up-D AND close>WMA | FLAT if RSI>70 AND K-cross-down-D AND close<WMA | Binance:BTC-USDT:spot:UTC-1d | qty-0.001BTC | completed-close-MARKET | cost-0.001-per-side`. A changed indicator variant, entry/exit condition, clock, or economics is another derivative.
- **Dedup at proposal time:** Connected GitHub `main` snapshot `8de9e53362ace3220df15757e8f37b429e31536b` has an untruncated tree of **352** root-level strategy Markdown files; README static count **352**. Exact stable source ID `ytN19Shr` and author `RevoTheTrader` had no main code-search matches. All **10** open `research/*` PR titles/bodies were checked, none contains this URL or the three-part rule. The nearest existing StochRSI zone-cross family uses *stochastic of RSI* rather than this **price stochastic with independent RSI oversold/overbought plus WMA trend filter**; other WMA/RSI records lack this joint three-part entry/exit mechanism. Count equality is not an independent full re-audit of historical PASS labels.

## Economic mechanism

### Source-reported

The author proposes an oversold RSI condition with upward stochastic momentum reversal and a price-above-WMA trend filter for long entries, with a symmetrical overbought/bearish-cross/price-below-WMA short setup. These are publication descriptions, not recovered Pine implementation facts.

### Research interpretation

A triple-gated reversal/trend-confluence hypothesis: price stochastic K/D crossing signals a turn; Wilder RSI must still be below 30 at the *same completed bar*; WMA50 filters to price-above-trend entries. When already long, the complete published bearish triple is interpreted as a **flat exit** instead of opening a short. This may produce rare trades or long holding periods; neither effectiveness nor trade frequency has been reproduced.

## Signal

**One pinned data stream:** Binance BTC-USDT spot 1d candles, UTC daily boundaries; finite OHLC and actual positive close required, no higher/lower timeframe, volume, external model, future extrema or market sessions.

**Deterministic formulas (all researcher-pinned where publication does not expose Pine defaults):**

1. `delta[t] = close[t] - close[t-1]`, `gain=max(delta,0)`, `loss=max(-delta,0)`. Seed average gain/loss with arithmetic means of the first **14** valid deltas; thereafter Wilder recursive mean `avg[t]=(13*avg[t-1]+value[t])/14`. `RSI14=100-100/(1+avgGain/avgLoss)`; when loss=0 and gain>0 use 100, gain=loss=0 use 50, gain=0/loss>0 use 0. No incomplete seed produces a signal.
2. `rawK[t]=100*(close[t]-min(low[t-13..t]))/(max(high[t-13..t])-min(low[t-13..t]))`; if denominator=0, `rawK` is unavailable (no fabricated 50 or forward fill). `K[t]=SMA3(rawK)[t]`, `D[t]=SMA3(K)[t]`. Require every input of both smoothing windows finite.
3. `WMA50[t] = sum_{i=0..49} ((50-i)*close[t-i]) / 1275`, newest bar weight 50; all 50 completed closes required.
4. `cross_up[t]=(K[t-1]<=D[t-1] AND K[t]>D[t])`; `cross_down[t]=(K[t-1]>=D[t-1] AND K[t]<D[t])`. Equality on the prior bar counts; equality on the current bar does not. All predicates require finite current and previous K/D.
5. **Entry only while FLAT:** `RSI14[t]<30 AND cross_up[t] AND close[t]>WMA50[t]`. **Exit only while LONG:** `RSI14[t]>70 AND cross_down[t] AND close[t]<WMA50[t]`. All three predicates are evaluated on the **same** completed bar; no remembered partial signals, OR substitution or price-only exit. A long exit takes priority over any entry evaluation; RSI <30 and >70 are mutually exclusive anyway.
6. The first **100 consecutive complete daily candles** are warmup-only and FLAT. Earliest eligible decision is the 101st completed bar, provided all indicators and `t-1` crossings are finite. A missing/duplicate/out-of-order daily candle invalidates continuity: suspend signals and rebuild 100 consecutive complete candles; never compress missing time into adjacent indicator periods.

## Required data

Actual exchange OHLC with an **opening timestamp** and UTC 1d interval from pinned Binance spot candles feed; each candle becomes decision-available **only at its completed close**. No synthetic fills, price interpolation, `security()` lookahead, inferred missing closes, funding, mark price, order book, other pair or non-OHLCV data. Reject nonfinite or nonpositive prices, missing bars and duplicate timestamps.

## Execution assumptions

- **Pinned Hummingbot model directly inspected through connected GitHub app on 2026-10-26:** package `20260920`, `hummingbot/VERSION = dev-2.17.0`, source commit `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. Specific inspected files: `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` (1d), `binance_spot_candles.py::_parse_rest_candles` (row[0] is OPEN timestamp; row[1..5] OHLCV), `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` (controller action loop and position holds), `executors_simulator/order_executor_simulator.py` (MARKET first-row fill at **actual historical close**, `filled_amount_quote=qty*close`, `cum_fees_quote=trade_cost*notional`, `POSITION_HOLD`), `hummingbot/strategy_v2/executors/order_executor/data_types.py`, and `backtesting_data_provider.py`. The earlier independently reviewed Alpha PR **#414** reports **902/902 wheel bytes identical** for the package/source binding, not rehashed this cycle; #417 provides prior bounded primitive review. This proposal does **not** claim a new engine capability.
- **Minimal prospective ControllerV2/backtest controller** (not built or deployed): calculate only complete-candle predicates, emit `CreateExecutorAction` with `OrderExecutorConfig` on connector `binance`, pair `BTC-USDT`, `TradeType.BUY` for entry and `TradeType.SELL` for liquidation, `Decimal("0.001")` BTC, `execution_strategy=MARKET`, `price=None`, `leverage=1`. A confirmed SELL nets against the existing long; no futures short, margin or borrowing.
- **Causal fill convention:** raw candle timestamp `T[t]` is **open**, but `close[t]` becomes available at `D[t]=T[t]+86400s`. The derivative defines its effective signal decision **and historical fill clock** as `D[t]`; the pinned simulator's same-row-close MARKET fill is an **idealized historical model**, not a guaranteed executable live close. Never pretend the raw open timestamp is the decision time, and never use `close[t+1]`, next-open guesses or fabricated fill prices. No intrabar stop/limit order path is required.
- **Position state:** `FLAT -> ENTRY_PENDING -> LONG -> EXIT_PENDING -> FLAT` only on **confirmed** fills. At most one pending order and one 0.001 BTC position, no DCA/safety orders, pyramiding, concurrent pairs, partial exits, reverse-short, trailing, TP, SL, time stop, or implicit cooldown. A rejected/unfilled BUY returns to FLAT and requires a **new future cross-up**; a rejected/unfilled SELL retains LONG with a latched liquidation intent retried on each later valid completed bar until confirmed. No new entry on an exit bar; earliest re-entry is the next completed bar with a new full entry predicate. If the sample ends LONG, mark the open 0.001 BTC to the last **actual** close, do not invent a terminal exit fill.
- **Ledger/costs:** start with 10,000 USDT unborrowed spot cash, fixed 0.001 BTC, reject an entry if `cash < qty*actual_close*(1+0.001)`. Research `trade_cost=0.001` per filled side (0.1% assumed quote notional, **not** a verified Binance customer fee tier), deducted from cash; BUY cash decrement `Q*P*(1+fee)`, SELL increment `Q*P*(1-fee)`; net realized quote PnL `Q*(sell-buy)-fee*Q*(sell+buy)`. `BacktestPositionHold` tracks average cost and gross realized PnL; accumulated `cum_fees_quote` must be subtracted for net economics. Spot has **no perpetual funding contract** (not a claim of zero realized perpetual funding). Spread/slippage/latency, partial fills, live precision/tick/lot/min-notional and exchange-specific fee tiers are **not independently verified or simulated**, so no claim of live fill realism.
- **Engine hazards fenced:** `terminated_executors_window=None` or a persistent confirmed-fill ledger is required for day-scale controller state; default time-windowing can hide old completed orders from the controller view. `BacktestingDataProvider.get_price_by_type` may return `Decimal("1")` on missing prices: explicitly **reject** this fallback and require actual historical close. `prepare_market_data` may discard NaN rows: continuity must be validated before using the derived signal so a missing daily candle never becomes a false adjacent period. Failed/pending actions never masquerade as fills.

## Evidence

### Source-reported

The directly read TradingView publication by RevoTheTrader (2025-03-14) specifies the three long predicates (RSI<30, K crossing above D, price above WMA), three short predicates (RSI>70, K crossing below D, price below WMA), and explicit Pine `strategy.entry` directions. It gives no independently verifiable net backtest statistics or complete executable Pine bytes in the retrieved page.

### Independently reproduced

Not independently reproduced. No backtest, Qlib/Hummingbot parity test, trade log, fee-tier verification or performance reproduction occurred in this Scout cycle.

### Negative evidence

Full Pine unavailable; no claim of source-native indicator defaults, order sequencing, native exit/risk/capital behavior or trade-event equivalence. Derived price Stochastic is **not** StochRSI; WMA50/RSI14/Stoch14,3,3 are researcher-selected pins. No profit, Sharpe, Survivor or HB Certified claim. No unsupported maker, next-open, intrabar, multi-asset or perpetual funding path is claimed.

**Six-gate submission evidence (for independent Hermes Auditor, not self-approval):** (1) complete pinned RSI, price-Stoch, WMA arithmetic, finite guards and exact crossing comparisons; (2) Binance spot LONG/FLAT, SHORT disabled; (3) triple-gated entry/exit, all stop/target/trailing/time exits disabled; (4) explicit fixed position, no DCA/concurrency, pending/fill/retry/re-entry states; (5) directly inspected pinned source's 1d Binance spot feed, ControllerV2/OrderExecutor MARKET close-fill, actual-close notional/fee, POSITION_HOLD and timestamp/price hazards, prior package hash evidence; (6) 100-bar continuous warmup, completed-bar decision clock and no future leakage. PASS here is a **proposed research admission record** requiring independent exact-head review, not an audit verdict.

## Falsification plan

With all source and derivative pins frozen, compare only in later authorized research: (F1) the full three-gate long setup against the same price-Stoch crossing without RSI gating; (F2) the full setup against the same crossing without WMA gating; (F3) opposite triple-gated liquidation against a researcher-declared RSI-only liquidation. Each change is a separately labeled derivative, not a hidden parameter search or evidence of this candidate's profitability. Do not perform screening until any newly required execution primitive receives representative Qlib/Hummingbot event-level validation.

## Crypto portability

The BTC-USDT Binance spot UTC-1d venue is a researcher-selected bounded instance of a market-agnostic source. The published short setup is used as a **flat exit only**; no short borrowing or funding. Porting to another pair, timeframe, derivative or fill convention changes the pinned research identity and requires separate data/engine verification. The house DCA 6/6/6, seven coins and futures 3x/5x campaign are downstream **optional experiments**, not HB_READY admission conditions.

## Limitations

No complete public Pine revision bytes, no source-event equivalence, no realized fill/fee/slippage validation, no profitability/OOS, no Hummingbot/Qlib candidate event-level parity, no trading approval. Triple-gated liquidation can leave a long open indefinitely; no protective stop is present. Same-bar-close MARKET fills are historical modeling, not an order type promising live close execution. Package-to-source wheel hash is cited from PR #414 rather than reverified here.

## Implementation status

Not implemented. No strategy-specific controller, Qlib artifact, Hummingbot run, container modification or trade is created by this record. Engine expressibility is bounded to the inspected historical spot close-fill model.

## Adoption boundary

Research-only; adoption not approved. Independent Hermes Auditor GitHub Webhook Review alone may source-verify, remediate on exact PR head, or reject/close. PASS is not Qlib parity, Survivor, HB Certified, Paper, Testnet or Live authorization.

## Related Wiki records

None.

## Sources

- TradingView primary publication: https://www.tradingview.com/script/ytN19Shr-RSI-Stochastic-WMA-Strategy/ (RevoTheTrader, 2025-03-14).
- Pinned engine source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior package/engine evidence: https://github.com/HCH725/alpha-strategy-research/pull/414 and https://github.com/HCH725/alpha-strategy-research/pull/417
