---
schema: strategy-research-record-v1
title: "FER-Hurst-ADX Regime-Gated AMO/KAMA Momentum with TradingView Source-Code Contradiction Audit"
created: 2026-09-14
updated: 2026-09-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
  - regime-filter
  - momentum
  - hurst
  - fractal-efficiency
  - source-code-audit
status: research-only
confidence: low
source_as_of: 2026-09-14
sources:
  - https://www.tradingview.com/script/NK5dYlr4-Entropic-Regime-Field-JOAT/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "TradingView description presents Garman-Klass volatility as part of a three-factor entropy classifier, but the reviewed Pine source does not use GK in the LOW/HIGH regime gate."
  - "TradingView prose says AMO crosses zero; the reviewed Pine source triggers at +20/-20."
  - "TradingView prose describes GK normalization as a percentile rank; the reviewed Pine source uses trailing-100-bar min-max normalization."
---

# FER-Hurst-ADX Regime-Gated AMO/KAMA Momentum with TradingView Source-Code Contradiction Audit

## Provenance

- Primary source: `officialjackofalltrades`, **Entropic Regime Field [JOAT]**, public TradingView open-source Pine Script indicator, published June 5, 2026; page and source reviewed 2026-09-14.
- Stable public URL: https://www.tradingview.com/script/NK5dYlr4-Entropic-Regime-Field-JOAT/
- The full public Pine source was inspected rather than relying only on the publication prose. This record normalizes the logic and does not reproduce the script.
- Repository deduplication on 2026-09-14 found no existing record with TradingView identity `NK5dYlr4` or the same FER + synthetic-Hurst + ADX regime gate combined with AMO/KAMA simultaneous confirmation. Existing Hurst, entropy, and regime records use materially different mechanisms, datasets, or signals.
- Incremental value is primarily the exact source-code audit: three material discrepancies exist between the publication description and the actual Pine implementation.

## Economic mechanism

### Source-reported

The author proposes that directional momentum should be acted on only when price behavior is sufficiently organized. Fractal Efficiency Ratio (FER) measures how straight the recent price path is, a synthetic Hurst approximation measures persistence, and ADX requires directional strength. Momentum is represented by a weighted composite of RSI, Stochastic, and Williams %R and is confirmed by price crossing a KAMA. The publication also describes Garman-Klass (GK) volatility as part of the entropy framework.

### Research interpretation

The falsifiable alpha hypothesis is not that “entropy” itself predicts returns, but that a **persistence/efficiency regime gate** can improve the conditional quality of a simultaneous momentum-and-adaptive-trend crossover. If the gate adds genuine information, AMO/KAMA signals taken only when FER, synthetic Hurst, and ADX jointly indicate persistence should outperform the same signals without the gate after realistic costs. Because the source code does not actually use GK in regime classification, GK should be treated as a diagnostic display variable unless separately tested as a `research-proposed` extension.

## Signal

The public Pine source makes the core signal mechanically reconstructable.

### Source-reported construction

**Regime inputs and defaults**

- FER lookback: 14 bars.
- LOW-regime FER threshold: `FER >= 0.60`.
- HIGH-regime FER threshold: `FER <= 0.35`.
- Synthetic Hurst window: 20 bars.
- LOW-regime Hurst threshold: `H >= 0.52`.
- ADX: `ta.dmi(14,14)`; LOW-regime minimum `ADX >= 22`; HIGH-regime trigger if `ADX < 14`.
- GK averaging length: 14 bars; GK is calculated and displayed but is **not used in the Pine LOW/HIGH regime gate**.

FER is the absolute 14-bar net close displacement divided by the sum of absolute one-bar close changes over the same lookback.

The synthetic Hurst approximation compares variance of 1-bar price changes with variance of 5-bar changes divided by 5 over a 20-bar window, transforms the variance ratio through a log-based formula, adds 0.5, and clamps the estimate to `[0.1, 0.9]`. The source itself cautions that this is a simplified directional approximation rather than a rigorous Hurst estimator.

Regime state in the reviewed code is:

- **LOW:** `FER >= 0.60 AND ADX >= 22 AND synthetic Hurst >= 0.52`.
- **HIGH:** `FER <= 0.35 OR ADX < 14`.
- **TRANSITION:** otherwise.

**Adaptive Momentum Oscillator (AMO)**

- RSI(14), centered at 50, weight 40%.
- Stochastic(14), centered at 50, weight 35%.
- Williams %R(14), centered at -50, weight 25%; the reviewed code applies an explicit negative sign in its normalization.
- Composite multiplied by 100.
- AMO threshold default: `20`.
- KAMA period default: 21.
- Signal cooldown: 5 bars.

**Long signal:** on a confirmed bar, all of the following must occur simultaneously:

1. AMO crosses above `+20`;
2. regime is LOW;
3. close crosses above KAMA;
4. at least 5 bars have elapsed since the prior signal.

**Short signal:** symmetric conditions with AMO crossing below `-20` and close crossing below KAMA.

This differs materially from the publication prose, which says AMO crosses zero.

**Reference trade block**

The indicator visually marks reference levels at signal close using ATR(14): target `2.0 × ATR` and stop `1.5 × ATR`. Because this is an indicator rather than a TradingView `strategy()`, these are signal annotations rather than broker-emulator orders.

### Formation / availability

- Signals require `barstate.isconfirmed`; therefore they become available only at the completed chart bar.
- No future-data request was identified in the reviewed signal construction.
- Timezone/session convention is inherited from the TradingView chart and is not fixed by the source.
- Warm-up behavior is governed by Pine `na` propagation through rolling calculations; no explicit source-defined minimum warm-up bar count is provided.

### Holding / exit / overlap

The source does not define an executable position lifecycle, position sizing, overlapping-position policy, or formal exit precedence. The ATR target/stop boxes are visual reference levels. Therefore the **execution layer is underspecified**, even though the signal trigger itself is reconstructable.

## Required data

- Instrument: any chart instrument with valid OHLC data; volume is not required by the core reviewed regime/AMO/KAMA signal.
- Fields: open, high, low, close, timestamp; chart history sufficient for the rolling windows.
- Venue/universe: not specified by source.
- Timeframe: configurable TradingView chart timeframe; no source-validated optimal timeframe is established.
- Point-in-time: only completed bars may trigger signals because of `barstate.isconfirmed`.
- Timestamp: exchange/chart timezone unless a reproduction explicitly freezes another convention.
- Missing/stale data: not explicitly handled by the source; `research-proposed` reproduction should fail closed rather than impute missing OHLC.
- Fees, spread, slippage, funding, borrow, and impact data are absent from the source indicator and are required for any tradability test.

## Execution assumptions

The source is an indicator, not an executable `strategy()`. No source-defined order type, broker fill model, latency, spread, slippage, fee schedule, participation cap, leverage, margin, funding, borrow, liquidation logic, position sizing, or partial-fill behavior is provided.

For any later test, a `research-proposed` causal convention should execute no earlier than the next tradable event after the confirmed signal bar, with explicit fees/spread/slippage and, for perpetuals, funding. None of those assumptions are source-reported.

The source includes a lightweight internal win/loss dashboard, but it is not treated as valid performance evidence here because its accounting is not equivalent to a broker-simulated strategy: it can inspect bar high/low against reference levels, does not model trading costs, and does not supply a complete executable position lifecycle.

## Evidence

### Source-reported

TradingView presents the script as an open-source three-state market classifier and says directional AMO/KAMA signals are restricted to LOW entropy regimes. The page reports default FER lookback 14, LOW/HIGH FER thresholds 0.60/0.35, Hurst window 20 with LOW threshold 0.52, GK averaging length 14, and LOW-regime ADX minimum 22. It also states that signals are confirmed-bar/non-repainting and warns that the Hurst estimate is simplified. No fixed Sharpe, CAGR, drawdown, statistically validated out-of-sample return, or crypto-specific performance result is reported on the reviewed page.

The source code supplies additional exact logic: LOW regime requires FER, ADX, and Hurst together; HIGH regime requires low FER or ADX below 14; AMO uses 40/35/25 weights and triggers at ±20 with simultaneous KAMA crossover; cooldown is 5 bars; ATR reference target/stop defaults are 2.0/1.5.

### Independently reproduced

not independently reproduced

### Negative evidence

- **GK contradiction:** publication prose markets FER + Hurst + GK as a three-factor entropy architecture, but the actual LOW/HIGH gate in the reviewed Pine source does not reference GK. ADX is the third operative gate instead.
- **AMO trigger contradiction:** publication prose says AMO crosses zero; source code requires crossing `+20` for long and `-20` for short.
- **GK normalization contradiction:** prose calls GK normalization a trailing-100-bar percentile rank; source code uses min-max normalization over the trailing 100 bars, which is not an empirical percentile rank.
- **Synthetic-Hurst limitation:** the author explicitly states the Hurst approximation is simplified and should not be interpreted as a rigorous statistical Hurst estimate.
- **Internal dashboard is weak evidence:** no transaction costs or executable order model are provided, same-bar high/low handling can create ambiguous outcome ordering, and the dashboard is not a `strategy()` backtest. No dashboard statistic is accepted here as performance evidence.
- **Existing external caution in this repository:** adjacent research documents that common trend/regime filters can fail out of sample or after costs; therefore the FER/Hurst/ADX gate must demonstrate incremental value over ungated AMO/KAMA rather than being presumed useful.
- No source-reported walk-forward, cross-venue, parameter-stability, capacity, or crypto-perpetual cost study was found.

## Falsification plan

All protocols below are `research-proposed`; numeric rejection rules are `research-defined falsification threshold` values.

1. **Gate ablation / incremental-alpha test.** On BTCUSDT and ETHUSDT perpetuals at 1h and 4h, compare: (a) AMO+KAMA only, (b) +FER, (c) +FER+ADX, (d) +FER+ADX+synthetic Hurst. Use chronological walk-forward splits and identical execution/cost assumptions. `research-defined falsification threshold`: reject the regime-gate hypothesis if the full gate fails to improve median OOS net Sharpe by at least 0.15 over ungated AMO+KAMA and does not reduce maximum drawdown by at least 10% relative.
2. **GK contradiction test.** Add GK only as a separately labeled `research-proposed` gate and compare it with the actual source-code gate. `research-defined falsification threshold`: if GK provides no statistically/economically meaningful OOS improvement, reject the publication narrative that GK is an essential regime-classification component.
3. **Parameter perturbation.** Perturb FER thresholds/lookback, Hurst window/threshold, ADX threshold, AMO threshold, and KAMA period by approximately ±20% without test-set retuning. Reject as parameter-fragile if more than half of neighboring configurations flip net return sign or full-gate median OOS Sharpe falls to `<= 0`.
4. **Point-in-time audit.** Reconstruct every rolling statistic strictly from data available through the confirmed signal close and execute no earlier than the next tradable event. Any material advantage that exists only under same-bar optimistic fills is a timing falsification.
5. **Cost stress.** Include maker/taker fees, observed spread, 5/10/20 bps round-trip slippage stresses, and perpetual funding. Reject practical tradability if median OOS net Sharpe is `<= 0` at 10 bps round-trip friction on BTC/ETH majors.
6. **Regime placebo.** Circularly shift the LOW/TRANSITION/HIGH state series within quarterly blocks while preserving the AMO/KAMA signals. Reject the claimed gating mechanism if the true regime gate fails to beat the 95th percentile of placebo-gated net Sharpe outcomes.
7. **Cross-venue/regime stability.** Repeat on at least two liquid venues and split bull/bear, high/low volatility, and weekend/weekday periods. Reject claims of broad robustness if profitability is confined to one venue or one narrow market regime.

## Crypto portability

**unproven**.

The mechanism only needs bar data and is mechanically portable to 24/7 crypto markets, but the reviewed source does not provide crypto-specific OOS evidence. A crypto implementation must freeze UTC bar boundaries, distinguish spot from perpetual prices, model exchange-specific fees/spreads/slippage, account for funding and mark/index mechanics, handle fragmented venue liquidity, and avoid survivorship in symbol selection. Portability does not imply approval to trade.

## Limitations

- not independently reproduced
- indicator rather than executable strategy; exit, sizing, and fill semantics are underspecified
- no fixed source-reported performance result accepted as evidence
- three material prose-versus-code contradictions identified
- synthetic Hurst is explicitly approximate
- no crypto-specific empirical validation
- no explicit fees, spread, slippage, funding, impact, capacity, or latency model
- no source-defined venue, universe, or timestamp convention
- multi-filter construction carries material data-mining and parameter-fragility risk

## Implementation status

`not-implemented`. No quantitative runtime, strategy family, historical backtest, Paper, Testnet, or Live implementation was created or executed in this Scout cycle.

## Adoption boundary

`research-only`; `adoption: not-approved`; `approval_scope: research-only`.

This staging record is a source-code-audited research hypothesis, not validation of profitability and not authorization for implementation or trading.

## Related Wiki records

No stable Hermes Wiki Brain strategy path was fabricated. Materially adjacent staging-repository records reviewed for deduplication include `crypto-perpetual-order-flow-entropy-microstructure-taker-cost-falsification-2026-09-13.md`, which provides negative evidence that Shannon trade-sign entropy adds no incremental short-horizon crypto alpha, and `crypto-perpetual-pairs-trading-cointegration-hurst-halflife-walkforward-2026-09-12.md`, which uses a materially different Hurst anti-persistence mechanism for pair selection. Neither duplicates this FER/Hurst/ADX directional regime gate.

## Sources

1. `officialjackofalltrades`, **Entropic Regime Field [JOAT]**, TradingView public open-source Pine Script indicator, published June 5, 2026; page and full public source reviewed September 14, 2026. https://www.tradingview.com/script/NK5dYlr4-Entropic-Regime-Field-JOAT/
