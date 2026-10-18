---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven RSI S00139 washout-cross SMA-gated long-flat on BTCUSDT 1h bars
created: 2026-10-19
updated: 2026-10-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-16
sources:
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/rsi_momentum_s00139.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven RSI S00139 washout-cross SMA-gated long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, `forven-adl-ema-cross`, `forven-atr-volume-breakout`, `forven-aroon-up-down-cross`, `forven-ema-rsi-pullback-reclaim`, `forven-double-bottom-neckline-break`, `forven-vwap-rolling-cross`, `forven-chaikin-mf-threshold-cross`, `forven-elder-ray-bull-power-cross`, `forven-adx-trend-pulse-reclaim`, `forven-dema-cross`, `forven-trix-signal-cross-zero-gate`, `forven-ultimate-oscillator-cross-gated`, `forven-bollinger-s00120-rsi-breakout`, `forven-three-bar-reversal-decline-gated`, `forven-atr-breakout-channel`, `forven-pivot-s1-bounce-r1-exit`, `forven-volatility-contraction-breakout`, `forven-connors-rsi-oversold-recross`, `forven-kdj-dual-gate`, `forven-heikin-ashi-color-change`, and `forven-bb-edge-fade-reclaim` records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`; verified as the repository HEAD via `git ls-remote` and a full shallow clone during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/rsi_momentum_s00139.py`.
- GitHub blob SHA at the pinned commit: `31061265e576825295332c8033e2b4d4e36c4cfc`, size 4809 bytes.
- Byte-identity check: the file retrieved from `raw.githubusercontent.com` at the pinned commit and from the clone at the pinned HEAD is 4809 bytes, 151 lines, SHA-256 `0af517f545a875969c9d5e1aa840491a0b82754fb9d7c0213f89e4c7857de19d`, identical to the GitHub blob (`git hash-object` reproduces `31061265…4e36c4cfc`) — the entire file was retrieved and inspected.
- Registration: the file self-registers via `STRATEGY_CLASS = RSIMomentumS00139Strategy` and the `STRATEGIES = [("S00139-BTC-RSI_MOMENTUM", RSIMomentumS00139Strategy, {"_asset": "BTC"})]` roster pin. This record pins the `S00139-BTC-RSI_MOMENTUM` roster leg. Repo-wide search for `RSIMomentumS00139Strategy` / `S00139-BTC` returns this file only — identity is unique.
- The file's own words (quoted for gate evidence, never extended): module docstring `RSI Momentum Strategy - S00139.` with `Strategy: BTC-RSI_MOMENTUM-S00139`, `Entry: Price above SMA and RSI crosses above rsi_oversold threshold (momentum reversal)`, `Exit: RSI crosses above rsi_overbought threshold or price below SMA`; `default_params` returns exactly `{ "rsi_period": 14, "rsi_oversold": 25, "rsi_overbought": 75, "sma_period": 20, "atr_period": 14, "leverage": 3.0 }`; `describe()` returns `BTC S00139: RSI Momentum. Enter long when price is above 20-period SMA and RSI crosses above 25 (oversold). Exit when RSI crosses above 75 (overbought) or price falls below SMA.`; `compatible_regimes` returns `{"TREND_UP", "RANGE_BOUND", "VOLATILE"}` (metadata never read by the signal path); `parameter_space()` returns `{ "rsi_period": (10, 20, 2), "rsi_oversold": (20, 35, 5), "rsi_overbought": (65, 80, 5), "sma_period": (15, 30, 5) }` (a documented search surface only — this record pins the defaults and runs no search). The docstring's `Based on backtest results: Sharpe 0.97 / Win Rate 68.6% / Profit Factor 1.18 / Max Drawdown 42.40% / Fitness 42.3` phrases carry no sample, window, trade count, or cost basis anywhere in the 151 lines — this record adopts no source-reported performance (see Evidence).
- Single decision path (verified by `def` census): the file defines one signal method, `generate_signal()` — no `generate_signals` vectorized twin exists anywhere in the file, no scalar delegate, no second decision logic exists to diverge. The `confidence` value and the `indicators` dict (`rsi`, `sma`, `atr_14`, `price_above_sma`) are diagnostic echoes — none ever enters any predicate.
- Out-of-file calls pinned (both resolved, both pure): line 16 `from forven.strategies.indicators import rsi as compute_rsi, atr` resolves through that module's PEP-562 `__getattr__` facade (`_FACADE_NAMES` includes `"rsi"` and `"atr"`, verified in `forven/strategies/indicators.py` at the pinned commit, blob `fdda8b77429e133372482e25cdff8ea31bd59b2a`) to `forven/scanner.py` `def rsi(series, period=14)` (line 1914: Wilder's RSI — `delta.clip` gain/loss with `ewm(alpha=1.0/n, adjust=False, min_periods=n)` smoothing, `rs = gain / loss.clip(lower=1e-9)`, `100 - 100/(1+rs)`) and `def atr(df, period=14)` (line 1946: true-range `rolling(period).mean()` over `high/low/close`). `scanner.py` at the pinned commit is 464565 bytes, blob `9a1d77b90bf214c03aa230a5f46775aab94748bd` (`git hash-object` verified this cycle — identical to the blob pinned by the admitted `forven-ema-rsi-pullback-reclaim` record). Both helpers are pure pandas over passed series/frames (no DB, no network, no global state in the quoted bodies). No other import ships beyond `pandas` and the local `BaseStrategy, Signal` base.
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` (blob `27508a2a6b8c546e21adefdb97fc0144fabf881b`, identical to the blob pinned by the admitted `forven-bb-edge-fade-reclaim` record) defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults, `direction: str = "long"` default, plus `__post_init__` coercion that refuses non-Boolean flags — flags arriving as strict booleans (as here, via `bool(...)`) pass through unchanged, and the `direction="long"` literal resolves to its book. The base further pins `supported_trade_modes == {"long_only"}` and `mirror_short_safe == False` — the long-only lane below is the class's own declared posture, not a researcher reinterpretation.
- Full-file token census (verified by search over the 151 lines this cycle): 2 `direction="long"` literals and zero `short` / zero `sell` (no short path anywhere); the sole `stop` token is the uncalled `def get_stop_loss` line fenced below — 0 `limit` / 0 `profit` / 0 `qty` / 0 `trail` (no order arguments, no live risk legs); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 3.0` default); 0 `volume` / 0 `funding` / 0 `mark_price` / 0 `request` / 0 `security` / 0 `barstate` / 0 `timeframe` in any order-gating line (the only `volume`-free OHLC reads are `close` for SMA/RSI plus `high/low/close` inside the diagnostic ATR call); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` / 0 `cooldown` (no position-aware state conditions any signal). The lone `position` substring in the file is the English word inside the `# Confidence based on RSI position` comment — no state semantic.
- Dead-stop fence (verified repo-wide at the pinned HEAD): `git grep -n "get_stop_loss"` over the entire tree returns exactly four hits — the commented template line in `STRATEGY_TEMPLATE.md`, the base docstring bullet, the base default (`return None`, "use trailing stop in daemon"), and this file's override. Zero callers exist in `backtest.py`, `execution_kernel.py`, `sizing.py`, or anywhere else. The override body (`signal.price - 3 * atr_14` when `atr_14` is present and positive, else `None`) is therefore uncalled dead code in the pinned engine — the effective coded posture is exits-only with no stop, recorded as explicitly disabled below, never presented as a live leg.
- Registry-collision fence: `TYPE_NAME = "rsi_momentum"` is shared with `builtin/rsi_momentum.py` (S012) and the strategy template; `registry.py:register_type` refuses shadowing (`already registered by ...; use a unique TYPE_NAME`). This record never keys identity by `TYPE_NAME` — it pins class plus file plus roster leg, all unique — so the collision changes no event.
- Single `df["..."]` read in the file body is `df["close"]` (line 71); the ATR helper additionally reads that frame's `high`/`low`/`close` columns. No `open`, no `volume`, no external feed is read by any order-gating line.

Pre-write dedup (2026-10-19): working-tree filename/content search for `rsi_momentum_s00139` / `RSIMomentumS00139Strategy` / `S00139` / `S00139-BTC-RSI_MOMENTUM` returns zero strategy records citing this source file. No closed `research/*` PR ever carried this file (merged Scout PRs #270–295 are WorldQuant/PVI/Mayer/PGO/Caporale-Plastun/wick/Ehlers/Caporale and twenty-five Forven files through bb-fade #295). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. The pool's nearest RSI neighbours are fenced as different constructions in Negative evidence 8 — none trades an SMA(20)-gated RSI(14) washout-cross entry at 25 with an overbought-cross-or-trend-loss dual exit at 75. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: an `RSI Momentum` system that buys a `momentum reversal` when price sits above its SMA and RSI crosses back above an oversold threshold, and exits when RSI crosses above an overbought threshold or price falls below the SMA. No behavioural, structural, or risk-premium channel is claimed anywhere in the 151 lines. The file ships docstring backtest phrases (`Sharpe: 0.97`, `Win Rate: 68.6%`, `Profit Factor: 1.18`, `Max Drawdown: 42.40%`, `Fitness: 42.3`) with no sample, window, trade count, or cost basis — this record claims no source-reported performance (see Evidence).

### Research interpretation

Washout-reclaim machine with a trend leash, long-only, edge-triggered entry with a dual-leg exit. Unlike midline-reclaim records (ema-rsi-pullback: RSI reclaims 45 inside an EMA stack — a pullback inside an intact uptrend), this system waits for a genuine washout: RSI(14) must print under 25 and cross back up, AND the close must already sit above SMA(20) — it buys exhaustion turns that have already recovered trend position, never dips still buried under the average. Unlike always-in oscillator records (drm-dynamic-rsi: adaptive-length RSI mirror crosses, two-sided always-in), exits here are one-sided profit-or-failure legs: RSI surging into overbought (cross above 75) banks the momentum extension, while any close back under the SMA admits trend failure — with no stop leg anywhere, the SMA leg is the sole capital guardrail. The coded consequence is a patient washout buyer: entries print only on bars where a sub-25 RSI proves itself reversed by the same bar's print above trend, and every position ends either on measured overheating or on demonstrated trend loss.

## Signal

Exact rule as pinned (any other RSI length, SMA length, threshold pair, strictness, exit leg, fill, frame, book, or ordering is a different, unpinned rule). All identifiers below are the program's own; the single `generate_signal` path is the single source of truth:

```text
sma20[t]  = mean(close[t-19 .. t])
rsi14[t]  = 100 - 100 / (1 + gain14[t] / max(loss14[t], 1e-9))   // Wilder, ewm alpha=1/14, min_periods=14
atr14[t]  = mean(TR[t-13 .. t])                                  // diagnostic only, never gates an order
entry     = (close[t] > sma20[t]) AND (rsi14[t-1] < 25) AND (rsi14[t] >= 25)
exit_     = ((rsi14[t-1] < 75) AND (rsi14[t] >= 75)) OR (close[t] < sma20[t])
guard     = len(df) < 22 -> flat/flat by coded rule (see Required data)
```

- Trade events: `entry_signal=True` with `direction="long"` on washout-cross-plus-trend bars; otherwise `entry_signal=False` with `exit_signal=bool(exit_)` on the same return. The SMA leg of the exit is a STATE level (while positioned and parked under the SMA, it stays true every bar — close-and-hold-flat); the RSI leg is an edge (fires only on the cross-into-overbought bar).
- Exact boundaries (pinned semantics): entry needs price STRICTLY above the SMA (`>` — a close landing exactly on the average fires nothing) with an RSI cross that admits equality on the current bar (`>= 25`) but demands strict sub-threshold history (`< 25`). The RSI exit leg mirrors this (`< 75` then `>= 75` — a close landing exactly on 75 from below exits); the SMA exit leg admits no equality (`<` — a close exactly on the average holds). At zero variance the Wilder divisor is clipped (`1e-9`), never divided by zero — fenced, not repaired.
- Same-bar both-legs ordering (predeclared researcher pin — the source returns both flags with no ordering): a bar satisfying BOTH legs (a one-bar RSI surge from below 25 to at/above 75 with the close above the SMA — entry true and RSI-exit leg true together; the SMA-exit leg is mutually exclusive with entry by strictness) resolves by pre-bar book — a flat book OPENS long at the close (the exit leg is a no-op without a position); a positioned book CLOSES to flat at the close with NO same-bar reopen (re-entry re-arms on the next qualifying washout-cross bar). Single-leg bars follow their leg; no-leg bars hold. No hidden Hummingbot default is relied upon.
- Direction: long-only with an explicit pre-first-signal flat state plus the coded guard flat. Zero `short`/`sell` tokens ship anywhere; the base class pins `supported_trade_modes == {"long_only"}` and `mirror_short_safe == False` — a two-sided reading would contradict the file and its base. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the overbought-cross / below-SMA pair is the sole position-ending path. Stop loss, take profit, trailing-stop order, and time limit are absent from the effective engine behaviour and recorded as explicitly disabled, not as defaults to be assumed — the file's `get_stop_loss` override (entry minus 3× ATR) is quoted above and fenced as uncalled dead code at the pinned commit (repo-wide grep: zero callers), so no reviewer repair may promote it into a live leg. `confidence` (`min(1, (rsi-25)/10)` on entry bars, else `0.0`) and the `indicators` dict are diagnostic — neither conditions any order line.
- Position rule (predeclared researcher pin): single-unit; a positioned book treats further entry-only bars as hold-no-ops (no pyramiding, no averaging); a flat book treats exit-only legs as no-ops; re-entry re-arms on any qualifying washout-cross bar after any exit subject to the both-legs rule above (no cooldown specified — explicitly none, not invented). Pre-first-signal and guard bars are flat by coded/record rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar OHLC (`close` for SMA/RSI/comparisons; `high/low/close` inside the diagnostic ATR call) with fixed non-negative offsets — no `volume`, no funding/OI/mark-price read, no `request.*`, `security()`, `timeframe*`, `barstate.*`, session/calendar call, or stop/limit order argument anywhere in the order-gating path (verified by the census above returning zero matches). The Wilder RSI uses `ewm(min_periods=14)` and the SMA/ATR use trailing rolling means — deterministic given the pinned pandas semantics; the scanner docstring states the RSI matches TradingView/Binance `ta.rsi`, disclosed as a claim, never independently verified here. The `compatible_regimes` set is metadata never read by the signal path (which takes only `df`/`params`); treating the label as a gate would be a different, unpinned rule.

## Required data

- Completed `1h` bars of BTCUSDT: `high`/`low`/`close` ONLY — SMA(20) and Wilder-RSI(14) over closes for the gating path, plus the true-range ATR(14) diagnostic. No bar `open`/`volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request` / 0 `security` anywhere; 0 `timeframe` tokens in the whole file).
- Single decision timeframe `1h` (researcher pin, disclosed — the file names no timeframe). One evaluation per completed bar; all windows (the 20-bar SMA, the Wilder RSI seed, the 14-bar ATR, the one-bar RSI edge lookback) read the decision bar and its causal past only — the ATR's `close.shift()` is a one-bar causal lag, no shift tricks, no future reference; fills land on the decision bar's own close (`price=round(curr_close, 4)`, pinned derived rule).
- Warmup: the source ships its own length guard (`len(df) < sma_period + 2`, i.e. 22 bars at defaults — the file comment says "+ 1" but the code reads `+ 2`; the code governs). This record adopts a 22-bar record-rule warmup with pre-warmup bars flat (no derivation — the coded guard already holds them flat with `entry=False, exit=False`): at 22+ bars the SMA seed (20), the RSI `min_periods=14` stabilization, the ATR seed (14), and the one-prior-bar edge read are all defined. Before that, `NaN` comparisons are `False` by construction, so no leg can fire early — coded behaviour, disclosed. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice of the `S00139-BTC-RSI_MOMENTUM` roster leg — the source roster pins `_asset BTC` for this leg; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills (`price=round(curr_close, 4)` — the decision bar's own close), compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same lane primitive the twenty-five admitted Forven-sibling records use. No maker-touch, queue, or intrabar-path-dependent fill: the only legs are bar-close-evaluated market entry/exit orders, sequenced by the predeclared both-legs ordering rule (see Signal) — no ambiguous same-bar fill order is left to the engine.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its `leverage: 3.0` default is replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position at any time; washout-cross bars while positioned hold without adds; either exit leg closes the open side in full; re-entry after an exit needs only the next qualifying washout-cross bar subject to the both-legs rule (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (151 lines: module docstring with the washout-cross rule, `default_params` with the 14/25/75/20/14 set, the SMA gate, the strict washout-cross entry, the dual-leg exit, the `direction="long"` literals and the `round(curr_close, 4)` price echo, the `S00139-BTC-RSI_MOMENTUM` roster pin, plus the quoted-but-uncalled ATR-stop override). It ships docstring backtest phrases with no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Guard behaviour fenced: before the 22nd bar the coded guard returns flat/flat; leading-`NaN` legs compare false by construction, so every pre-warmup bar is flat twice over — disclosed, not repaired. A shorter warmup would admit `NaN`-flat bars only (never spurious events), but the 22-bar floor is still pinned so the first trusted bar has fully defined windows.
2. Exact-touch rule fenced: a close landing exactly on the SMA (`==`) is NEITHER above (no entry) NOR below (no SMA exit) — it holds by strictness; an RSI print landing exactly on 25/75 from the qualifying side satisfies the `>=` half and fires the corresponding edge. Strictness is preserved throughout — disclosed, not smoothed.
3. Both-legs surge fenced: a one-bar RSI surge from below 25 to at/above 75 with the close above the SMA fires both legs and resolves by the predeclared book rule (flat→long, positioned→flat with no same-bar reopen) — disclosed researcher pin, not source semantics. The patience cost — banking nothing of the surge on a positioned book — is the prescribed posture, disclosed as a principal limitation.
4. Overbought-loiter fenced: while positioned with RSI parked at/above 75 WITHOUT a fresh cross (entered earlier, RSI drifted up), the RSI exit leg stays false — only a fresh cross-into-overbought bar or a close under the SMA ends the position. There is no level-hold exit on the RSI leg by construction; a melt-up that never prints a sub-75 prior bar rides until the SMA breaks — disclosed, not repaired.
5. Below-SMA loiter fenced: while positioned and parked under the SMA, the SMA exit leg stays true every bar — the engine closes on the first such bar and later legs are flat-book no-ops. No "exit signal missed" state can strand a position on this leg.
6. Zero-variance fenced: flat closes pin gain and loss at zero; the Wilder divisor is clipped (`1e-9`), RSI reads `0.0`-adjacent rather than `NaN` — entry strictly impossible (RSI cannot reach 25 from flat tape without an up-move, and the SMA gate needs dispersion first); exit legs read false. No division by zero exists anywhere — disclosed, not repaired.
7. Confidence/ATR diagnostic fenced: `confidence` and the full `indicators` dict (including `atr_14`) never enter any predicate — an engine that skips computing both reaches identical events. The ATR series exists in the file only to feed the uncalled stop override and the echo dict.
8. Cousin records fenced as different constructions (none trades an SMA-gated RSI washout-cross at 25 with an overbought-cross-or-trend-loss dual exit): the admitted forven-ema-rsi-pullback-reclaim sibling reclaims RSI through the 45 midline inside a dual-EMA(12/34) stack with a close-above-fast filter and exits on rollover under 62 or slow-EMA loss with no stop concept (midline-reclaim trigger, different gate, different exit pair, SOL roster); the admitted drm-dynamic-rsi-momentum record adapts its own RSI length (20–50) to price/momentum correlation and trades 30/70 mirror crosses two-sided always-in (adaptive smoothing, different thresholds, different direction handling); the admitted forven-connors-rsi-oversold-recross sibling trades a 3-component ConnorsRSI composite (different oscillator entirely); the admitted chartart-bollinger-rsi sibling needs a joint RSI(6)-50 turn AND a 200-bar rail reclaim, two-sided always-in (joint condition, different lookback, different direction handling); the admitted forven-bollinger-s00120-rsi-breakout sibling breaks the UPPER Bollinger rail while RSI(14) reads oversold (breakout-plus-gate, different trigger family, BNB roster). Not a threshold re-tuning of any of them: moving the washout line to 30/45, dropping the SMA gate, or converting the 75-cross exit to a rollover would each be a different, unpinned rule — none is admitted here.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-`1h` market choice, the same-bar-close fills, the position-state pin, the both-legs ordering, and house sizing/costs — all predeclared above; the 22-bar guard floor is source-verbatim code, not an adoption. The 14/25/75/20 construction, the strict washout-cross entry, the dual-leg exit, the long-only stance, and the no-stop/no-target/no-trailing/no-time-exit/no-cooldown stance are source-verbatim effective behaviour. The Wilder-ewm RSI and trailing-mean ATR arithmetic are the file's (plus its pinned scanner passengers') own execution semantics.
10. The RSI length, the 25/75 pair, the SMA length, the strict gate, the washout-cross entry, the dual exit, the long-only stance, and the no-stop stance are pinned, not removed: re-tuning any length/threshold, softening strictness to touches, converting an edge to a level (or the reverse), adding a stop/target/filter/cooldown/gate, adding a short leg, or sizing partially instead of single-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 14/25/75/20 construction as written / strict SMA gate / washout-cross entry / dual-leg exit / both-legs ordering / single-unit long-only / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Gate relevance: dropping the SMA gate (pure RSI washout-cross entry, same dual exit) must not improve net expectancy; fail ⇒ the coded trend gate adds nothing over its ungated twin.
- F2 — Exit relevance: replacing the dual exit with the SMA leg alone (same entry) must not improve net expectancy; fail ⇒ the 75-cross overheating leg adds nothing over the trend-loss leg.
- F3 — Oscillator relevance: trading the identical gate-plus-cross structure on a 14-bar CCI through symmetric 25/75-style washout lines (same entry/exit/pins, Wilder RSI replaced) must not reproduce-or-beat net expectancy; fail ⇒ the Wilder-RSI construction adds nothing over its mean-deviation twin and the record is a label variant of one.

## Crypto portability

Direct for the long leg on either venue type: single-venue BTCUSDT perpetual `1h` completed bars with `high`/`low`/`close` fields only. No session calendar (crypto trades continuously; the 20-bar SMA, the Wilder seed, the 14-bar ATR, and the one-bar edge lookback need no session-gap semantics), no corporate actions, no dividends, no funding/OI reads, no cross-venue state. 24/7 continuity means every lookback bar is always the immediately prior print — no weekend-gap discontinuity to normalize. Tick-size rounding follows the venue; the record's 4-decimal price echo is display precision only and changes no event. Leverage/margin follow the house overlay, not the source's bare `3.0` default. The long-only book expresses identically on spot (no margin needed) and on perpetual under the house overlay; it is the same rule on both.

## Limitations

- The source ships no fill-timing flag: same-bar-close fills are a disclosed researcher derivation, never a source claim. An engine filling at next-open would print different event prices on identical bars.
- The source ships no timeframe: the `1h` frame is a disclosed researcher choice. Other frames re-tune nothing in the rule text but produce different event streams; they are different, unpinned evaluations.
- The source ships no costs: all economics come from the house overlay. No realized-funding claim is made; modeled funding is never reported as canonical.
- The source ships no position semantics and no both-legs ordering: single-unit bookkeeping with the flat→long / positioned→flat same-bar rule is a predeclared researcher pin, never a source claim; the Forven engine's own ordering may differ — this record is not evidence of source-engine behaviour.
- The file's `get_stop_loss` override is uncalled dead code at the pinned commit (repo-wide grep evidence above); the effective posture is exits-only with no stop. Any engine that wires the override into live fills would print different event streams; that wiring is a different, unpinned rule.
- The docstring backtest phrases (`0.97` Sharpe and companions) are adopted by no section of this record: they ship without sample, window, trade count, or cost basis and cannot satisfy the traceable-provenance rule — stated plainly so no reader mistakes them for evidence.
- Washouts that never cross back above 25 never trade; melt-ups that never print a fresh sub-75 prior bar ride until the SMA breaks (Negative evidence 4); a tape that grinds along the SMA without a strict side prints nothing.
- The RSI follows the pinned scanner's Wilder-ewm arithmetic (`min_periods=14`), not necessarily any other platform's RSI seeding — cross-platform values differ slightly in early bars by construction; this record claims only the file's own arithmetic.
- Not independently reproduced; no live, Paper, Testnet, or profitability claim of any kind. Admission is engineering capability only.

## Implementation status

not-implemented. No dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record; downstream materialization follows the `IMPLEMENTATION_NEEDED` route without revisiting HB_READY admission.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. Any future authorization requires a separate downstream decision outside this repository's admission scope.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/rsi_momentum_s00139.py
- https://github.com/judder659/Forven
