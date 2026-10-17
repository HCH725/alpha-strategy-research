---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven Ultimate Oscillator 7/14/28 oversold-recross long-flat on BTCUSDT 1h bars
created: 2026-10-17
updated: 2026-10-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-16
sources:
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/ultimate_oscillator.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven Ultimate Oscillator 7/14/28 oversold-recross long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, `forven-adl-ema-cross`, `forven-atr-volume-breakout`, `forven-aroon-up-down-cross`, `forven-ema-rsi-pullback-reclaim`, `forven-double-bottom-neckline-break`, `forven-vwap-rolling-cross`, `forven-chaikin-mf-threshold-cross`, `forven-elder-ray-bull-power-cross`, `forven-adx-trend-pulse-reclaim`, `forven-dema-cross`, and `forven-trix-signal-cross-zero-gate` records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/ultimate_oscillator.py`.
- GitHub blob SHA at the pinned commit: `86dc10b8288ae68463b9be5b98f9e5ea553035f6`, size 3910 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 3910 bytes, 133 lines, SHA-256 `67cf9516d61003c1630ce9b608fc4f6b87278f11d131d44c906ea54bda9cc2a0`, identical to the GitHub blob (`git hash-object` reproduces `86dc10b8…553035f6`) — the entire file was retrieved and inspected.
- Registration: the file self-registers via `STRATEGY_CLASS = UltimateOscillatorStrategy`, `TYPE_NAME = "ultimate_oscillator"` (line 13), and the `STRATEGIES = [("PREBUILT-ULT-OSC", UltimateOscillatorStrategy, {"_asset": "BTC"})]` roster pin (lines 131–133).
- The file's own words (quoted for gate evidence, never extended): module docstring `Ultimate Oscillator strategy.` / `UO = weighted average of buying pressure / true range across 3 periods.` / `Entry: UO crosses above oversold` / `Exit: UO crosses above overbought then drops` / `Compatible Regimes: RANGE_BOUND, TREND_UP`; class docstring `UO = 100 * (4 * avg7 + 2 * avg14 + avg28) / 7` / `where avg = sum(BP) / sum(TR) over each period.`; `describe()` returns `Enters when UO crosses above {oversold}; exits when UO crosses above {overbought} then drops.`; `default_params` returns exactly `{ "period1": 7, "period2": 14, "period3": 28, "oversold": 30, "overbought": 70, "leverage": 1.0 }` (lines 40–48); `compatible_regimes` returns `{"RANGE_BOUND", "TREND_UP"}` (lines 50–52); `parameter_space()` returns period/threshold ranges (lines 119–126, a documented search surface only — this record pins the defaults and runs no search).
- Full-file token census (verified by search over the 133 lines this cycle): hardcoded `direction="long"` (two sites: the live signal on line 111 and the short-frame guard on line 74 — the sole order-direction token); 0 `short` / 0 `sell` (no short path anywhere); 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` (no order arguments, no risk legs); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 1.0` default); 0 `volume` / 0 `funding` / 0 `request` / 0 `security` / 0 `barstate` in any order-gating line; direct `df["…"]` reads are exactly `df["close"]`, `df["high"]`, `df["low"]` (one site each, lines 64–66 — `high`/`low` enter only buying-pressure/true-range arithmetic, never a separate order leg); 0 `ema` / 0 `ewm` / 0 `rsi` / 0 `mfi` / 0 `wma` / 0 `hma` / 0 `vwap` (all three smoothers are exact-window `rolling().sum()` ratios — no exponential/recursive seeder exists anywhere); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` (no position-aware state conditions any signal); 0 `generate_signals` (the file ships only the scalar `generate_signal` path — no vectorized twin exists to diverge); 0 `crossover` / 0 `crossunder` / 0 `ta.cross` (both edges are direct strict-inequality comparisons, never an ambiguous cross builtin). The single `timeframe` token (line 17, class-docstring prose `multi-timeframe momentum strategy`) is descriptive prose only — zero multi-frame reads exist (0 `request` / 0 `security`), and the computation is single-frame rolling sums. `confidence` and the two `indicators` fields are diagnostic — zero order-gating comparisons read them.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the 7/14/28 triple-window buying-pressure construction, the 4/2/1 weights, the oversold-recross entry, the overbought-then-drop exit, the long-only stance, the no-stop posture, and its own `len(df) < max_period + 3` short-frame guard — but ships no venue, no timeframe, no fill-timing flag, and no position-sizing rule inside this file. Researcher-declared adaptations are exactly three: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted inside-bar, williams-ema-reclaim, linreg, zscore, adl, atr-volume, aroon, ema-rsi-pullback, double-bottom, vwap-cross, chaikin-mf, elder-ray, adx-trend-pulse, dema-cross, and trix-signal-cross records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) house sizing/capital/costs replacing the bare `leverage: 1.0` default (see Execution assumptions; sizing changes no event under the predeclared single-unit rule). No tie-break pin is needed: entry and exit are provably mutually exclusive on every bar (see Signal). The source's own short-frame guard is adopted verbatim as the warmup floor (see Required data), so no warmup invention is required either. The UO arithmetic, the threshold pair, the long-only stance, and the no-stop/no-target/no-time-exit posture are source-verbatim.

Pre-write dedup (2026-10-17): working-tree filename/content search for `builtin/ultimate_oscillator` / `PREBUILT-ULT-OSC` / `UltimateOscillatorStrategy` / `TYPE_NAME = "ultimate_oscillator"` returns zero strategy records — no record cites this source file. The sole pool cousin is fenced as a different signal construction in Negative evidence 8 (`ultimate-oscillator-oversold-breakout-long`, TV EdgeTools `z985j4Yo`, PR #101 merged: 6/14/20 SMA-smoothed UO, level-hold `UO < 30` entry refiring every oversold bar, `close > high[1]` prior-high-break exit, `1d`, next-bar-open fills — six axes differ here: 7/14/28 rolling-sum-ratio smoothing, cross-edge entry, overbought-exhaustion-drop exit, `1h`, same-bar-close fills, immutable GitHub file source). No closed `research/*` PR ever carried this source file (closed-state search for `ultimate` returns only merged PR #101). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: a 7/14/28 sum-ratio UO recrossed above 30 with an overbought-drop exit is a different signal construction from a 6/14/20 SMA-blend UO held under 30 with a prior-high-break exit — not a threshold re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: a `Ultimate Oscillator strategy` where `UO = weighted average of buying pressure / true range across 3 periods`, entry on `UO crosses above oversold`, exit on `UO crosses above overbought then drops`. No behavioural, structural, or risk-premium channel is claimed anywhere in the 133 lines. The file ships no performance number of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Triple-window buying-pressure timing with an exhaustion exit, long-only, state-holding. Each window's `sum(BP)/sum(TR)` ratio reads what fraction of recent true range was buying pressure; the 4/2/1 weighting lets the 7-bar window dominate while the 14- and 28-bar legs anchor it, so a one-bar spike cannot move the reading alone. The entry buys the exact bar the reading recrosses above 30 from below (oversold repair, not oversold holding — bars that stay under 30 never enter). The exit surrenders the unit on the exact bar the reading, having once reached 70+, turns down (overbought exhaustion, not a level recross — a reading that never reaches 70 is held indefinitely). There is no stop leg and no holding leg: a market that alternates recross-and-drop prints repeated full round-trips (whipsaw profile, disclosed), while a recross whose exhaustion never prints is held indefinitely. Unlike stop-based systems there is no fixed-distance risk leg — the exhaustion turn is the sole risk control by construction.

## Signal

Exact rule as pinned (any other period, weight, threshold, exit leg, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own; the triple-window stack is in-file (lines 79–90), no out-of-file indicator conditions any order:

```text
prev_close(t)   = close.shift(1)                                                     // causal, in-file
bp(t)           = close - min(low, prev_close)                                      // buying pressure, >= 0
tr(t)           = max(high, prev_close) - min(low, prev_close), 0 -> 1e-10          // true range, zero-guarded
avg1(t)         = sum(bp, 7) / sum(tr, 7)                                           // exact rolling windows
avg2(t)         = sum(bp, 14) / sum(tr, 14)
avg3(t)         = sum(bp, 28) / sum(tr, 28)
uo(t)           = 100 * (4*avg1 + 2*avg2 + avg3) / 7
entry           = (prev_uo <= 30) and (curr_uo > 30)                                // oversold recross edge
exit_           = (prev2_uo < 70) and (prev_uo >= 70) and (curr_uo < prev_uo)        // overbought-then-drop
min_bars        = period3 + 3 = 31 (source guard; shorter frames return both-signals-false)
```

- Trade events: `entry_signal=bool(entry)`, `exit_signal=bool(exit_)`, `direction="long"` (hardcoded literal — no short emission exists anywhere in the file, verified by full-file search). A flat book enters one full unit on an entry bar; a long book exits the full unit on an exit bar. Entries while already long are no-ops under the predeclared single-unit rule (see position rule); exits while flat are deterministic no-ops. The entry is a one-bar recross edge (strict current-bar inequality on the pair) so no level-refire pressure exists by construction — bars lingering above 30 never re-fire; the exit is a three-bar turn pattern and fires on any qualifying bar.
- Mutual-exclusion proof (no tie-break pin required): entry requires `prev_uo <= 30`; exit requires `prev_uo >= 70` — no single bar satisfies both, including every exact-equality boundary (strict current-bar comparisons fire nothing on ties: `curr_uo == 30` fails the entry's strict `>`, `prev2_uo == 70` fails the exit's strict `<`, `curr_uo == prev_uo` fails the exit's strict `<`) and short frames (the source guard returns both-signals-false before any average is read). The reviewer is never asked to invent an ordering.
- Direction: long-only. The short side is absent by construction (0 `short` / 0 `sell` in the file) and recorded as explicitly disabled. Spot-compatible (no naked shorting required).
- Exits and risk (explicit): the overbought-then-drop turn is the sole position-ending path. Opposite-signal exit is not applicable (no short leg exists). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence=min(1.0, (curr_uo - oversold)/15.0)` on entry bars only (lines 103–105) and the two `indicators` fields are diagnostic — none conditions any order line.
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further entry bars as no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops. Re-entry re-arms on any qualifying recross bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-guard bars are flat by record rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `close`/`high`/`low` with fixed non-positive offsets (trailing rolling sums, a one-bar shift, two prior-bar UO reads) — no `request.*`, `security()`, `timeframe*`, `barstate.*`, volume, funding/OI/mark-price read, session/calendar call, second oscillator, recursive smoother, or stop/limit order argument anywhere in the order-gating path (verified by the census above returning zero matches). The file ships only the scalar `generate_signal` path (no vectorized twin exists to diverge). The `compatible_regimes == {"RANGE_BOUND", "TREND_UP"}` set is metadata never read by the signal path (which takes only `df`/`params`); treating the label as a gate would be a different, unpinned rule. The `tr.replace(0, 1e-10)` zero-guard is source-verbatim; residual whole-window-flat division is fenced in Negative evidence 4.

## Required data

- Completed `1h` bars of BTCUSDT: `close`, `high`, `low` for every order-gating comparison (`close` for buying pressure, the price echo, and the shift; `high`/`low` inside buying-pressure/true-range arithmetic only). No `open`-series read, no bar `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request` / 0 `security` anywhere; the lone `timeframe` token is class-docstring prose, never a data call).
- Single decision timeframe `1h` (researcher pin, disclosed — the file names no timeframe). One evaluation per completed bar; all reads reference confirmed bars only (`close.shift(1)`, trailing rolling windows, `iloc[-1]`/`[-2]`/`[-3]` on the UO series); fills land on the decision bar's own close (`price=round(curr_close, 4)`, pinned derived rule).
- Warmup: the source guard holds every frame shorter than `period3 + 3 = 31` bars flat with both signals false (adopted verbatim as the record floor — covers the 28-bar rolling-sum seeding plus the two prior-bar UO references with margin). At 31+ bars the longest window and all three UO reads are defined; any residual leading `NaN` compares false under the strict inequalities, so no leg can fire — coded behaviour, disclosed. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market beyond the `_asset BTC` roster pin; naming normalization is the only market step, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills (`price=round(curr_close, 4)` — the decision bar's own close), compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same lane primitive the fifteen admitted Forven-sibling records use. No maker-touch, queue, or intrabar-path-dependent fill: the only legs are bar-close-evaluated market entry/exit orders. Mutual exclusion (proven above) means no bar ever sequences two fills.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its `leverage: 1.0` default is replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with the single-unit/no-add/noop-on-repeat position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one long position at any time; re-entry after an exit needs only the next qualifying recross bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The unused short permission requires no margin-short modeling.

## Evidence

### Source-reported

The file ships the full construction (133 lines: module/class docstrings with the entry/exit sentences, `TYPE_NAME`, `default_params` at `7` / `14` / `28` / `30` / `70` / `1.0`, the `len(df) < max_period + 3` guard, the `bp`/`tr` definitions with the `1e-10` zero-guard, the three rolling-sum ratios, the 4/2/1-weighted `uo` formula, the strict recross/turn predicates, the hardcoded `direction="long"`, the `round(curr_close, 4)` price echo, the `PREBUILT-ULT-OSC` roster pin). It ships zero adopted performance numbers of any kind — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` ship anywhere — the sole position-closing path is the overbought-then-drop turn. The absence of any stop is coded absence, disclosed, not a tunable parameter here.
2. Flat-until-recross, then fully exposed: before the first `UO` recross above 30 the system never trades; bars printing deep under 30 without recrossing never enter; once long, a reading that never reaches 70 holds the full unit indefinitely — no guardrail of any kind exists between entry and the exhaustion turn. This is the coded trade, disclosed, not a tunable parameter here.
3. Overbought-never-reached hold fenced: a recross whose UO tops out at, say, 65 and slides back to 40 without ever printing `>= 70` never exits — the three-bar turn requires the `prev_uo >= 70` print. Such mid-zone round-trips ride the full adverse excursion. Disclosed, not repaired.
4. Division legs fenced: `avg1/2/3 = sum(BP)/sum(TR)` divide by rolling true-range sums that reach zero only if an entire 7/14/28-bar window prints zero range — impossible on continuously traded BTCUSDT `1h` bars (every hourly bar in venue history spans a non-zero range); the source's `tr.replace(0, 1e-10)` guards single-bar zeros. No further guard ships in the source; the venue property is disclosed as the standing guard, and a flat-window deployment would be a different, unpinned rule.
5. Warmup blindness fenced: rolling-28 seeding suppresses every leg inside the first ~30 bars even if a textbook recross occurs — the adopted 31-bar flat guard (source-verbatim) converts this into a record rule rather than a silent miss; a shorter warmup would be a different, unpinned rule.
6. Source basis fenced: the source names no market beyond `_asset BTC` and no timeframe at all. The BTCUSDT-`1h` choice, same-bar-close fills, single-unit/no-add/noop pin, and house sizing/costs are researcher choices, disclosed; this record is therefore never evidence that any source-market deployment passes.
7. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-`1h` market choice, the same-bar-close fills, the position-state pin, and house sizing/costs — all predeclared above; the 7/14/28 periods, the 4/2/1 weights, the buying-pressure/true-range definitions, the rolling-sum ratios, the `30`/`70` literals, the strict predicates, the long-only stance, the 31-bar guard, and the no-stop/no-target/no-trailing/no-time-exit/no-cooldown posture are source-verbatim.
8. The `7` / `14` / `28` literals, the `4` / `2` / `1` weights, the rolling-sum-ratio smoothing (not SMA, not EMA), the strict recross entry (not level-hold, not touch), the three-bar overbought-drop exit (not prior-high-break, not level recross), the single-unit long-only stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning any period/weight/threshold, swapping a smoother, converting the edges into level holds, adding a stop/target/filter/cooldown/gate, adding a short leg, or sizing partially instead of single-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `7` / `14` / `28` / `4` / `2` / `1` / `30` / `70` / strict predicates / single-unit long-only / overbought-drop exit / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Threshold relevance: replacing the pinned `30` recross level with any adjacent oversold level must not improve net expectancy; fail ⇒ the pinned literal carries no advantage over neighboring levels and the record's threshold choice is arbitrary.
- F2 — Exit-leg relevance: replacing the overbought-then-drop exit with a fixed N-bar time exit must not improve net expectancy; fail ⇒ the exhaustion turn adds nothing over a clock exit.
- F3 — Triple-window relevance: replacing the pinned 4/2/1 triple-window blend with any single-window buying-pressure ratio at the same `30`-style recross must not improve net expectancy; fail ⇒ the multi-window blending adds nothing over a single lookback.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision frame `1h` by researcher pin; high/low/close arithmetic with no venue-specific read). The OHLC arithmetic ports across perpetual venues without structural change. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behaviour needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Researcher market: the source names no market beyond the roster `_asset BTC` — BTCUSDT is a researcher choice; signal timing on other markets would differ by construction.
- Researcher frame: the source names no timeframe — `1h` is a researcher choice; other frames would differ by construction.
- Derived fills: same-bar-close fills are a researcher derivation for this repository family, never the Forven engine's own timing claim — backtest economics under next-open fills would differ by construction.
- No price stop, no time stop: adverse excursion after entry has no guardrail beyond the exhaustion turn, which requires a `>= 70` print that may arrive many bars later, after deep excursion, or never; repeated recross prints while long are no-ops, so averaging down is impossible by construction. This is the coded posture, disclosed as the record's principal risk.
- Overbought-never-reached holds (Negative evidence 3) and warmup blindness (Negative evidence 5) are pinned costs of the rule, not recovered.
- Unused cost default: the source's bare `leverage: 1.0` carries no fee/funding concept; derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Position-state pin: same-side-add and flat-state exit behaviour is pinned by record rule, disclosed, not independently source-proven beyond the file's stateless per-bar signals.
- The word `timeframe` in the class docstring is prose, never a data dependency — a deployment reading a second frame would be a different, unpinned rule.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; when this strategy is formally selected for execution, the `IMPLEMENTATION_NEEDED` route adds the minimal strategy-specific implementation and returns to the same pipeline without redoing HB_READY.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission. No live-trading authorization is granted or implied.

## Related Wiki records

None — no Wiki Brain record was written for this candidate (Scout contract: no Wiki writes).

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/ultimate_oscillator.py (primary — pinned commit, full file read)
- https://github.com/judder659/Forven (repository identity)
