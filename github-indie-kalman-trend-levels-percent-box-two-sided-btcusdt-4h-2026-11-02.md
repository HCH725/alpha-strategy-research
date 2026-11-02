---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: BigBeluga dual-Kalman 50/150 cross percent-box two-sided on BTCUSDT 4h bars
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
  - https://github.com/Indie-script/indie-script.github.io/blob/008ef56613e6a5d3ca599e25fb0f70c39f7c2fea/indicators/KalmanFilter%20lite/KalmanFilter%20lite.pinescript5
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Dual-Kalman 50/150 cross + avg-price 2%/4% box — independent BTC-USDT 4h derivative

## Provenance

**Canonical source (fetched live over HTTPS this cycle, immutable pin):** `Indie-script/indie-script.github.io` commit **`008ef56613e6a5d3ca599e25fb0f70c39f7c2fea`** (2025-04-18, repo's sole history entry — stable), file **`indicators/KalmanFilter lite/KalmanFilter lite.pinescript5`**, blob `db90d0fdb2c670b6ab9b1d9d2c40d4f9cc4d9c4b`, **4,561 bytes / 94 lines**, Pine v5, `indicator("Kalman Trend Levels [BigBeluga]", overlay = true, ...)` — an indicator, not a strategy. Raw bytes re-downloaded this cycle hash to sha256 `f4f816000aedc7f6cc494e3412fac2ee38df81245f572732793fce27edefb03e`, byte-identical to the working copy. Permalink above.

**Order-affecting logic read verbatim (code governs; indicator ships no orders):** `kalman_filter(src, length, R = 0.01, Q = 0.1)` recursion — `var float estimate = na` seeded once via `if na(estimate) estimate := src[1]`; `prediction := estimate`; `kalman_gain := error_est / (error_est + error_meas)` with `var float error_est = 1.0`, `var float error_meas = R * (length)`; `estimate := prediction + kalman_gain * (src - prediction)`; `error_est := (1 - kalman_gain) * error_est + Q / (length)`. Instantiated twice on `close` with fenced defaults `short_len = input.int(50)` / `long_len = input.int(150)`; state `trend_up = short_kalman > long_kalman`; flip idiom `trend_up and not trend_up[1]` (up-flip) mirrored `trend_up[1] and not trend_up` (down-flip) — in-source these arm labels/boxes only (display triggers, never orders — disclosed).

**Pine-block census (94-line fence):** 1 `indicator(`; 0 `strategy.entry` / 0 `strategy.exit` / 0 `strategy.close` / 0 `strategy.order` code of any kind (no alert token anywhere — disclosed); `kalman_filter(close, …)` ×2; `ta.atr` ×1 (`ta.atr(200) * 0.5` feeds display boxes/zones only — dropped, disclosed); 6 `input.*` (50/150/`retest_sig=false`/`candle_color=true`/2 colors — retest fenced off at its default `false`, never pinned); 0 `request.` / 0 `security(` / 0 `timeframe.*` / 0 `barstate.isconfirmed` / 0 `calc_on_every_tick` / 0 `bar_magnifier` / 0 `pyramiding` — all recorded as absent, never filled in. All labels/boxes/`plotcandle`/fills display-only — dropped, disclosed.

**Structural facts carried over exactly:** (a) dual adaptive-gain Kalman smoothers on `close` with coupled lengths 50/150 and shared R=0.01/Q=0.1; (b) trend state is the strict inequality `short > long`, flips only on completed-bar transitions; (c) no MTF, no session/timezone, no intrabar/magnifier semantics anywhere; (d) the ATR(200)×0.5 zones are box-drawing levels, not stops — never ported as risk.

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the source is an indicator and ships no entries, exits, sizing, or risk. Researcher-declared adaptations are exactly nine: (1) promotion of the source flip idiom to two-sided entries on confirmed bars (disclosed promotion, same strict semantics); (2) latched avg-price −2%/+4% box with entries-dominate stop-first resolution (fully researcher-designed risk — the source has no exits; disclosed); (3) fixed **0.01 BTC** sizing (≈783.1 USDT at probe close 78,313.0, above verified 50-USDT min-notional and 0.001 min-qty; 10,000 USDT cash; Isolated 1×); (4) 300-bar warmup with pre-warmup bars flat (150 = long-filter structural scale, +150 researcher margin for gain convergence); (5) display drop (labels, boxes, candle colors, fills, retest); (6) constant fence (50/150/0.01/0.1/two-sided/box-on — any other value is a different unpinned rule); (7) explicit **0.05%/side research cost**, slippage unmodeled (disclosed); (8) close-decided exits filled next-bar-open MARKET (research-model timing convention, never a live-engine claim); (9) once-per-completed-bar evaluation (source timing class otherwise preserved — no `isconfirmed` ships, so the bar discipline is a researcher pin, disclosed).

**Immutable derivative identity:** `GH:Indie-script-008ef56|kalman50-150_R0.01-Q0.1_cross_SL2-TP4-avgpx-latched|independent-derived-v1|BinanceFutures:BTC-USDT:4h|TWO-SIDED|0.01BTC|nextopen-MARKET|fee0.0005|cash10000|lev1x-isolated|entries-dominate-stopfirst|warmup300|2026-11-02`. Changing any formula, length, ratio, gate, timing, market, risk, cost, cash, leverage or direction creates a different derivative.

## Economic mechanism

### Source-reported
Adaptive noise-balancing trend-state estimation: each Kalman filter trusts new closes versus its prior estimate per the R/Q variance ratio (tight tracking in trends, heavy smoothing in chop — no fixed lag/length), and the short/long pair crossing marks trend-state transitions with built-in hysteresis (a flip needs sustained displacement, not one noisy bar).

### Research interpretation
Unlike pool EMA siblings (static-span averages, e.g. naked EMA9/21 cross with the same house 2%/4% box — fixed lag, flips on every strict cross), this machine's edges move with per-bar adaptive gain (lengths 50/150 set noise scaling, not span lag), so flips are rarer and more selective: 11 post-warmup predicates per 1,500 4h bars here versus 72 for the EMA9/21 sibling. Unlike closed unmerged #623 (egoigor1976 kinetic-Kalman breakout ±MAE200×2.6, ETHUSDT 15m — prediction-band breakout signal, no risk box, plus buying-power-abort/margin-ledger/terminated-window defects that closed it), this derivative uses a different source, a dual-filter cross signal, BTCUSDT 4h, a latched percent box, and replicates none of those defects (no abort rule, no margin ledger, no terminated-window claim — fenced below). Four-axis distinction holds on source, signal, risk, and market.

## Signal — Gate 1, fully pinned derivative

Index completed UTC 4-hour bars `t = 0, 1, ...` with real Binance BTC-USDT futures `C[t]` for signals/anchors, `H[t]`/`L[t]` for box-touch legs, `O[t]` for fills. A bar with missing/nonfinite/non-positive OHLC, or `H < max(O,C)` / `L < min(O,C)`, is invalid for signals. All constants are source-default literals.

- **Kalman pair (causal, per-bar, Pine-faithful):** `Ks[t]=KF50(C)`, `Kl[t]=KF150(C)` with `KF` the exact recursion above (R=0.01, Q=0.1, `error_est` seeded 1.0, `estimate` seeded from `C[1]` — first bar na, disclosed); `up[t]` = `Ks[t]>Kl[t]`.
- **Predicates (actionable only t ≥ 300, at bar `t`'s close):** `longSig[t] = up[t] and not up[t-1]`, `shortSig[t] = not up[t] and up[t-1]`. Pre-warmup bars flat by record rule; every na/degenerate bar is an explicit neither-fire hold.
- **Latched box (researcher-designed, fixed at fill-average `A`, never moved):** long `SL=A×0.98`, `TP=A×1.04`; short mirrored `SL=A×1.02`, `TP=A×0.96`.
- **Resolution (explicit researcher pin):** entries fill next-bar-open MARKET; each held bar `v` (fill bar +1 onward) evaluates at its close in code order — opposite entry first (reversal dominates, old box dies), else SL-touch, else TP-touch (`H/L` vs latched levels); SL+TP co-fire is one flat close (stop wins). Opposite confluence while flat is impossible by construction (strict opposite inequalities — verified property). Single position, no adds: same-side refire is a no-op.

## Required data / Gate 6 causality

**Warmup:** minimum 300 contiguous valid completed 4h bars; covers the long filter's 150-bar structural scale plus a 150-bar researcher margin for adaptive-gain convergence (the recursion is defined from bar 1 via the `src[1]` seed — the margin renders seeding immaterial post-warmup, disclosed). No warmup-bar trades; pre-warmup flat by record rule.

Binance Kline `timestamp` is bar-open `T[t]` (pinned perpetual-candles path; `4h` is a carried `INTERVALS` entry `14400` — byte-verified at the pin this cycle; row[0] open-time parsing, 4h-boundary alignment verified live this cycle). Bars become available no earlier than `T[t]+14400s`. All decisions use completed bars only (researcher once-per-bar pin — no `isconfirmed` ships in source, disclosed); fills at next-bar open; SL/TP legs are close-decided against completed-bar `H/L` with next-open fills (research-model convention, disclosed). No incomplete bar, future extremum, repainted graphic, MTF call, session template, or same-bar intrabar signal. Single OHLC feed — no second data dependency. If this effective-time discipline cannot be enforced, Gates 5/6 fail in implementation.

## Execution assumptions / Gate 5 pinned Hummingbot path

**Exact bounded engine:** Hummingbot package label `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (ancestor of local checkout `2dbc844` verified this cycle via `merge-base --is-ancestor`; re-verified at the pin this cycle: `BacktestingEngineBase.run_backtesting` + `determine_executor_actions` in controller bases, `OrderExecutorSimulator` class byte-present in `executors_simulator/`, `INTERVALS "4h": 14400` in `hummingbot/data_feed/candles_feed/binance_perpetual_candles/constants.py`). Prior merged Alpha PR **#414** reports a 902/902 wheel-file byte match and 33-assert representative validation for this source/package path; this Scout did not independently rehash the wheel. A different deployed package must be revalidated.

- **Market/feed:** Binance BTC-USDT futures venue, one 4h OHLCV stream (single-feed design — no MTF, no session, no second symbol). Opens feed next-open fills.
- **Controller path:** `BacktestingEngineBase.run_backtesting` → `controller.determine_executor_actions` → `CreateExecutorAction(OrderExecutorConfig)` → `OrderExecutorSimulator.simulate`. A **strategy-specific, not-yet-implemented** controller must compute the dual-Kalman recursion with strict flip semantics, the new-position avg-price 2%/4% latch, and the entries-dominate stop-first state pin. The generic executor does not calculate the strategy.
- **Orders (OrderExecutor only — PositionExecutor deliberately unused):** entries `side = BUY/SELL`, `position_action = OPEN`, closes `position_action = CLOSE` (SL, TP, and reversal legs all close-then-act per the pin), `amount = Decimal("0.01")` (≈783.1 USDT at probe close — above verified 50-USDT min-notional and 0.001 min-qty), `connector_name = "binance"`, `trading_pair = "BTC-USDT"`, `execution_strategy = MARKET`, `price = None`, `leverage = 1` (Isolated). MARKET legs fill at the next bar's **open** per the source timing class. No fill executes if its required future bar is absent. Controller must use confirmed executor/hold state with a persistent ledger, never infer position from order requests. Fills are never conditional on equity, funding, or buying power: fixed-size 1× single-position with no compounding and **no abort rule** (the #623 defect class is explicitly fenced out — disclosed).
- **Fees and accounting:** 0.05% per filled side is a RESEARCHER research-model pin; slippage unmodeled, **not** evidence of zero real slippage (disclosed). Funding is **flagged, never zeroed**: 4h holds routinely span `00:00`/`08:00`/`16:00 UTC` stamps — modeled economics are not realized/canonical funding. No margin/cash-ledger behavior beyond the simulator's own accounting is claimed (no #623-style buying-power ledger — disclosed). Never treat engine PnL as fee-inclusive net equity without rebuilding from the fill ledger plus recorded fees. Precision beyond min-qty/min-notional/tick facts, partial fills, market impact and live fee tier remain unverified — not an execution or profitability approval.
- **Package/commit binding disclosure:** `20260920` is retained as the policy package **label only**; Gate 5 is bounded to the pinned commit's research-simulation semantics re-verified above, reusing the previously reviewed MARKET next-open primitive with close-decided box legs and no novel executor type. Sibling PASS records are execution-path evidence only, never proof of this candidate.

## Evidence

### Source-reported
The pinned 94-line fence ships the complete signal construction: the indicator declaration, the 50/150 length inputs with R=0.01/Q=0.1 defaults, the exact Kalman prediction/update recursion with seeding, the strict-inequality trend state with confirmed-bar flip idiom, and ATR(200)×0.5 display zones. It ships no orders, no sizing, no exits, and no performance figure of any kind — none adopted; all of those are researcher pins disclosed above.

### Independently reproduced
**None.** No strategy backtest, event-level Qlib/Hummingbot parity, wheel rehash, deployment or profitability experiment occurred. Pinned engine source inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifacts this run are researcher self-checks of the signal/latch/state pipeline (Pine-faithful Kalman pair, strict flips, avg-price latch, code-order entries-dominate stop-first resolution, next-open fills), run in scratch (never committed): `SELF-CHECK OK` — logic verification only, not a backtest, not parity.

**Planted-tape verification (this cycle, deterministic PASS):** MICRO-SL tape prints a long-flip at bar 207 driving 1 open / 1 SL close ending flat (digest `aa070bb350b33e49`); MICRO-REV mean-reverting tape prints 6 opens / 5 reversal closes ending holding (digest `266b2e6a82034291`); 956-bar trend/shock macro tape prints 2 post-warmup `LE` driving 2 opens / 2 TP closes ending flat (digest `23514d7620d72d6e`); two independent runs identical.

**Live-exchange microstructure probes (this cycle, futures 4h klines, 1,500 completed bars 2026-02-25→2026-11-01, last close 78,313.0):** 5 post-warmup `LE` and 6 post-warmup `SE` predicate bars drive 11 state-machine opens / 11 closes (6 SL-touch / 3 TP-touch, 2 reversals) ending FLAT (digest `76924aaa4ba6b618`); sub-window bars 300–999 print 3 `LE` / 2 `SE` driving 5 opens / 4 closes (2 SL / 0 TP / 2 reversals) ending LONG, same honest cut (digest `bc3e0630da96204a`). 0.01 BTC ≈ 783.1 USDT notional at window close. Two independent runs produce identical digests. Admission is engineering capability, never an event-rate or profitability claim.

### Negative evidence
At the pre-write snapshot `main@6c4ea20e`, the root Git tree contained **512** strategy Markdown records (514 files minus two READMEs). Exact-identity working-tree searches for `kalman` / `Kalman` / `BigBeluga` / `indie-script` / `db90d0fd` return **zero** records. Fifteen open `research/*` PRs were inspected by per-PR title/head — no collision. Closed-PR scan surfaces only #623 (TradingView egoigor1976 kinetic-Kalman breakout MAE-band, ETHUSDT 15m — closed NOT_LOSSLESS, never merged): different source, different signal (prediction-band breakout vs dual-filter cross), different risk (none vs latched 2%/4% box), different market/TF, and its exact blockers (buying-power abort, margin ledger, terminated-window error) are fenced out above. Not a duplicate, paraphrase, or trivial parameter variant.

## Falsification plan

After independent admission and separate downstream selection only: compare the frozen Kalman-cross box book against (a) static-EMA twins (isolating adaptivity), (b) no-box twins (pure flip-to-flip reversal — isolating the percent box), (c) single-Kalman slope twins (isolating the cross), and (d) 1%/2% and 3%/6% box twins (isolating the 2R choice; researcher variation); check event rate, SL/TP/reversal attribution, hold-time distribution, warmup sensitivity (300 vs 450), and fill-anchor slippage. Event-level Qlib/Hummingbot parity of the strategy/execution path is required before mass screening if that path introduces a new unverified capability; do not interpret HB_READY as parity or profitability.

## Crypto portability

This derivative is **BTC-USDT Binance futures 4h** only. Stated plainly: the filter needs closes plus the 300-bar admission warmup (long-length-bound); the entries are dual-Kalman flips with a live-window rate of ~11 predicates per 1,500 4h bars; the exits are a researcher-latched 2%/4% avg-price box with reversal dominance; 4h slippage plus funding apply to every held span. No rescaling, no cross-asset claim is made. No frequency, profitability, or capacity claim is made. Seven-coin, 1h/4h/1d, BO/SO 6/6/6, and 3×/5× futures experiments are optional separate downstream campaigns, **not** admission requirements or silently authorized equivalent executions.

## Limitations

The indicator→strategy promotion, market/timeframe pin (source is chart-agnostic), sizing, cash, leverage, warmup, display drop, constant fence, 0.05% research fee, close-decided next-open resolution, and once-per-bar evaluation are researcher pins, never attributed to the source. The source ATR(200)×0.5 zones are display levels, never ported as risk (disclosed). The repository `© BigBeluga` file is licensed CC BY-NC-SA 4.0 — this record cites short literal lines only and reproduces no source block; research-only use asserted, no commercial claim. Pine v5 Kalman seeding (`src[1]` first-value seed, `error_est` 1.0) is adopted explicitly with a 150-bar convergence margin inside the 300 warmup. Entries read completed-bar closes only; SL/TP legs are close-decided against completed-bar H/L with next-open fills (research-model convention, disclosed). Probe windows end flat except the sub-window LONG — no invented fills. Package/source binding cites an earlier independent review for the wheel hash rather than a fresh rehash. No Qlib parity, historical Survivor, HB Certified, Paper/Testnet/Live or profitability claim.

## Implementation status

`not-implemented`: no dedicated controller, Qlib executable recipe or deployment artifact was created. PASS is a bounded research-expressibility proposal, not a claim of already runnable materialization. A selected strategy may later need the minimal strategy-specific implementation without a second admission flag.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review must independently inspect this exact PR head, remediate only primary-source-verifiable facts, then PASS exact-head merge or NOT_LOSSLESS close. Scout does not approve, merge, close, trade, backtest or deploy.

## Related Wiki records

None asserted.

## Sources

- Primary implementation + pin: https://github.com/Indie-script/indie-script.github.io/blob/008ef56613e6a5d3ca599e25fb0f70c39f7c2fea/indicators/KalmanFilter%20lite/KalmanFilter%20lite.pinescript5 (commit `008ef56613e6a5d3ca599e25fb0f70c39f7c2fea`, 2025-04-18; blob `db90d0fdb2c670b6ab9b1d9d2c40d4f9cc4d9c4b`; Pine v5, 94 lines / 4,561 bytes; raw sha256 `f4f816000aedc7f6cc494e3412fac2ee38df81245f572732793fce27edefb03e` verified live 2026-11-02; CC BY-NC-SA 4.0 © BigBeluga — short-literal citation only)
- Exchange verification: Binance futures `fapi/v1/exchangeInfo` (`BTCUSDT`, `PERPETUAL`, `tickSize 0.10`, min-qty 0.001, min-notional 50) plus `fapi/v1/klines` 4h microstructure probes (1,500 completed bars 2026-02-25→2026-11-01, 5 LE / 6 SE → 11 opens / 11 closes, plant digests `aa070bb350b33e49`/`266b2e6a82034291`/`23514d7620d72d6e`, window digests `76924aaa4ba6b618`/`bc3e0630da96204a`), fetched live 2026-11-02
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently merged pinned package/source evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
- Closed unmerged Kalman lineage (different mechanism, blockers fenced — never claimed): https://github.com/HCH725/alpha-strategy-research/pull/623
- Nearest pool lineages (different mechanisms, unmerged-proof never claimed): naked-cross `github-traderspost-ema921-naked-percent-box-two-sided-btcusdt-4h-2026-11-02.md`; Q-Trend-KVO confluence https://github.com/HCH725/alpha-strategy-research/pull/697; MACD86 zero-gate https://github.com/HCH725/alpha-strategy-research/pull/698
- Pine reference: v5 `var`-series causal recursion, `ta.atr`, strict-inequality flip idiom
