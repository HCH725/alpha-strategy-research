---
schema: strategy-research-record-v1
title: "Concentrated Liquidity Market Maker Path-Dependent Liquidity Provision: Win-Score Area Metric, 15-Position Taxonomy, and Early Barrier Profit-Taking"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto-microstructure
  - concentrated-liquidity
  - uniswap-v3
  - aerodrome
  - base-chain
  - path-dependent-pnl
  - win-score
  - barrier-exit
status: research-only
confidence: high
source_as_of: 2026-04
sources:
  - "Andrey Urusov, Rostislav Berezovskiy, Anatoly Krestenko, and Andrei Kornilov, 'Liquidity provision in CLMMs: evidence from transactions data', arXiv:2604.22069v1 [q-fin.TR, q-fin.CP], April 2026. DOI: 10.48550/arXiv.2604.22069. https://arxiv.org/abs/2604.22069"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Concentrated Liquidity Market Maker Path-Dependent Liquidity Provision: Win-Score Area Metric, 15-Position Taxonomy, and Early Barrier Profit-Taking

## Provenance

- **Primary Source:** Andrey Urusov, Rostislav Berezovskiy, Anatoly Krestenko, and Andrei Kornilov, *"Liquidity provision in CLMMs: evidence from transactions data"*, arXiv preprint `arXiv:2604.22069v1 [q-fin.TR, q-fin.CP]`, published April 2026. DOI: [10.48550/arXiv.2604.22069](https://doi.org/10.48550/arXiv.2604.22069). Full text: [https://arxiv.org/abs/2604.22069](https://arxiv.org/abs/2604.22069).
- **Primary Categories:** Trading and Market Microstructure (`q-fin.TR`), Computational Finance (`q-fin.CP`).
- **Context:** While Concentrated Liquidity Market Makers (CLMMs, such as Uniswap v3 and Aerodrome Slipstream) dramatically increase capital efficiency by allowing Liquidity Providers (LPs) to allocate reserves within customized price intervals $[a, b]$, empirical literature has struggled to characterize the path-dependent profitability of active LP strategies. Urusov et al. reconstruct exact historical transaction-level PnL paths across WETH/USD pools on the Base network, introduce a continuous "win-score" area metric $\omega$, establish a complete 15-class structural position taxonomy, and uncover the behavioral rules that distinguish the profitable ~16.7% minority of LPs from losing participants.

## Economic mechanism

### Source-reported

1. **Path-Dependent PnL vs. Terminal Endpoint Flaw:** Evaluating an LP position purely at terminal burn time $t = T$ creates severe survival and selection bias. An LP may experience positive cumulative PnL for 95% of its holding time, only to be closed during an adverse tail-divergence spike. The path-dependent "win-score" metric captures the area under the cumulative PnL curve:
   $$\omega = \frac{A^+}{A^+ + A^-} \in [0, 1]$$
   where $A^+$ is the integrated area of positive cumulative PnL states and $A^-$ is the integrated area of negative cumulative PnL states.
2. **Empirical Profitability Deficit:** Across transaction-level on-chain data for Base WETH/USD pools, only approximately **1 in 6 LPs (~16.7%)** achieve positive terminal PnL after accounting for divergence loss / impermanent loss and gas fees. Furthermore, only **1 in 7 LPs (~14.3%)** are "consistently successful" (achieving both $\mathrm{PnL}_T \ge 0$ and win-score $\omega > 0.5$).
3. **15-Position Structural Taxonomy:** Positions are classified into a 15-state taxonomy based on initial pool price $P_{\mathrm{start}}$, terminal price $P_{\mathrm{end}}$, and lower/upper range boundaries $[a, b]$:
   - Centered inside range ($a < P_{\mathrm{start}} < b$).
   - One-sided limit orders ($P_{\mathrm{start}} \le a$ or $P_{\mathrm{start}} \ge b$).
   - Boundary traversal transitions (e.g., entering in-range, traversing through, and exiting out-of-range).
4. **The Early Barrier Profit-Taking Alpha:** Profitable LPs systematically exhibit two distinct operational behaviors:
   - **Tight Mid-Concentration:** Initial liquidity is concentrated tightly around the entry pool price ($P_{\mathrm{start}} \approx \sqrt{a b}$), maximizing instantaneous fee accrual density during high-activity regimes.
   - **Early Exit Before Full Boundary Traversal:** Profitable LPs do not passively wait for price to breach range boundaries $a$ or $b$; instead, they actively close/burn the position before the full price interval is traversed once cumulative fee revenue reaches target thresholds. This converts the short gamma profile of CLMM liquidity provision into an embedded profit-taking barrier option.
5. **Cross-Pool Multi-LP Specialization:** A specialized class of sophisticated "multi-LPs" operates concurrently across competing DEX protocols on Base (e.g., Uniswap v3, Aerodrome, PancakeSwap, SushiSwap), actively reallocating capital to capture fee surges driven by DEX volume shifts.

### Research interpretation

The falsifiable thesis is that **CLMM LP alpha is generated not by passive liquidity provision, but by active barrier management: concentrating liquidity tightly around entry price and triggering an early position burn when either (1) accumulated fee yield reaches a take-profit target or (2) price approaches an endogenous barrier distance $d_{\mathrm{exit}} = \theta (b - a)$ before full boundary crossing**:
- LPs who passively hold positions until boundary breach suffer maximal Loss-Versus-Rebalancing (LVR) and adverse selection from toxic informed order flow.
- Active early barrier exit truncates the left tail of divergence loss, shifting the win-score $\omega$ above the 0.5 threshold and generating positive net expectation.

## Signal

### 1. Position Initialization (Entry State)

At time $t_0$, observe pool price $S_0 = P_{\mathrm{pool}}(t_0)$ and 1-hour realized volatility $\hat{\sigma}_t$:
- Set tight concentrated price bounds $[a, b]$ symmetric in log-space:
  $$a = S_0 e^{-k \hat{\sigma}_t \sqrt{\Delta t}}, \quad b = S_0 e^{+k \hat{\sigma}_t \sqrt{\Delta t}}$$
  with concentration factor $k \in [0.5, 1.5]$ and expected horizon $\Delta t \in [1\text{h}, 24\text{h}]$.
- Mint concentrated liquidity $L = \frac{\Delta x}{\frac{1}{\sqrt{S_0}} - \frac{1}{\sqrt{b}}} = \frac{\Delta y}{\sqrt{S_0} - \sqrt{a}}$.

### 2. Path-Dependent Cumulative PnL Tracking

At each block $t \ge t_0$:
- Compute cumulative fee earnings $F(t) = \int_{t_0}^t \frac{L}{L_{\mathrm{total}}(u)} \gamma_{\mathrm{fee}} dV_{\mathrm{swap}}(u)$.
- Compute mark-to-market position value $V_{\mathrm{LP}}(t, S_t) = x(S_t) S_t + y(S_t)$.
- Compute divergence PnL relative to initial hold baseline $V_{\mathrm{hold}}(t) = x(S_0) S_t + y(S_0)$:
  $$\Delta \mathrm{PnL}(t) = V_{\mathrm{LP}}(t, S_t) + F(t) - V_{\mathrm{hold}}(t) - \mathrm{GasCosts}$$
- Update running positive and negative PnL integration areas $A^+(t)$ and $A^-(t)$.

### 3. Barrier Early Exit Triggers

Execute an atomic position burn (liquidity removal and token swap back to initial asset weights) when ANY of the following rules is satisfied:
1. **Take-Profit Barrier:** Cumulative fee yield exceeds target ratio:
   $$F(t) \ge \alpha_{\mathrm{target}} \cdot V_{\mathrm{LP}}(t_0)$$
2. **Boundary Distance Proximity Barrier (Early Exit):** Current pool price drifts near the outer boundary:
   $$\frac{\min(S_t - a, b - S_t)}{b - a} \le \theta_{\mathrm{barrier}} \quad (\text{default } \theta_{\mathrm{barrier}} = 0.15)$$
   *Critical rule:* Close the position *before* the price exits the range and turns the position entirely into the depreciating asset.
3. **Win-Score Decay Stop:** If running win-score falls below threshold $\omega(t) < 0.30$ after a minimum holding window $t - t_0 > 2\text{ hours}$.

## Required data

- **Venues & Pools:** WETH/USD pools across Base Layer-2 DEXs:
  - Uniswap v3 (0.05% and 0.30% fee tiers).
  - Aerodrome Slipstream (concentrated liquidity pools).
  - PancakeSwap v3 (Base).
  - SushiSwap v3 (Base).
- **On-Chain Event Logs:** Full-fidelity event logs decoded via RPC or archive nodes:
  - `Mint` (liquidity addition, tick lower, tick upper, amounts).
  - `Burn` (liquidity removal).
  - `Swap` (amount0, amount1, sqrtPriceX96, liquidity, tick).
  - `Collect` (fee withdrawal amounts).
- **Gas & L2 Base Fee Data:** `baseFeePerGas`, `priorityFee`, and L1 data submission overhead fees.

## Execution assumptions

- **Transaction Submission:** EIP-1559 transactions on Base L2 with priority gas bidding to ensure inclusion within $\le 1\text{ block}$ ($< 2\text{s}$).
- **Gas Drag:** L2 execution gas costs (~$0.01 to $0.05 per mint/burn on Base) factored into net PnL calculations.
- **Slippage on Exit:** Liquidity burn is accompanied by an immediate rebalancing swap through DEX aggregator or pool to return to target delta-neutral or original asset allocation.

## Evidence

### Source-reported

- **Empirical Dataset:** Full on-chain transaction logs of all liquidity provision events in WETH/USD pools on Base chain covering Uniswap, Aerodrome, PancakeSwap, and SushiSwap.
- **Key Empirical Statistics:**
  - **Overall LP Win Rate:** Only **16.7% (~1 in 6)** of all studied LP positions achieved a positive net terminal PnL.
  - **Consistent Success Rate:** Only **14.3% (~1 in 7)** achieved both positive terminal PnL and a win-score $\omega > 0.5$.
  - **Behavioral Divergence:** Profitable positions were heavily clustered in taxonomy classes characterized by symmetric initial entry pricing ($P_{\mathrm{start}} \in [a, b]$) combined with early exit execution prior to boundary breach.
  - **Platform Activity Difference:** Aerodrome demonstrated significantly higher active liquidity management intensity and turnover compared to other Base DEX platforms.

### Independently reproduced

- Not independently reproduced.

### Negative evidence

- None identified in the reviewed sources; absence is not evidence of no negative result.
- Passive "set-and-forget" concentrated LP positions overwhelmingly produce negative alpha due to LVR and toxic flow extraction during volatility expansions.

## Falsification plan

1. **Passive Range Hold vs. Barrier Exit Ablation:** Compare the realized Sharpe and win-score $\omega$ of the barrier exit strategy against an identical entry position held until natural range expiration or fixed time $T$. If the barrier exit does not improve the proportion of profitable positions by at least 15 percentage points, the early barrier exit mechanism is falsified.
2. **Volatile Trending Market Stress Test:** Backtest the strategy during sustained multi-day directional trend regimes ($|\mu / \sigma| > 2.0$). If premature barrier exits generate excessive transaction fee drag that eliminates all net fee yield, the strategy lacks robustness to directional trend shocks.
3. **Cross-Chain Generalization:** Evaluate the rule on Ethereum Mainnet where gas costs are 50x–100x higher than Base. If high gas friction renders the early exit threshold economically unviable, the strategy is strictly confined to low-fee L2 environments.

## Crypto portability

- **Portability Classification:** `direct`.
- **Crypto Native Implementation:**
  - The mechanism is natively formulated on decentralized concentrated liquidity AMMs (Uniswap v3, Aerodrome, Camelot, Raydium CLMM).
  - Can be executed directly via smart contract bots or off-chain keeper networks on Base, Arbitrum, Optimism, and Solana.
- **Crypto Portability Risks:**
  - L2 sequencer downtime or transaction congestion during high-volatility crashes can prevent early barrier burns, exposing the position to full range-out loss.
  - MEV frontrunning and JIT (Just-In-Time) liquidity attacks can dilute fee share before high-volume swaps occur.

## Limitations

- **Gas-Sensitivity to Chain Choice:** Active barrier rebalancing is viable on low-cost L2s (Base, Arbitrum) and Solana, but prohibitive on Ethereum L1 for small to medium capital allocations.
- **Adverse Selection during News Shocks:** Sudden gap moves (e.g., protocol exploits or sudden macroeconomic announcements) can jump across the barrier in a single block before a burn transaction can be confirmed.
- **Fee Tier Crowding:** When multiple LPs adopt identical tight bands, fee distribution scales inversely with aggregate pool liquidity $L_{\mathrm{total}}$, compressing annualized yields.

## Implementation status

- Not implemented in our research stack.
- No PyBroker, NautilusTrader, paper, testnet, or live trading validation has been performed.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- This record represents theoretical and empirical research capture for quantitative intake review. It does not constitute authorization for deployment or capital allocation.

## Related Wiki records

- `[[quant/crypto-uniswap-v3-just-in-time-jit-liquidity-provision-price-impact-2026-09-01]]`
- `[[quant/defi-concentrated-liquidity-stochastic-impulse-control-tail-risk-2026-09-02]]`
- `[[quant/defi-amm-loss-versus-rebalancing-lvr-mechanics]]`

## Sources

- Andrey Urusov, Rostislav Berezovskiy, Anatoly Krestenko, and Andrei Kornilov, "Liquidity provision in CLMMs: evidence from transactions data", arXiv preprint `arXiv:2604.22069v1 [q-fin.TR, q-fin.CP]`, April 2026. DOI: [10.48550/arXiv.2604.22069](https://doi.org/10.48550/arXiv.2604.22069). Full text: [https://arxiv.org/abs/2604.22069](https://arxiv.org/abs/2604.22069).
