---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: WaveTrend cross zone-gated two-sided on BTCUSDT 1d bars
created: 2026-10-11
updated: 2026-10-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-02-22
sources:
  - https://github.com/7b809/logic-gems
  - https://www.tradingview.com/script/2KE8wTuF-Indicator-WaveTrend-Oscillator-WT/
  - https://www.fmz.com/strategy/449714
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# WaveTrend cross zone-gated two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (verified 2026-10-11):

- Pinned executable artifact (real `strategy()`, Pine v5, `overlay=false`): file `strategys/wavetrend.pine` in https://github.com/7b809/logic-gems at commit `b5bba4340d3d537fa68212078e982ce4eb3311d3` (repo HEAD at research time), local SHA-256 `5c616a570df66b0e49b13eadf1e1b1d4c610580a59358533a10d95477ec86957` (64 lines, byte-verified at the pinned commit — identical hash re-fetched at the pinned SHA, never reconstructed from memory). File history shows a single touching commit `39a0c4366be52f9d15972fa8a04ec8c0960fad70` ("Auto update", 2026-02-22, adopted as `source_as_of`); the bytes are unchanged since. Header declaration quoted verbatim: `strategy("WaveTrend Cross Strategy [LazyBear Modified]", overlay=false, pyramiding=0, initial_capital=100000)`. No quantity argument ships on any order leg (Pine default single-contract sizing — recorded as absent portable economics, never as cost evidence).
- Lineage corroboration, not the executable artifact: LazyBear's canonical open-source WaveTrend indicator https://www.tradingview.com/script/2KE8wTuF-Indicator-WaveTrend-Oscillator-WT/ fetched from this runner with HTTP 200; the `<title>` pins `Indicator: WaveTrend Oscillator [WT] by LazyBear — TradingView`, the `LazyBear` author token repeats in-page, and the page carries the open-source marker. The indicator prose ("when the oscillator crosses above the signal when below the Oversold band it is a good BUY signal", mirrored for SELL) matches the pinned strategy's gated-cross construction qualitatively; every formula line in this record comes from the pinned GitHub bytes above, disclosed here, not hidden.
- Public-strategy corroboration: FMZ strategy page https://www.fmz.com/strategy/449714 ("WaveTrend Cross LazyBear Strategy", author token `burakaydingr`, `//@version=5`) fetched with HTTP 200; its prose describes the same construction (dual WaveTrend lines, faster-over-slower cross gives the buy/sell signal, four OB/OS auxiliary levels) and its backtest stanza names `Futures_Binance BTC_USDT` on `1h`. The page's full code pane is login-walled ("Login to view full source") — disclosed here; no formula line is sourced from that pane.
- Text census over the pinned script body: 1 `strategy(` / 2 `strategy.entry` (`"BUY"`/`strategy.long`, `"SELL"`/`strategy.short`) / 2 `strategy.close` (`"BUY"`, `"SELL"`) / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=` / 0 `security(` / 0 `request.*` / explicit `pyramiding=0` (no same-direction adds; an opposite-side entry reverses the open leg) / 0 `process_orders_on_close` (Pine default: per-completed-bar evaluation, next-bar fills) / 6 `input.int` (10/21/60/53/-60/-53, quoted in Signal) / 2 `ta.crossover` / 2 `ta.crossunder` / 1 `ta.cross` (display-only plot marker, reads no order path) / 1 `hlc3` (the sole price read) / 0 bare `open` / 0 bare `high` / 0 bare `low` / 0 bare `close` / 0 `volume` / 0 `time`/`timenow` / 0 `barstate.islast` / 0 `var` / 0 loops. The `initial_capital=100000` economics line is recorded as absent portable economics, never as cost evidence.

Licence and rights: this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence (the pinned script carries no licence header; the LazyBear indicator it modifies is open-source).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly five: (1) market/frame pin `BTCUSDT 1d` (the code names no market and no timeframe; this pin is a pure researcher choice, disclosed here, never presented as source-native); (2) same-bar-close fills (the source ships no execution-timing argument — Pine default evaluates per completed bar and fills on the next bar; no `process_orders_on_close` ships anywhere, quoted verbatim in census); (3) an adopted 60-bar warmup with pre-warmup bars flat by record rule (the EMA(21)-of-CI chain resolves far earlier — see Required data); (4) house sizing/capital/costs replacing the absent source economics (no quantity, no commission, no slippage ships anywhere; see Execution assumptions); (5) record-pinned cross tie-break and na-division semantics (the source calls `ta.crossover`/`ta.crossunder` without pinning the exact-tie bar, and divides by an EMA that reads exactly zero on exactly-flat windows — this record pins both outcomes arithmetically in Signal, disclosed here as researcher specification, never presented as source-verbatim Pine semantics). The 10/21/60/53/-60/-53 inputs, the hlc3-EMA-SMA arithmetic, the 0.015 normalization, the zone-gated entries, the ungated opposite-cross closes, the entry-before-close statement order, the single-position posture, and the no-stop/no-target/no-cooldown stance are source-native and unmodified.

Pre-write dedup (2026-10-11): working-tree case-insensitive searches for `wavetrend`, `logic-gems`, `burakaydingr`, `449714`, and `wave-trend` return zero strategy records using this source, author script, or construction — no `main` record reads WaveTrend anywhere in any order leg. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closed PR #6 (LazyBear WaveTrend wt1/wt2 cross, NOT_LOSSLESS) is distinguished on five axes, not revisited: (i) trigger — this record's entries are zone-gated (`wt1 < -53` / `wt1 > 53` conjunctions), while #6's entries fired on every naked wt1/wt2 cross with OB/OS levels plot-only; (ii) direction — two-sided with symmetric close legs here versus long-only with the short leg commented out there; (iii) exits — symmetric opposite-cross closes on both legs here versus a single-leg close there; (iv) source identity and version — logic-gems Pine v5 artifact at pinned SHA here versus the fmzquant Pine v4 artifact there; (v) specification stance — this record predeclares the tie-break and na-division outcomes as a derived executable rule (see Signal), while #6 claimed 1:1 lossless fidelity and left both outcomes open, which was its exact blocker. Closest pool records are different mechanism classes: `qqe-fast-slow-cross-two-sided-btcusdt-1d` smooths RSI, not channel-normalized typical price; `tsi-signal-cross-reversal-btcusdt-1d` double-smooths momentum without channel normalization or zone gating; `stochastic-ott-dual-trend-btcusdt-1d` is a bounded %K/%D cross with a trend-filter overlay, not a CCI-family oscillator. No pool record evaluates a WaveTrend WT1/WT2 cross, and no pool record gates entries on ±53 zone conjunctions.

## Economic mechanism

### Source-reported

Oversold-bounce / overbought-exhaustion capture on channel-normalized momentum (pinned Pine plus FMZ prose): the WaveTrend chain stretches typical price `hlc3` away from its EMA(10) channel in units of EMA-smoothed absolute deviation (the 0.015 divisor is the CCI-family constant that scales the excursion), then re-smooths twice (EMA(21), SMA(4)) into a fast line WT1 and a signal line WT2. A WT1-over-WT2 cross that prints while WT1 is still below −53 means downside momentum is turning before the bounce has travelled far — the prescribed long entry; the mirror above +53 is the prescribed short. Exits need no target because any opposite cross — gated or mid-zone — closes the leg: the design bets that the turn of the fast line itself, not a level, is the timely exit. There is no stop, no target, no flat-holding logic beyond the close legs.

### Research interpretation

Zone-gated reversal system, two-sided, with honest flat states. Unlike naked-cross records, the trigger has a bouncer: mid-zone crosses move no capital — they can only close an open leg, never open one — so the book sits flat through chop that never reaches an extreme and only joins turns born inside the zones. Unlike stop/target records, risk control is purely the opposite cross: a leg whose opposite cross never prints is held indefinitely, and a market that alternates gated entries prints repeated full reversals with no resting flat. The entry-before-close statement order makes same-bar conflict resolution deterministic (a zone-qualified opposite cross reverses via the entry leg with the close leg a no-op; an unqualified opposite cross closes to flat). The bet is on extreme-born turns plus fast-line exits, not on any moving-average regime, volume print, calendar effect, or second timeframe.

## Signal

Exact rule as pinned (all inputs frozen — any other value is a different, unpinned rule):

- Declarations (derived): single-position state machine over `BTCUSDT 1d` with same-bar-close execution and house sizing/costs (see Execution assumptions). At most one open leg; state ∈ {flat, long, short}; flat exists before the first signal, after any ungated opposite cross, and under the warmup rule.
- Oscillator, pinned verbatim at defaults (`n1 = 10`, `n2 = 21`, `obLevel1 = 60`, `obLevel2 = 53`, `osLevel1 = -60`, `osLevel2 = -53`), with `ap(t) = (high(t) + low(t) + close(t)) / 3`: `esa(t) = EMA₁₀(ap)`; `d(t) = EMA₁₀(|ap − esa|)`; `ci(t) = (ap(t) − esa(t)) / (0.015 · d(t))`; `tci(t) = EMA₂₁(ci)`; `wt1(t) = tci(t)`; `wt2(t) = SMA₄(wt1)`. EMA/SMA are Pine `ta.ema`/`ta.sma` recursions evaluated once per completed bar.
- Record-pinned cross events (adaptation 5, arithmetic — no bar may fire both): bullish cross(t) ⟺ `wt1(t−1) ≤ wt2(t−1)` ∧ `wt1(t) > wt2(t)`; bearish cross(t) ⟺ `wt1(t−1) ≥ wt2(t−1)` ∧ `wt1(t) < wt2(t)`. An exact-equality prior bar therefore arms the cross rather than vetoing it — pinned here, not quoted as source semantics. Na-valued inputs (see na fence below) satisfy neither event.
- Entry long: on bullish cross(t) **and** `wt1(t) < -53` on the same bar (from flat: open long; from short: atomic reversal — close short plus open long as a single reversal event, matching Pine's opposite-side `strategy.entry` reversal under explicit `pyramiding=0`). Refires while already long are no-ops. Entry short: mirror on bearish cross(t) **and** `wt1(t) > 53`.
- Exits: `strategy.close("BUY")` on every bearish cross(t) (gated or mid-zone); `strategy.close("SELL")` on every bullish cross(t). Source statement order is entries-then-closes: a zone-qualified opposite cross reverses through the entry leg with the close leg a no-op; an unqualified opposite cross closes to flat with no new entry. No stop, no target, no trailing, no time exit, no cooldown — pinned as written (the script ships zero `strategy.exit` legs and names no stop anywhere), explicitly none, not invented. A mid-zone cross with no open opposite leg moves nothing.
- Direction: two-sided with explicit flat states (pre-first-signal, post-close, warmup). A long-only or short-only reading would contradict the prescribed SELL leg; each is a different, unpinned rule.

## Required data

- Completed `1d` bars of BTCUSDT: `high`, `low`, `close` via `hlc3` only (the EMA channel, the deviation chain, and the cross comparisons). No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (derived pin; the body contains no `security(`/`request.*` call, so the derived rule is single-frame by construction).
- Warmup: the binding seed is the EMA(21) of `ci` (resolves within ~30 completed closes) over the EMA(10) channel pair; the SMA(4) signal line resolves earlier. The adopted warmup is the first 60 completed `1d` bars flat by record rule (predeclared researcher choice — covers the recursion seeds plus margin; no traded bar reads a seeded value). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Each bar's HLC enters the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (derived pin; the code names no market and no timeframe — venue choice, symbol spelling, and frame are disclosed here, never presented as source claims). Full two-sided expression assumes a futures venue; a spot-only deployment expresses the long state and reversal mechanics only to the extent the venue permits shorting — disclosed.
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar fill (no execution-timing argument ships anywhere — quoted verbatim in census); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity, and the trigger reads only completed-bar HLC, so each bar's outcome is a single deterministic event (hold, open, close, or atomic reversal) under either fill convention.
- Sizing/capital/costs: the source ships no portable economics (no quantity, commission, or slippage argument ships anywhere — recorded as absent economics, never as zero-cost evidence) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: single-position machine — at most one open leg; same-state bars while positioned are no-ops; the opposite qualified cross reverses in full (one atomic event); the opposite unqualified cross closes to flat; re-entry is allowed on the next fresh qualified cross after any close (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (10/21 channel/average lengths, the hlc3-EMA-deviation-CI chain with the 0.015 constant, the EMA(21)/SMA(4) WT1/WT2 pair, the ±60/±53 zone grid, the zone-gated BUY/SELL entry pair, and the symmetric opposite-cross close pair with explicit `pyramiding=0`) plus the FMZ prose naming the faster-over-slower cross with OB/OS auxiliaries and a `Futures_Binance BTC_USDT 1h` backtest stanza — quoted in Provenance. It ships no portable performance: no table, no figure, no metric — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: the body contains zero `strategy.exit` legs; the only exit paths are the two quoted `strategy.close` legs on opposite crosses. The no-stop/no-target/no-time posture is prescribed, explicitly none, never hidden.
2. Zone-gate veto fenced: a wt1/wt2 cross whose WT1 prints mid-zone (`−53 ≤ wt1 ≤ 53`) fires no entry leg at all — the `< osLevel2` / `> obLevel2` conjunctions are order-gating, quoted verbatim. No flat bar can be entered by a mid-zone cross; such a cross can only close an open opposite leg.
3. Trigger exclusivity fenced: the record-pinned bullish/bearish cross events are strictly mutually exclusive on one bar (both require opposite strict inequalities on the current bar) — no bar fires both entries, no priority rule needed or invented beyond the source's entries-then-closes statement order, which is mirrored exactly.
4. Same-bar conflict resolved by source order: entry legs precede close legs in the pinned bytes, so a zone-qualified opposite cross reverses via the entry with the close a deterministic no-op; an unqualified opposite cross closes to flat. No bar produces both a close and a same-direction open.
5. Reversal completeness fenced: Pine's opposite-side `strategy.entry` closes the open leg and opens the new one; the record's atomic-reversal event mirrors exactly this — no positioned bar swallows an opposite qualified cross, and same-state bars are no-ops under explicit `pyramiding=0` (quoted in census).
6. Na-division fence, stated plainly (adaptation 5): on an exactly-flat `hlc3` window `d(t) = 0`, so `ci(t)` resolves to Pine `na`; `na` propagates through `tci`/`wt1`/`wt2`, and `na`-valued cross events satisfy neither record-pinned event — no order leg can fire on an `na` bar. The flat-window outcome is therefore hold-by-construction, pinned here as researcher specification, never quoted as source text.
7. Tie-break fence, stated plainly (adaptation 5): an exact `wt1(t−1) == wt2(t−1)` tie arms the cross (or-equal prior) rather than vetoing it — one deterministic outcome is pinned for the derived rule; the source's Pine-version wording is not quoted as fidelity, and the alternative strict-prior reading is a different, unpinned rule.
8. No future leakage in the stack, stated plainly: at decision bar `t`, the slowest inputs are completed closes through bar `t` (EMA seeds resolve before the 60-bar warmup ends) — every input is complete at bar `t`'s close. No `security()`, no `request.*`, no negative index, no `barstate.islast`-gated repainting path, no `time` read at all. The `ta.cross` plot marker reads the same completed-bar pair and drives no order.
9. hlc3 data fence, admitted plainly: unlike close-only records, the order-gating chain reads venue `high` and `low` through `hlc3` — venue bar-construction differences can touch `ap` and hence every downstream value. A venue that cannot supply completed HLC daily bars cannot trade the pinned rule; extension to heikin-ashi or otherwise resampled feeds would be a different, unpinned rule.
10. Two-sided posture provably complete: symmetric `"BUY"`/`"SELL"` legs with symmetric zone-gated triggers and symmetric opposite-cross closes. No third direction exists.
11. Derivation boundary fenced: the only non-source-native behaviors in this record are the `BTCUSDT 1d` market/frame pin, same-bar-close fills, the adopted 60-bar warmup with record-rule pre-warmup flat, house sizing/costs, and the record-pinned tie-break/na semantics — all predeclared above; the 10/21/60/53/-60/-53 inputs, the hlc3-EMA-SMA arithmetic, the 0.015 constant, the zone-gated entries, the ungated opposite-cross closes, the entries-then-closes order, the single-position guard, and the risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, or timing of the source passes.
12. Network limitation disclosed: every formula line above was byte-verified in the pinned GitHub file at commit `b5bba43` (local SHA-256 recorded, re-fetched at the pinned SHA); the canonical LazyBear indicator page verified live the title, author, and open-source identity, while the FMZ page's full code pane was login-walled — the division of evidence is disclosed here, not hidden.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 10/21/60/53/-60/-53 WaveTrend chain / zone-gated entries / ungated opposite-cross closes / atomic reversal / no-stop-no-target posture / two-sided / `1d` BTCUSDT / same-bar-close fills / record-pinned tie-break are frozen.

- F1 — Zone-gate relevance: dropping the zone conjunctions (naked WT1/WT2 cross entries, same closes) must not improve net expectancy; fail ⇒ the ±53 gate adds nothing over the bare cross.
- F2 — Smoothing-length relevance: shortening the average length to `n2 = 14` (same channel length, same gates, same closes) must not improve net expectancy; fail ⇒ the 21-bar second smoothing adds nothing over a faster variant.
- F3 — Short-leg relevance: disabling the short leg (long-only with the same gated entries and crossunder closes) must not improve net expectancy; fail ⇒ two-sided expression adds nothing over the long leg alone.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (derived pin; the code names no market at all). The hlc3 arithmetic ports across perpetual venues without structural change, but venue bar-construction differences touch `high`/`low` and hence `ap` — disclosed above, not hand-waved. The channel/deviation normalization auto-scales in the asset's own price units, so no fixed-pip recalibration is needed across assets — cross-asset behavior differences are still real and unclaimed. The rule is two-sided with no stop leg, so a spot-only deployment expresses the long state and reversal mechanics only to the extent the venue permits shorting — full two-sided expression assumes a futures venue, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no session gating anywhere); decision boundaries are calendar-day bars of the venue feed, disclosed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived market and frame: the code names no market and no timeframe; this record pins `BTCUSDT 1d` (the FMZ corroboration names `BTC_USDT 1h`, not adopted). Cross-market and cross-frame behavior differences are real — the adaptation is disclosed, and this record makes no claim about any other market, frame, or the source's native setting.
- Derived fill timing: the source fills next-bar under Pine defaults with no timing argument; this record executes same-bar-close on `1d` BTCUSDT. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- Derived tie-break and na semantics: the exact-tie arming rule and the flat-window hold outcome are researcher-pinned executable semantics for the derived rule, not source-verbatim Pine claims — disclosed as adaptation 5. A downstream implementation using the opposite tie-break is a different, unpinned rule.
- No source economics: no quantity, commission, or slippage ships anywhere — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- No price stop, no time stop: adverse excursion after entry has no guardrail beyond the opposite cross; a leg whose opposite cross never prints is held indefinitely. This is the prescribed posture, disclosed as a principal risk.
- Whipsaw sensitivity: alternating qualified crosses print repeated full reversals with no flat state to rest in, while mid-zone crosses can only close — a long closed by chop must wait for a fresh zone-born cross to re-enter. The gated-trigger/ungated-exit asymmetry is the prescribed design, disclosed, not smoothed.
- hlc3 venue sensitivity: `high`/`low` definition differences across venues propagate through the whole chain — disclosed above.
- Long seed: the EMA(21)-of-CI chain needs roughly 30 completed closes plus margin; the first 60 `1d` bars are flat by record rule, so early-history signals never enter any evaluation.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Immutable GitHub implementation (pinned executable artifact: `strategys/wavetrend.pine` at commit `b5bba4340d3d537fa68212078e982ce4eb3311d3`, file unchanged since `39a0c43` 2026-02-22, local SHA-256 `5c616a570df66b0e49b13eadf1e1b1d4c610580a59358533a10d95477ec86957`): https://github.com/7b809/logic-gems/blob/main/strategys/wavetrend.pine
- LazyBear canonical WaveTrend indicator page (title, author, and open-source identity verified live via HTTP-200 page record; lineage corroboration only, formulas from the pinned bytes above): https://www.tradingview.com/script/2KE8wTuF-Indicator-WaveTrend-Oscillator-WT/
- FMZ public strategy page (same-construction prose and `Futures_Binance BTC_USDT 1h` stanza verified live; full code pane login-walled, disclosed above): https://www.fmz.com/strategy/449714
- Pine strategy semantics (Pine-default fills, `pyramiding`, `ta.crossover`/`ta.crossunder`/`ta.ema`/`ta.sma` semantics): https://www.tradingview.com/pine-script-reference/v5/
