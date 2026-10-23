---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade HourBasedStrategy UTC hour-window state long-flat on BTCUSDT 1h bars
created: 2026-10-23
updated: 2026-10-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/HourBasedStrategy.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade HourBasedStrategy UTC hour-window state long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the same lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, `freqtrade-asdts-rockwell`, `freqtrade-macd-cci-dip-state`, `freqtrade-binhv27`, `freqtrade-macd-cross-cci-edge`, and `freqtrade-technical-cmf-sign-state` records — this is only its twelfth record, and the first pinned to this exact file).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/HourBasedStrategy.py`.
- GitHub blob SHA at the pinned commit: `8f0abc74262da360b2cfb8ac853cc83e8376a612`, size 4270 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 4270 bytes, 104 lines, SHA-256 `61755d49c46b3037c102f60de30841910472b6da06e9b578882b3dfc125b9ccc`, identical to the GitHub blob (`git hash-object` reproduces `8f0abc74…e8376a612`) — the entire file was retrieved and inspected.
- Registration: the file defines class `HourBasedStrategy(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `berlinguyinca/AverageStrategy.py` (EMA8/21 cross edges, `4h`), `berlinguyinca/BinHV45.py` (BB-penetration dip, `1m`), `PowerTower.py` (close-power tower, `5m`), `PatternRecognition.py` (TA-Lib pattern menu, `1d`), and every other admitted pin are different pins with different gates — this record pins ONLY the HourBasedStrategy file's literals below, and no reviewer repair may substitute a sibling constant or a commented archaeology number.
- The file's own words (quoted for gate evidence, never extended): header `In this strategy we try to find the best hours to buy and sell in a day.(in hourly timeframe)` and `you should just use 1h timeframe on this strategy`; `timeframe = '1h'`; `minimal_roi = { "0": 0.528, "169": 0.113, "528": 0.089, "1837": 0 }` (ladder keys are position-age minutes); `stoploss = -0.10`; frozen hyperspace literals `buy_params = { "buy_hour_max": 24, "buy_hour_min": 4 }` and `sell_params = { "sell_hour_max": 21, "sell_hour_min": 22 }` (printed under the file's own `Buy hyperspace params:` / `Sell hyperspace params:` comments); indicator `dataframe['hour'] = dataframe['date'].dt.hour` (the single indicator line — a pure timestamp projection, no price read); entry `(dataframe['hour'].between(self.buy_hour_min.value, self.buy_hour_max.value))` (`enter_long = 1`); exit `(dataframe['hour'].between(self.sell_hour_min.value, self.sell_hour_max.value))` (`exit_long = 1`). No `trailing`, no `startup_candle_count`, no `use_exit_signal` / `exit_profit_only` override, no `can_short`, no `process_only_new_candles`, no order-type mapping ships anywhere — the framework defaults below are disclosed as defaults, never as file literals.
- Out-of-file calls pinned (none — resolved by absence): zero indicator-library calls execute anywhere in the gating path. The `talib` / `qtpylib` / `numpy` import lines are commented out (`# import talib.abstract as ta`, `# import freqtrade.vendor.qtpylib.indicators as qtpylib`, `# No need to These imports. just for who want to add more conditions`) — display leftovers with no gate effect. The four `IntParameter(0, 24, ...)` declarations (`buy_hour_min` default 1, `buy_hour_max` default 0, `sell_hour_min` default 1, `sell_hour_max` default 0, spaces `buy`/`buy`/`sell`/`sell`) are frozen by the shipped `buy_params`/`sell_params` literals under the file's hyperopt contract — exactly the freeze pattern the admitted Strategy005 record pins for its eight literals; the low/high ranges, `optimize` spaces, and defaults never execute under this freeze (see Negative evidence 4). No DB, no network, no `request.*`, no `security()`, no resample/interpolate, no informative-pair call in the file.
- Full-file token census (verified over the 104 lines this cycle): 0 `short` (case-insensitive — no short leg, no short identifier anywhere); 0 `volume` (no volume token in the file body — the rule never reads volume); 0 `shift` (no lag call anywhere — the rule reads the decision bar's own hour print, a persistent state, never an edge); 0 `open` (no open-column read — the signal path reads the bar timestamp only); 0 `crossed` (no edge call — both legs are persistent states); 0 `ta.` / 0 `qtpylib` live calls (commented imports only); 1 live `stoploss` (`-0.10`) and 1 live `minimal_roi` (the four-rung ladder) as the only risk legs, plus 4 commented archaeology copies each (fenced below); 0 shipped `trailing`; 0 `startup_candle_count` (the record's 30-bar floor is a predeclared researcher pin, never a file semantic); 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop); 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic); 0 `resample` / 0 `informative` / 0 `request` / 0 `security`; 0 `fillna` / 0 `ffill` / 0 `interpolate` (no NaN patching — and no NaN path exists, see Signal).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Freqtrade deployment. The source pins the `1h` frame, the UTC hour projection, the frozen 4–24 entry window, the frozen 22–21 (empty) exit band, the four-rung ROI ladder, the −10% stop, and the long-only stance — but ships no venue spelling, no fill-timing flag, no warmup guard, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market `BTCUSDT` (the file names no market; the SHIB/SAND/KDA venue names in commented hyperopt archaeology are never market pins, and no source-market equivalence is claimed); (2) completed-bar decisions with same-bar-close market fills (the file's own framework contract evaluates per completed bar — derivation disclosed, never presented as the source engine's own timing); (3) single-unit position pin with hold-no-op semantics plus a 30-bar researcher warmup pin (the file carries no position reference and no length guard — disclosed, never presented as source-native behaviour); (4) the source's absent sizing/costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with no safety-order/add tranche activating under the single-unit/no-add pin (see Execution assumptions). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-23): working-tree filename/content search for `hourbased`, `buy_hour`, and `hour-of-day` returns zero strategy records — no record in the pool cites this source file. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian band-ratio) trades an hour-window rule. Calendar cousins in the pool are fenced as different constructions in Negative evidence 7. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: hold long exposure through the hours of the day when the completed `1h` bar's hour print falls inside the frozen 4–24 window (hours 4 through 23 UTC — twenty of every twenty-four bars), stand flat through hours 0–3, exit through a decaying four-rung ROI ladder (52.8% inside the opening minutes, 11.3% after 169 min, 8.9% after 528 min, breakeven after 1837 min) behind a fixed −10% stoploss, with the coded signal-exit leg printing nothing under the frozen empty band. The commented hyperopt backtest tallies (SHIB/SAND/KDA trade counts, win rates, profit totals) are archaeology prose — this record adopts no source-reported performance (see Evidence).

### Research interpretation

UTC-daytime seasonality harvester, long-only, price-blind. The rule reads no price and no volume — it is a pure calendar-state machine that is long the tape for twenty hours of each UTC day and flat for the three early-UTC hours (00:00–03:59, the quiet Asian-early session on Binance's UTC clock). The ROI ladder is patient by construction: the opening 52.8% rung is nearly unreachable in ordinary tape, so early exits are the −10% stop in practice; the ladder only starts harvesting realistic moves after ~3 h (11.3%) and bleeds to a breakeven-any-profit exit after ~30.6 h — a position that survives a full day is closed for anything above flat. The failure mode is plain: a tape that drifts sideways inside the window holds the unit for a day-plus graze exit while paying the spread on every re-entry (no cooldown — any post-exit in-window bar re-arms immediately), and a sharp adverse move inside the window rides the full −10% stop with no trailing or breakeven defence. There is no chop filter, no volatility read, and no weekend/holiday awareness — disclosed, not repaired.

## Signal

Exact rule as pinned (any other window edge, exit band, risk rung, fill, frame, or book is a different, unpinned rule). The hour bounds are frozen file literals (`buy_params`/`sell_params`), never tuned here:

```text
hour[t]   = UTC hour of the completed 1h bar's own open timestamp (0..23, total function)
entry     = hour[t] in [4, 24]   // between() inclusive both ends: fires exactly 4..23
exit_sig  = hour[t] in [22, 21]  // inverted band: fires NEVER (proven all-False, see below)
risk      = ROI {"0": 0.528, "169": 0.113, "528": 0.089, "1837": 0} (fraction of entry-price distance, by position age in minutes);
            fixed stop at -10% (stoploss -0.10, same basis)
floor     = no NaN path exists (hour prints on bar 1; see Required data)
```

- Trade events: `enter_long=1` on every bar printing an in-window hour, `direction` long-only; `exit_long=1` never prints under the frozen band. Each print is a persistent state, not a one-bar edge — a book already positioned treats further in-window bars as hold-no-ops under the position pin below, and a flat book treats out-of-window bars as no-ops.
- Exact boundaries (pinned semantics, empirically verified this cycle with a minimal assert over hours 0..23): `between(4, 24)` is inclusive — hours 4 and 23 fire, hours 0–3 do not (20 firing bars per UTC day, no smoothing); `between(22, 21)` with an inverted band prints all-False on every hour — the signal-exit leg is deterministically dead code under the freeze, so all signal exits are absent and only the ROI ladder plus the stop can close a position (coded framework behaviour, disclosed, never repaired into a signal).
- Mutual-exclusion proof (no tie-break pin required): the exit leg never prints, so entry and signal-exit never co-print on any bar. ROI/stop cannot co-fire with entry on the entry bar either (zero distance at the fill). Under the single-unit position pin, a flat book treats any in-window bar as entry (risk legs are no-ops without a position — no same-bar round-trip), while a positioned book treats an in-window bar co-printing an ROI/stop leg as exit-close (the entry print is a hold-no-op while positioned). The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero short-leg tokens ship anywhere, and the framework default `can_short = False` applies (disclosed default, never a file literal) — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the four-rung decaying ROI ladder and the −10% stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — moot while the signal leg never prints; disclosed defaults, never file literals). ROI rungs and stop are fractions of entry-price distance, evaluated at bar closes — this basis is leverage-invariant, so downstream leverage/margin accounting cannot alter any exit event. No trailing, no time exit beyond the ladder's breakeven rung, no breakeven move — explicitly none further, not invented. No exit leg reads net profit, fees, or funding — fees change only the performance report, never whether an exit fires (disclosed).
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further in-window bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats out-of-window bars and risk legs as no-ops; re-entry re-arms on any qualifying in-window bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only the completed bar's own timestamp (a total, immutable projection — `dt.hour` of the bar open print) under the file's own framework contract (per-completed-bar evaluation — disclosed default, never a file literal); no forming values are ever read. No price, volume, funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `1h` bars of BTCUSDT: the bar timestamp only (the hour projection reads `date`, never `open`/`high`/`low`/`close`/`volume`). No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar-table, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1h` (source-native — the file prints `timeframe = '1h'` and its header restricts to the hourly frame). One evaluation per completed bar; fills land on the decision bar's own close under the derived rule below. The hour is the data feed's UTC hour of the bar's open timestamp (Binance klines are UTC) — the same timestamps the pinned backtester walks, so no separate clock or timezone conversion exists in the path.
- Warmup (researcher pin, disclosed): 30 one-hour bars held flat. Covers one full 24-hour rotation plus margin so the first signal is observed mid-cycle. The file ships no `startup_candle_count` — quoted absence, never filled in from elsewhere. Coded behaviour underneath needs no seed (the hour projection prints on bar 1 — there is no rolling window to seed and no NaN path). No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced Strategy005, TechnicalExample-CMF, and BinHV27 siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry prints and the ROI/stop legs are all bar-close-evaluated; the Signal mutual-exclusion proof (exit leg never prints) leaves no ambiguous same-bar signal fill order, and any bar co-printing an in-window entry with an ROI/stop leg resolves by the position pin (flat → enter, positioned → exit-close), so no intrabar ordering assumption is needed.
- Interval precedent (disclosed, not assumed): `1h` is an already-admitted interval on `main` via the Forven `1h` family (including the PPO-zero-gated-cross and Heikin-Ashi records) and 83 `1h` pool records — no novel-interval confirmation is required for this frame. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI ladder and stop percentages are preserved verbatim as the risk legs (fractions of entry-price distance, leverage-invariant events) while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal — no safety-order/add tranche activates in this derived version, so position events are fully determined by the legs above and sizing changes no event, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the in-window hour state opens the full unit on a flat book; the ROI ladder or the stop closes it in full; re-entry after an exit needs only the next in-window bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (104 lines: the single `dt.hour` projection, the two frozen `between` legs, the `timeframe`/`minimal_roi`/`stoploss`/`buy_params`/`sell_params` literals, and the `HourBasedStrategy(IStrategy)` class pin). It ships no adopted sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: the hour projection is total — `date` prints on every completed bar and `dt.hour` has no NaN path, so the first bar already carries a valid state. The 30-bar record-rule floor additionally holds every pre-rotation bar flat — disclosed, not repaired. The file ships no `startup_candle_count`, so the floor is purely a researcher pin, never misattributed.
2. Exact-touch rule fenced: `between` is inclusive on both ends — hours exactly on 4 and 23 fire, hours exactly on 0–3 hold flat (asserted over all 24 hours this cycle). Strictness-or-inclusivity preserved throughout — disclosed, not smoothed.
3. Dead-exit-band fence: `between(22, 21)` prints all-False on every hour (asserted: zero prints across 0..23 this cycle) — the signal-exit leg is deterministically dead under the shipped freeze, so exits are ROI-ladder-plus-stop only. Coded framework behaviour, disclosed, not repaired into a signal and never supplemented with an invented exit.
4. Hyperopt freeze fenced: the four `IntParameter` declarations plus the `buy_params`/`sell_params` freeze resolve to the four frozen literals `4/24` buy and `22/21` sell — the low/high ranges, `optimize` spaces, and `default=1/0/1/0` never govern under the freeze (the default-fallback reading, under which the entry band itself would be empty and the rule would never trade, is fenced as an unpinned variant — disclosed, not repaired). Adopting any other point of the declared 0–24 spaces would be a different, unpinned rule. This is the same freeze pattern the admitted Strategy005 record pins for its eight literals.
5. Archaeology fence: the four commented hyperopt-result blocks (SHIB/SAND/KDA/multi-venue tallies with their own buy/sell/ROI/stop numbers) and their venue names are prose leftovers — the coded legs govern; no venue there is a market pin, no tally there is a performance claim, and no reviewer repair may promote any commented number into the rule.
6. Dead-import fence: the commented `talib` / `qtpylib` / `numpy` lines (`just for who want to add more conditions`) execute nothing — the gating path performs zero price/volume reads and zero library calls. Converting the rule into an indicator-gated system would be a different, unpinned rule.
7. Cousin records fenced as different constructions (none trades UTC hour-window persistent states with a decaying ROI ladder on `1h`): the admitted `bitcoin-intraday-first-last-halfhour` pool-mate times momentum legs on `30m` first/last half-hours (momentum-gated timing, different frame, different legs — a market drifting flat all day fires entries here but nothing there); the admitted `monday-drift-weekly` pool-mate holds a weekday calendar drift (weekly hold, no intraday windows, no ROI ladder); the admitted `turn-of-month` / `santa-claus-rally` / `pre-holiday-drift` pool-mates hold multi-day scheduled drifts (different horizons, no hour states); the admitted `moreira-muir-volatility-managed` pool-mate scales by volatility (no calendar read at all). Not a window re-tuning of any of them: moving either window edge, enabling the exit band, or changing any ROI rung, the stop, or the frame would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `AverageStrategy.py`, `BinHV45.py`, `PowerTower.py`, `PatternRecognition.py`, `Strategy001.py`–`Strategy005.py`, `Supertrend.py`, `UniversalMACD.py`, `MultiMa.py`, `Diamond.py`, `Bandtastic.py`, and every other file in the collection are separate pins — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT market choice, the same-bar-close fills, the single-unit/no-add/no-cooldown position pin, the 30-bar warmup floor (the file ships none), the framework-default readings (`can_short=False`, `use_exit_signal=True`, `exit_profit_only=False`, per-completed-bar evaluation), and house sizing/costs with safety tranches deactivated — all predeclared above. The `1h` frame, the hour projection, the frozen 4–24 entry window with its verified inclusivity, the frozen empty exit band, the four-rung ROI ladder, the −10% stop, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: hour projection / frozen 4–24 window with verified inclusivity / frozen empty exit band / four-rung ROI ladder / −10% stop / single-unit long-only / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Window relevance: entering on every post-warmup bar (hour gate removed, same ladder/stop) must not improve net expectancy; fail ⇒ the hour window adds nothing over blind exposure.
- F2 — Ladder relevance: removing the ROI ladder (stop-only exits, same entry) must not improve net expectancy; fail ⇒ the decaying ladder adds nothing over the bare stop.
- F3 — Stop relevance: removing the −10% stop (ladder-only exits, same entry) must not improve net expectancy; fail ⇒ the stop backstop adds nothing over the bare ladder.

## Crypto portability

BTCUSDT Binance perpetual `1h` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, holiday, or equity-hours concept is read anywhere — the only clock is the data feed's UTC bar hour, portable across 24/7 crypto tape on any venue printing UTC bar timestamps (a non-UTC venue clock would shift the windows — disclosed, not repaired). No price or volume field is read, so tick-size/spot-vs-perp quote differences cannot alter any signal event. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- The `1h` frame rides existing admission precedent (the Forven `1h` family and 83 `1h` pool records) — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- A position opened late in the window is held through the flat 0–3 UTC hours with no signal exit available (the exit leg never prints) — only the ladder or the stop can release it; a market whose dislocation arrives during flat hours is missed outright. There is no decay, chop, trend-loss, or further time exit beyond the ladder's breakeven rung — disclosed, not repaired.
- Re-entry after any exit needs only the next in-window bar (no cooldown) — whipsaw round trips inside the window are the principal friction, disclosed as the main cost of the persistent-state construction.
- The hour is the venue clock's bar-hour print — pinned here to Binance UTC klines; exact reproduction inherits that clock alongside the 30-bar floor.
- Hyperopt scaffolding is frozen, not searched: the `IntParameter` ranges never execute under this record; only the four `buy_params`/`sell_params` literals govern. Any re-optimization would be a different, unpinned rule.
- No trailing, no breakeven, no short leg, no cooldown — all explicitly absent, never to be added by repair. The opening 52.8% rung is nearly unreachable in ordinary tape, so the −10% stop is the binding early risk leg — disclosed as the record's principal risk.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/HourBasedStrategy.py
- https://github.com/freqtrade/freqtrade-strategies
