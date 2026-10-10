---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: CHOP zone DMI-PSAR reversal two-sided on BTCUSDT 1d bars
created: 2026-10-11
updated: 2026-10-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-09-18
sources:
  - https://www.tradingview.com/script/GrP0zABg-CHOP-Zone-Entry-Strategy-DMI-PSAR-Exit/
  - https://github.com/hasnocool/tradingview-pine-scripts
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# CHOP zone DMI-PSAR reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (verified 2026-10-11):

- Canonical script page: https://www.tradingview.com/script/GrP0zABg-CHOP-Zone-Entry-Strategy-DMI-PSAR-Exit/ (`CHOP Zone Entry Strategy + DMI/PSAR Exit` by IronCasper, `//@version=4` `strategy()`). Page identity (title, author, full Inputs / Long-Short-Entry / Close-Reverse / Alerts prose) verified via the stable-URL page record; a direct page-HTML fetch from this runner returns HTTP 200 for a script shell without the rule text, so no formula line is claimed from page HTML — every formula and every order-gating line below was read verbatim from the immutable GitHub artifact instead, quoted in census.
- Pinned executable artifact (immutable GitHub mirror, complete Pine block read line by line): https://github.com/hasnocool/tradingview-pine-scripts at commit `69969aeaf271b2f7b5a7632a1bde43069a0cbe26` (2024-09-18, adopted as `source_as_of`), file `CHOP Zone Entry Strategy + DMI-PSAR Exit.pine` (header pins `// Title: "CHOP Zone Entry Strategy + DMI/PSAR Exit"`, `// Revision: 1.2`, `// Author: © IronCasper`, MPL-2.0). Unlike indicator-`study()` sources, this artifact is a real `strategy()` with `strategy.entry`/`strategy.close` legs — the position handling below is source-native, not a researcher state machine.
- Text census over the pinned Pine block: 1 `strategy(` / 4 `strategy.entry` (open-Long / open-Short / reverse-to-Long / reverse-to-Short) / 2 `strategy.close` (`"Long"` / `"Short"`, `when = active and goClose`) / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `pyramiding` (Pine default: no same-direction adds) / 0 `process_orders_on_close` (Pine default: per-completed-bar evaluation, next-bar fills) / 0 `commission_*` / 0 `default_qty_*` except `default_qty_value=1` (recorded as absent economics, never as cost evidence) / 0 `volume` (order-gating reads `high`/`low`/`close` only — neither `open` nor `volume` appears in any gating line) / 0 `time`/`timenow` / `offset` input pinned `0` (no forward/backward shift — causal by construction).
- Canonical inputs pinned verbatim: `lookbackPeriod=14`, `smoothLength=4` (SMA smoothing of the raw index), `offset=0`, `tradeType="Follow Trend"` (default; enables both sides plus reversal), `sensitivity=1` (entry on the first bar of each zone state; the multi-bar confirmation loop is bypassed — see Signal), `enableDMI=true`, `adxLen=14`, `diLen=14`, `adxKeyLevel=25`, `enablePSAR=true`, `psarStart=0.015`, `psarIncr=0.001`, `psarMax=0.2`, `showChopAs="Colored Line (PSAR)"` (default view; the LazyBear-momentum gate is inert under this default — fenced in Negative evidence).
- Source-reported entry/exit prose (script page, quoted for gate evidence): Long/Short Entry — (1) CHOP over 61.8 (long) or under 38.2 (short); (2) with DMI enabled, ADX above the key level (default 25); (3) sensitivity bars all in-state; (4) under Follow Trend with PSAR enabled, longs only in PSAR uptrend, shorts only in downtrend. Close/Reverse — (1) DMI close when ADX drops below the key level with `-DI > +DI` (long) or `+DI > -DI` (short); (2) PSAR close on trend-state flip; (3) CHOP-reversal closes apply only when both DMI and PSAR are disabled (not this record's configuration — fenced below); (4) an entry edge on the same bar as any close flag reverses, otherwise the leg closes. Page performance language is demo-only (10%-equity/100k-capital backtest anecdotes across SPX 15M, TSLA 30M, EURUSD 4H with mixed results; the author states no standalone-use claim) — this record claims no source-reported performance and no reproduced performance. The script names no market and no timeframe — the `BTCUSDT 1d` pin below is a fully researcher-declared derivation choice, disclosed here, never presented as a source claim.

Licence and rights: this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence (mirror file carries MPL-2.0).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) market/frame pin `BTCUSDT 1d` (the code names no market and no timeframe; the page prose cites only non-crypto demo frames — this pin is a pure researcher choice, disclosed here, never presented as source-native); (2) same-bar-close fills (the source ships no execution-timing argument — Pine default evaluates per completed bar and fills on the next bar; no `process_orders_on_close` ships anywhere, quoted verbatim in census); (3) an adopted 60-bar warmup with pre-warmup bars flat by record rule (covers the 14-bar indicator seeds plus EMA-stabilization margin — see Required data); (4) house sizing/capital/costs replacing the absent source economics (demo-only 10%-equity/100k-capital prose with zero cost assumption — recorded as absent, never as zero-cost evidence; see Execution assumptions). The CHOP custom formula, all zone thresholds, the EMA-based DMI/ADX construction, the PSAR triple, the zone-edge entries, the PSAR-flip and DMI-cross exits, the atomic reversal, the single-position posture, and the no-stop/no-target/no-cooldown stance are source-native and unmodified.

Pre-write dedup (2026-10-11): working-tree case-insensitive searches for `GrP0zABg`, `ironcasper`, `chop zone`, `choppiness`, `dreiss`, and `ta.ci(` return zero strategy records using this source, author script, or indicator — the only `choppiness` hits are ordinary prose (`tape choppiness` in the FVG record) and `[[quant/tradingview-choppiness-donchian-breakout-filter-2026-09-16]]` Wiki links inside Related-Wiki sections of two unrelated records, never a Dreiss-index mechanism. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `psar-flip-stop-reverse-btcusdt-1d` trades every bare PSAR dot-side flip with no regime gate and no DMI leg (this rule enters only on CHOP-zone edges confirmed by ADX > 25 and the PSAR trend state, and exits on ADX-breakdown DI crosses that the PSAR record never computes); `dmi-swings-contrarian-adx-btcusdt-1d` is an ADX-exhaustion fade (this rule demands ADX strength, never fades it); `sideways-dmi-bollinger-breakout-long-btcusdt-4h` gates a Bollinger breakout on DMI (no CHOP line, no zone-edge entries, no PSAR state machine anywhere). Five-axis distinction: mechanism differs (regime-zone edge entries — chop-coil longs above 61.8, trend-exhaustion shorts below 38.2 — confirmed by trend-strength and exited by trailing-stop flip plus strength-breakdown cross), signal construction differs (no pool record computes the Dreiss log-ratio index, let alone this script's close-inclusive custom construction, against ADX-25 and PSAR state), trigger differs (first-bar-of-zone-state edge with close-direction clause — not a cross, not a flip, not a band touch), data differs (`high`/`low`/`close` only; no `open`, no `volume`).

## Economic mechanism

### Source-reported

Chop-coil breakout anticipation funded by trend-strength confirmation, with a trailing stop as the only risk leg (page prose plus quoted Pine, demo-only performance section fenced above): the Choppiness Index grades movement quality on 0–100 — above 61.8 the market is retracing itself (chop), below 38.2 it is covering ground efficiently (trend) — but says nothing about direction. The script therefore never trades the index alone: longs fire only from the high-chop zone on a rising close (the coil-release bet — extended consolidation precedes directional expansion), shorts only from the low-chop zone on a falling close, both only while ADX reads above 25 (trend-strength confirmation that deletes range-era whipsaws) and only in the PSAR trend direction (Follow Trend). Exits are the mirror discipline: a PSAR flip closes immediately (the trailing stop is the exit), an ADX breakdown below 25 combined with an opposing DI cross closes (the strength thesis is dead), and an opposite zone edge on any close-flag bar reverses atomically. The design bets that the highest-expectancy entries are regime-transition bars confirmed by strength, and that anything held past a PSAR flip or an ADX breakdown is hope, not a position.

### Research interpretation

Zone-edge transition system, two-sided with composite strength-gated entries and three-path exits plus an explicit pre-warmup flat state. Unlike cross systems that trade the moment one line passes another, this rule never trades a bare cross: its entries require a CHOP zone print AND a same-direction close AND ADX strength AND PSAR agreement — four comparisons on the same bar. Unlike always-in-market flip systems, the rule rests flat whenever no fresh zone edge fires and whenever a leg meets any of its three close paths. Note the deliberate asymmetry the source pins plainly: longs are born in high chop (anticipating the release), shorts in deep trend (riding exhaustion into the next range) — the two sides hunt opposite regimes, so the system's long book and short book have structurally different holding environments, disclosed, not smoothed. The price of the ADX gate is missed early trend: a coil that releases without ADX ever clearing 25 never enters at all, and a PSAR flip on a single violent bar closes a leg that the next bar's continuation would have vindicated. The bet is on confirmed regime-transition bars, not on any reversal level, volume print, mean-reversion extreme, or calendar effect.

## Signal

Exact rule as pinned (all inputs frozen — any other value is a different, unpinned rule):

- Declarations (derived): single-position state machine over `BTCUSDT 1d` with same-bar-close execution and house sizing/costs (see Execution assumptions). At most one open leg; state ∈ {flat, long, short}.
- Indicator stack, pinned verbatim: `sumATR = sum(atr(1), 14)`; `maxHi = highest(high >= close[1] ? high : close[1], 14)`; `minLo = lowest(low <= close[1] ? low : close[1], 14)`; `CHOP(t) = 100 × log10(sumATR / (maxHi − minLo)) / log10(14)`, then `CHOP := sma(CHOP, 4)`; `offset = 0` (no shift). This is the script's custom close-inclusive construction, pinned as written — never "corrected" toward the textbook reference formula. DMI, pinned verbatim: `upMove = change(high)`, `downMove = −change(low)`; raw `+DM = upMove > downMove ∧ upMove > 0 ? upMove : 0` (mirror for `−DM`); `TR14 = ema(tr, 14)`; `+DI = 100 × ema(+DM, 14) / TR14` (mirror for `−DI`); `ADX = 100 × ema(abs((+DI − −DI) / (+DI + −DI)), 14)` with `fixnan` carry-forward on the pre-seed division. PSAR, pinned verbatim: `psar = sar(0.015, 0.001, 0.2)`; state `up` iff `psar < close`, else `dn`. Every input is a completed bar's `high`/`low`/`close`; no `open` and no `volume` is read. The LazyBear `linreg` momentum block ships in the file but gates no order under the canonical `showChopAs = "Colored Line (PSAR)"` default (fenced in Negative evidence).
- Zone edges (source-native first-bar-of-state events at the pinned `sensitivity = 1`, whose confirmation loop is bypassed by code): `E_L(t) = (CHOP(t) ≥ 61.8) ∧ (close(t) > close(t−1)) ∧ ¬E_L-state(t−1)`; `E_S(t) = (CHOP(t) ≤ 38.2) ∧ (close(t−1) > close(t)) ∧ ¬E_S-state(t−1)`.
- Entry long: on `E_L(t)` from flat, open long at the same-bar close iff `ADX(t) > 25` and PSAR state is `up` (Follow-Trend gate). Refires of `E_L` while already long are no-ops (Pine-default no-pyramiding plus the `not(activeLong)` guard). Entry short: mirror on `E_S(t)` iff `ADX(t) > 25` and PSAR state is `dn`; refires while short are no-ops.
- Exits (any one closes): PSAR flip (`dn` after `up` closes long; `up` after `dn` closes short); DMI breakdown (`ADX < 25 ∧ −DI > +DI` closes long; `ADX < 25 ∧ +DI > −DI` closes short); opposite edge (see ordering). No stop, no target, no time exit, no cooldown — pinned as written (the script ships zero `strategy.exit` legs and the page prose names no stop beyond the PSAR trailing stop), explicitly none, not invented.
- Evaluation order (source-native, preserved): exits evaluated with the close-flag consolidation, then entries, once per completed bar. A bar that raises a close flag and prints the opposite edge reverses atomically (one close plus one open, a single reversal event — `goReverse` branch). A bar that raises a close flag with no opposite edge ends flat; re-entry is allowed on the next fresh zone edge with no cooldown (explicitly none, not invented). An opposite edge while positioned always raises the close flag through the opposite-edge clause, so no positioned bar can swallow a reversal signal (fenced in Negative evidence).
- Direction: two-sided with an explicit pre-warmup flat state (first 60 `1d` bars flat by record rule; before that, no order can fire). `tradeType = "Follow Trend"` enables both sides and reversal; a long-only or short-only reading would contradict the prescribed sell leg and is a different, unpinned rule.

## Required data

- Completed `1d` bars of BTCUSDT: `high`/`low`/`close` (CHOP log-ratio, ATR sum, DI true range, PSAR stepping). No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (derived pin; the script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction).
- Warmup: the binding seeds are the 14-bar CHOP window plus the `ema(⋅, 14)` DI/ADX smoothing chains (recursive EMAs stabilize within ~3 × 14 bars). The adopted warmup is the first 60 completed `1d` bars flat by record rule (predeclared researcher choice — covers every seed plus margin; the `fixnan` pre-seed branch never fires on a traded bar). No repainting, no negative shift, no future reference (`offset = 0` pinned; the `sensitivity` loop reads only the current and past bars), no full-sample normalization; one evaluation per completed bar. Each bar's high/low/close enter the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (derived pin; the code names no market and no timeframe, and the page prose cites only SPX/TSLA/EURUSD demo frames — venue choice, symbol spelling, and frame are disclosed here, never presented as source claims).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar fill (no execution-timing argument ships anywhere — quoted verbatim in census); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. Exit-before-entry ordering makes each bar's outcome a single deterministic event (hold, close, open, or atomic reversal) under either evaluation of the two edges.
- Sizing/capital/costs: the source ships no portable economics (demo-only 10%-equity/100k-capital prose, `default_qty_value=1`, zero cost assumption — recorded as absent economics, never as zero-cost evidence) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: single-position machine — at most one open leg; same-direction edge refires while positioned are no-ops; the opposite edge reverses in full (the coded close flag plus the fresh entry edge, one atomic event); an edge while flat opens; re-entry is allowed on the next fresh edge after any close (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (custom CHOP formula with close-inclusive extremes, SMA-4 smoothing, 61.8/38.2 zone thresholds with the close-direction clauses, EMA-based DMI/ADX with all three lengths and the 25 key level, PSAR 0.015/0.001/0.2 with the dot-side state rule, first-bar-of-state edges at sensitivity 1, Follow-Trend PSAR gating, the three close paths with the both-disabled CHOP-reversal fallback, and the atomic reverse/close handling with single-position guards) plus the complete entry/exit prose for both legs — quoted in Provenance. It ships no portable performance: only demo-anecdote prose (mixed results across three non-crypto demo frames, no table or figure, author disclaims standalone use) — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: the block contains zero `strategy.exit` legs and the page prose prescribes only the PSAR-flip, DMI-breakdown, and opposite-edge paths — the no-stop/no-target/no-time posture is prescribed (the prose lists entries and exits exhaustively and names no fixed stop anywhere; the PSAR trailing stop is the stop), explicitly none, never hidden.
2. Entries are edges, not levels, stated plainly: `goLong`/`goShort` require `not(cond[sensitivity])` with the pinned `sensitivity = 1` reading the prior bar's state, and the multi-bar loop is skipped by code (`if sensitivity != 1` bypass). Substituting a persisting-level entry (firing every in-zone bar) would be a different, unpinned rule.
3. Same-bar edge exclusivity fenced: `E_L` requires `close(t) > close(t−1)` while `E_S` requires `close(t−1) > close(t)` — strictly mutually exclusive, with doji bars (`close == close[1]`) firing neither. Deterministic under either fill convention.
4. Reversal completeness fenced: `closeShortState` includes the `goLong` clause and `closeLongState` includes the `goShort` clause, so an opposite edge while positioned always raises its close flag and the `goReverse` branch fires — no positioned bar swallows a reversal. Same-direction refires while positioned hit the `not(activeLong)`/`not(activeShort)` guards and are no-ops — no pyramiding path exists in code or in Pine defaults (`pyramiding` unset).
5. Momentum block fenced as visual-only: `curr_momUpTrend`/`curr_momDnTrend` gate entries only when `showChopAs == "Colored Line (MOM)"`; the canonical default is `"Colored Line (PSAR)"`, under which the Follow-Trend gate reads `psarTrendState` alone. Adopting the MOM view would be a different, unpinned rule.
6. CHOP-fallback closes fenced as inert: `chopCloseLong`/`chopCloseShort` evaluate to `false` whenever either enable is true — both are enabled in this record, so the only close paths are the PSAR flip, the DMI breakdown, and the opposite edge. No fourth close path exists.
7. No future leakage in the stack, stated plainly: at decision bar `t`, every input reads completed bars through `t` (the oldest-referenced lags are the 14-bar windows and `close(t−1)`). No `security()`, no `request.*`, no negative index, no `offset ≠ 0`, no `barstate.islast`-gated repainting path, no `time` read at all. The `fixnan` pre-seed branch is fenced out of every traded bar by the 60-bar warmup.
8. Two-sided posture provably complete: `tradeType = "Follow Trend"` sets both side selectors and `reverseAllowed` true with symmetric buy and sell legs and symmetric exits; no third direction exists.
9. Custom-formula honesty, admitted plainly: the script's `maxHi`/`minLo` fold `close[1]` into the extremes, so its index is not identical to the textbook reference construction — pinned as written, never normalized, disclosed as the record's principal replication risk alongside the long-book/short-book regime asymmetry in Research interpretation.
10. Derivation boundary fenced: the only non-source-native behaviors in this record are the `BTCUSDT 1d` market/frame pin, same-bar-close fills, the adopted 60-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the custom CHOP formula, smoothing, thresholds, close-direction clauses, DMI/ADX construction, PSAR triple, zone-edge entries, three close paths, atomic reversal, single-position guards, and risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, or timing of the source passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: custom CHOP-14/SMA-4 stack / 61.8-38.2 zone edges with close-direction clauses / ADX-25 gate / PSAR 0.015-0.001-0.2 Follow-Trend gating / three-path exits with atomic reversal / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Zone relevance: replacing the zone edges with bare PSAR-state flips (long on flip to `up`, short on flip to `dn`, same three close paths) must not improve net expectancy; fail ⇒ the CHOP-regime entry gate adds nothing over the PSAR trailing-stop machine alone.
- F2 — Strength-gate relevance: dropping the ADX-25 confirmation (zone edges gated by PSAR state only, same exits) must not improve net expectancy; fail ⇒ the DMI strength confirmation adds nothing over the zone-plus-PSAR rule.
- F3 — PSAR-leg relevance: disabling the PSAR flip close and the Follow-Trend direction gate (zone edges with ADX gate only, DMI-breakdown and opposite-edge closes only) must not improve net expectancy; fail ⇒ the PSAR trailing-stop leg adds nothing over the CHOP-plus-ADX rule.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (derived pin; the code names no market at all and the page prose cites only non-crypto demo frames). The high/low/close arithmetic ports across perpetual venues without structural change; the rule reads no volume, so venue volume-definition differences cannot touch it. The log-ratio index auto-scales in the asset's own price units, so no fixed-pip recalibration is needed across assets — cross-asset behavior differences are still real and unclaimed. The rule is two-sided with no stop leg, so a spot-only deployment expresses the long state and reversal mechanics only to the extent the venue permits shorting — full two-sided expression assumes a futures venue, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no session gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived market and frame: the code names no market and no timeframe (page prose cites only SPX 15M, TSLA 30M, EURUSD 4H demos); this record pins `BTCUSDT 1d`. Cross-market and cross-frame behavior differences are real — the adaptation is disclosed, and this record makes no claim about any other market, frame, or the source's demo frames.
- Derived fill timing: the source fills next-bar under Pine defaults with no timing argument; this record executes same-bar-close on `1d` BTCUSDT. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- No source economics: the source ships only demo-anecdote prose and `default_qty_value=1` with no commission, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- No price stop, no time stop: adverse excursion after entry has no guardrail beyond the PSAR flip and the DMI-breakdown cross; a leg whose PSAR never flips and whose ADX never breaks down is held indefinitely. This is the prescribed posture, disclosed as a principal risk.
- Whipsaw sensitivity: a CHOP line flickering across a zone boundary with alternating closes prints repeated edge/reversal pairs, and a coil that releases without ADX clearing 25 never enters at all. The edge-plus-gate construction is the prescribed design, disclosed, not smoothed.
- Slow seed: the 14-bar windows plus EMA-stabilization dominate warmup; the first 60 `1d` bars are flat by record rule, so early-history signals never enter any evaluation.
- Network limitation disclosed: TradingView page HTML from this runner carries no rule text (script shell only); canonical identity (title/author/ID/prose) is verified via the stable-URL page record and every formula via the immutable mirror's verbatim Pine at pinned SHA — never from memory or paraphrase.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- TradingView canonical script page (IronCasper CHOP Zone Entry Strategy + DMI/PSAR Exit; stable-URL identity and rule prose verified, page HTML carries no rule text from this network, disclosed above): https://www.tradingview.com/script/GrP0zABg-CHOP-Zone-Entry-Strategy-DMI-PSAR-Exit/
- Immutable GitHub source (complete Pine v4 block read end to end at pinned SHA `69969aeaf271b2f7b5a7632a1bde43069a0cbe26`, 2024-09-18): https://github.com/hasnocool/tradingview-pine-scripts
- Pine strategy semantics (Pine-default fills, `pyramiding`, `fixnan`/`ema`/`sar` semantics): https://www.tradingview.com/pine-script-reference/v5/
