---
schema: strategy-research-record-v1
title: "Hurst Future Lines of Demarcation Cycle-State Strategy — TradingView Source-Code Audit"
created: 2026-09-14
updated: 2026-09-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
  - hurst-cycle
  - cycle-state
  - trend-following
status: research-only
confidence: medium
source_as_of: 2026-09-14
sources:
  - "https://www.tradingview.com/script/4B9sbgmC-Hurst-Future-Lines-of-Demarcation-Strategy/"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The TradingView description illustrates a 20/40/80-day Signal/Trade/Trend FLD hierarchy, while the reviewed current Pine source defaults are 5/20/80 bars; source comments also describe the quarter/trade defaults as 20/40 days even though the executable inputs are 5 and 20."
---

# Hurst Future Lines of Demarcation Cycle-State Strategy — TradingView Source-Code Audit

## Provenance

- **Primary source:** BarefootJoey, `Hurst Future Lines of Demarcation Strategy`, public TradingView open-source Pine Script v5 strategy.
- **Stable public URL:** https://www.tradingview.com/script/4B9sbgmC-Hurst-Future-Lines-of-Demarcation-Strategy/
- **TradingView publication/update metadata:** published April 2024; page shows update on 2024-04-08.
- **Source inspection:** public description and the complete current 99-line Pine source were inspected directly on 2026-09-14.
- **Canonical-source identity:** TradingView script ID `4B9sbgmC`.
- **Repository deduplication:** a repository-wide pre-write search for `future line of demarcation`, `FLD`, `hurst cycle`, `cycle hurst`, and `demarcation` found no existing materially matching strategy record. This therefore clears the current incremental-write threshold as a distinct signal-construction family and as a source-code contradiction audit.

## Economic mechanism

### Source-reported

The author attributes the strategy to J. M. Hurst's Future Line of Demarcation concept. The stated idea is that price interaction with half-cycle-shifted price curves can identify cycle peaks/troughs, distinguish directional "cascading" FLD structure from tangled consolidation, and provide entry/exit context. The page presents a three-scale hierarchy: a faster Signal FLD, a Trade FLD for the cycle being traded, and a slower Trend FLD.

### Research interpretation

The executable source is best normalized as a **multi-horizon lagged-price state machine**, not as evidence that a hidden periodic cycle has been estimated. With smoothing disabled, each FLD is simply the selected source (`ohlc4` by default) lagged by half of a user-chosen cycle length. The relative ordering of the three lagged values defines an eight-state phase/trend classification. Entries occur only when price crosses the fast lagged reference while the state machine is in the most strongly aligned bullish or bearish phase.

The falsifiable mechanism is therefore:

1. **Multi-horizon ordering:** if recent price levels remain ordered above or below progressively slower lagged references, directional persistence may dominate mean reversion.
2. **Phase-transition trigger:** a cross of current `ohlc4` through the fast lagged reference may identify renewed movement in the direction implied by the ordered lag structure.
3. **Cycle-label caveat:** calling the horizons "Hurst cycles" does not by itself establish periodicity. The current source uses fixed user inputs rather than estimating a dominant cycle from data.

## Signal

**Specification status:** source code is exact enough to reconstruct the current default strategy logic, subject to TradingView broker-emulator execution semantics. Page prose and source defaults are materially inconsistent, so the record is contested.

### Formation timestamp and availability

- `source = ohlc4` by default.
- All signal components are computed on the active chart timeframe.
- With default Pine strategy behavior, conditions are evaluated after a bar is calculated; no `calc_on_every_tick` or `process_orders_on_close` override is declared in the reviewed `strategy()` call.
- Therefore a historical reproduction should treat a signal formed at bar close as becoming executable under TradingView's default broker-emulator timing rather than assuming an impossible earlier same-bar fill.

### Lookback / cycle construction

Source-reported executable defaults from the reviewed Pine:

- Signal cycle input `cyc_q = 5` bars; strategy reference `signal = FLD_out[round(cyc_q / 2)]`.
- Trade cycle input `cyc = 20` bars; strategy reference `trade = FLD_out[round(cyc / 2)]`.
- Trend cycle input `cyc_d = 80` bars; strategy reference `trend = FLD_out[round(cyc_d / 2)]`.
- `smoothFLD = false` by default, so `FLD_out = SMA(source, 1)`, which is effectively the source itself.
- Optional smoothing uses `SMA(source, FLDsmooth)` with default `FLDsmooth = 5` when enabled.

The TradingView page describes a 20/40/80-day example and the code comments refer to 20-day and 40-day defaults for the first two horizons, but the executable input defaults are 5 and 20. This contradiction must not be silently repaired.

### State machine

The current source defines the following relevant states:

- **State 1 (A):** `signal > trade > trend`.
- **State 5 (E):** `signal < trade < trend`.
- **State 6 (F):** after State 5, current `price < signal`.

Other intermediate A-through-H states classify transitions between the three FLDs and current price, but the actual entry rules use only State 1 for long entries and State 6 for short entries.

### Entry

- **Long:** `crossover(price, signal)` while `state == 1`.
- **Short:** `crossunder(price, signal)` while `state == 6`.
- `price = source`, therefore default entry comparisons use `ohlc4`, not `close`.
- Source does not declare pyramiding; reproduction should use TradingView's default strategy pyramiding behavior unless testing a deliberately modified variant.

### Exit

Two selectable close-trigger inputs are defined. Their defaults are:

- `close_buy_in_1 = 'Price'`
- `close_buy_in_2 = 'Trade'`

Therefore, under defaults:

- **Exit long:** while long, `crossunder(price, trade)`.
- **Exit short:** while short, `crossover(price, trade)`.

The user may instead select Price, Signal FLD, Trade FLD, Trend FLD, or None for each side of the crossover pair. Those alternative configurations are source-supported parameterizations, not separate validated strategies.

### Holding / re-entry

- No fixed maximum holding period is declared.
- Positions persist until the configured close crossover occurs or an opposite-entry reversal is processed under TradingView strategy semantics.
- Re-entry occurs only on a fresh qualifying crossover and state condition.

### Position sizing and strategy defaults

Source-reported from the current `strategy()` declaration:

- initial capital: `$100,000`;
- quantity type: percent of equity;
- default quantity: `5%` of equity per entry;
- commission: `0.02%`;
- slippage: `1` tick.

No leverage or margin model is explicitly declared in the reviewed code.

## Required data

- **Instrument/universe:** source is symbol-agnostic; no fixed universe is specified.
- **Venue:** chart-selected TradingView venue/feed; no venue-selection rule is specified.
- **Market type:** not constrained by source; may be spot, futures, perpetuals, equities, or other continuous chart instruments.
- **Timeframe:** chart timeframe; the page's explanatory example uses "day" cycles, but the Pine inputs are raw bar counts and therefore change meaning across chart timeframes.
- **Fields:** OHLC is sufficient for default `ohlc4`; volume is not used.
- **Timestamp convention:** TradingView chart/session timestamps; timezone/session handling is not explicitly normalized by source.
- **Point-in-time rule:** use only completed bars available at signal formation; all FLD strategy references are backward lags in the reviewed source. The positive `plot(..., offset=...)` values are visual shifts and must not be mistaken for future-known data in a reproduction.
- **Missing-data assumptions:** unspecified.

## Execution assumptions

### Source-reported

- Strategy sizing is 5% of equity.
- Commission is 0.02%.
- Slippage is 1 tick.
- Orders are generated with `strategy.entry` / `strategy.close` market-style strategy calls; no explicit limit/stop price is supplied.

### Research interpretation

- A source-parity reproduction must preserve TradingView's default strategy order timing and reversal behavior rather than assuming fills at the same price used to form the signal.
- Spread, market impact, partial fills, exchange outages, funding, borrow, and liquidation mechanics are not modeled by the source.
- The 1-tick slippage assumption is not economically comparable across instruments with different tick values or across crypto venues.
- Capacity is unaddressed.

## Evidence

### Source-reported

The source page explains the Hurst FLD framework and publishes the complete strategy code. It reports no stable Sharpe ratio, CAGR, win rate, profit factor, maximum drawdown, out-of-sample statistic, or crypto-specific performance figure in the reviewed public text. No profitability claim is promoted into evidence here.

### Independently reproduced

not independently reproduced

### Negative evidence

- **Description/code contradiction:** the page's 20/40/80 example and source comments do not match the executable 5/20/80 default inputs.
- **Cycle-identification gap:** the code does not estimate a dominant cycle; it applies fixed bar-count lags chosen by the user.
- **Timeframe sensitivity:** the same numeric input means radically different economic horizons on 15-minute, 1-hour, 4-hour, or daily charts.
- **Execution simplification:** commission and one-tick slippage are modeled, but spread, impact, funding/borrow, and venue failure are omitted.
- **No independent performance evidence:** no reproducible OOS or cross-venue result was identified in the reviewed source.

## Falsification plan

1. **Source-parity audit.** Data: the same TradingView symbol/timeframe and bar history used for a chosen reference chart. Reproduce `ohlc4`, optional smoothing, half-cycle lags, A-through-H state transitions, entries, exits, commissions, and one-tick slippage. **research-defined falsification threshold:** any systematic mismatch in state/entry/exit timestamps after accounting for documented TradingView broker-emulator timing invalidates downstream testing; fix parity first.
2. **Cycle-label ablation.** Compare source defaults `5/20/80` against simple non-Hurst lag triplets with the same approximate spacing and against a conventional multi-horizon trend baseline. Metric: after-cost Sharpe and net expectancy on held-out data. **research-defined falsification threshold:** if FLD ordering does not outperform the simpler lagged-price baseline by at least 0.10 Sharpe on a majority of pre-specified OOS panels, reject the claim that the Hurst labeling adds incremental predictive structure.
3. **Parameter perturbation.** Test ±20% perturbations around all three horizon inputs while preserving ordering. **research-defined falsification threshold:** if the sign of net expectancy flips for more than half of neighboring parameter combinations, classify the rule as parameter-fragile.
4. **Timeframe invariance test.** Use BTC and ETH on 1h, 4h, and 1d bars with horizon semantics fixed in clock time rather than raw bar count. **research-defined falsification threshold:** if performance disappears when equivalent real-time horizons are preserved across bar sizes, treat any chart-timeframe result as discretization-dependent rather than cycle evidence.
5. **Walk-forward OOS.** Freeze parameters on an initial period and evaluate at least three non-overlapping forward regimes containing bull, bear, and sideways conditions. **research-defined falsification threshold:** if after-cost Sharpe is non-positive in two or more forward regimes, reject a general directional-alpha claim.
6. **Cost stress.** Increase modeled all-in friction from source commission/slippage to venue-realistic taker fees plus 1, 2, and 5 bps additional slippage per side. **research-defined falsification threshold:** if expected return becomes non-positive at a realistic liquid BTC/ETH taker-cost setting, reject tradability for that configuration.
7. **State-machine ablation.** Compare fast-FLD crossover alone versus crossover gated by State 1/6. **research-defined falsification threshold:** if gating does not improve OOS after-cost expectancy or drawdown on a majority of panels, reject the incremental value of the multi-horizon state classifier.
8. **Placebo timing test.** Randomly circular-shift the state series relative to entry crossovers while preserving marginal state frequencies. **research-defined falsification threshold:** if the true alignment does not exceed the 95th percentile of placebo after-cost expectancy, reject timing specificity.

## Crypto portability

**unproven**

The logic can technically be applied to crypto OHLC bars, but the reviewed source does not provide crypto-specific empirical evidence. Portability risks include:

- 24/7 bars make "day" labels dependent on UTC/session boundary choices;
- a fixed bar-count cycle may not preserve economic meaning across 1h/4h/1d crypto charts;
- spot and perpetual prices can diverge during funding/liquidation stress;
- perpetual funding is omitted from source economics;
- venue fragmentation can change crossover timing and slippage;
- one-tick slippage is not comparable across Binance, OKX, Bybit, CME, or spot venues.

Any BTC/ETH operationalization beyond literal source parity is `research-proposed` until independently tested.

## Limitations

- contested source documentation because default horizon prose/comments conflict with executable inputs;
- not independently reproduced;
- no source-reported OOS evidence;
- no crypto-specific validation;
- fixed cycle lengths rather than data-estimated dominant cycles;
- timeframe semantics are underspecified because inputs are bars while prose describes days;
- no explicit spread, impact, funding, borrow, capacity, latency, or failure model;
- no declared maximum holding period;
- results may be sensitive to TradingView order-fill semantics and selected chart feed.

## Implementation status

`not-implemented`.

No implementation has been created in the quantitative research runtime. This Scout run did not backtest the strategy, modify PyBroker/Nautilus or any current runtime, create an implementation task, or produce Paper/Testnet/Live execution code.

## Adoption boundary

This record is `research-only`, `not-implemented`, and `not-approved`. It is a normalized public-source capture plus source-code audit, not evidence that FLD trading is profitable or suitable for deployment. Presence in the staging repository does not authorize implementation, paper trading, testnet, or live trading.

## Related Wiki records

No exact Hermes Wiki Brain strategy-research record matching TradingView source `4B9sbgmC` or the same three-horizon FLD A-through-H state machine was identified by the pre-write repository search. No Wiki link is fabricated here.

## Sources

1. BarefootJoey, **Hurst Future Lines of Demarcation Strategy**, TradingView public open-source Pine Script v5 strategy, updated 2024-04-08; public description and complete current 99-line source inspected directly on 2026-09-14: https://www.tradingview.com/script/4B9sbgmC-Hurst-Future-Lines-of-Demarcation-Strategy/
