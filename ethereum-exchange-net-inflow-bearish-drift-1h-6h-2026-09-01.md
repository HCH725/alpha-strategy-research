---
schema: strategy-research-record-v1
title: Ethereum Exchange Net-Inflow Bearish Drift at 1-6 Hour Horizons
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - ethereum
  - onchain
  - exchange-flow
  - intraday
status: research-only
confidence: medium
source_as_of: 2023-01-20
sources:
  - https://arxiv.org/abs/2411.06327
  - https://doi.org/10.48550/arXiv.2411.06327
  - https://EconPapers.repec.org/RePEc:arx:papers:2411.06327
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - The source reports statistically significant ETH net-inflow return predictability, but does not specify a complete executable underlying-ETH trading rule or demonstrate net-of-cost profitability for such a rule.
---

# Ethereum Exchange Net-Inflow Bearish Drift at 1-6 Hour Horizons

## Provenance

Primary source: Yeguang Chi, Qionghua (Ruihua) Chu, and Wenyan Hao, *Return and Volatility Forecasting Using On-Chain Flows in Cryptocurrency Markets*, arXiv:2411.06327. Initial arXiv submission: 2024-11-10; the RePEc/EconPapers record reports a revised version in 2025-09.

Stable references:

- https://arxiv.org/abs/2411.06327
- https://doi.org/10.48550/arXiv.2411.06327
- https://EconPapers.repec.org/RePEc:arx:papers:2411.06327

The source studies intraday BTC, ETH, and USDT exchange-flow data. The reported return-forecasting sample runs from 2017-12-16 through 2023-01-20. The exact provider-specific exchange-address classification and historical revision policy must be reproduced from the primary data source before implementation; this record does not infer them.

Source/data as-of date for this record: 2023-01-20, the end of the reported core return-forecasting sample.

## Economic mechanism

### Source-reported

The paper reports that ETH net inflows into cryptocurrency exchanges negatively forecast future ETH returns across 1-, 2-, 3-, 4-, and 6-hour horizons. The authors interpret positive ETH net inflow as movement of ETH toward exchanges that is consistent with increased intent or ability to sell, creating bearish near-term price pressure.

The paper separately reports that USDT net inflows positively forecast BTC and ETH returns at shorter horizons, illustrating that the sign of an exchange-flow signal depends on the asset being transferred: base-asset inflow may represent sell-side inventory, whereas stablecoin inflow may represent deployable buying power.

### Research interpretation

This is an event-conditioned, within-instrument intraday bearish-drift hypothesis:

- Primary state variable: ETH exchange net inflow at time `t`.
- Expected direction: larger positive ETH net inflow predicts lower subsequent ETH return.
- Source-supported horizons: 1, 2, 3, 4, and 6 hours.
- Mechanism: temporary increase in readily sellable ETH inventory on exchanges and associated order-flow pressure.

The falsifiable hypothesis is that unusually positive ETH exchange net inflow contains incremental information about subsequent ETH returns beyond current return, volatility, market beta, and ordinary price momentum.

This is not equivalent to claiming that every deposit is a sale. Custody migration, exchange internal-wallet movements, bridge operations, staking flows, OTC settlement, and mislabeled addresses can all generate false flow signals.

## Signal

Source-normalized signal semantics:

1. At each intraday observation time `t`, calculate ETH exchange net inflow as exchange inflow minus exchange outflow using point-in-time labeled exchange addresses.
2. Use only flow information observable by `t`; do not use later address labels or retroactively corrected classifications without explicit vintage controls.
3. Forecast ETH return over the next 1, 2, 3, 4, or 6 hours.
4. The source reports a negative coefficient on ETH net inflow for ETH future returns across those intraday horizons.
5. Extreme positive ETH net-inflow observations are treated by the source as bearish events; the paper also evaluates top-percentile inflow states in its options exercise.

Operational trading trigger: **underspecified**.

The source does not provide one canonical production rule for shorting the underlying ETH. It does not specify a single required percentile, z-score, absolute ETH threshold, or rolling normalization window for an executable directional strategy. A future independent test may evaluate source-motivated event buckets such as top 10%, 5%, and 1% positive net-inflow states, but those must be labeled research thresholds rather than silently presented as the paper's canonical underlying-ETH entry rule.

Exit / holding rule: source-supported forecast horizons are 1-6 hours, but the single preferred holding period is **underspecified**.

Position sizing, re-entry, overlapping-event handling, and simultaneous horizon aggregation are **underspecified**.

## Required data

- ETH on-chain transfer data with timestamps.
- Point-in-time exchange-address labels for centralized exchanges.
- Exchange inflow and exchange outflow series, preferably at hourly or finer resolution.
- Derived net inflow: `inflow - outflow`.
- ETH spot or index price aligned to the same clock.
- 1h, 2h, 3h, 4h, and 6h forward returns.
- Current/lagged ETH returns for source-style controls.
- Venue and timezone normalization; UTC should be the default replication clock unless the source data contract specifies otherwise.
- Address-label vintage metadata to detect look-ahead from later exchange-wallet identification.
- Exchange maintenance, wallet migration, bridge, staking, and custody-event metadata where available.

For a tradable extension:

- ETH spot or perpetual bid/ask, fees, slippage, and depth.
- Perpetual funding, mark/index basis, and liquidation data if the hypothesis is implemented through derivatives.

## Execution assumptions

The paper establishes predictive regressions and an options application; it does not provide a fully specified executable ETH spot/perpetual short strategy.

Any independent implementation must model:

- data publication latency between on-chain transfer occurrence, confirmation, provider classification, and strategy availability;
- signal-to-order delay;
- spot borrow availability if shorting spot;
- perpetual funding and basis if using perps;
- bid-ask spread, fees, slippage, and impact;
- exchange outages and partial fills;
- overlapping signals across 1-6 hour horizons;
- large exchange internal transfers that may not represent market-facing inventory.

Same-timestamp execution using a net-flow value that was only finalized after the bar is prohibited because it would create look-ahead bias.

## Evidence

### Source-reported

The source reports statistically significant negative relationships between ETH net inflow at time `t` and ETH returns over the next 1, 2, 3, 4, and 6 hours in the 2017-12-16 to 2023-01-20 sample.

The paper's extreme-event case studies include periods in May 2022 where large ETH net inflows were followed by lower ETH prices over subsequent intraday horizons, consistent with the regression sign.

The source also tests ETH options. For top versus bottom 10% ETH net-inflow states in its reported options sample, selling ETH calls performs materially better in high-inflow states than low-inflow states; the paper additionally examines top/bottom 5% and 1% buckets with qualitatively similar direction. These results are source-reported and belong to an options overlay, not direct proof of an executable underlying-ETH short rule.

The RePEc/EconPapers abstract for the revised paper reiterates that ETH net inflows negatively predict ETH returns and volatility across intraday intervals and that BTC net inflows do not exhibit the same return-predictive pattern, providing a useful internal placebo across assets.

All claims above are source-reported. They have not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- No independent reproduction has been performed here.
- The source does not publish a single canonical underlying-ETH entry threshold, position-sizing rule, or net-of-cost short-strategy result.
- Exchange-address labeling is inherently revision-prone; using modern labels on historical transfers can create information leakage.
- Positive exchange inflow is not equivalent to immediate selling and can be contaminated by internal wallet maintenance, custody changes, bridge flows, staking operations, and OTC settlement.
- The core return sample ends in January 2023, before the later institutional and ETF-era market structure; post-2023 persistence is unproven.
- A regression coefficient can be statistically significant while remaining too small, too delayed, or too costly to monetize.
- The source's stronger options result depends on options-market execution, implied volatility, strike selection, and delta exposure and should not be transferred mechanically to spot/perpetual returns.

## Falsification plan

1. Reconstruct ETH exchange inflows/outflows with point-in-time address labels and explicit label-vintage controls.
2. Reproduce 1h, 2h, 3h, 4h, and 6h forward-return regressions over the source sample without using revised future labels.
3. Extend strictly out of sample from 2023-01-21 onward, including 2024-2026 market structure.
4. Compare raw net inflow, signed log-scaled inflow, rolling z-scores, and percentile ranks; treat any threshold selection as a new research choice.
5. Use contemporaneous and lagged ETH return, realized volatility, volume, market return, and funding/basis controls to test incremental information.
6. Run event studies around top 10%, 5%, and 1% positive net-inflow states and matched placebo timestamps.
7. Remove known exchange internal-wallet migrations and major custody/bridge events; the signal should survive if it represents genuine market-facing sell pressure.
8. Test independent data vendors or independently built exchange-label maps to quantify provider-label risk.
9. Test both spot and perpetual execution with realistic latency, fees, spread, slippage, funding, and borrow constraints.
10. Materially weaken or reject the hypothesis if post-2023 OOS coefficients lose their negative sign, event returns are indistinguishable from matched controls, or realistic net PnL is non-positive across reasonable source-motivated thresholds.

## Crypto portability

direct

The signal is crypto-native and directly uses Ethereum blockchain flows to centralized exchanges. No traditional-market portability assumption is required.

Porting from the source's predictive relation to perpetual execution is adapted rather than automatic because funding, mark/index mechanics, liquidation flows, basis, and leverage can materially change realized PnL.

## Limitations

- Working-paper / preprint evidence.
- Not independently reproduced.
- Core return sample ends 2023-01-20.
- Production entry threshold: underspecified.
- Preferred holding horizon within 1-6 hours: underspecified.
- Position sizing and overlapping-signal state machine: underspecified.
- Historical point-in-time exchange-label availability: data gap.
- Post-2023 and post-ETF market persistence: unproven.
- Net-of-cost profitability for a direct ETH short/perpetual implementation: unproven.

## Implementation status

Research-only. No implementation has been completed in PyBroker, NautilusTrader, the strategy registry, any data pipeline, Paper, Testnet, or Live workflows.

## Adoption boundary

This record is research material only. Presence in the Alpha Strategy Pool does not mean the hypothesis is profitable, validated alpha, approved for implementation, approved for paper trading, approved for testnet, or approved for live trading.

No implementation task is created by this record.

## Related Wiki records

No stable Hermes Wiki Brain link is added in this Scout cycle.

The repository contains other on-chain and microstructure records, but this record remains separate because its identity is specifically the intraday predictive relation between ETH exchange net inflow and subsequent ETH returns.

## Sources

1. Chi, Yeguang; Chu, Qionghua (Ruihua); Hao, Wenyan. *Return and Volatility Forecasting Using On-Chain Flows in Cryptocurrency Markets*. arXiv:2411.06327, submitted 10 November 2024. https://arxiv.org/abs/2411.06327
2. DOI resolver for arXiv:2411.06327. https://doi.org/10.48550/arXiv.2411.06327
3. RePEc/EconPapers record for arXiv:2411.06327, reporting the 2025-09 revised version and updated abstract. https://EconPapers.repec.org/RePEc:arx:papers:2411.06327
