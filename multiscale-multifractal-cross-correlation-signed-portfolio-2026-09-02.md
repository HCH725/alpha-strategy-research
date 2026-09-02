---
schema: strategy-research-record-v1
title: "Mean-MFCCA Signed Multifractal Cross-Correlation Analysis for Multiscale Downside Risk Minimization"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - portfolio-optimization
  - multifractal
  - detrended-cross-correlation
  - mfcca
  - tail-risk
  - expected-shortfall
  - multi-asset
status: research-only
confidence: medium
source_as_of: 2026-08-24
sources:
  - "Shinji Kakinaka and Ken Umeno, 'Portfolio Allocation under Heterogeneous Scales and Multifractality', arXiv:2608.04987v1 [q-fin.PM, q-fin.RM], August 24 2026. https://arxiv.org/abs/2608.04987. DOI: https://doi.org/10.48550/arXiv.2608.04987"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Mean-MFCCA Signed Multifractal Cross-Correlation Analysis for Multiscale Downside Risk Minimization

## Provenance

- Canonical Source: arXiv:2608.04987v1 [q-fin.PM, q-fin.RM], submitted August 5, 2026; revised August 24, 2026.
- Authors: Shinji Kakinaka (School of Economics and Management, Kochi University of Technology, Japan; kakinaka.shinji@kochi-tech.ac.jp) and Ken Umeno (Graduate School of Informatics, Kyoto University, Japan; umeno.ken.8z@kyoto-u.ac.jp).
- DOI: https://doi.org/10.48550/arXiv.2608.04987
- Stable Source URLs:
  - Abstract: https://arxiv.org/abs/2608.04987
  - PDF: https://arxiv.org/pdf/2608.04987
- Empirical dataset: Daily returns of 4 representative financial assets:
  - Nikkei 225 stock index (Japan)
  - S&P 500 stock index (US)
  - West Texas Intermediate (WTI) crude oil futures
  - Gold spot against US Dollar (XAU/USD)
  - Source: One-minute dealer quotes from HistData (http://www.histdata.com/), aggregated to daily close at the 17:00 Eastern Time daily trading pause. Sample covers January 2011 to November 2023 (N=3330 aligned daily return observations).

## Economic mechanism

### Source-reported

Financial asset cross-correlations are neither scale-free nor amplitude-independent. Under the Fractal Market Hypothesis (Peters 1994), financial markets comprise heterogeneous market participants operating across diverse holding periods (from high-frequency intraday traders to multi-month institutional investors). Furthermore, asset price dynamics exhibit multifractality, meaning that small and large fluctuations scale with different generalized Hurst exponents.

Prior multifractal portfolio models (e.g., mean-MFDCCA; Li et al. 2021, 2024) rectified local detrended cross-covariances by taking absolute values $|X_v(t) - \tilde{X}_v(t)||Y_v(t) - \tilde{Y}_v(t)|$ before taking the generalized average over segments. This absolute-value rectification strips out the directional sign of local co-movement. Consequently, counter-moving assets that hedge each other are treated identically to co-moving assets that amplify joint risk.

The paper introduces Multifractal Cross-Correlation Analysis (MFCCA; Oświeçimka et al. 2014) into portfolio allocation:
1. **Sign-Preserving Fluctuation Function**: MFCCA retains the sign of local detrended covariance:
   $$F_{XY,\mathrm{MFCCA}}^q(s) = \frac{1}{2N_s} \sum_{v=1}^{2N_s} \mathrm{sgn}\left[f_{XY}^2(s,v)\right] \left|f_{XY}^2(s,v)\right|^{q/2}$$
   Co-moving components ($f_{XY}^2 > 0$) increase portfolio risk, while counter-moving components ($f_{XY}^2 < 0$) decrease risk.
2. **Scale-Dependent Limit**: At $q=2$, the MFCCA quadratic form coincides with the Detrended Cross-Correlation Analysis (DCCA) fluctuation function of the portfolio series itself, recovering a scale-dependent generalization of classical portfolio variance.
3. **Population-Level Aggregation**: Optimal portfolio weights are integrated across a scale grid $S$ and fluctuation order grid $Q$, synthesizing an allocation that diversifies simultaneously across investor investment horizons and volatility regimes.

### Research interpretation

The proposed alpha mechanism is risk-premia harvesting via structural downside-risk minimization. Rather than maximizing forecasted directional return, the mean-MFCCA model constructs a risk-minimizing covariance-like metric that is robust to heavy tails, non-Gaussian jumps, and scale-dependent correlation breakdowns.

By explicitly capturing negative co-movements across different volatility amplitudes ($q$) and holding durations ($s$), the model shifts portfolio capital into assets that provide genuine tail diversification during large drawdowns, while avoiding the over-allocation to spurious hedges caused by absolute-value distortion in MFDCCA.

## Signal

The strategy produces monthly rebalanced portfolio weights $\mathbf{w}^{opt} = [w_1^{opt}, \dots, w_n^{opt}]^T$ for an $n$-asset universe ($n=4$ in the empirical paper).

### Signal construction steps

1. **Profile Construction & Detrending**:
   For each asset series $\{x_t\}_{t=1}^N$, compute profile $X(t) = \sum_{i=1}^t (x_i - \bar{x})$. Partition $X(t)$ into $N_s = \lfloor N/s \rfloor$ non-overlapping segments of scale length $s$. Repeat from the reverse end to obtain $2N_s$ segments.
   Within each segment $v$, fit a degree-2 polynomial local trend $\tilde{X}_v(t)$.
2. **Local Detrended Cross-Covariance**:
   $$f_{ij}^2(s,v) = \frac{1}{s}\sum_{t=1}^s \left[X_{v,i}(t) - \tilde{X}_{v,i}(t)\right] \left[X_{v,j}(t) - \tilde{X}_{v,j}(t)\right]$$
3. **Signed MFCCA Fluctuation Matrix**:
   For fluctuation order $q \in Q$ and scale $s \in S$:
   $$F_{ij,\mathrm{MFCCA}}^q(s) = \frac{1}{2N_s} \sum_{v=1}^{2N_s} \mathrm{sgn}\left[f_{ij}^2(s,v)\right] \left|f_{ij}^2(s,v)\right|^{q/2} \quad (q \neq 0)$$
   $$F_{ij,\mathrm{MFCCA}}^0(s) = \frac{1}{2N_s} \sum_{v=1}^{2N_s} \mathrm{sgn}\left[f_{ij}^2(s,v)\right] \ln\left|f_{ij}^2(s,v)\right| \quad (q = 0)$$
4. **Positive Semidefinite Regularization**:
   The empirical fluctuation matrix $\mathbf{F}_{\mathrm{MFCCA}}^q(s)$ is symmetrized. If negative eigenvalues occur (observed in only 0.95% of rolling windows, exclusively at $q=1$), eigenvalue clipping replaces negative eigenvalues with zero to ensure a positive semidefinite quadratic objective.
5. **Single $(q,s)$ Quadratic Program**:
   For target annual return $r_e \in [0\%, 3\%]$ (converted to daily required return):
   $$\min_{\mathbf{w}} \frac{1}{2} \sum_{i,j=1}^n w_i(q,s) w_j(q,s) F_{ij,\mathrm{MFCCA}}^q(s)$$
   $$\text{subject to } \sum_{i=1}^n w_i(q,s) E(r_i) \ge r_e, \quad \sum_{i=1}^n w_i(q,s) = 1, \quad w_i(q,s) \ge 0$$
   where $E(r_i)$ is estimated as the sample mean of daily returns within the estimation window.
6. **Multiscale & Multifractal Population Aggregation**:
   The final allocation vector $\mathbf{w}^{opt}$ aggregates over all $(s, q)$ pairs:
   $$w_i^{opt} = \sum_{s \in S} \sum_{q \in Q} \alpha(s) \beta(q) w_i(q,s)$$
   with uniform weights $\alpha(s) = \frac{1}{\#S}$ and $\beta(q) = \frac{1}{\#Q}$.

### Parameters

- Estimation window length: $N_w = 520$ trading days (approximately 2 rolling calendar years).
- Rebalancing cadence: Monthly rolling shift (yielding 131 rolling evaluation windows over 2013–2023).
- Scale set: $S = \{5, 30, 55, 80, 105, 130\}$ trading days (upper bound $\approx N_w / 4$).
- Fluctuation order set: $Q = \{1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0\}$ (focusing on moderate to large market fluctuations).
- Annual required return grid: $r_e \in [0\%, 3\%]$.
- Detrending polynomial degree: 2 (quadratic detrending).

## Required data

- Universe: 4 macro asset proxies:
  - Nikkei 225 equity index (cash/index dealer quote)
  - S&P 500 equity index (cash/index dealer quote)
  - WTI crude oil (futures continuous prompt contract)
  - XAU/USD (gold spot against US Dollar)
- Venue / Source: HistData (http://www.histdata.com/).
- Timeframe: 1-minute dealer bid/ask mid-quotes aggregated to daily closes at 17:00 Eastern Time.
- Cleaning: Synchronous trading calendar filtering; days with missing values in any of the 4 assets are dropped, yielding 3330 daily aligned log-returns.
- Point-in-time constraints: Estimation uses only historical rolling window $N_w = 520$ days prior to the rebalancing date.

## Execution assumptions

- Signal-to-order timing: Monthly rebalancing computed at month end; weights applied to subsequent month's daily returns.
- Position constraints: Long-only ($w_i \ge 0$), fully invested ($\sum w_i = 1$). No short sales, no leverage.
- Frictions: The source paper presents gross returns and risk metrics; explicit transaction costs, exchange fees, borrow fees, and bid-ask spreads are omitted in the baseline paper tables.

## Evidence

### Source-reported

All figures below are cited directly from Kakinaka and Umeno (2026):

1. **Synthetic Process Experiments (50 seeded realizations of $N=2^{13}$ steps)**:
   - Generated from coupled two-component ARFIMA and Markov-Switching Multifractal (MSM) models.
   - Evaluated using 10-period 99% Value-at-Risk (VaR) and 10-period 97.5% Expected Shortfall (ES) as positive loss measures (smaller is better):
     - **MV (Mean-Variance)**: VaR = 6.677 (std 0.722), ES = 6.742 (std 0.733)
     - **MD (MFDCCA, $q=2$)**: VaR = 6.342 (std 0.542), ES = 6.603 (std 0.597)
     - **MMFD (MFDCCA, $q \in Q$)**: VaR = 6.193 (std 0.570), ES = 6.433 (std 0.590)
     - **MC (MFCCA, $q=2$)**: VaR = 5.925 (std 0.614), ES = 6.095 (std 0.612)
     - **MMFC (MFCCA, $q \in Q$, proposed)**: **VaR = 5.923** (std 0.607), **ES = 6.048** (std 0.594)
   - Paired Wilcoxon signed-rank tests confirmed that all pairwise differences in ES were statistically significant ($p < 10^{-5}$), including MMFC over MC. Realized returns were statistically indistinguishable ($p > 0.3$ for all pairs).
   - Notably, the $q=2$ sign-preserving MC portfolio outperformed the fully multifractal MMFD model, proving that preserving the sign of local covariance contributes more to tail-risk reduction than expanding fluctuation orders without signs.
2. **Empirical Multi-Asset Results (131 rolling monthly windows, Jan 2011 – Nov 2023)**:
   - In-sample: MMFC attained the smallest average monthly drawdown and smallest 10-day 97.5% ES among all 5 portfolios for every required return $r_e \in [0\%, 3\%]$. Drawdown reduction was statistically significant against MV and MFDCCA ($p \simeq 0.04$ at $r_e = 1\%$ using HAC standard errors); ES improvement over MC was significant ($p \simeq 0.01$).
   - Out-of-sample: MMFC attained the lowest average monthly drawdown and lowest 10-day 99% VaR across all required returns $r_e$, while improving annualized total return over both MV and MC.
   - Drawdown advantage of MMFC over MFDCCA was highly significant ($p < 10^{-4}$ under paired monthly tests at $r_e=1\%$).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Return vs. Risk Trade-off: MFDCCA-based portfolios delivered higher raw out-of-sample realized returns than MMFC, but suffered visibly higher drawdowns, VaR, and ES.
- Out-of-Sample Statistical Power: While MMFC consistently achieved lower drawdown and VaR than classical Mean-Variance (MV) out-of-sample, block-bootstrap tests did not achieve 5% statistical significance against MV over the 131-month test window, reflecting sample size limitations.
- Non-PSD Occurrences: At $q=1$, 0.95% of estimated MFCCA matrices were not positive semidefinite, requiring eigenvalue clipping.

## Falsification plan

1. **Fourier Phase-Randomized Surrogate Test**: Generate phase-randomized surrogate return series that preserve power spectra and linear correlation but destroy multifractal cascades and asymmetric co-movements. If the MMFC portfolio does not lose its tail-risk advantage over MV on the surrogate series, the multifractal hypothesis is falsified.
2. **Turnover Cost Barrier Test**: Model a turnover fee of 15–25 bps per rebalance. If monthly allocation adjustments between equity, oil, and gold consume all risk-reduction benefits relative to a static risk-parity allocation, the strategy is deemed economically unexecutable.
3. **High-Dimensional Asset Universe Stress Test**: Expand the universe from $n=4$ to $n=50$ assets. Test whether the proportion of non-PSD matrices escalates and whether quadratic program solve times become intractable.

## Crypto portability

Portability status: **adapted / unproven**.

The source paper exclusively tests traditional equities, commodities, and currencies (Nikkei, S&P 500, WTI, Gold). Porting to cryptocurrency requires explicit adaptation:

1. **Continuous 24/7 Trading**: The 17:00 Eastern Time session boundary does not apply to crypto; a UTC midnight boundary must be standardized.
2. **Extreme Multifractality & Fat Tails**: Cryptocurrency returns display significantly stronger multifractality (wider singularity spectra $\Delta \alpha$) and higher jump frequencies than traditional commodities. Fluctuation orders $Q$ may need re-calibration to avoid numerical divergence in $|f_{ij}^2|^{q/2}$ for large $q$.
3. **Perpetual Basis & Funding Drag**: Applying multiscale allocation across spot and perpetual contracts must incorporate 8-hour funding rates, which can erode monthly holding returns.
4. **Liquidation Contagion**: During crypto market flash-crashes, cross-asset correlations rapidly converge toward 1 across all scales, temporarily nullifying the diversification benefits of counter-moving components.

## Limitations

- **Omission of Transaction Costs**: The paper does not evaluate turnover fees or market impact in its empirical backtest.
- **Narrow Universe**: Empirical validation is restricted to 4 macro assets; behavior in large cross-sections ($n > 20$) is unverified.
- **Heuristic Population Weighting**: Equal weighting across scales ($\alpha(s) = 1/\#S$) and fluctuation orders ($\beta(q) = 1/\#Q$) is an ad-hoc heuristic rather than an analytically optimized meta-policy.
- **Absence of Public Code Repository**: The paper provides mathematical formulations but no public GitHub repository or commit SHA.

## Implementation status

not-implemented. This research capture is an analysis of published academic literature; no implementation in NautilusTrader, PyBroker, or live execution engines has been created.

## Adoption boundary

research-only / not-approved. This record is strictly for research interpretation and does not authorize paper trading, testnet deployment, or live capital allocation.

## Related Wiki records

- [[quant/portfolio-covariance-and-shrinkage-2026-08-28]]
- [[quant/volatility-targeting-risk-parity-constrained-2026-08-28]]
- [[quant/expected-shortfall-and-risk-of-ruin-2026-08-28]]
- [[quant/phase9-factor-covariance-redundancy-risk-decomposition-2026-08-28]]

## Sources

- Shinji Kakinaka and Ken Umeno, 'Portfolio Allocation under Heterogeneous Scales and Multifractality', arXiv preprint arXiv:2608.04987v1 [q-fin.PM, q-fin.RM], August 24, 2026. Available at: https://arxiv.org/abs/2608.04987; PDF: https://arxiv.org/pdf/2608.04987.
- Oświęcimka, P., Drożdż, S., Forczek, M., Jadach, S., and Kwapień, J. (2014), 'Detrended cross-correlation analysis consistently extended to multifractality', Physical Review E, 89(2), 023305.
- Podobnik, B., and Stanley, H. E. (2008), 'Detrended cross-correlation analysis: a new method for analyzing two nonstationary time series', Physical Review Letters, 100(8), 084102.
- Peters, E. E. (1994), 'Fractal market analysis: applying chaos theory to investment and economics', John Wiley & Sons.
- Li, H., Chun, W., Wu, X., and Luo, L. (2024), 'Multi-asset portfolio model optimization based on mean multifractal detrended cross correlation analysis', Mathematical and Computer Modelling of Dynamical Systems, 30(1), 736–757.
