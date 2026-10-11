---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Camarilla R1-S1 rail-cross reversal two-sided on BTCUSDT 1d bars
created: 2026-10-11
updated: 2026-10-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-09-18
sources:
  - https://www.tradingview.com/script/pZshc5OY-Camarilla-Pivot-Points-Backtest/
  - https://github.com/hasnocool/tradingview-pine-scripts
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Camarilla R1-S1 rail-cross reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (verified 2026-10-11):

- Canonical script page: https://www.tradingview.com/script/pZshc5OY-Camarilla-Pivot-Points-Backtest/ (`Camarilla Pivot Points Backtest — Strategy by HPotter`). Fetched from this runner with HTTP 200; the `<title>` pins `Camarilla Pivot Points Backtest — Strategy by HPotter — TradingView` and the author token `HPotter` repeats in-page. Page HTML carries the script shell without rule text from this network, so no formula line is claimed from page HTML — every formula and every order-gating line below was read verbatim from the immutable GitHub artifact instead, quoted in census.
- Pinned executable artifact (immutable GitHub mirror, complete Pine block read line by line): https://github.com/hasnocool/tradingview-pine-scripts at commit `69969aeaf271b2f7b5a7632a1bde43069a0cbe26` (2024-09-18, adopted as `source_as_of`), file `Camarilla Pivot Points Backtest.pine` (header pins `Script Name: Camarilla Pivot Points Backtest`, `Author: HPotter`, `Copyright by HPotter v1.0 07/05/2020`, description prose stating pivot studies use "values from a previous period"). Local file SHA-256 `77fc2fd00dab0dfd852472cfc77b7aff9e058ba253164412518d9074cec5a093`. Unlike indicator-`study()` sources, this artifact is a real `strategy()` with `strategy.entry` Long/Short legs — the position handling below is source-native, not a researcher state machine.
- Text census over the pinned Pine block: 1 `strategy(` / 2 `strategy.entry` (`"Long"`/`strategy.long`, `"Short"`/`strategy.short`) / 1 `strategy.close_all` (inside the `possig == 0` branch) / 0 `strategy.exit` / 0 `strategy.close(` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=` / 3 `security(` (all `syminfo.tickerid` at the `res` input, default `"D"`) / 0 `pyramiding` (Pine default: no same-direction adds; a same-direction `strategy.entry` only maintains the open leg, an opposite-side entry reverses it) / 0 `process_orders_on_close` (Pine default: per-completed-bar evaluation, next-bar fills) / 0 `commission_*` / 0 `default_qty_*` (recorded as absent economics, never as cost evidence) / 0 `volume` / 0 `open` (the token `open` appears nowhere in the file — order-gating reads `high`/`low`/`close` only) / 0 `time`/`timenow` / 0 `request.*`.
- Canonical inputs pinned verbatim: `res = "D"`, `SellFrom = "R1"`, `BuyFrom = "S1"`, `reverse = false`. Level arithmetic pinned verbatim: `xRange = xHigh − xLow`; `S1 = xClose − xRange × (1.1/12)`; `S2/S3/S4` at `(1.1/6)`, `(1.1/4)`, `(1.1/2)`; `R1..R4` mirror above `xClose`; `R5 = (xHigh/xLow) × xClose`; `S5 = xClose − (R5 − xClose)`. State machine pinned verbatim: `pos := close > B ? 1 : close < S ? −1 : nz(pos[1], 0)` with `B`/`S` selected by the `SellFrom`/`BuyFrom` options; `possig` equals `pos` at the pinned `reverse = false`; `possig == 1` enters Long, `possig == −1` enters Short, `possig == 0` closes all (reachable only while `pos` still holds its `0` seed — fenced in Negative evidence).
- Source-reported intent (mirror header prose, quoted for gate evidence): "Pivot point studies highlight prices considered to be a likely turning point when looking at values from a previous period" — the levels are previous-period levels, not same-bar levels. The script ships no market, no timeframe, and no performance claim of any kind (only an educate-only warning) — this record claims no source-reported performance and no reproduced performance.

Licence and rights: this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly five: (1) market/frame pin `BTCUSDT 1d` (the code names no market and no timeframe; this pin is a pure researcher choice, disclosed here, never presented as source-native); (2) single-frame resolution collapse — the code's `security(syminfo.tickerid, "D", …)` levels are pinned to the prior completed `1d` bar's `high`/`low`/`close` (under Pine-default `lookahead_off`, a `"D"` security read publishes the last *completed* daily bar, i.e. previous-period values exactly as the header prose states; the same-bar-HLC reading is fenced as degenerate in Negative evidence); (3) same-bar-close fills (the source ships no execution-timing argument — Pine default evaluates per completed bar and fills on the next bar; no `process_orders_on_close` ships anywhere, quoted verbatim in census); (4) an adopted 2-bar warmup with pre-warmup bars flat by record rule (levels need exactly one completed prior bar plus margin — see Required data); (5) house sizing/capital/costs replacing the absent source economics (zero cost assumption — recorded as absent, never as zero-cost evidence; see Execution assumptions). The Camarilla coefficients, the R1/S1 default selection, the rail-cross-with-hold state machine, the atomic reversal, the single-position posture, and the no-stop/no-target/no-cooldown stance are source-native and unmodified.

Pre-write dedup (2026-10-11): working-tree case-insensitive searches for `camarilla`, `pZshc5OY`, `hpotter camarilla`, and `1.1/12` return zero strategy records using this source, author script, indicator, or level construction. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closed research PRs (#6 WaveTrend, #10 golden/dead cross, #17 MACD histogram, #20 Ichimoku-RSI, #58 reconstruction batch) contain no Camarilla record. Closest pool record is a different mechanism class: `pivot-point-breakout-kaufman-btcusdt-1d` trades Kaufman pivot-high/pivot-low breakouts with `ta.pivothigh`/`ta.pivotlow` swing detection and is long-only at its pinned defaults (contested frontmatter) — this rule computes fractional-range Camarilla rails from prior-bar HLC with no swing detection anywhere and is two-sided at its pinned defaults. Five-axis distinction: mechanism differs (prior-period rail-cross state with hold versus swing-pivot breakout), signal construction differs (no pool record computes `close ± range × 1.1/12` rails, let alone crosses them with sticky hold), trigger differs (close-vs-rail state transition, not a cross of two series, not a band touch), data differs (`high`/`low`/`close` only; no `open`, no `volume`), and source identity differs (TV `pZshc5OY` HPotter 2020-05-07).

## Economic mechanism

### Source-reported

Prior-period turning-point rails with always-in-market reversal discipline (header prose plus quoted Pine, educate-only warning fenced above): Camarilla equations compress the previous period's volatility spread (`xHigh − xLow`) into fractional rails around its close — R1/S1 sit just `1.1/12` of the range outside it. A daily close printed above R1 means the market accepted prices beyond the prior period's implied resistance (breakout acceptance → long); a close below S1 means acceptance beyond implied support (breakdown acceptance → short); anything between the rails means no acceptance, so the sticky state holds whatever leg is open. There is no stop, no target, no flat state by design after the first signal — the opposite rail is the exit. The design bets that prior-period Camarilla rails are the market's real intraday-turning-point map and that the highest-expectancy posture is to always hold the side of the last acceptance.

### Research interpretation

Prior-period rail-cross state system, two-sided, always-in-market after the first signal, with a sticky hold band between the rails. Unlike cross systems that trade the moment one line passes another, this rule has memory: between R1 and S1 nothing fires and the open leg simply rides — the rails are a state machine, not a pulse generator. Unlike band-fade systems, it never fades the rail touch: touches without a close beyond the rail are ignored entirely, so a bar that spikes through R1 intraday but closes back inside changes nothing. The price of the sticky hold is indefinite adverse rides: a leg whose opposite rail is never reached on a close is held forever, and a market that chops across both rails prints repeated full reversals with no flat state to hide in. The bet is on prior-period acceptance, not on any momentum extreme, volatility compression, volume print, or calendar effect.

## Signal

Exact rule as pinned (all inputs frozen — any other value is a different, unpinned rule):

- Declarations (derived): single-position state machine over `BTCUSDT 1d` with same-bar-close execution and house sizing/costs (see Execution assumptions). At most one open leg; state ∈ {flat, long, short}; flat exists only before the first signal and (transiently) under the warmup rule.
- Level stack, pinned verbatim at defaults (`res = "D"` collapsed to prior completed bar, `SellFrom = "R1"`, `BuyFrom = "S1"`, `reverse = false`): with `pH = high[1]`, `pL = low[1]`, `pC = close[1]`, `pR = pH − pL`: `R1 = pC + pR × (1.1/12)`; `S1 = pC − pR × (1.1/12)`. `B = R1`, `S = S1`. No `open` and no `volume` is read anywhere.
- State update (source-native, evaluated once per completed bar): `pos(t) = 1` iff `close(t) > R1(t)`; `−1` iff `close(t) < S1(t)`; else `pos(t−1)` (sticky hold; `R1(t) > S1(t)` strictly whenever `pR > 0`, so the two triggers are mutually exclusive; a zero-range prior bar makes `R1 = S1 = pC` and the strict inequalities leave `close == pC` on hold — deterministic, fenced below).
- Entry long: on `pos` transitioning to `1` (from flat: open long; from short: atomic reversal — close short plus open long as a single reversal event, matching Pine's opposite-side `strategy.entry` reversal). Refires of the `pos == 1` state while already long are no-ops (Pine-default no-pyramiding). Entry short: mirror on transition to `−1`.
- Exits: the opposite transition only (long exits exactly when `pos` flips to `−1` and vice versa). No stop, no target, no trailing, no time exit, no cooldown — pinned as written (the script ships zero `strategy.exit` legs and names no stop anywhere), explicitly none, not invented. `strategy.close_all` exists in code only under `possig == 0`, which requires `pos == 0`: reachable solely on the seed bar(s) before any signal, where the book is already flat — there is no mid-book flat path.
- Direction: two-sided with an explicit pre-first-signal flat state (plus the 2-bar warmup flat by record rule). `reverse = false` preserves both sides; a long-only or short-only reading would contradict the prescribed sell leg and is a different, unpinned rule.

## Required data

- Completed `1d` bars of BTCUSDT: `high`/`low`/`close` (prior-bar rails plus same-bar close-vs-rail comparisons). No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (derived pin; the collapsed resolution reads only the immediately prior completed bar of the same frame — no live `request.*`/`security(` call survives the collapse, so the derived rule is single-frame by construction).
- Warmup: the binding seed is exactly one completed prior bar (the rail inputs). The adopted warmup is the first 2 completed `1d` bars flat by record rule (predeclared researcher choice — covers the 1-bar seed plus margin; the `nz(pos[1], 0)` pre-seed branch never fires on a traded bar). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Each bar's high/low/close enter the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (derived pin; the code names no market and no timeframe — venue choice, symbol spelling, and frame are disclosed here, never presented as source claims).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar fill (no execution-timing argument ships anywhere — quoted verbatim in census); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. The sticky-hold plus transition-only firing makes each bar's outcome a single deterministic event (hold, open, or atomic reversal) under either fill convention.
- Sizing/capital/costs: the source ships no portable economics (zero commission/quantity assumption — recorded as absent economics, never as zero-cost evidence) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: single-position machine — at most one open leg; same-state bars while positioned are no-ops; the opposite transition reverses in full (one atomic event); re-entry is allowed on the next fresh transition after any close (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (previous-period HLC inputs, the complete `(1.1/12, 1.1/6, 1.1/4, 1.1/2)` Camarilla coefficient set with R5/S5 extensions, the R1/S1 default rail selection, the close-vs-rail sticky state machine with `nz(pos[1], 0)` hold, the Long/Short entry pair with Pine-default reversal, and the seed-only `close_all` branch) plus the educate-only header prose — quoted in Provenance. It ships no portable performance: only an educate-only warning, no table, no figure, no metric — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: the block contains zero `strategy.exit` legs and the only close call is the seed-only `close_all`; the no-stop/no-target/no-time posture is prescribed, explicitly none, never hidden.
2. The `close_all` branch fenced as seed-only: `possig == 0` requires `pos == 0`, and `pos` leaves `0` permanently on the first bar whose close lands outside either rail (after which `nz(pos[1], 0)` carries ±1 forever). No positioned bar can reach it — there is no mid-book flat path to misread as an exit leg.
3. Same-bar reading fenced as degenerate (the reason for derivation 2): resolving `security(…, "D", …)` against the *same* bar's HLC makes `close > R1` (`0 > +range × 1.1/12`) and `close < S1` both identically false, so the rule would never trade. The header prose prescribes "values from a previous period", and Pine-default `lookahead_off` publishes the last completed HTF bar — the prior-bar collapse is the prose-faithful, non-degenerate reading, disclosed as derivation, never presented as the code's literal same-chart evaluation.
4. Zero-range prior bar fenced: `pR = 0` gives `R1 = S1 = pC`; both strict inequalities then fail except on exact equality, which holds — no division, no NaN, no order. Deterministic on doji/flat history.
5. Rail-trigger exclusivity fenced: `R1(t) > S1(t)` whenever `pR > 0`, so `close > R1` and `close < S1` are strictly mutually exclusive — no bar can fire both transitions, and no priority rule is needed.
6. Reversal completeness fenced: Pine's opposite-side `strategy.entry` closes the open leg and opens the new one; the record's atomic-reversal event mirrors exactly this — no positioned bar swallows an opposite transition, and same-state bars are no-ops under default no-pyramiding (`pyramiding` unset, quoted in census).
7. No future leakage in the stack, stated plainly: at decision bar `t`, rail inputs read bar `t−1` only and the trigger reads bar `t`'s completed close. No `security()`, no `request.*`, no negative index, no `barstate.islast`-gated repainting path, no `time` read at all. The pre-seed `nz` branch is fenced out of every traded bar by the 2-bar warmup.
8. Two-sided posture provably complete: symmetric `"Long"`/`"Short"` entry legs with symmetric rail triggers and symmetric reversal exits at the pinned `reverse = false`; enabling `reverse` would invert both sides and is a different, unpinned rule. No third direction exists.
9. V2-variant fence, admitted plainly: the mirror's sibling `Camarilla Pivot Points V2 Backtest.pine` rewrites the same coefficients as decimals but swaps the rail selection (`S` from H-levels, `B` from L-levels), under which the defaults degenerate to near-always-long. This record pins V1 only; adopting V2's mapping would be a different, unpinned rule.
10. Derivation boundary fenced: the only non-source-native behaviors in this record are the `BTCUSDT 1d` market/frame pin, the prior-bar resolution collapse, same-bar-close fills, the adopted 2-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the Camarilla coefficients, R1/S1 selection, rail-cross-with-hold state machine, atomic reversal, single-position guards, and risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, or timing of the source passes.
11. Network limitation disclosed: TradingView page HTML from this runner carries no rule text (script shell only — HTTP 200 identity verified via title/author tokens); every formula is quoted from the immutable mirror's verbatim Pine at pinned SHA — never from memory or paraphrase.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: prior-bar Camarilla R1/S1 rails / close-vs-rail sticky state with hold / atomic reversal / no-stop-no-target posture / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Rail relevance: replacing the R1/S1 rails with the bar's own prior close (long when `close(t) > close(t−1)` from flat/short, short on the mirror, same hold/reversal handling) must not improve net expectancy; fail ⇒ the Camarilla fractional rails add nothing over a bare prior-close momentum state.
- F2 — Hold-band relevance: removing the sticky hold (flat whenever the close lands inside the rails instead of holding the open leg, re-enter on the next outside close) must not improve net expectancy; fail ⇒ the always-in-market hold adds nothing over a rails-gated flat-between-signals rule.
- F3 — Level-width relevance: widening the trigger rails to R2/S2 (`±range × 1.1/6`, same state machine) must not improve net expectancy; fail ⇒ the R1/S1 width choice adds nothing over the next Camarilla rung.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (derived pin; the code names no market at all). The high/low/close arithmetic ports across perpetual venues without structural change; the rule reads no volume, so venue volume-definition differences cannot touch it. The fractional-range rails auto-scale in the asset's own price units, so no fixed-pip recalibration is needed across assets — cross-asset behavior differences are still real and unclaimed. The rule is two-sided with no stop leg, so a spot-only deployment expresses the long state and reversal mechanics only to the extent the venue permits shorting — full two-sided expression assumes a futures venue, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no session gating anywhere); prior-period boundaries are calendar-day bars of the venue feed, disclosed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived market and frame: the code names no market and no timeframe; this record pins `BTCUSDT 1d`. Cross-market and cross-frame behavior differences are real — the adaptation is disclosed, and this record makes no claim about any other market, frame, or the source's native intraday setting.
- Derived resolution collapse: the source's `security(…, "D", …)` levels are pinned to the prior completed `1d` bar. Under Pine-default `lookahead_off` this matches the previous-period semantics the header prose prescribes, but the literal same-chart-1d evaluation would be degenerate (fenced above) — the collapse is disclosed, not hidden, and this record makes no claim about the source's native-setting performance.
- Derived fill timing: the source fills next-bar under Pine defaults with no timing argument; this record executes same-bar-close on `1d` BTCUSDT. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- No source economics: the source ships no commission, sizing, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- No price stop, no time stop: adverse excursion after entry has no guardrail beyond the opposite rail; a leg whose opposite rail is never reached on a close is held indefinitely. This is the prescribed posture, disclosed as a principal risk.
- Whipsaw sensitivity: a close flickering across one rail prints repeated reversal pairs with no flat state to rest in, while a close parked between the rails holds through arbitrarily large intra-band excursions. The state-plus-hold construction is the prescribed design, disclosed, not smoothed.
- Short seed: rails need exactly one completed prior bar; the first 2 `1d` bars are flat by record rule, so early-history signals never enter any evaluation.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- TradingView canonical script page (HPotter Camarilla Pivot Points Backtest strategy; stable-URL identity verified via HTTP-200 title/author record, page HTML carries no rule text from this network, disclosed above): https://www.tradingview.com/script/pZshc5OY-Camarilla-Pivot-Points-Backtest/
- Immutable GitHub source (complete Pine v4 block read end to end at pinned SHA `69969aeaf271b2f7b5a7632a1bde43069a0cbe26`, 2024-09-18, local SHA-256 `77fc2fd00dab0dfd852472cfc77b7aff9e058ba253164412518d9074cec5a093`): https://github.com/hasnocool/tradingview-pine-scripts
- Pine strategy semantics (Pine-default fills, `pyramiding`, `security`/`lookahead` semantics): https://www.tradingview.com/pine-script-reference/v5/
