---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade Strategy001_custom_exit RSI-profit-gated HA EMA-cross long-flat on BTCUSDT 5m bars
created: 2026-10-22
updated: 2026-10-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/Strategy001_custom_exit.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade Strategy001_custom_exit RSI-profit-gated HA EMA-cross long-flat on BTCUSDT 5m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the same lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, `freqtrade-asdts-rockwell`, `freqtrade-macd-cci-dip-state`, `freqtrade-binhv27`, `freqtrade-macd-cross-cci-edge`, and `freqtrade-strategy001` records — this is only its thirteenth record, and the first pinned to this exact file).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/Strategy001_custom_exit.py`.
- GitHub blob SHA at the pinned commit: `cc423884a3aa80a8b68b10c3e1c1b7f5365b7784`, size 4931 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 4931 bytes, 143 lines, SHA-256 `d53ac16d0e81b755a19ea83c535f50a6dd0629c76087b822ae399fabeaa5e841`, identical to the GitHub blob (`git hash-object` reproduces `cc423884a…65b7784`) — the entire file was retrieved and inspected.
- Registration: the file defines class `Strategy001_custom_exit(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `user_data/strategies/Strategy001.py` (same entry/exit triplets but a different stop, no profit gating, no custom leg — separately fenced in Negative evidence 7), `user_data/strategies/Strategy005.py` (volume-surge Fisher washout, separately admitted), and every `user_data/strategies/berlinguyinca/*.py` sibling are different pins with different gates — this record pins ONLY the Strategy001_custom_exit file's literals below, and no reviewer repair may substitute a sibling constant. This file is also distinct from the admitted `freqtrade-strategy001-ha-ema-cross` pool record, which pins `berlinguyinca/freqtrade-strategies@ae998ae:strategy001.py` — a different repository, path, stop, and exit construction (fenced in Negative evidence 7).
- The file's own words (quoted for gate evidence, never extended): `timeframe = '5m'`; `minimal_roi = { "60": 0.01, "30": 0.03, "20": 0.04, "0": 0.05 }`; `stoploss = -0.10`; `trailing_stop = False` (with inert `trailing_stop_positive = 0.01` / `trailing_stop_positive_offset = 0.02` that never engage while trailing is off — disclosed, never a live leg); `process_only_new_candles = True` (completed-bar evaluation, file literal); `use_exit_signal = True`; `exit_profit_only = True` (signal exits fire only on profitable closes — file literal, with admitted precedent in the strategy005/SwingHighToSky/HLHB records); `ignore_roi_if_entry_signal = False`; `order_types = { 'entry': 'limit', 'exit': 'limit', 'stoploss': 'market', 'stoploss_on_exchange': False }`; `order_time_in_force = { 'entry': 'gtc', 'exit': 'gtc' }`; indicators `ema20/ema50/ema100 = ta.EMA(dataframe, timeperiod=N)` (TA-Lib close-input convention, same reading as the admitted siblings), `heikinashi = qtpylib.heikinashi(dataframe)` keeping only the `open`/`close` columns (`ha_high`/`ha_low` never materialize — zero tokens), `rsi = ta.RSI(dataframe, 14)` (explicit period 14); entry `qtpylib.crossed_above(ema20, ema50) & (ha_close > ema20) & (ha_open < ha_close)` (`enter_long = 1`, green bar); signal exit `qtpylib.crossed_above(ema50, ema100) & (ha_close < ema20) & (ha_open > ha_close)` (`exit_long = 1`, red bar); `informative_pairs` returns `[]` (single-frame by construction); `custom_exit` returns `"rsi_profit_sell"` when `(current_candle['rsi'] > 70) and (current_profit > 0)`, else `None` — the complete custom leg, quoted verbatim.
- Out-of-file calls pinned (all resolved by name, all standard): `ta.EMA` (TA-Lib EMA on close); `qtpylib.heikinashi` (causal recursion `ha_close[t] = (open+high+low+close)[t]/4`, `ha_open[t] = (ha_open[t-1]+ha_close[t-1])/2` over completed bars and its own past — same reading as the admitted strategy001 and forven-heikin-ashi records); `ta.RSI(dataframe, 14)` (Wilder RSI on close, explicit 14); `qtpylib.crossed_above` (standard Freqtrade one-bar edge: `(s1 > s2) & (s1.shift(1) <= s2.shift(1))` — causal two-bar comparison, disclosed, never redefined). No DB, no network, no `request.*`, no `security()`, no resample/interpolate/merge, no hyperopt parameter (`IntParameter`/`BooleanParameter`/`CategoricalParameter`/`DecimalParameter` zero hits — the single `hyperopt` token is a prose comment about configuration, never code), no second-pair call in the file.
- Full-file token census (verified over the 143 lines this cycle): 0 `short` (case-insensitive — no short leg, no short identifier anywhere); 0 `enter_short` / 0 `exit_short` (long-only is the coded posture, never an omission); 0 `volume` (no volume read of any kind — the Heikin-Ashi transform reads completed-bar OHLC only); 0 `shift` in the file body (no lag call — the single one-bar lookback lives inside the standard `crossed_above` edge, disclosed above); 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop); 0 `resample` / 0 `merge` / 0 `request` / 0 `security`; 1 `stoploss` attribute (`-0.10`) and 1 `minimal_roi` ladder as the only risk attributes; 3 `trailing_stop` tokens (`False` plus the two inert config values, fenced above); 0 `startup_candle_count` (the record's 110-bar floor is a predeclared researcher pin, never a file semantic); 0 `can_short` (spot long-only engine default governs — disclosed default, never a file literal); 0 `pyramid` / 0 `position_adjustment` / 0 `adjust_trade_position` / 0 `custom_stoploss` / 0 `use_custom_stoploss` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic); 0 `ha_high` / 0 `ha_low` (undisplayed columns never kept); 1 `order_types` / 1 `process_only_new_candles` / 1 `use_exit_signal` / 1 `ignore_roi` (all file literals, quoted above); `Dict` (1 import line), `List` (2 import lines), and `reduce` (1 import line, 0 calls) are imported and never called — dead imports, fenced as plumbing with no gate effect.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Freqtrade deployment. The source pins the `5m` frame, the HA EMA-cross entry/exit triplets, the RSI-70-plus-profit custom exit, the profit-gated signal exits, the four-rung ROI ladder, the −10% stop, the disabled trailing, and the long-only stance — but ships no venue spelling, no market fills, no warmup guard, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market `BTCUSDT` on Binance spot (the file names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed); (2) completed-bar decisions with same-bar-close market fills (the file's own `process_only_new_candles = True` contract evaluates per completed bar — the source's limit-GTC later-candle fills are scoped out, derivation disclosed, never presented as the source engine's own timing); (3) single-unit position pin with hold-no-op semantics plus a 110-bar researcher warmup pin (the file carries no position reference and no length guard — disclosed, never presented as source-native behaviour); (4) the source's absent sizing/costs ride the explicit house overlay and pinned house cost assumptions (fees; spot venue — no funding leg exists to model, and no hypothetical zero funding is claimed — the source declares no funding treatment at all). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-22): working-tree filename/content search for `strategy001_custom` and `rsi_profit_sell` returns zero strategy records — no record in the pool cites this source file or trades an RSI-70-plus-profit custom exit leg. Content search for `custom_exit` returns only the TD-Sequential record's absence fence (`0 custom_exit` — an explicit non-coverage). No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles band-ratio) trades a Heikin-Ashi EMA-cross signal, a profit-gated exit, or any custom-exit leg. The admitted `freqtrade-strategy001` pool-mate pins a different repository/path/stop/exit construction and is fenced as a different rule in Negative evidence 7. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the bar where a fresh trend impulse prints (EMA20 crossing above EMA50) while the Heikin-Ashi tape confirms trend color (green bar closing above EMA20) — and stand aside to flat when the slow trend itself turns (EMA50 crossing above EMA100) while the Heikin-Ashi tape flips red below EMA20, but only bank signal exits on profitable closes (`exit_profit_only = True`), with an extra profit-taking leg that sells any position whose completed-bar RSI exceeds 70 while in profit (`rsi_profit_sell`), a four-rung time-decaying ROI ladder (5% → 4% → 3% → 1%), and a −10% fixed stop behind every position. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Profit-gated edge-fresh Heikin-Ashi trend machine, long-only. The entry buys only impulses the synthetic tape agrees with on the same bar — a golden cross inside a red Heikin-Ashi bar buys nothing. The exit construction is deliberately loss-averse by code: a slow-cross-plus-red print at a loss is HELD (profit gating), not sold — the book waits for the ROI ladder, the −10% stop, a later profitable signal print, or the RSI-70 profit-taking leg instead. Unlike the admitted strategy001 pool-mate (same triplets, exits honored even at a loss, −30% stop, no custom leg), every losing trade in this record lives a different lifecycle: loss exits become holds, the stop binds three times sooner, and overbought-profitable bars exit early through a leg the pool-mate never had. Unlike pure signal-flip records, nothing here exits merely because the oscillator turned — the RSI leg demands profit too. The coded bet is on edge-fresh Heikin-Ashi-confirmed impulses resolving before the −10% stop, with upside harvested by RSI-70 profit prints and the decaying ROI ladder rather than by slow-cross timing alone.

## Signal

Exact rule as pinned (any other lookback, threshold, edge/level choice, gating, risk rung, fill, frame, or book is a different, unpinned rule). All identifiers below are the program's own; framework primitives expand to their pinned standard definitions:

```text
ema20[t]    = TA-Lib EMA(close, 20)
ema50[t]    = TA-Lib EMA(close, 50)
ema100[t]   = TA-Lib EMA(close, 100)
ha_close[t] = (open[t]+high[t]+low[t]+close[t])/4
ha_open[0]  = open[0]; ha_open[t>=1] = (ha_open[t-1]+ha_close[t-1])/2
rsi[t]      = TA-Lib RSI(close, 14)   // explicit period
xab(a,b)[t] = (a[t] > b[t]) AND (a[t-1] <= b[t-1])   // pinned crossed_above
entry    = xab(ema20,ema50)[t] AND (ha_close[t] > ema20[t])
           AND (ha_open[t] < ha_close[t])              // enter_long = 1, green bar
exit_sig = xab(ema50,ema100)[t] AND (ha_close[t] < ema20[t])
           AND (ha_open[t] > ha_close[t])              // exit_long = 1, red bar, fires only when profitable (file literal)
exit_rsi = (rsi[t] > 70) AND (profit[t] > 0)           // "rsi_profit_sell", completed-bar RSI and close-based net profit
risk     = ROI ladder {"0": 0.05, "20": 0.04, "30": 0.03, "60": 0.01} (fraction, by position age in minutes);
           fixed stop at -10% (stoploss -0.1)
floor    = leading-window bars: rolling NaN comparisons false (see Required data)
```

- Trade events: `enter_long=1` on a bar printing the three-conjunct entry edge-state, `direction` long-only; `exit_long=1` on a bar printing the three-conjunct exit edge-state (honored only on profitable closes per the file's `exit_profit_only = True`); `"rsi_profit_sell"` on a positioned bar printing RSI above 70 while in profit. Each signal leg is evaluated on completed bars only; a book already positioned treats non-exit bars (including further entry edges) as hold-no-ops under the position pin below.
- Exact boundaries (pinned semantics): strict `>` on current bars with `<=` admitted on the prior bar per the standard `crossed_above` expansion — an EMA20 landing exactly on EMA50 on the current bar fires nothing, while touching from below on the prior bar still arms the edge; a Heikin-Ashi doji (`ha_open == ha_close`) satisfies neither color leg — it can neither complete an entry nor an exit; the RSI leg is strict on both conjuncts (`> 70`, `> 0`) — a bar with `rsi == 70` or exactly breakeven profit fires nothing. All preserved throughout.
- Mutual-exclusion proof (no tie-break pin required): entry needs `ha_open[t] < ha_close[t]` (strict green) while the signal exit needs `ha_open[t] > ha_close[t]` (strict red) on the same bar — the two color regions are strictly disjoint, so entry and signal-exit never co-print even if both cross edges fire on one bar. The RSI-profit leg cannot co-fire with entry either: on the entry bar the distance from the fill is zero, so close-based net profit is at most zero (negative under any positive fee), while the leg strictly requires profit above zero. ROI/stop cannot co-fire with entry on the entry bar for the same zero-distance reason. The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero short-leg tokens ship anywhere, and no `can_short` override exists (spot long-only engine default governs — disclosed default, never a file literal) — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the profit-gated conjunct signal exit, the RSI-70-plus-profit custom exit, the four-rung ROI ladder, and the −10% stop are the complete position-closing set (`use_exit_signal = True` and the file-literal `exit_profit_only = True`, so signal exits bank only profitable closes; ROI and stop legs are never profit-gated by construction; disclosed file literals, never defaults). No trailing (`trailing_stop = False` file literal; the two trailing config values are inert, fenced in Provenance), no time exit, no breakeven move — explicitly none further, not invented. The ROI clock is minutes-held per the Freqtrade `minimal_roi` time-key convention (`"60"`/`"30"`/`"20"`/`"0"`), preserved verbatim.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry edges as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying three-conjunct bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `open`/`high`/`low`/`close` (Heikin-Ashi transform plus three EMA seeds plus RSI-14, fixed non-negative offsets, plus the standard one-bar edge lookback — no forward reference) with no `shift` call in the file body because the single lookback lives inside the standard `crossed_above` edge under the file's own `process_only_new_candles = True` contract; the decision bar's own forming values are never read — the `custom_exit` current-candle read is the completed decision bar under the derived bar-close evaluation (see Execution assumptions), never a forming intrabar print. No volume read, no funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `5m` bars of BTCUSDT spot: `open`/`high`/`low`/`close` only (Heikin-Ashi transform on all four; EMA seeds and RSI on `close`). No bar `volume` read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (`informative_pairs` returns `[]`, census-verified).
- Single decision timeframe `5m` (source-native — the file prints `timeframe = '5m'`). One evaluation per completed bar (`process_only_new_candles = True` file literal); every window reads the decision bar's causal past only (plus the one-bar edge lookback); fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 110 five-minute bars held flat. Covers the 100-bar EMA seed (longest window), the 14-bar RSI seed, the one-bar edge lag, and the Heikin-Ashi recursion seed with margin. The file ships no `startup_candle_count` — quoted absence, never filled in from elsewhere. Coded behaviour underneath: rolling windows print NaN until seeded and every strict/inclusive NaN comparison is false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance spot, long side only (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed). Spot carries no funding leg, so the pinned-engine unverified-funding path is never entered.
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced BbandRsi, AwesomeMacd, EMASkipPump, ADXMomentum, CMCWinner, ASDTSRockwell, MACDStrategy-state, MACDStrategy-crossed, BinHV27, and strategy001 siblings use. The source's limit-GTC later-candle fills are scoped out by this derivation (disclosed, mirroring the admitted TD-Sequential record's identical limit-to-close derivation). No maker-touch, queue, or intrabar-path-dependent fill: entry, both signal exits, and the ROI/stop legs are all bar-close-evaluated; the custom RSI-profit leg is evaluated on the completed decision bar's RSI and close-based net profit under pinned house costs (its forming-candle read under the source engine is the same completed bar under this derivation — disclosed, never a second timing). The Signal mutual-exclusion proof leaves no ambiguous same-bar signal fill order, and any bar co-printing a signal exit with an ROI/stop leg closes the full unit flat either way, so no intrabar ordering assumption is needed.
- Interval precedent (disclosed, not assumed): `5m` is an already-admitted interval on `main` via the EMASkipPump, CombinedBinHAndCluc, ASDTSRockwell, MACDStrategy-state, MACDStrategy-crossed, BinHV27, strategy001, strategy002, strategy003, strategy004, and strategy005 records — no novel-interval confirmation is required for this frame. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs/precision (derived, disclosed): the source ships no sizing, capital, fee, margin, or funding concept — its ROI ladder and stop percentages are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees; the source declares no funding treatment at all, and the spot venue contributes no funding leg). Accounting is continuous (unquantized) research accounting as the derived model assumption: fills book exactly at the decision-bar close with zero added slippage, no lot-size/min-notional/rounding gate, and no fee-rounding claim — price/quantity precision, minimums, and live quantization are explicitly out of scope, never silently borrowed from any engine default. No hypothetical zero funding is reported as realized funding because there is no funding leg to report.
- Concurrency: at most one position per market at any time; the entry edge opens the full unit on a flat book; either signal exit, the RSI-profit leg, any ROI rung, or the stop closes it in full; re-entry after an exit needs only the next qualifying three-conjunct bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (143 lines: the EMA/Heikin-Ashi/RSI indicator block, the two `crossed_above` conjunct edges, the `custom_exit` RSI-profit leg, the `timeframe`/`minimal_roi`/`stoploss`/`exit_profit_only`/`order_types` literals, the empty `informative_pairs`, and the `Strategy001_custom_exit(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: rolling NaNs compare false (no early entry, no early exit). The 110-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired. The file ships no `startup_candle_count`, so the floor is purely a researcher pin, never misattributed.
2. Exact-touch rule fenced: the cross edges are strict on the decision bar while admitting previous-bar equality; a Heikin-Ashi doji satisfies neither color leg; the RSI-profit leg is strict on both conjuncts (`> 70`, `> 0`) — a bar with `rsi == 70` or exactly breakeven profit fires nothing. Strictness and inclusivity preserved throughout — disclosed, not smoothed.
3. Dead-import plumbing fenced: `Dict`, `List`, and `reduce` are imported and never called anywhere in the 143 lines — display/plumbing leftovers with no gate effect, never repaired into a signal. Zero `*Parameter` spaces, zero fitted values anywhere in this artifact (the lone `hyperopt` token is a prose comment, never code).
4. Inert-trailing fence: `trailing_stop = False` is the file literal — the `trailing_stop_positive`/`trailing_stop_positive_offset` values ship alongside but can never engage while trailing is off. Coded fact, disclosed, not deleted and not activated by repair.
5. Unkept-column fence: only the Heikin-Ashi `open`/`close` columns are kept — `ha_high`/`ha_low` never materialize (zero tokens), so no hidden high/low leg exists to repair or evaluate.
6. Custom-leg interaction fenced (moot by construction, not by engine choice): the RSI-profit leg's own code requires `current_profit > 0`, so whatever the engine's `exit_profit_only` gating does to custom exits, the observable behavior is identical — the leg fires only on profitable closes. No reviewer selection between engine readings is needed. Signal-exit legs are profit-gated by the file literal itself (admitted-setting precedent in the strategy005/SwingHighToSky/HLHB records); ROI and stop legs are never profit-gated, by construction.
7. Cousin records fenced as different constructions: the admitted `freqtrade-strategy001` pool-mate pins a different repository (`berlinguyinca/freqtrade-strategies@ae998ae`, path `strategy001.py`) with the same entry/exit triplets but a −30% stop (3× wider), `exit_profit_only = False` (loss exits honored — every losing trade lives a different lifecycle), no `custom_exit` leg, and no `order_types`/`process_only_new_candles` literals — moving the stop, flipping the profit gate, or adding the RSI-profit leg each changes trade events, so none is a trivial parameter re-tuning of it; the admitted `freqtrade-strategy005` pool-mate (volume-surge Fisher washout, different indicators and gates), `freqtrade-swinghightosky` pool-mate (CCI-RSI dual threshold, `15m`), `freqtrade-hlhb` pool-mate (EMA-RSI-ADX quad gate, `4h`), and the other `5m` siblings (different oscillators, different conjunctions, no custom leg) share only the lane's interval and risk-ladder conventions. Not a threshold re-tuning of any of them: changing any EMA lookback, dropping any conjunction leg, flipping any strictness or gating, removing the custom leg, or changing any ROI rung, the stop, or the frame would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `Strategy001.py`, `Strategy005.py`, and every `berlinguyinca/*.py` file are separate pins — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-spot market choice, the same-bar-close market fills (source limit-GTC timing scoped out), the single-unit/no-add/no-cooldown position pin, the 110-bar warmup floor (the file ships none), the framework-default readings (`can_short` absent → spot long-only), the standard `crossed_above` one-bar edge semantics, the completed-bar reading of the custom leg's current-candle reference, the continuous research-accounting precision assumption with zero added slippage, and house sizing/costs — all predeclared above. The `5m` frame, both conjunct-cross triplets with all their literals and strictness, the RSI-70-plus-profit custom leg, the profit-gated signal exits, the four-rung ROI ladder with the −10% stop, the disabled trailing, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: EMA(20/50/100) / RSI(14) / conjunct edges / HA color legs with pinned strictness / RSI-70-plus-profit custom leg / profit-gated signal exits / four-rung ROI ladder / −10% stop / single-unit long-only / `5m` BTCUSDT spot / same-bar-close fills are frozen.

- F1 — Custom-leg relevance: removing the RSI-profit leg (signal exits, ROI, stop unchanged) must not improve net expectancy; fail ⇒ the overbought-profit harvest adds nothing over the bare gated machine.
- F2 — Profit-gating relevance: honoring signal exits even at a loss (`exit_profit_only = False` twin, same legs otherwise) must not improve net expectancy; fail ⇒ the loss-hold construction adds nothing over immediate signal exits.
- F3 — Stop relevance: widening the fixed stop to −30% (strategy001 pool-mate level, same legs otherwise) must not improve net expectancy; fail ⇒ the tighter −10% backstop adds nothing over the wider disaster stop.

## Crypto portability

BTCUSDT Binance spot `5m` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. No volume field is consumed at all. No funding leg exists on the spot pin, so no funding portability claim is made or needed.

## Limitations

- The `5m` frame rides existing admission precedent (EMASkipPump, CombinedBinHAndCluc, ASDTSRockwell, MACDStrategy-state, MACDStrategy-crossed, BinHV27, strategy001–005 `5m`) — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- A position in a market whose slow cross never prints a profitable red confirmation is held until an ROI rung, the RSI-profit leg, or the −10% stop; a market that oscillates with cold RSI but no qualifying cross prints repeated hold-no-ops with no flat state to rest in (profit-gated exit profile, disclosed). There is no decay, chop, trend-loss, or further time exit — disclosed, not repaired.
- TA-Lib indicator internals (EMA seeding, RSI Wilder smoothing) and the standard `crossed_above` one-bar edge live in libraries outside the pinned file — pinned by call with explicit periods 20/50/100 and 14, not re-derived; exact reproduction inherits those libraries' seeding alongside the 110-bar floor.
- The `Dict`/`List`/`reduce` imports and the inert trailing config values are dead — nothing further to fence.
- No short leg, no cooldown, no time exit — all explicitly absent, never to be added by repair.
- Live/limit-order/queue behavior is out of scope: the source's limit-GTC timing is scoped out by the derived same-bar-close fills, and this record makes no claim about the source timing's performance.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/Strategy001_custom_exit.py
- https://github.com/freqtrade/freqtrade-strategies
