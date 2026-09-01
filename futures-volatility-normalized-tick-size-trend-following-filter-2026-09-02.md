---
schema: strategy-research-record-v1
title: "Volatility-Normalized Tick Size Conditioning for Trend-Following Feedback Resilience"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - trend-following
  - market-microstructure
  - tick-size
  - market-impact
  - futures
  - high-frequency-trading
status: research-only
confidence: medium
source_as_of: 2026-07-02
sources:
  - "Jutta G. Kurth, Zoltan Eisler, Adam Rej, and Jean-Philippe Bouchaud, 'Is Trend Still Your Friend?: A Microstructural Account of the Demise of Short-Term Trend-Following', arXiv:2607.01550v1 [q-fin.TR], July 2026. https://arxiv.org/abs/2607.01550"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Volatility-Normalized Tick Size Conditioning for Trend-Following Feedback Resilience

## Provenance

- **Primary Source:** Jutta G. Kurth, Zoltan Eisler, Adam Rej, and Jean-Philippe Bouchaud (Capital Fund Management / CFM), *"Is Trend Still Your Friend?: A Microstructural Account of the Demise of Short-Term Trend-Following"*, arXiv preprint `arXiv:2607.01550v1 [q-fin.TR]`, published July 2026. URL: https://arxiv.org/abs/2607.01550.
- **Primary Category:** Trading and Market Microstructure (`q-fin.TR`).
- **Empirical Dataset:** Comprehensive multi-asset universe of ~100 liquid exchange-traded futures contracts spanning Commodities, Equities Indices, Fixed Income, and Foreign Exchange (FX) across global exchanges from 1995 to 2025.

## Economic mechanism

### Source-reported

Short-term trend-following strategies (e.g., lookback windows of 1 to 20 days) historically generated substantial risk-adjusted returns across asset classes, but suffered a sharp, persistent structural decline in profitability following the 2008–2009 Global Financial Crisis, whereas longer-horizon trend-following (50 to 200 days) remained robust.

The authors evaluate four common explanations for this phenomenon:
1. **CTA Capacity Constraints:** Dismissed; aggregate CTA assets under management stabilized, yet performance decay was concentrated specifically in short horizons.
2. **General Market Electronification:** Dismissed; electronic matching was already prevalent across major venues prior to 2008.
3. **CTA Order Flow Interaction Shifts:** Dismissed; cross-sectional CTA position correlation did not explain contract-level divergence.
4. **Microstructural Liquidity Constraints & HFT Intermediation:** Supported as the primary explanatory driver.

The paper models trend-following as a **self-fulfilling market impact feedback loop**:
$$\text{Trend Signal} \longrightarrow \text{Aggressive Order Flow} \longrightarrow \text{Temporary \& Permanent Market Impact} \longrightarrow \text{Price Continuation} \longrightarrow \text{Sustained Trend}$$

For this loop to generate positive net returns at short horizons, trend followers must execute directional flow without instantaneous adverse liquidity withdrawal. Following the 2008 crisis, the widespread dominance of High-Frequency Trading (HFT) electronic market makers fundamentally altered liquidity dynamics:
- In **small-tick contracts** (where the tick size is negligible relative to daily volatility), HFT market makers detect predictable directional order flow and rapidly cancel resting quotes or widen spreads, removing order book depth. This creates severe adverse execution drag and breaks the self-fulfilling impact loop.
- In **large-tick contracts** (where the minimum price increment is economically significant relative to daily volatility), price priority rules and queue dynamics enforce substantial residual resting limit order depth. The impact loop continues to function, allowing short-term trend-following alpha to persist.

### Research interpretation

This mechanism provides a foundational cross-sectional conditioning filter for systematic momentum and trend models:
1. **Microstructural Regime Conditioning:** Rather than allocating capital uniformly across a trend universe or abandoning short-term trend following entirely, systematic trend allocations should be dynamically conditioned on the **volatility-normalized tick size** ($\Theta_i$).
2. **Avoidance of Adverse Impact Traps:** Small-tick markets ($\Theta \ll 1$) should be excluded from short-horizon directional strategies (< 20 days) or assigned lower weights, preventing uncompensated execution friction against predatory HFT quote fade.
3. **Selective Alpha Harvesting:** Large-tick markets ($\Theta \ge \Theta_{\text{critical}}$) retain structural queue depth and can be safely harvested using short-horizon momentum signals.

## Signal

### 1. Volatility-Normalized Tick Size Metric ($\Theta_{i, t}$)

For each asset $i$ on trading day $t$:
- Let $\Delta p_i$ be the exchange minimum price increment (tick size).
- Let $P_{i, t}$ be the daily closing price.
- Let $\sigma_{i, t}$ be the annualized daily return volatility estimated over a rolling 60-day window:
  $$\sigma_{i, t} = \sqrt{\frac{252}{59} \sum_{k=0}^{59} \left(r_{i, t-k} - \bar{r}_{i, t}\right)^2}$$
- Define the dimensionless volatility-normalized tick size:
  $$\Theta_{i, t} = \frac{\Delta p_i}{P_{i, t} \cdot \sigma_{i, t} \cdot \sqrt{\Delta t_{\text{day}}}} = \frac{\Delta p_i / P_{i, t}}{\sigma_{i, t} / \sqrt{252}}$$

### 2. Contract Classification & Regime Gate

Contracts are categorized into microstructural regimes:
- **Small-Tick Regime ($S$):** $\Theta_{i, t} < \Theta_{\text{thresh}}$ (e.g., $\Theta < 0.05$ to $0.10$), where discrete tick friction is negligible and LOB depth is easily withdrawn by HFT algorithms.
- **Large-Tick Regime ($L$):** $\Theta_{i, t} \ge \Theta_{\text{thresh}}$ (e.g., $\Theta \ge 0.10$), where tick size imposes substantial price discreteness and deep order queues.

### 3. Strategy Construction & Conditioning Overlay

Let $\text{Signal}_{i, t}^{(H)}$ be a normalized short-horizon trend signal with lookback horizon $H \in [5, 20]$ days:
$$\text{Signal}_{i, t}^{(H)} = \text{clip}\left(\frac{\text{EMA}_{H}(P_{i, t}) - P_{i, t}}{\text{ATR}_{H}(P_{i, t})}, -1, +1\right) \quad \text{or} \quad \text{sign}\left(\sum_{k=1}^H r_{i, t-k}\right)$$

The conditioned portfolio position weight $w_{i, t}$ is:
$$w_{i, t} = \begin{cases} 
0, & \text{if } \Theta_{i, t} < \Theta_{\text{thresh}} \text{ and } H \le 20 \text{ days (small-tick lockout)} \\
\frac{\text{Signal}_{i, t}^{(H)}}{\sigma_{i, t}} \cdot \left(\frac{\Theta_{i, t}}{\sum_{j \in L} \Theta_{j, t}}\right), & \text{if } \Theta_{i, t} \ge \Theta_{\text{thresh}} \text{ (large-tick active trend)} \\
\frac{\text{Signal}_{i, t}^{(H)}}{\sigma_{i, t}}, & \text{if } H \ge 50 \text{ days (long-horizon unconstrained)}
\end{cases}$$

## Required data

- **Instrument Universe:** Exchange-traded futures contracts across commodities (energy, metals, agriculture), equity index futures, sovereign bond futures, and currency futures.
- **Venues:** CME, CBOT, NYMEX, ICE, Eurex, SGX.
- **Timeframe:** Daily OHLCV bars for trend signal and volatility estimation; contract specifications for tick size ($\Delta p_i$).
- **Fields:**
  - Daily Settlement Price / Close ($P_t$).
  - Daily High, Low, Volume.
  - Contract Tick Size ($\Delta p_i$) and point value.
  - Continuous spliced futures series (using open-interest or volume rollover rules).
- **Point-in-Time Requirement:** Volatility $\sigma_{i, t}$ computed strictly up to market close $t$; signal generated for next-day open execution $t+1$.

## Execution assumptions

- **Execution Timing:** Next-day market-on-open (MOO) or TWAP over the opening 15 minutes.
- **Order Types:** Aggressive market / marketable limit orders (consistent with standard systematic CTA implementation).
- **Transaction Costs & Slippage:**
  - Large-tick contracts: Bid-ask spread fixed at 1 tick ($\Delta p_i$), with adverse selection bounded by queue priority.
  - Small-tick contracts: Variable spread + quadratic market impact model calibrated to trade size relative to ADV.
- **Leverage & Volatility Targeting:** Target annualized portfolio volatility of 10% with cash/margin collateral constraints.

## Evidence

### Source-reported

- **Structural Break Around 2008:** Across the ~100 futures contracts studied (1995–2025), short-term trend-following strategies (1-day, 5-day, 10-day, 20-day lookbacks) generated positive and statistically significant Sharpe ratios prior to 2008 (~0.6 to 1.1 annualized). Post-2008, aggregate performance across small-tick contracts degraded to near-zero or negative Sharpe ratios.
- **Cross-Sectional Tick-Size Sorting:**
  - Contracts in the top tercile/quintile of volatility-normalized tick size $\Theta$ (large-tick contracts, such as Eurodollar/Short-Rate futures, select agricultural commodities, and fixed-income contracts with large minimum ticks) retained positive trend profitability post-2008.
  - Contracts in the bottom tercile of $\Theta$ (small-tick contracts, such as equity index futures and Brent/WTI crude oil after tick refinements) experienced the most severe performance collapse.
- **Horizon Invariance for Long Trends:** For long lookback horizons ($H \ge 50$ days up to 200 days), the performance degradation post-2008 was substantially less pronounced, consistent with the hypothesis that slow macro/fundamental drift is less vulnerable to high-frequency quote fading than fast feedback loops.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Tick Refinements & Structural Policy Changes:** Exchanges periodically adjust contract tick sizes (e.g., tick halving or micro-contract launches), which can abruptly transition an asset from large-tick to small-tick regime, decaying active strategy allocations without fundamental asset changes.
- **Crowding in Large-Tick Contracts:** As systematic capital notices resilience in large-tick instruments, queue lengths in large-tick order books increase significantly, resulting in higher execution latency and non-fill risk for limit orders.

## Falsification plan

1. **Cross-Sectional Microstructural Split Test:** Sort a hold-out multi-asset universe into 3 buckets based on $\Theta_{i, t}$ (Small, Medium, Large tick). Run an identical 10-day time-series momentum rule across all buckets post-2015.
   - **Failure Rule:** If the Sharpe ratio in the Large-Tick bucket is not statistically greater than the Small-Tick bucket by at least $\Delta \text{Sharpe} \ge 0.35$ ($p < 0.05$), the tick-size conditioning hypothesis is rejected.
2. **Tick-Size Change Event Study:** Identify historical exchange tick-size reduction events (e.g., tick halved from 1.0 to 0.5). Measure strategy Sharpe ratio 2 years before vs. 2 years after the event.
   - **Failure Rule:** If short-term trend Sharpe does not drop following a tick reduction, the causal microstructural mechanism is falsified.
3. **Execution Drag & Spread Attribution:** Compare gross vs. net performance across $\Theta$ quantiles under realistic LOB slippage models.
   - **Failure Rule:** If the difference in performance between small-tick and large-tick contracts disappears when gross (zero-cost) returns are analyzed, the phenomenon is purely cost-driven rather than an impact loop failure.

## Crypto portability

**adapted**

The source studies traditional futures contracts. Portability to cryptocurrency markets requires explicit research adaptation:
- **Continuous Variable Tick Grids:** In cryptocurrency spot and perpetual markets (e.g., Binance, Bybit, OKX), exchanges dynamically adjust tick sizes ($\Delta p$) based on price tiers. BTC and ETH perpetuals generally operate with very small relative tick sizes ($\Theta \ll 0.01$), effectively behaving as extreme small-tick markets dominated by sub-millisecond HFT market makers.
- **Altcoin Large-Tick Regimes:** Low-priced altcoin perpetual contracts (where tick size is constrained to say $0.0001$ on a $0.0020$ token) frequently exhibit large-tick dynamics ($\Theta > 0.05$) with deep order queues, where short-term momentum and breakout signals may experience less immediate quote fading.
- **24/7 Continuous Trading & Funding:** Absence of discrete market opens/closes and presence of 8-hour funding payments alter continuous trend drift.

## Limitations

- **Source Scope:** Traditional exchange-traded futures contracts; findings not directly verified on crypto perpetuals in the primary source.
- **Definition of Volatility Horizon:** $\Theta$ is sensitive to the estimation window for volatility $\sigma_t$ during rapid volatility spikes (e.g., market crashes).
- **Execution Model Dependency:** Assumes aggressive taker execution; passive limit order execution introduces adverse selection and fill-rate uncertainty in large-tick books.

## Implementation status

No implementation in our research stack. The record documents published empirical and theoretical findings from Kurth et al. (CFM, 2026); no PyBroker, Nautilus, or live trading components have been created.

## Adoption boundary

This record is research material only. Presence in this repository does not mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

## Related Wiki records

- [[quant/crypto-dynamic-time-series-momentum-volatility-impulse-2026-08-31]] — Dynamic time-series momentum and volatility overlays
- [[quant/crypto-retail-systematic-trading-null-result-adversarial-audit-2026-09-01]] — Systematic trend following null results and execution hurdles
- [[quant/crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01]] — Microstructure alpha transfer and cross-asset dynamics

## Sources

1. Jutta G. Kurth, Zoltan Eisler, Adam Rej, and Jean-Philippe Bouchaud, "Is Trend Still Your Friend?: A Microstructural Account of the Demise of Short-Term Trend-Following", arXiv preprint arXiv:2607.01550v1 [q-fin.TR], published July 2026. URL: https://arxiv.org/abs/2607.01550.
