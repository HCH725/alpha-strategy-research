---
schema: strategy-research-record-v1
title: Polymarket Binary Contract Mean-Reversion Under Transaction Cost Sensitivity
created: 2026-09-14
updated: 2026-09-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - prediction-market
  - polymarket
  - mean-reversion
  - binary-contract
  - transaction-cost
  - falsification
  - liquidity
status: research-only
confidence: medium
source_as_of: 2026-05-06
sources:
  - "Radovan Vojtko and Cyril Dujava, 'Exploiting Mean-Reversion in Decentralized Prediction Markets: Evidence from Polymarket Binary Contracts,' SSRN 6726362, May 6, 2026. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6726362"
  - "Quantpedia published version: https://quantpedia.com/exploiting-mean-reversion-in-decentralized-prediction-markets-evidence-from-polymarket-binary-contracts"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Polymarket Binary Contract Mean-Reversion Under Transaction Cost Sensitivity

## Provenance

Primary source: Radovan Vojtko and Cyril Dujava, **"Exploiting Mean-Reversion in Decentralized Prediction Markets: Evidence from Polymarket Binary Contracts,"** SSRN 6726362, written April 17, 2026; posted May 6, 2026. Affiliation: Quantpedia.

The paper studies three Polymarket binary outcome contracts: (1) "Will Jesus Christ return in 2025?" (quasi-risk-free, No side); (2) "Will China invade Taiwan in 2025?" (high-yield speculative, No side); (3) "Will the US confirm that aliens exist in 2025?" (high-yield speculative, No side). Data are 10-minute interval prices obtained via Polymarket's internal API, covering approximately one year: Jesus (2025-03-20 to 2026-01-01, 41,218 obs), China (2025-01-29 to 2026-01-01, 48,554 obs), Alien (2024-12-31 to 2026-01-01, 52,597 obs).

## Economic mechanism

### Source-reported

The authors hypothesize that binary prediction market contracts with fixed terminal settlement values ($0 or $1) create natural anchors for price reversion. Transient deviations from equilibrium prices—driven by sentiment shocks, liquidity imbalances, or information asymmetry—may be exploitable via a systematic averaging-down (mean-reversion) approach. The framework presupposes that a directional mispricing thesis has already been established (i.e., one believes a contract is mispriced), and asks whether systematic mean reversion can extract risk-adjusted returns from transient deviations during the price discovery phase.

### Research interpretation

The hypothesized mechanism is liquidity-driven transient mispricing in thinly traded binary contracts. When sentiment shocks or order-flow imbalances push prices away from fundamentals, the fixed settlement structure provides an anchor. However, the mechanism is fragile: it depends on the availability of passive limit-order execution at tight spreads. The key economic intuition is that binary contracts with near-certainty outcomes (like the Jesus contract) have very low intrinsic volatility, so transaction costs dominate the signal; speculative contracts with higher volatility have larger signal-to-noise ratios and are more cost-resilient.

## Signal

### Formation timestamp
Prices sampled at 10-minute intervals via Polymarket API. Signal computed at each observation time.

### Lookback window (X)
X-day rolling minimum of contract prices, where X ∈ {5, 10, 20} (research-defined parameter grid).

### Entry
Long signal when the current price falls at or below the X-day rolling minimum.

### Exit
Mandatory exit after Y days, where Y ∈ {1, 2, 3, 5} (research-defined parameter grid). No stop-loss or take-profit; position is held for the full Y-day period.

### Holding period
Exactly Y days (1, 2, 3, or 5 days depending on variant).

### Position sizing
Full capital reinvested upon each signal generation. No position overlap (research-defined; not specified in source).

### Parameters
All parameters (X, Y, signal thresholds) are researcher-defined grid-search values, not source-derived economic thresholds. The parameter grid spans 12 variants: X ∈ {5, 10, 20} × Y ∈ {1, 2, 3, 5}.

## Required data

- Platform: Polymarket (blockchain-based prediction market)
- Instrument: Binary outcome contracts (Yes/No, settles at $0 or $1)
- Universe: Three specific contracts analyzed; not a general universe
- Timeframe: 10-minute interval prices
- Fields: Contract price (bid/ask mid or last trade, exact method not fully specified in the Quantpedia summary)
- Settlement: Binary at $0 or $1 at expiry
- Timestamps: Not explicitly specified in available text; assumed UTC consistent with Polymarket
- Data gaps: Faulty data points toward end of 2025 (November) were interpolated using forward-fill from pandas

## Execution assumptions

### Zero-spread scenario
Passive limit-order execution with no transaction costs. Represents theoretical upper bound on achievable alpha.

### 10-basis-point spread scenario
Research-defined: 0.1% per-trade friction (0.2% round-trip). Represents aggressive market-order execution or passive execution during elevated volatility.

### Spread estimation
4-hour rolling windows, computing (high - low) / low for each window. Not a direct observable spread; this is a proxy.

### Fill model
Not explicitly specified. The zero-spread scenario assumes perfect fill at the price level; the 10 bps scenario adds a flat friction.

### Leverage / margin
Not specified. Assumed no leverage.

### Slippage / impact
Not explicitly modeled. The 10 bps spread proxy is intended to capture combined fees and slippage.

## Evidence

### Source-reported

**Buy-and-Hold benchmarks:**
- Jesus: CAR +5.98%, Sharpe +1.02, Max DD -2.37%
- China: CAR +12.69%, Sharpe +0.26, Max DD -24.29%
- Alien: CAR +8.63%, Sharpe +0.20, Max DD -21.94%

**Zero-spread (best variant per contract):**
- Jesus X5_Y1: CAR +7.95%, Sharpe +2.97, Max DD -0.61%, Calmar +13.14
- China X5_Y1: CAR +30.98%, Sharpe +1.58, Max DD -13.55%, Calmar +2.29
- Alien X5_Y2: CAR +33.33%, Sharpe +1.72, Max DD -11.54%, Calmar +2.89

**10 bps spread (best variant per contract):**
- Jesus X20_Y5: CAR +0.10%, Sharpe +0.04, Max DD -0.93% (near-zero alpha after costs)
- China X20_Y5: CAR +18.91%, Sharpe +1.96, Max DD -3.99%, Calmar +4.73
- Alien X10_Y5: CAR +22.09%, Sharpe +1.23, Max DD -11.14%, Calmar +1.98

**Key finding:** The previously optimal X5_Y1 strategy (best under zero spread) becomes the worst performer under 10 bps friction for the Jesus contract (CAR -7.83%, Sharpe -2.60). High-turnover strategies suffer disproportionately from friction. Patient strategies (X=20, Y=5) are most cost-resilient.

**Estimated spread distributions (4-hour rolling):**
- Jesus: median 0.00%, 99th percentile 0.36%, 99.9th percentile 0.63%
- China: median 0.00%, 99th percentile 1.18%, 99.9th percentile 2.21%
- Alien: median 0.05%, 99th percentile 1.65%, 99.9th percentile 12.42%

All performance figures are source-reported from Tables 3–9 of the Quantpedia publication and SSRN paper.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The central finding of the paper is itself a negative/limitation result: mean-reversion alpha degrades severely or disappears under realistic transaction costs.
- The Jesus contract (quasi-risk-free, near-100% terminal value) loses all alpha under 10 bps friction.
- High-turnover variants (short X, low Y) are the most cost-sensitive and can become deeply unprofitable.
- The 10 bps spread proxy may be optimistic for China and Alien contracts during stress periods (99.9th percentile spreads reach 2.21% and 12.42% respectively).
- The paper uses forward-fill interpolation for faulty data points, which could introduce look-ahead bias or smooth over genuine dislocations.

None identified in the reviewed sources beyond the paper's own cost-sensitivity findings; absence is not evidence of no additional negative result.

## Falsification plan

1. **Out-of-sample replication on different Polymarket contracts:** The paper tests only three contracts. Falsification requires testing on a larger, diversified universe of Polymarket binary contracts across different event types (sports, politics, crypto, science) and time periods. If the mean-reversion signal generalizes, it should appear in a random sample of 50+ binary contracts. (research-defined)

2. **Spread sensitivity sweep:** The 10 bps spread is research-defined. A systematic sweep of spread assumptions from 0 bps to 50 bps (in 5 bps increments) would identify the exact cost threshold at which each variant becomes unprofitable. (research-defined)

3. **Turnover-cost decomposition:** Separate the contribution of turnover frequency from signal quality by testing the same entry signal with mandatory longer minimum holding periods (Y ≥ 10 days). If the signal remains profitable at low turnover, the mechanism is genuine mispricing; if it vanishes, the alpha was purely an artifact of high-frequency noise. (research-defined)

4. **Execution quality audit:** The paper does not confirm actual fill quality on Polymarket. A real-money deployment with recorded fill data would test whether passive limit orders actually achieve zero-spread execution in practice. (research-defined)

5. **Competing explanation: duration bias:** Since all contracts settle to binary outcomes, any mean-reversion strategy that holds through maturity inherently benefits from convergence to terminal value. A falsification would test whether the signal still works when positions are closed before 50% of the remaining time-to-resolution. (research-defined)

## Crypto portability

**Not applicable.** This strategy is specific to prediction market binary contracts on Polymarket, not to cryptocurrency spot, perpetual futures, or on-chain DeFi instruments. The mechanism (binary settlement with fixed terminal value) does not transfer to standard crypto trading.

However, the broader insight about transaction cost sensitivity in mean-reversion strategies is relevant to crypto perpetual futures, where funding rates, slippage, and spread costs are material.

## Limitations

- **Extremely small sample:** Only three contracts tested, all on a single platform (Polymarket). Not a diversified universe.
- **Short sample period:** Approximately one year per contract. Insufficient for regime-change analysis.
- **Transaction cost proxy:** The 10 bps spread is a 4-hour rolling (high-low)/low proxy, not a directly observed bid-ask spread or fill cost. Actual execution costs on Polymarket may differ materially.
- **Forward-fill interpolation:** Faulty data points were interpolated using forward-fill, which could mask genuine price dislocations or introduce look-ahead bias.
- **No out-of-sample test:** All 12 variants were tested on the same data with a grid search. There is no true out-of-sample holdout.
- **Binary settlement convergence:** Strategies that hold through maturity benefit from the mechanical convergence of binary contracts to $0 or $1. This is a structural feature, not necessarily alpha from mean reversion.
- **No generalizability evidence:** Results are contract-specific and may not generalize to other prediction markets or event types.
- **AI-assisted writing disclosure:** The authors disclose use of Qwen3.6-Plus for "formatting assistance, language refinement, and partial support in data analysis."
- **No live or paper-trading evidence:** All results are backtested.
- `underspecified` — exact fill model, order book depth at signal time, and actual execution quality not reported.
- `not independently reproduced`

## Implementation status

Not implemented. No prototype, backtest, or deployment in our research stack.

## Adoption boundary

This record is research material only. It does not mean:
- Profitable or validated alpha
- Approved for implementation
- Approved for paper trading, testnet, or live trading

The paper's own central finding is that mean-reversion alpha in prediction markets is fragile under realistic transaction costs.

## Related Wiki records

- `[[quant/polymarket-15m-crypto-tri-transformer-market-making-2026-09-13]]` (different mechanism: Transformer-based market making on Polymarket 15-minute crypto binaries)
- `[[quant/polymarket-negrisk-executable-arbitrage-token-conversion-2026-09-03]]` (different mechanism: negative-risk arbitrage between Polymarket and token conversion)
- `[[quant/crypto-cross-platform-binary-threshold-mispricing-polymarket-binance-2026-09-01]]` (different mechanism: cross-platform binary threshold mispricing between Polymarket and Binance)
- `[[quant/kalshi-prediction-market-pricing-wedge-executable-spread-falsification-2026-09-13]]` (related: Kalshi prediction market pricing wedge with transaction cost falsification)

## Sources

1. Radovan Vojtko and Cyril Dujava. "Exploiting Mean-Reversion in Decentralized Prediction Markets: Evidence from Polymarket Binary Contracts." SSRN 6726362, May 6, 2026. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6726362
2. Quantpedia published version: https://quantpedia.com/exploiting-mean-reversion-in-decentralized-prediction-markets-evidence-from-polymarket-binary-contracts
