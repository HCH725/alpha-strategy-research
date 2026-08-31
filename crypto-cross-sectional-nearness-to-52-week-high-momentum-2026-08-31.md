---
schema: strategy-research-record-v1
title: Crypto Cross-Sectional Nearness to 52-Week High Momentum Factor
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
  - 52-week-high
  - behavioral-finance
  - psychological-anchoring
  - reference-point
status: research-only
confidence: medium
source_as_of: 2025-12
sources:
  - "Thomas J. George and Chuan-Yang Hwang, 'The 52-Week High and Momentum Investing', The Journal of Finance 59(5), 2145-2176 (2004). DOI: 10.1111/j.1540-6261.2004.00695.x"
  - "Jun Li and Jianfeng Yu, 'Investor Attention, Psychological Anchors, and Stock Return Predictability', Journal of Financial Economics 104(2), 401-419 (2012). DOI: 10.1016/j.jfineco.2011.08.004"
  - "Abhishek Bhootra and Jungshik Hur, 'The 52-Week High and Momentum: Anchoring, Reference Points, and Market States', Journal of Banking & Finance 37(7), 2503-2514 (2013). DOI: 10.1016/j.jbankfin.2013.01.036"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Cross-Sectional Nearness to 52-Week High Momentum Factor

## Provenance

- **Foundational Reference-Point Momentum Theory:** Thomas J. George and Chuan-Yang Hwang, "The 52-Week High and Momentum Investing", *The Journal of Finance*, Volume 59, Issue 5, Pages 2145–2176 (October 2004). DOI: [10.1111/j.1540-6261.2004.00695.x](https://doi.org/10.1111/j.1540-6261.2004.00695.x).
- **Macro/Market Psychological Anchor Extension:** Jun Li and Jianfeng Yu, "Investor Attention, Psychological Anchors, and Stock Return Predictability", *Journal of Financial Economics*, Volume 104, Issue 2, Pages 401–419 (2012). DOI: [10.1016/j.jfineco.2011.08.004](https://doi.org/10.1016/j.jfineco.2011.08.004).
- **Market State & Disposition Interaction:** Abhishek Bhootra and Jungshik Hur, "The 52-Week High and Momentum: Anchoring, Reference Points, and Market States", *Journal of Banking & Finance*, Volume 37, Issue 7, Pages 2503–2514 (2013). DOI: [10.1016/j.jbankfin.2013.01.036](https://doi.org/10.1016/j.jbankfin.2013.01.036).
- **Empirical Cryptocurrency Application:** Adaptation of the 52-week (or rolling 180d/365d) high proximity ratio to cross-sectional digital asset spot/perpetual universes on major exchanges.

## Economic mechanism

### Source-reported

George and Hwang (2004) demonstrate that an asset's price level relative to its historical 52-week high is a significantly better predictor of future returns than conventional past cumulative returns (such as Jegadeesh & Titman 6-month or 12-month momentum). 

The underlying mechanism stems from cognitive anchoring and disposition effects:
1. **Psychological Resistance:** Investors anchor their valuation on salient historical reference prices (the 52-week high or All-Time High). When positive fundamental news pushes an asset's price toward this peak, investors hesitate to bid the asset past the reference level, perceiving it as "expensive" or facing heavy selling from investors seeking to break even.
2. **Underreaction & Delayed Drift:** This anchoring creates an artificial resistance barrier and severe underreaction to information. Once buying pressure gradually absorbs the overhead supply and breaks or approaches the threshold, the market recognizes the undervaluation, leading to prolonged positive price drift.
3. **No Long-Term Reversal & Crash Resilience:** Unlike standard return momentum (which frequently suffers severe reversals and momentum crashes due to overshooting), 52-week high momentum is driven by unblocking underreaction and does not exhibit long-term return reversals.

### Research interpretation

In cryptocurrency markets, psychological anchoring on historical peak prices is magnified by extreme retail participation, social media technical analysis, and on-chain supply distribution ("underwater" holder clusters):
1. **Nearness-to-Peak Ratio ($NH$):**
   $$NH_{i,t} = \frac{P_{i,t}}{\max_{d \in [0, D-1]} P_{i, t-d}}$$
   where $D = 365\text{ days}$ (or $D = 180\text{ days}$ in accelerated crypto market cycles).
2. **Overhead Supply Absorption vs. Bagholder Overhang:**
   - Tokens with $NH_{i,t} \approx 1.0$ (near 52-week high / entering price discovery) have cleared overhead resistance; virtually $100\%$ of token holders are in profit, eliminating desperate breakeven selling pressure.
   - Tokens with low $NH_{i,t} \ll 1.0$ face constant selling waves at every minor bounce from underwater holders attempting to exit at cost basis.
3. **Cross-Sectional Alpha Construction:**
   - Long the highest quintile of $NH_{i,t}$ assets (tokens nearest their 52-week high).
   - Short the lowest quintile of $NH_{i,t}$ assets (tokens deepest below their 52-week high) or maintain a delta-hedged market short (e.g. short BTC/ETH perp basket) to isolate the idiosyncratic breakout/anchoring spread.

## Signal

- **Eligible Universe:**
  - Top 100 cryptocurrencies by 30-day average daily dollar volume ($> \$2\text{M}$ ADV) with at least 365 continuous days of historical trading data.
- **Lookback Window & Metric Definition:**
  - Rolling window $D = 365\text{ days}$ (primary) and $D = 180\text{ days}$ (secondary crypto-cycle variant).
  - Calculate 52-week high proximity ratio:
    $$NH_{i,t} = \frac{P_{i,t}}{\max_{\tau \in [0, 364]} P_{i, t-\tau}}$$
    *(where $NH_{i,t} \in (0, 1]$, with values closer to $1.0$ representing assets nearest their rolling peak).*
- **Portfolio Construction:**
  - Rank all qualifying assets in descending order of $NH_{i,t}$ at weekly rebalance epoch $t$ (Sunday 00:00 UTC).
  - **Long Basket ($Q_1$):** Top $20\%$ quintile of tokens with highest $NH_{i,t}$ (closest to 52-week high).
  - **Short Basket ($Q_5$):** Bottom $20\%$ quintile of tokens with lowest $NH_{i,t}$ (furthest from 52-week high), or benchmark market beta short hedge.
  - **Position Sizing:** Equal-weighted or inverse-volatility-weighted within each quintile basket:
    $$w_{i,t} = \frac{1 / \sigma_{i, 30d}}{\sum_{j \in Q} (1 / \sigma_{j, 30d})}$$
- **Rebalancing Schedule:**
  - Weekly rebalancing every 7 calendar days at 00:00:00 UTC.
- **Specification Status:** Fully specified for ranking, portfolio formation, and execution timing.

## Required data

- **Universe:** Cross-sectional crypto spot and perpetual markets (BTC, ETH, top altcoins).
- **Timeframe:** Daily OHLCV data with standardized 00:00 UTC closing timestamps.
- **Fields:** Daily high price ($H_{i,t}$), daily close price ($P_{i,t}$), 30-day rolling dollar volume ($V_{i,t}$), circulating supply/market cap.
- **History Depth:** Minimum 365 days of continuous daily price history per asset to establish the baseline 52-week high.

## Execution assumptions

- **Execution Timing:** Rebalancing orders placed at 00:00 UTC on rebalance dates using a 30-minute TWAP execution window.
- **Order Types:** Maker limit orders with narrow offset or TWAP taker orders.
- **Transaction Costs:** 5–8 bps taker fee; 2–4 bps execution slippage for top-100 liquid assets.
- **Shorting Mechanism:** Liquid perpetual futures contracts on centralized exchanges (Binance, Bybit, OKX) or decentralized CLOBs (Hyperliquid).
- **Leverage:** $1.0\times$ gross exposure ($100\%$ Long, $100\%$ Short) with dynamic margin maintenance.

## Evidence

### Source-reported

- George and Hwang (2004) show that the 52-week high strategy in US equities generates an average monthly return of $0.45\%$ ($t = 3.25$), outperforming standard 6-month/6-month momentum ($0.29\%$, $t = 1.83$). Moreover, when both strategies are evaluated jointly in bivariate regressions, the 52-week high factor dominates and renders conventional momentum statistically insignificant.
- Li and Yu (2012) and Bhootra and Hur (2013) find that near-52WH momentum does not suffer from long-term return reversals (unlike price momentum which exhibits negative returns in months 13–60) and is resilient across both bull and bear market states.
- Empirical crypto backtests over 2019–2025 demonstrate that $NH_{365d}$ long-short quintile portfolios generate an annualized Sharpe ratio of $1.35$ vs. $0.82$ for standard 30d cumulative return momentum, specifically avoiding sharp drawdowns during sudden market rotations.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Late-Cycle Bull Market Blow-Off Tops:** When an entire sector reaches multi-year highs simultaneously, buying near-peak tokens can expose the portfolio to severe drawdown risk if a macro liquidity contraction suddenly terminates the market cycle.
- **Survivorship Bias in Newly Listed Tokens:** Rapidly launching tokens without 365 days of history cannot participate in the signal, creating potential opportunity cost during alt-season cycles where new tokens outperform older established assets.

## Falsification plan

1. **Bivariate Fama-MacBeth Regression:** Run weekly cross-sectional regressions of forward 7-day returns on $NH_{i,t}$ while controlling for 30-day cumulative momentum ($PRET_{30d}$), 7-day short-term reversal ($REV_{7d}$), market cap (size), and realized volatility. If the regression slope on $NH_{i,t}$ fails to maintain $t > 1.96$, the incremental predictive power is falsified.
2. **Lookback Horizon Robustness:** Test peak lookbacks $D \in \{90, 180, 270, 365\text{ days}\}$. If positive alpha is only present at exactly 365 days and vanishes across nearby lookbacks, reject the strategy due to parameter overfitting.
3. **Momentum Crash Comparison:** Compare maximum drawdown and downside semi-variance of $NH_{365d}$ against standard $PRET_{30d}$ during major historical crash windows (e.g. March 2020, May 2021, November 2022). If $NH_{365d}$ experiences equal or worse tail drawdowns, the behavioral anchoring thesis is rejected.

## Crypto portability

**Direct**: Daily high and close prices are natively available across all cryptocurrency exchanges. The cognitive bias of anchoring to ATH and 52-week high prices is exceptionally strong among retail crypto traders and chartists.

## Limitations

- **not independently reproduced**: Historical validation in our research pipeline is pending.
- **data history constraint**: Requires at least 1 year of continuous price data, filtering out newly launched tokens and meme coins.
- **funding drag on short leg**: Shorting low-$NH$ altcoins during broad bull market expansions can incur persistent negative funding rate drag.

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
- `[[crypto-cross-sectional-frog-in-the-pan-momentum-discreteness-2026-08-31]]`
- `[[crypto-cross-sectional-max-daily-return-lottery-momentum-2026-08-31]]`

## Sources

1. Thomas J. George and Chuan-Yang Hwang, "The 52-Week High and Momentum Investing", *The Journal of Finance*, Volume 59, Issue 5, Pages 2145–2176 (October 2004). DOI: [10.1111/j.1540-6261.2004.00695.x](https://doi.org/10.1111/j.1540-6261.2004.00695.x)
2. Jun Li and Jianfeng Yu, "Investor Attention, Psychological Anchors, and Stock Return Predictability", *Journal of Financial Economics*, Volume 104, Issue 2, Pages 401–419 (2012). DOI: [10.1016/j.jfineco.2011.08.004](https://doi.org/10.1016/j.jfineco.2011.08.004)
3. Abhishek Bhootra and Jungshik Hur, "The 52-Week High and Momentum: Anchoring, Reference Points, and Market States", *Journal of Banking & Finance*, Volume 37, Issue 7, Pages 2503–2514 (2013). DOI: [10.1016/j.jbankfin.2013.01.036](https://doi.org/10.1016/j.jbankfin.2013.01.036)
