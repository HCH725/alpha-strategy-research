---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: QuantifiedTrader Raff Channel midline-level long-flat on BTCUSDT 1d bars
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
  - https://quantifiedtrader.com/backtest/strategies/raff-channel
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# QuantifiedTrader Raff Channel midline-level long-flat on BTCUSDT 1d bars

## Provenance

**Primary source (fetched live over HTTPS this cycle):** QuantifiedTrader public strategy-library page `https://quantifiedtrader.com/backtest/strategies/raff-channel` (`Raff Channel`), fetched 2026-11-04 as a 42,839-byte page (SHA-256 `741789e177a0fb736a9a980ac8d5246abf30d36a8d0c7679fbddc92b59cc2eaf`). The page prints no login, paywall, author handle, or creation stamp (adopted `source_as_of` is the fetch date, per the merged QuantifiedTrader Disparity-Index lane precedent). The strategy-implementation code block is printed verbatim on the page (backtesting.py shape):

```text
class RaffChannel(Strategy):
    n = 20
    def init(self):
        mid, high, low = _raff_channel(self.data.Close, self.n)
        self.mid = self.I(lambda: mid, name="Mid")
    def next(self):
        if self.data.Close[-1] > self.mid[-1] and not self.position:
            self.buy()
        elif self.data.Close[-1] < self.mid[-1] and self.position:
            self.position.close()
```

Code census this cycle: 1 `buy()` / 1 `position.close()` / 0 short/sell-short calls / 0 stop/limit/trailing/time calls / 1 indicator call (`_raff_channel`, Close-only) / 0 volume / 0 High-Low reads by any order-gating line. The `high, low` unpack targets are never read by any order line (dead code, fenced below). This record cites and normalizes the rule and reproduces no source block beyond the short declarations quoted for gate evidence.

**Facts actually supplied by the source page:** backtested on **daily OHLCV** across major US equity indices and ETFs (S&P 500, NASDAQ Composite, DJI, Russell 2000, +16 more); entry/exit signals carry **no lookahead bias**; **trades execute at the open of the bar following the signal**; performance metrics are computed per symbol; **transaction costs and slippage are not modeled**. Signal prose: the channel draws a linear regression channel around price; long while price is above the midline (upward bias); exit when price falls back below the midline. No return, Sharpe, win-rate, or trade-count figure from the source is carried into the derived specification.

**Unpinned-helper gap (disclosed, not repaired):** the page calls a shared site helper `_raff_channel(close, n)` whose body is printed nowhere on the page (the name occurs exactly once in the whole fetch, at the call site — verified this cycle). This derivative therefore does **not** claim byte-equivalence with the site's helper. It freezes the textbook Raff midline — the ordinary-least-squares regression-line endpoint over the trailing `n` closes — as an explicit researcher choice, fully specified below. This choice carries no seeding ambiguity: closed-form OLS over completed closes is arithmetically exact from the first full window, so no framework-equivalence question arises beyond the disclosed formula (the same treatment the merged Disparity-Index lane record gave its unprinted `_disparity` helper). The `high`/`low` band legs are never order-reading, so no band-construction choice is pinned or needed.

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the source ships equity-universe backtesting.py semantics with no venue/fill/cost leg this record can reuse verbatim. Researcher-declared adaptations are exactly six: (1) market pin **BTCUSDT Binance spot 1d** (long-flat needs no margin-short permission; spot is the minimal realistic venue — the source's equity-index universe is kept separate, never claimed); (2) completed-bar decisions with **next-bar-open market** fills (the source's own stated execution — "trades execute at the open of the bar following the signal" — preserved verbatim); (3) input frozen at `n = 20` with the closed-form OLS-endpoint midline (any other window or midline construction is a different, unpinned rule); (4) adopted **60-bar warmup** with pre-warmup bars flat by record rule (structural minimum is index 19 — first 20-close window — verified this cycle; 60 follows the merged QuantifiedTrader 1d sibling package with conservative margin); (5) house sizing/costs replacing the source's no-cost model (fixed 0.01 BTC, 0.1%/side taker; spot means no funding leg exists — constructive exclusion, never zero-claimed; fixed size is event-neutral for timing under state-independent signals); (6) missing-bar stretches freeze evaluation at the prior target — book and ledger retained across the freeze, evaluation resumes on the next valid bar with no warmup repetition, never backfilled, never forced flat. The midline-level entry/exit polarity, the strict comparators, the long-only stance, and the no-stop/no-target posture are source-pinned or predeclared; no short leg is invented.

**Immutable derivative identity:** `qtraff:RaffChannel-olsmid-20_level-hold|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001-nofunding|spot1x|nostop-notarget|warmup60|2026-11-04`. Changing any input, midline construction, comparator, direction, timing, market, risk, cost, sizing, or book state creates a different derivative.

**Pre-write dedup (2026-11-04):** working-tree base is current `main@2856b12c` (560 root strategy records, READMEs excluded; this file is the 561st). Content searches for `raff`, `RaffChannel`, `quantifiedtrader.com/backtest/strategies/raff`, and `_raff_channel` return zero strategy records (the single `raff` substring hit pool-wide is the English word "traffic" in an unrelated Donchian record). The pool's nearest linreg-channel records are all fenced as different signal objects (Negative evidence 1–4). No open `research/*` PR is this page, author, construction, or signal (17 open PRs enumerated this cycle — #48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708, #725 — titles contain no Raff hit; the QuantifiedTrader sitemap's six already-mined siblings are disparity-index, fractal-breakout, intraday-intensity, random-walk-index, twiggs-money-flow, volume-price-trend). No duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

Level-hold trend participation against a regression midline, long side only. The construction is self-describing: a 20-bar linear-regression channel is drawn around price; any bar printing above the channel midline holds the long thesis (upward bias); the first print back below the midline ends it. The page prose claims only this trend-following intuition — this record adopts none of it beyond the coded comparisons. The equity-index universe and the unmodeled-costs stance are source facts, not this record's venue or economics. No performance figure is carried anywhere.

### Research interpretation

Regression-midline level-hold, long-flat — a *level* object, not an edge object. Unlike the pool's band-breakout cousins (which wait for a close to pierce a ±2σ rail — rare, explosive events), this rule holds the long on *every* bar above the midline and enters from flat on the first such bar: participation is the default state above the line, not a breakout reward. Unlike the pool's slope-sign cousins (which trade the *tilt* of the regression line and can stay long while price sits far below a rising line), this rule never reads the slope — a flat or falling line still holds the long while price prints above it, and a steeply rising line still exits the moment price dips under it. Unlike SMA-level cousins, the OLS endpoint weights recent closes more heavily than old ones, so the line hugs fresh price action tighter than a simple average of the same window. The failure mode is plain: in a grinding decline the midline sinks with price and the level can stay armed (or hold) through a continuing slide with no guardrail — disclosed, not upgraded (the planted sustained-down tape exercises exactly this path).

## Signal

Exact rule as pinned (daily decision on completed `1d` bars; entries/exits next-bar-open market; long-flat single-unit book — any other input, midline construction, comparator, sizing, fill, or cost is a different, unpinned rule):

- R1 — Measure grid: completed `1d` bars of BTCUSDT spot only. Continuous calendar days; no session template, no holiday skip. Bar time is never read by any order-gating line.
- R2 — Source series: `C[t]` is the sole signal input (`O[t]` never read by any order-gating line — fills price at opens; notionals reference closes for cost sizing only). No `H[t]`, no `L[t]`, no volume, no funding/OI/mark-index read gates on any order; no sentiment/macro/on-chain/cross-venue state. Single timeframe, single asset.
- R3 — Midline (frozen, researcher-pinned textbook construction): over trailing closes `C[t-19..t]`, `MID[t]` is the ordinary-least-squares regression-line value at the endpoint (closed form: slope `b = Σxc·(w−w̄)/Σxc²` on centered `x = 0..19`, `MID[t] = w̄ + b·(19 − x̄)`). Finite exactly when all 20 trailing closes are finite (first possible at index 19 — verified this cycle). Non-positive/non-finite prints force NaN → hold (no signal, no close).
- R4 — Entry (pinned, level not edge): if FLAT and `C[t] > MID[t]` (post-warmup) → buy at the next open. Any above-midline bar while flat enters — no breakout, no cross-up edge, no band touch is required.
- R5 — Exit (pinned, level): if LONG and `C[t] < MID[t]` → close the whole book at the next open. Exact equality (`C == MID`) neither enters nor exits, by the strict comparators as coded.
- R6 — Risk legs (file absence, not invented): stop-loss, take-profit, trailing, and any second exit are all explicitly disabled — the program ships none, and no prose ships any. The below-midline cross is the sole exit path.
- R7 — Position state (single deterministic path — no reset, no re-warmup): one 0.01-BTC unit max, long or flat. Safety orders: explicitly none. No cooldown: after any close, the next above-midline bar re-enters at its next open (`not self.position` guard preserved — while LONG, above-midline bars are no-ops; while FLAT, below-midline bars are no-ops). Entries and exits can never co-fire on the same bar (strict `>` vs strict `<` on the same two prints — disjoint by arithmetic, including the degenerate constant tape). Fills are unconditional.
- R8 — Warmup: flat until 60 completed `1d` bars (structural minimum is index 19; 60 follows the merged QuantifiedTrader 1d sibling package with margin — verified this cycle). The 60-bar pin is frozen: a longer warmup prints the same signal series but a different forced-flat-restart book (this cycle's 150-bar restart prints 286/286 vs the pinned 297/297), so it is a different, unpinned claim.
- R9 — Invariant identifier: `qtraff:RaffChannel-olsmid-20_level-hold|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001-nofunding|spot1x|nostop-notarget|warmup60|2026-11-04` (any input, construction, comparator, direction, sizing, fill, risk, or cost change is a different derivative).

## Required data

- Completed `1d` closes of BTCUSDT: `C[t]` is the sole series the formula reads (`O[t]` fills only; notionals reference closes for cost sizing only). No `H[t]`, no `L[t]`, no `volume`, no funding-signal, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; the single window reads trailing completed closes only, never a second feed).
- Warmup: 60 completed `1d` bars flat by record rule — structural minimum is the 20th completed bar (binding leg: 20-close OLS window, verified finite at index 19 this cycle; first decidable comparison at index 19). Pre-warmup and any NaN-signal bars are flat/hold by record rule; missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (the window reads completed bars including the decision bar only), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance spot, 1x, fixed 0.01 BTC per unit, single-unit book, no compounding. Long side explicitly enabled; short side explicitly disabled (zero short tokens anywhere in the printed program). Fills are never conditional on equity or buying power.
- Order timing (source-stated timing preserved verbatim): completed-bar decision with next-bar-open market fills for entries and whole-book closes — the source prose states "trades execute at the open of the bar following the signal", and this record adopts exactly that (the same verified execution primitive as the merged FMZ/QuantifiedTrader lane records; with no stop/limit legs anywhere in the derived machine there is no same-bar TP/SL ordering ambiguity; each bar's outcome is a single deterministic event: hold, open-long, or close-flat). This record claims no other fill convention: no same-bar-close print, no maker-touch, no intrabar-path-dependent fill.
- Pinned engine path (verified at the pin this cycle): Hummingbot package label `20260920`, VERSION `dev-2.17.0` (local checkout `2dbc844fadb9d863b3ab0af1b8ab100472102e42` carries `hummingbot/VERSION` file `2.17.0`, verified live this cycle; `8b0e067e80ab62f10846d518dcb5a8218527ddb3` is an ancestor of the local checkout, verified via `merge-base --is-ancestor` this cycle; code paths verified at the pin this cycle: `async def run_backtesting` in `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py:221`, `def determine_executor_actions` in `hummingbot/strategy/strategy_v2_base.py:747`, `class OrderExecutorSimulator` in `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py:9`, `INTERVALS "1d" = "1d"` in `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py:24`). Prior merged Alpha PR **#414** reports a 902/902 wheel-file byte match and 33-assert representative validation for this source/package path; this Scout did not independently rehash the wheel. A different deployed package must be revalidated. A strategy-specific, not-yet-implemented controller must compute the trailing OLS-midline level state pin via `CreateExecutorAction(OrderExecutorConfig)` market legs; the generic executor does not calculate the strategy. The precomputable midline series plus level-state machine is a plain signal series, not a new execution primitive; no new data requirement, no representative-capability validation owed.
- Stop/limit modeling: none — the derived spec carries zero stop/limit/trailing legs by record rule. No hidden Hummingbot stop-order defaults are relied upon, and with no stop/limit legs there is no same-bar TP/SL ordering ambiguity.
- Sizing/capital/costs: the source models no costs (recorded as the source's, never adopted). Explicit house overlay: single-unit frame, 0.1% taker fee per filled side, slippage unmodeled by declaration; fixed size is event-neutral for timing under state-independent signals. Exchange facts re-verified live this cycle via `api/v3/exchangeInfo`: `BTCUSDT`, `TRADING`, `tickSize 0.01`, min-qty/step 0.00001/0.00001, min-notional 5.0 (`NOTIONAL`). The fixed 0.01 BTC (≈774.54 USDT at the cycle's last completed close 77,453.86 on 2026-11-03, above the 5.0 min-notional and an exact multiple of the 0.00001 step). Spot venue means no funding leg exists — constructive exclusion, never modeled-or-realized funding.
- Concurrency: at most one single-asset engine position at any time; the below-midline print ends it (re-entry earliest next signal). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no hedge-mode requirement by construction.

## Evidence

### Source-reported

With exact provenance (page fetched live 2026-11-04, 42,839 bytes, SHA-256 `741789e177a0fb736a9a980ac8d5246abf30d36a8d0c7679fbddc92b59cc2eaf`; implementation block `class RaffChannel(Strategy)` with `n = 20`, `_raff_channel(self.data.Close, self.n)` mid/high/low unpack, `self.I(lambda: mid, name="Mid")`, `Close[-1] > mid[-1] and not position → buy()`, `Close[-1] < mid[-1] and position → position.close()`): the frozen input (`n 20`); the Close-only indicator read; the strict-comparator level entry/exit polarity; the `not self.position` single-unit guard; the long-only order set (zero short/stop/limit/time calls); the source's daily-OHLCV frame, no-lookahead statement, next-bar-open execution, unmodeled-costs stance, and equity-index universe (S&P 500, NASDAQ Composite, DJI, Russell 2000, +16 more). This record claims no source-reported performance number as its own — no return, Sharpe, win rate, or trade count is carried into the derived specification — and no reproduced performance exists.

### Independently reproduced

**None.** No strategy backtest, event-level Qlib/Hummingbot parity, wheel rehash, deployment or profitability experiment occurred. Pinned engine source inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifacts this run are researcher self-checks of the predicate/estimator/state pipeline (closed-form OLS-20 midline, 60-bar warmup, midline-level next-open single-unit long-flat machine), run in scratch (never committed): logic verification only, not a backtest, not parity.

**Planted-tape verification (this cycle, deterministic, double-run identical):** TAPE-flat (dead-constant 170-bar tape) prints 0 entries / 0 exits ending FLAT (digest `0f48a9b4`) — strict inequalities never arm on `C == MID`, so the constant tape is a clean no-op by exact arithmetic, as pinned; TAPE-up (sustained +1%/day 170-bar tape) prints 1 entry / 0 exits ending LONG (digest `61f7b456`) — the level arms once and the hold path is exercised, as pinned; TAPE-down (sustained −1%/day 170-bar tape) prints 1 entry / 0 exits ending LONG — the sinking midline keeps the level armed through the grind and the hold-through path is exercised, as pinned (disclosed limitation, not patched); TAPE-volregime (deterministic 170-bar ±0.2%-then-±2% alternation tape) prints 75 entries / 75 exits ending FLAT (digest `f0832c12`) — both transition paths are exercised, as pinned.

**Live-exchange microstructure probes (this cycle, Binance spot 1d klines, 3,366 completed bars 2017-08-17→2026-11-03, last close 77,453.86; the in-progress 2026-11-04 bar excluded):** 297 BUY-signal / 297 SELL-signal post-warmup bars drive 297 entries / 297 exits ending FLAT (longest completed hold 24 bars — non-degenerate, non-buy-and-hold). Two independent runs produce identical digests (signal-series digest `88cdf3ea`). Admission is engineering capability, never an event-rate or profitability claim.

### Negative evidence

1. Band-breakout fence, quantified plainly: pool `forven-linreg-channel-breakout` (period 50, 1h) enters only on a close piercing the +2σ rail from below — 37 such entries on this cycle's live window vs this record's 297 midline-level entries (same window, both rules recomputed in scratch this cycle). Different entry object (rail-edge vs midline-level), different window (50 vs 20), different frame (1h vs 1d) — never a parameter twin.
2. Band-touch fence: pool `linreg-channel-band-touch` (100/2.0/EMA50, two-sided) trades rail touches under EMA trend gates; this record has no band, no touch, no EMA gate, and no short leg — opposite construction, never a twin.
3. Slope-sign fence: pool `tradingview-tasc-linreg40-slope-sign` trades the *tilt* of the regression line; this record never reads the slope — a rising line with price beneath it exits here and holds there. Different signal object, never a twin.
4. Envelope fence: pool `fmz-442090-major-trend-indicator-long` (nested linreg envelope triple conjunction, state-following, no clock) holds while three conditions persist; this record holds on a single midline level with no conjunction — different mechanism, never a twin.
5. Midline-equality fence: exact `C == MID` prints neither enter nor exit by the strict comparators as coded (the planted TAPE-flat exercises this path with 0/0). A record adding an equality arm prints a different, unpinned event set; a reviewer must not swap it in.
6. NaN fence: any non-finite window print holds with no signal and no close. Interpolating, seeding, or backfilling is a different, unpinned rule.
7. Derivation-boundary fence: the unmodeled-costs stance and equity-index universe are the source's, never adopted — the next-open fixed-size spot machine with the frozen OLS-endpoint midline is the predeclared derivation, never a source claim; this record is therefore never evidence that the site endorses any executable posture. A reviewer must not substitute a same-bar-close, stop-carrying, futures-margined, or two-sided variant into this record.
8. Helper-construction fence: the record pins the closed-form OLS-endpoint midline. Any other midline (SMA, EMA, WMA, median, or a band-derived proxy) prints a different, unpinned event set; the `high`/`low` band legs are dead code here and a reviewer must not promote them into the signal to reshape the record.
9. Single-print-twin fence: no twin is admitted — any input change (e.g. 20→50 window), any dropped comparator strictness, any band/slope/EMA-gated variant, any other frame, fill, venue, or book is a different, unpinned rule.
10. Warmup-identity fence, admitted plainly: the 150-bar forced-flat restart prints 286/286 events vs 297/297 at the pinned 60 — the same signal series but a different book. Warmup 60 is frozen, not exemplary; any other warmup is a different, unpinned claim.
11. Number silence fenced: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from any source is adopted anywhere, and any dispute over exact magnitudes is decided against this record, never patched by inference.
12. Version fence: this record follows the QuantifiedTrader page as fetched 2026-11-04 (no printed creation stamp; fetch-date pin). If the page is ever edited, this record does not move with it.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: input `20` / OLS-endpoint midline / strict level comparators / long-flat book / no-stop-no-target posture / `1d` BTCUSDT spot / next-open fills / 0.01 BTC / 0.1% costs / 60-bar warmup are frozen.

- F1 — Midline relevance: an SMA20-level twin (enter/hold while `C > SMA(C,20)` — same rest) must not improve net expectancy; fail ⇒ the OLS endpoint adds nothing over a simple average, and the record is a moving-average label rather than a regression-midline edge.
- F2 — Level-vs-edge relevance: a band-breakout twin (enter only piercing `MID + 2σ(residuals)`, exit below `MID` — same rest) must not improve net expectancy; fail ⇒ the permissive level adds nothing over waiting for rail breaks, and the record is a breakout label with extra churn.
- F3 — Exit relevance: an edge-exit twin (exit only on the cross-down edge after at least one full bar above — same rest) must not improve net expectancy; fail ⇒ the level exit adds nothing over the edge, and the record's exit is decorative.
- F4 — Warmup relevance: the pinned 60 print and a 60-vs-60 re-run must print the identical event set (determinism check — digest `88cdf3ea` is the tripwire); fail ⇒ nondeterminism or seed leakage past the declared warmup.

## Crypto portability

Pinned to BTCUSDT Binance spot under the house overlay (declared port of an equity-index-headed backtesting.py program). The rule reads completed daily closes only, so no pit-session, gap, roll, split/dividend-adjustment, or corporate-action logic ports (equity-calendar effects are non-issues on spot — disclosed, not modeled). The composite is unit-free in price-ratio terms (no absolute-price threshold anywhere), so unlike price-level systems the rule ports across venues without re-scaling — yet midline trend-following on crypto microstructure (24/7 bars, stablecoin-quoted prints, volatility-regime shifts the source never traded) fires at a cadence the source never measured (297 round-trips across 3,306 post-warmup bars here, longest hold 24 bars), disclosed without re-tuning. The rule is long-flat, so a spot deployment expresses the full machine with no short permission — a two-sided or perpetual variant would be a different, unpinned claim (this record's gate-5 evidence is the spot path only; the source's equity universe is provenance, not execution). No warmup history beyond 60 `1d` bars is consumed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Hold-through by design: the live window prints 297 entries across 3,306 post-warmup bars with only the below-midline print as exit — a grinding decline that drags the midline down with it holds (or re-arms) with no guardrail, by the prescribed design (the planted sustained-down tape holds LONG to the tape end).
- Single-venue port residual: backtesting.py close/open arithmetic vs Binance spot execution (prints, fees, open-definition across 24/7 sessions, equity-vs-crypto regime differences) is unclaimed, disclosed.
- Next-open latency idealization: signal cadence on the decision close print while fills land on the next open; any live gap between the two differs by construction — disclosed, research-only (this convention is the source's own stated execution, preserved verbatim).
- No-authorship-page residual: the page prints no handle, license, or creation stamp; provenance rests on the QuantifiedTrader URL/slug, printed names, page hash, and fetch date — disclosed.
- Performance evidence is absent: nothing here is calibrated, fitted, or tuned to any backtest (the `n = 20` default is the source's, never re-run here; the page's own grid-search section, where available, is not adopted as a parameter source).
- Author scope: the page ships exploratory research with an explicit not-investment-advice disclaimer, not a vetted trading system — this record is research-only and claims no live suitability.

## Implementation status

`not-implemented`: no dedicated controller, Qlib executable recipe or deployment artifact was created. PASS is a bounded research-expressibility proposal, not a claim of already runnable materialization. A selected strategy may later need the minimal strategy-specific implementation without a second admission flag.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review must independently inspect this exact PR head, remediate only primary-source-verifiable facts, then PASS exact-head merge or NOT_LOSSLESS close. Scout does not approve, merge, close, trade, backtest or deploy.

## Related Wiki records

None asserted.

## Sources

- Primary page + pin: https://quantifiedtrader.com/backtest/strategies/raff-channel (`Raff Channel`; page fetched live 2026-11-04, 42,839 bytes, SHA-256 `741789e177a0fb736a9a980ac8d5246abf30d36a8d0c7679fbddc92b59cc2eaf`; implementation block `class RaffChannel(Strategy)` with `n = 20`, `_raff_channel(self.data.Close, self.n)` mid/high/low unpack (helper body unprinted — name occurs once, at the call site), `self.I(lambda: mid, name="Mid")`, `Close[-1] > mid[-1] and not position → buy()`, `Close[-1] < mid[-1] and position → position.close()`; zero short/stop/limit/trailing/time calls; daily OHLCV frame, no-lookahead statement, next-bar-open execution, unmodeled costs, equity-index universe S&P 500 / NASDAQ / DJI / Russell 2000 +16)
- Lane precedent (different mechanism, unmerged-proof never claimed): `quantifiedtrader-disparity-index-14-zero-cross-long-flat-btcusdt-1d-2026-10-26.md` (unprinted-helper textbook-freeze derivation pattern with 60-bar warmup)
- Nearest pool lineages (different mechanisms, unmerged-proof never claimed): `forven-linreg-channel-breakout-*` (period-50 +2σ rail-edge entry); `linreg-channel-band-touch-*` (100/2.0/EMA50 two-sided rail-touch); `tradingview-tasc-linreg40-slope-sign-*` (regression tilt object); `fmz-442090-major-trend-indicator-long-*` (nested linreg envelope conjunction)
- Exchange verification: Binance spot `api/v3/exchangeInfo` (`BTCUSDT`, `TRADING`, `tickSize 0.01`, min-qty/step 0.00001/0.00001, min-notional 5.0 via `NOTIONAL`) plus `api/v3/klines` 1d probes (3,366 completed bars 2017-08-17→2026-11-03, 297 BUY-signal / 297 SELL-signal post-warmup → 297 entries / 297 exits ending FLAT, longest completed hold 24 bars, signal digest `88cdf3ea` double-run identical; 150-bar restart prints 286/286 — warmup-identity fence), fetched live 2026-11-04
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently merged pinned package/source evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
