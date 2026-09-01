---
schema: strategy-research-record-v1
title: "Matched-Filter Order Flow Normalization: Investor-Segmented Signal Extraction"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - order-flow
  - market-microstructure
  - matched-filter
  - signal-processing
  - investor-segmentation
  - cross-sectional-alpha
status: research-only
confidence: medium
source_as_of: 2026-02-20
sources:
  - "Sungwoo Kang, 'Optimal Signal Extraction from Order Flow: A Matched Filter Perspective on Normalization and Market Microstructure', arXiv:2512.18648v3 [q-fin.CP], revised February 20, 2026. https://arxiv.org/abs/2512.18648"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Matched-Filter Order Flow Normalization: Investor-Segmented Signal Extraction

## Provenance

- **Primary Source:** Sungwoo Kang (Korea University), *"Optimal Signal Extraction from Order Flow: A Matched Filter Perspective on Normalization and Market Microstructure"*, arXiv preprint `arXiv:2512.18648v3 [q-fin.CP]`, first submitted December 21, 2025, revised February 20, 2026. URL: https://arxiv.org/abs/2512.18648.
- **Primary Category:** Computational Finance (`q-fin.CP`).
- **Empirical Dataset:** 2,784,812 common stock-day observations from the Korean equity market (KOSPI and KOSDAQ) spanning January 2020 through December 2024, utilizing granular regulatory order flow data segmented by investor type (Domestic Institutional, Foreign Institutional, and Retail/Individual).

## Economic mechanism

### Source-reported

Order flow intensity is widely recognized as a primary carrier of private information and directional inventory pressure in financial markets. However, the standard empirical practice of normalizing order flow by arbitrary denominators (e.g., historical volume, rolling standard deviation, or market capitalization) lacks theoretical grounding and frequently obscures or degrades the underlying predictive signal.

Applying the **Matched Filter Theorem** from signal detection theory—which states that the optimal linear filter maximizing the signal-to-noise ratio (SNR) must match the template of the incoming signal waveform—Kang proves that the optimal normalization operator for order flow must mirror the structural scaling constraints of the underlying market participants:
1. **Capacity-Constrained Institutional Investors ($S^{\text{MC}}$):**
   - Domestic mutual funds, pension funds, and asset managers operate under capital allocation and portfolio weight constraints. Their dollar investment in a stock scales proportionally with the firm's total equity value (Market Capitalization, $\text{MCAP}$).
   - Therefore, normalizing institutional net buying by Market Capitalization ($S^{\text{MC}} = \Delta V_i / \text{MCAP}_i$) constitutes the exact matched filter for detecting fundamental institutional information.
2. **Volume-Targeting Algorithmic Executors ($S^{\text{TV}}$):**
   - Foreign institutional investors and quantitative execution desks possess private directional information but execute via volume-participation algorithms (VWAP, TWAP, or POV percentage-of-volume) to minimize market impact. Their order flow intensity scales directly with the stock's contemporaneous Trading Value ($\text{TV}$).
   - Normalizing foreign net buying by Trading Value ($S^{\text{TV}} = \Delta V_i / \text{TV}_i$) constitutes the matched filter for volume-targeting stealth execution.
3. **The "Informed Executor" Hypothesis:**
   - The paper shows that foreign investors' volume-scaling behavior is not a reflection of uninformative noise, but rather an endogenous footprint of sophisticated execution algorithms concealing informed orders. Mismatching the normalization (e.g., applying $S^{\text{MC}}$ to foreign flow or $S^{\text{TV}}$ to domestic fund flow) attenuates the signal correlation by up to 50%.

### Research interpretation

This mechanism provides a rigorous framework for systematic cross-sectional alpha factor engineering:
1. **Elimination of Preprocessing Arbitrariness:** Replaces heuristic feature engineering with mathematically optimal signal extraction tailored to trader execution topology.
2. **Multi-Channel Flow Decomposition:** Separating raw order flow into distinct investor/execution categories and applying matched normalization filters prevents mutual signal cancellation.
3. **Capacity & Size Heterogeneity:** The signal demonstrates an asymmetric edge in smaller, less liquid names where institutional information asymmetry is highest and algorithmic stealth is constrained.

## Signal

### 1. Investor-Segmented Order Flow Definitions

For each asset $i$ on trading day $t$:
- Let $B_{i, t}^{(k)}$ and $S_{i, t}^{(k)}$ be the total buy and sell trading value (in currency units) executed by investor class $k \in \{\text{Inst}, \text{Foreign}, \text{Retail}\}$.
- Net Buying Value:
  $$\Delta V_{i, t}^{(k)} = B_{i, t}^{(k)} - S_{i, t}^{(k)}$$

### 2. Matched Filter Normalizations

- **Market-Cap Matched Filter ($S^{\text{MC}}$) for Institutional Fund Flow:**
  $$S_{i, t}^{\text{MC}, \text{Inst}} = \frac{\Delta V_{i, t}^{\text{Inst}}}{\text{MCAP}_{i, t-1}}$$
- **Trading-Value Matched Filter ($S^{\text{TV}}$) for Algorithmic Foreign Flow:**
  $$S_{i, t}^{\text{TV}, \text{Foreign}} = \frac{\Delta V_{i, t}^{\text{Foreign}}}{\text{TradingValue}_{i, t}}$$
- **Retail Noise Contrarian Filter ($S^{\text{Retail}}$):**
  $$S_{i, t}^{\text{Retail}} = -\frac{\Delta V_{i, t}^{\text{Retail}}}{\text{TradingValue}_{i, t}}$$

### 3. Composite Cross-Sectional Alpha Signal

Standardize each matched signal cross-sectionally to zero mean and unit variance ($Z(\cdot)$):
$$\alpha_{i, t} = w_1 \cdot Z\left(S_{i, t}^{\text{MC}, \text{Inst}}\right) + w_2 \cdot Z\left(S_{i, t}^{\text{TV}, \text{Foreign}}\right) + w_3 \cdot Z\left(S_{i, t}^{\text{Retail}}\right)$$
where $w_1, w_2 > 0$ and $w_3 \ge 0$.

### 4. Portfolio Construction

- Rank all assets cross-sectionally by $\alpha_{i, t}$ at day $t$ close.
- Form a long-short quintile (Q5 - Q1) or decile portfolio with dollar-neutral, beta-neutral weights:
  $$w_{i, t+1} = \frac{\alpha_{i, t} - \bar{\alpha}_t}{\sum_j |\alpha_{j, t} - \bar{\alpha}_t|}$$
- Rebalance daily at market open $t+1$.

## Required data

- **Instrument Universe:** All actively traded common stocks on KOSPI and KOSDAQ (or equivalent market with categorized broker/investor flow feeds).
- **Venues:** Korea Exchange (KRX) or any market venue publishing regulatory buyer/seller category breakdowns.
- **Timeframe:** Daily aggregated flow and pricing data.
- **Fields:**
  - Net Buying Value by investor category ($\Delta V^{\text{Inst}}$, $\Delta V^{\text{Foreign}}$, $\Delta V^{\text{Retail}}$).
  - Total Daily Trading Value ($\text{TV}_t$).
  - Closing Market Capitalization ($\text{MCAP}_{t-1}$).
  - Daily Opening, Closing, High, Low prices and shares outstanding.
- **Point-in-Time Requirement:** Daily flow and capitalization metrics available after market close $t$; portfolio executed at open $t+1$.

## Execution assumptions

- **Execution Timing:** Next-day market-on-open (MOO) or VWAP over the first 30 minutes.
- **Order Types:** Aggressive market / limit orders at open.
- **Transaction Costs & Slippage:** Standard institutional equity commission (5 bps) + Korean securities transaction tax + bid-ask spread and linear market impact model.
- **Short Selling:** Assumes borrow availability for Q1 short leg (subject to regulatory short-sale restrictions in specific regimes).

## Evidence

### Source-reported

- **Statistical Significance (t-statistics):**
  - In cross-sectional Fama-MacBeth predictive regressions over 2,784,812 stock-days (2020–2024), the matched filter $S^{\text{MC}}$ applied to domestic institutional flow achieves a t-statistic of **$t = 9.65$** for predicting next-day returns.
  - The matched filter $S^{\text{TV}}$ applied to foreign algorithmic flow achieves a t-statistic of **$t = 16.35$** for predicting next-day returns.
  - Mismatched normalizations (e.g., $S^{\text{TV}}$ on domestic institutions or $S^{\text{MC}}$ on foreign flow) result in substantial attenuation of t-statistics and explanatory power.
- **Signal-to-Noise Ratio (SNR) Gain:** Monte Carlo simulations calibrated to market microstructure demonstrate up to **$1.99\times$ improvement in signal correlation** when using the matched normalization versus standard ad-hoc volume filters.
- **Economic Performance & Size Effect:**
  - Long-short decile/quintile portfolios based on the matched composite flow signal yield an annualized **Sharpe ratio of 2.75 in the smallest market-cap quintile**.
  - Performance exhibits a strong small-cap / illiquidity interaction, where informational asymmetry is greatest.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Regulatory Short-Sale Bans:** During periods when regulators ban short selling (e.g., KRX temporary bans), the short leg cannot be fully monetized, reducing net strategy Sharpe.
- **Institutional Reporting Latency:** If broker/investor breakdown data is delayed by the exchange until hours after market close, opening execution may face timestamp synchronization challenges.
- **Large-Cap Alpha Compression:** In Mega-Cap stocks (top 5% market cap), high analyst coverage and aggressive algorithmic arbitrage compress the Sharpe ratio of the signal to $< 0.8$.

## Falsification plan

1. **Matched vs. Mismatched Factor Perturbation Test:** Compare two parallel systematic factor portfolios on out-of-sample data: Portfolio A using matched filters ($S^{\text{MC}}$ for Inst, $S^{\text{TV}}$ for Foreign) vs. Portfolio B using inverted/mismatched filters ($S^{\text{TV}}$ for Inst, $S^{\text{MC}}$ for Foreign).
   - **Failure Rule:** If Portfolio A does not outperform Portfolio B by at least $\Delta \text{Sharpe} \ge 0.40$ ($p < 0.01$), the matched-filter hypothesis is rejected.
2. **Investor Category Placebo Test:** Randomly shuffle investor category labels across stocks daily while preserving aggregate net order flow.
   - **Failure Rule:** If the synthetic shuffled portfolio generates statistically significant positive alpha, the reported result is driven by generic volume/momentum confounding rather than investor segmentation.
3. **Transaction Cost Degradation Test:** Stress-test net returns against increasing round-trip execution costs from 10 bps to 40 bps.
   - **Failure Rule:** If net annual return drops below zero at a round-trip friction of 25 bps, the signal is economically unviable as an alpha strategy.

## Crypto portability

**adapted**

The empirical study is conducted on Korean equity market microstructure where exchange-level investor tags are published. Porting to cryptocurrency markets requires structural adaptation:
- **On-Chain Wallet Entity Labeling:** Public blockchain analytics (e.g., Arkham, Nansen, Glassnode) provide entity-tagged order flow and transfer volumes (e.g., Institutional Custody / Fund wallets vs. Smart Money vs. Retail exchange deposits). Normalizing fund custody wallet flow by total token circulating market cap ($S^{\text{MC}}$) matches the institutional capacity filter.
- **DEX vs. CEX Microstructure:** In perpetual DEXs (e.g., Hyperliquid), large algorithmic traders execute via programmatic TWAP/VWAP sub-accounts. Normalizing taker volume by 24-hour pool turnover ($S^{\text{TV}}$) approximates the algorithmic volume-targeting filter.
- **High Market Impact & Volatility:** Crypto altcoins exhibit significantly wider bid-ask spreads and higher slippage, demanding strict liquidity filtering.

## Limitations

- **Exchange Telemetry Dependency:** Requires granular segmented investor flow data; not directly applicable to opaque anonymous equity exchanges (e.g., US dark pools) without reverse-engineered trade classification.
- **Small-Cap Capacity Limit:** High Sharpe ratios in the smallest quintile are constrained by market capacity and trading volume limits.
- **Model Tuning:** The relative weighting $(w_1, w_2, w_3)$ of investor streams requires periodic recalibration.

## Implementation status

No implementation in our research stack. The record documents published empirical and theoretical findings from Kang (arXiv:2512.18648v3, 2026); no PyBroker, Nautilus, or live trading components have been created.

## Adoption boundary

This record is research material only. Presence in this repository does not mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

## Related Wiki records

- [[quant/crypto-multilevel-order-flow-imbalance-intraday-2026-08-31]] — Multi-level order flow imbalance and microstructure
- [[quant/crypto-world-order-flow-cross-sectional-quintile-weekly-2026-08-31]] — Cross-sectional world order flow alpha factors
- [[quant/crypto-public-wallet-identity-trader-informativeness-adverse-selection-2026-09-02]] — Public wallet identity and adverse selection
- [[quant/passive-market-impact-optimal-execution-mlofi-2026-09-02]] — Passive market impact and optimal execution

## Sources

1. Sungwoo Kang, "Optimal Signal Extraction from Order Flow: A Matched Filter Perspective on Normalization and Market Microstructure", arXiv preprint arXiv:2512.18648v3 [q-fin.CP], first submitted December 21, 2025, revised February 20, 2026. URL: https://arxiv.org/abs/2512.18648.
