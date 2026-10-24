---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade triple-Supertrend unison long-flat on BTCUSDT 1h bars
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
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/Supertrend.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade triple-Supertrend unison long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the same repository that supplied the twenty-three admitted `freqtrade-*` records, including the `BbandRsi` sibling that pins the identical commit below).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/Supertrend.py`.
- GitHub blob SHA at the pinned commit: `757b15214c0088b38973b3eb0d6bd56bfcfbf56c`, size 6448 bytes, 156 newline-terminated lines (`git hash-object` reproduces `757b1521…fbf56c`, SHA-256 `c73d2dc221e2a52274b20846bed0879212eaca72916948e8c6103f4d4dd8aeea` — the entire file was retrieved and inspected this cycle).
- Registration: the file defines class `Supertrend(IStrategy)` (the only class in the file), `INTERFACE_VERSION = 3`, `timeframe = '1h'`, `startup_candle_count = 199`. Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path plus author line `@juankysoriano`, all unique.
- The file's own words (quoted for gate evidence, never extended): docstring `Generate a 3 supertrend indicators for 'buy' strategies & 3 supertrend indicators for 'sell' strategies` / `Buys if the 3 'buy' indicators are 'up'` / `Sells if the 3 'sell' indicators are 'down'`; caveat block stating the vendored `supertrend` implementation follows `freqtrade-strategies#30` discussion comment `853042401` and is explicitly `not validated; meaning this that is not proven to match the results by the paper where it was originally introduced or any other trusted academic resources` (disclosed, never upgraded); `buy_params = { "buy_m1": 4, "buy_m2": 7, "buy_m3": 1, "buy_p1": 8, "buy_p2": 9, "buy_p3": 8 }`; `sell_params = { "sell_m1": 1, "sell_m2": 3, "sell_m3": 6, "sell_p1": 16, "sell_p2": 18, "sell_p3": 18 }`; `minimal_roi = { "0": 0.087, "372": 0.058, "861": 0.029, "2221": 0 }`; `stoploss = -0.265`; `trailing_stop = True`, `trailing_stop_positive = 0.05`, `trailing_stop_positive_offset = 0.144`, `trailing_only_offset_is_reached = False`; entry `enter_long = 1` when the three `supertrend_N_buy_{m}_{p}` legs read `'up'` with `volume > 0`; exit `exit_long = 1` when the three `supertrend_N_sell_{m}_{p}` legs read `'down'` with `volume > 0`; `supertrend_direction` keeps pre-warmup `None` as the empty string via `.fillna('')` so cold bars never equal `'up'`/`'down'`.
- Vendored indicator pinned (actually read, second immutable artifact): `technical.indicators.supertrend` from https://github.com/freqtrade/technical at commit `5852e5407588ad04d539f5d5071c60d9dc69b95a` (repository HEAD via `git ls-remote` this cycle), file `technical/indicators/supertrend.py`, blob `eba46c8b4e7322a53934a775cc281dd48332d146` (`git hash-object` match), 1873 bytes. Its exact construction, transcribed into the Signal section below: TA-Lib `TRANGE` true range, ATR as `rolling(period).mean()` (SMA, never Wilder), `hl2 ± multiplier·ATR` basic bands, prior-bar-ratcheted final bands looped from `i = period`, `st` band-state machine, direction `None` wherever `st == 0` (warmup) else `'up'`/`'down'` by `close < st`. Pure completed-bar reads (`high`/`low`/`close` at `i` and `i-1` only) — causal by construction.
- Full-file token census (verified over the 156 lines this cycle): 0 `enter_short` / 0 `exit_short` / 0 `can_short` / 0 `short` (no short leg anywhere); 1 `stoploss` (`-0.265`), 1 `minimal_roi`, 4 `trailing_stop*` lines (the complete risk stack, nothing else); 0 `informative` / 0 `resample` / 0 `merge_informative` / 0 `custom_exit` / 0 `custom_stoploss` / 0 `adjust_trade_position` / 0 `order_types` / 0 `order_time_in_force` / 0 `leverage` / 0 `funding` / 0 `mark_price` / 0 `security` / 0 `request` / 0 `process_only_new_candles` / 0 `use_exit_signal` / 0 `exit_profit_only` (framework defaults below are disclosed as defaults, never file literals); 2 `volume` (the two `> 0` gates only); 0 `ta.` uses (`import talib.abstract as ta` ships but is never called — dead import, fenced); 6 `IntParameter` declarations whose `.range` loops in `populate_indicators` build a 630-combination hyperopt scaffold the entry/exit legs never address (legs read only `self.buy_m1.value` etc., which load from `buy_params`/`sell_params` — the scaffold is search surface, never a second rule).
- Framework defaults applied (disclosed, never file literals): `can_short = False` (long-only corroboration), `use_exit_signal = True` with `exit_profit_only = False` (the `exit_long` leg closes even at a loss), one evaluation per completed bar.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Freqtrade deployment. The source pins the triple-leg unison entry/exit with all six `(multiplier, period)` pairs, the `volume > 0` gates, the `1h` frame, the 199-bar startup floor, the long-only stance, and the full risk literals (`-0.265` stop, `{0: 8.7%, 372: 5.8%, 861: 2.9%, 2221: 0%}` ROI ladder, 5%-distance trailing with the offset inoperative). Researcher-declared adaptations are exactly five: (1) research market `BTCUSDT` spot (the file names no market); (2) completed-bar decisions with MARKET fills at the decision bar's own close on the cited pinned-engine path (freqtrade fills are engine-side; derivation disclosed, never a source claim); (3) single-unit `0.001` BTC position pin with controller-memory state machine, co-print hold pin, and per-bar precedence `exit-signal > stop > ROI > trailing` (the file ships no sizing and no multi-leg precedence); (4) bar-close evaluation of the stop/ROI/trailing legs (freqtrade evaluates risk intrabar; this record evaluates every leg on completed-bar closes — disclosed approximation, never presented as the Freqtrade engine's timing); (5) the pinned research cost model below (fee 0.001/side post-hoc, slippage 0, funding not applicable on spot). This record is therefore never evidence that the original source strategy itself passed.

Pre-write dedup (2026-10-25): working-tree search for `strategies/Supertrend.py`, `juankysoriano`, `supertrend_1_buy`, `supertrend_1_sell`, `buy_m1` returns zero strategy records — no pool record cites this file. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian band-ratio) trades a triple-Supertrend unison leg. Not a duplicate, paraphrase, or trivial parameter variant: the six-leg two-parameter-set unison trigger with the volume gate and the stop/ROI-ladder/trailing stack is fenced against every Supertrend-family pool-mate in Negative evidence 6–8.

## Economic mechanism

### Source-reported

The source claims only what its code prints: hold long exposure while three differently-parameterized Supertrend bands agree the tape points up (`(4,8)`, `(7,9)`, `(1,8)` all `'up'` with traded volume), stand back to flat when a second, slower triple set agrees it points down (`(1,16)`, `(3,18)`, `(6,18)` all `'down'`). Every position carries a −26.5% stop backstop, a duration-relaxed ROI ladder (8.7% fresh, 5.8% past 372 min, 2.9% past 861 min, breakeven past 2221 min), and a 5%-distance trailing floor armed from entry. The file's only prose beyond authorship is the hyperopt-generation comment (values came from `ShortTradeDurHyperOptLoss` on `20210101-`/`1h`) and the not-validated caveat — a provenance note, never a second trigger. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Triple-confirmation trend rider, long-only, belt-and-suspenders exits. Unlike single-band flip records (one ATR band changes its mind and the book obeys), this machine demands three bands with deliberately mismatched speeds to hum the same note — a lone-band whipsaw prints nothing, and the exit legs are an entirely different, slower triple set, so entries and exits are asymmetric by construction (a fast up-alignment can open while the slow down-set stays silent, and vice versa). The risk stack means most positions end on a barrier, not on the signal: verified this cycle on a 1200-bar synthetic 1h tape (pinned seed 7), 23 closed trades split across ROI-take and signal exits. The honest structural footnote: with trailing armed from entry, the −26.5% stop literal is shadowed — the effective floor from the first bar is peak-profit-minus-5%, so the stop survives in the record only as the `max()` anchor, disclosed, never repaired.

## Signal

Exact rule as pinned (any other multiplier, period, leg count, gate, risk literal, fill, frame, book, or precedence is a different, unpinned rule). All identifiers below are the program's own, with the vendored construction transcribed verbatim:

```text
TR[i]        = max(high-low, |high-close[i-1]|, |low-close[i-1]|)   // TA-Lib TRANGE
ATR(p)[i]    = mean(TR[i-p+1 .. i])                                 // SMA, NaN until seeded
basic_ub     = hl2 + m*ATR(p);  basic_lb = hl2 - m*ATR(p)           // hl2=(high+low)/2
final_ub[i]  = basic_ub[i] if basic_ub[i]<final_ub[i-1] or close[i-1]>final_ub[i-1] else final_ub[i-1]
final_lb[i]  = basic_lb[i] if basic_lb[i]>final_lb[i-1] or close[i-1]<final_lb[i-1] else final_lb[i-1]
st[i]        = band-state machine over (final_ub, final_lb, close)  // looped from i=p
dir(m,p)[i]  = '' while st==0; else 'up' if close>=st else 'down'
entry_t      = (dir(4,8)=='up') & (dir(7,9)=='up') & (dir(1,8)=='up') & (volume>0)
exit_sig_t   = (dir(1,16)=='down') & (dir(3,18)=='down') & (dir(6,18)=='down') & (volume>0)
profit_t     = close_t/entry_close - 1;  peak_t = max(profit over open bars);  dur_t = (t-entry_bar)*60 min
stop_t       = (profit_t <= -0.265)
roi_t        = (profit_t >= rung(dur_t)), rung = 0.087/0.058/0.029/0.0 at dur >= 0/372/861/2221
trail_t      = (profit_t < max(-0.265, peak_t - 0.05))
```

- Trade events: `enter_long` on a unison-up bar with volume; `direction` long-only; position-ending legs per completed bar in fixed precedence `exit_sig > stop > roi > trail` (researcher pin, disclosed — the file orders no multi-leg tie). A flat book enters one full unit (`0.001` BTC) on an entry bar; a long book exits the full unit on the first firing leg.
- Exact boundaries (pinned semantics): leg equality is string-exact (`'up'`/`'down'` — the pre-warmup `''` never matches); the volume gate is strict (`> 0` — a zero-volume bar vetoes even a perfect unison); stop/ROI/trailing use `<=`/`>=`/`<` exactly as coded above; ROI rung steps at `dur >=` each key. The `0.144` offset never enters any comparison (`trailing_only_offset_is_reached = False` — disclosed reading, not repaired).
- Co-print pin (researcher rule, disclosed): entry and exit-signal on the same bar hold the prior state — flat stays flat (no entry), long stays long on the signal (the entry is a hold-no-op; barriers still evaluate normally). Zero co-print bars observed on this cycle's 1200-bar tape, so the pin is unexercised but fully specified; the reviewer is never asked to invent an ordering.
- Entry-bar exclusion proof (no self-exit): on the entry bar `profit = 0`, `dur = 0` — signal co-print is absorbed by the pin above, stop needs `≤ -26.5%`, ROI needs `≥ 8.7%`, trailing needs `< max(-26.5%, -5%)`. Asserted this cycle: no leg can fire on its own entry bar.
- Direction: long-only. Zero `enter_short`/`exit_short`/`can_short`/`short` tokens ship anywhere and the framework default `can_short = False` applies — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the slow-triple signal, the −26.5% stop, the four-rung ROI ladder, and the 5%-distance trailing floor are the complete position-closing set (`use_exit_signal = True`, `exit_profit_only = False` defaults — exits fire even at a loss). No breakeven move, no second stop, no time exit beyond the ladder's 2221-minute breakeven rung — explicitly none, not invented.
- Position rule (predeclared researcher pin): single-unit (`0.001` BTC fixed base quantity), at most one open position; a positioned book treats further entry bars as hold-no-ops — no pyramiding, no averaging; a flat book treats all risk legs as no-ops; re-entry re-arms on any qualifying unison bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: every leg reads only completed-bar `high`/`low`/`close`/`volume` with fixed non-positive offsets (the `i-1` ratchet reads, the rolling ATR window, zero negative shifts); no funding/OI/mark-price read, no `request.*`, `security()`, hyperopt parameter, or stop/limit order argument anywhere in the gating path. The 630-combination `IntParameter` scaffold is build-time search surface read by zero order-gating comparisons (fenced, never promoted).

## Required data

- Completed `1h` bars of BTCUSDT: `high`/`low`/`close` (six Supertrend constructions, band comparisons, profit/peak math) and `volume` (the two `> 0` gates). No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1h` (source-native — the file prints `timeframe = '1h'`). One evaluation per completed bar; all windows (max period 18, ratchets, duration clock) read the decision bar and its causal past only.
- Availability mapping (pinned-engine support, not assumed): Binance spot REST kline row `timestamp` is the bar OPEN time (`binance_spot_candles.py` `_parse_rest_candles`, `row[0]`, same pinned engine commit below) and the row retains base volume at `row[5]`; the websocket path maps `data["k"]["v"]` to `volume`. The decision/fill effective time for row `t` is `timestamp_t + 3600s` (the bar's close time — exact for contiguous fixed-interval klines). At that instant every input bar `≤ t` is complete and `close_t`/`volume_t` are the current market prints: signals read no future, fills take no future. Contiguity rule (deterministic data rule, disclosed): a bar whose `timestamp` does not equal the previous bar's `timestamp + 3600s` (a gap) carries no decision and no fill — the book holds its prior state across the gap; prices are never fabricated, missing bars are never interpolated.
- Warmup (source-native, never shortened): `startup_candle_count = 199` completed `1h` bars held flat — the file's own floor, covering the max 18-bar ATR seed, both ratchet chains, and all six direction series with margin. Coded behaviour underneath: `st == 0` bars yield `None` → `''`, matching neither `'up'` nor `'down'`; every strict/NaN comparison before seeding is false. Raw-leg prints observed before bar 199 on this cycle's synthetic tape (24 entries, 52 exits) are absorbed as flat-book no-ops under the record rule — disclosed, not repaired. First record-rule entry observed at bar 203 — outside the floor, so the floor preserves rather than suppresses the observed behaviour. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT spot, unleveraged (researcher choice — the file names no market; no source-market equivalence is claimed).
- Pinned-engine path with distribution-to-source binding (verified this cycle against immutable artifacts, not assumed): Hummingbot package `20260920` — wheel `hummingbot-20260920-cp312-cp312-macosx_11_0_arm64.whl` (SHA-256 `ea5a929c52095bc03fd34f5b3fb2fbfef068f7ea880af6c38290d1ddb729a148`; METADATA `Name: hummingbot / Version: 20260920`; wheel `hummingbot/VERSION` content `dev-2.17.0` plus trailing newline, byte-identical to the commit file below) — VERSION `dev-2.17.0`, engine source commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3` (`HCH725/hummingbot`; verified ancestor of that repository's local HEAD `2dbc844` this cycle). Whole-tree equivalence: all 902 `hummingbot/**/*.py` files inside the wheel are SHA-256 byte-identical to the same paths at the engine commit (902/902, zero missing, zero different — verified this cycle by hashing every wheel member against `git show <commit>:<path>`); the capability-critical files hash:

| file | SHA-256 (wheel == commit) |
|---|---|
| `strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` | MARKET-first-candle comment present (`# Market orders fill immediately at first candle`, `entry_price = close` at that row) |
| `strategy_v2/backtesting/backtesting_engine_base.py` | `DEFAULT_TERMINATED_EXECUTORS_WINDOW: float = 60 * 60` literal present |
| `data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py` | REST parse uses `row[0]` open-time and retains `row[5]` base volume; websocket maps `data["k"]["v"]` to `volume` |
| `data_feed/candles_feed/binance_spot_candles/constants.py` | `"1h": "1h"` member of the pinned `INTERVALS` map |

Label fence (pre-declared so no repair is ever needed): the commit's `setup.py` static string `version = "20260729"` is a source-tree label, not the distributed build's version — binding here rests on content hashes of the shipped code, never on the label. Specified path: spot connector `binance` + `BinanceSpotCandles` feed (`interval` passed straight to the venue) + `OrderExecutor` MARKET + controller-memory flat/long book. MARKET executors fill at the creation row's timestamp and close — the decision bar's own close at its effective close time, causally available. No maker-touch, queue, or intrabar-path-dependent fill. The bar-close risk legs (stop/ROI-ladder/trailing) are controller-evaluated predicates over completed closes on this same path — they require no stop-order, limit-order, or intrabar primitive; the pinned `position_executor_simulator.py`/`TripleBarrierConfig` barrier vocabulary (`CloseType.STOP_LOSS/TAKE_PROFIT/TRAILING_STOP/TIME_LIMIT`) is cited as existence evidence that barrier-style closes are inside the pinned engine's modeled semantics, never as the evaluation path this record rides.
- Controller state machine (derived, fully specified — no engine default is relied on for decisions): the controller keeps its own fill ledger with states flat/long(Q). On row `t` (at/after the 199-bar floor) it evaluates the source predicates over completed bars `≤ t`; flat+entry-signal creates one MARKET BUY for `Q = 0.001` BTC and records long(Q); long+any-firing-barrier in precedence `exit_sig > stop > roi > trail` creates one MARKET SELL for `Q` and records flat; long+entry is a hold-no-op; flat+any-leg is a no-op; entry/exit-signal co-print holds prior state. Exit sizing comes from the controller's own ledger, never from engine timing. A strategy-specific controller artifact itself is downstream `IMPLEMENTATION_NEEDED` work, never an admission leg; what is demonstrated here is that every required primitive exists on the cited path. No new execution primitive is introduced beyond bar-close predicate evaluation over the sibling-validated MARKET path — the once-per-new-requirement validation the contract calls for is the code-evidence + rule-level assert battery re-checked below.
- Sizing/capital/costs (pinned research cost model — defined here, never punted downstream): fee `0.001`/side passed as the engine `trade_cost` and accumulated per fill as `cum_fees_quote`; slippage `0.0` pinned (fills land exactly on the engine close); funding not applicable (spot has no funding leg; the file reads no funding — census zero); precision: the cited path applies no quantity or price rounding and the configured quantity is `Q = 0.001` BTC. Binary floating-point rounding and tiny residual base balances after netting are possible and not claimed away; controller-memory flat/long state, not any engine hold flag, governs decisions. Trade economics identity: `net = Σ realized_gross − Σ cum_fees_quote`. Explicitly fenced: engine summary labels (`net_pnl_quote`, `update_state total_pnl`) are never used here as fee-inclusive equity; economics come only from the stated identity. No hypothetical zero funding is reported as realized funding — there is no funding on spot to report.
- Leverage/margin/liquidation: none exists on the specified path — spot, unleveraged, no margin account, no liquidation branch, no forced-close state.
- Concurrency: at most one position at any time; single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (156 lines: the triple-buy/triple-sell docstring, the six `(multiplier, period)` pairs across `buy_params`/`sell_params`, the `volume > 0` conjunctions on both legs, the `minimal_roi` ladder, the `-0.265` stop, the four trailing literals, the `1h` frame, the 199-bar startup floor, the `fillna('')` warmup guard, and the `Supertrend(IStrategy)` class pin) plus the file's own not-validated caveat. It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Representative rule-level validation executed this cycle (2026-10-25, `qlib-tests` venv with pandas 3.0.6 / numpy 2.5.4): the REAL six-leg rule with the REAL vendored construction (TRANGE true range, SMA-ATR, hl2 bands, prior-bar ratchet, st state machine, `None→''` warmup — transcribed line-for-line from pinned blob `eba46c8b…dd48332d146`) running the REAL entry/exit conjunctions with the REAL risk literals — source-identity asserts plus rule-causality asserts plus engine-binding asserts re-checked at the pinned commits this cycle, all passing:

- Source identity (6 asserts): strategy blob `757b1521`, 6448 bytes, 156 lines, `git hash-object` reproduces the Contents-API SHA, commit equals repository HEAD via `git ls-remote`; technical blob `eba46c8b`, 1873 bytes, `git hash-object` match at commit `5852e54`.
- R1 params pin (3 asserts): buy pairs `(4,8)/(7,9)/(1,8)` and sell pairs `(1,16)/(3,18)/(6,18)` load from `buy_params`/`sell_params`; `timeframe '1h'`; `startup_candle_count 199`.
- R2–R9 rule causality (10 asserts): 199-bar floor holds (raw pre-floor prints 24 entries/52 exits fenced as flat-book no-ops); entries and exits both exist on a 1200-bar synthetic 1h tape (pinned seed 7: 436 entries, 226 exits, 0 co-print bars); deterministic prefix re-evaluation agreement; first record-rule entry at bar 203 (outside the floor); long-only (zero short tokens file-wide); volume gate vetoes zero-volume bars (bars 100/500/501 probes); ROI rung boundaries literal (`>= 0/372/861/2221` min → `0.087/0.058/0.029/0.0`); entry-bar self-exit impossible on every leg.
- Book behaviour (same tape, derived machine): 23 closed trades across `roi` + `signal` kinds — barriers and signal both end positions in practice.
- Barrier micro-scenarios (4 asserts): forced-entry crash exits on the 5%-of-peak trailing floor with the `-0.265` literal wired as the `max()` anchor (trailing-shadows-stop, source-consistent); forced-entry rally exits on the ROI rung; spike-then-fade exits `trail` on the exact bar the floor breaks; exit-signal wins precedence over silent barriers on a shared bar.
- V3 code-evidence asserts (re-checked at the pinned engine commit this cycle): `DEFAULT_TERMINATED_EXECUTORS_WINDOW: float = 60 * 60` literal present; MARKET-first-candle comment present; `INTERVALS` contains `1h`; REST parse uses `row[0]` open-time and retains `row[5]` volume; barrier vocabulary (`CloseType.TAKE_PROFIT/STOP_LOSS/TRAILING_STOP/TIME_LIMIT`, `TripleBarrierConfig`) present as existence evidence. Not a performance backtest, not a deployment — a primitive capability check reusing the sibling-validated MARKET path, exactly the once-per-new-requirement validation the contract calls for.
- V4 distribution binding: 902/902 wheel `hummingbot/**/*.py` members SHA-256-identical to the engine commit, zero missing, zero different; METADATA `Version: 20260920`; wheel `hummingbot/VERSION` == `dev-2.17.0` plus newline; engine commit verified ancestor of local HEAD `2dbc844`.

### Negative evidence

1. Leading-window behaviour fenced: the SMA-ATR seeds over the first `period` bars while `st == 0` yields `None` → `''`, matching neither leg; the file's own 199-bar startup floor plus the record rule hold all early bars flat — disclosed, not repaired.
2. Exact-match rule fenced: legs compare string equality (`== 'up'` / `== 'down'` — the `''` warmup value never matches); the volume gate is strict (`> 0`); stop/ROI/trailing use `<=` / `>=` / `<` exactly as coded. Nothing is smoothed or re-thresholded.
3. Unison-vs-edge scope fenced: entry demands all three buy legs `'up'` on the same bar (a two-of-three alignment prints nothing and is never latched); exit demands all three sell legs `'down'`. The six legs are two different parameter sets — the exit is never the entry's negation, and weakening either side to a majority or a single leg would be a different, unpinned rule with different trade events.
4. Stop-shadow fenced: with `trailing_only_offset_is_reached = False` the 5%-distance trailing floor is armed from the entry bar, so the effective immediate floor is `peak − 5%` and the verbatim `-0.265` stop literal survives only as the `max()` anchor — unreachable while trailing is on. The `0.144` offset participates in zero comparisons. Both facts are disclosed readings of the file's own literals, never repaired into a tighter stop or a live offset.
5. Diagnostic quarantine fenced: `INTERFACE_VERSION`, the hyperopt-generation comment, the 630-combination `IntParameter` scaffold, the dead `talib.abstract` import, and the `(value, direction)` tuple's discarded value leg are read by zero order-gating comparisons; `parameter` defaults inside `IntParameter(...)` never override the loaded `buy_params`/`sell_params`.
6. Pool Supertrend siblings fenced (three axes: source file, trigger, gates): `alorse-supertrend-rsi50-cross-rsi72-exit-long` trades a single Pine Supertrend band with an RSI-50 cross entry and RSI-72 exit; `alorse-stochrsi-supertrend-ema200-long` trades a single Pine band with StochRSI/EMA200 gates. This record trades six Python-side bands in two asymmetric triples with a volume gate and a stop/ROI-ladder/trailing stack — different source files, different trigger multiplicity, different exit form. The shared `Supertrend` name is an indicator label, not a shared signal.
7. Open SuperTrend PR fenced: open `research/*` PR #63 (SuperTrend ATR-flip, TradingView Pine single-band flip-flop on BTCUSDT `1d`) triggers on one band's direction flip with no second triple, no volume gate, no barrier stack, and a different frame — different trigger × different gate set × different source file × different frame.
8. Pool trailing-stack cousins fenced: `freqtrade-hlhb-ema-rsi-adx-quad-gated`, `freqtrade-multima-tema-stack-trend`, `freqtrade-strategy005-volume-surge-fisher-washout`, `freqtrade-universalmacd-ema-ratio-dip-band`, `td-sequential-setup9-perfected` each carry trailing/stop vocabulary but trigger on EMA/RSI/ADX/TEMA/Fisher/TD-sequential constructions — none computes a triple-Supertrend unison. The shared risk vocabulary is framework furniture, not a shared signal.
9. Engine-label fences (answers to known review findings, pre-declared so no repair is ever needed): fee-inclusive cash is never claimed from `net_pnl_quote`; closed-trade equity is never claimed from `update_state total_pnl`; availability is never claimed from open-time labels without the `+3600s` mapping; fills are never claimed intrabar (risk legs are bar-close predicates by researcher pin); the 3600s terminated view is never relied on for position state; package-to-commit binding rests on the V4 content hashes above, never on the `setup.py` version label; no hypothetical zero funding is reported as realized funding.
10. Derivation boundary fenced: the only non-source-native behaviours are the BTCUSDT-spot-`1h` market pin (frame is source-native), the effective-time MARKET-close fills, the single-unit/controller-memory/co-print/precedence pin, the bar-close risk evaluation, and the `+3600s`/gap data rule — all predeclared above. The six `(multiplier, period)` pairs, the unison conjunctions, the volume gates, the ROI ladder, the stop literal, the trailing distance, the 199-bar floor, the long-only stance, and the not-validated caveat are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: triple-unison construction / six pinned pairs / volume gate / slow-triple exit / stop-ROI-trailing stack with coded precedence / single-unit `0.001` BTC / `1h` BTCUSDT spot / effective-time close fills are frozen.

- F1 — Unison relevance: collapsing either triple to its single fastest leg (same risk stack, same posture) must not improve net expectancy; fail ⇒ the unison adds nothing over a lone band and the record is a single-band variant of one.
- F2 — Exit-leg relevance: replacing the slow-triple signal exit with barrier-only exits (same entries, same risk stack) must not improve net expectancy; fail ⇒ the asymmetric sell triple is dead code wearing a signal-leg label.
- F3 — Trailing relevance: removing the trailing floor (stop + ROI ladder only, same entries/exits) must not improve net expectancy; fail ⇒ the trailing leg adds nothing over the static stop/ROI pair.

## Crypto portability

BTCUSDT spot `1h` is the research pin (the file names no market; the `1h` frame is source-native). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting and no leverage. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count, a rolling mean span, or a minute-duration clock on the decision frame, portable across 24/7 crypto tape. Spot has no funding leg, so the funding portability question does not arise; fees/slippage ride the pinned research model, never a venue schedule claim.

## Limitations

- Barrier-dominant exits by construction: most positions end on ROI or trailing, not on the slow-triple signal — the signal exit is the minority closer (verified minority on the synthetic tape), disclosed.
- Stop literal shadowed: the −26.5% stop cannot fire while 5%-distance trailing is armed from entry; the worst bar-close drawdown exit is ≈ −5% from peak, disclosed.
- Completed-bar risk latency: a bar that gaps through multiple barrier levels exits once, at that bar's effective close, on the precedence winner — there is no intrabar stop order to front-run the close, disclosed.
- Volume-gate veto: a perfect unison alignment on a zero-volume bar prints nothing and is never revisited — the gate is a veto, not a deferral, disclosed.
- Slow-exit profile: a reversal that never aligns all three slow legs `'down'` is ridden until a barrier fires; chop around a single slow leg flips nothing — the exit is a conjunction, not a hair-trigger, disclosed.
- Single-market scope: derived pin is BTCUSDT spot `1h` only; portability to other symbols/timeframes is untested and claimed nowhere.
- Research overlay dependence: fills, sizing, precedence, bar-close risk evaluation, and costs follow the derived pins and the stated economics identity — not the Freqtrade engine's own intrabar semantics, and not the engine summary labels fenced above.
- No breakeven move, no second stop, no cooldown — all explicitly absent, never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/Supertrend.py
- https://github.com/freqtrade/freqtrade-strategies
- https://github.com/freqtrade/technical/blob/5852e5407588ad04d539f5d5071c60d9dc69b95a/technical/indicators/supertrend.py
- https://github.com/freqtrade/technical
