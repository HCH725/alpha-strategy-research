---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Chande-momentum 80-cross reversal two-sided on BTCUSDT 1d bars
created: 2026-10-10
updated: 2026-10-10
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-09-02
sources:
  - https://github.com/hasnocool/tradingview-pine-scripts/blob/e031cab2819a7d56fb8bb9d000252f51439986e2/Chande%20Momentum%20Strat%20(Crossover).pine
  - https://www.tradingview.com/script/s1uuFSdY-Chande-Momentum-Strat-Crossover/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Chande-momentum 80-cross reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (pinned immutable GitHub file, live raw fetch 2026-10-10 at pin):

- Canonical file: https://github.com/hasnocool/tradingview-pine-scripts/blob/e031cab2819a7d56fb8bb9d000252f51439986e2/Chande%20Momentum%20Strat%20(Crossover).pine (repo `hasnocool/tradingview-pine-scripts`, file commit `e031cab2819a7d56fb8bb9d000252f51439986e2` dated 2023-09-02 — the sole commit touching this path; record `source_as_of` is that commit date, never the fetch date. Script author `burgercrisis`; TradingView canonical page `Chande Momentum Strat (Crossover)`, open-source strategy: https://www.tradingview.com/script/s1uuFSdY-Chande-Momentum-Strat-Crossover/).
- Full Pine v4 block read verbatim (2593 chars, `//@version=4`, `strategy(title="Chande Momentum Strat", shorttitle="ChandeMO Strat", format=format.price, precision=2)` — a real executable `strategy(`, not an indicator): 1 `strategy(` / 0 `study(` / 2 `strategy.entry` (`"Long"` long, `"Short"` short, each carrying an `alert_message` webhook-routing string) / 0 active `strategy.exit` (2 commented-out 20%-stop lines are dead code — pinned as absent, never adopted) / 0 `strategy.close` / 0 `strategy.order` / 0 `strategy.close_all`. 10 `input(` declarations: six backtest-window integers (start 2021-01-10, stop year 999999-09-26), `length = 9`, `src = close`, `buyline = -80`, `sellline = +80`. 1 `crossover(` (long leg, oscillator up through `-80`), 1 `crossunder(` (short leg, oscillator down through `+80`), 1 `change(`, 2 `sum(`, 2 `timestamp(`, 1 bare `time` series read (window gate only — pinned dead, see below), 0 `request.*`, 0 `security(`, 0 `process_orders_on_close` (language default governs, recorded as source-declared-by-default), 0 `pyramiding` (default `0` governs, recorded likewise), 0 `calc_on_every_tick` (default `false` governs).
- State rule read verbatim: `momm = change(src)`; `m1 = m >= 0 ? m : 0` (up-move part); `m2 = m >= 0 ? 0 : -m` (down-move magnitude); `sm1 = sum(m1, 9)`; `sm2 = sum(m2, 9)`; `chandeMO = 100 * (sm1 - sm2) / (sm1 + sm2)`. Long leg inside `if testPeriod()`: `crossover(chandeMO, buyline)` → `strategy.entry("Long", strategy.long)`; short leg: `crossunder(chandeMO, sellline)` → `strategy.entry("Short", strategy.short)`. No other order path exists.
- Source-reported venue (mirror header, corroboration only — never a gate fact): "Different signal then the other Chande Momentum strategy. In my opinion they both work better at different time frames and possibly commodities." A third-party mirror (`quanttradingpro`) renders this script's Strategy Tester snapshot on COINBASE:BTCUSD 1-minute; that snapshot is not source-reported performance and is fenced as lineage-only. The TradingView page itself was not opened this run (extraction backend unavailable); the pinned GitHub block above carries every gate fact, and the TV URL is fenced as lineage-only.

Licence and rights: the pinned file carries the author's MPL-2.0 header (`© burgercrisis`). This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence. The two `alert_message` routing strings (`a=ABCD b=buy/sell e=binanceus …`) are third-party webhook placeholders, not credentials; they are dropped as non-portable chrome and never reproduced beyond this disclosure.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly six: (1) same-bar-close fills on the traded market's own `1d` bars (the source sets no `process_orders_on_close`, so TradingView fills entries next-bar-open by default; this record pins completed-bar decision with same-bar-close execution for 1:1 pinned-backtester compatibility, predeclared); (2) the test window pinned constant-true — the six window inputs plus both `timestamp(` values compute a 2021-01-10→999999-09-26 gate that is already effectively every-bar in-source, and the BTCUSDT-`1d` research deployment evaluates every post-warmup bar (predeclared; the dead inputs are pinned as dead, not repurposed); (3) the commented-out 20% stops stay out (dead code — `//` prefixed, never compiled; the derived spec carries no stop of any kind, predeclared — see Signal); (4) research market BTCUSDT Binance perpetual `1d` (the pinned rule names no market in-code; no source-market equivalence is claimed); (5) an adopted 30-bar warmup with pre-warmup bars flat by record rule (covers `sum(…, 9)` over `change(src)` seeding plus margin — see Required data); (6) house sizing/capital/costs replacing the wholly absent source economics (see Execution assumptions). The `length = 9` / `src = close` / `±80` levels / up-down-sum-ratio formula / cross pair / both-sides stance / default-`0` pyramiding are source-verbatim.

Pre-write dedup (2026-10-10): working-tree case-insensitive searches for `chande-momentum`, `chandemo`, and `burgercrisis` return zero strategy records using this source, author script, or oscillator-cross mechanism (the only `chande` hits anywhere in the pool are `Chandelier`-Exit mentions and the Qstick record's Tushar-Chande inventor note — different indicators, different rules). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #58 (reconstruction batch — all 17 file paths verified, no oscillator-cross record), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit stop-flip long), and #92 (SSL channel state reversal) — different mechanisms, indicators, and sources. Closed research PRs (#1–#97 reviewed by title) contain no Chande Momentum record; the sole CMO-adjacent pool member is `vidya-cmo-adaptive-slope-trend-btcusdt-1h-2026-10-05.md` (closed PR #9). Four-axis distinction against it: signal construction differs (raw normalized-momentum level-cross at fixed `±80` thresholds here versus the sign of a recursive VIDYA adaptive average whose smoothing speed is merely scaled by `|9-bar CMO|` on `ohlc4` there), trigger differs (oscillator cross events versus adaptive-average slope state), position/exits differ (two-sided full-unit reversal with no flat state after the first signal versus long-only slope-flip close with `pyramiding = 25`), and source identity differs (burgercrisis TV strategy `s1uuFSdY` versus FMZ prose strategy 430552). Closest pool threshold-cross records (`qstick-zero-cross`, `tsi-signal-cross`, `qqe-fast-slow-cross`) differ in oscillator arithmetic — no pool record computes `100·(Σup − Σdn)/(Σup + Σdn)` over 9-bar `change(close)` partitions.

## Economic mechanism

### Source-reported

Oversold-recovery / overbought-fade momentum rotation: the author's stated rule buys when the Chande line crosses up through the buy line and sells when it crosses down through the sell line, with the remark that the sibling variant suits different timeframes and commodities. No further economic rationale ships in-source.

### Research interpretation

Exhaustion-recovery timing on a bounded normalized-momentum gauge. Unlike zero-cross oscillators (Qstick, TSI — the cross itself marks direction change), the `±80` bands mean entries fire only on recovery-from-extreme (`−80` crossed upward = sellers' dominance breaking) and fade-from-extreme (`+80` crossed downward = buyers' dominance breaking); mid-zone crossings trade nothing. As derived to BTCUSDT daily rotation, the bet is that 9-bar up/down asymmetry mean-reverts after touching the author's extreme bands — the failure mode is the missing stop made plain: with the commented-out 20% stops confirmed dead and no stop coded anywhere, a trend-day that pins the oscillator beyond the band realizes the full adverse excursion until the opposite cross fires, so a one-way drift sequence is the record's principal risk, disclosed, not smoothed over.

## Signal

Exact rule as pinned (`length = 9`, `src = close`, `buyline = -80`, `sellline = +80` frozen — any other values are a different, unpinned rule):

- Declaration (derived): Pine v4 builtins (`change`, `sum`, `crossover`, `crossunder`, `strategy.entry`) with v4 semantics observed. Single-timeframe by construction (0 `request.*` / 0 `security(`). The `plot`/`hline` calls, `format`/`precision` display flags, both `alert_message` strings, and all six window inputs render, display, route, or compute dead values only and gate no order. Both legs live — single-side variants would be different, unpinned rules.
- State (pinned, source-verbatim): `momm = change(close)`; `m1` keeps non-negative changes, else `0`; `m2` keeps negated negative changes, else `0`; `sm1 = sum(m1, 9)`; `sm2 = sum(m2, 9)`; `chandeMO = 100·(sm1 − sm2)/(sm1 + sm2)`, range-clamped to `±100` by construction whenever the divisor is positive.
- Orders (source-coded, derivation only in fill timing, window, and dead-stop confirmation): a bar with `crossover(chandeMO, -80)` → enter long one unit; a bar with `crossunder(chandeMO, +80)` → enter short one unit. Opposite-signal entry while holding reverses in full in one step (Pine default `pyramiding = 0` reversal netting; the source declares no pyramiding — the default governs, recorded as source-declared-by-default). Same-direction re-entry while holding is a no-op under that default (no adds, never averaged).
- No entry/entry ambiguity exists anywhere in this record: `crossover` requires `chandeMO[1] ≤ −80` while `crossunder` requires `chandeMO[1] ≥ +80` — both cannot hold on one bar, so conflict priority is provably irrelevant. Exact-equality bars (`chandeMO == ±80` with no strict cross) fire neither leg — ties defined by the cross operators, disclosed. Non-signal bars are explicit no-ops; pre-first-signal bars are flat (no standing position exists until the first cross).
- Risk posture (pinned): no stop-loss, no take-profit, no trailing, no time exit, no cooldown (the only stop-like text in-source is two `//`-commented `strategy.exit` lines with `0.8×/1.2×` average-price stops — dead code that never compiles; each risk leg is explicitly none, not invented).
- Direction: two-sided long/short with symmetric band-cross logic and full-unit reversal. Futures venue required for the short leg (researcher market choice — pinned).

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (all order-gating arithmetic derives from `change(close)` partitions; `high`/`low`/`open`/`volume` are read by no order-gating line). No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request.*` / 0 `security(` anywhere; the lone `time` read feeds only the pinned-dead window gate).
- Single decision timeframe `1d` (researcher choice — the pinned rule names no timeframe). One evaluation per completed bar; all signal reads reference confirmed bars only (`change`/`sum`/`crossover`/`crossunder` lags, confirmed-bar relations); no intrabar path is read.
- Warmup: `change(close)` is `na` on the first bar and each `sum(…, 9)` needs nine defined partitions, so the oscillator is first defined on the 10th completed bar. The adopted warmup is the first 30 completed `1d` bars flat by record rule (~3× the fixed lookback 9 plus margin — predeclared researcher choice); no signal before bar 31 may trade. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the pinned rule names no market in-code, and no source-market equivalence is claimed).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution for entries and reversals, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source sets no `process_orders_on_close` (TradingView default fills entries next-bar-open); this record does not claim any source fill convention. Reversal bars resolve atomically: the opposite cross closes the old unit and opens the new one in the same step — the pinned net effect of Pine reversal netting under default `pyramiding = 0`, disclosed.
- Stop/limit modeling: none — the derived spec carries zero stop/limit/trailing/time orders by record rule (the only such text in-source is commented-out dead code — see Negative evidence). No hidden Hummingbot stop-order defaults are relied upon.
- Sizing/capital/costs: the source ships no sizing, capital, fee, slippage, margin, or funding concept of any kind (no `default_qty_*`, no `initial_capital`, no `commission_*`, no `slippage` anywhere). The explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all) apply to the derived evaluation here, with the single-unit/no-add position pin from Signal, never presented as source-native behavior.
- Concurrency: at most one position (long or short) at any time after the first signal; the opposite cross reverses in full in one step; re-entry after a reversal needs only the next qualifying cross (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The short leg requires margin-short permission, realistic on the pinned perpetual venue.

## Evidence

### Source-reported

The pinned file ships the full construction (Pine v4 `strategy(` declaration, ten inputs at pinned defaults, the up/down-partition CMO formula, the `±80` band pair, the cross-gated long/short entry pair, the constant-true window gate, plus the author's crossover-tenet description and MPL-2.0 header). The mirror description's third-party Strategy Tester snapshot (COINBASE:BTCUSD 1-minute) is venue chrome, never performance evidence. The file ships zero performance numbers of its own: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Dead stops, admitted plainly: the only stop-like text in-source is two `//`-commented `strategy.exit` lines (`0.8×` / `1.2×` of average price, labelled 20% stops). Commented Pine never compiles and never orders; adopting them would be researcher fiction at researcher-chosen levels. This record therefore carries no stop-loss, take-profit, trailing, time exit, or cooldown of any kind — a predeclared posture, disclosed, not source exits.
2. Fill-timing derivation, admitted plainly: with no `process_orders_on_close` in-source, TradingView fills entries next-bar-open by default — this record's same-bar-close fills are a researcher adaptation for pinned-backtester compatibility, disclosed, not source timing.
3. Window derivation, admitted plainly: the source gates entries on the 2021-01-10→999999-09-26 window; the six window inputs plus both `timestamp(` values are pinned as dead in the derived spec and evaluation is every post-warmup bar — disclosed, not repaired and not adopted as a window.
4. Missing stop, admitted bluntly: no risk leg of any kind exists anywhere in the derived spec — each explicitly none. A cross that immediately fails into a one-way drift realizes the full adverse excursion until the opposite band-cross fires; gap-through sequences have no bound in this record. This is the coded posture minus nothing (the dead stops were never alive), disclosed as the record's principal risk.
5. Zero-divisor edge, disclosed: nine consecutive zero-change bars make `sm1 + sm2 = 0`, so `100·0/0` is `na` and both cross guards are falsy — a perfectly flat 10-bar stretch fires nothing by construction, pinned, not smoothed over.
6. Routing-string drop, disclosed: both entries' `alert_message` values are third-party webhook placeholders (`a=ABCD … e=binanceus …`), not economics; they are dropped as non-portable chrome and quoted nowhere beyond this disclosure.
7. Source basis fenced: the pinned rule names no market or timeframe. The BTCUSDT-`1d` choice, same-bar-close fills, atomic-reversal ordering, every-bar evaluation, 30-bar warmup, single-unit/no-add pin, and house sizing/costs are researcher choices, disclosed; this record is therefore never evidence that any source-market deployment passes.
8. Derivation boundary fenced: the only non-source-native behaviors in this record are same-bar-close fills, atomic-reversal ordering, every-bar evaluation with dead window inputs, the adopted 30-bar warmup with record-rule pre-warmup flat, the dropped routing strings, the BTCUSDT-`1d` market choice, and house sizing/costs — all predeclared above; the `change(close)` partition / `sum(…, 9)` pair / `100·(Σup−Σdn)/(Σup+Σdn)` formula / `±80` bands / cross pair / both-sides stance / default-`0` pyramiding / no-risk-leg posture are source-verbatim. This record is therefore never evidence that the original script itself passes.
9. The `9` / `close` / `-80` / `+80` literals, the band-cross (not zero-cross, not region-hold) trigger, the full-unit reversal, and the two-sided stance are pinned, not removed: retuning any literal, widening crosses to region-holds, adding any TP/SL/trailing/cooldown leg, dropping the short leg, or sizing partially instead of full-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `CMO(9, close)` / `±80` bands / cross pair / full-unit reversal / two-sided / `1d` BTCUSDT / same-bar-close fills / atomic-reversal ordering are frozen.

- F1 — Band relevance: replacing the `±80` band crosses with plain zero-line `crossover/crossunder(chandeMO, 0)` entries through the same reversal exits must not improve net expectancy; fail ⇒ the extreme bands add nothing over the direction cross.
- F2 — Oscillator relevance: replacing the CMO cross triggers with 9-bar raw-momentum-sign entries (`change(close, 9) ≷ 0`) through the same reversal exits must not improve net expectancy; fail ⇒ the normalized up/down partition adds nothing over raw momentum sign.
- F3 — Reversal relevance: replacing opposite-cross reversal exits with fixed-horizon closes (exit N bars after entry, same entries) must not improve net expectancy; fail ⇒ the symmetric reversal adds nothing over time-based risk control.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision frame researcher-chosen `1d`; arithmetic over `close` only with no venue-specific read). The construction ports across perpetual venues with full OHLCV feeds without structural change. The short leg requires margin-short permission (realistic on perpetual venues; a spot-only deployment cannot express the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (the lone `time` read feeds only the pinned-dead window gate), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Dead stops stay dead: the commented-out 20% stops are never compiled in-source and no replacement level is invented here; backtest economics of any re-added stop level would differ by construction — the absence is disclosed, not hidden.
- No risk leg anywhere: loss is bounded only by the opposite band-cross reversal; the record carries no stop-loss/trailing/time-exit/cooldown by design — disclosed as the principal risk, not a gap to be quietly repaired later.
- Derived fill timing: same-bar-close execution is a researcher choice over logic that defaults (in TradingView) to next-bar-open; backtest economics of other timings differ by construction — the adaptation is disclosed, not hidden.
- Derived window: every-bar evaluation replaces the source's effectively-always-true window; the dead inputs are pinned, not repurposed — disclosed, not hidden.
- Researcher market/frame: the pinned rule names no market or timeframe — BTCUSDT `1d` is a researcher choice; signal timing on other markets or frames would differ by construction.
- Position-state pin: same-side-add behavior executes nowhere in-source beyond the default; the single-unit/no-add pin under Pine-default `pyramiding = 0` reversal netting is recorded as source-declared-by-default plus researcher pin, disclosed.
- No source cost declaration: no capital, commission, fee, slippage, margin, or funding assumption ships anywhere — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Warmup cost: the first 30 bars are flat by record rule, so any textbook cross inside warmup is deliberately untraded — pinned, not recovered.
- Flat-stretch silence: a perfectly flat 10-bar window yields `na` and fires nothing — pinned, not recovered.
- Lineage limit: the TradingView page was not opened this run (extraction unavailable); lineage rests on the pinned file's own author/version stamps and the stable TV URL — every gate fact is from the pinned block itself.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Chande Momentum Strat (Crossover) [burgercrisis] pinned GitHub mirror at commit `e031cab2819a7d56fb8bb9d000252f51439986e2` (sole commit touching this path, 2023-09-02): https://github.com/hasnocool/tradingview-pine-scripts/blob/e031cab2819a7d56fb8bb9d000252f51439986e2/Chande%20Momentum%20Strat%20(Crossover).pine
- Chande Momentum Strat (Crossover) [burgercrisis] canonical TradingView page, lineage-only (page not opened this run): https://www.tradingview.com/script/s1uuFSdY-Chande-Momentum-Strat-Crossover/
