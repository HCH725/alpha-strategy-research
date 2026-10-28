---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Trading_Indicator_Pro fourfold volume and 1.5% price expansion with SMA20/ATR14 filter and ten-bar signal cooldown — independent BTCUSDT spot 1h long-flat derivative
created: 2026-10-28
updated: 2026-10-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-02-08
sources:
  - https://www.tradingview.com/script/Fk7JtbC9-AI-Volume-Breakout-for-scalping/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Fourfold-volume impulse with SMA20, ATR14 volatility cap and ten-bar signal cooldown — independent derivative

## Provenance

- **Primary first-party TradingView source:** *AI Volume Breakout for scalping*, author **Trading_Indicator_Pro**, script identity **Fk7JtbC9**, initially published **2025-02-05**, updated **2025-02-08** (last release note: minor improvements). Public open-source **indicator** page read on 2026-10-28: https://www.tradingview.com/script/Fk7JtbC9-AI-Volume-Breakout-for-scalping/ . The complete Pine code, its version and an immutable source-byte digest were **not** retrieved. The author's indicator is **not** a complete source-native automated trading strategy, and this record does not claim Pine parity.
- **Verified author-description facts, not invented defaults:** volume change must be positive and current/previous-bar volume ratio at least **4.0**; absolute price change relative to bar open at least **1.5%**; trend confirmation uses **SMA20**; an ATR/close low-volatility filter exists; bullish/bearish directional signals exist; signals have a **10-bar cooldown**. The page explicitly says this is heuristic, **not ML/AI**. The first-party text does **not** publish the ATR length or low-volatility threshold, the exact priceDelta expression, initial indicator state, complete execution/risk orders, fees or fill semantics.
- **Independent researcher-defined derivative, NOT source-native/lossless:** This record selects Binance BTC-USDT **spot 1h**, maps the described price change to `close-open`, fixes ATR to Wilder RMA14 with a **strict 3% ATR/close ceiling**, defines price-vs-SMA20 trend tests, selects LONG/FLAT (bearish accepted signal closes a long), fixes a precise cooldown including no-op signals, sets 0.001 BTC fixed position, 10,000 USDT starting cash, 120-bar warmup, completed-close idealized MARKET fills, a 0.1% per-side modeled fee, zero additional modeled slippage, and all disabled risk/execution features. **ATR14 and 3%, all order/position/cash rules, seeds, cooldown priority, market and timeframe are researcher choices**, not attributed to the author. A source-native implementation would require the original Pine.
- **Frozen identity:** `TV:Fk7JtbC9|Trading_Indicator_Pro|2025-02-08|independent-derived-v1-20261028|BinanceSpot-BTC-USDT-UTC1h|V>0-and-V/Vprev>=4|abs(C-O)/O>=0.015|SMA20-price-side|WilderATR14/C<0.03|signal-cooldown10|LONG-FLAT|Q0.001BTC|cash10000USDT|fee0.001-side|same-completed-close-MARKET|warmup120`. Altering any of these makes a distinct derivative.

## Economic mechanism

**Source-reported:** The indicator marks unusual one-bar volume expansion coincident with a substantial directional price move, filtered by trend and low volatility. The source does not supply a verified automated trade ledger or a source-native risk model. No performance statistic is imported or reproduced.

**Research hypothesis only:** Fourfold relative volume and a >=1.5% directional bar may identify rare impulses, while a 20-bar SMA direction gate and ATR/close cap avoid countertrend and extreme-volatility entries. This is untested; the lack of protective stops can create unbounded holding periods and large drawdowns. No profitability or survivor claim.

## Signal — deterministic independent specification

- One Binance BTC-USDT spot **UTC-aligned 1h** OHLCV series. For bar index `t`, exchange timestamp `T[t]` labels its **open**, and the complete bar is available only at `E[t]=T[t]+3600 seconds`. Never evaluate the current incomplete candle. Every arithmetic comparison uses finite values and exact inequalities below; no machine-learning training, external signal, higher timeframe, cross-asset volume, order-book or funding feed.
- A valid candle has a unique strictly consecutive UTC 1h open timestamp; finite `O,H,L,C>0`, `H>=max(O,C)`, `L<=min(O,C)`, `H>=L`, and finite `V>=0`. An invalid, missing, duplicated or non-consecutive bar breaks the contiguous segment. Do not interpolate, forward-fill, infer a price or create an order on the invalid bar.
- `SMA20[t]=(C[t]+...+C[t-19])/20`, defined only after 20 contiguous valid bars. Current close participates because the decision is at **completed close**. Source gives length 20; this exact price source and equality handling are researcher-pinned.
- `TR[0]=H[0]-L[0]` at the first bar of each valid segment; for later bars `TR[t]=max(H[t]-L[t],abs(H[t]-C[t-1]),abs(L[t]-C[t-1]))`. `ATR14[13]=sum(TR[0..13])/14`, then `ATR14[t]=(13*ATR14[t-1]+TR[t])/14` for `t>=14`. This is **Wilder RMA14**, not an SMA of TR, and the entire ATR definition/length is researcher-selected because the source description omits it.
- `lowVol[t]=(ATR14[t]/C[t] < 0.03)`; **strict** threshold, equality fails. The 3% cap is researcher-defined, not an original default. `trendUp[t]=(C[t]>SMA20[t])`; `trendDown[t]=(C[t]<SMA20[t])`. Equality to SMA20 passes neither.
- `volumeImpulse[t]=(V[t-1]>0 && V[t]>V[t-1] && V[t]/V[t-1]>=4.0)`. The positive prior-volume guard makes division deterministic; zero previous volume cannot generate a signal. Equality at 4.0 passes. `delta[t]=C[t]-O[t]`; `priceImpulse[t]=(abs(delta[t])/O[t]>=0.015)`. Equality at 1.5% passes. This `delta` definition is explicitly a researcher interpretation of the author's unspecified `priceDelta`.
- `rawBull[t]=volumeImpulse[t] && priceImpulse[t] && delta[t]>0 && trendUp[t] && lowVol[t]`. `rawBear[t]=volumeImpulse[t] && priceImpulse[t] && delta[t]<0 && trendDown[t] && lowVol[t]`. They are mutually exclusive. No separate crossover or confirmation bar is required.
- **Signal cooldown (researcher state-machine pin):** `lastAcceptedSignalIndex` starts undefined at the beginning of each contiguous segment. A rawBull/rawBear event at eligible bar `t` is **accepted** iff no previous accepted signal exists in that segment or `t-lastAcceptedSignalIndex>10`. After any accepted signal, set `lastAcceptedSignalIndex=t`, **even when the portfolio-side order is a no-op or a BUY lacks funds**. The next **ten complete bars** `t+1..t+10` cannot emit accepted signals; `t+11` may. Rejected raw events do not reset cooldown. The author's prose gives ten bars, but this exact signal/no-op interpretation is a disclosed derivative choice.
- **FLAT -> LONG:** an accepted bullish signal buys exactly **0.001 BTC** via one modeled MARKET BUY at actual `C[t]` if available USDT cash covers `0.001*C[t]*(1+0.001)`. Otherwise remain FLAT, consume the signal for cooldown, and do not invent a partial fill or delayed order.
- **LONG -> FLAT:** an accepted bearish signal sells **all** 0.001 BTC via one modeled MARKET SELL at actual `C[t]`; the bearish indicator event is used as an exit, not a short entry. An accepted bullish signal while LONG and an accepted bearish signal while FLAT are **order no-ops but still start cooldown**. Only one accepted signal and at most one order per completed bar.
- **Position/risk:** initial FLAT, zero BTC and 10,000 USDT. Max one long, no short/borrow/margin/leverage (leverage=1), no DCA/safety orders/pyramiding/partial sizing/simultaneous orders/portfolio sharing. No SL, TP, trailing, time-based exit, mandatory liquidation, intrabar stop/limit/maker, scheduled session closure, or discretionary overrides. A LONG can persist indefinitely if no accepted bearish event occurs. At end of sample it remains marked to last valid close, **not** force-sold.
- **Warmup/gaps:** first **120 contiguous complete valid 1h bars** of a segment are indicator-only, with **no new signals/orders**; the 121st may trade. On a missing/invalid bar reset indicator and cooldown state and require a fresh 120 valid-bar warmup; an already held BTC position stays held through the gap, without synthetic exit or missing-price marking. Use last valid close for the last known mark until valid prices resume; never backfill missing close. After re-warmup the position is subject to the same accepted bearish exit rule. No future-bar correction, lookahead or full-sample fit.

## Required data

Only completed, timestamped Binance BTC-USDT spot 1h `open/high/low/close/volume`; previous-bar volume and previous close are used only after observation. The 120-bar warmup exceeds SMA20, ATR14 initialization and the ten-bar signal cooldown; all calculations are prefix-causal. No unsupported multi-asset synchronization, non-OHLCV input, next-open, intrabar, perpetual funding, short or multi-timeframe path is required.

## Execution assumptions — six-gate engine evidence

- **Pinned Hummingbot:** policy package **`20260920`**, `hummingbot/VERSION=dev-2.17.0`; pinned source inspected directly through GitHub connector at **`HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`**. That source's `setup.py` declares **`20260729`**, not the package pin; **do not silently equate these strings**. Previously independently reviewed alpha PR **#414** records a wheel SHA256 **`ea5a929c52095bc03fd34f5b3fb2fbfef068f7ea880af6c38290d1ddb729a148`** and 902 shipped Python files corresponding to the pinned source. This Scout **did not re-download/hash the wheel or inspect a deployed image**. Independent Auditor must confirm the applicability of the earlier package-to-source proof; otherwise Gate 5 must fail.
- **Actual inspected feed/clock:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` lists `1h`; `binance_spot_candles.py::_parse_rest_candles` maps Binance REST `row[0]` to the **open** timestamp and `row[1..5]` to OHLCV. `backtesting_data_provider.py` loads historical candle feeds; `backtesting_engine_base.py` prepares features, advances rows, calls controller `determine_executor_actions()` and processes `CreateExecutorAction`. Raw row timestamps **cannot** be treated as close-availability timestamps: all signals, state changes and fills here are effective only at `E[t]=T[t]+3600`. A dedicated controller is **not yet implemented**; it must enforce this causal offset, gap/120-bar warmup and cooldown rather than relying on an unadjusted `merge_asof` to mask stale features.
- **Actual inspected execution path:** `OrderExecutorConfig` permits `ExecutionStrategy.MARKET`, `TradeType.BUY/SELL`, fixed `amount`, `connector_name=binance`, `trading_pair=BTC-USDT`, `leverage=1`. `OrderExecutorSimulator.simulate` for MARKET uses the **first supplied row's close** as the fill price, sets `filled_amount_quote=amount*close` and `cum_fees_quote=trade_cost*filled_amount_quote`, and terminates as `POSITION_HOLD`. A signal at completed `t` must supply the **same completed row** for this idealized close-fill path, with effective event timestamp `E[t]`; no next-open or real post-close exchange execution guarantee is claimed. Controller inventory must reconcile confirmed simulated fill events and a separate ledger, not assume the delayed `positions_held` view is instantaneous.
- **Cash, fees and PnL:** fixed Q=0.001 BTC; starting cash 10,000 USDT; hypothetical `trade_cost=0.001` **per BUY and SELL side** (0.1% each). BUY debits `Q*P*(1+0.001)` USDT and adds Q BTC; SELL removes Q BTC and credits `Q*P*(1-0.001)` USDT. Track both-side fee-adjusted realized PnL and last-known-price unrealized PnL in a separate Decimal cash/BTC ledger and reconcile to simulated fills/fee events. Do **not** mistake simulator gross `net_pnl_quote` or aggregate `total_pnl` for fee-inclusive equity. No **additional modeled** slippage in this selected MARKET-close historical convention; **not** an assertion of zero actual slippage. Real fee tier, bid-ask spread, exchange tick/lot/min-notional, latency and partial fills are not verified; any unexpected fill failure, missing price, float/Decimal material residual or unsupported rounding must fail closed, never fabricate a trade.
- **Market economics:** Spot only; funding, liquidation, futures margin and borrow interest are **not applicable** to this declared unleveraged cash-and-BTC model, not assumed zero for a perpetual market. `BacktestingDataProvider.get_price_by_type` has a `Decimal("1")` fallback when price is missing; this fallback is **forbidden** for execution or PnL. Use only observed valid close and explicit cash/quantity.
- **Reused representative capability, not a new backtest:** Independently audited prior PRs **#414, #421, #423, #550** document this same pinned Binance spot OHLCV / MARKET-close / POSITION_HOLD / fee/clock primitive. This candidate changes only controller-side OHLCV indicator predicates and a ten-bar cooldown state; it does not demand an unverified data feed, executor, market or fill primitive. No new Hummingbot or Qlib run was performed; any new unverified execution path requires representative event-level Hummingbot/Qlib parity **before large-scale screening**.

## Evidence

### Source-reported
First-party TradingView page by Trading_Indicator_Pro, published 2025-02-05, last updated 2025-02-08, inspected 2026-10-28: `volumeThreshold=4.0`, positive volumeDelta, `abs(priceDelta/open)>=1.5%`, SMA20 trend confirmation, ATR/close low-volatility gate, bullish/bearish labels, and 10-bar signal cooldown. It calls itself an indicator, not an executable order/risk system; its AI label does not imply an ML model. Full Pine bytes were unavailable.

### Independently reproduced
**None for this candidate.** The Scout verified the author-described facts and inspected pinned engine source paths, but did not run TradingView Pine, Hummingbot, Qlib or a performance backtest. Prior PRs' audited engine evidence is cited, not represented as this candidate's own execution result.

### Dedup and negative evidence
Pre-write current main at `c79695d3e5c0da2da70c260d641871575c20ac0f`: **402** root strategy Markdown records and README count **402**; sampled PASS frontmatter, **not** a complete 402-file status audit. GitHub code search for `Fk7JtbC9`, `volumeThreshold`, and fourfold volume returned no exact record; GitHub PR search for the source ID, title and author returned no prior PR. All **10** open research PRs were checked by branch/title/source descriptions and none used this TradingView source. Nearest cousins (e.g. `forven-atr-volume-breakout-long-flat-ethusdt-1h-2026-10-17.md` and `dual-ema-engulfing-volume-long-btcusdt-1h-2026-10-07.md`) instead gate ATR/Donchian price breakouts or engulfing/EMA signals with rolling-average volume, **not** a fourfold **previous-bar** volume ratio conjoined with a >=1.5% open-to-close impulse, a Wilder-ATR/price cap and signal-level ten-bar cooldown. This is a materially different mechanism, not a parameter-only clone.
Original Pine and exact ATR/cooldown defaults are unavailable; no source-native equivalence is claimed. ATR14/3% and all order mechanics are expressly researcher-defined, not silently presented as author facts. Signals can be rare and holding risk is unlimited; modeled same-close fills and fees are not real execution guarantees.

## Falsification plan

Under a separately approved downstream research campaign, compare the frozen derivative with an otherwise identical strategy without the volume-ratio gate and with/without cooldown, using predetermined IS/OOS and declared research costs. Do not treat author chart labels as independently reproduced trades, tune on OOS, or claim profitability. A new execution capability, if introduced, requires one representative HB/Qlib event-level validation before mass screening; this Scout does not backtest.

## Crypto portability and limitations

The specified strategy is Binance BTC-USDT **spot 1h**, LONG/FLAT. It is not a claim that other symbols, perpetual futures, frequencies, DCA BO/SO 6/6/6, shorts, or next-open execution are banned; each would be a separately defined research change requiring its own applicable data/cost/causality proof. `hb_ready_status: PASS` is the **Scout's six-gate admission proposal pending independent Hermes Auditor review**, not an independent PASS verdict. It does not authorize profitability claims, Qlib parity, Survivor certification, deployment or Paper/Testnet/Live trading.

## Implementation status

`not-implemented`: no dedicated Hummingbot controller or Qlib strategy-specific executable recipe has been built or run. This does not create a second HB_READY admission gate.

## Adoption boundary

`status: research-only`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review alone may verify/remediate the exact head, PASS merge or NOT_LOSSLESS close. Scout never approves, merges, closes, writes README, backtests, trades or changes workflows.

## Sources

- https://www.tradingview.com/script/Fk7JtbC9-AI-Volume-Breakout-for-scalping/ — Trading_Indicator_Pro, public script first published 2025-02-05, last updated 2025-02-08.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned Hummingbot source.
- https://github.com/HCH725/alpha-strategy-research/pull/414 — independently reviewed pinned wheel/source evidence and execution primitives.
- https://github.com/HCH725/alpha-strategy-research/pull/550 — independently reviewed same Binance spot 1h MARKET-close primitive.
