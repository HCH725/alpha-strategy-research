---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: DPO-EMA crossover trend long on BTCUSDT 1d bars
created: 2026-10-09
updated: 2026-10-09
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-12-05
sources:
  - https://www.fmz.com/strategy/474030
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/DPO-EMA%E8%B6%8B%E5%8A%BF%E4%BA%A4%E5%8F%89%E9%87%8F%E5%8C%96%E7%AD%96%E7%95%A5%E7%A0%94%E7%A9%B6-DPO-EMA-Trend-Crossover-Quantitative-Strategy-Research.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# DPO-EMA crossover trend long on BTCUSDT 1d bars

## Provenance

Primary source read end to end (immutable public mirror file plus its recorded FMZ canonical page, fetched 2026-10-09):

- Canonical page: https://www.fmz.com/strategy/474030 (page title `DPO-EMA Trend Crossover Quantitative Strategy Research | FMZ`, publisher account `ChaoZhang`, `Created: 2024-12-05 14:57:18`, equal to the mirror `Last Modified`). Fetched over HTTPS during this cycle (644804 bytes): the page embeds the full `/*backtest ... */` header quoted below, the active `strategy("DPO 4,24 Strategy", shorttitle="DPO Strategy", overlay=true)` declaration, and the complete order block (`1 strategy.entry` / `1 strategy.close` / `0 strategy.exit` / `0 strategy.order` in page state, counted verbatim). Word-boundary counts over the whole landing HTML: `Net Profit` 0, `Profit Factor` 0, `Sharpe` 0, `Max Drawdown` 0, `Win Rate` 0, `win rate` 0, `Annualized` 0 — the page ships no performance numbers of any kind (adopted as `source_as_of` 2024-12-05 from the page Created stamp, which equals the mirror `Last Modified`).
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit date 2025-04-30 11:10:28 +0800, subject `update`; verified repository head at research time via the GitHub commits API — the same head pin as the merged KST, Schaff, TRIX, SQZMOM-LB, Aroon, Qstick, AC and Elder-ray admissions), exact file path `DPO-EMA趋势交叉量化策略研究-DPO-EMA-Trend-Crossover-Quantitative-Strategy-Research.md` (non-ASCII filename preserved verbatim; percent-encoded blob URL in Sources). File 6945 bytes, blob SHA `0d74502fa552e4f7d239b0686881c0fb16e98a42` (verified against the GitHub contents API at the pinned commit — size and SHA both match). The mirror prints `> Detail` = https://www.fmz.com/strategy/474030 and `> Last Modified` = 2024-12-05 14:57:18 (equal to the page Created stamp). The mirror carries no `Strategy Arguments` table — the script declares zero `input(...)` calls (every parameter is hardcoded: `length = 24`, `ema_length = 4`), so there is nothing to cross-check and nothing to retune.
- Full `//@version=5` block read in full (44 code lines, `/*backtest` through the final `strategy.close("Buy")`). The page-embedded `/*backtest*/` header (`start: 2019-12-23 08:00:00`, `end: 2024-12-04 00:00:00` in preview rendering, `period: 1d`, `basePeriod: 1d`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`) is byte-present on both the canonical page preview (2 hits each for `period: 1d`, `basePeriod: 1d`, `BTC_USDT`, `start: 2019-12-23 08:00:00`) and the mirror block — market (`BTC_USDT` Binance futures) and decision frame (`1d`) are therefore source-native, never researcher-chosen.
- Text census over the pinned code block: 1 `strategy.entry` (`strategy.entry("Buy", strategy.long)`) / 1 `strategy.close` (`strategy.close("Buy")`, no `when=`, unconditional on its bar) / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=`/`qty_percent` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `time(` / 0 `volume` / 0 `open`/`high`/`low`/`hl2`. The single `volume` word-boundary hit in the mirror file sits in the prose optimization list (`添加成交量确认` — a not-implemented suggestion), never in code. `pyramiding`, `process_orders_on_close`, `calc_on_every_tick`, `commission`, and `default_qty_*` are unset throughout. Price reads are `close` only (SMA of close, DPO subtraction, EMA of DPO, crossover pair).
- No risk layer ships anywhere in the source: zero stop/target/trailing/time-exit order legs, and the mirror's own risk section names stop-loss only as future optimization (`优化止损设置`), confirming none ships. The cross-down close posture below is therefore the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention.
- Page/mirror performance language is absent entirely (no table, figure, or number; the prose adjectives `效果显著`/`明显` carry no quantity) — this record claims no source-reported performance and no reproduced performance.
- Prose-versus-code gaps are pinned to the code, never repaired: (a) the prose recommends 4h-and-above frames and Heikin Ashi candles (`在使用平滑蜡烛图(Heikin Ashi)时效果更佳`), but the executed header is `1d` on standard exchange bars and the code reads raw `close`; (b) the prose advertises buy *and* sell signals (`产生买入和卖出信号`), but the code is long-only — the cross-down leg closes the long and never opens a short. This record pins the computation in both cases; anyone citing the prose alone would describe a different rule. Both gaps are fenced in Limitations.

Licence and rights: the canonical page is a public FMZ strategy publication by ChaoZhang. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly three: (1) same-bar-close fills (the source fills next-bar-open — no `process_orders_on_close` ships anywhere, quoted verbatim in census); (2) an adopted 100-bar warmup with pre-warmup bars flat by record rule (structural minimum is 38 bars — see Required data); (3) house sizing/capital replacing the language-default sizing (no `default_qty_*` ships anywhere — see Execution assumptions). Market (BTCUSDT Binance futures) and decision frame (`1d`) are source-native per the page-embedded backtest header, not adaptations. All three adaptations are predeclared here, confined to Provenance, Signal, Required data, Execution assumptions, and Limitations, with every original claim kept separate above. Indicator formulas, lookbacks, displacement, comparisons, order IDs, direction handling, the unconditional close leg, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-09): working-tree word-boundary searches for `dpo`, `474030`, `detrended`, and `DPO-EMA` return zero strategy records using this source, author strategy, or mechanism. Same-publisher ChaoZhang records exist (KST FMZ 436493, Schaff FMZ 365905, TRIX FMZ 428683, Aroon FMZ 438795, Qstick FMZ 439854, AC FMZ 435716, Elder-ray FMZ 432762, QQE-signals FMZ 365028) but carry different canonical identities, different indicator families, and different order sets. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #58 (ML/reconstruction batch — file list verified, no oscillator-cross record), and #63 (SuperTrend ATR-flip trend long) — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `golden-cross-sma-regime-gated-long-btcusdt-1h` crosses two raw price SMAs (no detrending, no oscillator, regime-gated); `rsi-ma-crossover-reversal-btcusdt-1d` crosses Wilder RSI27 against its own SMA10 (bounded momentum oscillator, no displaced baseline); `alma-cross-volume-gate-btcusdt-1d` crosses two ALMA price averages with a volume gate (no oscillator at all). Five-axis distinction: mechanism differs (detrended-oscillator-against-own-signal-line cross — price minus 13-bar-displaced SMA24, then crossed with its own EMA4), signal construction differs (no pool record uses a backward-displaced baseline subtraction), exits differ (unconditional cross-down `strategy.close("Buy")` flat leg, no trailing/band exits), source identity differs (FMZ 474030 Dec-2024 versus other FMZ IDs or TV authors), and direction handling differs (pure long-only with an explicit flat state versus two-sided or always-in-market holders).

## Economic mechanism

### Source-reported

Detrended trend capture (mirror `策略原理`, corroborated by the code): subtracting the 13-bar-displaced 24-bar average removes the slow drift so the residual (DPO) exposes where the current close stands against its own settled consensus; the fast 4-bar EMA of that residual acts as the trigger line. A cross-up means price has reclaimed its detrended consensus with momentum to spare — the long entry. A cross-down means the reclaim failed — the position is closed flat, never flipped short.

### Research interpretation

Single-oscillator cross system with an explicit flat state, long-only. Unlike always-in-market holders (Qstick, AC records) that must be long or short after warmup, this system rests flat whenever DPO sits below its signal line — the flat state is a first-class coded outcome (the close leg plus the no-short posture), not the absence of a signal. Unlike bounded oscillators (RSI/Williams-%R records) that fire on fixed 0–100 levels, the trigger here is self-referential: the signal line is carved from the same residual it judges, so the system adapts its own threshold to recent residual volatility without any volatility input. The displacement is strictly backward (13 completed bars), so no future information enters at any point — the detrending costs 13 bars of staleness, honestly priced in warmup (see Required data).

## Signal

Exact rule as pinned (hardcoded constants — no inputs exist to retune):

- Declaration (derived): `strategy("DPO 4,24 Strategy", shorttitle="DPO Strategy", overlay=true)` with same-bar-close execution adopted for the derived record (no such argument ships in the source) and house sizing replacing the unset language-default sizing (see Execution assumptions). `calc_on_every_tick` is unset (default false: exactly one evaluation per completed bar). No commission or margin assumption ships anywhere — pinned as absent, with house costs applying to the derived evaluation (see Execution assumptions).
- Constants (pinned, zero inputs): `length = 24`, `ema_length = 4`. Displacement `length / 2 + 1` evaluates to 13 under the pinned integers (int arithmetic on the declared constants). Changing any of them would be a different, unpinned rule.
- Baseline (pinned): `sma = ta.sma(close, 24)`; `shifted_sma = sma[13]` — the 24-bar average as it stood 13 completed bars ago (backward displacement only, causal by construction).
- Oscillator (pinned): `dpo = close - shifted_sma`; `dpo_ema = ta.ema(dpo, 4)`.
- Buy signal (pinned): `buy_signal = ta.crossover(dpo, dpo_ema)` — strict cross-up on the completed bar (equal values do not fire; ties hold prior state).
- Sell signal (pinned): `sell_signal = ta.crossunder(dpo, dpo_ema)` — strict cross-down on the completed bar.
- Entry long: `if (buy_signal) strategy.entry("Buy", strategy.long)` — fires only on the cross-up bar, with same-bar-close execution under the derived declaration.
- Exit: `if (sell_signal) strategy.close("Buy")` — unconditional close of the long on the cross-down bar (no `when=`, no quantity qualifier: the whole position), with same-bar-close execution under the derived declaration. No stop, no target, no trailing, no time exit — pinned as written, explicitly none, not invented.
- Direction: long-only with an explicit flat state. The cross-down leg never opens a short; on a spot venue the rule expresses unchanged (see Crypto portability).
- Display isolation: the two `plotshape` calls feed no order condition; order logic reads exactly the two cross booleans.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (SMA baseline, DPO subtraction, DPO-EMA line, crossover pair). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line. The prose volume suggestion is not code and is pinned as absent.
- Single decision timeframe `1d` (source-native per the page-embedded `period: 1d` / `basePeriod: 1d` header). The script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction. The prose 4h recommendation contradicts the executed header and is fenced in Limitations — this record evaluates completed `1d` bars only.
- Warmup: `ta.sma(close, 24)` is first fully windowed on the 24th completed `1d` bar; `sma[13]` needs 13 further bars — first defined DPO on the 37th completed bar; `ta.ema(dpo, 4)` seeds from the 37th; `crossover`/`crossunder` need two consecutive defined pairs — first evaluable signal on the 38th completed bar. Structural minimum is therefore the 38th completed `1d` bar; the adopted warmup is the first 100 completed `1d` bars flat by record rule (predeclared researcher choice). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (source-native per the header's `Futures_Binance BTC_USDT`; venue transfer from `BTC_USDT` to `BTCUSDT` spot-symbol spelling is naming only, never presented as a market change).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar-open (no execution-timing argument ships anywhere — quoted verbatim in Provenance); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill. With no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. The two signal booleans are mutually exclusive every bar (a strict cross-up and a strict cross-down cannot co-occur), so no ordering resolution is required.
- Sizing/capital/costs: no `default_qty_*`, commission, or margin assumption ships anywhere (quoted verbatim in census) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) replace the unset language defaults here, never presented as source-native behavior.
- Concurrency: no `pyramiding` ships anywhere, pinning the language default of no same-direction adds — at most one long unit under the fixed order ID `Buy`; repeat cross-up bars while positioned are no-ops, the cross-down close exits in full, and re-entry is allowed immediately on the next cross-up after any flat (no cooldown specified — explicitly none, not invented). Single engine position; no short side exists to conflict; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The mirror ships the full construction (SMA24, 13-bar backward displacement, DPO subtraction, EMA4 signal line, strict cross pair, fixed `Buy` order ID, unconditional close leg), the active `strategy(...)` declaration, the `DPO 4,24` title, and the page-embedded 1d/1d December-2019→December-2024 backtest header. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=`/`qty_percent` — the sole position-closing path is the coded cross-down `strategy.close("Buy")` leg. The absence is coded (the block ends with the close leg and no order call follows), and the mirror's risk prose proposes stops as future work, corroborating that none ships — fenced in Limitations for the reviewer rather than upgraded into a source claim.
2. Entry and exit legs are mutually exclusive on every bar by value (`crossover` and `crossunder` of the same pair cannot both be true on one bar), so no single bar can satisfy more than one order leg even though they sit in separate `if` statements.
3. Exit-leg conditionality, admitted plainly: a long opened on a cross-up exits only on the next cross-down. A market that keeps DPO above its signal line never exits until they recross — there is no time-stop to cut a stale trend, and choppy oscillation around the signal line can whipsaw the system in and out of flat with consecutive small losses. This is the coded trade, disclosed, not a tunable parameter here.
4. Long-only flat stretches earn nothing: while DPO sits below its signal line the system holds no position by code, not by choice of venue — disabling nothing, since no short leg exists to disable.
5. Boundary ties hold, never fire: exact equality of DPO and its EMA satisfies neither `crossover` nor `crossunder` (strict inequalities); warmup bars are flat by record rule.
6. The SMA length (24), displacement (13), EMA length (4), strict-cross definitions, fixed order ID, long-only posture, unconditional close leg, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning a length, adding a stop/target/cooldown, switching source series, replacing the displaced baseline with a plain SMA, enabling a short side, or moving to Heikin Ashi candles would each be a different, unpinned rule — none is admitted here.
7. Derivation boundary fenced: the only non-source-native behaviors in this record are same-bar-close fills, the adopted 100-bar warmup with record-rule pre-warmup flat, and house sizing — all predeclared above; market, timeframe, every signal, constant, transition, close leg, and risk posture are source-verbatim. This record is therefore never evidence that the original next-bar-open 1d/1d source itself passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: SMA24 / 13-bar backward displacement / EMA4 / strict-cross pair / unconditional cross-down close / long-only / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Detrending relevance: replacing DPO with the raw close-versus-SMA24 cross (`close` crossed with its own `ta.sma(close, 24)`, same EMA-free footing) must not improve net expectancy; fail ⇒ the backward-displaced detrending adds nothing over a plain price-average cross.
- F2 — Signal-line relevance: replacing the EMA4-of-DPO trigger with a fixed zero level (long while `dpo > 0`, flat otherwise) must not improve net expectancy; fail ⇒ the self-referential signal line adds nothing over a static detrended-level rule.
- F3 — Exit relevance: removing the cross-down close leg (holding the long through cross-downs — buy-and-hold from the first cross-up, since no opposite signal exists) must not improve net expectancy; fail ⇒ the explicit flat state is dominated by simply staying positioned.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (source-native venue family). The close-only arithmetic ports across perpetual venues without structural change; the rule is long-only with no short leg, so a spot-only deployment expresses it unchanged. No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read, so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source fills next-bar-open on a 1d-decision/1d-base Binance-futures backtest; this record executes same-bar-close on `1d` BTCUSDT. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- Prose-versus-code gaps (pinned to code): the prose recommends 4h-and-above frames and Heikin Ashi candles, contradicting the executed `1d` header on standard bars; the prose advertises buy *and* sell signals, contradicting the coded long-only posture. The record pins the computation; anyone citing the prose label alone would describe a different rule.
- No price stop and no time stop: adverse excursion after entry has no guardrail beyond the cross-down close, which may arrive late; oscillation around the signal line can compound consecutive whipsaw losses. This is the coded posture, disclosed as the record's principal risk.
- No source cost declaration: no commission, fee, slippage, or funding assumption ships anywhere in the source — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Warmup cost: the adopted 100-bar warmup means the system is blind for the first 100 bars of any 1d evaluation window (structural minimum 38).
- Performance evidence is absent: neither the mirror nor the canonical page reports any number; nothing here is calibrated, fitted, or tuned to the page-embedded 2019-12-23→2024-12-04 window.

## Implementation status

Not implemented. No Hummingbot controller/executor, no Qlib screening, no Paper/Testnet/Live run has been performed from this record. Admission claims pinned-engine expressibility only (see Execution assumptions), subject to independent six-gate review.

## Adoption boundary

Research-only. Not approved for any downstream screening, parity run, or trading authorization. Only a `PASS` under the live six-gate contract may merge this record into `main`; any `NOT_LOSSLESS` finding closes the PR lane without promotion.

## Related Wiki records

None.

## Sources

- Canonical FMZ strategy page (fetched 2026-10-09; title/publisher/created/backtest header read; code corroborated in page state; no order logic invented): https://www.fmz.com/strategy/474030
- Immutable mirror file actually executed against (full Pine v5 block read end to end; 6945 bytes): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/DPO-EMA%E8%B6%8B%E5%8A%BF%E4%BA%A4%E5%8F%89%E9%87%8F%E5%8C%96%E7%AD%96%E7%95%A5%E7%A0%94%E7%A9%B6-DPO-EMA-Trend-Crossover-Quantitative-Strategy-Research.md
