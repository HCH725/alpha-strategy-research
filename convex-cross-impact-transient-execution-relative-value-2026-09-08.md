---
schema: strategy-research-record-v1
title: "Convex Cross-Impact and Transient Impact Execution Model for Relative-Value Strategies"
created: 2026-09-08
updated: 2026-09-08
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - execution
  - transaction-cost
  - cross-impact
  - transient-impact
  - relative-value
status: research-only
confidence: medium
source_as_of: 2026-09-04
sources:
  - "https://arxiv.org/abs/2609.04712"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Convex Cross-Impact and Transient Impact Execution Model for Relative-Value Strategies

## Provenance

- **Primary Source:** Vincent Yinjun-Wang (Stanford MS&E, yinjunw@stanford.edu) and Madeleine Udell (Stanford MS&E), "Convex Modeling of Price Cross-Impact over Time," arXiv preprint `arXiv:2609.04712v1 [math.OC]`, submitted September 4, 2026.
  - Stable arXiv URL: https://arxiv.org/abs/2609.04712
  - Full text HTML: https://arxiv.org/html/2609.04712v1
  - Full text PDF: https://arxiv.org/pdf/2609.04712v1
  - DOI: 10.48550/arXiv.2609.04712 (pending DataCite registration)
- **Subjects:** math.OC, q-fin.CP, q-fin.PM, q-fin.RM
- **Funding:** ONR N000142412306, AFOSR FA9550-26-1-0012, Alfred P. Sloan Foundation, Stanford HAI, IBM Research
- **Repository Deduplication:** Audited all existing `.md` records in `alpha-strategy-research`. Zero prior records cite `arXiv:2609.04712`, Vincent Yinjun-Wang, Madeleine Udell, or address convex cross-impact transient impact execution modeling for relative-value strategies. Related existing records (`passive-market-impact-optimal-execution-mlofi-2026-09-02.md`, `market-making-axiomatic-unified-inventory-quoting-spread-decomposition-2026-09-02.md`) discuss market impact from different angles (passive execution, market-making) but do not capture this specific convex cross-impact transient model or its empirical calendar-spread results.

## Economic mechanism

### Source-reported

Yinjun-Wang & Udell (2026) identify two empirical regularities that existing transaction cost models omit:

1. **Cross-impact:** A trade in one contract also moves the prices of related contracts. Relative-value trades (e.g., calendar spreads) are cheaper than the sum of independently executed legs because correlated legs' impacts partially cancel.
2. **Transient impact:** Price impact decays over time according to a power law, so an unwind recovers part of the entry cost. Later trades in the same direction pay residual impact from earlier trades.

A model that ignores these effects **overprices** the impact of relative-value trades, causing traders to forgo potentially profitable opportunities. The proposed convex quadratic cost model captures both effects simultaneously, with a positive semidefinite cross-impact matrix coupling trades across contracts and a power-law decay kernel coupling trades across periods.

### Research interpretation

The core economic hypothesis is: **multi-leg relative-value strategies in correlated markets have materially lower net execution costs than separable (leg-by-leg) impact models predict, and explicitly modeling cross-impact and transient impact enables more aggressive and more profitable positioning.**

This is a transaction cost / execution quality mechanism, not a direct alpha signal. However, it has first-order implications for the net profitability of any relative-value strategy, including:

- **Funding rate arbitrage** (long spot / short perpetual in crypto)
- **Basis trading** (futures-spot convergence)
- **Cross-exchange spread trading**
- **Calendar spread strategies** on crypto perpetuals with different expiry characteristics
- **Multi-leg relative-value** in correlated crypto perpetual pairs

The mechanism suggests that separable impact models create a "false barrier" to relative-value trades — the true cost of a two-leg trade is less than the sum of two independent one-leg costs, meaning more relative-value trades are profitable than a naive TCA would suggest.

## Signal

This paper does not define a trading signal. It defines an **execution / portfolio construction optimization framework** that modifies how existing strategies are sized and timed.

### Source-reported

The optimization problem (Equation 5 in the paper) is:

```
maximize  sum(r_t^T * x_t) - phi_imp(u) - sum(a^T |u_t|)
subject to  x_t = x_{t-1} + u_t,  x_0 = x_T = 0
            1^T x_t = 0  (calendar spread: equal dollar long/short)
            ||x_t||_1 <= x_max
            CVaR_alpha(-r_tilde^T x_t) <= r_max
```

Where:
- `r_t` = forecast returns
- `x_t` = dollar holdings (position)
- `u_t` = dollar trades
- `phi_imp(u)` = convex quadratic impact cost with cross-impact and transient impact
- `a^T |u_t|` = bid/ask spread cost

The cross-impact matrix at period t is: Λ_t = Γ_t^{1/2} C_t Γ_t^{1/2}
Where:
- Γ_t = diag(γ_{t,1}, ..., γ_{t,n}) with γ_{t,i} = ℓ_i * σ_{t,i} / v_{t,i} (self-impact: volatility/volume)
- C_t = positive semidefinite impact correlation matrix (proxy: return correlation)

The transient impact kernel: k(h) = (1 + h/τ)^{-β}, with τ=1, β=1/2 (research-proposed parameters, calibrated to the empirical setting).

The full impact cost: phi_imp(u) = u^T A u, where A = B(G ⊗ I_n)B, with G = (K + K^T)/2 and K_{ts} = k(a_t - a_s) for s ≤ t.

### Research-proposed operationalization

The parameters (τ=1, β=1/2, ℓ_i=1, α=0.95, r_max = 50 bps of x_max) are research-proposed and calibrated to the WTI crude oil empirical setting. For crypto adaptation, these would need re-estimation.

## Required data

- **Instruments:** Multiple correlated contracts (e.g., BTC perpetual vs. spot, ETH perpetual vs. spot, cross-exchange perpetual pairs)
- **Venue:** Any venue with multi-contract trading (e.g., Binance, OKX, Bybit for crypto perpetuals)
- **Market type:** Perpetual swaps, futures, or spot-perp pairs
- **Timeframe:** Daily or intraday trading periods (the model is period-agnostic; dates need not be equally spaced)
- **Fields needed:**
  - Return volatility per contract per period (σ_{t,i})
  - Dollar volume per contract per period (v_{t,i})
  - Return correlation matrix across contracts (C_t)
  - Bid/ask spread per contract
  - For transient impact: time distances between trading periods
- **Point-in-time:** All inputs must be available at the start of each period; the model freezes estimates within each month in the paper's implementation
- **Missing data:** The paper simulates dollar volume from public data (CFTC reports for WTI); for crypto, exchange-reported volume and funding data are available

## Execution assumptions

- **Signal-to-order timing:** Portfolio is optimized before each month (or planning horizon), then executed over the horizon. Paper uses a once-per-month optimization; a receding-horizon variant is suggested for practice.
- **Fill model:** Linear impact with power-law decay; no nonlinear (square-root) impact modeled
- **Fees:** Bid/ask spread explicitly included: a = (1.0, 1.5) bps for nearby/deferred (WTI). [research-proposed for crypto: would need to be re-estimated for each venue]
- **Slippage:** Captured by the cross-impact and transient impact model
- **Spread:** Explicit bid/ask cost per trade
- **Impact / capacity:** The model scales impact as σ/v (volatility/volume ratio); capacity depends on volume availability
- **Leverage / margin:** Not explicitly modeled; the CVaR risk limit implicitly caps leverage
- **Funding:** Not included (paper studies WTI futures, not perpetuals). For crypto perpetual adaptation, funding rate cost must be added to the objective.
- **Latency:** Not modeled (portfolio construction timescale, not execution timescale)

## Evidence

### Source-reported

All empirical results below trace directly to Yinjun-Wang & Udell (arXiv:2609.04712v1, Section 4, Table 1, Figure 1). Sample: WTI crude oil futures, 2004–2011 (96 months). Universe: nearby and deferred WTI contracts around S&P GSCI monthly roll.

| Policy | Alpha (bps) | Impact cost — predicted (bps) | Impact cost — simulated (bps) | Spread (bps) | Net (bps) |
|---|---|---|---|---|---|
| Baseline [9] (separable 3/2-power) | 0.6 | 1.0 | 0.0 | 0.2 | 0.4 |
| Self-impact (no cross, no transient) | 7.7 | 6.9 | 2.7 | 2.7 | 2.3 |
| Transient cross-impact (proposed) | 12.9 | 5.9 | 5.9 | 3.9 | 3.1 |

Key findings:
- The baseline separable model barely trades (net 0.4 bps) because it overprices impact and forgoes the spread opportunity.
- The self-impact model trades more aggressively (net 2.3 bps) but still overprices because it ignores cross-impact cancellation between correlated legs.
- The transient cross-impact model captures the most alpha (12.9 bps) and achieves the highest net PnL (3.1 bps) by correctly modeling that correlated legs' impacts partially cancel and that unwind recovers part of the entry cost.
- The estimated correlation between nearby and deferred WTI returns is 0.96, making cross-impact cancellation substantial.
- Calendar spread compression: nearby-minus-deferred spread falls ~41 bps over the roll window and recovers ~65 bps within two weeks (consistent with documented 30–40 bp compression).

### Independently reproduced

Not independently reproduced. All empirical findings are third-party results reported by Yinjun-Wang & Udell (2026, arXiv:2609.04712v1). No internal simulation has been conducted.

### Negative evidence

None identified in the reviewed sources; absence is not evidence of no negative result. The paper acknowledges that:
- Dollar volume is simulated (not observed from licensed exchange data)
- The model uses linear impact, not the empirically observed square-root law
- The symmetric coupling (Λ_t^{1/2} Λ_s^{1/2}) is a convexity-preserving approximation, not the true causal impact
- Results are demonstrated only on a single market (WTI crude oil) and a single strategy type (calendar spreads)

## Falsification plan

1. **Cross-impact in crypto perpetuals:** Measure actual cross-impact between correlated crypto perpetual contracts (e.g., BTC-PERP vs. ETH-PERP) by executing synthetic metaorders and measuring price response across contracts. If cross-impact in crypto is negligible (correlation < 0.3 or cross-impact coefficient statistically indistinguishable from zero), the model's advantage over separable models disappears. [research-defined falsification threshold: cross-impact correlation < 0.3]

2. **Transient impact decay rate in crypto:** Estimate the power-law decay exponent β for crypto perpetuals. If β ≈ 0 (impact does not decay) or β is very large (impact decays instantly), the transient impact component adds no value. [research-defined: β outside [0.1, 2.0] range]

3. **Net PnL improvement on crypto relative-value strategies:** Apply the convex cross-impact model to existing crypto basis/funding-rate strategies in backtest. If net PnL improvement is < 0.5 bps per trade, the practical value is marginal. [research-defined: < 0.5 bps improvement threshold]

4. **Cost sensitivity to correlation estimation:** The model's advantage depends on accurate estimation of C_t. If correlation estimation error is large (e.g., rolling EWMA with λ=0.97 is unstable in crypto's regime-switching environment), the model may perform worse than simpler baselines. [research-defined: test with rolling windows of 20, 50, 100 days]

5. **Capacity test:** If the model's advantage disappears at realistic crypto position sizes (where market impact is already captured by spread/slippage), the model adds no marginal value.

## Crypto portability

**Adapted**

The paper's model is directly applicable in structure to crypto perpetual futures, but requires material adaptations:

- **Spot vs. perpetual distinction:** The model trades two contracts (nearby/deferred). In crypto, the analogous pair is perpetual vs. spot, or two correlated perpetuals. The cross-impact structure (correlated legs partially cancel) applies equally.
- **Funding rate:** Not included in the paper's model. For crypto perpetuals, the funding rate is a material cost/benefit that must be added to the objective function.
- **24/7 session structure:** The model's period-agnostic design (dates need not be equally spaced) accommodates crypto's continuous trading.
- **Venue fragmentation:** Crypto liquidity is split across multiple venues; cross-impact may operate differently across venues than within a single venue.
- **Liquidity:** Crypto perpetuals for major assets (BTC, ETH) have substantial volume, making the model's volume-dependent impact formulation applicable.
- **Correlation structure:** Crypto perpetuals are highly correlated (BTC-PERP and ETH-PERP correlation often > 0.7), making cross-impact cancellation potentially significant.
- **Index roll analog:** Crypto has no S&P GSCI-style roll, but analogous predictable flow events exist: CME futures expiry, quarterly perpetual funding rate regime changes, and options expiry (max pain).
- **Risk:** The paper's CVaR risk limit is directly applicable to crypto.

## Limitations

- **Linear impact assumption:** The paper uses linear impact (not square-root), which understates impact for large trades. For crypto, where market impact is often nonlinear, this may be material. [underspecified for crypto]
- **Simulated volume:** Dollar volume is simulated from public data, not observed from exchange data. The model's performance may differ with actual volume data. [data gap]
- **Single market validation:** Results are demonstrated only on WTI crude oil (2004–2011). No validation on crypto, equities, or other markets. [unproven for crypto]
- **Single strategy type:** Results are for calendar spreads only. Generalization to other relative-value strategies (basis, funding rate, cross-exchange) is unproven. [unproven]
- **No funding cost:** The model does not include funding rate, which is a first-order cost for crypto perpetual strategies. [data gap for crypto adaptation]
- **Correlation estimation:** The model uses EWMA (λ=0.97) for correlation estimation. In crypto's regime-switching environment, this may be unstable. [data gap]
- **No live/in-sample distinction in the traditional sense:** The paper optimizes once per month and evaluates over the same sample period. Walk-forward or out-of-sample testing is not performed. [underspecified]
- **Publication status:** Preprint, not peer-reviewed. [not independently reproduced]

## Implementation status

Not implemented. No implementation in `nautilus-quant-system`, PyBroker, or NautilusTrader has been executed. No strategy family has been created. The model framework is captured for research reference only.

## Adoption boundary

This record is research material only. It does not represent:
- A validated alpha strategy
- An approved execution model
- Authorization for paper trading, testnet, or live trading
- A recommendation to modify any existing strategy's execution logic

The record captures a transaction cost modeling framework from a primary academic source. Any adoption would require: (1) crypto-specific calibration of cross-impact and transient impact parameters, (2) integration with funding rate and spread costs, (3) validation against naive execution baselines, and (4) formal review.

## Related Wiki records

- [[quant/passive-market-impact-optimal-execution-mlofi-2026-09-02]] — Adjacent execution/market-impact record; different focus (passive execution vs. cross-impact for relative-value)
- [[quant/market-making-axiomatic-unified-inventory-quoting-spread-decomposition-2026-09-02]] — Adjacent market-making record; mentions cross-venue leakage but from a different angle

## Sources

1. Vincent Yinjun-Wang and Madeleine Udell, "Convex Modeling of Price Cross-Impact over Time," arXiv preprint `arXiv:2609.04712v1 [math.OC]`, submitted September 4, 2026.
   - Stable arXiv URL: https://arxiv.org/abs/2609.04712
   - Full text HTML: https://arxiv.org/html/2609.04712v1
   - DOI: https://doi.org/10.48550/arXiv.2609.04712
