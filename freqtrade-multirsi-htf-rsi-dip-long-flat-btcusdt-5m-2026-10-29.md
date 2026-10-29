---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade MultiRSI HTF-RSI dip long-flat on BTCUSDT 5m bars
created: 2026-10-29
updated: 2026-10-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/MultiRSI.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade MultiRSI HTF-RSI dip long-flat on BTCUSDT 5m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the same lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, `freqtrade-asdts-rockwell`, `freqtrade-macd-cci-dip-state`, `freqtrade-macd-cross-cci-edge`, and `freqtrade-binhv27` records — this is only its eleventh record, and the first pinned to this exact file).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/berlinguyinca/MultiRSI.py`.
- GitHub blob SHA at the pinned commit: `0ddcb5b6b7f7bf925d6b363d5a90fe446de64fd7`, size 2326 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 2326 bytes, 71 newline-terminated lines, SHA-256 `0bd453350bdf32db4355277d79a3c7268d166d043bab59e30403a1e97687aa06`, identical to the GitHub blob (`git hash-object` reproduces `0ddcb5b6…d7`) — the entire file was retrieved and inspected.
- Registration: the file defines class `MultiRSI(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, every other `user_data/strategies/berlinguyinca/*.py` sibling is a different pin with different constants — this record pins ONLY the MultiRSI literals below, and no reviewer repair may substitute a sibling constant.
- The file's own words (quoted for gate evidence, never extended): `timeframe = '5m'`; `minimal_roi = { "0": 0.01 }`; `stoploss = -0.05`; `get_ticker_indicator()` returns `int(self.timeframe[:-1])` (i.e. `5`); indicators `sma5 = ta.SMA(timeperiod=5)`, `sma200 = ta.SMA(timeperiod=200)`, short frame `resample_to_interval(... * 2)` (= 10 minutes) with `ta.RSI(timeperiod=14)`, long frame `resample_to_interval(... * 8)` (= 40 minutes) with `ta.RSI(timeperiod=14)`, base `ta.RSI(dataframe)` (default period), both merges via `resampled_merge`, then `dataframe.ffill(inplace=True)`; entry `(sma5 >= sma200) & (rsi < resample_40_rsi - 20)` (`enter_long = 1`); exit `(rsi > resample_10_rsi) & (rsi > resample_40_rsi)` (`exit_long = 1`). No `trailing`, no `startup_candle_count`, no `use_exit_signal` / `exit_profit_only` override, no `can_short`, no `process_only_new_candles`, no order-type mapping ships anywhere — the framework defaults below are disclosed as defaults, never as file literals.
- Out-of-file calls pinned (all resolved by name, all standard): `ta.SMA` (TA-Lib SMA on close, periods 5 and 200 — file literals); `ta.RSI` (TA-Lib Wilder RSI on close, period 14 explicit on both resampled frames, library-default 14 on the base frame — disclosed, never overridden); `resample_to_interval` / `resampled_merge` from `technical.util` (epoch-aligned label-left bins, `date_merge = date + resampled_int − original_int` alignment, left-merge plus forward-fill — independently verified against the library source this cycle; the library docstring directs callers to `resampled_merge` specifically "to avoid lookahead bias"). No DB, no network, no `request.*`, no `security()`, no interpolate, no hyperopt parameter (`IntParameter`/`BooleanParameter`/`CategoricalParameter`/`DecimalParameter` zero hits), no informative-pair call, no volume read in the file.
- Full-file token census (verified over the 71 lines this cycle): 0 `buy` / 0 `sell` (new-interface `enter_long`/`exit_long` only); 0 `volume` (no volume read of any kind — SMAs and RSIs read close only); 0 `shift` (no lag call in the file body); 0 `crossed` (no edge legs — every leg is a persistent level comparison, disclosed); 0 `hyperopt` / 0 `Parameter`; 3 `short` — all three are the identifier `dataframe_short` (the 10-minute resampled-frame plumbing), zero short legs and zero short identifiers beyond that name; 1 `minimal_roi` ladder (single `0.01` rung) and 1 `stoploss` (`-0.05`) as the only risk legs; 0 shipped `trailing`; 0 `startup_candle_count` (the record's 200-bar floor is a predeclared researcher pin, never a file semantic); 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond the ROI rung and stop); 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Freqtrade deployment. The source pins the `5m` frame, the SMA-regime gate, the resampled-RSI dip entry, the dual-superiority RSI exit, the single 1% ROI rung, the −5% stop, and the long-only stance — but ships no venue spelling, no fill-timing flag, no warmup guard, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market `BTCUSDT` (the file names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed); (2) completed-bar decisions with same-bar-close market fills (the file's own framework contract evaluates per completed bar — derivation disclosed, never presented as the source engine's own timing); (3) single-unit position pin with hold-no-op semantics plus a 200-bar researcher warmup pin (the file carries no position reference and no length guard — disclosed, never presented as source-native behaviour); (4) the source's absent sizing/costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-29): working-tree filename/content search for `multirsi` (case-insensitive) returns only sibling-fence mentions (`freqtrade-technical-cmf-sign-state` names `berlinguyinca/Scalp.py`-style separate pins including this file; two records cite closed PR #539 in their closed-PR scans) — no record in the pool cites, pins, or trades this source file. Content search for `resample_40` returns zero records — no pool record reads a 40-minute resampled RSI. No open `research/*` PR (#593 Vinicius Supertrend, #353 Heracles KCD, #350 ClucMay72018, #331 AdxSmas, #304 Forven CCI, #251 Swift 2YMA, #92 SSL channel, #89 Chandelier Exit, #63 SuperTrend flip, #49 Gauss StochRSI, #48 Larry Williams streak) trades a resampled-RSI spread system. Closed Scout PR #539 (`MultiRSI HTF spread`, same source file, closed 2026-10-27 NOT_LOSSLESS for two HTF-mapping contradictions — RSI-then-hold versus hold-then-RSI, and at/before versus strictly-before boundary reads) is fenced as a different derived identity in Negative evidence 8: this record re-declares the mapping with ONE consistent rule used everywhere (each HTF close advances the RSI state exactly once; the visible value is always the latest HTF block ending at-or-before the decision-bar close), never a reopen of that head. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: on `5m` bars, buy when the fast SMA sits at/above the slow SMA while the base-frame RSI14 sits more than 20 points under the 40-minute RSI14 (stacked-MA regime plus slower-horizon-relative washout); sell when the base RSI14 recovers above BOTH the 10-minute and the 40-minute RSI14 (short-horizon tone reclaims both slower tones). A single 1% ROI rung and a fixed −5% stoploss backstop every position. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Regime-gated relative-washout machine, long-only. The SMA leg supplies the regime veto (no dip-buying into a stacked-downtrend tape), while the 20-point RSI spread supplies the timing (the fast tone must be deeply washed out *relative to the slow tone*, not merely low in absolute terms — so a bar with RSI 25 against a 40m RSI of 30 prints nothing, and a bar with RSI 45 against a 40m RSI of 70 prints the entry). The exit is deliberately slower than the entry: the fast tone must reclaim both slower tones, so a V-bounce that only clears the 10m RSI keeps the book positioned. Unlike one-bar-edge records (each leg fires at most on its crossing bar), every leg here is a persistent state — a book already positioned treats entry-state bars as hold-no-ops until a qualifying exit state, the ROI rung, or the stop. A scheme that exits on either RSI leg alone, or on an absolute RSI threshold, would be a different, unpinned rule.

## Signal

Exact rule as pinned (any other SMA/RSI periods, spread constant, edge-vs-state pairing, risk rung, fill, frame, or book is a different, unpinned rule). All identifiers below are the program's own; the column names `resample_10_rsi` / `resample_40_rsi` are the merge's own naming (`resample_<minutes>_<column>`).

```text
sma5[t]   = SMA(close, 5) on completed 5m closes
sma200[t] = SMA(close, 200) on completed 5m closes
rsi5[t]   = TA-Lib Wilder RSI14 over completed 5m closes
rsi10[t]  = TA-Lib Wilder RSI14 over 10m block closes, each block advancing state once (HTF rule below)
rsi40[t]  = TA-Lib Wilder RSI14 over 40m block closes, each block advancing state once (HTF rule below)
entry = (sma5[t] >= sma200[t]) AND (rsi5[t] < rsi40[t] - 20)   // enter_long = 1, persistent state
exit_sig = (rsi5[t] > rsi10[t]) AND (rsi5[t] > rsi40[t])       // exit_long = 1, persistent state
risk = single take-profit rung {"0": 0.01} (1% from the entry minute, bar-close-evaluated);
       fixed stop at -5% (stoploss -0.05, bar-close-evaluated)
floor = leading-window bars: rolling NaN comparisons false (see Required data)
```

- THE single HTF mapping rule (used identically in Signal, Required data, Execution assumptions, and Falsification — there is no second rule): 10m blocks are `[T, T+10min)` and 40m blocks are `[T, T+40min)` on UTC-epoch-aligned boundaries, built from completed `5m` bars of the same feed; each block close advances that frame's RSI14 state exactly once (RSI-then-hold — the RSI is computed over the block-close series and the resulting value is held forward, never recomputed over repeated 5m closes); the value visible on a completed `5m` decision bar closing at time `c` is always the RSI of the latest block with block-end `<= c` ("at-or-before", inclusive of a block completing exactly at `c`). This reproduces the source file's `resample_to_interval` (label-left bins) + `resample_to_interval`-then-RSI + `resampled_merge` (`date_merge = date + K − 5`, left-merge, forward-fill) construction: under that construction a `K`-minute bin first joins the `5m` bar closing exactly when the bin completes, and older bars carry the held value — point-in-time on every bar, no forward reference. The reverse ordering (holding 5m closes then computing RSI) is NOT equivalent and is NOT this record: it would be a different, unpinned rule.
- Trade events: `enter_long=1` on any bar printing the two-conjunct entry state, `direction` long-only; `exit_long=1` on any bar printing the dual-superiority exit state. Both legs are persistent states, not one-bar edges — a book already positioned treats further entry-state bars as hold-no-ops under the position pin below.
- Exact boundaries (pinned semantics): the SMA comparison is inclusive (`>=` — an exact touch fires the regime leg); all four RSI comparisons are strict (`<`, `>` — `rsi5` exactly 20 points under `rsi40` fires nothing; `rsi5` exactly equal to either HTF RSI fires neither exit leg). All preserved throughout.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `rsi5 < rsi40 − 20`, hence `rsi5 < rsi40`, while any signal-exit bar has `rsi5 > rsi40` — arithmetically exclusive on every bar, degenerate or otherwise, so entry and signal-exit never co-print. ROI/stop cannot co-fire with entry on the entry bar either (zero distance at the fill). The reviewer is never asked to invent an ordering.
- Direction: long-only. The 3 `short`-substring tokens are all the plumbing identifier `dataframe_short` (the 10-minute resampled frame) — zero short legs ship anywhere, and the framework default `can_short = False` applies (disclosed default, never a file literal) — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the dual-superiority signal exit, the single 1% ROI rung, and the −5% stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — exits fire even at a loss; disclosed defaults, never file literals). The rung reads Freqtrade-native: `{"0": 0.01}` demands 1% from the entry minute, bar-close-evaluated under the derived timing. No trailing, no time exit, no breakeven move — explicitly none further, not invented.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry-state bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying entry-state bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `close` (SMAs, all three RSIs, and both block-close series — fixed non-negative offsets, no forward reference) under the file's own framework contract (`process_only_new_candles` default true — disclosed default, never a file literal); the decision bar's own forming values are never read. No volume, funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `5m` bars of BTCUSDT: `close` only (SMAs on `close`; all three RSIs on `close` / block closes). No `open`, `high`, `low` read, no bar `volume` read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol or external-feed dependency of any kind.
- Single decision timeframe `5m` (source-native — the file prints `timeframe = '5m'`). One evaluation per completed bar; the 10m/40m block series are deterministic epoch-aligned aggregations of the same `5m` feed (see the single HTF mapping rule in Signal — same-feed arithmetic, never a second feed or subscription); every window reads the decision bar's causal past only; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 200 completed five-minute bars held flat. Covers the SMA200 seed, the RSI14-over-40m-block seed (15 blocks × 40 min = 600 min = 120 `5m` bars), and the merge forward-fill seed with margin. The file ships no `startup_candle_count` — quoted absence, never filled in from elsewhere. Coded behaviour underneath: rolling windows print NaN until seeded, `ffill` never fills leading NaN, and every strict/inclusive NaN comparison is false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced BbandRsi, AwesomeMacd, EMASkipPump, ADXMomentum, CMCWinner, ASDTSRockwell, MACDStrategy-state, MACDStrategy-crossed-edge, and BinHV27 siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, the dual-superiority signal exit, and the ROI/stop legs are all bar-close-evaluated; the Signal mutual-exclusion proof leaves no ambiguous same-bar signal fill order, and any bar co-printing a signal exit with an ROI/stop leg closes the full unit flat either way, so no intrabar ordering assumption is needed.
- Interval precedent (disclosed, not assumed): `5m` is an already-admitted interval on `main` via the EMASkipPump, CombinedBinHAndCluc, ASDTSRockwell, MACDStrategy-state, MACDStrategy-crossed-edge, and BinHV27 records — no novel-interval confirmation is required for this frame. The 10m/40m block arithmetic needs no second feed: it is epoch-aligned aggregation of the same admitted `5m` feed under the single HTF mapping rule. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI rung and stop percentages are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the entry state opens the full unit on a flat book; the dual-superiority signal exit, the ROI rung, or the stop closes it in full; re-entry after an exit needs only the next qualifying entry-state bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (71 lines: the SMA/RSI indicator block, the two resampled-RSI frames with their merges, the two-conjunct entry state, the dual-superiority exit state, the `timeframe`/`minimal_roi`/`stoploss` literals, and the `MultiRSI(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: rolling NaNs compare false and `ffill` never fills leading NaN (no early entry, no early exit). The 200-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired. The file ships no `startup_candle_count`, so the floor is purely a researcher pin, never misattributed.
2. Exact-touch rule fenced: the SMA leg is inclusive (`>=`) while all four RSI legs are strict (`<`/`>`) — a bar with `sma5 == sma200` satisfies the regime leg; a bar with `rsi5` exactly 20 points under `rsi40`, or exactly equal to either HTF RSI, satisfies nothing on the spread legs. Strictness and inclusivity preserved throughout — disclosed, not smoothed.
3. Ordering fence (the #539 lesson, built into this record, never blurred): RSI-then-hold is the ONLY ordering here. Hold-then-RSI (repeating each HTF close across its 5m bars before computing RSI) is arithmetically a different series and would print different trade events — it is a different, unpinned rule, explicitly excluded, not silently available as a reviewer repair.
4. Boundary-read fence (the second #539 lesson, built into this record): "latest block with block-end `<=` decision-bar close" is the ONLY availability read. A "strictly before" read (which would hold the previous block on every HTF-boundary bar) would print different trade events — it is a different, unpinned rule, explicitly excluded, not silently available as a reviewer repair.
5. Prose-vs-code fence: the entry comment `# must be bearish` is prose — the coded leg requires `sma5 >= sma200` (a stacked, non-bearish regime filter), so a below-stack bar never fires entry regardless of the spread. Coded legs govern; prose never narrows or widens them.
6. Dead-plumbing fence: `get_ticker_indicator` is a pure `int('5m'[:-1])` helper (returns `5`; the `* 2` / `* 8` factors are the 10m/40m frames, verified arithmetic, never tuned); `dataframe_short` / `dataframe_long` are frame plumbing names with no order meaning. Zero hyperopt tokens, zero `*Parameter` spaces, zero fitted values anywhere in this artifact.
7. Cousin records fenced as different constructions (none trades a cross-timeframe RSI-spread state with an SMA-regime gate, long-flat, on any frame): the admitted `freqtrade-cofibit-stochf-ema-rail-adx-gated` pool-mate trades a single-frame STOCHF-cross plus EMA-rail plus ADX state (edge legs, oscillator cross, rail exits — never a cross-timeframe RSI spread); the admitted `freqtrade-strategy004-adx-cci-dual-stoch-recross` pool-mate trades ADX/CCI/dual-stochastic recross edges (different oscillators, edge construction); the admitted `freqtrade-swinghightosky-cci-rsi-dual-threshold` pool-mate trades single-frame CCI+RSI dual thresholds (absolute thresholds, never a relative cross-frame spread); the admitted `rsi-classic-level-reversal`, `rsi-ma-crossover-reversal`, `rsi-sma-gated-cross-reversal`, and `cumulative-rsi-dual-threshold` pool-mates trade single-frame absolute RSI levels/crosses (never HTF-relative). Not a threshold re-tuning of any of them: moving any SMA/RSI period, the spread constant, either strictness, or changing any ROI/stop literal, the frame, or the hold-vs-recompute ordering would each be a different, unpinned rule — none is admitted here.
8. Closed-PR fence: closed Scout PR #539 (`freqtrade-multirsi-triple-rsi-spread-long-flat-btcusdt-5m-2026-10-28.md`, same source file, closed 2026-10-27 NOT_LOSSLESS) is a different derived identity — its head carried two contradictory HTF mappings and is not reopened here; this record's single consistent HTF rule (each HTF close advances RSI state exactly once; latest block ending at-or-before the decision close, everywhere) is the precise remediation of that closure's stated blockers. Sibling files `MACDStrategy.py`, `MACDStrategy_crossed.py`, `ADXMomentum.py`, `AdxSmas.py`, `ASDTSRockwellTrading.py`, `AwesomeMacd.py`, `BbandRsi.py`, `CombinedBinHAndCluc.py`, `EMASkipPump.py`, `CMCWinner.py`, `ClucMay72018.py`, `Scalp.py`, `CCIStrategy.py`, `Low_BB.py`, `MultiRSI.py`-as-any-other-pin, `SmoothOperator.py`, `TechnicalExampleStrategy.py`, and every other file in the collection are separate pins — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT market choice, the same-bar-close fills, the single-unit/no-add/no-cooldown position pin, the 200-bar warmup floor (the file ships none), the framework-default readings (`can_short=False`, `use_exit_signal=True`, `exit_profit_only=False`, per-completed-bar evaluation), the TA-Lib default-period reading (base RSI 14 — library default, never a file literal), the verified `resampled_merge` alignment semantics, and house sizing/costs — all predeclared above. The `5m` frame, the SMA-regime gate with all its literals and strictness, the resampled-RSI dip entry, the dual-superiority exit, the single 1% ROI rung with the −5% stop, the RSI-then-hold ordering, the at-or-before boundary read, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: SMA(5/200) with inclusive gate / RSI14 on all three frames / 20-point spread with pinned strictness / persistent-state legs / dual-superiority exit / single 1% ROI rung / −5% stop / single-unit long-only / `5m` BTCUSDT / same-bar-close fills / RSI-then-hold ordering / at-or-before boundary read are frozen.

- F1 — Regime-gate relevance: dropping the SMA legs (naked RSI-spread state, same risk) must not improve net expectancy; fail ⇒ the stacked-MA veto adds nothing over the spread alone.
- F2 — Spread relevance: replacing the 20-point cross-frame spread with a fixed absolute entry threshold (same exit, same risk) must not improve net expectancy; fail ⇒ the HTF-relative construction adds nothing over a single-frame level.
- F3 — Risk-leg relevance: removing the ROI rung/stop pair (signal-only exits) must not improve net expectancy; fail ⇒ the 1% rung plus −5% backstop adds nothing over the bare state machine.

## Crypto portability

BTCUSDT Binance perpetual `5m` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar/block count on the decision frame, portable across 24/7 crypto tape. No volume field is consumed at all. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- The `5m` frame rides existing admission precedent (EMASkipPump, CombinedBinHAndCluc, ASDTSRockwell, MACDStrategy-state, MACDStrategy-crossed-edge, BinHV27 `5m`) — no novel-interval confirmation burden attaches to this frame (see Execution assumptions). The 10m/40m block arithmetic rides the same admitted feed, never a second feed.
- A position in a market whose fast RSI never reclaims both HTF RSIs is held until the 1% rung or the −5% stop; a market pinned in the entry spread with the regime gate holding prints repeated hold-no-ops with no flat state to rest in (persistent-state profile, disclosed). There is no decay, chop, trend-loss, or further time exit — disclosed, not repaired.
- TA-Lib indicator internals (SMA/RSI seeding, Wilder smoothing) and the `technical.util` resample/merge helpers live in libraries outside the pinned file — pinned by call with explicit periods 5/200/14 and verified merge alignment, not re-derived; exact reproduction inherits those libraries' seeding alongside the 200-bar floor. Epoch alignment of the 10m/40m blocks to UTC 5-minute boundaries is a disclosed derivation assumption matching both the library's epoch-origin bins and exchange-bar alignment.
- No trailing, no breakeven, no short leg, no cooldown — all explicitly absent, never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/MultiRSI.py
- https://github.com/freqtrade/freqtrade-strategies
