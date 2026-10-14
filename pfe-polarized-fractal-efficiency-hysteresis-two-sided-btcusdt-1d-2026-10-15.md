---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: PFE polarized-fractal-efficiency hysteresis-band reversal two-sided on BTCUSDT 1d bars
created: 2026-10-15
updated: 2026-10-15
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2017-09-29
sources:
  - https://www.tradingview.com/script/dTukyGTy-PFE-Polarized-Fractal-Efficiency-Backtest/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# PFE polarized-fractal-efficiency hysteresis-band reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (verified 2026-10-15):

- Canonical script page: https://www.tradingview.com/script/dTukyGTy-PFE-Polarized-Fractal-Efficiency-Backtest/ (`PFE (Polarized Fractal Efficiency) Backtest — Strategy by HPotter`, published Sep 29, 2017, adopted as `source_as_of`). Read in a real browser at HTTP 200; the `<title>` pins `PFE (Polarized Fractal Efficiency) Backtest — Strategy by HPotter — TradingView`, the `OPEN-SOURCE SCRIPT` badge and the `HPotter` (WIZARD badge) author token repeat in-page. The page exposes the full open-source Pine block in its Source code tab — all 36 lines were read verbatim there and are quoted in census below, so no formula line in this record comes from memory or paraphrase.
- Pinned executable artifact (real `strategy()`, Pine v2): `strategy(title="PFE (Polarized Fractal Efficiency)", shorttitle="PFE (Polarized Fractal Efficiency)")`. Header prose (verbatim intent, quoted for gate evidence): the Polarized Fractal Efficiency indicator "measures the efficiency of price movements by drawing on concepts from fractal geometry and chaos theory. The more linear and efficient the price movement, the shorter the distance the prices must travel between two points and thus the more efficient the price movement." Settings note: "You can change long to short in the Input Settings." Risk note: "For purpose educate only". The script ships no market, no timeframe, and no performance claim of any kind — this record claims no source-reported performance and no reproduced performance.
- Text census over the 36-line Pine block: 1 `strategy(` / 2 `strategy.entry` (`"Long"`/`strategy.long`, `"Short"`/`strategy.short`) / 0 `strategy.exit` / 0 `strategy.close` / 0 `strategy.close_all` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=` / 0 `security(` / 0 `request.*` / 0 `pyramiding` (Pine default: no same-direction adds; a same-direction `strategy.entry` only maintains the open leg, an opposite-side entry reverses it) / 0 `process_orders_on_close` (Pine default: per-completed-bar evaluation, next-bar fills) / 0 `calc_on_every_tick` (Pine default: `false`) / 0 `commission_*` / 0 `default_qty_*` (recorded as absent economics, never as cost evidence) / 0 `volume` / 0 `open` / 0 `high` / 0 `low` (the block reads `close` only — `close[Length]`, `close[1]`, and current `close`) / 0 `time`/`timenow` / 0 `barstate.islast`. `hline`/`barcolor`/`plot` lines are visualization only and gate no order.
- Canonical inputs and constants pinned verbatim: `Length = input(9, minval=1)`; `LengthEMA = input(5, minval=1)`; `BuyBand = input(50, step = 0.1)`; `SellBand = input(-50, step = 0.1)`; `reverse = input(false, title="Trade reverse")`. Indicator pinned verbatim: `PFE = sqrt(pow(close - close[Length], 2) + 100)`; `C2C = sum(sqrt(pow((close - close[1]), 2) + 1), Length)`; `xFracEff = iff(close - close[Length] > 0, round((PFE / C2C) * 100), round(-(PFE / C2C) * 100))`; `xEMA = ema(xFracEff, LengthEMA)`. State machine pinned verbatim: `pos = iff(xEMA < SellBand, -1, iff(xEMA > BuyBand, 1, nz(pos[1], 0)))`; `possig` equals `pos` at the pinned `reverse = false`; `possig == 1` enters Long, `possig == -1` enters Short.

Licence and rights: this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) market/frame pin `BTCUSDT 1d` (the code names no market and no timeframe; this pin is a pure researcher choice, disclosed here, never presented as source-native); (2) same-bar-close fills (the source ships no execution-timing argument — Pine default evaluates per completed bar and fills on the next bar; no `process_orders_on_close` ships anywhere, quoted verbatim in census); (3) an adopted 15-bar warmup with pre-warmup bars flat by record rule (the polarized-efficiency window needs 10 completed closes plus the EMA recursion and `pos[1]` latch margin — see Required data); (4) house sizing/capital/costs replacing the absent source economics (zero cost assumption — recorded as absent, never as zero-cost evidence; see Execution assumptions). The 9/5/±50 inputs, the `+100`/`+1` fractal-distance constants, the signed `round()` efficiency construction, the EMA(5) smoothing, the ±50 hysteresis latch, the atomic reversal, the single-position posture, and the no-stop/no-target/no-cooldown stance are source-native and unmodified.

Pre-write dedup (2026-10-15): working-tree case-insensitive searches for `polarized`, `fractal efficiency`, `BuyBand`/`SellBand`, `xFracEff`, `hannula`, and `dTukyGTy` return zero strategy records using this source, author script, indicator, or construction (the sole `PFE` hit anywhere is the Pfizer ticker illustration inside the Force Index record, a different subject entirely). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state-following reversal two-sided), plus docs-only #212 — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `kama-efficiency-ratio-adaptive-trend-two-sided-btcusdt-1d` is the same HPotter template but computes an efficiency-ratio-scaled smoothing constant (0.666/0.0645 fast/slow ends) and trades prior-close-vs-adaptive-average state — no band, no hysteresis, no EMA-of-signed-efficiency; `frama-ma-cross-gated-long-btcusdt-1d` adapts by fractal dimension with an SMA-cross trigger; `vidya-cmo-adaptive-slope-trend-btcusdt-1h` adapts by CMO with a slope trigger; `ravi-threshold-latch-reversal-two-sided-btcusdt-1d` latches on a moving-average-convergence percentage, not on a signed fractal-efficiency oscillator; no pool record evaluates an EMA-smoothed signed fractal-efficiency reading against symmetric ±50 hysteresis bands. Five-axis distinction: mechanism differs (fractal-distance efficiency oscillator versus adaptive average, fractal dimension, CMO smoothing, or convergence percentage), signal construction differs (no pool record builds `sqrt(Δ²+100)/Σsqrt(δ²+1)` signed efficiency with `round()` discretization), trigger differs (dual-threshold hysteresis latch with sticky mid-zone hold, not a cross, not a single-rail state), data differs (`close` only; no `high`, no `low`, no `open`, no `volume`), and source identity differs (TV `dTukyGTy` HPotter 2017-09-29).

## Economic mechanism

### Source-reported

Fractal-efficiency trend acceptance with hysteresis-band reversal discipline (header prose plus quoted Pine, educate-only warning fenced above): the numerator `sqrt((close − close[9])² + 100)` measures the straight-line distance travelled over 9 bars; the denominator `Σsqrt((close − close[1])² + 1)` accumulates the per-bar path length over the same window. Their signed, percent-scaled ratio prints near ±100 when the 9-bar run is straight (efficient, trend acceptance) and near 0 in chop (inefficient drift). Smoothing that reading with EMA(5) and latching it against ±50 bands means a leg is entered only when smoothed efficiency escapes the mid-zone to its side, and held while it merely decays back into the zone — the opposite band escape is the exit. There is no stop, no target, no flat state by design after the first signal — the opposite band is the exit. The design bets that straight-line 9-bar efficiency, hysteresis-filtered, separates tradable runs from noise better than any fixed-average cross, and that the highest-expectancy posture is to always hold the side of the last band escape.

### Research interpretation

Single-series oscillator-latch system, two-sided, always-in-position after the first signal, with a sticky hold inside the (−50, +50) mid-zone. Unlike cross systems that trade the moment one line passes another, this rule has no second series at all: the only moving part is the smoothed efficiency reading itself, and the bands convert it into a three-state latch (long / hold / short) where the hold state inherits the last escape. Unlike single-rail state systems, a decaying leg is not exited on mere weakening — it must prove the opposite side's efficiency before the book flips, which suppresses mid-zone flicker at the cost of late exits. The price of the always-in posture is indefinite adverse rides: a leg whose opposite band never prints is held forever, and alternating band escapes print repeated full reversals with no flat state to hide in. The bet is on hysteresis-filtered fractal efficiency, not on any momentum extreme, volume print, second series, or calendar effect.

## Signal

Exact rule as pinned (all inputs frozen — any other value is a different, unpinned rule):

- Declarations (derived): single-position state machine over `BTCUSDT 1d` with same-bar-close execution and house sizing/costs (see Execution assumptions). At most one open leg; state ∈ {flat, long, short}; flat exists only before the first signal and under the warmup rule.
- Polarized efficiency, pinned verbatim at defaults (`Length = 9`, `LengthEMA = 5`, `BuyBand = 50`, `SellBand = −50`, `reverse = false`): with `c(t) = close(t)`: `D(t) = sqrt((c(t) − c(t−9))² + 100)`; `P(t) = Σᵢ₌₀⁸sqrt((c(t−i) − c(t−i−1))² + 1)` (strictly ≥ 9 by construction — no division by zero, no NaN, deterministic); `E(t) = round(+100·D(t)/P(t))` iff `c(t) − c(t−9) > 0`, else `round(−100·D(t)/P(t))` (exact-equality closes take the negative branch — deterministic, never invented); `S(t) = ema(E, 5)` seeded `0` via `nz`-equivalent before warmup (fenced below — no traded bar reads the seed). Only `close` is read anywhere.
- State update (source-native, evaluated once per completed bar): `pos(t) = 1` iff `S(t) > 50`; `−1` iff `S(t) < −50`; else `pos(t−1)` (sticky hold inside the mid-zone, including exact band touches at ±50; both triggers are strictly mutually exclusive — no bar can fire both, no priority rule needed).
- Entry long: on `pos` transitioning to `1` (from flat: open long; from short: atomic reversal — close short plus open long as a single reversal event, matching Pine's opposite-side `strategy.entry` reversal). Refires of the `pos == 1` state while already long are no-ops (Pine-default no-pyramiding). Entry short: mirror on transition to `−1`.
- Exits: the opposite transition only (long exits exactly when `pos` flips to `−1` and vice versa). No stop, no target, no trailing, no time exit, no cooldown — pinned as written (the script ships zero `strategy.exit` legs and names no stop anywhere), explicitly none, not invented. The standalone block contains no `close_all` anywhere, so there is no flat path after the first signal at all — `possig == 0` is reachable only on the seed bar(s) before any signal, where the book is already flat.
- Direction: two-sided with an explicit pre-first-signal flat state (plus the 15-bar warmup flat by record rule). `reverse = false` preserves both sides; a long-only or short-only reading would contradict the prescribed sell leg, and enabling `reverse` would invert both sides — each is a different, unpinned rule.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (polarized-efficiency window, EMA recursion, and band-latch comparisons). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (derived pin; the block contains no `security(`/`request.*` call, so the derived rule is single-frame by construction).
- Warmup: the binding seed is the 9-bar polarized-efficiency window (first fully-defined `E` needs 10 completed closes via `close[9]`) plus the EMA(5) recursion and the `pos[1]` latch margin. The adopted warmup is the first 15 completed `1d` bars flat by record rule (predeclared researcher choice — covers the 10-bar seed plus margin; the seed branch never fires on a traded bar). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Each bar's close enters the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (derived pin; the code names no market and no timeframe — venue choice, symbol spelling, and frame are disclosed here, never presented as source claims).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar fill (no execution-timing argument ships anywhere — quoted verbatim in census); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity, and the trigger reads only completed closes, so each bar's outcome is a single deterministic event (hold, open, or atomic reversal) under either fill convention.
- Sizing/capital/costs: the source ships no portable economics (zero commission/quantity assumption — recorded as absent economics, never as zero-cost evidence) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: single-position machine — at most one open leg; same-state bars while positioned are no-ops; the opposite transition reverses in full (one atomic event); re-entry is allowed on the next fresh transition after any close (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (Length-9 polarized-efficiency distances with `+100`/`+1` constants, the signed `round()` percent construction with the strict-inequality positive branch, the EMA(5) smoothing, the ±50 hysteresis latch with `nz(pos[1], 0)` hold, and the Long/Short entry pair with Pine-default reversal) plus the fractal-geometry header prose and the long/short settings note — quoted in Provenance. It ships no portable performance: only an educate-only warning, no table, no figure, no metric — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: the block contains zero `strategy.exit` legs and zero close calls of any kind; the no-stop/no-target/no-time posture is prescribed, explicitly none, never hidden.
2. The seed-flat branch fenced as pre-signal-only: `pos == 0` survives only until the first bar whose smoothed efficiency lands strictly outside the mid-zone, after which `nz(pos[1], 0)` carries ±1 forever. No positioned bar can reach flat — there is no mid-book flat path to misread as an exit leg.
3. Div-zero impossible in code: `C2C = sum(sqrt(pow((close - close[1]), 2) + 1), Length)` sums 9 terms each ≥ 1, so the divisor is ≥ 9 on every bar. No guard needed, no NaN, no order ambiguity, deterministic.
4. Sign-branch exclusivity fenced: `close − close[9] > 0` and its complement partition every bar — exactly one branch fires, and the equality case deterministically takes the negative leg. Band triggers `S > 50` / `S < −50` are strictly mutually exclusive with a deterministic hold otherwise — no bar fires both transitions, and no priority rule is needed or invented.
5. Reversal completeness fenced: Pine's opposite-side `strategy.entry` closes the open leg and opens the new one; the record's atomic-reversal event mirrors exactly this — no positioned bar swallows an opposite transition, and same-state bars are no-ops under default no-pyramiding (`pyramiding` unset, quoted in census).
6. No future leakage in the stack, stated plainly: at decision bar `t`, the efficiency construction reads closes `t−9…t` and the EMA recursion reads prior smoothed values — every input is complete at bar `t`'s close. No `security()`, no `request.*`, no negative index, no `barstate.islast`-gated repainting path, no `time` read at all. The seed branch is fenced out of every traded bar by the 15-bar warmup.
7. Two-sided posture provably complete: symmetric `"Long"`/`"Short"` entry legs with a symmetric hysteresis trigger and symmetric reversal exits at the pinned `reverse = false`; enabling `reverse` inverts both sides and is a different, unpinned rule. No third direction exists.
8. KAMA-overlap fence, admitted plainly: the sibling HPotter `KAMA Backtest` record shares the template shape (Long/Short pair, `reverse` input, Pine-default reversal) and an efficiency intuition, but computes an efficiency-ratio-scaled smoothing constant traded against prior-close-vs-average state — no band, no hysteresis, no signed `round()` oscillator, no EMA-of-efficiency. This record pins the standalone HPotter PFE block only and adopts none of the KAMA arithmetic.
9. Close-only data fence: the block's alphabet of price reads is exactly `{close}` — venue `high`/`low`/`open`/`volume` definition differences cannot touch any order-gating line. A venue that cannot supply 10 pre-decision daily closes cannot trade the pinned rule.
10. Derivation boundary fenced: the only non-source-native behaviors in this record are the `BTCUSDT 1d` market/frame pin, same-bar-close fills, the adopted 15-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the polarized-efficiency arithmetic, the 9/5/±50 inputs, the close-only inputs, the hysteresis latch, the atomic reversal, the single-position guards, and the risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, or timing of the source passes.
11. Network limitation disclosed: every formula line above was read verbatim from the canonical page's own Source code tab at HTTP 200 (title/author/date identity verified in-page by this runner); no immutable mirror is cited because none is needed — the canonical open-source block is the complete executable artifact.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: Length-9/EMA-5 polarized efficiency / ±50 hysteresis latch with hold / atomic reversal / no-stop-no-target posture / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Hysteresis relevance: replacing the ±50 latch with a zero-midline flip (`S(t) > 0` long, `< 0` short, hold on exact zero, same reversal handling) must not improve net expectancy; fail ⇒ the hysteresis bands add nothing over a midline rule.
- F2 — Window relevance: shortening the efficiency window to `Length = 4` (same EMA length, same bands, same state machine) must not improve net expectancy; fail ⇒ the 9-bar efficiency measurement adds nothing over a fast-window variant.
- F3 — Smoothing relevance: trading the raw signed efficiency `E(t)` directly against the ±50 bands (no EMA(5), same latch semantics) must not improve net expectancy; fail ⇒ the EMA smoothing adds nothing over the raw reading.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (derived pin; the code names no market at all). The close-only arithmetic ports across perpetual venues without structural change; the rule reads no high/low/open/volume, so venue bar-construction and volume-definition differences cannot touch it. The efficiency ratio is unit-free and the bands are fixed at ±50 percent-scale, so no fixed-pip recalibration is needed across assets — cross-asset behavior differences are still real and unclaimed. The rule is two-sided with no stop leg, so a spot-only deployment expresses the long state and reversal mechanics only to the extent the venue permits shorting — full two-sided expression assumes a futures venue, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no session gating anywhere); decision boundaries are calendar-day bars of the venue feed, disclosed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived market and frame: the code names no market and no timeframe; this record pins `BTCUSDT 1d`. Cross-market and cross-frame behavior differences are real — the adaptation is disclosed, and this record makes no claim about any other market, frame, or the source's native setting.
- Derived fill timing: the source fills next-bar under Pine defaults with no timing argument; this record executes same-bar-close on `1d` BTCUSDT. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- No source economics: the source ships no commission, sizing, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- No price stop, no time stop: adverse excursion after entry has no guardrail beyond the opposite hysteresis band; a leg whose opposite trigger never prints is held indefinitely. This is the prescribed posture, disclosed as a principal risk.
- Whipsaw sensitivity: smoothed efficiency flickering across a band edge prints repeated reversal pairs with no flat state to rest in, while mid-zone decay holds through arbitrarily large adverse excursions uncaptured by the latch. The latch-plus-hold construction is the prescribed design, disclosed, not smoothed.
- `round()` discretization: band-edge bars resolve on integer-rounded efficiency, so a fractional reading just inside a band can round across it (or vice versa) — deterministic per the pinned formula, but a reimplementation that smooths before rounding, or compares unrounded values, would be a different, unpinned rule.
- Warmup seed: the efficiency window needs 10 completed closes plus recursion margin; the first 15 `1d` bars are flat by record rule, so early-history signals never enter any evaluation.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- TradingView canonical script page (HPotter PFE Backtest strategy; stable-URL identity verified via HTTP-200 title/author/date record; full 36-line Pine v2 block read verbatim from the page's Source code tab): https://www.tradingview.com/script/dTukyGTy-PFE-Polarized-Fractal-Efficiency-Backtest/
- Pine strategy semantics (Pine-default fills, `pyramiding`, `nz`/`iff` semantics): https://www.tradingview.com/pine-script-reference/v5/
