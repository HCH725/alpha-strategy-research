---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven Bollinger S026 EMA200-ADX-gated upper-breakout long-flat on ETHUSDT 1h bars
created: 2026-10-20
updated: 2026-10-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-19
sources:
  - https://github.com/judder659/Forven/blob/265ca464e70191d406a97a91afeccef727ea0a68/forven/strategies/builtin/bollinger.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven Bollinger S026 EMA200-ADX-gated upper-breakout long-flat on ETHUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-bollinger-s00120-rsi-breakout`, `forven-stochastic-k20-recross`, `forven-roc-zero-cross-momentum`, `forven-bb-squeeze-breakout`, `forven-bb-edge-fade-reclaim`, and forty-odd further Forven-sibling records on `main`).
- Pinned commit SHA: `265ca464e70191d406a97a91afeccef727ea0a68` (committed `2026-10-19T21:40:12Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/bollinger.py`.
- GitHub blob SHA at the pinned commit: `6e784974b98ce4e1fe0bde2b47901daf3da5262c`, size 3632 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 3632 bytes, 116 lines, SHA-256 `70c6fedf161339c4d08f59b8b9bc23160ab1c834b7cd38d59ead1089ed006b18`, identical to the GitHub blob (`git hash-object` reproduces `6e784974…3da5262c`) — the entire file was retrieved and inspected. Cross-pin stability: the same bytes were fetched at the previous HEAD `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (byte-identical); the path history shows only three commits, all June ancestors (`d1bfff63` initial public release, `b77ae2a7` execution kernel, `e5bcf06` R3 worker jailing) — the signal logic has not drifted.
- Registration: the file self-registers via `STRATEGY_CLASS = BollingerStrategy`, `TYPE_NAME = "bollinger"` (line 7), and the `STRATEGIES = [("S026-BB-ETH", BollingerStrategy, {"_asset": "ETH"})]` roster pin (lines 114–116). Source-side registry note, disclosed: the sibling `forven/strategies/builtin/bollinger_s00120.py` (`BollingerS00120Strategy`, admitted as `forven-bollinger-s00120-rsi-breakout`) declares the same `TYPE_NAME = "bollinger"` string — this record cites the exact file path, class name, and roster tuple, so the shared label changes no order line here.
- The file's own words (quoted for gate evidence, never extended): module docstring `Bollinger Band Breakout strategy — S026.`; `describe()` returns `Buys when price breaks above the upper Bollinger Band (20-period, 2.0 std dev) while in an uptrend. Sells when price falls back to the middle band.`; `default_params` returns exactly `{ "bb_period": 20, "bb_std": 2.0, "adx_period": 14, "adx_min": 20, "leverage": 3.0 }` (lines 25–29); `compatible_regimes` returns `{"TREND_UP", "RANGE_BOUND"}` (lines 31–33); `parameter_space()` returns period/std/threshold ranges (lines 104–109, a documented search surface only — this record pins the defaults and runs no search).
- Single-source-of-truth structure (verified line by line): `generate_signals()` (lines 43–63) is the vectorized twin computing both legs; `generate_signal()` (lines 65–102) delegates its boolean decision to that twin (`entries, exits = self.generate_signals(df)`, line 87) and only echoes prices/diagnostics around it — no second decision logic exists to diverge. The `atr(df, 14)` call (line 76) feeds only the `atr_14` display field (line 100); it never enters any predicate.
- Indicator helpers pinned at the same commit (both actually read): `forven/scanner.py` exposes `adx(df, period=14)` (Wilder-style construction with `ewm(span=period, adjust=False)` smoothing on TR/DM/DX, `1e-9` zero-guards) and `atr(df, period=14)` (`tr.rolling(period).mean()`); both bodies are byte-identical between the previous pin and the pinned HEAD (only unrelated live-kernel/enrichment code moved elsewhere in that module). `forven/strategies/indicators.py` (35784 bytes, byte-stable across pins) re-exports both through `_FACADE_NAMES` via the lazy `__getattr__` hook, so `from forven.strategies.indicators import adx, atr` resolves to exactly those scanner bodies — one implementation, no twin divergence. The Bollinger/EMA arithmetic itself is in-file rolling/ewm calls, never a helper call.
- Full-file token census (verified by search over the 116 lines this cycle): hardcoded `direction="long"` (exactly one site, line 93 — the sole order-direction token); 0 `direction="short"`; 0 `short` / 0 `sell` / 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` / 0 `target` / 0 `cooldown` / 0 `pyramid` (no short emission, no order arguments, no risk legs anywhere); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 3.0` default); 0 `volume` / 0 `funding` / 0 `request` / 0 `security` / 0 `barstate` / 0 `timeframe` in any order-gating line; direct `df["…"]` reads are exactly `df["close"]` (lines 49/70 — `high`/`low` enter only inside the `scanner.adx` strength gate and the diagnostic ATR echo, never as standalone price reads); 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` (no position-aware state conditions any signal). `open`-series reads: zero anywhere.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the ETH roster asset, the 20/2.0 Bollinger construction, the in-file EMA(200) trend line, the scanner-ADX(14) ≥ 20 strength gate, the strict upper-rail-cross entry, the mid-band-touch exit, the long-only stance, and the no-stop posture — but ships no venue spelling, no timeframe, no fill-timing flag, no warmup floor, and no position-sizing rule inside this file. Researcher-declared adaptations are exactly three: (1) research market/timeframe `ETHUSDT` `1h` (the file names no timeframe and no venue spelling; the roster pins `_asset ETH` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted Forven-sibling records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) house sizing/capital/costs replacing the bare `leverage: 3.0` default (see Execution assumptions; sizing changes no event under the predeclared single-unit rule). No tie-break pin is needed: entry and exit are provably mutually exclusive on every bar (see Signal). The first-210-bars flat rule is the researcher warmup pin (see Required data) — the source ships no guard, and none is pretended. The band arithmetic, the EMA(200) construction, the scanner-ADX construction, the `20` literal, the strict edge/level predicates, the long-only stance, and the no-stop/no-target/no-trailing/no-time-exit/no-cooldown posture are source-verbatim.

Pre-write dedup (2026-10-20): working-tree filename/content search for `builtin/bollinger.py` (exact path), `S026`, `S026-BB-ETH`, and `BollingerStrategy` returns zero strategy records citing this source file — the only pool hit for the bare path is the S00120 record's registry-collision note, which cites a different file. The pool's band-breakout cousins are fenced as different signal constructions in Negative evidence 8. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), #251 (Swift 2-year MA multiplier zone-state long-flat), and #304 (Forven CCI oversold-recross long-flat) — no Bollinger mechanism among them. Not a duplicate, paraphrase, or trivial parameter variant: an upper-band breakout bought only above a 200-bar trend line with trend-strength certification, exiting solely on mid-band touch, long-flat on ETH, is a different signal construction from an RSI-oversold-gated breakout with a satiation exit, a bare ungated breakout, a lower-band fade, or a squeeze release — not a threshold re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: a `Bollinger Band Breakout` for ETH that `Buys when price breaks above the upper Bollinger Band (20-period, 2 std dev) while in an uptrend` and `Sells when price falls back to the middle band`. No behavioural, structural, or risk-premium channel is claimed anywhere in the 116 lines. The file ships no performance number of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Trend-certified breakout, long-only, state-holding. The Bollinger leg buys upside expansion through the 2σ rail; the dual gate admits only breakouts printed above the 200-bar exponential trend line with the directional index certifying trend strength (ADX ≥ 20) — expansion with a certified trend behind it, not chop pokes through the rail. The single structural exit surrenders the unit when price sinks back under the midline. There is no stop leg and no satiation leg: a breakout that keeps climbing is held indefinitely, while a breakout that collapses exits only at the midline touch. Unlike dip-buying band systems there is no lower-band leg — weakness without an upper-rail break never trades; unlike the S00120 sibling there is no oscillator gate and no overbought exit — an exhausted vertical breakout with weak trend certification never enters, and a certified one is never exited early on momentum heat.

## Signal

Exact rule as pinned (any other band length, sigma multiple, EMA length, ADX length, threshold, exit leg, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own; the twin at lines 43–63 is the single source of truth and the scalar path delegates to it:

```text
bb_mid(t)       = SMA20(close)                                                      // rolling mean
sdv(t)          = STDEV20(close)                                                    // pandas rolling sample stdev (ddof=1, pinned semantic)
bb_upper(t)     = bb_mid(t) + 2.0 * sdv(t)
ema200(t)       = EMA200(close)                                                     // ewm span=200, adjust=False, in-file
adx(t)          = scanner.adx(14)                                                   // ewm-span-14 TR/DM/DX construction, pinned body
breakout(t)     = (close[t-1] <= upper[t-1]) and (close[t] > upper[t])               // strict upper-rail cross
trend_ok(t)     = close[t] > ema200[t]
strength_ok(t)  = adx(t) >= 20
entry           = breakout and trend_ok and strength_ok
exit_           = close[t] < bb_mid(t)                                              // structural touch level, not a cross edge
warmup_bars     = 210 (researcher pin; source ships no guard — see Required data)
```

- Trade events: `entry_signal=bool(entry)`, `exit_signal=bool(exit_)`, `direction="long"` (hardcoded literal — no short emission exists anywhere in the file, verified by full-file search). A flat book enters one full unit on an entry bar; a long book exits the full unit on an exit bar. Entries while already long are no-ops under the predeclared single-unit rule (see position rule); exits while flat are deterministic no-ops. The entry is a one-bar cross edge (strict current-bar inequalities throughout) so no level-refire pressure exists by construction — bars lingering above the rail never re-fire; the exit level fires on any qualifying bar while long.
- Mutual-exclusion proof (no tie-break pin required): entry requires `close > bb_upper` where `bb_upper >= bb_mid` always (sigma multiple non-negative, stdev non-negative), while the exit requires `close < bb_mid` — jointly unsatisfiable (at zero stdev the rail equals the midline and the two strict inequalities contradict directly). Every exact-equality boundary fires nothing (strict comparisons throughout: `close == upper` fails the breakout, `close == mid` fails the exit), and pre-warmup bars are flat by record rule. The reviewer is never asked to invent an ordering.
- Direction: long-only. The short side is absent by construction (0 `short`, 0 `sell` — verified by the census above) and recorded as explicitly disabled. Spot-compatible (no naked shorting required).
- Exits and risk (explicit): the mid-band touch is the sole position-ending path. Opposite-signal exit is not applicable (no short leg exists). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence=min(1.0, curr_adx / 40)` on entry bars only (line 94) and the five `indicators` fields (including the ATR echo) are diagnostic — none conditions any order line.
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further entry bars as no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops. Re-entry re-arms on any qualifying breakout bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `close` (bands, EMA200, edges) plus `high`/`low` inside the `scanner.adx` strength gate and the diagnostic-only ATR echo; no `open`-series read, no bar `volume`, no funding/OI/mark-price read, no `request.*`, `security()`, `timeframe*`, `barstate.*`, session/calendar call, second oscillator, or stop/limit order argument anywhere in the order-gating path (verified by the census above returning zero matches). The vectorized twin and the delegating scalar path share one predicate set (no twin divergence possible by construction). The `compatible_regimes == {"TREND_UP", "RANGE_BOUND"}` set and the `parameter_space()` ranges are metadata never read by the signal path (which takes only `df`/`params`); treating either as a gate or running the search surface would be a different, unpinned rule.

## Required data

- Completed `1h` bars of ETHUSDT: `close` for every order-gating comparison (band construction, EMA200, ADX inputs, both predicates); `high`/`low` inside the `scanner.adx` strength gate and the diagnostic-only ATR echo. No `open`-series read, no bar `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request` / 0 `security` anywhere; 0 `timeframe` tokens in the whole file).
- Single decision timeframe `1h` (researcher pin, disclosed — the file names no timeframe). One evaluation per completed bar; all reads reference confirmed bars only (shifted prior-bar comparisons, trailing rolling/ewm windows, `iloc[-1]` on the delegated twin series); fills land on the decision bar's own close (`price=round(curr_close, 4)`, pinned derived rule).
- Warmup: the source ships no length guard (only `.fillna(False)` for leading-NaN legs). The record floor is researcher-declared: the first 210 completed `1h` bars are flat by record rule (≈8.75 days) — covering the 20-bar Bollinger seed, the one-bar edge lookback, the ADX(14) ewm seeding, and the 200-bar EMA seeding with margin. At 211+ bars every window and every prior-bar read is defined; leading-`NaN` legs compare false by construction before that, so no leg can fire early — coded behaviour, disclosed. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: ETHUSDT Binance perpetual under the house overlay (researcher choice — the source roster pins `_asset ETH`; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills (`price=round(curr_close, 4)` — the decision bar's own close), compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same lane primitive the admitted Forven-sibling records use. No maker-touch, queue, or intrabar-path-dependent fill: the only legs are bar-close-evaluated market entry/exit orders. Mutual exclusion (proven above) means no bar ever sequences two fills.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its `leverage: 3.0` default is replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with the single-unit/no-add/noop-on-repeat position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one long position at any time; re-entry after an exit needs only the next qualifying breakout bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The unused short permission requires no margin-short modeling.

## Evidence

### Source-reported

The file ships the full construction (116 lines: module/class docstrings with the entry/exit sentences, `TYPE_NAME`, `default_params` at `20` / `2.0` / `14` / `20` / `3.0`, the vectorized twin with the strict breakout/trend/strength/mid-exit predicates, the delegating scalar path with the hardcoded `direction="long"` and the `round(curr_close, 4)` price echo, the `S026-BB-ETH` roster pin). It ships zero adopted performance numbers of any kind — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `target` ship anywhere — the sole position-closing path is the mid-band touch. The absence of any stop is coded absence, disclosed, not a tunable parameter here.
2. Gate starvation fenced: breakouts that print while `close <= EMA200` or `ADX < 20` never enter — in a range the rail can be broken bar after bar with weak trend certification and the system stays flat throughout; in a rally below the 200-bar line (deep recovery) every breakout is vetoed. Disclosed, not repaired.
3. Touch-exit ride fenced: an entry whose price tops out just above the midline and slides sideways without ever printing `close < bb_mid` is held indefinitely — the exit is a touch level, so a graze closes the full unit while a hover holds it. Disclosed, not repaired.
4. Sample-stdev semantic fenced: the rails use pandas rolling sample standard deviation (`ddof=1`), not the population/biased stdev of Pine `ta.stdev` — a pinned in-file semantic, disclosed; swapping the denominator would be a different, unpinned rule.
5. Scanner-ADX semantic fenced: the strength gate uses the repository's own ewm-span-14 TR/DM/DX construction (`scanner.adx` body quoted in Provenance), not Wilder's RMA ADX — a pinned source semantic, disclosed; swapping the smoother would be a different, unpinned rule.
6. Warmup blindness fenced: the 200-bar EMA seed suppresses every gated leg inside the first ~201 bars even if a textbook certified breakout prints — the adopted 210-bar flat rule converts this into a record rule rather than a silent miss; a shorter warmup would be a different, unpinned rule.
7. Empty-frame behaviour fenced: the delegating scalar path calls `.iloc[-1]` after the twin, so a zero-row frame would raise `IndexError` instead of returning flat — no engine path ever passes an empty frame (backtests feed full history; the record floor starts at bar 1), and every non-empty pre-warmup frame resolves all-False by construction. Disclosed, not repaired; a guard-adding rewrite would be a different file version.
8. Cousin fence (all different signal constructions, none a re-tuning of this rule): the S00120 sibling buys the same 20/2.0 rail cross only while RSI(14) reads oversold (opposite gate philosophy — exhaustion, not certification), carries a second satiation exit, and trades BNB; the FMZ bare-breakout cousin buys ungated 20/1.5σ crosses with a crossunder (edge, not touch) exit on BTC 1d; `bb-edge-fade` sells rail pokes (fade atom); `bb-squeeze` buys volatility releases (squeeze atom, no rail cross); ChartArt joint RSI-50/rail cross, Flawless Victory lower-dip level hold, DMI-gated dip reclaim, and MACD-deadzone explosion share only the band surname. Entry/exit bars differ against every one of them by construction.
9. Source basis fenced: the source names no market beyond `_asset ETH` and no timeframe at all. The ETHUSDT-`1h` choice, same-bar-close fills, single-unit/no-add/noop pin, 210-bar warmup, and house sizing/costs are researcher choices, disclosed; this record is therefore never evidence that any source-market deployment passes.
10. Derivation boundary fenced: the only non-source-native behaviours in this record are the ETHUSDT-`1h` market choice, the same-bar-close fills, the position-state pin, the warmup floor, and house sizing/costs — all predeclared above; the 20/2.0 band construction, the EMA(200) construction, the scanner-ADX(14)/`20` gate, the strict breakout predicate, the mid-touch exit, the long-only stance, and the no-stop/no-target/no-trailing/no-time-exit/no-cooldown posture are source-verbatim.
11. The `20` / `2.0` literals, the in-file EMA(200) basis (not SMA), the scanner-ADX (not Wilder) basis, the `20` strength literal, the upper-breakout edge (not level-hold, not touch), the trend-plus-strength conjunction (not bare breakout, not oscillator gate), the single mid-touch exit (not dual-leg, not reversal), the single-unit long-only stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning any length/multiple/threshold, swapping a smoother or stdev denominator, converting the edge into a level hold, dropping either gate, adding a stop/target/filter/cooldown/gate, adding a short leg, or sizing partially instead of single-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `20` / `2.0` / EMA(200) / scanner-ADX(14) / `20` / strict predicates / single-unit long-only / single mid-touch exit / `1h` ETHUSDT / same-bar-close fills are frozen.

- F1 — Gate-conjunction relevance: replacing the pinned breakout-plus-trend-plus-strength conjunction with the bare upper-band breakout (same mid-touch exit) must not improve net expectancy; fail ⇒ the EMA200/ADX gates add nothing over a plain band breakout.
- F2 — Strength-gate relevance: dropping only the ADX ≥ 20 leg (keeping the EMA200 trend leg) must not improve net expectancy; fail ⇒ strength certification adds nothing over a pure trend line.
- F3 — Rail-width relevance: rebuilding the rails at 1.5σ (same gates, same exit) must not improve net expectancy; fail ⇒ the 2.0σ width adds nothing over the narrower classic rail.

## Crypto portability

Pinned to ETHUSDT Binance perpetual under the house overlay (decision frame `1h` by researcher pin; roster-asset affinity kept — `_asset ETH`; close/high/low arithmetic with no venue-specific read). The OHLC arithmetic ports across perpetual venues without structural change. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behaviour needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Researcher market: the source roster pins `_asset ETH` but no venue spelling — ETHUSDT is a researcher choice; signal timing on other markets would differ by construction.
- Researcher frame: the source names no timeframe — `1h` is a researcher choice; other frames would differ by construction.
- Derived fills: same-bar-close fills are a researcher derivation for this repository family, never the Forven engine's own timing claim — backtest economics under next-open fills would differ by construction.
- No price stop, no time stop, no satiation exit: adverse excursion after entry has no guardrail beyond the mid-band touch, which may arrive many bars later, after deep excursion, or after a long hover; repeated breakout prints while long are no-ops, so averaging down is impossible by construction. This is the coded posture, disclosed as the record's principal risk.
- Gate-starvation holds (Negative evidence 2) and warmup blindness (Negative evidence 6) are pinned costs of the rule, not recovered.
- Unused cost default: the source's bare `leverage: 3.0` carries no fee/funding concept; derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Position-state pin: same-side-add and flat-state exit behaviour is pinned by record rule, disclosed, not independently source-proven beyond the file's stateless per-bar signals.
- The shared `TYPE_NAME = "bollinger"` string with the sibling `bollinger_s00120.py` is a source-side registry label only — this record's identity is the exact file path, class, and roster tuple, and a deployment resolving strategies by that bare label would be a different, unpinned wiring.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; when this strategy is formally selected for execution, the `IMPLEMENTATION_NEEDED` route adds the minimal strategy-specific implementation and returns to the same pipeline without redoing HB_READY.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission. No live-trading authorization is granted or implied.

## Related Wiki records

None — no Wiki Brain record was written for this candidate (Scout contract: no Wiki writes).

## Sources

- https://github.com/judder659/Forven/blob/265ca464e70191d406a97a91afeccef727ea0a68/forven/strategies/builtin/bollinger.py (primary — pinned commit, full file read)
- https://github.com/judder659/Forven (repository identity)
