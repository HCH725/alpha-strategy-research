---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: QuantifiedTrader Disparity Index 14 zero-cross long-flat BTCUSDT 1d independent derivative
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
  - https://quantifiedtrader.com/backtest/strategies/disparity-index
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# QuantifiedTrader Disparity Index 14 zero-cross — independently specified long-flat derivative

## Provenance

**First-party source:** QuantifiedTrader public strategy-library page, *Disparity Index*, read live 2026-10-26 (42,672 bytes HTML fetched this cycle; byte-identical to the pre-existing scratch mirror, methodology code character-identical): https://quantifiedtrader.com/backtest/strategies/disparity-index . No login, paywall, or private content was involved.

**Facts actually supplied by the source page:** the strategy is backtested on **daily OHLCV** price data across major US equity indices and ETFs; entry/exit signals are generated with **no lookahead bias**; **trades execute at the open of the bar following the signal**; performance metrics are computed per symbol; **transaction costs and slippage are not modeled**. The signal prose states the Disparity Index measures the **percentage difference between price and its N-period SMA**, that the strategy **enters long when the index crosses above zero (price reclaiming its average)**, and **exits when it drops back below zero**. The pinned decision code is exactly: `n = 14`; `self.disp = self.I(_disparity, self.data.Close, self.n)`; entry `self.disp[-1] > 0 and self.disp[-2] <= 0 and not self.position -> buy()`; exit `self.disp[-1] < 0 and self.position -> position.close()`. No short/sell-short call, no stop/target/trailing/time call, and no sizing literal ship anywhere in the rule. Close is the only price array read (`self.data.Close`); High/Low/Volume are read nowhere in the rule.

**Unpinned-helper gap (disclosed, not repaired):** the page calls a shared site helper `_disparity(close, n)` whose body is printed on no strategy page this cycle (verified by whole-page search of the live fetch; a sweep of all cached sibling QuantifiedTrader pages prints no `def _disparity` anywhere — the name occurs exactly once, at the call site). This derivative therefore does **not** claim byte-equivalence with the site's helper. It freezes the textbook definition from the page's own prose — `100*(Close − SMA(Close,14))/SMA(Close,14)` — as an explicit researcher choice, fully specified below. Unlike ATR/RMA-based helpers this choice carries no seeding ambiguity: a simple moving average over completed closes is arithmetically exact from the first full window, so no framework (TA-Lib or otherwise) equivalence question arises beyond the disclosed formula.

**Independent derivative, not source-native reconstruction:** the researcher explicitly chooses (1) Binance BTC-USDT **spot 1d**, LONG/FLAT rather than the source equity-index universe (no timeframe adaptation — the source is already daily); (2) the single-leg DISP(14) construction below with the code-faithful strict comparators and undefined-never-trades treatment; (3) a cross-up **edge** LONG entry from FLAT (`DISP[t] > 0` with `DISP[t−1] <= 0`, exactly as coded — not a level hold) with a strict sub-zero **level** LONG exit (`DISP[t] < 0`); (4) **close-effective** MARKET simulator fills instead of the source next-open execution; (5) fixed **0.001 BTC** sizing with no compounding instead of any framework-default share sizing; (6) no stop/target/trailing/time exit, no DCA and no short; (7) 60 valid completed daily bars of warmup, data-gap treatment and re-entry rules below; (8) pinned simulator `trade_cost = 0.0001` per filled side as a **researcher-selected house research input** — the source models no costs, so no fee value is attributed to it. All researcher-selected order rules and disabled behaviors belong to this independent derivative alone.

**Immutable strategy identity:** QT-disparity-index | derived-v1-disp14-edge-enter-level-exit | BinanceSpot-BTC-USDT-1d | 2026-10-26. Any changed input, window, comparator, clock, position rule, cost or fill model creates a different derivative.

## Economic mechanism

The source hypothesizes that a close reclaiming its 14-bar average from below marks renewed demand worth riding, and that falling back below the average means the reclaim thesis has failed. This derivative holds the long only while the close stays at or above its average, entering solely on the cross-up edge and exiting on the first sub-zero print. It is not a proven edge; long exposure can lose substantially and the declared derivative has no protective stop. No QuantifiedTrader reported performance is reproduced or independently claimed.

## Signal

**Gate 1: fully frozen, deterministic formulas.** Use one consecutive UTC daily BTC-USDT spot OHLCV stream; bar t opens at UTC timestamp T[t], with all O/H/L/C/V only available for decisions at effective timestamp T[t]+86400 seconds. Rolling windows include the current **completed** bar and exclude all future bars.

- SMA14[t] = mean(close[t−13..t]), defined for t ≥ 13; earlier bars have no average and never decide.
- DISP[t] = 100×(close[t] − SMA14[t])/SMA14[t], defined for t ≥ 13. No zero-guard is specified because every validated bar has strictly positive close (see causality guards), hence SMA14[t] > 0 by construction and the division is always exact — this is specified derivative behavior, verified arithmetically in scratch, not an invented patch.
- **LONG entry from FLAT only (edge, not level):** DISP[t] > 0 **and** DISP[t−1] <= 0, after the 60-bar warmup, exactly as the source `if self.disp[-1] > 0 and self.disp[-2] <= 0 and not self.position` does. A bar printing above zero while the prior bar was already above zero does **not** enter; exactly `0.0` never enters. Decisions are therefore possible only from t ≥ 14.
- **LONG exit (level):** DISP[t] < 0. Strict: exactly `0.0` never exits; the first sub-zero print after entry closes the unit, exactly as the source `elif self.disp[-1] < 0 and self.position` does.
- Entry and exit can never co-fire: entry needs DISP[t] > 0 while exit needs DISP[t] < 0 on the same bar, disjoint by arithmetic, so no tie-break pin is required. If an exit condition occurs while FLAT it is a no-op; if an entry condition occurs while LONG it is a no-op. At most one filled order per completed bar.
- **Flat-market consequences (specified, verified in scratch — never a false no-op claim):** an all-flat history prints SMA14 == close and hence DISP = 0.0: from FLAT nothing enters (0.0 is not > 0.0); while LONG the position is **held** (0.0 is not < 0.0) — a disclosed behavioral difference from guard-pathed oscillators that exit on flat prints. A lone uptick after a flat stretch prints a small positive DISP with a non-positive predecessor and enters on the edge (scratch demonstration: +0.05 tick after flat prints DISP ≈ +0.046 and enters) — this is the code-faithful edge consequence, disclosed, not patched away.
- Start FLAT; require **60 consecutive valid completed daily candles** before the first decision (covers the 15-bar definability minimum — full SMA window plus one predecessor bar for the edge — with conservative margin; the same 60-bar package as the sibling QuantifiedTrader 1d spot long-flat derivatives, applied here to a seeding-free construction). A gap, duplicate/non-monotonic timestamp, invalid OHLCV, or broken UTC daily cadence resets warmup for fresh entries and exits; if already LONG, hold without inventing gap fills and resume exit evaluation after a fresh 60-bar valid segment.
- **Cooldown:** none specified — explicitly none, not invented. Re-entry after any exit requires only FLAT state plus a fresh cross-up edge on a later bar (never a retrospective entry). No queued signals.
- **Position state:** FLAT -> PENDING_BUY -> LONG only on confirmed simulator full-fill BUY; LONG -> PENDING_SELL -> FLAT only on confirmed full-fill SELL. Pending states suppress all additional actions. The pinned simulator's MARKET path fills fully at the first supplied close; a sent action is not falsely equated to a fill in controller state. The controller must persist fill-derived state independent of the delayed positions_held view.
- **Risk and disabled behaviors (Gates 2–4):** exactly one spot LONG of **0.001 BTC** or FLAT; no short, margin, leverage, pyramiding, DCA, safety orders, simultaneous exposure, fractional/partial orders, scaling, stop loss, take profit, trailing stop, timeout, forced liquidation, maker/limit orders or end-of-sample SELL. No additional opposite-signal leg. No reinvestment/compounding. If still LONG on the final available completed bar, mark the position at the last valid close without inventing an exit trade.

## Required data and causality

**Gate 6:** Binance BTC-USDT spot 1d O/H/L/C/V with strictly increasing UTC midnight bar-open timestamps 86400 seconds apart. Each valid bar has finite positive O/H/L/C, high >= max(open,close), low <= min(open,close), high >= low, and finite nonnegative volume. The rule reads **Close only** — High/Low/Volume are never order-gating inputs (a key material distinction from range- and money-flow records). DISP needs only the current plus trailing 13 closes and one predecessor print; no future data, no unconfirmed intrabar values, no lookahead joins, no model fitting, no hindsight detection. The exact-division and never-trade-undefined treatments are specified derivative behavior. Missing close prices block signals and fills rather than defaulting to synthetic prices. One asset, one decision timeframe, no cross-asset synchronization, futures funding, external indicators, ML artifacts or order-book inputs.

## Execution assumptions and pinned Hummingbot compatibility

**Gate 5 is bounded to a real inspected pinned simulation path, not a deployment claim.** Admission policy identifies Hummingbot package label **20260920**, VERSION **dev-2.17.0**. The independently inspected source is **HCH725/hummingbot at commit 8b0e067e80ab62f10846d518dcb5a8218527ddb3**; its hummingbot/VERSION file reads dev-2.17.0 (verified this cycle via raw fetch at the pin). A package build digest was not available and this record does **not** claim that package 20260920 was byte-for-byte matched to this source commit or deployed. The engine-path claim is limited to this pinned source and previously reviewed matching research semantics.

- **Market/data:** BinanceSpotCandles constants.py maps the **1d** interval (INTERVALS bidict) and REST /api/v3/klines with symbol/interval/limit params (both verified this cycle at the pin); binance_spot_candles.py parses REST row[0] as timestamp with row[1..5] as O/H/L/C/V and WS kline keys o/h/l/c/v (verified this cycle). A strategy-specific controller must compute the declared single-leg DISP(14) features, verify contiguous completed bars and supply a single BTC-USDT spot 1d stream. The engine does not magically implement this reclaim signal.
- **Controller/action/executor:** BacktestingEngineBase.simulate_execution iterates processed rows, calls update_state(row), controller.determine_executor_actions(), and CreateExecutorAction -> simulate_executor; OrderExecutorConfig with ExecutionStrategy.MARKET and BUY/SELL side routes to OrderExecutorSimulator (row path verified this cycle at the pin). The latter fills MARKET orders immediately at the first supplied row timestamp and **close** price, sets filled_amount_quote = amount×close, cum_fees_quote = trade_cost×filled_amount_quote, and CloseType.POSITION_HOLD. Full fill at one close is an explicit simulator convention, not proof of actual executable spot fills.
- **Timestamp caveat:** source candle timestamp is the **bar OPEN label**. BacktestingEngineBase.prepare_market_data uses merge_asof on timestamp_bt (verified this cycle); backward as-of joining alone does not establish that a completed close was known at the open. The required derivative controller gates the completed bar until T[t]+86400, and the resulting research event/fill ledger is explicitly normalized to that **close-effective** timestamp while using the simulator's same-row close price. This is a disclosed adaptation away from the source next-open execution and does not claim a real post-close order can fill at the already-observed close. No intrabar or lower-timeframe path is assumed.
- **Position and ledger:** BacktestPositionHold nets equal-base BUY and SELL ("Buys and sells of the same asset net out automatically. Realized PnL comes from matched buy/sell volume"), tracking average entry price, gross matched realized PnL and accumulated fees separately (verified this cycle at the pin). The engine's positions_held conversion is delayed; pin terminated_executors_window=None and use persistent pending/fill-confirmed controller state to avoid duplicate orders or losing prior fills. After a 0.001 BTC BUY at P_b and a 0.001 BTC SELL at P_s, modeled net quote PnL = 0.001*(P_s-P_b) - 0.0001*0.001*(P_b+P_s); do not misreport gross native net_pnl_quote or pnl_timeseries as fee-inclusive equity. An open position's marked equity carries the already-paid BUY fee.
- **Costs:** pin simulator trade_cost=**0.0001 per filled side** (0.01%, researcher-selected house research input — the source models no costs and no rate is attributed to it); this is **research cost input only**, not verified Binance realized commission. No separate simulator slippage is added, which is **zero additional modeled slippage**, not evidence of zero actual spread/latency/slippage. Spot funding is inapplicable (no fabricated futures funding). Binance minimum notional, lot/tick precision, exchange commissions, partial fills, liquidity and real trading viability remain unverified; do not infer live admissibility.
- **Reused independent path review:** HCH725/alpha-strategy-research PR **#417** merged 2026-10-24 after independent HB_READY review of this same pinned Binance spot 1d / MARKET first-close / POSITION_HOLD and fee-ledger research path. That verifies an **engine primitive**, not this new indicator, trade series, profitability, package digest or candidate-specific parity. This cycle additionally re-read the pinned VERSION, Binance spot candle constants/parser, backtesting engine row/action routing, OrderExecutorSimulator and BacktestPositionHold code at the pin.

## Evidence and six-gate summary

1. **Deterministic signals:** complete SMA14/DISP(14) construction with frozen percentage formula, cross-up edge entry and strict sub-zero level exit defined above; the unpinned-helper gap is disclosed with a frozen researcher choice grounded in the page's own prose, and no TA-Lib/framework equivalence beyond that formula is claimed.
2. **Direction:** Binance BTC-USDT spot LONG/FLAT only, no short/margin.
3. **Entry/exit/risk:** reclaim-edge BUY, sub-zero SELL, all other stop/target/trailing/time legs disabled; no hidden defaults.
4. **Position:** fixed 0.001 BTC, single pending/filled state, no cooldown (explicitly none), edge re-trigger re-entry, no DCA/concurrency.
5. **Pinned engine:** concrete source commit re-read this cycle, 1d Binance candle path, controller action, MARKET full-close fill, timestamp normalization, fee and POSITION_HOLD ledger limitations; no novel unverified execution primitive used.
6. **Causality:** 60 completed-bar warmup, finite/gap guards, no future reads, decision and research-fill effective at completed bar close.

**Source-reported:** only the page identity, daily-OHLCV/no-lookahead/next-open methodology, unmodeled-costs disclaimer, percentage-difference prose, single-leg DISP(14) code rule with its strict comparators and long-only stance stated in Provenance. **Researcher-designed:** every market/fill/sizing/warmup/cost transfer plus the frozen SMA-based helper choice identified above. **Independently reproduced backtest performance:** none. **Historical survivor/HB Certified/Qlib parity:** none claimed. A stdlib-only scratch self-check this cycle confirmed ENTER/EXIT disjointness, flat-market DISP = 0.0 with no flat entries and flat-hold (not exit) while long, tick-after-flat edge entry, warmup accounting, and strict ENTER/EXIT alternation across five fuzz seeds — pure logic validation, not a backtest.

## Deduplication

Main at immutable SHA **c17e401c19983a1995e535b6d73db622d376466d** contained **338** root strategy records; README static count **338**. Working-tree filename/content search for `disparity` returns zero strategy records. GitHub PR/issue title search for `disparity` across this repository returns zero items ever. Ten open research/* PRs were checked (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend, #89 Chandelier, #92 SSL channel, #251 Swift 2YMA, #304 forven CCI, #331 AdxSmas, #350 ClucMay, #353 Heracles Keltner-Donchian) — none carries this primary source or a disparity rule.

Nearest neighbors are **not equivalent**: `forven-zscore-mean-reversion-long-flat-btcusdt-1h-2026-10-17` and `forven-zscore-mean-reclaim-long-flat-ethusdt-1h-2026-10-19` standardize the SMA distance by rolling standard deviation (with an explicit zero-variance guard problem this record never has) on a **1h** grid — this record trades the guard-free raw percentage distance on **1d** (different normalization, different guard surface, different horizon); `etf-3day-reversion-ema5-mean-reversion-long-btcusdt-1d-2026-10-08` trades an EMA5 distance with its own holding construction, not a single-SMA percentage edge/level pair; `golden-cross-sma-regime-gated-long-btcusdt-1h` and `eterna-sma-50-200-crossover` trade **dual-MA crosses**, not a price-vs-its-own-average reclaim edge; `qstick-zero-cross-trend-two-sided-btcusdt-1h` builds its oscillator from open-minus-close candle Becker structure, **two-sided**, not a close-vs-SMA percentage, long-flat only; `quantifiedtrader-random-walk-index-14-hysteresis-long-flat-btcusdt-1d-2026-10-26` and `quantifiedtrader-twiggs-money-flow-21-zero-cross-long-flat-btcusdt-1d-2026-10-25` share only the QT lane and the 1d spot long-flat derivative package — RWI trades √N-scaled High/Low displacement hysteresis levels, TMF trades a **volume-weighted** accumulation ratio, while DISP reads **Close only** with an edge-entry/level-exit pair (a volume-bar pinned at its range top prints TMF near +1 yet DISP from close-average distance alone). Different formula, different edge-vs-state construction, different risk set: not a duplicate, paraphrase, or trivial parameter variant.

## Falsification plan

After separate downstream research authorization, compare the frozen DISP(14) edge/level pair against (a) a level-hold ablation entering on any above-zero print without the cross-up edge and (b) a longer-window variant DISP(28) with the same comparators, on predeclared IS/OOS partitions; verify that the edge requirement and the window actually change entry/exit event times. Any new or unverified execution/data primitive requires representative Qlib/Hummingbot event-level validation before mass Qlib screening. Do not tune on OOS. No backtest was run by Scout.

## Crypto portability

Native crypto venue by declaration (Binance BTC-USDT spot 1d); no equity-to-crypto portability transform is asserted beyond the disclosed derivative identity. Spot semantics remove funding; minimum-notional, precision, liquidity and live viability remain unverified limitations, never assumed.

## Implementation status

Not implemented: no candidate-specific controller, feature module or replay artifact was created; only pinned generic engine files were read. The disclosed derived model must be implemented exactly if selected downstream.

## Adoption boundary

Frontmatter PASS is a **Scout-proposed six-gate research eligibility claim**, subject to independent Hermes Auditor review, not an independently approved merge. This is **not** a source-engine reproduction, actual Binance economics, profitable strategy, Qlib parity, HB Certified, survivor, deployment or Paper/Testnet/Live approval. No secrets, paid content, copied code block or private information included.

## Related Wiki records

None.

## Sources

- https://quantifiedtrader.com/backtest/strategies/disparity-index — QuantifiedTrader public strategy-library source; methodology and decision code read live 2026-10-26 (42,672 bytes HTML); page carries no publication date so source_as_of is the read date.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned Hummingbot source (VERSION, spot candle constants/parser, backtesting engine, order simulator, position-hold ledger re-read this cycle).
- https://github.com/HCH725/alpha-strategy-research/pull/417 — independent review of the same pinned spot 1d MARKET-close POSITION_HOLD research primitive.
