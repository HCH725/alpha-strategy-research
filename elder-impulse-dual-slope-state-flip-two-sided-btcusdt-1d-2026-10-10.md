---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Elder Impulse dual-slope state-flip two-sided on BTCUSDT 1d bars
created: 2026-10-10
updated: 2026-10-10
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2020-07-22
sources:
  - https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types/elder-impulse-system
  - https://github.com/thanhnguyennguyen/tradingview-pine-scripts/blob/cbb13bd8a411bf1c84cdc24a0a95384a0c2c6936/scripts/Elder_Impulse_System.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Elder Impulse dual-slope state-flip two-sided on BTCUSDT 1d bars

## Provenance

Primary sources read end to end and cross-checked against each other (fetched 2026-10-10):

- Technical specification: StockCharts ChartSchool `Elder Impulse System` page (https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types/elder-impulse-system, ~692KB fetched over HTTPS during this cycle). The page attributes the system to Alexander Elder's book `Come Into My Trading Room`, states the system "identifies inflection points where a trend speeds up or slows down", and pins the full decision rule verbatim: Green price bar = (13-period EMA > previous 13-period EMA) AND (MACD-Histogram > previous period's MACD-Histogram); Red price bar = both falling; blue otherwise. The MACD-Histogram is pinned to MACD(12,26,9). Entries/exits prose: "A buy signal occurs when the long-term trend is deemed bullish, and the Elder Impulse System turns bullish on the intermediate-term trend" (weekly gate required for daily buys; sells mirrored; counter-gate signals ignored). The page's quoted professional posture is "enter cautiously but exit fast" — the impulse turning against the position ends the trade. No performance table, figure, or numbered backtest claim is cited or relied on anywhere in this record; this record claims no source-reported performance.
- Executable corroboration (verbatim public Pine, indicator-grade): repository https://github.com/thanhnguyennguyen/tradingview-pine-scripts, full commit SHA `cbb13bd8a411bf1c84cdc24a0a95384a0c2c6936` (commit date 2020-07-22, subject `adding Elder impulse system`; adopted as `source_as_of` 2020-07-22), exact file path `scripts/Elder_Impulse_System.pine` (1378 bytes, CC0 notice in-file). The block sets `source = close`, `macd_length_fast = 12`, `macd_length_slow = 26`, `macd_length_signal = 9`, `ema_length = 13`, computes `macd_histogram = macd - macd_signal` with `macd = ema(source,12) - ema(source,26)`, and gates color on strict inequalities only: `elder_bulls = (ema[0] > ema[1]) and (macd_histogram[0] > macd_histogram[1])`, `elder_bears = (ema[0] < ema[1]) and (macd_histogram[0] < macd_histogram[1])`, else blue, applied via `barcolor`. Census: 0 `strategy.*` calls of any kind (pure `study` indicator — no order, qty, timing, commission, or sizing ships anywhere), 0 `request.*` calls (single frame by construction), 0 `volume`/`high`/`low` reads in any gating line (`source = close` only). Formula-for-formula identical to the ChartSchool specification, including strict (not >=) slope comparisons.
- No `©` republication beyond single-line declarations quoted for gate evidence; this record cites and normalizes the rule and reproduces no source block beyond the short declarations above.

Licence and rights: the ChartSchool page is public technical documentation and the mirror file carries an in-file CC0 notice. This record cites and normalizes the rule only.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly five: (1) single-timeframe collapse — the source-native posture is dual-timeframe (weekly/long-term gate plus intermediate impulse; StockCharts discards daily signals against the weekly trend), while the derived strategy runs the impulse state machine on `1d` bars alone with no higher-timeframe gate (material, predeclared — a genuinely weekly-gated variant would be a different, unpinned rule); (2) same-bar-close fills on completed-bar decisions (the source is an indicator study with no order-timing leg at all; the ChartSchool entries/exits prose keys off closed-bar impulse turns); (3) an adopted 100-bar warmup with pre-warmup bars flat by record rule (covers EMA-26 plus signal-line seeding — see Required data); (4) house sizing/capital/costs replacing the source economics (the source ships zero economics of any kind — see Execution assumptions); (5) venue normalization to BTCUSDT Binance perpetual (the source is market-generic; Elder wrote for equities — no market-specific leg is altered because none exists). There is deliberately NO length/threshold change (`13` / `12,26,9` / strict inequalities frozen), NO blue-bar entry invention (blue always holds), and NO stop/target/trailing/time addition (the SafeZone concept belongs to a different Elder text and a different script — none is adopted here).

Pre-write dedup (2026-10-10): working-tree case-insensitive word-boundary searches for `\bimpulse\b` return a single strategy hit — the SQZMOM-LB record's generic-prose word "impulse" in its interpretation paragraph, never an Elder rule, formula, or source. `\bmama\b` / `\bfama\b` / `\bforce index\b` / `\bvpci\b` / `\bdecycler\b` return zero hits. The `elder` hits elsewhere are other records' own dedup paragraphs plus the merged `elder-ray-123reversal-combo-two-sided-btcusdt-1h-2026-10-09.md` (Elder-ray Bull Power + 123-reversal combo on `1h` — different mechanism, see distinction below). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `elder-ray-123reversal-combo-two-sided-btcusdt-1h-2026-10-09.md` ANDs a 123-reversal streak leg with a session-anchored DayHigh-minus-EMA Bull-Power leg and stands flat on disagreement (no MACD histogram, no dual-slope impulse anywhere); `macd-signal-cross-reversal-btcusdt-1d-2026-10-09.md` trades MACD-line/signal-line crosses (level crossing of two lines, no slope conjunction with any EMA); no pool record evaluates the conjunction of EMA-13 slope with MACD-histogram slope. Five-axis distinction: signal construction differs (dual-slope impulse state — trend inertia AND momentum acceleration must agree — versus line-cross or power-minus-consensus constructions), trigger differs (fresh green/red impulse turns with blue-bar hold versus cross pulses or agreement gates), exits differ in event set (opposite-impulse reversal only, blue never exits, no stop/target/trailing/time leg), source identity differs (Elder/StockCharts lineage with a CC0 Pine pin at `cbb13bd` versus FMZ IDs or other TV authors), and timeframe handling differs (deliberate single-`1d` derived collapse with the weekly gate explicitly dropped versus source-native MTF or single-frame natives).

## Economic mechanism

### Source-reported

Dual-engine impulse censorship (Elder via StockCharts): a 13-period EMA measures trend inertia (rising = bulls in charge of trend) while the MACD-Histogram slope measures momentum acceleration (rising = bulls growing stronger). Only bars where both engines point the same way are tradable impulses — green means trend and momentum jointly accelerate upward, red jointly downward. Mixed bars (blue) mean one engine has failed: the trend is losing a driver, so the system censors new entries and hurries exits rather than predicting. The quoted professional posture is "enter cautiously but exit fast".

### Research interpretation

State-following (not pulse-triggered, not level-holding) two-sided trend-momentum system with no price stop, target, trailing, or time exit — flat until the first green/red close, then always positioned, holding through blue indecision and flipping only on the opposite impulse. Unlike pulse-cross systems (Laguerre, MACD-signal-cross) that fire on single bars and must flip immediately, blue bars are a first-class hold state: a green run interrupted by one blue bar keeps the long on. Unlike agreement-flat systems (Elder-ray combo) that stand aside on disagreement, disagreement here holds the existing side — the censor bites entries, never the held position. The honestly priced cost is slow exit in rounded reversals: a long entered on a fresh green can ride through a long blue decay before the first red close flips it.

## Signal

Exact rule as pinned (`13` / `12,26,9` / strict inequalities / `close` frozen — any other value, source, or comparison is a different, unpinned rule):

- Indicator arithmetic (pinned, source-verbatim, single-TF): on BTCUSDT `1d` closes, `E13 = EMA(close,13)`; `MACDline = EMA(close,12) - EMA(close,26)`; `MACDsig = EMA(MACDline,9)`; `hist = MACDline - MACDsig`. All reads are `close` only.
- Bar state on each completed bar `t` (strict comparisons per the pinned code — equality on either leg yields blue, never forced): `Green(t) = (E13(t) > E13(t-1)) AND (hist(t) > hist(t-1))`; `Red(t) = (E13(t) < E13(t-1)) AND (hist(t) < hist(t-1))`; `Blue(t)` otherwise.
- Position state machine (derived, fully specified): state in {flat, long, short}; flat before the first non-blue close by record rule. On each completed bar close: Green closes long-or-enters (enter full unit if flat or short — a held short reverses in full in the same step); Red mirrors to short; Blue holds the prior state (flat stays flat). Green-while-long and Red-while-short are holds with no add (see Execution assumptions).
- Same-bar exclusivity: Green and Red are mutually exclusive on every bar by construction (both slope pairs cannot simultaneously rise and fall), so no bar can ever order both sides — no same-bar ordering ambiguity exists anywhere in this record. The double-equality edge (both legs exactly unchanged) yields Blue and the position simply holds — stated, not patched.
- Risk legs (pinned absence, not invented): the source ships no order block at all and the ChartSchool exit leg is the opposite impulse turn — the derived posture is explicitly no stop, no target, no trailing, no time exit. No SafeZone, ATR, or volatility leg is adopted.
- Direction: two-sided long/short with symmetric state reversal. Futures venue required for the short leg (the derived venue is a perpetual — pinned).
- Display isolation: the pinned Pine's `barcolor` renders only and gates no order beyond the Green/Red predicates normalized above.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (sole series read by any order-gating line — `source = close` in the pinned block; `high`, `low`, `open`, `volume` are read nowhere). No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request.*` calls; the source-native weekly gate is dropped by predeclared derivation, never silently modeled).
- Single decision timeframe `1d` (derived collapse — see declaration; no `request.*` call anywhere).
- Warmup: the EMA-26 leg plus the 9-bar signal smoothing need a seeding transient (leading bars carry `nz`-style zero-seeded indicator artifacts in any faithful implementation). The adopted warmup is the first 100 completed `1d` bars flat by record rule (predeclared researcher choice — covers the slowest leg several times over); no bar before bar 101 may trade. No repainting (`close` read only on completed bars), no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (the source is market-generic with no market leg; venue choice is researcher-declared, never presented as source-native).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is indicator-grade (no order block ships anywhere); this record does not claim any source fill convention. No maker-touch, queue, or intrabar-path-dependent fill: with mutually exclusive state transitions and no stop/target legs, there is no same-bar ordering ambiguity of any kind. `1d` is a supported pinned-engine interval (current campaign already screens `1d`).
- Sizing/capital/costs: the source ships no live sizing argument of any kind (pure `study`) and no commission, fee, slippage, margin, or funding assumption anywhere. The explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all) apply to the derived evaluation here, with the single-unit/no-add/reverse-full position pin from Signal, never presented as source-native behavior.
- Concurrency: at most one unit per side (same-direction re-entry is a hold, never an add, by state-machine construction — restated as record rule, predeclared); the opposite impulse reverses in full in one step; re-entry after a reversal needs only the next opposite impulse (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The short leg requires margin-short permission, realistic on the pinned perpetual venue.

## Evidence

### Source-reported

The ChartSchool page ships the full specification (Elder/Come-Into-My-Trading-Room attribution, the "inflection points where a trend speeds up or slows down" purpose line, the Green/Red/Blue decision rule with MACD(12,26,9) pinned, the weekly-gate entries/exits doctrine with valid/ignored-signal chart illustrations, and the "enter cautiously but exit fast" posture line). The pinned Pine block ships the executable corroboration (`Elder Impulse System` study, `source = close`, `12/26/9` MACD inputs, `13` EMA input, strict-inequality bull/bear predicates, CC0 notice). Neither source ships a performance table, figure, or numbered backtest claim — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.*` calls ship anywhere in the pinned block — the sole position-changing path is the opposite impulse turn reversing the full unit. The absence of any live stop is coded absence, disclosed, not a tunable parameter here.
2. Always-positioned exposure after the first impulse, admitted plainly: the system holds a side through blue decay until the opposite impulse — a market that trends against the entry keeps the full unit on with no guardrail beyond the next opposite turn, which may arrive many bars later or after deep excursion. Whipsaw that alternates green/red across chop flips the full unit repeatedly. This is the derived trade, disclosed, not a tunable parameter here.
3. Weekly-gate collapse fenced: the source-native rule discards daily impulses against the weekly trend; the derived strategy trades every `1d` impulse with no gate. A genuinely weekly-gated variant would be a different, unpinned rule — none is admitted here. This record is therefore never evidence that the dual-timeframe Elder posture itself passes.
4. Derivation boundary fenced: the only non-source-native behaviors in this record are the single-`1d` collapse, same-bar-close fills, the adopted 100-bar warmup with record-rule pre-warmup flat, venue normalization, and house sizing/costs — all predeclared above; the `13` / `12,26,9` literals, the `close` source, the strict-inequality dual-slope predicates, the Green/Red/Blue state set, the blue-hold rule, the full-unit reversal, the two-sided stance, and the no-stop/no-target/no-cooldown stance are source-verbatim. This record is therefore never evidence that any weekly-gated, next-tick-fill, or SafeZone-stopped reading of the source itself passes.
5. The `13` / `12,26,9` literals, the strict (not >=) comparisons, the dual-slope conjunction (not either leg alone), the blue-hold rule (not blue-exit, not blue-entry), the full-unit reversal, the two-sided stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning any literal, converting the conjunction into a single-leg or line-cross rule, exiting or entering on blue, adding a stop/target/filter/cooldown/gate, dropping the short leg, or sizing partially instead of full-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `13` / `12,26,9` / strict dual-slope conjunction / `close` / blue-hold / full-unit reversal / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Conjunction relevance: replacing the pinned dual-slope conjunction with either single leg alone (EMA-13 slope only, or histogram-slope only) under the identical state machine must not improve net expectancy; fail ⇒ the conjunction adds nothing over its parts and the impulse pin is unmoored.
- F2 — Construction relevance: replacing the pinned histogram-slope leg with a MACD-line/signal-line cross leg (the pool's existing MACD mechanism) under the identical EMA-13 slope conjunction must not improve net expectancy; fail ⇒ the slope-of-histogram construction adds nothing over the ordinary line cross.
- F3 — Direction relevance: replacing the coded impulse-following direction (long on fresh green) with its fade (long on fresh red) under the identical gate must not improve net expectancy; fail ⇒ the executable direction adds nothing over its mirror and the rule is direction-arbitrary.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision frame derived single-`1d`; no signal-series adaptation of any kind — predeclared section above lists all five derivations, none touching lengths, comparisons, or source). The close-price EMA/MACD recursion ports across perpetual venues without structural change. The short leg requires margin-short permission (realistic on perpetual venues; a spot-only deployment cannot express the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read, so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Single-timeframe collapse: the source-native weekly gate is dropped; backtest economics of the gated versus collapsed postures differ by construction — the adaptation is disclosed, not hidden.
- Derived fill timing: the source is an indicator study with no order-timing leg; this record executes same-bar-close on `1d` BTCUSDT perpetual — disclosed, not hidden, never claimed as source convention.
- Position-state pin: restates the hold/no-add/reverse-full state machine as record rule; it is a researcher restatement where it goes beyond the indicator predicates, disclosed, not source-verbatim.
- Weekly-gate prose exists only in the ChartSchool doctrine and is excluded here — a reader trusting the doctrine alone would reconstruct the opposite-gating, unpinned rule.
- No price stop, no time stop, always positioned after the first impulse: adverse excursion after entry has no guardrail beyond the opposite impulse turn, which may arrive many bars later or after deep excursion; alternating chop across green/red flips the full unit repeatedly. This is the derived posture, disclosed as the record's principal risk.
- No source cost declaration: no live capital, commission, fee, slippage, margin, or funding assumption ships anywhere in the pinned block — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Venue choice only: the source is market-generic; the derived venue is Binance `BTCUSDT` perpetual. Microstructure, tick size, fee, and funding differences are carried by the house overlay — no equivalence is claimed.
- Equality-edge behavior (either slope leg exactly unchanged yields Blue/hold) follows the pinned strict inequalities; a >= implementation would be a different, unpinned rule — none is admitted here.

## Implementation status

Not implemented. No Hummingbot controller/executor has been written for this record; no Qlib screening, parity run, Paper, Testnet, or live deployment is authorized or claimed. Admission PASS (upon independent review) means model-consistent research admissibility under the pinned engine assumptions above — nothing more.

## Adoption boundary

- `status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. This record is not authorization to trade, allocate capital, or deploy to any live, paper, or test venue.
- Downstream eligibility (Qlib screening after event-level parity, Hummingbot re-validation, survivor promotion) is governed solely by the repository's downstream contract and is never implied by this record alone.
- Any parameter, frame, market, direction, fill-timing, or risk change versus the pinned rule above constitutes a different, unpinned strategy requiring its own record and review.

## Related Wiki records

None. No Wiki Brain ingestion was performed for this record (Scout PR-only workflow performs no intake review or wiki writes).

## Sources

- https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types/elder-impulse-system — StockCharts ChartSchool technical specification (Elder/Come-Into-My-Trading-Room lineage; Green/Red/Blue dual-slope rule with MACD(12,26,9); weekly-gate entries/exits doctrine; page fetched 2026-10-10, ~692KB).
- https://github.com/thanhnguyennguyen/tradingview-pine-scripts/blob/cbb13bd8a411bf1c84cdc24a0a95384a0c2c6936/scripts/Elder_Impulse_System.pine — public Pine mirror carrying the verbatim indicator block (`Elder Impulse System` study, `source = close`, `12/26/9` MACD, `13` EMA, strict-inequality bull/bear predicates, `barcolor`; CC0 notice; commit `cbb13bd8a411bf1c84cdc24a0a95384a0c2c6936`, 2020-07-22).
