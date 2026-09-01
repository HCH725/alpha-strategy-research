---
schema: strategy-research-record-v1
title: "Dynamic Grid Trading Strategy with Adaptive Boundary Resets in Cryptocurrency Markets"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - grid-trading
  - mean-reversion
  - volatility-harvesting
  - adaptive-reset
  - market-making
  - zero-expectation
status: research-only
confidence: medium
source_as_of: 2025-06-13
sources:
  - "Kai-Yuan Chen, Kai-Hsin Chen, Jyh-Shing Roger Jang, 'Dynamic Grid Trading Strategy: From Zero Expectation to Market Outperformance', arXiv:2506.11921v1 [q-fin.TR], June 2025. https://arxiv.org/abs/2506.11921"
  - "colachenkc/Dynamic-Grid-Trading GitHub repository (commit reference / code release): https://github.com/colachenkc/Dynamic-Grid-Trading"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Dynamic Grid Trading Strategy with Adaptive Boundary Resets in Cryptocurrency Markets

## Provenance

- **Paper URL:** https://arxiv.org/abs/2506.11921
- **Full arXiv ID:** 2506.11921v1 [q-fin.TR]
- **Authors:** Kai-Yuan Chen, Kai-Hsin Chen, Jyh-Shing Roger Jang (National Taiwan University)
- **Published:** 2025-06-13
- **Primary Category:** Quantitative Finance - Trading and Market Microstructure (q-fin.TR)
- **Code Repository:** https://github.com/colachenkc/Dynamic-Grid-Trading
- **Data Source:** Minute-level historical candlestick data for BTC/USDT and ETH/USDT (January 2021 to July 2024)

## Economic mechanism

### Source-reported

The authors provide a formal mathematical proof that traditional static geometric grid trading is a "zero-expectation" system under standard martingale/random walk market dynamics. While traditional grid trading captures incremental arbitrage cash flows from price oscillations within a predefined price band $[P_{min}, P_{max}]$, it suffers from terminal boundary failure: when the price breaks above the upper boundary $P_{max}$, the trader holds pure cash and misses all continuing upside; when the price breaks below the lower boundary $P_{min}$, the trader holds 100% depreciated inventory and suffers severe unrealized capital losses that mathematically cancel out accumulated historical grid profits.

To eliminate the zero-expectation trap, the authors propose the **Dynamic Grid-based Trading (DGT)** strategy. DGT introduces an asymmetric boundary reset mechanism:
1. **Upward Boundary Breach ($P_t > P_{upper}$):** The strategy liquidates remaining inventory at market peak, locks in accumulated grid arbitrage profits, resets the grid center to the current price, and reinvests the expanded capital base into a new grid.
2. **Downward Boundary Breach ($P_t < P_{lower}$):** The strategy refuses to realize capital losses on the accumulated base inventory. Instead, it holds the underlying spot crypto and deploys *only* the accumulated cash arbitrage profits earned during the preceding grid lifecycle as working principal to establish a new, lower-tier grid centered at the depressed market price.

### Research interpretation

The underlying economic thesis is **volatility extraction with non-linear downside risk segmentation**:
- In high-volatility cryptocurrency markets, asset prices oscillate with fat-tailed distributions and prolonged trending phases.
- Static grid trading behaves like shorting a straddle/strangle: it collects steady premium (grid spread) during range-bound regimes but incurs unbounded losses in strong directional moves.
- DGT converts the short volatility profile into an asymmetric payout structure:
  - On the upside, it acts like a trailing dynamic accumulator that compounds gains and resets reference levels.
  - On the downside, by isolating accumulated grid cash earnings as a risk-budget cushion for secondary grid deployment, it avoids forced margin liquidation or fire-sale realization of base inventory while continuing to harvest local micro-volatility at lower price levels.

**Component roles:**
- **Primary Grid Engine:** Geometric grid structure placing limit buy/sell orders at logarithmic intervals to capture local mean-reverting microstructure noise.
- **Upward Dynamic Reset:** Trailing re-centering trigger that converts unhedged inventory into cash and compounds total portfolio equity.
- **Downward Asymmetric Isolation Filter:** Capital segmentation rule that locks initial base spot exposure and funds secondary lower-grid market making exclusively from earned arbitrage alpha.

## Signal

- **Formation timestamp:** Evaluated at 1-minute candlestick close (or real-time tick updates upon grid boundary crossings).
- **Lookback / Initialization:**
  - Initial upper boundary: $P_{upper} = P_0 \times (1 + \delta_{upper})$
  - Initial lower boundary: $P_{lower} = P_0 \times (1 - \delta_{lower})$
  - Number of grid intervals: $N$
  - Grid interval spacing: $\Delta p = \ln(P_{upper} / P_{lower}) / N$ (geometric grid)
- **Order Placement Logic:**
  - Place $N/2$ limit buy orders below current price at $P_i = P_{center} \cdot e^{-i \cdot \Delta p}$
  - Place $N/2$ limit sell orders above current price at $P_j = P_{center} \cdot e^{j \cdot \Delta p}$
  - When buy order at $P_i$ fills, immediately post limit sell order at $P_i \cdot e^{\Delta p}$
  - When sell order at $P_j$ fills, immediately post limit buy order at $P_j \cdot e^{-\Delta p}$
- **Dynamic Boundary Reset Trigger:**
  - **Upper Breach ($P_t \ge P_{upper}$):**
    - Execute market sell on remaining base asset inventory.
    - Calculate total realized portfolio equity $E_t = \text{Cash}_t$.
    - Set new initial price $P_0' = P_t$, recompute $[P_{lower}', P_{upper}']$, redeploy full capital $E_t$.
  - **Lower Breach ($P_t \le P_{lower}$):**
    - Retain all filled base asset inventory (do not sell at a loss).
    - Extract accumulated realized grid arbitrage profit $\Pi_{grid} = \sum (\text{Sell Price} - \text{Buy Price}) \times \text{Size} - \text{Fees}$.
    - If $\Pi_{grid} > \text{MinCapital}$, deploy $\Pi_{grid}$ as the dedicated capital for a secondary subordinate grid centered at $P_t$.
    - If price rebounds above the original lower boundary $P_{lower}$, consolidate secondary grid profits into primary ledger.
- **Parameters:**
  - Grid boundary width $\delta \in [0.05, 0.25]$ (5% to 25% price range)
  - Grid count $N \in [10, 100]$
  - Rebalance interval: 1 minute (evaluation frequency)
  - Trading fee tier: Maker 0.02% / Taker 0.05% (modeled in simulation)

## Required data

- **Instrument:** Spot cryptocurrency pairs (BTC/USDT, ETH/USDT) or linear perpetual contracts (collateralized in USDT).
- **Universe:** High-liquidity cryptocurrency assets with continuous two-way order books.
- **Venue:** Centralized spot/perp exchanges (e.g., Binance, OKX, Bybit, Coinbase).
- **Timeframe:** 1-minute OHLCV bars or real-time L2 order book feeds / tick-by-tick trades.
- **Fields:** Open, High, Low, Close, Volume, Timestamp, Maker fee schedule, Taker fee schedule.
- **Point-in-time:** Real-time stream without look-ahead; boundary checks triggered strictly on current bar close or tick breach.
- **Missing-data handling:** If exchange websocket disconnects or data drops, existing resting limit orders remain on exchange order book; state synchronization is performed via REST order query upon reconnection.

## Execution assumptions

- **Order Types:**
  - Grid level orders: Passive limit orders (Maker).
  - Upper boundary reset liquidations: Immediate market or aggressive marketable limit orders (Taker).
- **Fill Model:** Limit orders are filled when market price touches or crosses the grid price level; assumes sufficient book depth at touch for standard retail sizing.
- **Transaction Costs:**
  - Maker fee: 0.00% to 0.02% (depending on exchange VIP tier).
  - Taker fee: 0.04% to 0.05%.
  - Slippage: Modeled at 0.01% on boundary market resets.
- **Margin / Leverage:** Spot basis (1x leverage, no liquidation risk) or low-leverage perpetuals (<= 2x).

## Evidence

### Source-reported

- Evaluated across **1-minute candlestick data** for Bitcoin (BTC) and Ethereum (ETH) from **January 2021 to July 2024** (encompassing bull, bear, and range-bound macro market regimes).
- Backtest findings reported in the paper:
  - The Dynamic Grid Trading (DGT) strategy consistently outperformed both the traditional static grid trading strategy and the benchmark buy-and-hold (B&H) strategy across the multi-year evaluation window.
  - In terms of **Internal Rate of Return (IRR)**, DGT achieved superior risk-adjusted capital efficiency by continuously compounding upward breakout capital while insulating downside drawdown through profit-isolated sub-grids.
  - DGT significantly reduced **Maximum Drawdown (MDD)** compared to buy-and-hold during severe market drawdowns (e.g., 2022 crypto bear market), as the strategy held cash buffers and deployed fractional profit capital during lower regimes.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Sustained Non-Volatile Bear Trending (Slow Bleed):** In a prolonged monotonic downward trend with negligible intraday price oscillation, accumulated grid profits $\Pi_{grid}$ may be insufficient to fund meaningful secondary grids, leaving the primary base asset inventory sitting with large unrealized drawdowns.
- **Fee Friction / Tight Grids:** If grid spacing $\Delta p$ is set too narrow relative to exchange taker/maker fee hurdles, churn fees erode total arbitrage profits, causing the secondary downside risk budget to fail to materialize.
- **Flash Crashes and Liquidity Gaps:** During extreme market disconnections or gap-down openings, limit buy orders can fill instantaneously across all levels without opportunity for intermediate sell bounces, concentrating inventory at adverse prices.

## Falsification plan

1. **Ablation Test on Reset Mechanism:** Compare DGT against a static grid and a simple trailing-stop grid over identical market data. **Failure rule:** If DGT does not achieve a statistically significant higher Sortino ratio and lower maximum drawdown than the static grid across out-of-sample data, the adaptive reset mechanism hypothesis is falsified.
2. **High-Fee Stress Test:** Scale maker fees from 0.02% to 0.08% and taker fees from 0.05% to 0.15%. **Failure rule:** If the strategy's net IRR turns negative while the underlying asset price exhibits normal volatility, the alpha is purely fee-rebate dependent.
3. **Synthetic Geometric Brownian Motion (GBM) vs. Jump Diffusion:** Test on pure GBM simulations (zero autocorrelation, no mean reversion) vs. empirical crypto price series. **Failure rule:** If DGT produces zero excess return over buy-and-hold on empirical data, the volatility-harvesting premise fails.
4. **Out-of-Sample Altcoin Test:** Run DGT on non-BTC/ETH high-beta altcoins (e.g., SOL, AVAX, DOGE) over 2024-2026 out-of-sample periods. **Failure rule:** If altcoin down-trends permanently impair the accumulated inventory without profit recovery, the capital preservation rule is rejected.

## Crypto portability

**direct**

The strategy was developed, modeled, and backtested natively on cryptocurrency spot/perpetual market data (BTC/USDT and ETH/USDT).
- **24/7 Continuous Trading:** Crypto markets operate without opening/closing gaps, making dynamic continuous grid monitoring more effective than in traditional equities with overnight gap risk.
- **High Intraday Volatility:** The structural retail participation and high volatility in crypto provide abundant order-crossing opportunities for passive grid liquidity harvesting.
- **Perpetual Funding Considerations:** If implemented on USDT-margined perpetuals rather than spot, funding rates must be factored into the holding cost of accumulated lower-grid inventory.

## Limitations

- **Capital Lock-in on Severe Downtrends:** While DGT avoids realizing losses on downward boundary breaches, the primary spot capital remains locked in base assets until price recovery, resulting in substantial opportunity cost during multi-year bear cycles.
- **Parameter Sensitivity:** Optimal grid count $N$ and boundary width $\delta$ depend heavily on realized market volatility; fixed parameter configurations may underperform during volatility regime shifts.
- **Exchange Latency & API Rate Limits:** Maintaining dozens of resting limit orders and rapidly resetting them during boundary breakouts requires robust websocket infrastructure and may hit exchange API rate limits during high-volatility spikes.

## Implementation status

No implementation in our research stack. The paper provides theoretical proofs and open-source Python backtesting scripts; no NautilusTrader or PyBroker execution module has been constructed.

## Adoption boundary

This record is research material only. Presence in this repository does not mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

## Related Wiki records

- [[quant/crypto-short-horizon-15min-mean-reversion-taker-flow-2026-09-01]] — Related short-horizon intraday mean-reversion microstructure dynamics
- [[quant/crypto-liquidity-provision-reversal-premium-cross-market-2026-09-01]] — Passive liquidity provision and reversal capture mechanisms
- [[quant/rsi-mean-reversion_ohlcv-2026-08-31]] — Baseline mean-reversion comparison

## Sources

1. Kai-Yuan Chen, Kai-Hsin Chen, Jyh-Shing Roger Jang, "Dynamic Grid Trading Strategy: From Zero Expectation to Market Outperformance", arXiv:2506.11921v1 [q-fin.TR], June 2025. https://arxiv.org/abs/2506.11921
2. Open-source implementation repository: `colachenkc/Dynamic-Grid-Trading` on GitHub. https://github.com/colachenkc/Dynamic-Grid-Trading
