---
schema: strategy-research-record-v1
title: Bitcoin Intraday Time-Series Momentum Using Volume-Defined Trading Sessions
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - bitcoin
  - intraday
  - momentum
  - market-microstructure
status: research-only
confidence: medium
source_as_of: 2022-05
sources:
  - https://doi.org/10.1111/fire.12290
  - https://research.birmingham.ac.uk/en/publications/bitcoin-intraday-time-series-momentum/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Intraday Time-Series Momentum Using Volume-Defined Trading Sessions

## Provenance

Primary source: Shen, Dehua; Urquhart, Andrew; Wang, Pengfei (2022), “Bitcoin intraday time series momentum,” *Financial Review*, 57(2), 319–344, DOI: `10.1111/fire.12290`. The article was first published online on 2021-10-26 and appeared in the May 2022 issue.

Stable sources reviewed:

- https://doi.org/10.1111/fire.12290
- https://research.birmingham.ac.uk/en/publications/bitcoin-intraday-time-series-momentum/

The public abstract and institutional publication page clearly state the principal predictive relation and economic interpretation, but do not expose all implementation details needed to reconstruct the authors’ exact backtest. This record therefore preserves the idea as a source-backed alpha hypothesis and marks missing details explicitly rather than inventing them.

## Economic mechanism

### Source-reported

The authors report that Bitcoin’s first half-hour return positively predicts its last half-hour return when the 24-hour market is segmented using trading activity rather than a conventional exchange open/close. They use trading volume as a proxy for market trading time and report that predictability is strongest in trading sessions characterized by the highest volume or volatility.

The authors attribute the documented intraday momentum primarily to liquidity provision rather than late-informed trading. They also report stronger economic gains from the timing strategy during Bitcoin market downturns.

### Research interpretation

The falsifiable mechanism is an intraday persistence effect concentrated around periods of elevated market participation. If early-session price pressure reflects liquidity demand that is only partially absorbed, subsequent same-session or end-session price changes may continue in the same direction before liquidity fully normalizes.

This is economically distinct from multi-day cross-sectional momentum. The signal is time-series, single-asset, intraday, and conditioned by session activity. The volume/volatility conditioning is potentially part of the alpha mechanism rather than merely an execution filter.

## Signal

Source-backed normalized hypothesis:

1. Define a recurring intraday trading session for Bitcoin using the source’s activity-based session convention, where trading volume is used as a proxy for market trading time.
2. Measure the return during the first 30 minutes of that session.
3. Use the sign and/or magnitude of the first-half-hour return to forecast the return during the final 30 minutes of the same session.
4. Positive early return implies positive expected late-session return; negative early return implies negative expected late-session return.
5. The source reports stronger predictability for sessions with high volume or high volatility.

The exact trading rule is **underspecified** in the public material reviewed. Specifically, the following are not reconstructed from the accessible source pages:

- the exact timezone and clock boundaries used to define each recurring session;
- the exact historical volume window used to identify the relevant trading session;
- whether the trading strategy uses only the sign of the first-half-hour return or a continuous magnitude-based forecast;
- exact entry timestamp after signal formation;
- exact exit timestamp and price convention;
- whether the high-volume/high-volatility conditioning is ex ante, contemporaneous, or used only in subsample analysis;
- exact position-sizing rule;
- exact fee, spread, slippage, and leverage assumptions.

Do not treat this record as a fully reconstructable implementation specification until those details are recovered from the full paper or independently specified and validated.

## Required data

Minimum research data requirements:

- Instrument: Bitcoin spot or a clearly specified Bitcoin trading instrument.
- Venue: source venue(s) must be recovered from the full paper before exact replication; venue fragmentation may materially affect results.
- Market type: likely spot in the original study, but exact replication must confirm source data.
- Timeframe: at least 30-minute bars; finer-grained data are preferable to construct precise session boundaries.
- Fields: timestamp, open, high, low, close, traded volume; realized-volatility inputs if reproducing the high-volatility conditioning.
- Timestamp: consistent timezone and 24/7 clock convention.
- Point-in-time: volume/volatility filters must use only information available before the trade decision.
- Missing-data: do not impute missing bars silently; stale or partial bars must be excluded or handled by a predeclared rule.

For perpetual-futures adaptation, additional fields would be required: mark/index price, funding rate, funding timestamp, contract specification, fees, and spread/slippage data.

## Execution assumptions

The accessible public sources do not provide enough detail to reproduce execution exactly.

Research implementation should therefore explicitly test:

- signal formed after the first 30-minute interval closes;
- execution at next available tradable price rather than the already observed signal bar close unless source documentation confirms otherwise;
- exit at the start/end of the final 30-minute interval according to a predeclared convention;
- taker and maker fee variants;
- bid-ask spread and slippage sensitivity;
- latency sensitivity;
- no leverage in the baseline replication;
- no assumption of frictionless shorting unless the selected instrument permits it.

Any same-bar execution convention that uses information unavailable at order time would invalidate the test.

## Evidence

### Source-reported

Shen, Urquhart, and Wang report statistically meaningful Bitcoin intraday time-series momentum in which the first half-hour positively predicts the final half-hour return. They report stronger predictability for initial trading sessions with high volume or volatility and substantial economic gains from momentum-based market timing and asset allocation, particularly during Bitcoin downturns.

The source also reports evidence consistent with liquidity provision as the mechanism rather than late-informed trading.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No direct independent replication or contradiction was identified in the sources reviewed for this capture.

Important caution: the publicly accessible abstract does not expose the exact session construction, trading rule, costs, or sample definition. Therefore the economic-value claim must remain source-reported and should not be interpreted as verified net alpha.

## Falsification plan

The hypothesis would be materially weakened or rejected if, under a leakage-safe replication:

- first-half-hour returns do not significantly predict final-half-hour returns out of sample;
- the effect disappears after realistic fees, spread, and slippage;
- results depend entirely on one timezone/session definition selected after observing outcomes;
- predictability vanishes when the session and volume/volatility filters are fixed ex ante;
- the result is confined to one venue and fails across major liquid Bitcoin venues;
- apparent momentum is explained by overlapping bars, stale prices, data-quality issues, or same-bar look-ahead;
- the high-volume/high-volatility subgroup does not outperform a predeclared unconditional baseline;
- the sign of the relation is unstable across market regimes without a reproducible regime rule.

Required robustness tests should include multiple non-overlapping sample periods, venue replication, alternative but predeclared timezone conventions, cost sensitivity, and an unconditional intraday-momentum baseline.

## Crypto portability

**Direct** for Bitcoin spot if the original source specification can be recovered.

**Adapted / unproven** for Bitcoin perpetual futures and other cryptocurrencies. Perpetual markets introduce funding, mark/index-price mechanics, leverage-driven liquidations, and potentially different intraday liquidity cycles. Altcoins may have materially different volume concentration and venue fragmentation.

The strategy is particularly sensitive to 24/7 session definition. Any crypto adaptation must fix candle boundaries and timezone rules before evaluation.

## Limitations

- **underspecified**: exact session construction and exact trading rule are not recoverable from the public abstract alone.
- **not independently reproduced**.
- **data gap**: original venue, exact sample period, and execution-cost specification must be recovered from the full paper for faithful replication.
- **unproven** outside the original Bitcoin setting.
- High turnover makes cost assumptions potentially decisive.
- Intraday market structure may have changed materially since the original sample.
- Results may be sensitive to exchange fragmentation and timezone/session definitions.

## Implementation status

No implementation has been completed in PyBroker, NautilusTrader, or any other internal research stack.

`implementation_status: not-implemented`

## Adoption boundary

This record is research material only. It is not evidence of validated alpha and is not approved for implementation, paper trading, testnet, or live trading.

`status: research-only`

`adoption: not-approved`

`approval_scope: research-only`

## Related Wiki records

No stable related Hermes Wiki Brain record was referenced in this Scout cycle. Concept-level consolidation belongs to the separate future Reviewer workflow.

## Sources

1. Shen, D., Urquhart, A., & Wang, P. (2022). Bitcoin intraday time series momentum. *Financial Review*, 57(2), 319–344. https://doi.org/10.1111/fire.12290
2. University of Birmingham research record for the same peer-reviewed article: https://research.birmingham.ac.uk/en/publications/bitcoin-intraday-time-series-momentum/
