---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade EMASkipPump EMA-dip BB volume-guarded long-flat on BTCUSDT 5m bars
created: 2026-10-20
updated: 2026-10-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/EMASkipPump.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade EMASkipPump EMA-dip BB volume-guarded long-flat on BTCUSDT 5m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the same repository that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, and `freqtrade-awesome-macd` records — this is only its fifth record).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/berlinguyinca/EMASkipPump.py`.
- GitHub blob SHA at the pinned commit: `b0750c7f1c1877a4e1f77897a784cce7a4674988`, size 3020 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 3020 bytes, 87 lines, SHA-256 `74117c68b3407a775d80fc4d4f1b27852689baad2255f19a7026a2b0c45b2085`, identical to the GitHub blob (`git hash-object` reproduces `b0750c7f…74988`) — the entire file was retrieved and inspected.
- Registration: the file defines class `EMASkipPump(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `berlinguyinca/BbandRsi.py` (RSI(14) level AND typical-price BB(20, 2) dip conjunction, `1h`), `berlinguyinca/CombinedBinHAndCluc.py` (dual-leg BB-penetration with microstructure guards, `5m`), and `berlinguyinca/AwesomeMacd.py` (AO-cross gated by MACD polarity, `1h`) are different pins with different gates — this record pins ONLY the EMASkipPump file's literals below, and no reviewer repair may substitute a sibling constant.
- The file's own words (quoted for gate evidence, never extended): `EMA_SHORT_TERM = 5`; `EMA_MEDIUM_TERM = 12`; `EMA_LONG_TERM = 21`; `minimal_roi = { "0": 0.1 }`; `stoploss = -0.05`; `timeframe = '5m'`; class docstring `basic strategy, which trys to avoid pump and dump market conditions. Shared from the tradingview slack`; ROI comment `we only sell after 100%, unless our sell points are found before` (verbatim — the coded ROI leg is `0.1`, i.e. 10%, and the record pins the code, never the comment's stray `%` figure); stoploss comment `should be converted to a trailing stop loss` (a wish, never a shipped leg — fenced below); indicators `ta.EMA(dataframe, timeperiod=5/12/21)`, `qtpylib.bollinger_bands(qtpylib.typical_price(dataframe), window=20, stds=2)`, `ta.MIN(dataframe, timeperiod=12)`, `ta.MAX(dataframe, timeperiod=12)`; volume guard `dataframe['volume'] < (dataframe['volume'].rolling(window=30).mean().shift(1) * 20)`; entry `close < ema5 & close < ema12 & close == min12 & close <= bb_lowerband`; exit `close > ema5 & close > ema12 & close >= max12 & close >= bb_upperband`. No `trailing`, no `startup_candle_count`, no `use_exit_signal` / `exit_profit_only` override, no `can_short`, no `process_only_new_candles`, no order-type mapping ships anywhere — the framework defaults below are disclosed as defaults, never as file literals.
- Out-of-file calls pinned (all resolved by name, all standard): `ta.EMA` / `ta.MIN` / `ta.MAX` (TA-Lib abstract on closes, fixed periods 5/12/21/12); `qtpylib.typical_price` ((H+L+C)/3) and `qtpylib.bollinger_bands(..., window=20, stds=2)` (Freqtrade vendor calls pinned by call; their internal arithmetic lives outside this file and is disclosed as such, never re-derived here). No DB, no network, no `request.*`, no `security()`, no resample/interpolate, no hyperopt parameter in the file.
- Full-file token census (verified over the 87 lines this cycle): 0 `enter_short` / 0 `exit_short` / 0 `can_short` (case-insensitive — the 5 `short` hits are all the `EMA_SHORT_TERM` identifier; no short leg anywhere); 1 `stoploss` (`-0.05`) and 1 `minimal_roi` (`{"0": 0.1}`) as the only risk legs; 0 shipped `trailing` (the single `trailing` hit is the stoploss code comment wishing for a future conversion — explicitly not a leg); 0 `startup_candle` / 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop); 2 `volume` (the guard only — no volume-weighted trigger); 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic); `ema_21` is computed and never read by any order line (plumbing-only, fenced below).

Pre-write dedup (2026-10-20): working-tree filename/content search for `EMASkipPump` / `EMA_SHORT_TERM` / `skip-pump` returns zero strategy records. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas) trades an EMA-stack dip with MIN/MAX extremes, typical-price Bollinger rails, and a volume anti-pump guard. The pool's nearest cousins are fenced as different constructions in Negative evidence 7 — none conjoins a sub-EMA12 dip print, a 12-bar lowest-low print, a typical-price lower-rail touch, and a 30-bar volume-spike veto with a mirrored EMA-reclaim/highest-high/upper-rail exit. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code and docstring print: buy the bar where price dips below both fast EMAs while printing the trailing 12-bar low at or under the typical-price lower Bollinger rail — a washed-out dip — unless the bar's volume exceeds 20× its trailing 30-bar mean (a pump bar the file refuses to chase); exit the mirror (price reclaims both fast EMAs while printing the trailing 12-bar high at or above the upper rail). A 10% ROI target and a −5% stoploss backstop every position. The file's docstring frames this as avoiding pump-and-dump conditions. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Dip-with-receipts machine with a bouncer, long-only. Unlike bare Bollinger-dip records (fire every rail touch), the dip must simultaneously print the 12-bar lowest low AND sit under both fast EMAs — the rail touch alone never suffices, so shallow tags that hold above the EMAs are refused. Unlike pure EMA-cross records (trade the cross itself), no cross is ever traded: both entry and exit are state prints (below-both vs above-both), never an edge. The volume veto is the pump-and-dump discipline made literal — a dip bar printed on 20× mania volume is held flat, so the buyer only lifts washed-out, quiet tape. The mirrored exit is reclaim-symmetric: the book banks only when price re-establishes itself above both EMAs at the 12-bar high against the upper rail, so dead-cat bounces that fail the EMAs keep the position open until ROI or the −5% stop.

## Signal

Exact rule as pinned (any other EMA periods, BB window/stds, MIN/MAX lookback, volume multiple, ROI/stop pair, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own:

```text
ema5[t]    = TA-Lib EMA(close, 5)
ema12[t]   = TA-Lib EMA(close, 12)
mid/low/up = vendor Bollinger(typical_price(HLC), 20, 2)
min12[t]   = TA-Lib MIN(close, 12)          // trailing 12-bar lowest low
max12[t]   = TA-Lib MAX(close, 12)          // trailing 12-bar highest high
volmean    = volume.rolling(30).mean().shift(1)
guard      = volume[t] < volmean[t] * 20    // anti-pump veto
entry      = guard AND (close[t] < ema5[t]) AND (close[t] < ema12[t])
             AND (close[t] == min12[t]) AND (close[t] <= low[t])     // enter_long = 1
exit_sig   = (close[t] > ema5[t]) AND (close[t] > ema12[t])
             AND (close[t] >= max12[t]) AND (close[t] >= up[t])      // exit_long = 1
risk       = take-profit at +10% from entry (minimal_roi {"0": 0.1}); fixed stop at -5% (stoploss -0.05)
floor      = leading-window bars: rolling NaN comparisons false (see Required data)
```

- Trade events: `enter_long=1` on any bar printing the guarded five-conjunct dip, `direction` long-only; `exit_long=1` on bars printing the four-conjunct reclaim. Each print is a state print re-evaluated per bar, not a one-bar edge — a book already positioned treats further entry bars as hold-no-ops under the position pin below.
- Exact boundaries (pinned semantics): entry EMAs strict `<` (a close exactly on either EMA vetoes that conjunct); exit EMAs strict `>`; `close == min12` fires on ties (the rolling MIN includes the current bar, so ties satisfy equality — disclosed, not smoothed); rail touches `<=` / `>=` fire on exact contact. All preserved throughout.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `close[t] < ema12[t]` while any signal-exit bar has `close[t] > ema12[t]` — entry and signal-exit never co-print on any bar, degenerate or otherwise. ROI/stop cannot co-fire with entry on the entry bar either (zero distance at the fill). The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero short-leg tokens ship anywhere, and the framework default `can_short = False` applies (disclosed default, never a file literal) — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the mirrored reclaim signal, the +10% ROI leg, and the −5% stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — exits fire even at a loss; disclosed defaults, never file literals). No trailing (the code comment wishes for one — explicitly unshipped, never to be added by repair), no time exit, no breakeven move — explicitly none, not invented.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying dip bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar OHLCV (`close`/`high`/`low` for EMAs, typical price, MIN/MAX, rails; `volume` for the guard) with fixed non-negative offsets (`t`, trailing windows, one `shift(1)` on the volume mean) — no funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path. Freqtrade engine column semantics (`enter_long`/`exit_long` per completed bar) are the file's own framework contract.

## Required data

- Completed `5m` bars of BTCUSDT: `high`/`low`/`close` for the EMA(5/12/21)/typical-price-BB(20,2)/MIN/MAX(12) path and `volume` for the 30-bar anti-pump guard. No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `5m` (source-native — the file prints `timeframe = '5m'`). One evaluation per completed bar; every window reads the decision bar and its causal past only — the volume mean is additionally `shift(1)`-lagged, so the guard never sees the decision bar's own volume average; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 40 five-minute bars held flat. Covers the EMA-21 seed (longest EMA), the BB(20) rolling seed, the 30-bar volume mean plus its one-bar shift, and the MIN/MAX(12) windows. Coded behaviour underneath: rolling windows print NaN until seeded and every strict NaN comparison is false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced CombinedBinHAndCluc (`5m`, the direct interval sibling), BbandRsi, AwesomeMacd, and TDSequential siblings and the admitted Forven siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, the mirrored signal exit, and the ROI/stop legs are all bar-close-evaluated; the Signal mutual-exclusion proof leaves no ambiguous same-bar fill order to the engine.
- Interval precedent (disclosed, not assumed): `5m` is an already-admitted interval on `main` via the CombinedBinHAndCluc record — no novel-interval confirmation is required for this frame. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI/stop percentages are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the dip opens the full unit on a flat book; the mirrored reclaim exit, the ROI leg, or the stop closes it in full; re-entry after an exit needs only the next qualifying dip bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (87 lines: the EMA(5/12/21) calls, the typical-price BB(20, 2) block, the MIN/MAX(12) extremes, the 30-bar volume guard, the guarded five-conjunct long entry, the mirrored four-conjunct exit, the `timeframe`/`minimal_roi`/`stoploss` literals, and the `EMASkipPump(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: rolling NaNs compare false (no early entry, no early exit). The 40-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired.
2. Exact-touch rule fenced: entry EMAs strict `<` and exit EMAs strict `>` fire nothing on equality; rail `<=`/`>=` fire on contact; `close == min12` fires on ties (rolling MIN includes the current bar). Strictness and tie semantics preserved throughout — disclosed, not smoothed.
3. Dead-column plumbing fenced: `ema_21` is computed and never read by any order line — plumbing/display-only, never a trend filter, never repaired into a gate.
4. Unshipped-trailing fenced: the stoploss comment `should be converted to a trailing stop loss` is an author wish, not a leg — no trailing ships anywhere and this record implements none. A trailing variant would be a different, unpinned rule — disclosed, not repaired.
5. ROI-comment fence: the comment `we only sell after 100%` contradicts the coded `minimal_roi = { "0": 0.1 }` (10%) — the record pins the code literal, never the comment's stray figure. Disclosed, not reinterpreted.
6. Guard-selectivity fenced: the volume veto binds only above 20× the lagged 30-bar mean — on ordinary tape it passes nearly every bar, so the entry is effectively the four-conjunct dip except during mania prints. The absence of a participation floor is a coded fact (quiet dips enter exactly like busy ones) — disclosed, not reinterpreted as a liquidity requirement.
7. Cousin records fenced as different constructions (none trades an EMA-stack dip with MIN/MAX extremes, typical-price Bollinger rails, and a volume-spike veto on `5m`): the admitted BbandRsi pool-mate conjoins RSI(14) levels with typical-price BB dips on `1h` (no EMA stack, no MIN/MAX, no volume guard, mirrored logic, different frame); the admitted CombinedBinHAndCluc pool-mate trades dual BB-penetration legs with microstructure fractions on `5m` (no EMA state, no extremes, no volume veto, different exits); the admitted AwesomeMacd pool-mate trades AO-cross edges gated by MACD polarity on `1h` (no dip state, no rails, no volume); the admitted forven-williams-ema-reclaim sibling reclaims a single EMA off Williams extremes (no rail touch, no MIN/MAX print, no volume veto). Not a threshold re-tuning of any of them: moving any EMA period, the BB window/stds, the MIN/MAX lookback, the volume multiple, the ROI/stop pair, or the frame would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `BbandRsi.py`, `CombinedBinHAndCluc.py`, and `AwesomeMacd.py` are separate pins — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT market choice, the same-bar-close fills, the single-unit/no-add/no-cooldown position pin, the 40-bar warmup floor, the framework-default readings (`can_short=False`, `use_exit_signal=True`, `exit_profit_only=False`, per-completed-bar evaluation), and house sizing/costs — all predeclared above. The `5m` frame, the guarded five-conjunct entry with all its literals, the mirrored four-conjunct exit, the +10%/−5% risk pair, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: guarded EMA-dip / EMA(5/12/21) / typical-price BB(20,2) / MIN/MAX(12) / 20× volume veto / mirrored reclaim exit / +10% ROI / −5% stop / single-unit long-only / `5m` BTCUSDT / same-bar-close fills are frozen.

- F1 — Guard relevance: dropping the volume veto (pure four-conjunct dip entry, same exit/risk) must not improve net expectancy; fail ⇒ the anti-pump guard adds nothing over the bare dip.
- F2 — Extremes relevance: replacing `close == min12` / `close >= max12` with the rail touches alone (entry without the lowest-low print, exit without the highest-high print, same guard/risk) must not improve net expectancy; fail ⇒ the MIN/MAX prints add nothing over rails plus EMA state.
- F3 — Risk-pair relevance: removing the ROI/stop pair (signal-only exits) must not improve net expectancy; fail ⇒ the +10%/−5% backstop adds nothing over the bare reclaim machine.

## Crypto portability

BTCUSDT Binance perpetual `5m` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count, portable across 24/7 crypto tape. Volume is a standard candle field on the venue; no exotic feed is required. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- The `5m` frame rides existing admission precedent (CombinedBinHAndCluc) — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- The signal exit fires only on a full reclaim print (above both EMAs at the 12-bar high against the upper rail); a position decaying sideways below the EMAs without printing a fresh dip is held until ROI or the −5% stop. There is no trend-loss or time exit — disclosed, not repaired.
- qtpylib `typical_price` / `bollinger_bands` internals live in the Freqtrade vendor module outside the pinned file — pinned by call, not re-derived; exact reproduction inherits that module's rolling semantics alongside TA-Lib's EMA/MIN/MAX seeding.
- TA-Lib EMA seeding inherits the library's warmup; the 40-bar floor keeps early-bar instability out of trusted events.
- No trailing, no breakeven, no time exit, no short leg, no cooldown — all explicitly absent, never to be added by repair.
- The `ema_21` column is computed and gated nowhere — nothing further to fence.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/EMASkipPump.py
- https://github.com/freqtrade/freqtrade-strategies
