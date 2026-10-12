---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Percent B MFI dual-thrust cross two-sided on BTCUSDT 1d bars
created: 2026-10-13
updated: 2026-10-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-13
sources:
  - https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/percent-b-money-flow
  - https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/b-indicator
  - https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/money-flow-index-mfi
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Percent B MFI dual-thrust cross two-sided on BTCUSDT 1d bars

## Provenance

Primary sources read end to end as Markdown this cycle (fetched 2026-10-13, all HTTP 200):

- Strategy page: `table-of-contents/trading-strategies-and-models/trading-strategies/percent-b-money-flow` (title `Percent B Money Flow`, attributes the system to John Bollinger's *Bollinger on Bollinger Bands*: "Buy when %B moves above .80 and the Money Flow Index (MFI) moves above 80. Sell when %B moves below .20 and the Money Flow Index (MFI) moves below 20. Bollinger suggests using the Parabolic SAR for stops."). Direction is two-sided by construction: the worked examples direct selling short on sell signals ("Selling short on the mid-December sell signal would have resulted in a loss, while buying on the early January buy signal would have resulted in a modest gain"). No backtest table, metric, Sharpe, win rate, or drawdown ships anywhere — the examples are qualitative anecdotes only, and this record claims no source-reported performance of any kind.
- %B indicator page: `.../technical-indicators/b-indicator` — "The default setting for %B is based on the default setting for Bollinger Bands (20,2). The bands are set two standard deviations above and below the 20-day simple moving average" with price input the close. Its scan block pins executable trigger semantics verbatim: `Daily %B(20,2.0,Daily Close) > 0.8` AND `Daily MFI(14) > 80` AND `Yesterday's Daily MFI(14) < 80` (bullish), mirrored with `< 0.2` / `< 20` / `> 20` for the bearish side — i.e. %B beyond the thrust level as state while MFI crosses the extreme. The scan's volume-prefilter line (`SMA(20,Volume) > 40000`, an equity-liquidity screen) is not part of the strategy rule and is excluded here, disclosed.
- MFI indicator page: `.../technical-indicators/money-flow-index-mfi` — "based on a 14-period MFI, which is the default setting in SharpCharts and the setting recommended by the creators"; arithmetic pinned verbatim: `Typical Price = (High + Low + Close)/3`, `Raw Money Flow = Typical Price x Volume` (positive when typical price rises, negative when it declines, excluded when unchanged), `Money Flow Ratio = (14-period Positive Money Flow)/(14-period Negative Money Flow)`, `Money Flow Index = 100 - 100/(1 + Money Flow Ratio)`. Default "calculated using 14 periods".
- Scan-over-prose pin (one material discrepancy, disclosed): the %B page prose once writes `MFI(10)` ("An uptrend begins when %B is above .80 and MFI(10) is above 80"), but the same page's executable scan clauses use `MFI(14)` twice with cross semantics, and the MFI page independently confirms 14 as both the SharpCharts default and the creators' recommendation. This record pins `MFI(14)`; an `MFI(10)` printing would be a different, unpinned rule and is excluded from every order leg here.
- Licence and rights: StockCharts ChartSchool is public technical documentation. This record cites and normalizes the rule (short quoted phrases for gate evidence only) and reproduces no extended source passage.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly five: (1) market/timeframe port — the source demonstrates on daily equity charts with no symbol; the derived record trades BTCUSDT Binance perpetual on completed `1d` bars; (2) same-bar-close fills (the source ships no execution-timing statement); (3) position-state pin — single-unit per side, repeat-signal-while-positioned as no-op, full reversal on the opposite signal, flat before the first signal (predeclared; the source names no sizing/pyramiding); (4) an adopted 40-bar warmup with pre-warmup bars flat by record rule (covers the SMA20/stdev20 seed and the MFI 14-bar money-flow seed plus margin — see Required data); (5) house sizing/capital/costs replacing the absent source economics (see Execution assumptions). The %B(20,2.0,close) construction, the MFI(14) arithmetic, the 0.80/0.20 and 80/20 thresholds, the MFI-cross trigger semantics, the two-sided buy-strength/sell-weakness stance, and the reversal-only no-stop posture are source-native and unmodified.

Pre-write dedup (2026-10-13): working-tree case-insensitive searches for `percent-b`, `%B`-with-MFI co-occurrence, `money-flow` dual-thrust, and `Bollinger on Bollinger` return zero strategy records combining %B with MFI — no admitted rule uses this source page, book lineage, or dual indicator. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state-following reversal) — single-file heads, different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `bollinger-band-breakout-long-midline-exit-btcusdt-1d-2026-10-11.md` is a single-band long-only breakout (close crossing above the 1.5σ upper band, midline exit, no volume read, no short leg); `mfi-threshold-divergence-reversal-two-sided-btcusdt-4h-2026-10-12.md` is a mean-reversion system on `4h` (MFI crossing back up through 20 / down through 80 plus 5-bar divergence under midline gates — the opposite philosophy: fading extremes, never buying them); `alphatrend-mfi-atr-trailing-reversal` reads MFI only as a `>= 50` coefficient gate for an ATR ratchet (MFI never crosses a threshold there). Five-axis distinction: source identity differs (StockCharts Percent-B-Money-Flow/Bollinger lineage versus FMZ 426339 or Eterna files), signal construction differs (%B(20,2.0) state gate stacked with an MFI(14) extreme cross versus single-band cross, divergence pair, or ratchet gate), trigger differs (MFI crossing *up through 80* while %B > 0.80 — buying strength — versus crossing back through 20, midline exit, or ratchet self-cross), direction handling differs (symmetric two-sided flip versus long-only), and frame/economics are separately pinned (`1d` two-sided, no stops by source construction).

## Economic mechanism

### Source-reported

New-trend ignition by dual thrust: a surge in %B (close thrust into the top quintile of its own Bollinger range) reflects a strong upthrust in prices, and a simultaneous MFI surge above 80 shows that thrust is backed by heavy buying volume. The design buys strength mid-advance on the theory that further strength follows ("in theory, the buy signal will occur in the middle of the advance"); symmetrically it sells weakness mid-decline. The stated risk is trend failure after the thrust ("Failure of the trend to continue is the biggest risk to the system"), handled in the source only by the suggested Parabolic SAR stops — whose parameters ship nowhere and are therefore not part of this record.

### Research interpretation

Edge-triggered two-sided continuation system with no price level, stop, target, or confirmation leg beyond the two gates — always-in-market after the first signal, flipping only on the opposite dual trigger. Unlike the pool's mean-reversion MFI record (which fades extremes: long only when MFI recrosses *up through 20*), this system *buys* the overbought print (MFI crossing *up through 80*) and only when volatility-normalized position agrees (%B > 0.80) — congestion at extremes without a fresh MFI cross fires nothing, so stale overbought holds are ignored by construction. Unlike the pool's single-band Bollinger breakout (price-only, long-only, midline exit), both directions require volume conviction, and exits are opposite-signal reversals rather than midline reclaims. The bet, ported to BTCUSDT's own daily bars, is on daily thrust persistence backed by money flow, never on a level, squeeze, calendar, divergence, or mean-reversion anchor.

## Signal

Exact rule as pinned (%B 20/2.0, MFI 14, 0.80/0.20, 80/20 frozen; any other value is a different, unpinned rule):

- Indicator arithmetic (source-native): `basis[t] = SMA(close, 20)[t]`; `σ[t] = population stdev(close, 20)[t]` (researcher computation pin, disclosed: StockCharts specifies "two standard deviations" without a sample/population qualifier; population matches the Bollinger standard and the admitted pool BB convention); `upper[t] = basis[t] + 2σ[t]`; `lower[t] = basis[t] − 2σ[t]`; `%B[t] = (close[t] − lower[t]) / (upper[t] − lower[t])`. MFI per the pinned page formulas: `TP = (H+L+C)/3`, signed `RMF = TP × V` by `TP` change versus the prior bar (unchanged-TP bars excluded), `MR = Σ14 positive / Σ14 negative`, `MFI = 100 − 100/(1 + MR)`; a zero negative-flow sum pins `MFI = 100` (standard boundary, disclosed).
- Entry long: `%B[t] > 0.80` AND `MFI[t] > 80` AND `MFI[t−1] < 80` → open the full long (or, while short, close the full short and open the full long in the same execution step: full reversal, no residual leg). While already long, a repeat firing is a no-op by record rule (predeclared single-unit pin). Before the first signal the system is flat (no position by construction).
- Entry short / reversal: `%B[t] < 0.20` AND `MFI[t] < 20` AND `MFI[t−1] > 20` → mirror image (open full short; while long, full reversal in one step; repeat-while-short is a no-op).
- Long/short firings are mutually exclusive on every bar by construction (`MFI[t] > 80` and `MFI[t] < 20` cannot co-hold) — no same-bar ordering ambiguity exists anywhere in this record. Boundary equality (`%B == 0.80`, `MFI == 80`, `MFI[t−1] == 80`, and mirrors) fails the strict predicates and the position simply holds — stated, not patched. A degenerate bar with `upper == lower` (twenty identical closes) leaves %B undefined (`0/0`) and fires neither leg — pinned as hold. An `na` indicator value (warmup) fires neither predicate — pinned as hold, never patched with a guard constant.
- Risk legs (pinned absence, not invented): the strategy page ships no stop/target/trailing/time-exit parameter — only the parameterless sentence "Bollinger suggests using the Parabolic SAR for stops". With no SAR acceleration, maximum, or application rule recoverable from any primary source, this record's posture is explicitly no stop, no target, no trailing, no time exit; a PSAR-stop printing would be a different, unpinned rule (see Negative evidence).
- Direction: two-sided long/short with symmetric reversal. Futures venue required for the short leg (realistic on the pinned perpetual venue).

## Required data

- Completed `1d` bars of BTCUSDT: `close` (%B), plus `high`/`low`/`close`/`volume` (MFI typical-price and money flow). No `open`-series read ships in any order-gating line; no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order leg. The rule makes no cross-symbol call, so it is single-symbol single-frame by construction.
- Single decision timeframe `1d` (researcher port; the source demonstrates on daily charts). One evaluation per completed bar.
- Warmup: the binding seeds are the SMA20/stdev20 seed (20 completed bars) and the MFI 14-bar money-flow accumulation (typical-price change needs one prior bar, so 15 completed bars). The adopted warmup is the first 40 completed `1d` bars flat by record rule (predeclared researcher choice — roughly twice the slow seed with margin); no signal before bar 41 may trade. No repainting (all inputs are completed-bar prints), no negative shift, no future reference, no full-sample normalization. Binance spot/futures candle volume is the point-in-time print for the completed bar — no restatement, no revision.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (the source names no market — daily equity charts — so the venue/symbol pin is a researcher market choice, disclosed, never presented as source-native).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source ships no execution-timing statement; this record does not claim any source fill convention. No maker-touch, queue, or intrabar-path-dependent fill: with mutually exclusive dual-gate legs and no stop/target legs, there is no same-bar ordering ambiguity of any kind.
- Sizing/capital/costs: the source ships no live sizing, capital, commission, fee, slippage, margin, or funding assumption anywhere. The explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all) apply to the derived evaluation here, with the single-unit/no-add/reverse-full position pin from Signal, never presented as source-native behavior.
- Concurrency: at most one unit per side under fixed Long/Short order paths (predeclared pin over absent source text); repeat same-side firings while positioned are no-ops; the opposite firing reverses in full in one step; re-entry after a reversal needs only the next opposite dual trigger (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The short leg requires margin-short permission, realistic on the pinned perpetual venue.

## Evidence

### Source-reported

No performance table, figure, backtest metric, Sharpe, win rate, drawdown, or profit number ships anywhere on the strategy, %B, or MFI pages — the only outcome language is qualitative anecdote ("would have resulted in a loss", "a modest gain", "resulted in a sharp loss"). This record claims no source-reported performance. Exact empirical numbers require traceable table/figure/section provenance or are omitted — there are none to report.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The lone `MFI(10)` prose mention on the %B page conflicts with the same page's executable `MFI(14)` scan clauses and the MFI page's creator-recommended 14-period default. This record follows the scan-plus-default (14) exclusively; the `MFI(10)` printing is fenced as a different, unpinned rule, never mixed into any leg.
- The page's Parabolic SAR stop suggestion ships with no acceleration, maximum, timeframe, or application rule; the worked RRC example shows a SAR stop triggering, but no parameter is recoverable from any primary source, so no stop leg is pinned here. The `Tweaking` section's MACD-confirmation and ADX<15-regime overlays are explicitly optional refinements ("chartists should consider"), not the system rule — adopting them would specify a different, unverified strategy.
- The scan's `SMA(20,Volume) > 40000` equity-liquidity prefilter is a universe screen, not a signal leg, and is excluded (BTCUSDT venue liquidity is a house-evaluation matter, not a source rule).
- The σ population/sample qualifier, the `MFI = 100` zero-negative-flow boundary, the strict-inequality edge holds, and the degenerate-bar hold above are computation pins stated in Signal — the reviewer can verify each against the cited pages; none invents a threshold, length, or leg.

## Falsification plan

- Recompute %B(20,2.0) and MFI(14) from BTCUSDT `1d` bars with an independent implementation (SMA plus population stdev; Wilder-style money-flow sums, unchanged-TP exclusion, `MFI = 100` on zero negative flow) and verify dual-trigger bars: long only where `%B > 0.80` with MFI crossing up through 80, short only where `%B < 0.20` with MFI crossing down through 20.
- Falsified if: independent recomputation disagrees on signal bars; any order fires on a bar where either gate fails; a flat pre-warmup bar carries a position; any fill requires an intrabar path, a stop/target leg, non-close data, or a second symbol/timeframe.
- Downstream performance screening (house overlay, fees plus historical funding) is out of scope for admission; only event-level rule fidelity matters here.

## Crypto portability

Direct: single-symbol rule with no equity-session, breadth, fundamental, or calendar dependency. Both indicators read standard Binance candle fields (volume included) available point-in-time on the perpetual venue. The short leg ports to the perpetual short permission without rule change; spot-only evaluation would disable the short leg explicitly (a different, long/flat-only evaluation, not covered by this record's two-sided claim).

## Limitations

- Reversal-only exits: no stop, target, trailing, or time exit exists in this record by source construction (the SAR suggestion is parameterless); adverse thrust-failure whipsaws and mid-zone chop are held without guardrail — the page itself names trend failure as the biggest risk.
- Gate sparsity: entries need a fresh MFI extreme cross under a %B thrust state, so long calm or extreme-congestion stretches hold a stale-side position with no re-confirmation leg.
- Thrust-chasing profile: signals print mid-advance/mid-decline by design ("buy strength, sell weakness"), so entries systematically pay the thrust and rely on continuation that may not extend.
- Derivation scope: market/timeframe port, same-bar-close fills, 40-bar warmup, σ/MFI-boundary/edge computation pins, and house economics are researcher-declared (above); the record is a disclosed derivative, not a lossless source reproduction.
- No funding treatment in the source; realized-funding performance cannot be claimed without a verified implementation (house cost assumptions govern downstream evaluation).
- `confidence: medium` reflects interpretation confidence (verbatim rule sentence, executable scan clauses, dual-page default corroboration), not expected profitability.

## Implementation status

`not-implemented` — no Hummingbot controller, no Qlib job, no backtest, no Paper/Testnet/Live artifact exists for this record.

## Adoption boundary

`not-approved`, `research-only`. This record is an admission candidate only: eligible for downstream model-consistent research after independent six-gate review. No trading authorization of any kind is implied or granted.

## Related Wiki records

None — no Wiki Brain write was performed for this Scout cycle.

## Sources

- https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/percent-b-money-flow — canonical primary strategy source (Bollinger-attributed %B+MFI dual-thrust rule, two-sided worked examples, SAR-stop suggestion without parameters); rule sentence and trigger semantics read verbatim this cycle.
- https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/b-indicator — official %B semantics corroboration (%B(20,2) defaults, close input, executable scan clauses with MFI(14) cross semantics).
- https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/money-flow-index-mfi — official MFI semantics corroboration (14-period creator-recommended default, typical-price/money-flow/ratio formulas, 80/20 overbought/oversold levels).
