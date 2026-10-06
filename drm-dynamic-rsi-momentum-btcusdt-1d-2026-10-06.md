---
schema: strategy-research-record-v1
title: QuantNomad DRM dynamic-length RSI momentum system on BTCUSDT 1d bars
created: 2026-10-06
updated: 2026-10-06
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-06
sources:
  - https://www.tradingview.com/script/08eSyDlq-DRM-Strategy/
  - https://github.com/hasnocool/tradingview-pine-scripts/blob/69969aeaf271b2f7b5a7632a1bde43069a0cbe26/DRM%20Strategy.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# QuantNomad DRM dynamic-length RSI momentum system on BTCUSDT 1d bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Mirror repository URL: https://github.com/hasnocool/tradingview-pine-scripts
- Pinned commit SHA: `69969aeaf271b2f7b5a7632a1bde43069a0cbe26` (`ls-remote` HEAD check on 2026-10-06 confirms this is still the repository head, same pin as prior scout cycles).
- Exact file path: `DRM Strategy.pine`.
- GitHub blob SHA at the pinned commit: `5d1e36a788785aca3aac46c832611d184b4014b8`, size 3222 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is byte-identical (`cmp` clean) to the file extracted from the previously vendored mirror archive; SHA-256 `26a12752c255b1ee2972ee7aa73c6413f8a44a608e8dae7b1e429f14071a3a8e`, 3222 bytes.
- The pinned file is a mirror scrape that embeds, in order: `Script Name: DRM Strategy`, `Author: QuantNomad`, the author description (see below), and the full Pine v5 program (76 code lines plus scrape line-number prefixes).

TradingView stable page read directly on 2026-10-06 over HTTPS (public, no login):

- Stable URL: https://www.tradingview.com/script/08eSyDlq-DRM-Strategy/
- Page title: `DRM Strategy by QuantNomad — TradingView`; author credit `QuantNomad` appears throughout the page; the description layer repeats the dynamic-length premise quoted below.
- The page marks the script open-source, which corroborates that the mirrored program text is the published source; no rule in this record is taken from page prose alone — every rule cites the pinned program.

Source description, as printed (truncated mid-sentence in the mirror; recorded exactly, not completed):

```text
One of the ways I go when I develop strategies is by reducing the number of parameters and removing fixed parameters and levels.
In this strategy, I'm trying to create an RSI indicator with a dynamic length.
Length is computed based on the correlation between Price and its momentum.
You can set min and max values for the RSI, and if the correlation is close to 1,...
```

Provenance gaps (stated, not repaired): the mirror truncates the description sentence after "close to 1"; no DOI, no version tag, no test suite, no peer-review statement, and no performance table is cited anywhere in this record. All defaults below are the program's own `input.*` defvals, pinned as read.

Pre-write dedup (2026-10-06): word-boundary search of the working tree for `drm`, `rsiLen`, `QuantNomad`, `Dynamic RSI Momentum`, `rmaFun` returned 0 Markdown matches; `gh pr list --state open` is empty, so no open `research/*` PR shares this source or signal. Against the 8 records on `main`: no record uses an RSI oscillator of any kind (Gann HiLo band state machine, VIDYA CMO-adaptive average, P-Signal erf dead-band, Kaufman pivot breakout, EHMA range band, DMI Swings ADX-45 exhaustion, Ichimoku Cloud + ADX filter, Bookstaber ATR change-penetration) — mechanism, signal construction, and source identity (QuantNomad TV script `08eSyDlq`) are all distinct. The TV-mirror `RSI w MA Strategy` and `Cumulative RSI Strategy` were never admitted and use different constructions (RSI-vs-MA cross, summed RSI with date-window gating).

## Economic mechanism

### Source-reported

The source states the mechanism only as author intent: fewer parameters, no fixed levels where avoidable, and an RSI whose length adapts to the correlation between price and its own momentum. No behavioural, structural, or risk-premium channel is claimed.

### Research interpretation

Falsifiable hypothesis: when price and its 10-bar momentum are strongly positively correlated (trending persistence), the rule lengthens the RSI lookback (up to 50) so that only a deeply washed-out reversal (cross up through 30) triggers a long; when correlation is weak or negative (choppy / reversing tape), it shortens the lookback (down to 20) so the oscillator reacts faster. The short side mirrors this at the 70 line. The bet is regime-adaptive momentum ignition: adaptive smoothing lets the oscillator stay quiet in noise and speak only on correlation-confirmed dislocations, holding the taken side until the mirror-image dislocation arrives. This is a ported technical-analysis hypothesis; the source supplies no sample and no evidence, so the mechanism is research interpretation, not source-reported fact.

## Signal

All symbols below are the program's own identifiers; all values are program defaults, pinned.

Inputs (defaults):

- `len = 10` (Momentum Length), `src = close` (Source), `min_rsi = 20`, `max_rsi = 50`, `upLvl = 70.0`, `dnLvl = 30.0`.

Adaptive length construction (exact, deterministic):

```text
momVal = src - src[len]                                   (10-bar momentum, len = 10)
corr   = ta.correlation(src, momVal, len)                 (Pearson, 10-bar window)
corr   := corr > 1 or corr < -1 ? na : corr               (explicit float-error clamp)
rsiLen := int(min_rsi + nz(round((1 - corr) * (max_rsi - min_rsi) / 2, 0), 0))
```

So `rsiLen` is an integer in `[20, 50]`: correlation +1 maps to 20, correlation −1 maps to 50, `na` correlation maps to 20 via the explicit `nz(..., 0)` fallback. No discretion, no hidden state.

Oscillator (exact custom Wilder-style RSI written out in source, not a black-box call):

```text
rmaFun(s, L): sma = ta.sma(s, L); alpha = 1/L
              sum = 0.0; sum := na(sum[1]) ? sma : alpha*s + (1-alpha)*nz(sum[1])
rsiFun(s, L) = 100 - 100 / (1 + rmaFun(up-move, L) / rmaFun(down-move, L))
rsiMom = rsiFun(src, rsiLen)
```

Trade events (the complete order-call set — two `strategy.entry` calls, zero `strategy.exit`/`close`/`order`/`cancel` calls):

```text
long  = ta.crossover(rsiMom, dnLvl)     (confirmed-bar cross up through 30)
short = ta.crossunder(rsiMom, upLvl)    (confirmed-bar cross down through 70)
if long  and not na(rsiMom) -> strategy.entry("Long",  strategy.long)
if short and not na(rsiMom) -> strategy.entry("Short", strategy.short)
```

Mutual exclusion (provable, not assumed): `long` requires `rsiMom[1] <= 30 < rsiMom`; `short` requires `rsiMom[1] >= 70 > rsiMom`. Both cannot hold on the same bar. With one id per side and the v5 default `pyramiding = 0` (unset in source), same-side re-entry while positioned is rejected by the engine and the next opposite cross reverses the position — the position converges to exactly long-1 or short-1 after the first signal, starting flat. Opposite-signal exit is therefore effected by the reversing entry; stop loss, take profit, trailing stop, and time exit are absent in source and recorded as explicitly disabled, not as defaults to be assumed.

Crossover semantics note for the reviewer: `ta.crossover`/`ta.crossunder` here compare confirmed-bar values against constant levels (30 / 70) under `process_orders_on_close = true`, so both legs are completed-bar decisions with same-bar-close execution. They are preserved exactly as written; no next-bar-open approximation is involved.

Division-by-zero edge (analyzed, source-explicit): if the down-move RMA is zero (unbroken up-tape over the lookback), the RSI division yields `na` in Pine and the `not na(rsiMom)` guard suppresses the signal — the rule goes quiet rather than firing. Port code must reproduce this guard, not a clamped 100.

## Required data

- OHLCV daily bars of one pair; the rule reads `close` only (via default `src = close`).
- Deterministic causal transforms only: `ta.sma`, `ta.correlation`, and the written-out RMA/RSI recursion above.
- No timeframe reference, no `request.*`/`security`, no `barstate.*`, no session/time input, no funding/OI/mark feeds, no order-book, news, or cross-venue state. Warmup is derivable: every lookback is known (`len = 10` momentum/correlation horizon; `rsiLen` bounded in `[20, 50]`; the RMA seed is a 50-bar-max `ta.sma`). Conservative warmup bound: 60 daily bars (50-bar maximum seed plus the 10-bar momentum/correlation horizon).

## Execution assumptions

- Source execution semantics: `process_orders_on_close = true` — completed-bar decision, same-bar-close fill. Compatible with the pinned Hummingbot baseline lane; no conversion required.
- Research market (explicitly labeled house overlay, not source-native): `BTCUSDT` perpetual, `1d` decision timeframe. The source names no market and references no venue calendar, session, or contract-specific feed, so the program math is venue-neutral; contract identity is preserved by labeling the research market explicitly. Spot is not used because the rule takes naked short positions.
- Source sizing (`strategy.percent_of_equity`, 50) and the absent commission model are event-neutral: replaced downstream by the standard house execution overlay (Base 6% + Safety 6% + 6%, Isolated, 3×/5×, pinned Binance fees plus realized funding). The overlay changes no signal, event, or exit.
- First-signal behavior: flat until the first cross; thereafter always in the market (long or short) until the mirror cross. No pyramiding, no cooldown, no re-entry rule missing — repetition can only occur via a fresh opposite cross, which is fully specified.

## Evidence

### Source-reported

The source reports no performance numbers. No Sharpe, ROI, win rate, drawdown, trade list, or equity curve is cited in this record because none is printed in the pinned artifact; the TV landing layer likewise exposes only the script description and inputs, not a performance table.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No contradictory performance or failure report is cited in source. The absence of evidence is recorded as absence, not as support.

## Falsification plan

Research tests only — none of these substitutes for a missing rule (no rule is missing):

1. Parameter-stability: re-run with `rsiLen` frozen at 20 / 35 / 50 (killing adaptation) on the same BTCUSDT 1d history; if the adaptive version does not beat all frozen variants out-of-sample, the adaptation hypothesis is rejected.
2. Threshold-swap: symmetric 30/70 vs 20/80; a strategy whose sign depends on the exact round-number pair is curve-fit, not signal.
3. Timeframe portability: run the identical rule on 4h and 1h; the source is timeframe-agnostic, so collapse off-1d weakens the claim to a 1d artifact.
4. Correlation-channel check: decompose P&L into high-correlation vs low-correlation regimes; if gains do not concentrate where the adaptive channel claims edge (fast reaction in low-correlation tape), reject the mechanism story while keeping the rule as-is.
5. First-trade and always-in-market accounting: verify the backtest holds flat before the first cross and never nets to zero exposure afterwards; any deviation is an implementation bug, not a strategy property.

## Crypto portability

Venue-neutral program math (no sessions, no gaps logic, no dividends/splits, no exchange timezone call) ports cleanly to 24/7 crypto bars. Two port notes: (a) crypto trends can sustain longer unbroken runs than the equity tape the author trades, which exercises the `na`-guard quiet path more often — expected behavior, not a bug; (b) the rule is always in the market, so funding and fee drag on the perpetual research market must be modeled with pinned house assumptions, never zeroed silently.

## Limitations

1. No protective stop exists in source; tail risk on gap-like vertical moves is borne fully by the reversing entry. Recorded as explicitly disabled per source — must not be "repaired" with an invented stop.
2. Earlier scout funnels applied a blanket hard-kill to any `ta.crossover`/`ta.crossunder` usage. This record admits the crossover legs on contract terms instead: the admission contract requires crossover semantics to be *exact*, which these are (confirmed-bar series vs constant level, same-bar-close execution, zero look-ahead). The reasoning is stated here so the reviewer can audit it; no semantic conversion was performed.
3. Dynamic-length recursion: `rmaFun` carries `sum[1]` computed under past `rsiLen` values. This is exactly reproducible from the printed recursion and needs no invention, but port code must replicate the recursion verbatim rather than re-seeding a fixed-length Wilder RSI per bar.
4. The mirror truncates the author's description mid-sentence; nothing in this record depends on the missing clause.
5. Only program defaults are pinned. Input variants (different momentum length, RSI bounds, or threshold levels) are not separate strategies and must not be cherry-picked.
6. Confidence is `medium` (interpretation confidence): the rule text is complete and unambiguous, but the source offers no sample, no evidence, and no market declaration, so all mechanism and portability claims above remain hypotheses.

## Implementation status

- `not-implemented`. No Hummingbot/Qlib/n8n/Paper/Testnet/Live work has been performed or is authorized by this record.

## Adoption boundary

- `research-only`, `not-approved`. Admission of this record would mean only that its core signal and trade-event semantics are losslessly expressible under the pinned backtester with the labeled house overlay — not profitability, survival, or any trading approval.

## Related Wiki records

- None. No Wiki Brain write was performed for this cycle.

## Sources

- TradingView stable page (description/author corroboration): https://www.tradingview.com/script/08eSyDlq-DRM-Strategy/
- Immutable mirror file at pinned commit (rule text): https://github.com/hasnocool/tradingview-pine-scripts/blob/69969aeaf271b2f7b5a7632a1bde43069a0cbe26/DRM%20Strategy.pine
- Author identity as printed in source: QuantNomad. Original Pine version tag: `//@version=5`.
