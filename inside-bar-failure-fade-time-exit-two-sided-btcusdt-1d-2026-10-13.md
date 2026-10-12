---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Inside bar failure-fade with 3-bar time exit two-sided on BTCUSDT 1d bars
created: 2026-10-13
updated: 2026-10-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-09-14
sources:
  - https://www.fmz.com/strategy/426807
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/里向破坏策略Inside-Bar-Failure-Strategy.md
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Inside bar failure-fade with 3-bar time exit two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (immutable public mirror file plus its recorded FMZ canonical page, fetched 2026-10-13):

- Canonical page: https://www.fmz.com/strategy/426807 (fetched live over HTTPS during this cycle with HTTP 200, 738232 bytes of landing HTML). Author token `ChaoZhang` × 2; title token `Inside Bar Failure` × 8; executable-order tokens `strategy.entry` × 2; parameter token `Look Forward` × 7; stanza venue tokens `Futures_Binance` × 2 and `BTC_USDT` × 2. The ZH/EN prose states the rule plainly: check whether the prior two bars formed an inside bar (bar 2 high/low inside bar 1 range); a bar-3 high above bar 2 high that still closes above bar 2 low is a long signal; a bar-3 low below bar 2 low that still closes below bar 2 high is a short signal; positions may be closed a fixed number of bars later (e.g. 3). The page ships no performance numbers of any kind — this record claims no source-reported performance (see Evidence).
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (verified as the repository HEAD via `git ls-remote` during this cycle — the same head pin as the merged Bollinger-breakout, PVT-EMA, KDJ, STARC, T3-Tillson, WaveTrend, Qstick, Aroon, SQZMOM-LB, TRIX, Schaff, KST, OBV-EMA and eleven further admissions), exact file path `里向破坏策略Inside-Bar-Failure-Strategy.md` (2725 bytes, non-ASCII filename quoted verbatim, no encoding ambiguity). The mirror prints `> Author` = `ChaoZhang` (mirror porter), `> Detail` = https://www.fmz.com/strategy/426807, `> Last Modified` = `2023-09-14 16:43:52` (date part adopted as `source_as_of`), the `[trans]` ZH/EN prose matching the canonical page rule quoted above, a one-row Strategy Arguments table (`v_input_1 = 3`, `Look Forward`), and the complete executable Pine block.
- Full `//@version=3` block read in full (the entire 2725-byte file was retrieved; order-affecting lines are the `forward` input, the two `longCondition`/`shortCondition` definitions, the two `strategy.entry` legs, and the two `strategy.close` legs; everything else is declaration plumbing). The `/*backtest*/` stanza prints verbatim `start: 2022-09-07 00:00:00`, `end: 2022-10-31 23:59:00`, `period: 4d`, `basePeriod: 1d`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]` — the `4d` period label is non-standard and is quoted here exactly as printed, never normalized into a claim (see Execution assumptions for the adopted research frame).
- Text census over the pinned code block: 1 `strategy(` (title `Inside Bar Failure` / `overlay=true` plumbing only — no capital, cost, timing, or pyramiding argument ships anywhere in the declaration) / 2 `strategy.entry` (`"Long"`/`strategy.long`, `"Short"`/`strategy.short`, no `qty=`/`limit=`/`stop=`/`when=` qualifiers) / 2 `strategy.close` (`"Long"`, `"Short"`, no `when=` qualifier) / 0 `strategy.exit` / 0 `strategy.order` / 0 active `stop=`/`limit=`/`profit=`/`loss=` / 0 `plot`/`plotshape`/`bgcolor` (no display layer of any kind) / 0 `security(` / 0 `request.*` / 0 `timeframe(` / 0 `nz(` / 0 `var` / 0 `volume` / 0 `open` (only `high`/`low`/`close` series are read) / 0 `pyramiding` / 0 `process_orders_on_close` / 0 `initial_capital` / 0 `commission` / 0 `calc_on_every_tick`. No portable economics beyond the bare declaration stub ships anywhere — recorded as an absent-economics stub, never as zero-cost evidence.
- Licence and rights: the mirror block ships no licence header line; this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) market/frame pin `BTCUSDT 1d` (the executable stanza itself backtests `Futures_Binance BTC_USDT`; the stanza prints the non-standard `period: 4d` label quoted verbatim above — this record adopts the campaign `1d` decision frame because every order condition reads only completed-bar `high`/`low`/`close` comparisons, disclosed here, never presented as source-native); (2) completed-bar decisions with same-bar-close fills (the source ships no execution-timing argument — Pine default evaluates per completed bar and fills on the next bar; no `process_orders_on_close` ships anywhere, quoted verbatim in census — this record pins completed-bar evaluation with same-bar-close fills and claims no next-bar timing, disclosed here); (3) an adopted 10-bar warmup with pre-warmup bars flat by record rule (covers the `[2]` seed plus the 3-bar history reference with margin — see Required data); (4) house sizing/capital/costs replacing the absent source economics (see Execution assumptions). The inside-bar containment test, both failure-fade edges, the `forward = 3` time exit, the two-sided stance, the script-order entry-before-close sequencing, the pinned pyramiding-0 default, and the no-stop/no-target posture are source-native and unmodified. No tie-break had to be invented: the two entry edges are provably mutually exclusive on every bar including the degenerate flat print (see Negative evidence).

Pre-write dedup (2026-10-13): working-tree case-insensitive filename search for `inside` returns zero strategy records; content search for `inside bar` / `inside-bar` pool-wide hits only the dedup prose of `nr7-price-breakout-long-btcusdt-1d-2026-10-10.md` (its own pre-write search sentence, not a mechanism). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `nr7-price-breakout-long` buys the narrowest-range-of-seven breakout and follows it (7-bar contraction gate, 10-day time exit plus ATR stop, long-only); `donchian-20-10-breakout-btcusdt-1h-2026-10-06.md` buys every rolling-20-bar-high close with a 10-bar-low signal exit and no containment precondition; `darvas-box-breakout-long-btcusdt-1d-2026-10-09.md` follows confirmed box breakouts with an opposite-rail exit; `turtle-system-2-55d-breakout-2n-stop-half-n-add-two-sided-btcusdt-1d-2026-10-12.md` follows 55-day breakouts with a 2N stop and pyramided adds. Five-axis distinction: no pool record and no open PR conditions entries on a 2-bar inside containment whose one-sided probe fails back inside (fade, not follow), and none pairs that fade with a fixed 3-bar time exit, two-sided reversal entries, and zero protective-stop layer. Not a trivial parameter variant.

## Economic mechanism

### Source-reported

Failed-auction fade off a two-bar balance: an inside bar prints when the second bar's entire range is contained in the first — a completed two-sided auction with no new information. When the next bar probes one side of that balance (low under the inside low, or high over the inside high) but closes back inside it, the probe has failed: the breakout side found no continuation and the balance reasserts. The design fades the failed probe (long off the failed breakdown, short off the failed breakup) and holds at most three bars, on the premise that genuine post-balance trends declare themselves immediately while stale fades decay. The prose ships no stop, no target, no trailing: the 3-bar time exit plus the opposite-side reversal entry are the entire risk control.

### Research interpretation

Three-bar containment-failure machine, event-driven, two-sided, time-boxed. Unlike every breakout-follow record in the pool (Donchian, Darvas, Turtle-55d, NR7, BB-breakout) this system bets the other way: the entry requires the probe to fail, so clean follow-through breakouts that close outside the inside range fire nothing by construction. Unlike oscillator-cross systems there is no level, no smoothing, no band: the signal is pure bar-geometry (four strict inequalities plus one close test). Unlike stop-carrying records there is no protective leg: adverse excursion after entry has no guardrail beyond the 3-bar clock and the opposite fade, which reverses the book outright. The edge, if any, lives in the documented microstructure intuition that failed probes of fresh two-bar balances snap back within a handful of bars — a bet on hours-to-days mean reversion of probe extremes, not on any trend, level, indicator, calendar effect, or second timeframe.

## Signal

Exact rule as pinned (`forward = 3` frozen — any other value is a different, unpinned rule):

- Declarations (derived): two-sided long/flat/short machine over `BTCUSDT 1d` with same-bar-close execution and house sizing/costs (see Execution assumptions). State ∈ {flat, long, short}; both directions are live legs.
- Inside containment, pinned verbatim: bar `t-1` is inside bar `t-2` iff `high[t-2] > high[t-1]` and `low[t-2] < low[t-1]` (strict inequalities — a touch on either rail is not containment, and fires nothing).
- Entry long, pinned verbatim: `longCondition(t)` = containment and `low[t] < low[t-1]` (downside probe) and `high[t] < high[t-1]` (no upside break — the probe is one-sided) and `close[t] > low[t-1]` (close back above the probed rail — the failure). Live via `strategy.entry("Long", strategy.long)`, evaluated on the completed-bar close with same-bar-close execution under the derived declaration.
- Entry short, pinned verbatim: `shortCondition(t)` = containment and `high[t] > high[t-1]` (upside probe) and `low[t] > low[t-1]` (one-sided) and `close[t] < high[t-1]` (close back below the probed rail). Live via `strategy.entry("Short", strategy.short)` on the same completed-bar close.
- Time exit, pinned verbatim: `if longCondition[3]` → `strategy.close("Long")`; `if shortCondition[3]` → `strategy.close("Short")` — the position opened by a signal is closed in full exactly three completed bars later (no partial, nothing left behind), evaluated on that bar's close. `strategy.close` with no open position is a deterministic no-op.
- Reversal semantics, pinned as coded: both entry legs are live, so an opposite-side signal while positioned reverses the book in one event (closes the open side, opens the opposite side) per Pine `strategy.entry` default semantics; same-side repeat signals while positioned are rejected no-ops under the pinned pyramiding-0 default (see Execution assumptions). After any exit the next bar satisfying an entry edge enters immediately (no cooldown specified — explicitly none, not invented).
- Script order, pinned as coded: entries precede closes in the block, so a bar that both carries a fresh signal and closes a 3-bar-old signal opens-then-closes within the same event — net flat by the close with two same-bar fills (see Negative evidence). Deterministic by script order, never ambiguous.
- Display isolation: the block contains zero plot-family calls — there is no display layer capable of influencing any order condition.

## Required data

- Completed `1d` bars of BTCUSDT: `high` (containment rails and probe tests), `low` (containment rails and probe tests), `close` (failure confirmation). No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d`. The script takes no timeframe input and makes no live `request.*`/`security(`/`timeframe(` call, so it is single-frame by construction; `1d` is adopted as the research frame because it is a campaign timeframe and the bar-geometry logic is frame-agnostic — never presented as anything beyond that (see Limitations).
- Warmup: each signal reads bars `t`, `t-1`, `t-2`, so the first signal-eligible bar is the 3rd completed `1d` bar; the time exit reads a 3-bar-old signal value (pure history reference, no future). This record adopts a 10-bar warmup with pre-warmup bars flat by record rule, covering the seed with margin. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT under the house overlay (the rule reads completed-bar high/low/close only; venue transfer is never presented as source-native semantics).
- Order timing (predeclared derivation): completed-bar decisions with same-bar-close fills, 1:1 compatible with the pinned Hummingbot backtester. The source's own timing is next-bar-open (no timing argument ships — quoted verbatim in Provenance); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill. Zero `strategy.exit` calls, hence no stop/limit order and no same-bar TP/SL ordering ambiguity anywhere in the rule; the only same-bar sequencing is the coded entry-before-close order (see Signal), which resolves deterministically to a costed round trip.
- Sizing/capital: the source declaration carries no quantity, capital, or cost rule of any kind, replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions, never presented as source-native behavior.
- Concurrency: `pyramiding` is unset (Pine v3 default 0: no same-direction add while positioned). The default is load-bearing and therefore pinned explicitly: repeat same-side signals during an open position are rejected no-ops; opposite-side signals reverse in one event; re-entry is allowed immediately on the next qualifying edge after any exit (no cooldown — explicitly none). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The canonical page ships the inside-bar definition, the two one-sided-probe-plus-close-back-inside signal rules, the fixed-N-bars-later close (`Look Forward`, default 3), both trading directions, and prose risk guidance (probe validity needs further verification; setups are infrequent; trend-counter trades possible). It ships zero performance numbers: no return, no win rate, no profit factor, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=` — the 3-bar time close plus opposite-side reversal are the sole position-ending paths by construction, and the prose promises no stop or target.
2. Entry edges are mutually exclusive on every bar: long requires `high[t] < high[t-1]` while short requires `high[t] > high[t-1]` — no single print satisfies both, so no same-bar long-vs-short ordering ambiguity exists to resolve.
3. Strict containment and strict probes: equality on any rail (`high[t-2] == high[t-1]`, `low[t] == low[t-1]`, `close[t] == low[t-1]`) fires nothing; a zero-range mother bar can still contain (both strict inequalities hold vacuously only if the inside bar is strictly smaller — otherwise nothing fires). Ties are dead bars, pinned, not smoothed.
4. Same-bar open-plus-time-close determinism: a bar carrying both a fresh signal and the 3-bar-lagged close of an older signal executes entry-then-close in script order — net flat by the close with two fills, costed twice under the house overlay. Resolved by code order, never guessed.
5. Flat-state determinism: `strategy.close("Long"/"Short")` with no open position is a no-op; `strategy.entry` while already positioned same-side is rejected under pinned pyramiding 0; the seed bars satisfy no order condition by themselves (every edge needs bars `t-1` and `t-2`).
6. The window (`[2]` seed, `[3]` exit lag), the `forward = 3` input, both directions, and the no-stop posture are pinned, not removed: retuning the hold length, adding a stop/target/cooldown/session filter, enabling `reverse`-style inversion, or widening containment to touches would each be a different, unpinned rule — none is admitted here.
7. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT-`1d` research frame (against the stanza's verbatim `period: 4d` label), same-bar-close fills, the 10-bar warmup, and house sizing/costs — all predeclared above; every edge, input, default, ordering, and risk posture is source-verbatim. This record is therefore never evidence that the original next-bar-open source itself passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 2-bar strict containment / one-sided probe / close-back-inside fade / `forward = 3` / two-sided with reversal / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Fade relevance: entering WITH the probe direction (breakout-follow: long on upside break, short on downside break) instead of fading it must not improve net expectancy; fail ⇒ the failure-fade adds nothing over naive inside-bar breakout-following.
- F2 — Time-box relevance: holding each entry until the opposite fade signal (no 3-bar clock) instead of the coded time exit must not improve net expectancy; fail ⇒ the 3-bar box adds nothing over signal-only exits.
- F3 — Containment relevance: admitting rail-touch bars (`<=`/`>=`) as inside bars instead of the strict containment must not improve net expectancy; fail ⇒ the strict two-bar balance definition adds nothing over loose range-overlap trading.

## Crypto portability

Pinned to BTCUSDT under the house overlay. The high/low/close-only two-sided logic ports to perps or spot without structural change for the long legs; the short legs require a short-capable venue (perps under the house overlay — short legs on spot-only deployment are explicitly out of scope, not silently dropped). No funding-dependent leg, no stablecoin-specific assumption, no session, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (`open` is never referenced), so session-gap behavior is simply absent rather than approximated; inside bars form purely on printed range containment. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source fills next-bar-open; this record executes same-bar-close. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- Derived research frame: the stanza prints the non-standard `period: 4d` label (quoted verbatim, never normalized); this record decides on `1d`. Bar-geometry transfers mechanically across frames, but the trade population of 4d-labeled bars versus 1d bars differs by construction.
- Time-boxed blind clock: every position dies at 3 bars regardless of probe quality; a genuine post-balance trend is exited while running, and chop prints alternating fade/reversal round trips — the coded cost of the design, disclosed, not smoothed.
- No price stop: adverse excursion after entry has no guardrail beyond the 3-bar clock and the opposite reversal; a vertical-against move is held to the clock.
- Infrequent setups by source admission: strict 2-bar containment plus one-sided failed probes are rare events; evaluation windows contain long flat stretches, and reversal entries can flip the book on consecutive bars in probe-heavy chop.
- Performance evidence is absent: the canonical page reports no numbers at all; nothing here is calibrated, fitted, or tuned to any backtest.

## Implementation status

Not implemented. No Hummingbot/Qlib/n8n execution, no Paper/Testnet/Live run, no parameter tuning, no independent reproduction — per the Scout contract the record stops at admission review.

## Adoption boundary

Research-only, not approved for any adoption scope. A PASS here means admissibility to model-consistent research under the pinned Hummingbot benchmark — not profitability, not Qlib parity, not Paper/Testnet/Live permission. Any downstream use requires its own separate authorization outside this repository's admission lane.

## Related Wiki records

None — per the Scout contract no Wiki Brain write is performed in this lane.

## Sources

- FMZ canonical strategy page (primary rule prose + backtest stanza): https://www.fmz.com/strategy/426807
- Immutable code mirror (primary executable rule, commit `7853bb2bf262c4567ac238d3552d97f0e50cb801`, path `里向破坏策略Inside-Bar-Failure-Strategy.md`): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/里向破坏策略Inside-Bar-Failure-Strategy.md
- Pine Script strategy semantics reference (order/timing defaults): https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
