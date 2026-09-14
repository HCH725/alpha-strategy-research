---
schema: strategy-research-record-v1
title: "Aggregated Perpetual Open-Interest Expansion + Volume-Delta Conviction Filter"
created: 2026-09-14
updated: 2026-09-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - open-interest
  - volume-delta
  - order-flow
  - momentum
  - market-microstructure
status: research-only
confidence: medium
source_as_of: 2026-09-14
sources:
  - "https://www.tradingview.com/script/IGXOajGL-Aggressive-Order-Flow/"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Aggregated Perpetual Open-Interest Expansion + Volume-Delta Conviction Filter

## Provenance

- **Primary source:** TradingView public open-source indicator, *Aggressive Order Flow*.
- **Author / page identity:** `btcmaxlev`, TradingView.
- **Stable public URL:** https://www.tradingview.com/script/IGXOajGL-Aggressive-Order-Flow/
- **Source page publication label:** TradingView displays `Feb 24`; the captured public page does not expose the year in the retrieved text, so no publication year is inferred here.
- **Source as-of:** 2026-09-14.
- **Public-use status:** TradingView labels the script open-source. This record does not reproduce the Pine source; it only normalizes the publicly described signal logic.
- **Repository deduplication audit:** Existing repository records include (a) `retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11.md`, which reports that one-minute CVD/order-flow momentum and absorption did not survive realistic retail costs, and (b) `crypto-perp-crowded-flush-reversal-microstructure-2026-09-12.md`, which uses falling open interest during sharp price declines to identify forced-deleveraging reversals. This TradingView hypothesis is materially different: it conditions directional order-flow on **aggregate open-interest expansion across multiple perpetual feeds**, treating rising OI plus signed volume delta as evidence of fresh directional commitment rather than liquidation-driven position closure.

## Economic mechanism

### Source-reported

The source describes the indicator as combining aggregated open interest (OI) from up to five user-selected perpetual-futures feeds with per-candle volume delta.

Its interpretation is:

- **OI increasing + positive volume delta:** fresh positioning is entering while aggressive buying dominates; the source labels this bullish conviction.
- **OI increasing + negative volume delta:** fresh positioning is entering while aggressive selling dominates; the source labels this bearish conviction.
- **OI flat or decreasing:** price movement is more likely to reflect existing positions being closed rather than new directional commitment; the source treats this as lower-conviction movement.

The source presents the construction as a directional-bias / order-flow conviction indicator, not as independently validated alpha evidence.

### Research interpretation

The falsifiable hypothesis is that **signed aggressive flow should have more continuation value when it is accompanied by expanding aggregate perpetual open interest than when the same signed flow occurs during flat or declining open interest**.

The proposed causal channel is market-structure based:

1. Positive/negative volume delta identifies the direction of aggressive taker pressure within the candle.
2. Rising aggregate OI suggests that at least part of the move is associated with creation of new derivative exposure rather than only liquidation or position closure.
3. The conjunction may therefore distinguish **fresh directional risk-taking** from mechanically induced or exhaustion-prone price moves.
4. Because OI is aggregated across several perpetual feeds, the signal attempts to reduce single-venue positioning noise and capture market-wide commitment.

This interpretation is not source-proven. Existing repository evidence that standalone CVD/order-flow signals failed after costs is directly relevant negative evidence; the incremental hypothesis is whether OI expansion adds enough conditional information to improve predictive power.

## Signal

**Specification status: underspecified.** The public TradingView description makes the state logic clear but does not expose enough parameter detail in the retrieved page to reconstruct an exact trading strategy without guessing.

### Source-reported state construction

For each chart candle `t`:

1. Select up to five perpetual-futures OI feeds; the source states that a ticker can be set to spot to disable that slot.
2. Sum open interest across active perpetual feeds.
3. Measure whether aggregated OI has increased by more than a user-defined percentage threshold.
4. Compute per-candle volume delta by decomposing lower-timeframe volume into buying and selling pressure.
5. Classify the candle:
   - **Bullish conviction:** aggregated OI increase exceeds threshold **and** net volume delta > 0.
   - **Bearish conviction:** aggregated OI increase exceeds threshold **and** net volume delta < 0.
   - **Low conviction / neutral:** aggregated OI is flat or decreasing.

The source also displays a stat box comparing aggregate OI now versus `N` candles ago, including absolute and percentage change.

### Material underspecification

The retrieved public description does **not** specify:

- the default OI-change threshold;
- whether the conviction-state OI change is strictly one-bar or uses the same configurable `N`-bar comparison shown in the stat box;
- the exact lower timeframe used for volume-delta decomposition;
- the exact buy/sell-volume classification convention;
- chart-bar close versus intrabar signal availability;
- whether higher-timeframe candles can repaint due to lower-timeframe aggregation;
- a trading entry rule, holding period, re-entry rule, stop, target, or position-sizing rule.

Therefore this record does **not** convert the indicator into an invented executable strategy. Any trading implementation would require a separate research specification.

### Research-proposed test signal

For falsification only, a researcher may test the following explicitly as `research-proposed` rather than source-reported:

- At chart-bar close `t`, define bullish state when aggregate OI percentage change over a pre-declared lookback is above a fixed threshold and signed volume delta is positive; bearish state is the mirror image.
- Evaluate next-bar and multi-bar forward returns conditioned on bullish/bearish state versus matched controls with the same signed delta but non-expanding OI.

All lookbacks, thresholds, horizons, and execution choices in such a test must be fixed before evaluation and are not supplied by the TradingView source.

## Required data

### Source-reported

- Up to five user-selected perpetual-futures OI feeds.
- Lower-timeframe volume used to estimate buying versus selling pressure for per-candle volume delta.
- Chart-candle timestamps for state classification.
- Aggregate OI now and historical OI for the comparison window.

### Research-required detail not supplied by source

- **Instrument / universe:** exact perpetual contracts and quote/settlement currencies are user-selected and therefore underspecified.
- **Venue:** source permits multiple perpetual feeds but the public description does not enumerate a required venue set.
- **Timeframe:** chart timeframe and lower timeframe used for delta must be fixed before research.
- **Fields:** OI, OHLCV/trade-volume decomposition, symbol metadata, and timestamps.
- **Point-in-time:** OI publication latency and lower-timeframe volume availability must be lagged according to each venue/feed's actual release timing.
- **Timestamp alignment:** cross-venue OI feeds must be normalized to one clock and candle boundary, preferably UTC for crypto research (`research-proposed`).
- **Missing data:** missing or stale OI from any feed should be flagged, not silently forward-filled (`research-proposed`).
- **Funding / fees / spread:** not part of the indicator logic but mandatory for any tradability test.

## Execution assumptions

The TradingView source is an indicator, not an execution specification.

### Source-reported

- No order type, fill model, latency model, participation cap, leverage, fee schedule, spread, slippage, market-impact model, funding treatment, or failure-handling rule is specified on the reviewed page.
- No explicit entry/exit strategy is supplied.

### Research-proposed

For a causal historical test, form the state only after all constituent OI and lower-timeframe volume data for chart bar `t` are available, then measure or trade from the next eligible bar. This is a research proposal, not source-reported execution behavior.

Any conversion to market orders must include venue-specific taker fees, spread, slippage, and perpetual funding. A passive-maker implementation would require a separate fill-probability/adverse-selection model.

## Evidence

### Source-reported

The TradingView page describes the signal semantics and visualization but provides **no source-reported Sharpe ratio, win rate, CAGR, drawdown, t-statistic, sample period, transaction-cost study, or out-of-sample validation** on the reviewed page.

The source therefore supports only the existence and construction concept of the indicator, not profitability.

### Independently reproduced

not independently reproduced

### Negative evidence

1. `retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11.md` reports that one-minute CVD/order-flow momentum and absorption signals on Binance did not survive an approximately 0.13% round-trip cost; the reported predictable moves were much smaller than costs. This directly weakens any assumption that signed volume delta alone constitutes tradable alpha.
2. The same negative-results study reports no robust edge from spot-perpetual CVD divergence and no robust liquidation-cascade signal across its tested sample.
3. `crypto-perp-crowded-flush-reversal-microstructure-2026-09-12.md` documents a different OI regime: sharp price declines accompanied by **falling** OI can identify forced deleveraging and subsequent reversal. This is not a direct contradiction because the present hypothesis concerns **rising** OI and continuation, but it shows that OI direction changes the economic meaning of order flow and must be modeled explicitly.
4. The TradingView source supplies no empirical evidence that aggregating multiple OI feeds improves forecast accuracy versus single-venue OI or versus volume delta alone.
5. Cross-venue OI aggregation can be mechanically distorted by different contract multipliers, quote currencies, inverse versus linear contracts, exchange reporting conventions, and duplicated economic exposure unless normalized consistently.

## Falsification plan

All thresholds below are `research-defined falsification threshold` unless explicitly marked otherwise.

1. **Incremental-information test versus volume delta alone**
   - **Data:** point-in-time BTC and ETH perpetual OI from at least Binance, Bybit, and OKX plus synchronized trade/volume data.
   - **Sample:** minimum 12 months spanning both high- and low-volatility regimes.
   - **Metric:** out-of-sample predictive regression / classification improvement and net forward-return separation.
   - **Failure rule:** reject the incremental-OI hypothesis if adding normalized aggregate OI expansion fails to improve OOS information coefficient by at least 0.01 **and** fails to improve net Sharpe by at least 0.10 versus signed volume delta alone.
   - **Action:** retain volume delta and OI as descriptive state variables only, not alpha.

2. **Matched-control continuation test**
   - Match candles by asset, volatility, absolute return, and signed delta magnitude.
   - Compare candles with expanding OI versus flat/declining OI.
   - **Failure rule:** reject if forward returns in the delta direction are not statistically larger for expanding-OI states after block-bootstrap confidence intervals and multiple-testing correction.

3. **Direction symmetry test**
   - Test bullish (OI up + delta positive) and bearish (OI up + delta negative) separately.
   - **Failure rule:** if one side is persistently null/negative across both BTC and ETH, restrict or reject the symmetric-conviction interpretation rather than averaging both directions together.

4. **OI aggregation ablation**
   - Compare single-venue OI, raw summed OI, USD-notional-normalized multi-venue OI, and market-share-weighted OI.
   - **Failure rule:** if multi-venue aggregation does not outperform the best single venue out of sample, the cross-venue aggregation claim adds no research value.

5. **Threshold perturbation / overfitting test**
   - Pre-declare a small threshold grid and lower-timeframe delta resolutions using training data only.
   - **Failure rule:** reject if performance exists only at one narrow threshold and disappears under adjacent parameter values or walk-forward evaluation.

6. **Cost and latency stress**
   - Include venue-specific taker fees, half-spread, slippage, funding, and at least one-bar signal-to-order delay.
   - **Failure rule:** reject tradability if net expectancy is non-positive at realistic retail/VIP fee tiers or if edge decays before causal execution.

7. **Placebo test**
   - Randomly permute OI-change labels within volatility/regime blocks while preserving signed volume delta.
   - **Failure rule:** reject if the observed incremental effect does not exceed the 95th percentile of the placebo distribution.

8. **Cross-venue robustness**
   - Re-run on BTC and ETH using Binance-led, Bybit-led, and OKX-led constituent sets.
   - **Failure rule:** reject a universal interpretation if the sign of the effect reverses across major venue configurations.

## Crypto portability

**direct** — the source construction is explicitly based on cryptocurrency perpetual-futures open interest and lower-timeframe volume delta.

Key crypto-specific risks:

- **Perpetual contract heterogeneity:** linear USDT/USDC contracts, coin-margined inverse contracts, and different contract multipliers cannot be naively summed without normalization.
- **Funding:** rising OI may coincide with crowded funding regimes; continuation could be overwhelmed by subsequent liquidation risk.
- **24/7 operation:** no common market close exists, so all cross-venue alignment requires explicit UTC candle boundaries.
- **Venue fragmentation:** one venue can lead positioning changes while another lags, making aggregate OI look smoother but less timely.
- **Exchange reporting differences:** OI units and publication latency differ by venue/feed.
- **Liquidation state dependence:** falling OI during large moves can imply deleveraging/exhaustion rather than conviction; the indicator's neutral treatment of non-expanding OI may hide useful reversal information.

## Limitations

- **underspecified:** the reviewed public page does not expose the default OI threshold, exact OI comparison window for the conviction state, or exact lower-timeframe delta construction.
- **not independently reproduced:** no replication was performed in this Scout cycle.
- **No source-reported performance evidence:** the page describes an indicator, not validated alpha.
- **No execution model:** profitability cannot be inferred from candle colors.
- **Potential aggregation-unit error:** raw OI sums across heterogeneous contracts can be economically meaningless unless normalized.
- **Potential look-ahead / availability risk:** cross-venue OI updates and lower-timeframe volume decomposition must be point-in-time aligned.
- **Publication / selection bias:** a public TradingView script is not a controlled empirical study.
- **Incremental-value burden is high:** existing repository evidence already shows standalone CVD/order-flow signals can fail after realistic costs; the OI conditioning must demonstrate genuine incremental predictive power rather than merely improve narrative coherence.

## Implementation status

`not-implemented`.

No Pine code was copied into the research stack. No PyBroker/Nautilus/runtime strategy was created, no historical backtest was run, and no Paper/Testnet/Live execution was authorized.

## Adoption boundary

This record is research capture only.

Its presence in the repository does **not** mean the indicator is profitable, validated alpha, suitable for implementation, or approved for Paper, Testnet, or Live trading. Any future implementation or adoption requires separate review and independent validation under the current quantitative runtime contract.

## Related Wiki records

No stable Hermes Wiki Brain path was verified for this exact hypothesis during this Scout run, so no Wiki link is fabricated.

Materially related staging-repository records reviewed for deduplication and contradiction context:

- `retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11.md`
- `crypto-perp-crowded-flush-reversal-microstructure-2026-09-12.md`
- `order-flow-imbalance-predictive-decoupling-cost-falsification-2026-09-12.md`
- `crypto-perpetual-order-flow-entropy-microstructure-taker-cost-falsification-2026-09-13.md`

## Sources

1. TradingView, `btcmaxlev`, *Aggressive Order Flow*, public open-source indicator. Stable URL: https://www.tradingview.com/script/IGXOajGL-Aggressive-Order-Flow/ . Page displays publication label `Feb 24`; reviewed 2026-09-14.
2. Repository negative-evidence context: `retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11.md`.
3. Repository related OI/liquidation context: `crypto-perp-crowded-flush-reversal-microstructure-2026-09-12.md`.
