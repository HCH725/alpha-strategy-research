---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: IMI 50-midline-cross flip two-sided on BTCUSDT 1d bars
created: 2026-10-15
updated: 2026-10-15
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 1994
sources:
  - https://doc.stocksharp.com/en/topics/api/indicators/list_of_indicators/intraday_momentum_index
  - https://help.cqg.com/cqgic/26/Documents/intradaymomentumindeximi.htm
  - https://www.tradingview.com/script/1R88ynW5-Intraday-Momentum-Index
  - https://github.com/ta4j/ta4j/blob/0d1e1a0870aff46f1f44beacad2fdda5bf3238db/ta4j-core/src/main/java/org/ta4j/core/indicators/IntraDayMomentumIndexIndicator.java
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# IMI 50-midline-cross flip two-sided on BTCUSDT 1d bars

## Provenance

Primary sources read end to end (verified 2026-10-15):

- StockSharp technical documentation, `Intraday Momentum Index (IMI)` page, fetched live over HTTPS during this cycle (HTTP 200, 401651 bytes). States the indicator `is a technical indicator developed by Tushar Chande that combines intraday pricing principles and the RSI concept to measure intraday momentum`. Ships the full construction: `Gain = Close - Open, if Close > Open` and `Loss = Open - Close, if Close < Open`; `Sum Gains = Sum of all Gains over Length period` and `Sum Losses = Sum of all Losses over Length period`; `IMI = 100 * (Sum Gains / (Sum Gains + Sum Losses))`; `Note: If (Sum Gains + Sum Losses) equals zero, IMI is set to 50 to avoid division by zero`. Ships the calculation period default (`default value: 14`), the level map (`Values above 70 are typically viewed as indicating market overbought conditions`, `Values below 30 are typically viewed as indicating market oversold conditions`), and the pinned trigger pair (`Centerline Crossovers: Crossing the 50 line from bottom to top can be viewed as a bullish signal; Crossing the 50 line from top to bottom can be viewed as a bearish signal`). This record claims no crypto performance and no reproduced performance.
- CQG official platform documentation, `Intraday Momentum Index (IMI)` page, fetched live during this cycle (HTTP 200, 9988 bytes). States `The Intraday Momentum Index (IMI) is a technical indicator developed by market technician Tushar Chande`, and pins the same construction independently: `Gains = CP - OP on Up Days, i.e., Close > Open` (`CP = Closing price`, `OP = Opening price`); `Losses = OP - CP on Down Days, i.e., Open > Close`; `n = Number of days (14 is commonly used)`. A doji bar (`Close == Open`) is neither an up day nor a down day under either definition, so it contributes zero to both sums by construction — no researcher tie-break is needed or invented.
- TradingView lineage (open-source confirmation only — rule read in the StockSharp/CQG/ta4j sources, never retyped from here): `Intraday Momentum Index` by `everget`, page carries the `OPEN-SOURCE SCRIPT` badge, fetched live during this cycle (HTTP 200, 428658 bytes of landing HTML). The page states `Intraday Momentum Index indicator script. This indicator was originally developed by Tushar Chande.`
- ta4j immutable implementation, fetched raw at pinned commit `0d1e1a0870aff46f1f44beacad2fdda5bf3238db` (resolved as the current `git ls-remote` HEAD of `ta4j/ta4j` during this cycle), file `ta4j-core/src/main/java/org/ta4j/core/indicators/IntraDayMomentumIndexIndicator.java` (HTTP 200, 2845 bytes): `realBody = close - open`; `closeOpenDiff = max(realBody, 0)`; `openCloseDiff = abs(min(realBody, 0))`; `SMA` of each leg over `barCount`; `IMI = 100 * avgGain / (avgGain + avgLoss)`. The ratio of equal-length means equals the ratio of equal-length sums, so this is the identical arithmetic to the documented formula. Bars before the indicator is stable return `NaN` (unstable-bar concept — fenced out of every traded bar by the warmup below).
- Book lineage (attribution only): public IMI documentation attributes the construction to Tushar Chande (with Stanley Kroll) in `The New Technical Trader` (reported 1994, adopted as `source_as_of: 1994`); the 1994 date itself is source-reported context, not byte-verified in this cycle. An additional practitioner article (`Technical Analysis of Stocks & Commodities`, Intraday Momentum Index) was attempted during this cycle but returned HTTP 403 and is therefore NOT used as evidence anywhere in this record.

Licence and rights: this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any source trading system. Researcher-declared adaptations are exactly five: (1) market pin `BTCUSDT` on Binance futures with the source-native daily frame kept (the sources describe daily bars — frame-faithful, venue transfer plus symbol spelling, futures short permission disclosed here, never presented as source-native); (2) midline-cross-only scope (the documented `70`/`30` overbought/oversold levels, divergence use, and trend-quantification-first guidance are real source content, disclosed here and never carried into the traded trigger — see Negative evidence); (3) same-bar-close fills on completed `1d` bars; (4) an adopted 30-bar warmup with pre-warmup bars flat by record rule (plain sums need no EMA seed convention — none exists, none invented); (5) house sizing/capital/costs replacing the absent source economics (zero cost assumption — recorded as absent, never as zero-cost evidence; see Execution assumptions). The open/close body rule, the `max(C-O,0)`/`max(O-C,0)` legs, the 14-bar sums, the `100 x gains/(gains+losses)` ratio, the all-zero-window `50` convention, the `50`-midline cross trigger pair, the atomic reversal, and the no-stop/no-target/no-flat stance are source-pinned or predeclared above and unmodified elsewhere.

Pre-write dedup (2026-10-15): working-tree case-insensitive fixed-string searches for `Intraday Momentum` and word-boundary `IMI` return zero strategy records using this source, author, indicator, or construction. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. The two closed October-15 Scout PRs (#219 engulfing body-cover flip, #220 morning/evening-star gap-penetration flip) are candlestick-pattern reversals with unrelated arithmetic. Closest pool records are different mechanism classes: every `rsi-*` record (including `rsi-classic-level-reversal`, `cumulative-rsi-dual-threshold`, `connors-rsi2-ma70-fade`, `drm-dynamic-rsi-momentum`, `laguerre-rsi-cu-cd-cross`) accumulates close-to-close changes and never reads the open; `qstick-zero-cross-trend-two-sided-btcusdt-1h` trades the raw unbounded average `SMA(Close-Open)` against zero with no ratio and no fixed midline; `vzo-tactic1-band-recross-reversal-two-sided-btcusdt-1d` normalizes signed volume (not price bodies) through an EMA pair against fixed `+-40` bands; `dual-ema-engulfing-volume-long` trades a two-bar engulfing shape, not a 14-bar body ratio. No pool record computes `100 x summed open-to-close gains / summed open-to-close bodies` or crosses its `50` midline. Shared `RSI-concept` wording or shared open/close inputs are not shared signal.

## Economic mechanism

### Source-reported

Intraday-body acceptance with midline-cross reversal discipline: each bar's real body (`Close - Open`) is split into a gain leg (green bodies only) and a loss leg (red bodies only), both summed over 14 bars, and their share scaled to `0-100` so the print reads which side owned the recent opens-to-closes — buyers' or sellers'. Crossing up through `50` means intraday selling pressure has released enough to accept the long side; crossing down through `50` means intraday buying pressure has released enough to accept the short side. The design bets that open-to-close persistence leads the next body: unlike close-to-close RSI, which ignores where each session opened, the print moves only on bodies actually printed between each bar's own open and close, so gaps between bars can never touch any order-gating line. There is no stop, no target, no flat state by record design after the first signal — the opposite midline cross is the exit.

### Research interpretation

Single-series bounded-oscillator system, two-sided, always-in-position after the first signal, with the midline as the only trigger. Unlike cumulative systems (OBV, PVT) whose totals drift without bounds and need a second series to cross, this rule normalizes participation into a fixed `0-100` scale so one constant level (`50`) suffices forever — no moving reference, no re-fit, no second line. Unlike zero-line flippers, the trigger sits at the exact balance point where summed gains equal summed losses, so every holding period is exactly one pressure-regime migration. Unlike Qstick, which averages raw signed bodies (unbounded, scale-dependent, zero-crossed), this rule divides by total body activity, making the print unit-free and comparable across volatility regimes — a `50` cross means the same pressure balance at any price level. Unlike the pool's close-to-close RSI records, overnight gaps and inter-bar jumps are structurally invisible: only the within-bar body enters either sum. The price of the always-in posture is indefinite adverse rides plus whipsaw pairs when the print straddles `50`: a leg whose opposite cross never prints is held forever. The bet is on open-to-close body persistence, not on any price pattern, second series, volume read, calendar effect, or volatility read.

## Signal

Exact rule as pinned (all inputs frozen — any other value is a different, unpinned rule):

- Declarations (derived): single-position state machine over `BTCUSDT 1d` with same-bar-close execution and house sizing/costs (see Execution assumptions). At most one open leg; state ∈ {flat, long, short}; flat exists only before the first signal and under the warmup rule.
- Body legs, pinned verbatim at defaults (`Length = 14`): with `O(t)` open and `C(t)` close of completed bar `t`: `G(t) = max(C(t) - O(t), 0)`; `L(t) = max(O(t) - C(t), 0)`. A doji bar (`C(t) == O(t)`) contributes `0` to both legs by construction under both the StockSharp and CQG definitions — no tie-break exists or is invented.
- Indicator, pinned verbatim: `IMI(t) = 100 x sum(G, 14)(t) / (sum(G, 14)(t) + sum(L, 14)(t))` over completed bars `t-13..t`. All-zero window (fourteen dojis): `IMI(t) = 50` by the pinned StockSharp convention (`IMI is set to 50 to avoid division by zero`) — the record's governing branch, predeclared here, matching the ta4j unstable-bar fence in effect (such a window never trades under the warmup rule on real BTCUSDT anyway — fenced in Negative evidence). No smoothing, no seed, no tie-break anywhere in the stack.
- Entry long: on bar `t` with `IMI(t-1) < 50` and `IMI(t) >= 50` (crossing the `50` line from bottom to top, landing inclusive; from flat: open long; from short: atomic reversal — close short plus open long as a single reversal event). Refires of the long state while already long are no-ops (no pyramiding — explicitly none, not invented).
- Entry short: mirror on `IMI(t-1) > 50` and `IMI(t) <= 50` (crossing the `50` line from top to bottom).
- Exits: the opposite cross only (long exits exactly when the short trigger prints and vice versa). No stop, no target, no trailing, no time exit, no cooldown — explicitly none by record rule, not invented, consistent with the trigger pair forming a complete always-in machine. There is no flat path after the first signal at all — flat is reachable only pre-signal and under warmup.
- Direction: two-sided with an explicit pre-first-signal flat state (plus the 30-bar warmup flat by record rule). The documented centerline pair prescribes both the bullish and the bearish leg; a long-only or short-only reading would contradict it.

## Required data

- Completed `1d` bars of BTCUSDT: `open` (body split) and `close` (body split) only — Binance USDT-M futures by record pin (see Limitations). No `high`, no `low`, no volume, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line. Gaps between bars never enter either sum.
- Single decision timeframe `1d` (frame-faithful to the documented daily construction; the rule references no other frame, no multi-timeframe input, no `security`-style call of any kind — single-frame by construction).
- Warmup: the binding cost is the two 14-bar plain sums (first fully-formed value needs 14 completed bars) plus the `t-1` comparison reach. The adopted warmup is the first 30 completed `1d` bars flat by record rule (predeclared researcher choice — covers both sums plus the comparison reach with wide margin; no seed branch exists to fence). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Each bar's open/close enter the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (frame-faithful `1d`; venue choice, symbol spelling, and short permission disclosed in Provenance, never presented as source claims).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity, and each trigger reads only completed opens/closes, so each bar's outcome is a single deterministic event (hold, open, or atomic reversal).
- Sizing/capital/costs: the sources ship no portable economics (zero commission/quantity assumption — recorded as absent economics, never as zero-cost evidence) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior. Funding is modeled, never reported as realized or canonical funding.
- Concurrency: single-position machine — at most one open leg; same-state bars while positioned are no-ops; the opposite cross reverses in full (one atomic event); re-entry is allowed on the next fresh cross after any close (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The sources ship the full construction (`Gain = Close - Open, if Close > Open`; `Loss = Open - Close, if Close < Open`; `Sum Gains`/`Sum Losses` over the `Length` period; `IMI = 100 * (Sum Gains / (Sum Gains + Sum Losses))`; all-zero window set to `50`), the period default (`14` / `14 is commonly used`), the level map (`70` overbought, `30` oversold), the midline trigger pair (crossing `50` bottom-to-top bullish, top-to-bottom bearish), and the Chande attribution — quoted in Provenance. None of the sources ships a backtest table for this construction, so this record carries zero source-reported performance numbers and claims no performance of any kind.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No performance to carry, admitted plainly: unlike paper-sourced records with backtest tables, the IMI documentation ships construction, levels, and trigger semantics only — there is no expectancy number anywhere to fence, and this record claims none.
2. Untraded source content fenced, admitted plainly: the `70`/`30` overbought/oversold levels, divergence use, failed-swing reads, and the quantify-the-trend-first guidance are real documented content deliberately not carried into the traded trigger (they need trend-state or swing judgments this record does not define). The pinned `50`-cross pair is therefore signal-complete by record rule, and carrying OB/OS meanings onto it would be fabrication.
3. No hidden exits or risk layer: the traded machine names no stop, no target, no trailing, no time exit anywhere — the no-stop/no-target posture is the record rule, explicitly none, never hidden. Every adverse excursion is held to the opposite midline cross.
4. Trigger exclusivity fenced: the long trigger requires `IMI(t-1) < 50` and the short trigger requires `IMI(t-1) > 50` — no prior print satisfies both, so no bar fires both transitions and no priority rule is needed or invented. (A single bar can traverse the whole scale, but then exactly one leg's prior-side condition holds.)
5. Exact-touch determinism fenced: landings exactly on `50` count as crosses by the pinned `>=`/`<=` comparisons (measure-zero on continuous prints — disclosed, not oversold as tolerance). The all-zero-window `50` print therefore holds the prior state deterministically: at `50/50` neither prior-side condition holds.
6. Doji leg fenced: `C(t) == O(t)` contributes `0` to both sums under both independent definitions (StockSharp, CQG) — no bar leaves either leg undefined, no tie-break invented. A window of pure dojis resolves to the pinned `50` convention, never to `NaN` trading.
7. Gaps structurally excluded, stated plainly: each leg reads only its own bar's open-to-close body; inter-bar jumps (`C(t-1)` to `O(t)`) enter neither sum at any bar. Overnight-gap sensitivity is zero by construction, not by assumption.
8. No future leakage in the stack, stated plainly: at decision bar `t`, both sums read completed bars `t-13..t`, and each trigger compares prints `t-1..t` — every input is complete at bar `t`'s close. No multi-frame read, no negative index, no full-sample normalization, no repainting path, no calendar read at all. No seed branch exists anywhere in the stack.
9. RSI/Qstick/VZO-family overlap fence, admitted plainly: the pool's close-to-close RSI records never read the open; `qstick-zero-cross` averages raw signed bodies with no ratio and no fixed midline; `vzo-tactic1` normalizes signed volume through an EMA pair against fixed `+-40` bands with no price-body read. This record divides summed price bodies by summed price bodies against a fixed `50` midline with no volume, no smoothing, and no second series. Shared `RSI-concept` wording or shared open/close inputs are not shared signal.
10. Two-sided posture provably complete: symmetric `50`-cross-up long / `50`-cross-down short legs with symmetric atomic-reversal exits under the documented centerline pair — no third direction exists, and a long-only reading would contradict the printed bearish leg.
11. Derivation boundary fenced: the only non-source-native behaviors in this record are the `BTCUSDT` futures market pin with the source-native daily frame kept, the midline-cross-only scope, same-bar-close fills, the adopted 30-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the body-split rule, the gain/loss legs, the 14-bar sums, the ratio formula, the all-zero `50` convention, the cross triggers, the atomic reversal, the single-position guards, and the risk posture are source-pinned or predeclared. This record is therefore never evidence that any other market, frame, period, threshold set, or timing of the source passes.
12. Network limitation disclosed: the formula, legs, period, levels, trigger pair, and zero-convention lines above were byte-verified in the fetched StockSharp page (401651 bytes, HTTP 200) and cross-checked against the fetched CQG page (9988 bytes, HTTP 200), the fetched figurebetter worked example (423996 bytes, HTTP 200), the pinned ta4j file (2845 bytes at commit `0d1e1a0870aff46f1f44beacad2fdda5bf3238db`), and the TradingView page title/author/badge (428658 bytes, HTTP 200); the TASC practitioner article was attempted but refused (HTTP 403) and contributes nothing. The division of evidence is disclosed here, not hidden.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: open-to-close body split / `max(C-O,0)`+`max(O-C,0)` legs / 14-bar plain sums / `100 x gains/(gains+losses)` ratio with all-zero `50` / `50`-midline cross pair with hold / atomic reversal / no-stop-no-target posture / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Midline relevance: replacing the `50` flip with a `70`/`30` overbought-fade/oversold-dip trigger pair (same period, same state machine, same reversal handling) must not improve net expectancy; fail ⇒ the balance-point cross adds nothing over the documented OB/OS levels.
- F2 — Period relevance: shortening the sums to `Length = 7` (same midline, same cross, same state machine) must not improve net expectancy; fail ⇒ the 14-bar body memory adds nothing over a fast variant.
- F3 — Posture relevance: exiting to flat on the opposite cross instead of atomic reversal (same entries, same midline, flat between migrations) must not improve net expectancy; fail ⇒ the always-in alternation adds nothing over a flat-resting variant.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (frame-faithful `1d`; venue transfer disclosed). The rule reads only completed daily opens and closes, so no high/low definition differences and no volume-series differences can touch any order-gating line — but spot-vs-perp open/close prints can still differ structurally (funding-driven drift, venue aggregation, anomalous prints), so the futures-venue pin is load-bearing and disclosed. The ratio is unit-free and the midline is a fixed constant, so no fixed-pip recalibration is needed across assets — cross-asset behavior differences are still real and unclaimed. The rule is two-sided with no stop leg, so a spot-only deployment expresses the long state and reversal mechanics only to the extent the venue permits shorting — full two-sided expression assumes a futures venue, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read beyond each calendar-day bar's own open-to-close body (no session gating anywhere); decision boundaries are calendar-day bars of the venue feed, disclosed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived market pin: the sources describe daily stock bars; this record pins `BTCUSDT` futures `1d`. Cross-market and spot-vs-perp open/close behavior differences are real — the venue transfer is disclosed, and this record makes no claim about any other market or the sources' native venue.
- Untested trigger scope: the only source-documented trigger carried here is the `50`-midline cross pair; the `70`/`30` levels, divergence, and trend-first guidance are performance-unclaimed context, and the pinned pair itself carries no expectancy claim until downstream research measures it.
- No source economics: the sources ship no commission, sizing, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- No price stop, no time stop: adverse excursion after entry has no guardrail beyond the opposite midline cross; a leg whose opposite trigger never prints is held indefinitely. This is the record-rule posture, disclosed as a principal risk.
- Whipsaw sensitivity: midline straddles print repeated reversal pairs with no flat state to rest in, by the prescribed always-in design. The midline construction is the documented trigger, disclosed, not smoothed.
- Body-definition sensitivity: venue open/close prints (rolls, aggregation, anomalous prints) flow straight into both legs; a venue that cannot supply trustworthy per-bar opens and closes cannot trade the pinned rule.
- Warmup cost: both sums need 14 completed bars plus comparison margin; the adopted 30-bar warmup absorbs this structurally with wide margin, and the first 30 bars are flat by record rule.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- StockSharp technical documentation, Intraday Momentum Index (IMI) — formula, legs, period default, 70/30 levels, 50-cross trigger pair, all-zero 50 convention, Chande attribution (verified live in the fetched page during this cycle; zero crypto claims): https://doc.stocksharp.com/en/topics/api/indicators/list_of_indicators/intraday_momentum_index
- CQG official platform documentation, Intraday Momentum Index (IMI) — independent construction pin, up/down-day definitions, 14-day convention, Chande attribution (verified live in the fetched page during this cycle): https://help.cqg.com/cqgic/26/Documents/intradaymomentumindeximi.htm
- figurebetter indicator guide, Intraday Momentum Index — worked body-sum example and 14-lookback convention (verified live in the fetched page during this cycle): https://figurebetter.com/guides/indicators/intraday-momentum-index
- TradingView everget lineage (title/author/open-source-badge confirmation only): https://www.tradingview.com/script/1R88ynW5-Intraday-Momentum-Index
- ta4j immutable implementation (construction cross-check only — ratio-of-means identity disclosed): https://github.com/ta4j/ta4j/blob/0d1e1a0870aff46f1f44beacad2fdda5bf3238db/ta4j-core/src/main/java/org/ta4j/core/indicators/IntraDayMomentumIndexIndicator.java
