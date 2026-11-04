---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: QuantifiedTrader ROC Crossover dual-momentum long-flat on BTCUSDT 1d bars
created: 2026-11-05
updated: 2026-11-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-21
sources:
  - https://quantifiedtrader.com/backtest/strategies/roc-crossover/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# QuantifiedTrader ROC Crossover dual-momentum long-flat on BTCUSDT 1d bars

## Provenance

**Primary source (fetched live over HTTPS this cycle):** QuantifiedTrader public strategy-library page `https://quantifiedtrader.com/backtest/strategies/roc-crossover/` (`ROC Crossover`), fetched 2026-11-05 as a 42,885-byte page (SHA-256 `277a33205dbf9d53da566ec991633248991df8fcc2d9c9bb8cf32ab6aff499f1`). The page prints no login, paywall, or author handle; its meta description prints the data stamp `Data as of 2026-10-21` (adopted as `source_as_of`; the fetch date is the verification date, per the merged QuantifiedTrader Raff-Channel / Projection-Oscillator / Keltner-Squeeze / ATR-Bands / BB-Width-Squeeze / MFI / QStick / Elder-Ray lane precedent). The strategy-implementation code block is printed verbatim on the page (backtesting.py shape):

```text
class ROCCrossover(Strategy):
    n_fast = 5
    n_slow = 20
    def init(self):
        self.roc_fast = self.I(_roc, self.data.Close, self.n_fast)
        self.roc_slow = self.I(_roc, self.data.Close, self.n_slow)
    def next(self):
        if crossover(self.roc_fast, self.roc_slow) and not self.position:
            self.buy()
        elif crossover(self.roc_slow, self.roc_fast) and self.position:
            self.position.close()
```

Code census this cycle over the saved page bytes: 1 `buy()` / 1 `position.close()` / 2 `crossover` calls inside the implementation block (17 page-wide, the other 15 all inside the `<meta name="keywords">` payload — fenced, never an order leg) / 2 indicator registrations (`self.I`) / `_roc` exactly twice, both at the call sites, with zero `def _roc` definitions printed anywhere — the helper body is unprinted, the same gap shape the merged Raff-Channel / Projection-Oscillator / Keltner-Squeeze / ATR-Bands / BB-Width-Squeeze / MFI / QStick / Elder-Ray lane records froze via textbook construction. `def ` occurs exactly twice (`init`, `next`). The order path carries zero `.sell` / zero `short(` / zero `sell(` / zero `StopLoss` / zero `TakeProfit` / zero `trailing` tokens (the page-wide `short` token occurs exactly once, inside the prose adjective "short-term momentum" — fenced, never an order; page-wide `stop` × 19 / `take_profit` × 16 occur only inside the meta "stop-loss / take-profit sensitivity" label and the stop-loss/take-profit sensitivity table payload — fenced, never an order leg; `trailing` never occurs). This record cites and normalizes the rule and reproduces no source block beyond the short declarations quoted for gate evidence.

**Facts actually supplied by the source page:** backtested on **daily OHLCV** across major US equity indices and ETFs; entry/exit signals carry **no lookahead bias**; **trades execute at the open of the bar following the signal**; performance metrics are computed per symbol; the parameter grid-search section, where available, is not adopted as a parameter source; **transaction costs and slippage are not modeled**. Signal prose: "Compares a fast and slow Rate of Change. Enters long when the fast ROC crosses above the slow ROC (short-term momentum accelerating relative to longer-term), exits on the reverse crossover." The meta description prints average Sharpe −0.09, return −2.5%, max drawdown 23.2% with best symbol DJI Sharpe 0.49 — no return, Sharpe, win-rate, drawdown, or trade-count figure from the source is carried into the derived specification anywhere.

**Prose-vs-code fence (code governs, prose agrees):** both legs are `crossover` edges (strict cross-up), not level holds — the prose "crosses above" / "reverse crossover" matches the program exactly, so no prose/code divergence exists to fence beyond recording the agreement. The entry edge fires only on the first bar the fast print moves strictly above the slow print; the exit edge fires only on the first bar the slow print moves strictly above the fast print. Both legs are quoted as printed.

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the source ships equity-universe backtesting.py semantics with no venue/fill/cost leg this record can reuse verbatim. Researcher-declared adaptations are exactly six: (1) market pin **BTCUSDT Binance spot 1d** (long-flat needs no margin-short permission; spot is the minimal realistic venue — the source's equity-index universe is kept separate, never claimed); (2) completed-bar decisions with **next-bar-open market** fills (the source's own stated execution — "trades execute at the open of the bar following the signal" — preserved verbatim); (3) inputs frozen at `n_fast = 5` / `n_slow = 20` with the closed-form textbook construction below (100 × (C[t] − C[t−n]) / C[t−n], pure shift ratio with no smoothing recursion and no seed — disclosed as the researcher freeze for the unprinted helper); (4) adopted **100-bar warmup** with pre-warmup bars flat by record rule (structural minimum is index 21 — the slow leg reads C[t−20] and the crossover reads the prior bar — verified this cycle; 100 carries margin); (5) house sizing/costs replacing the source's no-cost model (fixed 0.01 BTC, 0.1%/side taker; spot means no funding leg exists — constructive exclusion, never zero-claimed; fixed size is event-neutral for timing under state-independent signals); (6) missing-bar stretches freeze evaluation at the prior target — book and ledger retained across the freeze, evaluation resumes on the next valid bar with no warmup repetition, never backfilled, never forced flat. The dual-ROC cross-up entry, the reverse-cross exit, the long-only stance, and the no-stop/no-target posture are source-pinned or predeclared; no short leg is invented.

**Immutable derivative identity:** `qtroccross:ROCCrossover-dualroc5-20|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001-nofunding|spot1x|nostop-notarget|warmup100|2026-11-05`. Changing any input, ROC construction, threshold, comparator, direction, timing, market, risk, cost, sizing, or book state creates a different derivative.

**Pre-write dedup (2026-11-05):** working-tree base is current `main@f84ab309` (568 root strategy records, READMEs excluded; this file is the 569th). Content searches for the canonical slug `strategies/roc-crossover`, the class name `class ROCCrossover`, and the exact construction tokens `roc_fast` / `roc_slow` return zero same-source/same-construction records (the pool's ROC relatives are all fenced in Negative evidence: the Forven ROC12 zero-cross edge, the Pine ROC30 sign-state hold, the Coppock WMA-smoothed dual-ROC composite, the KST four-horizon composite, and the PPO/MACD dual-line cousins — different legs, triggers, and exits; generic `roc`/`momentum`/`crossover` hits are MA-cross or unrelated records, never a raw ROC5-vs-ROC20 cross machine). No open `research/*` PR is this page, author, construction, or signal (17 open PRs enumerated this cycle — #48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708, #725 — none is a ROC, dual-ROC, or QuantifiedTrader-momentum machine). No duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

Dual-horizon return-ratio race, long side only. The fast ROC (5-bar return) measures short-term momentum; the slow ROC (20-bar return) measures longer-term momentum. The position opens when short-term momentum accelerates through longer-term momentum from below (fast crosses above slow) and ends it on the reverse cross (slow crosses above fast). The equity-index universe and the unmodeled-costs stance are source facts, not this record's venue or economics. No performance figure is carried anywhere.

### Research interpretation

Acceleration-cross machine — the impatient cousin of the pool's single-ROC records (which read one return ratio against the fixed zero line) and the unsmoothed sibling of the pool's MACD/PPO dual-line records (which race two exponential averages, not two return ratios). Unlike zero-line oscillators the trigger never reads a fixed level — both rails move every bar, so entries fire on relative acceleration, not on absolute momentum sign. Unlike price-vs-average trend filters (SMA/EMA cross, price-above-SMA) the trigger object is a pair of return ratios, so a smooth geometric ramp never fires: on a constant +1%/day tape the 20-bar return (≈22%) permanently exceeds the 5-bar return (≈5.1%), pinning fast below slow forever (planted sustained-up tape prints 0 entries / 0 exits ending FLAT — disclosed non-participation by construction, not patched; the sustained-down tape prints the same 0/0 FLAT — disclosed). Unlike level-state holds (ROC-sign, AD-line-trend) both legs are one-bar cross edges — consecutive fast-above-slow bars enter exactly once on the crossing bar and hold silently after. The failure mode is plain: chop that whips the two ratios around each other prints repeated cross/cross-back round trips with no stop and no profit-taking leg (the planted dip-recover-parabolic trip exercises exactly one such round trip: 1 entry / 1 exit ending FLAT, first entry t=105, first exit t=140 — disclosed); an exactly flat tape pins both ratios at exact zero forever, so neither edge ever arms (planted dead-flat tape: 0/0 ending FLAT — disclosed, not patched).

## Signal

Exact rule as pinned (daily decision on completed `1d` bars; entries/exits next-bar-open market; long-flat single-unit book — any other input, ROC construction, threshold, sizing, fill, or cost is a different, unpinned rule):

- R1 — Measure grid: completed `1d` bars of BTCUSDT spot only. Continuous calendar days; no session template, no holiday skip. Bar time is never read by any order-gating line.
- R2 — Source series: `O[t]`/`H[t]`/`L[t]` unread; `C[t]` feeds both ROC rails only (volume fills nothing and gates nothing). No funding/OI/mark-index read gates on any order; no sentiment/macro/on-chain/cross-venue state. Single timeframe, single asset.
- R3 — Dual-ROC stack (frozen, researcher-pinned textbook construction for the unprinted helper): `ROCn[t] = 100 × (C[t] − C[t−n]) / C[t−n]` for `n ∈ {5, 20}`, defined whenever `t ≥ n` with strictly positive prices (division by zero is arithmetically impossible on BTC spot closes and is fenced without inventing a guard branch — a zero print would be a different, unpinned data regime). No smoothing, no recursion, no seed — the only lookback operator is the fixed shift. Any other ratio, scaling, span, or smoothing prints a different, unpinned series.
- R4 — Entry (pinned cross-up edge): if FLAT and `ROC5[t] > ROC20[t]` and `ROC5[t−1] <= ROC20[t−1]` (post-warmup) → buy at the next open. A persistent fast-above-slow hold fires exactly once on the crossing bar; exact-equality current (`==`) fails the strict leg and fires nothing.
- R5 — Exit (pinned reverse cross-up edge): if LONG and `ROC20[t] > ROC5[t]` and `ROC20[t−1] <= ROC5[t−1]` (equivalently `ROC5[t] < ROC20[t]` with `ROC5[t−1] >= ROC20[t−1]`) → close the whole book at the next open. The program ships no NaN guard, but every print is defined by construction from index 20 on, so seeding can never smuggle an entry or an exit; pre-warmup bars are flat/hold by record rule.
- R6 — Risk legs (file absence, not invented): stop-loss, take-profit, trailing, time exit, and any second exit are all explicitly disabled — the program ships none, and no prose ships any executable one. The page's stop-loss/take-profit sensitivity table is a parameter sweep overlaid on the same rule, never an order leg — fenced, not adopted. The reverse crossover is the sole exit path.
- R7 — Position state (single deterministic path — no reset, no re-warmup): one 0.01-BTC unit max, long or flat. Safety orders: explicitly none. No cooldown: after any close, the next fast-crosses-above-slow bar re-enters at its next open (`not self.position` guard preserved — while LONG, qualifying cross-up bars are no-ops; while FLAT, reverse-cross bars are no-ops). Entry and exit can never co-fire (entry needs `ROC5[t] > ROC20[t]`, exit needs `ROC5[t] < ROC20[t]` — jointly unsatisfiable on every bar including exact-equality bars, where neither fires) — no tie-break pin is required. The degenerate constant window (both ROCs pinned at exact zero) arms neither leg — verified on planted tape this cycle (0/0 ending FLAT), fenced by arithmetic, disclosed, not patched.
- R8 — Warmup: flat until 100 completed `1d` bars (structural minimum is index 21 — the slow leg needs C[t−20] and the crossover reads the prior bar — verified this cycle; 100 carries margin). The 100-bar pin is frozen: any other warmup is a different, unpinned claim.
- R9 — Invariant identifier: `qtroccross:ROCCrossover-dualroc5-20|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001-nofunding|spot1x|nostop-notarget|warmup100|2026-11-05` (any input, construction, threshold, comparator, direction, sizing, fill, risk, or cost change is a different derivative).

## Required data

- Completed `1d` bars of BTCUSDT: `C[t]` feeds both ROC rails (`O[t]`/`H[t]`/`L[t]` gate nothing). Base-asset volume is unread by every order-gating line. No `funding-signal`, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; both ROCs read trailing completed closes only, never a second feed).
- Warmup: 100 completed `1d` bars flat by record rule — structural minimum is index 21 (binding legs: slow shift `C[t−20]` plus the `t−1` crossover read, verified this cycle). Pre-warmup bars are flat/hold by record rule; missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (windows read completed bars including the decision bar only — same-bar comparison with one-bar history, no lag beyond the pinned shifts, no negative shift), no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance spot, 1x, fixed 0.01 BTC per unit, single-unit book, no compounding. Long side explicitly enabled; short side explicitly disabled (zero short-order tokens in the order path; the lone page-wide `short` token is the prose adjective "short-term" — fenced, never an order). Fills are never conditional on equity or buying power.
- Order timing (source-stated timing preserved verbatim): completed-bar decision with next-bar-open market fills for entries and whole-book closes — the source prose states "trades execute at the open of the bar following the signal", and this record adopts exactly that (the same verified execution primitive as the merged FMZ/QuantifiedTrader lane records; with no stop/limit legs anywhere in the derived machine there is no same-bar TP/SL ordering ambiguity; each bar's outcome is a single deterministic event: hold, open-long, or close-flat, and R7 proves the two legs can never co-fire). This record claims no other fill convention: no same-bar-close print, no maker-touch, no intrabar-path-dependent fill.
- Pinned engine path (verified at the pin this cycle): Hummingbot package label `20260920`, VERSION `dev-2.17.0` (local checkout `2dbc844` carries `hummingbot/VERSION` file `2.17.0`, verified live this cycle; `8b0e067e80ab62f10846d518dcb5a8218527ddb3` is an ancestor of the local checkout, verified via `merge-base --is-ancestor` this cycle; code paths verified at the pin this cycle: `async def run_backtesting` in `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py:221`, `def determine_executor_actions` in `hummingbot/strategy/strategy_v2_base.py:747`, `class OrderExecutorSimulator` in `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py:9`, `INTERVALS "1d" = "1d"` in `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py:24`). Prior merged Alpha PR **#414** reports a 902/902 wheel-file byte match and 33-assert representative validation for this source/package path; this Scout did not independently rehash the wheel. A different deployed package must be revalidated. A strategy-specific, not-yet-implemented controller must compute the trailing dual-ROC pin via `CreateExecutorAction(OrderExecutorConfig)` market legs; the generic executor does not calculate the strategy. The precomputable dual-ROC series plus cross-edge state machine is a plain signal series, not a new execution primitive; no new data requirement, no representative-capability validation owed.
- Stop/limit modeling: none — the derived spec carries zero stop/limit/trailing legs by record rule. No hidden Hummingbot stop-order defaults are relied upon, and with no stop/limit legs there is no same-bar TP/SL ordering ambiguity.
- Sizing/capital/costs: the source models no costs (recorded as the source's, never adopted). Explicit house overlay: single-unit frame, 0.1% taker fee per filled side, slippage unmodeled by declaration; fixed size is event-neutral for timing under state-independent signals. Exchange facts re-verified live this cycle via `api/v3/exchangeInfo`: `BTCUSDT`, `TRADING`, `tickSize 0.01`, min-qty/step 0.00001/0.00001, min-notional 5.0 (`NOTIONAL`). The fixed 0.01 BTC (≈805.74 USDT at the cycle's 24hr last price 80,573.97, above the 5.0 min-notional and an exact multiple of the 0.00001 step). Spot venue means no funding leg exists — constructive exclusion, never modeled-or-realized funding.
- Concurrency: at most one single-asset engine position at any time; the reverse cross ends it (re-entry earliest next signal). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no hedge-mode requirement by construction.

## Evidence

### Source-reported

With exact provenance (page fetched live 2026-11-05, 42,885 bytes, SHA-256 `277a33205dbf9d53da566ec991633248991df8fcc2d9c9bb8cf32ab6aff499f1`; implementation block `class ROCCrossover(Strategy)` with `n_fast = 5` / `n_slow = 20`, `_roc` at exactly the two `self.I` call sites with the helper body unprinted — the name occurs twice, both at call sites; zero `def` prints beyond `init`/`next`), two `self.I` registrations, `crossover(roc_fast, roc_slow) and not position → buy()`, `crossover(roc_slow, roc_fast) and position → position.close()`; zero short/sell/stop/take-profit/trailing order tokens in the order path (`short` occurs once page-wide inside "short-term" prose — fenced; `stop` × 19 / `take_profit` × 16 occur only inside the meta label and the sensitivity-table payload — fenced, not adopted; `trailing` never occurs); daily OHLCV frame, no-lookahead statement, next-bar-open execution, unmodeled costs, equity-index universe, and 2026-10-21 data stamp. This record claims no source-reported performance number as its own — no return, Sharpe, win rate, drawdown, or trade count is carried into the derived specification — and no reproduced performance exists.

### Independently reproduced

**None.** No strategy backtest, event-level Qlib/Hummingbot parity, wheel rehash, deployment or profitability experiment occurred. Pinned engine source inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifacts this run are researcher self-checks of the predicate/estimator/state pipeline (dual-ROC 5/20 + cross-edge pair + 100-bar warmup, next-open single-unit long-flat machine), run in scratch (never committed): logic verification only, not a backtest, not parity.

**Planted-tape verification (this cycle, deterministic):** TAPE-flat (dead-constant 170-bar tape) prints 0 entries / 0 exits ending FLAT — both ROCs pinned at exact zero, neither strict edge armed, as pinned (disclosed never-trades degeneration, not patched); TAPE-up (sustained +1%/day compounding 170-bar tape) prints 0 entries / 0 exits ending FLAT — the 20-bar return permanently exceeds the 5-bar return on smooth geometric ramps so fast never crosses above slow, as pinned (disclosed steady-trend non-participation by construction, not patched); TAPE-down (sustained −1%/day 170-bar tape) prints 0 entries / 0 exits ending FLAT — same arithmetic mirror, as pinned (disclosed, not patched); TAPE-trip (deterministic 260-bar flat/dip/recover/parabolic tape) prints 1 entry / 1 exit ending FLAT (first entry t=105 at FAST −2.4751 vs SLOW −2.9627, first exit t=140 at FAST 4.0645 vs SLOW 4.3455 — the full round trip is exercised, as pinned).

**Live-exchange microstructure probes (this cycle, Binance spot 1d klines, 3,366 completed bars 2017-08-17→2026-11-03; the in-progress 2026-11-04 bar excluded after dedup/sort/close-time check):** 193 post-warmup entries / 192 exits ending LONG (non-degenerate). Two independent runs produce identical digests (event-series digest `83b99f85`). Admission is engineering capability, never an event-rate or profitability claim.

### Negative evidence

1. Single-ROC fence: pool `forven-roc-zero-cross-momentum-long-flat-btcusdt-1h-2026-10-20` (unsmoothed ROC12 against the fixed zero line, cross-edge, 1h, same-close) and pool `roc-sign-state-long-flat-btcusdt-1d-2026-10-11` (ROC30 level-state hold, any-positive-bar long) each read one return ratio against zero — no second ROC rail anywhere, different trigger object, different exit (zero recross vs reverse inter-ROC cross). Never a twin.
2. Smoothed-composite fence: pool `coppock-curve-zero-state-long-flat-btcusdt-1d-2026-10-09` (WMA-smoothed 11/14-ROC sum) and the KST/STC records (multi-horizon weighted sums against signal lines) smooth and combine horizons — this machine races two raw unsmoothed ratios with no averaging anywhere. Never a twin.
3. Dual-average fence: pool EMA/DEMA/TEMA/HMA-cross and MACD/PPO dual-line records race two averages (or an average against its signal line) — this machine averages nothing; both rails are shift ratios. Different trigger object, never a twin. Open PR #662 (Jasonkasei dual-MACD histogram) and #690 (FMZ EMA-stack RSI-recross) are different indicator families with different gates — never a twin.
4. Level-system fence: pool AD-line/OBV/CMF and balance-of-power records command on volume-weighted accumulation levels or normalized price-location oscillators, never a dual return-ratio cross — never a twin.
5. Single-print-twin fence: no twin is admitted — any input change (e.g. 5/20 → any other pair), any level-hold or zero-gated variant, any gated, bracketed, or stop-carrying variant, any smoothed ROC construction, frame, fill, venue, or book is a different, unpinned rule.
6. Seed fence: the ROC construction is a pure fixed-shift ratio with no recursion and no seed; every print from index 20 is defined by construction so no guard is invented. Smoothing, reseeding, or warming differently is a different, unpinned rule.
7. Warmup-identity fence, admitted plainly: the pin is 100 completed bars (structural minimum index 21); any other warmup remains a different, unpinned claim even where it prints the same book.
8. Number silence fenced: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from any source is adopted anywhere, and any dispute over exact magnitudes is decided against this record, never patched by inference.
9. Version fence: this record follows the QuantifiedTrader page as fetched 2026-11-05 (data stamp 2026-10-21 printed in page meta). If the page is ever edited, this record does not move with it.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: inputs `5` / `20` / textbook shift-ratio ROC construction / dual cross-edge pair / long-flat book / no-stop-no-target posture / `1d` BTCUSDT spot / next-open fills / 0.01 BTC / 0.1% costs / 100-bar warmup are frozen.

- F1 — Dual-rail relevance: a single-rail twin (enter on `ROC5[t] > 0` while flat, exit on `ROC5[t] < 0` — same rest) must not improve net expectancy; fail ⇒ the slow rail adds nothing over a zero line, and the record is a gate label on a single-ROC machine.
- F2 — Edge-shape relevance: a level-hold twin (long whenever `ROC5[t] > ROC20[t]` while flat — same rest) must not improve net expectancy; fail ⇒ the cross edge adds nothing over holding every fast-above-slow bar, and the distinction is decorative.
- F3 — Horizon relevance: swapping the pair to `10` / `30` (same rest) must not improve net expectancy; fail ⇒ the 5/20 choice adds nothing over any neighboring pair and the pin is arbitrary decoration.
- F4 — Warmup relevance: the pinned 100 print and a 100-vs-100 re-run must print the identical event set (determinism check — digest `83b99f85` is the tripwire); fail ⇒ nondeterminism or seed leakage past the declared warmup.

## Crypto portability

Pinned to BTCUSDT Binance spot under the house overlay (declared port of an equity-index-headed backtesting.py program). The rule reads completed daily closes only, so no pit-session, gap, roll, split/dividend-adjustment, or corporate-action logic ports (equity-calendar effects are non-issues on spot — disclosed, not modeled; crypto gaps between bars feed the ratios only through the printed close reads, disclosed). No volume read means equity-vs-crypto volume-regime comparability is a non-issue here — disclosed without re-tuning; the rule fires at a cadence the source never measured (193 entries across 3,266 post-warmup bars here), disclosed. The rule is long-flat, so a spot deployment expresses the full machine with no short permission — a two-sided or perpetual variant would be a different, unpinned claim (this record's gate-5 evidence is the spot path only; the source's equity universe is provenance, not execution). No warmup history beyond 100 `1d` bars is consumed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Never-trades degeneration by construction: an exactly flat tape pins both ROCs at exact zero, so neither strict edge ever arms (planted dead-flat tape: 0/0 ending FLAT — disclosed, not upgraded).
- Steady-trend non-participation by construction: smooth geometric ramps pin the slow return above the fast return, so the entry edge never arms (planted sustained-up and sustained-down tapes: both 0/0 ending FLAT — disclosed, not patched).
- Chop-whip by construction: two moving ratios crossing and recrossing print repeated round trips with no stop or target (planted trip tape: 1/1 ending FLAT; live probes show the same edge-race texture) — disclosed, not patched.
- Single-venue port residual: backtesting.py close-ratio arithmetic vs Binance spot execution (prints, fees, open-definition across 24/7 sessions) is unclaimed, disclosed.
- Next-open latency idealization: signal cadence on the decision close print while fills land on the next open; any live gap between the two differs by construction — disclosed, research-only (this convention is the source's own stated execution, preserved verbatim).
- Hold-band residual: the machine commands nothing while the fast/slow ordering persists — multi-week holds through ordered chop that never recrosses are the normal case, not an anomaly, disclosed.
- No-authorship-page residual: the page prints no handle, license, or creation stamp; provenance rests on the QuantifiedTrader URL/slug, printed names, page hash, data stamp, and fetch date — disclosed.
- Performance evidence is absent: nothing here is calibrated, fitted, or tuned to any backtest (the `5` / `20` defaults are the source's, never re-run here; the page's own grid-search section, where available, is not adopted as a parameter source; the page's printed Sharpe/return/drawdown figures are fenced, never adopted).
- Author scope: the page ships exploratory research with an explicit not-investment-advice posture in the site family, not a vetted trading system — this record is research-only and claims no live suitability.

## Implementation status

`not-implemented`: no dedicated controller, Qlib executable recipe or deployment artifact was created. PASS is a bounded research-expressibility proposal, not a claim of already runnable materialization. A selected strategy may later need the minimal strategy-specific implementation without a second admission flag.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review must independently inspect this exact PR head, remediate only primary-source-verifiable facts, then PASS exact-head merge or NOT_LOSSLESS close. Scout does not approve, merge, close, trade, backtest or deploy.

## Related Wiki records

None asserted.

## Sources

- Primary page + pin: https://quantifiedtrader.com/backtest/strategies/roc-crossover/ (`ROCCrossover`; page fetched live 2026-11-05, 42,885 bytes, SHA-256 `277a33205dbf9d53da566ec991633248991df8fcc2d9c9bb8cf32ab6aff499f1`; implementation block `class ROCCrossover(Strategy)` with `n_fast = 5` / `n_slow = 20`, `_roc` at exactly the two `self.I` call sites (helper body unprinted — the name occurs twice, both at call sites; zero `def` prints beyond `init`/`next`), `crossover(roc_fast, roc_slow) and not position → buy()`, `crossover(roc_slow, roc_fast) and position → position.close()`; zero short/sell/stop/take-profit/trailing order tokens in the order path (`short` occurs once page-wide inside "short-term" prose — fenced; `stop` × 19 / `take_profit` × 16 occur only inside the meta label and sensitivity-table payload — fenced, not adopted; `trailing` never occurs); daily OHLCV frame, no-lookahead statement, next-bar-open execution, unmodeled costs, equity-index universe, 2026-10-21 data stamp)
- Lane precedent (different mechanism, unmerged-proof never claimed): `quantifiedtrader-elder-ray-bull-bear-power-long-flat-btcusdt-1d-2026-11-05.md`, `quantifiedtrader-qstick-body-cross-long-flat-btcusdt-1d-2026-11-05.md`, `quantifiedtrader-money-flow-index-dip-level-long-flat-btcusdt-1d-2026-11-05.md`, `quantifiedtrader-bb-width-squeeze-sma-state-long-flat-btcusdt-1d-2026-11-05.md`, `quantifiedtrader-atr-bands-lower-touch-midline-exit-long-flat-btcusdt-1d-2026-11-05.md`, `quantifiedtrader-keltner-squeeze-upper-breakout-sma-exit-long-flat-btcusdt-1d-2026-11-05.md`, `quantifiedtrader-raff-channel-midline-level-long-flat-btcusdt-1d-2026-11-04.md` and `quantifiedtrader-projection-oscillator-zero-cross-long-flat-btcusdt-1d-2026-11-04.md` (unprinted-helper textbook-freeze derivation pattern)
- Nearest pool lineage (different mechanism, unmerged-proof never claimed): `forven-roc-zero-cross-momentum-long-flat-btcusdt-1h-2026-10-20.md` (single ROC12-vs-zero cross-edge machine — one rail, fixed level, different exit), `roc-sign-state-long-flat-btcusdt-1d-2026-10-11.md` (single ROC30 level-state hold — no edge, no second rail) and `coppock-curve-zero-state-long-flat-btcusdt-1d-2026-10-09.md` (WMA-smoothed dual-ROC composite — smoothed, summed, different exit, fenced in Negative evidence)
- Exchange verification: Binance spot `api/v3/exchangeInfo` (`BTCUSDT`, `TRADING`, `tickSize 0.01`, min-qty/step 0.00001/0.00001, min-notional 5.0 via `NOTIONAL`) plus `api/v3/klines` 1d probes (3,366 completed bars 2017-08-17→2026-11-03, in-progress 2026-11-04 bar excluded after dedup/sort/close-time check; 193 post-warmup entries / 192 exits ending LONG, event digest `83b99f85` double-run identical; planted tapes flat 0/0 FLAT, up 0/0 FLAT, down 0/0 FLAT, dip-recover-parabolic trip 1/1 FLAT with first entry t=105 / first exit t=140 — degeneration/non-participation/round-trip fences), fetched live 2026-11-05
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently merged pinned package/source evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
