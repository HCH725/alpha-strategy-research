---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: QuantifiedTrader Fractal Breakout 2-2 fixed-lag confirmed-level long-flat BTCUSDT 1d independent derivative
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
  - https://quantifiedtrader.com/backtest/strategies/fractal-breakout
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# QuantifiedTrader Fractal Breakout 2-2 fixed-lag confirmed-level long-flat derivative

## Provenance

**First-party source:** QuantifiedTrader public strategy-library page, *Fractal Breakout*, fetched live 2026-10-26 (43,394 bytes HTML; the Methodology code block is character-identical to the pre-existing scratch mirror fetched earlier): https://quantifiedtrader.com/backtest/strategies/fractal-breakout . No login, paywall, or private content was involved. The page carries no publication date, so `source_as_of` is the read date.

**Facts actually supplied by the source page:** the strategy is backtested on **daily OHLCV** price data across major US equity indices and ETFs; entry/exit signals are generated with **no lookahead bias**; **trades execute at the open of the bar following the signal**; performance metrics are computed per symbol; **transaction costs and slippage are not modeled**. The signal prose states the rule uses Bill Williams' fractal pattern — a bar with two lower highs on each side — **enters long when price closes above a confirmed fractal high**, and **exits when price falls to a fractal low**. The pinned decision code is printed in full on the page (no hidden helper — every operator is visible):

`left = 2; right = 2`; `n = left + right + 1` (= 5); `fh` = 5-bar centered rolling maximum test `x.iloc[2] if x.iloc[2]==x.max() else NaN` on High; `fl` = the mirror minimum test on Low; decision `idx = left + right + 2` (= 6); `fh_val = fh[-idx]`, `fl_val = fl[-idx]`; entry `not NaN(fh_val) and Close[-1] >= fh_val and not position -> buy()`; exit `not NaN(fl_val) and Close[-1] <= fl_val and position -> position.close()`. No short/sell-short call, no stop/target/trailing/time call, and no sizing literal ship anywhere in the rule. High/Low/Close are read; Volume is read nowhere in the rule.

**Independent derivative, not source-native reconstruction:** the researcher explicitly chooses (1) Binance BTC-USDT **spot 1d**, LONG/FLAT rather than the source equity-index universe (no timeframe adaptation — the source is already daily); (2) the literal fixed-lag-6 construction below with the code-faithful non-strict comparators and NaN-never-trades treatment — the reference slot is always exactly five bars back, never a most-recent-fractal search; (3) a **close-effective** MARKET simulator fill instead of the source next-open execution; (4) fixed **0.001 BTC** sizing with no compounding instead of any framework-default share sizing; (5) no stop/target/trailing/time exit, no DCA and no short; (6) 60 valid completed daily bars of warmup, data-gap treatment and re-entry rules below; (7) standing **EXIT-before-ENTRY** priority on co-fire bars; (8) pinned simulator `trade_cost = 0.0001` per filled side as a **researcher-selected house research input** — the source models no costs, so no fee value is attributed to it. All researcher-selected order rules and disabled behaviors belong to this independent derivative alone.

**Immutable strategy identity:** QT-fractal-breakout-22 | derived-v1-fixed-lag6-level-pair | BinanceSpot-BTC-USDT-1d | 2026-10-26. Any changed input, window, lag, comparator, clock, position rule, cost or fill model creates a different derivative.

## Economic mechanism

### Source-reported

A confirmed 5-bar fractal high (a bar with two lower highs on each side) is presented as resistance whose upside close-break marks expansion worth riding; a fall to a confirmed fractal low ends the ride. Breakout persistence, not reversal fade, is the stated thesis. These are hypotheses, not demonstrated profits.

### Research interpretation

This derivative holds a long only between a fixed-lag confirmed-fractal-high upside print and the first confirmed-fractal-low touch. It buys persistence (close at/above the old confirmed extreme), never fades it, and carries no protective stop — a continued bleed that never prints a sub-fractal-low close stays exposed. Because ties satisfy the `==` admission test, flat markets admit both references and churn (disclosed below). No QuantifiedTrader reported performance is reproduced or independently claimed.

## Signal

**Gate 1: fully frozen, deterministic formulas.** Use one consecutive UTC daily BTC-USDT spot OHLCV stream; bar t opens at UTC timestamp T[t], with all O/H/L/C/V only available for decisions at effective timestamp T[t]+86400 seconds. All windows below reference **completed** bars only.

- `FH[t]` = `H[t-5]` if `H[t-5] == max(H[t-7], H[t-6], H[t-5], H[t-4], H[t-3])`, else undefined. `FL[t]` = `L[t-5]` if `L[t-5] == min(L[t-7], L[t-6], L[t-5], L[t-4], L[t-3])`, else undefined. This is the literal `rolling(5, center=True)` admission test read at fixed lag `idx = 6` (the value centered five bars back, whose two right-side confirmation bars `t-4, t-3` are complete). Exact float `==`, code-faithful; no tolerance band is invented. Defined only for t >= 7; earlier bars never decide.
- **LONG entry from FLAT only:** `FH[t]` defined **and** `C[t] >= FH[t]`. Non-strict and code-faithful: a close exactly equal to the fractal high enters (disclosed). A fractal sitting at any other lag (e.g. a fresh extreme at `t-4`) does **not** fire — fixed slot, never a most-recent search (scratch demonstration: neighbor-slot extreme with confirming close prints no entry).
- **LONG exit (level):** `FL[t]` defined **and** `C[t] <= FL[t]`. Non-strict and code-faithful: a close exactly equal to the fractal low exits (disclosed).
- **Co-fire rule:** entry needs `C[t] >= FH[t]` while exit needs `C[t] <= FL[t]`; both can hold at once (flat markets admit both references through `==` ties). Standing order: evaluate **EXIT first while LONG, ENTRY only from FLAT** — exactly the source `if/elif` posture under position gating, binding here by declaration. While LONG a co-fire bar SELLs; while FLAT the same prints BUY only if the entry leg holds.
- **Flat-market consequence (specified, verified in scratch):** an all-flat stretch admits `FH == FL == C` every bar, so from FLAT each bar enters and while LONG each bar exits — code-faithful alternating BUY/SELL churn with a per-side research cost each way, disclosed, not patched away.
- Start FLAT; require **60 consecutive valid completed daily candles** before the first decision (covers the t >= 7 definability minimum with wide margin; the same 60-bar package as the sibling QuantifiedTrader 1d spot long-flat derivatives). A gap, duplicate/non-monotonic timestamp, invalid OHLC, or broken UTC daily cadence resets warmup for fresh entries and exits; if already LONG, hold without inventing gap fills and resume exit evaluation after a fresh 60-bar valid segment.
- **Cooldown:** none specified — explicitly none, not invented. Re-entry after any exit requires only FLAT state plus a fresh defined-reference entry print on a later bar (never a retrospective entry). No queued signals. At most one action per completed bar.
- **Position state:** FLAT -> PENDING_BUY -> LONG only on confirmed simulator full-fill BUY; LONG -> PENDING_SELL -> FLAT only on confirmed full-fill SELL. Pending states suppress all additional actions. A sent action is not falsely equated to a fill in controller state. The controller must persist fill-derived state independent of the delayed positions_held view.
- **Risk and disabled behaviors (Gates 2–4):** exactly one spot LONG of **0.001 BTC** or FLAT; no short, margin, leverage, pyramiding, DCA, safety orders, simultaneous exposure, fractional/partial orders, scaling, stop loss, take profit, trailing stop, timeout, forced liquidation, maker/limit orders or end-of-sample SELL. No additional opposite-signal leg. No reinvestment/compounding. If still LONG on the final available completed bar, mark the position at the last valid close without inventing an exit trade.

## Required data and causality

**Gate 6:** Binance BTC-USDT spot 1d O/H/L/C/V with strictly increasing UTC midnight bar-open timestamps 86400 seconds apart. Each valid bar has finite positive O/H/L/C, high >= max(open,close), low <= min(open,close), high >= low, and finite nonnegative volume. The rule reads **High/Low/Close only** — Volume is never order-gating (a key material distinction from volume-weighted records). References need only bars `t-7..t`, all complete at decision time; no future data, no unconfirmed intrabar values, no lookahead joins, no model fitting, no hindsight detection, no repainting (the fixed-lag slot reads only confirmation-complete windows). Missing prices block signals and fills rather than defaulting to synthetic prices. One asset, one decision timeframe, no cross-asset synchronization, futures funding, external indicators, ML artifacts or order-book inputs.

## Execution assumptions and pinned Hummingbot compatibility

**Gate 5 is bounded to a real inspected pinned simulation path, not a deployment claim.** Admission policy identifies Hummingbot package label **20260920**, VERSION **dev-2.17.0**. The independently inspected source is **HCH725/hummingbot at commit 8b0e067e80ab62f10846d518dcb5a8218527ddb3**; its hummingbot/VERSION file reads dev-2.17.0 (verified this cycle from the local pin). A package build digest was not available and this record does **not** claim that package 20260920 was byte-for-byte matched to this source commit or deployed. The engine-path claim is limited to this pinned source and previously reviewed matching research semantics.

- **Market/data:** BinanceSpotCandles constants.py maps the **1d** interval (INTERVALS bidict, verified this cycle at the pin); the candle parser reads REST row[0] as the bar timestamp with row[1..5] as O/H/L/C/V (verified this cycle at the pin). A strategy-specific controller must compute the declared single-leg fixed-lag fractal references, verify contiguous completed bars and supply a single BTC-USDT spot 1d stream. The engine does not magically implement this breakout signal.
- **Controller/action/executor:** BacktestingEngineBase.simulate_execution iterates processed rows, calls controller.determine_executor_actions(), and routes each CreateExecutorAction over the current-row forward slice to the executor simulator (row path verified this cycle at the pin). OrderExecutorConfig with ExecutionStrategy.MARKET and BUY/SELL side routes to OrderExecutorSimulator, which fills MARKET orders at the first supplied row timestamp and **close** price, sets filled_amount_quote = amount×close and cum_fees_quote = trade_cost×filled_amount_quote, and reports CloseType.POSITION_HOLD (all verified this cycle at the pin). Full fill at one close is an explicit simulator convention, not proof of actual executable spot fills.
- **Timestamp caveat:** source candle timestamp is the **bar OPEN label**. The engine joins features with backward as-of on timestamp_bt (verified this cycle); that join alone does not establish that a completed close was known at the open. The required derivative controller gates the completed bar until T[t]+86400, and the resulting research event/fill ledger is explicitly normalized to that **close-effective** timestamp while using the simulator's same-row close price. This is a disclosed adaptation away from the source next-open execution and does not claim a real post-close order can fill at the already-observed close. No intrabar or lower-timeframe path is assumed.
- **Position and ledger:** BacktestPositionHold nets equal-base BUY and SELL ("Buys and sells of the same asset net out automatically. Realized PnL comes from matched buy/sell volume"), tracking average entry price, gross matched realized PnL and accumulated fees separately (verified this cycle at the pin). The engine's positions_held conversion is delayed; pin terminated_executors_window=None (pinned default is only 3600 seconds) and use persistent pending/fill-confirmed controller state to avoid duplicate orders or losing prior fills. After a 0.001 BTC BUY at P_b and a 0.001 BTC SELL at P_s, modeled net quote PnL = 0.001*(P_s-P_b) - 0.0001*0.001*(P_b+P_s); do not misreport gross native net_pnl_quote or pnl_timeseries as fee-inclusive equity. An open position's marked equity carries the already-paid BUY fee.
- **Costs:** pin simulator trade_cost=**0.0001 per filled side** (0.01%, researcher-selected house research input — the source models no costs and no rate is attributed to it); this is **research cost input only**, not verified Binance realized commission. No separate simulator slippage is added, which is **zero additional modeled slippage**, not evidence of zero actual spread/latency/slippage. Spot funding is inapplicable (no fabricated futures funding). Binance minimum notional, lot/tick precision, exchange commissions, partial fills, liquidity and real trading viability remain unverified; do not infer live admissibility.
- **Reused independent path review:** HCH725/alpha-strategy-research PR **#417** merged 2026-10-24 after independent HB_READY review of this same pinned Binance spot 1d / MARKET first-close / POSITION_HOLD and fee-ledger research path. That verifies an **engine primitive**, not this new indicator, trade series, profitability, package digest or candidate-specific parity. This cycle additionally re-read the pinned VERSION, Binance spot candle constants/parser, backtesting engine row/action routing, OrderExecutorSimulator and BacktestPositionHold code at the pin.

## Evidence

### Source-reported

Only the page identity, daily-OHLCV/no-lookahead/next-open methodology, unmodeled-costs disclaimer, Bill Williams fractal prose, and the complete single-leg 2-2 decision code with its fixed `idx = 6` slot, non-strict comparators, NaN guards and long-only stance stated in Provenance. **Researcher-designed:** every market/fill/sizing/warmup/cost transfer plus the EXIT-first co-fire priority and gap/hold treatments identified above. **Independently reproduced backtest performance:** none. **Historical survivor/HB Certified/Qlib parity:** none claimed.

### Independently reproduced

**Rule-logic self-check (stdlib only, not a backtest):** the frozen fixed-lag references plus the FLAT/LONG state machine were executed over hand-constructed bars and 5×400-bar fuzz streams: slot-exact fractal entry fires; equality closes enter/exit; neighbor-slot (most-recent) extremes do not fire; NaN slots never trade; flat markets churn BUY/SELL under EXIT-first priority as disclosed; pre-t-7 bars never decide; BUY/SELL strictly alternate across all fuzz seeds. **Engine-code inspection only, not a strategy backtest:** pinned Hummingbot commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3` was read line-by-line for the Binance spot `1d` candle parser (open-timestamp rows), the row-wise engine action loop with current-row forward slices, MARKET-first-row-close fill, quote-notional fee accumulator, POSITION_HOLD ledger, `hummingbot/VERSION` and 3600-second vs `None` terminated-executor visibility. The candidate's trade events, QuantifiedTrader outputs, Qlib/Hummingbot parity, and net returns have **not** been independently reproduced. No backtest was executed.

### Negative evidence

- No sizing, warmup, cost, or framework-default order setting is available from the retrieved source page; **source-native/lossless equivalence is unverified**. The independent derivative is evaluated against its own frozen rules only.
- The fixed five-bar-back reference slot is literal code behavior, not a most-recent-fractal search; a reader expecting freshest-confirmation semantics must treat this as a different event stream by construction.
- No verified next-open fill, live close fill, partial fill, market impact, exchange fee schedule, futures funding or venue order-size permission. None is silently imputed.

## Deduplication

Main at immutable SHA **012f29ea6d9968b32ba7792f28beb3c54e782d33** contained **348** root strategy records; README static count **348**. Working-tree filename/content search for `fractal-breakout` and `quantifiedtrader.com/backtest/strategies/fractal` returns zero strategy records; GitHub title search for `fractal-breakout` returns zero items ever, and a title sweep over recently closed PRs returned no fractal-titled candidate. Ten open research/* PRs were checked (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend, #89 Chandelier, #92 SSL channel, #251 Swift 2YMA, #304 forven CCI, #331 AdxSmas, #350 ClucMay, #353 Heracles Keltner-Donchian) — none carries this primary source or a fractal rule.

Nearest neighbors are **not equivalent**: `williams-fractal-ema-band-fixed-rr-two-sided-btcusdt-1d-2026-10-10` fades EMA-band-contained pivots with a resting EMA-slow stop and 1.5R limit OCO book, two-sided — this record has no EMA, no band, no stop/target at all, and a level-touch exit, long-flat only; `support-resistance-fractal-trailing-breakout-two-sided-btcusdt-4h-2026-10-11` averages 21 admitted extremes into an r-offset dual trailing band behind a trend latch with a reversal book on **4h** — this record averages nothing, latches nothing, and trades one fixed-lag raw confirmed level on **1d**; `pfe-polarized-fractal-efficiency-hysteresis-two-sided` trades an efficiency ratio, not pivot geometry; `wick-reversal-hammer-shooting-star-long-flat` trades single-candle wicks, not 5-bar confirmed fractals. Different source, different signal construction, different risk book, different horizon/direction: not a duplicate, paraphrase, or trivial parameter variant.

## Falsification plan

After separate downstream research authorization, compare the frozen 2-2 fixed-lag rule against (a) a wider-window 3-3 variant with the same lag construction and comparators, and (b) a one-extra-bar confirmation ablation that requires the entry print to persist on the next completed bar, on predeclared IS/OOS partitions; verify that the window and the timing actually change entry/exit event times. Any new or unverified execution/data primitive requires representative Qlib/Hummingbot event-level validation before mass Qlib screening. Do not tune on OOS. No backtest was run by Scout.

## Crypto portability

Native crypto venue by declaration (Binance BTC-USDT spot 1d); no equity-to-crypto portability transform is asserted beyond the disclosed derivative identity. Spot semantics remove funding; minimum-notional, precision, liquidity and live viability remain unverified limitations, never assumed.

## Limitations

- A breakdown that never prints a sub-fractal-low close leaves the long exposed with no stop, target, or time exit; the flat-market churn disclosed above pays a per-side research cost on every alternation.
- The source next-open execution is not reproduced; entries/exits happen at the simulated trio-completion close, which changes events versus the site's backtest clock.
- Exact source framework revision, original sizing/cost settings and profitability are unknown. The simulated completed-close fill is a **backtest convention**, not a live execution guarantee.
- The modeled 0.01%-per-side research cost, zero additional modeled slippage, fixed base size and absence of futures funding do not prove actual Binance trade economics. A long position can remain exposed during data outages. No Qlib parity, survivor status or trading approval follows from HB_READY.

## Implementation status

Not implemented: no candidate-specific controller, feature module or replay artifact was created; only pinned generic engine files were read. The disclosed derived model must be implemented exactly if selected downstream.

## Adoption boundary

Frontmatter PASS is a **Scout-proposed six-gate research eligibility claim**, subject to independent Hermes Auditor review, not an independently approved merge. This is **not** a source-engine reproduction, actual Binance economics, profitable strategy, Qlib parity, HB Certified, survivor, deployment or Paper/Testnet/Live approval. No secrets, paid content, copied code block or private information included.

## Related Wiki records

None.

## Sources

- https://quantifiedtrader.com/backtest/strategies/fractal-breakout — QuantifiedTrader public strategy-library source; methodology and decision code read live 2026-10-26 (43,394 bytes HTML); page carries no publication date so source_as_of is the read date.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned Hummingbot source (VERSION, spot candle constants/parser, backtesting engine, order simulator, position-hold ledger re-read this cycle).
- https://github.com/HCH725/alpha-strategy-research/pull/417 — independent review of the same pinned spot 1d MARKET-close POSITION_HOLD research primitive.
