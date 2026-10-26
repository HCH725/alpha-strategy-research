---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "trade_lexx RSI14 smoothed-Bollinger envelope cross — independent ETH-USDT spot 4h long-flat derivative"
created: 2026-10-27
updated: 2026-10-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
  - derived
status: research-only
confidence: medium
source_as_of: 2025-07-29
sources:
  - https://www.tradingview.com/script/8fzZ9aWv-rsi-bb-stddev-signal/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# trade_lexx RSI14 smoothed-Bollinger envelope cross — ETH-USDT spot 4h derivative

**Immutable research identity:** `TV:8fzZ9aWv | trade_lexx | published:2024-12-19 | page-updated:2025-07-29 | independent-derivative-v1:2026-10-27 | Binance ETH-USDT spot 4h | Wilder RSI14; SMA5(RSI); population-BB20(2.0) on SMA5; raw RSI crosses above lower envelope BUY / below upper envelope SELL | next-completed-bar-close MARKET | 0.01 ETH | fee-assumption 0.10% per side`. This identity is for the **fully specified derivative**, not the inaccessible Pine revision.

## Provenance

**Primary, public TradingView publication:** [RSI BB StdDev Signal](https://www.tradingview.com/script/8fzZ9aWv-rsi-bb-stddev-signal/) by **trade_lexx**, originally **2024-12-19**, latest visible release note **2025-07-29**, stable public script ID `8fzZ9aWv`. The page labels the script **open-source** and calls it an **indicator**, not a trading strategy. The public description and dated release notes were directly inspected on 2026-10-27. The complete Pine source bytes, Pine language version, historical code revision and actual default input values were **not retrieved**; this record does not assert source-native event equivalence.

**Facts actually described by the author:** RSI on user-selected input (close is described as default); the RSI is smoothed by a selectable moving average; Bollinger-style upper/lower envelopes are applied to that smoothed RSI; a **BUY signal** occurs when RSI crosses **up** through the lower RSI envelope, and a **SELL signal** when RSI crosses **down** through the upper envelope. The page additionally describes optional MA-signal modules, divergence detection, overbought/oversold zone filters, minimum bars between signals, alternating-signal mode, and (2025-07-29) an OR/AND combination mode with a universal connector. The author supplies **no verified complete trading-position, fill, stop, fee, or broker emulator contract** on the accessible page. The source is an indicator and its signals are not evidence of executed trades.

**Researcher-designed changes, all explicit (independent strategy, not a reconstruction):** select Binance `ETH-USDT` spot `4h`; select RSI14 Wilder seed on close; select SMA5 smoothing and 20-sample **population** standard deviation with multiplier 2.0 on the smoothed RSI; compare **raw RSI** against those envelope lines; use the described BB crossing signals **alone** (disable other MA signals, divergences, zones, AND mode, alert-combination effects, min-signal spacing and alternation filters); map BUY to one long entry and SELL to a complete long exit, with no short; fix 100 completed-bar flat warmup; use **one-bar-delayed MARKET close-price simulation**, fixed 0.01 ETH, a single position, explicit fee/cash rules and no stop/target/time exit. None of these researcher-chosen numbers, order conventions, disabled optional modules or portfolio choices are attributed to the author's original Pine defaults. Any change creates a different derivative identity.

**Dedup (main `9c1e5e782de325d0ac6c0f621d8802850b746aa4`):** current main tree has 370 root strategy Markdown records (excluding two READMEs), README declares 370; this is count agreement, **not** a claim that this Scout individually re-audited every existing PASS frontmatter. GitHub main code search for `8fzZ9aWv` and `trade_lexx`, and open-PR searches for that script ID, author and RSI-BB names, returned no match. All ten currently open `research/*` PRs were inspected by title/source scope and none cites this publication or this RSI-on-RSI-envelope rule. The nearest pool relatives use **price** Bollinger bands with RSI gates (e.g. ChartArt joint RSI50/price-BB cross, Forven price-BB RSI breakout, GPSRosario RSI29/price-BB), or **RSI Donchian** prior-extreme breakout (different rolling-extremum arithmetic and exit). This candidate uses a standard-deviation envelope of **smoothed RSI itself** and two asymmetric raw-RSI/envelope crosses; neither a source duplicate nor a mere threshold variation. Search indexing cannot prove absence of every paraphrase; the distinct event algebra is stated here for auditor verification.

## Economic mechanism

**Research hypothesis only:** an RSI reading that recovers above its own volatility-normalized *lower* envelope may mark a momentum rebound; holding until RSI falls back through its own *upper* envelope seeks the subsequent momentum swing. A single oscillatory threshold can whipsaw; no stop means prolonged adverse price moves remain possible. There are **no independently reproduced or adopted returns, win rates, Sharpe ratios, survivor claims, or profitability assertions**.

## Signal — complete frozen derived specification

1. **Input and arithmetic:** chronological contiguous Binance spot `ETH-USDT` UTC `4h` completed OHLCV, though the order signal reads **close only**. Require finite positive O/H/L/C, coherent OHLC bounds, finite nonnegative volume, strict 14,400-second open-time increments and no duplicates. Decimal precision 28 for cash/positions, float64 for indicator computation; no fitted model or training step. Incomplete final candle excluded. No forward-fill, synthetic bars, interpolation or full-sample normalization.
2. **Wilder RSI(14):** `d[t]=C[t]-C[t-1]`, `g=max(d,0)`, `l=max(-d,0)`. At chronological index `t=14`, seed mean gain/loss from `d[1..14]`; for `t>14`, `G[t]=(13*G[t-1]+g[t])/14`, `L[t]=(13*L[t-1]+l[t])/14`. `R[t]=100-100/(1+G/L)`; if `L=0,G>0` use 100; if `G=0,L>0` use 0; if both zero use 50. Undefined before index 14. Never substitute a different RSI seeding algorithm.
3. **RSI smoothing and bands:** `S[t]=SMA_5(R)[t]` (first defined at `t=18`). `M[t]=SMA_20(S)[t]` (first defined at `t=37`). `V[t]=(sum_{j=0}^{19}(S[t-j]-M[t])^2)/20` (population, `ddof=0`), `sigma[t]=sqrt(V[t])`, `Lo[t]=M[t]-2.0*sigma[t]`, `Hi[t]=M[t]+2.0*sigma[t]`. Band center and dispersion use **smoothed RSI**, whereas the cross-tested oscillator is **raw RSI**; this is a researcher pin, not a claim about inaccessible source-code defaults. The band has `Lo<=Hi` even at zero variance.
4. **Signal edges:** `buy[t]=(R[t-1] <= Lo[t-1]) AND (R[t] > Lo[t])`; `sell[t]=(R[t-1] >= Hi[t-1]) AND (R[t] < Hi[t])`. Strict current comparisons and inclusive prior comparisons; touches at current band do not fire. Both require defined prior/current oscillator and band. Because `Lo<=Hi`, BUY and SELL cannot both occur on one bar (the prior RSI would have to be at/below Lo and at/above Hi while current RSI would have to be above Lo and below Hi, impossible even for a zero-width envelope).
5. **Warmup:** index `t=0..99` remains FLAT and cannot enqueue orders; first signal eligible at `t=100` after **100 complete 4h bars**. RSI/Bollinger seeded by index 37; warmup adds margin. An already-positive oscillator relationship at warmup end does not create a new cross. No historical pre-warmup signal is replayed.
6. **Position and order state:** states FLAT, LONG (exactly `0.01 ETH` after confirmed BUY), and at most one pending BUY/SELL scheduled for the **next** completed 4h bar. On completed bar `t`, first execute any order queued by the signal at `t-1` at `C[t]` (if valid, affordable and actually simulated as filled); then evaluate `buy[t]` if FLAT or `sell[t]` if LONG and enqueue the relevant **opposite** action for `t+1`. Thus a filled BUY at `t` may arm a SELL for `t+1` but cannot SELL on `t`; similarly a filled SELL may arm a later fresh BUY. If a queued BUY is unaffordable/rejected, remain FLAT and discard that order, without phantom inventory or auto-retry; a later fresh BUY edge is required. If SELL cannot be confirmed, retain actual LONG inventory and do not invent liquidation. The last bar's pending action remains unfilled and is reported as pending, not fabricated. Exactly one simulated action per bar; no pyramiding, no averaging/DCA, no concurrent position, no cooldown, no compounding, no partial exit, no intrabar orders, no re-entry without a new BUY cross. Initial quote cash `10,000 USDT`, no borrowed cash.
7. **Risk and disabled features:** no stop loss, take-profit order, trailing stop, timeout, profit filter, margin liquidation, short, hedge, futures leverage, safety orders, forced end-of-sample sale, hidden strategy defaults, MA/divergence/zone filter or alert-based alternative entry. The sole LONG exit is the SELL edge; if no SELL edge arrives, the position can remain open indefinitely. Terminal open inventory is valued at the **last actually observed** close without a fictitious SELL.
8. **Cost and sizing:** BUY quantity `0.01 ETH`, cash debit `0.01*C_fill*(1+0.001)`; SELL full actual held ETH, cash credit `qty*C_fill*(1-0.001)`. `0.10%` per executed side is an explicit **research assumption**, not a verified Binance account fee. Fees in quote are tracked separately from gross average entry and gross realized PnL. This version models no additional slippage; it **does not assert real spread/impact is zero**. The quantity is a research arithmetic pin, not a claim of verified live exchange LOT_SIZE/min-notional filters. Spot funding is **not applicable**; no fictional zero-funding futures assumption.

## Required data, timestamps, and causality

- One native `4h` Binance spot feed, `ETH-USDT`. The pinned `binance_spot_candles/constants.py` supports `"4h":"4h"`; the REST parser maps `row[0]` to the **candle-open** timestamp and `row[1..5]` to OHLCV. Validate contiguous full bars **before** the engine's `merge_asof` and `dropna` preprocessing; these engine operations alone do not prove candle completeness. Missing/invalid prices or time gaps are a hard **run invalidation** (not silent compression, fabricated close, or forced flat).
- At signal bar `t`, `R/S/M/Lo/Hi` are computed only after its close, effective time `open[t]+14,400s`. The pending action from `t` is issued on the **following** completed bar `t+1`, priced by the pinned MARKET simulator at `C[t+1]`; effective modeled fill time `open[t+1]+14,400s`. The simulator internally labels its row with the **open** timestamp; research event reports must correct the semantic close-time label and must never claim that a live post-close order could necessarily execute at the just-observed historical close. No `request.security`, HTF alignment, future extremum, repainting pivot, negative shift, or unfinished candle input.

## Execution assumptions — pinned Hummingbot source-path evidence

- **Pinned baseline:** Hummingbot package `20260920`, VERSION `dev-2.17.0`, inspected source ref `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. The GitHub connector read `hummingbot/VERSION`, Binance spot intervals/parser, `OrderExecutorConfig`, `OrderExecutorSimulator`, and `BacktestingEngineBase`/`BacktestPositionHold` at that ref in this Scout. Package-to-source byte identity was previously documented in accepted Alpha PR #414, **not independently rehashed this run**.
- **Controller/engine route (future minimal implementation, not deployed):** a strategy-specific controller computes this frozen RSI/envelope state from validated completed bars, queues the prior-bar action, and emits `CreateExecutorAction` for `OrderExecutorConfig(connector_name="binance", trading_pair="ETH-USDT", side=BUY/SELL, amount=Decimal("0.01") or actual held quantity, execution_strategy=MARKET, price=None, leverage=1)`. `BacktestingEngineBase.simulate_execution` calls `update_state(row)`, then `determine_executor_actions()` and `simulate_executor()` on each processed row. The controller must keep an explicit pending/filled ledger; an executor config or a lagging `positions_held` snapshot is **not** itself proof of a fill.
- **Actual pinned fill primitive:** `OrderExecutorSimulator.simulate` MARKET branch selects the first processed row, prices the fill at that row's `close`, sets `filled_amount_quote=amount*close`, `cum_fees_quote=trade_cost*notional`, and emits `CloseType.POSITION_HOLD`. No maker/limit/next-open/intrabar primitive is required. The single-asset, sequential BUY/full SELL path is the already accepted model-consistent subset; it is not a claim of live closing-price executability.
- **Accounting:** `BacktestPositionHold._process_order` accumulates same-side amount and weighted average entry; opposite-side SELL reduces exposure and books **gross** realized quote PnL. `add_executor` separately accumulates quote fees. Net economics must subtract all executed-side fees, including any open-entry fee, and reconcile `cash + held ETH * last_valid_close` with gross PnL and fees. No futures margin, leverage, mark/index feed, or funding model is invoked.
- **Capability boundary:** source inspection proves the needed native 4h OHLCV, one-action-per-bar MARKET close-fill, sequential spot position-hold and quote-fee model **exists** in the pinned source. It does **not** prove a dedicated controller already exists, exact strategy Qlib parity, historical market microstructure, package-wheel hash this run, live precision, or profitability. If later engineering requires a new primitive, representative event-level Qlib/Hummingbot parity is required **before** large-scale screening using it; no per-strategy profitability criterion is added to HB_READY.

## Six HB_READY gates — Scout proposal for independent exact-head audit

1. **Determinism:** exact Wilder RSI14 seeding, SMA5, 20-population-sigma RSI envelope, 2.0 width, cross inequalities, warmup, no model fit, and complete pending-order priority.
2. **Direction:** Binance ETH-USDT **spot LONG/FLAT**, no naked short, no margin.
3. **Entries/exits/risk:** BUY raw RSI crossing the *lower RSI envelope*, SELL raw RSI crossing *upper RSI envelope*; next-complete-bar-close actions, full exit, all other risk/exit modules explicitly disabled.
4. **Position/state:** fixed 0.01 ETH, 10,000 USDT initial cash, one pending action, no DCA/pyramiding/cooldown, fee-aware affordability, actual-fill ledger, deterministic failed-action/last-bar/reentry handling.
5. **Pinned engine:** directly inspected 4h Binance spot feed, row-close MARKET fill, `CreateExecutorAction` path, POSITION_HOLD net position/cost accounting and separate quote fees at the pinned source ref; no unsupported price or data path presumed.
6. **Causality:** 100 complete-bar flat warmup, strictly backward indicator windows, no incomplete bar, no future shift, decision `open+4h`, fill only on following completed bar, timestamp correction and explicit historical close-fill limitation.

`hb_ready_status: PASS` is **the Scout's proposed expressibility assessment for this declared derivative**, not an independent Auditor approval, an assertion about the original indicator's lossless behavior, a completed executable implementation, or authorization to merge. Exact-head independent Hermes Auditor review controls acceptance.

## Evidence and negative evidence

**Source-reported:** the original indicator's RSI-vs-smoothed-RSI-Bollinger lower/upper crossing signals and optional modules, with author/publication/update dates cited above. It does **not** report any reproducible strategy performance adopted here.

**Independently reproduced:** **none** — no TradingView/Pine backtest, Qlib/Hummingbot backtest, trade-by-trade parity, live fill, fee quote, PnL or OOS result was generated.

**Unavailable/not claimed:** original Pine version/bytes/defaults; precise source smoothing and Bollinger standard-deviation estimator; original signal filter toggles, divergence timing and broker/order execution; exchange live fills, precision and slippage; full independent re-audit of every existing main strategy frontmatter; implementation and parity. All decision-critical unknowns were **chosen and disclosed as derivative rules** rather than silently imputed to the source. This derivative is not a source-native replacement.

## Falsification plan and research boundary

After separate implementation authorization, replay a representative contiguous 4h sequence containing lower-envelope rebound, zero-band-variance, upper-envelope crossdown, rejected BUY, queued last-bar action and an open terminal position. Compare signal indices, `open+4h` decision times, following-bar MARKET fill indices/amounts, quote fees and net position between the minimal controller and Qlib before mass screening of any newly unverified execution capability. A subsequent fixed-cost IS/OOS research campaign may test whether the envelope adds value over plain RSI thresholds; no retuning on OOS and no performance promise.

Only the described ETH-USDT spot 4h research derivative is covered. Downstream 7-coin/1h-4h-1d/BO+SO 6/6/6/futures leverage campaigns are **separate optional experiments**, not this record's HB_READY prerequisites. Any overlay changing entry/exit events requires its own explicit derivative identity and cost/causality evidence.

## Implementation status and adoption boundary

`implementation_status: not-implemented`. This Markdown is a frozen research specification, **not** a Hummingbot controller or Qlib entrypoint. When formally selected without an executable artifact, the repository's existing `IMPLEMENTATION_NEEDED` engineering route applies; it is not a second admission status. `status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. No Paper/Testnet/Live permission. Only the independent Hermes Auditor may approve/merge the exact reviewed PR head; only the existing signed webhook receiver may update the README count after merge.

## Sources

- TradingView primary: https://www.tradingview.com/script/8fzZ9aWv-rsi-bb-stddev-signal/ (trade_lexx, 2024-12-19; latest visible update 2025-07-29).
- Pinned Hummingbot VERSION: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/VERSION
- Pinned Binance spot intervals: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py
- Pinned Binance spot REST timestamp parser: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py
- Pinned MARKET close-fill: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py
- Pinned backtest/position-hold/fee accounting: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/backtesting_engine_base.py
- Pinned order config: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/executors/order_executor/data_types.py
- Prior package/source identity evidence (not rehashed here): https://github.com/HCH725/alpha-strategy-research/pull/414
