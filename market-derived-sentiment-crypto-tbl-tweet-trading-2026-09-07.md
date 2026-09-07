---
schema: strategy-research-record-v1
title: "Market-Derived Sentiment: Context-Aware Language Models for Crypto Forecasting via Triple Barrier Labeling"
created: 2026-09-07
updated: 2026-09-07
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - sentiment
  - LLM
  - NLP
  - bitcoin
  - tweet
  - triple-barrier-labeling
status: research-only
confidence: medium
source_as_of: 2026-09-07
sources:
  - "Hamid Moradi-Kamali, Mohammad-Hossein Rajabi-Ghozlou, Mahdi Ghazavi, Ali Soltani, Amirreza Sattarzadeh, and Reza Entezari-Maleki, 'Market-Derived Financial Sentiment Analysis: Context-Aware Language Models for Crypto Forecasting', arXiv:2502.14897v2 [cs.CE], submitted February 17, 2025; revised March 2, 2025. DOI: 10.48550/arXiv.2502.14897. https://arxiv.org/abs/2502.14897"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Market-Derived Sentiment: Context-Aware Language Models for Crypto Forecasting via Triple Barrier Labeling

## Provenance

- **Authors:** Hamid Moradi-Kamali, Mohammad-Hossein Rajabi-Ghozlou, Mahdi Ghazavi, Ali Soltani, Amirreza Sattarzadeh, Reza Entezari-Maleki (School of Computer Engineering, Iran University of Science and Technology, Tehran, Iran)
- **Title:** Market-Derived Financial Sentiment Analysis: Context-Aware Language Models for Crypto Forecasting
- **arXiv:** 2502.14897v2 [cs.CE] (cross-listed: cs.CL, cs.LG, q-fin.ST)
- **Submitted:** February 17, 2025; v2 March 2, 2025
- **Status:** Preprint (not peer-reviewed)
- **Length:** 13 pages, 6 figures
- **Code:** https://github.com/hamidm21/Revisit_FSA (public repository referenced in paper)
- **Primary Source:** arXiv PDF: https://arxiv.org/pdf/2502.14897
- **Data as-of:** February 2025 (tweet data 2015–2023, Bitcoin OHLCV 2015–2023)

**Pre-Write Deduplication Audit:** An exhaustive search across all existing `*.md` records in the repository confirmed zero matches for `2502.14897`, `Moradi-Kamali`, `Rajabi-Ghozlou`, `Entezari-Maleki`, `market-derived sentiment`, `tweet classification bitcoin trading`, or `prompt-tuning sentiment crypto`. No existing record captures this paper or a materially similar mechanism. Triple Barrier Labeling appears only as a reference citation in `cross-sectional-equity-ridge-percentile-rank-alpha-2026-09-03.md` (citing Lopez de Prado 2018), which is a structurally different equity factor strategy with no overlap.

## Economic mechanism

### Source-reported

The authors hypothesize that traditional Financial Sentiment Analysis (FSA) fails because human-annotated sentiment labels (Bullish/Bearish/Neutral) are subjective and do not reflect actual market reactions to text. They propose replacing subjective annotations with **market-derived labels** using Triple Barrier Labeling (TBL), where labels are assigned based on subsequent price movements rather than perceived sentiment. The key insight is that historical market reactions to words are a more reliable indicator of their market impact than human interpretation.

The mechanism combines three components:
1. **Market-derived labeling**: Tweets are labeled based on whether subsequent BTC price action hits an upper barrier (Bullish), lower barrier (Bearish), or neither within a time window (Neutral), using dynamic barriers scaled by EWMA volatility.
2. **Context-aware language modeling**: A domain-specific language model (CryptoBERT) is fine-tuned on these market-derived labels, with market context (RSI, ROC, previous trend) and temporal context (date) injected via prompt-tuning.
3. **Signal aggregation**: Daily tweet predictions are aggregated via majority vote or mean averaging to generate trading signals, with confidence scores used for position sizing.

### Research interpretation

The hypothesized alpha mechanism is that social media text contains forward-looking information about short-term price trends, and that this information is better extracted when the language model is trained on labels that directly correspond to actual market outcomes rather than subjective sentiment interpretations. The market-derived labeling acts as a bridge between textual features and measurable price behavior, while prompt-tuning with technical indicators provides the model with market regime context.

This is a **composite signal** combining:
- **Primary signal:** Context-aware language model classification of daily Bitcoin tweets into market-derived trend labels (Bullish/Bearish/Neutral)
- **Confirmation:** Confidence-weighted aggregation of daily tweet predictions
- **Position sizing:** Confidence-score-proportional sizing (research-proposed)

## Signal

- **Formation timestamp:** Daily; tweet predictions are aggregated at end-of-day using majority vote or mean method. Signal is formed after all daily tweets are classified.
- **Lookback:** The language model processes individual tweets in real-time. The TBL labeling uses a 30-day EWMA volatility window for barrier calibration. The vertical barrier (holding period) ranges from 8 to 15 days, optimized per evaluation period.
- **Long entry:** Bullish signal (majority vote or mean exceeds threshold) → open long position.
- **Short entry:** Bearish signal → open short position (In-Out-Short strategy).
- **Exit:** Bearish signal closes long; Bullish signal closes short (In-Out strategy). TBL strategy uses dynamic take-profit/stop-loss barriers.
- **Holding period:** TBL strategy: typically 2–5 days per trade (source-reported average). In-Out strategy: held until opposite signal.
- **Parameters:**
  - EWMA volatility window: τ = 30 days
  - Upper/lower barrier factors (Fu, Fl): optimized over 6-month intervals to maximize Sharpe ratio (research-proposed optimization)
  - Vertical barrier: 8–15 days, optimized per period (research-proposed)
  - Language model: CryptoBERT, first 11 layers frozen, classification head fine-tuned
  - Training: 2 epochs, 5-fold cross-validation, AdamW optimizer, lr=10⁻⁵, batch size=12
  - Prompt features: Previous window trend, ROC, RSI (described as text in prompts)
- **Position sizing:** Confidence-score-proportional (normalized 0–1 via min-max). Higher confidence → larger position (research-proposed).
- **Re-entry rules:** New signal at each daily aggregation triggers re-evaluation.
- **Underspecified:** Exact threshold values for mean-method signal generation (Tbearish, Tbullish) are optimized per 6-month period but specific values are not disclosed in the paper; barrier factors Fu, Fl are optimized but exact values not reported.

## Required data

- **Instrument:** Bitcoin (BTC/USD)
- **Universe:** Single asset (Bitcoin only); no cross-sectional component
- **Venue:** Not specified for trading; tweet data sourced from Twitter/X (2015–2023); OHLCV from unspecified source (likely Yahoo Finance or similar, given PreBit baseline comparison)
- **Market type:** Spot Bitcoin (no perpetual/futures differentiation in the paper)
- **Timeframe:** Daily bars for OHLCV; daily aggregation of tweet predictions
- **Fields:**
  - OHLCV (Open, High, Low, Close, Volume)
  - Twitter/X tweets about Bitcoin (daily collection, ~60,000 tweets per evaluation fold)
  - Technical indicators: RSI (thresholds 30/70), ROC (dynamically thresholded), MACD, SMA7, SMA21, EMA12, EMA26
  - Ethereum price, Gold price (used in fusion baseline, not in primary model)
- **Timestamp:** Daily; tweet timestamps used for temporal context (year, month, day)
- **Missing-data:** Not explicitly addressed. Tweet preprocessing includes URL removal, user ID removal, punctuation removal, lemmatization, and filtering of promotional/advertisement content.
- **Point-in-time:** Tweets are collected daily and labeled using only information available up to that date (no look-ahead in labeling). TBL barriers are computed using historical EWMA volatility (forward-looking without look-ahead bias, per authors).

## Execution assumptions

- **Signal-to-order timing:** End-of-day signal generation; assumed next-day execution (not explicitly stated).
- **Order type:** Assumed market order (not specified).
- **Fill model:** Not specified; assumed perfect fill at close.
- **Fees:** Not modeled in the primary backtest. The authors note that "robust evaluation frameworks must simulate real-world conditions, incorporating transaction costs" as future work.
- **Slippage:** Not modeled.
- **Spread:** Not modeled.
- **Impact / capacity:** Not addressed. Single-asset (BTC) strategy with daily rebalancing; capacity likely limited by BTC liquidity but not a binding constraint for retail-sized capital.
- **Leverage / margin:** Not specified; assumed 1x.
- **Latency:** Not applicable for daily-frequency strategy.
- **Partial fills / failures:** Not addressed.

**Critical execution gap:** The paper does not model transaction costs, slippage, or spread. Given the high Sharpe ratios reported, cost sensitivity is a major unknown. The TBL strategy executes 33–84 trades per evaluation period (each 6–12 months), implying roughly monthly turnover. At typical crypto spot taker fees (10–15 bps round-trip), cumulative cost drag over a 6-month period could be material but is not quantified.

## Evidence

### Source-reported

All figures below are directly reported by Moradi-Kamali et al. (arXiv:2502.14897v2, February/March 2025):

**Classification performance (Table 1, 5-fold cross-validation on 2020 dataset Ea, ~60,000 tweets):**
- Base-1 (FinBERT): F1 17.2% ± 0.3%
- Base-2 (CryptoBERT): F1 27.7% ± 0.8%
- CUA (CryptoBERT fine-tuned on market-derived labels): F1 43.0% ± 2.2%
- CA (Context-Aware, with market context prompts): F1 89.5% ± 13.2%
- TCA (Temporal Context-Aware): F1 86.5% ± 6.9%

**Event-sampled dataset (Eb, ~40,000 tweets 2015–2023 excluding 2020):**
- CA model: F1 80.3% ± 0.2%
- TCA model: F1 71.0% ± 1.4%

**Backtesting performance (Table 3, source-reported Sharpe ratios):**

| Regime | Strategy | Daily Return | Sharpe | Sortino | Max DD | Win Rate |
|---|---|---|---|---|---|---|
| Bullish (2017–2018) | Majority TBL | 7.86% | 5.07 | 8.42 | 20.92% | 84.84% |
| Bullish | Buy & Hold | 3.38% | 3.12 | 4.52 | 35.36% | — |
| Neutral (mid-2019–mid-2020) | Mean TBL | 2.81% | 3.73 | 6.17 | 25.67% | 77.77% |
| Neutral | Buy & Hold | 0.04% | 0.58 | 0.69 | 63.97% | — |
| Bearish (2018–2019) | Majority TBL | 3.72% | 4.70 | 7.62 | 33.77% | 72.05% |
| Bearish | Sell & Hold | 0.19% | 1.26 | 1.77 | 26.45% | — |

- TBL strategy trades 33–84 times per 6–12 month period with average trade durations of 2–5 days.
- In-Out-Long strategy: highest daily return (10.88%) in bullish regime but poor in bearish (0.43%).
- In-Out-Short strategy: highest win rate (93.33%) in bearish regime.
- Out-of-sample check: January 2021 (first month after training, bullish): Majority TBL Sharpe 4.43, Mean TBL Sharpe 3.49.

**Ablation (context components):**
- Removing previous label from prompts: accuracy drops to 43.6%
- Removing RSI: accuracy 79.0%
- Removing ROC: accuracy 78.8%

**Misclassification analysis:** Only 5.1% of Bullish labels misclassified as Bearish; 12.5% of Bearish misclassified as Bullish. Most errors are Bullish/Bearish → Neutral (conservative failure mode).

**Baseline comparisons (Table 2):**
- Base-3 (LSTM, inspired by PreBit): F1 49.20%
- Base-4 (Autoencoder, inspired by Zha et al.): F1 50.01%
- Fusion model (sentiment + price): F1 55.94%
- Majority CA (proposed): F1 54.21% (OVR); 86.12% (OVO bullish), 82.62% (OVO bearish)

### Independently reproduced

Not independently reproduced. All figures are direct extractions from Moradi-Kamali et al. (arXiv:2502.14897v2).

### Negative evidence

- The TCA (Temporal Context-Aware) model shows signs of overfitting: F1 drops from 86.5% (Ea) to 71.0% (Eb), suggesting temporal features may not generalize.
- High standard deviations in CA model performance (±13.2% F1 on Ea) indicate sensitivity to data splits.
- The extremely high Sharpe ratios (5.07, 4.70) are suspicious and likely reflect: (a) no transaction costs, (b) no slippage/spread, (c) potential overfitting to the specific 2017–2020 sample, (d) the labeling process itself being optimized on the same data used for backtesting (barrier factors Fu, Fl, Vt optimized per 6-month period to maximize Sharpe).
- The paper acknowledges that "the association between specific textual patterns and market trends may be transient, requiring frequent model updates."
- The paper acknowledges that "reducing numerical features to categorical prompts may lose some of the fine-grained details critical for identifying complex patterns."
- The bullish regime test period (2017–2018) coincides with one of Bitcoin's most extreme bull runs (+1200%), which is unlikely to recur and may inflate Sharpe ratios.
- No risk-free rate adjustment beyond the 4% annual rate used in Sharpe calculation.
- Only tested on Bitcoin; no evidence of portability to altcoins or other crypto assets.

None identified in the reviewed sources beyond the above; absence is not evidence of no negative result.

## Falsification plan

1. **Out-of-sample replication:** Replicate the full pipeline on a post-2023 Bitcoin dataset with tweet data from X/Twitter, using the same model architecture and hyperparameters. Required sample: ≥12 months of daily data covering at least one regime transition.
2. **Transaction cost stress test:** Re-run backtests with realistic taker fees (10–15 bps round-trip), slippage (1–5 bps), and spread costs. Failure threshold: Sharpe ratio drops below 1.5 after costs.
3. **Parameter perturbation:** Vary barrier factors (Fu, Fl) by ±20% from optimized values and re-evaluate. If Sharpe degrades by >50%, the strategy is overfit to barrier calibration.
4. **Alternative universe:** Test on ETH/USD tweets and price data. If the mechanism is generalizable to crypto sentiment, it should produce positive (though potentially weaker) results on ETH.
5. **Labeling ablation:** Compare market-derived TBL labels against: (a) simple next-day return labels, (b) human-annotated sentiment labels, (c) random labels. If TBL does not materially outperform (a), the labeling innovation is not the source of alpha.
6. **Temporal stability:** Test whether the model maintains performance when retrained on a rolling 6-month window and evaluated on the subsequent 6 months (walk-forward). If performance degrades sharply, the text-market association is transient.
7. **Failure metric:** If out-of-sample Sharpe < 1.0 after transaction costs, the strategy is rejected for live deployment.

## Crypto portability

**Adapted.** The paper is natively crypto-focused (Bitcoin tweets → BTC trading signals). However, several portability considerations apply:

- **Spot vs. perpetual:** The paper tests on spot BTC only. For perpetual futures, funding rate dynamics and leverage effects are not modeled and could either enhance or erode the signal.
- **Venue fragmentation:** Tweet sentiment may not be uniformly distributed across trading venues; the paper does not model venue-specific order flow.
- **24/7 session structure:** The daily aggregation frequency aligns with crypto's continuous trading, but tweet volume and quality may vary by time zone and session.
- **Liquidity:** BTC spot is sufficiently liquid for this strategy's frequency, but altcoin adaptation would face liquidity constraints.
- **Data dependency:** The strategy requires real-time access to Twitter/X data, which has become increasingly restricted and costly since the paper's submission. This is a material execution risk.
- **Mark/index price:** Not applicable for spot strategy.

## Limitations

- **Preprint, not peer-reviewed:** The paper has not undergone formal peer review.
- **No transaction cost modeling:** The most critical limitation. High Sharpe ratios (5.07, 4.70) are gross of all costs. Net-of-cost performance is unknown and could be substantially worse.
- **Potential overfitting:** Barrier factors (Fu, Fl, Vt) are optimized per 6-month period using Sharpe ratio as the objective function, using the same data period. This is a form of in-sample optimization that inflates backtest performance.
- **Narrow sample period:** Backtesting covers 2017–2020, which includes an extreme bull run (+1200%) and a severe bear market. Generalizability to other regimes is unproven.
- **Single-asset test:** Only Bitcoin is tested. No cross-sectional or multi-asset evidence.
- **Data access risk:** Twitter/X data access has become restricted and costly since the paper's submission (2025). The tweet collection pipeline may not be reproducible without paid API access.
- **High variance in model performance:** CA model F1 ranges from 76.3% to 90.3% across folds (±13.2%), suggesting instability.
- **No live or paper-trading validation:** All results are backtested only.
- **Conservative misclassification but still material:** 5.1% Bullish→Bearish misclassification could produce significant drawdowns during adverse periods.
- **Labeling window overlap:** The TBL vertical barrier (8–15 days) overlaps with the daily signal aggregation, creating potential label leakage between consecutive prediction windows. The paper does not address this explicitly.

## Implementation status

Not implemented. This is a research-only capture of a sentiment-based trading strategy for Bitcoin. No implementation in our research stack (PyBroker, Nautilus, or otherwise) has been attempted. The GitHub repository (https://github.com/hamidm21/Revisit_FSA) exists but has not been evaluated or verified.

## Adoption boundary

This record is research material only. Its presence in this repository does not mean:
- The strategy is profitable
- The high Sharpe ratios are reliable or reproducible
- The strategy has been validated for implementation
- The strategy is approved for paper trading, testnet, or live trading
- Transaction costs have been accounted for

The extremely high reported Sharpe ratios (5.07, 4.70) should be treated with significant skepticism until independently reproduced with realistic cost assumptions.

## Related Wiki records

- `[[quant/llm-news-sentiment-direct-rl-crypto-trading-ddqn-grpo-2026-09-06]]` — Related in using LLM-derived sentiment for crypto trading, but uses a fundamentally different approach (RL-based DDQN/GRPO with news sentiment scores as state features, not tweet classification with market-derived labels).
- `[[quant/crypto-macro-sentiment-contrarian-fear-greed-ema-2026-09-03]]` — Related in sentiment-based crypto signals, but uses Fear & Greed index with EMA smoothing, not tweet-level classification.
- `[[quant/colas-multimodal-corroboration-latent-asset-signals-crypto-trading-2026-09-04]]` — Related in multimodal crypto signal generation, but uses latent space fusion of market/technical/news/sentiment modalities rather than market-derived tweet labeling.

No structurally similar records exist in the repository. The market-derived labeling + context-aware prompt-tuning approach is novel to this collection.

## Sources

1. Hamid Moradi-Kamali, Mohammad-Hossein Rajabi-Ghozlou, Mahdi Ghazavi, Ali Soltani, Amirreza Sattarzadeh, and Reza Entezari-Maleki, "Market-Derived Financial Sentiment Analysis: Context-Aware Language Models for Crypto Forecasting", arXiv:2502.14897v2 [cs.CE], submitted February 17, 2025; revised March 2, 2025. DOI: 10.48550/arXiv.2502.14897. https://arxiv.org/abs/2502.14897
2. Public GitHub repository: https://github.com/hamidm21/Revisit_FSA
