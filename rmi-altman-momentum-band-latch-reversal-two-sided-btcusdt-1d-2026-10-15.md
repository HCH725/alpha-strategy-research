---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: RMI Altman momentum-band latch reversal two-sided on BTCUSDT 1d bars
created: 2026-10-15
updated: 2026-10-15
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2017-10-19
sources:
  - https://www.tradingview.com/script/gYZ1PPNy-Relative-Momentum-Index-Backtest/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# RMI Altman momentum-band latch reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (verified 2026-10-15):

- TradingView canonical page `Relative Momentum Index Backtest`, strategy by `HPotter` (`WIZARD` badge), carrying the `OPEN-SOURCE SCRIPT` badge, dated `Oct 19, 2017`. Rendered live in a real browser during this cycle: page title, badge, date, author, and the full 42-line `//@version=2` Pine source (`View in Pine Editor・42 lines`) were all read on the `Source code` tab. Code header pins authorship and date verbatim: `Copyright by HPotter v1.0 19/10/2017`. The description block attributes the construction to Roger Altman (`The Relative Momentum Index (RMI) was developed by Roger Altman`, momentum `substituted for strength`, counting up/down days `from the close relative to the close x-days ago where x is not necessarily 1 as required by the RSI`). The page's `WARNING` lines (`For purpose educate only`, bar-colors note) are education-only context and gate no order. This record claims no crypto performance and no reproduced performance.
- Static cross-check: the same canonical URL fetched over HTTPS during this cycle (HTTP 200, 930248 bytes) carries the same `OPEN-SOURCE` badge, the same `HPotter` author marks, and the same `Relative Momentum` description text — confirming the live page read is the same publication, not a lookalike.
- Full-code census over the rendered 42 lines: 1 `strategy(` declaration (`strategy(title="Relative Momentum Index", shorttitle="RMI")`, shipping no `pyramiding`, no commission, no `calc_on_every_tick`, and no `process_orders_on_close` argument anywhere — Pine defaults govern, quoted as absence, never filled in); 2 `strategy.entry` legs (`strategy.entry("Long", strategy.long)`, `strategy.entry("Short", strategy.short)`); 0 `strategy.exit` / 0 `strategy.close` / 0 `strategy.order`; 0 `stop=` / `limit=` / `profit=` / `loss=` / `qty_percent`; 0 `request.*` / `security(` / `timeframe(` / `time(`; 0 `volume` / `open` / `high` / `low` / `hl2` reads (the only price read is `xPrice = close`, plus its own `Length`-lagged value `xPrice[Length]`); 4 `input(` pins (`Length = input(20, minval=1)`, `BuyZone = input(40, minval=1)`, `SellZone = input(70, minval=1)`, `reverse = input(false, title="Trade reverse")`). `hline` / `barcolor` / `plot` legs are visual only and gate no order.

Licence and rights: this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source publication. Researcher-declared adaptations are exactly five: (1) market pin `BTCUSDT` on Binance futures with the source-native daily frame kept (the source is symbol-agnostic; venue transfer plus symbol spelling and futures short permission disclosed here, never presented as source-native); (2) `reverse=false` pinned (the shipped `reverse` toggle set to its default; `reverse=true` is a different, unpinned rule — see Negative evidence); (3) same-bar-close fills on completed `1d` bars (the source ships no `process_orders_on_close`, i.e. Pine default next-bar-open timing — this derivation is predeclared here, never presented as source timing); (4) an adopted 50-bar warmup with pre-warmup bars flat by record rule (source seeds are deterministic from bar one — see Signal — the warmup fences seed dominance, predeclared researcher choice); (5) house sizing/capital/costs replacing the absent source economics (zero commission/quantity assumption — recorded as absent economics, never as zero-cost evidence; see Execution assumptions). The `close`-only price read, the `Length=20` momentum lag, the Wilder-style accumulation pair, the `100 x RM/(1+RM)` ratio, the `40`/`70` band pair, the latch-and-hold neutral zone, the two-sided `Long`/`Short` order pair, and the no-stop/no-target/no-flat-after-first-signal stance are source-pinned or predeclared above and unmodified elsewhere.

Pre-write dedup (2026-10-15): working-tree case-insensitive fixed-string searches for `Relative Momentum`, word-boundary `RMI`, and `Altman` return zero strategy records using this source, author strategy, or construction. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. The three closed October-15 Scout PRs (#222 Blau DTI band-latch, #223 DPO zero-sign latch, #224 Bufi adaptive-threshold RSI time-exit) carry unrelated arithmetic. Closest pool records are different mechanism classes: every `rsi-*` record (including `rsi-classic-level-reversal`, `cumulative-rsi-dual-threshold`, `connors-rsi2-ma70-fade`, `drm-dynamic-rsi-momentum`, `laguerre-rsi-cu-cd-cross`) accumulates one-bar close-to-close changes and never reads a multi-bar momentum lag; `chande-momentum-80-cross` trades the raw unbounded difference `close - close[n]` with no Wilder smoothing and no ratio; `qstick-zero-cross-trend` averages raw signed bodies with no ratio and no fixed band; `vzo-tactic1` normalizes signed volume through an EMA pair against fixed `+-40` bands with no price-momentum read. No pool record computes a Wilder-smoothed ratio of `Length`-lagged momentum against a `40`/`70` latch band. Shared `RSI` wording or shared `close` inputs are not shared signal.

## Economic mechanism

### Source-reported

Momentum-persistence capture with band-latch reversal discipline (description block, corroborated by the code): instead of counting up/down days close-to-close as the RSI does, the print counts them from each close relative to the close `Length` days ago, then smooths the up/down legs the Wilder way and scales their share to `0-100`. Reading below `40` means lagged-momentum selling pressure has exhausted enough to accept the long side; reading above `70` means lagged-momentum buying pressure has stretched enough to accept the short side. Between the bands the prior stance simply holds — the neutral zone is a latch, not a signal. The design bets that multi-bar momentum persistence leads the next leg: unlike one-bar RSI, single-bar noise cannot touch any order-gating line unless it survives the `Length`-bar differencing and the Wilder accumulation. There is no stop, no target, no flat state by record design after the first signal — the opposite band print is the exit.

### Research interpretation

Single-series bounded-oscillator system, two-sided, always-in-position after the first signal, with an asymmetric hysteresis band as the only trigger. Unlike cumulative systems (OBV, PVT) whose totals drift without bounds and need a second series to cross, this rule normalizes participation into a fixed `0-100` scale so two constant levels (`40`/`70`) suffice forever — no moving reference, no re-fit, no second line. Unlike midline flippers, the trigger pair is deliberately asymmetric (`40` long leg, `70` short leg), so long entries demand deeper exhaustion than short entries — every holding period is exactly one band-to-opposite-band migration with a wide neutral latch between them. Unlike the pool's close-to-close RSI records, the differencing lag is `20` bars rather than `1`: the print moves only on momentum that persists across the full lag window, making it structurally slower and smoother than any same-length RSI at the cost of later entries. Unlike Chande's raw momentum oscillator, the Wilder ratio makes the print unit-free and comparable across volatility regimes. The price of the always-in posture is indefinite adverse rides plus whipsaw pairs when the print straddles a band edge: a leg whose opposite band never prints is held forever. The bet is on lagged-momentum persistence, not on any price pattern, second series, volume read, calendar effect, or volatility read.

## Signal

Exact rule as pinned (all inputs frozen — any other value is a different, unpinned rule):

- Declarations (derived): single-position state machine over `BTCUSDT 1d` with same-bar-close execution and house sizing/costs (see Execution assumptions). At most one open leg; state ∈ {flat, long, short}; flat exists only before the first signal and under the warmup rule. `reverse=false` pinned (source default).
- Price read, pinned verbatim: `xPrice = close` of completed bars only; momentum `xMom(t) = C(t) - C(t-20)` with `Length = 20`.
- Accumulation legs, pinned verbatim (Wilder-style with deterministic seeds): `xMU(t) = xMU(t-1) - xMU(t-1)/20 + xMom(t)` when `xMom(t) >= 0`, else `xMU(t-1)` (seed `nz(xMU[1], 1)`); `xMD(t) = xMD(t-1) - xMD(t-1)/20 + abs(xMom(t))` when `xMom(t) <= 0`, else `xMD(t-1)` (seed `nz(xMD[1], 1)` on the updating branch, `nz(xMD[1], 0)` on the holding branch). A zero-momentum bar (`xMom(t) == 0`) satisfies both update branches and decays both legs by `1/20` with `+0` — deterministic, no tie-break needed or invented.
- Indicator, pinned verbatim: `RM(t) = xMU(t) / xMD(t)`; `nRes(t) = 100 x RM(t) / (1 + RM(t))`. A zero-denominator bar (`xMD(t) == 0`, reachable only before any down-momentum has ever printed) yields `na`, which fails both strict band comparisons and holds the prior state by the latch below — deterministic hold, fenced in Negative evidence.
- Entry long: on bar `t` with `nRes(t) < 40` (BuyZone strictly undershot; from flat: open long; from short: atomic reversal — close short plus open long as a single reversal event). Refires of the long state while already long are no-ops (no pyramiding — Pine default with two opposing `strategy.entry` legs, explicitly none, not invented).
- Entry short: mirror on bar `t` with `nRes(t) > 70` (SellZone strictly overshot).
- Latch: when `40 <= nRes(t) <= 70` (or `nRes(t)` is `na`), `pos` holds `pos(t-1)` (`nz(pos[1], 0)` seeds flat before the first band print) — the neutral zone never issues an order by construction.
- Exits: the opposite band print only (long exits exactly when the short trigger prints and vice versa). No stop, no target, no trailing, no time exit, no cooldown — explicitly none by record rule, not invented, consistent with the band pair forming a complete always-in machine. There is no flat path after the first signal at all — flat is reachable only pre-signal and under warmup.
- Direction: two-sided with an explicit pre-first-signal flat state (plus the 50-bar warmup flat by record rule). The shipped `Long`/`Short` order pair prescribes both legs; a long-only or short-only reading would contradict it.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (momentum leg reads `C(t)` and `C(t-20)`) — Binance USDT-M futures by record pin (see Limitations). No `open`, no `high`, no `low`, no volume, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (frame-faithful to the daily construction; the rule references no other frame, no multi-timeframe input, no `security`-style call of any kind — single-frame by construction).
- Warmup: the binding cost is the `20`-bar momentum reach plus Wilder-accumulation settle from deterministic seeds. The adopted warmup is the first 50 completed `1d` bars flat by record rule (predeclared researcher choice — covers the full lag window plus accumulation settle with wide margin; no seed branch is hidden). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Each bar's close enters the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (frame-faithful `1d`; venue choice, symbol spelling, and short permission disclosed in Provenance, never presented as source claims).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity, and each trigger reads only completed closes, so each bar's outcome is a single deterministic event (hold, open, or atomic reversal).
- Sizing/capital/costs: the source ships no portable economics (zero commission/quantity assumption — recorded as absent economics, never as zero-cost evidence) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior. Funding is modeled, never reported as realized or canonical funding.
- Concurrency: single-position machine — at most one open leg; same-state bars while positioned are no-ops; the opposite band print reverses in full (one atomic event); re-entry is allowed on the next fresh band print after any close (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (momentum `xPrice - xPrice[Length]` with `Length = 20`; the Wilder-style `xMU`/`xMD` accumulation pair with `nz` seeds; `RM = xMU / xMD`; `nRes = 100 x (RM / (1+RM))`), the band pair (`BuyZone = 40`, `SellZone = 70`), the latch-and-hold neutral semantics (`pos` holding `pos[1]` between bands), the `reverse` toggle default (`false`), the two-sided `Long`/`Short` order pair, and the Altman attribution — quoted in Provenance. The source ships no backtest table, so this record carries zero source-reported performance numbers and claims no performance of any kind.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No performance to carry, admitted plainly: unlike paper-sourced records with backtest tables, the HPotter publication ships construction, bands, and order semantics only — there is no expectancy number anywhere to fence, and this record claims none.
2. `reverse=true` fenced, admitted plainly: the shipped toggle would mirror both legs (long above `70`, short below `40`); it is a real source control deliberately not carried into the traded rule. The pinned `reverse=false` reading is therefore signal-complete by record rule, and carrying the mirrored posture onto it would be fabrication.
3. No hidden exits or risk layer: the traded machine names no stop, no target, no trailing, no time exit anywhere — the no-stop/no-target posture is the record rule, explicitly none, never hidden. Every adverse excursion is held to the opposite band print.
4. Trigger exclusivity fenced: the long trigger requires `nRes(t) < 40` and the short trigger requires `nRes(t) > 70` — no print satisfies both, so no bar fires both transitions and no priority rule is needed or invented.
5. Exact-touch determinism fenced: landings exactly on `40` or `70` satisfy neither strict comparison, so the latch holds the prior state deterministically (measure-zero on continuous prints — disclosed, not oversold as tolerance). The `na` print (zero denominator only) likewise holds the prior state deterministically.
6. Seed determinism fenced: every recursive leg carries its `nz` seed in the pinned code (`xMU` seeds `1`, `xMD` seeds `1`/`0`, `pos` seeds `0`), so the first bars evaluate to flat-hold rather than undefined — and the adopted 50-bar warmup fences seed dominance on top, predeclared.
7. Zero-momentum determinism fenced: `xMom(t) == 0` satisfies both `>= 0` and `<= 0` update branches, decaying both legs by `1/20` with `+0` — one deterministic outcome, no branch ambiguity, no tie-break invented.
8. No future leakage in the stack, stated plainly: at decision bar `t`, momentum reaches back to completed bar `t-20`, both legs accumulate only values available at each bar's close, and the latch compares only print `t` against fixed bands — every input is complete at bar `t`'s close. No multi-frame read, no negative index, no full-sample normalization, no repainting path, no calendar read at all. The source sets no intrabar evaluation flag, and the derived rule evaluates once per completed bar.
9. RSI/CMO/Laguerre/DRM-family overlap fence, admitted plainly: the pool's close-to-close RSI records difference with lag `1`; `chande-momentum-80-cross` differences with lag `n` but never Wilder-smooths and never ratios; `laguerre-rsi-cu-cd-cross` gamma-filters one-bar gains/losses; `drm-dynamic-rsi-momentum` adapts the RSI length, never the momentum lag. This record differences with lag `20` AND Wilder-accumulates AND ratios against a fixed `40`/`70` latch band with no volume, no gamma filter, and no second series. Shared `RSI` wording or shared `close` inputs are not shared signal.
10. Two-sided posture provably complete: asymmetric `40`-dip long / `70`-stretch short legs with symmetric atomic-reversal exits under the shipped `Long`/`Short` order pair — no third direction exists, and a long-only reading would contradict the printed short leg.
11. Derivation boundary fenced: the only non-source-native behaviors in this record are the `BTCUSDT` futures market pin with the source-native daily frame kept, the `reverse=false` pin, same-bar-close fills, the adopted 50-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the `close`-only read, the `20`-bar momentum lag, the Wilder accumulation pair with seeds, the ratio formula, the `40`/`70` band pair, the latch, the atomic reversal, the single-position guards, and the risk posture are source-pinned or predeclared. This record is therefore never evidence that any other market, frame, length, band set, `reverse` setting, or timing of the source passes.
12. Publication identity disclosed: the formula, legs, bands, latch, toggle default, and order pair above were read in the browser-rendered open-source Pine (42 lines, `//@version=2`, `HPotter v1.0 19/10/2017`) and cross-checked against the 930248-byte static fetch of the same canonical URL (same badge, author, and description). The division of evidence is disclosed here, not hidden.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `close`-only read / `20`-bar momentum lag / Wilder accumulation with pinned seeds / `100 x RM/(1+RM)` ratio with `na`-hold / `40`-dip long with `70`-stretch short latch band / atomic reversal / no-stop-no-target posture / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Band relevance: replacing the asymmetric `40`/`70` latch band with a symmetric `30`/`70` RSI-style band pair (same lag, same accumulation, same state machine, same reversal handling) must not improve net expectancy; fail ⇒ the `40` dip leg adds nothing over the conventional oversold level.
- F2 — Lag relevance: shortening the momentum lag to `1` bar (the RSI-form restriction of the same `Length = 20` accumulation, same bands, same state machine) must not improve net expectancy; fail ⇒ the `20`-bar differencing adds nothing over one-bar RSI accumulation.
- F3 — Posture relevance: exiting to flat on the opposite band print instead of atomic reversal (same entries, same bands, flat between migrations) must not improve net expectancy; fail ⇒ the always-in alternation adds nothing over a flat-resting variant.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (frame-faithful `1d`; venue transfer disclosed). The rule reads only completed daily closes, so no high/low definition differences and no volume-series differences can touch any order-gating line — but spot-vs-perp close prints can still differ structurally (funding-driven drift, venue aggregation, anomalous prints), so the futures-venue pin is load-bearing and disclosed. The ratio is unit-free and the bands are fixed constants, so no fixed-pip recalibration is needed across assets — cross-asset behavior differences are still real and unclaimed. The rule is two-sided with no stop leg, so a spot-only deployment expresses the long state and reversal mechanics only to the extent the venue permits shorting — full two-sided expression assumes a futures venue, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read beyond each calendar-day bar's own close (no session gating anywhere); decision boundaries are calendar-day bars of the venue feed, disclosed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived market pin: the source is symbol-agnostic; this record pins `BTCUSDT` futures `1d`. Cross-market and spot-vs-perp close behavior differences are real — the venue transfer is disclosed, and this record makes no claim about any other market or the source's native venue.
- Untested trigger scope: the only source-documented trigger carried here is the `40`/`70` latch-band pair under `reverse=false`; the mirrored `reverse=true` posture is real source content deliberately not traded, and the pinned pair itself carries no expectancy claim until downstream research measures it.
- No source economics: the source ships no commission, sizing, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- No price stop, no time stop: adverse excursion after entry has no guardrail beyond the opposite band print; a leg whose opposite trigger never prints is held indefinitely. This is the record-rule posture, disclosed as a principal risk.
- Whipsaw sensitivity: band-edge straddles print repeated reversal pairs with no flat state to rest in, by the prescribed always-in design. The asymmetric band construction is the documented trigger, disclosed, not smoothed.
- Close-print sensitivity: venue close prints (rolls, aggregation, anomalous prints) flow straight into the momentum leg twice (at `t` and `t-20`); a venue that cannot supply trustworthy per-bar closes cannot trade the pinned rule.
- Warmup cost: the momentum reach needs 20 completed bars plus accumulation settle; the adopted 50-bar warmup absorbs this structurally with wide margin, and the first 50 bars are flat by record rule.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- TradingView HPotter open-source strategy, Relative Momentum Index Backtest — full 42-line `//@version=2` rule, band pair, latch, toggle default, order pair, Altman attribution (rendered live in the browser during this cycle; zero crypto claims): https://www.tradingview.com/script/gYZ1PPNy-Relative-Momentum-Index-Backtest/
