---
schema: strategy-research-record-v1
title: "Crowd Trading Signals — Social Media Explicit Buy/Sell Predict Short-Term Crypto Returns"
created: 2026-09-11
updated: 2026-09-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - social-media
  - event-study
  - sentiment
status: research-only
confidence: medium
source_as_of: 2026-09-11
sources:
  - "https://doi.org/10.1007/s12525-025-00815-6"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crowd Trading Signals — Social Media Explicit Buy/Sell Predict Short-Term Crypto Returns

## Provenance

- **Primary source:** Frederic Haase, Tom Celig, Oliver Rath, and Detlef Schoder. "Wisdom of the crowd signals: Predictive power of social media trading signals for cryptocurrencies." *Electronic Markets*, Volume 35, article number 64 (2025). DOI: [10.1007/s12525-025-00815-6](https://doi.org/10.1007/s12525-025-00815-6). Open access.
- **Sample period:** January 1, 2022 to June 30, 2023 (hourly resolution).
- **Universe:** 287 cryptocurrencies with ≥100 crowd trading signals each, sourced from CoinMarketCap listed assets. 28,700 signals total (100 per crypto, balanced).
- **Data source (signals):** Stockpulse database covering X (Twitter), Reddit, Stocktwits, Telegram, CoinMarketCap, and Discord.
- **Data source (prices):** CoinMarketCap aggregated hourly closing prices (from Coinbase, Kraken, and others).
- **Publication status:** Published in Electronic Markets (Springer), received 19 January 2025, accepted 25 June 2025, published online 11 July 2025.

## Economic mechanism

### Source-reported

The authors propose that explicit crowd-based trading signals — time-stamped buy and sell recommendations shared publicly on social media — represent concrete trading advice that captures collective market expectations in real time. Unlike aggregated sentiment (which averages over noisy posts), these explicit signals represent actionable intent from heterogeneous market participants. The mechanism is that social media users observe market events, formulate directional views, and share them publicly; subsequent short-term price continuation around these signals creates a temporary trading opportunity before market self-correction.

### Research interpretation

The hypothesized mechanism is a combination of:

1. **Short-term autocorrelation / momentum continuation:** Market events trigger social media signal generation; the initial trend continues briefly (1–4 hours) before reversing, creating a window for signal-following trades.
2. **Information diffusion lag:** Retail crowd participants observe and react to market events with a small delay; their explicit signals then propagate through social networks, creating delayed order flow that temporarily continues the original price move.
3. **Asymmetric predictability:** Sell signals show stronger and more persistent predictive effects than buy signals (AR = -0.52% vs +0.35% at hour 0), suggesting that selling pressure or negative information propagates differently than buying pressure.
4. **Market efficiency interaction:** The effect concentrates in low-cap and low-performance cryptos, consistent with these assets being less informationally efficient and more susceptible to crowd-driven price pressure.

## Signal

- **Formation timestamp:** Signal extracted from social media posts using a zero-shot LLM classification (BART Large MNLI) that classifies posts into five categories: "Immediate buy advice," "Immediate sell advice," "Neutral," "Long-term trading advice," and "Not related." Inter-rater agreement: Gwet's Gamma = 0.7239 (buy) and 0.7179 (sell).
- **Lookback window:** CAPM regression estimation uses 240 hours of data before each signal, with a 24-hour gap between estimation window and event window.
- **Long entry:** At the asset's hourly open price at the time of the buy signal.
- **Short entry (sell signal):** At the asset's hourly open price at the time of the sell signal (direction implied by the signal direction).
- **Exit:** Position closed at the close price one hour after entry.
- **Holding period:** 1 hour (fixed).
- **Re-entry rules:** New signal triggers a new position; no position carried across signals.
- **Position sizing:** research-proposed — fixed equal-weight sizing across all signals; capital allocated evenly across all signals received each day.
- **Transaction costs:** research-proposed — 0.3% per trade (round-trip = 0.6%).
- **Filtering:** Top and bottom 3% of trade returns excluded via quantile filter (to handle illiquid/small-cap artifacts).
- **Aggregation:** Equal-weighted daily capital curve, no compounding across individual trades.
- **Parameters:**
  - Signal classification threshold: zero-shot with "Immediate buy/sell advice" label
  - Entry: hourly open; exit: hourly close, 1 hour later
  - Fee: 0.3% per trade
  - Quantile filter: 3% on each tail
  - Minimum signals per crypto: 100

## Required data

- **Instrument:** 287 cryptocurrencies across a wide range of market capitalizations (from ~$55M median to top coins).
- **Venue:** CoinMarketCap aggregated prices (from Coinbase, Kraken, and other leading exchanges).
- **Market type:** Spot (aggregated across exchanges).
- **Timeframe:** Hourly resolution.
- **Fields:** Hourly OHLC (close used for CAPM abnormal returns; open used for strategy entry; close used for strategy exit).
- **Social media data:** Posts from X (Twitter), Reddit, Stocktwits, Telegram, CoinMarketCap, and Discord, tagged with crypto cashtags.
- **Market capitalization:** From CoinMarketCap as of June 30, 2023.
- **Point-in-time:** Signal timestamps are from the original social media post timestamps. Price data from CoinMarketCap. No explicit lookahead protections are described for the social media data pipeline.
- **Timestamp:** Hourly aggregation; timezone not explicitly stated (CoinMarketCap standard).
- **Missing-data:** Not stated; signals from cryptocurrencies with <100 signals were excluded.

## Execution assumptions

- **Signal-to-order timing:** Signal published on social media → trader identifies signal → enters at next hourly open. The latency between signal publication and trader action is not explicitly modeled; the strategy assumes execution at the same hourly candle's open.
- **Fill model:** research-proposed — perfect fill at hourly open price.
- **Fees:** research-proposed — 0.3% per trade (source states this assumption but does not provide empirical justification).
- **Slippage:** Not modeled. Source explicitly states: "Factors such as slippage were not accounted for in our analysis."
- **Spread:** Not modeled.
- **Impact / capacity:** Not modeled. The strategy does not account for market impact, particularly relevant for low-cap cryptos where the effect is strongest.
- **Leverage / margin:** Not used (spot only).
- **Funding:** Not applicable (spot).
- **Borrow / shorting:** Not applicable (sell signals result in closing positions or going short only in the hypothetical; the strategy description is ambiguous about whether it actually shorts or simply avoids longs).
- **Latency:** Not modeled.

## Evidence

### Source-reported

All results from Haase et al. (2025):

**Event study results (hour 0):**
- Buy signals: AR = +0.003497 (+0.35%), permutation p < 0.01, 55.83% positive returns.
- Sell signals: AR = -0.005180 (-0.52%), permutation p < 0.01, 63.87% negative returns.
- Sell signals are significantly stronger than buy signals (asymmetric effect).

**Subsample analysis (hour 0):**
- Low-cap crypto buy signals: AR = +0.006732 vs high-cap: +0.003802 (diff. p < 0.01).
- Low-cap crypto sell signals: AR = -0.007722 vs high-cap: -0.005208 (diff. p < 0.01).
- Low-performance crypto buy signals: AR = +0.005778 vs high-performance: +0.004825 (diff. p < 0.01).
- Low-performance crypto sell signals: AR = -0.007066 vs high-performance: -0.005514 (diff. p < 0.01).
- Cryptocurrency age: no significant difference (H4 rejected).

**Post-signal dynamics:**
- Buy signals: negative AR at hour +1 (AR = -0.000469, p < 0.01), suggesting partial reversal.
- Sell signals: sustained negative AR at hours +4, +6, +7 (all p < 0.01).

**Trading strategy (out-of-sample):**

| Metric | Strategy | CCI30 | S&P 500 |
|---|---|---|---|
| Total return | 115.23% | 67.72% | 11.80% |
| Sharpe ratio | 2.43 | 2.60 | 2.02 |
| Max drawdown | -14.92% | -23.91% | -10.28% |
| Win rate | 27.97% | 57.34% | 56.64% |

- The strategy achieves 115.23% total return on the out-of-sample period with a Sharpe of 2.43.
- Win rate is low (27.97%) but the average winning trade is large enough to compensate — the strategy relies on fat-tailed positive returns.
- The low win rate combined with high Sharpe suggests the strategy profits from occasional large moves.

**Neutral signal robustness:** AR at hour 0 for neutral signals is -0.000324, statistically insignificant — confirming that directional content drives the effect.

**Market-adjusted model robustness:** Results consistent with CAPM-based abnormal returns.

**Signal bot prevalence:** ~6% of accounts classified as signal bots; not considered to significantly impact results.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The source acknowledges that signals may be reactive (follow rather than lead price movements): "some signals appear to follow, rather than lead, market movements — suggesting partially reactive behavior by users."
- Buy signals show a reversal at hour +1 (negative AR), suggesting the effect is temporary and partially mean-reverting.
- The authors note: "In practice, one would likely incorporate more refined signal selection criteria, dynamically adjust allocations, and integrate additional data sources."
- Slippage and market impact are not modeled; for low-cap cryptos (where effects are strongest), these costs could substantially erode returns.
- The sample period (Jan 2022 – Jun 2023) spans a crypto bear market (2022) and partial recovery (2023); regime dependence is not tested.
- ~10% of the crypto universe overlaps with known pump-and-dump targets (La Morgia et al. 2023), though no direct pump-and-dump signal was identified in the dataset.

## Falsification plan

- **Out-of-sample period:** The source used an out-of-sample split, but the full-sample and out-of-sample periods are within the same Jan 2022–Jun 2023 window. A truly forward-looking test on Jul 2023+ data is needed.
- **Regime dependence:** Test whether the signal predictive power persists across bull, bear, and sideways regimes. The sample is predominantly bear-to-neutral.
- **Cost sensitivity:** The 0.3% fee assumption is optimistic for low-cap cryptos. Test at 0.5%, 1.0%, and 2.0% per trade.
- **Slippage stress:** Model explicit slippage for low-cap cryptos (where effects are strongest) — 0.1%, 0.5%, 1.0% per trade.
- **Capacity / impact:** Test whether returns degrade as position size increases, particularly for the low-cap subsample.
- **Signal decay over time:** Test whether the effect persists as the dataset grows older and more participants adopt similar strategies.
- **Platform decomposition:** Test whether effects differ across X, Reddit, Stocktwits, Telegram, and Discord.
- **Bot filtering:** Test whether removing identified signal bots changes results.
- **Alternative benchmarks:** Compare against buy-and-hold of the same universe (rather than CCI30) and risk-free rate.

## Crypto portability

direct

The source is specifically about crypto spot markets across 287 cryptocurrencies. The mechanism (social media signal → short-term price continuation) is directly studied in crypto. However:

- The study uses CoinMarketCap aggregated spot prices, not per-exchange data. Execution on any single venue may face different liquidity and slippage conditions.
- The 287-crypto universe includes many low-cap tokens with thin order books; real-world execution at the signal timestamp may be substantially worse than hourly open price.
- No perpetual futures, funding rate, or leverage considerations are addressed.
- 24/7 market structure means signals can arrive at any time, requiring always-on monitoring.

## Limitations

- **No slippage or market impact modeled:** The source explicitly acknowledges this. For low-cap cryptos (where effects are strongest), this is a material omission.
- **Reactive signal concern:** The authors acknowledge signals may follow rather than lead price movements, suggesting the "predictive" power may partly reflect trend continuation from the underlying event.
- **Regime dependence untested:** The sample spans a bear market and partial recovery; behavior in strong bull markets is unknown.
- **CoinMarketCap aggregated prices:** May not reflect actual executable prices on any single exchange.
- **Low win rate (27.97%):** The strategy relies on large winners to compensate for frequent small losses; this is psychologically challenging and execution-sensitive.
- **Data source dependency:** Requires access to Stockpulse database for historical social media signals; this is a proprietary data source.
- **No replication in perpetual futures or leveraged context:** All results are spot-only.
- **Sample period limitation:** Jan 2022–Jun 2023 may not be representative of all market conditions.
- **Pump-and-dump overlap:** ~10% of crypto universe historically targeted by pump-and-dump schemes; effect of including/excluding these is not tested.

## Implementation status

Not implemented. No implementation in our research stack (PyBroker, Nautilus, or otherwise).

## Adoption boundary

This record is research material only. Presence in this repository does **not** mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

## Related records

- `[[llm-crypto-influencer-twitter-trading-signal-granger-6h-lag-2026-09-07]]` — Related but materially distinct: Alizadeh et al. (2024) study influencer/news outlet Twitter activity and Granger causality at 6-hour lags; Haase et al. (2025) study explicit crowd buy/sell signals with hourly event study and immediate (1-hour) predictive power. Different source, mechanism, methodology, sample, and timing.

## Sources

1. Frederic Haase, Tom Celig, Oliver Rath, and Detlef Schoder. "Wisdom of the crowd signals: Predictive power of social media trading signals for cryptocurrencies." *Electronic Markets*, Volume 35, article number 64 (2025). DOI: [10.1007/s12525-025-00815-6](https://doi.org/10.1007/s12525-025-00815-6). URL: https://link.springer.com/article/10.1007/s12525-025-00815-6.
