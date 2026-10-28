---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Nirvana EMA20/50 BB-width squeeze-release breakout with OBV confirmation and ATR/time exits — independent BTC-USDT spot 1h long-flat derivative"
created: 2026-10-29
updated: 2026-10-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
status: research-only
confidence: medium
source_as_of: 2025-09-18
sources:
  - https://www.tradingview.com/script/DBJue4sR/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Nirvana EMA/BB squeeze release + OBV breakout — independent long-flat derivative

## Provenance

- **Primary public TradingView source:** fkgkekd1122, *Nirvana True Duel*, published **2025-09-18**, stable public script ID **DBJue4sR**, open-source strategy page https://www.tradingview.com/script/DBJue4sR/ . The author's first-party English and Korean descriptions were read directly on **2026-10-29**. The full Pine source bytes, Pine revision digest, default settings and execution flags were **not** obtained; no Pine-code or original-fill parity is claimed.
- **Source-described facts only:** long setup combines **EMA20 > EMA50**, Bollinger Band-width squeeze followed by expansion, **close above the upper band**, and positive OBV flow. A short setup reverses these signs. The description states **ATR × 1.5 stop distance**, partial profit-taking at **1.5–2 times stop distance**, and a maximum-bars-held time exit; it recommends 5m/15m and mentions an 8-hour example. It does **not** pin BB length/deviation, exact squeeze definition, OBV smoothing/flow predicate, ATR estimator/entry fill, partial take-profit sizing, holding-bar limit or cost model.
- **Explicit independent derived strategy, not source-native:** Researcher pins Binance BTC-USDT spot UTC **1h**, LONG/FLAT only; EMA20/50 recursion; BB20/2 population deviation and strict 20-prior-bar minimum-width squeeze; expansion >1.10× prior width; OBV positive over three bars; fixed 0.001 BTC position; **full** close-triggered exit at frozen ATR14 stop or 1.5R target (no partial TP); 48-bar time exit; same-completed-close MARKET historical simulation; hypothetical 0.1% fee per side; cash, no-reentry and fail-closed state. All are **researcher changes** and may materially change trades relative to the original Pine strategy. No original short, intrabar stop, exchange order, partial TP or 5m/15m semantics are represented as preserved.
- **Immutable derivative identity:** `TV:DBJue4sR|fkgkekd1122|2025-09-18|independent-derived-v1-20261029|BinanceSpot-BTC-USDT-UTC1h|EMA20-50-seedfirst|BB20-popstd2|prior20-strict-width-min|width-release-gt1.10|close-gt-upper|OBV3-positive|ATR14-Wilder-close-SL1.5-TP2.25|time48|LONG-FLAT-Q0.001BTC|cash10000USDT|same-completed-close-MARKET|fee0.001-side|warmup120`. Any changed parameter, seed, time, size, market or fill convention is a new derivative.
- **Dedup on current main and open research PRs:** Connected GitHub main snapshot `6c65f27de60c53273a24a2b25361c054efc44d12` has **424** root-level strategy Markdown records and README count **424**. GitHub code searches for `DBJue4sR`, `fkgkekd1122`, `Nirvana`, and the combined EMA/BB/OBV mechanism returned no same-source strategy. All **10** open PRs were inspected by head/title; none uses this source; open PR search for source ID returned none. Related `forven-bb-squeeze-breakout` uses **BB-inside-Keltner** with no EMA20/50+OBV conjunction or frozen ATR/time bracket; `forven-volatility-contraction-breakout` uses ATR-percentile/BB-median contraction with EMA200/RSI, not a prior-minimum BB-width release and OBV; `bollinger-band-breakout-long-midline-exit` lacks squeeze/OBV and uses midline exit. These are materially different rules; not a mere parameter tweak. No exhaustive mathematical-equivalence proof is claimed.

## Economic mechanism

**Source-reported:** trend alignment, volatility contraction/release and OBV confirmation aim to select breakouts. The author's 1.5× ATR stop and profit/time-exit concepts are not independently verified fills or returns.

**Research hypothesis:** simultaneous release from a fresh width minimum and bullish OBV flow might distinguish participation-backed breakouts from generic upper-band crossings. The frozen 1.5R close target is **not** a guaranteed realized 1.5R because the fill is at an observed close, not a stop/limit price. No profitability, Sharpe, OOS, Survivor or HB Certified evidence is claimed.

## Signal — complete independent derived specification (Gates 1–4 and 6)

1. **Feed and clock:** exactly one Binance BTC-USDT **spot 1h** UTC-aligned OHLCV stream. Bar `t` has raw opening epoch `T[t]` divisible by 3600, and data become decision-available only at `E[t]=T[t]+3600`. Require contiguous 3600-second timestamps, finite positive O/H/L/C, `low<=min(open,close)<=max(open,close)<=high`, and finite nonnegative base-BTC volume. A missing/duplicate/incomplete/invalid candle **invalidates the run** before any new action, including if already LONG; never forward-fill, invent a price, silently drop a bar or liquidate at a fabricated price.
2. **EMAs:** `EMA_n(C)[0]=C[0]`; for `t>0`, `EMA_n[t]=(2/(n+1))*C[t]+(1-2/(n+1))*EMA_n[t-1]`, separately for `n=20,50`. Bullish trend iff `EMA20[t]>EMA50[t]`; equality fails. No future smoothing or fitted parameters.
3. **Bollinger bands:** `M[t]=mean(C[t-19..t])`, `SD[t]=sqrt(sum((C[i]-M[t])^2,i=t-19..t)/20)` (**population** SD), `U[t]=M[t]+2*SD[t]`, `L[t]=M[t]-2*SD[t]`, `W[t]=(U[t]-L[t])/M[t]` for `t>=19` and `M[t]>0`. Use full **current completed** bar in these values. An undefined/nonfinite width invalidates signal generation; no alternative estimator or default.
4. **Fresh squeeze and release (researcher-defined):** `squeeze[t-1]` iff `W[t-1] < min(W[t-2],...,W[t-21])` (**strict** new 20-prior-bar width minimum, not a Keltner squeeze); `release[t]` iff `squeeze[t-1] && W[t]>1.10*W[t-1]`. This is one-bar release after a fully observed squeeze. Equal width fails; never inspect `t+1` or retrospectively repaint a squeeze. Require all 22 widths to exist.
5. **OBV:** `OBV[0]=0`. For `t>=1`, `OBV[t]=OBV[t-1]+V[t]` if `C[t]>C[t-1]`, subtract `V[t]` if `C[t]<C[t-1]`, otherwise unchanged. **Researcher-defined positive-flow gate:** `V[t]>0 && OBV[t]>OBV[t-1] && OBV[t]>OBV[t-3]`. This is a three-bar net-positive flow plus current up-volume, **not** an assertion of the author's unspecified OBV variant.
6. **ATR14:** `TR[0]=H[0]-L[0]`; for `t>=1`, `TR[t]=max(H[t]-L[t],abs(H[t]-C[t-1]),abs(L[t]-C[t-1]))`. Seed `ATR[13]=mean(TR[0..13])`; thereafter `ATR[t]=(13*ATR[t-1]+TR[t])/14`. An entry requires finite `ATR[t]>0`; freeze ATR at the entry fill bar, never use later ATR to move brackets.
7. **Warmup:** first **120 consecutive fully completed valid bars** are indicator-only, FLAT, with no orders; first eligible decision at zero-based `t=120`, requiring the prior 120 bars plus the current completed bar. This exceeds EMA50, BB20, 21-bar squeeze history, OBV3 and ATR14 needs. Insufficient buffer, missing bars or an incomplete current bar aborts; no truncated/whole-sample reseeding.
8. **Entry:** when FLAT, no pending order and `t>=120`, require `release[t] && EMA20[t]>EMA50[t] && C[t]>U[t] && V[t]>0 && OBV[t]>OBV[t-1] && OBV[t]>OBV[t-3] && ATR[t]>0`. All comparisons strict. On that **completed** bar submit exactly one modeled MARKET BUY of `Q=Decimal("0.001") BTC` at its actual `C[t]`; only after confirmed full fill set `entryPrice=C[t]`, `entryBar=t`, `R=1.5*ATR[t]`, `stop=entryPrice-R`, `target=entryPrice+1.5*R`. If initial cash cannot cover Q×C[t] plus modeled fee, do not trade or queue a stale signal.
9. **Exit and precedence:** while LONG, evaluate **only on a subsequent completed bar** `u>entryBar`: (a) `C[u]<=stop`; else (b) `C[u]>=target`; else (c) `u-entryBar>=48`. On first true condition submit exactly one full-Q MARKET SELL at **actual C[u]**. Reason priority is stop, target, then time; never fill at the threshold or intrabar high/low. If all false, HOLD. Stop/target are frozen **close-observed reference levels**, not intrabar protective exchange orders; actual loss can exceed R. No EMA/OBV discretionary exit.
10. **Position/state:** initial cash `Decimal("10000") USDT`, BTC=0; exactly FLAT or LONG(0.001 BTC), one pending-or-confirmed action per completed bar. Use the simulator's **confirmed full fill** to update a strategy-owned cash/BTC/entry/fee ledger. Reject missing, partial, stale, failed, inconsistent or nonfinite fills and abort instead of assuming success. After SELL return FLAT; no same-bar re-entry, and a later new independently qualifying squeeze-release event is required for another BUY. Ignore buy signals while LONG and exit conditions while FLAT. No short, leverage, borrow, margin, liquidation, pyramiding, DCA, safety orders, compounding, concurrency, cooldown beyond one action/bar, maker/limit, intrabar execution, trailing, extra stop/target, partial TP, or forced final liquidation.
11. **End-of-data:** if still LONG on the final completed bar, report base inventory and mark-to-market at that **observed** close separately from realized PnL. Never synthesize a terminal sell, future bar or future gap.

## Required data

One Binance spot BTC-USDT UTC 1h OHLCV feed, including real open timestamps, with a **validated contiguous pre-decision buffer** of at least 120 completed bars. Volume is native Binance base-asset candle volume, not external futures flow. No higher/lower timeframe, synchronized second asset, order book, tick, ML model, future pivots, corporate action, exchange session or funding feed. The original 5m/15m suggestion is not a required admission whitelist.

## Execution assumptions — pinned Gate 5

- **Pinned identity and source inspection:** Hummingbot package label **20260920**, `hummingbot/VERSION=dev-2.17.0`, immutable `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. Connected GitHub reads on **2026-10-29** verified `hummingbot/VERSION`, Binance spot candle interval constants and REST parsing, `BacktestingDataProvider`, `BacktestingEngineBase`, `OrderExecutorSimulator`, and `OrderExecutorConfig`. Independently reviewed merged Alpha PR **#414** reports wheel SHA256 `ea5a929c52095bc03fd34f5b3fb2fbfef068f7ea880af6c38290d1ddb729a148` and 902/902 Python-file byte identity to the source commit; this Scout did **not** rehash the wheel, so that binding remains prior evidence, not a fresh claim.
- **Actual data path:** `BinanceSpotCandles` supports `1h`, maps REST Kline row[0] to the **open** timestamp and row[1..5] to OHLCV. `BacktestingDataProvider.get_candles_feed` requests `start_time - max_records*interval`, but `get_candles_df` later trims to `start_time..end_time`; controller must inspect actual raw buffer **before** trimming and reject gaps/short history. A configured max_records or a returned DataFrame is not proof of contiguous completed history.
- **Controller and timestamp semantics:** `BacktestingEngineBase.prepare_market_data` joins controller features with `merge_asof` on raw candle-opening timestamps and overwrites row `timestamp` with the candle-open value. Precompute only causal complete-bar features, keyed to the matching **open timestamp T[t]** for that bar; logical `feature_available_at=decision_at=historical_fill_effective_at=E[t]`. The simulator's row/fill timestamp label T[t] must **not** be interpreted as access to that bar's close at its opening time. Same-completed-close MARKET fills are a bounded idealized historical convention, not live-guaranteed post-close execution. The strategy-specific controller is **not implemented** and must enforce the exact above signal/state/clock rules; a generic executor name is not implementation evidence.
- **Actual executor path:** `OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),position_action=OPEN/CLOSE,execution_strategy=MARKET,price=None,leverage=1)`. The pinned `OrderExecutorSimulator` fills MARKET at the **first supplied actual candle close**, records `filled_amount_quote=Q*close`, `cum_fees_quote=trade_cost*filled_amount_quote`, and terminates `CloseType.POSITION_HOLD`. `BacktestingEngineBase.simulate_execution` processes controller `CreateExecutorAction`s; `BacktestPositionHold` nets BUY/SELL base inventory and reports matched gross PnL and fees separately. The controller must reconcile **all confirmed executor fills** with its own state; a terminated-executor display window is not a complete inventory ledger.
- **Cost, precision and economic limits:** `run_backtesting(trade_cost=0.001)` fixes **hypothetical 0.1% per filled side**. BUY cash debit `Q*P*(1+0.001)`, SELL credit `Q*P*(1-0.001)`; realized net round-trip PnL `Q*(P_sell-P_buy)-0.001*Q*(P_buy+P_sell)`. Track fee-inclusive cash/equity separately from gross `BacktestPositionHold.realized_pnl_quote`. Compare actual simulated filled base/quote/fees against the Decimal ledger, tolerate at most 1e-9 BTC base and 1e-8 USDT quote/fee rounding; otherwise abort. Explicitly prohibit `BacktestingDataProvider.get_price_by_type`'s `Decimal("1")` missing-price fallback: use only a validated real candle close. No separate MARKET slippage model is applied here (idealized **modeled** zero additional slippage, not observed zero spread/latency). Spot funding, futures margin/liquidation and borrow costs are **not applicable**; do not mislabel futures funding as zero. Real exchange min-notional/lot/tick precision, fee tier, latency, slippage and partial fills are **not verified**, and no live tradability is claimed.
- **Capability boundary:** only one spot 1h OHLCV feed, deterministic controller predicates, existing MARKET historical-close fill, fee and position-hold primitives are needed. No new intrabar, next-open, maker, perpetual, cross-asset or non-OHLCV capability is assumed. Reuse prior independently reviewed representative pinned primitive evidence (#414); this Scout executed **no** strategy backtest, and new strategy-specific controller code and representative Qlib/Hummingbot event-level parity remain downstream engineering work before mass screening of any unverified path.

## Six-gate HB_READY proposal (independent audit required)

1. **G1 reproducible:** EMA20/50 seed, BB20 population variance, strict prior-20 width minimum, 1.10 release, OBV3, Wilder ATR14, strict ties and frozen stop/target are explicit.
2. **G2 direction:** Binance BTC-USDT spot LONG/FLAT only; original short disabled and disclosed.
3. **G3 entries/exits/risk:** exact all-of-five entry, frozen close-based stop 1.5ATR, full 1.5R target and 48-bar time exit with explicit priority; no hidden stop, partial exit or Hummingbot defaults.
4. **G4 state:** 0.001 BTC, 10,000 USDT, full-fill ledger, one position/order per bar, no DCA/pyramiding/concurrency, no same-bar re-entry, no compounding.
5. **G5 pinned engine:** directly inspected pinned Binance spot 1h candle, controller/backtest join, MARKET close simulator, POSITION_HOLD, fees, precision/clock limitations and missing-price fallback; only supported bounded path is claimed.
6. **G6 causality:** 120 pre-decision complete-bar warmup, strictly prior squeeze minimum, current completed-bar release and indicators, logical end-of-bar decision/fill, no future bar or retrospective signal.

`hb_ready_status: PASS` is **the Scout's proposed research admission claim only**, not an independent Hermes Auditor verdict, Pine lossless conversion, backtest result, Qlib parity, survivor status or trading authorization.

## Evidence and limitations

- **Source-reported only:** TradingView fkgkekd1122 publication dated 2025-09-18, directly read 2026-10-29, supplies EMA20/50, BB squeeze/release breakout, OBV positive flow, ATR1.5 stop, partial 1.5–2R TP and time-exit concepts. No source performance metrics are reproduced.
- **Independently reproduced for this strategy:** none. No original Pine replay, Hummingbot/Qlib event run, IS/OOS, actual fee or fill observation, Survivor or HB certification. Direct pinned engine **source-path inspection** and historical independent engine binding are capability evidence, not strategy execution.
- **Negative evidence:** Pine source/revision and original BB/OBV/squeeze/TP/time defaults were inaccessible. Researcher-defined BB20/2, minimum-width release, OBV3, ATR seed, 48 bars, full target, spot 1h, cost, same-close fill and position management are disclosed changes, **not** source-native facts. Actual stop/target fills can overshoot because only close prices are modeled.
- **Falsification plan (separately authorized later):** compare exact width-minimum release and OBV3 events to raw BB upper crosses; verify EMA/BB/OBV/ATR seeds, boundary ties, 48-bar time exit, entry-frozen brackets, missing-bar abort, same-close effective clock, full-fill ledger and fee-inclusive equity. Verify representative Qlib/Hummingbot event-level parity before large-scale screening of any unverified execution path. No backtest in this Scout.
- **Adoption boundary:** research-only, implementation_status not-implemented, adoption not-approved, approval_scope research-only. Independent Hermes Auditor GitHub Webhook Review alone owns source-fact remediation, exact-head PASS merge or NOT_LOSSLESS close; the existing signed webhook receiver alone owns post-merge README count reconciliation. Scout does not merge, approve, close, deploy, trade, backtest or alter workflows.

## Sources

- https://www.tradingview.com/script/DBJue4sR/ — fkgkekd1122, *Nirvana True Duel*, 2025-09-18; first-party page read 2026-10-29.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned Hummingbot source inspected via connected GitHub.
- https://github.com/HCH725/alpha-strategy-research/pull/414 — prior independent pinned wheel/source and MARKET-close primitive evidence.
