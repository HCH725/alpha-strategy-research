---
schema: strategy-research-record-v1
title: Coinbase-Spot vs Binance-Perpetual Premium ROC Leadership
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-20
sources:
  - https://www.tradingview.com/script/IcGFifsn-Spot-Premium-with-ROC/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Coinbase-Spot vs Binance-Perpetual Premium ROC Leadership

## Provenance

Public TradingView open-source indicator **Spot Premium with ROC** by `Leo_DC13`, published 2025-04-23 and updated 2025-08-14. Stable source: https://www.tradingview.com/script/IcGFifsn-Spot-Premium-with-ROC/ . Source reviewed as of 2026-09-20.

The source compares Coinbase BTC spot with Binance BTC perpetual pricing and adds rate-of-change (ROC) of that premium. Repository deduplication on current `main` found no record for this canonical TradingView source. Existing basis/premium records are related but materially distinct: this hypothesis focuses on the **velocity of a cross-venue spot-versus-perpetual premium**, not merely its level or a same-venue spot/perpetual basis.

## Economic mechanism

### Source-reported

The source describes the histogram as spot premium, using Coinbase spot relative to Binance perpetual price. Positive premium means spot is above the perpetual; negative premium means the perpetual carries a premium. It states that the ROC line measures how quickly this premium changes and may be normalized for stability. The author presents sustained positive premium as a possible bullish-sentiment signal, large divergences as possible arbitrage information, and premium behavior as potentially informative about funding pressure.

### Research interpretation

Hypothesis: **the change rate of the Coinbase-spot minus Binance-perpetual premium contains incremental information about short-horizon price leadership and positioning stress beyond the premium level itself.** A rapid increase in spot premium may indicate US spot demand leading leveraged offshore derivatives, while a rapid deterioration may indicate derivatives-led demand or spot weakness.

This is not assumed to be directional alpha. Competing hypotheses must be tested:

1. **Leadership continuation:** positive premium ROC predicts positive subsequent BTC returns, and negative ROC predicts negative returns.
2. **Dislocation mean reversion:** extreme premium ROC predicts convergence of the cross-market spread without useful directional BTC return information.
3. **Stress/volatility only:** extreme ROC predicts higher subsequent volatility but no stable return direction.

## Signal

Source-specified elements:

- Compare BTC spot on Coinbase with BTC perpetual futures on Binance.
- Spot-premium histogram is described as `spot - perp`; positive values mean spot trades above perp and negative values mean perp trades above spot.
- Compute a ROC line on the premium to measure how quickly the premium changes.
- The source offers an option to normalize ROC fluctuations for greater stability.

The reviewed source page does not unambiguously expose the exact ROC lookback, normalization formula/settings, canonical threshold, entry, exit, holding period, re-entry, position sizing, stop, or take-profit. These are `underspecified` and must not be invented.

Research-proposed operationalization for falsification only: compute a point-in-time premium series from synchronized Coinbase spot and Binance perpetual prices, then evaluate lagged premium change/ROC continuously before testing any rolling percentile event definition. Any lookback, smoothing, z-score, threshold or holding horizon introduced during research must be labeled `research-proposed` and estimated from past data only.

## Required data

- BTC spot prices from Coinbase.
- BTC perpetual-futures prices from Binance.
- Synchronized timestamps and identical bar boundaries across venues.
- OHLCV for the response instrument used to measure subsequent returns.
- Point-in-time symbol/contract metadata and venue availability.
- Funding rate, open interest, realized volatility and volume for controls where available.
- Explicit handling of USD versus stablecoin quotation differences, feed gaps, stale observations and exchange outages.

## Execution assumptions

The source is an indicator, not a complete executable strategy. Signal-to-order timing, order type, fill model, fees, spread, slippage, impact, funding, leverage, margin, latency, partial fills and failures are not specified.

For research, only completed information available at the signal timestamp may be used; a directional trade may execute no earlier than the next executable observation. Cross-venue arbitrage interpretation additionally requires modeling transfer/hedging constraints and venue-specific costs rather than assuming frictionless convergence.

## Evidence

### Source-reported

The source explains the premium and ROC construction and lists possible sentiment, arbitrage, risk-management and funding-related uses. It reports no independently audited backtest, Sharpe ratio, CAGR, drawdown, win rate or other strategy-performance statistic.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No direct negative empirical result is reported on the reviewed source page. Mechanically, the cross-venue spread can reflect quote-currency differences, venue microstructure, latency, stale bars or temporary feed problems rather than economically meaningful leadership. ROC can amplify noise, especially when calculated over short horizons. Absence of source-reported negative evidence is not evidence of no negative result.

## Falsification plan

1. Reconstruct synchronized Coinbase-spot and Binance-perpetual premium point-in-time; audit timestamp alignment and stale-feed behavior before testing predictability.
2. Test premium level and premium ROC as continuous variables before choosing thresholds.
3. Compare three outcomes: directional continuation, spread convergence/mean reversion, and volatility-only response.
4. Ablate `price momentum -> premium level -> premium ROC -> level x ROC interaction`. Reject the incremental hypothesis if ROC adds no out-of-sample information beyond premium level and ordinary price momentum.
5. Control for Binance funding, OI change, realized volatility, volume shocks and contemporaneous BTC return. Reject a distinct leadership interpretation if ROC merely relabels these states.
6. Compare raw dollar spread with percentage-normalized spread and leakage-safe rolling normalization. A result that depends on arbitrary price-scale treatment is weak evidence.
7. Run timestamp-shift/placebo tests and matched-volatility event controls; real premium ROC should outperform mechanically misaligned or randomized variants.
8. Test bull, bear, high-volatility and low-volatility regimes separately and require walk-forward/out-of-sample stability.
9. Stress venue outages, stablecoin/USD dislocations and missing observations. Exclude periods where the spread cannot be formed from contemporaneous executable prices.
10. Apply realistic fees, spread, slippage and funding to any trading operationalization. For convergence trades, model both legs and venue-specific execution rather than assuming costless arbitrage.

## Crypto portability

`direct`

The source itself is Bitcoin/crypto-specific. Portability to ETH or other assets is unproven and requires equivalent liquid Coinbase spot and Binance perpetual markets. Venue fragmentation, 24/7 trading, stablecoin/USD basis, funding, contract specification and changing venue market share are material risks.

## Limitations

- `underspecified`: exact ROC lookback, normalization, thresholds and trading rules are not fully exposed in the reviewed source description.
- `not independently reproduced`.
- Cross-venue premium may include quote-currency and venue-specific effects unrelated to directional alpha.
- ROC may amplify microstructure noise and stale-price artifacts.
- TradingView feed semantics and historical availability require audit before implementation.
- Source interpretations are hypotheses, not verified causal evidence.

## Implementation status

Research record only. No implementation, backtest, robustness campaign, paper trading, testnet or live validation has been completed in our research stack.

## Adoption boundary

`research-only / not-implemented / not-approved`.

Presence in this repository does not imply Research Intake Review passage, production-candidate admission, Qlib validation, profitability, validated alpha, survivor status, implementation approval, paper-trading approval, testnet approval or live-trading approval.

## Related Wiki records

No stable Hermes Wiki Brain links are asserted from this GitHub-only Scout run.

Repository-relative conceptual neighbors include the existing spot/perpetual basis and premium-leadership research records; this record is differentiated by cross-venue Coinbase-spot/Binance-perpetual **premium velocity (ROC)**.

## Sources

- TradingView — **Spot Premium with ROC**, `Leo_DC13`, published 2025-04-23, updated 2025-08-14, reviewed 2026-09-20: https://www.tradingview.com/script/IcGFifsn-Spot-Premium-with-ROC/
