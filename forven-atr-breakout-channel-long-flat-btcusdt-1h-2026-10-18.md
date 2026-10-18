---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven ATR breakout symmetric channel long-flat on BTCUSDT 1h bars
created: 2026-10-18
updated: 2026-10-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-16
sources:
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/atr_breakout.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven ATR breakout symmetric channel long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, `forven-adl-ema-cross`, `forven-atr-volume-breakout`, `forven-aroon-up-down-cross`, `forven-ema-rsi-pullback-reclaim`, `forven-double-bottom-neckline-break`, `forven-vwap-rolling-cross`, `forven-chaikin-mf-threshold-cross`, `forven-elder-ray-bull-power-cross`, `forven-adx-trend-pulse-reclaim`, `forven-dema-cross`, `forven-trix-signal-cross-zero-gate`, `forven-ultimate-oscillator-cross-gated`, `forven-bollinger-s00120-rsi-breakout`, and `forven-three-bar-reversal-decline-gated` records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/atr_breakout.py`.
- GitHub blob SHA at the pinned commit: `8d1dacb66374e2c3776f96c1c308af5904e77d76`, size 4260 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 4260 bytes, 143 lines, SHA-256 `443bacf1ea304e486e73c97c3eeb1efc88ea9059075cb0a79abaef73dda05b61`, identical to the GitHub blob (`git hash-object` reproduces `8d1dacb6…77d76`) — the entire file was retrieved and inspected.
- Registration: the file self-registers via `STRATEGY_CLASS = ATRBreakoutStrategy`, `TYPE_NAME = "atr_breakout"` (line 12), and the `STRATEGIES = [("PREBUILT-ATR-BREAKOUT", ATRBreakoutStrategy, {"_asset": "BTC"})]` roster pin (lines 141–143).
- The file's own words (quoted for gate evidence, never extended): module docstring `ATR Breakout strategy.` / `Entry: price breaks above previous close + atr_mult * ATR (breakout confirmation)` / `Exit: price falls below previous close - atr_mult * ATR` (lines 1–6); class docstring `Measures N-period Average True Range and triggers entry when price closes beyond prev_close + atr_mult * ATR. Exit fires on the opposite side breakout or when price retreats inside the channel.` (lines 15–21); `describe()` returns `Enters when close > prev_close + {atr_mult} * ATR({atr_period}). Exits when close < prev_close - {atr_mult} * ATR({atr_period}). Lookback window: {lookback} bars.` (lines 51–56); `default_params` returns exactly `{ "atr_period": 14, "atr_mult": 2.0, "lookback": 20, "leverage": 1.0 }` (lines 39–44); `compatible_regimes` returns `{"TREND_UP", "TREND_DOWN", "BREAKOUT"}` (lines 47–49, metadata never read by the signal path); `parameter_space()` returns `{ "atr_period": (10, 20, 2), "atr_mult": (1.5, 3.0, 0.5), "lookback": (10, 30, 5) }` (lines 131–135, a documented search surface only — this record pins the 14 / 2.0 / 20 defaults and runs no search).
- Single decision path (verified line by line): `generate_signal()` (lines 59–129) is the sole signal method — no `generate_signals` vectorized twin exists anywhere in the file (0 matches), no scalar delegate, no second decision logic exists to diverge. The `confidence` computation (lines 110–114) and the `indicators` dict (lines 122–128) are diagnostic echoes that never enter any predicate.
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults, plus `__post_init__` coercion that refuses non-Boolean flags and resolves direction labels (`_normalize_signal_flag`, `_normalize_signal_direction`, lines 140–176) — flags arriving as strict booleans (as here, via `bool(...)` at line 118) pass through unchanged.
- Full-file token census (verified by search over the 143 lines this cycle): `direction="long"` guard literal (line 72); the computed `direction = "long" if entry else "short" if exit_ else "long"` (line 108 — the ONLY `short` token in the file besides its own `# Direction:` comment on line 107; no short ENTRY leg exists anywhere — see Signal); 0 `sell` / 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` (no order arguments, no risk legs); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 1.0` default); 0 `volume` / 0 `funding` / 0 `request` / 0 `security` / 0 `barstate` / 0 `timeframe` in any line, and 0 `open`-series reads anywhere (direct `df` reads are exactly `close` (line 64), `high`/`low` (lines 76–77), and the `close.shift(1)` anchor (line 81)); 0 `ema` / 0 `ewm` / 0 `sma` / 0 `rsi` (no average, no oscillator of any kind — the sole smoother is the true-range simple rolling mean, line 91); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` (no position-aware state conditions any signal).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the BTC roster asset, the 14-bar simple-mean ATR construction, the prev-close-anchored ±2.0×ATR symmetric channel, the upper-band entry, the lower-band exit, the 22-bar short-frame guard, and the no-stop posture — but ships no venue spelling, no timeframe, no fill-timing flag, and no position-sizing rule, and labels exit bars with a `short` direction echo (line 108) although no short-entry path exists. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue spelling; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted inside-bar, williams-ema-reclaim, linreg, zscore, adl, atr-volume, aroon, ema-rsi-pullback, double-bottom, vwap-cross, chaikin-mf, elder-ray, adx-trend-pulse, dema-cross, trix-signal-cross, ultimate-oscillator, bollinger-s00120, and three-bar-reversal records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) direction pinned `long` with every `exit_` bar routed to the long book (the source's `short` token fires only together with `exit_signal=True` on bars where `entry_signal=False` by mutual exclusion — no bar can open a short under either reading, verified in Signal; the pin changes no openable event, disclosed, never presented as source-native labelling); (4) house sizing/capital/costs replacing the bare `leverage: 1.0` default (see Execution assumptions; sizing changes no event under the predeclared single-unit rule). The 22-bar flat rule is the source's own guard, adopted verbatim — no researcher warmup pin is needed. No other pin is required: entry and exit can never co-fire (proven in Signal), and every strict-inequality boundary fires nothing on exact equality (see Signal). The 14 / 2.0 / 20 literals, the TR construction, the simple-mean ATR variant, the symmetric channel, the long book, and the no-stop/no-target/no-time-exit/no-cooldown posture are source-verbatim.

Pre-write dedup (2026-10-18): working-tree filename/content search for `atr_breakout` / `ATRBreakout` / `PREBUILT-ATR-BREAKOUT` / `atr_mult` returns zero strategy records citing this source file — the sole `atr_mult` hit anywhere is a passing prose token inside the admitted `forven-atr-volume-breakout` sibling, whose rule is a different construction (20-bar rolling-high buffer plus volume gate for entry, EMA12 recross for exit — fenced in Negative evidence 8). The pool's ATR-channel cousins are fenced as different signal constructions in Negative evidence 8 (Keltner EMA20-envelope plus momentum gate two-sided; SuperTrend median-band ATR-flip; Chandelier highest-high/lowest-low ATR trailing-stop flip in open PR #89; Donchian raw-extreme breakout with no volatility normalization; Waddah MACD-plus-BB explosion; ATR-trailing records). No closed `research/*` PR ever carried this source file. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: a 1-bar prev-close-anchored symmetric ±2×ATR(14) channel with upper-band long entry and lower-band long exit is a different signal construction from any average-anchored envelope, extreme-anchored trailing stop, volume-gated breakout, or oscillator-gated system — not a threshold re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: a breakout-confirmation channel where `Entry: price breaks above previous close + atr_mult * ATR` and `Exit: price falls below previous close - atr_mult * ATR`, with the class prose adding that the exit `fires on the opposite side breakout or when price retreats inside the channel`. No behavioural, structural, or risk-premium channel is claimed anywhere in the 143 lines. The file ships no performance number of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Single-bar-anchored volatility breakout, long-only, state-holding. Unlike average-anchored envelopes (Keltner/SuperTrend: breakout measured against a slow mean) or extreme-anchored trails (Chandelier/Donchian: measured against multi-bar highs/lows), this channel re-anchors every bar to the immediately prior close: the bands answer "did this bar's close clear two average true ranges of noise relative to where we just stood". Entry buys a bar that proves expansion; the exit is the symmetric invalidation — a bar that gives back the same volatility-normalized distance ends the trade on the first confirming close rather than waiting for a mean recross. There is no stop leg and no profit leg: a breakout that grinds sideways inside the rolling channel is held indefinitely, while a spike that reverses −2×ATR on the next bar is cut at once. Unlike the atr-volume sibling there is no volume confirmation and no EMA exit — weakness is confirmed only by the symmetric band, exited only by the symmetric band.

## Signal

Exact rule as pinned (any other lookback, multiplier, ATR variant, anchoring, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own; the single `generate_signal` path (lines 59–129) is the single source of truth:

```text
tr              = max(high - low, |high - prev_close|, |low - prev_close|)   // prev_close = close.shift(1)
atr             = tr.rolling(14).mean()                                      // simple rolling mean, NOT Wilder smoothing
curr_atr        = atr[t]                                                     // includes the decision bar's own TR — causal at close
upper_band      = close[t-1] + 2.0 * curr_atr
lower_band      = close[t-1] - 2.0 * curr_atr
entry           = close[t] > upper_band
exit_           = close[t] < lower_band
short_frame     = fewer than 22 completed bars → flat by source guard
```

- Trade events: `entry_signal=bool(entry)`, `exit_signal=bool(exit_)`, direction pinned `long` (see derived declaration — the source emits `direction="long"` on every entry bar and on every idle bar by line 108, and its `short` token fires only on exit bars where no entry can open). A flat book enters one full unit on an entry bar; a long book exits the full unit on an exit bar.
- Mutual exclusion, proven (no reviewer invention): `upper_band > lower_band` whenever `curr_atr > 0` (they differ by `4.0 * curr_atr`), so `close[t] > upper_band` and `close[t] < lower_band` cannot both hold; when `curr_atr == 0` exactly, both bands equal `close[t-1]`, and entry needs `close[t] > close[t-1]` while exit needs `close[t] < close[t-1]` — still exclusive. No bar ever sequences two fills, and no entry/exit priority rule is needed or invented.
- Exact-equality boundaries fire nothing (strict comparisons throughout: `close[t] == upper_band` enters nothing, `close[t] == lower_band` exits nothing, pinned semantic), and pre-guard bars are flat by source rule.
- Direction: long-only. No short-entry path exists anywhere in the file (the sole `short` token sits on the exit-only branch of line 108; `entry_signal=True` always coincides with the `long` branch, verified by the mutual exclusion above), and the short side is recorded as explicitly disabled. Spot-compatible (no naked shorting required).
- Exits and risk (explicit): the lower-band touch is the sole position-ending path. Opposite-signal exit is not applicable (no short leg exists). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence` (lines 110–114) and the six `indicators` fields (`atr`, `upper_band`, `lower_band`, `recent_high`, `recent_low`, `lookback`) are diagnostic — none conditions any order line. The `recent_high` / `recent_low` 20-bar extremes (lines 100–102) and the `lookback` value feed display only: retuning `lookback` changes no admitted event (pinned at the 20 default regardless — a different value is a different, unpinned rule).
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further entry bars as no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops. Re-entry re-arms on any qualifying breakout bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and short-frame bars are flat by source rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low` (TR, display extremes) and `close` (anchor, TR, bands, price echo); no `open`-series read, no bar `volume`, no indicator call of any kind (the ATR is inline arithmetic: one `shift(1)`, one trailing `rolling(14).mean()`), no funding/OI/mark-price read, no `request.*`, `security()`, `timeframe*`, `barstate.*`, session/calendar call, or stop/limit order argument anywhere in the order-gating path (verified by the census above returning zero matches). The ATR variant is pinned as the simple rolling mean (`tr.rolling(window=atr_period).mean()`, line 91 — not Wilder RMA smoothing; a Wilder-ATR reading would be a different, unpinned rule). The `compatible_regimes == {"TREND_UP", "TREND_DOWN", "BREAKOUT"}` set is metadata never read by the signal path (which takes only `df`/`params`); treating the label as a gate would be a different, unpinned rule.

## Required data

- Completed `1h` bars of BTCUSDT: `high`/`low` for the true-range construction and display extremes; `close` for the 1-bar anchor, the TR comparisons, the band arithmetic, and the price echo. No `open`-series read, no bar `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request` / 0 `security` anywhere; 0 `timeframe` tokens in the whole file).
- Single decision timeframe `1h` (researcher pin, disclosed — the file names no timeframe). One evaluation per completed bar; the current bar's TR uses only its own high/low plus the prior close (no shift tricks beyond the causal 1-bar anchor, one trailing 14-bar mean, one 20-bar display window); fills land on the decision bar's own close (`price=round(curr_close, 4)`, pinned derived rule).
- Warmup: the source ships its own length guard — `min_len = max(atr_period, lookback) + 2 = 22`, and shorter frames return an explicit all-flat Signal (lines 66–75). The 22-bar floor covers the 14-bar ATR seed and the 20-bar display window with margin. The record adopts this guard verbatim as its flat rule — no researcher warmup pin is needed and none is pretended. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source roster pins `_asset BTC`; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills (`price=round(curr_close, 4)` — the decision bar's own close), compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same lane primitive the eighteen admitted Forven-sibling records use. No maker-touch, queue, or intrabar-path-dependent fill: the only legs are bar-close-evaluated market entry/exit orders. Entry/exit can never co-fire (proven above), so no bar ever sequences two fills.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its `leverage: 1.0` default is replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with the single-unit/no-add/noop-on-repeat position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one long position at any time; re-entry after an exit needs only the next qualifying breakout bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The disabled short side requires no margin-short modeling.

## Evidence

### Source-reported

The file ships the full construction (143 lines: module docstring with the entry/exit sentences, `TYPE_NAME`, `default_params` at 14 / 2.0 / 20 / `leverage 1.0`, the TR/ATR/channel/entry/exit arithmetic, the 22-bar guard, the line-108 direction expression and the `round(curr_close, 4)` price echo, the `PREBUILT-ATR-BREAKOUT` roster pin). It ships zero adopted performance numbers of any kind — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` ship anywhere — the sole position-closing path is the lower-band touch. The absence of any stop is coded absence, disclosed, not a tunable parameter here.
2. No co-fire ambiguity: entry and exit are proven mutually exclusive on every bar (bands strictly ordered whenever ATR > 0; still exclusive at exactly ATR = 0) — unlike records that need a position-state ordering pin for same-bar overlap, this record needs none. Any engine evaluating both legs on one bar reaches the same single event.
3. Zero-ATR collapse fenced: fourteen identical true ranges pin `curr_atr = 0`, both bands collapse onto `close[t-1]`, and any uptick enters / any downtick exits. The strictness is preserved (equality still fires nothing), but selectivity collapses with volatility — disclosed, not repaired.
4. Sideways-hold fenced: a breakout that drifts inside the re-anchored channel without printing a −2×ATR bar is held indefinitely — no time exit, no profit leg, no trailing guardrail exists to end it. Disclosed, not repaired.
5. Lookback display-only fenced: `recent_high` / `recent_low` / `lookback` never enter any predicate — the 20-literal is pinned but event-neutral. An engine that skips computing display fields reaches identical events.
6. Short-frame behaviour fenced: frames shorter than 22 bars resolve all-flat by the source's own guard (explicit `entry_signal=False, exit_signal=False`, lines 67–75) — a coded behaviour, disclosed; no engine path ever passes an empty frame (backtests feed full history; the record floor starts at bar 1).
7. Source basis fenced: the source names no market beyond `_asset BTC` and no timeframe at all. The BTCUSDT-`1h` choice, same-bar-close fills, single-unit/no-add/noop pin, direction-long pin with long-book-routed exits, and house sizing/costs are researcher choices, disclosed; this record is therefore never evidence that any source-market deployment passes.
8. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-`1h` market choice, the same-bar-close fills, the direction-long pin (including long-book-routed exits), the position-state pin, and house sizing/costs — all predeclared above; the 14-bar simple-mean ATR, the prev-close anchor, the ±2.0 symmetric channel, the upper-band entry, the lower-band exit, the 22-bar guard, the long-only book, and the no-stop/no-target/no-trailing/no-time-exit/no-cooldown posture are source-verbatim. The direction pin changes no openable event: no short-entry path exists under either reading.
9. Cousin records fenced as different constructions (none computes `close[t]` vs `close[t-1] ± 2.0 × simple-mean-ATR(14)`): the admitted `forven-atr-volume-breakout` sibling enters above a 20-bar rolling high plus 0.7×ATR AND a volume gate and exits on an EMA12 recross (buffer-plus-volume-plus-average system, ETH 1h); pool `keltner-momentum-breakout-gated` anchors its envelope on EMA20 with a momentum-sign gate, two-sided; SuperTrend (open PR #63) trails median-based ATR bands with a direction latch; Chandelier Exit (open PR #89) trails multi-bar highest-high/lowest-low extremes; Donchian breaks raw multi-bar extremes with no volatility normalization; Waddah-Attar buys a MACD/BB explosion; `alphatrend-mfi-atr-trailing-reversal` and `nick-rypock-trailing-reverse` trail reversal stops, never a 1-bar-anchored symmetric channel. Not a threshold re-tuning of any of them.
10. The 14 / 2.0 / 20 literals, the simple-mean (non-Wilder) ATR variant, the 1-bar prev-close anchor (not an average, not a multi-bar extreme), the symmetric channel, the upper-entry/lower-exit pair, the strict inequalities, the single-unit long-only stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning any literal, converting ATR to Wilder smoothing, re-anchoring on an average or extreme, adding a volume/momentum gate, adding a stop/target/filter/cooldown/gate, adding a short entry leg, or sizing partially instead of single-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 14-bar simple-mean ATR / prev-close anchor / ±2.0 channel / upper-entry / lower-exit / strict predicates / single-unit long-only / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Channel relevance: replacing the pinned ±2.0×ATR channel with a fixed ±1% price channel around the same prev-close anchor (same exit logic) must not improve net expectancy; fail ⇒ the ATR normalization adds nothing over a fixed band.
- F2 — Anchor relevance: replacing the 1-bar prev-close anchor with a 20-bar EMA anchor at the same ±2.0×ATR(14) widths (same exit logic) must not improve net expectancy; fail ⇒ the 1-bar anchor adds nothing over the standard envelope.
- F3 — Exit symmetry: replacing the lower-band exit with a mid-anchor (prev-close) recross exit must not improve net expectancy; fail ⇒ the symmetric −2.0×ATR distance adds nothing over a plain anchor give-back.

## Crypto portability

Direct: single-venue BTCUSDT perpetual `1h` completed bars with standard OHLC fields. No session calendar (crypto trades continuously; the 1-bar anchor needs no session gap semantics), no corporate actions, no dividends, no funding/OI reads, no cross-venue state. 24/7 continuity means the anchor `close[t-1]` is always the immediately prior print — no weekend-gap discontinuity to normalize. Tick-size rounding follows the venue; the record's 4-decimal price echo is display precision only and changes no event. Leverage/margin follow the house overlay, not the source's bare `1.0` default.

## Limitations

- The source ships no fill-timing flag: same-bar-close fills are a disclosed researcher derivation, never a source claim. An engine filling at next-open would print different event prices on identical bars.
- The source ships no timeframe: the `1h` frame is a disclosed researcher choice. Other frames re-tune nothing in the rule text but produce different event streams; they are different, unpinned evaluations.
- The source ships no costs: all economics come from the house overlay. No realized-funding claim is made; modeled funding is never reported as canonical.
- The `short` direction echo (line 108) is routed to the long book by predeclared researcher pin; the Forven engine's own both-mode routing may read that label differently — this record is not evidence of source-engine behaviour.
- Zero-ATR flatlines collapse selectivity (Negative evidence 3); sideways breakouts are held without guardrail (Negative evidence 4); display fields are skipped without event change (Negative evidence 5).
- Not independently reproduced; no live, Paper, Testnet, or profitability claim of any kind. Admission is engineering capability only.

## Implementation status

not-implemented. No dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record; downstream materialization follows the `IMPLEMENTATION_NEEDED` route without revisiting HB_READY admission.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. Any future authorization requires a separate downstream decision outside this repository's admission scope.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/atr_breakout.py
- https://github.com/judder659/Forven
