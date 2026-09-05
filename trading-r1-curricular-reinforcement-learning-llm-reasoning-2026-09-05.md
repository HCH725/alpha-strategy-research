---
schema: strategy-research-record-v1
title: "Trading-R1: Curricular Reinforcement Learning with Reverse Reasoning Distillation for LLM Financial Trading"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - llm-reasoning
  - reinforcement-learning
  - grpo
  - volatility-normalization
  - equity-trading
status: research-only
confidence: medium
source_as_of: 2025-09-12
sources:
  - "https://arxiv.org/abs/2509.11420"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Trading-R1: Curricular Reinforcement Learning with Reverse Reasoning Distillation for LLM Financial Trading

## Provenance

- **Primary Source:** Yijia Xiao, Edward Sun, Tong Chen, Fang Wu, Di Luo, and Wei Wang (University of California, Los Angeles & Tauric Research), *"Trading-R1: Financial Trading with LLM Reasoning via Reinforcement Learning"*, arXiv preprint `arXiv:2509.11420v1 [cs.AI, q-fin.TR]`, submitted September 12, 2025.
- **Canonical URLs:**
  - Abstract: [https://arxiv.org/abs/2509.11420](https://arxiv.org/abs/2509.11420)
  - Full Text HTML: [https://arxiv.org/html/2509.11420](https://arxiv.org/html/2509.11420)
  - DOI: [10.48550/arXiv.2509.11420](https://doi.org/10.48550/arXiv.2509.11420)
- **Primary Open-Source Repository:** `https://github.com/TauricResearch/Trading-R1` [source-reported repository release declared in preprint; public code release].
- **Underlying Training Corpus:** Tauric-TR1-DB, a curated multi-modal financial dataset spanning January 1, 2024 to May 31, 2025 (~354 trading days, 100k samples) across 14 mega-cap US equities and sector ETFs [source-reported].

---

## Economic mechanism

### Source-reported

Financial markets demand interpretability, transparency, and disciplined execution. While general-purpose Large Language Models (LLMs) can generate fluent qualitative summaries, they suffer from two coupled failure modes when applied to financial trading:
1. **External Prior Vulnerability:** In noisy, unstructured financial environments, unguided models latch onto superficial or noisy signals in long contexts (20k–30k tokens), resulting in hallucinations and unanchored claims.
2. **Internal Prior Compounding:** In autoregressive generation, unconstrained chain-of-thought traces accumulate intermediate errors, leading to erratic conclusions and fragile decisions.

Conversely, purely mathematical Reasoning Language Models (RLMs) trained on coding and mathematics lack domain-specific financial discipline; their unconstrained reasoning paths frequently drift away from price-action realities into ungrounded tangents.

Trading-R1 resolves this dilemma by introducing a three-stage easy-to-hard curriculum that interleaves Supervised Fine-Tuning (SFT) warm-starts with Reinforcement Learning Fine-Tuning (RFT) via Group Relative Policy Optimization (GRPO):
- **Stage I (Structure):** Inculcates professional investment thesis organization (XML sectioning, headers, tables, summary conclusions).
- **Stage II (Evidence):** Enforces evidential rigor through mandatory "opinion-quote-source" structures, compelling the model to cite verifiable data points from the context.
- **Stage III (Decision):** Aligns final trading recommendations ({STRONG SELL, SELL, HOLD, BUY, STRONG BUY}) against realized multi-horizon, volatility-normalized price moves using an asymmetric payoff matrix that penalizes false bullish signals ~12% heavier than false bearish errors.

### Research interpretation

The underlying alpha mechanism is multi-modal information compression and risk-asymmetric decision alignment:
1. **Non-linear Cross-Modal Synthesis:** Quantitative time-series models typically operate on structured numerical tables, missing textual catalysts (regulatory disclosures, management guidance changes, supply chain revisions). Discursive LLMs capture these narrative nuances but lack quantitative discipline. By grounding qualitative extraction in multi-horizon volatility-normalized returns, Trading-R1 effectively acts as a semantic dimensionality reduction filter.
2. **Asymmetric Risk Pricing:** The asymmetric loss function ($M$) mathematically reflects institutional drawdown aversion. In equity markets, volatility spikes and liquidations concentrate in market downturns ("markets take the escalator up and the elevator down"). Conditioning policy gradients on heavier downside penalties reduces left-tail exposure and curbs momentum chasing near market tops.
3. **Multi-Horizon Volatility Denoising:** Normalizing 3-, 7-, and 15-day forward price returns by 20-day rolling return volatility converts unstandardized drift into Sharpe-equivalent signals. This prevents the learning algorithm from being dominated by high-beta regimes or volatile meme-stock periods.

---

## Signal

### 1. Multi-Horizon Volatility-Adjusted Target Labeling (Algorithm 1)

The training target and outcome evaluation signal are generated through a multi-horizon, volatility-normalized procedure:
1. **Price Smoothing:** Calculate Exponential Moving Average (EMA) price series from daily close prices [source-reported].
2. **Multi-Horizon Returns:** For each trading day $t$, calculate forward percentage price returns over three distinct time horizons [source-reported]:
   $$R_{H, t} = \frac{\text{EMA}_{t+H} - \text{EMA}_t}{\text{EMA}_t}, \quad H \in \{3, 7, 15\} \text{ trading days}$$
3. **Rolling Volatility Normalization:** Normalize each return series by the asset's trailing 20-day rolling return volatility $\sigma_{20, t}$ to yield Sharpe-like signals [source-reported]:
   $$S_{H, t} = \frac{R_{H, t}}{\sigma_{20, t}}$$
4. **Composite Signal Combination:** Combine multi-horizon signals using fixed empirical weights [source-reported]:
   $$S_{\text{comp}, t} = 0.3 \cdot S_{3, t} + 0.5 \cdot S_{7, t} + 0.2 \cdot S_{15, t}$$
5. **Asymmetric Quantile Discretization:** Map composite signal values $S_{\text{comp}}$ into five discrete action categories based on empirical percentile cutoffs of the training distribution [source-reported]:
   - **STRONG BUY:** $S_{\text{comp}} \ge 85\text{th percentile}$ (top 15%)
   - **BUY:** $53\text{rd percentile} \le S_{\text{comp}} < 85\text{th percentile}$ (32% of sample)
   - **HOLD:** $15\text{th percentile} \le S_{\text{comp}} < 53\text{rd percentile}$ (38% of sample)
   - **SELL:** $3\text{rd percentile} \le S_{\text{comp}} < 15\text{th percentile}$ (12% of sample)
   - **STRONG SELL:** $S_{\text{comp}} < 3\text{rd percentile}$ (bottom 3%)

### 2. Reverse Reasoning Distillation for SFT Warm-Start

To source long-chain supervisory reasoning traces without incurring massive annotation costs, the authors introduce reverse reasoning distillation [source-reported]:
1. Feed structured financial context into a frontier reasoning model API (e.g. OpenAI o3-mini or o4-mini) and extract its final trade recommendation [source-reported].
2. Pass the input context and the extracted recommendation to a planner model to infer the high-level analytical scaffolding [source-reported].
3. Employ a lightweight LLM (GPT-4.1-nano) to elaborate how each individual data modality (news, macro, fundamentals, technicals) justifies the recommendation [source-reported].
4. Programmatically stitch segments into a unified, step-by-step investment thesis (6k–8k tokens) paired with the input context (20k–30k tokens) [source-reported].

### 3. Three-Stage Curricular Reinforcement Learning (GRPO)

The base backbone model is Qwen3-4B [source-reported]. The model undergoes three sequential SFT warm-starts, each immediately followed by Group Relative Policy Optimization (GRPO) without an auxiliary value/critic network [source-reported]:

- **Stage I (Structure Reward $R_{\text{struct}}$):**
  - Enforces XML-tagged sectioning: requires 5 to 7 analytical category blocks (excluding `<think>`) plus a mandatory `<conclusion>` block [source-reported].
  - Checks for structural Markdown elements: headers ($\mathbf{1}_{\text{headers}}$), bullet points ($\mathbf{1}_{\text{bullets}}$), bold highlights ($\mathbf{1}_{\text{bold}}$), and tables ($\mathbf{1}_{\text{tables}}$) [source-reported].
  - Sections with word count $w < w_{\min} = 50$ words are penalized to a floor reward of 0.2 [source-reported].

- **Stage II (Evidence Reward $R_{\text{evid}}$):**
  - Requires claims to follow an "Opinion-Quote-Source" format [source-reported].
  - Opinion text precedes citation markers; optimal length $w_{\text{op}} \in [15, 90]$ words (strict range 16–30 words) [source-reported].
  - Direct context quotes must use italic markdown (`*quote*`); explicit source references must use inline code markdown (`` `source` ``) [source-reported].
  - Target bullet density: 4 to 7 evidence bullets per analysis section [source-reported]. Aggregation across sections utilizes harmonic mean to suppress outlier gaming [source-reported].

- **Stage III (Decision Reward $R_{\text{decision}}$ & Asymmetric Loss Matrix $\mathbf{M}$):**
  - Action space: $\hat{d} \in \{\text{STRONG SELL}, \text{SELL}, \text{HOLD}, \text{BUY}, \text{STRONG BUY}\}$ [source-reported].
  - Payoff matrix $\mathbf{M}$ (rows = predictions, columns = ground truth):
    - Exact match: $+1.00$ [source-reported]
    - Same-direction intensity mismatch (e.g., BUY vs STRONG BUY): $+0.75$ [source-reported]
    - False bullish penalty (STRONG BUY predicted vs STRONG SELL true): $-2.25$ [source-reported]
    - False bearish penalty (STRONG SELL predicted vs STRONG BUY true): $-2.00$ [source-reported] (encodes ~12% heavier penalty on false bullish signals)
    - Anti-hold penalty: predicting HOLD when market moves strongly is penalized $-1.50$ (bearish ground truth) or $-1.00$ (bullish ground truth) [source-reported]
    - Unparseable or missing decision tag: $-1.50$ penalty [source-reported].

---

## Required data

- **Universe:** 14 liquid US equities and major index/sector ETFs [source-reported]:
  - Mega-cap Tech: NVIDIA (NVDA), Microsoft (MSFT), Apple (AAPL) [source-reported].
  - Communication & Consumer: Meta (META), Amazon (AMZN), Tesla (TSLA) [source-reported].
  - Financials: Berkshire Hathaway (BRK.B), JPMorgan Chase (JPM) [source-reported].
  - Healthcare: Eli Lilly (LLY), Johnson & Johnson (JNJ) [source-reported].
  - Energy: ExxonMobil (XOM), Chevron (CVX) [source-reported].
  - Broad Index/Sector ETFs: SPDR S&P 500 ETF Trust (SPY), Invesco QQQ Trust (QQQ) [source-reported].
- **Sample Timeframes & Partitions:**
  - *Training Sample (Tauric-TR1-DB):* January 1, 2024 to May 31, 2025 (~354 trading days, 100k generated instances via 20 sample variations per day-ticker pair) [source-reported].
  - *Out-of-Sample Evaluation Window:* June 1, 2024 to August 31, 2024 (strictly held-out 3-month evaluation period) [source-reported].
- **Feature Modalities & Vendors:**
  - *Technicals:* Daily OHLCV, 2-year lookback for moving averages (SMA 20/50/200, EMA), MACD, RSI, ROC, KDJ, ATR, Bollinger Bands, Z-scores, MFI, PVO, VWMA, ADX (sourced from Yahoo Finance and stockstats; 15-day output windows) [source-reported].
  - *Fundamentals:* Income statements, balance sheets, cash flow metrics, SEC filings (sourced via SimFin API) [source-reported].
  - *News Streams:* Finnhub API (real-time structured news) and Google News web scraper, bucketed into temporal windows [source-reported].
  - *Sentiment & Positioning:* Finnhub insider sentiment, Finnhub insider transactions, Yahoo Finance sell-side analyst consensus recommendations [source-reported].
  - *Macroeconomic Context:* Federal Reserve Economic Data (FRED API) series [source-reported].
  - *Social Media:* Explicitly excluded from inputs due to severe sample bias and poor signal-to-noise ratio [source-reported].
- **Point-in-Time Integrity:** Strict chronological cutoff enforced on all textual news, filings, and macroeconomic prints; only data timestamped prior to trading day $t$ decision time is included [source-reported].

---

## Execution assumptions

- **Holding Horizon:** Medium-term horizon targeting ~1 week (5–7 trading days), balancing LLM inference latency against macro drift [source-reported].
- **Execution Timing:** Decision formed at close of trading day $t$; order execution simulated at next-day open [`research-proposed` next-open market fill].
- **Position Sizing & Action Semantics:** Discrete 5-state categorical action space [source-reported]:
  - STRONG BUY: +100% long allocation [`research-proposed`]
  - BUY: +50% long allocation [`research-proposed`]
  - HOLD: 0% net exposure (flat) [`research-proposed`]
  - SELL: -50% short allocation [source-reported long-short action semantics; `research-proposed`]
  - STRONG SELL: -100% short allocation [source-reported; `research-proposed`]
- **Transaction Costs & Slippage:** Main text reports gross backtest performance with an outcome reward trading cost parameter $\kappa \ge 0$ [source-reported; `research-proposed` 5 bps broker commission + 3 bps bid-ask half-spread].
- **Borrow & Shorting Friction:** Strategy permits shorting blue-chip equities; frictionless borrow assumed in reported paper metrics [source-reported; provenance gap on borrow availability / `research-proposed` 100 bps p.a. equity borrow fee].
- **Capacity & Participation Limits:** Evaluated solely on multi-hundred-billion to multi-trillion market cap mega-caps and liquid ETFs ($>\$11\text{T}$ combined market capitalization); estimated institutional capacity exceeds $\$100\text{M}$ [source-reported universe context; `research-proposed` 1.0% ADV participation cap].

---

## Evidence

### Source-reported

All figures below are transcribed directly from the empirical results in Section 4 and Section 5 of `arXiv:2509.11420v1`, evaluated over the held-out test period (June 1, 2024 to August 31, 2024):

#### 1. Out-of-Sample Performance on Target Assets:
- **NVIDIA (NVDA):**
  - Trading-R1 Sharpe Ratio: **1.88** [source-reported]
  - Trading-R1 Cumulative Return (CR): **8.08%** [source-reported]
  - Trading-R1 Hit Rate (HR): **70.0%** [source-reported]
- **Apple (AAPL):**
  - Trading-R1 Sharpe Ratio: **1.80** vs. GPT-4.1 baseline **1.24** [source-reported]
  - Trading-R1 Maximum Drawdown (MDD): **3.68%** vs. off-the-shelf RLMs **7.88%** [source-reported]
- **S&P 500 ETF (SPY):**
  - Trading-R1 Hit Rate (HR): **64.0%** [source-reported]

#### 2. Cross-Model Hierarchy and Comparative Findings:
- **Overall Performance Hierarchy:**
  $$\text{SLM} \ll \text{RLM} \ll \text{LLM} < \text{Trading-SFT} \approx \text{Trading-RFT} < \text{Trading-R1}$$
- **Small Language Models (SLMs: Qwen-4B, GPT-4.1-nano, GPT-4.1-mini):** Weakest performers; frequently produce negative Sharpe ratios due to shallow reasoning and hallucinations [source-reported].
- **Off-the-Shelf Reasoning Models (RLMs: DeepSeek, O3-mini, O4-mini):** Despite strong performance in math/coding benchmarks, unguided reasoning models perform poorly on trading tasks, incurring significant capital drawdowns due to verbose, unfocused reasoning that drifts away from market data [source-reported].
- **Large Language Models (LLMs: GPT-4.1, LLaMA-3.3, Qwen3-32B):** Outperform SLMs and off-the-shelf RLMs via broader general knowledge, but lag behind domain-aligned Trading-R1 [source-reported].
- **Trading-R1 Series Ablation:** Combining staged SFT warm-start with RFT produces superior risk-adjusted returns and lower drawdowns compared to either SFT-only or RL-only variants [source-reported].

### Independently reproduced

Not independently reproduced.

### Negative evidence

The authors document extensive structural failure modes and ablation pitfalls in Section 11 ("Trading-R0 Training Observations"):
1. **Instability of Mixed Reward Functions:** In early prototypes (Trading-R0), format/structural rewards and market-outcome rewards were optimized simultaneously in a single RL stage. This led to severe gradient conflict: format rewards pulled the model toward rigid XML compliance while outcome rewards pulled it toward speculative direction guessing. The model oscillated wildly, causing reward curves to spike and collapse [source-reported].
2. **Reward Hacking under Rigid Scaffolding:** Imposing strict, narrow budgets on intermediate `<think>` blocks resulted in "minimum viable completions": models generated superficial, boilerplate padding that satisfied regex checks while hollowing out substantive financial reasoning [source-reported].
3. **Structural Bullish Bias:** Training on 2024–2025 large-cap US equities and mega-cap tech leaders during an AI-driven bull market instilled a structural upward drift in model priors. Discretionary asymmetric quantile thresholds (85%/53%/15%/3%) deliberately hardcoded a long bias [source-reported].
4. **Data Vendor Contamination Vulnerability:** Without active web browsing, models cannot detect corrupted vendor data (e.g. S&P 500 P/E incorrectly fed as 38), directly hallucinating faulty thesis arguments [source-reported].

---

## Falsification plan

The core empirical and methodological claims of Trading-R1 can be tested and potentially falsified through the following five structured protocols:

1. **Macroeconomic Bear Regime & Left-Tail Shock Test:**
   - *Protocol:* Evaluate Trading-R1 on severe historical market drawdowns (e.g., 2022 Fed rate hiking cycle or March 2020 COVID crash) without adjusting the asymmetric quantile thresholds.
   - *Decision Rule (`research-defined falsification threshold`):* If the annualized Sharpe ratio drops below $-0.50$ or Maximum Drawdown exceeds benchmark buy-and-hold by $>5.0$ percentage points, reject the hypothesis that asymmetric loss weighting imparts genuine downside risk mitigation; the strategy's reported profitability is falsified as structural bull-market beta riding.
2. **Multi-Horizon Volatility Denoising Ablation (Placebo Control):**
   - *Protocol:* Replace the volatility-normalized multi-horizon labels ($S_{\text{comp}}$) with raw un-normalized forward close-to-close returns ($R_{7\text{d}}$) during RFT training.
   - *Decision Rule (`research-defined falsification threshold`):* If the un-normalized model achieves out-of-sample Sharpe ratios within $\pm 0.15$ of the volatility-normalized model on NVDA and AAPL, reject the hypothesis that multi-horizon rolling volatility normalization is a necessary mechanism for policy stability.
3. **Reverse Reasoning Distillation vs. Direct CoT Prompting:**
   - *Protocol:* Replace reverse-distilled supervisory traces with zero-shot chain-of-thought completions generated directly by open-source models (e.g. Qwen3-32B) during Stage I/II SFT warm-start.
   - *Decision Rule (`research-defined falsification threshold`):* If zero-shot CoT SFT matches Trading-R1's out-of-sample directional Hit Rate within $\pm 2.0$ percentage points, reject the claim that synthetic reverse-distillation from frontier proprietary models (o3-mini/o4-mini) provides unique structural alpha value.
4. **Transaction Cost and Slippage Friction Stress:**
   - *Protocol:* Apply escalating execution frictions to the simulated 1-week rebalance schedule: $\text{friction} \in \{5, 10, 15, 25, 40\} \text{ bps}$ per trade.
   - *Decision Rule (`research-defined falsification threshold`):* If the net cumulative return on NVDA and AAPL drops below $0.0\%$ at round-trip costs $\le 15\text{ bps}$, reject the practical tradability hypothesis; the gross edge is an artifact of frictionless rebalancing.
5. **Universe Generalization to Small/Mid-Cap Equities:**
   - *Protocol:* Test Trading-R1 on Russell 2000 constituents outside the $>\$11\text{T}$ blue-chip training universe.
   - *Decision Rule (`research-defined falsification threshold`):* If the cross-sectional Hit Rate falls to $\le 50.0\%$ (random chance) across small-cap equities, falsify the claim that Trading-R1 possesses generalizable financial reasoning; its edge is strictly confined to highly scrutinized mega-cap equities with dense public analyst coverage.

---

## Crypto portability

**Portability Classification: Adapted / Unproven**

The primary paper evaluates Trading-R1 strictly on 14 large-cap US equities and index ETFs. Porting this LLM-reasoning RL framework to cryptocurrency markets is a research interpretation and encounters major structural dislocations:

1. **Information Architecture Gap:** Equities possess standardized, audited corporate disclosures: quarterly 10-Q filings, annual 10-K reports, earnings call transcripts, and SEC insider filings (Form 4). In crypto, no such centralized accounting exists. The multi-modal data pipeline must be radically re-engineered to ingest on-chain smart contract activity, DEX liquidity pools, token unlocks, protocol revenue feeds, and GitHub developer commits [`research-proposed`].
2. **Continuous 24/7/365 Auction Dynamics:** Equity markets feature daily opening/closing auctions and weekend halts. Crypto trades continuously. The multi-horizon targets ($H \in \{3, 7, 15\}$ days) must be adapted to rolling synthetic 24-hour UTC intervals [`research-proposed`].
3. **Perpetual Futures Funding Rate Drag:** Trading-R1 assumes symmetrical long-short capability without financing friction. In crypto, shorting is primarily executed via perpetual contracts with 8-hour funding rates. In high-volatility bull runs, short funding or long basis premiums can rapidly erode 1-week gross alpha [`research-proposed`].
4. **Social Media Dependency Paradox:** The paper explicitly removed social media data due to noise in equities. However, in crypto markets, narrative velocity, Twitter/X discourse, and Telegram channel sentiment frequently drive token momentum ahead of technical indicators. Excluding social sentiment in crypto could blind the model to primary price catalysts [`research-proposed`].
5. **Severe Left-Tail Liquidation Cascades:** Crypto markets exhibit frequent -30% to -50% leverage wipeouts within hours. While the asymmetric loss matrix ($\mathbf{M}$) penalizes false bullish calls by ~12%, this penalty magnitude is calibrated to equity drawdowns and would be grossly insufficient to protect against crypto liquidation cascades [`research-proposed`].

---

## Limitations

- **Small Out-of-Sample Window:** The reported backtest covers only 3 months (June 1 to August 31, 2024), representing a limited market regime dominated by large-cap tech strength.
- **Structural Bullish Conditioning:** Training universe selection ($>\$11\text{T}$ mega-cap tech) and quantile boundaries (85%/53%/15%/3%) deliberately hardcode positive market drift.
- **Inference Latency & Token Overhead:** Input prompts average 20k–30k tokens and output theses span 6k–8k tokens. Generating trade decisions for a multi-asset universe requires substantial GPU compute (8x H100/H200 clusters), rendering high-frequency intraday updates impractical.
- **Lack of Independent Replication:** The preprint has not been published in a peer-reviewed finance journal; empirical metrics reflect author backtests and must be treated as unverified research claims.
- **Frictionless Borrow Assumption:** Assumes seamless shorting across all evaluated equities without borrowing constraints, recall risk, or locate fees.

---

## Implementation status

Not implemented. No implementation of the Trading-R1 architecture, reverse reasoning distillation pipeline, or GRPO financial training loop exists in `nautilus-quant-system`, PyBroker pipelines, or NautilusTrader harnesses.

---

## Adoption boundary

This record is research material only. Its presence in this repository does not mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

Any transition of Trading-R1 concepts into quantitative screening or strategy harnesses requires independent out-of-sample walk-forward validation across multiple market cycles, fee-adjusted friction modeling, and formal research intake review.

---

## Related Wiki records

- `[[quant/finsmart-market-aligned-reinforcement-learning-sentiment-alpha-2026-09-02]]` — Market-aligned reinforcement learning for equity news sentiment using GRPO.
- `[[quant/janus-q-event-driven-trading-hierarchical-gated-reward-modeling-2026-09-04]]` — Event-driven trading with hierarchical gated reward modeling and GRPO.
- `[[quant/alphar1-context-aware-alpha-screening-llm-reasoning-grpo-2026-09-03]]` — LLM reasoning aligned via GRPO for context-aware factor screening.
- `[[quant/finatom-head-free-token-generation-etf-allocation-dapo-grpo-2026-09-04]]` — Head-free token generation for ETF allocation via DAPO/GRPO.
- `[[quant/tradingmoe-query-key-sparse-expert-routing-llm-trading-2026-09-03]]` — Sparse mixture-of-experts routing for LLM financial trading.
- `[[quant/mrc-shapley-credit-multi-agent-llm-crypto-portfolio-2026-09-04]]` — Multi-agent LLM financial decision-making with cooperative game theory credit assignment.

---

## Sources

1. **Primary Academic Preprint:** Yijia Xiao, Edward Sun, Tong Chen, Fang Wu, Di Luo, and Wei Wang, *"Trading-R1: Financial Trading with LLM Reasoning via Reinforcement Learning"*, arXiv preprint `arXiv:2509.11420v1 [cs.AI, q-fin.TR]`, submitted September 12, 2025.
   - Abstract URL: [https://arxiv.org/abs/2509.11420](https://arxiv.org/abs/2509.11420)
   - Full Text HTML: [https://arxiv.org/html/2509.11420](https://arxiv.org/html/2509.11420)
   - DOI: [10.48550/arXiv.2509.11420](https://doi.org/10.48550/arXiv.2509.11420)
2. **Author Code & Terminal Repository:** `https://github.com/TauricResearch/Trading-R1` (cited in preprint abstract and Section 1).
3. **Foundational Methodological Literature Cited in Paper:**
   - Z. Shao et al., *"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models"*, arXiv:2402.03300, 2024 (Group Relative Policy Optimization - GRPO).
   - DeepSeek-AI et al., *"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"*, arXiv:2501.12948, 2025.
   - J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, *"Proximal Policy Optimization Algorithms"*, arXiv:1707.06347, 2017.
   - E. J. Hu et al., *"LoRA: Low-Rank Adaptation of Large Language Models"*, arXiv:2106.09685, 2021.
