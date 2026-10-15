---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: 8-day SMA5 run momentum-reversal two-sided on BTCUSDT 1d bars
created: 2026-10-16
updated: 2026-10-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: high
source_as_of: 2023-03-06
sources:
  - https://www.tradingview.com/script/fXvKVs5J-8-Day-Run-Momentum-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# 8-day SMA5 run momentum-reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end during this cycle (2026-10-16):

- Canonical strategy page: https://www.tradingview.com/script/fXvKVs5J-8-Day-Run-Momentum-Strategy/ (`8 Day Run - Momentum Strategy` by `Marcn5_`, `OPEN-SOURCE SCRIPT` badge, published `Mar 6, 2023`, no updates). Fetched live over HTTPS during this cycle (HTTP 200, 514657 bytes of page HTML with a desktop Chrome user-agent). Page-embedded metadata verified from the same fetch: `created_at` = `2023-03-06T12:44:31Z` (adopted as `source_as_of`), chart interval `1D`, chart symbol `CME_MINI:ES1!` (S&P 500 E-mini Futures), script id part `PUB;20c6da6239a74855958a71f99943041e`, page title `8 Day Run - Momentum Strategy by Marcn5_`.
- Author prose on the page (verified verbatim in the fetched HTML): inspired by Linda Bradford Raschke; captures momentum effects on daily periodicities; once prices print a run of 8 or more consecutive closes above or below the 5-period simple moving average the strategy is primed; it enters short on the first close above the 5sma after a run of 8+ closes below (mirror for long); all trades exit on the first close back above/below the 5sma. The prose nominates daily bars and futures markets, never crypto, never a second indicator.
- Executable Pine read live in a real browser session on the page's `Source code` tab during this cycle: complete `//@version=5` block, 43 lines (`View in Pine Editor・43 lines`), copyright `// © Marcuscor`, licence header Mozilla Public License 2.0, comment `Inpsired by Linda Bradford Raschke: a strategy for trading momentum in futures markets` (sic — author's own spelling, quoted exactly once here and never relied upon for any gate).
- Text census over the verified block: 1 `strategy(` (`"8D Run"`, `initial_capital = 50000`, `commission_value = 0.0004` — 0 `pyramiding`, 0 `process_orders_on_close`, 0 `calc_on_every_tick`, 0 `max_bars_back`, recorded as absent, never as evidence) / 1 `ta.sma(` (`close, 5`) / 2 `ta.barssince(` (`close < SMA`, `close > SMA`) / 2 `strategy.entry` (`"EL"`/`strategy.long`, `"ES"`/`strategy.short`) / 2 `strategy.close` (`"EL"` on `close > SMA`, `"ES"` on `close < SMA`) / 0 `strategy.exit` / 0 `strategy.order` / 0 `strategy.cancel` / 0 `stop=`/`limit=`/`profit=`/`loss=` / 0 `input.*` of any kind (the `5` and `8` are hardcoded literals, never inputs) / 0 `crossover(`/`crossunder(`/`ta.cross` / 0 `request.*`/`security(`/`timeframe(` / 0 `open`/`high`/`low`/`volume` reads anywhere (the only series read is `close`) / 0 `strategy.position_size`/`opentrades`/`equity` / 4 `bgcolor(` (display-only, fenced below).

Licence and rights: the page is a public open-source TradingView script (MPL-2.0 header on the code, open-source badge on the page). This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) market pin `BTCUSDT` Binance futures `1d` (the source demonstrates on `CME_MINI:ES1!` daily bars — equity-index futures, never crypto; the daily decision frame is kept source-native, only the venue/market is adapted and disclosed here, never presented as a source claim); (2) same-bar-close market fills (the source ships no execution-timing argument — Pine default evaluates per completed bar and fills on the next bar; this record pins completed-bar decision with same-bar-close execution, predeclared); (3) an adopted 20-bar warmup with pre-warmup bars flat by record rule (covers the SMA5 5-bar seed plus the 8-bar run plus the one-bar `[1]` confirmation plus `barssince` na-memory, with margin — see Required data); (4) house sizing/capital/costs replacing the source demo economics (`initial_capital = 50000`, `commission_value = 0.0004` recorded as absent portable economics, never as evidence — see Execution assumptions). The `5` / `8` constants, the `barssince`-run construction, the prior-bar confirmation, the `EL`/`ES` entry pair, the first-close-back exits, and the no-stop-no-target posture are source-verbatim. **No Safety Order, no DCA event, no pyramiding, no time exit, and no third leg is admitted in this record's version** — the admitted machine holds at most one leg per direction ids; the house BO/SO/SO DCA matrix is a downstream experiment, never part of this admission.

Pre-write dedup (2026-10-16): working-tree case-insensitive searches for `8d run`, `8 day run`, `8-day-run`, `fxvkvs5j`, `marcn5`, `marcuscor`, `triggerbuy`, and `triggersell` return zero strategy records using this source, author, or code. `sma(close, 5)` (both spacings) returns zero pool constructions. `barssince` hits pool-wide are different constructions (Renko brick-color recency, cyber-cycle self-cross, Williams-fractal, octa-EMA-Ichimoku, sideways-DMI, Darvas box rails — none counts closes against an SMA or gates entries on a completed run). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state-following reversal two-sided) — per-PR titles checked live, zero run-momentum content in any of them. Closest pool records are different mechanism classes: `three-down-three-up-consec-close-long-btcusdt-1h` counts strict close-vs-prior-close chains with no moving average anywhere (different signal object: candle-to-candle direction, never price-vs-average side); `double-seven-connors-pullback-long-btcusdt-1d` buys 7-day closing-range extremes under an MA200 regime gate (different trigger: range position, never a side-run plus first cross-back); `connors-rsi2-ma70-fade-two-sided-btcusdt-1d` fades RSI2 extremes (oscillator level, never a run count). No pool record gates entries on consecutive closes on one side of an average followed by the first cross-back bar.

## Economic mechanism

### Source-reported

Momentum capture on daily bars: after buyers hold price on one side of the 5-day average for 8 or more consecutive closes (a persistent one-sided run judged unlikely to extend without a pause), the strategy takes the first close back across the average as the entry — long on the first close at or below the average after a run of 8+ closes at or above it, short on the first close at or above the average after a run of 8+ closes at or below it (source prose, verbatim: it will then enter a short on the first close above the 5sma after a run of 8 or more closes below the 5sma, and it will enter a long when the price closes below the 5sma after a run of 8 or more closes above the 5sma; code governs equality per Signal) — and exits on the first close back across the average in the other direction. The source frames this as capturing momentum effects: the first counter-move through the average after a persistent run is entered in the direction of that prior run and held to the next recross, never a breakout, squeeze, level, or divergence print.

### Research interpretation

Precondition-plus-trigger reversal machine, two-sided. Unlike plain moving-average cross systems (every cross trades), here the cross is necessary but not sufficient: the bar before the trigger must complete a qualifying 8-bar side-run, so most crosses are ignored and only post-run first recrosses trade. Unlike consecutive-candle counters (close-vs-prior-close chains), the run is measured against a moving reference (price side of SMA5), so flat drift that hugs the average never accumulates a run while persistent premium/discount does. Unlike stop-and-reverse flip systems, exits are independent per-leg first-recross closes, not opposite entries — a leg that never sees its recross is simply held. The price of the run filter is missing every V-shaped turn that prints fewer than 8 one-sided closes; the price of the first-recross exit is surrendering any extended trend after a single adverse close through the average.

## Signal

Exact rule as pinned (Pine v5, zero inputs — `5` and `8` are hardcoded literals; any other value is a different, unpinned rule):

- Declarations (derived): two-leg state machine over `BTCUSDT 1d` with same-bar-close execution and house sizing/costs (see Execution assumptions). Order ids `EL` (long) and `ES` (short) exactly as shipped. No Safety Order, no DCA event, no pyramiding — explicitly none admitted here, not invented.
- Average (pinned verbatim): `SMA(t) = ta.sma(close, 5)(t)`; `TrendUp(t) = close(t) >= SMA(t)`; `TrendDown(t) = close(t) <= SMA(t)`.
- Long trigger (pinned verbatim): `TriggerBuy(t) = ta.barssince(close < SMA)(t) >= 8` (bars since the last close strictly below the average is 8 or more — i.e. the last 8+ closes printed at or above the average); `Buy(t) = TriggerBuy(t-1) and TrendDown(t)` — the run must have qualified on the prior completed bar and the current completed bar closes at or below the average.
- Long entry/exit (pinned verbatim): `Buy(t)` → `strategy.entry("EL", strategy.long)`; `close(t) > SMA(t)` → `strategy.close("EL")`.
- Short trigger/entry/exit (pinned verbatim mirror): `TriggerSell(t) = ta.barssince(close > SMA)(t) >= 8`; `Sell(t) = TriggerSell(t-1) and TrendUp(t)`; `Sell(t)` → `strategy.entry("ES", strategy.short)`; `close(t) < SMA(t)` → `strategy.close("ES")`.
- Entry and same-leg exit are mutually exclusive by construction on every bar: `Buy` needs `close <= SMA` while the `EL` close needs `close > SMA` (strict), and symmetrically for the short leg — no bar can both enter and exit the same leg, so no priority rule is needed or invented.
- Exits/risk: the first-close-back exit per leg only. No stop, no target, no trailing, no time exit — explicitly none by record rule, not invented. A leg whose recross print never arrives is held indefinitely.
- Direction: two-sided with explicit `EL` long and `ES` short legs (0 ambiguity about side intent; the short leg requires a shortable venue — the futures pin, disclosed).
- Re-entry: after any `strategy.close`, the next qualifying `Buy`/`Sell` bar re-enters (no cooldown specified — explicitly none, not invented). Same-direction re-trigger while the leg is open is a no-op under the Pine default no-pyramiding construction (absent `pyramiding` argument = v5 default 0 — recorded as the shipped default per pool precedent, never as a chosen parameter).

## Required data

- Completed `1d` bars of BTCUSDT: `close` only. No `open`/`high`/`low`/`volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (the Pine logic contains no timeframe constant and zero `security(`/`request.*` calls — single-frame by construction; the page chart interval `1D` and the daily-periodicity prose are kept, not transferred).
- Warmup: the binding cost is the run seed — `ta.sma(close,5)` needs 5 bars, `TriggerBuy`/`TriggerSell` need 8 one-sided closes, and `Buy`/`Sell` read the prior bar's trigger, so the first executable signal sits at bar 10 at the earliest (plus `barssince` na-memory before the first opposite-side cross). The adopted warmup is the first 20 completed `1d` bars flat by record rule (predeclared researcher choice — full seed plus wide margin; no signal before bar 21 may trade). No repainting (`calc_on_every_tick` unset so Pine evaluates per completed bar; every comparison reads completed bars only, and entries explicitly reference the prior bar's trigger), no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Every input is complete at bar `t`'s close — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (source demonstrates on `CME_MINI:ES1!` daily bars — venue/market adaptation disclosed in Provenance, never presented as a source claim; the `1d` decision frame is source-native).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) — the same verified execution primitive as the admitted `three-down-three-up-consec-close-long-btcusdt-1h`, `qstick-zero-cross-trend-two-sided-btcusdt-1h`, `ppo-signal-cross-reversal-two-sided-btcusdt-1d`, and `bollinger-band-breakout-long-midline-exit-btcusdt-1d` PASS records (single-frame completed-bar decision, same-bar-close market fill, no protective stop/limit legs anywhere in the derived machine, hence no same-bar TP/SL ordering ambiguity; each bar's outcome is a deterministic event: hold, open, close, or the code-ordered dual-leg sequence fenced below). No maker-touch, queue, multi-asset sync, lower/multi-timeframe alignment, non-OHLCV input, or intrabar-path-dependent fill is required by any line of this record.
- Sizing/capital/costs: the source ships demo-only economics (`initial_capital = 50000`, `commission_value = 0.0004` with no commission-type argument — recorded as absent portable economics, never as evidence) — derived evaluation carries the fixed, reproducible house research cost model (Base 6% + Safety 6% + Safety 6% notional framing, Isolated, 3x/5x; pinned house cost assumptions for fees plus modeled funding — no hypothetical zero funding claimed, never presented as source-native behavior). Funding is modeled, never reported as realized or canonical funding; the short leg's funding exposure is flagged as an unmodeled economic term in Limitations. No Safety-Order/DCA event participates in the admitted trigger machine regardless of downstream campaign settings.
- Concurrency: two order ids over one single-asset engine position — at most one net direction exposure at a time; an opposite-leg entry while the other leg is open reverses through Pine's default same-position opposite-entry handling (no second concurrent position is constructed anywhere). No shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The page ships the full construction (SMA5 definition, both `barssince` run counters with the `8` literal, both prior-bar-confirmed triggers, both entry/close order-id pairs, the display-only `bgcolor` legs), the daily-periodicity thesis, the entry/exit prose matching the code, the author/date/open-source stamps, and the `1D` ES1! demonstration chart. The page ships zero performance numbers of any kind (no returns, Sharpe, win rate, drawdown, or profit-factor tokens anywhere on the strategy page — strategy-report tab content is user-specific backtest chrome, never a source performance claim), so this record carries zero source-reported performance numbers and claims no performance of any kind.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No performance to carry, admitted plainly: unlike paper-sourced records with backtest tables, the rule source ships construction, triggers, and prose context only — there is no expectancy number anywhere to fence, and this record claims none.
2. Two-sided posture provably complete: 1 `strategy.long` entry plus 1 `strategy.short` entry with matching per-leg `strategy.close` exits — both directions exist in code, and a long-only reading would contradict the shipped `ES` leg (unlike long-only records that carry zero short calls).
3. No hidden exits or risk layer: 0 `strategy.exit`/`strategy.order`/`stop=`/`limit=` tokens anywhere — the no-stop/no-target posture is the record rule, explicitly none, never hidden. The prose exit ("first close back above/below") is coded exactly as the two `strategy.close` legs, and nothing else exits anything.
4. Same-leg entry/exit exclusivity proved: `Buy` needs `close <= SMA` while the `EL` close needs `close > SMA` on the same bar (strictly exclusive; symmetric for `ES`) — no priority invention is needed or admitted for same-leg sequencing.
5. Degenerate dual-leg tie fenced: `close == SMA` exactly makes both `TrendUp` and `TrendDown` true, so a bar with `TriggerBuy(t-1)` and `TriggerSell(t-1)` both true would assert both `Buy` and `Sell`. Both triggers true on the same prior bar requires 8+ consecutive closes exactly equal to a flat SMA5 (a degenerate constant-price run) — practically impossible on a live venue, and if it ever printed, Pine evaluates the `EL` lines before the `ES` lines, so the bar deterministically enters long then reverses short (net short by code order — disclosed, never traded on, never smoothed).
6. Prose/code equality nuance fenced: the prose says "closes below/above" but the code uses `<=`/`>=` (equality counts as trigger-side, and the run counters use strict `<`/`>`). The code governs every gate here; the prose is context only. An exact-equality close after a run triggers (code), even though the prose reads as strict — disclosed, not repaired.
7. `na`/seed determinism fenced: before seeding, `ta.sma` yields `na`, every comparison with `na` is false, and `na >= 8` never triggers — so no pre-seed bar can fire any leg; the adopted 20-bar flat absorbs all seeding structurally regardless of convention. No seeded or `na` value ever trades.
8. Dead code fenced: the four `bgcolor` calls are display-only (no order call reads any of them); `initial_capital`/`commission_value` are demo economics replaced by the house model. None gates anything.
9. Run/trigger/exit-family overlap fence, admitted plainly: the pool's consecutive-close record counts candle-to-candle direction with no average; the pool's Double-Seven record trades range extremes under a regime gate; the pool's Connors record fades oscillator extremes; the pool's `barssince` records key brick colors, self-crosses, fractals, or box rails. Shared `barssince`/run vocabulary is not shared signal: this record's `barssince(close≷SMA5)>=8` plus prior-bar-confirmed first-recross entry with first-recross exit exists nowhere else in the pool.
10. Economics absence fenced: the `50000`/`0.0004` pair is venue-free demo configuration — the record carries house sizing/costs only as a predeclared derivation, never as a source claim.
11. Derivation boundary fenced: the only non-source-native behaviors in this record are the `ES1!`→`BTCUSDT` market/venue pin (frame kept), the per-completed-bar evaluation with same-bar-close fills, the adopted 20-bar warmup with record-rule pre-warmup flat, and house sizing/costs with no admitted Safety-Order/DCA event — all predeclared above; the `5`/`8` literals, the run counters, the `[1]` confirmation, the entry/exit pairs, the two-sided posture, and the risk posture are source-pinned or predeclared. This record is therefore never evidence that any other market, frame, length, run count, trigger set, or timing of the source passes.
12. Division of evidence disclosed: the formula, literals, order ids, dead code, and prose above were verified in the fetched page HTML (514657 bytes, HTTP 200) and the live browser-read `Source code` tab (43-line `//@version=5` block); the title, author, open-source badge, publication date, `1D` interval, and ES1! chart symbol were verified in the same fetched page metadata. The division is disclosed here, not hidden.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `5` / `8` / `barssince`-run / prior-bar confirmation / first-recross entries / first-recross exits / no-stop-no-target posture / two-sided `EL`+`ES` / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Run-filter relevance: replacing the `8`-run precondition with `1` (every first cross-back of SMA5 trades, same entry/exit handling) must not improve net expectancy; fail ⇒ the 8-bar run filter adds nothing over a plain SMA5 cross-back system.
- F2 — Side-run relevance: replacing the price-vs-average side-run with a plain `crossover`/`crossunder` of close and SMA5 (same legs, same exits) must not improve net expectancy; fail ⇒ measuring the run against the average adds nothing over a raw cross.
- F3 — First-recross-exit relevance: holding each leg until the opposite-leg entry signal instead of the first recross close (same entries) must not improve net expectancy; fail ⇒ the quick first-recross exit is dominated by holding through adverse average excursions on this market.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (source demonstrates on `CME_MINI:ES1!` daily bars — market/venue adaptation disclosed, `1d` frame kept source-native). The rule reads completed daily closes only, so no open-print, session, or cross-venue difference can touch any order-gating line beyond each calendar-day bar's own prints — but spot-vs-perp prints can still differ structurally (funding-driven drift, venue aggregation), so the futures-venue pin is load-bearing and disclosed. Lengths `5`/`8` are fixed bar-count constants, so no fixed-pip recalibration is needed across assets — cross-asset behavior differences are still real and unclaimed. The rule is two-sided with an explicit short leg, so a spot-only deployment cannot express the full machine — full futures expression is assumed only for the pinned venue, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read beyond each bar's own close (no session gating anywhere; the run counters treat each daily bar's close-vs-average side identically); decision boundaries are calendar-day bars of the venue feed, disclosed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- No source economics: the source ships demo-only capital/commission with no fee schedule, slippage, leverage, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Short-leg funding exposure: the `ES` leg holds short perpetual exposure whose funding is modeled, never realized or canonical — adverse funding regimes are an unmodeled economic term, disclosed as a principal risk of the two-sided posture.
- No price stop, no time stop: adverse excursion after entry has no guardrail beyond the first recross close, which may arrive many bars later or after deep excursion; a leg whose recross print never arrives is held indefinitely. This is the record-rule posture, disclosed as a principal risk.
- Run-filter blindness: any V-shaped turn printing fewer than 8 one-sided closes never arms a trigger — the machine sits flat through fast reversals by the prescribed design, trading only slow-formed runs.
- Single-close exit fragility: one adverse close through the average closes the full leg, so wick-driven average touches on volatile daily bars can churn alternating entries and exits with no flat state to rest in, by the prescribed design.
- Seed convention cost: pre-seed `na` behavior is structurally excluded by the adopted 20-bar warmup (which is wider than any code-enforced seed) — early-bar behavior differences between seeding conventions never trade here.
- Next-bar timing reading: the same-bar-close fill is a predeclared derivation from Pine's default next-bar fills; any engine that modeled entries at the next open would trade different (slightly later) events.
- Degenerate-tie residual: the constant-price 8-bar tie analyzed in Negative evidence resolves deterministically by code order but has no live-market calibration — disclosed, never smoothed.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior and never part of this admission — no Safety-Order/DCA event is admitted in this record's version. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- TradingView public open-source strategy, 8 Day Run - Momentum Strategy by Marcn5_ (published 2023-03-06, daily periodicities, zero performance claims — verified live on the page and its Source code tab during this cycle): https://www.tradingview.com/script/fXvKVs5J-8-Day-Run-Momentum-Strategy/
