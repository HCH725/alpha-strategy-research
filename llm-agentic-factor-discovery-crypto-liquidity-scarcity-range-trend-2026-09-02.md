---
schema: strategy-research-record-v1
title: "Constrained LLM Agent Factor Discovery in Cryptocurrency Markets: Liquidity-Scarcity, Range-Attention, and Trend-Continuation Factor Family"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - factor-discovery
  - cross-sectional
  - liquidity-scarcity
  - range-attention
  - trend-continuation
  - LLM-agentic
  - small-cap
status: research-only
confidence: medium
source_as_of: 2026-09-02
sources:
  - "Yifan Ye, 'From Hypotheses to Factors: Constrained LLM Agents in Cryptocurrency Markets', arXiv:2604.26747v1 [q-fin.PM], April 2026. DOI: 10.48550/arXiv.2604.26747. https://arxiv.org/abs/2604.26747"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Constrained LLM Agent Factor Discovery in Cryptocurrency Markets: Liquidity-Scarcity, Range-Attention, and Trend-Continuation Factor Family

## Provenance

- **Primary Source:** Yifan Ye (Beijing Normal-Hong Kong Baptist University / UIC), *"From Hypotheses to Factors: Constrained LLM Agents in Cryptocurrency Markets"*, arXiv preprint `arXiv:2604.26747v1 [q-fin.PM]`, April 2026. DOI: [10.48550/arXiv.2604.26747](https://doi.org/10.48550/arXiv.2604.26747). Full text: [https://arxiv.org/abs/2604.26747](https://arxiv.org/abs/2604.26747).
- **Primary Subject Areas:** Portfolio Management (`q-fin.PM`), General Finance (`q-fin.GN`), Trading and Market Microstructure (`q-fin.TR`).
- **Context:** The paper proposes an agentic factor discovery framework where an LLM agent (GPT-5.4) proposes falsifiable factor hypotheses and symbolic signal recipes, while a deterministic evaluation engine enforces fixed data splits, selection gates, transaction costs, and portfolio tests. The agent controls search direction but cannot modify the evaluation protocol.

## Economic mechanism

### Source-reported

The framework converged across five search rounds from broad exploration toward a compact mechanism: **small, liquidity-scarce tokens with persistent intraday range and positive trend tend to outperform**. The author hypothesizes this reflects speculative attention being active in small tokens but not yet crowded, combined with informational inefficiency in less liquid segments. Failed hypotheses (range changes, volume recoveries) were identified as noisy, while level-based scarcity and attention measures proved more stable.

### Research interpretation

The falsifiable thesis is that **cross-sectional return predictability in cryptocurrency markets is concentrated in a liquidity-scarcity × range-persistence × trend-continuation factor family**:

1. **Liquidity scarcity:** Smaller market-cap tokens with lower dollar trading volume exhibit higher expected returns, consistent with an illiquidity premium or information asymmetry effect where under-researched assets offer compensation for bearing adverse selection risk.
2. **Range-attention:** Tokens with persistent intraday high-low range (normalized by price) attract speculative attention, which creates short-term demand pressure and positive drift.
3. **Trend continuation:** Assets exhibiting positive recent trend (lagged returns or moving average momentum) within the small-cap, high-range universe tend to continue outperforming, consistent with behavioral momentum or gradual information diffusion.
4. **Non-linearity in volume:** Volume level (rather than volume change or recovery) is the more stable predictor; sudden volume spikes or recoveries introduce noise.

The combination (ridge-regression weighted composite) captures complementary dimensions of the same speculative-attention-driven microstructure.

## Signal

### Formation timestamp
- Signal formed at daily close using point-in-time daily OHLCV and market-cap data.
- Execution lag: 1-day (signal at close of day t, evaluated against return from open of day t+1 to close of day t+2).
- Timezone: UTC (CoinMarketCap daily data convention).

### Lookback
- Cross-sectional percentile rank computed daily across all tradable assets.
- Rolling transforms use MA-10 for range (intraday high-low range over 10 days) and MA-3 for volume changes.
- No warm-up period specified beyond the standard 180-day minimum listing history filter.

### Long entry
- Assets ranked by composite score: `rank_t(-0.6 * log(1 + mcap) + 0.5 * MA10(range) - 0.2 * MA3(Δvolume))`.
- Top quintile (Q4) constitutes the long portfolio in equal-weight long-short construction.
- Cross-sectional ranking applied daily.

### Short entry
- Bottom quintile (Q0) constitutes the short portfolio.
- Equal-weight within each leg.

### Exit / holding period
- Daily rebalancing: scores recomputed daily, portfolio reconstituted daily.
- No explicit stop-loss or time exit; exit is implicit in daily re-ranking.

### Parameters
- Factor weights in composite score: -0.6 (log market cap), +0.5 (MA10 range), -0.2 (MA3 volume change). These are source-reported as discovered by the LLM agent.
- Ridge regression lambda for final combination: fitted on training data only.
- Selection gate thresholds: IC ≥ τ_IC and t_IC ≥ τ_t (fixed before each round).

### Position sizing
- Equal-weight within long and short legs.
- Market-cap-weighted variant also tested (performs poorly, indicating capacity constraint in small-cap alpha).

## Required data

- **Instrument:** Daily OHLCV + market capitalization for a broad cryptocurrency universe.
- **Universe:** CoinMarketCap daily data, January 2020 – December 2025. Assets with <180 days trading history or below a predefined average daily volume threshold excluded.
- **Venue:** CoinMarketCap aggregated data (not venue-specific).
- **Timeframe:** Daily bars.
- **Fields:** Open, High, Low, Close, Volume, Market Capitalization. Derived: log returns, relative volume, realized volatility, price-to-moving-average, high-low range, volume percentage change.
- **Point-in-time:** Standard daily close convention; no revision data described.
- **Timestamp:** UTC daily.
- **Missing-data:** Assets with insufficient history excluded; no explicit imputation described.
- **Funding/fee/spread:** Transaction costs modeled as percentage of traded value (0.1%–0.3% one-way).

## Execution assumptions

- **Order type:** Not specified; implied market order at next-day open.
- **Fill model:** Assumed full fill.
- **Latency:** Not specified; daily rebalancing implies T+1 execution.
- **Fees:** One-way transaction cost of 5 basis points in the main result; fee sensitivity tested at 0.1%, 0.2%, 0.3%.
- **Slippage:** Modeled as percentage of traded value; no explicit slippage model.
- **Impact / capacity:** Market-cap-weighted variant performs poorly, indicating alpha is concentrated in smaller tokens and capacity-constrained. Practical capacity limit not quantified.
- **Leverage / margin:** Not specified; equity-only long-short.

## Evidence

### Source-reported

- Ridge-combined equal-weight long-short portfolio: 44.55% annualized return, Sharpe ratio 1.55 in pure OOS period (2024–2026), after 5bp one-way trading cost.
- Training window: 2020–2022; validation: 2023; pure OOS: 2024 onward.
- Top individual factor OOS Sharpe ratios range from 1.70 to 2.41.
- Quintile sort shows monotonic Q0→Q4 performance separation.
- Market-cap-weighted version performs poorly.
- Fee sensitivity: Sharpe remains positive at 0.3% one-way cost (Sharpe ~0.46).
- Combo-signal L-S portfolio: annualized return ~44.5%, annualized vol ~28.7%, Sharpe 1.55, MaxDD -23.6%, Calmar 1.89, turnover 36.8%.
- Source reports all results; this result has not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Market-cap-weighted portfolio performs poorly, indicating alpha is concentrated in small-cap tokens with limited capacity.
- Range changes and volume recoveries identified as noisy factors by the agent.
- Transaction costs erode alpha; at 30bp one-way the combo Sharpe drops to ~0.46.
- The paper notes the framework "does not produce a frictionless large-cap trading strategy."

## Falsification plan

1. **Out-of-sample decay test:** Re-run ridge-combined factor on post-2026 data. If OOS Sharpe drops below 0.5 over a rolling 12-month window, the thesis is materially weakened.
2. **Capacity stress test:** Evaluate performance as a function of market-cap cutoff. If alpha disappears above the 50th percentile of market cap, the capacity constraint is confirmed.
3. **Factor ablation:** Test each component (log-mcap, range, volume change) independently in OOS. If the composite's edge is entirely driven by one component, the multi-factor thesis is falsified.
4. **Fee sensitivity:** Re-run with realistic perpetual-swap funding rates and maker/taker fees. If net Sharpe drops below zero at 10bp all-in cost, the strategy is not implementable.
5. **Regime decomposition:** Test separately in bull (BTC > 15% 60d return), bear (< -15%), and sideways regimes. If alpha is concentrated in one regime, the thesis is regime-dependent.
6. **Placebo test:** Shuffle asset labels cross-sectionally; if the shuffled Sharpe is comparable, the result may be driven by time-series rather than cross-sectional predictability.
7. **Parameter perturbation:** Vary the factor weights (±0.2 on each coefficient). If performance degrades sharply, the specific parameterization may be overfit.

## Crypto portability

**Direct.** The study is conducted entirely on cryptocurrency daily data from CoinMarketCap (January 2020 – December 2025). The mechanism is natively crypto-specific:

- **Spot vs perpetual:** The study uses spot-equivalent daily data; deployment on perpetual swaps would introduce funding rate dynamics not modeled.
- **24/7 session:** Daily bars are used, so session structure is implicitly handled.
- **Venue fragmentation:** CoinMarketCap aggregates across venues; liquidity-scarcity signal may be venue-dependent.
- **Listing/survivorship:** Assets with <180 days history excluded; survivorship bias is partially mitigated but not fully addressed (delisted assets may create look-ahead bias).
- **Liquidity:** The alpha is concentrated in small-cap tokens where order-book depth is thin; slippage risk is material.

## Limitations

- **Capacity-constrained:** Alpha is concentrated in small-cap tokens; market-cap-weighted version performs poorly. Practical capacity limit not quantified.
- **LLM-discovered factors may overfit:** The factor DSL constrains the search space, but the LLM's hypothesis generation is still a form of search over a finite sample. The selection gates mitigate but do not eliminate data-mining risk.
- **CoinMarketCap data:** Aggregated daily data may not reflect venue-specific liquidity or execution reality.
- **No explicit look-ahead protection for market cap:** Market-cap data availability and revision lag not described.
- **Transaction cost model simplistic:** Percentage-of-value model does not capture market impact, spread dynamics, or funding costs on perpetuals.
- **Training/selection overlap:** The LLM agent observes validation metrics during search (for diagnosis), creating potential soft leakage.
- **Single-author paper:** Limited independent review; results should be treated with appropriate skepticism.
- **OOS period (2024–2026) overlaps with the paper's own data period:** The "pure OOS" uses data through December 2025, which may overlap with data the model was trained on via the LLM's own knowledge.

## Implementation status

Not implemented. No implementation in our research stack (PyBroker, Nautilus, or paper trading) has been completed. The source provides a constrained DSL but no public code repository.

## Adoption boundary

This record represents research material only. A record being present in this repository does not mean:
- Profitable;
- Validated alpha;
- Approved for implementation;
- Approved for paper trading;
- Approved for testnet;
- Approved for live trading.

## Related Wiki records

No related Wiki Brain records identified for this specific factor family. Related concepts: cross-sectional crypto momentum, small-cap crypto alpha, liquidity premium in digital assets.

## Sources

- Yifan Ye, *"From Hypotheses to Factors: Constrained LLM Agents in Cryptocurrency Markets"*, arXiv:2604.26747v1 [q-fin.PM], April 2026. DOI: 10.48550/arXiv.2604.26747. https://arxiv.org/abs/2604.26747.
