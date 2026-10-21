---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade SwingHighToSky CCI-RSI dual-threshold long-flat on BTCUSDT 15m bars
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
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/SwingHighToSky.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade SwingHighToSky CCI-RSI dual-threshold long-flat on BTCUSDT 15m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (official open-source Freqtrade strategy collection; the lane that already supplied the admitted `freqtrade-multima`, `freqtrade-hlhb`, `freqtrade-simple-macd-bb-rsi`, `freqtrade-cofibit`, `freqtrade-strategy005`, and `freqtrade-universalmacd` records at this same pin — this record pins ONLY the SwingHighToSky literals below, and no reviewer repair may substitute a sibling constant).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` twice during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/SwingHighToSky.py`.
- GitHub blob SHA at the pinned commit: `4289cde249a7065a83401e85cf0cf37a5f6b0627`, size 3267 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 3267 bytes, 110 lines, SHA-256 `3778a09f02b88c1ca257e5346d6cc97ae8b7dd80a7559d003ab3a760ab1e5518`, identical to the GitHub blob (`git hash-object` reproduces `4289cde2…b0627`) — the entire file was retrieved and inspected.
- Registration: the file defines class `SwingHighToSky(IStrategy)` (the only class in the file), `INTERFACE_VERSION = 3`, framework column contract `populate_entry_trend` / `populate_exit_trend` (`enter_long` / `exit_long`, never the old `buy`/`sell` plumbing). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path plus pin, all unique. Every other `user_data/strategies/*.py` sibling is a different pin with different constants.
- The file's own words (quoted for gate evidence, never extended): `timeframe = '15m'`; `minimal_roi = { "0": 0.27058, "33": 0.0853, "64": 0.04093, "244": 0 }`; `stoploss = -0.34338`; module constants `cciBuyTP = 72`, `cciBuyVal = -175`, `cciSellTP = 66`, `cciSellVal = -106`, `rsiBuyTP = 36`, `rsiBuyVal = 90`, `rsiSellTP = 45`, `rsiSellVal = 88`; frozen hyperspace literals `buy_params = { "buy_cci": -175, "buy_cciTime": 72, "buy_rsi": 90, "buy_rsiTime": 36 }` and `sell_params = { "sell_cci": -106, "sell_cciTime": 66, "sell_rsi": 88, "sell_rsiTime": 45 }`; entry `(dataframe[f'cci-{self.buy_cciTime.value}'] < self.buy_cci.value) & (dataframe[f'rsi-{self.buy_rsiTime.value}'] < self.buy_rsi.value)` (`enter_long = 1`); exit `(dataframe[f'cci-sell-{self.sell_cciTime.value}'] > self.sell_cci.value) & (dataframe[f'rsi-sell-{self.sell_rsiTime.value}'] > self.sell_rsi.value)` (`exit_long = 1`); `informative_pairs()` returns `[]`. No `trailing`, no `startup_candle_count`, no `can_short`, no `use_exit_signal` / `exit_profit_only` override, no `order_types` mapping ships anywhere — the framework defaults below are disclosed as derived behaviour, never as file literals. The header docstring (author Kevin Ossenbrück, MIT, credits Bloom Trading / Mohsen Hassan) is lineage only — no performance, sample, window, trade count, or cost basis ships anywhere in the 110 lines.
- Out-of-file calls pinned (all resolved by name, all standard defaults): `ta.CCI(dataframe, timeperiod=…)` (TA-Lib Commodity Channel Index over `high`/`low`/`close` — no other argument, disclosed); `ta.RSI(dataframe, timeperiod=…)` (TA-Lib RSI over the default `close` input — no other argument, disclosed). No DB, no network, no `request.*`, no `security()`, no resample/interpolate, no `fillna`/`ffill` in the file.
- Full-file token census (verified over the 110 lines this cycle): 0 `short` (case-insensitive — no short leg, no short identifier anywhere); 0 `volume` (no volume read of any kind — both oscillators read price only); 0 `shift` (no bar offset anywhere — both legs read the decision bar only); 0 `cross` (no `crossed_above`/`crossed_below` edge anywhere — both legs are persistent level states, never one-bar edges); 0 `trailing` / 0 `startup_candle_count` / 0 `can_short` / 0 `use_exit_signal` / 0 `exit_profit_only` / 0 `process_only_new_candles` / 0 `order_types` / 0 `order_time_in_force` / 0 `leverage` / 0 `funding` / 0 `mark_price` (all such execution/position/economic semantics are predeclared researcher pins below, never file semantics); 0 `position_adjustment` / 0 `max_open_trades` / 0 `cooldown` (the position pin below is a predeclared researcher rule, never a file semantic); 1 `informative` (the `def informative_pairs(self): return []` empty-list literal — no second pair, no second timeframe, single-frame by construction); 0 `resample` / 0 `merge_informative` / 0 `fillna` / 0 `ffill` / 0 `interpolate` / 0 `dropna` (no NaN patching anywhere — strict NaN comparisons simply stay false); 0 `pyramid` / 0 `position_size` reads / 0 `syminfo` (the file names no market); 0 `hyperopt` / 0 `DecimalParameter` / 0 `CategoricalParameter` / 0 `BooleanParameter` / 0 `print(` (no tuning scaffolding beyond the eight `IntParameter` declarations); 9 `IntParameter` tokens (the eight live threshold/lookback declarations plus the import — the low/high ranges and `optimize=True` spaces are fenced out, the frozen `buy_params`/`sell_params` literals are the rule, see Signal); 4 `.range` (the four precompute loops over the declared `10..80` spaces — deterministic column plumbing, never signal); `reduce`/`numpy`/`qtpylib` imported and never called in the gating path (`DataFrame` appears in type hints only) — fenced as dead plumbing.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. The file is causal as written (no full-sample scalar, no repainting primitive, no multi-timeframe merge, no external package — no repair site exists). Researcher-declared adaptations are exactly five: (1) research market `BTCUSDT` (the source names no market); (2) completed-bar decisions with same-bar-close market fills; (3) single-unit/no-add/no-cooldown position pin plus a 100-bar researcher warmup floor (covers the 80-bar precompute span and the 72-bar longest effective seed with margin); (4) framework-default execution semantics pinned as derived behaviour (signal exits enabled as coded, ROI/stop legs bar-close-evaluated — disclosed, never presented as file literals); (5) the house cost/capital overlay replaces the absent source economics. Every period, every threshold, the frozen hyperspace literals, the entry conjunction, the exit conjunction, the ROI ladder, and the stop are untouched.

Pre-write dedup (2026-10-21): working-tree filename/content search for `SwingHighToSky`, `swinghigh`/`swing_high`, `cciBuyTP`, `cciBuyVal`, and `cci-72` returns zero strategy records — the single pool-wide `swing-high` hit is a generic section header inside the unrelated KAMA efficiency-ratio record (chart-pattern prose, never a record of this file). No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas) trades a CCI-RSI dual-threshold system. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims no behavioural channel anywhere in the 110 lines beyond its code: buy the bar where the 72-bar CCI prints under −175 while the 36-bar RSI sits under 90 (deep-oversold CCI washout with a permissive RSI ceiling), and stand aside to flat when the 66-bar CCI recovers above −106 while the 45-bar RSI prints above 88 (a near-overbought RSI reclaim), behind a decaying take-profit ladder (27.058% immediately down to breakeven after 244 minutes) and a −34.338% stop. It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Research interpretation

Deep-washout dip buyer, long-only, exited mostly by time-decayed profit-taking. Unlike MACD-line/signal cross systems that flip on an oscillator edge, the entry demands a severe CCI depression (72-bar CCI under −175 — a far-tail washout, not a mild dip) while the RSI leg (`< 90`) is deliberately permissive, failing only on extreme-overbought bars — so the CCI leg does the selecting and the RSI leg merely vetoes buying into vertical blow-off bars. Unlike stop/trailing exits, the position exits through the four-rung decaying ROI ladder or the wide stop on almost every round-trip: the signal exit needs a 45-bar RSI above 88 (a rare print), so it is a seldom-firing reclaim leg, not the workhorse — disclosed, never repaired into a livelier band. The coded consequence is a buyer of far-tail CCI washouts that rents exposure for at most ~4 hours of decaying upside before breakeven-gating, and that almost never cuts a winner early on a signal.

## Signal

Exact rule as pinned (any other CCI/RSI period, threshold, ROI rung, stop, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own:

```text
cci72[t]  = TA-Lib CCI(high, low, close, timeperiod=72)[t]
rsi36[t]  = TA-Lib RSI(close, timeperiod=36)[t]
cci66[t]  = TA-Lib CCI(high, low, close, timeperiod=66)[t]
rsi45[t]  = TA-Lib RSI(close, timeperiod=45)[t]
entry = (cci72[t] < -175) & (rsi36[t] < 90)    // enter_long = 1 (strict, state print)
exit_sig = (cci66[t] > -106) & (rsi45[t] > 88) // exit_long = 1 (strict, state print)
risk = decaying take-profit minimal_roi {"244":0,"64":0.04093,"33":0.0853,"0":0.27058};
       fixed stop at -34.338% (stoploss -0.34338); no trailing/trailer of any kind
guard = leading-window bars: NaN comparisons false (see Required data)
```

- Hyperspace freeze (pinned file literals, never tuned here): entry reads `buy_cci = -175` / `buy_cciTime = 72` / `buy_rsi = 90` / `buy_rsiTime = 36` exactly as printed in the file's `buy_params` dict (mirrored verbatim by the module constants `cciBuyVal`/`cciBuyTP`/`rsiBuyVal`/`rsiBuyTP`); exit reads `sell_cci = -106` / `sell_cciTime = 66` / `sell_rsi = 88` / `sell_rsiTime = 45` exactly as printed in `sell_params` (mirrored by `cciSellVal`/`cciSellTP`/`rsiSellVal`/`rsiSellTP`). The eight `IntParameter` low/high ranges, `optimize=True` spaces, and `default=100/20/30/26` placeholders are unfrozen search scaffolding — excluded from the rule, following the same freeze convention as the admitted Strategy005 record at this pin. Adopting any other point of the declared spaces would be a different, unpinned rule.
- Trade events: `enter_long=1` on any bar printing the two-conjunct washout state, `direction` long-only; `exit_long=1` on any bar printing the two-conjunct reclaim state. Both legs are STATE prints in construction (each persists while its levels hold — close-and-hold-flat); either leg can reprint across consecutive bars (no one-shot latch in code). New-interface `enter_long`/`exit_long` columns read as enter-long/exit-long directly.
- Exact boundaries (pinned semantics): strict throughout (`<`, `>` exactly as coded — CCI exactly on −175/−106 or RSI exactly on 90/88 fires nothing on that conjunct). The `72` / `36` / `66` / `45` / four threshold literals are never tuned here.
- Permissive/restrictive asymmetry (pinned, disclosed — not a repair site): the entry RSI leg (`rsi36 < 90`) fails only on extreme-overbought bars, so entry gating is effectively CCI-led; the exit RSI leg (`rsi45 > 88`) passes only on near-overbought bars, so signal exits are rare by construction and round-trips close overwhelmingly via the ROI ladder or the stop. Neither leg is dropped, widened, or re-thresholded here.
- Same-bar co-print pin (possible in principle, resolved by position pin — disclosed, not repaired): entry and exit read different CCI/RSI windows, so one bar can in principle print both (deep-then-snapping tape with both RSIs inside the 88–90 sliver). No engine ordering is invented: under the single-unit position pin, a flat book treats any co-print bar as entry (the exit leg needs a position and is a no-op without one — no same-bar round-trip), while a positioned book treats it as exit-close. ROI/stop legs start at zero distance on the entry bar — disclosed, not repaired.
- Direction: long-only. Zero `short` tokens ship anywhere — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the two-conjunct signal exit, the four-rung decaying ROI ladder, and the −34.338% stop are the complete position-closing set. No trailing, no time exit beyond the ladder, no breakeven move — explicitly none, not invented.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment`/`max_open_trades` ships anywhere); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying washout bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar OHLC (`high`/`low`/`close` for the CCI paths, `close` for the RSI paths) with fixed non-negative window offsets (no bar-shift edge anywhere — both legs read the decision bar only, no forward reference) — no volume/funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, informative merge (`informative_pairs` returns `[]`), interpolate, or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `15m` bars of BTCUSDT: `high`/`low`/`close` for the CCI(72)/CCI(66) paths; `close` for the RSI(36)/RSI(45) paths. No `volume`, funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `15m` (source-native — the file prints `timeframe = '15m'`). One evaluation per completed bar; every window reads the decision bar and its causal past only; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher floor, disclosed): the record-rule floor holds 100 fifteen-minute bars flat (~25 hours). Covers the 80-bar precompute span, the 72-bar longest effective seed, and indicator construction with margin. Coded behaviour underneath: TA-Lib seeds print NaN until windowed (every strict NaN comparison false — no leg can fire early; no `fillna`/`ffill` exists to smear them). No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, signal-exit, and ROI/stop legs are all bar-close-evaluated; the rare same-bar co-print resolves by the disclosed position pin, leaving no invented engine ordering.
- Interval precedent (exact, disclosed): an exact-`15m` PASS record already sits on `main` (the admitted CMCWinner triple-oscillator record — `15m` Freqtrade-sourced long-flat at its repository pin) — this record rides the same specified single-frame completed-bar `15m` Binance candle path, not an assumed one. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the same specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding. The price-only feed is a strict subset of that path's candle (no volume leg exists here at all).
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI ladder and stop percentage are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the washout entry opens the full unit on a flat book; signal exit, any ROI rung, or the stop closes it in full; re-entry after an exit needs only the next qualifying washout bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (110 lines: the four-family CCI/RSI precompute loops, the two-conjunct washout entry, the two-conjunct reclaim exit, the `timeframe`/`minimal_roi`/`stoploss` literals, the module-constant mirror, the `buy_params`/`sell_params` freeze, and the `SwingHighToSky(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: TA-Lib CCI/RSI seeds print NaN until windowed (every strict NaN comparison false — no early entry, no early exit; no `fillna`/`ffill` exists to smear seeds forward). The 100-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired.
2. Exact-touch rule fenced: strict `<`/`>` fires nothing on equality on every conjunct (CCI exactly −175/−106, RSI exactly 90/88 holds flat) — disclosed, not smoothed.
3. Co-print arithmetic fenced (possible, resolved — disclosed, not repaired): the two legs read different windows, so a snapping bar can in principle co-print both; the position pin resolves it (flat → enter, positioned → exit-close, never a same-bar round-trip). ROI/stop legs start at zero distance on the entry bar — disclosed, not repaired.
4. Zero-variance fenced: flat tape pins CCI at 0 (failing the `< −175` conjunct — no entry can print) and RSI midscale (failing neither RSI conjunct alone, but the CCI conjuncts gate both legs). No division by zero exists in the gating path (all legs are comparisons; indicator division lives inside the library calls, never in a gate denominator) — disclosed, not repaired.
5. Permissive/restrictive asymmetry fenced: entry RSI `< 90` vetoes only blow-off bars; exit RSI `> 88` makes signal exits rare by construction — round-trips close overwhelmingly via ROI/stop. Disclosed as effective behaviour, never re-thresholded.
6. Dead-code plumbing fenced: `reduce`, `numpy`, `qtpylib`, and `DataFrame`-only hints are imported and never called in the gating path; the eight `IntParameter` low/high ranges, `optimize=True` spaces, and `default=100/20/30/26` placeholders never govern under the `buy_params`/`sell_params` freeze — this record never conditions on them and no reviewer repair may promote any of them into a leg. Adopting any other point of the declared spaces would be a different, unpinned rule.
7. Cousin records fenced as different constructions (none trades a 72/36 CCI-RSI washout entered deep-oversold and reclaimed near-overbought on `15m`): the admitted MACDStrategy sibling trades a MACD-line vs signal-line state with CCI polarity on `5m` (different primitives, different frame); the admitted Simple sibling trades MACD-plus-Bollinger-plus-RSI momentum confluence (never a dual-threshold washout); the admitted Quickie sibling trades a single TEMA(9) slope against the Bollinger midline with an ADX gate (slope-plus-band, never CCI/RSI levels); the admitted strategy003 sibling trades an RSI-ceiling plus MFI washout with an EMA-regime OR-arm (RSI direction inverted, MFI-gated, different exit); the admitted strategy004 sibling trades an ADX-gated CCI washout with a hand-rolled dual-STOCHF recross (no RSI reclaim exit); the admitted CofiBit sibling trades a fast-stoch oversold edge with EMA rails (edge primitive, never level states); the admitted UniversalMACD sibling trades a single EMA-ratio band with an empty signal exit (no oscillator at all). Not a threshold re-tuning of any of them: changing any period, threshold, ROI rung, or risk literal would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: every other `user_data/strategies/*.py` sibling is a separate pin — its constants must never be substituted into this record.
9. Derivation boundary fenced: the non-source-native behaviours in this record are exactly the five declared adaptations (BTCUSDT market choice, same-bar-close fills, single-unit/no-add/no-cooldown position pin with 100-bar warmup floor, derived signal-exit/roi-on-entry-bar execution semantics, house sizing/costs) — all predeclared above. The `15m` frame, the CCI(72)/RSI(36) washout entry, the CCI(66)/RSI(45) reclaim exit, the frozen hyperspace literals, the ROI ladder, the −34.338% stop, the absent trailer, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: washout entry / all four periods / all four frozen thresholds / reclaim exit / ROI ladder / −34.338% stop / single-unit long-only / `15m` BTCUSDT / same-bar-close fills are frozen.

- F1 — CCI-severity relevance: softening the entry CCI leg to `< -100` (same RSI ceiling, same exit/risk) must not improve net expectancy; fail ⇒ the far-tail −175 severity adds nothing over a mild-oversold filter.
- F2 — Reclaim-leg relevance: dropping the signal-exit leg entirely (ROI/stop-only exits, same entry) must not materially change round-trip outcomes; fail ⇒ the rare reclaim leg carries weight beyond decoration.
- F3 — RSI-ceiling relevance: dropping the permissive `rsi36 < 90` entry conjunct (pure CCI-72 washout entry, same exit/risk) must not improve net expectancy; fail ⇒ the blow-off veto adds nothing over the bare CCI washout.

## Crypto portability

BTCUSDT Binance perpetual `15m` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count, portable across 24/7 crypto tape. Only the `high`/`low`/`close` candle fields are read (venue definition differences move only oscillator inputs, disclosed). Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- TA-Lib CCI/RSI internals live in their library outside the pinned file — pinned by call with explicit periods, not re-derived; exact reproduction inherits that module's seeding and rolling semantics alongside the file-local threshold wiring, under the disclosed 100-bar floor.
- Hyperopt scaffolding is frozen, not searched: the eight `IntParameter` ranges and `optimize=True` spaces never execute as search under this record; only the `-175/72/90/36` buy and `-106/66/88/45` sell literals govern. Any re-optimization would be a different, unpinned rule.
- The signal exit is rare by construction (45-bar RSI above 88) — almost every round-trip closes via the ROI ladder or the stop. This record repairs nothing: the effective behaviour is fully explicit and complete, and any livelier exit band would be a different, unpinned rule no reviewer may invent.
- No trailing, no breakeven, no time exit beyond the ROI ladder, no short leg, no cooldown — all explicitly absent, never to be added by repair. The permissive-vs-restrictive RSI asymmetry rides the file literals — disclosed as the record's principal behavioural risk.
- The file declares no order-type plumbing at all — fills are wholly under the derived same-bar-close convention; this record makes no claim about any live-order behaviour.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/SwingHighToSky.py
- https://github.com/freqtrade/freqtrade-strategies
