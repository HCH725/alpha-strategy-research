---
schema: strategy-research-record-v1
title: Bitcoin Friday 15:00 EST Post-Event Drift
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - bitcoin
  - intraday
  - seasonality
status: research-only
confidence: medium
source_as_of: 2021-12-31
sources:
  - "https://doi.org/10.24136/oc.2022.022"
  - "https://dehesa.unex.es/server/api/core/bitstreams/9a791b6e-e8e2-427c-b2f5-77b659cede7a/content"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Friday 15:00 EST Post-Event Drift

## Provenance

Primary source: José Luis Miralles-Quirós and María Mar Miralles-Quirós, “A new perspective of the day-of-the-week effect on Bitcoin returns: evidence from an event study hourly approach,” *Oeconomia Copernicana* 13(3), 745–782 (2022), DOI `10.24136/oc.2022.022`, published online 2022-09-25.

The paper studies hourly Bitcoin prices from Kraken over 2016-01-01 through 2021-12-31 and states that timestamps are expressed in Eastern Standard Time (EST). The public University of Extremadura repository PDF was read directly for this Scout cycle.

Repository and Hermes Wiki Brain source-identity checks found no existing record with the same DOI, exact paper title, or the same normalized Friday-15:00-EST post-event rule. Related pool records cover broader same-weekday seasonality, unconditional UTC time-of-day seasonality, and 15-minute candle-boundary seasonality, but none uses this source-specific event-study construction.

## Economic mechanism

### Source-reported

The authors report that Bitcoin hourly returns exhibit a day-of-the-week effect concentrated on Friday and that positive cumulative returns are especially visible in the hours following the Friday 15:00 EST event. They discuss informed-versus-noise-trader timing and recurring within-week trading behavior as possible explanations for the observed pattern.

The source presents the effect as a calendar anomaly rather than as a market-microstructure causal identification result. It does not establish a unique causal channel.

### Research interpretation

The falsifiable hypothesis is a deterministic, clock-conditioned short-horizon drift: after the Friday 15:00–15:59:59 EST event hour has completed, Bitcoin may exhibit positive continuation during the following several hours.

A plausible mechanism is recurring end-of-week information processing, liquidity-demand timing, or participant synchronization before the weekend. This mechanism is unproven. The apparent edge could instead be a sample-specific U.S.-session return pattern, multiple-testing artifact, Kraken-specific effect, or historical regime dependence.

This record therefore treats the calendar rule itself as the predictive signal and does not upgrade the source narrative into established causality.

## Signal

**Source-reported construction:**

- Instrument: Kraken BTC/USD spot.
- Sampling: hourly closing prices.
- Clock convention: Eastern Standard Time (EST), as stated by the paper.
- Event definition: each weekday/hour is treated as an event. For the focal rule, the event is Friday 15:00:00–15:59:59 EST.
- The paper evaluates cumulative post-event returns at 1, 2, 3, 4, 5, 6, 12, 18, and 24 hours after the event.
- For the trading exercise, the authors focus on Friday 15:00 EST and evaluate 4, 5, 6, 12, 18, and 24 hour holding intervals using a rolling three-year estimation window.
- The paper identifies the 4-hour version as the strongest of the tested holding intervals and describes it as buying at 16:00 EST and selling at 19:59:59 EST on Friday.

**Normalized primary hypothesis:**

1. Wait until the Friday 15:00–15:59:59 EST event hour is complete.
2. Enter a long BTC/USD spot position at 16:00 EST.
3. Hold for four hours.
4. Exit at the end of the 19:00–19:59:59 EST hour, corresponding to the source description of selling at 19:59:59 EST.
5. Do not re-enter until the next qualifying Friday.

The 5h, 6h, 12h, 18h, and 24h variants are source-reported robustness branches, not separate pool strategies in this record.

**Underspecified execution detail:** the paper uses hourly close-based returns but does not fully specify a live order type, bid/ask side, latency, or whether the quoted boundary price should be treated as an immediately executable trade. Any implementation using next-tick, next-bar-open, market, or limit execution is **research-proposed** and must not be presented as source-reported.

**Clock ambiguity to preserve:** the paper explicitly says EST rather than a daylight-saving-aware `America/New_York` clock. Exact reproduction should therefore use fixed UTC-5 timestamps. A daylight-saving-aware Eastern Time variant is **research-proposed** only as a robustness test.

## Required data

- Kraken BTC/USD spot market data covering at minimum the source sample, 2016-01-01 through 2021-12-31, plus a strictly later out-of-sample period.
- Hourly closes for source reproduction; preferably trades or top-of-book quotes for execution-aware testing.
- Timestamp precision sufficient to map observations to fixed EST (UTC-5) without ambiguity.
- Bid/ask spread, executable prices, and fees for net-performance testing.
- Missing-hour and stale-print flags. Do not impute missing market observations unless an explicit test protocol justifies the treatment.
- Point-in-time discipline: the Friday event hour must be fully closed before the 16:00 EST entry decision.
- For portability tests, equivalent spot data from additional liquid venues with synchronized timestamps.

## Execution assumptions

The source-reported cumulative abnormal return calculations do not incorporate transaction costs. The authors characterize online Bitcoin trading costs as negligible, but no execution model demonstrating this assumption is provided.

The source does not specify:

- market versus limit order;
- bid/ask side used for entry or exit;
- slippage or market impact;
- signal-to-order latency;
- partial fills or failed orders;
- capacity constraints;
- leverage, margin, or financing.

The normalized hypothesis is long-only spot and therefore does not require borrow or short availability.

For later testing, an executable next-available-price rule with observed taker fees and spread is **research-proposed**. Any synthetic fee, spread, slippage, or latency stress level introduced by the Scout must be labeled **research-defined falsification threshold** when used as a pass/fail cutoff.

## Evidence

### Source-reported

The paper reports hourly event-study evidence for Kraken Bitcoin from 2016-01-01 through 2021-12-31. Friday is the weekday with the strongest recurring positive post-event pattern in the authors’ analysis.

Using rolling one-, two-, and three-year windows, the authors report that the Friday effect remains especially persistent around the 15:00 EST event. In the two-year rolling analysis, they state that the post-event intervals from 4 through 24 hours following the Friday 15:00 event are statistically significant in more than 90% of the rolling windows.

The source then evaluates a Friday-15:00 trading exercise with 4h, 5h, 6h, 12h, 18h, and 24h holding periods and compares the strategy with event-hour-only exposure and a three-year buy-and-hold benchmark. The authors report the strongest performance for the shorter 4h–6h windows, with the 4-hour rule highlighted as the best-performing variant. They conclude that holding Bitcoin for 4–24 hours after the Friday 15:00 event outperforms their stated buy-and-hold comparison in the studied sample.

These are source-reported findings. Transaction costs are omitted from the reported cumulative abnormal returns, and no result above has been independently reproduced in this Scout cycle.

### Independently reproduced

not independently reproduced

### Negative evidence

- The source omits transaction costs from the cumulative abnormal return calculations. This is material for a weekly four-hour strategy whose edge may be small in absolute return terms.
- The source sample ends on 2021-12-31, leaving the persistence of the effect through later crypto market structure, ETF-era participation, and venue changes unverified.
- The focal Friday/hour and holding-window choices emerge from a broad event-study search over many weekday/hour combinations and multiple post-event horizons, creating multiple-testing and selection-risk concerns.
- The paper’s rolling-window robustness analysis reuses the historical sample rather than providing a clean post-publication out-of-sample test.
- Later published research on broad cryptocurrency seasonality reports that several historical weekday effects are unstable in newer samples. That study is not an exact replication of this Friday-15:00 intraday rule, but it weakens any claim that crypto calendar anomalies should be assumed persistent.

## Falsification

1. **Exact source reproduction.** Reconstruct Kraken BTC/USD hourly returns for 2016-01-01 through 2021-12-31 using fixed EST (UTC-5), and reproduce the Friday 15:00 event and 4h post-event return. **Research-defined falsification threshold:** if the sign or qualitative ranking of the 4h rule relative to the source’s other stated holding intervals cannot be reproduced under an exact-enough data convention, classify the source capture as non-reproducible and do not advance it.

2. **Strict post-source out-of-sample test.** Freeze the source rule—Friday, 15:00 EST event, 16:00 entry, 4h hold—without retuning and test data beginning 2022-01-01. **Research-defined falsification threshold:** reject the tradable-alpha hypothesis if the net mean strategy return is non-positive after observed fees and spread, or if annualized net Sharpe is less than or equal to zero over the predeclared OOS sample. Action: retain only as a historical anomaly record.

3. **Clock placebo.** Test adjacent event hours (for example ±1, ±2, and ±3 hours) and other weekdays without changing the holding rule. **Research-defined falsification threshold:** if similarly strong returns are broadly distributed across neighboring hours/days rather than localized around the stated event, reject the specific Friday-15:00 mechanism and attribute the result to a broader session effect.

4. **Multiple-testing correction.** Re-evaluate the original 7 weekdays × 24 hours × reported post-event horizons using a family-wise or false-discovery-rate correction. **Research-defined falsification threshold:** if the focal effect does not survive the predeclared correction at 5%, reject the claim of a distinct event-time anomaly.

5. **Timezone robustness.** Compare the source-faithful fixed EST clock with a daylight-saving-aware `America/New_York` mapping. This branch is **research-proposed**. If only one arbitrary clock convention works and the effect disappears under economically equivalent local-session alignment, downgrade the hypothesis to clock-definition-sensitive.

6. **Venue portability.** Freeze the rule and test other liquid BTC/USD or BTC/stablecoin spot venues using synchronized timestamps. **Research-defined falsification threshold:** if the effect is absent on at least two independent high-liquidity venues while remaining only on Kraken, classify it as venue-specific rather than general Bitcoin alpha.

7. **Cost and execution stress.** Re-run with observed maker/taker fees, half/full spread, and realistic boundary execution. **Research-defined falsification threshold:** if positive expectancy disappears under observed executable costs, reject the tradable version even if the raw return seasonality remains statistically detectable.

8. **Competing explanation test.** Control for unconditional U.S.-session return drift, contemporaneous volatility, Friday-specific volume, and broad market beta. If the Friday-15:00 indicator adds no incremental predictive value after these controls, reject the distinct-calendar-alpha interpretation.

## Crypto portability

**direct** for Bitcoin spot because the source itself studies BTC/USD on Kraken.

Portability beyond the original market is unproven. Crypto-specific considerations include:

- 24/7 trading means there is no formal Friday cash-market close, so the rule is a participant-clock effect rather than an exchange-session close effect.
- Venue fragmentation may make the anomaly Kraken-specific.
- Stablecoin-quoted spot pairs may differ from USD-quoted Kraken BTC/USD.
- Perpetual-futures adaptation would introduce funding, mark/index-price conventions, leverage, liquidation, and basis dynamics absent from the source; such an adaptation would be **research-proposed**, not direct source evidence.
- Fixed EST versus DST-aware local time materially changes the UTC event timestamp and must be controlled explicitly.

## Limitations

- `not independently reproduced`: no independent replication was performed in this Scout cycle.
- `data gap`: no post-2021 evidence was verified for this exact rule.
- `underspecified`: executable entry/exit price, order type, spread, slippage, and latency are not fully defined by the source.
- `unproven`: the causal mechanism is not identified.
- `unproven`: net profitability after current transaction costs and executable fills is unknown.
- Multiple-testing and post-selection risk are material because the focal event was identified from a large weekday/hour/horizon search space.
- The source is single-venue and Bitcoin-only.
- The paper uses EST terminology; interpreting it as daylight-saving-aware New York time without testing would silently change the source rule.

## Implementation status

`not-implemented`.

No PyBroker implementation, Nautilus historical validation, strategy-registry entry, data-pipeline change, Kanban task, Paper workflow, Testnet workflow, or Live workflow was created or modified by this Scout cycle.

## Adoption boundary

This record is research material in the Alpha Strategy Pool only.

It is not evidence that the strategy is profitable, not an implementation instruction, and not approval for Paper, Testnet, or Live trading. The record remains `status: research-only`, `implementation_status: not-implemented`, `adoption: not-approved`, and `approval_scope: research-only` until a separate Research Intake Review and subsequent authorized validation process says otherwise.

## Related Wiki records

No matching Hermes Wiki Brain strategy-research record was identified for this source or exact Friday-15:00-EST post-event mechanism during the pre-write search.

Related Alpha Strategy Pool records, which are not equivalent to Wiki Brain adoption, include:

- `crypto-cross-sectional-same-weekday-seasonality-20w-daily-2026-08-31.md` — cross-sectional same-weekday ranking, materially different source and signal construction.
- `crypto-intraday-utc-return-seasonality-tea-time-2026-09-03.md` — broad unconditional UTC time-of-day return seasonality, materially different event conditioning.
- `bitcoin-turn-of-15min-candle-seasonality-1m-2026-08-31.md` — quarter-hour candle-boundary seasonality, materially different clock phase and horizon.

## Sources

1. Miralles-Quirós, J. L., & Miralles-Quirós, M. M. (2022). “A new perspective of the day-of-the-week effect on Bitcoin returns: evidence from an event study hourly approach.” *Oeconomia Copernicana*, 13(3), 745–782. DOI: https://doi.org/10.24136/oc.2022.022
2. University of Extremadura public repository, open full-text PDF of the same paper: https://dehesa.unex.es/server/api/core/bitstreams/9a791b6e-e8e2-427c-b2f5-77b659cede7a/content
3. Müller, L. (2024). “Revisiting seasonality in cryptocurrencies.” *Finance Research Letters*, 64, 105429. DOI: https://doi.org/10.1016/j.frl.2024.105429 — used only as related negative evidence on the general persistence of cryptocurrency calendar anomalies; not an exact replication of the focal signal.
