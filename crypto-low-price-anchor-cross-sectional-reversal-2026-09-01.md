---
schema: strategy-research-record-v1
title: Crypto Lowest-Price-Anchor Cross-Sectional Reversal
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - reversal
  - behavioral-finance
status: research-only
confidence: medium
source_as_of: 2025-07-30
sources:
  - https://doi.org/10.1016/j.frl.2025.107800
  - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5001299
  - https://ideas.repec.org/a/eee/finlet/v85y2025ipas154461232501058x.html
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Lowest-Price-Anchor Cross-Sectional Reversal

## Provenance

Primary source: Kei Nakagawa and Ryuta Sakemoto, **“New behaviorally-based cross-sectional reversal portfolios in the cryptocurrency market and market uncertainty,”** *Finance Research Letters* 85 (2025), article 107800, DOI `10.1016/j.frl.2025.107800`.

A pre-publication version is available as SSRN 5001299. The SSRN record was posted 2024-11-21 and last revised 2025-07-30; its listed date written is 2025-07-02. The peer-reviewed journal record is treated as canonical provenance.

Source-identity check performed against the Alpha Strategy Pool before creation: no existing record matched DOI `10.1016/j.frl.2025.107800`, SSRN `5001299`, the exact paper title, or the distinctive mechanism of decomposing crypto reversal around the **lowest price observed during the formation period**.

This record is intentionally distinct from generic crypto cross-sectional reversal records. Its identity is not merely “buy losers / sell winners”; the source introduces a behavioral decomposition in which the formation-period minimum price is the anchor used to refine the reversal portfolio. That is a materially different signal construction and behavioral hypothesis.

Publicly accessible bibliographic/abstract material does not expose the full paper tables or complete portfolio-construction equations. Missing operational details below are therefore preserved as `underspecified` rather than inferred.

## Economic mechanism

### Source-reported

Nakagawa and Sakemoto propose a behavioral enhancement to conventional cross-sectional cryptocurrency reversal. The source states that the **lowest price during the formation period serves as the anchoring point** in a new decomposition of reversal portfolios.

The authors report that these behaviorally decomposed reversal portfolios outperform conventional cross-sectional reversal portfolios. They further report robustness across different portfolio-formation periods, interpret that pattern as consistent with heterogeneous investor horizons, and find that the portfolios hedge increases in stock- and gold-market uncertainty.

The source also reports that profitability remains robust after incorporating conservative transaction costs and when the COVID-19 pandemic period is included.

### Research interpretation

The falsifiable mechanism is an **anchoring-conditioned overreaction / reversal hypothesis**. A conventional loser signal mixes assets that reached their current loss through different paths. Conditioning the loss on the lowest price reached during the formation window may isolate coins for which investors are psychologically anchored to an extreme downside reference point, producing delayed correction or overreaction that is not captured by cumulative return alone.

The key research question is therefore incremental: **does lowest-price-anchor information add cross-sectional predictive power beyond ordinary past-return reversal?** If not, the behavioral decomposition is redundant even if conventional reversal itself remains profitable.

This interpretation does not establish that psychological anchoring is causal; the minimum-price variable may proxy for drawdown shape, tail risk, liquidity stress, lottery demand, momentum crash exposure, or other omitted characteristics.

## Signal

### Source-specified elements

- Universe: cryptocurrencies in a cross-sectional portfolio setting.
- Core family: reversal.
- Distinctive conditioning/decomposition variable: the **lowest price during the formation period** is used as the behavioral anchor.
- The source evaluates multiple formation periods rather than a single fixed horizon.
- Comparison baseline: conventional cross-sectional reversal portfolios.

### Underspecified source details

The publicly accessible abstract/bibliographic sources reviewed in this Scout cycle do **not** fully specify:

- exact cryptocurrency universe and survivorship rules;
- exact data vendor and venue mapping;
- precise formation-window lengths used in every specification;
- exact mathematical decomposition around the minimum-price anchor;
- breakpoint scheme (median, tercile, quintile, decile, etc.);
- portfolio weighting method;
- long-only versus long-short implementation details for each reported portfolio;
- holding period and rebalance frequency;
- overlap handling across formation/holding windows;
- exact transaction-cost assumptions;
- entry/exit timestamps.

These are `underspecified` / `data gap`. They must be recovered from the full source before any faithful implementation claim.

### Research-proposed operationalization for testability

The following is **research-proposed**, not source-reported, and exists only to make the hypothesis testable if the full source remains unavailable during a later research stage:

1. At each rebalance date, compute cumulative return over a backward-looking formation window for every eligible coin.
2. Record the minimum price reached inside that same formation window and derive a lowest-price-anchor feature such as distance from the current/formation-end price to that minimum.
3. Form a conventional reversal score from prior cumulative return.
4. Test whether conditioning or interacting the reversal score with the lowest-price-anchor feature improves forward cross-sectional return prediction relative to the reversal score alone.
5. Evaluate multiple formation and holding horizons rather than selecting one ex post.

No fixed threshold, quantile count, holding period, stop, leverage rule, or sizing convention is asserted here because the accessible source does not establish one.

## Required data

A faithful reconstruction requires, at minimum:

- point-in-time cryptocurrency universe membership;
- timestamped historical prices sufficient to identify each formation window's exact minimum price;
- total-return or adjusted price treatment appropriate for crypto instruments;
- market capitalization and liquidity fields for universe controls if used by the source;
- delisting/death histories to avoid survivorship bias;
- trading-volume and spread/cost data for execution realism;
- consistent 24/7 timestamp convention and rebalance boundaries.

For a modern exchange-level replication, venue-level spot or perpetual OHLCV should be used with explicit listing/delisting timestamps. Aggregated vendor prices should not be mixed with executable venue prices without documenting the mapping.

## Execution assumptions

The accessible source material states that results are robust to conservative transaction costs but does not expose the exact cost schedule in the reviewed public abstract/bibliographic material.

Therefore the following remain `underspecified`:

- market versus limit execution;
- fee tier;
- bid-ask spread;
- slippage and market impact;
- short borrow or perpetual funding for the short leg;
- partial fills and unavailable short inventory;
- signal-to-order timing;
- capacity constraints in smaller coins.

A later implementation study must use next-observable-bar execution or another causally valid convention. Same-close execution is not permitted unless the signal is demonstrably known before that close.

## Evidence

### Source-reported

The peer-reviewed *Finance Research Letters* article reports that:

- the lowest-price-anchor behavioral decomposition produces reversal portfolios with higher returns than conventional cross-sectional reversal portfolios;
- the result holds across different portfolio formation periods;
- the reversal portfolios provide hedging value against increases in stock- and gold-market uncertainty;
- profitability remains robust when conservative transaction costs are incorporated;
- profitability also remains robust when the COVID-19 pandemic period is included.

No exact return, Sharpe ratio, t-statistic, turnover figure, breakpoint, or cost number is recorded here because those precise values were not traceable from the public sources reviewed in this cycle.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No direct contradictory result for this exact lowest-price-anchor decomposition was identified in the reviewed sources. Absence of identified contradiction is not evidence that no negative result exists.

Important reasons to remain cautious:

- the accessible source summary does not expose full construction equations or exact economic magnitudes;
- conventional crypto reversal is known to be regime-, liquidity-, size-, and horizon-sensitive, so incremental anchor value could be sample-specific;
- minimum price may be a proxy for downside volatility, maximum drawdown, liquidity stress, or lottery-like characteristics rather than behavioral anchoring;
- cross-sectional short legs can be materially more expensive or infeasible than frictionless academic portfolios imply.

## Falsification plan

A later independent study should test the **incremental anchor hypothesis**, not merely re-establish generic reversal.

1. Reconstruct a survivorship-safe point-in-time crypto universe covering bull, bear, crash, and sideways regimes.
2. Replicate conventional cross-sectional reversal as the baseline.
3. Add the source's exact lowest-price-anchor decomposition once recovered from the full paper.
4. Run horse-race regressions / portfolio sorts controlling for prior return, maximum drawdown, realized volatility, downside volatility, size, liquidity, turnover, lottery proxies, and listing age.
5. Use non-overlapping and overlapping portfolio constructions where appropriate and correct inference for serial correlation.
6. Stress realistic fees, spread, slippage, funding/borrow, and impact.
7. Require genuine out-of-sample or walk-forward evaluation using a frozen specification.
8. Test multiple venue universes to determine whether the result is a vendor/venue artifact.

**Research-defined falsification threshold:** treat the distinctive anchor component as unsupported if, after controlling for ordinary reversal and the major confounds above, its incremental out-of-sample long-short spread is not positive net of realistic costs and its cross-sectional coefficient is not directionally stable across major regimes. This threshold is Scout-defined for falsifiability; it is not source-reported.

If the anchor feature fails while conventional reversal survives, reject the behavioral-anchor enhancement but retain generic reversal as a separate hypothesis family.

## Crypto portability

**Direct.** The primary source studies cryptocurrency portfolios rather than porting a traditional-asset result into crypto.

Portability across modern crypto venues is nevertheless `unproven` because the original source's exact universe and trading implementation are not visible in the reviewed public summary. Venue fragmentation, 24/7 session structure, listings/delistings, stablecoin quote differences, perpetual funding, short availability, and extreme altcoin liquidity dispersion can materially change realized results.

## Limitations

- `underspecified`: exact source equations and portfolio breakpoints are not available in the public abstract material reviewed here.
- `data gap`: exact sample dates, universe screens, holding horizons, turnover, and transaction-cost schedule were not recoverable from the accessible summary.
- `not independently reproduced`: no internal backtest or replication was performed.
- `unproven`: causal attribution to psychological anchoring is not established by this Scout record.
- The source is copyrighted; this record normalizes the hypothesis and cites provenance rather than redistributing source text.

## Implementation status

No PyBroker, NautilusTrader, notebook, strategy registry, data-pipeline, Paper, Testnet, or Live implementation has been created or modified in this Scout cycle.

`implementation_status: not-implemented`

## Adoption boundary

This record is research material only.

Presence in the Alpha Strategy Pool does **not** mean the strategy is profitable, validated, implementation-approved, paper-approved, testnet-approved, or live-approved.

`status: research-only`  
`adoption: not-approved`  
`approval_scope: research-only`

## Related Wiki records

No stable Hermes Wiki Brain link is asserted in this Scout cycle. Related Alpha Strategy Pool records in the broad reversal family should be treated as comparators, not as duplicates, because this record's distinctive hypothesis is the formation-period **lowest-price anchor** and its incremental value over ordinary prior-return reversal.

## Sources

1. Nakagawa, K., & Sakemoto, R. (2025). “New behaviorally-based cross-sectional reversal portfolios in the cryptocurrency market and market uncertainty.” *Finance Research Letters*, 85, 107800. DOI: https://doi.org/10.1016/j.frl.2025.107800
2. SSRN pre-publication record, Abstract ID 5001299, last revised 2025-07-30: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5001299
3. IDEAS/RePEc bibliographic record, including journal publication metadata and abstract: https://ideas.repec.org/a/eee/finlet/v85y2025ipas154461232501058x.html
