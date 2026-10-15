---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Ehlers Sinewave phase-cross flip two-sided on BTCUSDT 1d bars
created: 2026-10-16
updated: 2026-10-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-16
sources:
  - https://www.whselfinvest.com/en-lu/trading-platform/free-trading-strategies/tradingsystem/09-sinewave-ehlers
  - https://www.tradingview.com/script/bMR0ZDMy-Ehlers-Sinewave-Indicator-CC/
  - https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_HT_SINE.c
  - https://github.com/mementum/bta-lib/blob/master/btalib/indicators/ht_sine.py
  - http://www.davenewberg.com/Trading/TS_Code/Ehlers_Indicators/SineWave_Ind.html
  - https://github.com/MadBomber/sqa-tai/blob/main/docs/indicators/cycle/ht_sine.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Ehlers Sinewave phase-cross flip two-sided on BTCUSDT 1d bars

## Provenance

Primary sources read end to end during this cycle (2026-10-16), pinned:

- WHSelfInvest public strategy library, `The Sinewave Strategy` (fetched live this cycle, HTTP 200, 58592 bytes): Ehlers-lineage page (`Engineer Dr. John Ehlers`, `elaborated on his theories in the 2006 book "Cybernetic analysis for Stocks and Futures"`, `His favorite indicator is called Sinewave cyber`). Strategy rules verbatim in substance: `When the Sinewaves cross a new position is opened and the existing position is closed. A long position is converted into a short position. A short position is converted into a long position. As a consequence there is always an open position.` Close rule: `when the Sinewaves cross a new position is opened and the existing position is closed` (flip-only book, no stop/target leg on the base strategy). Source demo context is Eurostoxx 50 half-day aggregation (`28x15' i.e. 1/2 day`) — display context, never adopted. The page's honesty reservation and Grube variant are fenced in Negative evidence, never adopted.
- TradingView open-source script page `Ehlers Sinewave Indicator [CC]` by `cheatcountry` (fetched live this cycle, HTTP 200, 291572 bytes, `Open-source script`): lineage `The Sinewave Indicator was created by John Ehlers (Rocket Science For Traders pgs 97-99)`; cross rule verbatim in substance: `If the blue line crosses over the red line then within the next few bars the price will start an uptrend and if the blue line crosses below the red line then in the next few bars it will start a downtrend`. Release history shows book-error fixes (`Jun 4, 2020 Release Notes made changes to fix errors in the source book`), v5 update `Dec 29, 2021`, radian fix `Mar 26, 2023`. No performance table, trade count, or cost basis on the page — this record claims no source-reported performance.
- TA-Lib canonical implementation `src/ta_func/ta_HT_SINE.c` (repo `TA-Lib/ta-lib`, branch `main`, blob SHA `e5f5fee0568ae364c5101b93c5571101cff8f9fe`, 72691 bytes on disk this cycle; sibling definition `ta_func_defs/ht_sine/ht_sine.c` last touched by commit `48b5fd1bbeef9c24b724732cd38e1d22db758f3e`, 2026-06-27): pinned formula facts — Hilbert FIR constants `a = 0.0962`, `b = 0.5769`; lookback comment verbatim `31 input are skip + 32 output are skip ... 63 Total Lookback` with `31 is for being compatible with Tradestation`; outputs `outSine = sin(DCPhase*deg2Rad)`, `outLeadSine = sin((DCPhase+45)*deg2Rad)`; dominant-period clamp `6`/`50` with `0.2/0.8` smoothing (`period = (0.2*period) + (0.8 * tempReal)`); `smoothPeriod = (0.33*period)+(0.67*smoothPeriod)`.
- bta-lib readable mirror `btalib/indicators/ht_sine.py` (citing `Rocket Science for Traders: Digital Signal Processing Applications`): price pin `p0 = (high + low) / 2.0`; smoothing `p0smooth = (4.0*p0 + 3.0*p0(-1) + 2.0*p0(-2) + p0(-3)) / 10.0`; `LOOKBACK_TOTAL = 64`.
- Davenewberg EasyLanguage port of the RSFT Sine Wave (RSFT lineage, `From 'Cybernetic Analysis for Stocks and Futures' by John Ehlers`): `Inputs: Price((H+L)/2), alpha(.07)`; outputs `Plot1(Sine(DCPhase), "Sine")`, `Plot2(Sine(DCPhase + 45), "LeadSine")`.
- sqa-tai public docs `ht_sine.md` (cross-direction mapping, read live this cycle): `if prev_sine <= prev_lead && curr_sine > curr_lead` prints `BULLISH CROSSOVER: Sine crossed above Lead Sine` / `Consider LONG entry`; `elsif prev_sine >= prev_lead && curr_sine < curr_lead` prints `BEARISH CROSSOVER: Sine crossed below Lead Sine` / `Consider SHORT entry`. The page's ATR stops/targets, RSI confirmation, trend-mode gate, and amplitude filters are third-party additions — explicitly NOT adopted (see derived declaration).
- Licence and rights: this record cites and normalizes the rule (short quoted declarations only for gate evidence) and reproduces no source block beyond single-line facts.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any single source. The WHS page prescribes the flip book (always-in-market cross reversal, no stops); the cross-direction mapping is pinned from the sqa-tai/cheatcountry convention (Sine-up-through-LeadSine = long); the exact filter arithmetic is pinned from TA-Lib/bta-lib/Davenewberg (RSFT Ch.9 lineage). Researcher-declared adaptations are exactly five: (1) market pin `BTCUSDT` Binance futures `1d` (WHS demos Eurostoxx half-day bars — venue/frame pin disclosed, never a source claim); (2) completed-bar decision with next-bar-open market fills (the WHS page ships no bar-timing; Pine-default-compatible, disclosed, never an advantage claim); (3) price input pinned to `hl2` (btalib/Davenewberg convention — mihakralj-style `close` input or any other series would be a different, unpinned rule); (4) adopted 100-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 64th completed bar — see Required data); (5) house sizing/costs with modeled funding while held (no source ships portable economics — recorded as absent, never as evidence). The Hilbert constants, smoothing weights, homodyne construction, period clamp, 45-degree lead, cross predicates, flip-only book, pyramiding-once posture, and no-stop/no-target stance are source-pinned.

Pre-write dedup (2026-10-16): working-tree case-insensitive searches for `ht_sine`, `htsine`, `leadsine`, `lead sine`, `sinewave`, `sine wave`, and `rocket science` return zero strategy records using this source, indicator, or phase-cross construction. Open `research/*` PRs are only #48, #49, #63, #89, #92 (Larry Williams streak, Gaussian-channel StochRSI, SuperTrend flip, Chandelier Exit, SSL channel) — none is an Ehlers phase-cross system. Closest pool records differ in mechanism class — five-axis distinction in Signal and Negative evidence 6.

## Economic mechanism

### Source-reported

Dominant-cycle phase trading (WHS page plus RSFT lineage): the market spends most of its time in a measurable dominant cycle whose velocity and frequency change; the Hilbert transform extracts that cycle's phase (`Sinewave's specialty ... is to immediately adapt to velocity and frequency changes`), and the 45-degree-advanced LeadSine anticipates the turning point (`the anticipation signal is obtained strictly by mathematically advancing the phase. Momentum is not employed` — blackcat L2 page substance, RSFT Ch.9 lineage). Positions flip with the phase: cross up = cycle turning up (long), cross down = cycle turning down (short), always holding one side because the cycle is always somewhere in its rotation.

### Research interpretation

Phase-cross flip with an always-in-market book. Unlike every amplitude/level record (StochRSI, CCI, Fisher-zero, RSI-classic: oscillator-against-fixed-threshold) the trigger here compares two phase waves against each other — a turning-point detector with no level anywhere, so there is no overbought/oversold leg to tune. Unlike the pool's other Ehlers cross records (MAMA/FAMA adaptive-MA state, Cyber Cycle inverted self-cross with loss escape, Decycler fast-slow cross, Laguerre CU/CD cross, bandpass-resonator sign) the event is the dominant-cycle phase crossing its own 45-degree lead — a different filter, a different geometric event, and a different book (unconditional flip, never flat, no escape). Unlike flat-capable systems (Cyber Cycle escape, first-last-halfhour timing, NR7 breakout) this machine has no neutral gear after warmup:chop and trend alike are ridden one side at a time, and the honestly priced cost is full participation in phase misfires (see Negative evidence).

## Signal

Exact rule as pinned (any other input series, constant, book, fill, or frame is a different, unpinned rule):

- Price input (pinned): `p = hl2 = (high + low) / 2` of completed `1d` bars (btalib/Davenewberg convention).
- Smoothing (pinned): `smooth = (4·p + 3·p[1] + 2·p[2] + p[3]) / 10`.
- Hilbert detrender/quadrature (pinned, TA-Lib): FIR with `a = 0.0962`, `b = 0.5769`, adaptive factor `(0.075·period + 0.54)`; homodyne `I2/Q2` with `0.2/0.8` smoothing on current/prior; dominant period clamped to `[6, 50]` bars with `0.2/0.8` period smoothing and `0.33/0.67` smooth-period blending.
- Phase waves (pinned): `Sine = sin(DCPhase)`, `LeadSine = sin(DCPhase + 45°)` (TA-Lib outputs, Davenewberg plots); both range `[-1, +1]`.
- Entry long (pinned mapping): on a completed bar `t` (post-warmup) with `Sine[t-1] ≤ LeadSine[t-1]` AND `Sine[t] > LeadSine[t]` → close any short and open long at the next bar's open. The cross predicates use strict inequality on the current bar; an exact-equality print holds the prior state (no signal — disclosed convention, measure-zero on live tape).
- Entry short (pinned mapping): mirror — `Sine[t-1] ≥ LeadSine[t-1]` AND `Sine[t] < LeadSine[t]` → close any long and open short at the next bar's open. The two predicates are mutually exclusive on every bar by definition, so at most one flip fires per bar under any evaluation order.
- Book: always-in-market after warmup — the first post-warmup cross opens the initial position in the cross direction; every later cross flips. There is no flat state, no stop, no target, no trailing, no time exit — explicitly none by WHS base-strategy rule.
- Direction: symmetric two-sided flip. Shorts are native to USDT-M margin (no uptick rule, no borrow desk).
- Re-entry: every qualifying cross flips unconditionally (no cooldown specified — explicitly none, not invented).

## Required data

- Completed `1d` bars of BTCUSDT: `high`/`low` only (via `hl2` and its lags; the recursion reads only own-prior filter outputs). No `open`, no `close` series, no `volume`, no funding-signal, OI, mark/index price, order-book, on-chain, sentiment, macro, calendar, session-template, or cross-asset state is read anywhere.
- Single decision timeframe `1d` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; all filter constants are pinned, never estimated at runtime).
- Warmup: TA-Lib lookback is 63 bars (`63 Total Lookback`) so the first fully-constructed output prints on the 64th completed bar (btalib `LOOKBACK_TOTAL = 64` agrees); the adopted warmup is the first 100 completed `1d` bars flat by record rule (predeclared researcher choice). Any missing bar inside the window is skipped on available completed bars only — prices are never fabricated. No repaint path (every filter tap reads completed bars and own-prior outputs only; the DFT phase reads the trailing smooth-price buffer, never a future print).

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (the WHS page demos Eurostoxx — venue/frame adaptation disclosed, never a source claim).
- Order timing (predeclared derivation): completed-bar phase decision with next-bar-open market entries/flips — compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) on the same verified primitives as the admitted `ehlers-decycler` (next-open entries) and `holmberg-orb` (next-open entries) PASS records. No maker-touch, queue, multi-asset sync, lower/multi-timeframe alignment, non-OHLCV input, or intrabar-path-dependent fill is required. At most one flip (one close plus one open) per day. With no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity.
- Sizing/capital/costs: single 100%-equity unit, no adds, no leverage concept beyond the house overlay (no source ships portable economics — recorded as absent, never as evidence). Derived evaluation carries pinned house taker fees on every flip leg plus modeled funding while held — the book is always-in-market, so funding accrues continuously and is never zero-claimed. No Safety-Order/DCA event participates regardless of downstream campaign settings.
- Concurrency: one single-asset engine position at a time (each flip closes the current side first); no second leg is constructed anywhere — no hedge-mode requirement exists by construction. No shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

With exact provenance (all read end to end this cycle): the WHS page ships the complete base-strategy rule (flip on every cross, always-in-market book, no stop/target leg) and the Eurostoxx half-day demo context; the cheatcountry page ships the RSFT pgs 97-99 lineage and the cross-direction rule in substance; TA-Lib ships the exact filter arithmetic, constants, 63-bar lookback, and Sine/LeadSine outputs; btalib/Davenewberg ship the `hl2` input convention and smoothing weights; sqa-tai ships the explicit bullish/bearish crossover mapping in code. No source ships a performance number for THIS rule: the WHS page carries no return, win-rate, trade-count, or cost table for the base strategy — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Source's own robustness reservation, admitted plainly: `The Sinewave market cycles strategy developed by Dr John Ehlers gives variable results. The results go from astonishing to bad. It is not a robust strategy` (WHS conclusion) — carried as the record's headline risk; nothing here claims robustness the source itself denies.
2. Grube variant fenced, never adopted: author Claus Grube `added a trend filter as well as profit targets and stop loss criteria` (`MACD combination (11 and 66 periods EMA ...)`, `profit target is 10 times the ATR`, `hit ratio is around 70%` on a 10-year 15-minute Eurostoxx study). Every one of those legs — filter, target, stop, frame, market, and the 70% print — belongs to a different, unpinned rule; the WHS page itself warns `his filters and aggregations would require substantial modification` elsewhere. A reviewer must not graft any Grube leg onto this record to rescue or reshape it.
3. Third-party risk legs fenced: sqa-tai's ATR stops/targets, RSI confirmation, trend-mode gate, and amplitude/strength filters are that page's additions, explicitly not adopted — this record rides every phase cross with no guardrail, by the WHS base posture.
4. Trend-mode stall disclosed: Ehlers' own construction notes the phase `languishes when the market is in a trend mode` (RSFT-lineage indicator note) — without Grube's filter this record holds the wrong side through the stall until the counter-cross prints; the whipsaw immunity the indicator claims is a cycle-mode property, never a trend-mode promise.
5. Always-in-market cost disclosed: full participation means funding accrues on every held day and every chop cross pays two taker legs; there is no flat leg to rest in, unlike escape/timing records — the principal economic risk, carried over exactly.
6. Overlap fences, admitted plainly: pool `mama-fama-hilbert-state-flip` trades MAMA/FAMA adaptive-MA state (different Ehlers construction, no phase waves, no cross event); pool `cyber-cycle-signal-self-cross` trades an inverted self-cross of an EMA-of-cycle line with an 8-bar open-loss escape to flat (different filter, inverted mapping, escape-flat book); pool `bandpass-filter-reversed-cycle-sign` trades the sign of a cosine-derived first-order IIR resonator with pure reversal (different filter, sign event, no lead wave); pool `ehlers-decycler-oscillator-cross` trades a fast-slow Decycler oscillator cross long-flat (different construction, one-sided book); pool `laguerre-rsi-cu-cd-cross` trades a Laguerre CU/CD ratio cross (different transform, different event); pool `fisher-zero-cross` warps normalized prices through the Fisher nonlinearity against zero (different transform, level event). Shared `Ehlers`/`Hilbert`/`cross` vocabulary is not shared signal.
7. No hidden variants admitted: `close`-input, EBSW (Even Better Sinewave, a different book construction), any retuned constant, any stop/target/filter/cooldown, any other frame, fill, or single-side gating is a different, unpinned rule. A reviewer must not pick among these to rescue or reshape the record.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `hl2` input / smoothing weights / `a = 0.0962`, `b = 0.5769` / homodyne construction / `[6, 50]` period clamp / 45-degree lead / cross predicates / flip-only always-in-market book / next-open fills / no-stop posture / `1d` BTCUSDT are frozen.

- F1 — Mapping relevance: a naive-mapping twin (long on Sine-down-cross, short on Sine-up-cross — same machine, inverted sides) must not improve net expectancy; fail ⇒ the Ehlers cross-direction mapping adds nothing over its mirror on this market.
- F2 — Book relevance: a long-flat twin (long legs as pinned, short crosses exit to flat instead of flipping — same grid, fills, warmup) must not improve net expectancy; fail ⇒ the always-in-market short side destroys value and the flip derivation is the wrong port.
- F3 — Event relevance: a sign-level twin (long while `Sine > 0`, short while `Sine < 0`, same timing — level book on the identical waves) must not improve net expectancy; fail ⇒ the phase-cross event adds nothing over the wave's own sign.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (declared port of a Eurostoxx-index demo context). The rule reads completed daily bars only, so no pit-session, gap, or roll logic ports. The `hl2` input and Hilbert arithmetic need no pip recalibration across assets, yet crypto's 24/7 trend persistence vs an equity-index cycle prior is a real mismatch — unclaimed and undisguised (see Negative evidence 4). The rule is two-sided flip, so a spot-only deployment expresses only long-flip days while short-flip legs stay venue-gated (never silently converted) — a spot-only variant would be a different, unpinned claim. Funding accrues continuously by book design and is modeled, never zero-claimed. No warmup history beyond 100 daily bars is consumed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- No price stop, no time stop, no flat leg: adverse excursion after a flip has no guardrail before the counter-cross, by the prescribed base-strategy design — the record's principal risk.
- Phase stall in trends: the dominant-cycle estimator languishes when the market trends, so entries can arrive late and exits later, by the construction's own admission.
- Next-open lag: the cross is detected at the completed-bar close and filled at the next open, systematically one bar late on straight-line cycle turns.
- Always-in-market economics: every chop cross pays a full round trip plus continuous modeled funding; flat markets are the worst case, disclosed, not tuned away.
- Single-venue daily port: Eurostoxx half-day provenance vs 24/7 BTCUSDT daily execution is a declared derivation with unclaimed portability residual (prints, fees, funding, margin mechanics beyond the house model).
- Performance evidence is absent: no source reports a number for this exact rule, and none is claimed here.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior and never part of this admission — no Safety-Order/DCA event is admitted in this record's version. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- WHSelfInvest public strategy library, The Sinewave Strategy (Ehlers lineage, flip/always-in-market rule, robustness reservation, Grube variant fence — fetched live 2026-10-16, HTTP 200, 58592 bytes): https://www.whselfinvest.com/en-lu/trading-platform/free-trading-strategies/tradingsystem/09-sinewave-ehlers
- TradingView open-source script page, Ehlers Sinewave Indicator [CC] by cheatcountry (RSFT pgs 97-99 lineage, cross-direction rule, release history — fetched live 2026-10-16, HTTP 200, 291572 bytes): https://www.tradingview.com/script/bMR0ZDMy-Ehlers-Sinewave-Indicator-CC/
- TA-Lib canonical implementation, `src/ta_func/ta_HT_SINE.c` on `main` (blob SHA `e5f5fee0568ae364c5101b93c5571101cff8f9fe`, 72691 bytes; Hilbert constants, 63-bar lookback, Sine/LeadSine outputs, period clamp): https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_HT_SINE.c
- bta-lib readable formula mirror, `ht_sine.py` (`hl2` input, WMA weights, LOOKBACK_TOTAL = 64, RSFT book citation): https://github.com/mementum/bta-lib/blob/master/btalib/indicators/ht_sine.py
- Davenewberg RSFT EasyLanguage port (`Price((H+L)/2)`, `alpha(.07)`, Sine/LeadSine plots): http://www.davenewberg.com/Trading/TS_Code/Ehlers_Indicators/SineWave_Ind.html
- sqa-tai public indicator docs, `ht_sine.md` (explicit bullish/bearish crossover mapping; ATR/RSI/trend/amplitude additions not adopted): https://github.com/MadBomber/sqa-tai/blob/main/docs/indicators/cycle/ht_sine.md
