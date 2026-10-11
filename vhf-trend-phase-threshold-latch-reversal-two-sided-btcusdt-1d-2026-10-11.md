---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: VHF trend-phase threshold-latch reversal two-sided on BTCUSDT 1d bars
created: 2026-10-11
updated: 2026-10-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-01-08
sources:
  - https://www.fmz.com/strategy/438009
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/平均范围趋势过滤器回测策略Vertical-Horizontal-Filter-Backtest-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# VHF trend-phase threshold-latch reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (immutable public mirror file plus its recorded FMZ canonical page, fetched 2026-10-11):

- Canonical page: https://www.fmz.com/strategy/438009 (fetched live over HTTPS during this cycle with HTTP 200, 753173 bytes of landing HTML). Title `平均范围趋势过滤器回测策略Vertical-Horizontal-Filter-Backtest-Strategy` matches the mirror `> Name` verbatim; author token `ChaoZhang` × 2; prose states the rule twice (ZH/EN): `VHF = (Highest(Length) - Lowest(Length)) / SUM(ABS(Close-Close[1]), Length)` — above the signal threshold prices are in a trend state, below it in a congestion state, with trading signals generated accordingly. Word-boundary counts over the whole landing HTML: `Vertical Horizontal Filter` 11, `VHF` 21, `Sharpe` 0, `Win Rate` 0, `Max Drawdown` 0, `Annualized` 0, `Profit Factor` 0, `Net Profit` 0 — the page ships no performance numbers of any kind for this strategy; the sole `return` token is site-chrome JavaScript (`window.__cdn=function(p){...return b?...}`), not a performance figure. The prose admits parameter sensitivity and recommends pairing a stop loss (`需搭配止损`) as optimization advice — never a coded rule, never a source fact here.
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (verified as the repository head via `git ls-remote` during this cycle — the same head pin as the merged RVI-swma, Support-Resistance-fractal, NRTR, Bollinger, PVT-EMA, KDJ, STARC, T3-Tillson, WaveTrend, TSI and further admissions), exact file path `平均范围趋势过滤器回测策略Vertical-Horizontal-Filter-Backtest-Strategy.md`. File 6907 bytes, blob SHA `1d5064f7af6bfa352e6be5399d3c00d6573320fc` (verified with `git hash-object` reproducing the identical SHA on re-download, and matching the GitHub contents API `sha`/`size` at the pinned commit). The mirror prints `> Name`, `> Author` = `ChaoZhang`, one backtest screenshot image (performance content unread — no numbers transcribed, never a source fact here), the bilingual rule prose quoted above, the Strategy Arguments table (`Length = 28`, `Signal = 0.4`, `Trade reverse = false` — matching the code defaults exactly), `> Detail` = https://www.fmz.com/strategy/438009, `> Last Modified` = `2024-01-08 10:20:25` (date part adopted as `source_as_of`), and the FMZ backtest stanza (`start: 2023-01-01`, `end: 2024-01-07`, `period: 1d`, `basePeriod: 1h`, `Futures_Binance BTC_USDT`).
- Full `//@version=2` block read in full (order-affecting lines: the `strategy(` declaration, the 3 inputs, the `xHH`/`xLL`/`xNumerator`/`xDenominator`/`xVHF` legs, the `pos` latch, the `possig` line, the two level `strategy.entry` blocks; the `hline`/`barcolor`/`plot` visuals gate no order — see census).
- Text census over the pinned code block: 1 `strategy(` (`strategy(title="Vertical Horizontal Filter Backtest")` — title only, no `pyramiding`, no `process_orders_on_close`, no `initial_capital`, no `commission`, no `calc_on_every_tick`, pinned as written) / 0 `study(` / 0 `indicator(` / 2 active `strategy.entry` (`"Long"`/`strategy.long` when `possig == 1`, `"Short"`/`strategy.short` when `possig == -1`, no `qty=`/`limit=`/`stop=`/`when=` qualifiers) / 0 `strategy.close` / 0 `strategy.exit` / 0 `strategy.order` / 0 `strategy.cancel` / 0 `crossover` / 0 `crossunder` / 0 `ta.cross` / 1 `highest(` / 1 `lowest(` / 1 `sum(` / 2 `abs(` / 0 `request.security` / 0 `security(` / 3 `input(` (`Length = 28`, `Signal = 0.4`, `reverse = false` — the code defaults govern) / 4 `iff(` (two nested in `pos`, two nested in `possig`) / 2 `nz(` (both `nz(pos[1], 0)` seed initializers, never order-gating beyond the latch hold) / 1 `hline(` / 1 `barcolor(` / 1 `plot(` (all display-only) / `close` in the denominator leg / `high` in `xHH` / `low` in `xLL` / 0 `open` / 0 `volume` / 0 `ema(` / 0 `sma(` / 0 `rma(` / 0 `wma(` / 0 `rsi(` / 0 `stdev(` (the full indicator stack is highest/lowest/sum/abs only — no recursive smoother exists anywhere) / 0 `time(` / 0 `alert(` / 0 `var` / 0 `pyramiding` / 0 `process_orders_on_close` / 0 `commission` / 0 `barstate` / 0 `lookahead`. No portable economics beyond the two bare order legs ships anywhere — recorded as an absent-economics stub, never as zero-cost evidence.
- Licence and rights: the mirror block carries an HPotter educational-use header (`Copyright by HPotter v1.0 27/04/2018`, Adam White 1991 lineage); this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly six: (1) market pin `BTCUSDT` on Binance futures with the source-native `1d` frame kept (the source stanza pins `1d`/`1h` on `Futures_Binance BTC_USDT` — frame-faithful, venue transfer, symbol spelling and futures short permission disclosed here, never presented as source-native); (2) completed-bar decisions with same-bar-close fills (the source ships no `process_orders_on_close` argument — Pine default would fill later; this record's timing is a predeclared derivation, disclosed here); (3) an adopted 150-bar warmup with pre-warmup bars flat by record rule (covers the 28-bar highest/lowest/sum seeds with margin — see Required data); (4) house sizing/capital/costs replacing the absent source economics (see Execution assumptions); (5) single-unit/no-add/reverse-full position pin carried explicitly (no `pyramiding` argument ships anywhere; the level entries re-assert every bar while latched, so same-side repeats are no-ops and the opposite entry reverses the full unit in one step — see Signal); (6) `reverse = false` frozen at the code default so `possig == pos` verbatim (any `true` value is a different, unpinned rule — disclosed here, never presented as source-native). The `Length = 28` / `Signal = 0.4` coefficients, the range-ratio VHF construction, the threshold latch, the level BUY/SELL order pair, the two-sided reversal stance, and the no-stop/no-target posture are source-verbatim.

Pre-write dedup (2026-10-11): working-tree case-insensitive search for `vhf` returns only one incidental prose mention inside `ac-accelerator-rise-fall-two-sided-btcusdt-1d-2026-10-09.md` (its own dedup paragraph noting a `vhf` search returned zero — not a VHF mechanism record); search for `vertical-horizontal` / `vertical horizontal` returns nothing else. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool relatives: `dmi-swings-contrarian-adx` (directional-movement ADX system — different construction, no range-ratio), `sideways-dmi-bollinger-breakout-long` (DMI-gated lower-band reclaim — different family and trigger), `chop-zone-dmi-psar-reversal` (DMI/PSAR chop machine — different series), `tsmom-12m-sign-monthly-long` (time-series slope sign — different statistic), `nr7-price-breakout-long` (narrowest-range breakout — different trigger). None computes a highest-minus-lowest range over cumulative absolute close-change ratio with a fixed threshold latch. Not a trivial parameter variant.

## Economic mechanism

### Source-reported

Trend-phase capture without any curve fitting (prose plus code): the numerator (`highest(high,28) − lowest(low,28)`) is the market's 28-bar excursion envelope; the denominator (`sum(abs(close − close[1]),28)`) is the path actually travelled to draw that envelope. Their ratio (VHF) is near 1 when price moves in a straight line and collapses toward 0 when price chops sideways covering little net ground. Above `0.4` the design reads a trending phase and holds long; below `0.4` it reads congestion and holds short. The prose bets this price-native statistic avoids the lag and self-reference of SMA/EMA-based trend filters, warns it is parameter-sensitive and blind to false trends at turning points, and suggests a stop loss only as future optimization — never a rule.

### Research interpretation

Phase-latch reversal machine, level-triggered, two-sided, always-in-position after the first signal. Unlike cross-family records (TSI, KST, Schaff, QQE) there is no edge and no signal line — the latch level itself is the state: every bar with VHF above `0.4` asserts long, every bar below asserts short, and equality holds the previous state, so the position never rests flat once armed. Unlike gate-family records (SuperTrend #63, Chandelier #89, SSL #92) the threshold is a fixed constant, not a trailing rail — the `0.4` line never moves after any entry, so time in a congestion-short through a grinding trend is the coded cost of the design. Unlike volume-family records (OBV-EMA, PVT-EMA, Klinger, CMF-velocity) it reads no `volume` and no `open` — venue volume-reporting differences touch nothing. The deliberately uncomfortable leg is the congestion short: chop is traded short rather than sat out, so a sideways market that drifts upward grinds against the position by construction, disclosed, not smoothed.

## Signal

Exact rule as pinned (`Length = 28`, `Signal = 0.4`, `reverse = false` frozen — any other value is a different, unpinned rule):

- Declarations (derived): single-unit long/short machine over `BTCUSDT 1d` with same-bar-close execution and house sizing/costs (see Execution assumptions). State ∈ {flat, long, short}; flat exists only before the first signal. At most one unit is ever held.
- Phase statistic, pinned verbatim: `xHH[t] = highest(high, 28)[t]`; `xLL[t] = lowest(low, 28)[t]`; `xNumerator[t] = abs(xHH[t] − xLL[t])`; `xDenominator[t] = sum(abs(close − close[1]), 28)[t]`; `xVHF[t] = xNumerator[t] / xDenominator[t]`.
- Threshold latch, pinned verbatim: `pos[t] = 1` when `xVHF[t] > 0.4`, `-1` when `xVHF[t] < 0.4`, else `pos[t-1]` (seed `0`, flat — pinned initialization, never traded, see Required data). With `reverse = false`, `possig == pos` on every bar — pinned verbatim.
- Orders, pinned verbatim: `strategy.entry("Long", strategy.long)` when `possig == 1`; `strategy.entry("Short", strategy.short)` when `possig == −1`. Both are level conditions re-asserted every latched bar: from flat the first latched bar opens; while holding the same side repeats are no-ops under the single-unit pin; on the first bar of the opposite latch the opposite entry closes the full unit and opens the full opposite unit in one step (full reversal, no residual leg).
- Exits and risk, pinned absence (coded, not invented): 0 `strategy.close`, 0 `strategy.exit`, 0 `strategy.order` ship anywhere — the sole position-changing path is the opposite latch reversing the full unit. No stop, no target, no trailing, no time exit, no cooldown (explicitly none, not invented). The page prose's stop-loss suggestion is optimization advice, never a rule, and none is adopted here.
- Direction: two-sided with resting exposure to both sides across time, but never simultaneously. A long-only reading would contradict the `"Short"`/`strategy.short` block and is explicitly not this record. A flat-in-congestion reading would contradict the `iff(xVHF < Signal, −1, ...)` leg and is explicitly not this record.

## Required data

- Completed `1d` bars of BTCUSDT: `high` (`xHH`), `low` (`xLL`), `close` (denominator path sum) — no `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read anywhere.
- Single decision timeframe `1d` (source-native frame kept; zero `request.security`/`security(` calls ship anywhere, so no second evaluated frame exists by construction).
- Warmup: the binding seed stack is the 28-bar `highest`/`lowest`/`sum` windows plus the one-bar `close[1]` read. The adopted warmup is the first 150 completed `1d` bars flat by record rule (predeclared researcher choice — over 5× the 28-bar seed with margin; no traded bar reads a seeded value). Seed behavior is deterministic and fenced: under-seeded windows resolve `na`, `na` comparisons are false, and the latch holds its `nz(pos[1], 0) = 0` seed — flat by code, never a researcher tie-break. A 28-bar zero-path drought (all closes identical) yields `xVHF = 0/0 = na`, under which both latch arms are false and the previous state holds — fenced, never hidden. No repainting (fixed causal reads only, no negative shift), no future reference, no full-sample normalization, no `lookahead`, no `barstate`-gated order path; one evaluation per completed bar. The source stanza's `basePeriod: 1h` documents the author's own FMZ 1d backtest plumbing, not a second evaluated frame in the Pine logic — disclosed, not carried into this record.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (derived pin; the source stanza pins `1d`/`1h` on `Futures_Binance BTC_USDT` — frame kept, venue transfer, symbol spelling and futures short permission disclosed here, never presented as source-native). The short leg needs a venue with short permission; futures satisfies this — disclosed.
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source ships no `process_orders_on_close` argument — Pine default would fill later; this record claims no source-native timing and no intrabar behavior. With no stop/limit legs anywhere there is no same-bar TP/SL ordering ambiguity, and each bar resolves to at most one order event (open, no-op re-assertion, or full reversal).
- Intrabar recalc (predeclared derivation): the source ships no `calc_on_every_tick`; this record evaluates one discrete decision per completed bar with no post-fill recalculation — disclosed, not hidden.
- Sizing/capital/costs: the source ships no portable economics of any kind (bare `strategy.entry` legs with no `qty=`, no capital amount, no commission/slippage/funding/margin argument ships anywhere — recorded as an absent-economics stub, never as zero-cost evidence) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: single-unit machine by predeclared pin — at most one unit long or short; same-side re-assertions are no-ops; the opposite latch reverses in full in one step. No cooldown ships anywhere (explicitly none, not invented). No shared portfolio state, no cross-sectional ranking, no multi-pair logic. The `hline`/`barcolor`/`plot` calls render only and gate no order — disclosed.

## Evidence

### Source-reported

The mirror ships the full construction (the title-only `strategy(` declaration, all 3 inputs with code defaults, the `xHH`/`xLL`/numerator/denominator/VHF legs, the `pos` threshold latch, the `possig` line, the level `"Long"`/`"Short"` order pair, the HPotter/Adam-White lineage comment, the arguments table, and the FMZ backtest stanza). It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — the one backtest screenshot image is untranscribed and this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden risk layer: 0 `strategy.close`, 0 `strategy.exit`, 0 `strategy.order` — the sole position-changing path is the opposite latch reversing the full unit. The no-stop/no-target/no-trailing posture is coded absence, disclosed, not a tunable parameter here.
2. No smoothing-seed dispute: the only functions in the order path are `highest`/`lowest`/`sum`/`abs` over fixed 28-bar windows plus one-bar `close[1]` — no EMA/RMA/WMA/SMA/RSI/stdev variant choice anywhere; the adopted 150-bar warmup absorbs the 28-bar seed over five times with margin.
3. No tie-semantics dispute: there are no `crossover`/`crossunder`/`ta.cross` calls anywhere. The latch uses strict `>`/`<` against the fixed `0.4` line — an exact `0.4` print holds the previous state by code, pinned as written.
4. Zero-path fenced: a 28-bar identical-close drought yields `0/0 = na`, both latch arms false, previous state held — no order event can print from a degenerate print, disclosed.
5. Congestion-short fenced: `iff(xVHF < Signal, −1, ...)` explicitly holds short through congestion — a flat-in-chop reading would contradict the code and is explicitly not this record.
6. `reverse = false` fenced: the `possig` wrapper collapses to identity at the code default; any `true` value reassigns every signal and is a different, unpinned rule — disclosed in the derivation declaration.
7. Single-frame fenced: zero `request.security`/`security(` calls ship anywhere — no MTF pull, no cross-symbol pull, no `lookahead`. Every input is a causal function of completed `high`/`low`/`close` values inclusive of the decision bar, computable point-in-time with no future leakage — stated plainly.
8. Dead-surface fenced: `hline`/`barcolor`/`plot` render only and gate no order; none changes any order event under this record's timing, disclosed.
9. Order-id completeness fenced: the sole long id is `"Long"` and the sole short id is `"Short"`; with single-unit construction there is at most one unit to reverse, so no partial-fill residue is reachable by code.
10. Source-economics absence fenced: the stanza's date range and venue describe the author's FMZ backtest run, not portable cost facts — this record carries no commission/slippage/funding claim from the source and assigns all economics to the disclosed house overlay.
11. Derivation boundary fenced: the only non-source-native behaviors in this record are the `BTCUSDT` market pin with the source-native `1d` frame kept, completed-bar same-bar-close fills, the adopted 150-bar warmup with record-rule pre-warmup flat, single-unit/no-add/reverse-full construction, `reverse = false` frozen at default, discrete-bar execution without intrabar recalculation, and house sizing/costs — all predeclared above; the `28`/`0.4` coefficients, the range-ratio VHF construction, the threshold latch, the level order pair, the two-sided reversal stance, and the no-stop posture are source-verbatim. This record is therefore never evidence that any other market, frame, parameter set, or timing of the source passes.
12. Network limitation disclosed: every formula line above was byte-verified in the pinned mirror file at commit `7853bb2` (6907 bytes, blob SHA recorded, `git hash-object` identical on re-download, contents-API `sha`/`size` matched); the FMZ canonical page verified live the title, the `ChaoZhang` token, the VHF prose and formula, and the absence of any performance numbers — the division of evidence is disclosed here, not hidden.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `Length = 28` / `Signal = 0.4` / `reverse = false` / range-ratio VHF / threshold latch / level entries / reversal-only exits / no-stop posture / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Threshold relevance: replacing the `0.4` latch with always-long (every bar asserts long, shorts disabled, same risk posture) must not improve net expectancy; fail ⇒ the trend-phase threshold adds nothing over a buy-and-hold leg.
- F2 — Phase-statistic relevance: replacing the range-ratio VHF with a constant mid value that alternates only on the latch seed (same threshold, same rails, same risk posture) must not improve net expectancy; fail ⇒ the excursion-over-path statistic adds nothing over its own threshold mechanics.
- F3 — Two-sided relevance: running the long leg only with the short leg disabled (same statistic, same latch, same risk posture) must not improve net expectancy; fail ⇒ the congestion-short stance adds nothing over its long half.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (derived pin; the source stanza pins `1d`/`1h` on `Futures_Binance BTC_USDT`). The high/low/close arithmetic ports across perpetual venues without structural change — no volume or open read means venue volume-reporting and auction-open differences touch nothing, disclosed as a robustness property, not a portability proof. The two-sided stance requires a short-capable venue (futures satisfies this); a spot deployment would express only the long half and is a different, unpinned claim. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no session gating anywhere); decision boundaries are venue-feed 1d bars, disclosed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived market pin: the source stanza pins `Futures_Binance BTC_USDT`; this record pins `BTCUSDT` Binance futures with the source-native `1d` frame kept. Cross-market behavior differences are real — the adaptation is disclosed, and this record makes no claim about any other market.
- Derived timing: the source ships no `process_orders_on_close`; this record executes completed-bar same-bar-close discrete decisions. Fill economics under discrete-bar timing differ from next-bar fills by construction — the adaptation is disclosed, not hidden, and this record makes no claim about any other timing's performance.
- Reversal-only risk: there is no stop, no target, no trailing, no time exit, and no flat state after arming — an adverse trend-phase print holds long indefinitely, a grinding uptrend inside a congestion latch holds short indefinitely, and whipsaw across successive reversals is the coded cost of the design, disclosed, not smoothed, not supplemented.
- No source economics: the source ships no capital amount, commission, slippage, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Seed coverage: the 28-bar highest/lowest/sum windows settle across early history; the first 150 `1d` bars are flat by record rule, so early-history signals never enter any evaluation.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- FMZ canonical strategy page (title/author/prose verified live via HTTP-200 page record): https://www.fmz.com/strategy/438009
- Immutable mirror file at pinned commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (blob `1d5064f7af6bfa352e6be5399d3c00d6573320fc`, 6907 bytes): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/平均范围趋势过滤器回测策略Vertical-Horizontal-Filter-Backtest-Strategy.md
