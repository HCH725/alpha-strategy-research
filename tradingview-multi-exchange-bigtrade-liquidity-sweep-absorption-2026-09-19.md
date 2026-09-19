---
schema: strategy-research-record-v1
title: Multi-Exchange Big-Trade Liquidity Sweep and Absorption
created: 2026-09-19
updated: 2026-09-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-19
sources:
  - https://www.tradingview.com/script/LeOOO3Np/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Multi-Exchange Big-Trade Liquidity Sweep and Absorption

## Provenance

- Public TradingView open-source script: `able bigtrades dom + liquidity sweep`.
- Author/page identity: `Able-terminal`.
- Stable public URL: https://www.tradingview.com/script/LeOOO3Np/
- TradingView page displays publication label `Jan 21`; the retrieved public page does not expose a year, so no publication year is inferred.
- Source reviewed as of 2026-09-19.

## Economic mechanism

### Source-reported

The source combines abnormal-volume detection, subsequent price response, prior-high/low liquidity sweeps, and optional multi-exchange crypto volume aggregation. It distinguishes an extreme-volume event that subsequently produces directional price movement (`INIT`) from one where price fails to move (`ABS`). It also identifies sweeps where price trades beyond an old pivot and closes back across that level. For crypto, the page says volume can be aggregated across Binance, Bybit, OKX, Coinbase, and Kraken.

The author presents three use cases: liquidity-sweep reversal confirmed by a large trade, continuation after an initiative event, and fading an absorbed large trade.

### Research interpretation

The falsifiable hypothesis is that **price response conditional on unusually large, cross-venue volume contains more directional information than abnormal volume alone**. A large volume shock followed by displacement may identify initiative order flow and continuation; a large shock without commensurate displacement may identify absorption and subsequent reversal. A pivot sweep that closes back through the swept level supplies an independent market-structure failure condition that may strengthen the reversal case.

This interpretation does not treat `institutional`, `whale`, `stop hunt`, or absorption labels as verified participant identities. They are hypotheses about observable volume-price behavior.

## Signal

Source-supported components:

- Big-trade formation: current volume is standardized relative to recent volume; the page states a 30-bar average is used and describes tiered Z-score significance.
- Initiative/absorption classification: after a Tier-3 event, subsequent price behavior is used to distinguish strong directional movement (`INIT`) from failure to move (`ABS`). The exact response horizon and displacement threshold are not exposed in the retrieved page and are therefore **underspecified**.
- Bullish liquidity sweep: price trades below a prior low and closes back above it, usually with a big-trade confirmation.
- Bearish liquidity sweep: price trades above a prior high and closes back below it, usually with a big-trade confirmation.
- Source-described liquidity-reversal entry: after a bullish sweep plus Tier-2/3 big trade, long when the bar closes back above the sweep level; target is the opposite liquidity high. The symmetric bearish implementation is not explicitly specified on the reviewed page.
- Source-described initiative entry: trade in the initiative direction on a subsequent pullback; exact pullback definition and exit are **underspecified**.
- Source-described absorption entry example: at resistance, after an `ABS` event, short on a break of the absorption candle low; the symmetric long case and exit are **underspecified**.
- The page recommends Sigma 2.5 for volatile markets such as crypto, ATR normalization enabled, and requiring a big trade for sweep filtering. These are source recommendations, not independently validated parameters.

Research-proposed operationalization for later testing: treat the sweep-reversal, initiative-continuation, and absorption-reversal variants as separate hypotheses rather than combining them into one composite trading rule. Any exact response horizon, displacement threshold, pivot definition, symmetric rules, holding period, or exit added during implementation must be explicitly marked `research-proposed` unless recovered from the source.

## Required data

- Crypto instrument OHLCV.
- Historical swing/pivot highs and lows.
- Volume sufficient to compute the source's abnormal-volume standardization.
- For the multi-exchange variant, aligned volume feeds for Binance, Bybit, OKX, Coinbase, and Kraken where available for the same underlying market.
- Timestamp alignment and common bar boundaries across venues are required for aggregation.
- ATR is required if the source-recommended normalization is tested.
- The source's mini-DOM bid/ask and delta display is described as estimated; exact reconstruction requirements are **underspecified** and are not required for the narrower hypotheses above unless later source inspection establishes dependency.
- Point-in-time constraint: pivots, post-event initiative/absorption classification, and multi-venue observations may only become usable after the data required to confirm them exists. No signal may be backdated to the original event bar if its classification requires future bars.

## Execution assumptions

The source gives example entries but does not provide a complete execution model. Fees, spread, slippage, market/limit order choice, fill mechanics, latency, partial fills, funding, leverage, margin, capacity, and shorting assumptions are **underspecified**.

For later research, signal availability must respect bar-close and any post-event confirmation delay. Same-bar fills at information that is only known at the close must not be assumed without an explicit executable model.

## Evidence

### Source-reported

The source qualitatively claims that cross-exchange confirmation makes a big-trade signal more reliable and describes initiative, absorption, and liquidity-sweep interpretations. No traceable Sharpe, CAGR, drawdown, win rate, or other formal performance statistic is reported on the reviewed page, so none is recorded here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No independent negative empirical result was identified in the reviewed source. The participant-identity language is inferential: high standardized volume and low price displacement do not by themselves prove institutional absorption. Multi-exchange aggregation can also be distorted by venue-specific volume definitions, duplicated economic exposure, differing contract types, missing feeds, and bar-boundary mismatch. Absence of cited negative evidence is not evidence of robustness.

## Falsification plan

Test each source-described mechanism separately on point-in-time crypto data:

1. **Abnormal-volume baseline:** future return after a large-volume event with no price-response or sweep conditioning.
2. **Initiative continuation:** compare large-volume events classified as initiative against matched abnormal-volume controls. Falsify the continuation thesis if post-cost OOS directional performance is not materially better than the volume-only baseline.
3. **Absorption reversal:** compare low-displacement extreme-volume events against volume-only and random-event controls. Falsify if reversal performance is absent, unstable, or explained by ordinary short-term mean reversion.
4. **Liquidity sweep:** compare pivot sweep-and-reclaim alone versus sweep + big-trade confirmation. The volume-confirmation component fails if it provides no stable OOS incremental value.
5. **Cross-venue ablation:** compare multi-exchange aggregation with each available single venue and with equalized/matched volume controls. The aggregation thesis fails if cross-venue data does not improve stability or OOS information.
6. **Component ablation:** pivot structure only -> + abnormal volume -> + initiative/absorption classification -> + multi-venue aggregation. Reject unnecessary components that do not add incremental information.
7. **Causality audit:** explicitly model pivot confirmation and post-event classification delays; reject any result dependent on backdating.
8. **Cost sensitivity:** test realistic fees, spread, slippage and funding where applicable, especially on short-horizon variants.
9. **Robustness:** evaluate BTC, ETH and liquid altcoin perpetual/spot markets across volatility, trend and liquidity regimes without selecting parameters on the final OOS sample.

## Crypto portability

direct

The source explicitly includes crypto and describes aggregation across major crypto venues. Portability is nevertheless venue-sensitive because spot and perpetual volumes are not economically identical, 24/7 candle boundaries differ by data vendor, and cross-exchange symbol/contract normalization can create false confirmation.

## Limitations

- Not independently reproduced.
- Exact Tier-2/Tier-3 Z-score thresholds are not fully exposed in the retrieved page.
- Initiative/absorption response horizon and displacement threshold are underspecified.
- Pivot construction details are underspecified.
- Several entry examples lack symmetric rules and complete exits/holding periods.
- Multi-exchange symbol mapping and volume normalization are underspecified.
- `institutional`, `whale`, `absorption`, and `stop hunt` interpretations are not direct participant identification.
- Source publication year is not inferred from the incomplete public date label.

## Implementation status

No implementation in the research stack has been completed. No backtest, PyBroker/Nautilus validation, paper trading, testnet, or live verification is claimed.

## Adoption boundary

Research material only. Presence in this repository does not imply profitability, validated alpha, implementation approval, paper/testnet approval, or live-trading approval.

## Related Wiki records

None linked; no stable Hermes Wiki Brain page was established during this GitHub-only Scout run.

## Sources

- TradingView — Able-terminal, `able bigtrades dom + liquidity sweep`: https://www.tradingview.com/script/LeOOO3Np/ (reviewed 2026-09-19).
