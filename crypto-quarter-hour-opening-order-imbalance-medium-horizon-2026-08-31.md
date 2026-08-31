---
schema: strategy-research-record-v1
title: Crypto Quarter-Hour Opening Order-Imbalance Medium-Horizon Predictability
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - intraday
  - order-flow
  - microstructure
  - seasonality
status: research-only
confidence: medium
source_as_of: 2024-10-31
sources:
  - https://arxiv.org/abs/2607.09426
  - https://arxiv.org/pdf/2607.09426
  - https://ideas.repec.org/p/arx/papers/2607.09426.html
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Quarter-Hour Opening Order-Imbalance Medium-Horizon Predictability

## Provenance

Primary source: Chan Kim and Peter Reinhard Hansen, **“The Quarter-Hour Effect: Periodic Algorithmic Trading and Return Predictability in Cryptocurrency Futures,”** arXiv:2607.09426, July 2026 working-paper version. The PDF is dated 2026-07-13; the public RePEc/arXiv record lists a July 2026 revision.

The source studies Binance USDT-margined perpetual futures for BTC, ETH, XRP, SOL, DOGE, and ADA from 2021-01-01 through 2024-10-31 using aggregate trade data with millisecond timestamps, price, quantity, and aggressor-side information. The paper also reports a cross-exchange replication of the phase-specific dependence pattern for BTC and ETH on Bybit.

This record captures one specific source-backed hypothesis from the paper: order imbalance during the **first 10 seconds of each 15-minute boundary** predicts subsequent returns over roughly 4-12 hours. It is intentionally separate from the existing deterministic “turn-of-the-15-minute-candle” seasonality record, which trades unconditional boundary-minute returns rather than conditioning on signed order flow.

## Economic mechanism

### Source-reported

The authors report periodic bursts in trading activity, volatility, and signed order flow at one-, five-, and especially fifteen-minute clock boundaries. They associate the boundary activity with periodic algorithmic participation, supported in part by a sharp decline in trade-size roundness at those times.

For the predictive result relevant here, the paper finds that quarter-hour opening order imbalance has weak or negative short-horizon association with subsequent returns but becomes positively predictive at medium horizons. The effect is much stronger at the 15-minute boundary than at ordinary times or finer one-minute boundaries. The authors interpret the horizon pattern as consistent with systematic algorithmic order flow and public-state information becoming incorporated over several hours rather than as a structural causal impulse response.

### Research interpretation

The falsifiable hypothesis is that a concentrated burst of buyer- versus seller-initiated volume during the first 10 seconds after a quarter-hour boundary contains information about medium-horizon net demand. Positive opening imbalance should, on average, precede positive 4-12 hour returns; negative opening imbalance should precede negative returns.

This is a **clock-phase-conditioned order-flow signal**, not generic order-flow imbalance and not an unconditional calendar effect. The economically important conditioning variable is the quarter-hour phase itself.

A plausible mechanism is synchronized algorithmic execution or portfolio rebalancing that creates persistent directional pressure whose information content is not fully absorbed in the opening seconds. This remains a hypothesis rather than a proven causal mechanism.

## Signal

Source-supported signal definition:

1. Venue/market: Binance USDT-margined perpetual futures in the source.
2. Clock filter: quarter-hour openings at minute-of-hour `00`, `15`, `30`, or `45`.
3. Measurement window: the **first 10 seconds** of the quarter-hour opening.
4. For trades in that 10-second interval, compute signed order flow and normalize by total traded volume:

```text
OI_t = signed_order_flow_t / total_volume_t
```

where `OI_t` is bounded in `[-1, 1]` and aggressor side is inferred from the Binance `isBuyerMaker` field.

5. Directional hypothesis:

```text
if OI_t > 0:
    expected return over the next 4-12h is positive
if OI_t < 0:
    expected return over the next 4-12h is negative
```

The paper’s regression design measures forward log return from the price immediately after the signal interval and estimates horizons from 30 seconds through 24 hours. The source-reported predictive association is strongest and most consistent around 4, 8, and 12 hours.

**Underspecified trading rule:** the source establishes predictive regressions, not a canonical executable portfolio rule. It does not prescribe a single production threshold for `|OI_t|`, a mandatory holding horizon among 4/8/12 hours, whether overlapping signals should stack or replace one another, position sizing, or a transaction-cost-aware entry filter. Those choices must not be invented here.

## Required data

- Instruments: BTC, ETH, XRP, SOL, DOGE, ADA perpetual futures for direct source reproduction.
- Venue: Binance USDT-margined perpetual futures; Bybit is relevant only to reported cross-exchange robustness of the periodic structure.
- Time resolution: individual trades or data granular enough to reconstruct the first 10 seconds of every quarter-hour boundary.
- Required fields: millisecond timestamp, trade price, quantity, aggressor side / `isBuyerMaker` equivalent.
- Derived fields: buyer-initiated and seller-initiated volume, signed order flow, total volume, quarter-hour phase, forward returns.
- Price anchor: source main tests use transaction-price anchoring; appendix robustness also examines bid-ask mid-price anchoring over the period where quote data are available.
- Timezone: exact Binance exchange timestamp convention must be preserved; boundary alignment errors are a first-order risk.
- Point-in-time requirement: only trades observed inside the completed first 10-second signal window may enter the signal.
- Missing-data assumption: missing or incomplete boundary windows should be excluded rather than imputed silently.

## Execution assumptions

The source does **not** present the medium-horizon order-imbalance result as a complete net-of-cost trading strategy.

An executable test would therefore need to specify and model:

- entry immediately after the first 10-second boundary window closes;
- 4h, 8h, and 12h holding horizons tested separately rather than selected ex post;
- market versus passive entry;
- fees, spread, slippage, and impact;
- funding accrued over the holding interval;
- overlapping quarter-hour signals and gross/net exposure caps;
- whether a new opposite signal closes, reverses, or coexists with an existing position;
- leverage, margin, liquidation, and venue-risk constraints;
- latency between final trade in the 10-second window and order submission.

The paper notes that standard-tier Binance USDT perpetual fees over its sample were materially larger than the average gross edge in its separate **first-10-second opening-return forecasting** exercise. That fee comparison should not be transferred mechanically to the 4-12 hour order-imbalance regression, but it reinforces that cost-aware execution is essential.

## Evidence

### Source-reported

The source reports that order imbalance during the first 10 seconds of quarter-hour openings predicts cumulative future returns much more strongly at medium horizons than at short horizons.

For the six Binance perpetual contracts, the quarter-hour cumulative forecasting effect is positive at 4-12 hour horizons in every market. In the baseline discussion, estimates are statistically significant at the 95% level for four of six contracts across the 4h, 8h, and 12h horizons; SOL and ADA have weaker cells, with SOL at the 8h horizon reported as the sole insignificant cell in that comparison.

A robustness specification that keeps only the 15-minute interaction reports the following source-reported cumulative predictive slopes, in basis points per unit of order imbalance:

- BTC: 3.84 / 5.55 / 6.39 bps at 4h / 8h / 12h;
- ETH: 2.76 / 4.68 / 5.40 bps;
- XRP: 2.68 / 6.20 / 7.78 bps;
- SOL: 3.29 / 2.41 / 6.73 bps;
- DOGE: 5.02 / 8.49 / 11.33 bps;
- ADA: 2.07 / 5.39 / 5.10 bps.

The paper further reports that replacing raw imbalance with only its sign preserves positive medium-horizon predictive content for many contract/horizon combinations, and that excluding quarter-hours coinciding with funding settlement leaves the qualitative pattern intact.

The underlying sample for these medium-horizon regressions is 2021-01-01 through 2024-10-31. These are source-reported predictive-regression results, not independently verified trading returns.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself supplies several important caveats:

- predictive content is weak or negative at short horizons and becomes material only around 4-12 hours;
- SOL is notably less robust than the other contracts at some horizons;
- the result is a predictive association, not a structural causal impulse response;
- order imbalance is noisy: the paper reports that most first-10-second imbalance variation is residual rather than explained by its lag/public-signal decomposition;
- the paper does not provide a complete net-of-cost trading rule for this medium-horizon signal;
- results are estimated on 2021-2024 data and may decay after publication or as execution conventions change.

A related but distinct source result forecasts the **first 10-second return itself** at quarter-hour openings. The paper reports only about 0.5 bp average gross realized edge per trade for that separate forecast, versus materially larger standard-tier Binance round-trip fees. This is not negative evidence against the 4-12 hour imbalance signal directly, but it warns against conflating statistical predictability with immediately tradable alpha.

## Falsification plan

A modern reproduction should materially weaken or reject the hypothesis if any of the following occurs:

1. Reconstructing `OI_t` from point-in-time Binance trade data does not reproduce a positive 4-12h coefficient at true quarter-hour openings.
2. Shifted placebo grids such as `01/16/31/46` or other non-boundary phases perform similarly, undermining the quarter-hour conditioning mechanism.
3. The signal disappears after controlling for ordinary contemporaneous order imbalance, recent returns, volatility, volume, and bid-ask-bounce proxies.
4. Positive and negative `OI_t` signs fail to produce directionally symmetric medium-horizon predictability.
5. The result does not persist in a strict post-2024 out-of-sample period.
6. The effect is confined to one venue or one asset and fails on independent liquid perpetual venues.
7. A feasible non-overlapping or exposure-capped execution rule is non-profitable after fees, funding, spread, slippage, and market impact.
8. The apparent effect is sensitive to timestamp alignment, trade-side classification, or price anchoring in a way that removes economic significance.

Tests should pre-specify 4h, 8h, and 12h horizons. Failure at one horizon should not trigger unconstrained horizon mining.

## Crypto portability

**Direct** for liquid crypto perpetual futures where aggressor-side trade data and exact clock timestamps are available.

**Adapted / unproven** for:

- spot markets, where leverage, funding, and participant composition differ;
- options and dated futures;
- smaller altcoins with sparse first-10-second activity;
- venues whose matching-engine timestamps or trade-side flags differ materially from Binance.

Crypto-specific portability risks include 24/7 clocks, exchange timestamp conventions, venue fragmentation, funding schedules, liquidation-driven flow, mark/index differences, and rapid post-publication adaptation by market makers.

## Limitations

- **Not independently reproduced.**
- **Underspecified:** no canonical live threshold, holding horizon, overlap rule, sizing rule, or exit state machine is supplied by the source for this signal.
- **Data intensive:** requires reliable aggressor-side trade data at 10-second-or-finer resolution.
- **Working-paper risk:** the cited source is a 2026 arXiv working paper rather than a final peer-reviewed journal version as of this record.
- The source sample ends 2024-10-31; current persistence is unproven.
- Medium-horizon coefficients are statistically meaningful but modest in absolute basis-point terms, so implementation economics remain uncertain.
- The proposed algorithmic-trading mechanism is empirically motivated but not causally established.

## Implementation status

Not implemented in the research stack. No PyBroker, NautilusTrader, Paper, Testnet, or Live reproduction has been performed.

## Adoption boundary

This record is `research-only`, `not-implemented`, and `not-approved`. Presence in the Alpha Strategy Pool does not imply validated alpha, executable profitability, implementation approval, paper-trading approval, testnet approval, or live-trading approval.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted in this Scout cycle.

Related strategy-pool records include:

- `bitcoin-turn-of-15min-candle-seasonality-1m-2026-08-31.md` — unconditional BTC spot return concentration at 15-minute candle turns; distinct source, market type, and signal construction.
- `crypto-multilevel-order-flow-imbalance-intraday-2026-08-31.md` — generic intraday order-flow imbalance family; not conditioned on quarter-hour clock phase.

## Sources

1. Kim, C., & Hansen, P. R. (2026). “The Quarter-Hour Effect: Periodic Algorithmic Trading and Return Predictability in Cryptocurrency Futures.” arXiv:2607.09426. Stable abstract: https://arxiv.org/abs/2607.09426
2. Full public working paper PDF, July 2026 version: https://arxiv.org/pdf/2607.09426
3. RePEc/IDEAS record for arXiv paper 2607.09426: https://ideas.repec.org/p/arx/papers/2607.09426.html
