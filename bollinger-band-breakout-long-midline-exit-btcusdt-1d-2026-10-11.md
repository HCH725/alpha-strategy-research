---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Bollinger Band breakout long with midline exit on BTCUSDT 1d bars
created: 2026-10-11
updated: 2026-10-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-09-11
sources:
  - https://www.fmz.com/strategy/426339
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/Bollinger-Band-Breakout-strategy.md
  - https://www.tradingview.com/pine-script-reference/v4/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bollinger Band breakout long with midline exit on BTCUSDT 1d bars

## Provenance

Primary source read end to end (immutable public mirror file plus its recorded FMZ canonical page, fetched 2026-10-11):

- Canonical page: https://www.fmz.com/strategy/426339 (fetched live over HTTPS during this cycle with HTTP 200, 735541 bytes of landing HTML). Author token `ChaoZhang` × 2; page embeds the executable `/*backtest*/` header verbatim: `start: 2022-09-04 00:00:00`, `end: 2023-09-10 23:59:00`, `period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]` (each of `Futures_Binance`, `BTC_USDT` byte-present twice on the page). The ZH/EN prose states the rule twice: the middle band is the n-period moving average with upper/lower bands at ±m standard deviations (typical 20 periods and 1.5×), a break above the upper band means a strong uptrend and goes long, a break below the lower band means a strong downtrend — and admits plainly that the strategy ships with no stop-loss setting (`没有止损设置` / `lack of stop loss`). Word-boundary counts over the whole landing HTML: `Bollinger` 27, `Breakout` 7, `Sharpe` 0, `Win Rate` 0, `Max Drawdown` 0, `Annualized` 0, `Profit Factor` 0 — the sole `return` token is site-chrome JavaScript (`window.__cdn`), not a performance figure. The page ships no performance numbers of any kind.
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (verified as the repository head via `git ls-remote` during this cycle — the same head pin as the merged PVT-EMA, KDJ, STARC, T3-Tillson, WaveTrend, Qstick, Aroon, SQZMOM-LB, TRIX, Schaff, KST, OBV-EMA and eleven further admissions), exact file path `Bollinger-Band-Breakout-strategy.md` (pure-ASCII filename, no encoding ambiguity). File 4321 bytes, blob SHA `d1526bb044f3a2cb5e8c5a71df80b7062ca5598a` (verified with `git hash-object` reproducing the identical SHA on re-download, and matching the GitHub contents API `sha`/`size` at the pinned commit). The mirror prints `> Author` = `ChaoZhang` (mirror porter), `> Detail` = https://www.fmz.com/strategy/426339, `> Last Modified` = `2023-09-11 14:33:57` (date part adopted as `source_as_of`), the `[trans]` ZH/EN prose matching the canonical page rule quoted above, and the two-row Strategy Arguments table (`Period = 20`, `Standard Deviation = 1.5`) matching the code defaults exactly.
- Full `//@version=4` block read in full (order-affecting lines: the `source`/`length`/`mult` declarations, the `basis`/`dev`/`upper`/`lower` lines, the long-entry `if`, the long-close `if`; everything else is declaration plumbing or display-only plots/fill).
- Text census over the pinned code block: 1 `strategy(` (title/shorttitle/`overlay=true` plumbing plus `default_qty_type = strategy.percent_of_equity` / `default_qty_value = 100` capital configuration only — no capital amount, cost, timing, or pyramiding argument ships anywhere in the declaration) / 1 `strategy.entry` (`"Long"`/`strategy.long`, no `qty=`/`limit=`/`stop=`/`when=` qualifiers) / 1 `strategy.close` (`"Long"`, no `when=` qualifier) / 0 `strategy.exit` / 0 `strategy.order` / 0 `strategy.short` (no short leg anywhere — long-only by construction) / 0 active `stop=`/`limit=` / 1 `crossover` + 1 `crossunder` (the entry/exit edge pair, nothing else) / 1 `sma(` + 1 `stdev` (the full indicator stack) / 1 `close` (the `source = close` line; `high`/`low`/`open`/`volume` 0 as bare series — the two `low` substring hits are the `lower` band identifier, never a series read) / 2 `input(` (`Period = 20`, `Standard Deviation = 1.5`, the sole parameters) / 3 `plot` (`basis`, `p1` upper, `p2` lower) + 1 `fill` (display-only band shading) / 0 `security(` / 0 `request.*` / 0 `timeframe(` / 0 `ta.` (v4 built-ins used unprefixed) / 0 `nz(` / 0 `var` / 0 `pyramiding` / 0 `process_orders_on_close` / 0 `initial_capital` / 0 `commission` / 0 `calc_on_every_tick`. The `lower` band is computed and plotted but read by no order condition — counted in census, excluded from the rule, disclosed. No portable economics beyond the bare percent-of-equity stub ships anywhere — recorded as an absent-economics stub, never as zero-cost evidence.
- Licence and rights: the mirror block ships no licence header line; this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) market/frame pin `BTCUSDT 1d` (the executable `/*backtest*/` stanza itself backtests `Futures_Binance BTC_USDT` at `period: 1d` — this pin follows the stanza decision frame verbatim; the `1h` basePeriod is the stanza's sub-bar granularity, not a second decision frame, and only the symbol spelling is normalized, disclosed here, never presented as source-native); (2) completed-bar decisions with same-bar-close fills (the source ships no execution-timing argument — Pine default evaluates per completed bar and fills on the next bar; no `process_orders_on_close` ships anywhere, quoted verbatim in census — this record pins completed-bar evaluation with same-bar-close fills and claims no next-bar timing, disclosed here); (3) an adopted 100-bar warmup with pre-warmup bars flat by record rule (covers the SMA20/stdev20 seed with margin — see Required data); (4) house sizing/capital/costs replacing the absent source economics (see Execution assumptions). The `source = close` line, the `20`/`1.5` inputs, the `basis = sma` / `dev = mult * stdev` construction, the `crossover(source, upper)` entry edge, the `crossunder(source, basis)` exit edge, the `"Long"` order path, the long-only stance, and the no-stop/no-target posture are source-native and unmodified. No tie-break had to be invented: the two edges are provably mutually exclusive on every bar including the degenerate flat print (see Negative evidence), and each bar's outcome is a single deterministic event.

Pre-write dedup (2026-10-11): working-tree case-insensitive filename search for `bollinger` returns only `sideways-dmi-bollinger-breakout-long-btcusdt-4h-2026-10-07.md` and `waddah-attar-explosion-macd-bb-deadzone-two-sided-btcusdt-1d-2026-10-11.md` — no pure-Bollinger record exists anywhere. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool record `sideways-dmi-bollinger-breakout-long` is a different mechanism on four axes: (i) gate — it requires a DMI sideways-spread gate (`abs(pos_dm − neg_dm) < 20` on a 14/14 DMI) while this record has no gate of any kind; (ii) entry edge — it enters long on `crossover(close, lower)` (lower-band dip reclaim) while this record enters on `crossover(close, upper)` (upper-band breakout, the opposite side of the band); (iii) exit edge — it exits on `crossunder(close, upper)` while this record exits on `crossunder(close, basis)` (midline reclaim); (iv) parameters and frame — 2.0σ/4h-derived versus 1.5σ/stanza-native-1d from FMZ 426339 (Sep-2023). The Waddah record is a MACD-plus-BB-deadzone two-sided explosion system, and the Keltner/STARC/SQZMOM records use ATR/range bands, never a close-SMA ± stdev band. Not a trivial parameter variant.

## Economic mechanism

### Source-reported

Volatility-normalized breakout capture (mirror prose plus code): the 20-bar SMA is the slow consensus price and 1.5× the 20-bar standard deviation is the market's own recent dispersion ruler — the upper band is where price has stretched unusually far above consensus relative to what that exact window considers normal. A close crossing above that ruler means buyers just paid a statistically stretched price and held it into the close, which the design reads as strong-trend ignition rather than exhaustion; the position then rides until price sinks back through the consensus line itself (the midline crossunder), i.e. the stretch has fully decayed. The prose bets this fits visibly trending markets and warns the bands lag, breakouts can fail, and no stop ships with the design — the midline reclaim is the sole risk control.

### Research interpretation

Single-unit breakout-and-decay machine, edge-triggered, long-only, flat-capable. Unlike the sideways-DMI record there is no regime gate to hide behind: every upper-band cross while flat opens, chop prints alternating open-and-midline-close round trips, which is the coded cost of the design, disclosed, not smoothed. Unlike oscillator-cross systems (KDJ, Stochastic-OTT, KST, Schaff) the trigger is asset-scaled — the band auto-widens in volatile regimes so the same 1.5σ rule demands a larger absolute stretch when dispersion is high, a self-normalizing property fixed-threshold oscillators lack. Unlike stop-carrying records there is no protective leg beyond the midline exit: adverse excursion from entry back through the midline is the exit, and a gap-through-midline close exits at the same-bar close in this record's derived timing. The bet is on stretched-close persistence at the ~month scale under a 20-bar consensus leg, not on any price level, second indicator, slope test, calendar effect, or second timeframe.

## Signal

Exact rule as pinned (`length = 20` frozen, `mult = 1.5` frozen, `source = close` frozen — any other value is a different, unpinned rule):

- Declarations (derived): single-unit long/flat machine over `BTCUSDT 1d` with same-bar-close execution and house sizing/costs (see Execution assumptions). State ∈ {flat, long}; short is unreachable by code (zero `strategy.short` legs anywhere).
- Band block, pinned verbatim: `basis[t] = sma(close, 20)[t]`; `dev[t] = 1.5 × stdev(close, 20)[t]` (Pine v4 population `stdev`); `upper[t] = basis[t] + dev[t]`; `lower[t] = basis[t] − dev[t]` (computed and plotted only — read by no order condition, disclosed).
- Entry long, pinned verbatim: `crossover(source, upper)(t)` — `close[t-1] ≤ upper[t-1]` and `close[t] > upper[t]` — fires `strategy.entry("Long", strategy.long)`; from long (no pyramiding ships anywhere) no additive exposure can print; from flat it opens. A touch without penetration fires nothing.
- Exit long, pinned verbatim: `crossunder(source, basis)(t)` — `close[t-1] ≥ basis[t-1]` and `close[t] < basis[t]` — fires `strategy.close("Long")`, closing the full unit (the sole entry id — nothing partial, nothing left behind). After the exit the next bar satisfying the entry edge re-enters immediately (no cooldown specified — explicitly none, not invented).
- Exits and risk, pinned verbatim: there are none besides the midline cross — zero `strategy.exit` legs, zero `stop=`/`limit=` qualifiers, and the prose independently admits no stop-loss setting. No take-profit, no trailing, no time exit, no opposite-side exit (no short side exists) — pinned as written, explicitly none, not invented.
- Direction: long-only with resting flat. A two-sided or short reading would contradict the zero-`strategy.short` census and is explicitly not this record.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (band construction, entry edge, and exit edge — the sole series read by any order-gating line). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read anywhere.
- Single decision timeframe `1d` (derived pin following the stanza's own `period: 1d`; the `1h` basePeriod is sub-bar execution granularity in the FMZ stanza, not a second evaluated frame — the body contains no `security(`/`request.*` call, so the derived rule is single-frame by construction).
- Warmup: the binding seed is the SMA20/stdev20 seed (20 completed bars; both resolve `na` before, and `na` comparisons are false so no edge can fire pre-seeding — coded behavior, disclosed). The adopted warmup is the first 100 completed `1d` bars flat by record rule (predeclared researcher choice — 5× the slow length with margin; no traded bar reads a seeded value). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (derived pin following the executable header's own `Futures_Binance BTC_USDT` venue at `period: 1d` — venue transfer and symbol spelling are disclosed here, never presented as source-native). Long-only, so a spot deployment expresses the full rule unchanged (no short permission is ever needed) — disclosed.
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar fill (no execution-timing argument ships anywhere — quoted verbatim in census); this record claims neither the source fill timing nor any intrabar behavior. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity, and the two edges are mutually exclusive per bar (see Negative evidence), so each bar resolves to at most one order event.
- Sizing/capital/costs: the source ships no portable economics beyond the bare `default_qty_type = strategy.percent_of_equity` / `default_qty_value = 100` stub (no capital amount, no commission/slippage/funding/margin argument ships anywhere — recorded as an absent-economics stub, never as zero-cost evidence) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: single-unit machine by default no-pyramiding construction — at most one long unit; a second upper-band cross while long prints nothing. Exit is to flat on the next midline crossunder (no cooldown specified — explicitly none, not invented). No flat state is reachable except pre-first-entry and post-exit; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The mirror ships the full construction (the `source = close` line, the `20`/`1.5` inputs, the `sma`/`stdev` band block, the `crossover(source, upper)` entry, the `crossunder(source, basis)` exit, the `"Long"` entry/close pair, the three plots plus band fill, and the 2022-09-04→2023-09-10 `1d`/`1h` Binance backtest header), the author/title stamps, the two-row arguments table, and the bilingual rule prose with its explicit no-stop-loss admission. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden risk layer: the body contains zero `strategy.exit` legs and zero `stop=`/`limit=` qualifiers, and the prose independently admits no stop-loss setting. The no-stop/no-target posture is prescribed, explicitly none, never hidden.
2. Mutual-exclusion proof, stated plainly: entry requires `close[t] > upper[t]`; exit requires `close[t] < basis[t]`; and `upper[t] − basis[t] = dev[t] = 1.5 × stdev ≥ 0` always. Both true would require `close[t]` strictly above `upper[t]` and strictly below `basis[t]` with `upper[t] ≥ basis[t]` — impossible on every bar. Degenerate flat print fenced: if all 20 closes are identical, `dev = 0`, `upper = basis = close[t]`, and both strict inequalities fail — neither edge fires. No researcher precedence was invented: the shipped entry-`if`-before-exit-`if` order never arbitrates a real tie.
3. Edge-not-latch fenced: both conditions are `crossover`/`crossunder` (fire only on the cross bar), not a `close > upper` holding state — post-entry bars with price still above the band satisfy no entry guard, so no bar can open twice and no priority rule against the exit is needed.
4. na determinism fenced: before the SMA20/stdev20 seed both edges resolve false by Pine `na` comparison semantics; the adopted 100-bar flat absorbs the seed structurally. No seeded or `na` value ever trades — structural, disclosed, never a researcher tie-break.
5. `lower`-band fenced: `lower` is computed and plotted but read by no order condition — a reader mistaking it for a short trigger or a second exit would contradict the census (0 `strategy.short`, 1 `strategy.close` bound to the basis cross only). Disclosed, not hidden.
6. Single-id close completeness fenced: the sole entry id is `"Long"` and the sole close targets `"Long"` — with no pyramiding anywhere there is at most one unit to close, so `strategy.close("Long")` provably flattens the book. No partial-fill residue is reachable by code.
7. No future leakage in the stack, stated plainly: at decision bar `t` the slowest inputs are the SMA20/stdev20 values resolving at bar `t`'s close — every input is complete at the close. No `security()`, no `request.*`, no negative index, no offset input applied to any band, no `barstate`-gated order path. All three `plot` calls and the `fill` are display-only and drive no order.
8. Long-only posture provably complete: the code paths admit only flat→long opens and long→flat closes under default no-pyramiding — no short state is reachable by code. Any short-side reading would contradict the zero-`strategy.short` census and is explicitly not this record.
9. Derivation boundary fenced: the only non-source-native behaviors in this record are the `BTCUSDT 1d` market/frame pin, completed-bar same-bar-close fills, the adopted 100-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the `source = close` line, the `20`/`1.5` inputs, the SMA ± stdev band construction, the strict upper-breakout entry edge, the strict midline exit edge, the `"Long"`-id order path, single-unit no-pyramiding state, long-only direction, and the risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, mult, length, or timing of the source passes.
10. Network limitation disclosed: every formula line above was byte-verified in the pinned mirror file at commit `7853bb2` (4321 bytes, blob SHA recorded, `git hash-object` identical on re-download, contents-API `sha`/`size` matched); the FMZ canonical page verified live the title, the `ChaoZhang` token, the breakout/midline rule prose with its no-stop-loss admission, the `Futures_Binance BTC_USDT` `1d` backtest stanza, and the absence of any performance numbers — the division of evidence is disclosed here, not hidden.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `source = close` / SMA 20 / 1.5σ / strict `crossover(source, upper)` entry / strict `crossunder(source, basis)` exit / no-stop-no-target posture / long-only single-unit / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Band-weight relevance: replacing the 1.5σ upper-band entry with a plain SMA20 `crossover(close, basis)` entry (same midline exit, same risk posture) must not improve net expectancy; fail ⇒ the dispersion-normalized stretch adds nothing over a consensus-line cross.
- F2 — Multiplier relevance: replacing the 1.5σ band with a 2.0σ band (same 20 length, same edges, same risk posture) must not improve net expectancy; fail ⇒ the pinned tighter trigger adds nothing over the textbook-wide band.
- F3 — Exit relevance: replacing the midline exit with an opposite-band exit (`crossunder(close, lower)`-to-flat, a different, separately specified posture) must not improve net expectancy; fail ⇒ the quick decay-capture adds nothing over holding for the full round trip.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (derived pin following the executable header's own `Futures_Binance BTC_USDT` venue at `period: 1d`). The band arithmetic ports across perpetual venues without structural change — no volume read means venue volume-reporting differences touch nothing, disclosed as a robustness property, not a portability proof. The 1.5σ rule auto-scales in the asset's own dispersion units, so no fixed-pip recalibration is needed across assets — cross-asset behavior differences are still real and unclaimed. Long-only, so spot deployment expresses the full rule with no venue-gated short half — disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no session gating anywhere); decision boundaries are calendar-day bars of the venue feed, disclosed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source fills next-bar with no timing argument; this record executes completed-bar same-bar-close on `1d` BTCUSDT and claims no next-bar timing. Backtest economics of the timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- Derived market and frame: the stanza backtests `Futures_Binance BTC_USDT` at `period: 1d` (`1h` basePeriod is sub-bar granularity, not a second decision frame); this record pins `BTCUSDT 1d` with normalized symbol spelling. Cross-market and cross-frame behavior differences are real — the adaptation is disclosed, and this record makes no claim about any other market, frame, or base period.
- Midline-only risk control: the sole exit is the consensus-line reclaim — adverse excursion has no stop beyond the next midline crossunder, chop prints alternating full round trips, and the prose itself warns bands lag and breakouts fail. This is the prescribed posture (prose-admitted, zero coded exits), disclosed as the principal risk — not smoothed, not supplemented.
- No source economics: beyond the bare percent-of-equity stub the source ships no capital amount, commission, slippage, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Seed coverage: the SMA20/stdev20 seed settles within dozens of bars; the first 100 `1d` bars are flat by record rule, so early-history signals never enter any evaluation.
- Flat-market silence: twenty identical closes pin `dev = 0` and both strict edges fail — the machine holds its state through zero-dispersion prints rather than forcing a signal. Disclosed, not modeled further.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- FMZ canonical strategy page (breakout/midline rule prose with no-stop-loss admission plus `Futures_Binance BTC_USDT` 1d backtest stanza verified live via HTTP-200 page record): https://www.fmz.com/strategy/426339
- Immutable mirror file at pinned commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (blob `d1526bb044f3a2cb5e8c5a71df80b7062ca5598a`, 4321 bytes): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/Bollinger-Band-Breakout-strategy.md
- Pine strategy semantics (v4 order calls, default execution, unprefixed `sma`/`stdev`/`crossover`/`crossunder` built-ins): https://www.tradingview.com/pine-script-reference/v4/
