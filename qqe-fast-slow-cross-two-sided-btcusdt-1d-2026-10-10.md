---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: QQE fast-slow cross two-sided on BTCUSDT 1d bars
created: 2026-10-10
updated: 2026-10-10
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2022-05-24
sources:
  - https://github.com/fmzquant/strategies/blob/87a415edf7b08065fbcbfbfefb7351cd929e4dbd/Quantitative-Qualitative-Estimation.md
  - https://www.tradingview.com/script/tJ6vtBBe-QQE/
  - https://www.fmz.com/strategy/365315
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# QQE fast-slow cross two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (pinned immutable GitHub file, live raw fetch 2026-10-10):

- Canonical file: https://github.com/fmzquant/strategies/blob/87a415edf7b08065fbcbfbfefb7351cd929e4dbd/Quantitative-Qualitative-Estimation.md (repo `fmzquant/strategies`, file commit `87a415edf7b08065fbcbfbfefb7351cd929e4dbd` dated 2024-03-03 — latest commit touching this path; record `source_as_of` 2022-05-24 is the file's own `Last Modified` stamp, never the fetch date. Author `ChaoZhang`; header `© KivancOzbilgic`, MPL-2.0 notice; `Detail` link https://www.fmz.com/strategy/365315).
- Full Pine v4 block read verbatim (`//@version=4`, `study("Quantitative Qualitative Estimation", shorttitle="QQE", precision=4, resolution="")`): 1 `study(` / 0 `strategy(` / 2 `strategy.entry` / 0 `strategy.close` / 0 `strategy.exit` / 0 `strategy.order`. The two `strategy.entry` calls sit inside `if buySignalr and showsignals ... else if sellSignallr and showsignals` — dead code under a `study(` declaration (Pine executes `strategy.*` only in `strategy` scripts), so every fill in this file is a predeclared researcher derivation (see declaration below) while the signal semantics stay source-coded. 5 `input(` declarations: `src = input(close)` (pinned default `close`), `length = input(14, "RSI Length")`, `SSF = input(5, "SF RSI SMoothing Factor")` — all three gate calculation; `showsignals = input(true)` gates both the Buy/Sell `plotshape` pair and the entry block (pinned `true` — `false` would silence every signal, disclosed); `highlighting = input(true)` is display-only (fill colors). 2 `rsi(` calls (the same `rsi(src, length)` expression feeds both `RSII` and `QQEF`), 2 `ema(` calls, 1 `abs(`, 6 `nz(` (`nz(WWMA[1])`, `nz(ATRRSI[1])`, four `nz(QQES[1])`), 2 `crossover(` (`buySignalr`, one BUY alert), 2 `crossunder(` (`sellSignallr`, one SELL alert), 1 `cross(` (cross alert only), 3 `plot(` (FAST, SLOW, 50-level — the `50` line renders only), 2 `fill(`, 2 `plotshape(` (`Buy` labelup on `buySignalr`, `Sell` labeldown on `sellSignallr`), 5 `alertcondition(`, 0 `request.*`, 0 `security(`, 0 `time(`, 0 `open` / 0 `high` / 0 `low` / 0 `hl2` / 0 `hlc3` / 0 `volume` — the only price read is `close` via pinned `src`.
- State rule read verbatim: `RSII = ema(rsi(src, 14), 5)`; `TR = abs(RSII - RSII[1])`; `wwalpha = 1 / 14`; `WWMA := wwalpha*TR + (1-wwalpha)*nz(WWMA[1])` from `0.0`; `ATRRSI := wwalpha*WWMA + (1-wwalpha)*nz(ATRRSI[1])` from `0.0` (Wilder double smoothing of RSI's own bar-to-bar range — an ATR of RSI, not of price); `QQEF = ema(rsi(src, 14), 5)` (identical expression to `RSII` — the FAST line is the twice-smoothed RSI itself); `QUP = QQEF + ATRRSI*4.236`; `QDN = QQEF - ATRRSI*4.236`; the ratchet `QQES := QUP < nz(QQES[1]) ? QUP : QQEF > nz(QQES[1]) and QQEF[1] < nz(QQES[1]) ? QDN : QDN > nz(QQES[1]) ? QDN : QQEF < nz(QQES[1]) and QQEF[1] > nz(QQES[1]) ? QUP : nz(QQES[1])` from deterministic seed `0.0` (no `na` seed, no `na` propagation anywhere in the order-gating path); `buySignalr = crossover(QQEF, QQES)`; `sellSignallr = crossunder(QQEF, QQES)`. The `4.236` envelope factor, `14`, and `5` are pinned literals.
- Direction semantics are source-coded three times over: `plotshape` Buy/Sell labels, "QQE BUY SIGNAL!" / "QQE SELL SIGNAL!" alert messages, `strategy.entry("Enter Long", strategy.long)` / `strategy.entry("Enter Short", strategy.short)`, and prose ("Buy when QQE FAST crosses above QQE SLOW ... Sell when QQE FAST crosses below QQE SLOW"). The prose's 50-level variants ("or just buy when QQE lines crosses above 50 level") are NOT coded in the signal block and are explicitly NOT adopted here (disclosed).
- Lineage (read live 2026-10-10, corroboration only — no line-level fact in this record comes from it): TradingView `glaz` original https://www.tradingview.com/script/tJ6vtBBe-QQE/ (`QQE`, OPEN-SOURCE SCRIPT, Feb 20 2015, 50-line Pine v1 block read verbatim in-browser: `study("QQE")`, `src = close`, `Fast = input(2.6180)`, `Slow = input(4.2360)`, `RSI = input(14)`, `SF = input(2)`, WiMA double smoothing, dual fast/slow ATR-trailing bands, `trend`/`trend1` ratchet state machines with `nz(trend[1], 1)` seeds — the same indicator family, dual-band ancestor of the pinned single-SLOW-cross variant). The porter's FMZ backtest header comment (`start: 2022-04-23, end: 2022-05-22, period: 1h, basePeriod: 15m, Futures_Binance BTC_USDT`) and backtest PNG are porter config/chrome, never adopted as strategy facts and never performance evidence.

Licence and rights: the pinned file is a public MIT-licensed (MPL-2.0-noticed) port of a public open-source TradingView publication. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly six: (1) order mapping — the `strategy.entry` pair is dead code under `study(`, so entering long on a `buySignalr` bar and short on a `sellSignallr` bar is the researcher's executable mapping of the source-coded Buy/Sell signal pair (plotshape + alerts + entry constants + prose, all agreeing), predeclared; (2) same-bar-close fills on the traded market's own `1d` bars (the source declares no execution timing anywhere; the porter's `1h`/`15m` header is not adopted); (3) position-state pin — single-unit per side, full reversal on the opposite signal, predeclared (Pine `strategy.entry` defaults to no pyramiding, consistent but not cited as execution proof); (4) an adopted 60-bar warmup with pre-warmup bars flat by record rule (covers RSI-14 seeding plus the Wilder double-smoothing stabilization plus ratchet settling plus margin — see Required data); (5) research market BTCUSDT Binance perpetual `1d` (the source names no market for the rule itself; the porter's `BTC_USDT` header informed but does not constitute the choice — the market remains a researcher choice, predeclared); (6) house sizing/capital/costs replacing the wholly absent source economics (see Execution assumptions). The `rsi(src,14)` / `ema(...,5)` / Wilder `1/14` double smoothing / `4.236` envelope / `QQES` ratchet / FAST-over-SLOW cross pair / `showsignals = true` / no-stop/no-target posture are source-verbatim.

Pre-write dedup (2026-10-10): working-tree case-insensitive searches for `qqe`, `quantitative qualitative`, `QQEF`, `QQES`, `ATRRSI`, `tJ6vtBBe`, `365315`, `87a415e`, and `kivanc` return zero strategy records using this source, author script, indicator, or mechanism. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #58 (reconstruction batch — file list verified, no oscillator record), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closed research PRs (#1–#94 reviewed by title) contain no QQE record; closed PR #6 (LazyBear WaveTrend wt1/wt2 cross) is an esa-normalized price oscillator cross with no RSI, no ATR envelope, no ratchet. Closest pool RSI records differ in mechanism class: `rsi-classic-level-reversal-btcusdt-1h-2026-10-07.md` trades 30/60 RSI levels (no smoothing envelope, no cross of two QQE lines); `rsi-ma-crossover-reversal-btcusdt-1d-2026-10-07.md` crosses Wilder RSI27 against its own SMA10 (single smoothing, no volatility envelope, no ratchet); `cumulative-rsi-dual-threshold-long-btcusdt-1h-2026-10-08.md` sums raw RSI prints (no EMA, no ATR, no cross); `vidya-cmo-adaptive-slope-trend-btcusdt-1h-2026-10-05.md` is a CMO-adaptive average slope system (different oscillator, different signal). Four-axis distinction: signal construction differs (twice-EMA-smoothed RSI against its own Wilder-double-smoothed ATR ratchet envelope — no pool record builds a trailing level from RSI's own volatility), trigger differs (FAST/SLOW cross pair with source-coded Buy/Sell labels rather than level breaks or MA crosses), data differs (close-only single-timeframe; zero volume read, unlike the Klinger family), and source identity differs (fmzquant GitHub `87a415e` port of KivancOzbilgic QQE with glaz 2015 dual-band lineage).

## Economic mechanism

### Source-reported

RSI-volatility envelope trend following: the FAST line is RSI(14) twice smoothed (Wilder RSI then 5-bar EMA); the SLOW line is a ratcheting trailing level hung `4.236` ATRs-of-RSI above/below FAST that only tightens in the direction of travel and locks when FAST reverses — the author's tenet, quoted in-prose: QQE is "a smoother version of RSI" whose "smoothed ATR lines" make it "less susceptible to short term volatility", with trend read as FAST-above-SLOW (up) versus FAST-below-SLOW (down) and signals "at the moment of crossing of the QQE FAST and QQE SLOW lines". The porter's own WARNING is preserved as source-reported negative evidence: "QQE IS A RSI BASED INDICATOR SO THAT IT CAN TRIGGER FALSE SIGNALS DURING DIVERGENCES!"

### Research interpretation

Edge-triggered two-sided reversal system on smoothed-momentum-versus-own-volatility state, with no price level, band break, stop, target, or confirmation leg beyond the single FAST/SLOW cross pair — long while FAST rides above SLOW after a `buySignalr` bar, short while FAST rides below SLOW after a `sellSignallr` bar, changing only on crosses. Unlike level-based RSI systems (classic 30/60, cumulative thresholds) the trigger here is relational (FAST vs its own trailing envelope), so a grinding one-directional market that never crosses keeps the full unit indefinitely — the bet, as derived, is on BTCUSDT daily smoothed-momentum persistence inside a self-scaling volatility envelope, never on an oversold/overbought level, breakout, squeeze, calendar, or mean-reversion anchor. Unlike price-ATR trailing systems (SuperTrend, Chandelier, Triple-EMA vol-stop) the trailing stop lives in RSI space, not price space: a vertical price spike that barely moves RSI(14)-smoothed momentum need not cross, while a slow RSI bleed can cross with no price extreme at all. The cost is symmetric: RSI-space chop that alternately crosses flips the full unit with no confirmation beyond the coded cross pair, no cooldown, and no cost guard — exactly the divergence-whipsaw failure the porter's WARNING names.

## Signal

Exact rule as pinned (`src = close`, `length = 14`, `SSF = 5`, `4.236`, `showsignals = true`, `highlighting = true` frozen — any other values are a different, unpinned rule):

- Declaration (derived): Pine v4 builtins (`rsi`, `ema`, `abs`, `nz`, `crossover`, `crossunder`, `cross`, `plot`, `fill`, `plotshape`, `alertcondition`) with v4 `na` semantics observed. `resolution = ""` resolves to the chart's own timeframe — single-timeframe by construction (0 `request.*` / 0 `security(`). `precision = 4`, the `50` plot, both `fill(` calls, and `highlighting` render only and gate no order. `src`/`length`/`SSF`/`showsignals` gate calculation or signals; the 50-level prose variants are not coded and not adopted.
- State (pinned, source-verbatim): `RSII = ema(rsi(close, 14), 5)`; `TR = abs(RSII - RSII[1])`; `wwalpha = 1/14`; `WWMA := wwalpha*TR + (1-wwalpha)*nz(WWMA[1])` from `0.0`; `ATRRSI := wwalpha*WWMA + (1-wwalpha)*nz(ATRRSI[1])` from `0.0`; `QQEF = ema(rsi(close, 14), 5)`; `QUP = QQEF + ATRRSI*4.236`; `QDN = QQEF - ATRRSI*4.236`; `QQES` ratchet as quoted in Provenance from deterministic seed `0.0`. `QQEF` and `RSII` are the identical expression — one FAST line, disclosed, not two independent smoothings.
- Orders (derived mapping, predeclared, source-signal-coded): a bar with `buySignalr = crossover(QQEF, QQES)` → enter long (closing any short in the same step, full reversal, no residual leg); a bar with `sellSignallr = crossunder(QQEF, QQES)` → enter short (closing any long likewise). `crossover`/`crossunder` are strict bar-pair relations and cannot co-fire on one bar — no same-bar ordering ambiguity exists anywhere in this record. Non-signal bars are explicit no-ops (pinned: the source `if/else-if` maps only signal bars to entries). Bars before arming are flat by record rule (see Required data).
- Risk legs (pinned absence, not invented): 0 `strategy.close` / `strategy.exit` / `strategy.order` ship anywhere — the derived posture is explicitly no stop, no target, no trailing, no time exit; the sole position-changing path is the opposite cross reversing the full unit.
- Direction: two-sided long/short with symmetric reversal. Futures venue required for the short leg (researcher market choice — pinned).
- Display isolation: `plot` / `fill` / `plotshape` / `alertcondition` / `precision` render or notify only and cannot change any order; the `strategy.entry` pair is dead code under `study(` and is cited for direction semantics only, never as executed fills.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (via pinned `src = close`; the input's other options — high/low/open/hl2/hlc3/hlcc4/ohlc4 — are explicitly NOT adopted). No `open`, no `high`/`low` range, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (`resolution = ""` = chart timeframe; 0 `request.*` / 0 `security(` anywhere; the porter's `basePeriod: 15m` header carries no cross-timeframe indicator read in the verbatim logic and is not adopted).
- Single decision timeframe `1d` (researcher choice — the pinned rule names no timeframe; the porter's `1h` header is not adopted). One evaluation per completed bar; all reads reference confirmed bars only (`[1]` lags, confirmed-bar `crossover`/`crossunder` relations).
- Warmup: `rsi(14)` seeds on early bars and the Wilder `1/14` double smoothing plus the `QQES` ratchet need stabilization bars; all seeds are deterministic (`0.0` / `nz` fallbacks — no `na`-propagation blindness trap, disclosed). The adopted warmup is the first 60 completed `1d` bars flat by record rule (14 RSI seeding + ~28 Wilder double-smoothing stabilization + ratchet settling + margin — predeclared researcher choice); no signal before bar 61 may trade. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice informed by the porter's displayed `BTC_USDT` backtest header — the pinned rule itself names no market; naming normalization is the only market step, and no source-market equivalence is claimed).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source declares no execution timing (indicator declaration); this record does not claim any source fill convention. No maker-touch, queue, or intrabar-path-dependent fill: with mutually exclusive cross legs and no stop/target legs, there is no same-bar ordering ambiguity of any kind.
- Sizing/capital/costs: the source ships no sizing, capital, fee, slippage, margin, or funding concept of any kind. The explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all) apply to the derived evaluation here, with the single-unit/no-add/reverse-full position pin from Signal, never presented as source-native behavior.
- Concurrency: at most one position (long or short) at any time; the opposite cross reverses in full in one step; re-entry after a reversal needs only the next opposite cross (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The short leg requires margin-short permission, realistic on the pinned perpetual venue.

## Evidence

### Source-reported

The pinned file ships the full construction (Pine v4 block: `study` declaration, five inputs at pinned defaults close/14/5/true/true, Wilder `1/14` double smoothing of RSI's bar-to-bar range, the `4.236` envelope pair, the five-leg `QQES` ratchet from seed `0.0`, the FAST/SLOW cross signal pair with Buy/Sell labels, five alert conditions, the dead-code `strategy.entry` long/short pair, and the prose direction semantics plus the DIVERGENCE warning). The porter's backtest header comment and PNG are config/chrome, never performance evidence. The page ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Dead-code orders, admitted plainly: the `strategy.entry` pair cannot execute under `study(` — every fill here is a researcher mapping of the source-coded Buy/Sell signal pair (plotshape + alerts + entry constants + prose, mutually agreeing), disclosed, not source-executed behavior.
2. No hidden exits or risk layer: 0 `strategy.close` / `strategy.exit` / `strategy.order` ship anywhere — the sole position-changing path is the opposite cross reversing the full unit. The absence of any stop is coded absence, disclosed, not a tunable parameter here.
3. Always-in-market exposure after arming, admitted plainly: after the first cross the system is never flat — RSI-space chop that alternately crosses flips the full unit on every alternating cross with no confirmation beyond the coded pair, no cooldown, and no cost guard; adverse excursion between crosses has no guardrail of any kind. This is the coded trade, disclosed — and the exact failure the porter's DIVERGENCE warning names.
4. Envelope-blindness, disclosed: because the trailing level is denominated in RSI units, a violent price spike that leaves smoothed RSI inside the envelope fires nothing, while a slow RSI bleed with no price extreme can flip the full unit. RSI-space and price-space extremes are different events here, pinned, not repaired.
5. Warmup flatness fenced: the first 60 bars are flat by record rule, so any textbook cross inside warmup is deliberately untraded — pinned, not recovered. There is no `na`-propagation blindness (all seeds deterministic `0.0`); the warmup is stabilization-only, disclosed as a researcher choice.
6. Source basis fenced: the pinned rule names no market or timeframe (the porter's `BTC_USDT` / `1h` / `15m` header is porter config). The BTCUSDT-`1d` choice, same-bar-close fills, single-unit/no-add/reverse-full pin, 60-bar warmup, and house sizing/costs are researcher choices, disclosed (market informed by the porter's header, which is corroboration, not provenance for line-level facts); this record is therefore never evidence that any source-market deployment passes.
7. Derivation boundary fenced: the only non-source-native behaviors in this record are the signal-to-order mapping, same-bar-close fills, the position-state pin, the adopted 60-bar warmup with record-rule pre-warmup flat, the BTCUSDT-`1d` market choice, and house sizing/costs — all predeclared above; the `rsi(close,14)` / `ema(...,5)` / Wilder double smoothing / `4.236` envelope / `QQES` ratchet with `0.0` seed / FAST/SLOW cross pair / `showsignals = true` / no-stop/no-target/no-cooldown posture are source-verbatim. This record is therefore never evidence that the original script itself passes.
8. The `14` / `5` / `4.236` literals, the plain FAST/SLOW cross pair (not the prose's 50-level variants, not touch, not level-hold), the full-unit reversal, the two-sided stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning any literal, gating crosses on the 50 level, adding a stop/target/filter/cooldown/gate, dropping the short leg, setting `showsignals = false`, switching `src` off `close`, or sizing partially instead of full-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `src = close` / `length = 14` / `SSF = 5` / `4.236` / ratchet / FAST/SLOW cross pair / full-unit reversal / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Envelope relevance: replacing the Wilder-double-smoothed ATR-of-RSI envelope with a fixed ±10 RSI-unit band around QQEF through the same cross pair must not improve net expectancy; fail ⇒ the RSI-volatility envelope adds nothing over a fixed band.
- F2 — Smoothing relevance: replacing twice-smoothed `ema(rsi(14), 5)` FAST with raw `rsi(close, 14)` through the same ratchet and cross pair must not improve net expectancy; fail ⇒ the double smoothing adds nothing over raw RSI.
- F3 — Cross relevance: replacing the FAST/SLOW cross pair with 50-level FAST breaks (long above / short below) must not improve net expectancy; fail ⇒ the coded cross pair carries no advantage over the prose's level variant and the pin choice is arbitrary.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision frame researcher-chosen `1d`; arithmetic over `close` only with no venue-specific read). The construction ports across perpetual venues without structural change. The short leg requires margin-short permission (realistic on perpetual venues; a spot-only deployment cannot express the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere; `src` pinned to `close`), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Signal-to-order gap: the `strategy.entry` pair is dead code under `study(` — every entry, reversal, and sizing behavior here is a researcher mapping of a source-coded signal pair, disclosed, not source-executed (signal semantics corroborated four ways in-source: plotshape labels, alert messages, entry constants, prose).
- Researcher market/frame: the pinned rule names no market or timeframe — BTCUSDT `1d` is a researcher choice informed by the porter's backtest header; signal timing on other markets or frames would differ by construction.
- Derived fill timing: same-bar-close execution is a researcher choice over logic that declares no timing; backtest economics of other timings differ by construction — the adaptation is disclosed, not hidden.
- Position-state pin: same-side-add and reversal-quantity behavior executes nowhere in-source; the single-unit/no-add/reverse-full pin is a researcher choice, disclosed, not source-verbatim.
- No price stop, no time stop, never flat after arming: adverse excursion after entry has no guardrail beyond the opposite cross, which may arrive many bars later or after deep excursion; alternating crosses whipsaw the full unit repeatedly, especially under the porter's own DIVERGENCE warning. This is the coded posture, disclosed as the record's principal risk.
- No source cost declaration: no capital, commission, fee, slippage, margin, or funding assumption ships anywhere — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Warmup cost: the first 60 bars are flat by record rule, so any textbook cross inside warmup is deliberately untraded — pinned, not recovered.
- Single-smoothing identity: `QQEF` and `RSII` are the identical `ema(rsi(src,14),5)` expression — the record pins one FAST line fed by one smoothing chain, never two independent smoothings; "double" smoothing claims beyond the coded chain are not made here.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Quantitative-Qualitative-Estimation [ChaoZhang port of KivancOzbilgic QQE] pinned GitHub file at commit `87a415edf7b08065fbcbfbfefb7351cd929e4dbd` (file `Last Modified` 2022-05-24; FMZ strategy 365315): https://github.com/fmzquant/strategies/blob/87a415edf7b08065fbcbfbfefb7351cd929e4dbd/Quantitative-Qualitative-Estimation.md
- QQE [glaz] canonical open-source script page, dual-band lineage ancestor (published 2015-02-20): https://www.tradingview.com/script/tJ6vtBBe-QQE/
- FMZ strategy detail page `Quantitative Qualitative Estimation` [ChaoZhang] (porter config and backtest chrome only — full code login-gated, never cited for line-level facts): https://www.fmz.com/strategy/365315
