---
schema: strategy-research-record-v1
title: "Adaptive Anchored VWAP Reclaim with Online Logistic Follow-Through Filter — TradingView Source-Code Audit"
created: 2026-09-14
updated: 2026-09-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
  - crypto
  - anchored-vwap
  - online-learning
status: research-only
confidence: medium
source_as_of: 2026-09-14
sources:
  - "https://www.tradingview.com/script/fRCrxRLG/"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The TradingView description says learning resets on anchor/timeframe/parameter change, but the reviewed Pine source resets VWAP accumulators and anchorBar on re-anchor without resetting the online-logistic weights, setup queue, conformal-calibration array, or containment counters."
  - "The page describes bar-close training and no-repaint behavior, but the reviewed Pine source gates training/setup creation with barstate.isconfirmed while the displayed reclaimLong/reclaimShort signal booleans and alertcondition calls themselves are not confirmed-bar-gated; realtime signal stability therefore depends on evaluation and alert-frequency semantics."
---

# Adaptive Anchored VWAP Reclaim with Online Logistic Follow-Through Filter — TradingView Source-Code Audit

## Provenance

- **Primary source:** AetherEdge, `AetherEdge - Adaptive Anchored VWAP`, public TradingView open-source Pine Script v6 indicator.
- **Stable public URL:** https://www.tradingview.com/script/fRCrxRLG/
- **Publication timestamp shown by TradingView metadata:** 2026-06-18 17:33 UTC; the page can display `Jun 19` under local-time rendering.
- **Primary-source inspection:** the public description and the complete 280-line Pine source visible in TradingView's `Source code` tab were read directly on 2026-09-14. This record normalizes the implementation and does not reproduce the Pine source wholesale.
- **Repository/Wiki deduplication:** no existing record was found for TradingView script ID `fRCrxRLG`, this anchored-VWAP reclaim construction, or an online logistic classifier trained on the source's VWAP-reclaim follow-through label. Existing conformal-prediction, triple-barrier, and machine-learning records use materially different mechanisms, labels, or strategy families.
- **Incremental value:** the signal combines a causal confirmed-pivot re-anchored volume-weighted cost basis with rolling empirical band calibration and an online classifier that filters reclaim events. Direct source inspection also exposes material reset and realtime-confirmation caveats that are not captured by generic VWAP or machine-learning records.

## Economic mechanism

### Source-reported

The author presents anchored VWAP as a volume-weighted cost basis from an event. A reclaim or loss of that cost basis is treated as potentially informative only when a continuously learned model assigns sufficient probability to follow-through. The author also uses empirically calibrated volume-weighted deviation bands to avoid assuming normally distributed deviations around VWAP and recommends the tool for liquid crypto and futures markets.

### Research interpretation

The falsifiable hypothesis has three separable components:

1. **Reference-state component:** a recently confirmed swing, daily boundary, or manual event defines a market-participant cost-basis anchor. Crossing the resulting anchored VWAP may represent a change in control rather than an arbitrary price-level crossover.
2. **Conditional continuation component:** not every VWAP reclaim should continue. Recent directional momentum, trend alignment, RSI state, relative VWAP dispersion, relative volume, and anchor age may condition the probability that price continues in the reclaim direction before losing the VWAP again.
3. **Distribution-state component:** a rolling empirical quantile of standardized VWAP deviations can adapt the visual containment bands to fat-tailed price distributions. This component is descriptive/contextual in the current Pine source; it is not itself part of the reclaim entry gate.

The predictive claim therefore belongs to the **reclaim event plus online follow-through filter**, not to the conformal-style band alone. Each component requires ablation because the current source provides no evidence that all components contribute incremental alpha.

## Signal

**Specification status: partially reconstructable as an indicator event signal; trading strategy execution is underspecified.** The reclaim filter can be reconstructed from the reviewed source, but the source is `indicator()`, not `strategy()`, and does not define an executable position lifecycle.

### Source-reported / source-code-defined state

- **Chart source:** default `hlc3`; alternatives `close` and `ohlc4`.
- **ATR:** `ATR(14)` with a small numerical floor.
- **Trend features:** EMA fast `10`, EMA slow `30`.
- **RSI:** length `14`.
- **Default anchor mode:** `Auto (pivots)`.
- **Pivot strength:** `20` bars on both left and right sides.
- **Alternative anchors:** daily session boundary or manual timestamp.
- **VWAP:** cumulative `sum(source × volume) / sum(volume)` from the active anchor, with a volume-weighted second moment used to derive `vwSig`.
- **Fixed band width input:** `2.0 sigma`; adaptive calibration is enabled by default.
- **Adaptive band target:** outside fraction `0.10`, i.e. approximately 90% empirical containment.
- **Calibration window:** trailing `250` confirmed-bar standardized deviations `abs(source - VWAP) / vwSig`.
- **Label follow-through threshold:** `1.5 × ATR` measured from the reclaim close using the ATR stored at setup creation.
- **Label horizon:** `15` bars.
- **Online learning rate:** `0.03`.
- **Minimum displayed-signal probability:** `0.55`.
- **Warm-up gate:** `bar_index > 150`.

### Causal anchor timing

With auto anchoring, `ta.pivothigh(high, 20, 20)` / `ta.pivotlow(low, 20, 20)` becomes known only after the 20 right-side bars exist. The current source resets VWAP accumulators and sets `anchorBar = bar_index` on that **confirmation bar**. It does not retrospectively begin the VWAP on the historical pivot candle. A reproduction that anchors on the pivot timestamp at signal time would introduce look-ahead relative to the reviewed implementation.

### Online classifier features

For a reclaim side `s = +1` for upward reclaim and `s = -1` for downward loss, the source creates six features at the reclaim event:

1. side-oriented three-bar close momentum normalized by ATR and clipped to `[-3, 3]`;
2. side-oriented EMA(10)-EMA(30) spread normalized by ATR and clipped to `[-3, 3]`;
3. side-oriented centered RSI(14), scaled by 50 and clipped to `[-1, 1]`;
4. current volume-weighted VWAP dispersion relative to its 50-bar simple average, minus one, clipped to `[-1, 3]`;
5. current volume relative to its 20-bar simple average, minus one, clipped to `[-1, 3]`;
6. anchor age divided by 50, clipped to `[0, 3]`.

A seven-weight logistic model (intercept plus six coefficients), initialized at zero, produces `pFollow`. Each resolved historical setup updates the weights by one online gradient step using the fixed learning rate.

The source also computes an ATR-percentile volatility regime from `ATR(14)` percent rank over 100 bars (`<33`, `33-66`, `>=66`) for display. In the reviewed code that discrete regime variable is not part of the reclaim signal gate or logistic feature vector.

### Reclaim event and training label

- **Upward reclaim:** `close` crosses above current anchored VWAP.
- **Downward reclaim:** `close` crosses below current anchored VWAP.
- On a confirmed bar containing a reclaim, the source stores the six features, reclaim-side close, current ATR, and age zero as a training setup.
- On later confirmed bars, setup age increments. A long-side setup is labeled success if the current **close** reaches at least `entry + 1.5 × stored ATR`; a short-side setup is success if close reaches at least `entry - 1.5 × stored ATR`.
- A setup is labeled failure if price closes back across VWAP against the reclaim direction before success, or if age reaches `15` bars without success.
- Success takes precedence in the source's resolution order over same-bar recross and horizon checks.
- The online model is trained only when a setup resolves.
- At most 60 unresolved setups are retained; if the queue grows beyond 60, the oldest is dropped.

### Displayed signal

After the warm-up bar count, the indicator marks a reclaim long/short when the relevant close/VWAP crossover occurs and current model probability is at least `0.55`.

**Realtime timing caveat:** training and setup creation explicitly require `barstate.isconfirmed`, but `reclaimLong` / `reclaimShort` and their `alertcondition` expressions do not. Therefore a historical close-based reconstruction is clear, while intrabar/realtime signal availability is **underspecified/contested** unless alert frequency and bar-close use are frozen.

### Holding / exit / re-entry

The 15-bar triple-barrier-like horizon belongs to the **training label**, not to a source-defined trading position. The source does not specify order entry, position holding, stop, take-profit order, position sizing, pyramiding, overlapping-position treatment, or executable exit logic. Those fields are **underspecified** and must not be inferred from the label mechanics.

### Research-proposed operationalization for later validation

For a leakage-safe event study, use only completed bars, record the filtered reclaim event after the signal bar closes, and evaluate outcomes from the next executable bar onward. Any conversion of the training label into actual orders, including next-bar market entry or barrier exits, is **research-proposed**, not source-reported.

## Required data

- **Instrument/universe:** source is symbol-agnostic; author recommends liquid symbols and specifically mentions major crypto and futures. No fixed universe or listing/liquidity threshold is supplied.
- **Venue:** TradingView chart feed; no exchange-selection rule is supplied.
- **Market type:** indicator is generic. For crypto validation, spot and perpetual futures must be tested separately because source logic does not model funding or contract mechanics.
- **Timeframe:** author recommends crypto `15m–4H`; no single source-validated optimal timeframe is established.
- **Fields:** OHLCV sufficient for the current source; volume is required for both VWAP and one classifier feature.
- **Point-in-time requirements:** pivot-based anchoring must respect the 20-right-bar confirmation delay. No historical pivot may be made available before confirmation.
- **Timestamp/session:** exact exchange timezone and TradingView candle/session boundaries must be frozen. Daily-session anchor semantics especially depend on `time("D")` for the chart symbol.
- **Missing data:** not specified. A reproduction must not silently forward-fill missing OHLCV or volume.
- **Data quality:** source recommends reliable volume. Cross-venue differences in crypto reported volume can materially alter VWAP, dispersion, and volume-ratio features.

## Execution assumptions

The TradingView source is an indicator and supplies no broker-emulator execution model.

**Source omissions:** order type, fill model, signal-to-order delay, spread, maker/taker fee, slippage, market impact, participation cap, partial fills, leverage, margin, liquidation, funding, borrow, latency, venue failure, and position limits are not specified.

For later economic validation, any executable mapping must be explicitly **research-proposed**. A conservative default would observe only a completed-bar signal and allow the earliest order on the next bar; this is not part of the TradingView source.

The source's target/failure labels are based on bar **closes**, not intrabar high/low touches. A replication that uses intrabar barrier touches would change the training target and is not source parity.

## Evidence

### Source-reported

The public TradingView page and source document the anchored VWAP, volume-weighted dispersion bands, rolling empirical calibration, online logistic model, six feature families, reclaim event logic, `1.5 × ATR` / `15`-bar follow-through target, `0.55` probability threshold, and recommended use on liquid crypto/futures. The author states that training is bar-close based, characterizes the model as a linear classifier rather than deep learning or reinforcement learning, and warns that auto anchoring lags by pivot confirmation.

The reviewed source provides **no Sharpe ratio, CAGR, win rate, drawdown, profit factor, transaction-cost result, capacity estimate, independent out-of-sample result, or strategy-level return series**. No profitability claim is treated as evidence here.

### Independently reproduced

not independently reproduced

### Negative evidence

1. **Anchor-reset documentation contradiction:** the page says learning resets on anchor/timeframe/parameter change. In the reviewed current Pine source, a re-anchor resets cumulative VWAP state and `anchorBar`, but the online-logistic weights, unresolved-setup array, conformal-calibration array, and containment counters persist. A timeframe or input recompilation may reset script state, but an in-script auto re-anchor does not reset those learning objects.
2. **Realtime confirmation caveat:** model training and setup creation are gated by `barstate.isconfirmed`, but the displayed signal booleans and alert conditions are not. Historical plotted signals can therefore be interpreted at settled bar close, but the stronger blanket inference that realtime reclaim alerts cannot flicker intrabar is not established by the reviewed signal expressions.
3. **No economic backtest evidence:** this is an indicator; there is no source-defined executable lifecycle, cost model, or performance study demonstrating that the probability filter improves net returns.
4. **Online non-stationarity risk:** logistic weights persist across anchor changes in the current source, mixing training examples generated under different anchored states. Whether that improves adaptation or contaminates the conditional distribution is untested.
5. **Warm-up is bar-count based, not resolved-sample based:** after 150 bars the model may still have very few resolved training examples. With zero-initialized weights the initial probability is 0.5, below the 0.55 display threshold, so useful calibration depends on the realized sequence of resolved setups rather than the warm-up count alone.
6. **Calibration sample also spans re-anchors:** the 250-observation standardized-deviation array is not cleared on re-anchor in the reviewed source, so the adaptive band mixes deviations from multiple anchor regimes.
7. **Publication/selection bias:** a public TradingView script and its explanatory narrative are not controlled out-of-sample evidence.

## Falsification plan

1. **Source-parity and point-in-time audit.** Data: exact TradingView OHLCV for selected BTC/ETH symbols and timeframe, plus a line-for-line normalized reproduction of the reviewed source. Compare every re-anchor, VWAP value, training setup, resolved label, probability, and final signal. **research-defined falsification threshold:** any systematic use of the historical pivot timestamp before the 20-bar confirmation point, or any material signal mismatch not attributable to documented platform precision, invalidates the reproduction; fix parity before testing alpha.

2. **Classifier discrimination test.** Data: chronologically split BTCUSDT and ETHUSDT spot/perpetual samples across at least two venues where comparable OHLCV is available; no retraining on evaluation observations beyond the source's causal online updates. Metrics: OOS AUC, Brier score, and log loss for the source-defined 1.5-ATR/15-bar reclaim outcome. Baseline: unconditional expanding success probability and unfiltered reclaim events. **research-defined falsification threshold:** if OOS AUC is `<= 0.52` and Brier score does not improve over the unconditional baseline on both BTC and ETH, reject the claim that the six-feature online classifier adds useful discrimination.

3. **Probability-gate ablation.** Compare all source-parity VWAP reclaims against the subset passing `pFollow >= 0.55`; preserve identical timestamps and label semantics. Metrics: source-label success rate, next-bar executable forward return, and net expectancy after costs. **research-defined falsification threshold:** if the filtered set improves success rate by less than 2 percentage points and does not improve net expectancy on a majority of the prespecified symbol/timeframe panels, reject the probability gate's incremental-value hypothesis.

4. **Reset-policy contradiction test.** Run two causal variants: (A) current-source persistent weights/calibration across re-anchor; (B) reset weights/setup/calibration on each anchor as the page wording suggests. Keep all other settings fixed. Metrics: calibration, signal count, and executable expectancy. **research-defined falsification threshold:** if the two variants materially diverge, treat the documentation as non-equivalent implementations and do not pool their results; only the source-parity persistent-state variant may be called a reproduction of the current Pine source.

5. **Parameter robustness.** Prespecify a neighborhood before evaluation: pivot strength `{10,20,30}`, target ATR `{1.0,1.5,2.0}`, horizon `{10,15,20}`, probability threshold `{0.50,0.55,0.60,0.65}`. Use walk-forward evaluation without choosing the best OOS cell afterward. **research-defined falsification threshold:** if positive net expectancy exists only at the exact published default while a majority of nearby parameter cells are non-positive, reject robustness and classify the effect as parameter-fragile.

6. **Cost / execution stress.** Research-proposed executable mapping: signal accepted at completed-bar close, entry no earlier than next bar, with identical exit mapping across all variants. Stress round-trip fees+spread+slippage at 5, 10, and 20 bps plus observed perpetual funding where applicable. **research-defined falsification threshold:** if median net expectancy across BTC/ETH liquid panels is `<= 0` at 10 bps round-trip before funding, reject practical tradability under ordinary liquid-crypto taker-style execution.

7. **Realtime stability audit.** Replay lower-frequency bars from sub-bars or tick-capable data, computing the source signal intrabar and again at bar close. Metric: fraction of provisional intrabar alerts that disappear by the completed bar. **research-defined falsification threshold:** if more than 5% of provisional reclaim alerts disappear by close, reject any unrestricted realtime `no-repaint` interpretation and require bar-close-only signal handling. If the economic edge then disappears under next-bar execution, reject the tradable-alpha interpretation.

8. **Cross-venue / regime test.** Evaluate BTC and ETH on at least two independent venue feeds, separating high/low realized-volatility regimes and spot versus perpetual futures. **research-defined falsification threshold:** if the filtered reclaim effect is positive on only one venue feed or one narrow volatility regime and non-positive elsewhere after costs, classify portability as unproven and reject a general crypto-alpha claim.

On failure of the predictive, robustness, or cost gates above, retain the record as negative/falsification evidence rather than retuning thresholds after observing OOS results.

## Crypto portability

**adapted / unproven.** The author explicitly recommends major crypto among liquid instruments, so the source is not purely a traditional-asset port. However, the source supplies no crypto-specific performance evidence and no fixed venue/instrument contract.

Material crypto risks:

- 24/7 session boundaries alter the daily-anchor interpretation across exchanges/timezones;
- spot and perpetual volume can encode different participant populations;
- perpetual funding and liquidation mechanics are absent from the signal and cost model;
- exchange fragmentation can change VWAP and volume-ratio features materially;
- quote currency/stablecoin choice can alter observed volume and microstructure;
- cross-venue candle boundaries and data outages can change pivot confirmation and online training order;
- high-turnover lower-timeframe reclaims may be highly fee/spread sensitive.

Crypto portability is a research hypothesis only, not authorization to trade.

## Limitations

- `underspecified`: no source-defined executable entry fill, exit, sizing, overlap, or risk-management lifecycle.
- `not independently reproduced`.
- No source-reported performance statistics or independent OOS evidence.
- Current-source learning-state persistence conflicts with the page statement that learning resets on anchor changes.
- Realtime signal confirmation semantics are not fully frozen by the signal expressions themselves.
- TradingView script state, alert frequency, feed, timezone, and timeframe settings can alter practical behavior.
- Online logistic learning has no regularization, forgetting factor, class weighting, or explicit calibration correction in the reviewed source.
- The rolling empirical band is descriptive context in current signal logic; it should not be assumed to add alpha without ablation.
- Pivot confirmation creates a deliberate 20-right-bar delay under default auto mode.
- The source is a recent community publication with limited public usage history, not peer-reviewed research.

## Implementation status

`not-implemented`. No implementation of this candidate has been added to the quantitative research runtime, and no backtest, paper trading, testnet, or live verification was performed in this Scout cycle. The only artifact is this normalized research record in the staging repository.

## Adoption boundary

This record is `research-only`, `not-implemented`, `not-approved`, with `approval_scope: research-only`.

Presence in `alpha-strategy-research` does not establish profitable alpha, independent validation, implementation approval, or permission for Paper/Testnet/Live trading. Any later implementation or adoption requires a separate reviewed decision and independent historical validation.

## Related Wiki records

No exact Hermes Wiki Brain record matching TradingView source `fRCrxRLG` or the same anchored-VWAP reclaim plus online-logistic follow-through construction was identified in the pre-write search.

Materially adjacent Wiki research includes `quant/conformal-kelly-prediction-intervals-fractional-sizing-2026-09-02.md`, but that record studies conformal uncertainty as a position-sizing scale and is not evidence for this VWAP reclaim signal. Triple-barrier and machine-learning records also exist but use different labels, data, and mechanisms.

## Sources

1. AetherEdge, **AetherEdge - Adaptive Anchored VWAP**, TradingView public open-source Pine Script v6 indicator, publication metadata 2026-06-18 17:33 UTC; public description and complete current 280-line source inspected directly on 2026-09-14: https://www.tradingview.com/script/fRCrxRLG/
