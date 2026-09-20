---
schema: strategy-research-record-v1
title: Bitcoin Coinbase-CME-IBIT Cross-Market Premium Dispersion
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-07-08
sources:
  - https://www.tradingview.com/script/KZj3Pylk-4-diffs-CB-IBIT-Premium/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Coinbase-CME-IBIT Cross-Market Premium Dispersion

## Provenance

Public TradingView open-source script **4 diffs (CB & IBIT Premium)** by `LLVVB`. Stable URL: https://www.tradingview.com/script/KZj3Pylk-4-diffs-CB-IBIT-Premium/. TradingView shows the script updated on 2025-07-08. Source reviewed 2026-09-20.

The source exposes four contemporaneous Bitcoin price differentials: Coinbase spot versus Binance spot; Coinbase spot versus Binance perpetual; Bybit perpetual versus Binance perpetual; and CME futures versus an IBIT-implied Bitcoin value. The author describes these as tools for monitoring spot/perpetual/futures inefficiencies, ETF premium/discounts, arbitrage opportunities, and institutional pricing signals.

## Economic mechanism
### Source-reported

The source presents Coinbase-versus-offshore spot dispersion as a U.S.-versus-offshore market differential, Coinbase spot versus Binance perpetual as spot/perpetual basis relevant to funding or market stress, Bybit versus Binance perpetual as cross-venue derivative pricing dispersion, and CME versus IBIT-implied Bitcoin value as an institutional premium/discount and ETF-arbitrage clue.

### Research interpretation

A falsifiable hypothesis is that **joint dispersion across U.S. spot, offshore spot/perpetual, CME futures, and ETF-implied Bitcoin pricing contains incremental information about temporary segmentation of Bitcoin demand and arbitrage-capital pressure**. If one venue complex leads while related markets lag, subsequent returns may reflect either price discovery/continuation or convergence as arbitrage closes the dislocation.

This is deliberately a cross-market *dispersion and leadership* hypothesis rather than a claim that any single premium is intrinsically bullish or bearish. Competing hypotheses are: (1) U.S./institutional leadership predicts continuation; (2) unusually wide dispersion predicts mean reversion; (3) the spreads contain no incremental information after controlling for ordinary Bitcoin momentum, volatility, funding and trading-session effects.

## Signal

Source-defined observables:

1. Coinbase premium = Coinbase spot price minus Binance spot price.
2. Coinbase spot versus Binance perpetual = price difference between those markets.
3. Bybit versus Binance perpetual = price difference between the two perpetual markets.
4. IBIT premium = CME futures price versus an IBIT-implied Bitcoin value; the source describes the implied value as IBIT ETF price divided by Bitcoin held per share.

The source displays contemporaneous USD differences in a table. It does **not** specify a canonical lookback, normalization window, threshold, entry, exit, holding period, re-entry rule, position sizing, or executable multi-leg strategy. Those elements are underspecified.

Research-proposed operationalization: test each spread separately and a standardized cross-market dispersion vector using strictly point-in-time observations. Compare continuation and convergence labels over multiple forward horizons. Any z-score window, threshold, composite weighting, formation horizon, or trade rule introduced for testing is `research-proposed`, not source-reported.

## Required data

- Bitcoin spot prices from Coinbase and Binance.
- Bitcoin perpetual prices from Binance and Bybit.
- CME Bitcoin futures price corresponding to the source construction.
- IBIT market price plus point-in-time Bitcoin holdings and shares outstanding sufficient to reconstruct the ETF-implied Bitcoin value.
- Synchronized timestamps and explicit market calendars/timezones.
- For controls: Bitcoin OHLCV, volatility, perpetual funding and preferably open interest.
- Point-in-time ETF holdings/share-count data; revised or future-known holdings must not leak into historical formation timestamps.

The source does not specify exact TradingView ticker mappings or the CME contract-roll convention in the reviewed description; these are data gaps that must be resolved before implementation.

## Execution assumptions

No executable order model is source-specified. Same-bar execution, next-bar execution, market/limit choice, fees, spread, slippage, futures roll cost, ETF trading-hours constraints, funding, borrow, latency, partial fills, capacity and hedge ratios are underspecified.

A real relative-value implementation would face non-overlapping market hours: crypto trades continuously, while IBIT and CME have distinct sessions/closures. Research must therefore distinguish a predictive signal measured from synchronized available prices from a supposedly simultaneous arbitrage that may not have been executable.

## Evidence
### Source-reported

The source states the four differentials can be used to monitor price inefficiencies, arbitrage opportunities or institutional pricing signals. It does not report a backtest, Sharpe ratio, CAGR, drawdown, win rate, or other independently auditable performance statistic in the reviewed description.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source provides no demonstrated predictive performance. Several observables may mechanically reflect different trading sessions, contract specifications, ETF NAV/holdings timing, stale prices, stablecoin/USD denomination, or ordinary futures basis rather than exploitable alpha. The IBIT-implied calculation is especially vulnerable to point-in-time holdings/share-count alignment and market-hours artifacts. Absence of a source backtest is not evidence that the hypothesis fails, but it leaves profitability unproven.

## Falsification plan

1. Reconstruct all four spreads with point-in-time data and explicit timestamp/session rules; reject the hypothesis if the apparent effect disappears after stale-price and non-overlapping-hours controls.
2. Run ablations: Bitcoin price momentum/volatility baseline → each individual spread → U.S.-versus-offshore spot spread → spot/perpetual and cross-perpetual spreads → CME/IBIT component → full dispersion vector.
3. Test competing outcomes separately: continuation after venue leadership versus convergence after extreme dispersion. Do not select direction after observing results.
4. Control for funding, open interest, realized volatility, weekday/hour, U.S. cash-session state, CME session/roll, and broad Bitcoin momentum.
5. Use rolling or expanding normalization fitted only on information available at formation time. No full-sample z-scores.
6. Use timestamp-shift and venue-label placebo tests. A genuine cross-market mechanism should degrade when the relevant market alignment is destroyed.
7. Test pre-specified out-of-sample periods and multiple market regimes. Require incremental predictive value beyond the best simpler baseline.
8. Apply realistic costs separately for directional use and any multi-leg convergence implementation, including crypto fees/slippage/funding, CME futures costs/roll, ETF spread/fees and session constraints.
9. Failure criterion: no stable out-of-sample incremental effect after timing controls and costs, or an effect explainable by stale/non-synchronous prices, materially weakens or rejects the hypothesis.

## Crypto portability

direct

The underlying asset is Bitcoin and three of the four differentials directly involve crypto spot or perpetual markets. The CME/IBIT leg introduces traditional-market calendars, ETF structure and futures-contract conventions, so portability is direct at the Bitcoin thesis level but operationally dependent on careful cross-market synchronization.

## Limitations

- Trading logic is underspecified.
- Not independently reproduced.
- Exact ticker mappings and CME roll treatment are not specified in the reviewed source description.
- ETF holdings/share-count timing creates a material point-in-time data risk.
- Non-overlapping 24/7 crypto and traditional-market sessions can create stale-price pseudo-signals.
- A displayed price difference is not proof of executable arbitrage or predictive alpha.
- Stablecoin-versus-USD effects can contaminate Coinbase/Binance comparisons.

## Implementation status

Research-only external material. No implementation or Qlib full backtest has been completed in this research record.

## Adoption boundary

This record has not passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, become a frozen survivor/leaderboard entry, or received Paper, Testnet, or Live approval. It is not evidence of profitability or authorization to trade.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted from this GitHub-only Scout run.

## Sources

- LLVVB, **4 diffs (CB & IBIT Premium)**, TradingView open-source script, updated 2025-07-08: https://www.tradingview.com/script/KZj3Pylk-4-diffs-CB-IBIT-Premium/
