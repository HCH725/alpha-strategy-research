---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "QuantsPlaybook price-volume resonance HMA dual-threshold long-flat BTC-USDT spot 1d independent derivative"
created: 2026-10-27
updated: 2026-10-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - github
  - source-backed
status: research-only
confidence: medium
source_as_of: 2022-11-11
sources:
  - https://github.com/hugo2046/QuantsPlaybook/tree/3f83a77f4c7996ed8185b8979a42c4372c1d811f/C-%E6%8B%A9%E6%97%B6%E7%B1%BB/%E6%88%90%E4%BA%A4%E9%87%8F%E7%9A%84%E5%A5%A5%E7%A7%98_%E5%8F%A6%E7%B1%BB%E4%BB%B7%E9%87%8F%E5%85%B1%E6%8C%AF%E6%8C%87%E6%A0%87%E7%9A%84%E6%8B%A9%E6%97%B6/scr/bt_strategy.py
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Price-Volume Resonance — HMA price-momentum x HMA volume-momentum vs regime dual-threshold long-flat research derivative

## Provenance

**First-party GitHub source:** hugo2046/QuantsPlaybook, notebook/strategy family `C-择时类/成交量的奥秘_另类价量共振指标的择时` (price-volume resonance timing), strategy module header dated **2022-10-28**, last edited **2022-11-11**, inspected **2026-10-27** at immutable commit **`3f83a77f4c7996ed8185b8979a42c4372c1d811f`** (committed 2026-10-03): strategy body `scr/bt_strategy.py` (119 lines, read verbatim via immutable Contents API), config `scr/utils.py` (`BACKTEST_CONFIG = dict(n=3, threshold=(1.125,1.275), bma_window=50, ama_window=100, fast_window=5, slow_window=90)`), vectorized twin `scr/create_signal.py`, and the notebook markdown cell stating the same rules and parameters. No source-native, backtrader-identical or author-performance reproduction is claimed.

**Verified source-code facts:** `VM_Indicator` computes `bma=HMA50(close)`, `price_mom=bma/bma(-3)`, `vol_mom=HMA5(volume)/HMA100(volume)`, `Vol_Mom=price_mom*vol_mom`. `Shake_Filter` computes `SMA5/SMA90` of close and `Threshold=1.125 if fast>slow else 1.275` via `bt.If`. `VM_Strategy.next()` cancels any pending order, then: if in position and `vm<=threshold` issues `order_target_value(0)`; elif flat and `vm>threshold` issues `order_target_percent(0.95)`. The file contains no stop/limit/trailing/time-exit, no short leg, no pyramiding/sizer/DCA logic, and no alternate parameter set. Backtrader market orders execute at the next bar open by default; that source-native timing is **not** adopted here.

**Explicit independent derivative, NOT lossless source reproduction:** The researcher chooses a closed-form HMA construction below, Binance BTC-USDT **spot UTC 1d**, LONG/FLAT only, fixed 0.001 BTC, 10,000 USDT initial research cash, completed-close signal to next completed-close historical MARKET fill (substituting for the source backtester's next-open fill), and hypothetical 0.1% fee per filled side. The source 95%-equity target sizing and A-share cost model (0.0002 commission + 0.001 stamp duty + 0.0001 slippage in `utils.py`) are **not** adopted. These choices materially change trade events and economics and are researcher-authored.

**Frozen derived identity:** `GH:QuantsPlaybook|3f83a77|2022-11-11|independent-v1:2026-10-27|BinanceSpot:BTC-USDT:UTC1d|HMA50-BMA|PM-BMA/BMA[-3]|VR-HMA5V/HMA100V|VM-PMxVR|TH-SMA5gtSMA90-1p125-else-1p275|t-signal-to-tplus1-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-per-side|warmup-t108`. A change to any decision-critical rule defines a new derivative, not a silent update to this identity.

## Economic mechanism

### Source-reported

The author multiplies a Hull-smoothed price-momentum ratio by a Hull-smoothed volume-momentum ratio so that entries require price strength and participation expansion to agree, with the required agreement level relaxed (1.125) when the fast SMA is above the slow SMA and tightened (1.275) otherwise. No realized return is adopted.

### Research interpretation

This independent derivative tests a scale-free resonance product: both ratios are unit-free, so BTC quote/volume units cannot shift the signal. The regime gate makes the bar for resonance lower in an SMA-defined uptrend and higher otherwise. A single complementary inequality drives both entry and exit, so no second risk leg must be invented. No performance assertion is made.

## Signal

1. **Inputs and clock:** one contiguous, chronological real Binance BTC-USDT spot **UTC 1d** OHLCV sequence indexed t=0,1,...; each opening timestamp T[t] must be UTC midnight-aligned and T[t+1]-T[t]=86400 seconds. Require finite O,H,L,C>0, H>=max(O,C), L<=min(O,C), H>=L, and finite V>0 for every row. Abort on gaps, duplicates, missing prices/volume, malformed bars, unavailable last candle or out-of-order timestamps. No interpolation, synthetic price, full-sample fitting or partial candles. Bar t's completed values become available only at E[t]=T[t]+86400, not at T[t].
2. **WMA definition (researcher-specified closed form):** for a sequence X, `WMA_p(X)[t]=sum_{k=1..p} k*X[t-p+k]/(p*(p+1)/2)` for t>=p-1, undefined earlier. Newest observation carries weight p. Float64, no intermediate rounding. This pins the linear-weight convention explicitly rather than inheriting any library default.
3. **HMA definition (researcher-specified, Hull/backtrader structure):** `HMA_p(X)[t]=WMA_q(2*WMA_{p//2}(X)-WMA_p(X))[t]` with `q=int(sqrt(p))` (floor), valid once all three windows are valid. Instantiations: HMA50 uses WMA25/WMA50/WMA7; HMA5 uses WMA2/WMA5/WMA2; HMA100 uses WMA50/WMA100/WMA10. This is a **researcher-specified closed form**, not a bit-parity claim against any backtrader build.
4. **Resonance product:** `BMA=HMA50(Close)`; `PM[t]=BMA[t]/BMA[t-3]`, requiring finite BMA[t-3]>0. `AMA5=HMA5(Volume)`, `AMA100=HMA100(Volume)`; `VR[t]=AMA5[t]/AMA100[t]`, requiring finite AMA100[t]>0 and finite non-negative AMA5[t]. `VM[t]=PM[t]*VR[t]`. Any non-finite input invalidates bar t and aborts the research segment rather than fabricating a value.
5. **Regime threshold:** `SMA5[t]=mean(Close[t-4..t])`, valid from t=4; `SMA90[t]=mean(Close[t-89..t])`, valid from t=89. `TH[t]=1.125 if SMA5[t]>SMA90[t] else 1.275`; equality takes 1.275 (source `bt.If` strict-greater semantics).
6. **Warmup/entry:** start FLAT, zero BTC and 10,000 USDT. No trading for t=0..107; first possible completed-bar decision is **t=108** (HMA100 composite first valid at t=108; SMA90 valid from t=89). Indicators may be computed earlier but must never backfill a position before t=108.
7. **BUY scheduling:** if FLAT, no pending order, t>=108, and t is strictly later than any prior exit-fill bar, an entry event is `VM[t]>TH[t]` (strict). Store exactly one BUY instruction from the completed t signal. Dispatch at row t+1 only; idealized historical MARKET full fill uses **observed** Close[t+1] with economic effective time E[t+1]. Never use any t+1 values to decide the t entry. If t+1 is absent, no fill. Require actual positive close, valid size/rules and cash >=Q*price*(1+f), Q=Decimal("0.001") BTC and f=Decimal("0.001"); otherwise abort the research segment rather than invent a fill.
8. **No bracket:** there is no stop/target/trailing/time exit in this derivative, matching the source file's complete absence of any risk leg. Absence here is an explicit disclosed choice, not a hidden default.
9. **Exit and priority:** while LONG and no pending order, at each later completed bar u (never on the BUY fill bar), `VM[u]<=TH[u]` (equality exits) schedules a full SELL at row u+1 with idealized MARKET fill at its actual observed close effective E[u+1]; otherwise HOLD. Entry and exit inequalities are complementary, so no same-bar ordering assumption exists. No same-bar roundtrip.
10. **Order and re-entry state:** one position and at most one pending order. A confirmed full SELL returns to FLAT, records its fill bar and clears state; any later completed bar with a fresh `VM>TH` event may re-enter, with no cooldown and no DCA. Pending-order cancel-before-new-signal mirrors the source `next()` cancel-first structure. Rejected/partial/duplicate/ambiguous BUY or SELL fills, missing price, or insufficient actual data abort the research segment, not silently mutate inventory. A last-row signal without a subsequent observed candle is unfilled; at sample end mark open inventory only at last actual completed close, separately from realized PnL, with no fabricated forced liquidation.
11. **Explicitly disabled:** short/borrow, futures/perpetuals, margin/leverage/funding, pyramiding, DCA/safety orders, concurrent markets/shared capital, partial exits, dynamic sizing/compounding, maker/limit/next-open orders, intrabar stops, trailing, time exit, source A-share cost model, and hidden executor defaults. No simultaneous or hedged positions.

## Required data

One real Binance BTC-USDT spot 1d OHLCV feed; close and volume are both signal inputs. No external symbols, order book, futures funding, non-OHLCV data, secondary timeframes, fitting or future extrema. Validate candle continuity and all observed fill prices **before** the pinned engine's feature merge/dropna. Decisions occur at E[t], fills at E[t+1] in the idealized historical model, regardless of the native feed's opening timestamp. All indicators use only <=t completed data. Zero/negative volume or missing candles aborts.

## Execution assumptions

**Pinned GitHub-inspected benchmark (2026-10-27):** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, package label `20260920`, `hummingbot/VERSION=dev-2.17.0`. Immutable raw-file inspection this run of `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` (INTERVALS declares `1d`), `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` (MARKET path fills at the row's actual close with `filled_amount_quote`/`cum_fees_quote` and returns `CloseType.POSITION_HOLD`), `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` (`BacktestPositionHold`, `simulate_execution` calling `controller.determine_executor_actions()` with `CreateExecutorAction`), and `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py` (`get_price_by_type` missing-price fallback). Prior Alpha PR #414 reports independent package/source correspondence; no wheel/image digest rehash in this run.

- **Actual feed:** pinned BinanceSpotCandles declares `1d`; Binance REST row[0] is **opening timestamp**, row[1..5] supplies real OHLCV. No synthetic candles, inferred fill prices, or silent forward filling. `BacktestingEngineBase.prepare_market_data` can merge features and drop missing rows; a pre-engine strict continuity/validity check is mandatory.
- **Actual action path:** `BacktestingEngineBase.simulate_execution` calls `update_state(row)`, then `controller.determine_executor_actions()`, and simulates `CreateExecutorAction`. A future minimal candidate-specific controller (not yet implemented) must preserve t's signal/pending state, delay dispatch to t+1, and issue `OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),position_action=OPEN/CLOSE,execution_strategy=MARKET,price=None,leverage=1)`; no API name alone is asserted to implement this strategy.
- **Actual bounded fill:** MARKET dispatch on t+1 yields an idealized **t+1 close** fill at that row's actual close, not the source backtester's next-open fill and not an achievable live post-close market price. Native fill row timestamp is an **opening** timestamp; economic effective fill time must be normalized to E[t+1], never reported as T[t+1].
- **Position and fee ledger:** pinned `BacktestPositionHold` nets opposite BUY/SELL base quantities and reports gross realized PnL while fees accumulate separately. Maintain a persistent confirmed-fill ledger (`terminated_executors_window=None` or equivalent) and explicit research cash/inventory: BUY cash `-=Q*Pb*(1+f)`, SELL cash `+=Q*Ps*(1-f)`, net realized round-trip `Q*(Ps-Pb)-f*Q*(Pb+Ps)`. The fee `f=0.001` is a **hypothetical 0.1% quote-notional fee per filled side**, not a verified Binance fee tier. Engine float-ledger internals are not asserted equal to research-side Decimal bookkeeping; any fill/ledger ambiguity aborts the segment instead of being rounded into a fill. Never call gross engine PnL net. Spot funding is **not applicable**, not fabricated zero perpetual funding.
- **Fail-closed boundaries:** `BacktestingDataProvider.get_price_by_type` can return `Decimal("1")` on a missing price; explicitly **forbid** that fallback. Reject absent/nonpositive observed closes, zero/negative volume, invalid trading rules, unsupported precision/min-notional, partial fills and ambiguous position accounting rather than inventing economics. Simulator's idealized full fill does not prove real spread, slippage, liquidity, live minimum order/precision, dynamic fee or latency. The future controller, real execution and package binary are **not** independently validated; this record claims only the bounded pinned historical close-fill primitive.

## Evidence

### Source-reported

QuantsPlaybook price-volume resonance module (2022-10-28/2022-11-11): HMA50 price ratio over 3 bars lag times HMA5/HMA100 volume ratio, gated by SMA5-vs-SMA90 dual thresholds 1.125/1.275, target-percent entry and target-zero exit, no risk leg. No original backtest result is adopted.

### Independently reproduced

**None for strategy events, profits or outcomes.** No backtrader parity run, candidate-specific Hummingbot run, Qlib backtest, event-level parity, actual fills, installed package hash, OOS, Survivor or HB Certified claim. Only the **existing pinned source-code engine/data/executor/fee paths** were directly inspected via immutable raw files at the pinned commit. Alpha PR #414 is prior correspondence evidence, not a claim of re-execution this cycle.

### Negative evidence

Source next-open fill, 95%-equity target sizing and A-share cost model are **explicitly replaced**, not source-native rules. The vectorized twin `create_signal.py` carries an object-dtype flaw in its trend/shake filter path; pinned semantics follow `bt_strategy.py`'s `bt.If`, consistent with the notebook text. Idealized close fills and assumed fees do not prove exchange execution. No realistic live fills or funding are asserted.

**Six-gate proposal, pending independent Hermes Auditor:**
1. Determinism: closed-form WMA/HMA seeds, PM/VR/VM formulas, SMA regime, strict/weak inequality attribution, t=108 warmup.
2. Direction: Binance BTC-USDT spot LONG/FLAT; no short leg exists in source or derivative.
3. Entry/exit/risk: complementary VM-vs-TH inequality, full exit on `<=`, disclosed absence of any risk leg.
4. State: fixed 0.001 BTC, one pending order/position, cash and fees, no DCA/concurrency, fresh event after exit, abort on ambiguous fills.
5. Pinned model: directly inspected actual 1d feed, controller/action, MARKET close fill, POSITION_HOLD and fee paths; no unsupported next-open/intrabar/funding assumption.
6. Causality: 108 completed-bar warmup, t completed signal -> t+1 completed-close economic fill, no future bars, opening timestamp never misrepresented as close availability.

**Dedup snapshot:** at `main=7c9d91d8b34f70f79b14d5f60c21b8eaa77bb22c`, README static pool count and root Markdown strategy count were both **383** (excluding two READMEs). Repo-wide `grep -rilE` over root `*.md` returned zero for `resonance`, `HullMovingAverage`, `VM_Strategy`, `VM_Indicator`, `Shake_Filter`, `order_target_percent`, `1\.125`, `1\.275`; `QuantsPlaybook` matched only `qrs-penalized-rsrs-zscore-timing-long-flat-btcusdt-1d-2026-10-16.md` (RSRS z-score timing, different notebook and mechanism). All ten open `research/*` PR titles/bodies were checked for source identity with no match. Nearest pool neighbors (`forven-hma-cross`, `hull-ema-crossover-reversal`, `amihud-2002`) are HMA/EMA **cross** or impact-ratio mechanisms; this candidate has no cross and no risk leg, its core being the price-momentum x volume-momentum product against a **regime dual-threshold**. Existing 383 strategies were **not** exhaustively re-audited for PASS frontmatter; count equality is not represented as a full admission census.

## Falsification plan

With separate authorization, materialize only a minimal candidate-specific controller, validate the strict t/t+1 clock and actual close inputs, WMA/HMA window validity and equality cases (`VM==TH` exits, `SMA5==SMA90` takes 1.275), positive-volume requirement, post-exit re-entry, fail-closed invalid fills and fee-net position accounting. Before large-scale Qlib screening on a newly unverified execution path, obtain representative Hummingbot/Qlib event-level parity for signals, fills, fees and states. Separately assess fee-net IS/OOS performance; no such test is run by this Scout.

## Crypto portability

BTC-USDT spot 1d is researcher-selected, not an author-validated outcome or admission whitelist. Any futures, 3x/5x, DCA BO/SO 6/6/6, other coin or execution model is downstream optional research requiring a separately specified derivative and verified execution/cost/funding path. No implied transfer of results.

## Limitations

No backtrader parity run; source-native equivalence unverified. Derived closed-form HMA, next-close fill, fixed quantity and hypothetical fees materially differ from the source backtest. Idealized close fills and assumed fees do not prove exchange execution. No installed package rehash, strategy backtest, Qlib parity, profitability or live authorization. Volume-ratio signals assume continuous real spot volume; thin-volume regimes are untested.

## Implementation status

`not-implemented`: research specification only. No controller, Qlib recipe, trading deployment, backtest, container, n8n or cron changes.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. `hb_ready_status: PASS` is **Scout-proposed**, not self-approved. Independent Hermes Auditor GitHub Webhook Review owns source-fact remediation, exact-head PASS merge or NOT_LOSSLESS close. The existing signed webhook receiver alone owns README bookkeeping after an accepted merge. Scout does not approve, merge, close or write main.

## Related Wiki records

None created or modified.

## Sources

- https://github.com/hugo2046/QuantsPlaybook/tree/3f83a77f4c7996ed8185b8979a42c4372c1d811f/C-%E6%8B%A9%E6%97%B6%E7%B1%BB/%E6%88%90%E4%BA%A4%E9%87%8F%E7%9A%84%E5%A5%A5%E7%A7%98_%E5%8F%A6%E7%B1%BB%E4%BB%B7%E9%87%8F%E5%85%B1%E6%8C%AF%E6%8C%87%E6%A0%87%E7%9A%84%E6%8B%A9%E6%97%B6/scr/bt_strategy.py — hugo2046, first-party public strategy code, 2022-10-28/2022-11-11; inspected 2026-10-27 at the pinned commit.
- https://raw.githubusercontent.com/HCH725/hummingbot/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — immutable pinned engine source (feed constants, order executor simulator, backtesting engine base, data provider), inspected through immutable raw files 2026-10-27.
- https://github.com/HCH725/alpha-strategy-research/pull/414 — earlier package/source correspondence evidence; not re-run here.
