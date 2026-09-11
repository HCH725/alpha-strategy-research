---
schema: strategy-research-record-v1
title: "Entropic Value-at-Risk Parity for Tempered Stable Returns — EVaR-Based Inverse Risk Parity and Equal Risk Contribution (Choi 2026)"
created: 2026-09-11
updated: 2026-09-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - portfolio-optimization
  - risk-parity
  - entropic-value-at-risk
  - equal-risk-contribution
  - tempered-stable
  - mnts
  - ica
  - tail-risk
status: research-only
confidence: medium
source_as_of: 2026-09-11
sources:
  - "Jaehyung Choi, 'Entropic Value-at-Risk parity for tempered stable returns', arXiv:2609.11905v1 [q-fin.PM, q-fin.RM], submitted 11 September 2026. Stable URL: https://arxiv.org/abs/2609.11905. PDF: https://arxiv.org/pdf/2609.11905. HTML: https://arxiv.org/html/2609.11905v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Entropic Value-at-Risk Parity for Tempered Stable Returns — EVaR-Based Inverse Risk Parity and Equal Risk Contribution (Choi 2026)

## Provenance

- **Primary Source:** Jaehyung Choi, *"Entropic Value-at-Risk parity for tempered stable returns"*, arXiv preprint `arXiv:2609.11905v1 [q-fin.PM, q-fin.RM]`, submitted Friday, 11 September 2026.
- **Traceable Source URLs:**
  - Abstract: [https://arxiv.org/abs/2609.11905](https://arxiv.org/abs/2609.11905)
  - PDF: [https://arxiv.org/pdf/2609.11905](https://arxiv.org/pdf/2609.11905)
  - HTML Full Text: [https://arxiv.org/html/2609.11905v1](https://arxiv.org/html/2609.11905v1)
- **Author Contact:** Jaehyung Choi (`jj.jaehyung.choi@gmail.com`).
- **Primary Source Verification:** Direct full-text verification completed across all sections, mathematical proofs (Propositions 1–3, Corollary 1), and empirical performance tables (Tables 1–6).
- **Deduplication Audit:** Distinct in canonical source identity and mechanism from prior work `arXiv:2608.18022` (captured in `entropic-value-at-risk-tempered-stable-levy-portfolio-optimization-2026-09-02.md`). While `arXiv:2608.18022` addressed *direct portfolio optimization* (minimum-EVaR, E-STAR, and E-Rachev), this paper explicitly solves *risk budgeting and risk parity* (deriving asset-level Euler risk contributions, EVaR-IRP, EVaR-ERC, and location-free EVaR deviation).

## Economic mechanism

### Source-reported

Conventional risk parity constructs portfolio weights from risk characteristics rather than expected-return forecasts. Classical inverse risk parity (IRP) weights assets inversely to their standalone volatility, and equal risk contribution (ERC; Qian 2011; Maillard et al. 2010) equalizes volatility contributions across assets. However, variance-based risk parity treats upside and downside fluctuations symmetrically and fails to account for heavy tails, skewness, or non-Gaussian joint dependence.

Entropic Value-at-Risk (EVaR; Ahmadi-Javid 2012) is the tightest coherent upper bound on both Value-at-Risk (VaR) and Conditional Value-at-Risk (CVaR / Expected Shortfall) obtained from the Chernoff inequality. Defined as:
$$\mathcal{D}_\eta(\boldsymbol{w}) = \inf_{u > 0} \left\{ \frac{\Psi_{\boldsymbol{X}}(-u\boldsymbol{w}) - \ln \eta}{u} \right\}$$
where $\Psi_{\boldsymbol{X}}(\boldsymbol{z}) = \ln \mathbb{E}[e^{\boldsymbol{z}^\top \boldsymbol{X}}]$ is the cumulant-generating function (CGF), EVaR reflects the entire distribution tail via exponential tilting (the Esscher transform) and possesses a dual representation linked to relative entropy (Kullback-Leibler divergence).

The author develops EVaR-based risk budgeting for tempered stable distributions under two multivariate representations:
1. **Multivariate Normal Tempered Stable (MNTS) Projection:** Because the MNTS distribution is closed under linear portfolio aggregation, any portfolio $\boldsymbol{w}^\top \boldsymbol{X}$ remains analytically univariate NTS with parameters $(\alpha, \theta, \boldsymbol{w}^\top \boldsymbol{\beta}, \sqrt{\boldsymbol{w}^\top \boldsymbol{\Sigma} \boldsymbol{w}}, \boldsymbol{w}^\top \boldsymbol{\mu})$. The asset-level Euler contribution is derived analytically via the envelope theorem:
   $$\text{EVaRC}_{\eta, i}^{\text{MNTS}}(\boldsymbol{w}) = w_i \left( -\mu_i + \beta_i \{1 - (g^\star)^{\alpha/2-1}\} + u^\star (\boldsymbol{\Sigma}\boldsymbol{w})_i (g^\star)^{\alpha/2-1} \right)$$
   where $g^\star = 1 - \frac{2\theta u^\star \boldsymbol{w}^\top \boldsymbol{\beta}}{\alpha} - \frac{\theta (u^\star)^2 \boldsymbol{w}^\top \boldsymbol{\Sigma} \boldsymbol{w}}{\alpha}$.
2. **Independent Component Analysis (ICA) Factorization:** Assets are decomposed into statistically independent components $\boldsymbol{X} = \boldsymbol{m} + \mathbf{A}\boldsymbol{Y}$ with univariate NTS or Classical Tempered Stable (CTS) marginals. The Euler contribution is:
   $$\text{EVaRC}_{\eta, i}^{\text{ICA}}(\boldsymbol{w}) = w_i \left( -m_i - \sum_{j=1}^J A_{ij} \Psi'_{Y_j}(-u^\star \tilde{w}_j) \right)$$
   where $\tilde{\boldsymbol{w}} = \mathbf{A}^\top \boldsymbol{w}$.

Because EVaR is translation equivariant, raw EVaR Euler contributions incorporate the fitted location term $\boldsymbol{\mu}$. Centering returns ($\boldsymbol{X}^c = \boldsymbol{X} - \boldsymbol{\mu}$) defines the EVaR deviation $\mathcal{D}_\eta^c(\boldsymbol{w}) = \mathcal{D}_\eta(\boldsymbol{w}) - \boldsymbol{w}^\top \boldsymbol{\mu}$, with Euler contribution $\text{DEVaRC}_{\eta, i}(\boldsymbol{w}) = \text{EVaRC}_{\eta, i}(\boldsymbol{w}) - w_i \mu_i$. Under Gaussian returns, EVaR deviation is proportional to volatility ($k_\eta \sqrt{\boldsymbol{w}^\top \boldsymbol{\Omega} \boldsymbol{w}}$ where $k_\eta = \sqrt{-2\ln\eta}$), and EVaR-deviation IRP and ERC mathematically recover conventional volatility IRP and ERC.

Under ICA, the structural contrast between EVaR and CVaR Euler contributions is that EVaR weights components by their exponentially tilted (Esscher) mean $\xi_{\eta, j}^{\text{EVaR}}(\boldsymbol{w}) = \frac{\mathbb{E}[Y_j e^{-u^\star \tilde{w}_j Y_j}]}{\mathbb{E}[e^{-u^\star \tilde{w}_j Y_j}]}$, whereas CVaR weights components by their lower-tail conditional mean $\tau_{\eta, j}(\boldsymbol{w}) = \mathbb{E}[Y_j \mid \tilde{\boldsymbol{w}}^\top \boldsymbol{Y} \le q_\eta(\tilde{\boldsymbol{w}}^\top \boldsymbol{Y})]$.

### Research interpretation

The proposed alpha/risk mechanism is **asymmetric tail-risk equalization across non-Gaussian assets**. By equalizing EVaR Euler contributions rather than volatility:
- The portfolio shifts capital away from assets that contribute disproportionately to extreme exponential tail risk during market distress.
- Unlike direct optimization (minimum-EVaR), which often produces concentrated corner portfolios in low-volatility assets, ERC preserves broad diversification across all assets while balancing their marginal tail-loss impacts.
- However, the source's empirical findings reveal a crucial nuance: EVaR-ERC does *not* consistently dominate CVaR-ERC. Under direct MNTS, the two risk measures yield virtually identical allocations. Under ICA, EVaR-ERC achieves slightly higher gross Sharpe ratios in momentum and sector universes, but at the cost of 2x to 4x higher turnover than CVaR-ERC, which makes its net advantage sensitive to transaction frictions.

## Signal

### Formation timestamp

- **Source-reported:** Monthly rebalancing schedule. At each monthly rebalance date, the preceding 12 months (252 trading days) of daily returns are used to estimate the distributional parameters, and the resulting portfolio is held for one calendar month.
- `research-proposed`: Execution timestamp is assumed to be either Market-on-Close (MOC) on the final trading day of the month or Market-on-Open (MOO) on the first trading day of the subsequent month.

### Lookback window

- **Source-reported:** Rolling 12 months of daily returns (252 observations). The initial 12 months serve as the warm-up window.

### Allocation logic

All portfolios are long-only and fully invested: $\boldsymbol{w} \in \Delta_N = \{\boldsymbol{w} \in \mathbb{R}^N : \sum_{i=1}^N w_i = 1, w_i \ge 0\}$.

1. **EVaR-IRP (Inverse Risk Parity):**
   $$w_i^{\text{IRP}} = \frac{\mathcal{D}_{\eta, i}^{-1}}{\sum_{j=1}^N \mathcal{D}_{\eta, j}^{-1}}$$
   where $\mathcal{D}_{\eta, i} = \text{EVaR}_{1-\eta}(X^{(i)})$ is the standalone EVaR of asset $i$.
2. **EVaR-ERC (Equal Risk Contribution):**
   Solves for $\boldsymbol{w} \in \Delta_N$ such that all asset Euler contributions are equal:
   $$\text{EVaRC}_{\eta, i}(\boldsymbol{w}) = \text{EVaRC}_{\eta, j}(\boldsymbol{w}) = \frac{1}{N} \mathcal{D}_\eta(\boldsymbol{w}) \quad \forall i, j$$
   Implemented computationally by minimizing the sum of squared contribution differences:
   $$\min_{\boldsymbol{w} \in \Delta_N} \sum_{i=1}^N \sum_{j=1}^N \left( \text{EVaRC}_{\eta, i}(\boldsymbol{w}) - \text{EVaRC}_{\eta, j}(\boldsymbol{w}) \right)^2$$
3. **EVaR-deviation ERC:**
   Substitutes $\text{DEVaRC}_{\eta, i}(\boldsymbol{w}) = \text{EVaRC}_{\eta, i}(\boldsymbol{w}) - w_i \mu_i$ into the ERC condition, neutralizing the impact of historical sample mean returns.
4. **Tail Probability Parameter:**
   $\eta = 0.05$ (corresponding to a 95% confidence level for EVaR and matched CVaR).

### Numerical derivative computation

- **Source-reported:** Central finite differences for coordinate derivatives:
  $$\partial_i \mathcal{D}_\eta^{\mathcal{A}}(\boldsymbol{w}) = \frac{\mathcal{D}_\eta^{\mathcal{A}}(\boldsymbol{w} + h \boldsymbol{e}_i) - \mathcal{D}_\eta^{\mathcal{A}}(\boldsymbol{w} - h \boldsymbol{e}_i)}{2h}$$
  Model parameters are held fixed during weight perturbations; each perturbation re-evaluates the scalar EVaR minimization and its weight-dependent domain endpoints without re-fitting the underlying distribution. Step size $h$: `research-proposed: 1e-5` (standard finite-difference perturbation).

### Holding period & exit

- **Source-reported:** Strictly monthly rebalance; positions are held for 1 month with passive drift. No intra-month stop-loss, take-profit, or rebalancing threshold is applied.

## Required data

- **Instruments / Universes (Source-reported):**
  1. `XASSET` (7 broad ETFs): VTI (US Equities), EFA (EAFE Dev Equities), VWO (EM Equities), VNQ (US Real Estate), AGG (US Agg Bonds), TIP (US TIPS), GLD (Gold).
  2. `MOM10` (10 Deciles): Kenneth French 10 value-weighted momentum portfolios sorted on prior 12–2 returns.
  3. `SECTOR` (SPDR Sector ETFs): XLB, XLE, XLF, XLI, XLK, XLP, XLU, XLV, XLY (from Jan 2000), plus XLRE (from Oct 2015) and XLC (from Jun 2018).
- **Timeframe:** Daily frequency, adjusted close prices.
- **Fields:** Dividend- and split-adjusted daily returns.
- **Data Vendors:** Yahoo Finance (XASSET, SECTOR), Kenneth R. French Data Library (MOM10).
- **Missing Data Handling:** Source-reported: Only instruments with a complete 12-month return history at the rebalance date are included (e.g., XLRE and XLC enter dynamically once 12 months of history accumulate). Imputation is not used.
- **Point-in-Time Integrity:** Parameter estimation uses strictly backward-looking 12-month windows; no look-ahead bias in portfolio weights.

## Execution assumptions

- **Source-reported:**
  - Long-only fully invested ($\boldsymbol{w} \in \Delta_N$).
  - One-way drift-adjusted portfolio turnover per rebalance.
  - Proportional transaction costs evaluated at 0 bps (gross), 5 bps, 10 bps, and 25 bps.
  - Zero leverage, no short selling, no borrow fees.
- `research-proposed`:
  - Execution model: Market-on-close (MOC) or VWAP over the opening 30 minutes of the rebalance day.
  - Spread & Slippage: Beyond proportional trading fees, `research-proposed: 2 bps half-spread execution buffer` for large-cap equity and ETF instruments.
  - Capacity: Scalable to high institutional AUM ($100M+) given large-cap ETF liquidity.

## Evidence

### Source-reported

Backtest periods:
- `XASSET`: April 2006 – March 2026 (20 years out-of-sample).
- `MOM10`: January 1996 – March 2026 (30 years out-of-sample).
- `SECTOR`: January 2000 – March 2026 (26 years out-of-sample).
Statistical testing: Two-sided $p$-values computed via studentized circular block bootstrap (Ledoit & Wolf 2008), $B = 4,999$ resamples, block length $L = \lfloor T^{1/3} \rfloor$.

#### 1. Performance vs Equal-Weight Benchmark (Table 2)
- **ERC achieves positive Sharpe differences in all 9 universe–specification comparisons:**
  - `XASSET`:
    - MNTS ERC: $\Delta\text{SR} = +0.246$ ($p = 0.011^{**}$), $\Delta\text{CAGR} = -1.52\%$, $\Delta\text{Vol} = -6.37\%$, $\Delta\text{Calmar} = +0.089$.
    - ICA+NTS ERC: $\Delta\text{SR} = +0.170$ ($p = 0.086^*$), $\Delta\text{CAGR} = -1.45\%$, $\Delta\text{Vol} = -5.53\%$, $\Delta\text{Calmar} = +0.076$.
    - ICA+CTS ERC: $\Delta\text{SR} = +0.100$ ($p = 0.511$), $\Delta\text{CAGR} = -1.52\%$, $\Delta\text{Vol} = -4.77\%$.
  - `SECTOR`:
    - ICA+NTS ERC: $\Delta\text{SR} = +0.051$ ($p = 0.023^{**}$), $\Delta\text{CAGR} = +0.55\%$, $\Delta\text{Vol} = -1.00\%$, $\Delta\text{Calmar} = +0.027$.
    - ICA+CTS ERC: $\Delta\text{SR} = +0.042$ ($p = 0.059^*$), $\Delta\text{CAGR} = +0.41\%$, $\Delta\text{Vol} = -0.96\%$, $\Delta\text{Calmar} = +0.025$.
    - MNTS ERC: $\Delta\text{SR} = +0.022$ ($p = 0.209$).
  - `MOM10`:
    - ICA+CTS ERC: $\Delta\text{SR} = +0.032$ ($p = 0.035^{**}$), $\Delta\text{CAGR} = +0.39\%$, $\Delta\text{Vol} = -0.79\%$.
    - ICA+NTS ERC: $\Delta\text{SR} = +0.028$ ($p = 0.052^*$), $\Delta\text{CAGR} = +0.28\%$, $\Delta\text{Vol} = -0.79\%$.
    - MNTS ERC: $\Delta\text{SR} = +0.007$ ($p = 0.552$).
- **IRP achieves positive Sharpe differences in 8 of 9 comparisons** (e.g., XASSET MNTS IRP $\Delta\text{SR} = +0.177, p = 0.016$; MOM10 ICA+CTS IRP $\Delta\text{SR} = +0.026, p = 0.076$). The only negative IRP difference is XASSET ICA+CTS ($\Delta\text{SR} = -0.077, p = 0.710$).

#### 2. Comparison vs Matched Gaussian EVaR Benchmark (Table 3)
- In `MOM10` ERC, ICA+NTS and ICA+CTS exhibit statistically significant gross Sharpe improvements over the Gaussian benchmark:
  - ICA+NTS ERC: gross $\Delta\text{SR} = +0.014$ ($p = 0.041^{**}$).
  - ICA+CTS ERC: gross $\Delta\text{SR} = +0.019$ ($p = 0.057^*$).
- However, after 25 bps transaction costs, these differences fall to $+0.008$ ($p = 0.218$) and $+0.009$ ($p = 0.370$) and lose significance.
- Direct MNTS ERC underperforms the Gaussian benchmark by $-0.007$ in both gross ($p = 0.073^*$) and net ($p = 0.063^*$).
- Across all other universes (`SECTOR`, `XASSET`), no tempered stable specification exhibits a statistically significant gross or net difference over Gaussian EVaR ($p > 0.10$).

#### 3. Matched EVaR vs CVaR Comparisons (Table 4)
- **Direct MNTS:** EVaR and CVaR portfolios perform almost identically. ERC $\Delta\text{SR}$ (EVaR minus CVaR) is $-0.001$ in `SECTOR` ($p = 0.642$), $-0.003$ in `MOM10` ($p = 0.179$), and $+0.006$ in `XASSET` ($p = 0.651$). None is statistically significant.
- **ICA-based ERC:** Differences are larger:
  - `MOM10` ICA+NTS ERC: EVaR SR 0.595 vs CVaR SR 0.580 ($\Delta\text{SR} = +0.015, p = 0.028^{**}$).
  - `MOM10` ICA+CTS ERC: EVaR SR 0.600 vs CVaR SR 0.582 ($\Delta\text{SR} = +0.018, p = 0.065^*$).
  - `SECTOR` ICA+NTS ERC: $\Delta\text{SR} = +0.028$ ($p = 0.110$); ICA+CTS ERC: $\Delta\text{SR} = +0.017$ ($p = 0.323$).
  - `XASSET` ICA+NTS ERC: $\Delta\text{SR} = -0.061$ ($p = 0.440$); ICA+CTS ERC: $\Delta\text{SR} = -0.126$ ($p = 0.474$). Furthermore, EVaR suffers substantially higher maximum drawdown than CVaR under XASSET ICA+CTS ($34.56\%$ vs $20.93\%$).

#### 4. Turnover and Transaction Cost Attrition (Table 5)
- ICA-based EVaR-ERC generates substantially higher turnover than matched CVaR-ERC:
  - `SECTOR` ICA+NTS: $6.93\%$ (EVaR) vs $2.93\%$ (CVaR); ICA+CTS: $9.49\%$ vs $2.52\%$.
  - `MOM10` ICA+NTS: $5.27\%$ vs $1.96\%$; ICA+CTS: $8.09\%$ vs $1.91\%$.
  - `XASSET` ICA+NTS: $8.52\%$ vs $3.98\%$; ICA+CTS: $12.76\%$ vs $3.02\%$.
- Transaction costs steadily erode the EVaR–CVaR Sharpe premium in `MOM10` ICA+NTS ERC:
  - 0 bps: $+0.015$ ($p = 0.028^{**}$).
  - 5 bps: $+0.014$ ($p = 0.040^{**}$).
  - 10 bps: $+0.013$ ($p = 0.055^*$).
  - 25 bps: $+0.010$ ($p = 0.140$, not significant).

#### 5. Impact of Location Centering (Table 6)
- Comparing raw EVaR-ERC with EVaR-deviation ERC reveals no statistically significant difference in Sharpe ratio across all 9 comparisons (all $p$-values between $0.151$ and $0.993$). Removing the historical mean from the Euler risk contribution does not materially alter full-sample risk-parity performance.

### Independently reproduced

`Not independently reproduced.`

### Negative evidence

- **No uniform EVaR outperformance:** EVaR-ERC does not reliably outperform CVaR-ERC. Under direct MNTS, the differences are indistinguishable from zero ($p \ge 0.179$).
- **Reversal in Cross-Asset Universe:** In `XASSET`, ICA-based EVaR-ERC underperforms matched CVaR-ERC by $-0.061$ (NTS) and $-0.126$ (CTS), and increases max drawdown from $20.93\%$ to $34.56\%$ under CTS.
- **Excessive Turnover Friction:** ICA-based EVaR-ERC incurs 2.4x to 4.2x higher turnover than CVaR-ERC. At realistic institutional transaction costs of 25 bps, the statistical significance of the MOM10 EVaR premium completely vanishes.
- **Limited Benefit over Gaussian ERC:** Outside the momentum universe, tempered stable EVaR-ERC shows no statistically significant advantage over simple Gaussian volatility ERC.

## Falsification plan

1. **Transaction Cost Sensitivity Stress Test:**
   - Run backtests across varying execution cost levels: 0, 5, 10, 25, and 50 bps.
   - `research-defined falsification threshold`: If the net Sharpe ratio of EVaR-ERC falls below that of matched CVaR-ERC at transaction costs $\le 15\text{ bps}$, reject the operational thesis that EVaR's exponential tail weighting justifies its higher rebalancing turnover.
2. **Subperiod & Regime Stability Test:**
   - Partition out-of-sample data into distinct market regimes: high-volatility crash regimes (2000–2002 dot-com bust, 2008 GFC, March 2020 COVID) vs low-volatility bull regimes (2012–2017, 2021).
   - `research-defined falsification threshold`: If EVaR-ERC fails to deliver lower maximum drawdown or higher Calmar ratio than Gaussian ERC during high-volatility crash regimes, reject the hypothesis that EVaR provides superior downside catastrophe protection.
3. **Lookback Window Perturbation:**
   - Vary the parameter estimation lookback window across $L \in \{6, 9, 12, 18, 24\}$ months.
   - `research-defined falsification threshold`: If portfolio weights exhibit severe instability (rank correlation between adjacent lookbacks $< 0.70$) or monthly turnover exceeds $25\%$, reject the FastICA tempered stable estimation as overfitted to sample noise.
4. **Tail Probability Cutoff Audit:**
   - Evaluate performance across $\eta \in \{0.01, 0.025, 0.05, 0.10\}$ ($99\%, 97.5\%, 95\%, 90\%$ confidence).
   - `research-defined falsification threshold`: If the optimization frequently encounters boundary solutions ($u^\star$ on the boundary of the admissible domain) resulting in discontinuous weight jumps, flag the parametric specification as non-admissible for live deployment.
5. **Universe Portability / Crypto Cross-Validation:**
   - Test on non-equity assets (e.g., cryptocurrency perpetual futures or commodity futures).
   - `research-defined falsification threshold`: If the strategy cannot be computed without optimizer failure or produces negative Sharpe relative to equal weight across out-of-sample walk-forward partitions, reject cross-market portability.

## Crypto portability

- **Portability Status:** `adapted / unproven`.
- The source tests exclusively on traditional US equity, ETF, and momentum portfolios. It contains no empirical test on cryptocurrency markets.
- **Research Interpretation for Crypto Adaptation:**
  - Crypto asset returns exhibit far more severe heavy tails, negative skewness, and jump clustering than traditional equities. A tail-risk budgeting framework like EVaR-ERC is theoretically appealing because standard volatility parity underestimates the catastrophic drawdown risk of altcoin portfolios.
- **Crypto-Specific Portability Hurdles:**
  1. *24/7 Market Structure:* Continuous trading lacks a canonical market close; daily returns must be standardized to a specific UTC cut (e.g., 00:00 UTC).
  2. *Perpetual Funding Rates:* For perpetual contracts, funding payments represent a major drag or carry component. In a crypto implementation, returns $\boldsymbol{X}$ must be total economic returns including 8-hour funding cash flows.
  3. *Regime Shift Speed:* The 12-month rolling estimation window assumed in the paper is likely far too slow for crypto market cycles, where 90-day cycles can shift from euphoria to crash. However, shortening the window to 60–90 days risks severe estimation noise in FastICA and tempered stable shape parameters $(\alpha, \theta)$.
  4. *Liquidity & Spread Frictions:* Given that ICA EVaR-ERC generates substantial turnover ($5\%\text{--}13\%$ monthly in equities), applying it to mid-cap crypto assets with wider bid-ask spreads and taker fees (5–10 bps) would severely amplify turnover attrition.
  5. `research-proposed`: Crypto adaptation would require testing on a universe of high-liquidity perpetuals (e.g., top 10 assets on Binance/Hyperliquid with ADV $> \$50\text{M}$), with daily funding integration, 90-day exponentially weighted estimation, and a turnover-penalized ERC objective.

## Limitations

- **Turnover Drag:** ICA-based EVaR-ERC suffers from 2x to 4x higher turnover than CVaR-ERC, eroding its performance under realistic trading costs.
- **Empirical Ambiguity vs CVaR:** The paper demonstrates that EVaR does not provide a uniform advantage over CVaR; under direct MNTS, the two risk measures yield statistically indistinguishable portfolios.
- **FastICA Estimation Noise:** ICA decomposes asset returns into independent components, but FastICA estimation exhibits sign and permutation indeterminacy across rolling windows, which directly contributes to portfolio weight churn.
- **Underspecified Intra-Day Execution:** The paper does not specify intra-day execution timing (e.g., MOC vs MOO vs VWAP) or market impact models.
- **Unproven in Crypto:** No crypto data or perpetual mechanics were evaluated in the source.
- **Not Independently Reproduced:** All performance figures are source-reported and have not been replicated in our independent backtesting environment.

## Implementation status

- `not-implemented`.
- This record represents an external research capture. No code has been integrated into NautilusTrader or PyBroker, no data pipelines for tempered stable estimation or EVaR Euler derivatives have been built, and no live or paper trading is authorized.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- A strategy record being present here indicates only that the research has been normalized into canonical specification format. It does not imply that the strategy is profitable, approved for implementation, or authorized for paper, testnet, or live trading.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` (canonical strategy research specification)
- `[[quant/entropic-value-at-risk-tempered-stable-levy-portfolio-optimization-2026-09-02]]` (earlier parametric optimization study by Choi 2026, focusing on minimum-EVaR, E-STAR, and E-Rachev)
- `[[quant/simple-dynamic-stock-bond-gold-markowitz-volatility-control-2026-09-11]]` (dynamic multi-asset risk control)
- `[[quant/compact-rienet-volatility-drag-mitigation-leveraged-gmv-2026-09-02]]` (portfolio volatility drag mitigation)

## Sources

1. Choi, Jaehyung. "Entropic Value-at-Risk parity for tempered stable returns." arXiv preprint `arXiv:2609.11905v1 [q-fin.PM, q-fin.RM]`, submitted 11 September 2026. Stable URL: [https://arxiv.org/abs/2609.11905](https://arxiv.org/abs/2609.11905). PDF: [https://arxiv.org/pdf/2609.11905](https://arxiv.org/pdf/2609.11905). Full HTML: [https://arxiv.org/html/2609.11905v1](https://arxiv.org/html/2609.11905v1).
2. Ahmadi-Javid, Amir. "Entropic value-at-risk: A new coherent risk measure." *Journal of Optimization Theory and Applications*, 155(3):1105–1123, 2012.
3. Maillard, Sébastien, Thierry Roncalli, and Jérôme Teïletche. "The properties of equally weighted risk contribution portfolios." *Journal of Portfolio Management*, 36(4):60–70, 2010.
4. Qian, Edward. "Risk parity and diversification." *Journal of Investing*, 20(1):119–127, 2011.
5. Ledoit, Olivier, and Michael Wolf. "Robust performance hypothesis testing with the Sharpe ratio." *Journal of Empirical Finance*, 15(5):850–859, 2008.
