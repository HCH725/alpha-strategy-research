---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: QuantifiedTrader QStick body-cross long-flat on BTCUSDT 1d bars
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
  - https://quantifiedtrader.com/backtest/strategies/qstick/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# QuantifiedTrader QStick body-cross long-flat on BTCUSDT 1d bars

## Provenance

**Primary source (fetched live over HTTPS this cycle):** QuantifiedTrader public strategy-library page `https://quantifiedtrader.com/backtest/strategies/qstick/` (`QStick`), fetched 2026-11-05 as a 42,667-byte page (SHA-256 `f95aae9e6c83ad1ef87a1da12342e01dd9120457ae10d8e9ebd3278abce1b1dd`). The page prints no login, paywall, author handle, or creation stamp (adopted `source_as_of` is the fetch date, per the merged QuantifiedTrader Raff-Channel / Projection-Oscillator / Keltner-Squeeze / ATR-Bands / BB-Width-Squeeze / MFI lane precedent). The strategy-implementation code block is printed verbatim on the page (backtesting.py shape):

```text
class QStick(Strategy):
    n = 14
    def init(self):
        q = pd.Series(self.data.Close) - pd.Series(self.data.Open)
        self.qstick = self.I(_sma, q, self.n)
    def next(self):
        if self.qstick[-1] > 0 and self.qstick[-2] <= 0 and not self.position: self.buy()
        elif self.qstick[-1] < 0 and self.position: self.position.close()
```

Code census this cycle over the saved page bytes: 1 `buy()` / 1 `position.close()` / 0 `crossover` calls / 1 indicator registration (`self.I`) / `_sma` exactly once, at its call site, with zero `def _` definitions printed anywhere — the helper body is unprinted, the same gap shape the merged Raff-Channel / Projection-Oscillator / Keltner-Squeeze / ATR-Bands / BB-Width-Squeeze / MFI lane records froze via textbook construction. `def ` occurs exactly twice (`init`, `next`). The `short` token never occurs in page bytes. (`stop` / `take_profit` tokens occur only inside the page's stop-loss/take-profit sensitivity table payload and its "stop-loss / take-profit sensitivity" label — fenced, never an order leg; `trailing` never occurs.) This record cites and normalizes the rule and reproduces no source block beyond the short declarations quoted for gate evidence.

**Facts actually supplied by the source page:** backtested on **daily OHLCV** across major US equity indices and ETFs; entry/exit signals carry **no lookahead bias**; **trades execute at the open of the bar following the signal**; performance metrics are computed per symbol; **transaction costs and slippage are not modeled**. Signal prose: QStick smooths the difference between close and open prices over N periods; positive QStick means closes are consistently above opens (bullish candles); enters long on cross above zero, exits on cross below. No return, Sharpe, win-rate, or trade-count figure from the source is carried into the derived specification. The page's parameter grid-search section, where available, is not adopted as a parameter source.

**Prose-vs-code fence (code governs):** the prose says "exits on cross below" but the program tests the level `qstick[-1] < 0`, not a cross-down edge — any negative bar ends the position, not only a fresh cross-down bar. Along every reachable path the two coincide (a LONG book can only meet its first negative print as a cross from a non-negative state — verified on planted trip tape this cycle, exit t=157 from prior non-negative regime), but the executable rule follows the program level, never the prose edge. The entry leg is a true edge (`qstick[-1] > 0 and qstick[-2] <= 0`) — a bar parked above zero for weeks never re-enters; only the `not self.position` guard plus the edge stop re-entry. Both legs are quoted as printed.

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the source ships equity-universe backtesting.py semantics with no venue/fill/cost leg this record can reuse verbatim. Researcher-declared adaptations are exactly six: (1) market pin **BTCUSDT Binance spot 1d** (long-flat needs no margin-short permission; spot is the minimal realistic venue — the source's equity-index universe is kept separate, never claimed); (2) completed-bar decisions with **next-bar-open market** fills (the source's own stated execution — "trades execute at the open of the bar following the signal" — preserved verbatim); (3) input frozen at `n = 14` with the closed-form textbook construction below (14-bar simple moving average of per-bar `Close − Open` bodies, first finite at index 13 — verified this cycle; `_sma` is the ordinary SMA, disclosed as the researcher freeze for the unprinted helper); (4) adopted **100-bar warmup** with pre-warmup bars flat by record rule (structural minimum is index 13 — first finite SMA14 print — verified this cycle; 100 carries margin); (5) house sizing/costs replacing the source's no-cost model (fixed 0.01 BTC, 0.1%/side taker; spot means no funding leg exists — constructive exclusion, never zero-claimed; fixed size is event-neutral for timing under state-independent signals); (6) missing-bar stretches freeze evaluation at the prior target — book and ledger retained across the freeze, evaluation resumes on the next valid bar with no warmup repetition, never backfilled, never forced flat. The cross-up entry, the sub-zero exit, the long-only stance, and the no-stop/no-target posture are source-pinned or predeclared; no short leg is invented.

**Immutable derivative identity:** `qtqstick:QStick-body-sma14-zeroedge|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001-nofunding|spot1x|nostop-notarget|warmup100|2026-11-05`. Changing any input, body construction, threshold, comparator, direction, timing, market, risk, cost, sizing, or book state creates a different derivative.

**Pre-write dedup (2026-11-05):** working-tree base is current `main@73218ff8` (566 root strategy records, READMEs excluded; this file is the 567th). Content searches for the canonical slug `strategies/qstick`, the class name `class QStick`, and the exact helper token `_sma, q` return zero same-source/same-construction records (the only pool QStick hit is the FMZ-439854 two-sided cousin — edge-vs-hold, direction, frame, fill, and venue all differ, fenced in Negative evidence; generic `_sma` hits are SMA-family records with different inputs, never a `Close − Open` body average). No open `research/*` PR is this page, author, construction, or signal (17 open PRs enumerated this cycle — #48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708, #725 — none is a QStick, body-momentum, or QuantifiedTrader-oscillator machine). No duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

Body-pressure trend capture, long side only. The construction is self-describing: each bar's `Close − Open` body signs whether buyers or sellers won the bar; the 14-bar average asks whether closes have consistently beaten opens (bullish-candle regime) or the reverse. The position rides the below-to-above zero traverse and ends it on the first negative-average print. The equity-index universe and the unmodeled-costs stance are source facts, not this record's venue or economics. No performance figure is carried anywhere.

### Research interpretation

Zero-edge body-momentum machine — the patient cousin of the pool's FMZ QStick record (which holds a side on every bar: long whenever the average body is positive, short whenever negative, always in the market) and the structural sibling of the merged QuantifiedTrader MFI dip-level record (edge-vs-level honesty fence, same lane, same venue/timing/cost freeze). Unlike zero-line oscillators on close-to-close momentum (ROC-sign, CMF-sign) the input here is the open-to-close body, so overnight gaps between bars never enter the average — only intraday body pressure does. Unlike price-vs-average trend filters (SMA50 level, TASC linreg-slope sign) there is no price level and no regression — one spread, one average, one zero line. Unlike the pool's QStick combos (there are none — the FMZ record is the sole cousin) there is no second gate and no signal line. The failure mode is plain and verified this cycle: an exactly flat tape pins the average at exactly 0.0 and the machine never trades (planted dead-flat tape prints 0 entries / 0 exits ending FLAT — disclosed, not patched, the honest opposite of the MFI lane's buy-and-hold degeneration); a sustained ramp crosses during warmup and never re-arms post-warmup (planted sustained-up tape prints 0/0 ending FLAT — disclosed non-participation); a sustained bleed never prints positive and never participates (planted sustained-down tape prints 0/0 ending FLAT — disclosed); the round trip is exercised on the planted drift-dip-rip-dip tape (1 entry / 1 exit ending FLAT — disclosed).

## Signal

Exact rule as pinned (daily decision on completed `1d` bars; entries/exits next-bar-open market; long-flat single-unit book — any other input, body construction, threshold, sizing, fill, or cost is a different, unpinned rule):

- R1 — Measure grid: completed `1d` bars of BTCUSDT spot only. Continuous calendar days; no session template, no holiday skip. Bar time is never read by any order-gating line.
- R2 — Source series: `O[t]`, `C[t]` feed the body construction only (high/low/volume fill nothing and gate nothing). No funding/OI/mark-index read gates on any order; no sentiment/macro/on-chain/cross-venue state. Single timeframe, single asset.
- R3 — QStick stack (frozen, researcher-pinned textbook construction for the unprinted helper): `BODY[t] = C[t] − O[t]`; `QSTICK[t] = mean(BODY[t-13..t])` (ordinary 14-bar SMA of bodies; first finite at index 13 — verified this cycle). Finite exactly when all trailing inputs are finite. Any other body definition, window, averaging, or scaling prints a different, unpinned series.
- R4 — Entry (pinned, cross-up edge): if FLAT and `QSTICK[t] > 0` and `QSTICK[t-1] <= 0` (post-warmup) → buy at the next open. A touch of the line without crossing (`> 0` persisting) fires nothing; exact-zero current (`== 0`) fails the strict leg and fires nothing.
- R5 — Exit (pinned, sub-zero level): if LONG and `QSTICK[t] < 0` → close the whole book at the next open. The exit is a level hold, not a cross — it fires on any negative-average bar. The program ships no NaN guard, but a non-finite print never satisfies any strict comparison, so seeding can never smuggle an entry or an exit; pre-warmup and NaN-signal bars are flat/hold by record rule.
- R6 — Risk legs (file absence, not invented): stop-loss, take-profit, trailing, time exit, and any second exit are all explicitly disabled — the program ships none, and no prose ships any executable one. The page's stop-loss/take-profit sensitivity table is a parameter sweep overlaid on the same rule, never an order leg — fenced, not adopted. The sub-zero print is the sole exit path.
- R7 — Position state (single deterministic path — no reset, no re-warmup): one 0.01-BTC unit max, long or flat. Safety orders: explicitly none. No cooldown: after any close, the next cross-up bar re-enters at its next open (`not self.position` guard preserved — while LONG, qualifying cross bars are no-ops; while FLAT, negative bars are no-ops). Entry and exit can never co-fire (`QSTICK > 0` with prior `<= 0` vs `QSTICK < 0` are jointly unsatisfiable) — no tie-break pin is required. The degenerate all-zero window (`QSTICK == 0.0`) arms neither leg — verified on planted tape this cycle (0/0 ending FLAT), fenced by arithmetic, disclosed, not patched.
- R8 — Warmup: flat until 100 completed `1d` bars (structural minimum is index 13; 100 carries margin — verified this cycle). The 100-bar pin is frozen: any other warmup is a different, unpinned claim.
- R9 — Invariant identifier: `qtqstick:QStick-body-sma14-zeroedge|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001-nofunding|spot1x|nostop-notarget|warmup100|2026-11-05` (any input, construction, threshold, comparator, direction, sizing, fill, risk, or cost change is a different derivative).

## Required data

- Completed `1d` bars of BTCUSDT: `O[t]`/`C[t]` feed the body average (intraday pressure only — gaps between bars never enter). `H[t]`/`L[t]`/`V[t]` gate nothing. Base-asset volume is unread by every order-gating line. No `funding-signal`, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; the window reads trailing completed bars only, never a second feed).
- Warmup: 100 completed `1d` bars flat by record rule — structural minimum is index 13 (binding leg: 14-body SMA seed, verified first-finite at index 13 this cycle). Pre-warmup and any NaN-signal bars are flat/hold by record rule; missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (window reads completed bars including the decision bar only — same-bar comparison, no lag, no negative shift), no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance spot, 1x, fixed 0.01 BTC per unit, single-unit book, no compounding. Long side explicitly enabled; short side explicitly disabled (zero `short` tokens in page bytes; zero short order calls in the printed program). Fills are never conditional on equity or buying power.
- Order timing (source-stated timing preserved verbatim): completed-bar decision with next-bar-open market fills for entries and whole-book closes — the source prose states "trades execute at the open of the bar following the signal", and this record adopts exactly that (the same verified execution primitive as the merged FMZ/QuantifiedTrader lane records; with no stop/limit legs anywhere in the derived machine there is no same-bar TP/SL ordering ambiguity; each bar's outcome is a single deterministic event: hold, open-long, or close-flat, and R7 proves the two legs can never co-fire). This record claims no other fill convention: no same-bar-close print, no maker-touch, no intrabar-path-dependent fill.
- Pinned engine path (verified at the pin this cycle): Hummingbot package label `20260920`, VERSION `dev-2.17.0` (local checkout `2dbc844` carries `hummingbot/VERSION` file `2.17.0`, verified live this cycle; `8b0e067e80ab62f10846d518dcb5a8218527ddb3` is an ancestor of the local checkout, verified via `merge-base --is-ancestor` this cycle; code paths verified at the pin this cycle: `async def run_backtesting` in `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py:221`, `def determine_executor_actions` in `hummingbot/strategy/strategy_v2_base.py:747`, `class OrderExecutorSimulator` in `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py:9`, `INTERVALS "1d" = "1d"` in `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py:24`). Prior merged Alpha PR **#414** reports a 902/902 wheel-file byte match and 33-assert representative validation for this source/package path; this Scout did not independently rehash the wheel. A different deployed package must be revalidated. A strategy-specific, not-yet-implemented controller must compute the trailing body-average pin via `CreateExecutorAction(OrderExecutorConfig)` market legs; the generic executor does not calculate the strategy. The precomputable body-average series plus edge/level state machine is a plain signal series, not a new execution primitive; no new data requirement, no representative-capability validation owed.
- Stop/limit modeling: none — the derived spec carries zero stop/limit/trailing legs by record rule. No hidden Hummingbot stop-order defaults are relied upon, and with no stop/limit legs there is no same-bar TP/SL ordering ambiguity.
- Sizing/capital/costs: the source models no costs (recorded as the source's, never adopted). Explicit house overlay: single-unit frame, 0.1% taker fee per filled side, slippage unmodeled by declaration; fixed size is event-neutral for timing under state-independent signals. Exchange facts re-verified live this cycle via `api/v3/exchangeInfo`: `BTCUSDT`, `TRADING`, `tickSize 0.01`, min-qty/step 0.00001/0.00001, min-notional 5.0 (`NOTIONAL`). The fixed 0.01 BTC (≈801.98 USDT at the cycle's 24hr last price 80,198.01, above the 5.0 min-notional and an exact multiple of the 0.00001 step). Spot venue means no funding leg exists — constructive exclusion, never modeled-or-realized funding.
- Concurrency: at most one single-asset engine position at any time; the sub-zero print ends it (re-entry earliest next signal). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no hedge-mode requirement by construction.

## Evidence

### Source-reported

With exact provenance (page fetched live 2026-11-05, 42,667 bytes, SHA-256 `f95aae9e6c83ad1ef87a1da12342e01dd9120457ae10d8e9ebd3278abce1b1dd`; implementation block `class QStick(Strategy)` with `n = 14`, body line `q = Close − Open` series, `_sma(q, n)` single call (helper body unprinted — the name occurs once, at its call site; zero `def` prints beyond `init`/`next`), single `self.I` registration, `qstick[-1] > 0 and qstick[-2] <= 0 and not position → buy()`, `qstick[-1] < 0 and position → position.close()`): the frozen input; the O/C reads; the cross-up/level-down polarity with strict comparators; the `not self.position` single-unit guard; the long-only order set (zero short/crossover/stop/trailing order calls in the order path; stop/take-profit tokens fenced to the sensitivity table, never the code); the source's daily-OHLCV frame, no-lookahead statement, next-bar-open execution, unmodeled-costs stance, and equity-index universe. This record claims no source-reported performance number as its own — no return, Sharpe, win rate, or trade count is carried into the derived specification — and no reproduced performance exists.

### Independently reproduced

**None.** No strategy backtest, event-level Qlib/Hummingbot parity, wheel rehash, deployment or profitability experiment occurred. Pinned engine source inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifacts this run are researcher self-checks of the predicate/estimator/state pipeline (body-SMA14 + zero edge/level + 100-bar warmup, next-open single-unit long-flat machine), run in scratch (never committed): logic verification only, not a backtest, not parity.

**Planted-tape verification (this cycle, deterministic):** TAPE-flat (dead-constant 170-bar tape, bodies exactly zero) prints 0 entries / 0 exits ending FLAT — the zero window arms neither leg, as pinned (disclosed never-trades degeneration, not patched — the honest opposite of the MFI lane's buy-and-hold); TAPE-up (sustained +1%/day compounding 170-bar tape) prints 0 entries / 0 exits ending FLAT — the cross fires once at index 13 inside warmup and never re-arms post-warmup, as pinned (disclosed non-participation, not patched); TAPE-down (sustained −1%/day 170-bar tape) prints 0 entries / 0 exits ending FLAT — the average never prints positive, as pinned (disclosed, not patched); TAPE-trip (deterministic 260-bar drift/dip/rip/dip tape) prints 1 entry / 1 exit ending FLAT (entry t=105 at QSTICK 0.0714 from prior −0.1071 mid-rip, exit t=157 at QSTICK −0.2143 on the second dip — the full round trip is exercised, as pinned).

**Live-exchange microstructure probes (this cycle, Binance spot 1d klines, 3,366 completed bars 2017-08-17→2026-11-03; the in-progress 2026-11-04 bar excluded after dedup/sort/close-time check):** 192 post-warmup body-cross traverses drive 192 entries / 192 exits ending FLAT (non-degenerate; 1,535 negative-average bars and 1,731 positive-average bars in range, zero exact-zero prints). Two independent runs produce identical digests (event-series digest `c08dda0b`). Admission is engineering capability, never an event-rate or profitability claim.

### Negative evidence

1. FMZ-cousin fence: pool `qstick-zero-cross-trend-two-sided-btcusdt-1h-2026-10-09` (FMZ 439854, SMA of `close − open` length 14, fixed zero line) is a level-HOLDING two-sided always-in-market machine on 1h futures with same-bar-close fills — long whenever positive, short whenever negative, exits only by reversal. This record is an edge-TRIGGERED long-flat machine on 1d spot with next-bar-open fills — one cross-up opens, any negative print flattens, flat is the resting state, short is unreachable. Different entry bars (first post-warmup positive-hold bar vs first post-warmup cross-up edge), different exit bars (reversal-to-short vs flatten), different resting state (always positioned vs flat-capable), different frame/fill/venue — never a twin.
2. Zero-line-oscillator fence: pool `roc-sign-state`, `forven-roc-zero-cross`, `freqtrade-technical-cmf-sign-state` and `cmf-velocity-zero-cross` command on close-to-close momentum that admits overnight gaps; this record averages intraday bodies only, so gaps never enter the print. Different trigger object — never a twin.
3. Trend-filter fence: pool SMA/EMA/Tema slope, price-vs-average, and linreg-slope records (including `tradingview-tasc-linreg40-slope-sign`) test price levels or regression slopes, never a `Close − Open` body average — no shared series anywhere — never a twin.
4. Band-touch fence: pool `bollinger-band-breakout-long-midline-exit` (upper-band penetration entry, midline exit) and the just-merged QuantifiedTrader band records trade price rails, not a body-pressure average — no shared series anywhere — never a twin.
5. Single-print-twin fence: no twin is admitted — any input change (e.g. 14→10 window), any level-hold or two-sided variant, any gated, bracketed, or stop-carrying variant, any other body definition, frame, fill, venue, or book is a different, unpinned rule.
6. NaN/seed fence: any non-finite QSTICK print holds with no signal and no close (language-false comparisons, no guard invented); the body/SMA14 conventions are part of the pin. Interpolating, reseeding, or backfilling is a different, unpinned rule.
7. Warmup-identity fence, admitted plainly: the pin is 100 completed bars (structural minimum index 13); any other warmup remains a different, unpinned claim even where it prints the same book.
8. Number silence fenced: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from any source is adopted anywhere, and any dispute over exact magnitudes is decided against this record, never patched by inference.
9. Version fence: this record follows the QuantifiedTrader page as fetched 2026-11-05 (no printed creation stamp; fetch-date pin). If the page is ever edited, this record does not move with it.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: input `14` / textbook body-SMA14 construction / cross-up edge entry / sub-zero level exit / long-flat book / no-stop-no-target posture / `1d` BTCUSDT spot / next-open fills / 0.01 BTC / 0.1% costs / 100-bar warmup are frozen.

- F1 — Edge-vs-hold: a level-hold twin (enter whenever `QSTICK[t] > 0` while flat — same rest) must not improve net expectancy; fail ⇒ the cross-up edge adds nothing over holding every positive bar, and the record is an edge label on a hold machine.
- F2 — Exit-shape relevance: a cross-down twin (exit only on a fresh `QSTICK[t-1] >= 0` → `QSTICK[t] < 0` cross — same rest) must not improve net expectancy; fail ⇒ the always-armed level exit adds nothing over an edge exit along reachable paths, and the distinction is decorative.
- F3 — Body relevance: replacing the open-close body spread with a close-to-close momentum spread (`sma(change(close), 14)` against zero — same rest) must not improve net expectancy; fail ⇒ the body-pressure construction adds nothing over plain close momentum.
- F4 — Warmup relevance: the pinned 100 print and a 100-vs-100 re-run must print the identical event set (determinism check — digest `c08dda0b` is the tripwire); fail ⇒ nondeterminism or seed leakage past the declared warmup.

## Crypto portability

Pinned to BTCUSDT Binance spot under the house overlay (declared port of an equity-index-headed backtesting.py program). The rule reads completed daily O/C bodies only, so no pit-session, gap, roll, split/dividend-adjustment, or corporate-action logic ports (equity-calendar effects are non-issues on spot — disclosed, not modeled; crypto gaps between bars are excluded from the average by construction — the body reads intraday pressure only, disclosed). No volume read means equity-vs-crypto volume-regime comparability is a non-issue here — disclosed without re-tuning; the rule fires at a cadence the source never measured (192 traverses across 3,266 post-warmup bars here), disclosed. The rule is long-flat, so a spot deployment expresses the full machine with no short permission — a two-sided or perpetual variant would be a different, unpinned claim (this record's gate-5 evidence is the spot path only; the source's equity universe is provenance, not execution). No warmup history beyond 100 `1d` bars is consumed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Never-trades degeneration by construction: an exactly flat tape pins the average at 0.0 and neither leg ever arms (planted dead-flat tape: 0/0 ending FLAT — disclosed, not upgraded).
- Trend non-participation by construction: sustained ramps cross once inside warmup and never re-arm (planted sustained-up tape: 0/0) — the rule sits out every post-warmup ramp waiting for a fresh cross that never comes, disclosed, not patched.
- Bleed non-participation by construction: sustained bleeds never print positive (planted sustained-down tape: 0/0 ending FLAT) — disclosed, not patched.
- Single-venue port residual: backtesting.py O/C arithmetic vs Binance spot execution (prints, fees, open-definition across 24/7 sessions) is unclaimed, disclosed.
- Next-open latency idealization: signal cadence on the decision close print while fills land on the next open; any live gap between the two differs by construction — disclosed, research-only (this convention is the source's own stated execution, preserved verbatim).
- Hold-band residual: the zero line commands nothing while the average sits positive — multi-month holds through chop that never prints negative are the normal case, not an anomaly, disclosed.
- No-authorship-page residual: the page prints no handle, license, or creation stamp; provenance rests on the QuantifiedTrader URL/slug, printed names, page hash, and fetch date — disclosed.
- Performance evidence is absent: nothing here is calibrated, fitted, or tuned to any backtest (the `14` default is the source's, never re-run here; the page's own grid-search section, where available, is not adopted as a parameter source).
- Author scope: the page ships exploratory research with an explicit not-investment-advice disclaimer, not a vetted trading system — this record is research-only and claims no live suitability.

## Implementation status

`not-implemented`: no dedicated controller, Qlib executable recipe or deployment artifact was created. PASS is a bounded research-expressibility proposal, not a claim of already runnable materialization. A selected strategy may later need the minimal strategy-specific implementation without a second admission flag.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review must independently inspect this exact PR head, remediate only primary-source-verifiable facts, then PASS exact-head merge or NOT_LOSSLESS close. Scout does not approve, merge, close, trade, backtest or deploy.

## Related Wiki records

None asserted.

## Sources

- Primary page + pin: https://quantifiedtrader.com/backtest/strategies/qstick/ (`QStick`; page fetched live 2026-11-05, 42,667 bytes, SHA-256 `f95aae9e6c83ad1ef87a1da12342e01dd9120457ae10d8e9ebd3278abce1b1dd`; implementation block `class QStick(Strategy)` with `n = 14`, body line `q = Close − Open` series, `_sma(q, n)` single call (helper body unprinted — the name occurs once, at its call site; zero `def` prints beyond `init`/`next`), single `self.I` registration, `qstick[-1] > 0 and qstick[-2] <= 0 and not position → buy()`, `qstick[-1] < 0 and position → position.close()`; zero short/crossover order calls in the order path (`stop`/`take_profit` tokens occur only inside the stop-loss/take-profit sensitivity table payload and label — fenced, not adopted; `trailing` never occurs); daily OHLCV frame, no-lookahead statement, next-bar-open execution, unmodeled costs, equity-index universe)
- Lane precedent (different mechanism, unmerged-proof never claimed): `quantifiedtrader-money-flow-index-dip-level-long-flat-btcusdt-1d-2026-11-05.md`, `quantifiedtrader-bb-width-squeeze-sma-state-long-flat-btcusdt-1d-2026-11-05.md`, `quantifiedtrader-atr-bands-lower-touch-midline-exit-long-flat-btcusdt-1d-2026-11-05.md`, `quantifiedtrader-keltner-squeeze-upper-breakout-sma-exit-long-flat-btcusdt-1d-2026-11-05.md`, `quantifiedtrader-raff-channel-midline-level-long-flat-btcusdt-1d-2026-11-04.md` and `quantifiedtrader-projection-oscillator-zero-cross-long-flat-btcusdt-1d-2026-11-04.md` (unprinted-helper textbook-freeze derivation pattern)
- Nearest pool lineage (different mechanism, unmerged-proof never claimed): `qstick-zero-cross-trend-two-sided-btcusdt-1h-2026-10-09.md` (FMZ 439854 level-holding two-sided 1h same-close machine — edge-vs-hold, direction, frame, fill, and venue all differ, fenced in Negative evidence)
- Exchange verification: Binance spot `api/v3/exchangeInfo` (`BTCUSDT`, `TRADING`, `tickSize 0.01`, min-qty/step 0.00001/0.00001, min-notional 5.0 via `NOTIONAL`) plus `api/v3/klines` 1d probes (3,366 completed bars 2017-08-17→2026-11-03, in-progress 2026-11-04 bar excluded after dedup/sort/close-time check; 192 post-warmup body-cross traverses → 192 entries / 192 exits ending FLAT, event digest `c08dda0b` double-run identical; planted tapes flat 0/0 FLAT, up 0/0 FLAT, down 0/0 FLAT, drift-dip-rip-dip 1/1 FLAT with entry t=105 / exit t=157 — degeneration/non-participation/round-trip fences), fetched live 2026-11-05
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently merged pinned package/source evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
