---
schema: strategy-research-record-v1
title: "Alpha-R1: Context-Aware Alpha Factor Screening via Reinforcement-Learning Aligned LLM Reasoning"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - llm-reasoning
  - reinforcement-learning
  - grpo
  - factor-investing
  - alpha-screening
  - context-aware
  - multi-modal
  - cross-sectional-equity
status: research-only
confidence: medium
source_as_of: 2025-12-29
sources:
  - "Zuoyou Jiang, Li Zhao, Rui Sun, Ruohan Sun, Zhongjian Li, Jing Li, Daxin Jiang, Zuo Bai, and Cheng Hua, 'Alpha-R1: Alpha Screening with LLM Reasoning via Reinforcement Learning', arXiv preprint arXiv:2512.23515v1 [q-fin.PM, cs.AI, cs.LG], submitted December 29, 2025. Stable URL: https://arxiv.org/abs/2512.23515. DOI: https://doi.org/10.48550/arXiv.2512.23515"
  - "GitHub Repository: https://github.com/FinStep-AI/Alpha-R1, commit 61feaa359bd57761f5ac58f75af46ddfed2d2d7b, path README.md"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Alpha-R1: Context-Aware Alpha Factor Screening via Reinforcement-Learning Aligned LLM Reasoning

## Provenance

Primary source: Zuoyou Jiang, Li Zhao, Rui Sun, Ruohan Sun, Zhongjian Li, Jing Li, Daxin Jiang, Zuo Bai, and Cheng Hua (Shanghai Jiao Tong University, StepFun, and FinStep), *Alpha-R1: Alpha Screening with LLM Reasoning via Reinforcement Learning*, arXiv preprint `arXiv:2512.23515v1 [q-fin.PM, cs.AI, cs.LG]`, submitted December 29, 2025. Stable URL: `https://arxiv.org/abs/2512.23515`; DOI: `https://doi.org/10.48550/arXiv.2512.23515`.

Associated public implementation repository: `https://github.com/FinStep-AI/Alpha-R1`, immutable commit SHA `61feaa359bd57761f5ac58f75af46ddfed2d2d7b`, file `README.md`. As of this Scout run, the repository provides the paper link, citation, and project roadmap indicating that inference code and model weights are being prepared for public release.

Repository-wide and Hermes Wiki Brain searches found no prior record for `arXiv:2512.23515`, `Alpha-R1`, `Zuoyou Jiang`, or `FinStep-AI`. This record is materially distinct from existing multi-agent, formulaic alpha generation, or direct LLM sentiment scoring strategies: rather than generating new formulas or directly scoring securities with an LLM, Alpha-R1 formalizes dynamic factor selection as a **context-conditioned sparse linear model**, using an 8B-parameter reasoning LLM fine-tuned via Group Relative Policy Optimization (GRPO) on objective financial returns to dynamically activate or deactivate pre-compiled alpha factors based on semantic alignment between factor failure modes and evolving macro/news regimes.

## Economic mechanism

### Source-reported

The authors argue that the recurring degradation of quantitative factor strategies in financial markets is driven by signal decay and macroeconomic regime shifts rather than within-regime estimation noise. In non-stationary markets, the economic environment repeatedly invalidates historical correlations. Traditional machine learning and regularized models (such as Lasso, XGBoost, A2C, or numerical PPO) rely entirely on numerical time-series correlations and lack structural understanding of why a factor works; when re-estimated on limited and noisy samples during regime transitions, they suffer from high parameter variance and overfit transient patterns.

Conversely, general-purpose large language models (such as Claude 3.7 Sonnet or DeepSeek-R1) possess strong general reasoning faculties but lack financial grounding and risk awareness, generating decisions with severe drawdowns. Furthermore, existing LLM applications in quantitative finance focus largely on factor generation (mining formulas) rather than the sequential decision-making needed for factor screening.

Alpha-R1 addresses this gap by decoupling factor evaluation into:
1. An objective, low-variance linear pricing engine with fixed historical weights;
2. A context-aware semantic gating core (Qwen3-8B aligned via GRPO) that reasons over qualitative news narratives, price trends, and pre-compiled factor mechanism profiles to selectively activate factors whose economic logic matches prevailing market conditions.

### Research interpretation

The hypothesized mechanism is **semantic regime-conditional factor gating**. Under this thesis, factor efficacy is state-dependent, and the dominant source of empirical portfolio degradation is model misspecification across macro regimes rather than precision error in linear coefficients. By holding the linear score mapping fixed and treating the LLM as an inductive, semantic gating network $z_t \in \{0, 1\}^K$, the strategy avoids the catastrophic variance associated with frequent numerical covariance matrix or coefficient re-estimation.

Qualitative market news and macroeconomic announcements serve as leading regime indicators that precede purely backward-looking price momentum. When the reasoning core detects contextual inconsistency between a factor's known failure conditions (e.g., high-volatility liquidity shocks or speculative sector rotations) and current market narratives, it deactivates that factor, preserving portfolio capital and suppressing drawdown.

## Signal

### Source-reported construction

The strategy operates on a dynamic candidate pool $\mathcal{U}$ of $K=82$ computationally feasible formulaic factors selected from the Alpha101 library (Kakushadze, 2016).

1. **Pre-training and Historical Memory Phase (2020.01.01 – 2023.12.31):**
   - A multi-factor linear baseline is fitted across the historical window to determine fixed regression coefficients $\{\beta_i\}_{i=1}^K$ and intercept $\beta_0$.
   - Weekly market summaries $M_w = F_{\text{LLM}}(I_w \oplus M_{w-1})$ aggregate atomic price descriptions $S_t^{\text{price}}$ (technical indicators, trading volume, sector rotation) and news descriptions $S_t^{\text{news}}$ (financial news, macro announcements) into a global market memory $M_{\text{global}}$.
   - For each factor $i \in \mathcal{U}$, backtesting yields a quantitative performance vector $P_i$ (returns, volatility, decay profile). An LLM synthesizes $M_{\text{global}}$ and $P_i$ into a structured factor semantic profile $\alpha_{\text{des}, i} = F_{\text{LLM}}(M_{\text{global}}, P_i)$, articulating its economic rationale, regime suitability, and known failure conditions.

2. **Daily Decision State ($t$):**
   - Synthesize contemporaneous market state:
     $$S_t = F_{\text{LLM}}(S_t^{\text{price}}, S_t^{\text{news}})$$
   - Construct decision context:
     $$C_t = \{\alpha_{\text{des}, i}\}_{i \in \mathcal{U}} \oplus S_t$$
   - The Alpha-R1 model (Qwen3-8B fine-tuned via GRPO) processes $C_t$ deterministically ($\text{temperature} = 0$, $\text{top\_p} = 0.7$) to generate the active factor subset $\mathcal{A}_t \subseteq \mathcal{U}$.

3. **Stock Ranking and Scoring:**
   - For each stock $s$, predicted return is calculated using only factors in active subset $\mathcal{A}_t$:
     $$\text{Return}_{\text{predicted}}(s) = \beta_0 + \sum_{i \in \mathcal{A}_t} \left(\beta_i \times V_{i, s, t-1}\right)$$
     where $V_{i, s, t-1}$ is the standardized previous-day value of factor $i$ for stock $s$, and unselected factors contribute zero.
   - All eligible stocks in the universe are ranked in descending order of $\text{Return}_{\text{predicted}}$.
   - The Top $N = 10$ stocks are selected to form an equal-weighted target basket.

4. **Reinforcement Learning Alignment (GRPO):**
   - Training sample generation: On each date in 2024.07.01 – 2024.12.31, generate 300 samples with a randomly selected 40-factor subset from the 82-factor zoo to prevent formula memorization.
   - Objective:
     $$R_{\text{final}} = R_{\text{adjusted}} - P_{\text{structural}}$$
     where base reward is the holding period $H=5$ excess return over benchmark:
     $$R_{\text{base}} = \left(\text{Return}_{\text{port}}(\mathcal{A}_t, H) - \text{Return}_{\text{bench}}(H)\right) \times 100$$
   - LLM-as-judge consistency penalty: Claude 3.5 Haiku evaluates the reasoning trace against selected factors $\mathcal{A}_t$ and context $C_t$ to produce $P_{\text{consistency}} \in [0, 10]$, normalized to $P_{\text{norm}} = P_{\text{consistency}} / 10.0$.
     $$R_{\text{adjusted}} = \begin{cases} R_{\text{base}} \times (1 - P_{\text{norm}}) & \text{if } R_{\text{base}} > 0 \\ R_{\text{base}} \times (1 + P_{\text{norm}}) & \text{if } R_{\text{base}} \leq 0 \end{cases}$$
   - Structural penalty $P_{\text{structural}}$ enforces factor parsimony and heavily penalizes unparsable or hallucinated factor identifiers.
   - Updates policy via Group Relative Policy Optimization across group size $G$ with advantage clipping and KL penalty $\beta$ against reference model $\pi_{\text{ref}}$.

5. **Slot Rotation Portfolio Execution:**
   - Capital $C$ is partitioned into $H = 5$ independent sub-portfolios (slots).
   - On day $t$, only slot $k = t \pmod H$ is rebalanced to the newly selected Top 10 stocks:
     $$P_{t, k} = \text{Rebalance}(P_{t-1, k}, \mathcal{A}_t)$$
   - The remaining $H - 1 = 4$ slots remain passive, capping daily turnover at $1/H = 20\%$ of total capital.

### Research-proposed operationalization

For testing or independent reconstruction without requiring closed-source judge LLM APIs:
- Freeze the pre-trained linear weights $\beta_i$ on a fixed historical rolling window.
- Replace the LLM-as-judge consistency penalty $P_{\text{consistency}}$ with a deterministic rule-based penalty checking format validity and factor existence in the active zoo.
- Rebalance daily at market open following slot rotation $k = t \pmod 5$.

## Required data

- **Universe:** Chinese A-shares (CSI 300 for large-cap in-domain; CSI 1000 for small-cap out-of-domain evaluation).
- **Timeframe:** Daily OHLCV bars for factor calculations and portfolio accounting; 1-minute intraday bars (09:31–10:00) for VWAP execution pricing.
- **Factor inputs:** 82 Alpha101 formulaic alpha indicators computed strictly on point-in-time daily market data.
- **Unstructured textual data:** Daily financial news feeds, corporate announcements, and macroeconomic reports.
- **Trading constraints data:** Daily limit-up and limit-down price boundaries; initial IPO listing date flags.
- **Point-in-time conventions:** Factor values $V_{i, s, t-1}$ strictly use close data from day $t-1$. Daily news and price descriptions must be available prior to 09:30 on day $t$. Pre-training linear coefficients $\beta_i$ are frozen prior to the training/testing periods.
- **Missing data handling:** Stocks suspended from trading or lacking full factor history are excluded from daily ranking.

## Execution assumptions

- **Execution price model:** Volume-Weighted Average Price (VWAP) computed over the first 30 minutes of the continuous trading session (09:31–10:00):
  $$\hat{P}_{s, t} = \frac{\sum_{i=1}^{30} \left(\text{Price}_{s, t, i} \times \text{Volume}_{s, t, i}\right)}{\sum_{i=1}^{30} \text{Volume}_{s, t, i}}$$
- **Transaction fees:** 0.10% (10 bps) bilateral cost applied to both purchases and sales (accounting for exchange fees, stamp duty, and slippage).
- **Market trading limits:**
  - Buy orders are rejected if the stock reaches its upper limit-move (Limit-Up) during the 30-minute execution window.
  - Sell orders are deferred if the stock is locked at its lower limit-move (Limit-Down).
  - Stocks on their IPO initial listing day are strictly excluded from trading.
- **Capacity / Turnover:** Daily rebalancing is restricted to $1/5$ of total capital via slot rotation, reducing execution churn and mitigating market impact.

## Evidence

### Source-reported

The source reports backtest results averaged over five independent runs across the test period 2025.01.01 to 2025.06.30 under 10 bps bilateral transaction costs:

#### In-Domain Performance: CSI 300 Universe (Table 1)
- **Alpha-R1 (Ours):** Cumulative Return (CR) **12.99%**, Annualized Return (AR) **27.59%**, Sharpe Ratio (SR) **1.62**, Maximum Drawdown (MDD) **6.76%**.
- **Buy & Hold (CSI 300 Index):** CR **3.03%**, AR **6.70%**, SR **0.33**, MDD **10.49%**.
- **PCA:** CR **-0.48%**, AR **0.40%**, SR **-0.06**, MDD **14.69%**.
- **XGBoost:** CR **-10.03%**, AR **-21.65%**, SR **-1.54**, MDD **15.33%**.
- **LightGBM:** CR **-5.10%**, AR **-10.26%**, SR **-0.83**, MDD **13.43%**.
- **A2C (Advantage Actor-Critic):** CR **-5.52%**, AR **-11.12%**, SR **-0.85**, MDD **11.22%**.
- **PPO (Proximal Policy Optimization):** CR **0.89%**, AR **3.28%**, SR **0.11**, MDD **11.67%**.
- **Gemini 2.5 Pro Thinking:** CR **-7.04%**, AR **-14.45%**, SR **-1.01**, MDD **15.08%**.
- **Claude 3.7 Sonnet Thinking:** CR **-5.41%**, AR **-10.23%**, SR **-0.63**, MDD **13.58%**.
- **DeepSeek-R1:** CR **-5.98%**, AR **-11.93%**, SR **-0.82**, MDD **14.88%**.
- **Qwen3-8B (Unaligned Base):** CR **-6.32%**, AR **-12.41%**, SR **-0.77**, MDD **16.35%**.

#### Out-of-Domain Zero-Shot Performance: CSI 1000 Universe (Table 1)
- **Alpha-R1 (Ours):** CR **42.49%**, AR **78.18%**, SR **4.03**, MDD **9.25%**.
- **Buy & Hold (CSI 1000 Index):** CR **9.64%**, AR **22.14%**, SR **0.80**, MDD **16.87%**.
- **PCA:** CR **6.24%**, AR **16.09%**, SR **0.59**, MDD **16.13%**.
- **XGBoost:** CR **4.34%**, AR **11.77%**, SR **0.45**, MDD **19.12%**.
- **LightGBM:** CR **-5.37%**, AR **-6.92%**, SR **-0.26**, MDD **23.88%**.
- **A2C:** CR **11.80%**, AR **26.30%**, SR **1.15**, MDD **14.00%**.
- **PPO:** CR **-6.44%**, AR **-7.62%**, SR **-0.25**, MDD **29.31%**.
- **Gemini 2.5 Pro Thinking:** CR **-8.73%**, AR **-15.38%**, SR **-0.58**, MDD **28.37%**.
- **Claude 3.7 Sonnet Thinking:** CR **3.80%**, AR **13.26%**, SR **0.43**, MDD **16.98%**.
- **DeepSeek-R1:** CR **-7.58%**, AR **-12.87%**, SR **-0.50**, MDD **27.89%**.
- **Qwen3-8B:** CR **2.73%**, AR **10.23%**, SR **0.29**, MDD **21.78%**.

#### Ablation Analysis on CSI 300 (Table 2)
- **Alpha-R1 (Full):** CR **12.99%**, AR **27.59%**, SR **1.62**, MDD **6.76%**.
- **w/o Market Price:** CR **10.24%**, AR **22.42%**, SR **1.24**, MDD **12.87%**.
- **w/o News:** CR **8.75%**, AR **19.61%**, SR **1.03**, MDD **12.01%**.
- **w/o Semantic Description (raw math formulas):** CR **7.26%**, AR **16.76%**, SR **0.83**, MDD **13.32%**.
- **w/o RL Optimization (unaligned Qwen3-8B):** CR **-6.32%**, AR **-12.41%**, SR **-0.77**, MDD **16.35%**.

#### Gating Baseline Comparison on CSI 300 (Table 3)
- **Alpha-R1 (Semantic Gating):** CR **12.99%**, AR **27.59%**, SR **1.62**, MDD **6.76%**.
- **Lasso (Sparse L1 selection):** CR **1.58%**, AR **4.63%**, SR **0.20**, MDD **11.12%**.
- **IC Momentum (Top 10 by 20-day average IC):** CR **-6.33%**, AR **-12.55%**, SR **-0.80**, MDD **13.29%**.

All reported figures are third-party claims from the primary source paper and have not been independently reproduced.

### Independently reproduced

not independently reproduced

### Negative evidence

- Unaligned general reasoning LLMs (DeepSeek-R1, Claude 3.7 Sonnet Thinking, Gemini 2.5 Pro Thinking, and unaligned Qwen3-8B) all failed to generate positive excess returns on the CSI 300 in-domain test, generating negative Sharpe ratios (-0.63 to -1.01) and maximum drawdowns between 13.58% and 15.08%. General reasoning ability does not automatically translate into profitable quantitative execution without domain-specific RL alignment.
- Classical machine learning (XGBoost, LightGBM) and numerical reinforcement learning (A2C, PPO) suffered severe negative performance on CSI 300, confirming that naive correlation fitting deteriorates during non-stationary regime transitions.
- The evaluation test period is relatively short: 6 calendar months (January 1, 2025 to June 30, 2025).
- The public GitHub repository (`FinStep-AI/Alpha-R1` commit `61feaa359bd57761f5ac58f75af46ddfed2d2d7b`) currently hosts only the documentation and roadmap; the training and inference pipelines are marked as "Coming Soon", leaving replication dependent on the paper text description.

## Falsification plan

1. **Permuted Context & Placebo Test:**
   - Shuffle daily news narratives $S_t^{\text{news}}$ and factor semantic descriptions $\alpha_{\text{des}, i}$ across random days while preserving factor values and linear weights.
   - *Falsification threshold:* If Alpha-R1 with shuffled context matches or exceeds the risk-adjusted performance of the aligned model, reject the hypothesis that semantic reasoning over macro context provides genuine gating alpha.

2. **Static Gating & Random Subset Control:**
   - Compare Alpha-R1's dynamic active subsets $\mathcal{A}_t$ against $M = 1,000$ static or randomly chosen factor subsets of equal size with the same fixed linear weights $\beta_i$.
   - *Falsification threshold:* If the average Sharpe ratio of random factor subsets lies within 1 standard deviation of Alpha-R1, reject the claim of intelligent semantic screening.

3. **Multi-Year Out-of-Sample Horizon Test:**
   - Extend the out-of-sample evaluation window through all of 2025 and into 2026 without updating model weights or prompting templates.
   - *Falsification threshold:* If annualized Sharpe ratio drops below zero over a full 12-month holdout, classify the reported 6-month gain as regime-dependent backtest selection.

4. **Transaction Cost and Delay Stress Test:**
   - Increase bilateral transaction costs from 10 bps to 20 bps and 30 bps, and introduce a 1-day execution lag (trading at $t+1$ VWAP rather than same-day 09:31 VWAP).
   - *Falsification threshold:* If excess returns disappear at 20 bps or under a 1-day execution lag, reject tradability and classify the signal as an execution-sensitive artifact.

5. **Token Leakage and Publication Timing Audit:**
   - Audit all textual news sources to confirm timestamps strictly precede 09:30 CST on day $t$.
   - *Falsification threshold:* Any inclusion of articles published after market open or retroactively edited headlines invalidates the reported out-of-sample results.

6. **Judge LLM Replacement Test:**
   - Replace Claude 3.5 Haiku with a completely objective, non-LLM structural constraint during GRPO training.
   - *Falsification threshold:* If removing the LLM-as-judge produces equivalent policy performance, reject the necessity of LLM reasoning consistency rewards.

7. **Cross-Market Geographic Transfer:**
   - Evaluate the trained Alpha-R1 gating model on US equities (S&P 500 / Russell 2000) using US financial news.
   - *Falsification threshold:* If the model cannot outperform naive equal-weighted factor combination on US markets, reject generalizability across market institutional structures.

## Crypto portability

**unproven**

The primary paper evaluates exclusively Chinese A-share equity universes (CSI 300 and CSI 1000). The underlying mechanism—semantic gating of alpha factors conditioned on qualitative news narratives and macro regime shifts—is ported to crypto purely as a research interpretation and has not been demonstrated empirically in the cited source.

Key cryptocurrency portability challenges include:
- **Factor zoo mismatch:** The Alpha101 library is constructed around traditional equity exchange conventions (trading sessions, auction opens/closes, corporate actions). Crypto alpha factors are predominantly driven by continuous perpetual funding rates, order flow imbalance, liquidation clusters, cross-venue basis, and on-chain liquidity dynamics.
- **Unstructured text noise:** Crypto market narratives are heavily dispersed across social channels (Twitter/X, Telegram, Discord, governance forums) with high adversarial noise, sybil attacks, and bot activity, unlike regulated corporate announcements and macroeconomic releases.
- **24/7 continuous trading:** Equities have distinct overnight sessions and morning auction opens allowing discrete daily LLM inference; crypto trading is continuous, making daily slot rotation at 09:30 arbitrary.
- **Execution and derivative mechanics:** Crypto trading is dominated by perpetual futures with variable funding rates, margin liquidations, and exchange counterparty fragmentation, which are absent from the equity VWAP execution model.

## Limitations

- **underspecified:** Exact preprocessing pipelines, news API sources, prompt templates for $F_{\text{LLM}}$, and filtering thresholds for news articles are not fully specified in the paper text.
- **provenance gap:** The official GitHub repository (`FinStep-AI/Alpha-R1`) does not yet include the full source code or open-weight checkpoints for the GRPO-trained model.
- **short test window:** The reported out-of-sample empirical evaluation spans only 6 months (2025.01.01 to 2025.06.30).
- **computational cost:** Daily inference with an 8B-parameter LLM over high-dimensional multi-modal contexts incurs non-trivial operational latency and compute overhead.
- **single-asset-class evidence:** Tested only on Chinese A-share equities.
- **not independently reproduced**.

## Implementation status

No implementation in PyBroker, NautilusTrader, Paper, Testnet, or Live has been created or authorized from this record.

`implementation_status: not-implemented`

## Adoption boundary

This record is research material only. It does not establish profitable alpha, does not authorize implementation, and does not authorize Paper, Testnet, or Live trading.

All quantitative metrics and claims are source-reported. Any operational thresholds, falsification criteria, or crypto adaptations proposed herein are research interpretations and do not imply strategy approval.

## Related Wiki records

- `[[quant/alpha-combination-breadth-executable-bridge-2026-08-28]]`
- `[[quant/alpha-transforms-decay-neutralization-2026-08-28]]`
- `[[quant/backtest-overfitting-pbo-cscv-2026-08-27]]`
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`
- `[[quant/alphazerobeta-recurrent-ppo-market-neutral-portfolio-2026-09-02]]`
- `[[quant/crypto-cross-sectional-factor-zoo-iterative-alpha-compression-2026-09-01]]`

Related records in `alpha-strategy-research`:
- `tradingmoe-query-key-sparse-expert-routing-llm-trading-2026-09-03.md`
- `finsmart-market-aligned-reinforcement-learning-sentiment-alpha-2026-09-02.md`
- `retrieval-augmented-llm-expert-switching-portfolio-management-2026-09-03.md`

## Sources

1. Zuoyou Jiang, Li Zhao, Rui Sun, Ruohan Sun, Zhongjian Li, Jing Li, Daxin Jiang, Zuo Bai, and Cheng Hua, *Alpha-R1: Alpha Screening with LLM Reasoning via Reinforcement Learning*, arXiv preprint arXiv:2512.23515v1 [q-fin.PM, cs.AI, cs.LG], submitted December 29, 2025. Stable URL: https://arxiv.org/abs/2512.23515. DOI: https://doi.org/10.48550/arXiv.2512.23515. Full-text HTML: https://arxiv.org/html/2512.23515v1.
2. FinStep-AI, *Alpha-R1: Alpha Screening with LLM Reasoning via Reinforcement Learning* [GitHub Repository], commit SHA `61feaa359bd57761f5ac58f75af46ddfed2d2d7b`, December 30, 2025. URL: https://github.com/FinStep-AI/Alpha-R1.
3. Z. Kakushadze, *101 Formulaic Alphas*, Wilmott 2016 (84), pp. 72–81, 2016. DOI: https://doi.org/10.1002/wilm.10526.
