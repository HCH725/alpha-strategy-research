---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: QuantifiedTrader Random Walk Index 14 hysteresis long-flat BTCUSDT 1d independent derivative
created: 2026-10-26
updated: 2026-10-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-26
sources:
  - https://quantifiedtrader.com/backtest/strategies/random-walk-index
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# QuantifiedTrader Random Walk Index 14 hysteresis — independently specified long-flat derivative

## Provenance

**First-party source:** QuantifiedTrader public strategy-library page, *Random Walk Index*, read live 2026-10-26 (42,940 bytes HTML fetched this cycle; byte-identical to the pre-existing scratch mirror, methodology code character-identical): https://quantifiedtrader.com/backtest/strategies/random-walk-index . No login, paywall, or private content was involved.

**Facts actually supplied by the source page:** the strategy is backtested on **daily OHLCV** price data across major US equity indices and ETFs; entry/exit signals are generated with **no lookahead bias**; **trades execute at the open of the bar following the signal**; performance metrics are computed per symbol; **transaction costs and slippage are not modeled**. The signal prose states the Random Walk Index compares actual price movement to what would be expected in a random walk, that **RWI above 1 indicates a non-random directional move (a true trend)**, and that the strategy **enters long on breakout and exits when RWI drops below 0.5**. The pinned decision code is exactly: `n = 14`; `atr = _atr(h, l, c, self.n)`; `rwi_high = (h - l.shift(self.n)) / (atr * np.sqrt(self.n)).replace(0,1e-10)`; entry `self.rwi[-1] > 1 and not self.position -> buy()`; exit `self.rwi[-1] < 0.5 and self.position -> position.close()`. No short/sell-short call, no stop/target/trailing/time call, and no sizing literal ship anywhere in the rule. Volume is read nowhere in the rule (High/Low/Close only).

**Unpinned-helper gap (disclosed, not repaired):** the page calls a shared site helper `_atr(h, l, c, n)` whose body is printed on no strategy page this cycle (verified by whole-page search of the live fetch and of sibling QuantifiedTrader ATR/Keltner/volatility pages, which reference the same helper without defining it). This derivative therefore does **not** claim byte-equivalence with the site's helper. It freezes the standard Wilder RMA true-range recursion below as an explicit researcher choice, with the seed, divisor guard, warmup, and flat-market consequences fully specified and arithmetically checked in scratch this cycle. A differently-smoothed ATR would be a different, unpinned rule.

**Independent derivative, not source-native reconstruction:** the researcher explicitly chooses (1) Binance BTC-USDT **spot 1d**, LONG/FLAT rather than the source equity-index universe (no timeframe adaptation — the source is already daily); (2) the single-leg RWI(14) construction below with Wilder RMA ATR, the code-faithful `1e-10` denominator guard, and undefined-never-trades treatment; (3) strict level `RWI > 1.0` LONG entry from FLAT and strict level `RWI < 0.5` LONG exit (both levels exactly as coded — entry is a level hold, not a cross-up edge, and is specified as such); (4) **close-effective** MARKET simulator fills instead of the source next-open execution; (5) fixed **0.001 BTC** sizing with no compounding instead of any framework-default share sizing; (6) no stop/target/trailing/time exit, no DCA and no short; (7) 60 valid completed daily bars of warmup, data-gap treatment and re-entry rules below; (8) pinned simulator `trade_cost = 0.0001` per filled side as a **researcher-selected house research input** — the source models no costs, so no fee value is attributed to it. All researcher-selected order rules and disabled behaviors belong to this independent derivative alone.

**Immutable strategy identity:** QT-random-walk-index | derived-v1-rwi14-hysteresis-enter1.0-exit0.5 | BinanceSpot-BTC-USDT-1d | 2026-10-26. Any changed input, window, smoothing, comparator, clock, position rule, cost or fill model creates a different derivative.

## Economic mechanism

The source hypothesizes that displacement beyond √N-scaled average true range marks a statistically non-random directional move worth riding, and that collapse back under half that expectation means the trend thesis has failed. This derivative holds the long only while displacement stays above the exit floor, entering only on fresh super-unit prints and exiting on the first sub-0.5 print. It is not a proven edge; long exposure can lose substantially and the declared derivative has no protective stop. No QuantifiedTrader reported performance is reproduced or independently claimed.

## Signal

**Gate 1: fully frozen, deterministic formulas.** Use one consecutive UTC daily BTC-USDT spot OHLCV stream; bar t opens at UTC timestamp T[t], with all O/H/L/C/V only available for decisions at effective timestamp T[t]+86400 seconds. Rolling windows include the current **completed** bar and exclude all future bars. √14 ≈ 3.741657387 is a frozen constant.

- TR[t] = max(high[t]−low[t], |high[t]−close[t−1]|, |low[t]−close[t−1]|) for t ≥ 1; TR[0] is undefined (no prior close) and is never read.
- ATR[14] = mean(TR[1..14]) — the Wilder seed over the first fourteen defined true ranges; ATR[t] = (ATR[t−1]×13 + TR[t])/14 for t ≥ 15 (researcher-frozen Wilder RMA; see the helper-gap disclosure above — no equivalence with the site helper, TA-Lib, or any framework ATR is claimed).
- DEN[t] = ATR[t]×√14, except exactly `0`, which uses `1e-10` (code-faithful zero-guard for the `.replace(0,1e-10)` denominator treatment, never invented). DEN[t] is exactly zero only if every true range in history is zero (perfectly flat market).
- RWI[t] = (high[t] − low[t−14]) / DEN[t], defined for t ≥ 14; earlier bars have no RWI print and never decide.
- **LONG entry from FLAT only:** RWI[t] > 1.0, after the 60-bar warmup. This is a **level**, not a cross — any flat bar printing above 1.0 enters, exactly as the source `if self.rwi[-1] > 1 and not self.position` does. Exactly `1.0` never enters.
- **LONG exit:** RWI[t] < 0.5. Strict: exactly `0.5` never exits; the exit is a level — the first sub-0.5 print after entry closes the unit, exactly as the source `elif self.rwi[-1] < 0.5 and self.position` does.
- Entry and exit can never co-fire: entry needs RWI[t] > 1.0 while exit needs RWI[t] < 0.5 on the same bar, disjoint by arithmetic, so no tie-break pin is required. If an exit condition occurs while FLAT it is a no-op; if an entry condition occurs while LONG it is a no-op. At most one filled order per completed bar.
- **Flat-market consequences (specified, verified in scratch — never a false no-op claim):** an all-flat history prints ATR = 0, DEN = 1e-10, numerator 0, hence RWI = 0.0: from FLAT nothing enters (0.0 is not > 1.0); while LONG the position exits on the first evaluated bar (0.0 < 0.5). A lone uptick after a flat stretch divides a small nonzero displacement by a near-zero Wilder ATR and prints a large RWI (scratch demonstration: +0.05 tick after flat prints RWI ≈ 3.74 and enters) — this is the code-faithful guard consequence, disclosed, not patched away.
- Start FLAT; require **60 consecutive valid completed daily candles** before the first decision (covers the 15-bar definability minimum — L-shift-14 plus ATR seed over bars 0..14 — with Wilder transient-decay margin; the same 60-bar rationale as the sibling single-asset RWI record, applied here to a different construction). A gap, duplicate/non-monotonic timestamp, invalid OHLCV, or broken UTC daily cadence resets warmup for fresh entries and exits; if already LONG, hold without inventing gap fills and resume exit evaluation after a fresh 60-bar valid segment.
- **Cooldown:** none specified — explicitly none, not invented. Re-entry after any exit requires only FLAT state plus RWI > 1.0 on a later bar (level re-trigger, never a retrospective entry). No queued signals.
- **Position state:** FLAT -> PENDING_BUY -> LONG only on confirmed simulator full-fill BUY; LONG -> PENDING_SELL -> FLAT only on confirmed full-fill SELL. Pending states suppress all additional actions. The pinned simulator's MARKET path fills fully at the first supplied close; a sent action is not falsely equated to a fill in controller state. The controller must persist fill-derived state independent of the delayed positions_held view.
- **Risk and disabled behaviors (Gates 2–4):** exactly one spot LONG of **0.001 BTC** or FLAT; no short, margin, leverage, pyramiding, DCA, safety orders, simultaneous exposure, fractional/partial orders, scaling, stop loss, take profit, trailing stop, timeout, forced liquidation, maker/limit orders or end-of-sample SELL. No additional opposite-signal leg. No reinvestment/compounding. If still LONG on the final available completed bar, mark the position at the last valid close without inventing an exit trade.

## Required data and causality

**Gate 6:** Binance BTC-USDT spot 1d O/H/L/C/V with strictly increasing UTC midnight bar-open timestamps 86400 seconds apart. Each valid bar has finite positive O/H/L/C, high >= max(open,close), low <= min(open,close), high >= low, and finite nonnegative volume. The rule reads High/Low/Close only — volume is never an order-gating input (a key material distinction from money-flow records). RWI needs only the current plus trailing 14 bars; no t−1 comparison, no future data, no unconfirmed intrabar values, no lookahead joins, no model fitting, no hindsight detection. The zero-guard and never-trade-undefined treatments are specified derivative behavior. Missing close prices block signals and fills rather than defaulting to synthetic prices. One asset, one decision timeframe, no cross-asset synchronization, futures funding, external indicators, ML artifacts or order-book inputs.

## Execution assumptions and pinned Hummingbot compatibility

**Gate 5 is bounded to a real inspected pinned simulation path, not a deployment claim.** Admission policy identifies Hummingbot package label **20260920**, VERSION **dev-2.17.0**. The independently inspected source is **HCH725/hummingbot at commit 8b0e067e80ab62f10846d518dcb5a8218527ddb3**; its hummingbot/VERSION file reads dev-2.17.0 (verified this cycle via raw fetch at the pin). A package build digest was not available and this record does **not** claim that package 20260920 was byte-for-byte matched to this source commit or deployed. The engine-path claim is limited to this pinned source and previously reviewed matching research semantics.

- **Market/data:** BinanceSpotCandles constants.py maps the **1d** interval (INTERVALS bidict) and REST /api/v3/klines with symbol/interval/limit params (both verified this cycle at the pin); binance_spot_candles.py parses REST row[0] as timestamp with row[1..5] as O/H/L/C/V and WS kline keys o/h/l/c/v (verified this cycle). A strategy-specific controller must compute the declared single-leg RWI(14) features, verify contiguous completed bars and supply a single BTC-USDT spot 1d stream. The engine does not magically implement this displacement signal.
- **Controller/action/executor:** BacktestingEngineBase.simulate_execution iterates processed rows, calls update_state(row), controller.determine_executor_actions(), and CreateExecutorAction -> simulate_executor; OrderExecutorConfig with ExecutionStrategy.MARKET and BUY/SELL side routes to OrderExecutorSimulator (row path verified this cycle at the pin). The latter fills MARKET orders immediately at the first supplied row timestamp and **close** price, sets filled_amount_quote = amount×close, cum_fees_quote = trade_cost×filled_amount_quote, and CloseType.POSITION_HOLD. Full fill at one close is an explicit simulator convention, not proof of actual executable spot fills.
- **Timestamp caveat:** source candle timestamp is the **bar OPEN label**. BacktestingEngineBase.prepare_market_data uses merge_asof on timestamp_bt (verified this cycle); backward as-of joining alone does not establish that a completed close was known at the open. The required derivative controller gates the completed bar until T[t]+86400, and the resulting research event/fill ledger is explicitly normalized to that **close-effective** timestamp while using the simulator's same-row close price. This is a disclosed adaptation away from the source next-open execution and does not claim a real post-close order can fill at the already-observed close. No intrabar or lower-timeframe path is assumed.
- **Position and ledger:** BacktestPositionHold nets equal-base BUY and SELL ("Buys and sells of the same asset net out automatically. Realized PnL comes from matched buy/sell volume"), tracking average entry price, gross matched realized PnL and accumulated fees separately (verified this cycle at the pin). The engine's positions_held conversion is delayed; pin terminated_executors_window=None and use persistent pending/fill-confirmed controller state to avoid duplicate orders or losing prior fills. After a 0.001 BTC BUY at P_b and a 0.001 BTC SELL at P_s, modeled net quote PnL = 0.001*(P_s-P_b) - 0.0001*0.001*(P_b+P_s); do not misreport gross native net_pnl_quote or pnl_timeseries as fee-inclusive equity. An open position's marked equity carries the already-paid BUY fee.
- **Costs:** pin simulator trade_cost=**0.0001 per filled side** (0.01%, researcher-selected house research input — the source models no costs and no rate is attributed to it); this is **research cost input only**, not verified Binance realized commission. No separate simulator slippage is added, which is **zero additional modeled slippage**, not evidence of zero actual spread/latency/slippage. Spot funding is inapplicable (no fabricated futures funding). Binance minimum notional, lot/tick precision, exchange commissions, partial fills, liquidity and real trading viability remain unverified; do not infer live admissibility.
- **Reused independent path review:** HCH725/alpha-strategy-research PR **#417** merged 2026-10-24 after independent HB_READY review of this same pinned Binance spot 1d / MARKET first-close / POSITION_HOLD and fee-ledger research path. That verifies an **engine primitive**, not this new indicator, trade series, profitability, package digest or candidate-specific parity. This cycle additionally re-read the pinned VERSION, Binance spot candle constants/parser, backtesting engine row/action routing, OrderExecutorSimulator and BacktestPositionHold code at the pin.

## Evidence and six-gate summary

1. **Deterministic signals:** complete TR/Wilder-ATR(14)/DEN-guard/RWI(14) construction with frozen √14, strict super-1.0 entry level and strict sub-0.5 exit level defined above; the unpinned-helper gap is disclosed with a frozen researcher choice, and no Pine/TA-Lib/framework equivalence is claimed.
2. **Direction:** Binance BTC-USDT spot LONG/FLAT only, no short/margin.
3. **Entry/exit/risk:** RWI breakout-hold BUY, sub-0.5 SELL, all other stop/target/trailing/time legs disabled; no hidden defaults.
4. **Position:** fixed 0.001 BTC, single pending/filled state, no cooldown (explicitly none), level re-trigger re-entry, no DCA/concurrency.
5. **Pinned engine:** concrete source commit re-read this cycle, 1d Binance candle path, controller action, MARKET full-close fill, timestamp normalization, fee and POSITION_HOLD ledger limitations; no novel unverified execution primitive used.
6. **Causality:** 60 completed-bar warmup, finite/gap guards, no future reads, decision and research-fill effective at completed bar close.

**Source-reported:** only the page identity, daily-OHLCV/no-lookahead/next-open methodology, unmodeled-costs disclaimer, random-walk prose, single-leg RWI(14) code rule with the `1e-10` guard and long-only stance stated in Provenance. **Researcher-designed:** every market/fill/sizing/warmup/cost transfer plus the frozen Wilder ATR choice identified above. **Independently reproduced backtest performance:** none. **Historical survivor/HB Certified/Qlib parity:** none claimed. A stdlib-only scratch self-check this cycle confirmed ENTER/EXIT disjointness, flat-market RWI = 0.0 with no flat entries, forced-long exit on the guard path, tick-after-flat breakout entry, and warmup accounting across five fuzz seeds — pure logic validation, not a backtest.

## Deduplication

Main at immutable SHA **f30759fa3b78f1c5013a92b7492c0ba4df886dfb** contained **336** root strategy records; README static count **336**. Working-tree filename/content search for `random-walk` returns zero strategy records; `rwi` returns exactly one admitted record plus this proposal. GitHub issue/PR title search for `random-walk`/`rwi` across this repository returns zero items ever. Ten open research/* PRs were checked (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend, #89 Chandelier, #92 SSL channel, #251 Swift 2YMA, #304 forven CCI, #331 AdxSmas, #350 ClucMay, #353 Heracles Keltner-Donchian) — none carries this primary source or a single-leg RWI rule.

Nearest neighbors are **not equivalent**: `rwi-dominant-leg-state-following-two-sided-btcusdt-1h-2026-10-10` trades FMZ 440724's **dual-leg** dominant-leg comparison with a sub-threshold ranging gate, **two-sided** with full reversal, on **1h futures** — this record trades QuantifiedTrader's **single-leg** dual-threshold hysteresis (enter > 1.0, exit < 0.5), **long-flat only** with flat-capable hold bands, on **1d spot** (different source, signal construction, direction handling, horizon, and market — the same coexistence basis as the pool's four Donchian and two Williams-R records); `quantifiedtrader-twiggs-money-flow-21-zero-cross-long-flat-btcusdt-1d-2026-10-25` shares only the QT lane and the 1d spot long-flat derivative package — its TMF(21) is a **volume-weighted** typical-price-change accumulation ratio traded on a zero cross-up edge, while RWI reads **no volume at all** and trades displacement-level hysteresis (a volume-bar pinned at its range top prints TMF near +1 yet RWI from displacement alone); `forven-atr-breakout-channel` / `forven-atr-volume-breakout` trade price against ATR bands, not a normalized displacement oscillator with hysteresis levels; `chande-momentum-80-cross-reversal` is a two-sided summed-momentum threshold reversal, not a single-leg displacement hold/exit pair. Different formula, different edge-vs-state construction, different risk set: not a duplicate, paraphrase, or trivial parameter variant.

## Falsification plan

After separate downstream research authorization, compare the frozen single-leg RWI(14) hysteresis pair against (a) a dual-threshold ablation with the exit floor raised to 1.0 (pure level state, no hysteresis band) and (b) a volume-gated variant requiring same-bar volume above its 14-bar median, on predeclared IS/OOS partitions; verify that the hysteresis band and the volume-independence actually change entry/exit event times. Any new or unverified execution/data primitive requires representative Qlib/Hummingbot event-level validation before mass Qlib screening. Do not tune on OOS. No backtest was run by Scout.

## Crypto portability

Native crypto venue by declaration (Binance BTC-USDT spot 1d); no equity-to-crypto portability transform is asserted beyond the disclosed derivative identity. Spot semantics remove funding; minimum-notional, precision, liquidity and live viability remain unverified limitations, never assumed.

## Implementation status

Not implemented: no candidate-specific controller, feature module or replay artifact was created; only pinned generic engine files were read. The disclosed derived model must be implemented exactly if selected downstream.

## Adoption boundary

Frontmatter PASS is a **Scout-proposed six-gate research eligibility claim**, subject to independent Hermes Auditor review, not an independently approved merge. This is **not** a source-engine reproduction, actual Binance economics, profitable strategy, Qlib parity, HB Certified, survivor, deployment or Paper/Testnet/Live approval. No secrets, paid content, copied code block or private information included.

## Related Wiki records

None.

## Sources

- https://quantifiedtrader.com/backtest/strategies/random-walk-index — QuantifiedTrader public strategy-library source; methodology and decision code read live 2026-10-26 (42,940 bytes HTML); page carries no publication date so source_as_of is the read date.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned Hummingbot source (VERSION, spot candle constants/parser, backtesting engine, order simulator, position-hold ledger re-read this cycle).
- https://github.com/HCH725/alpha-strategy-research/pull/417 — independent review of the same pinned spot 1d MARKET-close POSITION_HOLD research primitive.
