---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "TradingView KrisWaters smoothed ROC trough volume-gated reversal long-flat BTCUSDT 4h independent derivative"
created: 2026-10-28
updated: 2026-10-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2019-12-05
sources:
  - https://www.tradingview.com/script/30AJfvAa-Mean-Reversion-Strategy-by-KrisWaters/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Smoothed ROC trough volume-gated reversal — BTCUSDT spot 4h long-flat derivative

## Provenance

- **Primary source (public TradingView page, read this cycle):** `Mean Reversion Strategy by KrisWaters`, author `kriswaters`, stable URL `https://www.tradingview.com/script/30AJfvAa-Mean-Reversion-Strategy-by-KrisWaters/`. Page fetched this cycle over plain HTTPS: HTTP 200, 707,581 bytes. Author prose (page `<meta name="description">`, verbatim): "This is a type of mean reversion strategy. It only generates long signals when the price is far away from the mean. It tries buy from the dip. Use it with BTC/USDT pair on 4 hour timeframe." Pair (`BTC/USDT`) and timeframe (`4 hour`) are source-text explicit, not reviewer-chosen.
- **Immutable Pine payload (byte-verified this cycle):** pine-facade `PUB;3pfvAh8BpsmL2N4MQVk8Jiq3s4QKa3ft` (the same PUB id embedded in the fetched page HTML), `get/.../last/`, version **1.0**, `created == updated == 2019-12-05T07:20:59.978687Z` (never revised since publication), `scriptAccess=open_no_auth`, `kind=strategy`, `is_price_study=false`. Source 1,160 bytes, sha256 `81a0746804befa2b3cefcc8a9b5a72276e1cce6302f75ed6a7c9a6db953142f2`. Pine header `// © kriswaters`, `//@version=4`, MPL-2.0 license line. Only rule tokens are normalized and cited here; no large source block is copied.
- **Source declares `strategy(...)`, with a full order census:** `strategy(` 1, `strategy.entry` 1 (`"buy"`, `strategy.long`), `strategy.close` 1 (`"buy"`), `strategy.short` 0, `strategy.exit` 0, `stop=`/`limit=`/`profit=`/`loss=` 0, `pyramiding=0` declared in the live `strategy()` call (not a comment), `process_orders_on_close` 0, `request.`/`security(`/`timeframe`/calendar/`barstate` 0, `input(` 2 (`maPeriod=6`, `dropRate=1.0` float step 0.1), `sma(` 1, `change(` 1. Commission is source-declared: percent-of-equity 100%, `commission_value=0.075` (% per side), `initial_capital=1000`, `currency='USD'`. No stop, target, trailing, time exit, or date gate exists anywhere in the payload.
- **Researcher-defined derivative v1, NOT source-native:** preserve the exact smoothed-ROC trough, volume-gate, strict-inequality and flat/long state rules, but trade Binance **BTCUSDT spot** UTC **4h** LONG/FLAT with fixed 0.001 BTC, 10,000 USDT cash, 0.075% fee per side (adopted from the source's own commission declaration), t-signal to t+1 completed-close MARKET fills, and a 20-bar FLAT warmup. This drops the 100%-equity compounding sizing and maps Pine's default next-bar fill onto the pinned completed-close path. These choices **materially change** original trade economics.
- **Frozen independent identity:** TV:30AJfvAa|PUB:3pfvAh8BpsmL2N4MQVk8Jiq3s4QKa3ft|KWROC|derived-v1-20261028|BinanceSpot-BTCUSDT-UTC4h|ma6-drop1.0-curCloseDiv|trough-volgate-latch|t-to-tplus1-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.00075-each-side|warmup20. Any decision-critical alteration creates a new derived version, not a silent update.

## Economic mechanism

### Source-reported

A 1-bar percent-change series smoothed by a 6-bar SMA forms a mean-reversion oscillator; a long fires only when the oscillator is rising out of a trough deeper than −1% while volume is rising bar-over-bar. The position closes only when the oscillator has turned positive while volume is falling bar-over-bar. No protective stop, target, trailing, or time exit exists anywhere in the payload.

### Research interpretation

This derivative is long only inside dip-recovery episodes (entered on the first rising-trough bar after the oscillator printed below −1%) and flat after the oscillator recrosses above zero on shrinking volume — a pure oscillator-plus-volume state hold, not a moving-average cross, not a band touch, and not a price-level breakout. Volume acts as confirmation on both legs (expansion to enter, contraction to exit); the only risk control is the opposite signal, so a grinding decline whose oscillator never recrosses zero while volume keeps expanding stays exposed.

## Signal

1. **Input and availability:** one chronological, contiguous sequence of actual Binance BTCUSDT spot UTC **4h** candles indexed t=0,1,... . Native opening time T[t] must be UTC 4h-aligned and T[t+1]-T[t]=14400 seconds. Require finite positive O,H,L,C, H>=max(O,C), L<=min(O,C), finite nonnegative V (base-asset volume as printed). Reject duplicates, gaps, out-of-order bars, missing/zero/nonfinite observed prices or incomplete candles; never interpolate or forward-fill. Completed bar t is available at E[t]=T[t]+14400, not T[t]. Float64 chronological arithmetic, no intermediate rounding. Only the **close** and **volume** series are consumed by the decision.
2. **Constants (researcher-pinned to payload defaults):** `maPeriod=6`, `dropRate=1.0` pinned (the payload's two `input()` defaults; the source menu is fenced, not adopted).
3. **Smoothed ROC (Pine-literal, divisor pinned):** `rateOfChange[t] = 100*(C[t]-C[t-1])/C[t]` for t>=1, na at t=0. Note the divisor is the **current** close `C[t]`, not `C[t-1]` — pinned literally, never "corrected" to the textbook ROC form. `changeMovAvg[t]` = arithmetic mean of `rateOfChange[t-5..t]` requiring all six finite (strict 6-valid window); na otherwise. First valid value lands at index 6 (verified in the replay below). Pine's early-bar na-skipping nuance is fenced by the warmup: this derivative never trades before t=20, so bars 0..19 are indicator seed only (disclosed researcher pin — see Limitations).
4. **Entry latch (verbatim, strict inequalities):** at t>=20 while FLAT with no pending action and t strictly later than the last SELL-fill bar: `changeMovAvg[t] > changeMovAvg[t-1] AND changeMovAvg[t-1] < (-1)*1.0 AND V[t-1] < V[t]`. Equality on any leg blocks entry (rising test, −1% depth test, and volume-expansion test are all strict). Queue exactly one BUY. Dispatch on row t+1 only, independently of that row's signal, and model a full 0.001 BTC MARKET fill at its **actual observed completed close** C[t+1], effective E[t+1]. No t+1 price, oscillator, or volume is used to decide at t. If row t+1 does not exist, leave unfilled. Require cash >=Decimal("0.001")*Decimal(str(C[t+1]))*(1+Decimal("0.00075")); insufficient funds or ambiguous/missing fill aborts rather than assuming borrowing.
5. **Exit latch (verbatim, strict inequalities):** when confirmed LONG and no pending action, on the first completed bar u after the BUY-fill bar with `changeMovAvg[u] > 0 AND V[u-1] > V[u]`, queue a full 0.001 BTC SELL for row u+1 at actual observed C[u+1], effective E[u+1]. No stop/target/trailing/time order exists in the payload; all are expressly disabled, not hidden defaults. The opposite signal itself is the sole risk mechanism.
6. **State and priority:** exactly FLAT, BUY_PENDING, LONG, SELL_PENDING; one position and one pending action maximum. Single unit with no adds (`pyramiding=0` is source-declared). The `strategy.position_size==0/>0` reads in the payload are provably equivalent to FLAT/LONG gates under single-unit no-add semantics and are implemented as explicit state gates. On a pending/fill bar ignore new order signals but keep oscillator/volume updating. On confirmed SELL, return to FLAT using the independent confirmed-fill inventory ledger and record last SELL-fill bar. Re-entry requires FLAT plus a future trough latch; no cooldown exists in the payload (explicitly none, not invented). Never BUY and SELL on the same bar (entry requires FLAT, exit requires LONG — mutually exclusive by construction, no tie-break needed). If a fill fails, is partial, duplicated, stale or cannot be reconciled, abort the segment. At sample end, an unfilled pending signal remains unfilled; open inventory is marked only to the last actual completed close and not fictitiously liquidated.
7. **Disabled:** 100%-equity compounding sizing, Pine default next-bar-open fill, source menu beyond pinned defaults, short/borrow leg, stops/targets/trailing/time exits, pyramiding, DCA/safety orders, simultaneous markets/shared capital, partial exits, dynamic sizing, limit/maker fills, intrabar triggers, discretionary overrides, hidden executor risk defaults and forced end-of-sample close.

## Required data

Only one real Binance BTCUSDT spot 4h OHLCV feed, no fitted models, external symbols, cross-asset shared capital, funding, order book, non-OHLCV features, second timeframe or future extrema. All decision inputs at t are C[0..t] and V[0..t] through the causal ROC/SMA chain from bars <=t completed by E[t]. A strict input validity and continuity check must precede the pinned engine's feature merge/dropna; if data cannot satisfy it, fail closed. Native Binance kline timestamp is the **open** time, never the completed-close availability or economic fill time. TV-chart volume versus Binance printed base-volume substitution is disclosed in Limitations.

## Execution assumptions

**Pinned source-code benchmark inspected at HCH725/hummingbot commit 8b0e067e80ab62f10846d518dcb5a8218527ddb3 on 2026-10-28:** the commit SHA and `hummingbot/VERSION` = **dev-2.17.0** (11 bytes) were verified via pinned raw fetch this round (package label **20260920** unchanged in the live admission contract). Three pinned raw files were byte-verified this round: `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` (993, `4h` declared in INTERVALS), `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` (3,913), `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py` (8,823). Key lines re-verified: MARKET `entry_price = df_filtered.loc[fill_timestamp, 'close']` (line 56), `CloseType.POSITION_HOLD` (line 70), and the `Decimal("1")` missing-price fallback in `get_price_by_type` (forbidden here).

- **Data:** pinned `BinanceSpotCandles` reads Binance REST `/api/v3/klines` opening timestamp plus actual OHLCV on the **4h** interval. Strict full-bar availability/continuity must be enforced before any feature dropna; a missing price is never substituted.
- **Controller/action path:** `BacktestingEngineBase.simulate_execution` iterates completed rows, calls `update_state(row)`, then `controller.determine_executor_actions()`, simulating CreateExecutorAction. A future minimal candidate-specific controller (not yet materialized) must retain the ROC/SMA values and FLAT/LONG/pending state and send the precommitted t signal on t+1 via OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY or SELL,amount=Decimal("0.001"),position_action=OPEN or CLOSE,execution_strategy=MARKET,price=None,leverage=1). The presence of this API is **not** alone the compatibility proof.
- **Observed fill primitive:** pinned OrderExecutorSimulator MARKET path fills at the first supplied candle with entry price taken from that row's actual close, not a fabricated price, computes float(amount)*entry_price as filled quote and trade_cost*quote as fee, then returns CloseType.POSITION_HOLD. Dispatch at t+1 produces the declared idealized t+1 completed-close fill. It is not an achievable post-close live order guarantee; economic timestamp is E[t+1], even though native row timestamp is T[t+1]. This **adapts** Pine's default next-bar fill into a disclosed completed-close derivative choice, not lossless reproduction.
- **Position and economics:** BacktestPositionHold aggregates BUY/SELL gross exposure and fees separately; native gross realized PnL is not net research PnL. Keep complete confirmed-executor history (terminated_executors_window=None or equivalent) and a separate Decimal research cash/inventory ledger independent of BacktestPositionHold.is_closed. Start cash=10000 USDT, BTC=0; each confirmed BUY: cash -= Q*P*(1+f), inventory +=Q; each confirmed SELL: cash +=Q*P*(1-f), inventory -=Q, with Q=Decimal("0.001") and f=Decimal("0.00075") (adopted from the source's own 0.075% commission declaration, applied per side as a hypothetical research cost). Net roundtrip realized =Q*(Ps-Pb)-f*Q*(Pb+Ps); record fees separately. This fee is a **hypothetical research convention**, not a verified Binance fee tier; spot funding is not applicable, not invented perpetual funding=0. No compounding (the source's 100%-equity sizing is fenced, never adopted).
- **Float/Decimal precision boundary:** native simulator computes quote in float; BacktestPositionHold re-derives base quantity from Decimal(quote)/price and checks net_amount_base==0 exactly. Opposite equal configured amounts can leave sub-atomic dust; its is_closed flag and positions_held are **not** used as the derivative's authoritative FLAT/LONG or cash ledger. Confirmed OrderExecutorConfig amount and full-fill evidence determine exact research inventory Q; compare engine-derived residual to expected inventory only diagnostically with absolute tolerance 1e-12 BTC and abort if greater. This tolerance is a **researcher-declared diagnostic**, not an engine patch, live lot precision, or silent rounding of an order. Earlier independently reviewed Alpha PRs #519/#529/#530 record bounded synthetic primitive exercises at Q0.001 and 1e-12 diagnostic tolerance; this record reuses that bounded pure-research primitive shape with the source-declared 0.00075 fee substituted and disclosed. No candidate-specific backtest or new primitive test is claimed here.
- **Pure-research precision contract:** deliberately no exchange lot/tick/min-notional/available-live-balance acceptance gating is claimed. This is an idealized fixed-quantity historical model, not an exchange-acceptable order assertion. Exchange trading rules, liquidity, spread, actual slippage, live fee tiers and real fills are out of scope; they must be independently verified before any deployment. The engine's `get_price_by_type` fallback Decimal("1") on missing prices (re-verified this round) is **forbidden**; missing/nonpositive actual close, ambiguous full-fill, unbounded dust or incomplete fee/position ledger aborts the research segment.

## Evidence

### Source-reported

Pinned facade payload (read end to end this cycle): `strategy()` declaration with `pyramiding=0`, two `input()` defaults (6/1.0), current-close-divisor `rateOfChange`, 6-bar `sma`, one `strategy.entry("buy", strategy.long)` leg gated on rising-trough-plus-volume-expansion plus flat state, one `strategy.close("buy")` leg gated on positive-oscillator-plus-volume-contraction plus long state, three visual `plot()` lines. Author prose pins `BTC/USDT` on the `4 hour` timeframe. No sizing beyond 100%-equity (fenced), no stop/target/trailing/time leg, no second timeframe, no repaint-capable call anywhere in the file.

### Independently reproduced

No strategy backtest, realized market fills, profits, Qlib parity, OOS, Survivor or HB Certified results. This cycle directly inspected the TradingView page (HTTP 200, 707,581 bytes, prose verified in page metadata) and the verbatim Pine payload from the pinned facade (size/sha256/version/dates pinned above), plus the immutable pinned Hummingbot feed/MARKET/POSITION_HOLD/fallback source paths (SHA, VERSION and three file sizes re-verified this round), and reused prior independent primitive evidence (#519/#529/#530), not a candidate-specific test or installed-binary hash. Prior primitive validation does not imply that an unimplemented dedicated controller already exists.

- **Rule-logic self-check (stdlib only, not a backtest):** the frozen ROC/SMA/latch chain plus the FLAT/LONG state machine were executed over the real-data replay below — all pass: equality bars route to hold on every leg; pre-validity bars stay silent crash-free; first valid `changeMovAvg` lands exactly at index 6 as derived; identical inputs give identical outputs across two runs (signal-series md5 `f74567103730962b385ca417dafc1038` twice). Both legs provably reachable (98 entry-latch bars and 3,983 state-independent exit-predicate bars).
- **Rule computability on real public data (availability check, not a backtest — no PnL, no returns computed):** 14,656 fully completed Binance BTCUSDT spot `4h` bars (2020-02-19 → 2026-10-28; the still-forming 2026-10-28 late bar excluded) verified contiguous at exact 14400-second open steps with zero invalid OHLCV bars (eight pre-2020 maintenance-window gaps, all before 2020-02-19 16:00Z, fenced out by starting the window after the last gap — listed in Negative evidence). Post-warmup evaluation yields 98 entry-latch bars and 69 filled round trips (median hold 5 bars, min 2, max 27) and ends FLAT — no long held at the sample end. Worked latches: ENTRY t=108 (2020-03-08 16:00Z, C 8280.11, CMA[t] −1.1919 rising from CMA[t-1] −1.3782 below −1.0, V 20292.371→20627.555 expanding); EXIT t=120 (2020-03-10 16:00Z, C 7978.80, CMA[t] 0.2656 above zero, V 22915.520→16312.364 contracting). The candidate's trade events, Qlib/Hummingbot parity, and net returns have **not** been independently reproduced. No backtest was executed.

### Six-gate proposed PASS — independent Hermes Auditor decides

1. **Determinism:** literal two defaults, literal current-close-divisor ROC formula with pinned strict-6 SMA seed convention, Pine-literal trough/volume/inequality recursion, strict-inequality firing with equality-hold, first-decision index and priority.
2. **Direction:** BTCUSDT spot LONG/FLAT; the payload holds zero short legs and the prose confirms long-only dip buying.
3. **Entry/exit/risk:** trough-rising BUY, positive-plus-contraction SELL; no payload stop/target/trailing/time leg exists (0-exit census in a `strategy()` payload) and all hidden defaults are expressly disabled; the opposite signal is the sole risk mechanism with no loss-cap claim.
4. **Position:** cash10000/Q0.001/fee0.00075, single pending and inventory ledger, mutually-exclusive FLAT/LONG gates with no cooldown needed, fail-closed fill reconciliation, re-entry only on a future bar while FLAT, no DCA or concurrency.
5. **Pinned compatibility:** actual 4h Binance spot feed, controller/action/next-row MARKET actual close, POSITION_HOLD gross-plus-fees and independently declared Decimal net ledger, pure-research precision/dust boundary; no unsupported next-open, intrabar, MTF, volume-normalization, or futures funding claim.
6. **Causality:** t>=20 completed-bar decision on C[0..t] and V[0..t] through values from bars <=t (structural lag 6, decision lag 20), t+1 completed-close fill effective E[t+1], opening timestamp not mistaken for completed data, no future leakage or synthetic prices.

### Negative evidence

No backtest, profitability, Qlib parity, OOS, Survivor or live-fill evidence is claimed. The Pine `sma` early-bar na convention is a disclosed researcher pin fenced by the 20-bar warmup, not a payload value. The opposite signal is bars late by construction and the book has no protective stop — a grinding decline that never recrosses zero on contracting volume stays exposed (longest observed hold 27 bars ≈ 4.5 days, disclosed as duration only, not as a loss bound). TV-chart volume and Binance printed base volume are different feeds; the relative bar-over-bar comparisons may flip boundary signals across feeds. The author prose ("far away from the mean") overclaims what the code measures (a −1% trough in smoothed 1-bar returns, not a distance from any mean) — fenced as prose/code divergence. Pre-2020 gaps fenced out of the replay window: 2018-02-08 (7 bars), 2018-06-26 (2), 2018-07-04 (1), 2018-11-14 (1), 2019-03-12 (1), 2019-05-15 (2), 2019-08-15 (1), 2020-02-19 (1). Event rate is moderate (69 trips per ~14.6k post-warmup 4h bars). Sibling dip/mean-reversion exposure shapes in the pool are disclosed, not hidden.

**Dedup:** current main at `3b1c0ed` has 407 root strategy Markdown records (README pool count 407, verified: 409 `*.md` minus two READMEs). Full-tree case-sensitive grep for `kriswaters`, `30AJfvAa`, `changeMovAvg`, `dropRate` returns zero strategy records. Nearest mechanism neighbors check: `roc-sign-state-long-flat` (bare 30-bar ROC sign, no smoothing/threshold/volume), `forven-roc-zero-cross-momentum` (12-bar ROC cross, no volume), `worldquant-alpha21-band-volume-gated` (two-sided band breach plus ADV ratio, reversal exits), `tradingview-tradevizion-mean-reversion-pro` (SMA5/SMA100 price-range location, cross exit), `coppock-curve-zero-state` (WMA of ROC sums, zero-axis), `low-high-dip-tp` (20-bar low reclaim plus EMA200 plus 8% TP), `etf-3day-reversion` (consecutive lower closes plus EMA5), `forven-momentum-burst` (20-bar volume percentile burst), `forven-zscore` (z-score bands) — all different trigger/exit constructions; none is a smoothed-1-bar-ROC trough with volume-gated signal exits. All ten open research/* PR titles were checked (#353 Heracles KCD, #350 ClucMay72018, #331 AdxSmas, #304 forven CCI, #251 Swift 2yMA, #92 SSL, #89 Chandelier, #63 SuperTrend flip, #49 Gauss StochRSI, #48 Larry Williams streak); none is ROC-trough/volume-gated. Existing root records were not re-audited individually in this Scout; the 407/407 count census plus the merged-base diff shows only reviewed PASS additions and README bookkeeping, with no other strategy changes.

## Falsification plan

With separate authorization only, materialize the minimal candidate-specific controller and test the 6/20-bar seed boundary, the strict-6 SMA pin against Pine's native early-bar values, trough-depth boundary at exactly −1.0, rising/falling equality routing on both legs, state memory through consecutive same-side troughs, re-entry after an exit while still FLAT, first-decision-edge behavior at bars 19/20, pending-bar gate freezes, exact t/t+1 timing, observed prices, quote fees at the source-declared 0.00075, separate Decimal inventory, float residual tolerance and end-of-sample treatment. Before large-scale Qlib screening of any new execution path, obtain representative event-level Hummingbot/Qlib parity. No such execution, deployment or backtest occurs in this Scout.

## Crypto portability

Source prose already names `BTC/USDT`; this derivative moves only the venue leg to Binance BTCUSDT spot 4h with no leverage or funding. No asset substitution beyond this single declared market is made. Porting the trough-gate latch to other spot symbols would be a new derived version with its own evidence, not covered by this record.

## Limitations

Verbatim rule tokens come from the pinned immutable facade payload (byte-inspected this round: 1,160 bytes with sha256 pinned above) under its MPL-2.0 header line; only rule tokens are normalized here. Pine's default next-bar fill is adapted to the disclosed t+1 completed-close research fill, not lossless reproduction. The source's 100%-equity compounding sizing is fenced, never adopted. TV-chart volume versus Binance printed base volume is a disclosed feed substitution. The pure-research close/full-fill/fee model is not a real exchange acceptance or executable strategy implementation. The opposite signal is bars late by construction and the book has no protective stop — a grinding decline that never prints an exit latch stays exposed. The SMA seed pin and the 20-bar warmup are disclosed researcher choices, not payload values. No performance, survivor, live or Qlib parity claims.

## Implementation status

**implementation_status: not-implemented** — research record only. **status: research-only; adoption: not-approved; approval_scope: research-only.** The proposed PASS is not self-approval: independent Hermes Auditor GitHub Webhook Review alone owns source-fact review, exact-head PASS merge or NOT_LOSSLESS close. The existing signed webhook receiver alone owns post-merge README bookkeeping. This Scout does not approve, merge, close, modify main or change any trading/backtest/cron system.

## Adoption boundary

Research-only. Not approved for Paper, Testnet, Live, Qlib mass screening, or any deployment. Downstream use requires the independent PASS review plus separate implementation and authorization steps outside this record.

## Related Wiki records

None created by this Scout.

## Sources

- https://www.tradingview.com/script/30AJfvAa-Mean-Reversion-Strategy-by-KrisWaters/ — TradingView strategy page carrying the title, author, prose (BTC/USDT, 4h) and canonical identity, read 2026-10-28 (HTTP 200).
- pine-facade `PUB;3pfvAh8BpsmL2N4MQVk8Jiq3s4QKa3ft` `get/.../last/` — immutable payload carrying the verbatim Pine v4 strategy, inspected 2026-10-28 at version 1.0 (created==updated 2019-12-05T07:20:59.978687Z).
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — immutable pinned engine paths inspected via pinned raw fetch this round (SHA/VERSION plus three file sizes and key lines re-verified).
- https://github.com/HCH725/alpha-strategy-research/pull/519 — prior independent bounded MARKET/POSITION_HOLD synthetic primitive review.
- https://github.com/HCH725/alpha-strategy-research/pull/529 — prior independent bounded pure-research execution and PASS-only census evidence.
- https://github.com/HCH725/alpha-strategy-research/pull/530 — prior independent PASS census evidence.
