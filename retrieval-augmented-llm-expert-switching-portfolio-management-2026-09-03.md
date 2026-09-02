---
schema: strategy-research-record-v1
title: "Regime-Aware Portfolio Management via Retrieval-Augmented LLM-Guided Expert Switching"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - portfolio-management
  - expert-switching
  - retrieval-augmented-generation
  - mixture-of-experts
  - transformer-vae
  - regime-detection
  - reinforcement-learning
  - llm-reasoning
  - multi-asset
  - crypto
  - cross-asset
status: research-only
confidence: medium
source_as_of: 2026-08-28
sources:
  - "https://arxiv.org/abs/2608.28252"
  - "https://doi.org/10.48550/arXiv.2608.28252"
  - "https://arxiv.org/html/2608.28252v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Regime-Aware Portfolio Management via Retrieval-Augmented LLM-Guided Expert Switching

## Provenance

- **Primary Paper:** Ahmad Asadi and Reza Safabakhsh (Deep Learning Lab, Computer Engineering Department, Amirkabir University of Technology, Tehran, Iran), *"Regime-Aware Portfolio Management via Retrieval-Augmented LLM-Guided Expert Switching"*, arXiv preprint `arXiv:2608.28252v1 [cs.AI, cs.LG, q-fin.PM, q-fin.ST]`, submitted August 28, 2026. DOI: `10.48550/arXiv.2608.28252`.
- **Primary Source Snapshot:** Complete author-published LaTeX source and figure package downloaded and inspected directly from `https://arxiv.org/e-print/2608.28252` (August 2026 tarball snapshot), including `manuscript.tex`, `01_introduction.tex`, `02_literature_review.tex`, `03_proposed_method.tex`, `04_experimental_results.tex`, `05_conclusion.tex`, `arch.png`, and data specification tables.
- **Public Traceable URLs:**
  - Abstract: `https://arxiv.org/abs/2608.28252`
  - Canonical DOI: `https://doi.org/10.48550/arXiv.2608.28252`
  - HTML Full Text: `https://arxiv.org/html/2608.28252v1`
- **Source/Data As-Of:** 2026-08-28.
- **Deduplication Audit:** Repository-wide audit confirms zero existing records covering `arXiv:2608.28252`, `Ahmad Asadi`, `Reza Safabakhsh`, `expert switching`, or `retrieval-augmented`. Related records in this repository (e.g., `tradingmoe-query-key-sparse-expert-routing-llm-trading-2026-09-03.md` covering query-key routing, and `regime-adaptive-continual-learning-portfolio-management-recap-2026-09-02.md` covering CUSUM change-point policy vectors) address fundamentally distinct mechanisms and source identities. Asadi & Safabakhsh (2026) uniquely introduces retrieval-augmented expert selection using a dual-stream Transformer-VAE latent space, offline Statements of Performance (SoPs), and an instruction-tuned LLM reasoning layer bounded by a formal monotonicity theorem ($V(\pi_{N+1}) \geq V(\pi_N)$).

## Economic mechanism

### Source-reported

Financial markets exhibit pronounced non-stationarity, regime shifts, and structural breaks that undermine conventional portfolio management models:
1. **Failure of Monolithic Policies:** Mean-variance optimization relies on stationary return distributions and stable covariance structures, while monolithic Deep Reinforcement Learning (DRL) policies overfit historical training regularities and suffer severe drawdown when confronted with novel volatility regimes or abrupt market shocks.
2. **Pathologies of Conventional Mixture-of-Experts (MoE):** In standard MoE architectures, learned gating networks or short-horizon performance-based routers become unreliable during regime transitions. Recent realized performance is noisy and misallocates capital, while supervised gating networks struggle to generalize to unseen regimes.
3. **Retrieval-Augmented Historical Grounding:** Instead of asking which expert performed best over the most recent 5 days, the framework frames routing as a historical matching problem: identifying historical market states that share the same latent macroeconomic and microstructural profile, and examining how candidate policies actually performed under those conditions.
4. **Constrained LLM Reasoning vs. Direct Trading:** Rather than having an LLM generate portfolio allocations directly (which benchmark literature shows fails to reliably outperform simple buy-and-hold over multi-month horizons), the LLM is restricted to a structured decision-support role. It evaluates retrieved Statements of Performance (SoPs), calibrates uncertainty, and selects the most appropriate quantitative expert.
5. **Monotonic Expert-Pool Scaling:** Under bounded estimation error ($\epsilon$), conservative switching margins ($\tau \geq 2\epsilon$), and specialist dominance ($\delta > \tau + 2\epsilon$), the system satisfies a monotonicity theorem: adding an incremental specialist to the expert pool cannot degrade overall portfolio utility ($V(\pi_{N+1}) \geq V(\pi_N)$), enabling modular expansion without retraining from scratch.

### Research interpretation

This is an adaptive meta-allocation and regime-switching framework designed to mitigate strategy obsolescence across non-stationary market regimes.

The core falsifiable hypothesis is: **In multi-asset portfolio management, selecting trading policies dynamically via dual-stream latent nearest-neighbor retrieval and constrained LLM risk/return evaluation achieves higher risk-adjusted return (Sharpe ratio) and lower drawdown than both static expert allocation and rolling-window recent-performance gating.**

Key theoretical and structural failure modes include:
- **Representation Collapse / Metric Distortion:** If the dual-stream Transformer-VAE fails to map functionally identical market stresses (e.g., liquidity vacuums, high-volatility sell-offs) to proximate latent coordinates, the retrieved nearest neighbors will provide irrelevant or misleading performance precedents.
- **Unprecedented / Out-of-Distribution Regimes:** If a market shock has no historical precedent in the index (e.g., an unprecedented protocol collapse or sovereign default), empirical grounding defaults to baseline historical means, potentially causing delayed or ineffective defensive switching.
- **Excessive Policy Turnover:** Discrete switching among policies with disparate target allocations every 5 days can incur substantial portfolio rebalancing friction, which will degrade net alpha if bid-ask spreads or market impact are elevated.
- **LLM Reasoning Sensitivity:** If the reasoning model lacks sufficient capacity or hallucinates outside the empirical SoP bounds, expert selection degrades to worse than random or static baselines, as empirically observed with smaller models (e.g., Gemma4-E4B in Forex).

## Signal

The strategy operates a two-stage pipeline: an offline indexing procedure that constructs a historical regime-performance database, and an online inference procedure that executes every $H = 5$ trading days.

### 1. Market State Representation & Dual-Stream Encoding

At each decision step $t$, the market state is captured by two rolling feature tensors of length $L = 22$ trading days:
1. **Asset-Level Technical Tensor ($S_t^{\mathrm{tech}} \in \mathbb{R}^{L \times A \times F_1}$):**
   - Covers $A = 30$ panel assets.
   - Features $F_1$: Log-returns, RSI, MACD, ATR, realized volatility, and volume changes.
   - Standardized via rolling z-score normalization.
2. **Market-Wide Condition Tensor ($S_t^{\mathrm{mkt}} \in \mathbb{R}^{L \times F_2}$):**
   - Captures aggregate trend indicators, volatility-regime measures, and market liquidity variables.

Each stream is encoded via a pretrained temporal Transformer-VAE into a Gaussian posterior:
$$q_{\phi_x}(z_x \mid S_t^x) = \mathcal{N}\left(\mu_x(S_t^x), \Sigma_x(S_t^x)\right), \quad x \in \{\mathrm{tech}, \mathrm{mkt}\}$$
Sampling a latent vector $z_x = \mu_x + \epsilon \odot \sigma_x$ with $\epsilon \sim \mathcal{N}(0, I)$ and dimension $d = 64$.
The latent market representation concatenates the two streams:
$$h_t = [z_t^{\mathrm{tech}} \mid z_t^{\mathrm{mkt}}] \in \mathbb{R}^{128}$$

### 2. Offline Indexing

For every historical timestamp $\tau < t$:
- State embedding $h_\tau$ is computed.
- Each expert $E^{(e)}$ in candidate pool $\mathcal{E} = \{E_1, \ldots, E_N\}$ is executed over forward horizon $H = 5$ days to compute realized return $R_\tau^{(e)}$, Sharpe ratio, and maximum drawdown.
- A Statement of Performance ($\mathrm{SoP}_\tau^{(e)}$) is generated summarizing market context, expert behavior, and uncertainty factors.
- Index entry stored: $\mathcal{D}_\tau = \left(h_\tau, \{R_\tau^{(e)}\}, \{\mathrm{SoP}_\tau^{(e)}\}\right)$.

### 3. Online Retrieval & Similarity Weighting

At decision time $t$:
1. Compute current embedding $h_t$.
2. Retrieve the $K = 3$ nearest historical regimes $\mathcal{N}_t = \mathrm{KNN}(h_t, \{h_\tau\}_{\tau < t}, K)$ using cosine similarity:
   $$\mathrm{sim}(h_t, h_\tau) = \frac{h_t \cdot h_\tau}{\|h_t\| \|h_\tau\|}$$
3. Compute normalized retrieval weights:
   $$w_\tau = \frac{\mathrm{sim}(h_t, h_\tau)}{\sum_{j \in \mathcal{N}_t} \mathrm{sim}(h_t, h_j)}$$
4. Compute similarity-weighted performance estimate for each expert $e$:
   $$\hat{R}_t^{(e)} = \sum_{\tau \in \mathcal{N}_t} w_\tau R_\tau^{(e)}$$

### 4. LLM Risk/Return Evaluator & Conservative Switching Rule

The retrieved SoPs, similarity-weighted performance summaries, and current market state description are supplied to the instruction-tuned LLM evaluator (Prompt Specification with temperature 0.1):
- **Role:** Financial risk analyzer operating within a dynamic MoE portfolio system.
- **Empirical Alignment Constraint:** Ground risk/return assessments strictly on observed historical MDD and realized information ratios in the retrieved context; no extrapolation beyond empirical observations; use historical baseline means for sparse regimes.
- **Conservative Margining Constraint:** Apply risk penalty buffer $\tau \geq 2\epsilon$ before recommending a switch from incumbent policy $\pi_N(s)$.
- **Tail-Event Separation Constraint:** Verify that candidate specialist performance outside its target regime does not fall below the weakest baseline expert.
- **Output:** Strict JSON:
  ```json
  {
    "expert_id": "E_N+1",
    "calculated_rho": "<float>",
    "confidence_bound_epsilon": "<float>",
    "regime_separation_margin_tau": "<float>",
    "tail_optimal_flag": "<boolean>"
  }
  ```
- **Switching Rule:**
  $$\pi_{N+1}(s) = \begin{cases} e^*(s), & \rho_{e^*(s)}(s) - \rho_{\pi_N(s)}(s) > \tau \\ \pi_N(s), & \text{otherwise} \end{cases}$$
  where $e^*(s) = \arg\max_{i} \rho_i(s)$.

### 5. Portfolio Weight Generation

The selected expert $E^{(e^*)}$ generates the continuous asset weight vector:
$$w_t = E^{(e^*)}(S_t) \in \mathbb{R}^A, \quad \sum_{i=1}^A w_{t, i} = 1$$
Candidate expert models:
- **A2C (Advantage Actor-Critic):** Synchronous policy-gradient baseline.
- **DDPG (Deep Deterministic Policy Gradient):** Off-policy continuous action actor-critic.
- **PPO (Proximal Policy Optimization):** Clipped objective policy-gradient.
- **TQC (Truncated Quantile Critics):** Distributional RL with quantile truncation for risk sensitivity.
- **CrossQ:** Modern off-policy actor-critic with batch normalization across critic updates.

## Required data

- **Asset Universe & Panels (30 assets per market panel):**
  - **Cryptocurrency (30 assets):** ADA, APT, ARB, ATOM, AVAX, BCH, BNB, BTC, DOGE, DOT, EGLD, ETC, ETH, FIL, HBAR, ICP, LINK, LTC, MATIC, MKR, NEAR, RNDR, SHIB, SOL, TON, TRX, UNI, VET, XLM, XRP (quoted in USD). Historical sample ranges span from 2014-09-17 (BTC, LTC) up to 2026-05-31 (1,311 to 4,275 daily samples per symbol).
  - **Equities (30 US stocks):** AAPL, ABBV, ACN, AMZN, BAC, BRK-B, COST, CRM, CVX, DIS, GOOGL, HD, JNJ, JPM, KO, LIN, MA, MCD, META, MRK, MSFT, NVDA, PEP, PG, TMO, TSLA, UNH, V, WMT, XOM. Sample range: 2000-01-03 to 2026-05-29 (3,372 to 6,641 daily samples).
  - **Foreign Exchange (30 currency pairs):** AUDCAD, AUDCHF, AUDJPY, AUDNZD, AUDUSD, CADJPY, CHFJPY, EURAUD, EURCAD, EURCHF, EURGBP, EURJPY, EURNZD, EURSEK, EURTRY, EURUSD, GBPAUD, GBPCAD, GBPCHF, GBPJPY, GBPNZD, GBPUSD, NZDCAD, NZDCHF, NZDJPY, NZDUSD, USDCAD, USDCHF, USDJPY, USDTRY. Sample range: 2000-01-03 to 2026-05-29 (5,212 to 6,876 daily samples).
- **Market Indices & Benchmarks:**
  - Crypto: Synthetic volume-weighted index (primary) and equal-weighted index.
  - Stocks: S&P 500, NASDAQ Composite, Dow Jones Industrial Average.
  - Forex: Composite feature stream across all pairs (no single market index).
- **Timeframe & Sampling:** Daily OHLCV bars.
- **Feature Set:** Rolling window $L = 22$ trading days of log-returns, RSI, MACD, ATR, realized volatility, and volume changes.
- **Point-in-Time Discipline:** Retrieval index constructed strictly chronologically; test-time retrieval queries restricted to historical records $\tau < t$ to eliminate look-ahead leakage.

## Execution assumptions

- **Decision Cadence:** Rebalancing occurs every $H = 5$ trading days.
- **Execution Timing:** Trades executed at the close/open of each 5-day cycle.
- **Order Model:** Assumed market/limit fill at daily settlement/close price.
- **Positioning & Leverage:** Long-only portfolio weights ($w_{t, i} \geq 0$, $\sum w_{t, i} = 1$). No short selling or margin leverage modeled in the primary benchmark.
- **Transaction Costs & Slippage:** The authors note standardized transaction-cost assumptions across comparison models, but do not provide an explicit basis-point breakdown (maker/taker fees and slippage parameters are an explicit provenance/data gap in the published text).

## Evidence

### Source-reported

All quantitative figures below are directly reported by Ahmad Asadi and Reza Safabakhsh (`arXiv:2608.28252v1`, August 2026):

#### 1. Standalone Expert Heterogeneity (Table 5)
Evaluated across single complete 30-symbol panels:
- **Cryptocurrency:**
  - TQC: Cum. Return 76.16%, Sharpe 1.71, Sortino 2.63, MDD -29%, Weeks Dominant 18 (32.7%).
  - DDPG: Cum. Return 71.26%, Sharpe 1.74, Sortino 2.73, MDD -26%, Weeks Dominant 6 (10.9%).
  - A2C: Cum. Return 63.00%, Sharpe 1.61, Sortino 2.44, MDD -25%, Weeks Dominant 19 (34.5%).
  - PPO: Cum. Return 60.49%, Sharpe 1.57, Sortino 2.38, MDD -27%, Weeks Dominant 3 (5.5%).
  - CrossQ: Cum. Return 53.66%, Sharpe 1.44, Sortino 2.24, MDD -28%, Weeks Dominant 9 (16.4%).
- **Stock Market:**
  - CrossQ: Cum. Return 38.21%, Sharpe 0.95, Sortino 1.42, MDD -27%, Weeks Dominant 32 (36.4%).
  - PPO: Cum. Return 33.38%, Sharpe 0.96, Sortino 1.46, MDD -22%, Weeks Dominant 21 (23.9%).
  - A2C: Cum. Return 32.16%, Sharpe 0.90, Sortino 1.35, MDD -23%, Weeks Dominant 17 (19.3%).
  - TQC: Cum. Return 32.09%, Sharpe 0.86, Sortino 1.28, MDD -26%, Weeks Dominant 13 (14.8%).
  - DDPG: Cum. Return 28.89%, Sharpe 0.85, Sortino 1.26, MDD -24%, Weeks Dominant 5 (5.7%).
- **Foreign Exchange:**
  - A2C: Cum. Return 4.27%, Sharpe 0.88, Sortino 1.20, MDD -2.18%, Weeks Dominant 6 (6.8%).
  - PPO: Cum. Return 4.07%, Sharpe 0.88, Sortino 1.20, MDD -2.00%, Weeks Dominant 9 (10.2%).
  - CrossQ: Cum. Return 2.62%, Sharpe 0.53, Sortino 0.69, MDD -2.68%, Weeks Dominant 18 (20.5%).
  - TQC: Cum. Return 2.26%, Sharpe 0.48, Sortino 0.60, MDD -2.18%, Weeks Dominant 43 (48.9%).
  - DDPG: Cum. Return 1.80%, Sharpe 0.36, Sortino 0.46, MDD -2.85%, Weeks Dominant 12 (13.6%).

#### 2. Expert Selection Comparison (Table 6)
- **Cryptocurrency:**
  - Best Fixed Expert: Cum. Return 68%, Ann. Return 62%, Ann. Vol. 0.32, Sharpe 1.64, Sortino 2.54, MDD -27%.
  - Recent-Performance Gating: Cum. Return 69%, Ann. Return 62%, Ann. Vol. 0.32, Sharpe 1.66, Sortino 2.57, MDD -27%.
  - **Proposed RAG:** Cum. Return 71%, Ann. Return 64%, Ann. Vol. 0.31, Sharpe 1.73, Sortino 2.72, MDD -26%.
- **Stock Market:**
  - Best Fixed Expert: Cum. Return 26%, Ann. Return 14%, Ann. Vol. 0.21, Sharpe 0.74, Sortino 1.11, MDD -26%.
  - Recent-Performance Gating: Cum. Return 33%, Ann. Return 17%, Ann. Vol. 0.20, Sharpe 0.91, Sortino 1.37, MDD -24%.
  - **Proposed RAG:** Cum. Return 34%, Ann. Return 18%, Ann. Vol. 0.19, Sharpe 0.96, Sortino 1.45, MDD -26%.
- **Foreign Exchange:**
  - Best Fixed Expert: Cum. Return 3.2%, Ann. Return 1.8%, Ann. Vol. 0.026, Sharpe 0.71, Sortino 0.92, MDD -1.9%.
  - Recent-Performance Gating: Cum. Return -0.4%, Ann. Return -0.2%, Ann. Vol. 0.029, Sharpe -0.062, Sortino -0.08, MDD -2.6%.
  - **Proposed RAG:** Cum. Return 4.3%, Ann. Return 2.4%, Ann. Vol. 0.028, Sharpe 0.88, Sortino 1.20, MDD -2.2%.

#### 3. Component Ablation (Table 8)
- **Cryptocurrency:**
  - No Retrieval (NR): Cum. Return +64.8%, Sharpe 1.622, MDD -26.7%.
  - No LLM (R$-$LLM): Cum. Return +69.1%, Sharpe 1.661, MDD -27.1%.
  - Full Framework (R+L+U): Cum. Return 71%, Sharpe 1.73, MDD -26%.
- **Stock Market:**
  - No Retrieval (NR): Cum. Return +33.1%, Sharpe 0.911, MDD -24.4%.
  - No LLM (R$-$LLM): Cum. Return +25.5%, Sharpe 0.735, MDD -26.5%.
  - Full Framework (R+L+U): Cum. Return 34%, Sharpe 0.96, MDD -26%.
- **Foreign Exchange:**
  - No Retrieval (NR): Cum. Return +3.2%, Sharpe 0.710, MDD -1.9%.
  - No LLM (R$-$LLM): Cum. Return -0.2%, Sharpe -0.025, MDD -2.4%.
  - Full Framework (R+L+U): Cum. Return 4.3%, Sharpe 0.88, MDD -2.2%.

#### 4. Model Sensitivity & Benchmark Comparisons (Tables 7, 9, 10, 11)
- **Pool Size Scaling (Table 7):** Expanding from 1 to 4 complementary experts monotonically improves Sharpe: Crypto $\Delta$Sharpe +19.8% (0.96 to 1.15), Stocks +22.0% (0.59 to 0.72), Forex +27.5% (0.51 to 0.65).
- **Indexing Model Compliance (Table 9):** Google/Gemma4-E4B succeeded in formatting structured index metadata in only 28% of cases (72% failure); Google/Gemma4-31B-it achieved 96% success; AliBaba/Qwen3.6-27B-it achieved 100% success.
- **Inference LLM Sensitivity (Table 10):** Qwen3.6-27B-it achieves Sharpe 1.73 (Crypto), 0.96 (Stocks), and 0.88 (Forex). Gemma4-E4B collapses in Forex to Cum. Return -5.4%, Sharpe -1.07, MDD -5.6%.
- **SOTA Comparison (Table 11):**
  - Crypto: Proposed (Sharpe 1.73, MDD -26%) vs LLM-MAS (Sharpe 1.50, MDD -28%), TAC (Sharpe 1.29, MDD -31%), AlphaMixRL (Sharpe 1.38, MDD -29%).
  - Stocks: Proposed (Sharpe 0.96, MDD -26%) vs Multi-LLM Black-Litterman (Sharpe 0.91, MDD -29%), AlphaMixRL (Sharpe 0.82, MDD -27%), TAC (Sharpe 0.74, MDD -28%).
  - Forex: Proposed (Sharpe 0.88, MDD -2.2%) vs Fine-tuned LLaMA (Sharpe 0.76, MDD -3.1%), AlphaMixRL (Sharpe 0.68, MDD -4.6%), TAC (Sharpe 0.61, MDD -5.1%).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Single-Run Point Estimate Protocol:** All reported metrics are point estimates from a single experimental pass on a single GPU per market panel; statistical dispersion across different random seeds is not provided.
- **Unisolated Uncertainty Ablation:** The ablation study did not include an isolated test removing only the uncertainty calibration component while holding retrieval and LLM reasoning constant.
- **Small Model Failure Mode:** Inference with smaller models (e.g., Gemma4-E4B) produces negative returns and negative Sharpe ratios in Forex (-5.4% return, -1.07 Sharpe), indicating that the system's viability depends heavily on high-capacity LLM reasoning.
- **Drawdown Non-Dominance:** In Stocks and Forex, the no-retrieval variant recorded a lower MDD (-24.4% vs -26% in Stocks; -1.9% vs -2.2% in Forex), demonstrating that retrieval-guided switching does not unconditionally minimize drawdown across every market.

## Falsification plan

To test whether the reported performance is genuine alpha or an artifact of sample selection, execute the following falsification protocol:
1. **Random Seed Dispersion Test:** Train the 5 underlying RL experts across 10 distinct random seeds. Measure whether the RAG switcher's advantage over the best fixed expert remains statistically significant ($p < 0.01$ under paired t-test).
2. **Shuffled-Embedding Placebo Test:** Replace the retrieved nearest-neighbor states $\mathcal{N}_t$ with 3 randomly sampled historical states from the database. If portfolio Sharpe ratio does not degrade toward or below recent-performance gating, the latent similarity metric provides no predictive regime signal.
3. **Turnover & Slippage Stress Test:** Apply realistic fee and slippage tiers: 5 bps, 10 bps, and 20 bps per round-trip rebalance. Calculate portfolio turnover rate $\frac{1}{2}\sum |w_{t} - w_{t-1}|$. If switching friction consumes more than 20% of net cumulative returns, the strategy cannot be deployed in production.
4. **Out-of-Sample Regime Shock Audit:** Evaluate performance specifically across out-of-sample stress windows (e.g., March 2020 crash, May 2021 crypto deleveraging, November 2022 FTX collapse). If the conservative margin $\tau$ causes delayed switching into defensive experts resulting in drawdowns exceeding 35%, the conservative switching axiom fails in practice.
5. **Ablation of LLM Prompt Guidance:** Replace the LLM reasoning step with a simple deterministic argmax over $\hat{R}_t^{(e)}$ adjusted by historical variance. If the LLM produces no statistically measurable margin over the deterministic formula, remove the LLM to eliminate operational latency and cost.

## Crypto portability

- **Portability Classification:** `adapted`
- **Portability Rationale:** Although the authors empirically test their framework on a 30-cryptocurrency spot/USD panel from 2014 to 2026, the underlying strategy treats crypto as an unconstrained, long-only spot portfolio rebalanced every 5 days. It does not account for the structural mechanisms of crypto derivatives.
- **Crypto-Specific Friction & Adaptation Requirements:**
  - **Perpetual Futures & Funding Rates:** Applying this expert-switching framework to crypto perpetuals requires incorporating funding rate carry into the state representation and expert reward functions. Holding long positions in high-funding regimes can erode returns.
  - **Execution & Liquidity Fragmentation:** Top 30 crypto tokens exhibit extreme dispersion in depth. Rebalancing 30 assets simultaneously every 5 days on spot venues incurs substantial taker fee and slippage costs on mid-cap tokens (e.g., EGLD, FIL, RNDR).
  - **24/7 Continuous Trading:** Traditional daily candle boundaries (00:00 UTC) can miss sharp weekend regime breaks; continuous intraday monitoring or event-driven rebalancing triggers may be required.
  - **Stablecoin & Quote Asset Risk:** Porting requires modeling depegging risk and venue-specific counterparty exposures across centralized and decentralized venues.

## Limitations

- **Omission of Explicit Fee/Slippage Schedules:** The paper does not specify the exact basis-point transaction fee or slippage model used in the main backtest tables (provenance gap).
- **Single Experimental Seed:** Point-estimate reporting limits statistical verification of robustness across random initializations.
- **Inference Latency & Operational Cost:** Querying a 27B+ parameter LLM at each portfolio rebalancing step introduces operational complexity, API/compute expenses, and non-zero inference failure risk.
- **Pretrained VAE Representation Drift:** The dual-stream Transformer-VAE requires offline pretraining; structural regime evolution over multi-year horizons may lead to latent representation drift unless periodic retraining is implemented.
- **5-Day Rebalancing Inflexibility:** Fixed 5-day holding horizons cannot dynamically react to sharp intraday flash crashes or liquidation cascades occurring within the holding interval.

## Implementation status

`not-implemented`

No implementation in PyBroker, NautilusTrader, or our execution engine has been conducted. This record represents normalized theoretical research only.

## Adoption boundary

- **Status:** `research-only`
- **Adoption Status:** `not-approved`
- **Approval Scope:** `research-only`

Presence in this repository does not indicate strategy approval, statistical validation in our backtesting engine, paper trading authorization, testnet testing, or live capital allocation.

## Related Wiki records

- `[[quant/cross-sectional-volatility-regime-gated-residual-mixture-of-experts-2026-09-02]]`
- `[[quant/regime-adaptive-continual-learning-portfolio-management-recap-2026-09-02]]`
- `[[quant/alphazerobeta-recurrent-ppo-market-neutral-portfolio-2026-09-02]]`
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`
- `[[quant/backtest-overfitting-pbo-cscv-2026-08-27]]`

## Sources

1. Ahmad Asadi and Reza Safabakhsh. *"Regime-Aware Portfolio Management via Retrieval-Augmented LLM-Guided Expert Switching"*, arXiv preprint `arXiv:2608.28252v1 [cs.AI, cs.LG, q-fin.PM, q-fin.ST]`, submitted August 28, 2026. DOI: `10.48550/arXiv.2608.28252`. URL: [https://arxiv.org/abs/2608.28252](https://arxiv.org/abs/2608.28252). HTML Full Text: [https://arxiv.org/html/2608.28252v1](https://arxiv.org/html/2608.28252v1).
2. Author LaTeX Source and Figure Package: `https://arxiv.org/e-print/2608.28252` (snapshot 2026-08-28/31, containing `manuscript.tex`, `01_introduction.tex`, `02_literature_review.tex`, `03_proposed_method.tex`, `04_experimental_results.tex`, `05_conclusion.tex`, and asset panel data).
