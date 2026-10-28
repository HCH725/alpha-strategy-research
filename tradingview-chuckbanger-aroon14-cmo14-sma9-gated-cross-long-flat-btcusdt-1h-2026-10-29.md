---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "ChuckBanger Aroon14 histogram-gated CMO14/SMA9 crossover — independently derived BTC-USDT spot 1h long-flat"
created: 2026-10-29
updated: 2026-10-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
status: research-only
confidence: medium
source_as_of: 2019-10-22
sources:
  - https://www.tradingview.com/script/hqJGWNKa-Aroon-Histogram-CMO-ChuckBanger/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Aroon histogram regime + Chande Momentum Oscillator signal-line crossover — independent research derivative

## Provenance and immutable identity

**Primary public TradingView source:** ChuckBanger, *Aroon Histogram + CMO [ChuckBanger]*, published **2019-10-22**, first-party public open-source **indicator**, stable script ID **hqJGWNKa**; public page checked 2026-10-29: https://www.tradingview.com/script/hqJGWNKa-Aroon-Histogram-CMO-ChuckBanger/ . The author's accessible text states that the indicator combines an **Aroon histogram**, a **Chande Momentum Oscillator (CMO)** line and a **simple moving average of CMO as a signal line**. It suggests trading the signal-line/CMO crossings or CMO extremes, but does **not** prescribe which crossing is a long/short entry, how the Aroon histogram gates an order, exact lookbacks, exits, risk, position state, execution clock, fees, or venue. The full executable Pine bytes and Pine language version were **not retrievable** from the public text interface; no source-code hash or source-native event equivalence is claimed. Do not mistake the author's indicator for an original executable strategy.

**Explicit independent derivative, NOT source-native/lossless:** preserve the public source's three indicator concepts and its suggestion to trade CMO versus its SMA. The researcher defines **all decision-critical executable details** below: Aroon 14 with a 15-candle extrema window and latest-tie rule; CMO 14 from raw close changes; SMA9(CMO); histogram-positive entry gate; upward CMO/SMA crossing BUY; downward crossing or histogram-nonpositive SELL; BTC-USDT Binance spot UTC 1h; LONG/FLAT; single 0.001 BTC; no stops, targets, short, DCA or other original visual/alert modes; 100 completed-bar warmup; t signal to t+1 completed-close MARKET historical fill; 10,000 USDT starting cash; 0.1% modeled fee per filled side; exact state and failure policies. These researcher choices are **not** attributed to ChuckBanger and may produce entirely different events from any original-script settings.

**Immutable derived-strategy identity:** `TV:hqJGWNKa:ChuckBanger:2019-10-22:public-description | independent-derived-v1:2026-10-29 | Binance:BTC-USDT:spot:UTC1h | Aroon14:15bar-extrema-most-recent-tie:up-minus-down>0 | CMO14:raw-delta-sums:SMA9 | CMO-crossup-and-Aroon-positive-buy | CMO-crossdown-or-Aroon-nonpositive-sell | LONG-FLAT:Q0.001:cash10000 | completed-t-to-next-completed-close-MARKET | warmup100 | fee0.001-per-side`. Any parameter, tie rule, signal priority, execution timing, market, risk or cost change creates a different derivative.

**Dedup at stable main `df66b2c1007a500262f4316f0809ff4bf71df865`:** GitHub connector's nontruncated recursive main tree contained **417** root-level strategy Markdown records (two READMEs excluded); README static counter **417**. Thirteen distributed frontmatter samples were PASS; this is **not** a complete 417-record frontmatter audit. GitHub main code search for `hqJGWNKa` returned none, and all-state PR search for `hqJGWNKa` or `Aroon CMO` returned none; the ten currently open PR titles/bodies were examined for source and mechanism. Nearest admitted cousins are `forven-aroon-up-down-cross-long-flat-btcusdt-1h-2026-10-17.md` (Aroon line crossover alone), `aroon-oscillator-midline-rail-exit-btcusdt-1d-2026-10-09.md` (Aroon-only midline and rail exits), `tradingview-edgetools-cmo9-oversold-time5-long-flat-btcusdt-1d-2026-10-26.md` (CMO oversold and timed exit) and `fmz-482833-cmo14-bb20-crossunder-oversold-long-flat-btcusdt-1h-2026-10-27.md` (CMO/Bollinger lower-band). None requires a **CMO14-versus-SMA9 upward crossing specifically gated by Aroon14 histogram >0, with crossdown-or-Aroon-regime-loss exit**; this is not a length-only retune.

## Falsifiable mechanism and exact signals

**Hypothesis (researcher interpretation):** a positive Aroon high/low recency differential may filter CMO momentum-line crosses to favor upward price regimes. This is a testable hypothesis, **not** an independently reproduced return, Sharpe, win rate, Survivor status or source-performance claim.

**Data and effective clock:** exactly one Binance BTC-USDT **spot 1h** OHLCV series, strictly contiguous UTC candles with exchange **open** timestamp `T[t]`, spaced 3600 seconds. Candle `t` becomes decision-available at `E[t]=T[t]+3600` seconds, not at its raw open label. All O/H/L/C must be finite and >0; H>=max(O,C), L<=min(O,C), V finite >=0; strictly ordered timestamps with no duplicates, gaps, synthetic rows, missing close, interpolation, forward fill or partial candle. Validate the **raw** feed before feature joins or Hummingbot `dropna`; abort the bounded research run if any violation exists. No external/secondary feed.

**Frozen float64 indicator arithmetic, chronological order, no fitting:**

1. For `t>=14`, inspect the **15 completed highs** `H[t-14..t]` and lows `L[t-14..t]`. Let `ageHigh` and `ageLow` be the number of bars since the **most recent** occurrence of the maximum high and minimum low respectively, integers in [0,14]; a tied extreme uses the most recent bar. Define `AroonUp14[t]=100*(14-ageHigh)/14`, `AroonDown14[t]=100*(14-ageLow)/14`, `AroonHist[t]=AroonUp14[t]-AroonDown14[t]`. Both equalities and a zero histogram are **not bullish**. Undefined before t=14. This exact 15-candle convention and tie rule are researcher-defined, not asserted to be the author's original Pine implementation.
2. `delta[k]=C[k]-C[k-1]` for k>=1, `gain[k]=max(delta[k],0)`, `loss[k]=max(-delta[k],0)`. For t>=14, `G14[t]=sum(gain[t-13..t])`, `L14[t]=sum(loss[t-13..t])`, `CMO14[t]=100*(G14[t]-L14[t])/(G14[t]+L14[t])`. If the denominator is zero or any value nonfinite, abort rather than invent a momentum observation; CMO is undefined before t=14. No Wilder smoothing or EMA.
3. For t>=22, `CMOsignal9[t]=sum(CMO14[t-8..t])/9`; no signal before t=22. A crossover uses **completed** t-1 and t values: `UP[t]=(CMO14[t-1]<=CMOsignal9[t-1]) AND (CMO14[t]>CMOsignal9[t])`; `DOWN[t]=(CMO14[t-1]>=CMOsignal9[t-1]) AND (CMO14[t]<CMOsignal9[t])`. Equality on the current bar is not a crossing. All sums are fixed-window arithmetic in ascending bar order.
4. **Warmup:** require 100 consecutive fully valid completed bars, indexed 0..99, with FLAT initial state, no orders and no pre-warmup inherited positions. Earliest decision bar is t=100. Indicators continue updating on all completed bars including order-fill bars; do not reuse a crossing that occurred during a pending order or warmup.
5. **FLAT entry:** only if `UP[t] AND AroonHist[t]>0`, emit a single pending BUY at decision availability E[t]. A CMO cross while AroonHist<=0 is **lost**, not delayed until the Aroon gate later turns positive; a fresh UP is required. No entry on a pure Aroon flip. A pending order suppresses further decisions.
6. **LONG exit:** on any completed decision bar strictly after the confirmed BUY fill bar, emit a full SELL if `AroonHist[t]<=0 OR DOWN[t]`. For simultaneous conditions, log `AR00N_NONPOSITIVE` first, `CMO_CROSSDOWN` second; only one SELL. A CMO cross-up during LONG is ignored. If neither exit ever occurs, hold through sample end; no synthetic liquidation.
7. **State machine:** `FLAT` -> `PENDING_BUY` -> `LONG` -> `PENDING_SELL` -> `FLAT`. No same-bar re-entry or new signal on a fill bar. Following a SELL, entry requires a **new** UP cross on a later completed decision bar with positive histogram. One position, one outstanding action, fixed Q; no pyramiding, scale-in/out, partial fill acceptance, safety orders, DCA, compounding, cooldown beyond the pending/fill suppression, short, leverage, margin, borrow, perpetual funding, intrabar stop/target, trailing, breakeven, time exit, forced sample-end liquidation or undocumented default. On missing/partial/rejected/mismatched fill or missing real execution price, **abort**; a last-bar pending order without a following actual candle remains unfilled and is not a trade.

## Execution assumptions — pinned Hummingbot Gate 5

**Engine:** HCH725/hummingbot **commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3`**, package label **`20260920`**, directly fetched `hummingbot/VERSION=dev-2.17.0` through the connected GitHub app on 2026-10-29. Prior Alpha PR #414 documents a 902/902 shipped-Python-file wheel/source identity verification for this exact baseline; this Scout **did not rehash installed wheel bytes** or run the candidate. If the wheel-to-commit mapping is later invalidated, Gate 5 must be rejected, not silently moved to another engine.

**Actual data path:** pinned `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` lists `1h`; `binance_spot_candles.py` parses Binance REST kline opening timestamp at row[0] and actual O/H/L/C/V from rows[1..5]. All required features use this one completed series. The data provider's missing-price `get_price_by_type` fallback `Decimal("1")` is **forbidden** as a fill/mark: require finite positive actual candle close, otherwise abort.

**Actual controller and executor path:** pinned `BacktestingEngineBase.simulate_execution` iterates prepared rows, calls `update_state(row)`, then `controller.determine_executor_actions()`, and passes `CreateExecutorAction(OrderExecutorConfig(...))` to `simulate_executor`. A future minimal strategy-specific controller (not implemented here) would retain the four explicit states and queue a signal on completed bar t, dispatching on **the following actual row t+1**. Use `connector_name="binance"`, `trading_pair="BTC-USDT"`, `side=TradeType.BUY/SELL`, `amount=Decimal("0.001")`, `position_action=PositionAction.OPEN/CLOSE`, `execution_strategy=ExecutionStrategy.MARKET`, `price=None`, `leverage=1`. `OrderExecutorConfig` at this pinned commit explicitly supports these fields. Do not treat the mere existence of these API names as proof: the inspected `OrderExecutorSimulator.simulate` MARKET branch fills at the **first supplied row's actual close**, sets quote fill `amount*close`, fee `trade_cost*amount_quote`, and terminates as `CloseType.POSITION_HOLD`. This is the precise model selected here; no LIMIT, maker queue, next-open or intrabar trigger is required.

**Timestamp and fill limitation:** signal `UP/DOWN` or Aroon loss is available only at E[t]. Historical simulated BUY/SELL uses actual C[t+1] at effective time E[t+1], **not** the raw `T[t+1]` open-time label, and does not promise an executable real-world post-close order at that same historical close. No future t+1 close enters the t decision. Suppress decision on fill row. The pinned simulator is an idealized historical close-fill model, not a TradingView broker-emulator or live fill-equivalence claim.

**Accounting and fees:** initial **10,000 USDT** unlevered spot cash, inventory 0 BTC, fixed `Q=Decimal("0.001")` BTC per entry. Explicitly call pinned backtest with `trade_cost=0.001`, **hypothetical 0.1% per filled side**, not verified historical Binance fees. Confirmed BUY at real `Pbuy` debits `Q*Pbuy*(1+0.001)` USDT and credits Q BTC only if cash suffices; confirmed SELL debits Q BTC and credits `Q*Psell*(1-0.001)`. Matched net PnL is `Q*(Psell-Pbuy)-0.001*Q*(Pbuy+Psell)`. Engine `BacktestPositionHold` nets opposite `POSITION_HOLD` fills and records gross realized PnL and fees separately; it derives base amount from float-derived quote/price and can leave dust. Use confirmed executor fills and a Decimal cash/BTC ledger as inventory authority; reconcile all terminated executors, fill notional, fee and position with tolerances at most `1e-9 BTC` and `1e-8 USDT` (diagnostics only; never hide a missing or partial fill). Require complete ledger, e.g. `terminated_executors_window=None` or equivalent; fail closed on material mismatch. Mark any terminal open position to the **last real** close as unrealized, not a fabricated SELL. The simulator models no additional spread/impact/latency slippage: **not** a claim of zero realized slippage. Binance fee tier, live tick/lot/min-notional/partial-fill acceptance are unverified; spot has no perpetual funding liability, and no futures funding observation is invented. No margin or liquidation model is needed.

## Six-gate Scout assessment (independent audit pending)

1. **Determinism:** exact Aroon14 15-bar latest-tie construction, raw-delta CMO14, SMA9, strict UP/DOWN and histogram comparisons, priority, full state and abort rules; no hidden parameters or fitted model.
2. **Direction:** one Binance BTC-USDT spot LONG/FLAT position; no short or futures permission assumed.
3. **Entries/exits/risk:** Aroon-positive gated CMO UP BUY; CMO DOWN or Aroon nonpositive full SELL; stop, TP, trailing, time and other risk behaviors explicitly disabled. Source is an indicator, and all executable rules are disclosed as derived.
4. **Position and DCA:** 0.001 BTC, 10,000 USDT, one full-fill pending action/position, no add/hedge/DCA/safety order, no same-fill-bar decision; re-entry requires a fresh UP.
5. **Pinned engine compatibility:** actual Binance spot 1h OHLCV REST parser, controller action iteration, OrderExecutor MARKET first-row close fill, POSITION_HOLD netting, modeled fee path, Decimal reconciliation, real-price-only guard and no unsupported multi-asset/short/futures/next-open/intrabar assumptions. Package/source evidence is inherited and explicitly bounded.
6. **Point-in-time causality:** 100 completed bars, t-1/t completed indicators, no future extrema or repaint, t decision at E[t], following real t+1 close model fill at E[t+1], strict data-contiguity and pending-state suppression.

## Negative evidence, limitations and later validation

The source does **not** publish complete decision-critical original Pine/order rules in accessible prose; this is an independently specified derivative, not a source-native reproduction. Original script's exact indicator lengths, smoothing, alert configuration, trade mapping and performance are unknown; none is silently asserted. No candidate Hummingbot or Qlib backtest, no event-level parity, OOS, Survivor certification, PnL, Paper/Testnet/Live, or controller implementation was performed. Hypothetical modeled costs and historical close fills do not establish exchange economics.

Later **authorized** falsification should cover tied Aroon extrema, 15-bar window edge, CMO zero-denominator abort, CMO/SMA equality, cross while histogram is nonpositive, histogram turn positive without new cross, crossdown versus Aroon-loss priority, warmup boundary, signal during pending/fill bar, first eligible re-entry, missing candles/price fallback, failed/partial fill, terminal pending order, fee and inventory float dust, and last-close unrealized valuation. Reuse only verified Hummingbot/Qlib execution primitives; before any large-scale Qlib screening requiring a new primitive, first validate representative event-level parity. This is not a new HB_READY gate or a profitability claim.

## Adoption boundary and sources

`hb_ready_status: PASS` is **Scout's six-gate research proposal**, not an independent Hermes Auditor PASS verdict. `status: research-only`, `implementation_status: not-implemented`, `adoption: not-approved`, `approval_scope: research-only`. Only independent Hermes Auditor GitHub Webhook Review may remediate primary-source facts, merge an exact-head PASS or close NOT_LOSSLESS; only the existing signed webhook receiver reconciles the main README after a confirmed merge. This Scout adds no implementation, test, container, trade, cron, README or other file.

- Primary TradingView source: https://www.tradingview.com/script/hqJGWNKa-Aroon-Histogram-CMO-ChuckBanger/ (ChuckBanger, 2019-10-22; public page accessed 2026-10-29).
- Pinned engine source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 (VERSION, Binance Spot candles/constants, backtesting engine/data provider, OrderExecutorConfig/Simulator).
- Prior wheel/source identity evidence: https://github.com/HCH725/alpha-strategy-research/pull/414 .
