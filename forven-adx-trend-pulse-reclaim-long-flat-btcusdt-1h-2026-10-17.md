---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven ADX trend-pulse pullback-reclaim long-flat on BTCUSDT 1h bars
created: 2026-10-17
updated: 2026-10-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-16
sources:
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/adx_trend_pulse.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven ADX trend-pulse pullback-reclaim long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, `forven-adl-ema-cross`, `forven-atr-volume-breakout`, `forven-aroon-up-down-cross`, `forven-ema-rsi-pullback-reclaim`, `forven-double-bottom-neckline-break`, `forven-vwap-rolling-cross`, `forven-chaikin-mf-threshold-cross`, and `forven-elder-ray-bull-power-cross` records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/adx_trend_pulse.py`.
- GitHub blob SHA at the pinned commit: `0d7639107d952ba4ce4045c4bcb1ed30447ec5cd`, size 4350 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 4350 bytes, 125 lines, SHA-256 `0abe8063a5104df61de927ffc12087887b61f4b087f8ac8af27715812437d017`, identical to the GitHub blob (`git hash-object` reproduces `0d763910…47ec5cd`) — the entire file was retrieved and inspected.
- Second provenance file (ADX construction only): the file's single out-of-file indicator import, `from forven.strategies.indicators import adx` inside `_indicator_frame`, resolves through that module's PEP-562 `__getattr__` facade (`_FACADE_NAMES` contains `"adx"`) to the canonical `adx(df, period=14)` in `forven/scanner.py` (line 1929; blob `9a1d77b90bf214c03aa230a5f46775aab94748bd`, 464565 bytes; facade module blob `fdda8b77429e133372482e25cdff8ea31bd59b2a`). The full `scanner.adx` body was read this cycle and is quoted verbatim in Signal; it reads `high`/`low`/`close` only through trailing `diff`/`shift(1)`/`ewm`/`concat-max` ops. No other out-of-file helper is imported (only `pandas` plus the local `BaseStrategy, Signal` base).
- The file's own words (quoted for gate evidence, never extended): module docstring `ADX trend continuation strategy with EMA pullback reclaim.`; `describe()` returns `Trend continuation on {asset}: reclaim the 21-bar EMA after a 4-bar pullback while ADX(14) stays above 18.0.`; `default_params` returns exactly `{ "ema_fast": 21, "ema_slow": 55, "adx_period": 14, "adx_threshold": 18.0, "pullback_bars": 4, "leverage": 2.0 }`; roster entry `("PREBUILT-ADX-TREND-PULSE-BTC", ADXTrendPulseStrategy, {"_asset": "BTC"})`; `compatible_regimes` returns `{"TREND_UP"}`; `parameter_space()` returns `{ "ema_fast": (10, 30, 5), "ema_slow": (40, 80, 5), "adx_threshold": (12, 28, 4), "pullback_bars": (2, 6, 1) }` (a documented search surface only — this record pins the defaults and runs no search).
- Full-file token census (verified by search over the 125 lines this cycle): hardcoded `direction="long"` (the sole order-direction token); 0 `short` / 0 `sell` (no short path anywhere); 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` (no order arguments, no risk legs); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 2.0` default); in-file `df[` reads are `df["close"]` only (one site); 0 `"open"` / 0 `volume` / 0 `funding` / 0 `request` / 0 `security` / 0 `timeframe` / 0 `barstate` (order-gating inputs are `close` plus the `high`/`low`/`close` ADX construction — volume is never read anywhere); 0 `rsi` / 0 `atr` / 0 `macd` / 0 `vwap` / 0 `stoch` (no second indicator); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` (no position-aware state conditions any signal). `confidence` and the `indicators={ema_fast, ema_slow, adx, trend_ok, recent_pullback}` dict are diagnostic — zero order-gating comparisons read them.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the EMA21/EMA55/ADX14 construction, the four-way entry conjunction (slow-EMA trend + ADX gate + 4-bar pullback touch + fast-EMA reclaim), the close-under-fast-EMA / ADX-under-gate exit pair, the long-only stance, and the no-stop posture — but ships no venue, no timeframe, no fill-timing flag, and no position-sizing rule inside this file. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted inside-bar, williams-ema-reclaim, linreg, zscore, adl, atr-volume, aroon, ema-rsi-pullback, double-bottom, vwap-cross, chaikin-mf, and elder-ray records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) an adopted 120-completed-bar warmup with pre-warmup bars flat by record rule (the file ships no length guard — NaN comparisons already yield both-signals-false on short frames — so the record rule carries the seeding discipline for the EMA55 plus the span-14 EWM stack; see Required data); (4) house sizing/capital/costs replacing the bare `leverage: 2.0` default (see Execution assumptions; sizing changes no event under the predeclared single-unit rule). No tie-break pin is needed: entry and exit are provably mutually exclusive on every bar (see Signal). The EMA/ADX arithmetic, the four-way entry, the exit pair, the long-only stance, and the no-stop/no-target/no-time-exit posture are source-verbatim and unmodified.

Pre-write dedup (2026-10-17): working-tree filename/content search for `builtin/adx_trend_pulse` / `PREBUILT-ADX-TREND-PULSE` / `ADXTrendPulseStrategy` / `trend_pulse_adx` returns zero strategy records — no record cites this source file. Pool cousins fenced as different mechanisms in Negative evidence 8 (`adx-di-cross-strength-gated-two-sided` fires on a ±DI cross behind a strength gate, two-sided, different source; `forven-ema-rsi-pullback-reclaim` reclaims an EMA behind an RSI bounce gate, not an ADX gate plus slow-EMA trend plus pullback-touch window; `double-seven-connors-pullback` is a Connors-style pullback). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: a four-way EMA55-trend × ADX14≥18 × 4-bar-pullback-touch × EMA21-reclaim conjunction with a close-under-EMA21 / ADX-under-gate exit, long-flat, from immutable file `builtin/adx_trend_pulse.py`, is a different signal construction from a ±DI-cross system or an RSI-gated reclaim — not a threshold re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: `ADX trend continuation strategy with EMA pullback reclaim` that enters on `reclaim the 21-bar EMA after a 4-bar pullback while ADX(14) stays above 18.0`. No behavioural, structural, or risk-premium channel is claimed anywhere in the 125 lines. The file ships no performance number of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Trend-continuation participation with a pullback-timing filter, long-only, state-holding. The slow EMA55 holds the regime vote (price above it), ADX14≥18 requires measurable trend strength so range chop cannot arm entries, the 4-bar pullback-touch window requires sellers to have actually pressed price into the fast EMA21 recently (no chasing of extended bars), and the reclaim cross times the entry to the exact bar buyers retake the fast line. The exit surrenders the unit on the first bar price slips back under the fast line or trend strength decays under the gate; the ADX clause that armed the entry doubles as a trailing strength guard once long. Unlike level-hold systems there is no repeated-entry pressure — the entry is a one-bar reclaim edge — and unlike stop-based systems there is no fixed-distance risk leg: a reclaim that fails on the next bar hands back the unit on that bar by construction (whipsaw profile, disclosed).

## Signal

Exact rule as pinned (any other period, gate, window, exit leg, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own; the ADX body is the canonical `scanner.adx` reached through the documented facade:

```text
ema_fast(t)       = ewm(span=21, adjust=False) of close                 // causal
ema_slow(t)       = ewm(span=55, adjust=False) of close                 // causal
TR                = max(high-low, |high-prev_close|, |low-prev_close|)  // causal
dm_pos            = ((high-high.shift()) > (low.shift()-low)) * (high-high.shift()).clip(lower=0)
dm_neg            = ((low.shift()-low) > (high-high.shift())) * (low.shift()-low).clip(lower=0)
atr14             = ewm(span=14, adjust=False) of TR
di_pos            = 100 * ewm(span=14, adjust=False)(dm_pos) / atr14
di_neg            = 100 * ewm(span=14, adjust=False)(dm_neg) / atr14
dx                = 100 * |di_pos-di_neg| / (di_pos+di_neg)
adx(t)            = ewm(span=14, adjust=False) of dx                     // all adjust=False
recent_pullback   = min(close.shift(1) over rolling 4) <= ema_fast.shift(1)
trend_ok          = close > ema_slow
adx_ok            = adx >= 18.0
reclaim           = (prev_close <= prev_ema_fast) and (curr_close > curr_ema_fast)
entry             = trend_ok and adx_ok and recent_pullback and reclaim
exit_             = (curr_close < curr_ema_fast) or (adx < 18.0)
```

- Trade events: `entry_signal=bool(entry)`, `exit_signal=bool(exit_)`, `direction="long"` (hardcoded literal — no short emission exists anywhere in the file, verified by full-file search). A flat book enters one full unit on an entry bar; a long book exits the full unit on an exit bar. Entries while already long are no-ops under the predeclared single-unit rule (see position rule); exits while flat are deterministic no-ops. The entry is a one-bar reclaim edge (strict prior/current inequalities on the fast EMA), so no level-refire pressure exists by construction; the exit is level-based by code and fires on any qualifying bar.
- Mutual-exclusion proof (no tie-break pin required): entry implies `curr_close > curr_ema_fast` and `adx >= 18.0`; exit requires `curr_close < curr_ema_fast` or `adx < 18.0` — no single bar satisfies both, including the exact-equality boundary (strict comparisons fire nothing on ties), single-bar frames (`previous=current` makes `reclaim` require `close<=ema_fast` and `close>ema_fast` at once — impossible), and NaN-seeding bars (every comparison against NaN is False, so both signals are false). The reviewer is never asked to invent an ordering.
- Direction: long-only. The short side is absent by construction (0 `short` / 0 `sell` in the file) and recorded as explicitly disabled. Spot-compatible (no naked shorting required).
- Exits and risk (explicit): the close-under-fast-EMA / ADX-under-gate pair is the sole position-ending path. Opposite-signal exit is not applicable (no short leg exists). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence=min(1.0, adx/40.0)` and the five `indicators` fields are diagnostic — none conditions any order line.
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further entry bars as no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops. Re-entry re-arms on any qualifying four-way bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low`/`close` with fixed non-negative offsets (trailing EWMs, a one-bar-shifted pullback window, a one-prior-bar reclaim read) — no `request.*`, `security()`, `timeframe*`, `barstate.*`, volume, funding/OI/mark-price read, session/calendar call, second oscillator, or stop/limit order argument anywhere in the order-gating path (verified by the census above returning zero matches). The vectorized `generate_signals` twin computes the same conjunction (`reclaim & trend_ok & adx_ok & recent_pullback`) and the same exit pair, confirming the scalar path. The `compatible_regimes == {"TREND_UP"}` set is metadata never read by the signal path (which takes only `df`/`params`); treating the label as a gate would be a different, unpinned rule.

## Required data

- Completed `1h` bars of BTCUSDT: `high`/`low`/`close` only (ADX TR/DM/DX construction, the EMA pair, the pullback-touch window, and the reclaim read). No `open`-series read, no bar `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read anywhere.
- Single decision timeframe `1h` (the script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction).
- Warmup: the construction stacks a 55-bar slow EMA beneath span-14 EWM smoothing of TR/DM/DX plus a 4-bar pullback window and a one-prior-bar reclaim read; the file ships no length guard (short frames already evaluate both signals false by NaN/degenerate-frame logic proven above). The adopted warmup is the first 120 completed `1h` bars flat by record rule (predeclared researcher choice — slow-EMA seeding plus EWM-stack margin). No negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Each bar's prints enter the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (the file names no venue; the roster pins `_asset BTC` — the Binance/BTCUSDT pin is a researcher market choice, disclosed, never presented as source-native).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted inside-bar, williams-ema-reclaim, linreg, zscore, adl, atr-volume, aroon, ema-rsi-pullback, double-bottom, vwap-cross, chaikin-mf, and elder-ray records establish same-bar-close as the pinned-compatible lane primitive for this exact repository family. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity, and entry/exit can never co-fire (proven above), so no intrabar ordering assumption is needed at all.
- Engine path for `1h` (gate 5, stated plainly): `1h` is a Binance-documented USDT-M kline interval; the derived rule needs only completed `1h` candles (`high`/`low`/`close`) on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no volume tape, no funding/OI/mark-price leg. That is the same single-frame completed-bar path as the admitted `1h` siblings from this source family, minus even the volume-column read the chaikin-mf and atr-volume records carry. Anything beyond that single-frame completed-bar path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: the source ships only a bare `leverage: 2.0` default with no capital, fee, slippage, funding, or margin assumption (quoted verbatim in census; the absences are disclosed, never read as zero cost) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior. Under the predeclared single-unit rule the sizing overlay changes no trade event.
- Concurrency: single-unit long-flat book — at most one open long; the exit pair closes the whole unit, and re-entry is allowed on any qualifying four-way bar after any exit (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (EMA21/EMA55 pair, span-14 EWM ADX with the 18.0 gate, 4-bar pullback-touch window, fast-EMA reclaim entry, close-under-fast-EMA / ADX-under-gate exit, fixed long-only stance with the literal `"long"` direction token, no risk legs) and the `PREBUILT-ADX-TREND-PULSE-BTC` roster pin. It ships no performance number of any kind — this record claims no source-reported performance, and no backtest figure is invented here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` — the sole position-closing path is the coded close-under-fast-EMA / ADX-under-gate pair. The absence is coded (the signal block ends with the two comparisons and only the diagnostic return follows).
2. Variant menu fenced, stated plainly: the `parameter_space()` surface (`ema_fast` 10–30, `ema_slow` 40–80, `adx_threshold` 12–28, `pullback_bars` 2–6) is a documented search grid the code never runs — this record freezes the `21/55/18.0/4` defaults as written; adopting any grid point would be a different, unpinned rule.
3. Edge-trigger fires as written, stated plainly: entry prints only on the reclaim bar behind all three arming conditions (strict prior/current inequalities plus windowed touch), not on every bar holding price above the fast EMA — adding a level-hold posture would be a different, unpinned rule.
4. No averaging down, stated plainly: the file is stateless (no position-aware branch exists to implement anything else) — an already-long book treats further entry bars as no-ops under the predeclared single-unit rule.
5. Regime/metadata/passenger quarantine, stated plainly: `confidence`, the five `indicators` fields (`ema_fast`, `ema_slow`, `adx`, `trend_ok`, `recent_pullback`), and the `compatible_regimes == {"TREND_UP"}` set are returned inside diagnostic fields or class metadata and read by zero order-gating comparisons — treating any of them (including the regime label) as a gate, filter, or sizing input would be a different, unpinned rule.
6. Short-frame path fenced, stated plainly: the file ships no length guard, but single-bar frames make `reclaim` self-contradictory (false) and NaN-seeding bars compare false everywhere — both signals false by construction, flat by record rule, and the returned price is a diagnostic echo, never a fill (frames are always full length on the declared venue; the adopted 120-bar warmup holds the book flat long past seeding).
7. Co-fire impossibility fenced with proof, stated plainly: entry requires `curr_close > curr_ema_fast` with `adx >= 18.0`, exit requires `curr_close < curr_ema_fast` or `adx < 18.0` — no bar, including exact-equality boundaries, single-bar frames, and NaN-seeding bars (both signals false), can satisfy both. No tie-break, no ordering assumption, and no reviewer invention is required anywhere in this record.
8. Pool-cousin fence, stated plainly: `adx-di-cross-strength-gated-two-sided-btcusdt-1d-2026-10-10.md` fires on a ±DI cross behind a strength gate, two-sided, from a different source; `forven-ema-rsi-pullback-reclaim-long-flat-solusdt-1h-2026-10-17.md` reclaims an EMA behind an RSI(14) touch-and-bounce gate with no ADX leg, no slow-EMA trend leg, and no pullback-touch window; `double-seven-connors-pullback-long-btcusdt-1d-2026-10-09.md` is a Connors-style pullback. This record requires the four-way conjunction of slow-EMA55 trend × ADX14≥18 × 4-bar pullback-touch × EMA21 reclaim with a close-under-EMA21 / ADX-under-gate exit, long-flat, on BTCUSDT `1h`, from immutable file `builtin/adx_trend_pulse.py` — different input construction × different trigger × different gate set × different exit × different source file. This record is therefore never evidence for those rules, and those records are never this rule's provenance.
9. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT market pin, the `1h` frame adoption, same-bar-close fills (with live intrabar behavior scoped out), the adopted 120-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the EMA/ADX arithmetic, the four-way entry, the exit pair, the order stance, and the risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, timing, input set, or the Forven engine's own execution semantics passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: EMA21/EMA55 × ADX14≥18 × 4-bar-pullback-touch × EMA21-reclaim entry / long-only / BTCUSDT `1h` / same-bar-close fills are frozen.

- F1 — Gate relevance: removing the ADX≥18 gate (bare EMA55-trend + pullback-touch + reclaim entry, same exit pair) must not reproduce-or-beat net expectancy; fail ⇒ the coded strength gate adds nothing over the bare reclaim.
- F2 — Window relevance: removing the 4-bar pullback-touch requirement (bare trend + gate + reclaim) must not improve net expectancy; fail ⇒ the touch window is dead code wearing a timing-filter label.
- F3 — Exit-leg relevance: replacing the exit pair with the bare close-under-EMA21 leg alone (dropping the ADX-under-gate clause) must not improve net expectancy; fail ⇒ the strength-decay clause is dead code wearing a risk-leg label.

## Crypto portability

Pinned to BTCUSDT Binance futures `1h` under the house overlay (market pin is a researcher choice following the file's `_asset BTC` roster pin; the file itself is venue-agnostic). The rule reads no volume tape, no funding, and no calendar — only `high`/`low`/`close` — so venue volume-definition differences cannot move any print; stated plainly as a portability strength with its boundary: cross-venue porting without re-verification would still be a different, unpinned claim, disclosed. The rule is long-only with no stop leg, so a spot-only deployment expresses it fully, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating and no `open`-series read anywhere), so session-gap behavior needs no approximation — the EMAs and the ADX stack simply span the continuous tape. Extension to other house-universe assets or timeframes would be a different, unpinned claim.
