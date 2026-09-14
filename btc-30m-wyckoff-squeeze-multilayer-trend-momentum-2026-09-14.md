---
schema: strategy-research-record-v1
title: "BTC 30m Wyckoff Squeeze Multi-Layer Trend/Momentum Strategy"
created: 2026-09-14
updated: 2026-09-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-03-30
sources:
  - "https://www.tradingview.com/script/e9D83CQS-Fenix-Wyckoff-Squeeze-BTC-30m/"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# BTC 30m Wyckoff Squeeze Multi-Layer Trend/Momentum Strategy

## Provenance

- **Primary source:** TradingView public open-source strategy, *Fenix Wyckoff Squeeze BTC 30m*, author `kamil_vaslavsky1`.
- **Stable URL:** https://www.tradingview.com/script/e9D83CQS-Fenix-Wyckoff-Squeeze-BTC-30m/
- **Publication/update information:** published March 27, 2026; page shows an update on March 30, 2026.
- **Source as-of:** 2026-03-30; page re-read by this Scout on 2026-09-14.
- **Public-use status:** TradingView marks the script open source. This record normalizes the rules and does not reproduce the Pine source.
- **Pre-write dedup:** repository search found no prior record citing this TradingView URL, author, Phoenix TCI combination, or the same complete multi-layer rule set.

## Economic mechanism

### Source-reported

The author describes a selective trend-following breakout system for BTCUSDC on 30-minute bars. The intended mechanism is that a volatility squeeze captures compression before directional expansion; a higher-timeframe EMA avoids counter-trend entries; HMA slope confirms local momentum acceleration; and a Phoenix composite of TCI, MoneyFlow, RSI, and LSMA attempts to require broad momentum agreement before entry. An optional ADX filter blocks low-trend regimes. The author characterizes the system as low-frequency and asymmetric: a low win rate is accepted in exchange for larger winners than losers.

### Research interpretation

The falsifiable hypothesis is that **post-compression directional expansion has higher persistence when volatility release, higher-timeframe trend, short-horizon slope, volume-weighted pressure, and oscillator direction agree simultaneously**. The components play distinct roles rather than representing one indicator stack:

- Regime/setup: Bollinger Bands inside Keltner Channels, followed by squeeze release.
- Macro direction: 2-hour EMA relative to price.
- Local acceleration: HMA slope.
- Momentum/participation confirmation: Phoenix TCI + MoneyFlow + RSI + LSMA direction.
- Optional regime gate: ADX.
- Exit/risk: ATR trailing stop, ATR target, maximum holding bars, optional Phoenix reversal.

Whether this confluence adds alpha beyond a simpler squeeze + trend baseline is unverified and should be tested by ablation. The source explicitly states the default parameters were optimized for BTCUSDC 30m, so parameter-selection bias is a material alternative explanation.

## Signal

**Signal reconstruction status: underspecified.** The TradingView public description provides the component logic and some defaults, but not every numerical Pine input needed to reproduce the exact default strategy without reading the full source code in TradingView's source-code panel. No missing value is upgraded here into a source-reported fact.

- **Formation timestamp:** 30-minute confirmed bar close. Source states `process_orders_on_close: true`; all `request.security()` calls use lookahead off.
- **Universe / default instrument:** BTCUSDC on Binance, 30-minute chart.
- **Long setup:**
  1. A Bollinger-Band / Keltner-Channel squeeze occurred within a configurable prior lookback and is releasing.
  2. Price is above the 2-hour EMA.
  3. HMA slope is rising.
  4. Phoenix TCI, MoneyFlow, and RSI simultaneously agree bullish.
  5. LSMA slope on the Phoenix composite agrees bullish.
  6. If enabled, ADX must be above its regime threshold; source-reported default threshold = 18.
- **Short setup:** mirror of the long rule: squeeze release, price below the 2-hour EMA, falling HMA slope, bearish Phoenix TCI/MoneyFlow/RSI agreement, bearish Phoenix LSMA slope, and optional ADX gate.
- **Higher-timeframe convention:** source recommends an HTF around 4× the entry timeframe; default is 2h for 30m entries.
- **Exit precedence:** source states multiple exit mechanisms run simultaneously and whichever triggers first closes the position:
  - ATR trailing stop;
  - fixed ATR take-profit set from entry;
  - maximum-hold-bars time exit;
  - optional Phoenix momentum-reversal exit.
- **Position sizing:** ATR-risk sizing targeting a fixed equity risk; source-reported default risk = 2% of equity, with size capped at 2× equity.
- **Known source-reported parameter defaults:** ADX threshold 18; risk per trade 2%; entry timeframe 30m; HTF EMA timeframe 2h; commission 0.1%; slippage 2 ticks.
- **Underspecified source parameters:** exact BB length/multiplier, KC length/multiplier, squeeze lookback, HMA length, HTF EMA length, Phoenix N1/N2/N3 lengths, RSI length/threshold convention, LSMA length, ATR length, ATR stop multiplier, ATR target multiplier, maximum hold bars, and volatility-adaptive scaling formula/default values are not numerically exposed in the reviewed public description. These must not be guessed.
- **Re-entry / overlap:** not fully specified in the reviewed description; underspecified.

## Required data

- **Instrument:** source default is Binance BTCUSDC; source also tags BTCUSDT as relevant but does not claim identical default performance.
- **Market type:** source text references Binance Futures taker fee assumptions, but the exact TradingView symbol/contract construction should be verified from the Pine source before implementation; mark contract type as underspecified.
- **Timeframe:** 30-minute entry bars; 2-hour higher-timeframe EMA by default.
- **Fields:** OHLCV sufficient for BB, KC/ATR, EMA, HMA, RSI, TCI, MoneyFlow, LSMA, and ADX/DMI.
- **Point-in-time:** confirmed 30m bar close; higher-timeframe `request.security()` lookahead disabled according to the source.
- **Timestamp / session:** crypto 24/7 bars; TradingView exchange timestamps and candle-boundary convention must be frozen during reproduction.
- **Missing data:** source does not specify stale/missing-bar handling; underspecified.
- **Funding:** not described in the source; omitted from reported backtest assumptions despite futures-oriented fee language.

## Execution assumptions

### Source-reported

- Orders are processed on confirmed bar close (`process_orders_on_close: true`).
- Higher-timeframe lookahead is explicitly off.
- Commission assumption: 0.1% per trade, described by the author as standard Binance Futures taker fee.
- Slippage assumption: 2 ticks.
- Pyramiding / simultaneous-position behavior is not stated in the reviewed description.
- Risk sizing uses ATR stop distance and fixed percentage of equity; default 2% risk; 2× equity size cap.

### Research interpretation

Before any implementation, fee semantics need clarification: “0.1% per trade” may mean per order/fill rather than round trip, and Binance fee schedules depend on account tier, maker/taker status, product, and time. Funding, spread, latency, mark-price liquidation, and market impact are absent from the public description and therefore cannot be assumed negligible.

## Evidence

### Source-reported

The TradingView author states that the default parameters were tested on **BTCUSDC 30m from December 2018 through March 2026**, spanning 507 completed trades. The author reports an approximate **28% win rate** under the default settings and explicitly explains that the thesis depends on large winner/loser asymmetry rather than a high hit rate. The page also states 0.1% commission, 2-tick slippage, confirmed-bar-close order processing, and lookahead disabled. No exact net return, Sharpe, CAGR, max drawdown, profit factor, or average-win/average-loss statistic is provided in the reviewed public description, so none is asserted here. Source: https://www.tradingview.com/script/e9D83CQS-Fenix-Wyckoff-Squeeze-BTC-30m/

### Independently reproduced

not independently reproduced

### Negative evidence

The source itself supplies several important caveats:

- Defaults are specifically **optimized for BTCUSDC 30m**, creating clear parameter-selection / in-sample overfit risk.
- The author recommends re-tuning BB, KC, ATR, Phoenix, HMA, HTF EMA, squeeze-lookback, and ADX parameters for other symbols/timeframes, which weakens claims of universal robustness.
- Approximate 28% win rate implies substantial dependence on tail winners and exit execution.
- Funding, spread, impact, liquidation mechanics, and venue-specific futures execution are not documented in the reviewed description.
- No independent reproduction or out-of-sample holdout is reported on the page.

## Falsification plan

1. **Exact-source reconstruction gate:** obtain the public Pine source and freeze every omitted default parameter. Failure rule: if the exact source cannot be reconstructed without guessing, keep the record research-only and do not implement.
2. **Walk-forward / OOS test:** freeze parameters on an earlier training window and test later BTCUSDC/BTCUSDT periods. **Research-defined falsification threshold:** net expectancy ≤ 0 after costs or materially negative OOS Sharpe rejects the alpha claim.
3. **Ablation:** compare full system against (a) squeeze release only, (b) squeeze + HTF EMA, (c) squeeze + HTF EMA + HMA, and (d) Phoenix confirmation alone. **Research-defined failure rule:** if the full confluence does not improve risk-adjusted OOS performance or drawdown versus simpler baselines, reject the added-component contribution.
4. **Parameter perturbation:** vary BB/KC, Phoenix, HMA, EMA, ATR, ADX, and squeeze-lookback values around defaults. Failure: profitability confined to a narrow parameter island indicates overfit.
5. **Cost stress:** retest taker fees at 1×/1.5×/2× assumed costs plus realistic spread/slippage and perpetual funding. Failure: edge disappearing under modest cost stress weakens tradability.
6. **Venue / symbol portability:** compare BTCUSDC and BTCUSDT across at least two major venues with point-in-time listing history. Failure: sign reversal or collapse outside the source symbol implies venue/symbol specificity.
7. **Regime breakdown:** separate bull, bear, high-volatility, low-volatility, and range regimes. Failure: returns concentrated in one historical episode without persistence weakens the claimed general trend-following mechanism.
8. **Signal timing audit:** verify higher-timeframe EMA values are only available after the HTF bar is confirmed and that no Pine recalculation behavior creates hidden lookahead.

## Crypto portability

**direct**, because the source is explicitly designed and source-tested on BTC crypto data.

Important crypto-specific risks remain:

- BTCUSDC versus BTCUSDT quote/collateral differences;
- spot versus perpetual contract ambiguity in the reviewed description;
- perpetual funding and mark/index-price mechanics are omitted;
- 24/7 candle boundaries can change indicator states across venues/timezones;
- venue fee tiers and maker/taker execution vary;
- size cap in “2× equity” does not itself model liquidation or maintenance margin;
- stablecoin-specific venue and depeg risk are not addressed.

## Limitations

- Public TradingView source description is rich in component logic but numerically incomplete; exact default reconstruction is **underspecified** until the Pine inputs are read directly.
- Single-author TradingView publication; no peer review.
- Source reports optimization on the same BTCUSDC 30m market used for the headline trade count / win rate.
- No explicit OOS, walk-forward, placebo, parameter-stability, or cross-venue evidence is reported.
- No exact net-return, Sharpe, CAGR, max-drawdown, profit-factor, or capacity evidence is available in the reviewed description.
- Hybrid complexity creates multiple-degrees-of-freedom risk; component ablation is mandatory before attributing alpha to the full confluence.
- Funding and futures-specific execution details are incomplete.

## Implementation status

`not-implemented`. This Scout did not copy or execute the Pine code, did not run a backtest, and did not modify the quantitative runtime. No PyBroker, NautilusTrader, Paper, Testnet, or Live task is authorized by this record.

## Adoption boundary

`research-only` / `not-implemented` / `not-approved` / `approval_scope: research-only`.

The record captures a public TradingView hypothesis with enough structural detail to justify later source-code reconstruction and falsification work. It does **not** establish profitable alpha, does not approve implementation, and does not authorize Paper/Testnet/Live execution.

## Related Wiki records

No exact duplicate TradingView source or materially identical full rule set was found in the staging repository during the pre-write search. Conceptually adjacent records include general volatility-breakout, regime-filter, and trend-following families, but none matched the source's complete squeeze + HTF EMA + HMA + Phoenix TCI/MoneyFlow/RSI + LSMA + ADX construction closely enough to treat this as a duplicate.

## Sources

- TradingView, `kamil_vaslavsky1`, *Fenix Wyckoff Squeeze BTC 30m*, public open-source strategy, published March 27, 2026 and updated March 30, 2026: https://www.tradingview.com/script/e9D83CQS-Fenix-Wyckoff-Squeeze-BTC-30m/
