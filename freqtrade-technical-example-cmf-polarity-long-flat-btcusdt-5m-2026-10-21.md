---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade TechnicalExample CMF-polarity state long-flat on BTCUSDT 5m bars
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
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/TechnicalExampleStrategy.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade TechnicalExample CMF-polarity state long-flat on BTCUSDT 5m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the same lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, `freqtrade-asdts-rockwell`, `freqtrade-macd-cci-dip-state`, `freqtrade-binhv27`, and `freqtrade-macd-cross-cci-edge` records — this is only its eleventh record, and the first pinned to this exact file).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/berlinguyinca/TechnicalExampleStrategy.py`.
- GitHub blob SHA at the pinned commit: `d0cafe787b0c03e4423bfb4dbb287d36f55e3c41`, size 1069 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 1069 bytes, 41 lines, SHA-256 `0a3d94c8ef857284c9bc37d592af329b1a831f9c504fb2d73b63db00d303db50`, identical to the GitHub blob (`git hash-object` reproduces `d0cafe78…55e3c41`) — the entire file was retrieved and inspected.
- Registration: the file defines class `TechnicalExampleStrategy(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `berlinguyinca/MACDStrategy.py`, `berlinguyinca/MACDStrategy_crossed.py`, `berlinguyinca/ADXMomentum.py`, `berlinguyinca/ASDTSRockwellTrading.py`, `berlinguyinca/AdxSmas.py` (open PR #331), `berlinguyinca/AwesomeMacd.py`, `berlinguyinca/BbandRsi.py`, `berlinguyinca/CombinedBinHAndCluc.py`, `berlinguyinca/EMASkipPump.py`, `berlinguyinca/CMCWinner.py`, `berlinguyinca/ClucMay72018.py` (open PR #350), `berlinguyinca/BinHV27.py`, `berlinguyinca/SmoothOperator.py` (closed, never merged), and `berlinguyinca/PowerTower.py` (degenerate on BTC-scale prices — fenced in Negative evidence 8) are different pins with different gates — this record pins ONLY the TechnicalExampleStrategy file's literals below, and no reviewer repair may substitute a sibling constant.
- The file's own words (quoted for gate evidence, never extended): `minimal_roi = { "0": 0.01 }`; `stoploss = -0.05`; `timeframe = '5m'`; indicator `dataframe['cmf'] = cmf(dataframe, 21)`; entry `(dataframe['cmf'] < 0)` (`enter_long = 1`); exit `(dataframe['cmf'] > 0)` (`exit_long = 1`) under the prose comment `different strategy used for sell points, due to be able to duplicate it to 100%`. No `trailing`, no `startup_candle_count`, no `use_exit_signal` / `exit_profit_only` override, no `can_short`, no `process_only_new_candles`, no order-type mapping ships anywhere — the framework defaults below are disclosed as defaults, never as file literals.
- Out-of-file call pinned (one only, resolved by name): `cmf` is `from technical.indicators import cmf`, where the `technical` package (`freqtrade/technical`, default branch `main`, HEAD `ce0e895d04356c3c713e84abaaf3b798c1928c7e`) defines in `technical/indicators/volume_indicators.py` (blob `5203e45dc0b4695d15dca1e7c0646d900ed315a4`, 621 bytes) exactly `cmf = chaikin_money_flow` with `def chaikin_money_flow(dataframe, period=21)`: `mfm = ((close - low) - (high - close)) / (high - low)`; `mfv = mfm * volume`; `cmf = mfv.rolling(21).sum() / volume.rolling(21).sum()`. Standard Chaikin Money Flow, trailing 21-bar window, no override in the strategy file. No DB, no network, no `request.*`, no `security()`, no resample/interpolate, no hyperopt parameter (`IntParameter`/`BooleanParameter`/`CategoricalParameter`/`DecimalParameter` zero hits), no informative-pair call in the file.
- Full-file token census (verified over the 41 lines this cycle): 0 `short` (case-insensitive — no short leg, no short identifier anywhere); 0 `shift` (no lag call in the file body — the rule reads the decision bar's own completed values only); 0 `crossed` (no edge call — both legs are persistent level states, disclosed); 0 `hyperopt` / 0 `Parameter`; 1 `stoploss` (the `-0.05` attribute) and 1 `minimal_roi` (the single-rung `0.01` ladder) as the only risk legs; 0 shipped `trailing`; 0 `startup_candle_count` (the record's 30-bar floor is a predeclared researcher pin, never a file semantic); 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop); 0 `volume` (no volume read in the file body — the volume weighting lives inside the pinned `cmf` helper, disclosed); 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic); 0 `resample` / 0 `informative` / 0 `request` / 0 `security`.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Freqtrade deployment. The source pins the `5m` frame, the CMF(21)-below-zero entry state, the CMF(21)-above-zero exit state, the single-rung 1% ROI, the −5% stop, and the long-only stance — but ships no venue spelling, no fill-timing flag, no warmup guard, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market `BTCUSDT` (the file names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed); (2) completed-bar decisions with same-bar-close market fills (the file's own framework contract evaluates per completed bar — derivation disclosed, never presented as the source engine's own timing); (3) single-unit position pin with hold-no-op semantics plus a 30-bar researcher warmup pin (the file carries no position reference and no length guard — disclosed, never presented as source-native behaviour); (4) the source's absent sizing/costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-21): working-tree filename/content search for `technicalexample` / `chaikin_money_flow` returns zero strategy records — no record in the pool cites this source file. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles band-ratio) trades a money-flow-polarity rule. CMF cousins in the pool are fenced as different constructions in Negative evidence 7. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: hold a long while the 21-bar Chaikin Money Flow sits below zero (volume-weighted distribution), release it when CMF reclaims above zero (volume-weighted accumulation). A single-rung 1% ROI (`"0": 0.01`) and a fixed −5% stoploss backstop every position. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Volume-signed polarity machine, long-only. Each bar's volume is signed by where the close sits inside the high–low range (close at the high prints +volume, at the low prints −volume) and the 21-bar CMF is that signed flow normalized by total volume — a bounded [−1, +1] gauge of whether volume has been accumulating near the highs or distributing near the lows. The book is entered on any flat bar printing distribution (`cmf < 0`) and held through every further distribution bar by design; it is released on the first bar printing accumulation (`cmf > 0`). Unlike edge-trigger records (which fire at most on a crossing bar), both legs are persistent states — a book already positioned treats further distribution bars as hold-no-ops until a qualifying accumulation bar, an ROI fill, or the stop. The exact-zero bar (`cmf == 0.0`) prints neither leg and is a pure hold by construction. The failure mode is plain: a market that oscillates around the zero line prints repeated entry-then-exit round trips with no hysteresis band, and a market that distributes without ever reclaiming zero is held until the ROI rung or the −5% stop — there is no decay, chop, or time exit (disclosed, not repaired).

## Signal

Exact rule as pinned (any other CMF period, threshold, state-vs-edge pairing, risk rung, fill, frame, or book is a different, unpinned rule). The CMF arithmetic below is the pinned `technical` helper's verbatim construction with the file's own `21`:

```text
mfm[t]  = ((close[t] - low[t]) - (high[t] - close[t])) / (high[t] - low[t])  // per-bar, causal
mfv[t]  = mfm[t] * volume[t]
cmf[t]  = sum(mfv[t-20..t]) / sum(volume[t-20..t])                            // trailing 21-bar, causal
entry   = (cmf[t] < 0)   // enter_long = 1, persistent state
exit_sig= (cmf[t] > 0)   // exit_long = 1, persistent state
risk    = ROI {"0": 0.01} (fraction); fixed stop at -5% (stoploss -0.05)
floor   = leading-window bars: rolling NaN comparisons false (see Required data)
```

- Trade events: `enter_long=1` on any flat bar printing `cmf < 0`, `direction` long-only; `exit_long=1` on any positioned bar printing `cmf > 0`. Each print is a persistent state, not a one-bar edge — a book already positioned treats further distribution bars (including the entry bar's own repeats) as hold-no-ops under the position pin below, and a flat book treats accumulation bars as no-ops.
- Exact boundaries (pinned semantics): both comparisons are strict (`< 0`, `> 0`) — a bar with `cmf == 0.0` fires neither leg and holds whatever book exists. All preserved throughout.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `cmf[t] < 0` while any signal-exit bar has `cmf[t] > 0` — no bar satisfies both, including the exact-zero boundary and NaN seed bars (all strict comparisons false). ROI/stop cannot co-fire with entry on the entry bar either (zero distance at the fill). The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero short-leg tokens ship anywhere, and the framework default `can_short = False` applies (disclosed default, never a file literal) — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the accumulation-state signal exit, the single-rung 1% ROI, and the −5% stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — exits fire even at a loss; disclosed defaults, never file literals). No trailing, no time exit, no breakeven move — explicitly none further, not invented.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry-state bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying distribution bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low`/`close`/`volume` (money-flow multiplier plus 21-bar trailing sums, fixed non-negative offsets) with no `shift` call in the file body and no edge lookback of any kind; the decision bar's own forming values are never read. No funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `5m` bars of BTCUSDT: `high`/`low`/`close` (money-flow-multiplier construction and both polarity reads) and bar `volume` (read twice inside the pinned helper — once to sign each bar's flow, once to normalize the 21-bar sum; the rule is doubly volume-weighted, disclosed; no standalone volume threshold leg ships). No `open` read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `5m` (source-native — the file prints `timeframe = '5m'`). One evaluation per completed bar; every window reads the decision bar's causal past only; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 30 five-minute bars held flat. Covers the 21-bar CMF rolling seed with margin. The file ships no `startup_candle_count` — quoted absence, never filled in from elsewhere. Coded behaviour underneath: rolling windows print NaN until seeded and every strict NaN comparison is false — no leg can fire early. Zero-range bars divide by zero inside the helper and resolve to NaN/inf deterministically — strict comparisons against them still resolve by the same inequalities (NaN false, signed-inf by sign), never a fill by accident. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced BbandRsi, AwesomeMacd, EMASkipPump, ADXMomentum, CMCWinner, ASDTSRockwell, MACDStrategy-state, MACDStrategy-crossed-edge, and BinHV27 siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, the accumulation-state signal exit, and the ROI/stop legs are all bar-close-evaluated; the Signal mutual-exclusion proof leaves no ambiguous same-bar signal fill order, and any bar co-printing a signal exit with an ROI/stop leg closes the full unit flat either way, so no intrabar ordering assumption is needed.
- Interval precedent (disclosed, not assumed): `5m` is an already-admitted interval on `main` via the EMASkipPump, CombinedBinHAndCluc, ASDTSRockwell, MACDStrategy-state, MACDStrategy-crossed-edge, and BinHV27 records — no novel-interval confirmation is required for this frame. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its 1% ROI rung and −5% stop are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the distribution state opens the full unit on a flat book; the accumulation-state signal exit, the 1% ROI, or the stop closes it in full; re-entry after an exit needs only the next qualifying distribution bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (41 lines: the `cmf(dataframe, 21)` call, the two polarity state legs, the `timeframe`/`minimal_roi`/`stoploss` literals, and the `TechnicalExampleStrategy(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: rolling NaNs compare false (no early entry, no early exit). The 30-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired. The file ships no `startup_candle_count`, so the floor is purely a researcher pin, never misattributed.
2. Exact-zero rule fenced: both legs are strict (`< 0` / `> 0`) — a bar sitting exactly on zero fires nothing on either side and holds the existing book. Strictness preserved throughout — disclosed, not smoothed.
3. Prose-vs-code fence: the exit comment's `different strategy used for sell points, due to be able to duplicate it to 100%` is prose — the coded exit leg is `(cmf > 0)` (`exit_long = 1`), and the coded leg governs. Prose never narrows or widens it.
4. Zero-hyperopt fence: 0 `Parameter` / 0 `hyperopt` tokens anywhere in the 41 lines — every literal (`21`, `0`, `0.01`, `-0.05`, `'5m'`) is a frozen constant, never a search-space default. No fitted value anywhere in this artifact.
5. Risk-posture fence: the −5% stop is 5× the opening 1% ROI rung — by construction the stop is a disaster backstop that almost never binds before the ROI rung or the accumulation-state exit in ordinary tape. Coded fact, disclosed, not reinterpreted as a tight risk regime and not tightened by repair.
6. Degenerate-bar fence: a zero-range bar (`high == low`) divides by zero inside the pinned helper and resolves to NaN/inf — strict comparisons against it still resolve deterministically (NaN false on both legs; signed-inf by sign), so no accidental fill. Zero-volume 21-bar windows likewise resolve deterministically through the same inequalities.
7. Cousin records fenced as different constructions (none trades a CMF-level polarity state pair, long-flat, with this risk pair): the admitted `forven-chaikin-mf-threshold-cross` pool-mate trades a 20-bar CMF threshold-CROSS edge pair (±0.05 with hysteresis, one-bar edge events, no level-hold) on `1h` from a different repository; the admitted `cmf-velocity-zero-cross-ema200-bracket` pool-mate trades a 7-bar-averaged CMF *velocity* (differenced flow) zero-cross behind an EMA-200 gate with a 2:1 ATR bracket, two-sided, on `1d`, from an FMZ port; the admitted `chaikin-oscillator-ad-zero-cross` pool-mate trades the MACD of the cumulative A/D line (a different indicator — oscillator of cumulative stock, not a volume-normalized flow ratio), two-sided, on `4h`. Not a threshold re-tuning of any of them: moving the CMF period, adding a hysteresis band, converting either state to a crossing edge, flipping any strictness, or changing the ROI rung, the stop, or the frame would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `PowerTower.py` is a degenerate pin on BTC-scale prices — its entry requires `close > close^3.849` on three lags, which is never true for any price above 1.0 (and trivially always true below it), so it specifies no tradeable BTCUSDT rule and is never substituted into this record. `MACDStrategy.py`, `MACDStrategy_crossed.py`, `ADXMomentum.py`, `AdxSmas.py`, `ASDTSRockwellTrading.py`, `AwesomeMacd.py`, `BbandRsi.py`, `CombinedBinHAndCluc.py`, `EMASkipPump.py`, `CMCWinner.py`, `BinHV27.py`, and `ClucMay72018.py` are separate pins — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT market choice, the same-bar-close fills, the single-unit/no-add/no-cooldown position pin, the 30-bar warmup floor (the file ships none), the framework-default readings (`can_short=False`, `use_exit_signal=True`, `exit_profit_only=False`, per-completed-bar evaluation), the pinned `technical`-library CMF construction (period 21 — file literal; arithmetic lives in the `ce0e895d` helper, never re-derived), and house sizing/costs — all predeclared above. The `5m` frame, the distribution-state entry with all its literals, the accumulation-state exit, the single-rung 1% ROI with the −5% stop, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: CMF(21) / polarity states / strict zero thresholds / state (never edge) legs / accumulation-state exit / single-rung 1% ROI / −5% stop / single-unit long-only / `5m` BTCUSDT / same-bar-close fills are frozen.

- F1 — Hysteresis relevance: replacing the zero-line polarity pair with a ±0.05 threshold-cross edge pair (same CMF(21) base, same risk) must not improve net expectancy; fail ⇒ the zero-line state construction adds nothing over its hysteresis edge twin.
- F2 — Normalization relevance: replacing the volume-normalized CMF ratio with the unnormalized 21-bar signed money-flow sum (same state-entry shape against a pinned absolute level, same exit) must not improve net expectancy; fail ⇒ the record is a signed-volume accumulator wearing a normalized-flow label.
- F3 — State-vs-edge relevance: replacing the persistent level-hold states with one-bar threshold-cross edges (same CMF(21), same zero line, same risk) must not improve net expectancy; fail ⇒ the state construction adds nothing over the pure rotation-timing twin.

## Crypto portability

BTCUSDT Binance perpetual `5m` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. The rule reads the bar-`volume` tape twice (flow signing and flow normalization), so venue volume-definition differences (e.g. spot vs futures volume, wash-reporting) move both the signal level and the polarity timing — stated plainly as a portability boundary: cross-venue porting without re-verification would be a different, unpinned claim, disclosed. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- The `5m` frame rides existing admission precedent (EMASkipPump, CombinedBinHAndCluc, ASDTSRockwell, MACDStrategy-state, MACDStrategy-crossed-edge, BinHV27 `5m`) — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- A position in a market whose CMF never reclaims above zero is held until the 1% ROI rung or the −5% stop; a market oscillating tightly around the zero line prints repeated entry-then-exit round trips with no hysteresis band to rest in (polarity-state profile, disclosed). There is no decay, chop, trend-loss, or further time exit — disclosed, not repaired.
- The CMF arithmetic (money-flow-multiplier division, volume weighting, 21-bar rolling sums) lives in the pinned `technical` helper outside the strategy file — pinned by call with period 21 at helper pin `ce0e895d`, not re-derived; exact reproduction inherits that helper's zero-division behaviour alongside the 30-bar floor.
- The `technical` package revision is pinned only as the `main`-branch HEAD observed this cycle (`ce0e895d`); a future helper change would be a different, unpinned rule — downstream reproduction must freeze this helper revision, disclosed.
- No trailing, no breakeven, no short leg, no cooldown — all explicitly absent, never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/TechnicalExampleStrategy.py
- https://github.com/freqtrade/freqtrade-strategies
