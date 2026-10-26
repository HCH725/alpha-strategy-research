---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "connorgeary150 RSI14 and BB20/2 dip with RSI50 or BB-mid reclaim exit — independent BTC-USDT spot 1d long-flat derivative"
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
source_as_of: 2026-02-23
sources:
  - https://www.tradingview.com/script/95JBkzXV-BTC-Mean-Reversion-RSI-Bollinger/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# RSI14 + close Bollinger(20,2) oversold dip, RSI50 / midline reclaim exit — independent long-flat derivative

## Provenance

**Primary first-party publication actually read 2026-10-26:** connorgeary150, *BTC Mean Reversion - RSI + Bollinger*, TradingView public open-source **strategy**, published 2026-02-23, stable script ID **95JBkzXV**: https://www.tradingview.com/script/95JBkzXV-BTC-Mean-Reversion-RSI-Bollinger/ . Its public description explicitly states: long if RSI(14)<30 AND price below the lower Bollinger Band; short if RSI(14)>70 AND price above upper band; long liquidation if RSI>50 OR price crosses back above the Bollinger middle; short liquidation if RSI<50 OR price crosses back below the middle. The author reports a BTCUSD 10-second study for 2026-02-16 through 2026-02-23; that is **source-reported, not reproduced or carried over**. The fetched page does **not** expose the complete Pine source bytes or the original BB length, multiplier, price input, fill flags, stop/target, sizing, pyramiding or fee settings. None is falsely attributed to the author.

**Independent derived executable strategy, not lossless Pine reconstruction:** researcher deliberately selects Binance BTC-USDT unleveraged spot, **UTC 1d** rather than the author's 10-second study, **long/flat only** (short entry and short exit disabled), Wilder RSI14 on close, **SMA20(close) ± 2.0 × population stdev20(close)**, the source-described long entry and long exit OR logic, **completed-bar-close historical MARKET simulation**, fixed 0.001 BTC, 80-bar warmup, 0.001 per-side modeled quote-notional transaction cost, no stops/targets/DCA and the precise pending/fill/continuity rules below. The original source's price-below-band and exit-cross language is made precise by the strict comparisons below; BB parameters, frame, venue, state, accounting and fill clock are **researcher-designed**, not silent author defaults. No claim of source-native trade-event equivalence.

**Immutable derivative identity:** `TV:95JBkzXV:connorgeary150:published-2026-02-23 | independently-derived-v1:2026-10-26 | Binance:BTC-USDT:spot:UTC1d | WilderRSI14(close),BB-SMA20(close)/population-stdev20×2 | ENTER RSI<30 & close<lower | EXIT RSI>50 OR close-cross-up-middle | LONG/FLAT,0.001BTC,no-DCA | completed-close-MARKET | trade_cost=0.001-per-side | 80-bar-warmup`. Changes to any decision-critical parameter, clock, exit OR, costs or state constitute a different derivative.

**Pre-write dedup:** GitHub connector read main at `708c43779bc606d51d950492d857ee658118b0aa` (untruncated tree: 353 root strategy records; static README: 353), searched main for `95JBkzXV` and `connorgeary150` (zero code-search hits), and checked all 10 open `research/*` PR titles/bodies (no matching URL or this exact rule); exact open PR search also returned zero. Closest existing mechanisms differ materially: `freqtrade-bband-rsi-dip-buy` enters RSI14<30 below a **typical-price** BB20/2 and exits on **RSI>70** with **+10% ROI/-25% stop**, not this **RSI>50 OR midline-cross** exit; `chartart-bollinger-rsi-double-joint-cross` requires two **simultaneous crossover edges** using RSI6/50 and BB200, and reverses two-sided; `forven-bb-edge-fade-reclaim` requires a **prior-band-pierce then reclaim edge** and no RSI. This is neither the same TradingView source nor materially identical entry/exit behavior. Numeric count agreement is not an independent re-audit of all prior PASS records.

## Economic mechanism

### Source-reported
An oversold oscillator and a statistically low price jointly define a contrarian dip. The author exits long once RSI recovers above 50 **or** price crosses back above the middle band; the two exit alternatives are independent. The source also defines a separate short path, deliberately excluded from this derivative.

### Research interpretation
The conjunctive entry filters out RSI-only dips that never reach the lower envelope. The first of two independent recovery conditions liquidates the long; a position may persist without a protective stop if neither recovers. There is no inferred profitability, Sharpe, drawdown, or trade-count claim for this derivative.

## Signal

Use a single uninterrupted stream of **completed** Binance BTC-USDT spot UTC 1d OHLC candles, t indexing the latest completed candle; only close enters the indicator formulas.

1. `delta[t]=close[t]-close[t-1]`; `gain=max(delta,0)`, `loss=max(-delta,0)`. Seed Wilder averages with the arithmetic mean of the first **14** valid deltas, then `avg[t]=(13*avg[t-1]+value[t])/14`. `RSI14=100-100/(1+avgGain/avgLoss)`. If avgLoss=0 and avgGain>0 return 100; both zero return 50; avgGain=0 and avgLoss>0 return 0. No unseeded RSI is eligible.
2. `basis[t]=sum(close[t-19..t])/20`. `sigma[t]=sqrt(sum((close[i]-basis[t])² for i=t-19..t)/20)` (**population** standard deviation, no sample ddof=1). `lower[t]=basis[t]-2*sigma[t]`, `upper[t]=basis[t]+2*sigma[t]`. Require 20 finite strictly positive closes. The upper band is computed for source context only; **no short or upper-band order** is active.
3. **ENTRY**, only while FLAT and no pending order: `RSI14[t] < 30 AND close[t] < lower[t]`. Both are strict level conditions, not crossover edges. Equality at 30 or lower band does not enter.
4. **EXIT**, only while LONG: `RSI14[t] > 50 OR ((close[t-1] <= basis[t-1]) AND (close[t] > basis[t]))`. Strict current RSI>50 or strict upward close/basis crossover with prior equality allowed. It is an **OR**, not AND. A price touch exactly at basis[t] does not count as cross; RSI exactly 50 does not exit unless the price-cross alternative is true.
5. **Bar priority:** evaluate EXIT only if long at bar start, ENTRY only if flat at bar start. A pending order suppresses further orders. No same-bar re-entry or same-bar exit of a newly entered position. A held long may remain indefinitely; no reverse-short, implicit stop-loss, take-profit, trailing, breakeven or time-limit exit.
6. **Warmup:** first 80 consecutive completed daily bars remain flat; earliest decision is completed bar 81 if current and previous RSI/band inputs are valid. A missing/duplicate/non-monotone UTC daily bar or invalid/nonpositive close suspends all new decisions and requires a fresh contiguous 80-bar warmup; if already long, preserve position without fabricating an exit. Never drop a missing bar and treat nonadjacent bars as adjacent.

## Required data and causality

Binance SpotCandles `1d` actual exchange open/high/low/close with exchange **open** timestamp `T[t]`. For a valid UTC day, signal input close[t] is not available until `D[t]=T[t]+86400 seconds`. **Normalize the effective decision and historical fill timestamp to D[t]** before using the pinned simulator's prepared candle rows; the raw exchange open timestamp must never be misrepresented as a close-available decision timestamp. Check monotonic daily continuity **before** the engine's `dropna` step. No `request.security`, incomplete candle, centered filter, future close, intrabar high/low fill, other pair, funding, mark/index price, trained model, order book or external feed is required. Never substitute a fabricated price when a candle or price lookup is missing.

## Execution assumptions — pinned Hummingbot Gate 5

**Directly inspected with the connected GitHub app this cycle:** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, distribution/package `20260920`, `hummingbot/VERSION = dev-2.17.0`. Specific source paths: `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` includes `1d`; `binance_spot_candles.py::_parse_rest_candles` maps row[0] to the candle's open timestamp and row[1..5] to OHLCV; `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` loops controller actions per prepared row, uses `BacktestPositionHold` for incremental BUY/SELL average-cost, realized-gross PnL and fee accumulation; `executors_simulator/order_executor_simulator.py` MARKET fills on the **first actual row close** and records `filled_amount_quote=amount*close`, `cum_fees_quote=trade_cost*notional`, `CloseType.POSITION_HOLD`; `backtesting_data_provider.py` exposes the price lookup's dangerous default `Decimal("1")` on missing keys. Prior independent Alpha PR **#414** reports a wheel/source 902/902-byte binding for this pin, **not rehashed this cycle**; #417 is prior bounded engine evidence. These are verified model primitives, not proof of any candidate backtest or of live-market fill prices.

**Proposed strategy-specific ControllerV2 (not implemented):** on a valid completed daily decision, emit a `CreateExecutorAction` containing `OrderExecutorConfig` with `ExecutionStrategy.MARKET`, connector `binance`, pair `BTC-USDT`, BUY to enter and SELL to fully liquidate, `Decimal("0.001")` base BTC, leverage 1, no limit/maker path. Model a single unborrowed spot book: `FLAT → BUY_PENDING → LONG → SELL_PENDING → FLAT` **only after confirmed fills**. Max one 0.001 BTC long, one pending order, one pair; no short, pyramiding, safety orders, averaging, shared capital, partial exits or concurrent strategies. If a BUY fails/unfills, return flat and require a **future eligible entry bar**; if SELL fails/unfills, retain long with liquidation intent latched and retry only on later valid completed bars until filled. Exit has priority and prevents re-entry that bar; no cooldown after confirmed exit, but re-entry requires a later new eligible completed bar. At sample end, value an open position at the last **real observed close** without inventing a terminal SELL fill.

**Timestamp and fill caveat:** the simulator's same-row-close MARKET execution is an **idealized historical close-price fill convention**, not a promise that an exchange market order submitted after close can obtain that same close. It must be described as a research model, not as source-native Pine fill semantics or live-trading realism. The pinned backtester `prepare_market_data` merges features by timestamp and calls `dropna`; data continuity and completed-close availability must be enforced upstream. Use `terminated_executors_window=None` so the controller can see confirmed daily POSITION_HOLD orders; the default one-hour visible history can otherwise hide an earlier daily fill. Persist a fill-confirmed state ledger, not order-submission guesses. Reject the provider's `Decimal("1")` fallback and any nonfinite or absent actual close.

**Costs/position accounting:** initial unborrowed spot cash **10,000 USDT**, fixed 0.001 BTC; entry requires `cash >= 0.001*actual_close*(1+0.001)`. Research `trade_cost=0.001` per **filled side**, i.e. a modeled 0.1% of actual filled quote notional, not a verified Binance account fee. BUY cash change `-Q*P*(1+f)`; SELL cash change `+Q*P*(1-f)`. Gross matched PnL `Q*(P_sell-P_buy)`; net matched PnL subtracts both `f*Q*P_buy` and `f*Q*P_sell`. The pinned hold ledger tracks gross realized PnL and `cum_fees_quote` separately; do **not** report gross `total_pnl` as fee-inclusive net. Historical simulator assumes close-price fills with no modeled additional slippage/spread/latency; that is **not measured zero slippage**. No funding contract exists for this unleveraged spot derivative; do not infer zero perpetual funding. Actual exchange taker tier, partial fills, precision, minimum notional, slippage and order execution are unverified; no Paper/Testnet/Live claim.

## Six-gate evidence for independent Hermes Auditor

1. **Determinism:** fully specified Wilder RSI14 seed, close-SMA20/population-stdev20 bands, thresholds, strictness, OR exit and data invalidation.
2. **Direction:** one BTC-USDT Binance spot long or flat; original source's short side expressly disabled as a derivative.
3. **Entry/exit/risk:** source-derived two-key entry and independent two-alternative recovery exit; all SL/TP/trailing/time/risk legs expressly disabled.
4. **State:** fixed 0.001 BTC, pending-fill state, no DCA/pyramiding/concurrency, failed order/retry and re-entry rules, no hidden cooldown.
5. **Pinned engine:** directly inspected pinned `1d` Binance SpotCandles, MARKET first-row-close OrderExecutor, ControllerV2 action loop, POSITION_HOLD cost/fee netting, timestamp normalization and missing-price/window hazards; prior #414 package binding, no new execution primitive claimed.
6. **Causality:** 80 complete contiguous bars, t and t−1 only, completed-close timestamp `T+86400`, no future data, no invented missing candles/prices.

**This PASS frontmatter is a Scout proposal requiring independent exact-head six-gate audit, not self-approval.** It is not a profitability result, source-native Pine equivalence, Qlib parity, Survivor/HB Certified status or trading permission. Before large-scale Qlib screening, validate any **new** strategy/execution primitive with representative Hummingbot/Qlib event-level parity; existing verified primitives may be reused per current policy.

## Evidence and limitations

**Source-reported:** TradingView publication specifies the long/short RSI and BB predicates, long/short recovery exits, and reports 1,181 trades / 710 profitable on its own 10-second BTCUSD study. These numbers are author claims only and **not** used as derived-strategy performance evidence.

**Independently verified this cycle:** first-party TradingView publication prose and pinned Hummingbot source paths enumerated above; main/root-count 353 and static README 353 at the captured SHA; dedup search and open research PR inspection. Full 353-record historical PASS frontmatter audit was **not** independently repeated; count equality is not a complete admission audit.

**Not independently reproduced:** complete Pine source, TradingView backtest, any candidate Hummingbot or Qlib backtest, venue fee/slippage/funding history, actual fill data, candidate event-level parity, profit/OOS, wheel hash this cycle. The derived 1d model is **not** the author's 10-second execution and may exhibit completely different event sequences. With no protective stop, an adverse move can be arbitrarily large until an exit condition fires; missing data can extend exposure.

## Falsification plan

Future authorized research may compare this frozen two-key entry with RSI-only entry and BB-only entry, and the frozen OR recovery exit with its RSI-only and midline-only alternatives; each alteration is a **separately declared derivative**, not an invisible parameter search. Do not run them in this Scout cycle.

## Crypto portability

The author's BTCUSD 10-second venue/frame is not carried as a source-native backtest. This candidate is explicitly BTC-USDT Binance spot 1d with fixed size, no leverage, no short and no funding contract. Different coins, futures, timeframes or BO/SO overlays require separate derivative disclosure and relevant engine/data-model verification; the downstream 7-coin, 1h/4h/1d, 6/6/6 and 3×/5× research campaign is **not** an HB_READY admission requirement.

## Implementation status

not-implemented. No controller code, Qlib executable, backtest, deployment, trading, cron or workflow change was made. An admitted but not materialized strategy follows existing `IMPLEMENTATION_NEEDED` when later selected, not a second eligibility gate.

## Adoption boundary

Research-only; adoption not approved; approval scope research-only. Independent Hermes Auditor GitHub Webhook Review alone owns source-fact remediation, exact-head PASS merge, or NOT_LOSSLESS closure. Scout does not approve, merge, close or update README.

## Related Wiki records

None.

## Sources

- https://www.tradingview.com/script/95JBkzXV-BTC-Mean-Reversion-RSI-Bollinger/ — connorgeary150, public publication, 2026-02-23.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned engine.
- https://github.com/HCH725/alpha-strategy-research/pull/414 — earlier independent package/source binding.
- https://github.com/HCH725/alpha-strategy-research/pull/417 — earlier bounded primitive review.
