---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Connors Double Seven pullback long with SMA200 gate on BTCUSDT 1d bars
created: 2026-10-09
updated: 2026-10-09
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-11-28
sources:
  - https://www.fmz.com/strategy/473246
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E8%B6%8B%E5%8A%BF%E8%B7%9F%E8%B8%AA%E4%B8%8E%E5%9D%87%E5%80%BC%E5%9B%9E%E5%BD%92%E5%8F%8C%E9%87%8D%E4%BC%98%E5%8C%96%E4%BA%A4%E6%98%93%E7%B3%BB%E7%BB%9FDouble-Seven-Strategy-Trend-Following-and-Mean-Reversion-Dual-Optimization-Trading-SystemDouble-Seven-Strategy.md
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Connors Double Seven pullback long with SMA200 gate on BTCUSDT 1d bars

## Provenance

Primary source read end to end (immutable public mirror file plus its recorded FMZ canonical page, fetched 2026-10-09):

- Canonical page: https://www.fmz.com/strategy/473246 (page title `Trend Following and Mean Reversion Dual Optimization Trading System(Double Seven Strategy) | FMZ`, publisher account `ChaoZhang` with 2 page hits, `Created: 2024-11-28 15:41:34`, equal to the mirror `Last Modified`). Fetched over HTTPS during this cycle (664183 bytes): the page embeds the full `/*backtest ... */` header quoted below, the active `strategy("Larry Connors' Double Seven Strategy", overlay=true)` declaration, and the complete order block (`1 strategy.entry` / `1 strategy.close` / `0 strategy.exit` / `0 strategy.order` in page state, counted verbatim). Word-boundary counts over the whole landing HTML: `Net Profit` 0, `Profit Factor` 0, `Sharpe` 0, `Max Drawdown` 0, `Win Rate` 0, `win rate` 0, `Annualized` 0 — the page ships no performance numbers of any kind (adopted as `source_as_of` 2024-11-28 from the page Created stamp, which equals the mirror `Last Modified`).
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit date 2025-04-30 11:10:28 +0800, subject `update`; verified repository head at research time via the GitHub commits API — the same head pin as the merged DPO-EMA, KST, Schaff, TRIX, SQZMOM-LB, Aroon, Qstick, AC, Elder-ray and ActionZone admissions), exact file path `趋势跟踪与均值回归双重优化交易系统Double-Seven-Strategy-Trend-Following-and-Mean-Reversion-Dual-Optimization-Trading-SystemDouble-Seven-Strategy.md` (non-ASCII filename preserved verbatim; percent-encoded blob URL in Sources). File 7543 bytes, blob SHA `ca22676fee69a94f53d71fd9057d51ac3111f6e8` (verified against the GitHub contents API at the pinned commit — size and SHA both match). The mirror prints `> Detail` = https://www.fmz.com/strategy/473246 and `> Last Modified` = 2024-11-28 15:41:34 (equal to the page Created stamp). The prose program description (both the Chinese original and the English `[trans]`) describes exactly the coded rule (MA200 trend gate plus 7-day low entry / 7-day high exit, quoted in Economic mechanism), so prose and code agree on the mechanism.
- Full `//@version=5` block read in full (code lines from `/*backtest` through the final `plot`, strategy declaration `strategy("Larry Connors' Double Seven Strategy", overlay=true)`; code header credits `© EdgeTools` under MPL-2.0). The page-embedded `/*backtest*/` header (`start: 2019-12-23 08:00:00`, `end: 2024-11-27 00:00:00`, `period: 1d`, `basePeriod: 1d`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`) is byte-present on both the canonical page preview (2 hits each for `period: 1d`, `basePeriod`, `BTC_USDT`) and the mirror block — market (`BTC_USDT` Binance futures) and decision frame (`1d`) are therefore source-native, never researcher-chosen. `basePeriod: 1d` equals the decision frame here, so there is no second execution-granularity frame to fence.
- Text census over the pinned code block: 1 `strategy.entry` (`strategy.entry("Long", strategy.long)`) / 1 `strategy.close` (`strategy.close("Long")`, no `when=`, unconditional on its bar) / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=`/`qty_percent` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `time(` / 0 `volume` / 0 `open`/`high`/`low` (the rule reads `close` only) / 0 `input.*` (there are no user inputs at all — 200 and 7 are hardcoded literals, so no default table can drift). `pyramiding`, `process_orders_on_close`, `calc_on_every_tick`, `calc_on_order_fills`, `commission`, `initial_capital` and `default_qty_*` are unset throughout. The single `plot` call (MA200 line) feeds no order condition; order logic reads exactly the two channel booleans.
- No risk layer ships anywhere in the source: zero stop/target/trailing/time-exit order legs, and the mirror's own optimization list names stop-loss enhancement and dynamic position management only as future work (`止损机制完善`, `仓位管理优化`), confirming none ships. The channel-high close posture below is therefore the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention.
- Page/mirror performance language is absent entirely (no table, figure, or number; the prose adjectives carry no quantity) — this record claims no source-reported performance and no reproduced performance.

Licence and rights: the canonical page is a public FMZ strategy publication by ChaoZhang; the pinned code block carries an MPL-2.0 header crediting EdgeTools. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly three: (1) same-bar-close fills (the source fills next-bar-open — no `process_orders_on_close` ships anywhere, quoted verbatim in census); (2) an adopted 200-bar warmup with pre-warmup bars flat by record rule (the SMA200 leg needs 200 completed bars — see Required data); (3) house sizing/capital replacing the language-default sizing (no `default_qty_*` ships anywhere — see Execution assumptions). Market (BTCUSDT Binance futures), decision frame (`1d`), pinned literals (SMA200 / 7-bar close channel), entry/exit triggers, order IDs, direction handling, the unconditional close leg, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-09): working-tree case-insensitive searches for `double-seven`, `double seven`, `doubleseven`, `connors`, `lowestClose7`, and `473246` return zero admitted rules using this source, author strategy, or mechanism — the only `Connors` hit anywhere is a lineage citation inside `etf-3day-reversion-ema5-mean-reversion-long-btcusdt-1d-2026-10-08.md` (a different TradeAutomation TV source admitting a 3-day lower-highs/lows chain under an EMA5 gate with an EMA5-recross exit, never a 7-day close channel under an SMA200 gate). Same-publisher ChaoZhang records exist (DPO-EMA FMZ 474030, HBTS FMZ 474020, KST FMZ 436493, Schaff FMZ 365905, TRIX FMZ 428683, Aroon FMZ 438795, Qstick FMZ 439854, AC FMZ 435716, Elder-ray FMZ 432762, Low-High FMZ 432972, ActionZone FMZ 448778) but carry different canonical identities, different indicator families, and different order sets. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #58 (ML/reconstruction batch — file list verified, no channel-pullback record), and #63 (SuperTrend ATR-flip trend long) — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `low-high-dip-tp-long-btcusdt-1d` (TradeAutomation FMZ 432972) recovers back *over* the prior 20-bar low (`crossover(close, lowest(close,20)[1])`) under an EMA200 gate and exits on a fixed 8% take-profit; `three-down-three-up-consec-close-long-btcusdt-1h` counts three consecutive lower/higher *closes* with no moving-average leg anywhere; `etf-3day-reversion-ema5-mean-reversion-long-btcusdt-1d` chains three lower highs AND lower lows under an EMA5 gate with an EMA5-recross exit. Five-axis distinction: mechanism differs (Connors pullback touch of the 7-day lowest close under a 200-day SMA regime gate with a 7-day-highest-close channel exit), signal construction differs (`close <= ta.lowest(close,7)` with the current bar inside the window AND `close > ta.sma(close,200)` versus recovery-crosses, close-count chains, or high/low chains), exits differ (channel-high `strategy.close` leg, no fixed-percentage leg, no average-recross leg), horizon is `1d` BTCUSDT, source identity differs (FMZ 473246, ChaoZhang, EdgeTools code).

## Economic mechanism

### Source-reported

Uptrend pullback capture (mirror `策略原理`, corroborated line-for-line by the code): the 200-day average defines the bull regime and only bars printing above it may buy; within that regime the 7-day lowest close marks the short-term washed-out print and buying it is the long entry; the first print at the 7-day highest close ends the trade. The design bets that pullbacks inside an intact long-term uptrend resolve upward before the channel top gives the profit back.

### Research interpretation

Regime-gated channel-toucher with an explicit flat state, long-only. Unlike recovery-cross systems (the Low-High record) that wait for price to climb back *over* a historical extreme, this system buys the extreme print itself (`close <= lowest`, current bar inside the window) — a lower fill by construction, at the cost of catching knives when the regime gate lags a topped market. Unlike count-chain systems (three-down, ETF 3-day) that require consecutive directional prints, a single new 7-day low suffices here even inside an otherwise choppy week. Unlike always-in-market holders, the system rests flat whenever the last signal was a channel-high close, and it never shorts: overbought 7-day highs while flat are no-ops, and 7-day lows printed below the SMA200 gate are ignored. The bet is on short-horizon mean reversion *inside* a 200-day bull regime at the ~1–2-week scale (7 daily closes), not on any oscillator level, volatility band, or calendar effect.

## Signal

Exact rule as pinned (no inputs exist — every value below is a hardcoded literal):

- Declaration (derived): `strategy("Larry Connors' Double Seven Strategy", overlay=true)` with same-bar-close execution adopted for the derived record (no such argument ships in the source) and house sizing replacing the unset language-default sizing (see Execution assumptions). `calc_on_every_tick` and `calc_on_order_fills` are unset (both default false: exactly one evaluation per completed bar). No commission, margin, or capital assumption ships anywhere — pinned as absent, with house costs applying to the derived evaluation (see Execution assumptions).
- Regime (pinned): `ma200 = ta.sma(close, 200)`; `priceAboveMa200 = close > ma200` (strict `>`: a close exactly on the average fails the gate).
- Channel (pinned): `lowestClose7Days = ta.lowest(close, 7)`; `highestClose7Days = ta.highest(close, 7)` — both windows include the current bar by built-in semantics, so the entry trigger is the close printing a fresh 7-bar low and the exit trigger is the close printing a fresh 7-bar high.
- Entry long: `if (longCondition) strategy.entry("Long", strategy.long)` with `longCondition = priceAboveMa200 and close <= lowestClose7Days` — fires on the single bar where the close is both above the 200-day average and at/through the trailing 7-close minimum, with same-bar-close execution under the derived declaration.
- Exit: `if (exitCondition) strategy.close("Long")` with `exitCondition = close >= highestClose7Days` — unconditional close of the long on any bar whose close is at/through the trailing 7-close maximum (no `when=`, no quantity qualifier: the whole position), with same-bar-close execution under the derived declaration. No stop, no target, no trailing, no time exit — pinned as written, explicitly none, not invented.
- Direction: long-only with an explicit flat state. No short leg exists anywhere; on a spot venue the rule expresses unchanged (see Crypto portability).
- Display isolation: the single `plot(ma200, ...)` renders only and cannot change any order.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (regime average, both 7-bar channel extremes, both trigger pairs). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (source-native per the page-embedded `period: 1d` header; `basePeriod: 1d` equals the decision frame, so no second frame exists). The script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction.
- Warmup: the SMA200 leg needs 200 completed `1d` closes before it is statistically settled; the 7-bar channel needs 7. The adopted warmup is the first 200 completed `1d` bars flat by record rule (predeclared researcher choice). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (source-native per the header's `Futures_Binance BTC_USDT`; venue transfer from `BTC_USDT` to `BTCUSDT` spot-symbol spelling is naming only, never presented as a market change).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar-open (no execution-timing argument ships anywhere — quoted verbatim in Provenance); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill. With no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. Entry and exit legs are evaluated as separate `if` statements in source order (entry first, then exit): on a bar where both conditions hold (possible only when all 7 trailing closes are equal — see Negative evidence), the derived execution fills the entry at the close and closes it at the same close, ending flat; no ordering resolution beyond source order is required.
- Sizing/capital/costs: no `default_qty_*`, commission, or margin assumption ships anywhere (quoted verbatim in census) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) replace the unset language defaults here, never presented as source-native behavior.
- Concurrency: no `pyramiding` ships anywhere, pinning the language default of no same-direction adds — at most one long unit under the fixed order ID `Long`; entry refires while already long are no-ops by the language default, the channel-high close exits in full, an exit while flat is a no-op, and re-entry is allowed immediately on the next qualifying pullback after any flat (no cooldown specified — explicitly none, not invented). Single engine position; no short side exists to conflict; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The mirror ships the full construction (SMA200 regime line, 7-bar lowest/highest close channel, strict-above gate, touch-low entry, touch-high exit, fixed `Long` order ID, unconditional close leg), the active `strategy(...)` declaration, the `Larry Connors' Double Seven Strategy` title, and the page-embedded 1d/1d December-2019→November-2024 backtest header. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=`/`qty_percent` — the sole position-closing path is the coded channel-high `strategy.close("Long")` leg. The absence is coded (the order block ends with the close leg and no order call follows), and the mirror's optimization prose proposes stop-loss enhancement and dynamic sizing as future work, corroborating that none ships — fenced in Limitations for the reviewer rather than upgraded into a source claim.
2. The entry trigger includes the current bar in its window (`ta.lowest(close, 7)` counts the forming close): the entry buys weakness as it prints, never a confirmed recovery — a strictly weaker fill than recovery-cross systems, disclosed, not repaired.
3. Exit-leg conditionality, admitted plainly: a long opened on a 7-day-low touch exits only on the next 7-day-high touch. A market that grinds sideways between the extremes, or that breaks the SMA200 regime downward after entry, never exits until a fresh 7-day high prints — there is no stop, no time-stop, and no regime-break exit (a close back under MA200 while long changes nothing by code). This is the coded trade, disclosed, not a tunable parameter here.
4. Degenerate equal-close bars fire both legs: when all 7 trailing closes are identical, `close <= lowest` and `close >= highest` are both true; source order (entry block before exit block) fills the long at the close and closes it at the same close, ending flat with two fills and no overnight exposure. This is the coded ordering, disclosed as the record's principal microstructure edge case.
5. Long-only flat stretches earn nothing: while the last signal was a channel-high close the system holds no position by code; 7-day lows printed under the SMA200 gate are ignored by code, not by venue choice — disabling nothing, since no short leg exists to disable.
6. The SMA200 literal, the 7-bar channel length, the touch (not cross) semantics, the strict-above regime gate, the fixed order ID, the long-only posture, the unconditional close leg, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning a length, converting the touch into a recovery cross, adding a stop/target/filter/cooldown, enabling a short side, or adding a regime-break exit would each be a different, unpinned rule — none is admitted here.
7. Derivation boundary fenced: the only non-source-native behaviors in this record are same-bar-close fills, the adopted 200-bar warmup with record-rule pre-warmup flat, and house sizing — all predeclared above; market, timeframe, every literal, both triggers, the close leg, and the risk posture are source-verbatim. This record is therefore never evidence that the original next-bar-open 1d/1d source itself passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: SMA200 / 7-bar close channel / touch-low entry / touch-high exit / strict regime gate / long-only / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Regime-gate relevance: removing the SMA200 gate (pure 7-day lowest-touch entry with 7-day-highest exit) must not improve net expectancy; fail ⇒ the 200-day regime filter adds nothing over the naked channel.
- F2 — Entry relevance: replacing the pullback-touch entry with the always-live regime hold (long whenever `close > ma200`, flat otherwise) must not improve net expectancy; fail ⇒ the 7-day-low touch adds nothing over holding the regime.
- F3 — Exit relevance: removing the channel-high close leg (holding the long through channel highs — buy-and-hold from the first qualifying pullback, since no opposite signal exists) must not improve net expectancy; fail ⇒ the explicit channel exit is dominated by simply staying positioned.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (source-native venue family). The close-only arithmetic ports across perpetual venues without structural change; the rule is long-only with no short leg, so a spot-only deployment expresses it unchanged. No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read, so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source fills next-bar-open on a 1d-decision/1d-base Binance-futures backtest; this record executes same-bar-close on `1d` BTCUSDT. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- No price stop, no regime-break exit, and no time stop: adverse excursion after entry has no guardrail beyond the channel-high close, which may arrive late or never in a topped market; a close back under SMA200 while long is held, not exited. This is the coded posture, disclosed as the record's principal risk.
- No source cost declaration: no commission, fee, slippage, or funding assumption ships anywhere in the source — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- SMA200 lag at regime turns: the 200-day average turns slowly, so early-bull pullbacks buy under a still-falling average (gated out) while late-bear breakdowns can enter just before the gate flips — the lag is the coded gate, disclosed, not smoothed.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- FMZ canonical strategy page (ChaoZhang, Created 2024-11-28): https://www.fmz.com/strategy/473246
- Immutable mirror file at pinned commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (blob `ca22676fee69a94f53d71fd9057d51ac3111f6e8`, 7543 bytes): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E8%B6%8B%E5%8A%BF%E8%B7%9F%E8%B8%AA%E4%B8%8E%E5%9D%87%E5%80%BC%E5%9B%9E%E5%BD%92%E5%8F%8C%E9%87%8D%E4%BC%98%E5%8C%96%E4%BA%A4%E6%98%93%E7%B3%BB%E7%BB%9FDouble-Seven-Strategy-Trend-Following-and-Mean-Reversion-Dual-Optimization-Trading-SystemDouble-Seven-Strategy.md
- Pine strategy semantics (order calls, default execution, built-in averages): https://www.tradingview.com/pine-script-reference/v5/
