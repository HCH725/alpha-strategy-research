---
schema: strategy-research-record-v1
title: Crypto Volatility Surface Completion via Convolutional VAE for Anomaly Detection and Surface Arbitrage
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
  - ethereum
  - volatility-surface
  - vae
  - anomaly-detection
  - binance-options
status: research-only
confidence: medium
source_as_of: 2026-06-15
sources:
  - https://arxiv.org/abs/2606.16961
  - https://arxiv.org/pdf/2606.16961
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Volatility Surface Completion via Convolutional VAE for Anomaly Detection and Surface Arbitrage

## Provenance

- **Paper:** Singh, S., Reddy, A., & Chopra, M. (2026). "Beyond the Smile: A Hybrid Convolutional VAE for Crypto Volatility Surfaces." arXiv:2606.16961 [cs.LG, q-fin.CP].
- **Submitted:** 15 June 2026.
- **Authors:** Sadanand Singh, Allam Reddy, Manan Chopra (Jasper Research, USA).
- **Data period:** May – October 2023 (6,034 hourly Binance Options surfaces for BTC and ETH).
- **Asset class:** BTC and ETH options on Binance Options.

## Economic mechanism

### Source-reported

The authors build a convolutional variational autoencoder (ConvVAE) for cryptocurrency implied-volatility (IV) surfaces parameterised on a 6×7 tenor–delta grid. Combined with a quadratic smile re-fit through a deterministic per-tenor routing rule, the hybrid predictor achieves:

- 0.83 vol points RMSE at 50% random masking (vs. 7.00 for smile re-fit alone — 8× improvement).
- 1.5–1.9 vol points under structurally-correlated hole patterns (vs. 9.6–13.1 for smile re-fit), where an entire tenor of strikes is withdrawn.
- Calendar- and butterfly-arbitrage-free reconstructions at listed strikes.
- Cross-asset transfer: joint BTC+ETH training improves both markets by 9–27% over single-symbol training.
- Unsupervised anomaly signal: per-snapshot reconstruction error flags the late-October 2023 ETF-anticipation rally and the August 17, 2023 flash crash without supervision.

### Research interpretation

This is primarily an **infrastructure / methodology paper** that enables several alpha strategies:

1. **Vol surface arbitrage:** The ConvVAE learns a low-dimensional manifold of "plausible" crypto vol surfaces. Observed surfaces with high reconstruction error may contain mispriced strikes or maturities — candidates for calendar spreads, butterfly spreads, or ratio spreads that exploit deviations from the learned manifold.

2. **Anomaly detection → regime awareness:** High reconstruction error periods coincide with known dislocations (ETF anticipation, flash crashes). This error signal could serve as a regime filter: avoid or reduce position sizing during elevated error periods, or contrarian trade the dislocation.

3. **Cross-asset vol surface transfer:** The shared BTC-ETH manifold implies that vol surface information from one asset can inform pricing on the other — potential for lead-lag or cross-asset vol surface relative-value trades.

4. **Operational robustness:** The paper addresses a practical problem (sparse/stale options chains) that directly affects any options-based strategy. The hybrid approach (smile re-fit when enough data, ConvVAE when data is sparse) is a deployable fallback mechanism.

**Distinction from existing records:** This is not a direct alpha signal but an infrastructure enabler. The alpha comes from how the surface completion and anomaly detection are used in downstream strategies (e.g., vol surface arbitrage, regime-adaptive position sizing).

## Signal

### Signal formation
- **Input:** Hourly Binance Options end-of-hour (EOH) snapshots, gridded onto a 6×7 tenor–delta grid.
- **Preprocessing:** Quality flags, provenance preservation, normalisation per tenor and delta.
- **Model:** 2D-convolutional masked-input VAE with deterministic per-tenor routing (smile re-fit when ≥3 observed cells in tenor row; ConvVAE otherwise).
- **Anomaly signal:** Per-snapshot reconstruction error (MSE across all grid cells) when evaluated without masking. Elevated error = surface deviates from learned manifold.

### Trading rules (source-reported, not specified as explicit strategy)
- **Anomaly detection:** High reconstruction error → flag period as anomalous; reduce exposure or enter contrarian vol trades.
- **Surface completion:** Use completed surface for pricing illiquid strikes/maturities; compare completed price vs. observed price for relative-value trades.
- **Cross-asset:** Compare BTC and ETH surface reconstruction errors; relative dislocation may indicate cross-asset vol spread opportunity.

### Parameters
- Grid: 6 tenors × 7 deltas per surface.
- Training window: May–October 2023 (6,034 hourly snapshots).
- Anomaly threshold: Not explicitly specified; reconstruction error is continuous.

## Required data

- **Instrument:** BTC and ETH options on Binance Options.
- **Data fields:** Full options chain (all strikes, all maturities) at hourly frequency. Implied volatilities across tenor–delta grid.
- **Timeframe:** Hourly snapshots.
- **Availability:** Binance Options public EOH archive.
- **Missing data assumptions:** The model handles partial observations (10–50% masking). Structurally correlated holes (entire tenor withdrawn) are the most challenging regime.

## Execution assumptions

- **Signal-to-order timing:** Hourly model inference; signals available at each snapshot.
- **Execution:** Options on Binance Options via market/limit orders.
- **Fees:** Binance Options trading fees.
- **Slippage:** Not modelled.
- **Spread:** Assumes mid-price for evaluation; real execution may face wider spreads on illiquid strikes.
- **Leverage:** Options are inherently leveraged.
- **Latency:** Model inference is fast (sub-second for single snapshot).
- **Partial fills:** Not addressed.

## Evidence

### Source-reported
- 0.83 vol points RMSE at 50% random masking (BTC+ETH joint model).
- 1.5–1.9 vol points under structured holes vs. 9.6–13.1 for smile re-fit.
- 8× improvement over parametric smile baseline.
- 9–27% improvement from joint BTC+ETH training over single-symbol.
- Unsupervised flagging of known dislocations (ETF rally, flash crash).
- Calendar- and butterfly-arbitrage-free at listed strikes.
- Full training and evaluation infrastructure released for reproducibility.

### Independently reproduced
Not independently reproduced.

### Negative evidence
- Training window is limited (May–October 2023, ~5 months). Generalisation to other regimes (bull market, bear market, high/low vol) is untested.
- Binance Options is less liquid than Deribit for BTC options; the manifold may not generalise to Deribit.
- The paper does not backtest any trading strategy using the anomaly signal or surface completion.
- Reconstruction error is a necessary but not sufficient condition for tradeable mispricing.

## Falsification plan

- **Required sample:** Retrain and evaluate on out-of-sample periods (2024–2026) covering different vol regimes.
- **Baseline:** Compare anomaly detection against simpler metrics (e.g., ATM IV level changes, skew changes, term structure slope changes).
- **Ablation:** Test whether ConvVAE reconstruction error adds information beyond standard vol surface summary statistics.
- **Cost sensitivity:** Model whether vol surface arbitrage signals survive Binance Options fees and bid-ask spreads.
- **Failure metric:** If reconstruction error does not correlate with subsequent price dislocations or strategy PnL, the anomaly signal fails.
- **Action on failure:** Retain the surface completion model as a practical tool for handling sparse options data; abandon the anomaly detection alpha claim.

## Crypto portability

direct

The paper is natively crypto-focused (BTC and ETH options on Binance Options). However:
- The model is trained on only 5 months of data from a single exchange. Generalisation to other exchanges (Deribit, OKX) and longer time periods is unproven.
- Binance Options has different contract specifications than Deribit (European vs. European, but different settlement and margin mechanics).
- The 6×7 tenor–delta grid is specific to Binance's listed strikes and expiries.

## Limitations

- **not independently reproduced** — No third-party replication of the ConvVAE training or anomaly detection performance.
- **data gap** — Training on only 5 months of data (May–October 2023) is a significant limitation. The model may overfit to this specific regime.
- **unproven** — No trading strategy backtest is provided. The connection between reconstruction error and tradeable alpha is hypothesised, not demonstrated.
- **underspecified** — The anomaly threshold and position sizing logic for any downstream strategy are not specified.
- **model risk** — The VAE architecture and hyperparameters are tuned to the specific training set; different market regimes may require retraining.
- **liquidity assumption** — Assumes Binance Options has sufficient liquidity for execution at model-implied prices, particularly for wing strikes.

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

- [[crypto-deribit-options-volatility-of-volatility-vov-realized-quarticity-2026-09-01]] — Related options infrastructure; uses realised quarticity for vol-of-vol estimation.
- [[bitcoin-options-implied-volatility-risk-reversal-skew-2026-09-01]] — Related options skew analysis; the ConvVAE provides a more sophisticated surface representation.
- [[defi-on-chain-options-mispricing-hegic-arbitrum-2026-09-01]] — Related options mispricing detection; this paper focuses on CEX options surfaces.

## Sources

1. Singh, S., Reddy, A., & Chopra, M. (2026). "Beyond the Smile: A Hybrid Convolutional VAE for Crypto Volatility Surfaces." arXiv:2606.16961 [cs.LG, q-fin.CP]. https://arxiv.org/abs/2606.16961
2. Data: 6,034 hourly Binance Options EOH snapshots (May–October 2023), BTC and ETH.
