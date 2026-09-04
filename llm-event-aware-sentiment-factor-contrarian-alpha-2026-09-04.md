---
schema: strategy-research-record-v1
title: "LLM Event-Aware Sentiment Factor: Contrarian Alpha from Social Media Event Labels (Wang & Wei 2025)"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - sentiment
  - llm
  - contrarian
  - event-driven
status: research-only
confidence: medium
source_as_of: 2026-09-04
sources:
  - "Yueyi Wang, Qiyao Wei, 'Event-Aware Sentiment Factors from LLM-Augmented Financial Tweets: A Transparent Framework for Interpretable Quant Trading', arXiv:2508.07408v1 [q-fin.ST], August 10 2025. https://arxiv.org/abs/2508.07408"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# LLM Event-Aware Sentiment Factor: Contrarian Alpha from Social Media Event Labels

## Provenance

- Paper: arXiv:2508.07408v1 [q-fin.ST], submitted August 10, 2025.
- Authors: Yueyi Wang, Qiyao Wei.
- Venue: Accepted at ICML 2025 New in ML Workshop.
- DOI: 10.48550/arXiv.2508.07408
- Source URL: https://arxiv.org/abs/2508.07408
- Code: Authors state all code and methodologies are publicly available; specific repository URL not identified in the paper text at time of capture.
- Dataset: 85,176 cleaned English-language tweets linked to stock tickers, subset of 862,231 original tweets. Tweet data sourced from Sowinska et al. (2020).
- Market data: Daily closing prices for S&P 500 constituents, aligned with tweet timestamps.
- Source data as-of: 2017 tweet corpus; backtest period not explicitly bounded in abstract but multi-year evaluation referenced.

## Economic mechanism

### Source-reported

The authors hypothesize that social media sentiment contains information beyond simple positive/negative polarity. By using an LLM (Gemini-2.5-pro) to assign multi-label event categories (e.g., "Speculation/Rumor," "Retail Investor Buzz," "Geopolitical Tension") to high-sentiment-intensity tweets, they construct event-specific sentiment factors. Certain event categories—particularly "Speculation/Rumor" and "Geopolitical Tension"—consistently yield negative forward returns when tweet volume and net tone are high, acting as contrarian indicators. The mechanism is that elevated social media discussion around these themes reflects retail overreaction, noise, or crowding, which corrects over subsequent days.

### Research interpretation

The hypothesized alpha channel is **contrarian sentiment reversal at short horizons**: high-intensity social media buzz around speculative or geopolitical narratives creates transient mispricing driven by retail overreaction and herding. The LLM event labels act as a signal-quality filter, separating noise-driven sentiment (which predictably reverses) from information-driven sentiment. The "Speculation/Rumor" label captures rumor-driven pump narratives; "Geopolitical Tension" captures fear-driven panic; "Retail Investor Buzz" captures retail momentum herding. The contrarian signal (fading high event-tone stocks) generates negative Sharpe ratios, implying a short-biased or mean-reversion alpha.

Key components:
- **Signal source:** LLM (Gemini-2.5-pro) zero-shot multi-label classification of financial tweets into 70+ event categories.
- **Net tone scoring:** Each tweet receives a continuous sentiment score via stacked LDA + logistic regression trained on forward returns.
- **Factor construction:** For each event label *e*, stock *i*, day *t*: F_{i,t,e} = sum of net tones for tweets tagged with *e* about stock *i* on day *t*.
- **Portfolio construction:** Cross-sectional quantile sorts on F_{i,t-1,e}; long-short decile portfolios.
- **Holding periods:** 1, 2, 3, and 7 trading days.

## Signal

- **Formation timestamp:** Daily, at market close. Tweets are timestamped; factor is computed at end-of-day t using all tweets on day t.
- **Lookback:** Same-day aggregation (no multi-day lookback by default; the factor aggregates tweet tones within a single day).
- **Long entry:** Bottom decile of event-tone factor (stocks with low/absent discussion of the event category).
- **Short entry:** Top decile of event-tone factor (stocks with high-volume, high-tone discussion of the event category).
- **Exit:** After holding period (1, 2, 3, or 7 days); daily rebalancing implied.
- **Parameters:** 70+ event category dictionary; sentiment threshold for tweet inclusion (not precisely specified in paper text); decile-based portfolio sorts; equal-weighted within quintiles/deciles.
- **Specification status:** Signal is reconstructible at a high level (factor formula, portfolio sort method, event dictionary described). Exact tweet preprocessing pipeline, sentiment model hyperparameters, and LLM prompting template are stated as publicly available but not reproduced in the paper text; these are research-defined parameters that would need the code repository to reproduce exactly.

## Required data

- **Instrument:** S&P 500 constituent stocks (US equities).
- **Venue:** US equity market (unspecified exchanges).
- **Market type:** Equities (spot).
- **Timeframe:** Daily bars (close-to-close returns).
- **Fields:** Daily closing prices; tweet-level text data with timestamps and cashtag annotations.
- **Point-in-time:** Tweets are timestamped; market data is daily close. The tweet dataset is from 2017; exact availability lag and look-ahead treatment not fully specified in paper text.
- **Timestamp:** Tweet timestamps are available; daily market data aligned to trading day close.
- **Missing-data:** Not explicitly addressed in paper text.

## Execution assumptions

- **Signal-to-order timing:** End-of-day factor construction; next-day execution assumed (factor at t-1, returns at t).
- **Order type:** Not specified; equal-weighted decile portfolios imply market-order execution at next open or close.
- **Fill model:** Not specified.
- **Fees/commissions:** Not explicitly modeled in the factor backtest.
- **Slippage:** Not explicitly modeled.
- **Impact/capacity:** Not discussed; S&P 500 universe suggests large-cap with reasonable liquidity, but signal capacity at scale is unknown.
- **Leverage/margin:** Not specified; long-short decile portfolios may require margin.
- **Benchmark:** Market index (S&P 500) used for equity curve comparison.

## Evidence

### Source-reported

**Lexicon-based baseline strategy (Section 4.1):**
- Annualized return: 8%
- Sharpe ratio: 5.0
- Maximum drawdown: -15.2%
- This baseline uses a dictionary trained on 2017 data; results presented in Figures 1-2 of the paper.

**LLM event-specific factors (Table 2, primary results):**

1-day horizon:
| Event Label | Samples | Sharpe | IC | p-value |
|---|---|---|---|---|
| Speculation/Rumor | 130 | -0.337*** | -0.039 | 0.0002 |
| Retail Investor Buzz | 92 | -0.359*** | 0.096 | 0.0009 |
| Geopolitical Tension | 25 | -0.661** | -0.139 | 0.0030 |

3-day horizon:
| Event Label | Samples | Sharpe | IC | p-value |
|---|---|---|---|---|
| Speculation/Rumor | 130 | -0.267** | -0.107 | 0.0028 |
| Geopolitical Tension | 25 | -0.700** | -0.078 | 0.0018 |

7-day horizon:
| Event Label | Samples | Sharpe | IC | p-value |
|---|---|---|---|---|
| Speculation/Rumor | 130 | -0.376*** | 0.104 | 0.0000 |
| Retail Investor Buzz | 92 | -0.461*** | 0.113 | 0.0000 |
| Geopolitical Tension | 25 | -0.540* | -0.104 | 0.0125 |

**Interpretation:** High event-tone stocks underperform (negative Sharpe on long-short decile portfolios). The "Retail Investor Buzz" IC turns positive at 7-day horizon, suggesting short-term overreaction followed by partial reversal. The "Speculation/Rumor" and "Geopolitical Tension" signals are consistently negative across all horizons.

**Residual analysis (Section 4.2):** Authors claim event-based factors are orthogonal to market beta, confirming alpha rather than risk-factor exposure.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Small sample sizes for some event categories (Geopolitical Tension: N=25; Viral Marketing Campaign: N=17).
- The 7-day horizon Geopolitical Tension result has p=0.0125 (significant but weaker than shorter horizons).
- "Retail Investor Buzz" IC is positive at 7-day horizon (IC=0.113), suggesting the contrarian signal may decay or reverse at longer horizons.
- The lexicon-based baseline Sharpe of 5.0 appears exceptionally high and may reflect in-sample bias (dictionary trained on same period as test).

## Falsification plan

1. **Out-of-sample test:** Apply the same pipeline to tweet data from 2018-2025 (different year) without retuning; failure if event-specific Sharpe ratios collapse to zero or flip sign.
2. **Cross-market replication:** Apply to crypto social media (Twitter/X posts about BTC, ETH, etc.) with appropriate event dictionary adaptation; failure if event labels show no predictive power in crypto.
3. **Parameter perturbation:** Vary the sentiment intensity threshold, number of quantiles (5 instead of 10), and holding period; failure if Sharpe ratios become insignificant.
4. **Transaction cost stress:** Add 5-10 bps round-trip cost; failure if Sharpe ratios collapse below 1.0.
5. **LLM sensitivity:** Re-run with a different LLM (e.g., GPT-4, Claude) to test if results are model-dependent.
6. **Event dictionary ablation:** Test with reduced event dictionary (3 categories instead of 70+); failure if results are driven by a single dominant category rather than the event taxonomy.
7. **Placebo test:** Shuffle tweet timestamps and re-run; failure if Sharpe ratios remain significant (would indicate overfitting).

## Crypto portability

**Adapted**

The mechanism (contrarian sentiment reversal from social media event labels) is theoretically portable to crypto markets, which exhibit strong retail-driven sentiment dynamics. However:

- The paper only demonstrates the effect in US equities; no crypto evidence exists.
- Crypto social media (Twitter/X, Reddit, Telegram) has different noise characteristics, bot prevalence, and narrative dynamics than equity social media.
- The 24/7 crypto market structure means daily aggregation may miss intraday sentiment dynamics.
- Event categories would need re-calibration for crypto-specific narratives (e.g., "halving speculation," "regulatory fear," "airdrop farming").
- Liquidity and market-impact differences between S&P 500 stocks and crypto assets are substantial.

## Limitations

- **Small samples:** Some event categories have very few observations (N=25 for Geopolitical Tension, N=17 for Viral Marketing Campaign). Statistical reliability is questionable for these categories.
- **Single-year data:** The tweet corpus is from 2017; results may not generalize to different market regimes.
- **In-sample baseline:** The lexicon-based baseline (Sharpe 5.0) may be inflated by in-sample training of the sentiment dictionary.
- **LLM dependency:** Results depend on Gemini-2.5-pro; different LLMs may produce different event labels and different factor performance.
- **No transaction costs:** The factor backtest does not account for trading costs, slippage, or market impact.
- **Code repository:** Authors claim code is publicly available but specific URL not identified in the paper; reproducibility depends on locating the repository.
- **Equities only:** No cryptocurrency or crypto-derivative evidence.
- **Not independently reproduced.**

## Implementation status

not-implemented. No implementation in our research stack. The paper provides a conceptual framework and backtested results only.

## Adoption boundary

This record is research material only. It does not imply:
- Profitable alpha
- Validated signal for our universe
- Approved for implementation
- Approved for paper/testnet/live trading

The negative Sharpe ratios on event-tone factors suggest a contrarian (short-biased) strategy, which has different operational requirements (short-selling capability, margin, borrow costs) than typical long-only approaches.

## Related Wiki records

None identified at time of capture.

## Sources

1. Yueyi Wang, Qiyao Wei, "Event-Aware Sentiment Factors from LLM-Augmented Financial Tweets: A Transparent Framework for Interpretable Quant Trading", arXiv:2508.07408v1 [q-fin.ST], August 10 2025. https://arxiv.org/abs/2508.07408
2. Accepted at ICML 2025 New in ML Workshop.
