---
schema: strategy-research-record-v1
title: LLM Agent-Discovered Liquidity-Scarcity Range-Attention Cross-Sectional Factor
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - factor-discovery
  - llm-agent
  - small-cap
  - liquidity-scarcity
  - range-attention
  - trend-continuation
status: research-only
confidence: medium
source_as_of: 2026-04-29
sources:
  - https://arxiv.org/abs/2604.26747
  - https://arxiv.org/html/2604.26747
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# LLM Agent-Discovered Liquidity-Scarcity Range-Attention Cross-Sectional Factor

## Provenance

- **Paper:** "From Hypotheses to Factors: Constrained LLM Agents in Cryptocurrency Markets"
- **Authors:** Yikuan Huang (HKUST), Zheqi Fan (HKUST), Kaiqi Hu (Rutgers), Yifan Ye (BNBU)
- **arXiv:** 2604.26747 [q-fin.PM], submitted 29 Apr 2026
- **Source URL:** https://arxiv.org/abs/2604.26747
- **Data source:** CoinMarketCap daily panel, January 2020–December 2025
- **Training window:** 2020–2022; Validation: 2023; Pure out-of-sample: 2024–2026
- **LLM used:** GPT-5.4 as the hypothesis-generation agent

## Economic mechanism

### Source-reported

The authors propose an agentic factor discovery framework where an LLM agent reads an append-only experiment trace, proposes falsifiable factor hypotheses, and maps them to executable recipes under a constrained domain-specific language (DSL). A deterministic evaluation engine enforces fixed data splits, selection gates, transaction costs, and portfolio tests. Across five search rounds, the agent converges from broad exploration toward a compact mechanism: small, liquidity-scarce tokens with persistent intraday range and positive trend tend to outperform. Failed hypotheses (range changes, volume recoveries) are noisy, while level-based scarcity and attention measures are more stable.

### Research interpretation

The core alpha hypothesis is a **cross-sectional composite factor** combining three orthogonal mechanisms:

1. **Liquidity scarcity (small-cap, low-volume):** Tokens with low market capitalization and muted dollar volume exhibit higher speculative attention per unit of liquidity, creating price pressure that persists over short horizons. This is a structural liquidity premium — thin books amplify directional moves.

2. **Range attention (persistent intraday high-low range):** Assets with consistently wide intraday ranges (relative to their price level) signal active speculative interest. The persistence of range — not the level — is the key signal, distinguishing engaged speculation from one-off volatility spikes.

3. **Trend continuation (positive lagged returns):** Tokens already in an uptrend attract momentum-chasing flow. Combined with scarcity and range, this creates a self-reinforcing dynamic where limited float amplifies directional momentum.

The composite mechanism is: **speculative attention concentrates in small, illiquid tokens where intraday range is persistently elevated, and existing positive momentum draws further flow — creating a liquidity-scarcity × attention × momentum interaction effect.**

The alpha is capacity-constrained: market-cap-weighted portfolios perform poorly, confirming the effect is concentrated in smaller tokens.

## Signal

The top-performing single factor discovered by the LLM agent is `h1_smallcap_lowvol_logret_vol` (Pure OOS Sharpe: +2.412). The composite signal is a ridge-regression combination of the curated good factor pool.

**Factor recipe (normalized from DSL):**

For each cross-section date, compute:

- **Small-cap score:** `cross_sectional_percentile_rank(market_cap)` — lower rank = smaller cap
- **Low-volume score:** `cross_sectional_percentile_rank(dollar_volume_20d_avg)` — lower rank = lower volume
- **Range persistence:** `rolling_mean(high_low_range_pct, 5d)` — 5-day average of (high-low)/close
- **Trend:** `lagged_return_1d` — previous day's close-to-close return
- **Low volatility:** `rolling_std(log_return, 20d)` — 20-day realized vol (lower = better)

**Composite signal:**
```
signal = ridge_combined(standardize_cross_sectional([small_cap, low_vol, range_persistence, trend]))
```

- **Long entry:** Top quintile of composite signal
- **Short entry:** Bottom quintile (for long-short construction)
- **Holding period:** 1 day (daily rebalance)
- **Execution:** Signal formed at close of day T, executed at close of day T+1 (1-day lag)
- **Portfolio construction:** Equal-weighted quintile sort; ridge regression trained only on 2020–2022 window

**Parameters (source-reported):**
- Ridge regression α tuned on training window
- Factor pool curated by LLM agent across 5 search rounds
- Selection gate: IC > threshold and IC t-stat > threshold (fixed before each round)

## Required data

- **Instrument universe:** Top ~200–500 cryptocurrencies by market cap on CoinMarketCap (filtered: ≥180 days history, minimum daily volume threshold)
- **Venue:** CoinMarketCap aggregated daily data (spot)
- **Market type:** Spot
- **Timeframe:** Daily
- **Fields:** OHLCV, market capitalization
- **Derived signals:** Close-to-close returns, log returns, realized volatility (20d), high-low range percentage, relative volume, dollar volume
- **Timestamp:** Daily close, UTC
- **Point-in-time:** All signals use only information available at or before signal formation date

## Execution assumptions

- **Signal-to-order timing:** 1-day execution lag (signal at T close, execute at T+1 close)
- **Market order:** Assumed market execution at next-day close
- **Fees:** 5 bps one-way trading cost assumed in main results
- **Spread:** Not explicitly modeled; subsumed into the 5 bps assumption
- **Slippage:** Not explicitly modeled beyond fee assumption
- **Capacity:** The equal-weighted long-short portfolio has 36.8% monthly turnover; the strategy is explicitly capacity-constrained to smaller tokens
- **Leverage:** Not specified; long-short construction implies some capital efficiency
- **Fill model:** Assumed perfect fill at close

## Evidence

### Source-reported

- Ridge-combined equal-weight long-short portfolio: **44.55% annualized return, 1.55 Sharpe ratio** in pure out-of-sample period (2024–2026) after 5 bps one-way cost
- Top single factor `h1_smallcap_lowvol_logret_vol`: Pure OOS Sharpe of +2.412
- Quintile portfolio shows clear monotonic relationship: top quintile significantly outperforms bottom quintile
- Market-cap-weighted version performs poorly — alpha concentrated in smaller tokens
- Fee sensitivity: L-S portfolio remains Sharpe > 0.46 even at 30 bps one-way cost
- Total of 25 single factors generated across 5 search rounds; top 9 have Pure OOS Sharpe > 1.7
- Failed hypotheses (range changes, volume recoveries) were noisy; level-based scarcity measures were more stable

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Market-cap-weighted portfolios perform poorly, indicating capacity constraints
- Alpha is concentrated in smaller tokens — large-cap crypto does not exhibit this effect
- The framework does not produce a frictionless large-cap trading strategy
- Transaction cost sensitivity: at 30 bps one-way, annualized return drops to ~1.2% with Sharpe ~0.46
- The DSL constraint limits factor complexity — more expressive models might find different signals

## Falsification plan

- **Out-of-sample extension:** Test on 2026+ data as it becomes available; the current OOS window (2024–2026) should be extended
- **Capacity test:** Measure performance decay as position size increases; the market-cap-weighted poor performance suggests the strategy may not scale beyond small-cap universe
- **Ablation:** Decompose the composite into individual components (small-cap alone, range alone, trend alone) to measure each component's marginal contribution
- **Regime sensitivity:** Test across bull/bear/sideways regimes separately; momentum components may fail in extended bear markets
- **Alternative LLM agents:** Replicate with different LLMs (not GPT-5.4) to test whether factor discovery is agent-dependent
- **Fee escalation:** Test at 50+ bps to simulate real-world costs for illiquid small-cap tokens (which may have wider spreads than the 5 bps assumption)
- **Failure metric:** If the equal-weight L-S portfolio Sharpe drops below 0.5 in a rolling 12-month window, the hypothesis is materially weakened

## Crypto portability

**direct**

This strategy originates from and is tested on cryptocurrency markets (CoinMarketCap daily panel). The mechanism — liquidity scarcity amplifying speculative attention in small-cap tokens — is inherently crypto-native. The 24/7 market structure, retail-driven speculation, and fragmented liquidity across many small tokens make this a natural fit for crypto.

However, portability risks include:
- **Liquidity:** The smallest tokens in the universe may have severe execution challenges (wide spreads, thin books) not captured by the 5 bps cost assumption
- **Listing risk:** Small-cap tokens may be delisted or experience exchange outages
- **Survivorship bias:** The dataset filters for tokens with ≥180 days history, potentially introducing survivorship bias
- **Regime dependence:** The 2024–2026 period may have specific market conditions (e.g., meme coin mania) that amplified small-cap speculation

## Limitations

- not independently reproduced
- capacity-constrained to small-cap tokens
- 5 bps fee assumption may underestimate real costs for illiquid tokens
- DSL constraint limits factor expressiveness
- LLM agent reproducibility uncertain (GPT-5.4 specific)
- survivorship bias risk in CoinMarketCap data
- short OOS window (2024–2026)
- market-cap-weighted version fails — alpha only in small-cap tail

## Implementation status

Not implemented in our research stack.

## Adoption boundary

This record represents research material only. Its presence does not mean:
- the strategy is profitable
- the alpha has been validated
- it is approved for implementation
- it is approved for paper trading
- it is approved for testnet
- it is approved for live trading

## Related Wiki records

- [[crypto-cross-sectional-low-volatility-premium-post-2017-2026-09-01]]
- [[crypto-cross-sectional-amihud-illiquidity-premium-2026-08-31]]
- [[crypto-cross-sectional-abnormal-investor-attention-momentum-2026-08-31]]
- [[crypto-cross-sectional-momentum-30d-top-quintile-7d-2026-08-31]]

## Sources

1. Huang, Y., Fan, Z., Hu, K., & Ye, Y. (2026). "From Hypotheses to Factors: Constrained LLM Agents in Cryptocurrency Markets." arXiv:2604.26747 [q-fin.PM]. https://arxiv.org/abs/2604.26747
