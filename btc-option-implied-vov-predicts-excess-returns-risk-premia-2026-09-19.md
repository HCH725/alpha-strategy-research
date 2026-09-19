---
schema: strategy-research-record-v1
title: "Option-Implied VoV Predicts BTC Excess Returns: Risk Premia in a Decentralized Options Market (Atanasova et al. 2026)"
created: 2026-09-19
updated: 2026-09-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - bitcoin
  - options
  - variance-risk-premium
  - volatility-of-volatility
  - risk-premia
  - return-predictability
  - deribit
status: research-only
confidence: medium
source_as_of: 2026-03-13
sources:
  - "SSRN working paper 6410838, March 13, 2026. DOI: 10.2139/ssrn.6410838. https://ssrn.com/abstract=6410838"
  - "SSRN updated version 6771170, May 15, 2026. DOI: 10.2139/ssrn.6771170. https://ssrn.com/abstract=6771170"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Option-Implied VoV Predicts BTC Excess Returns: Risk Premia in a Decentralized Options Market (Atanasova et al. 2026)

## Provenance

- **Authors:** Christina V. Atanasova, Terrel Miao, Ignacio Segarra, Frederick H. Willeboordse
- **Affiliation:** Beedie School of Business, Simon Fraser University
- **Paper title:** "What Do Crypto Options Tell Us? Risk Premia Implied by BTC Option Prices"
- **Primary source version:** SSRN 6410838, posted March 13, 2026 (37 pages, date written March 13, 2026)
- **Updated version:** SSRN 6771170, posted May 15, 2026 (1-page abstract, same paper)
- **DOIs:** 10.2139/ssrn.6410838, 10.2139/ssrn.6771170
- **SSRN URLs:** https://ssrn.com/abstract=6410838, https://ssrn.com/abstract=6771170
- **Sample period:** Data from Deribit BTC options panel; exact sample window not stated in abstract (data described as "high-frequency" and "large cross-section").
- **Universe:** Bitcoin (BTC) options on Deribit, the largest crypto derivatives venue by volume.
- **Primary-source checksum note:** Full PDF not independently verified in this run due to access limitations. Abstracts from both SSRN versions (6410838 and 6771170) were reviewed. Author list, title, affiliation, keywords, and date match across both versions. Specific numerical results (regression coefficients, t-statistics, R², sample period bounds, sample size) are not available from abstracts alone; those fields are marked as data gap below.

## Economic mechanism

### Source-reported

The authors use a large panel of BTC options from Deribit to recover arbitrage-consistent risk-neutral return distributions within a flexible structural option-pricing framework. They focus on option-implied risk premia that can be measured from high-frequency data: the variance risk premium (VRP) and an option-implied volatility-of-volatility (VoV) factor. Following Martin (2017), they assess how much of BTC expected excess returns can be accounted for by risk-neutral variance alone. They find that in contrast to equities, variance is insufficient and higher-order risk-neutral moments contain substantial incremental information about risk compensation in crypto markets. Option-implied factors—particularly VoV—predict BTC excess returns across multiple horizons and consistently outperform common sentiment- and equity-style predictors.

The authors note that these results hold in a market with limited institutional hedging demand and decentralized market making, providing evidence that option-implied premia are not solely driven by intermediary-based mechanisms (as in the traditional equity options literature) but reflect compensation for risk.

### Research interpretation

The falsifiable hypothesis is that higher-order risk-neutral moments—specifically the volatility-of-volatility (VoV) factor extracted from the BTC option-implied risk-neutral distribution—contain predictive information about future BTC spot returns that is incremental to (a) risk-neutral variance and (b) commonly used sentiment and equity-style predictors.

The economic channel is: in crypto options markets, the relative paucity of institutional hedging demand means the option-implied risk-neutral distribution more cleanly reflects risk compensation rather than intermediary positioning. VoV captures the market's pricing of uncertainty about future volatility, which is a higher-order risk factor that variance alone cannot capture. When VoV is elevated, options are pricing in higher tail risk; the risk premium for bearing this tail risk should be reflected in subsequent spot returns.

This is a **cross-sectional and time-series return predictability** hypothesis, not a direct options-trading alpha. The signal would need to be translated into a tradable position (e.g., delta-hedged option portfolio or spot position scaled by the predictability factor).

## Signal

- **Formation timestamp:** Daily (from option prices observed at Deribit; exact intraday timing not stated in abstract).
- **Lookback window:** The risk-neutral distribution is recovered from the cross-section of option prices at each point in time. Exact estimation window for the structural model is not stated in the abstract.
- **Primary signal:** Option-implied VoV factor extracted from the risk-neutral distribution of BTC options.
- **Secondary signal:** Variance risk premium (VRP) = risk-neutral variance minus physical variance.
- **Predictive target:** BTC excess returns at multiple horizons.
- **Signal construction:** The authors use a flexible structural option-pricing framework to avoid nonparametric smoothing across strikes and maturities. From the recovered risk-neutral distribution, they extract variance, VRP, and VoV. These are then used in predictive regressions for BTC excess returns.
- **Benchmark comparison:** Option-implied factors are compared against common sentiment- and equity-style predictors.
- **Entry rule:** Source does not specify a standalone trading entry rule. The result is a return predictability finding.
- **Exit rule:** Not specified.
- **Position sizing:** Not specified.
- **Parameters:** Not specified in the abstract.
- **Full specification:** Underspecified from abstracts alone. The exact predictive regression horizons, coefficient magnitudes, and t-statistics require access to the full 37-page PDF.

## Required data

- **Instrument:** BTC options on Deribit (large cross-section of strikes and maturities).
- **Venue:** Deribit (primary crypto options venue).
- **Market type:** Options (European-style, cash-settled).
- **Timeframe:** Daily option prices used to recover risk-neutral distributions; predictive regressions at multiple horizons (exact horizons not stated in abstract).
- **Fields:** Option prices (bid/ask/mid), strike, expiry, implied volatility, delta, underlying BTC spot price, realized returns.
- **Point-in-time:** Options data must be available in real-time at Deribit; no look-ahead required.
- **Timestamp:** UTC (Deribit standard).
- **Missing-data assumptions:** Not stated in abstract.

## Execution assumptions

- **Signal-to-order timing:** Not specified. The result is a predictability finding, not an implemented strategy.
- **Market/limit order:** Not specified.
- **Fill model:** Not specified.
- **Fees:** Not specified in abstract.
- **Slippage:** Not specified in abstract.
- **Spread:** Not specified in abstract.
- **Impact/capacity:** Not specified. BTC options on Deribit are among the most liquid crypto options globally, but capacity for factor-based strategies is unconstrained by the source.
- **Funding:** Not applicable for options positions (premia paid upfront).
- **Leverage/margin:** Not specified.
- **Borrow/shorting:** Not applicable (options strategies use premia, not borrow).
- **Latency:** Not specified (daily frequency suggests no ultra-low-latency requirement).
- **Partial fills/failures:** Not specified.

## Evidence

### Source-reported

- VRP is positive and highly persistent in BTC options (source-reported).
- Higher-order risk-neutral moments (particularly VoV) contain substantial incremental information about risk compensation beyond variance alone (source-reported).
- Option-implied factors predict BTC excess returns across multiple horizons (source-reported).
- Option-implied factors consistently outperform common sentiment- and equity-style predictors (source-reported).
- These results hold in a market with limited institutional hedging demand and decentralized market making (source-reported).

All of the above are stated in both SSRN abstracts (6410838 and 6771170). Specific numerical results (R², t-statistics, coefficient magnitudes, sample period, sample size, exact predictive horizons) are not available from the abstracts. They require access to the full 37-page PDF.

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed sources; absence is not evidence of no negative result.

## Falsification plan

1. **Out-of-sample predictive regression:** Replicate the predictive regressions on a held-out sample (e.g., last 12 months). If VoV loses statistical significance for BTC excess return prediction, the predictability hypothesis is weakened.
2. **Alternative universe/asset:** Test whether VoV predicts returns in other crypto options markets (ETH options on Deribit, Deribit SOL options). If the effect is specific only to BTC, it may reflect a single-asset anomaly rather than a general risk-premium mechanism.
3. **Transaction cost stress:** Even if predictability is real, the signal must survive transaction costs. If implementing the signal (e.g., scaling a BTC spot or perpetual position by the VoV factor) incurs costs that exceed the predicted return premium, the strategy is not actionable.
4. **Horizon sensitivity:** Test whether the predictive power of VoV is robust across different return horizons (1-day, 1-week, 1-month). If it only works at a single horizon, the finding may be fragile.
5. **Competing explanations:** Test whether the VoV predictability is subsumed by realized volatility, VIX-equivalent indices, or on-chain data. If realized vol or on-chain metrics capture the same information, the option-implied factor adds no incremental value.
6. **Data period sensitivity:** The sample likely spans specific BTC market regimes. Test whether the effect persists across bull, bear, and sideways regimes separately.

*Research-defined falsification threshold:* VoV predictive t-statistic must exceed |2.0| in the out-of-sample period and maintain positive predictive R² for at least one return horizon. If both fail, the hypothesis is rejected.

## Crypto portability

**Direct** — the mechanism is native to crypto options markets (BTC options on Deribit). The finding is specifically about crypto market microstructure: the absence of institutional hedging demand means option-implied premia more cleanly reflect risk compensation.

Crypto-specific considerations:
- Deribit is the dominant crypto options venue, so liquidity is concentrated there.
- BTC options are cash-settled in USDC, so there is no physical delivery risk.
- The 24/7 market structure means option prices update continuously, allowing daily risk-neutral distribution recovery.
- The decentralized market-making structure (no designated market makers, unlike equity options) means the risk-neutral distribution is shaped by a different participant mix.
- This paper specifically argues that intermediary-based explanations from equity markets (e.g., dealer hedging) do not apply in crypto, making the risk-premium interpretation more credible in this market.

## Limitations

- **Data access:** Full PDF not independently verified in this run due to SSRN access limitations. All specific numerical results are marked as data gap until the full paper can be reviewed.
- **Not independently reproduced:** This is a working paper result. No independent replication is available.
- **Sample period uncertainty:** Exact sample window not stated in the abstract. The paper was written March 2026, and uses Deribit data. If the sample is short or concentrated in a specific regime, generalizability is limited.
- **Exact performance numbers unavailable:** R², t-statistics, coefficient magnitudes, and predictive horizons require full paper access.
- **Implementation gap:** The paper demonstrates return predictability but does not implement a trading strategy. Translating the predictability into a tradable signal with proper execution, sizing, and risk management is an open question.
- **Single-asset study:** The result is demonstrated only for BTC. Generalizability to ETH or other crypto options is unknown.
- **Working paper status:** The paper has not yet undergone peer review.

## Implementation status

No implementation in our research stack has been completed. This is a pure research capture of an option-implied return predictability finding.

## Adoption boundary

This record is research material only. Its presence in this repository does not mean:
- The strategy is profitable;
- The VoV predictability has been validated for trading;
- The strategy has been approved for implementation;
- The strategy has been approved for paper trading, testnet, or live trading.

## Related Wiki records

- [[quant/bitcoin-option-rnd-low-volatility-high-vrp-regime-2026-09-01]] — Related: Bitcoin option-implied RND regimes and VRP decomposition (different source: arXiv:2410.15195, clustering approach). Different mechanism (regime classification vs. VoV return predictability).
- [[quant/crypto-deribit-options-volatility-of-volatility-vov-realized-quarticity-2026-09-01]] — Related: VoV in crypto options for pricing (Du & Shen 2025, JFM). Different source identity and mechanism (option pricing via affine GARCH vs. return predictability via structural risk-neutral recovery).
- [[quant/bitcoin-implied-jump-risk-premia-carry-prediction-2026-09-01]] — Related: Option-implied jump risk premia in BTC. Different mechanism (jump-risk premia vs. VoV factor).

## Sources

1. Christina V. Atanasova, Terrel Miao, Ignacio Segarra, Frederick H. Willeboordse. "What Do Crypto Options Tell Us? Risk Premia Implied by BTC Option Prices." SSRN working paper 6410838, Simon Fraser University, March 13, 2026. DOI: 10.2139/ssrn.6410838. 37 pages. https://ssrn.com/abstract=6410838
2. Same authors, updated version posted May 15, 2026 (1-page abstract): SSRN 6771170. DOI: 10.2139/ssrn.6771170. https://ssrn.com/abstract=6771170
3. Additional context: Atanasova et al. present "Illiquidity Premium and Crypto Option Returns" at NZ Finance Meeting 2025 (related work by same author group, same venue data).
