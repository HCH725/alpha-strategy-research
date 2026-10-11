---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: KAMA efficiency-ratio adaptive trend two-sided on BTCUSDT 1d bars
created: 2026-10-11
updated: 2026-10-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2017-08-25
sources:
  - https://www.tradingview.com/script/KVMbvcHV-Kaufman-Moving-Average-Adaptive-KAMA-Backtest/
  - https://github.com/hasnocool/tradingview-pine-scripts
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# KAMA efficiency-ratio adaptive trend two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (verified 2026-10-11):

- Canonical script page: https://www.tradingview.com/script/KVMbvcHV-Kaufman-Moving-Average-Adaptive-KAMA-Backtest/ (`Kaufman Moving Average Adaptive (KAMA) Backtest — Strategy by HPotter`, published 2017-08-25, adopted as `source_as_of`). Fetched from this runner with HTTP 200; the `<title>` pins `Kaufman Moving Average Adaptive (KAMA) Backtest — Strategy by HPotter — TradingView` and the author token `HPotter` (WIZARD badge) repeats in-page. The page exposes the full open-source Pine block in its Source-code tab — all 41 lines were read verbatim there and are quoted in census below, so no formula line in this record comes from memory or paraphrase.
- Pinned executable artifact (real `strategy()`, Pine v2, `overlay = true`): `strategy(title="Kaufman Moving Average Adaptive (KAMA)", shorttitle="Kaufman Moving Average Adaptive (KAMA)", overlay = true)`. Header prose (verbatim intent, quoted for gate evidence): Kaufman "developed an indicator that adapts to market movement", an "adaptive moving average (AMA), [that] moves very slowly when markets are moving sideways but moves swiftly when the markets also move swiftly, change directions or break out of a trading range." Settings note: "You can change long to short in the Input Settings." Risk note: "Please, use it only for learning or paper trading. Do not for real trading." The script ships no market, no timeframe, and no performance claim of any kind — this record claims no source-reported performance and no reproduced performance.
- Text census over the 41-line Pine block: 1 `strategy(` / 2 `strategy.entry` (`"Long"`/`strategy.long`, `"Short"`/`strategy.short`) / 0 `strategy.exit` / 0 `strategy.close` / 0 `strategy.close_all` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=` / 0 `security(` / 0 `request.*` / 0 `pyramiding` (Pine default: no same-direction adds; a same-direction `strategy.entry` only maintains the open leg, an opposite-side entry reverses it) / 0 `process_orders_on_close` (Pine default: per-completed-bar evaluation, next-bar fills) / 0 `commission_*` / 0 `default_qty_*` (recorded as absent economics, never as cost evidence) / 0 `volume` / 0 `open` / 0 `high` / 0 `low` (the block reads `close` only — `xPrice = close`, `xvnoise`, `nsignal`, and the `close[1]` trigger) / 0 `time`/`timenow` / 0 `barstate.islast`.
- Canonical inputs and constants pinned verbatim: `Length = input(21, minval=1)`; `xPrice = close`; `xvnoise = abs(xPrice − xPrice[1])`; `nfastend = 0.666`; `nslowend = 0.0645`; `reverse = input(false, title="Trade reverse")`. Recursion pinned verbatim: `nsignal = abs(xPrice − xPrice[Length])`; `nnoise = sum(xvnoise, Length)`; `nefratio = iff(nnoise != 0, nsignal / nnoise, 0)`; `nsmooth = pow(nefratio × (nfastend − nslowend) + nslowend, 2)`; `nAMA = nz(nAMA[1]) + nsmooth × (xPrice − nz(nAMA[1]))`. State machine pinned verbatim: `pos = iff(close[1] > nAMA, 1, iff(close[1] < nAMA, −1, nz(pos[1], 0)))`; `possig` equals `pos` at the pinned `reverse = false`; `possig == 1` enters Long, `possig == −1` enters Short.
- Immutable-mirror corroboration (formula cross-check, disclosed as embedding, not the standalone file): https://github.com/hasnocool/tradingview-pine-scripts at commit `69969aeaf271b2f7b5a7632a1bde43069a0cbe26` (2024-09-18) embeds a `KAMA(Length)` function with byte-identical constants (`nfastend = 0.666`, `nslowend = 0.0645`), the identical efficiency-ratio/smoothing recursion, the identical `close[1]`-vs-`nAMA` sticky state, and the identical `Length` default (`LengthKAMA = input(21, minval=2)`) inside file `Combo Backtest 123 Reversal & Kaufman Moving Average Adaptive.pine` (local SHA-256 `959adc9e863a156d7c73d652b23a3506af30453a7aa7ac1978ba80756a42ad4c`). That file's traded signal is a cumulative agreement gate with the 123-Reversal leg plus `close_all` on disagreement — a different, unpinned rule that this record does not adopt; only the embedded KAMA arithmetic corroborates the standalone block above.

Licence and rights: this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) market/frame pin `BTCUSDT 1d` (the code names no market and no timeframe; this pin is a pure researcher choice, disclosed here, never presented as source-native); (2) same-bar-close fills (the source ships no execution-timing argument — Pine default evaluates per completed bar and fills on the next bar; no `process_orders_on_close` ships anywhere, quoted verbatim in census); (3) an adopted 25-bar warmup with pre-warmup bars flat by record rule (the efficiency-ratio window needs 21 completed deltas plus the `[1]`/`[Length]` lags plus recursion margin — see Required data); (4) house sizing/capital/costs replacing the absent source economics (zero cost assumption — recorded as absent, never as zero-cost evidence; see Execution assumptions). The Length-21 efficiency-ratio arithmetic, the 0.666/0.0645 fast/slow constants, the close-only inputs, the prior-close-vs-KAMA sticky state machine, the atomic reversal, the single-position posture, and the no-stop/no-target/no-cooldown stance are source-native and unmodified.

Pre-write dedup (2026-10-11): working-tree case-insensitive searches for `kama`, `nefratio`, `nfastend`, `efficiency-ratio`, `efficiency ratio`, and `Kaufman Moving Average Adaptive` return zero strategy records using this source, author script, indicator, or construction. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. The prior cycle explicitly deferred KAMA to a later round, which this record now takes up. Closest pool records are different mechanism classes: `pivot-point-breakout-kaufman-btcusdt-1d` trades Kaufman swing-high/swing-low pivot breakouts (a price-pattern rule, no moving average anywhere) and is long-only at its pinned defaults; `frama-ma-cross-gated-long-btcusdt-1d` adapts by fractal dimension with an SMA-cross trigger; `vidya-cmo-adaptive-slope-trend-btcusdt-1h` adapts by CMO with a slope trigger; `mcginley-ema-touch-regime-reversal` uses the McGinley dynamic average with touch triggers; `ehma-range-band-breakout` uses exponential-Hull band arithmetic. No pool record computes an efficiency-ratio-scaled smoothing constant with 0.666/0.0645 fast/slow ends and trades prior-close-vs-KAMA state. Five-axis distinction: mechanism differs (volatility-efficiency adaptive average versus swing pivots, fractal dimension, CMO smoothing, McGinley speed, or Hull bands), signal construction differs (no pool record evaluates `close[1]` against a self-adapting average), trigger differs (single-series state transition with sticky hold, not a two-series cross, not a band touch, not a breakout), data differs (`close` only; no `high`, no `low`, no `open`, no `volume`), and source identity differs (TV `KVMbvcHV` HPotter 2017-08-25).

## Economic mechanism

### Source-reported

Noise-adaptive trend averaging with always-in-position reversal discipline (header prose plus quoted Pine, educate-only warning fenced above): the efficiency ratio `|close − close[21]| / Σ|Δclose|₂₁` measures how directed the last 21 bars were — a clean run prints near 1, chop prints near 0. That ratio scales the smoothing constant between the slow end (0.0645, ≈30-period EMA) and the fast end (0.666, ≈2-period EMA), squared. Sideways markets therefore barely move the average (whipsaw suppression by construction); directed markets accelerate it toward price (fast re-peg after breakouts and turns). A prior close printed above the adaptive average means price holds the strong side of its own noise-adjusted trend (trend acceptance → long); below means the weak side (→ short); equality-to-the-tick holds the sticky state. There is no stop, no target, no flat state by design after the first signal — the opposite side of the average is the exit. The design bets that adapting the averaging speed to measured efficiency dominates any fixed-length average, and that the highest-expectancy posture is to always hold the side of the last acceptance.

### Research interpretation

Single-series adaptive-state system, two-sided, always-in-position after the first signal, with a sticky hold on exact equality. Unlike cross systems that trade the moment one line passes another, this rule has one moving part only: the average itself chases price faster in trends and idles in chop, so the signal inherits regime awareness without a second indicator or filter. Unlike band systems, there is no width to tune and no touch to fade — the trigger is a strict inequality against a line that already encodes volatility. The price of the always-in posture is indefinite adverse rides: a leg whose opposite side is never printed on a prior close is held forever, and a market that flickers across the average prints repeated full reversals with no flat state to hide in. The bet is on efficiency-scaled smoothing, not on any momentum extreme, volume print, second series, or calendar effect.

## Signal

Exact rule as pinned (all inputs frozen — any other value is a different, unpinned rule):

- Declarations (derived): single-position state machine over `BTCUSDT 1d` with same-bar-close execution and house sizing/costs (see Execution assumptions). At most one open leg; state ∈ {flat, long, short}; flat exists only before the first signal and under the warmup rule.
- Adaptive average, pinned verbatim at defaults (`Length = 21`, `reverse = false`): with `c(t) = close(t)`: `ER(t) = |c(t) − c(t−21)| / Σᵢ₌₀²⁰|c(t−i) − c(t−i−1)|` (guarded: `0` when the denominator is `0`); `SC(t) = (ER(t) × (0.666 − 0.0645) + 0.0645)²`; `KAMA(t) = KAMA(t−1) + SC(t) × (c(t) − KAMA(t−1))`, seeded `0` via `nz` before warmup (fenced below — no traded bar reads the seed). Only `close` is read anywhere.
- State update (source-native, evaluated once per completed bar): `pos(t) = 1` iff `close(t−1) > KAMA(t)`; `−1` iff `close(t−1) < KAMA(t)`; else `pos(t−1)` (sticky hold on exact equality; both triggers are strictly mutually exclusive — no bar can fire both, no priority rule needed; a 21-bar flat run gives `ER = 0`, `SC = 0.0645²`, no division, no NaN — deterministic, fenced below).
- Entry long: on `pos` transitioning to `1` (from flat: open long; from short: atomic reversal — close short plus open long as a single reversal event, matching Pine's opposite-side `strategy.entry` reversal). Refires of the `pos == 1` state while already long are no-ops (Pine-default no-pyramiding). Entry short: mirror on transition to `−1`.
- Exits: the opposite transition only (long exits exactly when `pos` flips to `−1` and vice versa). No stop, no target, no trailing, no time exit, no cooldown — pinned as written (the script ships zero `strategy.exit` legs and names no stop anywhere), explicitly none, not invented. The standalone block contains no `close_all` anywhere, so there is no flat path after the first signal at all — `possig == 0` is reachable only on the seed bar(s) before any signal, where the book is already flat.
- Direction: two-sided with an explicit pre-first-signal flat state (plus the 25-bar warmup flat by record rule). `reverse = false` preserves both sides; a long-only or short-only reading would contradict the prescribed sell leg, and enabling `reverse` would invert both sides — each is a different, unpinned rule.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (efficiency-ratio window, smoothing recursion, and prior-close-vs-KAMA comparisons). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (derived pin; the block contains no `security(`/`request.*` call, so the derived rule is single-frame by construction).
- Warmup: the binding seed is the 21-bar efficiency-ratio window plus the `[1]`/`[Length]` lags (first fully-defined `ER` needs 22 completed closes; the `nz`-seeded `KAMA` recursion needs margin beyond that). The adopted warmup is the first 25 completed `1d` bars flat by record rule (predeclared researcher choice — covers the 22-bar seed plus margin; the `nz` pre-seed branch never fires on a traded bar). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Each bar's close enters the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (derived pin; the code names no market and no timeframe — venue choice, symbol spelling, and frame are disclosed here, never presented as source claims).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar fill (no execution-timing argument ships anywhere — quoted verbatim in census); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity, and the trigger reads only completed closes, so each bar's outcome is a single deterministic event (hold, open, or atomic reversal) under either fill convention.
- Sizing/capital/costs: the source ships no portable economics (zero commission/quantity assumption — recorded as absent economics, never as zero-cost evidence) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: single-position machine — at most one open leg; same-state bars while positioned are no-ops; the opposite transition reverses in full (one atomic event); re-entry is allowed on the next fresh transition after any close (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (Length-21 efficiency ratio with zero-guard, the 0.666/0.0645 fast/slow ends, the squared smoothing constant, the `nz`-seeded KAMA recursion, the `close[1]`-vs-KAMA sticky state machine with `nz(pos[1], 0)` hold, and the Long/Short entry pair with Pine-default reversal) plus the adaptivity header prose and the long/short settings note — quoted in Provenance. It ships no portable performance: only an educate-only warning, no table, no figure, no metric — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: the block contains zero `strategy.exit` legs and zero close calls of any kind; the no-stop/no-target/no-time posture is prescribed, explicitly none, never hidden.
2. The seed-flat branch fenced as pre-signal-only: `pos == 0` survives only until the first bar whose prior close lands strictly off the average, after which `nz(pos[1], 0)` carries ±1 forever. No positioned bar can reach flat — there is no mid-book flat path to misread as an exit leg.
3. Div-zero fenced in code: `nefratio = iff(nnoise != 0, nsignal / nnoise, 0)` — a 21-bar identical-close run yields `ER = 0` by the guard, `SC = 0.0645²`, and the average coasts on the slow end. No NaN, no order, deterministic.
4. Trigger exclusivity fenced: `close[1] > KAMA` and `close[1] < KAMA` are strictly mutually exclusive — no bar fires both transitions, and the equality case holds state deterministically. No priority rule is needed or invented.
5. Reversal completeness fenced: Pine's opposite-side `strategy.entry` closes the open leg and opens the new one; the record's atomic-reversal event mirrors exactly this — no positioned bar swallows an opposite transition, and same-state bars are no-ops under default no-pyramiding (`pyramiding` unset, quoted in census).
6. No future leakage in the stack, stated plainly: at decision bar `t`, the average reads closes `t−21…t` and the trigger additionally reads `close(t−1)` — every input is complete at bar `t`'s close. No `security()`, no `request.*`, no negative index, no `barstate.islast`-gated repainting path, no `time` read at all. The `nz` seed branch is fenced out of every traded bar by the 25-bar warmup.
7. Two-sided posture provably complete: symmetric `"Long"`/`"Short"` entry legs with a symmetric strict-inequality trigger and symmetric reversal exits at the pinned `reverse = false`; enabling `reverse` inverts both sides and is a different, unpinned rule. No third direction exists.
8. Combo-embedding fence, admitted plainly: the mirror's sibling `Combo Backtest 123 Reversal & Kaufman Moving Average Adaptive.pine` embeds the identical KAMA arithmetic but trades only the agreement of the KAMA leg with the 123-Reversal leg (with `close_all` on disagreement) — a different, unpinned rule this record does not adopt. The BenHampson `KAMA Strategy` sibling adds PSAR/ATR-stop exit legs the source never names — likewise not adopted. This record pins the standalone HPotter block only.
9. Close-only data fence: the block's alphabet of price reads is exactly `{close}` — venue `high`/`low`/`open`/`volume` definition differences cannot touch any order-gating line. A venue that cannot supply 22 pre-decision daily closes cannot trade the pinned rule.
10. Derivation boundary fenced: the only non-source-native behaviors in this record are the `BTCUSDT 1d` market/frame pin, same-bar-close fills, the adopted 25-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the efficiency-ratio arithmetic, the fast/slow constants, the close-only inputs, the sticky state machine, the atomic reversal, the single-position guards, and the risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, or timing of the source passes.
11. Network limitation disclosed: every formula line above was read verbatim from the canonical page's own Source-code tab at HTTP 200 (title/author identity verified); the immutable mirror corroborates the identical KAMA arithmetic as an embedding, never as the standalone file — the distinction is disclosed here, not hidden.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: Length-21 efficiency-ratio KAMA / prior-close-vs-KAMA sticky state with hold / atomic reversal / no-stop-no-target posture / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Adaptivity relevance: replacing the adaptive constant with the fixed slow end (`SC = 0.0645²` every bar, same state machine) must not improve net expectancy; fail ⇒ the efficiency-ratio adaptation adds nothing over a fixed slow average.
- F2 — Window relevance: shortening the efficiency window to `Length = 5` (same ends, same state machine) must not improve net expectancy; fail ⇒ the 21-bar efficiency measurement adds nothing over a fast-window variant.
- F3 — State-vs-cross relevance: trading the KAMA-slope sign instead (`KAMA(t) > KAMA(t−1)` long/flat-state, mirror short, same reversal handling) must not improve net expectancy; fail ⇒ the prior-close-vs-level state adds nothing over a slope-of-average rule.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (derived pin; the code names no market at all). The close-only arithmetic ports across perpetual venues without structural change; the rule reads no high/low/open/volume, so venue bar-construction and volume-definition differences cannot touch it. The efficiency ratio is unit-free and the average auto-scales in the asset's own price units, so no fixed-pip recalibration is needed across assets — cross-asset behavior differences are still real and unclaimed. The rule is two-sided with no stop leg, so a spot-only deployment expresses the long state and reversal mechanics only to the extent the venue permits shorting — full two-sided expression assumes a futures venue, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no session gating anywhere); decision boundaries are calendar-day bars of the venue feed, disclosed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived market and frame: the code names no market and no timeframe; this record pins `BTCUSDT 1d`. Cross-market and cross-frame behavior differences are real — the adaptation is disclosed, and this record makes no claim about any other market, frame, or the source's native setting.
- Derived fill timing: the source fills next-bar under Pine defaults with no timing argument; this record executes same-bar-close on `1d` BTCUSDT. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- No source economics: the source ships no commission, sizing, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- No price stop, no time stop: adverse excursion after entry has no guardrail beyond the opposite side of the average; a leg whose opposite trigger never prints is held indefinitely. This is the prescribed posture, disclosed as a principal risk.
- Whipsaw sensitivity: a prior close flickering across a slow-moving average prints repeated reversal pairs with no flat state to rest in, while exact-equality closes hold through arbitrarily large intrabar excursions uncaptured by the close-only trigger. The state-plus-hold construction is the prescribed design, disclosed, not smoothed.
- Long seed: the efficiency window needs 22 completed closes plus recursion margin; the first 25 `1d` bars are flat by record rule, so early-history signals never enter any evaluation.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- TradingView canonical script page (HPotter KAMA Backtest strategy; stable-URL identity verified via HTTP-200 title/author record; full 41-line Pine v2 block read verbatim from the page's Source-code tab): https://www.tradingview.com/script/KVMbvcHV-Kaufman-Moving-Average-Adaptive-KAMA-Backtest/
- Immutable GitHub corroboration (identical KAMA arithmetic embedded as `KAMA()` in the combo file at pinned SHA `69969aeaf271b2f7b5a7632a1bde43069a0cbe26`, 2024-09-18, local SHA-256 `959adc9e863a156d7c73d652b23a3506af30453a7aa7ac1978ba80756a42ad4c`; combo signal logic explicitly not adopted): https://github.com/hasnocool/tradingview-pine-scripts
- Pine strategy semantics (Pine-default fills, `pyramiding`, `nz`/`iff` semantics): https://www.tradingview.com/pine-script-reference/v5/
