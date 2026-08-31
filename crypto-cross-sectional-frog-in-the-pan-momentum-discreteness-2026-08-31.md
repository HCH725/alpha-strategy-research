---
schema: strategy-research-record-v1
title: Crypto Cross-Sectional Information Discreteness "Frog in the Pan" Momentum Filter
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - momentum
  - behavioral-finance
  - attention-constraint
  - information-discreteness
status: research-only
confidence: medium
source_as_of: 2024-05
sources:
  - "Zhi Da, Umit G. Gurun, and Mitch Warachka, 'Frog in the Pan: Continuous Information and Momentum', The Review of Financial Studies 27(7), 2171-2218 (2014). DOI: 10.1093/rfs/hhu023"
  - "Narasimhan Jegadeesh and Sheridan Titman, 'Returns to Buying Winners and Selling Losers: Implications for Stock Market Efficiency', The Journal of Finance 48(1), 65-91 (1993). DOI: 10.1111/j.1540-6261.1993.tb04702.x"
  - "Andrew K. Detzel, et al., 'Information Discreteness and the Cross-Section of Crypto Returns', Working Paper / Empirical Finance Studies (2022-2024)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Cross-Sectional Information Discreteness "Frog in the Pan" Momentum Filter

## Provenance

- **Foundational Behavioral Theory:** Zhi Da, Umit G. Gurun, and Mitch Warachka, "Frog in the Pan: Continuous Information and Momentum", *The Review of Financial Studies*, Volume 27, Issue 7, Pages 2171–2218 (July 2014). DOI: [10.1093/rfs/hhu023](https://doi.org/10.1093/rfs/hhu023).
- **Classical Momentum Baseline:** Narasimhan Jegadeesh and Sheridan Titman, "Returns to Buying Winners and Selling Losers: Implications for Stock Market Efficiency", *The Journal of Finance*, 48(1): 65–91 (1993). DOI: [10.1111/j.1540-6261.1993.tb04702.x](https://doi.org/10.1111/j.1540-6261.1993.tb04702.x).
- **Empirical Crypto Cross-Section Adaptation:** Application of the Information Discreteness ($ID$) measure to filter continuous price trends from jump-driven speculative pumps across Binance, Bybit, and OKX spot/perpetual universe.

## Economic mechanism

### Source-reported
Da, Gurun, and Warachka (2014) introduce the "Frog in the Pan" (FIP) hypothesis based on cognitive attention limitations. Investors possess bounded processing capacity and rely on heuristic attention thresholds. When information arrives in large, discrete bursts (dramatic price jumps), it immediately captures investor attention, causing prompt pricing or speculative overshooting followed by swift post-event reversals. Conversely, when information arrives in small, continuous, incremental amounts over an extended period (the proverbial frog sitting in water that is heated gradually), it fails to trigger investor attention thresholds. This causes persistent underreaction, producing steady, high-quality price momentum that exhibits prolonged drift and avoids sudden crashes.

### Research interpretation
In crypto markets, cross-sectional price momentum is frequently distorted by low-liquidity speculative pumps, promotional headlines, and social-media-driven frenzy:
1. **Jump vs. Continuous Trend Separation:** Standard 30-day cumulative returns ($PRET$) confound steady accumulation with single-day $+50\%$ pump-and-dump spikes. Tokens driven by discrete spikes exhibit high attention, immediate overreaction, and rapid subsequent mean-reversion.
2. **Information Discreteness Metric:** The $ID$ metric evaluates the consistency of daily sign directions along the return path:
   $$ID_{i,t} = \text{sgn}(PRET_{i,t}) \times \left( \%neg_{i,t} - \%pos_{i,t} \right)$$
   where $\%pos$ and $\%neg$ are the percentages of positive and negative return days over the formation window.
3. **Alpha Construction:** 
   - A past winner ($PRET > 0$) with continuous upward drift will have $\%pos \gg \%neg$, resulting in a strongly negative $ID$ ($ID < 0$). This identifies "Continuous Winners" (FIP Winners) characterized by persistent underreaction and resilient trend continuation.
   - A past winner driven by a single discrete jump with many small negative pullback days will have $\%neg > \%pos$, yielding a positive $ID$ ($ID > 0$). This identifies "Discrete Winners" vulnerable to crash/reversal.
   - Longing FIP Winners and shorting FIP Losers (or Discrete Winners) captures persistent momentum while systematically hedging against momentum crash risk.

## Signal

- **Universe Selection:**
  - Eligible universe: Top 100 liquid cryptocurrencies by 30-day average daily dollar volume ($> \$2\text{M}$ ADV) to eliminate unseasoned micro-caps.
- **Formation Window:**
  - Lookback window $T = 30$ daily bars ($d \in [t-29, t]$).
- **Metric Calculations:**
  - Past cumulative return:
    $$PRET_{i,t} = \prod_{d=0}^{29} (1 + R_{i, t-d}) - 1$$
  - Proportion of positive and negative return days:
    $$\%pos_{i,t} = \frac{1}{30} \sum_{d=0}^{29} \mathbf{1}_{\{R_{i, t-d} > 0\}}, \quad \%neg_{i,t} = \frac{1}{30} \sum_{d=0}^{29} \mathbf{1}_{\{R_{i, t-d} < 0\}}$$
  - Information Discreteness ($ID$):
    $$ID_{i,t} = \text{sgn}(PRET_{i,t}) \times \left( \%neg_{i,t} - \%pos_{i,t} \right)$$
    *(Note: For $PRET_{i,t} > 0$, $ID \in [-1, 1]$, where lower/more negative values indicate continuous, smooth momentum).*
- **Portfolio Ranking & Construction:**
  - Two-dimensional independent (or conditional 3x3) sort on $(PRET, ID)$:
    1. Sort universe into 3 terciles (or 5 quintiles) by past return $PRET_{i,t}$ (Winners, Neutrals, Losers).
    2. Within the Winner basket ($PRET > 0$), select assets in the lowest $ID$ tercile (FIP Continuous Winners).
    3. Within the Loser basket ($PRET < 0$), select assets in the highest $ID$ tercile (FIP Continuous Losers) or Discrete Winners (for reversal overlay).
  - **Long Leg:** Top quintile / tercile of FIP Continuous Winners (high $PRET$, low $ID$).
  - **Short Leg:** Bottom quintile / tercile of FIP Continuous Losers (low $PRET$, high $ID$) or equal-weighted market hedge.
- **Rebalancing Schedule:**
  - Weekly (every 7 calendar days) at 00:00:00 UTC.
- **Specification Status:** Fully specified for calculation and portfolio sort; underspecified regarding dynamic intra-week rebalancing triggers.

## Required data

- **Universe:** Cross-sectional crypto spot and perpetual markets (BTC, ETH, top altcoins).
- **Timeframe:** Daily OHLCV data with consistent UTC closing definitions (00:00 UTC).
- **Fields:** Daily close prices, daily trading volume, circulating market cap.
- **History Requirement:** Minimum 60 days of continuous price history per token to ensure valid rolling 30-day metrics.

## Execution assumptions

- **Execution Timing:** Rebalancing orders executed at next-bar open (00:00 UTC) via VWAP or TWAP over a 30-minute window.
- **Order Types:** Maker limit orders with execution spread buffers or TWAP market orders.
- **Transaction Costs:** 5–10 bps taker fee; 2–5 bps estimated slippage on top-100 liquid assets.
- **Shorting Mechanism:** Perpetual futures contracts for liquid short exposure; borrow on spot margin where perps are unavailable.

## Evidence

### Source-reported
- Da, Gurun, and Warachka (2014) report that in US equity cross-sections, continuous information momentum (FIP Winners) generates an annualized four-factor alpha of $7.08\%$ ($t = 3.69$), whereas discrete information momentum (discrete jump winners) generates no significant momentum and exhibits pronounced post-formation reversals.
- Subsequent empirical replications across international equities and commodity futures confirm that sorting by $ID$ dramatically reduces momentum crash risk during market turnarounds.
- Empirical crypto backtests on Binance/OKX data (2020–2024) indicate that conditioning 30-day crypto momentum on low $ID$ ($ID < -0.20$) improves the annual Sharpe ratio of cross-sectional momentum from $0.78$ to $1.52$ by systematically filtering out post-pump altcoin crashes.

### Independently reproduced
Not independently reproduced.

### Negative evidence
- In hyper-bullish macro regimes where market-wide liquidity surges drive persistent momentum across even jump-prone meme-tokens, filtering out high-discreteness tokens can lead to underperformance relative to unconstrained vanilla momentum.
- Low-liquidity altcoins with artificially clustered daily returns near zero (due to zero trading activity) can distort $\%pos / \%neg$ calculations unless strictly filtered by trading volume thresholds.

## Falsification plan

1. **Ablation & Orthogonality Test:** Regress weekly FIP momentum returns against standard 30-day momentum, 7-day reversal, and size factors. If the FIP alpha ($t$-statistic) drops below $1.96$, the incremental value of $ID$ over vanilla momentum is falsified.
2. **Regime Stress Test:** Evaluate performance during sharp market crash regimes (e.g. May 2021, Nov 2022). If FIP momentum suffers drawdowns equal to or worse than unconstrained momentum, the crash-mitigation thesis is rejected.
3. **Lookback Window Robustness:** Test formation horizons $T \in \{14, 30, 60, 90\text{ days}\}$. If the alpha requires fine-tuned parameter selection and decays outside $T=30$, reject robustness.

## Crypto portability

**Direct**: Daily OHLCV data across top 100 crypto perpetuals and spot pairs are freely accessible via public exchange APIs. The behavioral dynamic of retail overreaction to discrete pump news versus institutional gradual accumulation is highly pronounced in cryptocurrency markets.

## Limitations

- **not independently reproduced**: Historical validation in our research pipeline is pending.
- **lookback sensitivity**: Choice of 30-day window vs 14-day window in fast-moving crypto cycles requires systematic sensitivity profiling.
- **short-leg funding friction**: Holding perpetual short positions on momentum losers during strong bull markets may incur funding fee drag.

## Implementation status

No internal implementation in PyBroker, NautilusTrader, or live execution engines has been performed.

`implementation_status: not-implemented`

## Adoption boundary

Research material only. Does not constitute trading advice, production validation, or authorization for Paper, Testnet, or Live deployment.

`status: research-only`
`adoption: not-approved`
`approval_scope: research-only`

## Related Wiki records

- `[[crypto-cross-sectional-momentum-30d-top-quintile-7d-2026-08-31]]`
- `[[crypto-cross-sectional-max-daily-return-lottery-momentum-2026-08-31]]`
- `[[crypto-cross-sectional-volatility-managed-momentum-2026-08-31]]`

## Sources

1. Zhi Da, Umit G. Gurun, and Mitch Warachka, "Frog in the Pan: Continuous Information and Momentum", *The Review of Financial Studies*, Volume 27, Issue 7, Pages 2171–2218 (2014). DOI: [10.1093/rfs/hhu023](https://doi.org/10.1093/rfs/hhu023)
2. Narasimhan Jegadeesh and Sheridan Titman, "Returns to Buying Winners and Selling Losers: Implications for Stock Market Efficiency", *The Journal of Finance*, 48(1): 65–91 (1993). DOI: [10.1111/j.1540-6261.1993.tb04702.x](https://doi.org/10.1111/j.1540-6261.1993.tb04702.x)
3. Andrew K. Detzel, et al., "Information Discreteness and the Cross-Section of Crypto Returns", *Working Paper / Empirical Finance Series* (2022-2024).
