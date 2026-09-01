---
schema: strategy-research-record-v1
title: Crypto Security Shock Cross-Sectional Factor (Hacks / Market Cap)
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - security
  - on-chain
  - risk-premium
  - factor-pricing
status: research-only
confidence: medium
source_as_of: 2026-07-16
sources:
  - https://arxiv.org/abs/2601.07664 (arXiv:2601.07664v3, accepted Finance Research Letters)
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Security Shock Cross-Sectional Factor (Hacks / Market Cap)

## Provenance

- **Paper:** Brigida, Matthew. "Crypto Pricing with Hidden Factors." arXiv:2601.07664v3 [q-fin.PR], July 16, 2026. Accepted for publication in *Finance Research Letters*.
- **Author affiliation:** Chief Economist, Algorand Foundation; Department of Accounting and Finance, SUNY Polytechnic Institute.
- **Sample:** Weekly returns, January 2023 – December 2024 (105 weeks), top-100 CMC non-stablecoin universe (253 unique cryptocurrencies, >97% of total crypto market cap).
- **Data sources:** CoinMarketCap (prices, Fear & Greed, Altcoin Season Index), DeFiLlama (USD hacked amounts), CVX (Bitcoin implied volatility), Kenneth French data library (equity factors).
- **Key novelty claim:** "We study non-tradable state variables capturing investor sentiment (Fear and Greed), speculative rotation (Altcoin Season Index), and security shocks (hacked value scaled by market capitalization), which are new to the literature."

## Economic mechanism

### Source-reported

The author constructs a "Hacks" variable as USD amount hacked (from DeFiLlama) scaled by aggregate or per-asset market capitalization. This variable is converted to an AR(1) residual to isolate the shock component. The Hacks variable is tested alongside three other non-tradable state variables (Fear/Greed, Altcoin Season, CVX) as candidate pricing factors using the Giglio-Xiu (2021) three-pass latent factor estimator. In the main results (Table 3), Hacks does not carry a statistically significant price of risk (p=0.733), unlike the crypto SMB factor which is significant at 1%.

### Research interpretation

The economic hypothesis is that security incidents (hacks, exploits, bridge attacks) represent a systematic risk factor in crypto markets. When a large hack occurs, it may:

1. **Erode confidence in affected protocols/ecosystems**, causing correlated selling pressure.
2. **Trigger forced liquidations** if hacked collateral was used in DeFi lending.
3. **Reduce TVL across DeFi**, as users withdraw funds preemptively ("bank run" dynamic).
4. **Create information asymmetry** — sophisticated actors may front-run the market's delayed reaction to hack severity.

The cross-sectional prediction: assets with higher hack exposure (hacked value / market cap) should command higher expected returns as compensation for this risk. However, the Brigida (2026) finding is that Hacks is NOT priced in the latent-factor model, suggesting either (a) the market efficiently prices hack risk instantaneously, (b) the variable is too sparse/noisy to detect pricing, or (c) the sample period is too short.

This remains a **falsifiable and actionable hypothesis** — the null (no pricing) could be rejected with a longer sample, higher-frequency data, or a different construction (e.g., ecosystem-level hack exposure rather than aggregate).

## Signal

**Hypothesis:** Long short-portfolio sorted by hack exposure (hacked value / market cap).

- **Construction:** For each cross-section, rank assets by DeFiLlama-reported hacked USD amount scaled by market cap. Create a value-weighted long-short portfolio (top quartile minus bottom quartile).
- **Frequency:** Weekly (as in the source paper).
- **Alternative constructions to test:**
  - Rolling 30/60/90-day cumulative hacks (not just weekly).
  - Ecosystem-level hack exposure (e.g., Ethereum ecosystem hack total / ETH market cap).
  - Time-since-last-hack decay weighting.
  - Hack severity tiers (>$10M vs <$10M).
- **Parameters:** AR(1) residualization window for Hacks variable (source uses AR(1) on levels).
- **Overspecified:** The exact portfolio construction is specified, but the cross-sectional breakpoint sensitivity (20/80 vs 25/75 vs 30/70) is not fully explored in the source for Hacks specifically.

## Required data

- **Instrument universe:** Top-100 CMC non-stablecoin cryptocurrencies.
- **Venue:** CoinMarketCap for prices/market cap; DeFiLlama for hack data.
- **Market type:** Spot returns (weekly).
- **Data fields:** Weekly close prices, market capitalization, DeFiLlama hack tracker (USD amount, date, affected protocol/chain).
- **Timestamp:** Weekly frequency, end-of-week.
- **Missing data:** Hack events are sparse and episodic — many assets will have zero hacks in any given week. The source uses AR(1) residualization to handle this.

## Execution assumptions

- Source does not specify execution details for the Hacks variable beyond portfolio construction.
- Assumed market-cap-weighted long-short with no transaction costs reported.
- Weekly rebalancing.
- No leverage specified.
- The variable is non-tradable in itself — it cannot be directly traded. It could be expressed via (a) cross-sectional equity-like portfolio sorts on hack-exposed tokens, or (b) as a conditioning variable for other strategies.

## Evidence

### Source-reported

- **Hacks factor:** Mean weekly return 0.00%, Std 0.00%, Skewness 3.25, Kurtosis 11.26 (Table 1). Highly skewed and fat-tailed — consistent with episodic hack events.
- **Pricing test:** Hacks price of risk is not statistically significant (p=0.733) in the latent-factor model (Table 3).
- **Breakpoint robustness:** Not separately reported for Hacks in Table A1.
- **Context:** Of the four non-tradable state variables tested (Hacks, Fear/Greed, Altseason, CVX), NONE carry statistically significant prices of risk in the main specification. Only crypto SMB (SMBC) and crypto momentum (MomC) show significance among crypto-native factors.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The Brigida (2026) paper itself finds Hacks is NOT priced — this is direct negative evidence against the security shock risk premium hypothesis.
- However, the negative finding may be attributable to: (a) short sample (105 weeks), (b) sparse hack events creating low statistical power, (c) aggregate construction losing protocol-level signal.
- The paper's own caveat: "Our findings should be interpreted as exploratory evidence from a short but institutionally important sample period."

## Falsification plan

1. **Extended sample:** Replicate with weekly data from 2018–2026 to increase hack-event count and test across multiple market regimes (pre-FTX, post-FTX, post-ETF).
2. **Protocol-level hack exposure:** Instead of aggregate hacks, construct per-asset hack exposure (e.g., "was this token's ecosystem hacked?") as a binary or severity-weighted variable.
3. **Event-study approach:** Test post-hack drift for individual tokens — does price over- or under-react to hack announcements?
4. **DeFi TVL interaction:** Test whether hack events cause predictable TVL outflows that predict subsequent returns.
5. **Baseline:** Equal-weighted or market-cap-weighted crypto portfolio; random walk.
6. **Failure metric:** If post-hack drift is zero (t-stat < 2) across a sample of ≥50 hack events, the hypothesis is weakened.
7. **Action on failure:** Abandon hack-based cross-sectional factor; retain as conditioning variable only if event-study shows significance.

## Crypto portability

direct

The strategy is native to crypto markets — hacks and exploits are a crypto-specific phenomenon with no traditional-asset analog. The DeFiLlama hack tracker is a crypto-native data source.

## Limitations

- **Not independently reproduced** — single paper, exploratory sample.
- **Short sample** — 105 weeks, ~2023–2024, captures post-FTX recovery and ETF emergence but not full cycle.
- **Sparse events** — hack events are episodic; weekly frequency may miss or mis-time the signal.
- **Non-significant pricing** — the source paper itself finds Hacks is not priced, weakening the risk-premium thesis.
- **Data quality** — DeFiLlama hack tracker may undercount or misattribute hacks; reporting lags are possible.
- **Construction uncertainty** — AR(1) residualization of a sparse, skewed variable may not be the optimal transformation.

## Implementation status

Not implemented. This is a research-only record.

## Adoption boundary

This record represents normalized research material only. It does NOT mean:

- That the security shock factor is profitable.
- That hack-based cross-sectional sorting has been validated.
- That any implementation, paper trading, testnet, or live trading has occurred.
- That the Brigida (2026) negative pricing finding is incorrect or should be overridden.

## Related Wiki records

- [[crypto-cross-sectional-size-factor-smb-2026-08-31]] (related: cross-sectional factor pricing in crypto, same paper finds SMB significant)
- [[crypto-cross-sectional-realized-signed-jump-good-bad-volatility-2026-09-01]] (related: jump/risk factors in crypto cross-section)
- [[crypto-cross-sectional-systemic-tail-risk-covar-2026-08-31]] (related: systemic risk factors)

## Sources

1. Brigida, M. (2026). "Crypto Pricing with Hidden Factors." arXiv:2601.07664v3. Accepted, *Finance Research Letters*.
   - URL: https://arxiv.org/abs/2601.07664
   - Key tables: Table 1 (factor descriptive statistics), Table 3 (latent-factor price of risk estimates), Table A1 (breakpoint robustness).
2. DeFiLlama Hack Tracker: https://defillama.com/ (hack data source referenced in paper).
3. CoinMarketCap Fear & Greed Index and Altcoin Season Index (non-tradable state variables from paper).
