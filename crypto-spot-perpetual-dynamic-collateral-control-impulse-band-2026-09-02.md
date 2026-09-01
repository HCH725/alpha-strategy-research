---
schema: strategy-research-record-v1
title: "Permissionless Spot-Perpetual Basis Trading: Risk-Constrained Static Allocation and Asymmetric Dynamic Collateral Impulse Control"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - spot-perp-basis
  - funding-rate
  - collateral-control
  - impulse-control
  - hyperliquid
  - liquidation-risk
status: research-only
confidence: high
source_as_of: 2026-05-06
sources:
  - "Anatoly Krestenko, Mikhail Butov, Rostislav Berezovskiy, Danila Bolotin, 'Dynamic Collateral Control for Permissionless Spot Perpetual Basis Trading', arXiv:2605.05089v1 [q-fin.TR], May 6, 2026. DOI: 10.48550/arXiv.2605.05089. https://arxiv.org/abs/2605.05089"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Permissionless Spot-Perpetual Basis Trading: Risk-Constrained Static Allocation and Asymmetric Dynamic Collateral Impulse Control

## Provenance

- **Primary Source:** Anatoly Krestenko (Moscow Institute of Physics and Technology), Mikhail Butov (Vega Institute Foundation), Rostislav Berezovskiy (Vega Institute Foundation), and Danila Bolotin (Vega Institute Foundation / Moscow State University), *"Dynamic Collateral Control for Permissionless Spot Perpetual Basis Trading"*, arXiv preprint `arXiv:2605.05089v1 [q-fin.TR]`, submitted May 6, 2026. DOI: [10.48550/arXiv.2605.05089](https://doi.org/10.48550/arXiv.2605.05089). Full text: [https://arxiv.org/abs/2605.05089](https://arxiv.org/abs/2605.05089).
- **Primary Categories:** Quantitative Finance - Trading and Market Microstructure (`q-fin.TR`).
- **Context:** Mathematical formalization of permissionless spot-perpetual basis/carry trading (long spot vs. short perpetual) as an optimal collateral control problem under liquidation constraints, maintenance margins, carry drag, and on-chain execution wedging across venues (benchmarked on Hyperliquid and Binance).

## Economic mechanism

### Source-reported

In cryptocurrency markets, the spot-perpetual basis trade (holding long spot inventory while maintaining a short perpetual futures position to harvest positive funding rates) is traditionally viewed as a delta-neutral cash-and-carry strategy. However, in permissionless decentralized finance (DeFi) and isolated-margin perpetual venues:
1. **Collateral Partition Friction:** Total trading capital $C_t$ must be partitioned into spot inventory value $S_t Q_t$ and derivative margin collateral $M_t$. A rise in the underlying spot price $S_t$ causes unrealized losses on the short perpetual leg, depleting margin $M_t$ toward the maintenance margin fraction $MMF$, risking liquidation despite the spot position appreciating.
2. **Static vs. Risk-Constrained Benchmark:** Solving the unconstrained static expected return yields an over-leveraged allocation that maximizes funding collection at the cost of catastrophic liquidation ruin during volatility spikes. A risk-constrained formulation provides a robust operating benchmark where required collateral share increases monotonically with asset volatility $\sigma$, requiring significantly higher collateral for long-tail altcoins (e.g., LINK, DOGE) than for Bitcoin (BTC).
3. **Asymmetric Dynamic Boundaries:** When dynamic rebalancing is permitted, the control problem becomes an asymmetric impulse control band $[\underline{w}, \bar{w}]$ on the collateral fraction $w_t = M_t / C_t$:
   - The **lower intervention boundary** $\underline{w}$ is strictly dictated by solvency and liquidation avoidance (a hard barrier driven by jump risk and maintenance margin).
   - The **upper intervention boundary** $\bar{w}$ is dictated by an economic trade-off between carry drag (excess idle margin earning 0% funding) and fixed rebalancing costs (gas fees, transaction fees, and price impact).
4. **Execution Wedging:** Realized execution wedges (price impact and slippage when buying spot and opening short perps simultaneously) are asymmetric, particularly when "selling the basis," necessitating an execution buffer and minimum lot size.

### Research interpretation

The falsifiable thesis is that basis trading profitability in permissionless environments is primarily an **inventory and collateral solvency control problem**, not merely a funding prediction problem:
- Pure funding yield models underestimate the drag of idle collateral and the tail risk of liquidation caused by margin decoupling.
- The optimal dynamic operating policy is an $(s, S)$-type asymmetric impulse band: margin is left untouched within $[\underline{w}, \bar{w}]$; when price surges push $w_t \le \underline{w}$, urgent margin injection is triggered; when price drops cause excess collateral $w_t \ge \bar{w}$, capital is redeployed to spot only if the incremental funding carry exceeds the round-trip execution cost.
- Across centralized (Binance) and decentralized (Hyperliquid) architectures, venue-specific margin specifications (e.g., Hyperliquid defining maintenance margin fraction as half the maximum initial margin fraction) alter the optimal lower boundary $\underline{w}^*$.

## Signal

### State Variables and Ratio Definition
- At time $t$, total portfolio equity is $C_t = S_t Q_t + M_t + U_t$, where $S_t$ is spot price, $Q_t$ is spot inventory quantity (hedged with $-Q_t$ short perpetual contracts), $M_t$ is margin deposited in the perpetual contract, and $U_t$ is unallocated cash.
- The collateral fraction is defined as:
  $$w_t = \frac{M_t}{S_t Q_t + M_t}$$
- The position is liquidated if the margin ratio drops below the maintenance margin fraction:
  $$\frac{M_t + \text{PnL}_t^{\text{perp}}}{S_t Q_t} \le MMF$$

### Static Risk-Constrained Target
- For a given volatility $\sigma$, funding rate $f$, and maximum acceptable ruin probability $\alpha$ over horizon $T$, the static optimal collateral share $w^*$ is:
  $$w^* = \arg\max_w \mathbb{E}[\text{Carry}(w)] \quad \text{s.t.} \quad \mathbb{P}(\tau_{\text{liq}} \le T) \le \alpha$$
- Empirically, $w^*(\text{BTC}) < w^*(\text{ETH}) < w^*(\text{LINK}) < w^*(\text{DOGE})$, reflecting the monotonic relationship between volatility scaling and required liquidation buffer.

### Dynamic Impulse Control Rule
- **Lower Trigger (Solvency Intervention):**
  If $w_t \le \underline{w}$, execute an immediate rebalancing impulse:
  - Withdraw capital from spot (or transfer cash) to margin to reset $w_t \to w_{\text{target}}$.
  - If additional cash is unavailable, partially liquidate spot and perpetual legs symmetrically by fraction $\Delta Q / Q$ to restore margin coverage.
- **Upper Trigger (Carry Optimization):**
  If $w_t \ge \bar{w}$ AND the expected additional funding carry over expected holding duration $\mathbb{E}[T_{\text{hold}}]$ exceeds the round-trip rebalancing friction:
  $$f \cdot \Delta C \cdot \mathbb{E}[T_{\text{hold}}] > 2 \cdot (\text{Fee}_{\text{spot}} + \text{Fee}_{\text{perp}} + \text{Slippage}) + \text{Gas}$$
  Execute a rebalancing impulse: transfer excess margin to spot to expand hedged inventory $Q_t$, resetting $w_t \to w_{\text{target}}$.
- **Inactive Band:**
  If $\underline{w} < w_t < \bar{w}$, no rebalancing is performed (0 transaction costs incurred).

## Required data

- **Venues:** Decentralized perpetual DEXs (Hyperliquid, dYdX, Aevo) and Centralized exchanges (Binance, OKX, Bybit).
- **Instruments:** Spot tokens and matching USD/USDT/USDC perpetual contracts for major assets (BTC, ETH) and mid/alt assets (LINK, DOGE, SOL).
- **Data Feeds:**
  - L2/L3 order book depth and top-of-book quotes for spot and perpetual instruments.
  - Realized and implied 8-hour funding rates (and 1-hour funding rates on DEXs).
  - Exchange-specific margin rules: Initial Margin Fraction ($IMF$), Maintenance Margin Fraction ($MMF$), auto-deleveraging (ADL) queue rules, and liquidation fee penalties.
  - On-chain gas fee and bridge/transfer latency metrics (for cross-venue or permissionless margin transfers).
- **Frequency:** 1-second to 1-minute state monitoring for collateral tracking; tick-level execution during rebalancing events.

## Execution assumptions

- **Execution Model:** Simultaneous two-leg execution (Spot Buy + Perp Sell upon entry; Spot Sell + Perp Buy upon exit/rebalance).
- **Execution Wedges:** Realized basis spread includes taker fee (e.g. 2-5 bps), DEX routing gas costs, and order-book depth impact.
- **Venue Mechanics:**
  - Hyperliquid: $MMF = 0.5 \times IMF_{\max}$; cross-margin/isolated subaccount allocation.
  - Binance: Tiered maintenance margin brackets based on notional position size.
- **Slippage Buffer:** Execution buffer required to absorb adverse price drift between leg fills; asymmetric slippage observed during basis selling (perp leg moving faster than spot).

## Evidence

### Source-reported

- Krestenko, Butov, Berezovskiy, and Bolotin (2026, arXiv:2605.05089) demonstrate via analytical solutions, Monte Carlo simulations, and historical backtests:
  1. Unconstrained static optimization leads to aggressive over-leveraging that fails catastrophic ruin tests under real market volatility.
  2. The risk-constrained static allocation $w^*$ increases monotonically with asset volatility, requiring lower collateral for BTC than for volatile altcoins (LINK, DOGE).
  3. In dynamic Monte Carlo lifetime simulations, the lower intervention boundary $\underline{w}$ is structurally critical and active across all regimes to prevent liquidation.
  4. The upper intervention boundary $\bar{w}$ is only active and economically beneficial in high-funding, low-cost market regimes; under typical transaction costs, frequent upward rebalancing degrades net PnL.
  5. Backtesting against live routed execution on Hyperliquid and Binance confirms substantial execution wedges during basis selling, proving that minimum position size and buffer calibration are required for viable deployment.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- During severe one-way market surges (e.g., sharp short squeezes), basis widening combined with network congestion can prevent timely margin injection on-chain, causing liquidation on the perp leg before spot gains can be realized or transferred.
- When funding rates compress to near-zero or turn negative, the carry yield fails to cover the capital cost of the required margin buffer $w_t$.
- On-chain gas spikes during market stress can exceed the expected rebalancing benefit, rendering the upper boundary $\bar{w}$ economically invalid.

## Falsification plan

1. **Static vs. Dynamic Margin Stress Test:** Compare the net return and maximum drawdown of the asymmetric dynamic impulse band against static 50/50 margin allocation across historical high-volatility flash rallies (e.g., March 2024, November 2024). Falsification threshold: If the dynamic band achieves lower risk-adjusted return (Sharpe/Calmar) than the static benchmark after accounting for execution fees and slippage, reject the dynamic impulse thesis.
2. **Asset Volatility Monotonicity Test:** Calibrate $w^*(\sigma)$ across a 20-asset cross section. Falsification threshold: If empirical liquidation rates for altcoins using BTC-calibrated margin buffers exceed the risk threshold $\alpha = 0.01$, confirm that asset-specific volatility scaling is mandatory.
3. **Execution Wedge Ablation:** Measure realized slippage on simultaneous spot-perp entries across liquidity regimes. Falsification threshold: If execution wedge exceeds 50% of the annualized 30-day funding rate for position sizes $> \$100\text{k}$, basis trading capacity is falsified for non-institutional capital.

## Crypto portability

- **Direct:** The model is formulated natively for crypto permissionless and centralized spot-perpetual architectures (Hyperliquid, Binance).
- Direct application to any spot-perp pair with continuous or 8h/1h funding mechanics.

## Limitations

- **Not independently reproduced:** Results are based on Krestenko et al. (2026) preprint theoretical derivations and backtests.
- **On-chain Settlement Latency:** Model assumes instant margin rebalancing; cross-chain or wallet-to-DEX transfer delays introduce unmodeled jump-to-liquidation risks.
- **Negative Funding Regimes:** Model focuses on positive carry regimes (long spot / short perp); regime transitions to persistent negative funding require inverse position inversion not fully addressed in the base band formulation.

## Implementation status

- `not-implemented`
- Research capture only. No code deployed to PyBroker, Nautilus, or production execution engines.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- Not approved for paper, testnet, or live trading.

## Related Wiki records

- `[[crypto-perpetual-funding-rate-carry-spot-perp-2026-08-31]]`
- `[[ethena-optimal-execution-delta-neutral-steth-perp-carry-2026-09-02]]`
- `[[crypto-perpetual-autodeleveraging-trilemma-queue-haircut-2026-09-02]]`
- `[[crypto-perpetual-slippage-at-risk-sar-liquidity-early-warning-2026-09-02]]`

## Sources

1. Anatoly Krestenko, Mikhail Butov, Rostislav Berezovskiy, Danila Bolotin, *"Dynamic Collateral Control for Permissionless Spot Perpetual Basis Trading"*, arXiv preprint `arXiv:2605.05089v1 [q-fin.TR]`, May 6, 2026. DOI: [10.48550/arXiv.2605.05089](https://doi.org/10.48550/arXiv.2605.05089). Stable URL: https://arxiv.org/abs/2605.05089.
