---
schema: strategy-research-record-v1
title: "TradingView BTC RSI(14) + Bollinger Dual-Extreme Mean Reversion"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
  - bitcoin
  - mean-reversion
  - rsi
  - bollinger-bands
status: research-only
confidence: medium
source_as_of: 2026-09-17
sources:
  - https://www.tradingview.com/script/95JBkzXV-BTC-Mean-Reversion-RSI-Bollinger/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView BTC RSI(14) + Bollinger Dual-Extreme Mean Reversion

## Provenance

- **Source type:** public TradingView open-source strategy page.
- **Title:** `BTC Mean Reversion - RSI + Bollinger`.
- **Author:** `connorgeary150`.
- **Stable URL:** https://www.tradingview.com/script/95JBkzXV-BTC-Mean-Reversion-RSI-Bollinger/
- **TradingView page date label:** `Feb 23`; the source-reported test window is explicitly February 16–23, 2026.
- **Source inspected as of:** 2026-09-17.
- The page is marked **OPEN-SOURCE SCRIPT**, but this Scout run normalized only the public TradingView description exposed through web access; the Pine source itself was not copied or independently audited.
- Repository dedup on current `main` found no record containing this TradingView script ID/title/author. The closest repository record, `bollinger-bands_ohlcv-2026-08-31.md`, uses a materially different normalized rule (RSI(9) <= 25, previous bullish candle, previous Bollinger lower-band condition, long-side ATR exits). This record instead preserves a symmetric RSI(14) 30/70 + Bollinger-extreme entry with RSI-50-or-mid-band reversion exits.

## Economic mechanism

### Source-reported

The author describes the system as a BTC mean-reversion strategy. It requires both a momentum extreme (RSI) and a volatility-envelope extreme (price outside a Bollinger Band) before entering, then exits as momentum or price returns toward a neutral/mean state.

### Research interpretation

The falsifiable hypothesis is that a **dual extreme** contains more short-horizon reversal information than either indicator alone: RSI captures directional momentum exhaustion, while a Bollinger-band breach captures distance from a rolling volatility-adjusted center. Requiring both conditions may filter ordinary RSI extremes that occur near the mean and ordinary band breaks that still have strong momentum continuation.

The exit logic is consistent with this thesis: positions are closed once RSI returns through the neutral 50 level or price crosses the Bollinger middle band. This is a mean-reversion hypothesis, not a claim that Bollinger or RSI levels are intrinsically predictive.

## Signal

### Source-reported entry rules

- **Long:** `RSI(14) < 30` **and** price is below the lower Bollinger Band.
- **Short:** `RSI(14) > 70` **and** price is above the upper Bollinger Band.

### Source-reported exit rules

- **Long exit:** if `RSI > 50` **or** price crosses back above the Bollinger middle band.
- **Short exit:** if `RSI < 50` **or** price crosses back below the Bollinger middle band.

### Timing / parameter boundary

- The source reports testing the strategy on **BTCUSD, 10-second bars**.
- RSI lookback (`14`) and thresholds (`30`, `70`, neutral `50`) are source-reported.
- The reviewed TradingView description does **not** state the Bollinger lookback, standard-deviation multiplier, or exact price input. Do not silently assume standard `20, 2.0`; these parameters remain `underspecified` until recovered from the public Pine source.
- The public description does not specify whether signal evaluation is intrabar or only on confirmed bar close, nor whether fills occur on the signal bar or the next bar.
- Holding period is endogenous to the exit conditions; no fixed maximum holding period is stated.
- Re-entry, pyramiding, simultaneous opposite-side orders, position sizing, and leverage are not specified in the reviewed description.
- `research-proposed` causal operationalization for later testing: form the signal only from a completed bar and permit execution no earlier than the next bar. This is not source-reported and must not overwrite the source semantics if the Pine code specifies otherwise.

## Required data

- **Instrument / universe:** BTCUSD in the source-reported test; exact TradingView venue/ticker feed is not stated in the reviewed description.
- **Market type:** `underspecified` (spot, CFD, futures, perpetual, or index-style BTCUSD feed is not identified by the description).
- **Timeframe:** 10-second bars for the source-reported test.
- **Fields:** price bars sufficient to calculate RSI and Bollinger Bands; exact Bollinger source field must be recovered from the Pine source rather than assumed.
- **Derived features:** RSI(14), Bollinger upper/lower/middle bands.
- **Not required by the stated signal:** volume, order book, funding, open interest, basis, or options data.
- **Timestamp / timezone:** 10-second bar ordering is required; the source does not specify timezone/candle-boundary conventions.
- **Point-in-time requirement:** indicator values must use only information available at the signal timestamp; any implementation must avoid intrabar look-ahead when reproducing historical signals.

## Execution assumptions

- Signal-to-order timing: `underspecified`.
- Market vs. limit execution: `underspecified`.
- Fees, spread, slippage, latency and impact: not stated in the reviewed TradingView description.
- At a 10-second horizon, transaction costs and latency are material and must be modeled before interpreting any apparent edge.
- Short-side feasibility depends on the actual BTCUSD instrument. If ported to perpetual futures, funding, mark/index price, leverage and liquidation mechanics become additional assumptions not present in the source description.
- Position sizing and leverage: `underspecified`.

## Evidence

### Source-reported

On the same TradingView page, the author states that the strategy was run on **BTCUSD, 10-second timeframe, February 16–23, 2026**, specifically to obtain at least 500 trades. The source reports:

- **Total trades:** 1,181.
- **Profitable trades:** 710 / 1,181.
- **Reported profitable-trade rate:** approximately 60.1%.

These are third-party source claims from the TradingView page. The reviewed description does not provide a net-return, Sharpe, profit-factor, drawdown, or cost-adjusted result for this strategy, so none is inferred here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The reported sample spans only about one week and therefore does not establish regime robustness.
- The author explicitly says the 10-second setup was used to satisfy a requirement for at least 500 trades; this is a study-design/selection caveat rather than independent evidence of durable alpha.
- No explicit fees, spread, slippage or latency assumptions are reported in the reviewed description, which is especially material at 10-second frequency.
- No independent replication or out-of-sample result was identified in the reviewed TradingView source.

## Falsification plan

1. **Specification recovery:** before implementation, recover the exact Bollinger inputs, Bollinger lookback/multiplier, order timing, pyramiding and sizing semantics from the public Pine source. If these cannot be resolved, retain the record as `underspecified` rather than inventing defaults.
2. **Frozen-rule reproduction:** reproduce the source window on the identified BTCUSD feed if possible, then freeze the recovered rule before any out-of-sample test.
3. **Out-of-sample test:** evaluate later BTC data across trend, crash and range regimes using causal next-bar execution and explicit fees/spread/slippage.
4. **Ablation:** compare the conjunction against RSI-only and Bollinger-only variants. The dual-confirmation hypothesis is materially weakened if it adds no cost-adjusted value over the simpler components.
5. **Direction split:** evaluate long and short legs separately because crypto trend asymmetry and shorting/funding mechanics can make the two sides behave differently.
6. **Failure condition:** reject the alpha hypothesis if the apparent reversal edge disappears after realistic execution costs or fails to outperform its simpler single-indicator baselines out of sample.

## Crypto portability

`direct` for the broad crypto hypothesis because the cited source itself tests BTCUSD.

Portability to a different crypto venue or market type remains `adapted`: Binance spot/perpetuals may differ from the source feed in spread, 24/7 candle boundaries, funding, mark/index behavior, liquidity and short-side mechanics. The source-reported 10-second result must not be treated as evidence for those other implementations without reproduction.

## Limitations

- Bollinger lookback, multiplier and exact input field are `underspecified` in the reviewed description.
- Signal evaluation/fill timing is `underspecified`.
- Exact BTCUSD venue/market type is `underspecified`.
- Reported evidence is a short one-week, high-frequency sample.
- Costs and latency are not reported in the reviewed description.
- Public Pine source was not independently audited in this Scout run.
- Not independently reproduced.
- No profitability or trading approval is implied by inclusion in this repository.

## Implementation status

`not-implemented`.

No PyBroker, Nautilus, paper, testnet or live implementation/validation was performed in this Scout cycle.

## Adoption boundary

Research material only. This record is not evidence of validated alpha and is not approval for implementation, paper trading, testnet or live trading.

## Related Wiki records

No stable Hermes Wiki Brain link was consulted or asserted in this GitHub-only Scout run.

Repository-level adjacent records used only for dedup context:

- `bollinger-bands_ohlcv-2026-08-31.md` — RSI/Bollinger/ATR reversal variant with materially different entry and exit semantics.
- `rsi-mean-reversion_ohlcv-2026-08-31.md` — RSI/VWAP reversal family, different location signal and filters.

## Sources

- https://www.tradingview.com/script/95JBkzXV-BTC-Mean-Reversion-RSI-Bollinger/
