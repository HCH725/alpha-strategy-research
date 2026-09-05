---
schema: strategy-research-record-v1
title: "SAC Two-Sided Transactions with USDT Lending Portfolio on Binance Perpetual Futures"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - reinforcement-learning
  - portfolio-management
  - crypto
  - perpetual-futures
  - lending
status: research-only
confidence: medium
source_as_of: 2024-08-09
sources:
  - "arXiv:2408.05382v1 — https://arxiv.org/abs/2408.05382"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# SAC Two-Sided Transactions with USDT Lending Portfolio on Binance Perpetual Futures

## Provenance

- **Paper:** Optimizing Portfolio with Two-Sided Transactions and Lending: A Reinforcement Learning Framework
- **Authors:** Ali Habibnia, Mahdi Soltanzadeh
- **arXiv:** [2408.05382v1](https://arxiv.org/abs/2408.05382) — submitted 2024-08-09
- **URL:** https://arxiv.org/html/2408.05382v1
- **Source as-of:** 2024-08-09 (v1)

## Economic mechanism

### Source-reported

The authors propose that standard RL-based portfolio models fail to exploit the full opportunity set available in crypto perpetual futures markets because they restrict actions to long-only or exclude lending/borrowing. By allowing **two-sided transactions** (simultaneous long and short positions across assets) and **USDT lending/borrowing** (earning interest on idle capital or borrowing to increase exposure), the agent can capture more market opportunities. The PnL-based reward function with a penalty term is designed to improve convergence in this more complex environment by explicitly controlling downside risk during training.

### Research interpretation

The hypothesized alpha mechanism is: (1) **dynamic long/short allocation** captures returns from both rising and falling crypto assets, rather than only bullish exposure; (2) **USDT lending** earns yield on capital that would otherwise sit idle in the portfolio, adding a small but steady return component; (3) **USDT borrowing** allows the agent to lever up when opportunities are favorable, amplifying returns (but also risk). The core claim is that the combination of these three mechanisms, governed by a learned policy, produces superior risk-adjusted returns compared to traditional single-period optimization (MV, MAD, CVaR) or naive return-based RL.

This is primarily a **portfolio construction and capital allocation** mechanism, not a directional alpha signal. The agent learns a policy for weight allocation across 12 crypto perpetual futures, rebalancing every 4 hours.

## Signal

- **Formation timestamp:** State observed at each 4-hour rebalancing interval; action (portfolio weight vector) executed immediately after observation.
- **Lookback:** 48 hours of hourly price data (N=49 observations) used as input state.
- **Entry/Exit:** Continuous weight allocation across 12 crypto perpetual futures (ADA, BNB, BTC, DASH, DOGE, DOT, ETH, LINK, LTC, MANA, MATIC, SOL — all USDT-margined). The agent outputs a weight vector; rebalancing is performed to match target weights.
- **Holding period:** 4-hour rebalancing cadence; positions held until next rebalance.
- **Parameters:**
  - Rebalancing frequency: 4 hours
  - Historical lookback: 48 hours
  - Penalty parameter in reward function: 25 (agent sensitivity to loss is 25x sensitivity to profit)
  - Transaction fee: 0.05% per trade
  - Annual borrowing rate (USDT): 5%
  - Annual lending rate (USDT): 3%
  - Initial investment: $1,000
  - SAC hyperparameters: actor LR=2e-4, critic LR=6e-4, discount=0.99, entropy weight=0.08, batch size=16
- **Position sizing:** Fully determined by the SAC agent's policy output (continuous weight vector, summing to leverage-adjusted total).

## Required data

- **Universe:** 12 crypto assets (ADA, BNB, BTC, DASH, DOGE, DOT, ETH, LINK, LTC, MANA, MATIC, SOL) on Binance perpetual futures (USDT-margined).
- **Venue:** Binance USD-M perpetual futures.
- **Market type:** Perpetual futures (USDT-settled).
- **Timeframe:** Hourly OHLCV for input; 4-hour rebalancing.
- **Fields:** Close price (hourly); no order-book, funding, or alternative data used.
- **Point-in-time:** Hourly price data sourced from www.cryptodatadownload.com; no point-in-time or survivorship-bias treatment described.
- **Timestamp:** Not specified; assumed UTC based on Binance convention.
- **Missing data:** Not addressed.
- **Funding/fee/spread:** Transaction fee modeled at 0.05%. Borrowing rate 5% p.a., lending rate 3% p.a. Spread, slippage, and market impact are not modeled.

## Execution assumptions

- **Signal-to-order timing:** Same-bar execution (rebalance immediately at decision time).
- **Order type:** Assumed market orders with instant execution.
- **Fill model:** Full liquidity assumed — all transactions execute instantly at observed prices.
- **Fees:** 0.05% per transaction.
- **Spread:** Not modeled.
- **Slippage:** Not modeled.
- **Impact / capacity:** Not modeled; assumes no price impact from trading.
- **Funding:** USDT borrowing at 5% p.a., lending at 3% p.a.
- **Leverage / margin:** Implicitly available through two-sided positions and borrowing, but explicit leverage limits are not stated.
- **Partial fills / failures:** Not addressed.

**Critical limitation:** The paper assumes full liquidity and market neutrality (transactions do not affect prices). These are strong assumptions for a 12-asset crypto perpetual portfolio with 4-hour rebalancing. Real-world execution would face spread, slippage, and capacity constraints that could materially erode returns.

## Evidence

### Source-reported

From Table 4 of the paper (testing results):

**Portfolio A (high-volatility period: May 2021 – Sep 2022, 4-month test):**
- Total return: 575.585%
- Win rate: 52.840%
- Average 4-hour return: 0.347%
- Std dev: 4.181%
- Sharpe ratio: 10.468
- Downside deviation: 3.031%
- Sortino ratio: 14.442
- Max drawdown: 65.519%
- Calmar ratio: 18.149

**Portfolio B (low-volatility period: Jun 2022 – Oct 2023, 4-month test):**
- Total return: 145.627%
- Win rate: 51.730%
- Average 4-hour return: 0.139%
- Std dev: 1.815%
- Sharpe ratio: 3.557
- Downside deviation: 1.187%
- Sortino ratio: 5.438
- Max drawdown: 18.370%
- Calmar ratio: 9.507

Benchmarks (MV, MAD, CVaR, return-based RL) produced negative or low-positive returns in both periods. The return-based RL failed to converge, suggesting the standard return reward function is inadequate for this more complex environment.

**Caveats:** These are source-reported backtest results. The Sharpe ratios are extremely high (10.468 in Port A) and may reflect overfitting to the training period or unrealistic execution assumptions (full liquidity, no slippage). The training period (12 months) immediately precedes the test period (4 months), which does not provide out-of-sample temporal separation from the most recent training data.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The paper acknowledges that full liquidity and market neutrality assumptions are unrealistic.
- Port A's max drawdown of 65.519% indicates substantial risk even with the proposed model.
- The win rates (~52%) are only marginally above random, suggesting returns are driven by magnitude of wins vs. losses rather than directional accuracy.
- The return-based RL benchmark failed to converge, which may indicate the environment is challenging but does not validate that the proposed model's convergence is robust.
- No walk-forward, rolling window, or out-of-sample robustness testing is described.

## Falsification plan

1. **Out-of-sample temporal separation:** Extend the test period beyond 4 months and introduce a gap between training and test sets to assess overfitting.
2. **Walk-forward validation:** Implement rolling-window training with out-of-sample testing across multiple market regimes (bull, bear, sideways, crash).
3. **Cost sensitivity:** Re-run with realistic spread (1-5 bps), slippage models, and capacity constraints to determine if returns survive transaction costs beyond the modeled 0.05%.
4. **Parameter perturbation:** Vary penalty parameter (25), lookback (48h), rebalancing frequency (4h), and borrowing/lending rates to assess stability.
5. **Universe robustness:** Test on different subsets of assets, different venues, and different time periods not used in training.
6. **Failure threshold:** If the Sharpe ratio drops below 1.0 or the model underperforms a simple equally-weighted buy-and-hold after realistic costs, the hypothesis is weakened.
7. **Action following failure:** If falsified, the two-sided/lending mechanism alone is insufficient without a robust directional signal; investigate whether the alpha comes from the signal or the capital structure.

## Crypto portability

**Direct** — the paper is natively designed for and tested on Binance perpetual futures with 12 crypto assets.

Crypto-specific considerations:
- Funding rates on perpetual futures are not modeled; in practice, funding rates can be significant (positive or negative) and would affect the cost of maintaining long/short positions.
- The lending/borrowing rates (5%/3%) are assumed fixed; in reality, DeFi and CeFi lending rates are volatile and regime-dependent.
- 24/7 market structure is implicitly handled by the 4-hour rebalancing cadence.
- Venue fragmentation: results are specific to Binance; execution on other venues may differ.
- Liquidation risk on leveraged perpetual positions is not explicitly modeled.

## Limitations

- **Full liquidity and market neutrality assumptions** — unrealistic for crypto perpetual futures; spread, slippage, and market impact are not modeled.
- **No funding rate modeling** — perpetual futures funding rates are a material cost component that is completely omitted.
- **Limited training data** — 12 months of training with immediate 4-month test; no walk-forward or cross-validation.
- **High Sharpe ratios (10.468)** — suspiciously high and likely reflect favorable train/test regime alignment rather than robust alpha.
- **No alternative data** — only hourly close prices used; no order-book, sentiment, on-chain, or funding data.
- **Fixed lending/borrowing rates** — assumed constant; real rates are volatile.
- **No position limits or leverage caps** described.
- **Single venue** — Binance only; generalizability untested.
- **Source-reported results only** — not independently reproduced.
- **data gap** — collateral requirements for borrowing are explicitly assumed away.

## Implementation status

Not implemented. No code or implementation in our research stack.

## Adoption boundary

This record is research material only. Its presence in this repository does not mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

The extremely high reported Sharpe ratios should be treated with significant skepticism given the unrealistic execution assumptions and limited out-of-sample testing.

## Related Wiki records

- [[quant/crypto-perpetual-funding-rate-carry-spot-perp-2026-08-31]] — related topic of perpetual futures funding rate mechanics
- [[quant/crypto-perpetual-no-arbitrage-deviation-2026-08-31]] — related topic of perpetual futures pricing

## Sources

- Habibnia, A. & Soltanzadeh, M. (2024). Optimizing Portfolio with Two-Sided Transactions and Lending: A Reinforcement Learning Framework. arXiv:2408.05382v1. https://arxiv.org/abs/2408.05382
