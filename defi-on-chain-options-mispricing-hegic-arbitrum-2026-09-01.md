---
schema: strategy-research-record-v1
title: "DeFi On-Chain Options Mispricing: Hegic Quotes vs Model-Based Benchmark on Arbitrum"
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - defi
  - options
  - on-chain
  - mispricing
  - arbitrum
  - heigc
status: research-only
confidence: medium
source_as_of: 2025-12-23
sources:
  - "arXiv:2512.20190, https://arxiv.org/abs/2512.20190"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# DeFi On-Chain Options Mispricing: Hegic Quotes vs Model-Based Benchmark on Arbitrum

## Provenance

- **Source:** "Pricing of wrapped Bitcoin and Ethereum on-chain options" by Anastasiia Zbandut
- **Venue:** arXiv:2512.20190, submitted 23 December 2025
- **URL:** https://arxiv.org/abs/2512.20190
- **Target instruments:** Wrapped Bitcoin (WBTC) and wrapped Ethereum (WETH) European-style options on Hegic protocol, deployed on Arbitrum
- **Benchmark model:** Black–Scholes with regime-sensitive volatility estimated via a two-regime Markov-switching AR-(GJR)-GARCH model
- **Method:** Option-level feasible GLS regression of model-implied minus Hegic quoted prices

## Economic mechanism

### Source-reported

Hegic is a decentralized options protocol on Arbitrum that quotes European-style options on wrapped crypto assets. The paper constructs a model-based fair-value benchmark using Black–Scholes with a two-regime MS-AR-(GJR)-GARCH volatility filter, then measures the systematic gap between Hegic's quoted prices and this benchmark.

Key source-reported findings:

- **Hegic quotes underprice relative to the benchmark** on average, especially for call options.
- The mispricing spread **rises** with: order size, strike moneyness, time to maturity, and estimated volatility regime.
- The mispricing spread **falls** with: trading volume on the protocol.
- **WBTC options** show larger and more persistent mispricing spreads than WETH options.
- The framework provides a data-driven approach for monitoring and calibrating on-chain option pricing logic.

### Research interpretation

The systematic underpricing of Hegic options relative to a regime-aware Black–Scholes benchmark suggests a structural mispricing signal in DeFi options markets. The hypothesized mechanism is that automated market-maker-style option pricing on Hegic does not fully incorporate:

1. **Regime-dependent volatility clustering** — the two-regime MS-AR-(GJR)-GARCH model captures volatility state switches that Hegic's simpler pricing logic may miss.
2. **Liquidity premium / illiquidity discount** — lower trading volume on Hegic correlates with larger mispricing, consistent with thinner markets pricing options less efficiently.
3. **Complexity premium for WBTC** — wrapped Bitcoin options show larger spreads, possibly because WBTC has additional bridge/custodial risk not priced by Hegic, or because WBTC options are less liquid.

A falsifiable alpha hypothesis: buying underpriced Hegic options (especially WBTC calls in high-volatility regimes with low volume) and delta-hedging the position could capture the convergence of Hegic prices toward model fair value. The converse — selling overpriced Hegic puts in high-volume, low-vol regimes — may also be viable.

## Signal

- **Signal formation:** Continuous — monitor Hegic quoted prices on Arbitrum for WBTC and WETH European options.
- **Benchmark computation:** Estimate two-regime MS-AR-(GJR)-GARCH volatility from historical underlying returns; compute Black–Scholes fair value with regime-sensitive implied volatility.
- **Mispricing metric:** Model fair value minus Hegic quoted price (option-level residuals from feasible GLS).
- **Long entry:** When Hegic quoted call price is significantly below model fair value (residual exceeds a threshold, e.g., >1.5 standard deviations of the GLS residual distribution).
- **Short entry:** When Hegic quoted put price is significantly above model fair value.
- **Exit:** Convergence of Hegic price toward model fair value, or option expiry.
- **Position sizing:** Source does not specify; likely constrained by Hegic's available liquidity per strike/expiry.
- **Parameters:** Regime-switching volatility model parameters (estimated rolling); GLS residual threshold for entry; holding period until convergence or expiry.
- **Underspecified:** Entry/exit thresholds, position sizing rules, and delta-hedging frequency are not specified in the source.

## Required data

- **Instrument:** WBTC and WETH European-style options on Hegic (Arbitrum)
- **Venue:** Hegic protocol on Arbitrum; underlying price from major CEX (Binance, Coinbase) or on-chain oracle
- **Market type:** On-chain options (European exercise)
- **Timeframe:** Daily or sub-daily Hegic quote snapshots; daily underlying returns for volatility model estimation
- **Fields required:**
  - Hegic quoted prices (bid/ask or mid) per strike and expiry
  - Underlying spot price (WBTC, WETH) time series
  - Estimated regime-sensitive volatility (two-regime MS-AR-(GJR)-GARCH)
  - Trading volume on Hegic per option series
- **Timestamp:** On-chain transaction timestamps from Arbitrum; quote snapshots with block number
- **Data gap:** Hegic historical quote data availability is uncertain; the paper uses a specific dataset that may not be publicly reproducible

## Execution assumptions

- **Signal-to-order timing:** Depends on Hegic quote update frequency and block confirmation time on Arbitrum (~0.25s block time).
- **Fill model:** Hegic options are AMM-priced; buyer pays the quoted price. No order book, so fill is deterministic at the quoted price (minus gas).
- **Fees:** Arbitrum gas costs (low but non-zero); Hegic protocol fees on option premium.
- **Slippage:** Limited by AMM pricing function; larger orders may move the on-chain price if the AMM curve is steep.
- **Impact / capacity:** Hegic liquidity per strike/expiry is limited; capacity constrained by available open interest.
- **Leverage / margin:** Options are premium-paid upfront; no margin required for long options.
- **Latency:** Arbitrum block time (~0.25s) plus potential MEV/sandwich risk on option purchase transactions.
- **Delta hedging:** Requires simultaneous spot or perp position; introduces additional execution complexity on-chain.
- **Partial fills:** Not applicable for AMM-style execution; entire premium paid atomically.

## Evidence

### Source-reported

- Source reports systematic Hegic underpricing relative to MS-AR-(GJR)-GARCH Black–Scholes benchmark, with option-level feasible GLS regression showing statistically significant coefficients.
- Mispricing spread varies predictably with order size, strike, maturity, volatility, and volume.
- WBTC options show larger and more persistent spreads than WETH options.
- This result has not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The paper does not test whether the mispricing is exploitable after accounting for Hegic protocol fees, Arbitrum gas costs, and delta-hedging costs.
- The benchmark model (two-regime MS-AR-(GJR)-GARCH Black–Scholes) may itself be misspecified; mispricing relative to one model does not guarantee mispricing relative to true fair value.
- Hegic's AMM pricing may incorporate factors not captured by the benchmark (e.g., protocol-specific risk, smart contract risk, or IL considerations for LPs).
- Absence of identified negative evidence in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

- **Required sample:** Replicate the GLS regression on a fresh out-of-sample period (e.g., post-December 2025 Hegic data).
- **Baseline / control:** Compare Hegic mispricing to mispricing on other on-chain options protocols (e.g., Dopex, Lyra, Premia) to test whether the signal is Hegic-specific or protocol-agnostic.
- **Ablation tests:** Remove regime-switching component from volatility model; test whether simple GARCH or realized volatility produces similar mispricing.
- **Cost sensitivity:** Net the mispricing against Arbitrum gas, Hegic protocol fees, and delta-hedging execution costs. If the net edge is negative after costs, the strategy is not viable.
- **Out-of-sample:** Test on a rolling forward window not used in the original calibration.
- **Failure metric:** If net mispricing (after costs) is not statistically different from zero in out-of-sample data, the hypothesis is falsified.
- **Action on failure:** Abandon the strategy or investigate whether Hegic has updated its pricing model post-publication.

## Crypto portability

adapted

The strategy is native to crypto (on-chain options on Arbitrum). However:

- Hegic's pricing logic may change after publication, eliminating the mispricing.
- On-chain options markets are nascent and illiquid; capacity is severely limited.
- WBTC bridge/custodial risk is crypto-specific and may not be captured by standard pricing models.
- The two-regime volatility model assumes stationarity that may not hold in crypto's non-stationary regimes.
- MEV and sandwich attacks on Arbitrum could erode execution quality for large orders.

## Limitations

- not independently reproduced
- data gap — Hegic historical quote data availability and reproducibility uncertain
- underspecified — entry/exit thresholds, position sizing, and delta-hedging frequency not specified
- unproven — exploitable profitability after costs not demonstrated
- The paper is a pricing study, not a backtested trading strategy; the alpha hypothesis (buy underpriced Hegic options) is inferred, not tested.

## Implementation status

not-implemented

## Adoption boundary

This record represents research material only. A record being present in this repository does not mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

## Related Wiki records

- [[crypto-options-volatility-risk-premium-zscore-2026-08-31]]
- [[crypto-options-implied-correlation-dispersion-2026-08-31]]
- [[bitcoin-options-implied-volatility-risk-reversal-skew-2026-09-01]]
- [[crypto-amm-loss-versus-rebalancing-lvr-toxic-arbitrage-2026-08-31]]
- [[defi-lending-collateral-liquidation-discount-arbitrage-2026-09-01]]

## Sources

1. Zbandut, A. (2025). "Pricing of wrapped Bitcoin and Ethereum on-chain options." arXiv:2512.20190. https://arxiv.org/abs/2512.20190
