---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven TRIX 15/9 signal-cross zero-gated long-flat on BTCUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/trix.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven TRIX 15/9 signal-cross zero-gated long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, `forven-adl-ema-cross`, `forven-atr-volume-breakout`, `forven-aroon-up-down-cross`, `forven-ema-rsi-pullback-reclaim`, `forven-double-bottom-neckline-break`, `forven-vwap-rolling-cross`, `forven-chaikin-mf-threshold-cross`, `forven-elder-ray-bull-power-cross`, `forven-adx-trend-pulse-reclaim`, and `forven-dema-cross` records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/trix.py`.
- GitHub blob SHA at the pinned commit: `3414aac54c0191ecdba69fba8a52691e3a2c09b0`, size 3479 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 3479 bytes, 116 lines, SHA-256 `0d86d4f3876e7b57ac87c1350ae050b033776a2169073dc087e95199721e3b14`, identical to the GitHub blob (`git hash-object` reproduces `3414aac5…3a2c09b0`) — the entire file was retrieved and inspected.
- Registration: the file self-registers via `STRATEGY_CLASS = TrixStrategy`, `TYPE_NAME = "trix"` (line 7), and the `STRATEGIES = [("PREBUILT-TRIX", TrixStrategy, {"_asset": "BTC"})]` roster pin (line 114).
- The file's own words (quoted for gate evidence, never extended): module docstring `TRIX strategy.`; class docstring `TRIX = 1-bar rate-of-change of a triple-smoothed EMA.` / `Signal line = EMA of TRIX.` / `Entry: TRIX crosses above signal line AND TRIX > 0.` / `Exit: TRIX crosses below signal line.`; `describe()` returns `Enters when TRIX(15) crosses above its 9-bar signal line and TRIX > 0. Exits on TRIX crossing below signal.`; `default_params` returns exactly `{ "trix_period": 15, "signal_period": 9, "leverage": 1.0 }` (lines 32–38); `compatible_regimes` returns `{"TREND_UP", "TREND_DOWN"}` (lines 40–42); `parameter_space()` returns `{ "trix_period": (10, 20, 5), "signal_period": (5, 12, 1) }` (lines 105–109, a documented search surface only — this record pins the defaults and runs no search).
- Full-file token census (verified by search over the 116 lines this cycle): hardcoded `direction="long"` (two sites: the live signal on line 95 and the short-frame guard on line 61 — the sole order-direction token); 0 `short` / 0 `sell` (no short path anywhere); 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` (no order arguments, no risk legs); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 1.0` default); direct `df["…"]` reads are `df["close"]` only (one site, line 54 — the `atr(df, 14)` call on line 74 feeds only the `atr_14` diagnostic, never any entry/exit comparison); 0 `"open"` / 0 `volume` / 0 `funding` / 0 `request` / 0 `security` / 0 `timeframe` / 0 `barstate` in any order-gating line; 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` (no position-aware state conditions any signal); 0 `generate_signals` (the file ships only the scalar `generate_signal` path — no vectorized twin exists to diverge). `confidence` and the four `indicators` fields are diagnostic — zero order-gating comparisons read them.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the triple-EMA TRIX(15) construction, the 9-bar signal line, the zero-gated cross-up entry, the cross-down exit, the long-only stance, the no-stop posture, and its own `min_bars = trix_period*3+signal_period+2` short-frame guard — but ships no venue, no timeframe, no fill-timing flag, and no position-sizing rule inside this file. Researcher-declared adaptations are exactly three: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted inside-bar, williams-ema-reclaim, linreg, zscore, adl, atr-volume, aroon, ema-rsi-pullback, double-bottom, vwap-cross, chaikin-mf, elder-ray, adx-trend-pulse, and dema-cross records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) house sizing/capital/costs replacing the bare `leverage: 1.0` default (see Execution assumptions; sizing changes no event under the predeclared single-unit rule). No tie-break pin is needed: entry and exit are provably mutually exclusive on every bar (see Signal). The source's own `min_bars` guard is adopted verbatim as the warmup floor (see Required data), so no warmup invention is required either. The TRIX arithmetic, the signal pair, the zero gate, the long-only stance, and the no-stop/no-target/no-time-exit posture are source-verbatim.

Pre-write dedup (2026-10-17): working-tree filename/content search for `builtin/trix` / `PREBUILT-TRIX` / `TrixStrategy` / `TYPE_NAME = "trix"` returns zero strategy records — no record cites this source file. Pool cousins fenced as different mechanisms in Negative evidence 8 (`trix-dual-band-trend-two-sided` crosses twin TRIX(7)/TRIX(4) lines behind an SMA13/68 trend-state gate plus a 20-bar band filter, two-sided with reversal, from FMZ 428683; `ppo-signal-cross-reversal-two-sided` crosses a percentage EMA-spread oscillator against its signal, two-sided, different source and different oscillator construction; `forven-dema-cross` crosses two double-smoothed averages with no gate, long-flat, different source file). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: a single TRIX(15) against its own 9-bar signal with a zero gate (triple-EMA rate-of-change, long-flat, from immutable file `builtin/trix.py`) is a different signal construction from a twin-TRIX cross, an EMA-spread cross, or a dual-average cross — not a threshold re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: a `TRIX indicator strategy` where `TRIX = 1-bar rate-of-change of a triple-smoothed EMA`, the `Signal line = EMA of TRIX`, entry on `TRIX crosses above signal line AND TRIX > 0`, exit on `TRIX crosses below signal line`. No behavioural, structural, or risk-premium channel is claimed anywhere in the 116 lines. The file ships no performance number of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Triple-smoothed acceleration timing with a zero-momentum filter, long-only, state-holding. Each of the three chained EMAs damps single-bar spikes, so the one-bar rate-of-change of the stack reads sustained acceleration rather than raw bar noise; crossing that reading against its own 9-bar signal times the turn, while the `TRIX > 0` gate refuses entries whose acceleration has not yet cleared the zero line. The entry buys the exact bar the gated cross prints, and the exit surrenders the unit on the exact bar TRIX falls back below its signal. There is no stop leg and no holding leg: a market that alternates crosses prints repeated full round-trips (whipsaw profile, disclosed), while a cross-up whose reverse cross never prints is held indefinitely. Unlike stop-based systems there is no fixed-distance risk leg — the reverse cross is the sole risk control by construction.

## Signal

Exact rule as pinned (any other period, gate, exit leg, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own; the triple-EMA stack is in-file (lines 64–66), no out-of-file indicator conditions any order:

```text
ema1(t)         = ewm(span=15, adjust=False)(close)                                  // causal, in-file
ema2(t)         = ewm(span=15, adjust=False)(ema1)
ema3(t)         = ewm(span=15, adjust=False)(ema2)
trix(t)         = pct_change(ema3)(t) * 100                                         // 1-bar ROC, percent
signal(t)       = ewm(span=9, adjust=False)(trix)
cross_up        = (prev_trix <= prev_signal) and (curr_trix > curr_signal)
cross_down      = (prev_trix >= prev_signal) and (curr_trix < curr_signal)
entry           = cross_up and (curr_trix > 0)
exit_           = cross_down
min_bars        = trix_period*3+signal_period+2 = 56 (source guard; shorter frames return both-signals-false)
```

- Trade events: `entry_signal=bool(entry)`, `exit_signal=bool(exit_)`, `direction="long"` (hardcoded literal — no short emission exists anywhere in the file, verified by full-file search). A flat book enters one full unit on an entry bar; a long book exits the full unit on an exit bar. Entries while already long are no-ops under the predeclared single-unit rule (see position rule); exits while flat are deterministic no-ops. The entry is a one-bar cross edge (strict current-bar inequality on the pair) plus a level gate, so no level-refire pressure exists by construction; the exit is the mirror edge and fires on any qualifying bar.
- Mutual-exclusion proof (no tie-break pin required): entry requires `curr_trix > curr_signal`; exit requires `curr_trix < curr_signal` — no single bar satisfies both, including the exact-equality boundary (strict comparisons fire nothing on ties: `prev_trix == prev_signal` arms both prior clauses but both current clauses stay false) and short frames (the source guard returns both-signals-false before any average is read). The zero gate only narrows entries further and can never create a co-fire. The reviewer is never asked to invent an ordering.
- Direction: long-only. The short side is absent by construction (0 `short` / 0 `sell` in the file) and recorded as explicitly disabled. Spot-compatible (no naked shorting required).
- Exits and risk (explicit): the signal-cross-down is the sole position-ending path. Opposite-signal exit is not applicable (no short leg exists). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence=min(1.0, abs(curr_trix)*10)` (line 89) and the four `indicators` fields are diagnostic — none conditions any order line.
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further entry bars as no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops. Re-entry re-arms on any qualifying gated cross-up bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-guard bars are flat by record rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `close` with fixed non-negative offsets (trailing EWMs, a one-bar ROC, a one-prior-bar cross read) — no `request.*`, `security()`, `timeframe*`, `barstate.*`, volume, funding/OI/mark-price read, session/calendar call, second oscillator, or stop/limit order argument anywhere in the order-gating path (verified by the census above returning zero matches). The file ships only the scalar `generate_signal` path (no vectorized twin exists to diverge). The `compatible_regimes == {"TREND_UP", "TREND_DOWN"}` set is metadata never read by the signal path (which takes only `df`/`params`); treating the label as a gate would be a different, unpinned rule.

## Required data

- Completed `1h` bars of BTCUSDT: `close` only for every order-gating comparison (the TRIX stack, the signal line, the cross read, and the `price` echo). No `open`-series read, no bar `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. (The `atr(df, 14)` call reads `high`/`low`/`close` only to print the `atr_14` diagnostic — it conditions no order and its removal changes no trade event.)
- Single decision timeframe `1h` (the script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction).
- Warmup: the source ships its own guard — `min_bars = trix_period*3+signal_period+2 = 56` completed bars, shorter frames returning both-signals-false with `price=0.0` — adopted verbatim as the warmup floor, flat by record rule (predeclared: the guard *is* the seeding discipline for the triple-EWM-plus-signal stack; no researcher length is invented). No negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Each bar's close enters the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (the file names no venue; the roster pins `_asset BTC` — the Binance/BTCUSDT pin is a researcher market choice, disclosed, never presented as source-native).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted inside-bar, williams-ema-reclaim, linreg, zscore, adl, atr-volume, aroon, ema-rsi-pullback, double-bottom, vwap-cross, chaikin-mf, elder-ray, adx-trend-pulse, and dema-cross records establish same-bar-close as the pinned-compatible lane primitive for this exact repository family. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity, and entry/exit can never co-fire (proven above), so no intrabar ordering assumption is needed at all.
- Engine path for `1h` (gate 5, stated plainly): `1h` is a Binance-documented USDT-M kline interval; the derived rule needs only completed `1h` candles (`close` for orders, `high`/`low` for the atr diagnostic) on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no volume tape, no funding/OI/mark-price leg. That is the same single-frame completed-bar path as the admitted `1h` siblings from this source family, minus even the volume-column order read the chaikin-mf and atr-volume records carry. Anything beyond that single-frame completed-bar path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: the source ships only a bare `leverage: 1.0` default with no capital, fee, slippage, funding, or margin assumption (quoted verbatim in census; the absences are disclosed, never read as zero cost) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior. Under the predeclared single-unit rule the sizing overlay changes no trade event.
- Concurrency: single-unit long-flat book — at most one open long; the signal cross-down closes the whole unit, and re-entry is allowed on any qualifying gated cross-up bar after any exit (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (in-file triple-EMA stack, 1-bar percent ROC, 9-bar signal EMA, 15/9 defaults, zero-gated cross-up entry, cross-down exit, fixed long-only stance with the literal `"long"` direction token, its own 56-bar short-frame guard, no risk legs) and the `PREBUILT-TRIX` roster pin. It ships no performance number of any kind — this record claims no source-reported performance, and no backtest figure is invented here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` — the sole position-closing path is the coded signal cross-down. The absence is coded (the signal block ends with the two cross comparisons plus the zero gate, and only the diagnostic return follows).
2. Variant menu fenced, stated plainly: the `parameter_space()` surface (`trix_period` 10–20, `signal_period` 5–12) is a documented search grid the code never runs — this record freezes the `15/9` defaults as written; adopting any grid point would be a different, unpinned rule.
3. Edge-trigger fires as written, stated plainly: entry prints only on the cross bar (strict prior/current inequalities) behind the zero gate, not on every bar holding TRIX above its signal — adding a level-hold posture would be a different, unpinned rule.
4. No averaging down, stated plainly: the file is stateless (no position-aware branch exists to implement anything else) — an already-long book treats further entry bars as no-ops under the predeclared single-unit rule.
5. Regime/metadata/passenger quarantine, stated plainly: `confidence`, the four `indicators` fields (`trix`, `signal_line`, `trix_positive`, `atr_14`), and the `compatible_regimes == {"TREND_UP", "TREND_DOWN"}` set are returned inside diagnostic fields or class metadata and read by zero order-gating comparisons — treating any of them (including the regime label) as a gate, filter, or sizing input would be a different, unpinned rule. The `atr(df, 14)` call exists solely to print that diagnostic; deleting it changes no trade event.
6. Short-frame path fenced, stated plainly: frames shorter than 56 bars return both-signals-false with `price=0.0` by source code (lines 58–61) — flat by construction, and the returned zero price is a diagnostic echo, never a fill (frames are always full length on the declared venue).
7. Co-fire impossibility fenced with proof, stated plainly: entry requires `curr_trix > curr_signal`, exit requires `curr_trix < curr_signal` — no bar, including exact-equality boundaries and short frames (both signals false), can satisfy both, and the zero gate only narrows entries further. No tie-break, no ordering assumption, and no reviewer invention is required anywhere in this record.
8. Pool-cousin fence, stated plainly: `trix-dual-band-trend-two-sided-btcusdt-1d-2026-10-09.md` crosses twin TRIX(7) against TRIX(4) behind an SMA13/68 trend-state gate plus a 20-bar SMA band filter, two-sided with atomic reversal, from FMZ 428683; `ppo-signal-cross-reversal-two-sided-btcusdt-1d-2026-10-15.md` crosses a percentage EMA-spread oscillator (not a triple-EMA rate-of-change) against its signal, two-sided, different source; `forven-dema-cross-long-flat-btcusdt-1h-2026-10-17.md` crosses DEMA(12) against DEMA(26) with no gate, long-flat, from a different source file in this same repository. This record crosses a single TRIX(15) — triple-EMA rate-of-change — against its own 9-bar signal behind a zero gate, with a reverse-cross exit, long-flat, on BTCUSDT `1h`, from immutable file `builtin/trix.py` — different input construction × different trigger pair × different gate × different exit/posture × different source file. This record is therefore never evidence for those rules, and those records are never this rule's provenance.
9. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT market pin, the `1h` frame adoption, same-bar-close fills (with live intrabar behavior scoped out), and house sizing/costs — all predeclared above; the source's own 56-bar guard is adopted verbatim, not invented. The TRIX arithmetic, the signal pair, the zero gate, the order stance, and the risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, timing, input set, or the Forven engine's own execution semantics passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: TRIX15/signal9 gated cross pair / long-only / BTCUSDT `1h` / same-bar-close fills are frozen.

- F1 — Zero-gate relevance: dropping the `curr_trix > 0` requirement (bare TRIX×signal cross, same exit) must not reproduce-or-beat net expectancy; fail ⇒ the zero gate adds nothing over the plain cross.
- F2 — Triple-smoothing relevance: replacing the triple-EMA TRIX with a single-EMA(15) one-bar ROC crossed against its own 9-bar signal (same gate, same exit) must not reproduce-or-beat net expectancy; fail ⇒ the triple smoothing adds nothing over a plain ROC cross.
- F3 — Exit-leg relevance: replacing the reverse-cross exit with a TRIX-falling-below-zero level exit must not improve net expectancy; fail ⇒ the edge-triggered exit is dead code wearing a risk-leg label.

## Crypto portability

Pinned to BTCUSDT Binance futures `1h` under the house overlay (market pin is a researcher choice following the file's `_asset BTC` roster pin; the file itself is venue-agnostic). The order-gating rule reads no volume tape, no funding, and no calendar — only `close` — so venue volume-definition differences cannot move any print; stated plainly as a portability strength with its boundary: cross-venue porting without re-verification would still be a different, unpinned claim, disclosed. The rule is long-only with no stop leg, so a spot-only deployment expresses it fully, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating and no `open`-series read anywhere), so session-gap behavior needs no approximation — the triple-EWM stack simply spans the continuous tape. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the file returns the decision bar's own close but ships no explicit fill-timing flag; this record evaluates completed bars only and executes same-bar-close on BTCUSDT `1h`. Any live intrabar behavior is out of scope.
- Derived market pin: the file names no venue and no timeframe (roster pins `_asset BTC` only) — BTCUSDT `1h` is a researcher market/frame choice for the house universe, never a source claim.
- Source economics are leverage-only: beyond the bare `leverage: 1.0` default the source ships no capital sizing, no fee, no slippage, no funding, and no margin assumption — derived evaluation must carry the full house cost load (fees plus historical funding; no hypothetical zero funding claimed), and this record reports no net performance of its own.
- No price stop, no time stop: adverse excursion after placement has no guardrail beyond the signal cross-down; a market that spikes TRIX through its signal above zero on one acceleration print and then fades hands the unit straight back on the next bar by construction, and a cross-up whose reverse cross never prints is simply held (opportunity profile, disclosed). This is the coded posture, disclosed as the record's principal risk.
- Seed bars: the triple 15-bar EWM stack plus the 9-bar signal EWM and the one-prior-bar cross read dominate early bars; the first 56 `1h` bars are flat by record rule (source guard adopted verbatim), so early-history signals never enter any evaluation. Substituting a seeded/warm-started average would move every early print and is a different, unpinned rule.
- Zero-gate whipsaw: the gate refuses sub-zero crosses, but a TRIX that oscillates across its signal while hovering just above zero can still print repeated entry-then-exit round trips by construction — disclosed, never hand-waved.
- No co-fire corner exists: see Negative evidence 7 — entry and exit are mutually exclusive by construction on every bar, so no tie-break pin was adopted.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record; the six-gate claim is pinned-engine expressibility of the declared rule, never a profitability, parity, or trading authorization.

## Adoption boundary

Research-only, not approved. No live, Paper, or Testnet authorization follows from this record. Any downstream standardized overlay (house DCA/capital/leverage), Qlib screening, or Hummingbot re-validation is a separate, explicitly authorized step outside this record.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/trix.py (primary source — executable Python strategy, 116 lines, fetched live 2026-10-17 at pinned HEAD commit, 3,479 bytes, blob `3414aac5…3a2c09b0`, SHA-256 `0d86d4f3…1e3b14`; in-file triple-EMA TRIX plus signal-line rule, atr helper feeds the `atr_14` diagnostic only; no performance figure ships anywhere in the file)
- https://github.com/judder659/Forven (repository home; HEAD verified `e9a6c09` by `git ls-remote` this cycle)
