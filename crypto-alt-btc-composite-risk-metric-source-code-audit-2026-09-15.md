---
schema: strategy-research-record-v1
type: strategy-research-record
title: "ALT/BTC Composite Risk Metric DCA Strategy — Source-Code Audit"
created: 2026-09-15
updated: 2026-09-15
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - tradingview
  - altcoin
  - relative-strength
  - sentiment-proxy
  - source-code-audit
status: research-only
confidence: low
source_as_of: 2026-09-15
sources:
  - "https://www.tradingview.com/script/bZzxTcfj-ALT-Risk-Metric-Strategy/"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
---

# ALT/BTC Composite Risk Metric DCA Strategy — Source-Code Audit

## Provenance

- **Primary source:** TradingView open-source strategy `ALT Risk Metric Strategy` by `nakphanan`.
- **Stable source URL:** https://www.tradingview.com/script/bZzxTcfj-ALT-Risk-Metric-Strategy/
- **Publication / update:** published 2025-12-10; TradingView page reviewed as of 2026-09-15. The page includes later release text describing a four-dimension composite risk metric.
- **Source inspection:** the public TradingView description and the current Pine source were inspected directly. The normalized rules below paraphrase the source; no Pine script is reproduced.
- **Deduplication / incremental value:** repository and read-only Hermes Wiki Brain searches found multiple generic Fear & Greed, sentiment, macro, and relative-strength records, but no record for this TradingView source or the same ALT/BTC composite construction. The incremental value is principally **source-code integrity / execution evidence**: the advertised profit-only exit is absent from executable sell conditions, the named "Social Risk" component is price-derived RSI/ATR rather than social data, and the selected crypto input does not force the strategy to trade that same instrument because TradingView strategy orders execute on the chart symbol.

## Economic mechanism

### Source-reported

The source proposes that an altcoin's price relative to Bitcoin is a more useful crypto-cycle state variable than its USD price alone. Low ALT/BTC risk is treated as relative undervaluation / accumulation opportunity; high ALT/BTC risk is treated as relative overextension / profit-taking opportunity. The page describes a weighted weekly technical risk score supplemented by synthetic Fear & Greed, macro PMI, and "Social Risk" adjustments, then applies tiered DCA entries and sequential partial exits.

The page's baseline technical score uses approximately 5% normalized MACD, 60% RSI, and 35% deviation from a long-term moving average. It describes the additional dimensions as market sentiment, US manufacturing PMI, and social-risk context.

### Research interpretation

The economically testable object is not DCA sizing itself. It is a **composite relative-risk state** whose core is ALT/BTC trend/momentum and whose auxiliary components are intended to condition crypto-cycle exposure. If valid, the composite should identify periods when an altcoin is unusually weak versus BTC before subsequent relative recovery, and periods of unusually strong ALT/BTC extension before subsequent relative underperformance.

The source-code audit materially narrows that interpretation:

- the so-called Fear & Greed component is a **synthetic market-data proxy**, not an externally published Crypto Fear & Greed Index;
- the so-called Social Risk component is derived from the chart symbol's own RSI and ATR/price volatility, not from social-media observations;
- the macro component uses TradingView `ECONOMICS:USBCOI`, which other TradingView material uses as an ISM/PMI proxy, but the exact economic-series identity and release-time alignment must be independently validated before causal testing;
- the source description states that sells occur only when in profit, but the inspected sell predicates contain no average-entry-price or P&L gate. This is a direct description-versus-code contradiction.

## Signal

The following is a source-faithful normalization of the current Pine logic, with ambiguities called out explicitly.

- **Formation timestamp / availability:** signals are evaluated on the chart bars while higher-timeframe ALT/BTC inputs are requested with `lookahead_off`. The source does not additionally require the prior completed weekly observation (for example via a one-week offset), so a future reproduction must distinguish historical TradingView HTF-bar semantics from realtime developing-week availability rather than assuming a completed-week-only signal.
- **Primary instrument state:** build the selected altcoin/Bitcoin pair from user inputs (default altcoin `ETH`, exchange `BINANCE`) and request weekly data.
- **Core technical lookbacks / defaults:**
  - RSI length: 10 weeks;
  - long-term moving-average length: 150 weeks;
  - MACD-style EMA lengths: 8 and 26 weeks;
  - normalization lookback for the MACD component: 500 weekly observations;
  - final smoothing length: 5.
- **Core technical score:** combine the normalized MACD component at 5%, RSI at 60%, and long-term moving-average deviation component at 35%, producing a risk-scale technical state.
- **Synthetic Fear & Greed adjustment (enabled by default):** source constructs a market-data proxy from ALT/BTC price/return/money-flow-like terms and crypto market context including TradingView `BVOL24H` and `BTC.D`; default weight is 0.20 and smoothing is 5. This is not source evidence of an external published Fear & Greed index.
- **Macro adjustment (enabled by default):** request TradingView `ECONOMICS:USBCOI` at daily frequency, smooth over 3 observations, compare with the source's 50 neutral level, and apply default weight 0.15. `pmiOffset` is configurable by the source; any nonzero setting must be audited for point-in-time validity before research use.
- **"Social Risk" adjustment (enabled by default):** compute RSI(14) on the chart symbol, center it around the neutral region, damp/scale using ATR-relative volatility, smooth over 7 observations, and apply default weight 0.10. Despite the label, the inspected implementation requires no social-media or sentiment-feed data.
- **Entry:** long-only. On each eligible chart bar, if composite risk is at or below tier thresholds, submit DCA cash-sized entries. Defaults are L1 <=70 for 5 units of quote cash, L2 <=50 for 6 additional units, and L3 <=30 for 7 additional units; deeper tiers accumulate the applicable amounts as coded. Pyramiding is set high enough to permit repeated accumulation.
- **Exit:** sequential risk-threshold partial closes. Defaults are L1 >=70 with `qty_percent=25`, L2 >=85 with `qty_percent=35`, and L3 >=100 with `qty_percent=40`, with state flags enforcing sequence. **Current source-code sell conditions do not test whether the position is profitable**, despite the page statement that exits trigger only when in profit.
- **Holding / rebalance:** no fixed holding period and no short side. Positions can persist while risk remains between active exit conditions. New qualifying buys can reset the staged sell progression as defined by the source.
- **Stop:** no source stop-loss rule identified.
- **Trading instrument boundary:** TradingView `strategy.entry` / `strategy.close` act on the chart instrument. The selected altcoin input controls signal construction and webhook metadata but does not itself force the Strategy Tester to trade that selected external symbol. A source-parity test must therefore require chart-symbol / selected-symbol consistency or explicitly classify cross-symbol testing as a different hypothesis.

## Required data

- Weekly selected ALT/BTC OHLCV / close series as requested from TradingView.
- Chart-symbol OHLCV for the chart-timeframe "Social Risk" proxy and actual Strategy Tester instrument.
- TradingView `BVOL24H` series used by the synthetic Fear & Greed proxy.
- TradingView `BTC.D` Bitcoin-dominance series.
- TradingView `ECONOMICS:USBCOI` macro series used by the source as a PMI-like input.
- Point-in-time requirements:
  - preserve the actual availability of higher-timeframe weekly values at each chart timestamp;
  - preserve the publication/revision timing of the macro series rather than backfilling revised history as if known earlier;
  - do not silently substitute Alternative.me or another Fear & Greed index for the source's synthetic proxy;
  - require selected ALT/BTC symbol availability on the chosen exchange, and separately verify chart-symbol parity for the traded instrument.

## Execution assumptions

- Source declares initial capital of 10,000 and cash-based sizing.
- Source declares 0.1% commission.
- Source enables `process_orders_on_close=true`.
- No explicit source slippage model was identified.
- Repeated DCA entries are permitted through high pyramiding.
- The backtest executes on the chart symbol; external symbol inputs are used for signal/context and webhook construction, not for cross-instrument order routing inside TradingView Strategy Tester.
- Any independent reproduction should use the first executable price consistent with the source's order-processing setting and must not infer fills on a different selected altcoin unless the chart itself is that instrument.

## Evidence

### Source-reported

- TradingView publishes the script as open source and describes it as an ALT/BTC risk strategy for multi-crypto DCA and profit taking.
- The source describes RSI, MACD, long-term moving-average deviation, synthetic market-sentiment context, macro PMI context, and a volatility-adjusted RSI "Social Risk" component.
- The page states that exit tiers are sequential and states that sells trigger when in profit and risk exceeds thresholds.
- No source Sharpe ratio, CAGR, statistically controlled out-of-sample alpha estimate, or independent live-performance evidence was identified in the reviewed TradingView material.

### Independently reproduced

not independently reproduced

### Negative evidence

- **Description / executable-code contradiction:** the page states that sells trigger only when in profit, but the inspected executable sell conditions depend on positive position size, risk thresholds, and sell-stage flags; no average-entry-price or realized/unrealized-profit condition is present.
- **"Social" naming overstates data provenance:** the inspected Social Risk component is price-derived RSI plus ATR-relative volatility and contains no social-media observations.
- **Synthetic sentiment rather than independent sentiment feed:** the Fear & Greed label refers to a composite proxy constructed from market-price/volume/dominance/volatility variables, not a separately observed sentiment index. This creates substantial feature overlap with the technical core and weakens claims of independent multimodal confirmation.
- **Instrument-parity risk:** Strategy Tester orders execute on the chart instrument, while the selected crypto input drives the ALT/BTC signal. A user can therefore produce a backtest whose traded chart symbol differs from the selected signal asset unless parity is enforced manually.
- **Point-in-time macro risk:** the macro series must be aligned to its original publication availability and revisions; the source itself does not demonstrate a vintage-data audit.
- **No independent performance reproduction:** no independent net-of-cost OOS result was found for this exact composite.

## Falsification plan

1. **Source-parity reproduction.** Reimplement only the inspected code semantics on a fixed altcoin/chart pair and compare risk values, staged entries, and staged exits with TradingView. `research-defined falsification threshold`: any persistent unexplained mismatch in signal timestamps or staged trade state invalidates the reproduction before alpha evaluation.
2. **Profit-gate contradiction test.** Record every source-code exit and test whether any executes below the then-current average entry price. If at least one such exit occurs, reject the page's "only when in profit" statement as a description of the executable strategy.
3. **Component ablation.** Compare core ALT/BTC technical score versus +synthetic Fear & Greed, +macro, and +"Social Risk" components in frozen walk-forward folds. `research-defined falsification threshold`: if auxiliary components fail to improve net OOS risk-adjusted performance or downside control versus the core across the majority of predeclared folds, classify them as redundant rather than incremental alpha.
4. **True-sentiment placebo / substitution.** Compare the source's synthetic Fear & Greed proxy with a separately timestamped external crypto sentiment index only as a research-proposed variant. If the source proxy behaves no better than its own price-only ablation, reject any interpretation that the label itself establishes independent sentiment information.
5. **Macro vintage audit.** Reconstruct `USBCOI` publication availability and revisions. `research-defined falsification threshold`: if a causal vintage-aligned series materially changes the sign/timing of the macro adjustment or removes any OOS benefit, reject the macro-conditioning edge.
6. **Chart / selected-symbol parity test.** Run identical selected ALT/BTC signals on (a) matching chart instrument and (b) deliberately mismatched chart instrument. Any performance difference attributable to the traded chart rather than the selected asset demonstrates that unguarded backtests are not evidence for the advertised selected-altcoin strategy.
7. **Threshold robustness.** Predeclare perturbations around 70/50/30 buy and 70/85/100 sell thresholds plus adjacent RSI/MA/MACD lookbacks. `research-defined falsification threshold`: if positive net OOS performance is isolated to one narrow setting and fails for the majority of neighboring specifications, classify the result as parameter-fragile.
8. **Execution-cost stress.** Retest with observed venue fees, spread and slippage beyond the source's commission-only assumption. `research-defined falsification threshold`: if net OOS excess return versus a simple matched DCA / BTC-relative benchmark is non-positive under realistic costs, reject tradeability.

## Crypto portability

**Direct but venue-sensitive.** The source is crypto-native and uses ALT/BTC, BTC dominance and crypto volatility context. Portability is nevertheless constrained by exchange-specific ALT/BTC history, delistings, changing liquidity, missing volume, and the chart-symbol / selected-symbol boundary. Smaller altcoins introduce severe survivorship and execution-cost risk. No claim of portability to every listed altcoin is warranted from the source alone.

## Limitations

- `contested: true` because the profit-only exit statement is inconsistent with inspected executable sell predicates.
- The economic value of repeated DCA sizing is separate from predictive alpha and must not be counted as evidence that the risk metric forecasts returns.
- Synthetic Fear & Greed and "Social Risk" are predominantly transformations of market data, so apparent multi-factor diversification can be overstated.
- Macro vintage/revision handling is not established.
- Higher-timeframe formation semantics require explicit historical-versus-realtime parity testing.
- No independent reproduction, OOS robustness study, capacity analysis, or live execution evidence was identified.
- No explicit source slippage model was identified.
- Multi-asset claims require separate testing because each altcoin has different listing history, liquidity and structural survivorship risk.

## Implementation status

`not-implemented` — this record only normalizes and audits a public TradingView research source. No strategy implementation, backtest runtime change, execution adapter, or production task is authorized by this Scout record.

## Adoption boundary

`not-approved` / `research-only` — the record may enter research review but must not be treated as approval for Paper, Testnet, or Live trading. Promotion requires independent source-parity reproduction, point-in-time data validation, falsification, realistic cost testing, and separate approval under the quantitative research pipeline.

## Related Wiki records

- `[[quant/crypto-macro-sentiment-contrarian-fear-greed-ema-2026-09-03]]` — related crypto sentiment timing family, but it uses an external Fear & Greed series and a different mechanism.
- `[[quant/crypto-fear-greed-weekly-ar1-innovation-risk-premium-2026-09-04]]` — related Fear & Greed research, but studies a sentiment innovation risk premium rather than this TradingView ALT/BTC composite.
- `[[quant/crypto-bitcoin-cvar-risk-aware-q-learning-adaptive-controller-2026-09-02]]` — related use of crypto sentiment as a risk state, with a different RL exposure-control mechanism.

## Sources

1. TradingView, `ALT Risk Metric Strategy`, nakphanan, open-source public strategy: https://www.tradingview.com/script/bZzxTcfj-ALT-Risk-Metric-Strategy/
