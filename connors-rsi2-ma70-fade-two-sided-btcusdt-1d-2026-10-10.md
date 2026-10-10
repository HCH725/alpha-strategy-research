---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Connors RSI2 MA70-gated two-sided extreme fade on BTCUSDT 1d bars
created: 2026-10-10
updated: 2026-10-10
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2020-05-14
sources:
  - https://www.fmz.com/strategy/207157
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/Larry-Connors-RSI2%E5%9D%87%E5%80%BC%E5%9B%9E%E5%BD%92%E7%AD%96%E7%95%A5.md
  - https://school.stockcharts.com/doku.php?id=trading_strategies:rsi2
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Connors RSI2 MA70-gated two-sided extreme fade on BTCUSDT 1d bars

## Provenance

Primary source read end to end (canonical FMZ page fetched over HTTPS during this cycle plus the immutable GitHub mirror at the pinned commit):

- Canonical page: https://www.fmz.com/strategy/207157 (page title `Larry Connors RSI2均值回归策略 | FMZ`, publisher account `homily`, `Last Modified` 2020-05-14 — adopted as `source_as_of`). Fetched during this cycle (703006 bytes): the page embeds the complete MyLanguage source quoted below, the `/*backtest ... */` header (`start: 2018-01-01 00:00:00`, `end: 2020-05-12 00:00:00`, `period: 15m`, `basePeriod: 15m`, `exchanges: [{"eid":"Futures_OKCoin","currency":"BTC_USD"}]`, `ContractType quarterly`, each marker byte-present twice on the page), the single strategy-argument row (`Y` default `70`), and the two lineage comments (`https://school.stockcharts.com/doku.php?id=trading_strategies:rsi2` and the pyalgotrade RSI2 sample URL). Word-boundary counts over the whole landing HTML: `Net Profit` 0, `Profit Factor` 0, `Sharpe` 0, `Max Drawdown` 0, `Win Rate` 0, `Annualized` 0, `Total Profit` 0 — the page ships no performance numbers of any kind.
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit date 2025-04-30, verified repository head at research time via the GitHub commits API — the same head pin as the merged Double-Seven, DPO-EMA, KST, Schaff, TRIX, SQZMOM-LB, Aroon, Qstick, AC, Elder-ray and ActionZone admissions), exact file path `Larry-Connors-RSI2均值回归策略.md` (non-ASCII filename preserved verbatim; percent-encoded blob URL in Sources). File 958 bytes, blob SHA `33132661560e29932bfd5075280507b4444331a1` (verified against the GitHub contents API at the pinned commit — size and SHA both match). The mirror prints `> Detail` = https://www.fmz.com/strategy/207157, `> Author` = homily, and `> Last Modified` = 2020-05-14 09:50:47 (equal to the page stamp).
- Text census over the pinned code block: 1 `BK` (buy-open long) / 1 `SK` (sell-open short) / 1 `SP` (sell-close long) / 1 `BP` (buy-close short) / 1 `AUTOFILTER` / 0 stop/limit/target/trailing legs of any kind / 0 volume reads / 0 `open`/`high`/`low` reads (the rule reads `CLOSE` only) / exactly 1 strategy argument (`Y` default 70). The sizing line `liang:=INTPART(1*MONEYTOT*REF(C,1)/100)` is language-broker contract sizing with no HB equivalent, replaced by the house overlay (see derived declaration). `SKVOL`/`BKVOL` close the full contra-side position by language semantics.
- No risk layer ships anywhere in the source: zero stop/target/trailing/time-exit legs, and exits are the opposite RSI2-extreme signal legs only. The signal-only-exit posture below is therefore the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention.
- Page/mirror performance language is absent entirely (no table, figure, or number) — this record claims no source-reported performance and no reproduced performance.

Licence and rights: the canonical page is a public FMZ strategy publication by homily; the code block cites the StockCharts RSI2 school page and a pyalgotrade sample as its indicator lineage. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) research market/timeframe BTCUSDT `1d` (the script's arithmetic reads `CLOSE` only and is symbol-agnostic; the FMZ block's `15m`/`15m` Futures-OKCoin-quarterly context is FMZ-platform execution, not HB-modelable source timing — same port rationale as the admitted ALMA record, whose source block was `4h`/`15m`); (2) same-bar-close fills on completed-bar decisions (the MyLanguage backtest fills market legs on the next tick/open — this record does not claim source timing); (3) an adopted 70-bar warmup with pre-warmup bars flat by record rule (the MA70 leg needs 70 completed bars — see Required data); (4) house sizing/capital replacing the `liang`/`MONEYTOT` broker sizing (no `default_qty_*`-style portable sizing ships — see Execution assumptions; the `AUTOFILTER` single-unit no-add behavior is preserved as the no-pyramiding rule). Formula, MA length, RSI2 construction, 90/10 thresholds, strict inequalities, side gating, all four order legs, the full-position close semantics, two-sided direction, and the no-stop/no-target posture are source-native and unmodified.

Pre-write dedup (2026-10-10): working-tree case-insensitive searches for `207157`, `homily`, `Larry-Connors-RSI2`, `rsi2均值`, `AUTOFILTER`, and `SKVOL` return zero admitted rules using this source, author strategy, or mechanism — the only loose `connors` hits pool-wide are lineage/mechanism-different records (`double-seven-connors-pullback-long-btcusdt-1d-2026-10-09.md`, a 7-day lowest-close touch under an SMA200 gate with a channel-high exit; `etf-3day-reversion-ema5-mean-reversion-long-btcusdt-1d-2026-10-08.md`, a 3-day lower-highs/lows chain under an EMA5 gate). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Five-axis distinction: mechanism differs (Wilder-style 2-period RSI extreme fade with the trade side gated by a 70-bar average — no pool record computes any 2-period RSI or fades 90/10 tails), signal construction differs (`SMA(MAX(CLOSE-LC,0),2,1)/SMA(ABS(CLOSE-LC),2,1)*100` crossed against fixed 90/10 levels, versus channel touches, count chains, or slower-oscillator crosses), exits differ (opposite-tail signal legs plus full-position closes, no stop/trailing/time variant matches), source identity differs (FMZ 207157 homily May-2020 versus FMZ 473246 ChaoZhang or other authors), and direction handling differs (symmetric two-sided fade with an explicit flat state versus long-only or always-in-market holders).

## Economic mechanism

### Source-reported

Short-horizon tail fade inside a side regime (mirror title `Larry-Connors-RSI2均值回归策略`, corroborated line-for-line by the code and its StockCharts-RSI2 lineage comment): the 70-bar average decides which side may trade, and only a 2-period RSI print at an extreme tail may fire — overbought tails are faded with shorts above the average, oversold tails are faded with longs below it, and the opposite tail ends the trade. The design bets that 2-bar panic prints snap back before the regime leg reprices.

### Research interpretation

Regime-gated symmetric contrarian with an explicit flat state, two-sided. Unlike the pool's Double-Seven record (same Connors lineage, different mechanism) that buys the 7-day lowest *close* under an SMA200 gate, this system never reads a channel extreme — it reads a normalized 2-bar velocity ratio against fixed 90/10 tails, so a slow bleed that never prints a 2-day panic fires nothing here while still triggering channel-touch systems. Unlike recovery-cross systems it buys weakness as it prints (the entry bar's own close is already RSI2<10), never a confirmed bounce. Unlike always-in-market reversal holders, the system rests flat whenever the last signal was an opposite-tail exit, and each side only exists on its own side of the average: overbought prints above MA70 while flat open shorts (never longs), oversold prints below MA70 while flat open longs (never shorts), and mid-range RSI2 prints are no-ops on both sides. The bet is on 2-bar over-extension snapping back at the ~days scale under a 70-bar side gate, not on any channel, count chain, band, calendar effect, or volatility envelope.

## Signal

Exact rule as pinned (Y=70, RSI length 2, tails 90/10, strict inequalities — any other value is a different, unpinned rule):

- Lines (pinned): `LC := REF(CLOSE,1)`; `RSI2 = SMA(MAX(CLOSE-LC,0),2,1)/SMA(ABS(CLOSE-LC),2,1)*100` (Wilder-style 2-period RSI on closes; a zero 2-bar loss sum pins RSI2 at 100, a zero gain sum pins it at 0 — deterministic, no divide-by-zero branch needed beyond the formula); `ma1 := MA(CLOSE,70)` (simple 70-bar average of closes).
- Entry long: `CLOSE < ma1 AND RSI2 < 10` → buy-open long (`BK`), same-bar-close execution under the derived declaration. Strict `<` on both legs: a close exactly on the average or an RSI2 print of exactly 10 fires nothing.
- Exit long: `CLOSE < ma1 AND RSI2 > 90` → close long in full (`SP(BKVOL)` — the whole long position), same-bar-close execution. Strict `>` on the tail leg.
- Entry short: `CLOSE > ma1 AND RSI2 > 90` → sell-open short (`SK`), same-bar-close execution.
- Exit short: `CLOSE > ma1 AND RSI2 < 10` → close short in full (`BP(SKVOL)` — the whole short position), same-bar-close execution.
- Direction: two-sided with an explicit flat state. Cross-side same-bar dual-fire is impossible by construction (a close cannot be both strictly above and strictly below the average); same-side entry refires while positioned are no-ops under the preserved `AUTOFILTER` single-unit behavior (see Execution assumptions).
- Risk legs (pinned absence, not invented): no stop, no target, no trailing, no time exit anywhere — the sole position-closing paths are the two opposite-tail signal legs above.
- Display/plumbing isolation: the `liang` sizing line computes broker contract counts only and gates no order condition; no plot, no input beyond `Y=70`, no session/calendar/volume leg exists.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (prior-close reference, RSI2 gains/losses, MA70, all four trigger pairs). No `open` (except as nothing — fills are closes), no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (declared research frame per the derivation; the script takes no timeframe input and makes no multi-frame call, so it is single-frame by construction).
- Warmup: the MA70 leg needs 70 completed `1d` closes before it is statistically settled; RSI2 needs 2. The adopted warmup is the first 70 completed `1d` bars flat by record rule (predeclared researcher choice). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (declared port; the source venue `Futures_OKCoin BTC_USD quarterly` no longer exists as a pinned-connector market — no cross-venue equivalence claimed).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-tick/open on a 15m/15m FMZ backtest (no execution-timing override ships anywhere); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity, and cross-side dual-fire is structurally impossible (see Signal).
- Sizing/capital/costs: the `liang` broker-sizing line ships no portable sizing (quoted verbatim in Provenance) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) replace it here, never presented as source-native behavior.
- Concurrency: `AUTOFILTER` pins no same-direction adds — at most one long unit and at most one short unit logic (single engine position, one side at a time: a contra-side entry signal while positioned flips through the exit-then-entry bar sequence only if both legs fire, which requires opposite MA70 sides on one close — impossible; so any flip passes through at least one flat bar by construction); entries while already positioned on that side are no-ops, an exit while flat is a no-op, and re-entry is allowed immediately on the next qualifying extreme after any flat (no cooldown specified — explicitly none, not invented). No shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The mirror ships the full construction (Wilder-style RSI2 formula, MA70 side gate, strict-inequality four-leg order set with full-position closes, `AUTOFILTER`, single `Y=70` argument, StockCharts/pyalgotrade lineage comments), the author/title stamps, and the page-embedded 15m/15m January-2018→May-2020 backtest header. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 stop/limit/target/trailing/time legs — the sole position-closing paths are the two opposite-tail signal legs. A fade entry that keeps trending can ride the full adverse excursion with no guardrail; a −30% run against a fade is held to the next opposite tail by construction. This is the coded posture, disclosed, not a tunable parameter here.
2. Regime-cross trap, admitted plainly: exits require the exit bar to sit on the *same* MA70 side as the entry (long exits need `CLOSE<ma1`, short exits need `CLOSE>ma1`). A long opened below the average that rallies through it with RSI2 neutral never exits — the position is carried above the gate with no exit leg armed until price falls back below the average AND prints RSI2>90. Mirror image for shorts. This is the coded gating, disclosed as the record's principal structural edge case.
3. The entry buys weakness as it prints: the entry bar's own close already reads RSI2<10 (long) or RSI2>90 (short) — there is no confirmed-recovery requirement, so the fill systematically precedes any bounce. Disclosed, not repaired.
4. Thresholds and lengths are pinned literals (`Y=70`, RSI length 2, tails 90/10, strict inequalities): retuning a tail, lengthening the RSI, converting the fade into a recovery cross, adding a stop/target/filter/cooldown, disabling a side, or adding a regime-break exit would each be a different, unpinned rule — none is admitted here.
5. Scale-port boundary fenced: the source's 90/10 tails and MA70 were set in a 15m context; on `1d` bars the same arithmetic describes a slower phenomenon (multi-day panic tails under a ~quarterly side gate) with different trade frequency and holding character. The port is disclosed, not hidden, and this record makes no claim about the source timing's behavior or performance.
6. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT-`1d` research frame, same-bar-close fills, the adopted 70-bar warmup with record-rule pre-warmup flat, and house sizing — all predeclared above; formula, lengths, thresholds, inequalities, side gating, all four legs, full-position closes, two-sided direction, and the risk posture are source-verbatim. This record is therefore never evidence that the original 15m OKCoin-quarterly source itself passes.
7. Long/short legs while flat are side-locked, admitted plainly: an RSI2<10 washout printed *above* the average can only cover a short, never open a long; an RSI2>90 blowoff printed *below* the average can only exit a long, never open a short. Half of all extreme tails are entry-inert by code.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: Wilder-RSI2(2) / MA70 / 90-10 tails / strict inequalities / side gating / four legs / full closes / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Regime-gate relevance: removing the MA70 side condition (pure two-sided RSI2 90/10 fade — longs on any RSI2<10, shorts on any RSI2>90) must not improve net expectancy; fail ⇒ the 70-bar side gate adds nothing over the naked oscillator fade.
- F2 — Entry relevance: replacing the fade entries with side-only holding (long whenever `CLOSE<ma1`, short whenever `CLOSE>ma1`, flat never) must not improve net expectancy; fail ⇒ the RSI2-extreme timing adds nothing over holding the MA side.
- F3 — Exit relevance: removing the opposite-tail exit legs (each fade entry held until the next contra-side entry signal, passing through flat only at flips) must not improve net expectancy; fail ⇒ the explicit tail exits are dominated by simply staying positioned.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (declared port of a defunct OKCoin-quarterly source market). The close-only arithmetic ports across perpetual venues without structural change; both sides are explicit legs, so a spot-only deployment expresses the long half unchanged while the short half stays venue-gated (short permission unused, never silently converted). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read, so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing and frame: the source fills next-tick/open on a 15m-decision/15m-base OKCoin-quarterly backtest; this record executes same-bar-close on `1d` BTCUSDT. Backtest economics of the two timings, frames, and venues differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source configuration's performance.
- No price stop, no regime-break exit, and no time stop: adverse excursion after entry has no guardrail beyond the opposite-tail close, which may arrive late or never; a close through the MA70 side while positioned disarms the exit instead of triggering one. This is the coded posture, disclosed as the record's principal risk.
- No source cost declaration: no commission, fee, slippage, or funding assumption ships anywhere in the source — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Tails are rare by construction: 90/10 on a 2-period RSI fires only on consecutive near-limit bars, so the system spends most bars flat by code — long flat stretches earn nothing and any evaluation window is dominated by idle time. This is the coded selectivity, disclosed, not smoothed.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- FMZ canonical strategy page (homily, Last Modified 2020-05-14): https://www.fmz.com/strategy/207157
- Immutable mirror file at pinned commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (blob `33132661560e29932bfd5075280507b4444331a1`, 958 bytes): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/Larry-Connors-RSI2%E5%9D%87%E5%80%BC%E5%9B%9E%E5%BD%92%E7%AD%96%E7%95%A5.md
- Indicator lineage cited in-source (RSI2 construction reference, not a separate strategy source): https://school.stockcharts.com/doku.php?id=trading_strategies:rsi2
