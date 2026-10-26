---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "FMZ Shannon Entropy V2 percentrank-tail long-flat BTCUSDT 1d derivative"
created: 2026-10-26
updated: 2026-10-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - fmz
  - source-backed
status: research-only
confidence: medium
source_as_of: 2022-05-24
sources:
  - https://www.fmz.com/strategy/365095
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FMZ Shannon Entropy V2 (Info-S) percentrank-tail — independent long-flat derivative

## Provenance

**Primary first-party publication actually read 2026-10-26:** FMZ strategy **365095**, *Shannon Entropy V2* (shorttitle `Info-S`), published by FMZ user **ChaoZhang** 2022-05-23 15:07:54, last modified 2022-05-24 10:13:21 (1,268 hits, 4 forks, tags `stdev,WMA`): https://www.fmz.com/strategy/365095 . The page-embedded Pine (`//@version=4`, in-code header `© kocurekc / @author Kocurekc`, MPL-2.0) was read in full from the served page bytes. Frozen source defaults: `src=close`, `len=9` (Entropy Length), `avg=44` (Averaging Length), `vPR=2` (Percent Rank Limit), `bc=true` (Include Source), `vc=true` (Include Volume). Display-only inputs (`range=0.025` color level, `pb` Print Bands, WMA/stdev bands) gate nothing and are inert for signals. The author's prose states the value measures price/volume "surprise"/information, that "Buy and Sell points are up to the user", and shows a mirror-author backtest config block (2h period / 15m base, Futures_Binance BTC_USDT, 2022-04-22 through 2022-05-21); that config is **source-reported context, not reproduced or carried over**.

**Declaration mismatch, disclosed:** the FMZ-published Pine declares `study()` yet contains `strategy.entry("Enter Long", strategy.long)` / `strategy.entry("Enter Short", strategy.short)` lines; as published it is not a runnable strategy. This record is therefore an **explicitly derived executable strategy, not a lossless source reproduction**: it uses only the two verbatim signal conditions, which appear identically in the code's `plotshape` lines (`hvp>vPR`-style green/red markers) and in the entry lines — long interest when `hvp<vPR`, short interest when `hvp>(100-vPR)` — with the short leg mapped to a flat exit. No other behavior is attributed to the author.

**Independent derived executable strategy:** researcher deliberately selects Binance BTC-USDT unleveraged spot, **UTC 1d**, **long/flat only** (short leg disabled and mapped to exit), frozen source defaults above, **completed-bar-close historical MARKET simulation**, fixed 0.001 BTC, 52-bar warmup, 0.001 per-side modeled quote-notional transaction cost, no stops/targets/DCA and the precise pending/fill/continuity rules below. Pine `strategy.entry` market semantics are **not** claimed; the fill clock is the researcher-designed research model below. No claim of source-native trade-event equivalence.

**Immutable derivative identity:** `FMZ:365095:ChaoZhang:modified-2022-05-24 | independently-derived-v1:2026-10-26 | Binance:BTC-USDT:spot:UTC1d | entropy9(price-shares,volume-shares,44-rank,limit2) | ENTER hvp<2 | EXIT hvp>98 | LONG/FLAT,0.001BTC,no-DCA | completed-close-MARKET | trade_cost=0.001-per-side | 52-bar-warmup`. Changes to any decision-critical parameter, clock, threshold, cost or state constitute a different derivative.

**Pre-write dedup:** read main at `102b7a1` (354 root strategy records; static README: 354), searched main for `365095`, `kocurekc`, `Info-S`, `shannon` and `entropy` (zero record hits), and checked all 10 open `research/*` PR titles/bodies (#353, #350, #331, #304, #251, #92, #89, #63, #49, #48 — no matching URL or entropy rule). Closest existing mechanisms differ materially: `forven-connors-rsi-oversold-recross` uses `PercentRank(ROC)` inside a Connors composite oscillator (no information shares, no log2, no volume); `forven-momentum-burst-mean-reversion` uses a researcher-defined percentile on momentum (no entropy); `fibonacci-retracement-reclaim` trades single-swing levels (no template-free dispersion statistic). No pool record computes Shannon price/volume share entropy. Numeric count agreement is not an independent re-audit of all prior PASS records.

## Economic mechanism

### Source-reported

Dispersion between the last 9 closes carries "price information"; dispersion between the last 9 log-volumes carries "volume information". Their difference (`info = H(price) − H(volume)`, in bits) highlights bars needing attention: large change means new information, minimal new information means complacency. Extreme low 44-bar percent-rank of `info` marks long interest; extreme high marks short interest. The author leaves buy/sell use to the reader.

### Research interpretation

A strict 44-bar rolling minimum of `info` (entry) means the current bar's price/volume information mix is calmer than every one of the previous 44 bars — a complacency extreme. A rolling maximum (exit) means it is the most surprising bar of the window. Both are rare tail events on daily bars by construction. There is no inferred profitability, Sharpe, drawdown, or trade-count claim for this derivative.

## Signal

Use a single uninterrupted stream of **completed** Binance BTC-USDT spot UTC 1d OHLCV candles, t indexing the latest completed candle (0-based from sample start).

1. **Data preconditions for bar t:** `close>0` and `volume>0`, both finite, for every bar in `t-8..t`. If violated, `info[t]` is not computed (treated as na): no entry fires; a held long is preserved without fabricating an exit. `log` is the natural logarithm (Pine `log`); `log2(x)=log10(x)/log10(2)` by change of base, computed in double precision.
2. **Shares:** `S9C[t]=sum(close[t-8..t])`; `cr[t-i]=close[t-i]/S9C[t]` for `i=0..8`. `L[t-i]=log(volume[t-i])`; `S9L[t]=sum(L[t-8..t])`; `vr[t-i]=L[t-i]/S9L[t]`. (`sum` = sliding sum of the last 9 values including the current bar.)
3. **Entropy:** `Hc[t]=−sum(cr·log2(cr),9)`; `Hv[t]=−sum(vr·log2(vr),9)`; `info[t]=Hv[t]−Hc[t]` (bits). Terms with a zero share never occur under the preconditions (`cr,vr>0` strictly when all inputs are positive).
4. **Percent-rank:** `hvp[t]=100×#{j=1..44 : info[t-j] ≤ info[t]}/44`, defined only when `info[t-44..t]` are all valid (ties count toward rank, per the official "less than or equal to the current value of given series" definition: https://www.tradingview.com/pine-script-reference/v5/#fun_ta*percentrank ). On the 44-lattice, **ENTRY ⟺ count=0** and **EXIT ⟺ count=44**; no other value can satisfy the strict thresholds.
5. **ENTRY**, only while FLAT and no pending order: `hvp[t] < 2` (verbatim source threshold). Equality at 2 does not enter.
6. **EXIT**, only while LONG: `hvp[t] > 98` (verbatim source threshold; source short leg mapped to flat). Equality at 98 does not exit.
7. **Bar priority:** evaluate EXIT only if long at bar start, ENTRY only if flat at bar start. The two thresholds are mathematically mutually exclusive. A pending order suppresses further orders. No same-bar re-entry or same-bar exit of a newly entered position. A signal while long is ignored (Pine default `pyramiding=0` adds nothing). A held long may remain indefinitely; no stop-loss, take-profit, trailing, breakeven or time-limit exit exists — all expressly disabled, matching the source (which defines no risk leg).
8. **Warmup:** bars at index 0–51 are warmup-only and cannot trigger orders; the first signal evaluation uses the close of bar index 52 (the earliest bar whose 44 previous info values, indices 8–51, are all valid). A missing/duplicate/non-monotone UTC daily bar or a precondition violation suspends all new decisions and requires a fresh contiguous 52-bar warmup; if already long, preserve position without fabricating an exit. Never drop a missing bar and treat nonadjacent bars as adjacent.

## Required data and causality

Binance SpotCandles `1d` actual exchange open/high/low/close/**volume** with exchange **open** timestamp `T[t]`. For a valid UTC day, signal inputs close[t]/volume[t] are not available until `D[t]=T[t]+86400 seconds`. **Normalize the effective decision and historical fill timestamp to D[t]** before using the pinned simulator's prepared candle rows; the raw exchange open timestamp must never be misrepresented as a close-available decision timestamp. Check monotonic daily continuity **before** the engine's `dropna` step. No `request.security`, incomplete candle, centered filter, future close, intrabar high/low fill, other pair, funding, mark/index price, trained model, order book or external feed is required. Never substitute a fabricated price when a candle or price lookup is missing.

## Execution assumptions — pinned Hummingbot Gate 5

**Directly inspected with the connected GitHub app this cycle:** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, distribution/package `20260920`, `hummingbot/VERSION = dev-2.17.0`. Specific source paths: `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` includes `1d`; `binance_spot_candles.py::_parse_rest_candles` maps row[0] to the candle's open timestamp (seconds) and row[1..5] to OHLCV; `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` loops controller actions per prepared row (`iterrows`), uses `BacktestPositionHold` for pending POSITION_HOLD accounting, `prepare_market_data` calls `dropna`; `backtesting/executors_simulator/order_executor_simulator.py` MARKET fills at the **first candle timestamp** with `entry_price` at that row close and records `cum_fees_quote=trade_cost*amount_quote`, `CloseType.POSITION_HOLD`; `backtesting_data_provider.py` exposes the price lookup's dangerous default `Decimal("1")` on missing keys. Prior independent Alpha PR **#414** reports a wheel/source binding for this pin, **not rehashed this cycle**; #417 is prior bounded engine evidence. These are verified model primitives, not proof of any candidate backtest or of live-market fill prices.

**Proposed strategy-specific ControllerV2 (not implemented):** on a valid completed daily decision, emit a `CreateExecutorAction` containing `OrderExecutorConfig` with `ExecutionStrategy.MARKET`, connector `binance`, pair `BTC-USDT`, BUY to enter and SELL to fully liquidate, `Decimal("0.001")` base BTC, leverage 1, no limit/maker path. Model a single unborrowed spot book: `FLAT → BUY_PENDING → LONG → SELL_PENDING → FLAT` **only after confirmed fills**. Max one 0.001 BTC long, one pending order, one pair; no short, pyramiding, safety orders, averaging, shared capital, partial exits or concurrent strategies. If a BUY fails/unfills, return flat and require a **future eligible entry bar**; if SELL fails/unfills, retain long with liquidation intent latched and retry only on later valid completed bars until filled. Exit has priority and prevents re-entry that bar; no cooldown after confirmed exit, but re-entry requires a later new eligible completed bar. At sample end, value an open position at the last **real observed close** without inventing a terminal SELL fill.

**Timestamp and fill caveat:** the simulator's same-row-close MARKET execution is an **idealized historical close-price fill convention**, not a promise that an exchange market order submitted after close can obtain that same close. It must be described as a research model, not as source-native Pine fill semantics or live-trading realism. The pinned backtester `prepare_market_data` merges features by timestamp and calls `dropna`; data continuity and completed-close availability must be enforced upstream. Use `terminated_executors_window=None` so the controller can see confirmed daily POSITION_HOLD orders; the default one-hour visible history can otherwise hide an earlier daily fill. Persist a fill-confirmed state ledger, not order-submission guesses. Reject the provider's `Decimal("1")` fallback and any nonfinite or absent actual close.

**Costs/position accounting:** initial unborrowed spot cash **10,000 USDT**, fixed 0.001 BTC; entry requires `cash >= 0.001*actual_close*(1+0.001)`. Research `trade_cost=0.001` per **filled side**, i.e. a modeled 0.1% of actual filled quote notional, not a verified Binance account fee. BUY cash change `-Q*P*(1+f)`; SELL cash change `+Q*P*(1-f)`. Gross matched PnL `Q*(P_sell-P_buy)`; net matched PnL subtracts both `f*Q*P_buy` and `f*Q*P_sell`. The pinned hold ledger tracks gross realized PnL and `cum_fees_quote` separately; do **not** report gross `total_pnl` as fee-inclusive net. Historical simulator assumes close-price fills with no modeled additional slippage/spread/latency; that is **not measured zero slippage**. No funding contract exists for this unleveraged spot derivative; do not infer zero perpetual funding. Actual exchange taker tier, partial fills, precision, minimum notional, slippage and order execution are unverified; no Paper/Testnet/Live claim.

## Six-gate evidence for independent Hermes Auditor

1. **Determinism:** fully specified 9-bar share/entropy formulas, frozen `len/avg/vPR/src/bc/vc` defaults, official percentrank semantics with tie rule, strict thresholds with lattice equivalences, data preconditions and na handling.
2. **Direction:** one BTC-USDT Binance spot long or flat; original source's short leg expressly disabled and mapped to exit as a declared derivative.
3. **Entry/exit/risk:** source-verbatim two-threshold entry/exit; all SL/TP/trailing/time/risk legs expressly disabled, matching the source (which defines none).
4. **State:** fixed 0.001 BTC, pending-fill state, no DCA/pyramiding/concurrency, failed order/retry and re-entry rules, no hidden cooldown.
5. **Pinned engine:** directly inspected pinned `1d` Binance SpotCandles (volume included), MARKET first-row-close OrderExecutor, ControllerV2 action loop, POSITION_HOLD cost/fee netting, timestamp normalization and missing-price/window hazards; prior #414 package binding, no new execution primitive claimed.
6. **Causality:** one warmup definition (bars 0–51 flat, first decision at close of bar 52), completed-close timestamp `T+86400`, `t-44..t` inputs only, no future data, no invented missing candles/prices.

**This PASS frontmatter is a Scout proposal requiring independent exact-head six-gate audit, not self-approval.** It is not a profitability result, source-native Pine equivalence, Qlib parity, Survivor/HB Certified status or trading permission. Before large-scale Qlib screening, validate any **new** strategy/execution primitive with representative Hummingbot/Qlib event-level parity; existing verified primitives may be reused per current policy.

## Evidence and limitations

**Source-reported:** FMZ 365095 publication (ChaoZhang mirror of kocurekc's Shannon Entropy V2) specifies the entropy formulas, the `len/avg/vPR` defaults, the `hvp<vPR` long-interest and `hvp>(100-vPR)` short-interest conditions, and prose describing information/surprise with buy/sell use left to the reader. The mirror-author 2h/15m futures backtest config is context only. These are author facts only and **not** used as derived-strategy performance evidence.

**Independently verified this cycle:** first-party FMZ publication bytes (metadata, description, full embedded Pine) and pinned Hummingbot source paths enumerated above; main/root-count 354 and static README 354 at the captured SHA; dedup search and open research PR inspection; official Pine reference definitions of `percentrank` (previous-values ≤ current), `log` (natural) and sliding `sum`.

**Not independently reproduced:** any candidate Hummingbot or Qlib backtest, venue fee/slippage/funding history, actual fill data, candidate event-level parity, profit/OOS, wheel hash this cycle. The derived 1d spot model is **not** the author's study and may exhibit completely different event sequences. Tail-threshold signals are inherently sparse on daily bars (a statistical-power risk, not an admission defect). With no protective stop, an adverse move can be arbitrarily large until an exit condition fires; missing data can extend exposure.

## Falsification plan

Future authorized research may compare this frozen tail pair against the price-only (`vc=false`) and volume-only (`bc=false`) entropy variants, and against neighboring rank limits; each alteration is a **separately declared derivative**, not an invisible parameter search. Do not run them in this Scout cycle.

## Crypto portability

The author's venue/frame context is not carried as a source-native backtest. This candidate is explicitly BTC-USDT Binance spot 1d with fixed size, no leverage, no short and no funding contract. Different coins, futures, timeframes or BO/SO overlays require separate derivative disclosure and relevant engine/data-model verification; the downstream 7-coin, 1h/4h/1d, 6/6/6 and 3×/5× research campaign is **not** an HB_READY admission requirement.

## Implementation status

not-implemented. No controller code, Qlib executable, backtest, deployment, trading, cron or workflow change was made. An admitted but not materialized strategy follows existing `IMPLEMENTATION_NEEDED` when later selected, not a second eligibility gate.

## Adoption boundary

Research-only; adoption not approved; approval scope research-only. Independent Hermes Auditor GitHub Webhook Review alone owns source-fact remediation, exact-head PASS merge, or NOT_LOSSLESS closure. Scout does not approve, merge, close or update README.

## Related Wiki records

None.

## Sources

- https://www.fmz.com/strategy/365095 — ChaoZhang (code © kocurekc), FMZ publication, 2022-05-23 (modified 2022-05-24).
- https://www.tradingview.com/pine-script-reference/v5/#fun_ta*percentrank — official `percentrank` / `log` / `sum` semantics.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned engine.
- https://github.com/HCH725/alpha-strategy-research/pull/414 — earlier independent package/source binding.
- https://github.com/HCH725/alpha-strategy-research/pull/417 — earlier bounded primitive review.
