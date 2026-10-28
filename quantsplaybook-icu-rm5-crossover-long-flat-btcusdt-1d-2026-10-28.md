---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "QuantsPlaybook ICU repeated-median (Siegel) 5-bar endpoint crossover long-flat BTCUSDT 1d independent derivative"
created: 2026-10-28
updated: 2026-10-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-03
sources:
  - https://github.com/hugo2046/QuantsPlaybook/tree/3f83a77f4c7996ed8185b8979a42c4372c1d811f/C-%E6%8B%A9%E6%97%B6%E7%B1%BB/ICU%E5%9D%87%E7%BA%BF
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# ICU repeated-median 5-bar endpoint crossover — BTCUSDT spot 1d long-flat derivative

## Provenance

- **Primary source (public GitHub, immutable):** hugo2046/QuantsPlaybook at commit `3f83a77f4c7996ed8185b8979a42c4372c1d811f` (committer date 2026-10-03T02:27:34Z, verified this cycle via GitHub API; still master HEAD). Strategy family `C-择时类/ICU均线` (ICU moving average timing under a Chinese brokerage report).
- **Verbatim files read end to end this cycle via immutable Contents API:** `C-择时类/ICU均线/src/icu_ma.py` (1,141 bytes, md5 `144b88dc803b746ee7e58df877dec1ce`), `C-择时类/ICU均线/src/bt_icu_ind.py` (889 bytes, md5 `1ec84f5034e31295f7664ddd33a6bf2a`), `C-择时类/ICU均线/src/bt_strategy.py` (2,736 bytes, md5 `0fe8e204568c1f7a8e1cf959b90e09e4`). Only rule tokens are normalized and cited here; no large source block is copied (the repository carries no license file).
- **Notebook and report lineage:** `C-择时类/ICU均线/ICU_MA.ipynb` (398,916 bytes, 23 cells, read this cycle) states the cross rule `Buy_t if Price_t > ICUMVG_t and Price_{t-1} < ICUMVG_{t-1}` / `sell_t` mirror, works the example with **past-5-trading-day rolling ICU**, and carries the研报 reference `参考/20230412_中泰证券_「均线」才是绝对收益利器-ICU均线下的择时策略.pdf`. Both code defaults pin N=5 (`IcuMaInd params N=5`, `CrossOverStrategy params periods=5`).
- **Researcher-defined derivative v1, NOT source-native:** preserve the exact Siegel hierarchical repeated-median endpoint definition and strict cross comparison, but trade Binance **BTCUSDT spot** UTC **1d** LONG/FLAT with fixed 0.001 BTC, 10,000 USDT cash, hypothetical 0.1% fee per side, t-signal to t+1 completed-close MARKET fills, and first eligible decision t=5. This drops the 沪深300 venue, backtrader `order_target_percent(0.95)`/`close()` sizing, backtrader commission/slippage stamp (万1滑点, 佣金万3, 印花税千1), and resolves the source's own T-close vs T+1-open timing conflict (below) in favor of a disclosed t+1 close adaptation. These choices **materially change** original trade economics.
- **Frozen independent identity:** GH:QuantsPlaybook|3f83a77|ICU-RM5|derived-v1-20261028|BinanceSpot-BTCUSDT-UTC1d|Siegel-hierarchical-x0to4|endpoint-cross-strict|t-to-tplus1-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-each-side|first-decision-t5. Any decision-critical alteration creates a new derived version, not a silent update.

## Economic mechanism

### Source-reported

A 5-day robust-regression endpoint (repeated median, 50% breakdown point) tracks the price level without OLS outlier pull; a price-over-endpoint cross is the timing signal for absolute-return择时. The notebook's own words: price up-cross buys, price down-cross sells flat; the 5-day window is the worked example. No protective stop, target, trailing, or time exit exists in the strategy code.

### Research interpretation

This derivative is long only while the last completed cross was bullish and flat after the first bearish cross — a pure level-cross state hold on a 5-bar robust endpoint, not a slope-sign trade, not a band touch, and not a contrarian envelope fade. The repeated-median endpoint is discontinuous by construction (median of medians), so crosses fire often and holding periods are short; the only risk control is the opposite cross, so a grinding decline that never prints a down-cross stays exposed.

## Signal

1. **Input and availability:** one chronological, contiguous sequence of actual Binance BTCUSDT spot UTC **1d** candles indexed t=0,1,... . Native opening time T[t] must be UTC midnight-aligned and T[t+1]-T[t]=86400 seconds. Require finite positive O,H,L,C, H>=max(O,C), L<=min(O,C); volume is unused and unchecked. Reject duplicates, gaps, out-of-order bars, missing/zero/nonfinite observed prices or incomplete candles; never interpolate or forward-fill. Completed bar t is available at E[t]=T[t]+86400, not T[t]. Float64 chronological arithmetic, no intermediate rounding. Only the **close** series is consumed by the decision.
2. **Constants (researcher-pinned to source defaults):** `N=5` pinned (two code defaults plus the notebook past-5-day example; the notebook's separate N-search cells are disclosed under Limitations and not adopted). x-coordinates `x=0,1,2,3,4` pinned (icu_ma.py passes `np.arange(n)` explicitly; bt_icu_ind.py omits x which defaults to the same arange under scipy semantics — pinned here explicitly). Method `hierarchical` pinned (icu_ma.py explicit; bt_icu_ind.py relies on the scipy default, pinned here explicitly).
3. **Siegel hierarchical endpoint (all bars, causal only):** for window `W=C[t-4..t]` with x=0..4: per-j `m_j=median_{i!=j}(W_j-W_i)/(j-i)` via stdlib `statistics.median`; `slope=median_j(m_j)`; `intercept=median_i(W_i-slope*i)`; `ICU[t]=intercept+slope*4`. ICU[0..3] are undefined (never invented). The `bt_icu_ind.py` `except→icu[0]=0` fallback is **forbidden**; any nonfinite window aborts the bar fail-closed instead of printing a zero that would fabricate a cross.
4. **Cross (strict inequalities, equality holds):** bull latch `C[t]>ICU[t] and C[t-1]<ICU[t-1]`; bear latch `C[t]<ICU[t] and C[t-1]>ICU[t-1]`. Equality on either side fires nothing and holds existing position/pending action. No confirmation bar, no second indicator, no threshold band.
5. **First decision:** t=5 is the first crossable bar (first ICU at index 4, first comparable pair 4/5). Bars 0..4 are indicator seed, never orders. No extra researcher warmup margin is added.
6. **Entry:** when FLAT with no pending action, t>=5, t strictly later than the last SELL-fill bar, and a bull latch at t, queue exactly one BUY. Dispatch on row t+1 only, independently of that row's signal, and model a full 0.001 BTC MARKET fill at its **actual observed completed close** C[t+1], effective E[t+1]. No t+1 price or indicator is used to decide at t. If row t+1 does not exist, leave unfilled. Require cash >=Decimal("0.001")*Decimal(str(C[t+1]))*(1+Decimal("0.001")); insufficient funds or ambiguous/missing fill aborts rather than assuming borrowing.
7. **Exit:** when confirmed LONG and no pending action, on the first eligible completed bar u after the BUY-fill bar with a bear latch at u, queue a full 0.001 BTC SELL for row u+1 at actual observed C[u+1], effective E[u+1]. No stop/target/trailing/time order exists in source; all are expressly disabled, not hidden defaults. The opposite cross itself is the sole risk mechanism.
8. **State and priority:** exactly FLAT, BUY_PENDING, LONG, SELL_PENDING; one position and one pending action maximum. Bull and bear can never co-fire on one bar (strict complementary crosses); no tie-break is needed. Single unit with no adds (source `order_target_percent`/`close()` with `if not position / elif` admits no pyramiding). On a pending/fill bar ignore new order signals but keep ICU/cross updating. On confirmed SELL, return to FLAT using the independent confirmed-fill inventory ledger and record last SELL-fill bar. Re-entry requires FLAT plus a future bull latch (no cooldown). Never BUY and SELL on the same bar. If a fill fails, is partial, duplicated, stale or cannot be reconciled, abort the segment. At sample end, an unfilled pending signal remains unfilled; open inventory is marked only to the last actual completed close and not fictitiously liquidated.
9. **Disabled:** backtrader sizing/commission/slippage/stampDuty semantics, the notebook's T-close idealized fill, short/borrow leg (no short exists in source or derivative), stops/targets/trailing/time exits, pyramiding, DCA/safety orders, simultaneous markets/shared capital, partial exits, dynamic sizing/compounding, limit/maker fills, intrabar triggers, the `except→0` fallback, discretionary overrides, hidden executor risk defaults and forced end-of-sample close.

## Required data

Only one real Binance BTCUSDT spot 1d OHLC feed, no fitted models, external symbols, cross-asset shared capital, funding, order book, non-OHLCV features, second timeframe or future extrema. All decision inputs at t are C[t-4..t] and recursive ICU/cross values from bars <=t completed by E[t]. A strict input validity and continuity check must precede the pinned engine's feature merge/dropna; if data cannot satisfy it, fail closed. Native Binance kline timestamp is the **open** time, never the completed-close availability or economic fill time.

## Execution assumptions

**Pinned source-code benchmark inspected at HCH725/hummingbot commit 8b0e067e80ab62f10846d518dcb5a8218527ddb3 on 2026-10-28:** the commit SHA, its date (2026-09-20) and `hummingbot/VERSION` = **dev-2.17.0** were verified via GitHub API and pinned raw fetch this round (package label **20260920** unchanged in the live admission contract). Four pinned raw files were byte-verified this round against prior independent review sizes: `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` (993), `hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py` (3,924), `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` (3,913), `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py` (8,823). Key lines re-verified: MARKET `entry_price = df_filtered.loc[fill_timestamp, 'close']` (line 56), `CloseType.POSITION_HOLD` (line 70), `Decimal("1")` missing-price fallback (forbidden here), and the `1d` interval declaration.

- **Data:** pinned `BinanceSpotCandles` constants declare the **1d** interval and read Binance REST `/api/v3/klines` opening timestamp plus actual OHLCV. Strict full-bar availability/continuity must be enforced before any feature dropna; a missing price is never substituted.
- **Controller/action path:** `BacktestingEngineBase.simulate_execution` iterates completed rows, calls `update_state(row)`, then `controller.determine_executor_actions()`, simulating CreateExecutorAction. A future minimal candidate-specific controller (not yet materialized) must retain the 5-bar window/ICU/cross values and FLAT/LONG/pending state and send the precommitted t signal on t+1 via OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY or SELL,amount=Decimal("0.001"),position_action=OPEN or CLOSE,execution_strategy=MARKET,price=None,leverage=1). The presence of this API is **not** alone the compatibility proof.
- **Observed fill primitive:** pinned OrderExecutorSimulator MARKET path fills at the first supplied candle with entry price taken from that row's actual close, not a fabricated price, computes float(amount)*entry_price as filled quote and trade_cost*quote as fee, then returns CloseType.POSITION_HOLD. Dispatch at t+1 produces the declared idealized t+1 completed-close fill. It is not an achievable post-close live order guarantee; economic timestamp is E[t+1], even though native row timestamp is T[t+1]. This **adapts** the source code's T+1-open fill (`T日收盘产生信号,T+1日开盘买入` / `以下一日开盘价卖出`) from open to close and **delays** the notebook's idealized T-close fill (`出现信号立刻以收盘价买入` / `T日信号T日close买入`) by one bar; both deviations are disclosed derivative choices, not lossless reproduction.
- **Position and economics:** BacktestPositionHold aggregates BUY/SELL gross exposure and fees separately; native gross realized PnL is not net research PnL. Keep complete confirmed-executor history (terminated_executors_window=None or equivalent; the pinned default is only 3600 seconds) and a separate Decimal research cash/inventory ledger independent of BacktestPositionHold.is_closed. Start cash=10000 USDT, BTC=0; each confirmed BUY: cash -= Q*P*(1+f), inventory +=Q; each confirmed SELL: cash +=Q*P*(1-f), inventory -=Q, with Q=Decimal("0.001") and f=Decimal("0.001"). Net roundtrip realized =Q*(Ps-Pb)-f*Q*(Pb+Ps); record fees separately. This **0.1% quote-notional fee per side is hypothetical**, not a verified Binance fee tier; spot funding is not applicable, not invented perpetual funding=0. No compounding.
- **Float/Decimal precision boundary:** native simulator computes quote in float; BacktestPositionHold re-derives base quantity from Decimal(quote)/price and checks net_amount_base==0 exactly. Opposite equal configured amounts can leave sub-atomic dust; its is_closed flag and positions_held are **not** used as the derivative's authoritative FLAT/LONG or cash ledger. Confirmed OrderExecutorConfig amount and full-fill evidence determine exact research inventory Q; compare engine-derived residual to expected inventory only diagnostically with absolute tolerance 1e-12 BTC and abort if greater. This tolerance is a **researcher-declared diagnostic**, not an engine patch, live lot precision, or silent rounding of an order. Earlier independently reviewed Alpha PRs #519/#529/#530 record bounded synthetic primitive exercises at Q0.001, fee 0.001 and 1e-12 diagnostic tolerance; this record reuses that bounded pure-research primitive. No candidate-specific backtest or new primitive test is claimed here.
- **Pure-research precision contract:** deliberately no exchange lot/tick/min-notional/available-live-balance acceptance gating is claimed. This is an idealized fixed-quantity historical model, not an exchange-acceptable order assertion. Exchange trading rules, liquidity, spread, actual slippage, live fee tiers and real fills are out of scope; they must be independently verified before any deployment. The engine's BacktestingDataProvider.get_price_by_type fallback Decimal("1") on missing prices (re-verified this round) is **forbidden**; missing/nonpositive actual close, ambiguous full-fill, unbounded dust or incomplete fee/position ledger aborts the research segment.

## Evidence

### Source-reported

Pinned GitHub files (read this cycle): `icu_ma.py` defines `siegelslopes_ma` via `scipy.stats.siegelslopes(price_ser, np.arange(n), method="hierarchical")` returning `intercept+slope*(n-1)` and `calc_icu_ma` as `price.rolling(N).apply(...)`; `bt_icu_ind.py` pins `N=5` and computes `stats.siegelslopes(close_N)` returning `intercept+slope*(N-1)` with an `except→icu[0]=0` fallback; `bt_strategy.py` pins `periods=5`, documents `T日收盘产生信号,T+1日开盘买入` with `以下一日开盘价卖出`, and trades `CrossOver(close, signal)` via `order_target_percent(0.95)`/`close()` with no stop/target/trailing/time leg. The notebook states the strict cross formula, the past-5-day rolling example, and the idealized `T日信号T日close买入` convention alongside backtrader cost stamps. No sizing beyond 0.95-target, no warmup-cause, no profitability claim is adopted from the program.

### Independently reproduced

No strategy backtest, Pine event parity, realized market fills, profits, Qlib parity, OOS, Survivor or HB Certified results. This cycle directly inspected the verbatim strategy sources from the immutable pinned commit plus the immutable pinned Hummingbot feed/MARKET/POSITION_HOLD/fee source paths (SHA, date, VERSION and four file sizes re-verified this round), and reused prior independent primitive evidence (#519/#529/#530), not a candidate-specific test or installed-binary hash. Prior primitive validation does not imply that an unimplemented dedicated controller already exists.

- **Rule-logic self-check (stdlib only, not a backtest):** the frozen hierarchical endpoint plus the FLAT/LONG state machine were executed over the real-data replay below — all pass: equality prints route to hold; pre-validity bars stay silent crash-free; first valid ICU lands exactly at index 4 as derived; identical inputs give identical outputs across two runs (signal-series md5 `df2c199f7a7aedf98484bc06d479ced5` twice). Both legs provably reachable (222 bull latches and 222 bear latches).
- **Rule computability on real public data (availability check, not a backtest — no PnL, no returns computed):** 2,126 fully completed Binance BTCUSDT spot `1d` bars (2021-01-01 → 2026-10-27; the still-forming 2026-10-28 candle excluded) verified contiguous at exact 86400-second open steps with zero invalid OHLC bars; post-seed evaluation yields 222 bull-latch bars and 222 bear-latch bars under the frozen rules. Worked latches: ENTRY 2021-01-17 (C 35828.61, ICU 35538.18), EXIT 2021-01-08 (C 40582.81, ICU 41721.83), ENTRY 2021-01-28 (C 33364.86, ICU 32675.64), EXIT 2021-01-15 (C 36742.22, ICU 40127.95). Simulated t+1-close state execution over the same sample fills 274 side-events and ends FLAT (last C 80909.77) — no long held at the sample end. The candidate's trade events, Qlib/Hummingbot parity, and net returns have **not** been independently reproduced. No backtest was executed.

### Six-gate proposed PASS — independent Hermes Auditor decides

1. **Determinism:** literal N=5, literal x=0..4, literal hierarchical repeated-median formula, strict-inequality cross with equality-hold, first-decision index and priority.
2. **Direction:** BTCUSDT spot LONG/FLAT; no short entry exists in source or derivative.
3. **Entry/exit/risk:** bull-cross BUY, bear-cross SELL; no source stop/target/trailing/time order leg exists and all hidden defaults are expressly disabled (0-exit/stop census in strategy code); the opposite cross is the sole risk mechanism with no loss-cap claim.
4. **Position:** cash10000/Q0.001/fee0.001, single pending and inventory ledger, fail-closed fill reconciliation, re-entry only on a future bar while FLAT, no DCA or concurrency.
5. **Pinned compatibility:** actual 1d Binance spot feed, controller/action/next-row MARKET actual close, POSITION_HOLD gross-plus-fees and independently declared Decimal net ledger, pure-research precision/dust boundary; no unsupported next-open, intrabar, MTF or futures funding claim.
6. **Causality:** t>=5 completed-bar decision on C[t-4..t] and ICU/cross values from bars <=t (max lag 4), t+1 completed-close fill effective E[t+1], opening timestamp not mistaken for completed data, no future leakage or synthetic prices.

### Negative evidence

No backtest, profitability, Qlib parity, OOS, Survivor or live-fill evidence is claimed. The notebook's N-search cells (`N: arange(5,205,5)`, GFO 20 iterations on 沪深300) mean N=5 may reflect tuning, not a proven optimum; it is pinned here only by the two code defaults plus the past-5-day example, and the auditor decides whether that suffices. The source's T-close vs T+1-open conflict is fenced with both wordings preserved and the derivative's t+1-close choice disclosed. Turnover is high by construction (222 latches per ~2,100 daily bars; 274 side-fills under state gating). Sibling regression exposure shapes in the pool (below) are disclosed, not hidden.

**Dedup:** current main at `bcb2c1d` has 403 root strategy Markdown records (README pool count 403, verified equal: 405 `*.md` minus two READMEs). Full-tree case-sensitive grep for `siegelslopes`, `Repeated Median`, `重复中位数`, `ICU均线`, `icu_ma`, `ICU_MA` returns zero strategy records; `QuantsPlaybook` matches only `qrs-penalized-rsrs-zscore-timing` (cross-sectional RSRS slope timing) and `quantsplaybook-price-volume-resonance` (HMA price-volume product with dual thresholds) — different notebooks and mechanisms. Nearest pool relatives trade different signal objects despite the shared regression/long-flat shape: `tradingview-tasc-linreg40-slope-sign` (40-bar OLS slope sign), `nw-endpoint-envelope-contrarian` (Gaussian-kernel endpoint envelope fade), `linreg-channel-band-touch` / `forven-linreg-channel-breakout` (OLS channel rails) — none is a 5-bar Siegel repeated-median endpoint with a strict price-vs-endpoint cross. All ten open research/* PR titles were checked (#353 Heracles KCD, #350 ClucMay72018, #331 AdxSmas, #304 forven CCI, #251 Swift 2yMA, #92 SSL channel, #89 Chandelier Exit, #63 SuperTrend flip, #49 Gauss StochRSI, #48 Larry Williams streak); none is QuantsPlaybook-ICU or robust-endpoint based. Existing root records were not re-audited individually in this Scout; the 403/403 count census plus the merged-base diff shows only reviewed PASS additions and README bookkeeping, with no other strategy changes.

## Falsification plan

With separate authorization only, materialize the minimal candidate-specific controller and test the N=5 seed first bars, the `except→0` fail-closed boundary, flat-tape hold behavior, the exact equality-hold boundary routing, state memory through consecutive same-side crosses, re-entry after an exit while still FLAT, first-decision-edge behavior at bars 4/5, pending-bar gate freezes, exact t/t+1 timing, observed prices, quote fees, separate Decimal inventory, float residual tolerance and end-of-sample treatment. Before large-scale Qlib screening of any new execution path, obtain representative event-level Hummingbot/Qlib parity. No such execution, deployment or backtest occurs in this Scout.

## Crypto portability

Native venue is 沪深300 daily bars; this derivative moves only the venue leg to Binance BTCUSDT spot 1d with no leverage or funding. No asset substitution beyond this single declared market is made. Porting the RM5 endpoint cross to other spot symbols would be a new derived version with its own evidence, not covered by this record.

## Limitations

Verbatim code comes from the immutable public commit payload (byte-inspected this round: 1,141/889/2,736 bytes with md5s pinned above); no login-wall bypass was performed. The repository has no license file, so only rule tokens are normalized here. The pure-research close/full-fill/fee model is not a real exchange acceptance or executable strategy implementation. The opposite cross is bars late by construction and the book has no protective stop — a grinding decline that never prints a bear cross stays exposed. Turnover is high (222 latches per ~2,100 daily bars; both legs proven reachable). The source T-close/T+1-open conflict and the notebook N-search are disclosed above and not resolved by invention. No performance, survivor, live or Qlib parity claims.

## Implementation status

**implementation_status: not-implemented** — research record only. **status: research-only; adoption: not-approved; approval_scope: research-only.** The proposed PASS is not self-approval: independent Hermes Auditor GitHub Webhook Review alone owns source-fact review, exact-head PASS merge or NOT_LOSSLESS close. The existing signed webhook receiver alone owns post-merge README bookkeeping. This Scout does not approve, merge, close, modify main or change any trading/backtest/cron system.

## Adoption boundary

Research-only. Not approved for Paper, Testnet, Live, Qlib mass screening, or any deployment. Downstream use requires the independent PASS review plus separate implementation and authorization steps outside this record.

## Related Wiki records

None created by this Scout.

## Sources

- https://github.com/hugo2046/QuantsPlaybook/tree/3f83a77f4c7996ed8185b8979a42c4372c1d811f/C-%E6%8B%A9%E6%97%B6%E7%B1%BB/ICU%E5%9D%87%E7%BA%BF — hugo2046, public strategy family carrying the verbatim RM5 endpoint and crossover sources plus notebook/report lineage, inspected 2026-10-28 at pinned commit 3f83a77.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — immutable pinned engine paths inspected via the pinned tree this round (SHA/date/VERSION plus four file sizes and key lines re-verified).
- https://github.com/HCH725/alpha-strategy-research/pull/519 — prior independent bounded MARKET/POSITION_HOLD synthetic primitive review.
- https://github.com/HCH725/alpha-strategy-research/pull/529 — prior independent bounded pure-research execution and PASS-only census evidence.
- https://github.com/HCH725/alpha-strategy-research/pull/530 — prior independent PASS census evidence.
