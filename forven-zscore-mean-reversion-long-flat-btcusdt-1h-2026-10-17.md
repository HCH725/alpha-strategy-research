---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven z-score mean reversion long-flat on BTCUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/zscore_reversion.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven z-score mean reversion long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, and `forven-linreg-channel-breakout` records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/zscore_reversion.py`.
- GitHub blob SHA at the pinned commit: `3a423ff2df09e37c99120e20cd3e597013f21298`, size 3300 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 3300 bytes, 116 lines, SHA-256 `202ebbce5a5dbbb6c026b2bd146907f72c5be48d3b491ab32d60b836495dcea7` — the entire file was retrieved and inspected; the order-gating rule lives entirely in this one file (close-only rolling z-score level).
- The file's own words (quoted for gate evidence, never extended): module docstring `Z-score mean reversion strategy.` / `Computes z = (close - rolling_mean) / rolling_std. Enters long when z drops below -entry_z (oversold). Exits when z crosses back above exit_z (mean).`; class docstring `Z-score mean reversion strategy.`; `describe()` returns `Z-score mean reversion: {period}-period z-score, enter when z < -{entry_t}, exit when z > {exit_t}.` (with defaults `20-period z-score, enter when z < -2.0, exit when z > 0.0`); `default_params` returns exactly `{ "period": 20, "entry_threshold": 2.0, "exit_threshold": 0.0, "leverage": 1.0 }`; roster entry `("PREBUILT-ZSCORE", ZScoreReversionStrategy, {"_asset": "BTC"})`; `compatible_regimes` returns `{"RANGE_BOUND"}`; `parameter_space()` returns `{ "period": (10, 50, 5), "entry_threshold": (1.5, 3.0, 0.5), "exit_threshold": (-0.5, 0.5, 0.5) }` (a documented search surface only — this record pins the defaults and runs no search).
- Full-file token census (verified by search over the 116 lines this cycle): 3 `direction` literals, all `"long"` (the two no-signal guards plus the signal return — the sole order-direction token); 0 `short` / 0 `sell` (no short path anywhere); 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` (no order arguments, no risk legs); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 1.0` default); 0 `volume` / 0 `open` / 0 `high` / 0 `low` / 0 `time` / 0 `request` / 0 `security` / 0 `timeframe` / 0 `barstate` (only `close` is read by any order-gating line — three `df["close"]` reads, zero reads of any other column); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` (no position-aware state conditions any signal). Imports are only `pandas` plus the local `BaseStrategy, Signal` base — no indicator facade, no external feed, no cross-asset import.
- Close-only fence (quoted line identities): line 56 `curr_close = float(df["close"].iloc[-1])`, line 67 `rolling_mean = df["close"].rolling(period).mean()`, line 68 `rolling_std = df["close"].rolling(period).std()` — the complete set of `df[` reads in the file. No `open`/`high`/`low`/`volume` token appears on any order-gating line.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the 20-bar close rolling-mean / sample-σ z-score construction, the `z < -2.0` oversold level entry, the `z > 0.0` mean-reclaim exit, the long-only stance, and the no-stop posture — but ships no venue, no timeframe, no fill-timing flag, and no position-sizing rule inside this file. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue; the roster pins `_asset BTC` and the admitted sibling Forven records all execute Binance `BTC/USDT-1h` — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted S01508, inside-bar, williams-ema-reclaim, and linreg records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) an adopted 30-completed-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 22nd completed bar — 20-bar rolling seed plus the `period + 2` length guard — plus margin; see Required data); (4) house sizing/capital/costs replacing the bare `leverage: 1.0` default (see Execution assumptions; sizing changes no event under the predeclared single-unit rule). The z-score arithmetic, the level entry, the level exit, the long-only stance, the entry/exit mutual exclusivity, and the no-stop/no-target/no-time-exit posture are source-verbatim and unmodified.

Pre-write dedup (2026-10-17): working-tree filename/content search for `builtin/zscore_reversion` / `PREBUILT-ZSCORE` / `Z-Score Reversion` returns zero strategy records — no record cites this source file. Content search for close-price z-score level records returns only the pool cousin `qrs-penalized-rsrs-zscore-timing-long-flat-btcusdt-1d-2026-10-16.md`, fenced as a different mechanism in Negative evidence 7 (RSRS-beta z-score vs close z-score here). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: a close-price level mean-reversion hold is a different signal construction from an RSRS-slope cross-timing system, not a threshold re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its four sentences print: a `Z-score mean reversion strategy` that `Computes z = (close - rolling_mean) / rolling_std`, `Enters long when z drops below -entry_z (oversold)`, and `Exits when z crosses back above exit_z (mean)`. No behavioural, structural, or risk-premium channel is claimed anywhere in the 116 lines. The file ships no performance number of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Oversold-level fade, long-only, state-holding. The 20-bar rolling mean of `close` is the fair-value anchor; the rolling sample dispersion (pandas default `ddof=1`) is the ruler. A print more than two sample deviations below the anchor is bought as a washout — unlike breakout-chase systems in the pool, this rule buys weakness and holds the full unit through further weakness until price reclaims the anchor itself (`z > 0.0`). There is no trend pre-gate (no EMA, no slope, no ADX, no volume confirmation): any deep-oversold print fires, even inside a vertical downtrend. Unlike cross-edge systems there is no one-bar trigger — the entry and exit are *levels* that hold true across consecutive bars (every bar with `z < -2.0` prints entry; every bar with `z > 0.0` prints exit), so the position rule does the edge work, disclosed. The failure mode is plain: a genuine regime break that pins `z` deeply negative keeps the book long with no stop while the anchor itself slides down bar after bar, and a V-bounce that recovers only to `z = -0.1` is held indefinitely with no profit-taking leg until the full reclaim prints.

## Signal

Exact rule as pinned (any other period, threshold, gate polarity, exit leg, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own:

```text
mean      = rolling_mean(close, 20)      // pandas rolling mean, trailing 20 closes, decision bar inclusive
std       = rolling_std(close, 20)       // pandas rolling sample std, ddof=1 (library default), trailing 20 closes
z         = (curr_close - mean) / std
entry     = (z < -2.0)                   // entry_threshold 2.0 negated
exit_     = (z > 0.0)                    // exit_threshold 0.0
```

- Trade events: `entry_signal=bool(entry)`, `exit_signal=bool(exit_)`, `direction="long"` (literal — no short emission exists anywhere in the file, verified by full-file search). A flat book enters one full unit on an entry bar; a long book exits the full unit on an exit bar. Entries while already long are no-ops under the predeclared single-unit rule (see position rule); exits while flat are deterministic no-ops. Because entry and exit are levels, consecutive oversold bars each print entry (first fills, rest no-ops) and consecutive above-mean bars each print exit (first closes, rest no-ops) — coded holding behavior, disclosed, not a missing edge.
- Direction: long-only. The short side is absent by construction (0 `short` / 0 `sell` in the file) and recorded as explicitly disabled. Spot-compatible (no naked shorting required).
- Exits and risk (explicit): the above-mean level (`z > 0.0`) is the sole position-ending path. Opposite-signal exit is not applicable (no short leg exists). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence = min(|z| / 4.0, 1.0)` on entry bars (0.0 otherwise) and `indicators={z_score, rolling_mean, rolling_std}` are diagnostic — none conditions any order line.
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further entry bars as no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops. Re-entry re-arms on the next `z < -2.0` bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Conflict priority (provably irrelevant): entry and exit cannot fire on the same bar. Entry requires `z < -2.0`; exit requires `z > 0.0` — strict inequalities on the same print with `-2.0 < 0.0`, mutually exclusive on every bar including the degenerate guard path (NaN or `std == 0` returns neither, coded). Hence every bar resolves to at most one of {entry, exit, neither}. No priority rule is needed and none is missing.
- Determinism note for the reviewer: the rule reads only `close` with one trailing 20-bar window, closed-form rolling-mean / rolling-std arithmetic, and one division — no `request.*`, `security()`, `timeframe*`, `barstate.*`, volume-weighted logic, session/calendar call, high/low/open read, or stop/limit order argument anywhere in the file (verified by the census above returning zero matches). The `len(df) < period + 2` guard plus the `NaN / std == 0` short-circuit return only well-defined full windows to the arithmetic. The `compatible_regimes == {"RANGE_BOUND"}` set is metadata never read by the signal path (which takes only `df`/`params`), so no regime model gates any order. The rolling std is the pandas sample estimator (`ddof=1`, the library default the code does not override) — pinned as written; substituting a population denominator would be a different, unpinned rule.

## Required data

- `1h` bars of one pair: `close` only for every order-gating line (rolling mean, rolling sample std, both level legs). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade/aggressor, L2/order-book, on-chain, options/Greeks, sentiment/news, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1h` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; every test reads trailing closes of the same series, never a second feed).
- Warmup: 30 completed `1h` bars flat by record rule — structural minimum is the 22nd completed bar (20-bar rolling seed plus the `period + 2` length guard; pre-seed bars return the explicit no-signal guard, and NaN/std-zero bars return the second explicit guard, both verified in code). Pre-warmup bars are flat by record rule; missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (every window reads completed bars only), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (the file names no venue; the roster pins `_asset BTC` — the Binance/BTCUSDT pin is a researcher market choice, disclosed, never presented as source-native).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted S01508, inside-bar, williams-ema-reclaim, and linreg records establish same-bar-close as the pinned-compatible lane primitive for this exact repository family. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. Entry and exit cannot co-fire (proven above), so no intrabar ordering assumption is needed at all.
- Engine path for `1h` (gate 5, stated plainly): `1h` is a Binance-documented USDT-M kline interval; the derived rule needs only completed `1h` candles (`close`) on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no funding/OI/mark-price leg. That is the same single-frame completed-bar path as the admitted `1h` siblings from this source family. Anything beyond that single-frame completed-bar path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: the source ships only a bare `leverage: 1.0` default with no capital, fee, slippage, funding, or margin assumption (quoted verbatim in census; the absences are disclosed, never read as zero cost) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior. Under the predeclared single-unit rule the sizing overlay changes no trade event.
- Concurrency: single-unit long-flat book — at most one open long; same-direction refires are no-ops by record rule, the mean-reclaim level closes the whole unit, and re-entry is allowed immediately on the next qualifying oversold bar after any exit (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (frozen `period 20 / entry 2.0 / exit 0.0` inputs, trailing close rolling-mean with sample-σ z-score, oversold-level entry, mean-reclaim exit, fixed long-only stance with the literal `"long"` direction token, no risk legs) and the `PREBUILT-ZSCORE` BTC roster pin. It ships no performance number of any kind — this record claims no source-reported performance, and no backtest figure is invented here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` — the sole position-closing path is the coded above-mean `exit_`. The absence is coded (the signal block ends with the single level comparison and only the diagnostic return follows).
2. Variant menus fenced, stated plainly: the `parameter_space()` surface (`period` 10–50, `entry_threshold` 1.5–3.0, `exit_threshold` −0.5–0.5) is a documented search grid the code never runs — this record freezes the `20/2.0/0.0` defaults as written; adopting any grid point would be a different, unpinned rule.
3. Level-hold behavior fires as written, stated plainly: every bar with `z < -2.0` prints entry and every bar with `z > 0.0` prints exit with no edge/cross gate anywhere in the file — adding a cross-up edge, a reclaim confirmation, or an EMA gate would be a different, unpinned rule. Deep-trend oversold bars are bought repeatedly (as no-ops while positioned), not vetoed.
4. No averaging down, stated plainly: consecutive oversold bars while already long are no-ops under the predeclared single-unit rule, matching the file's stateless signal (no position-aware branch exists to implement anything else).
5. Regime/metadata quarantine, stated plainly: `confidence`, `z_score`, `rolling_mean`, `rolling_std`, and the `compatible_regimes == {"RANGE_BOUND"}` set are returned inside diagnostic fields or class metadata and read by zero order-gating comparisons — treating any of them as a gate, filter, or sizing input would be a different, unpinned rule.
6. No future leakage in the stack, stated plainly: at decision bar `t`, the rolling mean, the rolling sample std, and the `curr_close` read use completed-bar closes through `t` with fixed non-negative offsets only (`df["close"]` trailing window plus `.iloc[-1]`). No `security()`, no `request.*`, no negative index, no `open`/`high`/`low`/`volume` read in any order leg; pre-seed and NaN/std-zero bars return the explicit no-signal guards, never a forward read.
7. Pool-cousin fence (QRS RSRS-zscore record), stated plainly: `qrs-penalized-rsrs-zscore-timing-long-flat-btcusdt-1d-2026-10-16.md` trades the same z-score word but is a different mechanism on five axes — different input (600-bar standardized 18-bar high/low regression slope `beta(t)` with correlation penalty vs trailing 20-bar close mean/std here), different trigger (upward rail-cross of the penalized statistic through `+0.7` while flat vs oversold level-hold at `z < -2.0` here), different exit (opposite rail cross / time-box vs mean-reclaim level `z > 0.0` here), different geometry (18/600-bar regression machinery on `1d` vs 20-bar close moments on `1h` here), different source (QRS notebook vs Forven immutable Python commit here). This record is therefore never evidence for that rule, and that record is never this rule's provenance.
8. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT market pin, the `1h` frame adoption, same-bar-close fills (with live intrabar behavior scoped out), the adopted 30-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the rolling-mean/sample-σ arithmetic, the oversold entry, the mean-reclaim exit, the order stance, and the risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, timing, input set, or the Forven engine's own execution semantics passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `20/2.0/0.0` z-score / oversold-level entry / mean-reclaim exit / long-only / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Level-vs-midline relevance: replacing the `z < -2.0` oversold entry with a below-mean entry (`z < 0.0`, same exit) must not improve net expectancy; fail ⇒ the coded deep-oversold level adds nothing over its shallow twin.
- F2 — Reclaim-exit relevance: replacing the `z > 0.0` mean-reclaim exit with an overbought exit (`z > +2.0`, same entries) must not improve net expectancy; fail ⇒ the coded reclaim-through-fair-value exit adds nothing over its opposite-extreme twin.
- F3 — No-gate relevance: adding an EMA50 trend gate to the entry (same levels, same exit) must not improve net expectancy; fail ⇒ the coded ungated posture adds nothing over its trend-gated twin.

## Crypto portability

Pinned to BTCUSDT Binance futures `1h` under the house overlay (market pin is a researcher choice on a venue-agnostic source file; the `_asset BTC` roster pin is adopted as venue rationale, not as performance evidence). The z-score arithmetic ports across perpetual venues without structural change — it reads completed-bar `close` only, so venue volume-definition differences cannot move the signal at all, disclosed. The rule is long-only with no stop leg, so a spot-only deployment expresses it fully, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the file returns the decision bar's own close but ships no explicit fill-timing flag; this record evaluates completed bars only and executes same-bar-close on `1h` BTCUSDT. Any live intrabar behavior is out of scope.
- Derived market pin: the file names no venue and no timeframe (roster pins `_asset BTC` only) — BTCUSDT `1h` is a researcher market/frame choice for the house universe, never a source claim.
- Source economics are leverage-only: beyond the bare `leverage: 1.0` default the source ships no capital sizing, no fee, no slippage, no funding, and no margin assumption — derived evaluation must carry the full house cost load (fees plus historical funding; no hypothetical zero funding claimed), and this record reports no net performance of its own.
- No price stop, no time stop: adverse excursion after placement has no guardrail beyond the mean reclaim; a regime break that pins `z` deeply negative is held with no stop while the anchor slides, and a partial recovery to `z = -0.1` is held indefinitely with no profit-taking leg. This is the coded posture, disclosed as the record's principal risk.
- Level-hold whipsaw: a tick below `-2.0` followed by an immediate reclaim prints a full round-trip loss by construction; chop around `-2.0` prints repeated entry-then-exit round trips, disclosed.
- Seed bars: the 20-bar rolling seed dominates early bars; the first 30 `1h` bars are flat by record rule, so early-history signals never enter any evaluation.
- Sample-std pin: the rolling dispersion is the pandas sample estimator (`ddof=1`); a population denominator would move every `z` print and is a different, unpinned rule.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record; the six-gate claim is pinned-engine expressibility of the declared rule, never a profitability, parity, or trading authorization.

## Adoption boundary

Research-only, not approved. No live, Paper, or Testnet authorization follows from this record. Any downstream standardized overlay (house DCA/capital/leverage), Qlib screening, or Hummingbot re-validation is a separate, explicitly authorized step outside this record.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/zscore_reversion.py (primary source — executable Python strategy, 116 lines, fetched live 2026-10-17 at pinned HEAD commit, 3,300 bytes, SHA-256 `202ebbce…95dcea7`; no performance figure ships anywhere in the file)
- https://github.com/judder659/Forven (repository home; HEAD verified `e9a6c09` by `git ls-remote` this cycle)
