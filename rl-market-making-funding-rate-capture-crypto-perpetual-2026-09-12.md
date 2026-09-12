---
schema: strategy-research-record-v1
title: "RL Market Making with Funding Rate Capture on Crypto Perpetual Futures"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - reinforcement-learning
  - market-making
  - perpetual-futures
  - funding-rate
  - crypto
status: research-only
confidence: medium
source_as_of: 2026-09-12
sources:
  - "https://doi.org/10.1016/j.jfds.2026.100197"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# RL Market Making with Funding Rate Capture on Crypto Perpetual Futures

## Provenance

- **Authors:** Edson Pindza (Department of Decision Sciences, University of South Africa), Claude Rodrigue Bambe Moutsinga (Sefako Makgatho Health Sciences University)
- **Paper title:** "Reinforcement learning for automated market making in cryptocurrency perpetual futures: Integrating funding rate dynamics with historical BTCUSDT evidence"
- **Journal:** Journal of Finance and Data Science (ScienceDirect)
- **DOI:** [10.1016/j.jfds.2026.100197](https://doi.org/10.1016/j.jfds.2026.100197)
- **Published:** June 17, 2026
- **Access:** ScienceDirect (paywalled; no open-access version located)
- **Source data as-of:** 2026-09-12 (DOI landing page and abstract verified via search; full text not independently read due to access restrictions)

## Economic mechanism

### Source-reported

The paper addresses a gap in reinforcement learning (RL) market making research: existing approaches for crypto perpetual futures ignore the funding rate mechanism that transfers payments between long and short position holders every 8 hours. The authors propose that jointly optimizing spread decisions and funding rate capture—rather than treating funding as an exogenous overlay—can improve market-making profitability. The state design embeds crypto-native contract mechanics directly into the agent's information set.

### Research interpretation

The hypothesized mechanism is that a market maker who actively manages inventory relative to funding rate regime (e.g., skewing quotes to capture funding from the paying side, or reducing exposure before adverse funding settlements) can earn incremental returns beyond pure spread income. This is an information-edge hypothesis: the funding rate dynamics contain exploitable structure that conventional Avellaneda-Stoikov-style market makers ignore.

The strategy is a hybrid:
- **Core signal:** RL-optimized bid-ask spread and inventory decisions (PPO/SAC policies)
- **Regime filter:** Volatility filtering and fee-aware quoting
- **Inventory management:** Momentum-based inventory targeting (directional bias based on recent price momentum)
- **Funding integration:** State features include current and historical funding rates, funding rate z-scores, and funding rate regime classification

## Signal

- **Formation timestamp:** Hourly decision intervals aligned with Binance Futures API candle boundaries.
- **Lookback:** Not fully specified in accessible sources. State features include realized volatility and order-flow imbalance proxy over rolling windows; exact lookback windows are described in the paper's Methods section (not accessible).
- **Entry (quote placement):** The RL agent outputs bid-ask spread and inventory target. When the agent quotes, it places limit orders on both sides. The "performance-first adaptive" variant adds: (1) volatility filtering (wider spreads in high-vol regimes), (2) fee-aware quoting (ensuring spread covers fee structure), (3) momentum-based inventory targeting (skewing quotes to build position in the direction of recent momentum).
- **Exit:** Inventory rebalancing through quote adjustments; the agent continuously updates quotes. No explicit stop-loss or time-based exit described in accessible sources.
- **Holding period:** Continuous market making with no fixed holding period; inventory is managed dynamically.
- **Parameters:** Not fully specified in accessible abstract/search snippets. The paper describes the MDP formulation, state features, and reward function in detail (Methods section, not accessible). Key hyperparameters for PPO/SAC are in the paper's experimental setup.
- **Position sizing:** Inventory is bounded (the agent manages a single-instrument position on BTCUSDT perpetual). Exact position limits not specified in accessible sources.

**Note:** The signal is partially underspecified from accessible sources. Full reconstruction requires reading the paper's Methods and Experimental Setup sections.

## Required data

- **Instrument:** BTCUSDT perpetual futures contract on Binance Futures
- **Venue:** Binance Futures (USDT-margined)
- **Market type:** Perpetual futures
- **Timeframe:** Hourly candles (OHLCV) for price data; 8-hour funding rate settlement data
- **Fields:** OHLCV (hourly), funding rate (per 8h settlement), mark price, index price, order-flow imbalance proxy (exact construction not specified in accessible sources)
- **Sample period:** 31 December 2022 22:00 to 18 May 2026 11:00 (29,606 hourly observations); funding rate sample: 1 January 2023 00:00 to 18 May 2026 08:00 (3,701 records)
- **Timestamp:** UTC (Binance API standard)
- **Point-in-time:** Public Binance Futures API data; no survivorship bias concern for a single instrument
- **Missing data:** Not specified in accessible sources

## Execution assumptions

- **Signal-to-order timing:** The agent decides at hourly intervals; quotes are placed as limit orders. Exact latency between decision and order placement not specified.
- **Order type:** Limit orders (maker); the agent continuously quotes bid and ask.
- **Fill model:** Not fully specified in accessible sources. The paper likely uses a backtest fill model based on historical order book data, but exact assumptions (partial fills, queue priority, etc.) are in the Methods section.
- **Fees:** The "performance-first adaptive" variant explicitly incorporates fee-aware quoting. Exact fee assumptions (maker vs. taker rate) are in the paper's experimental setup (not accessible). Binance standard maker fee is 0.02%, taker fee 0.04% for VIP-0 tier; the paper likely uses these or similar values.
- **Slippage:** Not specified in accessible sources.
- **Spread:** The agent optimizes spread as part of its action space.
- **Funding:** Funding rate is a key state feature and is integrated into the agent's decision-making. Funding is paid/received every 8 hours based on the perpetual-spot basis. The paper explicitly models this as part of the PnL.
- **Leverage:** Not specified in accessible sources.
- **Impact / capacity:** Not addressed; the paper studies a single instrument (BTCUSDT) which has deep liquidity.
- **Latency:** Not specified in accessible sources; the paper notes that production deployment requires addressing latency constraints.
- **Partial fills / failures:** Not specified in accessible sources.

**Data gaps:** Transaction cost assumptions, fill model details, slippage model, and exact fee schedule are in the paper's Methods/Experimental Setup sections (not accessible from search snippets).

## Evidence

### Source-reported

The paper reports the following results on the final historical holdout period (specific holdout dates not specified in accessible sources):

**Performance-first adaptive market making variant:**
- Annualized return: 24.63%
- Sharpe ratio: 1.49
- Zero-risk-free Sharpe ratio: 1.87
- Maximum drawdown: 6.39%

**Baseline RL policy (PPO/SAC without the adaptive variant):**
- "Remains only marginally positive under the conservative Sharpe definition" (exact numbers not specified in accessible sources)

The paper notes that these results come from a "performance-first adaptive market making variant with volatility filtering, fee-aware quoting, and momentum-based inventory targeting"—i.e., the best-performing configuration includes non-RL heuristic overlays on top of the RL policy.

Source reports these results but acknowledges that profitability depends critically on explicit fee, regime, and inventory filters. The paper contributes a "reproducible real-data benchmark" and identifies requirements for production readiness.

**Important caveat:** The performance figures are from a single-instrument (BTCUSDT) backtest on a specific holdout period. They have not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The paper itself provides significant negative evidence:
1. The raw RL policy (without the adaptive variant overlays) is only marginally positive, suggesting that pure RL market making without heuristic augmentation does not produce robust returns.
2. The authors explicitly state that "profitability depends critically on explicit fee, regime, and inventory filters"—implying the RL component alone is insufficient.
3. The authors note that "risk controls, execution assumptions, latency constraints, and multi-venue extensions" are required before production readiness, suggesting the backtest results do not translate directly to live trading.
4. The best results use a "performance-first adaptive" variant, which raises concerns about in-sample optimization of the heuristic overlays (the paper's holdout methodology details are not accessible).
5. The results are on a single instrument (BTCUSDT) over a specific sample period; cross-asset generalization is untested.

## Falsification plan

- **Out-of-sample test:** Replicate the study on ETHUSDT, SOLUSDT, and other liquid perpetual contracts to test cross-asset portability.
- **Regime breakdown:** Evaluate performance during high-vol (e.g., March 2020, May 2021, FTX collapse Nov 2022) vs. low-vol regimes separately.
- **Ablation:** Test the pure RL policy vs. the adaptive variant to isolate the contribution of each heuristic overlay.
- **Cost sensitivity:** Vary maker/taker fees from 0.01% to 0.06% to test robustness to fee changes.
- **Latency stress:** Introduce realistic decision-to-fill delays (50ms, 200ms, 1s) to test degradation.
- **Sample period sensitivity:** Walk-forward validation with expanding or rolling windows rather than a single holdout.
- **Failure threshold:** If the adaptive variant's Sharpe drops below 0.5 after doubling transaction costs, or if the pure RL policy shows negative returns, the thesis is materially weakened.
- **Action on failure:** Mark as rejected for implementation; retain as reference for funding-rate-aware MDP state design methodology.

## Crypto portability

**Adapted** — The strategy is native to crypto perpetual futures and directly models crypto-specific mechanics (funding rates, perpetual contract structure). However, it is tested only on BTCUSDT on Binance Futures. Portability to other perpetual contracts (ETH, SOL, altcoins) is untested. Portability to decentralized perpetual exchanges (Hyperliquid, dYdX) is untested and would require different execution infrastructure.

Crypto-specific portability considerations:
- Funding rate intervals vary across venues (4h, 8h); the paper uses Binance's 8-hour cycle.
- Liquidity and spread characteristics differ significantly across perpetual contracts.
- The strategy assumes a single-instrument deployment; multi-asset portfolio effects are not studied.
- 24/7 trading means the agent must handle continuous operation without session breaks.

## Limitations

- **Single instrument:** Results are for BTCUSDT only. Cross-asset generalization is untested.
- **Single sample period:** One holdout period; walk-forward or multiple holdout validation is not reported.
- **Adaptive variant concern:** The best results use heuristic overlays (volatility filtering, fee-aware quoting, momentum inventory targeting) on top of the RL policy. It is unclear how much of the performance comes from the RL component vs. the heuristic overlays. An ablation separating these contributions would strengthen the evidence.
- **Data access limitation:** Full text of the paper was not accessible due to paywall; some details (exact transaction cost assumptions, fill model, PPO/SAC hyperparameters, holdout period definition, specific table references) could not be verified from primary source. All performance figures are sourced from the abstract and search snippets.
- **Not independently reproduced.**
- **Production gap:** The authors explicitly identify latency, multi-venue execution, and risk controls as prerequisites for production. The backtest does not account for these real-world constraints.
- **Publication bias:** Positive results are more likely to be published; the marginal performance of the raw RL policy suggests the field may be closer to the noise floor than the headline Sharpe implies.

## Implementation status

No implementation in our research stack. The paper provides a reproducible benchmark using public Binance data, but the full code implementation was not located in open-source repositories during this scout run.

## Adoption boundary

This record represents research-only material. It does not constitute:
- A validated or profitable strategy
- Approval for implementation
- Approval for paper trading, testnet, or live trading
- Evidence that RL market making on perpetual futures produces risk-adjusted returns after realistic execution costs

## Related Wiki records

- [[crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01]] — Pindza 2026 (same lead author) found that microstructure signals carry genuine but weak information not exploitable at retail fee levels. The RL market making paper addresses a different problem (spread optimization + funding capture) but shares the same author and venue.
- [[crypto-cex-dex-cross-venue-funding-spread-carry-2026-08-31]] — Related work on funding rate dynamics across venues.
- [[crypto-two-tiered-cex-dominant-funding-discovery-structural-arbitrage-2026-09-12]] — Zhivkov et al. 2026 on two-tiered funding rate market structure.

## Sources

1. Edson Pindza, Claude Rodrigue Bambe Moutsinga. "Reinforcement learning for automated market making in cryptocurrency perpetual futures: Integrating funding rate dynamics with historical BTCUSDT evidence." *Journal of Finance and Data Science*, 2026. DOI: [10.1016/j.jfds.2026.100197](https://doi.org/10.1016/j.jfds.2026.100197). Published June 17, 2026.

Note: Full text was not accessible due to ScienceDirect paywall. Author affiliations, sample details, and performance figures are sourced from the DOI landing page abstract and search-engine snippets. Some execution assumption details are marked as data gaps.
