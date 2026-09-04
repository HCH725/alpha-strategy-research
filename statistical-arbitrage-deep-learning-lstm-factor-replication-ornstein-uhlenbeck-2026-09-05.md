---
schema: strategy-research-record-v1
title: "Statistical Arbitrage via Deep Learning Risk Factor Replication: Two-Layer Stacked LSTM and Sparse/Dense Factor Residual Ornstein-Uhlenbeck Mean Reversion in Concentrated Equity Markets"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - pairs-trading
  - deep-learning
  - lstm
  - recurrent-neural-networks
  - pca
  - eigenportfolios
  - ornstein-uhlenbeck
  - mean-reversion
  - arbitrage-pricing-theory
  - market-neutral
status: research-only
confidence: high
source_as_of: 2025-11-21
sources:
  - "Marek Adamczyk and Michał Dąbrowski, 'Statistical Arbitrage in Polish Equities Market Using Deep Learning Techniques', arXiv:2512.02037v1 [q-fin.ST], November 2025. https://arxiv.org/abs/2512.02037"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Statistical Arbitrage via Deep Learning Risk Factor Replication: Two-Layer Stacked LSTM and Sparse/Dense Factor Residual Ornstein-Uhlenbeck Mean Reversion in Concentrated Equity Markets

## Provenance

- **Primary Source:** Marek Adamczyk and Michał Dąbrowski, *"Statistical Arbitrage in Polish Equities Market Using Deep Learning Techniques"*, arXiv preprint `arXiv:2512.02037v1 [q-fin.ST]`, dated November 21, 2025.
- **Canonical arXiv URL:** [https://arxiv.org/abs/2512.02037](https://arxiv.org/abs/2512.02037)
- **Direct HTML Full Text:** [https://arxiv.org/html/2512.02037v1](https://arxiv.org/html/2512.02037v1)
- **Primary LaTeX Source Bundle:** Verified directly against official arXiv source package `arXiv:2512.02037` containing `Master_thesis_pretty.tex` (201,882 bytes, University of Wrocław, Faculty of Mathematics and Computer Science). All equations, network parameters, calibration algorithms, and tabular empirical metrics in this record trace directly to this primary LaTeX source.
- **Academic Context:** Research supervised by dr Marek Adamczyk, awarded distinction in the national Polish Mathematical Society (PTM) competition for best master's thesis in probability and applied mathematics (Michał Dąbrowski).
- **Pre-Write Deduplication & Identity Audit:** A repository-wide inspection verified zero matches for `2512.02037`, `Adamczyk`, `Dąbrowski`, `Dabrowski`, or `WIG20` across all 372 existing markdown records. While the repository contains statistical arbitrage records utilizing high-frequency order flow or signature kernels (e.g. `signature-optimal-execution-statistical-arbitrage-quadratic-reduction-2026-09-02.md`, `crypto-drl-execution-overlay-multi-pair-trading-2026-09-01.md`), this research investigates an independent, non-overlapping paradigm: the extension of the classical Avellaneda & Lee (2008) multi-factor statistical arbitrage framework using a two-layer stacked LSTM network to generate dynamic, time-aware cross-sectional factor replications directly from peer asset return sequences in concentrated equity markets, evaluated alongside classical PCA and ETF benchmarks across normal (2017–2019) and acute recession (2020 COVID-19) regimes.

## Economic mechanism

### Source-reported

In classical pairs trading (Tartaglia / Morgan Stanley 1987; Gatev et al. 2006), two highly correlated individual securities are traded against each other when their price ratio diverges from historical parity. However, trading discrete 1-to-1 asset pairs suffers from major structural defects:
1. Each asset possesses idiosyncratic company-specific noise with differing oscillation frequencies, leading to non-stationary pair divergence.
2. Pair selection is combinatorial, fragile, and sensitive to structural breaks in single-firm operations.

Avellaneda and Lee (2008) reformulated statistical arbitrage under Arbitrage Pricing Theory (APT; Ross 1976), decomposing each individual stock return $R_t^i$ into systematic risk factors and an idiosyncratic residual:
$$R_t^i = \alpha_i dt + \sum_{j=1}^r \beta_{ij} F_t^j + dI_t^i$$
where $F_t^j$ represent tradable systematic risk drivers, $\beta_{ij}$ are factor loadings, and $dI_t^i$ represents the asset-specific idiosyncratic return. When cumulative idiosyncratic return $I_t^i = \sum_{k=1}^t dI_k^i$ deviates from its equilibrium level, competitive market forces (arbitrageurs expanding buy orders for undervalued assets and shorting overvalued ones) exert corrective pressure, driving $I_t^i$ back toward its long-term mean. This reversion is formalized by modeling $I_t^i$ as a continuous-time Ornstein-Uhlenbeck (OU) process:
$$dI_t^i = \kappa_i (\mu_i - I_t^i) dt + \sigma_i dB_t^i$$
where $\kappa_i$ represents the speed of mean reversion, $\mu_i$ is the long-term equilibrium mean, $\sigma_i$ is idiosyncratic volatility, and $B_t^i$ is standard Brownian motion.

The authors identify a fundamental limitation in existing factor generation techniques:
- **Principal Components Analysis (PCA):** Extracts static orthogonal eigenvectors from the trailing sample covariance matrix $\widehat{\mathbf{\Sigma}} = \frac{1}{n-1}\mathbf{Y}\mathbf{Y}^T$. While effective in normal regimes, PCA treats all historical observations symmetrically, assumes linear factor combinations, and fails to capture sequential temporal dynamics or time-varying lead-lag relationships.
- **Exchange Traded Funds (ETFs):** In less developed or concentrated equity markets (such as the Warsaw Stock Exchange / GPW, market capitalization $\approx €300\text{B}$ across 415 domestic and foreign firms), the ETF spectrum is sparse. Polish sector ETFs do not exist, restricting direct index replication to a handful of broad benchmark funds (BETA ETF WIG20TR, mWIG40TR, sWIG80TR).
- **Deep Learning (Stacked LSTM):** To overcome the linear and time-invariant constraints of PCA and OLS, the authors propose training a recurrent neural network (two-layer stacked LSTM) that maps the multivariate return history of all $N-1 = 59$ peer stocks over a lookback window $W=120$ days directly to a time-varying coefficient vector $\beta_t^i \in \mathbb{R}^{59}$. The LSTM cell memory ($c_t$) and hidden state ($h_t$) preserve long-term temporal dependencies without vanishing gradients, allowing the network to modulate factor sensitivities conditioned on whether a position was opened during an earlier state of the lookback sequence.

### Research interpretation

1. **Microstructure of Concentrated Equity Markets:** Unlike the US equity universe (S&P 500 / Russell 3000) where hundreds of liquid names provide dense industry clusters, smaller national equity markets are dominated by a handful of mega-caps (on GPW, the top 5 companies in WIG20 account for $>50\%$ of index capitalization, heavily weighted toward state-backed commercial banks like PKO BP, Pekao, and energy/materials firms like PKN Orlen, KGHM). In such concentrated markets, idiosyncratic dispersion is constrained because systemic macro and banking liquidity factors dominate total variance (first principal component explains $>15\%$ alone, and 15 components capture $>50-67\%$ of total variance).
2. **Dynamic OLS vs. Recurrent Non-Linear Memory:** Standard rolling OLS fits factor loadings by treating all observations in the estimation window as exchangeable draws from a stationary distribution. An LSTM acts as a state-dependent recursive filter: by updating cell gates ($f_t, i_t, o_t$) at each time step, it dynamically adjusts the effective lookback and penalizes irrelevant cross-asset correlations via an explicit $L_1$ sparsity regularizer.
3. **Decoupling Market Direction from Factor Residuals:** By constructing an exact hedged portfolio ($+1$ unit of target stock $i$, short $\beta_{ij}$ units of systematic factors/peers), the strategy eliminates broad equity beta. Alpha generation depends entirely on whether the residual process $I_t^i$ satisfies unconditional stationarity and exhibits a mean-reversion speed $\kappa_i > 4$ (half-life $\tau_i < 60$ trading days) sufficient to overcome bid-ask spreads, financing costs, and exchange transaction fees.

## Signal

The trading signal operates through a daily multi-stage estimation and filtering pipeline:

### 1. Risk Factor Formulation and Asset Replication (`source-reported`)
Across a fixed universe of $N=60$ equities (combined components of WIG20 and mWIG40), systematic factor replications are generated using one of three structural architectures:
- **Architecture A: Principal Components Analysis (PCA)**
  - Normalized daily returns $Y_t^i = (R_t^i - \overline{R}_i) / \overline{\sigma}_i$ computed over a rolling 252-trading-day calibration window.
  - Spectral decomposition of sample covariance matrix $\widehat{\mathbf{\Sigma}} = \frac{1}{n-1}\mathbf{Y}\mathbf{Y}^T = \mathbf{F} \mathbf{\Lambda} \mathbf{F}^T$.
  - Eigenportfolios $F_t^j = \sum_{k=1}^{60} \frac{f_j^{(k)}}{\overline{\sigma}_k} R_t^k$ for $j=1, \dots, r$.
  - Two variants evaluated:
    - *Constant $r$:* Fixed $r = 15$ eigenportfolios (explaining ~53–67% of total variance across sample years).
    - *Variable $r$:* Dynamic $r$ selected such that cumulative explained variance $\sum_{j=1}^r \lambda_j / \sum_{k=1}^{60} \lambda_k \ge 0.55$ (55%).
  - Eigenvector basis recalculated annually (once every 252 trading days); factor loadings $\beta_{ij}$ re-estimated daily via OLS over rolling $W=120$ days.
- **Architecture B: Stacked Long Short-Term Memory Network (LSTM)**
  - Model Architecture: Two stacked LSTM layers, each with hidden dimension $h = 64$.
  - Input at time $t$: 59-dimensional vector $\mathbf{X}_t \in \mathbb{R}^{59}$ containing daily returns of all peer stocks in the 60-stock universe (excluding target stock $i$).
  - Sequence lookback: $W = 120$ trading days.
  - Forward computation:
    - Layer 1: $h_t^{(1)}, c_t^{(1)} = \text{LSTM}_1(\mathbf{X}_t, h_{t-1}^{(1)}, c_{t-1}^{(1)})$
    - Layer 2: $h_t^{(2)}, c_t^{(2)} = \text{LSTM}_2(h_t^{(1)}, h_{t-1}^{(2)}, c_{t-1}^{(2)})$
    - Linear output projection producing daily factor loading vector $\boldsymbol{\beta}_t^i \in \mathbb{R}^{59}$.
  - Loss function with $L_1$ regularization penalty ($p = 10^{-5}$):
    $$\mathcal{L} = \frac{1}{W} \sum_{t=1}^W \left( R_t^i - \sum_{j=1}^{59} \beta_t^{(j)} X_t^{(j)} \right)^2 + p \sum_{j=1}^{59} |\beta_t^{(j)}|$$
  - Optimization: Adam optimizer, batch size $B = 16$, trained annually on rolling 3-year historical windows (e.g. 2014–2016 for 2017 deployment, 2015–2017 for 2018 deployment, 2016–2018 for 2019 deployment), initialized with a 120-day warm-up period before each deployment year.
- **Architecture C: Exchange Traded Funds (ETFs)**
  - *Real/Sparse ETFs:* 3 benchmark funds: BETA ETF WIG20TR, BETA ETF mWIG40TR, BETA ETF sWIG80TR. Factor loadings $\beta_{i, \text{ETF}}$ estimated via rolling 120-day OLS.
  - *Artificial/Dense Sector ETFs:* 14 sector total return subindices (WIG-BANKI, WIG-BUDOWN, WIG-CHEMIA, WIG-ENERG, WIG-GORNIC, WIG-GRY, WIG-INFO, WIG-LEKI, WIG-MEDIA, WIG-MOTO, WIG-NRCHOM, WIG-ODZIEZ, WIG-PALIWA, WIG-SPOZYW). Replicated assuming zero tracking error; factor loadings estimated via rolling 120-day OLS.

### 2. Ornstein-Uhlenbeck Residual Modeling (`source-reported`)
- For each stock $i$ on trading day $t$, idiosyncratic return increments are extracted:
  $$dI_k^i = R_k^i - \alpha_i dt - \sum_{j} \beta_{ij} F_k^j, \quad k = t - W + 1, \dots, t$$
- Cumulative residual process constructed: $I_k^i = \sum_{u=1}^k dI_u^i$.
- $I_k^i$ mapped to a discrete AR(1) specification:
  $$I_k^i = \phi_0^i + \phi_1^i I_{k-1}^i + \zeta_k^i$$
  with coefficients $\phi_0^i, \phi_1^i$ estimated using Yule-Walker method of moments over rolling window $W = 120$ trading days ($dt = 1/252$).
- Continuous OU parameters recovered:
  $$\kappa_i = -\frac{\ln(\phi_1^i)}{dt}, \quad \mu_i = \frac{\phi_0^i}{1 - \phi_1^i}, \quad \sigma_i = \sqrt{\frac{\widehat{\text{Var}}(\zeta^i) \cdot 2\kappa_i}{1 - (\phi_1^i)^2}}$$
- **Mean-Reversion Gate Filter (`source-reported`):**
  Only stocks with estimated mean-reversion speed $\kappa_i > 4$ (corresponding to half-life $\tau_i = \frac{252}{\kappa_i} < 63$ trading days) are eligible for signal generation. Stocks failing this gate ($\kappa_i \le 4$) are barred from opening new positions.

### 3. Normalized Signal Generation and Execution Cutoffs (`source-reported`)
- Normalized dimensionless trading score $G_t^i$:
  $$G_t^i = \frac{I_t^i - \mu_i}{\sqrt{\sigma_i^2 / (2\kappa_i)}}$$
  where the denominator $\sqrt{\sigma_i^2 / (2\kappa_i)}$ represents the stationary standard deviation of the OU process. As $t \to \infty$, $G_t^i \sim \mathcal{N}(0, 1)$.
- **Position State Machine:** Each stock has an active state $s_t^i \in \{-1, 0, 1\}$ (short, flat, long). At most 1 open position per stock:
  - **Open Long Position ($s_t^i = 0 \to +1$):** Triggered when $G_t^i \le -\overline{g}_{ol}$. Buy $+1$ unit of stock $i$, short $\beta_{ij}$ units of systematic replicating factors.
  - **Close Long Position ($s_t^i = +1 \to 0$):** Triggered when $G_t^i \ge \overline{g}_{cl}$. Liquidate long stock and cover short factor hedge.
  - **Open Short Position ($s_t^i = 0 \to -1$):** Triggered when $G_t^i \ge \overline{g}_{os}$. Short $-1$ unit of stock $i$, buy $\beta_{ij}$ units of systematic replicating factors.
  - **Close Short Position ($s_t^i = -1 \to 0$):** Triggered when $G_t^i \le -\overline{g}_{cs}$. Cover short stock and sell long factor hedge.
- **In-Sample Calibrated Thresholds (`source-reported`):**
  Calibrated via 2D grid search on 2015–2016 in-sample data:
  - *PCA ($r=15$ and Variable $r$):* $\overline{g}_{ol} = \overline{g}_{os} = 1.10$, $\overline{g}_{cl} = \overline{g}_{cs} = -0.50$.
  - *LSTM:* $\overline{g}_{ol} = \overline{g}_{os} = 1.10$, $\overline{g}_{cl} = \overline{g}_{cs} = -0.15$.
  - *Real ETFs:* $\overline{g}_{ol} = \overline{g}_{os} = 2.10$, $\overline{g}_{cl} = \overline{g}_{cs} = 0.75$.
  - *Artificial Sector ETFs:* $\overline{g}_{ol} = \overline{g}_{os} = 1.95$, $\overline{g}_{cl} = \overline{g}_{cs} = 0.40$.
- **Static Leg Weight Rule (`source-reported`):** Once a trade is entered at time $t_0$, the hedge quantities $\beta_{ij}(t_0)$ remain locked until exit at $t_1$. Dynamic daily rebalancing of the hedge leg during an open trade is explicitly avoided to minimize turnover and transaction fees.
- **End-of-Horizon Liquidation Rule (`source-reported`):** No new positions are opened within the final $W/2 = 60$ trading days of the investment horizon ($t = 3$ years). Any remaining open positions are unconditionally closed on the final day.

## Required data

- **Universe:** 60 equities representing the top 20 large-cap (WIG20) and 40 mid-cap (mWIG40) stocks listed on the Warsaw Stock Exchange (GPW) (`source-reported`).
- **Data Source & History:** GPW daily official closing data from 2012 to 2022 (`source-reported`).
- **Price Fields:** Daily adjusted close prices (Total Return adjusted, incorporating cash dividends, rights offerings, and splits) (`source-reported`).
- **Benchmark & Sector Indices:**
  - Rating indices: WIG, WIG20, WIG20TR, mWIG40, mWIG40TR, sWIG80, sWIG80TR (`source-reported`).
  - Sector indices: 14 subindices (WIG-BANKI, WIG-BUDOWN, WIG-CHEMIA, WIG-ENERG, WIG-GORNIC, WIG-GRY, WIG-INFO, WIG-LEKI, WIG-MEDIA, WIG-MOTO, WIG-NRCHOM, WIG-ODZIEZ, WIG-PALIWA, WIG-SPOZYW) (`source-reported`).
  - Traded ETFs: BETA ETF WIG20TR, BETA ETF mWIG40TR, BETA ETF sWIG80TR (`source-reported`).
- **Point-in-Time & Lookahead Protection:**
  - Rolling estimation window $W = 120$ trading days for OU parameter calibration and OLS loadings (`source-reported`).
  - Annual PCA eigenvector estimation uses strictly the preceding 252 trading days (zero forward overlap) (`source-reported`).
  - LSTM training uses non-overlapping rolling 3-year historical blocks with 120-day burn-in; predictions in deployment year are strictly forward-propagating without future return leakage (`source-reported`).
- **Missing Data & Corporate Action Handling:** In-sample grid optimization in 2015–2016 restricted to companies possessing continuous trading history since 2012; sector indices created after 2017 (e.g. WIGTECH, WIG-MOTO prior to inception) omitted during in-sample calibration (`source-reported`).
- **Risk-Free Rate:** 52-week Polish Treasury Bill yield: $r_f = 1.50\%$ annualized for 2017–2019; $r_f = 0.50\%$ annualized for 2020 (`source-reported`).

## Execution assumptions

- **Execution Timing & Fill Model:** Daily close-to-close execution. Signals computed on day $t$ closing prices; orders assumed filled at day $t$ adjusted close price (`source-reported`). *(Note: In live implementation, this requires entering at MOC — Market-on-Close auction — or next-day open; fill at same-bar close constitutes an optimistic execution assumption).*
- **Order Types:** Unconstrained market orders with zero fill latency (`source-reported`). *(Realistic limit-order execution model is `research-proposed`).*
- **Transaction Costs & Fees:** Flat transaction fee $c = 0.10\%$ (10 basis points) charged on every trade leg (applied on entry and exit to both the primary stock and every component of the replicating factor portfolio) (`source-reported`).
- **Short Selling:** Frictionless borrowing and short selling assumed across all 60 constituent stocks and benchmark ETFs (`source-reported`). *(In practice, GPW securities lending is illiquid for mid-caps in mWIG40; borrow cost model is `research-proposed`).*
- **Portfolio Sizing & Leverage Model (`source-reported`):**
  - Gross portfolio leverage constraint: 2:1 leverage ratio ($200\%$ gross exposure).
  - Capital per trade: $\Lambda_t = \frac{2}{60} E_t$, where $E_t$ is total accumulated portfolio equity.
  - Sizing is uniformly distributed across the $N=60$ potential stock sleeves (allocating $\sim 3.33\%$ of equity per sleeve, magnified to $\sim 6.67\%$ gross asset + hedge exposure under 2:1 leverage).
- **Cash Accounting & Tracking Metric $C_t$ (`source-reported`):** In addition to realized equity $E_t$, daily cash account $C_t$ tracks intermediate cash flows and margin commitments across all open multi-leg positions.
- **Capacity Constraint:** Not explicitly specified by primary source. Given median daily trading turnover on GPW mWIG40 components ($\sim €200\text{k} - €1\text{M}$), strategy capacity is estimated at $\le €5\text{M}$ before market impact degrades 10 bps fee assumptions (`research-proposed`).

## Evidence

### Source-reported

The primary source evaluates four distinct factor generation architectures across two out-of-sample test periods:
1. **Normal Market Regime (2017–2019, 3 calendar years):**
   - **PCA (Constant $r=15$):**
     - Annual Sharpe Ratio $\mathcal{S}$: **2017: +2.63**, **2018: +1.01**, **2019: -1.16** (Table 4.2 / tab:5).
     - Cumulative Profit: $\sim 20$ PLN on initial $E_0 = 100$ PLN (**+20.0%** cumulative return).
     - Sector Breakdown: Best performing sub-portfolios were Fuels ($\mathcal{S}_{2017}=1.79, \mathcal{S}_{2018}=1.10, \mathcal{S}_{2019}=0.36$), Architecture ($\mathcal{S}=1.39, 0.49, 0.75$), and Unassigned/Other ($\mathcal{S}_{2017}=2.80$). Weakest in 2019 was Pharma ($\mathcal{S}=-1.31$) and Banks ($\mathcal{S}=-1.00$).
   - **PCA (Variable $r$, $\ge 55\%$ variance):**
     - Annual Sharpe Ratio $\mathcal{S}$: **2017: +2.51**, **2018: +0.44**, **2019: -0.91** (Table 4.2 / tab:5).
     - Cumulative Profit: $\sim 20$ PLN (**+20.0%** cumulative return).
     - Similar trajectory to constant $r$, confirming that $r \approx 15-18$ captures the stable variance threshold.
   - **Stacked LSTM Network ($2 \times 64$ hidden units):**
     - Annual Sharpe Ratio $\mathcal{S}$: **2017: +0.60**, **2018: +2.09**, **2019: -1.53** (Table 4.3 / tab:5.5).
     - Cumulative Return: $\sim +10.0\%$ (final equity $E_T \approx 110$ PLN).
     - Sector Breakdown: In 2018, Real Estate ($\mathcal{S}=2.05$), Architecture ($\mathcal{S}=1.81$), Banks ($\mathcal{S}=1.53$), Clothes ($\mathcal{S}=1.52$), and Pharma ($\mathcal{S}=1.17$) delivered strong performance. In 2019, performance collapsed broadly across Media ($\mathcal{S}=-1.90$), Mining ($\mathcal{S}=-0.16$), Food ($\mathcal{S}=-1.58$), and Real Estate ($\mathcal{S}=-1.80$).
   - **Existing Real ETFs (3 benchmark funds):**
     - Annual Sharpe Ratio $\mathcal{S}$: **2017: -0.25**, **2018: -0.46**, **2019: +1.43** (Table 4.4 / tab:6).
     - Cumulative Profit: $\sim 5$ PLN (**+5.0%** cumulative return).
     - Characterized by very low trade activity, wide residual bands, and negative returns during 2017–2018, recovering only in 2019.
   - **Artificial Dense Sector ETFs (14 sector indices):**
     - Annual Sharpe Ratio $\mathcal{S}$: **2017: +1.28**, **2018: -1.63**, **2019: -0.84** (Table 4.5 / tab:7).
     - Cumulative Profit: $\sim 5$ PLN (**+5.0%** cumulative return). High turnover and transaction drag eroded performance after 2017.
   - **Empirical Mean-Reversion Speeds (2019 sample, Table 4.1 / tab:4):**
     - Mean $\kappa$ across all sectors: PCA constant $r$: $\kappa = 19.46$ ($\tau = 13.56$ days); PCA variable $r$: $\kappa = 20.17$ ($\tau = 13.14$ days); LSTM: $\kappa = 20.80$ ($\tau = 12.44$ days); Real ETFs: $\kappa = 21.60$ ($\tau = 12.24$ days); Artificial ETFs: $\kappa = 22.45$ ($\tau = 11.90$ days).
     - Fastest mean-reverting sectors: Games ($\tau = 9.04 - 11.32$ days), Real Estate ($\tau = 8.03 - 12.09$ days), Fuels ($\tau = 10.00 - 13.18$ days).
     - Slowest mean-reverting sectors: Clothes ($\tau = 9.31 - 20.17$ days), Food ($\tau = 11.04 - 17.45$ days), Chemistry ($\tau = 11.76 - 16.88$ days).
2. **Acute Recession Regime (2020 COVID-19 Pandemic Holdout):**
   - **PCA (Constant $r=15$):** Severe failure: Sharpe $\mathcal{S} = \mathbf{-1.39}$ (Table 4.6 / tab:8). Catastrophic equity drawdown starting in mid-2020 as spring 2020 crash distortions corrupted the rolling 120-day factor loadings.
   - **PCA (Variable $r=18$):** Sharpe $\mathcal{S} = \mathbf{+0.59}$ (Table 4.6 / tab:8), insulated by retaining 18 components to absorb elevated macro crash variance.
   - **Stacked LSTM Network:** Sharpe $\mathcal{S} = \mathbf{-0.34}$ (Table 4.7 / tab:9). Moderately negative; smoother parameter transitions prevented the catastrophic equity collapse observed in constant PCA. Profited in H1 2020, but suffered decay in late 2020.
   - **Existing Real ETFs (3 funds):** Sharpe $\mathcal{S} = \mathbf{+0.56}$, final equity $E_T = 103.44$ (**+3.44%** return) (Table 4.8 / tab:10). Stable equity curve with minimal drawdowns.
   - **Artificial Dense Sector ETFs (14 indices):** Sharpe $\mathcal{S} = \mathbf{+0.68}$, final equity $E_T \approx 105$ PLN (**+5.0%** return) (Table 4.9 / tab:11). Broad sector aggregation effectively cushioned against idiosyncratic single-stock breakdowns.

### Independently reproduced

Not independently reproduced in internal quantitative backtesting engine. The empirical findings reported above are verified directly from the author's primary research manuscript and tabular datasets.

### Negative evidence

1. **Catastrophic Parameter Breakdown in Crash Regimes:** Both PCA and LSTM rely on rolling estimation windows of single-stock returns. During the COVID-19 crash of March 2020, cross-sectional correlations spiked to near unity. As these extreme crash returns rotated into the rolling 120-day estimation window during summer/autumn 2020, factor loadings $\beta_{ij}$ became severely distorted. Residuals diverged without mean-reverting, generating massive false entry signals and sustained losses ($PCA_{r=15}$ Sharpe $-1.39$ in 2020).
2. **Persistent 2019 Decay Across All Machine Learning Models:** All statistical arbitrage methods (PCA $r=15$, PCA variable $r$, LSTM, and Artificial Sector ETFs) suffered negative Sharpe ratios in 2019 ($\mathcal{S} \in [-1.53, -0.84]$), demonstrating that unhedged idiosyncratic trend persistence and macro drift frequently overpower statistical mean-reversion over 12-month spans.
3. **Transaction Fee Vulnerability:** The authors note that polish GPW standard retail transaction fees are $0.29\%$ (29 bps). The backtest assumed an aggressive institutional rate of $0.10\%$ (10 bps). Because statistical arbitrage requires simultaneously transacting in the target stock and up to 15–59 hedge components, realistic exchange fees of $0.20-0.29\%$ plus half-spread completely extinguish the $+10-20\%$ cumulative profits over 3 years.

## Falsification plan

To test whether the deep-learning and PCA residual mean-reversion signals provide genuine structural alpha or merely capture transient in-sample curve-fitting, the following operational tests must be executed:

1. **Ablation of Recurrent Memory (Feedforward / OLS Control):**
   - *Protocol:* Replace the two-layer stacked LSTM with (a) a standard rolling OLS regression and (b) a non-recurrent multi-layer perceptron (MLP) over the identical 120-day input sequence.
   - *Metric:* Out-of-sample annualized Sharpe ratio and maximum drawdown.
   - *Decision Rule:* If the LSTM fails to outperform rolling OLS by at least $+0.30$ annual Sharpe or exhibits identical rank-correlation of hedge weights ($\rho > 0.90$), falsify the hypothesis that recurrent temporal memory provides unique economic factor representation (`research-defined falsification threshold`).
2. **Transaction Cost and Fee Stress Test:**
   - *Protocol:* Scale transaction costs $c$ from the baseline 10 bps across $\{15\text{ bps}, 20\text{ bps}, 25\text{ bps}, 30\text{ bps}\}$ per leg, incorporating a linear market impact model: $\Delta P = \gamma \cdot \sqrt{\text{Volume} / \text{ADV}_{20}}$.
   - *Decision Rule:* If cumulative net return over 2017–2019 drops below $0.0\%$ at $c \le 18\text{ bps}$, reject the strategy as an unexecutable friction illusion (`research-defined falsification threshold`).
3. **Regime-Conditional Crash Stress (Volatility-Gated Abstention):**
   - *Protocol:* Evaluate residual stationarity under rolling market realized volatility spikes ($>90\text{th}$ percentile of 252-day market volatility).
   - *Decision Rule:* If the OU half-life $\tau_i$ expands beyond 40 trading days during high-volatility regimes for $>50\%$ of universe assets, confirm that the mean-reversion mechanism collapses during stress, mandating an operational regime abstention switch (`research-defined falsification threshold`).
4. **Shuffled-Label / Synthetic Factor Placebo Test:**
   - *Protocol:* Randomly permute the identity of peer stocks in the LSTM input vector $\mathbf{X}_t$, destroying cross-sectional industry structure while preserving individual asset marginal return distributions.
   - *Decision Rule:* If the placebo LSTM produces annualized Sharpe $\mathcal{S} > 0.50$ (comparable to true sector peers), falsify the claim that the network extracts structural industry risk factors (`research-defined falsification threshold`).

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Primary Mechanism Portability:** The economic premise of Arbitrage Pricing Theory (decomposing altcoin returns into broad market beta, sector/thematic factors, and idiosyncratic mean-reverting residuals) is theoretically sound in cryptocurrency markets, but must be treated as a `research-proposed` adaptation:
  - *Perpetual Futures Market Structure:* In crypto, single-asset shorting is natively available via linear USDT/USDC perpetual contracts with zero borrow locate frictions, directly resolving the GPW equity shorting bottleneck.
  - *Funding Rate Friction:* Unlike equities where borrowing incurs a stable interest rate, crypto perpetuals charge funding rates every 8 hours. Holding an idiosyncratic pairs trade over an average half-life of $\tau \approx 10-15$ days exposes the strategy to cumulative funding drag. If an altcoin's divergence is driven by crowded retail longing, funding rates can exceed $50-100\%$ APR, rapidly erasing residual mean-reversion profits (`research-proposed`).
  - *24/7 Session & Continuous OU Calibration:* Equities trade in discrete daily sessions with standard closing auctions. Crypto trades continuously 24/7/365. The 120-day calibration window must be adapted to either 120 daily closes (00:00 UTC) or 4-hour/1-hour bars with adaptive volatility scaling (`research-proposed`).
  - *Liquidity Fragmentation & Basis Disconnect:* Cross-sectional altcoin liquidity is highly fragmented across Binance, Bybit, OKX, and decentralized venues. Spot-perpetual basis dislocations and exchange liquidation cascades frequently trigger non-linear price excursions that violate Gaussian OU assumptions, causing extreme residual tail divergence (`research-proposed`).

## Limitations

- **Underspecified Execution Latency:** The primary source assumes costless instantaneous fills at the official daily closing price. Same-bar closing execution introduces potential lookahead or unachievable MOC pricing for illiquid mid-cap constituents (`underspecified`).
- **No Borrowing Fee Accounting:** The empirical simulation charges a 10 bps transaction fee but completely omits short borrow fees (which typically range from $1\%$ to $8\%$ annualized for GPW mid-caps) (`data gap`).
- **Severe Survivorship & In-Sample Selection Bias:** Universe inclusion required companies to have existed since 2012 and maintain membership in WIG20/mWIG40. Delisted, bankrupt, or suspended firms were excluded, biasing historical mean-reversion metrics upward (`methodological limitation`).
- **Lack of Independent Out-of-Sample Verification:** The stacked LSTM methodology has only been tested on the Polish GPW dataset across 2017–2020. It has not been independently replicated on US equities, European large-caps, or cryptocurrency markets (`unproven`).

## Implementation status

- `implementation_status: not-implemented`
- No production or prototype implementation exists in `nautilus-quant-system` or PyBroker research stacks.
- Capturing this research does not authorize trading or paper-trading execution.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- This record serves solely as normalized upstream quantitative research material for ChatGPT Research Intake Review and downstream synthesis. It does not constitute investment advice, backtest verification, or an approved algorithmic trading strategy.

## Related Wiki records

- `[[quant/statistical-arbitrage-multi-factor-avellaneda-lee-2026-08-30]]`
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`
- `[[quant/crypto-drl-execution-overlay-multi-pair-trading-2026-09-01]]`
- `[[quant/signature-optimal-execution-statistical-arbitrage-quadratic-reduction-2026-09-02.md]]`
- `[[quant/foreign-exchange-spatiotemporal-graph-statistical-arbitrage-2026-09-02.md]]`

## Sources

- **Primary Source Paper:** Marek Adamczyk and Michał Dąbrowski, *"Statistical Arbitrage in Polish Equities Market Using Deep Learning Techniques"*, arXiv preprint `arXiv:2512.02037v1 [q-fin.ST]`, November 21, 2025. URL: [https://arxiv.org/abs/2512.02037](https://arxiv.org/abs/2512.02037).
- **Primary Source Code & Manuscript Bundle:** Retrieved from official arXiv source bundle [https://arxiv.org/src/2512.02037](https://arxiv.org/src/2512.02037), containing complete author LaTeX manuscript `Master_thesis_pretty.tex` (University of Wrocław, 2025). All equations, network parameters, calibration algorithms, and tabular empirical metrics in this record trace directly to this primary LaTeX source.
- **Foundational Theoretical References:**
  - Marco Avellaneda and Jeong-Hyun Lee, *"Statistical Arbitrage in the U.S. Equities Market"*, Quantitative Finance, Vol. 10, No. 7, pp. 761–782, 2010 (preprinted 2008).
  - Stephen A. Ross, *"The Arbitrage Theory of Capital Asset Pricing"*, Journal of Economic Theory, Vol. 13, No. 3, pp. 341–360, 1976.
  - Evan Gatev, William N. Goetzmann, and K. Geert Rouwenhorst, *"Pairs Trading: Performance of a Relative-Value Arbitrage Rule"*, Review of Financial Studies, Vol. 19, No. 3, pp. 797–827, 2006.
