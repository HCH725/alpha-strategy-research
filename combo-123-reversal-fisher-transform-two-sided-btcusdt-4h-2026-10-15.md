---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: 123-reversal Fisher-transform agreement-gated reversal two-sided on BTCUSDT 4h bars
created: 2026-10-15
updated: 2026-10-15
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-09-13
sources:
  - https://www.fmz.com/strategy/426618
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/123%E5%8F%8D%E8%BD%AC%E4%B8%8E%E8%B4%B9%E5%B8%8C%E5%B0%94%E5%8F%98%E6%8D%A2%E6%8C%87%E6%A0%87%E7%BB%84%E5%90%88%E7%AD%96%E7%95%A5123-Reversal-and-Fisher-Transform-Indicator-Combo-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# 123-reversal Fisher-transform agreement-gated reversal two-sided on BTCUSDT 4h bars

## Provenance

Primary source read end to end (immutable public mirror file plus its recorded FMZ canonical page, fetched 2026-10-15):

- Canonical page: https://www.fmz.com/strategy/426618 (page title `123反转与费希尔变换指标组合策略|123 Reversal and Fisher Transform Indicator Combo Strategy | FMZ`, publisher account `ChaoZhang`, `Created: 2023-09-13 17:35:36`-stamped, equal to the mirror `Last Modified`). Fetched over HTTPS during this cycle (758358 bytes): the page exposes the same six-argument set in order (`Length`, `KSmoothing`, `DLength`, `Level`, `LengthFTI`, `Trade reverse`), the full `/*backtest ... */` header preview quoted below, and the complete order block (2 `strategy.entry` / 1 `strategy.close` in page state — the single close is the `strategy.close_all()` line — quoted verbatim in census). Word-boundary counts over the landing HTML: `Net Profit` 0, `Profit Factor` 0, `Sharpe` 0, `Max Drawdown` 0, `win rate` 0, `Win Rate` 0, `Annualized` 0 — the page ships no performance numbers of any kind (adopted as `source_as_of` 2023-09-13 from the page Created stamp, which equals the mirror `Last Modified`).
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit author date `2025-04-30T03:10:28Z`, subject `update`; verified via the GitHub commits API — the same head pin as the merged KST, Schaff, TRIX, SQZMOM-LB, Aroon, Qstick, AC and Elder-ray-123 admissions), exact file path `123反转与费希尔变换指标组合策略123-Reversal-and-Fisher-Transform-Indicator-Combo-Strategy.md` (non-ASCII filename preserved verbatim; percent-encoded blob URL in Sources). File 6193 bytes, blob SHA `98ebbac55816afff3df44c9dddb6346cf3be2b9a` (verified against the GitHub contents API at the pinned commit — size and SHA both match). The mirror prints `> Detail` = https://www.fmz.com/strategy/426618 and `> Last Modified` = 2023-09-13 17:35:36 (equal to the page Created stamp). Its six-row `> Strategy Arguments` table (15/true/3/50/10/false) agrees with the six pinned `input(...)` declarations (15/1/3/50/10/false) and the page-embedded argument set; the single rendering difference (`KSmoothing` printed `true` in the mirror table versus `input(1, minval=1)` in code and value `1` in page state) resolves to the identical effective smoothing length 1 either way and is fenced in Limitations, never silently picked.
- Full `//@version=4` `strategy(title="Combo Backtest 123 Reversal & Fisher Transform Indicator", shorttitle="Combo", overlay=true)` block read in full (3357 characters, `/*backtest*/` through the final `strategy.close_all()`). The header comment attributes the combo to `Copyright by HPotter v1.0 28/08/2020`, the reversal leg to Ulf Jensen's book `How I Tripled My Money In The Futures Market` page 183, and the Fisher leg to the Gaussianizing formula `y = 0.5 * ln((1+x)/(1-x))` — original-authorship lineage is preserved here, never claimed by the FMZ publisher. The page-embedded `/*backtest*/` header (`start: 2023-08-13 00:00:00`, `end: 2023-09-12 00:00:00` in preview rendering, `period: 4h`, `basePeriod: 15m`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`) is byte-present on both the canonical page preview and the mirror block — market (`BTC_USDT` Binance futures) and decision frame (`4h`) are therefore source-native, never researcher-chosen.
- Text census over the pinned code block: 2 `strategy.entry` / 1 `strategy.close` (the `strategy.close_all()` flat leg) / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=`/`qty_percent` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `volume` / 0 `time(` / 0 `dayofmonth`. `overlay=true` appears once inside the strategy declaration (display only). `pyramiding`, `process_orders_on_close`, `calc_on_every_tick`, `commission`, and `default_qty_*` are unset throughout. Price reads are `close` (14), `high` (4: stoch line plus `hl2` construction), `low` (8: stoch line plus `hl2` construction and `lowest` line); `open` never appears; `hl2` appears once as the Fisher input.
- No risk layer ships anywhere in the source: zero stop/target/trailing/time-exit order legs, and the mirror's own risk prose proposes parameter optimization and money management as future work (`参数优化仍然关键,需要严格的资金管理`), confirming none ships. The agreement-loss flat plus opposite-agreement reversal posture below is therefore the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention.
- Page/mirror performance language is absent entirely (no qualitative praise with numbers, no table, figure, or number) — this record claims no source-reported performance and no reproduced performance.
- Prose-versus-code gaps are pinned to the code, never repaired: (a) the prose describes a 9-day stochastic with slow-below-50 longs / fast-above-50 shorts, but the code computes a 15-bar stochastic with `vFast<vSlow and vFast>50` longs and `vFast>vSlow and vFast<50` shorts; (b) the prose describes three-day gapping 123 price action, but the code tests two consecutive closes (`close[2]` vs `close[1]` vs `close`) gated on the stochastic position. This record pins the computation in both cases; anyone citing the prose alone would describe a different rule. Both gaps are fenced in Limitations.

Licence and rights: the canonical page is a public FMZ strategy publication by ChaoZhang carrying an HPotter copyright header. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly three: (1) same-bar-close fills (the source fills next-bar-open — no `process_orders_on_close` ships anywhere, quoted verbatim in census); (2) an adopted 100-bar warmup with pre-warmup bars flat by record rule (structural minimum is 17 bars — see Required data); (3) house sizing/capital replacing the language-default sizing (no `default_qty_*` ships anywhere — see Execution assumptions). Market (BTCUSDT Binance futures), decision frame (`4h`), and the six defaults are source-native per the page-embedded backtest header and the `input(...)` lines, not adaptations. All three adaptations are predeclared here, confined to Provenance, Signal, Required data, Execution assumptions, and Limitations, with every original claim kept separate above. Indicator formulas, lookbacks, comparisons, state recursion, order IDs, direction handling, the close-all flat leg, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-15): working-tree case-insensitive filename search for `123-reversal-fisher`, `426618`, `lengthfti`, `posfti`, and `fisher-transform-indicator-combo` returns zero strategy records using this source identity or combo title — the sole `426618`-adjacent hit pool-wide is a prose mention inside the KAMA record's combo-embedding fence naming a different 123+KAMA sibling, never this file. Content search for `posReversal123 == 1 and posFTI == 1`, `Combo Backtest 123 Reversal & Fisher`, and `nFish > nz(nFish[1])` returns zero records using this combo (the only `posReversal123` pool hit is the Elder-ray-123 record, which pairs the same 123 leg with a session-anchored DayHigh-minus-EMA Elder leg on `1h` FMZ 432762 — different confirmation leg, different data, different frame; the only `nFish` pool hit is the Fisher zero-cross record, which signals on the signed side of zero `nFish>0` on `1d` TV qhXwZvJ2 — different Fisher event, no 123 leg, no agreement gate). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `elder-ray-123reversal-combo-two-sided-btcusdt-1h-2026-10-09.md` gates the same 123 streak leg on Elder Bull Power (`DayHigh - ema(close,13) > 0` with a UTC-day anchor); this record gates it on Fisher-slope (`nFish > prev`) built from normalized `hl2` — no session anchor, no EMA, no Trigger; `fisher-zero-cross-reversal-btcusdt-1d-2026-10-09.md` holds the signed side of zero with a latched state and reverses two-sided with no flat; this record never tests zero and rests flat on any leg disagreement via `close_all`. Five-axis distinction: source identity differs (FMZ 426618 Sep-2023 HPotter-28/08/2020/Jensen-p183/Fisher lineage versus FMZ 432762 or TV qhXwZvJ2), mechanism differs (two-leg AND-agreement with explicit flat versus single-oscillator latch), signal construction differs (stoch-15/1/3/50 streak AND Fisher-10 slope versus stoch-14 streak AND Elder spread versus Fisher zero-sign), exits differ (agreement-loss `close_all` plus opposite-agreement reversal, no zero-cross exit), and horizon differs (`4h` source-native versus `1h`/`1d`).

## Economic mechanism

### Source-reported

Combo filtering of reversal timing through Gaussianized confirmation (mirror strategy description plus code header): the 123-reversal leg hunts two-consecutive-close streaks faded back by the stochastic position, while the Fisher leg demands the Gaussian-warped `hl2` confirm direction by slope — rising Fisher for longs, falling Fisher for shorts. Only bars where both legs agree open or hold a position; disagreement stands flat. Agreement gating filters single-leg whipsaw at the cost of sparse signals (the mirror's own risk section admits parameter sensitivity and the need for strict money management).

### Research interpretation

Two-gate AND-combo with an explicit neutral state. Unlike always-in-market holders (Qstick, AC records) that must be long or short after warmup, and unlike single-trigger cross systems (KST/Schaff records) that fire once per crossing, this system rests flat whenever the legs disagree — the flat state is a first-class coded outcome (`close_all`), not the absence of a signal. The reversal leg is countertrend in spirit (buy two-up-closes while %K sits above 50 but below %D) while the Fisher leg is pro-slope (warped `hl2` must itself be rising); their conjunction selects streaks whose normalized price warp is already moving with the streak — a narrower, more deliberate trade than either leg alone. Sparse signals are the honestly priced cost (see Negative evidence).

## Signal

Exact rule as pinned (defaults quoted — effective inputs unmodified):

- Declaration (derived): `strategy(title="Combo Backtest 123 Reversal & Fisher Transform Indicator", shorttitle="Combo", overlay=true)` with same-bar-close execution adopted for the derived record (no such argument ships in the source) and house sizing replacing the unset language-default sizing (see Execution assumptions). `calc_on_every_tick` is unset (default false: exactly one evaluation per completed bar). No commission or margin assumption ships anywhere — pinned as absent, with house costs applying to the derived evaluation (see Execution assumptions).
- Inputs (pinned, table- and page-agreeing): `Length=15` (`input(15, minval=1)`), `KSmoothing=1` (`input(1, minval=1)`; table prints `true` — identical effective length, see Provenance), `DLength=3` (`input(3, minval=1)`), `Level=50` (`input(50, minval=1)`), `LengthFTI=10` (`input(10, minval=1)`), `reverse=false` (`input(false, title="Trade reverse")`). Retuning any of them would be a different, unpinned rule.
- Reversal leg (pinned): `vFast = sma(stoch(close, high, low, 15), 1)` (raw 15-bar %K); `vSlow = sma(vFast, 3)` (%D). `posReversal123 = +1` when `close[2] < close[1] and close > close[1] and vFast < vSlow and vFast > 50` (two consecutive up closes with %K above 50 but below %D); `-1` when `close[2] > close[1] and close < close[1] and vFast > vSlow and vFast < 50` (two consecutive down closes with %K below 50 but above %D); otherwise hold `nz(pos[1], 0)`.
- Fisher leg (pinned): `xHL2 = hl2`; `xMaxH = highest(xHL2, 10)`; `xMinL = lowest(xHL2, 10)`; `nValue1 = 0.33*2*((xHL2-xMinL)/(xMaxH-xMinL)-0.5) + 0.67*nz(nValue1[1])`; `nValue2` clamps `nValue1` to `±0.999` via the nested `iff`; `nFish = 0.5*log((1+nValue2)/(1-nValue2)) + 0.5*nz(nFish[1])`. `posFTI = +1` when `nFish > nz(nFish[1])` (rising warp), `-1` when `nFish < nz(nFish[1])` (falling warp), otherwise hold `nz(pos[1], 0)` — a slope test, never a zero test.
- Combo (pinned): `pos = +1` iff `posReversal123 == 1 and posFTI == 1`; `-1` iff both are `-1`; else `0`. `possig = pos` under the pinned `reverse=false`; the `reverse=true` inversion path is disclosed-as-disabled code, never the admitted rule — enabling it would be a different, unpinned rule.
- Entry long: `if (possig == 1) strategy.entry("Long", strategy.long)` — agreement-holding, re-asserted on every completed `4h` bar while both legs agree long, with same-bar-close execution under the derived declaration.
- Entry short: `if (possig == -1) strategy.entry("Short", strategy.short)` — mirror terms. The two `if` statements are separate but their conditions are mutually exclusive on every bar, so at most one entry call fires per bar under any evaluation order — no same-bar long/short conflict exists to resolve.
- Flat leg: `if (possig == 0) strategy.close_all()` — any agreement loss (either leg flips or falls to hold while the other disagrees) closes the whole position at the adopted fill. No stop, no target, no trailing, no time exit — pinned as written, explicitly none, not invented.
- Direction: symmetric two-sided with an explicit flat state. A short-side instrument is required for the short legs; on a spot-only venue they are inexpressible and the record would not be the same rule (see Crypto portability).
- Display isolation: `barcolor(...)` feeds no order condition; order logic reads exactly the two entry conditions plus the flat condition.

## Required data

- Completed `4h` bars of BTCUSDT: `close`, `high`, `low` only (stoch line plus `hl2`-derived Fisher warp via `highest`/`lowest`). No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, or cross-venue state is read by any order-gating line. `hl2` is `(high+low)/2` on the same bar, never a second feed.
- Single decision timeframe `4h` (source-native per the page-embedded `period: 4h` header). The script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction. The header's `basePeriod: 15m` is the FMZ execution granularity of the source backtest, not a signal input — the derived record evaluates completed `4h` bars only and claims no 15m behavior.
- Warmup: the 15-bar stochastic needs 15 completed `4h` bars, `%D = sma(%K, 3)` needs 3 %K values — first fully-windowed reversal state on the 17th completed bar; `highest/lowest(hl2, 10)` is full from bar 10; the `pos[1]`/`nValue1[1]`/`nFish[1]` recursions are defined from the first bar via `nz` (resolving flat/zero). Structural minimum is therefore the 17th completed `4h` bar for the first evaluable combo state; the adopted warmup is the first 100 completed `4h` bars flat by record rule (predeclared researcher choice). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (source-native per the header's `Futures_Binance BTC_USDT`; venue transfer from `BTC_USDT` to `BTCUSDT` spot-symbol spelling is naming only, never presented as a market change).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. The source's own timing is next-bar-open (no execution-timing argument ships anywhere — quoted verbatim in Provenance); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill. With no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. The two entry legs are mutually exclusive every bar (see Signal), and the flat leg fires only when neither entry condition holds, so no ordering resolution is required.
- Engine path for `4h` (gate 5, stated plainly): `4h` is a Binance-documented USDT-M kline interval; the derived rule needs only completed `4h` candles (`close`/`high`/`low` plus same-bar `hl2`) on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no volume-definition dependence, no funding/OI/mark-price leg. That is the same single-frame completed-bar path as the admitted `4h` records and the admitted combo records (Elder-ray-123 on `1h`, DSS-Bressert on `2h`); the stochastic smoothing and Fisher recursion advance deterministically from known closes with `nz` seeds, so no hidden lookahead is ever modeled. Anything beyond that single-frame completed-bar path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: no `default_qty_*`, commission, or margin assumption ships anywhere (quoted verbatim in census) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions replace the unset language defaults here, never presented as source-native behavior. Historical funding is flagged per the house baseline: no campaign may claim complete realized-funding performance without a verified implementation.
- Concurrency: no `pyramiding` ships anywhere, pinning the language default of no same-direction adds — at most one unit per side under fixed order IDs `Long`/`Short`; repeat same-agreement entries while positioned are no-ops, the opposite-agreement entry reverses (closes the current side and opens the opposite in one transition), and any agreement loss closes all via the coded flat leg. Re-entry is allowed immediately on the next qualifying agreement after any flat (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The mirror ships the full two-leg construction (stoch 15/1/3/50 streak conditions, Fisher-10 normalized warp with slope state, triple-AND combo with `close_all` flat), the two agreement-holding order legs with their order IDs, the six inputs, the HPotter/Jensen/Fisher authorship header, and the page-embedded 4h/15m August-September-2023 backtest header. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=`/`qty_percent` — the sole position-closing paths are the coded `close_all` flat leg and opposite-agreement reversal. The absence is coded (the block ends with the flat leg and the display call after the two entries), and the mirror's risk prose proposes optimization and money management as future work, corroborating that none ships — fenced in Limitations for the reviewer rather than upgraded into a source claim.
2. Entry legs are mutually exclusive on every bar by value (`possig` is a single integer that cannot equal 1 and -1 at once), and the flat leg fires only when `possig == 0`, so no single bar can satisfy more than one order leg even though they sit in separate `if` statements.
3. Exit-leg conditionality, admitted plainly: a long opened on dual agreement exits only when agreement breaks (either leg flips or holds-against). A market that keeps both legs aligned never exits until they diverge — there is no time-stop to cut a stale agreement, and choppy leg-flapping around the stochastic Level or the Fisher slope can whipsaw the system in and out of flat. This is the coded trade, disclosed, not a tunable parameter here.
4. Sparsity is structural: both legs must agree, and the mirror's own risk section warns of parameter sensitivity. Long evaluation windows may contain few or zero trades; this record treats trade scarcity as the strategy's honest cost, never as a reason to loosen the AND into an OR (which would be a different, unpinned rule).
5. Boundary ties hold, never fire: exactly-equal consecutive closes satisfy neither streak condition (strict inequalities); exactly-equal Fisher prints (`nFish == prev`) inherit prior Fisher state via `nz(pos[1], 0)`; exactly-50 %K satisfies neither streak side; a zero-range Fisher window (`xMaxH == xMinL`) divides by zero and yields `na`, which falsifies every comparison it touches so the bar holds prior state; warmup bars are flat by record rule.
6. The stochastic length (15), smoothing chain (1/3), Level (50), two-close streak definition, Fisher length (10), warp constants (0.33/0.67/0.999/0.5), fixed order IDs, symmetric states, the `close_all` flat leg, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning a length, enabling reverse, adding a stop/target/cooldown, switching source series, replacing slope with zero-sign, or disabling a side would each be a different, unpinned rule — none is admitted here.
7. Derivation boundary fenced: the only non-source-native behaviors in this record are same-bar-close fills, the adopted 100-bar warmup with record-rule pre-warmup flat, and house sizing — all predeclared above; market, timeframe, every signal, threshold, default, transition, flat leg, and risk posture are source-verbatim. This record is therefore never evidence that the original next-bar-open 4h/15m source itself passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: stoch 15/1/3/50 / two-close streak / Fisher-10 warp / slope state / dual-agreement gate / `close_all` flat / `reverse=false` / symmetric entries / `4h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Agreement relevance: replacing the AND-combo with either leg alone (reversal-only, Fisher-slope-only) must not improve net expectancy; fail ⇒ the agreement gate adds nothing over its parts.
- F2 — Fisher-leg relevance: replacing the Fisher-slope leg with a hold-true gate (reversal-only with the same flat semantics) must not improve net expectancy; fail ⇒ the Gaussian warp adds nothing over the streak leg.
- F3 — Flat-state relevance: removing the `close_all` leg (holding the last side through disagreement, reversal-only) must not improve net expectancy; fail ⇒ the explicit flat state is dominated by simply staying positioned.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (source-native venue family). The OHLC-only logic ports across perpetual venues without structural change; the short legs require a shortable instrument, so a spot-only deployment cannot express this rule (disabling the short side would be a different, unpinned rule). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read beyond completed `4h` bars, so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source fills next-bar-open on a 4h-decision/15m-base Binance-futures backtest; this record executes same-bar-close on `4h` BTCUSDT. Backtest economics of the two timings and bases differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- Stanza labels: the mirror prints `basePeriod: 15m` alongside `period: 4h` (quoted verbatim, never normalized); this record decides and fills on completed `4h` bars only. The stanza window (2023-08-13 to 2023-09-12) is a quoted label, not a claimed result; no performance is asserted over it.
- Prose-versus-code gaps (pinned to code): the prose's 9-day stochastic with slow-below-50 longs / fast-above-50 shorts contradicts the coded 15-bar stochastic with opposite-side `vFast`-vs-`vSlow` gating; the prose's three-day gapping description contradicts the coded two-consecutive-close test. The record pins the computation; anyone citing the prose label alone would describe a different rule.
- `KSmoothing` rendering gap: mirror table prints `true`, code declares `input(1, minval=1)`, page state shows `1` — all resolve to effective smoothing length 1. No alternative reading changes any order event, but the reviewer should weigh the table rendering as documented here.
- No price stop and no time stop: adverse excursion after entry has no guardrail beyond agreement loss, which may arrive late; leg-flapping around the Level-50 line or Fisher-slope equality can compound consecutive whipsaw losses. This is the coded posture, disclosed as the record's principal risk.
- No source cost declaration: no commission, fee, slippage, or funding assumption ships anywhere in the source — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Sparse-signal cost: dual agreement is infrequent by the source's own sensitivity warning; evaluation windows may hold few trades, and flat stretches earn nothing while remaining exposed to the next whipsaw entry.
- Warmup cost: the adopted 100-bar warmup means the system is blind for the first 100 bars of any 4h evaluation window (structural minimum 17).
- Performance evidence is absent: neither the mirror nor the canonical page reports any number; nothing here is calibrated, fitted, or tuned to the page-embedded 2023-08-13→2023-09-12 window.
- Licence: the executable source carries an HPotter copyright header via the FMZ porter page — downstream implementation must honor its terms; this record copies no code block.

## Implementation status

Not implemented. No Hummingbot controller/executor, no Qlib screening, no Paper/Testnet/Live run has been performed from this record. Admission claims pinned-engine expressibility only (see Execution assumptions), subject to independent six-gate review.

## Adoption boundary

Research-only. Not approved for any downstream screening, parity run, or trading authorization. Only a `PASS` under the live six-gate contract may merge this record into `main`; any `NOT_LOSSLESS` finding closes the PR lane without promotion.

## Related Wiki records

None.

## Sources

- Canonical FMZ strategy page (fetched 2026-10-15; title/publisher/created/arguments/backtest header read; code corroborated in page state; no order logic invented): https://www.fmz.com/strategy/426618
- Immutable mirror file actually executed against (full Pine v4 block read end to end; 6193 bytes): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/123%E5%8F%8D%E8%BD%AC%E4%B8%8E%E8%B4%B9%E5%B8%8C%E5%B0%94%E5%8F%98%E6%8D%A2%E6%8C%87%E6%A0%87%E7%BB%84%E5%90%88%E7%AD%96%E7%95%A5123-Reversal-and-Fisher-Transform-Indicator-Combo-Strategy.md
