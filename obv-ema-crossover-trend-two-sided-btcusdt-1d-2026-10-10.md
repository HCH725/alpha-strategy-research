---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: OBV ATR-scaled EMA6/24-crossover trend two-sided on BTCUSDT 1d bars
created: 2026-10-10
updated: 2026-10-10
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-02-20
sources:
  - https://www.fmz.com/strategy/442252
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E5%9F%BA%E4%BA%8EOBV%E6%8C%87%E6%A0%87%E7%9A%84%E8%B6%8B%E5%8A%BF%E8%B7%9F%E8%B8%AA%E7%AD%96%E7%95%A5OBV-EMA-Crossover-Trend-Following-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# OBV ATR-scaled EMA6/24-crossover trend two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (canonical FMZ page fetched over HTTPS during this cycle plus the immutable GitHub mirror at the pinned commit):

- Canonical page: https://www.fmz.com/strategy/442252 (page title `OBV EMA Crossover Trend Following Strategy | FMZ`, publisher account `ChaoZhang`, `Created` 2024-02-20 15:35:08 — adopted as `source_as_of`). Fetched during this cycle (778994 bytes): the page states the rule in both languages (calculate the 6-day EMA and 24-day EMA of OBV; 6-day EMA crossing above 24-day EMA generates a long signal; crossing below generates a short signal; 3% stop loss), the `/*backtest ... */` header (`start: 2024-01-01 00:00:00`, `end: 2024-01-31 23:59:59`, `period: 1h`, `basePeriod: 15m`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`, each marker byte-present twice on the page), and the strategy header (`strategy("OBV EMA X BF 🚀", overlay=false, initial_capital=10000, default_qty_type=strategy.percent_of_equity, default_qty_value=100, commission_type=strategy.commission.percent, commission_value=0.0)`). Word-boundary counts over the whole landing HTML: `Net Profit` 0, `Profit Factor` 0, `Sharpe` 0, `Win Rate` 0, `Max Drawdown` 0, `Annualized` 0, `Total Profit` 0, `Return` 0 — the page ships no performance numbers of any kind.
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit date 2025-04-30, the same head pin as the merged Double-Seven, DPO-EMA, KST, Schaff, TRIX, SQZMOM-LB, Aroon, Qstick, AC, Elder-ray, ActionZone and Connors-RSI2 admissions), exact file path `基于OBV指标的趋势跟踪策略OBV-EMA-Crossover-Trend-Following-Strategy.md` (non-ASCII filename preserved verbatim; percent-encoded blob URL in Sources). File 10166 bytes, blob SHA `310d14192735d558ef7de9d7385411a4d9f29619` (verified against the GitHub contents API at the pinned commit — size and SHA both match). The mirror prints `> Detail` = https://www.fmz.com/strategy/442252, `> Author` = ChaoZhang, and `> Last Modified` = 2024-02-20 15:35:08 (equal to the page stamp).
- Text census over the pinned Pine block: 2 `strategy.entry` (`"L"` long on the raw fast-over-slow cross, `"S"` short on the raw cross-under) / 2 `strategy.exit` (`"L SL"` / `"S SL"`, both `stop=` only, zero `limit=` legs) / 12 `input(` call lines (6 dead date inputs, ATR Period, ATR Mult, the two anonymous EMA lengths 24/6, Stop Loss % 3.0, Take Profit % 5000.0) / 3 code `crossover` calls + 1 code `crossunder` call (raw cross pair plus the alternation-filtered `long_signal`/`short_signal` pair that drives only SL bookkeeping, never entries) / `volume` on 1 code line (5 occurrences inside the single OBV formula) plus 2 prose lines / `take_level_l/s` computed but read 0 times by any exit / `atrmult` defined once and read 0 times / `last_high/last_low` computed (5 occurrences) and read 0 times by any order / `testPeriod() => true` unconditionally (all date inputs dead). The full OBV line reads `obv = cum(change(src) > 0 ? volume * (volume / atr) : change(src) < 0 ? -volume * (volume / atr) : 0 * volume / atr)` with `src = close` and `atr = atr(input(title="ATR Period", defval=3, minval=1))` — an ATR-scaled (volume-squared-over-ATR) OBV variant, not textbook Granville OBV, pinned exactly as written.
- No take-profit, trailing, time-exit, date-filter, ATR-multiplier, or high/low-breakout leg ships anywhere in executable form: the only position-closing paths are the 3% stop legs and the opposite raw-cross entry reversing the unit. The stop-only risk posture below is therefore the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention.
- Page/mirror performance language is absent entirely (no table, figure, or number) — this record claims no source-reported performance and no reproduced performance.

Licence and rights: the canonical page is a public FMZ strategy publication by ChaoZhang with no licence header in the artifact. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly five: (1) research market/timeframe BTCUSDT `1d` (the script's arithmetic reads `close/high/low/volume` only and is symbol-agnostic; the FMZ block's `1h`/`15m` Futures-Binance context is FMZ-platform execution, not HB-modelable source timing — same port rationale as the admitted Connors-RSI2 record, whose source block was `15m`/`15m`); (2) same-bar-close fills on completed-bar decisions (the Pine block ships no `process_orders_on_close`, so its default timing is next-bar-open — this record does not claim source timing); (3) an adopted 120-bar warmup with pre-warmup bars flat by record rule (the EMA24 leg needs 24 completed bars; 120 covers seeding plus the cumulative-OBV baseline transient with margin — see Required data); (4) house sizing/capital/costs replacing the block's 100%-equity/zero-commission configuration (see Execution assumptions; the Pine no-pyramiding default is preserved as the single-position rule); (5) the stop fill basis is the derived close-fill average price with range-evaluated stop-market semantics (the source stop is an intrabar stop order off its own fills — this record does not claim identical intrabar paths, only the same stop price, trigger side, and arming rule). Formula, ATR period, EMA lengths, cross-edge definitions, strict inequalities, both entry IDs, both stop legs with the 3% literal, the post-entry arming gate, two-sided direction, and every dead-code exclusion are source-native and unmodified.

Pre-write dedup (2026-10-10): working-tree word-boundary searches for `OBV` return zero strategy records using any On-Balance Volume construction — no pool record computes any cumulative volume signal; `442252` and `OBV-EMA-Crossover` return zero; same-publisher ChaoZhang records exist but are mechanism-different (CMF-velocity FMZ-lane, Qstick FMZ 439854, KST FMZ 436493, Aroon FMZ 438795, TRIX FMZ 428683, Schaff FMZ-lane — different FMZ IDs, indicators, and rules). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Five-axis distinction: mechanism differs (ATR-scaled cumulative volume-flow dual-EMA cross with a hard 3% stop — the pool's Klinger record is a volume×trend EMA-difference oscillator with different construction, different risk, and no OBV cum; the CMF record is a money-flow ratio; every price-EMA-cross record reads price only and never volume), signal construction differs (`cum` of signed volume-squared-over-ATR3 crossed 6-over-24, versus price crosses, oscillator crosses, or band touches), exits differ (3% stop-market plus opposite-cross full reversal, no target/trailing/time variant matches), source identity differs (FMZ 442252 ChaoZhang Feb-2024 versus other FMZ IDs or TV authors), and direction handling differs (symmetric two-sided with an explicit post-stop flat state versus long-only or always-in-market holders).

## Economic mechanism

### Source-reported

Volume-weighted trend riding (mirror title `OBV-EMA-Crossover-Trend-Following-Strategy`): the dual EMA lines of the OBV judge whether OBV itself is in an uptrend, and positions follow that trend direction long/short; volume reflects participants' collective intent so the signal is claimed more reliable than price-only crosses, while the fast/slow EMA pair filters noise yet stays sensitive to trend change. The design bets that sustained signed-volume accumulation (uptrend) or distribution (downtrend) persists once the fast OBV average confirms above/below the slow one, with a fixed 3% stop as the sole guardrail.

### Research interpretation

Cumulative-flow regime holding with a hard stop, two-sided. Unlike the pool's Klinger record (an EMA-difference of volume×trend that fires on oscillator triggers), this system never normalizes flow into a bounded oscillator — it rides the raw cumulative scaled-volume total through two nested smoothings (ATR3 scaling, then EMA6/EMA24), so slow institutional-style accumulation that never spikes any oscillator still drags the fast average over the slow one. Unlike price-EMA-cross systems it can stay positioned through price chop that whips price crosses, provided signed volume keeps accumulating; mirror-wise, a price breakout on collapsing volume fires nothing here. Unlike always-in-market reversal holders, the stop leg creates a genuine flat state: a stopped-out position waits for the next raw cross rather than flipping immediately. The bet is on multi-day signed-volume persistence at the ~weeks scale under a 24-bar structural leg, not on any price level, band, calendar effect, or volatility envelope.

## Signal

Exact rule as pinned (ATR 3, EMA 6/24, stop 3%, Pine v4 builtins, strict edges — any other value is a different, unpinned rule):

- Lines (pinned): `src = close`; `atr3 = atr(3)` (Pine v4 Wilder-RMA true-range average over `high/low/close`, literal 3); `obv[t] = obv[t-1] + f[t]`, seeded 0 before the first available bar, with `f[t] = +volume[t]*(volume[t]/atr3[t])` if `close[t] > close[t-1]`, `-volume[t]*(volume[t]/atr3[t])` if `close[t] < close[t-1]`, and exactly `0` on equal closes; `e_slow = ema(obv, 24)`; `e_fast = ema(obv, 6)` (Pine `ema`, α = 2/(n+1), SMA-seeded at length bars, `na` before — `na` comparisons are false so no edge can fire pre-seeding, coded behavior, disclosed).
- Entry long: `long_event = crossover(e_fast, e_slow)` (strict: `e_fast[t-1] <= e_slow[t-1]` and `e_fast[t] > e_slow[t]`) while flat → buy-open long at the same-bar close under the derived declaration.
- Entry short: `short_event = crossunder(e_fast, e_slow)` (strict mirror) while flat → sell-open short at the same-bar close.
- Reversal: a contra-side raw event while positioned closes the full unit and opens the full contra unit at the same single close price (one net fill step — the Pine `strategy.entry("S")`-while-long reversal mapped onto the derived fill; no same-bar ordering ambiguity exists because entry, reversal, and close share one decision price).
- Same-side refire while positioned is a no-op (Pine default no-pyramiding preserved as the single-position rule); an exit signal while flat is a no-op.
- Stop (pinned, the sole risk leg): long stop price = entry fill × 0.97, short stop price = entry fill × 1.03 (literal `input 3.0`). Stop-market semantics: triggered when a post-entry bar's range touches the stop price on the adverse side (`low` for longs, `high` for shorts), filled at the stop price, armed from the bar after entry (source `when=since_longEntry > 0` / `when=since_shortEntry > 0` — the entry bar's own excursion is unprotected by code, disclosed). One stop order per position (same-ID replacement); while flat no stop exists. After a stop fill the book is flat until the next raw cross (no automatic re-entry, no cooldown specified — explicitly none, not invented).
- Direction: two-sided with an explicit flat state (pre-first-signal flat by construction; post-stop flat until the next raw event).
- Risk legs (pinned dead code, not invented): the `Take Profit %` input (5000.0) is never wired — `take_level_l/s` are computed and read 0 times, so no target exists; `atrmult` (defval 1) is read 0 times, so no ATR-multiplier leg exists; `last_high/last_low` are read 0 times by any order, so no high/low-breakout exit exists; `testPeriod()` returns true unconditionally, so no date/session filter exists; no trailing, no time exit anywhere.
- Display/plumbing isolation: the two `plot(` legs and two `bgcolor(` legs render only and gate no order; the `last_long/last_short/last_open_*` alternation-filtered signals drive only the SL arming bookkeeping, never entries (entries read the raw cross pair — preserved exactly as written).

## Required data

- Completed `1d` bars of BTCUSDT: `close`, `high`, `low`, `volume` (`high`/`low` enter solely inside `atr(3)`; `close` enters `src`, the sign test, and the EMAs via OBV; `volume` enters only the OBV scaling term). No `open` (except as nothing — fills are closes), no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (declared research frame per the derivation; the script takes no timeframe input and makes no multi-frame call, so it is single-frame by construction).
- Warmup: the EMA24 leg needs 24 completed `1d` closes before it is statistically settled (Pine `ema` is `na` before its SMA seed — structurally silent, disclosed); ATR3 needs 3; the cumulative OBV baseline is arbitrary but cancels exactly in the fast-minus-slow cross comparison (additive constants pass through both EMAs identically). The adopted warmup is the first 120 completed `1d` bars flat by record rule (predeclared researcher choice — 5× the slow length, covering seeding plus the early-baseline transient with margin). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (declared port; the source venue `Futures_Binance BTC_USDT` names no separate spot/perp/margin layout — no cross-venue equivalence claimed beyond the same manufacturer venue family).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution for entries and reversals, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar-open on a `1h`/`15m` FMZ backtest (no execution-timing override ships anywhere); this record does not claim source fills. No maker-touch, queue, or intrabar-path-dependent entry fill: with one decision price per bar and mutually exclusive raw events, there is no same-bar entry ordering ambiguity.
- Stop execution (predeclared derivation): the 3% stop is a stop-market leg evaluated against post-entry bars' `high`/`low` ranges and filled at the pinned stop price, expressible on the pinned backtester's stop-execution path with the source's post-entry arming gate preserved; representative event-level Qlib/HB parity is still required before screening (see Implementation status). An entry-bar touch of the stop level exits nothing (arming gate, coded).
- Sizing/capital/costs: the block's `initial_capital=10000`, 100%-equity sizing and 0.0 commission ship no portable economics — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) replace them here, never presented as source-native behavior.
- Concurrency: at most one position (long or short) at any time; the opposite raw event reverses in full in one step; re-entry after a stop needs only the next raw cross (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The short leg requires margin-short permission, realistic on the pinned perpetual venue.

## Evidence

### Source-reported

The mirror ships the full construction (ATR3 scaling line, 6/24 anonymous EMA inputs, strict raw cross pair, alternation-filtered SL bookkeeping, two entry IDs, two stop-only exits, the six dead date inputs, the unwired 5000% TP input, the unread ATR-Mult input, the always-true test period, and the 100%-equity/zero-commission header), the author/title stamps, and the page-embedded January-2024 `1h`/`15m` Binance backtest header. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer beyond the stop: 0 `limit=` legs, 0 `strategy.close`, unwired TP/high-low/date/ATR-mult legs — the sole position-closing paths are the 3% stop and the opposite-raw-cross reversal. A trend that reverses slowly without ever printing a raw cross or touching the stop is ridden all the way back; this is the coded posture, disclosed, not a tunable parameter here.
2. Entry-bar stop blindness, admitted plainly: the `since_*Entry > 0` arming gate means a bar that both opens the position at its close and (in source intrabar terms)pierces the stop level intrabar exits nothing under this record's completed-bar rule — the first guardable bar is the next one. A gap-style adverse move on the entry bar itself is held unprotected by code.
3. Lag stack, admitted plainly: ATR3 smoothing inside the cum plus the EMA24 structural leg means violent 1d moves largely complete before the cross prints, while choppy markets print alternating raw crosses that flip the full unit (with stop churn between). Shortening any length would be a different, unpinned rule — none is admitted here.
4. ATR-zero/flat edge, admitted plainly: `atr3 = 0` (three consecutive zero-range bars) makes the scaling term divide by zero → `na` propagates and both EMAs go `na` → strict cross booleans are false → no fire. Equal closes add exactly 0. Both are structural, disclosed, and unencounterable on `1d` BTCUSDT outside a venue outage.
5. Dead-code boundary fenced: enabling the 5000% TP input (or any retuned TP), the ATR-Mult input, the high/low tracking, the date window, or any trailing/time leg would each be a different, unpinned rule — none is admitted here. The mirror arguments-table cell showing `v_input_8 = true` for ATR Mult contradicts the code's `defval=1`; the code governs, and the input is dead either way.
6. Scale-port boundary fenced: the source's 6/24 lengths and 3% stop were set in a `1h`-decision context; on `1d` bars the same arithmetic describes a slower phenomenon (multi-week flow persistence with wider holding character) with different trade frequency. The port is disclosed, not hidden, and this record makes no claim about the source timing's behavior or performance.
7. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT-`1d` research frame, same-bar-close fills, the adopted 120-bar warmup with record-rule pre-warmup flat, house sizing/costs, and the close-fill stop-price basis — all predeclared above; ATR period, OBV formula, EMA lengths, strict cross edges, both entry IDs, both stop legs with the 3% literal, the post-entry arming gate, full-unit reversal, two-sided direction, the post-stop flat state, and every dead-code exclusion are source-verbatim. This record is therefore never evidence that the original `1h` FMZ deployment passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: ATR-scaled OBV formula / EMA 6-24 / strict cross edges / full-unit reversal / 3% post-armed stop / no-TP-no-trailing-no-time / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Scaling relevance: replacing the ATR-scaled OBV with plain Granville OBV (unscaled cumulative signed volume, same 6/24 cross + 3% stop) must not improve net expectancy; fail ⇒ the volume-squared-over-ATR normalization adds nothing over textbook OBV.
- F2 — Stop relevance: removing the 3% stop legs (signal-only version where the sole position-changing path is the opposite-cross reversal) must not improve net expectancy; fail ⇒ the hard stop adds nothing over riding every cross to the next cross.
- F3 — Cross-timing relevance: replacing cross-event entries with always-in-side state holding (position = side of `e_fast` vs `e_slow` from warmup end, re-entering immediately post-stop while the side persists) must not improve net expectancy; fail ⇒ waiting for cross events adds nothing over holding the slow-leg side.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (declared port of an FMZ Binance-futures source context). The OHLCV arithmetic ports across perpetual venues without structural change; both sides are explicit legs, so a spot-only deployment expresses the long half unchanged while the short half stays venue-gated (short permission unused, never silently converted). Volume is standard per-bar kline volume, point-in-time with no leakage. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read, so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing and frame: the source fills next-bar-open on a `1h`-decision/`15m`-base Binance backtest; this record executes same-bar-close on `1d` BTCUSDT. Backtest economics of the two timings, frames, and venues differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source configuration's performance.
- Stop-model boundary: the source stop is an intrabar stop-market order; this record pins the same stop price, trigger side, and arming gate with range-evaluated stop-price fills. Same-bar entry-plus-stop ordering cannot arise (arming gate), and opposite-cross-vs-stop same-bar priority is resolved by the completed-bar rule (cross evaluated at the close; stop evaluated on post-entry bars only) — pinned, not assumed.
- No source cost declaration beyond a 0.0-commission placeholder: no fee, slippage, or funding assumption ships anywhere usable — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- OBV seed arbitrariness: the cumulative total starts from an arbitrary baseline, but additive constants cancel exactly in the fast-minus-slow cross comparison, so the seed affects nothing after warmup — disclosed, not smoothed.
- Scale selectivity: 6/24 OBV crosses on `1d` bars fire infrequently, so the system spends long stretches positioned through chop or flat after stops — long idle/adverse stretches are the coded trade, disclosed, not smoothed.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- FMZ canonical strategy page (ChaoZhang, Created 2024-02-20 15:35:08): https://www.fmz.com/strategy/442252
- Immutable mirror file at pinned commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (blob `310d14192735d558ef7de9d7385411a4d9f29619`, 10166 bytes): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E5%9F%BA%E4%BA%8EOBV%E6%8C%87%E6%A0%87%E7%9A%84%E8%B6%8B%E5%8A%BF%E8%B7%9F%E8%B8%AA%E7%AD%96%E7%95%A5OBV-EMA-Crossover-Trend-Following-Strategy.md
