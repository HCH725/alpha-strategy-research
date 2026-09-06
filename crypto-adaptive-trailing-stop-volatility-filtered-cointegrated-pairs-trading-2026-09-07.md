---
schema: strategy-research-record-v1
title: "Adaptive Trailing Stop-Loss and Volatility-Filtered Cointegrated Pairs Trading in Cryptocurrency Markets"
created: 2026-09-07
updated: 2026-09-07
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - pairs-trading
  - statistical-arbitrage
  - cointegration
  - adaptive-stop-loss
  - volatility-filter
  - risk-management
status: research-only
confidence: medium
source_as_of: 2025-08-05
sources:
  - "DOI: 10.1002/fut.70018 — Palazzi, R.B. (2025). Journal of Futures Markets, 45(11), 1911-1933."
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Adaptive Trailing Stop-Loss and Volatility-Filtered Cointegrated Pairs Trading in Cryptocurrency Markets

## Provenance

- **Source:** Palazzi, Rafael Baptista, "Trading Games: Beating Passive Strategies in the Bullish Crypto Market"
- **Venue:** Journal of Futures Markets, Volume 45, Issue 11, pp. 1911-1933, published 2025-08-05
- **DOI:** 10.1002/fut.70018
- **ORCID:** 0000-0002-2657-1253
- **Affiliation:** Universidade Federal de São Paulo / University of São Paulo
- **License:** CC BY (open access)
- **Funding:** CAPES (00x0MA614) and CNPq (152052/2022-4)
- **PDF:** https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/fut.70018

## Economic mechanism

### Source-reported

The strategy examines cointegrated pairs trading in cryptocurrency markets, introducing systematic parameter optimization within the trading framework. Ten major cryptocurrencies are selected based on market capitalization and consensus mechanism. The methodology incorporates dynamic risk management through adaptive trailing stop-loss and volatility filtering mechanisms. The source reports that the pairs trading strategy consistently outperforms conventional pairs trading and passive approaches, generating significant risk-adjusted excess returns while maintaining low market exposure.

### Research interpretation

The core economic mechanism is relative-value mean reversion in cointegrated cryptocurrency pairs — when the spread between two cointegrated assets deviates from its equilibrium, a market-neutral position is entered to capture the reversion. The key novelty over standard pairs trading is the integration of two risk-management layers: (1) an adaptive trailing stop-loss that dynamically adjusts exit thresholds based on realized volatility or spread behavior, and (2) a volatility filter that gates or modulates position sizing/exposure during high-volatility regimes. The hypothesis is that these dynamic risk controls improve the Sharpe ratio and reduce drawdowns relative to static entry/exit pairs trading, by avoiding forced exits during normal mean-reversion and by reducing exposure during structural breaks or volatility spikes. This is a ported hypothesis (pairs trading originates in equity markets, e.g., Gatev et al. 2006) applied to crypto spot markets.

## Signal

- **Formation timestamp:** not specified in accessible abstract/introduction; data sample spans January 2019 to May 2024.
- **Pair selection:** Ten major cryptocurrencies selected by market capitalization and consensus mechanism; exact selection criteria and list not fully accessible from abstract/introduction (data gap).
- **Cointegration test:** Standard cointegration methodology (likely Engle-Granger or Johansen); exact test and significance threshold not fully specified in accessible sections (data gap).
- **Entry:** Spread deviation from equilibrium triggers long/short positions in the two-leg pair; exact Z-score or spread threshold not specified in accessible sections (data gap).
- **Adaptive trailing stop-loss:** Dynamic exit threshold that adjusts based on realized spread volatility or trailing maximum favorable excursion; exact functional form not specified in accessible sections (data gap).
- **Volatility filter:** Mechanism to gate or reduce position sizing during high-volatility regimes; exact filter type (e.g., rolling realized vol threshold, GARCH-based) not specified in accessible sections (data gap).
- **Parameter optimization:** Systematic parameter optimization is applied within the trading framework (overfitting risk noted).
- **Position sizing:** not specified in accessible sections (data gap).
- **Holding period:** not specified in accessible sections (data gap).

## Required data

- **Instrument / universe:** Ten major cryptocurrencies by market capitalization and consensus mechanism (exact list not specified in accessible sections; data gap).
- **Market type:** Spot cryptocurrency markets (inferred from "bullish crypto market" framing; the paper does not specify perpetual futures or derivatives; data gap).
- **Venue:** not specified in accessible sections (data gap).
- **Timeframe:** not specified in accessible sections (data gap); likely daily or intraday given the 5+ year sample period.
- **Fields:** OHLCV price data sufficient to compute cointegration spreads, trailing stop-loss thresholds, and volatility filters.
- **Sample period:** January 2019 to May 2024.
- **Transaction costs:** not specified in accessible sections (data gap).

## Execution assumptions

- The paper claims the strategy outperforms passive approaches and conventional pairs trading with low market exposure.
- Execution model, fill assumptions, slippage, spread, and fee treatment are not specified in accessible sections (data gap).
- The "systematic parameter optimization" implies in-sample parameter selection, which raises overfitting concerns unless strict walk-forward or cross-validation is applied (underspecified).
- Both legs assumed to execute simultaneously; exact live legging behavior not established.

## Evidence

### Source-reported

The source reports that the pairs trading strategy consistently outperforms conventional pairs trading and passive approaches, generating significant risk-adjusted excess returns while maintaining low market exposure. Exact Sharpe ratios, CAGR, MDD, win rates, and other performance metrics are not available from the accessible sections (data gap — full paper content not retrievable). The paper has been cited 2 times as of September 2026 (Semantic Scholar).

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed sources; absence is not evidence of no negative result. Pairs trading in crypto is known to suffer from structural breaks where cointegration relationships permanently fail, and high transaction costs can erode mean-reversion alpha. The "bullish crypto market" title framing suggests the sample period may be regime-dependent.

## Falsification plan

- Reproduce the source design: identify the ten cryptocurrencies, apply the same cointegration tests and parameter optimization framework.
- Walk-forward test: split the January 2019–May 2024 sample into formation/trading windows without overlapping selection; reject if adaptive stop-loss advantage vanishes out-of-sample.
- Cost sensitivity: test with Binance taker fees (0.04%/0.02%) and realistic slippage/spread; reject if net Sharpe falls below 0.5.
- Regime test: evaluate performance separately in bullish (2019-2021) vs bearish (2022) subperiods; reject if the strategy only works in one regime.
- Ablation: compare adaptive trailing stop-loss vs static stop-loss and volatility filter vs no filter to isolate the marginal contribution of each risk-management layer.
- Overfitting check: evaluate whether systematic parameter optimization produces stable parameters across formation windows or exhibits high variance (instability = overfitting signal).

## Crypto portability

direct

The strategy is explicitly formulated and tested for the cryptocurrency market. However, the exact venue, instrument type (spot vs. perpetual), and fee model are not specified in accessible sections (data gap).

Key portability considerations:
- Spot vs. perpetual: if tested on spot, the strategy avoids funding rate exposure but requires actual asset borrowing for short legs.
- If tested on perpetual futures, funding rate dynamics could materially affect the spread behavior and mean-reversion timing.
- 24/7 session structure means cointegration relationships may behave differently than in traditional equity markets with fixed trading hours.
- Venue fragmentation: the same pairs may show different spreads across Binance, OKX, Bybit, etc.

## Limitations

- data gap: Full paper content was not retrievable; signal construction, exact parameters, performance metrics, fee model, venue, and instrument type could not be verified from primary source. Record is based on abstract, introduction, and metadata only.
- data gap: The "systematic parameter optimization" method is not specified in accessible sections; overfitting risk is unquantified.
- data gap: Transaction cost, slippage, spread, and funding treatment not specified.
- data gap: Exact pair selection criteria and list of ten cryptocurrencies not specified.
- unproven: Not tested on our internal Nautilus/PyBroker infrastructure.
- not independently reproduced.
- Regime dependency: "bullish crypto market" title suggests results may be regime-dependent; the 2019-2024 sample includes a major bull run and a major crash, but the adaptive mechanisms' behavior across regimes is unclear.

## Implementation status

not-implemented

## Adoption boundary

research-only

## Related Wiki records

- `[[quant/crypto-pairs-trading-copula-cointegration-2026-08-31]]`
- `[[quant/crypto-drl-execution-overlay-multi-pair-trading-2026-09-01]]`
- `[[quant/crypto-factor-augmented-volatility-pairs-trading-2026-09-01]]`

## Sources

1. Palazzi, Rafael Baptista (2025). "Trading Games: Beating Passive Strategies in the Bullish Crypto Market." *Journal of Futures Markets*, 45(11), 1911-1933. DOI: 10.1002/fut.70018. Published 2025-08-05. Open Access (CC BY). https://doi.org/10.1002/fut.70018
