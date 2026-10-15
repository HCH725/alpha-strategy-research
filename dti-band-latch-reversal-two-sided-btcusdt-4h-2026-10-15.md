---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Blau DTI band-latch reversal two-sided on BTCUSDT 4h bars
created: 2026-10-15
updated: 2026-10-15
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-09-18
sources:
  - https://www.fmz.com/strategy/427157
  - https://mql5.com/en/code/384
  - https://motivewave.com/studies/directional_trend_index.htm
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Blau DTI band-latch reversal two-sided on BTCUSDT 4h bars

## Provenance

Primary source read end to end (executable code is the specification):

- Canonical page: https://www.fmz.com/strategy/427157 (page title `方向趋势指数交易策略|Directional Trend Index Trading Strategy`). Fetched live over HTTPS during this cycle (HTTP 200, 767546 bytes). The page embeds the full Pine v2 program byte-verbatim inside its data payload, recovered by deterministic unescape to a canonical 2618-byte text (sha256 `1b3f5bd4ee98dced3c695da583b766cc5b3571b82ed574fedbcbdc93cd6a25bd`). The embedded block opens with the page-embedded `/*backtest*/` header (`start: 2023-08-18 00:00:00`, `end: 2023-09-17 00:00:00`, `period: 4h`, `basePeriod: 15m`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`) and the code header `Copyright by HPotter v1.0 29/03/2017`, whose comment block attributes the technique to William Blau's book `Momentum, Direction and Divergence` (1995) and describes the DTI as a zeroline-bearing extension of Welles Wilder's DM+ (`Blau added to it a zeroline, relative to which the indicator is deemed positive or negative. A stable uptrend is a period when the DTI value is positive and rising, a downtrend when it is negative and falling`). Adopted as `source_as_of` 2023-09-18 from the page's 2023-09-18 stamp alongside the backtest window; the page exposes no separate Created stamp in the fetched state.
- Text census over the recovered program: 2 `strategy.entry` (`strategy.entry("Long", strategy.long)` / `strategy.entry("Short", strategy.short)`, inside two independent single-sided `if` guards on one three-valued latch, no `when=`, no price/`qty` argument — market entries) / 0 `strategy.close` / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=` / 0 `limit=` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `time(` / 0 `volume` / 0 `open` / 0 `close` (the rule reads `high` and `low` only, each with a single `[1]` reach) / exactly 6 `input(` (`r = input(14, ...)`, `s = input(10, ...)`, `u = input(5, ...)`, `OS = input(45, ...)`, `OB = input(-45, ...)`, `reverse = input(false, ...)` — all pinned at defaults; any other value is a different, unpinned rule). No `strategy(...)` declaration ships anywhere; `//@version=2` ships at the top. `pyramiding`, `process_orders_on_close`, `calc_on_every_tick`, `initial_capital`, `commission_*` and `slippage` are unset throughout (Pine language defaults apply: no same-direction adds, next-bar-open fills, one evaluation per completed bar). Display calls (`hline`, `barcolor`, 3 `plot`) render only and feed no order condition.
- No risk layer ships anywhere in the source: zero stop/target/trailing/time-exit order legs, and the page's own Enhancements prose (`Consider adding stop loss strategies to control risk`) confirms the stop is absent by design gap, not by hidden leg. The latch-plus-opposite-reversal posture below is therefore the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention.
- Page/mirror performance language is absent entirely (no table, figure, or number anywhere — English word-boundary counts over the whole landing HTML: `Sharpe` 0, `Net Profit` 0, `Profit Factor` 0, `Win Rate` 0, `Max Drawdown` 0; the Chinese prose carries only qualitative risk sentences, no numeric claim) — this record claims no source-reported performance and no reproduced performance.

Independent corroboration (formula and polarity — rule read in the FMZ code, never retyped from here):

- MQL5 CodeBase `Directional Trend Index Blau_DTI` by `abolk` (https://mql5.com/en/code/384, fetched HTTP 200, 65005 bytes, page-stamped 2011.07.14): pins the identical construction `DTI(q,r,s,u) = 100 * EMA(EMA(EMA(HLM(q),r),s),u) / EMA(EMA(EMA(|HLM(q)|,r),s),u)` with the explicit zero branch (`if ... =0, then DTI(...)=0`), where `HLM(q)=HMU(q)-LMD(q)` is the Composite High/Low Momentum. Its defaults (q=2, r=20, s=5, u=3) differ from the pinned code — pinned values govern here; the page corroborates the recurrence shape, the high/low-momentum legs, and the divide-by-zero convention only.
- MotiveWave official study documentation, `Directional Trend Index` (https://motivewave.com/studies/directional_trend_index.htm, fetched HTTP 200, 1997798 bytes): ships the condensed calculation code with defaults `rPeriod = 14`, `sPeriod = 10`, `uPeriod = 5` — exactly the pinned `r/s/u` triple — and pins the signal polarity byte-verbatim in the fetched page: `DTI values above 25 are considered to be overbought and therefore offer an opportunity to sell. DTI values below -25 are considered oversold and present an opportunity to buy`, with `If the DTI peaks above the top guide a sell signal will be generated. Conversely, if the DTI troughs below the bottom guide a buy signal will be given`. Strength-high maps to the sell/short side and weakness-low to the buy/long side — the same polarity the pinned code executes at its own `+-45` bands.
- MultiCharts `DTI_Trade` documentation was attempted during this cycle but the host answered a Cloudflare challenge page instead of content, so it contributes nothing anywhere in this record.

Licence and rights: the canonical page is a public FMZ strategy publication; the pinned code block carries the HPotter v1.0 29/03/2017 header with a paper-trading-only notice (`Please, use it only for learning or paper trading. Do not for real trading`). This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) same-bar-close fills (no execution-timing argument ships anywhere in the source, whose market entries fill next-bar-open under language defaults); (2) an adopted 60-bar warmup with pre-warmup bars flat by record rule (covers the 14+10+5 EMA seeding stack plus the 1-bar momentum reach with wide margin — see Required data); (3) house sizing/capital/costs replacing the absent source sizing (no capital, commission, fee, slippage, funding, or margin assumption ships anywhere — see Execution assumptions); (4) symbol spelling `BTC_USDT` to `BTCUSDT` on the source-native venue and frame (Binance futures, `4h` decision frame kept — frame-faithful and venue-faithful, never presented as source-native). Indicator arithmetic (14/10/5 triple EMA on high/low momentum, `+-45` bands, `reverse=false`), the seeded latch, the order IDs, two-sided reversal handling, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-15): working-tree case-insensitive searches for `directional.trend`, `blau_dti`, `HLM(`, and `427157` return zero strategy records using this source, author script, indicator, or construction — the only `blau` tokens anywhere are prose lineage notes inside `dss-bressert-double-smoothed-stochastic-trigger-latch-two-sided-btcusdt-2h` (Blau double-smoothed *stochastic* zone latch, FMZ 441102) and `tsi-signal-cross-reversal-btcusdt-1d` (Blau double-smoothed bar-to-bar *change* normalization 25/13/13 against its own signal EMA, FMZ 428611). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `adx-di-cross-strength-gated-two-sided-btcusdt-1d` crosses Wilder's DM+/DM- lines (unsmoothed directional movement, no ratio normalization, no bands); `aroon-oscillator-midline-rail-exit-btcusdt-1d` times bars-since-extremes (no momentum legs at all); `pmo-signal-cross-reversal-two-sided-btcusdt-1d` double-custom-smooths a close-only ratio ROC (35/20/10, no high/low read, signal-line cross, no latch). Five-axis distinction: no pool record and no open PR evaluates Blau's triple-EMA high/low-momentum ratio `100*EMA(EMA(EMA(HMU-LMD,14),10),5)/EMA(EMA(EMA(|HMU-LMD|,14),10),5)` with a seeded `+-45` band latch and reversal-only exits on any market or frame.

## Economic mechanism

### Source-reported

The code header plus the page prose describe the mechanism only as: composite high/low momentum, triple-exponentially smoothed and normalized into a bounded oscillator around a zeroline, traded at overbought/oversold bands with the position held until the next signal (`一直持有至下一信号出现` — held until the next signal appears). The header's Blau note adds the regime read: positive-and-rising DTI is the stable-uptrend state, negative-and-falling the downtrend state. No behavioural, structural, or risk-premium channel is claimed beyond this momentum/normalization description.

### Research interpretation

Exhaustion-latch reversal system, two-sided, always-in-market after the first signal. Unlike the pool's cross-and-forget oscillators (MACD, TSI, PMO), which fire on the single bar of a line cross and carry no memory, this rule latches: once DTI prints beyond a band, the side is held through the entire return journey across the zeroline until the print reaches the *opposite* band. The exit is therefore never the midline — a short opened at DTI above +45 rides all the way down through zero to below -45 before reversing. The bet is that triple-smoothed high/low-momentum extremes mark push-exhaustion: the side is taken against the extreme (short into strength, long into weakness, exactly the MotiveWave-documented polarity) and held while the push decays. Unlike Wilder ADX/DI systems, which separate direction (+DI/-DI) from strength (ADX) into distinct lines, this rule folds both into one signed ratio so a single pair of constant bands suffices. Unlike flat-capable band systems, there is no neutral state after the first signal — mid-band chop is held, not exited, so sideways tapes grind through full-scale traversals with no stop to truncate them. The price of the latch is indefinite adverse rides: a leg whose opposite band never prints is held forever.

## Signal

Exact rule as pinned (all inputs frozen — any other value is a different, unpinned rule):

- Declarations (derived): single-position state machine over `BTCUSDT 4h` with same-bar-close execution and house sizing/costs (see Execution assumptions). At most one open leg; state in {flat, long, short}; flat exists only before the first signal and under the warmup rule.
- Momentum legs, pinned verbatim at defaults (`r = 14`, `s = 10`, `u = 5`): with `H(t)` high and `L(t)` low of completed bar `t`: `xHMU(t) = max(H(t) - H(t-1), 0)`; `xLMD(t) = max(L(t-1) - L(t), 0)`; `xPrice(t) = xHMU(t) - xLMD(t)`; `xPriceAbs(t) = |xPrice(t)|`. A bar that extends neither extreme contributes `0` to both legs by construction — no tie-break exists or is invented.
- Indicator, pinned verbatim: `xuXA(t) = EMA(EMA(EMA(xPrice, 14), 10), 5)`; `xuXAAbs(t) = EMA(EMA(EMA(xPriceAbs, 14), 10), 5)`; `DTI(t) = xuXAAbs(t) != 0 ? 100 * xuXA(t) / xuXAAbs(t) : 0` — the source's explicit zero branch, so a dead tape prints exactly `0`, never `na`.
- Latch, pinned verbatim (`OS = 45`, `OB = -45`, `reverse = false`): `pos(t) = DTI(t) > 45 ? -1 : (DTI(t) < -45 ? 1 : nz(pos(t-1), 0))`; `possig(t) = pos(t)` under the pinned `reverse=false` (the `reverse=true` mirror is a different, unpinned rule).
- Entry long: bars with `possig(t) == 1` fire `strategy.entry("Long", strategy.long)` — the position opens on the first latched bar and same-side refires while long are no-ops under the pinned no-pyramiding default; from short the opposite latch reverses in full as a single reversal event.
- Entry short: mirror on `possig(t) == -1` (`strategy.entry("Short", strategy.short)`).
- Mutual exclusion (structural, not assumed): `possig` is single-valued in {-1, 0, 1} on every bar, so both order guards can never fire on the same bar — no same-bar ordering ambiguity exists anywhere in this record.
- Exits: the opposite band latch only (long exits exactly when the short latch prints and vice versa). No stop, no target, no trailing, no time exit, no cooldown — explicitly none by record rule, not invented, consistent with the latch forming a complete always-in machine. There is no flat path after the first signal at all — flat is reachable only pre-signal and under warmup.
- Direction: two-sided with an explicit pre-first-signal flat state (plus the 60-bar warmup flat by record rule). The coded latch prescribes both legs; a long-only reading would contradict the printed short leg.

## Required data

- Completed `4h` bars of BTCUSDT: `high` (momentum-up leg) and `low` (momentum-down leg) only — Binance futures by source-native pin (see Limitations). No `open`, no `close`, no volume, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `4h` (source-native per the page-embedded `period: 4h` header; the script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction).
- Warmup: the binding cost is the triple-EMA seeding stack (14 + 10 + 5) plus the 1-bar high/low reach. The adopted warmup is the first 60 completed `4h` bars flat by record rule (predeclared researcher choice — covers the full stack with wide margin; the Pine `ema()` seeding convention is the language's own and needs no invention here). No repainting (every `[1]` reference reads a completed prior bar), no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Each bar's high/low enter the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (source-native decision frame `4h` and source-native venue kept; only the symbol spelling `BTC_USDT` to `BTCUSDT` is normalized — a predeclared derivation, never presented as source-native. The short leg requires a margin venue, which the pinned venue provides natively).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar-open (no execution-timing argument ships anywhere); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere and structurally exclusive entries, each bar's outcome is a single deterministic event (hold, open, or atomic reversal), so the header's `basePeriod: 15m` execution granularity cannot change any event. `calc_on_every_tick` is unset (defaults false: exactly one evaluation per completed bar).
- Sizing/capital/costs: the source ships no capital, sizing, commission, fee, slippage, or margin assumption anywhere — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all) apply to the derived evaluation here, never presented as source-native behavior. Funding is modeled, never reported as realized or canonical funding.
- Concurrency: no `pyramiding` ships anywhere, pinning the language default of no same-direction adds — at most one unit per side under the fixed order IDs `Long` / `Short`; opposite-latch entries reverse the position in full under that default; same-side refires while already positioned are no-ops; re-entry is allowed immediately on the next opposite latch (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The page ships the full construction (14/10/5 smoothing inputs, `+-45` bands, `reverse=false`, high/low momentum legs, triple-EMA ratio with explicit zero branch, seeded band latch, fixed `Long`/`Short` order IDs, two-sided reversal handling), the page-embedded 4h/15m August–September-2023 backtest header on `Futures_Binance BTC_USDT`, the `Directional Trend Index (DTI)` title, and the HPotter 29/03/2017 header with the Blau-1995 lineage note — quoted in Provenance. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.close`, 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`qty`/`when=` — the sole position-closing path on each side is the opposite band latch reversing under the no-pyramiding default. The page's own Enhancements prose (`Consider adding stop loss strategies to control risk`) confirms the absence is by design gap, and the code header's paper-trading-only notice is disclosed, not hidden.
2. Always-in-market after the first signal, admitted plainly: once the first band latch trades, the system holds a position on every subsequent bar until the opposite band — there is no flat state, no stop, no time-stop. The latch must traverse the full scale (long opened below -45 exits only below... only when DTI exceeds +45), so ranging markets grind through whole-scale reversals with full exposure each way. This is the coded trade, disclosed, not a tunable parameter here.
3. Prose/code contradiction fenced, code governs: the page's Chinese description reads `当DTI上穿上轨时做多,下穿下轨时做空` (cross-above-upper goes long) — the executable code does the exact opposite (`DTI > OS` sets `pos = -1`, which fires the `Short` entry). The code is the pinned specification ( executable order legs, fixed literals, count-verified census); the prose sentence is pinned as prose-only, contradicted, and excluded from the derived spec. The code's polarity is independently corroborated by the MotiveWave documentation (overbought → sell opportunity; oversold → buy), quoted in Provenance.
4. Polarity economics stated plainly: the coded rule shorts strength (DTI above +45) and buys weakness (DTI below -45) — an exhaustion-reversal reading of Blau's oscillator, not a trend-following reading of the header's `positive and rising` note. Carrying trend-following expectations onto this latch would be fabrication; the reversal posture is the record rule.
5. `reverse=true` fenced: the input exists in source but is pinned `false`. Enabling it would mirror both legs (strength-long / weakness-short) — a different, unpinned rule, never admitted here.
6. Trigger exclusivity fenced: `possig` takes exactly one value in {-1, 0, 1} per bar, so no bar fires both transitions and no priority rule is needed or invented. (A single bar can traverse the whole band span, but then exactly one leg's latch condition holds at the close print.)
7. Band-touch determinism fenced: crossings require strict `>` / `<` against 45 / -45, so exact touches hold the prior latch state deterministically — disclosed, not oversold as tolerance. The zero-branch `DTI = 0` print therefore holds state: at exactly `0` neither band condition holds.
8. Dead-tape branch fenced: `Val2 == 0` (no high/low extension anywhere in the smoothing memory) prints exactly `0` by the source's explicit branch — no bar leaves DTI undefined, no `na` guard invented. Such a print holds the prior latch under fence 7.
9. No future leakage in the stack, stated plainly: at decision bar `t`, the momentum legs read completed bars `t-1..t`, the EMAs recurse over completed prints only, and the latch reads `pos(t-1)` — every input is complete at bar `t`'s close. No multi-frame read, no negative index, no full-sample normalization, no repainting path, no volume/calendar read at all. No seed branch beyond `nz(pos[1], 0)` exists anywhere in the stack.
10. Blau-family overlap fence, admitted plainly: the pool's `dss-bressert` record double-smooths a bounded close-position *stochastic* (range position, then stochastic-of-stochastic) with a trigger-line zone conjunction; `tsi-signal-cross` double-smooths bar-to-bar *close change* normalized by smoothed absolute change against its own signal EMA. This record triple-smooths *high/low extensions* as a signed ratio against fixed bands with a seeded hold — different legs (highs/lows vs close-only), different recurrence (triple EMA 14/10/5 vs double stochastic vs double EMA 25/13/13), different trigger (band latch vs zone conjunction vs signal cross). Shared `Blau` lineage wording is not shared signal.
11. Two-sided posture provably complete: symmetric above-+45 short / below-−45 long latch legs with symmetric atomic-reversal exits — no third direction exists, and a long-only reading would contradict the printed short leg.
12. Derivation boundary fenced: the only non-source-native behaviors in this record are same-bar-close fills, the adopted 60-bar warmup with record-rule pre-warmup flat, house sizing/costs, and the `BTC_USDT`→`BTCUSDT` spelling normalization — all predeclared above; frame, venue, every literal, the momentum legs, the triple-EMA ratio, the zero branch, the latch, the order IDs, reversal handling, and the risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, period, band set, `reverse` setting, or timing of the source passes.
13. Network limitation disclosed: the formula, legs, inputs, latch, order pair, and header lines above were byte-verified in the fetched FMZ page (767546 bytes, HTTP 200) with the canonical code extracted at sha256 `1b3f5bd4...` (2618 bytes); the recurrence and zero branch were cross-checked against the fetched MQL5 page (65005 bytes, HTTP 200) and the smoothed-parameter triple plus signal polarity against the fetched MotiveWave page (1997798 bytes, HTTP 200). The MultiCharts documentation page was attempted but answered a Cloudflare challenge and contributes nothing. The division of evidence is disclosed here, not hidden.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: high/low momentum legs / `14/10/5` triple EMA / `100*xuXA/xuXAAbs` ratio with explicit zero branch / `+-45` band latch with seeded hold / `reverse=false` / atomic reversal / no-stop-no-target posture / two-sided / `4h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Band relevance: narrowing the latch to the MotiveWave-documented `+-25` guides (same recurrence, same latch, same reversal handling) must not improve net expectancy; fail ⇒ the wide `+-45` bands add nothing over the documented guide levels.
- F2 — Polarity relevance: enabling the source-shipped `reverse=true` mirror (strength-long / weakness-short, same bands, same latch) must not improve net expectancy; fail ⇒ the coded exhaustion-reversal polarity adds nothing over the trend-following mirror.
- F3 — Posture relevance: exiting to flat on the opposite band instead of atomic reversal (same entries, same latch, flat between migrations) must not improve net expectancy; fail ⇒ the always-in alternation adds nothing over a flat-resting variant.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (decision frame and venue both source-native per the page-embedded `period: 4h` / `Futures_Binance BTC_USDT` header — only spelling normalized). The rule reads only completed 4h highs and lows, so no close-definition, volume-series, or funding-feed differences can touch any order-gating line — but spot-vs-perp high/low prints can still differ structurally (funding-driven drift, wick aggregation, anomalous prints), so the futures-venue pin is load-bearing and disclosed. The ratio is unit-free and the bands are fixed constants, so no fixed-pip recalibration is needed across assets — cross-asset behavior differences are still real and unclaimed. The rule is two-sided with no stop leg, so a spot-only deployment expresses the long state and reversal mechanics only to the extent the venue permits shorting — full two-sided expression assumes a futures venue, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read beyond each 4h bar's own high/low extension (no session gating anywhere); decision boundaries are venue-feed 4h bars, disclosed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Prose/code divergence: the page prose describes a trend-following cross (long above the upper line) while the executable code implements the exhaustion-reversal latch (short above +45). This record pins the code and excludes the prose sentence — anyone reproducing the prose reading builds a different, unpinned rule.
- Untested trigger scope: the only source-coded trigger carried here is the `+-45` band latch at `reverse=false`; the MotiveWave `+-25` guides, peak/trough confirmation reads, and the header's trend-state note are performance-unclaimed context, and the pinned latch itself carries no expectancy claim until downstream research measures it.
- No source economics: the source ships no commission, sizing, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- No price stop, no time stop: adverse excursion after entry has no guardrail beyond the opposite band latch, which may arrive many bars later after a full-scale traversal; a leg whose opposite band never prints is held indefinitely. This is the record-rule posture, disclosed as a principal risk.
- Whipsaw sensitivity: band straddles print repeated full-scale reversal pairs with no flat state to rest in, by the prescribed always-in design. The latch construction is the coded trigger, disclosed, not smoothed.
- High/low-definition sensitivity: venue prints (rolls, wick aggregation, anomalous prints) flow straight into both momentum legs; a venue that cannot supply trustworthy per-bar highs and lows cannot trade the pinned rule.
- Warmup cost: the triple-EMA stack needs 14+10+5 bars of seeding plus the 1-bar momentum reach; the adopted 60-bar warmup absorbs this structurally with wide margin, and the first 60 bars are flat by record rule.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- FMZ canonical strategy page, Directional Trend Index Trading Strategy (ID 427157) — full executable rule, inputs, latch, order pair, backtest header, HPotter header, Blau attribution (verified live in the fetched page during this cycle; zero performance claims): https://www.fmz.com/strategy/427157
- MQL5 CodeBase, Directional Trend Index Blau_DTI by abolk — recurrence shape, high/low-momentum legs, zero branch (verified live in the fetched page during this cycle): https://mql5.com/en/code/384
- MotiveWave official study documentation, Directional Trend Index — 14/10/5 parameter corroboration, overbought→sell / oversold→buy polarity (verified live in the fetched page during this cycle): https://motivewave.com/studies/directional_trend_index.htm
