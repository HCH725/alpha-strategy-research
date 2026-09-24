---
schema: strategy-research-record-v1
title: TradingView Price-Volume Binary-Entropy Divergence
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-24
sources:
  - https://www.tradingview.com/script/bvYZ1CdF-Bernoulli-Process-Binary-Entropy-Function/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Price-Volume Binary-Entropy Divergence

## Provenance

Public TradingView open-source script: **Bernoulli Process - Binary Entropy Function**, author/page identity `kocurekc`. The page shows original publication `Jul 26, 2020`, a version-2 update `Aug 26, 2022`, and page update `Dec 26, 2024`. Stable source URL: https://www.tradingview.com/script/bvYZ1CdF-Bernoulli-Process-Binary-Entropy-Function/. Source reviewed as of 2026-09-24.

## Economic mechanism

### Source-reported

The source applies a Bernoulli/binary-entropy construction to price and volume separately and describes subtracting the volume-derived entropy measure from the price-derived measure so the resulting histogram can be read in a MACD-like fashion. The author states that shorter settings can expose divergences and specifically suggests that volume may move before price. The page also presents BTC, stock, and forex strategy examples as illustrations, without supplying an auditable performance table in the reviewed text.

### Research interpretation

The falsifiable hypothesis is that **a divergence between binary information states in price and volume contains incremental directional information because participation/volume structure may change before the corresponding price structure changes**. This is materially different from generic return-distribution entropy used only as a tradeability regime gate: the proposed information is the relative state of two observable series, price and volume.

The mechanism is not assumed true. A simpler price-volume momentum or standardized-volume divergence may capture the same information without an entropy transform.

## Signal

Source-supported construction from the reviewed public description:

- Calculate a binary/Bernoulli entropy measurement for price and for volume.
- The author states that price and volume can be plotted separately and that the volume-derived measure can be subtracted from the price-derived measure to create a MACD-like histogram.
- The source says values between roughly 9 and 22 bars have been useful for collecting enough measurements and warns that lengths below 5 run into a Nyquist-frequency issue; these are source-reported guidance, not independently validated optima.
- The source describes an averaging/summation stage and highlighting of an information signal above a stated 5% / two-sigma level, adjustable with a percent-rank variable.
- The source says shorter settings such as 7, 9, and 11 can show histogram divergences.

Materially underspecified from the reviewed public page:

- exact binary event definition for each price and volume observation under every selectable averaging mode;
- exact version-2 default lookback and averaging/summation settings;
- exact formal long/short entry, exit, holding, re-entry, and position-sizing lifecycle for the illustrated strategies;
- exact divergence-detection algorithm and equality/pivot rules;
- whether highlights themselves are intended as executable signals or diagnostics.

No missing trading lifecycle is invented. **Research-proposed operationalization:** first reproduce the source indicator point-in-time, then test whether signed changes/crossings and price-versus-volume entropy spread/divergence predict next-period returns. Any such mapping is research-proposed rather than source-reported.

## Required data

Timestamped price bars and volume. At minimum, a point-in-time price series and corresponding bar volume are needed for the two entropy measurements. The source does not require funding, mark/index/basis data, order book/depth, aggressor-side trades, open interest, or options data.

The page discusses BTC, stocks, and forex examples but does not constrain one venue, market type, or mandatory timeframe. Volume semantics differ materially across venues and asset classes; crypto testing must preserve venue-specific point-in-time volume rather than silently mixing incomparable feeds.

## Execution assumptions

The reviewed public description does not specify a complete executable order lifecycle. Signal-to-order timing, same-bar versus next-bar execution, market/limit order type, commissions, spread, slippage, impact/capacity, leverage/margin, borrow, funding, latency, partial fills, and failures are all unspecified.

Any later backtest must use completed-bar information and an explicitly declared execution model; missing costs must not be interpreted as zero costs.

## Evidence

### Source-reported

The source describes the indicator as a Bernoulli/binary-entropy measure applied to price and volume and states that subtracting volume entropy from price entropy yields a MACD-like histogram. It says shorter settings may expose divergences and presents BTC, stock, and forex strategy examples as illustrations.

No source-reported Sharpe, CAGR, maximum drawdown, win rate, statistically tested alpha, or auditable performance table was identified in the reviewed public page text. Therefore no performance precision is recorded here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself indicates parameter sensitivity: measurement length changes how much information is captured, lengths below 5 are cautioned against, and version 2 added multiple averaging options plus an alternate “purest” binary-entropy equation that the author says is less consistent on direction. The public description does not provide a fully reconstructable trading lifecycle or independent evidence that the entropy transform outperforms simpler price-volume divergence controls.

## Falsification plan

1. Reproduce the public binary-entropy calculations point-in-time from completed bars before evaluating predictive returns; reject any reconstruction that requires future observations.
2. Freeze a small source-supported parameter set before OOS evaluation rather than optimizing across the 9-22 guidance range on the test sample.
3. Compare price-minus-volume binary entropy against simpler controls: price momentum minus volume momentum, standardized volume change, OBV-style price-volume confirmation, and raw up/down proportions without the entropy transform.
4. Test the entropy spread itself, its crossing/turning behavior, and a predeclared divergence rule separately. Do not infer that all visual highlights are equivalent signals.
5. Evaluate chronologically separated OOS samples across trend/range and high/low-volatility regimes, and across multiple liquid crypto instruments/venues where reliable volume exists.
6. Stress fees, spread and slippage under an explicit next-bar execution model for any directional operationalization.
7. Reject or materially weaken the hypothesis if the entropy transform fails to add stable OOS information over simple price-volume controls, if sign/direction is unstable across parameter choices, or if any apparent edge depends on venue-specific volume artifacts.

## Crypto portability

**adapted**

The source explicitly shows a BTC strategy example, so crypto is within the author's intended use, but the reviewed page does not provide auditable crypto performance evidence or a complete crypto execution specification. The hypothesis therefore remains unproven.

Crypto-specific risks include 24/7 sessions, exchange-specific candle boundaries, spot versus perpetual volume differences, venue fragmentation, wash/artificial volume, changing market share across venues, and perpetual funding if a directional perpetual implementation is later tested. Volume must be treated as venue-specific unless an aggregation methodology is explicitly defined.

## Limitations

- Exact version-2 binary-event and averaging equations from source code: not independently reconstructed in this run.
- Trading lifecycle: **underspecified**.
- Divergence algorithm: **underspecified**.
- Cost/fill model: **data gap**.
- Cross-venue volume comparability: **data gap**.
- Crypto profitability evidence: **unproven**.
- Performance: **not independently reproduced**.

## Implementation status

Not implemented in the research stack. No Qlib full backtest, survivor promotion, leaderboard entry, Paper, Testnet, or Live validation is implied.

## Adoption boundary

Research-only. Presence in this repository does not mean the hypothesis passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor, demonstrated profitability, or received implementation/Paper/Testnet/Live approval.

## Related Wiki records

No Wiki Brain lookup or write was performed because this Scout is GitHub-only. No Wiki relationship is asserted. Repository-level comparison families for later research include Shannon/binary entropy, price-volume divergence, information-state regime filters, and volume-confirmation strategies; similarity alone is not adoption evidence.

## Sources

- TradingView — kocurekc, **Bernoulli Process - Binary Entropy Function** (public open-source script; published 2020-07-26; version-2 release 2022-08-26; page updated 2024-12-26; reviewed 2026-09-24): https://www.tradingview.com/script/bvYZ1CdF-Bernoulli-Process-Binary-Entropy-Function/
