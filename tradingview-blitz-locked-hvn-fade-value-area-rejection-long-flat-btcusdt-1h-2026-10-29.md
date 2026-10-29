---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "blitz_locked value-area rejection (fade-only) — independent BTC-USDT spot 1h long-flat derivative"
created: 2026-10-29
updated: 2026-10-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-29
sources:
  - https://www.tradingview.com/script/1OnkbAiE-HVN-Fade-Break-Volume-Profile-Fade-Breakout-Strategy/
  - https://www.tradingview.com/support/solutions/43000502040-volume-profile-indicators-basic-concepts/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Value-area rejection long, POC target — independently derived BTC-USDT spot 1h strategy

## Provenance

**First-party TradingView publication:** blitz_locked, *HVN Fade & Break | Volume Profile Fade & Breakout Strategy*, Pine v6 open-source strategy, script ID **1OnkbAiE**, page `<time datetime="Tue, 29 Sep 2026 20:21:11 GMT">` (page label "Sep 30"), https://www.tradingview.com/script/1OnkbAiE-HVN-Fade-Break-Volume-Profile-Fade-Breakout-Strategy/ . **Full Pine source read end to end in this cycle on 2026-10-29** (all 482 lines: inputs, `f_pocOnly`, `f_buildProfile`, session/naked-POC bookkeeping, fade/breakout predicates, `strategy.entry`/`strategy.exit` blocks, the author's `runtime.error` guard requiring chart TF < profile period): 24,339 bytes, SHA256 `2a9d8a6bd9a25e3ad77f01106de29e58411f66e084eec379c47319a9def4db77`, byte-identical to the independent fetch of 2026-10-28; the live page title and author were re-verified on 2026-10-29. The script builds a rolling multi-session volume-at-price profile (POC / VAH / VAL), tracks "naked" (untouched) POCs, detects HVN zones, and trades two setups. Verified source defaults used here: `profileTF="D"`, `lookbackPeriods=20`, `rowsNb=60`, `vaPct=70.0`, `rsiLen=14`, `rsiOS=40`, `rsiOB=60`, `pivotLen=5`, `atrLen=14`, `atrStopMult=1.2`, `rMultiple=1.8`, `volMult=1.5`, `volAvgLen=20`, `oneTradeAtATime=true`, `tradeMode="Both"`, `initial_capital=10000`, `commission_value=0.02`, `slippage=2`.

**Profile algorithm authority:** TradingView, *Volume profile indicators: basic concepts* (first-party knowledge base), §"Calculating value area" — POC = highest-volume row; target = total × 70%; expand from the POC, each step adding the larger of the next row above/below; ties go to the row closer to the POC, then above; VAH = highest included row, VAL = lowest included row.

**Two verified defects / divergences in the published script (not repaired silently — declared, both re-traced in the source this cycle):**
1. **VAH/VAL edge expressions are inverted.** The script's expansion keeps `up` (pointer moving *down* from the POC row) and `dn` (pointer moving *up*), then emits `outVAH = pl + (vahRow+1)*step` from the low-side pointer and `outVAL = pl + valRow*step` from the high-side pointer, i.e. the low-side pointer defines VAH and the high-side pointer defines VAL. Traced on 10 toy rows `[0,0,0,9,5,1,0,0,0,0]`, `pl=100`, `step=1`: the included rows are `[3,4]` and the script returns `VAH=104.0, VAL=104.0` where the correct edges are `VAH=105.0, VAL=103.0`; on `[0,0,0,1,5,9,0,0,0,0]` it returns `VAH=VAL=105.0` against correct `106.0/104.0`. This derivative therefore keeps the script's **row construction and POC rule verbatim** but defines the **value-area edges from TradingView's published expansion rule**, applied to those same 60 rows.
2. **Prose vs. code.** The description says a fade fires when price "pokes outside the value area and closes back inside on the *same bar*"; the code actually tests `low[1] < profVAL and close > profVAL and close > close[1] and rsi <= rsiOS` (source line 423), a **two-bar** previous-bar-probe / current-bar-reclaim pattern. This record follows the **code**, not the prose.

**Explicit independent derivative (NOT source-native):** preserved: the rolling 20-period volume-at-price histogram, the 60-row equal-split construction, POC definition, the fade-long entry predicate (including RSI14 ≤ 40 and the up-close requirement), the fade stop formula `min(low − 0.6·ATR14, last confirmed 5/5 pivot low)` and the POC target. Researcher choices: (a) Binance **BTC-USDT spot 1h** chart with **UTC day** sessions instead of the author's suggested 5m–15m chart (the author's own runtime guard only requires chart TF < profile period); (b) **LONG/FLAT only**, fade setup only (`tradeMode="Fade only"`), short side, breakout setup, HVN zones, naked-POC targets and the R-multiple fallback all disabled; (c) value-area edges per TradingView's published rule, as declared above; (d) exits are evaluated on **completed bar closes** (MARKET) instead of the source's intrabar `strategy.exit` stop/limit bracket; (e) a setup is skipped when the POC target is not strictly above the decision close; (f) fixed `0.001 BTC` instead of 25%-of-equity, 10,000 USDT initial cash, 0.1% modeled fee per filled side, 720-bar warmup.

**Immutable strategy identity:** `TV:1OnkbAiE:blitz_locked:2026-09-29 | independent-derived-v1:2026-10-29 | BTC-USDT-Binance-spot-1h-UTCday-sessions | profile20x60-va70-TV-expansion | fade-long:low[1]<VAL,close>VAL,close>close[1],RSI14<=40,POC>close | stop=min(low-0.6ATR14,lastPivotLow5) | target=POC | LONG/FLAT-Q0.001-no-DCA | completed-close-MARKET | fee0.001/side | warmup720`. Any change in profile window/rows/VA%, entry predicate, stop, target, market, timing or costs is a different derivative.

**Dedup on `main@094202e1` (439 root strategy records, re-run this cycle):** root-level case-insensitive full-text search for `volume profile`, `value area`, `VAH`, `HVN`, `naked POC`, `volume at price`, `session profile`, `volume distribution`, `rowsNb`, `vaPct`, `1OnkbAiE`, `blitz_locked` returns **zero** strategy records. The single `value area` hit is `r-breaker-7-level-breakout-reversal-flip-two-sided-btcusdt-1h-2026-10-14.md`, which uses that phrase for **arithmetic prior-day pivot ladders** ("prior-day auction … plus an extension arm"), not a volume-at-price histogram, and trades a different trigger (ladder flip with an r2/s2 probe latch). Substring `poc` hits elsewhere are word fragments ("epoch"/"Coppock"), not POC levels. All eleven open `research/*` PRs (#593 Vinicius Supertrend volume/body/RSI, #353 Heracles Keltner/Donchian ratio, #350 ClucMay72018 BB-discount, #331 AdxSmas, #304 forven CCI recross, #251 Swift 2YMA multiplier, #92 SSL channel, #89 Chandelier Exit, #63 SuperTrend, #49 Gaussian channel, #48 3-EMA channel) were inspected by title: none contains volume-profile, value-area, VAH/VAL/HVN or POC content. Explicitly different from volume-flow families: `tradingview-kriswaters-smoothed-roc-trough-volume-gated-*` (volume only gates an ROC trough, no price-binning), `tradingview-ai-volume-quadruple-atr-cooldown-*` (4× average-volume confirmation on a price/ATR entry), OBV/CMF/AD-line records (volume *flow*, not volume *by price*), `forven-vwap-pullback-distance-*` (volume-**weighted mean**, not the modal row). No duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported
The rolling profile marks where the last 20 sessions actually transacted. The value area is the band holding ~70% of that volume; the POC is its single densest price. A probe below the lower edge that is immediately reclaimed on an up close with oversold RSI is treated as rejection of "cheap" prices inside an otherwise accepted range, with the POC as the reversion objective and the ATR/pivot distance as the invalidation. The author labels the script an educational template with illustrative defaults, not an optimized system.

### Research interpretation
This derivative buys only a **completed-bar** reclaim of the lower value-area edge after the prior bar traded below it, on the UTC-day profile frozen at the session's first bar. The POC is the exit; a completed close back under the frozen stop abandons the thesis. Nothing about profitability, win rate or the author's own backtest is imported.

## Signal

One contiguous sequence of **completed** Binance BTC-USDT Spot 1h OHLCV candles, indexed `t=0`, `H[t]>=max(O[t],C[t])>=min(O[t],C[t])>=L[t]`, `V[t]>=0`, strictly 3600 s apart, with no missing, duplicated or out-of-order bars.

1. **Session clock and warmup.** A UTC day session begins on the bar whose open timestamp is exactly `00:00:00Z`. All levels below are rebuilt on that bar from completed data only and stay frozen until the next rebuild. No profile, entry, stop or target evaluation exists before **720** completed 1h bars (30 complete UTC days, a researcher pin far beyond the 480-bar profile and the 14-bar indicator seeds); the first eligible rebuild and the earliest possible decision are therefore on the first bar of day 31.
2. **Profile window.** `W` = the 480 completed 1h bars immediately preceding the rebuild bar (the 20 most recently completed UTC sessions). No bar of the current session enters its own profile.
3. **Rows (source-verbatim).** `pl = min(L over W)`, `ph = max(H over W)`, `step = (ph-pl)/60` (if `step<=0`, `step = syminfo.mintick`, i.e. 0.01 on BTC-USDT). For each bar `i` in `W`: `r0 = clamp(floor((L[i]-pl)/step), 0, 59)`, `r1 = clamp(floor((H[i]-pl)/step), 0, 59)`, `share = V[i]/(r1-r0+1)`, and `share` is added to every row `r0..r1`. Rows are half-open `[pl+r*step, pl+(r+1)*step)`.
4. **POC (source-verbatim).** `p` = the **lowest** row index attaining the maximum row volume (the script's strict `>` scan keeps the first maximum); `POC = pl + (p+0.5)*step`. Ties therefore resolve downward deterministically.
5. **Value area (TradingView published rule).** `target = 0.70 * sum(rows)`; start with `lo = hi = p`, `acc = rows[p]`; repeatedly compare `rows[lo-1]` (below) with `rows[hi+1]` (above), ignore out-of-range rows, take the larger volume — ties take the row closer to `p`, and equal distance takes the row **above**; if `acc + chosen > target` **stop**, else include it (`lo-=1` or `hi+=1`, `acc+=chosen`). Then `VAH = pl + (hi+1)*step` (top edge of the highest included row) and `VAL = pl + lo*step` (bottom edge of the lowest included row). The published script's inverted edge expressions are **not** used (see Provenance defect 1).
6. **Indicators (source defaults, completed bars only).** `RSI14` = Wilder RSI on closes (`ta.rsi`); `ATR14` = Wilder RMA of true range `max(H-L, |H-C[t-1]|, |L-C[t-1]|)` (`ta.atr`); pivot lows use `pivotLen=5`: `low[t]` is a confirmed pivot low when it is strictly lower than the five lows on each side (`ta.pivotlow`), and the confirmation only exists at `t+5`; `lastSwingLow` is the price of the most recently **confirmed** pivot low, `na` before the first one.
7. **Entry (source fade-long, code-exact).** At completed bar `t`, with `POC`, `VAH`, `VAL` all defined for the current session, `FLAT`, and no order pending, emit one BUY when **all** of: `L[t-1] < VAL`, `C[t] > VAL`, `C[t] > C[t-1]`, `RSI14[t] <= 40`, and `POC > C[t]`. Equality on `RSI14` and on the `VAL` test qualifies; the last clause is a declared researcher guard (see Provenance (e)) that removes only setups whose POC target would be at or below the fill.
8. **Stop and target at entry (source formulas).** `S = min(L[t] - 0.6*ATR14[t], lastSwingLow)` when `lastSwingLow` is defined, otherwise `S = L[t] - 0.6*ATR14[t]` (source line 446: `atrStopMult(1.2)*0.5 = 0.6`); `T = POC`. Both are frozen for the life of the trade.
9. **Exit.** On each later completed bar `u`: SELL at that close when `C[u] <= S` (invalidation) or `C[u] >= T` (target). Because `S < T`, the two conditions cannot both hold. One action per bar, exits before entries, no same-bar re-entry; the position is otherwise held with no time limit.
10. **State and re-entry.** States `FLAT`, `LONG`. After a confirmed SELL, `FLAT` on the next bar and a fresh qualifying setup may enter immediately (the source imposes no cooldown; `oneTradeAtATime` only suppresses signals while a position is open). An absent, rejected, expired, partial, mismatched or unconfirmed fill **aborts the research run** rather than fabricating inventory.
11. **Explicitly disabled:** short/sell-side entries (`rsiOB=60` short fade), the breakout setup, HVN-zone and naked-POC targets, the `rMultiple=1.8` fallback target, the `volMult=1.5`/`volAvgLen=20` volume filter, pyramiding, DCA/safety orders, multiple pairs, concurrent positions, intra-bar bracket orders, trailing/breakeven stops, cooldowns, funding, leverage/margin and forced end-of-sample liquidation. An open end-of-sample long is marked to the last **real** close.

## Required data

Exactly one Binance Spot BTC-USDT `1h` candle feed: completed O/H/L/C, base-asset `volume` and the open timestamp. Volume is a **decision input** (rows 3–5). No order book, trade tape, lower or higher timeframe, second symbol, trained model, index/mark price, funding or external feed. Validate continuous 3600 s spacing, UTC-day coverage and OHLC geometry **before** the pinned engine's `dropna`; a missing/invalid bar or a day with fewer than 24 bars fails closed and aborts the run rather than shifting a session boundary or filling rows with stale data.

## Execution assumptions

**Pinned engine:** Hummingbot package `20260920`, `hummingbot/VERSION=dev-2.17.0`, source commit `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (all re-verified live this cycle: `hummingbot/VERSION` returns `dev-2.17.0`; `setup.py` carries the historical `version = "20260729"` string, i.e. the setup string is **not** the distribution pin). Previously reviewed Alpha PR #414 records a package-20260920 wheel mapping to this commit; this Scout read the source paths below but **did not rehash the wheel**. Auditor must reject Gate 5 if that mapping is invalid.

**Data/clock path (verified live this cycle at commit `8b0e067`):** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` defines `INTERVALS` including `1h` (also `15m`, `1d`); `binance_spot_candles.py` parses REST `row[0]` as the **candle-open** timestamp in seconds and `row[1..5]` as O/H/L/C plus base-asset `volume`. Completed bar `t` becomes available at `effective_ts[t] = open_ts[t] + 3600 s`; normalize the controller decision row and the historical fill row to that effective close. The UTC-day rebuild trigger is the decision bar whose `open_ts` is `00:00:00Z`, and its profile uses only bars with `effective_ts <= open_ts`. No incomplete hourly bar is eligible.

**Controller/executor/fill path (verified live this cycle at commit `8b0e067`):** a strategy-specific, **not yet implemented**, ControllerV2 state machine reads the 1h candles (volume included) from the market data provider, maintains the frozen session profile, and emits `CreateExecutorAction(OrderExecutorConfig(...))` with `ExecutionStrategy.MARKET`, connector `binance`, pair `BTC-USDT`, BUY/SELL, `Decimal("0.001")` base amount, leverage 1. The pinned `strategy_v2/backtesting/backtesting_engine_base.py` prepares each row (carrying `volume_bt` into the working `volume` column, then `dropna`); `strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` fills MARKET at the **first supplied row's close** (`entry_price = close`, `filled_amount_quote = amount*entry_price`, `cum_fees_quote = trade_cost*amount_quote`) and terminates as `CloseType.POSITION_HOLD`. `BacktestPositionHold` nets BUY/SELL exposure with realized gross PnL tracked separately from fees. `CandlesConfig.max_records` must exceed 480 so a single session rebuild can see its full window outside the backtest loader. Reconcile fill/inventory state after the final engine flush; any missing or invalid price aborts the run — never a fabricated mark. Validate real Binance trading rules (lot size, min notional, precision) before simulation; reject rather than resize 0.001 BTC silently. Pinned `dropna` preparation must not conceal raw gaps; validate continuity first.

**Research economic model:** initial **10,000 USDT** unborrowed spot cash, fixed `Q=0.001 BTC`, single pair, one pending action; research fee `f=0.001` per filled side of actual quote notional. BUY requires `cash >= Q*P*(1+f)`; SELL requires confirmed inventory `>= Q`. Matched net realized USDT `= Q*(P_sell-P_buy) - f*Q*(P_buy+P_sell)`; open inventory is marked separately and gross `total_pnl` must not be labeled fee-net. The modeled fill is the decision bar's own close (an idealized convention, **not** a live after-close fill); zero additional slippage is assumed, not observed. Spot-only has no funding contract; do not report futures funding as zero. Exchange fee tier, lot/tick/min-notional checks, partial fills and latency are **not verified**.

## Evidence

### Source-reported
The dated first-party page supplies the rolling-profile construction, POC/VA/HVN definitions, both setups, the fade predicate, the stop/target structure and every default used above. The page's own warnings state the script is an educational template, its defaults are illustrative and not tuned, it is not a finished system, there is no reward:risk filter or drawdown circuit breaker, and percent-of-equity sizing is not risk-normalized. No source performance metric is imported.

### Independently reproduced
**Read and verified in this cycle:** the complete Pine v6 source of script `1OnkbAiE` (all 482 lines, SHA256-pinned above: inputs, `f_pocOnly`, `f_buildProfile`, session/naked-POC bookkeeping, fade/breakout predicates, `strategy.entry`/`strategy.exit` blocks, the author's `runtime.error` guard requiring chart TF < profile period); the pinned Hummingbot `VERSION`, `setup.py` string at commit `8b0e067`, `binance_spot_candles` interval table and REST row parser, `backtesting_engine_base.prepare_market_data` (volume carry + `dropna`), and `order_executor_simulator.simulate` (MARKET first-row-close fill, quote/fee ledger, `POSITION_HOLD` termination). **No backtest and no Qlib/Hummingbot run performed**; Gate 5 is a static pinned-source compatibility claim only.

### Negative evidence
Not a lossless reproduction: the published VAH/VAL edges are defective (verified above), the prose and code disagree on the fade's bar alignment, the chart timeframe is changed from 5m–15m to 1h, shorts and the breakout setup are disabled, and the intrabar bracket is replaced by completed-close exits. The close-based stop can only exit at a bar close beyond `S`, so realized losses can exceed the nominal stop distance, and the modeled same-close entry is optimistic versus any real order placed after a bar closes. The strategy has no protective limit on holding time and no drawdown control. Count agreement on `main` is not proof that every historical frontmatter was independently re-audited in this cycle.

## Falsification plan

Future authorized tests (not performed here): profile window exactly 480 bars vs 479/481; a session with 23 or 25 hourly bars; ties in row volume and in POC; VA expansion stopping on the overshoot row; `VAL`/`RSI` equality boundaries; the `low[1]` probe paired with a non-up close; the POC-below-entry guard firing; `lastSwingLow` `na` before the first pivot confirmation; a stop and a target in the same session; re-entry on the bar after an exit; missing 00:00 bar, rejected fill, fee-net reconciliation and end-of-sample open inventory.

## Crypto portability

`BTC-USDT` Binance spot `1h` with UTC-day sessions only. Other pairs, `1d`/`4h` charts, `W` profiles, shorts, the breakout setup, futures/leverage or the house 6/6/6 DCA campaign are **separate** derivatives requiring their own specification and engine evidence; none is an admission prerequisite for this record.

## Limitations

The published script's value-area edges are defective and its prose disagrees with its code, so no source-native or lossless claim is made; the value-area definition is taken from TradingView's published algorithm instead. No candidate-specific Hummingbot/Qlib simulator run, controller implementation, wheel-byte rehash, exchange live fill or Qlib parity. A completed-close MARKET fill and a completed-close stop are optimistic versus an intrabar bracket; the strategy is unprotected between exits and may hold through adverse moves. The conjunction (prior-bar probe + reclaim + up-close + RSI ≤ 40 + POC above close) is selective by construction, so downstream evaluation needs the full 2017+ history rather than a short window.

## Implementation status

not-implemented; no code, container, backtest, Qlib/Hummingbot controller, n8n, deployment, cron or trading changes. Subsequent engineering materialization follows the existing `IMPLEMENTATION_NEEDED` path only if this strategy is independently audited and later selected.

## Adoption boundary

Research-only; adoption not approved; approval scope research-only. Independent Hermes Auditor GitHub Webhook Review alone owns source-fact remediation, exact-head six-gate PASS merge or NOT_LOSSLESS close. Scout never approves, merges or edits `main`/README.

## Related Wiki records

None asserted.

## Sources

- blitz_locked, *HVN Fade & Break | Volume Profile Fade & Breakout Strategy*, TradingView, Pine v6 open-source strategy, script ID `1OnkbAiE`, published 2026-09-29 20:21 UTC, full source read end to end 2026-10-29 (24,339 bytes, SHA256 `2a9d8a6bd9a25e3ad77f01106de29e58411f66e084eec379c47319a9def4db77`): https://www.tradingview.com/script/1OnkbAiE-HVN-Fade-Break-Volume-Profile-Fade-Breakout-Strategy/
- TradingView, *Volume profile indicators: basic concepts*, §"Calculating value area", tie-breaking rules and VAH/VAL definition: https://www.tradingview.com/support/solutions/43000502040-volume-profile-indicators-basic-concepts/
- HCH725/hummingbot source commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3` (live-verified this cycle): `hummingbot/VERSION`, `setup.py`, `hummingbot/data_feed/candles_feed/binance_spot_candles/{constants.py,binance_spot_candles.py}`, `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py`, `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`.
- HCH725/alpha-strategy-research PR #414, prior wheel/source pin evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
