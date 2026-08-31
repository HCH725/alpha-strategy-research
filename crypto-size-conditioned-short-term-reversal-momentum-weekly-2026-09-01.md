---
schema: strategy-research-record-v1
title: Crypto Size-Conditioned Short-Term Reversal versus Momentum
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - momentum
  - reversal
  - size
status: research-only
confidence: medium
source_as_of: 2025
sources:
  - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6628860
  - https://doi.org/10.2139/ssrn.6628860
  - https://www.quantseeker.com/p/weekly-research-recap-a23
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - Existing crypto literature reports strong dependence of short-horizon continuation/reversal on liquidity, universe construction, and formation horizon; the source itself attributes only part of the size split to liquidity and idiosyncratic volatility.
---

# Crypto Size-Conditioned Short-Term Reversal versus Momentum

## Provenance

Primary source: Zezhou Xu and Fenglin Wu, “Size-Momentum Puzzle in Cryptocurrencies,” SSRN working paper, 15 pages, posted 22 April 2026. SSRN abstract page: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6628860. DOI: https://doi.org/10.2139/ssrn.6628860.

The primary public abstract states that the sign of short-term return predictability varies monotonically with cryptocurrency size: small coins exhibit short-term reversal, while large coins exhibit momentum. It further states that the small-coin effect is driven mainly by rebounds among recent losers, whereas the large-coin effect reflects continued underperformance dynamics.

Secondary public research summary used only for quantitative/contextual details not visible in the primary abstract: QuantSeeker, “Weekly Research Recap,” 2026, https://www.quantseeker.com/p/weekly-research-recap-a23. That summary attributes a 2018–2025 sample to Xu and Wu and reports the smallest size quintile as showing a 4.9% one-week loser-minus-winner reversal spread, versus approximately +1.0% winner-minus-loser momentum in the largest size quintile. These figures are secondary-source-reported and have not been independently checked against the full paper tables in this Scout cycle.

Exact sample end date, point-in-time universe construction, market-cap definition, weighting convention, and all portfolio-sort implementation details not visible in the reviewed public material remain **underspecified**.

## Economic mechanism

### Source-reported

Xu and Wu report a robust size-dependent relation between prior returns and subsequent cryptocurrency returns. Small cryptocurrencies show short-term reversal, whereas large cryptocurrencies show momentum, with the relation changing monotonically across the size distribution.

The paper further reports that small-coin reversal is driven mainly by rebounds among recent losers. For large coins, the authors describe the momentum side as reflecting persistent return dynamics rather than the same rebound mechanism. Liquidity frictions and idiosyncratic volatility explain part, but not all, of the observed size dependence.

### Research interpretation

The falsifiable hypothesis is that **market capitalization is a state variable for the sign of short-horizon return continuation**. The same recent-return signal should not be applied uniformly across the crypto cross-section:

- among sufficiently small coins, recent losers should be expected to mean-revert more strongly than recent winners;
- among sufficiently large coins, recent winners should be expected to continue outperforming recent losers over the short horizon.

A plausible mechanism is that smaller coins are more exposed to temporary price pressure, thin liquidity, retail-driven overshooting, and larger idiosyncratic shocks, creating rebound opportunities after recent losses. Larger coins may incorporate information more gradually and sustain directional demand for longer, producing continuation rather than reversal.

Because the primary source states that liquidity and idiosyncratic volatility explain only part of the size split, size should initially be treated as an empirical conditioning variable rather than assumed to be merely a proxy for liquidity.

## Signal

Source-faithful normalized signal family, with explicit gaps preserved:

1. At each weekly formation date, construct a point-in-time eligible cryptocurrency universe.
2. Rank the universe by market capitalization and partition it into size groups. The secondary summary specifically discusses the smallest and largest **quintiles**.
3. Within each size group, compute a recent-return ranking over the source’s short-term formation horizon.
4. For the **smallest size quintile**, use a contrarian direction: recent losers are the long side and recent winners are the short/comparison side.
5. For the **largest size quintile**, use a momentum direction: recent winners are the long side and recent losers are the short/comparison side.
6. Hold the resulting portfolios for approximately one week for the focal short-horizon test, then re-form.

The reviewed public text does **not** expose enough methodological detail to assert the exact recent-return formation window, breakpoint convention for the return sort, weighting scheme, minimum-history rule, treatment of stablecoins/wrapped assets, exact rebalance timestamp, or whether intermediate size quintiles are directly traded or used only to demonstrate monotonicity. These are **underspecified** and must not be invented.

Therefore this record is a strategy hypothesis capture, not a production-ready implementation specification.

## Required data

- Point-in-time cryptocurrency universe with survivorship-safe listing and delisting history.
- Point-in-time market capitalization or sufficient price and circulating-supply data to reconstruct it without look-ahead.
- Daily or higher-frequency prices sufficient to compute the paper’s short-term formation return and one-week forward holding return.
- Trading volume, turnover, spreads, and/or Amihud-style liquidity proxies for mechanism tests.
- Idiosyncratic volatility estimates using a clearly specified crypto factor benchmark.
- Asset metadata to identify stablecoins, wrapped representations, redenominations, migrations, forks, and stale-price observations.
- Exact timestamp/timezone convention for market-cap snapshots and return measurement.
- If adapted to perpetual futures, point-in-time contract availability, funding, mark/index data, contract specifications, and open-interest/liquidity history.

## Execution assumptions

Execution details are **underspecified** in the reviewed public material.

A leakage-safe reproduction should form ranks only after all formation-period prices and market-cap inputs are observable, then trade at the next executable timestamp rather than implicitly filling at the same close used to construct the signal.

Material assumptions requiring explicit testing include:

- market versus limit orders;
- maker/taker fees;
- bid-ask spread;
- slippage and market impact;
- rebalance turnover;
- short availability / borrow constraints for spot implementations;
- funding and liquidation risk for perpetual-futures implementations;
- stale prices and thin-market execution in the smallest size quintile;
- delisting and migration events;
- partial fills and capacity limits.

Execution costs are especially important because the reported reversal side is concentrated in smaller cryptocurrencies, where gross statistical predictability can be difficult to monetize.

## Evidence

### Source-reported

The primary SSRN abstract reports a monotonic size-dependent pattern: small cryptocurrencies exhibit strong short-term reversal, whereas large cryptocurrencies exhibit momentum. It states that small-coin reversal is driven mainly by rebounds among recent losers and that liquidity frictions plus idiosyncratic volatility explain part, but not all, of the pattern.

A secondary QuantSeeker summary of the Xu–Wu paper reports a 2018–2025 sample and states that, in the smallest cryptocurrency quintile, recent losers outperformed recent winners by approximately **4.9% over the next week**, while the largest size quintile showed approximately **+1.0% weekly winner-minus-loser momentum**. The same secondary summary reports that large-cap momentum increases over longer holding horizons, approaching approximately 4.0% over four weeks.

These numerical figures are **secondary-source-reported**, not independently verified against the primary paper tables in this Scout cycle, and should not be treated as our own evidence.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The result is a 2026 working-paper finding rather than a settled empirical law and has not been independently reproduced here.

Existing pool records already document that short-horizon crypto momentum and reversal are highly sensitive to liquidity, size, and formation horizon. In particular, `crypto-cross-sectional-last-day-return-reversal-liquidity-conditioned-2026-08-31.md` preserves evidence that most illiquid coins reverse at the daily horizon while the largest and most tradeable coins can exhibit daily momentum. `crypto-cross-sectional-momentum-30d-top-quintile-7d-2026-08-31.md` preserves evidence that a liquid, screened universe can exhibit 30-day cross-sectional momentum over a seven-day holding period.

These related findings are directionally compatible with size conditioning but also imply substantial specification risk: changing the formation horizon, liquidity threshold, or universe can flip the observed sign.

No independent modern robustness test was performed in this Scout cycle.

## Falsification plan

The hypothesis should be materially weakened or rejected if a point-in-time modern replication finds any of the following:

1. The sign of recent-return predictability does not differ between the smallest and largest market-cap groups.
2. The size interaction is not monotonic or disappears after reasonable liquidity and idiosyncratic-volatility controls.
3. Small-coin loser rebounds are concentrated in stale prices, delisting artifacts, micro-price jumps, or assets that are practically untradeable.
4. Large-coin momentum does not survive realistic fees, spread, slippage, and turnover.
5. The result is unstable to nearby formation/holding windows or to alternative but reasonable market-cap breakpoints.
6. A point-in-time universe removes the effect that appears in a survivorship-biased reconstruction.
7. The smallest-coin reversal leg cannot be monetized under realistic capacity, shorting, or execution assumptions.
8. The sign split disappears in a genuinely untouched post-2025 sample or across independent data vendors/venues.

Required controls should include equal-weight and value-weight portfolios, liquidity-matched size groups, market-beta controls, idiosyncratic-volatility controls, long-leg versus short-leg decomposition, and placebo size assignments.

## Crypto portability

**Direct**, because the source itself studies cryptocurrency returns.

Portability is nevertheless conditional on market segment:

- Spot crypto is the closest conceptual match unless the full source explicitly states otherwise.
- A perpetual-futures adaptation is **adapted / unproven** because contract listings truncate the small-cap universe and introduce funding, leverage, liquidation, mark/index mechanics, and different shorting constraints.
- A Binance-only or major-exchange universe may eliminate many of the very small coins that generate the reversal side of the source result.
- Market-cap measurement in crypto is sensitive to circulating-supply revisions, token migrations, wrapped assets, and data-vendor methodology.
- The 24/7 market structure requires a fixed UTC or venue-native rebalance boundary.

## Limitations

- **Not independently reproduced.**
- **Working-paper risk:** SSRN paper posted 22 April 2026; no peer-reviewed publication was identified in this Scout cycle.
- **underspecified:** exact formation horizon, return-sort breakpoints, portfolio weighting, rebalance timestamp, eligibility screen, and intermediate-quintile treatment were not fully recoverable from the reviewed public text.
- **secondary-source dependence:** the 4.9%, 1.0%, approximately 4.0%, and 2018–2025 quantitative details come from a public secondary summary rather than a table checked directly in the primary PDF.
- **data gap:** exact source sample end date and point-in-time universe rules were not recovered.
- **execution gap:** gross predictability in small coins may not survive realistic spread, impact, capacity, and shorting constraints.
- **specification risk:** the direction of crypto momentum/reversal is known to vary with lookback, holding horizon, size, and liquidity.
- **unproven** for perpetual-futures adaptation.

## Implementation status

No implementation in PyBroker, NautilusTrader, the strategy registry, Paper, Testnet, Demo, or Live trading has been created or modified.

`implementation_status: not-implemented`

## Adoption boundary

This record is research material in the Alpha Strategy Pool only. It is not evidence of validated alpha, not an implementation task, and not approval for Paper, Testnet, Demo, or Live trading.

`status: research-only`

`adoption: not-approved`

`approval_scope: research-only`

## Related Wiki records

No Hermes Wiki Brain record was queried, created, or modified in this Scout cycle.

Related Alpha Strategy Pool artifacts:

- `crypto-cross-sectional-last-day-return-reversal-liquidity-conditioned-2026-08-31.md` — daily reversal with opposite-sign behavior among the largest/most liquid coins.
- `crypto-cross-sectional-momentum-30d-top-quintile-7d-2026-08-31.md` — 30-day momentum in a screened tradable universe, with size/liquidity-dependent negative evidence.

## Sources

1. Zezhou Xu and Fenglin Wu, “Size-Momentum Puzzle in Cryptocurrencies,” SSRN working paper, posted 22 April 2026. Abstract page: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6628860
2. DOI / SSRN persistent identifier: https://doi.org/10.2139/ssrn.6628860
3. QuantSeeker, “Weekly Research Recap,” public summary discussing the Xu–Wu paper and its reported 2018–2025 size-quintile results: https://www.quantseeker.com/p/weekly-research-recap-a23
