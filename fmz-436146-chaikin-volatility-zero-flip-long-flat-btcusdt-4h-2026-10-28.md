---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Chaikin Volatility range-ROC zero-flip long-flat BTC-USDT 4h (independent derivative)"
created: 2026-10-28
updated: 2026-10-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-28
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于柴金波动率指标的短线交易策略Short-term-Trading-Strategy-Based-on-Chaikin-Volatility-Indicator.md
  - https://www.fmz.com/strategy/436146
  - https://www.tradingview.com/script/Zp7s3wPv-Chaikin-Volatility-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Chaikin Volatility range-ROC zero-flip — independent research derivative

## Provenance

**Primary GitHub source (immutable):** `fmzquant/strategies` at commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (HEAD, committed 2025-04-30), file `基于柴金波动率指标的短线交易策略Short-term-Trading-Strategy-Based-on-Chaikin-Volatility-Indicator.md`, read in full via raw file fetch on 2026-10-28. Author line: `ChaoZhang`. Detail link recorded inside the file: `https://www.fmz.com/strategy/436146`. Last-modified line inside the file: `2023-12-21 16:14:56`. The file embeds one complete Pine Script v2 strategy (`Copyright by HPotter v1.0 01/12/2016`, `strategy(title="Chaikin Volatility Strategy Backtest")`) plus a Chinese/English prose description of the same rule. No FMZ account, login, or paywall was required to read this mirror; the FMZ detail page itself was not separately fetched and no claim about its current rendered state is made.

**Source-native facts, not independently reproduced:** Range `xPrice = high - low`; `xROC_EMA = roc(ema(xPrice, Length), ROCLength)` with `Length = input(10, minval=1)`, `ROCLength = input(12, minval=1)`, `Trigger = input(0, minval=1)`, `reverse = input(false)`; state `pos = 1` when `xROC_EMA < Trigger`, `-1` when `xROC_EMA > Trigger`, else carried (`nz(pos[1], 0)`); `reverse=false` default keeps `possig = pos`; `strategy.entry("Long", strategy.long)` while `possig == 1`, `strategy.entry("Short", strategy.short)` while `possig == -1` (Pine default no-pyramiding, opposite entry reverses). The FMZ backtest header inside the file uses `period: 3h`, `basePeriod: 15m`, `Futures_Binance BTC_USDT`, 2023-11-20→2023-12-04. The prose states: long when the indicator crosses above Trigger, short when it crosses below (loose prose; the Pine bytes govern). These original fills, futures economics, backtest statistics, and source event sequence have NOT been reproduced or inherited.

**Explicit independent derivative, NOT source-native/lossless:** Preserve the distinctive EMA-of-range ROC(10,12) zero-threshold state flip, but deliberately (1) trade Binance BTC-USDT **spot 4h** LONG/FLAT (the FMZ header's `3h` is not a pinned-feed interval, see Gate 5; the Pine itself is timeframe-free), (2) convert the source's short leg into a **flat exit** (spot cannot short; no margin, no futures, no funding leg), (3) pin `reverse=false` (source default; the reverse option is disabled, not traded), (4) use fixed **0.001 BTC** per trade and 10,000 USDT initial unborrowed cash, (5) use completed-close historical MARKET fills with a hypothetical **0.1% per filled side** cost model, (6) pin EMA seeding/warmup/zero-denominator/division behavior below, (7) disable all stop/TP/trailing/time exits (opposite-signal exit only). These changes materially alter trade events and economics; no source parity or profitability is claimed.

**Immutable derivative identity:** `FMZ:436146:fmzquant-mirror-7853bb2bf262c4567ac238d3552d97f0e50cb801:independent-derived-v1:CV-EMA10-ROC12-zeroflip:reverse-off | BinanceSpot:BTC-USDT:UTC4h:LONG-FLAT:Q0.001BTC | Hummingbot-MARKET-close:cost0.001-per-side | warmup64`. Any altered source facts, lengths, threshold, market, event order, price convention, or cost constitutes a different derivative.

## Economic mechanism

### Source-reported

Range expansion/contraction (high-minus-low EMA change) marks short-term volatility regimes; low/contracting volatility is treated as the long side and expanding volatility as the short side (HPotter template: `pos = 1` below Trigger, `-1` above). No economic proof is offered by the source; its own header says learning/paper-trading only.

### Research interpretation

Falsifiable hypothesis only: after a volatility contraction (range-EMA falling versus 12 bars ago), a small long position may capture the subsequent drift; when range-EMA expands versus 12 bars ago, stepping aside may avoid expansion shocks. This derivative does NOT implement the source's short side and therefore cannot profit from, nor fully replicate, the source's two-sided event sequence. No expectancy is asserted.

## Signal

- Input: exactly one Binance BTC-USDT **spot 4h UTC** OHLCV series. Candle `t` is labeled by **open** timestamp `T[t]` (multiples of 14,400s), closes and becomes available at `T[t]+14400` seconds. Use only **completed** candles. Require consecutive 4h timestamps, finite OHLCV, `high>=max(open,close)>=min(open,close)>=low>0`, `volume>=0`. Any missing, duplicate, non-4h, NaN, nonpositive-price, or otherwise invalid bar **aborts the research run**; do not interpolate, forward-fill, or invent a trade price.
- `R[t] = high[t]-low[t]` (`>=0` by validity).
- `EMA10`: `alpha = 2/(10+1)`; `EMA10[9] = mean(R[0..9])` (SMA seed, matching Pine `ta.ema` seeding semantics — a **researcher pin**, stated as derivative definition, not a byte-verified Pine v2 runtime claim); `EMA10[t] = alpha*R[t]+(1-alpha)*EMA10[t-1]` for `t>=10`; undefined for `t<9`.
- `CV[t] = 100*(EMA10[t]-EMA10[t-12])/EMA10[t-12]`; undefined (`na`) when either EMA is undefined or the baseline `EMA10[t-12]==0` (division-by-zero is fail-closed carry, never a trade; Pine division-by-zero yields `na`).
- `Trigger = 0` pinned (source Pine default; the FMZ args table renders this row idiosyncratically and is not relied upon).
- `pos[t] = 1` if `CV[t]<0`; `-1` if `CV[t]>0`; else `pos[t-1]`. Strict inequalities; exact-zero carries. `pos` starts at `0` on the last warmup bar; `CV=na` carries (no signal).
- **Warmup:** consume at least **64 consecutive completed 4h bars** before the first signal; no entry during warmup; no pre-warmup state is carried (covers EMA seed 10 + ROC lag 12 with margin). Start FLAT.
- **Entry:** when FLAT and `pos` flips to `1` (`pos[t]==1` and previous `pos!=1`), BUY exactly **0.001 BTC** at the completed signal bar's **close** under the pinned historical MARKET-close simulation. Set LONG, `entry_price=close[t]`. The entry bar is **not** evaluated for exit (structurally exclusive: `pos[t]==1` cannot satisfy the exit condition).
- **Exit:** when LONG and `pos` flips to `-1`, SELL all 0.001 BTC at that completed close, return FLAT. This is the source short leg converted into a flat exit — a declared adaptation, not source reproduction.
- **State/priority:** exit precedes entry consideration; both cannot fire on one bar. Ignore `pos==1` persistence while LONG (no pyramiding, no adds). After an exit, re-entry requires a fresh `pos` flip to `1`. One spot long or flat only; no short, pyramiding, averaging, DCA/safety orders, partial fills, SL/TP/trailing/time exits (all **explicitly disabled**, no hidden Hummingbot defaults), maker/limit, leverage, margin, funding, cross-asset state, or shared-capital allocation. No terminal trade is fabricated if LONG at the last bar; mark the open position at the last close for reporting.
- On any missing/failed MARKET fill, insufficient **modeled** cash, nonfinite fee/price, or position-book mismatch outside the tolerance below, **abort the run** rather than inventing an order, cash balance, or missing price. No optimization or parameter search is performed in this record.

## Required data

Single Binance BTC-USDT spot 4h completed OHLCV series only (open-time labeled, one interval, one pair). No index, funding, OI, sentiment, on-chain, multi-timeframe, or cross-asset input. Warmup 64 completed 4h bars (~10.7 days). Range-ROC needs no hidden feed or unsupported synchronization.

## Execution assumptions

**Pinned benchmark:** Hummingbot package `20260920`, `hummingbot/VERSION=dev-2.17.0`, GitHub repository `HCH725/hummingbot` at immutable commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3`. The following real code paths were read via raw fetch on 2026-10-28; this is **static capability evidence**, not a strategy backtest:

1. **Data/clock:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` declares `INTERVALS` including **`4h`** (and `1h/1d` etc.; it does **not** declare `3h`, which is why this derivative pins `4h` instead of the FMZ header's `3h`). `binance_spot_candles.py` maps REST `/api/v3/klines` open-time `row[0]` plus OHLCV `row[1..5]` into candle timestamps (websocket `k.t` likewise). `backtesting_engine_base.py` exposes processed `open_bt/high_bt/low_bt/close_bt/volume_bt` columns keyed by that open-time timestamp. Range-ROC plus close-only flip needs no hidden feed.
2. **Controller/executor:** `backtesting_engine_base.py` iterates `update_state(row)`, `controller.determine_executor_actions()`, `CreateExecutorAction`, then `simulate_executor`. A **strategy-specific, not-yet-implemented controller** can hold the explicitly defined `pos` state, issuing `OrderExecutorConfig(connector_name="binance", trading_pair="BTC-USDT", side=BUY/SELL, amount=Decimal("0.001"), execution_strategy=MARKET, leverage=1)`. Research expressibility argument, **not** a claim that an executable controller already exists.
3. **Fill and causal clock:** `executors_simulator/order_executor_simulator.py` fills MARKET at the **first supplied candle's `close`**, records `filled_amount_quote=float(amount)*close`, charges `trade_cost*filled_amount_quote`, returns `CloseType.POSITION_HOLD`. The simulator `fill_timestamp` is the candle's **open-time label**; all derivative decisions/fills are explicitly reported at **open timestamp + 14400 seconds**, never as available at candle open. Same-close fills are a **historical zero-latency modeling convention**, not an achievable post-close exchange guarantee; no next-open, maker, high/low touch, or stop primitive is hidden in this derivative.
4. **Spot position and research costs:** Initial modeled cash **10,000 USDT**, position either **0** or **0.001 BTC**. A BUY at price `p` reduces exact Decimal research cash by `0.001*p*(1+0.001)`; a SELL increases it by `0.001*p*(1-0.001)`. The fixed **0.1% per-side fee is a hypothetical research input**, not a verified Binance fee. `trade_cost=0.001` is passed to the simulator. Realized gross quote PnL = `(sell_price-buy_price)*0.001` per round trip via matched buys/sells; net PnL = gross minus both-side fees from the independent Decimal ledger. Open equity = cash + 0.001*last_close. The pinned `BacktestPositionHold` computes gross matched PnL (`_process_order` nets buys/sells) and accumulates quote fees separately in `cum_fees_quote`; reconcile both against the independent ledger. Spot funding is **not applicable**, not a fabricated realized zero-funding stream. No margin or liquidation.
5. **Float/Decimal caveat and fail-closed bound:** `OrderExecutorSimulator` uses float for filled quote while `BacktestPositionHold.add_executor` converts back to base by division and `is_closed` tests exact zero, so a tiny engine residual is possible after equal 0.001 BTC BUY/SELL legs. The derived controller must use its **explicit confirmed-order 0/0.001 BTC state**, never infer re-entry eligibility solely from the engine's exact-zero flag. On each fill reconcile engine net base with exact research inventory and engine gross PnL/fees with the Decimal ledger, allowing at most **1e-10 BTC base residual** and **1e-6 USDT quote rounding discrepancy**; larger deviations, negative modeled cash, or an unaccounted fill **abort**, not silently reclassify exposure. These are **research diagnostic bounds**, not exchange precision claims or engine fixes.
6. **Capability boundary:** This path models completed 4h OHLCV, one spot pair, historical MARKET-close fills, and quote-fee accounting only. It does **not** verify tick/lot/min-notional rules, order acceptance, liquidity, commission tiers, slippage, partial fills, or live execution. Simulator modeled slippage is absent; that is **not** evidence actual slippage is zero. The source's futures/3h/15m outcomes are deliberately **not** carried over. If any unmodeled capability becomes materially required, Gate 5 must be reassessed before research expansion.

## Evidence

### Source-reported

Full Pine v2 rule quoted in Provenance (state flip at Trigger 0, Length 10, ROCLength 12, reverse option); FMZ header backtest window 2023-11-20→2023-12-04 on `Futures_Binance BTC_USDT period 3h`; author's own learning/paper-only disclaimer. No source performance number is repeated here (none with traceable table/figure provenance was found in the file).

### Independently reproduced

On 2026-10-28 the researcher ran a **dual-implementation check on 1000 live Binance BTCUSDT spot 4h klines** (consecutive open timestamps, zero gaps): (A) textbook EMA recursion with SMA seed plus ROC definition; (B) independently formulated seed-decay summation plus ratio-minus-one ROC form. Result: **zero mismatches** across all 1000 bars (value tolerance 1e-9, `na` masks identical). Post-warmup (64 bars) state machine: **53 entries / 53 exits**, final FLAT, zero pre-warmup signals, zero same-bar entry/exit conflicts. Hand-verified first entry bar: baseline/range-EMA arithmetic recomputed by hand (`100*(754.819343-845.568984)/845.568984 = -10.7324% < 0` with prior state `-1` → FLAT-to-LONG flip). This is a **signal-logic check only**, not a backtest, not profitability evidence, and not Qlib/HB parity.

### Negative evidence

Pine runtime bytes were read from the GitHub mirror, not executed; TradingView page `Zp7s3wPv` (same HPotter author line, 2014) was inspected for identity only — its code pane requires login, so **no TradingView Pine byte is claimed**. The FMZ detail page `436146` was not separately fetched. The source's 3h/futures/short-leg outcomes are explicitly not reproduced. The zero-denominator and exact-zero-CV branches are untested on live data (no flat-range 4h bar occurred in the 1000-bar window); they are fail-closed by definition. PASS here is the researcher's **six-gate submission claim**, not independent approval, implementation, Qlib parity, Survivor, profitability, or Paper/Testnet/Live authorization.

## Falsification plan

Before any mass screening of this primitive, one representative event-level check must agree: independent re-implementation signal log (entry/exit bar open-timestamps) versus the pinned-engine run's order timestamps, fill prices equal to the corresponding completed closes, Decimal ledger versus engine gross/fees within the 1e-10/1e-6 bounds, and abort on any data-validity violation. Persistent mismatch, negative modeled cash, or an unaccounted fill falsifies the execution binding (not the source). No live, Paper, or Testnet action is authorized by this record.

## Crypto portability

Single-pair Binance BTC-USDT spot 4h by construction; no exotic market structure is assumed, so the rule ports mechanically to any spot pair/interval with consecutive completed bars, but each new market/interval is a **different derivative** requiring its own record and evidence. Futures, margin, shorting, or portfolio-shared-capital ports are out of scope for this record.

## Limitations

- Two-sided source reduced to long-flat: upside/protection behavior differs materially from the original; the `reverse=true` branch is never traded.
- Opposite-signal exit only: no protective stop; gap/expansion losses between 4h closes are fully realized in the model.
- 4h pinned instead of the FMZ header's 3h (unsupported by the pinned feed); Pine itself is timeframe-free, so no source-timeframe fidelity is claimed either way.
- Hypothetical 0.1%/side fee; no slippage/liquidity/lot-size modeling; same-close fills are a historical convention.
- EMA seeding follows documented Pine `ta.ema` semantics as a researcher pin; any Pine-version seeding nuance is a disclosed approximation, bounded by the 64-bar warmup.
- 53/53 flip density on the check window implies frequent round trips; costs dominate economics — research question only, not a trade recommendation.

## Implementation status

`not-implemented`: no controller, recipe, Qlib entrypoint, or execution binding exists. Downstream engineering route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, then proceed), which is materialization-pending, not REJECT, and never a second admission field. This record carries no executable artifact.

## Adoption boundary

`research-only`, `not-approved`. No Paper/Testnet/Live trading, no deployment, no scheduling change, and no Qlib mass screening before the representative event-level parity check above. Independent Hermes Auditor must verify source facts and all six gates at the exact PR head before any merge.

## Related Wiki records

None. This Scout run wrote no Wiki Brain records (PR-only workflow; no wiki, Hummingbot, Qlib, or n8n actions taken).

## Dedup, pool, and review routing

- Base `430e70b` == `origin/main`; pool snapshot **393** root-level strategy records (395 Markdown files minus the two READMEs); README count line reads 393.
- Code search over all `main` records for `chaikin.?volatility`, `cvol`, `xROC_EMA`, and `436146`: **zero hits**. Nearest families fenced as materially different: `chaikin-oscillator` (A/D-line MACD, not range-ROC), `cmf-velocity` (Chaikin Money Flow, not range-ROC), FMZ-mirror `Chaikin-Oscillator-Strategy` and `Chaikin-Money-Flow-CMF` files (different indicators, not used). No record trades EMA-of-range ROC zero-flips.
- Same-author TradingView pages (`Zp7s3wPv` strategy 2014, `5JPpNU88` backtest 2016, `QAjxTT0J` indicator) describe the same HPotter template but their code bytes were **not** read (login wall) and are **not** claimed as source; the GitHub mirror file above is the sole rule source.
- Open `research/*` PRs at submission time (Heracles-KCD #353, ClucMay #350, AdxSmas #331, forven-CCI #304, Swift-2YMA #251, SSL #92, Chandelier #89, Supertrend-flip #63, Gauss-StochRSI #49, LW-streak #48): none is a range-volatility mechanism; no duplicate.
- Submitted for independent six-gate HB_READY admission review; the reviewer may only remediate source-verifiable facts and must never invent a derivative to rescue this PR.
