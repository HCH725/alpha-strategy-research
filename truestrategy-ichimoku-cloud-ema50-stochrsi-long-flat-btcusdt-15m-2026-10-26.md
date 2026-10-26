---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TrueStrategy displaced-Ichimoku-cloud EMA50 StochRSI-gated long-flat derivative on BTC-USDT spot 15m
created: 2026-10-26
updated: 2026-10-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2021-12-03
sources:
  - https://github.com/CryptoRobotFr/TrueStrategy/blob/61b668c9adeb4e8506412452e9eab290b8086b37/ichiCloud-stoch-ema/%231binanceEGLD.py
  - https://github.com/CryptoRobotFr/TrueStrategy/tree/61b668c9adeb4e8506412452e9eab290b8086b37
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TrueStrategy displaced-Ichimoku-cloud EMA50 StochRSI-gated long-flat — independent BTC-USDT spot 15m derivative

## Provenance

**Primary source (immutable, read end to end this cycle):** repository `CryptoRobotFr/TrueStrategy`, pinned HEAD commit `61b668c9adeb4e8506412452e9eab290b8086b37` (committed 2021-12-03T22:00:52Z; verified this cycle as the repository's `main` head via the commits API), exact file path `ichiCloud-stoch-ema/#1binanceEGLD.py`. File size **2744 bytes**; GitHub contents API at the pin returns blob SHA `1daf683714e25c89677ce6452b481daa0253c131` and size 2744, matching an independent local `git hash-object`/byte count of the fetched bytes (SHA-256 `c5793895687c0ca90dc0a2d14784f652da1e14b80775977b13ca677afce766c9`). The file is 74 lines: a Binance-spot live-trading script (`from binance.client import Client`, `import ta`), pair `EGLDUSDT`, 15-minute klines (`Client.KLINE_INTERVAL_15MINUTE`, `"2 day ago UTC"`), market BUY/SELL calls only.

**Source-verbatim trading configuration (quoted, not paraphrased):** `pairSymbol = 'EGLDUSDT'`; `fiatSymbol = 'USDT'`; `cryptoSymbol = 'EGLD'`; `myTruncate = 2`; `truncate()` floors to 2 decimals (`floor(float(n)*10**decimals)/10**decimals`); klines `"2 day ago UTC"` at `KLINE_INTERVAL_15MINUTE`; `minToken = 5/actualPrice`; BUY gated on `float(fiatAmount) > 5`; SELL gated on `float(cryptoAmount) > minToken`. API key/secret are blank placeholders. Absent anywhere in the file (whole-file token census): `stop`, `stoploss`, `take_profit`, `trailing`, `ROI`, `short`, `leverage`, `DCA`, `cooldown`, `hyperopt`, `cross`, `informative`, `startup_candle`, any second timeframe, any `volume` read (zero `volume` tokens outside the dropped dataframe column list). The script reads the decision on `df['...'].iloc[-2]` (the last completed bar) through one `if / elif / else` chain ending in `print("No opportunity to take")`.

**Source-verbatim signal code (quoted):** `df['EMA50']=ta.trend.ema_indicator(df['close'], 50)`; `df['STOCH_RSI']=ta.momentum.stochrsi(df['close'])` (bare defaults); `df['SSA'] = ta.trend.ichimoku_a(df['high'],df['low'],3,38).shift(periods=48)`; `df['SSB'] = ta.trend.ichimoku_b(df['high'],df['low'],38,46).shift(periods=48)`. Buy leg: `(close[-2] > SSA[-2]) and (close[-2] > SSB[-2]) and (STOCH_RSI[-2] < 0.8) and (close[-2] > EMA50[-2])` → market BUY of the full fiat balance. Sell leg: `((close[-2] < SSA[-2]) or (close[-2] < SSB[-2])) and (STOCH_RSI[-2] > 0.2)` → market SELL of the full crypto balance. All comparisons are strict; no cross operator, no smoothing call, no second timeframe. The `ta` package version is pinned nowhere by the source; the exact frozen formulas are transcribed below from `ta` **0.11.0** (downloaded and read this cycle, `ta-0.11.0.tar.gz`) and owned by this derivative as disclosed researcher freeze, never attributed to the source author.

**Independent derivative — NOT source-native or lossless:** researcher-declared adaptations are exactly: (1) market **Binance BTC-USDT spot 15m** (the author traded EGLDUSDT; no timeframe adaptation — the source is already 15m); (2) **completed-bar close-effective MARKET** fills instead of the source live-market order calls; (3) **no stoploss, take-profit, trailing, ROI ladder, or time exit** — the source file contains none of these, so the drop follows the file rather than inventing risk economics (there is no retained percentage to miscompute); (4) fixed **0.001 BTC** sizing on 10,000 USDT unborrowed cash with hypothetical **0.01% per-side** simulator cost instead of the author's full-balance `truncate()` sizing with 5-USDT minimums; (5) warmup of **100 consecutive valid completed 15m bars**, flat before that by record rule (structural analysis: SSB first defined at bar index 93 = 45-bar Span-B window + 48-bar displacement; SSA at 85; EMA50 at 49; raw StochRSI at 26); (6) the `ta`-0.11.0 formula freeze below (Ichimoku `visual=False` → no internal shift, so the `.shift(48)` is the only displacement; rolling `min_periods` equal to each window since `fillna=False`; EMA `ewm(span=50, min_periods=50, adjust=False)`; RSI Wilder-style `alpha=1/14, min_periods=14, adjust=False` with `emadn == 0 → 100`; raw StochRSI `(RSI-min14)/(max14-min14)` with 0/0 → NaN, `smooth1/smooth2` accepted-but-unused on this path). All six choices can change source trades and are evaluated only as this independently specified executable research strategy.

**Immutable identity:** `TS:ichiCloud-stoch-ema:CryptoRobotFr@61b668c9 | independent-derived-v1:2026-10-26 | SSA(3,38)+48/SSB(38,46)+48:ta0.11.0-visualFalse | EMA50 | rawStochRSI14:BUY<0.8/SELL>0.2 | BinanceSpot:BTC-USDT:15m:LONG-FLAT:0.001BTC | completed-close-MARKET:trade_cost=0.0001`. Any change in windows, displacement, thresholds, operators, market, clock, size, cost, state, or fill model is a different research version.

**Deduplication on main SHA `a7f8a58`:** current main has **356** root-level strategy Markdown records and README pool count **356**. Working-tree filename/content searches for `EGLD`, `ichimoku_a`, `shift(48)`, `1daf6837`, and `binanceEGLD` return **zero** records. All **10** currently open `research/*` PRs were inspected (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend, #89 Chandelier, #92 SSL channel, #251 Swift 2YMA, #304 forven CCI, #331 AdxSmas, #350 ClucMay, #353 Heracles Keltner-Donchian) — none cites this source or any displaced-cloud-plus-EMA50 rule. The only pool record mentioning `TrueStrategy` is yesterday's `freqtrade-crossema-28-48-stochrsi-threshold` file, which cites it solely as upstream credit for a different pinned file (davidzr CrossEMA: dual-EMA **level alignment** 28/48, no cloud, no EMA50, 1h) — a different canonical file and a materially different normalized signal, not this rule. Closest main mechanisms are (a) `ichimoku-rsi-gated-reversal-btcusdt-1d-2026-10-08.md`, a **two-sided** Coinrule system on standard 9/26/52 windows with Tenkan/Kijun state, Chikou momentum and an RSI-50 gate — this candidate is long-flat, uses custom 3/38/46 windows with a 48-bar displacement, has no Tenkan/Kijun/Chikou legs, and gates on raw-StochRSI 0.8/0.2 plus EMA50; (b) `forven-ichimoku-tenkan-kijun-cross-cloud-gated-long-flat-btcusdt-1d-2026-10-24.md`, a Tenkan/Kijun **cross-edge** system with cross-down exit — this candidate trades strict cloud-position **levels** with an OR-leg signal exit; (c) `octa-ema-ichimoku-trend-long`, an EMA-ribbon system with no oscillator gate. The leftover branch `research/hermes-ichimoku-cloud-20261024-1037` is the merged head of the forven rule, not this source. No duplicate source or materially identical normalized rule was identified: no pool record combines a 48-bar-displaced custom-window Ichimoku cloud with an EMA50 trend leg and a raw-StochRSI dual threshold on one timeframe.

## Economic mechanism

### Source-reported

The source states no mechanism beyond its code: a `Tuto binance.md` sibling and a `BacktestEGLD.ipynb` notebook ship in the same folder but were **not read and are not adopted** — no source-reported performance, sample, or behavioural claim is made anywhere in the pinned 74-line script, so per the exact-numbers rule this record claims no source-reported performance at all.

### Research interpretation

Displaced-cloud breakout hold with a trend-plus-exhaustion double gate, long-only: requiring the close above **both** cloud spans (with the cloud read 48 bars displaced, i.e. a slow, sticky regime print) plus above EMA50 means the position only exists while price holds over two independent slow trend representations; the raw-StochRSI `< 0.8` entry refusal skips prints at the very top of the 14-bar RSI range (late-chase filter), while the OR-leg exit (close under **either** span, confirmed by StochRSI back above 0.2) ends exposure on the first jointly-confirming breakdown bar without waiting for a cross edge. Unlike cross-edge Ichimoku systems the legs are levels — a persistent BUY print while LONG is a hold with no hidden cooldown, and chop above an intact cloud costs only opportunity. Missing a protective stop is a material loss risk, not an implicit engine default.

## Signal

**Market/data clock:** exactly one actual Binance spot `BTC-USDT` **15m** OHLCV stream. Each exchange opening timestamp `T[t]` labels a 15-minute bar whose data become available only at **T[t]+900 seconds**. Require consecutive opening timestamps separated by 900 seconds; O/H/L/C finite and positive, H>=max(O,C), L<=min(O,C). No incomplete bar, forward-fill, future bar, or synthetic price is accepted. The rule reads **Close** (all legs), **High/Low** (cloud construction only); **Volume is never read** (zero volume tokens in the gating path), so no volume guard is required and none is claimed.

**Frozen arithmetic (`ta` 0.11.0-verbatim, bare-default calls, `fillna=False`):** `conv[t] = (HH(high,3)[t]+LL(low,3)[t])/2` (first valid index 2); `base[t] = (HH(high,38)[t]+LL(low,38)[t])/2` (first valid 37); `SSAraw[t] = (conv[t]+base[t])/2`, `SSA[t] = SSAraw[t-48]` (first valid 85); `SSBraw[t] = (HH(high,46)[t]+LL(low,46)[t])/2`, `SSB[t] = SSBraw[t-48]` (first valid 93). The functional `ichimoku_a/b` wrappers default to `visual=False`, verified in package source — **no internal shift is applied**, so the source's `.shift(periods=48)` is the sole displacement (a pure lag: the value read at row `t` was computed from rows `≤ t-48`, never a forward reference). `EMA50[t]` is recursive `ewm(span=50, min_periods=50, adjust=False)` over closes (first valid index 49). `up[t]=max(C[t]-C[t-1],0)`, `dn[t]=max(C[t-1]-C[t],0)`; `EMAup/EMAdn` are recursive `ewm(alpha=1/14, min_periods=14, adjust=False)` (first valid index 13); `RSI[t] = 100` if `EMAdn[t]==0` else `100-(100/(1+EMAup[t]/EMAdn[t]))`. `rawS[t] = (RSI[t]-min14[t])/(max14[t]-min14[t])` with min/max over `RSI[t-13..t]` (first valid index 26); **no smoothing is applied** — the functional `ta.momentum.stochrsi()` returns the `.stochrsi()` series, and `smooth1/smooth2` are accepted-but-unused by that path (verified in package source: only `.stochrsi_k()`/`.stochrsi_d()` consume them). Any undefined input or a zero denominator (`max14==min14`, i.e. a flat RSI window) prints **NaN**, never 0 or a carried value.

**Legs:** `BUY[t] = C[t]>SSA[t] AND C[t]>SSB[t] AND rawS[t]<0.8 AND C[t]>EMA50[t]`; `SELL[t] = (C[t]<SSA[t] OR C[t]<SSB[t]) AND rawS[t]>0.2`. All comparisons are **strict**; any NaN operand makes its conjunction False (never trades on undefined prints — a flat market prints NaN StochRSI and zero entries). Entry and exit can never co-fire: BUY requires `C[t] > max(SSA,SSB)[t]` while SELL requires `C[t] < max(SSA,SSB)[t]`, disjoint by arithmetic on every bar including NaN bars, so no tie-break is required. The legs are levels, not edges: a persistent BUY print while LONG is a hold (no-op), and a persistent SELL print while FLAT is a no-op (this includes pre-warmup SELL legs, which the record rule independently holds flat).

**Warmup:** require **100 consecutive fully completed valid 15m bars**, counting the first input as bar 0, before the first eligible decision. Begin with 10,000 USDT, zero BTC, FLAT, no pending order, and no pre-warmup inferred position. First eligible t is 99 (structural full definability starts at bar 93; margin 7).

**Deterministic per-completed-bar order/state machine:**
1. At most one outstanding order. Reconcile any prior simulated executor's actual confirmed fill/failed status before evaluating new actions; creating an order alone never changes the confirmed position. No trade decision before the bar's completion time.
2. If confirmed LONG and a SELL retry is outstanding after a failed previous exit, issue exactly one new SELL of the confirmed held quantity on the **next valid completed bar**; do not require the original exit conjunction to persist. If LONG with no retry and SELL is true, issue one SELL for the full confirmed BTC position. Ignore BUY on every exit bar.
3. If confirmed FLAT and no SELL occurred this bar, if BUY is true and the available quote cash covers `0.001*C[t]*(1+0.0001)`, issue one BUY for 0.001 BTC; otherwise stay FLAT. After a failed BUY, re-evaluate the same level on the next valid bar without a hidden cooldown; no intra-bar retries.
4. An idealized full confirmed BUY fill sets LONG and deducts cash; a rejected/failed BUY leaves FLAT. An idealized full confirmed SELL sets FLAT and credits net cash; a rejected/failed SELL leaves LONG and sets the next-bar retry flag. Partial or indeterminate fills are outside the verified bounded model and **abort as unsupported**, never silently assume full size or fabricate a price. There is no same-bar exit-and-reentry; a new BUY is eligible only on a later completed bar. A confirmed LONG ignores further BUY prints.
5. If neither leg is due, HOLD. No discretionary/manual action. On the final available bar, mark any still-open LONG at the **last observed valid close** for research valuation; do not invent a terminal SELL.

**Explicitly disabled:** stoploss, take-profit, ROI ladder, trailing stop, SHORT (no short token ships; spot long-only), perpetual/futures, leverage, margin/borrowing, funding, pyramiding/position-stacking, DCA/safety orders, simultaneous positions, cooldown/protections, custom stoploss, partial targets, time exit, maker/limit/next-open/intrabar orders, informative-pair inputs, dynamic sizing, compounding, session filter, hidden controller risk defaults, and forced end-of-data liquidation. The SELL-signal leg is the only risk exit. Missing a protective stop is a material loss risk, not an implicit engine default.

**Data failure:** a missing, duplicate, invalid, nonconsecutive or undefined required bar after warmup invalidates the entire research run. Abort; do not let an engine `dropna` erase a gap, fall back to a constant price, or assume a fill.

## Required data

Single real Binance BTC-USDT **spot 15m** OHLCV with exchange **open timestamps** and actual O/H/L/C; Close gates every order leg, High/Low build the cloud, Volume is unread. No multi-timeframe alignment, cross-market series, external fundamentals, order book, funding, mark price, fitted model, or future price is required. One market is a deliberate derivative scope, **not** a policy admission whitelist.

## Execution assumptions

**Pinned Hummingbot engine inspected this cycle via connected GitHub:** package `20260920`, VERSION `dev-2.17.0` (`hummingbot/VERSION` re-read at the pin `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`). Prior independent package/source mapping evidence is in Alpha PR #414/#417; this cycle did **not** rehash the package wheel and does not assert fresh binary identity.

**Actual bounded data and controller path:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` maps **`15m`** in the `INTERVALS` bidict (verified this cycle at the pin — the mapping list runs `1s/1m/3m/5m/15m/30m/1h/...`); `binance_spot_candles.py::_parse_rest_candles` maps exchange `row[0]` open timestamp and `row[1..5]` OHLCV (file presence verified 200 at the pin this cycle; semantics per PR #414/#417). `strategy_v2/backtesting/backtesting_engine_base.py::run_backtesting` initializes feed/controller, then `simulate_execution` iterates processed rows, calls `update_state(row)`, `controller.determine_executor_actions()`, and `simulate_executor()`. `OrderExecutorConfig` in `strategy_v2/executors/order_executor/data_types.py` supports `connector_name="binance"`, `trading_pair="BTC-USDT"`, `side=TradeType.BUY/SELL`, `amount=Decimal("0.001")`, `position_action=OPEN/CLOSE`, `execution_strategy=MARKET`, `price=None`, `leverage=1`. A strategy-specific controller is **not implemented**; these are verified primitives, not a claim that this record is already wired into Hummingbot.

**Fill/position model:** `strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` MARKET path uses the first supplied historical row's actual `close` as full-fill price; `filled_amount_quote = amount*close`, `cum_fees_quote=trade_cost*notional`, `CloseType.POSITION_HOLD`. `BacktestPositionHold` in `backtesting_engine_base.py` nets opposing BUY/SELL base fills, tracks weighted average cost, gross realized/unrealized PnL, and fees **separately**. A MARKET SELL reduces the same BTC spot inventory; no short inventory is opened. The engine's raw candle timestamp is the **opening label**, so the economic decision and simulated fill must be recorded as **opening timestamp+900**, not as an open-time executable trade. This is an idealized **historical completed-close** convention only — a disclosed adaptation away from the source live-market calls — and real post-close market orders cannot be assumed to fill at that past close.

**Cash and costs:** pass explicit `run_backtesting(trade_cost=0.0001)`, a hypothetical **0.01% quote-notional fee per side**; this is not a measured Binance fee schedule or a source parameter (the source models no costs). Maintain independent unborrowed cash `cash_after_buy=cash_before-Q*Pbuy*(1+0.0001)` and `cash_after_sell=cash_before+Q*Psell*(1-0.0001)`, Q=0.001 BTC, and require sufficient cash before BUY. Net realized matched PnL `Q*(Psell-Pbuy)-0.0001*Q*(Pbuy+Psell)`; do not mistake gross `BacktestPositionHold.realized_pnl_quote` for net-of-fee performance. Real exchange fee tier, quantity/price precision, min notional, slippage, spread, latency, and partial fills remain **unverified** and are not simulated as realized zero costs. Spot funding is **not applicable**; do not label zero perpetual funding as observed. No futures leverage/margin claim is made.

**Required engine safeguards:** `BacktestingEngineBase` exposes terminated executors to controllers for only **900 simulated seconds** by default on this clock; use `terminated_executors_window=None` or an equivalent full-run confirmed-fill ledger so fill state is not lost across 15m bars. `prepare_market_data` calls `dropna`, so continuity/validity must be checked before entering the engine. `BacktestingDataProvider.get_price_by_type` can fall back to `Decimal("1")` when a price is missing; **prohibit this path** for strategy fills and abort on missing observed prices. No unverified maker, next-open, intrabar, perpetual or real-time fill path is claimed.

## Evidence

### Source-reported

The immutable source file (`CryptoRobotFr/TrueStrategy@61b668c9`, `ichiCloud-stoch-ema/#1binanceEGLD.py`, 2744 bytes, blob `1daf683714e25c89677ce6452b481daa0253c131`) states: EGLDUSDT Binance-spot live script; 15m klines `"2 day ago UTC"`; `ta.trend.ema_indicator(close, 50)`; bare-default `ta.momentum.stochrsi(close)`; `ta.trend.ichimoku_a(high,low,3,38).shift(periods=48)` / `ta.trend.ichimoku_b(high,low,38,46).shift(periods=48)`; the strict four-leg BUY (`close>SSA & close>SSB & stochrsi<0.8 & close>EMA50`) and three-leg SELL (`(close<SSA | close<SSB) & stochrsi>0.2`) conjunctions on `iloc[-2]`; full-balance market orders gated on 5-USDT minimums; and no stop/target/trailing/ROI/short/DCA/cooldown anywhere in its 74 lines. The sibling notebook and tutorial were not read and contribute no adopted fact.

### Independently reproduced

**No original-source trade reproduction, Qlib/Hummingbot backtest, event-level parity, return, Sharpe, or survivor claim.** This cycle verified the pinned Hummingbot source files and existing research-only MARKET/POSITION_HOLD/fee primitives; verified the `ta` 0.11.0 `stochrsi`/`RSIIndicator`/`EMAIndicator`/`IchimokuIndicator` sources quoted above (including the `visual=False` no-internal-shift finding that makes `.shift(48)` the sole displacement); verified the GitHub blob SHA/size/hash against the pin; and ran a stdlib-only scratch self-check of the frozen formulas confirming BUY/SELL disjointness (asserted per bar over five fuzz seeds), flat-market NaN with zero entries and no crash, strict LONG/FLAT alternation with at most one order per bar (2–6 round trips per 400-bar seed), no BUY leg before SSB index 93, record-rule warmup gating at bar 99, and mid-cloud equality firing neither leg — pure logic validation, not a backtest. No runtime trade, Paper/Testnet/Live or deployment was performed.

### Negative evidence

No K/D (%K/%D) lines exist anywhere in this construction — the gate is the raw unsmoothed StochRSI, so smoothed-crossover failure modes do not apply and must not be imputed. No Tenkan/Kijun/Chikou leg exists — cross-edge Ichimoku failure modes do not apply. The `ta` package version is unpinned by the source, so any other `ta` release's drift is out of scope for this frozen derivative. A no-stop long-only system can suffer large losses in a breakdown regime where the displaced cloud lags the fall. The 48-bar displacement makes the cloud sticky: fast V-reversals re-enter late by construction.

## Falsification plan

After independent admission and downstream selection, test strict-vs-nonstrict threshold edges (0.8/0.2 equality prints nothing), flat-RSI-window NaN (0/0 prints hold/no-enter by construction), mid-cloud equality bars (neither leg fires), persistent-level hold with no re-entry while LONG, failed BUY/SELL next-bar retry, confirmed fill vs order intent, missing 15m bar, warmup boundary at bar 99, completed-close vs raw-open clock, cash insufficiency and fee separation. If the execution primitive/path proves new or unverified, perform one representative Hummingbot/Qlib event-level comparison **before** large-scale screening; otherwise reuse verified primitives. Test IS/OOS net-of-declared-cost profitability separately from HB_READY.

## Crypto portability

Only the declared independent **BTC-USDT spot 15m** version is assessed. The author's EGLDUSDT pair is a quoted source fact, not a portability claim; equities, seven-coin 1h/4h/1d and 3x/5x futures/DCA campaign assumptions are **not** imported. Any leverage, funding, market, timeframe, DCA, or execution change requires a separately declared derived research identity; no blanket admission bans are inferred from these choices.

## Limitations

Research-only, no executable controller, no Pine equivalent (Python live-script source only; sibling notebook unread), no source-native trade equivalence (six disclosed adaptations), no verified realized market fee/slippage, no partial-fill or live-price guarantee, no independently reproduced performance, no Qlib parity. A no-stop strategy can suffer large losses; the displaced cloud lags fast breakdowns. The historical same-close fill is a pinned **simulation convention**, not proof of real tradability. HB_READY PASS is a **Scout admission proposal pending independent Hermes Auditor review**, not a self-certified deployment or profit claim.

## Implementation status

**not-implemented.** No strategy-specific executable, Qlib recipe, backtest, container action or trading action was created.

## Adoption boundary

**status: research-only; implementation_status: not-implemented; adoption: not-approved; approval_scope: research-only.** The independent Hermes Auditor GitHub Webhook Review owns exact-head PASS merge, verifiable source-fact remediation or NOT_LOSSLESS close. Scout never approves, merges, closes, edits README or bypasses review.

## Related Wiki records

None asserted; no Wiki change.

## Sources

- https://github.com/CryptoRobotFr/TrueStrategy/blob/61b668c9adeb4e8506412452e9eab290b8086b37/ichiCloud-stoch-ema/%231binanceEGLD.py — pinned primary source (2744 bytes, blob `1daf683714e25c89677ce6452b481daa0253c131`, SHA-256 `c5793895687c0ca90dc0a2d14784f652da1e14b80775977b13ca677afce766c9`, read live 2026-10-26)
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned Hummingbot source (VERSION, spot candle constants/parser path, backtesting engine, order simulator, position-hold ledger)
- Independent package/source review evidence: https://github.com/HCH725/alpha-strategy-research/pull/414 and https://github.com/HCH725/alpha-strategy-research/pull/417
- `ta` 0.11.0 (`ta/momentum.py` StochRSIIndicator/RSIIndicator, `ta/trend.py` EMAIndicator/IchimokuIndicator) — formula transcription source for the unpinned `ta` dependency
- Distinct main Coinrule Ichimoku-RSI family: https://github.com/HCH725/alpha-strategy-research/blob/a7f8a58/ichimoku-rsi-gated-reversal-btcusdt-1d-2026-10-08.md
- Distinct main Forven Ichimoku cross-edge family: https://github.com/HCH725/alpha-strategy-research/blob/a7f8a58/forven-ichimoku-tenkan-kijun-cross-cloud-gated-long-flat-btcusdt-1d-2026-10-24.md
