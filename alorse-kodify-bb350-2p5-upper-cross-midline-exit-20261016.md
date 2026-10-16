---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Kodify BB350 +2.5σ upper-band strict cross with SMA350 exit, Alorse-curated variant"
created: 2026-10-16
updated: 2026-10-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-16
sources:
  - https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/mean-reversion/Bollinger%20Breakout%20%5Bkodify%5D.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Kodify BB350 +2.5σ upper-band strict cross with SMA350 exit, Alorse-curated variant

## Provenance

Full Pine v4 script personally inspected: `Alorse/pinescript-strategies@8fb3837ddcd137f1450c3e82d654ff3df24d54d5`, path `strategies/mean-reversion/Bollinger Breakout [kodify].pine`: https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/mean-reversion/Bollinger%20Breakout%20%5Bkodify%5D.pine. Script itself says **author KODIFY.NET**, so credit Kodify as original author and Alorse as public repository curator. `pyramiding=0`, source default 10% current equity, capital 1000 USD, 0.01% source commission and default next-bar-OPEN market fills. No source performance/daily-chart settings embedded.

**Very close existing mechanism:** `bollinger-band-breakout-long-midline-exit-btcusdt-1d-2026-10-11.md` is also an upper Bollinger crossover with midline crossunder long exit, sourced from FMZ/ChaoZhang, but source defaults BB20 and **1.5σ**, whereas Kodify source independently sets **smaLength=350, stdLength=350, upper offset=2.5σ** (distinct source identity and default sampling horizon/risk exposure). This is a separate source-default parameterization of a known signal **family**, not a claim to invent an unrelated edge. If main policy dedup treats all param variants as duplicates, this PR should be closed as duplicate with precise main-file reference, not pushed to main. The original is kept intact, no performance screening.

## Economic mechanism and source signals

- `smaLength=350`, `stdLength=350`; `ubOffset=2.5`, `lbOffset=2.5` independently provided even though both 2.5 default. `smaValue=sma(close,350)`; `stdDev=stdev(close,350)`; `upperBand=smaValue+2.5*stdDev`; `lowerBand=smaValue-2.5*stdDev`.
- `showLong=true`, `showShort=false` source defaults.
- `enterLong=crossover(close,upperBand)` := prior close<=prior upperBand AND current close>upperBand (strict current); `exitLong=crossunder(close,smaValue)` := prior close>=prior SMA350 AND current close<SMA350.
- Source commands `strategy.entry('EL',long=true,when=enterLong)`, `strategy.close('EL',when=exitLong)`. `enterShort=crossunder(close,lowerBand)`, `exitShort=crossover(close,smaValue)` exist but `showShort=false` means their `strategy.entry('ES')`/close block does not execute in source-default rule. Never invent a default short.
- One long / flat; no price stops, target orders, trailing, expiry, cooldown, pyramiding, safety orders or cross-asset inputs. Subsequent breakout cross after flat can reenter; duplicate entry while long rejected. Entry/exit mutually exclusive at same bar since upperBand>=SMA and strict close cannot both cross above upper and below SMA.
- Conservative researcher-selected 351 complete bars flat warmup for both 350-bar rolling SMA/STDEV and previous strict-cross comparison. Source built-ins may compute earlier partial values; the 351 fence is explicit research derivative, not author rule. No future security/MTF/repainting; only trailing completed close.

## Execution assumptions — separate spot research derivative

Source-default indicator and direction pinned unchanged; research version uses `binance BTC-USDT 1h` **spot** single pair, completed t signal cached and applied on t+1 simulated CLOSE using existing MARKET `OrderExecutorSimulator` with no t+1 signal leak. Pine default source fill t+1 OPEN, therefore this is openly a different execution derivative, not original TradingView trade-price equivalence. Account starts 1000 USDT, fixed 100 USDT order per new signal (instead of source 10% changing equity, declared sizing derivative), quantity rounded down by spot connector step, reject below min-notional/no historical candle, exits sell exactly current held BTC. One-way `trade_cost=0.0001` research fee proxy matching nominal source 0.01% percent input; actual Binance fee, spread/slippage not assumed verified. No futures funding/leveraged risk because explicit spot venue. House 3x/5x and DCA campaign is not source-native.

Gate 5 bounded **existing** Hummingbot engine proof: `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` committed September 20 2026 and `hummingbot/VERSION=dev-2.17.0`, matches canonical baseline package 20260920/version. `BacktestingEngineBase.run_backtesting(controller_config,start,end,backtesting_resolution="1h",trade_cost=0.0001)` loads `BacktestingDataProvider` `binance_BTC-USDT_1h` completed OHLC and trading-rule quantizers, per-row `simulate_execution` uses `controller.determine_executor_actions()` and routes `OrderExecutorConfig MARKET` `CreateExecutorAction` to `OrderExecutorSimulator`. MARKET fills at first simulated row's CLOSE with `trade_cost*filled_amount_quote`; `POSITION_HOLD` `BacktestPositionHold._process_order` nets prior BUY with equal SELL, provides avg cost/realized PnL/cum fee. `controllers/generic/pmm_mister.py` demonstrates native MARKET OrderExecutor actions; specific BB350/2.5 strategy controller not implemented yet (as frontmatter says), no new runner/framework.

Pre-existing tests at **same version** inspected but not run: `test_backtest_position_hold.py` `test_buy_sell_netting`, `test_full_netting_closes_position`, `test_netted_position_realized_pnl_in_summary`; `test_backtesting_final_tick_ledger.py` spot Binance OrderExecutorConfig position-hold and terminal receipt; `test_backtesting_engine_directional.py` exchange historical candles and signal/action simulation. No strategy-level HB backtest executed, no binary digest claimed.

## Evidence

Original full Kodify Pine strategy code read from Alorse-curated repository and compared with existing `bollinger-band-breakout-long-midline-exit` on main. This is a **parameter-distinct implementation of the SAME broad family**, disclosed for independent dedup review. No author performance/effectiveness inherited.

## Falsification plan

Verify both 350 inputs, both 2.5σ offsets, strict cross above upper for entry and strict cross below SMA350 for exit, no default Short. Native t signal -> t+1 close market fill, fee0.0001 side, one held BTC unit with quantity netting, 351 bar warmup. Confirm exact source is not already main; if policy treats parameter changes within a family as not new strategy, reject gracefully without claiming some different edge.

## Crypto portability

Single-frame price series, no mandatory author timeframe; 1h spot evaluation only one derived setting, no implied futures 42-cell parity.

## Limitations

BB350 1h uses long history and lag, can whipsaw; potential family duplicate of existing BB breakout record is openly stated. No stop; fill differs from original next-open, fixed capital differs from percent equity. Simulator does not price market impact.

## Implementation status

`not-implemented`; GitHub strategy document only, not Qlib/HB/backtest/n8n deployment.

## Adoption boundary

`research-only`, `not-approved`. Existing Reviewer must independently establish six Gate PASS **and material difference sufficiently unique to current pool**, then merge exact reviewed head, or close as a proven duplicate.

## Sources

- Primary https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/mean-reversion/Bollinger%20Breakout%20%5Bkodify%5D.pine
- Existing similar record https://github.com/HCH725/alpha-strategy-research/blob/main/bollinger-band-breakout-long-midline-exit-btcusdt-1d-2026-10-11.md
- Hummingbot VERSION https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/VERSION
- Native tests https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3/test/hummingbot/strategy_v2/backtesting
- Policy https://github.com/HCH725/alpha-strategy-research/blob/main/.github/HB_READY_REVIEW.md
