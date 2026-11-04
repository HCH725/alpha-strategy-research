---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: QuantifiedTrader ATR Bands lower-touch midline-exit long-flat on BTCUSDT 1d bars
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
  - https://quantifiedtrader.com/backtest/strategies/atr-bands/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# QuantifiedTrader ATR Bands lower-touch midline-exit long-flat on BTCUSDT 1d bars

## Provenance

**Primary source (fetched live over HTTPS this cycle):** QuantifiedTrader public strategy-library page `https://quantifiedtrader.com/backtest/strategies/atr-bands/` (`ATR Bands`), fetched 2026-11-05 as a 42,764-byte page (SHA-256 `f535db27e01bd351c7a622046fd0f2b0b726b802ed37e3edff617dc33e639664`). The page prints no login, paywall, author handle, or creation stamp (adopted `source_as_of` is the fetch date, per the merged QuantifiedTrader Raff-Channel / Projection-Oscillator / Keltner-Squeeze lane precedent). The strategy-implementation code block is printed verbatim on the page (backtesting.py shape):

```text
class ATRBands(Strategy):
    n = 14; mult = 2
    def init(self):
        upper, mid, lower = _atr_bands(self.data.Close, self.data.High, self.data.Low, self.n, self.mult)
        self.mid = self.I(lambda: mid, name="Mid")
        self.lower = self.I(lambda: lower, name="Lower")
    def next(self):
        if self.data.Close[-1] <= self.lower[-1] and not self.position: self.buy()
        elif self.data.Close[-1] >= self.mid[-1] and self.position: self.position.close()
```

Code census this cycle over the rendered visible text before the backtest-data loader (scripts/styles stripped): 1 `buy()` / 1 `position.close()` / 0 short/sell-short order calls / 0 stop/limit/trailing/time/target/profit calls / 2 indicator registrations (`self.I`) / 0 volume reads by any order-gating line. Helper-name census: `_atr_bands` 1, exactly at its call site, with zero `def _` definitions printed anywhere — the helper body is unprinted, the same gap shape the merged Raff-Channel / Projection-Oscillator / Keltner-Squeeze lane records froze via textbook construction. This record cites and normalizes the rule and reproduces no source block beyond the short declarations quoted for gate evidence.

**Facts actually supplied by the source page:** backtested on **daily OHLCV** across major US equity indices and ETFs (S&P 500, NASDAQ Composite, DJI, Russell 2000, +16 more); entry/exit signals carry **no lookahead bias**; **trades execute at the open of the bar following the signal**; performance metrics are computed per symbol; **transaction costs and slippage are not modeled**. Signal prose: ATR Bands place upper and lower bands around a rolling SMA using ATR multiples; long on a lower-band touch (mean-reversion); exit when price returns to the midline. Prose and program agree on every executable leg — no prose-vs-code mismatch exists on this page (unlike the Keltner-Squeeze sibling). No return, Sharpe, win-rate, or trade-count figure from the source is carried into the derived specification. The page's parameter grid-search section, where available, is not adopted as a parameter source.

**Dead-rail disclosure (code fact):** the helper returns three rails but only `Mid` and `Lower` are registered and read — `upper` is computed-but-never-registered, and no order-gating line references it anywhere. The executable rule is therefore a lower-touch/midline-exit machine; the upper band is display-only residue. A reviewer must not invent an upper-band exit, stop, or target into this record.

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the source ships equity-universe backtesting.py semantics with no venue/fill/cost leg this record can reuse verbatim. Researcher-declared adaptations are exactly six: (1) market pin **BTCUSDT Binance spot 1d** (long-flat needs no margin-short permission; spot is the minimal realistic venue — the source's equity-index universe is kept separate, never claimed); (2) completed-bar decisions with **next-bar-open market** fills (the source's own stated execution — "trades execute at the open of the bar following the signal" — preserved verbatim); (3) inputs frozen at `n = 14, mult = 2` with the closed-form textbook envelope below (SMA14 mid + Wilder ATR14, SMA-seeded — the same seeding convention as the merged Keltner-Squeeze sibling); (4) adopted **60-bar warmup** with pre-warmup bars flat by record rule (structural minimum is index 14 — first full SMA14 window plus first seeded Wilder ATR14 print — verified this cycle; 60 follows the merged QuantifiedTrader 1d sibling package with conservative margin); (5) house sizing/costs replacing the source's no-cost model (fixed 0.01 BTC, 0.1%/side taker; spot means no funding leg exists — constructive exclusion, never zero-claimed; fixed size is event-neutral for timing under state-independent signals); (6) missing-bar stretches freeze evaluation at the prior target — book and ledger retained across the freeze, evaluation resumes on the next valid bar with no warmup repetition, never backfilled, never forced flat. The lower-touch entry, the midline exit, the long-only stance, and the no-stop/no-target posture are source-pinned or predeclared; no short leg is invented.

**Immutable derivative identity:** `qtatrband:ATRBands-sma14-atr14x2-lower-touch_mid-exit|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001-nofunding|spot1x|nostop-notarget|warmup60|2026-11-05`. Changing any input, envelope construction, seed, comparator, direction, timing, market, risk, cost, sizing, or book state creates a different derivative.

**Pre-write dedup (2026-11-05):** working-tree base is current `main@5ccc26f9` (563 root strategy records, READMEs excluded; this file is the 564th). Content searches for `ATRBands`, `atr_bands`, and the canonical slug `strategies/atr-bands` return zero same-source/same-construction records (the pool's `ATR Bands` prose mentions are generic cousin fences inside unrelated records, never this page or construction). No open `research/*` PR is this page, author, construction, or signal (17 open PRs enumerated this cycle — #48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708, #725 — none is an ATR-band, QuantifiedTrader-ATR, or lower-touch-reversion machine). The pool's ATR/envelope cousins are all fenced as different signal objects (Negative evidence 1–6). No duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

Lower-band-touch mean-reversion, long side only. The construction is self-describing: a slow SMA midline marks the average, two average true ranges below it mark how far price may stretch before the dip counts as extended, a close printing at or through the lower rail holds the reversion thesis, and the first close back at or above the midline ends it. The equity-index universe and the unmodeled-costs stance are source facts, not this record's venue or economics. No performance figure is carried anywhere.

### Research interpretation

Dip-in, midline-out object — the mirror image of the merged Keltner-Squeeze sibling (which breaks *above* a manufactured rail and exits on an average). Unlike the pool's Donchian cousins (which trade raw highest-high/lowest-low extremes every print actually touched), both rails here are manufactured (SMA plus/minus scaled ATR), so entries key off volatility-normalized displacement rather than realized extremes. Unlike the pool's breakout ATR channel (Forven's prev-close-anchored ±2×ATR machine, which buys expansion), this rule buys *weakness* against a slow average and holds only until the average is reclaimed — the round trip is bounded by construction to one stretch-and-snap. Unlike RSI/volume-gated dip buyers (Super-Scalper, Bandtastic, BB-RSI-dip), this rule carries no confirmation gate at all — any lower-rail touch arms, exhausted or cascading. The failure mode is plain: a sustained bleed that keeps printing below the sinking lower rail adds no second unit but never exits either (the planted sustained-down tape enters once and rides LONG to the tape end — disclosed, not upgraded); a vertical ramp never touches and never participates (the planted sustained-up tape arms zero times — disclosed).

## Signal

Exact rule as pinned (daily decision on completed `1d` bars; entries/exits next-bar-open market; long-flat single-unit book — any other input, envelope construction, seed, comparator, sizing, fill, or cost is a different, unpinned rule):

- R1 — Measure grid: completed `1d` bars of BTCUSDT spot only. Continuous calendar days; no session template, no holiday skip. Bar time is never read by any order-gating line.
- R2 — Source series: `H[t]`, `L[t]`, `C[t]` are the sole signal inputs (`O[t]` never read by any order-gating line — fills price at opens; notionals reference closes for cost sizing only). No volume, no funding/OI/mark-index read gates on any order; no sentiment/macro/on-chain/cross-venue state. Single timeframe, single asset.
- R3 — Envelope (frozen, researcher-pinned textbook construction for the unprinted helper): `SMA14[t]` is the plain 14-bar mean of closes (first finite at index 13); `ATR14[t]` is the Wilder RMA of true ranges seeded by the SMA of the first 14 true ranges (first finite at index 14); `Mid[t] = SMA14[t]`; `Lower[t] = Mid[t] − 2.0 · ATR14[t]` (`Upper[t] = Mid[t] + 2.0 · ATR14[t]` is computed inside the helper but never registered and never read by any order-gating line — dead rail by code fact). Finite exactly when all trailing inputs are finite (first possible at index 14 — verified this cycle). The seeding convention is part of the pin: any other seed (e.g. first-close seed, SMA-ATR seed) prints a different, unpinned series.
- R4 — Entry (pinned, lower-touch): if FLAT and `C[t] <= Lower[t]` (post-warmup) → buy at the next open. Touch counts (`<=`), as coded — a close exactly on the rail enters.
- R5 — Exit (pinned, midline reclaim): if LONG and `C[t] >= Mid[t]` → close the whole book at the next open. Touch counts (`>=`), as coded — a close exactly on the midline exits. The program ships no NaN guard, but a non-finite rail never satisfies either comparison (NaN `<=`/`>=` is false), so seeding can never smuggle an entry or an exit; pre-warmup and NaN-signal bars are flat/hold by record rule.
- R6 — Risk legs (file absence, not invented): stop-loss, take-profit, trailing, time exit, and any second exit are all explicitly disabled — the program ships none, and no prose ships any executable one. The midline print is the sole exit path.
- R7 — Position state (single deterministic path — no reset, no re-warmup): one 0.01-BTC unit max, long or flat. Safety orders: explicitly none. No cooldown: after any close, the next lower-touch bar re-enters at its next open (`not self.position` guard preserved — while LONG, touch bars are no-ops; while FLAT, above-lower bars are no-ops). Entry and exit can never co-fire while `Lower[t] < Mid[t]` (needs `C <= Lower` and `C >= Mid` jointly — impossible); only the degenerate `ATR14[t] = 0` collapse (`Lower == Mid`) admits a co-fire bar, where the program's `if/elif` order resolves entry-first — deterministic by code order, exercised by no tape this cycle, disclosed.
- R8 — Warmup: flat until 60 completed `1d` bars (structural minimum is index 14; 60 follows the merged QuantifiedTrader 1d sibling package with margin — verified this cycle). The 60-bar pin is frozen: a longer warmup is a different, unpinned claim even where it prints the same book (this cycle's 150-bar restart prints an identical 33/33 — reported, not promoted into the pin).
- R9 — Invariant identifier: `qtatrband:ATRBands-sma14-atr14x2-lower-touch_mid-exit|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001-nofunding|spot1x|nostop-notarget|warmup60|2026-11-05` (any input, construction, seed, comparator, direction, sizing, fill, risk, or cost change is a different derivative).

## Required data

- Completed `1d` bars of BTCUSDT: `H[t]`/`L[t]` (true-range path inside ATR14) and `C[t]` (SMA source and both comparisons) are the sole series the formula reads (`O[t]` fills only; notionals reference closes for cost sizing only). No `volume`, no funding-signal, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; the windows read trailing completed bars only, never a second feed).
- Warmup: 60 completed `1d` bars flat by record rule — structural minimum is index 14 (binding legs: 14-bar SMA window plus the seeded Wilder ATR14, verified first-finite at index 14 this cycle). Pre-warmup and any NaN-signal bars are flat/hold by record rule; missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (windows read completed bars including the decision bar only — same-bar comparison, no lag, no negative shift), no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance spot, 1x, fixed 0.01 BTC per unit, single-unit book, no compounding. Long side explicitly enabled; short side explicitly disabled (zero short/sell-short order tokens in the printed program). Fills are never conditional on equity or buying power.
- Order timing (source-stated timing preserved verbatim): completed-bar decision with next-bar-open market fills for entries and whole-book closes — the source prose states "trades execute at the open of the bar following the signal", and this record adopts exactly that (the same verified execution primitive as the merged FMZ/QuantifiedTrader lane records; with no stop/limit legs anywhere in the derived machine there is no same-bar TP/SL ordering ambiguity; each bar's outcome is a single deterministic event: hold, open-long, or close-flat, with the documented `if/elif` priority only reachable in the degenerate zero-ATR collapse). This record claims no other fill convention: no same-bar-close print, no maker-touch, no intrabar-path-dependent fill.
- Pinned engine path (verified at the pin this cycle): Hummingbot package label `20260920`, VERSION `dev-2.17.0` (local checkout `2dbc844` carries `hummingbot/VERSION` file `2.17.0`, verified live this cycle; `8b0e067e80ab62f10846d518dcb5a8218527ddb3` is an ancestor of the local checkout, verified via `merge-base --is-ancestor` this cycle; code paths verified at the pin this cycle: `async def run_backtesting` in `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py:221`, `def determine_executor_actions` in `hummingbot/strategy/strategy_v2_base.py:747`, `class OrderExecutorSimulator` in `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py:9`, `INTERVALS "1d" = "1d"` in `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py:24`). Prior merged Alpha PR **#414** reports a 902/902 wheel-file byte match and 33-assert representative validation for this source/package path; this Scout did not independently rehash the wheel. A different deployed package must be revalidated. A strategy-specific, not-yet-implemented controller must compute the trailing band-touch/midline state pin via `CreateExecutorAction(OrderExecutorConfig)` market legs; the generic executor does not calculate the strategy. The precomputable band series plus touch/reclaim state machine is a plain signal series, not a new execution primitive; no new data requirement, no representative-capability validation owed.
- Stop/limit modeling: none — the derived spec carries zero stop/limit/trailing legs by record rule. No hidden Hummingbot stop-order defaults are relied upon, and with no stop/limit legs there is no same-bar TP/SL ordering ambiguity.
- Sizing/capital/costs: the source models no costs (recorded as the source's, never adopted). Explicit house overlay: single-unit frame, 0.1% taker fee per filled side, slippage unmodeled by declaration; fixed size is event-neutral for timing under state-independent signals. Exchange facts re-verified live this cycle via `api/v3/exchangeInfo`: `BTCUSDT`, `TRADING`, `tickSize 0.01`, min-qty/step 0.00001/0.00001, min-notional 5.0 (`NOTIONAL`). The fixed 0.01 BTC (≈774.54 USDT at the cycle's last completed close 77,453.86 on 2026-11-03, above the 5.0 min-notional and an exact multiple of the 0.00001 step). Spot venue means no funding leg exists — constructive exclusion, never modeled-or-realized funding.
- Concurrency: at most one single-asset engine position at any time; the midline print ends it (re-entry earliest next signal). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no hedge-mode requirement by construction.

## Evidence

### Source-reported

With exact provenance (page fetched live 2026-11-05, 42,764 bytes, SHA-256 `f535db27e01bd351c7a622046fd0f2b0b726b802ed37e3edff617dc33e639664`; implementation block `class ATRBands(Strategy)` with `n = 14; mult = 2`, `_atr_bands(Close, High, Low, n, mult)` single call (helper body unprinted — the name occurs once, at its call site; zero `def` prints), `Mid` + `Lower` registrations (upper computed-but-never-registered), `Close[-1] <= lower[-1] and not position → buy()`, `Close[-1] >= mid[-1] and position → position.close()`): the frozen inputs; the Close/High/Low indicator reads; the lower-touch-entry / midline-exit polarity with touch-counting comparators; the `not self.position` single-unit guard; the long-only order set (zero short/stop/limit/time calls in the order path); the source's daily-OHLCV frame, no-lookahead statement, next-bar-open execution, unmodeled-costs stance, and equity-index universe (S&P 500, NASDAQ Composite, DJI, Russell 2000, +16). This record claims no source-reported performance number as its own — no return, Sharpe, win rate, or trade count is carried into the derived specification — and no reproduced performance exists.

### Independently reproduced

**None.** No strategy backtest, event-level Qlib/Hummingbot parity, wheel rehash, deployment or profitability experiment occurred. Pinned engine source inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifacts this run are researcher self-checks of the predicate/estimator/state pipeline (textbook SMA14 + Wilder ATR14 + lower/midline rails, 60-bar warmup, lower-touch / midline-reclaim next-open single-unit long-flat machine), run in scratch (never committed): logic verification only, not a backtest, not parity.

**Planted-tape verification (this cycle, deterministic):** TAPE-flat (dead-constant 170-bar tape with 0.05% wicks) prints 0 entries / 0 exits ending FLAT — the small residual ATR holds the lower rail a breath below price and the touch never arms, as pinned; TAPE-up (sustained +1%/day compounding 170-bar tape) prints 0 entries / 0 exits ending FLAT — the ramp never looks back at the trailing rail, as pinned (disclosed non-participation, not patched); TAPE-down (sustained −1%/day 170-bar tape) prints 1 entry / 0 exits ending LONG — the grind touches once and never reclaims the sinking midline, as pinned (disclosed bleed-hold, not patched); TAPE-volregime (deterministic 170-bar ±0.2%-then-±2% alternation tape) prints 3 entries / 3 exits ending FLAT — both transition paths are exercised, as pinned.

**Live-exchange microstructure probes (this cycle, Binance spot 1d klines, 3,366 completed bars 2017-08-17→2026-11-03, last close 77,453.86; the in-progress 2026-11-04 bar excluded):** 33 post-warmup lower-touch bars drive 33 entries / 33 exits ending FLAT (non-degenerate, non-buy-and-hold). Two independent runs produce identical digests (event-series digest `65e707ee`). Admission is engineering capability, never an event-rate or profitability claim.

### Negative evidence

1. Breakout-direction fence: pool `forven-atr-breakout-channel` (prev-close-anchored ±2×ATR14 simple-mean channel, 1h) buys *upper-band* expansion and exits at the *opposite* band. This record anchors on SMA14, buys *lower-rail* weakness, and exits at the *midline*. Opposite trade direction, different anchor, different ATR variant, different exit, different frame — never a twin.
2. Gated-dip fence: pool `fmz-super-scalper-rsi-atr-band-dip` (RSI-gated, two-sided, 5m) and `freqtrade-bband-rsi-dip-buy` (BB + RSI, 1h) both require oscillator confirmation and trade both sides or BB rails. This record has no RSI read anywhere, is long-flat only, and trades SMA±ATR rails on 1d. Different gates, direction, rails, and frame — never a twin.
3. Bollinger-midline fence: pool `bollinger-band-breakout-long-midline-exit` shares only the midline *exit* — its entry breaks *above* an SMA±2σ band (breakout-long) while this record touches *below* an SMA−2×ATR rail (reversion-long). Same exit rail does not make the same signal object; entry polarity is opposite — never a twin.
4. Keltner-sibling fence: the just-merged `quantifiedtrader-keltner-squeeze` (EMA20 + 2×Wilder-ATR10, fixed one-bar envelope lag, breakout-long, SMA20 exit) and this record differ on every rail input (EMA20/ATR10 vs SMA14/ATR14), comparison timing (lagged vs same-bar), trade direction (breakout vs dip), and exit (average level vs envelope midline). Same lane pattern, different machine — never a twin.
5. Donchian/extreme fence: the Donchian family (raw highest-high/lowest-low extremes) and Chandelier/StarC trailing stops trade levels the market actually printed; both rails here are manufactured (average ± scaled ATR) and may never print. Different construction — never a twin.
6. Upper-rail fence: a record entering or exiting on the upper band, adding any stop/target/cooldown/gate, flipping either comparator to strict, or moving to any other window, multiplier, frame, fill, venue, or book prints a different, unpinned event set; a reviewer must not swap any of them in.
7. NaN/seed fence: any non-finite rail print holds with no signal and no close (language-false comparisons, no guard invented); the SMA-seeded Wilder ATR convention is part of the pin. Interpolating, reseeding, or backfilling is a different, unpinned rule.
8. Single-print-twin fence: no twin is admitted — any input change (e.g. 14→20 window, 2.0→1.5 multiplier), any lagged variant, any gated or two-sided variant, any other frame, fill, venue, or book is a different, unpinned rule.
9. Warmup-identity fence, admitted plainly: the 150-bar forced-flat restart prints an identical 33/33 book at the pinned 60 — reported as a determinism observation, never promoted into the pin; any other warmup remains a different, unpinned claim.
10. Number silence fenced: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from any source is adopted anywhere, and any dispute over exact magnitudes is decided against this record, never patched by inference.
11. Version fence: this record follows the QuantifiedTrader page as fetched 2026-11-05 (no printed creation stamp; fetch-date pin). If the page is ever edited, this record does not move with it.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: inputs `14/2.0` / textbook envelope construction + seeds / lower-touch-entry / midline-exit / long-flat book / no-stop-no-target posture / `1d` BTCUSDT spot / next-open fills / 0.01 BTC / 0.1% costs / 60-bar warmup are frozen.

- F1 — Rail relevance: a Donchian-14 twin (enter on close at/below the trailing 14-bar lowest low / exit at/above the 14-bar highest high — same rest) must not improve net expectancy; fail ⇒ the SMA−ATR manufactured rail adds nothing over realized extremes, and the record is a dip label rather than an envelope edge.
- F2 — Touch relevance: a strict-inequality twin (enter on `C[t] < Lower[t]`, exit on `C[t] > Mid[t]` — same rest) must not improve net expectancy; fail ⇒ the touch-counting comparators add nothing over strict penetration, and the record's boundary inclusion is decorative.
- F3 — Exit relevance: an opposite-band twin (exit on close at/above `Upper[t]` instead of `Mid[t]` — same rest) must not improve net expectancy; fail ⇒ the midline exit adds nothing over the envelope's own far rail, and the record's snap-back exit is decorative.
- F4 — Warmup relevance: the pinned 60 print and a 60-vs-60 re-run must print the identical event set (determinism check — digest `65e707ee` is the tripwire); fail ⇒ nondeterminism or seed leakage past the declared warmup.

## Crypto portability

Pinned to BTCUSDT Binance spot under the house overlay (declared port of an equity-index-headed backtesting.py program). The rule reads completed daily bars only, so no pit-session, gap, roll, split/dividend-adjustment, or corporate-action logic ports (equity-calendar effects are non-issues on spot — disclosed, not modeled). The composite is unit-free in rail-ratio terms (no absolute-price threshold anywhere), so unlike price-level systems the rule ports across venues without re-scaling — yet dip-buying on crypto microstructure (24/7 bars, stablecoin-quoted prints, cascade dynamics the source never traded) fires at a cadence the source never measured (33 entries across 3,306 post-warmup bars here), disclosed without re-tuning. The rule is long-flat, so a spot deployment expresses the full machine with no short permission — a two-sided or perpetual variant would be a different, unpinned claim (this record's gate-5 evidence is the spot path only; the source's equity universe is provenance, not execution). No warmup history beyond 60 `1d` bars is consumed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Gate-free by design: with no confirmation gate in the printed program, any lower-rail touch arms — including the first touch of a prolonged cascade that never snaps back (the planted sustained-down tape rides LONG to the tape end — disclosed, not upgraded).
- Dead-rail residual: the helper computes an upper band the program never registers and no order line ever reads; this record treats it as display-only residue and fences it as non-executable (a reviewer repairs from code facts only).
- Single-venue port residual: backtesting.py close/open arithmetic vs Binance spot execution (prints, fees, open-definition across 24/7 sessions, equity-vs-crypto regime differences) is unclaimed, disclosed.
- Next-open latency idealization: signal cadence on the decision close print while fills land on the next open; any live gap between the two differs by construction — disclosed, research-only (this convention is the source's own stated execution, preserved verbatim).
- Degenerate-collapse residual: in the theoretical `ATR14 = 0` collapse (`Lower == Mid`), entry and exit co-fire and the `if/elif` order resolves entry-first — deterministic by code order, exercised by no tape this cycle, disclosed.
- No-authorship-page residual: the page prints no handle, license, or creation stamp; provenance rests on the QuantifiedTrader URL/slug, printed names, page hash, and fetch date — disclosed.
- Performance evidence is absent: nothing here is calibrated, fitted, or tuned to any backtest (the `14/2.0` defaults are the source's, never re-run here; the page's own grid-search section, where available, is not adopted as a parameter source).
- Author scope: the page ships exploratory research with an explicit not-investment-advice disclaimer, not a vetted trading system — this record is research-only and claims no live suitability.

## Implementation status

`not-implemented`: no dedicated controller, Qlib executable recipe or deployment artifact was created. PASS is a bounded research-expressibility proposal, not a claim of already runnable materialization. A selected strategy may later need the minimal strategy-specific implementation without a second admission flag.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review must independently inspect this exact PR head, remediate only primary-source-verifiable facts, then PASS exact-head merge or NOT_LOSSLESS close. Scout does not approve, merge, close, trade, backtest or deploy.

## Related Wiki records

None asserted.

## Sources

- Primary page + pin: https://quantifiedtrader.com/backtest/strategies/atr-bands/ (`ATR Bands`; page fetched live 2026-11-05, 42,764 bytes, SHA-256 `f535db27e01bd351c7a622046fd0f2b0b726b802ed37e3edff617dc33e639664`; implementation block `class ATRBands(Strategy)` with `n = 14; mult = 2`, `_atr_bands(Close, High, Low, n, mult)` single call (helper body unprinted — name occurs once, at its call site; zero `def` prints), `Mid` + `Lower` registrations (upper computed-but-never-registered), `Close[-1] <= lower[-1] and not position → buy()`, `Close[-1] >= mid[-1] and position → position.close()`; zero short/stop/limit/trailing/time/target/profit order calls in the order path; daily OHLCV frame, no-lookahead statement, next-bar-open execution, unmodeled costs, equity-index universe S&P 500 / NASDAQ / DJI / Russell 2000 +16)
- Lane precedent (different mechanism, unmerged-proof never claimed): `quantifiedtrader-keltner-squeeze-upper-breakout-sma-exit-long-flat-btcusdt-1d-2026-11-05.md`, `quantifiedtrader-raff-channel-midline-level-long-flat-btcusdt-1d-2026-11-04.md` and `quantifiedtrader-projection-oscillator-zero-cross-long-flat-btcusdt-1d-2026-11-04.md` (unprinted-helper textbook-freeze derivation pattern with 60-bar warmup)
- Nearest pool lineages (different mechanisms, unmerged-proof never claimed): `forven-atr-breakout-channel-long-flat-btcusdt-1h-2026-10-18.md` (prev-close-anchored breakout, opposite direction); `fmz-super-scalper-rsi-atr-band-dip-two-sided-btcusdt-5m-2026-10-31.md` (RSI-gated two-sided dip); `freqtrade-bband-rsi-dip-buy-long-flat-btcusdt-1h-2026-10-20.md` (BB + RSI dip); `bollinger-band-breakout-long-midline-exit-btcusdt-1d-2026-10-11.md` (BB breakout, opposite entry polarity)
- Exchange verification: Binance spot `api/v3/exchangeInfo` (`BTCUSDT`, `TRADING`, `tickSize 0.01`, min-qty/step 0.00001/0.00001, min-notional 5.0 via `NOTIONAL`) plus `api/v3/klines` 1d probes (3,366 completed bars 2017-08-17→2026-11-03, 33 post-warmup lower-touch bars → 33 entries / 33 exits ending FLAT, event digest `65e707ee` double-run identical; 150-bar restart prints identical 33/33 — warmup-identity fence), fetched live 2026-11-05
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently merged pinned package/source evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
