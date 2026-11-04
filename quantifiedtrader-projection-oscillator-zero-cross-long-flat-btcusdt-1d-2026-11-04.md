---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: QuantifiedTrader Projection Oscillator zero-cross long-flat on BTCUSDT 1d bars
created: 2026-11-04
updated: 2026-11-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-11-04
sources:
  - https://quantifiedtrader.com/backtest/strategies/projection-oscillator
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# QuantifiedTrader Projection Oscillator zero-cross long-flat on BTCUSDT 1d bars

## Provenance

**Primary source (fetched live over HTTPS this cycle):** QuantifiedTrader public strategy-library page `https://quantifiedtrader.com/backtest/strategies/projection-oscillator` (`Projection Oscillator`), fetched 2026-11-04 as a 43,013-byte page (SHA-256 `19e7db9cf44885e924990b09be42b1f3fcb4c8c310afb9b525797219d6e300da`). The page prints no login, paywall, author handle, or creation stamp (adopted `source_as_of` is the fetch date, per the merged QuantifiedTrader Raff-Channel lane precedent). The strategy-implementation code block is printed verbatim on the page (backtesting.py shape):

```text
class ProjectionOscillator(Strategy):
    n = 14
    def init(self):
        self.po = self.I(_projection_oscillator, self.data.High, self.data.Low, self.data.Close, self.n)
    def next(self):
        if self.po[-1] > 0 and self.po[-2] <= 0 and not self.position:
            self.buy()
        elif self.po[-1] < 0 and self.position:
            self.position.close()
```

Code census this cycle over the rendered visible text (scripts/styles stripped): 1 `buy()` / 1 `position.close()` / 0 short/sell-short calls / 0 stop/limit/trailing/time calls / 1 indicator registration (`self.I`, High+Low+Close args) / 0 volume reads by any order-gating line. The `stop` substring occurs only inside fetched script/analytics payloads (zero occurrences in visible text). This record cites and normalizes the rule and reproduces no source block beyond the short declarations quoted for gate evidence.

**Facts actually supplied by the source page:** backtested on **daily OHLCV** across major US equity indices and ETFs (S&P 500, NASDAQ Composite, DJI, Russell 2000, +16 more); entry/exit signals carry **no lookahead bias**; **trades execute at the open of the bar following the signal**; performance metrics are computed per symbol; **transaction costs and slippage are not modeled**. Signal prose: the oscillator projects a linear regression line forward and measures where price sits relative to the projected high-low range; long when the oscillator crosses above zero, exit on the reverse. No return, Sharpe, win-rate, or trade-count figure from the source is carried into the derived specification. The site's separate aggregate overview table (per-strategy SL/TP lab columns on a different page) is not adopted anywhere — this page ships no stop/target, and this record invents none.

**Unpinned-helper gap (disclosed, not repaired):** the page calls a shared site helper `_projection_oscillator(high, low, close, n)` whose body is printed nowhere on the page (the name occurs exactly once in the whole fetch, at the call site — verified this cycle). This derivative therefore does **not** claim byte-equivalence with the site's helper. It freezes a textbook Chande-style projected-range oscillator — one-step-ahead OLS projections of the trailing high/low ranges with the close scored centered inside that projected range — as an explicit researcher choice, fully specified below. This choice carries no seeding ambiguity: closed-form OLS over completed bars is arithmetically exact from the first full window, so no framework-equivalence question arises beyond the disclosed formula (the same treatment the merged Raff-Channel lane record gave its unprinted `_raff_channel` helper). Any other projection construction is a different, unpinned rule.

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the source ships equity-universe backtesting.py semantics with no venue/fill/cost leg this record can reuse verbatim. Researcher-declared adaptations are exactly six: (1) market pin **BTCUSDT Binance spot 1d** (long-flat needs no margin-short permission; spot is the minimal realistic venue — the source's equity-index universe is kept separate, never claimed); (2) completed-bar decisions with **next-bar-open market** fills (the source's own stated execution — "trades execute at the open of the bar following the signal" — preserved verbatim); (3) input frozen at `n = 14` with the closed-form projected-range oscillator below (any other window or projection construction is a different, unpinned rule); (4) adopted **60-bar warmup** with pre-warmup bars flat by record rule (structural minimum is index 13 — first 14-bar window — verified this cycle; 60 follows the merged QuantifiedTrader 1d sibling package with conservative margin); (5) house sizing/costs replacing the source's no-cost model (fixed 0.01 BTC, 0.1%/side taker; spot means no funding leg exists — constructive exclusion, never zero-claimed; fixed size is event-neutral for timing under state-independent signals); (6) missing-bar stretches freeze evaluation at the prior target — book and ledger retained across the freeze, evaluation resumes on the next valid bar with no warmup repetition, never backfilled, never forced flat. The cross-up entry edge, the below-zero exit level, the long-only stance, and the no-stop/no-target posture are source-pinned or predeclared; no short leg is invented.

**Immutable derivative identity:** `qtprosc:ProjectionOscillator-projrange-14_zero-cross|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001-nofunding|spot1x|nostop-notarget|warmup60|2026-11-04`. Changing any input, projection construction, comparator, direction, timing, market, risk, cost, sizing, or book state creates a different derivative.

**Pre-write dedup (2026-11-04):** working-tree base is current `main@743ff2fd` (561 root strategy records, READMEs excluded; this file is the 562nd). Content searches for `ProjectionOscillator`, `_projection_oscillator`, `projection-oscillator`, and `Projection Oscillator` return zero same-source/same-construction records — the only same-helper hit pool-wide is a passing mention inside the merged QuantifiedTrader intraday-intensity record's sibling-helper fence (not a signal, never a twin), and the only word-boundary `projection` hits are generic English uses in three unrelated records (volume-block RSI, Hurst-composite, Kroha-Hurst). The pool's nearest zero-cross cousins are all fenced as different signal objects (Negative evidence 1–3). No open `research/*` PR is this page, author, construction, or signal (17 open PRs enumerated this cycle — #48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708, #725 — titles contain no projection hit; the QuantifiedTrader sitemap's eight already-mined siblings are disparity-index, fractal-breakout, intraday-intensity, raff-channel, random-walk-index, twiggs-money-flow, volume-price-trend, plus the Schaff/KST lane records from other sources). No duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

Projected-range position timing, long side only. The construction is self-describing: a linear regression line is projected forward from recent bars, price is scored by where the close sits inside the projected high-low range, and a cross above zero holds the long thesis; the first print below zero ends it. The page prose claims only this projection intuition — this record adopts none of it beyond the coded comparisons. The equity-index universe and the unmodeled-costs stance are source facts, not this record's venue or economics. No performance figure is carried anywhere.

### Research interpretation

Regression-projected-range zero-cross, long-flat — an *edge-in, level-out* object. Unlike the pool's band-breakout cousins (which wait for a close to pierce a volatility rail — rare, explosive events), this rule enters on the first bar the close prints above the projected mid-range: participation keys off the forecast, not the realized extreme. Unlike the pool's slope-sign cousins (which trade the *tilt* of a regression line and can stay positioned while price sits far from it), this rule never reads any slope — only the close's centered position inside the one-step-ahead projected range, so a flat market that drifts above its own projected midpoint still arms. Unlike SMA-level cousins, the projected range adapts to trend (both rails tilt with the regression), so the zero line is a moving forecast-relative reference, not a backward average. The failure mode is plain: in a steady compounding climb the projected range climbs with price and the level can stay unarmed the whole way up (the planted sustained-up tape arms zero times), while a grinding decline keeps it pinned below zero with no guardrail either way — disclosed, not upgraded.

## Signal

Exact rule as pinned (daily decision on completed `1d` bars; entries/exits next-bar-open market; long-flat single-unit book — any other input, projection construction, comparator, sizing, fill, or cost is a different, unpinned rule):

- R1 — Measure grid: completed `1d` bars of BTCUSDT spot only. Continuous calendar days; no session template, no holiday skip. Bar time is never read by any order-gating line.
- R2 — Source series: `H[t]`, `L[t]`, `C[t]` are the sole signal inputs (`O[t]` never read by any order-gating line — fills price at opens; notionals reference closes for cost sizing only). No volume, no funding/OI/mark-index read gates on any order; no sentiment/macro/on-chain/cross-venue state. Single timeframe, single asset.
- R3 — Projected oscillator (frozen, researcher-pinned textbook construction): over trailing `H[t-13..t]` / `L[t-13..t]`, fit ordinary-least-squares lines on `x = 0..13` and project one step ahead: `PH[t] = aH + bH·14`, `PL[t] = aL + bL·14` (closed form: `b = (n·Σxy − Σx·Σy)/(n·Σx² − (Σx)²)`, `a = (Σy − b·Σx)/n`, `n = 14`). `PO[t] = 2·(C[t] − PL[t])/(PH[t] − PL[t]) − 1`. Finite exactly when all 14 trailing highs/lows/close are finite and `PH[t] > PL[t]` (first possible at index 13 — verified this cycle). Degenerate (`PH ≤ PL`) or non-finite prints force NaN → hold (no signal, no close).
- R4 — Entry (pinned, cross-up edge): if FLAT and `PO[t] > 0` and `PO[t-1] <= 0` (post-warmup) → buy at the next open. A NaN prior bar never satisfies the edge (comparison is false), so seeding can never smuggle an entry.
- R5 — Exit (pinned, below-zero level): if LONG and `PO[t] < 0` → close the whole book at the next open. Exact zero (`PO == 0`) neither enters (needs strict `>`) nor exits (needs strict `<`), by the comparators as coded.
- R6 — Risk legs (file absence, not invented): stop-loss, take-profit, trailing, and any second exit are all explicitly disabled — the program ships none, and no prose ships any. The below-zero print is the sole exit path.
- R7 — Position state (single deterministic path — no reset, no re-warmup): one 0.01-BTC unit max, long or flat. Safety orders: explicitly none. No cooldown: after any close, the next cross-up bar re-enters at its next open (`not self.position` guard preserved — while LONG, cross-up bars are no-ops; while FLAT, below-zero bars are no-ops). Entries and exits can never co-fire on the same bar (entry needs `PO > 0`, exit needs `PO < 0` — disjoint by arithmetic, including degenerate tapes).
- R8 — Warmup: flat until 60 completed `1d` bars (structural minimum is index 13; 60 follows the merged QuantifiedTrader 1d sibling package with margin — verified this cycle). The 60-bar pin is frozen: a longer warmup prints the same signal series but a different forced-flat-restart book (this cycle's 150-bar restart prints 332/331 vs the pinned 342/341), so it is a different, unpinned claim.
- R9 — Invariant identifier: `qtprosc:ProjectionOscillator-projrange-14_zero-cross|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001-nofunding|spot1x|nostop-notarget|warmup60|2026-11-04` (any input, construction, comparator, direction, sizing, fill, risk, or cost change is a different derivative).

## Required data

- Completed `1d` bars of BTCUSDT: `H[t]`/`L[t]` (range projection) and `C[t]` (position inside the projected range) are the sole series the formula reads (`O[t]` fills only; notionals reference closes for cost sizing only). No `volume`, no funding-signal, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; the single window reads trailing completed bars only, never a second feed).
- Warmup: 60 completed `1d` bars flat by record rule — structural minimum is the 14th completed bar (binding leg: 14-bar OLS projection window, verified finite at index 13 this cycle; first decidable edge at index 14 since the entry reads `PO[t-1]`). Pre-warmup and any NaN-signal bars are flat/hold by record rule; missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (the window reads completed bars including the decision bar only), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance spot, 1x, fixed 0.01 BTC per unit, single-unit book, no compounding. Long side explicitly enabled; short side explicitly disabled (zero short tokens anywhere in the printed program). Fills are never conditional on equity or buying power.
- Order timing (source-stated timing preserved verbatim): completed-bar decision with next-bar-open market fills for entries and whole-book closes — the source prose states "trades execute at the open of the bar following the signal", and this record adopts exactly that (the same verified execution primitive as the merged FMZ/QuantifiedTrader lane records; with no stop/limit legs anywhere in the derived machine there is no same-bar TP/SL ordering ambiguity; each bar's outcome is a single deterministic event: hold, open-long, or close-flat). This record claims no other fill convention: no same-bar-close print, no maker-touch, no intrabar-path-dependent fill.
- Pinned engine path (verified at the pin this cycle): Hummingbot package label `20260920`, VERSION `dev-2.17.0` (local checkout `2dbc844fadb9d863b3ab0af1b8ab100472102e42` carries `hummingbot/VERSION` file `2.17.0`, verified live this cycle; `8b0e067e80ab62f10846d518dcb5a8218527ddb3` is an ancestor of the local checkout, verified via `merge-base --is-ancestor` this cycle; code paths verified at the pin this cycle: `async def run_backtesting` in `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py:221`, `def determine_executor_actions` in `hummingbot/strategy/strategy_v2_base.py:747`, `class OrderExecutorSimulator` in `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py:9`, `INTERVALS "1d" = "1d"` in `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py:24`). Prior merged Alpha PR **#414** reports a 902/902 wheel-file byte match and 33-assert representative validation for this source/package path; this Scout did not independently rehash the wheel. A different deployed package must be revalidated. A strategy-specific, not-yet-implemented controller must compute the trailing projected-range zero-cross state pin via `CreateExecutorAction(OrderExecutorConfig)` market legs; the generic executor does not calculate the strategy. The precomputable oscillator series plus edge/level state machine is a plain signal series, not a new execution primitive; no new data requirement, no representative-capability validation owed.
- Stop/limit modeling: none — the derived spec carries zero stop/limit/trailing legs by record rule. No hidden Hummingbot stop-order defaults are relied upon, and with no stop/limit legs there is no same-bar TP/SL ordering ambiguity.
- Sizing/capital/costs: the source models no costs (recorded as the source's, never adopted). Explicit house overlay: single-unit frame, 0.1% taker fee per filled side, slippage unmodeled by declaration; fixed size is event-neutral for timing under state-independent signals. Exchange facts re-verified live this cycle via `api/v3/exchangeInfo`: `BTCUSDT`, `TRADING`, `tickSize 0.01`, min-qty/step 0.00001/0.00001, min-notional 5.0 (`NOTIONAL`). The fixed 0.01 BTC (≈774.54 USDT at the cycle's last completed close 77,453.86 on 2026-11-03, above the 5.0 min-notional and an exact multiple of the 0.00001 step). Spot venue means no funding leg exists — constructive exclusion, never modeled-or-realized funding.
- Concurrency: at most one single-asset engine position at any time; the below-zero print ends it (re-entry earliest next signal). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no hedge-mode requirement by construction.

## Evidence

### Source-reported

With exact provenance (page fetched live 2026-11-04, 43,013 bytes, SHA-256 `19e7db9cf44885e924990b09be42b1f3fcb4c8c310afb9b525797219d6e300da`; implementation block `class ProjectionOscillator(Strategy)` with `n = 14`, `_projection_oscillator(High, Low, Close, n)` registration (helper body unprinted — name occurs once, at the call site), `po[-1] > 0 and po[-2] <= 0 and not position → buy()`, `po[-1] < 0 and position → position.close()`): the frozen input (`n 14`); the High/Low/Close indicator read; the cross-up-entry / below-zero-exit polarity; the `not self.position` single-unit guard; the long-only order set (zero short/stop/limit/time calls in visible text); the source's daily-OHLCV frame, no-lookahead statement, next-bar-open execution, unmodeled-costs stance, and equity-index universe (S&P 500, NASDAQ Composite, DJI, Russell 2000, +16 more). This record claims no source-reported performance number as its own — no return, Sharpe, win rate, or trade count is carried into the derived specification — and no reproduced performance exists.

### Independently reproduced

**None.** No strategy backtest, event-level Qlib/Hummingbot parity, wheel rehash, deployment or profitability experiment occurred. Pinned engine source inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifacts this run are researcher self-checks of the predicate/estimator/state pipeline (closed-form OLS-14 projected range, 60-bar warmup, cross-up/level-down next-open single-unit long-flat machine), run in scratch (never committed): logic verification only, not a backtest, not parity.

**Planted-tape verification (this cycle, deterministic, double-run identical):** TAPE-flat (dead-constant 170-bar tape) prints 0 entries / 0 exits ending FLAT (digest `e3b0c442`) — the oscillator prints exact `0.0` on the constant tape and the strict edge never arms, as pinned; TAPE-up (sustained +1%/day compounding 170-bar tape) prints 0 entries / 0 exits ending FLAT (digest `e3b0c442`) — the projected range climbs with price and the level never arms on the steady climb, as pinned (disclosed limitation, not patched); TAPE-down (sustained −1%/day 170-bar tape) prints 0 entries / 0 exits ending FLAT (digest `e3b0c442`) — the oscillator stays pinned below zero through the grind, as pinned; TAPE-volregime (deterministic 170-bar ±0.2%-then-±2% alternation tape) prints 55 entries / 54 exits ending LONG (digest `2920fe03`) — both transition paths are exercised, as pinned.

**Live-exchange microstructure probes (this cycle, Binance spot 1d klines, 3,366 completed bars 2017-08-17→2026-11-03, last close 77,453.86; the in-progress 2026-11-04 bar excluded):** 342 cross-up post-warmup bars drive 342 entries / 341 exits ending LONG (longest completed hold 16 bars — non-degenerate, non-buy-and-hold). Two independent runs produce identical digests (event-series digest `e230d705`). Admission is engineering capability, never an event-rate or profitability claim.

### Negative evidence

1. Zero-cross-cousin fence, quantified plainly: pool `forven-roc-zero-cross-momentum` trades a volume-free ROC(12) zero level; pool `twiggs-money-flow-21-zero-cross` trades a volume-weighted money-flow zero; pool `quantifiedtrader-intraday-intensity-21-zero-cross` trades an intraday-intensity zero. This record trades neither ROC, money flow, nor intraday intensity — it trades the close's centered position inside a one-step-ahead OLS-projected high-low range (`n = 14`, High+Low+Close inputs). Different signal object, different inputs, never a twin.
2. Slope-sign fence: pool linreg-slope records trade the *tilt* of a regression line; this record never reads any slope — both rails' tilts enter only through the projected range they imply, and a steeply rising projection with the close beneath its midpoint still exits here and holds there. Different signal object, never a twin.
3. Band-level fence: pool Bollinger/std-dev records trade closes against backward-looking SMA±kσ rails; this record's rails are forward-projected OLS ranges with no standard-deviation term anywhere. Different construction, never a twin.
4. Entry/exit-asymmetry fence: the entry is an *edge* (cross-up needs two consecutive prints) while the exit is a *level* (any below-zero print closes). A record symmetrizing both to edges, or both to levels, prints a different, unpinned event set; a reviewer must not swap it in.
5. Exact-zero fence: `PO == 0` neither enters nor exits by the strict comparators as coded (the planted TAPE-flat exercises this path with 0/0). A record adding a zero-touch arm prints a different, unpinned event set.
6. NaN fence: any non-finite window print, and any degenerate `PH ≤ PL` projection, holds with no signal and no close. Interpolating, seeding, or backfilling is a different, unpinned rule.
7. Derivation-boundary fence: the unmodeled-costs stance and equity-index universe are the source's, never adopted — the next-open fixed-size spot machine with the frozen projected-range construction is the predeclared derivation, never a source claim; this record is therefore never evidence that the site endorses any executable posture. A reviewer must not substitute a same-bar-close, stop-carrying, futures-margined, or two-sided variant into this record. The site's separate aggregate-table SL/TP lab columns (different page) are explicitly not adopted.
8. Helper-construction fence: the record pins the centered projected-range formula `PO = 2·(C−PL)/(PH−PL) − 1` with one-step-ahead OLS rails. Any other projection (close-deviation-from-trend, SMA/EMA-centered, median, or band-derived proxy) prints a different, unpinned event set; a reviewer must not promote an alternative into the signal to reshape the record.
9. Single-print-twin fence: no twin is admitted — any input change (e.g. 14→20 window), any dropped comparator strictness, any volume-gated or slope-gated variant, any other frame, fill, venue, or book is a different, unpinned rule.
10. Warmup-identity fence, admitted plainly: the 150-bar forced-flat restart prints 332/331 events vs 342/341 at the pinned 60 — the same signal series but a different book. Warmup 60 is frozen, not exemplary; any other warmup is a different, unpinned claim.
11. Number silence fenced: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from any source is adopted anywhere, and any dispute over exact magnitudes is decided against this record, never patched by inference.
12. Version fence: this record follows the QuantifiedTrader page as fetched 2026-11-04 (no printed creation stamp; fetch-date pin). If the page is ever edited, this record does not move with it.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: input `14` / projected-range construction / cross-up-entry / below-zero-exit / long-flat book / no-stop-no-target posture / `1d` BTCUSDT spot / next-open fills / 0.01 BTC / 0.1% costs / 60-bar warmup are frozen.

- F1 — Projection relevance: an SMA14-midpoint twin (enter on cross above / exit below the trailing `(highest(high,14)+lowest(low,14))/2` midpoint — same rest) must not improve net expectancy; fail ⇒ the OLS projection adds nothing over a Donchian midpoint, and the record is a range label rather than a projection edge.
- F2 — Edge-vs-level relevance: a level-entry twin (enter on any above-zero bar while flat, not just the cross-up edge — same rest) must not improve net expectancy; fail ⇒ the restrictive edge adds nothing over permissive level participation, and the record's entry is decorative.
- F3 — Exit relevance: an edge-exit twin (exit only on the cross-down edge after at least one full bar above — same rest) must not improve net expectancy; fail ⇒ the level exit adds nothing over the edge, and the record's exit is decorative.
- F4 — Warmup relevance: the pinned 60 print and a 60-vs-60 re-run must print the identical event set (determinism check — digest `e230d705` is the tripwire); fail ⇒ nondeterminism or seed leakage past the declared warmup.

## Crypto portability

Pinned to BTCUSDT Binance spot under the house overlay (declared port of an equity-index-headed backtesting.py program). The rule reads completed daily bars only, so no pit-session, gap, roll, split/dividend-adjustment, or corporate-action logic ports (equity-calendar effects are non-issues on spot — disclosed, not modeled). The composite is unit-free in range-ratio terms (no absolute-price threshold anywhere), so unlike price-level systems the rule ports across venues without re-scaling — yet projected-range timing on crypto microstructure (24/7 bars, stablecoin-quoted prints, volatility-regime shifts the source never traded) fires at a cadence the source never measured (342 entries across 3,306 post-warmup bars here, longest hold 16 bars), disclosed without re-tuning. The rule is long-flat, so a spot deployment expresses the full machine with no short permission — a two-sided or perpetual variant would be a different, unpinned claim (this record's gate-5 evidence is the spot path only; the source's equity universe is provenance, not execution). No warmup history beyond 60 `1d` bars is consumed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Never-arms by design: the planted sustained-up tape arms zero times across 170 compounding-climb bars — a steady trend that drags the projected range with it never prints the edge, by the prescribed design (the live window still prints 342 entries across 3,306 post-warmup bars with only the below-zero print as exit — disclosed, not upgraded).
- Single-venue port residual: backtesting.py close/open arithmetic vs Binance spot execution (prints, fees, open-definition across 24/7 sessions, equity-vs-crypto regime differences) is unclaimed, disclosed.
- Next-open latency idealization: signal cadence on the decision close print while fills land on the next open; any live gap between the two differs by construction — disclosed, research-only (this convention is the source's own stated execution, preserved verbatim).
- No-authorship-page residual: the page prints no handle, license, or creation stamp; provenance rests on the QuantifiedTrader URL/slug, printed names, page hash, and fetch date — disclosed.
- Performance evidence is absent: nothing here is calibrated, fitted, or tuned to any backtest (the `n = 14` default is the source's, never re-run here; the page's own grid-search section, where available, is not adopted as a parameter source).
- Author scope: the page ships exploratory research with an explicit not-investment-advice disclaimer, not a vetted trading system — this record is research-only and claims no live suitability.

## Implementation status

`not-implemented`: no dedicated controller, Qlib executable recipe or deployment artifact was created. PASS is a bounded research-expressibility proposal, not a claim of already runnable materialization. A selected strategy may later need the minimal strategy-specific implementation without a second admission flag.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review must independently inspect this exact PR head, remediate only primary-source-verifiable facts, then PASS exact-head merge or NOT_LOSSLESS close. Scout does not approve, merge, close, trade, backtest or deploy.

## Related Wiki records

None asserted.

## Sources

- Primary page + pin: https://quantifiedtrader.com/backtest/strategies/projection-oscillator (`Projection Oscillator`; page fetched live 2026-11-04, 43,013 bytes, SHA-256 `19e7db9cf44885e924990b09be42b1f3fcb4c8c310afb9b525797219d6e300da`; implementation block `class ProjectionOscillator(Strategy)` with `n = 14`, `_projection_oscillator(High, Low, Close, n)` registration (helper body unprinted — name occurs once, at the call site), `po[-1] > 0 and po[-2] <= 0 and not position → buy()`, `po[-1] < 0 and position → position.close()`; zero short/stop/limit/trailing/time calls in visible text; daily OHLCV frame, no-lookahead statement, next-bar-open execution, unmodeled costs, equity-index universe S&P 500 / NASDAQ / DJI / Russell 2000 +16)
- Lane precedent (different mechanism, unmerged-proof never claimed): `quantifiedtrader-raff-channel-midline-level-long-flat-btcusdt-1d-2026-11-04.md` (unprinted-helper textbook-freeze derivation pattern with 60-bar warmup)
- Nearest pool lineages (different mechanisms, unmerged-proof never claimed): `forven-roc-zero-cross-momentum-*` (ROC-level zero object); `twiggs-money-flow-21-zero-cross-*` (volume-weighted money-flow zero); `quantifiedtrader-intraday-intensity-21-zero-cross-*` (intraday-intensity zero; carries a passing `_projection_oscillator` sibling-helper mention, never a signal)
- Exchange verification: Binance spot `api/v3/exchangeInfo` (`BTCUSDT`, `TRADING`, `tickSize 0.01`, min-qty/step 0.00001/0.00001, min-notional 5.0 via `NOTIONAL`) plus `api/v3/klines` 1d probes (3,366 completed bars 2017-08-17→2026-11-03, 342 cross-up post-warmup bars → 342 entries / 341 exits ending LONG, longest completed hold 16 bars, event digest `e230d705` double-run identical; 150-bar restart prints 332/331 — warmup-identity fence), fetched live 2026-11-04
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently merged pinned package/source evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
