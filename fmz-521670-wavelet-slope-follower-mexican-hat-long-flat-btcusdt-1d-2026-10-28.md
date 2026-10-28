---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "FMZ 521670 Wavelet Candlestick Slope Follower Mexican-Hat long-flat BTCUSDT 1d independent derivative"
created: 2026-10-28
updated: 2026-10-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - fmz
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-28
sources:
  - https://www.fmz.com/strategy/521670
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Wavelet Candlestick Slope Follower (Mexican Hat, level 3) — BTCUSDT spot 1d long-flat derivative

## Provenance

- **Primary source (first-party FMZ page, public, no login):** https://www.fmz.com/strategy/521670 — title `Wavelet Candlestick Slope Follower`, author `ianzeng123`, `Created: 2025-12-17 15:27:18`, Copy 9 / Hits 631, tags `Trend/SLOPE/WAVELET/MEXICAN HAT/RICKER`, Pine v5 program `strategy("Wavelet Candlestick Slope Follower-Master Edition ", overlay=true)` under header `// © wojlucz` with Mozilla Public License 2.0 notice. This cycle the page returned HTTP 200 twice (906,425-byte document; all seven verbatim code tokens `Norm Long`, `w_close`, `Mexican Hat (Ricker)`, `strategy.entry`, `Smoothing Level`, `convolve`, `plotcandle` confirmed present in the public HTML); no login-wall bypass was performed.
- **Verbatim program inspected in full this cycle:** the complete 121-line Pine v5 listing (4,674 bytes, md5 `a2143f58190a6fa0f29ae15e646cc4b8`) was extracted from the public page payload and read end to end. Only rule tokens are normalized and cited here; no large source block is copied into this repository.
- **Declaration-line census on the verbatim program:** 1 `strategy(`, 1 `strategy.entry` (`"Norm Long"`/`strategy.long`), 1 `strategy.close` (`"Norm Long"`), 0 `strategy.exit`, 0 `strategy.order`, 0 `pyramiding`, 0 `process_orders_on_close`, 0 `calc_on_every_tick`, 0 `request.*`/`security(`/`timeframe.`/`import`, 0 `volume`, 0 `barstate`, 0 `nz(`/`na(`. Three `input.*` declarations exist but only two affect the signal (`w_type` default `"Mexican Hat (Ricker)"`, `w_lvl` default `3` min 1 max 5); the third (`show_candles`, default true) is display-only and not adopted.
- **Researcher-defined derivative v1, NOT source-native:** preserve the exact Mexican-Hat coefficients, normalization, 3-level cascade, and strict slope comparison, but trade Binance **BTCUSDT spot** UTC **1d** LONG/FLAT with fixed 0.001 BTC, 10,000 USDT cash, hypothetical 0.1% fee per side, Pine-default next-bar semantics adapted to next completed-bar-close MARKET fills, and warmup 60. This drops the source `/*backtest` stanza (2025-01-01→2025-12-15, `Futures_Binance BTC_USDT`, balance 500000, `period/basePeriod 1d`) and default-quantity semantics. These choices **materially change** original trade economics.
- **Frozen independent identity:** FMZ:521670|ianzeng123|wojlucz-pinev5|derived-v1-20261028|BinanceSpot-BTCUSDT-UTC1d|MexHat-L3-normalized|wclose-slope-sign|entry-rising-exit-falling|t-to-tplus1-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-each-side|warmup60. Any decision-critical alteration creates a new derived version, not a silent update.

## Economic mechanism

### Source-reported

Wavelet denoising plus low-dimensional decision: a Mexican-Hat (Ricker) wavelet filter reconstructs smooth candlesticks from noisy prices, and the simplest slope judgment on the smoothed close makes long/flat decisions. The 7-tap kernel `[-0.1, 0.0, 0.4, 0.8, 0.4, 0.0, -0.1]` acts as an edge-detection filter whose negative side lobes penalize distant-price influence; three cascade levels (steps 1/2/4) composite short-horizon smoothing with longer-horizon trend while preserving wavelet shape. The page's numeric superiority claims ("40% noise filtering", "25% fewer false signals", "outperforms traditional MA") are unsubstantiated marketing prose with no table, figure, or reproducible experiment and are **not** adopted as evidence.

### Research interpretation

This derivative holds a long only while the smoothed close keeps rising bar-over-bar and exits to flat on the first smoothed-close decline — a pure slope-sign state hold on a fixed 43-tap causal FIR, not a threshold breakout and not a band cross. The kernel's negative lobes (total −0.2208 weight after normalization) make it a different signal object from any all-positive-weight average: equal closes route to hold (both predicates false), and the only risk control is the slope-flip close exit, so a slow bleed that never prints a downtick in smoothed space stays exposed.

## Signal

1. **Input and availability:** one chronological, contiguous sequence of actual Binance BTCUSDT spot UTC **1d** candles indexed t=0,1,... . Native opening time T[t] must be UTC midnight-aligned and T[t+1]-T[t]=86400 seconds. Require finite positive O,H,L,C, H>=max(O,C), L<=min(O,C); volume is unused and unchecked. Reject duplicates, gaps, out-of-order bars, missing/zero/nonfinite observed prices or incomplete candles; never interpolate or forward-fill. Completed bar t is available at E[t]=T[t]+86400, not T[t]. Float64 chronological arithmetic, no intermediate rounding. Only the **close** series is consumed by the decision (open/high/low feed display-only smoothed candles, never a predicate).
2. **Constants (researcher-pinned to source defaults):** `w_type="Mexican Hat (Ricker)"` pinned (the six sibling wavelet branches are code-present but unexplored and frozen out, not silently removed), `w_lvl=3` pinned, kernel `h=[-0.1,0.0,0.4,0.8,0.4,0.0,-0.1]`, weight sum `1.4`.
3. **Pine-faithful cascade (all bars, causal only):** `convolve(src,coeffs,step)`: `y[t]=Σ_i src[t-i·step]·h[i] / 1.4`; any out-of-range history index yields Pine `na`, never an invented value. `w_close = L3(L2(L1(close)))` with steps 1, 2, 4. Maximum causal lag is 6+12+24=42 bars, so the first valid `w_close` falls at index 42 (verified on real data this cycle). Division guard `sum_w != 0 ? sum_val/sum_w : sum_val` is code-present; with the pinned kernel the divisor is always 1.4.
4. **State:** `w_close[t]` na or `w_close[t-1]` na → hold the prior state (pre-validity: no signal, never an order). Else `w_close[t]>w_close[t-1]` → `+1` (rising); `w_close[t]<w_close[t-1]` → `-1` (falling); strict inequality with equality routing to hold — both Pine `if` guards are false on equal prints.
5. **Warmup:** bars t=0..59 are **60 completed-bar no-trade warmup** (researcher-declared; covers the 42-bar cascade seed plus margin — first valid `w_close` at index 42, first comparable slope at index 43, verified this cycle). First eligible decision is t=60.
6. **Entry:** when FLAT with no pending action, t>=60, t strictly later than the last SELL-fill bar, and `state[t]==+1` (faithful to the source `if (is_rising) strategy.entry("Norm Long", strategy.long)` under default pyramiding=0), queue exactly one BUY. Dispatch on row t+1 only, independently of that row's signal, and model a full 0.001 BTC MARKET fill at its **actual observed completed close** C[t+1], effective E[t+1]. No t+1 price or indicator is used to decide at t. If row t+1 does not exist, leave unfilled. Require cash >=Decimal("0.001")*Decimal(str(C[t+1]))*(1+Decimal("0.001")); insufficient funds or ambiguous/missing fill aborts rather than assuming borrowing.
7. **Exit:** when confirmed LONG and no pending action, on the first eligible completed bar u after the BUY-fill bar with `state[u]==-1` (faithful to the source `if (is_falling) strategy.close("Norm Long")`), queue a full 0.001 BTC SELL for row u+1 at actual observed C[u+1], effective E[u+1]. No stop/target/trailing/time order exists in source; all are expressly disabled, not hidden defaults. The slope flip itself is the sole risk mechanism.
8. **State and priority:** exactly FLAT, BUY_PENDING, LONG, SELL_PENDING; one position and one pending action maximum. Rising and falling can never co-fire on one bar (strict complementary predicates with an equality hold); no tie-break is needed. Source default pyramiding=0 gives a single unit with no adds. On a pending/fill bar ignore new order signals but keep the state updating. On confirmed SELL, return to FLAT using the independent confirmed-fill inventory ledger and record last SELL-fill bar. Re-entry requires FLAT plus `state==+1` on a future bar (no cooldown). Never BUY and SELL on the same bar. If a fill fails, is partial, duplicated, stale or cannot be reconciled, abort the segment. At sample end, an unfilled pending signal remains unfilled; open inventory is marked only to the last actual completed close and not fictitiously liquidated.
9. **Disabled:** Pine next-bar default order semantics (adapted to the declared t+1 completed-close MARKET fill), futures leverage/margin, default quantity semantics, the six non-Ricker wavelet branches, `w_lvl≠3` levels, the source `/*backtest` stanza venue/period/balance, short/borrow leg (no short entry exists in source or derivative — the page prose phrase "long/short decisions" contradicts its own code and the code governs), stops/targets/trailing/time exits, pyramiding, DCA/safety orders, simultaneous markets/shared capital, partial exits, dynamic sizing/compounding, limit/maker fills, intrabar triggers, discretionary overrides, hidden executor risk defaults and forced end-of-sample close.

## Required data

Only one real Binance BTCUSDT spot 1d OHLC feed, no fitted models, external symbols, cross-asset shared capital, funding, order book, non-OHLCV features, second timeframe or future extrema. All decision inputs at t are C[t] and recursive cascade/state values from bars <=t completed by E[t]. A strict input validity and continuity check must precede the pinned engine's feature merge/dropna; if data cannot satisfy it, fail closed. Native Binance kline timestamp is the **open** time, never the completed-close availability or economic fill time.

## Execution assumptions

**Pinned source-code benchmark inspected at HCH725/hummingbot commit 8b0e067e80ab62f10846d518dcb5a8218527ddb3 on 2026-10-28:** the commit SHA, its date (2026-09-20) and `hummingbot/VERSION` = **dev-2.17.0** were verified via GitHub API and pinned raw fetch this round (package label **20260920** unchanged in the live admission contract). Four pinned raw files were byte-verified this round against prior independent review sizes: `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` (993), `hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py` (3,924), `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` (3,913), `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py` (8,823).

- **Data:** pinned `BinanceSpotCandles` constants declare the **1d** interval and read Binance REST `/api/v3/klines` opening timestamp plus actual OHLCV. Strict full-bar availability/continuity must be enforced before any feature dropna; a missing price is never substituted.
- **Controller/action path:** `BacktestingEngineBase.simulate_execution` iterates completed rows, calls `update_state(row)`, then `controller.determine_executor_actions()`, simulating CreateExecutorAction. A future minimal candidate-specific controller (not yet materialized) must retain the cascade/state values and FLAT/LONG/pending state and send the precommitted t signal on t+1 via OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY or SELL,amount=Decimal("0.001"),position_action=OPEN or CLOSE,execution_strategy=MARKET,price=None,leverage=1). The presence of this API is **not** alone the compatibility proof.
- **Observed fill primitive:** pinned OrderExecutorSimulator MARKET path fills at the first supplied candle with entry price taken from that row's actual close (`entry_price = df_filtered.loc[fill_timestamp, 'close']`), not a fabricated price, computes float(amount)*entry_price as filled quote and trade_cost*quote as fee, then returns CloseType.POSITION_HOLD. Dispatch at t+1 produces the declared idealized t+1 completed-close fill. It is not an achievable post-close live order guarantee; economic timestamp is E[t+1], even though native row timestamp is T[t+1].
- **Position and economics:** BacktestPositionHold aggregates BUY/SELL gross exposure and fees separately; native gross realized PnL is not net research PnL. Keep complete confirmed-executor history (terminated_executors_window=None or equivalent; the pinned default is only 3600 seconds) and a separate Decimal research cash/inventory ledger independent of BacktestPositionHold.is_closed. Start cash=10000 USDT, BTC=0; each confirmed BUY: cash -= Q*P*(1+f), inventory +=Q; each confirmed SELL: cash +=Q*P*(1-f), inventory -=Q, with Q=Decimal("0.001") and f=Decimal("0.001"). Net roundtrip realized =Q*(Ps-Pb)-f*Q*(Pb+Ps); record fees separately. This **0.1% quote-notional fee per side is hypothetical**, not a verified Binance fee tier; spot funding is not applicable, not invented perpetual funding=0. No compounding.
- **Float/Decimal precision boundary:** native simulator computes quote in float; BacktestPositionHold re-derives base quantity from Decimal(quote)/price and checks net_amount_base==0 exactly. Opposite equal configured amounts can leave sub-atomic dust; its is_closed flag and positions_held are **not** used as the derivative's authoritative FLAT/LONG or cash ledger. Confirmed OrderExecutorConfig amount and full-fill evidence determine exact research inventory Q; compare engine-derived residual to expected inventory only diagnostically with absolute tolerance 1e-12 BTC and abort if greater. This tolerance is a **researcher-declared diagnostic**, not an engine patch, live lot precision, or silent rounding of an order. Earlier independently reviewed Alpha PRs #519/#529/#530 record bounded synthetic primitive exercises at Q0.001, fee 0.001 and 1e-12 diagnostic tolerance; this record reuses that bounded pure-research primitive. No candidate-specific backtest or new primitive test is claimed here.
- **Pure-research precision contract:** deliberately no exchange lot/tick/min-notional/available-live-balance acceptance gating is claimed. This is an idealized fixed-quantity historical model, not an exchange-acceptable order assertion. Exchange trading rules, liquidity, spread, actual slippage, live fee tiers and real fills are out of scope; they must be independently verified before any deployment. The engine's BacktestingDataProvider.get_price_by_type fallback Decimal("1") on missing prices (re-verified this round) is **forbidden**; missing/nonpositive actual close, ambiguous full-fill, unbounded dust or incomplete fee/position ledger aborts the research segment.

## Evidence

### Source-reported

Public FMZ page `521670` (read this cycle): Mexican-Hat kernel `[-0.1, 0.0, 0.4, 0.8, 0.4, 0.0, -0.1]`, `w_lvl=3` three-level cascade with steps 1/2/4, slope rule `w_close > w_close[1]` long entry / `w_close < w_close[1]` position close, and the full 121-line Pine v5 program carrying one `strategy.entry`, one `strategy.close`, zero exits/orders, three inputs (two signal-relevant, one display-only), and the `/*backtest` venue stanza. The page's "40%"/"25%"/"outperforms MA" numerals are marketing prose without experiment provenance and are fenced off, not evidence. No sizing, warmup-cause, cost model, or profitability claim exists in the program; all such settings here are researcher-declared.

### Independently reproduced

No strategy backtest, Pine event parity, realized market fills, profits, Qlib parity, OOS, Survivor or HB Certified results. This cycle directly inspected the verbatim Pine v5 source from the public first-party page plus the immutable pinned Hummingbot feed/MARKET/POSITION_HOLD/fee source paths (SHA, date, VERSION and four file sizes re-verified this round), and reused prior independent primitive evidence (#519/#529/#530), not a candidate-specific test or installed-binary hash. Prior primitive validation does not imply that an unimplemented dedicated controller already exists.

- **Rule-logic self-check (stdlib only, not a backtest):** the frozen cascade/state plus the FLAT/LONG state machine were executed over the real-data replay below — all pass: equality prints route to hold; pre-validity bars stay silent crash-free; first valid `w_close` lands exactly at index 42 as derived (6+12+24); identical inputs give identical outputs across two runs (signal-series md5 `0b4ccd9efbc02b3ebc5242176e50460e` twice). Both legs provably reachable (129 entry-latches and 129 exit-latches).
- **Rule computability on real public data (availability check, not a backtest — no PnL, no returns computed):** 2,126 fully completed Binance BTCUSDT spot `1d` bars (2021-01-01 → 2026-10-27; the still-forming 2026-10-28 candle excluded) verified contiguous at exact 86400-second open steps with zero invalid OHLC bars; post-warmup evaluation yields 129 entry-latch bars and 129 exit-latch bars under the frozen rules. Worked latches: ENTRY 2021-03-02 (C 48440.65), EXIT 2021-03-13 (C 61188.39), ENTRY 2021-03-22 (C 54083.25), EXIT 2021-04-06 (C 57991.15). Terminal state is FLAT (last C 80909.77, slope −1) — no long held at the sample end. The candidate's trade events, Qlib/Hummingbot parity, and net returns have **not** been independently reproduced. No backtest was executed.

### Six-gate proposed PASS — independent Hermes Auditor decides

1. **Determinism:** literal 7-tap kernel, literal 1.4 normalization, pinned Ricker/level-3 cascade, strict-inequality slope state with equality-hold, warmup and priority.
2. **Direction:** BTCUSDT spot LONG/FLAT; no short entry exists in source or derivative (page-prose/code mismatch fenced with code governing).
3. **Entry/exit/risk:** slope-rising BUY, slope-falling SELL; no source stop/target/trailing/time order leg exists and all hidden defaults are expressly disabled (1-entry/1-close/0-exit census); the slope flip is the sole risk mechanism with no loss-cap claim.
4. **Position:** cash10000/Q0.001/fee0.001, single pending and inventory ledger, fail-closed fill reconciliation, re-entry only on a future bar while FLAT, no DCA or concurrency.
5. **Pinned compatibility:** actual 1d Binance spot feed, controller/action/next-row MARKET actual close, POSITION_HOLD gross-plus-fees and independently declared Decimal net ledger, pure-research precision/dust boundary; no unsupported next-open, intrabar, MTF or futures funding claim.
6. **Causality:** t>=60 completed-bar decision on C[t] and cascade/state values from bars <=t (max lag 42), t+1 completed-close fill effective E[t+1], opening timestamp not mistaken for completed data, no future leakage or synthetic prices.

### Negative evidence

No backtest, profitability, Qlib parity, OOS, Survivor or live-fill evidence is claimed. The source's own 2025-01-01→2025-12-15 backtest stanza is a venue/period stamp, not performance evidence, and is not reused. The six non-Ricker wavelet branches and `w_lvl≠3` levels are code-present but deliberately unexplored; any claim about them would be invention. Sibling slope-sign exposure shapes in the pool (below) are disclosed, not hidden.

**Dedup:** current main at `644ed23` has 401 root strategy Markdown records (README pool count 401, verified equal); full-tree case-sensitive grep for `wavelet`, `Mexican Hat`, `Ricker`, `521670`, `Wavelet Candlestick`, `wojlucz` returns zero same-source hits, and `harmonic`/`xabcd`/`gartley`/`markov` (the two rejected alternate lanes this cycle) likewise return zero strategy records. Nearest pool relatives trade different signal objects despite the shared slope-sign exposure shape: `tradingview-tasc-linreg40-slope-sign-long-flat` (40-bar linear-regression slope), `tradingview-systemsoverfeelings-kama40-slope-flip-close-bracket` (Kaufman adaptive average flip), `elder-impulse-dual-slope-state-flip-two-sided` (EMA-slope histogram state), `freqtrade-quickie-tema-slope-bbmid-adx-gated-long-flat` (TEMA-slope with BB/ADX gates), `vidya-cmo-adaptive-slope-trend` (VIDYA/CMO adaptive slope) — none is a fixed 43-tap negative-lobe wavelet FIR with strict smoothed-close slope comparison. All ten open research/* PR titles were checked (#353 Heracles KCD, #350 ClucMay72018, #331 AdxSmas, #304 forven CCI, #251 Swift 2yMA, #92 SSL channel, #89 Chandelier Exit, #63 SuperTrend flip, #49 Gauss StochRSI, #48 Larry Williams streak); none is FMZ-sourced or wavelet-based. Existing root records were not re-audited individually in this Scout; the 401/401 count census plus the merged-base diff shows only reviewed PASS additions and README bookkeeping, with no other strategy changes.

## Falsification plan

With separate authorization only, materialize the minimal candidate-specific controller and test the cascade seed first bars, the `sum_w` division guard, flat-tape hold behavior, the exact equality-hold boundary routing, state memory through long flat-slope stretches, slope re-entry after an exit while still FLAT, warmup-edge suppression at bars 59/60, pending-bar gate freezes, exact t/t+1 timing, observed prices, quote fees, separate Decimal inventory, float residual tolerance and end-of-sample treatment. Before large-scale Qlib screening of any new execution path, obtain representative event-level Hummingbot/Qlib parity. No such execution, deployment or backtest occurs in this Scout.

## Crypto portability

Native venue is already BTC-USDT (source stanza Futures_Binance); this derivative moves only the venue leg to Binance spot 1d with no leverage or funding. No asset substitution is made. Porting the Mexican-Hat level-3 slope state to other spot symbols would be a new derived version with its own evidence, not covered by this record.

## Limitations

Verbatim code comes from the FMZ first-party public page payload (byte-inspected this round: 4,674 bytes, md5 `a2143f58190a6fa0f29ae15e646cc4b8`); the page is publicly readable with no login, and no login-wall bypass was performed. The pure-research close/full-fill/fee model is not a real exchange acceptance or executable strategy implementation. The slope flip is bars late by construction (42-bar cascade seed) and the book has no protective stop — a grinding decline that never prints a smoothed downtick stays exposed. Turnover is moderate-high (129 entries per ~2,100 daily bars in the availability check; both legs proven reachable). The source `/*backtest` stanza granularity/venue is dropped in favor of the declared t+1 completed-close fill. The page's performance numerals are marketing prose, not evidence. No performance, survivor, live or Qlib parity claims.

## Implementation status

**implementation_status: not-implemented** — research record only. **status: research-only; adoption: not-approved; approval_scope: research-only.** The proposed PASS is not self-approval: independent Hermes Auditor GitHub Webhook Review alone owns source-fact review, exact-head PASS merge or NOT_LOSSLESS close. The existing signed webhook receiver alone owns post-merge README bookkeeping. This Scout does not approve, merge, close, modify main or change any trading/backtest/cron system.

## Adoption boundary

Research-only. Not approved for Paper, Testnet, Live, Qlib mass screening, or any deployment. Downstream use requires the independent PASS review plus separate implementation and authorization steps outside this record.

## Related Wiki records

None created by this Scout.

## Sources

- https://www.fmz.com/strategy/521670 — ianzeng123, first-party public page carrying the verbatim 121-line Pine v5 Wavelet program (kernel, cascade, slope entry/close, venue stanza), inspected 2026-10-28.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — immutable pinned engine paths inspected via the pinned tree this round (SHA/date/VERSION plus four file sizes and key lines re-verified).
- https://github.com/HCH725/alpha-strategy-research/pull/519 — prior independent bounded MARKET/POSITION_HOLD synthetic primitive review.
- https://github.com/HCH725/alpha-strategy-research/pull/529 — prior independent bounded pure-research execution and PASS-only census evidence.
- https://github.com/HCH725/alpha-strategy-research/pull/530 — prior independent PASS census evidence.
