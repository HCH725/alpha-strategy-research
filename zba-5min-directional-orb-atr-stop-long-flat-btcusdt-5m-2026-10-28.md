---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Zarattini-Barbon-Aziz 5-minute directional ORB with 10%-ATR stop long-flat BTCUSDT 5m (independent derivative)"
created: 2026-10-28
updated: 2026-10-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-02-16
sources:
  - https://doi.org/10.2139/ssrn.4729284
  - https://www.sfi.ch/en/publications/n-24-98-a-profitable-day-trading-strategy-for-the-u.s.-equity-market
  - https://www.quantconnect.com/research/18444/opening-range-breakout-for-stocks-in-play/
  - https://www.quantifiedstrategies.com/stocks-in-play-trading-strategy-day-trading/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Zarattini-Barbon-Aziz 5-minute directional ORB with 10%-ATR stop long-flat BTCUSDT 5m

## Provenance

- **Primary source:** Zarattini, Barbon & Aziz, *A Profitable Day Trading Strategy For The U.S. Equity Market*, Swiss Finance Institute Research Paper 24-98 / SSRN 4729284, version **2024-02-16**, 27 pages; PDF fetched live **2026-10-28** (1,038,400 bytes, SHA-256 `85d9b8c3c4de0ae31dc74e4c19a8d2f0f3d17347a0c9f840a9002d3ac14f9ca6`), read end to end via text extraction.
- **Immutable proposed research identity:** `SSRN:4729284|ZBA-2024-02-16|derived-v1-20261028|BTCUSDT-spot-5m|ORB-first5min-bullish-gate|ATR14d-stop0.10|tplus1-completed-close|Q0.001-fee0.001`. The identity is fixed by this record and PR head, NOT a hash of any source revision.
- **Source-reported facts (§-pinned):** §2: 5-minute ORB with a directional gate — bearish first 5-minute candle (close below open) admits short only, bullish first candle admits long only, doji (open equals close) admits no order; stop buy/sell order placed at the 5-minute range high/low; stop loss at **10% of 14-day ATR** from entry; if not stopped, position closed at end of trading day; Figure 2 worked example (BLDR, daily ATR $5, short at range low $174.44, stop at 10% ATR). §2.1: base-sample backtest 2016-01-01–2023-12-31, $25,000 start, $0.0035/share commission; Table 1 base: 29% total, 3.2% annual, Sharpe 0.48, hit 41.4%, MDD 13%. §4: Stocks-in-Play filters — open above $5, 14-day average volume at least 1,000,000 shares, 14-day ATR above $0.50, first-5-minute Relative Volume at least 100%, only the top 20 stocks by Relative Volume; sizing targets a 1% loss on deployed capital if stopped with a 4x leverage cap; Table 2 ORB+RelVol: 1,637% total, 41.6% IRR, Sharpe 2.81, hit 48.4%, MDD 12%, alpha 35.8%, beta 0.00. QuantConnect research #18444 (live-fetched 2026-10-28) independently recreates the same rule (5-minute range, bullish→stop-buy at range high with stop at high minus k·ATR, RelVol>1 top selection, 2016 backtest Sharpe 2.396 vs SPY 0.836, beta −0.042). QuantifiedStrategies Stocks-in-Play article states the same 10%-of-14-day-ATR stop, 1% risk sizing and session-end exit (live page bot-walled 2026-10-28; rules recovered from the indexed article excerpt plus the paper and the QuantConnect recreation; no archived clean copy exists).
- **Explicit independent derivative, NOT source-native or lossless:** research pins single-asset BTCUSDT Binance spot 5m, UTC-day session (00:00–00:00 UTC, range bar 00:00–00:05 UTC), long-only (short leg disabled on spot; only bullish-range days trade), completed-5m-close breakout entry with next-completed-close MARKET fills, Wilder ATR14 on completed **daily** bars for the 10% stop distance, close-evaluated stop/session-end exits, fixed quantity/cash/fees and its own ledger. The paper's US-equity universe, penny/liquidity/RelVol/top-20 stock selection, intraday stop-market touch fills, 1%-risk/4x portfolio sizing, $0.0035/share costs and all original performance numbers are NOT ported. Every changed decision rule is specified below; source-native event equivalence and any transfer of the paper's returns are explicitly disclaimed.

## Economic mechanism

### Source-reported

The paper argues the first 5 minutes reveal the institutional supply/demand imbalance prevailing through the day; trading only high-Relative-Volume stocks isolates news-driven intraday trends, and a tight 10%-ATR stop with a session-end exit harvests continuation while cutting reversals (§2, §4).

### Research interpretation

This derivative keeps only the paper's **directional opening-range gate plus ATR-distance stop** and transplants it onto a 24/7 crypto tape with a UTC-day session: it buys a completed-close break of the first-5-minute high on bullish-range days, risks a fixed 10%-of-daily-ATR distance evaluated on closes, and is always flat before midnight. It may miss touch-but-close-back breakouts, enter after the move, or gap far beyond its signal-level stop; no protective order or profitability is implied, and none of the paper's stock-selection edge transfers.

## Signal

Two ordered series of Binance **BTCUSDT spot** completed OHLCV: 5m bars (index `t` within UTC day `D`, `t=0..287`) and daily bars (index `d`), deterministic float64 arithmetic, no ML, fit or full-sample optimization.

1. **Session grid:** day `D` opens at 00:00 UTC. Range bar `t=0` (00:00–00:05 UTC) fixes `RH[D]=high[0]`, `RL[D]=low[0]`, `O0[D]=open[0]`, `C0[D]=close[0]`. `BULL[D]=(C0[D]>O0[D])` strict; bearish or doji days stay flat all day (paper §2 doji rule, extended to the disabled short leg).
2. **Daily ATR14 (Wilder):** on completed daily bars, `TR[0]=high[0]-low[0]`; `TR[d]=max(high[d]-low[d],abs(high[d]-close[d-1]),abs(low[d]-close[d-1]))` for `d>0`. `ATR14[13]=mean(TR[0..13])`, then `ATR14[d]=(13*ATR14[d-1]+TR[d])/14`. `A[D]` = ATR14 of the last daily bar closing at or before day-`D` open (i.e. through `D-1`); frozen for day `D`, never recomputed intraday. First tradable day requires 15 completed daily bars.
3. **BUY signal** at completed 5m bar `s` in `[1,283]` iff `BULL[D]` AND research state FLAT with no pending action AND `close[s]>RH[D]` (strict; a close exactly on the high is not a breakout) AND `A[D]>0`. At most one entry per day: bars after the first BUY signal are never evaluated for entry.
4. BUY pending on `s` fills full `Q` at actual completed bar `b=s+1` close `P_b` (only when that bar exists and full-fill evidence is valid); freeze `stop=P_b-0.10*A[D]`. If `stop<=0` or prices/ATR invalid, abort rather than invent a stop. Risk distance `R=0.10*A[D]`.
5. **SELL signal** on completed bar `e` in `[b+1,285]` iff LONG and no pending action and at least one of: `close[e]<=stop` (STOP) or (`e==285` AND still LONG, EOD). Label priority STOP > EOD; both fill at the same next close when they coincide on `e==285`. SELL fills full Q at actual completed close `P_{e+1}` (bar ≤286, always exists). A stop-level breach can fill much worse at the later close; do not cap the loss at R.
6. All other exits (intraday stop-market/limit touch orders, profit target, trailing, opposite short signal, partial exits, overnight holds, liquidation, drawdown kill switch) are **disabled**. No silent executor defaults. Days with no BUY signal stay flat (as in the paper).

## Required data

Only actual Binance spot BTCUSDT 5m and 1d open/high/low/close/volume. Before any feature use, require strictly increasing 5m open timestamps spaced 300 seconds and strictly increasing daily opens spaced 86400 seconds aligned to 00:00 UTC, finite positive O/H/L/C, `high>=max(open,close)`, `low<=min(open,close)`, `high>=low`, finite nonnegative volume; a day missing any bar `0..286`, or with duplicate/discontinuous/incomplete bars, or with fewer than 15 completed daily bars behind it, is void (flat, fail-closed). No synthetic candles, zero-price fallback, future fills, external feeds or funding data. All signals use current and earlier **completed** bars; `A[D]` uses daily bars closed before the session; no repainting, negative shifts or future extrema.

## Execution assumptions

**Pinned Hummingbot evidence, read as immutable raw files 2026-10-28:** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, package label `20260920`, `hummingbot/VERSION=dev-2.17.0`. Read `data_feed/candles_feed/binance_spot_candles/constants.py` (993 bytes), `binance_spot_candles.py` (3924 bytes), `strategy_v2/backtesting/backtesting_engine_base.py` (39071 bytes), `backtesting_data_provider.py` (8823 bytes), `backtesting/executors_simulator/order_executor_simulator.py` (3913 bytes), `backtesting/executor_simulator_base.py` (4453 bytes), and the `CloseType` import from `strategy_v2/models/executors.py`. Prior independently reviewed bounded engine primitive exercise is in Alpha PR #519; #529/#530/#532/#533 independently audited this research-only MARKET/POSITION_HOLD lane. This record does not claim a dedicated controller already exists or a new wheel/image hash verification.

- **Feed and time:** BinanceSpotCandles REST `/api/v3/klines` parser maps the first exchange timestamp (candle OPEN) to the row timestamp; `5m` and `1d` both exist in the pinned intervals. 5m bar `t` is available only at `E[t]=T[t]+300` seconds; daily bar `d` only after its 00:00 UTC close. `A[D]` is therefore known at the session open.
- **Engine path:** `BacktestingEngineBase.simulate_execution` calls `update_state(row)` then `controller.determine_executor_actions()`, passing `processed_features.loc[i:max_ts]` to `simulate_executor`. A minimal future controller maintains the record's FLAT/LONG/PENDING, frozen range/ATR/stop and once-per-day state; it queues a signal at completed `s`/`e` and emits one `CreateExecutorAction(OrderExecutorConfig)` **only on the next bar**, never on the signal bar. Config: `connector_name="binance"`, `trading_pair="BTC-USDT"`, `side=BUY/SELL`, `amount=Decimal("0.001")`, `position_action=OPEN/CLOSE`, `execution_strategy=MARKET`, `price=None`, `leverage=1`. No entry/exit decisions can create a same-bar round trip: every signal fills strictly one bar later, and at most one BUY plus one SELL exist per day.
- **Actual bounded fill:** pinned `OrderExecutorSimulator` MARKET fills at the first supplied row's **real close**, `amount_quote=float(Q)*close`, `cum_fees_quote=trade_cost*amount_quote`, `CloseType.POSITION_HOLD`. Dispatch on next row gives idealized next-completed-close fill. `ExecutorSimulation` exposes fill timestamp/filled quote/terminated evidence. If missing/invalid real close, partial/duplicate/failed/stale/unmatched fill, insufficient cash or a nonexistent successor (impossible inside bars ≤286 by construction): fail closed. `BacktestingDataProvider.get_price_by_type` has a `Decimal("1")` missing-price fallback; it is explicitly forbidden for this model.
- **Research ledger:** start `cash=Decimal("10000") USDT`, `inventory=Decimal("0") BTC`, exact `Q=Decimal("0.001") BTC`, one position and at most one pending action. Full confirmed BUY: `cash-=Q*P*(1+f); inventory+=Q`; SELL: `cash+=Q*P*(1-f); inventory-=Q`; `f=Decimal("0.001")` per side is an explicit **hypothetical** quote-notional taker-like fee, NOT verified Binance tier. `trade_cost=0.001`. Gross PnL `Q*(Ps-Pb)`; fees `f*Q*(Pb+Ps)`; net = gross minus fees. No compounding, partial exits, DCA, safety orders, pyramiding, concurrent markets/positions, cooldown (beyond one-per-day) or same-bar round trip. A new UTC day re-arms independently. Terminal LONG is impossible by construction (EOD always fills at bar 286); no synthetic liquidation.
- **Precision/positions:** native MARKET uses float quote and `BacktestPositionHold` derives Decimal base from quote/price with exact-zero closure, potentially retaining microscopic dust; native `positions_held` also lags. Research state is **independent confirmed-fill Decimal cash/inventory**, not native exact-zero `is_closed` or gross-only summary. Compare engine-implied base to expected within `1e-12 BTC` and fee/quote within `1e-8 USDT` diagnostic tolerances; above limits abort. Keep complete terminated history (`terminated_executors_window=None` or equivalent). These are research-only precision checks, NOT exchange rounding/lot/tick/min-notional or live acceptance.
- **Scope:** Spot funding is not applicable (not assumed-zero unknown perpetual funding); no futures leverage/margin/liquidation, maker/limit/intrabar executor, slippage modeling beyond explicitly idealized zero additional slippage, real spread/liquidity, exchange minimums or actual fee tier. The 5m+1d dual-feed alignment is demonstrated only through the two pinned spot candle intervals above; no unverified engine capability is inferred from an API or candle interval name alone.

## Evidence

### Source-reported

Paper §2/§2.1/§4/Table 1/Table 2/Figure 2 as pinned in Provenance: directional 5-minute ORB, stop-buy at range high (bullish) / stop-sell at range low (bearish), doji admits nothing, 10%-of-14-day-ATR stop, session-end exit, 1%-risk sizing with 4x cap, RelVol≥100% top-20 selection with $5/1M-share/$0.50-ATR filters; base 2016–2023 29% total (Sharpe 0.48, hit 41.4%, MDD 13%) vs ORB+RelVol 1,637% total (41.6% IRR, Sharpe 2.81, hit 48.4%, MDD 12%, alpha 35.8%, beta 0.00); QuantConnect #18444 recreation: 2016 Sharpe 2.396 vs SPY 0.836, beta −0.042. None of these returns transfer to this crypto derivative.

### Independently reproduced

No original backtest parity, candidate-specific Hummingbot/Qlib backtest, event-level Qlib parity, profitability, OOS, Survivor, HB Certified or exchange fill is claimed. Direct inspection of the immutable pinned Hummingbot source plus existing independently audited bounded MARKET/POSITION_HOLD primitive evidence supports only the stated research model. All UTC-day sessioning, long-only gating, close-breakout/stop/EOD translation and cost/size choices are researcher-selected and reproducible, not source-reported execution facts.

### Six-gate evidence for independent auditor

1. Deterministic float64 session grid, strict breakout/equality boundaries, Wilder ATR14 seed, frozen per-day ATR/stop, one-per-day state, explicit price and fee models.
2. BTCUSDT Binance spot 5m LONG/FLAT only; short/borrow/futures disabled; bearish/doji days flat by rule.
3. Complete BUY and two priority SELL conditions (STOP, EOD), frozen stop from confirmed entry, delayed completed-close fills; no hidden intrabar stop/target/trailing.
4. Exact Q/cash, single position/pending, full-fill state, no DCA/pyramiding/concurrency, next-day re-arm, no void-day or post-286 fake fill.
5. Exact pinned Binance spot dual-feed/controller action/MARKET actual-close/POSITION_HOLD/fee and Decimal ledger with fail-closed precision; reuse independently reviewed bounded primitive #519/#529/#530/#532, no new engine primitive or claimed live acceptance.
6. 15 daily bars + completed range bar warmup, decision at E[t], next completed-close fill, no incomplete bar, future leak, synthetic prices or ambiguous intrabar events.

**Dedup (2026-10-28):** working-tree case-insensitive searches for `zarattini`, `barbon`, `aziz`, `stocks-in-play`, `relative-volume`, `relvol`, `first-5`, `5-minute`, `doji`, `4729284` return no record using this paper, directional first-candle gate, or 10%-ATR-stop construction; the two letter-`orb` hits are materially different (Forven trailing 4-bar Donchian channel with band-level exits; Holmberg open-anchored ±ρ% first-touch threshold with next-open fills and no stop). GitHub issue/PR search for `4729284` returned none. All 10 open `research/*` PR titles were checked and none represents this paper or its directional 5-minute ORB. Baseline `main@2245b98`: README 392, tree 392 root strategy records (excluding both READMEs).

## Falsification plan

Under separate future authorization only: range-bar high/low equality (no breakout on touch), doji and bearish-day flatness, breakout-equality no-entry, stop-boundary equality, STOP-over-EOD priority on bar 285, entry-window edges (bars 1 and 283), void days (missing bars fail closed), ATR seed and freeze, stop<=0 abort, pending and fill-bar successor existence, gaps through stop, Decimal full-fill/dust/fees, and point-in-time prefix invariance. Validate a genuinely new Qlib/HB execution primitive with representative event-level parity before mass Qlib screening; none is run here.

## Crypto portability

Explicit independent BTCUSDT spot 5m derivative. The original is a US-equity intraday system whose edge depends on stock selection; no claim of source equivalence, live session-open latency, or automatic port to other markets, timeframes, futures or DCA. The paper's 1,637%/Sharpe-2.81 evidence does not transfer.

## Limitations

The paper's intraday stop-market touch fills are idealized to next-completed-close MARKET fills, which miss touch-but-close-back breakouts and fill stop breaches late; the RelVol/universe edge is dropped, so original performance explicitly does not transfer. 5m/1d dual-feed alignment, UTC-day sessioning, long-only gating, fixed sizing and hypothetical costs are **declared researcher choices**, not reconstructed source facts. Historical completed-close MARKET fill is idealized and may be unavailable live; there is no guaranteed stop protection, measured slippage, spread, real fee tier, order minimum validation or performance evidence. The independent auditor must reject if any claimed pinned-model path is not substantiated.

## Implementation status

`implementation_status: not-implemented`. Research-only strategy specification; no dedicated controller, Hummingbot/Qlib execution, container, trading or deployment performed.

## Adoption boundary

`status: research-only`; `adoption: not-approved`; `approval_scope: research-only`. Proposed `hb_ready_status: PASS` is for independent Hermes Auditor GitHub Webhook Review; Scout does not self-approve, merge or close. Existing signed webhook receiver alone reconciles README after a confirmed accepted merge.

## Related Wiki records

No new Wiki/registry entries; Forven/Holmberg ORB families are not asserted equivalent.

## Sources

- https://doi.org/10.2139/ssrn.4729284 — Zarattini, Barbon & Aziz, SFI RP 24-98, v2024-02-16; PDF read end to end 2026-10-28 (27 pages, SHA-256 `85d9b8c3…c14f9ca6`).
- https://www.sfi.ch/en/publications/n-24-98-a-profitable-day-trading-strategy-for-the-u.s.-equity-market — SFI record page confirming authors, date 27 Nov 2024, sample and headline results.
- https://www.quantconnect.com/research/18444/opening-range-breakout-for-stocks-in-play/ — independent LEAN recreation of the paper's rule, live-fetched 2026-10-28.
- https://www.quantifiedstrategies.com/stocks-in-play-trading-strategy-day-trading/ — rule summary (live page bot-walled 2026-10-28; indexed excerpt cross-checked against paper §2/§4).
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned source inspected as immutable raw files.
- https://github.com/HCH725/alpha-strategy-research/pull/519 — independent bounded MARKET/POSITION_HOLD primitive audit.
- https://github.com/HCH725/alpha-strategy-research/pull/529 — independently reviewed pure-research accounting path.
- https://github.com/HCH725/alpha-strategy-research/pull/532 — recent independent bounded execution audit.
