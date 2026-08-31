---
schema: strategy-research-record-v1
title: Bitcoin Turn-of-15-Minute-Candle Intraday Seasonality
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - bitcoin
  - intraday
  - seasonality
  - microstructure
status: research-only
confidence: medium
source_as_of: 2023-03-02
sources:
  - https://doi.org/10.1016/j.heliyon.2023.e14236
  - https://pubmed.ncbi.nlm.nih.gov/36938429/
  - https://research.lut.fi/converis/portal/detail/Publication/23546543
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Turn-of-15-Minute-Candle Intraday Seasonality

## Provenance

Primary source: Shanaev, Savva; Vasenin, Mikhail; Stepanov, Roman, **“Turn-of-the-candle effect in bitcoin returns,”** *Heliyon* 9(3), e14236, published online 2023-03-02. DOI: `10.1016/j.heliyon.2023.e14236`.

The paper is peer-reviewed and open access. It studies one-minute Bitcoin returns across seven exchanges and reports a recurring return concentration at the turns of 15-minute candles. The reported anomaly is strongest and most consistent in 2021, with an out-of-sample check covering January-August 2022.

This record is a normalized research capture only. It does not claim that the effect persists in current markets or on Binance specifically.

## Economic mechanism

### Source-reported

The authors report that positive Bitcoin returns are disproportionately concentrated in the minutes corresponding to the starts of 15-minute candles: minute labels 0, 15, 30, and 45 of each hour. They find little evidence for a 10-minute cycle, argue that Bitcoin block timing is therefore unlikely to explain the pattern, and suggest that high-frequency algorithmic trading reacting to 15-minute candle information is a plausible explanation.

The paper also frames the anomaly as consistent with adaptive market efficiency because it appears only in later sample years rather than being stable throughout Bitcoin history.

### Research interpretation

The falsifiable hypothesis is that synchronized attention and order submission around widely used 15-minute bar boundaries creates a short-lived recurring imbalance in aggressive demand versus supply. If this mechanism is real, average returns during the boundary-associated one-minute intervals should exceed returns during non-boundary minutes after realistic spread, fee, latency, and adverse-selection costs.

This is a market-microstructure/clock-time seasonal effect, not a directional forecast derived from RSI, moving averages, momentum ranking, or funding/basis.

## Signal

Source-supported normalized rule:

1. Instrument: Bitcoin spot on a specific exchange.
2. Sampling frequency: one-minute returns.
3. Identify one-minute observations whose minute-of-hour label is `00`, `15`, `30`, or `45`.
4. Hold long Bitcoin exposure only for those turn-of-the-15-minute-candle observations; remain out of Bitcoin during other one-minute observations.
5. Repeat each hour.

Pseudocode representation of the source claim:

```text
for each 1-minute observation t:
    if minute_of_hour(t) in {0, 15, 30, 45}:
        target_exposure = long BTC
    else:
        target_exposure = flat
```

**Underspecified execution detail:** the accessible paper text states that the strategy “holds Bitcoin ... at the turns of the candle” and evaluates one-minute returns associated with those minute labels, but does not unambiguously specify in order-book terms whether the executable trade is entered exactly at the start of the labeled minute and exited at its end, or uses another close-to-close convention. That timing must be verified from the full methods/code before implementation. No alternative timing rule is invented here.

No short leg is source-supported in this record.

## Required data

- Instrument: BTC spot pair corresponding to the tested venue.
- Venues in the source include Bitfinex, Bittrex, Binance, Gemini, KuCoin, Bitstamp, and FTX over their available histories.
- Timeframe: one-minute.
- Fields: timestamp and one-minute price series sufficient to reproduce one-minute returns; bid/ask spread data is additionally required for executable testing.
- Timestamp: exact exchange timestamp convention is required; candle-boundary alignment must be consistent with the source and venue.
- Point-in-time: no look-ahead is required for the clock-time signal itself, but the executable entry timestamp must precede the return interval being harvested.
- Fees: venue-specific maker/taker schedule or historical effective fees.
- Spread: contemporaneous bid-ask spread or a conservative point-in-time proxy.
- Missing data: gaps around boundary minutes should not be silently imputed.

## Execution assumptions

The source simulation uses Bitfinex 2021 and explicitly models the Bitfinex fee schedule, simulated rolling 30-day strategy volume, and Bitfinex-specific bid-ask spread data from Bitcoinity. The source reports that high turnover makes fees initially prohibitive and that economics change materially as rolling volume lowers fees.

For independent reproduction, execution must model:

- four entry/exit cycles per hour if exposure is limited to one boundary minute;
- exchange-specific taker/maker fees;
- bid-ask spread on both entry and exit;
- latency around exact candle boundaries;
- partial fills and queue position if limit orders are considered;
- market impact at realistic size;
- whether historical zero-fee/high-volume tiers are still attainable and comparable.

The source does not establish modern execution feasibility on Binance or perpetual futures. Funding is irrelevant for the original spot implementation but would matter for a perpetual adaptation.

## Evidence

### Source-reported

The paper reports average turn-of-candle returns of about **0.58 basis points per minute** across the examined exchanges in its highlighted 2021 results, while average returns during other minutes are negative. The 2021 effect is reported as statistically strong across all seven sample exchanges, with t-statistics above nine in the paper’s discussion.

For a Bitfinex 2021 trading simulation, the paper reports that after both fees and bid-ask spreads a starting capital of **$5,000** produced **74.18% net return**, compared with **60.27%** for buy-and-hold. The paper’s Table 5 reports strong sensitivity to starting capital because the historical rolling-volume fee schedule materially changes transaction costs.

The paper also reports out-of-sample persistence for Bitfinex during **January-August 2022**, though at a lower magnitude than 2021.

These are source-reported results and have not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The paper itself provides important fragility evidence:

- the anomaly is not stable across the full historical sample and was absent in the earlier Bitcoin years;
- it emerges only later and becomes broadly consistent across exchanges around 2020-2021, implying regime dependence;
- high transaction fees can make the high-turnover strategy economically infeasible at lower capital/volume tiers;
- the 2022 out-of-sample effect is weaker than the 2021 in-sample effect;
- the proposed algorithmic-trading mechanism is plausible but not causally established.

The effect therefore should not be treated as a timeless calendar premium.

## Falsification plan

A modern test should reject or materially downgrade the hypothesis if any of the following hold:

1. Boundary-minute mean returns at `00/15/30/45` are not positive and statistically distinguishable from non-boundary minutes in a recent out-of-sample period.
2. The effect disappears after controlling for exchange timestamp alignment, stale prices, bad prints, and data-source artifacts.
3. Net performance is non-positive after realistic current fees, two-sided spread, latency, and slippage.
4. The effect is concentrated in one venue or one short regime and fails on independent major venues.
5. A placebo test on shifted minute sets (for example `01/16/31/46`) performs similarly, weakening the candle-boundary interpretation.
6. The effect does not survive post-2022 data, indicating decay after publication or market adaptation.
7. Entry/exit timing reconstructed from the source cannot be executed without using information from the same bar that would create look-ahead.

Failure should leave the record as negative/decayed research evidence rather than trigger parameter mining for a nearby minute pattern.

## Crypto portability

**Direct** for Bitcoin spot venues that support correctly aligned one-minute data and sufficiently low execution costs.

**Adapted / unproven** for:

- BTC perpetual futures, where funding, mark/index mechanics, leverage, and derivatives-specific microstructure differ;
- other cryptocurrencies, because the paper does not establish cross-asset portability;
- other candle intervals such as 5-minute, 30-minute, or 1-hour boundaries.

Crypto-specific risks include 24/7 clocks, venue-specific candle construction, UTC versus exchange timestamp conventions, fragmentation across venues, fee-tier changes, and the possibility that widespread algorithmic adoption arbitrages away a clock-time anomaly.

## Limitations

- **Not independently reproduced.**
- **Underspecified:** exact executable order timestamp/price convention for each labeled one-minute return must be confirmed before implementation.
- **Regime-sensitive:** the anomaly was not present throughout Bitcoin history.
- Historical Bitfinex fee tiers and market structure may not match current venues.
- FTX is no longer an executable venue, so its historical evidence is replication evidence only.
- The source’s causal explanation involving high-frequency algorithms is suggestive, not proven.
- Publication and discovery can induce post-publication decay.
- High turnover makes cost assumptions first-order rather than secondary.

## Implementation status

Not implemented in the research stack. No PyBroker, NautilusTrader, paper, testnet, or live reproduction has been performed.

## Adoption boundary

This record is `research-only` and `not-approved`. It is not evidence that the strategy is currently profitable, executable, suitable for leverage, or approved for implementation, Paper, Testnet, or Live trading.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted in this Scout cycle. Related strategy-pool material includes the separate Bitcoin intraday time-series-momentum record, but the mechanisms and signals are materially different: this record is deterministic clock-time seasonality around 15-minute candle boundaries rather than return-conditioned intraday momentum.

## Sources

1. Shanaev, S., Vasenin, M., & Stepanov, R. (2023). “Turn-of-the-candle effect in bitcoin returns.” *Heliyon*, 9(3), e14236. DOI: https://doi.org/10.1016/j.heliyon.2023.e14236
2. PubMed record, PMID 36938429: https://pubmed.ncbi.nlm.nih.gov/36938429/
3. LUT University research portal publication record: https://research.lut.fi/converis/portal/detail/Publication/23546543
