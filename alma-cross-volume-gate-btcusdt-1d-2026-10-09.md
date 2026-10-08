---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: ALMA 60/120 cross with volume-oscillator gate two-sided on BTCUSDT 1d bars
created: 2026-10-09
updated: 2026-10-09
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2022-08-27
sources:
  - https://github.com/fmzquant/strategies/blob/master/Arnaud-Legoux-Moving-Average-Cross-ALMA.md
  - https://www.fmz.com/strategy/380250
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# ALMA 60/120 cross with volume-oscillator gate two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (FMZ public strategy mirror plus its embedded Pine block, fetched 2026-10-09):

- Canonical file: https://github.com/fmzquant/strategies/blob/master/Arnaud-Legoux-Moving-Average-Cross-ALMA.md (`Arnaud-Legoux-Moving-Average-Cross-ALMA`, FMZ mirror of Zer3192's FMZ strategy https://www.fmz.com/strategy/380250, FMZ page stamp Created 2022-08-27 17:00:46, adopted as `source_as_of`). Page-stated Pine author is Sarahann999 under MPL-2.0; the TP/SL percentage construction credits kodify.net.
- Pinned commit: `87a415edf7b08065fbcbfbfefb7351cd929e4dbd` (latest commit touching this path, 2024-03-03); the file at that commit is byte-identical to the live file (4662 bytes, sha256 `5f1d48821906a841764266fa6f88c9854be3e6139f070080e752ebabbf9e7df1`, verified by diff before writing). Page-stated FMZ backtest block: `Futures_Binance BTC_USDT`, period `4h`, basePeriod `15m`, 2021-05-08 to 2022-05-07 — FMZ-platform execution context, never presented as Hummingbot semantics (see derived declaration).
- Page-stated rule (verbatim substance): fast ALMA(60, offset 0.85, sigma 6) crossing slow ALMA(120, offset 0.85, sigma 6), gated by a volume oscillator `osc = 100 * (ema(volume, 5) - ema(volume, 10)) / ema(volume, 10) > 0` with entries only when flat, long TP +2% / SL −2.5% and short TP −2% / SL +2.5% off the position average price. The FMZ page ships a backtest-chart image but no readable performance table in its text — this record claims no source-reported performance numbers (see Evidence).
- Full `//@version=5` block read to the last line. Load-bearing defaults pinned verbatim from the argument table and code: `long_entry = true`, `short_entry = true`, both ALMA offsets `0.85`, both sigmas `6`, fast length `60`, slow length `120`, volume EMA lengths `5`/`10`, both take-profits `2%`, both stop-losses `2.5%`, `src = close`.
- Text census over the pinned block: 2 `strategy.entry` calls (`Long`/`strategy.long`, `Short`/`strategy.short`), 2 `strategy.exit` calls (limit+stop off average price, one per side), 0 `strategy.order`, 0 `request.*`, 0 `security(`, 0 `timeframe(`, 0 `process_orders_on_close`, 0 `pyramiding`, 0 `calc_on_every_tick`, 4 `volume` reads (all inside the oscillator gate plus its `nz()` guard), 1 `runtime.error` guard (fires only when the venue supplies zero cumulative volume), 2 `alert(` calls and 2 `plot` calls — display-only, gating no order.
- Licence and rights: Pine is MPL-2.0 (Sarahann999); FMZ page is a public strategy mirror. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly three: (1) research market/timeframe BTCUSDT `1d` (the script is symbol-agnostic over `close`/`volume`; the FMZ block's `4h`/`15m` Futures_Binance context is FMZ-platform execution, not HB-modelable source timing); (2) same-bar-close entry fills on completed-bar decisions (the source sets no `process_orders_on_close`, so its native entries fill on the next tick — this record does not claim next-tick source timing); (3) the two `strategy.exit` limit/stop touch orders are executed as completed-bar-close-confirmed exits at the identical ±% levels (see Signal — the levels, sides, and percentages are unmodified; only the touch-vs-close confirmation changes, because intrabar touch-path fills are not demonstrated on the pinned HB route). All three adaptations are predeclared here, confined to Provenance, Signal, Execution assumptions, and Limitations, with every original claim kept separate above. ALMA lengths/offsets/sigmas, the oscillator formula and its `> 0` gate on both sides, flat-only entries, two-sided direction, and the ±2%/±2.5% risk posture are source-native and unmodified.

Pre-write dedup (2026-10-09): working-tree searches for `alma`, `arnaud`, and `legoux` return zero strategy records computing or trading any Arnaud-Legoux average (no prose mention anywhere in the pool). The volume-oscillator gate `ta.ema(volume` likewise returns zero pool records. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #58 (17-file ML/portfolio reconstruction batch, unmerged — file list verified, no ALMA or moving-average-cross record), and #63 (SuperTrend ATR-flip trend long) — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `ema-20-50-cross-btcusdt-1h-2026-10-06.md` (plain dual-EMA cross, no Gaussian window, no volume gate, no fixed-percentage exits), `dual-ema-engulfing-volume-long-btcusdt-1h-2026-10-07.md` (volume appears, but as an engulfing confirmation on plain EMAs, single-sided long, no ALMA, no percentage risk exits), and `hull-ema-crossover-reversal-btcusdt-1d-2026-10-08.md` (HULL/EMA cross reversal with no volume gate and no TP/SL leg). No pool record evaluates `ta.alma`, latches an ALMA 60/120 cross, gates both sides on a volume momentum oscillator, or exits both sides at asymmetric fixed percentages off average price. Five-axis distinction: mechanism differs (Gaussian-window ALMA cross plus volume-momentum gate plus fixed-percentage risk exits, versus plain-EMA/HULL crosses or oscillator level reversals), signal construction differs (formula below with the pinned (60, 0.85, 6)/(120, 0.85, 6) pair and the (5, 10) volume oscillator — nothing in the pool computes either), exits differ (close-confirmed ±2%/±2.5%-off-average exits on both sides, no matching exit leg in any cross record), source identity differs (FMZ/Zer3192 380250 at pinned commit `87a415e` versus HPotter, TV authors, or paper sources), and direction handling differs (both sides live under their own entries and exits versus long-only or reversal records).

## Economic mechanism

### Source-reported

Gaussian-smoothed trend cross with participation confirmation: the fast ALMA(60) crossing the slow ALMA(120) reads as a low-lag trend turn (the ALMA window concentrates weight near the recent past via offset 0.85 while sigma 6 keeps it smooth), and the `osc > 0` gate demands that short-horizon volume momentum exceed its longer baseline — i.e., the turn must arrive with expanding participation. Risk is hard-capped per trade at −2.5% with profit taken at +2%, so the system is a capped payoff harvester on ALMA turns, not a runner.

### Research interpretation

Turn-with-participation plus asymmetric payoff cap. Unlike plain dual-MA crosses (equal-weighted or exponential memory), the ALMA pair's Gaussian window makes the cross react to the shape of the recent leg rather than its average level, so ranging chop that oscillates inside the window produces fewer cross events than a fast SMA pair would. The volume gate then rejects the quietest of those turns on both sides. The flat-only rule makes the system single-position and event-driven: at most one capped trade per turn, re-armed only after the exit. No leverage, sizing, or cost edge is embedded in the signal; sizing lines are absent from the source beyond percent-of-equity configuration, so the house overlay supplies them (see Execution assumptions).

## Signal

Exact rule as pinned (defaults quoted — inputs unmodified; `ta.alma` is the TradingView v5 built-in Arnaud-Legoux moving average over `src` with the pinned length/offset/sigma triple):

- Averages: `AlmaFast = ta.alma(close, 60, 0.85, 6)`; `AlmaSlow = ta.alma(close, 120, 0.85, 6)`.
- Volume oscillator: `shortVol = ta.ema(nz(volume), 5)`; `longVol = ta.ema(nz(volume), 10)`; `osc = 100 * (shortVol - longVol) / longVol`.
- Cross events (mutually exclusive by construction — `ta.crossover` and `ta.crossunder` of the same pair can never fire on one bar): `buy = ta.crossover(AlmaFast, AlmaSlow)`; `sell = ta.crossunder(AlmaFast, AlmaSlow)`.
- Entries (derived timing, completed-bar decision with same-bar-close fill): `buySignal = buy and osc > 0 and flat`; `sellSignal = sell and osc > 0 and flat`, where `flat` means no open position. Quoted verbatim disclosure: the source gates **both** sides on `osc > 0` (the sell leg does not use `osc < 0`); this asymmetry is source-native, preserved, and never "corrected".
- Exits (predeclared derivation — close-confirmed at identical source levels): while long, exit at the completed-bar close when `close >= avgPrice * 1.02` (take, source `longProfitPerc = 2%`) or `close <= avgPrice * 0.975` (stop, source `longStopPerc = 2.5%`); while short, exit at the completed-bar close when `close <= avgPrice * 0.98` (take, source `shortProfitPerc = 2%`) or `close >= avgPrice * 1.025` (stop, source `shortStopPerc = 2.5%`), where `avgPrice` is the entry fill (the entry-bar close). Exit evaluation starts on the first completed bar after the entry bar. TP and SL levels straddle the entry on opposite sides, so both can never trigger on one close — no ordering rule is needed or invented.
- Display isolation: both `plot` calls (ALMA circles) and both `alert(` calls gate no order condition; restyling, hiding, or removing any of them cannot alter any admitted event.

## Required data

- Completed `1d` bars of BTCUSDT: `close` (both ALMAs) and `volume` (oscillator gate only) from the single candle feed. No `open`, no `high`/`low`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d`. The script takes no timeframe input and makes no live `request.*`/`security(`/`timeframe(` call, so it is single-frame by construction; `1d` is adopted as the research frame because it is a campaign timeframe — never presented as anything beyond that (see Limitations).
- Warmup: the slow ALMA needs 120 bars and a cross needs one prior bar, so this record adopts a 125-completed-bar warmup before any admitted event (covers ALMA seeding plus the volume-EMA(10) seeding with margin). No repainting, no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar, and the volume gate reads only the completed bar's own candle volume.

## Execution assumptions

- Research market: BTCUSDT under the house overlay (the rule reads `close`/`volume` only; venue transfer is never presented as source-native semantics).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution for entries; completed-bar-close-confirmed exits at the source's ±% levels starting the bar after entry. The source's own timing is next-tick entries with intrabar limit/stop touch exits under FMZ-platform context — this record does not claim that timing. No maker-touch, queue, or intrabar-path-dependent fill. There is exactly one deterministic fill price per admitted event (the completed-bar close).
- Sizing/capital: the source carries no quantity line (percent-of-equity configuration only), replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions, never presented as source-native behavior.
- Concurrency: entries require the flat state (source `strategy.position_size == 0` on both legs; `pyramiding` unset, Pine default single position per direction). At most one open position; repeat same-side crosses while in position are rejected no-ops; after any exit the book is flat and the next qualifying cross bar re-enters. Re-entry after flat requires a fresh cross event (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The FMZ page ships the ALMA-cross-plus-volume-gate construction, the full pinned input table (offsets 0.85/0.85, sigmas 6/6, lengths 60/120, volume EMAs 5/10, TP 2%/2%, SL 2.5%/2.5%), the two-sided entry/exit code, and the FMZ backtest block (Futures_Binance BTC_USDT, 4h/15m, 2021-05-08→2022-05-07) with a backtest-chart image but no readable performance table in the mirrored text. This record claims no source-reported performance numbers and no reproduced performance, and does not rely on the page's image. (This record adopts BTCUSDT `1d` as a predeclared research frame and claims no source-venue or source-timeframe semantics.)

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden order paths: 2 `strategy.entry` and 2 `strategy.exit` calls are the complete live order surface; 0 `strategy.order`, 0 multi-leg brackets beyond one limit+stop pair per side, and the alert/plot calls gate nothing.
2. Cross exclusivity proven: `buy` requires `ta.crossover(AlmaFast, AlmaSlow)` while `sell` requires `ta.crossunder` of the same pair — both cannot hold on one bar, so no priority rule is needed or invented.
3. Both-sides `osc > 0` preserved verbatim: the short leg's positive-gate requirement is the source's own text, kept exactly as written; "fixing" it to `osc < 0` would be a different, unpinned rule and is not admitted here.
4. Entry-bar determinism: on the entry bar `avgPrice` equals the fill (the same close), so `close >= avgPrice * 1.02` and `close <= avgPrice * 0.975` are both false — exits cannot co-fire with the entry even if evaluated; evaluation is additionally fenced to start the next bar.
5. Zero-volume edge named: if a venue ever supplied zero volume, `nz(volume)` feeds zeros, the oscillator goes flat/na (comparisons false, no signals), and the source's own `runtime.error` guard names that path — deterministic, with no reviewer invention around it. Division by `longVol` can only be reached with seeded EMA state; a zero denominator yields na, which fails the `> 0` gate safely.
6. Price-field minimalism: `open`, `high`, and `low` are absent from the entire block, so session gaps, opens, and wicks cannot influence any admitted event — gap behavior is absent rather than approximated.
7. The ALMA triples, oscillator lengths, `> 0` threshold, flat-only rule, two-sided direction, and ±2%/±2.5% levels are pinned, not removed: retuning any length/offset/sigma/threshold, dropping the volume gate, adding a cooldown/session filter, or disabling a side would each be a different, unpinned rule — none is admitted here.
8. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT-`1d` research frame, same-bar-close entry fills, and close-confirmed (instead of touch) exits at identical levels — all three predeclared above; every average, threshold, default, state transition, and risk percentage is source-verbatim. This record is therefore never evidence that the FMZ-platform source itself passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: ALMA (60, 0.85, 6)/(120, 0.85, 6) / oscillator (5, 10, `> 0` both sides) / flat-only / two-sided / ±2% TP / ±2.5% SL / `1d` BTCUSDT / close-confirmed execution are frozen.

- F1 — ALMA relevance: replacing the ALMA pair with a plain SMA(60)/SMA(120) cross (same gate, exits, and timing) must not reproduce-or-beat net expectancy; fail ⇒ the Gaussian window adds nothing over a basic average cross and the record is a label variant of one.
- F2 — Volume-gate relevance: removing the `osc > 0` gate (cross-plus-flat entries only, exits kept) must not improve net expectancy; fail ⇒ the participation filter adds nothing over the raw cross.
- F3 — Risk-leg relevance: removing both TP/SL legs (hold until the opposite cross, entries still flat-gated) must not improve net expectancy; fail ⇒ the capped-payoff exits add nothing over cross-to-cross holding.

## Crypto portability

Pinned to BTCUSDT perps under the house overlay. The close/volume two-sided logic ports to perps without structural change; a spot-only deployment would require disabling the short side and would be a different, unpinned rule. No funding-dependent leg, no stablecoin-specific assumption, no session, no cross-venue state. The 24/7 crypto market has no opens/sessions for the rule to read (`open` is never referenced); `close`/`volume` are the completed-bar prints. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived exit confirmation: the source exits on intrabar limit/stop touch; this record exits on completed-bar-close confirmation at identical levels. Touch exits cut losers/winners intrabar while close confirmation can exit a full bar later past the level — backtest economics of the two timings differ by construction. The adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- Derived entry timing: the source fills entries on the next tick after the signal bar; this record fills at the signal-bar close. Same-direction gap moves between close and next tick accrue differently — disclosed, not hidden.
- Always-ready single position: after any exit the system re-arms immediately on the next qualifying cross with no cooldown, so a choppy ALMA-cross cluster can print repeated capped-loss trades with no structural filter — the source provides none and this record invents none.
- Volume-feed dependence: a venue or feed without candle volume degrades to zero signals by construction (plus the source's own error guard); the strategy is not venue-portable to volume-less feeds.
- Both-sides-positive gate: shorts also demand expanding volume momentum, so breakdowns on draining volume never trigger — a source-native blind spot, preserved as written.
- Warmup cost: the adopted 125-bar warmup blinds the first bars of any 1d evaluation window (deterministic seeding, but incomplete ALMA history).
- Performance evidence is absent: the mirrored page reports no readable numbers; nothing here is calibrated, fitted, or tuned to any backtest.

## Implementation status

Not implemented. No Hummingbot controller/executor, no Qlib screening, no Paper/Testnet/Live run has been performed from this record. Admission claims pinned-engine expressibility only (see Execution assumptions), subject to independent six-gate review.

## Adoption boundary

Research-only. Not approved for any downstream screening, parity run, or trading authorization. Only a `PASS` under the live six-gate contract may merge this record into `main`; any `NOT_LOSSLESS` finding closes the PR lane without promotion.

## Related Wiki records

None.

## Sources

- FMZ strategy mirror, pinned commit `87a415edf7b08065fbcbfbfefb7351cd929e4dbd` (fetched 2026-10-09): https://github.com/fmzquant/strategies/blob/master/Arnaud-Legoux-Moving-Average-Cross-ALMA.md
- FMZ canonical strategy page (Zer3192, 2022-08-27): https://www.fmz.com/strategy/380250
- Pine strategy semantics (order calls, default execution, built-in moving averages): https://www.tradingview.com/pine-script-reference/v5/
