---
schema: strategy-research-record-v1
title: DeFi AMM Continuous-Installment Options LVR Replication and Delta Hedging
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - defi
  - amm
  - lvr
  - continuous-installment-options
  - delta-hedging
  - automated-market-making
  - exotic-options
  - adverse-selection
status: research-only
confidence: high
source_as_of: 2025-08-05
sources:
  - "Singh, S. F., Li, R. K. X., Gaskin, S., Wu, Y., Klinck, J., Michalopoulos, P., Poulos, Z., & Veneris, A. (2025). Modeling Loss-Versus-Rebalancing in Automated Market Makers via Continuous-Installment Options. arXiv preprint arXiv:2508.02971v1 [q-fin.PR]. https://arxiv.org/abs/2508.02971"
  - "Singh et al. (2025). Modeling Loss-Versus-Rebalancing in Automated Market Makers via Continuous-Installment Options. In 7th Conference on Advances in Financial Technologies (AFT 2025). Schloss Dagstuhl–Leibniz-Zentrum für Informatik, LIPIcs Vol. 327."
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# DeFi AMM Continuous-Installment Options LVR Replication and Delta Hedging

## Provenance

- **Primary source:** Srisht Fateh Singh, Reina Ke Xin Li, Samuel Gaskin, Yuntao Wu, Jeffrey Klinck, Panagiotis Michalopoulos, Zissis Poulos, and Andreas Veneris, "Modeling Loss-Versus-Rebalancing in Automated Market Makers via Continuous-Installment Options", *arXiv preprint arXiv:2508.02971v1 [q-fin.PR / cs.CR]*, published August 5, 2025. Presented at the *7th Conference on Advances in Financial Technologies (AFT 2025)*, Schloss Dagstuhl – Leibniz-Zentrum für Informatik, LIPIcs Vol. 327. URL: https://arxiv.org/abs/2508.02971.
- **Related foundational works:**
  - Milionis, J., Moallemi, C. C., Roughgarden, T., & Zhang, A. L. (2022). Automated Market Making and Loss-Versus-Rebalancing. *arXiv:2208.06046*.
  - Davis, M. H., Guo, X., & Wu, G. (2001). Impulse Control of Brownian Motion and Continuous-Installment Options. *Mathematical Finance*, 11(2), 173-193.
  - Adams, H., et al. (2021). Uniswap v3 Core. *Uniswap Whitepaper*.
- **Context:** While standard literature identifies Loss-Versus-Rebalancing (LVR) as the adverse-selection cost of passive market making, Singh et al. (2025) provide an exact mathematical option-theoretic equivalence: an AMM liquidity position is analytically identical to a portfolio of perpetual American continuous-installment (CI) options with early-withdrawal optionality.
- **Public-use status:** Open-access academic publication and arXiv preprint.

## Economic mechanism

### Source-reported

In Constant-Function Automated Market Makers (CFAMMs) such as Uniswap v2 and concentrated liquidity pools like Uniswap v3, liquidity providers (LPs) supply token reserves along an invariant curve (e.g. $x \cdot y = k$). 

External arbitrageurs continuously monitor the pool price against external liquid venues (CEXs) and execute toxic arbitrage trades whenever pool prices become stale, extracting rent from passive LPs. This running adverse-selection cost is formalized as Loss-Versus-Rebalancing (LVR).

Singh et al. (2025) prove the following theoretical foundations:
1. **Perpetual American Continuous-Installment Option Payoff:** Unlike European options with fixed maturities, an AMM LP position has no expiry date and can be terminated at any chosen stopping time by burning liquidity. This makes the LP position structurally equivalent to a perpetual American continuous-installment (CI) option portfolio.
2. **LVR as Option Theta:** The paper analytically proves that the running instantaneous Loss-Versus-Rebalancing of the AMM LP position is mathematically equal to the continuous installment rate / time-decay ($\Theta$) earned/paid on the embedded at-the-money CI options in the replicating portfolio.
3. **Constant LVR Boundaries:** The authors derive a specialized delta profile and price boundary conditions under which an AMM position experiences a strictly price-independent, constant LVR rate over an arbitrarily long investment horizon.
4. **Volatility Calibration:** Because continuous volatility $\sigma$ in perpetual options cannot be assumed static, the framework introduces a systematic calibration mapping the term structure of implied volatilities (from Deribit options) to the perpetual CI option parameters.

### Research interpretation

The alpha hypothesis is **LVR-immunized delta-neutral liquidity provision and fee-spread extraction**:

1. By decomposing the CFAMM liquidity position into its continuous-installment option replicating portfolio, an LP can dynamically compute its exact analytical delta $\Delta_{\text{AMM}}(S_t)$ and hedge directional exposure on liquid perpetual futures (e.g., Binance, Hyperliquid, Deribit).
2. The remaining net return is:
   $$\text{PnL}_{\text{net}} = \text{Collected Pool Fees} - \text{Realized LVR} - \text{Delta Hedging Costs}$$
3. Because LVR is proven to equal the continuous-installment option $\Theta(\sigma_{\text{implied}})$, an LP can formulate a deterministic break-even condition: an LP should supply liquidity if and only if the expected retail fee yield exceeds the continuous installment theta $\Theta_{\text{CI}}(S_t, \sigma_{\text{implied}})$.
4. Furthermore, constructing liquidity distribution across ticks matching the derived "Constant-LVR profile" stabilizes running adverse-selection drag, eliminating the severe convex LVR spikes that occur when prices linger near narrow concentrated liquidity boundaries.

## Signal

The normalized signal and execution strategy operate as follows:

1. **Continuous Volatility Calibration:**
   - At timestamp $t$, sample the implied volatility term structure $\sigma_{\text{IV}}(T_i)$ from liquid Deribit/CME Bitcoin or Ethereum options across multiple expirations ($T_1, T_2, \dots, T_n$).
   - Fit the term structure to calibrate the effective perpetual continuous-installment parameter $\sigma_t^*$.

2. **Continuous-Installment Option Theta & LVR Benchmark:**
   - Compute the instantaneous theoretical LVR drag rate per unit of liquidity $L$:
     $$\Theta_{\text{CI}}(S_t, \sigma_t^*) = \frac{1}{8} (\sigma_t^*)^2 S_t L$$
   - Estimate the forecastable uninformed retail fee generation rate $\hat{f}_t = \mathbb{E}[\text{FeeRate}_t \mid \text{RetailFlowVolume}_t]$.

3. **Active Liquidity Allocation Decision:**
   - **Enter / Supply Liquidity:** Enter when $\hat{f}_t > \Theta_{\text{CI}}(S_t, \sigma_t^*) \cdot (1 + \text{CostBuffer})$.
   - **Exit / Withdraw Liquidity:** Burn liquidity when $\hat{f}_t \le \Theta_{\text{CI}}(S_t, \sigma_t^*)$, avoiding toxic adverse-selection regimes.

4. **Constant-LVR Tick Distribution:**
   - Deploy capital across concentrated liquidity price interval $[S_{\text{lower}}, S_{\text{upper}}]$ structured according to the Singh et al. constant-LVR density function:
     $$\Delta_{\text{AMM}}(S) = \frac{\sqrt{S_{\text{upper}}} - \sqrt{S}}{\sqrt{S_{\text{upper}}} - \sqrt{S_{\text{lower}}}}$$
     yielding a linear delta decay and uniform LVR accumulation per price unit.

5. **Dynamic Delta Hedging Engine:**
   - At each block interval $t_k$, observe underlying reference price $S_{t_k}$.
   - Compute total portfolio delta $\Delta_{\text{AMM}}(S_{t_k})$.
   - Compare with existing hedge position $H_{t_k}$ in perpetual futures:
     $$\delta_{\text{imbalance}} = \Delta_{\text{AMM}}(S_{t_k}) + H_{t_k}$$
   - **Hedge Rebalance Trigger:** If $|\delta_{\text{imbalance}}| > \epsilon_{\text{threshold}}$ (e.g. $0.05 \text{ BTC}$), submit market/limit order on perpetual exchange to adjust $H_{t_{k+1}} = -\Delta_{\text{AMM}}(S_{t_k})$.

6. **Specification Boundary:**
   - The paper fully specifies the theoretical equivalence proofs, delta profiles, and volatility calibration equations. The exact retail order flow predictor ($\hat{f}_t$) and discrete delta-hedging threshold ($\epsilon_{\text{threshold}}$) require empirical tuning against venue gas and maker/taker fee structures.

## Required data

- **DEX Pool State:** Uniswap v3 / concentrated liquidity tick-level liquidity distribution ($L$), tick spacing, cumulative swap fees, and real-time reserves ($x_t, y_t$).
- **Reference CEX / Mark Price:** High-frequency mid-price $S_t$ from primary liquid CEX / perpetual venues (e.g. Binance BTCUSDT / ETHUSDT, Hyperliquid).
- **Options Implied Volatility Surface:** Deribit BTC/ETH options surface across strike and maturity grids to calibrate continuous perpetual parameter $\sigma_t^*$.
- **Perpetual Futures Venue:** Bid/ask quotes, funding rate, taker/maker fee schedule, and position margin status for dynamic delta-hedging execution.
- **Gas & Network State:** Ethereum / Arbitrum base fee (EIP-1559), priority gas fees, and block timestamp synchronization.

## Execution assumptions

### Source-reported assumptions

- Continuous-time asset price follows geometric Brownian motion $dS_t = \mu S_t dt + \sigma S_t dW_t$.
- Liquidity provider has early-exercise optionality to costlessly withdraw liquidity at any stopping time.
- Theoretical market with frictionless continuous trading.

### Practical implementation assumptions

- **Discrete Hedging Lag:** Delta hedging occurs at discrete intervals (block times $\Delta t \approx 12\text{s}$ on Ethereum L1, $\approx 250\text{ms}$ on Arbitrum), creating gamma slippage / discrete hedging tracking error.
- **Hedging Costs:** Perpetual futures taker fee ($\approx 2–5\text{ bps}$) and funding rate payments incurred on the short perpetual hedge.
- **On-chain Gas Costs:** Gas fees incurred when minting, burning, or collecting fees from the AMM position.
- **Toxicity Divergence:** In periods of extreme market momentum, informed order flow dominates retail swaps, causing realized LVR to outstrip theoretical theta.

## Evidence

### Source-reported

Singh et al. (2025) demonstrate:
- Analytical proof of exact equivalence between CFAMM LVR and perpetual American continuous-installment option time-decay ($\Theta$).
- Mathematical derivation of the Constant-LVR liquidity profile that linearizes delta progression across the price band $[S_{\text{lower}}, S_{\text{upper}}]$.
- Calibration framework demonstrating that calibrating perpetual continuous volatility from Deribit IV surfaces provides superior out-of-sample adverse-selection tracking compared to naive historical rolling realized volatility.
- Closed-form formulas for the value function of the LP withdrawal option.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Volatile Jump Regimes:** In discontinuous jump regimes (flash crashes, de-pegs), continuous-installment option delta replication breaks down, resulting in severe unhedged inventory losses before perpetual hedges can be executed.
- **Perpetual Funding Drag:** Maintaining a continuous short delta hedge on crypto perpetuals exposes the LP to structural positive funding rates (bull market carry drag), which can erode net fee gains.
- **Gas vs Fee Inefficiency on L1:** On Ethereum mainnet, gas costs for active liquidity repositioning and frequent mint/burn operations often exceed the fee margin for sub-$1M LP pools.

## Falsification plan

The strategy hypothesis should be deemed falsified if:
1. **Delta-Hedged PnL Deficit:** Across a 6-month walk-forward backtest on major pairs (e.g., ETH/USDC, WBTC/USDC), net PnL of the CI-option delta-hedged LP strategy is negative after subtracting perpetual trading fees, funding costs, and on-chain gas.
2. **Implied Volatility Miscalibration:** The Deribit-calibrated continuous volatility $\sigma_t^*$ fails to anticipate realized LVR spikes, resulting in a lower Information Ratio than a simple static 30-day realized volatility baseline.
3. **Constant-LVR Profile Inefficiency:** The constant-LVR liquidity profile earns lower fee-to-LVR ratios than standard concentrated single-tick LP allocations across empirical market regimes.
4. **Discrete Hedging Leakage:** Discrete hedging intervals on Layer-2 venues generate gamma slippage that exceeds $50\%$ of the gross collected AMM fees during high-volatility days ($\sigma > 80\%$ annualized).

## Crypto portability

**Direct**: The mechanism is explicitly derived for decentralized automated market makers (Uniswap v2/v3, Curve, Sushiswap) and delta-hedging on cryptocurrency derivatives exchanges (Deribit, Binance Futures, Hyperliquid).

Portability considerations:
- Direct implementation on EVM Layer-2s (Arbitrum, Base, Optimism) where low gas costs permit frequent liquidity rebalancing.
- Direct applicability to Solana concentrated liquidity AMMs (Orca Whirlpools, Raydium CLMM).
- Derivatives hedging can be executed across centralized exchanges or decentralized perpetual protocols (Hyperliquid, dYdX).

## Limitations

- **not independently reproduced**;
- **theoretical continuous-time assumption:** real-world discrete block times introduce hedging error;
- **funding rate exposure:** short delta hedge on perpetuals carries variable funding cost;
- **execution friction:** requires simultaneous monitoring of on-chain pool states, options volatility surfaces, and CEX perpetual order books;
- **retail order flow volatility:** retail fee generation is stochastic and can evaporate during low-volume consolidation periods.

## Implementation status

not-implemented

No implementation in PyBroker, NautilusTrader, or internal trading pipelines has been performed.

## Adoption boundary

research-only

This record is research material only. It does not constitute investment advice, a validated profitable strategy, or authorization for Paper, Testnet, or Live trading execution.

## Related Wiki records

- [[quant/crypto-amm-loss-versus-rebalancing-lvr-toxic-arbitrage-2026-08-31]] — foundational Milionis et al. LVR and toxic arbitrage framework.
- [[quant/crypto-deribit-options-volatility-of-volatility-vov-realized-quarticity-2026-09-01]] — Deribit options volatility surface dynamics.
- [[quant/crypto-dex-pdlp-delta-neutral-liquidity-provision-2026-08-31]] — delta-neutral LP strategies on decentralized exchanges.

## Sources

1. Singh, S. F., Li, R. K. X., Gaskin, S., Wu, Y., Klinck, J., Michalopoulos, P., Poulos, Z., & Veneris, A. (2025). "Modeling Loss-Versus-Rebalancing in Automated Market Makers via Continuous-Installment Options." *arXiv preprint arXiv:2508.02971v1 [q-fin.PR / cs.CR]*, published 5 August 2025. URL: https://arxiv.org/abs/2508.02971
2. Singh, S. F., et al. (2025). "Modeling Loss-Versus-Rebalancing in Automated Market Makers via Continuous-Installment Options." In *Proceedings of the 7th Conference on Advances in Financial Technologies (AFT 2025)*. Schloss Dagstuhl – Leibniz-Zentrum für Informatik, LIPIcs Vol. 327. DOI: https://doi.org/10.4230/LIPIcs.AFT.2025.15
3. Milionis, J., Moallemi, C. C., Roughgarden, T., & Zhang, A. L. (2022). "Automated Market Making and Loss-Versus-Rebalancing." *arXiv preprint arXiv:2208.06046*. URL: https://arxiv.org/abs/2208.06046
