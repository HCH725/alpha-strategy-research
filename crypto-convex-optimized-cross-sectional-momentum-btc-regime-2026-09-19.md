---
schema: strategy-research-record-v1
title: "Convex-Optimized Cross-Sectional Cryptocurrency Momentum with BTC Regime Overlay"
created: 2026-09-19
updated: 2026-09-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional-momentum
  - convex-optimization
  - portfolio-construction
  - shrinkage-covariance
  - regime-filter
status: research-only
confidence: medium
source_as_of: 2026-08-05
sources:
  - "https://github.com/afries24/crypto-cross-sectional-momentum (branch: crypto-cross-sectional-momentum, commit: ebf50df665f96880e60dcea0c429bab6aa42af3a)"
  - "https://github.com/afries24/crypto-cross-sectional-momentum/blob/crypto-cross-sectional-momentum/Convex_Opt_Final+Project.py"
  - "https://github.com/afries24/crypto-cross-sectional-momentum/blob/crypto-cross-sectional-momentum/README.md"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Convex-Optimized Cross-Sectional Cryptocurrency Momentum with BTC Regime Overlay

## Provenance

- **Author:** Aiden Fries
- **Repository:** https://github.com/afries24/crypto-cross-sectional-momentum
- **Branch:** `crypto-cross-sectional-momentum`
- **Full commit SHA:** `ebf50df665f96880e60dcea0c429bab6aa42af3a`
- **Primary source file:** `Convex_Opt_Final+Project.py` (also `src/strategy.py` in earlier commit)
- **README date:** July 26, 2026
- **Latest commit date:** August 5, 2026
- **Source type:** GitHub educational research project with full Python implementation and backtest results
- **Note:** The repository contains 3 commits on the `crypto-cross-sectional-momentum` branch. The README and strategy code are verified at the latest commit SHA above.

## Economic mechanism

### Source-reported

The author hypothesizes that cross-sectional momentum (relative-strength ranking) predicts weekly returns in major cryptocurrencies because information diffuses gradually, investor attention is uneven, and flows chase recent winners (Jegadeesh and Titman, 1993). These mechanisms may be especially relevant in crypto markets due to continuous trading, fragmented participation, and heterogeneous asset-level response speeds to market-wide narratives.

The author further hypothesizes that convex mean-variance optimization with shrinkage covariance improves risk control relative to equal-weight momentum, by allocating more capital to assets with favorable risk-adjusted momentum contributions and constraining gross exposure.

### Research interpretation

The mechanism is cross-sectional momentum with covariance-aware portfolio construction and a conditional directional tilt via a BTC regime filter.

Component roles:
- **Primary signal:** Cross-sectional ranking by trailing L-week return; assets in the upper quantile are long candidates, lower quantile are short candidates.
- **Regime filter:** BTC 200-day moving average; when BTC is above the MA (bull regime), short candidates are disabled, creating asymmetric directional exposure.
- **Portfolio construction:** Convex mean-variance optimization (CVXPY) balancing expected momentum return against shrinkage-regularized covariance risk, subject to gross-leverage cap of 1.0.
- **Covariance estimation:** Rolling-window sample covariance with diagonal shrinkage toward the identity, following a simplified Ledoit-Wolf rationale.

The strategy is **not** a market-neutral momentum factor; it is a low-beta, conditionally directional strategy whose return depends on both momentum skill and residual crypto market exposure.

## Signal

### Formation timestamp
- Signals formed at each Friday close (weekly rebalance).
- Weights are shifted by one weekly observation before multiplication by realized returns (next-bar execution assumption).

### Lookback
- Trailing L-week simple return: `m(i,t) = P(i,t) / P(i,t-L) - 1`
- Locked value: L = 3 weeks (selected from training grid over 1–4 weeks).

### Long entry
- Assets in the upper cross-sectional quantile (locked: 0.75) with positive raw return become long candidates.

### Short entry
- Assets in the lower cross-sectional quantile (locked: 0.25) with negative raw return become short candidates.
- **Short positions are disabled when BTC daily close > BTC 200-day moving average** (bull regime overlay).

### Exit
- Weekly rebalance: positions are reconstructed each Friday. No intraday stop or take-profit; the portfolio is rebalanced to new optimizer-determined weights.
- If an asset drops out of the upper/lower quantile, its weight goes to zero.

### Holding period
- One week (Friday to Friday).

### Parameters (locked from training)
| Parameter | Search set | Locked value |
|---|---|---|
| Lookback L | 1, 2, 3, 4 weeks | 3 |
| Upper quantile | 0.55, 0.60, 0.65, 0.70, 0.75 | 0.75 |
| Risk aversion (gamma) | 2, 3, 4, 5, 6, 8, 10, 12 | 3 |
| Covariance window | 60, 90, 180, 252 days | 60 |
| Shrinkage intensity | 0.25, 0.40, 0.60 | 0.60 |
| Gross leverage cap | ≤ 1.0 | 1.0 |
| Dollar neutrality | Not imposed on primary | False |
| Bull overlay | BTC 200-day MA | Enabled |

### Position sizing
- Optimizer solves: `maximize μ'w - γ(w'Σw)` subject to gross-leverage ≤ 1.0, long candidates w[i] ≥ 0, short candidates w[i] ≤ 0, non-candidates w[i] = 0.
- μ is the vector of raw L-week trailing returns (not rank-demeaned-normalized).
- Σ is the annualized shrinkage covariance matrix.

### Underspecified items
- The exact number of grid-searched combinations and whether the quantile boundary optimum (0.75 = search maximum) implies the true optimum is higher is not established.
- Gamma is weakly identified (multiple values produce similar training Sharpe).
- Covariance window selected at boundary (60 days = minimum tested).

## Required data

- **Universe:** 12 large-cap USDT spot pairs: BTC, ETH, SOL, ADA, XRP, DOT, MATIC, LTC, DOGE, LINK, AVAX, ATOM.
- **Venue:** Binance Spot (public historical klines, no API key required).
- **Market type:** Spot only. No perpetual futures, no funding rates, no order-book data.
- **Timeframe:** Daily closes resampled to weekly (Friday closes).
- **Fields:** Close price, quote volume (for availability diagnostics only).
- **Training period:** 2020-01-01 to 2022-12-31.
- **Validation period:** 2023-01-01 to 2024-06-30.
- **Point-in-time:** Universe is defined ex post (assets known at end of research window), creating survivorship bias (see Limitations).

## Execution assumptions

- **Signal-to-order timing:** Weights formed at Friday close, applied to next week's return (one-week lag). Research-proposed assumption of next-bar execution.
- **Order type:** Market order assumed.
- **Fill model:** Perfect fill assumed; no partial fills, no slippage modeling, no order-book impact.
- **Fees:** 20 bps all-in per unit of turnover (primary); sensitivity tested at 7, 10, and 30 bps.
- **Spread:** Not modeled.
- **Slippage:** Not modeled.
- **Funding:** Not applicable (spot only).
- **Leverage/margin:** Not applicable (spot only); gross exposure capped at 1.0.
- **Borrow/shorting:** Not modeled. Short positions are weight-constrained by the optimizer but no borrow cost or availability constraint is imposed.
- **Latency:** Not modeled.
- **Partial fills/failures:** Not modeled.

## Evidence

### Source-reported

**Primary strategy (convex-optimized, non-dollar-neutral) holdout performance (2023-01-01 to 2024-06-30, net of 20 bps):**

| Metric | Value |
|---|---|
| Annualized arithmetic return | 22.09% |
| Annualized volatility | 16.60% |
| Sharpe ratio | 1.33 |
| Maximum drawdown | -7.0% |
| Average weekly turnover | 16.43% |
| Annualized alpha (vs BTC) | 12.0% |
| Alpha t-statistic | 0.91 (not significant at 5%) |
| BTC beta | 0.10 |
| BTC correlation | 0.33 |
| Net exposure | 0.10 |
| Gross exposure | 0.15 |

**Training period (2020-2022, net of 20 bps):**

| Metric | Value |
|---|---|
| Annualized arithmetic return | 32.29% |
| Annualized volatility | 15.86% |
| Sharpe ratio | 2.04 |
| Maximum drawdown | -6.6% |
| Average weekly turnover | 13.35% |
| Annualized alpha (vs BTC) | 30.0% |
| Alpha t-statistic | 3.32 |
| BTC beta | 0.04 |

**Benchmark comparison (holdout, net of 20 bps):**

| Model | Ann. return | Sharpe | Max DD | Turnover | BTC beta |
|---|---|---|---|---|---|
| Primary optimized | 22.09% | 1.33 | -7.0% | 16.43% | 0.10 |
| Equal-weight momentum | 44.92% | 0.66 | -50.0% | 95.30% | 0.66 |
| Dollar-neutral optimized | 0.18% | 0.06 | -4.0% | 3.73% | 0.00 |
| Dollar+beta-neutral | 0.18% | 0.06 | -4.0% | 3.73% | 0.00 |
| BTC buy-and-hold | 101.04% | 1.81 | -18.0% | 0.00% | 1.00 |

**Cost sensitivity (holdout):**

| Cost | Ann. return | Sharpe |
|---|---|---|
| 7 bps | 23.20% | 1.39 |
| 10 bps | 22.95% | 1.38 |
| 20 bps | 22.09% | 1.33 |
| 30 bps | 21.24% | 1.28 |

**Large-week dependence (holdout):**
- Excluding the best week reduces Sharpe to ~1.11; excluding the two best weeks reduces to ~0.87.
- Best week: Nov 10, 2023 (+16.24%), driven by SOL (+7.57 pp contribution).
- Worst week: Oct 6, 2023 (-3.25%).

**Key source-reported caveats:**
- Alpha is not statistically significant at conventional levels (t = 0.91).
- Dollar-neutral variants eliminate nearly all return, indicating the baseline is not a market-neutral factor.
- Bitcoin buy-and-hold has a higher Sharpe ratio (1.81) in the holdout.
- Performance is concentrated in a subset of the evaluation period (strong Nov 2023).
- The training Sharpe of 2.04 degrades to 1.33 in holdout, consistent with selection effects.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Dollar-neutral construction eliminates the effect (Sharpe drops from 1.33 to 0.06), indicating the return is primarily directional beta rather than pure cross-sectional momentum alpha.
- Holdout alpha t-statistic of 0.91 is not significant at 5%.
- Performance degrades materially when the best weeks are excluded.
- The strategy does not beat Bitcoin buy-and-hold on Sharpe in the holdout (1.33 vs 1.81).
- The quantile parameter (0.75) was selected at the boundary of the search grid, and covariance window (60 days) was also a boundary selection — both suggest the optimal values may lie outside the tested range.
- Gamma (risk aversion) is weakly identified — multiple values produce similar training Sharpe.

None identified in the reviewed sources beyond the above; absence is not evidence of no negative result.

## Falsification plan

1. **Walk-forward validation:** Repeat parameter selection through anchored or rolling walk-forward windows with a new untouched holdout. The current single-grid-point training optimization is insufficient.
2. **Point-in-time universe:** Reconstruct the eligible universe at each rebalance using historical listings, delistings, contemporaneous liquidity screens, and listing-age requirements to eliminate survivorship bias.
3. **Ablation — remove bull overlay:** Test the signal without the BTC 200-day MA regime filter to isolate the contribution of the directional tilt vs pure momentum.
4. **Ablation — rank-demeaned signal:** Compare raw trailing returns with rank-demeaned-normalized scores in the optimizer.
5. **Robust inference:** Use Newey-West or block-bootstrap standard errors instead of conventional OLS for alpha/beta inference.
6. **Broader benchmark:** Regress against BTC, ETH, and crypto factor mimics (size, momentum) instead of BTC alone.
7. **Cost stress:** Model funding rates, borrow availability, maker/taker fees, market-impact estimates, and capacity by coin.
8. **Failure threshold:** If walk-forward out-of-sample Sharpe < 0.5 after realistic costs, or if alpha t-statistic remains below 1.96, the hypothesis is materially weakened.
9. **Action on failure:** Discard or fundamentally redesign the signal/construction; do not retune on the same validation data.

## Crypto portability

**Adapted.**

The strategy is native to crypto spot markets (Binance USDT pairs), so the mechanism does not require porting from traditional assets. However, several crypto-specific considerations apply:

- **Spot vs perpetual:** The strategy uses spot data only. Porting to perpetual futures introduces funding rate exposure, mark/index price differences, and liquidation risk — none of which are modeled.
- **Funding:** Not applicable in spot; a perpetual-futures version would need to account for periodic funding payments that can erode or enhance carry.
- **24/7 session:** Weekly rebalance at Friday close uses a conventional calendar; crypto markets trade continuously, and Friday close may not align with optimal execution windows.
- **Venue fragmentation:** Binance-only data; cross-venue execution would face different prices, liquidity, and fees.
- **Liquidity:** The universe is restricted to 12 large-cap assets, limiting capacity and leaving smaller-cap momentum opportunities untested.
- **Survivorship:** The fixed universe excludes delisted or failed assets, overstating historical performance.

## Limitations

- **Survivorship bias:** Universe is defined ex post from 12 assets known at end of research window. Failed, delisted, or illiquid coins are absent. This is the most material limitation.
- **Short sample:** Training period is 3 years; holdout is 18 months. Single grid-search optimization creates selection risk.
- **Alpha not significant:** Holdout alpha t-statistic of 0.91 does not meet conventional significance thresholds.
- **Boundary parameter selection:** Both quantile (0.75 = max of grid) and covariance window (60 days = min of grid) are boundary optima, suggesting the true optimum may lie outside the tested range.
- **No execution realism:** 20 bps stylized cost; no slippage, spread, funding, borrow, impact, partial fills, or latency modeling.
- **Solver diagnostics omitted:** Counts of optimal, infeasible, and failed CVXPY solves are not reported.
- **Not independently reproduced:** Results are source-reported only.
- **Dollar-neutral fragility:** The effect disappears under dollar neutrality, indicating the baseline return is not a pure cross-sectional factor.
- **Concentrated returns:** Performance is materially dependent on a small number of strong weeks.

## Implementation status

Not implemented. No code has been run in our research stack. The source repository provides a complete Python implementation (`Convex_Opt_Final+Project.py`) that fetches public Binance historical data and runs the backtest locally.

## Adoption boundary

This is a research-only capture. Presence in this repository does not mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

The source itself is an educational research project and does not constitute investment advice.

## Related Wiki records

- `[[quant/binance-perpetual-cross-sectional-momentum-taker-cost-falsification-2026-09-13]]` — Related cross-sectional momentum falsification study on Binance perpetuals; finds momentum fails after taker costs. Different source, different methodology (full-history replication vs convex optimization), different findings. This record documents a momentum-via-optimization approach; the falsification record documents a momentum-fails-after-costs finding.
- `[[quant/crypto-cross-sectional-volatility-managed-momentum-2026-08-31]]` — Volatility-managed cross-sectional momentum in crypto (academic paper). Different mechanism (volatility scaling vs convex optimization + regime filter).
- `[[quant/strategy-research-record-spec-v1]]` — Schema specification.

## Sources

1. Aiden Fries, "Cross-Sectional Cryptocurrency Momentum: Convex Portfolio Optimization, Shrinkage Covariance, and Robustness Diagnostics", GitHub repository `afries24/crypto-cross-sectional-momentum`, branch `crypto-cross-sectional-momentum`, commit `ebf50df665f96880e60dcea0c429bab6aa42af3a`, dated July 26, 2026 (latest commit August 5, 2026). Source URL: https://github.com/afries24/crypto-cross-sectional-momentum
2. Aiden Fries, "Convex_Opt_Final+Project.py" (strategy implementation), same repository and commit as above. URL: https://github.com/afries24/crypto-cross-sectional-momentum/blob/crypto-cross-sectional-momentum/Convex_Opt_Final+Project.py
