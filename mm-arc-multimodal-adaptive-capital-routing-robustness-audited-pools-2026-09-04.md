---
schema: strategy-research-record-v1
title: "MM-ARC: Multimodal Adaptive Routing of Capital with Robustness-Audited Strategy Pools"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - multimodal-learning
  - mixture-of-experts
  - capital-routing
  - bayesian-optimization
  - portfolio-optimization
status: research-only
confidence: medium
source_as_of: 2026-07-28
sources:
  - "https://arxiv.org/abs/2509.05080"
  - "https://arxiv.org/html/2509.05080v3"
  - "https://doi.org/10.48550/arXiv.2509.05080"
  - "https://anonymous.4open.science/r/MM-ARC-32F7"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# MM-ARC: Multimodal Adaptive Routing of Capital with Robustness-Audited Strategy Pools

## Provenance

- **Primary Source:** Yang Chen (Zhejiang University), Yuchen Cao (City University of Hong Kong), Jacky Keung (City University of Hong Kong), Leilei Gan (Zhejiang University), Kun Kuang (Zhejiang University), Yueheng Jiang (Zhejiang University), Zhaozhao Ma (Zhejiang University), Jianping Zhu (Dalian University of Technology), Fei Wu (Zhejiang University), and Jinpeng Li (Zhejiang University), *"MM-ARC: Multimodal Adaptive Routing of Capital with Robustness-Audited Strategy Pools"*, arXiv preprint `arXiv:2509.05080v3 [q-fin.TR]`, submitted September 2025, revised July 2026.
- **Canonical URLs:**
  - Abstract: [https://arxiv.org/abs/2509.05080](https://arxiv.org/abs/2509.05080)
  - Full Text (HTML v3): [https://arxiv.org/html/2509.05080v3](https://arxiv.org/html/2509.05080v3)
  - PDF: [https://arxiv.org/pdf/2509.05080](https://arxiv.org/pdf/2509.05080)
  - DOI: [10.48550/arXiv.2509.05080](https://doi.org/10.48550/arXiv.2509.05080)
- **Code & Experiment Artifacts:** Anonymous reproduction repository at [https://anonymous.4open.science/r/MM-ARC-32F7](https://anonymous.4open.science/r/MM-ARC-32F7).
- **Verification Method:** Direct reading of the primary paper full text (arXiv:2509.05080v3), mathematical derivations, experimental setup, and all numeric diagnostics in Tables 1–21.
- **Deduplication Audit:** A repository-wide and Hermes Wiki Brain search confirmed zero prior records referencing `arXiv:2509.05080`, "MM-ARC", "Robustness-Audited Bayesian Optimization", or "RABO".

## Economic mechanism

### Source-reported

Financial markets are non-stationary decision environments where predictive evidence is distributed across price sequences, chart geometry, and textual market summaries. A system that predicts price direction accurately can nevertheless fail as a practical trading engine when its component signals compete for capital without coordination, violate cross-asset portfolio constraints, or dissipate through excessive turnover and transaction costs. 

Existing financial language models and mixture-of-experts (MoE) architectures route representations or computational tokens rather than capital. An allocation router in quantitative portfolio management must allocate actual capital weights, where mistakes directly generate unwanted leverage, turnover friction, and drawdown cascades. Conversely, repeated heuristic or Bayesian optimization (BO) search over unconstrained strategy candidates enlarges the effective hypothesis space and severely amplifies data-snooping and backtest overfitting.

MM-ARC resolves this tension through four interlocking structural mechanisms:
1. **Multimodal State Fusion:** Aligns three causal representations derived from the exact same 100-bar OHLCV window: a visual chart view (candlestick and CYC-MRKAB multi-indicator overlay), a numerical view (OHLCV time series and technical indicators), and a structured-text view (deterministic technical summary of trends, support/resistance, and volume).
2. **Adaptive Continuous Capital Routing:** Rather than selecting a single discrete expert, a regime-conditioned router produces continuous simplex-valued capital allocations ($w_{t,u} \in \Delta^4$) across four interpretable strategy experts (trend, reversal, breakout, exposure control). The router combines fused multimodal embeddings, a supervised fine-tuning (SFT) regime prior, and historical validation robustness scores.
3. **Market-Shared Strategy Pools with Bounded Asset Residuals:** Instead of maintaining $744$ asset-specific pools ($62 \text{ assets} \times 4 \text{ experts} \times 3 \text{ regimes}$), MM-ARC pools strategies into $60$ market-expert-regime pools ($5 \text{ markets} \times 4 \text{ experts} \times 3 \text{ regimes}$). Asset-level personalization is restricted to bounded numeric parameter residuals ($\delta_{u,j}$), preventing categorical or structural divergence and dramatically shrinking the search space.
4. **Robustness-Audited Bayesian Optimization (RABO):** Replaces validation-peak maximization with a five-term composite rank audit across purged validation blocks: matched-block benchmark exceedance ($R_P$), 5% lower-tail quantile ($R_{Q_5}$), median performance ($R_{\text{med}}$), local parameter stability under 5% perturbation ($R_{\text{stab}}$), and realized turnover ($R_{\text{turn}}$).
5. **Market-Feasible Portfolio Projection Layer:** Synchronizes raw expert targets on native market calendars and projects them onto convex operational constraints (gross exposure, position limits, long-only feasibility for A-shares, margin, cash, and turnover penalties) before submitting executable orders.

### Research interpretation

The falsifiable quantitative thesis of MM-ARC is that:
1. **Regime-Conditioned Simplex Gating:** Dynamic reallocation of capital among orthogonal, interpretable strategy families (momentum, mean-reversion, breakout, exposure reduction) produces superior risk-adjusted returns and shallower drawdowns than either fixed-weight diversification or discrete regime-switching, because real market regimes exhibit continuous grade transitions rather than discrete state jumps.
2. **Downside-Distribution Selection Over Peak-Fitting:** Selecting strategies by lower-tail empirical performance ($Q_5$) and parameter-neighborhood flatness ($S(x)$) successfully immunizes the admitted pool against selection bias / backtest overfitting, effectively trading away marginal in-sample upside for out-of-sample survival.
3. **Hierarchy Regularization:** Constraining asset-level parameters as small bounded residuals around market-level parent strategies acts as structural shrinkage, preventing individual assets with noisy histories from inventing spurious rules while preserving cross-asset market coherence.

## Signal

### Mathematical Formulation

Let $m \in \mathcal{M}$ index an asset class / market and $u \in \mathcal{U}_m$ index an individual asset. At decision time $t$ (market close):

#### 1. Multimodal State Encoding & Regime Prior
Three synchronous views are constructed from the causal 100-bar window:
$$z_{t,u} = \operatorname{Encoder}(I_{t,u}, X_{t,u}, T_{t,u})$$
where:
- $I_{t,u}$: Visual branch (candlestick chart + CYC-MRKAB chart with 20/50/200 MAs, Bollinger Bands, MACD, RSI, KDJ).
- $X_{t,u}$: Numerical branch (100 daily OHLCV bars and technical indicator series normalized with training-only statistics).
- $T_{t,u}$: Structured-text branch (deterministic text summary of returns, volatility, moving-average ordering, support/resistance levels, and volume).
- $\operatorname{Encoder}$: Qwen3-VL-8B-Instruct adapted via 4-bit QLoRA.

The supervised regime prior over $r \in \{\text{uptrend}, \text{downtrend}, \text{sideways}\}$ is:
$$p_{t,u} = \operatorname{Softmax}(W_p z_{t,u} + b_p) \in \Delta^3$$

#### 2. Continuous Capital Router
The router produces continuous simplex-valued expert weights over $K=4$ experts:
$$w_{t,u} = \operatorname{Softmax}\left( W_g z_{t,u} + b_{g,m} + W_{\text{prior}} p_{t,u} + \eta_g c^{\text{rob}}_{m, \hat{r}_{t,u}} \right) \in \Delta^4$$
where:
- $k \in \{1: \text{trend}, 2: \text{reversal}, 3: \text{breakout}, 4: \text{exposure\_control}\}$.
- $\hat{r}_{t,u} = \arg\max_r p_{t,u,r}$ is the dominant predicted regime.
- $c^{\text{rob}}_{m, \hat{r}_{t,u}} \in \mathbb{R}^4$ is the historical validation robustness score vector of the admitted pools.
- $\eta_g \ge 0$ is the evidence tilt parameter.

#### 3. Expert Target Generation
Each expert $k$ emits a target exposure $h_{t+1 \mid t, u, k} \in [-1, 1]$ (expressed as a fraction of market portfolio NAV) according to typed schema rules. The unconstrained raw asset target is:
$$\tilde{h}_{t+1 \mid t, u} = \sum_{k=1}^4 w_{t,u,k} h_{t+1 \mid t, u, k}$$

#### 4. Market-Feasible Convex Projection Layer
For each market portfolio $m$, the raw target vector $\tilde{h}_{t+1 \mid t, m}$ is projected onto the feasible operational set $\mathcal{C}_m$:
$$h^*_{t+1 \mid t, m} = \arg\min_{h \in \mathcal{C}_m} \frac{1}{2} \| h - \tilde{h}_{t+1 \mid t, m} \|_2^2 + \lambda_{\text{turn}} \| h - h^*_{t,m} \|_1$$
where $\mathcal{C}_m$ enforces:
- Gross exposure cap: $\sum_{u \in \mathcal{U}_m} |h_u| \le L_m^{\max}$.
- Per-asset position limit: $|h_u| \le H_{u,m}^{\max}$.
- Directional restrictions: $h_u \ge 0$ for A-shares (long-only); margin caps for equities and crypto.
- Cash buffer requirements.

The executed rebalance order submitted at the next tradable open is:
$$q_{t+1,m} = h^*_{t+1 \mid t, m} - h^*_{t,m}$$

#### 5. Executed Credit & Exposure Attribution
To reconcile post-projection holdings back to expert contributions without leakage:
$$a^{\pm}_{t+1 \mid t, u, k} = \frac{\operatorname{ReLU}(\pm w_{t,u,k} h_{t+1 \mid t, u, k}) + \epsilon}{\sum_{k'=1}^4 \operatorname{ReLU}(\pm w_{t,u,k'} h_{t+1 \mid t, u, k'}) + 4\epsilon}$$
The attributed executed expert holding is:
$$h^*_{t+1 \mid t, u, k} = a^+_{t+1 \mid t, u, k} \operatorname{ReLU}(h^*_{t+1 \mid t, u}) - a^-_{t+1 \mid t, u, k} \operatorname{ReLU}(-h^*_{t+1 \mid t, u})$$
Transaction costs are allocated based on post-projection executed turnover, not raw unexecuted proposals.

#### 6. Robustness-Audited Strategy Admission (RABO)
Candidate strategies $x = (s, \theta)$ proposed by Bayesian Optimization are evaluated on synchronized market portfolios over purged validation blocks $\mathcal{B}_m^{\text{val}}$.
The composite admission score is:
$$J_R(x) = \frac{1}{5} \left( R_P(x) + R_{Q_5^{\text{cand,val}}}(x) + R_{\text{med}}(x) + R_{\text{stab}}(x) + R_{\text{turn}}(x) \right)$$
where within each pool update:
- $R_P(x)$: Ranks matched-block benchmark exceedance $P(J_{\text{pool}}(x) > J_{\text{bench}})$ against a fixed-seed reference $x_{m,k,r}^{\text{seed}}$.
- $R_{Q_5^{\text{cand,val}}}(x)$: Ranks the 5% quantile of the shrunk validation distribution $\mathcal{D}^{\text{shrunk}}_{m,k,r}(x)$.
- $R_{\text{med}}(x)$: Ranks the median validation return.
- $R_{\text{stab}}(x)$: Ranks parameter stability under one-at-a-time 5% coordinate perturbations:
  $$S(x) = \frac{1}{|\mathcal{N}(x)|} \sum_{x' \in \mathcal{N}(x)} \frac{J_{\text{loc}}(x')}{\max(|J_{\text{loc}}(x)|, \epsilon_{\text{stab}})}$$
- $R_{\text{turn}}(x)$: Ranks realized turnover (penalizing excessive churning).

Top 5 candidates enter the active pool $\mathcal{P}_{m,k,r}$. Sparse validation cells ($B_{\text{eff}} < B_{\min} = 20$) use hierarchical shrinkage toward the market-expert parent distribution:
$$\mathcal{D}^{\text{shrunk}}_{m,k,r}(x) = \gamma \mathcal{D}_{m,k,r}(x) + (1-\gamma) \mathcal{D}_{m,k}(x), \quad \gamma = \min(1, B_{\text{eff}} / B_{\min})$$

## Required data

- **Universe:** 62 real instruments across 5 distinct markets:
  1. China A-Shares: 10 large-cap liquid equities (SSE/SZSE).
  2. U.S. Equities: 15 large-cap liquid equities (NYSE/NASDAQ).
  3. Exchange-Traded Funds (ETFs): 15 liquid sector/asset ETFs.
  4. Commodity & Financial Futures: 20 liquid contracts (CME/ICE/SHFE).
  5. Cryptocurrencies: Bitcoin (BTC/USDT) and Ethereum (ETH/USDT).
- **History Length:** January 2017 to June 30, 2026 (crypto starts January 2021).
  - Training: January 2017 to December 2023.
  - Validation: January 2024 to June 2025.
  - Frozen Trading Holdout: July 1, 2025 to June 30, 2026.
- **Timeframe & Resolution:** Daily closing prices; orders executed at next market open.
- **Modality Data Requirements:**
  - Candlestick and CYC-MRKAB chart images rendered at $448 \times 448$ resolution.
  - Numerical OHLCV series + 20/50/200 MAs, Bollinger Bands, MACD, RSI, KDJ.
  - Deterministic technical text generated causally from the same window.
- **Point-in-Time & Leakage Controls:**
  - 90-session forward regime labels are strictly purged at split boundaries.
  - All source timestamps must precede or equal the decision cutoff $t$.
  - Futures contracts use lagged dominant-contract volume stitching and a dedicated roll ledger.

## Execution assumptions

- **Execution Timing:** Rebalance decision formed at daily close ($t$); projected order executed at next tradable open ($t+1$).
- **Transaction Costs:**
  - **Normalized Baseline Protocol:** Flat all-in one-way friction of 10 bps ($0.10\%$) per unit of executed one-way turnover:
    $$C_m(q_{t,m}) = c_{\text{norm}} \| q_{t,m} \|_1, \quad c_{\text{norm}} = 10 \text{ bps}$$
    Full portfolio liquidation and re-investment incurs $\approx 20 \text{ bps}$ round-trip.
  - **Market-Specific Friction Replacement Schedule:**
    - A-shares: 18 bps (incorporates commission, slippage, and sell-side stamp duty).
    - U.S. Equities: 8 bps (commission + spread/impact).
    - ETFs: 6 bps.
    - Futures: 5 bps (exchange fees, slippage, and roll costs).
    - Cryptocurrency: 25 bps (taker fees, bid-ask spread, slippage, and perpetual funding costs).
- **Trading Constraints:**
  - A-shares: Long-only feasibility ($h_u \ge 0$), $T+1$ execution rule, no short selling.
  - U.S. Equities & ETFs: Bounded long/short subject to Reg-T margin and borrow limits.
  - Futures: Leverage bounded by exchange maintenance margins.
  - Crypto: Bounded leverage, 24/7 continuous session, subject to funding rate settlement.

## Evidence

### Source-reported

All figures below are directly reported by Chen et al. (arXiv:2509.05080v3, July 2026) evaluated over the frozen trading holdout (July 1, 2025 – June 30, 2026) across five training seeds (42–46):

#### 1. Main Equal-Market Results (Normalized 10-bps Cost Protocol, Table 2)
Equal-market summaries average 5 separately settled market portfolios:

| Method | Total Return (TR%) | Sharpe Ratio (SR) | Max Drawdown (MDD%) | Annualized One-Way Turnover |
| :--- | :---: | :---: | :---: | :---: |
| **Buy-and-Hold (B&H)** | $14.0 \pm 0.0$ | $0.58 \pm 0.00$ | $-24.7 \pm 0.0$ | $0.0\times$ |
| **Stochastic Technical Search** | $8.9 \pm 0.9$ | $0.45 \pm 0.03$ | $-20.3 \pm 0.6$ | — |
| **PPO** | $8.4 \pm 0.6$ | $0.45 \pm 0.06$ | $-18.3 \pm 0.3$ | $11.1\times$ |
| **Time-VLM-style** | $9.7 \pm 0.9$ | $0.49 \pm 0.06$ | $-18.5 \pm 0.5$ | $13.6\times$ |
| **FinAgent (adapted)** | $8.7 \pm 0.8$ | $0.44 \pm 0.03$ | $-20.6 \pm 0.3$ | $17.5\times$ |
| **LLMoE-style Routing** | $10.4 \pm 0.9$ | $0.53 \pm 0.05$ | $-18.3 \pm 0.4$ | $12.5\times$ |
| **MM-ARC (Proposed)** | $\mathbf{14.1 \pm 0.9}$ | $\mathbf{1.33 \pm 0.06}$ | $\mathbf{-13.7 \pm 0.2}$ | $\mathbf{7.2\times}$ |

#### 2. Matched Difference & Data-Snooping Tests (Table 3)
Resampled matched seed-market-block differences (1,200 circular-block bootstrap draws):
- **MM-ARC vs. LLMoE-style:**
  - $\Delta\text{SR} = +0.80$, 95% CI $[+0.26, +1.46]$
  - $\Delta\text{MDD} = +4.6\text{ pp}$, 95% CI $[+2.03, +6.94]$
  - $\Delta Q_{5,20d}^{\text{port}} = +2.15\text{ pp}$, 95% CI $[+0.78, +3.56]$
  - Family-level tests: Hansen's SPA $p = 0.039$; White's Reality Check $p = 0.021$.
- **MM-ARC vs. Global Learned Static Weights:**
  - $\Delta\text{SR} = +0.21$, 95% CI $[+0.10, +0.39]$
  - $\Delta\text{MDD} = +1.6\text{ pp}$, 95% CI $[+0.25, +2.70]$
  - $\Delta Q_{5,20d}^{\text{port}} = +1.38\text{ pp}$, 95% CI $[+0.30, +2.57]$
- **MM-ARC vs. Market-Specific Learned Static Weights:**
  - $\Delta\text{SR} = +0.12$, 95% CI $[+0.06, +0.21]$
  - $\Delta\text{MDD} = +0.8\text{ pp}$, 95% CI $[+0.05, +1.32]$
  - $\Delta Q_{5,20d}^{\text{port}} = +0.63\text{ pp}$, 95% CI $[+0.15, +1.14]$
- **Full RABO vs. BO-best (Peak-Selector):**
  - $\Delta\text{SR} = +0.31$, 95% CI $[+0.13, +0.55]$
  - $\Delta\text{MDD} = +3.6\text{ pp}$, 95% CI $[+1.36, +5.68]$
  - $\Delta Q_{5,20d}^{\text{port}} = +3.63\text{ pp}$, 95% CI $[+1.64, +5.65]$

#### 3. Per-Market Breakdown (Table 19, TR% / SR / MDD%)
- **China A-Shares:** B&H $19.8\% / 0.72 / -22.0\%$; LLMoE $13.3\% / 0.69 / -16.9\%$; Learned Static $15.2\% / 1.32 / -13.3\%$; MM-ARC $\mathbf{15.8\% / 1.46 / -12.5\%}$.
- **U.S. Equities:** B&H $\mathbf{32.3\%} / 0.92 / -29.1\%$; LLMoE $19.7\% / 0.68 / -22.5\%$; Learned Static $23.5\% / 1.42 / -17.4\%$; MM-ARC $24.2\% / \mathbf{1.55} / \mathbf{-16.5\%}$.
- **ETFs:** B&H $16.1\% / 0.75 / -16.7\%$; LLMoE $10.4\% / 0.56 / -15.6\%$; Learned Static $14.2\% / 1.30 / -10.8\%$; MM-ARC $\mathbf{14.9\% / 1.45 / -9.8\%}$.
- **Futures:** B&H $4.6\% / 0.35 / -18.2\%$; LLMoE $5.7\% / 0.44 / -13.7\%$; Learned Static $8.8\% / 1.12 / -10.7\%$; MM-ARC $\mathbf{9.1\% / 1.30 / -9.6\%}$.
- **Cryptocurrency:** B&H $-2.9\% / 0.18 / -37.6\%$; LLMoE $2.9\% / 0.28 / -22.8\%$; Learned Static $\mathbf{7.3\%} / 0.89 / \mathbf{-20.3\%}$; MM-ARC $6.5\% / \mathbf{0.94} / -20.6\%$.

#### 4. Market-Specific Friction Replacement Sensitivity (Table 15)
Under realistic 18/8/6/5/25 bps friction:
- MM-ARC: TR $13.9\%$, SR $1.31$, MDD $-13.8\%$.
- LLMoE-style: TR $9.9\%$, SR $0.50$, MDD $-18.0\%$.

#### 5. Search Workload & Computational Efficiency (Table 6)
- Asset-specific RABO ($744$ pools): $4,464$ generated schemas, $43,192$ backtests, $31.6\text{ h}$ E2E wall-clock time, $126.4\text{ CPU h}$, $18.2\text{ GPU h}$, $28.4\text{ GB}$ peak RAM.
- Shared + Residual design ($60$ pools): $360$ generated schemas, $3,594$ backtests, $\mathbf{4.6\text{ h}}$ E2E wall-clock time (including $0.42\text{ h}$ residual fitting), $\mathbf{18.7\text{ CPU h}}$, $\mathbf{3.2\text{ GPU h}}$, $\mathbf{21.8\text{ GB}}$ peak RAM.
- Net computational savings: $91.9\%$ fewer pools, $91.7\%$ fewer backtests, $85.4\%$ reduction in wall-clock runtime.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Cryptocurrency Volatility Lags:** In cryptocurrency, MM-ARC achieved its lowest risk-adjusted performance across all asset classes (SR $0.94$, MDD $-20.6\%$). Specifically, in training seed 46, the crypto sub-portfolio suffered a severe $-20.5\%$ drawdown between January 18 and February 5, 2026, when a violent regime shift outpaced the frozen 20-day pool refresh cadence.
2. **U.S. Equity Bull Drift Underperformance:** In strong unidirectional equity bull regimes (U.S. Equities 2025–2026), Buy-and-Hold achieved substantially higher raw total return ($32.3\%$) than MM-ARC ($24.2\%$), because MM-ARC's exposure control and diversification continuously reserved cash / hedged short downside.
3. **Modality Ablation Vulnerability:** Removing the visual chart modality drops equal-market SR from $1.33$ to $1.14$ (MDD deepens to $-15.3\%$); deliberately corrupting the visual inputs collapses SR to $0.85$ (MDD $-17.2\%$), demonstrating substantial sensitivity to visual representation corruption.
4. **Friction Sensitivity:** Increasing one-way turnover friction to 50 bps degrades MM-ARC TR from $14.1\%$ to $10.8\%$ and SR from $1.33$ to $1.00$.
5. **Ablation of Exposure Expert:** Removing the dedicated exposure control expert degrades portfolio MDD from $-13.7\%$ to $-18.2\%$, showing that the router's downside protection relies heavily on defensive cash allocation.

## Falsification plan

The core MM-ARC hypotheses can be falsified by the following operational tests:
1. **Dynamic Routing vs. Static Weights Contrast:** Compare MM-ARC against market-specific static weights over an out-of-sample forward horizon of at least 252 sessions. If paired circular block bootstrap $\Delta\text{SR} \le 0$ ($p > 0.05$) or $\Delta\text{MDD} \le 0$, the hypothesis that dynamic multimodal gating provides incremental economic value over a tuned static mixture is rejected.
2. **Vision-Language Redundancy Test:** Evaluate an ablated text-plus-numerical version against the full multimodal architecture. If the difference in out-of-sample Sharpe ratio is statistically indistinguishable from zero ($\Delta\text{SR} \le 0.05$ with $p > 0.10$), the claim that chart visual representations contain unique orthogonal market information is falsified.
3. **RABO vs. Peak-BO Overfitting Test:** In a rolling walk-forward test, compare candidates admitted via RABO against candidates admitted via pure validation Sharpe / return peaks ($J_{\text{eval}}^{\text{peak}}$). If out-of-sample $Q_{5,20d}^{\text{port}}$ and realized drawdowns show no statistically significant advantage for RABO after transaction costs, the core premise that multi-objective distribution auditing mitigates backtest overfitting is falsified.
4. **Crypto Rapid-Shift Stress Test:** Run MM-ARC on higher-frequency crypto market data with a fixed daily rebalance clock during abrupt deleveraging cascades (e.g., liquidation spirals). If the strategy experiences a drawdown exceeding the unhedged benchmark by $>5\%$, the hypothesis that daily multimodal routing can adequately protect crypto portfolios without intraday execution is falsified.

## Crypto portability

- **Empirical Status in Source:** **Directly tested** on BTC and ETH daily continuous data (2021–2026). However, for broader altcoins, decentralized assets, and higher-frequency crypto derivatives, portability is labeled **adapted / unproven**.
- **Portability Considerations & Frictions:**
  - **24/7 Continuous Trading:** Crypto markets do not have market open/close boundaries. While MM-ARC operated on a continuous daily UTC midnight rebalance clock for BTC and ETH, daily rebalancing is vulnerable to intraday liquidation wicks.
  - **Funding Rate Drag:** In perpetual futures, long/short carry costs fluctuate violently. While the source included funding rate proxies in the 25-bps crypto friction schedule, highly crowded momentum trades can incur substantial funding drag.
  - **Liquidity & Spread Fragmentation:** BTC and ETH represent top-tier liquidity. Porting MM-ARC to smaller-cap altcoins would violate the linear 25-bps friction assumption due to thin order-book depth and high slippage.
  - **Downside Cascade Risk:** As documented by the source in seed 46 ($-20.5\%$ crypto loss in 18 days), structural crypto deleveraging occurs much faster than traditional equity drawdowns, necessitating intraday risk overlays rather than daily frozen pools.

## Limitations

1. **Frozen Temporal Horizon:** The primary test was conducted over a single 12-month frozen trading holdout (July 2025 to June 2026). While statistically rigorous with circular block bootstrapping and data-snooping corrections (SPA and Reality Check), it represents a single macroeconomic cycle.
2. **Moderate Universe Breadth:** The benchmark evaluates 62 liquid instruments. Scaling to hundreds or thousands of equities/tokens would require hierarchical industry/sector pooling rather than a single market-level pool.
3. **Synthetic / Causal Text Limitation:** The text modality in MM-ARC is generated deterministically from OHLCV and indicators rather than incorporating external macroeconomic news, SEC filings, social sentiment, or order-flow feeds.
4. **Execution Simplicity:** The execution model uses next-day market-open orders and a proportional turnover cost ledger. It does not model limit order queue dynamics, partial fills, latency, or nonlinear square-root price impact.
5. **Computation Overhead:** Tuning and adapting the Qwen3-VL-8B-Instruct foundation model requires dedicated GPU infrastructure, though structural sharing reduces search time from $31.6$ to $4.6$ hours.

## Implementation status

`not-implemented`. This strategy research capture has not been implemented or validated within NautilusTrader, PyBroker, or any live trading pipeline.

## Adoption boundary

`research-only`.
- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

This record is a normalized research capture for evaluation and synthesis. It is not approved for live trading, testnet execution, paper trading, or production capital allocation.

## Related Wiki records

- `[[tradingmoe-query-key-sparse-expert-routing-llm-trading-2026-09-03]]` — LLM query-key sparse expert routing across regime-specialized models.
- `[[retrieval-augmented-llm-expert-switching-portfolio-management-2026-09-03]]` — Retrieval-augmented LLM expert switching for portfolio management.
- `[[maple-multi-alpha-position-aware-listwise-ensembling-2026-09-04]]` — Multi-alpha position-aware listwise ensembling for cross-sectional portfolio construction.
- `[[regime-adaptive-continual-learning-portfolio-management-recap-2026-09-02]]` — Continual learning and regime-adaptive portfolio management under non-stationary market drift.
- `[[strata-selective-state-space-intraday-raw-bars-cross-sectional-ranking-2026-09-02]]` — Cross-sectional ranking from raw intraday bars using selective state-space architectures.
- `[[statistical-arbitrage-rank-space-cnn-transformer-hybrid-atlas-2026-09-02]]` — Deep hybrid models for statistical arbitrage and rank-space portfolio optimization.

## Sources

1. **Primary Academic Source:** Yang Chen, Yuchen Cao, Jacky Keung, Leilei Gan, Kun Kuang, Yueheng Jiang, Zhaozhao Ma, Jianping Zhu, Fei Wu, and Jinpeng Li. *"MM-ARC: Multimodal Adaptive Routing of Capital with Robustness-Audited Strategy Pools"*, arXiv preprint `arXiv:2509.05080v3 [q-fin.TR]`, submitted September 2025, revised July 2026.
   - Stable arXiv URL: [https://arxiv.org/abs/2509.05080](https://arxiv.org/abs/2509.05080)
   - Full text HTML: [https://arxiv.org/html/2509.05080v3](https://arxiv.org/html/2509.05080v3)
   - Full text PDF: [https://arxiv.org/pdf/2509.05080](https://arxiv.org/pdf/2509.05080)
   - DOI: [10.48550/arXiv.2509.05080](https://doi.org/10.48550/arXiv.2509.05080)
2. **Reproduction Codebase:** Anonymous open-science repository containing executable pipelines, schema grammars, and experiment records: [https://anonymous.4open.science/r/MM-ARC-32F7](https://anonymous.4open.science/r/MM-ARC-32F7).
