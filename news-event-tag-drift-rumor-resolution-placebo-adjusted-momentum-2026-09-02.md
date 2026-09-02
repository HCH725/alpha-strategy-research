---
schema: strategy-research-record-v1
title: "News Event-Tag Drift and Rumor Resolution: Placebo-Adjusted Abnormal Return Dynamics across Quantified Disclosures and Narrative Overreaction"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - nlp
  - llm
  - active-learning
  - event-driven
  - news-alpha
  - post-earnings-announcement-drift
  - rumor-trading
  - market-efficiency
status: research-only
confidence: high
source_as_of: 2026-08-14
sources:
  - "Alireza Kargarzadeh, Nariman Khaledian, Navid Parvini, Subhrangshu Ghatak, and Arman Khaledian, 'Buy the Rumor, Sell the News: When Is News Priced In?', arXiv:2608.14014v1 [cs.AI, cs.LG, q-fin.ST], August 14, 2026. DOI: 10.48550/arXiv.2608.14014. https://arxiv.org/abs/2608.14014"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# News Event-Tag Drift and Rumor Resolution: Placebo-Adjusted Abnormal Return Dynamics across Quantified Disclosures and Narrative Overreaction

## Provenance

- **Authors:** Alireza Kargarzadeh (`alireza.kargarzadeh@tailstate.ai`), Nariman Khaledian (`khaledian.nariman@gmail.com`), Navid Parvini (`navid.parvini@zanista.ai`), Subhrangshu Ghatak (`s.ghatak@increasealpha.com`), and Arman Khaledian (`arman.khaledian@zanista.ai`)
- **Title:** "Buy the Rumor, Sell the News: When Is News Priced In?"
- **Identifier:** arXiv:2608.14014v1 [cs.AI, cs.LG, q-fin.ST]
- **Submission Date:** August 14, 2026
- **DOI:** [10.48550/arXiv.2608.14014](https://doi.org/10.48550/arXiv.2608.14014)
- **Stable URL:** https://arxiv.org/abs/2608.14014
- **Full Text HTML:** https://arxiv.org/html/2608.14014v1
- **License:** arXiv.org perpetual non-exclusive license
- **Data Universe:** 4.57 million financial news articles covering approximately 3,000 U.S.-listed stocks (with 2,591 tradeable symbols having daily price history) from 2023 to 2026, extracted from the NewsWitch commercial crawler (>70 million raw crawled articles). The event study evaluates 1,681,657 scored (stock, trading day, tag) events, comprising 1,317,252 signed events and 364,405 neutral-sentiment placebo events.

## Economic mechanism

### Source-reported

Two longstanding market axioms state:
1. "News is already priced in by the time it is published."
2. "Buy the rumor, sell the news."

Both assertions hypothesize that the market's price adjustment precedes and completes at publication, rather than initiating upon publication. The authors empirically test these claims at scale by deploying an active-learning-distilled transformer tagger and an embedding-based story clusterer, accompanied by a neutral-sentiment placebo control group.

The findings establish two core economic mechanisms:
1. **Anticipation and Rumor Absorption:** The price move connected to a news event concentrates heavily prior to and on publication day. For signed rumor-flagged events, the entire abnormal return occurs on the rumor date; subsequent official confirmation produces zero marginal move (+0.01%) and undergoes subsequent drift reversal (-0.06%).
2. **Cognitive Processing Duality (Numbers vs. Stories):** Markets exhibit a structural divergence in information processing:
   - **Quantified Fundamental Disclosures** (earnings, dividends, guidance, analyst revisions): Suffer from institutional underreaction and slow information dissemination, generating positive post-announcement drift that persists for weeks.
   - **Soft Narrative Stories** (product launches, macro commentaries, leadership shifts, competitive chatter): Suffer from attention-driven retail overreaction and speculative overshooting, resulting in subsequent multi-week mean reversion.
3. **Information Uncertainty Resolution (Second Moment):** News carries "width" (volatility) as well as direction. Media attention inflates volatility prior to publication day; publication resolves uncertainty, causing realized volatility to drop to 0.86 of its historical EWMA forecast immediately post-publication.

### Research interpretation

The strategy operationalizes an event-driven cross-sectional equity overlay:
- **Placebo-Adjusted Residual Signal:** Raw news drift is contaminated by a pervasive background drift: stocks covered in the news trail the single-beta market benchmark by $-0.34\%$ to $-0.92\%$ per month regardless of news direction. Naive strategies that fade positive news in small caps mistakenly attribute this $-0.92\%$ structural benchmark drag to "sentiment reversal." By demeaning raw abnormal returns against a neutral-sentiment placebo baseline ($b_{k,w}$), genuine directional alpha separates from non-directional coverage bias.
- **Dual-Book Implementation:**
  - **Fundamental Long/Short Continuation Leg:** Long stocks with positive quantified disclosures (earnings, capital returns) and short stocks with negative quantified disclosures from Day +6 to Day +20.
  - **Narrative Overreaction Reversal Leg:** Short stocks with positive soft story-driven coverage (promotional product launches, speculative PR) and long negative narrative stories from Day +6 to Day +20.
  - **Pre-Confirmation Rumor Liquidation:** Take profit immediately on the rumor date; never buy the confirmation date.

## Signal

### Formation timestamp & cadence
- **Article Ingestion:** Continuous throughout the trading day. Articles published after 16:00 New York time (market close) roll to trading day $t+1$.
- **Signal Formation:** Formed at the daily close ($t$).
- **Holding Period:** Positions enter at the close of trading day $t+5$ and exit at the close of trading day $t+20$ (a 15-trading-day holding window).

### Tagging & distillation architecture
1. **Teacher LLM:** `gpt-5-mini` hosted on Azure evaluates article title, body, and metadata using a frozen JSON schema. It assigns one of 17 mutually exclusive event tags and 5 binary attributes:
   - **Event Tags (17):** Real corporate events (earnings, guidance, analyst actions, capital returns, launches, partnerships, M&A, legal/regulatory, leadership, operations, macro, competition, credit/debt, insider trades, offerings) plus two dedicated sink categories (`price commentary` and `promotional content`) to prevent false categorization.
   - **Binary Attributes (5):** `scheduled`, `forward looking`, `primary source`, `quantified`, `rumor`.
2. **Distilled Student Classifier:** An 82M-parameter `distilroberta-base` model with 7 task heads (primary tag, secondary tag, 5 binary attributes) trained on 129,463 active-learning-selected teacher labels. It achieves:
   - 87.5% overall tag agreement with the teacher (94.0% agreement at confidence $\ge 0.80$, covering 85% of articles).
   - 92%–99% attribute agreement.
   - High inference throughput: 125–160 articles/second on consumer silicon (Apple M4 Pro).

### Story clustering & event definition
- **Intra-Day Clustering:** Articles for stock $s$ on day $t$ sharing the same primary tag are clustered using cosine similarity of title-and-summary embeddings (threshold $\ge 0.80$).
- **Inter-Day Story Matching:** New clusters are matched against the running story centroid. A story remains active for a tag-dependent lifespan (e.g., M&A and legal up to 90 days, leadership/operations up to 14–28 days, commentary 2 days).
- **First Report vs. Follow-Up:** Flags articles as first reports (`NEW`) or follow-up coverage (`REPEAT`). Over 55% of all articles are follow-ups.
- **Event Sentiment:** Aggregates vendor article sentiment across 5 levels $[-2, -1, 0, +1, +2]$. An event is signed if the average is non-zero ($s \in \{-1, +1\}$), and neutral if all constituent articles are Neutral.

### Return measurement & placebo calibration
- **Abnormal Return ($AR_t$):** Beta-adjusted daily return against the S&P 500 ETF (SPY):
  $$AR_{s,t} = r_{s,t} - \beta_{s,t} r_{\text{SPY}, t}$$
  where $\beta_{s,t}$ is the rolling 252-day OLS market beta (minimum 126 days; default 1.0 if missing).
- **Size Bucketing ($k$):** Stocks partitioned annually into three equal-sized terciles by dollar volume: Small, Mid, Large.
- **Placebo Baseline ($b_{k,w}$):** Mean abnormal return of neutral-sentiment events within size bucket $k$ over event window $w$ (e.g., days $+6 \dots +20$).
- **Adjusted Abnormal Return:** The signed directional excess return net of the coverage baseline:
  $$\widetilde{AR}_{s,w} = s_s \cdot \left( AR_{s,w} - b_{k,w} \right)$$
  where $s_s \in \{-1, +1\}$ denotes the sentiment direction.

### Trading rules
1. **Quantified Fundamental Continuation Book:**
   - On day $t+5$ post-event for tags `earnings` ($+0.22\%$) and `capital returns` ($+0.35\%$):
     - If sentiment $s = +1$: Long stock $s$, hedge with $-\beta_s$ SPY.
     - If sentiment $s = -1$: Short stock $s$, hedge with $+\beta_s$ SPY.
   - Close position at the market close of day $t+20$.
2. **Narrative Overreaction Fading Book:**
   - On day $t+5$ post-event for soft narrative tags `product launches` ($-0.18\%$), `macro read-throughs` ($-0.34\%$), `leadership` ($-0.18\%$):
     - If sentiment $s = +1$: Short stock $s$, hedge with $+\beta_s$ SPY.
     - If sentiment $s = -1$: Long stock $s$, hedge with $-\beta_s$ SPY.
   - Close position at the market close of day $t+20$.
3. **Rumor Protocol:**
   - If attribute `rumor == 1`: Liquidate existing long positions or exit momentum trades on the day of the rumor. Do NOT enter on subsequent official confirmation dates ($0.00\%$ incremental alpha, $-0.06\%$ post-confirmation drag).

## Required data

- **News Corpus:** 4.57 million deduplicated, financial news articles covering 2,591 US equities from January 2023 to mid-2026.
  - Fields: Article publication timestamp (millisecond precision), source domain, URL, ticker symbol, article title, raw text, LLM summary, vendor sentiment score.
- **Price & Market Data:**
  - Daily closing prices and split/dividend-adjusted returns for 2,591 U.S. equities.
  - S&P 500 ETF (SPY) daily returns for market beta hedging.
  - Daily dollar volume for annual 3-tercile size partitioning.
- **Model Checkpoints & Embeddings:**
  - Embedding model for story clustering (cosine similarity $\ge 0.80$).
  - DistilRoBERTa 82M 7-head classifier weights.

## Execution assumptions

- **Execution Cadence:** Positions rebalanced daily at the market close ($16:00$ ET).
- **Signal-to-Execution Delay:** 5 trading days post-event (Day $+5$ close to Day $+20$ close), eliminating execution latency issues and microstructural bid-ask bouncing on the announcement date.
- **Portfolio Construction:** Market-neutral overlay. Each position consists of the underlying equity leg plus an offsetting market-beta position in SPY.
- **Capital Allocation:** Equal-weight across all active candidate positions on each day.
- **Transaction Costs:** Modeled at flat fees of 0 bps, 10 bps, and 20 bps per side. Borrow availability and locate costs are unmodeled (noted as a critical vulnerability for the short-heavy books).

## Evidence

### Source-reported

All statistics trace directly to Kargarzadeh et al. (arXiv:2608.14014v1, Sections 4.1–5.6, Figures 1–5, Tables 1–6):

1. **Pre-Publication vs. Post-Publication Concentration:**
   - Pooled across all 1,317,252 signed events, the cumulative abnormal move in the news direction reaches **$+0.58\%$** by the close of publication day (Day 0), but ends Day $+20$ at only **$+0.20\%$**.
   - Ratio of Day 0 close to Day $+20$ close is **$2.8$**: by the closing bell of publication day, the market had moved nearly 3 times further than where it settles one month later.
   - Quantified fundamental pre-moves: Earnings $+1.41\%$ pre-event, $+0.42\%$ on Day 0, $-0.05\%$ raw post-event (ratio 1.06). Analyst actions $+1.12\%$ pre-event, $+0.22\%$ on Day 0, $-0.13\%$ raw post-event (ratio 1.20).

2. **Rumor Attribute Dynamics (18,618 Rumor Events):**
   - 94% of rumor-flagged events are followed by an official confirmation event within 60 trading days (median gap: 6 days).
   - Rumor Day Abnormal Return: **$+0.36\%$** in the rumor's direction.
   - Drift between Rumor and Confirmation: **$-0.09\%$**.
   - Confirmation Day Return: **$+0.01\%$** (statistically indistinguishable from zero).
   - Days $+6$ to $+20$ Post-Confirmation Drift: **$-0.06\%$**.
   - M&A Rumors breakdown: **$+0.24\%$** on rumor day, **$-0.32\%$** into confirmation, **$-0.10\%$** on news day, **$-0.37\%$** post-news. "Whoever traded the rumor captured the entire move; whoever bought the confirmation bought the top."

3. **Discovery of the Placebo Background Drift:**
   - Neutral-sentiment news events drift down relative to beta benchmark over Days $+1 \dots +20$:
     - Small-cap neutral events: **$-0.92\%$**
     - Mid-cap neutral events: **$-0.58\%$**
     - Large-cap neutral events: **$-0.34\%$**
   - Completely quiet days (no news in prior 5 days) drift down similarly: Small caps **$-0.74\%$**, Mid caps **$-0.88\%$**, Large caps **$-0.59\%$**.
   - De-biasing effect: In raw data, positive news appears to reverse ($-0.62\%$) and negative news appears to continue ($+0.63\%$). Once the placebo baseline is subtracted, both adjusted drifts become **$0.00\%$ ($p \approx 0.90$)**.

4. **Adjusted Post-Event Drift Map (Days $+6 \dots +20$):**
   - **Quantified Fundamental Continuation:**
     - Capital Returns: **$+0.35\%$** ($p < 0.001$)
     - Earnings: **$+0.22\%$** ($p < 0.001$)
     - Guidance: **$+0.13\%$** ($p < 0.05$)
     - Analyst Actions: **$+0.10\%$** ($p < 0.05$)
     - Survives Benjamini-Hochberg False Discovery Rate (FDR) control at 5%.
   - **Soft Narrative Overreaction Reversal:**
     - Macro Read-Throughs: **$-0.34\%$** ($p < 0.001$)
     - Product Launches: **$-0.18\%$** ($p < 0.05$)
     - Leadership Stories: **$-0.18\%$** ($p < 0.05$)
     - Competition: **$-0.17\%$** ($p < 0.05$)

5. **Calendar-Time Portfolio Backtests (Beta-Hedged Overlays):**
   - **Small-Cap Launch/Partnership Fading Strategy:**
     - Gross Annualized Return: **15.8%**
     - Gross Sharpe Ratio: **1.35**
     - At 20 bps Cost per Side: Net Sharpe **0.77**
   - **CRITICAL FALSIFICATION BENCHMARK:** A strategy that shorts *every* small-cap stock appearing in the news regardless of sentiment (neutral or signed) delivers **15.9%** gross annualized return with an identical Sharpe ratio of **1.35**. The cumulative performance curves lie directly on top of each other.
   - **Legal/Regulatory Continuation Strategy:** Gross Sharpe **0.66**, but net return collapses to zero at 10 bps transaction costs.

6. **Second Moment Uncertainty Resolution:**
   - Post-event realized volatility averages **0.86** of its historical EWMA forecast (0.87 for neutral, 0.86 for signed events).
   - Attention scaling: Days with $\ge 10$ articles move 1.36x normal, versus 1.05x for single-article days.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **The Sentiment Illusion / Background Drift Confound:** The 15.8% gross return (Sharpe 1.35) obtained by fading small-cap positive news is an artifact of the benchmark: shorting *any* covered small-cap stock yields 15.9% (Sharpe 1.35). The sentiment classification contributes $0.00\%$ incremental alpha.
2. **Transaction Cost Vulnerability:** The genuine fundamental drift signals (earnings at $+0.22\%$ over 15 trading days) are economically small. A two-way transaction cost of 10–15 bps plus short locate/borrow fees consumes virtually all gross alpha.
3. **Borrow Constraints in Small Caps:** Both the launch-fading strategy and the neutral small-cap short benchmark are overwhelmingly short-biased books in small-cap equities, where hard-to-borrow fees, short squeezes, and locate availability prevent physical execution.
4. **Alpha Decay Across Sample:** Raw pooled post-news reversal declined by more than half from 2024 ($-0.49\%$) to 2026 ($-0.18\%$), and adjusted pooled drift was zero from 2025 onwards, indicating that market participants and algorithmic systems have rapidly adapted.

## Falsification plan

1. **Short Borrow Cost & Locate Audit:** Re-evaluate the small-cap launch-fading and neutral-short portfolios by incorporating historical borrow fees from Markit/S3 Partners:
   $$\text{Return}_{\text{net}} = \text{Return}_{\text{gross}} - \text{BorrowFee}_{s,t} - \text{Cost}_{\text{trade}}$$
   If net Sharpe ratio drops below 0.3 or borrow costs exceed 500 bps/year on the short leg, the strategy is deemed non-investable.
2. **Multi-Factor Placebo Stress Test:** Replace the single-beta SPY adjustment with a 5-factor Fama-French + Momentum model:
   $$AR_{s,t} = r_{s,t} - (\alpha_s + \beta_{s,1} \text{MKT}_t + \beta_{s,2} \text{SMB}_t + \beta_{s,3} \text{HML}_t + \beta_{s,4} \text{RMW}_t + \beta_{s,5} \text{CMA}_t + \beta_{s,6} \text{UMD}_t)$$
   If the small-cap background drift ($b_{k,w} = -0.92\%$) shrinks to zero, the background drift is confirmed to be an unhedged size/style exposure rather than a publicity premium.
3. **Out-of-Sample Regime Shift Test:** Evaluate the quantified fundamental continuation (earnings $+0.22\%$) on a 2026–2028 out-of-sample forward window. If the cumulative abnormal drift over days $+6 \dots +20$ fails to achieve $t > 1.96$, the post-announcement drift from public web news is confirmed to have fully arbitrated away.
4. **Rumor Pre-Announcement Gap Test:** Test execution of rumor trading using tick-level order book data on announcement timestamps. If the entire $+0.36\%$ move occurs in the first 500 milliseconds, human-scale or daily-close execution is falsified.

## Crypto portability

- **Portability Status:** `adapted` / `unproven`.
- **Structural Differences & Risks:**
  - **Latency & Algorithmic Front-Running:** In crypto, news aggregators (e.g., CryptoPanic, Tree of Alpha, Telegram scrapers, X/Twitter bots) feed sub-second trading bots directly connected to Binance/Bybit API or Solana DEX priority gas auctions (PGA). Daily-close execution has zero applicability; the entire move occurs in milliseconds.
  - **The "Sell the News" Dynamic in Crypto:** Crypto exhibits extreme cases of "buy the rumor, sell the news" around scheduled token unlocks, hard forks, ETF approvals, and mainnet upgrades (e.g., Ethereum Merge, Bitcoin Spot ETF approval). Prices typically rally into the event and dump immediately upon formal confirmation. The finding that confirmation dates yield zero alpha and negative forward drift applies directly as a negative risk control.
  - **Altcoin Background Drift:** Altcoins exhibit a severe structural downward drift relative to Bitcoin (BTC) over medium horizons, analogous to the $-0.92\%$ small-cap equity background drift documented in the paper. An unhedged "altcoin sentiment fade" strategy would simply capture the structural altcoin bleed against BTC.
  - **Lack of Standardized Financial Disclosures:** Unlike SEC 10-Q/10-K filings, crypto "guidance" or "capital returns" (token buybacks, staking rewards) are non-standardized, unregulated, and prone to sybil wash reporting.

## Limitations

1. **Short-Biased Book Feasibility:** High gross Sharpe ratios rely on shorting small-cap stocks, ignoring short borrow costs, locate limits, and catastrophic squeeze risks.
2. **Backfilled Sample Segment:** The 2023 portion (<3% of events) was backfilled retrospectively rather than collected live.
3. **Classifier Label Disagreement:** The distilled DistilRoBERTa model disagreed with the GPT teacher on 12.5% of primary tags, concentrated in junk categories (`price commentary`, `promotional content`).
4. **Daily Price Coarseness:** Use of daily closing prices cannot isolate intraday pre-market and after-hours earnings releases from regular market hours.
5. **Sample Period Regime:** 2023–2026 was a strong mega-cap tech bull market, potentially skewing cross-sectional size interactions.

## Implementation status

- `not-implemented` in our research stack.
- No PyBroker, NautilusTrader, paper trading, testnet, or live trading implementation has been conducted.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`
- This record represents an academic literature research extraction. It does not authorize trading execution or strategy implementation in production systems.

## Related Wiki records

- `[[quant/foreign-exchange-macro-news-fundamental-momentum-llm-taylor-rule-2026-09-02]]`
- `[[quant/lstm-learnable-sector-embeddings-cross-sectional-reversal-2026-09-02]]`
- `[[quant/spxw-0dte-vrp-learning-to-rank-2026-09-01]]`

## Sources

1. Alireza Kargarzadeh, Nariman Khaledian, Navid Parvini, Subhrangshu Ghatak, and Arman Khaledian, *"Buy the Rumor, Sell the News: When Is News Priced In?"*, arXiv preprint `arXiv:2608.14014v1 [cs.AI, cs.LG, q-fin.ST]`, submitted August 14, 2026. DOI: [10.48550/arXiv.2608.14014](https://doi.org/10.48550/arXiv.2608.14014). Full text: [https://arxiv.org/html/2608.14014v1](https://arxiv.org/html/2608.14014v1).
