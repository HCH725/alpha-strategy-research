---
schema: strategy-research-record-v1
title: "FinSMART: Market-Aligned Reinforcement Learning via Group Relative Policy Optimization for Cross-Sectional Equity Sentiment Alpha"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - large-language-models
  - reinforcement-learning
  - grpo
  - sentiment-analysis
  - cross-sectional-equity
  - market-aligned
  - lora
status: research-only
confidence: medium
source_as_of: 2026-07-29
sources:
  - "Giorgos Iacovides, Wuyang Zhou, and Danilo Mandic, 'FinSMART: Financial Sentiment Analysis for Algorithmic Trading through Market-Aligned Reinforcement Learning', arXiv preprint arXiv:2607.28127v1 [cs.CL, cs.LG, q-fin.ST, q-fin.TR], submitted July 29, 2026. Stable URL: https://arxiv.org/abs/2607.28127. Full text HTML: https://arxiv.org/html/2607.28127v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FinSMART: Market-Aligned Reinforcement Learning via Group Relative Policy Optimization for Cross-Sectional Equity Sentiment Alpha

## Provenance

- **Primary Source:** Giorgos Iacovides, Wuyang Zhou, and Danilo Mandic (Imperial College London), *"FinSMART: Financial Sentiment Analysis for Algorithmic Trading through Market-Aligned Reinforcement Learning"*, arXiv preprint `arXiv:2607.28127v1 [cs.CL, cs.LG, q-fin.ST, q-fin.TR]`, submitted July 29, 2026. Stable URL: [https://arxiv.org/abs/2607.28127](https://arxiv.org/abs/2607.28127). Full text HTML: [https://arxiv.org/html/2607.28127v1](https://arxiv.org/html/2607.28127v1).
- **Underlying Text & Market Data Sources:**
  - Financial news corpus: Comprehensive business articles collected from *The Motley Fool* (TMF) and *MarketWatch* from February 2015 to June 2021.
  - Traded Universe: Constituent stocks of the S&P 500 index (1,672 trading days of daily return data per company retrieved from Yahoo Finance).
  - Target entity linking: BERT-base-NER model used to identify corporate entities referenced in news articles; only articles with entity confidence $\ge 98\%$ retained.
  - Sentiment gating: Pre-trained reference LLM restricts the training corpus to articles possessing unambiguous sentiment signals (forcing valid token completions in $\{\texttt{Positive}, \texttt{Negative}, \texttt{Neutral}\}$).
  - Chronological Partitioning:
    - In-sample training corpus: News published up to December 31, 2018 (approximately 30,000 articles, with 5% held out for validation and checkpoint selection every 500 steps);
    - Out-of-sample backtest & inference corpus: Articles published between January 1, 2019 and June 30, 2021 (approximately 325,000 articles, spanning both benign equity expansion and the COVID-19 liquidity crash).
- **Foundational Literature:**
  - Shao, Z. et al. (2024), "DeepSeekMath: Pushing the limits of mathematical reasoning in open language models", arXiv:2402.03300 — Group Relative Policy Optimization (GRPO) framework.
  - Iacovides, G., Zhou, W., and Mandic, D. (2025), "FinDPO: Financial sentiment analysis for algorithmic trading through preference optimization of LLMs", *Proceedings of the 6th ACM International Conference on AI in Finance (ICAIF '25)*, 647–655 — logit-to-score conversion and preference optimization baseline.
  - Hu, E. J. et al. (2022), "LoRA: Low-rank adaptation of large language models", *ICLR 2022* — parameter-efficient fine-tuning.
  - Ke, Z. T., Kelly, B. T., and Xiu, D. (2019), "Predicting returns with text data", *NBER Working Paper* No. 26186 — methodology for equity text alpha signals.

## Economic mechanism

### Source-reported

1. **Failure of Human-Annotated Supervised Fine-Tuning (SFT):** Prevailing financial language models (FinBERT, FinLlama, Instruct-FinGPT) are trained on static human-annotated sentiment corpora (such as Financial PhraseBank). These datasets are market-agnostic, narrow in scale, and reflect linguistic opinions rather than tradable economic consequences. Supervised fine-tuning promotes sample memorization rather than out-of-sample generalization, leading to alpha decay when market regimes shift.
2. **Realized Market Outcomes as Direct Reinforcement Learning Supervision:** FinSMART abandons manual labels and establishes an end-to-end feedback loop directly from realized financial returns. An LLM policy (Llama-3-8B-Instruct) generates sentiment predictions $d \in \{-1, 0, +1\}$ that are optimized via Group Relative Policy Optimization (GRPO) against economic market rewards.
3. **Dual-Filter Asymmetric Trading Reward:** Raw market returns possess high noise, fat tails, and non-stationarity. To prevent mode collapse or training instability, the reward structure requires two independent market conditions:
   - **Condition 1 (Directional Profitability):** The predicted sentiment sign must match the stock's realized return ($\operatorname{sign}(d) = \operatorname{sign}(r)$);
   - **Condition 2 (Idiosyncratic Alpha Significance):** The stock's excess return over the market index ($\alpha = r_{\mathrm{stock}} - r_{\mathrm{SPY}}$) must exceed an economic significance hurdle $|\alpha| > \tau$ (calibrated to $\tau = 0.5\%$).
   - **Asymmetric Payoff:** Correct directional predictions receive $+1.0$, while incorrect predictions receive $-0.5$, penalizing errors while avoiding conservative collapse to neutral outputs.
4. **Contemporaneous Training Supervision vs. Next-Day Out-of-Sample Execution:** The authors demonstrate that publication-day returns exhibit strong alignment with news sentiment (e.g. 5.0% alpha spread on TMF and Pearson correlation of 0.41), whereas 1-day shifted returns drop to 0.3% spread and 0.03 correlation. Using same-day returns during GRPO training supplies a dense supervisory gradient, while evaluating trading exclusively on next-day open-to-open returns guarantees strict causal execution without look-ahead bias.
5. **Periodic Market-Aware Continual Retraining:** Because training requires only unlabelled news text and observed market returns, the model supports automated periodic retraining (tested via a 6-month expanding window), continually updating sentiment representations as market vernacular and macro dynamics evolve.

### Research interpretation

The alpha hypothesis is a **cross-sectional text-implied event drift strategy**:
1. **Underreaction to Firm-Specific News Catalysts:** Equity markets exhibit delayed price discovery following company-specific news releases. By filtering for high-conviction named entities ($\ge 98\%$ confidence) and idiosyncratic alpha ($|\alpha| > 0.5\%$), the model isolates genuine informational shocks from market-wide co-movement.
2. **Nonlinear Sentiment Scoring via Logit Projections:** Unlike heuristic lexicon counting, the policy extracts continuous sentiment scores $[-1, 1]$ directly from next-token logits. This provides cross-sectional dispersion, enabling a high-conviction ranking of extreme winners and losers across the S&P 500 universe.
3. **Information Coefficient (RankIC) Superiority:** The model's cross-sectional ranking ability generates an out-of-sample RankIC of 0.061 (a 15% increase over preference-optimized FinDPO), translating into robust long-short spread capture.

## Signal

### Data Pipeline and Signal Filtering

1. **Named Entity Recognition (NER) Filter:**
   - Raw news articles from The Motley Fool and MarketWatch are processed via `BERT-base-NER`.
   - Articles are retained if and only if the identified corporate entity has a confidence score $\ge 98\%$; multi-company or ambiguous articles are discarded.
2. **Sentiment Gating:**
   - The entity-linked article text is presented to the frozen reference model $\pi_{\mathrm{ref}}$ under a constrained classification prompt restricted to $\{\texttt{Positive}, \texttt{Negative}, \texttt{Neutral}\}$.
   - If the reference model does not assign highest probability to one of these three tokens, the article is discarded.

### Reward Function Formulation (Training Phase)

For an article $x$ discussing a stock with realized raw return $r$ and S&P 500 proxy return $r_{\mathrm{SPY}}$, the idiosyncratic return is:
$$\alpha = r - r_{\mathrm{SPY}}$$
The ground-truth market direction state $y \in \{-1, 0, +1\}$ is defined with hurdle $\tau = 0.5\%$:
$$y = \begin{cases} +1, & \text{if } r > 0 \text{ and } \alpha > \tau \\ -1, & \text{if } r < 0 \text{ and } \alpha < -\tau \\ 0, & \text{otherwise} \end{cases}$$
For model-generated directional prediction $d \in \{-1, 0, +1\}$, the discrete asymmetric reward $R(x, d)$ is:
$$R(x, d) = \begin{cases} +1.0, & \text{if } d = y \text{ and } y \in \{-1, +1\} \\ -0.5, & \text{if } d \ne y \text{ and } y \in \{-1, +1\} \\ 0.0, & \text{if } y = 0 \end{cases}$$

### Group Relative Policy Optimization (GRPO)

- Group size: $G = 8$ completions sampled per prompt $x$.
- Relative Advantage Normalization:
  $$A_i = \frac{r_i - \mu(r)}{\sigma(r) + \delta}, \quad \delta = 10^{-4}$$
- Clipped surrogate loss regularized by reference KL divergence ($\beta = 0.1$):
  $$\mathcal{L}_{\mathrm{GRPO}}(\theta) = -\frac{1}{G} \sum_{i=1}^G \left[ \min\left( \frac{\pi_\theta(y_i|x)}{\pi_{\theta_{\mathrm{old}}}(y_i|x)} A_i, \; \operatorname{clip}\left(\frac{\pi_\theta(y_i|x)}{\pi_{\theta_{\mathrm{old}}}(y_i|x)}, 1-\epsilon, 1+\epsilon\right) A_i \right) - \beta D_{\mathrm{KL}}(\pi_\theta \,||\, \pi_{\mathrm{ref}}) \right]$$
- Parameter efficiency: Low-Rank Adaptation (LoRA) applied with rank $r = 16$, scaling factor $\alpha = 32$, dropout $0.05$ (13.6M trainable parameters, 0.17% of Llama-3-8B-Instruct).

### Continuous Sentiment Scoring (Inference Phase)

At inference time on trading day $t$, the discrete classification prompt produces output logits for the sentiment tokens. Using the FinDPO logit-to-score transformation:
$$S_{i, t} = \frac{\exp(\ell_{+}) - \exp(\ell_{-})}{\exp(\ell_{+}) + \exp(\ell_{-}) + \exp(\ell_{0})} \in [-1, 1]$$
where $\ell_{+}, \ell_{-}, \ell_{0}$ are unnormalized logits for $\texttt{Positive}, \texttt{Negative}, \texttt{Neutral}$.
For companies with $N_t$ articles published on day $t$, the daily composite sentiment is the arithmetic mean:
$$S_t = \frac{1}{N_t} \sum_{i=1}^{N_t} S_{i, t}$$

### Cross-Sectional Long-Short Portfolio Allocation

1. On each trading day $t$, rank all investable S&P 500 stocks having valid news sentiment scores $S_t$.
2. Allocate equal capital weights across the top $35\%$ ranked companies (Long portfolio, $N_{\mathrm{Long}}$).
3. Allocate equal capital weights across the bottom $35\%$ ranked companies (Short portfolio, $N_{\mathrm{Short}}$).
4. Middle $30\%$ ranked companies are unallocated.

## Required data

- **Universe:** Point-in-time constituent stocks of the S&P 500 index. Dynamically reconstituted daily to include only companies with both published news and active market trading data (eliminating survivorship bias).
- **Text Data:**
  - Full-text financial news feeds from *The Motley Fool* and *MarketWatch* (February 2015 to June 2021);
  - Timestamps aligned to US equity trading days (UTC/EST).
- **Market Data:**
  - Daily Open, High, Low, Close (OHLC) equity prices from Yahoo Finance;
  - Daily S&P 500 index proxy (SPY ETF) prices for benchmark return and idiosyncratic alpha calculation;
  - Daily open-to-open returns: $r_{i, t+1} = (P_{i, t+2}^{\mathrm{open}} - P_{i, t+1}^{\mathrm{open}}) / P_{i, t+1}^{\mathrm{open}}$.
- **Missing Data Handling:** Companies without published news articles on date $t$ are omitted from that day's ranking; days without valid trading quotes are dropped.

## Execution assumptions

- **Execution Cadence:** Daily rebalancing at the market open on day $t+1$ using sentiment derived from news published on day $t$.
- **Holding Period:** Exactly 1 trading day (positions opened at market open $t+1$ and liquidated at market open $t+2$).
- **Return Calculation:** Strictly next-day open-to-open returns ($r_{\mathrm{Long}, t+1} - r_{\mathrm{Short}, t+1}$), completely separating execution from the same-day returns used in GRPO training.
- **Risk-Free Rate:** Assumed $R_f = 0$ in the empirical benchmark due to prevailing near-zero yields over the study period.
- **Friction & Shorting Assumptions:**
  - Primary source reports performance without explicitly deducting taker commissions, borrow fees, or slippage (explicit provenance gap).
  - Short positions assume perfect borrow availability for all bottom-quintile S&P 500 stocks.

## Evidence

### Source-reported

All figures, metrics, and comparisons trace directly to Iacovides, Zhou, & Mandic (arXiv:2607.28127v1, Section 6, Tables 1–2, Figure 4):

1. **Out-of-Sample Portfolio Performance (January 2019 – June 2021, Table 1):**
   - **FinSMART (Market-Aligned RL, Static Model):**
     - Cumulative Return ($r_{\mathrm{cum}}$): **264.9%**
     - Annualized Return ($R_p$): **91.5%**
     - Annualized Sharpe Ratio ($S_a$): **1.97**
     - Sortino Ratio ($S_o$): **2.40**
     - Calmar Ratio ($C_r$): **4.23**
     - Rank Information Coefficient (RankIC): **0.061**
   - **FinDPO Baseline (Previous State-of-the-Art Preference Model, Llama-3-8B):**
     - Cumulative Return: 109.8%
     - Annualized Return: 45.0%
     - Annualized Sharpe Ratio: 1.12
     - RankIC: 0.053
     - *FinSMART relative improvement over FinDPO:* $+141\%$ cumulative return, $+103\%$ annualized return, $+75.9\%$ Sharpe ratio, $+15.1\%$ RankIC.
   - **FinLlama Baseline (Supervised Fine-Tuned Llama-2-7B):**
     - Cumulative Return: 67.2%, Annualized Sharpe: 0.81, RankIC: 0.041.
   - **FinBERT Baseline (Araci 2019, 110M Encoder):**
     - Cumulative Return: 41.5%, Annualized Sharpe: 0.54, RankIC: 0.028.
   - **Lexicon Baselines (LMD, HIV-4, VADER):**
     - LMD: Cumulative Return 18.2%, Sharpe 0.28, RankIC 0.012.
     - VADER: Cumulative Return 22.4%, Sharpe 0.32, RankIC 0.015.
     - HIV-4: Cumulative Return 11.7%, Sharpe 0.19, RankIC 0.009.

2. **Periodic Market-Aligned Retraining Performance (6-Month Expanding Window, Table 2 & Figure 4):**
   - When retrained every 6 months using accumulated news and market feedback across 4 sequential iterations:
     - Cumulative Return increases from **264.9%** (static model) to **406.0%** (retrained model).
     - Sharpe Ratio, Sortino Ratio, Calmar Ratio, and RankIC exhibit monotonic improvements across each retraining epoch.
     - Positive correlation of $r = 0.72$ between the volume of newly added articles in each 6-month period and the incremental performance delta over the static baseline.

3. **Computational Efficiency:**
   - Full GRPO training on 30,000 articles completes in 8 hours on a single NVIDIA A6000 (48 GB) GPU with 13.6M LoRA parameters.

### Independently reproduced

`not independently reproduced`.

### Negative evidence

- **Omission of Transaction Costs and Borrow Fees:** The primary source does not deduct bid-ask spread, broker commissions, market impact, or short borrow fees. In a daily rebalanced 35% long-short equity strategy with high news-driven turnover, friction will erode gross returns.
- **Extreme Return Decay Beyond Publication Day:** The authors' own preliminary empirical tests reveal that the alpha spread between positive and negative news drops precipitously from 5.0% on publication day down to 0.3% on next-day returns (and Pearson correlation drops from 0.41 to 0.03). This confirms that markets absorb news rapidly and that residual open-to-open drift is narrow.
- **Entity Identification Vulnerability:** Performance depends heavily on the NER threshold ($\ge 98\%$). In lower-liquidity news environments with syndicated or ambiguous headlines, NER error degrades reward quality.

## Falsification plan

1. **Transaction Cost and Borrow Fee Hurdle Test:** Apply realistic execution costs (5 bps maker / 15 bps taker fees plus 50 bps annualized borrow cost on short positions). If net annualized Sharpe ratio drops below 0.80, falsify the tradable institutional alpha claim.
2. **Entity-Shuffling Placebo Test:** Randomly shuffle the stock tickers associated with news articles while preserving return series. If the resulting GRPO policy achieves a RankIC within 1 standard deviation of 0.061, invalidate the hypothesis that market-aligned reinforcement learning learns true semantic signals.
3. **Publication Lag Stress Test:** Introduce an artificial execution delay of 24 to 48 hours after news publication. If RankIC decays to $\le 0.015$ (comparable to static VADER), confirm that the edge is purely an ephemeral post-earnings announcement drift phenomenon.
4. **Out-of-Universe Transfer Test:** Apply the pre-trained FinSMART model to UK FTSE 100 or European Stoxx 600 news without fine-tuning. If RankIC fails to exceed zero with statistical significance ($t < 1.96$), reject cross-market universality.

## Crypto portability

- **Portability:** `adapted` / `unproven`.
- **Porting Rationale:** The primary source evaluates US equities (S&P 500) exclusively. The core mechanism (reinforcement learning from realized market returns using LLMs) has not been demonstrated on cryptocurrencies.
- **Crypto Portability Challenges:**
  - **Source Material Shift:** Crypto sentiment is dominated by decentralized, uncurated social channels (Crypto Twitter/X, Telegram announcements, Discord, governance forums) rather than formal editorial outlets like MarketWatch or The Motley Fool.
  - **Entity Disambiguation:** Ticker ambiguity is severe in crypto (e.g., meme tokens with identical tickers, wrapped assets, multi-chain tokens), which challenges standard BERT-base-NER models.
  - **Continuous 24/7 Market Clocks:** Lack of market open/close boundaries requires defining custom rolling event windows (e.g. 1-hour or 4-hour post-headline drift) rather than daily open-to-open bars.
  - **Perpetual Funding Rate Drag:** Taking short positions in high-sentiment-dispersion altcoins exposes the strategy to unpredictable funding rate spikes on perpetual exchanges.

## Limitations

- `not independently reproduced`;
- `unproven` in crypto markets (adapted research interpretation only);
- **Omission of Friction Modeling:** Backtest results reflect zero transaction costs, zero market impact, and zero borrow expense;
- **Restricted News Sourcing:** Relies exclusively on two curated editorial news providers (The Motley Fool and MarketWatch); performance on raw wire services (Bloomberg, Reuters) or social media is unmeasured;
- **Survivorship and Coverage Bias:** Only S&P 500 constituents with high-confidence news coverage are traded on any given day, introducing variable cross-sectional breadth ($N_t \ll 500$).

## Implementation status

- `not-implemented`.
- Pure research capture. No NautilusTrader, PyBroker, paper trading, testnet, or live trading modules have been constructed or authorized.

## Adoption boundary

- `research-only`, `not-approved`.
- This record captures academic research on reinforcement learning for LLM financial sentiment extraction. It does not authorize capital allocation, strategy promotion, or automated trading deployment.

## Related Wiki records

- `[[quant/foreign-exchange-macro-news-fundamental-momentum-llm-taylor-rule-2026-09-02]]` — LLM-driven macro news fundamental momentum.
- `[[quant/news-event-tag-drift-rumor-resolution-placebo-adjusted-momentum-2026-09-02]]` — Event tag drift and rumor resolution momentum.
- `[[quant/tda-persistent-homology-finbert-sentiment-portfolio-optimization-2026-09-02]]` — Sentiment extraction via FinBERT coupled with topological data analysis.
- `[[quant/crypto-cross-sectional-sentiment-risk-beta-premium-2026-09-01]]` — Cross-sectional sentiment risk premia.

## Sources

1. Giorgos Iacovides, Wuyang Zhou, and Danilo Mandic, *"FinSMART: Financial Sentiment Analysis for Algorithmic Trading through Market-Aligned Reinforcement Learning"*, arXiv preprint `arXiv:2607.28127v1 [cs.CL, cs.LG, q-fin.ST, q-fin.TR]`, submitted July 29, 2026. Stable URL: [https://arxiv.org/abs/2607.28127](https://arxiv.org/abs/2607.28127). Full text HTML: [https://arxiv.org/html/2607.28127v1](https://arxiv.org/html/2607.28127v1).
2. Shao, Z., Wang, P., Zhu, Q., Xu, R., Song, J., Bi, X., Zhang, H., Zhang, M., Li, Y. K., Wu, Y., and Guo, D. (2024), "DeepSeekMath: Pushing the limits of mathematical reasoning in open language models", arXiv preprint `arXiv:2402.03300`.
3. Iacovides, G., Zhou, W., and Mandic, D. (2025), "FinDPO: Financial sentiment analysis for algorithmic trading through preference optimization of LLMs", *Proceedings of the 6th ACM International Conference on AI in Finance (ICAIF '25)*, 647–655. DOI: [10.1145/3768292.3770367](https://doi.org/10.1145/3768292.3770367).
4. Hu, E. J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., Wang, L., and Chen, W. (2022), "LoRA: Low-rank adaptation of large language models", *International Conference on Learning Representations (ICLR)*.
5. Ke, Z. T., Kelly, B. T., and Xiu, D. (2019), "Predicting returns with text data", *NBER Working Paper* No. 26186. DOI: [10.3386/w26186](https://doi.org/10.3386/w26186).
6. Araci, D. (2019), "FinBERT: Financial sentiment analysis with pre-trained language models", arXiv preprint `arXiv:1908.10063`.
