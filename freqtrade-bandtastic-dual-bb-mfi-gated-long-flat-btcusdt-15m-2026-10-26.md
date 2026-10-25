---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade Bandtastic dual-band MFI-gated long-flat on BTCUSDT 15m bars
created: 2026-10-26
updated: 2026-10-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/Bandtastic.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade Bandtastic dual-band MFI-gated edge — independently derived executable research rule

## Provenance and immutable identity

- Primary GitHub identity: repository `freqtrade/freqtrade-strategies` (open-source Freqtrade strategy collection, MIT-licensed file by Robert Roman); exact file path `user_data/strategies/Bandtastic.py`; class `Bandtastic(IStrategy)` (the only class in the file); pinned commit SHA `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`, verified as the repository HEAD via the GitHub commits API during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 7310 bytes, 163 lines, SHA-256 `15dcb60d49a3681241cd39645f0fe8e6dc247687bf878c2026f37bb1c5790b57`, identical to the GitHub blob (`git hash-object` reproduces `f7710c76ae1e4ac7aff90857a647e4c2143baf9f`, size 7310 via the contents API at the pinned commit) — the entire file was retrieved and inspected end to end.
- The file's own words (quoted for gate evidence, never extended): `timeframe = '15m'`; `startup_candle_count = 999`; risk block `minimal_roi = {"0": 0.162, "69": 0.097, "229": 0.061, "566": 0}`, `stoploss = -0.345`, `trailing_stop = True` with `trailing_stop_positive = 0.01` / `trailing_stop_positive_offset = 0.058` / `trailing_only_offset_is_reached = False`; indicators are exactly `ta.RSI(dataframe)` and `ta.MFI(dataframe)` (both TA-Lib defaults, timeperiod 14, pinned by call), four Bollinger sets `qtpylib.bollinger_bands(qtpylib.typical_price(dataframe), window=20, stds=1/2/3/4)`, and EMA rows for every period in the hyperopt ranges (all dead under the defaults below); with the shipped defaults (`buy_rsi_enabled=False`, `buy_mfi_enabled=False`, `buy_ema_enabled=False`, `buy_trigger="bb_lower1"`) the long entry is `(close < bb_lowerband1) & (volume > 0)`; with the shipped defaults (`sell_rsi_enabled=False`, `sell_mfi_enabled=True` with `sell_mfi=46`, `sell_ema_enabled=False`, `sell_trigger="sell-bb_upper2"`) the long exit is `(mfi > 46) & (close > bb_upperband2) & (volume > 0)`.
- Full-file token census (verified by search over the 163 lines this cycle): 1 `INTERFACE_VERSION` (`3`); 0 `enter_short` / 0 `exit_short` / 0 `can_short`; 0 `process_only_new_candles`; 0 `informative_pairs` / 0 `resample` / 0 `merge_informative`; 0 `position_adjustment` / 0 `leverage` / 0 `custom_stoploss` / 0 `protections` / 0 cooldown; no volume read besides the `volume > 0` guards and the MFI input; 0 `fee` / 0 `slippage` / 0 `funding` (no economics anywhere). The file header prints one hyperopt-result comment (`Optimized With Sharpe Ratio and 1 year data`, 30918 trades, `119.93%`) — cited here as file-printed provenance only; this record adopts no performance figure of any kind.
- **Not source-native / not a lossless Freqtrade reproduction.** The source pins the `15m` frame, the 999-bar startup count, the guard/trigger defaults above, and the full risk block — but ships no venue spelling, no fill-timing flag, and no position-sizing rule.
- **All researcher-defined differences/choices, declared in advance:** (1) long-only (the file ships no short leg of any kind — nothing disabled); (2) the file's entire risk block (four-rung ROI ladder, `-0.345` stoploss, active trailing block) is explicitly disabled — the signal-exit leg is the sole position-ending path, so no profit-trigger definition is required anywhere in this record; (3) fix Binance BTCUSDT **spot** `15m` candles (the file names no market); (4) same-decision-bar **close-price MARKET fills** on completed bars, instead of claiming the source engine's fill convention; (5) fix one `0.001 BTC` base-size position, one-position-only, no DCA, no cooldown; (6) pin the dual-band arithmetic and the MFI14 recurrence below exactly (finite-window bands need no library; the MFI seed transient is extinguished by the adopted 999-bar warmup); (7) fix the contiguity, gap, cost and clock model below. No other source-native execution or cost equivalence is claimed.
- **Fitted-parameter disclosure (Gate 1):** the shipped guard/trigger defaults are the author's published hyperopt-fitted values (`buy_fastema=211`, `buy_slowema=250`, `sell_fastema=7`, `sell_slowema=6`, thresholds `52/30/57/46`); the training pairs, window and cutoff are undisclosed in-file beyond the `1 year data` comment. This derivative freezes those fitted defaults verbatim as constants — no re-fit, no selection among the trigger/guard alternatives (the `bb_lower2/3/4`, `sell-bb_upper1/3/4` and EMA/RSI-guard alternatives stay off exactly as the defaults leave them). The derivative is therefore deterministic and reproducible; the fitted provenance is fenced as a limitation, never as portable edge.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the bar where close falls under the 1-sigma lower Bollinger rail (typical price, 20 bars); sell the bar where close is back above the 2-sigma upper rail while 14-bar money-flow is firm (MFI above 46); backstop every position with a four-rung ROI ladder, a fixed `-34.5%` stoploss and an active trailing stop. No behavioural, structural, or risk-premium channel is claimed anywhere in the 163 lines.

### Research interpretation

Research hypothesis only: a close printing beneath the 1-sigma typical-price band marks a statistical washout leg, and requiring both a reclaim of the wider 2-sigma band and firm money-flow on the exit keeps the position through weak dead-cat bounces that never rebuild participation. Unlike single-band mean-reversion records, the entry rail (1 sigma) and the exit rail (2 sigma) are deliberately asymmetric, so the round trip must cross the full band width plus a flow confirmation — unlike RSI-gated dip records, no oscillator participates in the entry at all. This is a washout-plus-participation hypothesis, not a breakout order or a guaranteed profit mechanism. No return, Sharpe, win-rate, drawdown, or other independently reproduced statistic is asserted.

## Signal — fully specified derived rule

Data are UTC Binance BTCUSDT spot `open, high, low, close, volume` on **completed** `15m` candles. Let bar index `t` refer to the current completed candle. All comparisons are strict; equality on any strict leg fails. Define:

```text
TP[t]      = (H[t] + L[t] + C[t]) / 3
SMA20[t]   = mean(TP[t-19 .. t])
SD20[t]    = sqrt( sum((TP[k] - SMA20[t])^2 for k in t-19..t) / 19 )   // sample std, ddof=1
L1[t]      = SMA20[t] - SD20[t]
U2[t]      = SMA20[t] + 2 * SD20[t]
```

- The band block is undefined for `t < 19` (fewer than 20 bars) and for any bar whose 20-bar window contains a non-finite input. `SD20[t] == 0` (twenty identical typical prints) renders `L1 == U2 == SMA20`; both strict legs then read false — an explicit no-op, never a fill.
- `MFI14` is the TA-Lib `MFI(timeperiod=14)` construction pinned as arithmetic: for `t >= 1`, `rawMF[t] = TP[t]*V[t]`; `pos[t] = rawMF[t]` if `TP[t] > TP[t-1]` else `0`; `neg[t] = rawMF[t]` if `TP[t] < TP[t-1]` else `0`. Seed `SP/SN` = means of `pos/neg` over the first 14 flows; then Wilder recursion `SP = (SP*13 + pos[t])/14`, `SN = (SN*13 + neg[t])/14`; `MFI = 100 - 100/(1 + SP/SN)`. Undefined for the first 14 bars of history and on any bar where `SP + SN == 0` (zero-denominator guard — such bars generate no signal under any library edge convention). The adopted 999-bar warmup drives the seed residue `(13/14)^985` to exactly zero for all practical purposes, so no TA-Lib version or seeding alternative can move any post-warmup event.
- `entry[t] = (C[t] < L1[t]) and (V[t] > 0)`; `exit_[t] = (MFI14[t] > 46) and (C[t] > U2[t]) and (V[t] > 0)`. The first bar of history satisfies neither (no lookback). A zero-volume bar can never satisfy either leg.
- **Entry and exit predicates are logically disjoint:** entry needs `C[t] < L1[t]`, exit needs `C[t] > U2[t]`, and `L1[t] <= SMA20[t] <= U2[t]` on every bar — no bar can satisfy both, so no same-bar conflict ordering is ever required. Exit evaluation precedes entry evaluation as stated order; it is moot by construction.
- State transitions are evaluated **once after the bar is complete**, using the state carried *into* the bar:
- `FLAT + entry[t]` -> MARKET BUY exactly `0.001 BTC` at that completed bar's close, then `LONG` with entry bar `t`.
- `LONG + (t > entry_bar) + exit_[t]` -> MARKET SELL the entire recorded `0.001 BTC` at that bar's close, then `FLAT`.
- Otherwise hold the previous state. A held position never adds, even if a fresh entry edge prints. The entry bar **cannot** be its own exit (additionally enforced by the `t > entry_bar` arm).
- After an exit, a fresh qualifying entry edge on a later bar may enter immediately; no cooldown (the source ships none — explicitly none, not invented).
- All pre-warmup and pre-first-entry bars are FLAT. Missing/invalid candles cause **no signal and no fill**, not synthetic price or forced entry. On the final data bar, a remaining position is reported as open; no fabricated terminal liquidation.
- Direction is LONG/FLAT only; the file ships no short leg to disable. Reverse-on-signal, hedging, simultaneous positions, pyramiding, averaging, safety orders/DCA, ROI ladder, stop loss, trailing stop, take profit, partial exits, stop/limit/maker orders, and time-based exits are all **disabled by this derived specification**. No hidden executor defaults supply any of them. Dead file columns under the frozen defaults (RSI14, all EMA rows, 3-sigma/4-sigma rails) are never read by either leg.

## Required data, warmup, causality

- One market, one `15m` UTC candle feed: `high/low/close` (typical-price bands), `close` (both cross legs), `volume` (positivity guards and the MFI flow weight). No `open` reads, no L2, funding, cross-asset, mark/index, calendar events, higher/lower timeframe, or other non-OHLCV data are read by any signal.
- Derived warmup adopts the source's own `startup_candle_count`: **999 contiguous valid completed `15m` bars**, no trade before it — covers the 20-bar bands, the MFI14 seed transient (extinguished, see above), and every dead EMA period with margin.
- Every signal on bar `t` depends solely on bars `<= t`. A bar is only made available after its `15m` close; the close is never treated as known at that bar's open. No repainting, lookahead, negative shift, full-sample fitting, future pivot, or partial higher-timeframe candle.
- Validity per bar: finite positive O/H/L/C, `H >= max(O,C)`, `L <= min(O,C)`, finite nonnegative V, strictly consecutive 900-second opening timestamps. A violating bar generates no signal and no fill and resets the 999-bar continuity count. If LONG across a gap, confirmed inventory is retained and exit evaluation resumes only after a fresh valid warmup — never an invented exit price.

## Execution assumptions — pinned Hummingbot capability evidence

**Pinned contract:** Hummingbot package `20260920` (policy label), `hummingbot/VERSION = dev-2.17.0`, repository `HCH725/hummingbot` commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3` (commit object verified present in the local clone this cycle; VERSION read at the pin). Read-only inspection of this exact commit establishes the following *code-level primitives*, not a strategy-specific live/testnet run:

1. **Data/venue:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` lists `15m` in `INTERVALS` with `CANDLES_ENDPOINT = "/api/v3/klines"`. `binance_spot_candles.py` parses `row[0]` as candle **open timestamp** and OHLC plus volume from `row[1..5]`. The research decision clock is explicitly **open_timestamp + 900 seconds**, the completed `15m` bar's effective availability time; raw Hummingbot candle timestamps remain open-time labels and must not be mistaken for close-time decisions.
2. **Fill:** `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`, `OrderExecutorSimulator.simulate`: `ExecutionStrategy.MARKET` fills at the first supplied row, uses that row's **close** as `entry_price`, records `filled_amount_quote = amount * close`, `cum_fees_quote = trade_cost * filled_amount_quote`, and terminates with `POSITION_HOLD`. The engine's raw `fill_timestamp` is the supplied row's **open-time label**; the declared causal event time is the separately normalized close-effective time `open_timestamp + 900`. This is a **research backtest convention**, not a live guaranteed close fill.
3. **Controller and ledger:** `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` executes `update_state(row)` then `controller.determine_executor_actions()`, accepts `CreateExecutorAction` with `OrderExecutorConfig`, and uses `BacktestPositionHold` to net executed BUY/SELL base exposure and separately accumulate realized gross PnL and fees ("Buys and sells of the same asset net out automatically. Realized PnL comes from matched buy/sell volume."). `prepare_market_data` joins features with backward `merge_asof` on open labels, so a controller must withhold each signal until that bar is complete. The derived controller's own persistent `FLAT/LONG(entry_bar, Q)` state and fill ledger (not the engine's bounded terminated-executor view — use `terminated_executors_window=None` or a persistent equivalent) gate entries/exits. A controller implementing exactly these transitions is **not yet implemented** and is a downstream engineering artifact, not a second HB_READY admission criterion.
4. **Cost/position model:** one `Q=0.001 BTC` BUY/SELL unit on Binance **spot**, no leverage/margin/liquidation/futures funding; funding is **not applicable**, not silently set to a fictitious realized zero-funding stream. Pinned backtest fee is `trade_cost=0.001` **per side**, applied to each simulated fill's quote notional; modeled slippage is `0.0` because this pinned MARKET simulator fills at its close input, **not** a claim of actual zero market slippage. Per completed trade, fee-adjusted research PnL is `realized_gross_quote - sum(cum_fees_quote)`; the executor `net_pnl_quote` alone is not accepted as fee-adjusted cash/equity. Deliberately there is **no cash-sufficiency gate and no initial-capital dependency**: trade events depend only on candles and fill-confirmed state, so no balance initialization, reservation, or cash-ledger rule can alter any event. The simulator uses binary floats for amount*price with no verified exchange tick/lot rounding, so tiny float residues and real-world precision/slippage discrepancies are limitations, not hidden fills. `BacktestingDataProvider.get_price_by_type` has a fallback `Decimal("1")`, which **must not** be used as an absent BTC price.
5. **Timing constraints:** no next-open, intrabar stop, maker queue, partial fill, shared capital, multi-timeframe, or simultaneous multi-asset semantics are required by this derivative. The single-row MARKET-close primitive is reused, and the `15m` `+900s` normalization is mandatory before comparing event timestamps. No missing bar's close is invented; a missing `15m` bar blocks that bar's decision/fill.

These exact engine source paths and restrictions provide **static code-path compatibility evidence** for the defined derived rule. No Qlib/Hummingbot strategy backtest, runtime deployment, trade, or event-level Qlib/HB parity was performed in this Scout cycle. Independent Hermes Auditor must independently verify Gate 5 and all other gates against the pinned code before any merge. Representative engine-path parity remains required before screening if the path is not already validated; PASS is not profitability, Qlib materialization, Survivor, HB Certified or trading authorization.

## Six-gate HB_READY evidence for independent review

1. **Deterministic:** exact typical-price dual-band arithmetic (SMA20, ddof=1 sigma, 1-sigma entry rail / 2-sigma exit rail), exact MFI14 recurrence with seed and zero-guard, strict entry/exit legs with explicit undefined handling, provably disjoint legs, explicit bar offsets and state priority; all researcher choices pinned above.
2. **Direction:** BTCUSDT Binance spot LONG/FLAT only; the file ships no short leg.
3. **Entry/exit/risk:** entry on the completed sub-1-sigma-plus-volume bar, exit on the completed over-2-sigma-plus-MFI46-plus-volume bar, no protective/partial/other exit; disabled behaviours enumerated, including terminal position handling. No profit-trigger definition is needed because no ROI/stop/trailing leg exists in this derivative.
4. **State:** one fixed `0.001 BTC` unit, no adds/DCA, no same-bar conflict possible, entry-bar arm, no cooldown beyond it, deterministic transitions, no capital-dependent branching.
5. **Engine:** exact Hummingbot package/version/commit, BinanceSpotCandles `15m` feed, controller state, OrderExecutor MARKET-close fill, raw/open vs effective/close timestamps, spot accounting, fee/slippage/precision limitations and BacktestPositionHold netting identified by actual immutable code paths; no unverified specialized execution requirement is introduced.
6. **Causality:** 999 completed-bar contiguous warmup (adopting the source's own startup count), point-in-time completed-bar evaluation, no future access, normalized event times and missing-bar fail-closed behavior.

## Evidence and negative evidence

**Primary-source reported:** `Bandtastic.py` at `f3340ce` (163 lines) expressly prints the `15m` frame, the 999-bar startup count, the typical-price 20-bar 1/2/3/4-sigma band set, the RSI14/MFI14/EMA-row columns, the default long entry conjunction (sub-1-sigma close AND positive volume, all oscillator/EMA guards off), the default long exit conjunction (MFI above 46 AND over-2-sigma close AND positive volume), and the full risk block (four-rung ROI ladder, `-0.345` stop, active trailing). The file ships no market, no fill timing, no sizing, and no adopted performance number — this record claims no source-reported performance.

**Independently reproduced:** None. Static pinned-engine source read only, as detailed above, plus a researcher self-check of the band/MFI recurrence and the FLAT/LONG state machine on a synthetic 1010-bar 15m tape in scratch (never committed): dip engineered under the 1-sigma rail, rally engineered over the 2-sigma rail with firming flow — `SELF-CHECK OK: ENTER@bar1000close99.0, EXIT@bar1008close103.5/MFI64.9`, same-bar conflict asserted impossible across the tape — logic verification only, not a backtest, not parity. The file is research-only, not implemented.

**Dedup (main at `546733b`, 335 strategy records, 2026-10-26):** working-tree filename/content search for `Bandtastic` / `bb_lowerband1` / `sell-bb_upper2` returns zero strategy records citing this source file or its dual-rail mechanism (the only `Bandtastic` mention anywhere is a passing prior-art line inside the HLHB record, never a rule). Mechanism cousins fenced as different: `freqtrade-bband-rsi-dip-buy-*` (1h, single 2-sigma typical band, RSI<30 entry / RSI>70 exit — oscillator on both legs, no MFI, no dual rail); `freqtrade-strategy003-*` (5m Fisher/EMA/MFI washout — its typical-price BB column is computed but never read); `freqtrade-emaskippump-*` (5m EMA5/12 plus 12-bar MIN/MAX rails plus 2-sigma BB on both legs — no MFI, no 1-sigma rail); `freqtrade-combined-binh-cluc-*` and `forven-bollinger-*` (BB-penetration breakouts, opposite direction of this washout entry); `percent-b-mfi-dual-thrust-*` (1d two-sided %B/MFI thrust cross, not a 1-sigma/2-sigma rail pair with an MFI-gated exit). No record pairs a 1-sigma typical-price entry rail with a 2-sigma typical-price plus MFI46 exit gate at `15m` long-flat with no risk legs. All currently open `research/*` PRs were inspected for the same source and mechanism (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas, #350 ClucMay72018, #353 Heracles) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant.

**Limitations:** The file's ROI ladder, stop, and trailing block are deliberately not carried over — this derivative is long-flat signal-exit only and is never evidence that the original full-risk source passes. The frozen guard/trigger defaults are the author's published hyperopt fit on undisclosed training data — adopted verbatim, never re-fit, with no portable-edge claim. Close-price fills and modeled fees do not reproduce actual venue microstructure; no spot execution/live approval. The exit needs both the wider-rail reclaim and firm flow, so a position can bleed through a grinding fade that never prints a qualifying exit bar. Qlib/Hummingbot event parity and strategy-specific executable artifact remain future, separately authorized work.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: dual-band arithmetic / MFI14 recurrence / strict legs / disjoint rails / single-unit long-only / `15m` BTCUSDT / same-bar-close fills are frozen.

- F1 — Flow-gate relevance: exiting on every over-2-sigma bar regardless of the MFI46 gate (same entry) must not improve net expectancy; fail ⇒ the money-flow confirmation adds nothing over the naked wide-rail reclaim.
- F2 — Rail-asymmetry relevance: replacing the 1-sigma entry rail with the 2-sigma rail (symmetric washout/reclaim, same exit) must not reproduce-or-beat net expectancy; fail ⇒ the narrow-entry/wide-exit asymmetry adds nothing over a single-rail round trip.
- F3 — Typical-price relevance: rebuilding both rails from close prices instead of typical prices (same sigmas, gate, and pins) must not reproduce-or-beat net expectancy; fail ⇒ the high/low-inclusive typical construction adds nothing over close-only bands.

## Crypto portability

Direct for the long leg on either venue type: single-venue BTCUSDT `15m` completed bars with `high/low/close/volume` fields only. No session calendar (crypto trades continuously; the 20-bar windows and the 999-bar warmup need no session-gap semantics), no corporate actions, no dividends, no funding/OI reads, no cross-venue state. 24/7 continuity means every lookback bar is always the immediately prior print — no weekend-gap discontinuity to normalize. Tick-size rounding follows the venue; no displayed price precision changes any event. The long-only book expresses identically on spot (no margin needed) and on perpetual under a house overlay; it is the same rule on both.

## Implementation status

not-implemented. No dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record; downstream materialization follows the `IMPLEMENTATION_NEEDED` route without revisiting HB_READY admission.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. Any future authorization requires a separate downstream decision outside this repository's admission scope.

## Related Wiki records

None.

## Sources

- Primary GitHub source (pinned, read end to end this run): https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/Bandtastic.py
- Repository: https://github.com/freqtrade/freqtrade-strategies
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
