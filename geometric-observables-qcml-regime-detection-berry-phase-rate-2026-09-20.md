---
schema: strategy-research-record-v1
title: "QCML Geometric Observables for Financial Regime Detection (Berry Phase Rate)"
created: "2026-09-20"
updated: "2026-09-20"
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - regime-detection
  - geometric
  - risk-overlay
status: research-only
confidence: medium
source_as_of: "2026-09-20"
sources:
  - "https://arxiv.org/abs/2605.17117"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# QCML Geometric Observables for Financial Regime Detection (Berry Phase Rate)

## Provenance

- **Primary Source:** Will Hammond (Pitzer College, Claremont, CA), "Geometric Observables for Financial Regime Detection," *arXiv preprint* `arXiv:2605.17117v2 [q-fin.ST]`, submitted May 16, 2026; revised May 27, 2026.
- **DOI:** `10.48550/arXiv.2605.17117`
- **Canonical URL:** https://arxiv.org/abs/2605.17117
- **Full text HTML:** https://arxiv.org/html/2605.17117v2
- **GitHub repository:** https://github.com/willhammondhimself/qcml-geometric-sde (latest commit: `26d61e8842ded283e216ac0660d7e1408832dcd7`, May 15, 2026)
- **Author:** Will Hammond, Pitzer College, Claremont, CA, USA. Email: whammond@pitzer.edu
- **Paper version:** v2 (May 27, 2026); 25 pages, 10 figures, 1 table.
- **Source reviewed as of:** 2026-09-20.

## Economic mechanism

### Source-reported

The paper proposes that geometric observables extracted from a QCML (Quantum Cognitive Machine Learning) spectral embedding of equity-index returns can detect regime transitions (calm-to-crisis switches) in financial markets. The framework embeds data as unit vectors in a finite-dimensional complex Hilbert space, builds a Hamiltonian from Hermitian operators scaled by PCA eigenvalues, and extracts four geometric quantities from the ground-state embedding:

1. **Berry Phase Rate:** Tracks accumulated geometric phase over a rolling window, responding to holonomy (curvature enclosed by the data trajectory).
2. **Spectral Entropy:** Measures the disorder in the eigenvalue distribution of the density operator.
3. **Reduced State Purity:** Quantifies entanglement or information loss when tracing out subsystems.
4. **Hamiltonian Sensitivity:** Measures how the ground state responds to parameter perturbations.

The mechanism is geometric, not statistical: regime shifts perturb the Hamiltonian and the induced Fubini–Study metric, Berry curvature, and topological invariants respond, providing detection signals that are structurally different from classical rolling-window, GARCH, or HMM-based approaches.

### Research interpretation

The hypothesis is that the data manifold's geometric curvature responds to structural regime changes that classical linear-feature detectors miss. The geometric observables capture distinct aspects of market state: curvature (Berry Phase Rate), entropy (Spectral Entropy), entanglement structure (Reduced State Purity), and sensitivity (Hamiltonian Sensitivity). Because geometric and classical channels are largely uncorrelated (mean |ρ| ≈ 0.22 in the paper), they hypothesize complementary regime coverage.

For a trading system, these observables could serve as:
- **Regime filter:** Suppress or modulate strategy exposure when Berry Phase Rate or consensus scores indicate elevated regime risk.
- **Risk overlay:** De-risk positions when geometric indicators signal crisis onset, as demonstrated in the paper's SPY de-risking experiment.

The paper is not an alpha strategy per se — it is a regime-detection methodology that could be composed with alpha strategies as a risk-management layer.

## Signal

### Source-reported

The paper does not define a standalone trading entry/exit rule. The regime-detection signal is constructed as follows:

1. **Feature construction:** Rolling 4-day return features enriched with lagged rolling statistics (mean, std, skew, kurtosis), fed into a QCML embedding with default parameters (dH=6, window w=15).
2. **Score computation:** For each observable, a z-score is computed against an expanding-window or full-sample reference distribution (Algorithm 1 in the paper).
3. **Detection threshold:** The paper uses z-score thresholding; the default threshold is selected via walk-forward nested hyperparameter optimization (HPO) against crisis labels.
4. **Walk-forward deployment:** Preprocessing (PCA, normalization) is fit on expanding data; hyperparameters are selected via nested HPO on past crisis windows; detection is applied forward.

Key signal characteristics:
- **Signal formation:** Daily (rolling window of w=15 trading days).
- **Lookback:** w=15 trading days (default).
- **Berry Phase Rate:** OOS walk-forward median Cohen's d = 0.72 (95% bootstrap CI [0.34, 1.18]), 67% fewer false alarms than Random Forest (1.2 vs 3.6/yr).
- **Reduced State Purity:** Highest in-sample separability (d = 0.83) but degrades on frozen holdout (d ≈ 0.26) — not reliable for live deployment.
- **Geometric-orthogonal insight:** Mean |ρ| ≈ 0.22 between geometric and classical channels, suggesting distinct signal capture.

### Research-defined thresholds

The following are **research-defined falsification thresholds**, not source-reported operational rules:
- Cohen's d > 0.5 for walk-forward detection (paper's default for "useful").
- False alarm rate < 3.6/yr (baseline RF level) for deployment viability.
- The paper's SPY de-risking experiment: Berry Phase Rate > threshold triggers de-risking, cutting max drawdown by ~51% with no Sharpe degradation. This is a demonstration, not a validated trading strategy.

## Required data

- **Universe:** US equity indices (S&P 500 / SPY, VIX). The paper evaluates on equity index returns, not crypto.
- **Timeframe:** Daily returns.
- **Data fields:** Daily close prices, rolling return features (mean, std, skew, kurtosis over 4-day windows).
- **Point-in-time:** Walk-forward preprocessing ensures no lookahead bias; expanding-window or rolling-window normalization.
- **Crypto-specific data gap:** No crypto universe is tested. The paper evaluates on 17 historical equity-market crises (2000–2024).

## Execution assumptions

- The paper does not specify a trading execution model. The SPY de-risking experiment (Section 6.3) is described as a risk-management overlay: when the Berry Phase Rate exceeds a threshold, the portfolio reduces equity exposure.
- **Signal-to-order timing:** Daily signal, presumably next-day execution.
- **Fill model:** Not specified.
- **Fees/slippage:** Not reported for the de-risking experiment.
- **Position sizing:** Not specified beyond the de-risking overlay concept.

## Evidence

### Source-reported

All figures from Hammond (arXiv:2605.17117v2):

- **Walk-forward OOS (Berry Phase Rate):** Median Cohen's d = 0.72 (95% bootstrap CI [0.34, 1.18], 10,000 resamples) across 5 of 9 labeled crisis windows; highest per-crisis Cohen's d among three walk-forward detectors on 5 of 9 crises.
- **False alarm rate:** Berry Phase Rate ~1.2/yr vs. Random Forest 3.6/yr (~67% reduction).
- **Offline separability (Reduced State Purity):** d = 0.83 (rank 1/46 methods); Absorption Ratio d = 0.80 (rank 2, classical benchmark).
- **Geometric-classical decorrelation:** Mean |ρ| ≈ 0.22, confirming distinct signal channels.
- **SPY de-risking experiment (Section 6.3):** Berry Phase Rate threshold triggers equity de-risking; max drawdown reduced by ~51% with no degradation in Sharpe ratio. This is a single-asset demonstration, not a backtested trading strategy.
- **Friedman test:** χ² = 233.1, p < 10⁻¹⁶ (methods are not exchangeable across crises).

### Independently reproduced

Not independently reproduced. This is a single-author paper with code available on GitHub; no third-party replication has been found.

### Negative evidence

- **Reduced State Purity OOS degradation:** d drops from 0.83 (in-sample) to ~0.26 on frozen holdout, meaning high offline separability does not guarantee out-of-sample stability.
- **No crypto testing:** The entire evaluation is on equity indices. No evidence of regime detection on crypto perpetual futures, crypto spot, or DeFi markets.
- **Single-author, no peer review:** As of the review date, this paper has not been peer-reviewed.
- **Berry Phase Rate median lead time:** Walk-forward median lead time is 4 days (retrospective lead time ~90 days), meaning it may not provide timely signals for high-frequency or intraday strategies.
- **No transaction cost analysis:** The de-risking experiment does not report turnover, transaction costs, or slippage.
- **Limited scope:** 17 equity crises over 24 years; sample size for regime detection evaluation is inherently small.

## Falsification plan

1. **Crypto portability test:** Apply the Berry Phase Rate to daily returns of BTC, ETH, SOL, and a crypto index. Measure walk-forward Cohen's d against known crypto crisis windows (LUNA/UST May 2022, FTX Nov 2022, Yen-carry Aug 2024, Oct 2025 cascade). Required: d > 0.4 on at least 3 of 5 events.
2. **False alarm calibration:** Run on 12+ months of live or out-of-sample crypto data. Target: < 2 false alarms per year at the equity-tested threshold.
3. **Ablation vs. classical baselines:** Compare Berry Phase Rate against rolling volatility z-score, HMM, GARCH, and CUSUM on the same crypto crisis windows. Required: Berry Phase Rate achieves higher or comparable Cohen's d on at least 50% of events.
4. **Cost sensitivity:** Model the de-risking overlay with realistic daily rebalancing costs (2–5 bps per trade). Test whether the ~51% drawdown reduction survives after costs.
5. **Threshold robustness:** Sweep detection thresholds; require that the Sharpe improvement from de-risking is positive across at least 3 threshold values, not just the optimal.
6. **Failure condition:** If Berry Phase Rate Cohen's d on crypto < 0.3 in walk-forward, or false alarm rate > 4/yr, the regime-detection hypothesis fails for crypto.

## Crypto portability

**adapted**

The paper's mechanism is geometric and theoretically asset-class-agnostic — it operates on return features and their manifold geometry. However:

- **No crypto evidence:** All evaluation is on US equity indices (S&P 500, VIX). No crypto universe is tested.
- **Crypto regime structure differs:** Crypto markets have 24/7 trading, frequent extreme moves driven by leverage/liquidation cascades, and structural regime differences (CEX vs. DEX, funding-rate mechanics). The Berry curvature response to these regime types is unknown.
- **Data frequency:** The paper uses daily returns. Crypto markets exhibit meaningful intraday microstructure (funding settlement every 8h, liquidation cascades on minute timescales) that daily features may not capture.
- **Portability risk:** The geometric embedding is calibrated on equity return distributions. Crypto return distributions are heavier-tailed and have different autocorrelation structure. The Hilbert space embedding may require re-calibration.

## Limitations

- **No crypto testing:** The entire evidence base is equity-market only. Crypto portability is unproven.
- **Not a standalone alpha strategy:** This is a regime-detection / risk-overlay methodology, not a predictive alpha signal.
- **Reduced State Purity OOS instability:** d ≈ 0.26 on frozen holdout vs. 0.83 in-sample; not reliable for deployment.
- **Small evaluation set:** 17 crises over 24 years; regime detection claims are inherently limited by the number of regime transitions.
- **No peer review:** Single-author preprint.
- **No transaction cost analysis:** De-risking experiment does not account for turnover or costs.
- **Walk-forward lead time:** Median 4-day lead time limits applicability to higher-frequency strategies.
- **Hyperparameter sensitivity:** Paper acknowledges default parameters sit on a broad plateau, not an isolated optimum; performance may be fragile across different market regimes.
- **Complementary, not replacement:** Paper explicitly positions geometric channels as complements to classical methods, not substitutes.

## Implementation status

Not implemented. No implementation in our research stack (Qlib, Hermes, or any downstream system) has been completed.

## Adoption boundary

Every newly collected external strategy is research material only.

A record being present in this repository does **not** mean:

- passed Research Intake Review;
- entered Hermes Wiki Brain;
- entered the production candidate pool;
- completed Qlib full-backtest validation;
- became a frozen survivor or leaderboard entry;
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

## Related Wiki records

- [[quant/crypto-perpetual-liquidation-cascade-early-warning-taker-flow-variance-2026-09-01]] — related regime-detection/early-warning literature for crypto perpetual cascades; the geometric observables could complement taker-flow-variance-based precursor signals.
- [[quant/crypto-quarter-hour-algorithmic-order-flow-predictability-2026-09-14]] — different mechanism (microstructural clock-phase effects) but both address detecting non-standard regime or structural features in crypto markets.

## Sources

1. Will Hammond. "Geometric Observables for Financial Regime Detection." *arXiv preprint* `arXiv:2605.17117v2 [q-fin.ST]`, submitted May 16, 2026; revised May 27, 2026. DOI: `10.48550/arXiv.2605.17117`. URL: https://arxiv.org/abs/2605.17117. Full text HTML: https://arxiv.org/html/2605.17117v2. GitHub: https://github.com/willhammondhimself/qcml-geometric-sde.
