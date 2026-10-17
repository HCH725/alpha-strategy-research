---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven Bollinger S00120 RSI-gated upper-breakout long-flat on BNBUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/bollinger_s00120.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven Bollinger S00120 RSI-gated upper-breakout long-flat on BNBUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, `forven-adl-ema-cross`, `forven-atr-volume-breakout`, `forven-aroon-up-down-cross`, `forven-ema-rsi-pullback-reclaim`, `forven-double-bottom-neckline-break`, `forven-vwap-rolling-cross`, `forven-chaikin-mf-threshold-cross`, `forven-elder-ray-bull-power-cross`, `forven-adx-trend-pulse-reclaim`, `forven-dema-cross`, `forven-trix-signal-cross-zero-gate`, and `forven-ultimate-oscillator-cross-gated` records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/bollinger_s00120.py`.
- GitHub blob SHA at the pinned commit: `26075adbfc9e4cbf58f9ddffc14fc38e91238e84`, size 5104 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 5104 bytes, 151 lines, SHA-256 `f056bbe95b6f03ffbd0159483250bfd4349d39f46891b859109f03b8c64e9f5d`, identical to the GitHub blob (`git hash-object` reproduces `26075adb…91238e84`) — the entire file was retrieved and inspected.
- Registration: the file self-registers via `STRATEGY_CLASS = BollingerS00120Strategy`, `TYPE_NAME = "bollinger"` (line 12), and the `STRATEGIES = [("S00120-BNB-BOLLINGER", BollingerS00120Strategy, {"_asset": "BNB"})]` roster pin (lines 149–151). Source-side registry note, disclosed: the sibling `forven/strategies/builtin/bollinger.py` (`BollingerStrategy`) declares the same `TYPE_NAME = "bollinger"` string — this record cites the exact file path, class name, and roster tuple, so the shared label changes no order line here.
- The file's own words (quoted for gate evidence, never extended): module docstring `Bollinger Band Breakout with RSI Filter — S00120.` / `Strategy: BNB-BOLLINGER-S00120` / `Entry: Price breaks above upper Bollinger Band (20-period, 2 std) AND RSI < rsi_entry_long (oversold)` / `Exit: Price falls below middle Bollinger Band OR RSI > rsi_entry_short (overbought)`; `describe()` returns `BNB S00120: Buys when price breaks above the upper Bollinger Band (20-period, 2 std dev) while RSI < 30 (oversold at breakout). Exits when price falls below middle band or RSI > 70.`; `default_params` returns exactly `{ "bb_period": 20, "bb_std": 2.0, "rsi_entry_long": 30, "rsi_entry_short": 70, "rsi_period": 14, "leverage": 3.0 }` (lines 31–39); `compatible_regimes` returns `{"TREND_UP", "RANGE_BOUND", "VOLATILE"}` (lines 41–43); `parameter_space()` returns period/std/threshold ranges (lines 137–144, a documented search surface only — this record pins the defaults and runs no search).
- Single-source-of-truth structure (verified line by line): `generate_signals()` (lines 54–88) is the vectorized twin computing both legs; `generate_signal()` (lines 90–135) delegates its boolean decision to that twin (`entries, exits = self.generate_signals(df)`, line 112) and only echoes prices/diagnostics around it — no second decision logic exists to diverge. The `atr(df, 14)` call (line 109) feeds only the `atr_14` display field (line 133); it never enters any predicate.
- Indicator helpers pinned at the same commit (both actually read): `forven/scanner.py` blob `9a1d77b90bf214c03aa230a5f46775aab94748bd` (464565 bytes) exposes `rsi(series, period=14)` (line 1914: Wilder RMA RSI via `ewm(alpha=1/n, adjust=False, min_periods=n)`, documented in-file as matching `indicators._rsi` so scanner strategies fire on the same bars as the backtest) and `atr(df, period=14)` (line 1946: `tr.rolling(period).mean()`); `forven/strategies/indicators.py` blob `fdda8b77429e133372482e25cdff8ea31bd59b2a` (35784 bytes) re-exports both through `_FACADE_NAMES` (line 864) and documents the identical Wilder construction in `_rsi` (lines 161–169). The Bollinger arithmetic itself is in-file rolling means/standard-deviations, never a helper call.
- Full-file token census (verified by search over the 151 lines this cycle): hardcoded `direction="long"` (exactly one site, line 126 — the sole order-direction token); 0 `direction="short"`; the `short` substring occurs at exactly 7 sites and every one is the `rsi_entry_short` exit-threshold parameter name (6 sites) or the prose `short threshold` (line 61) — no short emission exists anywhere; 0 `sell` / 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` (no order arguments, no risk legs); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 3.0` default); 0 `volume` / 0 `funding` / 0 `request` / 0 `security` / 0 `barstate` / 0 `timeframe` in any order-gating line; direct `df["…"]` reads are exactly `df["close"]` (two sites, lines 71/97 — `high`/`low` enter only inside the diagnostic ATR helper, never a predicate); 0 `ema` / 0 `ewm` / 0 `crossover` / 0 `crossunder` (both edges are direct strict-inequality comparisons, never an ambiguous cross builtin); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` (no position-aware state conditions any signal). `open`-series reads: zero anywhere.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the BNB roster asset, the 20/2.0 Bollinger construction, the RSI(14) Wilder construction, the 30/70 threshold pair, the upper-breakout-gated-by-oversold entry (with the RSI-reversal alternative), the mid-band-or-overbought dual exit, the long-only stance, and the no-stop posture — but ships no venue spelling, no timeframe, no fill-timing flag, no warmup floor, and no position-sizing rule inside this file. Researcher-declared adaptations are exactly three: (1) research market/timeframe `BNBUSDT` `1h` (the file names no timeframe and no venue spelling; the roster pins `_asset BNB` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted inside-bar, williams-ema-reclaim, linreg, zscore, adl, atr-volume, aroon, ema-rsi-pullback, double-bottom, vwap-cross, chaikin-mf, elder-ray, adx-trend-pulse, dema-cross, trix-signal-cross, and ultimate-oscillator records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) house sizing/capital/costs replacing the bare `leverage: 3.0` default (see Execution assumptions; sizing changes no event under the predeclared single-unit rule). No tie-break pin is needed: entry and exit are provably mutually exclusive on every bar (see Signal). The first-22-bars flat rule is the researcher warmup pin (see Required data) — the source ships no guard, and none is pretended. The band arithmetic, the RSI construction, the threshold pair, the long-only stance, and the no-stop/no-target/no-time-exit posture are source-verbatim.

Pre-write dedup (2026-10-17): working-tree filename/content search for `bollinger_s00120` / `S00120` / `S00120-BNB-BOLLINGER` / `BollingerS00120Strategy` returns zero strategy records — no record cites this source file. The pool's band-oscillator cousins are fenced as different signal constructions in Negative evidence 8 (ChartArt RSI(6)-50 joint-cross on 200-bar rails two-sided 1d; Flawless Victory v1 BB20-1σ lower-dip level long with upper-and-RSI exit on BTC; plain upper-breakout-midline-exit with no oscillator; DMI-gated dip reclaim; MACD deadzone explosion). No closed `research/*` PR ever carried this source file (closed-state search over the last 40 PRs shows only Forven TRIX/DEMA/ADX/Elder-Ray/Chaikin/VWAP/double-pattern/EMA-RSI/Aroon/ATR-volume/ADL/zscore/linreg/Williams/inside-bar siblings, WorldQuant alphas, and Alorse records — no S00120). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: an upper-band breakout bought only while RSI(14) reads oversold, with a mid-band-or-overbought dual exit, long-flat on BNB, is a different signal construction from a dip bought below the lower band, a joint RSI-50/band-rail cross, or a bare band breakout — not a threshold re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: a `Bollinger Band Breakout with RSI Filter` for BNB that `Buys when price breaks above the upper Bollinger Band (20-period, 2 std dev) while RSI < 30 (oversold at breakout)` and `Exits when price falls below middle band or RSI > 70`. No behavioural, structural, or risk-premium channel is claimed anywhere in the 151 lines. The file ships no performance number of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Contrarian-gated breakout, long-only, state-holding. The Bollinger leg buys upside expansion through the 2σ rail; the RSI gate admits only breakouts the momentum oscillator calls oversold — expansion the crowd has not yet chased, plus the reversal-alternative bar where RSI just slipped back under 30 while price breaks up (exhaustion-slip entry, not momentum confirmation). The dual exit surrenders the unit either on structural failure (close back under the midline) or on momentum satiation (RSI above 70), whichever prints first. There is no stop leg: a breakout that keeps climbing with RSI pinned under 70 is held indefinitely, while a breakout that collapses without ever printing RSI>70 exits only at the midline. Unlike dip-buying band systems there is no lower-band leg — weakness without an upper-rail break never trades.

## Signal

Exact rule as pinned (any other band length, sigma multiple, RSI length, threshold, exit leg, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own; the twin at lines 54–88 is the single source of truth and the scalar path delegates to it:

```text
bb_mid(t)       = SMA20(close)                                                      // rolling mean
sdv(t)          = STDEV20(close)                                                    // pandas rolling sample stdev (ddof=1, pinned semantic)
bb_upper(t)     = bb_mid(t) + 2.0 * sdv(t)
rsi(t)          = Wilder-RMA RSI(14) on close (scanner.rsi; ewm alpha=1/14, min_periods=14)
breakout(t)     = (close[t-1] <= upper[t-1]) and (close[t] > upper[t])               // strict upper-rail cross
oversold(t)     = rsi(t) < 30
reversal(t)     = (rsi[t-1] >= 30) and (rsi(t) < 30)                                 // slip-back-under alternative
entry           = breakout and (oversold or reversal)
exit_           = (close < bb_mid) or (rsi > 70)                                    // structural OR satiation exit
warmup_bars     = 22 (researcher pin; source ships no guard — see Required data)
```

- Trade events: `entry_signal=bool(entry)`, `exit_signal=bool(exit_)`, `direction="long"` (hardcoded literal — no short emission exists anywhere in the file, verified by full-file search). A flat book enters one full unit on an entry bar; a long book exits the full unit on an exit bar. Entries while already long are no-ops under the predeclared single-unit rule (see position rule); exits while flat are deterministic no-ops. The entry is a one-bar cross edge (strict current-bar inequalities throughout) so no level-refire pressure exists by construction — bars lingering above the rail never re-fire; either exit disjunct fires on any qualifying bar.
- Mutual-exclusion proof (no tie-break pin required): entry requires `close > bb_upper` where `bb_upper >= bb_mid` always (sigma multiple non-negative, stdev non-negative), while the structural exit requires `close < bb_mid` — jointly unsatisfiable (at zero stdev the rail equals the midline and the two strict inequalities contradict directly); entry requires `rsi < 30` (both alternatives), while the satiation exit requires `rsi > 70` — jointly unsatisfiable. Every exact-equality boundary fires nothing (strict comparisons throughout: `close == upper` fails the breakout, `close == mid` fails the structural exit, `rsi == 30` fails both entry alternatives, `rsi == 70` fails the satiation exit), and pre-warmup bars are flat by record rule. The reviewer is never asked to invent an ordering.
- Direction: long-only. The short side is absent by construction (0 `direction="short"`, 0 `sell` — the 7 `short` substrings are the `rsi_entry_short` exit-threshold name and one prose `short threshold`, never a side) and recorded as explicitly disabled. Spot-compatible (no naked shorting required).
- Exits and risk (explicit): the mid-band-or-overbought pair is the sole position-ending path. Opposite-signal exit is not applicable (no short leg exists). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence=min(1.0, rsi/100)` on entry bars only (line 127) and the five `indicators` fields (including the ATR echo) are diagnostic — none conditions any order line.
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further entry bars as no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops. Re-entry re-arms on any qualifying breakout bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `close` (Bollinger, RSI, edges) plus `high`/`low` inside the diagnostic-only ATR helper (which feeds no predicate); no `open`-series read, no bar `volume`, no funding/OI/mark-price read, no `request.*`, `security()`, `timeframe*`, `barstate.*`, session/calendar call, second oscillator, or stop/limit order argument anywhere in the order-gating path (verified by the census above returning zero matches). The vectorized twin and the delegating scalar path share one predicate set (no twin divergence possible by construction). The `compatible_regimes == {"TREND_UP", "RANGE_BOUND", "VOLATILE"}` set is metadata never read by the signal path (which takes only `df`/`params`); treating the label as a gate would be a different, unpinned rule.

## Required data

- Completed `1h` bars of BNBUSDT: `close` for every order-gating comparison (band construction, Wilder RSI, both edges); `high`/`low` inside the diagnostic-only ATR echo. No `open`-series read, no bar `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request` / 0 `security` anywhere; 0 `timeframe` tokens in the whole file).
- Single decision timeframe `1h` (researcher pin, disclosed — the file names no timeframe). One evaluation per completed bar; all reads reference confirmed bars only (shifted prior-bar comparisons, trailing rolling windows, `iloc[-1]` on the delegated twin series); fills land on the decision bar's own close (`price=round(curr_close, 4)`, pinned derived rule).
- Warmup: the source ships no length guard (only `len(df) < 2` for the directional-series plumbing and `.fillna(False)` for leading-NaN legs). The record floor is researcher-declared: the first 22 completed `1h` bars are flat by record rule — covering the 20-bar Bollinger seed, the one-bar edge lookback, and the RSI(14) RMA seeding with margin. At 22+ bars every window and every prior-bar read is defined; leading-`NaN` legs compare false by construction before that, so no leg can fire early — coded behaviour, disclosed. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BNBUSDT Binance perpetual under the house overlay (researcher choice — the source roster pins `_asset BNB`; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills (`price=round(curr_close, 4)` — the decision bar's own close), compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same lane primitive the sixteen admitted Forven-sibling records use. No maker-touch, queue, or intrabar-path-dependent fill: the only legs are bar-close-evaluated market entry/exit orders. Mutual exclusion (proven above) means no bar ever sequences two fills.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its `leverage: 3.0` default is replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with the single-unit/no-add/noop-on-repeat position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one long position at any time; re-entry after an exit needs only the next qualifying breakout bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The unused short permission requires no margin-short modeling.

## Evidence

### Source-reported

The file ships the full construction (151 lines: module/class docstrings with the entry/exit sentences, `TYPE_NAME`, `default_params` at `20` / `2.0` / `30` / `70` / `14` / `3.0`, the vectorized twin with the strict breakout/oversold/reversal/dual-exit predicates, the delegating scalar path with the hardcoded `direction="long"` and the `round(curr_close, 4)` price echo, the `S00120-BNB-BOLLINGER` roster pin). It ships zero adopted performance numbers of any kind — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` ship anywhere — the sole position-closing path is the mid-band-or-overbought pair. The absence of any stop is coded absence, disclosed, not a tunable parameter here.
2. Oversold-gate starvation fenced: breakouts that print while RSI reads 30+ never enter — in a sustained rally the rail can be broken bar after bar with RSI pinned high and the system stays flat throughout. The gate admits only breakouts the oscillator calls exhausted. Disclosed, not repaired.
3. Satiation-never-reached hold fenced: a breakout entry whose RSI tops out at, say, 65 and slides back without ever printing `> 70` exits only when price sinks under the midline — the full round-trip is ridden. The midline is the sole structural guardrail. Disclosed, not repaired.
4. Sample-stdev semantic fenced: the rails use pandas rolling sample standard deviation (`ddof=1`), not the population/biased stdev of Pine `ta.stdev` — a pinned in-file semantic, disclosed; swapping the denominator would be a different, unpinned rule.
5. Warmup blindness fenced: the 20-bar seed suppresses every leg inside the first ~21 bars even if a textbook breakout prints — the adopted 22-bar flat rule converts this into a record rule rather than a silent miss; a shorter warmup would be a different, unpinned rule.
6. Empty-frame behaviour fenced: the delegating scalar path calls `.iloc[-1]` after the twin, so a zero-row frame would raise `IndexError` instead of returning flat — no engine path ever passes an empty frame (backtests feed full history; the record floor starts at bar 1), and every non-empty pre-warmup frame resolves all-False by construction. Disclosed, not repaired; a guard-adding rewrite would be a different file version.
7. Source basis fenced: the source names no market beyond `_asset BNB` and no timeframe at all. The BNBUSDT-`1h` choice, same-bar-close fills, single-unit/no-add/noop pin, 22-bar warmup, and house sizing/costs are researcher choices, disclosed; this record is therefore never evidence that any source-market deployment passes.
8. Derivation boundary fenced: the only non-source-native behaviours in this record are the BNBUSDT-`1h` market choice, the same-bar-close fills, the position-state pin, the warmup floor, and house sizing/costs — all predeclared above; the 20/2.0 band construction, the Wilder RSI(14) construction, the `30`/`70` literals, the strict breakout/oversold/reversal/dual-exit predicates, the long-only stance, and the no-stop/no-target/no-trailing/no-time-exit/no-cooldown posture are source-verbatim.
9. The `20` / `2.0` literals, the Wilder-RMA (not SMA) RSI basis, the `30` / `70` literals, the upper-breakout edge (not level-hold, not touch), the oversold-or-reversal conjunction (not bare breakout), the mid-band-or-overbought dual exit (not single-leg, not reversal), the single-unit long-only stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning any length/multiple/threshold, swapping a smoother or stdev denominator, converting the edges into level holds, dropping the RSI gate, adding a stop/target/filter/cooldown/gate, adding a short leg, or sizing partially instead of single-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `20` / `2.0` / RSI(14) Wilder / `30` / `70` / strict predicates / single-unit long-only / dual exit / `1h` BNBUSDT / same-bar-close fills are frozen.

- F1 — RSI-gate relevance: replacing the pinned breakout-plus-oversold conjunction with the bare upper-band breakout (same dual exit) must not improve net expectancy; fail ⇒ the oversold gate adds nothing over a plain band breakout.
- F2 — Reversal-alternative relevance: dropping only the RSI-slip-back-under alternative (entry on strict oversold only) must not improve net expectancy; fail ⇒ the exhaustion-slip leg adds nothing over the strict level gate.
- F3 — Dual-exit relevance: replacing the mid-band-or-overbought pair with either single leg alone must not improve net expectancy; fail ⇒ the dropped disjunct carries no independent risk control.

## Crypto portability

Pinned to BNBUSDT Binance perpetual under the house overlay (decision frame `1h` by researcher pin; roster-asset affinity kept — `_asset BNB`; close/high/low arithmetic with no venue-specific read). The OHLC arithmetic ports across perpetual venues without structural change. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behaviour needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Researcher market: the source roster pins `_asset BNB` but no venue spelling — BNBUSDT is a researcher choice; signal timing on other markets would differ by construction.
- Researcher frame: the source names no timeframe — `1h` is a researcher choice; other frames would differ by construction.
- Derived fills: same-bar-close fills are a researcher derivation for this repository family, never the Forven engine's own timing claim — backtest economics under next-open fills would differ by construction.
- No price stop, no time stop: adverse excursion after entry has no guardrail beyond the mid-band-or-overbought pair, which may arrive many bars later, after deep excursion, or (satiation leg) never; repeated breakout prints while long are no-ops, so averaging down is impossible by construction. This is the coded posture, disclosed as the record's principal risk.
- Satiation-never-reached holds (Negative evidence 3) and warmup blindness (Negative evidence 5) are pinned costs of the rule, not recovered.
- Unused cost default: the source's bare `leverage: 3.0` carries no fee/funding concept; derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Position-state pin: same-side-add and flat-state exit behaviour is pinned by record rule, disclosed, not independently source-proven beyond the file's stateless per-bar signals.
- The shared `TYPE_NAME = "bollinger"` string with the sibling `bollinger.py` is a source-side registry label only — this record's identity is the exact file path, class, and roster tuple, and a deployment resolving strategies by that bare label would be a different, unpinned wiring.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; when this strategy is formally selected for execution, the `IMPLEMENTATION_NEEDED` route adds the minimal strategy-specific implementation and returns to the same pipeline without redoing HB_READY.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission. No live-trading authorization is granted or implied.

## Related Wiki records

None — no Wiki Brain record was written for this candidate (Scout contract: no Wiki writes).

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/bollinger_s00120.py (primary — pinned commit, full file read)
- https://github.com/judder659/Forven (repository identity)
