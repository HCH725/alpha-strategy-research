---
schema: strategy-research-record-v1
title: "CEX-DEX Cross-Venue Arbitrage under Non-Instantaneous Settlement: Risk-Adjusted Threshold Execution and Subslot Latency Compression"
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - arbitrage
  - cex-dex
  - mev
  - execution-risk
  - market-microstructure
  - subslots
  - latency
  - uniswap-v3
  - binance
status: research-only
confidence: high
source_as_of: 2026-01
sources:
  - "Aleksei Adadurov, Sergey Barseghyan, Anton Chtepine, Antero Eloranta, Andrei Sebyakin, Arsenii Valitov, 'Second Thoughts: How 1-second subslots transform CEX-DEX Arbitrage on Ethereum', arXiv:2601.00738v1 [q-fin.TR], January 2026. https://arxiv.org/abs/2601.00738"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# CEX-DEX Cross-Venue Arbitrage under Non-Instantaneous Settlement: Risk-Adjusted Threshold Execution and Subslot Latency Compression

## Provenance

- **Primary Source:** Aleksei Adadurov, Sergey Barseghyan, Anton Chtepine, Antero Eloranta, Andrei Sebyakin, and Arsenii Valitov, "Second Thoughts: How 1-second subslots transform CEX-DEX Arbitrage on Ethereum", *arXiv preprint arXiv:2601.00738v1 [q-fin.TR]*, January 2026. URL: [https://arxiv.org/abs/2601.00738](https://arxiv.org/abs/2601.00738).
- **Related Foundational Literature:**
  - P. Daian et al. (2020), "Flash Boys 2.0: Frontrunning, Transaction Reordering, and Consensus Instability in Decentralized Exchanges", *IEEE S&P 2020*.
  - L. Fritsch et al. (2022), "Cross-Exchange Arbitrage in the Decentralized Web", *IEEE Access*.
  - C. F. Robinson et al. (2024), "Preconfirmations in Based Rollups: Structural Latency and Arbitrageur Exposure".
- **Context:** In classic centralized-decentralized exchange (CEX-DEX) arbitrage, an agent seeks to extract price discrepancies between a continuous central limit order book (e.g., Binance) and a discrete automated market maker (e.g., Uniswap v3). While the CEX leg is executed via ultra-low-latency API order routing with immediate acknowledgement, the DEX leg requires submitting an on-chain transaction that experiences stochastic block inclusion latency ($\Delta t \approx 12\text{s}$ on Ethereum L1). Adadurov et al. (2026) model the optimal threshold policy under this asymmetric execution risk and quantify the structural transformation caused by 1-second subslots.

## Economic mechanism

### Source-reported

1. **Asymmetric Leg Execution Risk:** A cross-venue arbitrageur faces fundamental structural asymmetry:
   - The CEX leg offers sub-millisecond execution and deterministic fill confirmation.
   - The DEX leg is subject to discrete slot latency, priority gas auctions (PGA / MEV-Boost builders), and toxic price movement during the pending inclusion interval $\tau \in [0, \Delta t]$.
2. **Optimal Reservation Discrepancy Threshold:** Because failed or front-run DEX transactions result in either reverted gas losses or unhedged directional inventory exposure on the CEX leg, a risk-averse arbitrageur requires a minimum reservation threshold $\Delta P^*(t)$ strictly greater than direct fees ($c_{\text{fees}} + c_{\text{gas}}$):
   $$\Delta P^*(t) = c_{\text{fees}} + c_{\text{gas}} + \gamma \cdot \operatorname{Var}\left[\Delta S_{\tau} \mid \text{pending}\right] + \text{Premium}(\text{reversion risk})$$
   where $\gamma$ is the trader's risk aversion coefficient and $\operatorname{Var}[\Delta S_\tau] \propto \sigma^2 \tau$ represents the variance of price drift over the block interval $\tau$.
3. **Subslot Latency Risk Compression:** Reducing the block inclusion interval from the 12-second slot time to 1-second subslots (or L2 preconfirmations) compresses the adverse selection variance by an order of magnitude ($\tau \to \tau / 12$), sharply reducing the required hurdle premium $\Delta P^*(t)$ and unlocking latent low-margin arbitrage opportunities.

### Research interpretation

The falsifiable thesis is a **variance-penalized CEX-DEX cross-venue latency arbitrage mechanism**:
1. **Dynamic Volatility-Adjusted Threshold Policy:** Rather than executing when $|P_{\text{DEX}} - P_{\text{CEX}}| > c_{\text{fixed}}$, the optimal entry threshold must be dynamically adjusted for instantaneous high-frequency volatility $\sigma_{\text{HF}}$ and expected inclusion latency $\mathbb{E}[\tau]$:
   $$\theta_t = \left(f_{\text{CEX}} + f_{\text{DEX}}\right) + \frac{C_{\text{gas}}}{Q \cdot P_t} + k \cdot \sigma_{\text{HF}, t} \sqrt{\mathbb{E}[\tau]}$$
   where $k$ parameterizes the empirical risk-aversion haircut.
2. **Venue Routing & Subslot Benefit:** In sub-second subslot environments (or fast rollup preconfirmation systems), the threshold $\theta_t$ collapses towards zero, allowing high-frequency statistical arbitrage engines to execute high-turnover, low-margin trades across concentrated liquidity pools.

## Signal

### Mathematical Formulation of Entry & Execution Rule

1. **Price Observation:**
   - $P_{\text{CEX}, t}$: Mid-price on Binance spot/perpetual book at timestamp $t$.
   - $P_{\text{DEX}, t}$: Effective marginal execution price for trade size $Q$ on Uniswap v3 pool.
   - $\sigma_t$: Realized 1-minute high-frequency return volatility on CEX.

2. **Hurdle Spread Calculation:**
   $$\text{Spread}_t = \frac{P_{\text{DEX}, t} - P_{\text{CEX}, t}}{P_{\text{CEX}, t}}$$
   $$\theta_t = \left(\text{fee}_{\text{CEX}} + \text{fee}_{\text{DEX}}\right) + \frac{\text{GasCost}_{\text{USD}}}{Q \cdot P_{\text{CEX}, t}} + \alpha \cdot \sigma_t \sqrt{\tau_{\text{block}}}$$
   where $\alpha \ge 1.96$ represents a 95% confidence variance buffer for pending block inclusion drift $\tau_{\text{block}}$.

3. **Trade Direction & Sizing:**
   - **Case A (DEX Rich):** $\text{Spread}_t > +\theta_t$:
     - Submit private DEX swap: Sell base asset on Uniswap v3 for quote asset.
     - Simultaneously (or conditionally upon builder receipt) execute CEX buy: Buy $Q$ base asset on Binance.
   - **Case B (CEX Rich):** $\text{Spread}_t < -\theta_t$:
     - Submit private DEX swap: Buy base asset on Uniswap v3 with quote asset.
     - Simultaneously execute CEX short/sell: Sell $Q$ base asset on Binance.
   - **Optimal Size $Q^*$:** Determined by matching marginal AMM price impact to marginal CEX book depth up to tick slippage tolerance:
     $$Q^* = \arg\max_Q \left[ Q \cdot \left(|\Delta P(Q)| - \theta_t(Q)\right) \right]$$

### Algorithmic Implementation Architecture

```python
import math
import dataclasses
from typing import Optional, Literal

@dataclasses.dataclass
class CexDexArbitrageSignal:
    timestamp_ns: int
    direction: Literal["BUY_CEX_SELL_DEX", "BUY_DEX_SELL_CEX", "NO_TRADE"]
    cex_price: float
    dex_effective_price: float
    raw_spread_bps: float
    hurdle_threshold_bps: float
    net_expected_edge_bps: float
    optimal_size_base: float

def compute_cex_dex_arbitrage_opportunity(
    cex_mid_price: float,
    dex_pool_sqrt_price: float,
    dex_liquidity_l: float,
    dex_fee_tier_bps: float,
    cex_taker_fee_bps: float,
    gas_cost_usd: float,
    hf_volatility_per_sec: float,
    block_latency_sec: float,
    risk_haircut_k: float = 2.0
) -> CexDexArbitrageSignal:
    """
    Computes risk-adjusted CEX-DEX arbitrage signal under Adadurov et al. (2026) framework.
    """
    # Marginal DEX price from sqrt price
    dex_price = dex_pool_sqrt_price ** 2
    raw_spread = (dex_price - cex_mid_price) / cex_mid_price
    raw_spread_bps = raw_spread * 10000.0

    # Risk-adjusted hurdle threshold
    base_fees_bps = dex_fee_tier_bps + cex_taker_fee_bps
    variance_risk_bps = (risk_haircut_k * hf_volatility_per_sec * math.sqrt(block_latency_sec)) * 10000.0
    
    # Baseline test notional size ($50,000 USD equivalent)
    test_notional_usd = 50000.0
    gas_drag_bps = (gas_cost_usd / test_notional_usd) * 10000.0
    
    hurdle_threshold_bps = base_fees_bps + gas_drag_bps + variance_risk_bps

    if raw_spread_bps > hurdle_threshold_bps:
        # DEX price is higher than CEX: Sell on DEX, Buy on CEX
        direction: Literal["BUY_CEX_SELL_DEX", "BUY_DEX_SELL_CEX", "NO_TRADE"] = "BUY_CEX_SELL_DEX"
        net_edge = raw_spread_bps - hurdle_threshold_bps
        opt_size = test_notional_usd / cex_mid_price
    elif raw_spread_bps < -hurdle_threshold_bps:
        # CEX price is higher than DEX: Buy on DEX, Sell on CEX
        direction = "BUY_DEX_SELL_CEX"
        net_edge = abs(raw_spread_bps) - hurdle_threshold_bps
        opt_size = test_notional_usd / cex_mid_price
    else:
        direction = "NO_TRADE"
        net_edge = 0.0
        opt_size = 0.0

    return CexDexArbitrageSignal(
        timestamp_ns=0,
        direction=direction,
        cex_price=cex_mid_price,
        dex_effective_price=dex_price,
        raw_spread_bps=raw_spread_bps,
        hurdle_threshold_bps=hurdle_threshold_bps,
        net_expected_edge_bps=net_edge,
        optimal_size_base=opt_size
    )
```

## Required data

- **CEX Real-Time L2/L3 Order Book:** Binance ETH/USDT and BTC/USDT WebSocket depth streams (depth20/diff-depth) with microsecond server timestamps.
- **DEX State & Mempool Logs:** Full Uniswap v3 tick arrays, `slot0` state updates, and pending mempool transactions / builder block pre-allocations via local RPC node (Reth/Geth).
- **Historical Calibration Sample:** Tick-by-tick Binance and Uniswap v3 data (matching the July–September 2025 benchmark dataset evaluated in the study).
- **Latency & Gas Feeds:** Ethereum L1 base fee (`baseFeePerGas`), priority fee tip distributions, and L2 subslot / preconfirmation commitment receipts.

## Execution assumptions

- **Dual-Leg Order Routing:**
  - DEX leg routed through private builder bundles (Flashbots / Titan / BeaverBuild) to eliminate public mempool frontrunning.
  - CEX leg routed via low-latency FIX/WebSocket API with Post-Only or IOC market orders.
- **Fail-Safe Inventory Model:** If the DEX bundle fails to land on-chain during the target block, the CEX hedging order must either trigger immediate stop-out or settle into a statistical inventory management buffer.
- **Capital Allocation:** Equal collateral reserves maintained in CEX spot margin/perpetual sub-accounts and on-chain smart contract vaults.

## Evidence

### Source-reported

- Adadurov, Barseghyan, Chtepine, Eloranta, Sebyakin, and Valitov (arXiv:2601.00738v1, January 2026) report from simulations calibrated to empirical Binance and Uniswap v3 data (July–September 2025):
  1. **Transaction Count Expansion:** Transitioning from the standard 12-second Ethereum slot time to a 1-second subslot regime produces an average **$+535\%$ increase in arbitrage transaction count**.
  2. **Volume Growth:** Arbitrage trading volume increases by **$+203\%$ on average** across the analyzed trading pairs.
  3. **Variance Compression:** The mechanism is driven by a profound compression in the variance of both successful and failed trade outcomes, directly raising the risk-adjusted Sharpe ratio for risk-averse arbitrageurs and rendering lower-fee liquidity tiers profitable.

### Independently reproduced

- `not independently reproduced`.

### Negative evidence

- **Toxic Settlement & Priority Fee Wars:** In high-congestion regimes, competitive builder bidding and priority gas spikes erode up to **$80\%$** of gross arbitrage profits, transferring value to block proposers and validators (MEV extraction).
- **Desynchronization Loss:** Sudden disconnections or API rate limits on the CEX side while an on-chain transaction is mined can generate unbounded unhedged directional losses during high-volatility flash crashes.

## Falsification plan

1. **Empirical Simulation:** Calibrate the dynamic hurdle threshold $\theta_t$ against historical 1-second Binance tick data and Uniswap v3 swap blocks across different latency intervals ($\Delta t \in \{1\text{s}, 2\text{s}, 6\text{s}, 12\text{s}\}$).
2. **Ablation Test:** Compare static fee thresholds against volatility-adjusted variance-penalized thresholds $\theta_t(\sigma_t, \tau)$.
3. **Falsification Thresholds:**
   - If the variance-adjusted threshold fails to achieve a higher Sharpe ratio than a naive fixed-fee threshold over a 3-month walk-forward test, reject the risk-adjusted hurdle hypothesis.
   - If subslot execution frequency fails to increase by at least **$+100\%$** when simulated latency drops from 12s to 1s under historical volatility, reject the latency sensitivity model.

## Crypto portability

- **Portability:** `direct`.
- **Domain Focus:** Directly investigates cross-venue cryptocurrency market microstructure between centralized exchanges (Binance) and decentralized AMMs (Uniswap v3) across Ethereum L1 and subsecond Layer-2/subslot architectures.

## Limitations

- `not independently reproduced`;
- **Builder Inclusion Probabilities:** Simulation models assume deterministic subslot inclusion upon bid submission, whereas actual MEV auctions introduce competitive bundle exclusion risks;
- **CEX Fee Tiers:** Empirical results depend heavily on VIP fee tier schedules on centralized exchanges.

## Implementation status

- `not-implemented`. Research capture only; no live arbitrage bots or execution engines implemented.

## Adoption boundary

- `research-only`, `not-approved`.
- This record captures academic research on CEX-DEX market microstructure and subslot dynamics. It does not authorize capital deployment or live trading.

## Related Wiki records

- `[[quant/crypto-priority-gas-auctions-pga-dex-latency-arbitrage-2026-09-01]]`
- `[[quant/hyperliquid-sunshine-trading-adverse-selection-liquidity-extraction-2026-09-01]]`
- `[[quant/defi-cfmm-intrinsic-liquidity-carr-madan-delta-hedge-2026-09-01]]`
- `[[quant/dex-cyclic-arbitrage-constant-product-amm-2026-09-01]]`

## Sources

1. Aleksei Adadurov, Sergey Barseghyan, Anton Chtepine, Antero Eloranta, Andrei Sebyakin, Arsenii Valitov, "Second Thoughts: How 1-second subslots transform CEX-DEX Arbitrage on Ethereum", *arXiv preprint arXiv:2601.00738v1 [q-fin.TR]*, January 2026. DOI: [10.48550/arXiv.2601.00738](https://doi.org/10.48550/arXiv.2601.00738). URL: [https://arxiv.org/abs/2601.00738](https://arxiv.org/abs/2601.00738).
