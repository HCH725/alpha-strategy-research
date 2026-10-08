---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Vortex spread-threshold EMA-smoothed two-sided on BTCUSDT 1d bars
created: 2026-10-09
updated: 2026-10-09
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-11-14
sources:
  - https://www.fmz.com/strategy/432100
  - https://www.tradingview.com/pine-script-reference/v4/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Vortex spread-threshold EMA-smoothed two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (FMZ public strategy page plus its fully embedded `//@version=4` Pine block, fetched 2026-10-09):

- Canonical page: https://www.fmz.com/strategy/432100 (`Quantitative Trading Strategy Based on Improved Vortex Indicator`, FMZ author ChaoZhang, page-stated creation `2023-11-14 14:40:54`, adopted as `source_as_of`). Page-stated Pine lineage is `[Guz]` (script title `%-[Guz] Vortex Indicator Custom`); the 10%-size/0.04%-fee remark lives only in a code comment crediting crypto futures conventions, not in any executable line.
- Page-stated FMZ backtest block: `Futures_Binance BTC_USDT`, period `1h`, basePeriod `15m`, 2023-10-14 to 2023-11-13 — FMZ-platform execution context, never presented as Hummingbot semantics (see derived declaration).
- Page-stated rule (verbatim substance): EMA-smoothed Vortex spread `VIP − VIM` triggers entries only past an asymmetric ±threshold (`crossover(spread, +0.162)` long, `crossunder(spread, −0.162)` short), any zero-cross of the spread (`cross(spread, 0)`) closes everything via `strategy.close_all()`, and each side carries its own limit+stop exit off the position average price (long TP +1.5% / SL −2.5%, short TP −1.7% / SL +2.5%). Both direction toggles default true. The FMZ page ships a backtest-chart image and "performs well" prose but no readable performance table in its text — this record claims no source-reported performance numbers (see Evidence).
- Full block read to the last line (the embedded `source` field terminates immediately after the `TP-SL Short` exit line; fetched page sha256 `b3480400…`, trailing JSON state verified as non-strategy payload). Load-bearing defaults pinned verbatim: `period_ = 300`, `ema_len = 7`, `tresh = 16.2`, `is_short = true`, `is_long = true`, long SL/TP `2.5%`/`1.5%`, short SL/TP `2.5%`/`1.7%`.
- Text census over the pinned block: 9 `input(` calls, 2 `strategy.entry` calls (`VortexLE`/`strategy.long`, `VortexSE`/`strategy.short`), 1 `strategy.close_all()`, 2 `strategy.exit` calls (limit+stop off average price, one per side), 0 `strategy.order`, 0 `request.*`, 0 `security(`, 0 `process_orders_on_close`, 0 `pyramiding`, 0 `calc_on_every_tick`, 0 `volume` reads, 4 `strategy.position_avg_price` reads (all inside the four TP/SL level lines), 1 `crossover`, 1 `crossunder`, 1 `cross` (the zero-cross close). The `strategy(...)` header sets only title/shorttitle/overlay — no capital, quantity, commission, or slippage line. Both `plot(VIP/VIM)` lines, the equity plot, and the trailing-stop arguments are commented out — display-only or dead text gating no order.
- Licence and rights: page is a public FMZ strategy; Pine comments disclaim investment advice. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) research market/timeframe BTCUSDT `1d` (the script is symbol-agnostic over OHLC; the FMZ block's `1h`/`15m` Futures_Binance context is FMZ-platform execution, not HB-modelable source timing); (2) same-bar-close entry fills on completed-bar decisions (the source sets no `process_orders_on_close`, so its native entries fill on the next tick — this record does not claim next-tick source timing); (3) the two `strategy.exit` limit/stop touch orders are executed as completed-bar-close-confirmed exits at the identical ±% levels (see Signal — the levels, sides, and percentages are unmodified; only the touch-vs-close confirmation changes, because intrabar touch-path fills are not demonstrated on the pinned HB route); (4) atomic-bar evaluation gated on flat-at-bar-start with TP/SL-over-signal-close exit priority (the source's same-bar entry-then-`close_all` sequencing and resting-touch-vs-market-close race are unfalsifiable on the pinned route — this record picks one deterministic order and discloses it, never presenting it as source-native semantics). All four adaptations are predeclared here, confined to Provenance, Signal, Execution assumptions, and Limitations, with every original claim kept separate above. Vortex length/EMA/threshold, the spread formulas, the zero-cross close, flat single-position handling, two-sided direction, and the asymmetric TP/SL percentages are source-native and unmodified.

Pre-write dedup (2026-10-09): working-tree searches for `vortex`, `VIP`, and `VIM` return zero strategy records computing or trading any Vortex construction (no prose mention anywhere in the pool). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #58 (17-file ML/portfolio reconstruction batch, unmerged — file list verified, no Vortex or spread-threshold record), and #63 (SuperTrend ATR-flip trend long) — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `stochastic-ott-dual-trend-btcusdt-1d-2026-10-06.md` (oscillator-plus-trendfilter dual confirmation, no Vortex construction, no spread-threshold triggers, no zero-cross close), `dmi-swings-contrarian-adx-btcusdt-1d-2026-10-06.md` (directional-movement family, no Vortex sums, no threshold-spread entries), and `triple-ema-volstop-tp-long-btcusdt-1d-2026-10-08.md` (EMA-structure exits, single-sided long, no Vortex signal). No pool record evaluates `sum(abs(high − low[1]))`, normalizes by summed ATR, EMA-smooths a VI+/VI− spread, triggers entries on asymmetric ±0.162 spread-threshold crosses, or closes all positions on a spread zero-cross. Five-axis distinction: mechanism differs (Vortex-spread threshold-break plus zero-cross flattening plus fixed-percentage risk exits, versus MA crosses, oscillator level reversals, or channel breakouts), signal construction differs (formula below with the pinned (300, 7, 16.2) triple — nothing in the pool computes it), exits differ (zero-cross signal close plus close-confirmed asymmetric TP/SL legs on both sides, no matching exit leg in any record), source identity differs (FMZ 432100 ChaoZhang/[Guz], 2023-11-14, versus HPotter, TV authors, or paper sources), and direction handling differs (both sides live under their own entries, a shared flattening close, and per-side asymmetric risk, versus long-only or symmetric-risk records).

## Economic mechanism

### Source-reported

Smoothed vortex-spread breakout with securing flattening: the EMA(7)-smoothed difference between normalized positive and negative vortex movement must stretch past ±0.162 before either side fires, so quiet chop where the two vortex lines merely tangle never triggers; any decay of the spread back through zero flattens the whole book. Risk is hard-capped per trade (long −2.5%, short −2.5%) with asymmetric profit-taking (long +1.5%, short +1.7%), so the system is a capped payoff harvester on vortex-spread thrusts, not a runner.

### Research interpretation

Thrust-past-threshold plus always-armed flattening. Unlike raw VI+/VI− cross systems (every tangle fires), the ±0.162 spread gate plus EMA(7) smoothing makes the entry a high-conviction-dominance event: the normalized vortex imbalance must be both large and persistent enough to survive smoothing. The zero-cross `close_all` then acts as a regime-invalidated stop that needs no price level — a spread that can no longer hold its sign exits even before any TP/SL prints. The flat-at-bar-start gating makes the system single-position and event-driven: at most one capped trade per thrust, re-armed only after the exit, with no leverage, sizing, or cost edge embedded in the signal (the `strategy(...)` header carries no quantity/commission line, so the house overlay supplies them — see Execution assumptions).

## Signal

Exact rule as pinned (`ta` forms below are the Pine v4 built-ins; `sum`/`ema`/`atr`/`crossover`/`crossunder`/`cross` per the v4 reference; defaults quoted — inputs unmodified):

- Vortex sums over `period_ = 300`: `VMP = sum(abs(high − low[1]), 300)`; `VMM = sum(abs(low − high[1]), 300)`; `STR = sum(atr(1), 300)`.
- Smoothed lines (`ema_len = 7`): `VIP = ema(VMP / STR, 7)`; `VIM = ema(VMM / STR, 7)`; `spread = VIP − VIM`.
- Events (`tresh = 16.2`, so `tresh / 100 = 0.162`): `longEvent = crossover(spread, +0.162)`; `shortEvent = crossunder(spread, −0.162)`; `closeEvent = cross(spread, 0)`. Long and short events are mutually exclusive by construction (the spread cannot cross above +0.162 and below −0.162 on one bar) — no entry-side priority is needed or invented. Quoted verbatim disclosure: the short trigger uses `−tresh/100` while the long uses `+tresh/100`, and the take-profit percentages are asymmetric (`1.5%` long vs `1.7%` short); both asymmetries are source-native, preserved, and never "corrected".
- Entries (derived timing, completed-bar decision with same-bar-close fill, flat-at-bar-start only): if flat at the bar start and `longEvent` and `is_long` (default true) → enter long at the close; if flat at the bar start and `shortEvent` and `is_short` (default true) → enter short at the close. Entries while in position are rejected no-ops (see Negative evidence for the source-faithfulness of flat gating).
- Exits (predeclared derivation — close-confirmed at identical source levels, evaluated from the first completed bar after the entry bar): while long, exit at the completed-bar close when `close >= avgPrice * 1.015` (take, source `take_profit_long_percent = 1.5%`), `close <= avgPrice * 0.975` (stop, source `stop_loss_long_percent = 2.5%`), or `closeEvent` (source `strategy.close_all()`); while short, exit at the completed-bar close when `close <= avgPrice * 0.983` (take, source `take_profit_short_percent = 1.7%`), `close >= avgPrice * 1.025` (stop, source `stop_loss_short_percent = 2.5%`), or `closeEvent`, where `avgPrice` is the entry fill (the entry-bar close). TP and SL levels straddle the entry on opposite sides, so both can never trigger on one close. If a TP/SL level and `closeEvent` fire on the same bar, the TP/SL exit takes precedence (predeclared researcher priority — the source's resting-touch-vs-market-close race is unfalsifiable on the pinned route, so this record fixes one order and discloses it).
- Display isolation: both commented `plot(VIP/VIM)` lines, the commented equity plot, the commented trailing-stop arguments, and the `10% position size / 0.04% fee` prose comment gate no order condition; restyling, enabling, or removing any of them cannot alter any admitted event.

## Required data

- Completed `1d` bars of BTCUSDT: `high`, `low`, `close` (vortex sums plus `atr(1)`, which additionally reads `close[1]`). No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d`. The script takes no timeframe input and makes no live `request.*`/`security(`/`timeframe(` call, so it is single-frame by construction; `1d` is adopted as the research frame because it is a campaign timeframe — never presented as anything beyond that (see Limitations).
- Warmup: the vortex sums need 300 bars, the EMA(7) needs seeding, and each event needs one prior bar, so this record adopts a 312-completed-bar warmup before any admitted event (300 + 7 + 1 + 4 margin). No repainting, no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT under the house overlay (the rule reads OHLC only; venue transfer is never presented as source-native semantics).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution for entries; completed-bar-close-confirmed exits at the source's levels (or on the zero-cross signal) starting the bar after entry. The source's own timing is next-tick entries with intrabar limit/stop touch exits plus a next-tick market flatten under FMZ-platform context — this record does not claim that timing. No maker-touch, queue, or intrabar-path-dependent fill. There is exactly one deterministic fill price per admitted event (the completed-bar close).
- Sizing/capital: the source header carries no quantity line (the 10% size remark is prose, not code), replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions, never presented as source-native behavior. The 0.04% fee remark is likewise prose, not an executed commission line.
- Concurrency: flat-at-bar-start single position (source `pyramiding` unset → Pine default single position per direction; same-side re-entries rejected; opposite-threshold traverses pass through the zero-cross flatten first — see Negative evidence). At most one open position; after any exit the book is flat and only a fresh threshold-cross bar re-enters (no cooldown specified — explicitly none, not invented). A full traverse bar (exit signal plus opposite entry signal on one bar while in position) exits at the close and does not flip — re-entry needs a fresh cross on a later bar. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The FMZ page ships the smoothed-Vortex-spread construction, the full pinned input table (Length 300, EMA Length 7, Threshold 16.2, both direction toggles true, SL/TP 2.5%/1.5% long and 2.5%/1.7% short), the two-sided entry/flatten/exit code, and the FMZ backtest block (Futures_Binance BTC_USDT, 1h/15m, 2023-10-14→2023-11-13) with a backtest-chart image and "performs well" prose but no readable performance table in the page text. This record claims no source-reported performance numbers and no reproduced performance, and does not rely on the page's image. (This record adopts BTCUSDT `1d` as a predeclared research frame and claims no source-venue or source-timeframe semantics.)

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden order paths: 2 `strategy.entry`, 1 `strategy.close_all`, and 2 `strategy.exit` calls are the complete live order surface; 0 `strategy.order`, 0 multi-leg brackets beyond one limit+stop pair per side, and all plot/equity/trail lines are commented out.
2. Entry exclusivity proven: `longEvent` requires `crossover(spread, +0.162)` while `shortEvent` requires `crossunder(spread, −0.162)` — both cannot hold on one bar, so no entry-side priority rule is needed or invented.
3. Flat gating is source-faithful, not a researcher restriction: `pyramiding` is unset (Pine default rejects same-direction re-entries), and any opposite-threshold traverse must cross the zero line between +0.162 and −0.162, where `condition_close` fires the flatten first (script order places entries before `close_all`, so a same-bar traverse resolves to flat, never to a held reversal). The derived flat-at-bar-start rule reproduces exactly this outcome.
4. Entry-bar determinism: on the entry bar `avgPrice` equals the fill (the same close), so no TP/SL level can trigger on the entry bar even if evaluated; evaluation is additionally fenced to start the next bar.
5. TP/SL straddle proven: long levels sit at ×1.015/×0.975 and short levels at ×0.983/×1.025 — each pair straddles the entry on opposite sides, so TP and SL can never co-fire on one close; only the TP/SL-vs-zero-cross tie needed a rule, and it is predeclared above rather than hidden.
6. Asymmetries preserved verbatim: the ±threshold pair is symmetric but the take-profits (`1.5%` vs `1.7%`) are not; "fixing" the short TP to `1.5%` would be a different, unpinned rule and is not admitted here.
7. Price-field minimalism: `open` and `volume` are absent from the entire block, so session gaps, opens, and participation data cannot influence any admitted event — gap/volume behavior is absent rather than approximated.
8. The (300, 7, 16.2) triple, the zero-cross flatten, the flat single-position handling, two-sided direction, and the asymmetric TP/SL percentages are pinned, not removed: retuning any length/threshold, dropping the EMA smoothing or the flatten, adding a cooldown/session filter, or disabling a side would each be a different, unpinned rule — none is admitted here.
9. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT-`1d` research frame, same-bar-close entry fills, close-confirmed (instead of touch) exits at identical levels, and the atomic-bar priority order — all four predeclared above; every sum, ratio, threshold, default, state transition, and risk percentage is source-verbatim. This record is therefore never evidence that the FMZ-platform source itself passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: Vortex (300, 7, ±0.162) / flat-only / two-sided / zero-cross flatten / long +1.5%/−2.5% / short −1.7%/+2.5% / `1d` BTCUSDT / close-confirmed execution are frozen.

- F1 — Threshold relevance: replacing the ±0.162 threshold triggers with plain zero-cross entries (enter on `cross(spread, 0)` direction, flatten/exits kept) must not reproduce-or-beat net expectancy; fail ⇒ the spread gate adds nothing over a raw vortex cross and the record is a label variant of one.
- F2 — Smoothing relevance: removing the EMA(7) smoothing (raw `VMP/STR` vs `VMM/STR` spread, same thresholds and exits) must not improve net expectancy; fail ⇒ the smoothing adds nothing over the raw vortex ratio spread.
- F3 — Risk-leg relevance: removing both TP/SL legs (hold until the zero-cross flatten, entries still flat-gated) must not improve net expectancy; fail ⇒ the capped-payoff exits add nothing over signal-to-signal holding.

## Crypto portability

Pinned to BTCUSDT perps under the house overlay. The OHLC-only two-sided logic ports to perps without structural change; a spot-only deployment would require disabling the short side and would be a different, unpinned rule. No funding-dependent leg, no volume-feed dependence, no stablecoin-specific assumption, no session, no cross-venue state. The 24/7 crypto market has no opens/sessions for the rule to read (`open` is never referenced). Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived exit confirmation: the source exits on intrabar limit/stop touch plus a next-tick market flatten; this record exits on completed-bar-close confirmation at identical levels (TP/SL priority over the signal close). Touch exits cut losers/winners intrabar while close confirmation can exit a full bar later past the level — backtest economics of the two timings differ by construction. The adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- Derived entry timing: the source fills entries on the next tick after the signal bar; this record fills at the signal-bar close. Same-direction gap moves between close and next tick accrue differently — disclosed, not hidden.
- No same-bar flip: a traverse bar while in position exits flat and waits for a fresh threshold cross; a fast V-shaped spread traverse can therefore sit out the reversal leg entirely — the derived consequence of atomic-bar gating, disclosed as specified.
- Always-ready single position: after any exit the system re-arms immediately with no cooldown, so a spread whipsawing around ±0.162 can print repeated capped-loss trades with no structural filter — the source provides none and this record invents none.
- Warmup cost: the adopted 312-bar warmup blinds the first bars of any 1d evaluation window (deterministic seeding, but incomplete vortex history).
- Performance evidence is absent: the page reports no readable numbers; nothing here is calibrated, fitted, or tuned to any backtest.

## Implementation status

Not implemented. No Hummingbot controller/executor, no Qlib screening, no Paper/Testnet/Live run has been performed from this record. Admission claims pinned-engine expressibility only (see Execution assumptions), subject to independent six-gate review.

## Adoption boundary

Research-only. Not approved for any downstream screening, parity run, or trading authorization. Only a `PASS` under the live six-gate contract may merge this record into `main`; any `NOT_LOSSLESS` finding closes the PR lane without promotion.

## Related Wiki records

None.

## Sources

- FMZ canonical strategy page (ChaoZhang, Pine lineage [Guz], 2023-11-14, fetched 2026-10-09): https://www.fmz.com/strategy/432100
- Pine v4 strategy semantics (order calls, default execution, built-in functions): https://www.tradingview.com/pine-script-reference/v4/
