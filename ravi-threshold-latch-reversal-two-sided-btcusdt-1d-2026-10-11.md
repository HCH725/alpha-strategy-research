---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: RAVI 0.14-threshold latch reversal two-sided on BTCUSDT 1d bars
created: 2026-10-11
updated: 2026-10-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2017-10-13
sources:
  - https://www.tradingview.com/script/qMGsVEKk-Range-Action-Verification-Index-RAVI-Backtest/
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# RAVI 0.14-threshold latch reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (canonical TradingView page fetched live over HTTPS plus the page's own open-source Pine payload fetched live from the TradingView Pine facade during this cycle, verified 2026-10-11):

- Canonical page: https://www.tradingview.com/script/qMGsVEKk-Range-Action-Verification-Index-RAVI-Backtest/ (page title `Range Action Verification Index (RAVI) Backtest — Strategy by HPotter`, author `HPotter`, `OPEN-SOURCE SCRIPT` badge, script-kind `strategy`). Theory prose on the page and in the code header: the indicator is the relative convergence/divergence of two moving averages scaled a hundredfold, on a different principle than ADX; Tushar Chande's suggested basis is a 13-week (65-working-day) slow average capturing quarterly participant sentiment, with the fast average at roughly 10% of it, rounded to seven.
- Full `//@version=2` block verified live from the facade (`scriptName: Range Action Verification Index (RAVI)`, `Copyright by HPotter v1.0 13/10/2017`, `created`/`updated` `2017-10-13T00:11:07Z` — adopted as `source_as_of` 2017-10-13, `scriptAccess: open_no_auth`, `lastVersionMaj: 1.0`): `strategy(title="Range Action Verification Index (RAVI)", shorttitle="RAVI")`, inputs `LengthMAFast = input(title="Length MA Fast", defval=7)`, `LengthMASlow = input(title="Length MA Slow", defval=65)`, `TradeLine = input(0.14, step=0.01)`, `reverse = input(false, title="Trade reverse")`, `hline(TradeLine, ...)` setup line, `xMAF = sma(close, LengthMAFast)`, `xMAS = sma(close, LengthMASlow)`, `xRAVI = ((xMAF - xMAS) / xMAS) * 100`, the `pos` latch, the `possig` reverse switch, both `strategy.entry` legs, the `barcolor(...)` assignment, and the final `plot(xRAVI, color=green, title="RAVI")`. No login wall stands between the reader and any order-gating line: every line that can open, close, or size a position was read verbatim from the primary source.
- Text census over the pinned code block: 2 `strategy.entry` (`"Long"` with `strategy.long`, `"Short"` with `strategy.short`, no price argument) / 0 `strategy.close` / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `time(` / 0 `volume` (the rule reads `close` only — `sma(close, ...)` twice; neither `open`, `high`, `low`, nor `volume` appears in any order-gating line) / exactly 4 `input(` (`LengthMAFast 7`, `LengthMASlow 65`, `TradeLine 0.14`, `reverse false` — all strategy inputs, no webhook strings) / `process_orders_on_close` unset (Pine default: signals evaluate per completed bar, fills on the next bar) / `pyramiding` unset (Pine default: no same-direction adds) / no `commission`/`slippage` arguments (Pine defaults — recorded as absent, never as zero-cost evidence; see Execution assumptions).
- No risk layer ships anywhere in the source: zero stop/target/trailing/time-exit order legs, and the header's only risk-adjacent line is the educate-only warning — the no-stop/no-target posture below is therefore the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention.
- Page performance language is absent entirely (no table, figure, or number) — this record claims no source-reported performance and no reproduced performance. The source names no market and no timeframe (pure indicator math plus order legs) — the `BTCUSDT 1d` pin below is a fully researcher-declared derivation choice, disclosed here, never presented as a source claim.

Licence and rights: the pinned code block carries `// Copyright by HPotter v1.0 13/10/2017` with an educate-only warning. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) market/frame pin `BTCUSDT 1d` (the source names no market and no timeframe at all — this pin is a pure researcher choice, disclosed here, never presented as source-native); (2) same-bar-close fills (the source ships no execution-timing argument — Pine default fills evaluate per completed bar and fill on the next bar; no `process_orders_on_close` ships anywhere, quoted verbatim in census); (3) an adopted 75-bar warmup with pre-warmup bars flat by record rule (covers the 65-bar slow-SMA seed plus margin — see Required data) and house sizing/capital/costs replacing the absent source economics (the source ships no commission/slippage/capital/funding/margin assumption at all — see Execution assumptions). The SMA-convergence percentage formula, the `7/65` lengths, the `0.14` trigger, the `reverse=false` setting, the threshold-latch state machine, the `Long`/`Short` order IDs, the two-sided reversal handling, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-11): working-tree case-insensitive search for `ravi`, `range-action-verification`, `Range Action Verification`, `LengthMAFast`, and `xRAVI` returns zero hits anywhere outside scratch — no admitted rule uses this source, author strategy, indicator, or mechanism. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closed research PRs contain no RAVI record. Closest pool records are different mechanism classes: `elder-ray-123reversal-combo` is Elder bull/bear power versus a 13-EMA consensus fused with a 123-reversal pattern (never an SMA-7/65 convergence percentage, never a single-constant latch); `kst-signal-cross` is a four-ROC smoothed momentum cross of two lines (never index-versus-constant); `cmf-velocity-zero-cross-ema200-bracket` is a normalized money-flow ratio with a velocity gate (reads volume; this rule reads no volume at all); `obv-ema-crossover-trend` crosses a cumulative signed-volume line against its EMA (this rule never touches volume and crosses nothing — its only comparison is index-versus-constant). Five-axis distinction: mechanism differs (Chande SMA-convergence percentage latch with binary ±1 state and reversal exits — versus power oscillators, ROC crosses, or money-flow ratios), signal construction differs (no pool record computes `((sma(close,7)-sma(close,65))/sma(close,65))*100`), trigger differs (index-above-`0.14` long state versus index-below-`0.14` short state, held until the opposite placement — not a cross, not a band touch, not a flip on opposite signal), data differs (close only; no high, low, volume, or multi-frame read), and source identity differs (HPotter RAVI Backtest, 2017-10-13, TV `qMGsVEKk`).

## Economic mechanism

### Source-reported

Trend-persistence latch (code header plus theory prose, no performance section ships): the quarterly slow average `sma(close,65)` is the market's consensus value and the weekly fast average `sma(close,7)` is current sentiment; when sentiment stretches more than `0.14` percent above consensus the trend is deemed confirmed and the system holds long, and when the convergence falls back below `0.14` the confirmation is deemed lost and the system holds short. The design bets that SMA-convergence persistence predicts continuation rather than exhaustion, and it expresses that bet as a latched two-sided state, not as a one-shot cross: once placed above or below the trigger, the posture persists until the index prints on the opposite side. There is deliberately no stop, no target, and no flat state after the first placement — the header admits educate-only status with no risk leg anywhere, by design gap rather than by hidden leg.

### Research interpretation

Single-threshold convergence latch, two-sided with reversal exits and an explicit pre-first-signal flat state. Unlike cross systems that trade the moment one line passes another, this rule never trades a cross at all: its only comparison is index-versus-constant (`0.14`), and the `pos` latch (`nz(pos[1], 0)` memory) makes every non-crossing bar a hold, not a decision. Unlike always-in-market flip systems, the rule rests flat before the first threshold placement (the latch seeds from `0`, and `0` fires neither entry leg). Note the asymmetry the source pins plainly: both latch branches compare against the same `+0.14` line (above → long, below → short) — there is no mirrored `-0.14` band, so the short state is the default resting side for any print at or under consensus. The price of the latch is whipsaw at the line: an index that flickers across `0.14` prints full long/short reversals at the worst prints of each flicker, and a strong trend whose convergence stays stretched keeps the system long into the teeth of a top — the coded rule rides stretched convergence rather than fading it with confirmation. The bet is on trend persistence, not on any reversal level, volume print, mean-reversion extreme, or calendar effect.

## Signal

Exact rule as pinned (`7/65` lengths, `0.14` trigger, `reverse=false` frozen — any other value is a different, unpinned rule):

- Declaration (derived): `strategy(title="Range Action Verification Index (RAVI)", shorttitle="RAVI")` semantics preserved with the derived `BTCUSDT 1d` market/frame pin and same-bar-close execution adopted (no such timing argument ships in the source) and house sizing/costs replacing the absent source economics (see Execution assumptions). Pine-default no-pyramiding semantics hold (no `pyramiding` argument ships): at most one open position, same-direction refires are no-ops, opposite entries reverse in full.
- Index (pinned): `xMAF = sma(close, 7)`; `xMAS = sma(close, 65)`; `xRAVI = ((xMAF - xMAS) / xMAS) * 100` — no zero-guard ships in the source; on any traded market `xMAS` (a 65-bar average of positive closes) cannot be zero, and an `na` print would fail both strict comparisons and hold the prior latch state by construction (see Negative evidence). Every input is a completed bar's `close`; no `open`, `high`, `low`, or `volume` is read.
- State latch (pinned): `pos = iff(xRAVI > TradeLine, 1, iff(xRAVI < TradeLine, -1, nz(pos[1], 0)))` with `TradeLine = 0.14` — strictly above places long state, strictly below places short state, exact equality holds the prior state. With `reverse = false`, `possig = pos`.
- Entry long: `strategy.entry("Long", strategy.long)` under `if (possig == 1)` — fires on any completed bar whose latched state is long, with same-bar-close execution under the derived declaration. Refires while already long are no-ops under default no-pyramiding semantics.
- Entry short: `strategy.entry("Short", strategy.short)` under `if (possig == -1)` — fires on any completed bar whose latched state is short, with same-bar-close execution under the derived declaration. From flat it opens short; from long it reverses to short in full (the sole exit path — coded, not invented).
- Direction: two-sided with an explicit pre-first-signal flat state (the latch seeds `pos` from `0` via `nz(pos[1], 0)` and `0` fires neither leg; before the convergence first places on either side of `0.14`, no order can fire). After the first placement the system is always in market (long or short) — there is no coded flat state beyond the seed, disclosed, not enabled.
- Display isolation: the `hline(TradeLine, ...)` setup line, the `barcolor(...)` assignment, and `plot(xRAVI, ...)` render only and cannot change any order; order logic reads exactly the two `if` lines. No stop, no target, no trailing, no time exit — pinned as written, explicitly none, not invented.

## Required data

- Completed `1d` bars of BTCUSDT: `close` (only indicator input, read twice via the two SMAs). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (derived pin; the script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction).
- Warmup: the SMA-65 seed needs 65 completed `1d` bars — binding constraint is bar index ≥ 65 before every referenced value is fully seeded (the SMA-7 seed is absorbed inside it). The adopted warmup is the first 75 completed `1d` bars flat by record rule (predeclared researcher choice — covers seed plus margin). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Each bar's close enters the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (derived pin; the source names no market and no timeframe — venue choice and symbol spelling are disclosed here, never presented as a source claim).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar fill (no execution-timing argument ships anywhere — quoted verbatim in census); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. Entry legs are evaluated in source order (long block before short block): `possig` takes exactly one of `1`/`-1`/`0` per bar, so at most one leg can fire on any bar — no same-bar double-fill ordering exists under either evaluation order.
- Sizing/capital/costs: the source ships no economics at all (no capital, no commission/slippage argument, no funding, no margin assumption — quoted verbatim in census; the absence is disclosed, never read as zero cost) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: Pine-default no-pyramiding semantics hold — at most one open position under the fixed order IDs `Long`/`Short`; same-direction refires while already positioned are no-ops by the pinned default, the opposite entry reverses in full (the sole position-closing path), an entry while flat opens, and re-placement is allowed immediately on the next qualifying bar after any reversal (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (SMA-7 fast leg, SMA-65 slow leg, hundredfold convergence percentage, `0.14` single trigger with `0.01` step, `reverse=false`, fixed `Long`/`Short` order IDs, display-only hline/barcolor/plot), the active `strategy(...)` declaration, the `Range Action Verification Index (RAVI)` / `RAVI` titles, the four pinned inputs, and the Chande-65/7 theory header. It ships zero performance numbers and names zero markets and zero timeframes: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.close`, 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=` — the sole position-closing path is the coded opposite-state `strategy.entry` reversal. The absence is coded (the order block ends with the short leg and only display code follows it in evaluation order) and the header carries no risk leg anywhere.
2. Coded rule is a single-line latch, not a symmetric band, stated plainly: both latch branches compare `xRAVI` against the same `TradeLine = 0.14` (above → long, below → short); there is no `-0.14` mirror anywhere in the source, so the short state is the resting side for every print at or under consensus. Substituting a symmetric ±`0.14` band would be a different, unpinned rule.
3. No future leakage in the smoothing, stated plainly: at decision bar `t`, `xMAF` reads completed closes through `t`, `xMAS` reads completed closes through `t`, and the percentage reads those two seeded averages — every input is a completed historical bar. No `security()`, no `request.*`, no negative index, no `barstate.islast`-gated repainting path.
4. Same-bar entry ordering fenced: `possig` is exactly one of `1`/`-1`/`0` per bar (the latch's three branches are mutually exclusive by strict inequalities plus else-hold), so at most one of the two entry legs can fire on any bar. Deterministic under either fill convention.
5. Two-sided posture provably complete: both `strategy.long` and `strategy.short` appear exactly once each, each under its own guarded `if`; no third direction exists. The `reverse` switch is pinned `false` — enabling it would invert both sides and would be a different, unpinned rule.
6. Convergence-flicker whipsaw, admitted plainly: an index oscillating across `0.14` prints full long/short reversals at the worst prints of each flicker, and a sustained stretch holds long through distribution. There is no confirmation filter, no stop, and no flat state after the first placement — the coded posture, disclosed as the record's principal risk.
7. The close-only SMA-7/65 pair, the hundredfold convergence formula, the `0.14` trigger, the `reverse=false` setting, the strict latch inequalities, the fixed `Long`/`Short` order IDs, the reversal-only exits, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning any length or the trigger, converting the latch into a cross, symmetrizing the trigger into a band, adding a stop/target/filter/cooldown, or enabling `reverse` would each be a different, unpinned rule — none is admitted here.
8. Derivation boundary fenced: the only non-source-native behaviors in this record are the `BTCUSDT 1d` market/frame pin, same-bar-close fills, the adopted 75-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the convergence formula, lengths, trigger, latch, order IDs, reversal handling, and risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, or timing of the source passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: close-only SMA-7/65 / hundredfold convergence / `0.14` single-line latch / `reverse=false` / reversal exits / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Direction relevance: inverting the side mapping (above-`0.14` short, below-`0.14` long, same latch mechanics) must not improve net expectancy; fail ⇒ the coded persistence direction adds nothing over its mirror.
- F2 — Latch relevance: replacing the single-`0.14` line with a symmetric ±`0.14` band (long above `+0.14`, short below `-0.14`, hold between with latch memory, same entries) must not improve net expectancy; fail ⇒ the coded single-line latch is dominated by the symmetric-band construction it resembles.
- F3 — Smoothing relevance: replacing the SMA-7/SMA-65 pair with an EMA-7/EMA-65 pair (same lengths, trigger, and latch) must not improve net expectancy; fail ⇒ the coded SMA smoothing adds nothing over its exponential twin.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (derived pin; the source names no market at all). The close-price arithmetic ports across perpetual venues without structural change; the rule reads no volume, so venue volume-definition differences cannot touch it. The rule is two-sided with no stop leg, so a spot-only deployment expresses the long state and reversal-to-flat/short mechanics only to the extent the venue permits shorting — full two-sided expression assumes a futures venue, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived market and frame: the source names no market and no timeframe; this record pins `BTCUSDT 1d`. Cross-market and cross-frame behavior differences are real — the adaptation is disclosed, and this record makes no claim about any other market, frame, or the source's market-less performance.
- Derived fill timing: the source fills next-bar under Pine defaults with no timing argument; this record executes same-bar-close on `1d` BTCUSDT. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- No source economics: beyond Pine defaults the source ships no capital, commission, slippage, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- No price stop, no time stop, no post-placement flat: adverse excursion after placement has no guardrail beyond the opposite-threshold reversal; a position whose index never prints on the opposite side of `0.14` is held indefinitely. This is the coded posture, disclosed as the record's principal risk.
- Chop sensitivity: threshold flicker prints full reversals in ranging markets, and sustained convergence holds longs through distribution. The latch-plus-reversal construction is the coded design, disclosed, not smoothed.
- Slow seed: the 65-bar slow average dominates warmup; the first 75 `1d` bars are flat by record rule, so early-history signals never enter any evaluation.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- TradingView canonical strategy page (HPotter, 2017-10-13, full executable Pine verified live via the page's own open-source facade payload): https://www.tradingview.com/script/qMGsVEKk-Range-Action-Verification-Index-RAVI-Backtest/
- Pine strategy semantics (order calls, default execution, history-referencing semantics): https://www.tradingview.com/pine-script-reference/v5/
