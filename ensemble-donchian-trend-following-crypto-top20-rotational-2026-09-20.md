---
schema: strategy-research-record-v1
title: Ensemble Donchian Channel Trend-Following for Crypto Top-20 Rotational Portfolio
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - trend-following
  - donchian
  - ensemble
  - momentum
status: research-only
confidence: medium
source_as_of: 2025-10-02
sources:
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5209907"
  - "https://doi.org/10.2139/ssrn.5209907"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Ensemble Donchian Channel Trend-Following for Crypto Top-20 Rotational Portfolio

## Provenance

- **Paper:** "Catching Crypto Trends; A Tactical Approach for Bitcoin and Altcoins"
- **Authors:** Carlo Zarattini (Concretum Group, Lugano), Alberto Pagani (Concretum Group, Lugano), Andrea Barbon (University of St. Gallen; c/o University of Geneva)
- **Working paper series:** Swiss Finance Institute Research Paper No. 25-80
- **SSRN:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5209907
- **DOI:** https://doi.org/10.2139/ssrn.5209907
- **Posted:** May 6, 2025; last revised October 2, 2025
- **Pages:** 38
- **Source data as-of:** 2025-10-02 (paper revision date)
- **Dataset:** All cryptocurrencies traded since 2015; survivorship bias-free

## Economic mechanism

### Source-reported

The paper applies classical trend-following methodology — successfully deployed in traditional asset classes for decades — to cryptocurrency markets. The authors argue that crypto markets are fertile ground for systematic trend strategies due to high liquidity, substantial volatility, lack of conventional valuation anchors, and a participant base prone to emotion-driven decisions. Trend-following captures sustained directional moves while limiting downside through systematic exits.

### Research interpretation

The hypothesized mechanism is trend persistence / momentum in cryptocurrency returns at daily horizons. The ensemble approach — combining signals from multiple Donchian channel lookback periods — is designed to capture trends across different timeframes (short, medium, long) and reduce sensitivity to any single lookback window. The economic rationale is that crypto markets exhibit fat-tailed, trending return distributions where breakout signals can persistently capture upside while volatility-based position sizing controls risk.

Components:
- **Signal:** Ensemble of 9 Donchian channel breakout models (lookbacks: 5, 10, 20, 30, 60, 90, 150, 250, 360 days)
- **Position sizing:** Volatility-targeting at 25% annualized, capped at 200% allocation
- **Universe:** Top 20 most liquid coins, dynamically selected (rotational)
- **Cost mitigation:** Rebalance threshold technique (research-proposed; exact mechanism underspecified in available sources)

## Signal

- **Formation timestamp:** Daily; signal formed at end of trading day based on close prices.
- **Lookback:** Nine independent Donchian channel lookback windows: 5, 10, 20, 30, 60, 90, 150, 250, 360 days. Endpoints inclusive (standard Donchian definition: highest high / lowest low over N periods).
- **Long entry:** Price closes above the N-day highest high for a given lookback window. Each of the 9 models generates an independent long signal. The ensemble aggregates these into a single combined signal (exact aggregation rule: equal-weight averaging of individual model signals — research-proposed; the precise combination formula should be verified in the primary source).
- **Short entry:** Not specified in available abstracts. The strategy appears to be long-only or flat (goes to cash when no trend signal fires). research-proposed assumption that the strategy is long-only.
- **Exit:** Price closes below the N-day lowest low for the corresponding lookback window. Each model independently exits when its own lower channel is breached.
- **Holding period:** No fixed holding period; position held until exit signal fires. Expected holding period depends on trend duration.
- **Parameters:** Nine lookback periods (5, 10, 20, 30, 60, 90, 150, 250, 360 days); 25% annualized volatility target; 200% max allocation cap; equal-weight ensemble combination. These parameter values are source-reported from the abstract and secondary summaries; the exact ensemble aggregation formula should be verified in the primary PDF.
- **Position sizing:** Each position sized to contribute to a 25% annualized portfolio volatility target. Allocation capped at 200% (allowing up to 2x leverage). Dynamic: exposure decreases during high-volatility regimes and increases during calmer regimes.
- **Rebalance threshold:** The paper proposes a portfolio technique to mitigate transaction costs by introducing a rebalance threshold (avoiding unnecessary rebalancing when changes are small). Exact threshold rule: underspecified in available sources; needs primary-source verification.

## Required data

- **Instrument:** Spot cryptocurrency tokens (not perpetual futures in the primary formulation).
- **Universe:** Top 20 most liquid coins by market cap or volume, dynamically selected. Survivorship bias-free dataset covering all cryptocurrencies traded since 2015. Delphic Alpha replication used 67 coins excluding stablecoins with minimum 1 year of history.
- **Venue:** Not specified in abstract; likely aggregated spot data from major exchanges.
- **Timeframe:** Daily bars (close-to-close).
- **Fields:** OHLC (highest high, lowest low for Donchian channels); close for signal formation.
- **Missing-data:** Not specified; survivorship bias is explicitly addressed.

## Execution assumptions

- **Signal-to-order timing:** Next-day open (standard for daily breakout systems; research-proposed assumption).
- **Order type:** Market order (research-proposed).
- **Fill model:** Full fill at next-day open (research-proposed).
- **Fees:** Source reports net-of-fees returns. Delphic Alpha replication used 10 bps round-trip cost. Exact fee assumption in the primary paper: underspecified in available sources.
- **Slippage:** Not explicitly modeled in available summaries.
- **Leverage:** Up to 2x (200% allocation cap).
- **Funding:** Not applicable for spot positions; the primary formulation appears to use spot, not perpetual futures.
- **Capacity:** Not specified; the strategy targets top-20 liquid coins, suggesting reasonable capacity for institutional-scale capital.

## Evidence

### Source-reported

The following are reported by Zarattini, Pagani & Barbon (SSRN 5209907) as described in the abstract and secondary summaries:

- **Bitcoin-only backtest (Combo ensemble model):** CAGR 30%, Sharpe ratio 1.58, Sortino ratio 2.03, max drawdown 19% (vs. 80%+ for passive BTC buy-and-hold). Annualized alpha of 14% versus Bitcoin. These figures are reported for a single-asset Bitcoin backtest.
- **Multi-coin portfolio (top 20 most liquid coins):** Sharpe ratio above 1.5, annualized alpha of 10.8% versus Bitcoin. Net-of-fees returns.
- **Bear market avoidance:** Ensemble avoids major drawdowns; max drawdown ~12% vs. BTC's 84% (from Delphic Alpha replication; may differ from paper's exact figures).
- **Diversification:** Crypto trend-following shows low correlation with traditional asset class trend-following strategies.
- **Execution:** Paper discusses both on-chain and off-chain implementation methods.

**Important caveat:** The Bitcoin-only CAGR/Sharpe/alpha figures (30%/1.58/14%) appear to be from a single-asset backtest, while the top-20 portfolio figures (Sharpe >1.5, alpha 10.8%) are from the multi-coin rotational portfolio. These are different experimental configurations. The exact figures should be verified against specific tables in the primary PDF.

### Independently reproduced

- **Delphic Alpha replication (Substack):** Independent replication using the same methodology (9 Donchian breakouts, 25% vol target, 10 bps cost, equal-weight portfolio of 67 coins) reported consistent results: avoided 2018 and 2022 crypto winters, max drawdown ~12%, consistently positive rolling Sharpe. Not peer-reviewed; not independently audited.

Not independently reproduced in our research system.

### Negative evidence

- The Delphic Alpha replication noted that BNB, ETH, and BTC were the strongest contributors, suggesting concentration risk in a few assets.
- Trend-following strategies in crypto are known to suffer in prolonged sideways or choppy markets. The paper's sample period (2015–2025) includes both strong trending periods (2017, 2020–2021) and extended bear/sideways markets (2018, 2022). Performance in regime transitions is not separately reported in available sources.
- Transaction cost sensitivity: the paper acknowledges high-frequency rebalancing costs and proposes a threshold technique, but the exact cost-resilience is underspecified.
- Survivorship bias in the crypto universe: while the dataset is described as survivorship bias-free, coins that were delisted or became illiquid during the sample may have different execution characteristics than the backtest assumes.
- Shorter lookback periods (5–30 days) showed strongest risk-adjusted returns on Bitcoin, but these may be more sensitive to execution costs and slippage in practice.

None identified in the reviewed sources beyond the above; absence is not evidence of no negative result.

## Falsification plan

1. **Out-of-sample test:** Apply the ensemble Donchian system to crypto data from October 2025 onward (post-paper revision). If Sharpe ratio degrades below 1.0 over a 12-month rolling window, the trend signal may be decaying.
2. **Cost sensitivity stress test:** Increase round-trip costs from 10 bps to 30 bps and 50 bps. If net Sharpe drops below 0.5 at 30 bps, the strategy is cost-sensitive. **research-defined falsification threshold.**
3. **Ensemble ablation:** Test individual lookback periods (5, 20, 60, 150, 360) in isolation. If the ensemble outperforms all individual models, the diversification across horizons adds value; if any single model dominates, the ensemble is not necessary.
4. **Regime breakdown:** Separate performance into trending (ADX > 25) vs. choppy (ADX < 25) regimes. If the strategy loses money in choppy regimes, the ensemble's risk control depends on regime identification.
5. **Universe sensitivity:** Test on top-10 vs. top-30 vs. top-50 coins. If performance degrades substantially when expanding beyond top-20, the strategy may be capacity-constrained or liquidity-dependent.
6. **Placebo / permutation test:** Shuffle entry signals while preserving holding periods. If shuffled signals produce comparable returns, the edge may be driven by the volatility-targeting position sizing rather than the breakout signal.
7. **Comparison baseline:** Benchmark against buy-and-hold BTC, equal-weight crypto basket, and simple moving average crossover (50/200) on the same universe and period.

## Crypto portability

direct

The strategy is native to cryptocurrency spot markets. The paper explicitly addresses crypto implementation including on-chain execution (DEX) and off-chain execution (CEX). The 24/7 trading structure means Donchian channel signals fire continuously rather than being restricted to exchange hours. However, the primary formulation uses spot, not perpetual futures; porting to perpetuals would introduce funding rate dynamics that are not modeled.

Key crypto-specific considerations:
- **Spot vs. perpetual:** Primary formulation is spot-based. Perpetual futures would add funding rate carry (positive or negative depending on market regime) that could enhance or erode returns.
- **24/7 trading:** Continuous signals; no session-boundary effects.
- **Venue fragmentation:** Top-20 coin selection may vary by venue; liquidity fragmentation could affect fill quality.
- **Delisting risk:** Survivorship-bias-free dataset addresses this, but live implementation must handle delistings in real time.
- **Stablecoin exclusion:** Paper explicitly excludes stablecoins.

## Limitations

- **Primary source access:** The full PDF was not directly read in this scout run; methodology details (exact ensemble aggregation formula, rebalance threshold rule, precise fee model, table-level performance provenance) are derived from the abstract and secondary summaries. These should be verified against the primary PDF before use in falsification or implementation.
- **Performance figures from secondary sources:** The CAGR 30%, Sharpe 1.58, alpha 14% (Bitcoin-only) and Sharpe >1.5, alpha 10.8% (multi-coin) are reported in secondary summaries, not directly traced to specific tables in the primary paper.
- **Sample period:** 2015–2025. Crypto market microstructure has changed substantially (rise of perpetual futures, institutional adoption, Binance dominance). Early-period results may not generalize.
- **Universe construction:** "Top 20 most liquid coins" — exact selection criteria (by volume, market cap, or both), reconstitution frequency, and minimum listing age are underspecified.
- **Survivorship bias claim:** The paper claims survivorship-bias-free data, but details on how delisted/illiquid coins are handled in the backtest are not available in the abstract.
- **Not independently reproduced** in our research system.
- **Transaction cost model:** Exact fee/slippage assumptions in the primary paper are underspecified; Delphic Alpha used 10 bps.
- **Capacity:** Not quantified; top-20 liquid coins suggest reasonable capacity but actual market impact is unknown.
- **Regime dependence:** Crypto trend-following is known to suffer in choppy/sideways markets; regime-specific performance is not reported.

## Implementation status

Not implemented. No implementation in our research stack (PyBroker, Nautilus, or otherwise).

## Adoption boundary

This record is research material only. Presence in this repository does not mean:
- Profitable
- Validated alpha
- Approved for implementation
- Approved for paper trading
- Approved for testnet
- Approved for live trading

## Related Wiki records

- `[[crypto-perpetual-regime-aligned-right-tail-trend-cost-hurdle-2026-09-13]]` — Right-tail trend following with macro regime filter; different mechanism (right-tail capture vs. ensemble Donchian breakout) but same crypto trend-following domain.
- `[[crypto-perpetual-supertrend-wpr-trend-following-cost-gate-falsification-2026-09-12]]` — Multi-timeframe Supertrend/Williams %R trend-following; different indicator family but shares the trend-following-in-crypto theme.
- `[[crypto-walk-forward-window-optimization-double-oos-momentum-2026-09-04]]` — Walk-forward momentum with double out-of-sample; different methodology but related crypto momentum domain.
- `[[llm-news-enhanced-cross-sectional-momentum-tilt-2026-09-06]]` — Different paper by overlapping authors (Anic, Barbon, Seiz, Zarattini) on LLM-enhanced momentum; distinct mechanism.

## Sources

1. Carlo Zarattini, Alberto Pagani, Andrea Barbon. "Catching Crypto Trends; A Tactical Approach for Bitcoin and Altcoins." Swiss Finance Institute Research Paper No. 25-80. SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5209907. DOI: https://doi.org/10.2139/ssrn.5209907. Posted May 6, 2025; last revised October 2, 2025. 38 pages.
2. QuantifiedStrategies.com summary of the paper methodology and performance. https://www.quantifiedstrategies.com/crypto-trend-trading-strategy-for-bitcoin/ (secondary source; not peer-reviewed).
3. Delphic Alpha independent replication. https://delphicalpha.substack.com/p/the-replicator-catching-crypto-trends (secondary source; independent but not peer-reviewed).
