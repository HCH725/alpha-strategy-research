---
schema: strategy-research-record-v1
title: LLM-Detected Crypto Influencer Twitter Trading Signal with 6-Hour Granger-Led Price Predictability
created: 2026-09-07
updated: 2026-09-07
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - sentiment
  - social-media
  - granger-causality
  - LLM-signal
status: research-only
confidence: low
source_as_of: 2026-09-07
sources:
  - "Meysam Alizadeh, Yasaman Asgari, Zeynab Samei, Sara Yari, Shirin Dehghani, Mael Kubli, Darya Zare, Juan Diego Bermeo, Veronika Batzdorfer, and Fabrizio Gilardi, 'Exploring Relationships Between Cryptocurrency News Outlets and Influencers' Twitter Activity and Market Prices', arXiv:2411.05577v1 [cs.SI], November 8, 2024. https://arxiv.org/abs/2411.05577"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# LLM-Detected Crypto Influencer Twitter Trading Signal with 6-Hour Granger-Led Price Predictability

## Provenance

- **Primary source:** Meysam Alizadeh, Yasaman Asgari, Zeynab Samei, Sara Yari, Shirin Dehghani, Mael Kubli, Darya Zare, Juan Diego Bermeo, Veronika Batzdorfer, and Fabrizio Gilardi. "Exploring Relationships Between Cryptocurrency News Outlets and Influencers' Twitter Activity and Market Prices." arXiv preprint `arXiv:2411.05577v1 [cs.SI]`, submitted November 8, 2024. DOI: [10.48550/arXiv.2411.05577](https://doi.org/10.48550/arXiv.2411.05577).
- **Stable URL:** https://arxiv.org/abs/2411.05577
- **Affiliations:** Digital Democracy Lab, University of Zurich; Digital Society Initiative, University of Zurich; IPM, Tehran; Allameh Tabataba'i University, Tehran; Karlsruhe Institute of Technology.
- **Sample period:** Twitter data collected June 10, 2023 to February 28, 2024; cryptocurrency prices October 2023 to March 2024.
- **Universe:** 9 major cryptocurrencies by market cap: BTC, ETH, XRP, SOL, DOGE, BNB, ADA, DOT, SHIB.
- **Data source:** Twitter Academic API + manual influencer collection; CoinMarketCap for prices.
- **Corpus:** 470,658 English tweets from 2,687 identified crypto influencers and 74 financial news outlets.

## Economic mechanism

### Source-reported

The authors hypothesize that crypto influencers and news outlets on Twitter produce information that is not immediately incorporated into cryptocurrency prices. Influencers act as information intermediaries: their buy/not-buy trading signals, when aggregated over a 24-hour rolling window, should contain predictive content about future price movements. The mechanism is behavioral: retail investors follow influencer recommendations with a lag, creating a delayed demand shock that manifests in prices over subsequent hours.

### Research interpretation

This is a **social information diffusion hypothesis**: aggregated LLM-detected directional trading signals from a curated network of crypto influencers granger-cause short-horizon price movements in major cryptocurrencies. The hypothesized alpha mechanism is:

- **Information channel:** Influencers (PageRank/Betweenness/Closeness-dominant Twitter users in the crypto retweet network) post buy/not-buy signals that propagate to retail followers with a delay.
- **Signal aggregation:** The 24-hour rolling sum of buy vs. not-buy signals, processed through CryptoBERT, produces a social sentiment score SS_i(t) that contains incremental information.
- **Market inefficiency:** The information is not instantly priced in, creating a 6-hour+ window for informed trading.

This is distinct from generic sentiment analysis (which uses VADER/FinBERT on raw sentiment) in that the signal is specifically a **trading directional signal** (buy vs. not-buy) extracted from identified influencers, not a general mood metric.

## Signal

### Formation timestamp

- Social signal computed at each hourly timestamp t using the preceding 24-hour window of influencer/news tweets.
- Price data at hourly frequency from CoinMarketCap.
- No specific timezone stated for tweet timestamps (Twitter API default assumed UTC).

### Lookback

- 24-hour rolling window for signal aggregation.
- No warm-up period specified.

### Signal formula (source-reported)

The social signal for cryptocurrency i at time t is:

```
SS_i(t) = (1 + N_i_Buy(t)) / (1 + N_i_NotBuy(t))
```

Where N_i_Buy(t) = count of "buy" (bullish) classified tweets for coin i in the preceding 24 hours, and N_i_NotBuy(t) = count of "not-buy" (bearish + neutral combined) classified tweets. The "not-buy" class combines sell and neutral signals because sell signals were rare (5.5% of influencer data, 25.5% of news data).

An augmented version incorporates general crypto market tweets (tweets about crypto without mentioning any specific coin):

```
SS_i_Crypto(t) = (1 + N_i_Buy(t) + N_Crypto_Buy(t)) / (1 + N_i_NotBuy(t) + N_Crypto_NotBuy(t))
```

### Long entry (research-proposed)

When SS_i(t) or SS_i_Crypto(t) increases relative to its recent rolling average, the social signal hypothesis predicts a positive price return at lags of 6-24 hours. No specific entry threshold is specified by the source.

### Short entry (research-proposed)

Not specified by the source. The paper tests Granger causality in both directions but focuses on the predictive power of social signals for prices, not the reverse.

### Exit (research-proposed)

Not specified by the source. The paper is exploratory/academic and does not define exit rules.

### Holding period (research-proposed)

The Granger causality results suggest predictability at lags of 1-24 hours, implying a maximum holding period of approximately 1 day. No specific holding period is prescribed.

### Parameters

- Signal model: CryptoBERT (trained on 3.2M crypto social media posts), accuracy 84% on 800 labeled influencer/news tweets.
- Irrelevance filter: GPT-3.5 with optimized prompt, accuracy 94% on 500 annotated tweets.
- Influencer identification: 4-method approach (retweet network centrality, marketing campaign analysis, keyword-based crawling, LunarCrush scraping), filtered to accounts with 5,000+ followers, active in last 3 months, average engagement 200+.
- All parameters above are source-reported.

### Position sizing (research-proposed)

Not specified by the source.

### Multi-timeframe (research-proposed)

The paper tests both hourly lags (1-24 hours) and daily/weekly cross-correlations (up to 7 days), suggesting multi-horizon effects. No specific multi-timeframe implementation is proposed.

### Fully specified?

**Underspecified.** The paper provides the signal formula and Granger causality evidence but does not define a complete trading strategy with entry thresholds, exit rules, sizing, or risk management.

## Required data

- **Instrument:** 9 major cryptocurrencies (BTC, ETH, XRP, SOL, DOGE, BNB, ADA, DOT, SHIB).
- **Venue:** CoinMarketCap aggregate prices (multi-exchange composite).
- **Market type:** Spot prices.
- **Timeframe:** Hourly prices; hourly tweet timestamps.
- **Fields:** OHLCV (from CoinMarketCap); tweet text, user metadata, retweet/follower counts (from Twitter Academic API).
- **Point-in-time:** Tweets collected via API during sample period; no survivorship bias treatment for influencer list.
- **Timestamp:** Not explicitly stated; Twitter API default timestamps assumed.
- **Missing-data:** Tweet filtering removes irrelevant content; no explicit treatment of missing price data.
- **Funding/fee/spread:** Not modeled.

## Execution assumptions

- **Signal-to-order timing:** Social signal available at timestamp t; price predictability at lags 1-24 hours (source-reported Granger causality p-values).
- **Fill model:** Not specified.
- **Fees:** Not modeled.
- **Slippage:** Not modeled.
- **Spread:** Not modeled.
- **Impact / capacity:** Not assessed. The paper does not discuss market impact or capacity constraints.
- **Leverage:** Not modeled.
- **Latency:** Not discussed. In practice, influencer tweets can be scraped in near-real-time, but the paper uses batch collection.

**Critical data gap:** The paper provides no transaction cost, slippage, or spread analysis. The Granger causality evidence does not imply net-of-cost profitability.

## Evidence

### Source-reported

All results below are from Alizadeh et al. (arXiv:2411.05577v1):

**Granger causality (Table 3, price changes ri_CP(t) vs. social signal ri_SS_crypto(t)):**
- **BTC:** p < 0.01 at lags 1-6 hours, p < 0.05 at lags 7-12 hours, p < 0.1 at lags 13-24 hours.
- **ETH:** p < 0.01 at lags 1-6 hours, p < 0.05 at lags 7-24 hours.
- **SOL:** p < 0.01 at lags 1-24 hours (strongest effect across all coins).
- **DOGE:** p < 0.05 at lags 1-6 hours, p < 0.1 at lags 7-12 hours.
- **ADA:** p < 0.05 at lags 1-3 hours only.
- **XRP:** p < 0.05 at lags 1-3 hours, p < 0.1 at lags 4-6 hours.
- **DOT:** p < 0.05 at lags 1-5 hours, p < 0.1 at lags 6-12 hours.
- **BNB:** p > 0.1 at all lags (no significant Granger causality).
- **SHIB:** p > 0.1 at lags 1-20 hours, p < 0.05 at lags 21-22 hours only.

**Cross-correlation (Table 4, highest correlation for ri_CP(t) vs. ri_SS_crypto(t)):**
- XRP: 0.04 at lag 20H (strongest among coins)
- ETH: 0.06 at lag 1H
- BTC: 0.08 at lag 0H
- SOL: 0.06 at lag 1H
- DOGE: 0.05 at lag 0H

These correlations are economically small. The paper frames these as statistically significant but does not claim a tradeable edge.

**Key finding (source-reported):** "For the top three cryptocurrencies with the highest presence within news and influencer posts [BTC, ETH, SOL], their aggregated LLM-detected trading signal over the preceding 24 hours granger-causes fluctuations in their market prices, exhibiting a lag of at least 6 hours."

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Mixed results across cryptocurrencies: BNB shows no significant Granger causality; SHIB shows only very delayed (21-22H) significance.
- Cross-correlation coefficients are small (mostly < 0.1 for log returns), suggesting the predictive relationship, while statistically significant, may be economically weak.
- The paper is explicitly framed as exploratory: "Our exploratory results showed..." (Conclusion, Section 5).
- The 5-month sample period (June 2023 - February 2024) covers a specific market regime (post-FTX recovery, Bitcoin ETF anticipation) and may not generalize.
- The authors note: "Overall, the results show a mixed pattern across cryptocurrencies and temporal periods."

## Falsification plan

1. **Out-of-sample replication (research-defined):** Re-run the CryptoBERT signal extraction and Granger causality analysis on a new 6-month period (e.g., March-September 2024). **Failure rule:** If BTC and ETH lose Granger significance at lags 1-6 hours at the 5% level, the signal is not temporally robust.
2. **Net-of-cost backtest (research-defined):** Implement a simple long-only strategy: buy at SS_i(t) increase, hold for 6-12 hours, exit. Include 10 bps round-trip costs (research-proposed). **Failure rule:** If Sharpe ratio < 0.5 after costs, the edge does not survive transaction friction.
3. **Influencer list decay (research-defined):** Re-identify the top influencer list using the same 4-method approach on a different 6-month period. **Failure rule:** If fewer than 50% of original influencers remain in the top list, the signal is not stable across time.
4. **Ablation: news outlets vs. influencers (research-proposed):** Test Granger causality separately for news outlets and influencer tweets. **Failure rule:** If news-outlet-only signals lose significance, the alpha is concentrated in influencer-specific behavior.
5. **Parameter sensitivity (research-defined):** Vary the lookback window from 12-48 hours. **Failure rule:** If significance is fragile across window choices, the result may be data-mined.
6. **Regime breakdown (research-defined):** Test separately in bull vs. bear sub-periods. **Failure rule:** If the signal only works in one regime, it is not a robust alpha.

## Crypto portability

**Direct.** The paper is entirely crypto-native: it uses cryptocurrency prices from CoinMarketCap and Twitter signals about crypto markets.

Key crypto-specific considerations:
- **Venue fragmentation:** CoinMarketCap aggregates across exchanges; actual execution would be venue-specific with different liquidity profiles.
- **24/7 market:** The hourly analysis aligns with crypto's continuous trading, but tweet volume may have diurnal patterns (more tweets during US/EU hours).
- **Twitter/X platform changes:** The paper uses Twitter Academic API; post-acquisition API changes may affect data availability.
- **Bot/manipulation risk:** The influencer identification process filters for "authentic" accounts, but the paper acknowledges that ~14% of crypto Twitter accounts are bots (citing Kraaijeveld & De Smedt 2020).
- **Signal decay:** Influencer credibility and follower attention may shift over time; the signal requires continuous re-identification of relevant influencers.

## Limitations

- **Small sample period:** 5 months (June 2023 - February 2024) covers a specific regime (post-FTX, pre-Bitcoin ETF approval). Generalizability is untested.
- **Low cross-correlation coefficients:** Log-return correlations are mostly < 0.1, suggesting the predictive relationship is statistically significant but economically small.
- **No transaction cost analysis:** The paper provides no evidence that the edge survives costs.
- **No risk management:** No stop-loss, position sizing, or portfolio construction framework.
- **Simple signal formula:** Equal weighting across all influencers regardless of follower count, engagement, or track record. The authors note this as a limitation and suggest future work on weighted signals.
- **Mixed results:** BNB shows no significant Granger causality; SHIB shows only very delayed effects; cross-asset results are heterogeneous.
- **Influencer identification is opaque:** The 4-method influencer selection process is complex and may not be reproducible without access to the same raw Twitter data.
- **Classification accuracy:** CryptoBERT achieves 84% accuracy on the trading signal task, implying ~16% misclassification rate that could introduce noise.
- **No independent reproduction:** Results have not been independently verified.
- **Platform risk:** Twitter/X API changes, paywall restrictions, or platform policy changes could invalidate the data collection approach.

## Implementation status

Not implemented. No backtest, paper trading, or live implementation has been conducted by the authors or by our research system.

## Adoption boundary

This record is research-only material. It does not constitute:
- A validated alpha signal;
- A recommendation to trade;
- Evidence of profitable trading after costs;
- Approval for implementation, paper trading, testnet, or live trading.

## Related Wiki records

- [[crypto-market-derived-sentiment-crypto-tbl-tweet-trading-2026-09-07]] — uses CryptoBERT for market-derived sentiment signals on crypto tweets, but with a different label generation method (market-condition-based rather than manual annotation).
- [[digital-twin-finfluencer-belief-elicitation-silent-region-cross-sectional-2026-09-06]] — studies finfluencer belief elicitation and silent-region signals, but for equity markets via structured interviews, not Twitter text classification.

## Sources

1. Meysam Alizadeh, Yasaman Asgari, Zeynab Samei, Sara Yari, Shirin Dehghani, Mael Kubli, Darya Zare, Juan Diego Bermeo, Veronika Batzdorfer, and Fabrizio Gilardi. "Exploring Relationships Between Cryptocurrency News Outlets and Influencers' Twitter Activity and Market Prices." arXiv preprint `arXiv:2411.05577v1 [cs.SI]`, submitted November 8, 2024. DOI: [10.48550/arXiv.2411.05577](https://doi.org/10.48550/arXiv.2411.05577). URL: https://arxiv.org/abs/2411.05577.
