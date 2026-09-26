---
schema: strategy-research-record-v1
title: TradingView Liquidity Sweep with Lower-Timeframe Delta Absorption
created: 2026-09-27
updated: 2026-09-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-27
sources:
  - https://www.tradingview.com/script/OvE4qQgh-Liquidity-Sweep-Delta-Absorption-PineGen-AI/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Liquidity Sweep with Lower-Timeframe Delta Absorption

## Provenance

Public TradingView open-source strategy `Liquidity Sweep + Delta Absorption [PineGen AI]` by `PinegenAI`. Stable source: https://www.tradingview.com/script/OvE4qQgh-Liquidity-Sweep-Delta-Absorption-PineGen-AI/ . Source reviewed 2026-09-27. The page was published two days before this review.

## Economic mechanism

### Source-reported

The author frames the setup as failed breakout / liquidity-sweep absorption. A confirmed swing high or low is pierced by the bar wick, but the bar closes back inside the level. The same bar must show elevated volume, a close displaced toward the opposite side of its range, and a lower-timeframe volume-delta proxy leaning against the sweep. The claimed interpretation is that aggressive orders beyond the swing level were absorbed rather than initiating continuation.

### Research interpretation

This is a falsifiable short-horizon mean-reversion hypothesis: a failed excursion through a previously confirmed pivot may carry more reversal information when participation is elevated and intrabar volume imbalance opposes the excursion. Component roles are: confirmed pivot = liquidity/reference level; wick-through plus close-back-inside = primary failed-breakout signal; volume and lower-timeframe delta = absorption confirmation; optional EMA/session/one-bar confirmation = filters; ATR stop, reward:risk target, and daily trade cap = risk/execution controls rather than alpha.

The delta input is explicitly a proxy derived from lower-timeframe up/down volume, not exchange-native bid/ask aggressor flow. Tests must not reinterpret it as true order-flow delta.

## Signal

- Formation: evaluate only on confirmed bars; pivot levels update only after a swing is fully confirmed.
- Reference level: most recently confirmed swing high and swing low using TradingView pivot logic.
- Bullish setup: price wick pierces the confirmed swing low and closes back inside; the sweep bar must also satisfy above-average volume, close-location, and lower-timeframe delta conditions leaning against the downside sweep.
- Bearish setup: symmetric logic around a confirmed swing high.
- Optional filters: one-bar confirmation, EMA trend filter, and adjustable session window. The source states the session default is 09:30–12:00 ET.
- Long and short directions can be enabled independently.
- Risk/exit: ATR-buffered stop beyond the sweep wick and configurable reward:risk target.
- Activity control: configurable daily trade cap.
- The exact pivot lookback default, volume-average window/threshold, close-location threshold, delta construction algebra/threshold, EMA parameters, ATR buffer, reward:risk default, daily cap default, and one-bar confirmation rule are **underspecified** in the reviewed public description. They must not be silently filled. Any later Scout-chosen operationalization is **research-proposed**.

## Required data

- OHLCV for the parent chart instrument.
- Parent timeframe; the source-reported example uses BTCUSDT 2h.
- Lower-timeframe OHLCV/volume data for the delta proxy; the lower timeframe must be smaller than the parent timeframe.
- Confirmed pivot state with causal availability enforced.
- Timestamp/timezone data sufficient to reproduce the optional ET session window.
- Venue and BTCUSDT market type (spot/perpetual) are not stated in the reviewed description: **data gap**.
- Point-in-time constraint: no pivot or lower-timeframe information may be used before it is available on the confirmed parent bar.

## Execution assumptions

The source states signals are evaluated on confirmed bars and reports a backtest using 0.02% commission and 2-tick slippage. It does not unambiguously specify same-close versus next-bar order timing, market/limit order semantics, spread, impact/capacity, partial fills, latency, venue, funding, leverage/margin, or perpetual-contract assumptions. These are **underspecified** and must be modeled explicitly in later research rather than inferred.

## Evidence

### Source-reported

For BTCUSDT on a 2h chart from 2022-01-01 through 2026-09-19, using what the author calls default settings, $10,000 initial capital, 10% of equity per trade, 0.02% commission, and 2-tick slippage, the page reports net profit +$568.41 (+5.68%), maximum drawdown $211.64 (2.02%), win rate 47.83% (11/23 trades), and profit factor 2.23. The author explicitly notes that 23 trades over roughly 4.7 years is a small sample and insufficient for strong conclusions about edge.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself flags the very small trade count. The default session is described as tuned for US index/futures and FX/gold day trading despite the displayed BTCUSDT backtest, creating a portability/session-selection concern. No independent evidence was identified in the reviewed source.

## Falsification plan

1. Reproduce the source logic causally, preserving confirmed-pivot timing and lower-timeframe availability.
2. Compare the full rule against a plain pivot sweep-and-reclaim baseline.
3. Ablate elevated volume, close-location, and lower-timeframe delta separately and jointly to determine whether the claimed absorption confirmation adds information.
4. Compare the lower-timeframe delta proxy with simpler parent-bar volume/direction proxies; where true aggressor-side trade data is available, compare against actual signed flow.
5. Test with and without the EMA, session, and one-bar confirmation filters so filter selection is not mistaken for core alpha.
6. Run broad parameter neighborhoods rather than optimizing a single pivot/volume/delta setting.
7. Require genuinely held-out chronological samples and multiple liquid crypto instruments/timeframes.
8. Apply realistic fee, spread, slippage and, for perpetuals, funding assumptions.
9. A **research-defined falsification threshold** is failure of the full absorption-conditioned signal to outperform the matched plain sweep/reclaim baseline after costs on held-out data with stable direction across major parameter neighborhoods.

## Crypto portability

direct

The cited source itself reports a BTCUSDT 2h backtest, so the hypothesis is directly demonstrated by the source in a crypto-labelled market. However, venue and spot-versus-perpetual identity are not stated. Crypto replication must therefore resolve market type, funding where applicable, 24/7 candle/session boundaries, venue fragmentation, tick size, and whether retaining a US-session filter is economically defensible.

## Limitations

- Not independently reproduced.
- Small source-reported sample: 23 trades.
- Exact delta-proxy algebra and several thresholds/defaults are **underspecified**.
- Venue and market type are a **data gap**.
- Lower-timeframe delta is not true exchange bid/ask tape.
- Session selection may be tuned to non-crypto market hours.
- Source-reported performance is not evidence of validated alpha.

## Implementation status

Research-only normalization. No implementation in the research stack and no Qlib full backtest has been completed.

## Adoption boundary

This record is research material only. Presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, is profitable or validated alpha, or is approved for implementation, Paper, Testnet, or Live trading.

## Related Wiki records

No canonical Wiki link is asserted from this GitHub-only Scout cycle.

## Sources

- TradingView, PinegenAI, `Liquidity Sweep + Delta Absorption [PineGen AI]`: https://www.tradingview.com/script/OvE4qQgh-Liquidity-Sweep-Delta-Absorption-PineGen-AI/ (reviewed 2026-09-27).
