---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade CofiBit fast-stoch edge EMA-rail ADX-gated long-flat on BTCUSDT 5m bars
created: 2026-10-21
updated: 2026-10-21
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2018-06-27
sources:
  - https://github.com/berlinguyinca/freqtrade-strategies/blob/ae998aec37cd4c83b8f0e512d9ea44edc7726351/user_data/strategies/berlinguyinca/CofiBitStrategy.py
  - https://github.com/berlinguyinca/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade CofiBit fast-stoch edge EMA-rail ADX-gated long-flat on BTCUSDT 5m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/berlinguyinca/freqtrade-strategies (open-source Freqtrade strategy collection; the original upstream of the lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, `freqtrade-asdts-rockwell`, `freqtrade-macd-cci-dip-state`, `freqtrade-strategy001`, `freqtrade-strategy002`, `freqtrade-strategy003`, `freqtrade-strategy004`, `freqtrade-hlhb`, `freqtrade-quickie`, and `freqtrade-simple` records — this is only its sixteenth record).
- Pinned commit SHA: `ae998aec37cd4c83b8f0e512d9ea44edc7726351` (committed `2018-06-27T17:27:40Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/berlinguyinca/CofiBitStrategy.py`.
- GitHub blob SHA at the pinned commit: `830317009067d20ddae8e6b349b9f24af12977d5`, size 2690 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 2690 bytes, 80 lines, SHA-256 `753c6d0f4be4397a530472a047050b6c825c83f32c237e2bbefb86c9b7686143`, identical to the GitHub blob (`git hash-object` reproduces `83031700…12977d5`) — the entire file was retrieved and inspected.
- Registration: the file defines class `CofiBitStrategy(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, every other `user_data/strategies/berlinguyinca/*.py` sibling is a different pin with different constants — this record pins ONLY the CofiBit literals below, and no reviewer repair may substitute a sibling constant.
- The file's own words (quoted for gate evidence, never extended): `ticker_interval = '5m'`; `minimal_roi = { "40": 0.05, "30": 0.06, "20": 0.07, "0": 0.10 }`; `stoploss = -0.25`; entry is the five-way AND of `open < ema_low`, `crossed_above(fastk, fastd)`, `fastk < 30`, `fastd < 30`, `adx > 30`; exit is the three-way OR of `open >= ema_high`, `crossed_above(fastk, 70)`, `crossed_above(fastd, 70)`. The docstring attribution (`taken from slack by user CofiBit`) is lineage only — no performance, sample, window, trade count, or cost basis ships anywhere in the 80 lines.
- Out-of-file calls pinned (all resolved by name, all standard defaults): `ta.STOCHF(dataframe, 5.0, 3.0, 0.0, 3.0, 0.0)` (explicit fastk_period 5 / fastd_period 3 / matype 0 pinned by call — `fastk`/`fastd` live every leg); `ta.EMA(dataframe, timeperiod=5, price='high'/'close'/'low')` (all explicit 5 — `ema_high` lives the exit leg, `ema_low` lives the entry leg, `ema_close` computed but never read: dead column, fenced below); `ta.ADX(dataframe)` (TA-Lib default `timeperiod=14` pinned by call — lives the entry gate). No volume column is read by any indicator in the gating path (STOCHF reads `close` windows; EMA/ADX read `high`/`low`/`close` only). No DB, no network, no `request.*`, no `security()` in the file.
- Full-file token census (verified over the 80 lines this cycle): 0 `short` (case-insensitive — no short leg, no short identifier anywhere); 0 `volume` (no volume column is ever named or read); 0 `resample` / 0 `informative` / 0 `request` / 0 `security` / 0 `typical_price` (no typical-price basis anywhere — the rails are raw high/low EMAs); 0 `shift` (the only lags are the two-bar `crossed_above` edges — fixed one-bar offsets, no forward reference); 3 `crossed_above` (the entry fastk/fastd edge plus the two scalar-70 exit edges — the only edge primitives); 0 `fillna` / 0 `ffill` / 0 `interpolate` (no NaN patching anywhere — strict NaN comparisons simply stay false); 1 `stoploss` attribute (`-0.25`) and 1 `minimal_roi` (the four-rung ladder) as the only risk legs; 0 shipped `trailing`; 0 `startup_candle_count` (the record's 60-bar floor is a predeclared researcher pin, never a file semantic); 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop); 0 `hyperopt` / 0 `hp.` / 0 `*Parameter` (no tuning surface at all); 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic); 5 `buy` / 3 `sell` (old-interface `populate_buy_trend` / `populate_sell_trend` plumbing plus the `buy`/`sell` column writes — mapped to enter-long/exit-long framework reading below, never a second leg); 0 `macd` / 0 `rsi` / 0 `cci` / 0 `mfi` / 0 `sar` / 0 `fisher` / 0 `bb` (none of the lane's usual oscillators appears anywhere).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. The file is causal as written (no full-sample scalar, no repainting primitive, no multi-timeframe merge, no external package — no repair site exists). Researcher-declared adaptations are exactly four: (1) research market `BTCUSDT` (the source names no market); (2) completed-bar decisions with same-bar-close market fills; (3) single-unit/no-add/no-cooldown position pin plus a 60-bar researcher warmup pin (covers the ADX14 seed, the STOCHF seed, the EMA5 seeds, and the two-bar `crossed_above` edges with margin); (4) the house cost/capital overlay replaces the absent source economics. Every threshold, every lookback, all three `crossed_above` edges, the EMA rails, the ROI ladder, and the stop are untouched.

Pre-write dedup (2026-10-21): working-tree filename/content search for `CofiBit`, `ema_high`, `ema_low`, and `STOCHF` returns no record combining a fast-stochastic oversold edge with EMA high/low price rails and an ADX gate — the `STOCHF` hits are different constructions (strategy004's hand-rolled dual-stack recross with CCI washout and volume floor; strategy003's level-state `fastd > fastk` inside an RSI/Fisher/MFI washout; strategy002's slow-STOCH level inside a hammer-pattern entry; the forven/slow-stochastic records' raw-FastK recross systems). No record conjoins `open < EMA5(low)` with a `crossed_above(fastk, fastd)` oversold edge and `ADX > 30`, exited by `open >= EMA5(high)` OR stoch-70 edges. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas) trades a fast-stoch/EMA-rail/ADX system. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the bar where price opens beneath its own 5-bar low-rail while the fast stochastic turns up from oversold (fastk crossing above fastd with both under 30) inside a certified trend (ADX above 30) — and stand aside to flat when price reclaims its 5-bar high-rail or either fast stochastic limb crosses up through 70, with a stepped take-profit ladder (10% inside 20 min, 7% inside 30, 6% inside 40, 5% beyond) and a −25% stop behind every position. No behavioural, structural, or risk-premium channel is claimed anywhere in the 80 lines.

### Research interpretation

Oversold-turn buyer inside certified trend, long-only, with price-rail discipline on both sides. Unlike dip systems that buy any cheap print, two permission keys are required at once: the oscillator must be turning (edge, not level — a merely-low-but-flat stochastic prints nothing) AND the trend must be certified (ADX above 30 — chop prints nothing even on a perfect turn). Unlike pure oscillator-turn records, price itself holds a veto through the EMA rails: the entry bar must open under the low-rail (no chasing prints that already reclaimed the band), and any reclaim of the high-rail exits immediately even if the oscillators stay cool. The exit is deliberately asymmetric to the entry: it fires on the first sign of heat (either limb crossing 70) or rail-reclaim, never waiting for a cross back down. The coded consequence is a buyer of trend-certified oversold turns that harvests rail-reclaims, early overheating, laddered scalp profits, or the wide stop.

## Signal

Exact rule as pinned (any other stochastic period, EMA length, ADX length, threshold, edge construction, ROI rung, stop, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own:

```text
fastk[t], fastd[t] = TA-Lib STOCHF(close windows; fastk_period 5, fastd_period 3, matype 0)
ema_high[t] = EMA5(high); ema_low[t] = EMA5(low); ema_close[t] = EMA5(close, dead)
adx[t]      = TA-Lib ADX(high/low/close, 14)
entry = (open[t] < ema_low[t]) AND crossed_above(fastk, fastd)[t]
        AND (fastk[t] < 30) AND (fastd[t] < 30) AND (adx[t] > 30)   // buy = 1
exit_sig = (open[t] >= ema_high[t])                                // sell = 1
        OR crossed_above(fastk, 70)[t] OR crossed_above(fastd, 70)[t]
risk = stepped take-profit ladder minimal_roi {"40":0.05,"30":0.06,"20":0.07,"0":0.10};
       fixed stop at -25% (stoploss -0.25)
guard = leading-window bars: NaN comparisons false (see Required data)
```

- Trade events: `buy=1` on any bar printing the five-conjunct state, `direction` long-only; `sell=1` on bars printing any of the three exit arms. The `crossed_above` legs are edge prints (true only on the crossing bar); the level legs persist while true — close-and-hold-flat. Old-interface `buy`/`sell` columns read as enter-long/exit-long (disclosed framework reading, never a second leg).
- Exact boundaries (pinned semantics): strict throughout (`<`, `>`, `>=` exactly as coded — an open exactly on `ema_low`, fastk/fastd exactly on 30, ADX exactly on 30 fires nothing on that conjunct; the exit's `open >= ema_high` fires on exact touch). The `30` / `70` / `5` / `14` literals are never tuned here. The three `crossed_above` edges ride the same verified `qtpylib.crossed_above` primitive the admitted HLHB sibling evidenced (`freqtrade@3d31927` forwarding to `technical@9c6d8fd`, scalar-broadcast inclusive edge) — the two scalar-70 arms use the same primitive with a broadcast threshold, never a hand-rolled comparison.
- Same-bar co-print pin (near-impossible, resolved by position pin — disclosed, not repaired): entry needs `fastk < 30` and `fastd < 30` while the stoch exit arms need a cross above 70 on the same bar — arithmetically exclusive on the oscillator legs. Entry needs `open < ema_low` while the rail exit needs `open >= ema_high` — exclusive unless the two period-5 high/low EMAs momentarily invert. No engine ordering is invented: under the single-unit position pin, a flat book treats any residual co-print bar as entry (the exit leg needs a position and is a no-op without one — no same-bar round-trip), while a positioned book treats it as exit-close. ROI/stop legs start at zero distance on the entry bar — disclosed, not repaired.
- Direction: long-only. Zero `short` tokens ship anywhere — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the three-arm signal exit, the four-rung ROI ladder, and the −25% stop are the complete position-closing set (old-interface `use_sell_signal = True` / `sell_profit_only = False` framework-default reading — exits fire even at a loss; disclosed defaults, never file literals). The ladder reads Freqtrade-native: rung `{"0": 0.10}` demands 10% from the entry minute, stepping down to 5% after 40 minutes — quoted verbatim, never smoothed. No trailing, no time exit, no breakeven move — explicitly none, not invented.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying five-conjunct bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar OHLC (`open` for the rail comparisons, `high`/`low`/`close` for EMA/ADX, `close` for STOCHF) with fixed non-negative offsets (trailing windows plus the two-bar `crossed_above` edges — no forward reference) — no volume, funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, informative merge, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path. The `open` legs read the completed bar's own open — point-in-time available at the decision, never intrabar. Freqtrade engine column semantics (`buy`/`sell` per completed bar) are the file's own framework contract.

## Required data

- Completed `5m` bars of BTCUSDT: `open` for the rail comparisons, `high`/`low`/`close` for the EMA5 rails and ADX14 path, `close` for the STOCHF path. No volume, funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `5m` (source-native — the file prints `ticker_interval = '5m'`). One evaluation per completed bar; every window reads the decision bar and its causal past only; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 60 five-minute bars held flat (~5 hours). Covers the ADX14 seed (~28 bars effective), the STOCHF seed, the EMA5 seeds, and the two-bar `crossed_above` edges with margin. Coded behaviour underneath: TA-Lib seeds print NaN until windowed (every strict NaN comparison false — no leg can fire early; no `fillna` exists to smear them). No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, signal exit, and ROI/stop legs are all bar-close-evaluated; the Signal co-print rule leaves no ambiguous same-bar fill order to the engine beyond the disclosed position pin.
- Interval precedent (exact, disclosed): exact-`5m` PASS records already sit on `main` (the admitted ASDTSRockwellTrading MACD-polarity state, MACDStrategy MACD-CCI dip-state, strategy002 hammer-gated oversold, strategy003 RSI-Fisher-MFI washout, strategy004 ADX-gated CCI washout, Quickie TEMA-slope, and Simple MACD-BB-RSI records — all `5m` Freqtrade-sourced long-flat) — this record rides the same specified single-frame completed-bar `5m` Binance candle path, not an assumed one. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the same specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI ladder and stop percentage are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the five-conjunct entry opens the full unit on a flat book; any exit arm, any ROI rung, or the stop closes it in full; re-entry after an exit needs only the next qualifying entry bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (80 lines: the STOCHF/EMA/ADX indicator block, the five-conjunct entry with its edge-plus-rail-plus-ADX legs, the three-arm exit, the `ticker_interval`/`minimal_roi`/`stoploss` literals, and the `CofiBitStrategy(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: TA-Lib rolling seeds print NaN until windowed (every strict NaN comparison false — no early entry, no early exit; no `fillna` exists to smear seeds forward). The 60-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired.
2. Exact-touch rule fenced: strict `<`/`>` fires nothing on equality on the entry legs; the exit rail fires on exact touch (`>=`) exactly as coded. A fastk/fastd exactly on 30 or ADX exactly on 30 holds — disclosed, not smoothed.
3. Co-print arithmetic fenced (near-impossible, resolved — disclosed, not repaired): oscillator legs make entry-vs-stoch-exit co-prints arithmetically exclusive; only a momentary EMA high/low inversion could co-print the rail legs with entry. The position pin resolves any residual (flat → enter, positioned → exit-close, never a same-bar round-trip). ROI/stop legs start at zero distance on the entry bar — disclosed, not repaired.
4. Zero-variance fenced: flat tape pins stochastics midscale (failing the sub-30 conjuncts), ADX toward 0/NaN (failing `> 30`), and EMA rails onto the flat line (the `open < ema_low` leg fails on exact equality). No division by zero exists anywhere in the gating path (all legs are comparisons or library-internal rolling arithmetic) — disclosed, not repaired.
5. Dead-column plumbing fenced: `ema_close` is computed every bar and read nowhere — display/plumbing leftover with no gate effect; this record never conditions on it and no reviewer repair may promote it into a leg. Zero `hyperopt` tokens ship anywhere — no tuning surface exists to repair into a signal.
6. Derivation-effect fenced: this record computes no behaviour differently from the file's letter — the four adaptations are market choice, fill convention, position/warmup pins, and house economics only. Every threshold, lookback, edge, rail, ROI rung, and the stop are verbatim; no reviewer invention is needed to execute it.
7. Cousin records fenced as different constructions (none conjoins a fast-STOCHF oversold edge with EMA high/low price rails and an ADX gate): the admitted strategy004 sibling trades an ADX-gated CCI washout with a hand-rolled dual-STOCHF recross, a volume floor, and a regime-collapse exit on `5m` (no `crossed_above` primitive, no price rails, no scalar-70 exit edges); the admitted strategy003 sibling trades an RSI/Fisher/MFI triple washout with an EMA-regime OR-arm on `5m` (oscillator level-states, never an oversold edge; SAR/Fisher exit, never a rail reclaim); the admitted strategy002 sibling buys a hammer-pattern-plus-band-penetration entry on `5m` (pattern trigger with slow-STOCH level, never a fast-stoch edge or ADX gate); the admitted forven-stochastic-k20 sibling trades a raw-FastK 20-recross with a dual exit on `1h` (no ADX, no EMA rails, different exit); the admitted freqtrade-hlhb sibling conjoins an RSI-50 edge with an EMA5/10 edge plus ADX>25 on `4h` (edge-cross trend construction with trailing stop, never an oversold stoch turn or rail discipline). Not a threshold re-tuning of any of them: dropping the ADX gate, either sub-30 conjunct, the edge primitive, or either rail would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: every other `berlinguyinca/*.py` sibling is a separate pin — its constants must never be substituted into this record.
9. Derivation boundary fenced: the non-source-native behaviours in this record are exactly the four declared adaptations (BTCUSDT market choice, same-bar-close fills, single-unit/no-add/no-cooldown position pin with 60-bar warmup floor, house sizing/costs) — all predeclared above. The `5m` frame, the five-conjunct entry with every literal and edge, the three-arm exit, the ROI ladder, the −25% stop, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: five-conjunct entry / all lookbacks, thresholds, edges, rails / three-arm exit / ROI ladder / −25% stop / single-unit long-only / `5m` BTCUSDT / same-bar-close fills are frozen.

- F1 — ADX-gate relevance: dropping the `adx > 30` conjunct (same stoch-edge-plus-rail entry, same exit/risk) must not improve net expectancy; fail ⇒ the trend-certification gate adds nothing over the ungated turn-plus-rail state.
- F2 — Rail-veto relevance: dropping the `open < ema_low` entry conjunct (same stoch-edge-plus-ADX entry, same exit/risk) must not improve net expectancy; fail ⇒ the low-rail price veto adds nothing over the pure oscillator-turn state.
- F3 — Rail-exit relevance: replacing the three-arm signal exit with ROI/stop-only exits (same entry, same risk) must not improve net expectancy; fail ⇒ the rail-reclaim/overheating exit adds nothing over fixed risk alone.

## Crypto portability

BTCUSDT Binance perpetual `5m` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count, portable across 24/7 crypto tape. Only standard OHLC candle fields are read (`open` for rails, `high`/`low`/`close` for EMA/ADX, `close` for STOCHF); no exotic feed is required. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- TA-Lib STOCHF/EMA/ADX internals and the `qtpylib.crossed_above` edge arithmetic live in their libraries outside the pinned file — pinned by call with defaults/explicits, not re-derived; exact reproduction inherits those modules' seeding and rolling semantics alongside the file-local column wiring, under the disclosed 60-bar floor.
- `ema_close` is computed and ignored — a reader must not mistake it for a gate; it gates nothing.
- The STOCHF call's trailing `3.0, 0.0` literals repeat the STOCH-style slots verbatim from the file — quoted as written, never reinterpreted; effective behaviour is the file's own call, not a re-derived parameter set.
- No trailing, no breakeven, no time exit beyond the ROI ladder, no short leg, no cooldown — all explicitly absent, never to be added by repair.
- The Slack-user attribution is lineage only — no rule in this record is sourced from chat; every literal comes from the pinned `.py` file.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/berlinguyinca/freqtrade-strategies/blob/ae998aec37cd4c83b8f0e512d9ea44edc7726351/user_data/strategies/berlinguyinca/CofiBitStrategy.py
- https://github.com/berlinguyinca/freqtrade-strategies
