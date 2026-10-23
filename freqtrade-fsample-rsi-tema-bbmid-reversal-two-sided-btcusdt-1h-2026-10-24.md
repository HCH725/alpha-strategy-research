---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade FSample RSI-cross TEMA-BBmid mirrored reversal two-sided on BTCUSDT 1h bars
created: 2026-10-24
updated: 2026-10-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/futures/FSampleStrategy.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade FSample RSI-cross TEMA-BBmid mirrored reversal two-sided on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the same lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, `freqtrade-asdts-rockwell`, `freqtrade-macd-cci-dip-state`, `freqtrade-binhv27`, `freqtrade-macd-cross-cci-edge`, `freqtrade-strategy005`, `freqtrade-quickie`, and `td-sequential-setup9-perfected` records — this is only its next record, and the first pinned to this exact file).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/futures/FSampleStrategy.py` (the perpetual-futures sample folder; its sibling `Readme.md` documents the folder's test config as Binance futures, `trading_mode: futures`, `margin_mode: isolated`, USDT stake — source-side venue fit, never the rule).
- GitHub blob SHA at the pinned commit: `cb55a9253473697fb7ccb71c8a8fe3454929cd92`, size 5413 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 5413 bytes, 162 lines, SHA-256 `3fcbe2ed16dd097fd6e4548172acbde871bdfe64c5a7341f337f19caf3daa225`, identical to the GitHub blob (`git hash-object` reproduces `cb55a925…4929cd92`) — the entire file was retrieved and inspected. Plain LF endings, no BOM.
- Registration: the file defines class `FSampleStrategy(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique.
- The file's own words (quoted for gate evidence, never extended): `timeframe = "1h"`; `minimal_roi = {"0": 1}`; `stoploss = -0.05`; `can_short = True`; `trailing_stop = False`; `process_only_new_candles = True`; `startup_candle_count: int = 30`; long leg `crossed_above(rsi, 30)` with `tema <= bb_middleband`, `tema > tema.shift(1)`, `volume > 0` (`enter_long = 1`); short leg `crossed_above(rsi, 70)` with `tema > bb_middleband`, `tema < tema.shift(1)`, `volume > 0` (`enter_short = 1`); long exit repeats the short-entry conjunction verbatim (`exit_long = 1`); short exit repeats the long-entry conjunction verbatim (`exit_short = 1`). The commented-out ladder `# minimal_roi = {"60": 0.1, "30": 0.2, "0": 0.2}` is a comment — the coded `{"0": 1}` governs, never the comment. No `use_exit_signal` / `exit_profit_only` / `ignore_roi_if_entry_signal` override, no `order_types`, no `order_time_in_force`, no `position_adjustment`, no `max_open_trades`, no `leverage`, no `funding`, no `mark_price` ships anywhere — the framework defaults below are disclosed as defaults, never as file literals.
- Indicator block (only four columns feed any leg): `ta.RSI(dataframe)` (no literal — TA-Lib default period 14, deterministic library default, disclosed, never tuned; the Quickie record passed on the same default-period basis for its MACD/ADX legs); `ta.TEMA(dataframe, timeperiod=9)` (explicit 9); `qtpylib.bollinger_bands(typical_price, window=20, stds=2)` (explicit 20/2 on typical price `(high+low+close)/3`); bar `volume`. Dead columns computed but never read by any leg: `adx`, `fastd`/`fastk`, `macd`/`macdsignal`/`macdhist`, `mfi`, `bb_lowerband`/`bb_upperband`/`bb_percent`/`bb_width`, `sar`, `htsine`/`htleadsine` — fenced, never inputs. `BooleanParameter`/`CategoricalParameter`/`DecimalParameter`/`IntParameter` are imported and never instantiated (zero `Parameter(` hits — dead template imports, no tuning scaffolding, every leg constant is a frozen literal).
- Full-file token census (verified over the 162 lines this cycle): 3 `short` (the `can_short` attribute plus the `enter_short`/`exit_short` legs — the complete two-sided stance, no hidden side); 0 `.value` (no hyperopt value read anywhere); 0 `resample` / 0 `informative` / 0 `request` / 0 `security(` (single-frame, no external feed); 0 `position_adjust` / 0 `max_open_trades` / 0 `cooldown` / 0 `pyramid` (the position pin below is a predeclared researcher rule, never a file semantic); 0 `order_types` / 0 `order_time_in_force` / 0 `leverage` / 0 `funding` / 0 `mark_price` (no economics beyond ROI/stop); 0 `trailing` beyond the single `trailing_stop = False` literal (the commented positive/offset pair is present-but-disabled, never to be enabled by repair); 0 `use_exit_signal` / 0 `exit_profit_only` (framework defaults disclosed below); 0 `fillna` / 0 `ffill` / 0 `interpolate` / 0 `dropna` (no NaN patching — strict NaN comparisons stay false); 0 negative `shift(-` (every offset is a causal non-negative lag — `shift(1)` inside the slope guards and the one-bar `crossed_above` offset only); 2 `crossed_above` (the two RSI edges — the only edge primitives); 1 `startup_candle_count` (the source-native 30-bar floor). `numpy`/`pandas` noqa imports are plumbing with no gate effect.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Freqtrade deployment. The source pins the `1h` frame, the RSI(14-default) cross-30/long and cross-70/short edges, the TEMA(9)-vs-BBmid(20, typical-price) side guards with strict slope guards, the volume-positive gate, the mirrored exits, the inert 100% ROI rung, the −5% stop, the disabled trailer, the two-sided stance, the per-completed-bar evaluation, and the 30-bar startup floor — but ships no venue spelling, no fill-timing flag, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market `BTCUSDT` Binance perpetual (the file names no market; the futures-folder test config is isolated-margin USDT-M fit, but no source-market equivalence is claimed); (2) completed-bar decisions with same-bar-close market fills (the file's own `process_only_new_candles` contract evaluates per completed bar — derivation disclosed, never presented as the source engine's own timing); (3) single-unit position pin with hold-no-op semantics (the file carries no position reference — disclosed, never presented as source-native behaviour); (4) the source's absent sizing/costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding per the baseline §4 rule; no hypothetical zero funding claimed — the source declares no funding treatment at all), with no safety-order/add tranche activating under the single-unit/no-add pin (see Execution assumptions). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-24): working-tree filename/content search for `fsample` returns zero strategy records — no record in the pool cites this source file. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian band-ratio) trades an RSI-cross/TEMA-BBmid mirrored rule. TEMA-BBmid cousins are fenced as different constructions in Negative evidence 7. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: ride long when RSI crosses up through 30 while TEMA(9) sits at-or-below the BB(20) midline and is rising; ride short when RSI crosses up through 70 while TEMA sits above the midline and is falling; each side exits exactly when the opponent's entry prints. A +100% ROI rung (`1` from open — coded but economically inert, fenced below) and a fixed −5% stoploss backstop every position. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Oversold/overbought snap-back reversal machine, two-sided and symmetric. The RSI edge timestamps the momentum turn (cross up through 30 = leaving oversold; cross up through 70 = pushing into overbought — note both edges are upward crosses, the side comes from the TEMA regime guard, not the cross direction), while the TEMA-vs-BBmid plus strict slope guards locate the price regime (below-mid-and-rising for longs, above-mid-and-falling for shorts) and the volume gate excludes zero-print bars. Because each side's exit IS the opponent's entry, the book is always either long, short, or transitioning — a flat book only persists while no edge prints. The −5% stop (far below any single-bar 1h noise the guards already filter) stands as a disaster backstop that almost never binds before a mirrored exit in ordinary tape. The failure mode is plain: an RSI that chops across 30/70 while TEMA straddles the midline whipsaws the book side-to-side with no cooldown, and a trend that keeps extending after entry holds the unit all the way to the stop — no time exit exists.

## Signal

Exact rule as pinned (any other RSI period, threshold, TEMA/BB lookback, slope strictness, edge-vs-state pairing, risk rung, fill, frame, or book is a different, unpinned rule). RSI 14 is the deterministic TA-Lib default, never a tuned choice:

```text
rsi[t]   = TA-Lib RSI(close, 14)              // default period, causal
tema[t]  = TA-Lib TEMA(close, 9)              // explicit 9, causal
bb_mid[t]= SMA(typical_price, 20)             // typical=(h+l+c)/3, causal
enter_long  = crossed_above(rsi,30)[t] & (tema[t] <= bb_mid[t])
              & (tema[t] > tema[t-1]) & (volume[t] > 0)     // edge, strict slope
enter_short = crossed_above(rsi,70)[t] & (tema[t] > bb_mid[t])
              & (tema[t] < tema[t-1]) & (volume[t] > 0)     // edge, strict slope
exit_long   = <identical to enter_short conjunction>
exit_short  = <identical to enter_long conjunction>
risk = ROI {"0": 1} (+100%, coded but inert — never binds, fenced);
       fixed stop at -5% (stoploss -0.05, same price-distance basis)
floor = source-native startup_candle_count = 30 completed 1h bars held flat
```

- Trade events: `enter_long`/`enter_short` are one-bar edges (`crossed_above` = true only on the crossing bar); the side guards are persistent states. A flat book opens the full unit on an edge bar; a positioned book treats same-side edges as hold-no-ops under the position pin below.
- Exact boundaries (pinned semantics): both RSI comparisons are upward-cross edges — a bar with `rsi == 30`/`70` exactly satisfies no edge unless the cross arithmetic holds; the long guard admits equality (`tema <= bb_mid`) while the short guard is strict (`tema > bb_mid`) — equality belongs to the long side only, coded, never a researcher tie-break. Both slope guards are strict — a flat TEMA (`tema[t] == tema[t-1]`) satisfies neither side. The volume gate is strict (`> 0`) — zero-volume bars deterministically print no edge. NaN comparisons/edges are false — leading-window bars print neither leg. All preserved throughout.
- Mutual-exclusion proof (no tie-break pin required): long-entry and short-entry never co-print — they require `tema[t] <= bb_mid[t]` versus `tema[t] > bb_mid[t]` (mutually exclusive on every bar including equality) AND rising versus falling TEMA (mutually exclusive under strictness). The RSI legs alone could theoretically co-fire only on a single-bar RSI leap from ≤30 to >70, but the TEMA guards already exclude the bar. Same-side entry and signal-exit never co-print (identical exclusion — the long exit IS the short-entry conjunction). Opponent entry/exit pairs are the identical conjunction by code: on such a bar a flat book enters (the exit leg needs a position and is a no-op without one — no same-bar round-trip), while a book holding that side exits in full. ROI/stop cannot co-fire with entry on the entry bar (zero distance at the fill). The reviewer is never asked to invent an ordering.
- Direction: two-sided explicit (`can_short = True` file literal plus coded `enter_short`/`exit_short` legs). BTCUSDT Binance perpetual is a realistic, declared research market — and the file lives in the collection's futures folder whose test config is Binance futures isolated-margin USDT-M (source-side fit, disclosed).
- Exits and risk (explicit): the mirrored signal exits, the inert +100% ROI rung, and the −5% stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — exits fire even at a loss; disclosed defaults, never file literals). The ROI rung at +100% is coded but economically inert (no 1h bar doubles from entry — disclosed as inert, exactly as the admitted TD-Sequential record fences its +500% rung, never as a live profit-taking leg); with the rung never binding, no intrabar-vs-close ROI sequencing question can arise. The −5% stop is a fraction of entry-price distance (close-to-close price return), evaluated bar-to-bar at closes — this basis is leverage-invariant, so downstream leverage/margin accounting cannot alter any exit event (see Execution assumptions for the liquidation fence). No trailing (`trailing_stop = False` file literal — the commented positive/offset pair is present-but-disabled, never to be enabled by repair), no time exit, no breakeven move — explicitly none further, not invented. No exit leg reads net profit, fees, or funding — fees change only the performance report, never whether an exit fires (disclosed).
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats same-side edge bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats exit-only bars as no-ops; re-entry re-arms on the next qualifying edge after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule (the source-native 30-bar floor governs seeding).
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low`/`close`/`volume` (typical-price BB plus two rolling windows and one-bar offsets with fixed non-negative lags — no forward reference) under the file's own framework contract (`process_only_new_candles = True` file literal — one evaluation per completed bar); the decision bar's own forming values are never read. No funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt value, or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `1h` bars of BTCUSDT: `high`/`low`/`close` (typical-price BB, TEMA, RSI construction) plus bar `volume` (strict-positive gate only — no volume threshold leg, no volume-weighted normalization). No `open` read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1h` (source-native — the file prints `timeframe = "1h"`). One evaluation per completed bar; every window reads the decision bar's causal past only (plus the decision bar's own completed print); fills land on the decision bar's own close under the derived rule below.
- Warmup (source-native, disclosed): `startup_candle_count = 30` — the file's own floor, held flat. Covers the 20-bar BB seed, the 14-bar RSI seed, and the 9-bar TEMA seed with margin. Coded behaviour underneath: rolling windows print NaN until seeded and every NaN edge/comparison is false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; the futures-folder isolated-margin USDT-M test config is venue fit, and venue spelling plus symbol normalization are the only market steps — no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced BbandRsi, AwesomeMacd, Quickie, Strategy005, BinHV27, and TD-Sequential siblings use. No order-types plumbing ships in the file at all (cleaner than the admitted Strategy005/TD-Sequential limit-plumbing mappings) — no maker-touch, queue, or intrabar-path-dependent fill: entries, both mirrored signal exits, and the stop leg are all bar-close-evaluated; the Signal mutual-exclusion proof leaves no ambiguous same-bar signal fill order, and any bar co-printing a mirrored exit with the stop leg closes the full unit flat either way, so no intrabar ordering assumption is needed. `process_only_new_candles = True` is source-native completed-bar semantics; the Binance kline close timestamp is the decision/availability timestamp (the bar is complete at its close — causal under same-bar-close fills).
- Interval precedent (disclosed, not assumed): `1h` is an already-admitted interval on `main` via the BbandRsi, AwesomeMacd, ADXMomentum, CMCWinner, and TD-Sequential records — no novel-interval confirmation is required for this frame. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its inert ROI rung and −5% stop are preserved verbatim as the risk legs (fractions of entry-price distance; the stop's basis is leverage-invariant) while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees: the campaign-manifest-pinned Binance USDT-M regular-user schedule per baseline §4 — no invented rate in this record; funding: the source declares no funding treatment at all, this record claims no realized funding, and any modeled funding stays downstream house-model scope — never a silent zero, never reported as realized), under the single-unit/no-add position pin from Signal — no safety-order/add tranche activates in this derived version, so position events are fully determined by the legs above and sizing changes no event, never presented as source-native behaviour.
- Leverage/liquidation fence (arithmetic, verifiable): at 5× isolated, a −5% adverse price move is a −25%-of-margin unrealized loss — several multiples above any standard isolated-liquidation threshold (which needs roughly a −19%+ excursion at 5×); at 3× the distance is larger still. The −5% stop therefore binds first by construction on every path — no price path reaches liquidation before the stop, so the margin model for this version is complete (stop-then-flat, no liquidation branch reachable, no forced-closure event to specify). The inert +100% ROI rung never interacts with margin. Liquidation, margin-call, and bankruptcy branches are arithmetically unreachable here, disclosed — not excluded by definitional fiat.
- Concurrency: at most one position per market at any time; an edge opens the full unit on a flat book; the mirrored exit or the stop closes it in full; re-entry after an exit needs only the next qualifying edge (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (162 lines: the indicator block, the two entry conjunctions, the two mirrored exit conjunctions, the `timeframe`/`minimal_roi`/`stoploss`/`can_short`/`trailing_stop`/`process_only_new_candles`/`startup_candle_count` literals, and the `FSampleStrategy(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: rolling NaNs compare false and NaN edges never cross (no early entry, no early exit). The source-native 30-bar floor additionally holds every pre-seed bar flat — file semantic, not a researcher pin.
2. Exact-equality rule fenced: the long guard admits `tema == bb_mid` while the short guard excludes it — equality belongs to the long side by code; both slope guards are strict so a flat TEMA satisfies neither side. Strictness preserved throughout — disclosed, not smoothed.
3. Zero-volume fence: the `volume > 0` gate reads the completed decision bar's own volume (point-in-time at close) — zero-print bars deterministically print no edge on either side. Coded gate, disclosed, not repaired into a signal.
4. Prose-vs-code fence: the commented-out `# minimal_roi = {"60": 0.1, "30": 0.2, "0": 0.2}` ladder is a comment — the coded `{"0": 1}` governs, so the comment neither narrows nor widens any gate. Coded legs govern; prose never does.
5. Inert-rung fence: the +100% ROI rung is coded but economically inert (no 1h bar doubles from entry) — disclosed as inert exactly as the admitted TD-Sequential record fences its +500% rung, never as a live profit-taking leg and never tightened by repair. Effective exits are the mirrored signal legs plus the −5% stop.
6. Wide-stop fence: the −5% stop stands several multiples below ordinary 1h noise the regime guards already filter — by construction a disaster backstop that almost never binds before a mirrored exit in ordinary tape, and always binds before any liquidation excursion (see Execution assumptions). Coded fact, disclosed, not reinterpreted as a tight risk regime and not tightened by repair.
7. No-edge-confusion fence: both entries are one-bar `crossed_above` edges (fixed one-bar offset, no forward reference) while all four guards are persistent states — converting any edge to a state (or vice versa) would be a different, unpinned rule with different trade events.
8. Cousin records fenced as different constructions (none trades an RSI-30/70 cross pair with TEMA(9)-vs-BBmid(20) side-plus-slope guards and mirrored two-sided exits on `1h`): the admitted `freqtrade-quickie` pool-mate trades ADX-gated TEMA/BBmid persistent states behind an SMA200>close filter (no RSI leg, no edges, long-flat, `5m`); the admitted `freqtrade-simple` pool-mate trades MACD+BB+RSI70 momentum legs (no cross edges, no TEMA, long-flat, `5m`); the admitted `freqtrade-strategy003` pool-mate trades an RSI-Fisher-MFI washout behind EMA gates (`5m`); the admitted `catching-the-bottom-rsi-dip-reversal` pool-mate trades an RSI dip-state reversal single-sided on `1h`; the admitted `chartart-bollinger-rsi-double-joint-cross` pool-mate trades a joint RSI+BB cross two-sided on `1d`; the admitted `td-sequential-setup9-perfected` pool-mate trades 9-count run-length perfection long-only on `1h` (pure pandas counting, zero indicator reads). Not a threshold re-tuning of any of them: moving any period, threshold, strictness, side, frame, or the mirror structure would each be a different, unpinned rule — none is admitted here.
9. Sibling-file fence: every other file in the collection (`berlinguyinca/*`, `Strategy00*`, `Supertrend`, `Diamond`, `PowerTower`, `Bandtastic`, the `Reinforced*` resampled siblings, the `lookahead_bias/*` folder) is a separate pin — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
10. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT market choice, the same-bar-close fills, the single-unit/no-add/no-cooldown position pin, the framework-default readings (`use_exit_signal=True`, `exit_profit_only=False`), and house sizing/costs with safety tranches deactivated — all predeclared above. The `1h` frame, both RSI edges with all literals and strictness, the TEMA/BBmid side-plus-slope guards, the volume gate, the mirrored exits, the inert ROI rung with the −5% stop, the disabled trailer, the two-sided stance, the per-completed-bar evaluation, and the 30-bar startup floor are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: RSI(14-default) / cross-30-long / cross-70-short edges / TEMA(9)-vs-BBmid(20, typical) guards with pinned strictness / mirrored exits / inert 100% rung / −5% stop / single-unit two-sided / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Edge relevance: entering on the first post-warmup bar per side-regime state (same guards, no RSI edges) must not improve net expectancy; fail ⇒ the cross edges add nothing over blind regime exposure.
- F2 — Guard relevance: removing the TEMA/BBmid side-plus-slope guards (bare RSI-30/70 cross reversal, same risk) must not improve net expectancy; fail ⇒ the regime guards add nothing over the bare cross pair.
- F3 — Risk-leg relevance: removing the −5% stop (mirrored-signal exits only, inert rung unchanged) must not improve net expectancy; fail ⇒ the disaster backstop adds nothing over the bare mirror machine.

## Crypto portability

BTCUSDT Binance perpetual `1h` is the research pin (source names no market; the file's own folder tests Binance futures isolated-margin USDT-M). Two-sided with full-unit open/close; the long-only book expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. Bar volume is a native Binance kline field on both spot and perpetual venues. Funding is declared nowhere in the source and modeled only downstream by house assumptions — never claimed as realized.

## Limitations

- The `1h` frame rides existing admission precedent (BbandRsi, AwesomeMacd, ADXMomentum, CMCWinner, TD-Sequential `1h`) — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- A trend that keeps extending after entry is held until the mirrored exit or the −5% stop; RSI chop across 30/70 while TEMA straddles the midline whipsaws the book side-to-side (edge-then-reverse round trips with no cooldown to damp them — disclosed as the principal friction). There is no decay, chop, trend-loss, or further time exit — disclosed, not repaired.
- TA-Lib default-period internals (RSI 14 seeding, TEMA initialization, NaN propagation) live in the TA-Lib/qtpylib libraries outside the pinned file — pinned by call with explicit-or-default periods, not re-derived; exact reproduction inherits those libraries' seeding alongside the 30-bar floor. RSI 14 is a deterministic library default, never a tuned or hidden parameter.
- The commented-out ROI ladder is dead — nothing further to fence.
- No trailing, no breakeven, no time exit, no cooldown — all explicitly absent, never to be added by repair.
- Liquidation branches are arithmetically unreachable under the −5% stop at 3x/5x isolated (see Execution assumptions) — disclosed as arithmetic, not waived by definition; any future version changing leverage, stop distance, or sizing re-opens this fence.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/futures/FSampleStrategy.py
- https://github.com/freqtrade/freqtrade-strategies
