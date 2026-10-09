---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: KST signal-cross trend two-sided on BTCUSDT 1h bars
created: 2026-10-09
updated: 2026-10-09
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-12-26
sources:
  - https://www.fmz.com/strategy/436493
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/KST%E7%AD%96%E7%95%A5.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# KST signal-cross trend two-sided on BTCUSDT 1h bars

## Provenance

Primary source read end to end (immutable public mirror file plus its recorded FMZ canonical page, fetched 2026-10-09):

- Canonical page: https://www.fmz.com/strategy/436493 (`KST策略`, author account `镜花水月`, page title `KST策略 | FMZ`, `Created` = 2023-12-25 12:16:58). Fetched over HTTPS during this cycle (733826 bytes): the page exposes the five strategy arguments (`v_input_1` … `v_input_5`, ROC1/ROC2/ROC3/ROC4/SMA1), the `/*backtest*/` header, and a truncated code preview (387 rendered characters, cut mid-declaration) followed by `Login to view full source` — so no order logic was taken from the canonical page itself. Word-boundary counts over the whole landing HTML: `Net Profit` 0, `Profit Factor` 0, `Sharpe` 0, `Max Drawdown` 0, `ROI` 0, `win rate` 0, `Backtest result` 0 — the page ships no performance numbers of any kind (only site copy/hit tallies, named here as unusable water, never performance).
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit date 2025-04-30 11:10:28 +0800, subject `update`; verified repository head at research time via the GitHub commits API — the same head pin as the merged Schaff, TRIX, SQZMOM-LB and Aroon admissions), exact file path `KST策略.md` (non-ASCII filename preserved verbatim; percent-encoded blob URL in Sources). File 1276 bytes, blob SHA `386c16f115887af49e9972c2c4529a7bce570ef4`, SHA-256 `45c2fd8e56af54ad1cbf9ef48e20d7db301751af34a93324cda8ae5527aa561e`. The mirror prints `> Detail` = https://www.fmz.com/strategy/436493 and `> Last Modified` = 2023-12-26 11:25:30 (adopted as `source_as_of`).
- Full `//@version=4` `strategy("KST策略", overlay = false, pyramiding=1, default_qty_type= strategy.percent_of_equity, default_qty_value = 100, commission_type=strategy.commission.percent, commission_value=0.07)` block read in full. The mirror's five-row `> Strategy Arguments` table (10/15/20/30/9) agrees exactly with the five pinned `input(...)` declarations, so there is no table-versus-code conflict. The page-embedded `/*backtest*/` header (`start: 2022-11-28 00:00:00`, `end: 2023-12-04 00:00:00`, `period: 1h`, `basePeriod: 15m`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`) is byte-present on both the canonical page and the mirror block — market (`BTC_USDT` Binance futures) and decision frame (`1h`) are therefore source-native, never researcher-chosen.
- Text census over the pinned block: 2 `strategy.entry` / 0 `strategy.exit` / 0 `strategy.close` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `volume` / 0 `high` / 0 `low` / 0 `open`. The only price series read anywhere is `close` (4 reads, one per `roc(close, …)`); `process_orders_on_close`, `calc_on_every_tick`, and any stop/target identifier are unset throughout.
- No risk layer ships anywhere in the source: zero stop/target/trailing/time-exit lines and no risk prose on either the mirror or the canonical page. The reversal-only exit posture below is therefore the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention — but there is no source sentence declaring the absence, which is fenced honestly in Limitations for the reviewer (same posture as the merged Schaff record).
- Transcription note, stated verbatim rather than repaired: the file prints `ta.crossover(KST,signal)` / `ta.crossunder(KST,signal)` under its `//@version=4` declaration line. This record pins the version-invariant edge semantics both spellings denote (strict cross above / cross below on the completed bar) and quotes the calls exactly as printed; the namespace prefix alters no threshold, lookback, or transition pinned below. The reviewer should weigh this note as documented here.
- Page/mirror performance language is absent entirely (no qualitative praise, no table, figure, or number) — this record claims no source-reported performance and no reproduced performance.

Licence and rights: the canonical page is a public FMZ strategy publication by 镜花水月. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly three: (1) same-bar-close fills (the source fills next-bar-open — no `process_orders_on_close` ships anywhere, quoted verbatim in census); (2) an adopted 100-bar warmup with pre-warmup bars flat by record rule (structural minimum is 53 bars — see Required data); (3) house sizing/capital replacing `percent_of_equity 100` language-default sizing (see Execution assumptions). Market (BTCUSDT Binance futures) and decision frame (`1h`) are source-native per the page-embedded backtest header, not adaptations. All three adaptations are predeclared here, confined to Provenance, Signal, Required data, Execution assumptions, and Limitations, with every original claim kept separate above. Indicator formulas, lookbacks, weights, signal smoothing, trigger semantics, pyramiding, commission, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-09): working-tree word-boundary searches for `kst`, `436493`, and `know sure` return zero strategy records using this source, author strategy, or mechanism — the only contiguous `kst` hits anywhere are inside the English word fragment of the merged Bookstaber record's title (`Bookstaber`), never a mechanism. Same-mirror authors exist (ChaoZhang Aroon FMZ 438795, TRIX FMZ 428683, Schaff FMZ 365905) but carry different canonical identities, different indicator families, and different order sets. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #58 (ML/portfolio reconstruction batch — file list verified, no KST record), and #63 (SuperTrend ATR-flip trend long) — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `trix-dual-band-trend-btcusdt-1d` is a triple-EMA percent-change dual-line band system, `stochastic-ott-dual-trend-btcusdt-1d` is a price-rank %K/%D stochastic plus OTT trailing system, `drm-dynamic-rsi-momentum-btcusdt-1d` is a single-RSI smoothing-race system. Five-axis distinction: mechanism differs (weighted four-horizon ROC-sum Know-Sure-Thing momentum with signal-line cross, two-sided with reversal), signal construction differs (no pool record evaluates `sma(roc(close,10),10) + 2*sma(roc(close,15),10) + 3*sma(roc(close,20),10) + 4*sma(roc(close,30),15)` against its own 9-bar SMA), exits differ (opposite signal-line cross reversal only, no band/trailing/tick exits), source identity differs (FMZ 436493 Dec-2023 by 镜花水月 versus other FMZ IDs or TV authors), and direction handling differs (symmetric two-sided: every cross up is long, every cross down is short — versus band-gated, long-only, or trailing-gated records).

## Economic mechanism

### Source-reported

None beyond the construction itself: the mirror and canonical page ship no mechanism prose (no Pring-theory paragraph, no regime claim). The coded economics are readable directly — the KST compresses four horizons of rate-of-change into one weighted momentum sum (longer horizons dominate via weights 1/2/3/4) and trades its crossings against a 9-bar signal average: crossing up prices broadening upside momentum (long), crossing down prices broadening downside momentum (short). Each side is held until the opposite cross reverses it. No stop, no target, no trailing order ships anywhere.

### Research interpretation

Two-sided momentum-regime harvesting on a smoothed multi-horizon ROC aggregate. Unlike single-lookback oscillators (RSI records) that fire on level breaches, both entries here are relational events between the aggregate and its own moving average — the system is always positioned after warmup (long or short), never resting flat except by reversal transit. The four-horizon weighting makes the aggregate slower and more deliberate than any single ROC leg, at the cost that adverse excursion has no guardrail except the opposite cross, which may arrive late (see Limitations). This record must be read as a pure reversal system, never as a risk-managed one.

## Signal

Exact rule as pinned (defaults quoted — effective inputs unmodified):

- Declaration (derived): `strategy("KST策略", overlay = false, pyramiding=1, …)` with same-bar-close execution adopted for the derived record (no such argument ships in the source) and house sizing replacing `percent_of_equity 100` (see Execution assumptions). `pyramiding=1` is source-native and load-bearing (see position state below). `calc_on_every_tick` is unset (default false: exactly one evaluation per completed bar). `commission_value=0.07` percent is pinned as the source cost assumption (house costs apply to the derived evaluation — see Execution assumptions).
- Inputs (pinned, table-agreeing): `ROC1=10`, `ROC2=15`, `ROC3=20`, `ROC4=30`, `SMA1=9` — all untyped `input(...)` integer-inferred. Retuning any of them, or resmoothing any leg, would be a different, unpinned rule.
- Aggregate (pinned): `ROCma1 = sma(roc(close,10),10)`; `ROCma2 = sma(roc(close,15),10)`; `ROCma3 = sma(roc(close,20),10)`; `ROCma4 = sma(roc(close,30),15)`; `KST = ROCma1 + ROCma2*2 + ROCma3*3 + ROCma4*4`; `signal = sma(KST,9)`.
- Entry long: cross of KST above signal (`KST[1] <= signal[1] and KST > signal`) → `strategy.entry("L",strategy.long)` — evaluated on the completed-bar close with same-bar-close execution under the derived declaration.
- Entry short: cross of KST below signal (`KST[1] >= signal[1] and KST < signal`) → `strategy.entry("S",strategy.short)` — mirror terms.
- Disabled gating (pinned as disabled, never invented): both order lines trail commented zero-line filters (`//and KST >= 0 //and signal >=0` on the long leg, `//and KST <= 0 //and signal <=0` on the short leg). They are comments, not code — this record does not enforce them, and enforcing them would be a different, unpinned rule.
- Exits: none coded. The sole exit path is opposite-entry reversal (a short cross while long reverses to short and vice versa). No stop, no target, no trailing, no time exit — pinned as written, explicitly none, not invented.
- Direction: symmetric two-sided by pinned crosses; flat is entered only transiently via reversal (no standalone flat signal). A short-side instrument is required for the short legs; on a spot-only venue they are inexpressible and the record would not be the same rule (see Crypto portability).
- Display isolation: `hline(0)` and the two `plot(...)` calls feed no order condition; order logic reads exactly the two cross conditions.

## Required data

- Completed `1h` bars of BTCUSDT: `close` only (via the four `roc(close, …)` legs). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1h` (source-native per the page-embedded `period: 1h` header). The script takes no timeframe input and makes no live `request.*` call, so it is single-frame by construction. The header's `basePeriod: 15m` is the FMZ execution granularity of the source backtest, not a signal input — the derived record evaluates completed `1h` bars only and claims no 15m behavior.
- Warmup: `roc(close,30)` needs 31 bars for its first full window; `sma(…,15)` needs 15 ROC values, so all four smoothed legs are full from the 45th completed `1h` bar; `signal = sma(KST,9)` needs 9 aggregate values, so the full signal pair is defined from the 53rd completed bar. Structural minimum is therefore the 53rd completed `1h` bar; the adopted warmup is the first 100 completed `1h` bars flat by record rule (predeclared researcher choice). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (source-native per the header's `Futures_Binance BTC_USDT`; venue transfer from `BTC_USDT` to `BTCUSDT` spot-symbol spelling is naming only, never presented as a market change).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. The source's own timing is next-bar-open (no execution-timing argument ships anywhere — quoted verbatim in Provenance); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill. With no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. The two order legs are separate `if` statements, but their conditions contradict on every bar (strict `KST > signal` versus strict `KST < signal` on the current bar), so at most one entry call fires per bar under any evaluation order — no same-bar long/short conflict exists to resolve.
- Sizing/capital/costs: `percent_of_equity 100` language-default sizing is replaced here by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions, never presented as source-native behavior. The source's `commission_value=0.07` percent is recorded above as the source cost assumption for reviewer reference.
- Concurrency: `pyramiding=1` is pinned explicitly — at most one same-direction add (two consecutive same-direction entries maximum); opposite-direction entry reverses. Same-side repeat triggers while positioned are normally impossible without an intervening opposite cross (any return of the aggregate to the far side of its average fires the reversal first), with exactly one fenced exception: an exact-touch dip (`KST` touching `signal` without printing strictly below/above) followed by a bounce can print a second same-direction cross while still positioned, which the pinned `pyramiding=1` fills as an add under fixed order IDs `L`/`S`. Re-entry is otherwise allowed immediately on the next qualifying opposite signal after any reversal (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The mirror ships the full four-leg KST construction (ROC lengths 10/15/20/30, smoothings 10/10/10/15, weights 1/2/3/4, signal SMA 9, close source), the two signal-line cross order legs with their commented-out zero-line filters, the `pyramiding=1` / 100%-equity / 0.07%-commission declaration, and the page-embedded 1h/15m backtest header. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.close`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=` — the opposite-cross reversal is the sole exit path by construction. The absence is coded (the block ends after the two entries), though no source sentence declares it — fenced in Limitations for the reviewer rather than upgraded into a source claim.
2. Entry legs are mutually exclusive on every bar twice over in practice: the conditions require contradictory current-bar states (strictly above versus strictly below the signal average), so no single bar can satisfy both even though they sit in separate `if` statements.
3. Exit-leg conditionality, admitted plainly: a long opened on an upward cross exits only on a later downward cross. Choppy oscillation around the signal average can whipsaw the system; a strong one-direction drift never exits until momentum actually turns — there is no time-stop to cut either behavior. This is the coded trade, disclosed, not a tunable parameter here.
4. Boundary ties fire only on departure: strict edge triggers mean equality holds no signal; an aggregate pinned exactly flat against its average fires neither entry; warmup bars are flat by record rule.
5. Flat-state determinism: with no open position both cross legs are live candidates each bar (edge-triggered, so resting flat between signals is the norm); post-warmup the system is always positioned after its first cross; same-side repeats are governed by the pinned `pyramiding=1` transition above.
6. The ROC lengths (10/15/20/30), the smoothings (10/10/10/15), the weights (1/2/3/4), the signal length (9), the close source, the disabled zero-line filters, the symmetric cross entries, the two-sided reversal posture, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning any length, enabling the zero-line gates, adding a stop/target/cooldown, switching source series, or disabling a side would each be a different, unpinned rule — none is admitted here.
7. Derivation boundary fenced: the only non-source-native behaviors in this record are same-bar-close fills, the adopted 100-bar warmup with record-rule pre-warmup flat, and house sizing — all predeclared above; market, timeframe, every signal, threshold, default, transition, commission declaration, and risk posture are source-verbatim. This record is therefore never evidence that the original next-bar-open 1h/15m source itself passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: ROC 10/15/20/30 / smoothings 10/10/10/15 / weights 1/2/3/4 / signal SMA 9 / symmetric cross entries / reversal-only exits / two-sided / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Aggregation relevance: replacing the four-horizon weighted KST with a single `sma(roc(close,20),10)`-versus-own-average cross system must not improve net expectancy; fail ⇒ the multi-horizon weighting adds nothing over a single-leg momentum cross.
- F2 — Signal-line relevance: replacing the KST-versus-9-bar-average crosses with KST zero-line crosses (long above 0, short below 0) must not improve net expectancy; fail ⇒ the signal average adds nothing over a fixed zero threshold.
- F3 — Reversal-exit relevance: adding a time-stop (flat after N bars without an opposite cross) must not improve net expectancy; fail ⇒ the pure-reversal holding rule is dominated by simply cutting stale positions.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (source-native venue family). The close-only logic ports across perpetual venues without structural change; the short legs require a shortable instrument, so a spot-only deployment cannot express this rule (disabling the short side would be a different, unpinned rule). No funding-dependent leg, no stablecoin-specific assumption, no session, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (`open`/`high`/`low` are never referenced), so session-gap behavior is simply absent rather than approximated. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source fills next-bar-open on a 1h-decision/15m-base Binance-futures backtest; this record executes same-bar-close on `1h` BTCUSDT. Backtest economics of the two timings and bases differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- No price stop and no time stop: adverse excursion after entry has no guardrail beyond the opposite cross, which may arrive late; whipsaw around the signal average can compound consecutive reversal losses. This is the coded posture, disclosed as the record's principal risk.
- Undeclared absence: the source is silent about risk — the no-stop reading rests on the code (the block ends after the entries) rather than on any source sentence. The reviewer should weigh this silence as documented here.
- Namespace transcription note: the file prints `ta.*` cross calls under a `//@version=4` declaration; only the version-invariant edge semantics are pinned, quoted verbatim. If the reviewer reads the prefix as a material defect rather than a transcription quirk, this record should not pass.
- Pyramiding edge: the pinned `pyramiding=1` admits a same-direction add on the exact-touch-then-bounce path fenced in Execution assumptions; evaluations must implement that transition, not assume single-unit positions unconditionally.
- Warmup cost: the adopted 100-bar warmup means the system is blind for the first 100 bars of any 1h evaluation window (structural minimum 53).
- Performance evidence is absent: neither the mirror nor the canonical page reports any number; nothing here is calibrated, fitted, or tuned to the page-embedded 2022-11-28→2023-12-04 window.

## Implementation status

Not implemented. No Hummingbot controller/executor, no Qlib screening, no Paper/Testnet/Live run has been performed from this record. Admission claims pinned-engine expressibility only (see Execution assumptions), subject to independent six-gate review.

## Adoption boundary

Research-only. Not approved for any downstream screening, parity run, or trading authorization. Only a `PASS` under the live six-gate contract may merge this record into `main`; any `NOT_LOSSLESS` finding closes the PR lane without promotion.

## Related Wiki records

None.

## Sources

- Canonical FMZ strategy page (fetched 2026-10-09; title/author/created/arguments/backtest header read; code preview truncated behind login, no order logic taken): https://www.fmz.com/strategy/436493
- Immutable mirror file actually executed against (full Pine v4 block read end to end; 1276 bytes): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/KST%E7%AD%96%E7%95%A5.md
