---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "FXEngineering Higher-High dip-breakout with SMA20/MACD/signal slope gates and stoch-%K-fall exit — independent BTC-USDT spot 1h long-flat derivative"
created: 2026-10-29
updated: 2026-10-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
  - derived
status: research-only
confidence: medium
source_as_of: 2026-10-29
sources:
  - https://github.com/hasnocool/tradingview-pine-scripts/blob/69969aeaf271b2f7b5a7632a1bde43069a0cbe26/Higher%20High%20-%20Lower%20Low%20Strategy.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FXEngineering Higher-High dip-breakout — independent long-flat research derivative

## Provenance

**Primary public source (immutable GitHub, read end to end):** `hasnocool/tradingview-pine-scripts`, file `Higher High - Lower Low Strategy.pine`, embedded strategy title *Higher High / Lower Low Strategy*, credited author **FXEngineering**, `//@version=4`, `strategy(title='Higher High / Lower Low Strategy', shorttitle='Initial Balance Strategy')`, `overlay=true`. File is 3,339 bytes / 87 lines; SHA256 `f1094e5f041c2f93a30687afd53bde06de55bb7f5ad23ef52c0c22d9755d2b43`, byte-identical at repo HEAD `69969aeaf271b2f7b5a7632a1bde43069a0cbe26` (2024-09-18) and at file commit `e031cab2819a7d56fb8bb9d000252f51439986e2` (2023-09-02, `Initial Upload Of Data`). Header prose: *"a very simple trend following strategy for Day Trading. The premise is to follow the Moving Average for the trend direction and buy/sell the dips and blips in the trend"*; long leg: *"In an uptrend, when the candle action offers a 'dip', or a lower high, the strategy will then buy on the close of the candle that breaks the high of the previous candle."*

**Source-native facts (defaults, all adopted):** `longOnly=true`, `useMACD=true`, `useSignal=true`, `periodA=20` (trend SMA), `periodK=5` (%K), `fast_length=5`, `slow_length=20`, `signal_length=30`, hardcoded `smoothD=3`, `smoothK=2`. Long entry when `high[2]>=high[1]` AND `high>high[1]` AND `SMA20` rising AND (`macd>macd[1]`) AND (`signal>signal[1]`), with `k,d,macd,signal` non-`na`, `month>=10`, `year>=2020`, flat book (`strategy.order("HH_LE", strategy.long, when=strategy.position_size==0)`). Long exit when `k<k[1]` while in position (`strategy.order("HH_SX", strategy.short, when=strategy.position_size!=0)`), where `k=sma(stoch(close,high,low,5),2)-50`, `d=sma(k,3)` (na-guard only), `macd=ema(close,5)-ema(close,20)`, `signal=ema(macd,30)`. No `pyramiding` argument (Pine default 0), no `process_orders_on_close`, no commission/fee/slippage/margin block, no stop/target/trailing/time-exit leg anywhere (verified by full-file read). The short-side block (lines 81–85) is dead code under the default `longOnly=true`.

**EXPLICIT INDEPENDENT DERIVATIVE; NOT source-native/lossless.** Researcher pins Binance BTC-USDT spot `1h` (source pins no venue/timeframe); keeps `longOnly=true` (source default) and drops the dead short block; drops the `month>=10 AND year>=2020` backtest-window gate as a research artifact; replaces next-tick market orders with completed-bar decisions and next-completed-bar-close MARKET fills; pins SMA-seeded classic EMA recursion, a flat-range stoch guard, a 100-bar warmup, single-pending-action bookkeeping, 0.001 BTC size, 10,000 USDT cash with admission guard, and 0.1% hypothetical fee per side. All are researcher rules, not alleged source facts. The `HH_SX` reversal-vs-close ambiguity in Pine is resolved by the predeclared long-only flat-closing SELL.

**Frozen identity:** `GH:hasnocool:f1094e5f:FXEngineering:HHLL-v4 | derived-v1:2026-10-29 | BinanceSpot:BTC-USDT:UTC1h | HHdip:H[t]>H[t-1]&H[t-2]>=H[t-1] | SMA20↑ & MACD(5,20)↑ & SIG30↑ | exit:k=SMA2(stoch5)-50:k[t]<k[t-1] | LONG-FLAT:Q0.001BTC:cash10000USDT | signal-E[t]:fill-next-E[t+1]-MARKET-row-close | fee0.001:W100:no-DCA:longOnly`. Any change to this identity is a different derivative.

**Dedup (prewrite, main `c8fc48af232ba368e8b43d8c814fd875669de05b`):** main holds 438 root-level strategy records and README count 438. Case-insensitive searches for `FXEngineering`, `HH_LE`, `HH_SX`, `Higher High Lower Low`, `higherhigh` return zero records of this source — the single `higher high` hit anywhere is a fencing phrase (`not ... higher high`) inside `forven-three-bar-reversal`'s own prose, a different three-lower-lows washout-reversal record with zero indicators (fenced below). Stoch-gated cousins differ in construction: `ChuckBanger Aroon14 CMO14/SMA9 crossover` (CMO cross, Aroon gate), `Forven stochastic K20 recross dual-exit` (%K level recross with dual exits), `Alorse StochRSI K/D oversold cross with Supertrend and EMA200` (K/D cross, Supertrend regime), `freqtrade-cofibit StochFast EMA-rail ADX-gated` (fast-stoch/rail/ADX). Structure cousins differ: N-bar Donchian maxima, 2–2 lag-confirmed fractal levels (`QuantifiedTrader Fractal Breakout`, `FMZ GBS TOP BOTTOM`), inside-bar/engulfing single-bar patterns. No pool record combines a 2-bar higher-high dip-breakout with SMA20/MACD/signal triple-slope gates and a smoothed-stoch-%K-fall exit. Open `research/*` PRs (#593, #353, #350, #331, #304, #251, #92, #89, #63, #49, #48) carry none of this source, author, file, or construction. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism
### Source-reported
Follow the SMA20 trend and buy the dip: after a lower-high pause, the close of the candle that breaks the prior candle's high re-confirms trend resumption; MACD/signal slope agreement filters counter-trend breaks; the trade ends when short-horizon momentum (%K) rolls over. The author ships no expectancy, cost, or execution trace.
### Research interpretation
A local 2-bar swing break with three rising slow filters selects with-trend resumption points while refusing extended vertical entries (MACD/signal must still be rising, not merely positive); the %K-fall exit cuts the long on the first completed-bar momentum downturn without any protective stop — a long can therefore sustain severe losses, and the exit is **not** a guaranteed stop or live fill.

## Signal

**Gate 1 — deterministic data and preprocessing.** One Binance BTC-USDT Spot UTC `1h` series indexed t=0,1,... by Binance candle **opening** timestamp T[t], T[t+1]-T[t]=3600 s. Require finite positive O,H,L,C, H>=max(O,C), L<=min(O,C), finite V>=0, strictly ordered unique complete candles; reject gaps, duplicates, incomplete bars, forward fills, missing prices, bad precision, synthetic data. Completed bar t is available only at E[t]=T[t]+3600. All features float64 in chronological order; no fitting, no external feeds.

**Trend SMA:** SMA20[t]=mean(C[t-19..t]); rising ⟺ SMA20[t]>SMA20[t-1].

**Classic EMAs (researcher-pinned SMA seed):** α(n)=2/(n+1). EMA_n seed = mean of first n closes of its input series; thereafter EMA[t]=α·x[t]+(1-α)·EMA[t-1]. EMA5/EMA20 on closes; macd[t]=EMA5[t]-EMA20[t]; signal[t]=EMA30 recursion on the macd series (seed = mean of first 30 macd values). Rising ⟺ strict `>` versus prior bar. This seeding is the **declared derivative's** pin, not a claim about Pine `ema` internals.

**Smoothed stochastic:** LL5[t]=min(L[t-4..t]), HH5[t]=max(H[t-4..t]); if HH5[t]==LL5[t] the bar yields no raw value (flat-range guard, researcher-declared); else raw[t]=100·(C[t]-LL5[t])/(HH5[t]-LL5[t]). k[t]=mean(raw[t-1..t])-50, requiring both raws valid. `d` is computed as mean(k[t-2..t]) for the na-guard only and gates no order, exactly as in source.

**Entry (level-based, source-faithful):** at completed t>=100, if FLAT with no pending action, all of k,d,macd,signal valid at t, and `H[t-2]>=H[t-1]` AND `H[t]>H[t-1]` AND SMA20 rising AND macd rising AND signal rising → queue BUY. Level semantics match source (`strategy.order when position_size==0` fires on any qualifying bar); pending actions suppress re-queueing; the signal bar's own qualification is consumed by the queued action.

**Exit:** while LONG and only on a bar strictly after the confirmed entry fill bar, if k[t] and k[t-1] valid and k[t]<k[t-1] → queue SELL (full size, flat-closing, never opening a short). Stop-loss, take-profit, trailing, time exit, opposite-signal exit, and auto-reversal are **disabled** (source ships none). No cooldown; re-entry re-arms on any later qualifying bar once FLAT.

## Required data

Only the one complete Binance Spot 1h OHLCV stream, with validated actual closes for every decision, fill, and mark. First eligible signal t=100 (covers SMA20 slope, stoch windows, EMA20 seed, and EMA30-of-macd seed with margin). No order-book, funding, higher-timeframe, multi-asset, session, or calendar inputs — the source date-window gate is dropped, not modeled.

## Execution assumptions

**Gates 2–4:** unleveraged Binance Spot BTC-USDT LONG/FLAT; shorts, margin, perpetuals, borrowing disabled (source default `longOnly=true`). One fixed BUY/SELL of Decimal("0.001") BTC, initial 10,000 USDT, zero BTC; single position and single pending action; no DCA, safety orders, pyramiding, compounding, partial exits, extra stops/targets, or hedges. State `FLAT -> BUY_PENDING -> LONG -> SELL_PENDING -> FLAT`. Pending actions suppress all fresh signals. Exit checks only against confirmed LONG; k-fall during BUY_PENDING is ignored (no open position, mirroring source `position_size!=0`). Failed, missing, partial, duplicate, or precision-invalid fills abort research rather than assuming execution; SELL failure retains LONG with latched exit intent, retrying only against the next real complete row. BUY requires quote cost within cash (cash never negative); if no next complete row exists the pending action stays unfilled and held BTC is marked at the last verified close — never a fabricated terminal exit.

**Historical event clock:** signal detected only after completed t at E[t]; latched action fills on completed t+1 at the pinned Hummingbot OrderExecutor `MARKET` simulator's **first supplied row's actual close C[t+1]**. Controller emits on t+1 from t's latched decision only; never on signal bar t. Raw Binance/engine row timestamps are **opening** T[t+1]; annotate economic completion E[t+1]=T[t+1]+3600 separately. Historical close-price simulator convention, **not** a live-fill claim. Entry fill bar cannot trigger exit; exit fill bar cannot trigger entry.

**Hypothetical costs/accounting:** trade_cost=0.001 per filled side of quote notional, not an observed Binance fee; no fabricated funding/spread/slippage. BUY at P costs 0.001·P·1.001 USDT for 0.001 BTC; SELL at S credits 0.001·S·0.999 USDT. Net matched PnL = 0.001·(S-P)-0.001·0.001·(P+S). Reconcile executor fills plus separate fee ledger against quote cash and base inventory; never present gross as net. Spot has no funding/margin/liquidation leg. Real impact, slippage, latency, partials are limitations, **not measured zero**.

## Evidence
### Source-reported
Immutable GitHub file (verified byte-identical at two commits) directly states the HH dip-breakout entry conjunction, the triple-slope filter defaults, the %K-fall long exit, long-only default, zero position size default, and the complete absence of stop/target/trailing/commission legs. No source-reported returns adopted.
### Independently reproduced
**No backtest or Qlib/Hummingbot run performed.** Gate 5 **static pinned-source inspection**: package baseline `20260920` per Alpha contract; `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` with `hummingbot/VERSION=dev-2.17.0` — **live-verified this cycle** via raw fetch (VERSION text `dev-2.17.0`; candles-constants blob `6d505dff42b60b356931df13eeeecd1e28b426f9`, 993 bytes, `1h` in the Binance Spot interval list). Remaining engine blobs are previously evidenced in the admitted record of Alpha PR #603 (merged 2026-10-29), cited here as prior evidence, not rehashed: backtesting engine `7d1e552dd7ee62df4f83f10950b8d593cd1106e6` (per-row `update_state` → `determine_executor_actions` → `simulate_executor` with a strategy-specific ControllerV2 carrying the prior completed-bar signal into the next row); OrderExecutor simulator `3b4e82e91896db9074295ca2a8a087dde2499eab` (MARKET fills at first supplied **row close**, `filled_amount_quote=amount*close`, `cum_fees_quote=trade_cost*amount*close`, POSITION_HOLD termination); OrderExecutorConfig `67715e3d14a1edf636defa95a7bbe5c73b8cff90` (connector `binance`, `BTC-USDT`, BUY/SELL, Decimal amount, OPEN/CLOSE, MARKET, leverage 1); data provider `e3d3e087b4da7c0381fac9621d1a04dcb8de81cf` (may return `Decimal("1")` for absent price — **forbidden** here for any fill/mark; abort instead). Wheel/source mapping per Alpha PR #414. One-stream 1h OHLCV suffices; interval listing alone is not execution proof. `terminated_executors_window=None` or equivalent persistent fill ledger required. Validate real Binance trading rules (lot size, min notional, precision) before simulation; reject rather than resize 0.001 BTC silently. Pinned `dropna` preparation must not conceal raw gaps; validate continuity first.
### Negative evidence
No Pine byte-execution comparison, no original backtest reproduction, no fee/latency/fill measurement, no wheel rehash this cycle, no Qlib parity, no performance claim. Closest pool cousins fenced as different constructions: `forven-three-bar-reversal` (three-lower-lows descent, zero indicators, fresh-lower-low exit — opposite pattern, no filters); N-bar Donchian maxima (absolute lookback extremes, not a 2-bar swing); 2–2 confirmed fractal levels (lag-confirmed pivots, not slope-gated swings); %K-level/K-D-cross stoch records (level/cross triggers, never a slope-fall exit); MACD line-cross/zone records (cross/level, never triple-slope agreement). This is an admission **proposal** pending independent Auditor, not proof of source-native equivalence or live readiness.

## Falsification plan

Auditor must verify the immutable file bytes/hash, author/title/version, default inputs, entry/exit predicates, dead short block, and coded absence of risk/cost legs; recompute SMA20 slope, classic-EMA-seeded MACD/signal, and SMA2-smoothed stoch %K on synthetic bars including the flat-range (HH==LL) guard; inspect completed-bar ordering, fill timestamps, ledger, fees, abort paths, pending suppression, entry-fill-bar exit lockout, and no future leakage. One representative Hummingbot↔Qlib event-level parity proof precedes any mass Qlib screening of this execution path. IS/OOS profitability is later work, not an HB_READY gate.

## Crypto portability

Rules use relative price geometry and normalized oscillator slopes, no equity session calendar; only Binance BTC-USDT spot 1h is claimed. Other symbols, futures, or intervals are new explicitly pinned identities, not assumed.

## Limitations

No stop/target/trailing/time-exit protection; the %K-fall exit can lag badly in vertical drops. Next-complete-close fills differ from the source's next-tick markets. Pine `ema` seeding and the `HH_SX` reversal-vs-close edge are resolved by declared derivative pins, not asserted as Pine facts. Real costs, live behavior, original returns, and wheel rehash are unverified. No invented zero funding/slippage. HB_READY PASS is not profitability, parity, or trading authorization.

## Implementation status

`not-implemented`: strategy-specific controller/ledger is specified but not deployed. Static Gate 5 compatibility is a bounded claim under the pinned source/previous wheel mapping; independent Hermes Auditor owns exact-head admission review. No Hummingbot/Qlib backtest, deployment or trading performed.

## Adoption boundary

`research-only`, `adoption: not-approved`, `approval_scope: research-only`. PASS frontmatter is a Scout six-gate admission claim awaiting independent review, **not** HB Certified, Qlib parity, profitability, or Paper/Testnet/Live authorization.

## Related Wiki records

None asserted; HH-swing, MACD-slope, and stoch-%K families on main use materially different triggers and exits as fenced above.

## Sources

- FXEngineering, *Higher High / Lower Low Strategy* (`//@version=4` Pine strategy), via hasnocool/tradingview-pine-scripts, pinned blob (verified identical at HEAD and file commit): https://github.com/hasnocool/tradingview-pine-scripts/blob/69969aeaf271b2f7b5a7632a1bde43069a0cbe26/Higher%20High%20-%20Lower%20Low%20Strategy.pine
- File commit: https://github.com/hasnocool/tradingview-pine-scripts/commit/e031cab2819a7d56fb8bb9d000252f51439986e2 ; repo HEAD: https://github.com/hasnocool/tradingview-pine-scripts/commit/69969aeaf271b2f7b5a7632a1bde43069a0cbe26
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Alpha contract: `README.md` and `.github/HB_READY_REVIEW.md` on main SHA `c8fc48af232ba368e8b43d8c814fd875669de05b`.
