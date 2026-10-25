---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: QuantifiedTrader Intraday Intensity 21 zero-cross long-flat BTCUSDT 1d independent derivative
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
  - https://quantifiedtrader.com/backtest/strategies/intraday-intensity
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# QuantifiedTrader Intraday Intensity 21 zero-cross — independently specified long-flat derivative

## Provenance

**First-party source:** QuantifiedTrader public strategy-library page, *Intraday Intensity*, read live 2026-10-26 (43,162 bytes HTML fetched this cycle): https://quantifiedtrader.com/backtest/strategies/intraday-intensity . No login, paywall, or private content was involved.

**Facts actually supplied by the source page:** the strategy is backtested on **daily OHLCV** price data across major US equity indices and ETFs; entry/exit signals are generated with **no lookahead bias**; **trades execute at the open of the bar following the signal**; performance metrics are computed per symbol; **transaction costs and slippage are not modeled**. The signal prose states the Intraday Intensity Index **measures where the close falls within the day's range, weighted by volume**, that **positive values indicate buying pressure**, and that the strategy **enters long when the smoothed III crosses above zero**. The pinned decision code is exactly: `n = 21`; `h,l,c,v = pd.Series(self.data.High), pd.Series(self.data.Low), pd.Series(self.data.Close), pd.Series(self.data.Volume)`; `iii = (2*c - h - l) / (h-l).replace(0,1e-10) * v`; `self.iii = self.I(lambda: iii.rolling(self.n).sum() / v.rolling(self.n).sum().replace(0,1e-10), name="III")`; entry `self.iii[-1] > 0 and self.iii[-2] <= 0 and not self.position -> buy()`; exit `self.iii[-1] < 0 and self.position -> position.close()`. One `buy()` call, zero short/sell-short calls, one `position.close()` call, no stop/target/trailing/time call, and no sizing literal ship anywhere in the rule. High, Low, Close and Volume are all read (`self.data.High/Low/Close/Volume`); Open is read nowhere in the rule.

**No unpinned-helper gap:** unlike sibling QuantifiedTrader pages that call shared site helpers (`_sma`, `_mfi`, `_projection_oscillator`), this page's decision code is fully self-contained (verified by whole-page search of the live fetch: zero `def _` definitions, exactly two `def` tokens — `init` and `next` — and zero `crossover` / zero `ewm` tokens anywhere on the page). Every operator, window, guard constant (`1e-10`, twice) and comparator is printed inline, so this derivative claims no frozen helper beyond what the page itself pins; only the pandas `rolling().sum()` leading-window NaN convention is researcher-frozen below (NaN = undefined = never trades), disclosed, and never attributed to the source.

**Independent derivative, not source-native reconstruction:** the researcher explicitly chooses (1) Binance BTC-USDT **spot 1d**, LONG/FLAT rather than the source equity-index universe (no timeframe adaptation — the source is already daily); (2) the single-leg III(21) construction below with the code-faithful edge-entry/level-exit zero pair and undefined-never-trades treatment; (3) an edge **LONG entry from FLAT** (`III[t] > 0` with `III[t−1] <= 0`, exactly as coded — a cross-up, not a level hold) with a strict **level LONG exit** (`III[t] < 0`); (4) **close-effective** MARKET simulator fills instead of the source next-open execution; (5) fixed **0.001 BTC** sizing with no compounding instead of any framework-default share sizing; (6) no stop/target/trailing/time exit, no DCA and no short; (7) 63 valid completed daily bars of warmup, data-gap treatment and re-entry rules below; (8) pinned simulator `trade_cost = 0.0001` per filled side as a **researcher-selected house research input** — the source models no costs, so no fee value is attributed to it. All researcher-selected order rules and disabled behaviors belong to this independent derivative alone.

**Immutable strategy identity:** QT-intraday-intensity | derived-v1-iii21-zero-cross | BinanceSpot-BTC-USDT-1d | 2026-10-26. Any changed input, window, comparator, clock, position rule, cost or fill model creates a different derivative.

## Economic mechanism

The source hypothesizes that locating each bar's close inside its own daily range and weighting that location by traded volume separates conviction-backed pressure (closes pinned toward the high on heavy volume) from indifferent chop (mid-range closes), and that the 21-bar volume-weighted average of that location crossing above zero marks buying pressure worth holding. This derivative holds the long only after such a cross-up and exits on the first sub-zero print. It is not a proven edge; long exposure can lose substantially and the declared derivative has no protective stop. No QuantifiedTrader reported performance is reproduced or independently claimed.

## Signal

**Gate 1: fully frozen, deterministic formulas.** Use one consecutive UTC daily BTC-USDT spot OHLCV stream; bar t opens at UTC timestamp T[t], with all O/H/L/C/V only available for decisions at effective timestamp T[t]+86400 seconds. Rolling windows include the current **completed** bar and exclude all future bars.

- Validated bars have finite positive O/H/L/C with high >= max(open,close), low <= min(open,close), high >= low; volumes are finite and nonnegative. A zero-range bar (high == low) can therefore only occur with open == high == low == close, and its location term is exactly `0.0` (see guard rule).
- Location-volume increment: LV[t] = ((2×Close[t] − High[t] − Low[t]) / R[t]) × Volume[t], where R[t] = High[t] − Low[t] except exactly `0`, which uses `1e-10` (code-faithful zero-guard, never invented). LV lies in [−Volume[t], +Volume[t]]; a close pinned at the high prints +Volume[t], at the low −Volume[t], mid-range 0.0.
- III[t] = sum(LV[i]) / sum(Volume[i]) for i in t−20..t (21 trailing bars); a zero volume-window divisor uses `1e-10` (code-faithful, never invented). III[t] is defined only for t ≥ 20; earlier bars have no print and never decide. III is bounded in [−1, +1] whenever the volume window is positive.
- **LONG entry from FLAT only (edge cross-up):** III[t−1] <= 0 AND III[t] > 0, after the 63-bar warmup, exactly as the source `if self.iii[-1] > 0 and self.iii[-2] <= 0 and not self.position` does. Strict on both sides: exactly `0.0` on the current bar never enters. Decisions are therefore possible only from t ≥ 21, gated in practice to t ≥ 63.
- **LONG exit (level):** III[t] < 0. Strict: exactly `0.0` never exits; the first sub-zero print after entry closes the unit, exactly as the source `elif self.iii[-1] < 0 and self.position` does.
- Entry and exit can never co-fire: entry needs III[t] > 0 while exit needs III[t] < 0 on the same bar, disjoint by arithmetic, so no tie-break pin is required. If an exit condition occurs while FLAT it is a no-op; if an entry condition occurs while LONG it is a no-op. At most one filled order per completed bar.
- **Flat-market consequences (specified, verified in scratch — never a false no-op claim):** an all-flat history prints LV = 0.0 and III = 0.0: from FLAT nothing enters (0.0 is not > 0.0); while LONG the position is **held** (0.0 is not < 0.0). A history positive from the first print never crosses up from a defined non-positive predecessor, so it **never enters retrospectively** — the edge requirement is a disclosed behavioral consequence, not patched away (scratch demonstration: pin-at-high from bar 0 yields zero entries; low-then-high regime flip yields exactly one BUY once the 21-window flushes the old regime). A lone mid-range-close day after pressure prints near-zero location volume and cannot by itself force a cross. A gap-up day whose close sits mid-range contributes ~0.0 location volume — pure intrabar-location behavior with no interbar displacement term (scratch demonstration: gap series prints III == 0.0 throughout).
- Zero-volume bars contribute LV = 0.0 and shrink the volume window; a fully zero 21-bar volume window prints III = 0.0/1e-10 = 0.0 (defined, hold/no-enter — never a crash, never a synthetic fill).
- Start FLAT; require **63 consecutive valid completed daily candles** before the first decision (21-bar window definability at t ≥ 20 plus the one-bar cross lookback, with 3×-window conservative margin — the same 3× package convention as the sibling QuantifiedTrader VPT(20)/60-bar 1d spot long-flat derivative). A gap, duplicate/non-monotonic timestamp, invalid OHLCV, or broken UTC daily cadence resets warmup for fresh entries and exits; if already LONG, hold without inventing gap fills and resume exit evaluation after a fresh 63-bar valid segment.
- **Cooldown:** none specified — explicitly none, not invented. Re-entry after any exit requires a **new** cross-up (prev <= 0, curr > 0), never a level hold or retrospective entry. No queued signals.
- **Position state:** FLAT -> PENDING_BUY -> LONG only on confirmed simulator full-fill BUY; LONG -> PENDING_SELL -> FLAT only on confirmed full-fill SELL. Pending states suppress all additional actions. The pinned simulator's MARKET path fills fully at the first supplied close; a sent action is not falsely equated to a fill in controller state. The controller must persist fill-derived state independent of the delayed positions_held view.
- **Risk and disabled behaviors (Gates 2–4):** exactly one spot LONG of **0.001 BTC** or FLAT; no short, margin, leverage, pyramiding, DCA, safety orders, simultaneous exposure, fractional/partial orders, scaling, stop loss, take profit, trailing stop, timeout, forced liquidation, maker/limit orders or end-of-sample SELL. No additional opposite-signal leg. No reinvestment/compounding. If still LONG on the final available completed bar, mark the position at the last valid close without inventing an exit trade.

## Required data and causality

**Gate 6:** Binance BTC-USDT spot 1d O/H/L/C/V with strictly increasing UTC midnight bar-open timestamps 86400 seconds apart. Each valid bar has finite positive O/H/L/C, high >= max(open,close), low <= min(open,close), high >= low, and finite nonnegative volume. The rule reads **High, Low, Close and Volume** — the intrabar range and close location gate every order (a key material distinction from Close-and-Volume-only records such as the sibling VPT derivative, and from Close-only records such as Disparity). III accumulates from the tape start under the frozen undefined-until-t-20 treatment; the cross needs the current plus trailing 21 prints; no future data, no unconfirmed intrabar values, no lookahead joins, no model fitting, no hindsight detection. The exact-guard and never-trade-undefined treatments are specified derivative behavior. Missing prices or volumes block signals and fills rather than defaulting to synthetic prices. One asset, one decision timeframe, no cross-asset synchronization, futures funding, external indicators, ML artifacts or order-book inputs.

## Execution assumptions and pinned Hummingbot compatibility

**Gate 5 is bounded to a real inspected pinned simulation path, not a deployment claim.** Admission policy identifies Hummingbot package label **20260920**, VERSION **dev-2.17.0**. The independently inspected source is **HCH725/hummingbot at commit 8b0e067e80ab62f10846d518dcb5a8218527ddb3**; its hummingbot/VERSION file reads dev-2.17.0 (verified this cycle via raw fetch at the pin). A package build digest was not available and this record does **not** claim that package 20260920 was byte-for-byte matched to this source commit or deployed. The engine-path claim is limited to this pinned source and previously reviewed matching research semantics.

- **Market/data:** BinanceSpotCandles constants.py maps the **1d** interval (INTERVALS bidict) and REST /api/v3/klines with symbol/interval/limit params (both verified this cycle at the pin); binance_spot_candles.py parses REST row[0] as timestamp with row[1..5] as O/H/L/C/V and WS kline keys o/h/l/c/v (verified this cycle). A strategy-specific controller must compute the declared single-leg III(21) features, verify contiguous completed bars and supply a single BTC-USDT spot 1d stream. The engine does not magically implement this range-location signal.
- **Controller/action/executor:** BacktestingEngineBase.simulate_execution iterates processed rows, calls update_state(row), controller.determine_executor_actions(), and CreateExecutorAction -> simulate_executor; OrderExecutorConfig with ExecutionStrategy.MARKET and BUY/SELL side routes to OrderExecutorSimulator (row path verified this cycle at the pin). The latter fills MARKET orders immediately at the first supplied row timestamp and **close** price, sets filled_amount_quote = amount×close, cum_fees_quote = trade_cost×filled_amount_quote, and CloseType.POSITION_HOLD. Full fill at one close is an explicit simulator convention, not proof of actual executable spot fills.
- **Timestamp caveat:** source candle timestamp is the **bar OPEN label**. BacktestingEngineBase.prepare_market_data uses merge_asof on timestamp_bt (verified this cycle); backward as-of joining alone does not establish that a completed close was known at the open. The required derivative controller gates the completed bar until T[t]+86400, and the resulting research event/fill ledger is explicitly normalized to that **close-effective** timestamp while using the simulator's same-row close price. This is a disclosed adaptation away from the source next-open execution and does not claim a real post-close order can fill at the already-observed close. No intrabar or lower-timeframe path is assumed.
- **Position and ledger:** BacktestPositionHold nets equal-base BUY and SELL ("Buys and sells of the same asset net out automatically. Realized PnL comes from matched buy/sell volume"), tracking average entry price, gross matched realized PnL and accumulated fees separately (verified this cycle at the pin). The engine's positions_held conversion is delayed; pin terminated_executors_window=None and use persistent pending/fill-confirmed controller state to avoid duplicate orders or losing prior fills. After a 0.001 BTC BUY at P_b and a 0.001 BTC SELL at P_s, modeled net quote PnL = 0.001*(P_s-P_b) - 0.0001*0.001*(P_b+P_s); do not misreport gross native net_pnl_quote or pnl_timeseries as fee-inclusive equity. An open position's marked equity carries the already-paid BUY fee.
- **Costs:** pin simulator trade_cost=**0.0001 per filled side** (0.01%, researcher-selected house research input — the source models no costs and no rate is attributed to it); this is **research cost input only**, not verified Binance realized commission. No separate simulator slippage is added, which is **zero additional modeled slippage**, not evidence of zero actual spread/latency/slippage. Spot funding is inapplicable (no fabricated futures funding). Binance minimum notional, lot/tick precision, exchange commissions, partial fills, liquidity and real trading viability remain unverified; do not infer live admissibility.
- **Reused independent path review:** HCH725/alpha-strategy-research PR **#417** merged 2026-10-24 after independent HB_READY review of this same pinned Binance spot 1d / MARKET first-close / POSITION_HOLD and fee-ledger research path. That verifies an **engine primitive**, not this new indicator, trade series, profitability, package digest or candidate-specific parity. This cycle additionally re-read the pinned VERSION, Binance spot candle constants/parser, backtesting engine row/action routing, OrderExecutorSimulator and BacktestPositionHold code at the pin.

## Evidence and six-gate summary

1. **Deterministic signals:** complete III(21) recurrence with inline code-faithful 1e-10 guards, full-window definability, edge cross-up entry and strict sub-zero level exit defined above; the page pins every operator so no helper equivalence is claimed beyond the disclosed NaN-freeze.
2. **Direction:** Binance BTC-USDT spot LONG/FLAT only, no short/margin.
3. **Entry/exit/risk:** cross-up BUY, sub-zero SELL, all other stop/target/trailing/time legs disabled; no hidden defaults.
4. **Position:** fixed 0.001 BTC, single pending/filled state, no cooldown (explicitly none), fresh-cross-up re-entry, no DCA/concurrency.
5. **Pinned engine:** concrete source commit re-read this cycle, 1d Binance candle path, controller action, MARKET full-close fill, timestamp normalization, fee and POSITION_HOLD ledger limitations; no novel unverified execution primitive used.
6. **Causality:** 63 completed-bar warmup, finite/gap guards, no future reads, decision and research-fill effective at completed bar close.

**Source-reported:** only the page identity, daily-OHLCV/no-lookahead/next-open methodology, unmodeled-costs disclaimer, close-in-range volume-weighted prose, single-leg III(21) code rule with its edge-entry/level-exit pair and long-only stance stated in Provenance. **Researcher-designed:** every market/fill/sizing/warmup/cost transfer plus the frozen NaN-free definability choice identified above. **Independently reproduced backtest performance:** none. **Historical survivor/HB Certified/Qlib parity:** none claimed. A stdlib-only scratch self-check this cycle confirmed ENTER/EXIT disjointness, flat-market III = 0.0 with no flat entries and flat-hold (not exit) while long, low-then-high single edge BUY, no retrospective entry for starts-positive histories, zero-volume defined prints, gap-with-midrange-close III == 0.0, and strict ENTER/EXIT alternation with at most one order per bar across five fuzz seeds — pure logic validation, not a backtest.

## Deduplication

Main at immutable SHA **90787d1e9e1d68dd66b516b757059ade8184c01** contained **342** root strategy records; README static count **342**. Working-tree filename search for `intraday-intensity` and `intradayintensity` returns zero strategy records; content search for `intraday intensity` and `IntradayIntensity` returns zero strategy records (the sole `intensity` prose hit in main is an unrelated ADX "trend intensity" mention in a DMI record). GitHub PR/issue searches for `intraday intensity` across this repository return zero items ever (open and closed). Ten open research/* PRs were checked (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend, #89 Chandelier, #92 SSL channel, #251 Swift 2YMA, #304 forven CCI, #331 AdxSmas, #350 ClucMay, #353 Heracles Keltner-Donchian) — none carries this primary source or an III rule.

Nearest neighbors are **not equivalent**: `quantifiedtrader-volume-price-trend-20-ma-level-long-flat-btcusdt-1d-2026-10-26` trades an **unbounded cumulative** percentage-flow against its own SMA20 with **level/level** triggers on **Close+Volume only** — this record trades a **bounded [−1,+1] 21-bar volume-weighted close-location ratio** with an **edge/level** zero pair reading **High/Low/Close/Volume** (a steady drip of small up-volume days and single spikes move the two lines differently by construction, and range/location inputs gate every order here); `quantifiedtrader-twiggs-money-flow-21-zero-cross-long-flat-btcusdt-1d-2026-10-25` — the closest sibling, sharing n = 21 and the zero edge/level shape — trades **interbar typical-price displacement** ((TP[t]−TP[t−1])×V/guarded-range summed over 21 bars against a sum(V×range) denominator, needing the prior bar and freezing incomplete windows to 0.0), while this record trades **pure intrabar close location** ((2C−H−L)/(H−L)×V summed over 21 bars against sum(V), no prior-bar term, NaN-until-full with 1e-10 guards): a gap-up day with a mid-range close spikes Twiggs while printing ~0.0 here, and steady drift with mid-range closes moves Twiggs while this record stays flat (scratch demonstration: gap series prints III == 0.0 throughout); `quantifiedtrader-disparity-index-14-zero-cross-long-flat-btcusdt-1d-2026-10-26` reads **Close only** with no volume or range input at all; `quantifiedtrader-random-walk-index-14-hysteresis-long-flat-btcusdt-1d-2026-10-26` trades √N-scaled High/Low displacement hysteresis levels with no volume input; `forven-obv-ema-cross-sma-gated-long-flat-btcusdt-1h-2026-10-19` cumulates **sign**-weighted volume against an EMA with an extra price gate on a **1h** grid. Different formula, different weighting, different trigger construction, different risk set: not a duplicate, paraphrase, or trivial parameter variant.

## Falsification plan

After separate downstream research authorization, compare the frozen III(21) edge/level zero pair against (a) a level-hold ablation entering from FLAT on any III[t] > 0 print (no cross requirement) and (b) a longer-window variant III(42) with the same comparators, on predeclared IS/OOS partitions; verify that the edge requirement and the window actually change entry/exit event times. Any new or unverified execution/data primitive requires representative Qlib/Hummingbot event-level validation before mass Qlib screening. Do not tune on OOS. No backtest was run by Scout.

## Crypto portability

Native crypto venue by declaration (Binance BTC-USDT spot 1d); no equity-to-crypto portability transform is asserted beyond the disclosed derivative identity. Spot semantics remove funding; minimum-notional, precision, liquidity and live viability remain unverified limitations, never assumed.

## Implementation status

Not implemented: no candidate-specific controller, feature module or replay artifact was created; only pinned generic engine files were read. The disclosed derived model must be implemented exactly if selected downstream.

## Adoption boundary

Frontmatter PASS is a **Scout-proposed six-gate research eligibility claim**, subject to independent Hermes Auditor review, not an independently approved merge. This is **not** a source-engine reproduction, actual Binance economics, profitable strategy, Qlib parity, HB Certified, survivor, deployment or Paper/Testnet/Live approval. No secrets, paid content, copied code block or private information included.

## Related Wiki records

None.

## Sources

- https://quantifiedtrader.com/backtest/strategies/intraday-intensity — QuantifiedTrader public strategy-library source; methodology and decision code read live 2026-10-26 (43,162 bytes HTML); page carries no publication date so source_as_of is the read date.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned Hummingbot source (VERSION, spot candle constants/parser, backtesting engine, order simulator, position-hold ledger re-read this cycle).
- https://github.com/HCH725/alpha-strategy-research/pull/417 — independent review of the same pinned spot 1d MARKET-close POSITION_HOLD research primitive.
