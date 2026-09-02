---
schema: strategy-research-record-v1
title: Ethereum Exchange Net-Inflow-Conditioned Call Selling
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - ethereum
  - options
  - on-chain
status: research-only
confidence: medium
source_as_of: 2025-06
sources:
  - https://arxiv.org/abs/2411.06327
  - https://arxiv.org/pdf/2411.06327
  - https://doi.org/10.48550/arXiv.2411.06327
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Ethereum Exchange Net-Inflow-Conditioned Call Selling

## Provenance

Primary source: Yeguang Chi, Qionghua (Ruihua) Chu, and Wenyan Hao, *Return and Volatility Forecasting Using On-Chain Flows in Cryptocurrency Markets*, arXiv:2411.06327. The currently reviewed public PDF is dated June 2025. The broad on-chain sample runs from 2017-12-16 to 2023-01-20; the option-strategy tables use Deribit ETH option trade data from 2021-01-01 to 2022-05-19.

Source-identity check: the same arXiv source is already represented in this repository and in Hermes Wiki Brain by `ethereum-exchange-net-inflow-bearish-drift-1h-6h-2026-09-01.md`, which captures the paper's ETH net-inflow return-forecasting hypothesis. This record is materially distinct rather than a reframing: it captures the paper's separate derivative implementation in which extreme ETH exchange net inflows condition ETH call-option selling, introducing Deribit option-chain, delta-hedge, implied-volatility, moneyness, and option-cost dependencies that are absent from the existing spot/return-predictability record.

## Economic mechanism

### Source-reported

The authors define ETH net inflow as ETH transferred into exchanges minus ETH transferred out. They interpret positive ETH net inflows as sell-side pressure: ETH moved to exchanges is more likely to be available for sale, and their regressions find negative subsequent ETH returns across the tested 1-, 2-, 3-, 4-, and 6-hour horizons. They then test whether this bearish state can be monetized through ETH call-option selling. In the option sample, they report that sell-call trades are profitable in most scenarios drawn from the top 10%, 5%, and 1% of ETH net inflows, while analogous bottom-percentile conditions are generally less favorable for call selling.

### Research interpretation

The falsifiable mechanism is a conditional short-convexity / short-upside-volatility trade: when unusually large ETH transfers into exchanges signal near-term sell pressure, the conditional probability and/or magnitude of an upside ETH move may fall enough that short ETH calls earn positive net PnL after the source's hedge and cost terms. This is not simply the same alpha as the existing ETH bearish-drift record because the traded payoff is nonlinear and depends on option implied volatility, strike/moneyness, maturity, delta hedging, and execution frictions.

A competing explanation is that high ETH inflow episodes coincide with high implied volatility and elevated option premia; if so, the option result could be compensation for selling volatility/tail risk rather than incremental information from exchange flows. That competing explanation must be tested explicitly.

## Signal

### Source-reported construction

- **Conditioning variable:** ETH exchange net inflow, defined as exchange inflows minus exchange outflows.
- **Condition buckets:** the authors evaluate top and bottom ETH net-inflow percentiles, explicitly including top/bottom 10%, 5%, and 1% buckets.
- **Trade direction:** sell ETH call options in high-ETH-net-inflow states.
- **Option matching:** comparisons use ETH call options matched on strike price, time to maturity, and quote time.
- **Option filters tested:** multiple implied-volatility buckets (`IV < 1`, `< 2`, `< 3`, whole sample, and `IV >= 1`, `>= 2`, `>= 3`) and multiple out-of-the-money ranges, including `<1%`, `1%-3%`, `3%-5%`, `5%-10%`, `10%-15%`, and `15%-20%`, plus combinations.
- **Portfolio:** short call plus a delta-linked underlying/perpetual hedge term as defined by the source.
- **Initial-capital convention in the source's case-study methodology:** USD 10,000.

### Underspecified source details

The source does not provide a single uniquely reproducible live-trading rule for:

- the exact publication/availability lag of the ETH net-inflow observation;
- the exact quote-selection timestamp relative to the finalized flow bucket;
- a unique option expiry / time-to-maturity rule for deployment;
- a unique IV and OTM filter to use as the canonical strategy rather than as reported scenario analysis;
- a precise live exit/holding rule applicable outside the paper's matched-quote evaluation;
- a live re-entry rule or overlapping-position rule.

Therefore the source-reported strategy is **underspecified** as a directly executable production rule. No missing parameter is silently invented here.

### Research-proposed testable operationalization

The following is **research-proposed**, not source-reported:

1. Form hourly ETH exchange net inflow only after the data vendor's finalized timestamp is known and apply the observed availability lag.
2. Rank the current observation against a trailing point-in-time history and flag the top decile as the primary high-inflow state; separately test top 5% and top 1% as predeclared sensitivity branches because those thresholds are explicitly analyzed by the source.
3. At the first tradable Deribit snapshot after the flow observation is available, construct a short-call candidate set across the source-tested OTM/IV regions without selecting the best ex post.
4. Evaluate short-call PnL with delta hedge, fees, spread, and slippage; test fixed predeclared horizons that map to the source's 1-6 hour return-predictability windows rather than optimizing an unconstrained holding period.
5. Run an ablation that replaces the flow gate with a matched implied-volatility-only gate to determine whether ETH inflow adds incremental predictive content beyond option richness.

Any chosen live quote time, maturity, holding horizon, or canonical IV/OTM filter remains **research-proposed** until independently validated.

## Required data

- **Underlying / signal asset:** ETH.
- **On-chain flow field:** exchange inflow and exchange outflow for ETH, with venue/entity attribution sufficient to reproduce net inflow.
- **Signal timeframe:** intraday, with the paper's predictive analysis covering 1, 2, 3, 4, and 6 hours.
- **Option venue:** Deribit for the source's option sample.
- **Option fields:** trade/quote timestamp, call price or bid/ask/mid, strike, expiry/time to maturity, implied volatility, delta, underlying/index price, and enough metadata to compute OTM distance.
- **Hedge fields:** ETH underlying/perpetual price and transaction-cost inputs for the delta-linked hedge.
- **Point-in-time requirement:** the on-chain net-inflow observation must be used only after its actual publication/finalization time. Using a retrospectively assembled hourly flow series as if known instantaneously would create look-ahead leakage.
- **Missing-data rule:** data gap; the source does not specify an imputation policy. Research should reject or skip intervals whose flow or option state is not point-in-time complete rather than impute silently.
- **Source sample dates:** on-chain sample 2017-12-16 to 2023-01-20; option-strategy sample 2021-01-01 to 2022-05-19.

## Execution assumptions

### Source-reported

The source computes call-option PnL using matched call prices at a current and later quote time, combines the option with a delta-linked underlying hedge, and reports a net portfolio return after explicit cost terms. The paper's formula includes a `0.0003` option-related cost term, a `0.0005 x delta` perpetual-hedge term, a `0.001 / 2` bid-ask-spread term scaled by the ETH index price, and a slippage term. The base scenario sets slippage to zero; a separate breakeven exercise solves for slippage that drives net PnL to zero.

The paper assumes USD 10,000 initial capital in its case-study strategy methodology.

### Research interpretation

The source's cost model is informative but should not be treated as current Deribit execution truth. A modern replication must use the contemporaneous option and perpetual fee tiers, actual bid/ask spreads, funding on the hedge, realistic latency, partial-fill assumptions, and market impact. The exact order type and hedge rebalance protocol are **underspecified**.

## Evidence

### Source-reported

The June 2025 arXiv version reports that ETH net inflows negatively forecast ETH returns across all tested 1-, 2-, 3-, 4-, and 6-hour intervals. In the option-strategy section, the authors state that sell ETH call options are profitable in most tested scenarios for the top 10%, 5%, and 1% ETH net-inflow buckets. Table 7 uses Deribit option trade data from 2021-01-01 to 2022-05-19 and compares top versus bottom net-inflow percentiles across multiple IV and OTM filters. The paper also reports that the bottom-percentile states, which correspond to ETH net outflows, do not provide a symmetric profitable call-buying relation.

The source's option evidence is scenario-based and includes multiple IV/OTM combinations. It should not be read as evidence that one precommitted live rule has already been validated out of sample.

### Independently reproduced

not independently reproduced

### Negative evidence

- The source itself reports asymmetry: ETH net outflows do not provide a consistent mirror-image return signal, so a symmetric long-call rule is not supported.
- The option section evaluates many IV and OTM subgroups, creating a multiple-testing / selection concern for any attempt to promote the best subgroup.
- The source's option sample ends 2022-05-19; persistence in the substantially larger and more institutional 2023-2026 ETH options market is unproven.
- Flow publication latency and exact live tradability are not fully specified; a leakage-safe replication could materially weaken the effect.
- The option PnL may partly reflect volatility-risk-premium compensation rather than incremental information from ETH exchange flows.

## Falsification plan

1. **Point-in-time leakage audit.** Reconstruct ETH exchange net inflows with actual data-availability timestamps. **Research-defined falsification threshold:** reject the hypothesis if the apparent advantage disappears when signals are delayed to first verifiable availability rather than period-end timestamps.
2. **Incremental-information ablation.** Compare the high-net-inflow short-call rule against an IV/moneyness-matched short-call baseline with no flow signal. **Research-defined falsification threshold:** reject the flow-conditioning mechanism if the flow-gated portfolio does not improve net risk-adjusted performance or tail loss relative to the matched volatility-only baseline out of sample.
3. **Predeclared percentile branches.** Test top 10%, 5%, and 1% inflow states without post-hoc selection. **Research-defined falsification threshold:** materially weaken the hypothesis if sign and economic value are confined to only one narrow threshold and fail adjacent predeclared thresholds.
4. **Out-of-sample regime test.** Use post-2022 Deribit data, including bull, bear, high-volatility, and low-volatility subperiods. **Research-defined falsification threshold:** reject if aggregate net PnL after realistic costs is non-positive and no predeclared regime exhibits stable positive expectancy.
5. **Cost/latency stress.** Apply current taker/maker fees, bid/ask spreads, perpetual funding, realistic hedge latency, and slippage/impact. **Research-defined falsification threshold:** reject tradability if modest cost or latency stress removes the sign of net expectancy.
6. **Tail-risk test.** Measure losses during abrupt upside squeezes and liquidation-driven rebounds. **Research-defined falsification threshold:** reject practical viability if the conditional short-call payoff is dominated by rare upside events such that risk-adjusted results are inferior to the matched baseline.
7. **Placebo timing.** Randomly shift the flow signal timestamps by non-overlapping placebo lags while preserving option-state distributions. **Research-defined falsification threshold:** materially weaken the information hypothesis if placebo timing performs similarly to true point-in-time flow timing.

## Crypto portability

**direct** for the source's ETH/Deribit setting: both the predictive signal and derivative strategy are studied directly in cryptocurrency markets.

Portability beyond the source sample remains conditional on:

- reliable exchange-wallet labeling and point-in-time flow delivery;
- Deribit option liquidity and strike/expiry availability;
- 24/7 timestamp alignment between on-chain flow aggregation, option quotes, and perpetual hedge prices;
- current fee tiers, funding, spread, and market impact;
- venue/entity reclassification over time;
- potential migration of ETH trading activity across centralized exchanges, decentralized venues, and ETF/regulated channels.

Extension to BTC, SOL, or other assets is **unproven** unless tested separately.

## Limitations

- **underspecified:** no single canonical live quote time, expiry, holding rule, re-entry rule, or IV/OTM branch is prescribed by the source.
- **data gap:** point-in-time publication/finalization latency of the on-chain flow feed is not fully specified.
- **not independently reproduced:** no independent replication has been run in this Scout cycle.
- **multiple-testing risk:** many option IV/OTM combinations are reported.
- **sample-age risk:** option evidence ends in May 2022.
- **execution-model risk:** source transaction-cost assumptions may not represent current Deribit conditions.
- **identification risk:** a volatility-risk-premium explanation may account for part or all of the option profits.
- **tail-risk:** short-call exposure can incur nonlinear losses during sudden upside moves even if average conditional returns are favorable.

## Implementation status

`not-implemented`.

No PyBroker, Nautilus, option execution engine, data pipeline, Paper, Testnet, or Live implementation was created or modified in this Scout cycle.

## Adoption boundary

This record is `research-only`, `not-implemented`, and `not-approved`. It is staging material for later Research Intake Review only. It does not authorize implementation, backtesting, paper trading, testnet trading, live trading, leverage, capital allocation, or option selling.

## Related Wiki records

- `quant/ethereum-exchange-net-inflow-bearish-drift-1h-6h-2026-09-01.md` — same primary source, but a materially different hypothesis: linear ETH return predictability from ETH exchange net inflows rather than conditional option selling.

No other materially equivalent ETH-net-inflow-conditioned call-selling record was found in the reviewed repository/Wiki search.

## Sources

1. Yeguang Chi, Qionghua (Ruihua) Chu, and Wenyan Hao, *Return and Volatility Forecasting Using On-Chain Flows in Cryptocurrency Markets*, arXiv:2411.06327, public PDF dated June 2025. https://arxiv.org/abs/2411.06327
2. Full public arXiv PDF, including Sections 2.4-2.5, Section 4 option-strategy discussion, and Tables 7-9. https://arxiv.org/pdf/2411.06327
3. arXiv DOI resolver: https://doi.org/10.48550/arXiv.2411.06327
