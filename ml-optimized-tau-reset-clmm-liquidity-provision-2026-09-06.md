---
schema: strategy-research-record-v1
title: "ML-Optimized τ-Reset Dynamic Liquidity Provision in Concentrated Liquidity AMMs"
created: 2026-09-06
updated: 2026-09-06
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - defi
  - uniswap-v3
  - concentrated-liquidity
  - liquidity-provision
  - machine-learning
  - ensemble
  - tau-reset
  - active-rebalancing
  - impermanent-loss
status: research-only
confidence: medium
source_as_of: 2026-03-30
sources:
  - "Urusov, A., Berezovskiy, R., Krestenko, A., Kornilov, A., and Yanovich, Y. (2025/2026). Dynamic Liquidity Provision in Decentralized Markets: Strategy Optimization and Performance Evaluation in Concentrated Liquidity AMMs. arXiv:2505.15338v2 [q-fin.MF]. https://arxiv.org/abs/2505.15338"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# ML-Optimized τ-Reset Dynamic Liquidity Provision in Concentrated Liquidity AMMs

## Provenance

- **Source:** arXiv:2505.15338v2, submitted 30 Mar 2026 (original v1 submitted 2025)
- **Authors:** Andrey Urusov (Vega Institute Foundation, Chuvash State University), Rostislav Berezovskiy (Vega Institute Foundation, HSE University), Anatoly Krestenko (Vega Institute Foundation, MIPT), Andrei Kornilov (Vega Institute Foundation), Yury Yanovich (Skolkovo Institute of Science and Technology)
- **Category:** q-fin.MF (Mathematical Finance)
- **Status:** Preprint (not peer-reviewed at time of capture)
- **Code:** Referenced as GitHub repository [27] in paper (Urusov, "Uniswap v3 LP dynamic strategies: source code, data and scripts"); exact URL not verified from primary source
- **Sample period:** In-sample: 1 April 2023 – 30 June 2024; Out-of-time (OOT): 1–30 September 2024
- **Universe:** Uniswap v3 pools on Ethereum mainnet: USDC/ETH 0.3%, USDC/ETH 0.05%, WBTC/ETH 0.3%, USDC/USDT 0.01%

## Economic mechanism

### Source-reported

The authors propose τ-reset strategies for dynamic liquidity reallocation in Concentrated Liquidity Market Makers (CLMMs) such as Uniswap v3. The mechanism partitions the price axis into buckets; when the pool price exits the LP's current liquid range (defined by parameter τ buckets on either side of a reference bucket), liquidity is reallocated. A machine learning ensemble (MLP + CatBoost + LSTM) predicts optimal capital allocation weights within the active ranges based on CEX market features (OHLCV-derived indicators from Binance). The authors claim consistent outperformance (13–23% higher fees) compared to uniform allocation benchmarks in a "predictive-advantage area" (PAA) corresponding to intermediate τ values (5–10).

### Research interpretation

The hypothesized alpha mechanism is that CEX price/volume/momentum signals (EMA, MACD, volume volatility) contain short-term information about which sub-ranges within the LP's active window will generate the most fee income, allowing asymmetric concentration of liquidity toward the side of the price range most likely to be traversed. This is a form of informed liquidity placement where the LP front-runs expected price movement within its active range, analogous to directional inventory management in traditional market making.

The strategy also introduces asymmetric τ+ηdown modifications that add empty protective buckets on the downside, reducing relocation frequency during sharp price declines and improving capital preservation. This is a risk-management overlay rather than an alpha signal per se.

## Signal

- **Formation timestamp:** Decision made at the start of each τ-reset epoch (when price exits the LP-liquid bucket range). Features are computed from the most recent 1-week window of 1-minute Binance OHLCV data for the target pair and BTC/USDT.
- **Lookback:** 7-day rolling window (10,080 minutes) of 1-minute OHLCV for feature computation.
- **Entry:** At each epoch boundary, the ML ensemble predicts optimal weight vector αLP ∈ R^{τ+1} (exploiting τ-symmetry) for allocation across the 2τ+1 LP-liquid buckets centered on the current reference bucket.
- **Exit:** Position is closed at the end of the OOT period (or when capital is depleted). No explicit stop-loss or take-profit; impermanent loss and downside risk are borne continuously.
- **Holding period:** Dynamic; epoch duration varies with market volatility. In-sample: average epoch ~15 hours (τ=5), ~45 hours (τ=10). OOT: similar.
- **Parameters:** τ ∈ {0, 1, 2, 5, 10, 20, 40, 100}; bucket width d = 10 USDC (for USDC-denominated pools); asymmetric variant adds ηdown empty downside buckets.
- **Position sizing:** Fixed initial capital W_LP = 1M USDC; no reinvestment of fees between epochs in the primary analysis. In the "As-Is" analysis with reinvestment, capital evolves.
- **Order type:** Liquidity provision (not directional trading); capital is split into token reserves per Uniswap v3 mechanics.
- **Underspecified:** Exact smart contract interaction timing, slippage during reallocation swaps, and MEV/JIT interaction are not modeled.

## Required data

- **Instrument:** Uniswap v3 LP positions (concentrated liquidity) on Ethereum mainnet
- **Venue:** Uniswap v3 (on-chain); CEX data from Binance for feature computation
- **Market type:** DeFi spot AMM (concentrated liquidity)
- **Timeframe:** 1-minute OHLCV bars from Binance; swap transaction data from Uniswap v3 subgraph
- **Fields:** OHLCV (close price, volume) for USDC/ETH and BTC/USDT on Binance; swap transaction data (prices, volumes, timestamps) from Uniswap v3 subgraph; pool TVL
- **Point-in-time:** Swap transactions are on-chain and available post-facto; CEX OHLCV is available with standard market data feeds
- **Timestamp:** UTC timestamps; 1-minute granularity for features
- **Missing-data:** Zero volumes replaced with 10^-8 constant; no explicit handling of missing swaps

## Execution assumptions

- **Gas costs:** 430,000 gas units per liquidity deployment; 215,000 gas units per burn; constant gas price of 20 Gwei. No gas cost if LP liquidity in a bucket remains unchanged after reallocation.
- **Fill model:** Assumes full execution of liquidity reallocation at the first price of the next epoch (minimum latency assumption of one block).
- **Token conversion costs:** Not modeled; the authors do not consider costs associated with token swaps necessary to convert into the desired asset for liquidity allocation.
- **Slippage/spread:** Not explicitly modeled for the LP reallocation trades. The authors note that in-pool prices are assumed to track market prices (efficient on-chain trading assumption).
- **MEV/JIT:** Not modeled. The authors explicitly acknowledge JIT liquidity and MEV (including sandwich attacks) as adverse factors but do not include them in the backtest.
- **Impermanent loss:** Modeled as part of the LP capital dynamics. The "natural" adverse factors (IL, downside price moves, gas) are included.
- **Leverage/margin:** Not applicable (LP capital is fully funded).
- **Impact/capacity:** The authors note that W_LP should be ≪ Σ (pool TVL) to avoid unrealistic results; they intentionally use a high W_LP to highlight modeling limitations.

## Evidence

### Source-reported

- **Liquidity approximation accuracy:** Parametric reconstruction achieves ~2% average approximation error for historical pool fees across all tested pools (Table 2: 1.3% for USDC/ETH 0.3% in-sample; 1.6% OOT).
- **ML vs uniform benchmark (USDC/ETH 0.3%, OOT Sep 2024):** τ=5: ML 104.5K vs uniform 90.5K USDC (+15.5%); τ=10: ML 59.2K vs uniform 50.0K USDC (+18.4%). (Table 1, Figure 17)
- **ML vs uniform benchmark (USDC/ETH 0.05%, OOT Sep 2024):** τ=5: ML 139.4K vs uniform 113.4K USDC (+23%); τ=10: ML 78.0K vs uniform 65.2K USDC (+20%). (Table 2)
- **ML vs uniform benchmark (WBTC/ETH 0.3%, OOT Sep 2024):** τ=5: ML 79.5K vs uniform 64.6K USDC (+23%); τ=10: ML 42.1K vs uniform 37.1K USDC (+13%). (Table 2)
- **Asymmetric strategy (USDC/ETH 0.05%, τ=5, ηdown=20, OOT Sep 2024):** Compound annual return 88.9% vs B&H 51.9%; MDD -11.8% vs -16.2%; Sharpe 1.7 vs 0.9. (Table 4)
- **Comparison with Fractal backtesting library:** <4% difference in cumulative fees (28,562 vs 29,674 USDC over ~1 month).
- **Source-reported performance figures are from Table 1, Table 2, Table 3, Table 4, and Figure 17 of the paper. All figures are source-reported and have not been independently reproduced.**

### Independently reproduced

Not independently reproduced.

### Negative evidence

- τ=0 and τ=1 strategies underperform uniform benchmark due to heightened impermanent loss and more frequent realization of market risk from excessive concentration. (Section 5.4, Figure 17)
- "As-Is" τ-reset strategies with frequent reallocations can rapidly deplete LP capital: τ=5 without asymmetric modification shows -92.0% compound annual return due to relocation costs and IL. (Table 3)
- The authors acknowledge that the modeling framework does not account for MEV, JIT liquidity, or competition among LPs, which would reduce realized performance.
- The reward ceiling under Approach 3 (LP fees as share of historical pool liquidity) caps attainable fees at the historical pool reward level.
- No identification of negative evidence in the reviewed sources beyond the authors' own limitations discussion; absence is not evidence of no negative result.

## Falsification plan

1. **Out-of-sample robustness:** Test the ML ensemble on multiple non-overlapping OOT periods across different market regimes (bull, bear, high-vol, low-vol). The current OOT is a single month (Sep 2024).
2. **Parameter perturbation:** Vary τ, d (bucket width), and ηdown across a grid; verify that the PAA (τ=5-10) is stable or identify regimes where it collapses.
3. **Transaction cost stress:** Include realistic gas price volatility (not fixed 20 Gwei), token conversion swap costs, and slippage during reallocation. Test sensitivity to gas price ±3x.
4. **MEV/JIT inclusion:** Model the impact of JIT liquidity and sandwich attacks on realized LP fees. Expected direction: negative impact on ML strategy performance.
5. **Capacity/LP competition:** Scale W_LP relative to pool TVL and model the effect of multiple LPs using similar ML strategies (game-theoretic interaction).
6. **Alternative universe:** Test on pools with different characteristics (lower liquidity, different asset pairs, L2 deployments).
7. **Baseline comparison:** Compare against buy-and-hold of the underlying assets, static concentrated liquidity, and simple rule-based rebalancing (e.g., fixed-period rebalance) as additional baselines.
8. **Failure metric:** If ML ensemble fails to outperform uniform benchmark in >50% of OOT months across multiple pools, the PAA hypothesis is materially weakened.

## Crypto portability

**direct**

The strategy is natively designed for Uniswap v3 on Ethereum mainnet. The mechanism (concentrated liquidity AMM, τ-reset reallocation) is specific to CLMMs and directly applicable to Uniswap v3 and similar protocols (e.g., QuickSwap, PancakeSwap v3, Camelot).

**Portability considerations:**
- The ML features are derived from Binance CEX data; cross-venue feature relevance may vary for pools on L2s or non-EVM chains.
- Gas costs are Ethereum-specific; L2 deployments would have materially different cost structures.
- The framework assumes on-chain swap data availability via subgraphs; this is protocol-specific.
- Pool TVL and swap volume vary significantly across venues; the PAA may shift.

## Limitations

- **Single OOT period:** All OOT results are from September 2024 only; no multi-regime validation.
- **No MEV/JIT modeling:** Real-world LP performance is likely lower due to JIT liquidity extraction and sandwich attacks.
- **No token conversion costs:** The framework ignores swap costs for rebalancing into the desired token composition.
- **Fixed gas price assumption:** 20 Gwei is unrealistic during periods of high Ethereum congestion.
- **High W_LP relative to TVL:** The authors intentionally use W_LP = 1M USDC against TVL of 40-140M to highlight modeling limitations; this inflates LP share and may overstate fee capture.
- **No competition modeling:** Single-LP analysis ignores strategic interactions among LPs.
- **Feature engineering is minimal:** Only 15 features per pair (EMA, MACD, volume volatility); more sophisticated features might improve or degrade results.
- **Ensemble weights are static:** Trained once on in-sample data; no adaptive retraining.
- **Not independently reproduced**
- **Preprint (not peer-reviewed)**
- **data gap:** Exact GitHub repository URL referenced as [27] not verified from primary source

## Implementation status

Not implemented in our research stack. No NautilusTrader, PyBroker, paper, testnet, or live implementation.

## Adoption boundary

This record is research material only. Presence in this repository does not mean:
- Profitable
- Validated alpha
- Approved for implementation
- Approved for paper trading
- Approved for testnet
- Approved for live trading

## Related Wiki records

- [[quant/defi-ppo-active-liquidity-uniswap-v3-concentrated-range-2026-09-06]] — Related Uniswap v3 active liquidity provision study using PPO (different mechanism: RL vs ML ensemble; different signal: policy gradient vs τ-reset with feature-based prediction)
- [[quant/defi-concentrated-amm-rammstein-stein-threshold-rebalancing-2026-09-02]] — Related concentrated AMM rebalancing strategy
- [[quant/defi-concentrated-liquidity-stochastic-impulse-control-tail-risk-2026-09-02]] — Related concentrated liquidity risk management

## Sources

1. Urusov, A., Berezovskiy, R., Krestenko, A., Kornilov, A., and Yanovich, Y. (2025/2026). Dynamic Liquidity Provision in Decentralized Markets: Strategy Optimization and Performance Evaluation in Concentrated Liquidity AMMs. arXiv:2505.15338v2 [q-fin.MF]. https://arxiv.org/abs/2505.15338
