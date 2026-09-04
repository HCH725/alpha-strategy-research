---
schema: strategy-research-record-v1
title: "Moira: Language-Driven Hierarchical Reinforcement Learning for Pair Trading"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - pairs-trading
  - hierarchical-reinforcement-learning
  - large-language-models
  - textual-policy-optimization
  - prompt-tuning
  - equity-long-short
status: research-only
confidence: medium
source_as_of: 2026-05-03
sources:
  - "Polydoros Giannouris, Yuechen Jiang, Lingfei Qian, Yuyan Wang, Xueqing Peng, Jimin Huang, Guojun Xiong, Sophia Ananiadou, 'Moira: Language-driven Hierarchical Reinforcement Learning for Pair Trading', arXiv:2605.01954v1 [cs.AI, cs.CL, cs.MA], May 2026. DOI: 10.48550/arXiv.2605.01954. https://arxiv.org/abs/2605.01954"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Moira: Language-Driven Hierarchical Reinforcement Learning for Pair Trading

## Provenance

- **Paper Title:** Moira: Language-driven Hierarchical Reinforcement Learning for Pair Trading
- **Authors:** Polydoros Giannouris (The University of Manchester), Yuechen Jiang (The University of Manchester), Lingfei Qian (The Fin AI), Yuyan Wang (The University of Manchester), Xueqing Peng (The Fin AI), Jimin Huang (The University of Manchester & The Fin AI), Guojun Xiong (Harvard University), Sophia Ananiadou (The University of Manchester & Archimedes/Athena RC)
- **arXiv Identifier:** arXiv:2605.01954v1 [cs.AI, cs.CL, cs.MA]
- **Submission Date:** 3 May 2026 16:37:52 UTC
- **Canonical DOI:** https://doi.org/10.48550/arXiv.2605.01954
- **Canonical URL:** https://arxiv.org/abs/2605.01954
- **HTML Full Text:** https://arxiv.org/html/2605.01954v1
- **PDF Primary Source:** https://arxiv.org/pdf/2605.01954v1
- **Primary source inspection:** Full 13-page text, formulas, Tables 1–8, and Appendices A–F inspected directly via PDF and HTML representations. All quantitative metrics, prompts, baseline comparisons, and ablation numbers trace directly to explicit locations in the primary source document.

## Economic mechanism

### Source-reported

The authors formulate pair trading as a hierarchical sequential decision-making problem with two distinct temporal and semantic layers:
1. **High-Level Abstraction (Pair Selection):** Operates on a coarse, episodic time scale (e.g. monthly), selecting an asset pair based on fundamental economic commonalities, long-horizon co-movement, and news/sentiment alignment across the universe.
2. **Low-Level Control (Trade Execution):** Operates on a fine, intra-episode time scale (daily), executing market-neutral long/short positions, managing entries, profit protection, trailing stops, and exits under short-horizon price fluctuations.

The central problem identified is **ambiguous credit assignment**: when a pair trading strategy loses money, conventional scalar rewards cannot disambiguate whether failure was caused by a flawed abstraction (the chosen stocks do not share a true economic relationship), suboptimal execution (poor entry timing or loose stops), or transient noise.

To solve this, the authors propose a **language-driven hierarchical reinforcement learning framework (Moira)** where:
- Both the high-level Selector and the low-level Trader are parameterized as prompt-conditioned Large Language Models (LLMs) whose parameters remain completely frozen.
- Policy optimization is conducted entirely in natural language prompt space via "textual gradients" produced by critic LLMs evaluating executed trajectories.
- The high-level Selector receives delayed, aggregated cumulative return feedback across the episode, refining pair selection heuristics.
- The low-level Trader performs intra-episode prompt optimization across sub-episodes (e.g. weekly), incorporating trajectory critiques into its mutable `POLICY` prompt block.
- Language acts as a semantic attribution interface, explicitly isolating failure modes (e.g., distinguishing between bad fundamental pairs versus bad entry timing) without cross-level gradient interference or catastrophic forgetting.

### Research interpretation

This is a **hybrid/composite statistical arbitrage and semantic reasoning hypothesis**. It marries two complementary alpha drivers:
1. **Semantic Regime & Commonality Discovery:** Pure price-based cointegration (e.g., Engle-Granger) and distance methods (e.g., Gatev et al.) are prone to finding spurious statistical co-movement that collapses out-of-sample or during structural breaks. Conditioning pair selection on multi-modal textual news and company fundamentals filters out spurious correlation and isolates assets sharing structural industry exposure (e.g., Amazon and Meta advertising/cloud dynamics).
2. **Dynamic Rule-Evolving Execution:** Rather than relying on static z-score Bollinger bands, the execution policy systematically develops risk-management heuristics (trailing stops, cooldown periods, news-catalyst divergence confirmation) derived from recent trade post-mortems.

The underlying economic thesis is that mean reversion in equity spreads is conditional on **fundamental economic co-dependence**: when spreads diverge without a divergent fundamental shock, mean reversion is probable; when spreads diverge due to a thesis break, holding through divergence incurs ruinous drawdowns. The LLM critic identifies whether divergent news warrants exiting immediately or waiting for reversion.

## Signal

### Formation timestamp

- **Observation schedule (source-reported):** Daily frequency using daily adjusted close prices from Yahoo Finance API. Textual news articles collected prior to daily market close from OpenAI Web Search, Finnhub, NewsData.io, and yfinance, summarized daily into a compact representation via GPT-5-nano.
- **Execution timestamp (`research-proposed`):** End-of-day market close (MOC) or next-day market open (MOO), assuming signal formation completes post-news summarization at daily market close. Timezone: US Eastern (America/New_York).

### Lookback

- **High-level Selector (source-reported):** Evaluated over a 30-day initial context window (beginning January 1, 2025) summarizing historical price dynamics and news sentiment across the universe.
- **Low-level Trader (source-reported):** Weekly sub-episode trajectories ($K_e$ sub-episodes per monthly episode), observing recent spread dynamics, open position states (entry price, share count), and daily news summaries.
- **Warm-up period (`research-proposed`):** 30 trading days of historical daily prices and news summaries.

### Entry

The Trader LLM receives structured JSON observations and emits an action from permissible actions:
- `long`: Long the first ticker, short the second ticker (market-neutral pair, sized by hedge ratio).
- `short`: Short the first ticker, long the second ticker.

The exact entry logic evolved across prompt update steps $k=0$ through $k=5$ (source Table 8):
- **Step $k=0$:** Enter only when the spread demonstrates sustained divergence (>2-day trend) accompanied by a clear news catalyst.
- **Step $k=1$:** Avoid entering if the spread has moved >2% over the prior 3 days without a fresh catalyst; require clear recent news divergence aligned with the spread move; wait for a pullback or consolidation before entry if the spread is trending.
- **Step $k=2$ (Event risk):** Avoid entering or adding to positions prior to major scheduled events (e.g., earnings announcements) if the spread has already moved >1.5%.
- **Step $k=3$ (Anti-overtrading):** Do not re-enter the same pair and direction for at least 2 trading days following an exit unless a major new catalyst emerges; require significant change in fundamental drivers before re-establishing a closed position.
- **Step $k=4$ (Signal quality filter):** Avoid entering when both stocks exhibit similar sentiment; require clear news divergence.
- **Step $k=5$ (Catalyst-driven fast response):** Enter immediately upon clear catalyst-driven news divergence aligned with spread movement, without waiting for prolonged (>2 days) sustained divergence confirmation.
- **Hedge ratio calculation (`research-proposed`):** OLS regression of log prices over the 30-day rolling window: $\log(P_{1,t}) = \alpha + \beta \log(P_{2,t}) + \epsilon_t$, where $\beta$ defines the dollar/share hedge ratio.

### Exit

The Trader LLM selects between:
- `close`: Exit to flat (close both legs simultaneously).
- `hold`: Keep current positions unchanged.

The exact exit logic evolved across prompt update steps (source Table 8):
- **Step $k=0$:** Hold through minor price reversals. Exit only if the economic thesis breaks or the spread moves >2% against entry. Do not exit based solely on a single-day adverse price fluctuation.
- **Step $k=2$ (Profit protection):**
  - Trailing stop: Exit if spread retraces 1.5% after exceeding 3% unrealized profit.
  - Partial profit-taking: Close 50% of position after >3% gain in 3 days.
  - Maximum holding period guideline: Approximately 5 trading days for news-driven trades.
- **Step $k=4$ (Dynamic reassessment):** Reassess thesis daily; if momentum stalls after 3–5 days in profit, consider exiting even if profit threshold is not reached. Replace fixed 5-day holding period with dynamic thesis-based reassessment after 3–5 days.
- **Step $k=5$ (Tighter protection):** Lower trailing stop trigger threshold from 3% to 2% (exit if retraces 1.5% after reaching 2% unrealized gain). Lower partial profit-taking threshold from 3% to 2%.

### Holding period

- **Source-reported:** Typical holding period of 3 to 5 trading days; reassessed daily; positions forced flat upon thesis breakdown or trailing stop activation.
- **Maximum hard time-stop (`research-proposed`):** 10 trading days to prevent capital stagnation during spread widening.

### Parameters

- **Underlying policy LLM (source-reported):** DeepSeek-V3.2 API, queried at temperature $T = 0$ to ensure deterministic responses.
- **News summarizer LLM (source-reported):** GPT-5-nano for consolidating daily multi-source textual streams into a unified representation.
- **Episode / Sub-episode structure (source-reported):** Episodes = 1 month; Sub-episodes = 1 week; Update steps = $K=0$ to $K=5$.
- **Critic prompt constraints (source-reported):** Trader critic output limited to $\le 12$ lines; Selector critic limited to $\le 10$ lines; outputs constrained to valid JSON action schema.
- **Position sizing (`research-proposed`):** Standardized $100,000 gross allocation ($50,000 long leg / $50,000 short leg) per pair trade.

## Required data

- **Instruments (source-reported):** Fixed universe of 10 liquid U.S. equities (source Table 6):
  - AAPL (Apple Inc., Consumer Electronics)
  - ADBE (Adobe Inc., Software)
  - AMZN (Amazon.com, Inc., E-Commerce)
  - BMRN (BioMarin Pharmaceutical Inc., Biotechnology)
  - CRM (Salesforce, Inc., Enterprise Software)
  - GOOGL (Alphabet Inc., Internet Services)
  - META (Meta Platforms, Inc., Internet Services)
  - MSFT (Microsoft Corporation, Enterprise Software)
  - NVDA (NVIDIA Corporation, Semiconductors)
  - TSLA (Tesla, Inc., Automotive)
  - *Primary traded pair in main evaluation:* AMZN / META.
- **Venue (source-reported):** U.S. Equity markets (NASDAQ / NYSE). Price data retrieved via Yahoo Finance API; news data from OpenAI Web Search, Finnhub, NewsData.io, yfinance.
- **Market type:** Cash Equity (spot long/short).
- **Timeframe:** Daily bars (daily adjusted close).
- **Fields:** Adjusted Close prices; daily aggregated news headlines and body text published prior to market close.
- **Point-in-time constraints (source-reported):** All news collected strictly prior to daily market close; no future data leakage into the daily decision state.
- **Missing-data handling (`research-proposed`):** If a stock halt or missing price occurs, hold existing position; do not enter new positions if daily news summary is empty or prices are unquoted.

## Execution assumptions

- **Execution timing (`research-proposed`):** Daily closing auction (MOC) or opening auction of subsequent day (MOO).
- **Order types (`research-proposed`):** Market orders executed simultaneously across both legs to maintain beta neutrality.
- **Fill model (source-reported):** Full fill at recorded daily adjusted close prices.
- **Transaction costs (source gap / provenance limitation):** The primary paper **does not incorporate transaction costs, bid-ask spreads, commissions, or short-borrow fees** in its backtest calculations.
- **Realistic cost overlay (`research-proposed`):** 5 bps per leg commission, 5 bps slippage per trade, and 1.5% annualized short-borrow fee on the short leg.
- **Leverage / Margin (`research-proposed`):** 100% margin (1x gross leverage: 100% cash reserve supporting the short leg and long leg under Regulation T).
- **Capacity (`research-proposed`):** High for mega-cap tech stocks (AMZN/META ADV > $5B/day); strategy capacity constrained primarily by LLM API latency/throughput rather than market depth.

## Evidence

### Source-reported

All figures below are directly extracted from the primary paper text and tables (arXiv:2605.01954v1). Evaluation period: January 1, 2025 to June 1, 2025 (5 months).

#### 1. Main Performance Comparison (Table 1)

| Model / Baseline | Annualized Return (AR %) ↑ | Sharpe Ratio (SR) ↑ | Sortino Ratio ↑ | Calmar Ratio (CR) ↑ | Max Drawdown (MDD %) ↓ | Annualized Volatility (AV %) ↓ | CVaR (95 %) ↑ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| GGR (Gatev et al. 2006 distance) | -9.550 | -0.800 | -1.557 | -1.287 | 7.420 | 14.150 | -1.540 |
| Correlation / Cointegration | +21.380 | 1.218 | 1.270 | 4.181 | 5.110 | 15.290 | -2.370 |
| TRIALS (Han et al. 2023 RL) | -4.700 | -0.125 | -0.550 | -0.750 | 6.280 | 17.192 | -4.800 |
| Flat-LLM (Non-hierarchical agent) | -7.690 | -0.403 | -0.450 | -0.885 | 8.690 | 20.370 | -3.270 |
| Moira-selection (Correlation pair + tuned trader) | -17.100 | -1.750 | -1.298 | -2.315 | 7.390 | 11.680 | -2.070 |
| Moira-tuning (Untuned base prompt trader) | +17.630 | 0.968 | 1.847 | 2.497 | 7.060 | 16.070 | -1.552 |
| **Moira (Fully tuned hierarchical)** | **+59.110** | **3.791** | **9.637** | **34.777** | **1.700** | **12.040** | **-0.800** |

*Note: In source Table 1, higher values are better for AR, SR, Sortino, Calmar, and CVaR; lower values are better for MDD and AV.*

#### 2. Pair Selection Controlled Isolation (Table 2 & Table 3)

- **Table 2:** Standard baselines evaluated on the Moira Selector's chosen pair (AMZN/META):
  - AR = 37.08%, SR = 0.875, Sortino = 1.245, MDD = 24.29%.
  *(Demonstrates that the Selector's chosen pair substantially improved raw baseline returns from 21.38% to 37.08%, but without the tuned trader MDD reached 24.29%).*
- **Table 3:** Performance of the fixed tuned Trader policy evaluated across alternative candidate pairs:
  - AMZN / META: AR = 59.09%, SR = 2.46, MDD = 7.87%
  - GOOGL / MSFT: AR = 12.26%, SR = 0.72, MDD = 9.13%
  - ADBE / AMZN: AR = 5.89%, SR = 0.26, MDD = 6.96%
  - MSFT / NVDA: AR = -4.21%, SR = -0.16, MDD = 13.26%
  - AMZN / TSLA: AR = -17.10%, SR = -1.75, MDD = 7.39%

#### 3. Prompt Initialization Robustness (Table 4)

Sensitivity across paraphrased prompt initializations (Mean ± Std):
- AR = 14.39% ± 6.97%
- SR = 1.00 ± 0.50
- Sortino = 1.13 ± 0.63
- Calmar = 4.22 ± 2.86
- MDD = 4.46% ± 2.43%
- CVaR (95%) = -1.84% ± 0.42%

#### 4. Trade Execution Statistics (Table 5)

Comparison of trade-level outcomes with and without prompt tuning:
- **Untuned Trader:** Win Rate = 46.67%, Mean Win = 1.44% ± 1.67%, Mean Loss = -0.98% ± 0.61%, Profit Factor = 1.37.
- **Tuned Trader:** Win Rate = 48.15%, Mean Win = 1.69% ± 1.17%, Mean Loss = -0.48% ± 0.29%, Profit Factor = 3.26.
*(Tuning primarily altered payoff asymmetry: average loss was halved from -0.98% to -0.48%, raising Profit Factor from 1.37 to 3.26 without relying on a substantial shift in win rate).*

#### 5. Computational Token Consumption (Table 7)

- Trader action inference: 30 calls, ~11.6k tokens/call, ~347k total.
- Trader critic (textual gradient): 6 calls, ~12.2k tokens/call, ~73k total.
- Selector action: 3 calls, ~57.6k tokens/call, ~173k total.
- Selector critic: 3 calls, ~57.8k tokens/call, ~173k total.
- Total token overhead: ~766k tokens across the evaluation horizon.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Extreme Pair Fragility (source Table 3):** Under the exact same tuned Trader policy, performance collapses when applied to other pairs (e.g. AMZN/TSLA produced AR -17.10% and SR -1.75; MSFT/NVDA produced AR -4.21% and SR -0.16). Profitability is highly sensitive to the initial pair selection.
2. **Selector Failure Severity (source Table 1):** When the LLM selector is replaced by correlation-based selection (Moira-selection), the strategy incurs an annualized return of -17.10% and Sharpe of -1.750, indicating that the execution policy cannot compensate for a poor pair choice.
3. **Zero Cost Friction:** The paper assumes zero commissions, zero market impact, zero borrow cost, and execution at exact closing prices. In reality, a strategy taking trades with an average win of 1.69% and holding for 3–5 days can lose a substantial portion of edge to round-trip bid-ask spreads (typically 2–5 bps each on 2 legs = 8–20 bps round trip) and short borrow fees.
4. **Short Sample Window:** The empirical evaluation spans only 5 months (January 1 to June 1, 2025) across 10 stocks, which is insufficient to establish statistical significance across market cycles or recessions.

## Falsification plan

To falsify the claim that language-driven hierarchical RL extracts genuine statistical arbitrage alpha:

1. **Extended Out-of-Sample Walk-Forward Test:**
   - Run the full Moira framework across 2020–2024 (encompassing the 2020 liquidity shock, 2021 bull market, 2022 rate-hike bear market, and 2023 tech rally).
   - *Failure condition (`research-defined falsification threshold`):* Out-of-sample annualized Sharpe ratio falls below 0.50 or maximum drawdown exceeds 20.0% net of transaction costs.
2. **Transaction Cost & Borrow Stress Test:**
   - Re-evaluate the strategy applying realistic execution frictions: 5 bps commission per leg, 5 bps half-spread slippage, and 2.0% annual borrow fee on the short leg.
   - *Failure condition (`research-defined falsification threshold`):* Profit factor drops below 1.15 or cumulative return turns negative.
3. **Ablation of News Context (Price-Only Control):**
   - Provide the Trader and Selector critics only price series and mathematical spread metrics, stripping all textual news and sentiment summaries.
   - *Failure condition (`research-defined falsification threshold`):* If the price-only agent achieves equivalent or superior Sharpe ratio compared to the multimodal agent, the core thesis that LLMs contribute semantic fundamental alpha is falsified.
4. **Counterfactual Pair Assignment Test:**
   - Force the tuned Trader to execute across 20 randomly selected non-cointegrated pairs.
   - *Failure condition (`research-defined falsification threshold`):* If the tuned execution policy generates positive Sharpe on randomly paired stocks, the alpha originates from trend-following/momentum bias rather than relative-value pairs cointegration.
5. **Prompt Permutation / Noise Test:**
   - Introduce synthetically degraded or shuffled news headlines.
   - *Failure condition (`research-defined falsification threshold`):* Performance does not decay by at least 30% under corrupted news, indicating the agent ignores news semantic content and hallucinates correlation.

## Crypto portability

**Adapted / Unproven**

The primary paper evaluates exclusively U.S. equities (NASDAQ/NYSE). Porting this mechanism to cryptocurrency markets is **unproven** and requires adaptation:

### Adaptation requirements
1. **Universe & Pair Selection:** Rather than equities, candidate pairs could be formed among liquid altcoins (e.g. SOL/ETH, AVAX/SOL, ARB/OP) or cross-exchange funding spreads.
2. **Data Pipeline:** News headlines would need to be replaced or supplemented by crypto-native information streams (crypto news APIs, Twitter/X sentiment, governance forum announcements, GitHub commit activity, and on-chain metrics such as active addresses, whale transfers, and DEX pool depth).
3. **Market Structure Differences:**
   - **24/7 Trading:** The daily bar close concept does not exist; hourly or 4-hour evaluation cycles must be defined (`research-proposed`).
   - **Perpetual Futures & Funding:** Unlike equities, crypto relative-value trading is typically executed via perpetual swaps. Funding rate differentials introduce a continuous carry cost or yield that must be explicitly incorporated into the Trader's reward and state representation.
   - **Exchange Fragmentation & Liquidity Disparities:** Spread divergence often reflects exchange-specific liquidation cascades rather than fundamental divergence; the agent risks entering "toxic" spreads that widen indefinitely.

*Porting this strategy to crypto must be treated as a pure research hypothesis without verified empirical validity.*

## Limitations

- **Source Provenance Gaps:** Zero transaction fees, slippage, or borrowing costs modeled in the paper.
- **Microscopic Sample Universe:** Tested only on a 10-stock basket, with primary execution results demonstrated on a single pair (AMZN/META).
- **Short Horizon:** 5-month test period in 2025 constitutes a very small statistical sample (~105 trading days).
- **Execution Vagueness:** Exact order execution mechanism (MOC vs MOO vs VWAP) and order-book fill modeling are not specified by the source.
- **Inference Latency and Cost:** Dependency on multi-turn LLM queries (DeepSeek-V3.2 and GPT-5-nano) introduces API latency, token expense, and potential service outages.
- **Non-Stationary LLM Weights:** Relying on commercial LLM APIs introduces API drift risks over long backtests.

## Implementation status

`not-implemented`

No implementation currently exists in our research stack (`nautilus-quant-system`, PyBroker, or NautilusTrader). Reproduction would require:
1. Setting up daily Yahoo Finance price data and multi-source news aggregation pipelines.
2. Implementing the contextual bandit Selector prompt loop and the intra-episode textual policy gradient Trader update loop.
3. Integrating DeepSeek-V3.2 API endpoints with deterministic temperature settings.

## Adoption boundary

This record is research material only. It does not represent:
- Validated alpha
- Profitable strategy
- Approval for implementation
- Approval for paper trading
- Approval for testnet
- Approval for live trading

## Related Wiki records

- [[quant/exploratory-reinforcement-learning-sequential-optimal-stopping-pairs-trading-2026-09-05]] — explores reinforcement learning for pairs trading optimal stopping boundaries; complementary parametric execution benchmark.
- [[quant/graphical-matching-pairs-trading-maximum-weight-matching-2026-09-05]] — combinatorial graph matching for multi-pair selection; alternative mathematical pair selection framework.
- [[quant/model-free-statistical-arbitrage-empirical-mean-reversion-time-reinforcement-learning-2026-09-05]] — model-free RL statistical arbitrage; contrasts parametric vs non-parametric policy optimization.
- [[quant/meta-rl-crypto-self-improving-meta-reward-trading-agent-2026-09-05]] — meta-reinforcement learning self-improving LLM trading agent; shares LLM prompt optimization and multi-modal integration.
- [[quant/multimarket-senseai-multi-agent-llm-regime-adaptive-equity-selection-2026-09-04]] — multi-agent LLM framework for equity selection; shares news and market sentiment integration.

## Sources

1. Polydoros Giannouris, Yuechen Jiang, Lingfei Qian, Yuyan Wang, Xueqing Peng, Jimin Huang, Guojun Xiong, Sophia Ananiadou. "Moira: Language-driven Hierarchical Reinforcement Learning for Pair Trading." arXiv:2605.01954v1 [cs.AI, cs.CL, cs.MA], submitted 3 May 2026. DOI: 10.48550/arXiv.2605.01954. https://arxiv.org/abs/2605.01954
