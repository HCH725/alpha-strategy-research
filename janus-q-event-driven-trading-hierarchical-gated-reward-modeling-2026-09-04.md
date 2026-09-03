---
schema: strategy-research-record-v1
title: "Janus-Q: End-to-End Event-Driven Trading via Hierarchical-Gated Reward Modeling"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - event-driven
  - llm-reasoning
  - reinforcement-learning
  - grpo
  - cumulative-abnormal-return
  - chinese-a-shares
  - barra-cne5
status: research-only
confidence: medium
source_as_of: 2026-02-27
sources:
  - "https://arxiv.org/abs/2602.19919"
  - "https://arxiv.org/html/2602.19919v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Janus-Q: End-to-End Event-Driven Trading via Hierarchical-Gated Reward Modeling

## Provenance

- **Paper Title:** *Janus-Q: End-to-End Event-Driven Trading via Hierarchical-Gated Reward Modeling*
- **Authors:** Xiang Li (The Hong Kong University of Science and Technology (Guangzhou) [HKUST-GZ], equal contribution), Zikai Wei (International Digital Economy Academy [IDEA], Shenzhen, equal contribution), Yiyan Qi (IDEA, Shenzhen), Wanyun Zhou (HKUST-GZ), Xiang Liu (HKUST-GZ), Penglei Sun (HKUST-GZ), Yongqi Zhang (HKUST-GZ, corresponding author), and Xiaowen Chu (HKUST-GZ)
- **Canonical Identifier:** arXiv:2602.19919v1 `[cs.AI, q-fin.TR, q-fin.ST]`
- **Submission Date:** 27 February 2026
- **Canonical URLs:** Abstract: `https://arxiv.org/abs/2602.19919` | HTML full text: `https://arxiv.org/html/2602.19919v1` | DOI: `https://doi.org/10.48550/arXiv.2602.19919`
- **Data Period:** 1 January 2023 to 25 January 2025 (news textual corpus) / 6 February 2025 (price data). Chronologically split into Historical Estimation (2023/01/01 – 2023/10/24), Training (2023/10/25 – 2024/08/27), Validation (2024/08/28 – 2024/11/11), and Test (2024/11/12 – 2025/01/25).
- **Target Universe:** 5,282 Chinese A-share common stocks spanning large-, mid-, and small-cap segments (evaluated relative to CSI 300, CSI 500, and CSI 1000 indices).
- **Dataset Scale:** 62,400 financial news event instances manually annotated by a panel of six domain professionals across 10 fine-grained event types, paired with market-adjusted, Barra CNE5 factor-neutralized Cumulative Abnormal Returns (CAR).

## Economic mechanism

### Source-reported

The authors argue that real financial asset price movements are rarely driven by smooth temporal dynamics alone; instead, they are frequently precipitated by discrete, interpretable events (e.g., earnings announcements, mergers and acquisitions, risk warnings, regulatory violations, financing events) that abruptly shift investor expectations and asset valuations. Different event types induce highly heterogeneous market responses in direction, magnitude, and persistence. Treating such structurally distinct events as homogeneous numerical inputs or passive textual embeddings obscures their economic meaning.

Existing quantitative LLM systems suffer from two primary limitations:
1. **Lack of Event-Market Granularity:** Datasets typically provide coarse sentiment without isolating statistically grounded, factor-neutralized abnormal price reactions (CAR). Raw price changes conflate broader market beta and industry/style factor movements with idiosyncratic event shocks.
2. **Misalignment Between Semantic Reasoning and Realized Market Outcomes:** Purely supervised models capture superficial text-price correlations, while standard reinforcement learning models use linear additive rewards where competing objectives offset each other, leading to reward hacking and spurious policies.

Janus-Q resolves this by establishing an end-to-end framework where news events are treated as primary decision units. First, event impacts are quantified using factor-neutralized CAR derived from a Barra CNE5 risk model. Second, decision-oriented training aligns reasoning via Supervised Fine-Tuning (SFT) and Group Relative Policy Optimization (GRPO) governed by a Hierarchical-Gated Reward Model (HGRM). HGRM enforces a hard direction gate (blocking rewards if directional alignment is negative), a soft event-type consistency gate (discounting payoffs when event taxonomy is misidentified), a cost-aware PnL reward with strength regularization, and magnitude shaping.

### Research interpretation

The underlying thesis is **idiosyncratic abnormal drift driven by information processing frictions around corporate disclosure events**. In complex equity markets with thousands of constituents, the arrival of discrete textual information requires interpretation of regulatory, legal, and operational nuances. Because retail and institutional capital digest disclosures at varying speeds, prices do not adjust instantaneously to full efficiency; rather, an idiosyncratic drift occurs over a short post-event horizon (1 to 2 trading days).

Crucially, raw returns are noisy and dominated by macroeconomic shifts and style premia. By explicitly subtracting the market model return and neutralizing the five major Barra CNE5 style factors (Size, Liquidity, Volatility, Momentum, Reversal) as well as industry exposures, the signal targets pure residual idiosyncratic mispricing.

The hierarchical gating structure serves as an inductive economic regularizer: by disallowing rewards whenever the direction sign is incorrect ($g_{\text{dir}} = 0$), the model cannot earn positive reinforcement from lucky fills that contradict its reasoning. Similarly, discounting payoffs when the event type is misclassified prevents the model from mapping spurious narrative noise into profitable trades.

## Signal

### Signal formation timestamp

News articles published between market open on day $t$ (09:30 China Standard Time, CST) and market open on day $t+1$ (09:30 CST) are processed overnight. The directional trading signal $\gamma_{s,t} \in \{\text{Long}, \text{Short}, \text{Hold}\}$ for each stock $s$ is fully formed before 09:30 CST on day $t+1$.

### Lookback

- **Estimation window ($\\mathcal{T}_{\\text{est}} = (T_0, T_1]$):** Precedes the event timestamp $t_0$, used to calibrate the OLS market model $r_{i,t} = \alpha_i + \beta_i r_{m(i),t} + \epsilon_{i,t}$ on historical event-free days, where $m(i)$ is the benchmark index corresponding to the market-cap tier (CSI 300, 500, or 1000). A buffer lag between $T_1$ and $t_0$ is enforced to prevent pre-event information leakage.
- **Event window ($\\mathcal{T}_{\\text{evt}} = (T_1, T_2]$):** Spans the abnormal return observation window around the event, over which factor neutralization and cumulative abnormal returns $\\text{CAR}_{i} = \\sum_{t \\in \\mathcal{T}_{\\text{evt}}} \\text{AR}_{i,t}^{\\text{RM}}$ are measured.
- **Event weight rolling window:** Event-type magnitude weights $w_k$ are re-estimated over rolling historical windows to adapt to evolving market regimes.

### Long entry

When the aggregated stock-level signal $\gamma_{s,t}$ indicates `Long`:
- Order placed at the market opening price $o_{s,t+1}$ on day $t+1$.
- Capital is allocated based on event-type weight $w_k$ (proportional to rolling historical mean absolute CAR of event type $k$), evenly split across qualifying stocks within each event category.

### Short entry

When the aggregated stock-level signal $\gamma_{s,t}$ indicates `Short`:
- Initiated at the market opening price $o_{s,t+1}$ on day $t+1$.
- (Note: The paper evaluates a theoretical symmetric long-short portfolio; real-world short execution in China A-shares faces severe stock borrow constraints).

### Exit / holding period

- **Default holding period:** Fixed 2-day holding period ($\tau(t) = t+2$).
- **Exit rule:** Liquidated at the official market closing price $c_{s,\tau(t)}$ on day $t+2$.
- **Holding period sensitivity:** Evaluated across horizons from 1 to 10 trading days. Peak performance is attained at a 1-day holding period (Total Return 0.122, Sharpe Ratio 1.8074); performance decays smoothly but remains positive up to 9 days, retaining Sharpe Ratio 0.398 at 10 days.

### Parameters

- **Event categories ($\\mathcal{E}$, 10 types):** Personal behavior, equity change, asset change, dividend, risk warning, financing, financial status, violation, industry, rating adjustment.
- **Direction classification:** $d = \text{sign}(c) \in \{\text{positive}, \text{negative}, \text{neutral}\}$.
- **Trading strength threshold ($\\tau$):** Fixed CAR magnitude cutoff determining $s \in \{\text{strong}, \text{weak}\}$.
- **Hard direction gate penalty ($\\lambda_{\\text{dir}}$):** $\lambda_{\text{dir}} > 1$, enforcing $g_{\text{dir}} = 0$ if directional alignment $s_{\text{dir}} < 0$.
- **Soft event gate parameters:** Penalty $\lambda_{\text{evt}} > 0$, missing penalty $\lambda_{\text{miss}} > 0$, discount factor $\alpha \in (0, 1)$ yielding multiplier $m_{\text{evt}}$.
- **PnL reward clipping ($\\rho$):** Symmetrically clips trade payoffs to $[-\rho, \rho]$.
- **Magnitude tolerance ($\\sigma$):** Controls the scale in Gaussian magnitude reward $r_{\text{mag}} = \exp(-(\hat{c} - c)^2 / 2\sigma^2)$.
- **Position ratio limit ($k\\times$):** Main experiment uses unconstrained exposure ($\infty$); parameter sweeps test $1\times, 2\times, 3\times$ NAV limits.
- **SFT training parameters:** LoRA rank $r=8$, LoRA alpha $\alpha=16$, LoRA dropout 0.1, max sequence length 1,400, AdamW optimizer ($\beta_1=0.9, \beta_2=0.999$, weight decay 0.01), learning rate $5 \times 10^{-6}$, warmup ratio 0.2, precision BF16, effective batch size $8 \times 4 \times N_{\text{GPU}}$ on $8 \times$ NVIDIA A100 (40GB).
- **GRPO training parameters:** Learning rate $\in \{1 \times 10^{-6}, 2 \times 10^{-6}, 5 \times 10^{-6}\}$, max grad norm $\in \{0.5, 1.0\}$, samples per prompt $\in \{2, 4, 8\}$, initial KL coefficient $\in \{0.05, 0.1, 0.2\}$, target KL $\in \{0.01, 0.02\}$, clip range $\in \{0.1, 0.2\}$, max prompt length $\in \{3000, 4196\}$, max response length $\in \{4196, 8192\}$.

### Position sizing

Type-weighted portfolio allocation: daily capital is distributed across event types according to their empirical historical impact magnitude $w_k = \frac{1}{|D_k|} \sum_{i \in D_k} |c_i|$. Capital assigned to each event type is divided equally among constituent stocks. Empirical historical magnitudes show:
- Risk warnings: mean absolute CAR $> 0.05$ (highest weight)
- Violations: mean absolute CAR $> 0.03$
- Routine corporate disclosures (Personal Behavior, Rating Adjustment): mean absolute CAR $< 0.02$ (lowest weight)

### Fully specified vs underspecified

- **Fully specified:** Mathematical reward formulas (hard gate, soft gate, cost-aware PnL, magnitude shaping), Barra CNE5 factor neutralization list, event taxonomy (10 categories), chronological splits, entry/exit bar timings (open on $t+1$, close on $t+2$), and SFT/GRPO hyperparameter grids.
- **Underspecified:**
  - The exact foundation base model checkpoint fine-tuned for Janus-Q is not explicitly stated by name in the text (provenance gap; Qwen2.5-7B is evaluated as a baseline and the LoRA CAUSAL_LM configuration indicates a standard 7B-class open-weights architecture).
  - Exact numerical values of thresholds $\tau, \lambda_{\text{dir}}, \lambda_{\text{evt}}, \lambda_{\text{miss}}, \kappa, \rho, \sigma$ are described via parameter bounds and equations rather than a single frozen scalar table.

## Required data

- **Instrument:** Chinese A-share ordinary common equities.
- **Universe:** 5,282 listed A-share equities across Shanghai and Shenzhen exchanges.
- **Benchmark Indices:** CSI 300 (large-cap), CSI 500 (mid-cap), and CSI 1000 (small-cap).
- **Timeframe:** Daily OHLCV pricing bars and discrete intraday publication timestamps for textual news releases.
- **Fields:**
  - Daily open ($o_{s,t}$) and close ($c_{s,t}$) prices from Tushare.
  - Raw financial news text and publication timestamps ($t_0$) from Datayes.
  - Corporate background profiles (industry classifications, market share) from Wind.
  - Multi-factor risk exposures: Barra CNE5 style factors (Size, Liquidity, Volatility, Momentum, Reversal) and industry classification vectors.
- **Point-in-time constraints:** Strict chronological partitioning (Train: 2023/10/25–2024/08/27; Val: 2024/08/28–2024/11/11; Test: 2024/11/12–2025/01/25). No look-ahead: signals for day $t+1$ incorporate only news published prior to 09:30 CST on day $t+1$.
- **Timestamp & Timezone:** China Standard Time (UTC+8). Exchange trading hours: morning open at 09:30 CST, afternoon close at 15:00 CST.
- **Missing data handling:** Unlisted, suspended, or limit-locked stocks that cannot be traded at open/close are omitted from execution. Imputation of returns is prohibited.

## Execution assumptions

- **Execution Timing:** Next-bar open execution. News arriving between $t$ 09:30 and $t+1$ 09:30 is executed at the market opening auction price $o_{s,t+1}$ on day $t+1$.
- **Exit Timing:** Market close auction on day $t+2$ ($c_{s, t+2}$).
- **Order Types:** Opening and closing auction market orders.
- **Fill Model:** Full execution assumed at published open/close bar prices.
- **Transaction Costs:** Cost-aware formulation in reward function incorporates transaction fee parameter $\kappa$.
- **Shorting Availability:** The study models an idealized long-short portfolio. In real Chinese A-share markets, short-selling via margin lending (融券) is heavily restricted, illiquid for small-cap names, and subject to borrow costs (~7–9% annualized) and regulatory curbs.

## Evidence

### Source-reported

All performance figures, metrics, and comparisons below are directly extracted from Li et al. (arXiv:2602.19919v1, Section 4, Tables 2, 3, 4, and Appendix A.4):

#### Out-of-Sample Test Performance (2024/11/12 – 2025/01/25, Table 2)

| Category | Model / Index | MAE ↓ | RMSE ↓ | Direction Acc (DA) ↑ | Event Type Acc (ETA) ↑ | Sharpe Ratio (SR) ↑ | Max Drawdown (MDD) ↓ |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Market Indices** | CSI 300 | – | – | – | – | -1.8027 | 0.0945 (9.45%) |
| | CSI 500 | – | – | – | – | -1.6074 | 0.1423 (14.23%) |
| | CSI 1000 | – | – | – | – | -0.1036 | 0.1456 (14.56%) |
| **Time-aware LLM** | Time-MQA | 0.0427 | 0.2651 | 0.4732 | 0.5958 | -4.2184 | 0.1589 (15.89%) |
| | ChatTS-14B | 0.0932 | 0.3271 | 0.4995 | 0.6223 | -4.2827 | 0.1675 (16.75%) |
| | TimeMaster | 0.0472 | 0.1015 | 0.4472 | 0.6263 | -5.9237 | 0.1981 (19.81%) |
| **Financial LLM** | Stock-Chain | 0.1352 | 0.3226 | 0.4510 | 0.4364 | -5.3581 | 0.1800 (18.00%) |
| | FinMA | 0.0947 | 0.2531 | 0.4550 | 0.5714 | -6.9668 | 0.2358 (23.58%) |
| | DISC-FinLLM | 0.0707 | 0.1672 | 0.4286 | 0.5608 | -4.6307 | 0.2139 (21.39%) |
| **Vanilla LLM** | QwQ-32B | 0.0437 | 0.0839 | 0.4674 | 0.7080 | 0.6481 | 0.0979 (9.79%) |
| | Claude-3-Haiku | 0.0384 | 0.0557 | 0.4547 | 0.4884 | -5.4698 | 0.1395 (13.95%) |
| | GPT-4o-mini | 0.0387 | 0.0558 | 0.4700 | 0.7508 | -3.8759 | 0.1060 (10.60%) |
| | DeepSeek-v3.1-nex-n1 | 0.0541 | 0.1214 | 0.4365 | 0.6811 | 0.3710 | 0.1300 (13.00%) |
| | Grok-3-mini-beta | 0.0369 | 0.0559 | 0.4795 | 0.5417 | -2.2698 | 0.0855 (8.55%) |
| | Qwen2.5-7B | 0.0377 | 0.0551 | 0.4114 | 0.4879 | -3.9154 | 0.1177 (11.77%) |
| | Gemini-2.5-flash | 0.0534 | 0.0730 | 0.4276 | 0.6797 | -2.0899 | 0.0805 (8.05%) |
| **Fine-tuned LLM** | **Janus-Q (Ours)** | **0.0349** | **0.0541** | **0.5869** | **0.8009** | **1.3088** | **0.1196 (11.96%)** |

Janus-Q achieves a Sharpe Ratio of 1.3088, outperforming the runner-up QwQ-32B (SR 0.6481) by +102.0% relative improvement, while increasing direction accuracy to 58.69% (versus 41.1%–49.9% for all competing baselines).

#### Structural Component Ablation Study (Table 3)

| Variant | MAE ↓ | DA ↑ | ETA ↑ | Sharpe Ratio (SR) ↑ |
| :--- | :---: | :---: | :---: | :---: |
| w/o CAR Supervision | 0.0387 | 0.5261 | 0.7796 | 0.8690 |
| w/o Company Info (Wind Profile) | 0.0353 | 0.5464 | 0.7790 | 0.9608 |
| **w/o Supervised Fine-Tuning (SFT)** | **0.0381** | **0.4429** | **0.6771** | **-5.2848** |
| w/o GRPO Reinforcement Tuning | 0.0355 | 0.5459 | 0.7881 | 1.1330 |
| **Janus-Q (Full)** | **0.0349** | **0.5869** | **0.8009** | **1.3088** |

*Crucial finding:* Eliminating SFT causes complete strategy collapse (SR drops from +1.3088 to -5.2848, DA falls by 14.4%), demonstrating that policy optimization cannot operate directly on raw unaligned foundation models without first structuring event reasoning.

#### Hierarchical Reward Objective Ablation (Table 4)

| Variant | MAE ↓ | DA ↑ | ETA ↑ | Sharpe Ratio (SR) ↑ |
| :--- | :---: | :---: | :---: | :---: |
| w/o Event Type Gate | 0.0345 | 0.5819 | 0.7817 | 1.2107 |
| w/o Direction Gate ($g_{\text{dir}}$) | 0.0357 | 0.5589 | 0.7896 | 1.2788 |
| w/o Magnitude Shaping | 0.0347 | 0.5653 | 0.7843 | 1.1558 |
| w/o PnL Objective | 0.0354 | 0.5799 | 0.7868 | 1.1953 |
| **HGRM (Full)** | **0.0349** | **0.5869** | **0.8009** | **1.3088** |

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Domain-Specific FinLLM Failure:** Existing financial domain-specific open-source models (FinMA, DISC-FinLLM, Stock-Chain) experienced severe underperformance, posting deeply negative Sharpe ratios (-4.63 to -6.97) and drawdowns exceeding 18%–23%. The authors attribute this to task-domain mismatch and context-length constraints that fail on long, narrative Chinese financial news.
2. **Time-Aware Model Inefficacy:** Time-series oriented LLMs (Time-MQA, ChatTS-14B, TimeMaster) incorporating text as auxiliary features degraded to Sharpe ratios between -4.21 and -5.92, showing that treating text as an auxiliary numerical feature fails to capture event shocks.
3. **Horizon Decay and Position Accumulation:** In unconstrained backtests (Figure 9), expanding the holding horizon beyond 2–3 days caused rapid performance degradation across models (QwQ-32B turned negative by day 3 and collapsed below SR -1.5 at longer horizons). Stale overlapping event positions accumulate unmodeled market variance.
4. **Catastrophic Failure Without SFT:** RL optimization via GRPO without SFT grounding produces complete policy failure (SR -5.2848), demonstrating the vulnerability of pure reinforcement learning to reward hacking in noisy financial environments.

## Falsification plan

1. **Out-of-Sample Subperiod Walk-Forward:** Extend the test split beyond 25 January 2025 across differing Chinese market macro regimes (e.g., strong bull runs, deflationary downturns, and high-volatility sector rotations). Falsification threshold: Out-of-sample annualized Sharpe ratio falling below 0.0 or maximum drawdown exceeding 25%.
2. **Short-Selling Friction Audit:** Re-run the backtest under realistic Chinese A-share trading rules:
   - Restrict short sales to stocks in the official margin-trading eligible list (融资融券标的).
   - Impose borrow fees of 7.5% per annum and a 0.1% stamp tax on selling.
   - Alternatively, test a long-only top-decile portfolio against the CSI 500 / CSI 1000 equal-weighted benchmark. If alpha disappears after removing the short leg, the strategy is not practically tradable in China A-shares.
3. **Execution Delay / Opening Price Impact Stress:** Shift execution from the opening auction price $o_{s,t+1}$ to a volume-weighted average price (VWAP) over the first 30 minutes of trading (09:30–10:00 CST). If abnormal returns decay within the opening 15 minutes, the alpha is an opening-auction latency artifact.
4. **Placebo Shuffled-News Test:** Permute news text across non-target companies while preserving publication dates and industry classifications. If the randomized model achieves a direction accuracy statistically indistinguishable from 58.7% ($p > 0.05$), the reported edge is driven by leakage or factor confounding rather than textual interpretation.
5. **Event-Type Ablation Stress:** Restrict the universe to low-magnitude corporate news (excluding Risk Warning and Violation). Test whether the remaining event classes generate statistically significant CAR alpha.

## Crypto portability

- **Portability Status:** Adapted / Unproven.
- **Porting Rationale:** The core economic intuition—that discrete textual events drive sudden expectation shifts whose idiosyncratic impact can be extracted by an LLM—is applicable to crypto markets. However, the exact implementation is heavily non-portable without major adaptations:
  - **No Standard Daily Opening Auction:** Crypto operates 24/7/365 with continuous trading. There is no overnight accumulation window or synchronized 09:30 CST opening call auction. Signals must be generated at continuous event arrival timestamps with sub-minute execution latencies.
  - **Data Source Differences:** Chinese equity disclosures originate from regulated statutory filings (via Datayes/Wind). Crypto news events originate from fragmented sources (X/Twitter, Discord, Telegram, governance forums, GitHub commits, on-chain oracle updates, token unlock schedules).
  - **Risk Factor Model Gap:** Crypto lacks a universally accepted Barra CNE5 style factor model. Factor neutralization would require constructing an endogenous crypto multi-factor model (neutralizing BTC beta, circulating market cap, funding rate momentum, and realized volatility).
  - **Contract & Funding Considerations:** In crypto perpetual futures, shorting is frictionless and symmetric, unlike A-shares. However, funding rate payments and liquidation cascades introduce substantial non-linear holding costs.

## Limitations

- **Underspecified Base Model Checkpoint:** The authors do not state the exact pre-trained foundation model checkpoint name (e.g., Qwen2.5-7B-Instruct or similar) fine-tuned to produce Janus-Q, creating a provenance barrier for exact zero-shot replication.
- **Short Test Horizon:** The test sample spans only 2.5 months (12 November 2024 to 25 January 2025), which is too brief to confirm multi-year regime robustness or statistical significance against economic cycles.
- **Idealized A-Share Shorting:** The backtest assumes symmetric frictionless shorting across 5,282 A-share tickers, which is structurally impossible under Chinese stock loan regulations.
- **Annotation Cost & Domain Dependency:** Training required 62,400 expert-annotated event instances and proprietary commercial databases (Datayes, Wind, Tushare), posing high barriers to open-source maintenance.
- **Look-Ahead & Restatement Risk:** Corporate disclosures and earnings figures can undergo subsequent revisions; strict point-in-time publication timestamps must be guaranteed.

## Implementation status

- Frontmatter status: `not-implemented`.
- No implementation exists in our PyBroker or Nautilus research stack.
- Capturing this research does not authorize backtesting campaigns, paper trading, testnet, or live trading.

## Adoption boundary

- Frontmatter status: `research-only`.
- Adoption: `not-approved`.
- Approval scope: `research-only`.
- The presence of this record in the repository serves purely as a normalized research capture. It does not constitute verified alpha, implementation authorization, or permission to deploy capital.

## Related Wiki records

- `[[quant/alphar1-context-aware-alpha-screening-llm-reasoning-grpo-2026-09-03]]` — LLM reasoning aligned via GRPO for context-aware factor screening.
- `[[quant/china-ashare-xgboost-treeshap-behavioral-factor-decomposition-2026-09-04]]` — Non-linear factor decomposition and behavioral anomaly capture in China A-shares.
- `[[quant/agentic-ai-nowcasting-stock-returns-llm-web-search-2026-09-04]]` — Real-time autonomous LLM web search nowcasting for equity selection.
- `[[quant/news-event-tag-drift-rumor-resolution-placebo-adjusted-momentum-2026-09-02]]` — Placebo-adjusted event-drift momentum from corporate rumors and news tags.
- `[[quant/finsmart-market-aligned-reinforcement-learning-sentiment-alpha-2026-09-02]]` — Market-aligned reinforcement learning for sentiment alpha.

## Sources

1. **Primary Research Paper:**
   - Authors: Xiang Li, Zikai Wei, Yiyan Qi, Wanyun Zhou, Xiang Liu, Penglei Sun, Yongqi Zhang, and Xiaowen Chu.
   - Title: *Janus-Q: End-to-End Event-Driven Trading via Hierarchical-Gated Reward Modeling*.
   - Publication: arXiv preprint `arXiv:2602.19919v1 [cs.AI, q-fin.TR, q-fin.ST]`, submitted 27 February 2026.
   - Canonical URL: `https://arxiv.org/abs/2602.19919`
   - Full-text HTML: `https://arxiv.org/html/2602.19919v1`
   - DOI: `10.48550/arXiv.2602.19919`
2. **Empirical Data Platforms Cited in Primary Source:**
   - Tushare Financial Data: `https://tushare.pro` (Daily A-share price and volume series)
   - Datayes Platform: `https://www.datayes.com` (Chinese financial news corpus)
   - Wind Financial Terminal: `https://www.wind.com.cn` (Firm profiles, market share, and Barra risk factors)
   - MSCI Barra CNE5 Equity Model: `https://www.msci.com/documents/10199/2935796a-0a80-4050-934a-12966d1e2518` (Factor risk structure)
