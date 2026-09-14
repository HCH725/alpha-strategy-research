---
schema: strategy-research-record-v1
title: "INJ Dual-RSI DCA Profit-Armed Exit — Source-Code Audit"
created: 2026-09-15
updated: 2026-09-15
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - tradingview
  - dca
  - mean-reversion
  - rsi
  - source-code-audit
status: research-only
confidence: medium
source_as_of: 2026-09-15
sources:
  - "https://www.tradingview.com/script/VPIQUHD7-3Commas-Dual-RSI-DCA-INJ-Long-Strategy/"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The source describes maximum deployed capital as a structural risk cap, but the executable strategy has no adverse-price stop or maximum holding exit; capital allocation is bounded, loss is not bounded at the same percentage."
  - "The Pine backtest sizes averaging orders explicitly, while the webhook add-funds payload does not encode the Pine-computed averaging-order amount, so external-bot sizing parity is not established by the public source."
---

# INJ Dual-RSI DCA Profit-Armed Exit — Source-Code Audit

## Provenance

- **Primary source:** TradingView open-source strategy `[3Commas] Dual RSI DCA INJ - Long Strategy` by `3Commas`.
- **Stable public URL:** https://www.tradingview.com/script/VPIQUHD7-3Commas-Dual-RSI-DCA-INJ-Long-Strategy/
- **Publication:** TradingView page dated June 11; reviewed as of 2026-09-15. The source-reported backtest window is 2026-03-16 through 2026-06-11.
- **Direct source inspection:** the public description and all 186 lines of the current Pine Script v6 source were inspected directly. This record normalizes the logic and does not reproduce the script.
- **Deduplication / incremental value:** repository and read-only Hermes Wiki Brain searches found generic RSI, DCA, and dual-RSI material, including `[[quant/cga-agent-multi-agent-genetic-algorithm-crypto-scalping-2026-09-05]]`, but no record for this TradingView source or the same oversold-entry + geometric averaging ladder + profit-gated overbought-rollover exit. Incremental value also comes from source-code execution evidence: one averaging order can fire per host bar, the webhook amount is not source-parity with Pine sizing by construction, and the advertised deployment cap is not a loss cap.

## Economic mechanism

### Source-reported

The author frames the strategy as a long-only crypto-perpetual mean-reversion system. A lower-timeframe RSI recovery from oversold conditions starts a position; progressively larger averaging orders add exposure as price moves adversely; after the position is at least a minimum percentage above its running average entry, an RSI rollover from overbought closes the entire position. The intended behavior is to buy local downside exhaustion, lower the average cost during further adverse drift, and allow profitable momentum to continue until an overbought rollover.

The source describes the five-order ladder as "soft compounding" and characterizes the approximately 9.93% maximum capital deployment at defaults as a structural risk cap.

### Research interpretation

The falsifiable alpha hypothesis is **conditional short-horizon mean reversion after an oversold RSI recovery**, with an asymmetric exit that requires both positive mark-to-average-entry distance and momentum rollover. The DCA ladder is primarily exposure/risk geometry rather than independent predictive alpha; its contribution must therefore be separated from the entry signal in ablation.

The risk claim requires narrowing. The source code bounds **cash/notional deployed by the strategy defaults**, not maximum adverse loss. With no stop-loss or maximum holding exit, a persistent downtrend can keep the strategy fully invested while losses continue; on a live perpetual, leverage/liquidation settings outside this Pine strategy can further change downside. Therefore "~9.93% deployed" must not be interpreted as "~9.93% maximum account loss."

## Signal

The current source is sufficiently explicit to reconstruct the Pine strategy mechanics, subject to TradingView broker-emulator semantics and the external webhook caveat below.

- **Instrument / default context:** calibrated for INJ/USDT perpetual on a 3-minute chart. The source description names `BYBIT:INJUSDT.P`; the executable Pine itself uses `syminfo.tickerid`, so signal data and Strategy Tester orders follow the chart symbol/venue actually loaded.
- **Formation timestamp / availability:** `calc_on_every_tick=false`; entry/exit logic is evaluated on host-bar updates and orders use `process_orders_on_close=true`. Lower-timeframe RSI values are requested with `barmerge.lookahead_off`. The source explicitly defines crosses by comparing the current requested RSI value with its value on the prior **host bar**, so a lower-timeframe cross that completes and reverses inside one larger host bar can be missed. Default host and requested timeframe are both 3 minutes.
- **Timezone / bar convention:** no custom signal timezone is specified; chart/exchange bar timestamps govern the RSI series. The optional date-filter literals are UTC. A reproduction must preserve the source venue's 3-minute candle boundaries rather than silently re-aggregate in another timezone.
- **Entry RSI:** RSI length 14 on requested timeframe `3`; long base entry when prior host-bar requested RSI is below 31 and current requested RSI is at or above 31, provided the strategy is flat and has no open trade.
- **Base order:** default cash amount 90 USDT. Market order is default; an optional limit-at-current-close mode is available. Quantity is computed as `90 / close` at signal evaluation.
- **Averaging-order count:** default 5; source permits input range 0–10.
- **First averaging-order size:** 110 USDT.
- **Averaging-order size progression:** order `k` uses `110 * 1.25^(k-1)` USDT. At five defaults this is approximately 110, 137.50, 171.88, 214.84, and 268.55 USDT.
- **Averaging-order price ladder:** first cumulative deviation is 1.30% below the **base-entry fill price**. Each subsequent incremental deviation step is multiplied by 1.3 before being added, yielding default cumulative thresholds approximately 1.30%, 2.99%, 5.18%, 8.04%, and 11.75% below base entry.
- **Averaging trigger:** if in position and the next averaging level is unfilled, trigger when host-bar `close <= baseEntry * (1 - cumulativeDeviation/100)`.
- **One-order-per-bar behavior:** the executable block evaluates only the next unfilled averaging order once per host bar. If a bar closes through multiple unused ladder levels, the source does **not** submit all crossed levels on that bar; it advances by one order and can add later orders only on subsequent qualifying bars. This is source-code behavior and materially differs from a generic resting-ladder interpretation.
- **Exit RSI:** RSI length 14 on requested timeframe `3`; rollover condition is prior host-bar requested RSI above 69 and current requested RSI at or below 69.
- **Profit gate:** compute current `strategy.position_avg_price`; exit is armed only when host-bar close is at least 2.4% above that running average entry.
- **Exit:** when both the 2.4% profit gate and RSI cross-down condition are true, close the full strategy position. There is no fixed take-profit order independent of RSI.
- **Stop / adverse exit:** none in the source. No maximum holding period is defined.
- **Re-entry:** after the position becomes flat, base-entry and averaging-order state reset; a fresh RSI cross-up is required for the next base entry.
- **Optional backtest window:** the Pine input exists but is disabled by default. Its literal defaults are 2025-11-16 UTC through 2030-01-01 UTC, so the source-reported 2026-03-16 to 2026-06-11 result window is not enforced by default code alone.
- **Position-size boundary:** default base plus five averaging orders totals about 992.77 USDT on 10,000 USDT initial capital, approximately 9.93% of initial capital before P&L effects.

## Required data

- Crypto perpetual OHLCV for the chart symbol, with default research target INJ/USDT perpetual.
- 3-minute close series sufficient to warm up RSI(14); if host timeframe differs from requested RSI timeframe, exact TradingView `request.security(..., lookahead_off)` host-bar sampling semantics are required for source parity.
- Exchange/venue identity and 3-minute candle boundary convention.
- Trading costs: source uses 0.08% commission and 3 ticks of slippage in Strategy Tester.
- For a live-perpetual interpretation: funding history, mark/index prices, contract multiplier, margin mode, leverage, liquidation rules, tick/lot size, and venue fees are additionally required; these are not fully modeled by the source backtest.
- Missing bars must not be silently imputed. A reproduction should fail or explicitly document venue gaps because RSI-cross timing and ladder triggers are path dependent.

## Execution assumptions

### Source-reported / source-coded

- `initial_capital = 10000`.
- Cash sizing; default base order 90 USDT.
- Pyramiding limit 6, consistent with one base plus five default averaging orders.
- Commission: 0.08%.
- Slippage: 3 ticks.
- `process_orders_on_close=true` and `calc_on_every_tick=false`.
- Market base order by default; optional limit base at the signal bar close.
- Averaging orders are generated only after an existing position is observed and use market `strategy.entry` calls when a closing-price deviation threshold is met.
- No stop-loss.
- Source-reported perpetual funding is omitted from the backtest.

### External-bot parity boundary

The Pine backtest computes each averaging-order quantity from the explicit geometric USDT progression. However, the current webhook `add_funds_in_quote` message contains the action, bot identifier/token, delay and pair, but does **not** encode the Pine-computed `aoQtyUsdt`. The base-entry webhook likewise does not encode the Pine base cash amount. Therefore exact execution parity between the TradingView backtest and a connected DCA bot depends on external bot configuration and is **underspecified** by this public source. No claim of end-to-end amount parity is warranted without a separately observed bot configuration.

## Evidence

### Source-reported

For the stated INJ perpetual 3-minute sample from 2026-03-16 through 2026-06-11, the TradingView page reports:

- initial capital: 10,000 USDT;
- net profit: +223.16 USDT (+2.23%);
- maximum equity drawdown: 204.77 USDT (1.98%);
- closed trades: 102;
- profitable trades: 84.31% (86 / 102);
- profit factor: 15.628;
- commission: 0.08%;
- slippage: 3 ticks;
- perpetual funding: not included.

These figures are source-reported TradingView results only. The page itself notes the short sample and warns that sustained downtrends can fill the entire averaging ladder and leave the position holding losses.

### Independently reproduced

not independently reproduced

### Negative evidence

- **Extremely short calibration/evidence window:** the reported sample is roughly 2.9 months and only 102 closed trades on one altcoin perpetual. It does not establish robustness across crypto regimes, venues, or assets.
- **No adverse-price exit:** after all averaging orders are filled, the strategy has no source-coded stop or maximum holding exit. A persistent decline can keep capital tied up and losses growing.
- **Deployment cap is not a loss cap:** ~9.93% is the default cash deployed relative to initial capital, not a guaranteed maximum percentage loss. The source wording risks conflating position allocation with loss-at-risk.
- **Funding omission:** perpetual funding is not included. A long-only position with potentially indefinite holding can be materially affected by sustained positive funding.
- **One averaging order per host bar:** a gap through multiple ladder thresholds is represented as at most one new AO on that bar, which can materially differ from a live ladder of resting orders or from an implementation that fills every crossed rung immediately.
- **Webhook sizing parity is not established:** the add-funds payload does not transmit the Pine-computed averaging amount, so the claim that one webhook drives the bot end-to-end does not by itself prove that live DCA sizing matches the backtest.
- **Backtest-window provenance gap:** the page reports a March-to-June 2026 test, while the Pine date filter is disabled by default and its literal defaults cover a different broad period. Exact reproduction therefore also requires the chart/test-window state used for the published report.
- **Parameter-selection risk:** thresholds 31/69, 2.4% minimum profit, the ladder geometry, and INJ 3-minute calibration are source choices with no independent evidence here that they were pre-registered rather than selected after search.

## Falsification plan

1. **Exact Pine source-parity test.** Use INJ/USDT perpetual 3-minute data on the source venue and reproduce every base entry, AO index, average price, and exit under the same fee/slippage semantics. `research-defined falsification threshold`: any persistent unexplained timestamp/state mismatch invalidates the reproduction before profitability analysis; action: stop alpha evaluation and resolve execution semantics.
2. **Walk-forward OOS test.** Freeze the source defaults and evaluate multiple non-overlapping future and earlier regimes without retuning. Compare net return, Sharpe, max drawdown, time-in-market, median holding time, and fraction of deals reaching AO5 against a simple RSI-entry/no-DCA control and buy-and-hold. `research-defined falsification threshold`: if net OOS Sharpe is <= 0 or the strategy fails to improve drawdown-adjusted return over both controls across the majority of predeclared folds, reject the alpha hypothesis.
3. **DCA ablation.** Hold the RSI entry/exit logic constant and compare (a) base-only, (b) equal-size ladder, and (c) source geometric ladder. `research-defined falsification threshold`: if the geometric ladder does not improve net OOS utility after controlling for average gross exposure, classify DCA geometry as risk reshaping rather than incremental alpha.
4. **Strong-downtrend stress.** Include prolonged crypto bear/downtrend and gap regimes. Measure maximum adverse excursion, maximum holding duration, capital lock-up, liquidation distance under realistic leverage, and worst loss after AO5. `research-defined falsification threshold`: if loss-at-risk exceeds a predeclared portfolio budget or liquidation occurs under intended venue leverage, reject the no-stop deployment configuration; action: do not promote unchanged source rules.
5. **Multi-threshold gap test.** Replay bars that cross 2+ unused AO thresholds and compare source one-AO-per-bar behavior with a research-proposed resting-ladder implementation that can fill every crossed level. `research-defined falsification threshold`: if performance/risk metrics materially change sign or ranking between these execution models, treat published backtest results as execution-model dependent rather than robust evidence.
6. **Funding/cost stress.** Add point-in-time venue funding, taker fees, bid/ask spread, tick-size slippage and latency. `research-defined falsification threshold`: if net OOS excess return over controls is <= 0 under a realistic cost case, reject tradeability.
7. **Parameter perturbation.** Predeclare neighborhoods around RSI 31/69, minimum profit 2.4%, first deviation 1.3%, step multiplier 1.3, and size multiplier 1.25. `research-defined falsification threshold`: if positive OOS performance is confined to the exact published combination and the majority of nearby combinations fail, classify the result as parameter-fragile.
8. **Cross-asset / venue test.** Apply frozen rules to a predeclared basket of liquid USDT perpetuals and at least two venues where data quality permits. `research-defined falsification threshold`: if the effect is isolated to INJ or one venue and disappears after cost normalization, reject broad crypto portability.
9. **Webhook parity audit.** Configure a paper-only DCA bot with documented amounts and compare emitted TradingView events with bot-side requested quote amounts. `research-defined falsification threshold`: any systematic mismatch between Pine base/AO cash sizing and bot-side sizing means the public webhook path is not source-parity; action: keep implementation unapproved until configuration is made explicit.

## Crypto portability

**Direct, but unproven beyond the calibrated instrument.** The source is explicitly designed for crypto perpetuals and calibrated to INJ/USDT on 3-minute bars. The mechanism can be tested on other liquid perpetuals, but portability is not established by the source. Relevant risks include 24/7 candle-boundary consistency, venue-specific liquidity/ticks, contract specifications, funding, mark/index divergence, exchange leverage/liquidation rules, and asset-specific mean-reversion behavior.

## Limitations

- `contested: true` because bounded deployment is described as a structural risk cap even though the executable strategy has no loss-bounding adverse exit, and because direct webhook execution does not encode the Pine-computed cash sizes needed to establish backtest/live sizing parity.
- The alpha contribution of RSI reversal is not separated from the exposure-increasing DCA ladder in the source-reported performance.
- `not independently reproduced`.
- Single asset, single short sample, and likely parameter-selection risk.
- Perpetual funding is omitted from source results.
- Live leverage/margin/liquidation state is outside the Pine strategy and therefore underspecified for production risk.
- Cross detection uses host-bar snapshots of requested RSI, not all intrabar lower-timeframe crosses when host timeframe is larger.
- Exact published backtest-window state is not encoded by the default date-filter inputs.
- Webhook amount parity is underspecified without external bot configuration.

## Implementation status

`not-implemented` — this Scout record only normalizes and audits the public TradingView strategy. It does not modify the quantitative runtime, create a strategy implementation task, run a backtest, or configure a DCA bot.

## Adoption boundary

`not-approved` / `research-only` — presence in this staging repository is not evidence of validated alpha and does not authorize Paper, Testnet, or Live deployment. Any later implementation or adoption requires separate review, independent source-parity reproduction, leakage/cost/funding tests, robust OOS falsification, and explicit approval.

## Related Wiki records

- `[[quant/cga-agent-multi-agent-genetic-algorithm-crypto-scalping-2026-09-05]]` — related RSI-based crypto signal research, but its Dual RSI construction is fast/slow RSI crossover with adaptive filters, materially different from this oversold-entry / overbought-exit DCA construction.
- `[[quant/production-dca-p2-integrated-closure-2026-09-04]]` — related DCA execution/accounting boundary work; it is operational infrastructure evidence, not evidence that this TradingView alpha works.

## Sources

1. TradingView, `3Commas`, `[3Commas] Dual RSI DCA INJ - Long Strategy`, public open-source Pine Script v6, reviewed 2026-09-15: https://www.tradingview.com/script/VPIQUHD7-3Commas-Dual-RSI-DCA-INJ-Long-Strategy/
