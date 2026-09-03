---
schema: strategy-research-record-v1
title: "Global Equity Soft Actor-Critic Dynamic Asset Allocation with Hierarchical Dirichlet Policy and Adaptive Retraining"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - reinforcement-learning
  - soft-actor-critic
  - portfolio-optimization
  - global-equities
  - walk-forward
status: research-only
confidence: medium
source_as_of: 2026-03-13
sources:
  - https://arxiv.org/abs/2605.17307
  - https://arxiv.org/html/2605.17307v1
  - https://doi.org/10.48550/arXiv.2605.17307
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Global Equity Soft Actor-Critic Dynamic Asset Allocation with Hierarchical Dirichlet Policy and Adaptive Retraining

## Provenance

Primary source: Kamil Kashif and Robert Ślepaczuk (Faculty of Economic Sciences, University of Warsaw), **"Deep Reinforcement Learning Framework for Diversified Portfolio Management Across Global Equity Markets"**, arXiv preprint `arXiv:2605.17307v1` [q-fin.PM] (cross-listed: `cs.AI`, `cs.LG`, `cs.NE`, `q-fin.TR`), submitted May 2026. DOI: `10.48550/arXiv.2605.17307`. Stable URLs: `https://arxiv.org/abs/2605.17307` and `https://arxiv.org/html/2605.17307v1`.

The dataset covers daily observations from 2003-01-02 to 2026-03-13 across three major equity indices: the NASDAQ-100 (U.S., benchmark ETF: QQQ), Nikkei 225 (Japan, benchmark ETF: EWJ), and EURO STOXX 50 (Europe, benchmark ETF: FEZ). Historical index membership dynamics (additions/deletions) were reconstructed from Bloomberg Terminal Anywhere subscription records to eliminate survivorship bias; constituent daily price data were sourced via the yfinance API. Out-of-sample trading evaluation runs from 2009-04-01 / 2009-04-06 through 2026-03-13 over 16 annual non-anchored walk-forward folds (5-year rolling training, 1-year validation, 1-year testing).

Repository-wide source identity checks on 2026-09-04 confirmed that `arXiv:2605.17307` and the authors Kashif and Ślepaczuk do not appear in any existing record or coverage manifest. Existing DRL portfolio records (`alphazerobeta-recurrent-ppo-market-neutral-portfolio-2026-09-02.md`, `sciphy-physics-informed-reinforcement-learning-portfolio-optimization-2026-09-02.md`, `regime-adaptive-continual-learning-portfolio-management-recap-2026-09-02.md`) address PPO market-neutral equity selection, physics-informed regularized RL, or continual clustering adaptation. This record specifically captures a multi-market Soft Actor-Critic (SAC) architecture with continuous action spaces parameterized by a Hierarchical Dirichlet policy (equity-cash stage followed by intra-equity asset distribution), turnover/concentration regularized rewards, and an adaptive rolling-validation Sharpe retraining trigger.

## Economic mechanism

### Source-reported

The authors model portfolio allocation as a sequential Markov Decision Process (MDP), arguing that traditional Mean-Variance Optimization (MVO) and supervised return-forecasting pipelines fail in live markets due to covariance estimation error, non-stationarity, and the disconnect between point-prediction accuracy and realized portfolio utility. Instead of predicting returns, an agent using maximum-entropy Soft Actor-Critic (SAC) directly learns continuous portfolio weight policies that maximize long-term risk-adjusted returns net of transaction costs, turnover penalties, and concentration penalties.

The authors hypothesize that active RL allocation provides the greatest economic value in equity markets characterized by lower trend persistence and higher structural uncertainty (such as post-crisis European equities), whereas passive Buy & Hold systematically dominates in strong, persistent secular bull markets (such as the tech-driven NASDAQ-100). Furthermore, they argue that decomposing allocation into a hierarchical policy—first deciding total risky equity exposure versus risk-free cash, and subsequently distributing risky capital across pre-selected momentum assets via a Dirichlet distribution—stabilizes action dynamics and provides effective drawdown protection.

### Research interpretation

The falsifiable mechanism is **dynamic risk-regime exposure switching regularized by continuous turnover and concentration penalties**. Under this thesis, the primary source of excess risk-adjusted return (or drawdown containment) is not precise multi-asset alpha prediction, but dynamic cash preservation during market stress and diversification during recovery. 

If this mechanism is genuine:
1. The cash-allowed hierarchical configuration (`LSTM_2`) should exhibit lower maximum drawdown and lower annualized volatility than fully invested configurations (`LSTM_NC_1`, `LSTM_NC_2`).
2. The active policy should demonstrate economic outperformance relative to passive Buy & Hold primarily in range-bound or high-uncertainty regimes (EURO STOXX 50, post-GFC Nikkei), but underperform naive Buy & Hold during persistent monotonic bull trends (NASDAQ-100 2014–2019) where cash holding and turnover drag extract a net cost.
3. If outperformance vanishes when compared against an equal-weight monthly rebalancing of the same top-$k$ momentum universe, the true return driver is the exogenous momentum pre-filter rather than the neural reinforcement policy.

## Signal

### Source-reported construction

The strategy operates daily at index market close, executing at the subsequent trading session.

1. **Exogenous Cross-Sectional Universe Pre-Filtering:**
   - At each time step $t$, filter the tradable index constituents (assets present in the index and having valid trading prices via the Bloomberg membership mask) by 120-day price momentum:
     $$\text{Momentum}_{i,t} = \frac{P_{i,t}}{P_{i,t-120}} - 1$$
   - Retain only the top-$k$ assets ($k \in \{20, 30\}$ depending on configuration; $k=20$ in the primary baseline, $k=10/20$ in NC variants). This keeps the neural state input dimensionality constant across all folds.

2. **State Feature Vector (60-Day Lookback Window):**
   - **Momentum features:** Daily logarithmic returns over horizons $X \in \{1, 5, 20, 60\}$ trading days:
     $$r_{i,t,X} = \ln(P_{i,t} / P_{i,t-X})$$
   - **Volatility features:** Rolling standard deviation of daily log returns over $X \in \{5, 20\}$ trading days:
     $$\sigma_{i,t,X} = \sqrt{\frac{1}{X-1}\sum_{s=0}^{X-1} (r_{i,t-s,1} - \bar{r}_{i,t,X})^2}$$
   - **Technical indicators:** 14-day RSI, MACD histogram (12/26/9), Bollinger Bands %B (20-day, 2$\sigma$), distance from rolling 20-day high ($P_{i,t} / \max_{0\le s < 20} P_{i,t-s} - 1$), and mean-reversion deviation from 20-day simple moving average ($P_{i,t} / \text{SMA}_{i,t,20} - 1$).
   - **Market-relative features:** Rolling 60-day equity beta relative to market proxy ETF (QQQ, EWJ, or FEZ), and 20-day log return.
   - **Global macro/market features:** Level of VIX and 5-day VIX change; cross-sectional average return of tradable assets and its 5-day rolling volatility; market breadth (percentage of assets with positive 20-day return); and 5-day and 20-day normalized return of market proxy ETF.

3. **Neural Representation Encoder:**
   - Asset features over the 60-day historical window are encoded per asset using a 1-layer LSTM (hidden size 64 or 128) or a 2-layer Transformer (hidden size 128, multi-head self-attention).
   - Cross-sectional attention aggregates individual asset representations into a unified market state embedding.

4. **Action Space & Policy Architecture:**
   - Action vector $\mathbf{w}_t = [w_{1,t}, \dots, w_{N_t,t}, w_t^c]^T$ representing asset allocations and cash weight $w_t^c$, subject to $w_{i,t} \ge 0, w_t^c \ge 0$ and $\sum_{i=1}^{N_t} w_{i,t} + w_t^c = 1$.
   - **Flat Dirichlet (`LSTM_1`, `TRANSFORMERS`):** A single policy network head outputs concentration parameters $\boldsymbol{\alpha}_t$ of a Dirichlet distribution spanning all $N_t$ assets plus cash.
   - **Hierarchical Dirichlet (`LSTM_2`):** The policy decomposes into two sequential stages:
     1. High-level allocation head outputs a Beta/Dirichlet distribution dividing capital between aggregate risky equity exposure $w_t^{equity}$ and risk-free cash $w_t^c = 1 - w_t^{equity}$.
     2. Low-level asset allocation head outputs Dirichlet parameters distributing $w_t^{equity}$ across the individual $N_t$ assets: $w_{i,t} = w_t^{equity} \cdot \tilde{w}_{i,t}$ where $\sum \tilde{w}_{i,t} = 1$.

5. **Optimization Objective & Reward Function:**
   - Continuous Soft Actor-Critic (SAC) framework optimizing expected reward plus policy entropy with fixed entropy temperature $\alpha = 0.2$ (fixed to prevent training collapse in non-stationary financial data), discount factor $\gamma = 0.99$, and soft target update $\tau = 0.005$.
   - Twin Q-critics mitigate value overestimation bias.
   - **Log Net Return Reward:**
     $$R_t = r_{p,t}^{net} - \lambda_{TO} \cdot TO_t - \lambda_{conc} \cdot (HHI_t - HHI_t^{min})$$
     where:
     - $r_{p,t}^{net} = \ln(V_t / V_{t-1})$ net of transaction costs (2 bps per unit of turnover).
     - Turnover penalty: $TO_t = \sum_{i=1}^{N_t} |w_{i,t} - w_{i,t}^{-}| + |w_t^c - w_t^{c,-}|$, with coefficient $\lambda_{TO} = 0.003$.
     - Concentration penalty: $HHI_t = \sum_{i=1}^{N_t} w_{i,t}^2$ and $HHI_t^{min} = 1/N_t$, with coefficient $\lambda_{conc} \in \{0.0, 0.1, 0.5\}$.
   - **Benchmark-Relative Reward (`LSTM_NC_1`, `LSTM_NC_2`):**
     $$R_t = (r_{p,t}^{net} - \tilde{r}_{b,t}) - \lambda_{TO} \cdot TO_t - \lambda_{conc} \cdot (HHI_t - HHI_t^{min})$$

6. **Non-Anchored Walk-Forward Optimization & Adaptive Retraining:**
   - 16 walk-forward annual cycles (2009–2026). Each cycle uses 5 years rolling training, 1 year validation, and 1 year out-of-sample testing.
   - **Adaptive Retraining Criterion:** Rather than retraining every year, model retraining is conditioned on validation performance. Let $S_k$ be the annualized validation Sharpe ratio at fold $k$. Retraining threshold:
     $$\theta_k = \frac{1}{m}\sum_{j=1}^m S_{k-j} - 0.5 \cdot \text{std}(S_{k-m \dots k-1})$$
     (with lookback $m \le 5$, active when $k \ge 3$).
   - The model is retrained if: (1) $S_k < 0$, (2) $S_k < \theta_k$, or (3) consecutive folds without retraining exceeds 3. Otherwise, the existing weights are deployed into the test year without re-estimation.

### Underspecified items

- The exact intra-day execution timing relative to daily bar close (e.g., market-on-close MOC vs next-day open MOO) is described as daily rebalancing, but exact order timestamp routing is not explicitly parameterized in the text.
- Slippage beyond fixed 2 bps proportional transaction fees is not modeled.
- The exact distribution of cash yield (whether cash earns risk-free rate or 0%) is not explicitly stated.

## Required data

- **Universe:** 
  - U.S.: NASDAQ-100 constituents; benchmark Invesco QQQ Trust ETF (`QQQ`).
  - Japan: Nikkei 225 constituents; benchmark iShares MSCI Japan ETF (`EWJ`).
  - Europe: EURO STOXX 50 constituents; benchmark SPDR Euro Stoxx 50 ETF (`FEZ`).
- **Data sources:**
  - Constituent daily prices: yfinance API (adjusted close, open, high, low, volume).
  - Index membership dynamics: Bloomberg Terminal Anywhere (point-in-time constituent additions and deletions from 2003 to 2026).
  - Global volatility: Cboe Volatility Index (`VIX`).
- **Frequency:** Daily.
- **Sample period:** 2003-01-02 to 2026-03-13 (in-sample training from 2003; out-of-sample evaluation from 2009-04-01 / 2009-04-06 to 2026-03-13).
- **Point-in-time constraints:** Strict point-in-time survivorship handling via daily tradability mask. Forward-fill used for constituency matrix between recorded addition/deletion events; forward-fill for missing price observations. Assets without active membership or valid prices are masked out of the investable universe.

## Execution assumptions

### Source-reported

- Rebalancing frequency: Daily.
- Transaction costs: Proportional cost of 2 basis points (0.02%) per unit of turnover ($L^1$ weight change), modeled to represent the lower bound of institutional tiered pricing (e.g., Interactive Brokers tiered equity commissions of 0.05 to 0.35 bps/share).
- Portfolio constraints: Long-only, no shorting ($w_{i,t} \ge 0$).
- Cash allowance: Cash holding allowed in `LSTM_1`, `LSTM_2`, and `TRANSFORMERS`; zero cash / fully invested enforced in `LSTM_NC_1` and `LSTM_NC_2`.
- Sizing / Leverage: Strictly unleveraged ($\sum w_{i,t} + w_t^c = 1$).

### Research interpretation

A 2 bps transaction cost assumption is realistic for high-volume institutional execution on mega-cap liquid equities (e.g., top NASDAQ-100 or EURO STOXX 50 names), but may underestimate market impact and bid-ask spread crossing costs for the less liquid tail of Nikkei 225 constituents. In particular, daily rebalancing with turnover levels of 10% to 23% per day accumulates substantial cumulative drag over 16 years. A higher transaction cost stress test (e.g., 5 to 10 bps) is essential before considering any implementation.

## Evidence

### Source-reported

All figures below are directly cited from the out-of-sample evaluation period (2009-04-01 / 2009-04-06 to 2026-03-13, 16 annual folds) across Tables 7, 8, 9, 10, 11, 15, and 16 of `arXiv:2605.17307v1`:

1. **NASDAQ-100 Performance (Table 7):**
   - Passive Buy & Hold (`QQQ`) achieves ARC 19.27%, ASD 20.41%, Max Drawdown 35.12%, IR1 0.9441, IR2 0.5180, Sharpe 0.9689, ADT 0.000.
   - Equal-Weight Monthly: ARC 18.13%, ASD 20.47%, MD 32.55%, IR1 0.8857, IR2 0.4933, Sharpe 0.9187, ADT 0.326.
   - Markowitz Min Variance: ARC 16.65%, ASD 19.18%, MD 31.00%, IR1 0.8681, IR2 0.4662, Sharpe 0.8978, ADT 0.214.
   - `LSTM_1` (Flat Dirichlet, Cash): ARC 17.61%, ASD 21.63%, MD 32.34%, IR1 0.8141, IR2 0.4433, Sharpe 0.8622, ADT 13.782.
   - `LSTM_2` (Hierarchical Dirichlet, Cash): ARC 15.64%, ASD 18.67%, MD 28.77%, IR1 0.8377, IR2 0.4554, Sharpe 0.8759, ADT 13.951.
   - `LSTM_NC_1` (Fully Invested, Rel. Reward): ARC 19.70%, ASD 24.20%, MD 41.23%, IR1 0.8140, IR2 0.3890, Sharpe 0.8678, ADT 16.326.
   - `TRANSFORMERS` (Flat, Cash): ARC 17.46%, ASD 21.43%, MD 32.27%, IR1 0.8147, IR2 0.4408, Sharpe 0.8619, ADT 14.248.
   - *Result:* Passive Buy & Hold and naive Equal-Weight Monthly beat all RL strategies on risk-adjusted IR2 and Sharpe on the NASDAQ-100.

2. **Nikkei 225 Performance (Table 8):**
   - Buy & Hold (`EWJ`): ARC 4.57%, ASD 20.41%, MD 55.80%, MLD 11.345 yr, IR1 0.2239, IR2 0.0183, Sharpe 0.3189, ADT 0.000.
   - Equal-Weight Monthly: ARC 12.40%, ASD 20.86%, MD 39.33%, MLD 3.060 yr, IR1 0.5944, IR2 0.1874, Sharpe 0.6630, ADT 0.261.
   - Markowitz Min Variance: ARC 13.17%, ASD 21.76%, MD 46.23%, MLD 1.048 yr, IR1 0.6052, IR2 0.1724, Sharpe 0.6772, ADT 0.239.
   - `LSTM_1` (Flat, Cash): ARC 11.22%, ASD 20.96%, MD 39.09%, MLD 0.690 yr, IR1 0.5353, IR2 0.1536, IR3 2.4979, Sharpe 0.6105, ADT 23.497.
   - `LSTM_2` (Hierarchical, Cash): ARC 9.12%, ASD 18.37%, MD 38.27%, MLD 0.571 yr, IR1 0.4965, IR2 0.1183, IR3 1.8876, Sharpe 0.5652, ADT 18.858.
   - *Result:* RL models beat passive Buy & Hold by a wide margin, but trail classical naive Equal-Weight and Markowitz Min Variance.

3. **EURO STOXX 50 Performance (Table 9):**
   - Buy & Hold (`FEZ`): ARC 7.81%, ASD 23.92%, MD 39.69%, MLD 1.643 yr, IR1 0.3265, IR2 0.0642, Sharpe 0.4333, ADT 0.000.
   - Equal-Weight Monthly: ARC 10.24%, ASD 20.63%, MD 39.40%, MLD 1.139 yr, IR1 0.4964, IR2 0.1290, Sharpe 0.5738, ADT 0.859.
   - Markowitz Min Variance: ARC 9.11%, ASD 18.31%, MD 36.24%, MLD 0.413 yr, IR1 0.4975, IR2 0.1251, Sharpe 0.5653, ADT 0.172.
   - `LSTM_1` (Flat, Cash): ARC 8.55%, ASD 18.71%, MD 33.52%, MLD 1.048 yr, IR1 0.4570, IR2 0.1166, Sharpe 0.5301, ADT 10.613.
   - `LSTM_2` (Hierarchical, Cash): ARC 8.36%, ASD 15.97%, MD 29.94%, MLD 1.060 yr, IR1 0.5235, IR2 0.1462, IR3 1.1525, Sharpe 0.5807, ADT 11.416.
   - `TRANSFORMERS` (Flat, Cash): ARC 8.71%, ASD 18.78%, MD 33.16%, MLD 1.048 yr, IR1 0.4638, IR2 0.1218, Sharpe 0.5367, ADT 8.418.
   - *Result:* All RL models outperform Buy & Hold on IR2. `LSTM_2` delivers the highest risk-adjusted IR2 (0.1462) across all strategies, including Equal-Weight and Markowitz.

4. **Cross-Asset Equal-Weight Ensemble Fund (Table 15):**
   - Common Benchmark (mean of QQQ, EWJ, FEZ): ARC 12.68%, ASD 16.53%, MD 28.63%, IR1 0.7671, IR2 0.3397, Sharpe 0.8055.
   - `LSTM_1` Ensemble: ARC 13.03%, ASD 14.72%, MD 28.16%, IR1 0.8852, IR2 0.4096, Sharpe 0.9062.
   - `LSTM_2` Ensemble: ARC 11.33%, ASD 12.75%, MD 25.46%, IR1 0.8886, IR2 0.3954, Sharpe 0.9054.
   - `TRANSFORMERS` Ensemble: ARC 12.21%, ASD 14.77%, MD 27.92%, IR1 0.8267, IR2 0.3615, Sharpe 0.8541.

5. **Statistical Significance Tests (Tables 10, 11, 16):**
   - **Newey-West HAC Mean Return Difference Tests (Table 10):** Across all three markets, zero RL strategies achieve statistically significant mean return differences relative to Buy & Hold (NASDAQ $p \in [0.31, 0.95]$; Nikkei $p \in [0.34, 0.69]$; Euro Stoxx $p \in [0.47, 0.63]$). Stationary bootstrap tests for $\Delta \text{Sharpe}$ and $\Delta \text{IR2}$ also fail to reject at the 10% level.
   - **Regression Abnormal Return $\alpha$ (Table 11):** In EURO STOXX 50, several models exhibit positive abnormal returns significant at 10%: `LSTM_1` ($\alpha = 0.0002, t=1.83, p=0.0333$), `LSTM_2` ($\alpha = 0.0002, t=2.26, p=0.0120$), and `TRANSFORMERS` ($\alpha = 0.0002, t=1.89, p=0.0291$). No significant $\alpha$ is found for NASDAQ-100 or Nikkei 225.
   - **Ensemble Regression $\alpha$ (Table 16 Panel B):** `LSTM_1` ($\alpha = 0.0001, t=1.65, p=0.0496$) and `LSTM_2` ($\alpha = 0.0001, t=1.66, p=0.0481$) show positive abnormal returns significant at 5%.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Failure of Raw Return Outperformance:** Formal Newey-West HAC inference and stationary block bootstrap tests show no statistically significant excess return over Buy & Hold across any of the three individual markets or in the cross-asset ensemble.
2. **Dominance of Naive and Classical Benchmarks:** Naive monthly 1/N equal-weighting and classical Markowitz minimum variance outperform all RL configurations on the Nikkei 225 and NASDAQ-100, demonstrating that complex deep RL policies struggle to extract alpha beyond simple diversification heuristics and momentum filtering.
3. **Severe Bull-Market Penalty:** In secular bull regimes (NASDAQ-100 2014–2019), active RL models underperform Buy & Hold by substantial margins due to turnover frictions and defensive cash dragging.
4. **Transformer Sub-optimality:** Replacing the 1-layer LSTM with a 2-layer self-attention Transformer increased per-fold training time from 14 hours to 23 hours (+64% compute cost) without delivering consistent risk-adjusted improvements over LSTM baselines.
5. **Turnover Sensitivity:** RL strategies exhibit average daily turnover of 8% to 23% (vs <0.9% for monthly rebalanced benchmarks). While viable at 2 bps, the performance advantage in EURO STOXX 50 would compress severely if execution costs rose above 5 bps.

## Falsification plan

To falsify the proposed SAC hierarchical asset allocation mechanism:

1. **Exogenous Momentum Ablation:** Replace the top-$k$ momentum pre-filter with a random asset selection or liquidity-only filter. If the SAC agent's Sharpe and IR2 collapse to or below the index benchmark, the observed performance is entirely attributable to the momentum premium rather than reinforcement learning policy optimization.
2. **Transaction Cost Sensitivity Stress Test:** Step transaction costs from 2 bps to 5, 8, 10, and 15 bps. If the risk-adjusted outperformance in EURO STOXX 50 and the ensemble flips to negative at $\le 6$ bps, the strategy represents an unexecutable turnover artifact.
3. **Walk-Forward Grid Meta-Overfitting Audit:** Perturb the walk-forward parameters (e.g., test 3-year and 7-year training windows, 6-month validation windows, and varying retraining thresholds $\theta_k$). Under [Bailey et al. (2017)](https://dx.doi.org/10.21314/JCF.2016.322) criteria, if the Sharpe ratio degrades by $>30\%$ under minor horizon perturbations, the reported stability is meta-overfitted.
4. **Placebo / Shuffled State Test:** Train the SAC agent on temporally shuffled feature sequences or randomized cross-sectional asset labels. If the agent achieves similar cumulative return or drawdown containment, the model is exploiting spurious state correlations rather than true temporal/structural signals.
5. **Sub-period Failure Criterion:** If out-of-sample IR2 drops below the naive Equal-Weight Monthly benchmark across two consecutive 3-year market cycles, reject the active policy in favor of classical rule-based allocation.

## Crypto portability

**Portability classification:** `adapted` / `unproven`.

The primary source explicitly evaluates liquid traditional equity indices (NASDAQ-100, Nikkei 225, EURO STOXX 50) and notes that crypto application is an unproven future direction. Porting this framework to cryptocurrency spot or perpetual markets introduces critical structural differences:

1. **Trading Session & Horizon Discrepancy:** Traditional equities operate on discrete daily sessions with well-defined market close auctions. Crypto markets trade 24/7/365 without daily auction fixes, requiring explicit synthetic candle cutoffs (e.g., 00:00 UTC) that may expose the model to timezone-specific liquidity shocks.
2. **Fee and Friction Disparity:** The paper assumes 2 bps institutional transaction costs. On cryptocurrency spot and perpetual venues (e.g., Binance, Hyperliquid, Bybit), retail/standard taker fees range from 2 to 5 bps, and altcoin bid-ask spreads frequently exceed 10 to 30 bps. Daily turnover of 10% to 20% would incur prohibitive friction unless constrained by much higher turnover penalties ($\lambda_{TO} \gg 0.003$).
3. **Perpetual Funding Costs & Basis Drift:** In crypto perpetuals, holding long positions across top momentum assets incurs funding rate debits (often 10% to 30% APR during bull regimes). The reward function must explicitly integrate funding payments into $r_{p,t}^{net}$.
4. **Survivorship & Delisting Dynamics:** Crypto altcoin universes exhibit extreme mortality rates and sudden liquidity evaporation compared to blue-chip equity indices. Constructing a point-in-time tradability mask in crypto requires rigorous delisting and liquidity filtering to avoid fatal look-ahead bias.

## Limitations

- **Lack of True Ceteris Paribus Ablation:** The paper's five evaluated configurations simultaneously vary encoder type (LSTM vs Transformer), policy structure (flat vs hierarchical), reward formulation (absolute vs benchmark-relative), and constraints (cash vs no-cash). Differences between models cannot be definitively attributed to a single component.
- **Statistical Insignificance on Raw Returns:** As documented by the authors using Newey-West HAC estimators and stationary block bootstraps, none of the RL models demonstrate statistically significant excess returns over Buy & Hold across the full 16-year sample.
- **Compute and Retraining Overhead:** Training requires 14 hours (LSTM) to 23 hours (Transformer) per walk-forward fold on an NVIDIA L4 GPU, making frequent real-time model re-estimation computationally demanding.
- **Fixed Hyperparameter Assumptions:** The entropy temperature $\alpha = 0.2$ and transaction fee assumption (2 bps) were held fixed without dynamic optimization or stress testing.
- **Underspecified Intra-day Execution:** The paper does not specify the exact order execution mechanism (MOC vs next-day open) or queueing/slippage dynamics.

## Implementation status

`not-implemented`.

This record represents external academic research capture only. No implementation has been created in PyBroker, NautilusTrader, or any internal research repository. No paper, testnet, or live trading has been authorized or conducted.

## Adoption boundary

`not-approved` / `research-only`.

This capture serves exclusively as a normalized research record in the public staging pool. Presence in this repository does not indicate strategy approval, backtest validation, or trading suitability. Implementation or adoption into any execution pipeline requires independent replication, leakage-safe backtesting, and separate review.

## Related Wiki records

- `alphazerobeta-recurrent-ppo-market-neutral-portfolio-2026-09-02.md`
- `sciphy-physics-informed-reinforcement-learning-portfolio-optimization-2026-09-02.md`
- `deep-portfolio-optimization-attention-lstm-omega-cvar-risk-parity-2026-09-03.md`
- `regime-adaptive-continual-learning-portfolio-management-recap-2026-09-02.md`
- `decision-focused-sparse-tangent-portfolio-dpp-topk-2026-09-03.md`
- `observable-matrix-dynamics-portfolio-optimization-2026-09-02.md`

## Sources

- Kamil Kashif and Robert Ślepaczuk, "Deep Reinforcement Learning Framework for Diversified Portfolio Management Across Global Equity Markets", arXiv preprint `arXiv:2605.17307v1` [q-fin.PM] (cross-listed: `cs.AI`, `cs.LG`, `cs.NE`, `q-fin.TR`), May 2026. Stable URL: `https://arxiv.org/abs/2605.17307`. Full-text HTML: `https://arxiv.org/html/2605.17307v1`. DOI: `10.48550/arXiv.2605.17307`.
- Source data and evaluation tables directly cited: Table 3 (Model Configurations), Table 4 (SAC Hyperparameters), Table 5 (Sequence Encoders), Table 6 (Environment and Training Parameters), Table 7 (NASDAQ-100 Performance Metrics), Table 8 (Nikkei 225 Performance Metrics), Table 9 (EURO STOXX 50 Performance Metrics), Table 10 (HAC and Bootstrap Tests), Table 11 (Regression Abnormal Returns), Table 12-14 (Sub-period Regime Analysis), Table 15 (Cross-Asset Ensemble Total Fund), Table 16 (Ensemble Statistical Tests).
