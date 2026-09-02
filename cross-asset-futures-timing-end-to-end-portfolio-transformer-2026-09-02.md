---
schema: strategy-research-record-v1
title: "End-to-End Parametric Portfolio Policies for Cross-Asset Futures Timing: Portfolio Transformer vs. LSTM Under Differentiable Sharpe Optimization"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - futures-timing
  - cross-asset
  - parametric-portfolio-policies
  - portfolio-transformer
  - differentiable-sharpe
  - macro-allocation
  - transaction-costs
status: research-only
confidence: high
source_as_of: 2026-07-01
sources:
  - "Austin Pollok and Kevin Robik, 'End-to-End Parametric Portfolio Policies for Cross-Asset Futures Timing: When Do AI Models Beat Simple Rules?', arXiv:2607.00475v1 [q-fin.ST, q-fin.PM, q-fin.TR], July 1, 2026. DOI: 10.48550/arXiv.2607.00475. Stable URL: https://arxiv.org/abs/2607.00475. Full text: https://arxiv.org/html/2607.00475v1."
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# End-to-End Parametric Portfolio Policies for Cross-Asset Futures Timing: Portfolio Transformer vs. LSTM Under Differentiable Sharpe Optimization

## Provenance

- **Primary Source:** Austin Pollok and Kevin Robik, *"End-to-End Parametric Portfolio Policies for Cross-Asset Futures Timing: When Do AI Models Beat Simple Rules?"*, arXiv preprint `arXiv:2607.00475v1 [q-fin.ST, q-fin.PM, q-fin.TR]`, submitted July 1, 2026.
- **Canonical DOI:** [10.48550/arXiv.2607.00475](https://doi.org/10.48550/arXiv.2607.00475)
- **Traceable Source URL:** `https://arxiv.org/abs/2607.00475` (HTML full text: `https://arxiv.org/html/2607.00475v1`)
- **Primary Subject Classifications:** Statistical Finance (`q-fin.ST`), Portfolio Management (`q-fin.PM`), Trading and Market Microstructure (`q-fin.TR`).
- **Data Provider:** Barchart end-of-day continuous-contract futures data with exchange-sourced volume and open-interest roll schedules (2000–2024).

## Economic mechanism

### Source-reported

Systematic multi-asset investing (global macro and managed futures / CTA) allocates capital across equities, fixed income, currencies, and commodities. Realized returns and portfolio risk are heavily driven by dynamic cross-asset timing decisions. However, forecasting asset-class returns is notoriously difficult due to low signal-to-noise ratios, non-stationarity, and abrupt regime shifts. As a consequence, institutional allocators frequently rely on simple heuristics: naive equal weighting ($1/N$), risk parity (inverse volatility), or 12-month time-series momentum (TSMOM).

The standard quantitative alternative is a two-step "predict-then-optimize" mean-variance framework:
1. Estimate expected returns ($\hat{\mu}$) via statistical or ML models;
2. Estimate the covariance matrix ($\hat{\Sigma}$);
3. Solve a Markowitz optimization program for portfolio weights.

This two-step paradigm compounds return prediction errors into extreme, unstable portfolio weights. In contrast, **End-to-End Parametric Portfolio Policies** collapse prediction and optimization into a single differentiable step. A neural network parameterizes an allocation policy that maps market state representations directly to portfolio weights, optimizing the downstream economic objective—a differentiable Sharpe ratio—via gradient ascent. The authors study this framework across the 16 most liquid CME futures to evaluate whether and when learned policies beat simple rules, comparing a Portfolio Transformer against a recurrent LSTM policy under realistic transaction costs.

### Research interpretation

The core alpha hypothesis evaluates whether direct state-to-weight policy learning can extract cross-asset timing premia that survive institutional execution frictions:

1. **Direct Loss Alignment without Covariance Inversion:** By backpropagating through a differentiable Sharpe ratio objective, the policy directly internalizes risk, correlation, and diversification trade-offs. It avoids the ill-conditioned matrix inversions ($\hat{\Sigma}^{-1}$) that destabilize classical Markowitz solutions.
2. **Attention-Driven Turnover Suppression:** A central empirical discovery of the paper is the architectural divergence in turnover. Recurrent networks (LSTMs) react aggressively to short-term return noise, generating daily turnover of 7% to 17% that erodes out-of-sample returns under moderate trading costs. Conversely, the Portfolio Transformer—combining Time2Vec temporal embeddings with causal multi-head self-attention and Gated Residual Networks (GRNs)—synthesizes multi-horizon context, dampening high-frequency rebalancing to an average daily turnover of ~2% ($0.02$). This low-turnover property preserves net risk-adjusted returns across cost regimes.
3. **Disentangling Skill from Efficient Market Exposure:** A critical nuance established in the paper's factor attribution is that high learned Sharpe ratios do not necessarily represent market-neutral timing skill. In equity index futures, the transformer's performance is driven by a steady, sub-unit benchmark exposure ($\beta \approx 0.5$) with negligible residual alpha. The model learns to harvest risk premia efficiently rather than generating true orthogonal market timing.

## Signal

The allocation strategy is formulated as an end-to-end parametric policy mapping cross-sectional market observations directly to continuous target weights:

- **State Input ($X_t$):**
  - Daily cross-sectional return vector across the 16 CME futures contracts.
  - Optional engineered features evaluated in ablation: 1/5/20/60-day rate of change (trend), lagged autocorrelation (mean reversion), rolling Hurst exponent, rolling skewness and kurtosis (regime indicators), 20-day realized volatility, and rolling pairwise correlation, all standardized via 252-day trailing $z$-scores.
  - *Empirical Note:* Out-of-sample walk-forward tests revealed that engineered features added little incremental value over raw cross-sectional return series; the primary production state uses the return cross-section.
- **Portfolio Transformer Architecture:**
  - **Temporal Embedding:** Time2Vec layer decomposing input time series into linear trend and learnable periodic sinusoidal components (frequencies and phase shifts).
  - **Encoder:** 4 identical layers of multi-head self-attention operating across assets and temporal lookbacks, each followed by a Gated Residual Network (GRN) that applies gating to modulate feature pass-through.
  - **Decoder:** 4 layers of multi-head cross-attention attending to encoder context representations.
  - **Causal Masking:** Strict lower-triangular causal attention mask ($M_{ij} = 0$ for $j \le i$, $M_{ij} = -\infty$ for $j > i$) preventing information leakage from future bars.
- **Signed-Softmax Output Weight Layer:**
  - The network maps state $X_t$ to raw decoder scores $s_{i,t}(\theta) \in \mathbb{R}$ for each asset $i \in \{1, \dots, N\}$.
  - Weights are generated via a signed-softmax transformation:
    $$w_{i,t}(\theta) = \frac{\operatorname{sign}\bigl(s_{i,t}(\theta)\bigr) \exp\bigl(|s_{i,t}(\theta)|\bigr)}{\sum_{j=1}^N \exp\bigl(|s_{j,t}(\theta)|\bigr)}$$
  - Properties: Allows unconstrained long ($w_i > 0$) and short ($w_i < 0$) positions while strictly bounding total gross leverage to unit notional: $\sum_{i=1}^N |w_{i,t}(\theta)| = 1.0$.
- **Training Objective (Differentiable Sharpe Ratio):**
  - Gross portfolio return: $R_{P,t}(\theta) = \sum_{i=1}^N w_{i,t}(\theta) R_{i,t}$.
  - Loss function: Negative annualized Sharpe ratio:
    $$\mathcal{L}(\theta) = - \frac{\mathbb{E}\left[R_{P,t}(\theta)\right]}{\sqrt{\operatorname{Var}\left(R_{P,t}(\theta)\right)}}$$
  - Cost-aware objective (studied in turnover regularization tests):
    $$\mathcal{L}_{\text{net}}(\theta) = - \frac{\mathbb{E}\left[R_{P,t}^{\text{net}}(\theta)\right]}{\sqrt{\operatorname{Var}\left(R_{P,t}^{\text{net}}(\theta)\right)}}, \quad R_{P,t}^{\text{net}}(\theta) = R_{P,t}(\theta) - \lambda \sum_{i=1}^N \left|w_{i,t}(\theta) - w_{i,t-1}(\theta)\right|$$
    where $\lambda = 0.0002$ (2 bps baseline).
- **Optimization Hyperparameters:**
  - Optimizer: AdamW with OneCycleLR learning rate schedule.
  - Activation: GELU; pre-activation Layer Normalization.
  - Gradient clipping norm: $1.0$.
  - Ensemble Averaging: Output weights averaged across 3 independently seeded transformer initializations to dampen seed-level variance.
- **Cadence:** Daily rebalancing at close-to-close timestamps.

## Required data

- **Universe (16 Most Liquid CME Futures Across 6 Asset Classes):**
  1. **Equity Indices (3):** E-mini S&P 500 (`ES`), E-mini NASDAQ-100 (`NQ`), E-mini Russell 2000 (`RTY`).
  2. **Interest Rates / Treasuries (4):** 2-Year Treasury Note (`ZT`), 5-Year Treasury Note (`ZF`), 10-Year Treasury Note (`ZN`), 30-Year Treasury Bond (`ZB`).
  3. **Foreign Exchange (2):** Euro FX (`6E`), Japanese Yen (`6J`).
  4. **Energy (2):** WTI Crude Oil (`CL`), Henry Hub Natural Gas (`NG`).
  5. **Metals (3):** Gold (`GC`), Copper (`HG`), Silver (`SI`).
  6. **Agriculturals (2):** Corn (`ZC`), Wheat (`ZW`).
- **Data Period:** January 2000 through December 2024 (25 years of daily data).
- **Vendor:** Barchart.
- **Continuous Contract Construction:** Continuous spliced contracts rolled based on volume and open interest; all rolling standardizations and feature calculations use strictly trailing historical bars (no look-ahead).
- **Fields:** Daily open, high, low, close, volume, and open interest.

## Execution assumptions

- **Execution Protocol:** Daily close-to-close execution. Signals generated using information through day $t$ close; target weights executed for holding period $t \to t+1$.
- **Transaction Cost Rate:** Baseline rate of 2 basis points ($0.0002$) per one-sided trade for liquid CME contracts; tested across sensitivity sweeps of 1 bp, 2 bps, 5 bps, and 10 bps.
- **Turnover Metrics:** Daily one-sided turnover defined as $\frac{1}{2}\sum_{i=1}^N |w_{i,t} - w_{i,t-1}|$:
  - Portfolio Transformer: $\sim 0.02$ per day across universes (approx. 2% daily rebalancing).
  - LSTM Policy: $0.07$ to $0.17$ per day (17% daily rebalancing on the pooled cross-asset portfolio).
- **Leverage & Financing:** Scale-invariant evaluation (unit gross exposure $\|w\|_1 = 1.0$); performance normalized to 10% annualized target volatility for cumulative risk-adjusted compounding comparisons.

## Evidence

### Source-reported

All metrics below reflect out-of-sample walk-forward generalization over 2011–2024 (initial 40% 2000–2010 used for training, followed by expanding ~4-year test blocks with 90/10 train/validation splits, no data shuffling).

**Table 1: Out-of-Sample Sharpe Ratio Across Universes and Strategies (2011–2024):**

| Universe / Asset Class | Transformer (Gross) | LSTM (Gross) | Equal Weight ($1/N$) | Risk Parity | TSMOM (12M) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Pooled Cross-Asset (16 Futures)** | **0.55** | 0.50 | 0.52 | Trails (p=0.99) | 0.44 (p=0.68) |
| **Equity Index (`ES`, `NQ`, `RTY`)** | 0.78* | **0.87*** | 0.78 | 0.79 | 0.55 |
| **Agriculturals (`ZC`, `ZW`)** | **0.34** | 0.22 | Negative | Negative | 0.15 |
| **Foreign Exchange (`6E`, `6J`)** | 0.11 | Negative | Negative | Negative | **0.25** |
| **Metals (`GC`, `HG`, `SI`)** | **0.48** | 0.42 | 0.38 | 0.40 | 0.31 |
| **Energy (`CL`, `NG`)** | 0.38 | 0.35 | **0.45** | 0.41 | 0.20 |
| **Interest Rates (`ZT`–`ZB`)** | 0.30 | 0.28 | 0.32 | 0.35 | **0.52** |

*\* Denotes statistical significance at $p < 0.05$ after Bonferroni multiple-testing correction across the 7 universes ($t \approx 3$ for equities; cross-asset transformer reaches $t \approx 2$, clearing unadjusted 5% level).*

**Table 2: Transaction Cost Sensitivity (Net Sharpe on Pooled Cross-Asset Portfolio):**

| Cost Rate (bps per side) | Transformer (Net Sharpe) | LSTM (Net Sharpe) |
| :--- | :--- | :--- |
| **0 bps (Gross)** | **0.55** | 0.50 |
| **2 bps (Realistic Liquid Baseline)** | **0.54** | 0.33 |
| **5 bps** | **0.52** | 0.08 |
| **10 bps (Stress)** | **0.50** | **-0.38** |

**Statistical Testing & Attribution (Source-Reported):**
- **Stationary Bootstrap vs. Benchmarks (Pooled Cross-Asset, 5,000 block resamples):**
  - Probability Transformer outperforms Risk Parity: $p = 0.99$.
  - Probability Transformer outperforms TSMOM: $p = 0.68$.
  - Probability Transformer outperforms Equal Weighting ($1/N$): $p = 0.59$ (matches rather than decisively beats $1/N$).
- **Factor Attribution (Residual Alpha vs. Benchmark Beta):**
  - In the equity index sleeve, regressing Transformer returns on the diversified benchmark yields an insignificant residual alpha ($\alpha \approx 0, p > 0.10$), while market exposure explains the majority of returns ($\beta \approx 0.50$). The model learns risk-efficient sub-unit market exposure rather than timing alpha.
  - The LSTM exhibits statistically significant residual alpha in equities, but its high turnover ($0.17$/day) wipes out this advantage after trading fees.
  - In metals and energy sleeves, the Transformer exhibits positive residual alpha point estimates.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Fragility of High-Capacity Complexity:** Introducing Mixture-of-Experts (MoE) architectures, larger feature sets (Hurst, autocorrelation, realized volatility), per-asset-class hyperparameter tuning, cross-model ensembling (combining LSTM + Transformer), and explicit turnover-penalized loss functions all failed to reliably improve out-of-sample performance over the simple 3-seed averaged Transformer.
- **Seed Sensitivity:** A single-seed Portfolio Transformer produces widely dispersed out-of-sample Sharpe ratios; ensembling across 3 distinct random seeds was required to stabilize generalization.
- **Extreme Cost Vulnerability of LSTM:** Due to daily turnover of $17\%$, the LSTM's net Sharpe on cross-asset futures crashes from $0.50$ (gross) to $-0.38$ at 10 bps, demonstrating that recurrent models severely overfit high-frequency return noise.
- **Parity with Naive 1/N Diversification:** The Transformer achieves a cross-asset Sharpe of $0.55$ gross ($0.54$ net at 2 bps), which is economically indistinguishable from naive $1/N$ equal weighting ($0.52$, bootstrap superiority probability only $59\%$). Where passive diversification is strong, the added complexity of end-to-end deep learning adds marginal net value.

## Falsification plan

1. **Transaction Cost Escalation Stress Test:** Evaluate the Portfolio Transformer under slippage schedules of 5 bps, 10 bps, and 15 bps. If net annualized Sharpe ratio drops below $0.30$ or falls below naive $1/N$ by more than $0.10$ Sharpe, the claim of low-turnover execution robustness is falsified.
2. **Stationary Block Bootstrap Test vs. Naive Rules:** Conduct a block bootstrap test (mean block length 21 trading days, 10,000 resamples) comparing net Transformer returns against $1/N$ equal weighting. If the empirical probability that Transformer outperforms $1/N$ falls below $0.50$, the hypothesis of superior learned allocation skill is rejected.
3. **Pure Alpha Neutrality Audit:** Regress learned portfolio returns on an equal-weighted cross-asset benchmark and a 12-month TSMOM factor. If the regression intercept $\alpha$ is statistically indistinguishable from zero ($t < 1.96$) while factor beta $\beta$ explains $> 70\%$ of return variance, the strategy is falsified as pure dynamic beta exposure rather than alpha timing.
4. **Cross-Sectional Contract Shuffling:** Permute the contract return series across columns randomly each rebalance. If the model achieves an out-of-sample Sharpe $> 0.25$, the policy is exploiting fitting artifacts or look-ahead leakage.
5. **Rejection Threshold:** If the rolling 3-year out-of-sample net Sharpe falls below $0.20$, the strategy is marked rejected for quantitative portfolio integration.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Porting Mechanism:** The end-to-end framework (mapping cross-sectional return tensors through a Portfolio Transformer with signed-softmax output layers) can be ported to top liquid crypto perpetual contracts (BTC, ETH, SOL, XRP, DOGE, AVAX, LINK, NEAR, SUI, ADA).
- **Crypto-Specific Structural Hazards:**
  1. **Lack of Asset-Class Orthogonality:** CME futures span 6 genuinely distinct asset classes with low mutual correlation (equities, rates, currencies, commodities). In crypto, virtually all altcoins exhibit correlation of $0.70 \text{--} 0.90$ with Bitcoin. Cross-asset breadth is largely illusory, reducing the cross-sectional timing problem to leveraged directional BTC/ETH beta.
  2. **Funding Rate Carry Costs:** CME futures reflect interest-rate implied financing via basis. Crypto perpetual futures incur variable 8-hour funding rates. In bull regimes, altcoin funding can exceed 30–50% annualized, creating severe negative drag on long positions that exceeds traditional futures roll drag.
  3. **Continuous 24/7 Market Microstructure:** CME futures observe standardized daily settlement windows. Crypto trades continuously with severe weekend liquidity evaporation and cascading deleveraging liquidations.
  4. **Basis Risk & Venue Fragmentation:** Funding rates and prices vary across exchanges (Binance, Bybit, OKX, Hyperliquid), requiring multi-venue execution modeling.

## Limitations

- **Limited Cross-Sectional Breadth in Single Sleeves:** Sub-asset sleeves contain only 2 to 4 contracts, constraining cross-sectional rank opportunities.
- **Absence of Residual Timing Alpha in Equities:** High Sharpe in equities is shown to be sub-unit beta exposure rather than orthogonal alpha.
- **Seed Variance:** Single-seed models are noisy; practical deployment mandates multi-seed ensemble averaging.
- **Not Independently Reproduced:** Empirical metrics rely exclusively on Pollok & Robik (arXiv:2607.00475v1).

## Implementation status

`not-implemented`. No implementation in PyBroker, NautilusTrader, or live trading engines has been performed.

## Adoption boundary

`research-only`. This document constitutes normalized research material. It does not authorize capital deployment, implementation into execution engines, paper trading, testnet verification, or live trading.

## Related Wiki records

- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`
- `[[quant/phase8-financial-ml-sample-leakage-contract-2026-08-28]]`
- `[[quant/volatility-targeting-risk-parity-constrained-2026-08-28]]`
- `[[quant/signal-to-executable-pnl-costs-2026-08-28]]`

## Sources

- Austin Pollok and Kevin Robik, *"End-to-End Parametric Portfolio Policies for Cross-Asset Futures Timing: When Do AI Models Beat Simple Rules?"*, arXiv preprint `arXiv:2607.00475v1 [q-fin.ST, q-fin.PM, q-fin.TR]`, submitted July 1, 2026. DOI: [10.48550/arXiv.2607.00475](https://doi.org/10.48550/arXiv.2607.00475). Stable URL: `https://arxiv.org/abs/2607.00475`. Full text: `https://arxiv.org/html/2607.00475v1`.
