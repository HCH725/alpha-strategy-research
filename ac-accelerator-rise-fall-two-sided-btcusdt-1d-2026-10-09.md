---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: AC accelerator rise-fall trend two-sided on BTCUSDT 1d bars
created: 2026-10-09
updated: 2026-10-09
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-12-18
sources:
  - https://www.fmz.com/strategy/435716
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E5%A8%81%E5%BB%89%E6%8C%87%E6%A0%87%E7%9A%84%E7%B2%BE%E5%A6%99%E9%9C%87%E8%8D%A1%E5%99%A8AC%E5%9B%9E%E6%B5%8B%E7%AD%96%E7%95%A5AC-Backtest-Strategy-of-Williams-Indicator.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# AC accelerator rise-fall trend two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (immutable public mirror file plus its recorded FMZ canonical page, fetched 2026-10-09):

- Canonical page: https://www.fmz.com/strategy/435716 (`AC Backtest Strategy of Williams Indicator`, publisher account `ChaoZhang`, page title `AC Backtest Strategy of Williams Indicator | FMZ`, `Created: 2023-12-18 12:03:38`). Fetched over HTTPS during this cycle (762448 bytes): the page exposes the three strategy arguments (`Length Slow` spin `34`, `Length Fast` spin `5`, `Trade reverse` switch off), the full `/*backtest ... */` header preview quoted below, and the complete order block (`2 strategy.entry` in page state, quoted verbatim in census), followed by a `Login to view full source` wall after the rendered preview — so the immutable mirror below is the executed code source, with the page serving as title/author/argument/header corroboration. Word-boundary counts over the whole landing HTML: `Net Profit` 0, `Profit Factor` 0, `Sharpe` 0, `Max Drawdown` 0, `win rate` 0, `Win Rate` 0, `Annualized` 0, `Return` 0 — the page ships no performance numbers of any kind (adopted as `source_as_of` 2023-12-18 from the page Created stamp, which equals the mirror `Last Modified`).
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit date 2025-04-30 11:10:28 +0800, subject `update`; verified repository head at research time via the GitHub commits API — the same head pin as the merged KST, Schaff, TRIX, SQZMOM-LB, Aroon and Qstick admissions), exact file path `威廉指标的精妙震荡器AC回测策略AC-Backtest-Strategy-of-Williams-Indicator.md` (non-ASCII filename preserved verbatim; percent-encoded blob URL in Sources). File 7255 bytes, blob SHA `b0a9a360667a990c68d147fba5e3e775b71fd3af`. The mirror prints `> Detail` = https://www.fmz.com/strategy/435716 and `> Last Modified` = 2023-12-18 12:03:38 (equal to the page Created stamp). Its three-row `> Strategy Arguments` table (34/5/false) agrees exactly with the three pinned `input(...)` declarations and the page-embedded argument triple, so there is no table-versus-code-versus-page conflict.
- Full `//@version=2` `strategy("Bill Williams. Awesome Oscillator (AC)")` block read in full. The header comment attributes the oscillator to `Copyright by HPotter v1.0 28/12/2016` and names Bill Williams as the Awesome Oscillator designer — original-authorship lineage is preserved here, never claimed by the FMZ publisher. The page-embedded `/*backtest*/` header (`start: 2022-12-11 00:00:00`, `end: 2023-12-17 23:59:59` in preview rendering, `period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`) is byte-present on both the canonical page preview and the mirror block — market (`BTC_USDT` Binance futures) and decision frame (`1d`) are therefore source-native, never researcher-chosen.
- Text census over the pinned code block (1550 characters, `//@version=2` through the final `plot(...)`): 2 `strategy.entry` / 0 `strategy.exit` / 0 `strategy.close` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=`/`qty_percent` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `volume` / 0 `dayofmonth` / 0 `time(`. The only price series read anywhere is `hl2` (two code reads, both inside the two `sma(hl2, ...)` lines); `high`/`low`/`close`/`open` never appear as bare series. `pyramiding`, `process_orders_on_close`, `calc_on_every_tick`, `commission`, `default_qty_*`, `margin_*`, and `overlay` are unset throughout.
- No risk layer ships anywhere in the source: zero stop/target/trailing/time-exit lines and no risk prose beyond generic caution in the mirror's `风险及解决方法` section (adding stops is listed as future optimization, never as shipped behavior). The rise-holding reversal-only exit posture below is therefore the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention — but there is no source sentence declaring the absence, which is fenced honestly in Limitations for the reviewer (same posture as the merged Qstick record).
- Page/mirror performance language is absent entirely (no qualitative praise, no table, figure, or number) — this record claims no source-reported performance and no reproduced performance.
- Label honesty: the prose and strategy title call the system "Awesome Oscillator (AO)", but the code computes AO minus its own 5-bar SMA (`xSMA1_SMA2 - xSMA_hl2`), i.e. the Accelerator-style second-difference quantity, and trades its rise versus fall — never a zero-line cross of AO itself. This record pins the computed quantity and its rise/fall rule, never the prose label; the mismatch is fenced in Limitations, not repaired.

Licence and rights: the canonical page is a public FMZ strategy publication by ChaoZhang carrying an HPotter copyright header. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly three: (1) same-bar-close fills (the source fills next-bar-open — no `process_orders_on_close` ships anywhere, quoted verbatim in census); (2) an adopted 100-bar warmup with pre-warmup bars flat by record rule (structural minimum is 38 bars — see Required data); (3) house sizing/capital replacing the language-default sizing (no `default_qty_*` ships anywhere — see Execution assumptions). Market (BTCUSDT Binance futures) and decision frame (`1d`) are source-native per the page-embedded backtest header, not adaptations. All three adaptations are predeclared here, confined to Provenance, Signal, Required data, Execution assumptions, and Limitations, with every original claim kept separate above. Indicator formula, lookbacks, rise/fall comparisons, state recursion, order IDs, direction handling, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-09): working-tree word-boundary searches for `awesome`, `accelerator`, `435716`, `elder-ray`, `bull-power`, `vhf`, and `vertical-horizontal` return zero strategy records using this source, author strategy, or mechanism. Same-publisher ChaoZhang records exist (KST FMZ 436493, Schaff FMZ 365905, TRIX FMZ 428683, Aroon FMZ 438795, Qstick FMZ 439854) but carry different canonical identities, different indicator families, and different order sets. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #58 (17-file ML/reconstruction batch — file list verified, no oscillator record), and #63 (SuperTrend ATR-flip trend long) — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `williams-r-level-cross-mean-reversion-long-btcusdt-1d` is a Williams %R threshold-cross mean-reversion long-only system (different Williams indicator, edge-triggered, long-only), `vidya-cmo-adaptive-slope-trend-btcusdt-1h` is an adaptive-average slope system, `rsi-classic-level-reversal-btcusdt-1h` is a single-oscillator level system. Five-axis distinction: mechanism differs (second-difference momentum rise/fall regime holding, symmetric two-sided), signal construction differs (no pool record evaluates `sma(hl2,5)-sma(hl2,34)` minus its own 5-bar SMA with bar-to-bar rise/fall recursion), exits differ (opposite-rise reversal only, no band/trailing/tick exits), source identity differs (FMZ 435716 Dec-2023 ChaoZhang/HPotter/Bill-Williams lineage versus other FMZ IDs or TV authors), and direction handling differs (rising-momentum holding long, falling-momentum holding short — versus threshold-cross, gated, or long-only records).

## Economic mechanism

### Source-reported

Bill Williams momentum-diagnosis via a double-smoothed median-price spread (mirror `策略原理`, corroborated by the code header): the Awesome Oscillator takes the fast/slow SMA spread of median price, and this strategy smooths it once more with a 5-bar SMA — the residual (spread minus its own average) reads as acceleration. A rising residual prints a blue histogram bar (buying regime); a non-rising residual prints red (selling regime). The mirrorJudges trend and momentum from the fast/slow median-price structure rather than from closes alone, filtering single-bar noise at the cost of lag.

### Research interpretation

Two-sided acceleration-regime holding on a median-price double spread. Unlike edge-triggered cross systems (KST/Schaff records) that fire once per crossing, and unlike the Qstick zero-level holder, this is a rise/fall holder: every completed bar re-asserts the side dictated by the bar-to-bar change of the residual, so the system is always positioned after warmup (long or short), never resting flat except on exactly-equal holds. The double smoothing (34-slow outer, 5-inner) filters chop at the cost that adverse excursion has no guardrail except the residual turning down, which may arrive late (see Limitations). This record must be read as a pure always-in-the-market reversal system, never as a risk-managed one.

## Signal

Exact rule as pinned (defaults quoted — effective inputs unmodified):

- Declaration (derived): `strategy("Bill Williams. Awesome Oscillator (AC)")` with same-bar-close execution adopted for the derived record (no such argument ships in the source) and house sizing replacing the unset language-default sizing (see Execution assumptions). `calc_on_every_tick` is unset (default false: exactly one evaluation per completed bar). No commission, margin, or overlay assumption ships anywhere — pinned as absent, with house costs applying to the derived evaluation (see Execution assumptions).
- Inputs (pinned, table- and page-agreeing): `Length Slow=34` (`input(34, minval=1)`), `Length Fast=5` (`input(5, minval=1)`), `reverse=false` (`input(false, title="Trade reverse")`). Retuning any of them would be a different, unpinned rule.
- Indicator (pinned): `xSMA1_hl2 = sma(hl2, 5)`; `xSMA2_hl2 = sma(hl2, 34)`; `xSMA1_SMA2 = xSMA1_hl2 - xSMA2_hl2` (the AO-style spread); `xSMA_hl2 = sma(xSMA1_SMA2, 5)`; `nRes = xSMA1_SMA2 - xSMA_hl2` (the traded accelerator-style residual).
- State recursion (pinned): `pos = +1` when `nRes > nRes[1]`, `-1` when `nRes < nRes[1]`, otherwise hold `nz(pos[1], 0)` — exactly-equal bars inherit the prior bar's state, and the very first bar resolves to `0` (flat, no order). `possig = pos` under the pinned `reverse=false`; the `reverse=true` inversion path is disclosed-as-disabled code, never the admitted rule — enabling it would be a different, unpinned rule.
- Entry long: `if (possig == 1) strategy.entry("Long", strategy.long)` — rise-holding, re-asserted on every completed `1d` bar while the residual keeps rising, with same-bar-close execution under the derived declaration.
- Entry short: `if (possig == -1) strategy.entry("Short", strategy.short)` — mirror terms. The two `if` statements are separate but their conditions are mutually exclusive on every bar (`possig` cannot equal both), so at most one entry call fires per bar under any evaluation order — no same-bar long/short conflict exists to resolve.
- Exits: none coded. The sole exit path is opposite-rise reversal (a falling residual while long reverses to short and vice versa). No stop, no target, no trailing, no time exit — pinned as written, explicitly none, not invented.
- Direction: symmetric two-sided by pinned rise/fall; flat is entered only via the exactly-equal state hold (and the first-bar zero). A short-side instrument is required for the short legs; on a spot-only venue they are inexpressible and the record would not be the same rule (see Crypto portability).
- Display isolation: `cClr`, `barcolor(...)`, and `plot(nRes, style=histogram, ...)` feed no order condition; order logic reads exactly the two rise/fall conditions.

## Required data

- Completed `1d` bars of BTCUSDT: `hl2` (i.e. `high` and `low`) only, via the two `sma(hl2, ...)` lines. No `close`, no `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (source-native per the page-embedded `period: 1d` header). The script takes no timeframe input and makes no live `request.*` call, so it is single-frame by construction. The header's `basePeriod: 1h` is the FMZ execution granularity of the source backtest, not a signal input — the derived record evaluates completed `1d` bars only and claims no 1h behavior.
- Warmup: the slow leg `sma(hl2, 34)` needs 34 completed `1d` bars for its first full window, the spread is full from bar 34, and the inner `sma(spread, 5)` needs 5 spreads — first fully-windowed residual on the 38th completed `1d` bar; the `nRes[1]` comparison and `pos[1]` recursion are defined from the first bar via `nz` (resolving flat). Structural minimum is therefore the 38th completed `1d` bar for the first evaluable rise/fall state; the adopted warmup is the first 100 completed `1d` bars flat by record rule (predeclared researcher choice). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (source-native per the header's `Futures_Binance BTC_USDT`; venue transfer from `BTC_USDT` to `BTCUSDT` spot-symbol spelling is naming only, never presented as a market change).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. The source's own timing is next-bar-open (no execution-timing argument ships anywhere — quoted verbatim in Provenance); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill. With no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. The two order legs are mutually exclusive every bar (see Signal), so no ordering resolution is required.
- Sizing/capital/costs: no `default_qty_*`, commission, or margin assumption ships anywhere (quoted verbatim in census) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions replace the unset language defaults here, never presented as source-native behavior.
- Concurrency: no `pyramiding` ships anywhere, pinning the language default of no same-direction adds — at most one unit per side under fixed order IDs `Long`/`Short`; repeat same-rise entries while positioned are no-ops and the opposite-fall entry reverses (closes the current side and opens the opposite in one transition). Re-entry is allowed immediately on the next qualifying opposite state after any reversal (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The mirror ships the full double-spread construction (`sma(hl2,5)`, `sma(hl2,34)`, spread, spread's 5-bar SMA, residual), the two rise-holding order legs with their order IDs, the `34` / `5` / `false` inputs, the HPotter/Bill-Williams authorship header, and the page-embedded 1d/1h December-2022→December-2023 backtest header. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.close`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=`/`qty_percent` — the opposite-rise reversal is the sole exit path by construction. The absence is coded (the block ends with display calls after the two entries), though no source sentence declares it — fenced in Limitations for the reviewer rather than upgraded into a source claim.
2. Entry legs are mutually exclusive on every bar by value (`possig` is a single integer that cannot equal 1 and -1 at once), so no single bar can satisfy both even though they sit in separate `if` statements.
3. Exit-leg conditionality, admitted plainly: a long opened on a rising residual exits only on a later falling residual. Choppy oscillation of the residual around flat can whipsaw the system; a strong one-direction drift never exits until the residual actually turns non-rising — there is no time-stop to cut either behavior. This is the coded trade, disclosed, not a tunable parameter here.
4. Boundary ties hold, never fire: exactly-equal residuals inherit prior state via `nz(pos[1], 0)`; a residual pinned exactly flat holds the existing side (or stays flat before the first signal); warmup bars are flat by record rule.
5. Flat-state determinism: with no open position both rise legs are live candidates each bar (rise-holding, so the first post-warmup non-equal residual always opens a position); post-warmup the system is always positioned after its first signal; same-side repeats are no-ops under the pinned no-add default.
6. The median-price source (`hl2`), both lengths (34/5), the double-spread construction, the rise/fall comparisons, the recursive hold, the `reverse=false` stance, the fixed order IDs, the symmetric states, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning a length, enabling reverse, adding a stop/target/cooldown, switching source series, inserting a zero-line cross, or disabling a side would each be a different, unpinned rule — none is admitted here.
7. Derivation boundary fenced: the only non-source-native behaviors in this record are same-bar-close fills, the adopted 100-bar warmup with record-rule pre-warmup flat, and house sizing — all predeclared above; market, timeframe, every signal, threshold, default, transition, and risk posture are source-verbatim. This record is therefore never evidence that the original next-bar-open 1d/1h source itself passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `sma(hl2,5)-sma(hl2,34)` spread / inner SMA 5 / residual rise-fall recursion / `reverse=false` / symmetric rise entries / reversal-only exits / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Smoothing relevance: replacing the inner 5-bar smoothing with the raw AO-style spread crossed against zero (long above, short below) must not improve net expectancy; fail ⇒ the accelerator residual adds nothing over the plain spread.
- F2 — Source relevance: replacing the `hl2` median-price source with `close` under identical lengths must not improve net expectancy; fail ⇒ the median-price construction adds nothing over closes.
- F3 — Holding relevance: adding a time-stop (flat after N bars without an opposite state) must not improve net expectancy; fail ⇒ the pure always-in-market holding rule is dominated by simply cutting stale positions.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (source-native venue family). The median-price-only logic ports across perpetual venues without structural change; the short legs require a shortable instrument, so a spot-only deployment cannot express this rule (disabling the short side would be a different, unpinned rule). No funding-dependent leg, no stablecoin-specific assumption, no session, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read beyond the per-bar `high`/`low` pair already pinned, so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source fills next-bar-open on a 1d-decision/1h-base Binance-futures backtest; this record executes same-bar-close on `1d` BTCUSDT. Backtest economics of the two timings and bases differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- Label-versus-code gap: prose calls the traded quantity the Awesome Oscillator, but the code trades AO minus its own 5-bar SMA (accelerator-style residual) on rise/fall, never an AO zero-cross. The record pins the computation; anyone citing the prose label alone would describe a different rule.
- No price stop and no time stop: adverse excursion after entry has no guardrail beyond the opposite state, which may arrive late; whipsaw of the residual around flat can compound consecutive reversal losses. This is the coded posture, disclosed as the record's principal risk.
- No source cost declaration: no commission, fee, slippage, or funding assumption ships anywhere in the source — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Undeclared absence: the source is silent about risk — the no-stop reading rests on the code (the block ends with display calls after the entries) rather than on any source sentence. The reviewer should weigh this silence as documented here.
- Warmup cost: the adopted 100-bar warmup means the system is blind for the first 100 bars of any 1d evaluation window (structural minimum 38).
- Performance evidence is absent: neither the mirror nor the canonical page reports any number; nothing here is calibrated, fitted, or tuned to the page-embedded 2022-12-11→2023-12-17 window.

## Implementation status

Not implemented. No Hummingbot controller/executor, no Qlib screening, no Paper/Testnet/Live run has been performed from this record. Admission claims pinned-engine expressibility only (see Execution assumptions), subject to independent six-gate review.

## Adoption boundary

Research-only. Not approved for any downstream screening, parity run, or trading authorization. Only a `PASS` under the live six-gate contract may merge this record into `main`; any `NOT_LOSSLESS` finding closes the PR lane without promotion.

## Related Wiki records

None.

## Sources

- Canonical FMZ strategy page (fetched 2026-10-09; title/publisher/created/arguments/backtest header read; code corroborated in page state; no order logic invented): https://www.fmz.com/strategy/435716
- Immutable mirror file actually executed against (full Pine v2 block read end to end; 7255 bytes): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E5%A8%81%E5%BB%89%E6%8C%87%E6%A0%87%E7%9A%84%E7%B2%BE%E5%A6%99%E9%9C%87%E8%8D%A1%E5%99%A8AC%E5%9B%9E%E6%B5%8B%E7%AD%96%E7%95%A5AC-Backtest-Strategy-of-Williams-Indicator.md
