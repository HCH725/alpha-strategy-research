---
schema: strategy-research-record-v1
title: Bitcoin U.S. Spot ETF Net-Flow Next-Day Drift
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - bitcoin
  - etf-flow
  - institutional-flow
  - price-impact
status: research-only
confidence: medium
source_as_of: 2025-04-30
sources:
  - https://doi.org/10.2139/ssrn.6592830
  - https://doi.org/10.3905/jai.2025.1.239
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - The primary working paper reports both flow-to-return predictability and return-to-flow feedback, so causal interpretation is not clean.
  - The same paper reports that individual flow shocks reverse after conditioning on future flows, implying that observed multi-day drift may reflect persistent follow-on flows rather than permanent information.
---

# Bitcoin U.S. Spot ETF Net-Flow Next-Day Drift

## Provenance

Primary source: Boon Chuan Lim, "The Price Impact of Spot Bitcoin ETF Flows," SSRN working paper, January 2026, DOI: https://doi.org/10.2139/ssrn.6592830. The public abstract reports daily net-flow data for the five largest U.S. spot Bitcoin ETFs over January 2024 through April 2025, totaling 313 trading days.

Supporting peer-reviewed/institutional source: Mieszko Mazur and Efstathios Polyzos, "Spot Bitcoin ETFs: The Effect of Fund Flows on Bitcoin Price Formation," *Journal of Alternative Investments* 27(4), 110-123 (2025), DOI: https://doi.org/10.3905/jai.2025.1.239. The institutional repository record reports a strong positive association between ETF net flows and Bitcoin price levels and documents substantial capital-flow magnitudes during the early post-launch period.

The SSRN paper is the canonical source for the next-day predictive claim in this record. The Mazur-Polyzos article is supporting evidence for the broader ETF-flow/Bitcoin price-formation mechanism, not evidence for the exact same next-day specification.

## Economic mechanism

### Source-reported

Lim reports that U.S. spot Bitcoin ETF net flows have material price impact and predict next-day Bitcoin returns. The paper also reports strong flow persistence and a bidirectional feedback loop in which prior returns affect subsequent ETF flows. Its interpretation is that repeated institutional flow shocks can create cumulative price drift because new flows arrive before earlier price-impact shocks fully reverse.

Mazur and Polyzos report that spot Bitcoin ETF capital flows became a major component of Bitcoin price formation during the early post-approval period.

### Research interpretation

The alpha hypothesis is not "ETF inflow causes a same-day BTC move" because same-day fund-flow data may be finalized only after much of that move has occurred. The usable hypothesis is narrower:

> Once day-t aggregate U.S. spot Bitcoin ETF net flow is fully observable, unusually positive net flow predicts positive BTC return on the next eligible horizon, while unusually negative flow predicts negative next-period return.

The mechanism is persistent institutional demand/supply pressure transmitted through ETF creation/redemption, spot acquisition or disposal, arbitrage, and inventory rebalancing. A competing explanation is endogenous flow chasing: BTC returns attract ETF flows, which makes flow appear predictive without representing an independent causal signal.

## Signal

Source-backed normalized hypothesis:

- Instrument: Bitcoin spot or a closely tracking liquid Bitcoin derivative.
- Explanatory variable: aggregate daily net flow across major U.S. spot Bitcoin ETFs.
- Signal formation: only after the day-t ETF flow figure is publicly finalized and timestamped.
- Direction:
  - positive day-t net flow -> long bias for the next trading horizon;
  - negative day-t net flow -> short / underweight bias for the next trading horizon.
- Primary horizon: next day / next eligible post-publication return interval.

Underspecified in the public primary materials reviewed in this Scout cycle:

- exact net-flow threshold required to initiate a position;
- whether raw dollar flow, flow/AUM, flow/BTC market cap, z-score, or another normalization is optimal;
- exact publication timestamp and data-vendor latency used by the source;
- exact long/short portfolio mapping;
- exact holding cutoff in UTC versus U.S. market hours;
- whether weekends are skipped, carried, or treated separately;
- exact transaction-cost model used for a standalone trading-rule interpretation.

Do not infer those details from the reported regression coefficient.

## Required data

- Daily net subscriptions/redemptions or equivalent net-flow estimates for U.S. spot Bitcoin ETFs, point-in-time and timestamped.
- ETF-level flows for at least the dominant funds, with an aggregate series constructed without look-ahead revisions.
- BTC spot prices with precise UTC timestamps.
- If trading a perpetual or futures implementation: mark/index price, funding, basis, contract availability, and roll data where applicable.
- Trading calendar mapping between U.S. ETF business days and Bitcoin's 24/7 market.
- Revision history for ETF-flow data because same-day preliminary estimates may differ from finalized values.

## Execution assumptions

Same-day execution using a flow value that was not yet publicly finalized is prohibited. The signal must be formed only after the relevant ETF flow data are observable in real time.

A research implementation should:

- enter no earlier than the first feasible BTC trading timestamp after the day-t flow publication;
- model spread, taker/maker fees, slippage, and funding/basis if derivatives are used;
- explicitly handle Friday flows, weekends, U.S. holidays, and asynchronous publication schedules;
- distinguish a U.S.-hours return window from a full 24-hour UTC return window;
- record stale, delayed, or revised flow prints as data-quality events rather than silently backfilling them.

## Evidence

### Source-reported

Lim reports, for January 2024 through April 2025 and the five largest U.S. spot Bitcoin ETFs, that a $100 million net flow is associated with approximately 53 basis points of same-day BTC return under OLS. Flows explain approximately 21% of daily return variation in that specification. More relevant to this record, the paper reports that ETF flows predict next-day Bitcoin returns with a Newey-West t-statistic of 3.12.

The same source reports bidirectional Granger-causality evidence: returns predict subsequent flows as well as flows predicting returns. It also reports strong flow persistence. Unconditionally, cumulative post-flow returns do not reverse over 1-20 days, but after controlling for future flows, individual flow shocks reverse significantly. The author interprets this as a flow-persistence effect rather than evidence that each individual price-impact shock is permanent.

Mazur and Polyzos report that ETF net flows are strongly positively associated with Bitcoin valuation during the early post-launch period. Their public institutional record also states that most Bitcoin price changes in their sample occur outside ETF trading hours. This supports the broader idea that flow-related price formation extends beyond the exchange session, but it is not a direct replication of Lim's next-day regression.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The sample starts only with the January 2024 U.S. spot-ETF launch and runs through April 2025, so the next-day relation is based on a short and structurally unusual regime.
- Returns also predict later flows, creating endogeneity and trend-chasing risk.
- Conditional reversal of individual flow shocks weakens any claim that one isolated inflow has permanent price impact.
- Public ETF-flow datasets are frequently revised and can have publication delays, creating severe look-ahead risk if backtests use finalized historical data without release timestamps.
- ETF flows may include market-neutral basis trades rather than directional demand, so gross inflow is not always equivalent to net bullish exposure.

## Falsification plan

1. Build a point-in-time ETF-flow database preserving first-publication timestamp and subsequent revisions.
2. Reproduce the next-day regression through April 2025 before extending the sample.
3. Run a genuine post-April-2025 holdout, including 2025-2026 bull, bear, high-outflow, and low-basis regimes.
4. Compare raw dollar flow with flow normalized by ETF AUM, BTC market cap, rolling volatility, and trailing flow dispersion.
5. Control for prior BTC return, CME basis, perpetual funding, realized volatility, dollar strength, equity risk sentiment, and lagged ETF flow.
6. Separate flow shocks from predictable flow continuation using an AR/VAR residual or other ex-ante innovation measure.
7. Test multiple feasible signal timestamps based on actual public release times rather than end-of-day hindsight.
8. Include Friday/weekend handling as a pre-specified branch, not a post-hoc optimization.
9. Reject or materially downgrade the hypothesis if the point-in-time post-publication signal fails to produce positive OOS information coefficient or net PnL after realistic costs, or if significance disappears after controlling for prior returns and expected flow persistence.

## Crypto portability

direct

The hypothesis is native to Bitcoin and U.S. spot Bitcoin ETFs. It does not automatically port to altcoins or non-U.S. ETF products. Potential adaptations to ETH or future crypto ETFs require independent testing because creation/redemption mechanics, AUM, liquidity, arbitrage depth, and investor base differ.

## Limitations

- Not independently reproduced.
- Working-paper evidence; the primary next-day result is not treated as final settled evidence.
- Short post-ETF historical sample.
- Flow timestamp / revision handling is a critical data gap for any real-time backtest.
- Exact production threshold and position-sizing rule are underspecified.
- Causality is contested because returns predict flows as well as flows predicting returns.
- Persistent market-neutral basis activity may contaminate a directional interpretation of ETF flows.
- Weekend and U.S.-holiday timing can materially change the realized holding window.

## Implementation status

Research-only. No PyBroker, NautilusTrader, strategy-registry, data-pipeline, paper, testnet, or live implementation has been created or modified in this Scout cycle.

## Adoption boundary

This record is Alpha Strategy Pool staging material only. It is not evidence that the hypothesis is currently profitable, not approval for implementation, and not authorization for paper, testnet, or live trading.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted here.

Related Alpha Strategy Pool families include institutional-flow, market-microstructure, and Bitcoin price-impact research. This record remains separate because its source, ETF-specific data, post-2024 regime, and next-day signal timing are materially distinct.

## Sources

1. Lim, Boon Chuan. "The Price Impact of Spot Bitcoin ETF Flows." SSRN working paper (2026). DOI: https://doi.org/10.2139/ssrn.6592830
2. Public abstract mirror for Lim's working paper, preserving the reported sample and next-day statistic: https://www.researchgate.net/publication/403907112_The_Price_Impact_of_Spot_Bitcoin_ETF_Flows
3. Mazur, Mieszko; Polyzos, Efstathios. "Spot Bitcoin ETFs: The Effect of Fund Flows on Bitcoin Price Formation." *Journal of Alternative Investments* 27(4), 110-123 (2025). DOI: https://doi.org/10.3905/jai.2025.1.239
4. Zayed University institutional repository record for Mazur-Polyzos: https://zuscholars.zu.ac.ae/works/7267/
