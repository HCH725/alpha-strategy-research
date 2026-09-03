---
schema: strategy-research-record-v1
title: Crypto Intraday Jump Same-Day Directional Continuation
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - intraday
  - jumps
  - microstructure
status: research-only
confidence: medium
source_as_of: 2025-05-06
sources:
  - "Danial Saef, Odett Nagy, Sergej Sizov, et al., 'Understanding temporal dynamics of jumps in cryptocurrency markets: evidence from tick-by-tick data', Digital Finance 6, 605-638 (2024), DOI: 10.1007/s42521-024-00116-1"
  - "Correction published 2025-05-06, DOI: 10.1007/s42521-025-00131-w; correction concerns author affiliation only"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The source reports same-day directional association between intraday jumps and end-of-day returns, but the end-of-day return mechanically contains the jump itself; this does not by itself establish post-jump tradable drift."
  - "The source's retained jump set requires Lee-Mykland detection plus same-day confirmation by Ait-Sahalia-Jacod-Li; causal intraday availability of the confirmation step is underspecified."
---

# Crypto Intraday Jump Same-Day Directional Continuation

## Provenance

Primary source: Danial Saef, Odett Nagy, Sergej Sizov, et al., *Understanding temporal dynamics of jumps in cryptocurrency markets: evidence from tick-by-tick data*, *Digital Finance* 6, 605-638 (2024), published 2024-08-08, DOI `10.1007/s42521-024-00116-1`.

The source is open access. A publisher correction dated 2025-05-06 (`10.1007/s42521-025-00131-w`) only adds a missing author affiliation; it does not alter the empirical method or results.

Source sample: tick-by-tick observations from 2019-04-12 through 2021-09-27, covering BTC, BCH, ETC, ETH, LTC and XRP traded against USDT across Binance, Bitfinex, Bitstamp, Coinbase Pro, HitBTC, OKex and Poloniex. The raw dataset contains approximately 1.76 billion ticks; the paper reports 1,392 detected jumps after its filtering procedure.

Repository-wide source-identity checks found no existing record for DOI `10.1007/s42521-024-00116-1`, the exact paper title, or the same distinctive mechanism of an intraday detected jump followed by same-day directional continuation toward the UTC day close. Hermes Wiki Brain search likewise found no matching record.

Related existing pool records cover cross-sectional jump-variance pricing, realized signed-jump factors, VPIN-based jump prediction, and option-implied jump premia. Those are materially different because they use cross-sectional ranking, volatility decomposition, order-flow toxicity, or options pricing rather than a within-day post-jump directional hypothesis.

## Economic mechanism

### Source-reported

The authors report that cryptocurrency jumps are frequent, asymmetric, clustered, and concentrated in high-attention periods. They argue that high-frequency jumps materially influence short-run price dynamics. In their panel regression, days with a positive intraday jump are associated with positive end-of-day returns, while days with a negative intraday jump are associated with negative end-of-day returns. A jump on the previous day does not significantly predict the following day's return.

The paper also documents strong microstructure caveats: crypto jump timing is difficult to localize precisely because dependent market microstructure noise requires substantial pre-averaging, and the exact jump time can only be approximated.

### Research interpretation

The falsifiable alpha hypothesis is that a sufficiently large, noise-robust intraday information shock may trigger **short-lived same-direction price continuation after the jump**, as information diffuses across venues and market participants, before the effect decays by the next UTC day.

However, the source evidence does **not** isolate post-jump returns from the jump itself. Because the dependent end-of-day return includes the detected intraday jump, the reported sign relation can arise mechanically even when there is zero drift after detection. Therefore this record treats tradable post-jump continuation as **unproven** and requires a post-event decomposition before any alpha claim can survive.

## Signal

The source does not provide a complete tradable entry/exit strategy. The following normalization separates source-reported mechanics from testable Scout operationalization.

### Source-reported jump identification

- Input: high-frequency trade-price data aggregated across the seven exchanges for each cryptocurrency.
- Primary detector: Lee and Mykland jump methodology with pre-averaging to mitigate market microstructure noise.
- Confirmation: retain jumps only when the Ait-Sahalia-Jacod-Li procedure also detects a jump on the same trading day.
- Sign: classify each retained jump as positive or negative.
- Day boundary: 23:59:59 UTC.
- The paper reports that same-day end-of-day returns tend to share the jump sign, while previous-day jumps do not significantly affect the next day's return.

### Research-proposed tradable hypothesis

- **Formation timestamp:** first timestamp at which a jump can be confirmed using only data available up to that moment. This is currently **underspecified** because the source does not establish causal intraday availability of the Ait-Sahalia-Jacod-Li confirmation step.
- **Entry:** after causal confirmation of a positive jump, enter long; after causal confirmation of a negative jump, enter short. This is **research-proposed**.
- **Entry price:** first executable quote or next event-time bar after causal confirmation, never the jump print itself. This is **research-proposed**.
- **Exit:** UTC day close at 23:59:59, or an earlier fixed post-event horizon in robustness tests. This is **research-proposed**.
- **Holding period:** variable, from confirmation time to UTC day close; overlapping same-direction signals may be collapsed to one position per asset. This is **research-proposed**.
- **Opposite-sign re-signal:** flatten and reverse only if the new jump is independently confirmed causally; otherwise ignore. This is **research-proposed**.
- **Sizing:** fixed risk unit or volatility-scaled notional only for testing; no source-reported sizing rule exists. Any chosen rule is **research-proposed**.
- **Stops / take-profit:** none source-reported. Any such rule must be labeled **research-proposed**.

The canonical research signal is therefore **underspecified for live reconstruction** until causal jump-confirmation timing is resolved.

## Required data

- **Instrument:** BTC/USDT, BCH/USDT, ETC/USDT, ETH/USDT, LTC/USDT, XRP/USDT spot or a precisely matched modern equivalent.
- **Universe:** source universe is the six named cryptocurrencies. Any expansion is **research-proposed**.
- **Venue:** source aggregates Binance, Bitfinex, Bitstamp, Coinbase Pro, HitBTC, OKex and Poloniex. A modern replication must explicitly define whether signals are venue-specific or built from a consolidated feed.
- **Timeframe:** raw tick data; pre-averaged high-frequency grids determined by the jump-estimation procedure.
- **Fields:** trade timestamp, trade price, symbol, venue; quote/bid-ask data are additionally required for realistic execution testing even though the source's empirical analysis is trade-price based.
- **Point-in-time:** all jump statistics used for trading must be computed strictly from observations available at or before the simulated decision timestamp. No full-day confirmation may leak into an earlier entry decision.
- **Timestamp:** UTC, with sub-second or event-time precision sufficient to preserve ordering before pre-averaging.
- **Missing data:** source excludes observations/days that cannot be aggregated sufficiently for the jump tests. A replication must preserve this exclusion rule and must not silently impute trade prices for a live signal unless the exact method requires it.
- **Funding/fee/spread needs:** spot fees, bid-ask spread, slippage and impact are required for a trading test. Perpetual portability additionally requires funding, mark/index basis and liquidation assumptions.

## Execution assumptions

The source estimates statistical relationships and does not provide a causal live execution model.

For a falsifiable trading test, all operational execution details are **research-proposed**:

- execute only after causal confirmation, never at the detected jump price;
- use next-observable bid/ask or next-bar execution rather than same-bar close;
- model taker fees and realized spread at minimum;
- include slippage and participation caps because jump periods are precisely when liquidity can deteriorate;
- enforce signal-to-order latency representative of real-time jump computation;
- reject any backtest that relies on end-of-day information to classify an earlier jump;
- for perpetual implementation, include funding, margin, liquidation, mark-price and contract-specific risk.

No leverage, position limit, order type, stop or risk budget is source-reported.

## Evidence

### Source-reported

- Sample: 2019-04-12 to 2021-09-27, six major cryptocurrencies, seven exchanges, approximately 1.76 billion raw ticks.
- The paper reports 1,392 retained jumps; approximately 61% are negative.
- Jumps are concentrated around 13:00-17:00 UTC and are least frequent roughly between 01:00-07:00 UTC.
- Section 5.4 / Table 7 reports that intraday jumps are significantly associated with end-of-day returns in the same direction as the jump.
- The paper reports no significant effect of a previous-day jump on the next day's return.
- The authors explicitly warn that crypto microstructure noise and pre-averaging make exact jump timing difficult to localize.

These are source-reported findings, not independently verified trading results. The source does not report transaction-cost-adjusted PnL for a post-jump trading strategy.

### Independently reproduced

not independently reproduced

### Negative evidence

1. **Mechanical same-day-return contamination:** the dependent end-of-day return contains the detected jump itself. A positive contemporaneous coefficient therefore does not prove positive return from immediately after detection to the close.
2. **No next-day persistence:** the source finds no significant effect from a previous-day jump on the next day's return, implying rapid decay and a narrow potential horizon.
3. **Causal timing gap:** retained jumps require same-day confirmation by a second jump test; whether that confirmation is available intraday without future observations is underspecified.
4. **Microstructure-noise uncertainty:** the source notes that high values of pre-averaging parameters can blur the exact event time, which directly threatens event-driven execution validity.
5. **Sample staleness / regime risk:** source data end in September 2021, before the 2022 deleveraging cycle, 2024 spot-BTC-ETF regime, and later market-structure changes.
6. **No source-reported cost model:** spread, fees, slippage, impact and latency could erase a short-lived continuation effect.

## Falsification plan

1. **Post-jump decomposition test** — Recompute returns strictly from the first causally available post-confirmation executable price to 23:59:59 UTC. **research-defined falsification threshold:** reject the alpha interpretation if the sign-conditioned mean post-jump return is not positive for positive jumps and negative for negative jumps out-of-sample, or if either side has a two-sided HAC/cluster-robust `p >= 0.05` after multiple-testing adjustment.
2. **Mechanical-identity placebo** — Compare the source-style full-day regression with a regression that removes all return accrued before confirmation. **research-defined falsification threshold:** if significance disappears after removing pre-confirmation return, classify the original result as mechanical contemporaneous association rather than tradable drift.
3. **Causal leakage audit** — Re-implement jump detection in streaming form. **research-defined falsification threshold:** if a retained jump cannot be classified using only information available before entry, the tradable hypothesis fails regardless of full-sample statistics.
4. **Horizon decay test** — Measure forward returns over 5m, 15m, 30m, 1h, 3h, 6h and to UTC close. **research-defined falsification threshold:** reject if no contiguous post-event horizon shows sign-consistent OOS continuation after false-discovery-rate control.
5. **Parameter robustness** — Perturb pre-averaging and jump-test significance parameters around the source configuration. **research-defined falsification threshold:** reject if effect sign depends on a narrow parameter choice or vanishes under reasonable microstructure-noise settings.
6. **Venue robustness** — Test consolidated feed, Binance-only, Coinbase-only and other sufficiently liquid venue feeds separately. **research-defined falsification threshold:** reject general portability if the effect is isolated to one venue or appears only after cross-venue timestamp aggregation.
7. **Cost and latency stress** — Apply observed spread, taker fees, slippage and 100ms/500ms/1s/5s decision latency. **research-defined falsification threshold:** reject implementation viability if net expectancy is non-positive at realistic venue-specific costs on the held-out sample.
8. **Regime OOS** — Reserve 2022 onward, including 2022 deleveraging, 2023 recovery, 2024 ETF era and 2025-2026 market structure. **research-defined falsification threshold:** reject if sign-consistent post-jump continuation does not survive at least two materially different post-2021 regimes.
9. **Competing explanation** — Control for contemporaneous volatility, order-flow imbalance, volume burst and market-wide BTC jump state. **research-defined falsification threshold:** if jump sign adds no incremental predictive power after controls, treat it as a proxy rather than independent alpha.

## Crypto portability

**Direct in market domain, unproven as tradable alpha.** The source itself studies cryptocurrency spot markets, so no traditional-market portability assumption is required. However, a modern implementation must adapt to current venue structure.

Key issues:

- 24/7 UTC session boundaries are arbitrary; alternative rolling horizons should be tested.
- Cross-venue fragmentation can make aggregated jump timing differ from executable venue timing.
- Stablecoin quote choice can matter; USDT depeg or venue-specific basis can contaminate jumps.
- Perpetual futures add funding, liquidation, mark/index basis and leverage effects absent from the source spot-style return analysis.
- Modern colocation, market-making and arbitrage may compress any 2019-2021 post-jump continuation faster than in the source sample.

## Limitations

- **underspecified:** causal intraday availability of the dual-test jump confirmation.
- **unproven:** tradable post-jump drift; the paper reports same-day association, not isolated after-jump PnL.
- **data gap:** no independent access/replication of the source's exact tick preprocessing in this Scout run.
- **execution gap:** no source-reported fees, spread, slippage, latency, impact, sizing or risk controls.
- **sample limitation:** April 2019-September 2021 only.
- **identification limitation:** contemporaneous full-day return can mechanically inherit the sign of the jump being used as regressor.
- **microstructure limitation:** pre-averaging can blur event ordering and reduce confidence in exact causal timestamps.
- **multiple-testing risk:** any expansion across assets, horizons and detector settings requires explicit multiplicity control.

## Implementation status

No PyBroker, NautilusTrader, Paper, Testnet, Live, data-pipeline, strategy-registry or production implementation has been created or modified by this research capture.

`implementation_status: not-implemented`

## Adoption boundary

This record is research material only. It does not establish profitability, validate a deployable signal, authorize implementation, or permit Paper/Testnet/Live trading.

`status: research-only`

`adoption: not-approved`

`approval_scope: research-only`

## Related Wiki records

No matching Hermes Wiki Brain record for this DOI, title, or same-day post-jump directional hypothesis was found in the pre-write search.

Related pool families include realized jump-variance pricing, signed-jump cross-sectional factors, VPIN/jump-arrival prediction, and option-implied jump-risk premia, but they are materially different signal constructions and were not treated as duplicates.

## Sources

1. Saef, D., Nagy, O., Sizov, S., et al. *Understanding temporal dynamics of jumps in cryptocurrency markets: evidence from tick-by-tick data*. Digital Finance 6, 605-638 (2024). Published 2024-08-08. DOI: https://doi.org/10.1007/s42521-024-00116-1
2. Saef, D., Nagy, O., Sizov, S., et al. *Correction: Understanding temporal dynamics of jumps in cryptocurrency markets: evidence from tick-by-tick data*. Digital Finance 7, 297 (2025). Published 2025-05-06. DOI: https://doi.org/10.1007/s42521-025-00131-w
