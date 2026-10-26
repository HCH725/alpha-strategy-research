---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade CrossEMA EMA28/48 alignment with raw StochRSI threshold gate, independent BTC-USDT spot 1h long-flat derivative
created: 2026-10-26
updated: 2026-10-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - freqtrade
status: research-only
confidence: medium
source_as_of: 2023-11-05
sources:
  - https://github.com/davidzr/freqtrade-strategies/blob/9623c1f3d8c7f60c8b411010fa26377e6ca99ab9/strategies/CrossEMAStrategy/CrossEMAStrategy.py
  - https://github.com/davidzr/freqtrade-strategies/tree/9623c1f3d8c7f60c8b411010fa26377e6ca99ab9
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade CrossEMA EMA28/48 alignment with raw StochRSI threshold gate — independent BTC-USDT spot 1h long-flat derivative

## Provenance

**Primary source (immutable, read end to end this cycle):** repository `davidzr/freqtrade-strategies`, pinned commit `9623c1f3d8c7f60c8b411010fa26377e6ca99ab9` (committed 2023-11-05), exact file path `strategies/CrossEMAStrategy/CrossEMAStrategy.py`. File size **7825 bytes**; GitHub contents API at the pin returns blob SHA `9c233f99da23a155ba373e70e88dcb397439d5a3` and size 7825, both matching an independent local `git hash-object`/byte count of the fetched bytes (SHA256 `28bc245bdb5840def41dea43171fe871d919c76690892d1c044fadbfcfdbda0e`). Class `CrossEMAStrategy(IStrategy)`, `INTERFACE_VERSION = 2`, docstring attribution "Cross EMA + stoch RSI / By Crypto Robot" with upstream pointer `https://github.com/CryptoRobotFr/TrueStrategy/` and a source-embedded freqtrade backtest summary table (ETH/USDT, 2017-08-19 → 2021-08-08, 250 trades, `--max-open-trades 1`, `--stake-amount unlimited`; cited below only for the cited facts, never adopted as performance evidence).

**Source-verbatim trading configuration (quoted, not paraphrased):** `timeframe = '1h'`; `minimal_roi = {"0": 100 # inactive}`; `stoploss = -0.99 # inactive`; `trailing_stop = False` (all trailing options commented/unconfigured); `process_only_new_candles = False`; `use_sell_signal = True`; `sell_profit_only = False`; `ignore_roi_if_buy_signal = False`; `startup_candle_count: int = 49 # EMA 48 + 1`; `order_types = {'buy': 'limit', 'sell': 'limit', 'stoploss': 'market', 'stoploss_on_exchange': False}`; `order_time_in_force = {'buy': 'gtc', 'sell': 'gtc'}`; `buy_stoch_rsi = DecimalParameter(0.5, 1, decimals=3, default=0.8, space="buy")`; `sell_stoch_rsi = DecimalParameter(0, 0.5, decimals=3, default=0.2, space="sell")`; `informative_pairs()` returns `[]`. Absent anywhere in the file (whole-file token census): `can_short`, `position_stacking`, `protections`, `use_custom_stoploss`, `custom_stoploss`, `trailing_stop_positive`, `stoploss_on_exchange = True`, `buy_params`/`sell_params` dicts, `leverage`, `DCA`, `cooldown`, any `sell_profit_only = True`, any short/sell-short order call (exactly one `'buy'] = 1` leg, exactly one `'sell'] = 1` leg). The author comments mark both ROI and stoploss inactive; this derivative takes the author at his word (see adaptations).

**Source-verbatim signal code (quoted):** indicators use the `ta` Python package only (`import ta`, never `talib`/`qtpylib` in this file): `dataframe['stoch_rsi'] = ta.momentum.stochrsi(dataframe['close'])`; `dataframe['ema28'] = ta.trend.ema_indicator(dataframe['close'], 28)`; `dataframe['ema48'] = ta.trend.ema_indicator(dataframe['close'], 48)`. Buy leg: `(ema28 > ema48) & (stoch_rsi < buy_stoch_rsi.value) & (volume > 0)` → `'buy'] = 1`. Sell leg: `(ema28 < ema48) & (stoch_rsi > sell_stoch_rsi.value) & (volume > 0)` → `'sell'] = 1`. Both legs are strict level conjunctions on the same completed bar; no cross operator, no shift, no second timeframe, no volume indicator beyond the `> 0` guard. The `ta` package version is pinned nowhere by the source; the exact frozen formulas are transcribed below from `ta` **0.11.0** (downloaded and read this cycle, `setup.py: version="0.11.0"`) and owned by this derivative as disclosed researcher freeze, never attributed to the source author.

**Independent derivative — NOT source-native or lossless:** researcher-declared adaptations are exactly: (1) market **Binance BTC-USDT spot 1h** (the author's own backtest ran ETH/USDT; no timeframe adaptation — the source is already 1h); (2) **completed-bar close-effective MARKET** fills instead of the source limit/GTC order types; (3) **no ROI exit and no stoploss leg** — both source fields are kept verbatim above and both carry the author's own `# inactive` comments, so the drop follows stated author intent rather than inventing risk economics (this is the opposite of retaining an ambiguous risk formula: there is no retained percentage to miscompute, and no fee-adjusted-versus-gross return basis to choose); (4) fixed **0.001 BTC** sizing on 10,000 USDT unborrowed cash with hypothetical **0.01% per-side** simulator cost instead of the author's `--stake-amount unlimited` / framework-default sizing; (5) warmup adopts the source's own `startup_candle_count = 49` ("EMA 48 + 1") as 49 consecutive valid completed 1h bars, flat before that by record rule; (6) the `ta`-0.11.0 formula freeze below (defaults `window=14, smooth1=3, smooth2=3, fillna=False`; EMA `span=N, min_periods=N, adjust=False`; RSI Wilder-style `alpha=1/14, min_periods=14, adjust=False` with `emadn == 0 → 100`). All six choices can change source trades and are evaluated only as this independently specified executable research strategy.

**Immutable identity:** `FT:CrossEMAStrategy:davidzr@9623c1f3 | independent-derived-v1:2026-10-26 | EMA28/EMA48-level:ta0.11.0 | rawStochRSI14:BUY<0.8/SELL>0.2 | volume>0 | BinanceSpot:BTC-USDT:1h:LONG-FLAT:0.001BTC | completed-close-MARKET:trade_cost=0.0001`. Any change in windows, thresholds, operators, market, clock, size, cost, state, or fill model is a different research version.

**Deduplication on main SHA `01424f9a35b29ccbeb3386030c7efd0552bcf6b3`:** current main has **355** root-level strategy Markdown records and README pool count **355**. Working-tree filename/content searches for `crossema`, `TrueStrategy`, `CryptoRobot`, `ema28`, `ema48`, `buy_stoch_rsi`, and `stochrsi(dataframe` return **zero** records; GitHub PR/issue search for `CrossEMA` and `TrueStrategy` across this repository returns **zero** items ever (open and closed). All **10** currently open `research/*` PRs were inspected (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend, #89 Chandelier, #92 SSL channel, #251 Swift 2YMA, #304 forven CCI, #331 AdxSmas, #350 ClucMay, #353 Heracles Keltner-Donchian) — none cites this source or any EMA28/48-plus-StochRSI rule. The closed NOT_LOSSLESS freqtrade PRs (#453 Bandtastic 15m, #478 RobotradingBody 4h body-expansion) are different indicators, timeframes, and blockers. Closest main mechanisms are (a) `alorse-stochrsi-supertrend-ema200-long-20261016.md`, which trades a **smoothed K-over-D crossover** gated by Supertrend/EMA200 — this candidate never computes K/D lines and never trades a cross; (b) `stoch-rsi-kd-zone-cross-two-sided-btcusdt-1h-2026-10-12.md`, a **two-sided K/D zone-cross reversal** — this candidate is long-flat with level/threshold legs and an EMA-alignment gate; (c) `freqtrade-adx-momentum-di-gated-long-flat-btcusdt-1h-2026-10-20.md`, an ADX/DI/MOM level system with no oscillator gate at all. No duplicate source or materially identical normalized rule was identified: no pool record combines a dual-EMA **level alignment** with a **raw (unsmoothed) StochRSI threshold** and a volume-positivity guard on one timeframe.

## Economic mechanism

### Source-reported

The author's construction bets that a medium-term EMA alignment (`ema28 > ema48`) identifies an uptrend worth holding, while a raw StochRSI print below 0.8 refuses entries printed at the very top of the 14-bar RSI range (late-chase filter), and the mirror pair (downtrend alignment plus StochRSI above 0.2) ends exposure. The source-embedded backtest table (ETH/USDT 1h, 2017-08-19 → 2021-08-08, 250 trades, `--max-open-trades 1`) exists in-file; its return/drawdown/profit figures are **not adopted** — they ship with no trade-level trace, no cost schedule, and `stake-amount unlimited` sizing, so per the exact-numbers rule this record claims no source-reported performance beyond the quoted table-existence facts.

### Research interpretation

Trend-alignment hold with an exhaustion-aware gate, long-only: the position persists through every bar the fast EMA stays above the slow one regardless of oscillator wiggles (no exit until the alignment itself flips AND the oscillator confirms non-oversold), so chop inside an intact alignment costs only opportunity while a genuine regime flip exits on the first jointly-confirming bar. Unlike cross-edge EMA systems the legs are levels — after a failed BUY the same level re-fires on the next qualifying bar with no hidden cooldown, and unlike K/D-cross StochRSI systems there is no smoothing lag between the RSI range print and the gate. The volume `> 0` guard is a data-validity condition, not a volume signal. Missing a protective stop is a material loss risk, not an implicit engine default.

## Signal

**Market/data clock:** exactly one actual Binance spot `BTC-USDT` **1h** OHLCV stream. Each exchange opening timestamp `T[t]` labels an hourly bar whose data become available only at **T[t]+3600 seconds**. Require consecutive opening timestamps separated by 3600 seconds; O/H/L/C finite and positive, H>=max(O,C), L<=min(O,C), V finite and nonnegative. No incomplete bar, forward-fill, future bar, or synthetic price is accepted. The rule reads **Close** (indicator chain) and **Volume** (positivity guard only); Open/High/Low are never read.

**Frozen arithmetic (`ta` 0.11.0-verbatim, bare-default calls):** for t>=1, `up[t]=max(C[t]-C[t-1],0)`, `dn[t]=max(C[t-1]-C[t],0)` (the package's `diff.where(diff>0,0.0)` / `-diff.where(diff<0,0.0)` reduce to exactly this, with the t=0 NaN resolving to 0.0 through the `where` fallback). `EMAup[t]` / `EMAdn[t]` are recursive `ewm(alpha=1/14, min_periods=14, adjust=False)` means over up/dn (seeded at the first observation, masked NaN for the first 13 prints, first valid index 13). `RSI[t] = 100` if `EMAdn[t]==0` else `100-(100/(1+EMAup[t]/EMAdn[t]))`. `rawS[t] = (RSI[t]-min14[t])/(max14[t]-min14[t])` with min/max over `RSI[t-13..t]`; **no smoothing is applied** — the functional `ta.momentum.stochrsi()` returns the `.stochrsi()` series, and the `smooth1/smooth2` arguments are accepted-but-unused by that path (verified in package source: only `.stochrsi_k()`/`.stochrsi_d()` consume them). Any undefined input or a zero denominator (`max14==min14`, i.e. a flat RSI window) prints **NaN**, never 0 or a carried value. `ema28[t]` / `ema48[t]` are recursive `ewm(span=N, min_periods=N, adjust=False)` means over closes (first valid indices 27 and 47). Structural full definability therefore starts at bar index 47.

**Legs (pinned defaults `buy_stoch_rsi=0.8`, `sell_stoch_rsi=0.2`; the hyperopt ranges `0.5–1` / `0–0.5` are menus the record does not take):** `BUY[t] = ema28[t]>ema48[t] AND rawS[t]<0.8 AND V[t]>0`; `SELL[t] = ema28[t]<ema48[t] AND rawS[t]>0.2 AND V[t]>0`. All six comparisons are **strict**; any NaN operand makes its conjunction False (never trades on undefined prints). Entry and exit can never co-fire: they require contradictory strict EMA orderings on the same bar, disjoint by arithmetic, so no tie-break is required. The legs are levels, not edges: a persistent BUY print while LONG is a hold (no-op), and a persistent SELL print while FLAT is a no-op.

**Warmup:** require **49 consecutive fully completed valid hourly bars** (the source's own `startup_candle_count`, comment "EMA 48 + 1"), counting the first input as bar 0, before the first eligible decision. Begin with 10,000 USDT, zero BTC, FLAT, no pending order, and no pre-warmup inferred position. First eligible t is 48.

**Deterministic per-completed-bar order/state machine:**
1. At most one outstanding order. Reconcile any prior simulated executor's actual confirmed fill/failed status before evaluating new actions; creating an order alone never changes the confirmed position. No trade decision before the bar's completion time.
2. If confirmed LONG and a SELL retry is outstanding after a failed previous exit, issue exactly one new SELL of the confirmed held quantity on the **next valid completed bar**; do not require the original exit conjunction to persist. If LONG with no retry and SELL is true, issue one SELL for the full confirmed BTC position. Ignore BUY on every exit bar.
3. If confirmed FLAT and no SELL occurred this bar, if BUY is true and the available quote cash covers `0.001*C[t]*(1+0.0001)`, issue one BUY for 0.001 BTC; otherwise stay FLAT. After a failed BUY, re-evaluate the same level on the next valid bar without a hidden cooldown; no intra-bar retries.
4. An idealized full confirmed BUY fill sets LONG and deducts cash; a rejected/failed BUY leaves FLAT. An idealized full confirmed SELL sets FLAT and credits net cash; a rejected/failed SELL leaves LONG and sets the next-bar retry flag. Partial or indeterminate fills are outside the verified bounded model and **abort as unsupported**, never silently assume full size or fabricate a price. There is no same-bar exit-and-reentry; a new BUY is eligible only on a later completed bar. A confirmed LONG ignores further BUY prints.
5. If neither leg is due, HOLD. No discretionary/manual action. On the final available bar, mark any still-open LONG at the **last observed valid close** for research valuation; do not invent a terminal SELL.

**Explicitly disabled:** ROI exit (source `{"0": 100 # inactive}` — dropped, not re-based); stoploss (source `-0.99 # inactive` — dropped, not re-based); trailing stop (source False); SHORT (no `can_short` ships; freqtrade spot default is long-only); perpetual/futures, leverage, margin/borrowing, funding, pyramiding/position-stacking, DCA/safety orders, simultaneous positions, cooldown/protections, custom stoploss, partial targets, take-profit limit, time exit, maker/limit/next-open/intrabar orders, informative-pair inputs, dynamic sizing, compounding, session filter, hidden controller risk defaults, and forced end-of-data liquidation. The sell-signal leg is the only risk exit. Missing a protective stop is a material loss risk, not an implicit engine default.

**Data failure:** a missing, duplicate, invalid, nonconsecutive or undefined required bar after warmup invalidates the entire research run. Abort; do not let an engine `dropna` erase a gap, fall back to a constant price, or assume a fill.

## Required data

Single real Binance BTC-USDT **spot 1h** OHLCV with exchange **open timestamps** and actual O/H/L/C/V; only Close (indicator chain) and Volume (positivity guard) gate orders. No multi-timeframe alignment, cross-market series, external fundamentals, order book, funding, mark price, fitted model, or future price is required. One market is a deliberate derivative scope, **not** a policy admission whitelist.

## Execution assumptions

**Pinned Hummingbot engine inspected this cycle via connected GitHub:** package `20260920`, VERSION `dev-2.17.0` (VERSION file re-read at the pin `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, reads `dev-2.17.0`). Prior independent package/source mapping evidence is in Alpha PR #414/#417; this cycle did **not** rehash the package wheel and does not assert fresh binary identity.

**Actual bounded data and controller path:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` maps **`1h`** in the `INTERVALS` bidict (verified this cycle at the pin — the mapping list runs `1s/1m/3m/5m/15m/30m/1h/2h/4h/6h/8h/12h/1d/3d/1w/1M`); `binance_spot_candles.py::_parse_rest_candles` maps exchange `row[0]` open timestamp and `row[1..5]` OHLCV. `strategy_v2/backtesting/backtesting_engine_base.py::run_backtesting` initializes feed/controller, then `simulate_execution` iterates processed rows, calls `update_state(row)`, `controller.determine_executor_actions()`, and `simulate_executor()`. `OrderExecutorConfig` in `strategy_v2/executors/order_executor/data_types.py` supports `connector_name="binance"`, `trading_pair="BTC-USDT"`, `side=TradeType.BUY/SELL`, `amount=Decimal("0.001")`, `position_action=OPEN/CLOSE`, `execution_strategy=MARKET`, `price=None`, `leverage=1`. A strategy-specific controller is **not implemented**; these are verified primitives, not a claim that this record is already wired into Hummingbot.

**Fill/position model:** `strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` MARKET path uses the first supplied historical row's actual `close` as full-fill price; `filled_amount_quote = amount*close`, `cum_fees_quote=trade_cost*notional`, `CloseType.POSITION_HOLD`. `BacktestPositionHold` in `backtesting_engine_base.py` nets opposing BUY/SELL base fills, tracks weighted average cost, gross realized/unrealized PnL, and fees **separately**. A MARKET SELL reduces the same BTC spot inventory; no short inventory is opened. The engine's raw candle timestamp is the **opening label**, so the economic decision and simulated fill must be recorded as **opening timestamp+3600**, not as an open-time executable trade. This is an idealized **historical completed-close** convention only — a disclosed adaptation away from the source limit/GTC types — and real post-close market orders cannot be assumed to fill at that past close.

**Cash and costs:** pass explicit `run_backtesting(trade_cost=0.0001)`, a hypothetical **0.01% quote-notional fee per side**; this is not a measured Binance fee schedule or a source parameter (the source models no costs). Maintain independent unborrowed cash `cash_after_buy=cash_before-Q*Pbuy*(1+0.0001)` and `cash_after_sell=cash_before+Q*Psell*(1-0.0001)`, Q=0.001 BTC, and require sufficient cash before BUY. Net realized matched PnL `Q*(Psell-Pbuy)-0.0001*Q*(Pbuy+Psell)`; do not mistake gross `BacktestPositionHold.realized_pnl_quote` for net-of-fee performance. Real exchange fee tier, quantity/price precision, min notional, slippage, spread, latency, and partial fills remain **unverified** and are not simulated as realized zero costs. Spot funding is **not applicable**; do not label zero perpetual funding as observed. No futures leverage/margin claim is made.

**Required engine safeguards:** `BacktestingEngineBase` exposes terminated executors to controllers for only **3600 simulated seconds** by default; use `terminated_executors_window=None` or an equivalent full-run confirmed-fill ledger so fill state is not lost across hourly bars. `prepare_market_data` calls `dropna`, so continuity/validity must be checked before entering the engine. `BacktestingDataProvider.get_price_by_type` can fall back to `Decimal("1")` when a price is missing; **prohibit this path** for strategy fills and abort on missing observed prices. No unverified maker, next-open, intrabar, perpetual or real-time fill path is claimed.

## Evidence

### Source-reported

The immutable source file (`davidzr/freqtrade-strategies@9623c1f3`, `strategies/CrossEMAStrategy/CrossEMAStrategy.py`, 7825 bytes, blob `9c233f99da23a155ba373e70e88dcb397439d5a3`) states: Crypto Robot "Cross EMA + stoch RSI" construction; 1h timeframe; `startup_candle_count = 49 # EMA 48 + 1`; `ta.momentum.stochrsi(close)` with hyperopt-pinned defaults 0.8/0.2; `ta.trend.ema_indicator(close, 28/48)`; the strict BUY (`ema28>ema48 & stoch_rsi<0.8 & volume>0`) and SELL (`ema28<ema48 & stoch_rsi>0.2 & volume>0`) conjunctions; ROI/stoploss both commented `# inactive`; trailing off; `use_sell_signal = True`; long-only by default (no short leg, no `can_short`); and an in-file backtest summary (ETH/USDT, 2017-08-19 → 2021-08-08, 250 trades, `--max-open-trades 1`) whose economics are not adopted.

### Independently reproduced

**No original-source trade reproduction, Qlib/Hummingbot backtest, event-level parity, return, Sharpe, or survivor claim.** This cycle verified the pinned Hummingbot source files and existing research-only MARKET/POSITION_HOLD/fee primitives; verified the `ta` 0.11.0 `stochrsi`/`RSIIndicator`/`_ema` sources quoted above; verified the GitHub blob SHA/size against the pin; and ran a stdlib-only scratch self-check of the frozen formulas confirming BUY/SELL disjointness (asserted per bar), flat-market NaN with zero flat entries and no crash, single BUY then single SELL alternation on a rise/fall regime pair, strict alternation with at most one order per bar across five fuzz seeds, warmup gating, and zero-volume no-trade — pure logic validation, not a backtest. No runtime trade, Paper/Testnet/Live or deployment was performed.

### Negative evidence

No K/D (%K/%D) lines exist anywhere in this construction — the gate is the raw unsmoothed StochRSI, so smoothed-crossover failure modes do not apply and must not be imputed. The hyperopt ranges are menus, not rules; only the pinned defaults are specified. The author's backtest figures are disclaimed as evidence. The `ta` package version is unpinned by the source, so any other `ta` release's drift is out of scope for this frozen derivative. A no-stop long-only system can suffer large losses in a flip-then-grind regime where the alignment flips late.

## Falsification plan

After independent admission and downstream selection, test strict-vs-nonstrict threshold edges (0.8/0.2 equality prints nothing), flat-RSI-window NaN (0/0 prints hold/no-enter by construction), EMA equality bars (neither leg fires), persistent-level hold with no re-entry while LONG, failed BUY/SELL next-bar retry, confirmed fill vs order intent, missing hourly bar, warmup boundary at bar 48, raw-open vs completed-close clock, cash insufficiency and fee separation. If the execution primitive/path proves new or unverified, perform one representative Hummingbot/Qlib event-level comparison **before** large-scale screening; otherwise reuse verified primitives. Test IS/OOS net-of-declared-cost profitability separately from HB_READY.

## Crypto portability

Only the declared independent **BTC-USDT spot 1h** version is assessed. The author's ETH/USDT demonstration pair is a quoted source fact, not a portability claim; equities, seven-coin 1h/4h/1d and 3x/5x futures/DCA campaign assumptions are **not** imported. Any leverage, funding, market, timeframe, DCA, or execution change requires a separately declared derived research identity; no blanket admission bans are inferred from these choices.

## Limitations

Research-only, no executable controller, no Pine equivalent (freqtrade Python source only), no source-native trade equivalence (six disclosed adaptations), no verified realized market fee/slippage, no partial-fill or live-price guarantee, no independently reproduced performance, no Qlib parity. A no-stop strategy can suffer large losses. The historical same-close fill is a pinned **simulation convention**, not proof of real tradability. HB_READY PASS is a **Scout admission proposal pending independent Hermes Auditor review**, not a self-certified deployment or profit claim.

## Implementation status

**not-implemented.** No strategy-specific executable, Qlib recipe, backtest, container action or trading action was created.

## Adoption boundary

**status: research-only; implementation_status: not-implemented; adoption: not-approved; approval_scope: research-only.** The independent Hermes Auditor GitHub Webhook Review owns exact-head PASS merge, verifiable source-fact remediation or NOT_LOSSLESS close. Scout never approves, merges, closes, edits README or bypasses review.

## Related Wiki records

None asserted; no Wiki change.

## Sources

- https://github.com/davidzr/freqtrade-strategies/blob/9623c1f3d8c7f60c8b411010fa26377e6ca99ab9/strategies/CrossEMAStrategy/CrossEMAStrategy.py — pinned primary source (7825 bytes, blob `9c233f99da23a155ba373e70e88dcb397439d5a3`, read live 2026-10-26); upstream credit `https://github.com/CryptoRobotFr/TrueStrategy/`
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned Hummingbot source (VERSION, spot candle constants/parser path, backtesting engine, order simulator, position-hold ledger)
- Independent package/source review evidence: https://github.com/HCH725/alpha-strategy-research/pull/414 and https://github.com/HCH725/alpha-strategy-research/pull/417
- `ta` 0.11.0 (`ta/momentum.py` StochRSIIndicator/RSIIndicator, `ta/trend.py` EMAIndicator, `ta/utils.py` `_ema`) — formula transcription source for the unpinned `ta` dependency
- Distinct main StochRSI-trigger family: https://github.com/HCH725/alpha-strategy-research/blob/01424f9a35b29ccbeb3386030c7efd0552bcf6b3/stoch-rsi-kd-zone-cross-two-sided-btcusdt-1h-2026-10-12.md
- Distinct main Alorse StochRSI-cross family: https://github.com/HCH725/alpha-strategy-research/blob/01424f9a35b29ccbeb3386030c7efd0552bcf6b3/alorse-stochrsi-supertrend-ema200-long-20261016.md
