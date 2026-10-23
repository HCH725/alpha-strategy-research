---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Gekko varPPO TSI adaptive-threshold regime-flip long-flat on BTCUSDT 1h bars
created: 2026-10-23
updated: 2026-10-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2020-02-16
sources:
  - https://github.com/askmike/gekko/blob/ff5698f1ae6329bab5729f145c35a74161e82bac/strategies/varPPO.js
  - https://github.com/askmike/gekko
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Gekko varPPO TSI adaptive-threshold regime-flip long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifacts for all rule citations):

- Repository URL: https://github.com/askmike/gekko (open-source Gekko crypto backtesting/bot project; no record in the pool cites any file from this repository — first Gekko-sourced record).
- Pinned commit SHA: `ff5698f1ae6329bab5729f145c35a74161e82bac` (committed `2020-02-16T14:25:21Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact strategy file path: `strategies/varPPO.js`.
- GitHub blob SHA at the pinned commit: `3cd2536cf222ab64398e444b33e8f60f474d44ba`, size 3297 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 3297 bytes, 136 lines, SHA-256 `a89f4d945eb81aea48340b0286f856847b35f2409a28e5a9ec552e4b1a16804b`, identical to the GitHub blob (`git hash-object` reproduces `3cd2536c…d44ba`) — the entire file was retrieved and inspected.
- Pinned out-of-file indicator implementations (actually read, all byte-verified against their GitHub blobs this cycle): `strategies/indicators/PPO.js` (37 lines, 1141 bytes, SHA-256 `e30d55e3…58286`, blob `b49e592c…e3db36c`); `strategies/indicators/TSI.js` (38 lines, 968 bytes, SHA-256 `704e3c82…317cc2`, blob `9cf8ee5d…512dc6f2`); `strategies/indicators/EMA.js` (36 lines, 880 bytes, SHA-256 `c8ff11a5…62efeae83`, blob `8e398fca…95c539`, file carries a leading BOM — quoted byte counts include it, formula unaffected).
- Pinned committed configuration (actually read, byte-verified: 538 lines, 13387 bytes, SHA-256 `e999ed7f…9103177d`, blob `34c5092a…e34667221`): `sample-config.js` at the same commit. This is the committed source of every numeric literal the strategy file does not carry inline: `config.tradingAdvisor` (lines 28–33: `candleSize: 60`, `historySize: 10`); `config.PPO` (lines 386–400: `short: 12`, `long: 26`, `signal: 9`); `config.varPPO` (lines 404–414: `momentum: 'TSI'`, `weightLow: 120`, `weightHigh: -120`, `persistence: 0`); `config.TSI` (lines 429–439: `short: 13`, `long: 25`, `thresholds.low: -25`, `thresholds.high: 25`). No other committed file supplies these literals — a reviewer repair may never substitute a sibling constant.
- The strategy file's own words (quoted for gate evidence, never extended): `method.init` (lines 16–29) resets `this.trend = { direction: 'none', duration: 0, persisted: false, adviced: false }`, sets `this.requiredHistory = this.tradingAdvisor.historySize`, and registers `this.addIndicator('ppo', 'PPO', config.PPO)` plus `this.addIndicator(momentumName, momentum, momentumSettings)` where `momentum = settings.momentum` (`'TSI'`) and `momentumName = momentum.toLowerCase()` (`'tsi'`, line 9); `method.update = function(candle)` (lines 32–34) is a documented no-op (`// nothing!`); `method.log` (lines 38–51) prints PPO/PPOsignal/PPOhist/momentum/price diagnostics only — it gates nothing; `method.check` (lines 53–134) computes `thresholds.low = momentumSettings.thresholds.low + hist * settings.thresholds.weightLow` and `thresholds.high = momentumSettings.thresholds.high + hist * settings.thresholds.weightHigh` (lines 59–62), advises `'long'` once per fresh up-regime (lines 82–84), `'short'` once per fresh down-regime (lines 106–108), and soft `this.advice()` everywhere else (lines 86, 110, 131). The sideways-reset block is COMMENTED OUT (lines ~122–129) — the regime stays sticky through sideways bars by code, disclosed, never repaired.
- Indicator arithmetic pinned verbatim: EMA seeds `result = price` on the first update and iterates `result = price * k + y * (1 - k)` with `k = 2 / (weight + 1)` (EMA.js — causal, closed form); PPO builds `shortEMA = EMA(12)`, `longEMA = EMA(26)`, `macd = shortEMA - longEMA`, `ppo = 100 * macd / longEMA`, `PPOsignal = EMA(9, ppo)`, `PPOhist = ppo - PPOsignal` (PPO.js — per-candle close price input, `input = 'price'`); TSI takes `momentum = close - prevClose` (first bar skipped via the `lastClose === null` guard, which sets `lastClose` and returns), `inner = EMA(25, mom)`, `outer = EMA(13, inner)`, mirrored absolute pair, `tsi = 100 * outer.result / absoluteOuter.result` (TSI.js — per-candle `candle.close` input, `input = 'candle'`). No other indicator, library, network, DB, resample, merge, or hyperopt artifact is touched by any order-gating line.
- Fenced-as-unused committed literals (present in the pinned files but read by zero order-gating comparisons — adopting any as a gate would be a different, unpinned rule): the `config.PPO.thresholds` block (`down/up/persistence`, lines 393–398) belongs to the standalone PPO strategy and is never read by `varPPO.js`; `config.TSI.thresholds.persistence` (`1`) is never read (varPPO reads only `momentumSettings.thresholds.low/high`); `method.log` diagnostics and the `log.debug` trend-duration prints condition nothing.
- Full-file token census over the 136-line strategy file (verified by search this cycle): 0 `stop` / 0 `limit` / 0 `trail` (no order arguments, no live risk legs of any kind); 0 `fee` / 0 `slippage` / 0 `commission` (no economics anywhere); 0 `funding` / 0 `mark_price`; 0 `volume` / 0 `open` (no such series read anywhere in the file); 0 `high` / 0 `low` price-series reads (the three `high`/`low` substring hits are the `thresholds.high/low` and `weightHigh/weightLow` field names, lines 60–61/64/88 — field labels, never a bar series); the single `Parameter` hit is the prose comment `calculated parameters` (line 37 — a log comment, no search machinery; the file is plain Node with zero optimizer imports); 0 `hyperopt` / 0 `resample` / 0 `merge` / 0 `request` / 0 `security`; exactly 5 `this.advice` call sites (one `'long'`, one `'short'`, three soft); `method.update` conditions nothing. `check()` reads no candle field directly — every signal input arrives through the two pinned close-only indicators.
- Licence and rights: the repository is open-source (MIT-licensed); this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of a live Gekko deployment. The source pins the `1h` frame (`candleSize: 60` committed default), the PPO(12,26,9) histogram construction, the TSI(13,25) momentum construction, the ±25 histogram-weighted adaptive thresholds, the persistence-0 once-per-regime advice posture, and the sticky-sideways regime — but ships no venue spelling, no fill-timing flag, no position-sizing rule, and no risk leg of any kind. Researcher-declared adaptations are exactly four: (1) research market `BTCUSDT` on Binance (the source is pair-agnostic — no symbol anywhere in the strategy, indicator, or config files; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed); (2) completed-bar decisions with same-bar-close market fills (the source framework evaluates per candle and routes live/paper orders through its own trader; this record freezes completed-bar evaluation with same-bar-close execution and scopes live/order-book behavior out, see Limitations); (3) long-flat direction pin with a 60-bar researcher warmup floor (the source advises both `'long'` and `'short'`; short-side entries are explicitly disabled here — short advices exit a long book and are no-ops when flat — and pre-warmup bars are flat by record rule, see Signal); (4) the source's absent sizing/costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with no safety-order/add tranche activating under the single-unit/no-add pin (see Execution assumptions). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-23): working-tree filename/content search for `varppo`, `varPPO`, `weightlow`, `weighthigh` returns zero strategy records — no record in the pool cites this source file or its histogram-weighted threshold construction. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian band-ratio) trades a TSI-vs-PPO-histogram adaptive-threshold rule, and no open or closed PR has ever carried a Gekko source. PPO/TSI/UO cousins in the pool are fenced as different constructions in Negative evidence 6. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: a variable-threshold PPO-confirmation regime machine (`Uses one of the momentum indicators but adjusts the thresholds when PPO is bullish or bearish` — `sample-config.js` line 403). The TSI momentum value is tested each candle against bands that breathe with the PPO histogram — `new threshold is default threshold + PPOhist * PPOweight` (line 407). A fresh cross into the low side advises long once; a fresh cross into the high side advises short once; sideways prints advise nothing and leave the regime untouched. The files ship no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Histogram-breathed exhaustion flip, long-flat. The TSI leg measures double-smoothed close-momentum while the PPO-histogram leg measures how decisively the 12/26 trend spread sits above or below its own signal — and the two are multiplied together into the decision bands: with no trend conviction (`hist ≈ 0`) the bands sit at the committed ±25 and only genuine TSI extremes fire; with strong bullish conviction (`hist > 0`) the low band rises toward the TSI print (longs trigger sooner) while the high band falls (short-exits trigger sooner) — the machine gets trigger-happy in the trend's favor and quicker to surrender against it. Because persistence is pinned at 0, each regime change fires exactly once on its first bar and then holds silently: a TSI that parks beyond the low band for ten bars prints one entry, not ten, and a long book survives the whole overbought traverse with no profit-taking leg. Unlike fixed-band TSI systems there is no static overbought/oversold line — the bands themselves are the signal's second input. Unlike stop-based systems there is no fixed-distance risk leg — the opposite-regime advice is the sole risk control by construction, so a long whose TSI mean-reverts without ever printing above the live high band is held indefinitely (disclosed disposition risk). The failure mode is plain: a histogram whipping around zero flaps the bands across a sideways TSI and flips the book across consecutive regimes with no cooldown to damp the round trips.

## Signal

Exact rule as pinned (any other PPO/TSI length, threshold, weight, persistence, regime, fill, frame, or book is a different, unpinned rule). All identifiers below are the program's own; `method.check` (lines 53–134) is the single source of truth — `method.update` is a no-op and `method.log` is diagnostic:

```text
ema(N, x)[t]  = x[t]*k + ema(N,x)[t-1]*(1-k), k = 2/(N+1), seeded first price
macd[t]       = EMA(12, close)[t] - EMA(26, close)[t]
ppo[t]        = 100 * macd[t] / EMA(26, close)[t]
signal[t]     = EMA(9, ppo)[t]
hist[t]       = ppo[t] - signal[t]
mom[t]        = close[t] - close[t-1]                       // first bar skipped
tsi[t]        = 100 * EMA(13, EMA(25, mom))[t] / EMA(13, EMA(25, |mom|))[t]
low[t]        = -25 + hist[t] * 120
high[t]       = 25 + hist[t] * (-120)
up-regime     = (tsi[t] < low[t])     // strict
down-regime   = (tsi[t] > high[t])    // strict
long advice   = first bar of a fresh up-regime   // duration 1 >= persistence 0
short advice  = first bar of a fresh down-regime // duration 1 >= persistence 0
entry         = long advice on a flat book  → open full unit long
exit_sig      = short advice on a long book → close full unit flat
```

- Trade events: a flat book opens one full unit on a long-advice bar; a long book closes the full unit on a short-advice bar. Both advices are once-per-regime edges (the `adviced` flag per direction, lines 82–84 / 106–108), not levels — a book already positioned treats further same-regime bars as hold-no-ops (soft advices), and a flat book treats down-regime bars as no-ops. Re-entry re-arms on the next fresh up-regime after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Exact boundaries (pinned semantics): both regime tests are strict (`<`, `>`) — a bar with `tsi == low` or `tsi == high` takes the sideways path and advises nothing; sideways bars advise soft and (per the commented-out reset) never clear the regime, so re-tests of the same side stay silent. Inverted-band overlap (`low > high`, i.e. `hist > 25/120 ≈ 0.2083`) with a print strictly between the bands satisfies the up-test first — the coded `if / else-if` order resolves it to the long branch deterministically; the reviewer is never asked to invent an ordering. Seed bars degrade to soft advice: zero/NaN indicator prints fail both strict tests, so no leg can fire before real history accumulates.
- Mutual-exclusion proof (no tie-break pin required): `check()` executes exactly one of the three paths per bar (coded `if / else-if / else`), so a bar emits at most one advice — long advice and short advice never co-print. The reviewer is never asked to invent a fill order.
- Direction: long-flat (researcher pin, disclosed). The source advises both sides; short-side entries are explicitly disabled here — a short advice on a flat book is a deterministic no-op, never a short sale. A two-sided reading would contradict this record. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the fresh down-regime advice is the complete position-closing set. Stop loss, take profit, trailing stop, ROI target, and time limit ship nowhere in any pinned file and are recorded as explicitly disabled, not as defaults to be assumed. No exit leg reads net profit, fees, or funding — fees change only the performance report, never whether an exit fires (disclosed).
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further long-advice bars as hold-no-ops (no pyramiding, no averaging — no position hook ships anywhere); a flat book treats short-advice bars as no-ops; re-entry re-arms on any fresh up-regime after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `close` (PPO via per-candle close price, TSI via per-candle `candle.close`, both declared `input` routings in the indicator files) through fixed causal EMA/rolling arithmetic with non-negative offsets only. No funding/OI/mark-price read, no `request.*`, no session/calendar call, no resample/merge, no optimizer parameter, and no stop/limit order argument anywhere in the gating path.

## Required data

- Completed `1h` bars of BTCUSDT: `close` only (sole series read — PPO consumes each completed bar's close price; TSI consumes each completed bar's `candle.close`; the strategy file itself reads no bar series directly). No `open`/`high`/`low`/`volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1h` (source-native — `candleSize: 60` committed default, `sample-config.js` line 31). One evaluation per completed bar; every window reads the decision bar's causal past only (plus the decision bar's own completed print); fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 60 completed `1h` bars held flat. Covers the source `requiredHistory = historySize = 10` (line 24) plus the PPO 12/26/9 EMA seeding (~47 bars), the TSI 13/25 double-EMA seeding (~38 bars), and the first-bar TSI skip — with margin. Coded behaviour underneath: unseeded prints fail both strict regime tests (soft advice), so no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same single-frame completed-bar close-evaluated lane primitive the admitted `1h` records (`freqtrade-adx-momentum-di-gated`, `freqtrade-awesome-macd-ao-cross-macd-gated`, `freqtrade-bband-rsi-dip-buy`, `forven-stddev-cross-swing`, `forven-dema-cross`) use. No maker-touch, queue, or intrabar-path-dependent fill: entry and the opposite-regime exit are once-per-regime edges, and the Signal mutual-exclusion proof leaves no ambiguous same-bar fill order, so no intrabar ordering assumption is needed.
- Interval precedent (disclosed, not assumed): `1h` is an already-admitted interval on `main` via the records above — no novel-interval confirmation is required for this frame. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its risk posture is the no-stop signal-flip stance preserved verbatim above, while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal — no safety-order/add tranche activates in this derived version, so position events are fully determined by the regime advices above and sizing changes no event, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; a fresh up-regime opens the full unit on a flat book; a fresh down-regime closes it in full; re-entry after an exit needs only the next fresh up-regime (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The pinned files ship the full construction (136-line regime machine with the once-per-regime advice posture, the 37-line PPO spread/signal/histogram arithmetic, the 38-line TSI double-smoothed momentum arithmetic, the seeded-first-price EMA iteration, and the committed `1h` frame / `12/26/9` / `13/25` / `±25` / `120/-120` / persistence-`0` literals). They ship no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: unseeded EMA/TSI prints fail both strict regime tests (soft advice — hold/flat). The 60-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired. The file's own `requiredHistory = 10` is quoted as the framework minimum, never as the record floor.
2. Exactequality fenced: both regime tests are strict — a bar printing exactly `tsi == low` or `tsi == high` takes the sideways path and advises nothing. Strictness preserved throughout — disclosed, not smoothed.
3. Inverted-band fence: when `hist > 25/120 ≈ 0.2083` the low band sits above the high band; a print strictly between them satisfies the up-test and takes the long branch by coded `if / else-if` order — disclosed, never reordered by repair. Mirrored prints outside both bands follow their own strict test.
4. Sideways-stickiness fence: the regime-reset block is commented out in source — sideways bars advise soft and keep the prior regime armed-state (`adviced` stays true), so drifting out and back into the same side without touching the other side prints nothing. Uncommenting the reset would be a different, unpinned rule.
5. No-edge-confusion fence: advices are once-per-regime edges, not persistent states — converting either advice to a level-hold (act on every in-regime bar) would be a different, unpinned rule with different trade events.
6. Cousin records fenced as different constructions (none trades a TSI print against PPO-histogram-breathed bands with once-per-regime advices, long-flat, with no risk leg): the admitted `forven-ppo-zero-gated-cross` pool-mate gates a PPO cross on the zero line (static gate, cross edge, `1h`, Forven source); the admitted `ppo-signal-cross-reversal` pool-mate trades PPO-vs-signal cross edges (two-sided, `1d`); the admitted `eterna-tsi-25-13-13-dual-path-gated-cross` pool-mate trades TSI dual-path cross edges behind its own gate (`4h`); the admitted `tsi-signal-cross-reversal` pool-mate trades a TSI-vs-signal cross (`1d`); the admitted `forven-ultimate-oscillator-cross-gated` and `ultimate-oscillator-oversold-breakout` pool-mates trade a different oscillator (7/14/28 triple-weighted UO, never TSI-vs-histogram bands). Not a threshold re-tuning of any of them: moving any PPO/TSI length, either base threshold, either histogram weight, the persistence, the advice posture, or the frame would each be a different, unpinned rule — none is admitted here.
7. Sibling-config fence: the `config.PPO.thresholds` block, `config.TSI.thresholds.persistence`, `method.log` diagnostics, and every other strategy section in `sample-config.js` are separate pins — their constants and semantics must never be substituted into this record.
8. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT market choice, the same-bar-close fills, the long-flat direction pin (short entries disabled), the 60-bar warmup floor (the source minimum is 10), and house sizing/costs with safety tranches deactivated — all predeclared above. The `1h` frame, the PPO(12,26,9) histogram arithmetic, the TSI(13,25) construction, the ±25 base bands with 120/−120 histogram weights, the persistence-0 once-per-regime advice posture, the sticky-sideways regime, the strict comparisons, and the no-stop stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: PPO(12,26,9) / TSI(13,25) / ±25 base bands / 120/−120 histogram weights / persistence-0 once-per-regime advices / sticky-sideways regime / long-flat / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Histogram-weight relevance: freezing the bands at the static ±25 (both weights to 0, same advices otherwise) must not improve net expectancy; fail ⇒ the PPO-histogram breathing adds nothing over its fixed-band twin.
- F2 — Momentum-choice relevance: replacing the TSI(13,25) print with the committed RSI(14) print against its own ±(30/70-derived) static bands (same histogram weights, same posture) must not improve net expectancy; fail ⇒ the TSI leg adds nothing over the config's sibling momentum input.
- F3 — Exit-leg relevance: replacing the opposite-regime exit with a fixed 5% stop (same entries otherwise, same fills) must not improve net expectancy; fail ⇒ the down-regime exit adds nothing over a bare distance stop.

## Crypto portability

BTCUSDT Binance perpetual `1h` is the research pin (source names no market; the `1h` frame is the committed `candleSize: 60` default). Long-flat with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. The rule reads completed-bar `close` only, so venue volume-definition differences cannot move any leg, disclosed. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- The `1h` frame rides existing admission precedent (ADXMomentum, AwesomeMacd, BbandRsi, StdDev-cross-swing, DEMA-cross `1h`) — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- A long whose TSI mean-reverts without ever printing above the live high band is held indefinitely (bounded by no stop of any kind); a histogram whipping around zero flaps the bands and flips the book across consecutive regimes with no cooldown to damp the round trips — disclosed as the principal risk and friction. There is no decay, chop, trend-loss, profit-taking, or further time exit — disclosed, not repaired.
- Gekko live/paper-trader order routing, queue/maker semantics, and multi-candle limit behaviour are scoped out by the derived same-bar-close market-fill pin — backtest economics of the timings differ by construction, disclosed, and this record makes no claim about the source engine's live behaviour or performance.
- Indicator seeding internals (first-price EMA seeding, first-bar TSI skip, NaN/zero-division degradation to soft advice) live in the pinned indicator files outside the strategy file — pinned by call with explicit lengths, not re-derived; exact reproduction inherits those seedings alongside the 60-bar floor.
- No trailing, no breakeven, no short entry, no cooldown — all explicitly absent, never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write is performed by the Scout lane.

## Sources

- https://github.com/askmike/gekko/blob/ff5698f1ae6329bab5729f145c35a74161e82bac/strategies/varPPO.js
- https://github.com/askmike/gekko
