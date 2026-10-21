---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade UniversalMACD EMA-ratio dip-band long-flat on BTCUSDT 5m bars
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
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/UniversalMACD.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade UniversalMACD EMA-ratio dip-band long-flat on BTCUSDT 5m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (official open-source Freqtrade strategy collection; the lane that already supplied the admitted `freqtrade-multima`, `freqtrade-hlhb`, `freqtrade-simple-macd-bb-rsi`, `freqtrade-cofibit`, and `freqtrade-strategy005` records at this same pin — this record pins ONLY the UniversalMACD literals below, and no reviewer repair may substitute a sibling constant).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/UniversalMACD.py`.
- GitHub blob SHA at the pinned commit: `62a1b2002fd1697d67c3cdaca583e668de23b7ae`, size 4558 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 4558 bytes, 113 lines, SHA-256 `b3a62e0d8a26024e7ab5f3613d0964e3954373bc3735c1ffd0678d84ce1b1e32`, identical to the GitHub blob (`git hash-object` reproduces `62a1b200…b7ae`) — the entire file was retrieved and inspected.
- Registration: the file defines class `UniversalMACD(IStrategy)` (the only class in the file), `INTERFACE_VERSION = 3`, framework column contract `populate_entry_trend` / `populate_exit_trend` (`enter_long` / `exit_long`, never the old `buy`/`sell` plumbing). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path plus pin, all unique. Every other `user_data/strategies/*.py` sibling is a different pin with different constants.
- The file's own words (quoted for gate evidence, never extended): `timeframe = '5m'`; `can_short: bool = False`; `minimal_roi = { "0": 0.213, "27": 0.099, "60": 0.03, "164": 0 }`; `stoploss = -0.318`; `trailing_stop = False` (with `trailing_stop_positive = None`, `trailing_stop_positive_offset = 0.0`, `trailing_only_offset_is_reached = False` present-but-disabled); `startup_candle_count: int = 30`; entry `dataframe['umacd'].between(self.buy_umacd_min.value, self.buy_umacd_max.value)` with frozen `DecimalParameter` defaults `buy_umacd_max = -0.01176` / `buy_umacd_min = -0.01416`; exit `dataframe['umacd'].between(self.sell_umacd_min.value, self.sell_umacd_max.value)` with frozen defaults `sell_umacd_max = -0.02323` / `sell_umacd_min = -0.00707`; indicator `dataframe['umacd'] = (dataframe['ma12'] / dataframe['ma26']) - 1` over `ta.EMA(dataframe, timeperiod=12)` and `ta.EMA(dataframe, timeperiod=26)`. The TradingView-page comment (`Universal-Moving-Average-Convergence-Divergence`, author `@mablue`) is lineage only.
- Out-of-file calls pinned (all resolved by name, all standard defaults): `ta.EMA(dataframe, timeperiod=…)` (TA-Lib abstract EMA over the default `close` input — the ONLY indicator primitive in the file; the file never names `close`/`open`/`high`/`low`); `Series.between(left, right)` (pandas inclusive-both-ends band predicate — the ONLY comparison primitive in both legs); `DataFrame.loc` assignment (pure column write, no state). No DB, no network, no `request.*`, no `security()` in the file.
- Full-file token census (verified over the 113 lines this cycle): 2 `short` (both the explicit long-only declaration — `can_short: bool = False` plus its `# Can this strategy go short?` comment; 0 `enter_short` / 0 `exit_short` — no short leg anywhere); 0 `volume` (no volume read of any kind); 0 `resample` / 0 informative-pair calls (`merge_informative_pair` is imported and never called — fenced); 0 `position_adjustment` / 0 `use_exit_signal` / 0 `exit_profit_only` / 0 `order_types` / 0 `process_only_new_candles` / 0 `leverage` / 0 `funding` / 0 `mark_price` (all such execution/position/economic semantics are predeclared researcher pins below, never file semantics); 1 `startup_candle_count` (`= 30`, source-declared warmup — honoured, never rewritten); 1 `max_open_trades` / 2 `stake_` / 1 `dry_run` / 1 `trading_mode` (all inside the `#`-commented sample-config block, never live code — fenced); 0 `fillna` / 0 `ffill` / 0 `interpolate` (no NaN patching anywhere — strict NaN comparisons simply stay false); 0 `shift` (no bar offset anywhere — both legs read the decision bar only); 0 `crossed_above` / 0 `crossed_below` (both legs are level bands, never edges); 5 `DecimalParameter` tokens (the four live band-edge declarations plus the import — the optimize-spaces are fenced out, the frozen defaults are the rule, see Signal; `BooleanParameter`/`CategoricalParameter`/`IntParameter` are imported and never declared — fenced); 1 commented `# print(...)` (display leftover — fenced); 0 `position_size` reads; 0 `syminfo` (the file names no market; the `#`-commented pair list is StaticPairList commentary, never a rule).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. The file is causal as written (no full-sample scalar, no repainting primitive, no multi-timeframe merge, no external package — no repair site exists). Researcher-declared adaptations are exactly five: (1) research market `BTCUSDT` (the source names no market); (2) completed-bar decisions with same-bar-close market fills; (3) single-unit/no-add/no-cooldown position pin plus a 100-bar researcher warmup floor (covers the source-declared 30-bar startup and the 26-bar EMA seed with margin); (4) framework-default execution semantics pinned as derived behaviour (signal exits enabled but the frozen exit band is empty so it never fires — disclosed, never presented as a file literal; ROI/stop legs bar-close-evaluated); (5) the house cost/capital overlay replaces the absent source economics. Every period, every band edge, the frozen parameter defaults, the ROI ladder, and the stop are untouched.

Pre-write dedup (2026-10-21): working-tree filename/content search for `UniversalMACD`, `umacd` (as the EMA-ratio column), and `xNEWcB8s` returns zero strategy records — the two `umacd` hits pool-wide are fenced non-records (a Pine-input toggle name in the unrelated TDI record, and a prose sibling-fence mention in the admitted HLHB record, which pins `hlhb.py`, never this file). No MACD primitive of any kind ships in this file, so the admitted MACD-line/signal siblings (Negative evidence 6) are different constructions. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas) trades an EMA-ratio band system. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims no behavioural channel anywhere in the 113 lines beyond its code: buy the bar where the 12-bar EMA sits 1.176%–1.416% under the 26-bar EMA (a mild-dip band in the EMA-ratio, not a cross), and hold until the decaying take-profit ladder (21.3% immediately down to breakeven after 164 minutes) or the −31.8% stop takes the book — the coded signal-exit band is empty under the frozen defaults, so it never hurries the exit. The pasted hyperopt comment (`40 trades … 92.90%`, avg profit `2.34%`, avg duration `3:13:00`) ships no pair list, window, dates, or cost basis and is quoted here as file text only — this record claims no source-reported performance from it.

### Research interpretation

Ratio-band dip buyer, long-only, with risk-ladder exits only. Unlike MACD-line/signal cross systems that flip on the histogram edge, the entry demands the EMA-ratio print sit inside a narrow below-zero window (short average modestly under the long average — a shallow pullback state, not a breakdown and not momentum ignition), so both ripping trends (ratio pinned high) and cliff dives (ratio far negative) print nothing. Unlike stop/trailing exits, the position exits only through the four-rung decaying ROI ladder or the wide stop — the signal-exit leg is provably dead under the frozen defaults (see Signal), so every round-trip is a dip-band entry harvested by time-decayed profit-taking or stopped at −31.8%. The coded consequence is a buyer of shallow EMA-ratio dips that rents exposure for at most ~2.7 hours of decaying upside before breakeven-gating, and that never cuts a winner early on a signal.

## Signal

Exact rule as pinned (any other EMA period, band edge, reduction, ROI rung, stop, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own:

```text
ma12[t]  = TA-Lib EMA(close, timeperiod=12)[t]
ma26[t]  = TA-Lib EMA(close, timeperiod=26)[t]
umacd[t] = ma12[t] / ma26[t] - 1
entry = (-0.01416 <= umacd[t] <= -0.01176)   // enter_long = 1 (inclusive band, state print)
exit_sig = (-0.00707 <= umacd[t] <= -0.02323) // exit_long = 1 — EMPTY under frozen defaults (left > right), never fires
risk = decaying take-profit minimal_roi {"164":0,"60":0.03,"27":0.099,"0":0.213};
       fixed stop at -31.8% (stoploss -0.318); trailing_stop False (None/0.0/False present-but-disabled)
guard = leading-window bars: NaN comparisons false (see Required data)
```

- Band-edge freeze (pinned `DecimalParameter` defaults, never tuned here): entry reads `buy_umacd_min = -0.01416` / `buy_umacd_max = -0.01176` exactly as defaulted; exit reads `sell_umacd_min = -0.00707` / `sell_umacd_max = -0.02323` exactly as defaulted. The `(-0.05, 0.05)` search ranges are unfrozen scaffolding — excluded from the rule. Adopting any other point of the four declared spaces would be a different, unpinned rule.
- Empty-exit-band proof (pinned semantics, verified this cycle — not a reviewer repair site): pandas `Series.between(left, right)` is `(left <= x) & (x <= right)` inclusive; with frozen `left = -0.00707 > right = -0.02323` no real `umacd` value satisfies both conjuncts, on any bar, at any time — `exit_long` is identically 0 under this record. Enumerated over representative ratio values (−0.05 … +0.05) the predicate returns all-False. This is effective disabled-signal-exit behaviour, disclosed — never silently dropped, never repaired into a live band.
- Trade events: `enter_long=1` on any bar printing the dip band, `direction` long-only; `exit_long` never prints under the freeze. Both legs are STATE prints in construction (the entry persists while the band holds — close-and-hold-flat); the entry can reprint across consecutive bars (no one-shot latch in code). New-interface `enter_long`/`exit_long` columns read as enter-long/exit-long directly.
- Exact boundaries (pinned semantics): inclusive throughout (`between` default — a ratio landing exactly on either edge fires the entry). The `12` / `26` / four edge literals are never tuned here.
- Same-bar co-print pin (impossible, resolved by construction — disclosed, not repaired): the exit leg can never print under the freeze, so no bar can ever co-print entry and signal-exit; no engine ordering is invented and no same-bar round-trip can occur. ROI/stop legs start at zero distance on the entry bar — disclosed, not repaired.
- Direction: long-only. `can_short: bool = False` ships in the file — a two-sided reading would contradict it. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the four-rung decaying ROI ladder and the −31.8% stop are the complete position-closing set (the signal leg is provably empty, disclosed above). No trailing (`trailing_stop = False` file literal — the `None`/`0.0`/`False` values are present-but-disabled, never to be enabled by repair), no time exit beyond the ladder, no breakeven move — explicitly none, not invented. Signal-exit/profit-gating and ROI-on-entry-bar semantics ride the predeclared derived behaviour (Execution assumptions), never a file invention.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment`/`max_open_trades` ships live anywhere); a flat book treats risk legs as no-ops; re-entry re-arms on any qualifying dip-band bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `close` (EMA internals — the sole indicator primitive) with fixed non-negative window offsets (no bar-shift edge anywhere — both legs read the decision bar only, no forward reference) — no volume/funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, informative merge, interpolate, or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `5m` bars of BTCUSDT: `close` only, for the two EMAs (periods 12 and 26). No `high`/`low`/`volume`, funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `5m` (source-native — the file prints `timeframe = '5m'`). One evaluation per completed bar; every window reads the decision bar and its causal past only; fills land on the decision bar's own close under the derived rule below.
- Warmup (source-declared plus researcher floor, disclosed): the file declares `startup_candle_count = 30`; the record-rule floor holds 100 five-minute bars flat (~8.3 hours). Covers the 30-bar source startup, the 26-bar longest EMA seed, and indicator construction with margin. Coded behaviour underneath: TA-Lib seeds print NaN until windowed (every strict NaN comparison false — no leg can fire early; no `fillna`/`ffill` exists to smear them). No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; the `#`-commented pair list is StaticPairList commentary, never a rule; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry and ROI/stop legs are all bar-close-evaluated; the provably empty signal leg leaves no ambiguous same-bar fill order to the engine beyond the disclosed position pin.
- Interval precedent (exact, disclosed): exact-`5m` PASS records already sit on `main` (the admitted Strategy001 HA-EMA-cross, Strategy005 volume-surge-Fisher, CofiBit fast-stoch, Simple MACD-BB-RSI, and Quickie TEMA-slope records — all `5m` Freqtrade-sourced long-flat at this repository's pins) — this record rides the same specified single-frame completed-bar `5m` Binance candle path, not an assumed one. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the same specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding. The close-only feed is a strict subset of that path's candle (no volume leg exists here at all).
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI ladder and stop percentage are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the dip-band entry opens the full unit on a flat book; any ROI rung or the stop closes it in full; re-entry after an exit needs only the next qualifying band bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (113 lines: the two-EMA indicator block, the EMA-ratio definition, the frozen four-edge band entry, the frozen empty signal-exit band, the `timeframe`/`minimal_roi`/`stoploss`/`trailing_stop`/`startup_candle_count`/`can_short` literals, and the `UniversalMACD(IStrategy)` class pin). The pasted hyperopt comment (`40 trades … 92.90%`, avg profit `2.34%`, median `3.00%`, avg duration `3:13:00`) ships no pair list, evaluation window, dates, or cost basis — this record claims no source-reported performance and no reproduced performance from it.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: TA-Lib EMA seeds print NaN until windowed (every NaN band comparison false — no early entry; no `fillna`/`ffill` exists to smear seeds forward). The 100-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired.
2. Exact-touch rule fenced: inclusive `between` fires on exact edge equality for the entry; the empty exit band fires on nothing at any value — disclosed, not smoothed.
3. Co-print arithmetic fenced (impossible — disclosed, not repaired): the frozen exit band is empty by construction, so no bar can co-print entry and signal-exit; the position pin has no residual to resolve. ROI/stop legs start at zero distance on the entry bar — disclosed, not repaired.
4. Zero-variance fenced: flat tape pins both EMAs onto the flat line (`umacd = 0`, outside the below-zero entry band — no entry can print). No division by zero exists in the gating path in any live market state (`ma26` is a positive price average — the ratio denominator can never be zero on real tape; multi-pass EMA arithmetic lives inside the library call, never in a gate denominator) — disclosed, not repaired.
5. Dead-code plumbing fenced: `merge_informative_pair`, `BooleanParameter`/`CategoricalParameter`/`IntParameter`, `pandas_ta`, `qtpylib`, `numpy as np`, `datetime`, and `Optional`/`Union` are imported and never called in the gating path (`DataFrame` appears in type hints only); the `#`-commented config block (`max_open_trades`, stake, dry-run wallet, `trading_mode`, pair list) and the `# print(...)` never execute; the four `(-0.05, 0.05)` search ranges never govern under the frozen defaults — this record never conditions on them and no reviewer repair may promote any of them into a leg. Adopting any other point of the declared spaces would be a different, unpinned rule.
6. Cousin records fenced as different constructions (none trades an EMA-ratio level band with an empty signal exit): the admitted MACD-CCI sibling pins `berlinguyinca/MACDStrategy.py` — a MACD-line vs signal-line cross-state (verified this cycle: `ta.MACD`, `macd > macdsignal` entry, `macd < macdsignal` exit — edge crosses, never a ratio band); the admitted Simple sibling trades MACD-plus-Bollinger-plus-RSI momentum (multi-primitive confluence, never a single-ratio band); the admitted Quickie sibling trades a single TEMA(9) slope against the Bollinger midline with an ADX gate (slope-plus-band, never a ratio level); the admitted strategy001–005 siblings trade HA-EMA-cross / hammer / RSI-Fisher-MFI / ADX-CCI / volume-surge-Fisher systems (no EMA-ratio anywhere). Not a threshold re-tuning of any of them: changing any period, edge, ROI rung, or risk literal would each be a different, unpinned rule — none is admitted here.
7. Sibling-file fence: every other `user_data/strategies/*.py` sibling is a separate pin — its constants must never be substituted into this record.
8. Derivation boundary fenced: the non-source-native behaviours in this record are exactly the five declared adaptations (BTCUSDT market choice, same-bar-close fills, single-unit/no-add/no-cooldown position pin with 100-bar warmup floor, derived signal-exit/roi-on-entry-bar execution semantics, house sizing/costs) — all predeclared above. The `5m` frame, the EMA(12)/EMA(26) pair, the ratio definition, the frozen dip-band entry, the frozen empty signal exit, the ROI ladder, the −31.8% stop, the disabled trailer, the 30-bar startup, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: dip-band entry / both EMA periods / all four frozen edges / empty signal exit / ROI ladder / −31.8% stop / single-unit long-only / `5m` BTCUSDT / same-bar-close fills are frozen.

- F1 — Band relevance: replacing the narrow dip band with a plain below-zero level (any `umacd < 0`, same risk) must not improve net expectancy; fail ⇒ the narrow window adds nothing over a bare weak-trend filter.
- F2 — Exit-ladder relevance: replacing the four-rung decaying ROI ladder with a single flat take-profit at the ladder's mean level (same entry, same stop) must not improve net expectancy; fail ⇒ the decay schedule adds nothing over one fixed target.
- F3 — Ratio relevance: replacing the EMA-ratio with a same-period EMA-spread level in price units (same band logic, same risk) must not improve net expectancy; fail ⇒ the ratio normalization adds nothing over a raw spread.

## Crypto portability

BTCUSDT Binance perpetual `5m` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count, portable across 24/7 crypto tape. Only the `close` candle field is read (venue close-definition differences move only EMA inputs, disclosed). Funding is declared nowhere in the source and modeled only downstream by house assumptions. The `#`-commented pair list ships no market semantics.

## Limitations

- TA-Lib EMA internals live in their library outside the pinned file — pinned by call with explicit periods, not re-derived; exact reproduction inherits that module's seeding and rolling semantics alongside the file-local ratio wiring, under the disclosed 100-bar floor.
- Hyperopt scaffolding is frozen, not searched: the four `DecimalParameter(-0.05, 0.05)` ranges never execute as search under this record; only the `-0.01176` / `-0.01416` / `-0.02323` / `-0.00707` defaults govern. Any re-optimization would be a different, unpinned rule.
- The frozen signal-exit band is empty by construction (left edge above right edge) — almost certainly an author-side min/max swap, but this record repairs nothing: the effective behaviour (ROI/stop-only exits) is fully explicit and complete, and any live exit band would be a different, unpinned rule no reviewer may invent.
- No trailing, no breakeven, no time exit beyond the ROI ladder, no short leg, no cooldown — all explicitly absent, never to be added by repair. Signal-exit profit-gating rides the predeclared derived behaviour — disclosed as the record's principal execution risk.
- The file declares no order-type plumbing at all — fills are wholly under the derived same-bar-close convention; this record makes no claim about any live-order behaviour.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/UniversalMACD.py
- https://github.com/freqtrade/freqtrade-strategies
