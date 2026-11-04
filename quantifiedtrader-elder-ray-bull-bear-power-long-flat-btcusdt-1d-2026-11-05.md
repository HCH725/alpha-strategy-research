---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: QuantifiedTrader Elder Ray bull-bear-power long-flat on BTCUSDT 1d bars
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
  - https://quantifiedtrader.com/backtest/strategies/elder-ray/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# QuantifiedTrader Elder Ray bull-bear-power long-flat on BTCUSDT 1d bars

## Provenance

**Primary source (fetched live over HTTPS this cycle):** QuantifiedTrader public strategy-library page `https://quantifiedtrader.com/backtest/strategies/elder-ray/` (`Elder Ray`), fetched 2026-11-05 as a 42,825-byte page (SHA-256 `854a56099b57603167a2d0b9735c3322fcb1c4055864e8ed635581f00b91c08d`). The page prints no login, paywall, or author handle; its meta description prints the data stamp `Data as of 2026-10-21` (adopted as `source_as_of`; the fetch date is the verification date, per the merged QuantifiedTrader Raff-Channel / Projection-Oscillator / Keltner-Squeeze / ATR-Bands / BB-Width-Squeeze / MFI / QStick lane precedent). The strategy-implementation code block is printed verbatim on the page (backtesting.py shape):

```text
class ElderRay(Strategy):
    n = 13
    def init(self):
        ema = _ema(pd.Series(self.data.Close), self.n)
        self.bull = self.I(lambda: pd.Series(self.data.High) - ema, name="Bull")
        self.bear = self.I(lambda: pd.Series(self.data.Low) - ema, name="Bear")
    def next(self):
        if self.bull[-1] > 0 and self.bull[-1] > self.bull[-2] and not self.position: self.buy()
        elif self.bear[-1] > 0 and self.position: self.position.close()
```

Code census this cycle over the saved page bytes: 1 `buy()` / 1 `position.close()` / 0 `crossover` calls / 2 indicator registrations (`self.I`) / `_ema` exactly once, at its call site, with zero `def _` definitions printed anywhere — the helper body is unprinted, the same gap shape the merged Raff-Channel / Projection-Oscillator / Keltner-Squeeze / ATR-Bands / BB-Width-Squeeze / MFI / QStick lane records froze via textbook construction. `def ` occurs exactly twice (`init`, `next`). The `short` token never occurs in page bytes. (`stop` / `take_profit` tokens occur only inside the page's stop-loss/take-profit sensitivity table payload and its "stop-loss / take-profit sensitivity" meta label — fenced, never an order leg; `trailing` never occurs.) This record cites and normalizes the rule and reproduces no source block beyond the short declarations quoted for gate evidence.

**Facts actually supplied by the source page:** backtested on **daily OHLCV** across major US equity indices and ETFs; entry/exit signals carry **no lookahead bias**; **trades execute at the open of the bar following the signal**; performance metrics are computed per symbol; the parameter grid-search section, where available, is not adopted as a parameter source; **transaction costs and slippage are not modeled**. Signal prose: "Elder Ray splits price action into Bull Power (High minus EMA) and Bear Power (Low minus EMA). Enters long when Bull Power is positive and rising, exits when Bear Power turns positive." The meta description prints average Sharpe −0.43, return −12.8%, max drawdown 33.6% with best symbol Merval Sharpe 0.88 — no return, Sharpe, win-rate, drawdown, or trade-count figure from the source is carried into the derived specification anywhere.

**Prose-vs-code fence (code governs):** the prose says "exits when Bear Power turns positive" but the program tests the level `bear[-1] > 0`, not a cross-up edge — any positive-Bear bar ends the position, not only a fresh turn-positive bar. The executable rule follows the program level, never the prose edge. The entry leg is a true edge-plus-rising conjunction (`bull[-1] > 0 and bull[-1] > bull[-2]`) — a bar parked positive-but-flat never enters; only the `not self.position` guard plus the rising leg stop re-entry. Both legs are quoted as printed.

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the source ships equity-universe backtesting.py semantics with no venue/fill/cost leg this record can reuse verbatim. Researcher-declared adaptations are exactly six: (1) market pin **BTCUSDT Binance spot 1d** (long-flat needs no margin-short permission; spot is the minimal realistic venue — the source's equity-index universe is kept separate, never claimed); (2) completed-bar decisions with **next-bar-open market** fills (the source's own stated execution — "trades execute at the open of the bar following the signal" — preserved verbatim); (3) input frozen at `n = 13` with the closed-form textbook construction below (13-bar exponential moving average of closes with span-13 `adjust=False` recursion seeded at the first close, matching the same site's inline `ewm(span=..., adjust=False)` convention on its KST/STC pages — verified deterministic this cycle; `_ema` is the ordinary EMA, disclosed as the researcher freeze for the unprinted helper); (4) adopted **100-bar warmup** with pre-warmup bars flat by record rule (structural minimum is index 1 — the entry leg reads `bull[-2]` — verified this cycle; 100 carries margin); (5) house sizing/costs replacing the source's no-cost model (fixed 0.01 BTC, 0.1%/side taker; spot means no funding leg exists — constructive exclusion, never zero-claimed; fixed size is event-neutral for timing under state-independent signals); (6) missing-bar stretches freeze evaluation at the prior target — book and ledger retained across the freeze, evaluation resumes on the next valid bar with no warmup repetition, never backfilled, never forced flat. The positive-and-rising Bull entry, the positive-Bear level exit, the long-only stance, and the no-stop/no-target posture are source-pinned or predeclared; no short leg is invented.

**Immutable derivative identity:** `qtelderray:ElderRay-bullrising-bearlevel-ema13|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001-nofunding|spot1x|nostop-notarget|warmup100|2026-11-05`. Changing any input, EMA construction, threshold, comparator, direction, timing, market, risk, cost, sizing, or book state creates a different derivative.

**Pre-write dedup (2026-11-05):** working-tree base is current `main@1ede1f82` (567 root strategy records, READMEs excluded; this file is the 568th). Content searches for the canonical slug `strategies/elder-ray`, the class name `class ElderRay`, and the exact construction tokens `Bull Power` / `Bear Power` return zero same-source/same-construction records (the pool's two Elder relatives are fenced in Negative evidence: the FMZ-432762 123-reversal-plus-bull-power two-sided combo and the Elder-Impulse dual-slope system — different legs, direction, frame, and fill; generic `ema`/`power` hits are EMA-family or unrelated records, never a High-minus-EMA13 / Low-minus-EMA13 bull-bear machine). No open `research/*` PR is this page, author, construction, or signal (17 open PRs enumerated this cycle — #48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708, #725 — none is an Elder Ray, bull/bear-power, or QuantifiedTrader-oscillator machine). No duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

Bull-vs-bear power split, long side only. Bull Power (`High − EMA`) measures how far buyers can lift the bar's top above the trailing average; Bear Power (`Low − EMA`) measures where the bar's bottom sits against the same average. The position opens when buyers show positive and still-strengthening power and ends it on any bar where even the low prints above the average (the page's overheat/exhaustion exit). The equity-index universe and the unmodeled-costs stance are source facts, not this record's venue or economics. No performance figure is carried anywhere.

### Research interpretation

Asymmetric power machine — the impatient cousin of the pool's FMZ Elder combo record (which needs a 123-reversal agreement plus a day-anchored session-high bull leg, holds a side two-sided, and never reads a rising-Bull edge) and the structural sibling of the merged QuantifiedTrader QStick record (edge entry plus level exit, same lane, same venue/timing/cost freeze). Unlike zero-line oscillators on a single spread (ROC-sign, QStick body average, Coppock curve) this machine reads two spreads against one shared EMA rail, and unlike price-vs-average trend filters (SMA50 level, price-above-SMA) the entry demands a rising print, not a level hold. The exit leg is the honest quirk, verified this cycle: on smooth ramps `BEAR > 0` is true almost everywhere, so fresh entries usually flatten on the very next bar (planted sustained-up tape prints 35 entries / 34 exits ending LONG — disclosed churn by construction, not patched, the opposite of the QStick lane's patient holds). The failure mode is equally plain: an exactly flat tape pins Bull Power at a positive constant that never rises, so the machine never trades (planted dead-flat tape prints 0 entries / 0 exits ending FLAT — disclosed, not patched); a sustained bleed never prints positive Bull Power (planted sustained-down tape prints 0/0 ending FLAT — disclosed); the round trip is exercised on the planted dip-rip-parabolic tape (31 entries / 31 exits ending FLAT, first entry t=129 at BULL 0.5735 ex −0.1605, first exit t=130 at BEAR 0.8637 — disclosed).

## Signal

Exact rule as pinned (daily decision on completed `1d` bars; entries/exits next-bar-open market; long-flat single-unit book — any other input, EMA construction, threshold, sizing, fill, or cost is a different, unpinned rule):

- R1 — Measure grid: completed `1d` bars of BTCUSDT spot only. Continuous calendar days; no session template, no holiday skip. Bar time is never read by any order-gating line.
- R2 — Source series: `O[t]` is unread; `H[t]`/`L[t]`/`C[t]` feed the power construction only (volume fills nothing and gates nothing). No funding/OI/mark-index read gates on any order; no sentiment/macro/on-chain/cross-venue state. Single timeframe, single asset.
- R3 — Power stack (frozen, researcher-pinned textbook construction for the unprinted helper): `EMA[t]` is the span-13 `adjust=False` recursion seeded at the first close (`EMA[0] = C[0]`, `EMA[t] = a·C[t] + (1−a)·EMA[t−1]` with `a = 2/14` — verified deterministic this cycle); `BULL[t] = H[t] − EMA[t]`; `BEAR[t] = L[t] − EMA[t]`. Finite on every bar by construction. Any other average, span, seeding, or adjustment prints a different, unpinned series.
- R4 — Entry (pinned, positive-and-rising conjunction): if FLAT and `BULL[t] > 0` and `BULL[t] > BULL[t−1]` (post-warmup) → buy at the next open. A positive-but-flat print fires nothing; exact-zero current (`== 0`) fails the strict leg and fires nothing.
- R5 — Exit (pinned, positive-Bear level): if LONG and `BEAR[t] > 0` → close the whole book at the next open. The exit is a level hold, not an edge — it fires on any positive-Bear bar, including the bar after entry on smooth ramps (disclosed one-bar-hold churn, not patched). The program ships no NaN guard, but every print is finite by construction, so seeding can never smuggle an entry or an exit; pre-warmup bars are flat/hold by record rule.
- R6 — Risk legs (file absence, not invented): stop-loss, take-profit, trailing, time exit, and any second exit are all explicitly disabled — the program ships none, and no prose ships any executable one. The page's stop-loss/take-profit sensitivity table is a parameter sweep overlaid on the same rule, never an order leg — fenced, not adopted. The positive-Bear print is the sole exit path.
- R7 — Position state (single deterministic path — no reset, no re-warmup): one 0.01-BTC unit max, long or flat. Safety orders: explicitly none. No cooldown: after any close, the next positive-and-rising Bull bar re-enters at its next open (`not self.position` guard preserved — while LONG, qualifying Bull bars are no-ops; while FLAT, positive-Bear bars are no-ops). Entry and exit can never co-fire (entry needs FLAT, exit needs LONG — jointly unsatisfiable by state) — no tie-break pin is required. The degenerate constant window (BULL pinned at a positive constant, never rising) arms neither leg — verified on planted tape this cycle (0/0 ending FLAT), fenced by arithmetic, disclosed, not patched.
- R8 — Warmup: flat until 100 completed `1d` bars (structural minimum is index 1 — the entry leg reads `bull[-2]` — verified this cycle; 100 carries margin). The 100-bar pin is frozen: any other warmup is a different, unpinned claim.
- R9 — Invariant identifier: `qtelderray:ElderRay-bullrising-bearlevel-ema13|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001-nofunding|spot1x|nostop-notarget|warmup100|2026-11-05` (any input, construction, threshold, comparator, direction, sizing, fill, risk, or cost change is a different derivative).

## Required data

- Completed `1d` bars of BTCUSDT: `H[t]`/`L[t]`/`C[t]` feed the EMA rail and the two power spreads (`O[t]` gates nothing). Base-asset volume is unread by every order-gating line. No `funding-signal`, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; the EMA reads trailing completed closes only, never a second feed).
- Warmup: 100 completed `1d` bars flat by record rule — structural minimum is index 1 (binding leg: `bull[-2]` read, verified this cycle). Pre-warmup bars are flat/hold by record rule; missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (window reads completed bars including the decision bar only — same-bar comparison, no lag, no negative shift), no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance spot, 1x, fixed 0.01 BTC per unit, single-unit book, no compounding. Long side explicitly enabled; short side explicitly disabled (zero `short` tokens in page bytes; zero short order calls in the printed program). Fills are never conditional on equity or buying power.
- Order timing (source-stated timing preserved verbatim): completed-bar decision with next-bar-open market fills for entries and whole-book closes — the source prose states "trades execute at the open of the bar following the signal", and this record adopts exactly that (the same verified execution primitive as the merged FMZ/QuantifiedTrader lane records; with no stop/limit legs anywhere in the derived machine there is no same-bar TP/SL ordering ambiguity; each bar's outcome is a single deterministic event: hold, open-long, or close-flat, and R7 proves the two legs can never co-fire). This record claims no other fill convention: no same-bar-close print, no maker-touch, no intrabar-path-dependent fill.
- Pinned engine path (verified at the pin this cycle): Hummingbot package label `20260920`, VERSION `dev-2.17.0` (local checkout `2dbc844` carries `hummingbot/VERSION` file `2.17.0`, verified live this cycle; `8b0e067e80ab62f10846d518dcb5a8218527ddb3` is an ancestor of the local checkout, verified via `merge-base --is-ancestor` this cycle; code paths verified at the pin this cycle: `async def run_backtesting` in `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py:221`, `def determine_executor_actions` in `hummingbot/strategy/strategy_v2_base.py:747`, `class OrderExecutorSimulator` in `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py:9`, `INTERVALS "1d" = "1d"` in `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py:24`). Prior merged Alpha PR **#414** reports a 902/902 wheel-file byte match and 33-assert representative validation for this source/package path; this Scout did not independently rehash the wheel. A different deployed package must be revalidated. A strategy-specific, not-yet-implemented controller must compute the trailing EMA13-plus-power pin via `CreateExecutorAction(OrderExecutorConfig)` market legs; the generic executor does not calculate the strategy. The precomputable power series plus conjunction/level state machine is a plain signal series, not a new execution primitive; no new data requirement, no representative-capability validation owed.
- Stop/limit modeling: none — the derived spec carries zero stop/limit/trailing legs by record rule. No hidden Hummingbot stop-order defaults are relied upon, and with no stop/limit legs there is no same-bar TP/SL ordering ambiguity.
- Sizing/capital/costs: the source models no costs (recorded as the source's, never adopted). Explicit house overlay: single-unit frame, 0.1% taker fee per filled side, slippage unmodeled by declaration; fixed size is event-neutral for timing under state-independent signals. Exchange facts re-verified live this cycle via `api/v3/exchangeInfo`: `BTCUSDT`, `TRADING`, `tickSize 0.01`, min-qty/step 0.00001/0.00001, min-notional 5.0 (`NOTIONAL`). The fixed 0.01 BTC (≈807.59 USDT at the cycle's 24hr last price 80,759.07, above the 5.0 min-notional and an exact multiple of the 0.00001 step). Spot venue means no funding leg exists — constructive exclusion, never modeled-or-realized funding.
- Concurrency: at most one single-asset engine position at any time; the positive-Bear print ends it (re-entry earliest next signal). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no hedge-mode requirement by construction.

## Evidence

### Source-reported

With exact provenance (page fetched live 2026-11-05, 42,825 bytes, SHA-256 `854a56099b57603167a2d0b9735c3322fcb1c4055864e8ed635581f00b91c08d`; implementation block `class ElderRay(Strategy)` with `n = 13`, EMA line `_ema(Close, 13)` (helper body unprinted — the name occurs once, at its call site; zero `def` prints beyond `init`/`next`), `bull = High − ema` / `bear = Low − ema` series, two `self.I` registrations, `bull[-1] > 0 and bull[-1] > bull[-2] and not position → buy()`, `bear[-1] > 0 and position → position.close()`; zero short/crossover order calls in the order path; stop/take-profit tokens fenced to the sensitivity table, never the code): the frozen input; the H/L/C reads; the positive-and-rising entry conjunction with strict comparators; the positive-Bear level exit; the `not self.position` single-unit guard; the long-only order set; the source's daily-OHLCV frame, no-lookahead statement, next-bar-open execution, unmodeled-costs stance, equity-index universe, and 2026-10-21 data stamp. This record claims no source-reported performance number as its own — no return, Sharpe, win rate, drawdown, or trade count is carried into the derived specification — and no reproduced performance exists.

### Independently reproduced

**None.** No strategy backtest, event-level Qlib/Hummingbot parity, wheel rehash, deployment or profitability experiment occurred. Pinned engine source inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifacts this run are researcher self-checks of the predicate/estimator/state pipeline (EMA13 + bull-rising/bear-level + 100-bar warmup, next-open single-unit long-flat machine), run in scratch (never committed): logic verification only, not a backtest, not parity.

**Planted-tape verification (this cycle, deterministic):** TAPE-flat (dead-constant 170-bar tape) prints 0 entries / 0 exits ending FLAT — Bull Power pinned at a positive constant that never rises, as pinned (disclosed never-trades degeneration, not patched); TAPE-up (sustained +1%/day compounding 170-bar tape) prints 35 entries / 34 exits ending LONG — fresh entries flatten on the next bar almost everywhere since `BEAR > 0` holds across smooth ramps, as pinned (disclosed churn by construction, not patched); TAPE-down (sustained −1%/day 170-bar tape) prints 0 entries / 0 exits ending FLAT — Bull Power never prints positive, as pinned (disclosed, not patched); TAPE-trip (deterministic 260-bar flat/dip/recover/parabolic tape) prints 31 entries / 31 exits ending FLAT (first entry t=129 at BULL 0.5735 ex −0.1605, first exit t=130 at BEAR 0.8637 — the full round trip is exercised, as pinned).

**Live-exchange microstructure probes (this cycle, Binance spot 1d klines, 3,366 completed bars 2017-08-17→2026-11-03; the in-progress 2026-11-04 bar excluded after dedup/sort/close-time check):** 444 post-warmup entries / 443 exits ending LONG (non-degenerate; 2,272 positive-Bull bars and 1,103 positive-Bear bars in range, zero exact-zero Bull prints). Two independent runs produce identical digests (event-series digest `b4f0176a`). Admission is engineering capability, never an event-rate or profitability claim.

### Negative evidence

1. FMZ-combo fence: pool `elder-ray-123reversal-combo-two-sided-btcusdt-1h-2026-10-09` (FMZ 432762, 14-bar stoch 123-reversal agreement AND a day-anchored session-high bull leg, two-sided always-evaluated state on 1h with same-bar-close fills) shares only the words "bull power" — no rising-Bull edge, no Bear-level exit, no shared series (session-high anchor vs trailing EMA13), different direction, frame, and fill. Never a twin.
2. Impulse-system fence: pool `elder-impulse-dual-slope-state-flip-two-sided-btcusdt-1d-2026-10-10` (Elder Impulse: EMA slope plus MACD-histogram color state) reads no High-minus-EMA / Low-minus-EMA spread anywhere — different trigger object, never a twin.
3. Power-oscillator fence: pool `balance-of-power-cross` (normalized BOP cross) and the merged QuantifiedTrader MFI/QStick records command on single-spread or volume-weighted constructions, never a dual High/Low-vs-EMA power pair with a rising conjunction — never a twin.
4. Trend-filter fence: pool SMA/EMA-cross, price-vs-average, and MACD-signal records test level holds or line crosses, never a positive-and-rising Bull Power gate paired with a positive-Bear level exit — no shared leg anywhere — never a twin.
5. Single-print-twin fence: no twin is admitted — any input change (e.g. 13→14 span), any level-hold or two-sided variant, any gated, bracketed, or stop-carrying variant, any other EMA construction, frame, fill, venue, or book is a different, unpinned rule.
6. Seed fence: the EMA recursion is seeded at the first close with `adjust=False` span-13 weights as part of the pin; every print is finite by construction so no guard is invented. Reseeding, warming differently, or switching adjustment is a different, unpinned rule.
7. Warmup-identity fence, admitted plainly: the pin is 100 completed bars (structural minimum index 1); any other warmup remains a different, unpinned claim even where it prints the same book.
8. Number silence fenced: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from any source is adopted anywhere, and any dispute over exact magnitudes is decided against this record, never patched by inference.
9. Version fence: this record follows the QuantifiedTrader page as fetched 2026-11-05 (data stamp 2026-10-21 printed in page meta). If the page is ever edited, this record does not move with it.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: input `13` / textbook span-13 `adjust=False` EMA construction / positive-and-rising Bull entry / positive-Bear level exit / long-flat book / no-stop-no-target posture / `1d` BTCUSDT spot / next-open fills / 0.01 BTC / 0.1% costs / 100-bar warmup are frozen.

- F1 — Rising-gate relevance: a level-hold twin (enter whenever `BULL[t] > 0` while flat — same rest) must not improve net expectancy; fail ⇒ the rising conjunction adds nothing over holding every positive-Bull bar, and the record is a gate label on a hold machine.
- F2 — Exit-shape relevance: a cross-up twin (exit only on a fresh `BEAR[t-1] <= 0` → `BEAR[t] > 0` cross — same rest) must not improve net expectancy; fail ⇒ the always-armed level exit adds nothing over an edge exit, and the distinction is decorative.
- F3 — Rail relevance: replacing the EMA13 rail with an SMA13 rail (`High − SMA13` / `Low − SMA13` — same rest) must not improve net expectancy; fail ⇒ the exponential rail adds nothing over the ordinary average.
- F4 — Warmup relevance: the pinned 100 print and a 100-vs-100 re-run must print the identical event set (determinism check — digest `b4f0176a` is the tripwire); fail ⇒ nondeterminism or seed leakage past the declared warmup.

## Crypto portability

Pinned to BTCUSDT Binance spot under the house overlay (declared port of an equity-index-headed backtesting.py program). The rule reads completed daily H/L/C prints only, so no pit-session, gap, roll, split/dividend-adjustment, or corporate-action logic ports (equity-calendar effects are non-issues on spot — disclosed, not modeled; crypto gaps between bars feed the spreads only through the printed H/L/C reads, disclosed). No volume read means equity-vs-crypto volume-regime comparability is a non-issue here — disclosed without re-tuning; the rule fires at a cadence the source never measured (444 entries across 3,266 post-warmup bars here), disclosed. The rule is long-flat, so a spot deployment expresses the full machine with no short permission — a two-sided or perpetual variant would be a different, unpinned claim (this record's gate-5 evidence is the spot path only; the source's equity universe is provenance, not execution). No warmup history beyond 100 `1d` bars is consumed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Never-trades degeneration by construction: an exactly flat tape pins Bull Power at a positive constant that never rises, so neither leg ever arms (planted dead-flat tape: 0/0 ending FLAT — disclosed, not upgraded).
- Churn by construction: on smooth ramps the positive-Bear exit is true almost everywhere, so fresh entries usually flatten on the very next bar (planted sustained-up tape: 35/34 ending LONG; live probes show the same one-bar-hold texture) — disclosed, not patched.
- Bleed non-participation by construction: sustained bleeds never print positive Bull Power (planted sustained-down tape: 0/0 ending FLAT) — disclosed, not patched.
- Single-venue port residual: backtesting.py H/L/C arithmetic vs Binance spot execution (prints, fees, open-definition across 24/7 sessions) is unclaimed, disclosed.
- Next-open latency idealization: signal cadence on the decision close print while fills land on the next open; any live gap between the two differs by construction — disclosed, research-only (this convention is the source's own stated execution, preserved verbatim).
- Hold-band residual: the exit commands nothing while Bear Power sits at or below zero — multi-week holds through chop that never prints positive-Bear are the normal case, not an anomaly, disclosed.
- No-authorship-page residual: the page prints no handle, license, or creation stamp; provenance rests on the QuantifiedTrader URL/slug, printed names, page hash, data stamp, and fetch date — disclosed.
- Performance evidence is absent: nothing here is calibrated, fitted, or tuned to any backtest (the `13` default is the source's, never re-run here; the page's own grid-search section, where available, is not adopted as a parameter source; the page's printed Sharpe/return/drawdown figures are fenced, never adopted).
- Author scope: the page ships exploratory research with an explicit not-investment-advice disclaimer, not a vetted trading system — this record is research-only and claims no live suitability.

## Implementation status

`not-implemented`: no dedicated controller, Qlib executable recipe or deployment artifact was created. PASS is a bounded research-expressibility proposal, not a claim of already runnable materialization. A selected strategy may later need the minimal strategy-specific implementation without a second admission flag.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review must independently inspect this exact PR head, remediate only primary-source-verifiable facts, then PASS exact-head merge or NOT_LOSSLESS close. Scout does not approve, merge, close, trade, backtest or deploy.

## Related Wiki records

None asserted.

## Sources

- Primary page + pin: https://quantifiedtrader.com/backtest/strategies/elder-ray/ (`ElderRay`; page fetched live 2026-11-05, 42,825 bytes, SHA-256 `854a56099b57603167a2d0b9735c3322fcb1c4055864e8ed635581f00b91c08d`; implementation block `class ElderRay(Strategy)` with `n = 13`, EMA line `_ema(Close, 13)` (helper body unprinted — the name occurs once, at its call site; zero `def` prints beyond `init`/`next`), `bull = High − ema` / `bear = Low − ema` series, two `self.I` registrations, `bull[-1] > 0 and bull[-1] > bull[-2] and not position → buy()`, `bear[-1] > 0 and position → position.close()`; zero short/crossover order calls in the order path (`stop`/`take_profit` tokens occur only inside the stop-loss/take-profit sensitivity table payload and label — fenced, not adopted; `trailing` never occurs); daily OHLCV frame, no-lookahead statement, next-bar-open execution, unmodeled costs, equity-index universe, 2026-10-21 data stamp)
- Lane precedent (different mechanism, unmerged-proof never claimed): `quantifiedtrader-qstick-body-cross-long-flat-btcusdt-1d-2026-11-05.md`, `quantifiedtrader-money-flow-index-dip-level-long-flat-btcusdt-1d-2026-11-05.md`, `quantifiedtrader-bb-width-squeeze-sma-state-long-flat-btcusdt-1d-2026-11-05.md`, `quantifiedtrader-atr-bands-lower-touch-midline-exit-long-flat-btcusdt-1d-2026-11-05.md`, `quantifiedtrader-keltner-squeeze-upper-breakout-sma-exit-long-flat-btcusdt-1d-2026-11-05.md`, `quantifiedtrader-raff-channel-midline-level-long-flat-btcusdt-1d-2026-11-04.md` and `quantifiedtrader-projection-oscillator-zero-cross-long-flat-btcusdt-1d-2026-11-04.md` (unprinted-helper textbook-freeze derivation pattern)
- Nearest pool lineage (different mechanism, unmerged-proof never claimed): `elder-ray-123reversal-combo-two-sided-btcusdt-1h-2026-10-09.md` (FMZ 432762 123-reversal-plus-session-high-bull two-sided 1h same-close machine — reversal leg, day anchor, direction, frame, and fill all differ, fenced in Negative evidence) and `elder-impulse-dual-slope-state-flip-two-sided-btcusdt-1d-2026-10-10.md` (EMA-slope plus MACD-histogram state system — no power spread anywhere, fenced in Negative evidence)
- Exchange verification: Binance spot `api/v3/exchangeInfo` (`BTCUSDT`, `TRADING`, `tickSize 0.01`, min-qty/step 0.00001/0.00001, min-notional 5.0 via `NOTIONAL`) plus `api/v3/klines` 1d probes (3,366 completed bars 2017-08-17→2026-11-03, in-progress 2026-11-04 bar excluded after dedup/sort/close-time check; 444 post-warmup entries / 443 exits ending LONG, event digest `b4f0176a` double-run identical; planted tapes flat 0/0 FLAT, up 35/34 LONG, down 0/0 FLAT, dip-rip-parabolic trip 31/31 FLAT with first entry t=129 / first exit t=130 — degeneration/churn/round-trip fences), fetched live 2026-11-05
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently merged pinned package/source evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
