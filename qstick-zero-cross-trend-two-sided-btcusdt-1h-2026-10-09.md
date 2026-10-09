---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Qstick zero-cross trend two-sided on BTCUSDT 1h bars
created: 2026-10-09
updated: 2026-10-09
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-01-24
sources:
  - https://www.fmz.com/strategy/439854
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E5%8F%8C%E5%90%91%E4%BA%A4%E5%8F%89%E9%9B%B6%E8%BD%B4Qstick%E6%8C%87%E6%A0%87%E5%9B%9E%E6%B5%8B%E7%AD%96%E7%95%A5Bi-directional-Crossing-Zero-Axis-Qstick-Indicator-Backtest-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Qstick zero-cross trend two-sided on BTCUSDT 1h bars

## Provenance

Primary source read end to end (immutable public mirror file plus its recorded FMZ canonical page, fetched 2026-10-09):

- Canonical page: https://www.fmz.com/strategy/439854 (`Bi-directional Crossing Zero Axis Qstick Indicator Backtest Strategy`, publisher account `ChaoZhang`, page title `Bi-directional Crossing Zero Axis Qstick Indicator Backtest Strategy | FMZ`, `Created` = 2024-01-24 14:14:07). Fetched over HTTPS during this cycle (759080 bytes): the page exposes the two strategy arguments (`v_input_1 Length = 14`, `v_input_2 Trade reverse = false`), the full `/*backtest*/` header quoted below, the complete order block (`2 strategy.entry`, `0 strategy.exit`, `0 strategy.close`, quoted verbatim in the page state), and a `Login to view full source` wall after the rendered preview — so the immutable mirror below is the executed code source, with the page serving as title/author/argument/header corroboration. Word-boundary counts over the whole landing HTML: `Net Profit` 0, `Profit Factor` 0, `Sharpe` 0, `Max Drawdown` 0, `win rate` 0 — the page ships no performance numbers of any kind (only site copy/hit tallies, named here as unusable water, never performance).
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit date 2025-04-30 11:10:28 +0800, subject `update`; verified repository head at research time via the GitHub commits API — the same head pin as the merged KST, Schaff, TRIX, SQZMOM-LB and Aroon admissions), exact file path `双向交叉零轴Qstick指标回测策略Bi-directional-Crossing-Zero-Axis-Qstick-Indicator-Backtest-Strategy.md` (non-ASCII filename preserved verbatim; percent-encoded blob URL in Sources). File 9870 bytes, blob SHA `138d7785447d8c4c61affd4856522605bcdfa22e`. The mirror prints `> Detail` = https://www.fmz.com/strategy/439854 and `> Last Modified` = 2024-01-24 14:14:07 (adopted as `source_as_of`). Its two-row `> Strategy Arguments` table (14/false) agrees exactly with the two pinned `input(...)` declarations and the page-embedded argument pair, so there is no table-versus-code-versus-page conflict.
- Full `//@version=2` `strategy(title="Qstick Indicator Backtest")` block read in full. The header comment attributes the indicator to `Copyright by HPotter v1.0 16/04/2018` and names Tushar Chande as the Qstick inventor — original-authorship lineage is preserved here, never claimed by the FMZ publisher. The page-embedded `/*backtest*/` header (`start: 2023-12-01 00:00:00`, `end: 2023-12-31 23:59:59`, `period: 1h`, `basePeriod: 15m`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`) is byte-present on both the canonical page and the mirror block — market (`BTC_USDT` Binance futures) and decision frame (`1h`) are therefore source-native, never researcher-chosen.
- Text census over the pinned code block (1847 characters, `//@version=2` through the final `fill(...)`): 2 `strategy.entry` / 0 `strategy.exit` / 0 `strategy.close` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=`/`qty_percent` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `volume` / 0 `high` / 0 `low`. The only price series read by any order-gating line are `close` and `open` (one code read each, both inside `xR = close - open`); remaining `open`/`close` substrings sit in prose comments only. `pyramiding`, `process_orders_on_close`, `calc_on_every_tick`, `commission`, `default_qty_*`, `margin_*`, and `overlay` are unset throughout.
- No risk layer ships anywhere in the source: zero stop/target/trailing/time-exit lines and no risk prose beyond wishlist items in the mirror's `优化方向` section (adding stops is listed as future optimization, never as shipped behavior). The level-holding reversal-only exit posture below is therefore the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention — but there is no source sentence declaring the absence, which is fenced honestly in Limitations for the reviewer (same posture as the merged KST record).
- Page/mirror performance language is absent entirely (no qualitative praise, no table, figure, or number) — this record claims no source-reported performance and no reproduced performance.

Licence and rights: the canonical page is a public FMZ strategy publication by ChaoZhang carrying an HPotter copyright header. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly three: (1) same-bar-close fills (the source fills next-bar-open — no `process_orders_on_close` ships anywhere, quoted verbatim in census); (2) an adopted 100-bar warmup with pre-warmup bars flat by record rule (structural minimum is 14 bars — see Required data); (3) house sizing/capital replacing the language-default sizing (no `default_qty_*` ships anywhere — see Execution assumptions). Market (BTCUSDT Binance futures) and decision frame (`1h`) are source-native per the page-embedded backtest header, not adaptations. All three adaptations are predeclared here, confined to Provenance, Signal, Required data, Execution assumptions, and Limitations, with every original claim kept separate above. Indicator formula, lookback, zero threshold, state recursion, order IDs, direction handling, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-09): working-tree word-boundary searches for `qstick`, `439854`, `chande`, and `tushar` return zero strategy records using this source, author strategy, or mechanism — the only contiguous `coppock`-family hit anywhere is inside the merged TRIX record's own dedup paragraph (a search term, never a mechanism), and no pool file mentions Qstick at all. Same-publisher ChaoZhang records exist (KST FMZ 436493, Aroon FMZ 438795, TRIX FMZ 428683, Schaff FMZ 365905) but carry different canonical identities, different indicator families, and different order sets. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #58 (17-file reconstruction batch — file list verified, no Qstick/indicator-cross record), and #63 (SuperTrend ATR-flip trend long) — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `vidya-cmo-adaptive-slope-trend-btcusdt-1h` is an adaptive-average slope system, `rsi-classic-level-reversal-btcusdt-1h` is a single-oscillator level system, `p-signal-erf-dead-band-reversal-btcusdt-1h` is an error-function dead-band system. Five-axis distinction: mechanism differs (SMA of close-minus-open body pressure against a fixed zero line, two-sided level-holding with reversal), signal construction differs (no pool record evaluates `sma(close - open, 14)` against zero with recursive state hold), exits differ (opposite-level reversal only, no band/trailing/tick exits), source identity differs (FMZ 439854 Jan-2024 ChaoZhang/HPotter versus other FMZ IDs or TV authors), and direction handling differs (symmetric two-sided level holding: long whenever above zero, short whenever below — versus edge-triggered crosses, gated, or long-only records).

## Economic mechanism

### Source-reported

Trend tracking and signal generation on candlestick body pressure (mirror `策略原理`, corroborated by the page meta description): the Qstick averages the open-to-close difference over a fixed window; a positive value means closes have dominated opens over the window (buying pressure), a negative value means opens have dominated closes (selling pressure). Crossing up through zero reads as buying pressure overtaking selling pressure (long); crossing down reads as selling pressure taking over (short). The mirror's prose additionally mentions an optional Qstick signal-line cross and a reverse-trade mode — both are documented in prose only: no signal-line average ships anywhere in the code, and the reverse toggle is pinned `false` (see Signal).

### Research interpretation

Two-sided body-momentum regime holding on a smoothed open-close spread. Unlike edge-triggered cross systems (KST/Schaff records) that fire once per crossing, this is a level-holding system: every completed bar re-asserts the side dictated by the sign of the average body, so the system is always positioned after warmup (long or short), never resting flat except on exact-zero holds. The 14-bar SMA filters single-bar noise at the cost that adverse excursion has no guardrail except the sign flip, which may arrive late (see Limitations). This record must be read as a pure always-in-the-market reversal system, never as a risk-managed one.

## Signal

Exact rule as pinned (defaults quoted — effective inputs unmodified):

- Declaration (derived): `strategy(title="Qstick Indicator Backtest")` with same-bar-close execution adopted for the derived record (no such argument ships in the source) and house sizing replacing the unset language-default sizing (see Execution assumptions). `calc_on_every_tick` is unset (default false: exactly one evaluation per completed bar). No commission, margin, or overlay assumption ships anywhere — pinned as absent, with house costs applying to the derived evaluation (see Execution assumptions).
- Inputs (pinned, table- and page-agreeing): `Length=14` (`input(14, minval=1)`), `reverse=false` (`input(false, title="Trade reverse")`). Retuning either of them would be a different, unpinned rule.
- Indicator (pinned): `xR = close - open`; `xQstick = sma(xR, 14)`.
- State recursion (pinned): `pos = +1` when `xQstick > 0`, `-1` when `xQstick < 0`, otherwise hold `nz(pos[1], 0)` — exact-zero bars inherit the prior bar's state, and the very first bar resolves to `0` (flat, no order). `possig = pos` under the pinned `reverse=false`; the `reverse=true` inversion path is disclosed-as-disabled code, never the admitted rule — enabling it would be a different, unpinned rule.
- Entry long: `if (possig == 1) strategy.entry("Long", strategy.long)` — level-holding, re-asserted on every completed `1h` bar while the average body stays positive, with same-bar-close execution under the derived declaration.
- Entry short: `if (possig == -1) strategy.entry("Short", strategy.short)` — mirror terms. The two `if` statements are separate but their conditions are mutually exclusive on every bar (`possig` cannot equal both), so at most one entry call fires per bar under any evaluation order — no same-bar long/short conflict exists to resolve.
- Exits: none coded. The sole exit path is opposite-level reversal (a short level while long reverses to short and vice versa). No stop, no target, no trailing, no time exit — pinned as written, explicitly none, not invented.
- Direction: symmetric two-sided by pinned levels; flat is entered only via the exact-zero state hold (and the first-bar zero). A short-side instrument is required for the short legs; on a spot-only venue they are inexpressible and the record would not be the same rule (see Crypto portability).
- Display isolation: `clr`, `barcolor(...)`, the two `plot(...)` calls, and `fill(...)` feed no order condition; order logic reads exactly the two level conditions. The prose-only signal-line average is absent from code and is not part of this rule.

## Required data

- Completed `1h` bars of BTCUSDT: `close` and `open` only (via the single `xR = close - open` line). No `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1h` (source-native per the page-embedded `period: 1h` header). The script takes no timeframe input and makes no live `request.*` call, so it is single-frame by construction. The header's `basePeriod: 15m` is the FMZ execution granularity of the source backtest, not a signal input — the derived record evaluates completed `1h` bars only and claims no 15m behavior.
- Warmup: `sma(xR, 14)` needs 14 completed `1h` bars for its first full window; the `pos[1]` recursion is defined from the first bar via `nz` (resolving flat). Structural minimum is therefore the 14th completed `1h` bar; the adopted warmup is the first 100 completed `1h` bars flat by record rule (predeclared researcher choice). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (source-native per the header's `Futures_Binance BTC_USDT`; venue transfer from `BTC_USDT` to `BTCUSDT` spot-symbol spelling is naming only, never presented as a market change).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. The source's own timing is next-bar-open (no execution-timing argument ships anywhere — quoted verbatim in Provenance); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill. With no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. The two order legs are mutually exclusive every bar (see Signal), so no ordering resolution is required.
- Sizing/capital/costs: no `default_qty_*`, commission, or margin assumption ships anywhere (quoted verbatim in census) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions replace the unset language defaults here, never presented as source-native behavior.
- Concurrency: no `pyramiding` ships anywhere, pinning the language default of no same-direction adds — at most one unit per side under fixed order IDs `Long`/`Short`; repeat same-level entries while positioned are no-ops and the opposite-level entry reverses (closes the current side and opens the opposite in one transition). Re-entry is allowed immediately on the next qualifying opposite level after any reversal (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The mirror ships the full Qstick construction (`close - open`, SMA 14, fixed zero line, recursive state hold), the two level-holding order legs with their order IDs, the `Length=14` / `Trade reverse=false` inputs, the HPotter/Chande authorship header, and the page-embedded 1h/15m December-2023 backtest header. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.close`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=`/`qty_percent` — the opposite-level reversal is the sole exit path by construction. The absence is coded (the block ends with display calls after the two entries), though no source sentence declares it — fenced in Limitations for the reviewer rather than upgraded into a source claim.
2. Entry legs are mutually exclusive on every bar by value (`possig` is a single integer that cannot equal 1 and -1 at once), so no single bar can satisfy both even though they sit in separate `if` statements.
3. Exit-leg conditionality, admitted plainly: a long opened on a positive level exits only on a later negative level. Choppy oscillation around zero can whipsaw the system; a strong one-direction drift never exits until the average body actually turns non-positive — there is no time-stop to cut either behavior. This is the coded trade, disclosed, not a tunable parameter here.
4. Boundary ties hold, never fire: exact-zero bars inherit prior state via `nz(pos[1], 0)`; an average body pinned exactly at zero holds the existing side (or stays flat before the first signal); warmup bars are flat by record rule.
5. Flat-state determinism: with no open position both level legs are live candidates each bar (level-holding, so the first post-warmup non-zero level always opens a position); post-warmup the system is always positioned after its first signal; same-side repeats are no-ops under the pinned no-add default.
6. The body spread (`close - open`), the length (14), the zero line, the recursive hold, the `reverse=false` stance, the fixed order IDs, the symmetric levels, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning the length, enabling reverse, adding a stop/target/cooldown, switching source series, inserting the prose-only signal line, or disabling a side would each be a different, unpinned rule — none is admitted here.
7. Derivation boundary fenced: the only non-source-native behaviors in this record are same-bar-close fills, the adopted 100-bar warmup with record-rule pre-warmup flat, and house sizing — all predeclared above; market, timeframe, every signal, threshold, default, transition, and risk posture are source-verbatim. This record is therefore never evidence that the original next-bar-open 1h/15m source itself passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `sma(close - open, 14)` / zero line / recursive hold / `reverse=false` / symmetric level entries / reversal-only exits / two-sided / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Spread relevance: replacing the open-close body spread with a close-to-close momentum spread (`sma(change(close), 14)` against zero) must not improve net expectancy; fail ⇒ the body-pressure construction adds nothing over plain close momentum.
- F2 — Threshold relevance: replacing the fixed zero line with the signal's own 9-bar SMA cross (long above, short below its average) must not improve net expectancy; fail ⇒ the zero line adds nothing over a self-relative trigger.
- F3 — Holding relevance: adding a time-stop (flat after N bars without an opposite level) must not improve net expectancy; fail ⇒ the pure always-in-market holding rule is dominated by simply cutting stale positions.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (source-native venue family). The open/close-only logic ports across perpetual venues without structural change; the short legs require a shortable instrument, so a spot-only deployment cannot express this rule (disabling the short side would be a different, unpinned rule). No funding-dependent leg, no stablecoin-specific assumption, no session, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read beyond the per-bar `open`/`close` pair already pinned, so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source fills next-bar-open on a 1h-decision/15m-base Binance-futures backtest; this record executes same-bar-close on `1h` BTCUSDT. Backtest economics of the two timings and bases differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- No price stop and no time stop: adverse excursion after entry has no guardrail beyond the opposite level, which may arrive late; whipsaw around zero can compound consecutive reversal losses. This is the coded posture, disclosed as the record's principal risk.
- No source cost declaration: no commission, fee, slippage, or funding assumption ships anywhere in the source — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Undeclared absence: the source is silent about risk — the no-stop reading rests on the code (the block ends with display calls after the entries) rather than on any source sentence. The reviewer should weigh this silence as documented here.
- Warmup cost: the adopted 100-bar warmup means the system is blind for the first 100 bars of any 1h evaluation window (structural minimum 14).
- Performance evidence is absent: neither the mirror nor the canonical page reports any number; nothing here is calibrated, fitted, or tuned to the page-embedded 2023-12-01→2023-12-31 window.

## Implementation status

Not implemented. No Hummingbot controller/executor, no Qlib screening, no Paper/Testnet/Live run has been performed from this record. Admission claims pinned-engine expressibility only (see Execution assumptions), subject to independent six-gate review.

## Adoption boundary

Research-only. Not approved for any downstream screening, parity run, or trading authorization. Only a `PASS` under the live six-gate contract may merge this record into `main`; any `NOT_LOSSLESS` finding closes the PR lane without promotion.

## Related Wiki records

None.

## Sources

- Canonical FMZ strategy page (fetched 2026-10-09; title/publisher/created/arguments/backtest header read; code corroborated in page state; no order logic invented): https://www.fmz.com/strategy/439854
- Immutable mirror file actually executed against (full Pine v2 block read end to end; 9870 bytes): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E5%8F%8C%E5%90%91%E4%BA%A4%E5%8F%89%E9%9B%B6%E8%BD%B4Qstick%E6%8C%87%E6%A0%87%E5%9B%9E%E6%B5%8B%E7%AD%96%E7%95%A5Bi-directional-Crossing-Zero-Axis-Qstick-Indicator-Backtest-Strategy.md
