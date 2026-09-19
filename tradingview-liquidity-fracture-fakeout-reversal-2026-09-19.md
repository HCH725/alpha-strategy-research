---
schema: strategy-research-record-v1
title: "TradingView Liquidity Fracture Fakeout Reversal"
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
  - https://www.tradingview.com/script/JRCQ5jXF-Liquidity-Fracture-Detector/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Liquidity Fracture Fakeout Reversal

## Provenance

Public TradingView open-source script **Liquidity Fracture Detector**, published 2025-04-18 by **CryptoSnagger**. Stable source: https://www.tradingview.com/script/JRCQ5jXF-Liquidity-Fracture-Detector/ . Source reviewed as of 2026-09-19.

The source describes an indicator for intraday micro-liquidity traps and structural fakeouts. It explicitly states that it is a discretionary-analysis tool rather than a buy/sell system or automated strategy.

## Economic mechanism

### Source-reported

The author frames a "liquidity fracture" as a temporary structural break associated with a volume spike, abnormal candle range, an extreme wick, and a break of a previous high/low that closes back inside the prior range. The stated interpretation is that such events can represent stop hunts, inefficient fills, or manipulated/order-flow-driven fakeouts and may precede reversals or trend acceleration.

### Research interpretation

The falsifiable alpha hypothesis is narrower than the source narrative: an intrabar break of recent structure that fails by bar close may contain short-horizon reversal information when the failure occurs with unusually high participation, unusually large range, and rejection-dominant candle geometry.

The proposed mechanism is failed price discovery / liquidity-taking exhaustion: aggressive movement through an observable prior extreme attracts or triggers liquidity, but inability to sustain the break by the close indicates that the marginal move was rejected. Volume and range anomalies are treated as participation/intensity filters, not independent proof of institutional activity.

Whether the event predicts reversal, continuation, or merely higher subsequent volatility is unresolved and must be tested rather than assumed.

## Signal

**Source-supported fracture event:**

- volume spike: current volume greater than `2x` its average; the source says the sensitivity is adjustable but does not expose the averaging lookback in the reviewed description;
- volatility/range spike: current candle range greater than `1.5x` its average; averaging lookback is underspecified in the reviewed description;
- extreme wick: wick larger than candle body;
- structural failure: price trades beyond a previous high or low and closes back within the old range;
- the source states that these elements are combined to mark a fracture.

The source labels an upside fakeout as a potential bull trap and a downside fakeout as a potential bear trap. It does not specify a canonical automated entry, exit, holding period, re-entry rule, position size, or order model.

**Research-proposed operationalization for later testing:** treat a confirmed downside fracture at bar close as a candidate long-reversal event and an upside fracture as a candidate short-reversal event. Test forward returns over fixed horizons rather than inventing a source-derived exit. Separately test continuation and absolute-return outcomes so the research does not presuppose reversal.

Signal formation should use only information available at the completed signal bar. Exact definition of "previous high/low," averaging windows, and wick-side handling remain underspecified and must be resolved transparently during implementation rather than attributed to the source.

## Required data

- OHLCV bars.
- Prior price structure sufficient to define the relevant previous high/low; exact source lookback is underspecified.
- Rolling volume average; source averaging lookback underspecified.
- Rolling candle-range average; source averaging lookback underspecified.
- Source describes intraday use cases at 1m, 5m, and 15m.
- Source states applicability to crypto, indices, futures, and forex; no specific crypto venue or market type is prescribed.
- Point-in-time construction is required: rolling references and structural levels must not use future bars.

## Execution assumptions

The source does not specify signal-to-order timing, market versus limit execution, fill model, fees, spread, slippage, market impact, funding, leverage, margin, borrow, latency, or partial fills.

For later research, any executable version should act no earlier than after the fracture bar is confirmed unless an explicitly causal intrabar implementation is separately defined. Execution assumptions would be research-proposed, not source-reported.

## Evidence

### Source-reported

The source describes the detection logic and intended discretionary use but does not provide a traceable performance statistic, Sharpe ratio, CAGR, drawdown, win rate, or independently audited backtest result in the reviewed page. No performance figure is therefore recorded here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself says the indicator does not provide buy/sell signals and recommends combining it with other price-action or order-flow setups. It also says marked fractures may precede either reversals **or trend accelerations**, which is direct ambiguity against treating every event as a contrarian signal.

No independent negative study was identified in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

1. Build the event causally on liquid crypto instruments across 1m, 5m, and 15m data, with all rolling/structure definitions frozen before OOS evaluation.
2. Measure signed forward returns after upside and downside fractures over multiple fixed horizons; also measure absolute forward returns to distinguish directional alpha from volatility forecasting.
3. Compare against unconditional returns and against matched controls with similar realized range and volume but without failed structural breaks.
4. Ablate the four components: structural failure only; + volume anomaly; + range anomaly; + wick condition. Reject complexity that does not add stable OOS information.
5. Sweep reasonable averaging/structure windows only in training data and require parameter neighborhoods, not a single optimized point, to survive OOS.
6. Test bull-trap and bear-trap directions separately and stratify by trend/regime and volatility state.
7. Apply realistic fees, spread and slippage appropriate to intraday crypto. If any directional edge disappears under plausible costs, reject it as a tradable alpha even if gross predictability exists.
8. Use walk-forward/OOS evaluation and reject the reversal thesis if the sign is unstable, indistinguishable from matched controls, or consistently explained only by elevated absolute volatility.

## Crypto portability

**direct** — the source explicitly includes crypto among its intended markets.

Portability still depends on venue and market type. Spot and perpetual markets can differ in volume, leverage-driven liquidation behavior, funding, and microstructure. Candle boundaries and exchange-specific volume can materially change fracture detection. Cross-venue robustness should therefore be tested rather than assuming one feed is representative.

## Limitations

- `underspecified`: previous-high/low lookback or pivot definition.
- `underspecified`: volume-average lookback.
- `underspecified`: range-average lookback.
- `underspecified`: exact wick-side logic when both wicks are large.
- `underspecified`: entry, exit, holding period, re-entry, sizing and execution.
- The stop-hunt / manipulation language is an interpretation, not directly observed participant identity from OHLCV bars.
- A four-condition conjunction can reduce sample size and increase overfitting risk.
- Not independently reproduced.

## Implementation status

Not implemented in our research stack. No backtest or formal validation was run by this Scout.

## Adoption boundary

Research material only. Presence in this repository does not establish profitability, validated alpha, implementation approval, paper-trading approval, testnet approval, or live-trading approval.

## Related Wiki records

No stable Hermes Wiki Brain record is asserted here; GitHub-only Scout operation does not access Wiki Brain.

## Sources

- TradingView — CryptoSnagger, **Liquidity Fracture Detector**, published 2025-04-18, reviewed 2026-09-19: https://www.tradingview.com/script/JRCQ5jXF-Liquidity-Fracture-Detector/
