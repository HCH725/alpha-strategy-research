---
schema: strategy-research-record-v1
title: Crypto Fear & Greed Weekly AR(1) Innovation Risk Premium
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - sentiment
  - fear-and-greed
  - latent-factor
  - risk-premium
status: research-only
confidence: medium
source_as_of: 2026-07-21
sources:
  - https://arxiv.org/abs/2601.07664
  - https://arxiv.org/html/2601.07664
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Fear & Greed Weekly AR(1) Innovation Risk Premium

## Provenance

Primary source: Matthew Brigida, *Crypto Pricing with Hidden Factors*, arXiv:2601.07664, current public draft dated 2026-07-21.

The source studies weekly cryptocurrency returns from 2023-01-01 through 2024-12-31. Its universe contains any non-stablecoin cryptocurrency that entered the CoinMarketCap top 100 by market capitalization at any point during the sample, producing 253 unique cryptocurrencies and 105 weekly observations. The author states that this construction is intended to reduce survivorship bias.

The focal hypothesis in this record is the paper's **Fear & Greed state-variable innovation**, not its separate Hacks / market-cap variable. The paper converts the CoinMarketCap Fear & Greed series to weekly percent changes and then uses the residual from an AR(1) model as the non-tradable sentiment shock. It estimates the price of risk for this shock with the Giglio-Xiu three-pass latent-factor method.

Repository-wide source-identity checks on 2026-09-04 found one existing record from the same paper, `crypto-security-shock-cross-sectional-factor-hacks-mktcap-2026-09-01.md`, but that record captures a materially different **security-shock / hacked-value** hypothesis. The current record is distinct because it uses a different source variable, economic mechanism, data dependency, and estimated risk premium. A separate pool record, `crypto-cross-sectional-sentiment-risk-beta-premium-2026-09-01.md`, uses Han (2025), the Alternative.me daily Fear & Greed Index, and rolling asset-level sentiment betas; it is therefore also materially distinct from the weekly CoinMarketCap AR(1)-innovation construction here.

## Economic mechanism

### Source-reported

The source treats Fear & Greed as a non-tradable state variable intended to capture changing investor sentiment in cryptocurrency markets. The paper converts the index to percent changes and removes predictable persistence with an AR(1), so the factor used in pricing tests is the **unexpected innovation** rather than the raw sentiment level.

Using the Giglio-Xiu latent-factor procedure, the source reports a negative estimated price of risk for the Fear & Greed innovation: `-0.051` with bootstrap `p = 0.058` in Table 5. The author interprets this as evidence that shocks to Fear & Greed may affect cryptocurrency expected returns after controlling for latent common factors.

The source does **not** report a complete executable long-short trading strategy based on this result.

### Research interpretation

A falsifiable interpretation is that exposure to unexpected market-wide sentiment changes is priced differently across cryptocurrencies. If the negative estimated price of risk is stable, cryptocurrencies with more positive loading on unexpected increases in Fear & Greed should, all else equal, carry lower subsequent expected returns than cryptocurrencies with lower or negative loading.

This is a **risk-premium / behavioral-state hypothesis**, not evidence of simple timing from the raw Fear & Greed level. The AR(1) residualization matters economically: a predictable high-sentiment level is not the same object as a new sentiment shock.

The most direct strategy translation is therefore a **research-proposed cross-sectional exposure sort** on each asset's loading to the point-in-time Fear & Greed innovation. That operationalization is not source-reported and must not be treated as an implemented rule.

## Signal

The source fully specifies the aggregate state-variable transformation but does not specify a tradeable portfolio built from asset-level sentiment exposure. The signal is therefore **underspecified as a trading strategy**.

Source-specified state variable:

1. At weekly frequency, obtain the CoinMarketCap Fear & Greed index.
2. Convert the index to percent change, as described by the source.
3. Fit an AR(1) model to the weekly transformed series.
4. Use the AR(1) residual as the unexpected Fear & Greed innovation.
5. In the source's asset-pricing test, map observed factors into latent return factors through the Giglio-Xiu three-pass estimator and estimate the price of risk associated with the Fear & Greed innovation.

Research-proposed testable portfolio translation:

- **Formation timestamp:** after the relevant weekly CoinMarketCap Fear & Greed observation has actually been published and the AR(1) residual can be computed without using future observations. Exact CoinMarketCap historical publication timestamps are a **data gap** and must be reconstructed point-in-time before testing.
- **Exposure estimation:** `research-proposed` rolling regression or rolling covariance estimate of each eligible cryptocurrency's weekly excess return sensitivity to the Fear & Greed innovation, using only observations available before formation.
- **Lookback:** `research-proposed`; predeclare 52 weeks as the primary window and test 26/78-week perturbations without choosing after observing results.
- **Entry / ranking:** `research-proposed`; if the negative price-of-risk hypothesis is retained, rank assets by estimated sentiment-innovation beta and test long the lowest-beta quartile versus short the highest-beta quartile.
- **Holding period:** `research-proposed` one week, aligned with the source sampling frequency.
- **Rebalance:** `research-proposed` weekly after all required observations become available.
- **Sizing:** `research-proposed` equal-weight and value-weight variants, reported separately.
- **Ties:** `research-proposed` deterministic secondary sort by market capitalization, then asset identifier.
- **Stop / take-profit / leverage:** not source-specified; none should be added to the primary replication.

No threshold, beta window, execution clock, or portfolio breakpoint above is source-reported unless explicitly identified as such.

## Required data

Source-required data:

- Weekly returns for non-stablecoin cryptocurrencies that were in the CoinMarketCap top 100 at any point during the 2023-2024 sample.
- Point-in-time market capitalization for universe construction and value weighting.
- CoinMarketCap Fear & Greed index.
- Risk-free rate for excess-return construction.
- Additional factors used by the source for the broader pricing model, including crypto market, size, momentum, TVL, equity-market and industry factors, Altcoin Season, Hacks, and CVX, when reproducing Table 5 rather than only the focal state-variable transform.

Point-in-time requirements:

- historical constituent eligibility must be reconstructed without using future top-100 membership;
- Fear & Greed publication timestamp and any historical revisions must be recorded;
- weekly percent-change inputs must use only values available by formation time;
- AR(1) estimation must be expanding or rolling point-in-time for a causal trading test; fitting the AR(1) on the complete sample and backfilling residuals would create look-ahead;
- missing values must remain missing unless an explicit, predeclared treatment is used; silent imputation is not allowed.

Crypto implementation data, if the research-proposed portfolio is tested:

- spot and/or perpetual prices with a declared venue rule;
- bid/ask spread, fees, slippage, funding, mark/index price, open interest, and shortability for every long/short asset;
- delisting and listing history;
- stablecoin quote-currency mapping and timestamp normalization to one declared UTC weekly boundary.

## Execution assumptions

The source is an asset-pricing study and does not specify execution mechanics for a sentiment-beta trading portfolio.

For any later causal test, the following are **research-proposed** assumptions rather than source claims:

- compute the signal only after the Fear & Greed observation and all weekly return inputs are available;
- place orders no earlier than the first executable timestamp after signal formation;
- test next-period marketable execution and a more conservative delayed/TWAP implementation separately;
- include maker/taker fees, observed spread, slippage, and market impact;
- for perpetuals, include funding and mark/index-price conventions;
- require historical shortability / contract existence on the short leg;
- no leverage in the primary falsification test;
- partial fills or unavailable shorts reduce the investable universe rather than being silently assumed filled.

The source-reported price of risk is not a net-of-cost trading return.

## Evidence

### Source-reported

The source reports:

- Sample: 105 weekly observations from 2023-01-01 through 2024-12-31 and 253 unique non-stablecoin cryptocurrencies that entered the CoinMarketCap top 100 during the period.
- Fear & Greed construction: CoinMarketCap Fear & Greed is converted to percent change and, together with the other non-tradable state variables, transformed to its residual component using an AR(1) model.
- Table 5, Giglio-Xiu latent-factor specification: Fear & Greed estimated price of risk `-0.051`, bootstrap `p = 0.058`.
- Table 5, conventional Fama-MacBeth comparison: Fear & Greed estimate `-0.009`, `p = 0.026`.
- The author concludes that there is evidence that shocks to the Fear & Greed index may affect cryptocurrency expected returns, while emphasizing the short and evolving crypto sample.

These are source-reported asset-pricing results, not independently verified strategy returns.

### Independently reproduced

not independently reproduced

### Negative evidence

- The Giglio-Xiu result is only marginal at conventional levels (`p = 0.058`), so the focal evidence is not strong enough to treat the factor as established.
- The sample is only 2023-2024, a short period with 105 weekly observations; regime stability after 2024 is **unproven**.
- The estimated Altseason effect is significant in Fama-MacBeth but not in the latent-factor model, illustrating that observed crypto state variables can lose apparent pricing power after latent common factors are controlled. This is direct warning that omitted-factor correction materially changes conclusions.
- The paper does not provide a net-of-cost sentiment-beta trading backtest.
- Publication timing for historical CoinMarketCap Fear & Greed observations is a **data gap** for causal trading reconstruction.
- A separate existing pool record based on Han (2025) studies daily Alternative.me sentiment beta and a nonlinear cross-sectional relation; differing provider, horizon, model, and sample mean the two findings should not be conflated as independent confirmation of the same exact signal.

## Falsification

1. **Primary source reproduction.** Reproduce the source's weekly Fear & Greed transformation and Giglio-Xiu estimate on the 2023-2024 sample. **Research-defined falsification threshold:** if the sign of the Fear & Greed price of risk is non-negative or the two-sided bootstrap `p >= 0.10`, treat the focal source result as not reproduced and do not advance the tradeable translation.

2. **Strict post-2024 OOS.** Freeze the source transformation and the predeclared research-proposed exposure-sort method, then evaluate only 2025 onward. **Research-defined falsification threshold:** reject the directional long-low-beta / short-high-beta hypothesis if the net spread return is `<= 0` over the predeclared OOS period or if its HAC t-statistic is `< 2.0`.

3. **Point-in-time publication audit.** Reconstruct the actual availability time of each CoinMarketCap Fear & Greed value and estimate AR(1) residuals causally. **Research-defined falsification threshold:** if correcting publication lag or full-sample residualization reverses the sign of the OOS spread or removes the source-sign pricing relation, reject the causal implementation.

4. **Parameter perturbation.** Predeclare 26/52/78-week beta windows and quartile/tercile breakpoints. **Research-defined falsification threshold:** if the sign is positive only for one isolated parameter combination and flips for the majority of adjacent specifications, classify the result as unstable and reject promotion.

5. **Placebo.** Randomly permute weekly Fear & Greed innovations within calendar-year blocks and rerun the full cross-sectional test. **Research-defined falsification threshold:** if the true-signal statistic does not exceed the 95th percentile of the placebo distribution, reject the sentiment-specific explanation.

6. **Competing-explanation control.** Add crypto market, size, momentum, liquidity, MAX/lottery, and the existing Alternative.me sentiment-beta signal where available. **Research-defined falsification threshold:** if the Fear & Greed innovation exposure loses sign consistency and incremental alpha after controls, classify it as redundant rather than independent alpha.

7. **Venue / cost stress.** Test liquid spot and perpetual subsets with observed fees, spreads, slippage, funding and shortability. **Research-defined falsification threshold:** if the OOS long-short spread is non-positive after realistic costs on every practical venue subset, reject tradeability even if the statistical price-of-risk estimate survives.

8. **Capacity / universe robustness.** Re-run with point-in-time top-50, top-100, and perpetual-listed universes. **Research-defined falsification threshold:** if the effect exists only in assets that cannot be shorted or whose quoted depth cannot support the predeclared participation cap, classify the effect as non-actionable.

Failure of the trading translation does not invalidate the source's descriptive asset-pricing result; it invalidates only the stronger alpha implementation hypothesis.

## Crypto portability

direct

The source, state variable, universe, and empirical pricing tests are all cryptocurrency-native. A tradeable implementation still depends on whether the CoinMarketCap index can be reconstructed point-in-time and whether the cross-sectional short leg is feasible.

Spot portability risks include fragmented venues, quote-currency differences, delistings, and lack of borrow. Perpetual portability adds funding, mark/index construction, contract-listing survivorship, liquidation mechanics, and the fact that the perpetual universe is narrower than the source's spot-like CoinMarketCap universe. Crypto trades continuously, so the weekly boundary must be declared explicitly rather than inherited from an equity-market session.

## Limitations

- **not independently reproduced**
- **underspecified trading rule:** the source reports an asset-pricing factor price, not an executable portfolio based on sentiment exposure.
- **data gap:** historical point-in-time publication timestamps and revisions for CoinMarketCap Fear & Greed were not established in this Scout cycle.
- **short sample:** 2023-2024 only.
- **weak-to-marginal statistical strength:** the latent-factor estimate has `p = 0.058`.
- **model dependence:** the numerical price of risk differs materially between Giglio-Xiu and Fama-MacBeth specifications.
- **latent-factor interpretation:** statistical pricing does not establish a unique behavioral causal channel.
- **execution gap:** no source-level fees, spread, slippage, funding, borrow, impact, or capacity backtest for the proposed beta-sort portfolio.
- **provider specificity:** CoinMarketCap Fear & Greed is not identical to Alternative.me Fear & Greed and should not be substituted silently.
- **current-regime validity unproven:** the source sample ends 2024-12-31.

## Implementation status

No implementation has been completed in PyBroker, NautilusTrader, Paper, Testnet, or Live workflows.

`implementation_status: not-implemented`

This record defines a research hypothesis and falsification path only. It creates no implementation task.

## Adoption boundary

`status: research-only`

`adoption: not-approved`

`approval_scope: research-only`

Presence in the Alpha Strategy Pool does not imply profitability, validated alpha, implementation approval, Paper approval, Testnet approval, or Live approval.

## Related Wiki records

No Hermes Wiki Brain strategy record was modified or promoted in this Scout cycle.

Related Alpha Strategy Pool records used for deduplication/context:

- `crypto-security-shock-cross-sectional-factor-hacks-mktcap-2026-09-01.md` — same primary paper, materially distinct Hacks / market-cap state variable.
- `crypto-cross-sectional-sentiment-risk-beta-premium-2026-09-01.md` — different Han (2025) source, Alternative.me daily index, asset-level sentiment-beta construction, and nonlinear cross-sectional hypothesis.

No stable Hermes Wiki Brain link is asserted here beyond the canonical strategy-research specification read for this run.

## Sources

1. Matthew Brigida, *Crypto Pricing with Hidden Factors*, arXiv:2601.07664, current public draft dated 2026-07-21. https://arxiv.org/abs/2601.07664
2. Public full-text HTML for the same paper, including data construction, factor definitions, Table 5, and conclusions. https://arxiv.org/html/2601.07664
