---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade Bandtastic quad-Bollinger asymmetric MFI-gated long-flat on BTCUSDT 15m bars
created: 2026-10-25
updated: 2026-10-25
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

# Freqtrade Bandtastic quad-Bollinger asymmetric MFI-gated long-flat on BTCUSDT 15m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; sibling files already supply pool records such as `freqtrade-bband-rsi-dip-buy`, `freqtrade-combined-binh-cluc`, `freqtrade-simple-macd-bb-rsi-momentum`, and `freqtrade-macd-cross-cci-edge` — this record pins ONLY the Bandtastic file below).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/Bandtastic.py`.
- GitHub blob SHA at the pinned commit: `f7710c76ae1e4ac7aff90857a647e4c2143baf9f`, size 7310 bytes.
- Byte-identity check: the file downloaded from the GitHub API at the pinned commit is 7310 bytes, 163 lines, and `git hash-object` reproduces `f7710c76…3baf9f` exactly — the entire file was retrieved and inspected.
- Registration: the file defines class `Bandtastic(IStrategy)` (the only class in the file; `INTERFACE_VERSION = 3`). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, every sibling file (`Supertrend.py`, `Diamond.py`, `PowerTower.py`, `HourBasedStrategy.py`, `Strategy001.py`–`Strategy005.py`, `UniversalMACD.py`, `MultiMa.py`, `hlhb.py`, and the whole `berlinguyinca/` subdirectory) is a different pin with different constants — this record pins ONLY the Bandtastic literals below, and no reviewer repair may substitute a sibling constant.
- The file's own words (quoted for gate evidence, never extended): `author: Robert Roman`; `timeframe = '15m'`; `minimal_roi = { "0": 0.162, "69": 0.097, "229": 0.061, "566": 0 }`; `stoploss = -0.345`; `startup_candle_count = 999`; `trailing_stop = True`, `trailing_stop_positive = 0.01`, `trailing_stop_positive_offset = 0.058`, `trailing_only_offset_is_reached = False`; default signal selection `buy_trigger = "bb_lower1"` with `buy_rsi_enabled = False`, `buy_mfi_enabled = False`, `buy_ema_enabled = False` (defaults `buy_rsi = 52`, `buy_mfi = 30`, `buy_fastema = 211`, `buy_slowema = 250` — all gated off at defaults), and `sell_trigger = "sell-bb_upper2"` with `sell_mfi_enabled = True` (default `sell_mfi = 46`), `sell_rsi_enabled = False`, `sell_ema_enabled = False`; entry legs `close < bb_lowerband1` plus `volume > 0`; exit legs `mfi > sell_mfi` AND `close > bb_upperband2` plus `volume > 0`; indicators `ta.RSI(dataframe)`, `ta.MFI(dataframe)`, and four `qtpylib.bollinger_bands(qtpylib.typical_price(dataframe), window=20, stds=N)` blocks for N = 1, 2, 3, 4. No `can_short`, no `use_exit_signal` / `exit_profit_only` override, no `process_only_new_candles`, no order-type mapping ships anywhere — framework defaults below are disclosed as defaults, never as file literals.
- Out-of-file calls pinned (all resolved by name, all standard): `ta.RSI(dataframe)` / `ta.MFI(dataframe)` (TA-Lib abstract defaults, timeperiod 14, pinned by call — disclosed, never overridden in the file); `qtpylib.bollinger_bands(qtpylib.typical_price(dataframe), window=20, stds=N)` returning the `lower`/`mid`/`upper` dict entries (typical price `(high+low+close)/3`, the Freqtrade vendor call pinned by call — its internal rolling arithmetic lives outside this file and is disclosed as such, never re-derived here). `ta.EMA(dataframe, timeperiod=period)` columns are computed for the hyperopt ranges but, at the pinned defaults, are read ONLY inside the disabled EMA guards — dead columns at defaults, fenced below. No DB, no network, no `request.*`, no `security()` in the file.
- Full-file token census (verified over the 163 lines this cycle): 0 `enter_short` / 0 `exit_short` / 0 `short` (case-insensitive — no short leg anywhere); 0 `crossed_` (no edge call — entry and exit are persistent levels, not one-bar edges); 0 `shift` (no lag call — all reads are same-bar); 5 `trailing` (the trailing block quoted above — researcher-disabled in this derived record, see declaration); 1 `startup_candle_count` (`999` — adopted as the researcher warmup floor below); 4 `volume` (the two `volume > 0` gates plus the column itself); 4 `typical_price` (the four band blocks); 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic); 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop/trailing); 0 `resample` / 0 `informative` (single timeframe throughout).
- The file header carries a hyperopt-result comment (`Optimized With Sharpe Ratio and 1 year data`, trade counts and a profit claim). It ships no market, sample window, cost basis, or reproducible table — this record adopts NO source-reported performance (see Evidence).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly six, all predeclared here: (1) research market `BTCUSDT` Binance spot (the source names no market); (2) completed-bar decisions with same-bar-close MARKET fills; (3) single-unit (`0.001 BTC`) / no-add / no-cooldown position pin plus a 1000-bar researcher warmup floor (covers the 20-bar band seed, the 14-bar RSI/MFI seeds, and preserves the source's own 999-bar conservatism with margin); (4) the file's ROI ladder and fixed stop are kept verbatim as bar-close-evaluated legs with strict comparisons and disclosed 15-minute age discretization (see Signal); (5) the file's trailing block is EXPLICITLY DISABLED by researcher choice — its runtime semantics are not reproduced, no trailing leg fires in this record, and no source-equivalence for trailing is claimed (the #416 failure mode is fenced by construction: nothing here asserts what the source trailing does); (6) the house spot cost model (fee `0.001` per side, zero modeled slippage) replaces the absent source economics. Every threshold, every lookback, the 1σ/2σ band asymmetry, the MFI-46 gate, the volume gates, and the ROI/stop literals are untouched.

Pre-write dedup (2026-10-25, main SHA `4deefd8ed820a3559b1ae0e2ec69da1c63475f82`): working-tree filename/content search for `Bandtastic`, `bb_lowerband1`, `buy_trigger`, `sell-bb_upper`, and `Robert Roman` returns zero strategy records. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas, #350 ClucMay72018, #353 Heracles) trades a quad-Bollinger signal. The pool's nearest Bollinger/MFI cousins are fenced as different constructions in Negative evidence 7 — none trades a bare 1σ typical-price lower-band penetration entry with an MFI-gated 2σ upper-band exit on `15m`. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the bar where the close sits under the 1σ typical-price lower band (a shallow-band dip, with RSI/MFI/EMA guards available but defaulted off) provided the candle printed volume; exit when money-flow heat confirms the recovery (`MFI(14)` above 46) AND the close reclaims over the 2σ upper band, with a four-rung time-decaying ROI ladder (16.2% → 9.7% → 6.1% → 0 over 0/69/229/566 minutes) and a −34.5% stoploss behind every position. No behavioural, structural, or risk-premium channel is claimed anywhere in the 163 lines.

### Research interpretation

Shallow-dip buyer with a two-key profit lock, long-only. Unlike deep-penetration systems (2σ breaks demanding microstructure proof — body displacement, tails, pump caps), the entry asks only the 1σ penetration fact plus non-zero volume: RSI can sit anywhere, no trend filter applies, so narrow-range drift-throughs enter exactly like high-conviction breaks. Unlike symmetric band-fade systems (lower-band entry, midline exit), the exit demands the opposite 2σ extreme AND money-flow permission — a midline reclaim without MFI heat holds the position, so slow grinds that never stretch the envelope AND heat up together are held until the ROI ladder or the wide stop. The coded consequence is a buyer of shallow band weakness that harvests only confirmed hot stretch recoveries, time-decayed profit targets, or the disaster stop.

## Signal

Exact rule as pinned (any other band width, multiplier, MFI/RSI length, threshold, gate combination, ROI/stop pair, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own:

```text
typ[t]         = (high[t] + low[t] + close[t]) / 3
bb_lower1[t]   = qtpylib BB(20, 1) lower over typ      // entry band; mid/upper1 computed, never gated
bb_upper2[t]   = qtpylib BB(20, 2) upper over typ      // exit band; lower2/mid2 computed, never gated
                 (stds=3,4 blocks computed, never read by any order line — display-only, fenced below)
rsi14[t]       = TA-Lib RSI(close, 14)                 // computed, never gated at defaults — fenced below
mfi14[t]       = TA-Lib MFI(14)                        // live exit gate
entry          = (close[t] < bb_lower1[t]) AND (volume[t] > 0)                          // enter_long = 1
exit_sig       = (mfi14[t] > 46) AND (close[t] > bb_upper2[t]) AND (volume[t] > 0)       // exit_long = 1
risk           = ROI ladder {"0": 0.162, "69": 0.097, "229": 0.061, "566": 0}
                 (fraction by position age in minutes, bar-close age in 15-minute steps — see below);
                 fixed stop at -34.5% (stoploss -0.345); NO trailing leg (researcher-disabled, declared above)
guard          = leading-window bars: rolling NaN comparisons false (see Required data)
```

- Trade events: `enter_long=1` on any bar printing the penetration level, `direction` long-only; `exit_long=1` on bars printing the MFI-plus-stretch conjunction. Both are persistent levels re-evaluated per bar, not one-bar edges (zero `crossed_`/`shift` in file) — a book already positioned treats further entry bars as hold-no-ops under the position pin below.
- Exact boundaries (pinned semantics): entry strict (`<` — a close exactly on the 1σ lower band fires nothing); both exit conjuncts strict (`>` — MFI exactly 46 or a close exactly on the 2σ upper band holds); the volume gates strict (`>` — zero-volume bars never print). ROI rung fires on strict `profit > rung` at the decision close; the stop fires on strict `profit < -0.345`. Strictness preserved throughout — disclosed, not smoothed.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `close[t]` strictly under the 1σ lower band, hence strictly under the 2σ upper band (`lower1 <= upper2` whenever band width >= 0 with positive prices), so `close[t] > bb_upper2[t]` is false on that bar — entry and signal-exit never co-print outside degenerate non-positive-band windows, which the warmup below excludes. ROI/stop cannot co-fire with entry on the entry bar either (zero distance at the fill). Bar-close evaluation priority for co-firing risk legs on a held bar is fixed `signal > stop > roi` (researcher pin, disclosed — reachable only when the signal exit and a risk leg print together while positioned).
- Direction: long-only. Zero `enter_short`/`exit_short`/`short` tokens ship anywhere, and the framework default `can_short = False` applies (disclosed default, never a file literal) — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the MFI-plus-stretch signal exit, the four-rung ROI ladder, and the −34.5% stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — exits fire even at a loss; disclosed defaults, never file literals). No trailing, no time exit, no breakeven move — explicitly none, not invented. The ROI age clock counts completed 15-minute bars since the entry fill (age_minutes = 15 × bars_held); the active rung is the last rung whose key is <= age_minutes — a disclosed bar-close discretization of the file's minute keys, never claimed as the source engine's intrabar timing.
- Position rule (predeclared researcher pin): single `0.001 BTC` unit, at most one open position; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying penetration bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar OHLCV (`close` for the band comparisons, `high`/`low` inside typical price, `volume` only for the integer-zero gates) with fixed non-negative offsets — no funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path. Freqtrade engine column semantics (`enter_long`/`exit_long` per completed bar) are the file's own framework contract.

## Required data

- Completed `15m` bars of BTCUSDT: `high`/`low`/`close` for the RSI(14)/MFI(14)/typical-price/BB(20, 1–4σ) path and the band comparisons, plus `volume` for the two strict-positivity gates ONLY. No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `15m` (source-native — the file prints `timeframe = '15m'`). One evaluation per completed bar; all windows (20-bar bands, 14-bar RSI/MFI) read the decision bar and its causal past only — no shift tricks, no future reference; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 1000 fifteen-minute bars held flat (~10.4 days). Covers the 20-bar band seed, the 14-bar RSI/MFI seeds, all reads, and preserves the file's own `startup_candle_count = 999` conservatism with margin. Coded behaviour underneath: rolling windows print NaN until seeded and every strict NaN comparison is false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance spot (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close MARKET fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`, repository `HCH725/hummingbot` commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3`, all paths below read at that exact commit during this cycle). No maker-touch, queue, or intrabar-path-dependent fill: entry, the MFI-plus-stretch signal exit, and the ROI/stop legs are all bar-close-evaluated; the Signal mutual-exclusion proof leaves no ambiguous same-bar entry/exit order to the engine, and the fixed `signal > stop > roi` priority covers co-firing risk legs on held bars.
- Pinned-engine evidence (read-only inspection of commit `8b0e067`, this cycle): `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` lists `15m` in `INTERVALS`; `binance_spot_candles/binance_spot_candles.py` passes `interval` to REST and parses `row[0]` (open timestamp, normalized to seconds) plus OHLCV `row[1]`–`row[5]`; `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` (`OrderExecutorSimulator.simulate`) fills `ExecutionStrategy.MARKET` at the first supplied row's `close` as `entry_price`, records `filled_amount_quote = amount * close` and `cum_fees_quote = trade_cost * filled_amount_quote`, and terminates `POSITION_HOLD`; `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` runs `update_state(row)` then `controller.determine_executor_actions()`, accepts `CreateExecutorAction`, and nets exposure through `BacktestPositionHold`. The research decision clock is the completed bar's effective availability time (open_timestamp + 900 seconds); raw engine row labels remain open-time and must not be mistaken for close-time decisions. A controller implementing exactly the Signal transitions is not yet implemented — a downstream engineering artifact, not a second admission criterion.
- Sizing/capital/costs: one `Q = 0.001 BTC` BUY/SELL unit on Binance spot, no leverage/margin/liquidation/futures funding; funding is not applicable, never silently set to a fictitious realized zero-funding stream. Pinned backtest fee is `trade_cost = 0.001` per side on each simulated fill's quote notional; modeled slippage is `0.0` because this pinned MARKET simulator fills at its close input — not a claim of actual zero market slippage. Per completed trade, fee-adjusted research PnL is realized gross quote minus summed `cum_fees_quote`; the executor `net_pnl_quote` alone is not accepted as fee-adjusted cash/equity. Binary-float amount-times-price arithmetic carries no verified exchange tick/lot rounding — a limitation, not a hidden fill.
- Concurrency: at most one position at any time; the penetration level opens the full unit on a flat book; the signal exit, any ROI rung, or the stop closes it in full; re-entry after an exit needs only the next qualifying penetration bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (163 lines: the `ta.RSI`/`ta.MFI` calls, the four typical-price BB(20, 1–4σ) blocks, the default-off guard parameters with their defaults, the `bb_lower1` entry and `sell-bb_upper2` exit selections, the volume gates, the `timeframe`/`minimal_roi`/`stoploss`/`startup_candle_count`/trailing literals, and the `Bandtastic(IStrategy)` class pin). Its header hyperopt comment is quoted in Provenance and adopted for nothing. This record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced. Static pinned-engine source read only, as detailed above. The file is research-only, not implemented.

### Negative evidence

1. Leading-window behaviour fenced: rolling NaNs compare false (no early entry, no early exit). The 1000-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired.
2. Exact-touch rule fenced: strict `<`/`>` fire nothing on equality; a close exactly on either band, MFI exactly 46, or zero volume all hold. Strictness preserved throughout — disclosed, not smoothed.
3. Dead-indicator plumbing fenced: the stds-3/4 band blocks, `bb_middleband*`, `bb_upperband1`, `bb_lowerband2`, `rsi`, and every `EMA_*` column are computed and never read by any order line at the pinned defaults — display-only, never triggers, never repaired into gates.
4. No-heat-exit fenced: the signal exit needs BOTH MFI heat and 2σ stretch — a midline reclaim without MFI above 46 holds the position until the ROI ladder or the −34.5% stop. There is no midline or RSI exit leg; the stop is the sole red-book guardrail besides time-decayed ROI — disclosed, not repaired.
5. Trailing explicitly absent fenced: the source file's trailing block is quoted in Provenance and disabled by predeclared researcher choice. This record's risk set is signal-plus-ROI-plus-stop only; nothing here asserts the source engine's trailing semantics, and the #416 trailing-offset failure mode cannot recur — fenced by construction, not repaired.
6. Zero-variance fenced: flat tape pins band width at 0 with bands on the mean; entry still needs a close strictly under the band and the exit a close strictly over the wider upper band — both unreachable on a pinned flat line, and all gates are comparisons with no division anywhere — disclosed, not repaired.
7. Cousin records fenced as different constructions (none trades a bare 1σ lower-band penetration entry with an MFI-gated 2σ upper-band exit on `15m`): the admitted `freqtrade-bband-rsi-dip-buy` sibling needs an RSI(14)-under-30 AND 2σ lower-band conjunction with an RSI-70 exit on `1h` (heat-gated deep dip, not a bare shallow dip); the admitted `freqtrade-combined-binh-cluc` sibling needs 40-bar body/tail microstructure guards OR an EMA50/discount/pump-cap leg with a profit-gated midline exit on `5m`; the admitted `freqtrade-simple-macd-bb-rsi-momentum` sibling needs MACD-polarity plus a rising 12-bar close-basis upper band plus RSI7 heat on `5m`; the admitted `mfi-threshold-divergence-reversal` sibling trades MFI divergence two-sided on `4h`; the admitted `forven-bollinger-s00120-rsi-breakout` sibling breaks the UPPER rail while RSI reads oversold (opposite direction of trade). Not a threshold re-tuning of any of them: moving the entry width, adding an RSI gate, dropping the MFI conjunct, changing the exit band, or changing the frame would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: every other file in `user_data/strategies/` at the pinned commit (including `Supertrend.py`, `Diamond.py`, `PowerTower.py`, `HourBasedStrategy.py`, `Strategy001.py`–`Strategy005.py`, `UniversalMACD.py`, `MultiMa.py`, `hlhb.py`, and the `berlinguyinca/` subdirectory) is a separate pin — their constants, legs, exits, frames, and risk tuples must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-literal behaviours in this record are the BTCUSDT spot market choice, the same-bar-close fills, the single-unit/no-add/no-cooldown position pin, the 1000-bar warmup floor, the trailing disablement, the bar-close ROI-age discretization with the fixed `signal > stop > roi` priority, the framework-default readings (`can_short=False`, `use_exit_signal=True`, `exit_profit_only=False`, per-completed-bar evaluation), and the spot fee/slippage model — all predeclared above. The `15m` frame, the four band blocks, the 1σ-entry/2σ-exit asymmetry, the MFI-46 gate, the volume gates, the guard defaults, the ROI ladder, and the −34.5% stop are source literals.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: quad-BB(20, typical) / 1σ-entry / 2σ-exit / MFI-46 gate / volume gates / ROI ladder / −34.5% stop / single-unit long-only / `15m` BTCUSDT spot / same-bar-close fills / no-trailing are frozen.

- F1 — Band-asymmetry relevance: replacing the 1σ entry band with the 2σ lower band (same exit/risk) must not improve net expectancy; fail ⇒ the shallow-dip selection adds nothing over the standard deep dip.
- F2 — Exit-conjunction relevance: replacing the MFI-plus-stretch exit with a bare upper-band touch (same entry/risk) must not improve net expectancy; fail ⇒ the MFI heat key adds nothing over the bare stretch exit.
- F3 — Risk-ladder relevance: removing the ROI ladder and stop (signal-only exits) must not improve net expectancy; fail ⇒ the time-decayed targets plus wide stop add nothing over the bare signal machine.

## Crypto portability

BTCUSDT Binance spot `15m` is the declared research market. The rule reads only completed-bar OHLCV with fixed non-negative offsets — no equity-session template, no calendar call, no market-specific microstructure beyond the two integer-zero volume gates. Porting to another spot symbol with a real 15-minute candle feed changes only the feed identity (a different, unpinned rule); porting to a perpetual venue would require an explicit funding/margin treatment this record does not contain. No 24/7-vs-session adjustment is needed for crypto spot, and none is claimed for equities.

## Limitations

No accessible full backtest economics for lossless attribution; market, fills, position pin, warmup, trailing disablement, ROI-age discretization, priority, venue, quantity, and costs are independently designed and disclosed. Close-price fills and modeled fees do not reproduce actual venue microstructure; no spot execution/live approval. The bare 1σ entry with all guards defaulted off can enter narrow-range drift-throughs that never stretch; the two-key exit can hold losing positions through long non-stretch chop until the wide −34.5% stop. The 1000-bar warmup discards the first ~10.4 days of any sample. Qlib/Hummingbot event parity and strategy-specific executable artifact remain future, separately authorized work.

## Implementation status

Not implemented. No controller, no executable recipe, no Qlib entrypoint, no backtest run, no Paper/Testnet/Live artifact exists for this record. Static pinned-engine source compatibility only, as detailed under Execution assumptions.

## Adoption boundary

Research-only. Not approved for Paper, Testnet, or Live trading. PASS (if granted by the independent reviewer) admits the declared derived rule to model-consistent research only — not profitability, Qlib parity, Survivor status, HB Certification, or any trading authorization. Any downstream use requires its own implementation, parity validation, and explicit authorization.

## Related Wiki records

None. No Wiki Brain record was created or consulted for this admission cycle (Scout contract: no Wiki writes).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/Bandtastic.py (primary — all rule citations)
- https://github.com/freqtrade/freqtrade-strategies (repository)
- Pinned engine paths at `HCH725/hummingbot` commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3`, inspected read-only this cycle: `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py`, `hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py`, `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`, `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py`
