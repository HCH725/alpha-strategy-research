---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven naked 20-bar Donchian prior-band breakout long-flat on BTCUSDT 1d bars
created: 2026-10-22
updated: 2026-10-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-21
sources:
  - https://github.com/judder659/Forven/blob/58ce0d0c73eb1cf1fc1de2d88cf46afd542750d8/forven/strategies/builtin/donchian.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven naked 20-bar Donchian prior-band breakout long-flat on BTCUSDT 1d bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository family that supplied the admitted `forven-donchian-regime-breakout`, `forven-keltner-adx-gated-breakout`, `forven-parabolic-sar-cross`, `forven-ema-cross-adx-regime`, and thirty-plus other admitted Forven records — this record pins ONLY the naked-`donchian.py` literals below, and no reviewer repair may substitute a sibling constant).
- Pinned commit SHA: `58ce0d0c73eb1cf1fc1de2d88cf46afd542750d8` (committed `2026-10-21T18:00:59Z`, verified via the GitHub commits API this cycle; verified as the repository HEAD via `git ls-remote` against `HEAD` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/donchian.py`.
- GitHub blob SHA at the pinned commit: `840b9897a7ed542f6ca131d03bd5ad22f6ca7171`, size 4226 bytes.
- Byte-identity check: the file retrieved from `raw.githubusercontent.com` at the pinned commit is 4226 bytes, 131 lines, SHA-256 `277397dfe525e19882d37b4fff497b4417854a3a8546101c529b427bf7149a58`, and `git hash-object` reproduces the GitHub blob (`840b9897…22f6ca7171`) — the entire file was retrieved twice at two refs (the pinned HEAD and the floating `master`) this cycle, byte-identical both times, and inspected in full.
- Registration: the file self-registers via `TYPE_NAME = "donchian"` (line 9) and `STRATEGY_CLASS = DonchianStrategy` (line 127). It ships a one-row `STRATEGIES` roster (lines 129–131): `("SXXX-DONCHIAN-BTC", DonchianStrategy, {"_asset": "BTC"})` — venue spelling is the bare `"BTC"` asset label only, no timeframe override, no market override. Repo-wide, no pool record pins this file's own entry/exit predicate as its rule (see dedup below).
- The file's own words (quoted for gate evidence, never extended): module docstring `Donchian Channel breakout strategy.` (line 1); class docstring `Donchian Channel Breakout strategy.`; `describe()` returns `Donchian Channel breakout (20-period lookback).` at defaults (lines 59–61); `default_params` returns exactly `{ "period": 20, "leverage": 3.0 }` (lines 49–52) — no cost, no sizing, no risk key ships anywhere in the defaults. No performance phrase of any kind ships anywhere in the 131 lines — this record adopts no source-reported performance (see Evidence).
- Single decision source, verified lockstep: `generate_signal()` (lines 63–109) is the per-bar path; `generate_signals()` (lines 111–121) is the vectorized twin returning `(entry_signals, exit_signals)` boolean Series. Both evaluate the identical predicate — prior-close setup against the prior-bar band plus strict current-close piercing (entry), mirrored on the lower band (exit) — the twin is the same formula in vector spelling, no third path exists (`def generate_signal` occurs exactly twice, lines 63 and 111). The scalar/twin predicate text was diffed field-by-field this cycle and agrees on every comparator, strictness, and shift.
- Band helper pinned in-file (actually read): `donchian_bands` (lines 25–30): `upper = high.rolling(period).max().shift(1)`, `lower = low.rolling(period).min().shift(1)`, `middle = (upper + lower) / 2.0` — prior-bar causal bands with an in-source `to avoid lookahead in both live and backtest paths` docstring (line 26). No second band construction exists anywhere in the file.
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` (12238 bytes, blob `27508a2a6b8c546e21adefdb97fc0144fabf881b` — byte-identical to the blob pinned by the admitted `forven-donchian-regime-breakout` and `forven-keltner-adx-gated-breakout` records) defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults, `direction: str = "long"` default, plus `supported_trade_modes = {"long_only"}` and `mirror_short_safe = False` (this file never overrides either; every return hardcodes `direction="long"`, lines 72/87/102).
- Full-file token census (verified by search over the 131 lines this cycle): `def generate_signal` exactly twice (the lockstep twins — no third path); `STRATEGIES` once (the one-row roster above); `round(` 6 sites (price/indicator formatting only — `price=round(curr_close, 4)`, band echoes, never an order-gating input); 0 `stop` / 0 `trail` / 0 `profit` / 0 `loss` / 0 `take_profit` (no risk order leg exists, not even in prose); 0 `fee` / 0 `funding` / 0 `slippage` / 0 `commission` / 0 `cost` (no economics beyond the bare `"BTC"` label and the fenced leverage default — house overlay supplies sizing/costs, see Execution assumptions); 0 `short` even case-insensitively (the short side is absent by construction, not merely untriggered); 0 `volume` (no volume filter of any kind); 0 `open` even case-insensitively (sole `df[` reads are `close`/`high`/`low` — no session/open-range logic of any kind); 0 `rsi` / 0 `macd` / 0 `stoch` / 0 `adx` / 0 `atr` / 0 `ema` / 0 `vwap` (no indicator conditions any order line — the signal path is pure pandas rolling extremes plus scalar comparisons); 0 `request.` / 0 `security(` / 0 `informative` / 0 `resample` (one prose `merges` token in a resolver comment, line 15 — plumbing prose, never a data path); 0 `timeframe` / 0 `data_requirements` / 0 `1d` / 0 `1h` (the file is timeframe-agnostic — the `1d` decision frame below is a disclosed researcher pin, never a file semantic); 0 `position` / 0 `pyramid` / 0 `opentrades` / 0 `cooldown` (no position-aware state conditions any signal); `middle` 6 sites (helper construction, scalar unpack, NaN-fallback average, indicators echo — never an order-gating input, fenced below).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the 20-bar prior-band construction, the prior-close-setup plus strict-piercing entry, the mirrored opposite-band exit, the long-only stance, the no-risk-leg posture, the prior-bar causal bands, and its own `len < period+2` short-frame guard — but ships no venue spelling beyond `"BTC"`, no timeframe declaration, no fill-timing flag, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1d` (the file's roster names bare `"BTC"` and declares no timeframe; the `BTCUSDT` venue spelling and the `1d` decision-frame pin are disclosed, never a source claim — the 20-bar channel is daily-bar heritage, see Signal); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the thirty-plus admitted Forven records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) single-unit long-flat position pin with hold-no-op semantics plus a 50-bar researcher warmup floor (an already-positioned book treats further breakout bars as hold-no-ops, a flat book treats exit-leg bars as no-ops, re-entry re-arms on any qualifying cross after any exit with no cooldown, pre-warmup bars flat by record rule — the floor covers the source's 22-bar guard plus the rolling-20 seeding transient with margin; see Required data); (4) house sizing/capital/costs supplying the missing economics (the file ships no sizing/cost key at all beyond the fenced leverage default; see Execution assumptions; sizing changes no event under the predeclared single-unit rule). No tie-break pin is needed: entry and exit are provably mutually exclusive on every bar (see Signal).

Pre-write dedup (2026-10-22): working-tree filename/content search for `DonchianStrategy` / `builtin/donchian.py` / `SXXX-DONCHIAN` returns zero pool records pinning this file's own predicate as their rule — the sole pool mention of this blob (`840b9897…`) is the admitted `forven-donchian-regime-breakout` record citing it as an out-of-file band helper for a different source file (`donchian_regime.py`, 55/20-entry/exit with EMA200-plus-ADX25 veto on `1d`), never as its rule. The word `donchian` occurs in the pool elsewhere only inside `donchian-20-10-breakout` (naked Pine 20-entry/10-exit demo on `1h`, no gate — see Negative evidence), `turtle-soup-donchian-fade-bracket` (opposite-side fade bracket, two-sided), and `eterna-donchian-20-1-midline` (two-sided midline machine on `4h`). No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles KCD-ratio) carries this source file or a naked-Donchian breakout. Not a duplicate, paraphrase, or trivial parameter variant: a naked 20-bar prior-band breakout with a mirrored 20-bar opposite-band exit, no veto, traded long-flat on `1d` bars from this immutable file, is a different normalized signal from a 55/20 veto-gated breakout (bars that break out with a cold veto fire there and nothing here), from a 20/10 Pine demo on `1h` (different exit length × different frame × different source), and from any two-sided midline/fade machine (opposite direction handling).

## Economic mechanism

### Source-reported

The source claims only what its sentences print: `Donchian Channel breakout strategy.` — `Donchian Channel breakout (20-period lookback).` No behavioural, structural, or risk-premium channel is claimed anywhere in the 131 lines. The file ships no backtest numbers of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Naked Turtle-style channel breakout, long-only, state-holding. The 20-bar prior high is the classic fast Turtle trigger: it fires only on genuine range expansion beyond everything printed in the last twenty completed bars, with the prior-bar shift guaranteeing the trigger level was knowable before the decision bar opened. There is deliberately no trend veto, no volatility normalization, and no profit-taking leg — a breakout bar is entered at the decision close and held until price breaks the mirror 20-bar prior low, however long that takes. Unlike the pool's veto-gated Donchian sibling (55-bar trigger admitted only with EMA200-plus-ADX25 health), every 20-bar piercing is entered regardless of trend health, so flat is reached only through the opposite-band exit; unlike the pool's naked 20/10 Pine sibling, the exit rail is the slow symmetric 20-bar low rather than a fast 10-bar rail, so winning advances are held materially longer and chop round-trips resolve differently on every tape; unlike Keltner/Bollinger channel cousins (volatility-scaled envelopes), the trigger levels are raw prior extremes with no normalization; unlike the pool's Donchian fade (opposite-side bet on the same geometry), this machine buys the break and never fades it. The failure mode is plain: a V-turn that recovers without first printing a 20-bar piercing is entered strictly after the recovery is underway; chop that pierces the 20-bar high and immediately breaks the 20-bar low whipsaws the book with no cooldown; a vertical advance is held with no profit-taking leg; a grinding decline is watched from flat with no short participation by construction.

## Signal

Exact rule as pinned (any other entry/exit length, band construction, trigger polarity, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own; `donchian_bands` (lines 25–30) is the single band construction both twins share:

```text
inputs (defaults, frozen): period = 20, _asset = "BTC"
bands:   upper_t = max(high_{t-20..t-1})   // rolling(20).max().shift(1), causal prior-bar
         lower_t = min(low_{t-20..t-1})    // rolling(20).min().shift(1), causal prior-bar
ready:   positional index >= 21  (per-bar guard: len(df) < period+2 → neutral; twin shift-NaN rows → False)
entry_t  = (close_{t-1} <= upper_t) AND (close_t > upper_t) AND ready
exit_t   = (close_{t-1} >= lower_t) AND (close_t < lower_t) AND ready
```

- Guard (source-verbatim): `len(df) < period + 2` (line 67) returns the explicit no-signal guard; the vectorized twin carries no separate guard but every shift-NaN row resolves via `.fillna(False)` (line 121). On complete data both agree from positional index 21. `price=round(curr_close, 4)` is formatting only (lines 71/86/101) — never an order-gating input.
- Trade events: `entry_signal` / `exit_signal` booleans (single path) matching the twin's `(entry_signals, exit_signals)` series; `direction="long"` hardcoded on every return (lines 72/87/102). A flat book enters one full unit on an entry bar; a long book exits the full unit on the first exit-leg bar. Entries while already long are no-ops under the predeclared single-unit rule (see position rule); exit-leg bars while flat are deterministic no-ops. Both legs are edge crosses (each fires once on the crossing bar — refires require a fresh cross back through the band).
- Mutual-exclusion proof (no tie-break pin required): entry requires `close_t > upper_t` with `upper_t >= lower_t` on every bar (a max over 20 prior highs vs a min over 20 prior lows; every bar has `high >= low`, so the band pair never inverts — on perfectly flat tape `upper_t == lower_t == close` and both legs still fail), while the exit leg requires `close_t < lower_t` — pairwise unsatisfiable on every bar, degenerate or otherwise. Touches fire nothing: `close == upper` fails the strict entry `>`; `close == lower` fails the strict exit `<`; the setup legs (`close_{t-1} <= upper`, `close_{t-1} >= lower`) admit equality without firing anything by themselves. The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero `short` tokens ship anywhere in the 131 lines, every return hardcodes `direction="long"`, and the pinned base class declares `supported_trade_modes = {"long_only"}` with `mirror_short_safe = False` — a two-sided reading would contradict the file twice over.
- Exits and risk (explicit): the mirrored 20-bar opposite-band breakdown is the sole position-ending path. Opposite-signal exit is not applicable (no short leg exists). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence` (1.0 on entry bars, else 0.0, lines 93–103) and the full `indicators` echo (`upper`, `lower`, `middle`) are diagnostic — none conditions any order line.
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further entry bars as no-ops (no pyramiding, no averaging); a flat book treats exit-leg bars as no-ops. Re-entry re-arms on any qualifying cross after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `close` (both trigger legs) and `high`/`low` (inside the pinned prior-bar bands) with fixed non-negative offsets (one-bar shifts only), exact strict/inclusive comparisons, and zero divisions anywhere in the gating path. The `compatible_regimes` set is class metadata read by zero signal lines. The 20-bar channel is daily-bar heritage (Donchian/Turtle lineage) — the `1d` frame pin below follows the mechanism, disclosed as a researcher choice on a timeframe-agnostic file, never as a file semantic. Substituting a 55/20 veto-gated pair, a 20/10 asymmetric pair, a volatility-scaled envelope, or an unshifted current-bar band would each be a different, unpinned rule.
- Warmup: 50 completed `1d` bars flat by record rule — structural minimum is the 22nd completed bar (the source's own `period+2` guard) plus margin covering the rolling-20 seeding transient and the twin's shift-NaN rows in one disclosed rule. Pre-warmup bars are flat by record rule; missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (every read is a completed bar at a non-negative offset; bands are `shift(1)` prior-bar by construction and by in-source docstring), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Required data

- `close`/`high`/`low` on `BTCUSDT` `1d` completed bars only (sole reads: `close` for both trigger legs; `high`/`low` enter the pinned prior-bar bands). No `open`, no `volume`, no external feed, no funding/OI/mark-price leg, no calendar, no multi-asset input.
- Warmup: 50 completed `1d` bars flat by record rule (structural minimum the 22nd completed bar — the source's own guard — plus margin for the rolling-20 seeding transient).
- Point-in-time: every read is a completed bar at a fixed non-positive offset (the bands look back 20 bars shifted one bar; the cross compares the last two prints); the decision bar's own `close` is both the last input and (via the derived same-bar-close pin, `price=round(curr_close, 4)`) the fill price basis.

## Execution assumptions

- Derived lane (all four pins predeclared in Provenance): `BTCUSDT` `1d`, completed-bar decisions with same-bar-close market fills (`price=round(curr_close, 4)` — the decision bar's own close), single-unit long-flat position with hold-no-op semantics, house sizing/capital/costs supplying the file's missing economics.
- Pinned-engine path (same lane primitive as the thirty-plus admitted Forven siblings on this exact repository family): the pinned Hummingbot package `20260920` / `dev-2.17.0` backtest model prices one market order at the decision bar's own close on `BTCUSDT` `1d` with the fixed research cost model below; pure pandas rolling-extreme arithmetic over completed `close`/`high`/`low` on a single frame with same-bar-close fills is the already-verified subset for this family — no new execution primitive, no multi-asset synchronization, no shared-capital contention, no lower-timeframe alignment, no non-OHLCV input, no next-open/maker/intrabar fill is required by this record. No engine commit, image digest, or file-level simulator claim is made here — compatibility is stated at the pinned package/VERSION lane level only.
- Sizing/capital/costs (explicit fixed research cost model, stated plainly): the file ships no sizing, no capital, and no fee/slippage/funding concept — its bare `"BTC"` label and the fenced `leverage: 3.0` default are never presented as economics. The derived evaluation pins taker fee `0.0005` per side (Binance USDT-M regular schedule, market fills are taker), zero added slippage, and funding explicitly unmodeled: the pinned-package baseline (§4 Funding) records that the pinned V2 backtesting simulator has no proven historical-funding implementation, so this record neither claims funding settlement nor zero-fills it — unsupported, flagged, never reported as realized. Precision/minimums ride the downstream run manifest preflight (min notional/qty/step-size), never fabricated here. The downstream house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) applies to the derived evaluation and changes no trade event under the predeclared single-unit rule — DCA is a downstream execution experiment, never an admission leg of this version. No capital-dependent forced-close state beyond the standard isolated-margin accounting is admitted.
- No stop/limit/trailing/time leg is modelled because none exists in source — explicitly disabled, never defaulted. Missing trade prices are never fabricated (pre-warmup and missing bars stay flat).

## Evidence

### Source-reported

The source ships the full construction (frozen `period = 20` with prior-bar Donchian bands, prior-close-setup plus strict-piercing entry, mirrored opposite-band exit, fixed long-only stance with hardcoded `direction="long"`, no risk legs) and the `SXXX-DONCHIAN-BTC` roster label. It ships no performance number of any kind — this record claims no source-reported performance, and no backtest figure is invented here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No twin-signal ambiguity: the per-bar path and the vectorized twin evaluate the same closed-form predicate (prior-close setup AND strict piercing, mirrored on the lower band) — the only difference is scalar vs Series spelling, diffed field-by-field this cycle. The `len < period+2` guard and the twin's shift-NaN `.fillna(False)` rows agree on the decision bar (positional index 21 is both `>= period+2` and NaN-free on complete data). No third path exists to select between.
2. No out-of-file construction risk: the bands are the in-file `donchian_bands` helper (rolling max/min plus `shift(1)` with an in-source anti-lookahead docstring — read in full with byte/hash pin above); there is no facade import, no scanner estimator, no second band variant to pin or fence.
3. NaN determinism, stated plainly: the file ships an explicit `pd.isna` guard (lines 82–88) collapsing any undecided band row to neutral, and the twin resolves every shift-NaN row via `.fillna(False)` (line 121). A NaN input print meets each strict/inclusive conjunct as `False` on both legs, so corrupt bars emit no signal by construction, never a spurious order. On complete data the 22-bar guard plus the 50-bar researcher floor already cover seeding, so no NaN reaches any order line in the admitted configuration; missing bars stay flat and are never fabricated.
4. Equality boundaries fire nothing: entry demands strict current-bar `close > upper` with setup `close_{t-1} <= upper`; exit demands strict `close < lower` with setup `close_{t-1} >= lower` — touches hold the prior state by construction, including the degenerate flat-tape case (`upper == lower == close` fires neither leg). The reviewer is never asked to invent an ordering.
5. Flat-tape fence: constant `high == low == close` tape makes every setup leg true-or-vacuous but both strict piercing legs false on every bar — the book stays flat forever with no spurious entry, disclosed, not repaired.
6. Dead-middle fence: the `middle` band is constructed (line 29), unpacked (line 76), NaN-fallback-averaged (line 92), and echoed into `indicators` (line 107) — and read by zero order-gating comparisons. Treating it as a gate, filter, or exit rail would be a different, unpinned rule.
7. Legacy-key and tuning-surface fence: `resolve_donchian_period` accepts a legacy `donchian_period` key (lines 12–22, floored at 2) and `parameter_space()` offers `period` in (10, 40, 5) (lines 123–124) — each a different, unpinned rule (renamed-but-equal inputs or re-tuned lengths). This record freezes canonical `period = 20` as written; adopting any of them would change trade events and is never claimed here.
8. Metadata quarantine: `leverage: 3.0` (line 52), `confidence` (1.0/0.0 entry flag), the `indicators={upper, lower, middle}` dict, `compatible_regimes` (`TREND_UP`/`TREND_DOWN`), `describe()`, `name`/`asset`, and the `SXXX-DONCHIAN-BTC` roster row are labels, tuning surface, or diagnostics — none conditions any order line, and no reviewer repair may promote any of them into a leg, a gate, or a sizing input. The house overlay governs sizing/costs, never the fenced leverage default.
9. Pool naked-Donchian sibling fenced, stated plainly: `donchian-20-10-breakout-btcusdt-1h-2026-10-06` (admitted, Pine `simple_donchian_breakout_demo.pine`) trades naked prior-20-high / prior-10-low extremes on `1h` bars. This record trades Forven's naked 20-bar high / 20-bar low symmetric pair on `1d` bars. Distinction: exit length (10 vs 20 — a rail that exits there holds here on every tape where price sits between the two rails) × frame (`1h` vs `1d` — disjoint bar sets, disjoint event sequences) × immutable source file. This record is therefore never evidence for that rule, and that record is never this rule's provenance.
10. Pool veto-gated Donchian sibling fenced, stated plainly: `forven-donchian-regime-breakout-long-flat-btcusdt-1d-2026-10-19` (admitted, `donchian_regime.py` at an older pin) trades a 55-bar high / 20-bar low AND-gated with a close-above-EMA200 plus scanner-ADX ≥ 25 veto. This record trades the naked 20-bar pair with no gate of any kind from a different immutable file. Distinction: entry length (20 vs 55) × gate (none vs EMA200-plus-ADX25 — a veto-failed breakout bar fires here and nothing there) × source file identity. Neither record is the other's provenance.
11. Pool Donchian-geometry cousins fenced, stated plainly: `turtle-soup-donchian-fade-bracket` bets the opposite side of the same geometry (fade the extreme, two-sided bracket) — a breakout bar here is a fade entry there with inverted economics; `eterna-donchian-20-1-midline-two-sided` trades the same 20-bar band two-sided with midline exits — direction handling and exit rails both differ. Opposite direction handling alone fences each pair regardless of shared Donchian vocabulary.
12. Derivation boundary fenced: the only non-source-native behaviours in this record are the `BTCUSDT` market choice, the `1d` frame pin on a timeframe-agnostic file, the same-bar-close fills, the single-unit/no-add/no-cooldown position pin, the 50-bar warmup floor (the file guards only 22 bars), and house sizing/costs — all predeclared above. The 20-bar prior-band construction, the setup-plus-piercing entry, the mirrored opposite-band exit, the long-only stance, and the no-risk-leg posture are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `period = 20` / prior-bar band pair / setup-plus-piercing entry / mirrored 20-bar-low exit / long-only / no risk legs / single-unit / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Exit-rail relevance: replacing the symmetric 20-bar-low exit with the pool's fast 10-bar-low rail (same entries, same posture) must not improve net expectancy; fail ⇒ the slow symmetric rail adds nothing over the admitted fast rail and the record over-claims its exit choice.
- F2 — Entry-length relevance: replacing the 20-bar entry band with the veto-gated sibling's 55-bar band (same mirrored exit form, same posture) must not reproduce-or-beat net expectancy; fail ⇒ the fast-trigger choice adds nothing over the admitted slow trigger and the record is a label variant of one.
- F3 — No-stop relevance: adding a fixed 5% stop to the naked posture (same entries, same band exit) must not improve net expectancy; fail ⇒ the explicitly disabled stop adds nothing to withhold and the no-risk-leg posture is over-claimed.

## Crypto portability

Direct: `BTCUSDT` perpetual/spot `1d` OHLCV on Binance — the rule consumes completed-bar `close`/`high`/`low` only, needs no venue-specific microstructure, no funding input, and no spot-vs-perp distinction in its arithmetic. The long-only no-stop posture expresses fully on spot; perps add no required leg. House costs (fees/funding/slippage) are overlaid downstream per the research campaign; modeled funding is never reported as realized funding, and unmodeled funding is flagged, never zero-filled.

## Limitations

- Late entries by construction: the 20-bar prior high sits above price by definition, so V-turns that recover without first printing a piercing are entered strictly after the recovery is underway — disclosed lag profile.
- Chop whipsaw: closes that pierce the 20-bar high and immediately break the 20-bar low print repeated enter-then-exit round trips with no cooldown and no structural filter — disclosed chop profile.
- No profit-taking: a vertical advance is held with no take-profit leg; opportunity cost accrues, disclosed.
- No risk leg: no stop loss, take profit, trailing-stop order, or time limit exists in source — recorded as explicitly disabled; adverse excursions after an entry have no capital guardrail besides the eventual 20-bar-low exit.
- Downtrend blindness: declines are watched from flat with no short participation — the zero-`short` posture is a stance choice with a return cost in sustained downtrends, disclosed.
- Single-market scope: derived pin is `BTCUSDT` `1d` only; portability to other symbols/timeframes is untested and claimed nowhere in this record.
- Research overlay dependence: fills, sizing, and costs follow the derived lane pins and the downstream house model — not the source engine's own semantics.

## Implementation status

`not-implemented` — no dedicated Qlib/Hummingbot executable artifact exists for this record. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream refusal; if formally selected for execution without a reproducible recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline stage), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/judder659/Forven/blob/58ce0d0c73eb1cf1fc1de2d88cf46afd542750d8/forven/strategies/builtin/donchian.py
- https://github.com/judder659/Forven
