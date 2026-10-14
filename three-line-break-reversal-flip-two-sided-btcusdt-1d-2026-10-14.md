---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Three-Line-Break N=3 reversal flip two-sided on BTCUSDT 1d bars
created: 2026-10-14
updated: 2026-10-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-14
sources:
  - https://help.tradestation.com/09_01/tradestationhelp/charting/linebreak_chart.htm
  - https://www.tradingview.com/support/solutions/43000502273-introduction-to-line-break-charts/
  - https://github.com/EarnForex/Three-Line-Break/blob/efe1adda175f1bbec5372b329368457095fd6a67/ThreeLineBreak.mq4
  - https://www.tradinformed.com/how-to-trade-3-line-break-charts-profitably/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Three-Line-Break N=3 reversal flip two-sided on BTCUSDT 1d bars

## Provenance

Primary sources read end to end (all four fetched live over HTTPS during this cycle):

- Construction + trading-interpretation artifact: TradeStation official Help, `Line Break Chart` (`help.tradestation.com/09_01/tradestationhelp/charting/linebreak_chart.htm`, 9,128 bytes as fetched) — full build rules, the `Line Breaks = 3` trading interpretation, and the back-test/automation note, all quoted verbatim below.
- Construction artifact: TradingView official Help Center, `Introduction to line break charts` (solution `43000502273`, fetched live 2026-10-14) — Japanese chart-type definition, typical `Number of lines = 3`, and the three-outcomes-per-close calculation method, quoted below.
- Algorithm artifact: `EarnForex/Three-Line-Break`, file `ThreeLineBreak.mq4` at pinned commit `efe1adda175f1bbec5372b329368457095fd6a67` (commit message `1.00`, committed 2025-04-07, 17,740 bytes as fetched via the pinned raw URL) — exact seeding, continuation, and reversal branch logic with strict edges, quoted below. The file carries `Copyright 2025, EarnForex.com`. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.
- Performance-context artifact: Tradinformed, `How To Trade 3 Line Break Charts Profitably` (fetched live 2026-10-14, 245,728 bytes) — EUR/USD-only Excel backtest with full rule/filter disclosure and a printed results table, cited under Source-reported with exact sample provenance; it is never crypto evidence and never this record's rule.

Pinned rule content (all three rule sources agree; verbatim quotes):

- TradeStation build (verbatim): `A new 'Up Line' is added if the Close of the current bar is greater than the high of the previous 'Up Line'.` / `A downward reversal occurs only if the Close of the current bar is less than the Lows of the specified number of prior Line Break lines.` / `An upward reversal occurs only if the Close of the current bar is greater than the Highs of the specified number of prior Line Break lines.` / `A new 'Down Line' is added if the Close of the current bar is less than the low of the previous 'Down Line'.` / `If there is no new high or low, no line is added.`
- TradeStation trading interpretation, headed `Trading Interpretation (when Line Break = 3)` (verbatim): `Buy when an Up Line emerges after three or more consecutive Down Lines.` / `Sell when a Down Line emerges after three or more consecutive Up Lines.` / `Avoid trading in "trendless" markets, where the Up Lines and Down Lines alternate.`
- TradeStation automation note (verbatim): `Strategies can be effectively back-tested and automated on Line Break charts, only when the applied strategy uses "on Close" orders (ex. Buy this bar on Close).` This record uses the strictly more conservative next-bar-open fill (predeclared derivation, never implied — see Execution assumptions).
- TradingView construction (verbatim): `The typical "Number of lines" setting is 3, which means that the chart forms a new up line only when the closing price is above the high prices of the last three lines, and forms a new down line when the closing price is below the past three lines' low prices.` / `If the current closing price is the same or the move in the opposite direction is not large enough to warn about a potential reversal, then no new line is drawn.` / `Each new closing price has three possible outcomes — New line, same color: When price extends in the same direction. New line, different color: When the price change is large enough to warrant a reversal. No new line: When price does not change or the reversal is not large enough to warrant a new line.`
- Pinned MQL seeding/edges (verbatim branch predicates from the fetched file at `efe1adda`): first-bar seeding `Close_prev = Close_new`; pre-first-line `if (Close_new > Close_prev) DrawBullishCandle / else if (Close_new < Close_prev) DrawBearishCandle` (strict — equality draws nothing); reversal window `int bars_to_check = (int)MathMin(LinesToBreak, TLB_N)` with the comment `Could be fewer than 3 (or LinesToBreak) bars in total right now`; reversal scope `No High/Low, hence consider both Open and Close` over the window's line opens and closes (`lowest_low`/`highest_high`); up-reversal `if ((CandleBufferC[0] < CandleBufferO[0]) && (Close_new > highest_high))` (strict); down-reversal `else if ((CandleBufferC[0] > CandleBufferO[0]) && (Close_new < lowest_low))` (strict); continuation-up `else if ((CandleBufferC[0] > CandleBufferO[0]) && (Close_new > Close_prev))` and continuation-down `else if ((CandleBufferC[0] < CandleBufferO[0]) && (Close_new < Close_prev))` (both strict against the prior line close); anything else appends no line. One completed bar produces at most one new line by construction.
- Tradinformed rule disclosure (verbatim): `My entry rules are simple enter a new trade on a new reversal line. In my backtest I did not test the effect of stop-losses, trailing stops or profit targets. I also did not filter trade entries by time of day.` Sample pin (verbatim): `I carried out my test on the EUR/USD forex pair on the 4-hour timeframe between December 2009 and June 2015.` Optional-filter pin (verbatim): `I tested using a 200 period EMA as an optional filter` with `When the filter was active I only traded long when the price was above the 200 EMA and only traded short below.` The 200-EMA filter, any stop/target/trailing, and any time-of-day filter are fenced as not adopted here — adopting any of them would be a different, unpinned rule.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the pinned N=3 Three-Line-Break reversal interpretation wired into a two-sided flip book on one crypto asset — not a lossless reproduction of any source deployment (no source trades BTCUSDT, ships fills, sizing, costs, or a venue). Researcher-declared adaptations are exactly six: (1) research market/timeframe BTCUSDT `1d` single-frame (all three rule sources are timeframe-agnostic close logic — the daily grid is the declared deployment, never implied); (2) bar-close decision with next-bar-open market fills (TradeStation's own automation note blesses on-Close orders; the sequential next-open fill is the declared, strictly more conservative port, never implied); (3) an adopted 30-bar warmup with pre-warmup bars flat by record rule (the sources pin no warmup — seeding starts at the oldest bar by code, so the warmup is the declared margin over the structural need, see Required data); (4) house sizing/capital/costs replacing the sources' complete absence of economics (the single-unit, never-add posture is the declared port of one-event-per-bar); (5) the flip-only book with researcher-declared no-stop/no-target/no-trailing/no-time-exit posture (TradeStation's interpretation and the Tradinformed test both ship no risk leg — the sole position-changing paths are qualified contra-reversals, predeclared here); (6) two-sided direction mapping with the short leg explicit (`Buy` targets long, `Sell` targets short — the Tradinformed test trades both sides; the perpetual short is the declared port of `Sell`, realistic on the pinned venue). The N=3 break count, strict reversal/continuation edges, seeding, three-outcomes-per-close, 3+-line qualification gate, alternation fence, pre-first-signal flat state, and every exclusion are source-native and unmodified.

Pre-write dedup (2026-10-14): working-tree case-insensitive searches for `line-break`, `linebreak`, `line break chart`, `kagi`, `renko`, `point.figure`, `point-and-figure`, `three.line`, `three line` return zero strategy records built on line-break/Kagi/Renko/point-and-figure construction (the only prose hits are `three lines: +DI/-DI/ADX` inside the DMI record, `the first three lines` of a Pine declaration inside the Williams-%R record, the Alligator's `three lines` of Jaw/Teeth/Lips, `trendline-break` prose inside the Special-K record, and `reclaim`-adjacent hyphenation — none is a line-break chart system). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI breakout long), #63 (SuperTrend ATR-flip long), #89 (Chandelier Exit stop-flip long), #92 (SSL channel reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records differ on every axis: `three-down-three-up-consec-close-long-btcusdt-1h-2026-10-07.md` buys three consecutive lower closes as a long-only fade and exits to flat on three higher closes (bare close-vs-prior-close chains over a fixed 3-bar window, `1h`, FMZ Pine v6 source, same-bar-close fills, long-only, flat-book); `three-white-soldiers-black-crows-flip-two-sided-btcusdt-1d-2026-10-14.md` fires on TA-Lib three-candle body/open/shadow predicates against trailing averages (fixed 3-bar geometry with-trend continuation, no run-length gate, every triple tradable). Five-axis distinction: mechanism differs (variable-span line-extreme break gated on 3+-line runs with an alternation fence, versus fixed-window candle geometry or naked close chains); signal construction differs (confirmed-line highs/lows over runs of confirmed lines, versus real-body/shadow averages or close chains); entries differ (only reversals that follow 3+ consecutive opposite lines; sub-3-line reversals are explicit no-ops); exits differ (qualified contra-reversal flip-only book); source identity differs (TradeStation official help + TradingView official chart docs + pinned EarnForex MQL versus TA-Lib C detectors versus FMZ Pine v6).

## Economic mechanism

### Source-reported

Noise-filtered reversal speculation from Japan (mirror TradeStation/TradingView titles): because a new line prints only when the close breaks the range covered by prior lines, chop that never exceeds the last three lines' extremes leaves no mark on the chart at all. TradeStation's interpretation converts that filtered chart into a two-action system — `Buy` the up-reversal that ends a 3+-line decline, `Sell` the down-reversal that ends a 3+-line advance — and fences alternation as `trendless` non-trading state. TradingView frames the same object as support/resistance and breakout revelation (`Breakouts: Occur when bars begin to generate in a defined direction after a period of trading within a support and resistance bound trading range`). Tradinformed's thesis sentence, kept as description: 3-line-break charts `filter out minor price fluctuations by focusing on significant moves` (paraphrase of the page's noise-filtering claim, never a rule here).

### Research interpretation

Run-gated reversal capture on a single 24/7 instrument, both sides coded. Unlike the pool's 3-down/3-up fade (which buys every washed-out decline and rests flat between episodes), this system trades only reversals certified by a 3+-line run and never rests flat after the first signal — selectivity comes from the run gate, not from sitting out. Unlike soldiers/crows (which reads fixed 3-bar candle microstructure and fires every qualifying triple), this system reads variable-span line extremes: a reversal can condense months of drift into its qualifying run, and a triple that fails to break three lines of range prints nothing at all — the signal's memory stretches and contracts with realized range instead of a fixed bar count. Unlike oscillator-cross systems it reads no normalized momentum and no average of any kind — only ordered line highs/lows built from closes. Unlike channel breakouts the rails are the system's own prior lines, so the breakout level ratchets with each continuation line rather than sitting on a rolling window. The bet is that N=3 line-break reversals after certified 3+-line runs on daily BTCUSDT precede multi-day directional drift often enough to survive V-shape whipsaw, with the run gate plus the alternation fence as the sole noise defence — and with the source's own sub-40%-win-rate, no-stop character inherited undisguised (see Negative evidence).

## Signal

Exact rule as pinned (N=3, strict edges as coded — any other break count, tolerance, filter, or stop is a different, unpinned rule):

- Notation: completed daily closes `C[i]`; confirmed TLB lines `L_1..L_K` (index 1 = oldest), each with `open` (prior line close, except `L_1`) and `close`; `dir(L) ∈ {up, down}`; run = trailing same-direction count. State evolves only on completed-bar closes, sequentially from the oldest available bar.
- Seeding (pinned MQL): the first line prints on the first strict close move (`C > prev` → up line at `C`, `C < prev` → down line at `C`; equal closes print nothing). Early bars use `bars_to_check = min(3, TLB_N)` exactly as coded.
- Per completed close `C[i]` (three outcomes, pinned): reversal-up iff last line is down and `C[i] > highest_high` (max over opens+closes of the last `min(3, TLB_N)` lines, strict); reversal-down iff last line is up and `C[i] < lowest_low` (strict); continuation-up iff last line is up and `C[i] > prev-line-close` (strict); continuation-down iff last line is down and `C[i] < prev-line-close` (strict); otherwise no new line (equal closes and insufficient moves are explicit no-ops).
- Position target (TradeStation interpretation, wired to the flip book): at the close of each completed bar `i` (post-warmup), the target for the next bar is long iff the update printed a reversal-up line AND the pre-update trailing run was 3+ consecutive down lines; short iff the update printed a reversal-down line AND the pre-update trailing run was 3+ consecutive up lines; else unchanged (hold current side; flat only before the first-ever qualified reversal). Orders fire for the next bar's open: flat→long buys at next open on qualified up-reversal; flat→short sells at next open on qualified down-reversal; long-held + qualified down-reversal flips full long to full short in one step at next open; short-held + qualified up-reversal flips full short to full long in one step at next open. Same-side continuation lines and unqualified (sub-3-line-run) reversals are ignored (single-unit, no adds — declared port of one-event-per-bar). At most one order event per bar boundary; no intrabar evaluation, no intrabar orders, no partials.
- Mutual exclusion (proven, not assumed): one close produces at most one new line (the MQL `if/else-if` chain), and a line is either reversal-up, reversal-down, continuation, or nothing — both legs can never fire on the same close and no priority ruling is owed.
- Degenerate tape (proven, not assumed): a zero-range history (`C` constant) never satisfies any strict inequality, so no line and no signal ever prints; the flat-until-first-signal state needs no extra guard. Sub-3-line early-history reversals are computable per `min(3, TLB_N)` but untradable here unless the pre-update run already spans 3+ lines — and a 3+-line run cannot exist before at least 4 lines, so the warmup plus the run gate jointly fence seeding artefacts.
- Risk legs (declared researcher posture, matching both rule sources' shipped absence of risk): no stop-loss, no take-profit, no trailing, no time exit — the sole position-changing paths are qualified contra-reversals. A vertical adverse move on/after the entry bar is held in full until the opposite qualified reversal prints. This is the coded trade, disclosed, not a tunable parameter here.
- Direction: two-sided flip system, always-in-market after the first signal, flat before it by construction.

## Required data

- Completed `1d` bars of BTCUSDT only: `close` builds the entire TLB state (line opens/closes, runs, reversal/continuation tests); `open` of the next bar prices fills. No `high`, no `low`, no `volume` (TradeStation: line-break volume is meaningless off 1-tick; none gates any order), no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state gates any order. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: daily bars. One evaluation per bar at its close; fills land on the next daily bar's open. All inputs are completed-bar values — no provisional intrabar value is ever used; confirmed lines are append-only and never revised by later bars.
- Warmup: the structural need is seeding (first strict move) plus a certifiable 3+-line run plus its terminating reversal — first signal needs at minimum ~5 directional bars. The adopted warmup is the first 30 completed `1d` bars flat by record rule (predeclared researcher choice — covers seeding, run certification, and first-reversal formation with margin). No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port; all three rule sources are venue-agnostic close logic — no cross-venue equivalence is claimed beyond close-price arithmetic).
- Order timing (predeclared derivation; TradeStation blesses on-Close automation and this record declines it for conservatism): completed-bar-close decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill is claimed. At most one order exists per bar boundary and mutual exclusion is proven, so there is no same-bar dual-fire to sequence; each flip is one net fill step at a single open price.
- Cash leg: flat earns nothing by record rule (flat exists only before the first signal). No T-bill, stablecoin-lending, funding-rebate, or synthetic yield is substituted.
- Sizing/capital/costs: the sources ship no portable economics — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3×/5×) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — long bars carry realized funding, short bars carry realized funding, pre-first-signal flat bars carry none) replace them here, never presented as source-native behavior. The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one single-unit position (long or short) at any time after the first signal; every position-changing event flips in full in one step; no cooldown specified — explicitly none, not invented (re-entry requires the opposite qualified reversal, so a cooldown would only delay coded flips). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The short leg requires margin-short permission, realistic on the pinned perpetual venue. Safety orders: explicitly none.

## Evidence

### Source-reported

The three rule sources ship the full construction (both continuation predicates, both strict reversal predicates, the no-new-line outcome, N=3 typical value, seeding from the oldest bar, the 3+-line Buy/Sell interpretation, and the alternation fence). The Tradinformed page ships the only adopted performance context, pinned to its own sample: EUR/USD `4-hour`, December 2009 – June 2015, enter-on-new-reversal-line, no stops/targets/trailing, no time-of-day filter — unfiltered `Net Pips 3,772`, `Profit Factor 1.22`, `158` winning / `256` losing trades (`Win Percentage 0.38`); with the (not adopted here) 200-period EMA filter `Net Pips 2,887`, `Profit Factor 1.39`, `86` winning / `113` losing (`0.43`); `Net Long Profit $228` vs `Net Short Profit $3,545` unfiltered. This record claims no source-reported crypto performance and no reproduced performance of any kind.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Sub-40% win rate with no risk leg, quoted plainly: the only adopted backtest context wins `0.38` of trades unfiltered (`0.43` with the fenced filter) and tests `no stop-losses, trailing stops or profit targets` by its own disclosure. This record inherits that character exactly — every adverse excursion is held to the opposite qualified reversal.
2. Wrong-market, wrong-frame evidence, admitted plainly: every printed number above is EUR/USD `4-hour` 2009–2015 from an Excel template with undisclosed costs — it is characterization context for the mechanism, never BTCUSDT-`1d` evidence and never a claim about this record's economics.
3. V-shape whipsaw, admitted plainly: a reversal needs the full 3-line extreme break, so a sharp V prints the flip near the extreme and the recovery re-reverses only after another full break — alternating 3+-line runs flip the full unit back and forth at the worst prices with no stop, target, or cooldown to dampen it. Narrowing N would be a different, unpinned rule — none is admitted here.
4. Fenced source-adjacent upgrades, admitted plainly: the 200-period EMA trend filter, Samco-style stops below the last opposite block / take-profits at prior support-resistance, RSI/MA confirmation overlays, and any time-of-day filtering are all described near the sources and none is adopted — adopting any would be a different, unpinned rule.
5. Conservative fill timing, admitted plainly: TradeStation blesses same-bar on-Close automation and this record still fills at the next bar's open — gap-through moves across reversal edges are taken at post-move opens, never at the signal close.
6. Warmup and seeding cost, admitted plainly: the first 30 daily bars are flat by record rule and the first line's direction is fixed by the oldest available history — a qualified reversal completing inside warmup is deliberately untraded, pinned, not recovered.
7. Derivation boundary fenced: the only non-source behaviors in this record are the BTCUSDT-`1d` deployment frame, next-open fills, the adopted 30-bar warmup with record-rule pre-warmup flat, house sizing/costs, and the flip-only risk posture — all predeclared above; the N=3 count, strict edges, seeding, three-outcomes-per-close, 3+-line gate, alternation fence, signed direction mapping, pre-first-signal flat state, and every exclusion are source-native. This record is therefore never evidence that any source deployment passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: the pinned N=3 count / strict reversal-continuation edges / seeding / 3+-line gate / alternation fence / flip-only book / two-sided / `1d` BTCUSDT / next-open fills / 30-bar warmup are frozen.

- F1 — Run-gate relevance: an unqualified twin (every reversal line flips, including sub-3-line alternations, same book/frame/fills) must not improve net expectancy; fail ⇒ the 3+-line certification and the trendless fence add nothing over raw reversal trading.
- F2 — Flip relevance: a flat-book twin (each qualified contra-reversal exits to flat instead of opening the contra unit, re-entering only on the next qualified reversal, same frame/fills) must not improve net expectancy; fail ⇒ staying perpetually exposed through flips adds nothing over reversal-and-hold episodes.
- F3 — Construction relevance: a bare-count twin (long-target on three consecutive higher closes, short-target on three consecutive lower closes, no line extremes, same book/frame/fills) must not improve net expectancy; fail ⇒ the variable-span line-extreme construction adds nothing over naked three-close chains.
- F4 — Selectivity relevance: buy-and-hold over the same sample must not improve net expectancy; fail ⇒ sitting out non-reversal stretches costs more in missed drift than it saves in avoided exposure.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid completed `1d` bar closes; fills at next-bar opens; the state machine reads closes only). The close-arithmetic ports across perpetual venues without structural change; the 24/7 market needs no session approximation (lines read bar closes only, never wall-clock sessions). Both sides are explicit legs, so a spot-only deployment expresses the long half only while every flip-to-short stays venue-gated (short permission unused, never silently converted) — a spot-only variant would be a different, unpinned claim. No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session template, no cross-venue state. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived frame and fill timing: the sources define close logic over abstract bars with no market, venue, or fill convention (and TradeStation's own note blesses on-Close fills this record declines); this record decides on completed `1d` bars with next-open fills. Backtest economics of other framings or timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about any other configuration.
- No source cost declaration of any kind: no fee, slippage, or funding assumption ships anywhere usable — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Always-in-market exposure: after the first signal the book is never flat by rule, so adverse drift between qualified contra-reversals is held in full — long unhedged stretches are the coded trade, disclosed, not smoothed.
- Static break count: N=3 is the sources' typical value, not tuned here — volatility regimes that break three lines routinely versus rarely are inherited as-is, disclosed, not adapted.
- Unmodeled alternation context: per TradeStation's own fence, alternating markets are `trendless` — this record inherits the fence exactly (sub-3-line reversals are no-ops) and claims no edge inside alternation.
- Warmup and seeding cost: the first 30 daily bars are flat by record rule and seeding is fixed by the oldest history, so a qualified reversal completing inside warmup is deliberately untraded — pinned, not recovered.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`, bar-close decision on completed `1d` bars, next-open market fills, single-asset two-sided flip book) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. PASS means the declared derived strategy is causally expressible under the pinned Hummingbot model — not profitable, not Qlib-paritied, not source-equivalent, not live-tradable.

## Related Wiki records

None.

## Sources

- TradeStation official Help, `Line Break Chart` — N-line build predicates, `If there is no new high or low, no line is added`, the `Trading Interpretation (when Line Break = 3)` Buy/Sell/alternation-fence clauses, and the on-Close automation note. https://help.tradestation.com/09_01/tradestationhelp/charting/linebreak_chart.htm (fetched live 2026-10-14, 9,128 bytes)
- TradingView official Help Center, `Introduction to line break charts` (solution 43000502273) — Japanese chart-type definition, typical `Number of lines` 3, three-outcomes-per-close calculation method. https://www.tradingview.com/support/solutions/43000502273-introduction-to-line-break-charts/ (fetched live 2026-10-14)
- EarnForex `Three-Line-Break`, `ThreeLineBreak.mq4` at commit `efe1adda175f1bbec5372b329368457095fd6a67` (`1.00`, 2025-04-07) — seeding, `MathMin(LinesToBreak, TLB_N)` window, strict reversal/continuation branches, one-line-per-bar construction. https://github.com/EarnForex/Three-Line-Break/blob/efe1adda175f1bbec5372b329368457095fd6a67/ThreeLineBreak.mq4 (fetched live 2026-10-14, 17,740 bytes)
- Tradinformed, `How To Trade 3 Line Break Charts Profitably` — reversal-entry rule disclosure, EUR/USD 4H Dec-2009–Jun-2015 sample pin, printed results table (3,772 net pips / PF 1.22 unfiltered; 2,887 / 1.39 with 200-EMA filter; 158W-256L). https://www.tradinformed.com/how-to-trade-3-line-break-charts-profitably/ (fetched live 2026-10-14)
