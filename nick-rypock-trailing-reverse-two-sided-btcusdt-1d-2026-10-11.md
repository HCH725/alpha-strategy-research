---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Nick Rypock Trailing Reverse percentage-channel flip two-sided on BTCUSDT 1d bars
created: 2026-10-11
updated: 2026-10-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2022-05-25
sources:
  - https://www.fmz.com/strategy/365713
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/Nick-Rypock-Trailing-Reverse-NRTR.md
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Nick Rypock Trailing Reverse percentage-channel flip two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (immutable public mirror file plus its recorded FMZ canonical page, fetched 2026-10-11):

- Canonical page: https://www.fmz.com/strategy/365713 (fetched live over HTTPS during this cycle with HTTP 200, 705917 bytes of landing HTML). Author token `ChaoZhang` × 2; prose names the indicator's 2001 inventor Konstantin Kopyrkin ("Nick Rypock" as the reversed reading), describes the idea as Chandelier-Exit-like but with a percentage distance instead of any ATR component, and states the channel uses only prices inside the current trend, excluding extremes of the previous trend (`Nick Rypock` 15, `NRTR` 19, `Kopyrkin` 14 on the page). Word-boundary counts over the whole landing HTML: `Sharpe` 0, `Win Rate` 0, `Max Drawdown` 0, `Annualized` 0, `Profit Factor` 0, `Take profit` 0, `Stop Loss` 0 — the sole `return` token is site-chrome JavaScript (`window.__cdn=function(p){var b="";return b?...}`), not a performance figure. The page ships no performance numbers of any kind.
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (verified as the repository head via `git ls-remote` during this cycle — the same head pin as the merged Chande-Kroll, Heikin-Ashi, Bollinger, PVT-EMA, KDJ, STARC, T3-Tillson, WaveTrend, Qstick, Aroon, SQZMOM-LB, TRIX, Schaff, KST, OBV-EMA and further admissions), exact file path `Nick-Rypock-Trailing-Reverse-NRTR.md` (pure-ASCII filename, no encoding ambiguity). File 4120 bytes, blob SHA `22b1b47d64c39c6983e39f0a0c3dbf0a07edd6f6` (verified with `git hash-object` reproducing the identical SHA on re-download, and matching the GitHub contents API `sha`/`size` at the pinned commit). The mirror prints `> Name` = `Nick-Rypock-Trailing-Reverse-NRTR`, `> Author` = `ChaoZhang`, `> Detail` = https://www.fmz.com/strategy/365713, `> Last Modified` = `2022-05-25 18:14:32` (date part adopted as `source_as_of`), the three-row Strategy Arguments table (`v_input_1` = 2 Correction %, `v_input_2`/`v_input_3` = true label/ribbon toggles) matching the code defaults line for line, the English inventor/method prose quoted above, one backtest screenshot image (performance content unread — no numbers transcribed, never a source fact here), and the FMZ backtest stanza (`start: 2022-04-24`, `end: 2022-05-23`, `period: 2h`, `basePeriod: 15m`, `Futures_Binance BTC_USDT`).
- Full `//@version=4` block read in full (order-affecting lines: the `k`/`percentage` declarations, the `var trend`/`hp`/`lp`/`nrtr` state block, the two trend-branch update legs, and the `if buySignal … else if sellSignal` order pair; the six `plot`/`plotshape`/`fill` calls, the three `alertcondition` calls, and the `showLabels`/`applyRibbon` inputs are visual/alert-only and gate no order).
- Text census over the pinned code block: 0 `strategy(` (the header declares `study("Nick Rypock Trailing Reverse", shorttitle="NRTR", overlay=true)` — the porter artifact fenced below) / 1 `study(` / 0 `indicator(` / 2 `strategy.entry` (`"Enter Long"`/`strategy.long`, `"Enter Short"`/`strategy.short`, no `qty=`/`limit=`/`stop=`/`when=` qualifiers) / 0 `strategy.exit` / 0 `strategy.order` / 0 `strategy.close` / 0 active `stop=`/`limit=`/`profit=`/`loss=` / 0 `ta.crossover` / 0 `ta.crossunder` (flips are computed by explicit `trend`/`trend[1]` equality tests, pinned as written) / 2 `plot(` + 4 `plotshape(` + 2 `fill(` (all visual only) / 3 `alertcondition(` (alerts only, no orders) / 0 `ta.highest` / 0 `ta.lowest` / 0 `ta.atr` / 0 `ta.rma` / 0 `request.security` / 3 `input` (float `k = 2`, bool `showLabels = true`, bool `applyRibbon = true`; only `k` is order-affecting) / 0 `pyramiding` / 0 `process_orders_on_close` / 0 `initial_capital` / 0 `commission` / 0 `na(` / 0 `nz(` / 0 `barstate` / 0 `lookahead` / 0 bare `open` / 0 bare `high` / 0 bare `low` / 0 `volume`. `close` is the sole price series read by any order-affecting line; `ohlc4` enters only through one `display.none` visual plot. No portable economics beyond the two bare order calls ships anywhere — recorded as an absent-economics stub, never as zero-cost evidence.
- Licence and rights: the mirror file carries no licence header of its own beyond the `Copyright (c) 2021-present, Alex Orekhov (everget)` Pine header line; this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly five: (1) header repair `study(` → `strategy(` with the two written `strategy.entry` legs kept verbatim (the mirror's `study` header would not compile its own order legs in Pine v4 — the executable signal/order lines are untouched, disclosed here); (2) market/frame pin `BTCUSDT 1d` (the source stanza pins `2h`/`15m` on `Futures_Binance BTC_USDT` — venue transfer, symbol spelling and frame choice are disclosed here, never presented as source-native); (3) completed-bar decisions with same-bar-close fills (the source ships no `process_orders_on_close` argument — Pine default would fill later; this record's timing is a predeclared derivation, disclosed here); (4) an adopted 300-bar warmup with pre-warmup bars flat by record rule (covers the `var`-seeded trend/extreme state with wide margin — see Required data); (5) house sizing/capital/costs replacing the absent source economics (see Execution assumptions). The `k = 2` coefficient, the trend/extreme update legs, the `trend == ±1 and trend[1] == ∓1` flip tests, the `if/else-if` order pair, the two-sided reversal stance, and the no-stop/no-target posture are source-native and unmodified.

Pre-write dedup (2026-10-11): working-tree case-insensitive search for `nrtr`, `rypock`, `kopyrkin`, `365713`, `trailing-reverse`, and `mobo-band` returns no strategy record. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool relatives: `psar-flip-stop-reverse` (parabolic time-accelerated stop flip — no percentage channel, no trend-memory extremes), open PR #89 Chandelier Exit (single highest-high/lowest-low ATR trailing-stop flip — the NRTR prose itself distinguishes NRTR as percentage-based with no ATR component), open PR #63 SuperTrend (ATR-multiple band flip — ATR-scaled, not percentage-scaled), and `triple-ema-volstop-tp-long` (volatility-stop with take-profit — stop-plus-target, not reversal-only). None computes the `hp * (1 − k%)` / `lp * (1 + k%)` current-trend-only percentage channel with the `trend[1]`-gated flip pair. Not a trivial parameter variant.

## Economic mechanism

### Source-reported

Percentage-distance trailing channel with trend-memory extremes (prose plus code): the line rides `k = 2%` inside the extreme reached during the current trend only (`hp * (1 − percentage)` under an uptrend, `lp * (1 + percentage)` under a downtrend), ratcheting with each new extreme and discarding the previous trend's extremes at every flip. A close printing through the line flips the trend and re-seeds the opposite extreme at the flip bar's close. The design bets that a 2% violation of the current-trend extreme marks a real regime turn rather than noise; it ships no stop, no target, and no flat state — the book always carries the last flip signal. The prose frames this explicitly as the ATR-free cousin of the Chandelier Exit.

### Research interpretation

State-latch flip machine, edge-triggered, two-sided — one of the simplest possible trigger surfaces: the entire signal is the two equality tests on the persistent `trend` integer. Unlike cross-event machines (Chande-Kroll stop-line crosses, Stochastic-OTT dual-trend) there is no derived level for price to cross — the line itself is a function of the latch, and the latch is a function of the line, so the system is a closed two-state loop with exactly one parameter. Unlike single-stop flip systems (Chandelier #89, PSAR, SuperTrend #63) the offset is a fixed percentage of the remembered extreme rather than a volatility multiple, so the channel neither breathes with ATR nor accelerates with time — chop persistence and trending hug are both set by the single `k`. Unlike oscillator-cross records (CMO-80, Fisher zero-cross) there is no bounded oscillator at all. The bet is on percentage violation of current-trend extremes as regime-shift evidence under `k = 2`, not on any price level, band penetration, volatility multiple, slope test, calendar effect, or second timeframe.

## Signal

Exact rule as pinned (`k = 2` frozen — any other value is a different, unpinned rule; `showLabels`/`applyRibbon` are visual-only and frozen at `true` with zero order effect):

- Declarations (derived): two-sided flip machine over `BTCUSDT 1d` with same-bar-close execution and house sizing/costs (see Execution assumptions). State ∈ {flat, long, short}; flat exists only before the first post-warmup order; at most one unit is ever held.
- Channel construction, pinned verbatim: `percentage = 2 * 0.01`; persistent `trend` (init `0`), `hp`/`lp`/`nrtr` (each init `close`); on every bar, if `trend >= 0`: new up-extreme ratchet (`close > hp` → `hp := close`, `nrtr := hp * (1 − percentage)`), then violation test (`close <= nrtr` → `trend := −1`, `lp := close`, `nrtr := lp * (1 + percentage)`); else (downtrend mirror): `close < lp` → `lp := close`, `nrtr := lp * (1 + percentage)`, then `close > nrtr` → `trend := 1`, `hp := close`, `nrtr := hp * (1 − percentage)`.
- Orders, pinned verbatim: `buySignal = trend == 1 and trend[1] == -1` → `strategy.entry("Enter Long", strategy.long)`; `sellSignal = trend == -1 and trend[1] == 1` → `strategy.entry("Enter Short", strategy.short)`, via `if buySignal … else if sellSignal` evaluated on every completed bar. From flat the first flip opens; from the same side the call is a no-op under the default no-pyramiding construction (no `pyramiding` argument ships anywhere); from the opposite side the call reverses the full unit in one step — reversal is the sole exit path, with no separate exit leg (zero `strategy.exit`/`strategy.close` legs anywhere). The two signals are mutually exclusive by construction (`trend` cannot equal both `1` and `−1`), so the `else` consumes nothing — disclosed; under single-unit no-pyramiding construction at most one order prints per bar, never stacking.
- Exits and risk, pinned verbatim: there are none besides reversal — zero `strategy.exit`/`strategy.close` legs, zero `stop=`/`limit=`/`profit=`/`loss=` qualifiers anywhere. No take-profit, no trailing beyond the flip line itself, no time exit, no flat signal — pinned as written, explicitly none, not invented.
- Direction: two-sided with resting exposure. A long-only reading would contradict the `"Enter Short"`/`strategy.short` leg and is explicitly not this record.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (the extreme ratchets, the percentage channel, and the two flip tests; no bare `open`/`high`/`low` series is read by any order-affecting line, and no `volume`, funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read anywhere; `ohlc4` feeds one `display.none` visual plot exclusively).
- Single decision timeframe `1d` (derived pin; zero `request.security` calls ship anywhere, so no second evaluated frame exists by construction).
- Warmup: the binding seed stack is the four `var` declarations (`trend = 0`, `hp`/`lp`/`nrtr` = first `close`) plus one `trend[1]` history read. The adopted warmup is the first 300 completed `1d` bars flat by record rule (predeclared researcher choice — two orders of magnitude beyond the single-bar structural seed with margin; no traded bar reads a seeded value). Seed behavior is deterministic and fenced: on the very first bar `trend = 0 ≥ 0` with `hp = nrtr = close` gives `close > hp` false and `close <= nrtr` true, so the seed forces `trend := −1` without printing any order (`trend[1]` is `na`, and `na`-gated comparisons never fire) — the warmup absorbs this seed flip structurally, disclosed, never a researcher tie-break. No repainting, no negative shift, no future reference, no full-sample normalization, no `lookahead`, no `barstate`-gated order path; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (derived pin; the source stanza pins `2h`/`15m` on `Futures_Binance BTC_USDT` — venue transfer, symbol spelling and frame choice are disclosed here, never presented as source-native). The short leg needs a venue with short permission; futures satisfies this — disclosed.
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source ships no `process_orders_on_close` argument — Pine default would fill later; this record claims no source-native timing and no intrabar behavior. No maker-touch, queue, or intrabar-path-dependent fill: with at most one written order event per bar and no stop/limit legs anywhere, same-bar ordering is trivially the written order, disclosed.
- Sizing/capital/costs: the source ships no portable economics of any kind (no capital amount, no commission/slippage/funding/margin argument ships anywhere — recorded as an absent-economics stub, never as zero-cost evidence) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: single-unit machine by default no-pyramiding construction — at most one unit long or short; same-side re-assertion prints nothing. No cooldown ships anywhere (explicitly none, not invented). No flat state is reachable after the first post-warmup order except by reversal; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The mirror ships the full construction (the `study` header, the `k`/`showLabels`/`applyRibbon` inputs, the four `var` state declarations, both trend-branch update legs, the `buySignal`/`sellSignal` flip tests, the `if/else-if` order pair, the visual `plot`/`plotshape`/`fill` block, the three `alertcondition` calls, the inventor/method prose, the three-row arguments table, and the FMZ backtest stanza). It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — the one backtest screenshot image is untranscribed and this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden risk layer: the body contains zero `strategy.exit`/`strategy.close` legs and zero `stop=`/`limit=`/`profit=`/`loss=` qualifiers. The no-stop/no-target reversal-only posture is prescribed, explicitly none, never hidden.
2. Header artifact repaired by predeclared derivation: the mirror declares `study(...)` while shipping two `strategy.entry` legs, which would not compile as printed under Pine v4. This record changes only the header plumbing to `strategy(` and keeps every signal/order line byte-identical in behavior; the repair is predeclared above, not a reviewer invention, and no formula, threshold, or order mapping was altered to effect it.
3. No third order path: the only order legs are the written `if/else-if` pair over mutually exclusive flip tests — every bar resolves to zero or one order event, so no precedence or cooldown rule was invented beyond written order under single-unit construction.
4. `<=` / `>` strictness fenced: the down-flip test is `close <= nrtr` (touch flips) while the up-ratchet test is `close > hp` (touch does not ratchet) and the up-flip test is `close > nrtr` (touch does not flip upward). An equal-touch reading swapped across legs would contradict the code and is explicitly not this record.
5. Seed behavior fenced: the four `var` initializers plus the `na` first `trend[1]` keep the seed bar order-free and force `trend := −1` deterministically (see Required data) — the adopted 300-bar flat absorbs the entire seed stack structurally, so no seeded value ever trades. Structural, disclosed, never a researcher tie-break.
6. Single-frame fenced: zero `request.security` calls ship anywhere — there is no MTF pull, no cross-symbol pull, and no `lookahead`. Every input is a causal function of completed `close` values inclusive of the decision bar, computable point-in-time with no future leakage — stated plainly. The source stanza's `basePeriod: 15m` is FMZdocumentation of its own 2h backtest, not a second evaluated frame in the Pine logic — disclosed, not carried into this record.
7. Visual/alert-only surface fenced: the two `plot(` calls, four `plotshape(` calls, two `fill(` calls, three `alertcondition(` calls, and the `showLabels`/`applyRibbon` inputs print labels, ribbons, and alerts and gate no order — a reader mistaking a Buy/Sell label or ribbon edge for a second signal would contradict the census. The signal is the `trend[1]`-gated flip pair, nothing else.
8. Order-id completeness fenced: the sole long id is `"Enter Long"` and the sole short id is `"Enter Short"` — with no pyramiding anywhere there is at most one unit to reverse, so the opposite-side `strategy.entry` provably flattens-and-reopens in one step. No partial-fill residue is reachable by code.
9. Source-economics absence fenced: the stanza's date range and venue describe the author's FMZ backtest run, not portable cost facts — this record carries no commission/slippage/funding claim from the source and assigns all economics to the disclosed house overlay.
10. Derivation boundary fenced: the only non-source-native behaviors in this record are the `strategy(` header repair, the `BTCUSDT 1d` market/frame pin, completed-bar same-bar-close fills, the adopted 300-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the `k = 2` coefficient, the trend/extreme update legs, the flip tests, the `if/else-if` order pair, single-unit no-pyramiding state, the two-sided reversal stance, and the risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, parameter set, or timing of the source passes.
11. Network limitation disclosed: every formula line above was byte-verified in the pinned mirror file at commit `7853bb2` (4120 bytes, blob SHA recorded, `git hash-object` identical on re-download, contents-API `sha`/`size` matched); the FMZ canonical page verified live the title, the `ChaoZhang` token, the Kopyrkin/NRTR percentage-channel prose, and the absence of any performance numbers — the division of evidence is disclosed here, not hidden.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `k = 2` / trend/extreme update legs / `trend[1]`-gated flip pair / `"Enter Long"`/`"Enter Short"` order pair / no-stop-no-target posture / two-sided single-unit / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Channel-width relevance: replacing `k = 2` with `k = 6` (same update legs, same flip tests, same risk posture) must not improve net expectancy; fail ⇒ the pinned 2% hug adds nothing over a wider channel.
- F2 — Trend-memory relevance: replacing the state-filtered flip pair with raw close-through-line crosses on both legs (firing on every `close <= nrtr` / `close > nrtr` touch without the `trend[1]` transition gate, same channel, same risk posture) must not improve net expectancy; fail ⇒ the current-trend-only memory adds nothing over memoryless line crosses.
- F3 — Two-sided relevance: running the long leg only with the short leg disabled (same channel, same gate, same risk posture) must not improve net expectancy; fail ⇒ the two-sided reversal stance adds nothing over its long half.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (derived pin; the source stanza pins `2h`/`15m` on `Futures_Binance BTC_USDT`). The close-only percentage arithmetic ports across perpetual venues without structural change — no volume read means venue volume-reporting differences touch nothing, disclosed as a robustness property, not a portability proof. The two-sided stance requires a short-capable venue (futures satisfies this); a spot deployment would express only the long half and is a different, unpinned claim. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no session gating anywhere); decision boundaries are calendar-day bars of the venue feed, disclosed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived header repair: the source prints `study(` over `strategy.entry` legs; this record executes the identical logic under a `strategy(` header. Backtest economics of the timings differ from Pine defaults by construction — the adaptation is disclosed, not hidden, and this record makes no claim about any other timing's performance.
- Derived market and frame: the source stanza pins `2h`/`15m`; this record pins `BTCUSDT 1d`. Cross-market and cross-frame behavior differences are real — the adaptation is disclosed, and this record makes no claim about any other market or frame.
- Reversal-only risk: there is no flat signal and no stop — adverse excursion reverses only on the next opposite flip, a drift that never prints through the ratcheted line holds indefinitely, and whipsaw under alternating flips is the coded cost of the design, disclosed, not smoothed, not supplemented.
- No source economics: the source ships no capital amount, commission, slippage, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Seed coverage: the `var` seed stack settles on the first bar; the first 300 `1d` bars are flat by record rule, so early-history signals never enter any evaluation.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- FMZ canonical strategy page (Kopyrkin/NRTR percentage-channel prose verified live via HTTP-200 page record): https://www.fmz.com/strategy/365713
- Immutable mirror file at pinned commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (blob `22b1b47d64c39c6983e39f0a0c3dbf0a07edd6f6`, 4120 bytes): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/Nick-Rypock-Trailing-Reverse-NRTR.md
- Pine strategy semantics (v4 `strategy.entry` order legs, `var` state persistence, history-referencing `[]`): https://www.tradingview.com/pine-script-reference/v5/
