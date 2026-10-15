---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: VZO tactic-1 band-recross reversal two-sided on BTCUSDT 1d bars
created: 2026-10-15
updated: 2026-10-15
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2009
sources:
  - https://www.ifta.org/assets/docs/d_ifta_journal_09.pdf
  - https://www.tradingview.com/script/P6bSDkjh-Volume-Zone-Oscillator-VZO/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# VZO tactic-1 band-recross reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (verified 2026-10-15):

- Canonical paper: IFTA Journal 2009 edition, `Volume Zone Oscillator (VZO)` by `Waleed Aly Khalil` (table of contents `page 18`; article journal pages 18–32; adopted as `source_as_of: 2009`). Fetched live over HTTPS during this cycle (HTTP 200, 4129874 bytes, 64 PDF pages). The VZO article text (abstract through conclusion, tables 1–8) was extracted and read verbatim; every quotation below is byte-present in that file. The paper ships the full construction (signed-volume rule, EMA smoothing pair, ratio formula, default period, band levels, three named tactics, two 5-year backtest tables for tactic 1, advantages/disadvantages) — quoted for gate evidence. This record claims no crypto performance and no reproduced performance.
- Pinned construction, verbatim: `The formula depends on only one condition; if the close of today is higher than the close of yesterday, the volume will be considered bullish, otherwise it will be bearish.` AmiBroker code line: `R = IIf(C > Ref(C,-1), V, -V)` — equal closes fall to the `-V` (bearish) leg, deterministic, no tie-break needed. `VP = EMA(R, period)`; `TV = EMA(V, period)`; `VZO = 100 X (VP/TV)`; `The default period for the VZO is 14`; scale `-100` to `+100`.
- Pinned levels, verbatim: `The oscillators' upper and lower boundaries (overbought/oversold) are positive and negative 40.` `The 60/-60 level actually marks extreme optimism or pessimism.` `The zero line demonstrates equilibrium between bulls and bears.` `The VZO tends to fluctuate between -40 and +40, the crossing of each creates buy/sell signals.`
- Pinned tactic-1 trigger, verbatim (Part Five §5.1): `giving a buy signal crossing up -40 and a sell signal crossing down below the 40 level` and `This tactic is considered to be ideal for sideways trends; during those periods, the VZO will tend to fluctuate between -40 and 40.`
- Two-sided permission, verbatim (§6.1 Advantages): `All sell signals can also be used to short, and buy signals to cover.`
- TradingView lineage (open-source confirmation only — rule read in the paper, never retyped from here): `Volume Zone Oscillator (VZO)` by `Beardy_Fred`, page carries the `OPEN-SOURCE SCRIPT` badge, fetched live during this cycle (HTTP 200, 333881 bytes of landing HTML).

Licence and rights: this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly five: (1) market pin `BTCUSDT` on Binance futures with the source-native daily frame kept (the paper trades daily stock bars — frame-faithful, venue transfer plus symbol spelling, futures volume definition, and futures short permission disclosed here, never presented as source-native); (2) core-tactic-only pin (the paper's tested variant adds a `15`/`-5` confirmation overlay, an `ADX() below 18` sideways gate whose ADX length is unprinted, and a 15-day-average-volume-above-25000-shares stock universe filter — all stock-specific and partly underspecified, none carried into this record, disclosed, never silently dropped); (3) same-bar-close fills on completed `1d` bars; (4) an adopted 100-bar warmup with pre-warmup bars flat by record rule plus a pinned EMA seed convention (the paper's AmiBroker EMA seed is undisclosed — see Required data); (5) house sizing/capital/costs replacing the absent source economics (zero cost assumption — recorded as absent, never as zero-cost evidence; see Execution assumptions). The `IIf(C > Ref(C,-1), V, -V)` signed-volume rule, the `EMA(R,14)`/`EMA(V,14)` pair, the `100 × VP/TV` ratio, the `±40` bands, the cross-up-`-40` buy / cross-down-`+40` sell pair, the alternating always-in posture, and the no-stop/no-target/no-flat stance are source-native and unmodified.

Pre-write dedup (2026-10-15): working-tree case-insensitive searches for word-boundary `vzo`, `volume zone` (signal use), and the canonical PDF filename return zero strategy records using this source, author, indicator, or construction; `-40`/`+40` appear in the pool only as return percentages or DOI strings, never as oscillator band levels. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `obv-ema-crossover-trend-two-sided-btcusdt-1d` trades an unbounded cumulative OBV total against its own EMA6/24 cross (no ratio, no bands); `pvt-ema-crossover-trend-two-sided-btcusdt-1d` trades a cumulative price-relative PVT total against its EMA cross (no signed-volume EMA ratio, no fixed bands); `cmf-velocity-zero-cross`, `force-index-100-zero-state`, `klinger-volume-oscillator-trigger-flip` each gate orders on different volume-pressure arithmetic (accumulation/distribution weighting, raw force, KVO trigger-line flips — none computes `100 × EMA(±V)/EMA(V)` and none recrosses fixed `±40` bands). No pool record trades a bounded signed-volume EMA ratio against fixed band recrosses. Shared `volume` input is not shared signal.

## Economic mechanism

### Source-reported

Signed-volume zone acceptance with band-recross reversal discipline: each bar's volume is signed bullish when its close rises versus the prior close and bearish otherwise (equal closes bearish by the printed `IIf`), both legs smoothed by same-period EMAs, and their ratio scaled to `±100` so the print reads which zone the volume sits in — bulls' or bears'. Crossing up `-40` means bear-side volume pressure has released enough to accept the long side; crossing down `+40` means bull-side pressure has released enough to accept the short side. The design bets that volume-zone migration leads price: the oscillator moves on signed participation, not on price action (`VZO does not move on the price action, but on volume`), so it can trade uptrend, downtrend, or sideways while price-based triggers still wait. There is no stop, no target, no flat state by design after the first signal — the opposite band recross is the exit (`The oscillator provides no price target`, fenced as prescribed posture in Negative evidence).

### Research interpretation

Single-series bounded-oscillator system, two-sided, always-in-position after the first signal, with the bands as the only trigger. Unlike cumulative systems (OBV, PVT) whose totals drift without bounds and need a second series to cross, this rule normalizes participation into a fixed `±100` scale so two constant levels (`-40`, `+40`) suffice forever — no moving reference, no re-fit, no second line. Unlike zero-line flippers, the trigger sits away from equilibrium: the `-40…+40` interior is a no-trade corridor, so chop around zero prints nothing and only a certified zone exit fires. Unlike the pool's EMA-cross volume records, nothing here crosses anything — the signal is a level recross by one series, and the exit is the mirror recross, which makes every holding period exactly one zone-to-opposite-zone migration. The price of the always-in posture is indefinite adverse rides plus whipsaw pairs when the print straddles a band edge: a leg whose opposite recross never prints is held forever, and the paper itself flags zero-straddling whipsaw as the known failure mode. The bet is on signed-volume persistence, not on any price pattern, second series, calendar effect, or volatility read.

## Signal

Exact rule as pinned (all inputs frozen — any other value is a different, unpinned rule):

- Declarations (derived): single-position state machine over `BTCUSDT 1d` with same-bar-close execution and house sizing/costs (see Execution assumptions). At most one open leg; state ∈ {flat, long, short}; flat exists only before the first signal and under the warmup rule.
- Signed volume, pinned verbatim at defaults (`period = 14`): with `C(t)` close and `V(t)` volume of completed bar `t`: `R(t) = +V(t)` iff `C(t) > C(t-1)`, else `−V(t)` (equal closes take the bearish leg — source-printed, never a researcher tie-break).
- Indicator, pinned verbatim: `VP(t) = EMA(R, 14)(t)`; `TV(t) = EMA(V, 14)(t)`; `VZO(t) = 100 × VP(t) / TV(t)`. EMA convention (predeclared researcher choice — the paper's AmiBroker seed is undisclosed): classic exponential with `α = 2/(14+1)`, seeded by the SMA of the first 14 values of each leg; the 100-bar warmup absorbs all seed contamination structurally (see Required data). `TV(t)` is strictly positive on any real volume feed, so the ratio is always defined — no divide-by-zero branch exists in practice (fenced in Negative evidence).
- Entry long: on bar `t` with `VZO(t−1) < −40` and `VZO(t) ≥ −40` (crossing up `-40`, landing inclusive; from flat: open long; from short: atomic reversal — close short plus open long as a single reversal event). Refires of the long state while already long are no-ops (no pyramiding — explicitly none, not invented).
- Entry short: mirror on `VZO(t−1) > +40` and `VZO(t) ≤ +40` (crossing down below the `40` level).
- Exits: the opposite recross only (long exits exactly when the short trigger prints and vice versa). No stop, no target, no trailing, no time exit, no cooldown — pinned as written (the tactics name no stop/target/trailing/time leg anywhere, and §6.2 confirms `The oscillator provides no price target`), explicitly none, not invented. There is no flat path after the first signal at all — flat is reachable only pre-signal and under warmup.
- Direction: two-sided with an explicit pre-first-signal flat state (plus the 100-bar warmup flat by record rule). The paper's `All sell signals can also be used to short, and buy signals to cover` prescribes both sides; a long-only or short-only reading would contradict it.

## Required data

- Completed `1d` bars of BTCUSDT: `close` (sign rule) and `volume` (both legs) only — Binance USDT-M futures contract volume by record pin (see Limitations). No `open`, no `high`, no `low`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (frame-faithful to the paper's daily bars; the construction references no other frame, no multi-timeframe input, no `security`-style call of any kind — single-frame by construction).
- Warmup: the binding seeds are the two `EMA(·, 14)` legs (first fully-seeded values need 14 completed bars each under the pinned SMA-seed convention) plus cross-comparison margin. The adopted warmup is the first 100 completed `1d` bars flat by record rule (predeclared researcher choice — covers both EMA seeds plus the `t−1` comparison reach with wide margin; the seed branch never fires on a traded bar). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Each bar's close/volume enter the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (frame-faithful `1d`; venue choice, symbol spelling, futures-volume definition, and short permission disclosed in Provenance, never presented as source claims).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity, and each trigger reads only completed closes/volumes, so each bar's outcome is a single deterministic event (hold, open, or atomic reversal).
- Sizing/capital/costs: the source ships no portable economics (zero commission/quantity assumption — recorded as absent economics, never as zero-cost evidence) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: single-position machine — at most one open leg; same-state bars while positioned are no-ops; the opposite recross reverses in full (one atomic event); re-entry is allowed on the next fresh recross after any close (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The paper ships the full construction (`R = IIf(C > Ref(C,-1), V, -V)`, `VP = EMA(R, period)`, `TV = EMA(V, period)`, `VZO = 100 X (VP/TV)`, default period `14`), the level map (`±40` boundaries, `±60` extremes, zero equilibrium), the tactic-1 trigger pair (cross up `-40` buy, cross down below `+40` sell, sideways ideal), the two-sided permission (`All sell signals can also be used to short, and buy signals to cover`), and two 5-year tactic-1 backtest tables (Egypt 01/01/2003–01/01/2008: `122` trades, `59.84%` winners, profit factor `2.99`, max trade % drawdown `-23.84%`, exposure `71.47%`; NYSE same window: `169` trades, `52.66%` winners, profit factor `2.12`, max trade % drawdown `-12.84%`, exposure `97.22%`, trade Sharpe `1.32`) — quoted in Provenance. Scope fence, stated plainly: those tables test the paper's filtered stock implementation (with the `15`/`-5` confirmation overlay, the `ADX() below 18` sideways gate, and the 25000-share universe filter), not the bare pinned core — so this record carries their numbers as source-reported context only and claims no performance for the pinned core and no reproduced performance of any kind.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Tested-variant scope fence, admitted plainly: the paper's 5-year numbers belong to an implementation that buys on crossings above `15` (not zero, as bullish confirmation), sells on crossings beneath `-5`, gates sideways by `ADX() below 18` (ADX length unprinted — unverifiable), and restricts the universe to 15-day-average-volume-above-25000-shares stocks. None of those four overlays is carried into the pinned core (stock-specific or underspecified — disclosed in Provenance). The pinned bare `±40` recross pair is therefore performance-unclaimed by construction; carrying the tables' expectancy onto it would be fabrication.
2. No hidden exits or risk layer: the three tactics name no stop, no target, no trailing, no time exit anywhere, and §6.2 confirms `The oscillator provides no price target` — the no-stop/no-target posture is prescribed, explicitly none, never hidden. Every adverse excursion is held to the opposite band recross.
3. Whipsaw mode fenced with the paper's own words: `Sometimes the VZO fluctuates around the zero level causing whipsaws` — and band-edge straddles print repeated reversal pairs with no flat state to rest in, by the prescribed always-in design. The interior corridor only silences zero chop; it does not silence edge chop.
4. Trigger exclusivity fenced: the long trigger requires `VZO(t−1) < −40` and the short trigger requires `VZO(t−1) > +40` — no prior print satisfies both, so no bar fires both transitions and no priority rule is needed or invented. (A single bar can traverse the whole corridor, but then exactly one leg's prior-side condition holds.)
5. Exact-touch determinism fenced: landings exactly on `±40` count as recrosses by the pinned `≥`/`≤` comparisons (measure-zero on continuous prints — disclosed, not oversold as tolerance).
6. Equal-close leg fenced: `C(t) == C(t−1)` takes `−V(t)` by the printed `IIf(C > Ref(C,-1), V, -V)` — no bar leaves `R(t)` undefined, no tie-break invented.
7. Ratio-definedness fenced: `TV(t)` is an EMA of non-negative volumes, strictly positive on any real feed — the `VP/TV` division has no zero-denominator branch in practice; all-flat zero-volume droughts (all `V = 0`) would print `0/0 = na` and hold the prior state deterministically, unreachable on traded BTCUSDT and fenced only for implementation completeness.
8. No future leakage in the stack, stated plainly: at decision bar `t`, the sign rule reads closes `t−1…t`, both EMAs accumulate bars `≤ t`, and each trigger compares prints `t−1…t` — every input is complete at bar `t`'s close. No multi-frame read, no negative index, no full-sample normalization, no `islast`-gated repainting path, no calendar read at all. The seed branch is fenced out of every traded bar by the 100-bar warmup.
9. OBV/PVT-family overlap fence, admitted plainly: the pool's OBV-EMA record trades an unbounded cumulative total against its own EMA cross and the PVT-EMA record trades a cumulative price-relative total against its EMA cross — both need a second series and have no fixed bands. This record normalizes signed participation into a bounded `±100` ratio and recrosses two constant levels with no second series. Shared `volume` input is not shared signal.
10. Two-sided posture provably complete: symmetric `−40`-recross long / `+40`-recross short legs with symmetric atomic-reversal exits under the paper's explicit short permission — no third direction exists, and a long-only reading would contradict the printed sell-to-short leg.
11. Derivation boundary fenced: the only non-source-native behaviors in this record are the `BTCUSDT` futures market pin with the source-native daily frame kept, the core-only tactic scope, same-bar-close fills, the adopted 100-bar warmup with record-rule pre-warmup flat and the pinned EMA seed convention, and house sizing/costs — all predeclared above; the signed-volume rule, the EMA pair, the 14 default, the ratio formula, the `±40` bands, the recross triggers, the atomic reversal, the single-position guards, and the risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, parameter set, confirmation overlay, or timing of the source passes.
12. Network limitation disclosed: every formula, level, tactic, table, and disadvantage line above was byte-verified in the fetched IFTA PDF (4129874 bytes, 64 pages, HTTP 200); the TradingView page verified live the script title, the `Beardy_Fred` author token, and the open-source badge — the division of evidence is disclosed here, not hidden.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `IIf(C > Ref(C,-1), V, -V)` signing / `EMA(R,14)`+`EMA(V,14)` pair / `100 × VP/TV` ratio / `±40` recross pair with hold / atomic reversal / no-stop-no-target posture / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Band relevance: narrowing both bands to `±20` (same period, same state machine, same reversal handling) must not improve net expectancy; fail ⇒ the `±40` zone width adds nothing over a hair-trigger variant.
- F2 — Period relevance: shortening the smoothing pair to `period = 7` (same bands, same latch-free recross, same state machine) must not improve net expectancy; fail ⇒ the 14-bar signed-volume memory adds nothing over a fast variant.
- F3 — Posture relevance: exiting to flat on the opposite recross instead of atomic reversal (same entries, same bands, flat between migrations) must not improve net expectancy; fail ⇒ the always-in alternation adds nothing over a flat-resting variant.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (frame-faithful `1d`; venue transfer disclosed). The rule reads only completed daily closes and futures contract volumes, so no high/low/open definition differences can touch any order-gating line — but spot-vs-perp volume series differ structurally, so the futures-volume pin is load-bearing and disclosed. The ratio is unit-free and the bands are fixed constants, so no fixed-pip recalibration is needed across assets — cross-asset behavior differences are still real and unclaimed. The rule is two-sided with no stop leg, so a spot-only deployment expresses the long state and reversal mechanics only to the extent the venue permits shorting — full two-sided expression assumes a futures venue, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no session gating anywhere); decision boundaries are calendar-day bars of the venue feed, disclosed. The paper's own forex warning (`Not applicable to trade FOREX, because the volume data is delayed`) does not transfer: venue-native perp volume is the defined input here, not a delayed proxy. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived market pin: the paper trades daily stock bars; this record pins `BTCUSDT` futures `1d` with futures contract volume. Cross-market and spot-vs-perp volume behavior differences are real — the venue transfer is disclosed, and this record makes no claim about any other market or the paper's native venue.
- Untested bare core: the only source-reported numbers belong to the filtered stock-tested variant (see Evidence scope fence); the pinned core carries no expectancy claim until downstream research measures it.
- No source economics: the paper ships no commission, sizing, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- No price stop, no time stop: adverse excursion after entry has no guardrail beyond the opposite band recross; a leg whose opposite trigger never prints is held indefinitely. This is the prescribed posture, disclosed as a principal risk.
- Whipsaw sensitivity: band-edge straddles print repeated reversal pairs with no flat state to rest in, while interior zero chop is silenced only by corridor, not by smoothing. The recross construction is the prescribed design, disclosed, not smoothed.
- Volume-definition sensitivity: contract-volume prints (rolls, venue aggregation, anomalous prints) flow straight into both EMA legs; a venue that cannot supply trustworthy per-bar volume cannot trade the pinned rule.
- EMA seed convention: the paper's AmiBroker EMA seed is undisclosed; this record pins the SMA-of-first-14 seed by researcher choice with the first 100 `1d` bars flat, so early-history signals never enter any evaluation.
- Warmup seed: both EMA legs need 14 completed bars plus comparison margin; the adopted 100-bar warmup absorbs this structurally with wide margin.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- IFTA Journal 2009 edition, Waleed Aly Khalil, Volume Zone Oscillator (VZO), journal pp. 18–32 (formula, levels, tactics, Tables 1–2, advantages/disadvantages verified live in the fetched PDF during this cycle; zero crypto claims): https://www.ifta.org/assets/docs/d_ifta_journal_09.pdf
- TradingView Beardy_Fred lineage (title/author/open-source-badge confirmation only): https://www.tradingview.com/script/P6bSDkjh-Volume-Zone-Oscillator-VZO/
