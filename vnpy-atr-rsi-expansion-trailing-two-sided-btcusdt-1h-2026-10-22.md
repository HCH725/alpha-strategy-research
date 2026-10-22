---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: vnpy AtrRsi ATR-expansion-gated RSI-threshold breakout with hand-rolled trailing stop two-sided on BTCUSDT 1h bars
created: 2026-10-22
updated: 2026-10-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-05
sources:
  - https://github.com/vnpy/vnpy_ctastrategy/blob/7a8768de9784dda35a7b261a7ade1dbfbff50919/vnpy_ctastrategy/strategies/atr_rsi_strategy.py
  - https://github.com/vnpy/vnpy_ctastrategy
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# vnpy AtrRsi ATR-expansion-gated RSI-threshold breakout with hand-rolled trailing stop two-sided on BTCUSDT 1h bars

## Provenance

Immutable sources actually read end to end (primary artifacts for all rule citations):

- Strategy repository URL: https://github.com/vnpy/vnpy_ctastrategy (open-source vnpy CTA strategy collection; no record in the pool pins any file from this repository — first vnpy lane record).
- Strategy pinned commit SHA: `7a8768de9784dda35a7b261a7ade1dbfbff50919` (committed `2026-10-05T14:22:15Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact strategy file path: `vnpy_ctastrategy/strategies/atr_rsi_strategy.py`.
- GitHub blob SHA at the pinned commit: `c31ea8a61769d7618cac50efefff9291bb1034b6`, size 3767 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 3767 bytes, 145 lines, SHA-256 `b71ecf36e51e53dec8610c72680cd01435caad8b880869ae039f4111537dc1f0`, identical to the GitHub blob (`git hash-object` reproduces `c31ea8a6…b1034b6`) — the entire file was retrieved and inspected.
- Registration: the file defines class `AtrRsiStrategy(CtaTemplate)` (the only strategy class in the file). vnpy strategies carry no roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `boll_channel_strategy.py`, `double_ma_strategy.py`, `dual_thrust_strategy.py`, `king_keltner_strategy.py`, `multi_signal_strategy.py`, `multi_timeframe_strategy.py`, `test_strategy.py`, and `turtle_signal_strategy.py` are different pins with different rules — this record pins ONLY the atr_rsi file's literals below, and no reviewer repair may substitute a sibling constant.
- Indicator-library pin (the strategy file's `am.atr` / `am.rsi` calls resolve here, read end to end for the `ArrayManager` section): https://github.com/vnpy/vnpy, pinned commit `c6e231caf32b7fc97e6459817fff66458cf7e7c4` (repository HEAD via `git ls-remote`, committed `2026-10-06T09:38:50Z`), file `vnpy/trader/utility.py`, blob `e88c46dc334bce9c776b2033909310e02bc3531c`, 41642 bytes (`git hash-object` reproduces the blob). `ArrayManager(size: int = 100)` default; `inited` flips true once `count >= size`; `atr(n)` returns `talib.ATR(high, low, close, n)`; `rsi(n)` returns `talib.RSI(close, n)` — standard TA-Lib Wilder semantics, pinned by call, never re-derived.
- The strategy file's own words (quoted for gate evidence, normalized where Chinese, never extended): module docstring `ATR与RSI策略` (ATR-and-RSI strategy); class docstring `用ATR与RSI开仓，并用跟踪止损平仓的策略` (entries with ATR and RSI, exits with a trailing stop); parameters `atr_length: int = 22`, `atr_ma_length: int = 10`, `rsi_length: int = 5`, `rsi_entry: int = 16`, `trailing_percent: float = 0.8`, `fixed_size: int = 1`; init arithmetic `rsi_buy = 50 + rsi_entry` / `rsi_sell = 50 - rsi_entry` (i.e. 66 / 34); gate `atr_value > atr_ma`; entries `buy(bar.close_price + 5, fixed_size)` on `rsi_value > rsi_buy`, `short(bar.close_price - 5, fixed_size)` on `rsi_value < rsi_sell`, both strictly inside the `pos == 0` branch; exits `sell(long_stop, abs(pos), stop=True)` with `long_stop = intra_trade_high * (1 - trailing_percent / 100)` inside the `pos > 0` branch and the mirror `cover(short_stop, abs(pos), stop=True)` with `short_stop = intra_trade_low * (1 + trailing_percent / 100)` inside the `pos < 0` branch; per-bar `cancel_all()` then re-issue; `load_bar(10)` history feed. No `minimal_roi`, no fixed `stoploss`, no time exit, no `can_short` flag (vnpy CTA trades both sides natively — both order legs are coded), no `position_adjustment`, no `startup_candle_count` (the warmup below rides the source's own `am.inited` gate with the pinned default size 100).
- Full-file token census (verified over the 145 lines this cycle): 0 `volume` (the only tick/volume-adjacent tokens are the `TickData` import and the `on_tick` → `bg.update_tick` aggregation plumbing that feeds bar construction — the decision path in `on_bar` reads bar high/low/close only; `open_price`, `volume`, `turnover`, `open_interest` are never read anywhere in the file); 0 `resample` / 0 `informative`; 0 hyperopt spaces (the `parameters` list names the same six file-literal attributes for vnpy's optimization registry — it defines no search range, and every value used below is the file literal); 0 `request.*`; 0 `security(`; 0 session/calendar calls; 2 `stop=True` (the two trailing-stop legs and nothing else); 1 `cancel_all`; 1 `fixed_size`; exhaustive `pos == 0` / `pos > 0` / `pos < 0` branch cover with entries coded ONLY in the flat branch and stops coded ONLY in the positioned branches.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live vnpy deployment. The source pins the ATR22-vs-SMA10 expansion gate, the RSI5 66/34 threshold pair, the flat-only entries, the 0.8% hand-rolled trailing stops, the fixed size 1, and the two-sided stance — but ships no market, no interval (vnpy CTA runs on whatever bar feed it is given), no venue spelling, and no fill-timing flag. Researcher-declared adaptations are exactly five: (1) research market `BTCUSDT` on completed `1h` bars (the file names no market and no interval; the `1h` choice is purely the researcher's on an already-admitted interval, and no source-market equivalence is claimed); (2) completed-bar decisions with same-bar-close market fills (the source backtester fills the marketable limit chase `close ± 5` same-bar and stop-market orders intrabar — the `± 5` point chase is a legacy futures-tick artifact dropped here, derivation disclosed, never presented as source-engine timing); (3) trailing-stop legs close-evaluated (a completed bar breaching the stop level exits flat at that bar's close, following the admitted `cci-ema-rsi-cross-trailing-stop-btcusdt-1h` ratchet-stop precedent — derivation disclosed, never presented as intrabar stop-market fills); (4) single-unit position pin `pos ∈ {−1, 0, +1}` (restates the source's `fixed_size = 1` with flat-only entries — source-native state, restated not redesigned); (5) the absent sizing/costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-22): working-tree filename/content search for `atrrsi`, `atr_rsi`, `atr-rsi` returns no strategy record pinning this source file (the only `AtrRsi` hits are the QQE envelope records — an ATR-of-RSI band construction, a different mechanism fenced in Negative evidence 7). No record in the pool comes from the `vnpy_ctastrategy` repository at all. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles band-ratio) trades an ATR-expansion × RSI-threshold conjunction with trailing-stop exits. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code and docstrings print: buy the bar where price-ATR sits above its own average together with RSI5 printing above 66 (volatility-expansion regime plus overbought-momentum entry), short the bar where ATR sits above its own average together with RSI5 printing below 34 (expansion regime plus oversold-momentum entry), and nurse every position with a 0.8% trailing stop ratcheted from the trade's intrabar extremum. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Volatility-expansion momentum machine, two-sided with genuine flat states. The ATR leg is a regime veto, not a direction signal: entries print ONLY while ATR22 trades above its own 10-bar average, so flat-volatility chop prints nothing on either side no matter what RSI reads. The RSI5 66/34 pair supplies the side: momentum continuation entries (buy strength, short weakness) rather than mean-reversion fades. The 0.8% trailing stop is the ONLY exit — there is no opposite-signal exit, no profit target, no time stop — so a trend that never pulls back 0.8% from its extremum is ridden indefinitely, while a Strat that spikes and reverses is cut at the ratchet. Because entries are gated on `pos == 0` and stops exist only when positioned, the book can never pyramid, never reverse directly, and never faces a same-bar entry-vs-exit ordering choice.

## Signal

Exact rule as pinned (any other ATR/RSI lengths, thresholds, trailing percent, entry gating, exit set, frame, or book is a different, unpinned rule). Decision bar `t` is always a completed `1h` bar; every read is at index `≤ t`:

```text
atr[t]    = TA-Lib ATR(high, low, close, 22)[t]      // via pinned ArrayManager
atrma[t]  = mean(atr[t-9], ..., atr[t])              // 10-bar average of ATR
rsi[t]    = TA-Lib RSI(close, 5)[t]                  // via pinned ArrayManager
regime[t] = (atr[t] > atrma[t])                      // strict volatility-expansion gate
FLAT book:   long_sig[t]  = regime[t] AND (rsi[t] > 66)  → open long  at close t
             short_sig[t] = regime[t] AND (rsi[t] < 34)  → open short at close t
LONG book (entered bar e < t): intra_high = max(high[e..t]);
             stop[t] = intra_high * 0.992; if (low[t] <= stop[t]) → flat at close t
SHORT book (entered bar e < t): intra_low = min(low[e..t]);
             stop[t] = intra_low * 1.008;  if (high[t] >= stop[t]) → flat at close t
floor     = first 100 completed bars held flat (see Required data)
```

- Trade events: entries print only on a flat book; the stop legs print only on a positioned book, starting the bar AFTER the entry bar (the source codes entries strictly inside the `pos == 0` branch and stops strictly inside the `pos ≠ 0` branches, so the entry bar itself never evaluates a stop — preserved). A positioned book treats further entry-gate bars as hold-no-ops under the position pin below; a flat book treats stop legs as no-ops (no stop exists).
- Exact boundaries (pinned semantics): the regime gate is strict (`>` — `atr == atrma` prints nothing); the RSI legs are strict (`> 66`, `< 34` — a print of exactly 66.0 or 34.0 fires neither leg); the stop triggers are inclusive (`low <= stop`, `high >= stop` — a touch fills). The 66/34 pair is `50 ± rsi_entry(16)` computed in `on_init`, quoted above — a bar with `rsi == 66` satisfies neither leg. All preserved throughout.
- Mutual-exclusion proof (no tie-break pin required): on a flat book, `long_sig` needs `rsi[t] > 66` while `short_sig` needs `rsi[t] < 34` — mutually exclusive on every bar, degenerate or otherwise, and the regime gate is shared, so both legs never co-print. Entries and stop-exits never meet on the same book either (entries exist only when flat, stops only when positioned). The reviewer is never asked to invent an ordering.
- Direction: two-sided. Both `buy` and `short` legs are coded with symmetric gates; vnpy CTA supports both sides natively with no `can_short` flag anywhere. The two-sided book expresses on a perpetual venue under the house overlay (see Crypto portability); no naked-spot construction is required.
- Exits and risk (explicit and complete): the 0.8% trailing stop per side is the entire position-closing set. No ROI ladder, no fixed stop, no time exit, no breakeven move, no opposite-signal exit — explicitly none further, not invented. The per-bar `cancel_all()` + re-issue in the source is stop-maintenance plumbing with no signal content; the derived close-evaluated equivalent needs no pending-order state (see Execution assumptions).
- Position rule (source-native state, restated): single unit, `pos ∈ {−1, 0, +1}`; entries only from flat (no pyramiding, no averaging — no `position_adjustment` ships anywhere); no direct reversal (a positioned book never evaluates the opposite entry leg — the source `elif` chain, preserved); re-entry re-arms on any qualifying flat-book bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low`/`close` (ATR true-range smoothing, RSI Wilder smoothing, plus fixed non-negative lookbacks — no forward reference); the decision bar's own forming values are never read. No `open` read, no bar `volume` read, no funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path. The `on_tick` → `BarGenerator` path is bar-construction plumbing: it aggregates ticks into the same completed bars the rule reads and takes no decision.

## Required data

- Completed `1h` bars of BTCUSDT: `high`/`low`/`close` only (ATR on `high`/`low`/`close`; RSI on `close`). No `open` read, no bar `volume` read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1h` (researcher-declared — the source ships no interval; vnpy CTA consumes whatever bar feed it is given. `1h` rides existing admission precedent on `main`, so no novel-interval confirmation burden attaches — see Execution assumptions).
- Warmup (source-constructive, disclosed): 100 completed `1h` bars held flat. The source gates every decision on `am.inited`, which flips true only after `count >= size` with the pinned default `size = 100`; the ATR22/SMA10/RSI5 seeds (≈ 32 bars) all fall inside that floor. Coded behaviour underneath: TA-Lib seed windows print NaN until seeded and every strict comparison on NaN is false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market and no interval; venue spelling, symbol normalization, and the `1h` frame are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — entries open at the decision bar's own close; a completed bar breaching its side's stop level closes the full unit flat at that bar's close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced BbandRsi, AwesomeMacd, EMASkipPump, ADXMomentum, CMCWinner, ASDTSRockwell, MACDStrategy-state, MACDStrategy-crossed, and BinHV27 siblings use, and following the admitted `cci-ema-rsi-cross-trailing-stop-btcusdt-1h` precedent for a close-evaluated ratcheting trailing stop with same-bar-close execution. No maker-touch, queue, or intrabar-path-dependent fill: the source's marketable limit chase (`close ± 5` legacy futures points) and intrabar stop-market triggers are normalized to bar-close fills here, disclosed, never presented as the source engine's own timing. The Signal mutual-exclusion proof leaves no ambiguous same-bar fill order, and stop evaluation begins strictly after the entry bar, so no intrabar ordering assumption is needed.
- Interval precedent (disclosed, not assumed): `1h` is an already-admitted interval on `main` across many records — no novel-interval confirmation is required for this frame. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing beyond `fixed_size = 1`, no capital, fee, margin, or funding concept — the single-unit book is preserved verbatim while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add/no-reversal position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the expansion-gated RSI leg opens the full unit on a flat book; the side's trailing stop closes it in full; re-entry after an exit needs only the next qualifying flat-book bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (145 lines: the six parameter literals, the `50 ± 16` threshold arithmetic, the ATR-expansion gate, the flat-only two-sided entries, the hand-rolled 0.8% trailing-stop pair, and the `AtrRsiStrategy(CtaTemplate)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: TA-Lib seed NaNs compare false (no early entry, no early stop). The 100-bar record-rule floor restates the source's own `am.inited` gate with the pinned default size — disclosed, not repaired. The file ships no `startup_candle_count`, so the floor's number comes from the pinned utility default, never from elsewhere.
2. Exact-touch rule fenced: the regime gate and both RSI legs are strict while the stop triggers are inclusive — a bar with `atr == atrma` or `rsi == 66.0` (34.0) fires nothing on either side; a bar touching its stop level exactly exits. Strictness and inclusivity preserved throughout — disclosed, not smoothed.
3. Tick-plumbing fence: the `TickData` import, `on_tick`, and `bg.update_tick` aggregate ticks into completed bars and take no decision; `cancel_all` + `put_event` + `write_log` are order-maintenance/display plumbing with no gate effect. Zero `volume` reads in the decision path despite the bar container carrying a volume field.
4. Registry fence: the `parameters`/`variables` lists name file-literal attributes for vnpy's optimization/display registry — they define no search space and change no value used below. Zero hyperopt tokens, zero `*Parameter` spaces, zero fitted values anywhere in this artifact.
5. Limit-chase fence: the source's `close ± 5` order prices are legacy futures-point chase on marketable limit orders, meaningless in BTCUSDT decimals — normalized to same-bar-close market fills here, disclosed derivation, never silently kept.
6. Stop-timing fence: the source's stop-market orders trigger intrabar while this record evaluates the breach on the completed bar and exits at its close — a disclosed research simplification following the admitted FMZ ratchet-stop precedent, never presented as identical fill economics.
7. Cousin records fenced as different constructions (none trades a price-ATR-vs-own-average expansion gate conjunct with an RSI5 66/34 threshold pair and a sole 0.8% trailing-stop exit set, two-sided): the admitted `cci-ema-rsi-cross-trailing-stop` pool-mate trades a CCI-threshold gate plus a fast/slow RSI cross plus a slow-EMA price filter with a ratcheting close stop (different gate, different trigger, different book); the admitted `qqe-fast-slow-cross` / alorse-QQE pool-mates trade an ATR-of-RSI envelope (volatility of the oscillator itself, not of price) with band-cross triggers and no trailing stop; the admitted `bookstaber-atr-momentum-breakout` pool-mate trades ATR-scaled price breakouts (ATR as a ruler, not as its own gated regime); the admitted keltner / supertrend / turtle / dual-thrust families trade band-breakout entries with band-based or fixed stops (no RSI-threshold side selection, no ATR-self-average regime veto). Not a threshold re-tuning of any of them: moving any ATR/RSI length, the 16-entry offset, the 0.8% trail, adding any ROI/fixed-stop/time exit, or changing the frame or book would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: every other file in `vnpy_ctastrategy/strategies/` at the pinned commit is a separate pin — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT market choice, the `1h` frame choice, the same-bar-close market fills, the close-evaluated (rather than intrabar) stop triggers, the framework-default readings (per-completed-bar evaluation, flat pre-seed), and house sizing/costs — all predeclared above. The ATR22-vs-SMA10 expansion gate with all its literals, the RSI5 66/34 threshold pair with strictness, the flat-only entries, the 0.8% hand-rolled trailing-stop pair with the post-entry-bar start, the fixed single unit, and the two-sided stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: ATR(22)/SMA10 / RSI(5) / 66-34 thresholds with pinned strictness / expansion gate / flat-only entries / sole 0.8% trailing-stop pair / single-unit two-sided / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Regime-gate relevance: dropping the ATR-expansion gate (pure RSI5 66/34 threshold entries with the same trailing stops) must not improve net expectancy; fail ⇒ the volatility-expansion veto adds nothing over the oscillator alone.
- F2 — Oscillator relevance: dropping the RSI legs (pure ATR-expansion entries alternating by prior-book side, same trailing stops) must not improve net expectancy; fail ⇒ the 66/34 side selection adds nothing over the regime gate alone.
- F3 — Trailing-stop relevance: replacing the 0.8% trailing-stop pair with opposite-threshold exits (exit long when `rsi < 34`, exit short when `rsi > 66`, same entries) must not improve net expectancy; fail ⇒ the hand-rolled trailing ratchet adds nothing over a symmetric threshold exit.

## Crypto portability

BTCUSDT Binance perpetual `1h` is the research pin (source names no market and no interval). Two-sided with full-unit open/close expresses natively on a perpetual venue under the house Isolated overlay; the long-only subset expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. No volume field is consumed at all. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- The `1h` frame is researcher-declared (the source ships no interval) and rides existing admission precedent — no novel-interval confirmation burden attaches to this record, but no source-timeframe fidelity is claimed either (see Execution assumptions).
- Stop-fill economics are simplified: an intrabar breach that recovers by the close still exits at the close in this record, while a live stop-market would fill near the stop level intrabar; the direction and magnitude of the resulting bias depends on tape and is not signed here — disclosed, not repaired.
- A position in a trend that never pulls back 0.8% from its extremum is held indefinitely; a market that chops with hot ATR but mid-range RSI prints repeated flat-book no-ops with no decay, chop, trend-loss, or further time exit — disclosed, not repaired.
- TA-Lib indicator internals (Wilder ATR/RSI seeding, SMA arithmetic) live in libraries outside the pinned files — pinned by call with lengths 22/10/5, not re-derived; exact reproduction inherits those libraries' seeding alongside the 100-bar floor.
- The `load_bar(10)` history-feed depth is engine-feed configuration with no signal content — nothing further to fence.
- No ROI ladder, no fixed stop, no time exit, no pyramiding, no reversal, no cooldown — all explicitly absent, never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/vnpy/vnpy_ctastrategy/blob/7a8768de9784dda35a7b261a7ade1dbfbff50919/vnpy_ctastrategy/strategies/atr_rsi_strategy.py
- https://github.com/vnpy/vnpy_ctastrategy
