---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: HPotter PVO signal-cross volume-momentum reversal two-sided on BTCUSDT 1d bars
created: 2026-10-12
updated: 2026-10-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2017-09-27
sources:
  - https://www.tradingview.com/script/KIfPIMty-Percentage-Volume-Oscillator-PVO-Backtest/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# HPotter PVO signal-cross volume-momentum reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (canonical TradingView page, live browser read 2026-10-12):

- Canonical page: https://www.tradingview.com/script/KIfPIMty-Percentage-Volume-Oscillator-PVO-Backtest/ (title `Percentage Volume Oscillator (PVO) Backtest`, author `HPotter` WIZARD, `OPEN-SOURCE SCRIPT`, dated Sep 27 2017 — adopted as `source_as_of` 2017-09-27; like/follower/view counters are page chrome, never performance evidence).
- Full Pine v2 block read verbatim (40 lines, `//@version=2`, header `Copyright by HPotter v1.0 27/09/2017`): 1 `strategy(` / 2 `strategy.entry` (`"Long"` + `"Short"`) / 0 `strategy.close` / 0 `strategy.exit` / 0 `strategy.order` / 0 `strategy.cancel`. 4 `input(` declarations: `LengthShortEMA = input(12, minval=1)`, `LengthLongEMA = input(26, minval=1)`, `LengthSignalEMA = input(9, minval=1)`, `reverse = input(false, title="Trade reverse")` — all four gate calculation, zero display-only inputs. 3 `ema(` calls, 2 nested `iff(` pairs (the `pos` state leg and the `possig` direction leg), 1 `hline(` (zero line — display only), 1 `barcolor(`, 3 `plot(` (PVO / Signal / PVO Histo histogram — display only), 1 `nz(`, 0 `request.*`, 0 `security(`, 0 `time(`, 0 `open`, 0 `high`, 0 `low`, 0 `close` — the sole bar-series read anywhere in the file is `volume`.
- Order legs read verbatim: `if (possig == 1)` → `strategy.entry("Long", strategy.long)`; `if (possig == -1)` → `strategy.entry("Short", strategy.short)`. No exit call of any kind ships — every exit in this record is the opposite-side reversal entry, pinned, never supplemented.
- The header prose (tracked, never adopted as rules): PVO is a momentum oscillator for volume; typically a breakout or support break is validated when PVO is rising or positive; `You can change long to short in the Input Settings`; `WARNING: For purpose educate only / This script to change bars colors`. The page-chart quote (ES 1D CME) is page chrome — the script names no tradable market and no timeframe.
- No performance table, figure, or number ships anywhere on the page or in the code — this record claims no source-reported performance and no reproduced performance.

Licence and rights: the canonical page is a public open-source TradingView publication. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly six: (1) research market BTCUSDT Binance perpetual `1d` (the source names no market and no timeframe — the ES chart quote is chrome); (2) completed-bar decision with next-bar-open fills, adopting the source's own Pine default timing (`process_orders_on_close` unset, `calc_on_every_tick` unset — see Execution assumptions); (3) position-state pin — single-unit per side, full reversal on the opposite leg, no adds (the source passes no `pyramiding` argument, i.e. Pine default 0, and no sizing concept at all); (4) an adopted 50-bar warmup with pre-warmup bars flat by record rule (covers the 26-bar slow-EMA seeding plus the 9-bar signal seeding plus margin — see Required data); (5) `reverse = false` pinned at the source default (honoring a direction flip would be a different, unpinned rule); (6) house sizing/capital/costs replacing the wholly absent source economics (see Execution assumptions). The 12/26/9 lengths, the percentage-normalized volume-MACD formula, the inverted `pos` polarity (long fires on the weak leg — fenced below, never "corrected"), the sticky equality-hold state machine with `0` seed, and the no-stop/no-target/no-cooldown posture are source-verbatim.

Pre-write dedup (2026-10-12): working-tree case-insensitive searches for `percentage.volume`, `pvo`, `KIfPIMty`, `xPVOHisto`, `xSignalEMA`, `LengthSignalEMA` return zero strategy records using this source, author script, indicator, or mechanism — the only `volume` text anywhere is gates or other volume constructions (Klinger signed-volume spread, OBV cumulative, PVT, Chaikin, CMF, MFI, KVO trigger), never a percentage-normalized volume MACD. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closed PRs (100 reviewed by title) contain no PVO record; closed LazyBear WaveTrend work is a price-only oscillator cross — different construction, different data (zero volume read), different source. Closest pool records differ on all four axes: `macd-signal-cross-reversal-btcusdt-1d-2026-10-09.md` crosses a price-only MACD line against its signal (zero volume read anywhere); `klinger-volume-oscillator-trigger-flip-two-sided-btcusdt-1d-2026-10-10.md` builds its oscillator from signed `±volume * 100` force with 34/55/13 lengths and a sticky `pos` map where `1` means strong (opposite polarity to this record); `obv-ema-crossover-trend-two-sided-btcusdt-1d-2026-10-10.md` crosses a cumulative price-signed volume total against its EMA (no percentage normalization, no signal line of an oscillator). Four-axis distinction: signal construction differs (percentage-normalized volume MACD `(fast-slow)/slow*100` against its own 9-bar EMA — no pool record normalizes volume this way), trigger differs (inverted strict-inequality state pair with equality hold), data differs (pure-volume rule — zero price reads of any kind), and source identity differs (TV `KIfPIMty` HPotter 2017-09-27 versus other TV authors).

## Economic mechanism

### Source-reported

Volume-momentum state following on normalized participation: the 12-bar volume EMA minus the 26-bar volume EMA, expressed as a percentage of the slow leg, measures whether near-term participation runs hotter than its own baseline; its position against its 9-bar signal decides the bar color and the order leg. The author's tenets (quoted in-code): PVO defines the ups and downs of volume and rising/positive PVO validates breakouts — while the coded order map itself takes the contrarian side of that validation prose (long fires on the weak leg; fenced in Signal, never reconciled by invention).

### Research interpretation

Edge-triggered two-sided reversal system on normalized volume momentum, with no price level, band, stop, target, or confirmation leg beyond the single PVO-versus-signal comparison — long while `possig == 1`, short while `possig == -1`, changing only on strict-inequality flips, holding through equality bars. Unlike price-only signal-line crosses (MACD, KST, TRIX, TSI, PPO) where both lines derive from `close` smoothing, here both lines derive from `volume` smoothing alone: a high-volume bar with a flat price still moves the state, and a large price move on thin volume moves nothing — the bet, as derived, is on BTCUSDT daily participation persistence, never on a price level, breakout, squeeze, calendar, or mean-reversion anchor. Unlike cumulative volume systems (OBV, PVT), the percentage normalization makes the state scale-free across volume regimes. The cost is symmetric: thin-volume chop that alternately satisfies the strict inequalities flips the full unit with no confirmation beyond the coded comparison, no cooldown, and no cost guard.

## Signal

Exact rule as pinned (`LengthShortEMA = 12` / `LengthLongEMA = 26` / `LengthSignalEMA = 9` / `reverse = false` frozen — any other values are a different, unpinned rule):

- Declaration (derived): Pine v2 builtins (`ema`, `iff`, `nz`, `strategy.entry`, `barcolor`, `plot`, `hline`) with v2 `na` semantics observed. The `hline(0)` and all three `plot(` calls render only and gate no order. All four inputs gate calculation.
- Oscillator (pinned, source-verbatim): `xShortEMA = ema(volume, 12)`; `xLongEMA = ema(volume, 26)`; `xPVO = ((xShortEMA - xLongEMA) / xLongEMA) * 100`; `xSignalEMA = ema(xPVO, 9)`; `xPVOHisto = xPVO - xSignalEMA` (plotted only — the histogram gates no order).
- State (pinned, source-verbatim, polarity fenced): `pos = iff(xSignalEMA < xPVO, -1, iff(xSignalEMA > xPVO, 1, nz(pos[1], 0)))` with deterministic seed `0`; `possig = pos` under the pinned `reverse = false` (the `reverse` input's flip map is source code but pinning it `true` would be a different, unpinned rule — explicitly not admitted here). Net default-direction semantics, stated plainly and never corrected: `possig == 1` (LONG leg) holds exactly while `xPVO < xSignalEMA` — the weak/negative volume-momentum leg; `possig == -1` (SHORT leg) holds exactly while `xPVO > xSignalEMA` — the strong leg. Equality bars (`xPVO == xSignalEMA`) hold the prior `pos` via `nz(pos[1], 0)`; before the first strict-inequality bar the system is flat (`pos == 0` seed — no position by construction).
- Orders (source-verbatim legs): the bar on which `possig == 1` evaluates → `strategy.entry("Long", strategy.long)`; the bar on which `possig == -1` evaluates → `strategy.entry("Short", strategy.short)`. Bars where `possig` is unchanged — including every equality-hold bar — are explicit no-ops (pinned, not invented: the source state itself does not change there).
- The two order legs are mutually exclusive on every bar by construction (a single `possig` value feeds both `if`s, and the underlying strict inequalities are opposite) — no bar can ever fire both legs, so no same-bar ordering ambiguity exists anywhere in this record.
- Position and re-entry (pinned defaults): the `strategy(` call passes no `pyramiding` argument, i.e. Pine default 0 — same-side re-entry while positioned is rejected by the engine; the opposite entry reverses the full position in one step (Pine reversal semantics, no residual leg). No `strategy.close` / `strategy.exit` / `strategy.order` / `strategy.cancel` call ships anywhere, so the sole position-changing path is the opposite flip — exits are reversals, pinned. No cooldown, no missing rule.
- Risk legs (pinned absence, not invented): 0 exit/stop/target/trailing/time calls ship anywhere — the derived posture is explicitly no stop, no target, no trailing, no time exit.
- Direction: two-sided long/short with symmetric reversal. Futures venue required for the short leg (researcher market choice — pinned).
- Degenerate-input behavior (pinned, edge-case-explicit): if `xLongEMA == 0` the division yields `na`, and any `na` comparison is false, so `pos` holds its prior value (no-op bar — disclosed, not repaired). BTCUSDT `1d` candle volume is never zero in practice, so this leg is a fenced guard, never a live path. `ponytail:` no approximation is made for zero-volume bars beyond the coded hold.
- Display isolation: `barcolor` / `plot` / `hline` render only and cannot change any order.

## Required data

- Completed `1d` bars of BTCUSDT: bar `volume` ONLY — the sole series read by any order-gating line. No `open`, `high`, `low`, `close`, funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read anywhere. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request.*` / 0 `security(` anywhere).
- Single decision timeframe `1d` (researcher choice — the source names no timeframe; the page-chart ES quote is chrome). One evaluation per completed bar; all reads reference confirmed bars only.
- Warmup: Pine `ema` seeds each leg with an SMA over its first `length` bars and yields `na` before that, so `xLongEMA` is first defined on the 26th bar and `xSignalEMA` (9-bar EMA over `xPVO`, itself `na` until bar 26) on the 34th bar; every `na` comparison holds `pos` at its seed. The adopted warmup is the first 50 completed `1d` bars flat by record rule (34-bar first-definable signal + 16 bars stabilization margin — predeclared researcher choice); no signal before bar 51 may trade. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; naming normalization is the only market step, and no source-market equivalence is claimed).
- Order timing (source-default timing, adopted as-is, disclosed): the source sets neither `process_orders_on_close` nor `calc_on_every_tick`, i.e. Pine v2 defaults — the signal is decided on the completed bar and filled at the next bar's open. This record adopts exactly that convention (completed-bar decision, next-bar-open fill), compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`); no same-bar-close conversion is performed and none is claimed. No maker-touch, queue, or intrabar-path-dependent fill: with mutually exclusive order legs and no stop/target legs, there is no same-bar ordering ambiguity of any kind.
- Sizing/capital/costs: the source ships no sizing, capital, fee, slippage, margin, or funding concept of any kind. The explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all) apply to the derived evaluation here, with the single-unit/no-add/reverse-full position pin from Signal, never presented as source-native behavior.
- Concurrency: at most one position (long or short) at any time; the opposite flip reverses in full in one step; re-entry after a reversal needs only the next opposite flip (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The short leg requires margin-short permission, realistic on the pinned perpetual venue.
- Volume semantics: the rule reads the traded venue's own per-bar candle volume number only; no assumption about spot-versus-perpetual versus equity volume semantics is pinned beyond that read — disclosed, not approximated.

## Evidence

### Source-reported

The page ships the full construction (40-line Pine v2 block: `strategy` with two entry ids at pinned defaults 12/26/9 plus `reverse = false`, the percentage-normalized volume-MACD formula, the inverted strict-inequality `pos` pair with equality hold and `nz(pos[1], 0)` seed, the `possig` direction map, the Long/Short entry pair, the red/green/blue bar coloring, the zero-line `hline`, and the PVO/Signal/Histo plots). The page ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.close` / `strategy.exit` / `strategy.order` / `strategy.cancel` calls ship anywhere — the sole position-changing path is the opposite entry reversing the full unit. The absence of any stop is coded absence, disclosed, not a tunable parameter here.
2. Inverted polarity admitted plainly: with the pinned `reverse = false`, the LONG leg holds while volume momentum is weak (`xPVO < xSignalEMA`) and the SHORT leg while it is strong — the coded map fades the author's own "rising/positive PVO validates breakouts" prose. This inversion is source-verbatim, pinned, and never repaired or re-signed here; flipping `reverse` to `true` would be a different, unpinned rule.
3. Always-in-market exposure after arming, admitted plainly: after the first flip the system is never flat — a market that alternately satisfies the strict inequalities flips the full unit on every alternating flip with no confirmation beyond the coded comparison, no cooldown, and no cost guard. Adverse excursion between flips has no guardrail of any kind. This is the coded trade, disclosed, not a tunable parameter here.
4. Pure-volume blindness: zero price reads of any kind — a vertical price collapse on thin volume cannot move the state, and a sideways market with oscillating volume flips the full unit. Disclosed as the record's principal model risk.
5. Warmup flatness fenced: the first 50 bars are flat by record rule, so any textbook flip inside warmup is deliberately untraded — pinned, not recovered.
6. Source basis fenced: the source names no market or timeframe (the page-chart ES quote is chrome). The BTCUSDT-`1d` choice, next-bar-open fills, single-unit/no-add/reverse-full pin, 50-bar warmup, and house sizing/costs are researcher choices, disclosed; this record is therefore never evidence that any source-market deployment passes.
7. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT-`1d` market choice, the next-bar-open fill adoption, the position-state pin, the adopted 50-bar warmup with record-rule pre-warmup flat, the `reverse = false` pin, and house sizing/costs — all predeclared above; the 12/26/9 lengths, the percentage-normalized formula, the inverted `pos` polarity with equality hold and `0` seed, the Long/Short entry pair, and the no-stop/no-target/no-cooldown posture are source-verbatim. This record is therefore never evidence that the original script itself passes.
8. The `12` / `26` / `9` literals, the inverted strict-inequality flip pair with equality hold (not plain crossover, not touch, not level-hold, not re-signed to MACD convention), the full-unit reversal, the two-sided stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning any length, re-signing the polarity, converting the sticky state into crossover calls, adding a stop/target/filter/cooldown/gate, dropping the short leg, honoring `reverse = true`, or sizing partially instead of full-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `12` / `26` / `9` / inverted sticky flip pair / full-unit reversal / two-sided / `1d` BTCUSDT / next-bar-open fills are frozen.

- F1 — Volume relevance: replacing the `volume` input with `close` through the identical (12, 26, 9) chain and inverted flip pair (i.e. a re-signed PPO) must not improve net expectancy; fail ⇒ the volume read adds nothing over price-only momentum.
- F2 — Normalization relevance: replacing the percentage normalization with the raw spread (`xShortEMA - xLongEMA`) against its own 9-bar EMA must not improve net expectancy; fail ⇒ the normalization adds nothing over a raw volume-MACD spread.
- F3 — Parameter relevance: replacing any pinned length (12, 26, 9) with an adjacent value must not improve net expectancy; fail ⇒ the pinned defaults carry no advantage over neighboring lookbacks and the record's literal choices are arbitrary.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision frame researcher-chosen `1d`; arithmetic over the venue's own candle volume with no venue-specific read and zero price reads). The construction ports across perpetual venues without structural change. The short leg requires margin-short permission (realistic on perpetual venues; a spot-only deployment cannot express the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Volume-magnitude comparability across venues is not claimed — the rule reads the traded venue's own candle volume only. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Researcher market/frame: the source names no market or timeframe — BTCUSDT `1d` is a researcher choice; signal timing on other markets or frames would differ by construction.
- Adopted fill timing: next-bar-open execution follows the source's own Pine defaults, but the source never states a fill convention in prose — backtest economics of other timings differ by construction; the adoption is disclosed, not hidden.
- Position-state pin: same-side-add and reversal-quantity behavior has no source concept beyond the default `pyramiding = 0`; the single-unit/no-add/reverse-full pin is a researcher choice, disclosed, not source-verbatim.
- No price stop, no time stop, never flat after arming: adverse excursion after entry has no guardrail beyond the opposite flip, which may arrive many bars later or after deep excursion; alternating flips whipsaw the full unit repeatedly. This is the coded posture, disclosed as a principal risk alongside pure-volume blindness.
- No source cost declaration: no capital, commission, fee, slippage, margin, or funding assumption ships anywhere — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Warmup cost: the first 50 bars are flat by record rule, so any textbook flip inside warmup is deliberately untraded — pinned, not recovered.
- Zero-volume guard: a zero slow-EMA bar yields `na` and holds state by Pine semantics — fenced, never a live path on BTCUSDT `1d`, disclosed.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Percentage Volume Oscillator (PVO) Backtest [HPotter] canonical open-source script page (published 2017-09-27): https://www.tradingview.com/script/KIfPIMty-Percentage-Volume-Oscillator-PVO-Backtest/
