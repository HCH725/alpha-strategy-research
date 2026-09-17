---
schema: strategy-research-record-v1
title: "Crypto-Market Volatility Beta: Negative Premium for Intermediate Exposure"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - volatility-risk-premium
  - DVOL
  - options-implied-volatility
  - factor-pricing
  - lottery-premium
status: research-only
confidence: medium
source_as_of: 2026-06
sources:
  - "https://doi.org/10.1016/j.ribaf.2026.101374 (Research in International Business and Finance, Volume 86, June 2026, 103374)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto-Market Volatility Beta: Negative Premium for Intermediate Exposure

## Provenance

Primary source: SeungOh Han, "The price of crypto-market volatility risk," *Research in International Business and Finance* 86 (June 2026), article 103374. DOI: https://doi.org/10.1016/j.ribaf.2026.101374.

The study examines cross-sectional cryptocurrency returns using sensitivity to Deribit's Bitcoin implied volatility index (DVOL) innovations as a systematic risk factor. Sample period: March 24, 2021 to July 26, 2024 (173 weeks). Universe: cryptocurrencies from CoinMarketCap filtered for liquidity and market capitalization. DVOL data from CryptoDataDownload; VIX from CBOE; weekly one-month T-bill rates from Ken French Data Library.

Author: SeungOh Han, Associate Professor of Finance at Sejong University (Ph.D. Finance, SUNY Buffalo). Research focuses on microstructure, asset pricing, and FinTech; published in *Journal of Empirical Finance*, *Applied Economics Letters*, *Finance Research Letters*, *Financial Innovation*, among others.

Related literature: Ang et al. (2006) on aggregate volatility risk and cross-sectional stock returns; Han (2024) on nonlinear relationship between VIX sensitivity and crypto returns; Liu, Tsyvinski & Wu (2022) on cryptocurrency factor models.

## Economic mechanism

### Source-reported

Cryptocurrencies with intermediate crypto-market volatility beta (sensitivity to DVOL innovations) systematically outperform those with extreme (high or low) beta. The author documents a negative volatility risk premium for high crypto-market volatility beta assets, meaning that cryptocurrencies most sensitive to aggregate crypto-market volatility shocks earn lower returns than those with moderate sensitivity. This negative premium is partly attributable to lottery-like characteristics: investors overpay for high-volatility-beta crypto assets because they exhibit lottery-like payoff profiles (positive skewness, high kurtosis), leading to systematic overvaluation and subsequent underperformance.

### Research interpretation

The hypothesized mechanism is a behavioral risk premium anomaly in crypto markets. Unlike the traditional equity volatility risk premium (where VIX exposure commands positive compensation), in crypto markets the most volatility-sensitive assets are systematically overpriced due to retail demand for lottery-like payoffs. This creates a cross-sectional return pattern where intermediate-volatility-beta assets earn a premium relative to both high-beta (overpriced lottery) and low-beta (insufficiently volatile to attract attention) assets.

This is distinct from idiosyncratic volatility pricing (Zhang & Li 2020) in that the factor is sensitivity to *aggregate* crypto-market volatility (systematic risk), not asset-specific idiosyncratic volatility. The DVOL-based beta captures how much each crypto asset co-moves with the aggregate implied volatility surface, not how volatile the asset itself is.

## Signal

### Formation timestamp

Weekly. DVOL innovations computed as weekly changes in the daily Deribit DVOL index. Crypto-market volatility beta for each asset estimated via rolling regression of weekly asset returns on weekly DVOL innovations over an expanding window starting March 2021.

### Lookback

Expanding window from March 24, 2021 (DVOL inception). Weekly frequency. The author does not specify a fixed lookback; the beta estimation uses the full available history up to each formation date.

### Entry

Long-short portfolio: long intermediate-volatility-beta quintiles, short extreme (highest and lowest) quintiles. The author constructs eight and twelve beta-sorted portfolios and forms long-short portfolios from the intermediate buckets versus the extremes.

### Exit

Weekly rebalance (implied by weekly formation frequency).

### Holding period

One week (weekly portfolio rebalancing).

### Parameters

- Sort: eight and twelve quantile portfolios by crypto-market volatility beta
- Long side: intermediate-beta quintiles (neither highest nor lowest)
- Short side: extreme-beta quintiles (highest and lowest)
- Dollar-neutral construction (implied by long-short portfolio design)

### Position-sizing

Not explicitly specified in the abstract. Research-proposed: equal-weight within each quintile bucket.

### Multi-timeframe dependencies

Weekly frequency. Beta estimation uses expanding window from DVOL inception (March 2021).

### Specification status

The entry/exit rules, portfolio construction details, and rebalancing frequency are derived from the paper's described methodology. Some details (exact quintile breakpoints, weighting within buckets, whether the portfolio is dollar-neutral or beta-neutral) are underspecified in the abstract and would require reading the full paper.

## Required data

- **Instrument**: Broad universe of liquid cryptocurrencies from CoinMarketCap (exact universe not specified in abstract; filtered for liquidity and market cap)
- **Venue**: Spot market data from CoinMarketCap; DVOL from Deribit/CryptoDataDownload
- **Market type**: Spot crypto returns; DVOL is an options-implied index
- **Timeframe**: Weekly returns; daily DVOL
- **Fields**: Weekly log returns for each crypto asset; daily DVOL index values; VIX (for controls); weekly T-bill rates
- **Point-in-time**: DVOL data begins March 24, 2021. The sample is constrained by DVOL availability.
- **Timestamp**: Weekly; timezone not specified
- **Missing-data**: Not specified. Research-proposed: exclude assets with insufficient data history for beta estimation.
- **Funding/fee/spread needs**: Not modeled in the paper. Research-proposed: realistic taker fees and spread assumptions would be needed for implementation.

## Execution assumptions

The paper is a factor-pricing study, not a backtest with explicit execution assumptions. The following are research-proposed for any implementation:

- Signal-to-order timing: end-of-week formation, beginning-of-week entry (research-proposed)
- Next-bar vs same-bar execution: next-week open (research-proposed)
- Market / limit order: market order assumed (research-proposed)
- Fill model: not specified in paper. Research-proposed: conservative taker fill.
- Fees: not modeled in the paper. Research-proposed: 10 bps round-trip (taker)
- Slippage: not modeled in the paper
- Impact / capacity: not addressed in the paper. Universe is large but many crypto assets are illiquid.
- Funding: not modeled (spot universe implied)
- Leverage / margin: not specified (long-short portfolio, no leverage assumed)
- Borrow / shorting: not addressed. Research-proposed: assume shorting feasible on liquid perps or via spot borrow.
- Latency: not relevant at weekly frequency
- Partial fills / failures: not addressed

## Evidence

### Source-reported

- **Long-short portfolio alpha**: Long-short portfolios of intermediate versus extreme crypto-market volatility beta quintiles yield five-factor alphas of 2.980% (eight portfolios) and 5.206% (twelve portfolios) per week, significant at the 10% level or better.
- **Weekly return difference**: Cryptocurrencies with intermediate crypto-market volatility beta outperform those with extreme risk by 5.221% weekly.
- **Negative premium**: High crypto-market volatility beta earns a negative risk premium, consistent with lottery-like overvaluation.
- **Robustness**: Results hold across eight and twelve quantile portfolios, various alternative specifications, and after controlling for conventional factors including equity-market volatility (VIX).
- **Distinct from equity volatility**: The crypto-market volatility risk premium is predominantly a distinct effect, not fully attributable to equity-market volatility innovations.
- Sample period: December 2021 to July 2024 (full sample); March 2021 to July 2024 (DVOL availability).

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed sources; absence is not evidence of no negative result.

## Falsification plan

1. **Out-of-sample test**: Replicate on a hold-out period beyond July 2024 using fresh DVOL data and an updated crypto universe. The original sample ends July 2024; any extension beyond this is out-of-sample. (Research-defined falsification threshold: five-factor alpha of long-short portfolio must remain positive and statistically significant at the 5% level in the hold-out period.)
2. **Transaction cost stress**: Re-run with realistic taker fees (minimum 10 bps round-trip) and spread assumptions. The paper does not model costs; if the 5.221% weekly return difference is eroded by realistic execution costs, the edge is not tradeable. (Research-defined threshold: net alpha must remain positive after 10 bps round-trip costs.)
3. **Liquidity filter**: Restrict the universe to assets above a minimum daily volume threshold (e.g., $1M daily) to test whether the effect survives in tradeable assets. (Research-defined: effect must persist in top-50% by volume.)
4. **Regime decomposition**: Split the sample by Bitcoin return regime (bull/bear/sideways) and test whether the intermediate-beta premium is concentrated in one regime or persists across regimes. (Research-defined: premium must be positive in at least two of three regimes.)
5. **Factor ablation**: Test whether the DVOL-beta factor survives inclusion of standard crypto factors (market, size, momentum from Liu, Tsyvinski & Wu 2022) and VIX sensitivity. The paper claims distinctness from equity volatility; this must be confirmed by factor spanning tests.
6. **Lottery mechanism test**: If the premium is driven by lottery-like overvaluation, then the intermediate-beta premium should be stronger in periods of high retail participation (measured by e.g., Google Trends for "crypto" or social media volume). (Research-defined: interaction term between retail proxy and beta-sorted returns should be significant.)

## Crypto portability

The source is already a crypto study using Deribit DVOL (Bitcoin options implied volatility) and cryptocurrency spot returns. The mechanism is native to crypto markets.

However, the implementation surface is spot crypto, not perpetual futures. Porting to perpetual futures would require:
- Replacing spot returns with perpetual futures returns (which include funding rate effects)
- Adjusting for the different return dynamics of leveraged instruments
- Accounting for the fact that high-volatility-beta perpetuals may have elevated funding rates, which could either amplify or dampen the lottery effect

Spot vs perpetual differences: The paper studies spot returns. Perpetual futures introduce funding rate payments that could distort the signal, especially for high-volatility-beta assets where funding is typically elevated.

Mark/index price: Not applicable (spot study).

## Limitations

- **Data gaps**: The paper does not specify the exact universe composition, liquidity filters, or whether survivorship bias is addressed. The CoinMarketCap universe may include delisted or dead tokens.
- **Not independently reproduced**: The results have not been replicated by an independent researcher.
- **Transaction costs not modeled**: The paper is a factor-pricing study, not a backtest. Whether the 5.221% weekly return difference survives realistic execution costs is unknown.
- **Short-selling feasibility**: The long-short portfolio requires shorting crypto assets, which may not be feasible for all assets in the universe (especially small-cap alts).
- **Sample period**: The study covers March 2021 to July 2024, which is a specific market regime (post-2021 bull, 2022 bear, 2023-24 recovery). Whether the effect persists in different regimes is untested.
- **Lottery mechanism is correlational**: The author shows the negative premium is "partly explained by lottery-like characteristics" but does not provide a causal mechanism.
- **DVOL availability**: DVOL data begins March 2021, limiting the sample to approximately 3 years. This is a short period for factor-pricing studies.
- **Underspecified implementation**: The exact portfolio construction, weighting, rebalancing, and execution details are not fully specified in the abstract.

## Implementation status

Not implemented. This is a factor-pricing research finding, not a trading strategy. No implementation in our research stack has been completed.

## Adoption boundary

This record is research material only. A record being present in this repository does **not** mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

The 5.221% weekly return difference is a gross, source-reported figure from a factor-pricing study. Whether it translates to a tradeable edge after costs, short-selling constraints, and liquidity filtering is unknown.

## Related Wiki records

- `[[quant/crypto-cross-sectional-idiosyncratic-volatility-pricing-2026-08-31]]` — Tests idiosyncratic volatility (IVOL) as a cross-sectional factor in crypto. Distinct mechanism: IVOL is asset-specific, while crypto-market volatility beta is sensitivity to aggregate DVOL innovations.
- `[[quant/crypto-options-dvol-iv-premium-shock-spot-predictor-2026-09-13]]` — Uses DVOL IV premium as a time-series predictor for spot returns. Distinct mechanism: time-series lead-lag vs. cross-sectional factor pricing.
- `[[quant/crypto-volatility-risk-premium-variance-swap-estimator-fragility-decay-2026-09-12]]` — Studies variance risk premium via variance swap estimators. Related topic (volatility risk premium) but different methodology and market structure.

## Sources

1. SeungOh Han, "The price of crypto-market volatility risk," *Research in International Business and Finance* 86 (June 2026), article 103374. DOI: https://doi.org/10.1016/j.ribaf.2026.101374. Source as-of: June 2026 (publication date). Sample period: March 24, 2021 to July 26, 2024.
