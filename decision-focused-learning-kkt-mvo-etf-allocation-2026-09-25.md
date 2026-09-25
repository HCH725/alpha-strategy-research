---
schema: strategy-research-record-v1
title: "Decision-Focused Learning for Mean–Variance Portfolio Optimization via KKT-Based Reformulation (Nosaka, Ikeda, & Takano, arXiv:2609.21427)"
created: 2026-09-25
updated: 2026-09-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - portfolio-optimization
  - decision-focused-learning
  - mean-variance
  - kkt-reformulation
  - mpec
  - etf-allocation
status: research-only
confidence: medium
source_as_of: 2026-09-18
sources:
  - "https://arxiv.org/abs/2609.21427 (arXiv:2609.21427v1 [cs.LG], submitted Fri, 18 Sep 2026 07:39:47 UTC, 11 pages, accepted at PRICAI 2026; only version — v2 returns 406 Not Found, checked 2026-09-25)"
  - "https://arxiv.org/html/2609.21427v1 (pinned full text, 157,748 bytes, SHA-256 82f7f097c40f3531908d4e99da35d9b918791fa99ec5339aa872d2018c43709b, converted to 31,754 characters / 439 lines and read end to end on 2026-09-25: Abstract, Sections 1–4, Tables 1–2, Figure 1 caption, References)"
  - "https://doi.org/10.48550/arXiv.2609.21427 (DataCite DOI, resolves HTTP 302 -> https://arxiv.org/abs/2609.21427 -> 200, checked 2026-09-25; conference acceptance note 'Accepted at PRICAI 2026' on landing page)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Decision-Focused Learning for Mean–Variance Portfolio Optimization via KKT-Based Reformulation (Nosaka, Ikeda, & Takano, arXiv:2609.21427)

## Provenance

- **Paper**: Kensei Nosaka (Graduate School of Science and Technology, University of Tsukuba, Tsukuba-shi, Ibaraki 305-8573, Japan; `s2620473@u.tsukuba.ac.jp`), Shunnosuke Ikeda (Faculty of Engineering, Information and Systems, University of Tsukuba; `ikeda@cs.tsukuba.ac.jp`), and Yuichi Takano (Faculty of Engineering, Information and Systems, University of Tsukuba; `ytakano@sk.tsukuba.ac.jp`), *"Decision-Focused Learning for Mean–Variance Portfolio Optimization via KKT-Based Reformulation"*, arXiv preprint `arXiv:2609.21427v1 [cs.LG]`.
- **Submission history & version**: v1 submitted Fri, 18 Sep 2026 07:39:47 UTC (382 KB); only version — `v2` endpoint returns HTTP 406 Not Found (checked 2026-09-25).
- **Publication status**: Accepted at **PRICAI 2026** (Pacific Rim International Conference on Artificial Intelligence). Comments field on arXiv landing page: *"11 pages, 1 figure, 2 tables. Accepted at PRICAI 2026"*.
- **Canonical DOI**: DataCite `10.48550/arXiv.2609.21427` (resolves HTTP 302 -> `https://arxiv.org/abs/2609.21427` -> 200, checked 2026-09-25).
- **Licence**: arXiv.org perpetual non-exclusive distribution license. This record cites, normalizes, and audits mathematical relationships and reported numerical values; no wholesale text redistribution.
- **Pinned primary source**: `https://arxiv.org/html/2609.21427v1`, 157,748 bytes, SHA-256 `82f7f097c40f3531908d4e99da35d9b918791fa99ec5339aa872d2018c43709b`, converted to 31,754 characters / 439 lines and read end to end on 2026-09-25 (Abstract, Sections 1–4, Tables 1–2, Figure 1 caption, References).
- **Keywords printed by source**: Decision-focused learning, Portfolio optimization, Bilevel optimization, Karush–Kuhn–Tucker conditions.
- **Code & data availability**:
  - Code: **No repository URL, no open-source repository link, and no replication scripts are provided in the text** (0 hits for `github.com`, `gitlab`, `code repository`, `script link`). The authors state the implementation was written in Python using the Pyomo optimization modeling language and the Artelys KNITRO 15.0 commercial NLP solver, alongside open-source Clarabel 0.11.1 (for baseline QPs/LPs) and qpth (for IPO-GRAD QP layers). The empirical code pipeline is therefore a `data gap`.
  - Data: Monthly adjusted closing prices from Yahoo Finance (`https://finance.yahoo.com/`) over January 2003 – December 2025.
- **Repository deduplication audit (2026-09-25)**: Whole-repository grep across all 968 tracked markdown records and `coverage_manifest.csv` confirmed zero prior records containing `2609.21427`, `10.48550/arXiv.2609.21427`, `Nosaka`, `Shunnosuke Ikeda`, `Yuichi Takano`, `KKT-Based Reformulation`, or `DFL-KKT`. Adjacent decision-focused portfolio records in this repository (`smart-predict-then-optimize-spo-plus-robust-portfolio-2026-09-05.md`, `decision-focused-sparse-tangent-portfolio-dpp-topk-2026-09-03.md`, `cost-sensitive-online-window-expert-aggregation-hedge-fixed-share-2026-09-25.md`) study different papers, distinct surrogate loss bounds, top-k ranking relaxations, or online window expert aggregations; none formulate or evaluate the exact single-level KKT MPEC reformulation with anchor regularization.

## Economic mechanism

### Source-reported

Markowitz Mean–Variance Optimization (MVO) formulates the fundamental trade-off between expected return and risk:
$$\min_{w \in \mathcal{S}} c(w; \bar{r}, V) := \frac{\delta}{2} w^\top V w - (1-\delta) \bar{r}^\top w$$
where $n$ is the number of assets, $w \in \mathbb{R}^n$ is the portfolio weight vector on the budget and short-sale constrained simplex $\mathcal{S} := \{w \in \mathbb{R}^n \mid \mathbf{1}^\top w = 1, w \ge \mathbf{0}\}$, $\bar{r} \in \mathbb{R}^n$ is expected return, $V \in \mathbb{R}^{n \times n}$ is a positive-definite covariance matrix ($V \succ O$), and $\delta \in (0,1)$ is the risk-aversion parameter (§2.1).

In conventional two-stage prediction-focused learning (PFL), return models $\hat{r}_{ti}(\theta_i) = \theta_i^\top \tilde{x}_{ti}$ are trained by minimizing mean squared prediction errors on returns. However, prediction accuracy is misaligned with downstream portfolio decision quality (§1.1):
1. In MVO, constraints (budget and no short-sales) govern allocation structures, and even minor prediction errors can trigger large swings in optimal portfolio weights and downstream performance.
2. Decision-focused learning (DFL) addresses this by directly minimizing the downstream decision loss:
   $$\ell_t(\Theta) := c(\hat{w}_t(\Theta); r_t, V_t) - c(w_t^{\text{oracle}}; r_t, V_t)$$
   where $w_t^{\text{oracle}} \in \arg\min_{w \in \mathcal{S}} c(w; r_t, V_t)$ is the hindsight ground-truth optimal portfolio under realized returns $r_t$.
3. Existing DFL methods introduce approximations that sacrifice exactness or tractability:
   - SPO+ (Elmachtoub & Grigas 2022) minimizes a convex surrogate upper bound rather than the true decision loss.
   - IPO-CF (Butler & Kwon 2023) drops short-sale constraints to obtain closed-form unconstrained derivatives, creating a structural mismatch when evaluating on constrained portfolios.
   - IPO-GRAD (Butler & Kwon 2023 via OptNet/qpth) unrolls gradients iteratively through a differentiable QP layer, which is computationally expensive and prone to gradient instability.
4. The proposed method (DFL-KKT) converts the bilevel optimization problem into a single-level Mathematical Program with Equilibrium Constraints (MPEC) by replacing the lower-level convex MVO with its exact Karush–Kuhn–Tucker (KKT) optimality conditions (§2.3):
   - Stationarity: $\delta V_t w_t - (1-\delta) \hat{r}_t(\Theta) - \mu_t \mathbf{1} - \lambda_t = \mathbf{0}, \forall t \in [T]$
   - Primal feasibility: $\mathbf{1}^\top w_t = 1, w_t \ge \mathbf{0}, \forall t \in [T]$
   - Dual feasibility: $\lambda_t \ge \mathbf{0}, \forall t \in [T]$
   - Complementary slackness: $\lambda_t \odot w_t = \mathbf{0}, \forall t \in [T]$
5. Because the complementarity conditions make the MPEC nonconvex and sensitive to initialization, the authors augment the upper-level objective with an $L_2$ anchor regularization term (§2.4):
   $$\min_{\Theta, \{w_t, \mu_t, \lambda_t\}_{t=1}^T} \frac{1}{T} \sum_{t=1}^T \left(\frac{\delta}{2} w_t^\top V_t w_t - (1-\delta) r_t^\top w_t\right) + \eta \|\text{vec}(\Theta - \Theta_{\text{ref}})\|_2^2$$
   subject to the KKT constraints, where $\eta \ge 0$ is a regularization parameter and $\Theta_{\text{ref}}$ is a reference parameter obtained from a fast baseline (such as IPO-CF or PFL).

### Research interpretation

The hypothesized mechanism is that embedding exact KKT conditions forces linear return predictors $\Theta$ to align directly with the active constraint set of the downstream portfolio QP. In standard MSE regression, equal weight is given to prediction errors across all assets. In MVO, assets with zero weight ($w_{ti}=0$) do not affect portfolio returns, and errors among them are irrelevant unless they falsely cross into positive weight. Conversely, small ranking errors between assets near the selection threshold cause large weight shifts. KKT-based DFL weights prediction errors by the shadow prices (dual multipliers $\lambda_t$ and $\mu_t$) induced by the portfolio constraints, focusing model capacity where it changes capital allocation.

Crucially, the mechanism is an **allocation-alignment and regularized decision-loss optimization** hypothesis applied to simple trailing momentum/volatility factors—**not** an exogenous informational discovery. The underlying inputs are purely trailing returns and realized volatilities of liquid ETFs. The anchor regularization term acts as a shrinkage prior toward the closed-form unconstrained or least-squares solution, preventing the non-convex MPEC solver from falling into degenerate local minima.

## Signal

All items are `source-reported` from §2 and §3 unless explicitly marked `research-proposed`.

- **Formation timestamp**: Monthly rebalancing cadence (`source-reported`). End-of-month adjusted close prices used (`source-reported`). All input features are computed strictly using information available up to the rebalancing date (`source-reported`). Training targets strictly exclude the current investment period to prevent look-ahead bias (`source-reported`). Exact execution clock time (e.g., strike on month-end close vs next-bar open) is unstated in source (`data gap`); next-bar market-open execution is `research-proposed`.
- **Lookback window**:
  - Feature lookback ($m=4$ features): 1-month average return, 3-month average return, 12-month average return, and 12-month realized volatility at each rebalancing date (`source-reported`).
  - Intercept: Augmented feature vector $\tilde{x}_{ti} = (x_{ti}^\top, 1)^\top \in \mathbb{R}^{m+1}$ with $m+1 = 5$ parameters per asset (`source-reported`).
  - Rolling training window: Most recent 48 months of monthly data ($T=48$), shifted forward monthly (`source-reported`).
  - Covariance window: 48 months of returns; estimated by applying Oracle Approximating Shrinkage (OAS, Chen et al. 2010) to an exponentially weighted moving average (EWMA) covariance estimator with decay factor $\alpha=0.97$ (`source-reported`).
- **Long / short & constraints**: Strict long-only simplex: $\mathbf{1}^\top w = 1, w \ge \mathbf{0}$. No short sales, no leverage, no borrowing (`source-reported`).
- **Rebalancing & holding period**: Monthly rebalancing; positions held for 1 month until the next rebalancing date (`source-reported`).
- **Optimization parameters**:
  - Risk-aversion parameter: Fixed at $\delta = 0.5$ across all methods (`source-reported`).
  - Regularization parameter $\eta$: Selected via grid search on the validation period (Jan 2011 – Dec 2015) over $\{0, 0.01, 0.05, 0.1, 0.5, 1, 5, 10, 50, 100, 500\}$ based on highest validation Sharpe Ratio (`source-reported`). Selected values: $\eta = 0.5$ for the International universe and $\eta = 0.01$ for the Sector universe (under IPO-CF reference) (`source-reported`).
  - Reference parameter $\Theta_{\text{ref}}$: IPO-CF solution at each rebalancing date (`source-reported`).
- **Solver configuration**:
  - Upper-level MPEC: Solved directly with Artelys KNITRO 15.0 via Pyomo in Python (`source-reported`). Feasibility and optimality tolerances set to $10^{-6}$, iteration budget up to 20,000 iterations, per-solve time limit of 500 seconds (`source-reported`). Residuals for the KKT system remained below $6.6 \times 10^{-9}$ across all rebalancing dates, with zero convergence failures (`source-reported`).
  - Baseline solvers: Clarabel 0.11.1 for MVO and SPO+ LP surrogate solves; qpth for IPO-GRAD QP layer with Adam (learning rate $10^{-3}$, 500 epochs, patience 50) (`source-reported`).
- **Operational specifications not in source (`research-proposed`)**:
  - Rebalancing execution time: Next-day open fill model (`research-proposed`).
  - Cash / margin yield: Benchmark risk-free rate for Sharpe calculation (SOFR / 3-month T-bill) (`research-proposed`).
  - Minimum trade threshold / position trimming: No lot sizing or minimum trade rebalance threshold is stated in source (`data gap`).

## Required data

Source-reported (§3.1):

| Parameter | Universe 1: International Equity ETFs | Universe 2: Sector Equity ETFs |
|---|---|---|
| **Constituents** | 8 developed-market country ETFs (DeMiguel et al. 2009): US, Canada, France, Germany, Italy, Japan, Switzerland, UK | 9 S&P 500 GICS sector ETFs: Information Technology, Financials, Health Care, Energy, Consumer Discretionary, Consumer Staples, Industrials, Utilities, Materials |
| **Representative Tickers** | SPY (or IVV), EWC, EWQ, EWG, EWI, EWJ, EWL, EWU | XLK, XLF, XLV, XLE, XLY, XLP, XLI, XLU, XLB |
| **Asset Count ($n$)** | $n = 8$ | $n = 9$ |
| **Data Vendor** | Yahoo! Finance (`https://finance.yahoo.com/`) | Yahoo! Finance (`https://finance.yahoo.com/`) |
| **Field** | Monthly adjusted closing prices | Monthly adjusted closing prices |
| **Total Span** | January 2003 – December 2025 (276 months) | January 2003 – December 2025 (276 months) |
| **Validation Window** | January 2011 – December 2015 (60 months) | January 2011 – December 2015 (60 months) |
| **Test Window** | January 2016 – December 2025 (120 months) | January 2016 – December 2025 (120 months) |

- **Fields required**: Monthly adjusted closing prices only (`source-reported`). No intraday data, tick data, order book, volume, open interest, or alternative data fields are used (`source-reported`).
- **Point-in-time / Survivorship status**: Fails point-in-time universe construction by design (`data gap`). Sector ETFs were selected based on being "available throughout the experimental period" (excluding Real Estate XLRE and Communication Services XLC) (`source-reported`). This imposes survivorship/backfill conditioning.
- **Missing data / corporate actions**: Handled via Yahoo Finance's split- and dividend-adjusted closing price series (`source-reported`).

## Execution assumptions

- **Transaction costs**: **Zero transaction costs, commissions, or slippage are deducted from returns in the source** (`data gap`). The paper evaluates gross returns.
- **Turnover reported**: Average portfolio turnover per rebalancing period, defined as $\text{TO} = \frac{1}{T} \sum_{t=1}^T \sum_{i=1}^n |w_{i,t+1} - w_{i,t}^+|$, where $w_{i,t}^+$ is portfolio weight before rebalancing (DeMiguel et al. 2009) (`source-reported`):
  - International: $\text{TO} = 0.991$ (DFL-KKT) vs 0.299 (IPO-GRAD), 1.088 (IPO-CF), 0.173 (SPO+), 1.138 (PFL), 0.016 (1/N), 0.000 (S&P 500) (`source-reported`).
  - Sector: $\text{TO} = 0.855$ (DFL-KKT) vs 0.685 (IPO-GRAD), 1.136 (IPO-CF), 0.319 (SPO+), 1.220 (PFL), 0.025 (1/N), 0.000 (S&P 500) (`source-reported`).
- **Cost coverage audit (word scan across pinned text, 2026-09-25)**: `transaction cost` **0**, `slippage` **0**, `spread` **0**, `bid-ask` **0**, `commission` **0**, `fee` **0**, `market impact` **0**, `latency` **0**, `execution` **0**, `capacity` **0**, `cost` **2** (both referencing computational solver run-time). Spread, slippage, execution delay, and market impact are completely omitted by the primary source → `data gap`, never read as zero in live trading.
- **Execution timing**: Instantaneous rebalance at monthly bar boundaries (`source-reported` implicit setup). Next-bar open execution is `research-proposed`.
- **Shorting / Borrow / Margin**: None. Strict long-only simplex $\sum w_i = 1, w_i \ge 0$ (`source-reported`).
- **Capacity**: Unstated in source (`data gap`). Universe consists of highly liquid mega-cap ETFs ($>\$1\text{B}$ AUM, high ADV), where market impact for modest book sizes is minimal, but high turnover creates steady fee drag.

## Evidence

### Source-reported

All figures below are `source-reported` from `arXiv:2609.21427v1` (Tables 1 and 2, test period January 2016 – December 2025, $N = 120$ monthly investment periods). Initial wealth normalized to 1.0. None has been independently reproduced.

**Table 1: Performance comparison on the International Universe (8 developed-market country ETFs):**

| Method | Sharpe Ratio (SR ↑) | Final Wealth (FW ↑) | Cumulative Decision Loss (CDL ↓) | CVaR95 % (↓) | Turnover (TO ↓) |
|---|---|---|---|---|---|
| **DFL-KKT** | **1.101** | **4.590** | **1.644** | 9.180 | 0.991 |
| IPO-GRAD | 0.984 | 3.869 | 1.719 | **8.795** | 0.299 |
| IPO-CF | 0.634 | 2.526 | 1.924 | 11.496 | 1.088 |
| SPO+ | 0.633 | 3.027 | 1.846 | 12.422 | 0.173 |
| PFL | 0.785 | 3.197 | 1.820 | 10.031 | 1.138 |
| 1/N | 0.747 | 2.774 | 1.902 | 9.481 | 0.016 |
| S&P 500 | 1.042 | 4.184 | — | 9.246 | **0.000** |

**Table 2: Performance comparison on the Sector Universe (9 S&P 500 GICS sector ETFs):**

| Method | Sharpe Ratio (SR ↑) | Final Wealth (FW ↑) | Cumulative Decision Loss (CDL ↓) | CVaR95 % (↓) | Turnover (TO ↓) |
|---|---|---|---|---|---|
| **DFL-KKT** | **1.136** | **6.490** | **2.969** | 9.454 | 0.855 |
| IPO-GRAD | 0.934 | 4.851 | 3.116 | 11.568 | 0.685 |
| IPO-CF | 0.426 | 1.900 | 3.560 | 14.439 | 1.136 |
| SPO+ | 0.809 | 4.083 | 3.241 | 10.868 | 0.319 |
| PFL | 0.630 | 2.810 | 3.392 | 11.812 | 1.220 |
| 1/N | 0.931 | 3.480 | 3.321 | 9.450 | 0.025 |
| S&P 500 | 1.042 | 4.184 | — | **9.246** | **0.000** |

**Solver convergence & stability (§3.1)**:
- Optimality and feasibility residuals for the KKT system (8)–(11) remained below $6.6 \times 10^{-9}$ across all training rebalancing windows under KNITRO 15.0 (`source-reported`).
- Zero convergence failures across all 120 rebalancing periods (`source-reported`).

**Effect of Regularization (§3.3 & Figure 1)**:
- Regularization consistently improved cumulative wealth over the unregularized variant ($\eta = 0$) across both universes under both $\Theta_{\text{IPO-CF}}$ and $\Theta_{\text{PFL}}$ reference parameters (`source-reported`).
- Trajectories are plotted visually in Figure 1(a–d); numeric trajectory values are not printed (`data gap`).

### Independently reproduced

`Not independently reproduced.` This scout run performed direct full-text reading of `arXiv:2609.21427v1`, audited mathematical equations (1)–(13), checked table cells, performed cost-term text scans, and verified landing metadata. No code was executed, no optimization was solved, and no backtest was re-run.

### Negative evidence

1. **Gross-only returns and severe turnover drag**: DFL-KKT generates an average monthly turnover of 0.991 (International) and 0.855 (Sector), reallocating nearly 100% of portfolio capital every month. Over the 120-month test window, cumulative turnover is $120 \times 0.991 = 118.9\times$ (International) and $120 \times 0.855 = 102.6\times$ (Sector). Charging a realistic round-trip institutional cost of 5–10 bps on $118.9\times$ turnover consumes $5.9\%$ to $11.9\%$ of portfolio value, which completely eliminates the modest excess final wealth over buy-and-hold S&P 500 (4.590 vs 4.184 gross = +9.7% margin).
2. **Fragility of edge over passive benchmark**: On the International universe, DFL-KKT's gross Sharpe Ratio is 1.101 vs passive S&P 500 ETF (SPY) Sharpe Ratio of 1.042 (an advantage of only +0.059 SR). When transaction costs and execution friction are applied, DFL-KKT likely underperforms passive buy-and-hold.
3. **Turnover inefficiency relative to other DFL formulations**: DFL-KKT's turnover is $3.3\times$ to $5.7\times$ higher than SPO+ (0.991 vs 0.173 on International; 0.855 vs 0.319 on Sector) and up to $3.3\times$ higher than IPO-GRAD (0.991 vs 0.299 on International). SPO+ and IPO-GRAD produce significantly more stable portfolios with less trading churn.
4. **Zero statistical inference or confidence intervals**: The paper reports only single point estimates over the 10-year period (2016–2025). Word scan for `t-stat`, `p-value`, `confidence interval`, `bootstrap`, `significan*` yielded 0 hits. No paired t-tests or bootstrap resamples confirm whether DFL-KKT's outperformance over IPO-GRAD or S&P 500 is statistically distinguishable from noise.
5. **Proprietary commercial solver dependency**: DFL-KKT relies on Artelys KNITRO 15.0, a costly commercial NLP solver. The authors acknowledge that at larger asset dimensions, specialized solvers may become computationally impractical (§4). MPECs inherently violate standard linear independence constraint qualification (LICQ) at points where both primal and dual slackness are zero ($w_{ti} = 0$ and $\lambda_{ti} = 0$), making open-source solvers (such as Ipopt) prone to premature convergence failures without special smoothing.
6. **Survivorship bias in ETF selection**: Only ETFs with unbroken history from 2003 to 2025 were retained. ETFs liquidated or restructured during this span are omitted.
7. **Absence of open-source replication repository**: No code repository is published by the authors, preventing direct reproduction without reimplementing the Pyomo MPEC formulation.

## Falsification plan

Every test below carries an explicit decision rule; failure results in rejection of the hypothesis and maintains `research-only` / `not-approved` status:

1. **F1 — Transaction cost ladder** (`research-defined falsification threshold`): Re-evaluate DFL-KKT net of transaction costs across a cost ladder of 0, 5, 10, 15, 20, and 30 bps per unit of turnover (half-spread + fee). **Fails if** DFL-KKT's net Sharpe Ratio falls below passive S&P 500 (1.042) or equal-weight 1/N at a cost of $\le 10$ bps on the International universe, or if net Final Wealth underperforms buy-and-hold.
2. **F2 — Open-source solver substitution audit** (`research-proposed`): Replace commercial KNITRO 15.0 with open-source Ipopt (using complementarity relaxation / smoothing) or a penalty formulation in Python. **Fails if** solve failure / convergence error rate exceeds 5% of monthly rebalancing periods, or if solution quality degrades Sharpe Ratio by $>0.15$ relative to KNITRO.
3. **F3 — Sub-period stability and statistical significance** (`research-defined falsification threshold`): Perform a moving-block bootstrap (5-month blocks, 10,000 resamples) and split-sample test (2016–2020 vs 2021–2025). **Fails if** the paired return difference between DFL-KKT and the best baseline (IPO-GRAD or S&P 500) fails to achieve a two-sided p-value $< 0.05$ (paired $t \ge 1.96$), or if DFL-KKT underperforms in either 5-year sub-period.
4. **F4 — Next-bar open execution audit** (`research-proposed`): Re-run backtest assuming rebalancing orders are filled at the market open on the first trading day of month $t+1$ rather than the same-bar close of month $t$. **Fails if** execution delay from close to open degrades net Sharpe Ratio by more than 0.10.
5. **F5 — Turnover-regularized MPEC ablation** (`research-proposed`): Add an explicit $L_1$ turnover penalty $c \|w_t - w_{t-1}\|_1$ directly into the MVO objective or upper-level loss. **Fails if** DFL-KKT cannot maintain its performance advantage over SPO+ when turnover is constrained to $\le 0.30$ per month.
6. **F6 — Expanded asset universe scaling** (`research-proposed`): Expand the asset universe from 8–9 liquid ETFs to a broader basket of 30–50 assets (e.g. S&P 100 or DJIA components). **Fails if** MPEC solve time exceeds 500 seconds or fails to converge in $>10\%$ of rebalancing dates.

## Crypto portability

`unproven`

The primary source evaluates **only US-listed developed-market and sector equity ETFs**. Portability to crypto is unproven and subject to substantial structural hurdles:

- **Market type**: The MVO formulation assumes long-only weights on a simplex ($\mathbf{1}^\top w = 1, w \ge \mathbf{0}$). In crypto perpetual markets, market-neutral long-short portfolios are standard; restricting to long-only spot exposes the book to severe crypto market drawdowns and beta.
- **24/7 session structure**: The paper operates on monthly calendar closes from Yahoo Finance. In crypto, trading is continuous without market closes; a 00:00 UTC monthly or weekly boundary must be defined (`research-proposed`).
- **High turnover & fee friction**: DFL-KKT turns over 85% to 99% of portfolio capital per month. In crypto spot/perpetual markets with typical taker fees of 2–5 bps plus bid-ask spread and market impact, high turnover creates severe performance drag.
- **Correlation and tail risk**: Crypto assets exhibit higher cross-asset correlations, non-stationary volatility regimes, and extreme left-tail jump risks that challenge standard Gaussian-based quadratic variance terms and OAS shrinkage.
- **Contract / margin mechanics**: Funding rates, margin requirements, liquidation thresholds, and quote-currency risk are absent from the source's model (`data gap`).

## Limitations

- `underspecified`: Exact execution price convention (close vs next open), risk-free rate convention for Sharpe calculation, minimum lot size, and trade threshold rules.
- `data gap`: Zero transaction costs, commissions, slippage, latency, market impact, or borrow fees modeled in the paper. Code repository URL absent. Trajectory values in Figure 1 are visual plots only without numeric tables.
- `not independently reproduced`: All numerical figures are source-reported from `arXiv:2609.21427v1`.
- Commercial solver dependency: Relies on proprietary Artelys KNITRO 15.0; feasibility under open-source solvers is untested.
- Survivorship bias in ETF selection: Only ETFs with unbroken history from 2003 to 2025 were retained.
- Lack of statistical inference: No bootstrap confidence intervals, p-values, or sub-period significance tests are provided by the authors.

## Implementation status

`implementation_status: not-implemented`

Nothing from this record has been implemented in our research stack: no Pyomo/KNITRO MPEC solver has been run, no portfolio model built, no backtest run, and no Qlib, Paper, Testnet, or Live activity conducted. This document is a normalized research capture and provenance audit only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`

Presence of this record in the staging repository does **not** mean:
- Passed Research Intake Review;
- Entered Hermes Wiki Brain;
- Entered the production candidate pool;
- Completed Qlib full-backtest validation;
- Became a frozen survivor or leaderboard entry;
- Validated alpha or profitable;
- Approved for implementation, Paper, Testnet, or Live.

The mechanism is a portfolio optimization / loss-alignment framework tested on historical ETF data under zero transaction costs, not an approved trading strategy.

## Related Wiki records

- `[[quant/smart-predict-then-optimize-spo-plus-robust-portfolio-2026-09-05]]` — Explores decision-focused learning for portfolio optimization under SPO+ surrogate loss with turnover penalties; contrasts with DFL-KKT's exact single-level KKT reformulation.
- `[[quant/finance-grounded-loss-functions-band-turnover-crypto-2026-09-05]]` — Investigates finance-grounded loss functions and turnover-band penalties for portfolio management.
- `[[quant/simple-dynamic-stock-bond-gold-markowitz-volatility-control-2026-09-11]]` — Dynamic Markowitz allocation with volatility control on multi-asset ETF universes.
- `[[quant/tda-persistent-homology-finbert-sentiment-portfolio-optimization-2026-09-02]]` — Dynamic mean-variance portfolio construction with market regime conditioning.

Adjacent records already in this repository (dedup and contrast):
- `smart-predict-then-optimize-spo-plus-robust-portfolio-2026-09-05.md` (`arXiv:2601.04062v3`, Wang & Hasuike) — Uses PyEPO SPO+ surrogate upper bound with turnover costs; DFL-KKT uses exact KKT conditions without surrogate losses.
- `decision-focused-sparse-tangent-portfolio-dpp-topk-2026-09-03.md` — Uses DPP / top-k differentiable ranking for sparse tangent portfolios; DFL-KKT formulates an MPEC for standard MVO.
- `cost-sensitive-online-window-expert-aggregation-hedge-fixed-share-2026-09-25.md` (`arXiv:2609.29887v1`, Liu & Hsieh) — Aggregates rolling window sizes via online learning (Hedge/Fixed Share); DFL-KKT trains return prediction models end-to-end via KKT reformulation.

## Sources

1. Nosaka, K., Ikeda, S., & Takano, Y. (2026). *Decision-Focused Learning for Mean–Variance Portfolio Optimization via KKT-Based Reformulation*. arXiv:2609.21427v1 [cs.LG], submitted 18 September 2026. Accepted at PRICAI 2026 (Pacific Rim International Conference on Artificial Intelligence). Stable URL: https://arxiv.org/abs/2609.21427. Full text: https://arxiv.org/html/2609.21427v1 (157,748 bytes; SHA-256 `82f7f097c40f3531908d4e99da35d9b918791fa99ec5339aa872d2018c43709b`), read end to end on 2026-09-25. Canonical DataCite DOI: https://doi.org/10.48550/arXiv.2609.21427.
2. Version/metadata audit (all 2026-09-25): `https://arxiv.org/abs/2609.21427v2` -> HTTP 406; `https://arxiv.org/html/2609.21427v2` -> HTTP 406. Landing page shows comments "11 pages, 1 figure, 2 tables. Accepted at PRICAI 2026". License: arXiv.org perpetual non-exclusive license.
3. Methodological antecedents cited by the source (recorded for provenance only): Markowitz (1952) MVO; Elmachtoub & Grigas (2022) SPO+; Butler & Kwon (2023) IPO; Bucarey et al. (2024) pessimistic bilevel optimization and KKT reformulation; DeMiguel et al. (2009) 1/N benchmark and turnover definition; Chen et al. (2010) Oracle Approximating Shrinkage (OAS); Artelys KNITRO 15.0; Pyomo; Clarabel 0.11.1; qpth (Amos & Kolter 2017).
