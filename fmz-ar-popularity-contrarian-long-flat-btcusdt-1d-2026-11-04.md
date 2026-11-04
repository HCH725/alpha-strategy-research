---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: AR popularity-oscillator contrarian long-flat on BTCUSDT 1d bars
created: 2026-11-04
updated: 2026-11-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-01-10
sources:
  - https://www.fmz.com/digest-topic/9873
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# AR popularity-oscillator contrarian — independent BTC-USDT spot 1d long-flat derivative

## Provenance

**Primary source (fetched live over HTTPS this cycle, HTTP 200, 663,913 bytes):** FMZ Quant digest **`https://www.fmz.com/digest-topic/9873`**, title "Quantitative trading strategy with price momentum analysis in Python", author **发明者量化-小小梦**, Created `2023-01-11 11:35:36`, Updated `2025-01-10 09:23:32` (both read from page metadata this cycle). Source market is pinned in prose: "We will use the Bitcoin spot of Huobi as the trading target". The page's backtest note reports only that the strategy "performed well in the backtest of this month" on Huobi spot BTC — a qualitative sentence with zero adopted figures.

**Order-affecting logic (Python strategy code on the page, cited with short literals only):** state constants `IDLE = 0` / `LONG = 1` / `SHORT = 2` with the explicit spot fence — "Note that this strategy is applied to the spot market, so there is no short opening or position. This is written here to facilitate understanding of the strategy and future expansion (such as extending to the futures market)." The per-loop machine reads `r = exchange.GetRecords()`, guards `len(r) <= 1`, computes `ar = sum(r.High - r.Open) / sum(r.Open - r.Low) * 100`, then: `if ar < 95 and (state == IDLE or state == SHORT):` buy-all (`exchange.Buy(-1, account["Balance"] * 0.9)`, gated on `Balance > 50`) → `state = LONG`; `elif ar > 80 and (state == IDLE or state == LONG):` sell-all (`exchange.Sell(-1, account["Stocks"] * 0.9)`, gated on `Stocks > 0.01`) → `state = SHORT`. The code ships zero stop, zero target, zero trailing, zero time exit, zero pyramiding guard beyond the FLAT-gated entry.

**Pinned prose defaults:** `AR = [Sum of all (High-Open) for N days / Sum of all (Open-Low) for N days] * 100`, with "N: The statistical window of the daily time cycle is generally 30 days by default, because the effective trading day of a month is about 30 days (digital currency 24/7 transactions, which may be conservative)". Regime frame: 100 is neutral ("If it is more than 100, the long position force begins to increase. If it is less than 100, the short position force begins to gather"); AR rising toward ~120 reads overbought ("the price is likely to fall back"); AR too low reads oversold ("you can consider waiting for the opportun[ity]"). Author caveats, all cited not adopted as tuning: "The above numbers are all default values and are not truth formulas"; the strategy "is still a shock[-market] effective" device that can exit early in major trends or bottom-fish early in major downs; "The threshold setting of the strategy also needs to be determined according to the characteristics of the trading object".

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the page's code sums its whole `GetRecords()` buffer (whose length is a backtest-setting artifact; in the page's own latest-month daily run that buffer is ≈30 daily bars, consistent with the prose N=30 default), sizes in percent-of-equity with cash/stock dust gates, and states no fill timing, warmup, cost, or venue-precision facts. Researcher-declared adaptations are exactly seven: (1) window freeze to the last **30** completed `1d` bars per the prose default (fenced in Negative evidence 1); (2) spot-cash semantics pinned — source `SHORT` state is cash, so the derivative is explicitly long-only LONG/FLAT with the short side disabled; (3) fixed **0.01 BTC** spot sizing (≈774.54 USDT at the cycle's last completed close 77,453.86 on 2026-11-03, above verified 5-USDT min-notional and 0.00001 min-qty, step-exact) replacing percent-of-equity plus dust gates; (4) all risk legs explicitly disabled — level-exit-only risk matching the shipped code; (5) 300-bar warmup with pre-warmup bars flat (10× the frozen window 30); (6) explicit **0.1%/side research cost** (Binance spot standard taker), slippage unmodeled (disclosed); (7) close-decided signals filled next-bar-open MARKET (research-model timing convention, never a live-engine claim) replacing the page's live-loop market orders.

**Immutable derivative identity:** `FMZ:digest9873-xiaoxiaomeng|ar30_sumH-O_sumO-L_95-80_level-band_longonly|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001|lev1x-spot|warmup300|2026-11-04`. Changing any window, threshold, timing, market, risk, cost, sizing, leverage or direction creates a different derivative.

**Pre-write dedup (2026-11-04):** working-tree base is current `main@ab12a4fe` (551 root strategy records, READMEs excluded; this file is the 552nd). Filename search for `price-momentum` / `popularity` / `arbr` / `brar` / `fmz-ar-` returns zero records. Whole-word content search for `kairi`, `brar`, `arbr`, `absolute price oscillator`, `dynamic momentum index`, `correlation trend index` returns zero records; the `ar < 95` / `ar > 80` threshold pair returns zero records; the `AR = [Sum` formula returns zero records (the lone `9873` substring hit in the pool is SSRN `abstract_id=1898735` inside an unrelated skewness paper). No open `research/*` PR is this file, author construction, or signal (17 open PRs enumerated by number — #48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708, #725 — none colliding; #725 is a PineCoders TASC gap-momentum slope record verified to contain zero AR/popularity content). Five-axis distinction vs nearest pool neighbors: different input and event vs all RSI-oversold-recross records (`forven-connors-rsi`, stoch/RSI washout family — smoothed close-momentum crosses, never a 30-day H/O/L positional ratio, never a level-band state machine); different math vs stochastic/%R records (normalized close position with smoothing vs unsmoothed ratio-of-sums); different horizon vs all single-bar H−O/O−L geometry records (`wick-reversal-hammer-shooting-star`, `80-20-wide-bar-fade`, `priceaction-sr16` — one-bar patterns, never a 30-day aggregate); different data vs all volume-flow records (ADL/CMF/OBV/Twiggs — this rule reads zero volume); different construction vs TASC gap-momentum #725 (gap-based slope vs open-positional ratio band). No duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

AR (per the digest) measures where the day's open sits between that day's high and low, aggregated over N days: the ratio of total upside reach above the open to total downside reach below it. 100 is the equilibrium where both forces balance; above 100 the long force builds, below 100 the short force gathers. A rising AR toward ~120 warns the market is overbought and due a pullback; a sunk AR marks oversold ground worth waiting on. The page's own limitation: used alone it exits trends early and fishes bottoms early — a shock-market device, with thresholds that must fit the traded object.

### Research interpretation

Unlike pool RSI/stochastic mean-reversion that smooths close-to-close momentum, this machine never looks at a close except for fills: it trades the crowd's intraday positional bias — how far price stretches above the open versus sags below it, summed over a calendar month of daily bars. The pinned band makes it a contrarian scalp, not a trend ride: it buys popularity-weakness (AR<95) and holds only while weakness persists (AR≤80), selling the first bounce back above 80. The economics of that port to BTCUSDT spot daily bars are fenced as a limitation, with no tuning inside this record.

## Signal

Exact rule as pinned (daily decision on completed spot `1d` bars; entries/exits next-bar-open market; long-only single-unit book — any other window, threshold, sizing, fill, or cost is a different, unpinned rule):

- R1 — Measure grid: completed `1d` bars of BTCUSDT spot only. Continuous calendar days (weekends included); no session template, no holiday skip.
- R2 — Source series: `H[t]`/`O[t]`/`L[t]` are the sole signal inputs. `C[t]` is validity and fill-economics only (fills price at opens; notionals reference closes). No volume read exists in this rule; no funding/OI/mark-index read gates on any order (spot has no funding by construction — disclosed exclusion, never a zero-funding fiction), no sentiment/macro/on-chain/cross-venue state.
- R3 — AR composite (source formula, window frozen per prose default): `AR[t] = 100 × Σ(H[i]−O[i]) / Σ(O[i]−L[i])` over the last 30 completed bars `i ∈ [t−29, t]`. If the denominator sums to exactly zero, the bar is degenerate and emits no event (hold; fenced).
- R4 — Events (source machine, strict inequalities pinned): `Buy[t] = (AR[t] < 95) while FLAT`; `Sell[t] = (AR[t] > 80) while LONG`. Branch is state-determined per the source `if/elif`: a FLAT bar with AR in (80, 95) enters LONG; a LONG bar with AR in (80, 95) exits to FLAT; equalities hold (`AR == 95` never buys, `AR == 80` never sells). At most one fill decision per bar by construction.
- R5 — Position (source machine): `LONG`/`FLAT` single-unit book. If FLAT and `Buy[t]` (post-warmup) → request LONG at the next open. If LONG and `Sell[t]` → exit the whole book at the next open. Source `SHORT` state is spot cash and is recorded here as FLAT; the short side is explicitly disabled and never opens.
- R6 — Risk legs (pinned absences, not invented): no stop, no target, no trailing, no time exit — explicitly none, matching the shipped code (no such call exists in the page's strategy).
- R7 — Position state: one 0.01-BTC spot unit max, long or flat, never short. Safety orders: explicitly none. No pyramiding: while LONG no new Buy can add (entry needs FLAT, R5) — pinned absence, not invented. The source's percent-of-equity sizing and `Balance > 50` / `Stocks > 0.01` dust gates are replaced by the fixed unit (adaptation 3, disclosed).
- R8 — Warmup and gaps: flat until 300 completed `1d` bars (10× the frozen window 30; the AR sum is a finite-window exact aggregate with no recursive seed, so any warmup ≥ 30 prints the identical post-warmup event set — the 300 margin is convention, fenced). A bar with nonfinite/non-positive OHLC is invalid for signals — explicit hold. Missing-bar stretches freeze evaluation at the prior target — never backfilled, never forced flat.
- R9 — Invariant identifier: `FMZ:digest9873-xiaoxiaomeng|ar30_sumH-O_sumO-L_95-80_level-band_longonly|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001|lev1x-spot|warmup300|2026-11-04` (any window, threshold, direction, sizing, fill, or cost change is a different derivative).

## Required data

- Completed `1d` bars of BTCUSDT spot only: `high`/`open`/`low` (sole signal inputs), `close` (validity and fill-economics only). No volume read exists in this rule; no funding/OI/mark-index read gates on any order (spot has no funding by construction — disclosed exclusion, never a zero-funding fiction), no sentiment/macro/on-chain/cross-venue state.
- Single decision grid: one signal evaluation per completed daily-bar close; fills land at the next bar's open. No provisional intrabar value is ever used. Every live input is frozen at the decision close — point-in-time clean.
- Warmup: flat until 300 completed bars (structural). No repainting (all inputs read closed-bar OHLC only over a fixed 30-bar window; finite memory, no recursive seed), no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance spot, 1x, fixed 0.01 BTC per unit, single-unit book, no compounding. Long side explicitly enabled; short side explicitly disabled (source SHORT is spot cash). Fills are never conditional on equity or buying power.
- Order timing (declared promotion): signal-bar-close decision; entries and exits fill at the next bar's open market. No maker-touch, queue, or intrabar-path-dependent fill is claimed. The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Sizing/capital/costs (all fixed this cycle): fixed 0.01 BTC per unit (≈774.54 USDT at the cycle's last completed close 77,453.86 on 2026-11-03 — the 11-04 bar was still forming at cycle time — above the cycle-verified Binance spot BTCUSDT `NOTIONAL minNotional 5.0`, `LOT_SIZE minQty/stepSize 0.00001/0.00001`, `PRICE_FILTER tickSize 0.01`; 0.01 is an exact multiple of the step). Explicit research cost overlay: 0.1% taker fee per filled side; slippage unmodeled by declaration. Spot venue means no funding leg exists — constructive exclusion, never modeled-or-realized funding.
- Pinned-engine path (bounded model, inspected this cycle — capability check, not implementation): Hummingbot package `20260920` / `VERSION dev-2.17.0` per the README pin (local checkout `2dbc844fadb9d863b3ab0af1b8ab100472102e42` carries `hummingbot/VERSION` file `2.17.0`, verified live this cycle); `hummingbot/strategy_v2/controllers/controller_base.py` (`determine_executor_actions`), `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py` (over spot feeds) and `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` all present — the single-TF spot-1d close-decided / next-open-market path is the same bounded route prior PASS records use. The 30-bar AR ratio plus level-band state machine is a plain precomputable signal series, not a new execution primitive; no new data requirement, no representative-capability validation owed.

## Evidence

### Source-reported

The live page ships every adopted headline fact quoted in Provenance: the `AR = [Sum(High-Open)/Sum(Open-Low)] × 100` formula with the N=30-day prose default, the `100` neutral frame with the ~120-overbought / sunk-oversold readings, the full `if ar < 95 … Buy … elif ar > 80 … Sell` state machine with its `IDLE/LONG/SHORT` constants, the explicit no-short-position-on-spot fence, the Huobi Bitcoin-spot target, and the qualitative latest-month backtest sentence. It ships zero stops, zero targets, zero sizing beyond percent-of-equity, zero thresholds beyond 95/80, zero performance figures — none adopted; all frozen trading semantics beyond the machine are researcher pins disclosed above.

### Independently reproduced

No strategy-level independent reproduction: no strategy backtest, no event-level Qlib/Hummingbot parity, no live order, testnet/paper trade, deployment, or profitability experiment occurred. Pinned engine file inspection demonstrates a bounded model path, not completed executable implementation. Researcher formula-sanity probe only (2026-11-04, disclosed, not strategy evidence): AR(30) recomputed from live Binance BTCUSDT `1d` klines prints finite in-range values (≈66–71 across the trailing windows this cycle), confirming the composite is computable on the pinned grid; no trade event, fill, or performance inference is drawn from it.

### Negative evidence

1. Window-freeze fence: the page's code sums its whole `GetRecords()` buffer while its prose pins N=30 days by default; this record freezes the last 30 completed bars (adaptation 1). In the page's own latest-month daily run the buffer is ≈30 daily bars, so the freeze is consistent with the source's demonstrated run, never a contradiction of it; any other window is unpinned.
2. Equality fence: `AR == 95` never buys and `AR == 80` never sells (strict inequalities pinned). An implementation using `<=`/`>=` prints a different, unpinned event set.
3. Band-overlap fence: thresholds overlap (80 < 95) by source design — in-band bars enter when FLAT and exit when LONG. An implementation that treats the band as a hold-zone in both states, or that reorders branch priority, prints a different, unpinned event set.
4. First-signal fence: the machine is level-based, not cross-based — the first post-warmup bar may enter immediately if `AR < 95`. Absorbed by the warmup; shorter warmups print different early event sets and are unpinned.
5. Degenerate-denominator fence: a 30-bar window summing `Σ(O−L) = 0` (thirty straight bars with open equal to low) emits no event here (hold). Live BTC tape never approaches this; an implementation dividing through zero prints a different, unpinned outcome.
6. Threshold-tunability fence: the author flags 95/80 as "default values … not truth formulas" that should fit the traded object — this record freezes the published pair anyway; any retuned pair is a different, unpinned derivative.
7. Number silence fenced: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from any source is adopted anywhere (the page's "performed well" sentence carries no numbers), and any dispute over exact magnitudes is decided against this record, never patched by inference.
8. Derivation boundary fenced: the only non-source behavior is the seven declared adaptations (30-bar freeze, long-only cash semantics, fixed sizing, disabled risk, 300-bar warmup, 0.1% cost overlay, next-open fills); the formula shape, 95/80 pair, state machine, inequalities, and spot market are source-faithful. This record is therefore never evidence that any author strategy passes.
9. Page-drift fence: this record follows the page content as fetched 2026-11-04 (Created 2023-01-11, Updated 2025-01-10). If the page is ever edited, this record does not move with it.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `AR(30)` ratio-of-sums / `95`-buy / `80`-sell level band / long-only / no-risk-leg exits / next-open fills / fixed 0.01 BTC spot / BTCUSDT `1d` / 300-bar warmup are frozen.

- F1 — Input relevance: an RSI(14)-level-band twin (same 95/80-style contrarian band on closes, same rest) must not improve net expectancy; fail ⇒ the H/O/L positional ratio adds nothing over close-momentum.
- F2 — Window relevance: an AR(60) twin (same rest) must not improve net expectancy; fail ⇒ the prose-default 30-day window carries no information.
- F3 — Band relevance: a symmetric 100-threshold twin (buy FLAT when AR<100, exit LONG when AR>100, same rest) must not improve net expectancy; fail ⇒ the published 95/80 asymmetry is decoration.
- F4 — Warmup relevance: a 350-bar-warmup twin must print the identical post-350 event set (finite 30-bar memory ⇒ structural identity is expected); fail ⇒ seed or ramp transients leak past the declared warmup.
- F5 — Exit relevance: a hold-while-weak twin (exit LONG only when AR>95 instead of 80, same rest) must not improve net expectancy; fail ⇒ the 80 scalp-exit adds nothing over a symmetric round-trip.

## Crypto portability

Pinned to BTCUSDT Binance spot (decision grid completed `1d` bar closes; entries/exits at next opens; H/O/L-only signal input — the only venue-specific reads are OHLC). The arithmetic ports across spot venues without structural change (no corporate-action or calendar adjustment exists to recheck; weekends trade continuously — the digest itself notes digital-currency 24/7 trading — so no equity-calendar port artifact). The source venue is Huobi BTC spot; the Binance port is a disclosed researcher adaptation. Extension to other house-universe assets, timeframes, windows, thresholds, grids, or unit counts would be a different, unpinned claim.

## Limitations

- The page is © FMZ / its author (cited with short literals only, never copied in bulk); the window freeze, long-only cash semantics, sizing, warmup, next-open fills and cost overlay are researcher adaptations disclosed in Provenance — the derived event set must not be cited as the author's output or as lossless reproduction.
- Single-venue, single-pair, single-timeframe spot claim only; funding/OI/cross-venue/macro regimes are out of scope by construction, and the 0.1%/side overlay is a research cost model, never realized economics.
- The author’s own limitation transfers: a shock-market device that can exit trends early and fish bottoms early, with thresholds the author flags as object-dependent defaults frozen here without tuning.
- Band overlap, equality handling, first-signal immediacy, degenerate denominators and the whole-buffer-vs-30 prose/code nuance are implementation-defined (Negative evidence 1–5); bit-exact cross-implementation match on pathological input is not claimed.
- Warmup (300) is a researcher margin at 10× the frozen window 30; shorter warmups print different early event sets and are unpinned.
- No profitability, Sharpe, drawdown, or capacity claim is made anywhere; PASS is pinned-engine expressibility only.

## Implementation status

`not-implemented` — no dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record. This status describes artifacts only and does not revoke HB_READY PASS or permit downstream refusal. If formally selected for execution with no reproducible recipe, the engineering route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, then return to the same pipeline without redoing HB_READY).

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`. This record authorizes no live, Paper, Testnet, or real-capital action of any kind.

## Related Wiki records

None.

## Sources

- https://www.fmz.com/digest-topic/9873 ("Quantitative trading strategy with price momentum analysis in Python", author 发明者量化-小小梦, Created 2023-01-11 11:35:36, Updated 2025-01-10 09:23:32; HTTP 200 verified this cycle, 663,913 bytes fetched 2026-11-04; AR formula, 100/120 regime prose, full entry/exit state machine, no-short-on-spot fence, Huobi Bitcoin-spot target — cited with short literals, never bulk-copied)
- Binance spot `BTCUSDT` exchange filters and `1d` klines fetched live this cycle (TRADING; `PRICE_FILTER tickSize 0.01`; `LOT_SIZE minQty/stepSize 0.00001/0.00001`; `NOTIONAL minNotional 5.0`; last completed daily close 77,453.86 on 2026-11-03; the 11-04 bar was still forming and no provisional value is used)
