---
schema: strategy-research-record-v1
title: "LLM Multi-Agent Multi-Modal Crypto Portfolio Management: Hierarchical Skill-Augmented Rebalancing"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - LLM-multi-agent
  - multi-modal
  - portfolio-management
  - weekly-rebalancing
  - sentiment
  - market-dynamics
status: research-only
confidence: medium
source_as_of: 2026-09-02
sources:
  - "Yichen Luo, Yebo Feng, Jiahua Xu, Paolo Tasca, Yang Liu, 'LLM-Powered Multi-Agent System for Automated Crypto Portfolio Management', arXiv:2501.00826v3 [q-fin.TR / cs.AI], January 2025 (revised June 2026). DOI: 10.48550/arXiv.2501.00826. https://arxiv.org/abs/2501.00826"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# LLM Multi-Agent Multi-Modal Crypto Portfolio Management: Hierarchical Skill-Augmented Rebalancing

## Provenance

- **Primary Source:** Yichen Luo, Yebo Feng, Jiahua Xu, Paolo Tasca, Yang Liu, *"LLM-Powered Multi-Agent System for Automated Crypto Portfolio Management"*, arXiv preprint `arXiv:2501.00826v3 [q-fin.TR / cs.AI]`, January 2025 (revised June 2026). DOI: [10.48550/arXiv.2501.00826](https://doi.org/10.48550/arXiv.2501.00826). Full text: [https://arxiv.org/abs/2501.00826](https://arxiv.org/abs/2501.00826).
- **Code Repository:** Anonymous pre-publication repository at `https://anonymous.4open.science/r/cryptoMAS-FCB2/` (as of paper publication; may change post-acceptance).
- **Primary Subject Areas:** Trading and Market Microstructure (`q-fin.TR`), Artificial Intelligence (`cs.AI`).
- **Context:** The paper proposes a multi-agent system (MAS) framework in which three modality-specialised LLM agents — Crypto Agent (market dynamics), News Agent (weekly news sentiment), and Trading Agent (signal fusion and portfolio execution) — coordinate under hierarchical, collaborative, or debate communication architectures and four capability configurations (zero-shot, CoT, RAG, skill-augmented). Each agent uses a rolling memory window and ReAct-style prompting for traceable reasoning.

## Economic mechanism

### Source-reported

The authors hypothesise that cryptocurrency portfolio management requires fusing heterogeneous multi-modal signals — structured price/volume/on-chain time series, unstructured news text, and technical indicators — under high volatility. Single LLM agents struggle with the breadth of modality-specific inputs; decomposing the task across specialised agents with different communication architectures allows each agent to focus on its modality while the Trading Agent coordinates the portfolio action. The Crypto Agent is identified as the primary alpha driver; the News Agent functions principally as a risk-dampening mechanism; memory provides cross-week continuity.

### Research interpretation

The falsifiable thesis is that **multi-modal signal fusion via modality-specialised LLM agents with hierarchical skill-augmented coordination produces superior risk-adjusted returns on a top-15-L1-cryptocurrency portfolio compared to single-agent, deep learning, or passive benchmarks**:

1. **Crypto Agent (market dynamics):** Processes 30-day rolling windows of daily close, volume, and market cap for each asset. Hypothesised to capture trend and momentum signals via structured time-series reasoning.
2. **News Agent (sentiment):** Processes weekly news articles (Cointelegraph) for sentiment encoding. Hypothesised to provide risk-dampening via event awareness rather than directional alpha.
3. **Trading Agent (signal fusion):** Fuses Crypto Agent and News Agent outputs with portfolio state to produce weekly rebalancing actions. Hypothesised to benefit from hierarchical coordination where each specialist provides modality-specific input.
4. **Hierarchical (Skill) architecture:** Top-down coordination where the Trading Agent directs specialists; skill-augmented capability adds domain-specific tool use. Hypothesised to maximise bull-market returns while maintaining interpretability.

## Signal

- **Formation timestamp:** Weekly (ISO week boundaries). Each agent processes the prior week's data; the Trading Agent produces rebalancing actions at the start of the new week.
- **Lookback:** 30 daily observations (closing price, volume, market cap) per asset for the Crypto Agent; weekly news articles for the News Agent; rolling memory window for cross-week continuity.
- **Universe:** Top 15 L1-blockchain native cryptocurrencies by market capitalisation as of January 2025: BTC, ETH, BNB, XRP, SOL, TRX, ADA, BCH, HYPE, XMR, ZEC, LTC, SUI, AVAX, HBAR. Fixed throughout the backtest.
- **Entry:** Trading Agent produces a portfolio weight vector across the 15 assets based on fused signals. Rebalancing occurs weekly.
- **Exit:** Implicit via weekly rebalancing — positions are adjusted at each week boundary.
- **Holding period:** 1 week (7 days) between rebalances.
- **Parameters:** Temperature 0.0 (deterministic sampling); 30-day rolling window; weekly rebalancing cadence; top-15 universe fixed at January 2025 market cap ranking.
- **Position sizing:** Portfolio weight vector produced by the Trading Agent; specific sizing logic is agent-determined via ReAct reasoning, not pre-specified.
- **Re-entry rules:** Weekly rebalancing — positions adjusted at each week boundary.

## Required data

- **Instrument:** Top 15 L1-blockchain native cryptocurrencies by market cap (BTC, ETH, BNB, XRP, SOL, TRX, ADA, BCH, HYPE, XMR, ZEC, LTC, SUI, AVAX, HBAR).
- **Universe:** Top 15 L1 native tokens by market capitalisation as of January 2025. Fixed throughout the backtest period (no reconstitution).
- **Venue:** Not explicitly stated; price data sourced from CoinGecko; news from Cointelegraph.
- **Timeframe:** Daily OHLCV (close, volume, market cap) for Crypto Agent; weekly news articles for News Agent.
- **Fields:** Daily closing price, trading volume, market capitalisation (CoinGecko); weekly news article text (Cointelegraph).
- **Point-in-time:** Price data is market data (no revision risk). News articles are published during the prior week. No lookahead protection details provided beyond weekly rebalancing cadence.
- **Timestamp:** ISO weekly boundaries; daily observations for 30-day lookback.
- **Missing-data:** Not explicitly addressed.
- **Funding/fee/spread needs:** Source-reported transaction cost is 0.1% per trade side (see Execution assumptions); no additional funding/spread/slippage sensitivity beyond that is reported.

## Execution assumptions

- **Order type:** Assumed market orders for weekly rebalancing; not explicitly stated.
- **Fill model:** Assumed full fill at close-of-week prices; not explicitly stated.
- **Latency:** Weekly rebalancing cadence implies low latency requirements.
- **Signal-to-order timing:** Trading Agent produces rebalancing actions at week start based on prior week's data.
- **Fees/spread/slippage:** Source-reported: 0.1% transaction cost per trade side applied in the backtest (Methods). Spread/slippage beyond this fixed cost is not separately modelled; this remains a limitation for live-cost robustness.
- **Leverage/margin:** Not specified; assumed unleveraged.
- **Position limits:** Portfolio weight vector across 15 assets; no explicit position limits stated.

## Evidence

### Source-reported

All empirical figures below are directly reported by Luo et al. (arXiv:2501.00826v3, 2025):

- **Best configuration:** Hierarchical (Skill) — cumulative return +133.52%, Sharpe ratio +1.502 over 52-week backtest (calendar year 2025) across top 15 L1 cryptocurrencies.
- **Ablation — Crypto Agent removal:** Cumulative return drops by 42.57 percentage points to +9.62%; Sharpe collapses to +0.424; win rate falls to 50.0% (coin-flip).
- **Ablation — Memory removal:** Cumulative return drops by 11.47 percentage points (+40.72% vs +52.19%); Sharpe ratio reduces by 0.165.
- **Ablation — News Agent removal:** Cumulative return drops by only 0.88 percentage points; annualised volatility increases by 6.76 percentage points; win rate decreases by 3.80 percentage points — news functions as risk dampener, not alpha driver.
- **Cross-model comparison:** MAS outperforms single-agent baseline under GPT-4o, GPT-5, and Claude Sonnet 4.5; Claude achieves highest mean return across all 16 architecture–capability combinations.
- **Regime analysis:** Skill augmentation maximises bull-market returns; CoT minimises bear-market drawdowns; RAG grounding reduces volatility at cost of upside capture.
- **Baselines outperformed:** Passive hold, equal-weight, single-agent LLM, five deep learning forecasters.

These results have **not** been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Single-seed backtest:** All experiments use temperature 0.0 (deterministic) but only a single seed; the authors note that "a full multi-seed sweep across the grid, three backbones, and 52 weekly ReAct rollouts is cost-prohibitive under commercial API pricing" and leave seed-variance quantification to future work.
- **Transaction cost scope (source-reported vs research-proposed):** The backtest is source-reported with 0.1% per trade side transaction cost. No spread/slippage beyond that fixed cost is modelled. Weekly rebalancing across 15 crypto assets means live trading costs could exceed this assumption; sensitivity to higher cost assumptions remains untested (see Falsification plan research-proposed extension).
- **Survivorship bias in universe:** The top-15-L1 universe is fixed at January 2025 market cap ranking; no reconstitution or survivorship handling is described.
- **Single-year backtest:** 2025 calendar year only; no out-of-sample or cross-regime validation.
- **LLM API cost dependency:** The strategy requires ongoing LLM API calls (GPT-4o/GPT-5/Claude) for each weekly rebalancing, introducing cost and availability dependencies.
- **None identified in the reviewed sources for negative results on the MAS architecture itself; absence is not evidence of no negative result.**

## Falsification plan

1. **Transaction cost sensitivity (research-proposed extension beyond source-reported 0.1% per side):** Reproduce the backtest varying round-trip costs above the source-reported baseline (e.g. 20–30 bps round-trip, and with spread/slippage) to test robustness. **Failure rule (research-defined):** If the Sharpe ratio drops below 1.0 under moderately higher cost assumptions, the strategy's alpha is not cost-robust beyond the source's fixed-cost model.
2. **Multi-seed variance:** Run the Hierarchical (Skill) configuration across 10+ random seeds (or temperature > 0) and report the distribution of Sharpe ratios. **Failure rule:** If the 95% confidence interval of the Sharpe ratio includes zero, the result is not statistically robust.
3. **Out-of-sample extension:** Extend the backtest to 2024 or 2026 (if data available) with the same fixed universe. **Failure rule:** If the strategy underperforms equal-weight buy-and-hold in the out-of-sample period, the 2025 result is likely overfit.
4. **Universe reconstitution:** Re-run with quarterly universe reconstitution (top 15 by market cap each quarter) to test survivorship sensitivity. **Failure rule:** If performance degrades by more than 50%, the fixed universe is a material driver.
5. **Single-agent baseline comparison at equal cost:** Compare MAS against a single-agent LLM with the same total token budget allocated to a single agent. **Failure rule:** If the single-agent baseline achieves comparable Sharpe, the multi-agent coordination adds no incremental value.
6. **LLM provider sensitivity:** Replace GPT-5 with an open-weight model (e.g., Llama 3, Qwen 2.5) of similar parameter count. **Failure rule:** If performance collapses with an open model, the alpha is model-specific rather than architecture-specific.

## Crypto portability

**direct** — the strategy is natively designed for cryptocurrency markets.

- The universe is top-15 L1 native cryptocurrencies; the framework is purpose-built for crypto.
- Weekly rebalancing cadence aligns with crypto's 24/7 market structure.
- News sentiment from crypto-native sources (Cointelegraph) is modality-specific.
- **Crypto-specific risks:** High-frequency regime shifts in crypto may stale the 30-day rolling window; meme-coin/small-cap tokens outside the top-15 universe may offer higher alpha but are excluded; funding rates on perpetual futures are not modelled (spot-equivalent universe assumed).

## Limitations

- **Single-year backtest:** Only 2025 calendar year; no out-of-sample validation.
- **Transaction cost: source-reported 0.1% per trade side;** no spread/slippage beyond that fixed cost is modelled, and sensitivity to higher live costs is untested.
- **Single-seed results:** Deterministic (temperature 0.0) but no variance quantification.
- **Fixed universe:** Top-15 L1 tokens fixed at January 2025; no survivorship handling.
- **LLM API cost and availability:** Strategy requires ongoing commercial LLM API access; cost may exceed alpha.
- **Model-dependent:** Results shown for GPT-4o, GPT-5, Claude Sonnet 4.5; open-model portability untested.
- **Underspecified execution:** Order type, fill model, and spread/slippage beyond the source-reported 0.1% per side are not modelled.
- **Reproducibility:** Code repository is anonymous pre-publication; may change post-acceptance.
- **Not independently reproduced.**

## Implementation status

No implementation in our research stack (PyBroker, Nautilus, or otherwise). The paper provides an open-source code repository (anonymous pre-publication), but no validation has been performed in our environment.

## Adoption boundary

This record is research material only. Its presence in this repository does **not** mean the strategy is profitable, validated, approved for implementation, or approved for paper/testnet/live trading. The reported +133.52% cumulative return and 1.502 Sharpe ratio are source-reported claims over a single year with source-reported 0.1% per trade side transaction cost (no spread/slippage beyond that).

## Related Wiki records

- [[llm-agentic-factor-discovery-crypto-liquidity-scarcity-range-trend-2026-09-02]] — Different mechanism: LLM agent discovers cross-sectional factor signals vs. multi-agent multi-modal portfolio management; distinct in signal construction (factor discovery vs. agent coordination), portfolio construction (factor ranking vs. weekly rebalancing), and time horizon (cross-sectional vs. weekly).

## Sources

1. Luo, Y., Feng, Y., Xu, J., Tasca, P., Liu, Y. (2025). "LLM-Powered Multi-Agent System for Automated Crypto Portfolio Management." arXiv:2501.00826v3 [q-fin.TR / cs.AI]. DOI: 10.48550/arXiv.2501.00826. https://arxiv.org/abs/2501.00826.
2. Code repository: https://anonymous.4open.science/r/cryptoMAS-FCB2/ (anonymous pre-publication).
