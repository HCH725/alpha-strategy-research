---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: PivotBoss outside-reversal range-expansion BTCUSDT spot 4h long-flat close-fill derivative
created: 2026-10-27
updated: 2026-10-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
status: research-only
confidence: medium
source_as_of: 2019-12-26
sources:
  - https://www.tradingview.com/script/epeZP4Ea-Outside-Reversal/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# PivotBoss outside reversal with 1.25x Wilder range-expansion gate — independent BTC-USDT spot 4h long-flat derivative

## Provenance

**Primary public TradingView identity:** strategy `Outside Reversal` by **adiwajshing**, stable script ID `epeZP4Ea`, page https://www.tradingview.com/script/epeZP4Ea-Outside-Reversal/ (title `Outside Reversal — Strategy by adiwajshing — TradingView`). Author one-line description (page `og:description`, read this cycle): `The PivotBoss outside reversal strategy`. Page metadata read this cycle (2026-10-27, 324,213-byte HTML): `script_type=strategy`, `script_id_part=PUB;Fh3mq8x51jejHRvEtClria853FhllV1P`, `version_maj=1`, `created_at=2019-12-26T19:24:23Z`, 63 likes / 0 comments / 2,629 views, OPEN-SOURCE badge, `access=1`.

**Complete Pine block retrieved verbatim this cycle** via the public pine-facade endpoint for that `script_id_part` at version 1 (`kind=strategy`, `scriptAccess=open_no_auth`, `created==updated==2019-12-26T19:24:21Z` — version 1.0, never edited, immutable): 17 lines, 624 bytes, `//@version=4`. The full traded rule, quoted for gate evidence (short plotting lines omitted, nothing else):

```pine
strategy("Outside Reversal", overlay=true)
barMultiplier = input(1.25)
barsBack = input(50)
myCandleSize = high-low
averageCandle = rma(myCandleSize, barsBack)
longSignal = low < low[1] and close > high[1] and (myCandleSize >= averageCandle*barMultiplier)
shortSignal = high > high[1] and close < low[1] and (myCandleSize >= averageCandle*barMultiplier)
strategy.entry("LONG", strategy.long, when=longSignal)
strategy.entry("SHORT", strategy.short, when=shortSignal)
```

**Token census over the 17 lines (read, never extended):** 1 `strategy(` (no `pyramiding=` → Pine default `0` governs; no `process_orders_on_close` → Pine default next-bar-open fill governs; no `commission`/`initial_capital`/`currency`/`default_qty` → Pine defaults govern, all replaced by the house model below); 2 `input(` with frozen literals `1.25` and `50`; 1 `rma(`; 2 `plotshape` (display only); 2 `strategy.entry` (LONG/SHORT); 0 `strategy.exit` / 0 `strategy.close` / 0 `strategy.order`; 0 `request.*` / 0 `security(` / 0 `time(` / 0 `timestamp(` / 0 `volume`. No timeframe binding ships anywhere in the code — the script runs on the chart timeframe, so the 4h research frame below is a disclosed researcher pin, never a source claim.

**Declared independent derivative v1, NOT source-native/lossless:** retain the source's exact `1.25` multiplier, `50`-bar Wilder range average, strict one-sided extreme comparisons, inclusive expansion gate, and the long/short signal pair; independently freeze **Binance BTC-USDT spot 4h, LONG/FLAT only** (the source SHORT leg is disabled — its only function in this book is the SELL signal, disclosed below), **0.001 BTC** fixed size, **10,000 USDT** unborrowed initial cash, **100-bar** warmup, **MARKET same-completed-close fills**, hypothetical **0.001/side** fee, and the state/cash/precision rules below. The Pine-default next-bar-open fill is converted to the house same-completed-close convention (disclosed timing change, same class as the admitted #518/#516 records — never a claim of source fill parity). All changes are part of this **separate strategy**, not evidence that the source script is expressible unchanged.

**Immutable research identity:** `TV-epeZP4Ea-adiwajshing-v1.0-20191226 | derived-v1-outside-reversal-rma50-x1p25 | BTC-USDT-binance-spot-4h | LONG on low<prevLow AND close>prevHigh AND range>=1.25*avgRange50 | FLAT on mirrored shortSignal | Q=0.001 BTC | close-fill | fee=0.001 | 2026-10-27`. Changing any component changes the derivative identity.

**Pre-write dedup:** base `main@7c9d91d8b34f70f79b14d5f60c21b8eaa13f5` in sync with `origin/main`; 385 root-level Markdown files = 383 strategy records + 2 READMEs, README static count 383. Case-insensitive pool searches for `outside reversal`, `outside-bar`, `epeZP4Ea`, `adiwajshing`, `myCandleSize`, `rma(myCandleSize`, `average range`, `rma(range` return zero strategy records. `PivotBoss` appears once — prose-only, in `wick-reversal-hammer-shooting-star` line 96 fencing the different-author `PivotBoss Wick Reversal Setup` (wick fractions, explicitly "different, unpinned rules"). `close > high[1]` appears in main only as the EXIT leg of `ultimate-oscillator-oversold-breakout` (prior-high retake on an oscillator dip), never as an outside-bar entry and never with a range-expansion ratio. `barsBack` appears once, incidentally inside `i_wfBarsBack` in the Williams-fractal record (shared Pine vocabulary, bracket-exit two-sided system — different rule). Ten open `research/*` PRs inspected by title/scope (#353, #350, #331, #304, #251, #92, #89, #63, #49, #48) — none is TradingView-sourced and none trades an outside-bar/range-expansion rule. The off-main branch `research/chatgpt-tradingview-lw-outside-day-atr-close-20261025-2117` (SpeculationLab X4ulJUXd, never PR-reviewed, never merged) is a different source AND a different rule: bearish close below the prior low, strict double-extreme outside bar, 1.5x prior-body filter, 1.5-ATR stop / 3-ATR target bracket exit on 1d, with unretrieved Pine and a researcher-invented body threshold. This candidate uses the opposite close direction, a Wilder-average range gate, a signal-flip exit, and fully retrieved verbatim code. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its page and code print: the PivotBoss outside-reversal setup — a bar undercutting the prior low then closing beyond the prior high, on a range at least 1.25 times its 50-bar Wilder average, is a long signal; the mirror is a short signal. The page ships no sample, window, trade count, performance figure, or risk paragraph — this record adopts no source-reported performance (see Evidence).

### Research interpretation

A one-bar range-expansion reversal catcher, long-only. Unlike conjunction records (RSI AND band, ADX AND rail), the trigger needs no oscillator confirmation — any sufficiently stretched outside-close bar fires. Unlike pure touch/reclaim records, the 1.25x Wilder gate refuses small-range wiggles that happen to close beyond the prior extreme. Unlike bracket-exit records, the position's entire fate rests on the mirrored signal: a drift that never prints the reverse pattern is held, not stopped. The coded consequence is a buyer of confirmed expansive upside rejection that exits only on confirmed expansive downside rejection.

## Signal — Gate 1, fully pinned derivative

**Input:** one UTC Binance BTC-USDT spot 4h OHLCV stream `O[t],H[t],L[t],C[t],V[t]`; `t` is a completed bar. Validate finite `O,H,L,C>0`, `H>=max(O,C)`, `L<=min(O,C)`, `V>=0` finite, strictly consecutive open-time timestamps 14,400 seconds apart, no duplicates. Reject the run before feature preparation on any missing/invalid/nonconsecutive bar; no dropna bridging, synthetic bars or price fallback.

**Range and Wilder average (researcher-pinned Pine-documented `rma` semantics; only the call `rma(myCandleSize, 50)` and the literal `50` are source facts):** `R[t]=H[t]-L[t]` (>= 0 by validation). `AR[49]=mean(R[0..49])` (SMA seed of the first 50 ranges); for `t>49`, `AR[t]=(R[t]+49*AR[t-1])/50`. Undefined (NaN) before index 49; every NaN comparison is false — no signal can form early. The average is self-inclusive (reads the current bar's range), exactly as the source line does.

**Completed-bar long predicate `Lg[t]`** (all true, `t>=50`): `L[t]<L[t-1]` (strict), `C[t]>H[t-1]` (strict), `R[t]>=1.25*AR[t]` (non-strict — equality passes, source `>=`), `AR[t]` finite. **Completed-bar flatten predicate `Sh[t]`** (all true, `t>=50`): `H[t]>H[t-1]` (strict), `C[t]<L[t-1]` (strict), `R[t]>=1.25*AR[t]`, `AR[t]` finite. No volume/funding/indicator beyond this path is read anywhere in the gating.

**Mutual exclusivity (verified analytically):** `Lg` needs `C[t]>H[t-1]` while `Sh` needs `C[t]<L[t-1]`; `H[t-1]>=L[t-1]` always, so both can never hold on one close. No priority ordering is needed and no same-bar round-trip can occur. A both-extremes outside bar (`L[t]<L[t-1]` AND `H[t]>H[t-1]`) may occur, but the close condition alone decides which (if either) predicate fires.

**Degenerate windows:** a 50-bar flat stretch (`AR[t]==0`) makes the gate `R[t]>=0`, always true — the predicates stay well-defined (no division exists anywhere in the path). Undefined `AR` never satisfies the finite gate.

**Direction (Gate 2):** BUY only; SELL only to close the confirmed long. No short, borrowing, futures, hedge, leverage, negative inventory or cross-market trade. The source SHORT entry is adopted solely as this book's flatten signal and never opens exposure.

**Entry (Gate 3):** with state FLAT, no pending order, post-warmup, `Lg[t]` true and `cash >= Q*C[t]*(1+f)` (`Q=Decimal("0.001")`, `f=0.001`), issue one MARKET BUY of exactly `Q` at the same row's observed completed `C[t]` under the pinned historical simulator convention. Cash shortfall → no order, stay FLAT (deterministic skip, run continues — see cash model). On **confirmed full fill**, record `entryPrice=C[t]`, state LONG, cash minus `Q*entryPrice*(1+f)`. Do not infer a fill from an order intent. A missing/failed/partial fill, invalid price or undefined fee **aborts** this bounded research run instead of inventing a trade or retry rule.

**Exit (Gate 3, the source's only close path):** while LONG, on each **strictly subsequent** completed bar, if `Sh[t]` true, SELL the entire confirmed `Q` at that bar's completed close; on confirmed fill, cash plus `Q*C[t]*(1-f)`, state FLAT. Entry-bar `Sh` is never tested (predicates are mutually exclusive, so nothing is lost). No stop-loss, no take-profit, no trailing, no time exit, no partial exit, no averaging, no forced end-of-data liquidation, no silent executor default — the 17-line source ships zero `strategy.exit`/`strategy.close`, and this derivative adds none. Hold otherwise, without time limit.

**State (Gate 4):** `FLAT`, `BUY_PENDING`, `LONG`, `SELL_PENDING`. Initialize `FLAT` after 100 valid completed bars. A BUY request transitions to `BUY_PENDING`; only a confirmed MARKET fill at that same completed close transitions to LONG. While LONG, all entry predicates are ignored. SELL request transitions to `SELL_PENDING`; only a confirmed filled SELL of the complete 0.001 BTC returns to FLAT. No same-bar SELL+BUY, no pyramiding (Pine default 0, adopted explicitly), **no DCA/safety orders (explicitly disabled — the downstream 6%+6%+6% house overlay is not active in this admission and never silently overrides single-unit semantics)**, no concurrency, no compounding, no session/cooldown (Pine ships none — explicitly none, not invented). A pending order prohibits additional actions. Re-entry is allowed on any later bar after a confirmed FLAT. An end-of-sample LONG is marked at the last real valid close, not closed with an invented fill.

## Required data / Gate 6 causality

**Warmup:** minimum 100 contiguous completed 4h bars before the first actionable bar; structural minimum is bar 50 (50 ranges seed the Wilder average plus one reference bar for `[1]` offsets). No warmup-bar trades; all rolling values start from the actual first historical bar, not from full-sample fitted statistics.

Binance Kline `timestamp` is the **bar-open** `T[t]` (pinned `BinanceSpotCandles._parse_rest_candles` reads row[0]); a bar's OHLC and derived average become available no earlier than `T[t]+14400s`. All decisions and the synthetic model fill are effective at that **completed-bar close**. The backtest engine's backward `merge_asof` operates on raw open-time indices, so a strategy-specific controller must gate features by close availability and not mistake open-time index `T[t]` for the decision time. No incomplete bar, higher-timeframe partial, future extremum, negative shift, repainting or same-bar intrabar touch is used. Pine's own default (no `process_orders_on_close`) fills entries at the next bar's open; this derivative's same-row-close fill is a **synthetic completed-bar convention replacing it** (disclosed above), not a real-world claim that a post-close order could capture the just-observed historical close. If this effective-time discipline cannot be enforced, Gates 5/6 fail in implementation.

## Execution assumptions / Gate 5 pinned Hummingbot path

**Exact bounded engine:** Hummingbot package label `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. Prior merged Alpha PRs **#414/#417** document package/source correspondence and representative engine validation for this source/package path, reused by sibling admissions **#483**, **#491**, **#494**, **#516** (4h spot) and **#518** (1m spot); this Scout **did not independently rehash** the wheel or run a backtest, except that `constants.py` was re-fetched at the pinned commit this cycle and reproduces blob `6d505dff42b60b356931df13eeeecd1e28b426f9` with `4h` in `INTERVALS`. A different deployed package must be revalidated.

- **Market/feed:** `BinanceSpotCandles` parses Binance `/api/v3/klines` open-time and OHLCV. Connector `binance`, pair `BTC-USDT`, one spot 4h stream. No funding or perpetual margin/mark/index, no order-book/volume-dependent decision, no multi-market or mixed-timeframe synchronization.
- **Controller path:** `BacktestingEngineBase.run_backtesting` → `controller.update_processed_data` → `prepare_market_data` → per-row `update_state` → `determine_executor_actions` → `CreateExecutorAction(OrderExecutorConfig)` → `OrderExecutorSimulator.simulate`. A **strategy-specific, not-yet-implemented** controller must calculate the exact range/Wilder-average/state and perform time gating. The generic executor does not calculate the strategy.
- **Orders (OrderExecutor only):** `OrderExecutorConfig` with `side=BUY/SELL`, `position_action=OPEN/CLOSE`, `amount=Decimal("0.001")` (the fixed initial and only unit size), `connector_name="binance"`, `trading_pair="BTC-USDT"`, `execution_strategy=MARKET`, `price=None`, `leverage=1`. The MARKET `OrderExecutorSimulator` fills fully at the first provided row's **close** and ends `CloseType.POSITION_HOLD`; not a live or intrabar fill. On confirmed fills, `BacktestPositionHold` nets base amounts, tracks weighted entry, realized gross PnL and fees. Do not infer a position from the order request; controller must use confirmed executor/hold state, with a persistent ledger or `terminated_executors_window=None` rather than relying on the default 3600s view for 4h bars.
- **Cash model (researcher-declared):** initial quote cash is exactly `10,000 USDT`, unborrowed; no other capital exists. BUY fill deducts `Q*fill_close*(1+f)`; SELL fill credits `Q*fill_close*(1-f)`; all accounting in Decimal. A BUY is requested only when `cash >= Q*C[t]*(1+f)`; otherwise the signal is skipped and the book stays FLAT (deterministic given data — the same close and signal always produce the same event for the pinned cash path). No leverage, no borrowing, no negative cash: any path that would require it aborts the run instead.
- **Fees and accounting:** pin `trade_cost=0.001` per filled BUY and SELL, exactly the simulator's `cum_fees_quote=trade_cost*amount*observed_close`. This is **hypothetical 0.1% each side**, not actual Binance fee; no slippage/spread modeled, **not** evidence of zero real slippage. For one round trip of 0.001 BTC: gross `0.001*(sell_close-buy_close)`; explicit research net `gross - 0.001*0.001*(buy_close+sell_close)`. The pinned engine's `summarize_results.net_pnl_quote` for POSITION_HOLD can reflect **gross** matched PnL while reporting fees separately; its `pnl_timeseries` also does **not** guarantee a complete fee-inclusive cumulative equity series after flat transitions. **Never** call either output fee-inclusive net equity without reconstructing from actual fill ledger plus recorded fees. Spot funding is **not applicable**, never fabricated as futures zero.
- **Precision research model (researcher-declared; live filters verified this cycle, live compatibility NOT claimed):** Binance BTC-USDT spot filters read live 2026-10-27 — `tickSize 0.01`, `LOT_SIZE stepSize 0.00001 / minQty 0.00001`, `NOTIONAL minNotional 5.00` with `applyMinToMarket=true`. In this model: `Q=0.001 BTC` is exactly 100 stepSize increments (exactly representable, so no lot rounding occurs in-path); fills occur at the raw observed completed close (tick rounding idealized away and disclosed as such); the min-notional rule is an active assertion `Q*C[t] >= 5 USDT` (i.e. `C[t] >= 5000`), checked at run start and before every BUY — violation aborts the run; partial fills do not exist in-model (any non-full fill aborts). Real-exchange precision behavior, fee tiers, market impact and slip
...[truncated 3880 chars]