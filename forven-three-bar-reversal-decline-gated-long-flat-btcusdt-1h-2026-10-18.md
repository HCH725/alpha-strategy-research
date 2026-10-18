---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven three-bar reversal decline-gated long-flat on BTCUSDT 1h bars
created: 2026-10-18
updated: 2026-10-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-16
sources:
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/three_bar_reversal.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven three-bar reversal decline-gated long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, `forven-adl-ema-cross`, `forven-atr-volume-breakout`, `forven-aroon-up-down-cross`, `forven-ema-rsi-pullback-reclaim`, `forven-double-bottom-neckline-break`, `forven-vwap-rolling-cross`, `forven-chaikin-mf-threshold-cross`, `forven-elder-ray-bull-power-cross`, `forven-adx-trend-pulse-reclaim`, `forven-dema-cross`, `forven-trix-signal-cross-zero-gate`, `forven-ultimate-oscillator-cross-gated`, and `forven-bollinger-s00120-rsi-breakout` records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/three_bar_reversal.py`.
- GitHub blob SHA at the pinned commit: `e5bf8885b7e40c362b1b6b83486fc35bda53b193`, size 3007 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 3007 bytes, 94 lines, SHA-256 `c9e64c5844f589ac976af3476c3c57bb10dcbdcc6dd5e17ff69d9b8c7db63fea`, identical to the GitHub blob (`git hash-object` reproduces `e5bf8885…da53b193`) — the entire file was retrieved and inspected.
- Registration: the file self-registers via `STRATEGY_CLASS = ThreeBarReversalStrategy`, `TYPE_NAME = "three_bar_reversal"` (line 13), and the `STRATEGIES = [("PREBUILT-THREE-BAR", ThreeBarReversalStrategy, {"_asset": "BTC"})]` roster pin (line 94).
- The file's own words (quoted for gate evidence, never extended): module docstring `Three-Bar Reversal strategy.` / `Detects three consecutive lower lows followed by a higher close on the third bar, signaling a potential reversal. The cumulative decline must exceed a configurable minimum percentage.`; `describe()` returns `Three-bar reversal pattern requiring at least a {min_decline_pct}% cumulative decline across three consecutive lower lows before a higher close.` with `md = self.params.get("min_decline_pct", 0.5)` (lines 37–42); `default_params` returns exactly `{ "leverage": 1.0 }` (lines 30–31); `compatible_regimes` returns `{"TREND_UP", "RANGE_BOUND"}` (lines 33–35); `parameter_space()` returns `{"min_decline_pct": (0.2, 2.0, 0.1)}` (lines 89–90, a documented search surface only — this record pins the 0.5 default and runs no search).
- Single decision path (verified line by line): `generate_signal()` (lines 44–87) is the sole signal method — no vectorized twin, no scalar delegate, no second decision logic exists to diverge. The `confidence` computation (lines 79–81) and the `indicators` dict (lines 82–86) are diagnostic echoes that never enter any predicate.
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults (lines 69–70), so the short-frame guard (`len(df) < min_bars` with `min_bars = 5`, lines 46–48) returning `Signal(price=...)` resolves to a flat no-trade bar by construction.
- Full-file token census (verified by search over the 94 lines this cycle): hardcoded `direction="long"` (exactly one site, line 78 — the sole order-direction token); 0 `direction="short"`; 0 `sell` / 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` (no order arguments, no risk legs); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 1.0` default); 0 `volume` / 0 `funding` / 0 `request` / 0 `security` / 0 `barstate` / 0 `timeframe` in any order-gating line; direct `df["…"]` reads are exactly `df["close"]` (three sites, lines 48/56/57) and `df["low"]` (four sites, lines 51–54) — no `high`, no `open`, no `volume` series read anywhere; 0 `ema` / 0 `ewm` / 0 `sma` / 0 `rolling` / 0 `crossover` / 0 `rsi` / 0 `atr` (no indicator of any kind — pure completed-bar low/close arithmetic); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` (no position-aware state conditions any signal).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the BTC roster asset, the three-consecutive-lower-lows construction, the higher-close confirmation, the 0.5% cumulative-decline gate, the new-lower-low exit, the long-only stance, the 5-bar short-frame guard, and the no-stop posture — but ships no venue spelling, no timeframe, no fill-timing flag, and no position-sizing rule. Researcher-declared adaptations are exactly three: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue spelling; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(close_1, 4)` — the decision bar's own close — and the admitted inside-bar, williams-ema-reclaim, linreg, zscore, adl, atr-volume, aroon, ema-rsi-pullback, double-bottom, vwap-cross, chaikin-mf, elder-ray, adx-trend-pulse, dema-cross, trix-signal-cross, ultimate-oscillator, and bollinger-s00120 records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) house sizing/capital/costs replacing the bare `leverage: 1.0` default (see Execution assumptions; sizing changes no event under the predeclared single-unit rule). The entry-implies-exit same-bar overlap is resolved by the predeclared position-state rule (see Signal) — the reviewer is never asked to invent an ordering. The 5-bar flat rule is the source's own guard, adopted verbatim — no researcher warmup pin is needed. No other pin is required: every strict-inequality boundary fires nothing on exact equality (see Signal). The decline-gate literal, the long-only stance, and the no-stop/no-target/no-time-exit posture are source-verbatim.

Pre-write dedup (2026-10-18): working-tree filename/content search for `three_bar_reversal` / `ThreeBarReversal` / `PREBUILT-THREE-BAR` / `three lower low` / `three-lower-low` returns zero strategy records — no record cites this source file. The pool's reversal-pattern cousins are fenced as different signal constructions in Negative evidence 8 (Fisher-transform 1-2-3 reversal two-sided 4h; single-bar engulfing; double-bottom neckline break; inside-bar continuation breakout; Alorse DMI three-bar DI-persistence plus EMA55 filter — a DMI-persistence construction, not a lower-lows price pattern). No closed `research/*` PR ever carried this source file (closed-state search shows only Forven TRIX/DEMA/ADX/Elder-Ray/Chaikin/VWAP/double-pattern/EMA-RSI/Aroon/ATR-volume/ADL/zscore/linreg/Williams/inside-bar/Bollinger-S00120 siblings, WorldQuant alphas, and Alorse records — no three-bar). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: three consecutive lower lows confirmed by a higher close with a cumulative-decline gate and a new-lower-low exit, long-flat on BTC, is a different signal construction from any oscillator cross, band breakout, or single-bar pattern — not a threshold re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: a pattern that `Detects three consecutive lower lows followed by a higher close on the third bar, signaling a potential reversal`, where `The cumulative decline must exceed a configurable minimum percentage`. No behavioural, structural, or risk-premium channel is claimed anywhere in the 94 lines. The file ships no performance number of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Exhaustion-slip reversal, long-only, state-holding. Three strictly descending lows establish a short-horizon washout; the higher close on the third bar prints the first rejection of lower prices; the 0.5% cumulative-decline gate refuses to pay for shallow drift that merely looks patterned. The exit is the pattern's own invalidation: any fresh lower low after entry ends the trade, so a reversal that fails to hold lows is cut on the first confirming bar rather than ridden. There is no stop leg and no profit leg: a reversal that grinds sideways without printing a new low is held indefinitely, while a V-bounce that never retests lows is ridden whole. Unlike oscillator-gated dips there is no momentum confirmation — weakness confirmed only by price structure, exited only by price structure.

## Signal

Exact rule as pinned (any other lookback, decline literal, confirmation leg, exit leg, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own; the single `generate_signal` path (lines 44–87) is the single source of truth:

```text
low_4           = low[t-3]                                                        // anchor bar
low_3, low_2, low_1 = low[t-2], low[t-1], low[t]                                 // sequence bars
close_2, close_1    = close[t-1], close[t]
three_lower_lows    = (low_3 < low_4) and (low_2 < low_3) and (low_1 < low_2)     // strict descent
higher_close        = close_1 > close_2                                         // rejection print
decline_pct         = ((low_4 - low_1) / low_4) * 100  (0.0 if low_4 <= 0)
sufficient_decline  = decline_pct >= 0.5
entry           = three_lower_lows and higher_close and sufficient_decline
exit_           = low_1 < low_2                                                 // fresh lower low
short_frame     = fewer than 5 completed bars → flat by source guard
```

- Trade events: `entry_signal=bool(entry)`, `exit_signal=bool(exit_)`, `direction="long"` (hardcoded literal — no short emission exists anywhere in the file, verified by full-file search). A flat book enters one full unit on an entry bar; a long book exits the full unit on an exit bar.
- Same-bar overlap, predeclared resolution (no reviewer invention): entry logically implies exit on the same bar, because `three_lower_lows` contains `low_1 < low_2`, which is exactly the exit predicate. The record resolves this by position-state rule, mirroring the stateless-source convention of the admitted Forven siblings: a flat book acts only on the entry leg (the co-fired exit is a deterministic no-op — there is nothing to exit); a long book acts only on the exit leg (repeat entry bars while long are no-ops). Entries while already long are no-ops under the predeclared single-unit rule (see position rule); exits while flat are deterministic no-ops. The entry is a strict-inequality edge so no level-refire pressure exists beyond genuinely new three-bar descents.
- Exact-equality boundaries fire nothing (strict comparisons throughout: `low_3 == low_4` breaks the descent, `close_1 == close_2` fails confirmation, `decline_pct == 0.5` minus epsilon fails the gate at exactly the literal only if below — `>=` admits exactly 0.5, pinned semantic), and pre-guard bars are flat by source rule.
- Direction: long-only. The short side is absent by construction (0 `direction="short"`, 0 `sell`) and recorded as explicitly disabled. Spot-compatible (no naked shorting required).
- Exits and risk (explicit): the fresh-lower-low predicate is the sole position-ending path. Opposite-signal exit is not applicable (no short leg exists). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence=np.clip(decline_pct / 1.5, 0, 1)` on every bar (lines 79–81) and the three `indicators` fields are diagnostic — none conditions any order line.
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further entry bars as no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops. Re-entry re-arms on any qualifying three-bar pattern after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and short-frame bars are flat by source rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `low` (descent, decline, exit) and `close` (confirmation, price echo); no `open`-series read, no `high`-series read, no bar `volume`, no indicator call of any kind, no funding/OI/mark-price read, no `request.*`, `security()`, `timeframe*`, `barstate.*`, session/calendar call, or stop/limit order argument anywhere in the order-gating path (verified by the census above returning zero matches). The `min_decline_pct` fallback literal `0.5` (line 45) equals the `describe()` literal and sits inside the documented `parameter_space` range — the pin is source-textual, not chosen. The `compatible_regimes == {"TREND_UP", "RANGE_BOUND"}` set is metadata never read by the signal path (which takes only `df`/`params`); treating the label as a gate would be a different, unpinned rule.

## Required data

- Completed `1h` bars of BTCUSDT: `low` for every structural comparison (descent chain, decline arithmetic, exit predicate); `close` for the confirmation comparison and the price echo. No `open`-series read, no `high`-series read, no bar `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request` / 0 `security` anywhere; 0 `timeframe` tokens in the whole file).
- Single decision timeframe `1h` (researcher pin, disclosed — the file names no timeframe). One evaluation per completed bar; all reads reference confirmed bars only (negative-index reads on the passed frame, no shift tricks, no rolling windows at all); fills land on the decision bar's own close (`price=round(close_1, 4)`, pinned derived rule).
- Warmup: the source ships its own length guard — `min_bars = 5`, and shorter frames return a price-only Signal whose entry/exit legs hold their `False` defaults (verified against the pinned `Signal` definition in `base.py`, lines 69–70). The 5-bar floor covers the 4-bar structural lookback with one bar of margin. The record adopts this guard verbatim as its flat rule — no researcher warmup pin is needed and none is pretended. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source roster pins `_asset BTC`; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills (`price=round(close_1, 4)` — the decision bar's own close), compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same lane primitive the seventeen admitted Forven-sibling records use. No maker-touch, queue, or intrabar-path-dependent fill: the only legs are bar-close-evaluated market entry/exit orders. Same-bar entry/exit overlap is sequenced by the predeclared position-state rule (flat acts on entry, long acts on exit), so no bar ever sequences two fills.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its `leverage: 1.0` default is replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with the single-unit/no-add/noop-on-repeat position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one long position at any time; re-entry after an exit needs only the next qualifying three-bar pattern (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The unused short permission requires no margin-short modeling.

## Evidence

### Source-reported

The file ships the full construction (94 lines: module docstring with the pattern sentences, `TYPE_NAME`, `default_params` at `leverage 1.0`, the `min_decline_pct` 0.5 fallback literal, the strict descent/confirmation/decline/exit predicates, the 5-bar guard, the hardcoded `direction="long"` and the `round(close_1, 4)` price echo, the `PREBUILT-THREE-BAR` roster pin). It ships zero adopted performance numbers of any kind — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` ship anywhere — the sole position-closing path is the fresh-lower-low predicate. The absence of any stop is coded absence, disclosed, not a tunable parameter here.
2. Entry-implies-exit overlap fenced: every entry bar co-fires the exit flag by construction (the descent's last inequality is the exit predicate). Under the predeclared position-state rule this is deterministic — flat books enter, long books exit, never both — but a same-bar-close engine that evaluates exits before entries on a flat book would stay flat where this record enters. The ordering is pinned here (entry leg governs the flat book), and any engine with the opposite sequencing would be a different, unpinned rule.
3. Hair-trigger exit fenced: while long, ANY lower low exits — including the very next bar if it merely ticks one tick lower while the reversal is otherwise intact. The exit has no confirmation, no decline gate, and no cooldown; whipsaw re-entry on the following three-bar pattern is the pinned cost, disclosed, not repaired.
4. Shallow-pattern blindness fenced: descents totalling less than 0.5% never enter even with a textbook three-lower-lows-plus-higher-close print — the gate admits only washouts the literal calls sufficient. A smaller literal would be a different, unpinned rule.
5. Sideways-hold fenced: a reversal that drifts sideways without printing a new low is held indefinitely — no time exit, no profit leg, no trailing guardrail exists to end it. Disclosed, not repaired.
6. Short-frame behaviour fenced: frames shorter than 5 bars resolve all-flat by the source's own guard (price-only Signal, both legs at their `False` defaults) — a coded behaviour, disclosed; no engine path ever passes an empty frame (backtests feed full history; the record floor starts at bar 1).
7. Source basis fenced: the source names no market beyond `_asset BTC` and no timeframe at all. The BTCUSDT-`1h` choice, same-bar-close fills, single-unit/no-add/noop pin, and house sizing/costs are researcher choices, disclosed; this record is therefore never evidence that any source-market deployment passes.
8. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-`1h` market choice, the same-bar-close fills, the position-state pin (including the flat-acts-on-entry ordering), and house sizing/costs — all predeclared above; the three-lower-lows construction, the higher-close confirmation, the `0.5` decline literal, the fresh-lower-low exit, the 5-bar guard, the long-only stance, and the no-stop/no-target/no-trailing/no-time-exit/no-cooldown posture are source-verbatim.
9. The `0.5` literal, the strict-descent chain (not level-hold, not touch), the higher-close confirmation (not close-above-anchor, not higher high), the fresh-lower-low exit (not opposite pattern, not fixed bars), the single-unit long-only stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning the literal, converting any strict inequality into a level hold, dropping the confirmation or the decline gate, adding a stop/target/filter/cooldown/gate, adding a short leg, or sizing partially instead of single-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: three-lower-lows / higher-close / `0.5` decline / fresh-lower-low exit / strict predicates / single-unit long-only / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Decline-gate relevance: replacing the pinned descent-plus-decline conjunction with the bare three-lower-lows-plus-higher-close pattern (same exit) must not improve net expectancy; fail ⇒ the 0.5% gate adds nothing over the bare pattern.
- F2 — Confirmation relevance: dropping only the higher-close leg (entry on descent-plus-decline alone) must not improve net expectancy; fail ⇒ the rejection print adds nothing over the washout shape.
- F3 — Exit-leg relevance: replacing the fresh-lower-low exit with a fixed-horizon exit must not improve net expectancy; fail ⇒ the structural invalidation carries no independent risk control over elapsed time.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision frame `1h` by researcher pin; roster-asset affinity kept — `_asset BTC`; low/close arithmetic with no venue-specific read). The OHLC arithmetic ports across perpetual venues without structural change. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behaviour needs no approximation. Division-by-zero is guarded in-source (`if low_4 > 0 else 0.0`). Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Researcher market: the source roster pins `_asset BTC` but no venue spelling — BTCUSDT is a researcher choice; signal timing on other markets would differ by construction.
- Researcher frame: the source names no timeframe — `1h` is a researcher choice; other frames would differ by construction.
- Derived fills: same-bar-close fills are a researcher derivation for this repository family, never the Forven engine's own timing claim — backtest economics under next-open fills would differ by construction.
- Derived ordering: the flat-acts-on-entry resolution of the entry-implies-exit overlap is a researcher pin — an engine evaluating exits first on a flat book would produce a different event set by construction.
- No price stop, no time stop: adverse excursion after entry has no guardrail beyond the fresh-lower-low predicate, which may arrive many bars later or after deep excursion; repeated pattern prints while long are no-ops, so averaging down is impossible by construction. This is the coded posture, disclosed as the record's principal risk.
- Hair-trigger exits (Negative evidence 3) and sideways holds (Negative evidence 5) are pinned costs of the rule, not recovered.
- Unused cost default: the source's bare `leverage: 1.0` carries no fee/funding concept; derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Position-state pin: same-side-add and flat-state exit behaviour is pinned by record rule, disclosed, not independently source-proven beyond the file's stateless per-bar signals.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; when this strategy is formally selected for execution, the `IMPLEMENTATION_NEEDED` route adds the minimal strategy-specific implementation and returns to the same pipeline without redoing HB_READY.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission. No live-trading authorization is granted or implied.

## Related Wiki records

None — no Wiki Brain record was written for this candidate (Scout contract: no Wiki writes).

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/three_bar_reversal.py (primary — pinned commit, full file read)
- https://github.com/judder659/Forven (repository identity)
