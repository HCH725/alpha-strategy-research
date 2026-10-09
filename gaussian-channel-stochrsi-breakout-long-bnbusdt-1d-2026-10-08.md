---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Gaussian channel StochRSI-gated breakout long system on BNBUSDT 1d bars
created: 2026-10-08
updated: 2026-10-08
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-08
sources:
  - https://www.fmz.com/strategy/482888
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Gaussian channel StochRSI-gated breakout long system on BNBUSDT 1d bars

## Provenance

Primary source actually read end to end (sole artifact for all rule citations):

- FMZ strategy page: https://www.fmz.com/strategy/482888 — `Trend Reversal Quantitative Trading Strategy Based on Gaussian Channel and Stochastic RSI`, author `SAJJAD JAMSHIDI`, `Last Modified 2025-02-20 16:41:36`.
- Live page re-fetched by Hermes on 2026-10-08 (HTTP 200, 722,767 bytes). The embedded `//@version=5` Pine block is semantically identical to the pre-existing local FMZ mirror copy (`scout-20261007/f03714.md`): strategy header (`process_orders_on_close=true`), Gaussian-channel formulas, StochRSI chain, `priceAboveUpper` / `priceBelowUpper` conditions, and the single `strategy.entry` + single `strategy.close` all match verbatim.
- FMZ backtest header printed verbatim in the source: `start: 2024-02-21 00:00:00`, `end: 2025-02-18 08:00:00`, `period: 1d`, `basePeriod: 1d`, `exchanges: [{"eid":"Binance","currency":"BNB_USDT"}]`. This header is the source's own executable scope (not a signal rule) and is the sole source of the pinned `1d` decision timeframe; downstream must declare its own evaluation window rather than silently re-tuning it.
- Source market identity: BNB spot daily bars on Binance. The research market below is `BNBUSDT 1d` under the explicit house overlay (a pinned-universe symbol); the spot-vs-perpetual basis difference is not part of the signal logic (closes only, no funding/spot-specific rule) and is labeled here, not hidden.
- The page prints no numeric performance (no ROI, win rate, Sharpe, drawdown, or trade list) in either the Chinese or English description blocks. This record therefore reports no source performance numbers and invents none.

Pre-write dedup (2026-10-08): case-insensitive search of the working tree for `gaussian`, `482888`, `sajjad` returns only an unrelated erf-math sentence in `p-signal-erf-dead-band-reversal-btcusdt-1h-2026-10-05.md` (Gaussian error-function mapping, different mechanism). `gh pr list --state open` shows only PR #48 (Larry Williams 3-EMA channel streak long, different channel/gate/source) and PR #36 (non-Scout `reconstruction/*` lane, different family) — no open `research/*` PR shares this source or signal. Against `main`: the closest records are `sideways-dmi-bollinger-breakout-long-btcusdt-4h` (SMA-20 basis, DMI sideways gate, *lower*-band reversal entry, 4h, BTC) and `stochastic-ott-dual-trend-btcusdt-1d` (dual-OTT flips, Stochastic leg disabled by default, Futures BTC) — this candidate differs in channel basis (EMA vs SMA), gate family (StochRSI k>d momentum vs DMI/OTT), entry side (upper-band breakout vs lower-band reversal), timeframe/market, and exit, so it is a materially distinct mechanism, not a trivial parameter variant. The five RSI-family records on `main` trade RSI levels/crosses directly; here StochRSI is only a k>d permission gate on a channel breakout, a different signal construction.

## Economic mechanism

### Source-reported

The source claims only qualitative behavior (no numbers anywhere): the Gaussian channel (EMA basis plus/minus two standard deviations) frames the prevailing volatility band, and Stochastic RSI momentum confirmation filters false breakouts; longs are taken on upside band breaks confirmed by rising StochRSI momentum and exited when price falls back through the upper band. No behavioral, structural, or risk-premium channel beyond breakout-plus-momentum-filter is claimed.

### Research interpretation

Falsifiable hypothesis: on daily bars, a close crossing strictly above an EMA-20 two-sigma band while StochRSI short momentum (K) exceeds its own average (D) marks upside pressure strong enough to carry for days; the cross back below the same band marks exhaustion. The backtest window and commission lines are source executable scope, not edge claims. This is a ported breakout hypothesis; the source supplies no quantitative evidence (see Evidence), so the mechanism is research interpretation, not source-reported fact.

## Signal

Exact rule as pinned (Pine v5, defaults quoted — inputs unmodified):

- Gaussian channel: `lengthGC = 20`, `multiplier = 2.0`; `basis = ta.ema(close, 20)`; `deviation = 2.0 * ta.stdev(close, 20)` (v5 `ta.stdev` default `biasCorrect = true`, i.e. sample standard deviation); `upperChannel = basis + deviation`; `lowerChannel = basis - deviation`. The lower band is plotted only and never read by any order condition — inert.
- RSI: `rsi = ta.rsi(close, 14)` (v5 RMA-smoothed Wilder RSI, deterministic).
- Stochastic RSI (explicit ratio, not a built-in): `lowestRSI = ta.lowest(rsi, 14)`; `highestRSI = ta.highest(rsi, 14)`; `stochRSI = (rsi - lowestRSI) / (highestRSI - lowestRSI) * 100`; `k = ta.sma(stochRSI, 3)`; `d = ta.sma(k, 3)`.
- Gate: `stochUp = k > d` — strict inequality; equality does NOT pass.
- Entry trigger: `priceAboveUpper = ta.crossover(close, upperChannel)` — strict v5 cross-over (`close[1] <= upper[1]` AND `close > upper`); touching without crossing does not enter.
- Exit trigger: `priceBelowUpper = ta.crossunder(close, upperChannel)` — strict cross-under; touching without crossing does not exit.
- Entry (long only): `strategy.entry("Long", strategy.long, when = priceAboveUpper and stochUp)`.
- Exit (long only): `strategy.close("Long", when = priceBelowUpper)`.
- Direction: long entry explicit; no `strategy.short` leg exists anywhere (0 occurrences) — short explicitly disabled per code.
- Opposite-signal exit: not applicable (no short side); the only exit is the upper-band signal exit above.
- Risk: stop loss none, take profit none, trailing stop none, time limit none — no such input or call exists in the file. No silent defaults relied upon.
- Position / re-entry: `pyramiding` unset = Pine v5 language default (0, single position, no same-direction adds); no cooldown input; no `strategy.position_*` read; no position-aware state. After an exit, the next bar satisfying entry conditions re-enters immediately. Sizing/capital lines (`default_qty_type = strategy.percent_of_equity`, `default_qty_value = 100`, `initial_capital` unset = Pine default) and cost lines (`commission_type = strategy.commission.percent`, `commission_value = 0.1`, `slippage = 0`) are event-neutral capital/accounting configuration, replaced by the house overlay.
- Timing: `process_orders_on_close = true`; `calc_on_every_tick` omitted = Pine v5 default false. Completed-bar decision with same-bar-close execution; no intrabar path dependence.
- Order inventory (whole executable block): exactly one `strategy.entry` and one `strategy.close`; 0 `strategy.exit`, 0 `strategy.order`, 0 `strategy.cancel`, 0 `limit=`, 0 `stop=`, 0 `qty_percent`, 0 `request.*`, 0 `time(`, 0 `timenow`, 0 `timeframe.`, 0 `dayofweek`/`dayofmonth`/`hour`, 0 `volume`, 0 `openinterest`, 0 funding/OI/mark-price references. No date-range gate exists — the system is always active.
- Edge case (deterministic, stated not patched): a 14-bar window with perfectly flat RSI makes `highestRSI - lowestRSI = 0`, so `stochRSI` (and hence `k`, `stochUp`) evaluates to `na`; `na` conditions are false in Pine, so no entry fires. Touching-but-not-crossing bars likewise never fire. Both behaviors follow directly from the pinned code.

**Lookback, formulas and warmup**

- Parameters as declared: channel 20 over `close` with multiplier 2.0; RSI 14; Stochastic window 14; smoothK 3; smoothD 3.
- All indicators are causal (current-bar `ema`/`stdev`/`rsi`/`lowest`/`highest`/`sma` over completed bars only); no negative shift, no future extrema, no full-sample normalization, no repaint path.
- Derived warmup: longest primitive chain is RSI(14) → 14-bar RSI extrema → SMA(3) → SMA(3), i.e. about 32 bars; channel needs 20. Conservative derived warmup: 40 completed 1d bars before the first signal bar is trusted.

## Required data

- `BNBUSDT` (research market under house overlay; source is BNB spot 1d) OHLCV at `1d`.
- Deterministic candle-derived indicators only (EMA, sample standard deviation, Wilder RSI, lowest/highest, SMA). No funding, open interest, mark/index price, liquidation feed, trade feed, order book, on-chain, options, sentiment, macro, or cross-venue state.

## Execution assumptions

- Completed-bar decision with same-bar-close execution per `process_orders_on_close = true` under the pinned Hummingbot baseline (`20260920` / `dev-2.17.0`).
- House execution overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) replaces only event-neutral sizing/capital/accounting; signal, timing, direction, entries, exits, and single-position behavior are preserved exactly as sourced.
- Research market `BNBUSDT 1d` is explicitly labeled; source executable scope (BNB spot 1d, 2024-02-21 → 2025-02-18, 0.1% commission, zero slippage) is not presented as downstream configuration.

## Evidence

### Source-reported

None numeric. The FMZ page (live, re-fetched 2026-10-08) and its description blocks print no ROI, Sharpe, win rate, drawdown, or trade list. Recorded here as "no source-reported numbers" — nothing invented, nothing carried over from the source's backtest-window header.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No contradictory evidence located. The flat-RSI `na` path and touch-without-cross path are non-firing by construction (see Signal), so they cannot silently generate trades the backtester would miss.

## Falsification plan

Research tests only (never substitutes for missing rules — no rule is missing):

1. Event-parity replay: implement the pinned formulas verbatim on `BNBUSDT 1d` closes and require trade-by-trade agreement (signal bar, entry/exit bar, direction, quantity under the same overlay) with the Hummingbot run before any performance reading.
2. Parameter-stability probe: vary channel length {15, 20, 25} and StochRSI windows {10/10, 14/14, 20/20} on a frozen pre-registered window; a result that exists only at exactly (20, 14/14/3/3) is curve-fit, not edge.
3. Gate-ablation probe: entry on channel breakout alone vs breakout + `k > d`; if the gate adds no out-of-sample improvement, the mechanism reduces to a plain band breakout.
4. Dead-band check: count touch-without-cross bars near the upper band; if most exits/entries cluster on equality-touch bars, the strict-crossing semantics deserve re-review.

## Crypto portability

Directly portable in construction to any spot/perpetual pair with clean daily closes (indicator-only, no venue-specific input). Portability of *performance* is unproven — BNB-only source scope; any other symbol is a new hypothesis requiring its own evidence, not an inference from this record.

## Limitations

- Long-only by construction; bear-market behavior is unobserved and unclaimed.
- Single exit (upper-band crossunder); gap-through exits and adverse-excursion control are absent by source design.
- `ta.stdev` sample-vs-population convention is pinned to the Pine v5 default (`biasCorrect = true`); re-implementations must match that default exactly.
- Source backtest window (2024-02-21 → 2025-02-18) is one regime sample, not evidence of robustness.
- No source-reported numbers exist, so there is nothing to reproduce yet — only the signal semantics are admitted.

## Implementation status

not-implemented. No Hummingbot/Qlib/n8n/Paper/Testnet/Live work has been performed from this record.

## Adoption boundary

research-only. Not approved for Paper, Testnet, Mainnet, or live trading. Downstream eligibility is read from `hb_ready_status: PASS` under the pinned baseline; presence of this file alone authorizes nothing.

## Related Wiki records

None (no Wiki Brain write is performed by the Scout lane).

## Sources

- https://www.fmz.com/strategy/482888 (primary; read end to end, live-verified 2026-10-08; author SAJJAD JAMSHIDI; last modified 2025-02-20 16:41:36; `period: 1d`, `basePeriod: 1d`, Binance `BNB_USDT`)
