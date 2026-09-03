---
schema: strategy-research-record-v1
title: "AlphaCrafter: Harness-Driven Multi-Agent LLM Framework for Cross-Sectional Equity Alpha Discovery and Portfolio Execution"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - llm-agentic
  - cross-sectional
  - equity
  - multi-agent
  - factor-discovery
status: research-only
confidence: medium
source_as_of: 2026-09-03
sources:
  - "Yishuo Yuan, Jiayi Sheng, Sirui Zeng, Jiaqi Wang, Jiaheng Liu, 'AlphaCrafter: Harnessing Multi-Agent Workflows for Cross-Sectional Quantitative Trading', arXiv:2605.05580v2 [cs.AI], submitted May 7 2026, revised July 28 2026. Submitted to AAAI 2027. https://arxiv.org/abs/2605.05580"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# AlphaCrafter: Harness-Driven Multi-Agent LLM Framework for Cross-Sectional Equity Alpha Discovery and Portfolio Execution

## Provenance

- **Primary Paper:** Yishuo Yuan, Jiayi Sheng, Sirui Zeng, Jiaqi Wang, Jiaheng Liu, *"AlphaCrafter: Harnessing Multi-Agent Workflows for Cross-Sectional Quantitative Trading"*, arXiv preprint `arXiv:2605.05580v2 [cs.AI]`, first submitted May 7 2026, revised July 28 2026. Submitted to AAAI 2027. DOI: [10.48550/arXiv.2605.05580](https://doi.org/10.48550/arXiv.2605.05580). Full text: [https://arxiv.org/abs/2605.05580](https://arxiv.org/abs/2605.05580), HTML: [https://arxiv.org/html/2605.05580v2](https://arxiv.org/html/2605.05580v2).
- **Code Repository:** No public code repository identified as of source as-of date. The paper does not reference an open-source implementation.

## Economic mechanism

### Source-reported

AlphaCrafter proposes a harness-driven multi-agent framework that automates the full factor-to-execution pipeline for cross-sectional quantitative trading. The framework is motivated by the observation that existing LLM-based trading agents rely on loosely specified natural-language workflows, leading to opaque reasoning, inconsistent behaviors across foundation models, and limited controllability. The key insight is that the *execution harness* — programmable policy specifications, execution constraints, and verification mechanisms — surrounding an LLM can be as important as the underlying model itself. The system operates via three coordinated agent clusters:

1. **Miner Cluster:** LLM agents autonomously generate candidate quantitative factors from market data, validate them against historical data using IC/Rank IC/ICIR metrics, and maintain a dynamic factor library with pruning of decaying factors.
2. **Screener:** An LLM agent diagnoses the current market regime (trend, volatility, correlation structure), evaluates semantic relevance of each factor to the diagnosed regime, computes suitability scores from recent Rank IC, and assembles a diversified factor ensemble with directional weights.
3. **Trader:** An LLM agent explores hyperparameter configurations of a reference top-K long-short strategy via backtesting, selects the configuration maximizing Sharpe ratio subject to risk constraints, and executes the portfolio.

The three agents share both in-context memory (immediate market awareness) and persistent long-term memory (archived trading trajectory, factor performance, and executed strategies). The regime-aware screening and adaptive de-risking emerge from the coordinated harness constraints without explicit volatility-targeting rules.

### Research interpretation

The core alpha hypothesis is that LLM-driven factor generation can discover novel, regime-appropriate quantitative signals that survive systematic validation, and that harness-structured multi-agent execution produces more stable and reproducible results than prompt-driven approaches. The economic mechanism is:

- **Factor novelty:** LLM agents can explore a broader space of factor expressions than traditional formulaic approaches (Alpha158 etc.), potentially discovering signals with unexploited alpha in cross-sectional equity returns.
- **Regime conditioning:** The Screener agent dynamically selects factors based on current market regime, providing a systematic adaptation mechanism that static factor models lack.
- **Cross-agent coordination:** The Miner-Screener-Trader pipeline introduces structured verification at each stage, filtering out overfitted or regime-inappropriate factors before they reach portfolio construction.

The reference strategy is a top-K long-short cross-sectional equity portfolio: for each trading day, a composite score is built from the factor ensemble, the top N_long assets go long and bottom N_short go short, with position sizing controlled by gross exposure β and net exposure bias γ, rebalanced at each market close.

## Signal

- **Formation timestamp:** Daily, at market close (end-of-day rebalancing). The Miner generates factors, the Screener diagnoses regime and selects factors, and the Trader searches hyperparameters and executes — all at daily frequency.
- **Lookback:** Factor expressions use a configurable lookback window ℓ over raw OHLCV features. The state representation includes a 60-day lookback of past asset returns, 20-day and 60-day rolling volatilities and their ratio, VXD (volatility index), and factor-specific historical data.
- **Entry (long):** Top N_long assets by composite factor score (weighted combination of selected factors with directional signs).
- **Entry (short):** Bottom N_short assets by composite factor score.
- **Exit:** Daily rebalancing; positions are liquidated and re-established at each market close based on updated factor scores and regime diagnosis.
- **Holding period:** 1 trading day (daily rebalance).
- **Parameters:** Hyperparameters are searched via LLM-guided backtesting at each rebalance. Key parameters include gross exposure β, net exposure bias γ, N_long, N_short, and factor ensemble weights. The LLM samples configurations conditioned on the diagnosed regime and selects the one maximizing Sharpe ratio subject to risk constraints (research-defined search procedure).
- **Position sizing:** Controlled allocation with gross exposure cap and net exposure bias. The Trader harness searches for the optimal configuration within a feasible region S_Θ (research-defined).

## Required data

- **Instrument / Universe:** CSI 300 constituents (Chinese A-shares) and S&P 500 constituents (U.S. equities).
- **Venue:** Not specified; paper-trading API from a real brokerage used for live trading phase.
- **Market type:** Equities (spot); daily frequency.
- **Timeframe:** Daily bars (OHLCV).
- **Fields:** Daily OHLCV (Open, High, Low, Close, Volume); fundamental indicators (PE, PS, PB, Dividend Yield Rate); financial statements (quarterly balance sheets, income statements, cash flow statements); alternative data (financial news and corporate announcements including authoritative sources such as the Federal Reserve).
- **Point-in-time:** Training: 2016.01.04–2022.12.30; Validation: 2023.01.03–2023.12.29; Backtesting: 2024.01.02–2026.02.27; Live trading: 2026.03.02–2026.06.12. LLM backbone training cutoff falls before the live trading window.
- **Timestamp:** Daily frequency; timezone alignment not explicitly stated.
- **Missing data:** Not explicitly addressed in the paper.
- **Funding/fee/spread:** Abstracted in backtesting (see Execution assumptions).

## Execution assumptions

- **Signal-to-order timing:** End-of-day rebalancing; portfolio weights updated at each market close.
- **Order type:** Market orders assumed (paper-trading API).
- **Fill model:** Not explicitly modeled in backtesting. Live trading uses real brokerage paper-trading API with actual market order execution mechanics.
- **Fees:** Abstracted in backtesting with fixed commission rates (research-defined assumption).
- **Slippage:** Abstracted in backtesting with symmetric, zero-mean slippage (research-defined assumption). The authors acknowledge this may not hold during market stress or for larger order sizes.
- **Spread:** Not modeled in backtesting.
- **Impact:** Not modeled in backtesting. The authors acknowledge price impact of trading illiquid index constituents is a limitation.
- **Capacity:** Not explicitly addressed. The paper notes that larger order sizes may face non-trivial frictions.
- **Leverage / margin:** Not explicitly stated; net exposure bias γ controls directional tilt.
- **Latency:** Daily frequency; intraday latency not relevant.
- **Partial fills / failures:** Not addressed.

## Evidence

### Source-reported

Source reports the following results on CSI 300 and S&P 500, grouped by backbone (primary source fixed to arXiv:2605.05580v2, 2026-07-28, Section 3.2 Table 2; Table 2 is organized by three backbone groups — not a single aggregate AlphaCrafter row — and figures below preserve the original three AlphaCrafter rows in backbone order):

Backtesting window 2024.01.02–2026.02.27 and Live trading window 2026.03.02–2026.06.12, columns ordered as CSI300 Backtest AR/SR/MDD, S&P500 Backtest AR/SR/MDD, CSI300 Live AR/SR/MDD, S&P500 Live AR/SR/MDD.

| Backbone | CSI300 Backtest AR (%) | CSI300 Backtest SR | CSI300 Backtest MDD (%) | S&P500 Backtest AR (%) | S&P500 Backtest SR | S&P500 Backtest MDD (%) | CSI300 Live AR (%) | CSI300 Live SR | CSI300 Live MDD (%) | S&P500 Live AR (%) | S&P500 Live SR | S&P500 Live MDD (%) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GPT 5.3 Codex | 16.76 | 1.5268 | -8.98 | 13.51 | 1.2531 | -8.85 | 9.57 | 1.1275 | -9.07 | 14.02 | 1.4546 | -9.06 |
| Claude Opus 4.6 | 18.88 | 1.6732 | -8.48 | 15.66 | 1.3425 | -7.98 | 10.70 | 1.1902 | -8.21 | 16.26 | 1.6012 | -9.53 |
| Gemini 3.1 Pro | 17.22 | 1.4852 | -9.27 | 14.52 | 1.3126 | -8.65 | 9.91 | 1.2001 | -8.17 | 14.25 | 1.4008 | -8.89 |

Provenance: each exact number traces to arXiv:2605.05580v2 Section 3.2 Table 2, row identity = backbone (GPT 5.3 Codex / Claude Opus 4.6 / Gemini 3.1 Pro), column identity = market × phase (Backtest/Live) × metric (AR/SR/MDD).

Source reports that AlphaCrafter achieves the highest Sharpe ratio across all baselines in backtesting and maintains favorable live-trading performance within each backbone group. Ablation experiments show that removing the Miner, Screener, or Trader component degrades performance. Cross-model stability study across the three backbones (GPT 5.3 Codex, Claude Opus 4.6, Gemini 3.1 Pro) shows AlphaCrafter exhibits lower cross-model and cross-trial variance than role-playing agent baselines. Live trading uses a paper-trading API from a real brokerage with actual market order execution.

All source-reported figures above are from the primary paper (arXiv:2605.05580v2, Section 3.2 Table 2). This result has not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Live trading AR is lower than backtesting AR for CSI300 across all three backbones in Table 2 (backtest 16.76–18.88% vs live 9.57–10.70%) and shows a smaller gap/mixed pattern for S&P500, suggesting potential backtest-to-live degradation, although the live period is short (69–73 trading days).
- The authors acknowledge LLM data leakage concern: backbone LLMs may have encountered market data during pre-training that overlaps with the backtesting period. Live trading is designed to be outside the training cutoff, but backtesting results should be interpreted with caution.
- Cross-model sensitivity: while AlphaCrafter shows lower variance than baselines, the study is limited to three frontier LLMs; generalizability to smaller or open-source models is unverified.
- The paper notes that the framework does not address futures, options, or cryptocurrency markets, which have fundamentally different factor definitions, regime dynamics, and execution constraints.

## Falsification plan

1. **Out-of-sample extension:** Extend the live-trading period beyond the current 69–73 trading days to assess whether the live Sharpe ratio stabilizes or degrades further. Required sample: ≥250 trading days of live execution.
2. **Transaction cost stress:** Re-run backtesting with realistic transaction costs: time-varying bid-ask spreads, market impact models, and partial fill assumptions. Failure threshold: if post-cost Sharpe drops below 0.5, the framework's alpha is not robust to execution frictions.
3. **Cross-model ablation with open-source LLMs:** Replicate with smaller or open-source models (Llama, DeepSeek). Failure: if Sharpe degrades by >50% relative to frontier models, the framework's performance depends on proprietary model capabilities rather than the harness design.
4. **Regime breakdown:** Evaluate performance separately in high-volatility vs low-volatility regimes, bull vs bear markets. Failure: if the regime-aware Screener does not outperform equal-weight factor allocation in any single regime, the regime conditioning adds no value.
5. **Factor decay monitoring:** Track whether LLM-generated factors exhibit alpha decay over time. Failure: if factor library requires constant regeneration (high turnover) to maintain performance, the system is overfit to recent conditions.
6. **Crypto portability test:** Adapt the Miner-Screener-Trader pipeline to a crypto cross-sectional universe (top-N altcoins by market cap). Failure: if the harness design does not transfer without fundamental restructuring, the framework is equity-specific rather than generalizable.

## Crypto portability

unproven

The paper explicitly states that extending to cryptocurrency markets is future work. The authors note that "factor definitions, regime dynamics, and execution constraints differ fundamentally in futures, options, and cryptocurrency markets," particularly citing "high-leverage and contract-specific microstructure that characterize derivatives trading."

Crypto portability risks:
- **Universe differences:** CSI 300 / S&P 500 are large-cap equity indices with deep liquidity; crypto cross-sectional universes have different liquidity profiles, survivorship, and listing dynamics.
- **Regime dynamics:** Crypto markets have 24/7 sessions, different volatility clustering patterns, and funding rate dynamics absent in equities.
- **Factor relevance:** Fundamental factors (PE, PS, PB, financial statements) are largely absent or unreliable in crypto; the Miner would need to discover entirely different factor expressions (on-chain, order flow, funding, sentiment).
- **Execution:** Daily rebalancing is well-suited for equities but may be too slow for crypto alpha decay; intraday or sub-hourly adaptation may be needed.
- **LLM data leakage:** Crypto-specific market data may be less represented in LLM pre-training, potentially reducing the Miner's ability to generate relevant factor hypotheses.

The harness-driven architecture (programmable policies, verification mechanisms) is conceptually transferable, but the specific factor library, regime diagnosis, and reference strategy would require complete re-engineering for crypto.

## Limitations

- **Equity-only empirical evidence:** All experiments are on CSI 300 and S&P 500 equities. No crypto or derivatives results.
- **Abstracted transaction costs:** Backtesting uses fixed commissions and symmetric zero-mean slippage. Real-world execution may face time-varying spreads, market impact, and partial fills that could erode alpha.
- **LLM data leakage risk:** Backbone LLMs may have parametric knowledge of market outcomes during the backtesting period (2024–2026), creating potential look-ahead bias. Live trading is designed to mitigate this but covers a short window.
- **Short live-trading period:** 69–73 trading days is insufficient to assess long-horizon performance, regime robustness, or tail risk.
- **Dependence on proprietary LLMs:** The framework uses GPT 5.3 Codex, Claude Opus 4.6, and Gemini 3.1 Pro. Generalizability to open-source or smaller models is unverified.
- **No code release:** The paper does not reference a public code repository, limiting independent reproduction.
- **Backtest-to-live gap:** Live trading AR is materially lower than backtesting AR in both markets, suggesting the backtesting environment may overstate achievable returns.
- **Factor novelty does not guarantee alpha:** The paper's own factor novelty analysis shows that structurally novel factors (highest Φ_inter) do not monotonically translate into better trading outcomes, indicating that factor generation alone is insufficient without effective screening.
- **Not independently reproduced.**

## Implementation status

Not implemented in our research stack. No PyBroker, Nautilus, paper, testnet, or live verification has been conducted.

## Adoption boundary

This record is research material only. Presence in this repository does not mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

## Related Wiki records

- [[quant/aeap-seads-llm-agentic-factor-discovery-formulaic-alpha-2026-09-03]] — AEAP/SEADS focuses on LLM-agentic formulaic alpha mining with GRPO; AlphaCrafter is a full multi-agent harness framework with Miner-Screener-Trader pipeline for cross-sectional equity trading.
- [[quant/madevolve-evolutionary-alpha-forecasting-passive-limit-order-bitcoin-2026-09-03]] — MadEvolve uses evolutionary optimization for Bitcoin limit order execution; AlphaCrafter is equity-focused cross-sectional factor-based trading.
- [[quant/llm-multi-agent-multi-modal-crypto-portfolio-hierarchical-skill-rebalancing-2026-09-02]] — LLM Multi-Agent uses hierarchical skill-augmented rebalancing for crypto portfolios; AlphaCrafter uses harness-driven factor discovery for equity cross-sectional trading.

## Sources

1. Yishuo Yuan, Jiayi Sheng, Sirui Zeng, Jiaqi Wang, Jiaheng Liu, *"AlphaCrafter: Harnessing Multi-Agent Workflows for Cross-Sectional Quantitative Trading"*, arXiv preprint `arXiv:2605.05580v2 [cs.AI]`, submitted May 7 2026, revised July 28 2026. Submitted to AAAI 2027. DOI: [10.48550/arXiv.2605.05580](https://doi.org/10.48550/arXiv.2605.05580). Stable URL: [https://arxiv.org/abs/2605.05580](https://arxiv.org/abs/2605.05580). Full text HTML: [https://arxiv.org/html/2605.05580v2](https://arxiv.org/html/2605.05580v2).
