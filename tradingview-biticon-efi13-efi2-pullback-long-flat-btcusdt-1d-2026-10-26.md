---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Biticon Elder Force Index dual-EMA pullback: independent BTC-USDT spot 1d long-flat derivative"
created: 2026-10-26
updated: 2026-10-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
  - derived
status: research-only
confidence: medium
source_as_of: 2020-04-23
sources:
  - https://www.tradingview.com/script/8ifWKF7d-Elder-s-force-index-impulse/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Biticon dual-EMA Elder Force Index pullback — independent BTC-USDT spot 1d long-flat derivative

## Provenance

**Primary TradingView publication:** Biticon, *Elder's force index impulse*, published **2019-10-10**, updated **2020-04-23** (release note: color-change alerts), stable public script ID **8ifWKF7d**, open-source **indicator**: https://www.tradingview.com/script/8ifWKF7d-Elder-s-force-index-impulse/ . First-party published description checked 2026-10-26. It states that Force Index combines close-to-close price change and volume, that short/long EMAs respectively indicate pullback and trend, and prints **buy** when long EFI > 0 AND short EFI < 0 and **sell** when long EFI < 0 AND short EFI > 0. These inequalities are source-reported; the indicator itself is **not** a self-contained trading strategy. Complete executable Pine bytes and exact native EMA periods, seeding, alert-event edge, market, order handling and costs were **not retrieved**. An open-source badge does not imply those bytes were inspected.

**Explicit independent strategy derivative, not a lossless source-native reconstruction:** Researcher defines EFI raw input, **short EMA(2)** and **long EMA(13)**, arithmetic-mean EMA seeds, a fresh-buy-state transition as long entry, a sell-state level as long exit, disabled short leg, Binance unleveraged spot BTC-USDT UTC **1d** candles, 60-bar warmup, fixed 0.001 BTC fills, close-effective historical MARKET execution, cash ledger, hypothetical 0.1%-per-side research fee and all state/risk/invalid-data conventions below. EMA lengths 2/13 are **research choices** inspired by classic Elder practice, **not** values verified from Biticon's Pine. This derivative does not assert original signal-event equivalence, reproduce source performance or silently attribute execution rules to the author.

**Frozen research identity:** `TV:8ifWKF7d:Biticon:2019-10-10:update-2020-04-23 | independent-derived-v1:2026-10-26 | BinanceSpot:BTC-USDT:UTC1d | EFIraw=(C[t]-C[t-1])*V[t] | EMA2-short/EMA13-long arithmetic-mean seeds | buy-state=EFI13>0&&EFI2<0 fresh-edge | sell-state=EFI13<0&&EFI2>0 level-exit | long/flat Q=0.001BTC | completed-close MARKET | 60 contiguous bars | modeled fee 0.001 each side`. Changing any element creates a different derivative.

**Dedup:** At pre-write main `a9e5f43d8e1e8da9d59034bc14c7256a88dfa05a`, root-level strategy Markdown count and README both **362**. GitHub code search on main for exact TradingView ID `8ifWKF7d` and all-state PR search for that ID found no records or PRs; no open `research/*` PR used it. The closest `force-index-100-zero-state-two-sided-btcusdt-1d-2026-10-12.md` is a StockCharts-derived **EMA100 raw-force sign-state trend reversal** (not the simultaneous **EMA13-positive / EMA2-negative contrarian pullback** predicate), and the Elder-ray 123 combo reads high/low versus EMA without price-change-times-volume. Different signal family, input transformation, source and state transitions. Count equality is **not** an independent frontmatter re-audit of all existing 362 records.

## Economic mechanism
### Source-reported
Force Index measures signed price-change intensity weighted by traded volume. The author labels a short negative EFI within a long positive EFI regime a **buy** condition, and the opposite signs a **sell** condition: pullback against a broader signed-volume regime.

### Research interpretation
A short-lived downward volume-weighted price impulse inside a positive longer-run impulse may revert. This hypothesis is untested. This is a spot long-only derivative; its sell state is a liquidation trigger, never a naked short. Neither profitability nor the original author's exact indicator values are claimed.

## Signal

1. **Input:** one actual Binance Spot BTC-USDT UTC daily OHLCV sequence. For zero-based completed bar `t`, finite `O[t],H[t],L[t],C[t]>0`, `H>=max(O,C)`, `L<=min(O,C)`, `H>=L`, and finite base-volume `V[t]>=0`. Daily raw open timestamps strictly increase by 86,400 seconds. Reject duplicate, missing, malformed, nonfinite or out-of-order bars. No synthetic interpolation.
2. **Raw force:** for `t>=1`, `F[t]=(C[t]-C[t-1])*V[t]` in USDT*BTC units. The raw force on t=0 is undefined; no lookahead, normalization or volume-weighting variant.
3. **Short EMA2:** seed `S[2]=(F[1]+F[2])/2`; for `t>=3`, `S[t]=(2/3)*F[t]+(1/3)*S[t-1]`. **Long EMA13:** seed `L[13]=sum(F[1]..F[13])/13`; for `t>=14`, `L[t]=(2/14)*F[t]+(12/14)*L[t-1]`. All comparisons are against mathematical zero with no rounding or epsilon. These seeds/lengths are researcher-defined.
4. **Buy-state:** `B[t]=(L[t]>0 && S[t]<0)`. **Sell-state:** `X[t]=(L[t]<0 && S[t]>0)`. Equality to zero is neutral. A state can remain true over multiple bars.
5. **Entry:** when confirmed FLAT, no order pending, and `B[t] && !B[t-1]`, submit exactly one long BUY for 0.001 BTC. No entry merely because B remains true. A FLAT state arising after liquidation must wait for a *later* fresh B transition. Pre-warmup B values may establish the previous-state bit but never place orders.
6. **Exit:** when confirmed LONG, no order pending, and `X[t]` (level, not just first edge), submit a full-inventory SELL. Exit is evaluated before any entry, and there is no same-bar reversal. A failed or unfilled SELL latches liquidation intent and retries at the next valid completed bar, without requiring X to remain true. A failed BUY returns to FLAT and requires a new B edge. Never mark an order filled merely because it was submitted.
7. **Book and risk:** state `FLAT -> BUY_PENDING -> LONG -> SELL_PENDING -> FLAT` only on confirmed simulated fills. Maximum one spot position, one pending action, 0.001 BTC initial and maximum inventory, no pyramiding, averaging, BO/SO/DCA, short, leverage, hedging, cross-asset exposure, cooldown, time stop, forced end-of-sample sale, stop loss, take profit, trailing, intrabar trigger or hidden default. Position remains exposed indefinitely until X; mark an open end-of-sample inventory to the last **actual** close, not as a fictitious realized liquidation.
8. **Warmup and gaps:** first 60 **consecutive complete** UTC daily bars are strictly no-trade; first possible decision is completed bar 61 (one-based). Both EMA states and their previous values must be defined. Any discontinuity suspends new decisions/fills; restart 60 valid contiguous-bar warmup before new signals. Existing holdings and unresolved orders remain explicit ledger items requiring reconciliation, never magically closed.

## Required data

One Binance Spot BTC-USDT `1d` candle stream: actual UTC open timestamp, open/high/low/close and **base traded volume**. Only C and V enter F; O/H/L validate actual bars. No other timeframe, synchronized second market, order book, external sentiment, fitted model, funding, perpetual mark/index, security() or incomplete candle is required. Decision-time timestamp is the completed daily bar's `raw_open+86400`, **not** the exchange API's open-time stamp.

## Execution assumptions

**Pinned Hummingbot evidence inspected via connected GitHub on 2026-10-26:** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, package label `20260920`, `hummingbot/VERSION=dev-2.17.0`. The Scout read these pinned code paths directly; it did **not** rehash the installed wheel (earlier independent PR #414 wheel-binding evidence remains separate).

- `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` explicitly supports `1d`; `binance_spot_candles.py::_parse_rest_candles` maps Binance REST row[0] to **candle-open timestamp**, rows[1..5] to actual O/H/L/C/V. Require 86,400-second complete-bar availability before acting, validate original continuity before feature preparation, and normalize the strategy's simulated decision/fill time to close-effective `T+86400`; do not treat a live unfinished daily bar as complete.
- `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py::run_backtesting` initializes `binance` trading rules and `1d` candles; `simulate_execution` updates controller state per processed row, invokes `determine_executor_actions()`, and routes `CreateExecutorAction(OrderExecutorConfig)` to the matching executor simulator with a forward slice beginning at that row. A **strategy-specific ControllerV2** would compute the pinned F/EMA features and state (not already implemented or claimed as an existing controller).
- `hummingbot/strategy_v2/executors/order_executor/data_types.py` provides `OrderExecutorConfig` with `connector_name="binance"`, `trading_pair="BTC-USDT"`, `execution_strategy=MARKET`, `side=BUY/SELL`, `amount=Decimal("0.001")`, `leverage=1`. SELL amount is the **confirmed remaining** BTC inventory. The simulation is single-venue unleveraged spot; no funding or borrow interest applies to this instrument.
- `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` explicitly sets MARKET fill timestamp to the **first supplied row**, price to that row's **actual close**, filled quote amount to amount*close, fee to `trade_cost*filled_amount_quote`, and close type to `POSITION_HOLD`. This **historical close-row model** is what the derivative specifies; it does **not** claim an executable live market order can obtain a completed candle's historical close. No limit/maker/next-open/intrabar fill is required.
- `BacktestPositionHold._process_order` in `backtesting_engine_base.py` nets BUY/SELL in base units, calculates weighted average entry and gross matched realized PnL, and separately accumulates `cum_fees_quote`. Run with `terminated_executors_window=None` so the controller can reconcile filled POSITION_HOLD actions across daily bars; use the complete executor/position ledger and final flush. Maintain a simple strategy-specific cash/inventory guard rather than assuming simulator enforces real spot balances or order precision.
- **Cost/cash convention:** start with exactly 10,000 USDT cash and 0 BTC, size 0.001 BTC. Research-only `f=0.001` of actual simulated quote notional on **each filled side**, never asserted as real Binance fees. BUY only if `cash>=Q*P*(1+f)`, then `cash-=Q*P*(1+f)`; SELL only if `inventory>=Q`, then `cash+=Q*P*(1-f)`. Matched net realized PnL `Q*(P_sell-P_buy)-f*Q*(P_buy+P_sell)`; open equity `cash+inventory*last_actual_close`, with no invented terminal fill/fee. Engine gross PnL must not be mislabeled net of fees. Spread, slippage, latency, actual partial fills, precision and min-notional are **unverified**, not presumed zero in live trading. No realized-funding claim for futures.
- `backtesting_data_provider.py::get_price_by_type` may default to `Decimal("1")` when a key is absent: **reject** that fallback and missing/nonfinite actual candle prices; no synthetic fill. Before accepting any result, require real feed rows, explicit fill event and reconciled inventory. The historical close-price convention is a research approximation, not trading authorization.

## Evidence
### Source-reported
Biticon's dated TradingView public indicator description contains both sign-conjunction buy/sell predicates and the short/long EMA interpretation. It supplies **no verified numerical trading results** for this independent spot derivative.

### Independently reproduced
Not independently reproduced. This Scout inspected the named pinned Hummingbot **source paths**, but ran **no** Pine, Hummingbot or Qlib backtest, downloaded no historical candles, and performed no fill or fee measurement.

### Negative evidence
The TradingView page text did **not** expose full Pine source, native EMA lengths/seed, exact alert-bar semantics or original order properties. These are explicitly researcher-defined rather than silently guessed. This is an indicator-to-strategy derivative, not a claim that the indicator's original hypothetical trades passed. Original/derivative trade-event equivalence is **not** established. Close-effective MARKET simulation is not live close execution. The package-to-wheel binary hash was not rechecked this run.

## Six-gate admission evidence (Scout proposal; independent exact-head review required)

1. **Determinism:** raw `(C[t]-C[t-1])*V[t]`, pinned EMA2/13 mean-seeded recursion, strict sign states, entry-edge and exit-level priority, invalid-data and warmup rules.
2. **Direction:** Binance unborrowed spot long/flat only; author sell signal closes long, no short.
3. **Entry/exit/risk:** buy-state rising edge and opposite sell-state level, retry behavior; no unmentioned SL/TP/trailing/time or forced liquidation.
4. **Position/DCA/state:** fixed 0.001 BTC, 10k cash guard, fill-confirmed pending states, one position, no DCA/pyramiding, later fresh-edge re-entry only.
5. **Pinned engine/data/economics:** verified pinned `1d` Binance SpotCandles, controller action and OrderExecutor MARKET first-row close model, POSITION_HOLD cost basis/fee ledger, spot-only fee/cash and no funding, no invented missing prices; model does not promise live fill realism.
6. **Causality:** 60 contiguous completed UTC daily bars, effective close availability `T+86400`, only current/prior raw inputs and recursive past EMA; no future extrema, repaint, higher-timeframe incomplete bar, fill-before-data or unobserved terminal sale.

**PASS here is a research-only Scout proposal, not independent Auditor approval, profitability, source-native fidelity, Qlib parity, Survivor/HB Certified status or Paper/Testnet/Live authorization.** Independent Hermes Auditor GitHub Webhook Review must verify this exact head and either PASS/merge or NOT_LOSSLESS/close; no Scout self-merge.

## Falsification plan

After separate authorization and representative Hummingbot/Qlib event-level primitive parity where needed, evaluate on a fixed full continuous window with modeled fees: (a) compare entry-edge pullback rule against long EFI13>0 sign-state baseline; (b) test whether the opposing sell-state exit delays loss containment versus a flat-on-EFI13<=0 derived comparator; (c) check actual number of completed B and X states, fill/cost reconciliation, open terminal exposure and drawdown. These comparators are **future separate hypotheses**, not changes to the frozen candidate. No backtest was run in this Scout.

## Crypto portability

Single BTC-USDT unleveraged Binance spot market is a researcher selection, not a whitelist admission restriction. Transferring to other coins, futures, intraday frames, DCA BO/SO overlays or 3×/5× leverage changes the execution/cost contract and requires separately declared research. Volume units, liquidity, precision, real fees and funding differ across instruments.

## Limitations

Indicator-to-strategy adaptation, source Pine not inspected, chosen EMA lengths/seeds and state semantics not author-native; no observed profitability, no independent fill/fee/equity reproduction, no wheel rehash, and a potentially very long unprotected holding period until the opposite sign conjunction. The close-row MARKET model can be causally simulated on pinned historical completed bars but is not guaranteed realizable at the exchange; execution/economic discrepancies must be investigated before certification. Main root PASS statuses beyond the inspected examples were not exhaustively re-audited; a numeric count match alone is not an admission integrity proof.

## Implementation status

`not-implemented`. No dedicated ControllerV2 strategy, Qlib executable recipe, market-data download, backtest or deployment was created. If selected downstream, use existing `IMPLEMENTATION_NEEDED` engineering route without introducing another admission status.

## Adoption boundary

`research-only`, `not-approved`, `approval_scope: research-only`. This record cannot authorize trading, paper/testnet/live execution or profitability claims. Any research DCA overlay must be disclosed as its own changed strategy/execution model.

## Related Wiki records

None linked or created in this Scout. Hermes may add independently reviewed research context later; no Wiki mutation in this cycle.

## Sources

- Primary: https://www.tradingview.com/script/8ifWKF7d-Elder-s-force-index-impulse/ — Biticon, 2019-10-10, updated 2020-04-23.
- Pinned engine source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — `dev-2.17.0`, package label `20260920`.
- Admission contract: `main` `README.md` and `.github/HB_READY_REVIEW.md` at pre-write `a9e5f43d8e1e8da9d59034bc14c7256a88dfa05a`.
