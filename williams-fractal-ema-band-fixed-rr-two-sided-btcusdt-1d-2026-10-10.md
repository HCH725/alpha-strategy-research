---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Williams Fractals EMA20/50-band fixed-R:R reversal two-sided on BTCUSDT 1d bars
created: 2026-10-10
updated: 2026-10-10
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-09-02
sources:
  - https://github.com/hasnocool/tradingview-pine-scripts/blob/main/5min%20Williams%20Fractals%20scalping%20(3commas).pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Williams Fractals EMA20/50-band fixed-R:R reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (raw file fetched over HTTPS during this cycle, 15749 chars):

- Repository: https://github.com/hasnocool/tradingview-pine-scripts — file `5min Williams Fractals scalping (3commas).pine` (root-level, blob SHA `5490e2ba8e980fdaae3b83e42d29d69bff13f01d`), sole file-touching commit `e031cab2819a7d56fb8bb9d000252f51439986e2` (`Initial Upload Of Data`, committer `hasnocool`, `2023-09-02T22:07:34Z` — adopted as `source_as_of`). The header block names author `Zippy111` and states the lineage: inspired by the MoneyZG YouTube strategy `Easy 5 Minute Scalping Strategy`, one-order-per-trade, Williams-Fractals signals, 3Commas-bot compatible.
- Text census over the pinned Pine v5 block: 1 `strategy(` (`5min Williams Fractals scalping (3commas)`, no `pyramiding=` → default `0` governs, no `process_orders_on_close` → Pine default governs, recorded as source-declared-by-default) / 2 `strategy.entry` (`LONG open` long, `SHORT open` short) / 2 `strategy.exit` (`Long close` limit+stop, `Short close` limit+stop) / 0 `strategy.close` / 0 `strategy.order` / 1 `strategy.risk.allow_entry_in` (`i_chkLong and i_chkShort ? all`, both checkboxes default `true` → two-sided by default) / `i_wf` Periods defval `2` (minval 2) with `i_wfBarsBack` default `true` (evaluate the WF bar, not the current bar) / EMA fast `20` / EMA slow `50` / `i_longProfitPerc` and `i_shortProfitPerc` defval `1.5` (minval 1.1, tooltip `Times the Stop Loss which is always the current Ema slow value`) / `i_tradeDontClose` defval `0` (exits armed from the entry bar) / date filter `01 Jan 2020` → `1 Jan 2099` (full-history by default) / EMA-gap filter default `false` / RSI filter default `false` (length 14, long band 0–70, short band 30–100, direction confirmation `false`) / pullback filter default `false` / 3Commas comments default `false` (bot IDs and email token empty by default — no external routing in the pinned spec).
- Full order legs read verbatim: long entry gated on `c_longCondition and strategy.opentrades == 0`, sets `c_longStopPrice := c_emaSlow`, `c_longExitPrice := close + ((close - c_emaSlow) * i_longProfitPerc)`; exit leg `strategy.exit("Long close", from_entry="LONG open", limit=c_longExitPrice, stop=c_longStopPrice)` armed whenever `ta.barssince(strategy.opentrades == 0) >= i_tradeDontClose` (= 0, always true). Short legs are the exact mirror (`c_shortStopPrice := c_emaSlow`, `c_shortExitPrice := close - ((c_emaSlow - close) * i_shortProfitPerc)`).
- Page performance language is absent entirely (the file ends in a custom backtester-table plot routine with only starting-balance/risk inputs, no reported return, win rate, profit factor, or trade count) — this record claims no source-reported performance and no reproduced performance.

Licence and rights: the repository ships no licence file; this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly five: (1) research market/timeframe BTCUSDT `1d` single-frame (the script names a `5min` scalping context with no timeframe input — timeframe is a chart setting, not a coded rule — so the port keeps every coded literal while changing only the evaluation frame); (2) same-bar-close fills on completed-bar decisions (the Pine block ships no `process_orders_on_close`, so its default timing is next-bar-open — this record does not claim source timing); (3) an adopted 100-bar warmup with pre-warmup bars flat by record rule (the EMA-50 leg needs 50 settled closes; 100 covers seeding plus the fractal-confirmation transient with margin — see Required data); (4) house sizing/capital/costs replacing the block's default full-equity order sizing (see Execution assumptions; the Pine no-pyramiding default and the `opentrades == 0` flat-only entry rule are preserved as the single-position book); (5) historical closed-bar indexing semantics for the `barstate.isrealtime ? 1 : 0` legs (on historical bars the block reads `close[0]`/current-bar values; the `1`-bar realtime offset is a live-trading anti-repaint artifact with no backtest meaning and is pinned out of this spec). Fractal formula shape, n = 2, the WF-bar lag evaluation, EMA 20/50 literals, the between-the-EMAs band conditions, the bull/bear alignment predicates, both entry IDs, the EMA-slow stop leg, the 1.5× fixed-R:R limit legs, the always-armed exit posture, the no-pyramiding single-position rule, two-sided direction, and every filter-OFF exclusion are source-native and unmodified.

Pre-write dedup (2026-10-10): working-tree case-insensitive searches for `fractal` return zero dedicated Williams-fractal strategy records (the only pool mention is an unrelated substring hit); `williams-fractal`, `wf scalp`, `hasnocool`, and `Zippy111` return zero titles and zero bodies. The pool's `ema-20-50-cross` record is a pure fast/slow cross system with no fractal leg and no fixed-R:R exit rail — a different signal and a different risk book. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Five-axis distinction: mechanism differs (confirmed fractal pivot + between-the-EMAs band fade with a fixed 1.5R bracket — no pool or queue record combines a 5-bar fractal pivot with an EMA-band location condition), signal construction differs (lag-2 pivot confirmation plus band containment plus EMA alignment, versus raw crosses, channel breaks, or oscillator thresholds), exits differ (resting stop-at-slow-EMA plus limit-at-1.5R OCO pair with no trailing, no time stop, and no opposite-signal exit — no pool record shares this exact risk posture), source identity differs (hasnocool/Zippy111 GitHub Pine, Sep-2023, versus other GitHub repos, FMZ IDs, or TV authors), and direction handling differs (two-sided single-position fade book, flat whenever no pivot-band setup prints, versus always-in-market reversal books and long-only holders).

## Economic mechanism

### Source-reported

Fractal-pivot reversal fade inside a slow-trend band (mirror description: Williams-Fractals signals on a 5-minute scalping chart, one order per trade): a freshly confirmed down-fractal (local low pivot) firing while price sits between the fast and slow EMAs in bull alignment is bought as a corrective-low entry; the EMA-slow line is the hard stop and 1.5× that distance is the fixed target, so each trade risks a band-break for a bounded snap-back. The header claims the fractal marks the turning point and the EMA band keeps entries out of choppy non-trend regions.

### Research interpretation

Location-gated pivot fade with a hard bracket, two-sided. Unlike the pool's pure EMA-cross record (which buys alignment itself and rides it), this system never buys alignment — it buys a confirmed local extreme *against* the last two bars' drift but *inside* slow-trend permission: a down-fractal pivot two bars back with the pivot-bar close below EMA20 yet above EMA50, while EMA20 still holds above EMA50, is the whole long thesis. Unlike channel-breakout holders (Donchian/Dual-Thrust/Darvas in pool) it fades the fresh extreme rather than chasing it, and unlike oscillator fades (Connors-RSI2, RSI-MA) it reads no normalized momentum at all — only pivot geometry plus two moving averages. Unlike trailing-stop riders (SuperTrend/Chandelier/UT-Bot/PSAR in pool and queue) the exit never follows price: stop and limit rest from the entry bar and the trade is binary — bracket resolved or nothing. The bet is on multi-bar snap-back completion inside an intact slow trend at the daily scale, not on breakout persistence, momentum normalization, or trend riding.

## Signal

Exact rule as pinned (n = 2, EMA 20/50, R:R 1.5/1.5, strict edges — any other value is a different, unpinned rule):

- Fractals (pinned shape, evaluated at lag `i_wf = 2` with `i_wfBarsBack = true`): at decision bar `t`, the pivot candidate is bar `t-2`. Up-fractal `c_upFractal[t]` = `high[t-2]` strictly greater than `high[t-1]`, `high[t]` (down-frontier) and strictly greater than the pre-pivot pair `high[t-3]`, `high[t-4]` under the frontier-0 arm, with arms 1–4 admitting defined equal-high pre-pivot shapes (the coded `<=`-with-strict-tail variants) — the block's five-arm OR as written, no arm added or removed. Down-fractal `c_downFractal[t]` is the exact low-side mirror. Confirmation completes on bar `t`'s close using bars `≤ t` only — no future reference.
- EMA legs (pinned literals, closed-bar semantics): `emaFast = ta.ema(close, 20)`, `emaSlow = ta.ema(close, 50)`; `bull = emaFast[t] >= emaSlow[t]`; `bear = emaFast[t] < emaSlow[t]`.
- Entry long: `c_downFractal[t]` AND `close[t-2] < emaFast[t-2]` AND `close[t-2] > emaSlow[t-2]` AND `bull[t]` AND flat (`strategy.opentrades == 0`) AND date filter open → buy-open long at the same-bar close under the derived declaration.
- Entry short: `c_upFractal[t]` AND `close[t-2] > emaFast[t-2]` AND `close[t-2] < emaSlow[t-2]` AND `bear[t]` AND flat AND date filter open → sell-open short at the same-bar close.
- Bracket (pinned legs, set from the entry bar): long `stop = emaSlow[entry]`, `limit = close[entry] + (close[entry] - emaSlow[entry]) * 1.5`; short `stop = emaSlow[entry]`, `limit = close[entry] - (emaSlow[entry] - close[entry]) * 1.5`. The OCO pair rests from the entry bar (`i_tradeDontClose = 0`, always armed); first touch closes the full unit. Same-bar stop/limit ambiguity is resolved stop-first (the conservative Pine same-bar precedence, pinned as the record rule).
- Risk legs (pinned absences, not invented): no trailing, no time exit, no opposite-signal exit (contra-side setups while positioned are ignored by the `opentrades == 0` gate — the book waits for bracket resolution, never flips), no second unit (Pine default no-pyramiding preserved).
- Direction: two-sided single-position fade book — long, short, or flat; flat whenever no setup prints or between bracket resolution and the next setup. No side is disabled (`allow_entry_in = all` by default).
- Filter isolation (pinned OFF, gated from no order): EMA-gap (`false`), RSI filter (`false`, length 14 with its bands and direction check inert), pullback filter (`false` — the `ZenLibrary` import feeds only this OFF branch and gates no order), 3Commas comments (`false`, IDs/tokens empty). Display/plumbing isolation: the `plot`/`plotshape` legs (fractal markers offset `-i_wf` render only) and the backtester-table routine gate no order.

## Required data

- Completed `1d` bars of BTCUSDT: `high`/`low` (fractal pivot geometry only), `close` (pivot-bar band containment, EMA inputs, limit arithmetic), `open` unused by any order-gating line. No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, higher-timeframe, or cross-venue state is read by any order-gating line (the RSI `request.security` leg is inert under the pinned filter-OFF config and reads the same frame's close in any case).
- Single decision timeframe `1d` (declared research frame per the derivation; the script's `5min` naming is chart context, not a coded rule — there is no timeframe input to supersede).
- Warmup: the EMA-50 leg needs 50 settled closes and the lag-2 fractal needs 2 confirmation bars; the adopted warmup is the first 100 completed `1d` bars flat by record rule (predeclared researcher choice — 2× the structural length, covering EMA seeding plus the early-fractal transient with margin). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar; the realtime `close[1]` branch is pinned out (see derivation 5).

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (declared port; the source venue context is 3Commas-routed crypto scalping with no pinned venue layout — no cross-venue equivalence claimed beyond the perpetual-venue family).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close market entries and a resting stop+limit OCO pair from the entry bar, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar-open by Pine default; this record does not claim source fills. No maker-touch, queue, or intrabar-path-dependent fill beyond first-touch bracket resolution with the pinned stop-first same-bar rule. The short leg requires margin-short permission, realistic on the pinned perpetual venue.
- Sizing/capital/costs: the block's default full-equity order sizing ships no portable economics — the explicit house overlay (Base 6% + Safety 6% + Safety 6% capital framing, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) replace it here, never presented as source-native behavior. No safety-order layering is admitted: entries while positioned are blocked by code, so any DCA add would change trade events and would be a different, unpinned strategy.
- Concurrency: at most one position (long or short) at any time; bracket resolution is the sole closer; re-entry on the next setup after resolution with no cooldown specified — explicitly none, not invented. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (strategy header with author/lineage note, direction checkboxes, date filter, both R:R inputs with 1.5 defaults, `tradeDontClose` 0, WF Periods 2 with WF-bar evaluation, EMA 20/50 inputs with gap filter OFF, RSI block OFF, pullback block OFF, 3Commas block OFF, the five-arm fractal loops both sides, the band-plus-alignment conditions, both entry IDs gated on flat, both stop/limit exit legs with the EMA-slow stop and 1.5× limit arithmetic). It ships zero performance numbers: no return, no win rate, no profit factor, no trade count — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Fade-into-breakdown, admitted plainly: a down-fractal inside bull alignment can print days before the slow trend actually breaks — the long then rides the full distance to the EMA-slow stop with no early-abort leg, and a gap through the stop resolves at the record's stop-first rule with slippage uncapped by any coded guard.
2. Zero-distance bracket edge, admitted plainly: an entry bar printing `close == emaSlow` (near-impossible on `1d` BTCUSDT outside a venue outage, but structurally reachable) sets stop == entry and limit == entry — the OCO collapses to a flat scratch by rule. Structural, disclosed, unfenced by the source.
3. Bracket-or-nothing rigidity, admitted plainly: winners cap at exactly 1.5R with no trailer and no partial — a trend day that runs 10R keeps 1.5R; losers always pay the full band distance. This is the coded posture, disclosed, not a tunable parameter here.
4. Setup drought, admitted plainly: the conjunction (fresh pivot + pivot-bar band containment + current-bar alignment + flat book) fires infrequently on `1d` bars, and the flat-only gate means a second setup printing mid-trade is discarded unseen — long idle stretches and skipped signals are the coded trade, disclosed, not smoothed.
5. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT-`1d` single research frame, same-bar-close fills, the adopted 100-bar warmup with record-rule pre-warmup flat, house sizing/costs, and historical closed-bar indexing — all predeclared above; n = 2, the five-arm fractal shape, WF-bar lag evaluation, EMA 20/50, the band-containment and alignment predicates, both entry IDs, the EMA-slow stop, the 1.5× limit arithmetic, always-armed exits, the flat-only single-position book, two-sided direction, and every filter-OFF exclusion are source-verbatim. This record is therefore never evidence that the original 5-minute chart deployment passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: n = 2 / EMA 20/50 / band containment / alignment predicates / lag-2 evaluation / stop-at-slow-EMA / 1.5× limits / stop-first OCO / flat-only single position / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Fractal relevance: replacing the fractal-pivot gate with any-bar band entries (long whenever `close < emaFast` and `close > emaSlow` with bull alignment while flat, same bracket) must not improve net expectancy; fail ⇒ the pivot-confirmation leg adds nothing over the band alone.
- F2 — Bracket relevance: replacing the 1.5R fixed bracket with opposite-fractal exits (hold each unit until the contra-side fractal confirms, same entries) must not improve net expectancy; fail ⇒ the fixed-R:R risk book adds nothing over pivot-to-pivot holding.
- F3 — Band relevance: dropping the pivot-bar band-containment legs (any confirmed fractal with current-bar alignment fires, same bracket) must not improve net expectancy; fail ⇒ the between-the-EMAs location condition adds nothing over raw fractal fading.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (declared port of a crypto-scalping source context). The OHLC/EMA arithmetic ports across perpetual venues without structural change; both sides are explicit legs, so a spot-only deployment expresses the long half unchanged while the short half stays venue-gated (short permission unused, never silently converted). No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read, so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived frame and fill timing: the source names a 5-minute scalping chart and fills next-bar-open by Pine default; this record evaluates `1d` bars and executes same-bar-close. Backtest economics of the two framings and timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source configuration's performance.
- No source cost declaration of any usable kind: no fee, slippage, or funding assumption ships anywhere — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Single-position bottleneck: the flat-only gate discards overlapping setups and the bracket-or-nothing book caps every winner at 1.5R — missed signals and capped runners are the coded trade, disclosed, not smoothed.
- Scale selectivity: the pivot-plus-band conjunction on `1d` bars describes multi-day snap-back geometry, so the system fires infrequently and spends long stretches flat or riding to the bracket — long idle/bracket-resolution stretches are the coded trade, disclosed, not smoothed.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- GitHub canonical source file (commit e031cab2819a7d56fb8bb9d000252f51439986e2, 2023-09-02; blob 5490e2ba8e980fdaae3b83e42d29d69bff13f01d): https://github.com/hasnocool/tradingview-pine-scripts/blob/main/5min%20Williams%20Fractals%20scalping%20(3commas).pine
