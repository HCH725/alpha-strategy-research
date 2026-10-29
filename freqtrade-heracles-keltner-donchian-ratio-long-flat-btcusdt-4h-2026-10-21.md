---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade Heracles Keltner-Donchian band-ratio state long-flat on BTCUSDT 4h bars
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
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/Heracles.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade Heracles Keltner-Donchian band-ratio state long-flat on BTCUSDT 4h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the same lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, `freqtrade-asdts-rockwell`, `freqtrade-macd-cci-dip-state`, `freqtrade-binhv27`, and `freqtrade-macd-cross-cci-edge` records — this is only its eleventh record, and the first pinned to this exact file).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/Heracles.py` (repository root-level strategies directory, NOT `berlinguyinca/` — author `@Mablue`, self-described "Strongest Son of GodStra").
- GitHub blob SHA at the pinned commit: `b4a6331b38fe5e9aec3f2ae6852e0dc917ec1d83`, size 3867 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 3867 bytes, 121 lines, SHA-256 `5b25d85297329243d7a3c65770975b5a70e52ec2684b1e007e5d8a3d1a7e3718`, identical to the GitHub blob (`git hash-object` reproduces `b4a6331b…917ec1d83`) — the entire file was retrieved and inspected.
- Registration: the file defines class `Heracles(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `user_data/strategies/GodStra.py` (parent work, different construction — no record pins it), `berlinguyinca/MACDStrategy.py`, `berlinguyinca/MACDStrategy_crossed.py`, `berlinguyinca/BinHV27.py`, and every other previously admitted sibling are different pins with different gates — this record pins ONLY the Heracles file's literals below, and no reviewer repair may substitute a sibling constant.
- The file's own words (quoted for gate evidence, never extended): `minimal_roi = { "0": 0.598, "644": 0.166, "3269": 0.115, "7289": 0 }` (keys are minutes); `stoploss = -0.256`; `timeframe = '4h'`; indicators `ta.volatility.keltner_channel_wband(high, low, close, window=20, window_atr=10, fillna=False, original_version=True)` into `volatility_kcw` and `ta.volatility.donchian_channel_pband(high, low, close, window=10, offset=0, fillna=False)` into `volatility_dcp` (the `ta` Python package, not TA-Lib — disclosed, never re-derived); entry `d = DFIND.shift(buy_indicator_shift).div(DFCRS.shift(buy_crossed_indicator_shift))` with `d.between(buy_div_min, buy_div_max)` (`enter_long = 1`); exit `dataframe.loc[:, 'exit_long'] = 0` (no exit signal, coded zero — the complete exit set is the ROI ladder plus the stop). No `trailing`, no `startup_candle_count`, no `use_exit_signal` / `exit_profit_only` override, no `can_short`, no `process_only_new_candles`, no order-type mapping ships anywhere — the framework defaults below are disclosed as defaults, never as file literals.
- Effective hyperopt constants (framework-resolved, fenced in Negative evidence 5): `buy_params = { "buy_crossed_indicator_shift": 9, "buy_div_max": 0.75, "buy_div_min": 0.16, "buy_indicator_shift": 15 }` — under Freqtrade semantics the `buy_params` dict values resolve each same-named space Parameter at load, so the effective gating literals are shifts 15/9 and band 0.16–0.75. The already-completed hyperopt that produced them is history, not a live fitting step: this record re-fits nothing and sweeps nothing.
- Out-of-file calls pinned (all resolved by name, all standard): `ta.volatility.keltner_channel_wband` / `ta.volatility.donchian_channel_pband` (closed-form channel-band columns on high/low/close with the literal windows above, `fillna=False` so leading windows print NaN — disclosed, never re-derived); `ta.utils.dropna` (drops rows containing any NaN — with complete exchange candles a leading-window trim only, fenced below); `Series.shift` (backward lags 15 and 9 — causal, never forward); `Series.div` (element-wise ratio); `Series.between` (pandas default inclusive-both bounds — inclusive 0.16/0.75, disclosed). No DB, no network, no `request.*`, no `security()`, no resample/interpolate/merge, no informative-pair call, no `DataProvider` read anywhere in the file.
- Full-file token census (verified over the 121 lines this cycle): 0 `short` (case-insensitive — no short leg, no short identifier anywhere); 0 `volume` (no volume read of any kind — both channel columns read high/low/close only; `dropna` trims on all columns but gates on none); 6 `shift` (two `buy_params` keys, two `IntParameter` declarations, two backward `Series.shift` uses — the only lookbacks in the gating path); 0 `trailing`; 0 `startup_candle_count` (the record's 60-bar floor is a predeclared researcher pin, never a file semantic); 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop); 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic); 0 `trailing` again for emphasis — none; 0 `resample` / 0 `informative` / 0 `merge` / 0 `request` / 0 `security` / 0 `get_pair_dataframe` / 0 `get_analyzed_dataframe`; 5 `Parameter` (one import line plus four space declarations); 3 `hyperopt` (three comment lines only — the loss line and two section headers, no live optimization); 3 `crossed` (the three `buy_crossed_indicator_shift` spellings, a name — not a cross edge); 0 `can_short` / 0 `use_exit_signal`. `reduce` is imported and never called — dead import, fenced as plumbing with no gate effect. The header backtest paste (`10/100: 25 trades ... 48.88Σ%`) ships no pair, window, or cost basis — adopted as nothing (see Negative evidence 6).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Freqtrade deployment. The source pins the `4h` frame, the Donchian-pband-over-Keltner-wband ratio state with all its literals, the ROI-only-plus-stop exit profile (no exit signal, coded), and the long-only stance — but ships no venue spelling, no fill-timing flag, no warmup guard, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market `BTCUSDT` (the file names no market; the `AgeFilter min_days_listed 100` pairlist comment is config advice, never a signal — venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed); (2) completed-bar decisions with same-bar-close market fills (the file's own framework contract evaluates per completed bar — derivation disclosed, never presented as the source engine's own timing); (3) single-unit position pin with hold-no-op semantics plus a 60-bar researcher warmup pin (the file carries no position reference and no length guard — disclosed, never presented as source-native behaviour); (4) the source's absent sizing/costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-21): working-tree filename/content search for `heracles` (case-insensitive) returns zero strategy records — no record in the pool cites this source file; blob `b4a6331b…` is unreferenced anywhere. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount) trades a channel-band-ratio state. Keltner/Donchian cousins in the pool are fenced as different constructions in Negative evidence 7. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: hold long exposure while the Donchian-10 position-band (15 bars ago) sits between 16% and 75% of the Keltner-20/10 bandwidth (9 bars ago) — a compression-relative position state that is true across whole regimes, not on a single crossing bar. There is no signal exit at all (`exit_long = 0`, coded): every position closes through the four-rung ROI ladder (`0.598` from open, `0.166` after 644 min, `0.115` after 3269 min, `0` after 7289 min — i.e. take whatever exists after ~5 days) or the fixed −25.6% stoploss. The file ships no usable performance basis — its header paste lacks pair, window, and costs — so this record adopts no source-reported performance (see Evidence).

### Research interpretation

Compression-relative camper, long-only. The Donchian pband leg measures where price sits inside its own 10-bar range (0 = range bottom, 1 = range top, lagged 15 bars); the Keltner wband leg measures absolute bandwidth as a fraction of price (lagged 9 bars). Their ratio is high when price presses a range extreme while bands are narrow, low when price hugs mid-range inside wide bands — the 0.16–0.75 acceptance band therefore vetoes both dead-flat tape (ratio pinned near zero as the numerator collapses) and violent expansion prints (ratio exploding past the ceiling), camping only in the middle regime where a range position coexists with breathable bandwidth. Because the state persists across bars, a positioned book treats further qualifying bars as hold-no-ops until an ROI rung or the stop releases it; a flat book simply waits for the next qualifying bar. The exit profile is deliberately signal-free — patience is enforced by the ladder, not by an oscillator release — so any scheme adding a signal exit would be a different, unpinned rule.

## Signal

Exact rule as pinned (any other channel window, ATR window, shift, band bound, inclusivity, state-vs-edge pairing, risk rung, fill, frame, or book is a different, unpinned rule). All identifiers below are the program's own; the `ta`-package call literals are file-verbatim:

```text
kcw[t] = ta.volatility.keltner_channel_wband(high, low, close, window=20, window_atr=10, fillna=False, original_version=True)[t]
dcp[t] = ta.volatility.donchian_channel_pband(high, low, close, window=10, offset=0, fillna=False)[t]
d[t]   = dcp[t-15] / kcw[t-9]          // backward shifts only; buy_params-resolved (see Provenance)
entry  = 0.16 <= d[t] <= 0.75          // enter_long = 1, persistent state (pandas between, inclusive both)
exit_sig = NONE (exit_long = 0, coded) // closes via risk legs only
risk   = ROI ladder {"0": 0.598, "644": 0.166, "3269": 0.115, "7289": 0} (fraction, by position age in minutes);
         fixed stop at -25.6% (stoploss -0.256)
floor  = leading-window bars: rolling NaN comparisons false; dropna trims leading-NaN rows (see Required data)
```

- Trade events: `enter_long=1` on every bar printing the in-band ratio state, `direction` long-only; no `exit_long` signal ever prints. A positioned book treats further qualifying bars as hold-no-ops under the position pin below; a flat book treats every non-qualifying bar as a no-op.
- Exact boundaries (pinned semantics): the acceptance band is inclusive on both ends (`Series.between` default) — a bar with `d == 0.16` or `d == 0.75` fires the entry leg; a bar with NaN `d` (leading window) fires nothing; a bar with infinite `d` (zero Keltner bandwidth divisor — perfectly flat tape) satisfies no bound and fires nothing under plain pandas comparison semantics, with no invented guard. All preserved throughout.
- Same-bar ambiguity: none exists to resolve — the file's only signal leg is the entry state and the exit leg is coded zero, so no tie-break pin is required and the reviewer is never asked to invent an ordering. Any bar co-printing the entry state with an ROI/stop release closes-or-opens the full unit flat-or-long deterministically under the single-unit pin (exit legs evaluated against the open position first — disclosed execution order, standard single-position semantics).
- Direction: long-only. Zero short-leg tokens ship anywhere, and the framework default `can_short = False` applies (disclosed default, never a file literal) — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the four-rung ROI ladder and the −25.6% stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply vacuously — no signal ever prints, so exits are ROI/stop only; disclosed defaults, never file literals). No trailing, no time exit beyond the `"7289": 0` rung (which closes at anything ≥ breakeven after ~5 days — coded fact, not a user time exit), no breakeven move — explicitly none further, not invented.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry-state bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats risk legs as no-ops; re-entry re-arms on any qualifying in-band bar after any close (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low`/`close` (two channel-band columns with fixed non-negative windows, plus fixed backward shifts 15/9 — no forward reference) with no `security()`, resample, interpolate, merge, or informative call anywhere in the gating path; the decision bar's own forming values are never read. No funding/OI/mark-price read, no `request.*`, no session/calendar call, no hyperopt parameter sweep at record time (the four constants are file-literal resolutions, never re-fit), and no stop/limit order argument anywhere in the gating path.

## Required data

- Completed `4h` bars of BTCUSDT: `high`/`low`/`close` only (both channel columns on `high`/`low`/`close`). No `open` read, no bar `volume` read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. (`dropna` trims rows on every column including `open`/`volume`, but trims nothing it gates on — with complete exchange candles the trim is a leading-window no-op, fenced in Negative evidence 4.) No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `4h` (source-native — the file prints `timeframe = '4h'`). One evaluation per completed bar; every window reads the decision bar's causal past only (plus the backward 15/9-bar shifts); fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 60 four-hour bars held flat (≈ 10 days). Covers the Keltner 20-bar window plus ATR-10 seeding, the Donchian 10-bar seed, and the 15-bar backward shift with margin. The file ships no `startup_candle_count` — quoted absence, never filled in from elsewhere. Coded behaviour underneath: `fillna=False` channel columns print NaN until seeded, `dropna` trims leading-NaN rows, and every NaN `between` comparison is false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; the `AgeFilter min_days_listed 100` pairlist comment is config advice for alt-coin rotation, never a signal leg — venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced BbandRsi, AwesomeMacd, EMASkipPump, ADXMomentum, CMCWinner, ASDTSRockwell, MACDStrategy-state, MACDStrategy-crossed-edge, and BinHV27 siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry-state evaluation, the ROI/stop legs are all bar-close-evaluated; with no exit signal in the file there is no signal-exit fill order to disambiguate, and any bar co-printing the entry state with an ROI/stop release resolves under the disclosed single-unit close-then-evaluate order.
- Interval precedent (disclosed, not assumed): `4h` is an already-admitted interval on `main` via the HLHB, MultiMA-TEMA-stack, and CCI-threshold-extreme-reversal records — no novel-interval confirmation is required for this frame. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI ladder and stop percentages are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the in-band state opens the full unit on a flat book; any ROI rung or the stop closes it in full; re-entry after a close needs only the next qualifying in-band bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (121 lines: the two `ta`-package channel calls with literal windows, the shift-ratio state with resolved constants, the `timeframe`/`minimal_roi`/`stoploss` literals, the coded-zero exit, and the `Heracles(IStrategy)` class pin). Its header comment pastes a result line (`25 trades ... 48.88Σ%`) with no pair, window, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: `fillna=False` channel columns print NaN until seeded, `dropna` trims leading-NaN rows, and every NaN `between` comparison is false (no early entry possible). The 60-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired. The file ships no `startup_candle_count`, so the floor is purely a researcher pin, never misattributed.
2. Exact-touch rule fenced: the acceptance band is inclusive on both ends under pandas `between` defaults — a bar with `d == 0.16` (0.75) satisfies the entry leg. A bar with infinite `d` (zero Keltner-bandwidth divisor on perfectly flat tape) satisfies neither bound under plain comparison semantics — coded fact, disclosed, with no invented zero-division guard. Strictness and inclusivity preserved throughout — disclosed, not smoothed.
3. Dead-import plumbing fenced: `reduce` is imported and never called anywhere in the 121 lines — display/plumbing leftover with no gate effect, never repaired into a signal. No live fitting step ships anywhere: the four gating constants are file-literal hyperopt resolutions, re-fit never.
4. `dropna` fence: `ta.utils.dropna(dataframe)` trims any row containing NaN across all columns (including `open`/`volume`, which no gating line reads) — with complete exchange candles only leading-window rows qualify, so the call is a causal leading trim, never a mid-sample hole-puncher and never a gate. No forward fill, no interpolation, no resample accompanies it.
5. Hyperopt-resolution fence: the `IntParameter`/`DecimalParameter` declarations print shadow defaults (`buy_indicator_shift` default 16) that the file's own `buy_params` dict overrides (15) under standard Freqtrade space-resolution semantics. Effective gating literals are the `buy_params` values (shifts 15/9, band 0.16–0.75) — resolved by stated framework rule, never chosen between, and the shadowed 16 must never be substituted by repair. A bar evaluated under default-16 would be a different, unpinned rule.
6. Header-paste fence: the `RESULT PASTE PLACE` comment (`25 trades. 18/4/3 ... Total profit 0.04888306 BTC ... Objective: -11.42103`) carries no pair, date window, stake, fee, or slippage basis — it is an unverifiable paste, adopted as zero performance evidence and never as a profitability claim. PASS here is engine expressibility only.
7. Cousin records fenced as different constructions (none trades a lagged Donchian-position-over-Keltner-bandwidth ratio state, ROI-and-stop-only exits, long-flat, on `4h`): the admitted `forven-keltner-adx-gated-breakout` pool-mate trades a Keltner-channel breakout gated by ADX regime on `1h` with signal exits (breakout, not ratio; different legs, exits, frame, risk); the admitted `bll-trb-200-percent-band` / `bll-vma-1-200-percent-band` pool-mates trade percent-band position states on `1d` two-sided (different bands, no ratio, no ROI ladder); the admitted `freqtrade-multima-tema-stack` pool-mate trades a TEMA-stack trend state on `4h` (moving-average stack, no channel ratio, different exits). Not a threshold re-tuning of any of them: moving any channel/ATR window, either shift, either band bound, the inclusivity, converting the state to an edge, adding any exit signal, or changing any ROI rung, the stop, or the frame would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `GodStra.py` (parent work) and every previously admitted Freqtrade-sourced record are separate pins — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT market choice, the same-bar-close fills, the single-unit/no-add/no-cooldown position pin, the 60-bar warmup floor (the file ships none), the framework-default readings (`can_short=False`, `use_exit_signal=True` applied vacuously, per-completed-bar evaluation), the `buy_params`-over-declaration resolution rule, the pandas `between`-inclusive and NaN/inf comparison semantics, and house sizing/costs — all predeclared above. The `4h` frame, the channel-call literals, the shift-ratio state with all its literals and inclusivity, the coded-zero exit with the four-rung ROI ladder and the −25.6% stop, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: Keltner(20, ATR 10, original)/Donchian(10) literals / shifts 15-and-9 / 0.16–0.75 inclusive band / persistent-state legs / signal-free exit profile / four-rung ROI ladder / −25.6% stop / single-unit long-only / `4h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Ratio relevance: replacing the ratio state with either leg alone (Donchian-pband band alone, or Keltner-bandwidth threshold alone, same risk) must not improve net expectancy; fail ⇒ the ratio adds nothing over its parts.
- F2 — Lag relevance: unlagging the state (same-bar `dcp/kcw` ratio, same band, same risk) must not improve net expectancy; fail ⇒ the 15/9-bar confirmation lags add nothing over the contemporaneous print.
- F3 — Risk-ladder relevance: removing the ROI ladder/stop pair is impossible without inventing an exit (the file codes zero signal exits) — so F3 instead neutralizes the ladder to a single `"0": 0` rung plus the pinned stop; that neutralized variant must not improve net expectancy; fail ⇒ the four-rung ladder adds nothing over a stop-only hold.

## Crypto portability

BTCUSDT Binance perpetual `4h` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. No volume field is consumed at all. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- The `4h` frame rides existing admission precedent (HLHB, MultiMA-TEMA-stack, CCI-threshold-extreme-reversal `4h`) — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- A position in a market whose ratio never leaves the band is held until an ROI rung or the −25.6% stop; a market that oscillates with the ratio stapled inside prints repeated hold-no-ops with no flat state to rest in, while a market that trends the ratio out-of-band idles flat with no chase leg. There is no decay, chop, trend-loss, or further time exit beyond the `"7289": 0` rung — disclosed, not repaired.
- The `ta`-package channel internals (Keltner ATR seeding, Donchian rolling extrema, `original_version` arithmetic) and the pandas `between`/`shift`/`div` semantics live in libraries outside the pinned file — pinned by call with the file's literal arguments, not re-derived; exact reproduction inherits those libraries' seeding alongside the 60-bar floor. The `ta` package version is unpinned in the file — disclosed, never filled in.
- The shadowed `IntParameter` default (16) and the `reduce` import are fenced leftovers — nothing further to fence.
- No signal exit, no trailing, no breakeven, no short leg, no cooldown — all explicitly absent, never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/Heracles.py
- https://github.com/freqtrade/freqtrade-strategies
