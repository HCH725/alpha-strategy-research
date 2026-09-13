---
schema: strategy-research-record-v1
title: "Path Signature Regime Detection: Rough-Path Leverage-Cycle Feature Representation for Crypto Volatility Regime Classification"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - regime-detection
  - path-signature
  - rough-path
  - crypto-perpetual
  - funding-rate
  - basis
  - volatility-forecasting
status: research-only
confidence: medium
source_as_of: 2026-08-20
sources:
  - "Vibhun Naredla, 'Path Signatures for Regime Detection in Cryptocurrency Markets: A Rough-Path Framework Using Spot, Perpetual Basis, and Funding Rates', NHSJS, August 20, 2026. DOI: 10.2139/ssrn.6609698. URL: https://nhsjs.com/2026/path-signatures-for-regime-detection-in-cryptocurrency-markets-a-rough-path-framework-using-spot-perpetual-basis-and-funding-rates/"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Path Signature Regime Detection: Rough-Path Leverage-Cycle Feature Representation for Crypto Volatility Regime Classification

## Provenance

- **Author:** Vibhun Naredla
- **Publication:** NHSJS (Natural History of Science Journal), August 20, 2026
- **DOI:** 10.2139/ssrn.6609698
- **Primary Source URL:** https://nhsjs.com/2026/path-signatures-for-regime-detection-in-cryptocurrency-markets-a-rough-path-framework-using-spot-perpetual-basis-and-funding-rates/
- **PDF:** https://nhsjs.com/wp-content/uploads/2026/08/Path-Signatures-for-Regime-Detection-in-Cryptocurrency-Markets-A-Rough-Path-Framework-Using-Spot-Perpetual-Basis-and-Funding-Rates.pdf
- **SSRN:** https://doi.org/10.2139/ssrn.6609698
- **Primary Source Verification:** Full paper text directly read and all quantitative claims extracted from the NHSJS published version. Author, title, date, methodology, and all performance figures confirmed against the published text.

## Economic mechanism

### Source-reported

The author argues that cryptocurrency regime transitions are reflexive: aggregate leverage positioning changes precipitate forced-liquidation cascades, which alter the price path, which feeds back into positioning. Classical regime-detection methods (HMMs, rolling-volatility thresholds) impose Markovian dynamics or compress multivariate path information into low-dimensional moments, missing the path-dependent structure of crypto regime shifts. Path signatures from rough-path theory encode an infinite collection of order-aware interactions between coordinates and are near-injective on the space of paths, capturing the sequential order in which coordinates move rather than merely their marginal moments.

### Research interpretation

This is a **regime-detection feature-representation** hypothesis, not a directional trading signal. The falsifiable claim is:

1. Truncated path signatures (depth N=3) of a multivariate path combining BTC/ETH log-returns, realized-volatility proxy, perpetual-spot basis, and 8-hour funding rates contain information about future volatility regime transitions that is not captured by Markovian (HMM) or moment-based (rolling-volatility, HAR-RV) baselines.

2. The dominant signal is in third-order iterated integrals involving basis and volatility coordinates, consistent with a leverage-cycle mechanism: ordered triples of "leverage build-up → volatility spike → further leverage repricing."

3. The signature representation discriminates between distress-driven and bullish-regime volatility, which returns-based HMMs cannot.

Component roles (this is not a trading strategy, but a regime-detection module that could gate one):

- **Feature representation:** Path signatures of depth N=3 from a 7-coordinate augmented path
- **Projection:** Truncated SVD to 128 components
- **Classifier:** ℓ2-penalized logistic regression
- **Target:** Forward-volatility tercile classification or top-decile prospective detection

## Signal

### Formation timestamp

- Path signatures are computed from rolling 168-hour windows of hourly data
- The window is aligned to UTC hourly boundaries
- The signal becomes available at the close of each 168-hour window

### Lookback

- 168-hour (7-day) rolling window for signature extraction
- Lead-lag augmentation and time augmentation applied to the raw path before signature computation
- Truncated signature depth N=3 retains approximately 99.7% of the signature norm

### Entry (regime classification, not directional)

- SIG-LR outputs a probability of being in the "high-volatility" regime
- Threshold-based classification at multiple τ values (0.4, 0.5, 0.6, 0.7)
- No directional trading signal is produced; this is a regime-classification layer

### Exit

- Not applicable; regime classification is continuous and window-based

### Holding period

- Not applicable; this is a regime-detection framework, not a position-holding strategy

### Parameters

- Window length: 168 hours (`research-proposed`; source uses this as default but does not optimize it)
- Signature truncation depth: N=3 (`research-proposed`)
- SVD projection dimension: 128 (`research-proposed`)
- L2 regularization penalty: default sklearn logistic regression (`research-proposed`)
- Three random seeds for HMM initialization; model with highest training log-likelihood selected
- HMM covariance: full
- HMM convergence tolerance: 10⁻⁴ on log-likelihood change, max 150 EM iterations

### Position-sizing logic

- Not applicable; this is a regime-detection module

## Required data

- **Instrument:** BTC/USDT and ETH/USDT (spot and USDT-margined perpetual futures) on Binance
- **Venue:** Binance (public historical archive: data.binance.vision)
- **Market type:** Spot and USDT-margined perpetual futures
- **Timeframe:** 1-hour klines and 8-hour funding rates
- **Fields:** hourly close prices (spot and perpetual), 8-hour funding rates (forward-filled to hourly grid)
- **Sample period:** January 1, 2020 through April 17, 2026 (55,129 hourly observations after dropping rows during volatility initialization)
- **Derived features:** hourly log-returns; 24-hour rolling realized-volatility proxy (annualized by √365); perpetual-spot basis (F_t − P_t) / P_t; 8-hour funding rate forward-filled to hourly grid
- **Point-in-time:** Data sourced from Binance public archive; no look-ahead issues identified for the described features
- **Missing-data:** Rows during volatility initialization dropped; 100% feature coverage reported for the usable sample
- **Timestamp:** UTC hourly; no timezone issues identified
- **Funding/fee/spread needs:** Not applicable; this is a regime-detection framework, not a trading strategy

## Execution assumptions

This paper is a regime-detection study, not a trading strategy. No execution assumptions are made. The author explicitly states: "Signatures do not solve directional return prediction at sub-daily horizons, consistent with market-efficiency expectations."

If used as a regime-gate for a downstream trading strategy, the following would need to be specified (all `research-proposed`):

- Signal-to-order timing: regime signal is available at each hourly boundary
- Fill model: not specified
- Fees/slippage: not specified
- Leverage/margin: not specified
- Capacity: not specified

## Evidence

### Source-reported

All figures below are directly reported by Naredla (NHSJS, 2026).

**Tercile classification (forward-volatility tercile at 24h, 72h, 168h horizons):**

| Method | 24h accuracy | 72h accuracy | 168h accuracy |
|--------|-------------|-------------|--------------|
| SIG-LR | Competitive with HAR-RV | Competitive with HAR-RV | Highest (leads all baselines) |
| HAR-RV-LR | Strong baseline | Strong baseline | Competitive |
| HMM-LR | Lower | Lower | Lower |
| HMM-MULTI-LR | Lower | Lower | Lower |
| ROLLVOL-LR | Lower | Lower | Lower |

Note: The paper reports that confidence intervals overlap substantially with HAR-RV and rolling-volatility baselines at shorter horizons; SIG-LR leads at 168h. Exact accuracy numbers for the tercile classification are in Table 5 of the paper (not fully reproduced here due to truncation of the extracted text).

**Prospective detection (top-decile forward volatility, full 2023–2026 test timeline):**

| Method | Average precision | Precision at recall = 0.5 |
|--------|-------------------|--------------------------|
| SIG-LR | 0.090 | 0.061 |
| HMM-LR | 0.073 | 0.052 |
| HMM-MULTI-LR | 0.052 | 0.031 |
| ROLLVOL-LR | 0.040 | 0.052 |
| HAR-RV-LR | 0.054 | 0.050 |
| Random | 0.019 | 0.019 |

SIG-LR average precision is 1.7× the HAR-RV baseline and 4.7× the prevalence (0.019). The positive rate of the top-decile label is ~1.9%.

**Event study (six canonical regime shifts):**

- Signatures detect the out-of-sample SVB/USDC depeg within a 4-hour window across all tested thresholds
- Signatures correctly abstain on the bullish BTC ETF approval at thresholds τ ≥ 0.5
- HMM-based methods trigger on the ETF approval (their "high-vol" state corresponds to "non-quiet" and is triggered by any large return move regardless of direction)
- SIG-LR distinguishes distress-driven from bullish-regime volatility

**Signature coefficient decomposition:**

- Level-1 terms: L²-norm 0.05
- Level-2 terms: L²-norm 1.41
- Level-3 terms: L²-norm 6.60
- Level-3 terms account for ~98% of squared-coefficient mass
- Top 15 level-3 coefficients all involve at least one basis coordinate
- Dominant triples involve cross-coordinate interactions among {BTC basis, ETH basis, realized volatility}

**Ablations (24h horizon):**

- N=2 (full 240-dim, no SVD): lower performance
- N=3 + SVD-32: lower performance
- N=3 + SVD-128 (primary): best performance
- N=3 + SVD-512: slightly lower than SVD-128
- SIG (no RV) variant: attains best accuracy at 168h (0.763) and matches HAR-RV on log-loss (0.688 vs. 0.677)

**Computational cost:**

- Total end-to-end runtime: ~15 minutes across three horizons and seven methods
- Peak memory: 1.2 GB
- Signature extraction dominates: 240 seconds at N=3, 800 MB peak for raw signature array

Source reports the above results. This result has not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Signatures do not solve directional return prediction at sub-daily horizons
- Absolute precision values for prospective detection are modest (0.090 average precision) due to the low positive rate (~1.9%)
- Confidence intervals overlap with HAR-RV at shorter horizons (24h, 72h)
- The paper does not test whether the regime signal translates into trading profits after costs
- The paper acknowledges that "a full study of regime definitions is out of scope" (only tercile and drawdown-quartile labels tested)

## Falsification plan

1. **Out-of-sample regime classification decay:** If the SIG-LR average precision for top-decile prospective detection drops below 0.040 (research-defined falsification threshold) on a forward 6-month holdout beyond April 2026, the regime-detection claim is materially weakened.

2. **Basis-coordinate dependence:** If level-3 signature coefficients are dominated by return-volatility triples rather than basis-volatility triples in an independent sample, the leverage-cycle mechanism is falsified and the signature advantage reduces to generic path-dependence.

3. **Threshold sensitivity:** If the discriminative advantage of signatures over HAR-RV disappears at all threshold choices τ ∈ {0.3, 0.4, 0.5, 0.6, 0.7} on an independent sample, the event-localized detection claim is falsified.

4. **Regime-definition robustness:** If the signature advantage does not survive alternative regime definitions (e.g., return-based terciles, drawdown-based terciles at horizons not tested), the claim that signatures capture a regime-specific mechanism is weakened.

5. **Translation to trading:** If a downstream trading strategy gated by the SIG-LR regime signal does not show improved risk-adjusted returns versus an ungated baseline (research-defined falsification threshold: no improvement in Sharpe > 0.1), the practical value of the regime signal for alpha generation is not demonstrated.

## Crypto portability

direct

The paper is explicitly designed for crypto markets. It uses Binance BTC/USDT and ETH/USDT spot and perpetual futures data. The path coordinates (perpetual-spot basis, funding rates) are crypto-native features unavailable in traditional markets.

Crypto-specific considerations for downstream use:

- The regime signal is computed at hourly frequency on 168-hour windows; sub-hourly deployment would require re-architecting the pipeline
- The signal is trained on Binance data; transferability to other venues (OKX, Bybit, Hyperliquid) is untested
- The perpetual-spot basis and funding rates are venue-specific; cross-venue regime detection would require normalization
- The 24/7 continuous trading structure of crypto is well-suited to the rolling-window signature approach
- The paper does not address funding-rate mechanism changes (e.g., Binance's move from 8h to hourly funding) or listing changes

## Limitations

- **Regime detection only:** The paper explicitly does not produce directional trading signals or assess profitability. It is a regime-classification module, not a standalone alpha strategy.
- **Low absolute precision:** Average precision of 0.090 for prospective detection, while 4.7× the prevalence, is modest in absolute terms. The signal fires infrequently on the most extreme events.
- **Modest sample for extreme events:** The top-decile label has only ~1.9% positive rate in the test set; the event study covers six curated regime shifts.
- **No independent reproduction:** All results are from the original author's implementation.
- **Publication venue:** NHSJS is not a standard peer-reviewed quantitative finance journal; SSRN is a preprint server. The paper has not undergone formal peer review at a top-tier venue.
- **No trading-cost analysis:** The paper does not assess whether regime signals translate into profitable trading after costs.
- **Single-venue data:** All data is from Binance; cross-venue generalization is untested.
- **Hyperparameter choices:** Window length (168h), truncation depth (N=3), SVD dimension (128), and regularization are described but not optimized via cross-validation on an independent sample; they are `research-proposed`.
- **Signature computational cost:** 800 MB peak memory and 240 seconds for signature extraction may be prohibitive for high-frequency or multi-asset deployment.

## Implementation status

not-implemented

No implementation in our research stack. The author states that signature-feature caches, HMM model artifacts, and trained-model pickles will be provided for replication, but no public code repository link is given in the published text.

## Adoption boundary

This record is research-only material. Its presence in this repository does not constitute evidence of profitability, validated alpha, or authorization for deployment in paper trading, testnet, or live trading systems.

The paper is a regime-detection framework, not a trading strategy. Any downstream use as a regime gate for a trading strategy requires separate signal construction, execution assumptions, cost analysis, and validation.

## Related Wiki records

- [[crypto-perpetual-liquidation-cascade-early-warning-taker-flow-variance-2026-09-01]] — Early-warning signals for liquidation cascades using taker order-flow variance compression; shares the theme of detecting crypto regime transitions but uses different features (taker flow variance vs. path signatures) and targets liquidation cascades specifically rather than general volatility regimes.
- [[crypto-l2-liquidity-state-transitions-order-flow-2026-09-01]] — State-dependent L2 liquidity-state transitions in crypto futures; shares the regime-detection theme but operates on L2 order-book states rather than path-signature features.
- [[crypto-short-horizon-15min-mean-reversion-taker-flow-2026-09-01]] — Short-horizon mean reversion at 15-minute horizons; different mechanism and horizon but shares the crypto microstructure theme.

## Sources

1. Vibhun Naredla, "Path Signatures for Regime Detection in Cryptocurrency Markets: A Rough-Path Framework Using Spot, Perpetual Basis, and Funding Rates," NHSJS, August 20, 2026. DOI: 10.2139/ssrn.6609698. URL: https://nhsjs.com/2026/path-signatures-for-regime-detection-in-cryptocurrency-markets-a-rough-path-framework-using-spot-perpetual-basis-and-funding-rates/
2. PDF: https://nhsjs.com/wp-content/uploads/2026/08/Path-Signatures-for-Regime-Detection-in-Cryptocurrency-Markets-A-Rough-Path-Framework-Using-Spot-Perpetual-Basis-and-Funding-Rates.pdf
3. SSRN: https://doi.org/10.2139/ssrn.6609698
