---
schema: strategy-research-record-v1
title: "Crypto Same-Day Abnormal-Return Continuation"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - intraday
  - momentum
  - event-conditioned
status: research-only
confidence: medium
source_as_of: 2019-09-01
sources:
  - "Guglielmo Maria Caporale and Alex Plastun, 'Momentum effects in the cryptocurrency market after one-day abnormal returns', Financial Markets and Portfolio Management 34, 251-266 (2020). DOI: https://doi.org/10.1007/s11408-020-00357-1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The abstract/methodology state a 2015-01-01 to 2019-09-01 sample, while the conclusion states 2017-01-01 to 2019-09-01. This record preserves that internal source inconsistency rather than silently choosing one interval."
---

# Crypto Same-Day Abnormal-Return Continuation

## Provenance

Primary source: Guglielmo Maria Caporale and Alex Plastun, *Momentum effects in the cryptocurrency market after one-day abnormal returns*, **Financial Markets and Portfolio Management** 34, 251-266 (2020), first published 2020-05-27; DOI `10.1007/s11408-020-00357-1`; open-access full text at Springer.

The study examines BTCUSD, ETHUSD, and LTCUSD using daily and hourly data from CoinMarketCap, Gemini, and Bitstamp. The abstract and methodology describe the sample as 2015-01-01 through 2019-09-01, while the conclusion states 2017-01-01 through 2019-09-01; this is recorded as a source contradiction.

Repository-wide and Hermes Wiki Brain source-identity searches found no existing record for DOI `10.1007/s11408-020-00357-1` or the exact paper title. Conceptually adjacent records include generic intraday momentum, jump-conditioned reversal, and last-day reversal studies, but this source uses a materially different event definition: a **daily open-to-close abnormal-return threshold, detected intraday, followed by same-day continuation to the daily close**.

## Economic mechanism

### Source-reported

The authors test whether unusually large daily cryptocurrency moves continue rather than immediately reverse. They motivate abnormal returns through market overreaction, herding, noise trading, behavioral biases, low liquidity, and delayed incorporation of information. Their empirical claim is that once an abnormal daily move becomes detectable before the day ends, price tends to continue in that same direction through the remainder of the day; the paper also studies the following day separately.

### Research interpretation

The falsifiable mechanism is **event-conditioned short-horizon continuation after a sufficiently extreme realized daily move**. A large open-to-current-price move may reflect one-sided information arrival, order-flow persistence, forced positioning, or delayed participation that has not yet fully cleared when the dynamic abnormal-return threshold is crossed. If continuation rather than reversal dominates after threshold crossing, a same-day directional position may earn positive gross expectancy.

This mechanism is narrower than generic momentum. It requires an extreme daily state first, and the alpha hypothesis concerns only the residual interval between threshold detection and the end of the trading day.

## Signal

### Source-reported construction

For day or hour `i`, the paper defines percentage return as:

`R_i = (Close_i / Open_i - 1) * 100%`.

A positive abnormal daily return is defined as:

`R_i > mean_n + k * sd_n`

and a negative abnormal daily return as:

`R_i < mean_n - k * sd_n`.

Source-specified `k` values:

- BTCUSD: `k = 2.0`;
- ETHUSD: `k = 1.5`;
- LTCUSD: `k = 1.5`.

The source states that the different `k` values were chosen to obtain sufficient event counts. `mean_n` and `sd_n` are the mean and standard deviation of daily returns over a period `n`, but the reviewed full text does **not** specify a single reconstructable live value or rolling convention for `n`. That element is therefore **underspecified**.

The paper's Strategy 1 is:

1. During the current day, determine when the ongoing daily move has become an abnormal-return event under the source threshold.
2. Open a position **in the same direction** as the abnormal return immediately after detection.
3. Close the position at the end of the day.

The paper estimates asset-specific average detection times from its sample, but those timing estimates are sample-derived rather than a universal live trigger. For BTCUSD, the text reports that positive abnormal days were generally detected after about 18:00 and negative abnormal days after about 16:00; ETHUSD and LTCUSD showed earlier average detection times. The source does not provide a sufficiently clear timezone convention in the reviewed text for production use.

### Research-proposed operationalization

No operational choice below should be treated as source-reported.

- **Research-proposed lookback:** use a fixed rolling 60-calendar-day window of fully closed UTC daily bars to estimate `mean_n` and `sd_n`; 60 days is proposed only to make the rule testable because the source leaves `n` underspecified.
- **Research-proposed formation clock:** at each completed 5-minute or 15-minute bar, compute current open-to-last price return from 00:00 UTC.
- **Research-proposed entry:** when that partial-day return first crosses the positive or negative abnormal-return threshold, enter in the direction of the move at the next executable bar/open quote.
- **Research-proposed exit:** close at the final executable bar before 00:00 UTC; no overnight carry for the Strategy 1 test.
- **Research-proposed re-entry:** at most one entry per asset per UTC day after the first threshold crossing.
- **Research-proposed position sizing:** fixed unit risk / fixed notional for first-pass inference only; no leverage optimization.
- The 60-day lookback, intraday sampling frequency, UTC day boundary, next-bar execution, one-entry rule, and sizing convention are all **research-proposed** and not in the source.

## Required data

- **Instruments:** BTCUSD, ETHUSD, LTCUSD for source replication; liquid BTC/ETH/LTC spot or perpetual instruments for modern portability tests.
- **Source-reported data vendors/venues:** CoinMarketCap, Gemini, Bitstamp.
- **Market type:** source evidence is based on cryptocurrency USD exchange-rate price series; it is not a perpetual-futures study.
- **Timeframe:** daily and hourly in the source; a live reconstruction requires intraday prices granular enough to identify threshold crossing before day-end.
- **Fields:** daily open/close; intraday open/close or timestamped trades/midquotes; fees/spread/slippage for tradability tests.
- **Point-in-time:** threshold statistics must be estimated only from returns available before the current day's signal. Any use of the current day's final close or future sample statistics in threshold formation would be look-ahead.
- **Timestamp:** exact timezone/day-boundary convention is material and **underspecified** in the reviewed source text.
- **Missing data:** source handling is not described in sufficient detail; do not silently impute missing bars or stale prices.
- **Funding/fee/spread needs:** the source trading simulation omits transaction costs. Modern perpetual testing additionally requires funding, mark/index behavior, margin, and liquidation assumptions.

## Execution assumptions

Source-reported Strategy 1 enters after abnormal-return detection and exits at day-end. The paper does not incorporate transaction costs such as spreads, fees, or swaps in the trading simulation and explicitly describes the simulation as a proxy for actual trading.

Material source gaps:

- exact signal-to-order latency is not specified;
- order type and fill model are not specified;
- spread/slippage/impact are omitted;
- exchange fragmentation is not modeled;
- timezone and exact daily close convention are not sufficiently specified for reconstruction;
- short borrow, leverage, and margin treatment are not specified;
- perpetual funding is not applicable to the original spot/exchange-rate evidence and would need separate modeling in a port.

Any modern test must execute only after the threshold is observable and must not reuse the bar that caused threshold crossing at an unavailable price.

## Evidence

### Source-reported

The source reports that abnormal daily returns are generally detectable before the day ends and that prices usually continue in the abnormal-return direction until the daily close. It develops Strategy 1 around that same-day continuation rule.

For positive abnormal-return events, the paper states that Strategy 1 has an average successful-trade rate close to **90%** across the studied cryptocurrencies. For negative abnormal-return events, it reports an average successful-trade rate of about **85%**. It also states that profits per trade and annualized profits are positive and statistically different from random-trading results in the Strategy 1 cases.

These figures are **source-reported**, are based on the paper's historical sample, and are not independently reproduced here. They are especially sensitive to the paper's omission of transaction costs and to its sample-derived timing logic.

The paper reports weaker next-day Strategy 2 results than same-day Strategy 1, and it identifies two next-day exceptions to momentum: BTCUSD after positive abnormal returns and ETHUSD after negative abnormal returns show contrarian behavior instead. This record focuses only on the materially cleaner same-day continuation mechanism.

### Independently reproduced

not independently reproduced

### Negative evidence

- The source omits transaction costs, spreads, fees, swaps, slippage, and market impact from the trading simulation.
- The threshold lookback `n` is not fully specified in the reviewed text, preventing exact reconstruction without further source material.
- The source uses sample-derived timing parameters, creating data-snooping and in-sample timing-selection risk.
- The source contains an internal contradiction over whether the sample begins in 2015 or 2017.
- The sample ends in 2019, before modern perpetual-market dominance, institutional participation, spot ETFs, and major exchange/microstructure changes.
- High win rate alone does not establish positive net expectancy once costs, adverse selection, and realistic fills are modeled.
- Related literature cited by the authors reports mixed momentum versus contrarian effects after large moves, so continuation should not be treated as structurally guaranteed.

## Falsification plan

1. **Exact event-definition reconstruction**
   - Data: BTCUSD, ETHUSD, LTCUSD daily/hourly series over the historical source era if obtainable.
   - Test: reconstruct the dynamic abnormal-return classifier and compare event counts/detection timing against the paper.
   - **Research-defined falsification threshold:** if no reasonable interpretation of `n` reproduces the qualitative event timing and event counts, downgrade the source signal to insufficiently specified rather than tuning `n` to maximize PnL.

2. **Strict modern out-of-sample continuation test**
   - Data: 2020 onward liquid BTC/ETH/LTC spot data, frozen UTC day boundary, fixed predeclared lookback.
   - Metric: post-trigger return from first executable price to UTC day-end, conditioned on positive/negative trigger separately.
   - **Research-defined falsification threshold:** reject the continuation hypothesis if the mean post-trigger return has the wrong sign or a 95% confidence interval that includes zero in both BTC and ETH after realistic costs.

3. **Threshold robustness**
   - Test predeclared nearby values around the source multipliers without optimizing on the evaluation set.
   - **Research-defined falsification threshold:** if alpha appears only at one exact `k` and disappears for modest perturbations, classify it as parameter-fragile.

4. **Clock placebo**
   - Shift the daily boundary by several hours and repeat with otherwise identical rules.
   - **Research-defined falsification threshold:** if similar continuation appears across arbitrary clock shifts with no concentration around the source-style boundary, treat the effect as generic intraday trend persistence rather than a distinct abnormal-day mechanism.

5. **Simple-baseline comparison**
   - Compare the event-conditioned rule against unconditional intraday momentum based on same elapsed-day return and against volatility-only filters.
   - **Research-defined falsification threshold:** reject incremental alpha if abnormal-return conditioning does not improve net expectancy, information ratio, or tail behavior relative to the simpler predeclared baseline.

6. **Cost and latency stress**
   - Include taker fees, half-spread, conservative slippage, and delayed next-bar execution; for perpetuals include funding and liquidation/margin assumptions.
   - **Research-defined falsification threshold:** reject tradability if net expectancy is non-positive under a realistic baseline cost model or becomes negative under modest stress.

7. **Regime and venue robustness**
   - Break results into bull/bear/high-volatility/low-volatility regimes and at least two major liquid venues.
   - **Research-defined falsification threshold:** if the effect is concentrated in one venue or one historical subperiod and is absent after 2020, treat it as regime-specific historical evidence rather than current alpha.

## Crypto portability

**direct** for the research mechanism because the cited source itself studies Bitcoin, Ethereum, and Litecoin.

Modern execution portability remains unproven. The original evidence predates the current perpetual-heavy market structure and does not address:

- perpetual funding and mark/index price mechanics;
- exchange fragmentation and venue-specific day boundaries;
- 24/7 liquidation cascades;
- stablecoin quote effects;
- modern maker/taker fee tiers;
- latency and adverse selection around large intraday moves;
- custody, withdrawal, and venue outage risk.

A spot implementation is closer to the original evidence. A perpetual implementation is an adaptation requiring its own cost, funding, margin, and liquidation tests.

## Limitations

- **underspecified:** the lookback period `n` used to compute the abnormal-return mean and standard deviation is not fully reconstructable from the reviewed text.
- **underspecified:** exact timezone/day-boundary convention is not sufficiently clear for production replication.
- **contested:** the source states conflicting sample start dates (2015 versus 2017).
- **not independently reproduced**.
- **data gap:** exact historical source datasets and supplementary timing tables were not independently reconstructed in this Scout cycle.
- Transaction costs are omitted in the source simulation.
- Asset universe is limited to BTC, ETH, and LTC.
- The evidence is old relative to current crypto market structure.
- The source-selected `k` values depend partly on desired event counts, creating parameter-selection concern.
- Source-reported profitability does not establish current net tradability.

## Implementation status

No PyBroker, NautilusTrader, strategy-registry, data-pipeline, Paper, Testnet, or Live implementation was created or modified in this Scout cycle.

`implementation_status: not-implemented`

## Adoption boundary

This record is research material only. It does not establish validated alpha and does not authorize implementation, Paper, Testnet, or Live trading.

All Scout-added operational choices are explicitly labeled **research-proposed**. All Scout-created acceptance/failure cutoffs are labeled **research-defined falsification threshold**.

## Related Wiki records

No matching record for DOI `10.1007/s11408-020-00357-1` or the exact paper title was found in Hermes Wiki Brain during the pre-write search.

Conceptually adjacent pool records include `crypto-intraday-state-dependent-momentum-jump-reversal-2026-09-01.md`, `bitcoin-intraday-time-series-momentum-volume-session-2026-08-31.md`, and `crypto-cross-sectional-last-day-return-reversal-liquidity-conditioned-2026-08-31.md`. They are not source-identity duplicates: this record uses a source-specific dynamic **daily abnormal-return threshold crossed intraday**, followed by continuation only until that day's close.

## Sources

1. Guglielmo Maria Caporale and Alex Plastun, *Momentum effects in the cryptocurrency market after one-day abnormal returns*, **Financial Markets and Portfolio Management** 34, 251-266 (2020). Published 2020-05-27. DOI: https://doi.org/10.1007/s11408-020-00357-1
2. Springer open-access full text for the same article: https://link.springer.com/article/10.1007/s11408-020-00357-1
