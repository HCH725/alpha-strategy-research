---
schema: strategy-research-record-v1
title: "Foreign Exchange Macro News Fundamental Momentum via Large Language Model Directional Classification: AIFX Index, Taylor-Rule Anchoring, and Asymmetric News Reaction"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - foreign-exchange
  - macro-momentum
  - large-language-models
  - fundamental-momentum
  - taylor-rule
  - news-sentiment
  - cross-sectional-fx
status: research-only
confidence: high
source_as_of: 2026-08-01
sources:
  - "Amin Izadyar, 'AI and Exchange Rate Predictability', arXiv:2608.00761v1 [q-fin.GN, q-fin.CP, q-fin.PM, q-fin.ST, q-fin.TR], August 1, 2026. DOI: 10.48550/arXiv.2608.00761. https://arxiv.org/abs/2608.00761"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Foreign Exchange Macro News Fundamental Momentum via Large Language Model Directional Classification: AIFX Index, Taylor-Rule Anchoring, and Asymmetric News Reaction

## Provenance

- **Primary Source:** Amin Izadyar (Department of Econometrics and Business Statistics, Monash University), *"AI and Exchange Rate Predictability"*, arXiv preprint `arXiv:2608.00761v1 [q-fin.GN, q-fin.CP, q-fin.PM, q-fin.ST, q-fin.TR]`, published August 1, 2026. DOI: [10.48550/arXiv.2608.00761](https://doi.org/10.48550/arXiv.2608.00761). Full text: [https://arxiv.org/abs/2608.00761](https://arxiv.org/abs/2608.00761).
- **Primary Subject Areas:** General Finance (`q-fin.GN`), Computational Finance (`q-fin.CP`), Portfolio Management (`q-fin.PM`), Statistical Finance (`q-fin.ST`), Trading and Market Microstructure (`q-fin.TR`).
- **Context:** The classical "exchange rate disconnect puzzle" (Meese & Rogoff, 1983) posits that structural macroeconomic fundamentals fail to outperform a random walk in predicting future exchange rate returns. Izadyar revisits this empirical puzzle by leveraging generative large language models (LLMs; GPT-4o and DeepSeek-V3) to interpret structured numerical economic calendar releases (realized, consensus forecast, and prior values across 544 indicators from 1996 to 2024, 174,820 releases from Investing.com) without temporal metadata. The model constructs a monthly fundamental sentiment index (AIFX) that yields an annualized Sharpe ratio exceeding 0.70 in cross-sectional G-10 currency trading, generating significant alpha orthogonal to benchmark FX factors.

## Economic mechanism

### Source-reported

1. **Taylor-Rule Monetary Policy Link:** Exchange rates are connected to macroeconomic fundamentals through central bank monetary policy reaction functions (Taylor, 1993; Clarida & Waldman, 2007; Engel & Wu, 2024). Economic data surprises in Inflation, Employment, and Broad Economic Activity dictate expected future policy interest rates and yield differentials.
2. **Asymmetric News Diffusion & Market Reaction:** Negative economic surprises (signaling economic contraction and currency depreciation) trigger rapid, immediate spot market re-pricing. Conversely, positive economic surprises (signaling expansion and potential rate hikes) exhibit delayed, under-reacting price discovery over multi-month horizons.
3. **Monetary Policy Inertia & Political Economy Bias:** Central banks respond swiftly and aggressively to negative output gaps by cutting rates, but exhibit caution, gradualism, and political friction when tightening policy (rate hikes are politically unpopular and slow growth). Consequently, positive surprises create persistent multi-month drift (fundamental momentum), whereas negative surprises are fully absorbed upon release.

### Research interpretation

The falsifiable thesis is that **cross-sectional differences in accumulated positive macroeconomic surprises generate persistent multi-month foreign exchange excess returns due to central bank rate-hiking inertia and delayed market under-reaction to positive fundamentals**:
- Traditional macro models fail because they enforce symmetric linear responses across positive and negative surprises and ignore unstructured indicator heterogeneity.
- Zero-shot LLM reasoning resolves non-linear economic indicator context without overfitting or memorization, converting heterogeneous calendar surprises into a normalized cross-sectional fundamental momentum signal.

## Signal

### 1. Zero-Shot LLM Directional Classification

For each economic release $k$ associated with currency $c$ occurring at time $t$:
- **Input Prompt:** Strictly contains `{Headline, Actual, Forecast, Previous, Currency}`. Date, time, and historical price movements are excluded to prevent look-ahead contamination.
- **LLM Output:**
  $$\mathrm{LLM}(\text{Prompt}_k) \to \{\text{Analysis: }\dots, \text{ Direction: } d_k\}$$
  where $d_k \in \{\text{STRENGTHEN}, \text{WEAKEN}, \text{INSIGNIFICANT OR UNCERTAIN}\}$.
- **Classification Categories:**
  - Positive news ($N^{\mathrm{pos}}$): $d_k = \text{STRENGTHEN}$.
  - Negative news ($N^{\mathrm{neg}}$): $d_k = \text{WEAKEN}$.
  - Neutral news ($N^{\mathrm{neutral}}$): $d_k = \text{INSIGNIFICANT OR UNCERTAIN}$.

### 2. AIFX Index Construction

Over a rolling lookback window $\tau \in [1, 60]$ months prior to month-end $t$:
$$\mathrm{Strength}_{c,t,\tau} = \frac{N_{c,t,\tau}^{\mathrm{pos}}}{N_{c,t,\tau}^{\mathrm{total}}}$$
$$\mathrm{Weakness}_{c,t,\tau} = \frac{N_{c,t,\tau}^{\mathrm{neg}}}{N_{c,t,\tau}^{\mathrm{total}}}$$
$$\mathrm{AIFX}_{c,t,\tau} = \mathrm{Strength}_{c,t,\tau} - \mathrm{Weakness}_{c,t,\tau} = \frac{N_{c,t,\tau}^{\mathrm{pos}} - N_{c,t,\tau}^{\mathrm{neg}}}{N_{c,t,\tau}^{\mathrm{total}}}$$
where $N_{c,t,\tau}^{\mathrm{total}} = N_{c,t,\tau}^{\mathrm{pos}} + N_{c,t,\tau}^{\mathrm{neg}} + N_{c,t,\tau}^{\mathrm{neutral}}$.

- **Weighted AIFX Variant:** Prompts the LLM to score potential impact magnitude $w_k \in [1, 100]$:
  $$\mathrm{AIFX}_{c,t,\tau}^{\mathrm{weighted}} = \frac{\sum_{k \in \mathrm{pos}} w_k - \sum_{k \in \mathrm{neg}} w_k}{\sum_{k \in \mathrm{total}} w_k}$$

### 3. Portfolio Allocation & Rebalancing Rules

- **Cross-Sectional AIFX Strategy:**
  - At the end of each calendar month $t$, rank all available G-10 currencies by $\mathrm{AIFX}_{c,t,\tau}$.
  - Form an equal-weighted long portfolio in the top 2 highest-ranked currencies.
  - Form an equal-weighted short portfolio in the bottom 2 lowest-ranked currencies.
  - Dollar-neutral by construction.
  - Hold positions for 1 month ($t$ to $t+1$), rebalancing on the final business day of each month.
- **Time-Series Strategy Variant:**
  - Define $\Delta\mathrm{AIFX}_{c,t,\tau} = \mathrm{AIFX}_{c,t,\tau} - \mathrm{AIFX}_{\mathrm{US},t,\tau}$.
  - Allocate $+1/N$ long if $\Delta\mathrm{AIFX} > 0$, and $-1/N$ short if $\Delta\mathrm{AIFX} < 0$.

## Required data

- **Universe:** G-10 Currencies: United States Dollar (USD), Euro (EUR), Japanese Yen (JPY), British Pound (GBP), Swiss Franc (CHF), Canadian Dollar (CAD), Australian Dollar (AUD), New Zealand Dollar (NZD), Swedish Krona (SEK), Norwegian Krone (NOK). (9 cross-sectional currency pairs vs. USD).
- **Macroeconomic Calendar Data:** Investing.com economic calendar (January 1996 to October 2024; 174,820 data points across 544 unique economic indicators).
- **FX Spot & Forward Rates:** End-of-day (London fix 16:00 UTC) spot exchange rates and 1-month forward rates from Bloomberg.
- **Point-in-Time Integrity:** Macro calendar values recorded at release timestamp; no subsequent benchmark revisions ingested.

## Execution assumptions

- **Instruments:** 1-month forward contracts or spot positions with 1-month forward roll overlay.
- **Execution Timing:** Rebalanced monthly at month-end London fix.
- **Friction & Spreads:** G-10 foreign exchange forward markets possess extreme depth; typical institutional bid-ask spreads are $0.5\text{--}2.0$ bps. With monthly turnover across 4 positions, transaction drag is modest ($\approx 5\text{--}15$ bps per annum).
- **Capacity:** Multi-billion dollar institutional capacity due to the $7.5\text{+ trillion}$ daily G-10 FX turnover.

## Evidence

### Source-reported

All figures trace directly to Izadyar (arXiv:2608.00761v1, Sections 4–6, Figures 1–6, Tables 1–4, and Appendix A):

1. **Cross-Sectional Strategy Performance:**
   - The AIFX cross-sectional strategy generates an **annualized Sharpe ratio exceeding 0.70** across intermediate and long lookbacks ($\tau \in [36, 60]$ months), with monotonic positive cumulative returns over 1996–2024.
2. **Orthogonal Factor Alpha (48-Month Lookback):**
   - Contemporaneous regression against 5 benchmark currency risk factors:
     $$RX_t = \alpha + \beta_1 \mathrm{Dollar}_t + \beta_2 \mathrm{DollarCarry}_t + \beta_3 \mathrm{Carry}_t + \beta_4 \mathrm{Mom}_t + \beta_5 \mathrm{Value}_t + \epsilon_t$$
   - Estimated **$\alpha$ accounts for 74% of the strategy's average excess return** ($p < 0.05$), demonstrating that the return is not explained by traditional carry, momentum, or value premiums.
3. **Panel Regression Significance:**
   - Panel regression with time fixed effects ($R_{c,t+1} = \alpha_t + \beta \mathrm{AIFX}_{c,t,\tau} + \epsilon_{c,t+1}$) yields statistically significant positive $t$-statistics for $\beta$ across lookback windows from 1 to 60 months ($t > 2.0$ peaking at $\tau \in [36, 48]$).
4. **Robustness across LLM Backbones:**
   - Replicating the entire pipeline with **DeepSeek-V3** produces Sharpe ratios and cumulative return profiles virtually indistinguishable from GPT-4o.
   - **Weighted AIFX** further enhances Sharpe ratios across almost all lookback windows.
5. **Look-Ahead Bias & Memorization Controls:**
   - *Guess the Year Test:* LLMs prompted with the same data headlines guessed the release year correctly only **5.6% of the time** on average (consistent with random guessing across the 28-year sample).
   - *Knowledge Cut-Off DiD:* Difference-in-differences between GPT-4o (cut-off Oct 2023) and GPT-3.5 (cut-off Sep 2021) shows no performance discontinuity across the 2021–2023 out-of-sample window.
   - *Pure Hindsight Portfolio:* Return of AIFX strategy is statistically orthogonal to an empirical hindsight memory factor.
6. **Underlying Driver Decomposition:**
   - Predictive power is concentrated in **Inflation, Employment, and Broad Economic Activity** indicators.
   - When decomposed into positive vs. negative news, **the predictive signal is overwhelmingly driven by the Strength ratio (positive news)**, while the Weakness ratio shows negligible multi-month predictive power.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- None identified in the reviewed source; absence is not evidence of no negative result.
- However, at very long lookbacks ($\tau \ge 54\text{ months}$), the orthogonal alpha becomes only marginally significant as the traditional 5-year Value factor gains explanatory power.

## Falsification plan

1. **Permuted / Inverted Signal Placebo Test:** Invert the LLM directional label ($STRENGTHEN \leftrightarrow WEAKEN$). If the inverted strategy fails to produce a statistically significant negative Sharpe ratio ($\mathrm{SR} < -0.60$), the baseline performance is attributable to sample drift rather than true fundamental informativeness.
2. **Surprise Threshold Ablation:** Replace LLM reasoning with a simple sign rule on standardized surprise $S = (\text{Actual} - \text{Forecast}) / \sigma$. If raw standard surprise matching achieves equal or superior Sharpe ratio and orthogonal alpha, the LLM semantic reasoning adds zero incremental value over classical econometric surprise scoring.
3. **Out-of-Sample Forward Audit (2024–2027):** Evaluate the strategy on live forward calendar releases from November 2024 onwards. If annualized Sharpe drops below $0.20$ over a 24-month live testing period, reject the hypothesis of persistent Taylor-rule fundamental momentum.

## Crypto portability

**Portability Status:** `adapted` / `unproven`.

- **Mechanism Portability:** Sovereign Taylor rules (interest rate targets driven by national inflation and employment) do not directly apply to cryptocurrency tokens. However, the conceptual framework—*accumulated fundamental news surprise momentum driven by asymmetric protocol adjustments*—can be ported to crypto fundamentals.
- **Adaptation Requirements:**
  - *Data Stream:* Replace macroeconomic indicators with protocol-level fundamental events: Token Terminal metrics (protocol revenue, fee generation, treasury changes, daily active users vs. consensus forecast), major governance votes, staking yield changes, and token emission/unlock announcements.
  - *Prompt Structure:* Prompt LLMs to evaluate whether a protocol metric release or upgrade implies token supply/demand STRENGTHEN, WEAKEN, or NEUTRAL.
  - *Universe:* Top 20 liquid Layer 1 / Layer 2 / DeFi tokens traded on perpetual futures markets.
- **Portability Risks:** Crypto markets are heavily dominated by Bitcoin market-wide beta, leverage cascades, and speculative narrative cycles; fundamental surprises may have shorter half-lives or lower signal-to-noise ratios compared to institutional G-10 sovereign currency flows.

## Limitations

- **API Cost & Latency:** Generating zero-shot LLM evaluations over hundreds of thousands of historical releases requires substantial API token budgets.
- **Calendar Data Dependency:** Relies on third-party calendar aggregator (Investing.com) consensus forecasts, which may be sparse or revised for smaller economies.
- **Lookback Length:** Optimal performance requires long lookback windows ($36\text{--}60$ months), limiting responsiveness to sudden macroeconomic structural breaks (e.g., regime shifts in globalization or central bank policy frameworks).

## Implementation status

`not-implemented`

No implementation has been conducted in the local research repository, PyBroker, NautilusTrader, paper, testnet, or live trading systems.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`

This record is an upstream research capture. It does not authorize strategy implementation, backtesting promotion, or production deployment.

## Related Wiki records

- `[[foreign-exchange-spatiotemporal-graph-statistical-arbitrage-2026-09-02]]`
- `[[retail-agent-structured-adverse-timing-contrarian-alpha-2026-09-02]]`
- `[[loop-gain-matrix-letf-rebalancing-crypto-closing-pressure-2026-09-02]]`

## Sources

- Amin Izadyar, *"AI and Exchange Rate Predictability"*, arXiv preprint `arXiv:2608.00761v1 [q-fin.GN, q-fin.CP, q-fin.PM, q-fin.ST, q-fin.TR]`, submitted August 1, 2026. DOI: `10.48550/arXiv.2608.00761`. URL: [https://arxiv.org/abs/2608.00761](https://arxiv.org/abs/2608.00761).
