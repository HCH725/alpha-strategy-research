---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Alorse RSI-EMA150/600 regime-gated RSI-state reversal long-flat on BTCUSDT 1h bars
created: 2026-10-22
updated: 2026-10-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-16
sources:
  - https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/momentum/RSI%20%2B%20EMA.pine
  - https://github.com/Alorse/pinescript-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Alorse RSI-EMA150/600 regime-gated RSI-state reversal long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/Alorse/pinescript-strategies (open-source Pine collection; the same lane that supplied the twelve admitted `alorse-*` spot records — this is its thirteenth record, and the first pinned to this exact file).
- Pinned commit SHA: `8fb3837ddcd137f1450c3e82d654ff3df24d54d5` (record `source_as_of` is the file's last-commit date at research time, never a fetch date).
- Exact file path: `strategies/momentum/RSI + EMA.pine`.
- GitHub blob SHA at the pinned commit: `cf25d1532cf4d810b7a4e7855a559c6b6cc9734c`, size 1744 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 1744 bytes, 37 lines, SHA-256 `198fe03dad68d77cf615d78fda23da30fb4867f36ef3afd4a82858b60056f2c5`, identical to the GitHub blob (`git hash-object` reproduces `cf25d153…6cc9734c`) — the entire file was retrieved and inspected.
- Registration: the file declares `strategy(title='RSI + EMA [Alorse]', shorttitle='RSI + EMA [Alorse]', overlay=true, pyramiding=0, currency=currency.USD, default_qty_type=strategy.percent_of_equity, initial_capital=1000, default_qty_value=20, commission_type=strategy.commission.percent, commission_value=0.01)` (© alorse, `//@version=5`, MPL-2.0 header). No timeframe is fixed anywhere in the file; no `process_orders_on_close` override ships anywhere.
- The file's own words (quoted for gate evidence, never extended): `rsi_length = input(14, …)`, `rsi_overbought = input(70, …)`, `rsi_oversold = input(30, …)`, `src = input(close, 'Source')`; `up = ta.rma(math.max(ta.change(src), 0), rsi_length)`; `down = ta.rma(-math.min(ta.change(src), 0), rsi_length)`; `rsi = down == 0 ? 100 : up == 0 ? 0 : 100 - 100 / (1 + up / down)`; `ma_type` default `'EMA'`, `ma_length` default `150`; `ma2_type` default `'EMA'`, `ma2_length` default `600`; `ma = ma_type == 'SMA' ? ta.sma(src, ma_length) : ta.ema(src, ma_length)` (and mirror for `ma2`); `longEntry = rsi < rsi_oversold and ma > ma2`; `shortEntry = rsi > rsi_overbought and ma > ma2`; `strategy.entry('Long', strategy.long, when=longEntry)`; `strategy.close('Long', when=rsi > rsi_overbought)`; `strategy.entry('Short', strategy.short, when=shortEntry)`; `strategy.close('Short', when=rsi < rsi_oversold)`.
- Full-file token census (verified over the 37 lines this cycle): 1 `strategy.entry('Long'` / 1 `strategy.close('Long'` / 1 `strategy.entry('Short'` / 1 `strategy.close('Short'`; 0 `strategy.exit` (no stop, no limit, no profit/loss, no trailing leg of any kind anywhere); 0 `strategy.order`; 0 `request.security` / 0 `security(` / 0 `request.*` (single chart timeframe only); 0 `lookahead`; 0 `ta.crossover` / 0 `ta.crossunder` / 0 `ta.cross` (state gates, never edges); 0 `timeframe` input; 0 `pyramid` beyond the `pyramiding=0` declaration; 0 `comment`/`alert_message`; 0 `process_orders_on_close`. All `input.*` calls carry source defaults (14 / 70 / 30 / close / EMA / 150 / EMA / 600) — this record pins those defaults verbatim, never another variant.
- Sibling-file fence: the twelve admitted alors pool-mates pin different files (`MACD + DMI.pine`, `DMI Winner.pine`, `QQE signals.pine`, `StochRSI + Supertrend Strategy.pine`, `Williams Vix Fix.pine`, `Flawless Victory.pine`, `Supertrend + RSI.pine`, `MTF RSI.pine`, `BB + Aroon.pine`, `BB Winner LITE.pine`, `Bollinger Breakout [kodify].pine`, `Exceeded candle.pine`) — their constants and legs must never be substituted into this record.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Pine deployment. The source pins the RSI(14) construction, the EMA150/EMA600 regime conjunction, the `rsi<30` long-entry state, the `rsi>70` long-close state, `pyramiding=0`, and the complete absence of any stop/limit/trailing/time leg — but ships no venue spelling, no fill-timing flag, no warmup guard, no fixed stake, and no timeframe. Researcher-declared adaptations are exactly five: (1) long-flat only — the source's `Short` entry/close pair is disabled, so no naked shorting exists on the spot venue (derivation disclosed, never presented as source-native behaviour); (2) research market `BTCUSDT` Binance spot with the `1h` decision frame (the file names neither; no source-market equivalence is claimed); (3) completed-bar decisions with same-bar-close MARKET fills through the pinned OrderExecutor lane (the file's Pine default is next-bar-OPEN — derivation disclosed, never presented as the source engine's own timing); (4) fixed 100 USDT stake with full-balance exits and a 650-bar researcher warmup pin (the file carries 20%-of-equity dynamic sizing and no length guard — disclosed, never presented as source-native behaviour); (5) modeled cost `trade_cost=0.001` per side with zero additional slippage (the file's nominal 0.01% display commission is quoted as source fact below and is NOT carried as the research cost). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-22): working-tree filename/content search for `rsi-ema`, `ema150`, `ema600`, `RSI + EMA` returns zero strategy records citing this source file or this mechanism. The closest pool strings (`actionzone` dual-EMA zone-transition, `alorse-qqe` QQE trailing-band, `ema-20-50-cross`, `ema-cloud-7-20`, `golden-cross-sma-regime`, `rsi-ma-crossover`, FMZ RSI-family records) are fenced as different constructions in Negative evidence 6. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles KCD-ratio) trades an RSI-state-plus-dual-EMA-regime conjunction. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: hold a long while the market sits in an oversold RSI state inside a slow-EMA uptrend regime (`rsi<30` with EMA150 above EMA600), and close it once the oscillator reaches the overbought state (`rsi>70`). The regime filter can only ever permit entries; the exit is a pure oscillator-state leg. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence). The file's nominal `commission_value=0.01` (0.01% percent-type display commission) is quoted here as source fact and is explicitly NOT the research cost model.

### Research interpretation

Oversold-dip machine inside a slow-trend regime, long-only, long-flat. The EMA150>EMA600 leg supplies the regime veto (dips printed under a slow downtrend print nothing), while the RSI<30 leg supplies the timing state (a healthy uptrend bar without an oversold print holds nothing). Unlike edge-triggered records (one-bar crosses), both legs are persistent states: a qualifying book opens on the first qualifying bar and every further qualifying bar is a hold-no-op by the `pyramiding=0` single-unit pin; the book closes in full on the first `rsi>70` bar. The exit is deliberately regime-blind — even a bar that keeps the uptrend regime is exited on the oscillator state alone — so any regime-conditioned exit would be a different, unpinned rule.

## Signal

Exact rule as pinned (any other RSI length, threshold, strictness, average type/length, state-vs-edge pairing, frame, or book is a different, unpinned rule). All identifiers below are the program's own; every `input` default is a source literal, never a researcher choice:

```text
up[t]   = ta.rma(max(close[t]-close[t-1], 0), 14)   // Wilder smoothing, past-only
down[t] = ta.rma(-min(close[t]-close[t-1], 0), 14)  // Wilder smoothing, past-only
rsi[t]  = down==0 ? 100 : up==0 ? 0 : 100 - 100/(1+up/down)
ma[t]   = ta.ema(close, 150)                        // source default type EMA
ma2[t]  = ta.ema(close, 600)                        // source default type EMA
longEntry[t] = (rsi[t] < 30) AND (ma[t] > ma2[t])   // persistent state, strict
exitLong[t]  = (rsi[t] > 70)                        // persistent state, strict
floor     = leading-window bars: na comparisons false (see Required data)
```

- Trade events: `strategy.entry('Long')` on a bar printing `longEntry` while flat opens the full stake; `strategy.close('Long')` on a bar printing `exitLong` while held sells the entire filled balance. Each leg is a persistent state, not a one-bar edge — a book already positioned treats further `longEntry` bars as hold-no-ops under `pyramiding=0`; a flat book treats `exitLong` bars as no-ops.
- Exact boundaries (pinned semantics): both comparisons are strict (`< 30`, `> 70`, `ma > ma2`) — a bar with `rsi == 30.0` prints no entry leg; a bar with `rsi == 70.0` prints no exit leg; a bar with `ma == ma2` prints no entry leg. All preserved throughout.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `rsi[t] < 30` while any exit bar has `rsi[t] > 70` — mutually exclusive on every bar, degenerate or otherwise, so entry and exit never co-print. There is no ROI/stop/trailing/time leg anywhere (verified zero `strategy.exit` tokens), so no exit-exit ordering exists either. The reviewer is never asked to invent an ordering.
- Direction: long-only (derived, disclosed). The source's `Short` entry/close pair is disabled in this record; the venue is spot with no naked shorting. A two-sided reading would contradict the declared derivative.
- Exits and risk (explicit): the `rsi>70` full-balance close is the complete position-closing set. No stop-loss, no take-profit, no trailing, no time exit, no breakeven move — explicitly none further, verifiable by the zero-`strategy.exit` census above, not invented.
- Position rule (predeclared researcher pin): single-unit spot, at most one open position; fixed 100 USDT buy stake per entry (see Execution assumptions); a positioned book treats further entry-state bars as hold-no-ops (no pyramiding, no averaging — `pyramiding=0` source semantic preserved); a flat book treats exit-state bars as no-ops; re-entry re-arms on any qualifying `longEntry` bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `close` (RMA/EMA recursions with fixed non-negative offsets plus `ta.change` one-bar lookback — no forward reference) with no `request.*`, `security()`, session/calendar call, funding/OI/mark-price read, resample, interpolate, or stop/limit order argument anywhere in the gating path. The decision bar's own forming values are never read.

## Required data

- Completed `1h` bars of BTCUSDT: `close` only for all gating lines (`ta.change`, RMA, EMA all read `close`; no `open`/`high`/`low` read, no bar `volume` read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line). `high`/`low`/`open`/`volume` ride the pinned candle frame as non-gating context only (see Execution assumptions). No multi-symbol, multi-timeframe, or external-feed dependency of any kind (verified zero `request.*`/`security` tokens).
- Single decision timeframe `1h` (researcher pin — the file fixes no timeframe; `1h` rides existing admission precedent on `main` via the ADXMomentum, BbandRsi, and AwesomeMacd records). One evaluation per completed bar; every window reads the decision bar's causal past only; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 650 completed one-hour bars held flat. Covers the EMA600 seed (the dominant lookback), the EMA150 seed, and the Wilder RMA14 seed with margin. The file ships no length guard — quoted absence, never filled in from elsewhere. Coded behaviour underneath: Pine `na` operands compare to `na`, and `when=na` is a no-op — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance spot under the declared derivative (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed). Connector `binance`, trading pair `BTC-USDT`, `backtesting_resolution='1h'`.
- Order timing (derived, disclosed): completed-bar decision with same-bar-close MARKET fills — the decision bar's own close, through `OrderExecutorConfig` with `ExecutionStrategy.MARKET` on the pinned engine path below. No maker-touch, queue, or intrabar-path-dependent fill: the entry state and the exit state are both bar-close-evaluated; the Signal mutual-exclusion proof leaves no ambiguous same-bar fill order; there is no second exit leg of any kind, so no exit-exit ordering assumption is needed. This is NOT the source Pine's default next-bar-OPEN timing — derivation disclosed.
- Pinned-engine path (all files read directly at `hummingbot/hummingbot@fac3a7f8c4adfd9f07f462cfaad9e2ed9e8b6467` during this cycle; `hummingbot/VERSION` at that commit reads `dev-2.17.0`, matching the mandatory 20260920 baseline): `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` `simulate_execution` (lines 282–287) calls `update_state(row)` — which loads the row's `close_bt` into controller prices and the row timestamp into controller time (lines 364–368) — and only then calls `controller.determine_executor_actions()`, simulating each `CreateExecutorAction` on `processed_features.loc[i:]` (line 287), i.e. starting at the decision row itself; `prepare_market_data` (lines 448–480) supplies completed per-tick OHLCV plus volume with `close` pinned to `close_bt`; `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` fills MARKET orders at the first row's `close` (lines 22–24, 56: `entry_price = df_filtered.loc[fill_timestamp, 'close']`), books `filled_amount_quote = amount × entry_price` with `cum_fees_quote = trade_cost × amount_quote` (lines 59–62), and returns `CloseType.POSITION_HOLD` (lines 64–71); the same-file `BacktestPositionHold` (lines 45–123) nets opposite BUY/SELL fills, realizes `(sell_price − avg_entry) × matched` on reduction (lines 73–78), accumulates `cum_fees_quote` across executors (line 119), and reports closed exactly when the net base amount returns to zero (lines 126–127). The claimed decision info set (completed bar `i` OHLCV including its close) therefore coincides exactly with the engine's actual info set (row-`i` `close_bt` loaded before actions) — no open-timestamp claim, no publication lag, no future read.
- Continuity note: `order_executor_simulator.py` at the pinned commit is byte-identical (verified by `diff` this cycle) to the same path at `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` cited by the twelve admitted alors pool-mates — the MARKET-at-first-close plus `trade_cost×notional` plus POSITION_HOLD lane is the same code, now cited at the upstream pin the current contract names.
- First-party test presence (names verified via the contents API at the pinned commit this cycle; read-only, never executed): `test/hummingbot/strategy_v2/backtesting/test_backtest_position_hold.py` (buy/sell netting and full-close accounting), `test_backtesting_final_tick_ledger.py` (POSITION_HOLD terminal ledger), `test_backtesting_engine_directional.py` (candle-driven action/engine fixture exercising `run_backtesting(…, backtesting_resolution, trade_cost)` with an adjustable `trade_cost`, lines 160–175 — that fixture uses the perpetual connector; this record's spot connector and cost values are researcher-pinned, never claimed as tested).
- Sizing/capital (predeclared researcher pins, disclosed): initial capital 1000 USDT (source parity); each entry buys a fixed 100 USDT stake — BTC amount `floor((100 / fill_close) / 0.00001) × 0.00001` (stepSize `0.00001` BTC verified live via `api.binance.com/api/v3/exchangeInfo` for BTCUSDT on 2026-10-22; tickSize `0.01` USDT; NOTIONAL `minNotional 5.0` with `applyMinToMarket=true` — every 100 USDT order passes by 20×); each exit sells the entire filled BTC balance; no compounding (fixed stake every entry). Quantization is controller-side sizing; the pinned simulators fill the given base amount verbatim (`amount_quote = amount × entry_price`, no engine-side rounding — cited lines above), so record and engine agree exactly. The source's 20%-of-equity dynamic sizing is NOT carried (disclosed adaptation).
- Costs (predeclared researcher pins, disclosed): `trade_cost=0.001` per side on fill notional (0.1%/side modeled taker cost), charged inside the pinned simulator as `cum_fees_quote = trade_cost × amount_quote` on both the buy and the sell executor; round-trip cost `0.001 × buy_notional + 0.001 × sell_notional`; reported net of a round trip `(sell_close − buy_close) × matched_BTC − fees`. The source's nominal 0.01% display commission is quoted source fact, never the research cost. Spread/slippage beyond the close fill is modeled as exactly zero (disclosed assumption). Fees affect reported PnL only — no leg in this record reads profit, cost, or balance (verified: no profit/cost reference anywhere in the gating path), so the fee choice cannot change any trade event.
- Futures/DCA/leverage/funding (explicitly excluded from this admitted version, disclosed): this record uses spot 1× with no margin, no leverage, no funding leg, and no Safety Orders. The house BO6%+SO6%+SO6% / Isolated / 3×/5× campaign overlay (baseline §1, a downstream research experiment, never an admission prerequisite) is NOT part of this version — there is no DCA trigger, averaging, or funding settlement to specify, and none is claimed. Per baseline §4, historical funding is unproven in the pinned simulator; this record requires no funding path at all (spot instrument), so that gap does not attach. No liquidation concept exists at 1× spot.
- Concurrency: at most one position at any time; the entry state opens the full stake on a flat book; the exit state closes it in full; re-entry after an exit needs only the next qualifying `longEntry` bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (37 lines: the RMA-based RSI definition with zero-guards, the dual default-EMA regime pair, the `longEntry`/`shortEntry` state pair, the two `strategy.close` state legs, and the `pyramiding=0` / 1000 USD / 20%-equity / 0.01%-commission declaration). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: Pine `na` operands yield `na` comparisons and `when=na` is a no-op (no early entry, no early exit). The 650-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired. The file ships no length guard, so the floor is purely a researcher pin, never misattributed.
2. Exact-touch rule fenced: all three gating comparisons are strict (`rsi < 30`, `rsi > 70`, `ma > ma2`) — a bar sitting exactly on 30.0, 70.0, or with equal averages fires nothing on that leg. Strictness preserved throughout — disclosed, not smoothed.
3. Input-variant fence: `ma_type`/`ma2_type` admit `SMA` as an option in the file, but both default to `'EMA'` with lengths 150/600 — this record pins the source defaults verbatim. An SMA-typed variant would be a different, unpinned rule, never substituted here.
4. Source-quirk fence (no repair): the source's `shortEntry` also requires `ma > ma2` (regime leg shared by both sides) — quoted as-is; the entire short pair is disabled in the derivative, so the quirk has no book effect here and is never "fixed".
5. Dead-leg fence: the `Short` entry/close pair, the `commission_value`, and the `default_qty_value=20` dynamic sizing exist in the source but are all excluded from the derived executable specification above — fenced as non-carried, never silently reactivated.
6. Cousin records fenced as different constructions (none trades an RSI(14)-state-plus-EMA150/600-regime conjunction, long-flat, with a pure `rsi>70` state exit and zero risk legs): the admitted `freqtrade-strategy003` pool-mate trades an RSI-Fisher-MFI triple washout gated by EMA with ROI/stop legs (`5m`); the admitted `freqtrade-cmcwinner` pool-mate trades a CCI+MFI+CMO triple-oversold state (`15m`); the admitted `freqtrade-swinghightosky` pool-mate trades a CCI-RSI dual-threshold state (`15m`); the admitted alors `mtf-rsi14-ema900` pool-mate trades a chart-RSI-vs-EMA900 syntax-normalized state from a different file with a different exit; the admitted alors `macd-dmi14-vstop20` pool-mate trades a MACD-cross-plus-DMI gate with a volatility-stop exit; the `actionzone` pool-mate trades edge-triggered dual-EMA zone transitions. Not a threshold re-tuning of any of them: moving any length/threshold, dropping the regime leg, converting either state to an edge, adding any risk leg, or changing the frame would each be a different, unpinned rule — none is admitted here.
7. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-spot market choice, the `1h` frame pin, the same-bar-close fills, the fixed-100-USDT-stake/full-balance/no-cooldown position pin, the 650-bar warmup floor, the long-only short-leg disablement, and the modeled 0.001/side zero-extra-slippage costs — all predeclared above. The RMA-RSI construction with all its literals and guards, the EMA150/EMA600 regime conjunction with source-default types, the strict `rsi<30` entry state, the strict `rsi>70` full close, the `pyramiding=0` single-unit stance, and the total absence of stop/limit/trailing/time legs are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: RSI(14, Wilder RMA, zero-guards) / strict `<30`+`>70` thresholds / EMA150-vs-EMA600 strict regime with source-default EMA types / persistent-state legs / full-stake open / full-balance close / no risk legs / single-unit long-only / `1h` BTCUSDT spot / same-bar-close MARKET fills / 0.001-per-side costs are frozen.

- F1 — Regime-leg relevance: dropping the `ma > ma2` conjunction (naked `rsi<30`→`rsi>70` state machine, same sizing/costs) must not improve net expectancy; fail ⇒ the slow-EMA regime veto adds nothing over the oscillator alone.
- F2 — Oscillator-timing relevance: replacing the `rsi<30` entry state with immediate entry on every regime-qualified bar (hold the regime while flat, same `rsi>70` exit, same sizing/costs) must not improve net expectancy; fail ⇒ the oversold-state timing adds nothing over the regime alone.
- F3 — Exit-state relevance: replacing the `rsi>70` exit with exit on regime loss (`ma < ma2`, same entry, same sizing/costs) must not improve net expectancy; fail ⇒ the overbought-state exit adds nothing over a regime-mirror exit.

## Crypto portability

BTCUSDT Binance spot `1h` is the research pin (source names no market). Long-only with full-stake open/full-balance close expresses unchanged on any spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. No volume field is consumed at all. No funding leg exists (spot), so portability carries no funding-model dependency.

## Limitations

- The `1h` frame rides existing admission precedent (ADXMomentum, BbandRsi, AwesomeMacd `1h`) — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- A position in a market whose RSI never prints above 70 is held indefinitely; a market that oscillates with hot RSI but no regime prints repeated flat no-ops with nothing to hold. There is no decay, chop, trend-loss, stop, target, trailing, or time exit — disclosed, not repaired.
- Pine indicator internals (`ta.rma` Wilder seeding, `ta.ema` seeding, `ta.change` first-bar `na`) live in the Pine library outside the pinned file — pinned by call with defaults 14/150/600 alongside the 650-bar floor; exact reproduction inherits those seedings.
- The modeled 0.001/side cost with zero extra slippage is a fixed research assumption, not a certified live-truth fee; live spreads, queue effects, and fee tiers are not modeled. Because no gating leg reads profit or cost, this assumption cannot alter a single trade event — it bounds only reported net.
- Exchange filters (stepSize/minNotional/tickSize) were verified live on 2026-10-22 and are quoted as of that date; a future exchange-info change would require a record update, not silent reinterpretation.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists (signal/controller code that maps `longEntry`/`exitLong` to `OrderExecutorConfig` MARKET actions is not written). Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/momentum/RSI%20%2B%20EMA.pine
- https://github.com/Alorse/pinescript-strategies
