---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven rolling-VWAP centerline cross long-flat on BTCUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/vwap_cross.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven rolling-VWAP centerline cross long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, `forven-adl-ema-cross`, `forven-atr-volume-breakout`, `forven-aroon-up-down-cross`, `forven-ema-rsi-pullback-reclaim`, and `forven-double-bottom-neckline-break` records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/vwap_cross.py`.
- GitHub blob SHA at the pinned commit: `a61efed36da265ddf61bb424797c0e3d18c9eebf`, size 2760 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 2760 bytes, 100 lines, SHA-256 `f8b845b9a7791ed192f5a4727e5ea51bbbd7f896e134071bcbc64fe5be04d011`, identical to the GitHub blob (`git hash-object` reproduces `a61efed3…c9eebf`) — the entire file was retrieved and inspected; the order-gating rule lives wholly in this one single file with zero out-of-file indicator helpers (only `numpy`-free `pandas` plus the local `BaseStrategy, Signal` base are imported).
- The file's own words (quoted for gate evidence, never extended): module docstring `VWAP Cross strategy.`; class docstring `VWAP crossover strategy using rolling VWAP.` / `Entry: Close crosses above VWAP from below.` / `Exit: Close crosses below VWAP from above.`; `describe()` returns `Enters when close crosses above rolling 20-bar VWAP. Exits when close crosses below VWAP.`; `default_params` returns exactly `{ "vwap_period": 20, "leverage": 1.0 }`; roster entry `("PREBUILT-VWAP-CROSS", VWAPCrossStrategy, {"_asset": "BTC"})`; `compatible_regimes` returns `{"TREND_UP", "RANGE_BOUND"}`; `parameter_space()` returns `{ "vwap_period": (10, 40, 5) }` (a documented search surface only — this record pins the default `20` and runs no search).
- Full-file token census (verified by search over the 100 lines this cycle): 2 `direction` literals, both `"long"` (hardcoded on every return — the sole order-direction token); 0 `short` / 0 `sell` (no short path anywhere); 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` (no order arguments, no risk legs); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 1.0` default); 0 `open` column read / 0 `time` / 0 `request` / 0 `security` / 0 `timeframe` / 0 `barstate` / 0 `funding` (order-gating reads are `high`, `low`, `close` for the typical price plus bar `volume` inside the VWAP accumulator — zero reads of any other column); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` (no position-aware state conditions any signal). Imports are only `pandas` plus the local base — no cross-asset import, no second feed, no external indicator module.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the rolling-20 typical-price VWAP construction, the close-cross-above entry, the close-cross-below exit, the long-only stance, and the no-stop posture — but ships no venue, no timeframe, no fill-timing flag, and no position-sizing rule inside this file. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted inside-bar, williams-ema-reclaim, linreg, zscore, adl, atr-volume, aroon, ema-rsi-pullback, and double-bottom records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) an adopted 30-completed-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 22nd completed bar — the 20-bar rolling VWAP plus the one-prior-bar cross read — plus margin; see Required data); (4) house sizing/capital/costs replacing the bare `leverage: 1.0` default (see Execution assumptions; sizing changes no event under the predeclared single-unit rule). No tie-break pin is needed: entry and exit are provably mutually exclusive on every bar (see Signal). The VWAP arithmetic, the cross entry, the cross exit, the long-only stance, and the no-stop/no-target/no-time-exit posture are source-verbatim and unmodified.

Pre-write dedup (2026-10-17): working-tree filename/content search for `builtin/vwap_cross` / `PREBUILT-VWAP-CROSS` / `VWAPCrossStrategy` returns zero strategy records — no record cites this source file. Content search for VWAP-family records returns only pool cousins fenced as different mechanisms in Negative evidence 8 (Eterna session-anchored VWAP band-tap two-sided system with EMA-50 gate; GKV adaptive-volatility VWMA(14) band-breakout long-flat). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: a fixed-window rolling-VWAP centerline cross with no bands and no regime gate, exited on the opposite centerline cross, is a different signal construction from session-anchored band-tap entries with an EMA-50 gate and center-line exits, or from adaptive-volatility band breakouts — not a threshold re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: a `VWAP crossover strategy using rolling VWAP` of `Entry: Close crosses above VWAP from below.` / `Exit: Close crosses below VWAP from above.` No behavioural, structural, or risk-premium channel is claimed anywhere in the 100 lines. The file ships no performance number of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Volume-weighted trend participation, long-only, state-holding. The rolling 20-bar VWAP is the recent session's volume-weighted mean price — not a time average — so the reference line leans toward where volume actually traded; the entry buys only the bar that reclaims that line from below, and the exit surrenders the unit only on the bar that loses it from above. Unlike band systems there are no rails to hold inside: every cross is decisive, and unlike level-hold systems there is no repeated-entry pressure — crosses are one-bar edge events, and the predeclared single-unit rule turns any same-side refire into a no-op. The failure mode is plain: a range that chops across its own 20-bar mean prints repeated cross-then-cross round trips with no stop and no profit-taking leg, and a vertical launch that never undercuts its mean after entry is simply held (opportunity profile, disclosed).

## Signal

Exact rule as pinned (any other period, average variant, exit leg, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own:

```text
typical_price   = (high + low + close) / 3                       // per-bar, causal
tp_vol          = typical_price * volume
vwap(t)         = sum(tp_vol[-20:]) / sum(volume[-20:])          // rolling 20-bar, causal
cross_above     = (prev_close <= prev_vwap) and (curr_close > curr_vwap)
cross_below     = (prev_close >= prev_vwap) and (curr_close < curr_vwap)
entry           = cross_above
exit_           = cross_below
```

- Trade events: `entry_signal=bool(entry)`, `exit_signal=bool(exit_)`, `direction="long"` (hardcoded literal — no short emission exists anywhere in the file, verified by full-file search). A flat book enters one full unit on an entry bar; a long book exits the full unit on an exit bar. Entries while already long are no-ops under the predeclared single-unit rule (see position rule); exits while flat are deterministic no-ops. Crosses are one-bar edge events (strict inequalities on the prior/current pair), so no level-refire pressure exists by construction.
- Mutual-exclusion proof (no tie-break pin required): entry implies `curr_close > curr_vwap`; exit implies `curr_close < curr_vwap` — no single bar satisfies both, including the exact-equality boundary (strict comparisons fire nothing on ties) and NaN seed bars (all strict comparisons false). The reviewer is never asked to invent an ordering.
- Direction: long-only. The short side is absent by construction (0 `short` / 0 `sell` in the file) and recorded as explicitly disabled. Spot-compatible (no naked shorting required).
- Exits and risk (explicit): the cross-below edge is the sole position-ending path. Opposite-signal exit is not applicable (no short leg exists). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence=0.6` on entry bars (else `0.0`) and `indicators={vwap, close}` are diagnostic — none conditions any order line.
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further entry bars as no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops. Re-entry re-arms on any qualifying cross after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low`/`close`/`volume` with fixed non-negative offsets (a trailing 20-bar rolling window plus a one-prior-bar cross read) — no `request.*`, `security()`, `timeframe*`, `barstate.*`, funding/OI/mark-price read, session/calendar call, or stop/limit order argument anywhere in the file (verified by the census above returning zero matches). The `len(df) < period + 2` guard returns both signals false on short frames; every pre-seed window prints NaN and every NaN strict comparison is false, so pre-seed bars deterministically print neither signal. The zero-volume-window guard (`.replace(0, 1e-10)` on the volume-sum denominator) keeps degenerate windows deterministic — comparisons against the resulting finite VWAP still resolve false/true by the same strict inequalities, never NaN. The `compatible_regimes == {"TREND_UP", "RANGE_BOUND"}` set is metadata never read by the signal path (which takes only `df`/`params`); treating the label as a gate would be a different, unpinned rule.

## Required data

- Completed `1h` bars of BTCUSDT: `close`/`high`/`low` (typical-price construction and both cross reads) and bar `volume` (read inside the rolling-VWAP accumulator — the rule's mean reference is volume-weighted, disclosed; no standalone volume threshold leg ships). No `open`-series read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read anywhere.
- Single decision timeframe `1h` (the script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction).
- Warmup: the construction stacks a 20-bar rolling VWAP beneath a one-prior-bar cross read (structural need = the 22nd completed `1h` bar). The adopted warmup is the first 30 completed `1h` bars flat by record rule (predeclared researcher choice — structural minimum plus seeding margin). No negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Each bar's prints enter the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (the file names no venue; the roster pins `_asset BTC` — the Binance/BTCUSDT pin is a researcher market choice, disclosed, never presented as source-native).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted inside-bar, williams-ema-reclaim, linreg, zscore, adl, atr-volume, aroon, ema-rsi-pullback, and double-bottom records establish same-bar-close as the pinned-compatible lane primitive for this exact repository family. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity, and entry/exit can never co-fire (proven above), so no intrabar ordering assumption is needed at all.
- Engine path for `1h` (gate 5, stated plainly): `1h` is a Binance-documented USDT-M kline interval; the derived rule needs only completed `1h` candles (`close`/`high`/`low`/`volume`) on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no funding/OI/mark-price leg. That is the same single-frame completed-bar path as the admitted `1h` siblings from this source family, extended only by a bar-`volume` column read that ships natively on the same kline stream. Anything beyond that single-frame completed-bar path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: the source ships only a bare `leverage: 1.0` default with no capital, fee, slippage, funding, or margin assumption (quoted verbatim in census; the absences are disclosed, never read as zero cost) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior. Under the predeclared single-unit rule the sizing overlay changes no trade event.
- Concurrency: single-unit long-flat book — at most one open long; the cross-below edge closes the whole unit, and re-entry is allowed on any qualifying cross after any exit (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (rolling-20 typical-price VWAP, close-cross-above entry, close-cross-below exit, fixed long-only stance with the literal `"long"` direction token, no risk legs) and the `PREBUILT-VWAP-CROSS` roster pin. It ships no performance number of any kind — this record claims no source-reported performance, and no backtest figure is invented here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` — the sole position-closing path is the coded cross-below edge. The absence is coded (the signal block ends with the two comparisons and only the diagnostic return follows).
2. Variant menu fenced, stated plainly: the `parameter_space()` surface (`vwap_period` 10–40 step 5) is a documented search grid the code never runs — this record freezes the `20` default as written; adopting any grid point would be a different, unpinned rule.
3. Edge-trigger fires as written, stated plainly: entry prints only on the cross bar (strict prior/current inequalities), not on every bar holding close above VWAP — adding a level-hold posture would be a different, unpinned rule.
4. No averaging down, stated plainly: the file is stateless (no position-aware branch exists to implement anything else) — an already-long book treats further entry bars as no-ops under the predeclared single-unit rule.
5. Regime/metadata/passenger quarantine, stated plainly: `confidence`, the two `indicators` fields (`vwap`, `close`), and the `compatible_regimes == {"TREND_UP", "RANGE_BOUND"}` set are returned inside diagnostic fields or class metadata and read by zero order-gating comparisons — treating any of them as a gate, filter, or sizing input would be a different, unpinned rule.
6. Short-frame path fenced, stated plainly: frames shorter than 22 bars return the last close with both signals false — flat by record rule, and that returned price is a diagnostic echo, never a fill (frames are always full length on the declared venue).
7. Co-fire impossibility fenced with proof, stated plainly: entry requires `curr_close > curr_vwap`, exit requires `curr_close < curr_vwap` — no bar, including exact-equality boundaries, NaN seed bars (all strict comparisons false), and zero-volume windows (finite guarded denominator, same strict inequalities), can satisfy both. No tie-break, no ordering assumption, and no reviewer invention is required anywhere in this record.
8. Pool-cousin fence (VWAP-family records), stated plainly: `vwap-bounce-band-reversal-two-sided-btcusdt-1h-2026-10-12.md` enters on wick-touch-gated taps of session-anchored ±0.5% VWAP deviation bands behind an EMA-50 regime gate, two-sided with VWAP-center-line exits, from an Eterna Pine source; `gkv-adaptive-vwma-band-breakout-long-flat-btcusdt-1d-2026-10-15.md` enters on closes above an adaptive-volatility-multiplied VWMA(14) upper band with a lower-band exit, long-flat on `1d`, from its own Pine source. This record crosses a fixed rolling-20 typical-price VWAP centerline with no bands, no regime gate, and no session reset, long-flat, on BTCUSDT `1h`, from immutable file `builtin/vwap_cross.py` — different input construction × different trigger × different gate × different exit × different source file. This record is therefore never evidence for those rules, and those records are never this rule's provenance.
9. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT market pin, the `1h` frame adoption, same-bar-close fills (with live intrabar behavior scoped out), the adopted 30-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the VWAP arithmetic, the cross entry, the cross exit, the order stance, and the risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, timing, input set, or the Forven engine's own execution semantics passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: rolling-VWAP(20) centerline cross / cross-below exit / long-only / BTCUSDT `1h` / same-bar-close fills are frozen.

- F1 — Weighting relevance: replacing the volume-weighted rolling mean with a plain 20-bar SMA of typical price (same cross entry shape, same opposite-cross exit) must not reproduce-or-beat net expectancy; fail ⇒ the record is a moving-average cross wearing a volume-weighted label.
- F2 — Edge relevance: replacing the cross-edge entry with a level-hold entry (close above VWAP on every such bar, same exit) must not improve net expectancy; fail ⇒ the coded edge adds nothing over its level twin.
- F3 — Window relevance: replacing the 20-bar rolling window with a session-anchored VWAP (same cross entry shape, same exit) must not improve net expectancy; fail ⇒ the fixed-window construction adds nothing over the session-anchored twin.

## Crypto portability

Pinned to BTCUSDT Binance futures `1h` under the house overlay (market pin is a researcher choice following the file's `_asset BTC` roster pin; the file itself is venue-agnostic). The rule reads the bar-`volume` tape inside the VWAP accumulator, so venue volume-definition differences (e.g. spot vs futures volume, wash-reporting) can move the reference line — stated plainly as a portability boundary: cross-venue porting without re-verification would be a different, unpinned claim, disclosed. The rule is long-only with no stop leg, so a spot-only deployment expresses it fully, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation — the rolling window simply spans the continuous tape. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the file returns the decision bar's own close but ships no explicit fill-timing flag; this record evaluates completed bars only and executes same-bar-close on BTCUSDT `1h`. Any live intrabar behavior is out of scope.
- Derived market pin: the file names no venue and no timeframe (roster pins `_asset BTC` only) — BTCUSDT `1h` is a researcher market/frame choice for the house universe, never a source claim.
- Source economics are leverage-only: beyond the bare `leverage: 1.0` default the source ships no capital sizing, no fee, no slippage, no funding, and no margin assumption — derived evaluation must carry the full house cost load (fees plus historical funding; no hypothetical zero funding claimed), and this record reports no net performance of its own.
- No price stop, no time stop: adverse excursion after placement has no guardrail beyond the opposite cross; a range that chops across its own 20-bar mean prints repeated entry-then-exit round trips by construction, and a launch that never undercuts its mean is simply held (opportunity profile, disclosed). This is the coded posture, disclosed as the record's principal risk.
- Seed bars: the 20-bar rolling window plus the one-prior-bar cross read dominate early bars; the first 30 `1h` bars are flat by record rule, so early-history signals never enter any evaluation. Substituting a seeded/warm-started average would move every early print and is a different, unpinned rule.
- Volume-tape dependence: the VWAP denominator reads bar `volume`; a zero-volume 20-bar window is deterministically absorbed by the coded `.replace(0, 1e-10)` guard (see Signal), but any venue whose volume tape is missing or redefined moves the reference line — disclosed in Crypto portability, never hand-waved.
- No co-fire corner exists: see Negative evidence 7 — entry and exit are mutually exclusive by construction on every bar, so no tie-break pin was adopted.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record; the six-gate claim is pinned-engine expressibility of the declared rule, never a profitability, parity, or trading authorization.

## Adoption boundary

Research-only, not approved. No live, Paper, or Testnet authorization follows from this record. Any downstream standardized overlay (house DCA/capital/leverage), Qlib screening, or Hummingbot re-validation is a separate, explicitly authorized step outside this record.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/vwap_cross.py (primary source — executable Python strategy, 100 lines, fetched live 2026-10-17 at pinned HEAD commit, 2,760 bytes, SHA-256 `f8b845b9…64fe5be04d011`; pure pandas single-file rule, zero out-of-file indicator helpers; no performance figure ships anywhere in the file)
- https://github.com/judder659/Forven (repository home; HEAD verified `e9a6c09` by `git ls-remote` this cycle)
