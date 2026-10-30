---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: OhRayOhRay Tri-band RSI14 WilliamsR14 BB20 oversold confluence long-flat BTC-USDT spot 1h independent close-fill derivative
created: 2026-10-30
updated: 2026-10-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-30
sources:
  - https://www.tradingview.com/script/pcqUER51-Tristan-s-Tri-band-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# OhRayOhRay Tri-band RSI14 / Williams %R14 / BB20 oversold-confluence close-fade (independent derivative)

## Provenance

- **Primary TradingView source:** [Tristan's Tri-band Strategy](https://www.tradingview.com/script/pcqUER51-Tristan-s-Tri-band-Strategy/) by **OhRayOhRay**, public open-source-script page, **2025-11-02** publication, page read **2026-10-30**. Stable TradingView script ID `pcqUER51`. Page's first-party description, not the unavailable embedded Pine source bytes, supports the source-reported rules below. No Pine byte-equivalence, unobserved default lengths or native order-fill identity is claimed.
- **Source-native facts from first-party page:** three-way long confluence: RSI at/below 30, Williams %R in -100..-80, and price touching/breaking the lower Bollinger Band, during selected trading sessions. Short confluence: RSI >=70, Williams %R -20..0, and price touching/breaking upper band. Long exit on reaching upper BB **OR** RSI >=70; short exit on reaching lower BB **OR** RSI <=30. Author says signals confirm at candle close and strategy enters next bar open. Sessions may select NY/London/Asia; periods, precise band basis, exact Pine order state, sizing, costs and stop implementation are not specified in the accessible prose.
- **Immutable identity of this researcher-defined derivative:** `TV:pcqUER51|OhRayOhRay|source-2025-11-02|derived-close-long-v1-20261030|BinanceSpot:BTC-USDT:UTC1h|RSI14-Wilder<=30&WPR14<=-80&C<=SMA20(C)-2*PSTD20(C)|exit:C>=SMA20(C)+2*PSTD20(C)OR-RSI14>=70|next-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-each-side|warmup40`. This is **not source-native**. Altering any signal, session, position, cost or fill rule creates a different version.
- **Researcher-defined event-changing choices, all declared upfront:** (1) choose BTC-USDT Binance **spot** UTC 1h and **long-only**; short disabled; (2) choose 24/7 continuous market with **no session filter**, rather than author-selected sessions; (3) pin Wilder RSI14, Williams %R14 and close-based SMA20 +/- two **population** standard deviations as explicit variants/periods, not claimed to be author defaults; (4) require **completed CLOSE <= lower band** rather than source's possibly intrabar touch, and **completed CLOSE >= upper band** rather than source's possibly intrabar reach; (5) use next **completed** bar close instead of author's next bar open; (6) fixed 0.001 BTC, cash 10,000 USDT, idealized MARKET fills, hypothetical fee 0.1%/side, no additional modeled slippage, 40-bar warmup, no SL/TP/trailing/DCA. These are a separately specified research strategy, not a silent repair of inaccessible Pine.
- **Dedup 2026-10-30:** GitHub connector searched main for `pcqUER51`, `OhRayOhRay`, `Tristan`, `tri-band` (no matches) and reviewed 11 open `research/*` PR heads/titles; no same TradingView URL or materially identical triple confluence. Closest records `freqtrade-bband-rsi-dip-buy` (two-key RSI+typical-price BB with ROI/stop; no Williams %R), `chartart-bollinger-rsi-double-joint-cross` (RSI/BB joint crosses, two-sided, no Williams %R), and `forven-williams-r-adx-gated` (Williams %R cross + ADX, no RSI/BB) use different decision-critical mechanisms. Not a trivial parameter variant.

## Economic mechanism

### Source-reported

The author presents three-indicator oversold/overbought confluence at outer Bollinger bands as a mean-reversion entry and opposite-band/RSI-overbought long exit; no independently verified return, Sharpe or execution performance accompanies the accessible first-party description.

### Research interpretation

A stricter **close-confirmed** triple-extreme dip buyer: require simultaneous RSI, Williams %R and Bollinger-band weakness, then hold until a completed-close upper-band recovery or RSI overbought state. Strong sustained downtrends can leave the position underwater because protective stops are intentionally absent.

## Signal

**Inputs and clock:** one contiguous, UTC-aligned Binance BTC-USDT **spot 1h** OHLCV stream. Index `t` is the candle's **open** timestamp `T[t]`; all its OHLCV become decision-available at `E[t] = T[t] + 3600 seconds`. No partially formed bars or intrabar signals. Every comparison uses completed values at E[t].

**Fully pinned indicators, close price only except Williams %R:**
- `RSI14[t]`: let `d[k] = C[k]-C[k-1]`, gains `max(d,0)`, losses `max(-d,0)`; seed average gain and loss as arithmetic means of the 14 changes `d[1]..d[14]`; for each subsequent k use Wilder recursive `avg[k]=(13*avg[k-1]+current[k])/14`. RSI = `100-100/(1+avgGain/avgLoss)`; if loss=0 and gain>0 return 100; if gain=0 and loss>0 return 0; if both=0 return 50. Values before index 14 are undefined.
- `WPR14[t] = -100*(HH14[t]-C[t])/(HH14[t]-LL14[t])`, where `HH14` and `LL14` are max high and min low over indices `t-13..t` inclusive. If the entire window has zero range, assign -50 (never an oversold entry); before index 13 undefined.
- `M20[t] = (1/20)*sum(C[k],k=t-19..t)`; `SD20[t] = sqrt((1/20)*sum((C[k]-M20[t])^2,k=t-19..t))` (population, not sample standard deviation); `Lower=M20-2*SD20`, `Upper=M20+2*SD20`. Before index 19 undefined. A zero-SD window is valid and uses coincident bands.

**ENTRY on eligible completed bar t while FLAT with no pending action:** `RSI14[t] <= 30 AND WPR14[t] <= -80 AND C[t] <= Lower[t]`. All three must hold on the **same** completed candle; equality qualifies. No edge/cross requirement, volume gate, time-of-day filter, or additional reversal candle. `WPR` is necessarily >= -100 for valid candles; no independent bound needs to be guessed.

**EXIT on eligible completed bar t while LONG and no pending action:** `C[t] >= Upper[t] OR RSI14[t] >= 70`. If both true, one SELL only; no priority ambiguity because both have identical full-position effect. Equality qualifies. No opposite-short reversal. There is **no** protective SL, separate TP price, trailing, ROI ladder, time-limit, cooldown, DCA, partial exit or sample-end forced liquidation; these are intentionally disabled for this derivative. An open position can persist across indefinitely many bars.

**Warmup:** completed indices 0..39 (40 bars) are data-only, FLAT and non-trading; first decision index 40. All rolling windows and Wilder seed are computed causally from earlier/current **completed** bars only. No future extrema, pivot confirmation, model training, MTF alignment, repaint, or negative shifts.

**Position and pending-action machine:** initial cash `Decimal("10000")` USDT, BTC inventory zero, FLAT. Exactly one position or pending action, fixed `Q=Decimal("0.001")` BTC; no borrowing, margin, leverage, shorting, pyramiding, concurrency or safety orders. At decision E[t], queue one MARKET BUY/SELL for **the next completed candle** f=t+1. At E[f], take the **actual recorded** C[f] as the historical idealized fill, not the signal candle's close or an invented price. BUY requires cash >= Q*C[f]*(1+fee); otherwise consume the signal, remain FLAT and do not partially fill or defer. A filled BUY adds exactly Q BTC and subtracts its fee-inclusive cost. A filled SELL removes exactly Q BTC and adds fee-net proceeds. On either fill bar, **do not evaluate a new signal**; earliest new decision is index f+1. If no f exists at sample end, pending action remains unfilled; a pending SELL leaves its existing inventory marked to the last real close. No order is generated on an invalid or missing bar.

**Exact cash/equity ledger:** fee `Decimal("0.001")` each side of actual quote notional; BUY cash delta `-Q*P*(1+fee)`, SELL `+Q*P*(1-fee)`, BTC inventory +/- Q. Use `Decimal(str(observed_price))`, never `Decimal(float)`; round-trip net `Q*(P_sell-P_buy)-fee*Q*(P_buy+P_sell)`; marked equity `cash+BTC*C[t]`. Position truth comes solely from the exact ledger, not native float dust, `positions_held` or terminated-executor retention. Compare simulated side/amount/quote/fee against ledger at each full fill with tolerance `max(1e-8, 1e-12*Q*P)` for float quote/fee reconciliation; any mismatch aborts as `ENGINE_MISMATCH`, never silently repairs state.

## Required data

Only real Binance BTC-USDT spot 1h O/H/L/C (volume may be present but is not a predicate). Validate finite positive OHLC, `H>=max(O,C)`, `L<=min(O,C)`, `H>=L`, finite nonnegative volume, strictly increasing UTC timestamps exactly 3600 seconds apart, no duplicates or incomplete bars. **Abort** on invalid/missing/duplicate/discontinuous data; never forward-fill, interpolate, synthesize price or use the provider's default `Decimal("1")` missing-price fallback. Use only completed bars at their E[t] availability. No funding feed, order book, cross-asset state, lower timeframe, external sentiment or ML.

## Execution assumptions

- **Pinned engine:** Hummingbot package `20260920`, `hummingbot/VERSION=dev-2.17.0`, code `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`; pinned files **read via GitHub connector this Scout**: `binance_spot_candles/constants.py` (1h supported, Binance `/api/v3/klines`), `binance_spot_candles.py` (open-time timestamp and OHLCV REST parsing), `backtesting_engine_base.py` (`update_state` then `determine_executor_actions` and `CreateExecutorAction` dispatch), `order_executor/data_types.py` (MARKET, side, amount, position_action, leverage), `order_executor_simulator.py` (MARKET first supplied row's **actual close**, quote = float(amount)*close, fees = trade_cost*quote, `POSITION_HOLD`), and `backtesting_data_provider.py` (feed, trading-rule and missing-price behavior). Previously independently reviewed same idealized spot MARKET-close/ledger primitive: alpha PRs #414, #550 and PASS review #628. No claim of rehashed wheel bytes or deployed container in this Scout.
- **Required future controller binding (not implemented):** a dedicated controller in the pinned `BacktestingEngineBase` path would compute the completed-bar signal at E[t], hold a one-bar pending action, then issue `CreateExecutorAction(OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),position_action=OPEN/CLOSE,execution_strategy=MARKET,price=None,leverage=1))` **only** when the fill row t+1 is processed. The controller must not use t+1's price to decide the earlier signal. Simulator's raw `timestamp` is the bar **open**; research economic decision/fill availability time is `E[t]` / `E[t+1]`. This is an idealized **historical next-completed-close** convention, **not** an executable live order promise at that past close.
- **Bounded compatibility:** this derivative uses one Binance spot 1h stream, one MARKET-close order per action, and a separate exact full-fill cash ledger. The simulator directly uses supplied amount and close; it does **not** verify exchange lot/tick/min-notional acceptance, partial fills, latency, spread or real liquidity. These exchange constraints are **not additional conditional branches in this declared idealized research model**, and no exchange-accepted fill is claimed. Future live/realistic execution requires separately pinned real rules and costs; this record does not pretend those checks occurred. It does not invoke `quantize_order_amount`, whose externally fetched trading rules are not historically pinned here. The explicit model is therefore deterministic **only for this idealized research fill convention**, not for exchange order validity.
- **Costs:** simulator `trade_cost=0.001` per side is a **hypothetical** research fee, not a verified Binance tier. No **additional modeled** slippage; not a claim of zero real slippage. Unleveraged spot has no perpetual funding or liquidation, not an assumption of zero perpetual funding. Do not use native gross-only executor summary as net equity; use the ledger and fee reconciliation. If missing real close or any engine mismatch, fail closed.
- **Gate 5 boundary:** one already-reviewed pinned data/executor primitive is reused, not inferred from a generic API name. No strategy-specific implementation, performance backtest, Qlib parity, Testnet or Live run is claimed. Representative Hummingbot↔Qlib event-level parity is required before **large-scale Qlib screening** of any new execution path, not a new HB_READY profitability gate.

## Evidence

### Source-reported

First-party TradingView page (2025-11-02) states the RSI/Williams %R/Bollinger three-way confluence and the opposite-band-or-RSI long exit. Its session filter, both-sided signals, wick/touch semantics and next-open statement are source-native, **not** silently attributed to this derivative. No source performance metrics are used as verified facts.

### Independently reproduced

Not independently reproduced. No Pine byte comparison, trading strategy backtest, Hummingbot/Qlib event replay, OOS or profitability reproduction was performed.

### Negative evidence

The page's accessible text does not disclose all Pine defaults or its precise source order state. The derivative resolves them as **explicit researcher choices**, not alleged source facts. Prior PR #629/#630 were rejected because they made historical venue trading-rule acceptance an unfixed **event-critical** condition; this record instead declares a bounded, idealized full-amount MARKET-close simulator without such an unfixed conditional and makes no real exchange-acceptance claim. Independent Auditor must still verify whether this bounded Gate 5 path suffices and close NOT_LOSSLESS if not. GitHub main at pre-write SHA `42708a5c90d9cdfd9d20732becfc128183d0b5ee` has 454 root-level records and README count 454; 16 distributed frontmatter checks were PASS, **not** an exhaustive 454-file admission audit.

## Falsification plan

For separately authorized later engineering: test exact 30/-80/band boundaries, RSI flat-window zero cases, Williams %R zero range, BB zero variance, 39/40 warmup boundary, persistent-oversold level versus crossover, upper-band/RSI simultaneous exit, one-bar pending and fill-bar exclusion, insufficient cash, final-bar pending, gaps/missing-price abort, float-to-Decimal ledger reconciliation and realistic venue acceptance as a distinct economic model. Do not represent source-reported statistics as reproduced.

## Crypto portability

Pinned only to Binance BTC-USDT spot UTC 1h, continuous 24/7. Other pairs, sessions, timeframes or perpetual contracts change events/costs and require a separately identified derivative and compatibility evidence. DCA BO/SO 6/6/6 and 3x/5x are optional downstream research experiments, **not** this HB_READY admission rule.

## Limitations

This derivative is deliberately not a lossless Pine implementation: periods, band basis, session disablement, long-only direction, close-touch rather than intrabar touch, next-completed-close rather than next-open, sizing and costs are researcher-defined. No protective stop or max hold means severe drawdown is possible. Research fills are idealized; no exchange precision, minimum notional, actual fee tier, slippage, latency or partial-fill realism is established. A future controller remains to be implemented; PASS does not prove it already exists.

## Implementation status

`implementation_status: not-implemented`; `status: research-only`. `hb_ready_status: PASS` here is a **Scout proposal pending independent Hermes Auditor**, not independent approval, Qlib parity, Survivor, HB Certified, or deployment authorization.

## Adoption boundary

`adoption: not-approved`; `approval_scope: research-only`. No Paper/Testnet/Live/trading permission. Scout makes no changes to Hummingbot, Qlib, n8n, cron, main, README or existing strategies. The independent Auditor owns exact-head PASS/NOT_LOSSLESS and only the existing signed webhook receiver owns post-merge README bookkeeping.

## Related Wiki records

None; no Wiki Brain write in this Scout.

## Sources

- https://www.tradingview.com/script/pcqUER51-Tristan-s-Tri-band-Strategy/ — OhRayOhRay, *Tristan's Tri-band Strategy*, published 2025-11-02; first-party description read 2026-10-30.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned Hummingbot source; specific files listed in Execution assumptions.
- https://github.com/HCH725/alpha-strategy-research/pull/414 — independently reviewed bounded MARKET/engine lineage.
- https://github.com/HCH725/alpha-strategy-research/pull/550 — independently reviewed spot MARKET-close/ledger lineage.
- https://github.com/HCH725/alpha-strategy-research/pull/628 — independent PASS review of same bounded spot research fill primitive.
