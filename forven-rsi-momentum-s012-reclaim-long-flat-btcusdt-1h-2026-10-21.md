---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven S012 RSI-reclaim EMA50/200 ADX-gated long-flat on BTCUSDT 1h bars
created: 2026-10-21
updated: 2026-10-21
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - https://github.com/judder659/Forven/blob/0a8b07fd02ac6864c0102fec08b6ae7ebfa32875/forven/strategies/builtin/rsi_momentum.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven S012 RSI-reclaim EMA50/200 ADX-gated long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-roc`, `forven-ema-cross-adx-regime`, `forven-dema-cross`, `forven-tema-cross`, `forven-hma-cross`, `forven-ema-rsi-pullback-reclaim`, `forven-rsi-s00139-washout-cross`, `forven-rsi-boundary-rejection`, `forven-connors-rsi`, and forty further Forven-sibling records on `main` — this is only its next record, and the first pinned to this exact file).
- Pinned commit SHA: `0a8b07fd02ac6864c0102fec08b6ae7ebfa32875` (verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/rsi_momentum.py`.
- GitHub blob SHA at the pinned commit: `f66f0905c5c32b5850a3261fed69c03915bfcc89`, size 5272 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 5272 bytes, 149 lines, SHA-256 `09befeece1ece8817a8ebaf21e6f915f1b5f263bef3aee4970774732648a6d72`, identical to the GitHub blob (`git hash-object` reproduces `f66f0905…15bfcc89`) — the entire file was retrieved and inspected.
- Registration: the file defines class `RSIMomentumStrategy(BaseStrategy)` (the only class in the file) with `TYPE_NAME = "rsi_momentum"` and roster `STRATEGIES = [("S012-ETH", ...), ("S012-SOL", ...), ("S012-BTC", RSIMomentumStrategy, {"_asset": "BTC"})]` — identity here is class plus file path plus the `S012-BTC` roster leg adopted below, all unique. (`TYPE_NAME = "rsi_momentum"` is shared with the strategy template and the S00139 sibling file — the admitted S00139 record already fences this registry collision; this record never keys identity by `TYPE_NAME` alone.)
- The file's own words (quoted for gate evidence, never extended): module docstring `RSI Momentum strategy — S012 variants.`; `describe()` returns `Buys when the 14-period RSI bounces up from below 40 while price is above the 50 and 200-bar moving averages. Sells when RSI drops below 60.`; `default_params` returns exactly `{ "rsi_period": 14, "rsi_entry": 40, "rsi_exit": 60, "ema_fast": 50, "ema_slow": 200, "adx_period": 14, "adx_min": 0, "leverage": 3.0 }`; `compatible_regimes` returns `{"TREND_UP"}`; `parameter_space()` returns `{ "rsi_entry": (30, 45, 5), "rsi_exit": (60, 80, 5), "adx_min": (0, 15, 5) }` (a documented search surface only — this record freezes the defaults and runs no search, fenced below); decision core `generate_signals` is declared `the SINGLE source of entry/exit logic so the backtest and the live/paper scanner trade the identical signal set` and `generate_signal` delegates its booleans to it (`entries, exits = self.generate_signals(df)`); `Signal` return carries `direction="long"`, `price=round(curr_close, 4)`, and `confidence=min(1.0, curr_adx / 40) if adx_ok else 0.0` (display-only legs, fenced below).
- Out-of-file calls pinned (both resolved by name at the same commit, both read end to end this cycle): `from forven.strategies.indicators import adx, rsi` resolves through that module's PEP-562 `__getattr__` facade (`_FACADE_NAMES` includes `"rsi"` and `"adx"`, verified at lines 864–880 of `indicators.py` at the pinned commit; `indicators.py` blob `fdda8b77429e133372482e25cdff8ea31bd59b2a`, 35784 bytes, `git hash-object` reproduces — byte-identical to the blob already pinned by the admitted ROC sibling) to `forven/scanner.py` (`def rsi(series, period=14)` at line 1917: Wilder's RSI — `delta.clip` gain/loss with `ewm(alpha=1/n, adjust=False, min_periods=n)` smoothing, `rs = gain / loss.clip(lower=1e-9)`, `100 - 100/(1+rs)`; `def adx(df, period=14)` at line 1932: TR from `high`/`low`/`close` plus one-bar shifts, strict-inequality `dm_pos`/`dm_neg`, `ewm(span=period, adjust=False)` ATR/DI/DX chain; `scanner.py` blob `78ab0403ac2fa46f700f206957f49f049a4a22ad`, 472181 bytes, verified this cycle). Both helpers are pure pandas over the passed frame (no DB, no network, no global state in the quoted bodies). The `atr(df, 14)` call inside `generate_signal` feeds only the display `indicators` dict (`atr_14`), never an order-gating line — fenced below.
- Full-file token census (verified over the 149 lines this cycle): 0 `short` (case-insensitive — no short leg, no short identifier anywhere); 0 `stoploss` / 0 `minimal_roi` / 0 `trailing` (no risk legs of any kind — the signal-exit-only posture below is the coded posture, never an omission); 0 `volume` (no volume read of any kind — the decision path reads `high`/`low`/`close` only); 0 `open` (no open read); 0 `funding` / 0 `mark_price` / 0 `liquidation`; 0 `order_types` / 0 `order_time_in_force`; 0 `position_adjust` / 0 `adjust_trade_position` / 0 `custom_stoploss` / 0 `custom_exit` / 0 `custom_stake` / 0 `leverage(` (no sizing callback — the single `"leverage": 3.0` default-params token is a Forven-runner sizing default, fenced below, never a gating leg); 0 `startup_candle_count` / 0 `timeframe` / 0 `can_short` / 0 `use_exit_signal` (no engine-behavior flags — Freqtrade concepts absent); 0 `resample` / 0 `informative` / 0 `request` / 0 `security` / 0 `merge`; 0 negative shifts (the single `.shift(1)` in the file body is the RSI prior-bar read; all scanner-helper shifts are `shift()` one-bar causal reads); 0 hyperopt `*Parameter` spaces (the `parameter_space()` dict is a plain grid declaration, fenced below). The one return line of `generate_signals` applies `.fillna(False)` to both legs — NaN comparisons are explicitly forced false: no leg can fire on an unseeded bar.
- Lineage base: `forven/strategies/base.py` (blob `27508a2a6b8c546e21adefdb97fc0144fabf881b`, 12238 bytes — byte-identical to the blob already pinned by the admitted ROC sibling, `git hash-object` reproduces this cycle) defines the `Signal` dataclass (`entry_signal` / `exit_signal` default False, `direction` default `"long"`); this file passes `direction="long"` explicitly on every return, so the long-only stance is a file literal twice over.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any Forven deployment. The source pins the Wilder-RSI(14) reclaim-of-40 entry, the dual EMA(50/200) level gate, the ADX(14)-floor evaluation, the RSI-rollover-below-60 single exit, the `S012-BTC` roster leg, and the long-only stance — but ships no venue spelling, no timeframe, no fill-timing flag, no warmup guard, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market `BTCUSDT` on Binance **spot** with decision frame `1h` (the file names no market, no venue, and no timeframe; the roster pins `_asset BTC`; venue spelling, symbol normalization, and the `1h` choice are the only market/frame steps, and no source-market or source-frame equivalence is claimed); (2) completed-row decisions with action-row-close MARKET fills on the pinned Hummingbot path below (the file's `price=round(close, 4)` informational leg coincides numerically with the decision-row close but the Forven runner's own fill semantics are not adopted — derivation disclosed, never presented as the source engine's timing); (3) single-unit position pin with hold-no-op semantics, fixed 100 USDT notional on 1000 USDT start with no compounding, plus a 250-bar researcher warmup pin (the file carries no position reference and no length guard — disclosed, never presented as source-native behaviour); (4) the source's absent economics ride explicit pinned costs (`trade_cost=0.001` per filled leg, slippage 0 model assumption, no funding because the venue is spot) while the file's `"leverage": 3.0` Forven-runner default and the house DCA overlay are both **excluded** from this admission version (see Execution assumptions). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-21): working-tree filename/content search for `builtin/rsi_momentum`, `RSIMomentumStrategy`, `PREBUILT` (zero hits outside this draft), and `S012-` (only the S00139 record's registry-collision fence, a different file) returns zero strategy records citing this source file. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles KCD-ratio) trades an RSI-reclaim-plus-dual-EMA-plus-ADX rule. RSI cousins in the pool are fenced as different constructions in Negative evidence 7. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code and `describe()` print: buy the single bar where 14-period Wilder RSI reclaims 40 from below while `close` stands above both the 50-bar and the 200-bar EMAs with the ADX floor evaluated; sell the single bar where RSI rolls over below 60 from above. The file ships no sample, window, trade count, stoploss, profit target, trailing rule, or cost basis — this record adopts no source-reported performance (see Evidence) and no source-reported risk leg.

### Research interpretation

Deep-oversold reclaim inside a long-horizon uptrend, long-only, state-holding. The dual-EMA level gate (50/200, both absolute `close > EMA` comparisons rather than a stack-shape comparison) asks that the bounce happen inside an intact slow uptrend, not a breakdown masquerading as a dip; the RSI reclaim through 40 (deeper than the pullback cousin's 45) asks that the bounce already show measurable momentum recovery rather than a falling knife still accelerating down; the ADX floor at 0 is evaluated every bar and true on every defined bar (ADX∈[0,100] by the verified construction — a vacuous-by-construction gate preserved verbatim, never optimized away). The exit is a single rollover leg (RSI losing 60): a position survives mid-range RSI chop between 40 and 60 and closes only on demonstrated momentum failure — there is no structural-loss leg, no stop, no profit-taking leg, and no time exit. Unlike persistent-state records (trade every bar the condition holds), the reclaim is a one-bar edge event: a book already positioned treats further reclaim bars as hold-no-ops until the rollover print. The failure mode is plain: a grind-down that keeps RSI pinned under 40 never enters at all (opportunity cost, disclosed), while a whipsaw that reclaims 40 then rolls under 60 prints repeated reclaim-then-rollover round trips with no stop and no profit-taking leg (disclosed).

## Signal

Exact rule as pinned (any other RSI period, reclaim/rollover level, EMA pair, ADX floor, edge-vs-state pairing, fill, frame, or book is a different, unpinned rule). All identifiers below are the program's own; helper bodies are the pinned `scanner.py` facades quoted above:

```text
rsi[t]      = WilderRSI(close, 14)   // scanner.rsi: RMA gain/loss, min_periods=14; NaN for bars 1..13
ema50[t]    = close.ewm(span=50, adjust=False).mean()
ema200[t]   = close.ewm(span=200, adjust=False).mean()
adx[t]      = ADX(h/l/c, 14)         // scanner.adx: ewm(span=14) chain, defined from bar 0
trend_ok    = (close[t] > ema50[t]) AND (close[t] > ema200[t])
adx_ok      = (adx[t] >= 0)          // vacuous-by-construction, evaluated verbatim
entry       = (rsi[t-1] < 40) AND (rsi[t] >= 40) AND trend_ok AND adx_ok   // one-bar reclaim edge
exit_sig    = (rsi[t-1] >= 60) AND (rsi[t] < 60)                          // one-bar rollover edge
both legs .fillna(False): NaN comparisons never fire
```

- Trade events: `entry_signal=True` on a bar printing the reclaim edge with both level gates green, `direction` long-only; `exit_signal=True` on a bar printing the rollover edge. Each print is a one-bar edge, not a persistent state — a book already positioned treats non-exit bars (including further reclaim edges) as hold-no-ops under the position pin below.
- Exact boundaries (pinned semantics): the reclaim is strict below on the prior bar (`< 40`) with inclusive reclaim (`>= 40`); the rollover is inclusive above on the prior bar (`>= 60`) with strict loss (`< 60`) — a bar with `rsi == 40` on both bars fires neither reclaim nor rollover on that pair; a bar reclaiming exactly to `40.0` fires the entry RSI pair; a bar rolling exactly to `60.0` does not fire the exit pair. The EMA comparisons are strict (`>`); the ADX comparison is inclusive (`>=`). All preserved throughout.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `rsi[t-1] < 40` while any signal-exit bar has `rsi[t-1] >= 60` — the prior-bar legs are arithmetically disjoint on every bar, NaN or otherwise (NaN fails both strict/inclusive comparisons, and the coded `.fillna(False)` forces both legs false). Entry and signal-exit never co-print, so the reviewer is never asked to invent an ordering.
- Direction: long-only. Zero short-leg tokens ship anywhere and `direction="long"` is passed explicitly on the single `Signal` return — a two-sided reading would contradict the file.
- Exits and risk (explicit): the rollover signal exit is the complete position-closing set. No stoploss, no profit target, no trailing, no time exit, no breakeven move — the file ships none (census-verified absence quoted above), explicitly none further, not invented and never to be added by repair.
- Position rule (predeclared researcher pin): single-unit, at most one open position; a positioned book treats further reclaim edges as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats the rollover leg as a no-op; re-entry re-arms on any qualifying reclaim bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low`/`close` (Wilder RMA plus span-EMAs with fixed non-negative offsets, plus the single one-bar RSI lookback — no forward reference) with exactly one `.shift(1)` call in the file body and only causal `.shift()` reads inside the quoted helper bodies; the decision bar's own forming values are never read. No funding/OI/mark-price read, no volume read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path. `generate_signal` delegates its booleans to `generate_signals` by the file's own single-source declaration, so the per-bar and vectorized readings cannot diverge.

## Required data

- Completed `1h` bars of BTCUSDT: `high`/`low`/`close` only (RSI and both EMAs on `close`; ADX on `high`/`low`/`close`; the display-only `atr_14` on the same three columns but gating nothing). No `open` read, no bar `volume` read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision frame `1h` (researcher choice — the file names no timeframe; one evaluation per completed bar; every window reads the decision bar's causal past only, plus the one-bar RSI lookback; fills land on the action row's own close under the verified engine path below).
- Warmup (researcher pin, disclosed): 250 completed `1h` bars held flat. Covers the Wilder-RSI `min_periods=14` seed, the ADX chain stabilization, and the span-200 EMA convergence with margin. The file ships no `startup_candle_count` — quoted absence, never filled in from elsewhere. Coded behaviour underneath: `min_periods=14` prints NaN until seeded and the return-line `.fillna(False)` forces every unseeded leg false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization. The pinned engine additionally drops NaN-feature rows itself (`dropna` in the verified `prepare_market_data` body quoted below).

## Execution assumptions

- Research market: BTCUSDT on Binance **spot** under the explicit pins below (researcher choice — the file names no market and no venue; the `S012-BTC` roster leg is the only asset step, and no source-market equivalence is claimed). Spot is chosen deliberately: a spot venue has no funding concept, no liquidation, and no margin accounting, so no unproven perpetual-economics path is claimed anywhere in this record.
- Pinned engine path (verified first-hand this cycle at the immutable tree, never inherited from a sibling record): `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (committed 2026-09-20, `hummingbot/VERSION` literally `dev-2.17.0`, matching the canonical pinned package `20260920` vintage):
  - `BacktestingEngineBase.run_backtesting(controller_config, start, end, backtesting_resolution="1h", trade_cost=0.001)` — `trade_cost` is an explicit run-input override (the engine default `0.0002` is not used; quoted signature read this cycle).
  - `initialize_candles_feed(CandlesConfig(connector="binance", trading_pair="BTC-USDT", interval="1h"))` — the Binance spot connector with dash-form spot pair, the same connector/pair spelling whose `MARKET` + `POSITION_HOLD` spot usage is covered by the pinned revision's own `test_backtesting_final_tick_ledger.py` (verified `connector_name="binance", trading_pair="ETH-USDT"` lines this cycle; tests inspected, not executed by us).
  - `prepare_market_data` merges controller features with `pd.merge_asof(..., left_on="timestamp_bt", right_on="timestamp", direction="backward")`, backfills `timestamp = timestamp_bt`, copies `open/high/low/close/volume` from the `_bt` completed-candle columns, and `dropna`s incomplete rows (body read this cycle) — only feature rows at or before the candle row can attach; no forward reference exists in this path.
  - `simulate_execution` visits each prepared row and routes the controller's `CreateExecutorAction(OrderExecutorConfig)` over the slice starting at the action row (`processed_features.loc[i:max_ts]`); the existing `StopExecutorAction` branch is never taken by this version (no stop legs exist). Routing is strictly by config type (`simulate_executor` body read this cycle) — this version uses **only** `OrderExecutorConfig`; the DCA/position/grid simulator paths are never invoked.
  - `OrderExecutorSimulator.simulate` with `ExecutionStrategy.MARKET`: `fill_timestamp = df['timestamp'].iloc[0]` (the action row's own timestamp), `entry_price = close at fill_timestamp` (the action row's own close), `cum_fees_quote = trade_cost × amount_quote`, close type `POSITION_HOLD` (full body read this cycle). No maker-touch, no queue, no limit-price chase, no intrabar-path-dependent fill.
  - `BacktestPositionHold._process_order` nets same-asset BUY/SELL automatically with matched-volume realized PnL; a SELL of the full filled base quantity zeroes the net and closes the hold (`is_closed`; class body read this cycle) — this is the exit mechanism for the rollover leg. No triple-barrier, no DCA averaging, no grid levels are configured anywhere in this version.
- Order timing (derived, disclosed, code-backed): completed-row decision with action-row-close MARKET fills. Decision inputs, availability stamp, and fill stamp are all the action row's own model timestamp — this is stated as the pinned model's self-consistent row convention as verified in the bodies above, **not** as a wall-clock close-time relabeling claim: no close-time restamping or availability-shift primitive is asserted beyond what the quoted lines show, and any live-trading availability lag is explicitly scoped out in Limitations. The Signal mutual-exclusion proof leaves no ambiguous same-row signal fill order, and with no stop/target legs there is no same-row TP/SL ordering question at all.
- Sizing/capital/costs (explicit, this version): start capital 1000 USDT; fixed 100 USDT notional BUY per entry (no compounding); SELL orders size the full actually-filled base quantity so a rollover exit flattens exactly; amounts quantize to the connector's published base increment and sub-min-notional orders are skipped (never synthetic fills). Cost per filled leg is the run-input `trade_cost=0.001` (0.10%), matching the Binance regular-user spot taker `0.1000%`/`0.1000%` (0.0750% only with BNB deduction — not assumed) read from the official fee schedule this cycle; the no-discount full rate is conservative by construction. Slippage is a 0 model assumption, disclosed. Funding is not modeled because the venue is spot, where the funding concept does not exist — no hypothetical zero is reported as realized funding. Precision/rounding ride the connector trading rules loaded by the verified `initialize_trading_rules` path.
- DCA exclusion (stated plainly to close the gate-4 loop): the downstream house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) is **not part of this admission version** — this version is single-unit spot 1x with no safety orders, no averaging, and no leverage (the file's `"leverage": 3.0` Forven-runner default is a non-adopted sizing token, disclosed, never executed). If the overlay is ever applied downstream, that execution is a separately declared derivative with its own trigger/cost/causality proof, never a silent extension of this record. DCA is not an admission requirement and none is added here.
- Concurrency: at most one position at any time on the single market; the reclaim edge opens the full unit on a flat book; the rollover exit closes it in full; re-entry after an exit needs only the next qualifying reclaim bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (149 lines: the `default_params`/`parameter_space`/`compatible_regimes` declarations, the `generate_signals`/`generate_signal` pair with the single-source declaration, the `S012-*` roster, and the `RSIMomentumStrategy` class pin, plus the two pinned pure helpers quoted above). It ships no sample, window, trade count, risk leg, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: Wilder-RSI prints NaN for bars 1–13 (`min_periods=14`) and the return line forces `.fillna(False)` on both legs — no entry, no exit before seeding. The 250-bar record-rule floor additionally holds every pre-convergence bar flat — disclosed, not repaired. The file ships no `startup_candle_count`, so the floor is purely a researcher pin, never misattributed.
2. Exact-touch rule fenced: the reclaim is strict-below/inclusive-above (`prev < 40`, `curr >= 40`); the rollover is inclusive-above/strict-below (`prev >= 60`, `curr < 60`); EMAs strict (`>`), ADX inclusive (`>=`). A bar sitting exactly on either threshold satisfies exactly the inclusive side — strictness and inclusivity preserved throughout, disclosed, not smoothed.
3. Vacuous-ADX fence: `adx_min = 0` with ADX∈[0,100] by the verified scanner body makes `adx_ok` true on every defined bar. It is evaluated verbatim on every bar and preserved — deleting it would be a different, unpinned rule. Disclosed as construction fact, never reinterpreted as a trend filter and never optimized away by repair.
4. Display-only plumbing fenced: `atr_14`, `curr_ema_fast/slow`, `curr_adx`, `trend_ok`, `oversold/overbought` echoes inside the `indicators` dict, plus `confidence = min(1.0, adx/40)` and `price=round(close, 4)`, gate no order — the booleans come solely from `generate_signals`. The file's `price` leg coincides numerically with the derivative's action-row-close fill but the Forven runner's fill semantics are not adopted. The `compatible_regimes = {"TREND_UP"}` set is descriptive metadata with no read anywhere in the gating path. The `parameter_space()` grid is an unexplored search surface — defaults frozen, no search run. None is repaired into a leg.
5. Helper-alias fence: `_get_oversold()`/`_get_overbought()` resolve through default params to exactly 40/60 (no `"oversold"`/`"overbought"` override keys ship anywhere) — deterministic literals, never alternate sources.
6. Dead-name fence: `talib`/`qtpylib`-style library indicators, `stochastic`, `williams_r`, funding/OI facades, and the scanner's enrichment/DB paths are never imported or called by this file — the only out-of-file names are the two pinned pure helpers. Zero fitted values anywhere in this artifact.
7. Cousin records fenced as different constructions (none trades a Wilder-RSI40-reclaim gated by dual absolute EMA50/200 levels with an ADX floor and a single RSI60-rollover exit, long-flat): the admitted `forven-ema-rsi-pullback-reclaim` pool-mate trades a 12/34 EMA-stack-shape gate with a 45-reclaim entry and a dual 62-rollover/EMA-loss exit on SOL (different EMA pair, different gate shape, different thresholds, dual exit); the admitted `forven-rsi-s00139-washout-cross` pool-mate trades a different file's washout-cross construction (different entry/exit events); the admitted `forven-rsi-boundary-rejection` pool-mate is two-sided with boundary-fade exits (different direction, different exits); the admitted `forven-connors-rsi` pool-mate trades a three-component Connors composite (different inputs); the admitted freqtrade `BbandRsi`/`strategy003` pool-mates come from different sources with BB-penetration and Fisher/MFI legs this file never reads. Not a threshold re-tuning of any of them: moving any period, level, gate, or exit leg would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: every other `forven/strategies/builtin/*.py` file (including `rsi_momentum_s00139.py`, `ema_rsi_pullback.py`, `macd.py`, `awesome_oscillator.py`) is a separate pin — its constants, legs, exits, and risk pairs must never be substituted into this record. The reviewer may verify source facts but must not invent an adaptation to rescue this PR.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-spot market choice, the `1h` frame choice, the action-row-close MARKET fills with the pinned trade_cost/slippage/no-funding pins, the single-unit/no-add/no-cooldown position pin with fixed 100 USDT notional, the 250-bar warmup floor, and the DCA/leverage exclusions — all predeclared above. The Wilder-RSI(14) reclaim-of-40 entry with all its literals and strictness, the dual EMA(50/200) level conjunction, the evaluated ADX(14)-at-0 floor, the single RSI-rollover-below-60 exit, the mutual-exclusion arithmetic, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: Wilder-RSI(14) / 40-reclaim / 60-rollover edges with pinned strictness / EMA(50/200) dual-level gate / ADX(14)-at-0 floor / one-bar-edge legs / single signal exit / single-unit long-only / `1h` BTCUSDT spot / action-row-close fills / `trade_cost=0.001` are frozen.

- F1 — Exit-leg relevance: a no-exit variant (enter on the same reclaim pin, hold every position to the sample end, same sizing/costs) must not improve net expectancy; fail ⇒ the rollover exit adds nothing over buy-and-hold-reclaims.
- F2 — Edge-timing relevance: a persistent-state variant (long whenever `rsi >= 40` with both level gates green, flat whenever the rollover prints, same exit) must not improve net expectancy; fail ⇒ the one-bar reclaim edge adds nothing over the level state.
- F3 — Gate relevance: a naked variant (reclaim/rollover edges alone, both EMA gates and the ADX floor dropped, same risk) must not improve net expectancy; fail ⇒ the dual-EMA-plus-ADX conjunction adds nothing over the bare RSI oscillator.

## Crypto portability

BTCUSDT Binance spot `1h` is the research pin (source names no market; the `S012-BTC` roster leg is the only asset step). Long-only with full-unit open/close expresses natively on a spot venue with no naked shorting and no margin. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. No volume field is consumed at all. Funding is declared nowhere because the venue is spot, where funding does not exist.

## Limitations

- The `1h` frame and the BTCUSDT-spot venue are researcher choices (the file is frame- and venue-agnostic); a different frame or venue would be a different, unpinned rule. The `1h` interval rides existing admission precedent on `main` — no novel-interval confirmation burden attaches to this record.
- The pinned model's row-timestamp convention is a backtest-model convention: decision inputs, availability stamp, and fill stamp coincide on the action row by the verified code, which is exactly what the admission claims and no more. Live-trading availability lag (act only after the close prints plus latency) is not modeled here and is scoped out — PASS is downstream research admission, not live equivalence.
- A position whose RSI never prints the rollover edge is held indefinitely (no stop, no target, no time exit — disclosed, not repaired); a market that reclaims 40 but loses both EMA levels holds nothing (entry needs all three green simultaneously).
- Span-EMA internals converge asymptotically from bar 0; exact reproduction inherits the pinned `ewm(adjust=False)` seeding alongside the 250-bar floor — a shorter history would shift early EMA values, which is why pre-floor bars are flat by record rule.
- The `parameter_space()` grid, the `compatible_regimes` tag, the `confidence` score, and the file's `"leverage": 3.0` token are not executed anywhere in this version — fenced, never to be added by repair.
- No trailing, no breakeven, no short leg, no cooldown, no DCA — all explicitly absent, never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/judder659/Forven/blob/0a8b07fd02ac6864c0102fec08b6ae7ebfa32875/forven/strategies/builtin/rsi_momentum.py
- https://github.com/judder659/Forven
- Engine code https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Engine VERSION https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/VERSION
- Existing tests https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3/test/hummingbot/strategy_v2/backtesting
- Existing six gates https://github.com/HCH725/alpha-strategy-research/blob/main/.github/HB_READY_REVIEW.md
