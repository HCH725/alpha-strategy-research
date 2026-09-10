---
schema: strategy-research-record-v1
title: "AI Misinformation Risk Factor Pricing — Cross-Sectional Equity Exposure to D3 News Innovations (Shen 2026)"
created: 2026-09-11
updated: 2026-09-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - ai-risk
  - misinformation
  - cross-sectional
  - equity
  - news-sentiment
  - factor-pricing
status: research-only
confidence: medium
source_as_of: 2026-09-11
sources:
  - "arXiv:2609.05485v1 [q-fin.GN], submitted 23 August 2026 — Yanhui (Patti) Shen, 'Are AI Risks Priced in the U.S. Stock Market? Evidence from Financial News Factors'"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# AI Misinformation Risk Factor Pricing — Cross-Sectional Equity Exposure to D3 News Innovations (Shen 2026)

## Provenance

- **arXiv:** [2609.05485v1](https://arxiv.org/abs/2609.05485) [q-fin.GN]
- **Author:** Yanhui (Patti) Shen (sole author)
- **Title:** "Are AI Risks Priced in the U.S. Stock Market? Evidence from Financial News Factors"
- **Submitted:** 23 August 2026
- **PDF:** https://arxiv.org/pdf/2609.05485
- **Universe:** US equities — NYSE, AMEX, Nasdaq ordinary common stocks (CRSP)
- **Sample period:** January 2016 – December 2025 (beta estimation begins January 2017; first holding month April 2017; last holding month December 2025)
- **Data source:** CRSP daily and monthly returns (delisting-adjusted); Kenneth R. French Data Library (factor returns, risk-free rate); Compustat accounting data; I/B/E/S analyst forecasts; CBOE VIX
- **Primary source verified:** Yes — full PDF read; Tables 7–8, 12; Sections 5–6

## Economic mechanism

### Source-reported

The author constructs four domain-specific AI-risk news factors by combining latent Dirichlet allocation (LDA) topic modeling on 7,787 Wall Street Journal articles (2016–2025) with the MIT AI Risk Repository taxonomy (Slattery et al., 2026). The seven MIT taxonomy domains are: D1 Discrimination/toxicity, D2 Privacy/security, D3 Misinformation, D4 Malicious actors/misuse, D5 Human-computer interaction, D6 Socioeconomic/environmental harm, D7 AI system safety/failures/limitations. Four domains generate active daily factors (D2, D3, D4, D6); D1, D5, D7 receive zero mapping weight.

The central finding is that only the D3 Misinformation factor is consistently priced. The economic channel: D3 peaks correspond to AI governance and policy events (EU AI Act, US executive orders, Bletchley Declaration, voluntary safety commitments). A positive D3 innovation signals unexpected improvement in AI-policy clarity and lower uncertainty. High-D3-beta stocks perform well when policy clarity improves but poorly when uncertainty rises. Investors require compensation for this exposure — consistent with the intertemporal asset pricing framework of Merton (1973) and the policy-uncertainty channel of Pástor and Veronesi (2013).

### Research interpretation

The hypothesized alpha mechanism is a **cross-sectional news-based risk premium**: firms with higher sensitivity to AI misinformation/policy news innovations earn higher expected returns as compensation for bearing non-diversifiable policy-uncertainty risk. The signal is an equity factor strategy, not a direct crypto strategy. For crypto portability, the analogous hypothesis would be that crypto assets or tokens whose valuations are sensitive to AI-regulatory news carry a similar premium — this is a research-proposed ported hypothesis, not demonstrated in the source.

The factor is constructed as follows:
1. LDA identifies 18 topics from 7,787 WSJ articles (K=18 selected via coherence, diversity, and cross-seed stability; seed 84 used)
2. 14 topics retained after manual + GPT-5.6 Sol relevance review (≥5/20 articles substantively AI-risk-related)
3. Topics mapped to MIT taxonomy subdomains via cosine similarity with frequency-matched null standardization and Sparsemax
4. Four active domains emerge: D2 (Privacy/security), D3 (Misinformation), D4 (Malicious actors/misuse), D6 (Socioeconomic/environmental harm)
5. Daily factor levels constructed by summing LDA topic proportions of day's articles weighted by topic-domain mapping weights
6. AR(1) innovations extracted (365-day rolling window); trading-day aligned with look-ahead protection
7. Firm-level betas estimated via daily regressions of excess returns on factor innovations (with FF factor controls)
8. Cross-sectional pricing tested via univariate portfolio sorts and Fama-MacBeth regressions

## Signal

### Formation timestamp

- Factor innovations are constructed at the trading-day frequency. Calendar-day AR(1) innovations are aligned to trading days using only prior-calendar-day innovations (no look-ahead). An ordinary Monday return is matched with summed Friday–Sunday innovations.
- Firm-level betas are estimated at month-end using the preceding 3 months of daily data (baseline).
- Portfolios are formed at month-end m and held during month m+1.

### Lookback

- Beta estimation: 3-month (baseline), 6-month, and 12-month windows; minimum 50/100/200 valid daily observations respectively.
- AR(1) innovation model: 365 calendar-day rolling window.

### Long entry

- At month-end, sort all eligible stocks by their estimated D3 beta into quintiles using NYSE breakpoints.
- Long portfolio P5: stocks in the highest D3-beta quintile.

### Short entry

- Short portfolio P1: stocks in the lowest D3-beta quintile.

### Exit / rebalance

- Monthly rebalance. Portfolios held for one month, then reformed.

### Holding period

- One month (monthly rebalance cadence).

### Parameters

- D3 beta estimation window: 3 months (baseline); also tested at 6 and 12 months.
- Innovation model: AR(1) (baseline); also tested AR(7), ARMA(1,1), ARMA(2,1).
- First-pass controls: CAPM, FF3, Carhart, FF5, FF5+UMD (five specifications).
- Industry controls: Fama-French 10 industries (with and without).
- Portfolio value-weighted using market capitalization at month-end.

### Position sizing

- Research-proposed: equal capital allocation across quintile portfolios; value-weighted within each quintile using market cap. No leverage assumed.

### Underspecified

- Signal is fully specified for the cross-sectional equity factor test described. No operational trading rules (limit orders, stop-losses, partial fills) are defined — this is an asset pricing test, not a live strategy blueprint.

## Required data

- **Instrument:** US equities — ordinary common stocks (CRSP sharetype=NS, securitytype=EQTY, securitysubtype=COM, usincflg=Y, issuertype=ACOR or CORP, primaryexch=N/A/Q)
- **Universe:** NYSE, AMEX, Nasdaq listed; delisting-adjusted returns
- **Venue:** US equity markets
- **Market type:** Equity (spot)
- **Timeframe:** Daily returns for beta estimation; monthly returns for portfolio evaluation
- **Fields:** Daily and monthly stock returns; market cap (for value weighting); SIC codes (for industry classification); Compustat accounting data (book equity, total assets, operating profitability); I/B/E/S analyst forecasts; CBOE VIX
- **News data:** Full-text WSJ articles (January 2016 – December 2025), 387,051 raw articles → 7,787 AI-risk articles (keyword filtering: AI lexicon ∩ risk lexicon)
- **Timestamp:** Article timestamps interpreted in Eastern Time (ET); aligned with US equity trading calendar
- **Point-in-time:** Article timestamps used; CRSP/Compustat/I/B/E/S data availability conventions followed
- **Missing-data:** Delisting returns set to −100% when missing; minimum observation requirements enforced for beta estimation

## Execution assumptions

- **Signal-to-order timing:** Month-end portfolio formation; next-month returns used. Standard asset-pricing convention.
- **Execution model:** Not specified — this is an asset pricing study, not a live trading system.
- **Fees:** Not modeled. The paper does not incorporate transaction costs, commissions, or market impact.
- **Slippage:** Not modeled.
- **Spread:** Not modeled.
- **Impact:** Not modeled.
- **Fill model:** Not specified.
- **Leverage:** Not specified (long-short portfolio is long P5, short P1; zero-cost in principle).
- **Capacity:** Not explicitly addressed. Value-weighting mitigates small-cap capacity concerns.
- **Latency:** Not applicable (monthly rebalance).

Note: The absence of transaction cost modeling is a limitation. The 0.49–0.57% monthly alpha must be evaluated against realistic trading costs before any implementation consideration.

## Evidence

### Source-reported

- **Univariate portfolio analysis (3-month beta window, FF5+UMD first-pass):**
  - D3 P5−P1 alphas: 0.538% (Carhart, t=2.16), 0.526% (FF5, t=1.94), 0.575% (FF5+UMD, t=2.23) per month
  - All five factor-model alphas positive; significant at 10% in all cases, 5% under Carhart and FF5+UMD
  - Raw excess return spread: 0.429%/month (t=1.52, not significant)
  - Monotonic alpha ordering from P1 to P5 under Carhart, FF5, FF5+UMD
  - Post-ranking betas: monotonically increasing from P1 (−0.00253) to P5 (0.00188)
  - Sample: 105 consecutive holding months (April 2017 – December 2025)
  - D2, D4, D6: no significant alphas in any specification

- **Fama-MacBeth regressions (3-month window, all specifications):**
  - D3 price of risk: positive in all 30 specifications (3 windows × 5 controls × 2 industry settings)
  - Without industry controls: 0.0403–0.0496, t-statistics 2.73–3.49 (all significant at 1%)
  - With industry controls: 0.0369–0.0429, t-statistics 2.85–3.56 (all significant at 1%)
  - Joint Wald test rejects H0 (all four λ=0) at 5% in 9/10 specifications
  - Average monthly cross-sectional sample: ~3,750 stocks

- **6-month and 12-month windows:**
  - All 20 D3 estimates positive and significant at 5%
  - 6-month: all significant at 1%
  - 12-month: t-statistics 2.04–2.20, significant at 5%

- **Robustness — alternative innovation models (3-month window, FF5+UMD, industry controls):**
  - AR(7), ARMA(1,1), ARMA(2,1): D3 price 0.0380–0.0479, t-statistics 2.98–4.00 (all significant at 1%)
  - None of D2, D4, D6 significant even at 10%

- **Robustness — pre-ChatGPT subsample (through November 2022):**
  - D3 price: 0.0346–0.0412, t-statistics 2.36–3.42
  - CAPM: significant at 5%; others at 1%
  - D2, D4, D6: not significant

- **High-D3-beta firm characteristics:**
  - Higher investment rates (I/A coefficient: 0.0027, t=3.67 in joint regression)
  - Consistent with policy-uncertainty channel (Gulen & Ion, 2016)

### Independently reproduced

Not independently reproduced.

### Negative evidence

- D2, D4, D6 factors show no reliable pricing evidence — the D3 result is domain-specific, not a general AI-risk premium.
- Raw return spread (0.429%/month) is not statistically significant (t=1.52) — the alpha comes from risk adjustment, not raw returns.
- Transaction costs not modeled; the paper acknowledges this as a limitation (typical for asset pricing studies).
- The paper notes that D6's heterogeneity (combining labor, environment, data-center narratives) may dilute its common priced component.
- No independent out-of-sample or live-trading verification exists.

## Falsification plan

1. **Out-of-sample test:** Replicate on non-US equity markets (e.g., European, Asian equities) to test geographic robustness. Falsified if D3 alpha disappears outside US.
2. **Point-in-time leakage audit:** Verify that WSJ article timestamps are genuinely available before the next trading day; any systematic delay would inflate results. Falsified if alpha is concentrated in overnight-gap days.
3. **Alternative news sources:** Replace WSJ with Reuters, Bloomberg, or social media news feeds. Falsified if D3 pricing is specific to WSJ editorial choices.
4. **Transaction cost sensitivity:** Apply realistic equity trading costs (commissions, bid-ask, market impact). Research-defined falsification threshold: if net alpha after costs falls below 0.20%/month (annualized ~2.4%), the strategy has marginal implementability.
5. **Subperiod stability:** Split sample into pre-2020 and post-2020 periods. Falsified if D3 pricing is concentrated in a single subperiod.
6. **Alternative topic models:** Replace LDA with BERT-based topic extraction or alternative NLP methods. Falsified if D3 pricing depends on LDA-specific artifact.
7. **Ablation of governance events:** Exclude articles mentioning specific policy events (EU AI Act, executive orders). Falsified if D3 alpha disappears without governance-news content.
8. **Capacity/liquidity constraint:** Test whether D3 alpha persists after excluding illiquid or micro-cap stocks (e.g., below NYSE median market cap).

## Crypto portability

**Adapted** — not directly demonstrated in the source.

The paper itself reviews crypto markets (spot, perpetual futures, on-chain) in its literature review section, noting that "crypto adds informative state but requires separate treatment of spot, perpetual, and decentralized cash flows and execution." However, the D3 factor pricing test is conducted exclusively on US equities.

For crypto adaptation, the analogous hypothesis would be:
- Construct a crypto-specific D3 news factor from crypto-native news sources (e.g., CoinDesk, The Block, crypto Twitter/X)
- Estimate sensitivity of crypto tokens/exchanges to AI-regulatory news innovations
- Test whether high-sensitivity crypto assets earn a premium

Crypto-specific portability risks:
- Crypto markets operate 24/7 — news arrival and market reaction timing differs from US equity sessions
- Crypto tokens have different microstructure (continuous trading, fragment across venues)
- AI-regulatory news may have asymmetric impact on crypto (e.g., EU AI Act may affect centralized vs. decentralized protocols differently)
- Funding rates and perpetual-futures dynamics are absent in the equity framework
- The paper's LDA + MIT taxonomy methodology requires adaptation to crypto-specific news sources
- Survivorship and listing dynamics differ materially from US equities

The mechanism (policy-uncertainty risk premium) is economically plausible in crypto but remains untested. This is a research-proposed ported hypothesis, not crypto empirical evidence.

## Limitations

- **No transaction cost modeling:** The 0.49–0.57% monthly alpha is gross of all trading costs. This is standard for asset pricing papers but a critical gap for any implementation consideration.
- **US equities only:** The D3 pricing is tested exclusively on US-listed equities. Cross-market portability is unknown.
- **Monthly rebalance:** The strategy assumes monthly portfolio turnover. Actual implementation costs depend on portfolio size, market cap, and liquidity.
- **News data availability:** The WSJ full-text archive is a proprietary data source. Replication requires access to this archive.
- **LDA topic model sensitivity:** Results depend on the choice of K=18 topics, seed 84, and the manual + GPT-assisted relevance review. Alternative topic models might yield different domain mappings.
- **Sample period overlap with AI boom:** Although the pre-ChatGPT subsample shows consistent results, the full sample (2016–2025) coincides with rapid AI adoption. The economic channel (policy-uncertainty) may evolve as AI regulation matures.
- **Not independently reproduced:** The result has not been replicated by independent researchers.
- **Publication bias concern:** As a single-author working paper, there is no independent peer review beyond arXiv.

## Implementation status

Not implemented. This record captures a cross-sectional equity factor pricing study. No implementation in our research stack has been completed. The strategy requires: (1) WSJ full-text archive access, (2) LDA model estimation and MIT taxonomy mapping, (3) daily factor construction pipeline, (4) rolling beta estimation, and (5) portfolio construction and rebalancing — none of which have been built.

## Adoption boundary

This is a research-only capture. A record being present in this repository does not mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

The 0.49–0.57% monthly alpha is a source-reported gross result that has not been independently reproduced or validated with transaction cost modeling.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` (schema specification)

No directly related strategy research records were identified in the repository that share the same source identity or materially similar mechanism. The closest conceptual relatives are:
- `quant/beta-times-quantity-noise-trader-flow-factor-pricing-2026-09-07.md` — also a cross-sectional factor pricing study, but uses trade-flow data rather than news text
- `quant/bitcoin-news-peer-overreaction-reversal-4w-2026-09-03.md` — uses news sentiment, but for crypto reversal rather than equity risk premium

## Sources

1. Shen, Yanhui (Patti). "Are AI Risks Priced in the U.S. Stock Market? Evidence from Financial News Factors." arXiv preprint arXiv:2609.05485v1 [q-fin.GN], submitted 23 August 2026. https://arxiv.org/abs/2609.05485
