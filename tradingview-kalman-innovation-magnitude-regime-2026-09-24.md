---
schema: strategy-research-record-v1
title: TradingView Kalman innovation-magnitude regime filter
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-24
sources:
  - https://www.tradingview.com/script/I2GxphFw-Kalman-Trend-Estimator-KTE-FibonacciFlux/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Kalman innovation-magnitude regime filter

## Provenance

- Public TradingView open-source script: **Kalman Trend Estimator [KTE] -FibonacciFlux**.
- Author/page identity: **FibonacciFlux**.
- Stable TradingView URL: https://www.tradingview.com/script/I2GxphFw-Kalman-Trend-Estimator-KTE-FibonacciFlux/
- TradingView page displays publication label **Apr 7**; the fetched public page does not display a year next to that label, so no year is inferred here.
- Source reviewed as of **2026-09-24**.
- The public description was normalized rather than copying Pine source code.

## Economic mechanism

### Source-reported

The author models observed price as a noisy measurement of a hidden trend state and applies a scalar Kalman filter. Process noise `Q` controls how quickly the latent state can change; measurement noise `R` controls smoothing. The author states that the Kalman gain adapts each bar and describes the filter innovation (prediction error) magnitude as a regime classifier: small innovations correspond to cleaner/trending conditions, while large innovations correspond to noisy/ranging conditions. The page also describes confidence bands from estimation uncertainty and signal dots at trend-direction changes.

### Research interpretation

The falsifiable hypothesis is not that a Kalman estimate is intrinsically profitable. It is that **the magnitude of one-step Kalman forecast errors contains incremental information about whether a simple directional rule is operating in a persistent versus noisy regime**. If innovation magnitude is only a repackaging of realized volatility, absolute returns, ATR, or distance from a smoother, the Kalman regime layer should be rejected.

A practical trading mapping is not fully specified by the source. Any use of innovation magnitude to gate a momentum, breakout, or trend-following rule is therefore **research-proposed**, not source-reported.

## Signal

### Source-reported construction

- Input: price; the public description does not identify a specific OHLC source field.
- State estimator: scalar Kalman filter estimating a hidden trend state.
- Process noise parameter: `Q`, default **0.01**.
- Measurement noise parameter: `R`, default **1.0**.
- Kalman gain updates every bar.
- Regime variable: magnitude of the Kalman innovation / prediction error.
- Interpretation: smaller innovation magnitude = trending/cleaner regime; larger innovation magnitude = noisy/ranging regime.
- Confidence bands use estimation uncertainty (`P` matrix).
- Signal dots are shown at trend-direction changes.
- The source says the indicator works across timeframes and instruments.

### Underspecified by the public description

The public description does **not** unambiguously specify the exact state/update equations as implemented, initialization, price field, innovation normalization, regime threshold, threshold lookback, direction-change rule, entry, short entry, exit, holding period, re-entry, position sizing, or order timing. Those fields must not be invented from the description.

### Research-proposed operationalization for falsification only

A future test may compute a strictly one-sided Kalman estimate using only information available through bar `t`, derive an innovation-magnitude feature at `t`, and compare simple directional baselines when the feature is low versus high. Thresholds should be frozen from training data or defined by trailing point-in-time ranks; this is **research-proposed** and is not attributed to FibonacciFlux.

## Required data

- Minimum: timestamped price bars sufficient to construct the chosen point-in-time price input.
- Instrument / universe: source says all instruments; no specific market or venue is prescribed.
- Timeframe: source says all timeframes; no preferred timeframe is prescribed.
- For crypto research: spot or perpetual OHLCV may be tested, but the source does not require volume, funding, open interest, order book, trades, or options data.
- Point-in-time requirement: state, covariance, innovation, and any trailing threshold must use only data available at signal formation time.
- Missing-data and session-boundary handling are not specified by the source.

## Execution assumptions

The source is an indicator description, not a complete executable trading strategy. It does not specify same-bar versus next-bar execution, market versus limit orders, fill model, fees, spread, slippage, impact, capacity, funding, leverage/margin, borrow/shorting, latency, or partial-fill/failure handling. Any future backtest must state these independently and must not attribute them to the source.

## Evidence

### Source-reported

The source describes the qualitative regime interpretation and default `Q = 0.01`, `R = 1.0`, but provides no traceable Sharpe, CAGR, win rate, drawdown, t-statistic, or other profitability evidence on the reviewed public page.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- No source-reported predictive or trading-performance evidence was identified on the reviewed public page.
- A large innovation can mechanically coincide with a large absolute return or volatility shock, so apparent regime information may be redundant with simpler volatility features.
- Kalman behavior depends on `Q`, `R`, initialization, and model assumptions; fixed defaults need not transport across instruments or bar sizes.
- The scalar linear-Gaussian framing can be misspecified for jumps, heavy tails, volatility clustering, and crypto microstructure.
- None identified beyond these methodological concerns in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

All thresholds and test mappings below are **research-proposed** unless explicitly source-reported above.

1. Build a leakage-safe, one-sided implementation and verify that every state update and innovation uses information available at or before the signal timestamp.
2. Compare the innovation-magnitude regime feature against simpler controls: absolute return, realized volatility, ATR, distance from an EMA, and residual magnitude from a simple exponential smoother.
3. Run an ablation ladder: directional baseline alone; baseline + simple volatility gate; baseline + Kalman innovation gate. The Kalman layer survives only if it adds stable out-of-sample information beyond the simpler controls.
4. Test parameter sensitivity around `Q` and `R` rather than selecting the best pair on the full sample. Reject the hypothesis if results require a narrow, unstable parameter island.
5. Test multiple liquid crypto assets, spot/perpetual market types where available, and several bar horizons with point-in-time universe handling. Reject broad portability claims if the effect is isolated to one instrument or timeframe.
6. Include realistic fees, spread/slippage, and perpetual funding where applicable. Reject a tradable mapping if the incremental effect does not survive costs.
7. Separate the regime claim from direction: innovation magnitude should first demonstrate regime-conditioning value; trend direction must come from an independently specified directional baseline. This prevents attributing directional alpha to a non-directional surprise measure.
8. Use untouched out-of-sample periods and report both positive and null/negative cohorts. Failure action: remove the Kalman innovation layer rather than add further filters to rescue it.

## Crypto portability

**unproven**

The source claims broad instrument/timeframe applicability but does not provide crypto-specific empirical evidence on the reviewed page. Crypto testing must account for 24/7 candle boundaries, venue fragmentation, spot-versus-perpetual price construction, mark/index versus traded price where relevant, funding for perpetual positions, and jump/heavy-tail behavior. The absence of an overnight session does not remove point-in-time alignment requirements.

## Limitations

- **underspecified:** exact implemented Kalman equations, initialization, price field, innovation normalization, regime threshold, direction-change rule, and trading lifecycle are not recoverable unambiguously from the reviewed public description.
- **not independently reproduced:** no independent implementation or backtest was run during this Scout cycle.
- **data gap:** no source-reported crypto sample, venue, execution model, costs, or predictive performance statistics are provided on the reviewed page.
- **unproven:** incremental alpha beyond simpler volatility/noise measures has not been established.

## Implementation status

`not-implemented`. This record is normalized research material only. No Qlib implementation, full backtest, survivor promotion, Paper, Testnet, or Live validation was performed.

## Adoption boundary

`research-only / not-approved`.

Presence in this repository does not mean this hypothesis passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, is profitable or validated alpha, or is approved for implementation, Paper, Testnet, or Live trading.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` — schema reference exposed by the repository README. No Wiki read or write was performed in this GitHub-only cycle.
- Repository-adjacent Kalman research exists for dynamic hedge ratios, statistical arbitrage, and latent-drift estimation, but those are materially different constructions from this single-series innovation-magnitude regime hypothesis.

## Sources

- TradingView, FibonacciFlux, **Kalman Trend Estimator [KTE] -FibonacciFlux** (public open-source script page), reviewed 2026-09-24: https://www.tradingview.com/script/I2GxphFw-Kalman-Trend-Estimator-KTE-FibonacciFlux/
