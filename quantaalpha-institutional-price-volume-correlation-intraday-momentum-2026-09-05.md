---
schema: strategy-research-record-v1
title: "QuantaAlpha Institutional Price-Volume Correlation and Intraday Return Momentum Factor via Trajectory-Level Evolutionary Mining in Cross-Sectional Equities"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cross-sectional-equity
  - price-volume-correlation
  - institutional-momentum
  - evolutionary-algorithm
  - quantaalpha
  - genetic-programming
  - trajectory-crossover
  - cs-rank-norm
  - topk-dropout
status: research-only
confidence: high
source_as_of: 2026-02-06
sources:
  - "Jun Han, Shuo Zhang, Wei Li, Yifan Dong, Tu Hu, Yumo Zhu, Xiaomin Yu, Xin Guo, Zhaowei Liu, Kunyi Wang, Jingping Liu, Tianyi Jiang, Ruichuan An, Sen Hu, Zhi Yang, Ronghao Chen, and Huacan Wang, 'QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining', arXiv:2602.07085v1 [cs.AI, q-fin.CP, q-fin.ST], February 6, 2026. DOI: 10.48550/arXiv.2602.07085. https://arxiv.org/abs/2602.07085"
  - "QuantaAlpha Team, 'QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining', GitHub repository, commit b7ceb27b1001261d7a95b209a963664ae1f8ab23. https://github.com/QuantaAlpha/QuantaAlpha"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# QuantaAlpha Institutional Price-Volume Correlation and Intraday Return Momentum Factor via Trajectory-Level Evolutionary Mining in Cross-Sectional Equities

## Provenance

- **Primary Research Paper:** Jun Han (SUFE), Shuo Zhang (QuantaAlpha), Wei Li (SUFE), Yifan Dong (SUFE), Tu Hu (QuantaAlpha), Yumo Zhu (SUFE), Xiaomin Yu (QuantaAlpha), Xin Guo (SUFE), Zhaowei Liu (SUFE), Kunyi Wang (QuantaAlpha), Jingping Liu (SYSU), Tianyi Jiang (PKU), Ruichuan An (PKU), Sen Hu (QuantaAlpha, PKU), Zhi Yang (SUFE), Ronghao Chen (QuantaAlpha, PKU), and Huacan Wang (QuantaAlpha), *"QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining"*, arXiv preprint `arXiv:2602.07085v1 [cs.AI, q-fin.CP, q-fin.ST]`, submitted February 6, 2026.
- **Canonical arXiv Abstract URL:** [https://arxiv.org/abs/2602.07085](https://arxiv.org/abs/2602.07085)
- **Direct HTML Full Text:** [https://arxiv.org/html/2602.07085v1](https://arxiv.org/html/2602.07085v1)
- **Digital Object Identifier (DOI):** [10.48550/arXiv.2602.07085](https://doi.org/10.48550/arXiv.2602.07085)
- **Official Open-Source Code Repository:** [https://github.com/QuantaAlpha/QuantaAlpha](https://github.com/QuantaAlpha/QuantaAlpha)
- **Immutable Commit SHA:** `b7ceb27b1001261d7a95b209a963664ae1f8ab23` (verified against remote repository HEAD).
- **Primary Source Package:** Inspected directly from official arXiv LaTeX source bundle `arXiv:2602.07085` containing `acl_latex.tex`, `main_section/1.introduction.tex`, `main_section/3.problem_formulation.tex`, `main_section/4.method.tex`, `main_section/5.experiments.tex`, `main_section/6.conclusion.tex`, `appendix/1.app_1.tex`, `appendix/2.app_2.tex`, `appendix/3.app_3.tex`, `tables/main_table.tex`, `tables/ablation_table.tex`, `tables/2.app_2.tex`, and `tables/3.app_3.tex`. All mathematical expressions, operator specifications, empirical metrics, factor identities, and ablation figures trace directly to this primary LaTeX package.
- **Pre-Write Deduplication & Identity Audit:** A rigorous audit across all 390 existing repository records confirmed zero matches for `2602.07085`, `QuantaAlpha`, `Institutional_Momentum_Score_20D`, `c57cace576a95356`, `df5a496878f4`, or `b7ceb27b1001261d7a95b209a963664ae1f8ab23`. This record represents an independent, source-verified capture of a concrete formulaic alpha factor and its evolutionary multi-agent generation architecture.

## Economic mechanism

### Source-reported

In quantitative equity investment, automated alpha mining using Large Language Models (LLMs) faces three structural vulnerabilities:
1. **Fragile Controllability:** Iterative factor refinement guided solely by noisy historical backtesting results induces severe semantic drift. The LLM gradually alters the underlying economic intuition to chase spurious in-sample correlations, producing fragile, overfitted expressions.
2. **Limited Trustworthiness & Lineage:** Standard multi-agent systems rely on stochastic re-prompting conditioned on transient conversational context. They discard intermediate research steps, failing to systematically inherit and recombine validated economic rationales across iterations.
3. **Constrained Exploration & Crowding:** Unconstrained search over-exploits narrow neighborhoods surrounding initial seed factors, leading to factor crowding and premature convergence to suboptimal local optima.

To resolve these defects, QuantaAlpha treats every end-to-end factor discovery run as an ordered, auditable research trajectory:
$$\tau = (s_0, a_0, s_1, a_1, \ldots, s_n)$$
where $s_0$ is the initial market context, $a_i$ represents an agentic action (hypothesis proposal, symbolic factor realization, AST parsing, consistency verification, code generation, or backtest evaluation), and $s_n$ is the terminal state containing backtest metrics.

Rather than re-generating factors from scratch, the system improves factor quality via **trajectory-level self-evolution**:
- **Controlled Mutation:** Self-reflection localizes the specific decision node $k$ responsible for suboptimal performance (e.g., an overly complex nested expression or an unconstrained holding period), freezing the valid prefix $(s_0, a_0, \ldots, s_k)$ and rewriting only the faulty segment $\mathrm{Refine}(a_k)$.
- **Hypothesis Crossover:** Recombines complementary high-reward segments from two distinct parent trajectories. In the documented case study, the LLM combines:
  - *Parent 1 (Trajectory `1e6d57e38e89`, Round 7 Mutation):* The **Retail Speculative Herding Hypothesis**, which posits that when retail investors chase momentum in high-attention stocks while institutional ownership declines and fundamentals deteriorate, the resulting upward price pressure is unsustainable and leads to mean reversion.
  - *Parent 2 (Trajectory `47e0f0e55382`, Round 6 Crossover):* The **Institutional Structural Momentum Hypothesis**, which posits that medium-term price trends driven by persistent institutional accumulation and confirmed by order-flow microstructure alignment generate robust, sustainable price continuation.
  - *Synthesized Offspring Hypothesis (Trajectory `df5a496878f4`, Round 8 Crossover):* A **Dual-Source Momentum Factor** (`Institutional_Momentum_Score_20D`, Factor ID `c57cace576a95356`), asserting that institutional sponsorship manifests through coordinated price-volume co-movement and end-of-day closing strength.

### Research interpretation

From a market microstructure and institutional order-flow perspective, the economic mechanism operates via two distinct, complementary channels:
1. **Informed Order-Flow Footprint ($\rho_{20}(\Delta P/P, \Delta V/V)$):** Institutional market participants execute large parent orders via algorithmic slicing (VWAP, TWAP, or POV meta-orders) over multiple days. Unlike retail noise trading where volume surges on emotional spikes regardless of price direction, institutional accumulation absorbs available ask depth, causing volume expansion to correlate positively with positive daily price changes ($\Delta P/P > 0$ when $\Delta V/V > 0$). Conversely, institutional distribution pushes prices downward as selling pressure expands volume. A high 20-day rolling Pearson correlation between price returns and percentage volume innovations serves as a robust proxy for persistent institutional sponsorship.
2. **Intraday Accumulation Bias ($\overline{(C - O)/C}_5$):** Institutional execution algorithms are typically most active approaching market close (Market-On-Close / benchmark matching), creating persistent buying pressure from opening call auction to closing bell when accumulating. Retail traders, by contrast, frequently trade in the opening 30 minutes following overnight news. Measuring the trailing 5-day average ratio of $(Close - Open)/Close$ isolates intraday price progression from opening auction shocks, capturing short-term institutional buying conviction.
3. **Cross-Sectional Interaction:** Multiplying 20-day institutional co-movement by 5-day intraday accumulation and ranking across the cross-section isolates securities experiencing simultaneous institutional sponsorship and short-term accumulation, filtering out noise-driven retail breakouts that lack institutional volume confirmation.

## Signal

### 1. Mathematical Formulation

The single-factor trading signal for security $i$ at date $t$, denoted as $\text{IMS}_{20D}(i, t)$, is defined as:

$$\text{IMS}_{20D}(i, t) = \operatorname{RANK}\left( \rho_{20}\left( \frac{P_{i,t} - P_{i,t-1}}{P_{i,t-1}}, \frac{V_{i,t} - V_{i,t-1}}{V_{i,t-1}} \right) \times \frac{1}{5} \sum_{k=0}^{4} \frac{C_{i,t-k} - O_{i,t-k}}{C_{i,t-k}} \right)$$

where:
- $P_{i,t}$ and $C_{i,t}$ represent the closing price of stock $i$ on trading day $t$;
- $O_{i,t}$ represents the opening price of stock $i$ on trading day $t$;
- $V_{i,t}$ represents the trading volume of stock $i$ on trading day $t$;
- $\frac{P_{i,t} - P_{i,t-1}}{P_{i,t-1}} = \frac{\Delta P_{i,t}}{P_{i,t-1}}$ is the 1-day percentage price return;
- $\frac{V_{i,t} - V_{i,t-1}}{V_{i,t-1}} = \frac{\Delta V_{i,t}}{V_{i,t-1}}$ is the 1-day percentage volume change;
- $\rho_{20}(\cdot, \cdot)$ denotes the rolling 20-trading-day Pearson correlation coefficient;
- $\frac{1}{5} \sum_{k=0}^{4} \frac{C_{i,t-k} - O_{i,t-k}}{C_{i,t-k}}$ is the 5-day rolling arithmetic mean of the intraday return ratio;
- $\operatorname{RANK}(\cdot)$ is the cross-sectional percentile rank normalization applied across all eligible stocks on date $t$, scaling factor scores to the uniform interval $[0, 1]$.

### 2. Symbolic Operator Specification (AST Intermediate Representation)

In the standardized QuantaAlpha Domain-Specific Language (DSL) / Qlib operator library, the factor expression is canonically represented as:

```text
RANK(TS_CORR(DELTA($close, 1)/$close, DELTA($volume, 1)/$volume, 20) * TS_MEAN(($close - $open)/$close, 5))
```

- **Symbolic Length:** 105 characters (complies with QuantaAlpha complexity ceiling $\le 250$ characters).
- **Base Feature Count:** 3 raw fields utilized (`$close`, `$open`, `$volume`; complies with ceiling $\le 6$ features).
- **Free Parameters:** 2 window lengths (20 days, 5 days; parameter ratio $< 50\%$).
- **Subtree Isomorphism:** Maximum AST subtree match against existing alpha zoo $< 5$ nodes.

### 3. Portfolio Construction & Order Execution Logic

The source evaluates the factor using the **TopkDropoutStrategy** within the Qlib quantitative backtesting engine:
- **Universe:** CSI 300 constituents (300 largest, most liquid A-share equities).
- **Portfolio Size ($topk$):** Fixed at $K = 50$ stocks (source-reported).
- **Rebalance Frequency:** Daily at market open (source-reported).
- **Selection & Turnover Gate ($n_{\text{drop}}$):** On each trading day $t$, all stocks in the universe are ranked by $\text{IMS}_{20D}$ (or predicted score from the downstream synthesizer). The $n_{\text{drop}} = 5$ lowest-scoring current holdings are liquidated and replaced with the 5 highest-ranked non-held candidate stocks (source-reported). This bounds daily turnover to approximately $10\%$ of portfolio value per day ($5 / 50 = 0.10$).
- **Weighting Scheme:** Equal weighting across all 50 active holdings ($w_i = 1/50 = 2.0\%$ per position; source-reported).
- **Target Forecast Horizon:** Next-day open-to-open excess return:
  $$y_t = \frac{P_{t+2}^{\text{close}}}{P_{t+1}^{\text{close}}} - 1 \quad \text{with order execution at } P_{t+1}^{\text{open}} \text{ (source-reported)}$$
- **Halt & Limit Filter:** Stocks that hit the 9.5% daily price change limit (`Limit Threshold = 9.5%`) are treated as untradable; executions for halted/limited stocks are deferred until limits expand (source-reported).

### 4. Full Factor Pool Synthesis (System-Level Signal)

Beyond single-factor evaluation, QuantaAlpha deploys a greedy, Rank IC-driven global factor pool:
- **Pool Admission Rule:** Factors generated across 5 iterations are sorted in descending order by validation Rank IC. A factor is admitted into the pool if and only if its pairwise absolute correlation with every factor already in the pool satisfies $|\rho| < 0.70$ (source-reported functional redundancy filter).
- **Pool Capacity:** Capped at $50\%$ of all candidate factors mined, yielding approximately $150$ validated, orthogonal factors (source-reported).
- **Downstream Predictor:** LightGBM gradient boosted decision tree trained on the 150-factor panel to predict next-day cross-sectional return ranks (source-reported).

## Required data

- **Asset Universe:** China Securities Index 300 (CSI 300), with out-of-sample transfer evaluation on CSI 500 and S&P 500 (source-reported).
- **Market Type:** Cash Equities (Chinese A-Shares; U.S. Equities for cross-market transfer).
- **Sampling Frequency:** Daily OHLCV bars.
- **Required Raw Fields:**
  - Open price (`$open`)
  - High price (`$high`)
  - Low price (`$low`)
  - Close price (`$close`)
  - Trading volume (`$volume`)
  - Volume-weighted average price (`$vwap`)
- **Data Split & Chronological Boundaries:**
  - *In-Sample Training Period:* January 1, 2016 to December 31, 2020 (5 calendar years; source-reported).
  - *Validation Period:* January 1, 2021 to December 31, 2021 (1 calendar year; source-reported).
  - *Out-of-Sample Test Period:* January 1, 2022 to December 26, 2025 (4 calendar years, 966 trading days; source-reported).
- **Preprocessing & Cleaning Protocol:**
  - Forward-fill missing feature values; replace infinite values with column boundaries; drop rows with missing forward labels (source-reported).
  - Apply cross-sectional rank normalization (`CSRankNorm`) independently to features and return labels on each datetime $t$ (source-reported).
- **Lookahead & Point-in-Time Safeguards:** Trailing rolling operators (`TS_CORR`, `TS_MEAN`, `DELTA`) use strictly backward-looking windows $[t-k, t]$. Feature extraction is finalized at market close $t$; order placement is executed at open $t+1$, strictly preventing lookahead bias.

## Execution assumptions

- **Signal-to-Order Timing:** Factor scores computed after market close on day $t$. Target portfolio generated prior to market open on day $t+1$. Orders submitted for execution at market open on day $t+1$ (`deal_price = Open`; source-reported).
- **Order Type & Fill Model:** Simulated Market-On-Open orders filled at the opening price $P_{t+1}^{\text{open}}$ (source-reported).
- **Transaction Costs & Commissions (Chinese A-Shares):**
  - Buying Cost: $0.05\%$ ($5$ bps; commission fee; source-reported).
  - Selling Cost: $0.15\%$ ($15$ bps; commission fee $+$ government stamp duty; source-reported).
  - Round-Trip Transaction Drag: $0.20\%$ ($20$ bps per full position cycle; source-reported).
  - Robustness cost scaling evaluated at $1.5\times$ ($0.30\%$ round-trip) and $2.0\times$ ($0.40\%$ round-trip; source-reported).
- **Slippage & Market Impact:** Not explicitly modeled in the Qlib backtesting engine (`research-proposed` operational limitation; partially mitigated by restricting universe to liquid CSI 300 large-cap stocks and limiting daily turnover via $n_{\text{drop}} = 5$).
- **Borrowing & Shorting Availability:** Naked shorting is prohibited in mainland Chinese A-share markets. All portfolio metrics are evaluated on a **long-only equal-weighted portfolio** relative to the benchmark index:
  $$r_{\text{excess}, t} = r_{\text{portfolio}, t} - r_{\text{benchmark}, t} - c_{\text{transaction}, t} \quad \text{(source-reported)}$$
- **Capital Allocation & Leverage:** 100% equity invested; 0% cash drag; 1.0x leverage (no margin borrowing; `research-proposed` operational rule).

## Evidence

### Source-reported

All figures below are directly reported by Jun Han et al. (arXiv:2602.07085v1, February 2026) across the primary text, tables, and appendices:

#### 1. Single-Factor Backtest Performance: `Institutional_Momentum_Score_20D` (Appendix B & C, Table 3, Table 4)
Backtested on the CSI 300 universe under Qlib TopkDropout ($K=50$, $n_{\text{drop}}=5$, $0.20\%$ round-trip cost):
- **Information Coefficient (IC):** **0.0126** (vs. Baseline: 0.0058; $+117.2\%$ relative gain).
- **Rank IC:** **0.0311** (vs. Baseline: 0.0220; vs. Parent 1 `1e6d57e38e89`: 0.0216; vs. Parent 2 `47e0f0e55382`: 0.0246; $+26.4\%$ to $+44.0\%$ improvement over parents).
- **Annualized Excess Return (ARR):** **7.80%** (vs. Baseline: 5.20%; $+50.0\%$ improvement).
- **Information Ratio (IR):** **0.963** (vs. Baseline: 0.973; Parent 1: 1.297; Parent 2: 1.347).
- **Maximum Drawdown (MDD):** **-11.37%** (vs. Baseline: -7.30%).
- **Daily Excess Return (without transaction costs):** **0.0328%** per day.
- **Daily Excess Return (with transaction costs):** **0.0128%** per day ($20$ bps round-trip cost drag reduces daily alpha by $0.0200\%$).
- **Excess Return Standard Deviation:** **0.52%** daily.
- **Turnover Rate (Fractional Factor Replacement, FFR):** **100%** across evaluated holding cycles.
- **Neural/ML Loss Metrics:** L2 Train Loss: $0.9936$; L2 Validation Loss: $0.9962$.

#### 2. System-Level Out-of-Sample Performance on CSI 300 (Table 1, 2022–2025 Test Period, 966 Trading Days)
Evaluated using the complete QuantaAlpha 150-factor pool synthesized via LightGBM:
- **With GPT-5.2 Backbone:**
  - **IC:** **0.0472** (Top across all baselines; vs. AlphaAgent GPT-5.2: 0.0347; vs. RD-Agent GPT-5.2: 0.0286; vs. TRA Deep Learning: 0.0421; vs. Alpha158: 0.0131).
  - **ICIR:** **0.2691** (vs. AlphaAgent: 0.2122; RD-Agent: 0.1995; TRA: 0.3402).
  - **Rank IC:** **0.0459** (vs. AlphaAgent: 0.0334; RD-Agent: 0.0250; TRA: 0.0511).
  - **Rank ICIR:** **0.2635** (vs. AlphaAgent: 0.2053; RD-Agent: 0.1739; TRA: 0.4203).
  - **Information Ratio (IR / SHR\*):** **0.6453** (vs. AlphaAgent: 0.1587; RD-Agent: 0.5321; TRA: 1.0502; DoubleEnsemble: 0.2490).
  - **Annualized Excess Return (ARR):** **4.68%** (vs. AlphaAgent: 1.11%; RD-Agent: 3.58%; TRA: 6.81%; Alpha158: 2.66%).
  - **Maximum Drawdown (MDD):** **11.80%** (vs. AlphaAgent: 13.89%; RD-Agent: 16.76%; TRA: 8.51%; MLP: 18.15%).
- **With DeepSeek-V3.2 Backbone:**
  - **IC:** **0.0461**; **ICIR:** **0.2624**; **Rank IC:** **0.0450**; **Rank ICIR:** **0.2574**; **IR:** **0.6271**; **ARR:** **4.53%**; **MDD:** **15.10%**.
- **With Claude-4.5-Sonnet Backbone:**
  - **IC:** **0.0445**; **ICIR:** **0.2507**; **Rank IC:** **0.0431**; **Rank ICIR:** **0.2446**; **IR:** **0.5619**; **ARR:** **4.12%**; **MDD:** **13.02%**.
- **With Gemini-3-Pro-Preview Backbone:**
  - **IC:** **0.0453**; **ICIR:** **0.2551**; **Rank IC:** **0.0439**; **Rank ICIR:** **0.2490**; **IR:** **0.5834**; **ARR:** **4.21%**; **MDD:** **12.10%**.
- **With Qwen3-235B Backbone:**
  - **IC:** **0.0450**; **ICIR:** **0.2538**; **Rank IC:** **0.0444**; **Rank ICIR:** **0.2507**; **IR:** **0.3511**; **ARR:** **2.06%**; **MDD:** **16.36%**.

#### 3. Daily Statistical Significance across 966 Trading Days (Appendix A.4, Table 10)
- **DeepSeek-V3.2 Factor Library:**
  - Daily IC: Mean **0.0459**, Median **0.0448**, Std **0.1711**, Positive Days **60.97%**, $95\%$ CI $[0.0348, 0.0544]$, $t$-statistic **$7.93$**, $p$-value **$2.22 \times 10^{-15}$**.
  - Daily Rank IC: Mean **0.0418**, Median **0.0403**, Std **0.1694**, Positive Days **60.97%**, $95\%$ CI $[0.0311, 0.0525]$, $t$-statistic **$7.67$**, $p$-value **$1.73 \times 10^{-14}$**.
- **Claude-4.5-Sonnet Factor Library:**
  - Daily IC: Mean **0.0426**, Median **0.0513**, Std **0.1833**, Positive Days **60.04%**, $95\%$ CI $[0.0311, 0.0542]$, $t$-statistic **$7.23$**, $p$-value **$4.95 \times 10^{-13}$**.
  - Daily Rank IC: Mean **0.0409**, Median **0.0438**, Std **0.1827**, Positive Days **60.04%**, $95\%$ CI $[0.0293, 0.0524]$, $t$-statistic **$6.95$**, $p$-value **$3.68 \times 10^{-12}$**.

#### 4. Ablation of Evolutionary Mining Components (Table 2)
Starting from full QuantaAlpha (DeepSeek-V3.2: IC 0.0461, Rank IC 0.0450, ARR 4.53%, MDD 15.10%):
- **Without Planning:** IC $0.0448$ ($-0.0013$), Rank IC $0.0437$ ($-0.0013$), ARR $3.81\%$ ($-0.72\%$), MDD $16.72\%$ ($+1.62\%$).
- **Without Mutation:** IC $0.0382$ ($-0.0079$), Rank IC $0.0371$ ($-0.0079$), ARR $3.27\%$ ($-1.26\%$), MDD $15.58\%$ ($+0.48\%$). Removing mutation causes the largest degradation in predictive power.
- **Without Crossover:** IC $0.0401$ ($-0.0060$), Rank IC $0.0419$ ($-0.0031$), ARR $4.02\%$ ($-0.51\%$), MDD $16.03\%$ ($+0.93\%$).

#### 5. Cross-Market Zero-Shot Generalization (Section 5.4, Figure 1)
Factors mined strictly on CSI 300 transferred directly without fine-tuning:
- **CSI 500 Out-of-Sample:** Cumulative excess return reached approximately **$40.28\%$** over 2022–2025.
- **S&P 500 Out-of-Sample:** Cumulative excess return reached approximately **$19.1\%$** over 2022–2025.

### Independently reproduced

Not independently reproduced in our execution stack.

### Negative evidence

The primary research reveals critical negative empirical findings and risk boundaries:
1. **Automated LLM Rejection for Live Trading (Appendix C.5):** Despite delivering higher excess returns (7.80% vs 5.20%) and higher Rank IC (0.0311 vs 0.0220), the LLM evaluation agent explicitly issued a **`REJECTED`** decision for `Institutional_Momentum_Score_20D`. The unweighted synthesis of retail herding and institutional momentum amplified portfolio maximum drawdown (expanding from $-7.30\%$ to $-11.37\%$) and reduced the Information Ratio (from $0.973$ to $0.963$). The evaluator concluded that without explicit volatility-regime conditioning, the factor amplifies tail volatility during market turmoil.
2. **Catastrophic Failure of Classical Reversal Factors During the 2023 Style Shift (Appendix C.1–C.2, Table 2, Table 3):** When the Chinese market rotated from large-cap "core assets" to small-cap/thematic rotation in 2023, traditional exhaustion and reversal factors experienced severe negative performance:
   - `KineticLength_AbsRetSum_Z_10D`: Rank IC **-0.0720**, IC **-0.0246** (path-length choppiness inverted under rapid style rotation).
   - `Drawdown_Gated_NegCorr_60D_20D_thr20pct`: Rank IC **-0.0282**, IC **-0.0095** (hard drawdown gates became brittle).
   - `Relative_Volume_Calm_Reversal` (AlphaAgent baseline): Rank IC **-0.0279**, IC **-0.0188** (quiet-volume momentum divergence failed).
   - `Volume_Stability_Momentum_Divergence_40D` (AlphaAgent baseline): Rank IC **-0.0247**, IC **-0.0155**.
   - `LVR_Bottom_Fishing_20D` (AlphaAgent baseline): Rank IC **-0.0190**, IC **-0.0144** (bottom-fishing reversal became toxic when reversals were short-lived and crowded).
3. **Diminishing Returns & Redundancy Beyond 12 Iterations (Section 5.5, Figure 8):** Factor pool predictive power and risk-adjusted return do not scale monotonically with mining rounds. Strategy performance peaks at iterations 11–12 (~350 factors). Additional iterations introduce redundant noise and worsen drawdown.

## Falsification plan

To disconfirm or validate the empirical efficacy of the `Institutional_Momentum_Score_20D` factor and its regime-adaptive extensions:

1. **Volume Innovation Orthogonality Test:**
   - *Hypothesis:* The predictive power of $\rho_$ho_{20}(\Delta P/P, \Delta V/V)$ originates specifically from volume-confirmed institutional accumulation, not from raw price momentum or raw volume trend.
   - *Test:* Regress daily factor scores against 20-day price momentum (`ROCP(close, 20)`) and 20-day volume momentum (`ROCP(volume, 20)`). Extract orthogonal residuals $\epsilon_{i,t}$ and backtest residual factor scores under identical TopkDropout execution.
   - *Failure condition:* `research-defined falsification threshold`: If the residual factor's Rank IC falls below $0.010$ (or t-statistic $< 2.0$), falsify the hypothesis that price-volume covariance provides distinct institutional alpha beyond classical momentum.
2. **Frictional Cost & Slippage Stress Test:**
   - *Test:* Simulate the TopkDropout strategy across 4 cost regimes: 10 bps, 20 bps (baseline), 30 bps, and 40 bps round-trip transaction costs, combined with a linear temporary price impact model ($10\%$ participation rate penalty).
   - *Failure condition:* `research-defined falsification threshold`: If net annualized excess return drops below $1.50\%$ or net Information Ratio falls below $0.30$ under 30 bps round-trip costs, classify the strategy as an execution-sensitive artifact unable to survive live execution frictions.
3. **Volatility-Regime Conditioning Ablation:**
   - *Test:* Implement the LLM evaluator's recommended repair by scaling $\text{IMS}_{20D}$ by an inverse volatility ratio:
     $$\text{IMS}_{\text{gated}} = \text{IMS}_{20D} \times \left( \frac{\sigma_{60}}{\sigma_{10}} \right)$$
     comparing drawdown and Information Ratio across high-volatility episodes (e.g., April 2025 stress period).
   - *Failure condition:* `research-defined falsification threshold`: If volatility gating fails to reduce maximum drawdown by at least $25\%$ relative to the ungated factor (i.e. MDD fails to improve to better than $-8.5\%$), reject the hypothesis that simple volatility gating resolves the factor's turbulence fragility.
4. **Placebo Shuffled-Volume Test:**
   - *Test:* Randomly permute daily volume series across stocks while preserving price return series intact. Recompute $\text{IMS}_{20D}$ on permuted data across 500 Monte Carlo paths.
   - *Failure condition:* `research-defined falsification threshold`: If permuted factor Rank IC falls within $1.0$ standard error of the unpermuted Rank IC ($0.0311$), reject the claim that volume-price interaction contains genuine predictive information.

## Crypto portability

- **Portability Classification:** `adapted/unproven` (research interpretation; the primary source demonstrates the mechanism exclusively in Chinese A-shares and U.S. cash equities).
- **Structural Portability Challenges in Crypto Markets:**
  1. **Absence of Discrete Session Close:** The factor relies on $\overline{(C - O)/C}_5$ to isolate intraday price progression from opening auction noise. Crypto perpetual contracts trade 24/7 without opening or closing auctions. Porting requires defining artificial session boundaries (e.g., 00:00 UTC to 23:59 UTC) or substituting intraday return with funding-interval returns (e.g., 8-hour settlement windows).
  2. **Taker vs. Maker Volume & Wash Trading:** In cash equities, consolidated exchange tape provides reliable volume. In crypto, spot and perpetual venues suffer from wash trading and fee-tier distortions. Applying raw volume innovations $\Delta V/V$ without filtering for aggressive taker flow or toxic liquidation volume risks capturing artificial exchange-rebate volume rather than institutional accumulation.
  3. **Perpetual Funding Drag:** Rebalancing a 50-token portfolio daily in perpetual contracts incurs funding rate payments every 8 hours. If institutional accumulation is concentrated in high-funding altcoins, funding drag will rapidly erode reported excess returns.
  4. **Liquidity Skew & Tail Risk:** In crypto, low-liquidity altcoins frequently experience sudden liquidation wicks that distort rolling Pearson correlation calculations. Correlation estimators in crypto require Winsorization or robust Rank correlation (`TS_RANK_CORR`) to prevent outliers from dominating factor scores.

## Limitations

- **Omission of Slippage and Execution Latency:** Backtests assume perfect fills at the next-day opening price $P_{t+1}^{\text{open}}$ without slippage or market impact (`data gap`).
- **Underspecified Order Placement Protocol:** The exact auction mechanics for executing TopkDropout rebalances at Open are not specified (`underspecified`).
- **Short-Side Restrictions:** The empirical backtest evaluates long-only excess returns against the index due to Chinese A-share shorting constraints; true market-neutral dollar performance remains unproven (`research-proposed limitation`).
- **Computational Overhead of Evolutionary Search:** Generating full trajectories consumes ~1.8M tokens per 5-iteration run and requires hosted LLM API availability (`research-proposed limitation`).
- **Sensitivity to Market Rotation:** As documented in the 2023 empirical analysis, rapid cross-style market rotations can cause path-length and reversal factors to invert sharply (`unproven in turbulent regimes`).

## Implementation status

- `implementation_status: not-implemented`
- No code has been implemented in our research stack (`nautilus-quant-system`, PyBroker, or NautilusTrader).
- No historical backtest, paper trading, testnet, or live trading has been authorized or conducted.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- This record serves strictly as normalized research material documenting a peer-reviewed evolutionary agentic alpha discovery framework and a specific synthesized factor candidate. It does not constitute approval for trading, implementation, or capital allocation.

## Related Wiki records

- `cross-market-alpha191-short-term-trading-factors-double-selection-lasso-2026-09-03.md` (formulaic alpha factor screening and lasso regression)
- `aeap-seads-llm-agentic-factor-discovery-formulaic-alpha-2026-09-03.md` (LLM-driven formulaic alpha generation architectures)
- `agonalpha-prompt-economy-adversarial-review-agentic-alpha-discovery-2026-09-04.md` (adversarial multi-agent factor discovery)
- `alphacrafter-harness-multi-agent-cross-sectional-equity-alpha-2026-09-03.md` (multi-agent cross-sectional equity alpha generation)
- `alphar1-context-aware-alpha-screening-llm-reasoning-grpo-2026-09-03.md` (reinforcement learning reasoning for factor screening)
- `china-ashare-mask-first-upstream-contamination-adjusted-mse-2026-09-04.md` (Chinese A-share cross-sectional factor evaluation and leakage auditing)
- `china-ashare-xgboost-treeshap-behavioral-factor-decomposition-2026-09-04.md` (A-share behavioral factor modeling and TreeSHAP decomposition)

## Sources

1. **Primary Research Paper:** Jun Han, Shuo Zhang, Wei Li, Yifan Dong, Tu Hu, Yumo Zhu, Xiaomin Yu, Xin Guo, Zhaowei Liu, Kunyi Wang, Jingping Liu, Tianyi Jiang, Ruichuan An, Sen Hu, Zhi Yang, Ronghao Chen, and Huacan Wang, *"QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining"*, arXiv:2602.07085v1 [cs.AI, q-fin.CP, q-fin.ST], February 6, 2026. DOI: [10.48550/arXiv.2602.07085](https://doi.org/10.48550/arXiv.2602.07085). Canonical URL: [https://arxiv.org/abs/2602.07085](https://arxiv.org/abs/2602.07085). Direct HTML: [https://arxiv.org/html/2602.07085v1](https://arxiv.org/html/2602.07085v1).
2. **Official GitHub Repository:** QuantaAlpha Team, *"QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining"*, GitHub repository: [https://github.com/QuantaAlpha/QuantaAlpha](https://github.com/QuantaAlpha/QuantaAlpha), commit `b7ceb27b1001261d7a95b209a963664ae1f8ab23`.
3. **Underlying Baseline Frameworks:**
   - Microsoft Qlib Quantitative Platform: [https://github.com/microsoft/qlib](https://github.com/microsoft/qlib)
   - AlphaAgent: Tang et al., *"AlphaAgent: LLM-Driven Alpha Mining with Regularized Exploration to Counteract Alpha Decay"*, KDD 2025: [https://arxiv.org/abs/2402.06649](https://arxiv.org/abs/2402.06649)
   - RD-Agent: Li et al., *"R&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization"*, arXiv:2505.15155, 2025.
