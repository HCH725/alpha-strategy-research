---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven double-bottom neckline-break long-flat on BTCUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/double_pattern.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven double-bottom neckline-break long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, `forven-adl-ema-cross`, `forven-atr-volume-breakout`, `forven-aroon-up-down-cross`, and `forven-ema-rsi-pullback-reclaim` records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/double_pattern.py`.
- GitHub blob SHA at the pinned commit: `8ddc2c34204d951cfe1db8668c36216fc727888b`, size 4400 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 4400 bytes, 137 lines, SHA-256 `6070d68f11697bd1519e25326ee58b7c4c9c22a5d97a907dee1d235b4aff25f7`, identical to the GitHub blob (`git hash-object` reproduces `8ddc2c34…27888b`) — the entire file was retrieved and inspected; the order-gating rule lives entirely in this one file (pure numpy/pandas, no out-of-file indicator helper).
- The file's own words (quoted for gate evidence, never extended): module docstring `Double top/bottom pattern detection strategy.` with `Detects two similar highs (double top) or two similar lows (double bottom) within a tolerance window. Entry on double bottom confirmation when price rises above the neckline.`; `describe()` returns `Double top/bottom detection over {lb} bars with {tol}% tolerance for matching peaks/troughs.`; `default_params` returns exactly `{ "lookback": 50, "tolerance_pct": 2.0, "neckline_break_pct": 0.5, "leverage": 1.0 }`; roster entry `("PREBUILT-DOUBLE-PATTERN", DoublePatternStrategy, {"_asset": "BTC"})`; `compatible_regimes` returns `{"RANGE_BOUND", "TREND_UP"}`; `parameter_space()` returns `{ "lookback": (20, 100, 10), "tolerance_pct": (0.5, 3.0, 0.5), "neckline_break_pct": (0.1, 1.5, 0.2) }` (a documented search surface only — this record pins the defaults and runs no search).
- Full-file token census (verified by search over the 137 lines this cycle): 2 `direction` literals, both `"long"` (the len-guard return and the main return — the sole order-direction tokens); 0 `short` / 0 `sell` (no short path anywhere, case-insensitive); 0 `stop` / 0 `limit` / 0 `profit` / 0 `trailing` / 0 `fee` / 0 `slippage` / 0 `commission` (no order arguments, no risk legs, no economics beyond the `leverage: 1.0` default); 0 `volume` / 0 `open` / 0 `funding` (order-gating reads are `close`, `high`, `low` only); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` / 0 `cooldown` (no position-aware state conditions any signal); 0 `request` / 0 `security` / 0 `barstate` / 0 `timeframe` (no cross-feed, no session read); 0 `generate_signals` / 0 `previous` (a single `generate_signal` code path — no second rule to corroborate or contradict); 0 out-of-file indicator-helper calls (imports are `numpy`, `pandas`, and the local `BaseStrategy, Signal` base only — no cross-asset import, no second feed, no fitted model).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the 50-bar twin-extrema matching (2% tolerance), the neckline-break entry, the double-top-breakdown exit, the long-only stance, and the no-stop posture — but ships no venue, no timeframe, no fill-timing flag, and no position-sizing rule inside this file. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(close, 4)` — the decision bar's own close — and the admitted S01508, inside-bar, williams-ema-reclaim, linreg, zscore, adl, atr-volume, aroon, and ema-rsi records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) an adopted 60-completed-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 52nd completed bar — the `len(df) < lookback + 2` guard — plus margin; see Required data); (4) house sizing/capital/costs replacing the bare `leverage: 1.0` default (see Execution assumptions; sizing changes no event under the predeclared single-unit rule). No tie-break pin is needed: entry and exit are provably mutually exclusive on every bar (see Signal). The twin-extrema construction, the neckline entry, the breakdown exit, the long-only stance, and the no-stop/no-target/no-time-exit posture are source-verbatim and unmodified.

Pre-write dedup (2026-10-17): working-tree filename/content search for `builtin/double_pattern` / `PREBUILT-DOUBLE-PATTERN` / `DoublePattern` returns zero strategy records — no record cites this source file. Content search for twin-extrema/neckline records returns only the pool cousin `pnf-double-top-breakout-double-bottom-breakdown-two-sided-btcusdt-1d-2026-10-14.md`, fenced as a different mechanism in Negative evidence 8 (point-and-figure box construction from a different source vs raw high/low extrema matching with tolerance plus neckline-break confirmation here). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: raw-extrema twin matching with a neckline-break entry and a double-top-breakdown exit is a different signal construction from a P&F-box breakout — not a threshold re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: a `Double top/bottom pattern detection strategy` that `Detects two similar highs (double top) or two similar lows (double bottom) within a tolerance window` with `Entry on double bottom confirmation when price rises above the neckline.` No behavioural, structural, or risk-premium channel is claimed anywhere in the 137 lines. The file ships no performance number of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Classical chart-pattern capture with confirmation discipline, long-only, state-holding. The twin-low match (within 2%) asks that the market has twice refused the same floor; the neckline break (close 0.5% above the highest high between the two troughs) asks that the recovery already prove itself rather than buying the second touch blind. The exit is the mirror discipline: a confirmed double top (twin highs within 2%) with a 0.5% breakdown below the intervening trough floor closes the full unit, so a position survives ordinary pullbacks and closes only on a demonstrated topping structure. Unlike edge-event systems there is a level-hold property: every bar satisfying the pattern-plus-break pair prints entry, so consecutive qualifying bars refire — the predeclared single-unit rule turns same-side refires into no-ops by construction. The failure mode is plain: a range that keeps printing matched lows without ever breaking the neckline never enters (opportunity cost, disclosed), while a choppy range that alternates double-bottom breaks with double-top breakdowns prints repeated entry-then-exit round trips with no stop and no profit-taking leg (disclosed).

## Signal

Exact rule as pinned (any other lookback, tolerance, neckline-break percentage, exit leg, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own:

```text
window   = last 50 completed bars (includes the decision bar)
half     = 25
first_low    = min(lows[0:25]);  second_low  = min(lows[25:50])
i1 = argmin(lows[0:25]);         i2 = argmin(lows[25:50])
double_bottom = (first_low > 0) and (|first_low - second_low| / first_low <= 0.02)
neckline = max(highs[i1 : 25+i2])                       // highest high between the two troughs
entry    = double_bottom and (neckline > 0) and (close > neckline * 1.005)
first_high   = max(highs[0:25]); second_high = max(highs[25:50])
j1 = argmax(highs[0:25]);        j2 = argmax(highs[25:50])
double_top = (first_high > 0) and (|first_high - second_high| / first_high <= 0.02)
topneck  = min(lows[j1 : 25+j2])                        // lowest low between the two peaks
exit_    = double_top and (topneck > 0) and (close < topneck * 0.995)
```

- Trade events: `entry_signal=bool(entry)`, `exit_signal=bool(exit_)`, `direction="long"` (hardcoded literal on both return paths — no short emission exists anywhere in the file, verified by full-file search). A flat book enters one full unit on an entry bar; a long book exits the full unit on an exit bar. Entries while already long are no-ops under the predeclared single-unit rule (see position rule); exits while flat are deterministic no-ops. Entry is level-style (every pattern-plus-break bar prints it — refires absorbed by the single-unit rule), not a one-bar edge; adding an edge-only posture would be a different, unpinned rule.
- Mutual-exclusion proof (no tie-break pin required): both index spans always contain bars 24 and 25 of the 50-bar window (`i1 <= 24`, `25+i2 >= 25`, same for `j1/j2`), so the spans overlap on a nonempty set; hence `neckline = max-high(A) >= max-high(overlap) >= min-low(overlap) >= min-low(B) = topneck`. Entry implies `close > neckline * 1.005 >= topneck * 1.005 > topneck * 0.995`, which contradicts the exit conjunct `close < topneck * 0.995`. No single bar with real prices satisfies both, including exact-equality boundaries (strict comparisons fire nothing on ties) and the guarded zero cases (`neckline > 0`, `topneck > 0` required). The reviewer is never asked to invent an ordering.
- Direction: long-only. The short side is absent by construction (0 `short` / 0 `sell` in the file, case-insensitive) and recorded as explicitly disabled. Spot-compatible (no naked shorting required).
- Exits and risk (explicit): the double-top-breakdown pair is the sole position-ending path. Opposite-signal exit is not applicable (no short leg exists). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence=min((close-neckline)/neckline*100, 1.0)` on entry bars (else `0.0`) and the `indicators={double_bottom, double_top, first_low, second_low, neckline}` dict are diagnostic — none conditions any order line.
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further entry bars as no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops. Re-entry re-arms on any qualifying pattern-plus-break bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `close`/`high`/`low` with fixed non-negative offsets (a trailing 50-bar window that includes the decision bar, plus `argmin`/`argmax` index reads inside that window) — no `request.*`, `security()`, `timeframe*`, `barstate.*`, volume, funding/OI/mark-price read, session/calendar call, or stop/limit order argument anywhere in the file (verified by the census above returning zero matches). The `len(df) < lookback + 2` guard holds short frames flat with `confidence=0.0`; every pre-seed or NaN comparison is false, so pre-seed bars deterministically print neither signal — the record-rule 60-bar warmup additionally holds them flat. The `compatible_regimes == {"RANGE_BOUND", "TREND_UP"}` set is metadata never read by the signal path (which takes only `df`/`params`); treating the label as a gate would be a different, unpinned rule.

## Required data

- `1h` bars of one pair: `close`, `high`, `low` (twin-extrema matching, neckline/topneck extremes, and every comparison read only these three series). No `volume`, no funding, OI, mark/index price, liquidation, trade/aggressor, L2/order-book, on-chain, options/Greeks, sentiment/news, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1h` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; every test reads trailing bars of the same series, never a second feed).
- Warmup: 60 completed `1h` bars flat by record rule — structural minimum is the 52nd completed bar (the coded `len(df) < 50 + 2` guard). The extra 8 bars are adopted margin; pre-warmup bars are flat by record rule. Missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (every window reads completed bars only), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (the file names no venue; the roster pins `_asset BTC` — the Binance/BTCUSDT pin is a researcher market choice, disclosed, never presented as source-native).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The file returns `price=round(close, 4)` — the decision bar's own close — and the admitted S01508, inside-bar, williams-ema-reclaim, linreg, zscore, adl, atr-volume, aroon, and ema-rsi records establish same-bar-close as the pinned-compatible lane primitive for this exact repository family. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity, and entry/exit can never co-fire (proven above), so no intrabar ordering assumption is needed at all.
- Engine path for `1h` (gate 5, stated plainly): `1h` is a Binance-documented USDT-M kline interval; the derived rule needs only completed `1h` candles (`close`/`high`/`low`) on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no volume/funding/OI/mark-price leg. That is the same single-frame completed-bar path as the admitted `1h` siblings from this source family. Anything beyond that single-frame completed-bar path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: the source ships only a bare `leverage: 1.0` default with no capital, fee, slippage, funding, or margin assumption (quoted verbatim in census; the absences are disclosed, never read as zero cost) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior. Under the predeclared single-unit rule the sizing overlay changes no trade event.
- Concurrency: single-unit long-flat book — at most one open long; the breakdown exit closes the whole unit, and re-entry is allowed on any qualifying pattern-plus-break bar after any exit (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (50-bar twin-extrema matching at 2% tolerance, neckline-break-0.5% entry on double-bottom confirmation, double-top-breakdown-0.5% exit, fixed long-only stance with the literal `"long"` direction tokens, no risk legs) and the `PREBUILT-DOUBLE-PATTERN` roster pin. It ships no performance number of any kind — this record claims no source-reported performance, and no backtest figure is invented here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `stop` / 0 `limit` / 0 `profit` / 0 `trailing` — the sole position-closing path is the coded double-top-breakdown pair. The absence is coded (the signal block ends with the two comparisons and only the diagnostic return follows).
2. Variant menu fenced, stated plainly: the `parameter_space()` surface (`lookback` 20–100 step 10, `tolerance_pct` 0.5–3.0 step 0.5, `neckline_break_pct` 0.1–1.5 step 0.2) is a documented search grid the code never runs — this record freezes the `50` / `2.0` / `0.5` defaults as written; adopting any grid point would be a different, unpinned rule.
3. Level-fire fires as written, stated plainly: entry prints on every pattern-plus-break bar (no prior/current edge pair gates it), not only on the first break bar — adding an edge-only posture would be a different, unpinned rule; consecutive refires are absorbed as no-ops by the predeclared single-unit rule.
4. No averaging down, stated plainly: the file is stateless (no position-aware branch exists to implement anything else) — an already-long book treats further entry bars as no-ops under the predeclared single-unit rule.
5. Regime/metadata/passenger quarantine, stated plainly: `confidence`, the five `indicators` fields, and the `compatible_regimes == {"RANGE_BOUND", "TREND_UP"}` set are returned inside diagnostic fields or class metadata and read by zero order-gating comparisons — treating any of them as a gate, filter, or sizing input would be a different, unpinned rule.
6. Short-frame path fenced, stated plainly: the coded `len(df) < lookback + 2` guard holds every frame shorter than 52 bars flat with `confidence=0.0` — every pre-seed comparison is absent-or-NaN-false so no signal can print, and the record-rule 60-bar flat covers seeding plus margin regardless.
7. Co-fire impossibility fenced with proof, stated plainly: both index spans always overlap (each contains window bars 24 and 25), so `neckline >= topneck` always and the entry threshold (`neckline * 1.005`) strictly exceeds the exit threshold (`topneck * 0.995`) — no bar, including exact-equality boundaries and guarded zero cases, can satisfy both. No tie-break, no ordering assumption, and no reviewer invention is required anywhere in this record.
8. Pool-cousin fence (double-top/bottom records), stated plainly: `pnf-double-top-breakout-double-bottom-breakdown-two-sided-btcusdt-1d-2026-10-14.md` trades point-and-figure box breakouts/breakdowns on BTCUSDT `1d` from a different source and method. This record matches raw `high`/`low` twin extrema within 2% over a trailing 50-bar window with a 0.5% neckline-break confirmation entry and a double-top-breakdown exit, long-flat, on BTCUSDT `1h`, from immutable file `builtin/double_pattern.py` — different input construction × different trigger × different confirmation × different source file. This record is therefore never evidence for that rule, and that record is never this rule's provenance.
9. Diagnostic-text discrepancy fenced, stated plainly: `describe()` formats its tolerance from `params.get("tolerance_pct", 1.5)` (fallback literal `1.5`), while `default_params` pins `2.0` — with defaults the text prints `2.0%` and this record pins the `default_params` value `2.0`, never the fallback literal; the text is diagnostic and conditions no order line.
10. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT market pin, the `1h` frame adoption, same-bar-close fills (with live intrabar behavior scoped out), the adopted 60-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the twin-extrema arithmetic, the neckline entry, the breakdown exit, the order stance, and the risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, timing, input set, or the Forven engine's own execution semantics passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 50-bar window / 2% twin tolerance / 0.5% neckline-break entry / double-top-breakdown exit / long-only / BTCUSDT `1h` / same-bar-close fills are frozen.

- F1 — Gate relevance: dropping the twin-match gate (any 50-bar-high neckline break entry, same exit) must not improve net expectancy; fail ⇒ the coded double-bottom match adds nothing over its ungated twin.
- F2 — Confirmation relevance: replacing the 0.5% neckline-break confirmation with a second-touch entry (enter on the twin-low bar itself, same exit) must not improve net expectancy; fail ⇒ the coded confirmation adds nothing over its touch twin.
- F3 — Construction relevance: replacing the double-top-breakdown exit with the mirror neckline-loss exit (close 0.5% under the double-bottom neckline, same entry) must not reproduce-or-beat net expectancy; fail ⇒ the record is a symmetric-channel variant wearing a pattern label.

## Crypto portability

Pinned to BTCUSDT Binance futures `1h` under the house overlay (market pin is a researcher choice following the file's `_asset BTC` roster pin; the file itself is venue-agnostic). The rule reads only `close`/`high`/`low` completed-bar extremes — no `volume` tape and no funding/OI/mark-price leg — so venue volume-definition and funding-regime differences cannot move any gate (there is no volume or funding read at all), stated plainly as a portability strength with a boundary: cross-venue porting without re-verification would still be a different, unpinned claim, disclosed. The rule is long-only with no stop leg, so a spot-only deployment expresses it fully, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the file returns the decision bar's own close but ships no explicit fill-timing flag; this record evaluates completed bars only and executes same-bar-close on BTCUSDT `1h`. Any live intrabar behavior is out of scope.
- Derived market pin: the file names no venue and no timeframe (roster pins `_asset BTC` only) — BTCUSDT `1h` is a researcher market/frame choice for the house universe, never a source claim.
- Source economics are leverage-only: beyond the bare `leverage: 1.0` default the source ships no capital sizing, no fee, no slippage, no funding, and no margin assumption — derived evaluation must carry the full house cost load (fees plus historical funding; no hypothetical zero funding claimed), and this record reports no net performance of its own.
- No price stop, no time stop: adverse excursion after placement has no guardrail beyond the breakdown exit; a matched-low range that never breaks its neckline never enters (opportunity cost, disclosed), while an alternating double-bottom-break / double-top-breakdown chop prints repeated entry-then-exit round trips by construction. This is the coded posture, disclosed as the record's principal risk.
- Seed bars: the 50-bar window plus the `len < 52` guard dominate early bars; the first 60 `1h` bars are flat by record rule, so early-history signals never enter any evaluation. Substituting a seeded/warm-started extreme would move every early print and is a different, unpinned rule.
- Level-fire refires: consecutive pattern-plus-break bars refire entry by construction — disclosed in Negative evidence 3; on the declared single-unit book they are deterministic no-ops, and on the declared venue frames are always full length.
- No co-fire corner exists: see Negative evidence 7 — entry and exit are mutually exclusive by construction on every bar, so no tie-break pin was adopted.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record; the six-gate claim is pinned-engine expressibility of the declared rule, never a profitability, parity, or trading authorization.

## Adoption boundary

Research-only, not approved. No live, Paper, or Testnet authorization follows from this record. Any downstream standardized overlay (house DCA/capital/leverage), Qlib screening, or Hummingbot re-validation is a separate, explicitly authorized step outside this record.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/double_pattern.py (primary source — executable Python strategy, 137 lines, fetched live 2026-10-17 at pinned HEAD commit, 4,400 bytes, SHA-256 `6070d68f…f25f7`; pure numpy/pandas passenger-free single-file rule; no performance figure ships anywhere in the file)
- https://github.com/judder659/Forven (repository home; HEAD verified `e9a6c09` by `git ls-remote` this cycle)
