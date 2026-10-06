---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Wilder RSI27 crossing its own SMA10 two-sided reversal system on BTCUSDT 1d bars
created: 2026-10-07
updated: 2026-10-07
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: high
source_as_of: 2023-11-07
sources:
  - https://www.fmz.com/strategy/431398
  - https://www.tradingview.com/pine-script-reference/v4/#fun_strategy
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Wilder RSI27 crossing its own SMA10 two-sided reversal system on BTCUSDT 1d bars

## Provenance

Primary source read end to end (FMZ public strategy page, verified live plus pinned mirror):

- FMZ strategy page: https://www.fmz.com/strategy/431398 (page title `RSI均线交叉策略RSI-Moving-Average-Crossover-Strategy`, author `ChaoZhang`, last modified `2023-11-07 15:35:58`).
- The live page was fetched 2026-10-07 (781225 bytes) and embeds the executable Pine block verbatim, including `strategy("RSI w MA Strategy"` and `process_orders_on_close=true`, with the same `ChaoZhang` author tag — page and code provenance agree, no repost/attribution mismatch.
- Executable artifact: one `//@version=4` Pine block with one live `strategy()` declaration (`RSI w MA Strategy`, `process_orders_on_close=true`), one explicit Wilder-style RSI construction (27), one `sma(rsi, 10)`, one `crossover` / one `crossunder` assignment, and four order calls (close-opposite + entry per signal side). Display-only `plot`/`plotshape`/`hline` calls carry no trade semantics.
- FMZ backtest header printed verbatim in the artifact: `start: 2022-10-31 00:00:00`, `end: 2023-11-06 00:00:00`, `period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`. This header is the source's own executable scope (not a signal rule); `period: 1d` pins the single decision timeframe and `Futures_Binance BTC_USDT` pins the BTCUSDT research market. `basePeriod: 1h` is FMZ execution granularity only: every rule reads completed daily-bar values under `process_orders_on_close=true` with no intrabar, MTF, or clock call, so no 1h signal is inferred.
- Mirror bytes pinned 2026-10-07: file 9239 bytes, SHA-256 `c7d5a36a3c425571739cb4dece7d236995f95fb6ea2c0646063127ea648b8029`. No second immutable host (GitHub blob) exists, so provenance is the FMZ stable URL plus these bytes — traceable and public, without commit-SHA immutability, which is stated rather than hidden.

Pre-write dedup (2026-10-07): working-tree search for `431398`, `RSI w MA`, and `rsi-ma` returned 0 strategy records; the four loose `rsi`/`moving average` text mentions (`drm-dynamic-rsi-momentum`, `sonic-r-rsi-dual-leg-long`, `ibs-mean-reversion-short`, `ehma-range-band`) are materially different mechanisms (dynamic RSI-band momentum, EMA-channel plus RSI dip-recovery long leg, IBS fade, EHMA band — none crosses RSI against its own moving average). `gh pr list --state open` shows only #36 (`reconstruction/legacy-family-quantaalpha`, non-Scout family record — different source, different mechanism). Closed research PRs (#6 WaveTrend, #10 golden/dead cross, #17 MACD, #20 Ichimoku-RSI, plus merged #5 Gann, #7 P-Signal, #9 VIDYA, #12 Bookstaber, #21 Kaufman pivot, #22 EHMA, #23 DMI, #25 Ichimoku-ADX, #28 DRM, #29 Monday-drift, #31 Donchian, #32 Flying-Dragon, #34 EMA-cross, #35 Stochastic-OTT, #37 IBS, #38 Sonic R) contain no RSI-vs-own-average crossover system. Five-axis distinction: mechanism differs (self-referential smoothing cross — RSI crossing its own SMA — versus level-based RSI, channel, band, calendar, or candle-count triggers), signal construction differs (explicit Wilder-form RSI(27) on `close` smoothed again by SMA(10), no other record smooths an oscillator with its own average), horizon/market is `1d` BTCUSDT two-sided reversal, source identity differs (FMZ 431398), and direction handling is symmetric long/short reversal versus long-only or level-fade records.

## Economic mechanism

### Source-reported

- Premise, as printed: RSI judges overbought/oversold conditions while a moving average filters random fluctuation; crossing the two identifies trend-reversal points, and the combination filters false signals better than either alone.
- The page claims the idea suits trending crypto and admits its limits in prose: wrong period parameters generate false signals, crossover-only logic cannot avoid traps, costs matter, and no stop-loss is coded. The coded edge is purely the two crossover signals.

### Research interpretation

- Falsifiable mechanism hypothesis: smoothing RSI(27) with its own SMA(10) creates an adaptive trigger line that rises and falls with the oscillator's own regime; a cross of RSI through its average marks a momentum-state change rather than a fixed-level excursion, so the system stays invested through level-pinned overbought/oversold stretches and flips only when momentum itself turns. Long leg and short leg are mirror images and independently falsifiable (F1 splits sides).
- The explicit Wilder construction matters: because the formula is coded bar-by-bar (`rma` of gains/losses) instead of calling a black-box `ta.rsi`, smoothing, source price, and the divide-by-zero edges are all pinned in the artifact itself.

## Signal

Exact executable semantics, read from the pinned block (nothing inferred, nothing added):

- Source price: `close` (`src = close`).
- RSI construction (explicit Wilder form, fixed lookback 27, `rma` smoothing): `up = rma(max(change(src), 0), 27)`, `down = rma(-min(change(src), 0), 27)`, `rsi = down == 0 ? 100 : up == 0 ? 0 : 100 - (100 / (1 + up / down))`. The `down == 0` / `up == 0` ternaries are coded divide-by-zero guards, not reviewer additions.
- Trigger line: `ma = sma(rsi, 10)` (simple average of the RSI series, fixed window 10). Defaults 27/10 are the artifact's `input` defvals, corroborated by the page's Strategy Arguments table (`Length = 27`, `RSI MA Window = 10`); the record pins these defaults.
- Triggers: `buySignal = crossover(rsi, ma)` (RSI was at/below its average on the prior confirmed bar and is above it now); `sellSignal = crossunder(rsi, ma)` (mirror image). Pine cross semantics on confirmed bars are deterministic and need no reviewer invention.
- Trade control: on `buySignal`, `strategy.close("Short", qty_percent = 100)` then `strategy.entry("Long", strategy.long, qty = .1)`; on `sellSignal`, `strategy.close("Long", qty_percent = 100)` then `strategy.entry("Short", strategy.short, qty = .1)`. The book reverses on every opposite signal and is always in the market after the first signal (no flat state by construction).
- Direction: both sides explicit; neither side disabled.
- Dead code, provably inert: `testPeriod() => true` is a constant-true function, so the `if testPeriod()` wrapper and all backtest-window `timestamp` inputs gate nothing; `band1/band0 = hline(70/30)` and all `plot`/`plotshape` calls are display-only — the 70/30 levels never enter any condition.
- No MTF: zero `request.*`/`security(`/`timeframe` calls. No volume, funding, OI, book, news, or session call anywhere in the executable block (`time` appears only inside the inert window inputs).

## Required data

- OHLCV daily bars of one pair (BTCUSDT) only; the signal consumes `close` alone.
- Deterministic causal indicators only: `change`, `max`/`min`, `rma`, `sma`, `crossover`/`crossunder` on confirmed bars.
- No unsupported feed: no funding, open interest, mark/index price, liquidation, trade/aggressor, L2, on-chain, options, sentiment, macro, or cross-venue state.

## Execution assumptions

- Decision on completed bar, execution at same-bar close: `process_orders_on_close = true` is coded, and `calc_on_every_tick` is unset (Pine default `false`), so no intrabar evaluation path exists — Gate 7 compatible with no approximation.
- Order sizing in code (`qty = .1` shares, `qty_percent = 100`, `initial_capital = 10000`, `currency = 'USD'`) is pure accounting and event-neutral: it never alters signal, timing, direction, or exits. Downstream applies the labeled house overlay (Base 6% + Safety 6% + 6%, Isolated, 3x/5x) and must not present it as source-native.
- Pyramiding unset: the documented engine default `0` applies — at most one same-direction position; a repeated same-side signal while already positioned is rejected (no-op), and the opposite-signal branch closes the current side before reversing. Re-entry behavior is therefore explicit and needs no invented cooldown.
- Risk fields: stop-loss, take-profit, trailing, and time-limit are all absent from the code — explicitly none/disabled, no silent defaults assumed. The page prose itself confirms no stop is coded.
- Warmup: RSI(27) needs 27 closes to seed `rma`, plus 10 more for `sma(rsi, 10)` — about 37 daily bars before the first signal can print; all lookbacks are known, no repaint, no negative shift, no future reference.

## Evidence

### Source-reported

- The page carries no numeric performance table, figure, or claimed ROI/Sharpe — only prose advantages/risks and the FMZ execution-scope header (`2022-10-31` to `2023-11-06`, `1d`, `Futures_Binance BTC_USDT`), which is an evaluation window, not a result. No number is reproduced here because none is traceably claimed.

### Independently reproduced

- Not independently reproduced.

### Negative evidence

- No stop-loss exists in the executable block; the source prose flags this as a drawdown risk. Any downstream evaluation must carry the full unprotected reversal book, not an assumed stop.

## Falsification plan

- F1 (side split): run long-only and short-only variants on BTCUSDT 1d; a symmetric edge predicts both sleeves contribute, while a one-sided result falsifies the reversal symmetry.
- F2 (self-smoothing necessity): replace `sma(rsi, 10)` with fixed 50-level cross rules; if fixed levels match or beat the cross, the adaptive-trigger hypothesis is falsified.
- F3 (engine parity): replay the pinned Pine bar-by-bar against the Hummingbot implementation trade by trade (signal bar, side, fill price = bar close); any divergence falsifies the lossless claim.

## Crypto portability

- Research market is BTCUSDT (Binance USDT-M perpetual) on `1d`, inside the house universe — no cross-venue substitution. Contract identity is preserved from the source header, not chosen for convenience.
- Portability beyond BTCUSDT/1d is untested and not claimed; the 27/10 parameterization is pinned as the source default, not tuned here.

## Limitations

- Always-in-market reversal: the book holds a position through chops with no flat state and no stop; whipsaw regimes can compound consecutive reversal losses.
- Fixed 27/10 parameters are source defaults, not robustness-tested here; sensitivity analysis is left to downstream screening under the house overlay.
- Single-pair, single-timeframe by construction; no MTF confirmation exists to lean on.

## Implementation status

- `not-implemented`: normalized from the pinned Pine block; no Hummingbot/Qlib implementation, no backtest, no Paper/Testnet/Live action taken or authorized by this record.

## Adoption boundary

- `not-approved`, `research-only`. PASS status asserts lossless semantic expressibility under the pinned Hummingbot baseline only — not profitability, not reproduction of source performance, not survivor promotion, and not trading approval.

## Related Wiki records

- None (no Wiki write performed in the Scout lane).

## Sources

- FMZ public strategy page (primary, with embedded executable Pine): https://www.fmz.com/strategy/431398
- Pine Script v4 `strategy()` reference (engine defaults incl. pyramiding): https://www.tradingview.com/pine-script-reference/v4/#fun_strategy
- Pine Script strategy concepts (order/execution semantics): https://www.tradingview.com/pine-script-docs/concepts/strategies/
- Pinned mirror: scout corpus `f00798.md`, 9239 bytes, SHA-256 `c7d5a36a3c425571739cb4dece7d236995f95fb6ea2c0646063127ea648b8029` (2026-10-07; live page re-fetched same day, 781225 bytes, code parity confirmed)
