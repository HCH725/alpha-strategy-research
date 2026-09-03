---
schema: strategy-research-record-v1
title: Brown-Crypto ESG Sustainability-Uncertainty Next-Day Downside with Illiquidity Amplification
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - esg
  - sustainability-uncertainty
  - cross-sectional
  - liquidity
  - daily
status: research-only
confidence: medium
source_as_of: 2025-06-30
sources:
  - https://doi.org/10.1016/j.frl.2026.109770
  - https://www.researchgate.net/publication/401677602_Sustainability_Uncertainty_and_Cryptocurrency_Returns_Evidence_from_Green_and_Brown_Assets
  - https://ideas.repec.org/a/eee/finlet/v96y2026ics1544612326003004.html
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Brown-Crypto ESG Sustainability-Uncertainty Next-Day Downside with Illiquidity Amplification

## Provenance

Primary source: Jying-Nan Wang, Hung-Chun Liu, and Yuan-Teng Hsu, *Sustainability uncertainty and cryptocurrency returns: Evidence from green and brown assets*, *Finance Research Letters* 96 (2026), article 109770, DOI `10.1016/j.frl.2026.109770`.

The directly reviewed primary-source text in this Scout cycle is the author-uploaded full-text version publicly accessible through ResearchGate. Bibliographic metadata was cross-checked against RePEc/IDEAS. The paper studies daily data from 2020-01-01 through 2025-06-30.

Source-identity / pool-level deduplication check:

- Repository search found no record containing the title, DOI, `ESGUI`, or the same green-versus-brown sustainability-uncertainty mechanism.
- Wiki Brain read-only search likewise found no `ESGUI`, source-title, or materially equivalent dedicated strategy-research record.
- The distinctive mechanism is **aggregate ESG sustainability uncertainty -> lower next-day crypto returns, concentrated in brown / energy-intensive cryptocurrencies and amplified by illiquidity**. This is not treated as a generic sentiment, fear-and-greed, climate-policy-uncertainty, low-volatility, or liquidity-premium record.
- No second record is created from a reframed title or broad ESG narrative; this record captures the single source-supported heterogeneous return-predictability hypothesis.

Source/data as-of date: empirical sample ends 2025-06-30; article publication is 2026.

## Economic mechanism

### Source-reported

The authors argue that higher ESG-driven sustainability uncertainty can worsen investor perceptions of cryptocurrencies through environmental controversies, social concerns, governance transparency, regulatory uncertainty, and compliance risk. They report that this adverse relationship is stronger for cryptocurrencies classified as brown / energy-intensive, while green cryptocurrencies appear more resilient. They also report that lower liquidity intensifies the negative effect of ESG sustainability uncertainty on future returns.

The source interprets the cross-sectional heterogeneity as consistent with sustainability-sensitive capital reallocation and a higher risk discount for environmentally controversial or energy-intensive digital assets during periods of elevated ESG uncertainty.

### Research interpretation

The normalized hypothesis is:

- **Market-wide state:** ESG sustainability uncertainty is elevated.
- **Cross-sectional susceptibility:** brown / energy-intensive cryptocurrencies have larger negative next-day exposure than green cryptocurrencies.
- **Liquidity interaction:** within the affected universe, lower-liquidity assets should exhibit more negative next-day sensitivity.
- **Expected direction:** higher point-in-time ESG uncertainty -> lower expected next-day return for brown cryptocurrencies, with the adverse effect becoming stronger as illiquidity rises.

This can be interpreted as a slow information/risk-discount channel in which sustainability-related uncertainty increases required compensation or triggers risk reduction, while illiquidity slows or magnifies price adjustment.

A major competing explanation is **timing leakage**: the source's ESGUI is monthly and is assigned to every trading day within that month. If the month-t value was not publicly available at the start of month t, the reported daily predictive relation cannot be assumed tradable in real time. This issue is therefore the first falsification gate, not a minor implementation detail.

## Signal

### Source-reported construction

The source estimates panel regressions of one-day-ahead cryptocurrency return on the ESG-related sustainability uncertainty index and liquidity:

`Ret_(i,t+1) = beta1 * ESGUI_t + beta2 * Liquidity_(i,t) + beta3 * (ESGUI_t * Liquidity_(i,t)) + controls_t + crypto_FE + year_FE + error_(i,t+1)`

Key source definitions:

- `Ret_(i,t+1)` is the natural logarithm of the day `t+1` price divided by the day `t` price.
- `ESGUI_t` is the natural logarithm of the ESG-related uncertainty index from Ongan et al. (2025).
- ESGUI is observed monthly in the underlying source and is converted to a daily series by assigning the same monthly value to all trading days in that month.
- Primary liquidity measure is standardized Amihud illiquidity, approximately absolute daily return divided by dollar trading volume.
- Robustness liquidity measure is standardized volatility-over-volume (VoV), using the daily high-low range scaled by volume.
- Larger LIQ / VoV values denote poorer liquidity.
- The regressions include cryptocurrency fixed effects and year fixed effects; controls include VIX, USD index return, S&P 500 return, oil return, gold return, and Crypto Fear and Greed Index.

The source studies a balanced 14-cryptocurrency sample:

- Green: ADA, ALGO, ATOM, POWR, TRX, XLM, XRP.
- Brown: BCH, BTC, DOGE, ETC, ETH, LTC, XMR.
- ETH is dynamically classified as brown before the Ethereum Merge on 2022-09-15 and green afterward.

### Source-reported empirical direction

The source reports:

- Full-sample ESGUI coefficient remains significantly negative after controls.
- In the controlled full-sample model, the ESGUI coefficient is reported as `-0.669`.
- In the controlled brown-cryptocurrency subsample, the ESGUI coefficient is reported as `-1.179`.
- A one-standard-deviation ESGUI increase of approximately `0.24` is associated by the authors with about `-0.161%` next-day return in the full sample and about `-0.283%` for brown cryptocurrencies.
- For green cryptocurrencies, the ESGUI coefficient is negative but not statistically significant in the focal subgroup specification.
- The `ESGUI × illiquidity` interaction is significantly negative in the reported models, indicating a stronger adverse effect when liquidity is poorer.
- Qualitative conclusions remain under the alternative VoV liquidity measure and the equally weighted ESGUI variant.

These are source-reported regression results, not independently reproduced trading performance.

### Operational trading rule

**underspecified**.

The paper reports predictive panel regressions, not a canonical executable trading strategy. It does not provide a unique real-time publication rule for ESGUI, tradable threshold, position-sizing map, portfolio weighting rule, order type, execution venue, stop, or transaction-cost backtest.

The following is **research-proposed** solely to make the hypothesis testable and must not be represented as source-reported:

1. Use only the latest ESGUI observation whose publication timestamp is verifiably available before portfolio formation.
2. Build a point-in-time green/brown classification, including the ETH PoW-to-PoS transition and any later protocol changes.
3. Form a brown-crypto candidate set using liquid, continuously tradable instruments available at the test venue.
4. Define ESG uncertainty state using a predeclared trailing transform of point-in-time ESGUI, such as level, change, percentile, or z-score; the choice is `research-proposed` and must be fixed before OOS testing.
5. When ESG uncertainty is elevated, test a short or underweight brown-crypto portfolio relative to a market/green control; test liquidity interaction using predeclared illiquidity buckets.
6. Hold for one day because the source dependent variable is next-day return.
7. Re-form only when all required data are available; do not backfill monthly ESGUI values into earlier days of the same month.

Any threshold, ranking rule, neutralization, hedge ratio, long leg, short leg, sizing rule, rebalance timestamp, stop, and execution convention is **research-proposed**.

## Required data

- **Primary market data:** daily close, high, low, and USD trading volume for the target cryptocurrency universe.
- **Source vendor:** CoinMarketCap in the paper; a replication may use an alternative vendor only if symbol mapping, venue aggregation, timestamp conventions, and survivorship handling are explicitly controlled.
- **ESG uncertainty data:** GDP-weighted ESGUI from the Economic Policy Uncertainty data source; equally weighted ESGUI as robustness.
- **ESGUI point-in-time metadata:** publication date/time for each monthly observation, revision history, vintage, and any retroactive methodological changes. This is mandatory for a tradability test.
- **Liquidity:** Amihud illiquidity and alternative VoV measure, calculated point-in-time from daily market data.
- **Controls for source reproduction:** VIX, USD index, S&P 500, crude oil, gold, and Crypto Fear and Greed Index.
- **Green/brown classification:** a dated, auditable consensus/energy-profile classification. The source dynamically reclassifies ETH on 2022-09-15.
- **Universe:** source uses 14 representative cryptocurrencies. A modern replication must define listing, delisting, minimum history, liquidity, and survivorship rules point-in-time.
- **Timestamp:** exact 24/7 daily boundary must be specified. The reviewed source does not uniquely state a crypto UTC close convention sufficient for live execution, so this is a **data gap**.
- **Missing data:** the source does not provide a canonical imputation rule for missing crypto observations. A replication should fail closed or skip incomplete observations rather than silently impute.
- **Costs:** realistic maker/taker fees, spread, slippage, market impact, borrow/funding for short legs, and venue-specific financing costs are required for trading tests.

## Execution assumptions

### Source-reported

The source is an econometric predictability study, not an execution study. No canonical order type, venue, shorting mechanism, leverage, signal-to-order latency, rebalance clock, borrow rule, funding treatment, spread/slippage model, or market-impact model is specified.

### Research interpretation

Any trading implementation must separately specify and stress:

- the first timestamp at which the monthly ESGUI value is actually knowable;
- delay from ESGUI release to signal computation and order submission;
- crypto daily-boundary convention in a 24/7 market;
- spot versus perpetual or dated-futures implementation;
- borrow availability or perpetual funding for short brown assets;
- exchange fragmentation, delisting, and contract substitutions;
- fees, bid-ask spread, slippage, impact, and partial fills;
- exposure neutralization against broad crypto beta if the test seeks cross-sectional rather than market-directional alpha;
- liquidity caps, especially because the source predicts a stronger effect precisely where trading costs may be highest.

Using a month-t ESGUI value on days before that value was publicly released is prohibited in any causal backtest.

## Evidence

### Source-reported

Wang, Liu, and Hsu report a statistically significant negative relation between ESGUI and next-day cryptocurrency returns over 2020-01-01 to 2025-06-30. The controlled full-sample ESGUI coefficient is reported as `-0.669`, while the controlled brown-crypto subgroup coefficient is `-1.179`.

The authors translate a one-standard-deviation ESGUI change of about `0.24` into an average next-day return decrease of approximately `0.161%` for the full sample and `0.283%` for brown cryptocurrencies. The corresponding green-crypto coefficient is not statistically significant in the focal subgroup results.

The paper also reports significantly negative ESGUI-by-illiquidity interaction coefficients and obtains qualitatively similar conclusions under an alternative VoV liquidity proxy and an equally weighted ESGUI variant.

The source does **not** report a canonical net-of-cost long-short strategy, executable real-time threshold, or independently validated post-2025 trading result.

### Independently reproduced

not independently reproduced

### Negative evidence

- **Point-in-time concern:** ESGUI is monthly and the source assigns each month's value to every trading day of that same month. Without a verified contemporaneous publication timestamp, this transformation may leak future information into early-month observations.
- The green-cryptocurrency subgroup does not show the same statistically significant negative ESGUI relation, so the effect is heterogeneous rather than universal.
- The source sample is a balanced set of 14 cryptocurrencies selected partly for market capitalization and trading-history availability; this can embed survivorship/selection effects relative to a live point-in-time universe.
- The source's liquidity interaction predicts a stronger effect in less liquid assets, precisely where trading costs and shorting constraints may be more severe.
- The study reports regressions rather than net-of-cost strategy returns; economic tradability is unproven.
- ESGUI is market-wide and slow-moving, so apparent daily significance could partly reflect omitted persistent macro/sentiment states rather than a uniquely causal ESG channel.
- The source uses CoinMarketCap aggregate daily data rather than venue-specific executable prices.
- No post-2025 OOS evidence was identified in the reviewed primary source.

## Falsification plan

1. **ESGUI publication-timestamp audit.** Reconstruct the exact publication/vintage timestamp for every monthly ESGUI value. Use a value only from the first moment it was publicly available. **research-defined falsification threshold:** reject the tradable hypothesis if the negative brown-crypto next-day relation becomes economically negligible or changes sign when same-month backfill is removed.
2. **Source-sample reproduction.** Reproduce the 2020-01-01 to 2025-06-30 panel specifications using the stated 14-coin sample, ETH reclassification, controls, crypto fixed effects, and year fixed effects. **research-defined falsification threshold:** materially weaken the record if the brown-subgroup ESGUI coefficient is not negative or the liquidity interaction cannot be reproduced in sign.
3. **Strict post-source OOS.** Test from 2025-07-01 onward without refitting thresholds on the OOS period. **research-defined falsification threshold:** reject persistence if point-in-time ESGUI exposure fails to produce negative brown-crypto next-day conditional returns across the full OOS period and major subregimes.
4. **Green-versus-brown spread test.** Compare brown-minus-green next-day returns conditional on ESGUI using the same point-in-time universe and liquidity controls. **research-defined falsification threshold:** weaken the sustainability-specific interpretation if brown assets are not more negatively sensitive than green assets.
5. **Liquidity interaction robustness.** Predeclare Amihud and VoV definitions and liquidity buckets. **research-defined falsification threshold:** reject the amplification claim if the adverse ESGUI slope does not become more negative with poorer liquidity or if the interaction is unstable across both liquidity definitions.
6. **Placebo timing test.** Shift ESGUI release-aligned observations forward/backward by placebo months while preserving its marginal distribution. **research-defined falsification threshold:** materially weaken the information hypothesis if placebo timing produces equal or stronger apparent predictability.
7. **Competing macro explanation.** Add broad crypto market return, realized volatility, stablecoin stress, funding/basis, dollar, rates, VIX, commodities, CFGI, and major regulatory-news controls. **research-defined falsification threshold:** materially weaken the ESG mechanism if ESGUI loses incremental predictive content once contemporaneously available common-state controls are included.
8. **Point-in-time universe test.** Replace the balanced 14-coin sample with a live reconstituted universe using only coins eligible at each historical date. **research-defined falsification threshold:** reject generalization if the effect exists only in the ex-post balanced set.
9. **Classification robustness.** Predefine an auditable green/brown taxonomy and separately test fixed versus time-varying protocol energy status. **research-defined falsification threshold:** weaken the environmental-susceptibility interpretation if results depend on one arbitrary classification choice.
10. **Cost / borrow / funding stress.** Implement research-proposed market-neutral or directional branches with realistic venue-specific costs. **research-defined falsification threshold:** reject tradability if expected net return is non-positive after conservative spread, slippage, fee, borrow/funding, and capacity assumptions.
11. **Parameter perturbation.** Test predeclared ESGUI level/change/z-score states and adjacent liquidity cutoffs. **research-defined falsification threshold:** reject a thresholded trading interpretation if positive net expectancy appears only under one narrow ex-post-selected threshold.
12. **Publication/revision robustness.** Compare first-release ESGUI vintages with revised historical values. **research-defined falsification threshold:** reject real-time usability if predictive content is materially concentrated in revised rather than first-release data.

Failure should lead to rejection or reclassification of this hypothesis, not unconstrained retuning.

## Crypto portability

**direct**.

The source directly studies cryptocurrency returns and explicitly distinguishes green and brown digital assets. No traditional-asset transplantation is required for the core hypothesis.

However, translating the source into modern trading requires additional crypto-specific choices:

- 24/7 daily-close convention;
- venue fragmentation and executable versus aggregate CoinMarketCap prices;
- spot versus perpetual/futures implementation;
- funding and basis;
- borrow/short availability for brown assets;
- stablecoin quote-currency effects;
- listing/delisting and survivorship;
- liquidity and impact constraints;
- protocol upgrades that alter energy usage or ESG classification;
- exchange/custody risk.

Extension beyond the source's 14-coin universe is **unproven**.

## Limitations

- **not independently reproduced**.
- **underspecified:** no canonical executable threshold, order type, hedge, sizing, stop, or rebalance clock is supplied by the source.
- **data gap:** the reviewed source does not specify the precise real-time publication timestamp and revision vintage of ESGUI observations.
- **potential look-ahead:** assigning a monthly ESGUI value to all days of that same month may not be causally tradable unless the value is known before those days.
- **data gap:** exact crypto daily closing timezone used for executable signal formation is not uniquely specified in the reviewed text.
- **balanced-panel risk:** the 14-coin sample may not represent a point-in-time investable universe and can embed survivorship/selection effects.
- **classification risk:** green/brown labels are partly conceptual and can change after protocol upgrades; ETH is one documented example.
- **cost/capacity risk:** the stronger reported effect under illiquidity may be offset by worse spread, slippage, impact, and borrow availability.
- **identification risk:** ESGUI can proxy for broader macro, regulatory, climate, or sentiment uncertainty.
- **frequency mismatch:** monthly ESGUI versus daily returns limits signal refresh and increases serial dependence concerns.
- **sample limit:** empirical evidence ends 2025-06-30.
- **execution gap:** source regressions do not establish net-of-cost trading profitability.

## Implementation status

`not-implemented`.

No PyBroker, NautilusTrader, strategy registry, data pipeline, Kanban, Paper, Testnet, or Live workflow was created or modified in this Scout cycle.

## Adoption boundary

This record is `research-only`, `not-implemented`, `not-approved`, and `approval_scope: research-only`.

Presence in the Alpha Strategy Pool means only that a source-backed and falsifiable research hypothesis has been normalized for Research Intake Review. It does not mean the strategy is profitable, validated alpha, approved for implementation, approved for paper trading, approved for testnet, or approved for live trading.

No implementation task is created by this record.

## Related Wiki records

No materially equivalent dedicated Wiki Brain strategy-research record was found in the pre-write read-only search for the source title, DOI, `ESGUI`, or the green/brown sustainability-uncertainty mechanism.

Related broad families may include sentiment, macro uncertainty, liquidity, and environmental/energy-state research, but concept-level clustering and consolidation belong to Research Intake Review rather than this Scout cycle.

## Sources

1. Jying-Nan Wang, Hung-Chun Liu, and Yuan-Teng Hsu, *Sustainability uncertainty and cryptocurrency returns: Evidence from green and brown assets*, *Finance Research Letters* 96 (2026), 109770. DOI: https://doi.org/10.1016/j.frl.2026.109770
2. Author-uploaded public full text reviewed in this Scout cycle, especially Sections 2.1-2.2 and 3.2-3.5, Tables 2-6: https://www.researchgate.net/publication/401677602_Sustainability_Uncertainty_and_Cryptocurrency_Returns_Evidence_from_Green_and_Brown_Assets
3. RePEc/IDEAS bibliographic record confirming journal metadata and DOI: https://ideas.repec.org/a/eee/finlet/v96y2026ics1544612326003004.html
