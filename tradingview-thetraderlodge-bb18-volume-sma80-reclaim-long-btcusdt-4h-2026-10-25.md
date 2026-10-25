---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TradingView thetraderlodge BB20 1.8-sigma lower-band reclaim with volume and SMA80 trend gate — independent BTCUSDT spot 4h derivative
created: 2026-10-25
updated: 2026-10-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-07-30
sources:
  - https://www.tradingview.com/script/ANWxAWqY-4H-Bollinger-Breakout-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Volume- and trend-gated lower Bollinger reclaim — independent derived strategy

## Provenance

- **Primary TradingView publication:** *4H Bollinger Breakout Strategy*, **thetraderlodge**, **2025-07-30**, stable public script ID **ANWxAWqY**, public open-source listing: https://www.tradingview.com/script/ANWxAWqY-4H-Bollinger-Breakout-Strategy/ . Author description directly read on **2026-10-25**. The accessible text is the author's description, **not a byte-verified Pine code listing**; no original Pine version, precise code-ordering, fills, or source-native equivalence is claimed.
- **Source-description facts:** 4h emphasis; Bollinger default length **20**, **SMA** basis, **close** input, standard-deviation multiplier **1.8**, plot offset **0**; default enabled filters: volume 20-bar average with **long volume > 105%** of average, trend **SMA80** with long price above it; RSI14 and RSI<85 are described as a **short-side** filter. Author describes long entry as an **upcross of the lower BB** and short entry as downcross of upper BB, with exits on opposite BB crosses. The page also states 0.1% commission and default full-equity sizing, but does not expose complete order/exit state in readable Pine.
- **Independent derivative, NOT lossless source reconstruction:** This record separately fixes the population-standard-deviation formula, exact cross equality semantics, lower-band reclaim plus volume/trend filter, **long-only** position state, and an **upper-band downcross** as the sole long exit. The author's generic “opposite BB crosses” does not establish that this precise exit is source-native. The derivative explicitly **disables short entries, stops, targets, trailing, time limits and all other unspecified optional source behaviors**. It selects Binance **BTC-USDT spot 4h**, fixed **0.001 BTC**, 100-bar warmup, completed-bar same-close **research-simulator** fills, strict data-gap handling, research fee accounting and no pyramiding/DCA. These are researcher decisions, not claims about the author's Pine defaults or historical trades.
- **Immutable identity:** `TV-ANWxAWqY | independently-derived-v1-BB20-SMA-1p8-lower-reclaim-volume105-SMA80-upper-downcross-exit | BinanceSpot-BTC-USDT-4h | 2026-10-25`. Any change to signal, formula, thresholds, market, clock, fill or position state constitutes a different derivative.

## Economic mechanism

### Source-reported

The author combines Bollinger lower/upper crossing with optional volume and trend filters. The published description presents long lower-band reclaim and short upper-band crossing, not verified backtest returns.

### Research interpretation

Hypothesis only: a 4h price reclaim of a volatility envelope's lower edge, conditional on above-average contemporaneous volume and price remaining above an 80-bar long-term SMA, may identify a trend-aligned dip. Exiting on an upper-band downward crossing waits for a full upper-envelope excursion and may leave positions underwater indefinitely. This is neither a tested edge nor a loss-limiting strategy.

## Signal

**Frozen independent derivative (Gates 1–4).** Single UTC-aligned, consecutive **14,400-second** Binance BTC-USDT spot OHLCV stream. Each bar `t` is labeled by its open timestamp `T[t]`; its complete OHLCV is available for decisions only at `T[t]+14400`. No other asset, time frame, order-book or non-OHLCV feed.

- `basis[t] = (1/20)*sum(close[t-i], i=0..19)`.
- `sd[t] = sqrt((1/20)*sum((close[t-i]-basis[t])^2, i=0..19))` (population, not sample standard deviation). `lower[t]=basis[t]-1.8*sd[t]`; `upper[t]=basis[t]+1.8*sd[t]`. The plot offset is **zero** and never changes decision data.
- `volumeMean[t]=(1/20)*sum(volume[t-i], i=0..19)`; `trendSMA80[t]=(1/80)*sum(close[t-i], i=0..79)`.
- **Entry, only if FLAT:** `close[t-1] <= lower[t-1] && close[t] > lower[t] && volume[t] > 1.05*volumeMean[t] && close[t] > trendSMA80[t]`. All current comparisons are strict; a previous equality permits the crossing edge. If 20-bar average volume is zero, the volume gate is false. No RSI gate on the long side; RSI14 and all short logic are explicitly disabled.
- **Exit, only if LONG:** `close[t-1] >= upper[t-1] && close[t] < upper[t]`. This **upper-band crossunder exit is a researcher-selected interpretation**, not a claim that the author's unspecified Pine exit uses the same rule. Entry filters do not gate an exit; no exit fires on merely touching the upper band, on the first crossing *above* it, or on the loss of SMA80.
- **State machine:** initially FLAT; first eligible decision after **100 consecutive valid completed 4h bars**. On each completed eligible bar, if FLAT test entry and create one simulated MARKET BUY of **0.001 BTC**; if LONG test exit and create one MARKET SELL of the full **0.001 BTC**. Otherwise HOLD. Exactly one action maximum per bar. No same-bar entry/exit or reversal. After a filled exit, the next eligible later bar may re-enter without cooldown; repeated entry signals while LONG are no-ops.
- **Position/risk:** one spot LONG or FLAT, no short, leverage, margin, pyramiding, DCA, safety orders, concurrency, partial orders/fills, portfolio allocation, stop loss, take profit, trailing stop, time exit, liquidation, maker/limit/intrabar orders or forced final-bar liquidation. If LONG at end of dataset, hold 0.001 BTC and mark at last valid close without inventing a terminal SELL. No capital compounding.
- **Input validity:** every bar must have expected UTC 4h open-time spacing, finite positive O/H/L/C, `high >= max(open,close)`, `low <= min(open,close)`, and finite nonnegative volume. Invalid/missing candles reset the 100-consecutive-bar warmup and suppress both entry and exit until 100 new contiguous valid completed candles; existing LONG exposure remains held, not liquidated at an invented fill. No forward filling, price substitution or silently spanning gaps. A zero-range bar is valid but does not itself create a synthetic crossing. Indicator windows must be wholly within the current valid segment.

## Required data

Single Binance BTC-USDT spot 4h OHLCV series with exact open timestamps; 20 completed bars for bands/volume mean, 80 for SMA80, and a preceding fully computed band for cross. The conservative 100-bar consecutive warmup covers both. No cross-symbol synchronization, external model, training, future extrema, funding series or secondary time frame.

## Execution assumptions

- **Pinned admission identifiers:** Hummingbot policy package label `20260920`, repository `hummingbot/VERSION=dev-2.17.0`; inspected **HCH725/hummingbot** at immutable commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3`. These are separate identifiers; the repository's `setup.py` distribution version `20260729` is not a verified build digest or proof of deployed package identity. The claim is bounded to **the pinned commit's research simulation semantics**, not an installed container.
- **Actual data path:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` explicitly supports `4h`; `binance_spot_candles.py` parses Binance Kline `row[0]` as open-time timestamp and `row[1..5]` as O/H/L/C/V. `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` exposes `open_bt/high_bt/low_bt/close_bt/volume_bt` and processes rows through `controller.determine_executor_actions()`, `CreateExecutorAction` and `OrderExecutorConfig`. A strategy-specific controller/feature implementation **does not yet exist**; it must calculate the declared 20/80-bar formulas and preserve state and validity rules, rather than claim that the generic engine already contains this strategy.
- **Fill model:** `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` handles `ExecutionStrategy.MARKET` with first supplied row timestamp and that row's `close` as full-fill price, `filled_amount_quote = Q * close`, `cum_fees_quote = trade_cost * filled_amount_quote`, and `CloseType.POSITION_HOLD`. The intended controller issues exactly one `CreateExecutorAction` with `OrderExecutorConfig` for Binance BTC-USDT, `MARKET`, BUY/SELL, `Q=0.001 BTC`, leverage 1; controller must maintain an immediate filled-position state rather than rely on delayed `positions_held` conversion to suppress duplicate orders.
- **Effective time and causal restriction:** the raw `timestamp_bt` is a **bar-open** label. The engine uses backward `merge_asof` and `dropna` in feature preparation, which **alone do not establish data availability**. The required strategy-specific implementation must expose the current OHLCV only after the completed bar and normalize both effective decision and research fill event to `T[t]+14400`, while using the declared same-row close simulator fill. This is a **simulation convention**; it does not assert that a real order submitted after observing the closing price can execute at that exact price. A future deployment requiring next-open/intrabar/maker realism is a new, separately verified engine path.
- **Costs and position ledger:** fix research `trade_cost=0.001` (**0.1% per filled side**), full fill `Q=0.001 BTC`, with modeled BUY cash outflow `Q*P_buy*(1+0.001)` and SELL inflow `Q*P_sell*(1-0.001)`. Compute realized net PnL as gross matched SELL–BUY less **both** fill fees; mark open BTC at last valid close, carrying already paid buy fee. `BacktestPositionHold` tracks gross position cost and accumulated fees, but native `summarize_results.net_pnl_quote` / `update_state.total_pnl` must **not** be mistaken for fee-inclusive cash/equity without reconstructing fills. **Spot funding is not applicable**; no fictitious futures funding=0. The simulator has no separately applied slippage in this model; this means **zero modeled additional slippage**, not evidence of real zero slippage. Exchange min-notional/lot precision, partial fills, real spreads, latency and realized commission are unverified and not represented as exchange-valid.
- **Reused representative capability:** admitted TradingView PR **#421** and **#423** independently reviewed this exact pinned Binance spot 4h / MARKET-close / POSITION_HOLD research execution path, including fee-ledger limitations and event-time normalization. This is reusable **engine-path evidence only**, not proof that this new candidate was implemented, backtested, profitable, or Qlib/Hummingbot-parity tested. No novel execution primitive is introduced.

## Evidence

### Source-reported

TradingView `ANWxAWqY` public author description, published 2025-07-30: BB20 SMA(close) 1.8, long lower-band crossover, volume 20-bar average >105%, SMA80 trend gate, short-side RSI14 filter, optional long/short and generic opposite-BB-cross exit. No original numerical performance is transcribed or asserted.

### Independently reproduced

**None for this candidate.** The Gate-5 expressibility argument is static pinned-code inspection plus reusable independently reviewed engine-path evidence, not a strategy backtest, Qlib parity run or independent reproduction of author metrics.

### Negative evidence

Readable TradingView page does not expose complete Pine; the exact original exit mapping, risk defaults, processing/fill behavior, and Pine code version are not verified. The independent derivative specifies and discloses these choices; no silent reconstruction or source-native claim. Research fills/fees are not real-world order economics; the strategy has no protective stop and may hold large unrealized losses.

## Falsification plan

Only after separate downstream approval, freeze this identity and compare against (a) the same lower-BB reclaim with no volume gate, (b) the same rule with no SMA80 gate, and (c) upper-band downcross versus midline crossunder exit, each on predetermined IS/OOS partitions without OOS tuning. Any new engine primitive requires representative Qlib/Hummingbot event-level validation before mass Qlib screening. **No backtest or trading was performed in this Scout cycle.**

## Crypto portability

Current declared instance is Binance BTC-USDT spot 4h only, without a universe restriction as an HB_READY prerequisite. A different pair/frame, derivatives funding/margin model, or BO/SO campaign overlay is a separately specified derivative or downstream research experiment; none is silently incorporated here.

## Limitations

PASS in frontmatter is a **proposed six-gate research admission claim pending independent Hermes Auditor review**, not an auditor's decision. Original Pine unavailable, no source-native equivalence, no independently reproduced returns, no deployment build digest, no live fill precision or slippage validation, no Qlib parity, no survivor or production approval. Exact package identity remains a boundary; reviewer must not invent a package-to-commit mapping.

## Implementation status

`not-implemented`: strategy-specific controller and data-gap/feature logic are not committed or deployed. Pinned simulator primitives were read only.

## Adoption boundary

`status: research-only`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review alone owns source-fact remediation, exact-head PASS merge or NOT_LOSSLESS close. This record does not authorize Paper, Testnet, Live, Qlib/Hummingbot backtests, n8n, containers, cron or other runtime changes.

## Related Wiki records

None asserted.

## Sources

- https://www.tradingview.com/script/ANWxAWqY-4H-Bollinger-Breakout-Strategy/ — thetraderlodge, 2025-07-30, public source description checked 2026-10-25.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned engine source read via connected GitHub app.
- https://github.com/HCH725/alpha-strategy-research/pull/421 — previously independently reviewed same research execution primitive.
- https://github.com/HCH725/alpha-strategy-research/pull/423 — previously independently reviewed same research execution primitive.
