---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Klinger volume-oscillator trigger-flip two-sided on BTCUSDT 1d bars
created: 2026-10-10
updated: 2026-10-10
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2017-08-29
sources:
  - https://www.tradingview.com/script/9iPwzLLR-Klinger-Volume-Oscillator-KVO-Strategy/
  - https://www.fmz.com/strategy/434301
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Klinger volume-oscillator trigger-flip two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (canonical TradingView page, live browser read 2026-10-10):

- Canonical page: https://www.tradingview.com/script/9iPwzLLR-Klinger-Volume-Oscillator-KVO-Strategy/ (title `Klinger Volume Oscillator (KVO) Strategy`, author `HPotter` WIZARD, `OPEN-SOURCE SCRIPT`, dated Aug 29 2017 — adopted as `source_as_of` 2017-08-29; stats `1/8/7` likes/comments/followers and `11 150` views are page chrome, never performance evidence).
- Full Pine v2 block read verbatim (41 lines, `//@version=2`, `study(title="Klinger Volume Oscillator (KVO)", shorttitle="KVO")`): 1 `study(` / 0 `strategy(` / 0 `strategy.entry` / 0 `strategy.close` / 0 `strategy.exit` / 0 `strategy.order` — a pure bar-coloring indicator with zero order calls, so every order in this file is a predeclared researcher derivation (see declaration below). 3 `input(` declarations: `TrigLen = input(13, minval=1)`, `FastX = input(34, minval=1)`, `SlowX = input(55, minval=1)` — all three gate calculation, zero display-only inputs. 3 `ema(` calls (`xFast`, `xSlow`, `xTrigger`), 2 `iff(` calls (the `xTrend` sign leg and the `pos` state leg), 1 `hline(` (zero line — display only), 1 `barcolor(`, 2 `plot(`, 1 `nz(`, 0 `request.*`, 0 `security(`, 0 `time(`, 0 `open`, 1 `volume` read (inside `xTrend`), `high`/`low`/`close` read only via `hlc3` and `hlc3[1]`.
- State rule read verbatim: `xTrend = iff(hlc3 > hlc3[1], volume * 100, -volume * 100)`; `xFast = ema(xTrend, FastX)`; `xSlow = ema(xTrend, SlowX)`; `xKVO = xFast - xSlow`; `xTrigger = ema(xKVO, TrigLen)`; `pos = iff(xKVO > xTrigger, 1, iff(xKVO < xTrigger, -1, nz(pos[1], 0)))`; `barcolor(pos == -1 ? red : pos == 1 ? green : blue)`. Equal-sum bars (`hlc3 == hlc3[1]`) take the `iff` false leg (`-volume * 100`, distribution) — source-verbatim simplification, pinned, never "corrected" to a textbook dm/cm variant here. Equality bars (`xKVO == xTrigger`) hold the prior `pos` via `nz(pos[1], 0)`; the seed is deterministic `0` (flat/blue), so there is no `na` seed and no `na` propagation anywhere in the order-gating path.
- No performance table, figure, or number ships anywhere on the page or in the code — this record claims no source-reported performance and no reproduced performance. The page-chart quote (ES 1D CME) is page chrome, never adopted as a strategy fact — the canonical source names no tradable market.

Corroborating port (read live 2026-10-10, prose + config only — full code is login-gated and therefore never cited for line-level facts): FMZ `ChaoZhang` strategy https://www.fmz.com/strategy/434301 (`流量主导型震荡量化策略`, created 2023-12-05), whose visible code header is `Copyright by HPotter v1.0 30/08/2017` — the same HPotter lineage. Its prose states the identical construction (`xTrend` / 34-day `xFast` / 55-day `xSlow` / `xKVO` spread / 13-day `xTrigger`) and the identical direction semantics (`上穿13天均线xTrigger时做多,下穿时做空` — long on cross above, short on cross below), and its displayed backtest block uses `period: 1d`, `basePeriod: 1h`, `BTC_USDT` on `Futures_Binance` with strategy params `TrigLen` / `FastX` / `SlowX` / `Trade reverse`. The FMZ port is corroboration only; every line-level fact in this record comes from the verbatim TV read.

Licence and rights: the canonical page is a public open-source TradingView publication. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly six: (1) state-to-order mapping — the source ships zero order calls (bar colors only), so entering long on the `pos` flip to `1` and short on the flip to `-1` is the researcher's executable mapping, predeclared and corroborated by the FMZ port's prose direction semantics; (2) same-bar-close fills on the traded market's own `1d` bars (the source declares no execution timing anywhere); (3) position-state pin — single-unit per side, equality-hold bars as no-op, full reversal on the opposite flip, predeclared (the source has no sizing concept at all); (4) an adopted 70-bar warmup with pre-warmup bars flat by record rule (covers the 55-bar slow-EMA stabilization plus the 13-bar trigger smoothing plus 2 bars margin — see Required data); (5) research market BTCUSDT Binance perpetual `1d` (the canonical source names no market; the FMZ port's displayed `BTC_USDT` / `1d` backtest block informed but does not itself constitute the choice — the market remains a researcher choice, predeclared); (6) house sizing/capital/costs replacing the wholly absent source economics (see Execution assumptions). The `xTrend` sign leg (including the equal-sums false leg), the 34/55/13 lengths, the `xKVO` spread, the sticky `pos` state machine with equality hold and `0` seed, and the no-stop/no-target posture are source-verbatim.

Pre-write dedup (2026-10-10): working-tree case-insensitive searches for `klinger`, `xKVO`, `xTrigger`, `xTrend`, `9iPwzLLR`, `434301`, `432845`, `430373`, and `volume force` return zero strategy records using this source, author script, indicator, or mechanism — the only volume text anywhere is gates, never a volume-constructed oscillator. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #58 (reconstruction batch — file list verified, no oscillator record), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closed research PRs (#1–#93 reviewed by title) contain no Klinger record; closed PR #6 (LazyBear WaveTrend wt1/wt2 cross) is a price-only esa-normalized oscillator cross — different construction, different data (no volume read), different source. Closest pool records differ in mechanism class: `macd-signal-cross-reversal-btcusdt-1d-2026-10-09.md` crosses a price-only MACD line against its signal with plain `crossover` calls (no volume read, no sticky state, no equality hold); `alma-cross-volume-gate-btcusdt-1d-2026-10-09.md` crosses two price averages and reads volume only as a gate (volume never enters the oscillator arithmetic); `dual-ema-engulfing-volume-long-btcusdt-1h-2026-10-07.md` likewise gates on volume while the signal is EMA alignment plus pattern. Four-axis distinction: signal construction differs (signed-volume-force double-EMA spread against its own EMA trigger with a sticky equality-hold state — no pool record builds its oscillator from signed volume), trigger differs (strict-inequality state flip with hold bars versus crossover calls or level breaks), data differs (first volume-constructed oscillator in the pool — `volume` gates an order leg), and source identity differs (TV `9iPwzLLR` HPotter 2017-08-29 with FMZ 434301 port corroboration versus other TV authors or FMZ IDs).

## Economic mechanism

### Source-reported

Volume-force trend following: each bar's entire volume is signed positive (accumulation) when the `hlc3` sum rises versus the prior bar and negative (distribution) otherwise; the fast (34) minus slow (55) EMA spread of that signed force (`xKVO`) measures whether near-term money flow runs hotter than its own baseline, and its position against its 13-bar trigger decides the bar color. The author's tenets (quoted in-code): rising sums accumulate, falling sums distribute, and a strong rising volume force should accompany an uptrend then contract late — the system is built to be sensitive enough for short-term tops/bottoms yet reflective of long-term money flow.

### Research interpretation

Edge-triggered two-sided reversal system on money-flow state, with no price level, band, stop, target, or confirmation leg beyond the single spread-versus-trigger comparison — long while `pos == 1`, short while `pos == -1`, changing only on strict-inequality flips, holding through equality bars. Unlike price-only signal-line crosses (MACD, KST, TRIX, TSI, DPO) where both lines derive from `close` smoothing, here the primary line is a volume-signed quantity: a large-volume bar whose `hlc3` sum barely rises still injects the full `+volume * 100` into the fast leg, so climactic-volume bars dominate the state — the bet, as derived, is on BTCUSDT daily money-flow persistence, never on a price level, breakout, squeeze, calendar, or mean-reversion anchor. Unlike volume-gated price systems (ALMA-volume-gate, engulfing-volume), volume here is the signal itself, not a filter. The cost is symmetric: thin-volume chop that alternately satisfies the strict inequalities flips the full unit with no confirmation beyond the coded comparison, no cooldown, and no cost guard.

## Signal

Exact rule as pinned (`TrigLen = 13`, `FastX = 34`, `SlowX = 55` frozen — any other values are a different, unpinned rule):

- Declaration (derived): Pine v2 builtins (`ema`, `iff`, `nz`, `hlc3`, `barcolor`, `plot`, `hline`) with v2 `na` semantics observed. The `hline(0)` and both `plot(` calls render only and gate no order. All three inputs gate calculation.
- State (pinned, source-verbatim): `xTrend = iff(hlc3 > hlc3[1], volume * 100, -volume * 100)` (equal-sum bars take the distribution leg — coded, disclosed); `xFast = ema(xTrend, 34)`; `xSlow = ema(xTrend, 55)`; `xKVO = xFast - xSlow`; `xTrigger = ema(xKVO, 13)`; `pos = iff(xKVO > xTrigger, 1, iff(xKVO < xTrigger, -1, nz(pos[1], 0)))` with deterministic seed `0`. `pos` therefore takes values in `{1, -1}` after the first strict-inequality bar and holds through every equality bar.
- Orders (derived mapping, predeclared, FMZ-port-corroborated): the bar on which `pos` flips to `1` → enter long (closing any short in the same step, full reversal, no residual leg); the bar on which `pos` flips to `-1` → enter short (closing any long likewise). Bars where `pos` is unchanged — including every equality-hold bar — are explicit no-ops (pinned, not invented: the source state itself does not change there). Before the first flip the system is flat (`pos == 0` seed — no position by construction).
- The two flip legs are mutually exclusive on every bar by construction (they require opposite strict inequalities on the same pair), so no bar can ever fire both legs — no same-bar ordering ambiguity exists anywhere in this record.
- Risk legs (pinned absence, not invented): 0 `strategy.*` calls ship anywhere — the derived posture is explicitly no stop, no target, no trailing, no time exit. The FMZ port's prose optimization section suggests adding stops/trend filters as future work — explicitly NOT adopted here; adopting any of them would be a different, unpinned rule.
- Direction: two-sided long/short with symmetric reversal. Futures venue required for the short leg (researcher market choice — pinned).
- Display isolation: `barcolor` / `plot` / `hline` render only and cannot change any order.

## Required data

- Completed `1d` bars of BTCUSDT: `high`, `low`, `close` (via `hlc3` and `hlc3[1]` only) plus bar `volume` (sole volume read, inside `xTrend`). No `open`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request.*` / 0 `security(` anywhere; the FMZ port's displayed `basePeriod: 1h` carries no cross-timeframe indicator read in the verbatim logic and is not adopted).
- Single decision timeframe `1d` (researcher choice informed by the FMZ port's displayed `1d` backtest block — the canonical source names no timeframe; the page-chart quote is page chrome, never adopted). One evaluation per completed bar; all reads reference confirmed bars only.
- Warmup: Pine `ema` seeds on the first bar (no `na` propagation — disclosed: unlike ATR-100 constructions there is no warmup blindness trap here), but the 55-bar slow leg and the 13-bar trigger smoothing need stabilization bars, and the `pos` seed needs its first strict-inequality bar. The adopted warmup is the first 70 completed `1d` bars flat by record rule (55 slow-EMA stabilization + 13 trigger smoothing + 2 bars margin — predeclared researcher choice); no signal before bar 71 may trade. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice informed by the FMZ port's displayed `BTC_USDT` backtest block — the canonical source names no market; naming normalization is the only market step, and no source-market equivalence is claimed).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source declares no execution timing (indicator only); this record does not claim any source fill convention. No maker-touch, queue, or intrabar-path-dependent fill: with mutually exclusive flip legs and no stop/target legs, there is no same-bar ordering ambiguity of any kind.
- Sizing/capital/costs: the source ships no sizing, capital, fee, slippage, margin, or funding concept of any kind. The explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all) apply to the derived evaluation here, with the single-unit/no-add/reverse-full position pin from Signal, never presented as source-native behavior.
- Concurrency: at most one position (long or short) at any time; the opposite flip reverses in full in one step; re-entry after a reversal needs only the next opposite flip (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The short leg requires margin-short permission, realistic on the pinned perpetual venue.
- Volume semantics: the rule reads the traded venue's own per-bar candle volume number only; no assumption about spot-versus-perpetual versus equity volume semantics is pinned beyond that read — disclosed, not approximated.

## Evidence

### Source-reported

The page ships the full construction (41-line Pine v2 block: `study` not `strategy`, three calculation inputs at pinned defaults 13/34/55, the `hlc3`-comparison sign leg with the `volume * 100` / `-volume * 100` pair, the 34/55 EMA spread, the 13-bar trigger EMA, the sticky `pos` state machine with `nz(pos[1], 0)` seed, the red/green/blue bar coloring, zero-line `hline`, KVO/Trigger plots). The FMZ port corroborates direction semantics in prose (`上穿…做多,下穿时做空`) and displays a `BTC_USDT` / `1d` backtest block with matching `TrigLen` / `FastX` / `SlowX` params. The page ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.*` calls ship anywhere — the sole position-changing path is the opposite flip reversing the full unit. The absence of any stop is coded absence, disclosed, not a tunable parameter here.
2. Always-in-market exposure after arming, admitted plainly: after the first flip the system is never flat — a market that alternately satisfies the strict inequalities flips the full unit on every alternating flip with no confirmation beyond the coded comparison, no cooldown, and no cost guard. Adverse excursion between flips has no guardrail of any kind. This is the coded trade, disclosed, not a tunable parameter here.
3. Climax-volume dominance: because the full bar volume is signed by a strict `hlc3` comparison, one giant-volume bar with a marginal sum change injects its entire `±volume * 100` into the fast leg and can flip the state single-handedly — including equal-sum bars, which the code deterministically signs negative. The equal-sums false leg is source-verbatim simplification versus textbook dm/cm accounting, pinned, never repaired here.
4. Warmup flatness fenced: the first 70 bars are flat by record rule, so any textbook flip inside warmup is deliberately untraded — pinned, not recovered. Unlike ATR-based constructions there is no `na`-propagation blindness; the warmup here is stabilization-only, disclosed as a researcher choice.
5. Source basis fenced: the canonical source names no market or timeframe (the page-chart ES quote is chrome). The BTCUSDT-`1d` choice, same-bar-close fills, single-unit/no-add/reverse-full pin, 70-bar warmup, and house sizing/costs are researcher choices, disclosed (market/frame informed by the FMZ port's displayed backtest block, which is corroboration, not provenance for line-level facts); this record is therefore never evidence that any source-market deployment passes.
6. Derivation boundary fenced: the only non-source-native behaviors in this record are the state-to-order mapping, same-bar-close fills, the position-state pin, the adopted 70-bar warmup with record-rule pre-warmup flat, the BTCUSDT-`1d` market choice, and house sizing/costs — all predeclared above; the `xTrend` sign leg (including the equal-sums distribution leg), the 34/55/13 lengths, the `xKVO` spread, the sticky `pos` machine with equality hold and `0` seed, and the no-stop/no-target/no-cooldown posture are source-verbatim. This record is therefore never evidence that the original script itself passes.
7. The `13` / `34` / `55` literals, the strict-inequality flip pair with equality hold (not plain crossover, not touch, not level-hold), the full-unit reversal, the two-sided stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning any length, converting the sticky state into crossover calls, adding a stop/target/filter/cooldown/gate (including the FMZ prose's suggested stop-loss and MACD filter), dropping the short leg, honoring a `Trade reverse`-style direction flip, or sizing partially instead of full-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `TrigLen = 13` / `FastX = 34` / `SlowX = 55` / signed-volume spread / sticky trigger-flip pair / full-unit reversal / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Volume-force relevance: replacing the signed-volume `xTrend` with a price-only momentum input of matched smoothing (e.g. `close - close[1]` through the same 34/55/13 chain) must not improve net expectancy; fail ⇒ the volume read adds nothing over price-only momentum.
- F2 — Sticky-state relevance: replacing the equality-hold `pos` machine with plain strict-crossover entries/exits must not improve net expectancy; fail ⇒ the hold bars add nothing over crossover timing.
- F3 — Parameter relevance: replacing any pinned length (13, 34, 55) with an adjacent value must not improve net expectancy; fail ⇒ the pinned defaults carry no advantage over neighboring lookbacks and the record's literal choices are arbitrary.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision frame researcher-chosen `1d`; arithmetic over `hlc3` sums plus the venue's own candle volume with no venue-specific read). The construction ports across perpetual venues without structural change. The short leg requires margin-short permission (realistic on perpetual venues; a spot-only deployment cannot express the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Volume-magnitude comparability across venues is not claimed — the rule reads the traded venue's own candle volume only. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- State-to-order gap: the source is a pure bar-coloring indicator with zero order calls — every entry, reversal, and sizing behavior here is a researcher mapping, disclosed, not source-verbatim (direction semantics corroborated by the FMZ port's prose, which is not line-level provenance).
- Researcher market/frame: the canonical source names no market or timeframe — BTCUSDT `1d` is a researcher choice informed by the FMZ port's displayed backtest block; signal timing on other markets or frames would differ by construction.
- Derived fill timing: same-bar-close execution is a researcher choice over an indicator that declares no timing; backtest economics of other timings differ by construction — the adaptation is disclosed, not hidden.
- Position-state pin: same-side-add and reversal-quantity behavior has no source concept at all; the single-unit/no-add/reverse-full pin is a researcher choice, disclosed, not source-verbatim.
- No price stop, no time stop, never flat after arming: adverse excursion after entry has no guardrail beyond the opposite flip, which may arrive many bars later or after deep excursion; alternating flips whipsaw the full unit repeatedly. This is the coded posture, disclosed as the record's principal risk.
- No source cost declaration: no capital, commission, fee, slippage, margin, or funding assumption ships anywhere — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Warmup cost: the first 70 bars are flat by record rule, so any textbook flip inside warmup is deliberately untraded — pinned, not recovered.
- Equal-sums simplification: bars with unchanged `hlc3` sums are deterministically signed as distribution (`-volume * 100`) by the `iff` false leg — source-verbatim, pinned, and coarser than textbook dm/cm volume-force accounting, disclosed.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Klinger Volume Oscillator (KVO) Strategy [HPotter] canonical open-source script page (published 2017-08-29): https://www.tradingview.com/script/9iPwzLLR-Klinger-Volume-Oscillator-KVO-Strategy/
- FMZ corroborating port `流量主导型震荡量化策略` [ChaoZhang] (strategy 434301, created 2023-12-05; prose direction semantics and displayed BTC_USDT/1d backtest block only — full code login-gated, never cited for line-level facts): https://www.fmz.com/strategy/434301
