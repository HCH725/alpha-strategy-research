---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Ehlers InstTrend delayed-line cross reversal two-sided on BTCUSDT 1d bars
created: 2026-10-16
updated: 2026-10-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2006-08
sources:
  - https://traders.com/Documentation/FEEDbk_docs/2006/08/TradersTips/TradersTips.html
  - https://www.fmz.com/lang/en/strategy/436000
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Ehlers InstTrend delayed-line cross reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (official TASC Traders' Tips page, fetched live 2026-10-16 in a real browser session, page title `Traders' Tips - August 2006`):

- Canonical page: https://traders.com/Documentation/FEEDbk_docs/2006/08/TradersTips/TradersTips.html (adopted as `source_as_of: 2006-08`). Editor's note pins lineage: this month's tips implement John Ehlers' article in the same issue, `Modeling The Market = Building Trading Strategies`, and the TradeStation section states the article `describes a process for extracting trend and cyclic elements from market data, then recombining them for trading purposes`. The TradeStation code credit is `--Mark Mills / TradeStation Securities, Inc.`; Ehlers' original authorship of the method is preserved here, never claimed by the page publisher or this record.
- The page's figure caption pins the traded event in substance: `The simulated trades shown in the sample chart above were generated in the EasyLanguage strategy by crosses of instantaneous trend and its two-bar delay line.`
- The complete EasyLanguage strategy `Ehlers-InstTrend` ships verbatim on the page (inputs `Price( MedianPrice )`, `Length( 20 )`, `Delay( 2 )`; recurrence `SMA = Average( Price, Length )`, `Mom = Momentum( Price, Length - 1 )`, `SmoothMom = ( Mom + 2 * Mom[1] + 2 * Mom[2] + Mom[3] ) / 6`, `ITrend = SMA + 0.5 * SmoothMom`; order legs `if ITrend crosses over ITrend[Delay] then Buy next bar market else if ITrend crosses under ITrend[Delay] then Sell short next bar at market`). Text census over the strategy listing: 1 `Buy next bar` / 1 `Sell short next bar` / 0 stop / 0 limit / 0 target / 0 trailing / 0 time-exit / 0 session / 0 volume — the no-stop/no-target always-in-market reversal posture is coded absence, disclosed as source-native, never invented.
- Cross-platform corroboration on the same page: the MetaStock section pins `pr:=MP()` (median price), `len:=20`, `sma:=Mov(pr,len,S)`, `sl:=pr-Ref(pr,-(len-1))`, the identical `(sl+(2*Ref(sl,-1))+(2*Ref(sl,-2))+Ref(sl,-3))/6` smoothing, and `sma+(0.5*ssl)` — i.e. `MedianPrice = (H+L)/2 = hl2`, `Average = simple MA`, `Momentum(Price, Length-1) = Price - Price[19]`. No indicator on the order path reads `open`, `close` as a series, `volume`, or any second timeframe.
- The page ships no performance number for this rule: no return, win rate, profit factor, trade count, date range, or cost table — this record claims no source-reported performance and no reproduced performance.
- Licence and rights: the page is TASC's public Traders' Tips code library (posted for copy-paste into analysis software). This record cites and normalizes the rule and reproduces only single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly three: (1) research market/timeframe BTCUSDT `1d` (the listing pins no symbol, venue, or timeframe — `MedianPrice`/`Length` are its only market-facing inputs); (2) an adopted 100-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 26th completed bar — see Required data); (3) house sizing/capital/costs replacing broker defaults (see Execution assumptions). Fill timing is source-native, not adapted: `next bar market` is modeled as next-open fills on completed `1d` bars. Signal arithmetic, constants, comparisons, order IDs' semantics, two-sided reversal, and the no-stop/no-target posture are unmodified.

Pre-write dedup (2026-10-16): working-tree case-insensitive filename search for `insttrend`, `instantaneous`, `trendline`, `smoothmom`, `ehlers-insttrend`, and `modeling-the-market` returns zero strategy records; content search for `ITrend`, `SmoothMom`, and `ITrend[Delay]` returns zero pool records. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class (see Negative evidence 6). This is a new family member, not a parameter variant: no pool record computes this recurrence or trades this event.

## Economic mechanism

### Source-reported

Trend extraction by cycle-notching plus lag-minimized momentum re-centering (article summary plus code structure): a 20-bar simple average over median price notches out the roughly-20-bar cyclic component, leaving the trend; half of the smoothed 19-bar momentum is added back to pull the lagging average toward the present bar with minimum lag. The trade fires when this lag-minimized trendline crosses its own two-bar-ago copy — a turning-point detector on the trend estimate, riding the new trend side until the estimate turns the other way.

### Research interpretation

Delayed-self-cross reversal on a lag-minimized trend estimate, always in market. Unlike two-MA cross systems (pool EMA-20-50/golden-cross records) that compare two different averages, the trigger here compares one composite line against its own delayed copy — there is only one constructed series, and the event is its self-consistency breaking. Unlike level-cross oscillators (Fisher-zero, StochRSI, CCI records) there is no fixed threshold; unlike the Cyber Cycle record there is no inversion mapping and no escape flat — every cross flips, flat never exists. The `else if` makes the two legs mutually exclusive on every bar by construction, and alternating polarity is structural: a second same-direction cross cannot print without an intervening opposite cross, so the book is single-unit reversal with pyramiding demonstrably irrelevant (no position-cap invention needed).

## Signal

Exact rule as pinned (defaults quoted — inputs unmodified):

- Price input (pinned): `Price = MedianPrice = (H+L)/2 = hl2` (MetaStock `MP()` corroboration on the same page).
- Recurrence (pinned, `Length = 20`): `SMA = Average(Price, 20)`; `Mom = Momentum(Price, 19) = Price - Price[19]`; `SmoothMom = (Mom + 2*Mom[1] + 2*Mom[2] + Mom[3]) / 6`; `ITrend = SMA + 0.5 * SmoothMom`. All lags are non-positive (current and past bars only).
- Entry long (pinned, `Delay = 2`): `ITrend crosses over ITrend[2]` → `Buy next bar at market` — filled at the next `1d` open under this record's source-native timing. Same-bar-close execution is a different, unpinned claim — none is admitted here.
- Entry short (pinned): `ITrend crosses under ITrend[2]` → `Sell short next bar at market` — mirror terms at the next `1d` open. The `else if` admits at most one order per bar; crossover and crossunder of the same pair are mutually exclusive in any case, so no same-bar long/short conflict exists to resolve.
- Exit: the opposite cross reverses the book (close-plus-flip in one transition). No stop, no target, no trailing, no time exit — pinned as written, explicitly none, not invented.
- Direction: symmetric two-sided reversal with no flat state at any time after warmup. A short-side instrument is required for the short legs; on a spot-only venue they are inexpressible and the record would not be the same rule (see Crypto portability).
- Display isolation: the page's figures and indicator-only listings (MetaStock/eSignal/AIQ/Wealth-Lab/AmiBroker and other vendor sections) feed no order condition; order logic reads exactly the two cross predicates above.

## Required data

- Completed `1d` bars of BTCUSDT: `high` and `low` only (via `hl2` and its lags through `Price[19]`; the recurrence additionally reads own-prior `Mom[1..3]` outputs). No `open` series, no `close` series, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (researcher-declared; the listing takes no timeframe input and makes no multi-frame call, so it is single-frame by construction).
- Warmup: `SMA(20)` needs the 20th bar; `Mom` needs `Price[19]` (20th bar); `SmoothMom` needs `Mom[3]` (23rd bar); `ITrend[2]` needs the 25th bar; the cross predicates compare against the prior bar's alignment, so the first evaluable signal sits on the 26th completed bar. Structural minimum is therefore the 26th completed `1d` bar; the adopted warmup is the first 100 completed `1d` bars flat by record rule (predeclared researcher choice). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (researcher-declared; venue/symbol spelling is naming only, never presented as source-native semantics).
- Order timing (source-native): completed-bar decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester — the same next-open path as the admitted `1d` reversal records. No maker-touch, queue, or intrabar-path-dependent fill. With no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity, and the `else-if` legs need no ordering resolution.
- Engine path for `1d` (gate 5, stated plainly): `1d` is a Binance-documented USDT-M kline interval; the derived rule needs only completed `1d` candles (`high`/`low` via `hl2`) on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no volume-definition dependence, no funding/OI/mark-price leg. That is the same single-frame completed-bar plus next-open path as the admitted `1d` records; the SMA/momentum recurrence advances deterministically from known bars, so no hidden lookahead is ever modeled. Anything beyond that path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: broker defaults are replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions here, never presented as source-native behavior. The book is always in market after warmup, so modeled funding accrues continuously — flagged per the house baseline, never zero-claimed; no campaign may claim complete realized-funding performance without a verified implementation.
- Concurrency: single-unit reversal by structural construction (same-direction consecutive crosses are impossible without an intervening opposite cross); repeat signals while positioned cannot occur; the opposite cross reverses in one transition. Re-entry is immediate on the next qualifying cross (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

With exact provenance (read end to end this cycle): the TASC page ships the complete rule (inputs, recurrence, both next-bar-market order legs, the two-bar-delay caption, the Mark Mills credit, and the Ehlers-article lineage note). It ships zero performance numbers for this rule: no return, win rate, trade count, date range, or cost table — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden risk layer: the strategy listing contains no stop, limit, target, trailing, or time-exit token — the sole position-closing path is the opposite-cross reversal. The absence is coded (the listing ends at the `Sell short` leg), disclosed in Signal for the reviewer rather than upgraded into a source claim.
2. Legs mutually exclusive every bar by listing construction (`if ... else if` over crossover/crossunder of the same pair) — no single bar can satisfy more than one order leg.
3. Reversal-only conditionality, admitted plainly: a position exits only on the opposite cross. A market that trends with the position never exits until a counter-cross prints — there is no target to bank a run, and chop around the delayed line compounds consecutive reversal losses plus continuous modeled funding. This is the coded trade, disclosed, not a tunable parameter here.
4. Boundary ties hold their side: an exactly-equal print (`ITrend == ITrend[2]`, or equality on the prior-bar alignment) is neither a cross-over nor a cross-under, so no order fires and the book carries the prior state; a zero-range `hl2` window still evaluates arithmetically (no division anywhere except the constant 6); warmup bars are flat by record rule.
5. Sibling strategy fenced, never adopted: the same page's `Ehlers-StoRSIModel` (StochasticRSI transform of the model with its own `Trigger = 0.05 + 0.9 * StochRSI[1]` cross rule) and the model-indicator listings are different, unpinned rules — a reviewer must not graft any of their legs (RSI lengths, stochastic window, trigger arithmetic) onto this record.
6. Overlap fences, admitted plainly: pool `cyber-cycle-signal-self-cross` trades an inverted self-cross of an EMA-of-cycle line with an 8-bar open-loss escape to flat (different filter, inverted mapping, escape-flat book); pool `mama-fama-hilbert-state-flip` trades adaptive MAMA/FAMA Hilbert state (different construction, no delayed-line event); pool `bandpass-filter-reversed-cycle-sign` trades the sign of a cosine-derived resonator (different filter, sign event); pool `ehlers-decycler-oscillator-cross` trades a fast-slow Decycler oscillator cross long-flat (different construction, one-sided book); pool `ehlers-sinewave-phase-cross-flip` trades Hilbert Sine/LeadSine phase crosses (different waves, different event); pool `laguerre-rsi-cu-cd-cross` and `fisher-zero-cross` trade different transforms against different events; pool `ema-20-50-cross`/`golden-cross-sma` compare two distinct moving averages (different event — no composite line, no self-delay); pool `dpo-ema-crossover` crosses a detrended oscillator against an EMA (different construction). Shared `Ehlers`/`cross`/`SMA` vocabulary is not shared signal.
7. No hidden variants admitted: `close`-input, the FMZ 2nd-order IT variant (`a = 0.07` filter with price-vs-`lag = 2*it - it[2]` trigger — a different book construction from `Cybernetic Analysis`, fenced as fence-source, never mixed into this recurrence), any retuned `Length`/`Delay`, any stop/target/filter/cooldown, any other frame, fill, or single-side gating is a different, unpinned rule. A reviewer must not pick among these to rescue or reshape the record.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `hl2` input / `Length = 20` / `Delay = 2` / `(1,2,2,1)/6` weights / `0.5` momentum loading / delayed-self-cross predicates / flip-only always-in-market book / next-open fills / no-stop posture / `1d` BTCUSDT are frozen.

- F1 — Delay relevance: a `Delay = 1` twin (same recurrence, one-bar delay) must not improve net expectancy; fail ⇒ the two-bar delay adds nothing over the one-bar self-cross.
- F2 — Momentum relevance: a raw-SMA twin (`ITrend := SMA(Price, 20)` crossed against its own 2-bar delay — momentum term deleted, same book and timing) must not improve net expectancy; fail ⇒ the Ehlers momentum correction adds nothing over its own average.
- F3 — Book relevance: a long-flat twin (long legs as pinned, short crosses exit to flat instead of flipping — same grid, fills, warmup) must not improve net expectancy; fail ⇒ the always-in-market short side destroys value and the flip derivation is the wrong port.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (declared port of a symbol-free listing). The rule reads completed daily bars only, so no pit-session, gap, or roll logic ports. The `hl2` input and fixed-length arithmetic need no recalibration across assets, yet crypto's 24/7 trend persistence vs the listing's roughly-20-bar cycle prior is a real mismatch — unclaimed and undisguised (see Negative evidence 3). The rule is two-sided reversal, so a spot-only deployment expresses only the long legs while short legs stay venue-gated (never silently converted) — a spot-only variant would be a different, unpinned claim. Funding accrues continuously by book design and is modeled, never zero-claimed. No warmup history beyond 100 daily bars is consumed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- No price stop, no time stop, no flat leg: adverse excursion after a flip has no guardrail before the counter-cross, by the prescribed listing design — the record's principal risk.
- Next-open lag: the cross is detected at the completed-bar close and filled at the next open, systematically one bar late on straight-line turns.
- Always-in-market economics: every chop cross pays a full round trip plus continuous modeled funding; flat markets are the worst case, disclosed, not tuned away.
- Single-venue daily port: symbol-free provenance vs 24/7 BTCUSDT daily execution is a declared derivation with unclaimed portability residual (prints, fees, funding, margin mechanics beyond the house model).
- Performance evidence is absent: no source reports a number for this exact rule, and none is claimed here.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior and never part of this admission — no Safety-Order/DCA event is admitted in this record's version. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- TASC Traders' Tips August 2006, TRADESTATION: MODELING THE MARKET (Ehlers-InstTrend EasyLanguage listing, two-bar-delay caption, MetaStock cross-corroboration, Ehlers-article lineage — read end to end in a real browser session 2026-10-16): https://traders.com/Documentation/FEEDbk_docs/2006/08/TradersTips/TradersTips.html
- FMZ public strategy page, Ehlers Instantaneous Trendline Strategy by ChaoZhang (2nd-order `a = 0.07` filter with price-vs-lag trigger — different book construction, fenced and never adopted; page fetched live 2026-10-16, HTTP 200, 803123 bytes): https://www.fmz.com/lang/en/strategy/436000
