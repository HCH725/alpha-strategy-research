---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "TradingView mfsz2015 Supertrend-flip and price-Stochastic K/D confirmation — independent BTCUSDT spot 4h long-flat derivative"
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
  - https://www.tradingview.com/script/cU0Z0nuY/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Supertrend bearish-to-bullish flip with Stochastic K/D cross — independent long-flat derivative

## Provenance

- **TradingView primary source:** [Supertrend + Stochastic Strategy](https://www.tradingview.com/script/cU0Z0nuY/), stable script ID `cU0Z0nuY`, author **mfsz2015**, first published **2026-01-24** (page date “Jan 24”, 2026 as observed 2026-10-25), author-labeled **VERSION 1.0**, **Pine Script v5**, published as a **public open-source *indicator*** rather than a trade-executing Pine `strategy()`. Page and author-written rules inspected 2026-10-25.
- **Source-native facts visible in the author's description:** a BUY visual signal requires a bearish→bullish Supertrend change, close above the Supertrend line, price-Stochastic K crossing above D, and a minimum inter-signal distance. SELL is the mirror bullish→bearish change, close below the line, K crossing below D and distance. Defaults described: Supertrend ATR period 10, multiplier 3.0; Stochastic raw %K length 14, K SMA smoothing 3, D SMA smoothing 3; oversold/overbought 20/80; minimum candles between visual signals 5. “Strong” signal badges are visual classifications, not separately established order rules. The page suggests entering at a signal-bar close and exiting on opposite signals or discretionary targets/stops, but specifies no numeric protective stop/target.
- **Source-access boundary:** the readable public page does **not** expose a byte-verifiable full Pine source listing, exact Supertrend recurrence/ATR initialization, zero-range Stochastic treatment, whether the five-bar distance is global or side-specific, Pine strategy order settings, position accounting or fills. **No source-native lossless trading-system claim is made.** Do not claim that an indicator's visual alerts are backtested orders.
- **Immutable research identity:** `TV:cU0Z0nuY:2026-01-24:author-v1.0:description-2026-10-25:derived-ST10x3-Stoch14-3-3-5bars:BTCUSDT-spot-4h-longflat-v1`. This is a frozen researcher specification anchored to the primary-source identity and as-of snapshot, **not** a claim of an immutable Pine source commit.
- **All researcher-defined adaptations, not silently attributed to the author:** exact recursive Supertrend and Stochastic edge-case formulas, 100-bar initialization/warmup, long/flat-only spot trading, one 0.001 BTC position, the entry-only five-bar cooldown interpretation, exit on *any* bearish Supertrend flip rather than waiting for the full conjunctive SELL badge, bar-close historical MARKET fills, explicit simulated cash/fees and disabled risk legs. These are assessed as this independent derivative's rules; they do not retroactively establish source-native semantics.
- **Dedup snapshot:** current `main` SHA `18dfc58ab9c67b3cac6d622609e1b0ee455b827f` (318 root-level strategy records and README counter 318, rechecked before branch creation 2026-10-25). Searches for `cU0Z0nuY` and `mfsz2015` found no matching `main` file or open research PR. Related `alorse-stochrsi-supertrend-ema200-long-20261016.md` uses **StochRSI**, EMA200 and a *bullish Supertrend state* gate rather than a **price-Stochastic crossover on the same bar as the Supertrend direction flip**; `slow-stochastic-14-3-regime-recross-two-sided-btcusdt-1d-2026-10-12.md` uses 20/80 stochastic rails with SMA200, no Supertrend; neither has materially identical normalized events. Open `research/*` PRs checked via current GitHub list; none cites this source.

## Economic mechanism

### Source-reported

The publisher combines a trend-regime transition (Supertrend) and contemporaneous price momentum confirmation (Stochastic %K/%D). A five-candle signal-spacing option suppresses clustered visual alerts. The source's qualitative “strong” badges use 20/80 zones. No reproducible source backtest PnL, Sharpe, fee model or trade ledger is provided by the inspected description.

### Research interpretation

The *derived* strategy tests whether a freshly bullish volatility-band regime plus an independently bullish Stochastic cross yields a sufficiently selective long entry, then leaves at the first bearish Supertrend transition. This entry conjunction is materially different from an always-bullish-regime Stochastic entry or an EMA trend crossover. Neither profitability nor a particular trade frequency is presumed; simultaneous events may be rare.

## Signal

**All equations and conventions below are researcher-defined, frozen, causal, and part of this independent derivative.** The primary source supplies the indicator families, default lengths, visual conjunction and cooldown *concept*, not byte-verified Pine internals.

- Universe: **Binance BTC-USDT spot**, one pair, **4h** bars, `H[t], L[t], C[t]` from completed, contiguous Binance spot OHLCV. Use no higher timeframe, other assets, tick, order book, open interest, mark/index or external data. Bar index `t=0` is the first bar of the **frozen input dataset**. A missing/duplicate 4h interval, non-finite price, `H<L`, `C` outside `[L,H]`, or non-positive `C` makes the run **invalid**; never fabricate or forward-fill a price.
- True range: `TR[0]=H[0]-L[0]`; for `t>0`, `TR[t]=max(H[t]-L[t], abs(H[t]-C[t-1]), abs(L[t]-C[t-1]))`. `ATR10[9]=mean(TR[0..9])`; for `t>=10`, `ATR10[t]=(9*ATR10[t-1]+TR[t])/10` (Wilder RMA, *not* SMA ATR after seed).
- Supertrend bands, from `t>=9`: `basicU[t]=(H[t]+L[t])/2 + 3*ATR10[t]`; `basicL[t]=(H[t]+L[t])/2 - 3*ATR10[t]`. Seed `U[9]=basicU[9]`, `Lband[9]=basicL[9]`, `direction[9]=BEAR`, `ST[9]=U[9]`. For each `t>=10`:
  - `U[t]=basicU[t]` if `basicU[t]<U[t-1]` OR `C[t-1]>U[t-1]`; otherwise `U[t]=U[t-1]`.
  - `Lband[t]=basicL[t]` if `basicL[t]>Lband[t-1]` OR `C[t-1]<Lband[t-1]`; otherwise `Lband[t]=Lband[t-1]`.
  - If `direction[t-1]=BEAR`, set `direction[t]=BULL` iff `C[t]>U[t]`, else BEAR. If `direction[t-1]=BULL`, set `direction[t]=BEAR` iff `C[t]<Lband[t]`, else BULL. Strict inequalities: equality preserves the previous direction. `ST[t]=Lband[t]` in BULL, otherwise `U[t]`.
- Price-Stochastic (not StochRSI): `HH14[t]=max(H[t-13..t])`, `LL14[t]=min(L[t-13..t])`. `rawK[t]=100*(C[t]-LL14[t])/(HH14[t]-LL14[t])` for `t>=13`; if the denominator is **exactly zero**, define `rawK[t]=50` (explicit derivative convention; the publisher does not document it). `K[t]=SMA3(rawK)[t]`; `D[t]=SMA3(K)[t]`. Missing pre-warmup values never trigger crosses. Bullish K/D cross at `t`: `K[t-1]<=D[t-1] AND K[t]>D[t]`; exact equality at `t` is not a cross.
- **Warmup and seed:** calculate the full chain from the frozen dataset's first bar, but forbid all trade decisions before `t=100` (101st *completed* 4h bar); no full-sample normalization or rolling-window use of future observations. Seed is deterministic and must be held fixed when comparing engines; data start and all parameters are part of the frozen identity.
- **Entry event:** `FLAT` AND `direction[t-1]=BEAR` AND `direction[t]=BULL` AND `C[t]>ST[t]` AND bullish K/D cross AND (`last_entry_index` unset OR `t-last_entry_index>=5`). The five-bar condition is **researcher-defined entry cooldown**; it is not claimed to be the publisher's exact global visual-signal-spacing implementation. Both “strong” and ordinary source BUY badges are eligible; 20/80 badge classification is not an extra entry filter.
- **Exit event (explicit derivative):** `LONG` AND `direction[t-1]=BULL` AND `direction[t]=BEAR`, **regardless of Stochastic**. This is an intentionally more prompt risk exit than the author's full visual SELL conjunction. If no bearish flip occurs, the long can remain open indefinitely; this is a declared risk, not a hidden stop.
- **Action priority:** exit first, entry second, otherwise hold. Both flip directions cannot occur on one completed bar. Never reverse to short. A repeated entry while LONG is ignored; an exit while FLAT is ignored. A completed bar can create at most one fill. If exit occurs, no same-bar re-entry. No position is opened on the first available bar.
- **Position machine:** initial `FLAT, cash=1000 USDT, base=0, last_entry_index=unset`. A valid FLAT entry with sufficient quote cash buys **Q=0.001 BTC**; record `last_entry_index=t` only after its modeled full fill and transition to `LONG(Q)`. If `cash < Q*C[t]*(1+0.001)`, skip the entry with no signal timestamp update; no borrowing. A valid exit sells the held **Q** and returns to FLAT; all exits bypass cooldown. No DCA, safety orders, averaging, pyramiding, simultaneous positions, short, hedge, reversal, re-entry on an unchanged BULL state, discretionary order, manual intervention or shared-capital coupling. The fixed quantity is a *research simulation* amount, not the source author's sizing.
- **Risk controls explicitly disabled:** no independent SL, TP, trailing stop/order, profit lock, time exit, margin call or forced liquidation. The Supertrend bearish flip is the only exit. No position-level stop is silently inserted. The source's discretionary swing stop and target suggestions are **not** treated as numeric strategy rules.

## Required data

Single `BTC-USDT` spot 4h OHLCV stream; the trading decisions consume `H,L,C` only. Use consecutive bars with 4h UTC-open labels, no incomplete current candle. `ATR10` and `K/D` require historical bars, not fitted artifacts. No funding, OI, leverage, mark price, intrabar path, cross-pair synchronization, order book, off-chain information or future extrema. The frozen run must specify exact dataset start/end and candle revision/source before downstream screening; none is invented here.

## Execution assumptions

- **Pinned engine identity, not guessed from version text:** policy package `20260920`, in-wheel `hummingbot/VERSION=dev-2.17.0`; source code pinned to `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. GitHub-connected reads on 2026-10-25 directly inspected the commit's `hummingbot/VERSION`, Binance spot candle files, `strategy_v2/backtesting/backtesting_engine_base.py` and `executors_simulator/order_executor_simulator.py`. Package-to-commit evidence is **inherited** from the independently admitted `forven-adx-trend-di-cross-long-flat-btcusdt-1d-2026-10-25.md` on this repo's main: wheel `hummingbot-20260920-cp312-cp312-macosx_11_0_arm64.whl`, SHA-256 `ea5a929c52095bc03fd34f5b3fb2fbfef068f7ea880af6c38290d1ddb729a148`, wheel metadata `Version: 20260920`, in-wheel VERSION `dev-2.17.0`, and reported 902/902 Python-file hash identity to the cited source commit. **This Scout did not independently rehash the wheel**; it does not infer identity from the source tree's unrelated `setup.py` version string.
- **Actual market/feed path:** `BinanceSpotCandles` maps `BTC-USDT` to `BTCUSDT`; pinned `constants.py` includes `4h` and `/api/v3/klines`; `_parse_rest_candles` maps exchange row `0` to **bar-open timestamp** and rows `1..5` to OHLCV. Only a finalized bar becomes a signal input. Controller feature normalization must explicitly assign **effective decision timestamp = bar-open timestamp + 14400 seconds** and exclude every row whose bar has not closed. Do not treat a 4h open timestamp as a close-time observation.
- **Actual controller/executor path:** pinned `BacktestingEngineBase.simulate_execution` calls `controller.determine_executor_actions()`, handles `CreateExecutorAction`, dispatches `OrderExecutorConfig` to `OrderExecutorSimulator`. Use connector `binance`, pair `BTC-USDT`, `TradeType.BUY/SELL`, `ExecutionStrategy.MARKET`, amount `Q=0.001`, leverage 1/no margin, `CloseType.POSITION_HOLD` netting. A **strategy-specific controller has not been implemented**; the above fully specified indicator/state machine is its required future deterministic feature computation, not an additional admission status.
- **Real simulator fill semantics:** for MARKET, `OrderExecutorSimulator` fills at the **first supplied row timestamp**, price `df.loc[fill_timestamp,'close']`, full quantity, `filled_amount_quote=Q*close`, `cum_fees_quote=trade_cost*filled_amount_quote`, and `CloseType.POSITION_HOLD`. Use **one** normalized row at the just-closed 4h bar's effective close time per action; this is a pinned **historical same-close simulation convention**, not a claim that a real order submitted after the close can obtain that close. No maker queue, next-open order, tick fill, partial fill or intrabar stop is needed or assumed.
- **Causality caveat and control:** `prepare_market_data()` uses backward `merge_asof` and `dropna`, which alone **do not prove feature availability**. The required controller/feature normalization must enforce completed-bar gating, timestamp shift and frozen warmup *before* calling the simulator; an early/forward-leaking row is a Gate-6 failure, not a supported shortcut. No signal uses future price/volume or a current unfinished 4h candle.
- **Ledger and economics:** `BacktestPositionHold` in the pinned `backtesting_engine_base.py` nets BUY and SELL of the same base, realizes matched gross PnL and separately accumulates `cum_fees_quote`. Fix `trade_cost=0.001` (0.1% quote notional **each filled side**). At BUY price `Pb`, modeled cash decreases `Q*Pb*(1+0.001)`; at SELL `Ps`, modeled cash increases `Q*Ps*(1-0.001)`; realized net trade PnL `Q*(Ps-Pb)-0.001*Q*(Pb+Ps)`. Open holdings are marked to last completed close, retaining paid entry fees in cash. Do **not** mistake `net_pnl_quote` of a hold executor or the engine's mixed `total_pnl` timeseries for fee-inclusive cash equity. Funding is **not applicable** to unleveraged spot, not a fictitious observed zero; no margin, perpetual financing or liquidation is modeled. The simulator path has no explicit slippage/spread term and fills at its candle close; modeled extra slippage is **0 by engine convention**, **not** a claim of zero actual slippage. Real fees, lot/tick/min-notional compliance, partial fills, exchange latency and live price availability remain **unverified** and are not claimed as deployment authorization.
- **Position-state timing:** maintain the derived controller's own immediately filled FLAT/LONG ledger and `last_entry_index`, not the engine's one-row-lagged `positions_held` or terminated-executor time-window view. A successful MARKET action is treated as an immediate historical full fill on its normalized row; the engine's delayed `POSITION_HOLD` conversion is only for netting/accounting, not a signal gate. Use one pair, one controller and no shared capital or concurrency assumptions. This reuses the already reviewed spot MARKET-close/POSITION_HOLD primitive; no new engine order type is introduced.

## Evidence

### Source-reported

TradingView author **mfsz2015**, script `cU0Z0nuY`, version 1.0, 2026-01-24: explicit BUY/SELL visual conjunctions, defaults (ATR10×3, Stochastic 14/3/3, five candles between signals), strong-signal 20/80 badges, and suggested signal-bar-close entry. No trustworthy source performance numbers or Pine order-execution details were available in the readable description.

### Independently reproduced

**Not independently reproduced.** This cycle inspected the TradingView first-party description and read the pinned Hummingbot GitHub source path, plus a previously admitted wheel-hash verification record. No Qlib/Hummingbot replay, trade-by-trade parity, backtest, performance result, wheel rehash or live fill verification was performed. The six gates here are a *reviewable claimed research specification* pending independent Hermes Auditor review, not a self-approved merge.

### Negative evidence

- No readable full Pine source revision; do **not** represent the recurrence, zero-range handling, five-bar entry cooldown, exit or fills as source-native.
- No source-backed discretionary swing-stop distance, profit target or performance sample; none is invented.
- No evidence for real exchange-close fills, actual spread, precision, partials or fee tier. Model them only within the pinned historical spot simulator and explicitly retain live limitations.
- Same-bar Supertrend flip and K/D cross may be rare; do not infer effectiveness from alert screenshots.
- The package-to-source hash proof is reused from a separately admitted record, not rehashed in this cycle; a contrary distribution hash would block Gate 5 and require an audit correction before merge.

### Six-gate HB_READY claim for independent review

1. **Deterministic:** ATR10 RMA seed, recursive ST bands/state, price-Stochastic 14/3/3, thresholds, strict crosses, zero-range rule, 100-bar warmup and entry spacing are fixed above; no trained artifact.
2. **Direction:** Binance spot long/flat only; shorts explicitly disabled.
3. **Entries/exits/risk:** exact conjunctive entry, bearish-flip exit, priority and explicit absence of stop/target/trailing/time exits.
4. **Position:** one Q=0.001 BTC, 1000 USDT simulated starting cash, no DCA/adds, entry-only five-bar cooldown, explicit ledger/re-entry rules and insufficient-cash skip.
5. **Pinned Hummingbot model:** fixed wheel/version/commit with inherited hash evidence and directly inspected Binance spot 4h candle, MARKET OrderExecutor, timestamp, fee and PositionHold accounting paths; no unsupported intrabar, multi-market or margin path.
6. **Point-in-time:** 100-bar completed-history warmup, 4h open→close timestamp normalization, only completed bars, no future shift, no fabricated prices or unverified next-open fills.

## Falsification plan

Before any downstream Qlib large-scale screening: freeze exact Binance spot 4h input start/end, replay the recurrence with a small independently computed reference on historical *completed* bars, verify strict flip/cross coincidence, five-bar entry spacing, one-entry/one-exit state and every trade's effective close timestamp. Reconcile MARKET OrderExecutor fills and PositionHold realized gross/fees with the cash-ledger identity on a representative sample. If any required engine primitive differs from the cited wheel/commit or a bar-open label leaks an incomplete candle, **do not claim HB_READY**; require independent remediation. Any new execution primitive needs one representative capability validation before mass screening. Profitability/OOS and later strategy-specific HB/Qlib event-level certification are separate stages.

## Crypto portability

The admitted *derivative specification* is fixed to BTC-USDT Binance spot 4h. Other symbols/timeframes and downstream BO/SO 6/6/6 or 3×/5× perpetual research overlays are **not** part of this identity; adding them may change trade events, fees, margin and funding, and requires separately disclosed and validated execution assumptions. The former pair/timeframe/OHLCV/same-close blanket bans are **not** used as admission gates.

## Limitations

A public indicator description is not an immutable executable Pine revision. Derived ST initialization and state handling can differ from the author's hidden exact code; the five-bar rule is deliberately entry-only here. Exiting on any bearish flip can produce a different ledger from the author's full SELL badge. No stop beyond that regime exit; gaps and sharp adverse moves remain possible. Historical same-close full fills omit real latency, spread and precision. No reported performance, Qlib parity, HB certification, profitability or live suitability.

## Implementation status

`not-implemented`. The deterministic specification is eligible for independent six-gate *research admission review*; no strategy-specific Hummingbot controller or Qlib executable recipe was created. If admitted and selected downstream, the existing `IMPLEMENTATION_NEEDED` route supplies the minimal family-specific executable without adding a second admission field, registry, compiler, service or control plane.

## Adoption boundary

`status: research-only`; `adoption: not-approved`; `approval_scope: research-only`. Scout PR only. Independent Hermes Auditor owns source-fact review, six-gate PASS/NOT_LOSSLESS decision and exact-head merge or close. No backtest, container change, Paper/Testnet/Live trade, strategy deployment or automatic approval is authorized.

## Related Wiki records

None supplied; no private Wiki data is asserted or copied.

## Sources

1. [mfsz2015 — Supertrend + Stochastic Strategy, TradingView public script `cU0Z0nuY`](https://www.tradingview.com/script/cU0Z0nuY/), published 2026-01-24, author version 1.0, description inspected 2026-10-25.
2. [Pinned Hummingbot source commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3`](https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3), read through connected GitHub app; specific data, engine, order and hold code paths named above.
3. [Repository HB_READY six-gate contract](https://github.com/HCH725/alpha-strategy-research/blob/18dfc58ab9c67b3cac6d622609e1b0ee455b827f/.github/HB_READY_REVIEW.md), snapshot main 2026-10-25.
