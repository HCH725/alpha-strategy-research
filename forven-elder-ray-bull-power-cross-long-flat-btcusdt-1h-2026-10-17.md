---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven Elder-ray bull-power cross long-flat on BTCUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/elder_ray.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven Elder-ray bull-power cross long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, `forven-adl-ema-cross`, `forven-atr-volume-breakout`, `forven-aroon-up-down-cross`, `forven-ema-rsi-pullback-reclaim`, `forven-double-bottom-neckline-break`, `forven-vwap-rolling-cross`, and `forven-chaikin-mf-threshold-cross` records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/elder_ray.py`.
- GitHub blob SHA at the pinned commit: `558af2cc55a406c4df2dd4776c8f958c2c4519b1`, size 2683 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 2683 bytes, 89 lines, SHA-256 `97c814c9cedd81fa44dc69a1633756abddfc9f9989faac00fe91477c3325926d`, identical to the GitHub blob (`git hash-object` reproduces `558af2cc…4519b1`) — the entire file was retrieved and inspected; the order-gating rule lives wholly in this one single file with zero out-of-file indicator helpers (only `numpy`/`pandas` plus the local `BaseStrategy, Signal` base are imported).
- The file's own words (quoted for gate evidence, never extended): module docstring `Elder Ray (Bull / Bear Power) strategy.` / `Uses an EMA of close prices to derive Bull Power (High - EMA) and Bear Power (Low - EMA). Enters long when the EMA is rising and Bull Power crosses above zero.`; `describe()` returns `Elder Ray strategy with a 13-period EMA. Enters long when EMA is rising and Bull Power crosses above zero.`; `default_params` returns exactly `{ "ema_period": 13, "leverage": 1.0 }`; roster entry `("PREBUILT-ELDER-RAY", ElderRayStrategy, {"_asset": "BTC"})`; `compatible_regimes` returns `{"TREND_UP"}`; `parameter_space()` returns `{ "ema_period": (5, 26, 1) }` (a documented search surface only — this record pins the default `13` and runs no search). The exit leg is pinned by the code comment `Exit: Bull Power falls back below 0 or EMA declining` together with the coded `exit_` line — quoted verbatim in Signal; the prose `describe()` names only the entry and is never treated as the exit specification.
- Full-file token census (verified by search over the 89 lines this cycle): 1 `direction` literal, `"long"` (the sole order-direction token); 0 `short` / 0 `sell` (no short path anywhere); 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` (no order arguments, no risk legs); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 1.0` default); 0 `open` column read / 0 `volume` / 0 `time` / 0 `request` / 0 `security` / 0 `timeframe` / 0 `barstate` / 0 `funding` (order-gating reads are `high`, `low`, `close` only — volume is never read anywhere in the file); 0 `rsi` / 0 `atr` / 0 `adx` / 0 `vwap` (no second indicator, no regime-gate read; `ema` hits are the indicator itself); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` (no position-aware state conditions any signal). `bear_power` is computed and returned inside the diagnostic `indicators` dict only — zero order-gating comparisons read it.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the 13-bar close-EMA construction, the Bull-Power (high − EMA) cross-above-zero entry behind a rising-EMA gate, the fall-below-zero / EMA-declining exit, the long-only stance, and the no-stop posture — but ships no venue, no timeframe, no fill-timing flag, and no position-sizing rule inside this file. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted inside-bar, williams-ema-reclaim, linreg, zscore, adl, atr-volume, aroon, ema-rsi-pullback, double-bottom, vwap-cross, and chaikin-mf records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) an adopted 30-completed-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 15th completed bar — the coded `ema_period + 2` guard — plus margin; see Required data); (4) house sizing/capital/costs replacing the bare `leverage: 1.0` default (see Execution assumptions; sizing changes no event under the predeclared single-unit rule). No tie-break pin is needed: entry and exit are provably mutually exclusive on every bar (see Signal). The Bull/Bear-Power arithmetic, the cross entry with its rising gate, the exit pair, the long-only stance, and the no-stop/no-target/no-time-exit posture are source-verbatim and unmodified.

Pre-write dedup (2026-10-17): working-tree filename/content search for `builtin/elder_ray` / `PREBUILT-ELDER-RAY` / `ElderRayStrategy` returns zero strategy records — no record cites this source file. Pool cousins fenced as different mechanisms in Negative evidence 8 (FMZ Elder-ray 123-reversal combo with a session-anchored DayHigh Elder leg behind a two-leg agreement gate, two-sided; Elder-impulse dual-slope state-flip, two-sided). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: a Bull-Power (high − EMA13) zero-cross entry behind a rising-EMA gate with a fall-below-zero / EMA-declining exit, long-flat, from immutable file `builtin/elder_ray.py`, is a different signal construction from a DayHigh-minus-EMA agreement-gated combo or an impulse slope-flip system — not a threshold re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: an `Elder Ray (Bull / Bear Power) strategy` of `Bull Power (High - EMA)` / `Bear Power (Low - EMA)` with `Enters long when the EMA is rising and Bull Power crosses above zero.` No behavioural, structural, or risk-premium channel is claimed anywhere in the 89 lines. The file ships no performance number of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Trend-consensus participation, long-only, state-holding. Each bar's Bull Power (`high − EMA13(close)`) measures how far the bar's high prints above the 13-bar value consensus; the entry buys only the bar where that power reclaims the zero line from below while the consensus itself is still rising — buyers proving strength at the highs with the trend behind them. The exit surrenders the unit on the first bar where the high slips back under the consensus or the consensus itself ticks down; the rising-EMA gate that armed the entry doubles as a trailing regime guard once long. Unlike level-hold systems there is no repeated-entry pressure — the entry is a one-bar cross edge — and unlike stop-based systems there is no fixed-distance risk leg: a market that spikes through zero on a single high print and then fades hands back the unit on the next bar by construction (whipsaw profile, disclosed).

## Signal

Exact rule as pinned (any other period, gate, exit leg, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own:

```text
ema(t)            = ewm(span=13, adjust=False) of close                  // causal
bull(t)           = high - ema(t)
bear(t)           = low - ema(t)                                          // diagnostic only, never gates an order
ema_rising        = ema(curr) > ema(prev)
entry             = ema_rising and (prev_bull <= 0.0) and (curr_bull > 0.0)
exit_             = (curr_bull < 0.0) or (not ema_rising)
```

- Trade events: `entry_signal=bool(entry)`, `exit_signal=bool(exit_)`, `direction="long"` (hardcoded literal — no short emission exists anywhere in the file, verified by full-file search). A flat book enters one full unit on an entry bar; a long book exits the full unit on an exit bar. Entries while already long are no-ops under the predeclared single-unit rule (see position rule); exits while flat are deterministic no-ops. The entry is a one-bar cross edge (strict inequalities on the prior/current pair against the fixed zero line), so no level-refire pressure exists by construction; the exit is level-based by code and fires on any qualifying bar.
- Mutual-exclusion proof (no tie-break pin required): entry implies `curr_bull > 0.0` and `ema_rising`; exit requires `curr_bull < 0.0` or `not ema_rising` — no single bar satisfies both, including the exact-equality boundary (strict comparisons fire nothing on ties) and short-frame bars (both signals false by the length guard). The reviewer is never asked to invent an ordering.
- Direction: long-only. The short side is absent by construction (0 `short` / 0 `sell` in the file) and recorded as explicitly disabled. Spot-compatible (no naked shorting required).
- Exits and risk (explicit): the fall-below-zero / EMA-declining pair is the sole position-ending path. Opposite-signal exit is not applicable (no short leg exists). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence=clip(bull/close, 0, 1)` and the `indicators={bull_power, bear_power, ema, ema_rising}` dict are diagnostic — none conditions any order line.
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further entry bars as no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops. Re-entry re-arms on any qualifying cross after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low`/`close` with fixed non-negative offsets (a trailing EMA plus a one-prior-bar cross/gate read) — no `request.*`, `security()`, `timeframe*`, `barstate.*`, volume, funding/OI/mark-price read, session/calendar call, second indicator, or stop/limit order argument anywhere in the file (verified by the census above returning zero matches). The `len(df) < ema_period + 2` guard returns both signals false on short frames. The `compatible_regimes == {"TREND_UP"}` set is metadata never read by the signal path (which takes only `df`/`params`); treating the label as a gate would be a different, unpinned rule.

## Required data

- Completed `1h` bars of BTCUSDT: `high`/`low`/`close` only (Bull/Bear-Power construction, the zero-cross reads, and the rising-EMA gate). No `open`-series read, no bar `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read anywhere.
- Single decision timeframe `1h` (the script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction).
- Warmup: the construction stacks a 13-bar EMA beneath a one-prior-bar cross/gate read (coded guard = the 15th completed `1h` bar). The adopted warmup is the first 30 completed `1h` bars flat by record rule (predeclared researcher choice — coded minimum plus seeding margin). No negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Each bar's prints enter the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (the file names no venue; the roster pins `_asset BTC` — the Binance/BTCUSDT pin is a researcher market choice, disclosed, never presented as source-native).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted inside-bar, williams-ema-reclaim, linreg, zscore, adl, atr-volume, aroon, ema-rsi-pullback, double-bottom, vwap-cross, and chaikin-mf records establish same-bar-close as the pinned-compatible lane primitive for this exact repository family. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity, and entry/exit can never co-fire (proven above), so no intrabar ordering assumption is needed at all.
- Engine path for `1h` (gate 5, stated plainly): `1h` is a Binance-documented USDT-M kline interval; the derived rule needs only completed `1h` candles (`high`/`low`/`close`) on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no volume tape, no funding/OI/mark-price leg. That is the same single-frame completed-bar path as the admitted `1h` siblings from this source family, minus even the volume-column read the chaikin-mf record carries. Anything beyond that single-frame completed-bar path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: the source ships only a bare `leverage: 1.0` default with no capital, fee, slippage, funding, or margin assumption (quoted verbatim in census; the absences are disclosed, never read as zero cost) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior. Under the predeclared single-unit rule the sizing overlay changes no trade event.
- Concurrency: single-unit long-flat book — at most one open long; the exit pair closes the whole unit, and re-entry is allowed on any qualifying cross after any exit (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (13-bar close EMA, Bull Power = high − EMA, cross-above-zero entry behind the rising-EMA gate, fall-below-zero / EMA-declining exit, fixed long-only stance with the literal `"long"` direction token, no risk legs) and the `PREBUILT-ELDER-RAY` roster pin. It ships no performance number of any kind — this record claims no source-reported performance, and no backtest figure is invented here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` — the sole position-closing path is the coded fall-below-zero / EMA-declining pair. The absence is coded (the signal block ends with the two comparisons and only the diagnostic return follows).
2. Variant menu fenced, stated plainly: the `parameter_space()` surface (`ema_period` 5–26 step 1) is a documented search grid the code never runs — this record freezes the `13` default as written; adopting any grid point would be a different, unpinned rule.
3. Edge-trigger fires as written, stated plainly: entry prints only on the zero-cross bar behind a rising EMA (strict prior/current inequalities), not on every bar holding Bull Power above zero — adding a level-hold posture would be a different, unpinned rule.
4. No averaging down, stated plainly: the file is stateless (no position-aware branch exists to implement anything else) — an already-long book treats further entry bars as no-ops under the predeclared single-unit rule.
5. Regime/metadata/passenger quarantine, stated plainly: `confidence`, the four `indicators` fields (`bull_power`, `bear_power`, `ema`, `ema_rising`), and the `compatible_regimes == {"TREND_UP"}` set are returned inside diagnostic fields or class metadata and read by zero order-gating comparisons — treating any of them (including `bear_power` or the regime label) as a gate, filter, or sizing input would be a different, unpinned rule.
6. Short-frame path fenced, stated plainly: frames shorter than 15 bars return the last close with both signals false — flat by record rule, and that returned price is a diagnostic echo, never a fill (frames are always full length on the declared venue).
7. Co-fire impossibility fenced with proof, stated plainly: entry requires `curr_bull > 0.0` with a rising EMA, exit requires `curr_bull < 0.0` or a non-rising EMA — no bar, including exact-equality boundaries and short-frame bars (both signals false), can satisfy both. No tie-break, no ordering assumption, and no reviewer invention is required anywhere in this record.
8. Pool-cousin fence (Elder-family records), stated plainly: `elder-ray-123reversal-combo-two-sided-btcusdt-1h-2026-10-09.md` fires only when a consecutive-close/stochastic streak leg AND a session-anchored DayHigh-minus-EMA Elder leg agree (two-leg agreement gate with an explicit flat state, two-sided, FMZ 432762 source); `elder-impulse-dual-slope-state-flip-two-sided-btcusdt-1d-2026-10-10.md` is an impulse slope-flip state system, two-sided. This record crosses Bull Power (`high − EMA13`) itself against the fixed zero line behind a rising-EMA gate with a fall-below-zero / EMA-declining exit, long-flat, on BTCUSDT `1h`, from immutable file `builtin/elder_ray.py` — different input construction × different trigger × different gate × different exit × different source file. This record is therefore never evidence for those rules, and those records are never this rule's provenance.
9. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT market pin, the `1h` frame adoption, same-bar-close fills (with live intrabar behavior scoped out), the adopted 30-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the Bull/Bear-Power arithmetic, the gated cross entry, the exit pair, the order stance, and the risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, timing, input set, or the Forven engine's own execution semantics passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: Bull-Power (high − EMA13) zero-cross entry behind the rising-EMA gate / long-only / BTCUSDT `1h` / same-bar-close fills are frozen.

- F1 — Gate relevance: removing the rising-EMA gate (bare Bull-Power zero-cross entry, same exit pair) must not reproduce-or-beat net expectancy; fail ⇒ the coded gate adds nothing over the bare cross.
- F2 — Exit-leg relevance: replacing the exit pair with the bare fall-below-zero leg alone (dropping the EMA-declining clause) must not improve net expectancy; fail ⇒ the declining-EMA clause is dead code wearing a risk-leg label.
- F3 — Power-vs-price relevance: replacing the Bull-Power cross (high − EMA) with a plain close-over-EMA cross (same gate, same exit) must not improve net expectancy; fail ⇒ the high-based power construction adds nothing over its close-based twin.

## Crypto portability

Pinned to BTCUSDT Binance futures `1h` under the house overlay (market pin is a researcher choice following the file's `_asset BTC` roster pin; the file itself is venue-agnostic). The rule reads no volume tape, no funding, and no calendar — only `high`/`low`/`close` — so venue volume-definition differences cannot move any print; stated plainly as a portability strength with its boundary: cross-venue porting without re-verification would still be a different, unpinned claim, disclosed. The rule is long-only with no stop leg, so a spot-only deployment expresses it fully, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating and no `open`-series read anywhere), so session-gap behavior needs no approximation — the EMA simply spans the continuous tape. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the file returns the decision bar's own close but ships no explicit fill-timing flag; this record evaluates completed bars only and executes same-bar-close on BTCUSDT `1h`. Any live intrabar behavior is out of scope.
- Derived market pin: the file names no venue and no timeframe (roster pins `_asset BTC` only) — BTCUSDT `1h` is a researcher market/frame choice for the house universe, never a source claim.
- Source economics are leverage-only: beyond the bare `leverage: 1.0` default the source ships no capital sizing, no fee, no slippage, no funding, and no margin assumption — derived evaluation must carry the full house cost load (fees plus historical funding; no hypothetical zero funding claimed), and this record reports no net performance of its own.
- No price stop, no time stop: adverse excursion after placement has no guardrail beyond the exit pair; a market that spikes Bull Power through zero on one high print and then fades hands the unit straight back on the next bar by construction, and a launch that never undercuts the consensus while the EMA keeps rising is simply held (opportunity profile, disclosed). This is the coded posture, disclosed as the record's principal risk.
- Seed bars: the 13-bar EMA plus the one-prior-bar cross/gate read dominate early bars; the first 30 `1h` bars are flat by record rule, so early-history signals never enter any evaluation. Substituting a seeded/warm-started average would move every early print and is a different, unpinned rule.
- Exit-level chatter: the exit pair is level-based, so a book that re-enters on a fresh cross while the EMA oscillates flat can print repeated entry-then-exit round trips by construction — disclosed, never hand-waved.
- No co-fire corner exists: see Negative evidence 7 — entry and exit are mutually exclusive by construction on every bar, so no tie-break pin was adopted.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record; the six-gate claim is pinned-engine expressibility of the declared rule, never a profitability, parity, or trading authorization.

## Adoption boundary

Research-only, not approved. No live, Paper, or Testnet authorization follows from this record. Any downstream standardized overlay (house DCA/capital/leverage), Qlib screening, or Hummingbot re-validation is a separate, explicitly authorized step outside this record.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/elder_ray.py (primary source — executable Python strategy, 89 lines, fetched live 2026-10-17 at pinned HEAD commit, 2,683 bytes, SHA-256 `97c814c9…3325926d`; pure pandas single-file rule, zero out-of-file indicator helpers; no performance figure ships anywhere in the file)
- https://github.com/judder659/Forven (repository home; HEAD verified `e9a6c09` by `git ls-remote` this cycle)
