---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Ehlers correlation trend fast-slow threshold long-flat on BTCUSDT 1d bars
created: 2026-10-16
updated: 2026-10-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2020-05
sources:
  - https://traders.com/Documentation/FEEDbk_docs/2020/05/TradersTips.html
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Ehlers correlation trend fast-slow threshold long-flat on BTCUSDT 1d bars

## Provenance

Primary source read end to end (official TASC Traders' Tips page, fetched live 2026-10-16 in a real browser session, page title `TRADERS' TIPS - MAY 2020`):

- Canonical page: https://traders.com/Documentation/FEEDbk_docs/2020/05/TradersTips.html (adopted as `source_as_of: 2020-05`). The page header pins lineage: this month's tips implement John F. Ehlers' article in the same issue, `Correlation As A Trend Indicator`, and the TradeStation section states Ehlers `introduces a new trend indicator that is based on the correlation between a security's price history and the ideal trend: a straight line` and that `we are providing the TradeStation EasyLanguage code for an indicator and strategy as well as a function`.
- The complete EasyLanguage function `_CorrelationTrend` ships verbatim on the page (input `Length( numericsimple )`; loop `for count = 0 to Length - 1` with `X = Close[count]`, `Y = -count`, accumulators `Sx/Sy/Sxx/Sxy/Syy`; `Num = Length*Sxy - Sx*Sy`; `Denom = SquareRoot((Length*Sxx - Sx*Sx)*(Length*Syy - Sy*Sy))`; guarded by `if Denom <> 0 then Corr = Num / Denom`).
- The complete EasyLanguage strategy `Correlation Trend` ships verbatim on the same page (inputs `FastLength( 20 )`, `SlowLength( 40 )`, `BuyThreshold( .5 )`, `SellThreshold( 0 )`; `CorrF = _CorrelationTrend( FastLength )`, `CorrS = _CorrelationTrend( SlowLength )`; order legs `if CorrF crosses over BuyThreshold then Buy next bar at Market` and `if CorrS crosses under SellThreshold then sell next bar at Market`). Text census over the strategy listing this cycle: 1 `Buy next bar` / 0 `SellShort` / 1 `sell next bar` / 0 `SetStop` / 1 `crosses over` / 1 `crosses under` — the lowercase `sell` is TradeStation's exit-long leg (flat), not a short entry; the no-stop/no-target long-flat posture is coded absence, disclosed as source-native, never invented.
- Source timeframe context: the TradeStation sample chart is a daily chart of the SPDR S&P 500 ETF (`FIGURE 1: TRADESTATION. The correlation trend indicator and strategy are applied to a daily chart of the SPDR S&P 500 ETF`); the page carries 4 `daily chart` mentions (TradeStation daily SPY ETF, thinkorswim one-year daily SPY, eSignal daily SPY, NinjaTrader daily SPY). The listing itself takes no symbol, venue, or timeframe input — lengths 20/40 and thresholds 0.5/0 are its only horizon/trigger inputs.
- Corroborating long-flat book on the same page: the Wealth-Lab section runs a `simple long-only WealthScript system` on the same indicator (`Buy at market when the 20-day CorrelationTrend crosses above zero`, `Exit long when the indicator crosses below zero`, `IsLastPositionActive` guard with `BuyAtMarket`/`SellAtMarket` at `bar + 1`) — cited only as book corroboration, never adopted as the pinned rule.
- The page ships no performance number for this rule: no return, win rate, profit factor, trade count, date range, or cost table — this record claims no source-reported performance and no reproduced performance.
- Licence and rights: the page is TASC's public Traders' Tips code library (posted for copy-paste into analysis software). This record cites and normalizes the rule and reproduces only single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) research market/timeframe BTCUSDT `1d` (the listing pins no symbol or venue; its daily-bar context ports 1:1 to daily crypto bars); (2) an adopted 100-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 41st completed bar — see Required data); (3) house sizing/capital/costs replacing broker defaults (see Execution assumptions); (4) an explicit single-unit / same-bar tie-break (repeat `Buy` legs while already long are no-ops; if both predicates fire on the same bar the exit leg wins and the book ends flat — see Signal). Signal arithmetic, constants, comparisons, order-leg semantics, long-flat direction, and the no-stop/no-target posture are unmodified. Fill timing is source-native, not adapted: `next bar at Market` is modeled as next-open fills on completed `1d` bars.

Pre-write dedup (2026-10-16): working-tree case-insensitive filename search for `correl`, `corrtrend`, `cti`, `correlation-trend`, and content search for `CorrelationTrend`, `_CorrelationTrend`, `CorrF`, `CorrS` returns zero strategy records. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class (see Negative evidence 6). This is a new family member, not a parameter variant: no pool record computes this correlation-to-straight-line recurrence or trades this event.

## Economic mechanism

### Source-reported

Trend-as-correlation: the price path over a lookback is Pearson-correlated against the ideal trend (a straight line, coded as `Y = -count`). A print near +1 means the recent closes track the ideal rise; a print near 0 or negative means no trend or a counter-trend. The example strategy splits horizons and triggers asymmetrically: the fast (20) leg must push above +0.5 to evidence a fresh trend onset (entry), while the slow (40) leg falling below 0 evidences trend failure (exit to flat).

### Research interpretation

Asymmetric two-horizon threshold long-flat on a straight-line-correlation oscillator. Unlike the Ehlers zero-lag family (Trendflex/SuperSmoother+RMS, InstTrend delayed self-cross, Cyber Cycle inverted self-cross with escape, MAMA/FAMA Hilbert state, Bandpass resonator sign, Decycler high-pass oscillator, Sinewave phase cross) there is no smoother, no RMS normalization, no Hilbert transform, and no fast-vs-slow oscillator cross — the event is one fast series crossing a fixed level (0.5) for entry and a different slow series crossing a different fixed level (0) for exit. Unlike level-cross oscillators (Fisher-zero, StochRSI, CCI, RSI records) the oscillator itself is a rolling correlation against a deterministic ramp, not a momentum normalization; unlike dual-average crosses (MACD/PPO/TSI/EMA records) no average of price is ever compared to another average. The two `if` legs are independent (no `else`), so entry and exit predicates are evaluated separately every bar; the book is single-unit long-flat by record rule with pyramiding demonstrably excluded (repeat buys while long are no-ops, no averaging, no second unit).

## Signal

Exact rule as pinned (defaults quoted — inputs unmodified):

- Price input (pinned): `Close` series only, via `X = Close[count]` for `count = 0..Length-1`. No `open`, `high`, `low`, `volume`, or second timeframe on the order path. Reference leg is deterministic (`Y = -count`), not data.
- Recurrence (pinned, per `Length`): `Sx/Sy/Sxx/Sxy/Syy` zeroed each bar, accumulated over `count = 0 to Length-1`; `Num = Length*Sxy - Sx*Sy`; `Denom = SquareRoot((Length*Sxx - Sx*Sx)*(Length*Syy - Sy*Sy))`; `if Denom <> 0 then Corr = Num / Denom`. All lags are non-positive (current and past closes only).
- Fast leg (pinned): `CorrF = _CorrelationTrend(20)`. Slow leg (pinned): `CorrS = _CorrelationTrend(40)`.
- Entry long (pinned): `CorrF crosses over BuyThreshold(.5)` → `Buy next bar at Market` — filled at the next `1d` open under this record's source-native timing. Same-bar-close execution is a different, unpinned claim — none is admitted here.
- Exit to flat (pinned): `CorrS crosses under SellThreshold(0)` → `sell next bar at Market` — mirror terms at the next `1d` open. No short entry exists anywhere in the listing (0 `SellShort` tokens by census).
- Exit: the slow-leg cross-under is the sole position-closing path. No stop, no target, no trailing, no time exit — pinned as written, explicitly none, not invented.
- Direction: long-only with flat state; short side explicitly disabled by listing construction. A short-side instrument is never required.
- Position rule (researcher tie-break, predeclared): single-unit; repeat entry predicates while already long are no-ops (no pyramiding, no averaging, no second unit). If both predicates fire on the same completed bar, the exit leg wins and the book ends flat with no same-bar re-entry; re-entry requires a fresh entry cross on a later bar. Listing-order evaluation (entry `if` first, exit `if` second) is preserved; the tie-break only resolves the dual-fire ambiguity the listing leaves silent.
- Display isolation: the page's `Correlation Trend` indicator listing (`Plot1(Corr)`, `Plot2(TriggerLevel)`), the MetaStock/ThinkorSwim/NeuroShell/NinjaTrader/Trade Navigator/Excel/Zorro/eSignal ports, and the Wealth-Lab zero-threshold variant feed no order condition; order logic reads exactly the two threshold-cross predicates above with 20/40/0.5/0.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (via `Close[0..39]` on the slow leg; the fast leg reads `Close[0..19]`). No `open`, `high`, `low`, `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (researcher-declared; the listing takes no timeframe input and makes no multi-frame call, so it is single-frame by construction; source context is daily bars).
- Warmup: the slow leg reads `Close[39]`, so window history is complete on the 40th bar; the cross predicates compare against the prior bar's alignment, so the first evaluable signal sits on the 41st completed bar. Structural minimum is therefore the 41st completed `1d` bar; the adopted warmup is the first 100 completed `1d` bars flat by record rule (predeclared researcher choice, covering correlation-settle transients). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (researcher-declared; venue/symbol spelling is naming only, never presented as source-native semantics). Long-flat book needs no short-side instrument.
- Order timing (source-native): completed-bar decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester — the same next-open path as the admitted `1d` records. No maker-touch, queue, or intrabar-path-dependent fill. With no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity; the only same-bar ambiguity (dual-fire) is resolved by the predeclared exit-wins tie-break.
- Engine path for `1d` (gate 5, stated plainly): `1d` is a Binance-documented USDT-M kline interval; the derived rule needs only completed `1d` candles (`close` series) on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no volume-definition dependence, no funding/OI/mark-price leg. That is the same single-frame completed-bar plus next-open path as the admitted `1d` records; the correlation recurrence advances deterministically from known closes, so no hidden lookahead is ever modeled. Anything beyond that path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: broker defaults are replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions here, never presented as source-native behavior. The book is long-or-flat, so modeled funding accrues only while long — flagged per the house baseline, never zero-claimed; no campaign may claim complete realized-funding performance without a verified implementation.
- Concurrency: single-unit long-flat by record rule (repeat buys while long are no-ops; exit wins dual-fire); re-entry is immediate on the next qualifying entry cross after flat (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

With exact provenance (read end to end this cycle): the TASC page ships the complete rule (EasyLanguage `_CorrelationTrend` function, the `Correlation Trend` indicator and strategy listings with 20/40/0.5/0 defaults, both next-bar-market order legs with 1/0 Buy/SellShort census, the daily SPDR S&P 500 ETF sample-chart context, the Ehlers-article lineage note, plus the Wealth-Lab long-only corroboration). It ships zero performance numbers for this rule: no return, win rate, trade count, date range, or cost table — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden risk layer: the strategy listing contains no stop, limit, target, trailing, or time-exit token — the sole position-closing path is the slow-leg cross under 0. The absence is coded (the listing ends at the `sell` leg), disclosed in Signal for the reviewer rather than upgraded into a source claim.
2. No short leg exists: 0 `SellShort` tokens by census — a reviewer must not graft a short entry, a symmetric exit-to-short, or a reversal book onto this record.
3. Asymmetry is structural, admitted plainly: entry reads the fast (20) series against 0.5 while exit reads the slow (40) series against 0. A market that trends weakly (correlation positive but below 0.5 on the fast leg) never enters; a position whose slow leg never crosses below 0 never exits until trend failure — chop between the two thresholds holds or idles the book while paying delay and (while long) modeled funding. This is the coded trade, disclosed, not a tunable parameter here.
4. Boundary ties hold their side: an exactly-equal print (`CorrF == 0.5`, `CorrS == 0`, or equality on the prior-bar alignment) is neither a cross-over nor a cross-under, so no order fires and the book carries the prior state; the `Denom <> 0` guard pins the only division; warmup bars are flat by record rule; dual-fire resolves exit-wins by record rule.
5. Sibling variant fenced, never adopted: the same page's Wealth-Lab `20-day crosses above/below zero` system, the MetaStock `Correl(Cum(1),C,20)` one-liner, the Zorro `CTI(Prices,20)` zero-cross profile, and all vendor indicator ports are different, unpinned rules for the order path — a reviewer must not graft any zero-threshold entry, any single-horizon twin, or any `Length` other than 20/40 onto this record.
6. Overlap fences, admitted plainly: pool `ehlers-trendflex-fast-slow-cross` trades two RMS-normalized zero-lag oscillators against each other (different construction, cross event, always-in-market book); pool `ehlers-insttrend-delayed-cross` trades one composite line against its own 2-bar-ago copy (different event — delayed self-cross); pool `cyber-cycle-signal-self-cross` trades an inverted self-cross with an 8-bar open-loss escape to flat (different filter, inverted mapping); pool `mama-fama-hilbert-state-flip` trades adaptive MAMA/FAMA Hilbert state (different construction); pool `bandpass-filter-reversed-cycle-sign` trades a cosine-resonator sign (different filter); pool `ehlers-decycler-oscillator-cross` trades a high-pass decycler oscillator cross (different construction); pool `ehlers-sinewave-phase-cross-flip` trades Hilbert Sine/LeadSine phase crosses (different waves); pool `macd/ppo/tsi-signal-cross`, `laguerre-rsi`, `fisher-zero-cross`, `stochrsi`, `cci`, `rsi` records trade different transforms against different events (no straight-line correlation, no 20/40 asymmetric thresholds). Shared `Ehlers`/`cross`/`20` vocabulary is not shared signal.
7. No hidden variants admitted: `hl2`/median-price input, any retuned `FastLength`/`SlowLength`, any symmetric threshold, any stop/target/filter/cooldown, any other frame, fill, or two-sided gating is a different, unpinned rule. A reviewer must not pick among these to rescue or reshape the record.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `close` input / Pearson-against-ramp recurrence as pinned / `FastLength = 20` / `SlowLength = 40` / `BuyThreshold = 0.5` / `SellThreshold = 0` / threshold-cross predicates / single-unit long-flat book with exit-wins tie-break / next-open fills / no-stop posture / `1d` BTCUSDT are frozen.

- F1 — Threshold relevance: a symmetric zero/zero twin (both legs at 0 — entry `CorrF crosses over 0`, exit as pinned) must not improve net expectancy; fail ⇒ the 0.5 onset hurdle adds nothing over a plain zero cross.
- F2 — Horizon-split relevance: a single-horizon twin (both legs at 20 — entry `CorrF crosses over 0.5`, exit `CorrF crosses under 0`, same book and timing) must not improve net expectancy; fail ⇒ the fast/slow horizon split adds nothing over one correlation series.
- F3 — Oscillator relevance: a raw-price twin (20/40 SMA spread crossing the same 0.5/0 thresholds is not dimensionally comparable, so the control is a 20/40 SMA-spread sign system with the same long-flat book and timing) must not match the pinned rule's trade-event structure; fail ⇒ the correlation construction adds nothing identifiable over plain average-spread trend following.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (declared port of a symbol-free listing with daily-bar context). The rule reads completed daily closes only, so no pit-session, gap, or roll logic ports. The fixed-length arithmetic needs no recalibration across assets, yet crypto's 24/7 trend persistence vs the listing's equity-daily trend-failure prior is a real mismatch — unclaimed and undisguised (see Negative evidence 3). The rule is long-flat, so spot and futures both express it without venue gating; funding accrues only while long and is modeled, never zero-claimed. No warmup history beyond 100 daily bars is consumed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- No price stop, no time stop: adverse excursion after entry has no guardrail before the slow-leg cross under 0, by the prescribed listing design — the record's principal risk.
- Next-open lag: each cross is detected at the completed-bar close and filled at the next open, systematically one bar late on straight-line turns and failures.
- Asymmetric hold exposure: weak-trend markets never trigger entry while post-peak longs wait for slow-leg failure; flat markets idle the book and whipsaw markets pay full round trips plus while-long modeled funding, disclosed, not tuned away.
- Correlation-settle transient: early post-warmup prints still carry window-fill memory; the 100-bar adopted warmup (vs the 41-bar structural minimum) is the declared guardrail, not a source number.
- Single-venue daily port: symbol-free provenance vs 24/7 BTCUSDT daily execution is a declared derivation with unclaimed portability residual (prints, fees, funding, margin mechanics beyond the house model).
- Performance evidence is absent: no source reports a number for this exact rule, and none is claimed here.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior and never part of this admission — no Safety-Order/DCA event is admitted in this record's version. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- TASC Traders' Tips May 2020, TRADESTATION: MAY 2020 (Correlation Trend EasyLanguage function, indicator and strategy listings with 20/40/0.5/0 defaults, daily SPDR S&P 500 ETF chart context, Ehlers-article lineage — read end to end in a real browser session 2026-10-16): https://traders.com/Documentation/FEEDbk_docs/2020/05/TradersTips.html
