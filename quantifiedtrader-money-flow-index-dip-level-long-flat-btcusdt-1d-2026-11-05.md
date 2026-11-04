---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: QuantifiedTrader Money Flow Index dip-level long-flat on BTCUSDT 1d bars
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
  - https://quantifiedtrader.com/backtest/strategies/money-flow-index/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# QuantifiedTrader Money Flow Index dip-level long-flat on BTCUSDT 1d bars

## Provenance

**Primary source (fetched live over HTTPS this cycle):** QuantifiedTrader public strategy-library page `https://quantifiedtrader.com/backtest/strategies/money-flow-index/` (`Money Flow Index`), fetched 2026-11-05 as a 42,620-byte page (SHA-256 `e3227373b4070824d9455022803d8a66e270d80e42cafe4f49dadec0db76fd9c`). The page prints no login, paywall, author handle, or creation stamp (adopted `source_as_of` is the fetch date, per the merged QuantifiedTrader Raff-Channel / Projection-Oscillator / Keltner-Squeeze / ATR-Bands / BB-Width-Squeeze lane precedent). The strategy-implementation code block is printed verbatim on the page (backtesting.py shape):

```text
class MoneyFlowIndex(Strategy):
    n = 14
    def init(self):
        self.mfi = self.I(_mfi, self.data.High, self.data.Low, self.data.Close, self.data.Volume, self.n)
    def next(self):
        if self.mfi[-1] < 20 and not self.position: self.buy()
        elif self.mfi[-1] > 80 and self.position: self.position.close()
```

Code census this cycle over the rendered visible text (scripts/styles stripped): 1 `buy()` / 1 `position.close()` / 0 short/sell-short order calls / 0 stop/limit/trailing/time/target/profit calls in the order path / 1 indicator registration (`self.I`) / 0 `crossover` calls. (`stop`/`trailing`/`take_profit` tokens never occur in visible text; the single `limit` token sits inside the legal boilerplate "not limited to accuracy" — fenced, not adopted.) Helper-name census: `_mfi` 1, exactly at its call site, with zero `def _` definitions printed anywhere — the helper body is unprinted, the same gap shape the merged Raff-Channel / Projection-Oscillator / Keltner-Squeeze / ATR-Bands / BB-Width-Squeeze lane records froze via textbook construction. `def ` occurs exactly twice (`init`, `next`). This record cites and normalizes the rule and reproduces no source block beyond the short declarations quoted for gate evidence.

**Facts actually supplied by the source page:** backtested on **daily OHLCV** across major US equity indices and ETFs; entry/exit signals carry **no lookahead bias**; **trades execute at the open of the bar following the signal**; performance metrics are computed per symbol; **transaction costs and slippage are not modeled**. Signal prose: Money Flow Index is a volume-weighted RSI; enters long when MFI drops below 20 (oversold with volume confirmation); exits when MFI rises above 80; volume weighting makes it more reliable than price-only oscillators. No return, Sharpe, win-rate, or trade-count figure from the source is carried into the derived specification. The page's parameter grid-search section, where available, is not adopted as a parameter source.

**Prose-vs-code fence (code governs):** the prose says "drops below 20" but the program tests the level `mfi[-1] < 20`, not a cross edge — a bar parked under 20 for weeks still satisfies the entry leg; only the `not self.position` guard stops re-entry. The prose says "rises above 80" but the program tests the level `mfi[-1] > 80` — any overbought bar ends the position, not a cross-down edge. Both level loosenings are quoted as printed and the executable rule follows the program, never the prose.

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the source ships equity-universe backtesting.py semantics with no venue/fill/cost leg this record can reuse verbatim. Researcher-declared adaptations are exactly six: (1) market pin **BTCUSDT Binance spot 1d** (long-flat needs no margin-short permission; spot is the minimal realistic venue — the source's equity-index universe is kept separate, never claimed); (2) completed-bar decisions with **next-bar-open market** fills (the source's own stated execution — "trades execute at the open of the bar following the signal" — preserved verbatim); (3) input frozen at `n = 14` with the closed-form textbook MFI construction below (typical-price money-flow ratio over 14 periods, strict direction predicates, `1e-10` zero-division floor — the pool's own `forven-mfi-threshold-cross` record pins this exact arithmetic, reused here, disclosed as the researcher freeze for the unprinted `_mfi`); (4) adopted **100-bar warmup** with pre-warmup bars flat by record rule (structural minimum is index 14 — first finite MFI print — verified this cycle; 100 carries margin); (5) house sizing/costs replacing the source's no-cost model (fixed 0.01 BTC, 0.1%/side taker; spot means no funding leg exists — constructive exclusion, never zero-claimed; fixed size is event-neutral for timing under state-independent signals); (6) missing-bar stretches freeze evaluation at the prior target — book and ledger retained across the freeze, evaluation resumes on the next valid bar with no warmup repetition, never backfilled, never forced flat. The sub-20 dip entry, the sup-80 exit, the long-only stance, and the no-stop/no-target posture are source-pinned or predeclared; no short leg is invented.

**Immutable derivative identity:** `qtmfi:MoneyFlowIndex-mfi14-lvl20-80|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001-nofunding|spot1x|nostop-notarget|warmup100|2026-11-05`. Changing any input, MFI construction, threshold, comparator, direction, timing, market, risk, cost, sizing, or book state creates a different derivative.

**Pre-write dedup (2026-11-05):** working-tree base is current `main@6c798f57` (565 root strategy records, READMEs excluded; this file is the 566th). Content searches for the canonical slug `strategies/money-flow-index`, the class name `MoneyFlowIndex`, and the exact helper token `_mfi` return zero same-source/same-construction records (the `_mfi` hits are cousin records only: `forven-mfi-threshold-cross` reclaim-edge, `mfi-threshold-divergence-reversal`, `freqtrade-bandtastic` combo — all fenced in Negative evidence, none a sub-20-level/​sup-80-level machine). No open `research/*` PR is this page, author, construction, or signal (17 open PRs enumerated this cycle — #48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708, #725 — none is an MFI, money-flow, or QuantifiedTrader-oscillator machine). No duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

Buy-the-dip with volume confirmation, long side only. The construction is self-describing: Money Flow Index weights price movement by volume, so a sub-20 print means the recent tape fell on heavy volume (capitulation-like); a sup-80 print means the recovery rallied on heavy volume (saturation-like). The position rides the dip-to-saturation traverse and ends it on arrival. The equity-index universe and the unmodeled-costs stance are source facts, not this record's venue or economics. No performance figure is carried anywhere.

### Research interpretation

Dip-level/volume-confirmed object — the patient sibling of the pool's reclaim-edge MFI record (which buys the recovery *after* MFI climbs back through 20) and the structural cousin of the merged ATR-Bands lower-touch record (which buys every volatility-rail touch with no oscillator confirmation at all). Unlike zero-line oscillators (ROC-sign, CMF-sign) both legs here are fixed-threshold levels with a wide 20–80 hold band between them, so the machine sits through mid-range chop that would flip-flop a zero-line follower. Unlike the pool's MFI combos (quad-confluence, divergence, bandtastic, ATR-trailing) there is no second gate, no divergence read, and no trailing leg — one series, two levels, one book. The failure mode is plain and verified this cycle: in a zero-variance tape the ratio pins at exactly 0.0 (both flows empty, floor engaged) so the machine buys the first post-warmup bar and holds forever (planted dead-flat tape prints 1 entry / 0 exits ending LONG — disclosed, not patched); a sustained ramp never prints sub-20 and never participates (planted sustained-up tape arms zero times — disclosed); a sustained bleed never prints sup-80 so the dip-buy holds its falling knife to the tape end (planted sustained-down tape prints 1 entry / 0 exits ending LONG — disclosed, the structural twin of the ATR-Bands bleed-hold).

## Signal

Exact rule as pinned (daily decision on completed `1d` bars; entries/exits next-bar-open market; long-flat single-unit book — any other input, MFI construction, threshold, sizing, fill, or cost is a different, unpinned rule):

- R1 — Measure grid: completed `1d` bars of BTCUSDT spot only. Continuous calendar days; no session template, no holiday skip. Bar time is never read by any order-gating line.
- R2 — Source series: `H[t]`, `L[t]`, `C[t]`, `V[t]` feed the MFI construction only (`O[t]` fills only). No funding/OI/mark-index read gates on any order; no sentiment/macro/on-chain/cross-venue state. Single timeframe, single asset.
- R3 — MFI stack (frozen, researcher-pinned textbook construction for the unprinted helper, reusing the pool's `forven-mfi-threshold-cross` arithmetic verbatim): `TP[t] = (H[t]+L[t]+C[t])/3`; `RMF[t] = TP[t]·V[t]`; `POS[t] = Σ RMF[i]` over `i ∈ t-13..t` with `TP[i] > TP[i-1]`; `NEG[t] = Σ RMF[i]` over `i ∈ t-13..t` with `TP[i] < TP[i-1]` (flat-TP bars contribute to neither sum — strict predicates); `MFI[t] = 100 − 100/(1 + POS[t]/max(NEG[t], 1e-10))` (first finite at index 14 — verified this cycle). Finite exactly when all trailing inputs are finite. Any other flow window, direction predicate, floor, or scaling prints a different, unpinned series.
- R4 — Entry (pinned, sub-20 dip level): if FLAT and `MFI[t] < 20` (post-warmup) → buy at the next open. A touch of the boundary (`== 20`) fails the strict leg and fires nothing.
- R5 — Exit (pinned, sup-80 saturation level): if LONG and `MFI[t] > 80` → close the whole book at the next open. The exit is a level hold, not a cross — it fires on any overbought bar, including bars that never entered. The program ships no NaN guard, but a non-finite print never satisfies any strict comparison, so seeding can never smuggle an entry or an exit; pre-warmup and NaN-signal bars are flat/hold by record rule.
- R6 — Risk legs (file absence, not invented): stop-loss, take-profit, trailing, time exit, and any second exit are all explicitly disabled — the program ships none, and no prose ships any executable one. The sup-80 print is the sole exit path.
- R7 — Position state (single deterministic path — no reset, no re-warmup): one 0.01-BTC unit max, long or flat. Safety orders: explicitly none. No cooldown: after any close, the next sub-20 bar re-enters at its next open (`not self.position` guard preserved — while LONG, qualifying dip bars are no-ops; while FLAT, overbought bars are no-ops). Entry and exit can never co-fire (`MFI < 20` vs `MFI > 80` are jointly unsatisfiable) — no tie-break pin is required. The degenerate zero-variance window (`POS == NEG == 0`) pins `MFI == 0.0` and arms the entry leg — verified on planted tape this cycle (1/0 ending LONG), fenced by arithmetic, disclosed, not patched.
- R8 — Warmup: flat until 100 completed `1d` bars (structural minimum is index 14; 100 carries margin — verified this cycle). The 100-bar pin is frozen: any other warmup is a different, unpinned claim.
- R9 — Invariant identifier: `qtmfi:MoneyFlowIndex-mfi14-lvl20-80|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001-nofunding|spot1x|nostop-notarget|warmup100|2026-11-05` (any input, construction, threshold, comparator, direction, sizing, fill, risk, or cost change is a different derivative).

## Required data

- Completed `1d` bars of BTCUSDT: `H[t]`/`L[t]`/`C[t]`/`V[t]` feed the MFI construction (typical price, flow direction, flow magnitude). `O[t]` fills only. Base-asset volume prints come from the same spot kline payload — no second feed. No `funding-signal`, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; the window reads trailing completed bars only, never a second feed).
- Warmup: 100 completed `1d` bars flat by record rule — structural minimum is index 14 (binding leg: 14-period flow window needing one prior typical price, verified first-finite at index 14 this cycle). Pre-warmup and any NaN-signal bars are flat/hold by record rule; missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (window reads completed bars including the decision bar only — same-bar comparison, no lag, no negative shift), no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance spot, 1x, fixed 0.01 BTC per unit, single-unit book, no compounding. Long side explicitly enabled; short side explicitly disabled (zero short/sell-short order tokens in the printed program). Fills are never conditional on equity or buying power.
- Order timing (source-stated timing preserved verbatim): completed-bar decision with next-bar-open market fills for entries and whole-book closes — the source prose states "trades execute at the open of the bar following the signal", and this record adopts exactly that (the same verified execution primitive as the merged FMZ/QuantifiedTrader lane records; with no stop/limit legs anywhere in the derived machine there is no same-bar TP/SL ordering ambiguity; each bar's outcome is a single deterministic event: hold, open-long, or close-flat, and R7 proves the two legs can never co-fire). This record claims no other fill convention: no same-bar-close print, no maker-touch, no intrabar-path-dependent fill.
- Pinned engine path (verified at the pin this cycle): Hummingbot package label `20260920`, VERSION `dev-2.17.0` (local checkout `2dbc844` carries `hummingbot/VERSION` file `2.17.0`, verified live this cycle; `8b0e067e80ab62f10846d518dcb5a8218527ddb3` is an ancestor of the local checkout, verified via `merge-base --is-ancestor` this cycle; code paths verified at the pin this cycle: `async def run_backtesting` in `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py:221`, `def determine_executor_actions` in `hummingbot/strategy/strategy_v2_base.py:747`, `class OrderExecutorSimulator` in `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py:9`, `INTERVALS "1d" = "1d"` in `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py:24`). Prior merged Alpha PR **#414** reports a 902/902 wheel-file byte match and 33-assert representative validation for this source/package path; this Scout did not independently rehash the wheel. A different deployed package must be revalidated. A strategy-specific, not-yet-implemented controller must compute the trailing MFI pin via `CreateExecutorAction(OrderExecutorConfig)` market legs; the generic executor does not calculate the strategy. The precomputable MFI series plus threshold state machine is a plain signal series, not a new execution primitive; no new data requirement, no representative-capability validation owed.
- Stop/limit modeling: none — the derived spec carries zero stop/limit/trailing legs by record rule. No hidden Hummingbot stop-order defaults are relied upon, and with no stop/limit legs there is no same-bar TP/SL ordering ambiguity.
- Sizing/capital/costs: the source models no costs (recorded as the source's, never adopted). Explicit house overlay: single-unit frame, 0.1% taker fee per filled side, slippage unmodeled by declaration; fixed size is event-neutral for timing under state-independent signals. Exchange facts re-verified live this cycle via `api/v3/exchangeInfo`: `BTCUSDT`, `TRADING`, `tickSize 0.01`, min-qty/step 0.00001/0.00001, min-notional 5.0 (`NOTIONAL`). The fixed 0.01 BTC (≈802.25 USDT at the cycle's 24hr last price 80,224.51, above the 5.0 min-notional and an exact multiple of the 0.00001 step). Spot venue means no funding leg exists — constructive exclusion, never modeled-or-realized funding.
- Concurrency: at most one single-asset engine position at any time; the sup-80 print ends it (re-entry earliest next signal). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no hedge-mode requirement by construction.

## Evidence

### Source-reported

With exact provenance (page fetched live 2026-11-05, 42,620 bytes, SHA-256 `e3227373b4070824d9455022803d8a66e270d80e42cafe4f49dadec0db76fd9c`; implementation block `class MoneyFlowIndex(Strategy)` with `n = 14`, `_mfi(High, Low, Close, Volume, n)` single call (helper body unprinted — the name occurs once, at its call site; zero `def` prints beyond `init`/`next`), single `self.I` registration, `mfi[-1] < 20 and not position → buy()`, `mfi[-1] > 80 and position → position.close()`): the frozen input; the HLCV reads; the dip-level/saturation-level polarity with strict comparators; the `not self.position` single-unit guard; the long-only order set (zero short/stop/limit/trailing/time calls in the order path); the source's daily-OHLCV frame, no-lookahead statement, next-bar-open execution, unmodeled-costs stance, and equity-index universe. This record claims no source-reported performance number as its own — no return, Sharpe, win rate, or trade count is carried into the derived specification — and no reproduced performance exists.

### Independently reproduced

**None.** No strategy backtest, event-level Qlib/Hummingbot parity, wheel rehash, deployment or profitability experiment occurred. Pinned engine source inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifacts this run are researcher self-checks of the predicate/estimator/state pipeline (textbook MFI14 + 20/80 levels + 100-bar warmup, next-open single-unit long-flat machine), run in scratch (never committed): logic verification only, not a backtest, not parity.

**Planted-tape verification (this cycle, deterministic):** TAPE-flat (dead-constant 170-bar tape with 0.05% wicks) prints 1 entry / 0 exits ending LONG — the zero-variance window pins MFI at exactly 0.0 so the machine buys the first post-warmup bar and holds forever, as pinned (disclosed buy-and-hold degeneration, not patched); TAPE-up (sustained +1%/day compounding 170-bar tape) prints 0 entries / 0 exits ending FLAT — the ramp never prints sub-20, as pinned (disclosed non-participation, not patched); TAPE-down (sustained −1%/day 170-bar tape) prints 1 entry / 0 exits ending LONG — the bleed never prints sup-80 so the dip-buy holds its falling knife to the tape end, as pinned (disclosed, not patched — the structural twin of the ATR-Bands bleed-hold); TAPE-drift-dip-rip (deterministic 260-bar drift/dip/rip tape) prints 1 entry / 1 exit ending FLAT (entry t=121 at MFI 15.9 mid-dip, exit t=160 at MFI 80.2 on the rip — the full round trip is exercised, as pinned).

**Live-exchange microstructure probes (this cycle, Binance spot 1d klines, 3,366 completed bars 2017-08-17→2026-11-03; the in-progress 2026-11-04 bar excluded):** 12 post-warmup dip-to-saturation traverses drive 12 entries / 12 exits ending FLAT (non-degenerate, non-buy-and-hold; 88 sub-20 bars and 194 sup-80 bars in range). Two independent runs produce identical digests (event-series digest `644c4058`). Admission is engineering capability, never an event-rate or profitability claim.

## Negative evidence

1. Reclaim-edge fence: pool `forven-mfi-threshold-cross` (MFI14 cross-up-through-20 reclaim entry, cross-down-through-80 exit, 1h) buys the recovery and sells the fade — this record buys the dip (`< 20` level) and sells the arrival (`> 80` level). Different entry bars, different exit bars, different horizon — never a twin.
2. Trailing/divergence fence: pool `alphatrend-mfi-atr-trailing-reversal` (MFI gate plus an ATR-trailing exit, 4h) and `mfi-threshold-divergence-reversal` (MFI-threshold plus divergence read, two-sided) both carry legs this record never tests — no trailing, no divergence anywhere in the pinned rule — never a twin.
3. Confluence fence: pool `fmz-482880-rsi-bb-imi-mfi-quad-confluence`, `freqtrade-bandtastic`, `freqtrade-ccistrategy`, `freqtrade-strategy003`, `tradingview-blitzalgo-displaced-donchian-decycler60-mfi14`, `tradingview-softkill21-psar-cmf20` and `percent-b-mfi-dual-thrust-cross` all gate MFI inside multi-indicator stacks this record never builds — one series, two levels here — never a twin.
4. Zero-line-oscillator fence: pool `roc-sign-state`, `forven-roc-zero-cross`, `freqtrade-technical-cmf-sign-state` and `cmf-velocity-zero-cross` command on zero-line state that always holds one side; this record's 20–80 hold band commands nothing across mid-range chop. Different trigger object — never a twin.
5. Band-touch fence: pool `bollinger-band-breakout-long-midline-exit` (upper-band penetration entry, midline exit), the just-merged `quantifiedtrader-atr-bands` (lower-rail touch, midline exit) and `quantifiedtrader-bb-width-squeeze` (width-gate plus average-state) trade price rails, not a volume-weighted oscillator — no shared series anywhere — never a twin.
6. Single-print-twin fence: no twin is admitted — any input change (e.g. 14→10 window, 20/80→30/70 thresholds), any reclaim-edge or cross-flavored variant, any gated, bracketed, or two-sided variant, any other flow construction, frame, fill, venue, or book is a different, unpinned rule.
7. NaN/seed fence: any non-finite MFI print holds with no signal and no close (language-false comparisons, no guard invented); the typical-price/strict-direction/`1e-10`-floor conventions are part of the pin. Interpolating, reseeding, or backfilling is a different, unpinned rule.
8. Warmup-identity fence, admitted plainly: the pin is 100 completed bars (structural minimum index 14); any other warmup remains a different, unpinned claim even where it prints the same book.
9. Number silence fenced: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from any source is adopted anywhere, and any dispute over exact magnitudes is decided against this record, never patched by inference.
10. Version fence: this record follows the QuantifiedTrader page as fetched 2026-11-05 (no printed creation stamp; fetch-date pin). If the page is ever edited, this record does not move with it.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: input `14` / textbook MFI construction + strict direction + `1e-10` floor / sub-20 dip entry / sup-80 saturation exit / long-flat book / no-stop-no-target posture / `1d` BTCUSDT spot / next-open fills / 0.01 BTC / 0.1% costs / 100-bar warmup are frozen.

- F1 — Dip-vs-reclaim: a reclaim-edge twin (enter only on a fresh `MFI[t-1] <= 20` → `MFI[t] > 20` cross — same rest) must not improve net expectancy; fail ⇒ the dip-level entry adds nothing over buying the recovery, and the record is a threshold label on the pool's existing reclaim machine.
- F2 — Exit relevance: a midline-exit twin (exit on `MFI[t] > 50` — same rest) must not improve net expectancy; fail ⇒ the sup-80 saturation exit adds nothing over a midline exit, and the record's full-traverse hold is decorative.
- F3 — Exit-shape relevance: a cross-down twin (exit only on a fresh `MFI[t-1] >= 80` → `MFI[t] < 80` cross — same rest) must not improve net expectancy; fail ⇒ the level-hold exit adds nothing over an edge exit, and the record's always-armed exit is decorative.
- F4 — Warmup relevance: the pinned 100 print and a 100-vs-100 re-run must print the identical event set (determinism check — digest `644c4058` is the tripwire); fail ⇒ nondeterminism or seed leakage past the declared warmup.

## Crypto portability

Pinned to BTCUSDT Binance spot under the house overlay (declared port of an equity-index-headed backtesting.py program). The rule reads completed daily HLCV only, so no pit-session, gap, roll, split/dividend-adjustment, or corporate-action logic ports (equity-calendar effects are non-issues on spot — disclosed, not modeled). Base-asset volume prints arrive in the same spot kline payload as HLC — no second feed, no cross-venue sync — yet equity-vs-crypto volume comparability (24/7 bars, stablecoin-quoted prints, cascade dynamics the source never traded) is unclaimed and disclosed without re-tuning; the rule fires at a cadence the source never measured (12 traverses across 3,266 post-warmup bars here), disclosed. The rule is long-flat, so a spot deployment expresses the full machine with no short permission — a two-sided or perpetual variant would be a different, unpinned claim (this record's gate-5 evidence is the spot path only; the source's equity universe is provenance, not execution). No warmup history beyond 100 `1d` bars is consumed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Zero-variance degeneration by construction: an exactly flat tape pins MFI at 0.0 and the machine buys once and holds forever (planted dead-flat tape: 1/0 ending LONG — disclosed, not upgraded).
- Trend non-participation by construction: sustained ramps never print sub-20 (0/0) — the rule sits out every ramp waiting for a dip that never comes, disclosed, not patched.
- Falling-knife hold by construction: sustained bleeds never print sup-80 (planted sustained-down tape: 1/0 ending LONG) — the dip-buy holds to the tape end, disclosed, not patched.
- Single-venue port residual: backtesting.py HLCV arithmetic vs Binance spot execution (prints, fees, open-definition across 24/7 sessions, equity-vs-crypto volume-regime differences) is unclaimed, disclosed.
- Next-open latency idealization: signal cadence on the decision close print while fills land on the next open; any live gap between the two differs by construction — disclosed, research-only (this convention is the source's own stated execution, preserved verbatim).
- Threshold-band residual: the 20–80 hold band commands nothing across mid-range chop — multi-month flat-holds inside the band are the normal case, not an anomaly, disclosed.
- No-authorship-page residual: the page prints no handle, license, or creation stamp; provenance rests on the QuantifiedTrader URL/slug, printed names, page hash, and fetch date — disclosed.
- Performance evidence is absent: nothing here is calibrated, fitted, or tuned to any backtest (the `14/20/80` defaults are the source's, never re-run here; the page's own grid-search section, where available, is not adopted as a parameter source).
- Author scope: the page ships exploratory research with an explicit not-investment-advice disclaimer, not a vetted trading system — this record is research-only and claims no live suitability.

## Implementation status

`not-implemented`: no dedicated controller, Qlib executable recipe or deployment artifact was created. PASS is a bounded research-expressibility proposal, not a claim of already runnable materialization. A selected strategy may later need the minimal strategy-specific implementation without a second admission flag.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review must independently inspect this exact PR head, remediate only primary-source-verifiable facts, then PASS exact-head merge or NOT_LOSSLESS close. Scout does not approve, merge, close, trade, backtest or deploy.

## Related Wiki records

None asserted.

## Sources

- Primary page + pin: https://quantifiedtrader.com/backtest/strategies/money-flow-index/ (`Money Flow Index`; page fetched live 2026-11-05, 42,620 bytes, SHA-256 `e3227373b4070824d9455022803d8a66e270d80e42cafe4f49dadec0db76fd9c`; implementation block `class MoneyFlowIndex(Strategy)` with `n = 14`, `_mfi(High, Low, Close, Volume, n)` single call (helper body unprinted — the name occurs once, at its call site; zero `def` prints beyond `init`/`next`), `mfi[-1] < 20 and not position → buy()`, `mfi[-1] > 80 and position → position.close()`; zero short/stop/limit/trailing/time/target/profit order calls in the order path (`limit` occurs once, inside the legal-boilerplate "not limited to accuracy" — fenced, not adopted); daily OHLCV frame, no-lookahead statement, next-bar-open execution, unmodeled costs, equity-index universe)
- Lane precedent (different mechanism, unmerged-proof never claimed): `quantifiedtrader-bb-width-squeeze-sma-state-long-flat-btcusdt-1d-2026-11-05.md`, `quantifiedtrader-atr-bands-lower-touch-midline-exit-long-flat-btcusdt-1d-2026-11-05.md`, `quantifiedtrader-keltner-squeeze-upper-breakout-sma-exit-long-flat-btcusdt-1d-2026-11-05.md`, `quantifiedtrader-raff-channel-midline-level-long-flat-btcusdt-1d-2026-11-04.md` and `quantifiedtrader-projection-oscillator-zero-cross-long-flat-btcusdt-1d-2026-11-04.md` (unprinted-helper textbook-freeze derivation pattern)
- MFI-arithmetic precedent (different mechanism, unmerged-proof never claimed): `forven-mfi-threshold-cross-long-flat-btcusdt-1h-2026-10-19.md` (typical-price money-flow ratio, strict direction predicates, `1e-10` floor — reused here as the frozen construction for the unprinted `_mfi`)
- Nearest pool lineages (different mechanisms, unmerged-proof never claimed): `alphatrend-mfi-atr-trailing-reversal-btcusdt-4h-2026-10-08.md` (MFI gate plus ATR-trailing exit); `mfi-threshold-divergence-reversal-two-sided-btcusdt-4h-2026-10-12.md` (threshold plus divergence read); `fmz-482880-rsi-bb-imi-mfi-quad-confluence-long-flat-btcusdt-1h-2026-10-27.md`, `freqtrade-bandtastic-1sig-lower-mfi46-upper2-close-bracket-long-flat-btcusdt-15m-2026-10-30.md` and `percent-b-mfi-dual-thrust-cross-two-sided-btcusdt-1d-2026-10-13.md` (MFI inside multi-indicator stacks)
- Exchange verification: Binance spot `api/v3/exchangeInfo` (`BTCUSDT`, `TRADING`, `tickSize 0.01`, min-qty/step 0.00001/0.00001, min-notional 5.0 via `NOTIONAL`) plus `api/v3/klines` 1d probes (3,366 completed bars 2017-08-17→2026-11-03, 12 post-warmup dip-to-saturation traverses → 12 entries / 12 exits ending FLAT, event digest `644c4058` double-run identical; planted tapes flat 1/0 LONG, up 0/0, down 1/0 LONG, drift-dip-rip 1/1 FLAT — degeneration/non-participation/round-trip fences), fetched live 2026-11-05
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently merged pinned package/source evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
