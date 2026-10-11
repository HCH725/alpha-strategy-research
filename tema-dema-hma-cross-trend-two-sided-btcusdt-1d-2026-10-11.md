---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TEMA-DEMA-HMA cross trend two-sided on BTCUSDT 1d bars
created: 2026-10-11
updated: 2026-10-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2020-10-30
sources:
  - https://github.com/hasnocool/tradingview-pine-scripts
  - https://www.tradingview.com/script/rlhozhjZ-TEMA-DEMA-HMA-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TEMA-DEMA-HMA cross trend two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (verified 2026-10-11):

- Pinned executable artifact (real `strategy()`, Pine v4, `overlay = true`): file `TEMA-DEMA-HMA Strategy.pine` in https://github.com/hasnocool/tradingview-pine-scripts at commit `69969aeaf271b2f7b5a7632a1bde43069a0cbe26` (2024-09-18), local SHA-256 `a4fa67fabd956559654610024750bb11ce4717cada536a58215385bad78cbb45`. Header declaration quoted verbatim: `strategy("TEMA/DEMA/HMA", overlay=true, pyramiding=0, default_qty_type=strategy.percent_of_equity, default_qty_value=100, initial_capital=1000000, commission_type=strategy.commission.percent, commission_value=0.1)`. The file preserves the author's description prose verbatim: "The TEMA/DEMA/HMA strategy is a basic trend follower looking for when the TEMA crosses above the DEMA as a buy signal and the opposite for the sell. The HMA is used as a longer more Dynamic MA to confirm the wider trend to filter out bad trades." The mirror copy carries page chrome (script-name/author header, `Copy code` marker, line numbers) around the intact script text — the code lines below are byte-verified in that file, never reconstructed from memory.
- Canonical TradingView identity corroboration: https://www.tradingview.com/script/rlhozhjZ-TEMA-DEMA-HMA-Strategy/ fetched from this runner with HTTP 200; the `<title>` pins `TEMA/DEMA/HMA Strategy by Tuned_Official — TradingView`, the `Tuned`/`tuned-com` author tokens and the `TEMA/DEMA/HMA` title token repeat in-page, the script flags read `is_public:true`, open-source, MPL-2.0 licence, `created_at:"2020-10-30T19:59:51.290613+00:00"` (adopted as `source_as_of`), and the embedded description text matches the mirror's description word for word. The page's Source-code tab itself was not machine-readable from this runner (bot-wall on the code pane), so every formula line in this record is sourced from the pinned mirror bytes above — disclosed here, not hidden.
- Text census over the script body: 1 `strategy(` / 2 `strategy.entry` (`"Long Entry"`/`strategy.long`, `"Short Entry"`/`strategy.short`) / 0 `strategy.exit` / 0 `strategy.close` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=` / 0 `security(` / 0 `request.*` / explicit `pyramiding=0` (no same-direction adds; an opposite-side entry reverses the open leg) / 0 `process_orders_on_close` (Pine default: per-completed-bar evaluation, next-bar fills) / 0 `volume` / 0 `open` / 0 `high` / 0 `low` / 0 `hlc3` / 0 `heikin` (the body reads `close` only) / 0 `time`/`timenow` / 0 `barstate.islast`. The `commission_*`/`initial_capital`/`default_qty_*` economics are recorded as absent portable economics, never as cost evidence.
- Canonical inputs and recursions pinned verbatim: `Tlength = input(8, minval=1)`; `Dlength = input(43, minval=1)`; `Hlength = input(52, minval=1)`; `Rlength = input(2, minval=1)`; TEMA cascade `ema1 = ema(close, 8)`, `ema2 = ema(ema1, 8)`, `ema3 = ema(ema2, 8)`, `tema = 3 * (ema1 - ema2) + ema3`; DEMA cascade `e1 = ema(close, 43)`, `e2 = ema(e1, 43)`, `dema = 2 * e1 - e2`; HMA `hma = wma(2 * wma(close, Hlength / 2) - wma(close, Hlength), round(sqrt(Hlength)))` with integer `52 / 2 = 26` and `round(sqrt(52)) = round(7.211) = 7`, i.e. `hma = wma(2 * wma(close, 26) - wma(close, 52), 7)` — deterministic, no researcher choice involved. Signal lines pinned verbatim: `up = crossunder(dema, tema) and rising(hma, Rlength)`; `down = crossover(dema, tema) and falling(hma, Rlength)`; `if up` → `strategy.entry("Long Entry", strategy.long)`; `if down` → `strategy.entry("Short Entry", strategy.short)`. `rising(x, len)`/`falling(x, len)` are Pine v4 built-ins (strict `x > x[len]` / `x < x[len]`), not researcher definitions. The computed-but-unread `upc = crossover(dema, tema)` / `downc = crossunder(dema, tema)` carry no order path and are explicitly not adopted as signals.
- Cross-check of prose against code: `crossunder(dema, tema)` fires exactly when TEMA crosses above DEMA — the description's "TEMA crosses above the DEMA as a buy signal" matches the Long leg; `crossover(dema, tema)` is the mirror image for the Short leg. No contradiction between prose and code.

Licence and rights: this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence (MPL-2.0 script, used within its terms).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) market/frame pin `BTCUSDT 1d` (the code names no market and no timeframe; this pin is a pure researcher choice, disclosed here, never presented as source-native); (2) same-bar-close fills (the source ships no execution-timing argument — Pine default evaluates per completed bar and fills on the next bar; no `process_orders_on_close` ships anywhere, quoted verbatim in census); (3) an adopted 60-bar warmup with pre-warmup bars flat by record rule (the HMA(52) window plus the `[Rlength]` lag needs 54 completed closes plus recursion margin — see Required data); (4) house sizing/capital/costs replacing the absent source economics (the shipped percent-of-equity/commission/capital line is recorded as absent portable economics, never as cost evidence; see Execution assumptions). The 8/43/52/2 inputs, the TEMA/DEMA/HMA arithmetic, the close-only inputs, the HMA-regime-gated cross triggers, the atomic reversal, the single-position posture, and the no-stop/no-target/no-cooldown stance are source-native and unmodified.

Pre-write dedup (2026-10-11): working-tree case-insensitive searches for `tema`, `dema`, `tuned`, `rlhozhjZ`, and `TEMA-DEMA-HMA` return zero strategy records using this source, author script, or construction — the only `tema`/`dema`/`tuned` hits anywhere are prose fragments (`re-tuned`, `tune`, `must not improve`) inside falsification/limitation text, never a signal. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closed PR #6 (LazyBear WaveTrend wt1/wt2 cross) is a price-normalized oscillator cross with no moving-average cascade and no regime filter — deliberately not revisited here. Closest pool records are different mechanism classes: `hull-ema-crossover-reversal-btcusdt-1d` crosses contemporaneous HMA(5) against EMA(5) with no third average and no regime gate; `ema-20-50-cross-btcusdt-1h` is a bare dual-EMA cross, long-only; `triple-ema-volstop-tp-long-btcusdt-1d` is a triple-EMA simultaneity gate with vol-stop exits. No pool record evaluates a TEMA-vs-DEMA cross, no pool record reads DEMA anywhere in an order leg, and no pool record uses a Hull average purely as a rising/falling regime filter. Five-axis distinction: mechanism differs (triple-average cross-plus-filter versus single-cross or band systems), signal construction differs (8/43 TEMA/DEMA cross gated by HMA(52) slope state — no pool record shares any of the three legs), trigger differs (regime-gated two-series cross, not a level, band touch, or state latch), data differs (`close` only; no `high`, no `low`, no `open`, no `volume`), and source identity differs (hasnocool `TEMA-DEMA-HMA Strategy.pine` at pinned SHA plus TV `rlhozhjZ` Tuned_Official 2020-10-30).

## Economic mechanism

### Source-reported

Fast-adaptive trend capture with slow-regime confirmation (description prose plus quoted Pine): the TEMA(8) leg reacts to price faster than any single average of comparable smoothness by cancelling triple-EMA lag, while the DEMA(43) leg gives a smoother slow reference — their cross marks the moment short-horizon direction overwhelms the longer-horizon drift. The HMA(52) regime filter then vetoes any cross that disagrees with the wider trend (longs only while the Hull line itself prints higher than 2 bars ago, shorts only while it prints lower), explicitly "to filter out bad trades". There is no stop, no target, no flat state by design after the first signal — the opposite gated cross is the exit. The design bets that a lag-cancelled fast/slow cross, admitted only with the slow regime's permission, whipsaws less than a naked cross while still turning faster than a single slow average.

### Research interpretation

Two-layer cross system, two-sided, always-in-position after the first signal. Unlike single-cross records, the trigger has a bouncer: the HMA slope state decides whether a fresh TEMA/DEMA cross is even eligible, so counter-trend crosses during an established Hull slope are ignored rather than traded — the book simply holds its side until a cross arrives that the regime endorses. Unlike band or latch systems, there is no width, threshold, or sticky equality branch: `crossover`/`crossunder` plus strict `rising`/`falling` are exact one-bar events, so no bar can fire both sides and no priority rule is needed or invented. The price of the always-in posture is the same as every reversal record's: a leg whose opposite gated cross never prints is held indefinitely, and a market that alternates eligible crosses prints repeated full reversals with no flat state to rest in. The bet is on lag-cancellation plus regime permission, not on any momentum extreme, volume print, calendar effect, or second timeframe.

## Signal

Exact rule as pinned (all inputs frozen — any other value is a different, unpinned rule):

- Declarations (derived): single-position state machine over `BTCUSDT 1d` with same-bar-close execution and house sizing/costs (see Execution assumptions). At most one open leg; state ∈ {flat, long, short}; flat exists only before the first signal and under the warmup rule.
- Averages, pinned verbatim at defaults (`Tlength = 8`, `Dlength = 43`, `Hlength = 52`, `Rlength = 2`), with `c(t) = close(t)`: `TEMA(t) = 3·(EMA₈(c) − EMA₈²(c)) + EMA₈³(c)`; `DEMA(t) = 2·EMA₄₃(c) − EMA₄₃²(c)`; `HMA(t) = WMA₇(2·WMA₂₆(c) − WMA₅₂(c))`. Only `close` is read anywhere.
- Regime state (Pine v4 built-ins, evaluated once per completed bar): `risingH(t) = HMA(t) > HMA(t−2)`; `fallingH(t) = HMA(t) < HMA(t−2)`; equality holds the prior regime implicitly (neither branch fires — deterministic, no invented hold variable).
- Entry long: on `crossunder(DEMA, TEMA)` (i.e. TEMA crossing above DEMA) **and** `risingH` on the same bar (from flat: open long; from short: atomic reversal — close short plus open long as a single reversal event, matching Pine's opposite-side `strategy.entry` reversal). Refires while already long are no-ops (`pyramiding=0` ships explicitly in the header). Entry short: mirror on `crossover(DEMA, TEMA)` (TEMA crossing below DEMA) **and** `fallingH`.
- Exits: the opposite eligible cross only (long exits exactly when a short entry fires and vice versa). No stop, no target, no trailing, no time exit, no cooldown — pinned as written (the script ships zero `strategy.exit` legs and names no stop anywhere), explicitly none, not invented. A counter-trend naked cross (regime gate closed) exits nothing and enters nothing — the book holds.
- Direction: two-sided with an explicit pre-first-signal flat state (plus the 60-bar warmup flat by record rule). A long-only or short-only reading would contradict the prescribed Short leg; each is a different, unpinned rule.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (TEMA/DEMA recursions, Hull windowed means, and the 2-bar regime lags). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (derived pin; the body contains no `security(`/`request.*` call, so the derived rule is single-frame by construction).
- Warmup: the binding seed is the HMA(52) windowed mean (52 completed closes) plus the `Rlength = 2` regime lag (first fully-defined `rising`/`falling` needs 54 completed closes); the TEMA(8) triple cascade and DEMA(43) double cascade resolve earlier. The adopted warmup is the first 60 completed `1d` bars flat by record rule (predeclared researcher choice — covers the 54-bar seed plus recursion margin; no traded bar reads a seeded value). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Each bar's close enters the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (derived pin; the code names no market and no timeframe — venue choice, symbol spelling, and frame are disclosed here, never presented as source claims).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar fill (no execution-timing argument ships anywhere — quoted verbatim in census); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity, and the trigger reads only completed closes, so each bar's outcome is a single deterministic event (hold, open, or atomic reversal) under either fill convention.
- Sizing/capital/costs: the source ships no portable economics (the percent-of-equity/commission/capital line is recorded as absent economics, never as zero-cost evidence) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: single-position machine — at most one open leg; same-state bars while positioned are no-ops; the opposite eligible cross reverses in full (one atomic event); re-entry is allowed on the next fresh eligible cross after any close (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (8/43/52/2 inputs, the triple-EMA TEMA cascade, the double-EMA DEMA cascade, the integer-resolved HMA(52) window, the `rising`/`falling` regime gate, and the gated Long/Short entry pair with explicit `pyramiding=0` reversal) plus the trend-follower-with-filter description prose — quoted in Provenance. It ships no portable performance: no table, no figure, no metric — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: the body contains zero `strategy.exit` legs and zero close calls of any kind; the no-stop/no-target/no-time posture is prescribed, explicitly none, never hidden.
2. Regime-gate veto fenced: a naked TEMA/DEMA cross whose HMA slope state disagrees fires no order leg at all — the `and rising`/`and falling` conjunctions are order-gating, quoted verbatim. No positioned bar can be exited by an ineligible cross, and no flat bar can be entered by one.
3. Trigger exclusivity fenced: `crossover` and `crossunder` of the same pair are strictly mutually exclusive on one bar, and each additionally requires its own regime branch — no bar fires both entries, no priority rule needed or invented. HMA equality-to-the-tick closes both regime branches deterministically (hold, not an exit).
4. Reversal completeness fenced: Pine's opposite-side `strategy.entry` closes the open leg and opens the new one; the record's atomic-reversal event mirrors exactly this — no positioned bar swallows an opposite eligible cross, and same-state bars are no-ops under explicit `pyramiding=0` (quoted in census).
5. No future leakage in the stack, stated plainly: at decision bar `t`, the slowest input is closes `t−51…t` (HMA window) plus the `t−2` regime lag — every input is complete at bar `t`'s close. No `security()`, no `request.*`, no negative index, no `barstate.islast`-gated repainting path, no `time` read at all. The recursion seeds resolve before the 60-bar warmup ends.
6. Two-sided posture provably complete: symmetric `"Long Entry"`/`"Short Entry"` legs with a symmetric gated-cross trigger and symmetric reversal exits. No third direction exists.
7. Dead-variable fence, admitted plainly: `upc`/`downc` are computed but read by no order, exit, or plot path in the pinned bytes — display remnants, explicitly not adopted as signals. Adopting them would be a different, unpinned rule.
8. Integer-arithmetic fence: `Hlength / 2` resolves to integer `26` and `round(sqrt(52))` to `7` under Pine v4 semantics — the HMA leg is therefore exactly `wma(2 * wma(close, 26) - wma(close, 52), 7)` with no float-length ambiguity for any downstream re-implementation to guess at.
9. Close-only data fence: the body's alphabet of price reads is exactly `{close}` — venue `high`/`low`/`open`/`volume` definition differences cannot touch any order-gating line. A venue that cannot supply 54 pre-decision daily closes cannot trade the pinned rule.
10. Derivation boundary fenced: the only non-source-native behaviors in this record are the `BTCUSDT 1d` market/frame pin, same-bar-close fills, the adopted 60-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the 8/43/52/2 inputs, the three average constructions, the close-only inputs, the regime-gated crosses, the atomic reversal, the single-position guard, and the risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, or timing of the source passes.
11. Network limitation disclosed: every formula line above was byte-verified in the pinned mirror file at commit `69969aea` (local SHA-256 recorded); the canonical TV page verified live the title, author, open-source/MPL status, publication date, and description identity, while its code pane was unreadable from this runner — the division of evidence is disclosed here, not hidden.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 8/43/52/2 TEMA/DEMA/HMA gated cross / atomic reversal / no-stop-no-target posture / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Regime-gate relevance: dropping the HMA gate (naked TEMA(8)/DEMA(43) cross, same reversals) must not improve net expectancy; fail ⇒ the Hull regime filter adds nothing over the bare cross.
- F2 — Slow-leg relevance: shortening the slow leg to `Dlength = 21` (same TEMA(8), same HMA(52) gate) must not improve net expectancy; fail ⇒ the 43-bar slow reference adds nothing over a faster variant.
- F3 — Lag-cancellation relevance: replacing TEMA(8) with a plain EMA(8) (same DEMA(43), same HMA gate) must not improve net expectancy; fail ⇒ the triple-EMA lag cancellation adds nothing over a single average.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (derived pin; the code names no market at all). The close-only arithmetic ports across perpetual venues without structural change; the rule reads no high/low/open/volume, so venue bar-construction and volume-definition differences cannot touch it. The averages auto-scale in the asset's own price units, so no fixed-pip recalibration is needed across assets — cross-asset behavior differences are still real and unclaimed. The rule is two-sided with no stop leg, so a spot-only deployment expresses the long state and reversal mechanics only to the extent the venue permits shorting — full two-sided expression assumes a futures venue, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no session gating anywhere); decision boundaries are calendar-day bars of the venue feed, disclosed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived market and frame: the code names no market and no timeframe; this record pins `BTCUSDT 1d`. Cross-market and cross-frame behavior differences are real — the adaptation is disclosed, and this record makes no claim about any other market, frame, or the source's native setting.
- Derived fill timing: the source fills next-bar under Pine defaults with no timing argument; this record executes same-bar-close on `1d` BTCUSDT. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- No source economics: the shipped percent-of-equity/commission/capital line is not portable evidence — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- No price stop, no time stop: adverse excursion after entry has no guardrail beyond the opposite eligible cross; a leg whose opposite gated cross never prints is held indefinitely. This is the prescribed posture, disclosed as a principal risk.
- Whipsaw sensitivity: alternating eligible crosses print repeated full reversals with no flat state to rest in, while exact-equality HMA closes hold through arbitrarily large intrabar excursions uncaptured by the close-only trigger. The gated-cross construction is the prescribed design, disclosed, not smoothed.
- Long seed: the HMA window plus regime lag needs 54 completed closes plus recursion margin; the first 60 `1d` bars are flat by record rule, so early-history signals never enter any evaluation.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Immutable GitHub implementation (pinned executable artifact: `TEMA-DEMA-HMA Strategy.pine` at commit `69969aeaf271b2f7b5a7632a1bde43069a0cbe26`, 2024-09-18, local SHA-256 `a4fa67fabd956559654610024750bb11ce4717cada536a58215385bad78cbb45`; TV page chrome preserved around the intact script text): https://github.com/hasnocool/tradingview-pine-scripts
- TradingView canonical script page (Tuned_Official identity, open-source/MPL status, 2020-10-30 publication date, and description text verified live via HTTP-200 page record; code pane not machine-readable from this runner, disclosed above): https://www.tradingview.com/script/rlhozhjZ-TEMA-DEMA-HMA-Strategy/
- Pine strategy semantics (Pine-default fills, `pyramiding`, `rising`/`falling`, `wma`/`ema` semantics): https://www.tradingview.com/pine-script-reference/v5/
