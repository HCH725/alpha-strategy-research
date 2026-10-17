---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven Chaikin-money-flow threshold cross long-flat on BTCUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/chaikin_mf.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven Chaikin-money-flow threshold cross long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, `forven-adl-ema-cross`, `forven-atr-volume-breakout`, `forven-aroon-up-down-cross`, `forven-ema-rsi-pullback-reclaim`, `forven-double-bottom-neckline-break`, and `forven-vwap-rolling-cross` records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/chaikin_mf.py`.
- GitHub blob SHA at the pinned commit: `c361a304eeaacaaee61e1501cafa8440a84843e9`, size 2968 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 2968 bytes, 105 lines, SHA-256 `7dc8c1e25697e9c1ab8f2d5add2176bba65a7cc220347201790a1f9530967176`, identical to the GitHub blob (`git hash-object` reproduces `c361a304…84843e9`) — the entire file was retrieved and inspected; the order-gating rule lives wholly in this one single file with zero out-of-file indicator helpers (only `pandas` plus the local `BaseStrategy, Signal` base are imported).
- The file's own words (quoted for gate evidence, never extended): module docstring `Chaikin Money Flow strategy.`; class docstring `Chaikin Money Flow (CMF) strategy.` / `Entry: CMF crosses above threshold.` / `Exit: CMF crosses below -threshold.`; `describe()` returns `Enters when 20-bar CMF crosses above 0.05. Exits when CMF crosses below -0.05.`; `default_params` returns exactly `{ "cmf_period": 20, "threshold": 0.05, "leverage": 1.0 }`; roster entry `("PREBUILT-CMF", ChaikinMFStrategy, {"_asset": "BTC"})`; `compatible_regimes` returns `{"TREND_UP"}`; `parameter_space()` returns `{ "cmf_period": (10, 30, 5), "threshold": (0.02, 0.10, 0.02) }` (a documented search surface only — this record pins the defaults `20` / `0.05` and runs no search).
- Full-file token census (verified by search over the 105 lines this cycle): 2 `direction` literals, both `"long"` (hardcoded on every return — the sole order-direction token); 0 `short` / 0 `sell` (no short path anywhere); 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` (no order arguments, no risk legs); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 1.0` default); 0 `open` column read / 0 `time` / 0 `request` / 0 `security` / 0 `timeframe` / 0 `barstate` / 0 `funding` (order-gating reads are `high`, `low`, `close` for the money-flow multiplier plus bar `volume` for the money-flow weighting and normalization — zero reads of any other column); 0 `ema` / 0 `rsi` / 0 `atr` / 0 `adx` / 0 `vwap` (no second indicator, no regime-gate read); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` (no position-aware state conditions any signal). Imports are only `pandas` plus the local base — no cross-asset import, no second feed, no external indicator module.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the 20-bar Chaikin-money-flow construction, the +0.05 cross-above entry, the −0.05 cross-below exit, the long-only stance, and the no-stop posture — but ships no venue, no timeframe, no fill-timing flag, and no position-sizing rule inside this file. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted inside-bar, williams-ema-reclaim, linreg, zscore, adl, atr-volume, aroon, ema-rsi-pullback, double-bottom, and vwap-cross records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) an adopted 30-completed-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 22nd completed bar — the 20-bar rolling CMF plus the one-prior-bar cross read — plus margin; see Required data); (4) house sizing/capital/costs replacing the bare `leverage: 1.0` default (see Execution assumptions; sizing changes no event under the predeclared single-unit rule). No tie-break pin is needed: entry and exit are provably mutually exclusive on every bar (see Signal). The CMF arithmetic, the threshold-cross entry, the threshold-cross exit, the long-only stance, and the no-stop/no-target/no-time-exit posture are source-verbatim and unmodified.

Pre-write dedup (2026-10-17): working-tree filename/content search for `builtin/chaikin_mf` / `PREBUILT-CMF` / `ChaikinMF` returns zero strategy records — no record cites this source file. Content search for Chaikin/CMF-family records returns only pool cousins fenced as different mechanisms in Negative evidence 8 (CMF-velocity zero-cross with EMA-200 gate and ATR bracket, two-sided, FMZ source; Chaikin-Oscillator A/D zero-cross momentum-divergence, two-sided). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: a 20-bar CMF level-threshold cross pair (±0.05, no gate, no bracket, long-flat, exited on the opposite threshold cross) is a different signal construction from a 7-bar-averaged CMF-velocity zero-cross behind an EMA-200 gate with a 2:1 ATR stop/limit bracket, or from a MACD-of-A/D-line oscillator — not a threshold re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: a `Chaikin Money Flow (CMF) strategy` of `Entry: CMF crosses above threshold.` / `Exit: CMF crosses below -threshold.` No behavioural, structural, or risk-premium channel is claimed anywhere in the 105 lines. The file ships no performance number of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Volume-signed accumulation participation, long-only, state-holding. Each bar's volume is signed by where the close sits inside the high–low range (close at the high prints +volume, at the low prints −volume) and the 20-bar CMF is that signed flow normalized by total volume — a bounded [−1, +1] gauge of whether volume has been accumulating near the highs or distributing near the lows. The entry buys only the bar that reclaims the +0.05 accumulation threshold from below, and the exit surrenders the unit only on the bar that loses the −0.05 distribution threshold from above; the dead band between the thresholds is an intentional hysteresis that keeps the book holding through neutral chop. Unlike velocity systems there is no differencing leg to whipsaw on flat CMF drift, and unlike level-hold systems there is no repeated-entry pressure — crosses are one-bar edge events, and the predeclared single-unit rule turns any same-side refire into a no-op. The failure mode is plain: a market that accumulates just enough to cross +0.05 and then bleeds sideways into distribution prints a full entry-then-exit round trip with no stop and no profit-taking leg, and a vertical launch that never undercuts −0.05 after entry is simply held (opportunity profile, disclosed).

## Signal

Exact rule as pinned (any other period, threshold, average variant, exit leg, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own:

```text
mfm(t)          = ((close - low) - (high - close)) / (high - low)  // per-bar, causal; 0-range bars divide by 1e-10
mfv(t)          = mfm(t) * volume
cmf(t)          = sum(mfv[-20:]) / sum(volume[-20:])               // rolling 20-bar, causal; 0-volume windows divide by 1e-10
cross_above     = (prev_cmf <= 0.05) and (curr_cmf > 0.05)
cross_below     = (prev_cmf >= -0.05) and (curr_cmf < -0.05)
entry           = cross_above
exit_           = cross_below
```

- Trade events: `entry_signal=bool(entry)`, `exit_signal=bool(exit_)`, `direction="long"` (hardcoded literal — no short emission exists anywhere in the file, verified by full-file search). A flat book enters one full unit on an entry bar; a long book exits the full unit on an exit bar. Entries while already long are no-ops under the predeclared single-unit rule (see position rule); exits while flat are deterministic no-ops. Crosses are one-bar edge events (strict inequalities on the prior/current pair against fixed thresholds), so no level-refire pressure exists by construction.
- Mutual-exclusion proof (no tie-break pin required): entry implies `curr_cmf > 0.05`; exit implies `curr_cmf < -0.05` — no single bar satisfies both, including the exact-equality boundary (strict comparisons fire nothing on ties) and NaN seed bars (all strict comparisons false). The reviewer is never asked to invent an ordering.
- Direction: long-only. The short side is absent by construction (0 `short` / 0 `sell` in the file) and recorded as explicitly disabled. Spot-compatible (no naked shorting required).
- Exits and risk (explicit): the −0.05 cross-below edge is the sole position-ending path. Opposite-signal exit is not applicable (no short leg exists). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence=min(1.0, abs(cmf)/0.2)` on entry bars (else `0.0`) and `indicators={cmf, threshold}` are diagnostic — none conditions any order line.
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further entry bars as no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops. Re-entry re-arms on any qualifying cross after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low`/`close`/`volume` with fixed non-negative offsets (a trailing 20-bar rolling window plus a one-prior-bar cross read) — no `request.*`, `security()`, `timeframe*`, `barstate.*`, funding/OI/mark-price read, session/calendar call, second indicator, or stop/limit order argument anywhere in the file (verified by the census above returning zero matches). The `len(df) < period + 2` guard returns both signals false on short frames; every pre-seed window prints NaN and every NaN strict comparison is false, so pre-seed bars deterministically print neither signal. The two coded guards (`hl_range.replace(0, 1e-10)` on the per-bar money-flow divisor; `.replace(0, 1e-10)` on the volume-sum denominator) keep degenerate bars and zero-volume windows deterministic — comparisons against the resulting finite CMF still resolve false/true by the same strict inequalities, never NaN. The `compatible_regimes == {"TREND_UP"}` set is metadata never read by the signal path (which takes only `df`/`params`); treating the label as a gate would be a different, unpinned rule.

## Required data

- Completed `1h` bars of BTCUSDT: `high`/`low`/`close` (money-flow-multiplier construction and both threshold-cross reads) and bar `volume` (read twice inside the rule — once to sign each bar's flow, once to normalize the 20-bar sum; the rule is doubly volume-weighted, disclosed; no standalone volume threshold leg ships). No `open`-series read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read anywhere.
- Single decision timeframe `1h` (the script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction).
- Warmup: the construction stacks a 20-bar rolling CMF beneath a one-prior-bar cross read (structural need = the 22nd completed `1h` bar). The adopted warmup is the first 30 completed `1h` bars flat by record rule (predeclared researcher choice — structural minimum plus seeding margin). No negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Each bar's prints enter the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (the file names no venue; the roster pins `_asset BTC` — the Binance/BTCUSDT pin is a researcher market choice, disclosed, never presented as source-native).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted inside-bar, williams-ema-reclaim, linreg, zscore, adl, atr-volume, aroon, ema-rsi-pullback, double-bottom, and vwap-cross records establish same-bar-close as the pinned-compatible lane primitive for this exact repository family. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity, and entry/exit can never co-fire (proven above), so no intrabar ordering assumption is needed at all.
- Engine path for `1h` (gate 5, stated plainly): `1h` is a Binance-documented USDT-M kline interval; the derived rule needs only completed `1h` candles (`high`/`low`/`close`/`volume`) on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no funding/OI/mark-price leg. That is the same single-frame completed-bar path as the admitted `1h` siblings from this source family, extended only by a bar-`volume` column read that ships natively on the same kline stream. Anything beyond that single-frame completed-bar path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: the source ships only a bare `leverage: 1.0` default with no capital, fee, slippage, funding, or margin assumption (quoted verbatim in census; the absences are disclosed, never read as zero cost) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior. Under the predeclared single-unit rule the sizing overlay changes no trade event.
- Concurrency: single-unit long-flat book — at most one open long; the −0.05 cross-below edge closes the whole unit, and re-entry is allowed on any qualifying cross after any exit (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (20-bar Chaikin money flow, +0.05 cross-above entry, −0.05 cross-below exit, fixed long-only stance with the literal `"long"` direction token, no risk legs) and the `PREBUILT-CMF` roster pin. It ships no performance number of any kind — this record claims no source-reported performance, and no backtest figure is invented here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` — the sole position-closing path is the coded −0.05 cross-below edge. The absence is coded (the signal block ends with the two comparisons and only the diagnostic return follows).
2. Variant menu fenced, stated plainly: the `parameter_space()` surface (`cmf_period` 10–30 step 5; `threshold` 0.02–0.10 step 0.02) is a documented search grid the code never runs — this record freezes the `20` / `0.05` defaults as written; adopting any grid point would be a different, unpinned rule.
3. Edge-trigger fires as written, stated plainly: entry prints only on the threshold-cross bar (strict prior/current inequalities), not on every bar holding CMF above +0.05 — adding a level-hold posture would be a different, unpinned rule.
4. No averaging down, stated plainly: the file is stateless (no position-aware branch exists to implement anything else) — an already-long book treats further entry bars as no-ops under the predeclared single-unit rule.
5. Regime/metadata/passenger quarantine, stated plainly: `confidence`, the two `indicators` fields (`cmf`, `threshold`), and the `compatible_regimes == {"TREND_UP"}` set are returned inside diagnostic fields or class metadata and read by zero order-gating comparisons — treating any of them as a gate, filter, or sizing input would be a different, unpinned rule.
6. Short-frame path fenced, stated plainly: frames shorter than 22 bars return the last close with both signals false — flat by record rule, and that returned price is a diagnostic echo, never a fill (frames are always full length on the declared venue).
7. Co-fire impossibility fenced with proof, stated plainly: entry requires `curr_cmf > 0.05`, exit requires `curr_cmf < -0.05` — no bar, including exact-equality boundaries, NaN seed bars (all strict comparisons false), zero-range bars, and zero-volume windows (finite guarded divisors, same strict inequalities), can satisfy both. No tie-break, no ordering assumption, and no reviewer invention is required anywhere in this record.
8. Pool-cousin fence (Chaikin/CMF-family records), stated plainly: `cmf-velocity-zero-cross-ema200-bracket-two-sided-btcusdt-1d-2026-10-10.md` enters on a 7-bar-averaged CMF *velocity* (differenced flow) crossing the fixed `0.0` line behind a strict EMA-200 side gate, two-sided with a 2:1 ATR stop/limit bracket plus opposite-cross reversal exits, on `1d`, from an FMZ/ChaoZhang port of TheSadRhinoInvesting's release; `chaikin-oscillator-ad-zero-cross-momentum-divergence-two-sided-btcusdt-4h-2026-10-12.md` trades the MACD of the cumulative A/D line (a different indicator — oscillator of cumulative stock, not a volume-normalized flow ratio), two-sided. This record crosses the 20-bar CMF *level* itself against fixed ±0.05 thresholds with no gate, no bracket, and no differencing leg, long-flat, on BTCUSDT `1h`, from immutable file `builtin/chaikin_mf.py` — different input construction × different trigger × different gate × different exit × different source file. This record is therefore never evidence for those rules, and those records are never this rule's provenance.
9. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT market pin, the `1h` frame adoption, same-bar-close fills (with live intrabar behavior scoped out), the adopted 30-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the CMF arithmetic, the threshold-cross entry, the threshold-cross exit, the order stance, and the risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, timing, input set, or the Forven engine's own execution semantics passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: CMF(20) level-threshold cross pair (+0.05 entry / −0.05 exit) / long-only / BTCUSDT `1h` / same-bar-close fills are frozen.

- F1 — Threshold relevance: replacing the ±0.05 threshold pair with a plain `0.0` level cross (same CMF(20) construction, same opposite-cross exit shape) must not reproduce-or-beat net expectancy; fail ⇒ the coded thresholds add nothing over the zero-line twin.
- F2 — Normalization relevance: replacing the volume-normalized CMF ratio with the unnormalized 20-bar signed money-flow sum (same cross-entry shape against a pinned absolute level, same exit) must not improve net expectancy; fail ⇒ the record is a signed-volume accumulator wearing a normalized-flow label.
- F3 — Level-vs-velocity relevance: replacing the level-threshold cross with a 7-bar CMF-change zero-cross (same 20-bar CMF base, same exit shape) must not improve net expectancy; fail ⇒ the level construction adds nothing over its velocity twin.

## Crypto portability

Pinned to BTCUSDT Binance futures `1h` under the house overlay (market pin is a researcher choice following the file's `_asset BTC` roster pin; the file itself is venue-agnostic). The rule reads the bar-`volume` tape twice (flow signing and flow normalization), so venue volume-definition differences (e.g. spot vs futures volume, wash-reporting) move both the signal level and the threshold-cross timing — stated plainly as a portability boundary: cross-venue porting without re-verification would be a different, unpinned claim, disclosed. The rule is long-only with no stop leg, so a spot-only deployment expresses it fully, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating and no `open`-series read anywhere), so session-gap behavior needs no approximation — the rolling window simply spans the continuous tape. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the file returns the decision bar's own close but ships no explicit fill-timing flag; this record evaluates completed bars only and executes same-bar-close on BTCUSDT `1h`. Any live intrabar behavior is out of scope.
- Derived market pin: the file names no venue and no timeframe (roster pins `_asset BTC` only) — BTCUSDT `1h` is a researcher market/frame choice for the house universe, never a source claim.
- Source economics are leverage-only: beyond the bare `leverage: 1.0` default the source ships no capital sizing, no fee, no slippage, no funding, and no margin assumption — derived evaluation must carry the full house cost load (fees plus historical funding; no hypothetical zero funding claimed), and this record reports no net performance of its own.
- No price stop, no time stop: adverse excursion after placement has no guardrail beyond the opposite threshold cross; a market that accumulates just enough to cross +0.05 and then bleeds into distribution prints repeated entry-then-exit round trips by construction, and a launch that never undercuts −0.05 is simply held (opportunity profile, disclosed). This is the coded posture, disclosed as the record's principal risk.
- Seed bars: the 20-bar rolling window plus the one-prior-bar cross read dominate early bars; the first 30 `1h` bars are flat by record rule, so early-history signals never enter any evaluation. Substituting a seeded/warm-started average would move every early print and is a different, unpinned rule.
- Volume-tape dependence: the CMF numerator and denominator both read bar `volume`; a zero-volume 20-bar window and a zero-range bar are deterministically absorbed by the two coded `1e-10` guards (see Signal), but any venue whose volume tape is missing or redefined moves both the signal level and every threshold cross — disclosed in Crypto portability, never hand-waved.
- No co-fire corner exists: see Negative evidence 7 — entry and exit are mutually exclusive by construction on every bar, so no tie-break pin was adopted.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record; the six-gate claim is pinned-engine expressibility of the declared rule, never a profitability, parity, or trading authorization.

## Adoption boundary

Research-only, not approved. No live, Paper, or Testnet authorization follows from this record. Any downstream standardized overlay (house DCA/capital/leverage), Qlib screening, or Hummingbot re-validation is a separate, explicitly authorized step outside this record.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/chaikin_mf.py (primary source — executable Python strategy, 105 lines, fetched live 2026-10-17 at pinned HEAD commit, 2,968 bytes, SHA-256 `7dc8c1e2…0967176`; pure pandas single-file rule, zero out-of-file indicator helpers; no performance figure ships anywhere in the file)
- https://github.com/judder659/Forven (repository home; HEAD verified `e9a6c09` by `git ls-remote` this cycle)
