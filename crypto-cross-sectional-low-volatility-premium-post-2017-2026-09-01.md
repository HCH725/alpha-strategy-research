---
schema: strategy-research-record-v1
title: Crypto Cross-Sectional Low-Volatility Premium in the Post-2017 Market
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - volatility
  - low-volatility
status: research-only
confidence: medium
source_as_of: "underspecified in public abstract; source published 2026-03"
sources:
  - https://doi.org/10.1016/j.frl.2026.109851
  - https://ideas.repec.org/a/eee/finlet/v97y2026ics1544612326003818.html
  - https://doi.org/10.1016/j.frl.2020.101683
  - https://econpapers.repec.org/article/eeefinlet/v_3a40_3ay_3a2021_3ai_3ac_3as154461232030667x.htm
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - Burggraf and Rudolf (2021) find no significant low-volatility premium in 1,000 cryptocurrencies from 2013-04-28 through 2019-11-01, whereas Pyo and Jang (2026) report a statistically and economically meaningful low-volatility premium in the post-2017 market.
---

# Crypto Cross-Sectional Low-Volatility Premium in the Post-2017 Market

## Provenance

Primary source: Sujin Pyo and Huisu Jang, “Revisiting the low-volatility anomaly in cryptocurrency markets,” *Finance Research Letters* 97 (2026), article 109851. DOI: https://doi.org/10.1016/j.frl.2026.109851. RePEc/IDEAS bibliographic record: https://ideas.repec.org/a/eee/finlet/v97y2026ics1544612326003818.html.

The reviewed public abstract states that the paper studies the cross-sectional relation between ex-ante volatility and subsequent cryptocurrency returns using volatility-sorted portfolios. It reports that lower-realized-volatility cryptocurrencies outperform higher-volatility counterparts across multiple formation windows and holding horizons in the post-2017 period, with a stronger premium in later subperiods. It also reports robustness to market-wide crypto exposure, exclusion of extreme Bitcoin episodes, and a fixed cohort of pre-2019 listed assets.

Contradictory earlier source: Tobias Burggraf and Markus Rudolf, “Cryptocurrencies and the low volatility anomaly,” *Finance Research Letters* 40 (2021). DOI: https://doi.org/10.1016/j.frl.2020.101683. Their public abstract reports no significant low-volatility premium for 1,000 cryptocurrencies over 2013-04-28 through 2019-11-01.

The exact Pyo–Jang sample start/end dates, exchange universe, eligibility filters, realized-volatility estimator, portfolio breakpoints, weighting convention, and exact formation/holding windows are **underspecified** in the public abstract reviewed in this Scout cycle. They are not inferred here.

## Economic mechanism

### Source-reported

Pyo and Jang interpret the emergence of a low-volatility premium relative to earlier crypto evidence as consistent with market maturation. They argue that deeper liquidity, greater market depth, and increased institutional participation may have caused cryptocurrency return dynamics to resemble the low-volatility relation documented in traditional asset classes more closely.

The source reports that the premium becomes more pronounced in later subperiods and remains after several robustness checks intended to reduce market-beta, extreme-Bitcoin-episode, selection, and survivorship concerns.

### Research interpretation

The falsifiable hypothesis is that, in a sufficiently mature cryptocurrency cross-section, **ex-ante realized volatility is negatively related to subsequent returns** after basic eligibility and liquidity controls: lower-volatility assets should outperform higher-volatility assets on average.

This should be treated as a regime-dependent anomaly rather than a timeless crypto law because the earlier Burggraf–Rudolf sample finds no significant low-volatility premium. A plausible interpretation is that the sign or strength of volatility pricing changes as the market transitions from thin, highly speculative early trading toward deeper and more institutionalized participation.

A competing explanation is limits-to-arbitrage or universe composition: high-volatility assets may be smaller, less liquid, newer, and harder to short or trade, so an apparent low-volatility premium could partly reflect size, liquidity, listing-age, survivorship, or execution-cost effects rather than volatility itself.

## Signal

Source-faithful normalized signal family with explicit gaps preserved:

1. At each formation date, construct a point-in-time eligible cryptocurrency universe.
2. Using only returns observable before the formation timestamp, estimate each asset’s ex-ante realized volatility over a trailing formation window.
3. Rank assets cross-sectionally from lowest to highest realized volatility.
4. Form volatility-sorted portfolios.
5. The focal directional hypothesis is **long lower-volatility assets and short / compare against higher-volatility assets**.
6. Hold for the subsequent source-defined holding horizon, then re-form.
7. Repeat across multiple formation windows and holding horizons rather than relying on one optimized specification.

The reviewed public abstract does **not** expose the exact volatility estimator, annualization convention, formation-window lengths, holding-period lengths, number of portfolios, breakpoint method, weighting rule, rebalance timestamp, minimum listing history, stablecoin treatment, or tradeability screen. These details remain **underspecified** and must not be silently invented.

## Required data

- Point-in-time cryptocurrency listing and delisting universe.
- Spot close prices or the exact market-type prices used by the source.
- Daily returns sufficient to estimate trailing realized volatility across multiple windows.
- Point-in-time market capitalization and circulating supply for size controls.
- Trading volume, turnover, spread, and/or Amihud-style illiquidity measures.
- Listing age and asset metadata to identify stablecoins, wrapped assets, migrations, redenominations, and stale prices.
- Market-wide cryptocurrency return factor / Bitcoin return for robustness controls.
- UTC or explicitly defined venue timestamp convention.
- If adapted to perpetual futures: point-in-time contract availability, funding, mark/index prices, open interest, contract specifications, and liquidation constraints.

## Execution assumptions

Execution details are **underspecified** in the reviewed public abstract.

A leakage-safe reproduction should form volatility ranks only after the final return used in the lookback is observable and execute at the next realistically tradable timestamp.

Material assumptions that require explicit modeling include:

- market versus limit execution;
- maker/taker fees;
- bid-ask spread;
- slippage and market impact;
- turnover at each reconstitution;
- spot borrow / short availability;
- capacity in high-volatility small-cap assets;
- delisting and stale-price handling;
- partial fills;
- funding and liquidation risk if implemented with perpetuals.

Because the short leg may contain volatile, less liquid assets, gross long-short evidence can materially overstate harvestable net alpha.

## Evidence

### Source-reported

Pyo and Jang (2026) report a statistically and economically meaningful low-volatility premium in the post-2017 cryptocurrency market: cryptocurrencies with lower realized volatility outperform higher-volatility counterparts across multiple formation windows and holding horizons. Their public abstract states that the premium becomes stronger in later subperiods.

The source also reports robustness after controlling for market-wide cryptocurrency exposure, excluding extreme Bitcoin episodes, and restricting the sample to a fixed cohort of assets listed before 2019 to address selection and survivorship concerns.

No exact return spread, Sharpe ratio, t-statistic, formation-window value, holding-period value, or portfolio breakpoint is quoted here because those quantities were not visible in the reviewed public abstract.

### Independently reproduced

Not independently reproduced.

### Negative evidence

Burggraf and Rudolf (2021) construct long-short portfolios over a sample of 1,000 cryptocurrencies from 2013-04-28 through 2019-11-01 and report **no evidence of a significant low-volatility premium**, including after varying sample size, rebalancing periods, and portfolio construction methodologies.

This directly contests any claim that low-volatility outperformance is stable across the full history of cryptocurrency markets. The newer result may represent a genuine structural change, a different universe/methodology, or a sample-specific outcome.

No independent post-publication replication was performed in this Scout cycle.

## Falsification plan

The post-2017 low-volatility hypothesis should be materially weakened or rejected if a modern point-in-time replication finds any of the following:

1. Low-minus-high volatility portfolio returns are nonpositive after realistic transaction costs.
2. The negative volatility–future-return relation disappears after controlling for size, liquidity, listing age, momentum, and market beta.
3. Results are concentrated in a small number of illiquid or stale-price assets.
4. A fixed pre-existing cohort or full delisting-aware universe removes the effect.
5. The sign fails across nearby, predeclared formation and holding windows.
6. The effect is confined to one bull or bear subperiod and vanishes in later untouched data.
7. Long-leg performance is not distinguishable from a generic quality/liquidity exposure, or the short leg is practically untradeable.
8. Results cannot be reproduced across independent data vendors or major venues.

A valid replication should report gross and net results, equal-weight and value-weight variants, long and short legs separately, turnover, capacity proxies, liquidity-matched comparisons, and subperiod stability.

## Crypto portability

**Direct**, because both cited empirical papers study cryptocurrency markets.

However, market-segment portability remains conditional:

- A spot implementation is conceptually closest unless the full Pyo–Jang paper specifies another market type.
- A perpetual-futures adaptation is **adapted / unproven** because the contract universe is narrower and introduces funding, leverage, liquidation, and mark/index mechanics.
- Exchange-specific listing policies can materially alter the high-volatility tail of the cross-section.
- Crypto trades 24/7, so volatility formation and rebalance boundaries must use fixed timestamps.
- Circulating-supply revisions, token migrations, wrapped assets, and delistings can distort point-in-time universe construction.

## Limitations

- **Not independently reproduced.**
- **contested:** the 2021 and 2026 peer-reviewed studies report materially different conclusions.
- **underspecified:** exact Pyo–Jang sample dates, venue/universe, volatility estimator, formation windows, holding horizons, portfolio breakpoints, weighting convention, and rebalance timestamp were not recoverable from the reviewed public abstract.
- **data gap:** exact source data as-of date is not visible in the public bibliographic material reviewed here.
- **execution gap:** net profitability may be materially lower than gross long-short evidence because high-volatility assets can be expensive or impossible to short and trade.
- **structural-break risk:** the core thesis itself depends on market maturation, so historical stability cannot be assumed.
- **factor-confounding risk:** realized volatility may proxy for size, liquidity, listing age, speculative demand, or lottery preference.
- **unproven** for perpetual-futures adaptation.

## Implementation status

No implementation in PyBroker, NautilusTrader, the strategy registry, any data pipeline, Paper, Testnet, Demo, or Live trading has been created or modified.

`implementation_status: not-implemented`

## Adoption boundary

This record is research material in the Alpha Strategy Pool only. It is not evidence of validated alpha, not an implementation task, and not approval for Paper, Testnet, Demo, or Live trading.

`status: research-only`

`adoption: not-approved`

`approval_scope: research-only`

## Related Wiki records

No Hermes Wiki Brain record was queried, created, or modified in this Scout cycle.

Related Alpha Strategy Pool artifacts include volatility-managed momentum and realized-moment records, but none captures this exact cross-sectional low-versus-high realized-volatility hypothesis from Pyo and Jang (2026).

## Sources

1. Sujin Pyo and Huisu Jang, “Revisiting the low-volatility anomaly in cryptocurrency markets,” *Finance Research Letters* 97 (2026), 109851. DOI: https://doi.org/10.1016/j.frl.2026.109851
2. RePEc/IDEAS bibliographic record and public abstract for Pyo and Jang (2026): https://ideas.repec.org/a/eee/finlet/v97y2026ics1544612326003818.html
3. Tobias Burggraf and Markus Rudolf, “Cryptocurrencies and the low volatility anomaly,” *Finance Research Letters* 40 (2021). DOI: https://doi.org/10.1016/j.frl.2020.101683
4. EconPapers bibliographic record and public abstract for Burggraf and Rudolf (2021): https://econpapers.repec.org/article/eeefinlet/v_3a40_3ay_3a2021_3ai_3ac_3as154461232030667x.htm
