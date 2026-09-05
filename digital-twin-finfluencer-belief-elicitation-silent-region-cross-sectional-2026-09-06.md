---
schema: strategy-research-record-v1
title: "Digital Twin Finfluencer Belief Elicitation: Silent-Region Cross-Sectional Return Predictability"
created: 2026-09-06
updated: 2026-09-06
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - LLM
  - sentiment
  - cross-sectional
  - social-media
  - equity
status: research-only
confidence: medium
source_as_of: 2026-08-02
sources:
  - "https://arxiv.org/abs/2608.01181"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Digital Twin Finfluencer Belief Elicitation: Silent-Region Cross-Sectional Return Predictability

## Provenance

- **Primary Source:** Boone Bowles (UC Santa Barbara), Raymond Duch (University of Oxford), Sorin Sorescu (University of Melbourne), *"Talking to Digital Twins: Selective Disclosure and Belief Measurement in Financial Social Media"*, arXiv preprint `arXiv:2608.01181v1 [econ.GN, cs.AI]`, submitted August 2, 2026. DOI: [10.48550/arXiv.2608.01181](https://doi.org/10.48550/arXiv.2608.01181). Full text: [https://arxiv.org/html/2608.01181v1](https://arxiv.org/html/2608.01181v1).
- **Sample Period:** December 14, 2025 through March 15, 2026 (approximately 50 stock-pick event dates, 53 macro trading days).
- **Universe:** 81 monitored finfluencer accounts on X (selected June 2025, ≥5,000 followers, content-consistency screened); 429 unique S&P 500 stock tickers in the stock-pick interview branch.
- **Source Status:** Preprint; not peer-reviewed at time of capture.

## Economic mechanism

### Source-reported

The authors frame the problem as *selective disclosure*: finfluencers' public posts represent voluntary disclosures that mix underlying beliefs with the decision to reveal them. Silence is ambiguous — a finfluencer may be silent because they have no view, because the stock is not salient, or because disclosure is strategically costly. The "silent region" (stocks not publicly discussed) is therefore unmeasured by post-based methods.

The proposed solution is to construct "digital twins" — LLM-based replicas of each finfluencer's public persona, built from profile metadata and recent monitored content — and interview them daily under a fixed, standardized protocol. This separates belief recovery from the disclosure decision. The interview protocol elicits stock-level direction (buy/hold/sell scores 0–100), speculation confidence, and macro-market views.

### Research interpretation

The hypothesized alpha mechanism is **information asymmetry through structured belief elicitation**: when finfluencers have views they choose not to disclose publicly, those views carry incremental information about future returns. The "silent region" — stocks finfluencers don't publicly discuss — is where the interview signal is strongest, suggesting that the unobserved portion of selective disclosure contains economically meaningful belief proxies.

The cross-sectional mechanism is: stocks with higher aggregate "Net Buy Share" (buy recommendations minus sell recommendations from meaningful low-speculation twin interviews) earn higher subsequent excess returns, while sell-leaning stocks underperform. This is consistent with limited-attention / slow-information-diffusion models where retail-facing intermediaries process and partially transmit information that has not yet fully incorporated into prices.

Key components:
- **Regime filter:** None explicitly proposed; signal tested unconditional.
- **Primary signal:** Net Buy Share from digital twin stock-pick interviews.
- **Confirmation filter:** Low speculation score threshold (speculation ≤ 40) and meaningful recommendation threshold (≥ 15 points from neutral 50).
- **Risk / exit:** Not specified; paper is a measurement study, not a trading strategy.

## Signal

**Formation timestamp:** Interviews are conducted daily, real-time, and archived before the relevant return window begins. Each interview response is assigned to the first trading day on which an investor could have observed and acted on it. All timestamps are US Eastern.

**Lookback:** Daily cross-sectional snapshot; no multi-day lookback in the baseline signal. Each event date produces a fresh cross-section of 429 stock-level signals.

**Long entry (research-proposed):** Rank stocks by Net Buy Share. Go long the top quintile (equal-weighted) of stocks with the highest Net Buy Share from digital twin interviews.

**Short entry (research-proposed):** Short the bottom quintile of stocks with the lowest (most negative) Net Buy Share.

**Exit (research-proposed):** Hold for 10 trading days, then rebalance to new signal cross-section.

**Holding period (research-proposed):** 10 trading days maximum; 5-day horizon also tested.

**Parameters:**
- Meaningful recommendation threshold: ≥ 15 points from neutral (50). Research-proposed per source.
- Low speculation threshold: speculation score ≤ 40. Research-proposed per source.
- Net Buy Share = (share of meaningful buys) − (share of meaningful sells) among low-speculation responses.
- Calendar-time portfolio: top quintile long, bottom quintile short, equal-weighted within legs.

**Underspecified items:**
- Position sizing and leverage: not specified.
- Re-entry rules: not specified.
- Signal decay: paper shows weak 1-day predictability, strengthening at 5–10 days; optimal rebalance cadence not determined.

## Required data

- **Instrument:** S&P 500 constituents (429 unique tickers during sample); US equities.
- **Venue:** US equity markets (specific exchange not specified).
- **Market type:** Spot / listed equities.
- **Timeframe:** Daily signal; 5- and 10-day return horizons.
- **Fields required:**
  - X social media account data: profile metadata, recent posts (for digital twin construction).
  - LLM API access (model not specified; likely GPT-4 class).
  - Stock prices, returns, market capitalizations (source: S&P Capital IQ).
  - S&P 500 index returns (for excess return calculation).
  - Finfluencer recommendation posts (for validation; not required for signal generation).
- **Point-in-time:** Interviews are conducted live, timestamped, and archived before return windows. No look-ahead bias by construction.
- **Timestamp:** US market time; daily resolution.
- **Missing data:** Not explicitly discussed in source.
- **Funding/fee/spread:** Not modeled. Paper explicitly states it does not study trading costs or liquidity.

## Execution assumptions

- **Signal-to-order timing:** Signal is formed before the return window begins. Same-day or next-day execution is implicit.
- **Order type:** Not specified. Assumed market order for research-proposed strategy.
- **Fill model:** Not specified.
- **Fees:** Not modeled.
- **Slippage:** Not modeled. Paper explicitly states it does not study trading costs.
- **Impact / capacity:** Not modeled. Equal-weighted quintile portfolio; capacity not assessed.
- **Leverage / margin:** Not specified.
- **Latency:** Not specified; daily rebalance assumed.
- **Partial fills / failures:** Not discussed.

## Evidence

### Source-reported

All results are from Bowles, Duch, and Sorescu (arXiv:2608.01181v1, August 2026):

**Fama–MacBeth cross-sectional regressions (Table 5, Panel B — Net Buy Share, full sample):**
- 1-day horizon: coefficient ≈ −0.002 pp per +10pp Net Buy Share (not significant).
- 5-day horizon: coefficient ≈ 0.166 pp per +10pp Net Buy Share (not significant at conventional levels).
- 10-day horizon: coefficient ≈ 0.404 pp per +10pp Net Buy Share (significant at 1% level, Newey–West SE = 0.152).

**Controlled Fama–MacBeth (Table 6, Panel B — Net Buy Share, with lagged return/vol controls):**
- 10-day horizon: coefficient ≈ 0.385 pp per +10pp Net Buy Share (significant at 5% level).

**Calendar-time long-short portfolio (Table 5, Columns 4–6 — Net Buy Share):**
- H-L Mean daily return: 12.0 bps.
- CAPM Alpha daily: 10.8 bps.
- 10-day Alpha: 108 bps (significant at 10% level).

**Silent-region signal (Table 8, Panel B — Net Buy Share, no-post sub-sample):**
- 5-day horizon: 0.242 pp per +10pp Net Buy Share (significant at 5%).
- 10-day horizon: 0.503 pp per +10pp Net Buy Share (significant at 5%).
- N = 18,159 stock-event observations (84.8% of sample).

**Validation (Table 3):**
- Digital twin sign alignment with public recommendations: 91.5% (meaningful low-speculation subset).
- Buy-sell ranking AUC: 0.776 (benchmark 0.522, p < 0.001).
- Pre-disclosure signed tilt: 5.32 vs. 2.60 placebo (p < 0.001).

**Staggered-vintage placebo tests (Table 7):**
- Net Buy Share: all 10 ten-day vintages positive and significant at 10%.
- Unrestricted placebo p-value: 0.0002.
- FF12 industry placebo p-value: 0.0268 (ten-day horizon).

**Value-weighted results (Table A2, Internet Appendix):**
- Estimates are much smaller and not statistically distinguishable from zero. Relation is concentrated in equal-weighted portfolios (i.e., smaller and mid-cap stocks within S&P 500).

### Independently reproduced

Not independently reproduced. All results are source-reported from Bowles, Duch, and Sorescu (arXiv:2608.01181v1, 2026).

### Negative evidence

1. **Short sample:** Only ~50 trading days of event dates over 3 months. Statistical power is limited; time-series dimension is short.
2. **Value-weighted insignificance:** When value-weighted (larger firms dominate), the signal loses statistical significance. The relation appears concentrated in equal-weighted portfolios, suggesting it is stronger among smaller S&P 500 constituents.
3. **Industry placebo erosion:** After preserving within-industry comovement (FF12 industry placebo), Net Buy Share remains significant at 10% for both horizons, but Tilt and Conviction-Weighted Meaningful Tilt lose significance at the five-day horizon. Industry-level shared views contribute to the signal.
4. **Public-post signal null:** In the overlap sample where public posts exist, the public-post signal does not predict returns (coefficient ≈ 0). The signal is entirely driven by the silent region.
5. **Overlapping return windows:** Baseline Fama–MacBeth and calendar-time results use overlapping return windows. While staggered-vintage tests address this, the short sample limits power.
6. **No out-of-sample period:** The entire 3-month sample is used for both signal construction and evaluation. No true out-of-sample test exists.
7. **LLM model sensitivity:** The paper does not test robustness across different LLM models or prompt variations. Digital twin fidelity depends on the specific LLM and prompt engineering.
8. **Sample period context:** December 2025–March 2026 included the U.S.–Iran conflict (beginning ~February 28, 2026), which may have affected market dynamics and finfluencer behavior during the sample.

## Falsification plan

1. **Out-of-sample temporal validation (research-proposed):** Extend the interview protocol to a new 3+ month period with the same finfluencer cohort. **Failure rule:** If the 10-day Net Buy Share coefficient drops below 0.15 pp per +10pp or loses significance at 10%, the signal is not temporally robust.
2. **Different LLM backbone (research-proposed):** Re-run digital twin interviews using a different LLM (e.g., Claude, open-source model). **Failure rule:** If sign alignment with public recommendations drops below 75% or the cross-sectional signal loses significance, the mechanism is LLM-dependent rather than persona-dependent.
3. **Expanded universe (research-proposed):** Extend to Russell 1000 or broader mid/small-cap universe. **Failure rule:** If the equal-weighted signal does not maintain significance, the S&P 500 result may be sample-specific.
4. **Transaction cost stress (research-proposed):** Model 5–10 bps round-trip cost and 1–2 day signal delay. **Failure rule:** If the 10-day alpha (108 bps) is erased by costs and delay, the signal is not implementable.
5. **Capacity test (research-proposed):** Assess how signal degrades with position size constraints and participation rate caps for smaller S&P 500 names. **Failure rule:** If practical capacity is below $50M notional, institutional deployment is questionable.
6. **Ablation of silent region (research-proposed):** Run the signal only on the overlap sample (public-post stock-dates). **Failure rule:** If the signal loses significance in the overlap sample (as the paper already suggests), the mechanism depends entirely on the unmeasured silent region.

## Crypto portability

**unproven**

The mechanism originates from US equity markets with finfluencers who primarily cover equities. Crypto portability is speculative:

- **Potential adaptation:** Crypto Twitter/X is heavily populated with finfluencers covering BTC, ETH, and altcoins. A similar digital twin protocol could be constructed for crypto finfluencers, potentially covering perpetual futures, spot tokens, and DeFi protocols.
- **Key risks:**
  - Crypto finfluencers may exhibit different disclosure patterns (more pump-and-dump, more incentive-aligned posting).
  - 24/7 market structure changes the interview cadence and relevance of daily snapshots.
  - Smaller market cap and thinner liquidity in many altcoins could amplify both signal and impact.
  - The "silent region" concept is directly portable, but the specific universe (S&P 500) is not.
  - LLM digital twin fidelity for crypto personas may differ from equity finfluencers.

## Limitations

- **Short sample:** ~50 event dates over 3 months. Time-series inference is limited.
- **Single LLM backbone:** Not tested across multiple models or prompt variations.
- **No true out-of-sample:** Entire sample used for signal evaluation.
- **Value-weighted insignificance:** Signal is concentrated in equal-weighted portfolios; weaker among largest-cap stocks.
- **No transaction cost modeling:** Paper explicitly does not study trading costs, slippage, or capacity.
- **Finfluencer selection bias:** 81 accounts selected from industry directories; not a census of all market-relevant finfluencers.
- **Regime dependence:** Sample includes a geopolitical shock (U.S.–Iran conflict); signal behavior in calm markets unknown.
- **Industry comovement:** A non-trivial portion of the signal is explained by within-industry correlated views.
- **LLM reproducibility:** Digital twin construction depends on specific LLM, prompt engineering, and monitoring pipeline; not easily reproducible without access to the same accounts and protocol.
- **data gap:** Paper does not report Sharpe ratio of the long-short portfolio in standard form; CAPM alpha is reported but not risk-adjusted return metrics like Sharpe, Sortino, or information ratio.
- **data gap:** Optimal holding period, rebalance cadence, and signal decay profile are not systematically characterized.

## Implementation status

No implementation in our research stack. Paper is a measurement/predictability study, not a trading strategy backtest. No code repository is publicly available.

## Adoption boundary

This record is research-only. Presence in this repository does not mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

The source itself explicitly states: *"The tests presented in this Section evaluate the informational content of twins' interviews. They do not evaluate the profitability of an implementable trading strategy."*

## Related Wiki records

No directly related Wiki Brain records identified. Adjacent concepts:
- LLM-based sentiment and news processing for equity selection.
- Social media sentiment cross-sectional return predictability.
- Finfluencer recommendation tracking.

## Sources

1. Boone Bowles, Raymond Duch, Sorin Sorescu. *"Talking to Digital Twins: Selective Disclosure and Belief Measurement in Financial Social Media"*. arXiv preprint `arXiv:2608.01181v1 [econ.GN, cs.AI]`, submitted August 2, 2026. DOI: [10.48550/arXiv.2608.01181](https://doi.org/10.48550/arXiv.2608.01181). Full text: [https://arxiv.org/html/2608.01181v1](https://arxiv.org/html/2608.01181v1).
