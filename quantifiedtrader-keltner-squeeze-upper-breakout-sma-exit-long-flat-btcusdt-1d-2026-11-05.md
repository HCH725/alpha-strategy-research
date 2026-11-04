---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: QuantifiedTrader Keltner Squeeze upper-breakout SMA-exit long-flat on BTCUSDT 1d bars
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
  - https://quantifiedtrader.com/backtest/strategies/keltner-squeeze/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# QuantifiedTrader Keltner Squeeze upper-breakout SMA-exit long-flat on BTCUSDT 1d bars

## Provenance

**Primary source (fetched live over HTTPS this cycle):** QuantifiedTrader public strategy-library page `https://quantifiedtrader.com/backtest/strategies/keltner-squeeze/` (`Keltner Squeeze`), fetched 2026-11-05 as a 43,001-byte page (SHA-256 `489824bfb591abf3548037bb29b11e2f3068a437878437db495115794da18882`). The page prints no login, paywall, author handle, or creation stamp (adopted `source_as_of` is the fetch date, per the merged QuantifiedTrader Raff-Channel / Projection-Oscillator lane precedent). The strategy-implementation code block is printed verbatim on the page (backtesting.py shape):

```text
class KeltnerSqueeze(Strategy):
    bb_n = 20; kelt_n = 20; atr_n = 10; mult = 2
    def init(self):
        atr = _atr(self.data.High, self.data.Low, self.data.Close, self.atr_n)
        self.kelt_upper = self.I(lambda: _ema(self.data.Close, self.kelt_n) + self.mult * atr, name="KeltUpper")
        self.sma = self.I(_sma, self.data.Close, self.kelt_n)
    def next(self):
        if self.data.Close[-1] > self.kelt_upper[-2] and not self.position: self.buy()
        elif self.data.Close[-1] < self.sma[-1] and self.position: self.position.close()
```

Code census this cycle over the rendered visible text before the backtest-data loader (scripts/styles stripped): 1 `buy()` / 1 `position.close()` / 0 short/sell-short order calls (the lone `sell` substring is inside `Rus**sell**` in the coverage header) / 0 stop/limit/trailing/time/target/profit calls / 2 indicator registrations (`self.I`) / 0 volume reads by any order-gating line. Helper-name census: `_atr` 1 / `_ema` 1 / `_sma` 1, each exactly at its call site, with zero `def _` definitions printed anywhere — the three helper bodies are unprinted, the same gap shape the merged Raff-Channel and Projection-Oscillator lane records froze via textbook construction. This record cites and normalizes the rule and reproduces no source block beyond the short declarations quoted for gate evidence.

**Facts actually supplied by the source page:** backtested on **daily OHLCV** across major US equity indices and ETFs (S&P 500, NASDAQ Composite, DJI, Russell 2000, +16 more); entry/exit signals carry **no lookahead bias**; **trades execute at the open of the bar following the signal**; performance metrics are computed per symbol; **transaction costs and slippage are not modeled**. Signal prose: squeeze = Bollinger Bands contracting inside Keltner Channels; long on breakout above the upper Keltner band; exit when price falls back below the average. No return, Sharpe, win-rate, or trade-count figure from the source is carried into the derived specification. The page's parameter grid-search section, where available, is not adopted as a parameter source.

**Prose-vs-code mismatches (disclosed, code governs):** (a) the prose advertises a Bollinger-inside-Keltner squeeze gate, but the printed program contains **no** Bollinger/Keltner comparison anywhere — `bb_n = 20` is declared once and never read again, and no order-gating line references any squeeze state. The executable rule is therefore a plain Keltner-upper breakout, never a squeeze-gated system, and this record never claims squeeze detection. (b) The prose says the exit is below "the EMA", but the coded exit leg reads `_sma` (SMA-20). The frozen rule follows the code (`SMA20`), and the prose word is fenced as non-executable. A reviewer must not swap an EMA exit or invent a squeeze gate into this record.

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the source ships equity-universe backtesting.py semantics with no venue/fill/cost leg this record can reuse verbatim. Researcher-declared adaptations are exactly six: (1) market pin **BTCUSDT Binance spot 1d** (long-flat needs no margin-short permission; spot is the minimal realistic venue — the source's equity-index universe is kept separate, never claimed); (2) completed-bar decisions with **next-bar-open market** fills (the source's own stated execution — "trades execute at the open of the bar following the signal" — preserved verbatim); (3) inputs frozen at `kelt_n = 20, atr_n = 10, mult = 2` with the closed-form textbook envelope below (`bb_n` is dead input by code fact — any live use of it is a different, unpinned rule); (4) adopted **60-bar warmup** with pre-warmup bars flat by record rule (structural minimum is index 19 — first full EMA20/SMA20 window — verified this cycle; 60 follows the merged QuantifiedTrader 1d sibling package with conservative margin); (5) house sizing/costs replacing the source's no-cost model (fixed 0.01 BTC, 0.1%/side taker; spot means no funding leg exists — constructive exclusion, never zero-claimed; fixed size is event-neutral for timing under state-independent signals); (6) missing-bar stretches freeze evaluation at the prior target — book and ledger retained across the freeze, evaluation resumes on the next valid bar with no warmup repetition, never backfilled, never forced flat. The fixed-lag breakout entry, the SMA-level exit, the long-only stance, and the no-stop/no-target posture are source-pinned or predeclared; no short leg is invented.

**Immutable derivative identity:** `qtktsq:KeltnerSqueeze-upper20-atr10x2-breakout_SMA20-exit|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001-nofunding|spot1x|nostop-notarget|warmup60|2026-11-05`. Changing any input, envelope construction, comparator, lag, direction, timing, market, risk, cost, sizing, or book state creates a different derivative.

**Pre-write dedup (2026-11-05):** working-tree base is current `main@43030906` (562 root strategy records, READMEs excluded; this file is the 563rd). Content searches for `KeltnerSqueeze`, `keltner-squeeze`, `keltner_squeeze`, and the canonical slug `strategies/keltner` return zero same-source/same-construction records. No open `research/*` PR is this page, author, construction, or signal (17 open PRs enumerated this cycle — #48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708, #725 — the sole Keltner-titled PR, #353 Heracles Keltner-Donchian band-ratio state, is a freqtrade ratio-state + ROI-ladder + stop machine on 4h, fenced in Negative evidence as a different signal object). The pool's three Keltner records and the squeeze/ATR-channel cousins are all fenced as different signal objects (Negative evidence 1–5). No duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

Volatility-envelope breakout timing, long side only. The construction is self-describing: an EMA-centered ATR envelope marks how far price may drift before the move counts as expansion, a close printing above the prior bar's upper envelope holds the long thesis, and the first close back below the trailing average ends it. The page prose claims only this breakout intuition plus an unprinted squeeze narrative — this record adopts none of it beyond the coded comparisons. The equity-index universe and the unmodeled-costs stance are source facts, not this record's venue or economics. No performance figure is carried anywhere.

### Research interpretation

Fixed-lag envelope breakout with average-level exit — a *breakout-in, mean-out* object. Unlike the pool's Donchian cousins (which break raw highest-high/lowest-low extremes — every print is a level the market actually touched), this rule breaks a *manufactured* level (EMA plus two average true ranges) that price may never have printed, so entries key off volatility-normalized displacement rather than realized extremes. Unlike the pool's momentum/slope-gated Keltner cousins (FMZ 481364's 14-bar momentum sign, Forven's ADX floor), this rule carries no regime gate at all — any close above the lagged envelope arms, calm or wild. Unlike SMA-level cousins, the entry rail breathes with ATR while the exit rail (plain SMA20) does not, so the round trip is asymmetric by construction: expansion opens it, average-gravity closes it. The failure mode is plain: a slow grinding climb can hug the envelope without ever printing the strict excess (the planted sustained-down tape arms zero times; the live window still prints 48 entries across 3,306 post-warmup bars with only the SMA print as exit — disclosed, not upgraded).

## Signal

Exact rule as pinned (daily decision on completed `1d` bars; entries/exits next-bar-open market; long-flat single-unit book — any other input, envelope construction, comparator, lag, sizing, fill, or cost is a different, unpinned rule):

- R1 — Measure grid: completed `1d` bars of BTCUSDT spot only. Continuous calendar days; no session template, no holiday skip. Bar time is never read by any order-gating line.
- R2 — Source series: `H[t]`, `L[t]`, `C[t]` are the sole signal inputs (`O[t]` never read by any order-gating line — fills price at opens; notionals reference closes for cost sizing only). No volume, no funding/OI/mark-index read gates on any order; no sentiment/macro/on-chain/cross-venue state. Single timeframe, single asset.
- R3 — Envelope (frozen, researcher-pinned textbook construction for the three unprinted helpers): `EMA20[t]` is the exponential average of closes with `k = 2/21`, seeded by the SMA of the first 20 closes (first finite at index 19); `ATR10[t]` is the Wilder RMA of true ranges seeded by the SMA of the first 10 true ranges; `SMA20[t]` is the plain 20-bar mean of closes (first finite at index 19). `Upper[t] = EMA20[t] + 2.0 · ATR10[t]`. Finite exactly when all trailing inputs are finite (first possible at index 19 — verified this cycle). The seeding convention is part of the pin: any other seed (e.g. first-close seed, SMA-ATR seed) prints a different, unpinned series. `bb_n` is dead input — read nowhere by any order-gating line.
- R4 — Entry (pinned, fixed-lag breakout): if FLAT and `C[t] > Upper[t-1]` (post-warmup) → buy at the next open. The code's `Close[-1] > kelt_upper[-2]` compares the decision bar's close against the *prior* bar's envelope — a one-bar lag that is, if anything, more conservative than a same-bar comparison. A NaN envelope leg never satisfies the edge (comparison is false), so seeding can never smuggle an entry.
- R5 — Exit (pinned, average level): if LONG and `C[t] < SMA20[t]` → close the whole book at the next open. Exact equality on either leg (`C == Upper[t-1]`, `C == SMA20`) neither enters (needs strict `>`) nor exits (needs strict `<`), by the comparators as coded — the planted flat tape exercises the entry-side equality with 0/0.
- R6 — Risk legs (file absence, not invented): stop-loss, take-profit, trailing, time exit, and any second exit are all explicitly disabled — the program ships none, and no prose ships any executable one. The SMA print is the sole exit path.
- R7 — Position state (single deterministic path — no reset, no re-warmup): one 0.01-BTC unit max, long or flat. Safety orders: explicitly none. No cooldown: after any close, the next breakout bar re-enters at its next open (`not self.position` guard preserved — while LONG, breakout bars are no-ops; while FLAT, sub-SMA bars are no-ops). Entries and exits can never co-fire on the same bar in the adverse direction set (entry needs `C > Upper[t-1] ≥ SMA`-region, exit needs `C < SMA20` — jointly satisfiable only in the degenerate `Upper[t-1] < SMA20[t]` inversion, where the program's `if/elif` order resolves entry-first; disclosed, deterministic, exercised by no planted tape this cycle).
- R8 — Warmup: flat until 60 completed `1d` bars (structural minimum is index 19; first decidable edge at index 20 since the entry reads `Upper[t-1]`; 60 follows the merged QuantifiedTrader 1d sibling package with margin — verified this cycle). The 60-bar pin is frozen: a longer warmup prints the same signal series but a different forced-flat-restart book (this cycle's 150-bar restart prints 46/46 vs the pinned 48/48), so it is a different, unpinned claim.
- R9 — Invariant identifier: `qtktsq:KeltnerSqueeze-upper20-atr10x2-breakout_SMA20-exit|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001-nofunding|spot1x|nostop-notarget|warmup60|2026-11-05` (any input, construction, seed, comparator, lag, direction, sizing, fill, risk, or cost change is a different derivative).

## Required data

- Completed `1d` bars of BTCUSDT: `H[t]`/`L[t]` (true-range path inside ATR10) and `C[t]` (EMA/SMA source and both comparisons) are the sole series the formula reads (`O[t]` fills only; notionals reference closes for cost sizing only). No `volume`, no funding-signal, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; the windows read trailing completed bars only, never a second feed).
- Warmup: 60 completed `1d` bars flat by record rule — structural minimum is the 20th completed bar (binding legs: 20-bar EMA/SMA windows, verified finite at index 19 this cycle; first decidable edge at index 20 since the entry reads `Upper[t-1]`). Pre-warmup and any NaN-signal bars are flat/hold by record rule; missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (windows read completed bars including the decision bar only; the entry envelope leg is one bar older still), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance spot, 1x, fixed 0.01 BTC per unit, single-unit book, no compounding. Long side explicitly enabled; short side explicitly disabled (zero short/sell-short order tokens in the printed program). Fills are never conditional on equity or buying power.
- Order timing (source-stated timing preserved verbatim): completed-bar decision with next-bar-open market fills for entries and whole-book closes — the source prose states "trades execute at the open of the bar following the signal", and this record adopts exactly that (the same verified execution primitive as the merged FMZ/QuantifiedTrader lane records; with no stop/limit legs anywhere in the derived machine there is no same-bar TP/SL ordering ambiguity; each bar's outcome is a single deterministic event: hold, open-long, or close-flat, with the documented `if/elif` priority only reachable in the degenerate envelope/average inversion). This record claims no other fill convention: no same-bar-close print, no maker-touch, no intrabar-path-dependent fill.
- Pinned engine path (verified at the pin this cycle): Hummingbot package label `20260920`, VERSION `dev-2.17.0` (local checkout `2dbc844` carries `hummingbot/VERSION` file `2.17.0`, verified live this cycle; `8b0e067e80ab62f10846d518dcb5a8218527ddb3` is an ancestor of the local checkout, verified via `merge-base --is-ancestor` this cycle; code paths verified at the pin this cycle: `async def run_backtesting` in `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py:221`, `def determine_executor_actions` in `hummingbot/strategy/strategy_v2_base.py:747`, `class OrderExecutorSimulator` in `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py:9`, `INTERVALS "1d" = "1d"` in `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py:24`). Prior merged Alpha PR **#414** reports a 902/902 wheel-file byte match and 33-assert representative validation for this source/package path; this Scout did not independently rehash the wheel. A different deployed package must be revalidated. A strategy-specific, not-yet-implemented controller must compute the trailing envelope-breakout/SMA-exit state pin via `CreateExecutorAction(OrderExecutorConfig)` market legs; the generic executor does not calculate the strategy. The precomputable envelope series plus breakout/level state machine is a plain signal series, not a new execution primitive; no new data requirement, no representative-capability validation owed.
- Stop/limit modeling: none — the derived spec carries zero stop/limit/trailing legs by record rule. No hidden Hummingbot stop-order defaults are relied upon, and with no stop/limit legs there is no same-bar TP/SL ordering ambiguity.
- Sizing/capital/costs: the source models no costs (recorded as the source's, never adopted). Explicit house overlay: single-unit frame, 0.1% taker fee per filled side, slippage unmodeled by declaration; fixed size is event-neutral for timing under state-independent signals. Exchange facts re-verified live this cycle via `api/v3/exchangeInfo`: `BTCUSDT`, `TRADING`, `tickSize 0.01`, min-qty/step 0.00001/0.00001, min-notional 5.0 (`NOTIONAL`). The fixed 0.01 BTC (≈774.54 USDT at the cycle's last completed close 77,453.86 on 2026-11-03, above the 5.0 min-notional and an exact multiple of the 0.00001 step). Spot venue means no funding leg exists — constructive exclusion, never modeled-or-realized funding.
- Concurrency: at most one single-asset engine position at any time; the SMA print ends it (re-entry earliest next signal). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no hedge-mode requirement by construction.

## Evidence

### Source-reported

With exact provenance (page fetched live 2026-11-05, 43,001 bytes, SHA-256 `489824bfb591abf3548037bb29b11e2f3068a437878437db495115794da18882`; implementation block `class KeltnerSqueeze(Strategy)` with `bb_n = 20; kelt_n = 20; atr_n = 10; mult = 2`, `_atr(High, Low, Close, atr_n)` + `_ema(Close, kelt_n)` upper registration and `_sma(Close, kelt_n)` registration (all three helper bodies unprinted — each name occurs once, at its call site; zero `def` prints), `Close[-1] > kelt_upper[-2] and not position → buy()`, `Close[-1] < sma[-1] and position → position.close()`): the frozen inputs; the High/Low/Close indicator reads; the fixed-lag-breakout-entry / SMA-level-exit polarity; the `not self.position` single-unit guard; the long-only order set (zero short/stop/limit/time calls in the order path — the lone `sell` substring is inside `Russell`); the source's daily-OHLCV frame, no-lookahead statement, next-bar-open execution, unmodeled-costs stance, and equity-index universe (S&P 500, NASDAQ Composite, DJI, Russell 2000, +16 more). This record claims no source-reported performance number as its own — no return, Sharpe, win rate, or trade count is carried into the derived specification — and no reproduced performance exists.

### Independently reproduced

**None.** No strategy backtest, event-level Qlib/Hummingbot parity, wheel rehash, deployment or profitability experiment occurred. Pinned engine source inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifacts this run are researcher self-checks of the predicate/estimator/state pipeline (textbook EMA20-SMA-seeded + Wilder ATR10 + SMA20 envelope, 60-bar warmup, fixed-lag-breakout / SMA-level next-open single-unit long-flat machine), run in scratch (never committed): logic verification only, not a backtest, not parity.

**Planted-tape verification (this cycle, deterministic, double-run identical):** TAPE-flat (dead-constant 170-bar tape) prints 0 entries / 0 exits ending FLAT — the envelope collapses onto price (ATR 0) and the strict excess never arms, as pinned; TAPE-up (sustained +1%/day compounding 170-bar tape) prints 1 entry / 0 exits ending LONG — the steady climb eventually exceeds the lagged envelope once and never prints the SMA exit, as pinned (disclosed behavior, not patched); TAPE-down (sustained −1%/day 170-bar tape) prints 0 entries / 0 exits ending FLAT — the close never exceeds the lagged envelope through the grind, as pinned; TAPE-volregime (deterministic 170-bar ±0.2%-then-±2% alternation tape) prints 6 entries / 5 exits ending LONG — both transition paths are exercised, as pinned. (TAPE-flat and TAPE-down share the empty-series digest by construction — both print no events.)

**Live-exchange microstructure probes (this cycle, Binance spot 1d klines, 3,366 completed bars 2017-08-17→2026-11-03, last close 77,453.86; the in-progress 2026-11-04/05 bars excluded):** 48 post-warmup breakout bars drive 48 entries / 48 exits ending FLAT (non-degenerate, non-buy-and-hold). Two independent runs produce identical digests (event-series digest `1f8682b9`). Admission is engineering capability, never an event-rate or profitability claim.

### Negative evidence

1. Momentum-gate fence: pool `keltner-momentum-breakout-gated` (FMZ 481364) is two-sided with a 14-bar momentum-sign gate, 1.5×ATR20 envelope, and mid-EMA-or-momentum-flip exits. This record has no momentum read anywhere, is long-flat only, uses 2.0×ATR10 with a fixed one-bar envelope lag, and exits solely on the SMA20 level. Different signal object, different inputs, never a twin.
2. ADX-gate fence: pool `forven-keltner-adx-gated-breakout` requires an ADX regime floor on 1h bars. This record has no ADX read anywhere and no regime gate — any lagged-envelope excess arms. Different signal object, never a twin.
3. Pullback-reclaim fence: pool `eterna-keltner-20-10-2p0-pullback-reclaim` trades a reclaim trigger (re-cross after pullback), two-sided, on 4h. This record trades a fresh lagged-envelope breakout edge with an SMA-level exit, long-flat, on 1d. Different trigger, direction, and exit, never a twin.
4. True-squeeze fence: pool `sqzmom-lb-squeeze-release-ema100` and open PR #353 (Heracles Keltner-Donchian band-ratio state with ROI ladder + stop) both trade genuine squeeze/ratio states with their own exit machinery. This record's printed program contains no squeeze gate at all (`bb_n` dead by code fact) — despite the page's name and prose, the executable rule is a plain envelope breakout. A reviewer must neither demand a squeeze gate here nor treat the name similarity as mechanism similarity.
5. ATR-channel-cousin fence: pool `forven-atr-breakout-channel`, `starc-band-breakout-latched`, `t3-tillson-channel-breakout`, and the Donchian family (raw highest-high/lowest-low extremes, e.g. `forven-naked-donchian-20-breakout`) all break levels built without an EMA-centered ATR envelope, most with different exits and gates. This record's rail is manufactured (`EMA20 + 2·ATR10`), never a touched extreme. Different construction, never a twin.
6. Prose-swap fence: a record exiting below an EMA (the prose word), adding a Bollinger-inside-Keltner squeeze gate (the prose narrative), using `bb_n`, or comparing against the same-bar envelope (dropping the `[-2]` lag) prints a different, unpinned event set; a reviewer must not swap any of them in.
7. Exact-equality fence: `C == Upper[t-1]` never enters and `C == SMA20` never exits by the strict comparators as coded (the planted TAPE-flat exercises the entry-side equality with 0/0). A record arming on touch prints a different, unpinned event set.
8. NaN/seed fence: any non-finite window print holds with no signal and no close; the SMA-seeded EMA / SMA-seeded Wilder ATR conventions are part of the pin. Interpolating, reseeding, or backfilling is a different, unpinned rule.
9. Single-print-twin fence: no twin is admitted — any input change (e.g. 20→10 Keltner window, 2.0→1.5 multiplier), any dropped lag, any gated or two-sided variant, any other frame, fill, venue, or book is a different, unpinned rule.
10. Warmup-identity fence, admitted plainly: the 150-bar forced-flat restart prints 46/46 events vs 48/48 at the pinned 60 — the same signal series but a different book. Warmup 60 is frozen, not exemplary; any other warmup is a different, unpinned claim.
11. Number silence fenced: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from any source is adopted anywhere, and any dispute over exact magnitudes is decided against this record, never patched by inference.
12. Version fence: this record follows the QuantifiedTrader page as fetched 2026-11-05 (no printed creation stamp; fetch-date pin). If the page is ever edited, this record does not move with it.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: inputs `20/10/2.0` / textbook envelope construction + seeds / lagged-breakout-entry / SMA-level-exit / long-flat book / no-stop-no-target posture / `1d` BTCUSDT spot / next-open fills / 0.01 BTC / 0.1% costs / 60-bar warmup are frozen.

- F1 — Envelope relevance: a Donchian-20 twin (enter on close above the trailing 20-bar highest high / exit below the 20-bar lowest low — same rest) must not improve net expectancy; fail ⇒ the EMA+ATR manufactured rail adds nothing over realized extremes, and the record is a breakout label rather than an envelope edge.
- F2 — Lag relevance: a same-bar twin (enter on `C[t] > Upper[t]` — same rest) must not improve net expectancy; fail ⇒ the fixed one-bar envelope lag adds nothing over the contemporaneous rail, and the record's lag is decorative.
- F3 — Exit relevance: an envelope-midline twin (exit on close below `EMA20[t]` instead of `SMA20[t]` — same rest) must not improve net expectancy; fail ⇒ the SMA-level exit adds nothing over the envelope's own midline, and the record's exit rail is decorative.
- F4 — Warmup relevance: the pinned 60 print and a 60-vs-60 re-run must print the identical event set (determinism check — digest `1f8682b9` is the tripwire); fail ⇒ nondeterminism or seed leakage past the declared warmup.

## Crypto portability

Pinned to BTCUSDT Binance spot under the house overlay (declared port of an equity-index-headed backtesting.py program). The rule reads completed daily bars only, so no pit-session, gap, roll, split/dividend-adjustment, or corporate-action logic ports (equity-calendar effects are non-issues on spot — disclosed, not modeled). The composite is unit-free in rail-ratio terms (no absolute-price threshold anywhere), so unlike price-level systems the rule ports across venues without re-scaling — yet envelope-breakout timing on crypto microstructure (24/7 bars, stablecoin-quoted prints, volatility-regime shifts the source never traded) fires at a cadence the source never measured (48 entries across 3,306 post-warmup bars here), disclosed without re-tuning. The rule is long-flat, so a spot deployment expresses the full machine with no short permission — a two-sided or perpetual variant would be a different, unpinned claim (this record's gate-5 evidence is the spot path only; the source's equity universe is provenance, not execution). No warmup history beyond 60 `1d` bars is consumed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Gate-free by design: with no squeeze, momentum, or regime gate in the printed program, any lagged-envelope excess arms — including whipsaw crossings in range-bound tapes (the planted vol-regime tape prints 6 entries across 170 bars — disclosed, not upgraded).
- Prose/code residual: the advertised squeeze gate and the EMA-exit word exist only in prose, never in the program; this record follows the program and fences the prose as non-executable (a reviewer repairs from code facts only).
- Single-venue port residual: backtesting.py close/open arithmetic vs Binance spot execution (prints, fees, open-definition across 24/7 sessions, equity-vs-crypto regime differences) is unclaimed, disclosed.
- Next-open latency idealization: signal cadence on the decision close print while fills land on the next open; any live gap between the two differs by construction — disclosed, research-only (this convention is the source's own stated execution, preserved verbatim).
- Degenerate-inversion residual: in the theoretical `Upper[t-1] < SMA20[t]` inversion, entry and exit could co-fire and the `if/elif` order resolves entry-first — deterministic by code order, exercised by no tape this cycle, disclosed.
- No-authorship-page residual: the page prints no handle, license, or creation stamp; provenance rests on the QuantifiedTrader URL/slug, printed names, page hash, and fetch date — disclosed.
- Performance evidence is absent: nothing here is calibrated, fitted, or tuned to any backtest (the `20/10/2.0` defaults are the source's, never re-run here; the page's own grid-search section, where available, is not adopted as a parameter source).
- Author scope: the page ships exploratory research with an explicit not-investment-advice disclaimer, not a vetted trading system — this record is research-only and claims no live suitability.

## Implementation status

`not-implemented`: no dedicated controller, Qlib executable recipe or deployment artifact was created. PASS is a bounded research-expressibility proposal, not a claim of already runnable materialization. A selected strategy may later need the minimal strategy-specific implementation without a second admission flag.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review must independently inspect this exact PR head, remediate only primary-source-verifiable facts, then PASS exact-head merge or NOT_LOSSLESS close. Scout does not approve, merge, close, trade, backtest or deploy.

## Related Wiki records

None asserted.

## Sources

- Primary page + pin: https://quantifiedtrader.com/backtest/strategies/keltner-squeeze/ (`Keltner Squeeze`; page fetched live 2026-11-05, 43,001 bytes, SHA-256 `489824bfb591abf3548037bb29b11e2f3068a437878437db495115794da18882`; implementation block `class KeltnerSqueeze(Strategy)` with `bb_n = 20; kelt_n = 20; atr_n = 10; mult = 2`, `_atr(High, Low, Close, atr_n)` + `_ema(Close, kelt_n)` upper registration and `_sma(Close, kelt_n)` registration (all three helper bodies unprinted — each name occurs once, at its call site; zero `def` prints), `Close[-1] > kelt_upper[-2] and not position → buy()`, `Close[-1] < sma[-1] and position → position.close()`; zero short/stop/limit/trailing/time/target/profit order calls in the order path; daily OHLCV frame, no-lookahead statement, next-bar-open execution, unmodeled costs, equity-index universe S&P 500 / NASDAQ / DJI / Russell 2000 +16)
- Lane precedent (different mechanism, unmerged-proof never claimed): `quantifiedtrader-raff-channel-midline-level-long-flat-btcusdt-1d-2026-11-04.md` and `quantifiedtrader-projection-oscillator-zero-cross-long-flat-btcusdt-1d-2026-11-04.md` (unprinted-helper textbook-freeze derivation pattern with 60-bar warmup)
- Nearest pool lineages (different mechanisms, unmerged-proof never claimed): `keltner-momentum-breakout-gated-btcusdt-1d-2026-10-09.md` (momentum-gated two-sided); `forven-keltner-adx-gated-breakout-long-flat-btcusdt-1h-2026-10-19.md` (ADX-gated); `eterna-keltner-20-10-2p0-pullback-reclaim-two-sided-btcusdt-4h-2026-10-20.md` (pullback-reclaim two-sided); `sqzmom-lb-squeeze-release-ema100-two-sided-btcusdt-1d-2026-10-09.md` (true squeeze-release); open PR #353 Heracles Keltner-Donchian band-ratio state (ratio-state + ROI ladder + stop, 4h, freqtrade)
- Exchange verification: Binance spot `api/v3/exchangeInfo` (`BTCUSDT`, `TRADING`, `tickSize 0.01`, min-qty/step 0.00001/0.00001, min-notional 5.0 via `NOTIONAL`) plus `api/v3/klines` 1d probes (3,366 completed bars 2017-08-17→2026-11-03, 48 post-warmup breakout bars → 48 entries / 48 exits ending FLAT, event digest `1f8682b9` double-run identical; 150-bar restart prints 46/46 — warmup-identity fence), fetched live 2026-11-05
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently merged pinned package/source evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
