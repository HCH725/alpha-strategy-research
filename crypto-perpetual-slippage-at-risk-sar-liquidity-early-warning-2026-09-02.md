---
schema: strategy-research-record-v1
title: "Slippage-at-Risk (SaR): Forward-Looking Order Book Liquidity Risk and Cascading Liquidation Early Warning"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - limit-order-book
  - liquidity-risk
  - slippage-at-risk
  - liquidation-cascade
  - market-microstructure
  - hyperliquid
status: research-only
confidence: medium
source_as_of: 2026-03-10
sources:
  - "Otar Sepper, 'Slippage-at-Risk (SaR): A Forward-Looking Liquidity Risk Framework for Perpetual Futures Exchanges', arXiv:2603.09164v1 [q-fin.RM, q-fin.TR], March 10, 2026. https://arxiv.org/abs/2603.09164"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Slippage-at-Risk (SaR): Forward-Looking Order Book Liquidity Risk and Cascading Liquidation Early Warning

## Provenance

- **Primary Paper:** Otar Sepper, *"Slippage-at-Risk (SaR): A Forward-Looking Liquidity Risk Framework for Perpetual Futures Exchanges"*, arXiv preprint `arXiv:2603.09164v1 [q-fin.RM, q-fin.TR]`, published March 10, 2026. URL: https://arxiv.org/abs/2603.09164.
- **Author:** Otar Sepper (Tallinn University of Technology / Decentralized Systems Lab).
- **Primary Categories:** Risk Management (`q-fin.RM`), Trading and Market Microstructure (`q-fin.TR`).
- **Dataset / Empirical Venue:** High-resolution Level-2 and Level-4 limit order book (LOB) event telemetry from the Hyperliquid decentralized perpetual futures exchange, specifically evaluating market-wide liquidity dynamics during the October 10, 2025 cryptocurrency liquidation cascade.

## Economic mechanism

### Source-reported

Traditional exchange risk frameworks rely on backward-looking Value-at-Risk (VaR) or Expected Shortfall (ES) computed from historical return distributions. In leveraged cryptocurrency perpetual futures markets, historical volatility models break down because execution risk is endogenous: when forced liquidations trigger, large market orders sweep resting limit order book depth, creating massive instantaneous slippage, price dislocations, and cascading secondary liquidations.

Sepper introduces **Slippage-at-Risk (SaR)**, a forward-looking liquidity risk framework that evaluates real-time order book capacity against potential liquidation shock distributions. The framework defines three foundational metrics:
1. **$\text{SaR}(\alpha)$:** The cross-sectional slippage quantile—the maximum percentage price dislocation expected at confidence level $1 - \alpha$ for a given liquidation order flow shock.
2. **$\text{ESaR}(\alpha)$:** The expected tail slippage conditional on exceeding the $\text{SaR}(\alpha)$ threshold.
3. **$\text{TSaR}(\alpha)$:** The aggregate dollar-denominated loss absorbed by market participants in the tail of the liquidation distribution.

Crucially, the paper introduces a **Concentration Adjustment** using the Herfindahl-Hirschman Index ($\text{HHI}$) of resting market maker depth:
$$\text{SaR}^*(\alpha) = \text{SaR}(\alpha) \cdot \left(1 + \kappa \cdot \text{HHI}_{\text{makers}}\right)$$
A market with high nominal depth dominated by 1–2 algorithmic market makers is penalized as fragile, because single-actor quote withdrawals instantly trigger deep liquidity vacuums.

### Research interpretation

This mechanism provides a dual-purpose quantitative edge:
1. **Defensive Liquidity Quoting & Inventory Protection:**
   - Market makers quoting passive limit orders can monitor $\text{SaR}^*(\alpha)$ in real-time. When $\text{SaR}^*$ spikes (signaling an imminent liquidity vacuum or liquidation cascade), algorithms can preemptively pull bids, widen spreads by $\Delta = 2 \times \text{ESaR}$, or reduce inventory limits before toxic liquidation flow hits the book.
2. **Offensive Liquidation Cascade Overshoot Capture:**
   - Liquidation engines execute mechanical market orders that exhaust order book depth down to the predicted tail slippage level $P_{\text{floor}} \approx P_{\text{mid}} \cdot (1 - \text{ESaR}(\alpha))$.
   - Systematic mean-reversion traders can place resting limit buy orders at $P_{\text{floor}}$, capturing violent price overshoots and subsequent mean-reverting liquidity replenishment.

## Signal

### 1. Order Book Sweep Function & Liquidation Shock Modeling
- **LOB Sweep Function:** Let $Q_t(p)$ be the cumulative bid depth available at price $p \le P_{\text{mid}, t}$. The execution price $\bar{P}(V)$ for a sell market order of notional volume $V$ satisfies:
  $$V = \int_{\bar{P}(V)}^{P_{\text{mid}, t}} Q_t(p) dp$$
  The percentage slippage is:
  $$S_t(V) = \frac{P_{\text{mid}, t} - \bar{P}(V)}{P_{\text{mid}, t}}$$
- **Liquidation Shock Distribution:** Let $f_L(V)$ be the probability density function of potential forced liquidation volume over a 5-minute horizon, estimated from aggregate open interest and cross-sectional leverage distributions:
  $$V \sim \text{Generalized Pareto}(\xi, \sigma, \mu_L)$$

### 2. SaR Metric Calculation
- **Slippage Quantile ($\text{SaR}_\alpha$):**
  $$\mathbb{P}\left(S_t(V) \ge \text{SaR}_\alpha\right) = \alpha \quad (\text{e.g., } \alpha = 0.05)$$
- **Expected Tail Slippage ($\text{ESaR}_\alpha$):**
  $$\text{ESaR}_\alpha = \mathbb{E}\left[S_t(V) \mid S_t(V) \ge \text{SaR}_\alpha\right]$$
- **Maker Concentration Penalty:**
  $$\text{HHI}_t = \sum_{m=1}^M \left(\frac{D_{m, t}}{\sum_{j=1}^M D_{j, t}}\right)^2$$
  where $D_{m, t}$ is the resting depth provided by maker wallet $m$ within 100 bps of midprice.
  $$\text{SaR}^*_t(\alpha) = \text{SaR}_\alpha \cdot (1 + \kappa \cdot \text{HHI}_t), \quad \kappa \approx 0.5$$

### 3. Systematic Trading Rules

#### Mode A: Defensive Risk Filter (Market Making & Carry Overlay)
- **Normal State:** If $\text{SaR}^*_t(0.05) < \theta_{\text{normal}}$, maintain standard tight quoting spreads ($\pm 2$ bps) and full inventory allocation.
- **Fragility Alert:** If $\text{SaR}^*_t(0.05) \ge \theta_{\text{alert}}$ (e.g., $> 150$ bps), immediately cancel resting bids in top 3 levels and widen quoting spreads to $\text{Spread}_t = 2.0 \times \text{ESaR}_t(0.05)$.
- **Hard Freeze:** If $\text{SaR}^*_t(0.01) \ge \theta_{\text{critical}}$ (e.g., $> 500$ bps), pull all resting maker orders and flatten net long delta.

#### Mode B: Offensive Cascade Mean-Reversion Entry
- **Trigger:** When cumulative forced liquidation prints exceed volume threshold $V_{\text{cascade}}$ within 60 seconds and $\text{SaR}^*_t(0.01)$ spikes.
- **Entry Price:** Place resting limit buy orders at:
  $$P_{\text{entry}} = P_{\text{mid}, t_0} \cdot \left(1 - \text{ESaR}_t(0.01)\right)$$
- **Take Profit / Exit:** Limit sell at $P_{\text{exit}} = P_{\text{entry}} \cdot (1 + 0.6 \times \text{ESaR}_t)$; maximum holding time 15 minutes.
- **Stop Loss:** Hard stop at $P_{\text{stop}} = P_{\text{entry}} \cdot (1 - 0.5 \times \text{ESaR}_t)$.

## Required data

- **Instrument:** Perpetual futures contracts (e.g., BTC-PERP, ETH-PERP, SOL-PERP).
- **Universe:** High-leverage perpetual contracts on transparent DEXs and centralized exchanges.
- **Venue:** Hyperliquid, dYdX, Binance Futures, Bybit.
- **Timeframe:** Subsecond tick event streams (Level-2 LOB snapshots at 100ms intervals, or Level-4 order placement/cancel/trade logs).
- **Fields:**
  - Full-depth bid/ask price and size arrays (levels $1$ to $50$).
  - Maker wallet / account identifiers (for HHI calculation on transparent venues).
  - Real-time open interest (OI) and liquidation print streams.
  - Mark price, index price, funding rate.
- **Point-in-time:** Real-time WebSocket streaming; causal rolling 5-minute liquidation volume calibration.

## Execution assumptions

- **Execution Venue:** Direct RPC / WebSocket connection to Hyperliquid validator nodes or CEX colocation.
- **Order Types:**
  - Defensive: Ultra-low latency cancellation requests (`batch_cancel`).
  - Offensive: Resting post-only limit buy orders placed deep in the book prior to liquidation cascade arrival.
- **Latency Requirement:** Order cancellation latency < 50ms to front-run cascading market orders.
- **Fees:** VIP DEX maker rebate (0.00% to -0.005%) or standard maker tier; offensive fills capture maker rebate on deep limit orders.

## Evidence

### Source-reported

- **Empirical Event Study (October 10, 2025 Liquidation Cascade):**
  - Analyzed order book microstructure across Hyperliquid perpetual markets during a systemic market-wide deleveraging event.
  - **Early Warning Lead Time:** $\text{SaR}^*(0.05)$ and $\text{ESaR}(0.05)$ spiked **15 to 45 minutes prior** to the main liquidation cascade, as market makers quietly thinned quotes and maker HHI concentrated from 0.18 to 0.42.
  - **Predictive Superiority:** Forward-looking SaR correctly predicted the magnitude of maximum realized slippage ($4.8\%$ on SOL-PERP) within a $12\%$ error band, whereas historical 99% VaR underestimated realized price dislocation by more than $300\%$.
  - **Capital Optimization:** The paper shows that exchanges and market makers calibrating margin and capital buffers to $\text{TSaR}(0.01)$ eliminate protocol bad debt while requiring $28\%$ less static capital during calm regimes.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **CEX Telemetry Asymmetry:** On centralized exchanges (Binance, Bybit), maker account identities are anonymized, making direct computation of maker HHI impossible without proprietary broker-level feeds. Aggregate top-5 depth must be used as an imperfect proxy.
- **False-Alarm Whipsaws:** Temporary quote pulls during macro announcements (e.g., FOMC, CPI) cause sharp spikes in SaR without subsequent liquidation cascades, causing defensive strategies to miss trading volume.
- **Liquidation Engine Pacing:** Some exchanges employ TWAP-style gradual liquidation algorithms that avoid sweeping the entire book at once, dampening instantaneous slippage and delaying the overshoot trigger.

## Falsification plan

1. **Lead-Time Cascade Prediction Test:** Measure whether $\text{SaR}^*(0.05) > 2.0 \times \text{baseline}$ predicts a subsequent $> 2\%$ rapid price dislocation within 30 minutes with Area Under the ROC Curve (AUC) $> 0.75$. **Failure rule:** If AUC $\le 0.55$, the forward-looking early warning hypothesis is rejected.
2. **Defensive Spread Widening Backtest:** Compare the Sharpe ratio and maximum drawdown of a passive market maker employing SaR-conditioned spread widening vs. static quoting across high-volatility months. **Failure rule:** If SaR spread widening does not reduce maker inventory drawdown during cascades by at least $25\%$, the defensive utility is falsified.
3. **Offensive Dip-Fill Realization Test:** Backtest resting limit buy orders placed at $P_{\text{mid}} \cdot (1 - \text{ESaR}(0.01))$. **Failure rule:** If post-fill 15-minute mean return is $\le 0.0\%$ (net of fees), the cascade overshoot mean-reversion hypothesis is falsified.

## Crypto portability

**direct**

The Slippage-at-Risk (SaR) framework is directly tailored to cryptocurrency derivatives market mechanics:
- **Perpetual Liquidation Engines:** Crypto perpetuals feature automated, transparent liquidation engines that trigger market orders when account margin falls below maintenance thresholds, creating deterministic order book sweeps.
- **Transparent DEX Telemetry:** Decentralized order book DEXs (Hyperliquid, Paradex, dYdX) publish cleartext maker IDs and complete order books, allowing exact computation of maker HHI and forward-looking sweep integrals in real time.

## Limitations

- **High-Frequency Computational Overhead:** Continuous numerical integration of the LOB sweep function $S_t(V)$ across 50 book levels requires optimized low-latency code (Rust / C++).
- **Extreme Tail Uncertainty:** Estimating the tail parameter $\xi$ of the Generalized Pareto distribution for liquidation volume is subject to parameter uncertainty during unprecedented macro shocks.
- **Exchange Rule Dependency:** Dependent on specific exchange liquidation mechanics (market order sweep vs. internal insurance fund absorption vs. ADL).

## Implementation status

No implementation in our research stack. The paper provides theoretical derivation, empirical event analysis on Hyperliquid, and risk metrics; no production code or live execution pipeline has been deployed.

## Adoption boundary

This record is research material only. Presence in this repository does not mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

## Related Wiki records

- [[quant/crypto-perpetual-liquidation-cascade-overshoot-reversal-2026-08-31]] — Liquidation cascade overshoot and mean reversion
- [[quant/crypto-perpetual-autodeleveraging-trilemma-queue-haircut-2026-09-02]] — Auto-deleveraging queue haircuts and exchange risk
- [[quant/crypto-public-wallet-identity-trader-informativeness-adverse-selection-2026-09-02]] — Public wallet identity and adverse selection on Hyperliquid

## Sources

1. Otar Sepper, "Slippage-at-Risk (SaR): A Forward-Looking Liquidity Risk Framework for Perpetual Futures Exchanges", arXiv preprint arXiv:2603.09164v1 [q-fin.RM, q-fin.TR], published March 10, 2026. URL: https://arxiv.org/abs/2603.09164.
