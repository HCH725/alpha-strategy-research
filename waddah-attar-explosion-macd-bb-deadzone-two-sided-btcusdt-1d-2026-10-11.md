---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Waddah Attar Explosion MACD-BB deadzone reversal two-sided on BTCUSDT 1d bars
created: 2026-10-11
updated: 2026-10-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-04-18
sources:
  - https://www.tradingview.com/script/d9IjcYyS-Waddah-Attar-Explosion-V2-SHK/
  - https://github.com/edyatl/waddah-attar-explosion
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Waddah Attar Explosion MACD-BB deadzone reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (verified 2026-10-11):

- Canonical script page: https://www.tradingview.com/script/d9IjcYyS-Waddah-Attar-Explosion-V2-SHK/ (`Waddah Attar Explosion V2 [SHK]`, crypto-market adaptation of LazyBear's MT4-ported Waddah Attar Explosion; stable-ID form of the `ru.tradingview.com/script/d9IjcYyS-Waddah-Attar-Explosion-V2-SHK/` URL quoted verbatim in the pinned port's docstring). The script page carries the full ENTER_BUY / EXIT_BUY / ENTER_SELL / EXIT_SELL prose pinned below. Direct page-HTML fetch from this network is refused by TradingView (HTTP 403 pattern on this runner), so no line is claimed from page HTML — every formula and every gating line below was read verbatim from the immutable GitHub artifact instead, quoted in census.
- Pinned executable artifact (immutable GitHub source, full original Pine block read line by line): https://github.com/edyatl/waddah-attar-explosion at commit `928f43180f72ab1f8537c9faf6c78cd4258969f7` (2023-04-18, adopted as `source_as_of`), whose `README.md` quotes the complete `study("Waddah Attar Explosion V2 [SHK]", shorttitle="WAE [SHK]")` block verbatim (header credits `// @author LazyBear` and `// Modified for Crypto Market by ShayanKM` preserved) and whose `wae.py` docstring pins the same canonical script URL. The quoted Pine is an indicator `study()`, not a `strategy()` — there are no `strategy.entry`/`strategy.close`/`strategy.exit` legs to census; the order-gating behavior comes from the script page's explicit ENTER/EXIT prose, quoted verbatim below, executed here through the predeclared derived single-position state machine.
- Text census over the quoted Pine block: 1 `study(` / 0 `strategy(` / 0 `strategy.entry` / 0 `strategy.close` / 0 `strategy.exit` / 0 `strategy.order` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `volume` (indicator inputs are `close` for MACD/BB plus `high`/`low`/`close` inside `tr(true)` for the dead zone — neither `open` nor `volume` appears anywhere) / 0 `time`/`timenow` / inputs pinned verbatim (`sensitivity=150`, `fastLength=20`, `slowLength=40`, `channelLength=20`, `mult=2.0`) / formulas pinned verbatim (`DEAD_ZONE = nz(rma(tr(true),100)) * 3.7`, `t1 = (calc_macd(close, fastLength, slowLength) - calc_macd(close[1], fastLength, slowLength))*sensitivity`, `e1 = (calc_BBUpper(close, channelLength, mult) - calc_BBLower(close, channelLength, mult))`, `trendUp = (t1 >= 0) ? t1 : 0`, `trendDown = (t1 < 0) ? (-1*t1) : 0`, sienna `ExplosionLine` plot of `e1`, blue cross `DeadZoneLine` plot).
- Source-reported ENTER/EXIT prose (pinned artifact `README.md`, `Original Indicator Overview`, quoted for gate evidence — this is the complete trading rule as the source states it): ENTER_BUY requires all four of (a) green histogram rising, (b) green histogram above the Explosion line, (c) Explosion line rising, (d) both green histogram and Explosion line above the Dead Zone line. EXIT_BUY: exit when the green histogram crosses below the Explosion line. ENTER_SELL mirrors with the red histogram (rising, above Explosion, Explosion rising, both above Dead Zone). EXIT_SELL: exit when the red histogram crosses below the Explosion line. Dead-zone veto stated plainly: "Trades should not be taken when the red or green histogram is below this line." No stop, no target, no trailing, no time exit, no pyramiding statement ships anywhere — the no-stop/no-target posture below is the prescribed posture pinned as written (declared explicitly, never hidden), not a researcher invention.
- Page performance language is absent entirely (no table, figure, or number) — this record claims no source-reported performance and no reproduced performance. The indicator names no market and the overview calls the 30-minute frame "best suited" without coding any timeframe — the `BTCUSDT 1d` pin below is a fully researcher-declared derivation choice, disclosed here, never presented as a source claim.

Licence and rights: this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly five: (1) market/frame pin `BTCUSDT 1d` (the overview suggests 30-minute use in prose only; the code names no market and no timeframe — this pin is a pure researcher choice, disclosed here, never presented as source-native); (2) rising-edge event semantics for the four-condition entries (the prose states level conditions that persist across bars; firing every bar would re-enter continuously, so this record fires on the first bar of each conjunction — predeclared here, never presented as source-native); (3) a single-position state machine with exit-before-entry ordering and atomic same-bar reversal (the `study()` ships no position handling at all — at most one open leg, same-direction refires are no-ops, opposite-leg edges reverse in full; see Signal); (4) same-bar-close fills with house sizing/costs replacing the absent source economics; (5) an adopted 120-bar warmup with pre-warmup bars flat by record rule (covers the 100-bar dead-zone seed plus margin — see Required data). The pinned input defaults, all five formulas, the four-condition entries, the histogram-cross exits, the dead-zone veto, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-11): working-tree case-insensitive searches for `waddah`, `shayankm`, `lazybear` (as signal author), `dead-zone`/`deadzone` (as a volatility-filter line), and `d9ijcyys` return zero strategy records using this source, author script, indicator, or mechanism — the only hits are passing mentions inside older records' dedup paragraphs (McGinley zero-hit probe, StochRSI/QQE lineage notes) and generic prose words (`dead-band`, `explosion` as ordinary volatility prose in P-Signal/SQZMOM records), never a MACD-difference histogram against a Bollinger-width explosion line with a true-range dead zone. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closed research PR titles contain no Waddah record. Closest pool records are different mechanism classes: `qqe-fast-slow-cross-two-sided-btcusdt-1d` crosses two RSI-smoothing lines (no MACD-difference histogram, no Bollinger-width line, no dead zone); `macd-signal-cross-reversal-btcusdt-1d` crosses a MACD line against its own signal average (no explosion line, no rising-conjunction, no dead-zone veto); `alma-cross-volume-gate-btcusdt-1d` gates a two-average cross on volume (volume never enters this rule's arithmetic). Five-axis distinction: mechanism differs (momentum-acceleration histogram confirmed by volatility-width expansion with an absolute-volatility dead-zone veto — versus line crosses or volume gates), signal construction differs (no pool record computes `(macd(t) − macd(t−1)) × 150` against `4 × stdev(close,20)` with an `rma(tr,100) × 3.7` veto), trigger differs (four-condition rising-edge conjunction — not a cross, not a threshold, not a band touch), data differs (`close` plus `high`/`low` via true range only; no `open`, no `volume`, no multi-frame read), and source identity differs (LazyBear/ShayanKM WAE V2 lineage via edyatl pin `928f431` and TV `d9IjcYyS`).

## Economic mechanism

### Source-reported

Explosion-confirmed momentum with a volatility-mute veto (overview prose plus quoted Pine, no performance section ships): `t1` is the one-bar change of the 20/40 MACD scaled by 150 — a momentum-acceleration histogram, green when MACD is rising (`t1 ≥ 0`), red when falling. `e1` is the full width of a 20-bar 2σ Bollinger Band on `close` — the "explosion" line that expands only when realized volatility breaks out. The Dead Zone (`3.7 ×` Wilder-smoothed true range over 100 bars) mutes everything below the market's own recent volatility size. A buy is taken only when acceleration is positive AND rising, volatility is expanding AND rising, and both clear the market's own noise floor — the design bets that trend legs worth holding begin as jointly-confirmed acceleration-plus-expansion events, and that anything weaker is chop to be filtered, not traded. Exits are symmetric polis: the moment the histogram sinks back below the explosion line, the expansion thesis is dead and the leg closes.

### Research interpretation

Four-condition conjunction system, two-sided with histogram-cross exits and an explicit pre-warmup flat state. Unlike cross systems that trade the moment one line passes another, this rule never trades a bare cross: its entries require acceleration (`t1`), expansion (`e1`), both rising, and both above an absolute-volatility floor — five strict comparisons must agree on the same bar. Unlike always-in-market flip systems, the rule rests flat whenever neither conjunction edge fires and whenever a leg's histogram sinks below the explosion line. Note the asymmetry the source pins plainly: entries demand full conjunction, exits demand only the single histogram-below-explosion print — a leg entered on five agreements can be closed by one disagreement, so the system is trigger-shy and exit-hasty by construction. The price of the dead zone is missed slow-burn trends: a grinding trend whose histogram never clears `3.7 ×` recent true range never enters at all, and a volatility spike that inflates `e1` faster than `t1` blocks entries at exactly the breakout moment the rule was built to catch. The bet is on jointly-confirmed acceleration-plus-expansion, not on any reversal level, volume print, mean-reversion extreme, or calendar effect.

## Signal

Exact rule as pinned (all five inputs frozen — any other value is a different, unpinned rule):

- Declarations (derived): single-position state machine over `BTCUSDT 1d` with same-bar-close execution and house sizing/costs (see Execution assumptions). At most one open leg; state ∈ {flat, long, short}.
- Indicator stack (pinned): `macd(t) = ema(close,20) − ema(close,40)`; `t1(t) = (macd(t) − macd(t−1)) × 150`; `e1(t) = 4 × stdev(close,20)` (upper-minus-lower Bollinger width at `mult=2.0`); `trendUp(t) = max(t1(t), 0)` (green); `trendDown(t) = max(−t1(t), 0)` (red); `DZ(t) = rma(tr(true),100) × 3.7` where `tr` is the true range of `high`/`low`/`close`. `stdev` is the Pine biased (population) standard deviation; `rma` is Wilder smoothing; `nz()` converts the pre-seed `na` prints to 0 — under the adopted 120-bar warmup every series is seeded before any evaluation, so the `nz` branch never fires on a traded bar (see Required data). Every input is a completed bar's `close`/`high`/`low`; no `open` and no `volume` is read.
- Buy-edge (derived edge of the source-native conjunction): `E_L(t) = (trendUp(t) > trendUp(t−1)) ∧ (trendUp(t) > e1(t)) ∧ (e1(t) > e1(t−1)) ∧ (trendUp(t) > DZ(t)) ∧ (e1(t) > DZ(t))` — fires only on the first bar where all five hold after a bar where at least one failed. Sell-edge `E_S(t)` mirrors with `trendDown`.
- Entry long: on `E_L(t)` from flat, open long at the same-bar close. Refires of `E_L` while already long are no-ops. Entry short: on `E_S(t)` from flat, open short at the same-bar close; refires while short are no-ops.
- Exits: long closes when `trendUp(t) < e1(t)` (the source-prescribed green-crosses-below-explosion print, evaluated on completed-bar values); short closes when `trendDown(t) < e1(t)`. No stop, no target, no trailing, no time exit, no cooldown — pinned as written, explicitly none, not invented.
- Evaluation order (predeclared derivation): exits first, then entries, once per completed bar. A bar that closes a leg and prints the opposite edge reverses atomically (one close plus one open, a single reversal event — no double-fill ordering beyond it). A bar that closes a leg with no opposite edge ends flat; re-entry is allowed on the next fresh edge with no cooldown (explicitly none, not invented).
- Direction: two-sided with an explicit pre-warmup flat state (first 120 `1d` bars flat by record rule; before that, no order can fire). After warmup the system enters only on conjunction edges — there is no always-in-market requirement and no coded flat state beyond the seed, disclosed, not enabled.

## Required data

- Completed `1d` bars of BTCUSDT: `close` (MACD 20/40, Bollinger width, histogram sign) and `high`/`low` (true range inside the dead zone only). No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (derived pin; the script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction).
- Warmup: the dead-zone seed `rma(tr,100)` is the binding constraint — 100 completed `1d` bars before every referenced value is seeded (EMA-40, SMA/stdev-20, and the one-bar MACD lag are all absorbed inside it). The adopted warmup is the first 120 completed `1d` bars flat by record rule (predeclared researcher choice — covers seed plus margin). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Each bar's close/high/low enter the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (derived pin; the overview suggests 30-minute use in prose and the code names no market and no timeframe — venue choice, symbol spelling, and frame are disclosed here, never presented as source claims).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The `study()` ships no execution-timing statement at all; this record does not claim any source fill timing. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. Exit-before-entry ordering makes each bar's outcome a single deterministic event (hold, close, open, or atomic reversal) under either evaluation of the two edges.
- Sizing/capital/costs: the source ships no economics of any kind (indicator `study()` — no capital, no quantity, no commission, no funding, no margin assumption) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: single-position machine — at most one open leg; same-direction edge refires while positioned are no-ops; the opposite edge reverses in full (the coded exit print plus the fresh entry edge, one atomic event); an edge while flat opens; re-entry is allowed on the next fresh edge after any close (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (five pinned inputs, the MACD-difference histogram, the Bollinger-width explosion line, the Wilder-TR dead zone, the green/red split, the sienna/blue plots) and the complete ENTER/EXIT prose for both legs with the dead-zone veto — quoted verbatim in Provenance. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: the `study()` block contains zero order legs of any kind and the overview prose prescribes only the histogram-cross exits — the position-closing paths are the green/red-crosses-below-explosion prints plus full reversal via the opposite edge. The absence is prescribed (the prose lists entries and exits exhaustively and names no stop anywhere).
2. Coded rule is a conjunction, not a cross, stated plainly: no `crossover(`/`crossunder(` call appears anywhere in the quoted Pine; the only comparisons the prose requires are `rising` (strictly greater than prior bar), `above Explosion`, and `above DeadZone`. Substituting any two-line cross would be a different, unpinned rule.
3. Same-bar edge exclusivity fenced: `trendUp(t) > 0` implies `t1(t) > 0` implies `trendDown(t) = 0`, and `0 > e1(t)` is impossible since `e1 = 4 × stdev ≥ 0` — so `E_L` and `E_S` cannot fire on the same bar (at `t1 = 0` both histograms print 0 and neither clears `e1`). Deterministic under either fill convention.
4. Exit-while-positioned consistency fenced: while long, `trendUp ≥ e1` holds on every bar until the exit print (the exit fires on the first bar it fails), so the exit condition `trendUp(t) < e1(t)` is exactly the prescribed cross-below on the only bars where it can be evaluated — no gap between "crossed below" and "is below" exists inside a held leg. Mirror holds for shorts.
5. No future leakage in the stack, stated plainly: at decision bar `t`, every input reads completed bars through `t` (`close[t−1]` is the oldest-referenced lag, one bar back). No `security()`, no `request.*`, no negative index, no `barstate.islast`-gated repainting path, no `time` read at all. The `nz()` pre-seed branch is fenced out of every traded bar by the 120-bar warmup.
6. Two-sided posture provably complete: the prose prescribes symmetric buy and sell legs with symmetric exits; no third direction exists. A long-only or short-only reading would contradict the prescribed sell leg and is a different, unpinned rule.
7. Dead-zone scale honesty, admitted plainly: `DZ = 3.7 × rma(tr,100)` is denominated in the traded asset's own price units, so it auto-scales across price levels (the "ATR instead of a fixed number" crypto adaptation the overview claims) — but it also means a volatility collapse drags the floor down and admits weak histograms, while a volatility spike raises the floor and can block entries at the breakout moment. This is the prescribed construction, disclosed as the record's principal risk, not smoothed.
8. Derivation boundary fenced: the only non-source-native behaviors in this record are the `BTCUSDT 1d` market/frame pin, rising-edge entry events, the single-position exit-before-entry machine with atomic reversal, same-bar-close fills, the adopted 120-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the five inputs, all five formulas, the four-condition conjunctions, the dead-zone veto, the histogram-cross exits, and the no-stop/no-target/no-cooldown stance are source-verbatim. This record is therefore never evidence that any other market, frame, or timing of the source passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: pinned five inputs / histogram-plus-explosion-plus-deadzone stack / four-condition rising-edge entries / histogram-cross exits / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Direction relevance: inverting the side mapping (buy-edge opens short, sell-edge opens long, same exits) must not improve net expectancy; fail ⇒ the coded green-up/red-down direction adds nothing over its mirror.
- F2 — Dead-zone relevance: dropping both dead-zone legs (three-condition edges: rising, above explosion, explosion rising — same exits) must not improve net expectancy; fail ⇒ the prescribed volatility-mute veto adds nothing over the unfiltered conjunction.
- F3 — Explosion-line relevance: replacing the stack with raw histogram-sign flips (long on `t1` crossing above 0, short on crossing below 0, exit on the opposite flip — same inputs, no `e1`, no dead zone) must not improve net expectancy; fail ⇒ the Bollinger-width confirmation plus dead-zone veto add nothing over the bare MACD-difference sign.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (derived pin; the code names no market at all and the overview suggests 30-minute use in prose only). The close/high/low arithmetic ports across perpetual venues without structural change; the rule reads no volume, so venue volume-definition differences cannot touch it. The dead zone auto-scales in the asset's own price units, so no fixed-pip recalibration is needed across assets — cross-asset behavior differences are still real and unclaimed. The rule is two-sided with no stop leg, so a spot-only deployment expresses the long state and reversal mechanics only to the extent the venue permits shorting — full two-sided expression assumes a futures venue, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no session gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived market and frame: the code names no market and no timeframe (overview prose suggests 30-minute); this record pins `BTCUSDT 1d`. Cross-market and cross-frame behavior differences are real — the adaptation is disclosed, and this record makes no claim about any other market, frame, or the source's prose-suggested frame.
- Derived event semantics: the prose states persisting level conditions; this record fires entries on rising edges and orders exits before entries with atomic reversal. Backtest economics of edge-versus-level firing differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about any other event semantics.
- Derived fill timing: the `study()` states no fill timing at all; this record executes same-bar-close on `1d` BTCUSDT. The adaptation is disclosed, not hidden.
- No source economics: the source ships no capital, sizing, commission, funding, or margin assumption of any kind — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- No price stop, no time stop, no post-exit flat: adverse excursion after entry has no guardrail beyond the histogram-cross exit; a leg whose histogram never sinks below the explosion line is held indefinitely. This is the prescribed posture, disclosed as a principal risk alongside the dead-zone risk in Negative evidence.
- Chop sensitivity: a histogram flickering across the explosion line prints repeated exit/re-entry pairs, and a sub-dead-zone grind never enters at all. The conjunction-plus-cross construction is the prescribed design, disclosed, not smoothed.
- Slow seed: the 100-bar dead-zone average dominates warmup; the first 120 `1d` bars are flat by record rule, so early-history signals never enter any evaluation.
- Network limitation disclosed: TradingView page HTML could not be fetched from this runner (HTTP 403); canonical identity (title/adaptation lineage/ENTER-EXIT prose) is verified via the stable-URL record and the immutable mirror's verbatim Pine plus prose at pinned SHA — never from memory or paraphrase.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- TradingView canonical script page (ShayanKM V2 adaptation of LazyBear Waddah Attar Explosion; stable-URL identity verified via the pinned port's verbatim docstring URL; page HTML refused from this network, disclosed above): https://www.tradingview.com/script/d9IjcYyS-Waddah-Attar-Explosion-V2-SHK/
- Immutable GitHub source (full original Pine block plus ENTER/EXIT prose read end to end at pinned SHA `928f43180f72ab1f8537c9faf6c78cd4258969f7`, 2023-04-18): https://github.com/edyatl/waddah-attar-explosion
- Pine strategy semantics (history-referencing, `nz`/`rma`/`tr` semantics): https://www.tradingview.com/pine-script-reference/v5/
