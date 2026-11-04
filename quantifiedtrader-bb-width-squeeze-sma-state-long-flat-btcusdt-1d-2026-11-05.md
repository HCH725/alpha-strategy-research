---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: QuantifiedTrader BB Width Squeeze SMA-state long-flat on BTCUSDT 1d bars
created: 2026-11-05
updated: 2026-11-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-11-05
sources:
  - https://quantifiedtrader.com/backtest/strategies/bb-width-squeeze/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# QuantifiedTrader BB Width Squeeze SMA-state long-flat on BTCUSDT 1d bars

## Provenance

**Primary source (fetched live over HTTPS this cycle):** QuantifiedTrader public strategy-library page `https://quantifiedtrader.com/backtest/strategies/bb-width-squeeze/` (`BB Width Squeeze`), fetched 2026-11-05 as a 43,057-byte page (SHA-256 `221979027a035370e5d1bfa84f1de740e61ab83884bf3b19f073b81b48bb0f95`). The page prints no login, paywall, author handle, or creation stamp (adopted `source_as_of` is the fetch date, per the merged QuantifiedTrader Raff-Channel / Projection-Oscillator / Keltner-Squeeze / ATR-Bands lane precedent). The strategy-implementation code block is printed verbatim on the page (backtesting.py shape):

```text
class BBWidthSqueeze(Strategy):
    n = 20; k = 2; width_n = 50
    def init(self):
        width = _bb_width(self.data.Close, self.n, self.k)
        self.width = self.I(lambda: width, name="Width")
        self.sma = self.I(_sma, self.data.Close, self.n)
        self.width_min = self.I(lambda: width.rolling(self.width_n).min(), name="WidthMin")
    def next(self):
        if self.width[-1] < self.width_min[-1]*1.1 and self.data.Close[-1] > self.sma[-1] and not self.position: self.buy()
        elif self.data.Close[-1] < self.sma[-1] and self.position: self.position.close()
```

Code census this cycle over the rendered visible text before the backtest-data loader (scripts/styles stripped): 1 `buy()` / 1 `position.close()` / 0 short/sell-short order calls / 0 stop/limit/trailing/time/target/profit calls in the order path / 3 indicator registrations (`self.I`) / 0 volume reads by any order-gating line. (`stop_loss`/`take_profit` tokens exist only inside stripped script/JSON page boilerplate, never in the visible methodology — fenced, not adopted.) Helper-name census: `_bb_width` 1 and `_sma` 1, each exactly at its call site, with zero `def _` definitions printed anywhere — the helper bodies are unprinted, the same gap shape the merged Raff-Channel / Projection-Oscillator / Keltner-Squeeze / ATR-Bands lane records froze via textbook construction. This record cites and normalizes the rule and reproduces no source block beyond the short declarations quoted for gate evidence.

**Facts actually supplied by the source page:** backtested on **daily OHLCV** across major US equity indices and ETFs (S&P 500, NASDAQ Composite, DJI, Russell 2000, +16 more); entry/exit signals carry **no lookahead bias**; **trades execute at the open of the bar following the signal**; performance metrics are computed per symbol; **transaction costs and slippage are not modeled**. Signal prose: Bollinger Band Width Squeeze waits for the band width to compress to a multi-period low (low volatility), then enters long when price breaks above the SMA; volatility expansion after a squeeze often produces strong directional moves. No return, Sharpe, win-rate, or trade-count figure from the source is carried into the derived specification. The page's parameter grid-search section, where available, is not adopted as a parameter source.

**Prose-vs-code fence (code governs):** the prose says "breaks above the SMA" but the program tests the level `Close[-1] > sma[-1]`, not a cross edge — a bar that has held above the average for weeks still satisfies the price leg; only the `not self.position` guard stops re-entry. The prose says "compress to a multi-period low" but the program tests the tolerance `width < width_min*1.1` (within 10% above the trailing 50-bar minimum), not a strict new minimum. Both loosenings are quoted as printed and the executable rule follows the program, never the prose.

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the source ships equity-universe backtesting.py semantics with no venue/fill/cost leg this record can reuse verbatim. Researcher-declared adaptations are exactly six: (1) market pin **BTCUSDT Binance spot 1d** (long-flat needs no margin-short permission; spot is the minimal realistic venue — the source's equity-index universe is kept separate, never claimed); (2) completed-bar decisions with **next-bar-open market** fills (the source's own stated execution — "trades execute at the open of the bar following the signal" — preserved verbatim); (3) inputs frozen at `n = 20, k = 2, width_n = 50` with the closed-form textbook construction below (plain SMA20 + population-σ Bollinger width + trailing-50 rolling minimum, decision bar included per the printed `.rolling()` call); (4) adopted **100-bar warmup** with pre-warmup bars flat by record rule (structural minimum is index 68 — first SMA20/width print at index 19 plus 49 further bars to fill the first 50-bar minimum — verified this cycle; 100 carries margin); (5) house sizing/costs replacing the source's no-cost model (fixed 0.01 BTC, 0.1%/side taker; spot means no funding leg exists — constructive exclusion, never zero-claimed; fixed size is event-neutral for timing under state-independent signals); (6) missing-bar stretches freeze evaluation at the prior target — book and ledger retained across the freeze, evaluation resumes on the next valid bar with no warmup repetition, never backfilled, never forced flat. The squeeze-tolerance entry, the above-SMA state leg, the sub-SMA exit, the long-only stance, and the no-stop/no-target posture are source-pinned or predeclared; no short leg is invented.

**Immutable derivative identity:** `qtbbwidth:BBWidthSqueeze-sma20-bbwidth50min-tol1.1_state|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001-nofunding|spot1x|nostop-notarget|warmup100|2026-11-05`. Changing any input, width construction, seed, tolerance, comparator, direction, timing, market, risk, cost, sizing, or book state creates a different derivative.

**Pre-write dedup (2026-11-05):** working-tree base is current `main@4c5286aa` (564 root strategy records, READMEs excluded; this file is the 565th). Content searches for `BBWidthSqueeze`, `_bb_width`, `WidthMin`, `width_min`, and the canonical slug `strategies/bb-width-squeeze` return zero same-source/same-construction records (the single `1.1 *`-adjacent pool hit is an unrelated volume-profile bracket record, never a width-minimum gate). No open `research/*` PR is this page, author, construction, or signal (17 open PRs enumerated this cycle — #48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708, #725 — none is a BB-width, QuantifiedTrader-squeeze, or width-minimum machine). The pool's squeeze cousins are all fenced as different signal objects (Negative evidence 1–6). No duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

Compression-then-participation, long side only. The construction is self-describing: the Bollinger width (upper minus lower) measures how far the market has recently been willing to roam; when that width sits within 10% of its own trailing 50-bar minimum, the market is deemed coiled; a close printing above the 20-bar average while coiled holds the expansion thesis, and the first close back below the average ends it. The equity-index universe and the unmodeled-costs stance are source facts, not this record's venue or economics. No performance figure is carried anywhere.

### Research interpretation

Coil-gated average-state object — the patient sibling of the merged ATR-Bands record (which buys every lower-rail touch with no gate at all) and the structural inverse of the squeeze-breakout cousins (which demand a band-penetration edge). Unlike the pool's Donchian cousins (raw realized extremes) both the gate and the trigger here are manufactured (width ratio, average level), so entries key off volatility-normalized compression rather than printed extremes. Unlike Forven's BB-squeeze (BB-inside-KC plus an upper-band breakout cross) and Lepotorico's width-gated breakout (width-vs-mean recency plus a band-penetration cross with a bracket), this rule demands no penetration anywhere — a bar that has floated above its average for a month inside a pinned width still arms on the first flat-book evaluation. The failure mode is plain and verified this cycle: in a perpetually compressed tape the gate never closes and the machine degenerates into a midline-state flip-flop, churning every other bar (the planted dead-flat tape prints 35 entries / 34 exits ending LONG — disclosed, not patched); a sustained ramp never compresses and never participates (planted sustained-up tape arms zero times — disclosed); a sustained bleed never prints above the average and never participates either, so unlike the ATR-Bands bleed-hold this rule cannot catch a falling knife at all (planted sustained-down tape arms zero times — disclosed).

## Signal

Exact rule as pinned (daily decision on completed `1d` bars; entries/exits next-bar-open market; long-flat single-unit book — any other input, width construction, seed, tolerance, sizing, fill, or cost is a different, unpinned rule):

- R1 — Measure grid: completed `1d` bars of BTCUSDT spot only. Continuous calendar days; no session template, no holiday skip. Bar time is never read by any order-gating line.
- R2 — Source series: `C[t]` is the sole signal input (`O[t]` fills only; `H[t]`/`L[t]` are never read by any order-gating line — the width is a close-only construction; notionals reference closes for cost sizing only). No volume, no funding/OI/mark-index read gates on any order; no sentiment/macro/on-chain/cross-venue state. Single timeframe, single asset.
- R3 — Width stack (frozen, researcher-pinned textbook construction for the unprinted helpers): `SMA20[t]` is the plain 20-bar mean of closes (first finite at index 19); `SD20[t]` is the population stdev (÷N, Pine/TA-Lib Bollinger convention — part of the pin, disclosed as the researcher freeze for the unprinted `_bb_width`); `Width[t] = 4.0 · SD20[t]` (upper-minus-lower algebra — the `k = 2` multiple survives only inside this product); `WidthMin[t] = min(Width[t-49..t])`, decision bar included per the printed `width.rolling(50).min()` call (first finite at index 68 — verified this cycle). Finite exactly when all trailing inputs are finite. Any other σ denominator, seed, or window convention prints a different, unpinned series.
- R4 — Entry (pinned, squeeze-tolerance plus above-average state): if FLAT and `Width[t] < WidthMin[t]·1.1` and `C[t] > SMA20[t]` (post-warmup) → buy at the next open. Because `Width[t] ≥ WidthMin[t]` always (the decision bar belongs to its own minimum window), the gate is exactly "width within 10% above its trailing 50-bar minimum". A touch of either boundary (`==`) fails the strict leg and fires nothing on that leg.
- R5 — Exit (pinned, sub-average level): if LONG and `C[t] < SMA20[t]` → close the whole book at the next open. The exit is a level hold, not a cross — it fires on any bar closing under the average, including bars that never entered. The program ships no NaN guard, but a non-finite print never satisfies any strict comparison, so seeding can never smuggle an entry or an exit; pre-warmup and NaN-signal bars are flat/hold by record rule.
- R6 — Risk legs (file absence, not invented): stop-loss, take-profit, trailing, time exit, and any second exit are all explicitly disabled — the program ships none, and no prose ships any executable one. The sub-average print is the sole exit path.
- R7 — Position state (single deterministic path — no reset, no re-warmup): one 0.01-BTC unit max, long or flat. Safety orders: explicitly none. No cooldown: after any close, the next squeeze-plus-state bar re-enters at its next open (`not self.position` guard preserved — while LONG, qualifying bars are no-ops; while FLAT, sub-average bars are no-ops). Entry and exit can never co-fire (`C > SMA` vs `C < SMA` are jointly unsatisfiable; `C == SMA` fails both strict legs) — no tie-break pin is required. The degenerate all-equal window (`Width == WidthMin == 0`) fails the strict gate (`0 < 0` is false) and fires nothing — verified on no live bar this cycle (zero zero-width bars in range), fenced by arithmetic.
- R8 — Warmup: flat until 100 completed `1d` bars (structural minimum is index 68; 100 carries margin — verified this cycle). The 100-bar pin is frozen: any other warmup is a different, unpinned claim.
- R9 — Invariant identifier: `qtbbwidth:BBWidthSqueeze-sma20-bbwidth50min-tol1.1_state|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001-nofunding|spot1x|nostop-notarget|warmup100|2026-11-05` (any input, construction, seed, tolerance, comparator, direction, sizing, fill, risk, or cost change is a different derivative).

## Required data

- Completed `1d` bars of BTCUSDT: `C[t]` is the sole series the formula reads (SMA source, width source, both comparisons). `O[t]` fills only; `H[t]`/`L[t]` are read by no order-gating line. No `volume`, no funding-signal, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; the windows read trailing completed bars only, never a second feed).
- Warmup: 100 completed `1d` bars flat by record rule — structural minimum is index 68 (binding legs: 20-bar SMA/width seed plus the 50-bar rolling minimum, verified first-finite at index 68 this cycle). Pre-warmup and any NaN-signal bars are flat/hold by record rule; missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (windows read completed bars including the decision bar only — same-bar comparison, no lag, no negative shift), no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance spot, 1x, fixed 0.01 BTC per unit, single-unit book, no compounding. Long side explicitly enabled; short side explicitly disabled (zero short/sell-short order tokens in the printed program). Fills are never conditional on equity or buying power.
- Order timing (source-stated timing preserved verbatim): completed-bar decision with next-bar-open market fills for entries and whole-book closes — the source prose states "trades execute at the open of the bar following the signal", and this record adopts exactly that (the same verified execution primitive as the merged FMZ/QuantifiedTrader lane records; with no stop/limit legs anywhere in the derived machine there is no same-bar TP/SL ordering ambiguity; each bar's outcome is a single deterministic event: hold, open-long, or close-flat, and R7 proves the two legs can never co-fire). This record claims no other fill convention: no same-bar-close print, no maker-touch, no intrabar-path-dependent fill.
- Pinned engine path (verified at the pin this cycle): Hummingbot package label `20260920`, VERSION `dev-2.17.0` (local checkout `2dbc844` carries `hummingbot/VERSION` file `2.17.0`, verified live this cycle; `8b0e067e80ab62f10846d518dcb5a8218527ddb3` is an ancestor of the local checkout, verified via `merge-base --is-ancestor` this cycle; code paths verified at the pin this cycle: `async def run_backtesting` in `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py:221`, `def determine_executor_actions` in `hummingbot/strategy/strategy_v2_base.py:747`, `class OrderExecutorSimulator` in `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py:9`, `INTERVALS "1d" = "1d"` in `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py:24`). Prior merged Alpha PR **#414** reports a 902/902 wheel-file byte match and 33-assert representative validation for this source/package path; this Scout did not independently rehash the wheel. A different deployed package must be revalidated. A strategy-specific, not-yet-implemented controller must compute the trailing width-minimum/state pin via `CreateExecutorAction(OrderExecutorConfig)` market legs; the generic executor does not calculate the strategy. The precomputable width series plus tolerance/state machine is a plain signal series, not a new execution primitive; no new data requirement, no representative-capability validation owed.
- Stop/limit modeling: none — the derived spec carries zero stop/limit/trailing legs by record rule. No hidden Hummingbot stop-order defaults are relied upon, and with no stop/limit legs there is no same-bar TP/SL ordering ambiguity.
- Sizing/capital/costs: the source models no costs (recorded as the source's, never adopted). Explicit house overlay: single-unit frame, 0.1% taker fee per filled side, slippage unmodeled by declaration; fixed size is event-neutral for timing under state-independent signals. Exchange facts re-verified live this cycle via `api/v3/exchangeInfo`: `BTCUSDT`, `TRADING`, `tickSize 0.01`, min-qty/step 0.00001/0.00001, min-notional 5.0 (`NOTIONAL`). The fixed 0.01 BTC (≈801.76 USDT at the cycle's 24hr last price 80,176.01, above the 5.0 min-notional and an exact multiple of the 0.00001 step). Spot venue means no funding leg exists — constructive exclusion, never modeled-or-realized funding.
- Concurrency: at most one single-asset engine position at any time; the sub-average print ends it (re-entry earliest next signal). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no hedge-mode requirement by construction.

## Evidence

### Source-reported

With exact provenance (page fetched live 2026-11-05, 43,057 bytes, SHA-256 `221979027a035370e5d1bfa84f1de740e61ab83884bf3b19f073b81b48bb0f95`; implementation block `class BBWidthSqueeze(Strategy)` with `n = 20; k = 2; width_n = 50`, `_bb_width(Close, n, k)` + `_sma(Close, n)` single calls (helper bodies unprinted — each name occurs once, at its call site; zero `def` prints), `Width` + 20-bar `sma` + `WidthMin = width.rolling(50).min()` registrations, `Width[-1] < WidthMin[-1]*1.1 and Close[-1] > sma[-1] and not position → buy()`, `Close[-1] < sma[-1] and position → position.close()`): the frozen inputs; the close-only indicator reads; the squeeze-tolerance/state-entry polarity with strict comparators; the `not self.position` single-unit guard; the long-only order set (zero short/stop/limit/time calls in the order path); the source's daily-OHLCV frame, no-lookahead statement, next-bar-open execution, unmodeled-costs stance, and equity-index universe (S&P 500, NASDAQ Composite, DJI, Russell 2000, +16). This record claims no source-reported performance number as its own — no return, Sharpe, win rate, or trade count is carried into the derived specification — and no reproduced performance exists.

### Independently reproduced

**None.** No strategy backtest, event-level Qlib/Hummingbot parity, wheel rehash, deployment or profitability experiment occurred. Pinned engine source inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifacts this run are researcher self-checks of the predicate/estimator/state pipeline (textbook SMA20 + population-σ width + trailing-50 minimum, 100-bar warmup, tolerance/state next-open single-unit long-flat machine), run in scratch (never committed): logic verification only, not a backtest, not parity.

**Planted-tape verification (this cycle, deterministic):** TAPE-flat (dead-constant 170-bar tape with 0.05% wicks) prints 35 entries / 34 exits ending LONG — the width parks at its own minimum so the gate never closes and the machine degenerates into an SMA-state flip-flop, as pinned (disclosed churn-degeneration, not patched); TAPE-up (sustained +1%/day compounding 170-bar tape) prints 0 entries / 0 exits ending FLAT — the ramp never compresses, as pinned (disclosed non-participation, not patched); TAPE-down (sustained −1%/day 170-bar tape) prints 0 entries / 0 exits ending FLAT — the bleed never prints above the average so the rule cannot catch a falling knife at all, as pinned (disclosed, not patched — the structural inverse of the ATR-Bands bleed-hold); TAPE-volregime (deterministic 170-bar ±0.2%-then-±2% alternation tape) prints 2 entries / 2 exits ending FLAT — both transition paths are exercised, as pinned.

**Live-exchange microstructure probes (this cycle, Binance spot 1d klines, 3,366 completed bars 2017-08-17→2026-11-03; the in-progress 2026-11-04 bar excluded):** 81 post-warmup squeeze-state bars drive 81 entries / 81 exits ending FLAT (non-degenerate, non-buy-and-hold; zero zero-width bars in range). Two independent runs produce identical digests (event-series digest `afb6e9d8`). Admission is engineering capability, never an event-rate or profitability claim.

### Negative evidence

1. Breakout-squeeze fence: pool `forven-bb-squeeze-breakout` (BB-inside-KC squeeze plus an upper-band breakout *cross*, 1h) and `github-lepotorico-bb-squeeze-width-gated-breakout` (width-vs-mean recency plus a band-penetration cross with an SL/TP bracket, two-sided, 1h) both demand a penetration edge this record never tests — this record's entry is a tolerance-plus-level state conjunction with no cross anywhere. Different squeeze construction, different trigger shape, different risk — never a twin.
2. Release/momentum-squeeze fence: pool `forven-ttm-squeeze` (squeeze-release transition plus 12-bar momentum polarity, 1h) and `sqzmom-lb-squeeze-release` (squeeze-transition plus linreg-momentum/EMA100 gates, two-sided, momentum-tick exits, 1d) both gate on momentum this record never reads. No momentum series exists anywhere in the pinned rule — never a twin.
3. Keltner-sibling fence: the just-merged `quantifiedtrader-keltner-squeeze` (Keltner upper breakout with a fixed one-bar lag, SMA exit, 1d) breaks *above* a manufactured rail while this record enters on compression-plus-level with no breakout; the exits differ (average level vs envelope midline only in name — the machines arm on disjoint bars). Same lane pattern, different machine — never a twin.
4. ATR-Bands fence: the just-merged `quantifiedtrader-atr-bands` buys *every* lower-rail touch with no gate while this record buys only inside a width compression with an above-average chaperone; the ATR rule holds its bleed to the tape end while this rule never enters a sustained bleed at all. Opposite participation in trends, gated vs gateless — never a twin.
5. Bollinger-breakout fence: pool `bollinger-band-breakout-long-midline-exit` enters on an upper-band penetration cross while this record's width never appears as a traded rail — width is a gate, never a trigger. Gate-vs-trigger inversion — never a twin.
6. Single-print-twin fence: no twin is admitted — any input change (e.g. 20→14 window, 1.1→1.0 tolerance, 50→20 minimum span), any cross-flavored variant, any gated or two-sided variant, any other σ denominator, frame, fill, venue, or book is a different, unpinned rule.
7. NaN/seed fence: any non-finite width/minimum/average print holds with no signal and no close (language-false comparisons, no guard invented); the population-σ plus decision-bar-included rolling-minimum conventions are part of the pin. Interpolating, reseeding, or backfilling is a different, unpinned rule.
8. Warmup-identity fence, admitted plainly: the pin is 100 completed bars (structural minimum index 68); any other warmup remains a different, unpinned claim even where it prints the same book.
9. Number silence fenced: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from any source is adopted anywhere, and any dispute over exact magnitudes is decided against this record, never patched by inference.
10. Version fence: this record follows the QuantifiedTrader page as fetched 2026-11-05 (no printed creation stamp; fetch-date pin). If the page is ever edited, this record does not move with it.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: inputs `20/2.0/50` / textbook width construction + population-σ seed + decision-bar-included minimum / 1.1 tolerance / above-average-state entry / sub-average exit / long-flat book / no-stop-no-target posture / `1d` BTCUSDT spot / next-open fills / 0.01 BTC / 0.1% costs / 100-bar warmup are frozen.

- F1 — Gate relevance: a gateless twin (enter on `C[t] > SMA20[t]` alone / exit on `C[t] < SMA20[t]` — same rest) must not improve net expectancy; fail ⇒ the width-compression gate adds nothing over a bare average-state follower, and the record is a gate label rather than a squeeze edge.
- F2 — Tolerance relevance: a strict-minimum twin (enter only on `Width[t] <= WidthMin[t]` — same rest) must not improve net expectancy; fail ⇒ the 1.1 tolerance band adds nothing over strict new-minimum timing, and the record's tolerance is decorative.
- F3 — Exit relevance: a midline-cross twin (exit only on a fresh `C[t-1] >= SMA[t-1]` → `C[t] < SMA[t]` cross — same rest) must not improve net expectancy; fail ⇒ the level-hold exit adds nothing over an edge exit, and the record's always-armed exit is decorative.
- F4 — Warmup relevance: the pinned 100 print and a 100-vs-100 re-run must print the identical event set (determinism check — digest `afb6e9d8` is the tripwire); fail ⇒ nondeterminism or seed leakage past the declared warmup.

## Crypto portability

Pinned to BTCUSDT Binance spot under the house overlay (declared port of an equity-index-headed backtesting.py program). The rule reads completed daily closes only, so no pit-session, gap, roll, split/dividend-adjustment, or corporate-action logic ports (equity-calendar effects are non-issues on spot — disclosed, not modeled). The composite is unit-free in width-ratio terms (no absolute-price threshold anywhere), so unlike price-level systems the rule ports across venues without re-scaling — yet compression-gated buying on crypto microstructure (24/7 bars, stablecoin-quoted prints, cascade dynamics the source never traded) fires at a cadence the source never measured (81 entries across 3,266 post-warmup bars here), disclosed without re-tuning. The rule is long-flat, so a spot deployment expresses the full machine with no short permission — a two-sided or perpetual variant would be a different, unpinned claim (this record's gate-5 evidence is the spot path only; the source's equity universe is provenance, not execution). No warmup history beyond 100 `1d` bars is consumed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Gate-free degeneration by construction: in a perpetually compressed tape the tolerance gate never closes and the machine churns as a bare average-state flip-flop (planted dead-flat tape: 35/34 ending LONG — disclosed, not upgraded).
- Trend non-participation by construction: sustained ramps never compress (0/0) and sustained bleeds never print above the average (0/0) — the rule sits out both, disclosed, not patched.
- Single-venue port residual: backtesting.py close/open arithmetic vs Binance spot execution (prints, fees, open-definition across 24/7 sessions, equity-vs-crypto regime differences) is unclaimed, disclosed.
- Next-open latency idealization: signal cadence on the decision close print while fills land on the next open; any live gap between the two differs by construction — disclosed, research-only (this convention is the source's own stated execution, preserved verbatim).
- Tolerance-band residual: "within 10% of the trailing minimum" is the program's literal gate, not a strict squeeze extreme — near-minimum chop arms exactly like a fresh compression, disclosed.
- No-authorship-page residual: the page prints no handle, license, or creation stamp; provenance rests on the QuantifiedTrader URL/slug, printed names, page hash, and fetch date — disclosed.
- Performance evidence is absent: nothing here is calibrated, fitted, or tuned to any backtest (the `20/2.0/50` defaults are the source's, never re-run here; the page's own grid-search section, where available, is not adopted as a parameter source).
- Author scope: the page ships exploratory research with an explicit not-investment-advice disclaimer, not a vetted trading system — this record is research-only and claims no live suitability.

## Implementation status

`not-implemented`: no dedicated controller, Qlib executable recipe or deployment artifact was created. PASS is a bounded research-expressibility proposal, not a claim of already runnable materialization. A selected strategy may later need the minimal strategy-specific implementation without a second admission flag.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review must independently inspect this exact PR head, remediate only primary-source-verifiable facts, then PASS exact-head merge or NOT_LOSSLESS close. Scout does not approve, merge, close, trade, backtest or deploy.

## Related Wiki records

None asserted.

## Sources

- Primary page + pin: https://quantifiedtrader.com/backtest/strategies/bb-width-squeeze/ (`BB Width Squeeze`; page fetched live 2026-11-05, 43,057 bytes, SHA-256 `221979027a035370e5d1bfa84f1de740e61ab83884bf3b19f073b81b48bb0f95`; implementation block `class BBWidthSqueeze(Strategy)` with `n = 20; k = 2; width_n = 50`, `_bb_width(Close, n, k)` + `_sma(Close, n)` single calls (helper bodies unprinted — each name occurs once, at its call site; zero `def` prints), `Width` + 20-bar `sma` + `WidthMin = width.rolling(50).min()` registrations, `Width[-1] < WidthMin[-1]*1.1 and Close[-1] > sma[-1] and not position → buy()`, `Close[-1] < sma[-1] and position → position.close()`; zero short/stop/limit/trailing/time/target/profit order calls in the order path; daily OHLCV frame, no-lookahead statement, next-bar-open execution, unmodeled costs, equity-index universe S&P 500 / NASDAQ / DJI / Russell 2000 +16)
- Lane precedent (different mechanism, unmerged-proof never claimed): `quantifiedtrader-atr-bands-lower-touch-midline-exit-long-flat-btcusdt-1d-2026-11-05.md`, `quantifiedtrader-keltner-squeeze-upper-breakout-sma-exit-long-flat-btcusdt-1d-2026-11-05.md`, `quantifiedtrader-raff-channel-midline-level-long-flat-btcusdt-1d-2026-11-04.md` and `quantifiedtrader-projection-oscillator-zero-cross-long-flat-btcusdt-1d-2026-11-04.md` (unprinted-helper textbook-freeze derivation pattern)
- Nearest pool lineages (different mechanisms, unmerged-proof never claimed): `forven-bb-squeeze-breakout-long-flat-btcusdt-1h-2026-10-19.md` (BB-in-KC squeeze plus breakout cross); `github-lepotorico-bb-squeeze-width-gated-breakout-two-sided-btcusdt-1h-2026-11-04.md` (width-vs-mean recency plus penetration cross with bracket); `forven-ttm-squeeze-momentum-release-long-flat-btcusdt-1h-2026-10-19.md` (release plus momentum); `sqzmom-lb-squeeze-release-ema100-two-sided-btcusdt-1d-2026-10-09.md` (transition plus momentum/EMA100 gates); `bollinger-band-breakout-long-midline-exit-btcusdt-1d-2026-10-11.md` (upper-band penetration entry — width-as-trigger, the inverse of this record's width-as-gate)
- Exchange verification: Binance spot `api/v3/exchangeInfo` (`BTCUSDT`, `TRADING`, `tickSize 0.01`, min-qty/step 0.00001/0.00001, min-notional 5.0 via `NOTIONAL`) plus `api/v3/klines` 1d probes (3,366 completed bars 2017-08-17→2026-11-03, 81 post-warmup squeeze-state bars → 81 entries / 81 exits ending FLAT, event digest `afb6e9d8` double-run identical; planted tapes flat 35/34 LONG, up 0/0, down 0/0, vol-regime 2/2 — degeneration/non-participation fences), fetched live 2026-11-05
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently merged pinned package/source evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
