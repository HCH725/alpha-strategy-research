---
schema: strategy-research-record-v1
title: Bitcoin Implied Jump Risk Premia as Predictor of Futures Carry and Delta-Hedged Option Performance
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - options
  - bitcoin
  - jump-risk
  - hawkes-process
  - implied-volatility
  - carry
  - relative-value
  - deribit
status: research-only
confidence: medium
source_as_of: 2025-10-24
sources:
  - https://arxiv.org/abs/2510.21297
  - https://arxiv.org/pdf/2510.21297
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Implied Jump Risk Premia as Predictor of Futures Carry and Delta-Hedged Option Performance

## Provenance

- **Paper:** Liu, F., Packham, N., & Sepp, A. (2025). "Jump risk premia in the presence of clustered jumps." arXiv:2510.21297 [q-fin.MF].
- **Submitted:** 24 October 2025.
- **Authors:** Francis Liu (Berlin School of Economics and Law / Humboldt-Universität zu Berlin), Natalie Packham (Berlin School of Economics and Law), Artur Sepp (LGT Bank Schweiz).
- **Data period:** April 2019 – May 2024 (BTC options and price data from Deribit and public sources).
- **Asset class:** Bitcoin (BTC) options on Deribit; BTC perpetual and fixed-maturity futures.

## Economic mechanism

### Source-reported

The authors develop a derivatives pricing model incorporating a bivariate Hawkes process that captures clustered positive and negative jumps in BTC returns. They introduce two additional parameters — positive and negative jump risk premia — defined as the difference between expected jump magnitudes under the risk-neutral (Q) and statistical (P) measures. These premia are inferred from jointly calibrating the model to BTC price dynamics and the implied volatility surface.

Key source-reported findings:
- Both positive and negative jump risk premia are observed in the May 2019 – October 2023 period, with frequent periods where implied jump risk exceeds realised jump risk (consistent with variance risk premium literature).
- Inferred jump risk premia exhibit predictive power for the cost of carry in one-month BTC futures on Deribit.
- Inferred jump risk premia exhibit predictive power for the performance of delta-hedged option strategies.
- BTC options exhibit a positive call skew on average (contradicting equity patterns), reflecting demand for lottery-like upside payoffs.
- The model accommodates sign-reversing implied volatility skew, where investors shift between put protection (negative skew) and call speculation (positive skew).

### Research interpretation

This is a **relative-value / carry alpha** hypothesis grounded in options-implied expectations vs. realised dynamics:

- **Signal mechanism:** When implied jump risk premia are elevated (market prices in excessive jump risk relative to realised jumps), options are overpriced relative to the realised jump distribution. Conversely, when implied jump risk premia are compressed or negative, options may be underpriced.
- **Carry connection:** The jump risk premia capture forward-looking risk preferences beyond standard funding costs. Elevated positive jump risk premia (call option demand) may predict higher futures basis/carry as bullish positioning intensifies. Elevated negative jump risk premia (put demand) may predict compressed or negative carry.
- **Delta-hedged options:** Systematically selling options when implied jump risk premia are elevated (options overpriced relative to realised) and delta-hedging should harvest the premia. The Hawkes process clustering structure means jumps arrive in clusters, so timing the premia relative to the jump cycle is important.
- **Distinction from existing records:** This is NOT about realised jump signals (momentum, reversal, signed jumps). It is about the *implied-to-realised* gap in jump risk, which is a forward-looking options pricing inefficiency signal.

## Signal

### Signal formation
- **Lookback:** Model calibration uses rolling historical BTC returns and options implied volatility surfaces (joint P-Q calibration).
- **Inputs:** (a) BTC daily returns (P-dynamics), (b) BTC ATM implied volatilities, (c) BTC 25-delta call and put skews, (d) options chain prices across strikes and maturities.
- **Model parameters:** Bivariate Hawkes process with positive/negative jump intensities (λ+, λ−), baseline rates (θ+, θ−), decay rates (κ+, κ−), and jump size distributions (ϖ+, ϖ−). Plus positive/negative jump risk premia (difference in expected jump magnitude between Q and P measures).

### Trading rules (source-reported, underspecified)
- **Carry prediction:** When positive jump risk premia are elevated → expect higher futures basis/carry; when negative jump risk premia are elevated → expect compressed/negative carry. Directional futures position sized accordingly.
- **Delta-hedged options:** When implied jump risk premia are high (options overpriced) → sell options (straddle/strangle), delta-hedge. When low → buy options or reduce position.
- **Exact entry/exit thresholds:** Underspecified in the paper. The relationship is demonstrated statistically but specific trading rules with explicit thresholds are not provided.

### Parameters
- Calibration window: Rolling (exact window not specified in the paper).
- Holding period: Aligned with one-month futures/options maturity.
- Position sizing: Not specified.

## Required data

- **Instrument:** BTC options on Deribit (all strikes, all expiries).
- **Underlying:** BTC perpetual futures (for funding / basis reference) and BTC spot.
- **Market type:** Options (European-style, cash-settled, inverse), perpetual futures, fixed-maturity futures.
- **Data fields:**
  - BTC daily returns (for P-dynamics estimation).
  - Full options chain: bid/ask or trade prices across strikes and maturities (for Q-dynamics calibration).
  - ATM implied volatility time series.
  - 25-delta call and put implied volatilities (for skew computation).
  - Futures basis / cost of carry (one-month fixed-maturity futures on Deribit).
  - Funding rates (perpetual futures).
- **Timeframe:** Daily calibration (model is calibrated to daily frequency data).
- **Availability:** Deribit public options data; BTC price data from public sources.
- **Missing data assumptions:** The paper uses trade-quality options data from Deribit. Real-time full-chain data may have gaps or stale quotes.

## Execution assumptions

- **Signal-to-order timing:** Model recalibrated periodically (frequency not specified); signals derived from calibration output.
- **Execution:** Options positions executed on Deribit via market or limit orders; delta hedging via perpetual or spot.
- **Fees:** Deribit options taker fees (~0.04% notional); perpetual futures trading fees.
- **Slippage:** Not modelled in the paper.
- **Spread:** Not modelled; assumes mid-price execution.
- **Leverage:** Not specified; options are inherently leveraged.
- **Latency:** Not relevant for daily-frequency signals.
- **Partial fills:** Not addressed.

## Evidence

### Source-reported
- Model calibrated to 30+ monthly cross-sections of BTC options surfaces (May 2019 – October 2023).
- Both positive and negative jump risk premia are frequently observed; implied jump risk often exceeds realised jump risk.
- Statistical relationship between inferred jump risk premia and one-month futures carry is demonstrated (correlation analysis).
- Statistical relationship between jump risk premia and delta-hedged option strategy returns is demonstrated.
- The paper includes Q-Q plots showing good model fit to observed inter-jump arrival times.
- No Sharpe ratio, CAGR, or specific backtest performance figures for a systematic trading strategy are reported.

### Independently reproduced
Not independently reproduced.

### Negative evidence
- The paper notes that "both positive and negative risk premia are observed, with frequent periods where the implied jump risk is higher than the realised jump risk" — this is consistent with options being generally overpriced (negative VRP), but the signal is not uniformly exploitable.
- The relationship between jump risk premia and carry is statistical, not deterministic. The paper does not demonstrate a robust trading strategy with explicit entry/exit rules and transaction costs.
- BTC options market liquidity varies significantly; wings may have wide spreads that erode alpha.

## Falsification plan

- **Required sample:** Replicate the joint P-Q calibration on out-of-sample BTC options data (2024–2026).
- **Baseline:** Compare against a naive carry strategy (always short perp / long spot) and a volatility risk premium strategy (always sell straddles, delta-hedge).
- **Ablation:** Test whether jump risk premia add predictive power beyond ATM implied volatility level alone, beyond skew alone, and beyond realised jump intensity alone.
- **Cost sensitivity:** Model Deribit taker fees, bid-ask spread on options, and perpetual funding costs. Determine minimum jump risk premium level needed to cover costs.
- **Failure metric:** If jump risk premia do not Granger-cause futures carry or delta-hedged returns out-of-sample, the hypothesis fails.
- **Action on failure:** Abandon the jump risk premia signal; retain Hawkes process calibration as a descriptive tool for jump clustering.

## Crypto portability

direct

The paper is natively crypto-focused (BTC options on Deribit). No portability concerns. However:
- The Deribit BTC options market is relatively young (2019+); the sample period covers only ~5 years.
- BTC options liquidity is concentrated in short-dated ATM strikes; wings and longer maturities may have insufficient data for reliable Hawkes calibration.
- The model assumes continuous trading and liquid options markets, which may not hold during extreme events.

## Limitations

- **underspecified** — The paper demonstrates statistical relationships but does not provide explicit, reproducible trading rules with entry/exit thresholds, position sizing, or transaction cost accounting.
- **not independently reproduced** — The Hawkes process calibration is computationally intensive and requires access to full Deribit options chain data.
- **data gap** — The paper uses historical data up to May 2024; the BTC options market has evolved significantly since then (ETF approval, institutional participation).
- **sample size** — 30+ monthly calibration points is limited for statistical inference on carry prediction.
- **model risk** — The bivariate Hawkes process is a parametric model; misspecification of jump size distributions or Hawkes dynamics could produce spurious premia estimates.
- **liquidity assumption** — Assumes Deribit options are sufficiently liquid for execution at model-implied prices.

## Implementation status

not-implemented

## Adoption boundary

This record represents research material only. It does not mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

## Related Wiki records

- [[crypto-deribit-options-volatility-of-volatility-vov-realized-quarticity-2026-09-01]] — Related options-based risk premium harvesting, but uses realised quarticity rather than Hawkes jump risk premia.
- [[crypto-cross-sectional-realized-signed-jump-good-bad-volatility-2026-09-01]] — Related to jump dynamics in crypto, but uses realised (not implied) jump decomposition.

## Sources

1. Liu, F., Packham, N., & Sepp, A. (2025). "Jump risk premia in the presence of clustered jumps." arXiv:2510.21297 [q-fin.MF]. https://arxiv.org/abs/2510.21297
2. Data period: April 2019 – May 2024. BTC options on Deribit; BTC price data from public sources.
