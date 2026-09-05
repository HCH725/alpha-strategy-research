---
schema: strategy-research-record-v1
title: "LLM News-Enhanced Cross-Sectional Momentum Tilt (Anic et al. 2025)"
created: 2026-09-06
updated: 2026-09-06
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cross-sectional-momentum
  - llm-reasoning
  - textual-analysis
  - news-sentiment
  - portfolio-tilt
  - factor-investing
status: research-only
confidence: medium
source_as_of: 2025-10-30
sources:
  - "Nikolas Anic, Andrea Barbon, Ralf Seiz, Carlo Zarattini. 'ChatGPT in Systematic Investing -- Enhancing Risk-Adjusted Returns with LLMs', arXiv:2510.26228v1 [q-fin.PM, q-fin.PR], October 2025. https://arxiv.org/abs/2510.26228"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# LLM News-Enhanced Cross-Sectional Momentum Tilt

## Provenance

- **Primary Source:** Nikolas Anic (Finreon AG), Andrea Barbon (University of St. Gallen), Ralf Seiz (Finreon AG and University of St. Gallen), Carlo Zarattini (Concretum Group).
- **Paper Title:** *"ChatGPT in Systematic Investing -- Enhancing Risk-Adjusted Returns with LLMs"*
- **Canonical arXiv Identifier:** `arXiv:2510.26228v1 [q-fin.PM, q-fin.PR]`, submitted October 30, 2025.
- **Canonical Stable URLs:**
  - Abstract: [https://arxiv.org/abs/2510.26228](https://arxiv.org/abs/2510.26228)
  - Full Text HTML: [https://arxiv.org/html/2510.26228v1](https://arxiv.org/html/2510.26228v1)
  - PDF: [https://arxiv.org/pdf/2510.26228](https://arxiv.org/pdf/2510.26228)
- **DOI:** [10.48550/arXiv.2510.26228](https://doi.org/10.48550/arXiv.2510.26228)
- **Primary Source Verification:** Full text, tables (Tables 1, 2, 3), and equations were directly inspected from the author-supplied primary LaTeX package (`paper.tex`, `paper.bbl`, `biblio.bib`) extracted from the official arXiv e-print archive. No secondary search snippets, AI aggregator digests, or intermediate summaries were used to extract strategy mechanics or empirical numbers.
- **Deduplication Audit:** A comprehensive repository-wide audit confirmed zero prior records referencing `arXiv:2510.26228`, Nikolas Anic, Andrea Barbon, Ralf Seiz, Carlo Zarattini, or Finreon. Related records in the repository examine LLM event sentiment for contrarian short-horizon signals (`llm-event-aware-sentiment-factor-contrarian-alpha-2026-09-04.md`), PPO weighting of LLM formulaic alphas (`adaptive-alpha-weighting-ppo-llm-generated-alphas-2026-09-05.md`), or standard cross-sectional momentum (`cross-sectional-crypto-momentum-2026-08-31.md`), but none explore prompt-engineered LLM confirmation and exponential weight tilting on top of classical 12-1 cross-sectional equity momentum.

## Economic mechanism

### Source-reported

The study grounds its hypothesis in the classical literature on empirical asset pricing anomalies, specifically information underreaction and delayed price adjustments following firm-specific fundamental disclosures (Jegadeesh & Titman 1993; Bernard & Thomas 1989; Hong & Stein 1999; Chan et al. 1996):

1. **Information processing frictions and momentum persistence:** Traditional 12-minus-1 month cross-sectional momentum profits arise because market participants gradually incorporate firm-level news into equity prices over multi-month horizons. However, historical price momentum alone cannot distinguish between sustained trends backed by genuine fundamental disclosures and price appreciation driven by transitory noise, speculative retail crowding, or exhausted catalysts.
2. **LLM as real-time semantic interpreter:** Large language models (LLMs) possess zero-shot reasoning capabilities to parse unstructured textual news feeds and evaluate whether current firm developments reinforce or contradict existing price trends.
3. **Contextual framing:** When prompted with explicit context that a stock has qualified for a momentum portfolio, the LLM evaluates contemporaneous news specifically for *continuation probability* rather than generic sentiment polarity. This conditions capital allocation toward stocks where fresh information supports trend persistence, while trimming exposure to stocks experiencing news fatigue, negative narrative shifts, or absence of supporting information.

### Research interpretation

The strategy operates as a two-stage hybrid systematic model:

```text
Component 1 (Factor Candidate Screen): 12-1 month cross-sectional return ranking (top 2 deciles of S&P 500)
Component 2 (Semantic Confirmation Gate): LLM news continuation scoring via prompt-engineered ChatGPT 4.0 mini
Component 3 (Selection & Conviction Filter): Top m=50 ranked candidates by LLM score (ties broken by momentum)
Component 4 (Nonlinear Capital Allocation): Exponential weight tilt W_i = E_i * eta^(Score_i) with 15% cap
```

The core falsifiable alpha hypothesis is that conditioning cross-sectional momentum on high-frequency semantic news confirmation dampens momentum crashes, filters out stale or reversing trends, and increases risk-adjusted return without altering the baseline investment universe.

## Signal

The strategy enhances the Carhart/Jegadeesh-Titman 12-month cross-sectional momentum factor using LLM news scores:

### 1. Candidate Universe Formation
- At each month-end date $t$, sort all constituents of the S&P 500 by their past 12-month cumulative total return, skipping the most recent month ($t-12$ to $t-2$, standard 12-1 momentum).
- Select the top two deciles (top 20%, approximately 100 stocks) as the candidate pool for LLM evaluation.

### 2. News Retrieval and Conditioning Window
- For each candidate stock $i$, collect all firm-specific news published between 15:45 NYSE time of business day $t-k$ and 15:45 NYSE time of rebalance date $t$.
- **Lookback parameter ($k$):** $k = 1$ business day (`source-reported` optimal parameter, tested: 1 day, 5 days).
- **News fields:** Title, short summary, publication timestamp (second-level precision), and media outlet from the Stock News API (`source-reported`).
- **Missing news handling:** If no news was published for stock $i$ in the lookback window, assign $\text{LLM\_Score}_i = 0$ (neutral stance, `source-reported`).

### 3. LLM Prompting and Scoring
- **Model:** OpenAI ChatGPT 4.0 mini (static, pre-trained up to October 2023, zero-shot without fine-tuning, `source-reported`).
- **Prompt Architecture:** Basic prompt (`source-reported` optimal, tested: Basic vs Advanced).
  - *Context:* Informs the model that it is constructing a long-only S&P 500 momentum portfolio.
  - *Task:* Model reads headlines and summaries up to 15:45 NYSE time and predicts whether upward momentum will continue over forecast horizon $l = 21$ business days (`source-reported` optimal parameter, tested: 1 day, 21 days).
  - *Output:* Raw probability score $s_i \in [0, 1]$, where 0 indicates momentum will stop or revert, 1 indicates continuation, and intermediate values represent continuation probability.
  - *Normalization:* Linear transformation to $[-1, +1]$:
    $$\text{LLM\_Score}_i = 2 s_i - 1$$
    (`source-reported`).

### 4. Ranking and Portfolio Selection
- Sort candidate stocks descending by normalized $\text{LLM\_Score}_i$.
- **Tie-breaking rule:** If multiple stocks have identical LLM scores, sort them by their original 12-1 momentum return rank (`source-reported`).
- **Selection cutoff ($m$):** Select the top $m$ stocks (`source-reported` optimal: $m = 50$, tested: 25, 50, 75, 100).

### 5. Weighting Scheme and Allocation Tilt
- **Baseline weight ($E_i$):** Market-capitalization weight (value-weighted, `source-reported` optimal, tested: equal vs value).
- **Tilt formulation:**
  $$W_i = E_i \cdot \eta^{\text{LLM\_Score}_i}$$
  where $\eta = 5.0$ (`source-reported` optimal multiplier, tested: 1.25, 2.5, 3.75, 5.0).
- **Weight standardization:** Standardize raw tilted weights to sum to 1:
  $$w_i = \frac{W_i}{\sum_{j=1}^m W_j}$$
- **Diversification constraint ($c$):** Maximum individual stock weight cap of 15% ($w_i \le 0.15$); excess weight is redistributed proportionally across remaining holdings (`source-reported` optimal: $c = \text{True}$, tested: True vs False).

### 6. Operational Classification
- **Lookback window ($k=1$ day):** `source-reported`
- **Holding / forecast horizon ($l=21$ business days / 1 month):** `source-reported`
- **Selection count ($m=50$ stocks):** `source-reported`
- **Prompt type ($\pi = \text{Basic}$):** `source-reported`
- **Initial weighting ($w = \text{Value-weighted}$):** `source-reported`
- **Weight multiplier ($\eta = 5.0$):** `source-reported`
- **Weight constraint ($c = 15\%$ max cap):** `source-reported`
- **Rebalancing frequency ($\tau = \text{Monthly}$):** `source-reported`
- **Order execution timing (16:00 NYSE market close):** `research-proposed` (paper collects news up to 15:45 and assumes end-of-day rebalancing).

## Required data

- **Instrument Universe:** Common equities comprising the S&P 500 index (`source-reported`).
- **Venues:** Primary US equity exchanges (NYSE, NASDAQ) (`source-reported`).
- **Market Type:** Spot / cash equity long-only (`source-reported`).
- **Timeframe & Resolution:**
  - Daily total returns and market capitalization for momentum screening and portfolio accounting (`source-reported`).
  - Minute/second-precision timestamps for financial news articles (`source-reported`).
- **Price Fields:** Daily closing prices, adjusted total returns, and shares outstanding / market cap (`source-reported`).
- **News Fields:** Article headline, short summary body, publication timestamp, source outlet (e.g., Bloomberg, CNBC, Zacks, Motley Fool, The Street, Fox Business) via Stock News API (`source-reported`).
- **Benchmark / Risk-Free Rate:** 3-month US Treasury bill rate from FRED (`source-reported`).
- **Point-in-Time Availability:** News timestamped strictly prior to 15:45 NYSE time on rebalance date $t$. 12-month momentum return calculated over month $t-12$ to $t-2$, excluding the immediate prior month $t-1$ to mitigate 1-month short-term reversal contamination (`source-reported`).
- **Missing Data Handling:** If no news is identified for a candidate stock within lookback $k$, $\text{LLM\_Score}_i = 0$ (`source-reported`).

## Execution assumptions

- **Rebalancing Schedule:** Monthly at month-end trading day (`source-reported`).
- **Signal-to-Order Latency:** News cut off at 15:45 NYSE time; orders placed for execution at 16:00 NYSE close (`research-proposed`).
- **Order Type & Fill Model:** Market-on-Close (MOC) or executed at daily closing price with complete fills (`research-proposed`).
- **Transaction Costs:** Flat 2 basis points (0.0002) per trade deducted from gross portfolio returns based on portfolio turnover (`source-reported`).
- **Slippage and Spread:** Included within the 2 bps conservative institutional equity fee model (`source-reported`).
- **Borrow / Shorting:** Not required; 100% long-only equity portfolio (`source-reported`).
- **Leverage:** Fully invested, 0% cash, no leverage (`source-reported`).
- **Capacity:** High institutional capacity, constrained only by S&P 500 liquidity (`source-reported`).

## Evidence

### Source-reported

All performance statistics below are directly reported by Anic, Barbon, Seiz, and Zarattini (arXiv:2510.26228v1, October 2025), evaluated on daily data net of 2 bps transaction costs:

#### Sample Partitions (Table 1)
- **Full Sample:** October 2019 to March 2025 (1,382 daily observations).
- **Validation Set (In-Sample):** October 2019 to December 2023 (~4 years, 1,070 daily observations).
- **Test Set (Out-of-Sample):** January 2024 to March 2025 (15 months, 312 daily observations).
  - *Strict Pre-training Cut-off Independence:* ChatGPT 4.0 mini was pre-trained up to October 2023; test period starting January 2024 is strictly out-of-sample relative to both market prices and the LLM's pre-training corpus.

#### Hyperparameter Optimization (Table 2)
Selected across 512 candidate parameter combinations using the objective function:
$$U(\theta) = \frac{3}{4}\text{Sharpe}(\theta) - \frac{1}{4}\text{MDD}(\theta)$$
- Optimal tuple: $\tau = \text{Month}, k = 1\text{ day}, l = 21\text{ days}, \pi = \text{Basic}, m = 50, c = \text{True (15\%)}, w = \text{Value-weighted}, \eta = 5.0$.

#### Strategy Performance Metrics (Table 3, net of 2 bps costs)

| Metric | Full Sample: Baseline | Full Sample: LLM-Enhanced | Out-of-Sample: Baseline | Out-of-Sample: LLM-Enhanced |
| :--- | :---: | :---: | :---: | :---: |
| **Sharpe Ratio** (annualized) | 0.57 | **0.69** | 0.79 | **1.06** |
| **Sortino Ratio** (annualized) | 0.54 | **0.69** | 0.93 | **1.28** |
| **Annualized Return** | 0.15 (15%) | **0.18 (18%)** | 0.24 (24%) | **0.30 (30%)** |
| **Annualized Volatility** | 0.26 (26%) | **0.24 (24%)** | 0.24 (24%) | **0.22 (22%)** |
| **Maximum Drawdown** | -0.33 (-33%) | **-0.31 (-31%)** | -0.19 (-19%) | **-0.17 (-17%)** |
| **Annualized Turnover** | 0.62 (62%) | 0.90 (90%) | 0.48 (48%) | 0.80 (80%) |

#### Time-Series Alpha Regression
- Regressing daily excess returns of the LLM-enhanced portfolio on baseline momentum yields an annualized alpha of **3.26%**, with $t\text{-statistic} = 1.763$ ($p\text{-value} = 0.078$, statistically significant at the 10% level; reported in Section 3.3 and LaTeX comments).

#### Ceteris Paribus Perturbation Analysis (Section 3.4 & Figure 4)
- **Rebalancing frequency:** Monthly rebalancing (Sharpe ~1.1) substantially outperforms weekly rebalancing (Sharpe ~0.7) due to turnover-cost drag.
- **News lookback window ($k$):** Expanding from 1 day to 5 days provides negligible Sharpe improvement, confirming news impact decays rapidly.
- **Prompt design ($\pi$):** Basic prompt (Sharpe ~1.1) outperforms Advanced prompt (Sharpe ~0.95), showing complex prompt structures add no incremental edge.
- **Tilt multiplier ($\eta$):** Increasing $\eta$ monotonically improves Sharpe ratio up to the 15% concentration bound.
- **Portfolio size ($m$):** Concentration in $m = 25$ stocks achieves peak Sharpe of ~1.3; performance degrades toward $m = 100$.
- **Weighting scheme ($w$):** Value-weighted baseline yields greater performance improvement than equal-weighted baseline, as large caps have richer news flow.

### Independently reproduced

Not independently reproduced. All metrics reflect direct extractions from the primary source LaTeX text and tables (`arXiv:2510.26228v1`).

### Negative evidence

- **Marginal Statistical Significance of Alpha:** The incremental alpha over baseline momentum is statistically significant only at the 10% level ($t = 1.763, p = 0.078$). At conventional 5% significance ($p < 0.05$), the null hypothesis of zero incremental alpha cannot be rejected.
- **Short Out-of-Sample Horizon:** The test sample spans only 15 months (312 trading days, Jan 2024 – Mar 2025), which coincided with a strong equity bull market driven by large-cap tech. Performance during a sustained bear market or momentum crash has not been observed out-of-sample.
- **Elevated Turnover:** LLM enhancement increases portfolio turnover from 48% to 80% out-of-sample and 62% to 90% full-sample.
- **Failure of Weekly Rebalancing:** Switching to weekly rebalancing collapses the Sharpe ratio from 1.1 to 0.7, demonstrating acute sensitivity to trading frequency and execution costs.
- **Omission of LLM Inference Costs:** The authors do not subtract OpenAI API querying costs (scoring 100 stocks monthly) from the return stream.

## Falsification plan

The following operational tests define pre-declared failure criteria to disconfirm the proposed alpha mechanism:

1. **Transaction Cost Sensitivity Stress Test:**
   - *Protocol:* Re-evaluate the out-of-sample period under varying round-trip transaction costs: 5 bps, 10 bps, 15 bps, and 20 bps.
   - *Decision Rule (`research-defined falsification threshold`):* If net annualized Sharpe ratio of the LLM-enhanced strategy falls below the baseline momentum Sharpe ratio at costs $\le 8$ bps, reject commercial implementability.
2. **Placebo / Shuffled News Null Hypothesis Test:**
   - *Protocol:* Permute news articles cross-sectionally (stock $A$ receives news of stock $B$) or feed scrambled synthetically generated headlines to the LLM.
   - *Decision Rule (`research-defined falsification threshold`):* If the shuffled/placebo news test achieves $\ge 85\%$ of the empirical Sharpe enhancement over baseline momentum, falsify the hypothesis that semantic content provides the edge, attributing gains instead to pseudo-random portfolio sparsification.
3. **Execution Latency / News Cutoff Perturbation:**
   - *Protocol:* Shift the news gathering cutoff from 15:45 to 12:00, 15:00, and next-day open 09:30.
   - *Decision Rule (`research-defined falsification threshold`):* If advancing the cutoff by 45 minutes (to 15:00) erodes $>50\%$ of the Sharpe difference, classify the strategy as an unexecutable latency artifact.
4. **Out-of-Universe Down-Cap Test:**
   - *Protocol:* Apply the strategy to Russell 2000 small-cap equities.
   - *Decision Rule (`research-defined falsification threshold`):* If the strategy fails to produce positive excess return net of small-cap spreads (15–25 bps), confirm the mechanism is strictly confined to news-dense mega-caps.
5. **Momentum Crash Stress Regime:**
   - *Protocol:* Evaluate strategy performance through historical or synthetic market inflection points with sharp momentum reversals.
   - *Decision Rule (`research-defined falsification threshold`):* If maximum drawdown exceeds $1.25\times$ the baseline momentum drawdown during a momentum crash, falsify the risk-reduction claim.

## Crypto portability

**Portability Status:** `adapted` / `unproven`

The primary source examines S&P 500 US equities exclusively. Applying this mechanism to cryptocurrency assets represents a research interpretation and has not been validated in the cited literature:

- **Universe Differences:** The S&P 500 provides a stable, highly liquid, regulated equity universe. A crypto adaptation would require restricting candidates to the top 30–50 liquid perpetuals or spot pairs (e.g., Binance USDT perpetuals) with strict liquidity filters (`research-proposed`).
- **Momentum Horizon Invalidation:** Classical 12-minus-1 month momentum is notoriously weak or non-existent in crypto due to rapid multi-month cyclical regimes. A ported crypto version must adapt lookback windows to 30-day, 60-day, or 90-day momentum (`research-proposed`).
- **News Ecology Fragmentation:** Crypto news does not follow regulated SEC/earnings disclosure calendars. Information is disseminated non-stop via Twitter/X, Discord, Telegram, and specialized crypto portals (CoinDesk, Cointelegraph), which exhibit high noise, bot manipulation, and paid promotions.
- **Continuous 24/7 Trading:** Absence of session close (16:00 NYSE). Rebalancing boundaries must be standardized to UTC midnight (00:00 UTC) (`research-proposed`).
- **Funding Rate Drag:** In perpetual futures, holding long momentum assets during strong bull runs entails paying continuous positive funding fees (often 20–50% annualized), which could easily overpower the 3.26% gross annual alpha.

## Limitations

- **Not Independently Reproduced:** No third-party code release or independent replication exists.
- **Marginal Statistical Significance:** Incremental alpha is statistically weak ($p = 0.078$).
- **Short Out-of-Sample Test Window:** 15 months (Jan 2024 – Mar 2025) across a single macro regime (AI/large-cap tech equity bull market).
- **Model Fragility:** Tested solely on OpenAI ChatGPT 4.0 mini; proprietary API updates may silently alter prompt interpretation and score distribution.
- **API Cost Omission:** LLM querying expenses (1,200 queries/year) are excluded from cost accounting.
- **Universe Restriction:** Limited to S&P 500 constituents; unproven on mid-caps, small-caps, or international equities.
- **Unproven in Digital Assets:** Portability to crypto is speculative.

## Implementation status

`not-implemented`

No implementation of this strategy exists in `nautilus-quant-system`, PyBroker, NautilusTrader, or any internal research repository. No data loaders for Stock News API or OpenAI LLM inference pipelines have been deployed.

## Adoption boundary

This document represents research capture only. Inclusion in this repository does not constitute:
- Validation of persistent alpha
- Approval for production backtesting
- Approval for paper trading
- Approval for testnet deployment
- Approval for live capital deployment

Any progression toward formal historical evaluation in `nautilus-quant-system` requires independent intake review, code implementation, and validation against survivorship-bias-free data.

## Related Wiki records

- `[[quant/cross-sectional-crypto-momentum-2026-08-31]]` — Baseline cross-sectional momentum mechanics and decile sorting.
- `[[quant/crypto-cross-sectional-frog-in-the-pan-momentum-discreteness-2026-08-31]]` — Return path discreteness and momentum persistence.
- `[[quant/llm-event-aware-sentiment-factor-contrarian-alpha-2026-09-04]]` — LLM-driven event extraction and social media sentiment signals.
- `[[quant/adaptive-alpha-weighting-ppo-llm-generated-alphas-2026-09-05]]` — Dynamic RL-based weighting of LLM-generated alpha signals.

## Sources

1. Nikolas Anic, Andrea Barbon, Ralf Seiz, and Carlo Zarattini. *"ChatGPT in Systematic Investing -- Enhancing Risk-Adjusted Returns with LLMs."* arXiv preprint `arXiv:2510.26228v1 [q-fin.PM, q-fin.PR]`, submitted October 30, 2025.
   - Stable Abstract: [https://arxiv.org/abs/2510.26228](https://arxiv.org/abs/2510.26228)
   - Full Text HTML: [https://arxiv.org/html/2510.26228v1](https://arxiv.org/html/2510.26228v1)
   - Full Text PDF: [https://arxiv.org/pdf/2510.26228](https://arxiv.org/pdf/2510.26228)
   - DOI: [10.48550/arXiv.2510.26228](https://doi.org/10.48550/arXiv.2510.26228)
