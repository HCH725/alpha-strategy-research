---
schema: strategy-research-record-v1
title: Crypto Futures State-Dependent L2 Liquidity-State Transitions and Order-Flow Additivity
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - market-microstructure
  - order-book
  - order-flow
  - liquidity-regimes
  - event-windows
status: research-only
confidence: high
source_as_of: 2026-05
sources:
  - "Joohyoung Jeon, 'When Does Order Flow Matter? State-Dependent L2 Liquidity-State Transitions in Crypto Futures', arXiv:2607.09230v1 [q-fin.TR], July 2026. https://arxiv.org/abs/2607.09230"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Futures State-Dependent L2 Liquidity-State Transitions and Order-Flow Additivity

## Provenance

- **Primary Source:** Joohyoung Jeon (Korea University), "When Does Order Flow Matter? State-Dependent L2 Liquidity-State Transitions in Crypto Futures", arXiv:2607.09230v1 [q-fin.TR], July 2026. Stable reference: https://arxiv.org/abs/2607.09230 (HTML: https://arxiv.org/html/2607.09230v1).
- **Universe & Sample:** Binance BTCUSDT and ETHUSDT perpetual futures spanning January 2023 through May 2026 across 40 rolling monthly out-of-sample folds.
- **Dataset Composition:** Top-20 limit-order-book (L2) snapshots sampled at 1-minute frequency (per-level bid/ask prices and sizes for 20 best levels), continuous aggregate trade flow (signed taker volume, trade counts, quantity, VWAP, returns), and scheduled macroeconomic release calendar (8,953 US event windows, plus Euro Area, Japan, UK, China).
- **Modeling Panel:** 47,513 windows per horizon, comprising 18,631 scheduled event windows (BTC: 9,330; ETH: 9,301) and 28,882 matched non-event control windows. Pre-event state base distribution: calm (~21%), mixed (~54%), stressed (~25%).

## Economic mechanism

### Source-reported

Jeon (2026) investigates whether persistent microstructure states dominate event-conditioned dynamics around scheduled information releases, formulating a supervised discrete L2 liquidity-state transition task rather than price-direction forecasting.

Key source-reported empirical findings:
1. **First-Order State Persistence:** The pre-event L2 liquidity state (relative spread, top-20 depth, and top-20 imbalance) is the primary predictor of post-event liquidity regimes. A coarse 3-class discrete state baseline beats the marginal frequency model on roughly two-thirds of held-out rows (improving by +0.034 at 1-minute and +0.045 at 5-minute horizons in joint negative log-likelihood $\Delta\text{NLL}$ and Brier $\Delta\text{Brier}$ scores).
2. **Linear Continuous Models Fail:** Feeding continuous L2 features into multinomial or ordered logit models underperforms the coarse discrete state baseline (-0.048 and -0.034 for multinomial logit; -0.052 and -0.047 for ordered logit). Continuous features only add predictive value when modeled nonlinearly.
3. **Nonlinear L2 Book Shape Gain:** A shallow histogram gradient-boosted classifier (depth 3, 60 iterations, learning rate 0.05, $L_2$ reg 1.0) over multi-scale L2 descriptors improves over the coarse state baseline by +0.044 (1m) and +0.060 (5m) (BTC: +0.037/1m, +0.052/5m; ETH: +0.052/1m, +0.067/5m; 90% bootstrap intervals exclude zero).
4. **State-Dependent, Asset-Asymmetric Order Flow:** Local order flow provides incremental predictive value *only* when layered on top of the nonlinear L2 shape model, not as a replacement. Furthermore, this additivity is strictly **ETH-dominant and stress-amplified**:
   - For ETH: Order flow adds +0.020 (1m) and +0.016 (5m) over the L2 baseline, clearing 95th-percentile blocked flow-shuffle nulls (0.006 and 0.003) with 90% event-cluster interval [.020, .023] (1m) and [.015, .018] (5m), with largest gains under pre-event liquidity stress.
   - For BTC: Order flow adds only +0.001 (1m) and +0.003 (5m), failing to separate from shuffle nulls across both horizons.

### Research interpretation

The falsifiable thesis is a **state-first microstructure conditioning principle**:
1. **Liquidity Regime Transition Mechanism:** Market participants withdrawing liquidity before scheduled events create persistent structural imbalances across the top-20 order book levels. The post-event market quality (spread widening, depth depletion, adverse selection) is primarily determined by this pre-existing limit-order book geometry rather than the macroeconomic label itself.
2. **Asymmetric Order-Flow Informativeness:** Order flow carries state-dependent predictive power for future liquidity transitions only in less saturated/more elastic books (ETH), whereas in high-liquidity anchor contracts (BTC), top-20 depth and spread shape already reflect available flow information.
3. **Execution & Market-Making Alpha Overlay:** Rather than trading unconditional order flow imbalance or naive price breakouts, quoting algorithms and execution schedulers must condition risk and spread-width multipliers on predicted post-event liquidity transitions ($S^{\text{post}} \in \{\text{calm}, \text{mixed}, \text{stressed}\}$).

## Signal

1. **Feature Construction (Lookback $[t-5\text{min}, t)$):**
   - **Relative Spread:** $\frac{P_{\text{ask},1} - P_{\text{bid},1}}{P_{\text{mid}}}$.
   - **Top-20 Depth:** Sum of base volume across top-20 bid and ask price levels ($\sum_{i=1}^{20} (Q_{\text{bid},i} + Q_{\text{ask},i})$), negated for orientation.
   - **Top-20 Imbalance:** Absolute order book volume imbalance $\frac{|\sum Q_{\text{bid},i} - \sum Q_{\text{ask},i}|}{\sum Q_{\text{bid},i} + \sum Q_{\text{ask},i}}$.
2. **Discrete State Assignment ($S^{\text{pre}}$):**
   - Compute symbol-specific tercile thresholds from training folds only.
   - Count how many oriented descriptors fall in their top (least liquid) tercile, capped at 2:
     - 0 severe descriptors $\to$ **Calm** ($S=0$)
     - 1 severe descriptor $\to$ **Mixed** ($S=1$)
     - $\ge 2$ severe descriptors $\to$ **Stressed** ($S=2$)
3. **Nonlinear Model & Order-Flow Layer (for ETH):**
   - Fit shallow gradient-boosted tree (max depth 3, 60 iterations, learning rate 0.05, $L_2$ regularization 1.0) on multi-scale L2 summary descriptors plus signed taker volume, trade count, volume-weighted average price (VWAP) deviation, and trade return over $[t-5\text{min}, t)$.
4. **Transition Output & Action Policy:**
   - Model outputs calibrated class probability distribution: $\hat{P}(S^{\text{post}} = k \mid \mathbf{x}_{\text{pre}}), k \in \{0, 1, 2\}$.
   - If $\hat{P}(S^{\text{post}} = \text{Stressed}) > \theta_{\text{stress}}$, withdraw passive maker limit orders or widen quotes dynamically; shift liquidity provision to post-event mean-reversion capture once the stress state resolves.

## Required data

- **Instruments:** Binance BTCUSDT and ETHUSDT perpetual futures.
- **Order Book Data:** Top-20 Level 2 (L2) order book snapshots at 1-minute cadence (prices and quantities for 20 best bid and ask levels).
- **Trade Flow Data:** Aggregate trade feed with millisecond timestamps, trade size, price, and aggressor buyer/seller flag.
- **Event Calendar Feed:** Timestamped schedule of macroeconomic announcements (US CPI, NFP, FOMC, GDP, plus major global economic releases).

## Execution assumptions

- **Execution Cadence:** 1-minute and 5-minute post-event evaluation windows.
- **Prediction Target:** Discrete transition probability distribution over 3 liquidity states ($h=1\text{min}, h=5\text{min}$), not sub-second execution queue simulation.
- **Costs & Sizing:** Model is designed for dynamic quoting, execution scheduling, and liquidity-state awareness. Direct taker execution must account for elevated spreads during the stressed regime.

## Evidence

### Source-reported

All figures below are directly reported by Jeon (arXiv:2607.09230v1, July 2026) across 40 rolling monthly out-of-sample folds (2023–2026):
- **Pre-Event State Baseline vs. Marginal:** Joint improvement of +0.034 (1m horizon) and +0.045 (5m horizon) in $\Delta\text{NLL}$ / $\Delta\text{Brier}$ scores; beats marginal model on ~66% of held-out rows. Realized volatility tercile baseline improves by only +0.008 (1m) and +0.015 (5m), confirming that spread/depth/imbalance state carries distinct predictive signal.
- **Linear Continuous Logit vs. State Baseline:** Multinomial logit underperforms by -0.048 (1m) and -0.034 (5m); ordered logit underperforms by -0.052 (1m) and -0.047 (5m).
- **Nonlinear L2-Shape Model vs. State Baseline:** Improves by +0.044 (1m) and +0.060 (5m) (BTC: +0.037/1m, +0.052/5m; ETH: +0.052/1m, +0.067/5m; 90% cluster bootstrap intervals strictly positive). Three-state accuracy: 0.586 (1m) and 0.554 (5m) against majority base rates 0.571 and 0.532.
- **Order-Flow Overlay Increment:**
  - Pooled: +0.010 (1m and 5m) over L2 shape baseline.
  - ETH: +0.020 (1m) and +0.016 (5m), exceeding the 95th-percentile flow-shuffle nulls (0.006 and 0.003) with 90% event-cluster bootstrap interval [.020, .023] at 1m and [.015, .018] at 5m.
  - BTC: +0.001 (1m) and +0.003 (5m), failing the 95th-percentile flow-shuffle null across both horizons.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Linear modeling of continuous L2 features reliably degrades performance relative to simple discrete state terciles, indicating that linear models overfit or misweight high-frequency order book noise.
- Order flow is **not** universally informative across major crypto assets: BTC futures show negligible incremental predictive power from order flow over L2 book shape, falsifying the assumption of uniform order flow alpha across cryptocurrencies.

## Falsification plan

1. **Cross-Venue Stability Test:** Evaluate the staged model sequence on Bybit and OKX perpetual futures order books. If ETH order flow fails to clear blocked flow-shuffle nulls on non-Binance venues, reject cross-venue portability.
2. **Expansion to Broader Altcoin Universe:** Test whether the order-flow additivity pattern scales monotonically with lower market cap / thinner liquidity (e.g. SOL, DOGE, AVAX). If altcoins exhibit BTC-like order-flow insensitivity, reject the liquidity-elasticity thesis.
3. **Live Execution PnL Impact:** Integrate the predicted transition probabilities into a maker quoting strategy. If conditioning quote width on predicted $S^{\text{post}}=\text{Stressed}$ fails to reduce adverse selection fill costs relative to a static spread baseline, reject execution utility.

## Crypto portability

**Direct**: Evaluated directly on native Binance BTCUSDT and ETHUSDT perpetual futures with 24/7 continuous order book and trade data.

## Limitations

- **Not independently reproduced.**
- **Cadence Resolution:** 1-minute snapshot resolution does not model sub-second queue priority or individual order cancellations.
- **Asset Specificity:** Order flow overlay is established only for ETH, not BTC.
- **Macro Surprise Excluded:** Model deliberately ignores announcement surprise numbers, utilizing only release timestamps.

## Implementation status

Not implemented. No PyBroker, NautilusTrader, paper, testnet, or live trading verification.

## Adoption boundary

Research material only. Does not constitute trading advice, production validation, or authorization for live deployment.

## Related Wiki records

- `[[quant/crypto-multilevel-order-flow-imbalance-intraday-2026-08-31]]`
- `[[quant/contrarian-market-making-fill-probability-order-flow-2026-09-01]]`
- `[[quant/bitcoin-fomc-announcement-event-drift-contraction-2026-09-01]]`

## Sources

1. Joohyoung Jeon, "When Does Order Flow Matter? State-Dependent L2 Liquidity-State Transitions in Crypto Futures", arXiv:2607.09230v1 [q-fin.TR], July 2026. https://arxiv.org/abs/2607.09230.
2. Complete paper text and tables: https://arxiv.org/html/2607.09230v1.
