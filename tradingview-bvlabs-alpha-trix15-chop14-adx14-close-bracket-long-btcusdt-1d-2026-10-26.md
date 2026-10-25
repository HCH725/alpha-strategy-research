---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: BVLabs Alpha TRIX15 zero-cross CHOP14/ADX14 gated long with fixed ATR close bracket on BTCUSDT 1d
created: 2026-10-26
updated: 2026-10-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-08-06
sources:
  - https://www.tradingview.com/script/1BJZkv2N-Alpha-TRIX-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# BVLabs Alpha TRIX15 zero-cross CHOP14/ADX14 gated long with fixed ATR close bracket on BTCUSDT 1d

## Provenance

Primary TradingView source: https://www.tradingview.com/script/1BJZkv2N-Alpha-TRIX-Strategy/ (stable script ID 1BJZkv2N, title "Alpha TRIX Strategy >_", author BVLabs, published 2026-04-10, updated 2026-08-06; public open-source listing read 2026-10-26). The visible first-party description, not an independently retrieved complete Pine program, supports exactly these source-level concepts: TRIX is one-bar rate of change of a triple EMA of close, its zero-line crossover triggers directional entries, CHOP below a threshold and ADX above a minimum simultaneously gate entry, and source-native TP/SL are ATR-derived and locked at entry. Source supports both long and short by configuration and says the native strategy.exit orders are placed at entry. The listing does NOT expose the effective Pine source text, default numeric TRIX/CHOP/ADX/ATR settings, actual Pine order-fill options, or full broker-emulator state. None of those missing values is asserted as an original-author default. No source performance claim is independently reproduced.

**Independent derived executable strategy, not lossless source reproduction.** Researcher-defined choices (all materially relevant): BTCUSDT Binance spot 1d; long-only with short disabled; TRIX triple EMA length 15 and zero-cross (no signal-line); CHOP14 < 38.2 and Wilder ADX14 > 25; ATR14 fixed 1.5x stop / 3.0x target; entry and exits evaluated at completed-bar close rather than source-native intrabar bracket orders; no opposite-signal exit; fixed 0.001 BTC and single-position state; 120 completed-bar warmup; explicit missing-data, cost, fill, and re-entry rules below. The source's three-layer TRIX/CHOP/ADX gate is retained conceptually; all numeric pins, direction restriction and execution/risk mechanics are a separately identified research derivative. The original source strategy is NOT represented as HB_READY PASS by this record.

Dedup checked against current main 3cbba57283dbd6d923aefcd9a2f63887b3cbfbb7 (344 root strategy records; README 344) and open research PRs before writing. No main code-search hit for script ID 1BJZkv2N or BVLabs, and no open PR hit for the script ID or TRIX. Existing forven-trix-signal-cross-zero-gate-long-flat (TRIX crossing its EMA9 signal above zero, signal-cross exit, no CHOP or ADX, no ATR bracket) and trix-dual-band-trend (fast/slow log-price TRIX cross with SMA trend/band gating, two-sided, no ATR bracket) have materially different triggers, gates, exits and provenance. The existing CHOP-zone DMI/PSAR strategy triggers CHOP zone states and PSAR/DMI exits rather than TRIX zero-cross gated by CHOP/ADX. This record is not a parameter-only duplicate of those mechanisms.

## Economic mechanism

### Source-reported

Triple-EMA smoothing isolates persistent rate-of-change direction. A fresh TRIX zero-axis crossing must coincide with both a non-choppy CHOP regime and a sufficiently strong ADX regime. The author describes locked ATR-derived exits, not any independently established profitability. The public description does not provide a complete numeric configuration.

### Research interpretation

A selective momentum-transition long: only a fresh positive TRIX crossing while CHOP is low and ADX is high may open the book. An ATR-based close-price bracket gives a frozen risk/reward reference without assuming that Hummingbot can reproduce the source's intrabar stop/limit execution. The trade-off is that a large intrabar loss is not bounded at the bracket level and may exceed the intended risk before the next completed close.

## Signal

All values use a contiguous series of completed BTCUSDT spot 1d OHLCV bars, with t indexing the latest completed bar. No volume is read by any signal.

- EMA15 of close is recursively alpha=2/16, seeded with the arithmetic mean of its first 15 defined observations; the second and third EMA15 are recursively applied to the preceding layer with the same seed convention. TRIX_t = 100*(EMA3_t/EMA3_(t-1) - 1); undefined or nonpositive denominators make the signal ineligible, never zero-filled. Long-cross_t = (TRIX_(t-1) <= 0 and TRIX_t > 0), with strict current positive crossing.
- TR_t = max(high_t-low_t, abs(high_t-close_(t-1)), abs(low_t-close_(t-1))). Wilder RMA14 of TR is ATR14: first value is SMA of 14 valid TR values, thereafter (13*previous + current)/14. For CHOP14, range_t = max(high over t-13..t)-min(low over t-13..t), sumTR_t = sum(TR over t-13..t); CHOP_t = 100*log10(sumTR_t/range_t)/log10(14). Undefined/nonpositive range or sum makes entry ineligible.
- Wilder ADX14: up=high_t-high_(t-1), down=low_(t-1)-low_t; +DM=up if up>down and up>0 else 0; -DM=down if down>up and down>0 else 0; smooth TR/+DM/-DM with Wilder RMA14; +DI=100*RMA(+DM)/RMA(TR), -DI likewise; DX=100*abs(+DI-(-DI))/(+DI+(-DI)); ADX14=Wilder RMA14 of DX. Zero/undefined denominators produce ineligible values, not fabricated zeros.
- ENTRY_t = flat AND Long-cross_t AND CHOP14_t < 38.2 AND ADX14_t > 25, all evaluated on the same completed bar. Exactly equal to either threshold fails. No later entry is allowed merely because a filter turns green after the TRIX edge has passed.
- On confirmed entry fill at the effective completed close P, freeze ATR14_t as A, stop=P-1.5*A and target=P+3.0*A. Require A>0 and P>1.5*A or do not enter; this ensures a strictly positive stop. Do not recompute A, stop or target until the position is flat.
- EXIT_t = long AND (close_t <= frozen_stop OR close_t >= frozen_target), evaluated only on completed bars strictly after the entry bar. Stop has priority if needed, but the two price conditions cannot both hold for a valid bracket. Sell the full held base quantity at that completed close, not at the crossed threshold. There is no signal/opposite-cross exit, intrabar stop, resting limit, trailing stop, breakeven, time stop, margin stop or discretionary override.
- Event priority: if long at bar start, evaluate EXIT only; no same-bar re-entry. If flat at bar start, evaluate ENTRY only; no same-bar exit. No event occurs on an invalid bar. If entry and an opposite TRIX condition appear in any hypothetical same-bar evaluation, only the stated long-cross entry predicate is relevant.
- Controller-memory state is FLAT or LONG(quantity=0.001 BTC, frozen stop, frozen target, fill-ledger reference). Entry while long is ignored; exit while flat is ignored; max one open position; no pyramiding, no DCA/BO/SO ladder, no concurrent orders, no cooldown. After exit, re-entry requires a fresh future eligible TRIX cross; the previous crossing cannot be reused. The state transition occurs on a confirmed simulated MARKET fill, not merely on submission; missing/failed fill leaves the prior state and suppresses a duplicate pending order.

## Required data

BTCUSDT Binance spot 1d high, low, close and original kline open timestamps, with continuous 86400-second UTC daily bars. Required trailing history is at least 120 fully completed bars; first 120 are flat with no order, even if indicator seeds are defined earlier. No multi-timeframe, multi-symbol, open interest, order-book, funding, mark/index price, future extrema, centered window, repainting or trained model. All recursive filters are forward-only, with no lookahead or full-sample normalization.

Venue REST klines label the OPEN timestamp (pinned BinanceSpotCandles parser reads row[0]); normalize the strategy's decision/fill effective timestamp to that bar's open timestamp + 86400 seconds BEFORE feeding the engine's prepared candle rows. No bar is eligible before that effective time. A missing/non-monotone bar or a gap versus the preceding expected UTC daily timestamp blocks both signals and fills until a fresh 120-bar contiguous warmup is available; a preexisting long remains in its previous state during the gap, with no fabricated close. Data-quality gaps can therefore prolong an unprotected position and are a declared limitation. If the normalized completed close is unavailable, no order or substitute price is permitted.

## Execution assumptions

Pinned Hummingbot distribution/package 20260920, VERSION dev-2.17.0, source commit 8b0e067e80ab62f10846d518dcb5a8218527ddb3 in HCH725/hummingbot. This run read the pinned engine's OrderExecutorSimulator, BacktestingEngineBase, ExecutorSimulatorBase, BinanceSpotCandles and constants, and BacktestingDataProvider. Earlier independent repo PR #414 documents wheel-to-commit byte identity (902/902 Python files) at the same pin; that binary check was not rerun this cycle and is not presented as fresh evidence.

Demonstrated engine path: Binance spot connector 'binance', trading_pair 'BTC-USDT', BinanceSpotCandles interval '1d' (pinned constants lists it), completed-bar OHLC feed, a strategy-specific DirectionalTradingController emitting CreateExecutorAction(OrderExecutorConfig with ExecutionStrategy.MARKET, side BUY or SELL, amount 0.001), OrderExecutorSimulator, and BacktestPositionHold accounting. In the pinned order simulator, MARKET fills on the first supplied dataframe row at that row's close, records filled_amount_quote = amount*close and cum_fees_quote = trade_cost*filled_amount_quote, then returns POSITION_HOLD; BacktestingEngineBase simulates actions over processed row slices and nets held BUY/SELL fills with incremental average cost/realized gross PnL. The required derived data normalization is an explicit pre-backtest input rule; BacktestingDataProvider exposes candle dataframes and BacktestingEngineBase prepares the timestamp index from the candle feed. This is a completed-bar MARKET-close *simulation*, not a claim of executable exchange closing-auction fills or of source-native Pine intrabar bracket equivalence. No new maker, next-open, intrabar, futures or shared-capital primitive is required.

Ledger control: maintain fill-confirmed quantity and entry/frozen-bracket state independently of the default terminated-executor view (which defaults to 3600 seconds and can drop prior 1d fills from the controller's view); do not infer flat/long from that bounded view. The engine's POSITION_HOLD update can lag a row, so the strategy controller must rely on its own confirmed-fill ledger and suppress duplicate pending actions. A downstream strategy-specific controller remains not-implemented; this record describes the pinned, already verified MARKET/hold primitives, not a deployed controller.

Costs and accounting: deterministic research trade_cost=0.001 quote-notional per BUY and SELL fill; zero modeled slippage is an explicitly artificial close-price simulation assumption, NOT a measured exchange slippage claim; actual venue taker fees, spread and price impact are unknown. No funding exists on unleveraged spot; no futures, leverage, margin, liquidation or mark-price economics are claimed. This OrderExecutor path does not perform live exchange lot/tick quantization; 0.001 BTC is a model base amount and venue execution permissions are not established. Net realized quote PnL for matched fills = BacktestPositionHold.realized_pnl_quote - BacktestPositionHold.cum_fees_quote. Do not use the OrderExecutor's gross-only net_pnl_quote field or BacktestingEngineBase total_pnl as a fee-inclusive closed-trade equity series. Floating-point amount*price conversion can leave tiny accounting residuals; the controller's fill ledger, not exact engine net-zero equality, governs entry eligibility. No invented fill, cost, zero funding payment or price is treated as realized.

## Evidence

### Source-reported

TradingView stable script 1BJZkv2N, BVLabs, public description published 2026-04-10 and updated 2026-08-06, explicitly describes triple-EMA one-bar TRIX ROC zero-cross, CHOP below threshold, ADX above threshold, directional entries and locked ATR bracket. It supplies no complete accessible Pine code in the fetched page and no verified numeric default settings. No source-reported return or win rate is used.

### Independently reproduced

This cycle independently read the pinned Hummingbot source paths at commit 8b0e067e80ab62f10846d518dcb5a8218527ddb3 and confirmed the MARKET-close first-row fill, 1d Binance spot interval and open-time parser, row-wise controller action processing, fee accumulation, POSITION_HOLD average-cost and realized-PnL netting, and the 3600-second default terminated-executor view. The earlier PR #414 records a wheel-to-source hash verification at this exact engine commit. No TradingView Pine execution, Qlib/Hummingbot backtest, live execution or performance reproduction was performed this cycle.

### Negative evidence

- Native source's immediate ATR strategy.exit stop/limit semantics are not claimed: this derivative deliberately checks completed CLOSE only and can exit far beyond its nominal stop/target.
- Numeric 15/14/14/14, 38.2/25, 1.5/3.0, 120 bars and fixed 0.001 BTC are researcher choices, not author defaults.
- Original can trade both directions; short is explicitly disabled here. Original entry fill mode and source pyramiding are not recoverable from the visible listing; this record substitutes and discloses its own state/fill model.
- The nearest admitted TRIX strategies trade TRIX-vs-signal or twin-TRIX crosses and different exits; this is a TRIX-vs-zero edge with *both* CHOP and ADX gates and a frozen ATR close bracket, not a trivial period retune.
- No backtest statistics, fee realism, source-native equivalence, Qlib parity or trading authorization is claimed.

## Falsification plan

With this derived configuration frozen before screening, compare its net-of-declared-cost event sequence against (a) TRIX15 zero-cross without CHOP gate, (b) without ADX gate, and (c) identical entries with a signal-based exit instead of the fixed ATR close bracket. Report complete bar coverage, missed signals, trades, costs and drawdown; no retrospective selection of favorable data or source-native claims. These are future downstream experiments, not executed Scout work.

## Crypto portability

BTCUSDT Binance spot 1d is the single pinned research market. Long-only, unleveraged, fixed base quantity and completed UTC day-close signals are model-compatible with the cited Binance spot MARKET/hold path; no assertion of actual liquidity, minimum notional, fills or venue fees. Other markets and intervals are untested research variants, not disallowed categories.

## Limitations

No Pine source-body access; all source-native details are limited to the author's public description. This record is explicitly independent and does not repair missing original defaults by guessing. The frozen ATR levels are evaluated on daily CLOSE, not touched intrabar, so gaps or fast adverse moves can exceed the nominal stop; missing data while holding is especially hazardous. EMA/RMA seed conventions, market, cost model and risk parameters are researcher-defined and must not be retroactively described as original. No profitability, canonical futures accounting, strategy-specific Qlib implementation or event-level Qlib/Hummingbot parity is demonstrated.

## Implementation status

not-implemented. HB_READY PASS here denotes a completely declared derived strategy expressible through already verified pinned model primitives, not a finished executable recipe. If later selected for Qlib research without an implementation, use the existing IMPLEMENTATION_NEEDED engineering route; validate representative new engine capabilities before mass screening and eventual event-level parity as required.

## Adoption boundary

status: research-only; adoption: not-approved; approval_scope: research-only. No Paper, Testnet or Live permission.

## Related Wiki records

None; Scout made no Wiki write.

## Sources

- https://www.tradingview.com/script/1BJZkv2N-Alpha-TRIX-Strategy/
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- https://github.com/HCH725/alpha-strategy-research/pull/414 (earlier independent pinned-wheel verification)
