---
schema: strategy-research-record-v1
title: "BTQ: Beta-Times-Quantity Factor Pricing Model via Noise-Trader Flow Risk Holdings"
created: 2026-09-07
updated: 2026-09-07
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: "2026-09-04"
sources:
  - "https://arxiv.org/abs/2609.05162v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# BTQ: Beta-Times-Quantity Factor Pricing Model via Noise-Trader Flow Risk Holdings

## Provenance

- **Paper:** Yu An, Yinan Su, and Chen Wang. "Quantity, Risk, and Return." arXiv preprint `arXiv:2609.05162v1 [q-fin.GN]`, submitted 2026-09-04.
- **Primary source URL:** https://arxiv.org/abs/2609.05162v1
- **PDF:** https://arxiv.org/pdf/2609.05162v1
- **Version:** v1 (submitted 2026-09-04)
- **Sample period:** January 2000 – December 2022 (276 months, ~1,644,000 stock-month observations)
- **Universe:** US equities, delisting-adjusted, from CRSP
- **Factors tested:** Fama-French-Carhart (FF3C) factors and 153 Jensen, Kelly, and Pedersen (2023) factors
- **Note:** This is an equity-focused paper. No crypto empirical results are presented.

## Economic mechanism

### Source-reported

The authors propose a two-investor-class model: noise investors (retail) generate large, correlated flows in individual stocks, and sophisticated investors (hedge funds, market makers) absorb these flows, causing fluctuations in their holdings of underlying systematic risks. Sophisticated investors are the marginal price-setters; when they hold more of a factor's risk, they demand higher compensation (higher factor premium). This gives rise to the "beta times quantity" (BTQ) model where expected return depends on both factor exposure (β) and the factor's quantity fluctuations (q) induced by noise trading flows. The mechanism draws from demand-based asset pricing (Gabaix & Koijen 2022) and noise-trader flow literature.

### Research interpretation

The hypothesized alpha channel is: cross-sectional return predictability arises from the interaction between a stock's factor risk exposure and the time-varying quantity of that factor's risk held by sophisticated investors. When retail investors sell a broad group of stocks with high exposure to a systematic factor, sophisticated investors accumulate that risk and demand a higher premium, widening the expected return spread between high-β and low-β stocks. The key parameter λk > 0 implies the risk-return association strengthens when factor quantity is high.

Hypothesized mechanism for potential crypto adaptation: In crypto perpetual markets, retail flow (e.g., leverage demand, directional speculation) could be decomposed into factor-like exposures (e.g., market beta, momentum, volatility) and the quantity of each factor absorbed by informed/institutional participants. If retail speculative flows generate factor-level quantity fluctuations that are absorbed by more sophisticated participants, a BTQ-like interaction could produce cross-sectional or time-series return predictability.

## Signal

- **Formation timestamp:** Monthly. Quantity variables (q) are formed at end of month t using 6-month accumulated flow shocks normalized by lagged total market capitalization. Factor exposures (β) are estimated using 12-month rolling daily returns.
- **Lookback:** q uses 6-month lookback of accumulated factor-level flow shocks. β uses 12-month rolling window of daily returns.
- **Signal construction:**
  1. Estimate stock-level factor exposure: β̂i,k,t = cov_t(ri,t, fk,t) / var_t(fk,t), using 12-month rolling daily returns.
  2. Construct stock-level dollar flows: $flow_i,t = −Σ_m $flow_m,t × weight_i,m,quarter(t)−2 (mutual fund flow-induced trading, FIT method per Coval & Stafford 2007, Froot & Ramadorai 2008, Lou 2012). Two-quarter lagged holding weights.
  3. Aggregate to factor level: flow_k,t^factor = Σ_i $flow_i,t × β̂_i,k,t × var_t(fk,t).
  4. Accumulate and normalize: q̃_k,t = (1/6) Σ_{h'=0}^{5} flow_k,t-h'^factor / total_market_cap_{t-h'-1}.
  5. Standardize: q_k,t = q̃_k,t / σ(q̃_k,t).
- **Trading rule (research-proposed):** Long high-β stocks × high q; short low-β stocks × low q. The BTQ term β_i,k,t × q_k,t serves as the return predictor.
- **Holding period:** Monthly rebalancing.
- **Parameters:** 6-month accumulation window for q, 12-month rolling window for β (both research-defined in the source). Lasso regularization for factor selection when K is large (153 JKP factors).
- **Underspecified:** The paper does not specify a formal long-short portfolio construction or threshold for entry/exit. The BTQ term is used as a return predictor in panel regressions, not as a direct trading signal. Operationalizing this as a tradeable strategy requires defining portfolio construction, sizing, and cost assumptions.

## Required data

- **Instrument:** US equities (CRSP universe)
- **Universe:** All CRSP-listed stocks with delisting adjustment; no explicit liquidity filter stated in source
- **Venue:** US equity markets (CRSP data)
- **Timeframe:** Monthly returns (daily returns for β estimation)
- **Fields:** Stock returns, factor returns (FF3C, 153 JKP factors), mutual fund returns, mutual fund TNA, mutual fund quarterly holdings (Thomson/Refinitiv S12), total US stock market capitalization
- **Point-in-time:** Mutual fund holdings reported with 45-day statutory delay; two-quarter lag used to ensure observability
- **Timestamp:** Monthly frequency, US market conventions
- **Missing-data:** Not explicitly discussed; standard CRSP delisting adjustments applied
- **Funding/fee/spread:** Not modeled in the source (this is a pricing model, not a trading strategy backtest)

## Execution assumptions

- **Signal-to-order timing:** Monthly rebalancing assumed (research-proposed)
- **Next-bar vs same-bar:** Not specified
- **Market / limit order:** Not specified
- **Fill model:** Not specified
- **Fees:** Not specified (source does not model transaction costs)
- **Slippage:** Not specified
- **Impact / capacity:** Not specified
- **Funding:** Not applicable (equity long-only or long-short, no leverage assumed)
- **Leverage:** Not specified
- **Latency:** Not applicable (monthly frequency)
- **Data gap:** The source is a factor pricing model, not a strategy backtest. Execution assumptions are entirely absent. Any operationalization would require specifying all of the above.

## Evidence

### Source-reported

- **Out-of-sample R²:** The BTQ model predicts monthly individual stock returns with OOS R² of approximately 1%, comparable to high-dimensional machine learning models. This is reported across multiple robustness settings (different sample periods, firm size groups, model specifications). (Section 1, Abstract, and Section 4.3)
- **Unconditional SML:** Nearly flat, consistent with prior literature (Black 1972, Frazzini & Pedersen 2014). Conditional on high q, the SML steepens significantly, revealing a positive risk-return association. (Section 4.1, Figure 2)
- **Factor selection:** Lasso from 153 JKP factors selects market factor as most prominent, with additional selected factors including betting-against-beta, volatility, idiosyncratic risk, and value. PCA-based approach selects only first two PCs with equally strong predictive power. (Section 4.4–4.5)
- **Quantity-only model:** No predictive power, confirming that β × q interaction is necessary. (Section 5.1)
- **Alternative channels:** No macroeconomic variables (126 FRED-MD series) can substitute for q in reproducing BTQ's predictive power, supporting the interpretation that quantity is not a facade for other forces. (Section 6)
- **Sample:** 1,644,000 stock-month observations, ~6,000 per month, January 2000–December 2022.
- **Note:** All performance figures are from the source and not independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed sources; absence is not evidence of no negative result.

## Falsification plan

1. **Out-of-sample degradation:** Re-run the BTQ predictive regression on sub-periods (e.g., 2010–2015, 2016–2022) separately. If OOS R² falls materially below 1% in any sub-period, the result is fragile.
2. **Parameter perturbation:** Vary the 6-month accumulation window for q (e.g., 3, 6, 12 months) and the 12-month rolling window for β (e.g., 6, 12, 24 months). If predictive power collapses, the result is parameter-dependent.
3. **Cost sensitivity:** Introduce realistic transaction costs (e.g., 10–20 bps per trade monthly) and evaluate whether the net-of-cost alpha remains meaningful at ~1% OOS R².
4. **Alternative flow measures:** Replace mutual fund FIT with direct retail flow proxies (e.g., Robinhood, retail broker data). If the effect disappears, the result depends on the specific flow measure.
5. **Cross-market test:** Replicate in non-US equity markets. If the effect is absent, it may be US-institution-specific (mutual fund structure, settlement conventions).
6. **Regime breakdown:** Test separately during high-volatility (GFC 2008–2009, COVID 2020) vs low-volatility regimes. The q variable spikes during crises; if predictive power is concentrated only in crisis periods, the strategy may not be tradeable in normal markets.

## Crypto portability

**Adapted**

The BTQ mechanism is theoretically portable to crypto if one can identify:
- **Noise traders:** Retail perpetual futures traders, leveraged speculative flows, meme-coin speculation
- **Sophisticated investors:** Market makers, institutional desks, MEV searchers
- **Factor exposures (β):** Cross-sectional betas to crypto market factor, momentum, volatility, funding-rate factors
- **Quantity (q):** Aggregate retail flow absorbed by sophisticated participants at the factor level

**Crypto-specific portability risks:**
- Crypto lacks a CRSP-equivalent mutual fund flow dataset; quantity proxies would need to be constructed from exchange-level order flow, on-chain data, or leveraged position data
- Factor structure in crypto is less established than in equities; the 153 JKP factors do not directly translate
- 24/7 trading and perpetual funding create additional factors (funding rate, basis) that could interact with quantity
- Cross-exchange fragmentation complicates flow aggregation
- Market microstructure differences (fragmented venues, different settlement, no centralized clearing) may alter the noise-trader-vs-sophisticated-investor dynamic
- The ~1% monthly OOS R² in equities may not translate to crypto, which has higher noise and different information structure

## Limitations

- **Equity-focused:** All empirical results are from US equities; no crypto or non-US evidence.
- **Not a trading strategy:** The source is a factor pricing model, not a strategy backtest. No transaction costs, slippage, capacity, or portfolio construction rules are specified.
- **Flow data dependency:** Requires mutual fund flow data (CRSP + Thomson/Refinitiv); this specific data infrastructure does not exist in crypto.
- **~1% OOS R²:** The predictive power is modest and may not survive realistic transaction costs, especially at monthly rebalancing.
- **Publication status:** Preprint (arXiv); not yet peer-reviewed as of 2026-09-04.
- **Data gap:** Transaction cost / slippage / spread / funding / liquidation / fill model — not stated in source. This is a pricing model, not a trading strategy backtest, so execution costs are not modeled.
- **Not independently reproduced:** All results are source-reported.
- **Factor zoo mitigation:** Lasso/PCA factor selection is data-driven and may overfit to the specific sample period.

## Implementation status

Not implemented. No implementation in our research stack has been completed. This is a research-only capture of an external factor pricing model.

## Adoption boundary

This record is research material only. It does not imply:
- Profitable alpha
- Validated factor premium
- Approved for implementation
- Approved for paper trading
- Approved for testnet
- Approved for live trading

## Related Wiki records

- `[[quant/crypto-cross-sectional-factor-zoo-iterative-alpha-compression-2026-09-01]]` — factor zoo compression in crypto (different mechanism: iterative alpha-based selection vs BTQ interaction)
- `[[quant/strategy-research-record-spec-v1]]`

## Sources

1. Yu An, Yinan Su, and Chen Wang. "Quantity, Risk, and Return." arXiv preprint `arXiv:2609.05162v1 [q-fin.GN]`, submitted 2026-09-04. https://arxiv.org/abs/2609.05162v1
