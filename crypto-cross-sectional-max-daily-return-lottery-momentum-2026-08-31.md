---
schema: strategy-research-record-v1
title: Crypto Cross-Sectional Maximum Daily Return Lottery Momentum
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
  - lottery-preference
  - max-effect
status: research-only
confidence: medium
source_as_of: 2021-09
sources:
  - https://doi.org/10.1186/s40854-021-00291-9
  - https://ideas.repec.org/a/spr/fininn/v7y2021i1d10.1186_s40854-021-00291-9.html
  - https://doi.org/10.1016/j.jfineco.2010.08.014
  - https://doi.org/10.1016/j.frl.2020.101536
  - https://doi.org/10.1016/j.jintfinmac.2021.101289
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Cross-Sectional Maximum Daily Return Lottery Momentum

## Provenance

Primary source: Melisa Ozdamar, Levent Akdeniz, and Ahmet Sensoy, “Lottery-like preferences and the MAX effect in the cryptocurrency market,” *Financial Innovation* 7, article 74 (2021). DOI: https://doi.org/10.1186/s40854-021-00291-9. Stable bibliographic record: https://ideas.repec.org/a/spr/fininn/v7y2021i1d10.1186_s40854-021-00291-9.html.

The primary study analyzes daily prices and market capitalization data from CoinMarketCap for cryptocurrencies spanning January 2014 to September 2020. The sample filters for coins with market capitalization above $5 million and excludes the first six months of trading history to mitigate initial illiquidity and listing anomalies, yielding an eligible sample expanding from 17 cryptocurrencies in 2014 to 523 cryptocurrencies by September 2020 (973 unique coins in total).

Foundational equity benchmark: Turan G. Bali, Nusret Cakici, and Robert F. Whitelaw, “Maxing out: stocks as lotteries and the cross-section of expected returns,” *Journal of Financial Economics* 99(2), 427–446 (2011). DOI: https://doi.org/10.1016/j.jfineco.2010.08.014.

Contrasting and supporting cryptocurrency literature:
- Yiyang Li, Andrew Urquhart, Pengfei Wang, and Weiqiang Zhang, “MAX momentum in cryptocurrency markets,” *SSRN Electronic Journal* (2020), corroborating persistent positive return predictability of extreme positive returns in cryptocurrency markets.
- Yuan Jia, Ya-nan Liu, and Shipeng Yan, “Higher moments, extreme returns, and cross-section of cryptocurrency returns,” *Finance Research Letters* 36 (2020), article 101536. DOI: https://doi.org/10.1016/j.frl.2020.101536.
- Klaus Grobys and Jukka Junttila, “Speculation and lottery-like demand in cryptocurrency markets,” *Journal of International Financial Markets, Institutions and Money* 71 (2021), article 101289. DOI: https://doi.org/10.1016/j.jintfinmac.2021.101289.

## Economic mechanism

### Source-reported

In traditional equities (Bali et al., 2011), investors exhibit lottery-like preferences by overpaying for stocks with high historical maximum daily returns ($\text{MAX}$). This preference induces overpricing and subsequent negative expected returns (a negative cross-sectional anomaly / mean reversion).

Ozdamar, Akdeniz, and Sensoy (2021) report the opposite empirical relationship in cryptocurrency markets: cryptocurrencies with high past maximum daily returns significantly outperform cryptocurrencies with low maximum daily returns over subsequent weekly intervals. The authors attribute this to persistent speculative demand, attention-driven retail chasing, and strong momentum characteristics specific to cryptocurrency assets, where extreme upward price shocks attract ongoing speculative participation rather than rapid mean reversion.

### Research interpretation

The falsifiable mechanism is attention-induced momentum persistence in speculative assets without fundamental anchor pricing. When a cryptocurrency experiences an extreme positive daily return within a rolling 28-day window:
1. Social sentiment, media visibility, and speculative retail attention spike.
2. Given structural limits to shorting and the absence of cash-flow valuation bounds, subsequent order flow continues in the direction of the extreme mover over multi-week holding horizons.
3. This creates a positive cross-sectional spread between high-MAX and low-MAX deciles that persists across weekly rebalancings.

Crucially, the sign of this anomaly in crypto (+MAX momentum) directly contradicts the classical equity sign (−MAX lottery reversal). Research must explicitly test whether this positive spread is an independent premium or a manifestation of short/medium-term price momentum and size/liquidity concentration.

## Signal

The normalized signal follows the portfolio-sort specification of Ozdamar et al. (2021):

1. **Formation interval and cadence**: At each weekly rebalancing timestamp $t$, compute metrics using the preceding $D_m = 28$ trading days (4 calendar weeks, assuming 7 trading days per week in 24/7 crypto markets).
2. **Primary signal ($\text{MAX}$)**:
   $$\text{MAX}_{i,t} = \max_{d \in [1, D_m]} (R_{i,d})$$
   where $R_{i,d}$ is the daily close-to-close return of cryptocurrency $i$ on day $d$.
3. **Multi-day average variant ($\text{MAX}(N)$)**:
   $$\text{MAX}(N)_{i,t} = \frac{1}{N} \sum_{k=1}^{N} R_{i,(k)}$$
   where $R_{i,(k)}$ represents the $k$-th highest daily return of coin $i$ over the 28-day window ($N \in \{2, 3, 4, 5\}$).
4. **Universe filter**:
   - Market capitalization $> \$5\text{M}$ as of week $t-1$.
   - Minimum 6 months of historical trading data since market listing.
5. **Portfolio ranking**:
   - Sort eligible universe into deciles (D1 lowest MAX to D10 highest MAX) or quintiles.
   - Long leg: Decile 10 (highest MAX).
   - Short / benchmark comparison leg: Decile 1 (lowest MAX).
6. **Holding period**: 1 week (7 trading days), rebalanced weekly.

Signal status: **fully specified** for decile sorting and holding window, but **underspecified** regarding intra-week execution timing (e.g. Sunday midnight UTC vs Monday 00:00 UTC) and weighting convention (value-weighted vs equal-weighted specifications both explored in source).

## Required data

- Point-in-time cross-sectional universe of cryptocurrencies.
- Daily OHLCV data (to compute daily returns, Garman-Klass volatility, and Amihud illiquidity).
- Point-in-time circulating supply and market capitalization (for $\$5\text{M}$ eligibility filter and value-weighting).
- Accurate listing and delisting dates to enforce the 6-month seasoning filter and prevent survivorship bias.
- Explicit UTC timestamp convention (e.g. 00:00:00 UTC daily close).
- Trading volume in quote currency (USD / USDT) for liquidity controls.

## Execution assumptions

- Signal formation uses daily closes through day $t$.
- Orders are submitted at the opening of the next weekly interval (next-bar open) to ensure zero lookahead bias.
- Taker vs maker assumptions: Original study assumes instantaneous frictionless execution. In reality, rebalancing across 50–500 altcoins incurs exchange taker fees (e.g. 5–10 bps) and bid-ask spread costs.
- Shorting feasibility: Shorting the D1 basket is often restricted or borrow-cost prohibitive for small-cap altcoins. The strategy is primarily deployable as a long-only top-decile selection / tilt model or as a long-altcoin vs short-BTC/ETH market-hedged portfolio.
- Slippage and capacity: High-MAX altcoins may exhibit elevated volatility and wider spreads, making capacity and market impact critical evaluation criteria.

## Evidence

### Source-reported

Ozdamar, Akdeniz, and Sensoy (2021) report:
- **Univariate decile portfolios**: Value-weighted weekly raw return difference between Decile 10 (high MAX) and Decile 1 (low MAX) equals **+3.03% per week** ($t$-statistic = 4.10, Newey-West adjusted).
- **Risk-adjusted spread**: Three-factor alpha difference equals **+1.99% per week** ($t$-statistic = 3.72).
- **Robustness across MAX(N)**: Significant positive spreads persist using average of $N=2, 3, 4, 5$ highest returns ($t$-stats $> 3.5$).
- **Fama-MacBeth cross-sectional regressions**: Positive and statistically significant MAX coefficient ($\gamma_{\text{MAX}} > 0$) after controlling for:
  - Size ($\ln(\text{MarketCap})$);
  - Price ($\ln(1 + \text{Price})$);
  - Intermediate momentum ($\text{MOM}$, cumulative return week $t-4$ to $t-2$);
  - Short-term reversal ($\text{REV}$, cumulative return in week $t-1$);
  - Amihud illiquidity ($\text{ILLIQ}$);
  - Volatility ($\text{VOL}$, Garman-Klass range-based volatility and idiosyncratic volatility $\text{IVOL}$);
  - Skewness (Total skewness $\text{TSKEW}$ and idiosyncratic skewness $\text{ISKEW}$);
  - Market sentiment regimes (StockTwits / Augmento Bitcoin sentiment index splits).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Conflicting literature on small unseasoned samples**: Jia et al. (2020) and Grobys & Junttila (2021) examine smaller cryptocurrency samples (20–84 coins) without strict market-cap/seasoning thresholds and find negative or insignificant relationships between extreme returns and future performance. This indicates that the MAX effect may suffer from severe pump-and-dump reversal in micro-cap unseasoned tokens.
- **Transaction cost erosion**: Weekly turnover in decile portfolios with high-volatility assets can generate significant transaction fee drag, potentially consuming the reported alpha spread.
- **Contradiction with traditional asset pricing**: In equities, commodities, and FX, MAX anomalies are predominantly negative; relying on a positive sign in crypto requires strong belief in persistent retail speculative momentum.

## Falsification plan

The hypothesis should be considered falsified or economically unviable if, in an out-of-sample modern test (October 2020 to August 2026):
1. The long-short Decile 10 minus Decile 1 weekly return spread is statistically indistinguishable from zero or negative under Newey-West standard errors ($t < 1.96$).
2. The alpha of the D10 portfolio vanishes after accounting for standard multi-factor benchmarks (Crypto Market, Size, 30-day Momentum).
3. Net returns become negative after applying realistic trading fees (5 bps maker / 10 bps taker) and empirical bid-ask spread models.
4. The effect disappears when excluding the top 1% most extreme micro-cap outliers, indicating the result was an artifact of data errors or unexecutable thin listings.
5. In an ablation test, standard 30-day cumulative momentum subsumes the predictive power of MAX in multivariate Fama-MacBeth regressions.

## Crypto portability

**Direct**, as the primary study is conducted entirely on cryptocurrency spot market assets.

Portability adaptations to perpetual futures:
- Perpetual universe is naturally liquid and filtered, which aligns with the need to avoid illiquid pump-and-dump noise.
- Perpetual funding rates must be factored in: high-MAX tokens often command high positive funding rates (longs pay shorts), which could penalize the long leg.

## Limitations

- **not independently reproduced**: requires full out-of-sample replication on post-2020 data.
- **underspecified execution**: exact execution hour, order type, and dynamic slippage model are omitted from academic source.
- **short-leg infeasibility**: unborrowable spot altcoins prevent pure delta-neutral execution.
- **funding rate drag**: on perpetuals, holding high-MAX runaway tokens may incur high funding fee burdens.
- **sample sensitivity**: positive sign depends heavily on market-cap filtering ($\ge \$5\text{M}$) and seasoning ($\ge 6\text{ months}$).

## Implementation status

No implementation in PyBroker, NautilusTrader, or any internal research/backtesting pipeline has been performed.

`implementation_status: not-implemented`

## Adoption boundary

This record is research material only. It does not represent a validated production strategy, an execution authorization, or approval for Paper, Testnet, or Live trading.

`status: research-only`

`adoption: not-approved`

`approval_scope: research-only`

## Related Wiki records

- `[[crypto-cross-sectional-momentum-30d-top-quintile-7d-2026-08-31]]`
- `[[crypto-cross-sectional-last-day-return-reversal-liquidity-conditioned-2026-08-31]]`

## Sources

1. Melisa Ozdamar, Levent Akdeniz, and Ahmet Sensoy, “Lottery-like preferences and the MAX effect in the cryptocurrency market,” *Financial Innovation* 7(1), 74 (2021). DOI: https://doi.org/10.1186/s40854-021-00291-9
2. RePEc/IDEAS bibliographic entry: https://ideas.repec.org/a/spr/fininn/v7y2021i1d10.1186_s40854-021-00291-9.html
3. Turan G. Bali, Nusret Cakici, and Robert F. Whitelaw, “Maxing out: stocks as lotteries and the cross-section of expected returns,” *Journal of Financial Economics* 99(2), 427–446 (2011). DOI: https://doi.org/10.1016/j.jfineco.2010.08.014
4. Yuan Jia, Ya-nan Liu, and Shipeng Yan, “Higher moments, extreme returns, and cross-section of cryptocurrency returns,” *Finance Research Letters* 36, 101536 (2020). DOI: https://doi.org/10.1016/j.frl.2020.101536
5. Klaus Grobys and Jukka Junttila, “Speculation and lottery-like demand in cryptocurrency markets,” *Journal of International Financial Markets, Institutions and Money* 71, 101289 (2021). DOI: https://doi.org/10.1016/j.jintfinmac.2021.101289
