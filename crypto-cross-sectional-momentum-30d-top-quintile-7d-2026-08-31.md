---
schema: strategy-research-record-v1
title: "Crypto Cross-Sectional Momentum: 30-Day Top-Quintile / 7-Day Rotation"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cryptocurrency
  - cross-sectional-momentum
  - momentum
status: research-only
confidence: high
source_as_of: 2022-11-06
sources:
  - "https://www.starkiller.capital/post/cross-sectional-momentum-in-cryptocurrency-markets"
  - "https://doi.org/10.2139/ssrn.4322637"
  - "https://wp.ffu.vse.cz/artkey/wps-202301-0003_impact-of-size-and-volume-on-cryptocurrency-momentum-and-reversal.php"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Fičura (2023) reports weekly reversal for small/illiquid cryptocurrencies while large/liquid cryptocurrencies exhibit weekly momentum, indicating strong universe/liquidity dependence."
---

# Crypto Cross-Sectional Momentum: 30-Day Top-Quintile / 7-Day Rotation

## Provenance

Primary source: Leigh Drogen, Corey Hoffstein, and Kevin Otte, *Cross-sectional Momentum in Cryptocurrency Markets*, first published 2023-01-11 and updated 2023-01-20 by Starkiller Capital; SSRN DOI `10.2139/ssrn.4322637`. The source studies spot cryptocurrency data from 2018-04-05 through 2022-11-06, with an in-sample period ending 2021-03-01 and the remainder treated as out-of-sample.

The primary source uses aggregated spot-market data supplied by Nomics and constructed from 57 selected CeFi and DeFi exchanges. It explicitly excludes perpetual-futures prices and volume from the tested portfolio construction.

Negative/regime evidence: Milan Fičura, *Impact of size and volume on cryptocurrency momentum and reversal* (FFA Working Papers, 2023). This study reports materially different short-horizon behavior by liquidity/size bucket: small and illiquid cryptocurrencies exhibit weekly reversal while large and liquid cryptocurrencies exhibit weekly momentum.

This record is a normalized research capture only. It has not been independently reproduced in the user's research stack.

## Economic mechanism
### Source-reported

Drogen, Hoffstein, and Otte hypothesize that short-horizon cross-sectional momentum in cryptocurrencies can arise from fragmented market access, limits to arbitrage and shorting, uneven information access, rational inattention, narrative-driven capital rotation, and the rapid migration of speculative capital toward currently favored protocols or themes. The paper describes this as a compressed "hot ball of money" effect in which recent winners may continue attracting attention and capital over roughly monthly horizons.

The authors explicitly acknowledge hindsight bias and do not establish these proposed channels causally.

### Research interpretation

The falsifiable hypothesis is that, within a sufficiently liquid and tradable cryptocurrency universe, relative winners over the prior 30 calendar days contain short-lived continuation information that persists for approximately the next week. The predictive object is cross-sectional rank, not the absolute direction of the crypto market.

The mechanism should be treated as conditional rather than universal. If momentum is primarily a property of large/liquid assets while small/illiquid assets mean-revert, then universe construction is part of the alpha thesis rather than merely an execution filter. A failure to reproduce the effect after point-in-time liquidity and listing filters would materially weaken the hypothesis.

## Signal

Base signal normalized from the primary source:

1. **Rebalance timestamp:** Thursday at `00:00 UTC`.
2. **Formation window:** compute each eligible asset's total return over the previous 30 calendar days using the source's aggregated spot pricing convention.
3. **Universe eligibility at each rebalance:**
   - the asset must be listed on at least three exchanges;
   - at least one listing must be on a CeFi exchange;
   - the asset must have average dollar volume of at least USD 5 million on at least half of the previous 30 days;
   - manually excluded categories in the source include rebase tokens and tokens with large transaction penalties.
4. **Cross-sectional sort:** rank all eligible assets by trailing 30-day return and split the universe into quintiles.
5. **Long entry:** hold an equally weighted portfolio of the top return quintile.
6. **Short entry:** none in the tested base strategy. The paper studies bottom-quintile returns for comparison but does not implement a tradable long/short portfolio because broad short availability, borrow, perpetual-futures availability, and funding costs are not modeled.
7. **Holding / rebalance period:** hold for 7 days, then recompute eligibility and 30-day returns and rebalance at the next weekly timestamp.
8. **Exit:** assets leave the portfolio at the next rebalance if they are no longer in the top quintile or no longer eligible. The source initially assumes instantaneous rebalance.
9. **Position sizing:** equal weight across top-quintile constituents in the reported base portfolio.
10. **Benchmark:** Bitcoin is the authors' primary practical benchmark; a weekly rebalanced equal-weight portfolio of all eligible assets is also reported as a theoretical comparison.

Parameter-selection caveat: the authors test lookbacks and holding periods from 5 to 150 days and observe a stable region around 15-35 day lookbacks with a 7-day rebalance. They select 30 days partly because it aligns with a common monthly reporting cycle. Therefore, `30d/7d` is source-selected after parameter exploration and should not be treated as an untouched ex-ante parameter choice.

Signal specification is sufficiently detailed for a research reproduction of the base rule, but the manual token-exclusion process is **underspecified** and must not be silently reconstructed.

## Required data

- **Instrument / market type:** spot cryptocurrencies for the primary reproduction.
- **Universe:** point-in-time eligible cryptocurrencies; survivorship-free inclusion is required.
- **Venue data:** price and volume across approved CeFi/DeFi venues, or a defensible point-in-time substitute that reproduces the source's multi-venue eligibility logic.
- **Timeframe:** daily data are sufficient for the 30-day formation and weekly rebalance signal if daily bars preserve the Thursday `00:00 UTC` boundary.
- **Fields:** close or equivalent daily reference price, dollar trading volume, exchange listing history, venue classification (CeFi/DeFi), and token metadata needed for exclusions.
- **Point-in-time requirements:** listing status, liquidity eligibility, and all universe filters must be evaluated using only information available at each rebalance.
- **Timestamp:** UTC alignment is required.
- **Missing data:** do not impute missing prices or volumes unless a separate reproducible rule is specified. Assets without sufficient formation history should be ineligible.
- **Fees / spread / impact:** needed for realistic validation. The source initially reports gross results and separately evaluates trading-cost sensitivity.
- **Perpetual adaptation:** if migrated to perpetual futures, additional data are required for contract availability, funding, mark/index prices, contract specifications, and point-in-time liquidity. This is not part of the source-tested base strategy.

## Execution assumptions

The primary backtest initially assumes instantaneous, frictionless weekly rebalancing at the signal timestamp. This is optimistic and not a production fill model.

The source later performs transaction-cost sensitivity and reports that approximately 125 bps of assumed trading cost is enough for the top-quintile portfolio to underperform its benchmark. It also reports that at an assumed 50 bps average explicit-plus-impact cost, annualized returns are reduced materially, emphasizing that turnover and long-tail liquidity are central to implementability.

The source discusses, but does not fully test, patient execution throughout the rebalance day, liquidity-weighted holdings, additional liquidity screening, and OTC execution. Market impact, partial fills, venue fragmentation, and operational failures remain **underspecified**.

No leverage is required for the long-only base strategy. No broad shorting or borrow assumptions are needed because the tested strategy does not short the bottom quintile.

## Evidence
### Source-reported

For the full 2018-04-05 to 2022-11-06 sample, the source reports the 30-day lookback / 7-day rebalance top-quintile portfolio at approximately 37.8% annualized return, versus -33.8% for the bottom quintile, 11.7% for the weekly equal-weight eligible-universe portfolio, and 28.7% for Bitcoin.

The source reports that the top/bottom quintile spread is present in both its in-sample and out-of-sample analyses, with robustness checks across random universe subsamples and rebalance weekdays. The out-of-sample period is materially weaker in absolute terms: the top-quintile portfolio is reported at approximately -2.35% annualized while the equal-weight portfolio and Bitcoin are reported at larger losses.

The authors also report very large drawdowns for the unfiltered top-quintile portfolio, exceeding 75% on multiple occasions. A separate 5-day / 50-day Bitcoin EMA trend overlay is shown as a possible beta-management extension, but that overlay is not part of this record's canonical alpha signal.

### Independently reproduced

Not independently reproduced.

### Negative evidence

Fičura (2023) reports that weekly return behavior is strongly conditioned by size and liquidity: weekly reversal is concentrated in small/illiquid cryptocurrencies, whereas large/liquid coins exhibit weekly momentum. This is consistent with treating liquidity/universe selection as a structural part of the signal and provides a direct falsification risk for naive all-coin implementations.

The primary source itself reports substantial transaction-cost sensitivity, very high drawdowns, a short sample relative to traditional asset classes, and an explicitly non-causal mechanism narrative. Its parameter choice follows a broad grid search, creating parameter-selection risk.

Prior literature summarized by the primary source is mixed, including studies reporting no momentum or reversal in earlier samples. Therefore the effect should be treated as time-varying and regime-dependent rather than a stable law.

## Falsification plan

A serious reproduction should fail or materially downgrade the hypothesis if any of the following hold:

1. A point-in-time, survivorship-safe reconstruction of the source universe does not produce monotonic future returns across 30-day return quintiles.
2. The top-minus-bottom spread or long-only top-quintile excess return disappears in a genuinely untouched out-of-sample period.
3. The effect is confined to assets that would have failed realistic liquidity, listing, or capacity constraints.
4. Net performance loses economic significance under realistic maker/taker fees, spread, slippage, impact, and turnover.
5. The result disappears when formation/rebalance parameters are perturbed within the source's reported stable neighborhood (for example 15-35 day lookbacks and 7-14 day holding/rebalance periods).
6. The signal is explained primarily by market beta rather than cross-sectional ranking, assessed against equal-weight and beta-aware baselines.
7. A liquidity/size interaction test shows that recent winners only continue in an economically negligible subset of the intended tradable universe.

Required controls should include equal weight, Bitcoin, randomized ranks, lagged or permuted formation returns, and liquidity-matched portfolios. A perpetual-futures adaptation should be evaluated separately rather than treated as a direct replication.

## Crypto portability

**Direct** for diversified spot-crypto universes with point-in-time exchange and liquidity data.

**Adapted / unproven** for Binance or other perpetual-futures universes. Perpetual markets may improve short availability and capacity for some assets, but funding, contract listing timing, leverage, mark/index pricing, and venue-specific liquidity change both the economics and implementation. A liquid-major perpetual universe may also remove the long-tail assets that contributed to the original cross-sectional spread.

The 24/7 market structure is directly compatible with the weekly UTC rebalance convention, but the exact candle boundary must remain consistent.

## Limitations

- **Not independently reproduced.**
- **Underspecified:** manual exclusions for rebase tokens, transaction-penalty tokens, and related metadata cleaning are not fully rule-based in the source.
- **Data gap:** a faithful reproduction requires point-in-time multi-venue spot listings and volume history; a single-exchange current-symbol list is not equivalent.
- **Unproven portability:** perpetual-futures implementation is not the source-tested strategy.
- The source's proposed behavioral and market-structure mechanisms are hypotheses, not causal findings.
- The sample is relatively short and spans major structural changes in the cryptocurrency market.
- The 30-day / 7-day rule follows parameter exploration and therefore requires fresh OOS validation.
- Long-only momentum retains substantial crypto beta and severe drawdown risk.
- Cost and capacity conclusions depend strongly on turnover, venue, asset liquidity, and execution style.

## Implementation status

No implementation or validation in PyBroker, NautilusTrader, paper trading, testnet, or live trading has been completed for this research record.

`implementation_status: not-implemented`

## Adoption boundary

This record is research material only. It is not evidence that the strategy remains profitable, not authorization to implement it, and not approval for paper, testnet, or live trading.

`status: research-only`

`adoption: not-approved`

`approval_scope: research-only`

## Related Wiki records

No stable Hermes Wiki Brain links are asserted in this staging record. Concept-level clustering and Wiki promotion belong to the separate downstream Reviewer workflow.

## Sources

1. Leigh Drogen, Corey Hoffstein, Kevin Otte, *Cross-sectional Momentum in Cryptocurrency Markets*, Starkiller Capital, published 2023-01-11, updated 2023-01-20: https://www.starkiller.capital/post/cross-sectional-momentum-in-cryptocurrency-markets
2. SSRN DOI for the same research: https://doi.org/10.2139/ssrn.4322637
3. Milan Fičura, *Impact of size and volume on cryptocurrency momentum and reversal*, FFA Working Papers 5:003 (2023): https://wp.ffu.vse.cz/artkey/wps-202301-0003_impact-of-size-and-volume-on-cryptocurrency-momentum-and-reversal.php
