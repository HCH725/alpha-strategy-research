---
schema: strategy-research-record-v1
title: "Puts + Trend-Following CVaR Hybrid Tail-Risk Allocation"
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tail-risk
  - trend-following
  - options
  - cvar
  - hybrid-hedge
  - jump-diffusion
  - stochastic-control
status: research-only
confidence: medium
source_as_of: 2026-07-01
sources:
  - "https://arxiv.org/abs/2607.00883"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Puts + Trend-Following CVaR Hybrid Tail-Risk Allocation

## Provenance

- **Primary Source:** Miquel Noguer i Alonso, Ali Al-Fallouji, "Tail Risk Management with Puts and Trend Following: A CVaR Framework for Crashes and Drawdowns", arXiv preprint `arXiv:2607.00883v1 [q-fin.MF]`, submitted July 1, 2026. Full text: https://arxiv.org/html/2607.00883v1
- **Authors:** Miquel Noguer i Alonso, Ali Al-Fallouji
- **Institution:** Artificial Intelligence Finance Institute (AIFI), Mirabaud Group
- **arXiv ID:** 2607.00883v1
- **Version date:** July 1, 2026
- **Sample period:** Stylized Monte Carlo (not historical backtest); model calibrated to representative parameters (Table 2 in source)
- **Universe:** Single risky asset class (equity-index-like); no explicit crypto calibration
- **Publication status:** Preprint (arXiv)

## Economic mechanism

### Source-reported

The authors frame tail-risk management as an **allocation problem across loss mechanisms**: abrupt crash states, volatility repricing, and persistent drawdowns require different forms of protection. Two common hedging sleeves are placed inside a single continuous-time CVaR-minimization framework:

1. **Long OTM put options (convex insurance):** Reprices immediately and contractually on jump impact. Strongest against sudden crash states but carries persistent premium drag (implied variance > realized variance).
2. **Systematic trend-following overlay (signal-driven):** Late on the first shock (signal must cross zero), but becomes increasingly defensive during persistent drawdowns without requiring fresh option premium. Can be positively carried over long samples.

The key analytical separation is **temporal**: puts hedge jump states on impact; trend hedges drawdowns that last long enough for the signal to cross through zero.

### Research interpretation

This is a **hybrid tail-risk allocation hypothesis**: a portfolio combining convex crash protection (OTM puts) with signal-driven drawdown protection (trend-following) reduces terminal CVaR relative to either pure sleeve, because the two mechanisms address complementary loss transmission channels.

Components:
- **Convex insurance sleeve:** Long OTM put options (mark-to-market, not terminal payoff)
- **Signal-driven sleeve:** Exponentially weighted log-return trend signal controlling directional exposure
- **Allocation objective:** CVaR minimization (Rockafellar-Uryasev representation)
- **Risk model:** Heston-type stochastic variance + negative Poisson jumps

The four-axis hedge-quality diagnostic separates: (a) conditional convexity, (b) tail-event reliability, (c) non-stress carry, (d) drawdown persistence.

## Signal

- **Signal formation:** Exponentially weighted log-return moving average as trend signal
- **Lookback window:** Parameterized (exact value calibration-dependent; not specified as fixed)
- **Long entry (trend sleeve):** Signal positive → directional long exposure
- **Short entry (trend sleeve):** Signal negative → directional short or defensive exposure
- **Put overlay:** Continuously held OTM puts with mark-to-market repricing
- **HJB-derived optimal allocation:** Wealth, spot, variance, and trend signal form the Markov state; directional exposure and convex-overlay exposure are jointly optimized
- **Parameters:** Heston parameters (κ, θ, ξ, ρ), jump parameters (λ, μζ, σζ), trend decay, CVaR confidence level
- **Fully specified:** Yes, within the model's parametric assumptions

## Required data

- Spot price (any liquid index or asset)
- Realized variance or implied volatility surface (for put pricing)
- Historical or simulated jump process parameters
- Trend signal constructed from log-returns
- No order-book or microstructure data required
- Timezone: N/A (continuous-time model)

## Execution assumptions

- Options: Mark-to-market accounting for put overlay; premium drag enters through physical return process (not terminal payoff)
- Trend sleeve: Signal-driven futures or overlay trades; no explicit transaction cost model in the paper
- Fill model: Not specified (stylized simulation)
- Fees/spread/slippage: Not explicitly modeled for trend sleeve; option premium drag is the primary cost
- Leverage: Directional bounds are parameterized; two-sided exposure allowed
- Capacity: Theoretical framework; no capacity analysis
- Funding: Not explicitly modeled (single-asset framework)

## Evidence

### Source-reported

The paper uses **stylized Monte Carlo experiments** (not historical backtests) with a fast Black-Scholes proxy for option valuation. Source-reported findings:

- Fixed equal-weight hybrids and grid-optimized hybrids reduce terminal CVaR relative to either pure sleeve in the reported regimes
- The exact weight location (optimal allocation between puts and trend) remains **calibration-dependent**
- The model reproduces the expected ranking of protection channels across crash, prolonged-bear, and volatility states
- The paper explicitly states: "The reported hybrid optima are best read as calibrated examples of the allocation logic developed below"

No specific Sharpe, CAGR, or drawdown numbers are reported. The evidence is mechanism validation, not performance backtesting.

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed sources; absence is not evidence of no negative result.

The paper acknowledges that:
- The exact hybrid weight is calibration-dependent
- The Black-Scholes proxy for option pricing is a simplification
- No historical backtest is provided
- The framework does not claim universal dominance of the hybrid over every possible option program or trend specification

## Falsification plan

- **Required sample:** Historical backtest across multiple asset classes and market regimes (crash, prolonged bear, volatility spike, recovery)
- **Relevant regimes:** At minimum: 2008 GFC, 2020 COVID, 2022 crypto winter, flash crash events
- **Baseline/control:** Pure OTM put program vs. pure trend-following vs. equal-weight hybrid vs. CVaR-optimized hybrid
- **Ablation tests:** Remove put sleeve, remove trend sleeve, vary CVaR confidence level, vary trend signal decay
- **Cost sensitivity:** Model explicit transaction costs for trend sleeve; test sensitivity to option bid-ask spread and roll costs
- **Out-of-sample requirement:** Walk-forward optimization on rolling windows
- **Failure metric:** If equal-weight or CVaR-optimized hybrid does not reduce CVaR vs. best pure sleeve across ≥3 independent regimes, the hybrid hypothesis is weakened
- **Action on failure:** Re-examine whether the two loss mechanisms are truly complementary in the target asset class

## Crypto portability

**Adapted**

The framework is asset-class agnostic in theory. For crypto application:
- OTM puts are available on Deribit (BTC, ETH) but with different liquidity, term structure, and skew dynamics than equity index puts
- Trend-following signals are directly applicable to crypto perpetual futures
- CVaR optimization is universal
- Crypto-specific risks: 24/7 session structure, perpetual funding rate dynamics, higher jump frequency, regime-dependent volatility clustering
- The paper does not calibrate to or test on crypto data; porting requires re-estimation of all model parameters

## Limitations

- **Theory-first paper with stylized Monte Carlo evidence** — no historical backtest
- **Black-Scholes proxy** for option pricing inside simulations (not production-grade)
- **Calibration-dependent** optimal weights — no universal allocation rule
- **No explicit transaction cost model** for the trend sleeve
- **Single-asset framework** — no cross-asset diversification analysis
- **Not independently reproduced**
- **No crypto-specific calibration or evidence**
- **Understated:** The four-axis diagnostic is proposed but not validated as a historical taxonomy

## Implementation status

Not implemented. This is a theoretical framework with stylized simulation evidence only. No production backtest, paper trading, or live implementation exists.

## Adoption boundary

A record being present in this repository does **not** mean:
- Passed Research Intake Review
- Entered Hermes Wiki Brain
- Entered the production candidate pool
- Completed Qlib full-backtest validation
- Became a frozen survivor or leaderboard entry
- Profitable
- Validated alpha
- Approved for implementation
- Approved for paper trading
- Approved for testnet
- Approved for live trading

## Related Wiki records

- [[quant/trend-following-time-series-momentum-universality-200-years]]
- [[quant/option-overlay-crash-protection-premium-drag]]
- [[quant/cvar-portfolio-optimization-tail-risk]]

## Sources

1. Miquel Noguer i Alonso, Ali Al-Fallouji, "Tail Risk Management with Puts and Trend Following: A CVaR Framework for Crashes and Drawdowns", arXiv:2607.00883v1 [q-fin.MF], July 1, 2026. https://arxiv.org/abs/2607.00883
