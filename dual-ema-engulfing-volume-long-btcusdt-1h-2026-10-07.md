---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Dual-EMA engulfing with volume-confirmed long system on BTCUSDT 1h bars
created: 2026-10-07
updated: 2026-10-07
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: high
source_as_of: 2023-12-07
sources:
  - https://www.fmz.com/strategy/434564
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Dual-EMA engulfing with volume-confirmed long system on BTCUSDT 1h bars

## Provenance

Primary source read end to end (FMZ public strategy page, verified live plus pinned mirror):

- FMZ strategy page: https://www.fmz.com/strategy/434564 (page title `指数均线封闭突破策略|Dual EMA Engulfing Breakout Strategy`, author `ChaoZhang`, `Created: 2023-12-07 15:50:13`, last-modified shown relatively as ~3 years ago).
- The live page was fetched 2026-10-07 (772662 bytes) and embeds the executable Pine block verbatim, including `strategy(` with `title = "fpemehd Strategy001"`, `process_orders_on_close = true`, and the same `ChaoZhang` author tag — page and code provenance agree.
- Executable artifact: one Pine block with one live `strategy()` declaration, two `ta.ema()` calls, one `strategy.entry(id = "Long", direction = strategy.long)` inside `if long_signal and time_cond`, one `strategy.close(id = "Long")` inside `if close_signal and time_cond`; no `strategy.exit`/`strategy.close_all`/`strategy.order`/`strategy.cancel`, no stop/limit args, no second entry path. Display-only `overlay = true` carries no trade semantics.
- FMZ backtest header printed verbatim in the artifact: `start: 2023-11-06 00:00:00`, `end: 2023-12-06 00:00:00`, `period: 1h`, `basePeriod: 15m`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`. This header is the source's own executable scope (not a signal rule); `period: 1h` pins the single decision timeframe and `Futures_Binance BTC_USDT` pins the BTCUSDT research market. `basePeriod: 15m` is FMZ execution granularity only: every rule reads completed hourly-bar OHLCV values under `process_orders_on_close = true` with no intrabar, MTF, or clock call, so no 15m signal is inferred.
- Mirror bytes pinned 2026-10-07: scout corpus `f04626.md`, 7708 bytes, SHA-256 `27f8186ee710068f4b44dfda591de7d44ac4f61a22a9bc41a5ae4b5dae5b4829`; executable code block inside it is 2774 bytes, SHA-256 `4880d5a8516f1863e8431aa1f8cd73e4537ba919ca8c316a40220aa97e8bbf74`. Live-page tail (entry/exit lines) verified character-identical to the mirror block. No second immutable host (GitHub blob) exists, so provenance is the FMZ stable URL plus these bytes — traceable and public, without commit-SHA immutability, which is stated rather than hidden.

Pre-write dedup (2026-10-07): working-tree search for `434564`, `engulf`, `Engulf`, and `fpemehd` returned 0 strategy records. The nearest neighbor, `ema-20-50-cross-btcusdt-1h-2026-10-06.md`, is a bare dual-EMA cross with no candlestick-pattern, body-ratio, or volume gate — a different signal construction, not a parameter variant. Loose `ema` text mentions (`drm-dynamic-rsi-momentum`, `sonic-r-rsi-dual-leg-long`, `flying-dragon-offset-ma-band-trend`, `rsi-ma-crossover-reversal`) are RSI/channel/band/cross-of-smoothing mechanisms, none combining EMA alignment with engulfing plus volume confirmation. `gh pr list --state open` shows only #36 (`reconstruction/legacy-family-quantaalpha`, non-Scout family record — different source, different mechanism). Closed research PRs (#6 WaveTrend, #10 golden/dead cross, #17 MACD, #20 Ichimoku-RSI, plus merged #5 Gann, #7 P-Signal, #9 VIDYA, #12 Bookstaber, #21 Kaufman pivot, #22 EHMA, #23 DMI, #25 Ichimoku-ADX, #28 DRM, #29 Monday-drift, #31 Donchian, #32 Flying-Dragon, #34 EMA-cross, #35 Stochastic-OTT, #37 IBS, #38 Sonic R, #39 RSI-MA, #40 RSI-Classic) contain no EMA-plus-engulfing-plus-volume long system. Five-axis distinction: mechanism differs (trend-alignment gate AND pattern gate AND volume gate versus any single-gate system on `main`), signal construction differs (four-condition conjunction plus two-condition disjunctive exit — no bare cross or level trigger), horizon is `1h` BTCUSDT long-only, source identity differs (FMZ 434564), and direction handling is long-only with no short path versus two-sided records.

## Economic mechanism

### Source-reported

- Premise, as printed: dual-EMA direction defines the tradeable regime; a bullish engulfing bar with expanding volume shows sudden long-force entry worth chasing; EMA direction reversal or a bearish engulfing bar shows force exhaustion and triggers exit without a fixed stop, saving whipsaw stop-slippage.
- The page admits its limits in prose: EMA regime can misfire, engulfing misleads in chop, and no fixed stop means larger adverse excursions — suggesting extra filters or break-even stops, none of which is coded.

### Research interpretation

- Falsifiable mechanism hypothesis: hourly BTCUSDT trends persist once alignment, pattern expansion, and participation agree; requiring all four long gates (regime + engulfing + two non-doji bodies + 1.2x volume) buys only expansion bars inside uptrends, while the disjunctive exit (regime flip OR bearish engulfing) cuts the long when force flips. Each gate is independently ablatable (F1/F2 split volume versus body-ratio gates).
- The conjunction structure matters: no single condition trades alone, so partial-signal paraphrases (e.g. EMA-cross-only) are not this strategy.

## Signal

Exact executable semantics, read from the pinned block (nothing inferred, nothing added):

- Source prices: `close` (both EMAs), plus `open`/`high`/`low` for the engulfing geometry and `volume` for the participation gate — all from the same completed hourly bar.
- Indicator variants: `ta.ema(source = close, length = 15)` short leg and `ta.ema(source = close, length = 30)` long leg ( Pine v5 `ta.*` namespace; the `// @version=5` pragma carries a stray leading space but every called function exists with identical semantics, so no variant ambiguity follows from the spacing quirk).
- Regime: `C_uptrend := close > C_ema_short and C_ema_short > C_ema_long`; `C_downtrend := close < C_ema_short and C_ema_short < C_ema_long` — strict comparisons, no crossover tie to resolve.
- Engulfing geometry: bullish `= (open[1] > close[1] and open <= close) and (low < low[1] and high > high[1])`; bearish mirrors with `<`/`>=` — exact bar-pair relations on confirmed bars.
- Body filter: prior- and current-bar body-to-range ratios in percent must both exceed `I_body` (input default `1`, min `1`, max `5`, step `0.1`); the record pins the default `1`.
- Volume gate: `volume > volume[1] * 1.2` — exact 20% expansion factor on the same-bar pair.
- Entry: `if long_signal and time_cond` → `strategy.entry(id = "Long", direction = strategy.long)`, where `long_signal = C_uptrend and C_bullish_engulfing and C_avoid_doge and C_volume_filter`.
- Exit: `if close_signal and time_cond` → `strategy.close(id = "Long")`, where `close_signal = C_downtrend or C_bearish_engulfing`.
- Direction: long-only; no short entry, no short close, no short path exists anywhere in the block — short side explicitly disabled by absence.
- Dead code, provably inert: `time_cond = true` is a constant, so the `and time_cond` suffix gates nothing; `I_start_date`/`I_finish_date` inputs are never referenced by any condition.
- No MTF: zero `request.*`/`security(`/`timeframe` calls. No funding, OI, mark/index, book, news, macro, session, or clock call anywhere in the executable block.

## Required data

- OHLCV hourly bars of one pair (BTCUSDT) only; the signal consumes `open`, `high`, `low`, `close`, and `volume` (the `V` in OHLCV — no external feed).
- Deterministic causal indicators only: two fixed-length EMAs plus exact bar-geometry comparisons and one volume-multiple comparison on confirmed bars.
- No unsupported feed: no funding, open interest, mark/index price, liquidation, trade/aggressor, L2, on-chain, options, sentiment, macro, or cross-venue state.

## Execution assumptions

- Decision on completed bar, execution at same-bar close: `process_orders_on_close = true` is coded, and `calc_on_every_tick` is unset (Pine default `false`), so no intrabar evaluation path exists — Gate 7 compatible with no approximation.
- Order sizing in code (`default_qty_type = strategy.percent_of_equity`, `default_qty_value = 100`, `initial_capital = 10000000`, `commission_type = strategy.commission.cash_per_order`, `commission_value = 0.01`, `slippage = 0`) is pure accounting and event-neutral: it never alters signal, timing, direction, or exits. Downstream applies the labeled house overlay (Base 6% + Safety 6% + 6%, Isolated, 3x/5x) and must not present it as source-native.
- Pyramiding unset: the documented engine default `0` applies — at most one long; a repeated qualifying bar while already long is rejected (no-op), and either exit disjunct closes the position. Re-entry is immediate on the next fully qualifying bar after an exit; no cooldown is coded — explicitly none, not missing.
- Risk fields: stop-loss, take-profit, trailing, and time-limit are all absent from the code — explicitly none/disabled, no silent defaults assumed. The page prose itself confirms no fixed stop is coded.
- Warmup: the longest lookback is EMA(30), plus one-bar `[1]` references — the first fully evaluable signal prints after 30 completed hourly closes; all lookbacks are known, no repaint, no negative shift, no future reference.
- Edge behavior, verified in-code (no invention): a zero-range bar makes a body ratio divide by zero → Pine `na` → the `>` comparison fails → `C_avoid_doge` is false → no entry; the first bar's `volume[1]` is `na` → the volume gate fails → no entry. Both degenerate cases safely suppress signals by construction.

## Evidence

### Source-reported

- The page carries no numeric performance table, figure, or claimed ROI/Sharpe — only prose advantages/risks and the FMZ execution-scope header (`2023-11-06` to `2023-12-06`, `1h`, `Futures_Binance BTC_USDT`), which is an evaluation window, not a result. No number is reproduced here because none is traceably claimed.

### Independently reproduced

- Not independently reproduced.

### Negative evidence

- No fixed stop exists in the executable block; the source prose flags regime misfires, chop-induced engulfing traps, and stop-less drawdown as risks. Any downstream evaluation must carry the full unprotected long-flat book, not an assumed stop.

## Falsification plan

- F1 (volume-gate ablation): drop only the `volume > volume[1] * 1.2` conjunct; if performance is unchanged, the participation gate carries no edge and the volume hypothesis is falsified.
- F2 (body-filter ablation): relax `I_body` to `0` (any engulfing qualifies); if results match the pinned `1`, the anti-doji filter is falsified.
- F3 (engine parity): replay the pinned Pine bar-by-bar against the Hummingbot implementation trade by trade (signal bar, side, fill price = bar close); any divergence falsifies the lossless claim.

## Crypto portability

- Research market is BTCUSDT (Binance USDT-M perpetual) on `1h`, inside the house universe — no cross-venue substitution. Contract identity is preserved from the source header, not chosen for convenience.
- Portability beyond BTCUSDT/1h is untested and not claimed; the 15/30/1%/1.2x parameterization is pinned as the source default, not tuned here.

## Limitations

- Long-flat book with no short leg and no stop: prolonged downtrends simply keep the system flat, but a qualifying expansion bar near a local top can still enter before the disjunctive exit fires.
- Volume-spike dependence: low-participation grinds rarely qualify, so the system may sit out long stretches; volume-print differences across venues could shift signals.
- Fixed 15/30/1%/1.2x parameters are source defaults, not robustness-tested here; sensitivity analysis is left to downstream screening under the house overlay.
- Single-pair, single-timeframe by construction; no macro or session filter exists to lean on.

## Implementation status

- `not-implemented`: normalized from the pinned Pine block; no Hummingbot/Qlib implementation, no backtest, no Paper/Testnet/Live action taken or authorized by this record.

## Adoption boundary

- `not-approved`, `research-only`. PASS status asserts lossless semantic expressibility under the pinned Hummingbot baseline only — not profitability, not reproduction of source performance, not survivor promotion, and not trading approval.

## Related Wiki records

- None (no Wiki write performed in the Scout lane).

## Sources

- FMZ public strategy page (primary, with embedded executable Pine): https://www.fmz.com/strategy/434564
- Pine Script v5 `strategy()` reference (engine defaults incl. pyramiding): https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
- Pine Script strategy concepts (order/execution semantics): https://www.tradingview.com/pine-script-docs/concepts/strategies/
- Pinned mirror: scout corpus `f04626.md`, 7708 bytes, SHA-256 `27f8186ee710068f4b44dfda591de7d44ac4f61a22a9bc41a5ae4b5dae5b4829` (2026-10-07; live page re-fetched same day, 772662 bytes, entry/exit tail parity confirmed)
