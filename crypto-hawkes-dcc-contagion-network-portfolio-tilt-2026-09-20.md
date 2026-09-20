---
schema: strategy-research-record-v1
title: "Crypto Hawkes-DCC Contagion Network Portfolio Tilt"
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - contagion
  - network
  - hawkes
  - dcc-garch
  - portfolio-construction
status: research-only
confidence: medium
source_as_of: 2026-09-01
sources:
  - "Edson Pindza and Jules Clement Mba. 'Contagion Dynamics in Multi-Asset Cryptocurrency Markets: A Hawkes Process and DCC-GARCH Framework.' Asia-Pacific Financial Markets, published 01 September 2026. DOI: 10.1007/s10690-026-09637-8. https://link.springer.com/article/10.1007/s10690-026-09637-8"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Hawkes-DCC Contagion Network Portfolio Tilt

## Provenance

- **Source:** Edson Pindza and Jules Clement Mba, "Contagion Dynamics in Multi-Asset Cryptocurrency Markets: A Hawkes Process and DCC-GARCH Framework," *Asia-Pacific Financial Markets*, Springer Nature, published 01 September 2026.
- **DOI:** 10.1007/s10690-026-09637-8
- **URL:** https://link.springer.com/article/10.1007/s10690-026-09637-8
- **Data source:** CryptoCompare API (publicly available daily closing prices).
- **Sample period:** 2 January 2021 to 5 March 2026 (1,889 daily observations per asset).
- **Universe:** Twenty non-stablecoin cryptocurrencies selected by market capitalisation as of January 2021: BTC, ETH, BNB, SOL, ADA, AVAX, DOT, LINK, MATIC, ATOM, UNI, LTC, XRP, ALGO, VET, ICP, FIL, XLM, THETA, XTZ. Universe fixed at start of sample to avoid look-ahead bias.

## Economic mechanism

### Source-reported

The paper identifies a source-bridge-receiver contagion network in cryptocurrency markets using Hawkes self-exciting point processes and DCC-GARCH correlation dynamics. Key source-reported findings:

1. **Contagion is driven by medium-cap platform tokens, not BTC/ETH alone.** Outgoing excitation is strongest from MATIC, ATOM, ADA, SOL, and ALGO. MATIC has the highest out-degree (5 outgoing edges) in the thresholded network. UNI has the highest in-degree (15 incoming edges) and is the dominant receiver.
2. **Correlation persistence is near-integrated.** DCC-GARCH estimates yield persistence a+b=0.9739, implying a correlation half-life of 26.2 trading days — materially slower reversion than standard equity-market benchmarks.
3. **Four contagion episodes identified:** China mining ban (6 days, June 2021), LUNA collapse (33 days, May-June 2022, peak correlation 0.791), tariff shock (1 day, April 2025), and macro risk repricing (17 days, October 2025, peak 0.780).
4. **Volatility amplification is heterogeneous.** During LUNA, BTC peaked at 0.24% daily conditional volatility while ADA reached 1.14%, XTZ 1.13%, and ATOM 1.61%.

### Research interpretation

The directed contagion network provides a falsifiable framework for regime-aware portfolio construction. The hypothesis: portfolios that underweight contagion-source assets and overweight contagion-receiver assets during stress regimes, and that account for the ~26-day correlation persistence when timing post-shock rebalancing, could achieve better risk-adjusted returns than equal-weight or static market-cap portfolios.

The source-bridge-receiver structure implies that source assets (MATIC, ADA, SOL, ATOM) amplify shocks while receiver assets (UNI, AVAX, XTZ, LINK) absorb them with lag. A portfolio tilt that reduces weight in source assets and increases weight in receiver assets during elevated-correlation regimes could reduce drawdown. The 26-day half-life implies that correlation shocks linger long enough for rolling-window risk models to understate post-crisis covariance.

**Note:** This is a research-proposed strategy hypothesis derived from the paper's descriptive findings. The paper does not propose or test a trading strategy.

## Signal

The paper does not define a trading signal. The following is a research-proposed operationalization derived from the paper's empirical findings:

- **Formation timestamp:** End-of-day (daily closing prices from CryptoCompare). Signal becomes tradable at next-day open.
- **Contagion network role classification (source-reported):**
  - **Source assets:** MATIC, ADA, SOL, ATOM, ALGO (strongest outgoing Hawkes excitation).
  - **Receiver assets:** UNI, AVAX, XTZ, LINK (highest incoming excitation).
  - **Bridge assets:** AVAX, XTZ (highest betweenness centrality).
  - **Benchmark assets:** BTC, ETH (non-negligible linkages but not dominant senders).
- **Regime filter (research-proposed):** Monitor system-mean DCC correlation. When rho_bar exceeds mean+1.5*std (the paper's contagion threshold = 0.744), enter "stress regime."
- **Portfolio tilt (research-proposed):**
  - In stress regime: underweight source assets, overweight receiver assets relative to equal-weight.
  - In normal regime: equal-weight or mild tilt toward receiver assets.
- **Rebalancing cadence (research-proposed):** Daily or every 3-5 days, aligned with DCC updating frequency.
- **Parameters:** The 1.5-sigma threshold, source/receiver asset lists, and tilt magnitudes are all research-proposed, not source-reported.
- **Signal is underspecified** in the sense that exact position-sizing, tilt magnitude, and threshold values require further research.

## Required data

- Daily closing prices for 20 non-stablecoin cryptocurrencies (BTC, ETH, BNB, SOL, ADA, AVAX, DOT, LINK, MATIC, ATOM, UNI, LTC, XRP, ALGO, VET, ICP, FIL, XLM, THETA, XTZ) against USD.
- Source: CryptoCompare API (publicly available).
- Market type: spot (daily closing prices); the paper does not use perpetual futures data.
- Timeframe: daily.
- Point-in-time: closing prices are available at end-of-day; no look-ahead bias in the paper's design.
- No funding, open interest, or order-book data required for the paper's framework. Any extension to perpetual futures would require additional data.

## Execution assumptions

- **Signal-to-order timing:** End-of-day signal, next-day open execution (research-proposed).
- **Order type:** Market orders assumed (research-proposed).
- **Fill model:** Assume full fill at next-day open (research-proposed).
- **Fees:** Not modeled in the paper. Research-proposed: assume standard maker/taker fees (e.g., 4-10 bps per side for crypto perpetuals).
- **Slippage:** Not modeled in the paper. Research-proposed: assume 5-20 bps slippage for mid-cap assets, lower for BTC/ETH.
- **Impact / capacity:** Not addressed in the paper. Medium-cap platform tokens (MATIC, ADA, SOL) have sufficient liquidity for moderate-size portfolios; receiver assets (UNI, AVAX, XTZ, LINK) also have adequate liquidity.
- **Leverage / margin:** Not addressed. Research-proposed: 1x (no leverage).
- **Funding:** Not applicable for spot; would be relevant if ported to perpetual futures.
- **Latency:** Not relevant at daily frequency.

## Evidence

### Source-reported

The paper provides the following empirical evidence (all source-reported):

1. **Contagion network structure (Table/Figure 1-2):** A 20x20 cross-excitation matrix estimated via Hawkes processes identifies MATIC, ATOM, ADA, SOL, and ALGO as primary contagion sources; UNI, AVAX, XTZ, and LINK as primary receivers. MATIC has highest out-degree (5), UNI highest in-degree (15).
2. **Correlation persistence (Section 5.3, Table 3):** DCC-GARCH yields a=0.0166, b=0.9573, persistence a+b=0.9739, half-life ~26.2 trading days.
3. **Sub-period mean correlations (Table 3):** 2021 bull: 0.6303; 2022 bear: 0.7057; 2023 recovery: 0.6699; 2024 re-entry: 0.6612; 2025-March 2026: 0.7047.
4. **Contagion episodes (Table 4):** Four episodes identified by rho_bar > 0.744 threshold. LUNA collapse most severe (33 days, peak 0.791). October 2025 macro repricing second most severe (17 days, peak 0.780).
5. **Volatility amplification (Figure 4):** During LUNA, source/bridge/receiver assets showed 4-7x higher conditional volatility than BTC/ETH.
6. **Robustness (Table 5):** Source/receiver rankings stable across alternative shock thresholds (k=1.5, 2.0, 2.5), edge cutoffs (85th, 90th, 95th percentiles), and sub-panels (5-asset, 10-asset).

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **FTX failure did not trigger a contagion episode.** The November 2022 FTX collapse pushed rho_bar to 0.738, below the 0.744 threshold, because correlations were already elevated. This suggests the threshold-based episode identification may miss stress that builds gradually.
2. **Source/receiver roles are ordinal, not knife-edge.** Robustness checks show consistent qualitative rankings but quantitative sensitivity to thresholds. The paper notes these are "descriptive features of the sample" not fixed structural properties.
3. **No out-of-sample or predictive test.** The paper is descriptive/risk-measurement, not a strategy backtest. No transaction costs, portfolio returns, or Sharpe ratios are reported for any trading strategy.
4. **Daily frequency may miss intraday contagion dynamics.** The Hawkes model operates on daily shocks; higher-frequency propagation is not captured.

## Falsification plan

1. **Required sample:** At minimum 3 years of daily data across 20+ non-stablecoin cryptocurrencies. Out-of-sample period should exclude 2021-2026 (the paper's in-sample window).
2. **Baseline / control:** Equal-weight portfolio of the 20-asset universe; market-cap-weighted portfolio; BTC-only benchmark.
3. **Ablation tests:**
   - Test portfolio tilt with only source-asset underweight (no receiver overweight).
   - Test portfolio tilt with only receiver-asset overweight (no source underweight).
   - Test without the regime filter (constant tilt regardless of DCC level).
   - Test with different contagion thresholds (1.0-sigma, 2.0-sigma).
4. **Cost sensitivity:** Vary one-way cost from 0 bps to 20 bps. Determine maximum viable cost for the strategy to remain profitable.
5. **Out-of-sample requirement:** Walk-forward or expanding-window re-estimation of Hawkes and DCC parameters. Source/receiver roles may change over time.
6. **Failure metric / threshold (research-defined):** Strategy fails if risk-adjusted return (Sharpe) does not exceed equal-weight baseline by at least 0.2 after costs over a 2-year out-of-sample period. Action on failure: abandon or re-specify signal.
7. **Regime robustness:** Test whether the 26-day half-life estimate holds in different sub-periods (bull vs bear markets).

## Crypto portability

**Adapted.** The paper studies crypto spot prices directly, so the contagion network and DCC framework are native to crypto markets. However:

- The paper uses daily spot closing prices, not perpetual futures. Porting to perpetuals requires: (a) funding rate dynamics, (b) basis risk, (c) different liquidity profiles.
- The 20-asset universe is fixed as of January 2021 and includes tokens that may have changed in market cap, liquidity, or relevance since then (e.g., MATIC rebranded to POL, VET and THETA may have lower liquidity).
- Exchange fragmentation: CryptoCompare aggregate prices are used; venue-specific contagion dynamics may differ.
- The source-bridge-receiver roles are estimated over 2021-2026 and may not persist in future regimes.
- 24/7 market structure means contagion can propagate at any time; daily frequency may understate intraday dynamics.

## Limitations

- **Descriptive, not predictive.** The paper does not backtest any trading strategy. All strategy hypotheses are research-proposed.
- **In-sample only.** No out-of-sample validation of source/receiver classifications or DCC persistence estimates.
- **Universe staleness.** The 20-asset universe is fixed at January 2021 market caps. Tokens like MATIC (now POL), VET, THETA may have changed materially.
- **Daily frequency.** Hawkes model operates on daily shocks; intraday contagion propagation is not captured.
- **No transaction costs.** The paper does not model trading costs, slippage, or capacity constraints.
- **Threshold sensitivity.** Contagion episode identification depends on the 1.5-sigma threshold; different thresholds yield different episode sets.
- **Stationarity assumption.** The Hawkes model assumes stationarity (branching ratio <1). In a rapidly evolving crypto market, source/receiver roles may shift faster than the model captures.
- **Not independently reproduced.** All findings are source-reported only.
- **Data gap:** The paper does not specify whether CryptoCompare closing prices are volume-weighted, whether delisted assets are handled, or whether the sample includes any adjustments for exchange-specific anomalies.

## Implementation status

Not implemented. No implementation in any research stack has been completed. The paper is descriptive/risk-measurement and does not provide implementable trading rules.

## Adoption boundary

This record is research material only. Its presence in this repository does not mean:
- Passed Research Intake Review;
- Entered Hermes Wiki Brain;
- Entered the production candidate pool;
- Completed Qlib full-backtest validation;
- Became a frozen survivor or leaderboard entry;
- Profitable;
- Validated alpha;
- Approved for implementation;
- Approved for paper trading;
- Approved for testnet;
- Approved for live trading.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` — Schema specification.
- No directly related strategy research records share the same source identity. Related contagion/spillover records exist (e.g., cross-asset spillover, systemic tail risk) but use different methodologies and source identities.

## Sources

1. Edson Pindza and Jules Clement Mba. "Contagion Dynamics in Multi-Asset Cryptocurrency Markets: A Hawkes Process and DCC-GARCH Framework." *Asia-Pacific Financial Markets*, published 01 September 2026. DOI: 10.1007/s10690-026-09637-8. https://link.springer.com/article/10.1007/s10690-026-09637-8
