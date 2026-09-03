---
schema: strategy-research-record-v1
title: Crypto Positive-Jump Variance Next-Week Reversal
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - realized-variance
  - signed-jumps
  - lottery-demand
status: research-only
confidence: high
source_as_of: 2023-06
sources:
  - "Suzanne S. Lee and Minho Wang, 'Variance Decomposition and Cryptocurrency Return Prediction', Journal of Financial and Quantitative Analysis 60(4), 1859-1890, published online 2024-04-15; DOI: https://doi.org/10.1017/S002210902400022X; open-access article/PDF: https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/variance-decomposition-and-cryptocurrency-return-prediction/9995E58095453CB44A3BC3C9C111969F"
  - "SSRN preprint DOI: https://doi.org/10.2139/ssrn.4721415"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Positive-Jump Variance Next-Week Reversal

## Provenance

- **Primary source:** Suzanne S. Lee and Minho Wang, “Variance Decomposition and Cryptocurrency Return Prediction,” *Journal of Financial and Quantitative Analysis*, Vol. 60, No. 4, June 2025, pp. 1859–1890. The article was published online on 2024-04-15. DOI: `10.1017/S002210902400022X`.
- **Stable public source:** https://doi.org/10.1017/S002210902400022X and the Cambridge open-access article/PDF linked in frontmatter.
- **Working-paper identifier:** SSRN DOI `10.2139/ssrn.4721415`.
- **Source/data as-of:** empirical sample ends June 2023; the sample begins October 2015.
- **Primary-source verification:** the Scout directly reviewed the Cambridge open-access article, including the variance definitions, Lee–Mykland jump-detection settings, sample construction, Table 4 portfolio sorts, Table 5 Fama–MacBeth decomposition, robustness tests, and mechanism discussion.
- **Pool-level source-identity check:** before writing, the staging repository was searched for the journal DOI, SSRN identifier, exact paper title, and distinctive positive-jump-variance mechanism; no source-level duplicate was found. The canonical Wiki Brain `quant/` tree was also searched read-only for the DOI/title/SSRN identifier and returned no match.
- **Why this is distinct from nearby pool records:** `crypto-cross-sectional-jump-diffusion-variance-decomposition-2026-08-31.md` is based on Leong and Kwok (2023) and ranks a bipower-variation-derived relative jump share / jump-vs-diffusion construction. `crypto-cross-sectional-realized-signed-jump-good-bad-volatility-2026-09-01.md` is based on Zhang and Zhao (2023) and uses a normalized signed-jump / semivariance construction. Lee and Wang instead identify individual jumps with the Lee–Mykland test and show that **absolute positive jump variance**, formed over the previous month, forecasts lower returns in the following week while negative jump variance loses incremental significance in the joint decomposition. The source, estimator, signal statistic, formation horizon, and identifying negative control are therefore materially different.

## Economic mechanism

### Source-reported

Lee and Wang report that cryptocurrencies with higher realized variance subsequently earn lower cross-sectional returns, and that the negative predictability is attributable to **positive jump variance** and **jump-robust variance**, rather than negative jump variance once the components are considered jointly. They connect the effect to speculative retail trading and lottery preferences: high positive-jump-variance cryptocurrencies tend to be smaller, lower priced, less liquid, more actively traded by retail participants, and associated with more positive sentiment. Their interpretation is that investors seeking a small probability of very large gains can bid up lottery-like cryptocurrencies, producing lower subsequent expected returns.

The authors explicitly examine short-selling availability and report that high-variance portfolios tend to have *more*, not less, futures trading activity. They therefore do not attribute the variance effect primarily to tighter short-sale constraints.

### Research interpretation

The falsifiable alpha hypothesis is a **cross-sectional lottery-demand reversal**: unusually large *recent positive discontinuous price variation* is a state variable for speculative overpricing. Conditional on point-in-time high-frequency data, coins with high trailing positive jump variance should underperform coins with low trailing positive jump variance over the next week.

This record deliberately isolates positive jump variance rather than treating “volatility” or “jump risk” generically. The source's joint regressions make negative jump variance a useful negative control: if upside and downside jump variance forecast subsequent returns equally after joint controls, the proposed lottery-demand channel is weakened.

The conversion from the source's predictive sort to a directional trading portfolio is **research-proposed**. The source reports High-minus-Low comparison portfolios; because the reported High-minus-Low return is negative, a testable alpha portfolio reverses that sign: long the Low positive-jump-variance tercile and short the High tercile.

## Signal

**Source-specified measurement path**

1. Use a 15-minute sampling grid. For each interval, take the latest bid and ask observation, remove quotes that remain unchanged for three consecutive intervals, form the mid quote `mid = 0.5 × (bid + ask)`, and compute 15-minute log returns.
2. Detect individual jumps using the Lee–Mykland (2008) test with local-volatility window `K = 156` at the 15-minute frequency. The source's baseline jump rejection level is 5%; it reports robustness at 1% and with a 10% false-discovery-rate filter. The paper also controls for intraday volatility patterns in jump classification.
3. For every detected positive jump within the measurement window, compute squared 15-minute return and sum it:

   `JV+_{i,w} = Σ r²_{i,t} · I(|T_{i,t}| > ζ) · I(r_{i,t} > 0)`

   where `T` is the Lee–Mykland jump statistic and `ζ` is its rejection criterion.
4. At the **end of every week `w`**, estimate the decomposed variance measure using the previous month of intraday observations, described by the source as weeks `w-3` through `w`.
5. Cross-sectionally sort eligible cryptocurrencies into **terciles** on `JV+` and observe excess returns in the **subsequent week**. The paper reports both equal-weighted and value-weighted portfolio results.

**Research-proposed trading operationalization**

- **Direction:** long the bottom `JV+` tercile; short the top `JV+` tercile. This inversion is research-proposed from the source-reported negative High-minus-Low predictive spread; it is not presented by the source as an approved trading strategy.
- **Formation timestamp:** the source states “end of every week” but does not specify a timezone or exact clock boundary. This is **underspecified**. A replication must predeclare one venue-native weekly boundary before examining results; a 24/7 UTC boundary may be used only if explicitly labeled **research-proposed**.
- **Entry timing:** source execution timing is **underspecified**. For causal testing, first executable order after all final 15-minute observations required for the formation window are available is **research-proposed**; same-bar fills are not assumed.
- **Holding / exit:** hold for the subsequent week and rebalance at the next weekly formation event. A one-week time exit is consistent with the source's dependent-return horizon; exact order timing remains **research-proposed**.
- **Weights:** equal-weight and value-weight are source-tested branches. No leverage target is specified by the source.
- **Re-entry:** weekly re-ranking is source-consistent. Buffering, hysteresis, stop losses, take profits, volatility targeting, and discretionary overrides are **not source-specified** and are excluded from this research record.
- **Ties:** source handling is **underspecified**. Any deterministic tie-breaking convention used in replication must be predeclared and labeled **research-proposed**.

## Required data

- **Original instrument/universe:** cryptocurrencies traded on Coinbase with more than nine months of intraday data; stablecoins excluded. The source's final sample contains 100 cryptocurrencies and includes a delisted coin. It reports robustness on Bitfinex and Bittrex.
- **Original sample:** October 2015 through June 2023.
- **Original vendor:** Kaiko tick-by-tick order-book quote and price data. This may require licensed data access; a public-data substitute would be an adaptation rather than an exact data replication.
- **Fields:** bid, ask, quote timestamps, 15-minute latest observation, mid quote, log returns; market capitalization for value-weighted replication. Bid-ask spread, trading volume, futures activity, retail proxy, and sentiment are required only for mechanism/heterogeneity replication, not the core `JV+` signal.
- **Timeframe:** raw/tick quote data sufficient to construct source-defined 15-minute mid-quote returns.
- **Point-in-time requirement:** only quotes known by the formation boundary may enter the previous-month window. Universe membership and eligibility must be constructed without future listing/delisting information.
- **Timestamp requirement:** source weekly timezone is **underspecified**. Quote timestamps must be normalized to one declared clock before 15-minute aggregation, and out-of-order records must be resolved causally.
- **Missing/stale data:** source removes quotes unchanged for three consecutive 15-minute intervals. Additional imputation is not source-specified and must not be silently introduced.
- **Costs / spread:** observed bid/ask is available in the source dataset, but Table 4 is an asset-pricing predictive-sort exercise rather than a full executable cost model. Realized fees, spreads, slippage, funding/borrow, and impact are required for a trading-feasibility test.

## Execution assumptions

The source does **not** specify a production execution policy, exchange fee schedule, market/limit order model, latency, participation cap, market impact, leverage, margin, partial fills, or failure handling. It notes that some cryptocurrencies can be difficult to short and uses long-short portfolios for comparison; a robustness exercise assumes Bitcoin can be shorted.

Accordingly:

- next-available-bar execution after signal availability is **research-proposed** for causal backtesting;
- using perpetual futures for a short leg is **research-proposed** and is not an exact replication of the Coinbase spot sample;
- any maker/taker fee, spread-crossing, slippage, funding, borrow, or impact model is **research-proposed** and must be parameterized from the venue/data period being tested;
- no leverage beyond a dollar-neutral comparison portfolio is assumed here;
- if a top-tercile asset is not shortable at the decision time, the exact-replication portfolio is not executable; a long-only exclusion/underweight variant is a separate adaptation and must not be conflated with the source result.

## Evidence

### Source-reported

- The study uses 100 cryptocurrencies over October 2015–June 2023, constructed from Coinbase/Kaiko intraday data with more than nine months of history and stablecoins excluded; the authors also report robustness on other exchanges.
- Table 4 sorts cryptocurrencies into terciles using the **previous month** of observations and measures **next-week** excess returns. For positive jump variance, the source reports High-minus-Low weekly excess-return spreads of **-3.6% equal-weighted** and **-2.3% value-weighted**, both marked significant at the 1% level. The corresponding 3-factor alphas are **-2.1%** and **-2.6%** per week, respectively.
- Table 5 jointly includes positive jump, negative jump, and jump-robust variance. Positive jump variance has coefficients of approximately **-1.470** and **-1.492** with t-statistics **-5.24** and **-4.69** in the reported specifications, while negative jump variance is positive but statistically insignificant (`t = 1.07` and `1.31`). Jump-robust variance remains negative and significant in the joint specifications.
- The paper reports that the positive-jump and jump-robust effects remain when the forward-return horizon is extended to two weeks and one month and when controlling for lagged returns and maximum returns. It also reports robustness across market-volatility, illiquidity, and business-cycle subsamples.
- The paper reports that the effect is stronger among smaller, lower-price, less-liquid, more retail-active cryptocurrencies and is associated with positive sentiment, supporting its lottery-preference interpretation.

These are third-party source-reported empirical results. They are **not** independently verified results of this Scout.

### Independently reproduced

not independently reproduced

### Negative evidence

- The source's negative-jump-variance sort is negative in simple portfolio sorts, but **negative jump variance is not incrementally significant** when positive jump and jump-robust variance enter the Fama–MacBeth regression jointly. This argues against a generic “all jump variance predicts reversal” interpretation.
- The source reports that volatility estimated from lower-frequency daily data is not significant in the comparable specification, implying that the effect depends materially on high-frequency variance measurement and may not survive coarse data.
- The paper's long-short portfolios are comparison devices and do not establish net tradability after real fees, spreads, short borrow/funding, slippage, or market impact.
- The sample ends in June 2023. The post-spot-ETF, later institutional, and changed venue-composition regimes are out of sample.
- The original Kaiko dataset may be licensed; exact independent replication may therefore face a data-access gap.

## Falsification plan

1. **Strict post-sample OOS test.** Freeze the source-defined 15-minute / Lee–Mykland `K=156` / 5% jump-detection / previous-month / weekly-tercile rule and evaluate on a point-in-time universe after June 2023. **Research-defined falsification threshold:** reject the directional alpha hypothesis if the net Low-minus-High `JV+` spread is non-positive over the predeclared OOS window or if its HAC t-statistic is below `2.0`. No parameter retuning after seeing OOS results.
2. **Signed-jump negative control.** Run a joint cross-sectional regression with `JV+`, `JV-`, and jump-robust variance using the same formation window. **Research-defined falsification threshold:** materially weaken the lottery-specific mechanism if `JV+` is not negative with `|t| >= 2.0`, or if `JV-` has an equal-or-larger negative standardized effect that is also significant. This tests whether direction-specific positive jumps add information rather than generic volatility.
3. **Point-in-time/leakage audit.** Rebuild universe eligibility, listings/delistings, quote filtering, and every 15-minute bucket using only data available by the formation timestamp. **Research-defined falsification threshold:** reject the replication if correcting any look-ahead or survivorship leakage eliminates the positive-jump spread or changes its sign.
4. **Jump-classification perturbation.** Predeclare the source-reported 1% jump threshold and 10% FDR-filter variants in addition to the 5% baseline. **Research-defined falsification threshold:** weaken the thesis if the Low-minus-High ordering reverses across both robustness variants; do not rescue it by searching arbitrary thresholds.
5. **Placebo test.** Randomly permute coin identities within each weekly `JV+` cross-section while preserving the time structure, and separately shift formation labels forward by one week. **Research-defined falsification threshold:** reject the signal-specific claim if the observed OOS spread is not more extreme than at least 95% of the predeclared placebo distribution.
6. **Incremental-factor control.** Control for size, lagged return, MAX return, realized skewness, liquidity, total variance, and jump-robust variance using point-in-time values. **Research-defined falsification threshold:** weaken the incremental `JV+` thesis if its OOS coefficient loses the negative sign or has `|t| < 2.0` in the predeclared joint specification.
7. **Execution/cost stress.** Apply observed venue-specific fees, bid-ask spread, slippage, borrow/funding, and a volume-based impact model to the research-proposed Low-minus-High implementation. **Research-defined falsification threshold:** reject executable-alpha feasibility if the net spread is non-positive or if realistic short availability prevents constructing the predeclared portfolio for a material share of rebalance dates.
8. **Venue robustness.** Replicate on at least two liquid venues/universes using the same clock and estimator. **Research-defined falsification threshold:** weaken portability if the sign reverses on both non-Coinbase venues or if the result exists only in stale/illiquid names excluded by practical execution filters.

## Crypto portability

**direct**

The empirical mechanism is demonstrated directly in cryptocurrency markets using 24/7 high-frequency data. Portability to a *different crypto venue or instrument*, however, is not automatic:

- Coinbase spot/Kaiko is the source sample; Binance/Bybit/OKX spot or perpetuals require new point-in-time validation.
- Perpetual futures add funding, mark/index price, liquidation, and contract-specific liquidity effects absent from the core spot return sort.
- 24/7 markets require a predeclared weekly clock boundary because the source says “end of every week” without an exact timezone.
- Venue fragmentation can cause an event to be a jump on one exchange but not another; the paper itself avoids mixing venues in the core sample because cross-exchange price deviations can contaminate high-frequency inference.
- Listing churn and short availability are material for a live cross-sectional portfolio.

Direct crypto evidence is not authorization to trade.

## Limitations

- **not independently reproduced**.
- **underspecified:** exact weekly clock/timezone, executable entry timestamp, order type, tie handling, and live re-entry/failure logic are not given by the source.
- **data gap:** exact source replication depends on historical Kaiko quote/order-book data and the paper's supplementary sample details.
- **execution gap:** source-reported predictive returns are not net executable returns and do not model present-day venue fees, spreads, slippage, funding/borrow, or impact.
- **sample/regime limitation:** empirical data end in June 2023.
- **capacity limitation:** the strongest economic mechanism is associated with smaller, lower-price and less-liquid coins, precisely where shorting and impact can be most problematic.
- **model-risk limitation:** the Lee–Mykland classification depends on local-volatility estimation, intraday-pattern adjustment, and jump threshold; misclassification can alter signed jump variance.
- **mechanism identification:** retail lottery preference is supported by cross-sectional characteristics and sentiment associations but is not a randomized causal intervention.
- This record does not merge the signal with existing relative-jump-share or realized-signed-jump records merely because they share a broad “jump/volatility” family. Their sources and normalized signal constructions are distinct at the pool stage.

## Implementation status

No implementation has been completed in the user's research stack.

`implementation_status: not-implemented`

This Scout cycle does not modify PyBroker, Nautilus, the strategy registry, any data pipeline, or any Paper/Testnet/Live workflow.

## Adoption boundary

Research material only.

`status: research-only`
`adoption: not-approved`
`approval_scope: research-only`

Presence in the Alpha Strategy Pool does not mean profitable, validated, implementation-approved, paper-approved, testnet-approved, or live-approved.

## Related Wiki records

No materially equivalent canonical Wiki Brain record was found by the pre-write source/mechanism search. No Wiki link is fabricated.

For **staging-pool dedup context only** (not canonical Wiki links), the closest existing records reviewed were:

- `crypto-cross-sectional-jump-diffusion-variance-decomposition-2026-08-31.md` — bipower-variation / relative-jump-share construction from Leong and Kwok (2023).
- `crypto-cross-sectional-realized-signed-jump-good-bad-volatility-2026-09-01.md` — realized signed-jump / good-vs-bad volatility construction from Zhang and Zhao (2023).

## Sources

1. Suzanne S. Lee and Minho Wang, “Variance Decomposition and Cryptocurrency Return Prediction,” *Journal of Financial and Quantitative Analysis*, 60(4), 1859–1890, published online 2024-04-15; journal issue June 2025. DOI: https://doi.org/10.1017/S002210902400022X
2. Cambridge University Press open-access article and PDF: https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/variance-decomposition-and-cryptocurrency-return-prediction/9995E58095453CB44A3BC3C9C111969F
3. Working-paper identifier: SSRN DOI https://doi.org/10.2139/ssrn.4721415
