---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TSI signal-line cross reversal two-sided on BTCUSDT 1d bars
created: 2026-10-10
updated: 2026-10-10
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-10-07
sources:
  - https://www.fmz.com/strategy/428611
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TSI signal-line cross reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (canonical FMZ page, fetched 2026-10-10):

- Canonical page: https://www.fmz.com/strategy/428611 (page title `Bitcoin Short-Term Trading Strategy Based on True Strength Index`, Chinese title `基于真实强弱指标的比特币短线交易策略`, public `Common strategy`, `Created: 2023-10-07 15:12:08` — adopted as `source_as_of` 2023-10-07). Fetched over HTTPS during this cycle (774197 bytes): the page embeds the full Pine block byte-verbatim — `price = request.security(syminfo.tickerid,resCustom,close)` with `resCustom = input(title="Timeframe", defval="15")`, `double_smooth(src, long, short) =>` (`ta.ema(ta.ema(src, long), short)`), `pc = ta.change(price)`, `tsi_value = 100 * (double_smoothed_pc / double_smoothed_abs_pc)`, `tsi2 = ta.ema(tsi_value, signal)`, the live order pair `strategy.entry("BUY", strategy.long, 1, when = buy)` / `strategy.entry("SELL", strategy.short, 1, when = sell)` with `buy = ta.crossover(tsi_value, tsi2)` / `sell = ta.crossunder(tsi_value, tsi2)`, and the page-embedded `/*backtest*/` header (`start: 2022-09-30 00:00:00`, `end: 2023-10-06 00:00:00`, `period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`). Word-boundary counts over the whole landing HTML: `Sharpe` 0, `Net Profit` 0, `Win Rate` 0, `Max Drawdown` 0, `Profit Factor` 0, `Annual(ized)` 0 — the page ships no performance numbers of any kind (adopted as no claimed performance anywhere in this record).
- Text census over the embedded code block: 2 `strategy.entry` (the BUY-long / SELL-short pair quoted above, each with explicit `qty = 1`) / 0 `strategy.close` / 0 `strategy.exit` / 0 `strategy.order` / 1 `request.security` (the `15`-minute same-symbol feed this derived record ports away, predeclared below) / 1 `ta.crossover` / 1 `ta.crossunder` / 4 `input(` declarations (`Timeframe` "15", `Long Length` 25, `Short Length` 13, `Signal Length` 13 — the three lengths pinned at defaults; any other value is a different, unpinned rule) / 0 `time(` / 1 `volume`-free block (no `volume` read anywhere) / `open`/`high`/`low` read nowhere (the rule reads `close` only, via the security call). `pyramiding`, `process_orders_on_close`, `calc_on_every_tick`, `max_bars_back`, commission and slippage appear only inside the COMMENTED-OUT `strategy(...)` declaration line (`// strategy("True Strength Indicator BTCUSD 15p", ... pyramiding=10, ...)` — inactive text, pinned as unspecified-by-active-code, never treated as live configuration). The `ta.*` / `math.*` / `color.*` namespaces pin Pine v5-era semantics (no `//@version` line ships in the block). The `hline(30/50/70)` plots, `plot(tsi_value)` / `plot(tsi2)` / `plot(rsiserie)`, both `alertcondition` calls, and all `bgcolor(...)` legs render or notify only and gate no order.
- No immutable GitHub mirror of this strategy was found (GitHub code search over `fmzquant/strategies` returns no True-Strength record); provenance rests on the canonical FMZ page read verbatim this cycle, which is an eligible public source. No `©` author line and no licence header ships in the embedded block; the page publisher account is not exposed in the fetched state, so no author attribution is claimed beyond the canonical URL.
- Page/prose performance language is absent entirely (no table, figure, or number anywhere) — this record claims no source-reported performance and no reproduced performance.

Licence and rights: the canonical page is a public FMZ strategy publication. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly six: (1) single-timeframe collapse — the source computes every series on `request.security(syminfo.tickerid, "15", close)` (15-minute closes) while charting `period: 1d`; the derived record computes the identical formula on the traded market's own `1d` closes (the pinned engine has no verified 15m-signal/1d-decision multi-timeframe path, so the source-native MTF split cannot satisfy gate 5; lengths, operators, and order are verbatim); (2) code-over-prose entry pin — the page prose claims longs only when `RSI > 50` and shorts only when `RSI < 50`, but the executable entries are pure `ta.crossover` / `ta.crossunder` (every RSI/CCI/stoch fragment in the entry lines is commented out; `rsiserie = ta.rsi(price,7)`, `cciserie = ta.cci(price,14)`, `stochserie = ta.stoch(price,14,3,3)` feed plots and `bgcolor` only) — the derived spec follows the executable code and excludes RSI/CCI/stoch from all order logic, predeclared; (3) same-bar-close fills (the source sets no execution-timing argument anywhere, so source fills are next-tick/next-open by language default); (4) position-state pin — the only sizing/pyramiding text (`qty = 1` per entry leg; `pyramiding=10`) lives in entry arguments and the inactive commented header, so live same-side-add and reversal-quantity behavior is unspecified-by-active-code; the derived record pins single-unit per side, repeat-signal-while-positioned as no-op, full reversal on the opposite cross, predeclared; (5) an adopted 60-bar warmup with pre-warmup bars flat by record rule (covers `change(1)` + EMA 25 + EMA 13 + signal EMA 13 plus seeding margin — see Required data); (6) house sizing/capital/costs replacing the absent-apart-from-inactive-text source economics (see Execution assumptions). The double-smoothing arithmetic (25/13/13), the TSI/signal cross triggers, the BUY-long/SELL-short order pair, and the reversal-only no-stop posture are source-native and unmodified.

Pre-write dedup (2026-10-10): working-tree case-insensitive searches for `true.strength` and boundary-delimited `tsi` return zero hits anywhere — no admitted rule uses this source, author publication, indicator, or mechanism. Same-publisher-family FMZ records exist (Coppock 431926, KST, Aroon, TRIX, Schaff, MACD, Qstick, Chandelier-PR) but carry different canonical identities, different indicator families, and different order sets. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long — single file verified), #49 (Gaussian channel StochRSI-gated breakout long — single file verified), #58 (reconstruction batch — file list verified, no TSI/strength record), #63 (SuperTrend ATR-flip trend long — single file verified), and #89 (Chandelier Exit dual-stop state-flip long — single file verified) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `kst-signal-cross-trend-two-sided-btcusdt-1h-2026-10-09.md` crosses a summed ROC against its own signal line without double-smoothing or normalization; `fisher-zero-cross-reversal-btcusdt-1d-2026-10-09.md` crosses a normalized nonlinear transform against the zero level, not against its own signal average; `trix-dual-band-trend-btcusdt-1d-2026-10-09.md` bands a triple-smoothed line rather than crossing an oscillator against its signal EMA. Four-axis distinction: signal construction differs (`100 * ema(ema(change,25),13) / ema(ema(abs(change),25),13)` double-smoothed normalized momentum versus summed-ROC, Fisher, or triple-EMA constructions — no pool record evaluates a Blau double-smoothed TSI against its own EMA), trigger differs (oscillator-vs-own-signal-EMA cross versus zero-level or band triggers), exits differ in event set (reversal-only via the opposite cross with no flat state versus flat-capable or band-edge exits), and source identity differs (FMZ 428611 October-2023 versus other FMZ IDs or TV authors).

## Economic mechanism

### Source-reported

Blau double-smoothed momentum: the bar-to-bar price change is double-smoothed by nested long/short EMAs and normalized by the identically smoothed absolute change, yielding a bounded (-100/+100) oscillator that measures the absolute strength and direction of moves while resisting noise and spikes. A cross of the TSI above its own signal EMA is read as buying power taking over (long); a cross below as selling power taking over (short). The page prose adds that an RSI 50-level filter avoids counter-momentum noise — pinned above as prose-only, contradicted by the executable code, and excluded from the derived spec.

### Research interpretation

Edge-triggered two-sided reversal system with no price level, band, stop, target, or confirmation leg — always-in-market after the first signal, flipping direction only on the opposite cross. Unlike zero-state holders (Coppock, Fisher) that re-assert a level every bar, this system trades only crossing bars and then holds through the Ramirez regime: chop between crosses costs adverse excursion with no guardrail, while the double smoothing delays both entries and reversals symmetrically. Unlike band/breakout systems there is no volatility or range gate — a flat-line cross on a dead bar flips the position exactly as a high-conviction cross does. Unlike the 15m-signal source, the derived record spends the identical formula on the traded market's own daily closes (predeclared collapse): the bet is on BTCUSDT's own double-smoothed momentum persistence at the daily frame, never on a 15m microstructure edge, an RSI regime, a level, breakout, squeeze, calendar, or mean-reversion anchor.

## Signal

Exact rule as pinned (25/13/13 frozen — the three lengths at defaults; any other value is a different, unpinned rule):

- Declaration (derived): Pine v5-era builtins (`ta.change`, `ta.ema`, `ta.crossover`, `ta.crossunder`, `math.abs`, `strategy.entry` v5 semantics observed). The commented-out `strategy(...)` header (capital, commission, `pyramiding=10`, `default_qty_*`) is inactive text — pinned as unspecified, with house sizing applying to the derived evaluation (see Execution assumptions). `calc_on_every_tick` is unset (defaults false: exactly one evaluation per completed bar).
- Indicator arithmetic (pinned, single-TF collapsed): `pc = change(close)`; `double_smoothed_pc = ema(ema(pc, 25), 13)`; `double_smoothed_abs_pc = ema(ema(abs(pc), 25), 13)`; `tsi_value = 100 * (double_smoothed_pc / double_smoothed_abs_pc)`; `tsi2 = ema(tsi_value, 13)` — all on BTCUSDT `1d` closes (predeclared collapse of the source's `"15"` security feed; nesting order, lengths, and operators verbatim).
- Entry long: `buy = crossover(tsi_value, tsi2)` → `strategy.entry("BUY", long)` — fires only on the crossing bar on confirmed closes, same-bar-close execution under the derived declaration. While already long, a repeat `buy` is a no-op by record rule (predeclared single-unit pin).
- Entry short / reversal: `sell = crossunder(tsi_value, tsi2)` → `strategy.entry("SELL", short)` — fires only on the crossing bar; while long it closes the full long and opens the full short in the same execution step (full reversal, no residual leg); while already short, a repeat `sell` is a no-op by record rule. Before the first signal the system is flat (no position by construction).
- `buy`/`sell` are mutually exclusive on every bar by construction (the TSI cannot cross its signal line in both directions on one bar), so no bar can ever fire both legs — no same-bar ordering ambiguity exists anywhere in this record. The measure-zero edge `tsi_value == tsi2` fires neither leg (both strict cross predicates fail) and the position simply holds — stated, not patched. A `0 / 0` divide (a run of zero-change bars driving the smoothed absolute change to exactly zero) yields NaN, which fires neither cross — pinned as hold, never patched with a guard constant.
- Risk legs (pinned absence, not invented): 0 `strategy.close`, 0 `strategy.exit`, 0 `strategy.order` ship anywhere — the derived posture is explicitly no stop, no target, no trailing, no time exit; the page prose's stop-loss suggestions ("trailing stop loss, time-based stop loss...") are optimization wishes, never rules, and none is adopted here.
- Direction: two-sided long/short with symmetric reversal. Futures venue required for the short leg (source venue is already `Futures_Binance BTC_USDT` — pinned).
- Display isolation: `hline`, `plot`, `alertcondition`, and `bgcolor` legs (including every RSI/CCI/stoch read) render or notify only and cannot change any order.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (sole series read by `change(close)` in the derived record). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line. The source's 15-minute `request.security` dependency is removed by the predeclared collapse — the derived record has no multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1d` (source chart header `period: 1d`; `basePeriod: 1h` equals native 1h execution granularity — 24 1h bars per 1d bar on a 24/7 venue — and with market-entry reversal legs only plus zero intrabar-conditional legs, no intrabar path exists for the base to affect). The order logic makes no live `request.*` call, so it is single-frame by construction.
- Warmup: `change` needs 1 bar, the nested EMAs need 25 then 13 bars of seeding, and the signal EMA needs 13 bars of TSI output. The adopted warmup is the first 60 completed `1d` bars flat by record rule (predeclared researcher choice — covers 1 + 25 + 13 + 13 plus seeding margin); no signal before bar 61 may trade. No repainting (`change`/`ema` read only completed closes), no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (source venue is already `Futures_Binance BTC_USDT` on the source `1d` chart frame — naming normalization to `BTCUSDT` is the only market change; the signal-series collapse 15m→own-1d is the predeclared derivation, never presented as source-native).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-tick/next-open (no execution-timing argument ships anywhere); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with mutually exclusive cross legs and no stop/target legs, there is no same-bar ordering ambiguity of any kind.
- Sizing/capital/costs: the source ships no live sizing — only entry `qty = 1` arguments and the inactive commented header's capital/commission text — with no commission, fee, slippage, margin, or funding assumption active anywhere. The explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all) apply to the derived evaluation here, with the single-unit/no-add/reverse-full position pin from Signal, never presented as source-native behavior.
- Concurrency: at most one unit per side under the fixed order IDs `BUY`/`SELL` (predeclared pin over inactive header text); repeat same-side crosses while positioned are no-ops; the opposite cross reverses in full in one step; re-entry after a reversal needs only the next opposite cross (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The short leg requires margin-short permission, realistic on the pinned perpetual venue.

## Evidence

### Source-reported

The page ships the full construction (15m `request.security` feed line with `"15"` default, 25/13/13 inputs, `double_smooth` nesting, `100 * dspc / dsapc` normalization, signal EMA, `ta.crossover`/`ta.crossunder` entry predicates, BUY-long/SELL-short order pair, `TSI BTCUSD 15p` working title, bilingual TSI+RSI prose, the 1d/1h Sep-2022→Oct-2023 backtest header on `Futures_Binance BTC_USDT`). It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.close`, 0 `strategy.exit`, 0 `strategy.order` — the sole position-changing path is the opposite cross reversing the full unit. The absence of any live stop is coded absence, disclosed, not a tunable parameter here.
2. Always-in-market exposure, admitted plainly: after the first cross the system is never flat — a market that chops sideways across the signal line flips the full unit on every alternating cross with no confirmation, no cooldown, and no cost guard. Adverse excursion between crosses has no guardrail of any kind. This is the coded trade, disclosed, not a tunable parameter here.
3. Lag at regime births: the signal smooths an already once-derived series twice (nested 25/13 EMAs on both legs) and then smooths the oscillator again (signal EMA 13) — a sharp V-reversal must drag three smoothers across the gap before any trigger prints, so entries and reversals arrive strictly after the turn by code. The lag is the coded smoother, disclosed, not shortened.
4. Source basis fenced: the source computes on 15-minute closes inside a 1d backtest (signal microstructure far faster than the chart frame — disclosed, never adopted). The derived record spends the identical formula on BTCUSDT's own `1d` closes instead; any divergence between 15m-signal timing and self-signal timing belongs to the predeclared collapse, and this record is therefore never evidence that the original 15m-signal source itself passes.
5. Prose/code divergence fenced: the page prose's RSI-50 filter (`RSI > 50` longs / `RSI < 50` shorts) is contradicted by the executable entries (filter fragments commented out; RSI/CCI/stoch feed display only). The derived spec follows the code and excludes all three oscillators from order logic; a genuinely RSI-gated variant would be a different, unpinned rule — none is admitted here.
6. Derivation boundary fenced: the only non-source-native behaviors in this record are the 15m→own-1d signal-series collapse, code-over-prose entry pin, same-bar-close fills, the single-unit/no-add/reverse-full position pin, the adopted 60-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; lengths, nesting, operators, normalization, the cross predicates, the BUY/SELL order pair, the `==`/NaN hold edges, and the no-stop/no-target/no-cooldown posture are source-verbatim. This record is therefore never evidence that the original next-tick 15m-signal source itself passes.
7. The `25` / `13` / `13` literals, the strict cross definitions (not touch, not level-hold), the full-unit reversal, the two-sided stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning any length, converting edge-crossing into state-holding, adding a stop/target/filter/cooldown/gate, dropping the short leg, or sizing partially instead of full-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `25/13/13` / close-only double-smoothed TSI vs own signal EMA / strict cross legs / full-unit reversal / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Signal-line relevance: replacing the TSI-vs-signal-EMA cross with the raw TSI zero-sign (`tsi_value > 0` long, `< 0` short, reversal on sign flip) must not improve net expectancy; fail ⇒ the signal-EMA cross adds nothing over the oscillator's own sign.
- F2 — Smoothing relevance: replacing the double-nested `ema(ema(...))` smoothing with single-EMA smoothing at the same lengths must not improve net expectancy; fail ⇒ the second smoothing pass adds nothing over single smoothing.
- F3 — Parameter relevance: replacing the pinned `25/13/13` triple with any adjacent classic triple must not improve net expectancy; fail ⇒ the pinned defaults carry no advantage over neighboring smoothings and the record's literal choice is arbitrary.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision frame source-native `1d`; signal series collapsed from the 15m feed — predeclared). The close-only arithmetic ports across perpetual venues without structural change. The short leg requires margin-short permission (realistic on perpetual venues; a spot-only deployment cannot express the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Signal-series collapse: the source signal is 15-minute closes; the derived signal is BTCUSDT-`1d` closes. Momentum timing of a 15m microstructure feed and a daily frame differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- Derived fill timing: the source fills next-tick/next-open on a 1d-decision/1h-base backtest; this record executes same-bar-close on `1d` BTCUSDT perpetual. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden.
- Position-state pin: live same-side-add and reversal-quantity behavior is unspecified-by-active-code (sizing text lives only in entry `qty` arguments and the inactive commented header); the single-unit/no-add/reverse-full pin is a researcher choice, disclosed, not source-verbatim.
- Prose/code divergence: the RSI-50 filter exists only in prose and is excluded here — a reader trusting the prose alone would reconstruct a different, unpinned rule.
- No price stop, no time stop, never flat after the first signal: adverse excursion after entry has no guardrail beyond the opposite cross, which may arrive many bars later or after deep excursion; chop across the signal line flips the full unit repeatedly. This is the coded posture, disclosed as the record's principal risk.
- No source cost declaration: no live capital, commission, fee, slippage, margin, or funding assumption ships anywhere in the active code — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Venue naming only: the source venue is already `Futures_Binance BTC_USDT`; the derived venue is Binance `BTCUSDT` perpetual. Microstructure, tick size, fee, and funding differences are carried by the house overlay — no equivalence is claimed.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- FMZ canonical strategy page (created 2023-10-07): https://www.fmz.com/strategy/428611
- Pine strategy semantics (order calls, default execution, v5 built-ins): https://www.tradingview.com/pine-script-reference/v5/
