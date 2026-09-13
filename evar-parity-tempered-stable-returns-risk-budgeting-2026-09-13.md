---
schema: strategy-research-record-v1
title: "Entropic Value-at-Risk Parity for Tempered Stable Returns: MNTS and ICA Risk Budgeting Under Non-Gaussian Tails"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - portfolio-allocation
  - risk-parity
  - entropic-value-at-risk
  - tempered-stable
  - mnts
  - ica
  - tail-risk
  - equal-risk-contribution
  - non-gaussian
  - transaction-costs
status: research-only
confidence: medium
source_as_of: 2026-09-11
sources:
  - "Jaehyung Choi, 'Entropic Value-at-Risk parity for tempered stable returns', arXiv:2609.11905v1 [q-fin.PM, q-fin.RM, stat.AP], September 11, 2026. https://arxiv.org/abs/2609.11905"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Entropic Value-at-Risk Parity for Tempered Stable Returns: MNTS and ICA Risk Budgeting Under Non-Gaussian Tails

## Provenance

- **Primary Source:** Jaehyung Choi (`jj.jaehyung.choi@gmail.com`), *"Entropic Value-at-Risk parity for tempered stable returns"*, arXiv preprint `arXiv:2609.11905v1 [q-fin.PM, q-fin.RM, stat.AP]`, submitted September 11, 2026.
  - Stable arXiv URL: https://arxiv.org/abs/2609.11905
  - Full-text HTML: https://arxiv.org/html/2609.11905v1
  - Full-text PDF: https://arxiv.org/pdf/2609.11905v1
  - Canonical DOI: [10.48550/arXiv.2609.11905](https://doi.org/10.48550/arXiv.2609.11905)
  - License: arXiv.org perpetual non-exclusive license.
- **Verification Integrity:** This record was generated following direct, full-text examination of the preprint mathematical derivations (Section 2 and 3), Propositions 1–3, Corollary 1, and empirical backtest evaluations (Section 4, Tables 1–6). No search snippets, third-party marketing summaries, or model-generated synthetic summaries were used to extract strategy rules, mathematical formulas, or quantitative findings.
- **Repository Deduplication:** Pre-write search across all records in `alpha-strategy-research` confirmed zero prior records citing `arXiv:2609.11905`, Jaehyung Choi's EVaR parity paper, or tempered stable EVaR risk budgeting. Adjacent record `deepm-regime-robust-macro-graph-causal-sieve-evar-2026-09-03.md` (Wood, Roberts, Zohren 2026, arXiv:2601.05975) applies EVaR within a deep neural network softmin objective on macro futures; it does not investigate parametric tempered stable distributions, Euler risk contributions, EVaR deviation location separation, or Inverse Risk Parity / Equal Risk Contribution portfolios.

## Economic mechanism

### Source-reported

Conventional risk parity frameworks (Inverse Risk Parity [IRP] and Equal Risk Contribution [ERC]; Qian 2011, Maillard et al. 2010) allocate portfolio weights based on standalone or marginal volatility under the implicit assumption of symmetric, Gaussian asset returns. However, empirical financial returns exhibit significant skewness, excess kurtosis, heavy tails, and nonlinear tail dependence. Volatility penalizes positive and negative deviations symmetrically and fails to capture catastrophic tail risk.

Entropic Value-at-Risk (EVaR; Ahmadi-Javid 2012) is the tightest coherent risk measure upper-bounding both Value-at-Risk (VaR) and Conditional Value-at-Risk (CVaR) obtained from the Chernoff inequality:
$$\mathrm{EVaR}_{1-\eta}(L) = \inf_{u > 0} \left\{ u^{-1} (\ln M_L(u) - \ln \eta) \right\}$$
where $M_L(u) = \mathbb{E}[e^{uL}]$ is the moment-generating function (MGF) of loss $L = -X$. 

The author posits that by integrating EVaR with flexible parametric tempered stable distributions—specifically Multivariate Normal Tempered Stable (MNTS) and Independent Component Analysis with Tempered Stable components (ICA+NTS and ICA+CTS)—risk parity portfolios can allocate capital based on true asymmetric tail risk rather than symmetric variance. Furthermore, because EVaR is translation equivariant, its Euler risk contributions conflate directional expected return (the fitted location parameter $\boldsymbol{\mu}$) with tail dispersion. By introducing the **EVaR deviation**:
$$\mathcal{D}_\eta^c(\boldsymbol{w}) = \inf_{u > 0} \left\{ u^{-1} \left( \Psi_{\boldsymbol{X}^c}(-u\boldsymbol{w}) - \ln \eta \right) \right\}, \quad \boldsymbol{X}^c = \boldsymbol{X} - \boldsymbol{\mu}$$
the framework isolates pure tail-risk budgeting from expected-return drift. Under Gaussianity, EVaR-deviation ERC recovers conventional volatility ERC exactly (Corollary 1).

### Research interpretation

The core economic hypothesis is that equalizing tail risk contributions (EVaR-ERC) under heavy-tailed tempered stable distributions improves risk-adjusted returns relative to naive equal weighting by penalizing assets with asymmetric left-tail crash vulnerability. 

However, the empirical findings reveal an essential economic and market-microstructure nuance:
1. **The Volatility Parity Ceiling:** While EVaR-ERC portfolios significantly outperform equal-weight portfolios across multi-asset, sector, and momentum universes, they offer almost no statistically significant improvement over conventional Gaussian volatility ERC. Tail-risk budgeting largely tracks volatility budgeting in broad equity/ETF universes because assets with severe tail risk also have high realized volatility.
2. **The Turnover/Friction Trap of Higher-Moment Parity:** When higher-moment tail differences do emerge (e.g., ICA-based EVaR-ERC in momentum deciles), the portfolio sensitivity to higher cumulants induces substantial weight turnover (2.5× to 4.5× that of matched CVaR or Gaussian portfolios). Under realistic transaction costs ($\ge 10\text{–}25$ bps), any gross Sharpe ratio advantage is dissipated by rebalancing friction.
3. **Location Invariance:** Removing the fitted location term (EVaR deviation vs raw EVaR) produces statistically indistinguishable portfolio Sharpe ratios ($p \in [0.151, 0.993]$), demonstrating that empirical 12-month trailing return drift does not distort monthly tail-risk allocation.

## Signal

### Mathematical Signal Construction

All portfolios are fully invested, long-only equity/ETF allocations with weights $\boldsymbol{w} \in \Delta_N = \left\{ \boldsymbol{w} \in \mathbb{R}^N : \boldsymbol{w}^\top \boldsymbol{e} = 1, \, w_i \ge 0 \right\}$ (`source-reported`).

#### 1. Standalone and Portfolio EVaR
Let $\boldsymbol{X} = (X^{(1)}, \dots, X^{(N)})^\top$ denote asset returns over horizon $t=1$.
- Standalone asset EVaR (`source-reported`):
  $$\mathcal{D}_{\eta, i} = \inf_{u > 0} \left\{ u^{-1} \left( \Psi_{X^{(i)}}(-u) - \ln \eta \right) \right\}$$
- Portfolio EVaR (`source-reported`):
  $$\mathcal{D}_\eta(\boldsymbol{w}) = \inf_{u > 0} \left\{ u^{-1} \left( \Psi_{\boldsymbol{X}}(-u\boldsymbol{w}) - \ln \eta \right) \right\}$$
  where $\Psi_{\boldsymbol{X}}(\boldsymbol{z}) = \ln \mathbb{E}[e^{\boldsymbol{z}^\top \boldsymbol{X}}]$ is the joint cumulant-generating function (CGF).

#### 2. Inverse Risk Parity (EVaR-IRP)
When all standalone $\mathcal{D}_{\eta, i} > 0$, weights are normalized inversely to standalone EVaR (`source-reported`):
$$w_i^{\mathrm{IRP}} = \frac{\mathcal{D}_{\eta, i}^{-1}}{\sum_{j=1}^N \mathcal{D}_{\eta, j}^{-1}}$$

#### 3. Equal Risk Contribution (EVaR-ERC)
Euler's homogeneous function theorem decomposes total portfolio EVaR into asset contributions (`source-reported`):
$$\mathcal{D}_\eta(\boldsymbol{w}) = \sum_{i=1}^N \mathrm{EVaRC}_{\eta, i}(\boldsymbol{w}), \quad \mathrm{EVaRC}_{\eta, i}(\boldsymbol{w}) = w_i \frac{\partial \mathcal{D}_\eta(\boldsymbol{w})}{\partial w_i}$$
The EVaR-ERC portfolio satisfies (`source-reported`):
$$\mathrm{EVaRC}_{\eta, i}(\boldsymbol{w}) = \mathrm{EVaRC}_{\eta, j}(\boldsymbol{w}) = \frac{1}{N} \mathcal{D}_\eta(\boldsymbol{w}) \quad \forall i, j \in \{1, \dots, N\}$$

#### 4. EVaR Deviation (Location Separation)
Let $\boldsymbol{\mu} = \mathbb{E}[\boldsymbol{X}]$ and $\boldsymbol{X}^c = \boldsymbol{X} - \boldsymbol{\mu}$. The EVaR deviation removes location drift (`source-reported`):
$$\mathcal{D}_\eta^c(\boldsymbol{w}) = \mathcal{D}_\eta(\boldsymbol{w}) - \boldsymbol{w}^\top \boldsymbol{\mu}$$
Euler contributions satisfy (`source-reported`, Proposition 1):
$$\mathrm{DEVaRC}_{\eta, i}(\boldsymbol{w}) = \mathrm{EVaRC}_{\eta, i}(\boldsymbol{w}) + w_i \mu_i$$
Under Gaussian returns $\boldsymbol{X} \sim N(\boldsymbol{\mu}, \boldsymbol{\Omega})$ (`source-reported`, Corollary 1):
$$\mathcal{D}_\eta^c(\boldsymbol{w}) = k_\eta \sqrt{\boldsymbol{w}^\top \boldsymbol{\Omega} \boldsymbol{w}}, \quad k_\eta = \sqrt{-2\ln\eta}$$
$$\mathrm{DEVaRC}_{\eta, i}(\boldsymbol{w}) = k_\eta \cdot \frac{w_i (\boldsymbol{\Omega}\boldsymbol{w})_i}{\sqrt{\boldsymbol{w}^\top \boldsymbol{\Omega} \boldsymbol{w}}}$$
yielding portfolio weights identical to conventional volatility IRP and ERC.

#### 5. Distributional Specifications & Risk Contributions
- **MNTS Model (`source-reported`):** Parameters $(\alpha, \theta, \boldsymbol{\beta}, \boldsymbol{\gamma}, \boldsymbol{\mu}, \boldsymbol{\rho})$ where $\alpha$ and $\theta$ are common NTS shape parameters, $\boldsymbol{\beta}$ is the time-change loading vector, $\boldsymbol{\gamma}$ is the diffusion-scale vector, $\boldsymbol{\mu}$ is location, and $\boldsymbol{\rho}$ is Brownian correlation.
  - Portfolio remains NTS under linear aggregation.
  - Interior Euler contribution (`source-reported`, Proposition 2):
    $$\mathrm{EVaRC}_{\eta, i}^{\mathrm{MNTS}}(\boldsymbol{w}) = w_i \left[ -\mu_i + (g^\star)^{\alpha/2-1} \left\{ \beta_i + u^\star (\boldsymbol{\Sigma}\boldsymbol{w})_i \right\} \right]$$
    where $\boldsymbol{\Sigma} = \mathrm{diag}(\boldsymbol{\gamma}) \boldsymbol{\rho} \, \mathrm{diag}(\boldsymbol{\gamma})$, $g^\star = 1 - 2\theta^{-1} u^\star (\boldsymbol{w}^\top \boldsymbol{\beta}) - \theta^{-1} (u^\star)^2 (\boldsymbol{w}^\top \boldsymbol{\Sigma}\boldsymbol{w})$, and $u^\star(\boldsymbol{w})$ is the optimal EVaR minimizer.
- **ICA Model (`source-reported`):** $\boldsymbol{X} = \boldsymbol{m} + \mathbf{A}\boldsymbol{S}$, where independent components $S^{(j)}$ are fitted to NTS or CTS laws.
  - Interior Euler contribution (`source-reported`, Proposition 3):
    $$\mathrm{EVaRC}_{\eta, i}^{\mathrm{ICA}}(\boldsymbol{w}) = w_i \left[ -m_i - \sum_{j=1}^J A_{ij} \Psi'_{S^{(j)}}(-u^\star \tilde{w}_j) \right], \quad \tilde{\boldsymbol{w}} = \mathbf{A}^\top \boldsymbol{w}$$
  - Contrast with CVaR: EVaR uses an Esscher-type exponentially tilted component mean $\xi_{\eta, j}^{\mathrm{EVaR}}(\boldsymbol{w}) = \Psi'_{S^{(j)}}(-u^\star \tilde{w}_j)$, whereas CVaR uses the lower-tail conditional component mean $\tau_{\eta, j}(\boldsymbol{w}) = \mathbb{E}[S^{(j)} \mid \sum_k \tilde{w}_k S^{(k)} \le q_\eta^S(\boldsymbol{w})]$.
- **Finite-Difference Implementation (`source-reported`):**
  To accommodate boundary solutions and weight-dependent MGF domain endpoints:
  $$\frac{\partial \mathcal{D}_\eta^\mathcal{A}(\boldsymbol{w})}{\partial w_i} \approx \frac{\mathcal{D}_\eta^\mathcal{A}(\boldsymbol{w} + h \boldsymbol{e}_i) - \mathcal{D}_\eta^\mathcal{A}(\boldsymbol{w} - h \boldsymbol{e}_i)}{2h}$$
  Numerical Euler contribution: $\mathrm{EVaRC}_{\eta, i}^\mathcal{A}(\boldsymbol{w}) = w_i \cdot \frac{\partial \mathcal{D}_\eta^\mathcal{A}(\boldsymbol{w})}{\partial w_i}$.

### Strategy Operational Rules

- **Signal Cadence & Rebalancing:** Monthly rebalancing at month-end (`source-reported`). Specific execution bar/time (e.g. month-end close vs month-start open) is unspecified in the text; labeled `research-proposed` as month-end close-to-open rebalancing.
- **Estimation Window:** Trailing 12 months (252 trading days) of daily returns used to fit distribution parameters at each rebalance date (`source-reported`).
- **Tail Probability ($\eta$):** $\eta = 0.05$ (corresponding to a 95% confidence level for EVaR and CVaR) (`source-reported`).
- **Constraints:** Long-only, fully invested ($\sum w_i = 1$, $w_i \ge 0$) (`source-reported`). No leverage, shorting, or cash buffer (`source-reported`).
- **Numerical Step Size ($h$):** Standard coordinate perturbation step size for central finite difference; labeled `research-proposed` as $h = 10^{-5}$ if unspecified by user implementation.

## Required data

- **Instruments & Universes (`source-reported`):**
  1. **XASSET (Cross-Asset ETFs, $N=7$):**
     - VTI (Vanguard Total Stock Market ETF)
     - EFA (iShares MSCI EAFE ETF)
     - VWO (Vanguard FTSE Emerging Markets ETF)
     - VNQ (Vanguard Real Estate ETF)
     - AGG (iShares Core U.S. Aggregate Bond ETF)
     - TIP (iShares TIPS Bond ETF)
     - GLD (SPDR Gold Shares)
     - Sample: April 1, 2005 to March 31, 2026. Out-of-sample backtest: April 2006 to March 2026 (20 years). Source: Yahoo Finance.
  2. **MOM10 (Momentum Deciles, $N=10$):**
     - 10 value-weighted momentum-sorted decile portfolios based on prior 12–2 returns (Jegadeesh & Titman 1993).
     - Sample: January 1995 to March 2026. Out-of-sample backtest: January 1996 to March 2026 (30+ years). Source: Kenneth R. French Data Library at Dartmouth College.
  3. **SECTOR (Select Sector SPDR ETFs, $N=9\text{ to }11$):**
     - Original 9 sectors (January 2000 to March 2026): XLB, XLE, XLF, XLI, XLK, XLP, XLU, XLV, XLY.
     - XLRE (Real Estate) enters October 2015; XLC (Communication Services) enters June 2018.
     - Sample: January 2000 to March 2026 (26+ years). Source: Yahoo Finance.
- **Data Fields:** Adjusted daily close prices and dividend-reinvested total returns (`source-reported`).
- **Point-in-Time & Survivorship Handling:**
  - For SECTOR, assets are added dynamically upon availability (XLRE in Oct 2015, XLC in Jun 2018), requiring full 12-month lookback history before becoming eligible (`source-reported`).
  - MOM10 series is survivorship-bias controlled by the French Library database construction (`source-reported`).
  - Yahoo Finance adjusted close data accounts for stock splits and dividend distributions (`source-reported`).

## Execution assumptions

- **Order Execution Mode:** Market-on-open or market-on-close rebalancing once per month (`source-reported` as monthly rebalancing; execution timestamp labeled `research-proposed`).
- **Turnover Definition:** Drift-adjusted one-way turnover per monthly rebalance:
  $$\mathrm{TO}_t = \frac{1}{2} \sum_{i=1}^N |w_{i, t} - w_{i, t^-}|$$
  where $w_{i, t^-}$ represents the market-drifted weight immediately prior to rebalancing (`source-reported`).
- **Transaction Cost Schedule:** Evaluated across four explicit cost tiers: 0 bps, 5 bps, 10 bps, and 25 bps per unit of one-way turnover (`source-reported`).
- **Borrow, Margin & Leverage:** Zero borrow, zero leverage, zero shorting (`source-reported`).
- **Capacity & Market Impact:** In broad U.S. ETFs (VTI, AGG, GLD, SPDR sectors), monthly turnover of 2%–12% on liquid multi-billion-dollar vehicles implies substantial capacity ($> \$100\text{M}$); market impact is negligible at standard institutional sizing at monthly frequency (`research-proposed`).

## Evidence

### Source-reported

All performance figures below are directly extracted from Choi (2026, arXiv:2609.11905v1, Tables 2–6). Statistical significance is assessed via two-sided $p$-values computed with a studentized circular block bootstrap following Ledoit & Wolf (2008, Section 3) with $B=4,999$ resamples and block length $L = \lfloor T^{1/3} \rfloor$:

#### 1. Benchmark Comparison Against Equal Weight (Table 2)
- **SECTOR (2000–2026, $T=26\text{ yrs}$):**
  - Equal Weight: Benchmark
  - MNTS IRP: $\Delta\mathrm{CAGR} = -0.03\%$, $\Delta\mathrm{Vol} = -0.99\%$, $\Delta\mathrm{SR} = +0.019$ ($p=0.200$)
  - ICA+NTS IRP: $\Delta\mathrm{CAGR} = +0.05\%$, $\Delta\mathrm{Vol} = -0.90\%$, $\Delta\mathrm{SR} = +0.021$ ($p=0.216$)
  - ICA+CTS IRP: $\Delta\mathrm{CAGR} = +0.02\%$, $\Delta\mathrm{Vol} = -0.92\%$, $\Delta\mathrm{SR} = +0.020$ ($p=0.290$)
  - MNTS ERC: $\Delta\mathrm{CAGR} = -0.05\%$, $\Delta\mathrm{Vol} = -1.14\%$, $\Delta\mathrm{SR} = +0.022$ ($p=0.209$)
  - ICA+NTS ERC: $\Delta\mathrm{CAGR} = +0.55\%$, $\Delta\mathrm{Vol} = -1.00\%$, $\Delta\mathrm{SR} = \mathbf{+0.051}$ ($p=\mathbf{0.023}$)
  - ICA+CTS ERC: $\Delta\mathrm{CAGR} = +0.41\%$, $\Delta\mathrm{Vol} = -0.96\%$, $\Delta\mathrm{SR} = \mathbf{+0.042}$ ($p=\mathbf{0.059}$)
- **MOM10 (1996–2026, $T=30\text{ yrs}$):**
  - MNTS IRP: $\Delta\mathrm{CAGR} = +0.00\%$, $\Delta\mathrm{Vol} = -0.82\%$, $\Delta\mathrm{SR} = +0.015$ ($p=0.238$)
  - ICA+NTS IRP: $\Delta\mathrm{CAGR} = +0.12\%$, $\Delta\mathrm{Vol} = -0.83\%$, $\Delta\mathrm{SR} = +0.021$ ($p=0.136$)
  - ICA+CTS IRP: $\Delta\mathrm{CAGR} = +0.24\%$, $\Delta\mathrm{Vol} = -0.83\%$, $\Delta\mathrm{SR} = \mathbf{+0.026}$ ($p=\mathbf{0.076}$)
  - MNTS ERC: $\Delta\mathrm{CAGR} = -0.16\%$, $\Delta\mathrm{Vol} = -0.78\%$, $\Delta\mathrm{SR} = +0.007$ ($p=0.552$)
  - ICA+NTS ERC: $\Delta\mathrm{CAGR} = +0.28\%$, $\Delta\mathrm{Vol} = -0.79\%$, $\Delta\mathrm{SR} = \mathbf{+0.028}$ ($p=\mathbf{0.052}$)
  - ICA+CTS ERC: $\Delta\mathrm{CAGR} = +0.39\%$, $\Delta\mathrm{Vol} = -0.79\%$, $\Delta\mathrm{SR} = \mathbf{+0.032}$ ($p=\mathbf{0.035}$)
- **XASSET (2006–2026, $T=20\text{ yrs}$):**
  - MNTS IRP: $\Delta\mathrm{CAGR} = -1.50\%$, $\Delta\mathrm{Vol} = -5.68\%$, $\Delta\mathrm{SR} = \mathbf{+0.177}$ ($p=\mathbf{0.016}$)
  - ICA+NTS IRP: $\Delta\mathrm{CAGR} = -1.41\%$, $\Delta\mathrm{Vol} = -5.16\%$, $\Delta\mathrm{SR} = \mathbf{+0.142}$ ($p=\mathbf{0.057}$)
  - ICA+CTS IRP: $\Delta\mathrm{CAGR} = -2.27\%$, $\Delta\mathrm{Vol} = -2.95\%$, $\Delta\mathrm{SR} = -0.077$ ($p=0.710$)
  - MNTS ERC: $\Delta\mathrm{CAGR} = -1.52\%$, $\Delta\mathrm{Vol} = -6.37\%$, $\Delta\mathrm{SR} = \mathbf{+0.246}$ ($p=\mathbf{0.011}$)
  - ICA+NTS ERC: $\Delta\mathrm{CAGR} = -1.45\%$, $\Delta\mathrm{Vol} = -5.53\%$, $\Delta\mathrm{SR} = \mathbf{+0.170}$ ($p=\mathbf{0.086}$)
  - ICA+CTS ERC: $\Delta\mathrm{CAGR} = -1.52\%$, $\Delta\mathrm{Vol} = -4.77\%$, $\Delta\mathrm{SR} = +0.100$ ($p=0.511$)

#### 2. Comparison Against Gaussian EVaR (Volatility Parity Benchmark) (Table 3)
- In SECTOR and XASSET, neither MNTS nor ICA specifications produce statistically significant Sharpe improvements over Gaussian EVaR (volatility parity) in gross or net terms ($p > 0.10$).
- In MOM10 ERC, ICA+NTS and ICA+CTS exhibit gross Sharpe improvements of $+0.014$ ($p=0.041$) and $+0.019$ ($p=0.057$). However, after 25 bps transaction costs, the net improvements shrink to $+0.008$ ($p=0.218$) and $+0.009$ ($p=0.370$), losing statistical significance.
- MNTS ERC in MOM10 underperforms Gaussian EVaR by $-0.007$ in both gross and net Sharpe ($p=0.073$ and $p=0.063$).

#### 3. Matched EVaR vs. CVaR Comparisons (Table 4)
Holding the return distribution model and risk parity rule identical:
- Under **MNTS**, EVaR and CVaR Sharpe ratios are nearly identical across all universes:
  - SECTOR ERC: $\Delta\mathrm{SR} = -0.001$ ($p=0.642$)
  - MOM10 ERC: $\Delta\mathrm{SR} = -0.003$ ($p=0.179$)
  - XASSET ERC: $\Delta\mathrm{SR} = +0.006$ ($p=0.651$)
- Under **ICA**, differences are larger but inconsistent and sign-flipping across universes:
  - MOM10 ICA+NTS ERC: $\Delta\mathrm{SR} = +0.015$ ($p=0.028$)
  - MOM10 ICA+CTS ERC: $\Delta\mathrm{SR} = +0.018$ ($p=0.065$)
  - SECTOR ICA+NTS ERC: $\Delta\mathrm{SR} = +0.028$ ($p=0.110$)
  - XASSET ICA+NTS ERC: $\Delta\mathrm{SR} = -0.061$ ($p=0.440$)
  - XASSET ICA+CTS ERC: $\Delta\mathrm{SR} = -0.126$ ($p=0.474$), with EVaR suffering larger Max Drawdown (34.56% vs 20.93%).

#### 4. Turnover & Transaction Cost Friction (Tables 5 & 6)
- Monthly turnover is substantially higher for ICA-based EVaR-ERC than matched CVaR-ERC:
  - SECTOR ICA+NTS: EVaR turnover $6.93\%$ vs CVaR turnover $2.93\%$.
  - MOM10 ICA+NTS: EVaR turnover $5.27\%$ vs CVaR turnover $1.96\%$.
  - XASSET ICA+NTS: EVaR turnover $8.52\%$ vs CVaR turnover $3.98\%$.
  - ICA+CTS turnover reaches $9.49\%$ (SECTOR), $8.09\%$ (MOM10), and $12.76\%$ (XASSET).
- As transaction costs scale from 0 bps to 25 bps, the MOM10 ICA ERC advantage collapses:
  - ICA+NTS: from $+0.015$ ($p=0.028$ at 0 bps) $\to +0.014$ ($p=0.040$ at 5 bps) $\to +0.013$ ($p=0.055$ at 10 bps) $\to +0.010$ ($p=0.140$ at 25 bps).
  - ICA+CTS: from $+0.018$ ($p=0.065$ at 0 bps) $\to +0.016$ ($p=0.101$ at 5 bps) $\to +0.014$ ($p=0.147$ at 10 bps) $\to +0.009$ ($p=0.373$ at 25 bps).

#### 5. EVaR Deviation vs Raw EVaR (Fitted Location Separation) (Table 6)
- Removing the fitted location term yields negligible full-sample Sharpe ratio changes across all universes and specifications:
  - SECTOR MNTS ERC: $\Delta\mathrm{SR} = -0.001$ ($p=0.512$)
  - SECTOR ICA+NTS ERC: $\Delta\mathrm{SR} = +0.004$ ($p=0.265$)
  - MOM10 MNTS ERC: $\Delta\mathrm{SR} = +0.006$ ($p=0.434$)
  - MOM10 ICA+NTS ERC: $\Delta\mathrm{SR} = -0.000$ ($p=0.537$)
  - XASSET MNTS ERC: $\Delta\mathrm{SR} = -0.003$ ($p=0.637$)
  - XASSET ICA+NTS ERC: $\Delta\mathrm{SR} = +0.003$ ($p=0.921$)
  - XASSET ICA+CTS ERC: $\Delta\mathrm{SR} = -0.037$ ($p=0.377$)
- None of the raw EVaR vs EVaR-deviation Sharpe differences have $p < 0.10$ ($p$-values range from 0.151 to 0.993), confirming that empirical location drift does not drive risk parity weights.

### Independently reproduced

Not independently reproduced. All figures and performance metrics represent third-party reported findings from Choi (arXiv:2609.11905v1, September 2026).

### Negative evidence

1. **No Robust Alpha Over Volatility Parity:** Across multi-asset (XASSET) and sector (SECTOR) universes, the sophisticated MNTS, ICA+NTS, and ICA+CTS EVaR-ERC models fail to achieve statistically significant Sharpe ratio outperformance over a simple Gaussian volatility ERC benchmark.
2. **Turnover Friction Dissipation:** While gross Sharpe ratios in MOM10 show a marginal boost for ICA-based EVaR over CVaR (+0.015 to +0.018), this advantage is entirely attributable to aggressive weight reallocation that produces 2.5× to 4.5× higher turnover. At 25 bps friction, the advantage drops below statistical significance ($p > 0.14$).
3. **Severe Multi-Asset Drawdown Vulnerability:** In the cross-asset ETF universe (XASSET), ICA+CTS EVaR-ERC experiences a catastrophic maximum drawdown of 34.56%, compared to only 20.93% for matched CVaR-ERC and 20.57% for MNTS EVaR-ERC, demonstrating severe instability in independent component tail fitting under mixed asset classes.
4. **Lack of Uniform EVaR Dominance:** In direct MNTS modeling, the EVaR–CVaR Sharpe differences are practically zero ($-0.003$ to $+0.006$, all $p > 0.17$), proving that EVaR does not provide an empirical tail-hedging advantage over standard CVaR within elliptical/projected tempered stable structures.

## Falsification plan

To falsify the hypothesis that EVaR-based parity provides genuine tail-risk alpha beyond conventional volatility parity:

1. **Transaction Cost Barrier Test (`research-defined falsification threshold`):**
   - *Protocol:* Rebalance monthly on MOM10 and SECTOR universes applying realistic execution costs ($10\text{ bps}$, $20\text{ bps}$, and $30\text{ bps}$).
   - *Falsification Condition:* If net Sharpe ratio difference $\Delta\mathrm{SR}_{\mathrm{net}}(\mathrm{EVaR\text{-}ERC} - \mathrm{Vol\text{-}ERC}) \le 0.0$ at $\ge 15\text{ bps}$ friction, the hypothesis of tradable tail-risk alpha is falsified.
2. **Ledoit-Wolf Multiple-Testing Correction (`research-defined falsification threshold`):**
   - *Protocol:* Adjust the pairwise bootstrap $p$-values across the 18 model-universe comparisons using the Romano-Wolf or Benjamini-Hochberg False Discovery Rate (FDR) control at $q = 0.05$.
   - *Falsification Condition:* If zero EVaR-ERC specifications survive multiple-testing adjustment relative to the Gaussian benchmark, the reported gross advantages are classified as data-snooping noise.
3. **Out-of-Sample Rolling Horizon Shift (`research-defined falsification threshold`):**
   - *Protocol:* Perturb the rolling estimation lookback window from 12 months to 6, 9, 18, and 24 months.
   - *Falsification Condition:* If EVaR-ERC underperforms conventional volatility ERC across $> 50\%$ of lookback perturbations, parameter instability falsifies the model.
4. **Synthetic Heavy-Tail Placebo Experiment (`research-defined falsification threshold`):**
   - *Protocol:* Generate synthetic multivariate Gaussian returns matching the empirical covariance matrix of XASSET and evaluate whether fitted MNTS/ICA EVaR-ERC produces spurious weight deviations and turnover drag.
   - *Falsification Condition:* If EVaR-ERC generates $> 5\%$ monthly turnover on purely Gaussian data with lower Sharpe ratio than sample ERC, the estimation methodology is rejected as overfitting.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Mechanism Portability Assessment:**
  The mathematical principles of Entropic Value-at-Risk and tempered stable modeling are asset-class agnostic and theoretically well-suited to cryptocurrency markets, which exhibit extreme non-Gaussianity, negative skewness, volatility clustering, and heavy power-law tails. However, direct transfer of monthly rebalancing across spot/perpetual tokens introduces severe crypto-specific operational frictions:
  1. **Continuous 24/7 Trading & Intraday Jumps:** Monthly rebalancing with 12-month lookback is ill-suited to crypto cycles, where regime changes occur over days rather than quarters. Adapting to weekly or daily rebalancing would dramatically inflate turnover.
  2. **Perpetual Funding Rate Drag:** In crypto perpetuals, equalizing tail-risk contributions ignores 8-hour funding rates. If an asset with low EVaR carries persistent high negative funding, the parity allocation will suffer negative cash-flow carry.
  3. **High Crypto Execution Friction:** Crypto spot and perpetual maker/taker fees (typically 2 to 5 bps VIP, 5 to 10 bps retail) plus bid-ask spreads (10 to 50 bps on mid/small-cap altcoins) exceed the 25 bps threshold where Choi demonstrated EVaR advantages evaporate.
  4. **Dynamic Universe & Delisting Hazard:** Crypto tokens frequently undergo hyper-inflationary emissions, protocol collapses, or exchange delistings, violating the continuous parameter continuity assumed by MNTS/ICA.
- **Porting Protocol (`research-proposed`):** Any crypto implementation must operate as an adapted multi-asset basket overlay on liquid majors (BTC, ETH, SOL) with weekly rebalancing, funding-adjusted net returns, and explicit turnover constraints ($\le 5\%$ per rebalance).

## Limitations

- **Traditional Asset Sample Only:** The empirical study evaluates traditional equity and multi-asset ETFs (Yahoo Finance and French Library); zero cryptocurrency empirical testing is conducted in the source paper.
- **Parametric Estimation Overhead:** Fitting MNTS (shape parameters $\alpha, \theta$, loading vector $\boldsymbol{\beta}$, covariance $\boldsymbol{\Sigma}$) and ICA mixing matrices at every monthly step is computationally intensive and subject to local-minima optimizer traps.
- **High Sensitivity to Estimation Window:** 12 months of daily data (252 observations) is a short sample for estimating higher-order tail parameters ($\alpha, \theta$, skewness $\boldsymbol{\beta}$), introducing estimation noise that manifests as excess turnover.
- **Absence of Trading Slippage & Market Impact:** The study applies flat proportional costs (0–25 bps) but does not model order-book depth, bid-ask spreads, or market impact.
- **Not Independently Reproduced:** All performance numbers trace exclusively to Choi (2026); independent code replication has not yet been executed in our research stack.

## Implementation status

`not-implemented`.

This research record represents an external quantitative research capture only. No component of the EVaR-parity, MNTS parameter fitting, ICA component decomposition, or finite-difference Euler budgeting has been implemented or backtested in PyBroker, NautilusTrader, Paper, Testnet, or Live systems.

## Adoption boundary

`not-approved` (`research-only`).

The presence of this record in `alpha-strategy-research` does not constitute:
- Strategy validation or verification of statistical profitability;
- Approval for portfolio implementation;
- Permission or readiness for Paper, Testnet, or Live capital deployment.

Any future consideration for research progression requires independent reproduction, out-of-sample audit post-March 2026, and strict transaction-cost attribution.

## Related Wiki records

- `[[quant/crypto-cross-sectional-amihud-illiquidity-premium-2026-08-31]]` — Tail risk and illiquidity pricing across crypto assets.
- `[[quant/deepm-regime-robust-macro-graph-causal-sieve-evar-2026-09-03]]` — Deep learning macro futures optimization under softmin EVaR objectives.
- `[[quant/expected-shortfall-factor-model-common-tail-loss-severity-2026-09-11]]` — Tail-risk factor pricing and expected shortfall loss severity models.
- `[[quant/simple-dynamic-stock-bond-gold-markowitz-volatility-control-2026-09-11]]` — Dynamic ETF multi-asset allocation benchmarks and volatility targeting.
- `[[quant/conformal-kelly-prediction-intervals-fractional-sizing-2026-02]]` — Robust sizing and uncertainty budgeting under non-Gaussian return distributions.

## Sources

1. Jaehyung Choi, *"Entropic Value-at-Risk parity for tempered stable returns"*, arXiv preprint `arXiv:2609.11905v1 [q-fin.PM, q-fin.RM, stat.AP]`, submitted September 11, 2026.
   - Stable arXiv URL: https://arxiv.org/abs/2609.11905
   - Full-text HTML: https://arxiv.org/html/2609.11905v1
   - Full-text PDF: https://arxiv.org/pdf/2609.11905v1
   - Canonical DOI: [10.48550/arXiv.2609.11905](https://doi.org/10.48550/arXiv.2609.11905)
2. Amir Ahmadi-Javid, *"Entropic value-at-risk: A new coherent risk measure"*, Journal of Optimization Theory and Applications, 155:1105–1123, 2012. DOI: 10.1007/s10957-011-9923-6.
3. Sébastien Maillard, Thierry Roncalli, and Jérôme Teïletche, *"The properties of equally weighted risk contribution portfolios"*, Journal of Portfolio Management, 36(4):60–70, 2010. DOI: 10.3905/jpm.2010.36.4.060.
4. Young Shin Kim, *"Portfolio optimization and marginal contribution to risk on multivariate normal tempered stable model"*, Annals of Operations Research, 312(2):853–881, 2022. DOI: 10.1007/s10479-021-04432-8.
5. Olivier Ledoit and Michael Wolf, *"Robust performance hypothesis testing with the Sharpe ratio"*, Journal of Empirical Finance, 15(5):850–859, 2008. DOI: 10.1016/j.jempfin.2008.03.002.
