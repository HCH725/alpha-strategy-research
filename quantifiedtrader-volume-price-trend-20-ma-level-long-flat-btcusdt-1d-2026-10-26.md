---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: QuantifiedTrader Volume Price Trend 20 MA-level long-flat BTCUSDT 1d independent derivative
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
  - https://quantifiedtrader.com/backtest/strategies/volume-price-trend
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# QuantifiedTrader Volume Price Trend 20 MA-level — independently specified long-flat derivative

## Provenance

**First-party source:** QuantifiedTrader public strategy-library page, *Volume Price Trend*, read live 2026-10-26 (43,071 bytes HTML fetched this cycle): https://quantifiedtrader.com/backtest/strategies/volume-price-trend . No login, paywall, or private content was involved.

**Facts actually supplied by the source page:** the strategy is backtested on **daily OHLCV** price data across major US equity indices and ETFs; entry/exit signals are generated with **no lookahead bias**; **trades execute at the open of the bar following the signal**; performance metrics are computed per symbol; **transaction costs and slippage are not modeled**. The signal prose states Volume Price Trend **accumulates volume multiplied by the percentage price change**, that the strategy sees **VPT rising above its MA as volume-confirmed upward momentum**, and **exits when VPT drops below its MA**. The pinned decision code is exactly: `n = 20`; `vpt = (c.pct_change() * v).cumsum()` with `c = pd.Series(self.data.Close)`, `v = pd.Series(self.data.Volume)`; `self.vpt_ma = self.I(_sma, vpt, self.n)`; entry `self.vpt[-1] > self.vpt_ma[-1] and not self.position -> buy()`; exit `self.vpt[-1] < self.vpt_ma[-1] and self.position -> position.close()`. No short/sell-short call, no stop/target/trailing/time call, and no sizing literal ship anywhere in the rule. Close and Volume are the only price arrays read (`self.data.Close`, `self.data.Volume`); High/Low are read nowhere in the rule.

**Unpinned-helper gap (disclosed, not repaired):** the page calls a shared site helper `_sma(vpt, n)` whose body is printed on no strategy page this cycle (verified by whole-page search of the live fetch: zero `def _sma` definitions; the name occurs exactly once, at the call site; the page carries zero `crossover` and zero `ewm` tokens). This derivative therefore does **not** claim byte-equivalence with the site's helper. It freezes the textbook definition from the page's own construction — `VPTMA20[t] = mean(VPT[t−19..t])`, arithmetic mean over the trailing 20 VPT prints — as an explicit researcher choice, fully specified below. A simple moving average over completed prints is arithmetically exact from the first full window, so no framework (TA-Lib or otherwise) equivalence question arises beyond the disclosed formula. The pandas `pct_change()/cumsum()` NaN convention is likewise **not** pinned: this derivative freezes its own NaN-free recurrence (`VPT[0] = 0`, `VPT[t] = VPT[t−1] + Volume[t]×(Close[t]−Close[t−1])/Close[t−1]`), disclosed below, and never attributes pandas edge semantics to the source.

**Independent derivative, not source-native reconstruction:** the researcher explicitly chooses (1) Binance BTC-USDT **spot 1d**, LONG/FLAT rather than the source equity-index universe (no timeframe adaptation — the source is already daily); (2) the single-leg VPT(20) construction below with the code-faithful strict comparators and undefined-never-trades treatment; (3) a level **LONG entry from FLAT** (`VPT[t] > MA[t]`, exactly as coded — not an edge cross) with a strict **level LONG exit** (`VPT[t] < MA[t]`); (4) **close-effective** MARKET simulator fills instead of the source next-open execution; (5) fixed **0.001 BTC** sizing with no compounding instead of any framework-default share sizing; (6) no stop/target/trailing/time exit, no DCA and no short; (7) 60 valid completed daily bars of warmup, data-gap treatment and re-entry rules below; (8) pinned simulator `trade_cost = 0.0001` per filled side as a **researcher-selected house research input** — the source models no costs, so no fee value is attributed to it. All researcher-selected order rules and disabled behaviors belong to this independent derivative alone.

**Immutable strategy identity:** QT-volume-price-trend | derived-v1-vpt20-ma-level | BinanceSpot-BTC-USDT-1d | 2026-10-26. Any changed input, window, comparator, clock, position rule, cost or fill model creates a different derivative.

## Economic mechanism

The source hypothesizes that weighting each bar's percentage price change by its traded volume and accumulating the product separates participation-backed drift from thin-air wiggle, and that the accumulated flow riding above its own 20-bar average marks volume-confirmed momentum worth holding. This derivative holds the long only while accumulated flow stays above its average, entering on any above-average print from flat and exiting on the first below-average print. It is not a proven edge; long exposure can lose substantially and the declared derivative has no protective stop. No QuantifiedTrader reported performance is reproduced or independently claimed.

## Signal

**Gate 1: fully frozen, deterministic formulas.** Use one consecutive UTC daily BTC-USDT spot OHLCV stream; bar t opens at UTC timestamp T[t], with all O/H/L/C/V only available for decisions at effective timestamp T[t]+86400 seconds. Rolling windows include the current **completed** bar and exclude all future bars.

- Validated closes are strictly positive and finite; volumes are finite and nonnegative; zero-volume bars are valid and contribute a zero increment (verified in scratch).
- VPT[0] = 0.0 (researcher-frozen seed; the source pandas leading-NaN convention is not pinned and not claimed). For t ≥ 1: VPT[t] = VPT[t−1] + Volume[t]×(Close[t] − Close[t−1])/Close[t−1]. The only division is by the prior validated close, strictly positive by construction, so the recurrence is always exact — no zero-guard is invented beyond the validated-input rule.
- VPTMA20[t] = mean(VPT[t−19..t]), defined for t ≥ 19; earlier bars have no average and never decide. The divisor 20 is a nonzero constant; no zero-guard is specified or needed.
- **LONG entry from FLAT only (level, not edge):** VPT[t] > VPTMA20[t], after the 60-bar warmup, exactly as the source `if self.vpt[-1] > self.vpt_ma[-1] and not self.position` does. A bar printing above its average while already LONG is a no-op; exactly equal prints never enter. Decisions are therefore possible only from t ≥ 19, gated in practice to t ≥ 60.
- **LONG exit (level):** VPT[t] < VPTMA20[t]. Strict: exactly equal prints never exit; the first below-average print after entry closes the unit, exactly as the source `elif self.vpt[-1] < self.vpt_ma[-1] and self.position` does.
- Entry and exit can never co-fire: entry needs VPT[t] > MA[t] while exit needs VPT[t] < MA[t] on the same bar, disjoint by arithmetic, so no tie-break pin is required. If an exit condition occurs while FLAT it is a no-op; if an entry condition occurs while LONG it is a no-op. At most one filled order per completed bar.
- **Flat-market consequences (specified, verified in scratch — never a false no-op claim):** an all-flat history prints VPT = 0.0 and VPTMA20 = 0.0: from FLAT nothing enters (0.0 is not > 0.0); while LONG the position is **held** (0.0 is not < 0.0) — a disclosed behavioral difference from guard-pathed oscillators that exit on flat prints. A lone uptick after a flat stretch prints a small positive VPT above a near-zero average and enters on the level (scratch demonstration: +0.05 tick after flat prints VPT = +0.005 above MA ≈ +0.00025 and enters) — this is the code-faithful level consequence, disclosed, not patched away. A lone downtick prints negative VPT below its average: from FLAT no entry, while LONG an exit (scratch demonstration: −0.05 tick prints VPT = −0.005 below MA ≈ −0.00025 and exits while long).
- Start FLAT; require **60 consecutive valid completed daily candles** before the first decision (covers the 20-bar definability minimum — 19 bars for the first average plus cumsum seeding — with conservative margin; the same 60-bar package as the sibling QuantifiedTrader 1d spot long-flat derivatives). A gap, duplicate/non-monotonic timestamp, invalid OHLCV, or broken UTC daily cadence resets warmup for fresh entries and exits; if already LONG, hold without inventing gap fills and resume exit evaluation after a fresh 60-bar valid segment.
- **Cooldown:** none specified — explicitly none, not invented. Re-entry after any exit requires only FLAT state plus a later above-average print (never a retrospective entry). No queued signals.
- **Position state:** FLAT -> PENDING_BUY -> LONG only on confirmed simulator full-fill BUY; LONG -> PENDING_SELL -> FLAT only on confirmed full-fill SELL. Pending states suppress all additional actions. The pinned simulator's MARKET path fills fully at the first supplied close; a sent action is not falsely equated to a fill in controller state. The controller must persist fill-derived state independent of the delayed positions_held view.
- **Risk and disabled behaviors (Gates 2–4):** exactly one spot LONG of **0.001 BTC** or FLAT; no short, margin, leverage, pyramiding, DCA, safety orders, simultaneous exposure, fractional/partial orders, scaling, stop loss, take profit, trailing stop, timeout, forced liquidation, maker/limit orders or end-of-sample SELL. No additional opposite-signal leg. No reinvestment/compounding. If still LONG on the final available completed bar, mark the position at the last valid close without inventing an exit trade.

## Required data and causality

**Gate 6:** Binance BTC-USDT spot 1d O/H/L/C/V with strictly increasing UTC midnight bar-open timestamps 86400 seconds apart. Each valid bar has finite positive O/H/L/C, high >= max(open,close), low <= min(open,close), high >= low, and finite nonnegative volume. The rule reads **Close and Volume only** — High/Low never gate an order (they validate row integrity only; a key material distinction from range- and displacement-based records). VPT accumulates from the tape start under the frozen seed; the MA needs the current plus trailing 19 VPT prints; no future data, no unconfirmed intrabar values, no lookahead joins, no model fitting, no hindsight detection. The exact-division and never-trade-undefined treatments are specified derivative behavior. Missing close or volume prices block signals and fills rather than defaulting to synthetic prices. One asset, one decision timeframe, no cross-asset synchronization, futures funding, external indicators, ML artifacts or order-book inputs.

## Execution assumptions and pinned Hummingbot compatibility

**Gate 5 is bounded to a real inspected pinned simulation path, not a deployment claim.** Admission policy identifies Hummingbot package label **20260920**, VERSION **dev-2.17.0**. The independently inspected source is **HCH725/hummingbot at commit 8b0e067e80ab62f10846d518dcb5a8218527ddb3**; its hummingbot/VERSION file reads dev-2.17.0 (verified this cycle via raw fetch at the pin). A package build digest was not available and this record does **not** claim that package 20260920 was byte-for-byte matched to this source commit or deployed. The engine-path claim is limited to this pinned source and previously reviewed matching research semantics.

- **Market/data:** BinanceSpotCandles constants.py maps the **1d** interval (INTERVALS bidict) and REST /api/v3/klines with symbol/interval/limit params (both verified this cycle at the pin); binance_spot_candles.py parses REST row[0] as timestamp with row[1..5] as O/H/L/C/V and WS kline keys o/h/l/c/v (verified this cycle). A strategy-specific controller must compute the declared single-leg VPT(20) features, verify contiguous completed bars and supply a single BTC-USDT spot 1d stream. The engine does not magically implement this flow signal.
- **Controller/action/executor:** BacktestingEngineBase.simulate_execution iterates processed rows, calls update_state(row), controller.determine_executor_actions(), and CreateExecutorAction -> simulate_executor; OrderExecutorConfig with ExecutionStrategy.MARKET and BUY/SELL side routes to OrderExecutorSimulator (row path verified this cycle at the pin). The latter fills MARKET orders immediately at the first supplied row timestamp and **close** price, sets filled_amount_quote = amount×close, cum_fees_quote = trade_cost×filled_amount_quote, and CloseType.POSITION_HOLD. Full fill at one close is an explicit simulator convention, not proof of actual executable spot fills.
- **Timestamp caveat:** source candle timestamp is the **bar OPEN label**. BacktestingEngineBase.prepare_market_data uses merge_asof on timestamp_bt (verified this cycle); backward as-of joining alone does not establish that a completed close was known at the open. The required derivative controller gates the completed bar until T[t]+86400, and the resulting research event/fill ledger is explicitly normalized to that **close-effective** timestamp while using the simulator's same-row close price. This is a disclosed adaptation away from the source next-open execution and does not claim a real post-close order can fill at the already-observed close. No intrabar or lower-timeframe path is assumed.
- **Position and ledger:** BacktestPositionHold nets equal-base BUY and SELL ("Buys and sells of the same asset net out automatically. Realized PnL comes from matched buy/sell volume"), tracking average entry price, gross matched realized PnL and accumulated fees separately (verified this cycle at the pin). The engine's positions_held conversion is delayed; pin terminated_executors_window=None and use persistent pending/fill-confirmed controller state to avoid duplicate orders or losing prior fills. After a 0.001 BTC BUY at P_b and a 0.001 BTC SELL at P_s, modeled net quote PnL = 0.001*(P_s-P_b) - 0.0001*0.001*(P_b+P_s); do not misreport gross native net_pnl_quote or pnl_timeseries as fee-inclusive equity. An open position's marked equity carries the already-paid BUY fee.
- **Costs:** pin simulator trade_cost=**0.0001 per filled side** (0.01%, researcher-selected house research input — the source models no costs and no rate is attributed to it); this is **research cost input only**, not verified Binance realized commission. No separate simulator slippage is added, which is **zero additional modeled slippage**, not evidence of zero actual spread/latency/slippage. Spot funding is inapplicable (no fabricated futures funding). Binance minimum notional, lot/tick precision, exchange commissions, partial fills, liquidity and real trading viability remain unverified; do not infer live admissibility.
- **Reused independent path review:** HCH725/alpha-strategy-research PR **#417** merged 2026-10-24 after independent HB_READY review of this same pinned Binance spot 1d / MARKET first-close / POSITION_HOLD and fee-ledger research path. That verifies an **engine primitive**, not this new indicator, trade series, profitability, package digest or candidate-specific parity. This cycle additionally re-read the pinned VERSION, Binance spot candle constants/parser, backtesting engine row/action routing, OrderExecutorSimulator and BacktestPositionHold code at the pin.

## Evidence and six-gate summary

1. **Deterministic signals:** complete VPT recurrence with frozen zero seed, SMA20 construction, level entry and strict below-average level exit defined above; the unpinned-helper gap is disclosed with frozen researcher choices grounded in the page's own construction, and no TA-Lib/framework equivalence beyond those formulas is claimed.
2. **Direction:** Binance BTC-USDT spot LONG/FLAT only, no short/margin.
3. **Entry/exit/risk:** above-average BUY, below-average SELL, all other stop/target/trailing/time legs disabled; no hidden defaults.
4. **Position:** fixed 0.001 BTC, single pending/filled state, no cooldown (explicitly none), level re-trigger re-entry, no DCA/concurrency.
5. **Pinned engine:** concrete source commit re-read this cycle, 1d Binance candle path, controller action, MARKET full-close fill, timestamp normalization, fee and POSITION_HOLD ledger limitations; no novel unverified execution primitive used.
6. **Causality:** 60 completed-bar warmup, finite/gap guards, no future reads, decision and research-fill effective at completed bar close.

**Source-reported:** only the page identity, daily-OHLCV/no-lookahead/next-open methodology, unmodeled-costs disclaimer, volume-times-pct-change accumulation prose, single-leg VPT(20) code rule with its strict comparators and long-only stance stated in Provenance. **Researcher-designed:** every market/fill/sizing/warmup/cost transfer plus the frozen SMA-based helper and NaN-free seed choices identified above. **Independently reproduced backtest performance:** none. **Historical survivor/HB Certified/Qlib parity:** none claimed. A stdlib-only scratch self-check this cycle confirmed ENTER/EXIT disjointness, flat-market VPT = 0.0 with no flat entries and flat-hold (not exit) while long, tick-after-flat level entry, downtick level exit while long, zero-volume increment behavior, warmup accounting, and strict ENTER/EXIT alternation across five fuzz seeds — pure logic validation, not a backtest.

## Deduplication

Main at immutable SHA **c2884de3f0c5200716bc5e7d20d75fe49645e813** contained **340** root strategy records; README static count **340**. Working-tree filename search for `vpt` and `volume-price` returns zero strategy records; content search for `VolumePriceTrend` and `volume-price-trend` returns zero strategy records. GitHub PR/issue searches for `volume-price-trend` and `VolumePriceTrend` across this repository return zero items ever (open and closed). Ten open research/* PRs were checked (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend, #89 Chandelier, #92 SSL channel, #251 Swift 2YMA, #304 forven CCI, #331 AdxSmas, #350 ClucMay, #353 Heracles Keltner-Donchian) — none carries this primary source or a VPT rule.

Nearest neighbors are **not equivalent**: `forven-obv-ema-cross-sma-gated-long-flat-btcusdt-1h-2026-10-19` cumulates **sign**-weighted volume (Granville OBV: ±1 per bar regardless of move size) against an **EMA20** with an extra SMA20 price gate, edge-triggered both legs on a **1h** grid — this record cumulates **percentage-magnitude**-weighted volume against its own **SMA20** with no price gate, level-triggered both legs on **1d** (a steady drip of small up-volume days and a single large spike move this record's line differently by construction, and the OBV price gate suppresses entries this record takes); `forven-adl-ema-cross-trend-gated`, `forven-chaikin-mf-threshold-cross`, `forven-mfi-threshold-cross` and `klinger-volume-oscillator-trigger-flip` trade money-flow ratios, threshold bands or dual-oscillator triggers, never a cumulative pct-change flow against its own simple average; `quantifiedtrader-twiggs-money-flow-21-zero-cross-long-flat-btcusdt-1d-2026-10-25` trades a bounded volume-weighted accumulation **ratio** zero-cross while this record trades an unbounded cumulative flow versus its own average level; `quantifiedtrader-disparity-index-14-zero-cross-long-flat-btcusdt-1d-2026-10-26` reads **Close only** with an edge-entry/level-exit percentage pair and no volume input at all; `quantifiedtrader-random-walk-index-14-hysteresis-long-flat-btcusdt-1d-2026-10-26` trades √N-scaled High/Low displacement hysteresis levels with no volume input. Different formula, different weighting, different trigger construction, different risk set: not a duplicate, paraphrase, or trivial parameter variant.

## Falsification plan

After separate downstream research authorization, compare the frozen VPT(20) level pair against (a) an edge-only ablation entering solely on the cross-up bar (VPT[t] > MA[t] with VPT[t−1] <= MA[t−1]) and (b) a longer-window variant VPTMA(40) with the same comparators, on predeclared IS/OOS partitions; verify that the level requirement and the window actually change entry/exit event times. Any new or unverified execution/data primitive requires representative Qlib/Hummingbot event-level validation before mass Qlib screening. Do not tune on OOS. No backtest was run by Scout.

## Crypto portability

Native crypto venue by declaration (Binance BTC-USDT spot 1d); no equity-to-crypto portability transform is asserted beyond the disclosed derivative identity. Spot semantics remove funding; minimum-notional, precision, liquidity and live viability remain unverified limitations, never assumed.

## Implementation status

Not implemented: no candidate-specific controller, feature module or replay artifact was created; only pinned generic engine files were read. The disclosed derived model must be implemented exactly if selected downstream.

## Adoption boundary

Frontmatter PASS is a **Scout-proposed six-gate research eligibility claim**, subject to independent Hermes Auditor review, not an independently approved merge. This is **not** a source-engine reproduction, actual Binance economics, profitable strategy, Qlib parity, HB Certified, survivor, deployment or Paper/Testnet/Live approval. No secrets, paid content, copied code block or private information included.

## Related Wiki records

None.

## Sources

- https://quantifiedtrader.com/backtest/strategies/volume-price-trend — QuantifiedTrader public strategy-library source; methodology and decision code read live 2026-10-26 (43,071 bytes HTML); page carries no publication date so source_as_of is the read date.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned Hummingbot source (VERSION, spot candle constants/parser, backtesting engine, order simulator, position-hold ledger re-read this cycle).
- https://github.com/HCH725/alpha-strategy-research/pull/417 — independent review of the same pinned spot 1d MARKET-close POSITION_HOLD research primitive.
