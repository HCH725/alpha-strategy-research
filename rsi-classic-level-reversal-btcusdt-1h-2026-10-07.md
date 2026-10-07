---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: RSI Classic 30/60 level-reversal long system on BTCUSDT 1h bars
created: 2026-10-07
updated: 2026-10-07
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: high
source_as_of: 2024-02-06
sources:
  - https://www.fmz.com/strategy/441161
  - https://www.tradingview.com/pine-script-reference/v4/#fun_strategy
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# RSI Classic 30/60 level-reversal long system on BTCUSDT 1h bars

## Provenance

Primary source read end to end (FMZ public strategy page, verified live plus pinned mirror):

- FMZ strategy page: https://www.fmz.com/strategy/441161 (page title `结合RSI指标与价格突破的短线策略A-Short-term-Strategy-Combining-RSI-Indicator-and-Price-Breakthrough`, author `ChaoZhang`, last modified `2024-02-06 12:01:14`).
- The live page was fetched 2026-10-07 (785447 bytes) and embeds the executable Pine block verbatim, including `strategy("RSI Classic Strategy (by Coinrule)"`, `process_orders_on_close=true`, and the same `ChaoZhang` author tag — page and code provenance agree, no repost/attribution mismatch beyond the stated Coinrule original (`© relevantLeader16058`).
- Executable artifact: one `//@version=4` Pine block with one live `strategy()` declaration, one `rsi(close, 14)` call, one `strategy.entry("long", ...)` and one `strategy.close("long", ...)`; no `strategy.exit`/`strategy.close_all`/`strategy.order`/`strategy.cancel`, no stop/limit args, no second entry path. Display-only `overlay=true` carries no trade semantics.
- FMZ backtest header printed verbatim in the artifact: `start: 2024-01-01 00:00:00`, `end: 2024-01-31 23:59:59`, `period: 1h`, `basePeriod: 15m`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`. This header is the source's own executable scope (not a signal rule); `period: 1h` pins the single decision timeframe and `Futures_Binance BTC_USDT` pins the BTCUSDT research market. `basePeriod: 15m` is FMZ execution granularity only: every rule reads completed hourly-bar values under `process_orders_on_close=true` with no intrabar, MTF, or clock call, so no 15m signal is inferred.
- Mirror bytes pinned 2026-10-07: scout corpus `f05175.md`, 7653 bytes, SHA-256 `d4d69e512287bc8b962b0b2d4340309bc5015a54d67327483d61fa427ddc0094`. No second immutable host (GitHub blob) exists, so provenance is the FMZ stable URL plus these bytes — traceable and public, without commit-SHA immutability, which is stated rather than hidden.

Pre-write dedup (2026-10-07): working-tree search for `441161`, `RSI Classic`, and `rsi-classic` returned 0 strategy records; the loose `rsi` text mentions (`drm-dynamic-rsi-momentum`, `rsi-ma-crossover-reversal`, `sonic-r-rsi-dual-leg-long`, `ibs-mean-reversion-short`, `ehma-range-band`) are materially different mechanisms (dynamic-length RSI momentum, RSI crossing its own SMA, EMA-channel plus RSI dip-recovery long leg, IBS fade, EHMA band — none is a fixed 30/60 level long-only reversal). `gh pr list --state open` shows only #36 (`reconstruction/legacy-family-quantaalpha`, non-Scout family record — different source, different mechanism). Closed research PRs (#6 WaveTrend, #10 golden/dead cross, #17 MACD, #20 Ichimoku-RSI, plus merged #5 Gann, #7 P-Signal, #9 VIDYA, #12 Bookstaber, #21 Kaufman pivot, #22 EHMA, #23 DMI, #25 Ichimoku-ADX, #28 DRM, #29 Monday-drift, #31 Donchian, #32 Flying-Dragon, #34 EMA-cross, #35 Stochastic-OTT, #37 IBS, #38 Sonic R, #39 RSI-MA) contain no fixed-level RSI 30/60 long-only system. Five-axis distinction: mechanism differs (fixed-level oversold/overbought reversal versus self-smoothing cross, dynamic-length, channel, band, calendar, or candle-count triggers), signal construction differs (plain `rsi(close,14) < 30` entry / `> 60` exit with strict level comparisons — no crossover of two series anywhere), horizon is `1h` BTCUSDT long-only, source identity differs (FMZ 441161), and direction handling is long-only with no short path versus two-sided reversal records.

## Economic mechanism

### Source-reported

- Premise, as printed: RSI judges local overbought/oversold extremes; buying below 30 captures short-term oversold bounce, selling above 60 locks in overbought retracement; pursuing short-term rotation efficiency without predicting trend turns.
- The page admits its limits in prose: cannot judge macro trend direction, RSI lags price, needs macro-regime awareness, and suggests adding trend filters or stop-loss — none of which is coded.

### Research interpretation

- Falsifiable mechanism hypothesis: hourly BTCUSDT exhibits short-horizon snap-back after deep RSI washes; a level-triggered long that enters once RSI prints below 30 and holds until RSI prints above 60 harvests that snap-back leg while staying flat through mid-range chop. Long-only and level-symmetric (30/60) legs are independently falsifiable (F1 splits entry/exit thresholds).
- The absence of any crossover call matters: strict level comparisons on confirmed bars are deterministic and need no tie-semantics invention.

## Signal

Exact executable semantics, read from the pinned block (nothing inferred, nothing added):

- Source price: `close` (`rsi(close, lengthRSI)`).
- Indicator variant: Pine v4 built-in `rsi()` (Wilder RSI via `rma` smoothing), fixed lookback 14 (`lengthRSI = 14`, hardcoded — not an optimizable input). Thresholds are `input` defvals corroborated by the Strategy Arguments table (`oversold = 30`, `overbought = 60`); the record pins these defaults.
- Entry: `strategy.entry(id="long", long = true, when = RSI < oversold and window())` — long opens on any completed 1h bar printing RSI below 30.
- Exit: `strategy.close("long", when = RSI > overbought and window())` — the long closes on any completed 1h bar printing RSI above 60.
- Direction: long-only; no short entry, no short close, no short path exists anywhere in the block — short side explicitly disabled by absence.
- Dead code, provably inert: `window() => true` is a constant-true function, so the `and window()` suffix and all backtest-window `timestamp`/`input` declarations gate nothing (defaults span 2020 to 2112, covering all crypto data); `showDate` never enters any condition.
- No MTF: zero `request.*`/`security(`/`timeframe` calls. No volume, funding, OI, book, news, or session call anywhere in the executable block (`timestamp` appears only inside the inert window inputs).

## Required data

- OHLCV hourly bars of one pair (BTCUSDT) only; the signal consumes `close` alone.
- Deterministic causal indicators only: Pine v4 `rsi(close, 14)` plus strict `<` / `>` level comparisons on confirmed bars.
- No unsupported feed: no funding, open interest, mark/index price, liquidation, trade/aggressor, L2, on-chain, options, sentiment, macro, or cross-venue state.

## Execution assumptions

- Decision on completed bar, execution at same-bar close: `process_orders_on_close = true` is coded, and `calc_on_every_tick` is unset (Pine default `false`), so no intrabar evaluation path exists — Gate 7 compatible with no approximation.
- Order sizing in code (`default_qty_type = strategy.percent_of_equity`, `default_qty_value = 30`, `initial_capital = 1000`, `commission_type = strategy.commission.percent`, `commission_value = 0.1`) is pure accounting and event-neutral: it never alters signal, timing, direction, or exits. Downstream applies the labeled house overlay (Base 6% + Safety 6% + 6%, Isolated, 3x/5x) and must not present it as source-native.
- Pyramiding unset: the documented engine default `0` applies — at most one same-direction long; a repeated sub-30 signal while already long is rejected (no-op), and the above-60 branch closes the position. Re-entry is immediate on the next sub-30 bar after an exit; no cooldown is coded — explicitly none, not missing.
- Risk fields: stop-loss, take-profit, trailing, and time-limit are all absent from the code — explicitly none/disabled, no silent defaults assumed. The page prose itself confirms no stop is coded.
- Warmup: RSI(14) needs 14 hourly closes before the first signal can print; all lookbacks are known, no repaint, no negative shift, no future reference.

## Evidence

### Source-reported

- The page carries no numeric performance table, figure, or claimed ROI/Sharpe — only prose advantages/risks and the FMZ execution-scope header (`2024-01-01` to `2024-01-31`, `1h`, `Futures_Binance BTC_USDT`), which is an evaluation window, not a result. No number is reproduced here because none is traceably claimed.

### Independently reproduced

- Not independently reproduced.

### Negative evidence

- No stop-loss exists in the executable block; the source prose flags trend-blindness and RSI lag as drawdown risks. Any downstream evaluation must carry the full unprotected long-flat book, not an assumed stop.

## Falsification plan

- F1 (threshold split): run 30-entry-only versus 60-exit-only sensitivity (e.g. 25/35 entries × 55/65 exits); if performance collapses outside a narrow band, the fixed-level hypothesis is falsified.
- F2 (hold-vs-fade necessity): replace the RSI gate with buy-and-hold over the same window; if buy-and-hold matches or beats the rotation, the snap-back edge is falsified.
- F3 (engine parity): replay the pinned Pine bar-by-bar against the Hummingbot implementation trade by trade (signal bar, side, fill price = bar close); any divergence falsifies the lossless claim.

## Crypto portability

- Research market is BTCUSDT (Binance USDT-M perpetual) on `1h`, inside the house universe — no cross-venue substitution. Contract identity is preserved from the source header, not chosen for convenience.
- Portability beyond BTCUSDT/1h is untested and not claimed; the 14/30/60 parameterization is pinned as the source default, not tuned here.

## Limitations

- Long-flat book with no short leg and no stop: prolonged downtrends can hold the long through deep drawdown until RSI recovers above 60.
- Fixed 14/30/60 parameters are source defaults, not robustness-tested here; sensitivity analysis is left to downstream screening under the house overlay.
- Single-pair, single-timeframe by construction; no trend filter exists to lean on.

## Implementation status

- `not-implemented`: normalized from the pinned Pine block; no Hummingbot/Qlib implementation, no backtest, no Paper/Testnet/Live action taken or authorized by this record.

## Adoption boundary

- `not-approved`, `research-only`. PASS status asserts lossless semantic expressibility under the pinned Hummingbot baseline only — not profitability, not reproduction of source performance, not survivor promotion, and not trading approval.

## Related Wiki records

- None (no Wiki write performed in the Scout lane).

## Sources

- FMZ public strategy page (primary, with embedded executable Pine): https://www.fmz.com/strategy/441161
- Pine Script v4 `strategy()` reference (engine defaults incl. pyramiding): https://www.tradingview.com/pine-script-reference/v4/#fun_strategy
- Pine Script strategy concepts (order/execution semantics): https://www.tradingview.com/pine-script-docs/concepts/strategies/
- Pinned mirror: scout corpus `f05175.md`, 7653 bytes, SHA-256 `d4d69e512287bc8b962b0b2d4340309bc5015a54d67327483d61fa427ddc0094` (2026-10-07; live page re-fetched same day, 785447 bytes, code parity confirmed)
