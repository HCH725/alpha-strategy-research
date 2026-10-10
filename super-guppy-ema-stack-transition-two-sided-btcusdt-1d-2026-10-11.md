---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Super Guppy 22-EMA rank-stack transition reversal two-sided on BTCUSDT 1d bars
created: 2026-10-11
updated: 2026-10-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-09-02
sources:
  - https://www.tradingview.com/script/vPStjyWz-Super-Guppy-Strategy/
  - https://github.com/hasnocool/tradingview-pine-scripts/blob/main/Super%20Guppy%20Strategy.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Super Guppy 22-EMA rank-stack transition reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (verified 2026-10-11):

- Canonical page: https://www.tradingview.com/script/vPStjyWz-Super-Guppy-Strategy/ (page title `Super Guppy Strategy by StanleyBostich`, author `StanleyBostich`, open-source strategy; header prose: `CM Super Guppy with Long/Short signals, backtesting, and additional options. Updated for PineScript v4. COINBASE:BTCUSD`; description snippet confirms the gray-transition close behavior and the gray-to-green long open pinned below). Direct page-HTML fetch from this network is refused by TradingView (HTTP 403 for both curl and the cloud browser backend), so no order-gating line is claimed from page HTML — every order-gating line below was read verbatim from the immutable mirror artifact instead, quoted in census.
- Pinned executable artifact (immutable GitHub implementation, full `//@version=4` block read line by line): https://github.com/hasnocool/tradingview-pine-scripts/blob/main/Super%20Guppy%20Strategy.pine at commit `e031cab2819a7d56fb8bb9d000252f51439986e2` (2023-09-02, adopted as `source_as_of`), whose header preserves the canonical identity verbatim (`Script Name: Super Guppy Strategy`, `Author: StanleyBostich`, `CM Super Guppy with Long/Short signals, backtesting, and additional options. Updated for PineScript v4. COINBASE:BTCUSD`): `strategy(title="Super Guppy Strategy", shorttitle="Super Guppy Strat", overlay = true, initial_capital=100000, default_qty_type = strategy.percent_of_equity, default_qty_value = 100, commission_type="percent", commission_value=0.0)`, the `src = close` declaration, all 23 EMA lengths, the fast/slow rank-order color rules, the `var isLong / var isShort` latch, the `long`/`short` transition signals, all eight order legs, and the display-only plots/plotshapes. No login wall stands between the reader and any order-gating line: every line that can open, close, or size a position was read verbatim from the pinned artifact.
- Text census over the pinned code block: 4 `strategy.entry` (`"LONG"` long / `"short"` short, each once for the `not useEarlySignals` branch and once for the `useEarlySignals` branch, no price argument) / 4 `strategy.close` (same branch doubling) / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `volume` (the rule reads `close` only — every EMA is `ema(src, lenN)` with `src = close`; neither `open`, `high`, `low`, nor `volume` appears in any order-gating line) / `time`/`timenow` appear exactly once, only in the inert backtest-window gate disclosed below / `process_orders_on_close` unset (Pine default: signals evaluate per completed bar, fills on the next bar) / `pyramiding` unset (Pine default: no same-direction adds) / economics arguments present but empty (`initial_capital=100000`, 100% equity, `commission_value=0.0` — recorded as absent economics, never as zero-cost evidence; see Execution assumptions).
- No risk layer ships anywhere in the source: zero stop/target/trailing/time-exit order legs — the no-stop/no-target posture below is therefore the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention.
- Page performance language is absent entirely (no table, figure, or number) — this record claims no source-reported performance and no reproduced performance. The source names no timeframe in code (chart prose says `COINBASE:BTCUSD` only) — the `BTCUSDT 1d` pin below is a fully researcher-declared derivation choice, disclosed here, never presented as a source claim.

Licence and rights: this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) market/frame pin `BTCUSDT 1d` (the code names no market and no timeframe at all — this pin is a pure researcher choice, disclosed here, never presented as source-native); (2) same-bar-close fills (the source ships no execution-timing argument — Pine default fills evaluate per completed bar and fill on the next bar; no `process_orders_on_close` ships anywhere, quoted verbatim in census); (3) an adopted 80-bar warmup with pre-warmup bars flat by record rule (covers the 66-bar slowest-EMA seed plus margin — see Required data) and house sizing/capital/costs replacing the absent source economics (the source ships `commission_value=0.0` and no funding/margin assumption at all — see Execution assumptions). The pinned input defaults (`useShorts=true`, `useEarlySignals=true`, all 23 EMA lengths, `show200Ema=false`), the 22-EMA rank-order stack state machine, the gray-transition entries, the opposite-signal close/reversal handling, the order IDs, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-11): working-tree case-insensitive search for `guppy`, `gmma`, `stanleybostich`, and `vpstjywz` returns zero hits anywhere outside scratch — no admitted rule uses this source, author strategy, indicator, or mechanism. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closed research PR titles contain no Guppy record. Closest pool records are different mechanism classes: `alligator-smma-stack-long-flat` is a 3-line displaced-SMMA jaw/teeth/lips stack, long-flat only (this rule is a 22-EMA strict rank-order stack with gray-transition entries, two-sided with reversal exits — never a 3-line displacement stack); `ema-cloud-7-20-trend` and `ema-20-50-cross` are two-line cross systems (this rule never trades a cross — its only trigger is whole-stack rank-order transitions); `triple-ema-volstop-tp-long` adds a VolStop trailing exit (this rule has no trailing leg at all). Five-axis distinction: mechanism differs (slow-group 15-EMA perfect-order state machine with fast-group agreement coloring and latched gray-transition entries — versus crosses, displacement stacks, or trailing-stop systems), signal construction differs (no pool record computes 22 close-EMAs with strict `ema8 > ... > ema22` / `ema8 < ... < ema22` ordering tests), trigger differs (gray-to-lime and red-to-gray bar transitions with `isLong`/`isShort` latching — not a cross, not a threshold, not a band touch), data differs (close only; no high, low, volume, or multi-frame read), and source identity differs (StanleyBostich Super Guppy Strategy, TV `vPStjyWz`, mirror pin `e031cab`).

## Economic mechanism

### Source-reported

Trader/investor agreement stack (code structure plus header prose, no performance section ships): 7 fast EMAs (3–21) track short-term trader consensus and 15 slow EMAs (24–66) track long-term investor consensus; when every slow EMA stands in perfect ascending rank order the investor group is in full bullish agreement (`lime`), when perfectly descending it is in full bearish agreement (`red`), and any disorder is disagreement (`gray`). Entries fire only on agreement transitions — gray-to-lime opens longs, gray-to-red opens shorts, and in the pinned early-signals mode the resolution of the opposite extreme (red-to-gray, lime-to-gray) also enters, on the bet that the end of one-sided agreement is the earliest tradable edge of the turn. The design bets that whole-group rank-order persistence predicts continuation, and expresses that bet as a latched two-sided state machine, not as one-shot crosses.

### Research interpretation

Rank-order stack transition system, two-sided with opposite-signal close/reversal exits and an explicit pre-first-signal flat state. Unlike cross systems that trade the moment one line passes another, this rule never trades a cross at all: its only comparisons are strict inequalities across 22 EMAs, and the `isLong`/`isShort` latch makes every non-transition bar a hold, not a decision. Unlike always-in-market flip systems, the rule rests flat before the first transition (both latch vars seed `false`, and no transition can print before seeded EMAs disagree-then-agree). Note the asymmetry the source pins plainly: in the pinned early mode, longs fire on gray-to-lime (fresh agreement) OR red-to-gray (bearish agreement dissolving) — the long state is therefore entered both at trend birth and at trend death, and shorts mirror it. The price of the stack is chop bleed: a whipsawing slow group that flickers between ordered and disordered prints full long/short reversals at the worst prints of each flicker, and a perfectly ordered stack holds the position into the teeth of a top with no stop anywhere. The bet is on group-agreement persistence, not on any reversal level, volume print, mean-reversion extreme, or calendar effect.

## Signal

Exact rule as pinned (all 23 lengths, `useShorts=true`, `useEarlySignals=true`, `show200Ema=false` frozen — any other value is a different, unpinned rule):

- Declaration (derived): `strategy(title="Super Guppy Strategy", shorttitle="Super Guppy Strat", overlay = true)` semantics preserved with the derived `BTCUSDT 1d` market/frame pin and same-bar-close execution adopted (no such timing argument ships in the source) and house sizing/costs replacing the absent source economics (see Execution assumptions). Pine-default no-pyramiding semantics hold (no `pyramiding` argument ships): at most one open position, same-direction refires are no-ops, opposite entries reverse in full.
- Stack (pinned): `src = close`; fast EMAs `ema(src, 3/6/9/12/15/18/21)`; slow EMAs `ema(src, 24/27/30/33/36/39/42/45/48/51/54/57/60/63/66)`; `EMA 200` (`ema(src,200)`) ships display-only under `show200Ema=false` (plots `na`) and never enters any order-gating line. Fast-bullish `colfastL` requires all 7 fast EMAs strictly descending in length order (`ema1 > ema2 > ... > ema7`); slow-bullish requires all 15 slow EMAs strictly ordered (`ema8 > ema9 > ... > ema22`); bearish states mirror with strict `<`. No zero-guard ships anywhere; on any traded market all inputs are positive seeded EMAs of positive closes, and an `na` print would fail every strict inequality and hold the prior latch state by construction (see Negative evidence). Every input is a completed bar's `close`; no `open`, `high`, `low`, or `volume` is read.
- State color (pinned): `colFinal2 = lime` iff slow-bullish, `red` iff slow-bearish, else `gray` — exactly one of three per bar, mutually exclusive by construction (both strict orderings cannot hold simultaneously).
- Transition signals, early mode (pinned): `long = not isLong and ((lime and prev gray) or (gray and prev red))`; `short = not isShort and ((gray and prev lime) or (red and prev gray))`; the `if long / if short` blocks latch `isLong`/`isShort` so each transition enters once. `long` and `short` cannot fire on the same bar (their color-transition pairs are disjoint).
- Entry long: `strategy.entry("LONG", strategy.long)` under `when=long and isWithinTimeBounds and useEarlySignals` — fires on gray-to-lime or red-to-gray transitions, with same-bar-close execution under the derived declaration. Refires while already long are no-ops under default no-pyramiding semantics.
- Entry short: `strategy.entry("short", strategy.short)` under `when=short and useShorts and isWithinTimeBounds and useEarlySignals` — mirror transitions; from flat it opens short, from long it reverses to short in full (a coded position-closing path, not invented). The `useShorts=false` setting would disable the short leg and is a different, unpinned rule.
- Exits: `strategy.close("LONG", when=short and ...)` closes longs on the opposite transition, and the opposite `strategy.entry` reverses in full — the sole position-closing paths, both coded. (The `not useEarlySignals` close legs are inert under the pinned `useEarlySignals=true`; disclosed, never relied upon.)
- Direction: two-sided with an explicit pre-first-signal flat state (both latch vars seed `false` and no transition can fire before the first gray-to-ordered or ordered-to-gray print; before that, no order can fire). After the first transition the system is always in market (long or short) — there is no coded flat state beyond the seed, disclosed, not enabled.
- Time-window isolation: `isWithinTimeBounds` reads `time`/`timenow` against the default `daysBackMax=100000` / `daysBackMin=0` inputs — under pinned defaults the window spans ~100,000 days back from now and is therefore always true on any traded history (inert, disclosed, never an order-gating signal). Display isolation: all `plot`/`plotshape`/color assignments render only and cannot change any order. No stop, no target, no trailing, no time exit, no cooldown — pinned as written, explicitly none, not invented.

## Required data

- Completed `1d` bars of BTCUSDT: `close` (only indicator input, read 22 times via the fast/slow EMA stacks; the 200-EMA reads `close` display-only under pinned `show200Ema=false`). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (derived pin; the script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction).
- Warmup: the slowest EMA-66 seed needs 66 completed `1d` bars — binding constraint is bar index ≥ 66 before every referenced value is seeded (all shorter EMAs are absorbed inside it; EMAs seed recursively from the first bar, so no `na` seeding gap exists beyond it). The adopted warmup is the first 80 completed `1d` bars flat by record rule (predeclared researcher choice — covers seed plus margin). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Each bar's close enters the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (derived pin; the source chart prose says `COINBASE:BTCUSD` and the code names no market and no timeframe — venue choice and symbol spelling are disclosed here, never presented as a source claim).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar fill (no execution-timing argument ships anywhere — quoted verbatim in census); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. On a transition bar the close leg and the opposite entry leg fire together as one atomic reversal event — no same-bar double-fill ordering exists beyond that single reversal under either evaluation order.
- Sizing/capital/costs: the source ships no usable economics (`initial_capital=100000`, 100% equity quantity, `commission_value=0.0`, no funding, no margin assumption — quoted verbatim in census; the zero commission is disclosed, never read as zero-cost evidence) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: Pine-default no-pyramiding semantics hold — at most one open position under the fixed order IDs `LONG`/`short`; same-direction refires while already positioned are no-ops by the pinned default (reinforced by the `isLong`/`isShort` latch, which blocks repeat transition entries), the opposite entry reverses in full (a coded position-closing path), an entry while flat opens, and re-entry is allowed immediately on the next qualifying transition after any reversal (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (22 order-driving close-EMAs at pinned lengths 3–66 plus display-only EMA-200, strict rank-order fast/slow color rules, three-state `colFinal2` machine, `isLong`/`isShort` latch, `long`/`short` transition signals, eight order legs across the two mode branches, fixed `LONG`/`short` order IDs, inert-by-default time window), the active `strategy(...)` declaration, the `Super Guppy Strategy` / `Super Guppy Strat` titles, and the pinned input defaults. It ships zero performance numbers and names zero timeframes in code: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=` — the position-closing paths are the coded opposite-transition `strategy.close` legs plus full reversal via the opposite `strategy.entry`. The absence is coded (the order block is followed only by display code in evaluation order) and the header carries no risk leg anywhere.
2. Coded rule is a rank-order stack, not a cross, stated plainly: no `crossover(`/`crossunder(` call appears anywhere in the source; the only comparisons are strict `>`/`<` chains across the 22 EMAs plus equality-free color transitions. Substituting any two-line cross would be a different, unpinned rule.
3. No future leakage in the stack, stated plainly: at decision bar `t`, every EMA reads completed closes through `t` — every input is a completed historical bar. No `security()`, no `request.*`, no negative index, no `barstate.islast`-gated repainting path. The `time`/`timenow` read is an inert always-true window under pinned defaults, never a signal.
4. Same-bar signal exclusivity fenced: the `long` and `short` transition pairs (`lime&prev-gray` / `gray&prev-red` versus `gray&prev-lime` / `red&prev-gray`) are disjoint by the three-state color, so at most one entry leg can fire on any bar. Deterministic under either fill convention.
5. Two-sided posture provably complete: both `strategy.long` and `strategy.short` appear in the pinned branch, each under its own guarded `when=`; no third direction exists. The `useShorts` switch is pinned `true` — disabling it would be a different, unpinned rule.
6. Stack-flicker whipsaw, admitted plainly: a slow group oscillating between ordered and disordered prints full long/short reversals at the worst prints of each flicker, and a perfectly ordered stack holds the position through distribution. There is no confirmation filter, no stop, and no flat state after the first transition — the coded posture, disclosed as the record's principal risk.
7. The close-only 22-EMA stack, all pinned lengths, the strict rank-order inequalities, the three-state color, the `useShorts=true` / `useEarlySignals=true` settings, the latched gray-transition entries, the fixed `LONG`/`short` order IDs, the opposite-signal close/reversal exits, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning any length, converting the stack into a cross, disabling early signals or shorts, adding a stop/target/filter/cooldown, or enabling the 200-EMA as a filter would each be a different, unpinned rule — none is admitted here.
8. Derivation boundary fenced: the only non-source-native behaviors in this record are the `BTCUSDT 1d` market/frame pin, same-bar-close fills, the adopted 80-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the EMA stack, lengths, color rules, latch, transitions, order IDs, reversal handling, and risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, or timing of the source passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: close-only 22-EMA rank-order stack / pinned lengths / `useShorts=true` / `useEarlySignals=true` / latched gray-transition entries / opposite-signal close-reversal exits / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Direction relevance: inverting the side mapping (gray-to-lime short, gray-to-red long, same latch mechanics) must not improve net expectancy; fail ⇒ the coded agreement direction adds nothing over its mirror.
- F2 — Early-signal relevance: replacing the pinned early transitions with the non-early pair (long only on gray-to-lime, short only on gray-to-red, same exits) must not improve net expectancy; fail ⇒ the coded early entries (red-to-gray longs, lime-to-gray shorts) are dominated by the stricter fresh-agreement-only construction the page prose emphasizes.
- F3 — Stack relevance: replacing the 15-EMA strict slow stack with a single `ema(close,30) > ema(close,60)` trend gate (same transitions, entries, and exits) must not improve net expectancy; fail ⇒ the coded whole-group rank ordering adds nothing over its two-line twin.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (derived pin; the code names no market at all and the chart prose says `COINBASE:BTCUSD`). The close-price arithmetic ports across perpetual venues without structural change; the rule reads no volume, so venue volume-definition differences cannot touch it. The rule is two-sided with no stop leg, so a spot-only deployment expresses the long state and reversal-to-flat/short mechanics only to the extent the venue permits shorting — full two-sided expression assumes a futures venue, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no session gating anywhere beyond the inert always-true window), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived market and frame: the code names no market and no timeframe; this record pins `BTCUSDT 1d`. Cross-market and cross-frame behavior differences are real — the adaptation is disclosed, and this record makes no claim about any other market, frame, or the source's market-less performance.
- Derived fill timing: the source fills next-bar under Pine defaults with no timing argument; this record executes same-bar-close on `1d` BTCUSDT. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- No source economics: the source ships only demo economics (`initial_capital=100000`, 100% equity, `commission_value=0.0`) with no funding or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- No price stop, no time stop, no post-transition flat: adverse excursion after entry has no guardrail beyond the opposite-transition close/reversal; a position whose stack never prints the opposite transition is held indefinitely. This is the coded posture, disclosed as the record's principal risk.
- Chop sensitivity: stack flicker prints full reversals in ranging markets, and a perfectly ordered stack holds positions through distribution. The stack-plus-reversal construction is the coded design, disclosed, not smoothed.
- Slow seed: the 66-bar slowest average dominates warmup; the first 80 `1d` bars are flat by record rule, so early-history signals never enter any evaluation.
- Network limitation disclosed: TradingView page HTML could not be fetched from this runner (HTTP 403); canonical identity (title/author/open-source status/description) is verified via the stable-URL search record and the mirror's verbatim header, and every order-gating line is verified from the immutable mirror artifact at pinned SHA — never from memory or paraphrase.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- TradingView canonical strategy page (StanleyBostich; stable URL identity and description verified via indexed page record; page HTML refused from this network, disclosed above): https://www.tradingview.com/script/vPStjyWz-Super-Guppy-Strategy/
- Immutable GitHub implementation (full executable Pine read end to end at pinned SHA `e031cab2819a7d56fb8bb9d000252f51439986e2`, 2023-09-02): https://github.com/hasnocool/tradingview-pine-scripts/blob/main/Super%20Guppy%20Strategy.pine
- Pine strategy semantics (order calls, default execution, history-referencing semantics): https://www.tradingview.com/pine-script-reference/v5/
