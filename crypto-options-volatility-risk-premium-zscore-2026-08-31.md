---
schema: strategy-research-record-v1
title: Crypto Options Volatility Risk Premium (VRP) Z-Score Harvesting
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

# Crypto Options Volatility Risk Premium (VRP) Z-Score Harvesting

## Provenance

- Repository URL: https://github.com/tfrmma/options-volatility-trading-strats
- Commit SHA: main (latest as of 2026-08-31)
- Exact file path: `README.md`
- Relevant source URL: https://github.com/tfrmma/options-volatility-trading-strats

## Economic mechanism

### Source-reported
Systematic variance risk premium harvesting. Implied volatility is persistently above realized volatility on average, but the premium compresses, occasionally inverts, and goes haywire around macro events. Trading the VRP z-score against its own trailing history avoids selling volatility mechanically every time IV > RV.

### Research interpretation
The economic mechanism relies on the structural overpricing of implied volatility relative to realized volatility (Volatility Risk Premium), which compensates volatility sellers for tail risks. By using a z-score of the VRP instead of a simple threshold, the strategy adapts to changing market regimes and volatility cycles, sizing positions according to the conviction level of the dislocation rather than taking a static exposure.

## Signal

- **Signal formation:** Calculate the VRP (Implied Volatility - Realized Volatility) and its trailing z-score.
- **Action:** Trade the VRP z-score against its own trailing history. On a "hold" signal, dynamically scale the existing position toward a new conviction-weighted vega target, trimming or adding at the same strikes subject to a tolerance band to minimize trading costs.
- **Risk Management:** Vega-based position sizing and dynamically hedging delta.

## Required data

- **Instrument:** Crypto options (e.g., BTC, ETH) and their underlying spot/futures.
- **Market type:** Options and Spot/Perpetual for hedging.
- **Fields:** Option chain data, Implied Volatility surface, historical Realized Volatility.
- **Requirements:** Options data requires modeling of the volatility surface (e.g., using SVI or Gatheral models) and strike interpolation.

## Execution assumptions

- **Delta hedging:** Continuous or band-based (Whalley-Wilmott bands) delta hedging of the options positions.
- **Fees and Spread:** Subject to a tolerance band so it isn't paying the spread on every small wobble. Fee-aware band width for delta hedging.
- **Liquidity:** Sufficient liquidity across the option chain for scaling into and out of positions without excessive market impact.

## Evidence

### Source-reported
Source asserts strategy logic and provides a backtesting engine but does not report specific historical Sharpe ratios or CAGR figures.

### Independently reproduced
Not independently reproduced.

### Negative evidence
None identified in the reviewed sources; absence is not evidence of no negative result.

## Falsification plan

- **Baseline:** Compare against a naive systematic short straddle/strangle strategy (selling anytime IV > RV).
- **Ablation test:** Test the impact of the z-score sizing and tolerance bands vs. simple threshold execution.
- **Failure metric:** Sustained negative PnL or Sharpe < 1.0 in out-of-sample backtests, particularly after accounting for crypto option bid-ask spreads and trading fees.

## Crypto portability

`direct`

Crypto-specific portability risks:
- Options liquidity on crypto venues is heavily concentrated in certain expiries and strikes.
- High transaction costs (spread + fees) can consume the entire variance risk premium if the rebalancing tolerance band is too tight.
- Tail events in crypto are larger than in traditional finance, which can lead to significant drawdown for short volatility strategies.

## Limitations

- `underspecified`: The exact lookback windows for the VRP z-score and the specific tolerance bands for scaling are not fully detailed.
- `not independently reproduced`: Has not been verified in internal simulation.

## Implementation status
No implementation in our research stack has been completed.

## Adoption boundary
This record is research material only. A record being present here does not mean it is profitable, validated alpha, or approved for implementation, paper trading, testnet, or live trading.

## Related Wiki records
None identified.

## Sources
- https://github.com/tfrmma/options-volatility-trading-strats
