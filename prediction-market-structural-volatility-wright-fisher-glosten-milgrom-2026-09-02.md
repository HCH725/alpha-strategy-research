---
schema: strategy-research-record-v1
title: "Structural Volatility Forecasting in Binary Prediction Markets via Wright-Fisher Resolution and Glosten-Milgrom Order Flow Channels"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - prediction-markets
  - volatility-forecasting
  - market-microstructure
  - wright-fisher
  - glosten-milgrom
  - polymarket
  - kalshi
status: research-only
confidence: medium
source_as_of: 2026-07-09
sources:
  - "Weiye Xi, Ciamac C. Moallemi, Mallesh Pai, and Shouqiao Wang, 'Volatility in Prediction Markets: A Structural Approach', arXiv:2607.08199v1 [q-fin.TR], July 9, 2026. https://arxiv.org/abs/2607.08199"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Structural Volatility Forecasting in Binary Prediction Markets via Wright-Fisher Resolution and Glosten-Milgrom Order Flow Channels

## Provenance

- **Primary Source:** Weiye Xi, Ciamac C. Moallemi, Mallesh Pai, and Shouqiao Wang, *"Volatility in Prediction Markets: A Structural Approach"*, arXiv preprint `arXiv:2607.08199v1 [q-fin.TR]`, published July 9, 2026. URL: https://arxiv.org/abs/2607.08199.
- **Primary Categories:** Trading and Market Microstructure (`q-fin.TR`), Mathematical Finance (`q-fin.MF`), Statistical Finance (`q-fin.ST`).
- **Empirical Dataset:** Comprehensive panel of binary event contracts from Kalshi across multiple categories (economics, politics, weather, entertainment, and sports).

## Economic mechanism

### Source-reported

Conventional volatility forecasting models (such as ARCH and GARCH) were designed for standard financial asset markets where prices are positive-valued unbounded processes and volatility is inferred from continuous return series. 

Binary prediction markets (such as Kalshi and Polymarket) possess three distinctive structural characteristics that invalidate vanilla ARCH/GARCH assumptions:
1. **Bounded Price Domain:** Prices represent state probabilities bounded strictly in $p_t \in (0, 1)$.
2. **Binary Terminal Payoffs:** Payoffs collapse discontinuously to $\{0, 1\}$ at resolution.
3. **Deterministic Horizon:** Contracts resolve at a known, fixed terminal deadline $T$.

The authors construct a dual-channel structural volatility framework:
1. **Wright-Fisher Deadline-Resolution Channel:** Captures the mathematical necessity that remaining binary uncertainty must be resolved as time approaches expiration. In a martingale diffusion bounded on $[0, 1]$, the instantaneous variance scales with distance from the boundaries and time-to-maturity:
   $$\sigma^2_{\text{WF}, t} = \frac{p_t (1 - p_t)}{T - t}$$
   Volatility is naturally maximized at fifty-fifty probability ($p = 0.5$) and diverges as $t \to T$.
2. **Glosten-Milgrom Order-Flow Channel:** Captures informed trading shocks and information asymmetry reflected in order book friction:
   $$\sigma^2_{\text{GM}, t} = S_t \sqrt{V_t}$$
   where $S_t$ is the prevailing bid-ask spread and $V_t$ is contract trading volume.

The combined structural model with residual GARCH dynamics achieves superior out-of-sample volatility forecasting performance compared to purely statistical autoregressive models.

### Research interpretation

This structural model provides an actionable foundation for three quantitative trading strategies in prediction markets:
1. **Dynamic Market-Maker Spread Sizing:** Automated market makers (AMMs and CLOB quoting bots) in prediction markets face severe adverse selection and inventory risk near expiration. By decomposing variance into its structural Wright-Fisher baseline $\frac{p(1-p)}{T-t}$ and informed order-flow shock $S\sqrt{V}$, quoting width can be scaled dynamically to avoid toxic fills while tightening quotes in uninformative regimes.
2. **Prediction Market Volatility Arbitrage / Mispricing Harvesting:** Where binary option derivatives or CPMM / LVR-sensitive AMM pools price options on prediction outcomes, the structural model identifies contracts whose implied volatility deviates significantly from structural fundamental variance.
3. **Cross-Category Regime Adaptation:** Economics contracts follow smooth deadline-resolution dynamics (high $\beta_1$), while sports contracts exhibit jump-like, event-concentrated information arrival (high $\beta_2$), allowing regime-differentiated risk allocation.

## Signal

### 1. Structural Volatility State Formulation

For a binary contract expiring at fixed timestamp $T$:
- At observation time $t < T$, record:
  - Mid-price / implied probability: $p_t \in (0, 1)$.
  - Time to resolution: $\tau_t = T - t$ (in years or days).
  - Bid-ask spread: $S_t = P_t^{\text{ask}} - P_t^{\text{bid}}$.
  - Rolling trading volume: $V_t$.

### 2. Dual-Channel Structural Specification

Estimate the structural instantaneous variance model:
$$\sigma_t^2 = \beta_0 + \beta_1 \left( \frac{p_t (1 - p_t)}{T - t} \right) + \beta_2 \left( S_t \sqrt{V_t} \right) + h_t$$
where $h_t$ is the residual autoregressive variance following a $\text{GARCH}(1, 1)$ process:
$$h_t = \omega + \alpha_1 \epsilon_{t-1}^2 + \beta_{\text{garch}} h_{t-1}$$
$$\epsilon_t = \Delta p_t - \mu_t$$

### 3. Alpha & Quoting Signals

- **Structural Implied Volatility:**
  $$\hat{\sigma}_t = \sqrt{\max\left(\epsilon_{\text{floor}}, \sigma_t^2\right)}$$
- **Market Quoting Spread Multiplier:**
  Set optimal bid and ask offsets $\delta_t^*$ around mid-price $p_t$:
  $$\delta_t^* = \kappa \cdot \hat{\sigma}_t \cdot \sqrt{\Delta t_{\text{quote}}} = \kappa \sqrt{\left[\beta_0 + \beta_1 \frac{p_t(1-p_t)}{T-t} + \beta_2 S_t \sqrt{V_t} + h_t\right] \Delta t_{\text{quote}}}$$
- **Volatility Arbitrage Signal ($z_{\sigma, t}$):**
  Compare model-forecasted variance $\hat{\sigma}_t^2$ against empirical realized variance over lookback window $H$:
  $$z_{\sigma, t} = \frac{\hat{\sigma}_t^2 - \sigma_{\text{realized}, t}^2}{\text{MAD}(\sigma^2)}$$
  - **Long Volatility / Spread-Widening Signal:** When $z_{\sigma, t} > +1.96$, buy cheap straddle or widen quoting bounds.
  - **Short Volatility / Liquidity Provision Signal:** When $z_{\sigma, t} < -1.96$, tighten quotes and capture inflated liquidity provider fees.

## Required data

- **Instrument Universe:** Binary prediction market contracts (Kalshi event contracts, Polymarket binary CTF tokens).
- **Venues:** CFTC-regulated prediction exchanges (Kalshi) or decentralized prediction platforms (Polymarket on Polygon).
- **Timeframe:** 1-minute, 5-minute, or 1-hour bar aggregations, alongside tick-level trade and quote data.
- **Fields:**
  - Probability / price ($p_t$).
  - Bid price ($P_t^{\text{bid}}$) and ask price ($P_t^{\text{ask}}$).
  - Trading volume ($V_t$) and trade count.
  - Exact contract settlement deadline ($T$).
  - Resolution category tag (Economics, Politics, Weather, Entertainment, Sports).

## Execution assumptions

- **Order Execution:** Limit orders posted to CLOB or liquidity provision via automated market maker (AMM) pools.
- **Transaction Costs:** 
  - Kalshi: Exchange taker/maker fee schedule per contract.
  - Polymarket: 0% trading fee on most markets; Polygon gas execution costs (< $0.01 per transaction).
- **Boundary Handling:** As $t \to T$, position limits must scale down to prevent catastrophic loss from discrete resolution jumps.
- **Settlement Protocol:** Binary settlement at either $0.00 or $1.00 upon oracle resolution.

## Evidence

### Source-reported

- **Structural Outperformance over GARCH:** Empirical evaluation on a large panel of Kalshi contracts demonstrates that structural specifications incorporating Wright-Fisher and Glosten-Milgrom terms strictly dominate plain ARCH and GARCH(1,1) benchmarks across out-of-sample forecast accuracy metrics (QLIKE and RMSE).
- **Optimal Hybrid Forecast:** The combination of structural Wright-Fisher/Glosten-Milgrom variables with residual GARCH dynamics achieved the lowest out-of-sample prediction error among all candidate architectures.
- **Cross-Category Transferability:** Out-of-sample tests revealed that category-specific parameter estimation did not systematically improve upon the pooled structural model, confirming the broad generalizability and stability of the underlying economic channels.
- **Category Information Dynamics:** Economics contracts exhibited smooth deadline-resolution convergence, whereas sports contracts showed event-concentrated, discrete jump-like dynamics.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Terminal Singularity Instability:** As $T - t \to 0$, the theoretical term $\frac{p(1-p)}{T-t}$ diverges toward infinity. Without an explicit cutoff floor $\tau_{\text{min}}$ (e.g., within 1 hour of expiry), empirical estimators become numerically unstable and generate explosive quoting bands.
- **Sports / Jump-Shock Breakdown:** In discrete-jump categories (e.g., in-play sports or election-night vote counts), information arrives as Poisson jumps rather than diffusive Wiener processes, causing diffusion-based volatility estimates to severely underestimate instantaneous tail risk.

## Falsification plan

1. **Out-of-Sample QLIKE Comparison:** Compare 1-step-ahead and $k$-step-ahead variance forecast losses (QLIKE loss metric) against a pure GARCH(1,1) baseline across 1,000 independent Polymarket/Kalshi contracts. Falsified if the structural model fails to achieve at least a $10\%$ reduction in mean QLIKE loss out-of-sample.
2. **Wright-Fisher Curvature Null Test:** Regress realized quadratic variation against the non-linear interaction term $\frac{p_t(1-p_t)}{T-t}$. Falsified if estimated coefficient $\beta_1$ is not positive and statistically significant ($t < 3.0$).
3. **Placebo Deadline Test:** Shuffle or artificially advance the expiration timestamp $T' = T + \Delta T$. Falsified if the model's predictive accuracy does not degrade substantially when provided false maturity dates.
4. **Market-Making P&L Simulation:** Simulate a quoting agent using structural spread scaling versus fixed-width spread quoting. Falsified if structural spread sizing fails to produce higher Sharpe ratio and lower maximum adverse selection drawdown.

## Crypto portability

- **Classification:** `direct`.
- **Portability Analysis:**
  - **Polymarket Implementation:** Directly applicable to Polymarket, which operates the largest decentralized binary prediction market utilizing a hybrid CLOB (Polymarket order book) and Gnosis Conditional Token Framework (CTF).
  - **Oracle / Resolution Latency:** On-chain resolution via UMA optimistic oracle introduces a discrete dispute window ($\approx 2$ hours) after event occurrence, requiring the terminal deadline $T$ in the model to represent the event occurrence timestamp rather than the on-chain assertion finalization timestamp.
  - **Liquidity & Spread Regimes:** Polymarket order books feature wider and more variable spreads $S_t$ than Kalshi, making the Glosten-Milgrom order-flow term ($S_t \sqrt{V_t}$) even more critical for crypto-native market makers.

## Limitations

- **Jump-Diffusion Omission:** The baseline model treats probability evolution as continuous diffusion plus autoregressive noise, omitting explicit compound Poisson jump processes necessary for sudden exogenous event announcements.
- **Thin Liquidity in Long-Tail Contracts:** Low-volume prediction contracts exhibit wide, stale spreads that introduce substantial measurement noise into the Glosten-Milgrom proxy.
- **Oracle Risk:** Disputed market resolutions or ambiguous resolution criteria introduce non-diffusive political/governance risk that cannot be forecasted via order book or time-to-maturity variables alone.

## Implementation status

Not implemented. No automated quoting system, PyBroker backtest, or live execution module has been constructed for this research record.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`

This record captures public empirical research on structural volatility modeling in prediction markets. It does not authorize deployment in paper, testnet, or live trading systems.

## Related Wiki records

- [[quant/prediction-market-optimal-market-making-latent-belief-hjb-2026-09-01]]
- [[quant/defi-prediction-market-uniform-loss-amm-lvr-dynamic-liquidity-2026-09-02]]
- [[quant/crypto-short-horizon-prediction-market-settlement-push-reversal-2026-09-01]]
- [[quant/spxw-0dte-vrp-learning-to-rank-2026-09-01]]

## Sources

- Weiye Xi, Ciamac C. Moallemi, Mallesh Pai, and Shouqiao Wang, *"Volatility in Prediction Markets: A Structural Approach"*, arXiv preprint `arXiv:2607.08199v1 [q-fin.TR]`, July 9, 2026. Available at: https://arxiv.org/abs/2607.08199.
