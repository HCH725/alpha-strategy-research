---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Elder-ray 123-reversal combo two-sided on BTCUSDT 1h bars
created: 2026-10-09
updated: 2026-10-09
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-11-21
sources:
  - https://www.fmz.com/strategy/432762
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E5%8F%8D%E8%BD%AC%E5%BC%BA%E5%8A%BF%E7%AD%96%E7%95%A5-Elder-Ray-Bull-Power-Combo-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Elder-ray 123-reversal combo two-sided on BTCUSDT 1h bars

## Provenance

Primary source read end to end (immutable public mirror file plus its recorded FMZ canonical page, fetched 2026-10-09):

- Canonical page: https://www.fmz.com/strategy/432762 (page title `Elder Ray Bull Power Combo Strategy | FMZ`, publisher account `ChaoZhang`, `Created: 2023-11-21 11:36:38`-stamped `2023-11-21 11:36:48`, equal to the mirror `Last Modified`). Fetched over HTTPS during this cycle (779250 bytes): the page exposes the same seven-argument set in order (`Length`, `KSmoothing`, `DLength`, `Level`, `LengthBP`, `Trigger`, `Trade reverse`), the full `/*backtest ... */` header preview quoted below, and the complete order block (`2 strategy.entry` / `1 strategy.close` in page state — the single close is the `strategy.close_all()` line — quoted verbatim in census), with `dayofmonth` appearing twice in page state (the `DayHigh` reset comparison). Word-boundary counts over the whole landing HTML: `Net Profit` 0, `Profit Factor` 0, `Sharpe` 0, `Max Drawdown` 0, `win rate` 0, `Win Rate` 0, `Annualized` 0, `Return` 0 — the page ships no performance numbers of any kind (adopted as `source_as_of` 2023-11-21 from the page Created stamp, which equals the mirror `Last Modified`).
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit date 2025-04-30 11:10:28 +0800, subject `update`; verified repository head at research time via the GitHub commits API — the same head pin as the merged KST, Schaff, TRIX, SQZMOM-LB, Aroon, Qstick and AC admissions), exact file path `反转强势策略-Elder-Ray-Bull-Power-Combo-Strategy.md` (non-ASCII filename preserved verbatim; percent-encoded blob URL in Sources). File 9680 bytes, blob SHA `42ed3cb8934181cf04ed27dd2dfa3e71db4164a5` (verified against the GitHub contents API at the pinned commit — size and SHA both match). The mirror prints `> Detail` = https://www.fmz.com/strategy/432762 and `> Last Modified` = 2023-11-21 11:36:48 (equal to the page Created stamp). Its seven-row `> Strategy Arguments` table (14/true/3/50/13/false/false) agrees with the seven pinned `input(...)` declarations (14/1/3/50/13/0/false) and the page-embedded argument set; the single rendering difference (`KSmoothing` printed `true` in the mirror table versus `input(1, minval=1)` in code and spin `1` on the page) resolves to the identical effective smoothing length 1 either way and is fenced in Limitations, never silently picked.
- Full `//@version=4` `strategy(title="Combo Strategy 123 Reversal & Elder Ray (Bull Power)", shorttitle="Combo", overlay=true)` block read in full (3165 characters, `//@version=4` through the final `strategy.close_all()`). The header comment attributes the combo to `Copyright by HPotter v1.0 15/06/2020`, the reversal leg to Ulf Jensen's book page 183, and the Elder-ray leg to Dr Alexander Elder — original-authorship lineage is preserved here, never claimed by the FMZ publisher. The page-embedded `/*backtest*/` header (`start: 2023-10-21 00:00:00`, `end: 2023-11-20 23:59:00` in preview rendering, `period: 1h`, `basePeriod: 15m`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`) is byte-present on both the canonical page preview and the mirror block — market (`BTC_USDT` Binance futures) and decision frame (`1h`) are therefore source-native, never researcher-chosen.
- Text census over the pinned code block: 2 `strategy.entry` / 1 `strategy.close` (the `strategy.close_all()` flat leg) / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=`/`qty_percent` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `volume` / 0 `time(`. `dayofmonth` appears exactly twice (both inside the single `DayHigh` reset comparison). `overlay=true` appears once inside the strategy declaration (display only). `pyramiding`, `process_orders_on_close`, `calc_on_every_tick`, `commission`, and `default_qty_*` are unset throughout. Price reads are `close` (14), `high` (3: stoch line, BP reset, BP ratchet), `low` (1: stoch line); `open`/`hl2` never appear.
- No risk layer ships anywhere in the source: zero stop/target/trailing/time-exit order legs, and the mirror's own risk prose proposes adding stops as future optimization (`考虑加入止损策略`), confirming none ships. The agreement-loss flat plus opposite-agreement reversal posture below is therefore the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention.
- Page/mirror performance language is absent entirely (no qualitative praise with numbers, no table, figure, or number) — this record claims no source-reported performance and no reproduced performance.
- Prose-versus-code gaps are pinned to the code, never repaired: (a) the prose describes a 9-day stochastic with slow-below-50 longs / fast-above-50 shorts, but the code computes a 14-bar stochastic with `vFast<vSlow and vFast>50` longs and `vFast>vSlow and vFast<50` shorts; (b) the prose describes daily Elder-ray bars, but the code runs the EMA(13) and session-anchored DayHigh on the source-native `1h` frame. This record pins the computation in both cases; anyone citing the prose alone would describe a different rule. Both gaps are fenced in Limitations.

Licence and rights: the canonical page is a public FMZ strategy publication by ChaoZhang carrying an HPotter copyright header. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly three: (1) same-bar-close fills (the source fills next-bar-open — no `process_orders_on_close` ships anywhere, quoted verbatim in census); (2) an adopted 100-bar warmup with pre-warmup bars flat by record rule (structural minimum is 16 bars — see Required data); (3) house sizing/capital replacing the language-default sizing (no `default_qty_*` ships anywhere — see Execution assumptions). Market (BTCUSDT Binance futures), decision frame (`1h`), and the UTC-midnight day anchor (Binance exchange timezone — see Signal) are source-native per the page-embedded backtest header and the `dayofmonth` reset line, not adaptations. All three adaptations are predeclared here, confined to Provenance, Signal, Required data, Execution assumptions, and Limitations, with every original claim kept separate above. Indicator formulas, lookbacks, comparisons, state recursion, order IDs, direction handling, the close-all flat leg, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-09): working-tree word-boundary searches for `elder`, `bull-power`, `432762`, `reversal123`, `123-reversal`, and `combo` return zero strategy records using this source, author strategy, or mechanism (the `elder`/`bull-power`/`dayofmonth` hits inside the merged AC record are its own dedup paragraph naming this absent family, corroborating absence rather than colliding). Same-publisher ChaoZhang records exist (KST FMZ 436493, Schaff FMZ 365905, TRIX FMZ 428683, Aroon FMZ 438795, Qstick FMZ 439854, AC FMZ 435716) but carry different canonical identities, different indicator families, and different order sets. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #58 (ML/reconstruction batch — file list verified, no oscillator/combo record), and #63 (SuperTrend ATR-flip trend long) — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `stochastic-ott-dual-trend-btcusdt-1d` is a stochastic/OTT dual-trend system with trailing exits (no Elder leg, no agreement-flat state); `monday-drift-weekly-calendar-hold-btcusdt-1h` is a weekly-calendar long-only hold (no indicator, no two-sided state machine); `williams-r-level-cross-mean-reversion-long-btcusdt-1d` is a single-oscillator threshold-cross long-only system. Five-axis distinction: mechanism differs (two-leg agreement gate with explicit flat — both legs must agree or the system stands aside), signal construction differs (no pool record combines a consecutive-close/stochastic streak leg with a session-anchored DayHigh-minus-EMA Elder leg), exits differ (agreement-loss `close_all` flat plus opposite-agreement reversal, no trailing/band exits), source identity differs (FMZ 432762 Nov-2023 ChaoZhang/HPotter/Jensen/Elder lineage versus other FMZ IDs or TV authors), and direction handling differs (two-sided with an explicit Damage flat state versus long-only or always-in-market holders).

## Economic mechanism

### Source-reported

Combo filtering of reversal timing through Elder power confirmation (mirror `策略原理`, corroborated by the code header): the 123-reversal leg hunts consecutive-close streaks faded back by the stochastic position, while the Elder-ray leg demands buyers (sellers) prove strength by holding the session high (low) above (below) the 13-bar value consensus. Only bars where both legs agree open or hold a position; disagreement stands flat. Agreement gating filters false-breakout whipsaw at the cost of sparse signals (the mirror's own risk section admits alignment is infrequent).

### Research interpretation

Two-gate AND-combo with an explicit neutral state. Unlike always-in-market holders (Qstick, AC records) that must be long or short after warmup, and unlike single-trigger cross systems (KST/Schaff records) that fire once per crossing, this system rests flat whenever the legs disagree — the flat state is a first-class coded outcome (`close_all`), not the absence of a signal. The reversal leg is countertrend in spirit (buy two-up-days while %K sits above 50 but below %D) while the Elder leg is pro-strength (session high must clear the EMA); their conjunction selects streaks that still carry buying power — a narrower, more deliberate trade than either leg alone. Sparse signals are the honestly priced cost (see Negative evidence).

## Signal

Exact rule as pinned (defaults quoted — effective inputs unmodified):

- Declaration (derived): `strategy(title="Combo Strategy 123 Reversal & Elder Ray (Bull Power)", shorttitle="Combo", overlay=true)` with same-bar-close execution adopted for the derived record (no such argument ships in the source) and house sizing replacing the unset language-default sizing (see Execution assumptions). `calc_on_every_tick` is unset (default false: exactly one evaluation per completed bar). No commission or margin assumption ships anywhere — pinned as absent, with house costs applying to the derived evaluation (see Execution assumptions).
- Inputs (pinned, table- and page-agreeing): `Length=14` (`input(14, minval=1)`), `KSmoothing=1` (`input(1, minval=1)`; table prints `true`, page spin `1` — identical effective length, see Provenance), `DLength=3` (`input(3, minval=1)`), `Level=50` (`input(50, minval=1)`), `LengthBP=13` (`input(13, minval=1)`), `Trigger=0` (`input(0)`; table prints `false` — identical), `reverse=false` (`input(false, title="Trade reverse")`). Retuning any of them would be a different, unpinned rule.
- Reversal leg (pinned): `vFast = sma(stoch(close, high, low, 14), 1)` (raw 14-bar %K); `vSlow = sma(vFast, 3)` (%D). `posReversal123 = +1` when `close[2] < close[1] and close > close[1] and vFast < vSlow and vFast > 50` (two consecutive up closes with %K above 50 but below %D); `-1` when `close[2] > close[1] and close < close[1] and vFast > vSlow and vFast < 50` (two consecutive down closes with %K below 50 but above %D); otherwise hold `nz(pos[1], 0)`.
- Elder leg (pinned): `xMA = ema(close, 13)`; `DayHigh := high` on the first bar of a new calendar day (`dayofmonth != dayofmonth[1]`), otherwise `max(high, nz(DayHigh[1]))` — the running session high since the day anchor. `nRes = DayHigh - xMA`; `posBP = +1` when `nRes > 0`, `-1` when `nRes < 0`, otherwise hold `nz(pos[1], 0)`.
- Day anchor (source-native): `dayofmonth` evaluates in the exchange timezone; the derived record pins this to Binance's exchange timezone (UTC), so the session high resets on the first completed `1h` bar dated a new UTC day. No local-timezone, DST, or session-template input exists anywhere — pinned as none.
- Combo (pinned): `pos = +1` iff `posReversal123 == 1 and posBP == 1`; `-1` iff both are `-1`; else `0`. `possig = pos` under the pinned `reverse=false`; the `reverse=true` inversion path is disclosed-as-disabled code, never the admitted rule — enabling it would be a different, unpinned rule.
- Entry long: `if (possig == 1) strategy.entry("Long", strategy.long)` — agreement-holding, re-asserted on every completed `1h` bar while both legs agree long, with same-bar-close execution under the derived declaration.
- Entry short: `if (possig == -1) strategy.entry("Short", strategy.short)` — mirror terms. The two `if` statements are separate but their conditions are mutually exclusive on every bar, so at most one entry call fires per bar under any evaluation order — no same-bar long/short conflict exists to resolve.
- Flat leg: `if (possig == 0) strategy.close_all()` — any agreement loss (either leg flips or falls to hold while the other disagrees) closes the whole position at the adopted fill. No stop, no target, no trailing, no time exit — pinned as written, explicitly none, not invented.
- Direction: symmetric two-sided with an explicit flat state. A short-side instrument is required for the short legs; on a spot-only venue they are inexpressible and the record would not be the same rule (see Crypto portability).
- Display isolation: `barcolor(...)` feeds no order condition; order logic reads exactly the two entry conditions plus the flat condition.

## Required data

- Completed `1h` bars of BTCUSDT: `close`, `high`, `low` only (stoch line, EMA line, DayHigh ratchet). No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, or cross-venue state is read by any order-gating line. The only calendar read is the `dayofmonth` day-rollover comparison, pinned to the UTC exchange timezone above.
- Single decision timeframe `1h` (source-native per the page-embedded `period: 1h` header). The script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction. The header's `basePeriod: 15m` is the FMZ execution granularity of the source backtest, not a signal input — the derived record evaluates completed `1h` bars only and claims no 15m behavior.
- Warmup: the 14-bar stochastic needs 14 completed `1h` bars, `%D = sma(%K, 3)` needs 3 %K values — first fully-windowed reversal state on the 16th completed bar; `ema(close, 13)` is full from bar 13; the `pos[1]` recursions are defined from the first bar via `nz` (resolving flat/zero). Structural minimum is therefore the 16th completed `1h` bar for the first evaluable combo state (the DayHigh ratchet accumulates from bar 1 and first resets on the first UTC-day rollover); the adopted warmup is the first 100 completed `1h` bars flat by record rule (predeclared researcher choice). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (source-native per the header's `Futures_Binance BTC_USDT`; venue transfer from `BTC_USDT` to `BTCUSDT` spot-symbol spelling is naming only, never presented as a market change).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. The source's own timing is next-bar-open (no execution-timing argument ships anywhere — quoted verbatim in Provenance); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill. With no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. The two entry legs are mutually exclusive every bar (see Signal), and the flat leg fires only when neither entry condition holds, so no ordering resolution is required.
- Sizing/capital/costs: no `default_qty_*`, commission, or margin assumption ships anywhere (quoted verbatim in census) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions replace the unset language defaults here, never presented as source-native behavior.
- Concurrency: no `pyramiding` ships anywhere, pinning the language default of no same-direction adds — at most one unit per side under fixed order IDs `Long`/`Short`; repeat same-agreement entries while positioned are no-ops, the opposite-agreement entry reverses (closes the current side and opens the opposite in one transition), and any agreement loss closes all via the coded flat leg. Re-entry is allowed immediately on the next qualifying agreement after any flat (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The mirror ships the full two-leg construction (stoch 14/1/3/50 streak conditions, EMA13, UTC-anchored DayHigh ratchet, Trigger-0 comparisons, triple-AND combo with `close_all` flat), the two agreement-holding order legs with their order IDs, the seven inputs, the HPotter/Jensen/Elder authorship header, and the page-embedded 1h/15m October-November-2023 backtest header. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=`/`qty_percent` — the sole position-closing paths are the coded `close_all` flat leg and opposite-agreement reversal. The absence is coded (the block ends with the flat leg and display calls after the two entries), and the mirror's risk prose proposes stops as future work, corroborating that none ships — fenced in Limitations for the reviewer rather than upgraded into a source claim.
2. Entry legs are mutually exclusive on every bar by value (`possig` is a single integer that cannot equal 1 and -1 at once), and the flat leg fires only when `possig == 0`, so no single bar can satisfy more than one order leg even though they sit in separate `if` statements.
3. Exit-leg conditionality, admitted plainly: a long opened on dual agreement exits only when agreement breaks (either leg flips or holds-against). A market that keeps both legs aligned never exits until they diverge — there is no time-stop to cut a stale agreement, and choppy leg-flapping around the Trigger/stochastic lines can whipsaw the system in and out of flat. This is the coded trade, disclosed, not a tunable parameter here.
4. Sparsity is structural: both legs must agree, and the mirror's own risk section warns alignment is infrequent. Long evaluation windows may contain few or zero trades; this record treats trade scarcity as the strategy's honest cost, never as a reason to loosen the AND into an OR (which would be a different, unpinned rule).
5. Boundary ties hold, never fire: exactly-zero `nRes` inherits prior Elder state via `nz(pos[1], 0)`; exactly-50 %K satisfies neither streak condition (strict inequalities); warmup bars are flat by record rule.
6. The stochastic length (14), smoothing chain (1/3), Level (50), streak definition (two consecutive closes), EMA length (13), Trigger (0), DayHigh UTC-day anchor, fixed order IDs, symmetric states, the `close_all` flat leg, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning a length, enabling reverse, adding a stop/target/cooldown, switching source series, replacing DayHigh with a plain bar high, or disabling a side would each be a different, unpinned rule — none is admitted here.
7. Derivation boundary fenced: the only non-source-native behaviors in this record are same-bar-close fills, the adopted 100-bar warmup with record-rule pre-warmup flat, and house sizing — all predeclared above; market, timeframe, day anchor, every signal, threshold, default, transition, flat leg, and risk posture are source-verbatim. This record is therefore never evidence that the original next-bar-open 1h/15m source itself passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: stoch 14/1/3/50 / two-close streak / EMA13 / UTC-anchored DayHigh / Trigger 0 / dual-agreement gate / `close_all` flat / `reverse=false` / symmetric entries / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Agreement relevance: replacing the AND-combo with either leg alone (reversal-only, Elder-only) must not improve net expectancy; fail ⇒ the agreement gate adds nothing over its parts.
- F2 — Anchor relevance: replacing the UTC-session-anchored DayHigh with the plain current-bar high (`high - ema(close,13) > 0`) must not improve net expectancy; fail ⇒ the session anchor adds nothing over a bar-local Elder spread.
- F3 — Flat-state relevance: removing the `close_all` leg (holding the last side through disagreement, reversal-only) must not improve net expectancy; fail ⇒ the explicit flat state is dominated by simply staying positioned.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (source-native venue family). The OHLC-plus-calendar-day logic ports across perpetual venues without structural change; the short legs require a shortable instrument, so a spot-only deployment cannot express this rule (disabling the short side would be a different, unpinned rule). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read beyond the UTC-day rollover already pinned, so session-gap behavior needs no approximation; the `dayofmonth` anchor resolves to 00:00 UTC on Binance. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source fills next-bar-open on a 1h-decision/15m-base Binance-futures backtest; this record executes same-bar-close on `1h` BTCUSDT. Backtest economics of the two timings and bases differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- Prose-versus-code gaps (pinned to code): the prose's 9-day stochastic with slow-below-50 longs / fast-above-50 shorts contradicts the coded 14-bar stochastic with `vFast>vSlow`-gated conditions on opposite sides of 50; the prose's daily Elder bars contradict the coded `1h` EMA13 plus session-anchored DayHigh. The record pins the computation; anyone citing the prose label alone would describe a different rule.
- `KSmoothing` rendering gap: mirror table prints `true`, code declares `input(1, minval=1)`, page spin shows `1` — all resolve to effective smoothing length 1. No alternative reading changes any order event, but the reviewer should weigh the table rendering as documented here.
- No price stop and no time stop: adverse excursion after entry has no guardrail beyond agreement loss, which may arrive late; leg-flapping around the Trigger/stochastic lines can compound consecutive whipsaw losses. This is the coded posture, disclosed as the record's principal risk.
- No source cost declaration: no commission, fee, slippage, or funding assumption ships anywhere in the source — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Sparse-signal cost: dual agreement is infrequent by the source's own admission; evaluation windows may hold few trades, and flat stretches earn nothing while remaining exposed to the next whipsaw entry.
- Warmup cost: the adopted 100-bar warmup means the system is blind for the first 100 bars of any 1h evaluation window (structural minimum 16).
- Performance evidence is absent: neither the mirror nor the canonical page reports any number; nothing here is calibrated, fitted, or tuned to the page-embedded 2023-10-21→2023-11-20 window.

## Implementation status

Not implemented. No Hummingbot controller/executor, no Qlib screening, no Paper/Testnet/Live run has been performed from this record. Admission claims pinned-engine expressibility only (see Execution assumptions), subject to independent six-gate review.

## Adoption boundary

Research-only. Not approved for any downstream screening, parity run, or trading authorization. Only a `PASS` under the live six-gate contract may merge this record into `main`; any `NOT_LOSSLESS` finding closes the PR lane without promotion.

## Related Wiki records

None.

## Sources

- Canonical FMZ strategy page (fetched 2026-10-09; title/publisher/created/arguments/backtest header read; code corroborated in page state; no order logic invented): https://www.fmz.com/strategy/432762
- Immutable mirror file actually executed against (full Pine v4 block read end to end; 9680 bytes): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E5%8F%8D%E8%BD%AC%E5%BC%BA%E5%8A%BF%E7%AD%96%E7%95%A5-Elder-Ray-Bull-Power-Combo-Strategy.md
