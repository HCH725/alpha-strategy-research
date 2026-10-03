---
schema: strategy-research-record-v1
title: Crypto Donchian Breakout with EMA/RSI/Volume/Volatility Filters
created: 2026-10-03
updated: 2026-10-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-03
sources:
  - https://www.tradingview.com/script/laT8fTXp-Donchian-Breakout-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Donchian Breakout with EMA/RSI/Volume/Volatility Filters

## Provenance

Public TradingView open-source strategy **Donchian Breakout Strategy** by **feliperazeek**, published 2025-04-10. Stable source: https://www.tradingview.com/script/laT8fTXp-Donchian-Breakout-Strategy/ . Source reviewed 2026-10-03. Canonical TradingView script identity: `laT8fTXp`.

The source describes the strategy as a crypto adaptation of Turtle-style Donchian trend following. It explicitly contrasts the classic 20-day entry / 10-day exit, ATR-based sizing and pyramiding framework with this variant's EMA and RSI entry filters, optional volatility and volume filters, ATR stop, commission model, and no pyramiding.

## Economic mechanism

### Source-reported

The author states that the strategy is intended to capture directional crypto trends while reducing false breakouts and chop. The EMA filter aligns entries with trend direction, RSI checks momentum, optional volatility and volume filters screen breakouts, and an ATR stop adapts risk to volatility. The author states that pyramiding is avoided because of crypto reversal risk.

### Research interpretation

The falsifiable hypothesis is not merely that Donchian breakouts trend-follow. It is that conditioning a Donchian breakout on trend alignment and momentum, with optional volatility/volume confirmation, improves out-of-sample breakout quality after costs relative to an otherwise matched raw Donchian breakout.

Component roles:
- Regime / direction: EMA filter.
- Primary signal: Donchian-channel breakout.
- Confirmation: RSI momentum check; optional volatility and volume filters.
- Risk / exit: ATR-based stop rather than relying only on a Donchian reversal.
- Portfolio behavior: no pyramiding.

Each added filter may only reduce trade count without adding information, so its incremental contribution requires ablation.

## Signal

Source-supported rules and parameters:
- The source identifies the classical Turtle reference as a 20-day Donchian breakout entry and 10-day Donchian exit, but does **not** unambiguously state on the retrieved public page that those exact lookbacks are the active defaults of this crypto variant.
- Entry requires a Donchian breakout, with an EMA trend-direction filter and RSI momentum check.
- Optional volatility and volume filters can be enabled to reduce false breakouts.
- Long and short trading can be configured.
- Risk management uses an ATR-based volatility stop.
- Pyramiding is disabled.
- The stop-loss multiplier is configurable.
- The default backtest date window starts 2025-01-01.

Underspecified on the reviewed page:
- active Donchian entry lookback and any Donchian exit lookback;
- EMA length and exact directional inequality;
- RSI length and threshold(s);
- volatility-filter definition and threshold;
- volume-filter lookback and threshold;
- ATR length and default stop multiplier;
- exact signal formation / order-fill timing;
- re-entry and cooldown semantics;
- position sizing for this crypto variant;
- holding-period cap.

Any future concrete choices for those missing items are **research-proposed**, not source-reported.

## Required data

- Crypto OHLCV bars for the tested venue/instrument.
- High/low/close history sufficient for Donchian formation.
- Close history sufficient for EMA and RSI.
- Volume if the optional volume filter is tested.
- OHLC history sufficient for ATR and the optional volatility filter once its exact source definition is resolved.
- Point-in-time requirement: all rolling indicators and breakout boundaries must use only information available at the signal timestamp; a breakout boundary must not include future bars.
- Venue, symbol universe, timeframe, candle timezone/boundaries, and missing-data treatment are **underspecified** on the reviewed page.

## Execution assumptions

The source reports a default commission model of **0.045%**. It does not specify whether that number is charged per side or round trip on the retrieved page.

Order type, same-bar versus next-bar fill, spread, slippage, market impact, partial fills, latency, funding, leverage/margin, liquidation handling, borrow/short constraints, and capacity are **underspecified**.

For causal research, next-bar execution after a fully formed signal is a **research-proposed** baseline and must be tested separately from any TradingView default fill behavior.

## Evidence

### Source-reported

The author qualitatively states that the design is intended for trending coins with strong directional moves and that the filters are intended to avoid chop / weak breakouts. The reviewed page provides no traceable Sharpe, CAGR, drawdown, profit factor, win rate, or comparable performance statistic, so none is recorded here.

The source states a default commission assumption of 0.045% and a default backtest start date of 2025-01-01. These are source configuration claims, not evidence of profitability.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself notes that the design is intended for trending coins, implying vulnerability to sideways/choppy regimes. No independently verified negative result was found in the reviewed source; absence is not evidence of no negative result.

The added EMA/RSI/volume/volatility filters create multiple degrees of freedom and may improve apparent backtests through selection or trade suppression rather than genuine incremental alpha.

## Falsification plan

1. Reconstruct the exact source rules only after all missing active defaults are resolved; otherwise label any test implementation **research-proposed**.
2. Compare the full filtered strategy against an otherwise matched raw Donchian breakout baseline.
3. Ablate EMA, RSI, volatility, and volume filters one at a time and jointly; require improvement to survive reduced trade count rather than relying on in-sample headline return.
4. Compare the ATR stop against a matched Donchian reversal exit while holding entries constant.
5. Test trending, ranging, high-volatility, and low-volatility crypto regimes separately.
6. Use walk-forward / frozen out-of-sample evaluation across multiple liquid crypto instruments and multiple venues where data quality permits.
7. Stress realistic maker/taker fees, spread, slippage and perpetual funding where applicable.
8. Perturb all resolved lookbacks and thresholds; reject an apparent edge that exists only on a narrow parameter island.
9. Audit indicator and channel formation point-in-time to prevent current-bar/future-bar leakage.
10. Materially weaken or reject the incremental-filter hypothesis if the full model fails to outperform the raw Donchian control on out-of-sample risk-adjusted behavior after costs, or if ablation shows no stable contribution from the added filters.

## Crypto portability

**direct**

The source explicitly presents this variant as designed for crypto. Portability is nevertheless venue- and implementation-sensitive because crypto trades 24/7, candle boundaries vary, perpetuals introduce funding and liquidation mechanics, and liquidity/fees differ across venues. The source does not establish that one parameter set transfers across coins, venues, spot and perpetual markets.

## Limitations

- Exact active Donchian, EMA, RSI, volatility, volume and ATR parameters are **underspecified** on the reviewed public page.
- Exact execution timing and order semantics are **underspecified**.
- The source's qualitative rationale is not independent evidence of alpha.
- Optional filters create multiple-testing / tuning risk.
- The source provides no traceable performance table on the reviewed page.
- Not independently reproduced.

## Implementation status

**not-implemented**

This is a research-only normalized external hypothesis. No backtest, runtime implementation, candidate preparation, Qlib execution, or survivor promotion was performed by this Scout.

## Adoption boundary

**not-approved / research-only**

Presence in this repository does not imply Research Intake Review approval, candidate eligibility, Qlib validation, survivor status, Paper/Testnet/Live approval, or authorization to trade.

## Related Wiki records

None asserted. This GitHub-only Scout did not access Hermes Wiki Brain. Repository-adjacent records include `tradingview-btc-donchian-adx-ema200-breakout-continuation-2026-09-16.md`, `tradingview-close-only-donchian-50-trend-following-2026-09-18.md`, and `ensemble-donchian-trend-following-crypto-top20-rotational-2026-09-20.md`; they use materially different signal constructions or research designs.

## Sources

- TradingView, feliperazeek, **Donchian Breakout Strategy**, published 2025-04-10, reviewed 2026-10-03: https://www.tradingview.com/script/laT8fTXp-Donchian-Breakout-Strategy/
