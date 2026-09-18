---
schema: strategy-research-record-v1
title: "TradingView Heikin-Ashi Wickless Acceleration + ADX Scalper"
created: 2026-09-18
updated: 2026-09-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-18
sources:
  - https://www.tradingview.com/script/d7hoosSf-1-Min-Rapid-Scalper/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Heikin-Ashi Wickless Acceleration + ADX Scalper

## Provenance

Public TradingView open-source strategy **1-Min Rapid Scalper**, author `BVLabs`. Stable URL: https://www.tradingview.com/script/d7hoosSf-1-Min-Rapid-Scalper/. The public page shows an initial `Apr 10` label and an update/release note dated `08/10/2026`; source reviewed 2026-09-18. The year of the initial Apr 10 publication label is not independently inferred here.

GitHub dedup on current `main` found no record containing canonical TradingView script ID `d7hoosSf`. Search for the normalized Heikin-Ashi wickless/ADX construction also found no materially same signal. Existing Heikin-Ashi records use different primary signal constructions, including Supertrend and moving-average crossover logic.

## Economic mechanism

### Source-reported

The author describes a short-horizon momentum sequence: a directional Heikin-Ashi color flip is followed by three consecutive wickless candles whose bodies expand sequentially. ADX must exceed a configurable threshold. The source interprets the sequence as fresh directional conviction rather than late-stage continuation and is designed primarily for one-minute impulse capture.

### Research interpretation

The falsifiable hypothesis is that a **fresh regime reversal followed by three bars of increasingly strong one-sided synthetic-candle morphology** identifies unusually concentrated short-horizon directional pressure, and that requiring elevated ADX removes weak/choppy occurrences. Component roles are:

- Regime initiation: opposite-color Heikin-Ashi bar four bars back.
- Primary signal: three consecutive same-direction wickless Heikin-Ashi candles with strictly increasing body size.
- Confirmation: ADX above a configurable threshold on the signal bar.
- Exit/risk: either a one-bar impulse exit or an ATR-based TP/SL with a percentage hard-cap stop.

The predictive claim belongs to the morphology sequence plus ADX gate; ATR and percentage stops are risk management and must not be counted as alpha without ablation evidence.

## Signal

Source-reported normalized logic:

- **Signal source:** true Heikin-Ashi values obtained through TradingView's Heikin-Ashi ticker/request mechanism rather than an approximate visual transformation.
- **Long setup:** the fourth lookback bar is bearish; the following three Heikin-Ashi bars are bullish-side wickless (`HA open = HA low`) and each body is strictly larger than the preceding body's size; ADX exceeds the configured threshold on the signal bar.
- **Short setup:** mirror image: the fourth lookback bar is bullish; the following three bars are bearish-side wickless (`HA open = HA high`) with strictly increasing body size; ADX exceeds threshold.
- **Formation timing:** conditions are evaluated on confirmed bars; the source states no repainting.
- **Entry:** order is placed for the open immediately following the signal bar.
- **Default exit:** a close command issued on the entry bar executes at the next bar open because `process_orders_on_close = false`, producing approximately one bar of exposure.
- **Alternative ATR mode:** TP and SL are fixed from the entry price using the prior bar's ATR and are not recalculated during the trade. A fixed-percentage "Plug" stop selects the tighter loss cap.
- **Primary timeframe:** 1 minute. Source says the construction can be used on liquid forex, crypto, equity futures and indices.

The public prose reviewed does not expose the exact ADX/DMI length and threshold defaults, ATR length/multipliers, Plug percentage, TP multiple, position sizing, pyramiding/re-entry behavior, or exact equality/tick-tolerance handling for the wickless condition. These are **underspecified** and are not invented here.

## Required data

Timestamped standard OHLC bars are required to derive causal Heikin-Ashi OHLC. ADX/DMI and ATR require sufficient OHLC history. No volume, funding, basis, open interest, trade-flow or order-book field is part of the stated signal.

The intended horizon is one minute, making exact timestamp/candle-boundary semantics material. Heikin-Ashi values must be formed only from completed information available at each signal timestamp. A reproduction must also preserve the source's confirmed-bar signal and next-bar-open execution separation.

## Execution assumptions

The source explicitly states next-bar-open entry after a confirmed signal. In default mode, the close instruction is issued on the entry bar and executes at the following bar open with `process_orders_on_close = false`. In ATR mode, stop/target levels use prior-bar ATR and are locked after position opening; the percentage Plug caps stop distance.

The reviewed source does not specify commission, spread, slippage, market/limit order type beyond TradingView strategy-order semantics, latency, impact/capacity, leverage/margin, funding/borrow, partial fills or failures. These omissions are especially material at one-minute frequency. Any economic test must stress realistic round-trip costs and next-bar-open gaps rather than assuming frictionless fills.

## Evidence

### Source-reported

The source presents the construction as designed for ultra-short impulse capture and recommends the one-bar mode for tight-spread, fast-fill instruments and ATR mode for wider intrabar volatility. The reviewed page does not provide a traceable Sharpe ratio, CAGR, drawdown, win rate or other quantitative performance statistic adopted by this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No independent negative study was identified in the reviewed source. The strategy's one-minute horizon creates obvious cost, latency and fill sensitivity, while exact wickless equality on synthetic Heikin-Ashi values may be implementation-sensitive. The author's claim that wickless sequences reflect directional pressure is a hypothesis, not independently verified order-flow evidence. Absence of additional negative evidence is not evidence of robustness.

## Falsification plan

1. Recover the exact public Pine defaults before claiming exact reproduction; unresolved values remain `underspecified`.
2. Reconstruct Heikin-Ashi causally and preserve confirmed-bar signal / next-bar-open entry timing. Reject any implementation that leaks current/future bar information.
3. Compare the full sequence against simple baselines: Heikin-Ashi color flip alone, three same-color bars without wick/body constraints, and the morphology sequence without ADX.
4. Ablate separately the wickless requirement, monotonically increasing body requirement, color-flip prerequisite and ADX gate to identify whether any component adds out-of-sample information.
5. Test both one-bar and ATR exits without treating exit engineering as signal alpha.
6. Stress spread, commission, slippage and one-bar adverse gaps at realistic one-minute crypto liquidity. The thesis is materially weakened if gross edge disappears under modest realistic costs or is concentrated in a small number of sessions.
7. Evaluate multiple liquid crypto instruments, venues and non-overlapping out-of-sample periods. Reject robustness claims if results depend on one venue/candle boundary or narrow parameter tuning.

## Crypto portability

`direct`. The source explicitly lists crypto among intended liquid instruments, although it does not provide independently verified crypto performance evidence.

Crypto-specific risks are substantial at this horizon: 24/7 candle boundaries, venue fragmentation, spread/slippage, exchange latency and outages, and for perpetuals funding/mark/index/liquidation mechanics. The one-bar default exit makes execution friction particularly likely to dominate small gross expectancy.

## Limitations

- Exact ADX/DMI parameters are **underspecified** in the reviewed prose.
- ATR/TP/SL/Plug defaults are **underspecified**.
- Exact position sizing and re-entry/pyramiding semantics are **underspecified**.
- Equality semantics for "wickless" Heikin-Ashi bars may depend on tick precision and implementation details.
- Heikin-Ashi candles are synthetic; the morphological interpretation is not direct evidence of actual intrabar order flow.
- One-minute execution is highly cost- and latency-sensitive.
- Not independently reproduced.

## Implementation status

`not-implemented`.

No backtest, Pine execution, or implementation in the user's quantitative research stack was performed in this Scout cycle.

## Adoption boundary

Research material only. Presence in this repository does not imply profitable alpha, successful validation, implementation approval, paper/testnet/live approval, or authorization to trade.

## Related Wiki records

No Hermes Wiki Brain record was consulted or asserted in this GitHub-only Scout cycle.

## Sources

- TradingView — `BVLabs`, **1-Min Rapid Scalper**: https://www.tradingview.com/script/d7hoosSf-1-Min-Rapid-Scalper/ (public open-source strategy; page shows update/release note 2026-08-10; reviewed 2026-09-18).
