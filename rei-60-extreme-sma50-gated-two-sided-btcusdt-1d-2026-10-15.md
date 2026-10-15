---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: DeMark REI 60-extreme SMA50-gated reversal two-sided on BTCUSDT 1d bars
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
  - https://support.instaforex.eu/analysis-tools/range-expansion-index
  - https://www.prorealcode.com/prorealtime-indicators/range-expansion-index-rei/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# DeMark REI 60-extreme SMA50-gated reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary sources read end to end (verified 2026-10-15):

- InstaForex support-portal technical documentation, `Range Expansion Index` page, fetched live over HTTPS during this cycle (HTTP 200, 60837 bytes). Attributes the indicator to Thomas DeMark as presented in `The New Science of Technical Analysis (Thomas R. DeMark, John Wiley&Sons, Inc., 1994)` (adopted as `source_as_of: 1994`; the book itself is attribution context, not byte-verified here). Ships the full conditional construction: `S1 = Sum(k, j=1) n(j)m(j)s(j)` with `k` the calculation period (`usually, 8`); the first quiet-market condition (`if ((High[j - 2] < Close[j - 7]) && (High[j - 2] < Close[j - 8]) && (High[j] < High[j - 5]) && (High[j] < High[j - 6])) n(j) = 0, else n (j) = 1`); the mirrored second condition (`if ((Low[j - 2] > Close[j - 7]) && (Low[j - 2] > Close[j - 8]) && (Low[j] > Low[j - 5]) && (Low[j] > Low[j - 6])) m(j) = 0, else m(j) = 1`); the signed leg (`s(j) = High[j]-High[j-2]+Low[j] - Low[j-2]`); the absolute leg (`S(2) = Sum(k, j=1) |High[j]-High[j-2]|+|Low[j] - Low[j-2]|`); and the ratio (`REI = S1/S2*100`). Pins the scale and levels (`fluctuates within the range from +100 to -100 percent`, `values running over +60 mean overbought`, `drops below the -60 level` oversold/rebound-possible, neutral zone `from -60 to +60` on flat markets by developer design). Ships the complete traded scheme with its trend filter: `A short-term position is opened if REI generates the extreme above the +60 level with the price being below SMA (50)` and `A long-term position is opened if REI generates the extreme below the -60 level with the price being above SMA (50)`. Notes `REI_period = 8` and that below-H4 use raises the setting to 12 (untraded scope here — this record keeps 8 on daily bars, see Negative evidence). This record claims no crypto performance and no reproduced performance.
- ProRealCode public indicator library, `Range Expansion Index (REI)` by `Nicolas`, created `May 15, 2020` (page fetched live during this cycle, HTTP 200, 201751 bytes, code block byte-verified inside the page). Independently pins the same construction in executable form: `REIPeriod = 8`; `diff1 = High - High[2]`; `diff2 = Low - Low[2]`; the identical quiet-market pair (`if ((High[2] < Close[7]) and (High[2] < Close[8]) and (High < High[5]) and (High < High[6])) then numzero1 = 0 else numzero1 = 1`, mirrored for `numzero2` on lows); `subvalue = (numzero1 * numzero2 * (diff1 + diff2))`; `AbsDailyValue = Abs(diff1)+Abs(diff2)`; both sums over `for j = 0 to REIPeriod-1`; and the ratio `REI = SubValueSum / AbsDailyValueSum * 100`. Independently pins the `+60`/`-60` dotted levels (`60 style(dottedline)`, `-60 style(dottedline)`), the `8 day timeframe` default, the `-100`/`+100` scale, and the 1994-book attribution (`developed by Thomas DeMark and published in his 1994 book, The New Science of Technical Analysis`). Pins the zero-denominator convention in code: `if (AbsDailyValueSum <> 0) then REI = ... else REI = 0` — the record's governing branch for flat windows, source-pinned, never invented.
- The two constructions are arithmetically identical (per-bar `n*m*signed-range-change` over 8 bars divided by the matching absolute sum, times 100); notation differs, no term differs. No other value in this record comes from any other source.

Licence and rights: this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any source trading system. Researcher-declared adaptations are exactly five: (1) market pin `BTCUSDT` on Binance futures with the source-native daily frame kept (venue transfer plus symbol spelling, futures short permission disclosed here, never presented as source-native); (2) entry-timing pin — the documented `generates the extreme` is evaluated once per completed bar as strict level presence (`REI > +60` / `REI < -60`) with same-bar-close fills (the sources ship the extreme-plus-filter trigger, not a fill convention); (3) exit pin — the sources ship entries and no exit, so the opposite entry-condition print closes and atomically reverses the leg (predeclared here; no stop, no target, no trailing, no time exit, no flat-after-signal — explicitly none, never hidden); (4) an adopted 60-bar warmup with pre-warmup bars flat by record rule (covers the 50-bar SMA plus the 8-bar sums plus the 8-bar condition reach with margin); (5) house sizing/capital/costs replacing the absent source economics (recorded as absent, never as zero-cost evidence; see Execution assumptions). The conditional `n`/`m` pair, the `diff1`/`diff2` legs, the 8-bar sums, the `100 x S1/S2` ratio, the zero-denominator `0` convention, the `+-60` extremes, and the SMA(50) filter side are source-pinned and unmodified elsewhere. **No Safety Order, no DCA event, no pyramiding, and no second leg is admitted in this record's version** — the admitted machine holds exactly one leg; the house BO/SO/SO DCA matrix is a separately declared downstream experiment only (see Adoption boundary). The reviewer is never asked to choose between versions: there is exactly one.

Pre-write dedup (2026-10-15): working-tree case-insensitive fixed-string searches for `Range Expansion`, word-boundary `REI`, and `DeMark` return zero strategy records using this source, author, indicator, or construction (the only `demark` hits are prose mentions inside other records' dedup paragraphs). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closed October-15 Scout PRs #222 (Blau DTI band-latch), #223 (DPO zero-sign latch), #224 (Bufi adaptive RSI), #225 (RMI band-latch) are different oscillators with different arithmetic. Closest pool records are different mechanism classes: `td-sequential-setup9-perfected-long` counts consecutive closes against a 4-bar-offset close with a perfection leg (never reads high/low 2-bar differences, never sums conditional signed ranges, never references `+-60` or any SMA filter); `demarker-threshold-recross-cooldown` accumulates DeMax/DeMin one-bar edges over 13 bars into a bounded ratio (no quiet-market `n`/`m` conditions, no 8-bar window, no SMA(50) gate); `mass-index-threshold-latch-reversal` sums EMA ratios of the raw high-low range over 25 bars (reads no close at all, has no signed legs and no absolute-sum denominator); every breakout-geometry record (`donchian-20-10-breakout`, `darvas-box-breakout`, `nr7-price-breakout`, `inside-bar-failure-fade`, `r-breaker-7-level`, `dual-thrust-open-range`) trades raw rolling extremes or opening ranges (never a conditional signed-range sum ratio against fixed `+-60` with an SMA(50) side filter). No pool record computes `100 x sum(n*m*(dH+dL),8) / sum(|dH|+|dL|,8)` or gates `+-60` extremes on SMA(50). Shared `momentum-oscillator` wording or shared high/low inputs are not shared signal.

## Economic mechanism

### Source-reported

Quiet-market-gated range-expansion acceptance with trend-filtered extremes: each bar's 2-bar high/low changes are signed, but bars that the `n`/`m` conditions flag as trendless (higher highs absent against week-ago closes and 5/6-bar highs, mirrored on lows) contribute exactly zero to the numerator while still contributing their absolute motion to the denominator — so sideways chop actively dilutes the print toward neutral instead of merely pausing it. The 8-bar ratio reads which side owned the accepted expansion; beyond `+60` with price below its 50-day average the record opens the short side, below `-60` with price above its 50-day average it opens the long side. The SMA(50) gate keeps extremes from firing against the mid-term trend. There is no source exit: this record's opposite-extreme reversal is the predeclared derived completion.

### Research interpretation

Single-series bounded-oscillator system, two-sided, always-in-position after the first signal, with the `+-60` extreme pair as the only trigger and SMA(50) as the only gate. Unlike plain range-sum oscillators (Mass Index, which never reads a close and never gates on trend), this rule multiplies every bar by a binary trend-acceptance switch computed from week-old closes and 5/6-bar extremes, so the numerator is a *qualified* expansion sum while the denominator stays unqualified — the print is acceptance-weighted, not raw. Unlike close-to-close RSI records, inter-bar gaps enter only through the `n`/`m` comparisons (week-ago closes) and never through the summed legs (which are pure high/low differences). Unlike Qstick/IMI body machines, the rule reads no open at all. The price of the always-in posture is indefinite adverse rides plus alternating-extreme whipsaw when both zones print in turn; a leg whose opposite condition never prints (extreme without the SMA side, or no extreme at all) is held forever. The bet is on accepted range-expansion persistence confirmed by mid-term trend side, not on any price pattern, second oscillator, volume read, calendar effect, or volatility read.

## Signal

Exact rule as pinned (all inputs frozen — any other value is a different, unpinned rule):

- Declarations (derived): single-position state machine over `BTCUSDT 1d` with same-bar-close execution and house sizing/costs (see Execution assumptions). At most one open leg; state ∈ {flat, long, short}; flat exists only before the first signal and under the warmup rule. No Safety Order, no DCA event, no pyramiding — explicitly none admitted here, not invented.
- Range legs, pinned verbatim at defaults (`k = REIPeriod = 8`): with `H(t)`, `L(t)`, `C(t)` of completed bar `t`: `diff1(t) = H(t) - H(t-2)`; `diff2(t) = L(t) - L(t-2)`. Quiet-market switches: `n(t) = 0` iff `H(t-2) < C(t-7)` and `H(t-2) < C(t-8)` and `H(t) < H(t-5)` and `H(t) < H(t-6)`, else `1`; `m(t) = 0` iff `L(t-2) > C(t-7)` and `L(t-2) > C(t-8)` and `L(t) > L(t-5)` and `L(t) > L(t-6)`, else `1`. Signed leg `sub(t) = n(t) x m(t) x (diff1(t) + diff2(t))`; absolute leg `a(t) = |diff1(t)| + |diff2(t)|`. Both sources agree term for term; the `j = 0 to REIPeriod-1` loop and the `Sum(k, j=1)` window are the same 8-bar window.
- Indicator, pinned verbatim: `S1(t) = sum(sub, 8)(t)` over completed bars `t-7..t`; `S2(t) = sum(a, 8)(t)` over the same window; `REI(t) = 100 x S1(t) / S2(t)` when `S2(t) <> 0`, else `REI(t) = 0` by the source-pinned ProRealCode branch (a fully-flat 8-bar window resolves to neutral, never to `NaN` trading — fenced in Negative evidence).
- Trend gate, pinned verbatim: `SMA50(t)` = plain mean of `C(t-49..t)`.
- Entry short: on bar `t` with `REI(t) > +60` strictly and `C(t) < SMA50(t)` strictly (extreme above `+60` with price below SMA(50); from flat: open short; from long: atomic reversal — close long plus open short as a single reversal event). Same-side reprints while short are no-ops (no adds — explicitly none admitted).
- Entry long: mirror on `REI(t) < -60` strictly and `C(t) > SMA50(t)` strictly.
- Exact-touch determinism, pinned by the strict source comparatives (`above` / `below`): `REI == +60`, `REI == -60`, and `C == SMA50` satisfy neither leg and change nothing — disclosed, not oversold as tolerance.
- Exits: the opposite entry-condition print only (predeclared derived completion — the sources ship no exit). No stop, no target, no trailing, no time exit, no cooldown, no flat-on-neutral-return — explicitly none by record rule, not invented, forming a complete always-in machine after the first signal. A positioned leg whose opposite condition never prints is held indefinitely.
- Direction: two-sided with an explicit pre-first-signal flat state (plus the 60-bar warmup flat by record rule). The documented scheme prescribes both the short and the long leg; a single-sided reading would contradict it.

## Required data

- Completed `1d` bars of BTCUSDT: `high` (2-bar differences plus `n`-condition reads), `low` (2-bar differences plus `m`-condition reads), `close` (week-ago condition reads plus SMA(50) plus gate side) — Binance USDT-M futures by record pin (see Limitations). No `open`, no volume, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (the documented 8-day construction is frame-faithful on daily bars; the below-H4 12-bar setting is real source content deliberately not carried here — see Negative evidence; the rule references no other frame, no multi-timeframe input — single-frame by construction).
- Warmup: the binding costs are the 50-bar SMA (first fully-formed value needs 50 completed bars), the 8-bar sums, and the condition reach (deepest read `C(t-15)` via the summed `t-7` bar's `C-8`). The adopted warmup is the first 60 completed `1d` bars flat by record rule (predeclared researcher choice — covers the SMA plus sums plus reach with margin). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Every input is complete at bar `t`'s close — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (frame-faithful `1d`; venue choice, symbol spelling, and short permission disclosed in Provenance, never presented as source claims).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) — the same verified execution primitive as the admitted `qstick-zero-cross-trend-two-sided-btcusdt-1h` and `imi-50-midline-cross-flip-two-sided-btcusdt-1d` PASS records (single-frame completed-bar decision, same-bar-close market fill, single-position machine, no stop/limit legs anywhere, hence no same-bar TP/SL ordering ambiguity; each trigger reads only completed bars, so each bar's outcome is a single deterministic event: hold, open, or atomic reversal). No maker-touch, queue, multi-asset sync, lower/multi-timeframe alignment, non-OHLCV input, or intrabar-path-dependent fill is required by any line of this record.
- Sizing/capital/costs: the sources ship no portable economics (zero commission/quantity assumption — recorded as absent economics, never as zero-cost evidence) — derived evaluation carries the fixed, reproducible house research cost model (Base 6% + Safety 6% + Safety 6% notional framing, Isolated, 3x/5x; pinned house cost assumptions for fees plus modeled funding — no hypothetical zero funding claimed, never presented as source-native behavior). Funding is modeled, never reported as realized or canonical funding; no historical-funding settlement path is required or claimed for this version. No Safety-Order/DCA event participates in the admitted trigger machine regardless of downstream campaign settings.
- Concurrency: single-position machine — at most one open leg; same-state bars while positioned are no-ops; the opposite entry condition reverses in full (one atomic event); re-entry is allowed on the next fresh opposite print after any close (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The sources ship the full conditional construction (`n`/`m` quiet-market conditions, `diff1`/`diff2` 2-bar legs, 8-bar signed and absolute sums, `REI = S1/S2*100`), the zero-denominator `0` convention (ProRealCode branch), the `-100`/`+100` scale, the `+60`/`-60` extreme levels, the neutral `+-60` band design, the SMA(50) filter scheme with both legs (short above `+60` with price below SMA(50); long below `-60` with price above SMA(50)), the `REI_period = 8` default, and the DeMark 1994-book attribution — quoted in Provenance. Neither source ships a backtest table for this construction, so this record carries zero source-reported performance numbers and claims no performance of any kind.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No performance to carry, admitted plainly: unlike paper-sourced records with backtest tables, both rule sources ship construction, levels, filter scheme, and code only — there is no expectancy number anywhere to fence, and this record claims none.
2. Untraded source content fenced, admitted plainly: the below-H4 `12`-bar setting is a real documented recommendation deliberately not carried here (this record is daily bars at 8 by record rule); carrying it would be a different, unpinned rule. The neutral-band design note is context, never a trigger.
3. No hidden exits or risk layer: the traded machine names no stop, no target, no trailing, no time exit, no neutral-return flat anywhere — the no-stop/no-target posture is the record rule, explicitly none, never hidden. Every adverse excursion is held to the opposite entry-condition print.
4. Trigger exclusivity proved: the short leg requires `C(t) < SMA50(t)` and the long leg requires `C(t) > SMA50(t)` — no bar satisfies both, so no bar fires both transitions and no priority rule is needed or invented. (A single bar can print an extreme on either side, but then exactly one leg's SMA side can hold.)
5. Exact-touch determinism fenced: `REI == +-60` and `C == SMA50` change nothing by the pinned strict comparatives (measure-zero on continuous prints — disclosed, not oversold as tolerance). The `S2 == 0` window resolves to the source-pinned `REI = 0` print, which satisfies neither leg and therefore holds the prior state deterministically.
6. Quiet-bar determinism fenced: when both switches read `0`, `sub(t) = 0` while `a(t)` still accumulates — chop dilutes the numerator by construction under both sources, no bar leaves either sum undefined, no switch invented.
7. Gaps bounded, stated plainly: the summed legs read only high/low 2-bar differences; inter-bar jumps enter no sum — only the `n`/`m` week-ago-close comparisons can see across bars, exactly as documented, never as an extra gate.
8. No future leakage in the stack, stated plainly: at decision bar `t`, sums read completed bars `t-7..t` with deepest raw read `C(t-15)`, the SMA reads `t-49..t`, and both triggers compare prints of bar `t` only — every input is complete at bar `t`'s close. No multi-frame read, no negative index, no full-sample normalization, no repainting path, no calendar read at all.
9. Oscillator-family overlap fence, admitted plainly: the pool's TD Sequential record counts closes against a 4-bar offset (no high/low reads, no sums, no ratio); the DeMarker record ratios one-bar DeMax/DeMin edges over 13 bars (no quiet-market switches, no 8-bar window, no SMA gate); the Mass Index record sums EMA ratios of raw ranges (reads no close, has no signed legs); breakout-geometry records trade raw extremes (never a conditional sum ratio). This record's `100 x qualified-signed-range-sum / absolute-range-sum` with dual `+-60` extremes and an SMA(50) side gate exists nowhere else in the pool. Shared `oscillator` wording or shared high/low inputs are not shared signal.
10. Two-sided posture provably complete: symmetric `+60`-below-SMA50 short / `-60`-above-SMA50 long legs with symmetric atomic-reversal exits under the documented scheme — no third direction exists, and a single-sided reading would contradict the printed opposite leg.
11. Derivation boundary fenced: the only non-source-native behaviors in this record are the `BTCUSDT` futures market pin with the source-native daily frame kept, the per-completed-bar strict-presence evaluation with same-bar-close fills, the opposite-print reversal exit, the adopted 60-bar warmup with record-rule pre-warmup flat, and house sizing/costs with no admitted Safety-Order/DCA event — all predeclared above; the `n`/`m` conditions, the legs, the 8-bar sums, the ratio, the zero-denominator `0`, the `+-60` extremes, the SMA(50) gate sides, the single-position guards, and the risk posture are source-pinned or predeclared. This record is therefore never evidence that any other market, frame, period, level set, filter length, or timing of the source passes.
12. Conflicting composite fenced, admitted plainly: a public TradingView user idea on a five-oscillator TD Alignment composite was read during this cycle and is NOT used anywhere in this record — it scores REI inside a `-5..+5` composite against `40`/`-40` internal bands for a different strategy, and its author discloses possible calculation errors. The standalone-REI rule sources both pin `+-60`; carrying composite bands onto this record would be fabrication.
13. Division of evidence disclosed: the formula, legs, conditions, period, scale, levels, filter scheme, and book attribution above were byte-verified in the fetched InstaForex page (60837 bytes, HTTP 200) and cross-checked term-for-term against the fetched ProRealCode page and its code block (201751 bytes, HTTP 200, Nicolas, 2020-05-15). The division of evidence is disclosed here, not hidden.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: conditional `n`/`m` pair / 2-bar high/low legs / 8-bar sums / `100 x S1/S2` ratio with source-pinned zero-`0` / strict `+-60` extremes with SMA(50) side gate / opposite-print atomic reversal / no-stop-no-target posture / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Level relevance: replacing the `+-60` extremes with the composite-style `+-40` bands (same period, same gate, same state machine, same reversal handling) must not improve net expectancy; fail ⇒ the documented extremes add nothing over the composite's internal bands.
- F2 — Filter relevance: removing the SMA(50) side gate (pure `+-60` extreme flip, same entries mirrored without trend side) must not improve net expectancy; fail ⇒ the mid-term trend gate adds nothing over raw extremes.
- F3 — Posture relevance: exiting to flat on return inside `+-60` instead of atomic reversal on the opposite print (same entries, same gate, flat between extremes) must not improve net expectancy; fail ⇒ the always-in alternation adds nothing over a flat-resting variant.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (frame-faithful `1d`; venue transfer disclosed). The rule reads only completed daily highs, lows, and closes, so no volume-series or open-print differences can touch any order-gating line — but spot-vs-perp high/low/close prints can still differ structurally (funding-driven drift, venue aggregation, anomalous wicks that flow straight into `diff1`/`diff2`), so the futures-venue pin is load-bearing and disclosed. The ratio is unit-free and the extremes plus SMA length are fixed constants, so no fixed-pip recalibration is needed across assets — cross-asset behavior differences are still real and unclaimed. The rule is two-sided with no stop leg, so a spot-only deployment expresses the long state and reversal mechanics only to the extent the venue permits shorting — full two-sided expression assumes a futures venue, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read beyond each calendar-day bar's own high/low/close (no session gating anywhere); decision boundaries are calendar-day bars of the venue feed, disclosed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived market pin: the sources describe daily stock/forex bars; this record pins `BTCUSDT` futures `1d`. Cross-market and spot-vs-perp high/low/close behavior differences are real — the venue transfer is disclosed, and this record makes no claim about any other market or the sources' native venue.
- Untested trigger scope: the only source-documented scheme carried here is the SMA(50)-gated `+-60` extreme pair; the below-H4 12-bar setting and the neutral-band design note are performance-unclaimed context, and the pinned pair itself carries no expectancy claim until downstream research measures it.
- No source economics: the sources ship no commission, sizing, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- No price stop, no time stop: adverse excursion after entry has no guardrail beyond the opposite entry-condition print; a leg whose opposite condition never prints is held indefinitely. This is the record-rule posture, disclosed as a principal risk.
- Alternating-extreme whipsaw: consecutive opposite extremes print repeated reversal pairs with no flat state to rest in, by the prescribed always-in design. The extreme-presence construction is the documented trigger, disclosed, not smoothed.
- Wick sensitivity: venue high/low prints (rolls, aggregation, anomalous wicks) flow straight into both legs and both switch conditions; a venue that cannot supply trustworthy per-bar highs, lows, and closes cannot trade the pinned rule.
- Warmup cost: the SMA needs 50 completed bars plus sums plus condition reach; the adopted 60-bar warmup absorbs this structurally with wide margin, and the first 60 bars are flat by record rule.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior and never part of this admission — no Safety-Order/DCA event is admitted in this record's version. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- InstaForex support-portal technical documentation, Range Expansion Index (REI) — conditional n/m construction, 8-bar sums, S1/S2 ratio, +-100 scale, +-60 extremes, SMA(50) filter scheme, REI_period 8, DeMark 1994-book attribution (verified live in the fetched page during this cycle; zero crypto claims): https://support.instaforex.eu/analysis-tools/range-expansion-index
- ProRealCode public indicator library, Range Expansion Index (REI) by Nicolas (2020-05-15) — independent executable pin of the same conditional construction, REIPeriod 8, +-60 dotted levels, zero-denominator 0 convention, 1994-book attribution (verified live in the fetched page and code block during this cycle): https://www.prorealcode.com/prorealtime-indicators/range-expansion-index-rei/
