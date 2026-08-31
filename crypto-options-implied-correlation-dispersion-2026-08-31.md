---
schema: strategy-research-record-v1
title: Crypto Options Implied Correlation Dispersion
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/tfrmma/options-volatility-trading-strats
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Options Implied Correlation Dispersion

## Provenance

- Repository URL: https://github.com/tfrmma/options-volatility-trading-strats
- Commit SHA: main (latest as of 2026-08-31)
- Exact file path: `README.md`
- Relevant source URL: https://github.com/tfrmma/options-volatility-trading-strats

## Economic mechanism

### Source-reported
Sells index volatility and buys vega-weighted component volatility, on the thesis that implied correlation is structurally too high because index puts get bid up as macro hedges. This strategy performs poorly during tail events when correlation goes to 1, hence it must be sized conservatively relative to other strategies.

### Research interpretation
The strategy harvests a correlation risk premium. Market participants often overpay for index options (to hedge broad market drawdowns), driving up the implied volatility of the index relative to the implied volatilities of its constituents. By systematically shorting the index volatility and going long the constituent volatility (dispersion trading), the strategy profits from the reversion of implied correlation to realized correlation, provided tail-risk events (where all assets crash together and correlation hits 1.0) are managed.

## Signal

- **Signal formation:** Track the implied correlation between a crypto index (e.g., a basket of major coins) and its constituents. Enter when implied correlation is high relative to historical norms.
- **Action:** Sell index volatility (e.g., short straddle on the index) and buy vega-weighted component volatility (e.g., long straddles on the components). 
- **Risk Management:** Independent pricing and delta-hedging of each leg against its own underlying spot. Conservative position sizing relative to pure volatility arbitrage to mitigate tail-event risk.

## Required data

- **Instrument:** Crypto options on an index (if available, or synthetically constructed) and options on its constituent assets (e.g., BTC, ETH, SOL).
- **Market type:** Options and Spot/Perpetual for hedging.
- **Fields:** Option chain data, Implied Volatility surface for both index and components.
- **Requirements:** Synchronized pricing and greek calculation for multiple underlyings.

## Execution assumptions

- **Delta hedging:** Each leg (index and components) must be delta-hedged independently against its own spot price.
- **Liquidity:** Requires liquid options on both the index (or proxy) and the components, which can be challenging in crypto outside of BTC and ETH.
- **Fees:** Higher execution drag due to trading multiple legs (index + all components).

## Evidence

### Source-reported
Provides a backtesting engine framework that composes one `UnderlyingBook` per underlying, allowing every leg to price, greek, and hedge off its own spot. No explicit historical performance figures are reported.

### Independently reproduced
Not independently reproduced.

### Negative evidence
None identified in the reviewed sources; absence is not evidence of no negative result.

## Falsification plan

- **Baseline:** Benchmark against the isolated performance of shorting index volatility or going long component volatility alone.
- **Ablation test:** Evaluate the impact of delta hedging frequency on the dispersion PnL given the multiple legs.
- **Failure metric:** Negative Sharpe ratio after full transaction costs, or catastrophic drawdown exceeding acceptable limits during a correlated market selloff.

## Crypto portability

`adapted`

Crypto-specific portability risks:
- Lack of liquid, tradable crypto indices with corresponding option markets. A proxy might need to be constructed using the most liquid pairs (e.g., a BTC/ETH basket), or a real index if listed on a venue like Deribit.
- Liquidity fragmentation across venues for altcoin options.
- The "correlation goes to 1" tail events are historically more frequent and violent in crypto than in traditional equities.

## Limitations

- `underspecified`: The exact definition of the index and the threshold for entering the dispersion trade are not detailed.
- `data gap`: Lack of deep options markets for a broad range of crypto assets limits the constituent pool.
- `not independently reproduced`: Has not been tested with live crypto data.

## Implementation status
No implementation in our research stack has been completed.

## Adoption boundary
This record is research material only. A record being present here does not mean it is profitable, validated alpha, or approved for implementation, paper trading, testnet, or live trading.

## Related Wiki records
None identified.

## Sources
- https://github.com/tfrmma/options-volatility-trading-strats
