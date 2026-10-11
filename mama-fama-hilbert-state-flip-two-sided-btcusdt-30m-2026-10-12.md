---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: MAMA-FAMA Hilbert-adaptive state-flip two-sided on BTCUSDT 30m bars
created: 2026-10-12
updated: 2026-10-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-09-27
sources:
  - https://www.fmz.com/strategy/428090
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# MAMA-FAMA Hilbert-adaptive state-flip two-sided on BTCUSDT 30m bars

## Provenance

Primary source read end to end (canonical FMZ strategy page fetched live over HTTPS, verified 2026-10-12):

- Canonical page: https://www.fmz.com/strategy/428090 (title `Ehlers MESA Adaptive Moving Average Trading Strategy`, page fetched live at 759,059 bytes HTTP 200; `<title>` pins the strategy identity; meta description states verbatim `Overview This strategy is based on Ehlers MESA Adaptive Moving Average and designed a trend trading strategy that tracks crossovers between two moving avera[ges]`; page prose states the strategy compares the magnitude relationship between the MAMA and FAMA lines to decide uptrend versus downtrend and generates trading signals on it. Page identity confirmed, zero performance numbers anywhere on the page: `Sharpe`/`Net Profit`/`Win Rate`/`Max Drawdown`/`Profit Factor`/`Annualized` all 0).
- Executable spec (source-verbatim, stanza first): `start: 2023-09-20 00:00:00 / end: 2023-09-27 00:00:00 / period: 30m / basePeriod: 15m / exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]` followed by the full `//@version=2` Pine block (64 lines, 2,738 bytes of escaped code text extracted and read verbatim this cycle — byte-level provenance, no paraphrase). Adopted `source_as_of` 2023-09-27 is the stanza's own backtest-window end date, disclosed here, never an authorship date.
- Code header (source-verbatim): `// @author LazyBear` with the strategy declaration `strategy("Ehlers MESA Adaptive Moving Average [LazyBear with ekoronin fix]", shorttitle="EMAMA_LB (ekoronin fix)", overlay=false, calc_on_every_tick=true, precision=0)`. The block is LazyBear's Ehlers-MAMA port (with the ekoronin radians-to-degrees fix in the phase line) wrapped as an executable strategy by the FMZ uploader; both credits disclosed, never conflated. Lineage corroboration only: John F. Ehlers, Stocks & Commodities V.19:10 "MESA Adaptive Moving Averages" — every formula line in this record comes from the FMZ page bytes above, disclosed here, not hidden.
- Text census over the pinned 64-line code block: 1 `strategy(` (quoted above) / 0 `study(` / 2 `strategy.entry` (`"Long"` with `strategy.long`, `"Short"` with `strategy.short`, no price/qty/when argument) / 0 `strategy.close` / 0 `strategy.exit` / 0 `strategy.order` / 0 `strategy.cancel` / 0 `stop=`/`limit=`/`profit=`/`loss=` / 0 `crossover(` / 0 `crossunder(` (the single `cross(` token sits inside the commented-out `//plotarrow(pa?(cross(mama, fama)...` display line — no live order leg calls any cross function) / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `time(` / 36 `nz(` (Hilbert-recursion seeds, seeding only) / 10 `iff(` (8 live clamps plus 2 inside the commented-out `possig` reverse-mode stub) / 6 `input(` (3 live: `src`/`fl`/`sl`; 3 frozen inside `//` comments: `pa`, `fr`, `ebc`) / 5 `plot(` (2 live 0/1 state plots plus 3 commented indicator plots) / 0 `alertcondition` / 0 `position_size` / 0 `position_avg` / 0 `openprofit` / 0 `strategy.equity` / 0 `pyramiding` / 0 `process_orders_on_close` / 1 `calc_on_every_tick` (pinned `true`, fenced below) / 0 `commission` / 0 `default_qty` / 0 order-leg `currency` / word-boundary `volume` 0 / `open` 0 / `high` 0 / `low` 0 / `close` 1 (exactly one code read: `src=input(close, ...)` — every other price read in the block is a lag of the `src` series, hence close-derived).
- Three live inputs frozen (any other value is a different, unpinned rule): `src = close`, `fl = .4` (Fast Limit), `sl = .04` (Slow Limit). No date window, no session template, no direction switch, no reverse-mode switch (the `possig` reverse stub is fully commented out — disclosed, never enabled).
- No risk layer ships anywhere in the source: zero stop/target/trailing/time-exit order legs — the no-stop/no-target posture below is the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention.
- Page performance language is absent entirely — this record claims no source-reported performance and no reproduced performance. The stanza names the market and frame outright (`Futures_Binance BTC_USDT`, `30m`) — the `BTCUSDT 30m` pin below is source-faithful, not a researcher derivation.

Licence and rights: the pinned code block carries LazyBear's public-indicator header with no licence gate on the page; this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly three: (1) same-bar-close fills on completed-bar decisions (the source declares `calc_on_every_tick=true` with no `process_orders_on_close` argument — pinned verbatim in census — so its live venue recalculates intrabar and its backtest fills next-bar by language default; this record freezes the completed-bar evaluation with same-bar-close execution and scopes live intrabar recalculation out, see Limitations); (2) an adopted 100-bar warmup with pre-warmup bars flat by record rule (covers the ~21-bar structural lag stack plus the `.2/.8` smoother seed decay plus margin; see Required data); (3) house sizing/capital/costs replacing the absent source economics (the source ships no commission/slippage/capital/funding/margin assumption at all — see Execution assumptions). The `30m` frame, the Binance-futures BTCUSDT venue, the `close` source read, the `.4/.04` alpha limits, the Hilbert-discriminator arithmetic, the MAMA/FAMA recursions, the strict-inequality state order pair with `Long`/`Short` IDs, the reversal-only exits, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-12): working-tree case-insensitive searches for `428090`, `hilbert`, `ekoronin`, `emama`, and `mesa adaptive` return zero strategy records using this source, author script, indicator, or construction; word-boundary `mama` outside older records' own dedup-prose paragraphs returns zero order-leg uses. Closed research PR #6 (LazyBear WaveTrend `wt1`/`wt2` oscillator cross) is a price-normalized CCI-family oscillator cross — different formula, different trigger, different source. The Ehlers-adjacent pool records (`laguerre-rsi`, `fisher-zero-cross`, `bandpass-filter`) use gamma-filter, Fisher-transform, and cosine-resonator constructions respectively — none computes a Hilbert-discriminator adaptive alpha and none trades a MAMA/FAMA state (five-axis distinction in Signal and Negative evidence). No pool record reads `close`-only Hilbert phase anywhere in any order leg. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources.

## Economic mechanism

### Source-reported

Hilbert-adaptive trend-state flip (page prose plus code header, no performance section ships): a Hilbert-transform discriminator measures the market's dominant cycle each bar and converts it into an adaptive smoothing factor `alpha` clamped between the Slow Limit (`.04`) and Fast Limit (`.4`) — fast cycles earn fast averaging, slow cycles earn slow averaging. The MAMA line applies that alpha to price; the FAMA line trails MAMA at half alpha as a confirmation rail. While MAMA prints above FAMA the market is deemed uptrending and the system holds long; while below, downtrending and short. There is deliberately no stop, no target, and no flat state — the order block ends with the short leg and no risk leg ships anywhere, by design gap rather than by hidden leg.

### Research interpretation

Adaptive-alpha state machine, two-sided with reversal exits — the first Hilbert-construction record in the pool. Unlike fixed-length average crosses (EMA 20/50, TEMA/DEMA/HMA, HMA-gated variants), there is no fixed lookback anywhere in the signal path: the effective averaging length breathes every bar with the measured cycle (`alpha = fl / dphase` clamped to `[.04, .4]`, i.e. effective lengths from 4 to 49 bars), so the system shortens itself in fast markets and lengthens itself in slow ones instead of being retuned. Unlike oscillator crosses (MACD, QQE, TSI, WaveTrend, DSS-Bressert), nothing here is bounded or normalized — both lines ride in raw price units and the trigger is a strict-inequality state (`mama > fama`), not a level, not a cross pulse: entries re-fire on every in-state bar and same-direction refires are no-ops under the fixed-ID single-position semantics, so the position simply persists through the whole state. Note the two pinned asymmetries, stated plainly: first, FAMA smooths MAMA (not price) at half alpha, so the confirmation rail lags the trigger line by construction — exits inherit that double smoothing symmetrically; second, the phase-difference floor (`dphase < 1 → 1`) caps alpha at the Fast Limit, so a cycle faster than one radian per bar cannot earn faster averaging — the clamp binds, disclosed. The bet is on Hilbert-measured cycle states at frozen `.4/.04` geometry, not on any price level, volume print, mean-reversion extreme, or calendar effect.

## Signal

Exact rule as pinned (`src = close`, `fl = .4`, `sl = .04` frozen — any other value is a different, unpinned rule):

- Declaration (source-faithful): `strategy("Ehlers MESA Adaptive Moving Average [LazyBear with ekoronin fix]", ..., overlay=false, calc_on_every_tick=true, precision=0)` semantics preserved with the stanza-native `BTCUSDT 30m` market/frame pin and same-bar-close execution adopted (see derived declaration) and house sizing/costs replacing the absent source economics (see Execution assumptions). No `pyramiding`/`process_orders_on_close`/capital argument ships — single-position reversal semantics hold from the fixed order-ID pair: at most one open position, same-direction refires are no-ops, opposite entries reverse in full.
- Indicator (pinned arithmetic — evaluated from the frozen inputs, not tuned): `sp = (4*src + 3*src[1] + 2*src[2] + src[3]) / 10.0` (weighted smooth); Hilbert discriminator legs `dt`/`q1`/`i1`/`jI`/`jq` with `.0962/.5769` coefficients and `(.075*nz(p[1]) + .54)` cycle compensation; quadrature pair `i2`/`q2` (`.2/.8` smoothing); phasor accumulators `re`/`im` (`.2/.8` smoothing); dominant-cycle estimate `p` via `2*pi/atan(im/re)` with 1.5x/0.67x rate limits, clamped to `[6, 50]`, smoothed `.2/.8`, plus `spp` `.33/.67` smoothing; `phase = 180/pi * atan(q1/i1)` with the ekoronin degrees fix; per-bar phase advance `dphase` floored at 1; adaptive `alpha = fl/dphase` clamped to `[sl, fl]`; `mama = alpha*src + (1-alpha)*nz(mama[1])`; `fama = .5*alpha*mama + (1-.5*alpha)*nz(fama[1])` — all causal recursion on completed bars with `nz` seeds only.
- Entry long: `strategy.entry("Long", strategy.long)` under `if (longSpike)` where `longSpike = mama > fama ? 1 : 0` — fires on every completed bar printing MAMA strictly above FAMA, with same-bar-close execution under the derived declaration. Refires while already long are no-ops under the fixed-ID single-position semantics.
- Entry short: `strategy.entry("Short", strategy.short)` under the separate `if (shortSpike)` where `shortSpike = mama < fama ? 1 : 0` — fires on every completed bar printing MAMA strictly below FAMA, with same-bar-close execution under the derived declaration. From flat it opens short; from long it reverses to short in full (the sole exit path — coded, not invented).
- Direction: two-sided with no coded flat state (the two `if` legs cover both strict-inequality directions and nothing else; equality and `na` bars fire neither leg and the inherited position simply persists). After the first signal the system is always in market (long or short) — disclosed, not enabled.
- Display isolation: the two live `plot(longSpike)`/`plot(shortSpike)` 0/1 rails render only and cannot change any order; the three commented plots, the commented crossover-marker stub, the commented barcolor stub, and the commented `possig` reverse stub are inert `//` text — order logic reads exactly the two order lines. No stop, no target, no trailing exit leg, no time exit — pinned as written, explicitly none, not invented.

## Required data

- Completed `30m` bars of BTCUSDT: `close` only (via the frozen `src = close` read and its `[1..6]` lags through the `sp`/`dt`/`q1` smoothing stack). No `open`-, `high`-, `low`-, or `volume`-series read ships in any live line; no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read anywhere.
- Single decision timeframe `30m` (stanza-faithful; the script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction — the stanza's `basePeriod: 15m` is the FMZ replay sub-step, never read by any order-gating line, disclosed, not a second signal frame).
- Warmup: the construction stacks a 4-bar weighted smooth with 6-lag Hilbert recursions (structural lag ≈ 21 bars: `sp[6]` through `dt[6]` through `q1[6]`/`i1[6]`) beneath four `.2/.8` seed-decayed smoothers (`i2`/`q2`, `re`/`im`, `p`, `mama`/`fama`) plus the `.33/.67` `spp` line. The adopted warmup is the first 100 completed `30m` bars flat by record rule (predeclared researcher choice — roughly five times the structural lag with smoother-decay margin; ≈50 hours of `30m` history). No negative shift, no future reference, no full-sample normalization; one evaluation per completed bar under the derived freeze (`calc_on_every_tick=true` scopes live intrabar recalculation out — see Limitations). Each bar's `close` enters the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (stanza-faithful — venue choice and symbol spelling come from the pinned stanza, never presented as a researcher invention; see Provenance).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own posture is `calc_on_every_tick=true` with no `process_orders_on_close` argument (quoted verbatim in census) — live intrabar recalculation plus next-bar backtest fills by language default; this record does not claim either source behavior. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. Entry legs are evaluated in source order (long `if` before short `if`): the two strict-inequality predicates are mutually exclusive per bar by construction (equality fires neither), so at most one leg can fire on any bar — no same-bar double-fill ordering exists under either evaluation order.
- Engine path for `30m` (gate 5, stated plainly): `30m` is a Binance-documented USDT-M kline interval; the derived rule needs only completed `30m` candles (`close` alone) on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no volume-definition dependence, no funding/OI/mark-price leg. That is the same single-frame completed-bar path as the admitted `15m`/`1h`/`2h`/`4h`/`1d` records (the `1h/4h/1d` whitelist stands removed as an independent ban, and no ban is reinstated here by another name); the source stanza itself executed this venue and symbol on `Futures_Binance`. Anything beyond that single-frame completed-bar path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: the source ships no economics at all (no capital, no commission/slippage argument, no funding, no margin assumption — quoted verbatim in census; the absence is disclosed, never read as zero cost) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: fixed-ID single-position semantics hold — at most one open position under the order IDs `Long`/`Short`; state entries re-fire every in-state bar and same-direction refires while already positioned are no-ops, the opposite entry reverses in full (the sole position-closing path), an entry while flat opens, and re-placement is allowed immediately on the next qualifying bar after any reversal (no cooldown specified — explicitly none, not invented). Equality bars and `na` bars (Pine `if(na)` never fires — e.g. a zero-division `q1/i1` bar) hold the inherited position by language semantics, disclosed, not invented. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (frozen `close` source read, `.4`/`.04` alpha limits, `.0962/.5769` Hilbert coefficients with `(.075*nz(p[1]) + .54)` compensation, `6..50` cycle clamp with 1.5x/0.67x rate limits, MAMA/FAMA recursions, the strict-inequality state order pair with fixed `Long`/`Short` IDs, display-only 0/1 rail plots), the `strategy("Ehlers MESA Adaptive Moving Average [LazyBear with ekoronin fix]", ..., calc_on_every_tick=true)` declaration, the `2023-09-20→2023-09-27` / `30m` / `Futures_Binance BTC_USDT` stanza, and the LazyBear header. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.close`, 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=` — the sole position-closing path is the coded opposite-state `strategy.entry` reversal. The absence is coded (the order block ends with the short leg and only a tab character follows it in the file) and the prose carries no risk leg anywhere.
2. Coded rule is a strict-inequality state, not a cross pulse, stated plainly: 0 `crossover(` / 0 `crossunder(` anywhere live (the lone `cross(` token is inside a `//`-commented display stub) — every in-state bar re-fires its leg and equality bars fire nothing, so the position persists through whole states rather than pulsing on edges. Substituting edge-only crossover entries would be a different, unpinned rule.
3. Reverse-mode stub fenced: the `possig` long/short-inversion block is fully commented out — anyone re-enabling it trades an unpinned rule, disclosed here.
4. No future leakage in the stack, stated plainly: at decision bar `t`, the `sp`/`dt`/`q1`/`i1`/`jI`/`jq`/`i2`/`q2`/`re`/`im`/`p`/`spp`/`phase`/`dphase`/`alpha`/`mama`/`fama` legs read completed-bar prints through `t` and seeded `[1]` priors only. No `security()`, no `request.*`, no negative index, no `open`/`high`/`low`/`volume` read, no `barstate.islast`-gated path; the only division (`q1/i1`, `im/re` guarded by `iff`) degrades to `na`-hold, never to a forward read.
5. Same-bar entry ordering fenced: the long `if` precedes the short `if`, and the two strict-inequality predicates cannot both print on one bar — at most one of the two entry legs can fire on any bar. Deterministic under either fill convention.
6. Two-sided posture provably complete: both `strategy.long` and `strategy.short` appear exactly once each, each under its own guarded `if`; no third direction exists. No flat state is coded after the first signal — always-in-market past seeding, disclosed.
7. Adaptive-alpha entries with a live short side, admitted plainly: unlike absolute-threshold oscillators that can peg one-sided at crypto scale, both lines ride in raw price units and the clamp re-anchors every bar by construction, so both state directions stay reachable without retuning — while a market that trends hard without printing the opposite state is ridden with no stop, and the double smoothing (MAMA plus half-alpha FAMA) delays both entries and reversals symmetrically. There is no confirmation filter, no stop, and no flat state — the coded posture, disclosed as the record's principal risk.
8. Derivation boundary fenced: the only non-source-native behaviors in this record are same-bar-close fills (with live intrabar recalculation scoped out), the adopted 100-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the market/frame pin is stanza-faithful, and the price reads, inputs, Hilbert arithmetic, recursions, order IDs, reversal handling, and risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, timing, alpha limit, or the commented-out reverse/cross modes of the source pass.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `close` Hilbert stack / `fl .4 / sl .04` / MAMA/FAMA state pair / reversal exits / two-sided / `30m` BTCUSDT / same-bar-close fills are frozen.

- F1 — FAMA-leg relevance: replacing the half-alpha FAMA rail with a fixed-length slow EMA of `close` at the same state entries must not improve net expectancy; fail ⇒ the coded confirmation rail adds nothing over its fixed-length twin.
- F2 — Adaptivity relevance: freezing `alpha` at its mid-range constant (`0.22`) for both recursions (same state entries) must not improve net expectancy; fail ⇒ the Hilbert-measured cycle adaptation adds nothing over its fixed-alpha twin.
- F3 — State relevance: firing entries on fresh-state edges only (first bar of each state, edges computed from the same pair) must not improve net expectancy; fail ⇒ the coded every-bar state-hold adds nothing over its edge-pulse twin.

## Crypto portability

Pinned to BTCUSDT Binance futures `30m` under the house overlay (stanza-faithful; the source stanza already names this venue and symbol). The `close`/Hilbert/MAMA/FAMA arithmetic ports across perpetual venues without structural change; the rule reads no volume, so venue volume-definition differences cannot touch it. The rule is two-sided with no stop leg, so a spot-only deployment expresses the long state and reversal-to-flat/short mechanics only to the extent the venue permits shorting — full two-sided expression assumes a futures venue, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source declares `calc_on_every_tick=true` with no `process_orders_on_close` argument (live intrabar recalculation, next-bar backtest fills by language default); this record evaluates completed bars only and executes same-bar-close on `30m` BTCUSDT. Backtest economics of the timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance. Any live intrabar re-entry behavior is out of scope.
- No source economics: beyond Pine defaults the source ships no capital, commission, slippage, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- No price stop, no time stop, no flat state: adverse excursion after placement has no guardrail beyond the opposite-state reversal; a position whose pair never prints the opposite state is held indefinitely. This is the coded posture, disclosed as the record's principal risk.
- Lag and clamp blindness: the Hilbert-plus-double-smoothing stack delays state entries symmetrically, and the `dphase` floor caps alpha at the Fast Limit — cycles faster than one radian per bar earn no faster averaging, while a hard trend without a state flip is ridden without acting. The state-plus-reversal construction is the coded design, disclosed, not smoothed.
- Recursion seed: the 6-lag Hilbert recursions plus the four `.2/.8` smoothers dominate early bars; the first 100 `30m` bars are flat by record rule, so early-history signals never enter any evaluation.
- Commented-stub quarantine: the `pa`/`fr`/`ebc` inputs, the crossover-marker/barcolor/fill plots, and the `possig` reverse stub are inert `//` text in the pinned block — re-enabling any of them is a different, unpinned rule, disclosed here.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record; the six-gate claim is pinned-engine expressibility of the declared rule, never a profitability, parity, or trading authorization.

## Adoption boundary

Research-only, not approved. No live, Paper, or Testnet authorization follows from this record. Any downstream standardized overlay (house DCA/capital/leverage), Qlib screening, or Hummingbot re-validation is a separate, explicitly authorized step outside this record.

## Related Wiki records

None.

## Sources

- https://www.fmz.com/strategy/428090 (primary source — FMZ strategy page, LazyBear-authored Pine block with ekoronin fix, stanza `2023-09-20→2023-09-27`, `30m`, `Futures_Binance BTC_USDT`; fetched live 2026-10-12, 759,059 bytes HTTP 200, zero performance numbers on page)
- https://www.tradingview.com/pine-script-reference/v5/ (Pine semantics reference for census terms — defaults only, never a source of strategy facts)
