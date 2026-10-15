---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Ehlers Decycler Oscillator fast-slow cross long-flat on BTCUSDT 1d bars
created: 2026-10-16
updated: 2026-10-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-11-04
sources:
  - https://www.tradingview.com/script/Z9wb3LVJ-blackcat-L2-Ehlers-Decycler-Oscillator/
  - https://github.com/everget/tradingview-pinescript-indicators/blob/master/oscillators/ehlers_decycler_oscillator.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Ehlers Decycler Oscillator fast-slow cross long-flat on BTCUSDT 1d bars

## Provenance

Primary sources read end to end during this cycle (2026-10-16), pinned immutable:

- Canonical page: `[blackcat] L2 Ehlers Decycler Oscillator` by blackcat1402 at https://www.tradingview.com/script/Z9wb3LVJ-blackcat-L2-Ehlers-Decycler-Oscillator/ — fetched live during this cycle (HTTP 200, 418571 bytes of landing HTML). Page carries the `OPEN-SOURCE SCRIPT` badge. Rule text verified verbatim in the fetched bytes: `The fast line has a period of 100 a K value of 1.2 and the slow line has a period of 125 and a K value of 1`, followed by the two executable sentences `1. Enter long when the fast line crosses over the slow line;` and `2. Exit long when the fast line crosses under the slow line`, plus the `Key Signal` map `Fast_Val --> Ehlers Decycler Oscillator fast line` / `Slow_Val --> Ehlers Decycler Oscillator slow line`. Lineage text states `John F. Ehlers introuced Decycler Oscillator in Sep, 2015` and cites `In "Decyclers" in Sep, 2015, John Ehlers described a method for constructing an oscillator`, with the code note `100% John F. Ehlers definition translation, even variable names are the same`. Remarks line identifies it as `The 85th script for Blackcat1402 John F. Ehlers Week publication`.
- Construction mirror (exact recurrence evidence): `oscillators/ehlers_decycler_oscillator.pine` in `everget/tradingview-pinescript-indicators` at repo HEAD `7037c4bcc3181ab24af4b15a8ecf265487841126` — file commit `7f20cfa04e8d` (committed `2023-11-04 UTC`, sole commit touching that path, adopted as `source_as_of`; blob SHA `17352eecc173837ea0eb6e74a7bc0c15c96c9d09`, 2509 bytes, reproduced byte-identical locally this cycle). File header reads `Copyright (c) 2019-present, Alex Orekhov (everget)` under `GPL-3.0`. The file is a `study()` indicator (`//@version=3`): 0 `strategy.*` calls anywhere, so the market pin, fill timing, sizing, and warmup below are the disclosed derivation, never a source claim.
- Pinned defaults (input lines): `hpPeriod = 125` / `k = 1` (slow line), `hpPeriod2 = 100` / `k2 = 1.2` (fast line), `src = close` — identical periods, K values, and price source to the canonical page's prose.
- Pinned recurrence (function lines, normalized to one line per fact): `_hp(src, P, mult)` computes `alphaArg = 2*PI/(mult*P*sqrt(2))`, `alpha = (cos(alphaArg)+sin(alphaArg)-1)/cos(alphaArg)` (with a `cos != 0` guard falling back to the prior alpha), then `hp[t] = (1-alpha/2)^2*(src[t]-2*src[t-1]+src[t-2]) + 2*(1-alpha)*hp[t-1] - (1-alpha)^2*hp[t-2]` with `nz()` seeds. Slow line: `decycler = src - _hp(src,125,1)`, `decosc = 100*1*_hp(decycler,125,0.5)/src`. Fast line: `decycler2 = src - _hp(src,100,1)`, `decosc2 = 100*1.2*_hp(decycler2,100,0.5)/src`. Crossover/crossunder markers: `crossover(decosc,decosc2)` (green circle) and `crossunder(decosc,decosc2)` (red circle) — the fast-over-slow / fast-under-slow pair of the canonical rule.
- Code census of the 2509-byte file: 0 `strategy(` / 0 `strategy.entry` / 0 `strategy.close` / 0 `strategy.exit` / 0 `stop=` / `limit=` / target / trailing / time-exit inputs or calls / 0 `request.*` / 0 `timeframe.*` / 0 `volume` / 0 `open` / 0 `high` / 0 `low` in any order-gating line (the rule reads `close` only; `open` is used solely as the derived fill price, never as a signal input) / exactly 7 `input(` (periods, K multipliers, `close` source, three display toggles — no date-window, no mode switch, no webhook string).
- Licence and rights: this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. The source ships a market-agnostic indicator with two prose trading sentences and no order, sizing, timing, or cost leg. Researcher-declared adaptations are exactly five: (1) market pin `BTCUSDT` Binance futures `1d` (the indicator names no market — venue/frame pin disclosed, never presented as a source claim); (2) indicator→executable long-flat machine: prose cross-over becomes flat→long at the next open, prose cross-under becomes long→flat at the next open, opposite-side repeat while positioned is a no-op — completed-bar decision with next-bar-open fills, predeclared per pool precedent; (3) `src=close` pinned (both scripts' default input, never re-chosen); (4) an adopted 250-bar warmup with pre-warmup bars flat by record rule plus house sizing/capital/costs (the file ships no economics of any kind — recorded as absent, never as evidence); (5) short side explicitly disabled (the source sentences cover long entry/exit only — no short leg is invented to make a two-sided machine). The `100/1.2` / `125/1` pair, the two-stage Butterworth-HP arithmetic, the `/src` normalization, the fast-over-slow / fast-under-slow cross pair, and the no-stop/no-target posture are source-pinned. **No stop, no target, no trailing, no time exit, no pyramiding, no short, and no gate/filter beyond the two crosses is admitted in this record's version.**

Pre-write dedup (2026-10-16): working-tree case-insensitive searches for `decycler`, `deco`, `blackcat`, `everget`, `decycl` return zero strategy records pool-wide. A second sweep for `high-pass`, `highpass`, `_hp(`, and `butterworth` returns only the `bandpass-filter-reversed-cycle-sign-two-sided-btcusdt-1h` record (single beta/gamma/alpha resonator, `Length 20`, `hl2` price, `BP`-vs-`0` reversed sign-state map, two-sided always-in-market — five-axis distinction in Signal and Negative evidence 7). Open `research/*` PRs are only #48, #49, #63, #89, #92 (Larry Williams streak, Gaussian-channel StochRSI, SuperTrend flip, Chandelier Exit, SSL channel) — none is a Decycler or dual-HP-cross rule.

## Economic mechanism

### Source-reported

Near-zero-lag cycle-phase trend capture through a dual high-pass pair: each Decycler subtracts a 2-pole Butterworth high-pass filter from the price (removing fast wiggle, keeping slow trend with almost no lag), and the Oscillator pair differences two such filters at different cutoffs so the very-long components cancel and only the cycle band between the cutoffs remains. The page's own rationale is that the construction `could help traders detect trend reversals with almost no lag` via `digital signal processing techniques`. When the faster (100-period, K1.2) line sits above the slower (125-period, K1) line the cycle phase is up and the system holds long; when it falls below, the long is exited.

### Research interpretation

Dual-cutoff cycle-phase state machine, long-flat. Unlike zero-line oscillators (pool `p-signal-erf`, `tsi-signal-cross`, `ppo-signal-cross` — one line versus a constant), here nothing is ever compared to a constant: the only comparison is fast-line-versus-slow-line, so a strong trend that pins both lines positive still holds long and a grinding drift that never stretches far from zero still crosses. Unlike single-resonator sign-state rules (pool `bandpass-filter-reversed` — one `BP` output versus `0`, reversed fade mapping, always in market), here there are two separately filtered lines with K scaling and `/close` normalization, the mapping is trend-following (long when fast is above slow, never short when the output is positive), and the book rests flat between an exit cross and the next entry cross by construction. The bet, as derived, is purely on 100-vs-125-bar cycle-phase persistence at daily cadence on BTCUSDT, never on a level, extreme, oscillator threshold, volume print, calendar, or funding anchor.

## Signal

Exact rule as pinned (all constants are source input defaults or code literals; any other value is a different, unpinned rule):

- Declarations (derived): single-asset long-flat machine over `BTCUSDT 1d` with next-bar-open execution and house sizing/costs (see Execution assumptions). At most one long position; never short, never both sides.
- First stage (pinned verbatim): `hpS[t] = _hp(close,125,1)[t]`, `hpF[t] = _hp(close,100,1)[t]`, where `_hp` is the recurrence quoted in Provenance (needs `close[t]`, `close[t-1]`, `close[t-2]` and its own two priors, `nz()`-seeded).
- Detrended lines (pinned verbatim): `slow[t] = close[t] - hpS[t]`, then `SLOW[t] = 100*1*_hp(slow,125,0.5)[t]/close[t]`; `fast[t] = close[t] - hpF[t]`, then `FAST[t] = 100*1.2*_hp(fast,100,0.5)[t]/close[t]`.
- Entry long (pinned prose, Pine strict-cross semantics): `FAST[t-1] <= SLOW[t-1] and FAST[t] > SLOW[t]` (fast crosses strictly over slow on completed bar `t`) while flat → buy 100% equity at the next bar's open. A cross-over bar while already long is a no-op (no add, no reset).
- Exit to flat (pinned prose, Pine strict-cross semantics): `FAST[t-1] >= SLOW[t-1] and FAST[t] < SLOW[t]` (fast crosses strictly under slow on completed bar `t`) while long → close all at the next bar's open. Touches without strict crossing never fire; equality legs belong to no-signal by record rule (measure-zero on live tape, disclosed tie convention).
- Exits/risk: opposite-cross close only. No stop, no target, no trailing, no time exit — explicitly none by record rule (0 such calls/inputs exist in the 2509-byte file).
- Direction: long-flat (source-native posture — the page sentences cover long entry and long exit only). Short is explicitly disabled, not omitted: no short order exists in this record's version, so no margin-short permission is needed and a spot-only deployment expresses the full machine.
- Re-entry: after any exit, the next strict cross-over opens long again (no cooldown specified — explicitly none, not invented).

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (both HP stages, both detrend lines, and both cross legs read `close` and nothing else — `open` is read solely as the fill price; `high`/`low`/`volume` are read by zero lines). No funding, OI, mark/index price, order-book, on-chain, sentiment, macro, calendar, session, or cross-asset state is read anywhere.
- Single decision timeframe `1d` (no multi-timeframe call, no `request.*`, no cross-sectional ranking — one asset, one frame).
- Warmup: the binding seed is the 125-period first-stage HP plus its second-stage pass (both stages carry two-bar `nz()` recursion seeds). The adopted warmup is the first 250 completed `1d` bars flat by record rule (twice the longest cutoff — covers both HP stages' settling plus margin, per the referenced implementation's own 2×-period guidance; no cross before bar 251 may trade). Every window is trailing and every input is complete at the bar's close under next-open fills — causal, no repaint path (confirmed closes only, no `barstate.islast`, no provisional input).

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (the indicator names no market — venue/frame adaptation disclosed in Provenance, never presented as a source claim).
- Order timing (predeclared derivation): completed-bar decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) — the same verified execution primitive as the admitted `bll-vma-1-200-percent-band` and `bll-trb-200-percent-band-fixed-10d` PASS records (single-frame completed-bar decision, next-open market fill, no protective stop/limit legs anywhere in the derived machine, hence no same-bar TP/SL ordering ambiguity; each bar's outcome is a deterministic event: hold, open-long, or close-flat). No maker-touch, queue, multi-asset sync, lower/multi-timeframe alignment, non-OHLCV input, or intrabar-path-dependent fill is required by any line of this record. At most one order per bar can fire (entry fires only while flat, exit fires only while long).
- Sizing/capital/costs: the file ships no economics (no capital, sizing, fee, or slippage line of any kind — recorded as absent portable economics, never as evidence) — derived evaluation carries the fixed, reproducible house research cost model (pinned house cost assumptions for fees plus modeled funding while long — no hypothetical zero funding claimed, never presented as source-native behavior; warmup and flat spells are genuine non-accrual time). No Safety-Order/DCA event participates in the admitted cross machine regardless of downstream campaign settings.
- Concurrency: one order path over one single-asset engine position — at most one long exposure at a time; no second position is constructed anywhere. No shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The canonical page ships the full trading construction (fast `100/K1.2` vs slow `125/K1` pair, `Enter long` on fast-over-slow cross, `Exit long` on fast-under-slow cross, `Fast_Val`/`Slow_Val` signal map, Ehlers `Decyclers` Sep-2015 lineage with same-variable-name translation claim, open-source badge). The pinned mirror file ships the exact executable arithmetic (two-stage `_hp` recurrence with `cos/sin` alpha, `nz()` seeds, `100*k*HP/decycler` normalization over `close`, `crossover`/`crossunder` marker pair, `close` default source). Neither ships any performance number: this record carries zero source-reported performance figures — exact empirical figures require traceable table/figure/section provenance and are omitted, never paraphrased.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No performance carried, admitted plainly: an indicator page plus a signal-only file is venue/market-agnostic construction evidence; no number exists to transfer, and this record claims none.
2. Indicator→machine boundary fenced: the mirror file contains 0 order calls, so the flat→long / long→flat next-open machine is the predeclared derivation, never a source claim; this record is therefore never evidence that blackcat1402 or everget endorses any executable posture.
3. Short side fenced: no short sentence exists anywhere on the page and no short leg exists in the file — a two-sided reversal twin on the identical cross pair would be a different, unpinned rule, never an auto-remediation of this record.
4. Division-by-`close` edge fenced: no zero-guard ships in the file; on BTCUSDT `close > 0` on every printed bar, so the normalization is always defined — a zero or negative print would be a data-feed break, never a traded event.
5. `nz()` seed edge fenced: the first two bars seed recursion with zeros, so early `FAST`/`SLOW` prints are seed-contaminated by construction — the adopted 250-bar flat warmup exists precisely to fence them, never to tune them away.
6. One-sided causality proved: every price read is `close[t-i]` with `i >= 0` (current or past closes); every filter read is its own trailing prior; the cross compares completed-bar values only. No future, repainted, or incomplete-bar input reaches any order.
7. Overlap fences, admitted plainly: pool `bandpass-filter-reversed-cycle-sign` computes one cosine-derived resonator (`beta/gamma/alpha`, `Length 20`) over `hl2` and trades its sign versus `0` with a deliberately reversed fade map, always in market — opposite formula, opposite price, opposite trigger, opposite mapping, opposite book state. Pool `cyber-cycle-signal-self-cross` trades one Ehlers cycle line against its own prior value (self-cross momentum), never a fast-vs-slow filter pair. Pool `mama-fama-hilbert-state-flip` trades a MESA-adaptive Hilbert pair, never fixed-cutoff Butterworth HP filters. Shared "Ehlers/cycle/filter" vocabulary is not shared signal.
8. No hidden variants admitted: `100/125` cutoffs, `1/1.2` K multipliers, `0.5` second-stage multiplier, `close` source, and the display toggles are file inputs a user *could* change — every non-default combination is a different, unpinned rule. A reviewer must not pick among these to rescue or reshape the record.
9. Derivation boundary fenced: the only non-source-native behaviors are the market/venue pin, the indicator→long-flat-machine executable reading with next-open fills, the adopted 250-bar flat warmup, house sizing/costs with no admitted Safety-Order/DCA event, and the explicitly disabled short — all predeclared above; the cutoff pair, K pair, recurrence, normalization, cross pair, and long-flat posture are source-pinned or predeclared. This record is therefore never evidence that any other market, frame, cutoff, multiplier, source, timing, or direction passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `100/1.2` fast / `125/1` slow / two-stage HP recurrence / `/close` normalization / `close` source / strict fast-slow cross pair / flat→long / long→flat / no-stop-no-target posture / long-flat / `1d` BTCUSDT / next-open fills are frozen.

- F1 — K-weight relevance: setting both K multipliers to `1.0` (same cutoffs, same machine) must not improve net expectancy; fail ⇒ the `1.2` fast-line emphasis adds nothing over an unweighted filter pair on this market.
- F2 — Pair-cross relevance: replacing the fast-slow cross with a slow-line zero-cross twin (long while `SLOW > 0`, flat while `SLOW <= 0` — same filters, same machine) must not improve net expectancy; fail ⇒ the dual-line cross adds nothing over a single-line zero state on this market.
- F3 — Direction-twin relevance: a fade twin on the identical grid (long on fast-under-slow cross, flat on fast-over-slow cross — same filters, same machine, reversed sides) must not improve net expectancy; fail ⇒ the trend-following cross mapping adds nothing over fading it on this market.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (the indicator names no market — venue pin disclosed). The rule reads completed daily closes only, so no open-print, session, or cross-venue difference can touch any order-gating line beyond each calendar-day bar's own prints — but spot-vs-perp prints can still differ structurally (funding-driven drift, venue aggregation), so the futures-venue pin is load-bearing and disclosed. Cutoffs `100/125` are fixed bar-count constants, so no fixed-pip recalibration is needed across assets — cross-asset behavior differences are still real and unclaimed. The 24/7 crypto market has no opens/gaps/sessions for the rule to read beyond each bar's own prints (no session gating anywhere; the filters treat each daily bar identically); decision boundaries are calendar-day bars of the venue feed, disclosed. The rule is long-flat, so a spot-only deployment expresses the full machine — no short permission is assumed anywhere. No funding-dependent leg, no stablecoin-specific assumption. The 250-bar warmup consumes roughly 0.7 years of daily history before the first cross — disclosed as a data-availability cost. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- No price stop, no time stop: adverse excursion after a cross-over entry has no guardrail beyond the opposite cross, which may arrive many bars later, after deep excursion, or never on a one-way drift. This is the record-rule posture, disclosed as a principal risk.
- Whipsaw by design: a fast line oscillating across the slow line prints full open/close cycles at the worst prints of each flicker; the K multipliers offer no band or hysteresis against it, by the prescribed design.
- IIR settling: Butterworth-HP feedback carries seed transients for roughly two cutoff cycles; the 250-bar warmup fences the seed, but volatility-regime shifts still re-excite transients mid-sample, by the prescribed design.
- Rare-or-frequent signals unknown: the cross cadence on BTCUSDT daily is unmeasured here and unclaimed; the machine may sit flat for long stretches or churn, and sample counts may be structurally small either way.
- Warmup cost: 250 daily bars of venue history are consumed before the first legal cross — backtest coverage on young markets is structurally short, disclosed.
- Next-open timing reading: the prose crosses confirm on bar close while fills land on the next open; an engine modeling same-bar-close entries would trade different (slightly earlier) events.
- Venue-portability residual: the rule carries only the arithmetic construction — any venue's prints, fees, funding, and margin mechanics beyond the house model are unclaimed, disclosed.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior and never part of this admission — no Safety-Order/DCA event is admitted in this record's version. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Canonical TradingView indicator page, blackcat1402 ([blackcat] L2 Ehlers Decycler Oscillator: fast 100/K1.2 vs slow 125/K1 pair, enter-long on fast-over-slow cross, exit-long on fast-under-slow cross, Ehlers Decyclers Sep-2015 lineage, open-source script, fetched live during this cycle): https://www.tradingview.com/script/Z9wb3LVJ-blackcat-L2-Ehlers-Decycler-Oscillator/
- Construction mirror read end to end this cycle, `everget/tradingview-pinescript-indicators` file `oscillators/ehlers_decycler_oscillator.pine` (2509 bytes; © Alex Orekhov, GPL-3.0; file commit `7f20cfa04e8d` dated 2023-11-04; two-stage `_hp` recurrence, `125/1` and `100/1.2` defaults, `close` source, `crossover`/`crossunder` marker pair verified from the pinned bytes): https://github.com/everget/tradingview-pinescript-indicators/blob/master/oscillators/ehlers_decycler_oscillator.pine
