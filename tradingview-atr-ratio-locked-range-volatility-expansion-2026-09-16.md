---
schema: strategy-research-record-v1
title: ATR-Ratio Locked-Range Volatility Expansion Breakout
created: 2026-09-16
updated: 2026-09-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-16
sources:
  - https://www.tradingview.com/script/57J0Kih3-Volatility-Expansion-Strategy-30M-MNQ/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# ATR-Ratio Locked-Range Volatility Expansion Breakout

## Provenance

Public TradingView open-source strategy page, **Volatility Expansion Strategy 30M [MNQ]**, by **ZenOutMan**, published Apr 13, 2026. Stable source: https://www.tradingview.com/script/57J0Kih3-Volatility-Expansion-Strategy-30M-MNQ/. Source reviewed 2026-09-16.

The source is written for MNQ on a 30-minute chart. Crypto use below is therefore a research-proposed portability hypothesis, not source-reported crypto evidence.

## Economic mechanism

### Source-reported

The author describes a volatility-cycle thesis: low-volatility "coiling" is followed by volatility expansion. Rather than trading any price high/low, the strategy freezes levels formed during compression and requires both relative-volatility expansion and a break of the frozen range.

### Research interpretation

Hypothesis: a transition from unusually low short-horizon realized range to renewed expansion can identify a regime in which a break of the immediately preceding compressed range has more directional persistence than an unconditional range breakout.

Component roles:

- Regime/setup: ATR-based relative-volatility compression.
- Primary signal: breakout of levels locked during the compressed state.
- Confirmation: ATR-based relative volatility must have expanded above its threshold at the breakout.
- Risk logic: ATR-derived stop distance; this is risk management, not assumed alpha.

The incremental feature versus a generic Donchian or squeeze breakout is the state-dependent **level locking**: the breakout reference is formed only during the volatility-compression state and freezes when that state ends.

## Signal

Source-reported normalized logic:

- Source timeframe/instrument: MNQ, 30-minute.
- Volatility ratio: `ATR(20) / SMA(ATR(20), 40)`.
- Compression state: volatility ratio < 0.95.
- While compressed, breakout high and breakout low are updated from the current bar's high and low.
- When compression ends, those levels freeze.
- Expansion confirmation: volatility ratio > 1.02.
- Entry trigger: expansion confirmation must coincide with price crossing a frozen breakout level; an upside crossover implies long and a downside cross implies short.
- Risk distance: ATR × 1.5, converted to instrument ticks for the source's MNQ execution model.

Underspecified from the reviewed TradingView description:

- exact Pine ATR smoothing convention beyond TradingView's `ta.atr` implementation;
- whether frozen levels represent only the last compressed bar's high/low or accumulated extrema across the compression episode (the prose says levels update to the current bar, so this distinction requires source-code-level confirmation before implementation);
- exact order timing/fill convention for crossover bars;
- profit-taking rule, if any, beyond the described ATR stop;
- re-entry and reset behavior after a completed breakout/trade;
- simultaneous/edge-case state transitions.

No missing rule is promoted here to a source-reported fact.

## Required data

For the source formulation:

- MNQ 30-minute OHLC data;
- sufficient history for ATR(20) and the 40-period SMA of ATR;
- instrument tick size for source-specific stop conversion.

For a research-proposed crypto port:

- spot or perpetual OHLC with fixed, explicitly defined candle boundaries;
- at least the same volatility-indicator warm-up history;
- venue/instrument tick size if reproducing tick-normalized order offsets.

No funding, open-interest, order-book, or options data is required by the source signal.

Point-in-time requirement: all compression, expansion, and frozen-level states must be constructed only from bars available at the signal timestamp. Candle-boundary and bar-close semantics must be fixed before testing.

## Execution assumptions

The source states that the risk distance is ATR × 1.5 and converted to ticks, with `strategy.exit` orders intended to protect positions during fast volatility moves.

The reviewed description does not fully specify same-bar versus next-bar fills, market/stop order semantics, fees, spread, slippage, partial fills, latency, or capacity. Those are **underspecified** and must be explicit in any later experiment.

For perpetual crypto, funding and mark/index-price mechanics would additionally need to be modeled if the holding period spans funding events; this is research-proposed portability handling, not part of the source.

## Evidence

### Source-reported

The TradingView page explains the rule and its intended volatility-expansion mechanism. No performance statistic from the page is relied upon in this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed source; absence is not evidence of no negative result. Generic breakout risks remain relevant, including false expansion, gap/slippage sensitivity, and threshold overfitting.

## Falsification plan

A later crypto test should falsify the hypothesis rather than merely optimize thresholds:

1. Freeze the source parameters first: ATR 20, ATR-baseline SMA 40, compression <0.95, expansion >1.02.
2. Test liquid crypto spot/perpetual markets across multiple fixed timeframes and volatility regimes with point-in-time bars.
3. Compare against an unconditional breakout using the same reference-range construction and against a simple volatility-squeeze breakout baseline.
4. Ablate the expansion confirmation and separately replace the compression-conditioned frozen level with an ordinary rolling high/low. This tests whether level locking and the volatility transition add incremental information.
5. Apply realistic fees, spread, slippage and, for perpetuals, funding.
6. Require out-of-sample persistence across assets/regimes. Material disappearance after costs, failure to outperform matched breakout controls, or performance concentrated in one asset/period materially weakens or falsifies the portable-alpha thesis.

## Crypto portability

**adapted**

The source demonstrates the construction on MNQ, not crypto. The volatility-state mechanism is instrument-agnostic enough to test in crypto, but portability is unproven.

Crypto-specific risks include 24/7 trading with no natural cash-session reset, venue-dependent candle boundaries, fragmented liquidity, more frequent discontinuous volatility bursts, spot/perpetual basis differences, and funding for perpetual positions. A crypto experiment must define when a compression episode begins/ends without importing an unstated session assumption.

## Limitations

- not independently reproduced;
- source evidence is MNQ, not crypto;
- execution details are underspecified;
- exact compressed-range level-update semantics require confirmation before implementation;
- threshold robustness (0.95 / 1.02) is unproven;
- no profitability or validation claim is made.

## Implementation status

Not implemented in the research stack. No PyBroker, Nautilus, paper, testnet, or live verification has occurred.

## Adoption boundary

Research material only. Presence in this repository does not mean profitable, validated alpha, approved for implementation, or approved for paper, testnet, or live trading.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted from this GitHub-only Scout run.

## Sources

- TradingView — ZenOutMan, **Volatility Expansion Strategy 30M [MNQ]**: https://www.tradingview.com/script/57J0Kih3-Volatility-Expansion-Strategy-30M-MNQ/ (published Apr 13, 2026; reviewed 2026-09-16).
