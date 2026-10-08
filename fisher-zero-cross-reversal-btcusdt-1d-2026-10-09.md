---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Fisher zero-cross two-sided reversal on BTCUSDT 1d bars
created: 2026-10-09
updated: 2026-10-09
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2016-12-23
sources:
  - https://www.tradingview.com/script/qhXwZvJ2-Fisher-Transform-Indicator-by-Ehlers-Backtest-v-2-0/
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Fisher zero-cross two-sided reversal on BTCUSDT 1d bars

## Provenance

Primary source read end to end (TradingView canonical strategy page plus its full open-source block, fetched 2026-10-09):

- Canonical page: https://www.tradingview.com/script/qhXwZvJ2-Fisher-Transform-Indicator-by-Ehlers-Backtest-v-2-0/ (`Fisher Transform Indicator by Ehlers Backtest v 2.0`, Strategy by HPotter [WIZARD badge on page], `OPEN-SOURCE SCRIPT`, page stamp Dec 23 2016, adopted as `source_as_of`). Tags on page: algotrading, backtesting, ehlers, fisher, strategy.
- Page-stated rule (verbatim substance): market prices are not Gaussian, but the Fisher transform `y = 0.5 * ln((1+x)/(1-x))` applied to normalized prices makes peak swings rare and sharply identifiable; "For signal used zero. You can change long to short in the Input Settings. Please, use it only for learning or paper trading. Do not for real trading." The page carries no performance table, figure, trade count, date range, or cost basis in its prose — this record claims no source-reported performance (see Evidence).
- Full 39-line `//@version=2` block read in the page's source viewer. Verbatim source declaration (note the absence it discloses, load-bearing for the derived status below): `strategy(title="Fisher Transform Indicator by Ehlers Backtest", shorttitle="Fisher Transform Indicator by Ehlers")` — no `process_orders_on_close`, no `pyramiding`, no `default_qty_*`, no `commission_*` lines. Source fills are therefore next-bar-open by Pine default; this record's same-bar-close execution is a separately identified researcher adaptation, never presented as source-native (see Execution assumptions).
- Pinned source inputs: `Length = input(10, minval=1)`, `reverse = input(false, title="Trade reverse")`. This record pins both defaults; retuning the window or enabling the flip would each be a different, unpinned rule.
- Text census over the pinned block: 0 `request.*`, 0 `security(`, 0 `timeframe(`, 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=`, 0 `alert(`/`alertcondition`, 0 `volume`, 0 `open`, 0 bare `close` (the rule reads `hl2` only — neither close, open, nor volume appears anywhere). Live order calls are exactly two (`strategy.entry("Long", strategy.long)`, `strategy.entry("Short", strategy.short)`). Display-only calls are `barcolor`, `hline(0, ...)`, and two `plot` lines — none gates any order.
- Licence and rights: the canonical page is an open-source publication by HPotter. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly two: (1) research market/timeframe BTCUSDT `1d` (the script takes no symbol, timeframe, session, or venue input and reads only `high`/`low` via `hl2`); (2) same-bar-close fills via `process_orders_on_close=true` (the source fills next-bar-open). Both adaptations are predeclared here, confined to Provenance, Signal, Execution assumptions, and Limitations, with every original claim kept separate above. Indicator formula, lookback, zero threshold, state-hold semantics, reverse default, pyramiding default, two-sided direction, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-09): working-tree searches for `fisher`, `ehlers`, `qhXwZvJ2`, `HPotter`, `hpotter`, `nFish`, and `nValue1` return zero strategy records using this source, author, oscillator, or formula. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #58 (17-family ML/portfolio reconstruction batch, unmerged), and #63 (SuperTrend ATR-flip trend long) — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `rsi-classic-level-reversal-btcusdt-1h-2026-10-07.md` holds a Wilder `rma`-smoothed gain/loss ratio below a fixed level (level-hold, long-only, signal-line close exit); `williams-r-level-cross-mean-reversion-long-btcusdt-1d-2026-10-09.md` fires strict cross events of an unsmoothed range-position ratio against fixed −80/−20 levels (long-only, overbought-recross exit); the Wilder-RSI27/SMA10 record crosses a smoothed ratio against its own average. This record instead warps bounded normalized `hl2` through the Fisher nonlinearity with recursive smoothing, signals on the signed side of zero with an explicit hold-prior state at exactly zero, and reverses two-sided — no pool record evaluates `0.5*log((1+x)/(1-x))`, gates on zero-sign with a latched state, or reverses long/short on that event. Five-axis distinction: mechanism differs (nonlinear Gaussianizing warp plus zero-sign latch, two-sided reversal, versus level-holds, level-crosses, or ratio/average crosses), signal construction differs (formula above with Length 10, nothing in the pool computes it), exits differ (opposite-signal reversal is the sole exit path, no level-recross/time/trailing variant matches), source identity differs (HPotter TV Dec-2016 `qhXwZvJ2` versus Julien_Exe, FMZ/ChaoZhang, hasnocool mirrors, or other TV authors), and direction handling differs (both sides live at the pinned default versus long-only or gated records).

## Economic mechanism

### Source-reported

Gaussianized exhaustion reversal: normalizing `hl2` into its trailing-window position and warping it through the Fisher transform makes turning points sharp and rare; a positive Fisher value reads as upside pressure (long), a negative value as downside pressure (short), with the zero line as the sole signal reference. The author ships no stop, no target, no trailing order: the opposite zero-sign reading is the entire risk control. Risk guidance is prose-only ("use it only for learning or paper trading") and specifies no executable rule.

### Research interpretation

Nonlinear position-momentum reversal with a latched state. Unlike RSI-family records, the signal performs no averaging of gains or losses: it ranks `hl2` inside its trailing 10-bar range, rescales to [−1, 1] with 0.33/0.67 recursion, clamps, then expands through `log((1+x)/(1−x))` so mid-range drift compresses and extremes spike — entries therefore trigger on the sign of a spike-amplified position readout, and the `pos` latch (hold prior at exactly zero) makes the system state-driven rather than event-driven: the book always carries the last nonzero conviction, long or short, with flat existing only before the first nonzero print. No leverage, sizing, or cost edge is embedded in the signal; sizing lines are absent from the source declaration, so the house overlay supplies them (see Execution assumptions).

## Signal

Exact rule as pinned (defaults quoted — inputs unmodified):

- Declaration (derived): `strategy(title="Fisher Transform Indicator by Ehlers Backtest", shorttitle="Fisher Transform Indicator by Ehlers", process_orders_on_close=true)` — the first two arguments are the source verbatim; `process_orders_on_close=true` is the predeclared researcher adaptation (source declaration carries no such argument). `pyramiding` is unset (v1/v2 language default: a single open entry per direction — additional same-direction entries rejected, opposite-direction entry closes and reverses; load-bearing here, pinned explicitly, see Execution assumptions).
- Normalization (window pinned): `xHL2 = hl2`, `xMaxH = highest(xHL2, Length)`, `xMinL = lowest(xHL2, Length)` with `Length = 10`.
- Warp (recursive, deterministically seeded): `nValue1 = 0.33*2*((xHL2-xMinL)/(xMaxH-xMinL)-0.5) + 0.67*nz(nValue1[1])`; `nValue2 = clamp(nValue1, ±0.999)` via the nested `iff`; `nFish = 0.5*log((1+nValue2)/(1-nValue2)) + 0.5*nz(nFish[1])`. Both recursions seed missing history with `nz(..., 0)`, so every bar evaluates to a finite value except a zero-range window (see Negative evidence).
- State latch (threshold pinned at zero): `pos = nFish>0 ? 1 : nFish<0 ? -1 : nz(pos[1], 0)` — strictly positive prints long-conviction, strictly negative prints short-conviction, an exact-zero print holds the prior bar's conviction, and the seed before any nonzero print is flat 0.
- Direction switch (pinned off): `possig = reverse ? -pos : pos` with `reverse = false`, so `possig == pos` at this configuration; enabling it would be a different, unpinned rule.
- Entries: `if (possig == 1)` → `strategy.entry("Long", strategy.long)`; `if (possig == -1)` → `strategy.entry("Short", strategy.short)`, evaluated on the completed-bar close with same-bar-close execution under the derived declaration. Because both conditions are checked every bar, the first bar printing the opposite conviction reverses the position in one step — reversal is the sole exit path by construction.
- Display isolation: `barcolor`, `hline(0)`, and the two `plot` calls (Fisher plus its one-bar-ago trigger twin) gate no order condition; the plotted trigger line is visualization only and is never referenced by any entry condition.

## Required data

- Completed `1d` bars of BTCUSDT: `high`/`low` only (via `hl2`). No `open`, no `close`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d`. The script takes no timeframe input and makes no live `request.*`/`security(`/`timeframe(` call, so it is single-frame by construction; `1d` is adopted as the research frame because it is a campaign timeframe and the script's classic daily design frame — never presented as anything beyond that (see Limitations).
- Warmup: the 10-bar high/low window is only full from the 10th completed `1d` bar, and both recursions seed deterministically with `nz(..., 0)` from the first bar, so the first fully-formed signal bar is the 10th completed `1d` bar. No repainting, no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT under the house overlay (the rule reads high/low only; venue transfer is never presented as source-native semantics).
- Order timing (predeclared derivation): `process_orders_on_close = true`: completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. The source's own timing is next-bar-open (declaration carries no such argument — quoted verbatim in Provenance); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill. 0 `strategy.exit` calls, hence no stop/limit order and no same-bar TP/SL ordering ambiguity anywhere in the rule.
- Sizing/capital: the source declaration carries no quantity or capital line at all, replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions, never presented as source-native behavior.
- Concurrency: `pyramiding` is unset (v1/v2 default: one open entry per direction). The default is load-bearing and therefore pinned explicitly: repeat same-conviction bars during an open position are rejected no-ops, and the opposite-conviction bar closes-and-reverses in a single step (no separate exit call exists or is needed). Re-entry after any flat seed state occurs on the next nonzero-conviction bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The canonical page ships the Gaussian-PDF rationale, the Fisher formula, the zero-signal reference, the `reverse` input option (default off), the two-sided entry construction, and prose risk guidance. It ships zero performance numbers in its prose: no return, no win rate, no profit factor — this record claims no source-reported performance and no reproduced performance, and does not rely on the page's Strategy Tester tab. (The page's chart header shows an ES1! futures context; this record adopts BTCUSDT `1d` as a predeclared research frame and claims no source-venue semantics.)

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=` — the opposite zero-sign entry is the sole exit path by construction, and the prose promises no stop or target.
2. Exact-zero determinism: `nFish == 0` holds the prior conviction via `nz(pos[1], 0)`; the `iff` chain is total (positive / negative / else), so no bar leaves `pos` undefined, and the pre-first-signal seed is flat 0, never a phantom side.
3. Flat-range division named: a zero 10-bar `hl2` range makes `(xHL2-xMinL)/(xMaxH-xMinL)` undefined (`na`), which propagates through `nFish` and makes both `>`/`<` comparisons false — the latch holds prior and fires nothing, by the language's own `na` comparison semantics.
4. Reverse switch fenced: at pinned `reverse=false` the short side is live source behavior, not an adaptation; flipping it would invert every signal and would be a different, unpinned rule — none is admitted here.
5. Display-free gating: `barcolor`/`hline`/both `plot` calls appear in no order condition; restyling or hiding any of them cannot alter any admitted event.
6. Price-field minimalism: `close`, `open`, and `volume` are absent from the entire block, so session gaps, opens, and volume reporting cannot influence any admitted event — gap behavior is absent rather than approximated.
7. The window, zero threshold, recursion seeds, reverse default, pyramiding default, and two-sided direction are pinned, not removed: retuning Length, thresholding at nonzero levels, gating on the plotted trigger line, adding a stop/target/cooldown/session filter, or enabling reverse would each be a different, unpinned rule — none is admitted here.
8. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT-`1d` research frame and same-bar-close fills, both predeclared above; every signal, threshold, default, state transition, and risk posture is source-verbatim. This record is therefore never evidence that the original next-bar-open source itself passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: Length 10 / zero-sign latch / two-sided / reverse-off / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Zero-reference relevance: entering on Fisher/trigger-line crosses (`nFish` crossing its plotted one-bar-ago twin, the visualization the source never trades) instead of the zero-sign latch must not improve net expectancy; fail ⇒ the zero reference adds nothing over the line-cross the page merely draws.
- F2 — Reversal relevance: holding each entry for a fixed research-defined bar count instead of the opposite-sign reversal must not improve net expectancy; fail ⇒ the always-in reversal adds nothing over time exits.
- F3 — Warp relevance: trading the zero-sign of the unwarped bounded input (`nValue1`, same recursion, no logarithm) must not reproduce-or-beat net expectancy; fail ⇒ the Fisher nonlinearity adds nothing over its own linear input and the record is a label variant of a plain position-momentum latch.

## Crypto portability

Pinned to BTCUSDT perps under the house overlay. The high/low-only two-sided logic ports to perps without structural change; a spot-only deployment would require disabling the short side and would be a different, unpinned rule. No funding-dependent leg, no stablecoin-specific assumption, no session, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (`open`/`close`/`volume` are never referenced), so session-gap behavior is simply absent rather than approximated. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source fills next-bar-open; this record executes same-bar-close. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- Always-in exposure: after the first nonzero print the latch never returns to flat, so the book carries overnight/weekend-equivalent risk on every bar with no neutral stance available by construction.
- No price stop: adverse excursion after entry has no guardrail beyond the opposite zero-sign print; a vertical-against move reverses only when the warped readout changes sign, which can be far.
- Warmup cost: the range window needs 10 completed bars, so the system is blind for the first 9 bars of any 1d evaluation window (recursion seeds are deterministic but the window is incomplete).
- Performance evidence is absent: the canonical prose reports no numbers at all; nothing here is calibrated, fitted, or tuned to any backtest.
- Zero-chop whipsaw: in a sideways market `nFish` can alternate sign on consecutive bars, printing long-short reversal pairs with no structural filter — the source provides none and this record invents none.
- Author's own caveat: the page asks that the script be used for learning or paper trading only; this record is research-only and claims no live suitability.

## Implementation status

Not implemented. No Hummingbot controller/executor, no Qlib screening, no Paper/Testnet/Live run has been performed from this record. Admission claims pinned-engine expressibility only (see Execution assumptions), subject to independent six-gate review.

## Adoption boundary

Research-only. Not approved for any downstream screening, parity run, or trading authorization. Only a `PASS` under the live six-gate contract may merge this record into `main`; any `NOT_LOSSLESS` finding closes the PR lane without promotion.

## Related Wiki records

None.

## Sources

- Canonical strategy page (fetched 2026-10-09): https://www.tradingview.com/script/qhXwZvJ2-Fisher-Transform-Indicator-by-Ehlers-Backtest-v-2-0/
- Pine v5 strategy semantics (declaration defaults, order calls, close-evaluated execution): https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
- Pine strategy concepts: https://www.tradingview.com/pine-script-docs/concepts/strategies/
