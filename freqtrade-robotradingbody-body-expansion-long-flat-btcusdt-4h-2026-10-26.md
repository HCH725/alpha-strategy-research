---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade RobotradingBody candle-body expansion long-flat on BTCUSDT 4h bars
created: 2026-10-26
updated: 2026-10-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-11-05
sources:
  - https://github.com/davidzr/freqtrade-strategies/blob/9623c1f3d8c7f60c8b411010fa26377e6ca99ab9/strategies/RobotradingBody/RobotradingBody.py
  - https://github.com/davidzr/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade RobotradingBody candle-body expansion long-flat on BTCUSDT 4h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/davidzr/freqtrade-strategies (public third-party Freqtrade strategy collection, GPL-3.0; no record in the pool pins any file from this repository — verified zero `davidzr` hits this cycle).
- Pinned commit SHA: `9623c1f3d8c7f60c8b411010fa26377e6ca99ab9` (author David Zabala, `2023-11-05T15:22:08Z`, message `initial commit`; the repository commits API returned exactly one commit this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `strategies/RobotradingBody/RobotradingBody.py`.
- GitHub blob SHA at the pinned commit: `e914e320e0563f91c4a2ea6f472401f68352d253`, 2722 bytes, SHA-256 `57f764a2dd256a0160cf2a744d3a41e83dacc5bb5f979f1f2d33ae9b77c8b028`.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit reproduces the blob SHA via `git hash-object` — the entire file was retrieved and inspected line by line.
- Registration: the file defines class `RobotradingBody(IStrategy)` (the only class in the file), `INTERFACE_VERSION = 2`.
- The file's own words (quoted for gate evidence, never extended): `timeframe = '4h'`; `startup_candle_count: int = 100`; `minimal_roi = { "0": 0.9 }`; `stoploss = -0.99`; `for_mult = IntParameter(1, 20, default=3, space='buy', optimize=True)`; `for_sma_length = IntParameter(20, 200, default=100, space='buy', optimize=True)`; `trailing_stop = False`; `use_sell_signal = True`; `sell_profit_only = False`; `ignore_roi_if_buy_signal = False`; `process_only_new_candles = False`; `order_types = { 'buy': 'limit', 'sell': 'limit', 'stoploss': 'market', 'stoploss_on_exchange': False }`; `order_time_in_force = { 'buy': 'gtc', 'sell': 'gtc' }`; indicators `dataframe['body'] = (dataframe['close'] - dataframe['open']).abs()` and `dataframe['body_sma'] = (ta.SMA(dataframe['body'], timeperiod=int(self.for_sma_length.value))) * int(self.for_mult.value)`; entry `(dataframe['open'] > dataframe['close']) & (dataframe['body'] > dataframe['body_sma']) & (dataframe['volume'] > 0)`; exit `(dataframe['close'] > dataframe['open']) & (dataframe['volume'] > 0)`; `informative_pairs` returns `[]`.
- In-file lineage comment (lineage only, not an independent source read): `https://www.tradingview.com/script/zUaR3Vbb-robotrading-body/`, `translated for freqtrade: viksal1982`, `A timeframe of 4 hours to 1 day`. The TradingView page itself was not fetched; no TV-side claim is carried into any gate.
- Framework calls pinned: `ta.SMA` is the TA-Lib abstract simple moving average with `timeperiod=100`, trailing window, first valid output on the 100th input bar; `IntParameter(...).value` resolves to its `default` absent hyperopt (this record pins the default-parameter version `for_mult=3`, `for_sma_length=100` — any tuned value is a different, unpinned rule). `qtpylib` is imported and used zero times.
- Full-file token census (verified over the downloaded bytes this cycle): 0 `short`; 2 live `IntParameter` (plus their import names); 1 `informative` (the stub returning `[]` — single-frame by construction); 2 `volume` (exactly the two `volume > 0` guards); 1 `ta.SMA`; 0 `shift` / 0 `crossed_*` / 0 `resample` / 0 `merge_informative_pair` / 0 `heikinashi` / 0 `request` / 0 `security`; 1 `minimal_roi`; 3 `stoploss` (literal, order-type key, comment-free); 1 `trailing`; `numpy as np` / `pandas as pd` imported and never called (display leftovers — fenced, not repaired).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source backtest. Researcher-declared adaptations are exactly six, all predeclared here: (1) market pin `BTCUSDT` Binance spot, unleveraged (the source is pair-agnostic — no symbol, no venue, no `trading_mode` anywhere in the file); (2) same-bar-close MARKET fills on completed-bar decisions (the source trades `limit` GTC entries/exits filled on later candles; this record freezes completed-bar evaluation with same-bar-close execution and scopes live/limit-order-book behaviour out — the same derivation the admitted freqtrade HLHB record carries for its own `limit`-GTC source); (3) a 100-bar warmup floor that restates the source `startup_candle_count = 100` verbatim (see Required data); (4) house sizing/costs replacing the absent source economics (fixed 0.001 BTC, modeled 0.001 per-side cost, 10,000 USDT book — the same overlay shape as the admitted connorgeary150 record); (5) bar-close evaluation of the stop and ROI legs with the explicit precedence below (the source evaluates risk intrabar in live trading; intrabar sequencing is scoped out, never invented); (6) completed-bar-only evaluation despite the source `process_only_new_candles = False` (scoped to the research model, disclosed). The `4h` frame, the `body`/`body_sma` construction, the `3` multiplier, the `100` length, all three entry conjuncts, both exit conjuncts, the ROI/stop/trailing literals, all behaviour flags, and the long-only posture are source-native and unmodified.

**Pre-write dedup (2026-10-26, working tree at `102b7a1`, 354 strategy records):** content search for `robotrading`, `body_sma`, `davidzr`, `viksal` returns zero records; filename search for `robotrading` returns zero; all 10 open `research/*` PR titles/bodies checked (Heracles KCD, ClucMay72018, AdxSmas, Forven CCI, Swift 2YMA, SSL channel, Chandelier Exit, SuperTrend flip, Gaussian StochRSI, Larry Williams streak) — none trades a candle-body statistic. Nearest pool cousins are fenced as different constructions in Negative evidence 7. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The file claims no behavioural, structural, or risk-premium channel anywhere in its bytes — it ships only the construction: buy the red candle whose absolute body exceeds three times its own 100-bar mean while the tape prints volume, and stand aside to flat on the first green candle. No sample, window, trade count, or cost basis ships with it, and no performance statistic is printed.

### Research interpretation

Oversized-red-candle mean-reversion entry with first-green exit, long-only. Unlike bare red-candle records (buy every down bar), the body must clear a self-scaling bar — a small-bodied drift-red buys nothing, so the entry selects expansion bars relative to their own recent regime, not fixed-point thresholds. Unlike breakout records (buy strength), it buys the exhaustion-shaped bar itself and surrenders on the first green print — the coded consequence is a holder of post-expansion snap-back attempts that never averages down, never waits out a second red day, and never shorts the continuation. The +90% ROI rung and −99% stop are file-literal but economically inert under this exit (see Signal): the green-candle exit dominates every realistic tape.

## Signal

Exact rule as pinned (any other lookback, multiplier, price input, threshold, edge/level choice, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own; `SMA(body,100)` is the pinned TA-Lib abstract trailing mean:

```text
body[t]     = abs(close[t]-open[t])
body_sma[t] = 3 * SMA(body, 100)[t]                                   // for_mult=3, for_sma_length=100 defaults pinned
entry = (open[t] > close[t]) AND (body[t] > body_sma[t]) AND (volume[t] > 0)   // buy = 1
exit_sig = (close[t] > open[t]) AND (volume[t] > 0)                            // sell = 1
risk = minimal_roi {"0": 0.9}; stoploss -0.99; trailing_stop False
guard = 100 completed 4h candles held flat; the first decision is the index-100 close
```

- Trade events: `buy=1` on bars printing the three-conjunct entry, `direction` long-only; `sell=1` on bars printing the two-conjunct exit. Both are LEVEL conditions on the decision bar (no edge, no latch, no hold — a qualifying bar whose volume leg fails never re-fires).
- Exact boundaries (pinned semantics): strict `>` throughout — a doji (`open == close`) fires neither leg; `body` exactly equal to `body_sma` and `volume` exactly `0` both fail their strict legs. The `100` length, the `3` multiplier, and the `0.9`/`-0.99` risk literals are never tuned here.
- Mutual-exclusion proof (no tie-break pin required): entry needs `open[t] > close[t]` while exit needs `close[t] > open[t]` on the same bar — the two regions are strictly disjoint, so entry and signal-exit never co-print even if the volume leg holds, and any engine collide rule is a backstop that never activates. The reviewer is never asked to invent an ordering.
- Direction: long-only. The file contains zero `short` tokens of any kind — no `enter_short`/`exit_short`/`can_short`; a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the green-candle signal exit (`use_sell_signal = True`, `sell_profit_only = False` — exits fire even at a loss), the `{"0": 0.9}` ROI rung, and the `-0.99` fixed stop are the complete position-closing set; `trailing_stop = False` and `ignore_roi_if_buy_signal = False` apply verbatim (ROI never skipped on entry bars). No breakeven move, no time exit — explicitly none, not invented. Under the first-green exit, the ROI rung (+90% while holding through red bars) and the stop (−99% single-book drawdown) are reachable only in pathological gaps; they are kept verbatim and bar-close-evaluated, never re-tuned into effective risk.
- Position rule (predeclared researcher pin): single-unit 0.001 BTC, at most one open position; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging — no stacking control of any kind ships in the file); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying three-conjunct bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Bar-close precedence (predeclared derivation, disclosed): on a positioned book each completed bar evaluates closing legs in fixed order — (1) fixed stop, (2) ROI rung, (3) signal exit; entry is evaluated only on a flat book. At most one net position change per bar by construction plus the mutual-exclusion proof.
- Determinism note for the reviewer: the rule reads only completed-bar OHLCV (`open`/`close` for `body`, the trailing 100-body window for `body_sma`, `volume` for the guard) with fixed non-negative offsets — no funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt-tuned value, or stop/limit order argument anywhere in the gating path. `plot_config` does not exist in this file.

## Required data

- Completed `4h` bars of BTCUSDT: `open`/`close` (the `body` transform and its 100-bar mean), `volume` (the `volume > 0` guard — source-native, no repair needed; on 24/7 crypto tape this leg is almost always true and is kept verbatim, never optimized away). `high`/`low` are read by no gating line. No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (`informative_pairs` returns `[]`).
- Single decision timeframe `4h` (source-native — the file prints `timeframe = '4h'`). One evaluation per completed bar; every window reads the decision bar and its causal past only; fills land on the decision bar's own close under the derived rule below.
- Warmup (source-verbatim floor, disclosed): 100 completed 4h candles held flat; the first decision is the index-100 close. Covers the source `startup_candle_count = 100` exactly (TA-Lib `SMA(body,100)` additionally seeds NaN on indices 0–98, where every strict comparison is false — no leg can fire early). No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance spot, unleveraged (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed; the file's own lineage is a TradingView-script port, and no session, calendar, or venue concept ships in the gating path, so the 24/7 crypto port changes no rule).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close MARKET fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted freqtrade HLHB record uses for its own `limit`-GTC source. No maker-touch, queue, or intrabar-path-dependent fill: entry, signal exit, stop, and ROI legs are all bar-close-evaluated under the fixed precedence above; the Signal mutual-exclusion proof leaves no ambiguous same-bar fill order to the engine.
- Engine path (exact, disclosed): exact-`4h` PASS records already sit on `main` (the admitted Eterna Donchian/Keltner/Chandelier/TSI `4h` cohort — frontmatter `hb_ready_status: PASS` spot-confirmed this cycle); this record rides the same specified single-frame completed-bar `4h` Binance candle path, not an assumed one. `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` at the pinned commit maps `"4h"` (directly fetched this cycle). Position accounting rides the pinned `BacktestPositionHold` average-cost/fee ledger with MARKET first-row-close `OrderExecutor` fills, per the bounded primitives verified for the admitted connorgeary150 record at `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (PRs #414/#417/#475 are prior bounded engine evidence, not rehashed this cycle); the provider's dangerous `Decimal("1")` missing-price default is rejected — any nonfinite or absent actual close suspends decisions. Pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding; this unleveraged spot derivative has no funding contract at all.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its risk literals are preserved verbatim while sizing and costs ride the explicit overlay (10,000 USDT book, fixed 0.001 BTC, modeled `trade_cost=0.001` per filled side, i.e. 0.1% of actual filled quote notional — a research assumption, not a verified Binance fee; no additional modeled slippage/spread/latency, which is not measured zero slippage), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one 0.001 BTC position at any time; the entry opens the full unit on a flat book; the signal exit, the ROI rung, or the fixed stop closes it in full; re-entry after an exit needs only the next qualifying entry bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (the `body`/`body_sma` indicator block, the three-conjunct entry, the two-conjunct exit, the `timeframe`/`startup_candle_count`/`minimal_roi`/`stoploss`/flag literals, and the `RobotradingBody(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: TA-Lib seeds print NaN until windowed (indices 0–98, every strict comparison false — no early entry, no early exit). The 100-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired.
2. Exact-touch rule fenced: strict `>` fires nothing on equality — dojis print neither `buy` nor `sell`; `body` exactly `body_sma` and `volume` exactly `0` both fail — disclosed, not smoothed.
3. Co-print arithmetic fenced (proven, not asserted): entry and signal-exit need strictly opposite open/close relations on the same bar — mutually exclusive by construction, and the predeclared fixed precedence binds regardless. Stop/ROI legs start at zero distance on the entry bar — the fixed precedence resolves them without intrabar claims, disclosed, not repaired.
4. Near-inert risk fenced: under the first-green exit the +90% ROI rung and −99% stop are reachable only in pathological gaps — kept verbatim and bar-close-evaluated under the fixed precedence, never re-tuned, never presented as effective protection. An adverse red-run can be arbitrarily large until the first green print; disclosed, not repaired with an invented stop.
5. Hyperopt-space plumbing fenced: the two `IntParameter` spaces (`for_mult` 1–20, `for_sma_length` 20–200) exist but this record pins the file defaults (3, 100) as the declared version — any tuned value is a different, unpinned rule. Zero `Categorical`/`Decimal`/`Boolean` spaces, zero fitted values anywhere — disclosed, never repaired into a signal.
6. Dead-import plumbing fenced: `qtpylib`, `numpy as np`, `pandas as pd` are imported and never called — plumbing leftovers with no gate effect. Zero `Parameter` values flow anywhere except the two pinned defaults.
7. Cousin records fenced as different constructions (none conjoins a red-candle body-vs-own-mean expansion test with a first-green exit on `4h`): the admitted `forven-engulfing-body-cover-volume` sibling trades two-candle engulfing cover geometry (no size normalization, `1h`); the admitted `dual-ema-engulfing-volume` sibling needs an engulf plus dual-EMA alignment; the admitted `qstick` sibling trades a *signed* `SMA(close-open,14)` zero-cross level-hold, two-sided (not an absolute-body ratio, not red-entry/green-exit); the admitted `vidya-cmo` sibling trades VIDYA slope with a CMO gate (no body statistic); the admitted `freqtrade-cofibit` sibling trades STOCHF/EMA-rail/ADX conjunctions (no body statistic). Dropping the expansion leg, the red-candle requirement, or the green-candle exit would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: every other file in the `davidzr/freqtrade-strategies` repository (a single-commit tree — no sibling strategy file shares this pin) is a separate pin — no constant may be substituted into this record.
9. Derivation boundary fenced: the non-source-native behaviours in this record are exactly the six predeclared pins (BTCUSDT spot market choice, same-bar-close MARKET fills, 100-bar warmup floor restating the source count, house sizing/costs, bar-close risk evaluation with fixed precedence, completed-bar evaluation despite `process_only_new_candles = False`) — all predeclared above. The `4h` frame, the `body`/`body_sma` construction, the `3` multiplier, the `100` length, the three-conjunct entry, the two-conjunct exit, the ROI/stop/trailing literals, the behaviour flags, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: three-conjunct entry / `body` construction / 100 length / 3 multiplier / two-conjunct exit / ROI-stop literals / single-unit long-only / `4h` BTCUSDT spot / same-bar-close fills with fixed precedence are frozen.

- F1 — Expansion-leg relevance: dropping the `body > body_sma` leg (any red candle with volume enters, same exit/risk) must not improve net expectancy; fail ⇒ the self-scaling size test adds nothing over a bare red-candle entry.
- F2 — Multiplier relevance: relaxing the multiplier to `1` (body above its own mean, same entry/exit/risk) must not improve net expectancy; fail ⇒ the 3× expansion selectivity adds nothing over a mean-reversion reading.
- F3 — Exit-leg relevance: holding through the first green candle until the second consecutive green print (same entry/risk) must not improve net expectancy; fail ⇒ the first-green exit timing adds nothing over a slower confirmation.

## Crypto portability

BTCUSDT Binance spot `4h` is the research pin (source names no market; its in-file lineage is a TradingView-script port, and no session, calendar, or venue-hours concept is read anywhere — every window is a trailing bar count, portable across 24/7 crypto tape). Long-only with full-unit open/close expresses unchanged on a perpetual venue only under a separately declared derivative (funding, margin, and liquidation semantics would need their own engine-path verification). The `volume > 0` guard reads native Binance 4h volume — no exotic feed. No funding contract exists for this unleveraged spot derivative; do not infer zero perpetual funding.

## Limitations

- TA-Lib abstract internals (SMA seeding and rolling semantics) and the pinned `IntParameter` default-resolution live in their libraries outside the pinned strategy file — pinned by call with the contemporaneous definitions quoted above, not re-derived; exact reproduction inherits those modules' seeding alongside the file-local arithmetic, under the disclosed 100-bar floor.
- No breakeven, no time exit, no trailing, no short leg, no cooldown — all explicitly absent, never to be added by repair.
- Bar-close evaluation of stop/ROI plus same-bar-close MARKET fills are the disclosed derivations (5) and (2) above: live limit-order-book behaviour, queue priority, and intrabar sequencing are scoped out, and this record makes no claim about the source's own limit-GTC backtest fills.
- `confidence: medium` reflects interpretation confidence in the file transcription, not expected profitability; the near-inert risk stack means adverse red-runs are uncapped until the first green print.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/davidzr/freqtrade-strategies/blob/9623c1f3d8c7f60c8b411010fa26377e6ca99ab9/strategies/RobotradingBody/RobotradingBody.py
- https://github.com/davidzr/freqtrade-strategies
