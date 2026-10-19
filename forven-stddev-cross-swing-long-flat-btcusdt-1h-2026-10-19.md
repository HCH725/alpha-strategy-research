---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven STDDEV z-score ±2.0 cross swing-hold long-flat on BTCUSDT 1h bars
created: 2026-10-19
updated: 2026-10-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-16
sources:
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/stddev_breakout.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven STDDEV z-score ±2.0 cross swing-hold long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, `forven-adl-ema-cross`, `forven-atr-volume-breakout`, `forven-aroon-up-down-cross`, `forven-ema-rsi-pullback-reclaim`, `forven-double-bottom-neckline-break`, `forven-vwap-cross`, `forven-chaikin-mf-threshold-cross`, `forven-elder-ray-bull-power-cross`, `forven-adx-trend-pulse-reclaim`, `forven-dema-cross`, `forven-trix-signal-cross`, `forven-ultimate-oscillator-cross-gated`, `forven-bollinger-s00120`, `forven-three-bar-reversal-decline-gated`, `forven-atr-breakout-channel`, `forven-pivot-s1-bounce-r1-exit`, `forven-volatility-contraction-breakout`, `forven-connors-rsi-oversold-recross`, `forven-kdj-dual-gate`, `forven-heikin-ashi-color-change`, `forven-bb-edge-fade-reclaim`, `forven-rsi-s00139-washout-cross`, `forven-obv-ema-cross-sma-gated`, `forven-mfi-threshold-cross`, `forven-williams-r-adx-gated`, `forven-rsi-boundary-rejection`, `forven-ema-cross-adx-regime`, `forven-vwap-pullback-distance`, and `forven-hma-cross` records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`, verified via the GitHub commits API this cycle; verified as the repository HEAD via `git ls-remote` against both `HEAD` and `refs/heads/main` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/stddev_breakout.py`.
- GitHub blob SHA at the pinned commit: `f7e382597549d860146c7ebeda48610e4d6b6cf`, size 3871 bytes.
- Byte-identity check: the file retrieved from `raw.githubusercontent.com` at the pinned commit is 3871 bytes, 130 lines, SHA-256 `3019b347af5c27933c344f8fcaad1b796be61def435c60e34c8a2144a1b0c5dd`, and `git hash-object` reproduces the GitHub blob (`f7e3825…d6b6cf`) — the entire file was retrieved twice and inspected (both fetches byte-identical).
- Registration: the file self-registers via `STRATEGY_CLASS = StdDevBreakoutStrategy` (line 126), `TYPE_NAME = "stddev_breakout"` (line 13), and the `STRATEGIES = [("PREBUILT-STDDEV", StdDevBreakoutStrategy, {"_asset": "BTC"})]` roster pin (lines 128–130). Repo-wide, no other builtin file carries this `TYPE_NAME` or roster name; working-tree search for `stddev_breakout` / `PREBUILT-STDDEV` / `StdDevBreakoutStrategy` returns zero strategy records citing this source file.
- The file's own words (quoted for gate evidence, never extended): module docstring `Standard Deviation / Z-Score Mean Reversion strategy.` with `Entry: Z-score drops below -threshold (oversold, mean-reversion buy)` / `Exit: Z-score rises above +threshold (overbought, take profit)` / `Compatible Regimes: RANGE_BOUND, MEAN_REVERSION` (lines 1–6); class docstring `Z-score mean reversion strategy.` with `Computes a rolling z-score: (close - SMA) / rolling_stddev.` / `Enters long when z-score falls below the negative threshold (oversold)` / `and exits when z-score rises above the positive threshold (overbought / mean achieved).` (lines 17–23); `describe()` returns `Z-score = (close - SMA(20)) / StdDev(20). Enters long when z < -2.0 (oversold). Exits when z > +2.0 (overbought / profit target).` (lines 52–58, with defaults); `default_params` returns exactly `{ "period": 20, "z_threshold": 2.0, "leverage": 1.0 }` (lines 41–46); `compatible_regimes` returns `{"RANGE_BOUND", "MEAN_REVERSION"}` (lines 48–50, metadata never read by the signal path); `parameter_space()` returns `{ "period": (10, 30, 5), "z_threshold": (1.5, 3.0, 0.5) }` (lines 119–123, a documented search surface only — this record pins the defaults and runs no search). No performance phrase of any kind ships anywhere in the 130 lines — this record adopts no source-reported performance (see Evidence).
- Single decision path, verified complete: `generate_signal()` (lines 60–117) is the sole signal method — no `generate_signals` vectorized twin exists anywhere in the 130 lines, so no twin-selection ambiguity exists. The method reads `close` only (line 64 — the complete set of `df[` reads in the file), applies its own short-frame guard (lines 66–74), builds the trailing SMA and sample-σ (lines 76–77, `ddof=1` explicit), maps zero-variance bars to `z = 0.0` (lines 79–83), evaluates the two edge-cross pairs on the last two z prints (lines 85–95), and returns a single `Signal` (lines 105–117).
- Zero out-of-file indicator dependencies: the file imports only `numpy`, `pandas`, and `forven.strategies.base` (lines 8–10). No `forven.strategies.indicators` facade import exists — no `atr`/`adx`/`rsi` diagnostic call conditions any order line (unlike the HMA/CCI siblings, there is nothing to fence here).
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` (12238 bytes, blob `27508a2a6b8c546e21adefdb97fc0144fabf881b`, identical to the blob pinned by the admitted `forven-rsi-s00139` and `forven-bb-edge-fade-reclaim` records) defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults (lines 69–70), `direction: str = "long"` default (line 72), plus `__post_init__` coercion (lines 78–80) and `_normalize_signal_direction` (line 160) mapping the `"long"` literal back to `"long"` — the file's guard literal (line 71) and live `direction = "long"` assignment (line 97, echoed at line 109) therefore survive untouched on every bar.
- Full-file token census (verified by search over the 130 lines this cycle): `direction=` occurs exactly twice (guard line 71 literal `"long"` and live line 109 echo of the line-97 `"long"` assignment; no short leg exists); 0 `sell` / 0 `stop` / 0 `limit` / 0 `qty` / 0 `trail` (no order arguments, no live risk legs of any kind); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 1.0` default, replaced by the house overlay — see Execution assumptions); 0 `funding` / 0 `mark_price` / 0 `request` / 0 `security` / 0 `barstate` / 0 `timeframe` in any line, and 0 `open`-series reads plus 0 `high` / 0 `low` / 0 `volume` reads anywhere (the sole `df[` read is `close` — line 64); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` / 0 `cooldown` (no position-aware state conditions any signal); 0 `short` (case-insensitive — no short path exists); the only two prose matches for profit language are docstring words (`take profit` line 4, `profit target` line 57 — no live leg); `len(df)` occurs exactly once (the line-66 guard — the file's own warmup floor, adopted verbatim, never invented).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the 20-bar close SMA / sample-σ z-score construction, the oversold-cross entry at −2.0, the overbought-cross exit at +2.0, the long-only stance, the no-stop posture, and its own `period + 2` short-frame guard — but ships no venue spelling, no timeframe, no fill-timing flag, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue spelling; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the thirty-plus admitted Forven records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) single-unit position pin with hold-no-op semantics with the source's own 22-bar guard adopted verbatim as the warmup floor (an already-positioned book treats same-direction cross-under bars as hold-no-ops, a flat book treats cross-over bars as no-ops, re-entry re-arms on any qualifying cross-under after any exit with no cooldown, pre-guard bars flat by the source's own rule — see Signal); (4) house sizing/capital/costs replacing the bare `leverage: 1.0` default (see Execution assumptions; sizing changes no event under the predeclared single-unit rule). No tie-break pin is needed: entry and exit are provably mutually exclusive on every bar (see Signal).

Pre-write dedup (2026-10-19): working-tree filename/content search for `builtin/stddev_breakout` / `PREBUILT-STDDEV` / `StdDevBreakoutStrategy` / `TYPE_NAME = "stddev_breakout"` returns zero strategy records — no record cites this source file. Roster-name search for `PREBUILT-STDDEV` returns this record only. The pool's z-score cousins are fenced as different constructions in Negative evidence 6 (level-hold mean-reclaim at exit 0.0 vs edge-cross full-swing hold at exit +2.0 here; RSRS-beta cross-timing vs close z-score here). No open or closed `research/*` PR ever carried this source file (closed-PR title search for `stddev` returns only the unrelated Inertia-RVI #215; the open `research/*` PRs are only #48/#49/#63/#89/#92/#251/#304 — different mechanisms, indicators, and sources). Not a duplicate, paraphrase, or trivial parameter variant: an oversold-cross to overbought-cross full-swing edge-hold (entry fires once on the cross-under bar, exit fires once on the cross-over bar, positions span the entire traverse) is a different signal construction from an oversold-level hold with a mean-reclaim exit (entry true on every sub-threshold bar, exit at 0.0) — not a threshold re-tuning. The admitted level record's own `parameter_space()` caps its exit threshold at ±0.5, so a +2.0 cross exit lies outside even that file's documented search surface.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: a `Standard Deviation / Z-Score Mean Reversion strategy` whose `Z-score drops below -threshold (oversold, mean-reversion buy)` for entry and whose `Z-score rises above +threshold (overbought, take profit)` for exit. No behavioural, structural, or risk-premium channel is claimed anywhere in the 130 lines. The file ships no backtest numbers of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Oversold-to-overbought swing capture, long-only, state-holding. The system buys the exact bar the trailing z-score crosses under −2.0 and then holds through the entire mean traverse, surrendering the unit only on the exact bar the z-score crosses over +2.0 — so every round trip spans the full statistical swing rather than banking the mean. Unlike level-hold mean-reversion (entry true on every oversold bar, exit at the mean), the edge-cross posture fires each leg exactly once per traverse: a z-score that parks under −2.0 for ten bars prints one entry, not ten, and a position survives the whole climb back through zero with no profit-taking leg. Unlike stop-based systems there is no fixed-distance risk leg — the overbought cross is the sole risk control by construction, which means a z-score that mean-reverts without ever reaching +2.0 is held indefinitely (disclosed disposition risk). The zero-variance guard maps dead bars to `z = 0.0`, which fires neither leg — flat-market determinism is preserved, not patched.

## Signal

Exact rule as pinned (any other period, threshold, average family, denominator, entry/exit leg, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own; `generate_signal` (lines 60–117) is the single source of truth — no second decision logic exists:

```text
inputs (defaults, frozen): period = 20, z_threshold = 2.0
sma[t]    = mean(close[t-19 .. t])                       // trailing 20-bar SMA, line 76
std[t]    = sample-stdev(close[t-19 .. t], ddof=1)       // trailing 20-bar sample σ, line 77
z[t]      = (std[t] > 0) ? (close[t] - sma[t]) / std[t] : 0.0   // lines 80-83
entry     = (z[t-1] >= -2.0) AND (z[t] < -2.0)           // cross under −threshold, line 92
exit_     = (z[t-1] <= +2.0) AND (z[t] > +2.0)           // cross over +threshold, line 95
```

- Guard (source-verbatim): `len(df) < period + 2` (line 66 — fewer than 22 bars) returns the explicit no-signal guard (lines 67–74); pre-guard bars are flat by the source's own rule, adopted verbatim as the warmup floor (see Required data).
- Trade events: `entry_signal=bool(entry)`, `exit_signal=bool(exit_)`, `direction="long"` (hardcoded literal on both return paths — no short emission exists anywhere in the file, verified by full-file search). A flat book enters one full unit on an entry bar; a long book exits the full unit on an exit bar. Entries while already long are no-ops under the predeclared single-unit rule (see position rule); exits while flat are deterministic no-ops. Both legs are one-bar edges (fire once on the cross bar — refires require a fresh traverse back across the threshold), not levels; treating either leg as a level-hold would be a different, unpinned rule.
- Mutual-exclusion proof (no tie-break pin required): entry requires `z[t] < -2.0` while exit requires `z[t] > +2.0` on the same print — unsatisfiable on every bar, including NaN/zero-variance bars (mapped to `0.0`, which satisfies neither conjunct) and exact-equality boundaries (strict `<` / `>` fire nothing on ties; the `>=` / `<=` history legs admit equality only on the prior bar). The reviewer is never asked to invent an ordering.
- Exits and risk (explicit): the overbought-cross pair is the sole position-ending path. Opposite-signal exit is not applicable (no short leg exists). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence = min(1.0, (|z| − 2.0) / 2.0 + 0.5)` on firing bars (else `0.0`, lines 99–103) and the `indicators={zscore, prev_zscore, sma, stddev}` dict (lines 111–116) are diagnostic — none conditions any order line.
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further entry bars as no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops. Re-entry re-arms on any qualifying cross-under bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only `close` with one trailing 20-bar window, closed-form SMA / sample-σ arithmetic, and one guarded division — no `request.*`, `security()`, `timeframe*`, `barstate.*`, volume-weighted logic, session/calendar call, high/low/open read, or stop/limit order argument anywhere in the file (verified by the census above returning zero matches). The `compatible_regimes == {"RANGE_BOUND", "MEAN_REVERSION"}` set is metadata never read by the signal path (which takes only `df`/`params`), so no regime model gates any order. The rolling std is the pandas sample estimator (`ddof=1`, explicit in code — line 77); substituting a population denominator would be a different, unpinned rule.
- Warmup: 30 completed `1h` bars flat by record rule — structural minimum is the 22nd completed bar (20-bar rolling seed plus the `period + 2` length guard; the cross pair additionally needs the two most recent z prints, both defined from the 22nd bar onward when variance is positive; zero-variance bars map to `0.0` and fire nothing). Pre-warmup bars are flat by record rule; missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (every window reads completed bars only), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Required data

- `close` on `BTCUSDT` `1h` completed bars only (sole `df[` read — line 64). No `open`/`high`/`low`/`volume`, no external feed, no calendar, no multi-asset input.
- Warmup: 30 completed `1h` bars flat by record rule (structural minimum the 22nd completed bar — 20-bar rolling seed plus the source's own `period + 2` guard — plus margin; the two-print cross needs no deeper history).
- Point-in-time: every window is trailing over completed bars; the decision bar's own close is both the last input and (via the derived same-bar-close pin) the fill price — no future bar, no unfinished-bar read, no repainting.

## Execution assumptions

- Derived lane (all four pins predeclared in Provenance): `BTCUSDT` `1h`, completed-bar decisions with same-bar-close market fills (`price=round(curr_close, 4)` — the decision bar's own close), single-unit position with hold-no-op semantics, house sizing/capital/costs replacing the bare `leverage: 1.0` default.
- Pinned-engine path (same lane primitive as the thirty-plus admitted Forven siblings on this exact repository family): the pinned Hummingbot package `20260920` / `dev-2.17.0` backtest model prices one market order at the decision bar's own close on `BTCUSDT` `1h` with declared house fees/funding/slippage overlay; close-only arithmetic, single-asset book, and same-bar-close fills are the already-verified subset for this family — no new execution primitive, no multi-asset synchronization, no shared-capital contention, no lower-timeframe alignment, no non-OHLCV input, no next-open/maker/intrabar fill is required by this record.
- No stop/limit/trailing/time leg is modelled because none exists in source — explicitly disabled, never defaulted. Missing trade prices are never fabricated (pre-warmup and missing bars stay flat).

## Evidence

### Source-reported

The source ships the full construction (frozen `period 20 / z_threshold 2.0` inputs, trailing close SMA with sample-σ z-score, oversold-cross entry, overbought-cross exit, fixed long-only stance with the literal `"long"` direction token, no risk legs) and the `PREBUILT-STDDEV` BTC roster pin. It ships no performance number of any kind — this record claims no source-reported performance, and no backtest figure is invented here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No twin-signal ambiguity: full-file search returns exactly one `def generate_signal` and zero `generate_signals` — there is no second decision path to select between.
2. No out-of-file indicator risk: the file's imports are `numpy`/`pandas`/`base` only — no facade-resolved `atr`/`adx`/`rsi` call exists to pin or fence.
3. Zero-variance determinism: a 20-bar window of identical closes yields `std = 0`, mapped to `z = 0.0` (lines 80–83) — both cross conjuncts fail, so flat markets emit neither leg; no division-by-zero, no NaN propagation into any order line.
4. Equality boundaries fire nothing: the live legs use strict `<` / `>` on the current print; a z-score landing exactly on ±2.0 holds the prior state by construction.
5. Same-bar double-fire is impossible (mutual-exclusion proof in Signal) — no ordering assumption, invented or otherwise, is required.
6. Pool-cousin fence (z-score records), stated plainly: `forven-zscore-mean-reversion-long-flat-btcusdt-1h-2026-10-17.md` trades a close-price z-score LEVEL hold (entry true on every bar with `z < -2.0`, exit on the `z > 0.0` mean-reclaim level) from immutable file `builtin/zscore_reversion.py` — a different input file, different `TYPE_NAME`, different roster name, level-vs-edge trigger semantics, and a mean-reclaim exit whose own documented search surface caps at ±0.5. `qrs-penalized-rsrs-zscore-timing-long-flat-btcusdt-1d-2026-10-16.md` times RSRS-beta z-scores, not close z-scores. This record crosses under −2.0 once per traverse and holds the full swing to the +2.0 cross-over, long-flat, on BTCUSDT `1h`, from immutable file `builtin/stddev_breakout.py` — different trigger × different exit × different hold semantics × different source file. This record is therefore never evidence for those rules, and those records are never this rule's provenance.
7. Variant menus fenced, stated plainly: the `parameter_space()` surface (`period` 10–30, `z_threshold` 1.5–3.0) is a documented search grid the code never runs — this record freezes the `20/2.0` defaults as written; adopting any grid point would be a different, unpinned rule.
8. Regime/metadata quarantine, stated plainly: `confidence`, `zscore`, `prev_zscore`, `sma`, `stddev`, and the `compatible_regimes == {"RANGE_BOUND", "MEAN_REVERSION"}` set are returned inside diagnostic fields or class metadata and read by zero order-gating comparisons — treating any of them as a gate, filter, or sizing input would be a different, unpinned rule.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `20/2.0` z-score / oversold-cross entry / overbought-cross exit / long-only / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Exit-leg relevance: replacing the +2.0 cross-over exit with the 0.0 mean-reclaim level must not improve net expectancy on the frozen 42-cell campaign; fail ⇒ the full-swing hold is dead weight wearing a risk-leg label.
- F2 — Edge-vs-level: replacing the one-bar cross triggers with level-hold triggers must not improve net expectancy; fail ⇒ the edge posture adds nothing over the level rule.
- F3 — Traverse scarcity: fewer than 5 completed round trips across the full available `1h` history ⇒ the ±2.0 band is too wide for this market/frame (observation, never a retune permit).

## Crypto portability

Direct: `BTCUSDT` perpetual/spot `1h` closes on Binance — the rule consumes closes only, needs no venue-specific microstructure, no funding input, and no spot-vs-perp distinction in its arithmetic. House costs (fees/funding/slippage) are overlaid downstream per the research campaign; modeled funding is never reported as realized funding.

## Limitations

- Indefinite-hold disposition: a position whose z-score mean-reverts without ever printing above +2.0 is held forever — the overbought cross is the sole exit and there is no time stop; prolonged grinds just under the exit band accumulate opportunity cost, disclosed.
- No risk leg: no stop loss, take profit, trailing stop, or time limit exists in source — recorded as explicitly disabled; adverse traverses beyond −2.0 have no capital guardrail besides the eventual exit cross.
- Whipsaw at the band: a z-score oscillating across −2.0 prints repeated entry-then-no-exit accumulation under the single-unit rule (refires absorbed as no-ops while positioned, but each fresh traverse after an exit opens again) — disclosed chop profile.
- Single-market scope: derived pin is `BTCUSDT` `1h` only; portability to other symbols/timeframes is untested and claimed nowhere in this record.
- Research overlay dependence: fills, sizing, and costs follow the derived lane pins and the downstream house model — not the source engine's own semantics.

## Implementation status

`not-implemented` — no dedicated Qlib/Hummingbot executable artifact exists for this record. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream refusal; if formally selected for execution without a reproducible recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline stage), never a second admission flag.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write is performed by the Scout lane.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/stddev_breakout.py (primary source — executable Python strategy, 130 lines, fetched live 2026-10-19 at pinned HEAD commit, 3,871 bytes, SHA-256 `3019b347…0c5dd`, blob `f7e3825…d6b6cf`; no performance figure ships anywhere in the file)
- https://github.com/judder659/Forven (repository context; pinned HEAD `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` verified this cycle)
- `forven/strategies/base.py` at the same commit (supporting semantics — `Signal` defaults and direction normalization, 12,238 bytes, blob `27508a2a…fabf881`, identical to the blob pinned by admitted sibling records)
