---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: (IK) Grid Script mapped-ladder long-only grid on BTCUSDT 15m bars
created: 2026-11-02
updated: 2026-11-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-11-02
sources:
  - https://www.tradingview.com/script/IIchZZ2m-IK-Grid-Script/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# (IK) Grid Script mapped-ladder long-only grid — independent BTC-USDT 15m derivative

## Provenance

**Canonical source (read live over HTTPS this cycle):** TradingView open-source strategy **`(IK) Grid Script`** by **`tapRoot_coding`** (Ian Kuzmik), stable URL above, Pine v4, Mozilla Public License 2.0 — short-literal citation only, no source block reproduced. The author description was verified live from the page HTML this cycle (long-only; market-order grid; buy on cross-under / sell on cross-over; one open order per grid line with orders mapped to grid lines so a buy on line #n always sells on line #n+1; top line never bought; bottom line never sold-on; grid cap 15 lines; `initial_capital` 100 USD with per-line sizing from capital/line-count; 0.1% commission; **no built-in stop loss**; manual bounds default with optional auto-bounds).

**Immutable logic pin (third-party mirror, byte-verified):** `hasnocool/tradingview-pine-scripts`, file **`(IK) Grid Script.pine`**, latest path commit **`e031cab2819a7d56fb8bb9d000252f51439986e2`** (2023-09-02), blob `9de5f486ea2604a1947cdfbe7145f736d35622af`, **10,552 bytes / 202 lines** (of which lines 1–114 are scraper artifacts — header echo plus line-number litter — and lines 115–202 carry the intact Pine body with NBSP padding; disclosed, logic read through the artifacts). Raw bytes fetched this cycle hash to sha256 `365f1f067d203dc47588c84d0ca8228f80523c698791d9b1aac057752ffa191d`, byte-identical to a second fetch pinned at the commit ref (`PIN-MATCH`). The body matches the live TV description clause-for-clause and matches the `strategy(...)` header independently quoted by FMZ strategy pages 439343/440879 (login-walled, corroboration only, never primary) and the official-org mirror doc `fmzquant/strategies` (same header line).

**Order-affecting logic read verbatim (code governs):** `strategy("(IK) Grid Script", overlay=true, pyramiding=14, close_entries_rule="ANY", default_qty_type=strategy.cash, initial_capital=100.0, currency="USD", commission_type=strategy.commission.percent, commission_value=0.1)`; inputs `i_autoBounds=false` (manual), `i_gridQty=8` (`minval=3`, `maxval=15`), manual bounds `0.285/0.225` (author-chart levels, not adopted); per-bar loop ascending over all lines — buy `id=tostring(i)` when `close < line[i]` and latch clear and `i < Q-1` with `qty=(initial_capital/(Q-1))/close`; sell `strategy.close(id=tostring(i-1))` when `close > line[i]` and `i != 0` and latch `orderArr[i-1]` set. No `strategy.exit`, no stop/target/trailing/time exit anywhere — author-explicit by design.

**Pine-block census (body fence):** 1 `strategy(`; 1 `strategy.entry` / 1 `strategy.close` / 0 `strategy.exit` / 0 `strategy.order`; 0 `request.*` / 0 `security(` / 0 `lookahead` / 0 `input.session` / 0 `timeframe.*` / 0 `calc_on_every_tick` / 0 `bar_magnifier` / 0 `process_orders_on_close` — all recorded as absent, never filled in. Default bar-close calculation with every predicate reading confirmed `close` only. With `i_autoBounds=false` the `highest/lowest/sma` auto-bound helpers are fenced off (their `f_getGridBounds` definitions remain in the body but no order path can reach them under the pinned input; disclosed). `pyramiding=14` is non-binding (at most `Q-1=7` concurrent reachable — disclosed); `close_entries_rule="ANY"` is inert here (only id-addressed `strategy.close` is used — disclosed).

**Structural facts carried over exactly:** (a) fixed manual grid, evenly spaced, bottom-up `line[i]=LB+W*i`; (b) cross-under buys / cross-over sells on confirmed close; (c) boolean per-line latch — one open order per line, re-arm only by its mapped sell; (d) order→line mapping (buy line #k exits only at line #k+1, whatever price does between); (e) top line never bought, sells never trigger at the bottom line; (f) fixed-cash sizing off initial capital (equity changes never resize); (g) 0.1% per-trade commission model; (h) long-only; single chart, single timeframe, OHLC-only, no session/timezone/MTF anywhere.

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the market/timeframe pin (source is timeframe-agnostic; author recommends small timeframes; reference copies backtest 1m/15m/1h — this record pins Binance BTC-USDT futures 15m), the manual bounds (source defaults are author-chart HBAR levels — researcher pins `LB=60000/UB=90000` bracketing the probe close), the capital scale (source 100 USD violates the 50-USDT min-notional per line — researcher pins `10000` USDT, i.e. ×100, so per-line `1428.5714` USDT), close-decided next-bar-open MARKET fills (Pine v4 default market-order semantics — same class, disclosed), the invalid-bar hold and the 5-bar admission warmup (source needs one close — 4 bars researcher margin, disclosed) are researcher adaptations. All are completely specified here; original claims are kept separate above.

**Immutable derivative identity:** `TV:IKGrid-tapRoot|manual-LB60000-UB90000-Q8-mapped-ladder|independent-derived-v1|BinanceFutures:BTC-USDT:15m|LONG-ONLY|cap10000-perline1428.5714|nextopen-MARKET|fee0.001|lev1x-isolated|warmup5|2026-11-02`. Changing any bound, line count, sizing, timing, market, cost, leverage or direction creates a different derivative.

## Economic mechanism

### Source-reported

Sideways-market mean-reversion harvesting: a fixed ladder of evenly spaced levels buys each dip through a line and sells exactly one line higher, capturing one grid-width per round trip without any price prediction; the author states a manual grid theoretically never loses (excluding slippage/commission) while warning there is no safety below the grid and no trading above it.

### Research interpretation

Unlike every pool sibling — the pool contains **zero** grid/ladder records at the pre-write snapshot (515 files grepped for `grid|martingale|pingpong|stepgain|gunbot|dca.bot`, zero hits; open `research/*` PRs likewise empty) — this machine never predicts: its only state is the per-line latch array, its only signal is the close-vs-line cross, and its exits are pre-mapped at entry time. Unlike pool breakout records it fades nothing and chases nothing; unlike pool mean-reversion records no band, z-score or indicator is involved. Live-window rate is sparse by construction: 3 post-warmup opens over 2,999 15m bars, all still held (down-drift month, no round trip completed — reported honestly, not tuned).

## Signal — Gate 1, fully pinned derivative

Index completed UTC 15-minute bars `t = 0, 1, ...` with real Binance BTC-USDT futures `C[t]` for signals, `O[t]` for fills. A bar with missing/nonfinite/non-positive OHLC, or `H < max(O,C)` / `L < min(O,C)`, is invalid (explicit hold). All constants are pinned literals: `LB=60000`, `UB=90000`, `Q=8`, `W=(UB-LB)/7=4285.714285...`, lines `L0..L7` bottom-up, per-line quote `10000/7=1428.5714` USDT.

- **Grid (fixed, causal):** lines need no history — computable before the first bar; no lookback, no repainting possible.
- **Buy leg (actionable only t ≥ 5, at bar `t`'s close, ascending `i=0..7`):** `buy[t,i] = C[t] < L[i] and latch[i]==false and i < 7` → open id `str(i)`, `qty = 1428.5714 / C[t]`.
- **Sell leg (same bar, after the buy check per `i`):** `sell[t,i] = C[t] > L[i] and i != 0 and latch[i-1]==true` → close id `str(i-1)`, latch cleared.
- **Mapping invariant:** a buy on line #k can only ever exit at line #k+1; one open per line; top line #7 never bought; no sell triggers at line #0. Same-bar multi-fire on both sides is legal (ascending loop order preserved from source).
- **Resolution (explicit researcher pin):** all bar-`t` legs fill at bar `t+1`'s **open** as MARKET orders; no fill executes if bar `t+1` is absent. At most 7 concurrent longs, fixed size each, no adds per line; a sold line re-arms immediately.
- **Explicitly disabled (source-native):** no stop-loss, no take-profit beyond the mapped sell, no trailing, no time exit, no opposite-direction action (long-only). Below-`LB` inventory is held indefinitely (`100% staked`, author's words); above-`UB` the book is flat and idle. This is the declared risk posture, not a gap.

## Required data / Gate 6 causality

**Warmup:** minimum 5 contiguous valid completed 15m bars (source needs one close; 4 bars researcher margin). No warmup-bar trades; pre-warmup flat by record rule.

Binance Kline `timestamp` is bar-open `T[t]` (pinned perpetual-candles path; `15m` is a carried `INTERVALS` entry `900` — byte-verified at the pin this cycle; row[0] open-time parsing and 15m-boundary alignment verified live this cycle over 2,999 bars). Bars become available no earlier than `T[t]+900s`. All decisions use the completed bar's `close` only; fills at next-bar open. No incomplete bar, future extremum, repainted level, MTF call, session template, or same-bar intrabar signal. Single OHLC feed — no second data dependency. If this effective-time discipline cannot be enforced, Gates 5/6 fail in implementation.

## Execution assumptions / Gate 5 pinned Hummingbot path

**Exact bounded engine:** Hummingbot package label `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (ancestor of local checkout `2dbc844` verified this cycle via `merge-base --is-ancestor`; re-verified at the pin this cycle: `BacktestingEngineBase.run_backtesting` + `determine_executor_actions` in controller bases, `OrderExecutorSimulator` class byte-present in `backtesting/executors_simulator/order_executor_simulator.py`, `INTERVALS "15m": 900` in `hummingbot/data_feed/candles_feed/binance_perpetual_candles/constants.py`). Prior merged Alpha PR **#414** reports a 902/902 wheel-file byte match and 33-assert representative validation for this source/package path; this Scout did not independently rehash the wheel. A different deployed package must be revalidated.

- **Market/feed:** Binance BTC-USDT futures venue, one 15m OHLCV stream (single-feed design — no MTF, no session, no second symbol). Opens feed next-open fills.
- **Controller path:** `BacktestingEngineBase.run_backtesting` → `controller.determine_executor_actions` → `CreateExecutorAction(OrderExecutorConfig)` → `OrderExecutorSimulator.simulate`. A **strategy-specific, not-yet-implemented** controller must compute the fixed 8-line ladder with the boolean per-line latch array, the mapped buy-#k/sell-at-#k+1 legs, and the ascending same-bar fire order. The generic executor does not calculate the strategy. Up to 7 concurrent `OrderExecutor`s (one per held line) — each a fixed-size long; `PositionExecutor`/grid-executor deliberately unused.
- **Orders (OrderExecutor only):** entries `side = BUY`, `position_action = OPEN`, closes `position_action = CLOSE`, `amount = 1428.5714/close` BTC (≈0.01824 BTC ≈ 1428.57 USDT at probe close — above verified 50-USDT min-notional, 0.001 min-qty and 0.10 tick facts), `connector_name = "binance"`, `trading_pair = "BTC-USDT"`, `execution_strategy = MARKET`, `price = None`, `leverage = 1` (Isolated). MARKET legs fill at the next bar's **open** per the source timing class. No fill executes if its required future bar is absent. Controller must use confirmed executor/hold state with a persistent latch ledger, never infer position from order requests. Fills are never conditional on equity, funding, or buying power: fixed-quote 1× ladder with no compounding and no abort rule (disclosed).
- **Fees and accounting:** 0.1% per filled side is a SOURCE commission pin (`commission_value=0.1` percent); slippage unmodeled, **not** evidence of zero real slippage (disclosed). Funding is **flagged, never zeroed**: long-only holds routinely span `00:00`/`08:00`/`16:00 UTC` stamps — modeled economics are not realized/canonical funding. No margin/cash-ledger behavior beyond the simulator's own accounting is claimed. Never treat engine PnL as fee-inclusive net equity without rebuilding from the fill ledger plus recorded fees. Precision beyond min-qty/min-notional/tick facts, partial fills, market impact and live fee tier remain unverified — not an execution or profitability approval.
- **Package/commit binding disclosure:** `20260920` is retained as the policy package **label only**; Gate 5 is bounded to the pinned commit's research-simulation semantics re-verified above, reusing the previously reviewed MARKET next-open primitive with close-decided level legs and no novel executor type. Sibling PASS records are execution-path evidence only, never proof of this candidate.

## Evidence

### Source-reported

The pinned body ships the complete machine: fixed manual bounds with even spacing, ascending per-line loop, cross-under cash-sized buys (`initial_capital/(Q-1)` per line), cross-over id-addressed closes, per-line boolean latches, order→line mapping, top-line buy ban, `pyramiding=14`, `close_entries_rule="ANY"`, 0.1% commission, long-only, and no stop of any kind. It ships no market/timeframe claim usable for futures (author-chart HBAR levels and small-timeframe advice — not adopted as 15m/crypto claims) and no performance figure of any kind — none adopted; those are researcher pins disclosed above.

### Independently reproduced

**None.** No strategy backtest, event-level Qlib/Hummingbot parity, wheel rehash, deployment or profitability experiment occurred. Pinned engine source inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifacts this run are researcher self-checks of the latch/ladder/mapping pipeline (ascending loop, mapped exits, top-line ban, same-bar multi-fire, below-bound bag, above-bound idle, next-open fills), run in scratch (never committed): `SELF-CHECK OK` — logic verification only, not a backtest, not parity.

**Planted-tape verification (this cycle, deterministic PASS, double-run identical):** TAPE-BUYSELL 1 open id6 / 1 mapped close ending flat (digest `6b9801efc4b8a0c8`); TAPE-MAP-HOLD chop below the exit line holds with no premature sell (digest `06390d20ebbc6b1f`); TAPE-MULTI one bar opens ids 5+6 (digest `98fb19a170d1ec25`); TAPE-BELOW opens all 7 tradeable lines and holds the bag with zero sells (digest `4c4299a9256bd40f`); TAPE-ABOVE 0 events ending flat (digest `4f53cda18c2baa0c`); TAPE-TOPGUARD 89999 below the excluded top line opens nothing (same digest). The tapes caught and fixed one genuine harness defect pre-write (an inverted `L`-consistency guard in the probe filter that rejected valid bars; the shipped state machine never used the guard — fixed, full re-run, double-run identical).

**Live-exchange microstructure probes (this cycle, futures 15m klines, 2,999 completed bars 2026-10-01→2026-11-02, last close 78,330.0):** 3 post-warmup opens (ids 6, 5, 4 as price drifted down through the ladder) / 0 closes, ending holding [4, 5, 6] (digest `117269a8d5aceb8a`); sub-window bars 999–1999 print 2 opens / 0 closes holding [5, 6] (digest `036a16ad9991b41b`). Per-line notional 1,428.57 USDT throughout. Two independent runs produce identical digests. Admission is engineering capability, never an event-rate or profitability claim.

### Negative evidence

At the pre-write snapshot `main@825e93f9`, the root Git tree contained **515** strategy Markdown files (517 minus two READMEs). Exact-identity working-tree searches for `grid` / `martingale` / `pingpong` / `stepgain` / `gunbot` / `dca.bot` / `ik-grid` / `taproot` / `tap_root` / `Grid Script` return **zero** same-construction records. Sixteen open `research/*` PRs were inspected by per-PR title/head — no collision (nearest open lanes are EMA-stack-RSI, OneTrend, dual-MACD, volume-dip, supertrend, Heracles, ClucMay, AdxSmas, CCI, 2yMA, SSL, Chandelier, Gaussian, Larry-Williams, dual-Kalman, Turtle-Soup — none a grid/ladder). Closed-PR scan surfaces no member of this family. Not a duplicate, paraphrase, or trivial parameter variant.

## Falsification plan

After independent admission and separate downstream selection only: compare the frozen ladder against (a) line-count twins (5/12 lines — isolating ladder density; researcher variation), (b) bound-width twins (tighter/wider researcher bounds — isolating range choice; researcher variation), (c) auto-bounds twins (lookback/dev trailing bounds — a different, undisclosed-here derivative; never attributed to source), and (d) fee/slippage twins (0.05%/0.1% plus a fixed-slip leg — isolating cost; researcher variation). Check event rate, round-trip attribution, hold-time distribution, below-bound dwell, warmup sensitivity (5 vs 1), and fill-anchor slippage. Event-level Qlib/Hummingbot parity of the strategy/execution path is required before mass screening if that path introduces a new unverified capability; do not interpret HB_READY as parity or profitability.

## Crypto portability

This derivative is **BTC-USDT Binance futures 15m** only. Stated plainly: the machine needs completed-bar OHLC plus the 5-bar admission warmup (no indicator bound); the entries are cross-under opens with a live-window rate of ~3 predicate bars per 2,999 15m bars in a down-drift month; the exits are pre-mapped sells one line up with no stop/target/trailing/time leg; 15m slippage plus funding apply to every held span. The ported legs carry no session, calendar, or gap-regime dependence (the source is session-free; market/timeframe/capital changes are disclosed researcher adaptations), so 24/7 crypto continuous trading introduces no session-template port of any kind. No rescaling, no cross-asset claim is made. No frequency, profitability, or capacity claim is made. Seven-coin, 1h/4h/1d, BO/SO 6/6/6, and 3×/5× futures experiments are optional separate downstream campaigns, **not** admission requirements or silently authorized equivalent executions.

## Limitations

The market/timeframe pin (source is timeframe-agnostic with small-timeframe advice — not adopted), manual bounds (researcher 60000/90000 vs author-chart levels), capital scale (×100 for min-notional), cash, leverage, warmup, constant fence, 0.1% source fee, close-decided next-open resolution, invalid-bar hold, and the inert `close_entries_rule`/non-binding `pyramiding` readings are researcher pins, never attributed to the source. The auto-bounds branch is fenced off by the pinned `false` input — any rule using trailing bounds is a different unpinned strategy. No performance figure is adopted from any mirror. Probe windows end holding — no invented fills. Package/source binding cites an earlier independent review for the wheel hash rather than a fresh rehash. The live window exercises opens only; mapped closes, multi-fire, bag-hold and idle legs are exercised on planted tapes, not live tape. No Qlib parity, historical Survivor, HB Certified, Paper/Testnet/Live or profitability claim.

## Implementation status

`not-implemented`: no dedicated controller, Qlib executable recipe or deployment artifact was created. PASS is a bounded research-expressibility proposal, not a claim of already runnable materialization. A selected strategy may later need the minimal strategy-specific implementation without a second admission flag.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review must independently inspect this exact PR head, remediate only primary-source-verifiable facts, then PASS exact-head merge or NOT_LOSSLESS close. Scout does not approve, merge, close, trade, backtest or deploy.

## Related Wiki records

None asserted.

## Sources

- Primary strategy + as-of: https://www.tradingview.com/script/IIchZZ2m-IK-Grid-Script/ (`(IK) Grid Script` by `tapRoot_coding`, Pine v4, MPL-2.0; author description verified live from page HTML 2026-11-02 — long-only, mapped ladder exits, no stop loss, short-literal citation only)
- Immutable logic mirror: `hasnocool/tradingview-pine-scripts`, file `(IK) Grid Script.pine`, path commit `e031cab2819a7d56fb8bb9d000252f51439986e2` (2023-09-02), blob `9de5f486ea2604a1947cdfbe7145f736d35622af`, 10,552 bytes; raw sha256 `365f1f067d203dc47588c84d0ca8228f80523c698791d9b1aac057752ffa191d` verified live 2026-11-02 with byte-identical commit-ref re-fetch (scraper line-number/NBSP artifacts disclosed)
- Corroboration only: FMZ strategy pages 439343/440879 (same `strategy(...)` header, login-walled) and `fmzquant/strategies` adaptive-grid doc (same header line)
- Exchange verification: Binance futures `fapi/v1/exchangeInfo` via `fapi.binance.com` (`BTCUSDT`, `PERPETUAL`, `TRADING`, `tickSize 0.10`, min-qty 0.001, min-notional 50) plus `fapi/v1/klines` 15m microstructure probes (2,999 completed bars 2026-10-01→2026-11-02, 3 opens / 0 closes holding [4,5,6], plant digests `6b9801ef`/`06390d20`/`98fb19a1`/`4c4299a9`/`4f53cda1`, window digests `117269a8d5aceb8a`/`036a16ad9991b41b`), fetched live 2026-11-02
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently merged pinned package/source evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
