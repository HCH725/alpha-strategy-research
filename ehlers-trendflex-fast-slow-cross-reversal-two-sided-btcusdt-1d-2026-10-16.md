---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Ehlers Trendflex fast-slow cross reversal two-sided on BTCUSDT 1d bars
created: 2026-10-16
updated: 2026-10-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2020-02
sources:
  - https://traders.com/Documentation/FEEDbk_docs/2020/02/TradersTips.html
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Ehlers Trendflex fast-slow cross reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (official TASC Traders' Tips page, fetched live 2026-10-16 in a real browser session, page title `TRADERS' TIPS - FEBRUARY 2020`):

- Canonical page: https://traders.com/Documentation/FEEDbk_docs/2020/02/TradersTips.html (adopted as `source_as_of: 2020-02`). The page header pins lineage: this month's tips implement John Ehlers' article in the same issue, `Reflex: A New Zero-Lag Indicator`, and the TradeStation section states Ehlers `introduces a new averaging indicator that he has designed with reducing lag in mind` and that `Ehlers provides TradeStation EasyLanguage code for the indicators`, while the page itself provides `EasyLanguage functions for the reflex and trendflex indicators that you can use in developing your own indicators and strategies` plus `an example strategy to help you get started`.
- The complete EasyLanguage function `_TrendFlex` ships verbatim on the page (input `Length( numericsimple )`; SuperSmoother prefilter `a1 = ExpValue(-1.414*3.14159/(.5*Length))`, `b1 = 2*a1*Cosine(1.414*180/(.5*Length))`, `c2 = b1`, `c3 = -a1*a1`, `c1 = 1-c2-c3`, `Filt = c1*(Close+Close[1])/2 + c2*Filt[1] + c3*Filt[2]`; accumulation `Sum = Sum + Filt - Filt[count]` for `count = 1 to Length`, `Sum = Sum/Length`; RMS normalization `MS = .04*Sum*Sum + .96*MS[1]`, `Trendflex = Sum/SquareRoot(MS)` guarded by `if MS <> 0`).
- The complete EasyLanguage strategy `Trendflex Cross` ships verbatim on the same page (inputs `FastLength( 20 )`, `SlowLength( 50 )`; `FastTF = _TrendFlex( FastLength )`, `SlowTF = _TrendFlex( SlowLength )`; order legs `if FastTF crosses over SlowTF then Buy next bar at Market else if FastTF crosses under SlowTF then SellShort next bar at Market`). Text census over the strategy listing: 1 `Buy next bar` / 1 `SellShort next bar` / 0 stop / 0 limit / 0 target / 0 trailing / 0 time-exit / 0 session / 0 volume — the no-stop/no-target always-in-market reversal posture is coded absence, disclosed as source-native, never invented.
- Source timeframe context: the TradeStation sample chart is a daily chart of AAPL (`FIGURE 1 ... applied on a daily TradeStation chart of AAPL`); the eSignal section corroborates daily-bar context (`plotted on a daily chart of SPY`) and the `Length` default of 20. The listing itself takes no symbol, venue, or timeframe input — lengths 20/50 are its only horizon inputs.
- The page ships no performance number for this rule: no return, win rate, profit factor, trade count, date range, or cost table — this record claims no source-reported performance and no reproduced performance.
- Licence and rights: the page is TASC's public Traders' Tips code library (posted for copy-paste into analysis software). This record cites and normalizes the rule and reproduces only single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly three: (1) research market/timeframe BTCUSDT `1d` (the listing pins no symbol or venue; its daily-bar context ports 1:1 to daily crypto bars); (2) an adopted 100-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 52nd completed bar — see Required data); (3) house sizing/capital/costs replacing broker defaults (see Execution assumptions). Fill timing is source-native, not adapted: `next bar at Market` is modeled as next-open fills on completed `1d` bars. Signal arithmetic, constants, comparisons, order-leg semantics, two-sided reversal, and the no-stop/no-target posture are unmodified.

Pre-write dedup (2026-10-16): working-tree case-insensitive filename search for `reflex`, `trendflex`, `trend-flex`, `zero-lag`, and `ehlers-trendflex` returns zero strategy records; content search for `TrendFlex`, `FastTF`, and `SlowTF` returns zero pool records. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class (see Negative evidence 6). This is a new family member, not a parameter variant: no pool record computes this recurrence or trades this event.

## Economic mechanism

### Source-reported

Zero-lag averaging split into cycle vs trend paths (article summary plus code structure): prices are gently pre-smoothed in a SuperSmoother, then each bar's deviation from its own trailing window is summed and normalized by trailing root-mean-square — a z-score-like oscillator with the smoother's lag removed by construction. The `Reflex` sibling synchronizes with the cycle component (slope-projected reference); the `Trendflex` sibling retains the trend component (flat reference). The example strategy trades the fast (20) Trendflex crossing the slow (50) one — a trend-regime flip detector: when the short-horizon trend estimate overtakes the long-horizon one, ride the new side until the estimates re-cross.

### Research interpretation

Fast-slow cross reversal on two RMS-normalized zero-lag trend estimators, always in market. Unlike the InstTrend record (one composite line vs its own 2-bar-ago copy — a delayed self-cross), the event here compares two different oscillators of different horizons (20 vs 50). Unlike EMA-difference systems (pool MACD/PPO/TSI records) there is no exponential moving average anywhere — the construction is SuperSmoother prefilter plus window-sum plus trailing-RMS normalization with fixed 20/50 horizons. Unlike level-cross oscillators (Fisher-zero, StochRSI, CCI records) there is no fixed threshold; unlike the Cyber Cycle record there is no inversion mapping and no escape flat — every cross flips, flat never exists. The `else if` makes the two legs mutually exclusive on every bar by construction, and alternating polarity is structural: a second same-direction cross cannot print without an intervening opposite cross, so the book is single-unit reversal with pyramiding demonstrably irrelevant (no position-cap invention needed).

## Signal

Exact rule as pinned (defaults quoted — inputs unmodified):

- Price input (pinned): `Close` series only, via `(Close + Close[1]) / 2` into the SuperSmoother. No `open`, `high`, `low`, `volume`, or second timeframe on the order path.
- Recurrence (pinned, per `Length`): `a1 = ExpValue(-1.414*3.14159/(.5*Length))`; `b1 = 2*a1*Cosine(1.414*180/(.5*Length))`; `c2 = b1`; `c3 = -a1*a1`; `c1 = 1-c2-c3`; `Filt = c1*(Close+Close[1])/2 + c2*Filt[1] + c3*Filt[2]`; `Sum = (1/Length)*Σ(Filt - Filt[count])` for `count = 1..Length`; `MS = .04*Sum*Sum + .96*MS[1]`; `Trendflex = Sum/SquareRoot(MS)` (guarded `if MS <> 0`). All lags are non-positive (current and past bars only).
- Fast leg (pinned): `FastTF = _TrendFlex(20)`. Slow leg (pinned): `SlowTF = _TrendFlex(50)`.
- Entry long (pinned): `FastTF crosses over SlowTF` → `Buy next bar at Market` — filled at the next `1d` open under this record's source-native timing. Same-bar-close execution is a different, unpinned claim — none is admitted here.
- Entry short (pinned): `FastTF crosses under SlowTF` → `SellShort next bar at Market` — mirror terms at the next `1d` open. The `else if` admits at most one order per bar; crossover and crossunder of the same pair are mutually exclusive in any case, so no same-bar long/short conflict exists to resolve.
- Exit: the opposite cross reverses the book (close-plus-flip in one transition). No stop, no target, no trailing, no time exit — pinned as written, explicitly none, not invented.
- Direction: symmetric two-sided reversal with no flat state at any time after warmup. A short-side instrument is required for the short legs; on a spot-only venue they are inexpressible and the record would not be the same rule (see Crypto portability).
- Display isolation: the page's `Trendflex Cross` indicator listing (`Plot1( FastTF - SlowTF )`, `Plot2( 0 )`) and all vendor indicator ports (eSignal/Wealth-Lab/NeuroShell/NinjaTrader/TradersStudio/Excel/ThinkorSwim/Quantacula sections) feed no order condition; order logic reads exactly the two cross predicates above.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (via `(Close+Close[1])/2` and its lags through `Filt[50]` on the slow leg; the recurrence additionally reads own-prior `Filt[1..2]` outputs and trailing `MS[1]`). No `open`, `high`, `low`, `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (researcher-declared; the listing takes no timeframe input and makes no multi-frame call, so it is single-frame by construction; source context is daily bars).
- Warmup: the slow leg reads `Filt[50]`, so filter history is complete on the 51st bar; the cross predicates compare against the prior bar's alignment, so the first evaluable signal sits on the 52nd completed bar. Structural minimum is therefore the 52nd completed `1d` bar; the adopted warmup is the first 100 completed `1d` bars flat by record rule (predeclared researcher choice, covering SuperSmoother seeding and `MS` RMS-settle transients). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (researcher-declared; venue/symbol spelling is naming only, never presented as source-native semantics).
- Order timing (source-native): completed-bar decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester — the same next-open path as the admitted `1d` reversal records. No maker-touch, queue, or intrabar-path-dependent fill. With no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity, and the `else-if` legs need no ordering resolution.
- Engine path for `1d` (gate 5, stated plainly): `1d` is a Binance-documented USDT-M kline interval; the derived rule needs only completed `1d` candles (`close` series) on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no volume-definition dependence, no funding/OI/mark-price leg. That is the same single-frame completed-bar plus next-open path as the admitted `1d` records; the SuperSmoother/window-sum recurrence advances deterministically from known bars, so no hidden lookahead is ever modeled. Anything beyond that path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: broker defaults are replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions here, never presented as source-native behavior. The book is always in market after warmup, so modeled funding accrues continuously — flagged per the house baseline, never zero-claimed; no campaign may claim complete realized-funding performance without a verified implementation.
- Concurrency: single-unit reversal by structural construction (same-direction consecutive crosses are impossible without an intervening opposite cross); repeat signals while positioned cannot occur; the opposite cross reverses in one transition. Re-entry is immediate on the next qualifying cross (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

With exact provenance (read end to end this cycle): the TASC page ships the complete rule (both EasyLanguage functions, the `Trendflex Cross` indicator and strategy listings with 20/50 defaults, both next-bar-market order legs, the daily-AAPL sample-chart context, the Ehlers-article lineage note). It ships zero performance numbers for this rule: no return, win rate, trade count, date range, or cost table — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden risk layer: the strategy listing contains no stop, limit, target, trailing, or time-exit token — the sole position-closing path is the opposite-cross reversal. The absence is coded (the listing ends at the `SellShort` leg), disclosed in Signal for the reviewer rather than upgraded into a source claim.
2. Legs mutually exclusive every bar by listing construction (`if ... else if` over crossover/crossunder of the same pair) — no single bar can satisfy more than one order leg.
3. Reversal-only conditionality, admitted plainly: a position exits only on the opposite cross. A market that trends with the position never exits until a counter-cross prints — there is no target to bank a run, and chop around the fast/slow alignment compounds consecutive reversal losses plus continuous modeled funding. This is the coded trade, disclosed, not a tunable parameter here.
4. Boundary ties hold their side: an exactly-equal print (`FastTF == SlowTF`, or equality on the prior-bar alignment) is neither a cross-over nor a cross-under, so no order fires and the book carries the prior state; the `MS <> 0` guard pins the only division; warmup bars are flat by record rule.
5. Sibling function fenced, never adopted: the same page's `_Reflex` (slope-projected `Filt + count*Slope` reference — a different oscillator) and the `ReflexIndicators.efs`/vendor indicator ports are different, unpinned rules for the order path — a reviewer must not graft any Reflex leg, any `Length` other than 20/50, or any zero-line trigger onto this record.
6. Overlap fences, admitted plainly: pool `ehlers-insttrend-delayed-cross-reversal` trades one composite line against its own 2-bar-ago copy (different event — delayed self-cross, single series); pool `cyber-cycle-signal-self-cross` trades an inverted self-cross of an EMA-of-cycle line with an 8-bar open-loss escape to flat (different filter, inverted mapping, escape-flat book); pool `mama-fama-hilbert-state-flip` trades adaptive MAMA/FAMA Hilbert state (different construction, no fast-slow cross); pool `bandpass-filter-reversed-cycle-sign` trades the sign of a cosine-derived resonator (different filter, sign event); pool `ehlers-decycler-oscillator-cross` trades a fast-slow Decycler oscillator cross long-flat (different construction, one-sided book); pool `ehlers-sinewave-phase-cross-flip` trades Hilbert Sine/LeadSine phase crosses (different waves, different event); pool `macd-signal-cross-reversal`, `ppo-signal-cross-reversal`, and `tsi-signal-cross-reversal` all cross fast-vs-slow lines but each builds them from exponential-average differences/ratios/double-smoothing (different filter, different normalization, different horizons — no SuperSmoother, no window-sum, no trailing-RMS); pool `laguerre-rsi-cu-cd-cross` and `fisher-zero-cross` trade different transforms against different events; pool `ema-20-50-cross`/`golden-cross-sma` compare raw price averages (different construction — no oscillator, no normalization). Shared `Ehlers`/`cross`/`20`/`50` vocabulary is not shared signal.
7. No hidden variants admitted: `hl2`/median-price input, any retuned `FastLength`/`SlowLength`, any zero-line trigger, any stop/target/filter/cooldown, any other frame, fill, or single-side gating is a different, unpinned rule. A reviewer must not pick among these to rescue or reshape the record.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `close` input / SuperSmoother coefficients as pinned / `FastLength = 20` / `SlowLength = 50` / window-sum plus trailing-RMS normalization / fast-slow cross predicates / flip-only always-in-market book / next-open fills / no-stop posture / `1d` BTCUSDT are frozen.

- F1 — Horizon relevance: a `50/50` twin (both legs at the slow horizon — degenerate no-trade control replaced in practice by a `20/20` twin) must not improve net expectancy; fail ⇒ the fast-slow horizon split adds nothing over a single-horizon line.
- F2 — Normalization relevance: a raw window-sum twin (SuperSmoother prefilter kept, trailing-RMS division deleted, same 20/50 cross, book, and timing) must not improve net expectancy; fail ⇒ the Ehlers RMS normalization adds nothing over its own unnormalized sums.
- F3 — Book relevance: a long-flat twin (long legs as pinned, short crosses exit to flat instead of flipping — same grid, fills, warmup) must not improve net expectancy; fail ⇒ the always-in-market short side destroys value and the flip derivation is the wrong port.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (declared port of a symbol-free listing with daily-bar context). The rule reads completed daily bars only, so no pit-session, gap, or roll logic ports. The fixed-length arithmetic needs no recalibration across assets, yet crypto's 24/7 trend persistence vs the listing's equity-daily cycle prior is a real mismatch — unclaimed and undisguised (see Negative evidence 3). The rule is two-sided reversal, so a spot-only deployment expresses only the long legs while short legs stay venue-gated (never silently converted) — a spot-only variant would be a different, unpinned claim. Funding accrues continuously by book design and is modeled, never zero-claimed. No warmup history beyond 100 daily bars is consumed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- No price stop, no time stop, no flat leg: adverse excursion after a flip has no guardrail before the counter-cross, by the prescribed listing design — the record's principal risk.
- Next-open lag: the cross is detected at the completed-bar close and filled at the next open, systematically one bar late on straight-line turns.
- Always-in-market economics: every chop cross pays a full round trip plus continuous modeled funding; flat markets are the worst case, disclosed, not tuned away.
- RMS-settle transient: early post-warmup `Trendflex` prints still carry trailing-`MS` seeding memory; the 100-bar adopted warmup (vs the 52-bar structural minimum) is the declared guardrail, not a source number.
- Single-venue daily port: symbol-free provenance vs 24/7 BTCUSDT daily execution is a declared derivation with unclaimed portability residual (prints, fees, funding, margin mechanics beyond the house model).
- Performance evidence is absent: no source reports a number for this exact rule, and none is claimed here.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior and never part of this admission — no Safety-Order/DCA event is admitted in this record's version. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- TASC Traders' Tips February 2020, TRADESTATION: FEBRUARY 2020 (Trendflex Cross EasyLanguage functions, indicator and strategy listings with 20/50 defaults, daily-AAPL chart context, Ehlers-article lineage — read end to end in a real browser session 2026-10-16): https://traders.com/Documentation/FEEDbk_docs/2020/02/TradersTips.html
