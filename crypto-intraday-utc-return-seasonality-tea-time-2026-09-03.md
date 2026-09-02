---
schema: strategy-research-record-v1
title: "Crypto UTC Intraday Return Seasonality Around Global Trading Hours"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - intraday
  - seasonality
  - time-of-day
  - liquidity
  - volatility
status: research-only
confidence: medium
source_as_of: 2024-06-10
sources:
  - "Brauneis, Mestel, Theissen (2024), 'The crypto world trades at tea time: intraday evidence from centralized exchanges across the globe', Review of Quantitative Finance and Accounting, DOI: 10.1007/s11156-024-01304-1, published 10 June 2024. https://doi.org/10.1007/s11156-024-01304-1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto UTC Intraday Return Seasonality Around Global Trading Hours

## Provenance

Primary source: Alexander Brauneis, Roland Mestel, and Erik Theissen, **"The crypto world trades at tea time: intraday evidence from centralized exchanges across the globe"**, *Review of Quantitative Finance and Accounting* 64, 275–304 (2025), published online 10 June 2024, DOI `10.1007/s11156-024-01304-1`, open-access canonical URL: https://doi.org/10.1007/s11156-024-01304-1.

The source analyzes hourly data from 1 July 2018 00:00 UTC through 1 January 2022 24:00 UTC. After filtering, its final panel contains 1,940 currency-pair/venue series across 38 centralized cryptocurrency exchanges and 386 currencies/tokens including fiat currencies and stablecoins. Data fields are hourly OHLC, volume, and transaction count from CryptoTick. The source explicitly studies time-of-day patterns rather than a complete executable trading strategy.

Repository source-identity check before writing found no existing record containing DOI `10.1007/s11156-024-01304-1`, the exact paper title, or the distinctive "tea time" mechanism. Wiki Brain source-identity search likewise found no record containing this DOI. Broadly related intraday records exist, but they use materially different signal constructions such as momentum, short-horizon reversal, candle-boundary effects, or order-flow imbalance.

## Economic mechanism

### Source-reported

The paper argues that crypto markets exhibit pronounced intraday patterns despite operating continuously without overnight closures or daily settlement. The authors interpret the cross-venue similarity of activity, volatility, liquidity, and return patterns as evidence that common information flow and globally synchronized trading activity matter more than purely local exchange-specific trader behavior.

The source reports that returns are below average from approximately 01:00 to 05:00 UTC, reach their daily peak between 15:00 and 16:00 UTC, and are also positive during the final three hours of the UTC day. Trading volume, transaction count, volatility, and illiquidity rise through the afternoon and generally peak around 16:00–17:00 UTC. The paper does **not** claim that a time-of-day trading rule is profitable after costs; it explicitly identifies strategy profitability as future research.

### Research interpretation

The falsifiable alpha hypothesis is a **UTC time-of-day return seasonality** associated with globally synchronized information arrival and trading participation. If the return pattern is persistent rather than sample-specific, a deterministic clock-based exposure schedule may contain incremental predictive information relative to an always-invested or time-shuffled control.

The trading interpretation below is **research-proposed**, not source-reported. It converts the descriptive return pattern into a minimal testable hypothesis while preserving the source's uncertainty about profitability.

## Signal

**Status:** partially specified by the source; executable trading rules are `research-proposed`.

### Source-reported pattern

- **Formation timestamp:** hourly UTC observations; the source defines hour labels so that, for example, hour 4 covers 03:00–04:00 UTC.
- **Weak-return window:** returns tend to be below average from 01:00 to 05:00 UTC.
- **Strong-return window:** returns reach their peak during 15:00–16:00 UTC.
- **Additional positive-return window:** the final three hours of the UTC day are positive on average in the source's aggregate pattern.
- **Activity/liquidity regime:** volatility, trading volume, transaction count, and illiquidity increase in the afternoon and generally peak around 16:00–17:00 UTC.
- **Robustness reported by source:** the broad time-of-day pattern remains present across market subperiods and in subsets with/without Bitcoin and with/without fiat/stablecoin legs.

### Research-proposed operationalization

To test the return-seasonality claim without inventing a complex strategy:

1. At each UTC hour boundary, classify the next hourly interval solely by clock time.
2. **Long leg:** hold +1 unit exposure during 15:00–16:00 UTC.
3. **Short leg:** hold -1 unit exposure during 01:00–05:00 UTC, evaluated separately from the long leg because shorting is not source-specified.
4. **Optional secondary long leg:** test 21:00–24:00 UTC separately; do not pool it with the primary 15:00–16:00 window unless it adds OOS value.
5. Remain flat outside tested windows.
6. Enter at the start of the designated hour and exit at the end of that hour. This timing convention is **research-proposed**; the paper estimates hourly patterns but does not prescribe order timing.
7. Equal notional exposure across eligible instruments for a cross-sectional panel test; single-instrument tests should be reported separately.

No stop, take-profit, volatility target, leverage multiplier, adaptive sizing rule, or additional indicator filter is source-reported. Adding any such feature would require a separately predeclared research branch.

## Required data

- **Instrument/universe:** crypto spot or spot-like currency pairs. The source uses currency-pair/venue observations; a research replication should define an ex-ante liquid universe and avoid survivorship bias.
- **Venue:** source covers 38 centralized exchanges after quality filtering; portability to Binance or another single venue is unproven until tested.
- **Market type:** source evidence is based on exchange pair data and is not specifically a perpetual-futures study.
- **Timeframe:** hourly.
- **Fields:** OHLC for returns; volume and transaction count if replicating the broader activity/liquidity regime; high/low data are required for the source's Garman-Klass volatility and Corwin-Schultz spread proxies.
- **Point-in-time:** all universe membership and liquidity/quality filters must be constructed without future information. Newly listed/delisted instruments must be handled point-in-time.
- **Timestamp:** UTC, with exact exchange timestamp alignment and daylight-saving-independent UTC boundaries.
- **Missing data:** no silent imputation. Stale, missing, suspended, or malformed hours should be excluded under a predeclared rule.
- **Costs:** maker/taker fees, observed spread where available, slippage, and market impact are required for a trading test. Perpetual implementations additionally require funding and mark/index conventions.

## Execution assumptions

### Source-reported

The source does not specify executable order type, fill model, latency, participation cap, leverage, or trading-cost model because it is a market-microstructure/time-of-day study rather than a strategy backtest.

### Research-proposed

- Signal is known from the UTC clock before the interval begins; no future price information is required.
- Evaluate next-hour open-to-close or boundary-to-boundary returns using strictly causal prices.
- Apply realistic taker-fee plus half-spread/slippage assumptions as a conservative baseline; maker execution may be tested separately but must not be assumed free.
- No leverage in the baseline.
- For short tests, require actual borrow/perpetual short availability and include associated financing/funding costs.
- Reject fills when market data are stale or venue status indicates a trading interruption.

## Evidence

### Source-reported

The source reports the following empirical findings for its 2018-07-01 to 2022-01-01 hourly sample:

- Final panel: 1,940 trading-pair/venue series on 38 exchanges.
- Returns tend to be below average from 01:00–05:00 UTC and peak between 15:00–16:00 UTC; the final three UTC hours also show positive average returns.
- Trading volume, transaction count, volatility, and illiquidity increase through the afternoon and generally peak around 16:00–17:00 UTC.
- The broad intraday patterns remain when the sample is split into different market subperiods and when examining Bitcoin versus non-Bitcoin pairs and fiat/stablecoin versus non-fiat/stablecoin pairs.
- The authors explicitly state that profitability of strategies exploiting these intraday seasonalities has not been established and remains a future-research question.

These are descriptive/source-reported results, not independently verified strategy performance.

### Independently reproduced

not independently reproduced

### Negative evidence

- The paper does not report net trading-strategy profitability, Sharpe ratio, drawdown, or transaction-cost-adjusted returns for the proposed clock-based exposure.
- Return commonality across exchanges is weaker than commonality in volatility, volume, and liquidity, so the return signal may be materially less stable than the activity regime.
- The source sample ends in January 2022, before major later structural changes including U.S. spot Bitcoin ETFs and subsequent market maturation.
- The authors themselves note that profitability of time-of-day-conditioned trading remains unresolved.

## Falsification

1. **Primary OOS test:** use a strictly later sample than 2022-01-01 on liquid crypto pairs. Compare mean 15:00–16:00 UTC return with the unconditional hourly mean. **research-defined falsification threshold:** fail the primary long hypothesis if the OOS difference is non-positive after costs.
2. **Weak-window test:** compare 01:00–05:00 UTC returns with the unconditional hourly mean. **research-defined falsification threshold:** fail the weak-window hypothesis if the OOS mean is not lower than the unconditional hourly mean.
3. **Trading-value test:** evaluate the predeclared long/flat and long/short clock rules after fees, spread, slippage, and where relevant funding. **research-defined falsification threshold:** reject practical alpha if net excess return versus a duration-matched time-shuffled clock placebo is <= 0.
4. **Clock placebo:** circularly shift UTC hour labels independently by day or use randomly selected equal-duration hourly windows. The target windows must outperform the placebo distribution without retuning.
5. **Venue robustness:** test Binance separately and at least one independent high-liquidity venue. If the sign reverses across major venues, treat the global mechanism as weakened.
6. **Regime stability:** split bull, bear, high-volatility, and low-volatility periods using ex-ante rules. Reject a universal-seasonality interpretation if performance is concentrated in one historical regime.
7. **Parameter perturbation:** test adjacent windows (14:00–15:00 and 16:00–17:00 UTC) as sensitivity checks, not as replacement windows chosen after seeing results. If only one narrow historical hour survives and adjacent windows collapse OOS, treat the mechanism as fragile.
8. **Competing explanation:** condition on major U.S./European market opens, macro-announcement times, derivatives settlement/fixing windows, and ETF-related flows where data permit. If the UTC effect disappears after these controls, interpret the clock as a proxy rather than a standalone alpha source.
9. **Capacity/liquidity test:** stress spread and impact specifically around 15:00–17:00 UTC because the source reports high activity but also high illiquidity. Reject implementability if realistic execution costs erase the gross effect.

## Crypto portability

**direct** for the descriptive crypto time-of-day hypothesis because the source itself is a multi-exchange cryptocurrency study.

Portability to current Binance spot is plausible but unproven OOS. Portability to perpetual futures is **adapted**, not direct: funding, mark/index pricing, leverage, liquidations, and derivatives-specific settlement conventions can alter the return pattern. The 24/7 nature of crypto makes UTC definitions stable, but exchange fragmentation, listing turnover, stablecoin quote effects, and venue-specific data quality remain material.

## Limitations

- `not independently reproduced`
- `unproven`: the source documents seasonality but does not demonstrate a profitable strategy.
- `data gap`: no source-reported net-of-cost strategy metrics.
- `data gap`: exact pair-level effect sizes and statistical significance for the proposed trading windows are not summarized as a tradable portfolio result.
- Source data end on 2022-01-01; structural persistence into the ETF era and later market structure must be tested.
- Aggregate equal-weight patterns across many pair/venue observations may not transfer to a single modern exchange.
- The source's exchange-quality filters use historical CoinMarketCap/CoinGecko ratings; reproducing those exact point-in-time ratings may be difficult.
- Return patterns show less cross-venue commonality than volume/volatility/liquidity patterns.
- The proposed long/short implementation is a Scout operationalization, not an author-reported trading rule.

## Implementation status

Not implemented. No PyBroker strategy, Nautilus strategy, registry entry, data-pipeline change, Paper/Testnet/Live workflow, or execution authorization was created in this Scout cycle.

## Adoption boundary

This record is research material only. It is not evidence of validated alpha and does not authorize implementation, paper trading, testnet, or live trading. Any operational rules marked `research-proposed` exist solely to make the source's descriptive claim falsifiable.

## Related Wiki records

- [[quant/bitcoin-intraday-time-series-momentum-volume-session-2026-08-31]] — related intraday horizon but a materially different momentum/volume-session signal rather than deterministic UTC time-of-day seasonality.

No canonical Wiki record with the same DOI or materially identical time-of-day rule was found during the pre-write search.

## Sources

1. Brauneis, A., Mestel, R., Theissen, E. (2024). "The crypto world trades at tea time: intraday evidence from centralized exchanges across the globe." *Review of Quantitative Finance and Accounting*, 64, 275–304 (2025). Published online 10 June 2024. DOI: https://doi.org/10.1007/s11156-024-01304-1. Open-access article: https://link.springer.com/article/10.1007/s11156-024-01304-1.
