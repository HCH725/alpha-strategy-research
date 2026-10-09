---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: CMF velocity zero-cross with EMA200 gate and ATR bracket two-sided on BTCUSDT 1d bars
created: 2026-10-10
updated: 2026-10-10
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-09-11
sources:
  - https://github.com/fmzquant/strategies/blob/87a415edf7b08065fbcbfbfefb7351cd929e4dbd/CMF-Momentum-Breakthrough-Moving-Average-Strategy.md
  - https://www.tradingview.com/script/zsTl96Gd-CMF-Velocity/
  - https://www.fmz.com/strategy/426394
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# CMF velocity zero-cross with EMA200 gate and ATR bracket two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (pinned immutable GitHub file, live raw fetch 2026-10-10):

- Canonical file: https://github.com/fmzquant/strategies/blob/87a415edf7b08065fbcbfbfefb7351cd929e4dbd/CMF-Momentum-Breakthrough-Moving-Average-Strategy.md (repo `fmzquant/strategies`, file commit `87a415edf7b08065fbcbfbfefb7351cd929e4dbd` dated 2024-03-03 — latest commit touching this path; record `source_as_of` 2023-09-11 is the file's own `Last Modified` stamp, never the fetch date. Author `ChaoZhang`; header names the strategy author `TheSadRhinoInvesting, v1.0, 2021.05.16, INITIAL RELEASE`; `Detail` link https://www.fmz.com/strategy/426394).
- Full Pine v4 block read verbatim (`//@version=4`, `strategy("CMF Velocity with 200EMA Strategy")` — a real executable `strategy(`, not an indicator): 1 `strategy(` / 0 `study(` / 2 `strategy.entry` / 2 `strategy.exit` / 0 `strategy.close` / 0 `strategy.order`. 15 `input(` declarations: 8 backtest-window fields (start/end year/month/day/hour), `direction = input(0, ... minval=-1, maxval=1)` (pinned `0` → `strategy.direction.all`, both sides live), `pLRatioMultiplier = 2`, `emaPeriod = 200`, `atrMultiplier = 2`, `atrPeriod = 10`, `cmfPeriod = 11`, `cmfVelocityPeriod = 7`. 1 `crossover(` (long leg), 1 `crossunder(` (short leg), 1 `plot(` (EMA only), 2 `timestamp(` (both dead — see below), 0 `request.*`, 0 `security(`, 0 `time(`, 0 `process_orders_on_close` (language default governs, recorded as source-declared-by-default), 0 `pyramiding` (default `0` governs, recorded likewise), 0 `calc_on_every_tick` (default `false` governs).
- Dead window, admitted plainly: `testPeriodStart`/`testPeriodEnd` are each defined once and referenced zero times afterward; the only gate on entries is the constant `timeBacktesting = true` (3 live occurrences: definition + both entry legs). The eight date inputs therefore change no order on any bar — the coded evaluation window is every bar, disclosed, not repaired and not adopted as a window.
- State rule read verbatim: `moneyFlowMultiplier = (((close - low) - (high - close)) / (high - low)) * volume` with `na(...) ? 0 : ...` guard; `cmf = sma(MFM, 11) / sma(volume, 11)`; `cmfVelocity = sma(change(cmf), 7)`; `atrSeries = atr(10)` (RMA-based Wilder ATR); `triggerEMA = ema(close, 200)`. Long leg: `crossover(cmfVelocitySeries, 0.0) and triggerEMA < close and timeBacktesting` → `strategy.entry("Long Entry", true)` + `strategy.exit("Exit", "Long Entry", stop = close - 2*ATR, limit = close + 4*ATR)`. Short leg mirrors with `crossunder`, `triggerEMA > close`, `strategy.entry("Short Entry", false)`, `stop = close + 2*ATR`, `limit = close - 4*ATR` (stop distance `2×ATR(10)`, profit distance `2×` stop offset = `4×ATR`, fixed 2:1 — pinned literals `2`, `2`, `200`, `10`, `11`, `7`).
- In-code lineage (source-reported, corroboration only — no line-level fact in this record comes from it): header cites `CMF Velocity: https://www.tradingview.com/script/zsTl96Gd-CMF-Velocity/` and states the strategy "works best in a strongly trending market". A live browser re-read of the TradingView page was not available in this run (extraction backend unavailable) and the FMZ detail page is login-gated for code; both are fenced as unopened, and every gate fact here comes from the pinned GitHub block above.
- The porter's backtest header comment (`start: 2023-08-11, end: 2023-09-10, period: 45m, basePeriod: 5m, Futures_Binance BTC_USDT`) and PNG are porter config/chrome, never adopted as strategy facts and never performance evidence.

Licence and rights: the pinned file is a public port of a public author's version-stamped strategy release. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly six: (1) same-bar-close fills on the traded market's own `1d` bars (the source sets no `process_orders_on_close`, so TradingView fills entries next-bar-open by default; this record pins completed-bar decision with same-bar-close execution for 1:1 pinned-backtester compatibility, predeclared); (2) bracket-touch evaluation on completed bars with pinned precedence — stop before limit on a both-touch bar (conservative), exits before entries within one bar (so a stop-touch bar that also prints the opposite cross exits-then-re-enters in one step, matching Pine reversal netting), predeclared (the source declares no intrabar/same-bar precedence anywhere); (3) an adopted 250-bar warmup with pre-warmup bars flat by record rule (covers EMA-200 seeding plus CMF-11/velocity-7/ATR-10 stabilization plus margin — see Required data); (4) research market BTCUSDT Binance perpetual `1d` (the porter's `BTC_USDT`/`45m`/`5m` header is not adopted); (5) the shared `"Exit"` id and Pine-default reversal-cancels-prior-bracket netting pinned as the record's position effect (see Signal); (6) house sizing/capital/costs replacing the wholly absent source economics (see Execution assumptions). The `cmf(11)` / `sma(change,7)` velocity / `0.0` cross pair / `ema(close,200)` strict gate / `2×ATR(10)` stop / `2:1` limit / `direction = 0` both-sides / dead-window-every-bar / `na→0` MFM guard are source-verbatim.

Pre-write dedup (2026-10-10): working-tree case-insensitive searches for `cmf`, `chaikin`, `zstl96`, `sadrhino`, `426394`, and `cmf velocity` return zero strategy records using this source, author script, indicator, or mechanism. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #58 (reconstruction batch — file list verified, no oscillator/money-flow record), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit stop-flip long), and #92 (SSL channel state reversal) — different mechanisms, indicators, and sources. Closed research PRs (#1–#95 reviewed by title) contain no CMF/Chaikin record. Closest pool money-flow records differ in mechanism class: `klinger-volume-oscillator-trigger-flip-two-sided-btcusdt-1d-2026-10-10.md` trades the fast/slow EMA spread of volume-signed force against a trigger line (no Chaikin normalization, no zero-cross, no regime gate, no bracket); `alphatrend-mfi-atr-trailing-reversal-btcusdt-4h-2026-10-08.md` gates an ATR ratchet on `mfi >= 50` and reverses on the trail's own lag-2 self-cross (no CMF, no velocity, no stop/limit order, different author and source). Four-axis distinction: signal construction differs (Chaikin money-flow ratio differenced over 7 bars crossed against the fixed `0.0` line — no pool record computes `sma(MFM,11)/sma(volume,11)` or its change-average), trigger differs (velocity zero-cross pair plus a strict `ema(close,200)` side gate, not a spread-vs-trigger or ratchet self-cross), exits differ (coded `strategy.exit` stop/limit bracket at fixed 2:1 plus opposite-cross reversal — the Klinger/AlphaTrend families ship no stop/limit order at all), and source identity differs (fmzquant `87a415e` port of TheSadRhinoInvesting's 2021 v1.0 release with `zsTl96Gd` indicator lineage).

## Economic mechanism

### Source-reported

Money-flow-velocity breakout with trend-regime gating and a fixed-asymmetry bracket: CMF Velocity is presented in-code as "the rate of change in money flow" — CMF itself accumulates each bar's volume signed by where the close sits inside the high–low range, normalized by total volume; velocity is the 7-bar average of its bar-to-bar change. A cross above `0` means money-flow momentum has turned positive (buy signal); a cross below `0` the mirror (sell signal). The `200` EMA permits only the regime side (longs above, shorts below). Risk is a fixed `2×ATR(10)` stop with profit at twice the risk (`2:1`). The author's own regime tenet is preserved in-code: "The strategy works best in a strongly trending market" — recorded as source-reported negative evidence that range chop is the named adverse regime.

### Research interpretation

Edge-triggered two-sided reversal system on money-flow momentum with a slow-regime veto and a fixed payoff-asymmetry bracket. Unlike price-only signal-line crosses (MACD, KST, TRIX, TSI) where both lines derive from `close` smoothing, here the primary line is a volume-normalized quantity: a high-volume bar whose close sits near its high injects the full signed volume into the CMF numerator, so climactic accumulation/distribution bars dominate the velocity — the bet, as derived, is on BTCUSDT daily money-flow persistence inside the EMA-200 regime, never on a price level, breakout, squeeze, calendar, or mean-reversion anchor. Unlike the Klinger family (volume-signed force spread versus its own trigger, always-in-market, no bracket) the trigger here is relational against the fixed `0.0` line with a 200-bar regime veto and every position carries a coded 2:1 bracket — chop that alternately crosses still flips the unit, but each flip risks exactly `2×ATR` for `4×ATR`, so the failure mode is bracket-stop attrition in trendless velocity chop (the author's own "trending market" warning), not unbounded adverse excursion: the bracket, not the opposite cross, is the primary loss bound.

## Signal

Exact rule as pinned (`cmfPeriod = 11`, `cmfVelocityPeriod = 7`, `emaPeriod = 200`, `atrPeriod = 10`, `atrMultiplier = 2`, `pLRatioMultiplier = 2`, `direction = 0`, `timeBacktesting = true` frozen — any other values are a different, unpinned rule):

- Declaration (derived): Pine v4 builtins (`sma`, `ema`, `atr`, `change`, `crossover`, `crossunder`, `na`, `timestamp`, `strategy.entry`, `strategy.exit`, `strategy.risk.allow_entry_in`) with v4 `na` semantics observed. Single-timeframe by construction (0 `request.*` / 0 `security(`). The `plot(triggerEMA)`, both `timestamp(` values, and all eight date inputs render or compute dead values only and gate no order. `direction = 0` pins `strategy.direction.all` — both legs live; `±1` would be a different, unpinned rule.
- State (pinned, source-verbatim): `MFM = ((close - low) - (high - close)) / (high - low) * volume`, `na → 0` on the bar; `cmf = sma(MFM, 11) / sma(volume, 11)`; `velocity = sma(change(cmf), 7)`; `ATR = atr(10)`; `E200 = ema(close, 200)`.
- Orders (source-coded, derivation only in fill timing and precedence): a bar with `crossover(velocity, 0.0)` and `close > E200` → enter long with bracket `stop = fill - 2*ATR`, `limit = fill + 4*ATR`; a bar with `crossunder(velocity, 0.0)` and `close < E200` → enter short with bracket `stop = fill + 2*ATR`, `limit = fill - 4*ATR`. `crossover`/`crossunder` cannot co-fire on one bar and the `close ≷ E200` gates are mutually exclusive — no same-bar entry/entry ambiguity exists anywhere in this record. Exact equality (`close == E200`, `velocity == 0.0` relationship without a strict cross) fires neither leg — ties defined by the strict operators, not ambiguous. Non-signal bars are explicit no-ops.
- Bracket evaluation (derived precedence, predeclared): levels are fixed at the entry bar's close and evaluated on subsequent completed bars only (the entry bar cannot self-exit). A post-entry bar touches the long stop if `low <= stop`, the long limit if `high >= limit` (mirror for shorts). Same-bar both-touch resolves stop-first (conservative). Within one bar, exits resolve before entries: a bar that stops out and simultaneously prints the opposite cross closes the old unit and opens the new one in the same step — the pinned net effect of Pine's reversal-cancels-prior-bracket semantics under default `pyramiding = 0` (source declares no pyramiding; the default governs, recorded as source-declared-by-default). The shared `"Exit"` id is benign under mutually exclusive legs — only one side's entry+bracket exists at a time, pinned.
- Risk posture (pinned): no trailing, no time exit, no cooldown (none coded — explicitly none, not invented). The sole position-changing paths are bracket touch and opposite-cross reversal.
- Direction: two-sided long/short with symmetric bracket and reversal. Futures venue required for the short leg (researcher market choice — pinned).

## Required data

- Completed `1d` bars of BTCUSDT: `high`, `low`, `close`, `volume` (all four read by order-gating lines: MFM uses high/low/close/volume; ATR uses high/low/close; EMA gate uses close). No `open`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request.*` / 0 `security(` anywhere; the porter's `basePeriod: 5m` header carries no cross-timeframe indicator read in the verbatim logic and is not adopted).
- Single decision timeframe `1d` (researcher choice — the pinned rule names no timeframe; the porter's `45m` header is not adopted). One evaluation per completed bar; all signal reads reference confirmed bars only (`change`/`[1]` lags, confirmed-bar `crossover`/`crossunder` relations); bracket touches reference completed-bar `high`/`low` extremes with no intrabar path.
- Warmup: `ema(close, 200)` seeding dominates (CMF needs ~11 + 7 velocity bars, ATR RMA ~10+ bars — all minor beside it); Pine `sma`/`atr`/`ema` print `na` until seeded, and `crossover(na, 0)` is falsy, so no signal can fire pre-seeding by construction. The adopted warmup is the first 250 completed `1d` bars flat by record rule (200 EMA seeding + ~18 velocity-chain stabilization + ATR settling + margin — predeclared researcher choice); no signal before bar 251 may trade. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice informed by the porter's displayed `BTC_USDT` backtest header — the pinned rule itself names no market; naming normalization is the only market step, and no source-market equivalence is claimed).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution for entries, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source sets no `process_orders_on_close` (TradingView default fills entries next-bar-open); this record does not claim any source fill convention. Bracket levels derive from the entry-bar close (`fill ± offsets`); bracket touches evaluate on subsequent completed bars' extremes as specified in Signal — no maker-touch, queue, or intrabar-path-dependent fill exists anywhere in this rule.
- Stop/limit modeling: the `2×ATR(10)` stop / `4×ATR` limit bracket is source-coded (`strategy.exit` with `stop=`/`limit=`), evaluated here under the completed-bar touch semantics above with stop-first same-bar precedence. No hidden Hummingbot stop-order defaults are relied upon; the precedence and exits-before-entries ordering are record rules, disclosed.
- Sizing/capital/costs: the source ships no sizing, capital, fee, slippage, margin, or funding concept of any kind. The explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all) apply to the derived evaluation here, with the single-unit/no-add position pin from Signal, never presented as source-native behavior.
- Concurrency: at most one position (long or short) at any time; a bracket touch closes in full; the opposite cross reverses in full in one step; re-entry after a close needs only the next qualifying cross (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The short leg requires margin-short permission, realistic on the pinned perpetual venue.

## Evidence

### Source-reported

The pinned file ships the full construction (Pine v4 `strategy(` declaration, fifteen inputs at pinned defaults, the `na`-guarded MFM expression, the `sma(11)/sma(volume,11)` CMF ratio, the `sma(change,7)` velocity, `atr(10)`, `ema(close,200)`, the constant-`true` backtest gate with dead date inputs, `direction = 0` both-sides, the zero-cross entry pair with strict EMA gates, and the `2×ATR` stop / `2:1` limit `strategy.exit` bracket pair, plus the author's trending-market tenet and version stamp). The porter's backtest header comment and PNG are config/chrome, never performance evidence. The page ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Fill-timing derivation, admitted plainly: with no `process_orders_on_close` in-source, TradingView fills entries next-bar-open by default — this record's same-bar-close fills are a researcher adaptation for pinned-backtester compatibility, disclosed, not source timing.
2. Precedence derivation, admitted plainly: the source declares no same-bar stop-vs-limit or exit-vs-entry precedence — stop-first and exits-before-entries are researcher record rules (conservative, deterministic), disclosed, not source semantics.
3. Dead date inputs, fenced: eight backtest-window inputs compute values nothing reads (`timeBacktesting = true` constant) — the every-bar evaluation is coded behavior, and the dead inputs are pinned as dead, not removed or repurposed.
4. `na` edges, disclosed: `high == low` bars zero the MFM via the `na → 0` guard (a limit-up/limit-down bar contributes nothing to CMF — pinned, not smoothed over); a zero `sma(volume, 11)` prints `cmf = na` → `velocity = na` → no cross (fail-safe toward no-trade, disclosed); pre-seeding `na` bars cannot signal by construction, and the 250-bar record-rule flat covers seeding plus stabilization.
5. Always-positioned-after-arming risk, admitted plainly: until a bracket fires, the system holds the full unit through adverse excursion bounded only by the `2×ATR` stop — alternating velocity crosses in trendless chop flip the unit repeatedly, each flip risking the full stop with no confirmation beyond the coded pair, no cooldown, and no cost guard; this is the coded trade, disclosed — and the exact failure the author's trending-market tenet names.
6. Source basis fenced: the pinned rule names no market or timeframe (the porter's `BTC_USDT` / `45m` / `5m` header is porter config). The BTCUSDT-`1d` choice, same-bar-close fills, precedence rules, 250-bar warmup, single-unit/no-add pin, and house sizing/costs are researcher choices, disclosed; this record is therefore never evidence that any source-market deployment passes.
7. Derivation boundary fenced: the only non-source-native behaviors in this record are same-bar-close fills, completed-bar bracket-touch evaluation with stop-first/exits-first precedence, the adopted 250-bar warmup with record-rule pre-warmup flat, the BTCUSDT-`1d` market choice, and house sizing/costs — all predeclared above; the CMF-11 ratio / velocity-7 / `0.0` cross pair / strict EMA-200 gates / `2×ATR(10)` stop / `2:1` limit / `direction = 0` both-sides / dead-window / `na→0` guard / no-trailing/no-time-exit/no-cooldown posture are source-verbatim. This record is therefore never evidence that the original script itself passes.
8. The `11` / `7` / `200` / `10` / `2` / `2` literals, the plain velocity zero-cross pair (not raw-CMF cross, not threshold bands), the strict `close ≷ E200` gates (equality fires nothing), the fixed 2:1 bracket, the full-unit reversal, and the two-sided stance are pinned, not removed: retuning any literal, gating crosses on bands, adding a trailing/time/cooldown leg, dropping the short leg, setting `direction = ±1`, or sizing partially instead of full-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `cmf(11)` / `velocity(7)` / `0.0` cross pair / `ema(close,200)` strict gates / `2×ATR(10)` stop / `2:1` limit / full-unit reversal / two-sided / `1d` BTCUSDT / same-bar-close fills / stop-first precedence are frozen.

- F1 — Velocity relevance: replacing `sma(change(cmf), 7)` with raw `cmf(11)` through the same zero-cross pair, gates, and bracket must not improve net expectancy; fail ⇒ the velocity differencing adds nothing over the CMF level.
- F2 — Regime-gate relevance: removing the `close ≷ ema(close,200)` side veto (both cross legs live on every bar) through the same bracket must not improve net expectancy; fail ⇒ the 200-bar gate adds nothing over the ungated cross pair.
- F3 — Bracket relevance: replacing the fixed `2×ATR` stop / `2:1` limit bracket with pure opposite-cross exits (no stop/limit orders) must not improve net expectancy; fail ⇒ the coded bracket adds nothing over reversal-only risk control.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision frame researcher-chosen `1d`; arithmetic over high/low/close/volume with no venue-specific read). The construction ports across perpetual venues with full OHLCV feeds without structural change. The short leg requires margin-short permission (realistic on perpetual venues; a spot-only deployment cannot express the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere; the date inputs are dead by code), so session-gap behavior needs no approximation. Zero-volume-average bars (`cmf = na` → no signal) are vanishingly rare on BTCUSDT but the fail-safe is venue-independent. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: same-bar-close execution is a researcher choice over logic that defaults (in TradingView) to next-bar-open; backtest economics of other timings differ by construction — the adaptation is disclosed, not hidden.
- Derived precedence: stop-first same-bar resolution and exits-before-entries ordering are researcher record rules over logic that declares no precedence; economics under other precedence choices differ by construction — disclosed, not hidden.
- Researcher market/frame: the pinned rule names no market or timeframe — BTCUSDT `1d` is a researcher choice informed by the porter's backtest header; signal timing on other markets or frames would differ by construction.
- Position-state pin: same-side-add behavior executes nowhere in-source beyond the default; the single-unit/no-add pin under Pine-default `pyramiding = 0` reversal netting is recorded as source-declared-by-default plus researcher pin, disclosed.
- Stop-bounded but chop-exposed: each position's loss is bounded by the `2×ATR` stop, but alternating velocity crosses in trendless markets flip the full unit repeatedly with no confirmation beyond the coded pair and no cost guard; adverse excursion within the stop band is realized in full on every touch. This is the coded posture, disclosed as the record's principal risk.
- No source cost declaration: no capital, commission, fee, slippage, margin, or funding assumption ships anywhere — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Warmup cost: the first 250 bars are flat by record rule, so any textbook cross inside warmup is deliberately untraded — pinned, not recovered.
- Lineage limit: the `zsTl96Gd` indicator page and the FMZ detail page were not opened this run (extraction unavailable / login-gated); lineage rests on the pinned file's own version-stamped author header and in-code indicator citation — every gate fact is from the pinned block itself.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- CMF-Momentum-Breakthrough-Moving-Average-Strategy [ChaoZhang port of TheSadRhinoInvesting v1.0 2021-05-16] pinned GitHub file at commit `87a415edf7b08065fbcbfbfefb7351cd929e4dbd` (file `Last Modified` 2023-09-11; FMZ strategy 426394): https://github.com/fmzquant/strategies/blob/87a415edf7b08065fbcbfbfefb7351cd929e4dbd/CMF-Momentum-Breakthrough-Moving-Average-Strategy.md
- CMF Velocity [TheSadRhinoInvesting] canonical indicator page, in-code lineage citation (published indicator referenced by the pinned strategy header; page not opened this run): https://www.tradingview.com/script/zsTl96Gd-CMF-Velocity/
- FMZ strategy detail page `CMF Momentum Breakthrough Moving Average Strategy` [ChaoZhang] (porter config and backtest chrome only — full code login-gated, never cited for line-level facts): https://www.fmz.com/strategy/426394
