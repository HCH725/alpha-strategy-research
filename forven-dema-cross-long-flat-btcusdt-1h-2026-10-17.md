---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven DEMA 12/26 cross long-flat on BTCUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/dema_cross.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven DEMA 12/26 cross long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, `forven-adl-ema-cross`, `forven-atr-volume-breakout`, `forven-aroon-up-down-cross`, `forven-ema-rsi-pullback-reclaim`, `forven-double-bottom-neckline-break`, `forven-vwap-rolling-cross`, `forven-chaikin-mf-threshold-cross`, `forven-elder-ray-bull-power-cross`, and `forven-adx-trend-pulse-reclaim` records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/dema_cross.py`.
- GitHub blob SHA at the pinned commit: `69bf2a4bf98a24895d8b9dd76eab7c692d43e59f`, size 3185 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 3185 bytes, 110 lines, SHA-256 `a727b0dc3e5a36bffebc24bc6461037fe10765c42bb59f8cf21304ed01664b36`, identical to the GitHub blob (`git hash-object` reproduces `69bf2a4b…6eab7c692d43e59f`) — the entire file was retrieved and inspected.
- Registration: the package `forven/strategies/builtin/__init__.py` is a 2-byte stub (blob `8d1c8b69…419a92f`), so discovery is file-level; this file self-registers via `STRATEGY_CLASS = DEMACrossStrategy` and the `STRATEGIES = [("PREBUILT-DEMA-CROSS", DEMACrossStrategy, {"_asset": "BTC"})]` roster pin (lines 106–110).
- The file's own words (quoted for gate evidence, never extended): module docstring `DEMA Cross strategy.`; class docstring `Entry: Fast DEMA crosses above Slow DEMA.` / `Exit: Fast DEMA crosses below Slow DEMA.`; `describe()` returns `Buys when {dema_fast}-bar DEMA crosses above {dema_slow}-bar DEMA. Exits on the reverse crossover.`; `default_params` returns exactly `{ "dema_fast": 12, "dema_slow": 26, "leverage": 1.0 }`; `compatible_regimes` returns `{"TREND_UP", "TREND_DOWN"}`; `parameter_space()` returns `{ "dema_fast": (8, 16, 2), "dema_slow": (20, 34, 2) }` (a documented search surface only — this record pins the defaults and runs no search).
- Full-file token census (verified by search over the 110 lines this cycle): hardcoded `direction="long"` (the sole order-direction token); 0 `short` / 0 `sell` (no short path anywhere); 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` (no order arguments, no risk legs); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 1.0` default); order-gating `df[` reads are `df["close"]` only (one site, line 59); 0 `"open"` / 0 `volume` / 0 `funding` / 0 `request` / 0 `security` / 0 `timeframe` / 0 `barstate` in any order-gating line (the `atr` import on line 56 feeds only the `confidence` diagnostic on line 84 — quoted below — and never any entry/exit comparison); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` (no position-aware state conditions any signal). `confidence` and the `indicators={dema_fast, dema_slow, atr_14}` dict are diagnostic — zero order-gating comparisons read them.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the DEMA12/DEMA26 construction, the cross-up entry, the cross-down exit, the long-only stance, the no-stop posture, and its own `min_bars = dema_slow*2+2` short-frame guard — but ships no venue, no timeframe, no fill-timing flag, and no position-sizing rule inside this file. Researcher-declared adaptations are exactly three: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted inside-bar, williams-ema-reclaim, linreg, zscore, adl, atr-volume, aroon, ema-rsi-pullback, double-bottom, vwap-cross, chaikin-mf, elder-ray, and adx-trend-pulse records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) house sizing/capital/costs replacing the bare `leverage: 1.0` default (see Execution assumptions; sizing changes no event under the predeclared single-unit rule). No tie-break pin is needed: entry and exit are provably mutually exclusive on every bar (see Signal). The source's own `min_bars` guard is adopted verbatim as the warmup floor (see Required data), so no warmup invention is required either. The DEMA arithmetic, the cross pair, the long-only stance, and the no-stop/no-target/no-time-exit posture are source-verbatim.

Pre-write dedup (2026-10-17): working-tree filename/content search for `builtin/dema_cross` / `PREBUILT-DEMA-CROSS` / `DEMACrossStrategy` / `TYPE_NAME = "dema_cross"` returns zero strategy records — no record cites this source file. Pool cousins fenced as different mechanisms in Negative evidence 8 (`tema-dema-hma-cross-trend-two-sided` crosses TEMA(8) against DEMA(43) behind an HMA(52) slope gate, two-sided always-in reversal, different source; `ema-20-50-cross` (Forven S01508 Pine demo) is a single-EMA cross, long-only, different source file; `forven-ema-rsi-pullback-reclaim` reclaims an EMA behind an RSI gate, not a dual-DEMA cross). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: a bare DEMA12/DEMA26 cross pair (double-smoothed averages, `2*EMA(n)-EMA(EMA(n))`, no gate, no filter), long-flat, from immutable file `builtin/dema_cross.py`, is a different signal construction from a TEMA-vs-DEMA gated cross or a single-EMA cross — not a threshold re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: a `DEMA crossover strategy` that `Buys when 12-bar DEMA crosses above 26-bar DEMA. Exits on the reverse crossover.` No behavioural, structural, or risk-premium channel is claimed anywhere in the 110 lines. The file ships no performance number of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Lag-reduced trend following, long-only, state-holding. Each DEMA leg cancels single-EMA lag (`2*EMA(n) − EMA(EMA(n))`), so the fast/slow cross turns earlier than a same-length single-EMA cross at the cost of less smoothing — the entry buys the exact bar the lag-reduced fast average retakes the slow average, and the exit surrenders the unit on the exact bar it falls back below. There is no gate, no filter, and no holding leg: a market that alternates crosses prints repeated full round-trips with no flat state to rest in (whipsaw profile, disclosed), while a leg whose reverse cross never prints is held indefinitely. Unlike stop-based systems there is no fixed-distance risk leg — the reverse cross is the sole risk control by construction.

## Signal

Exact rule as pinned (any other period, gate, exit leg, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own; the `_dema` helper is in-file (lines 10–14), no out-of-file indicator conditions any order:

```text
dema(n, t)      = 2*ewm(span=n, adjust=False)(close) - ewm(span=n, adjust=False)(ewm(span=n, adjust=False)(close))  // causal, in-file
dema_fast(t)    = dema(12, t)
dema_slow(t)    = dema(26, t)
cross_up        = (prev_fast <= prev_slow) and (curr_fast > curr_slow)
cross_down      = (prev_fast >= prev_slow) and (curr_fast < curr_slow)
entry           = cross_up
exit_           = cross_down
min_bars        = dema_slow*2+2 = 54 (source guard; shorter frames return both-signals-false)
```

- Trade events: `entry_signal=bool(entry)`, `exit_signal=bool(exit_)`, `direction="long"` (hardcoded literal — no short emission exists anywhere in the file, verified by full-file search). A flat book enters one full unit on an entry bar; a long book exits the full unit on an exit bar. Entries while already long are no-ops under the predeclared single-unit rule (see position rule); exits while flat are deterministic no-ops. The entry is a one-bar cross edge (strict current-bar inequality on the pair), so no level-refire pressure exists by construction; the exit is the mirror edge and fires on any qualifying bar.
- Mutual-exclusion proof (no tie-break pin required): entry requires `curr_fast > curr_slow`; exit requires `curr_fast < curr_slow` — no single bar satisfies both, including the exact-equality boundary (strict comparisons fire nothing on ties: `prev_fast == prev_slow` arms both prior clauses but both current clauses stay false) and short frames (the source guard returns both-signals-false before any average is read). The reviewer is never asked to invent an ordering.
- Direction: long-only. The short side is absent by construction (0 `short` / 0 `sell` in the file) and recorded as explicitly disabled. Spot-compatible (no naked shorting required).
- Exits and risk (explicit): the reverse crossover is the sole position-ending path. Opposite-signal exit is not applicable (no short leg exists). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence=min(1.0, spread/(curr_atr*2))` (line 84) and the three `indicators` fields are diagnostic — none conditions any order line.
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further entry bars as no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops. Re-entry re-arms on any qualifying cross-up bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-guard bars are flat by record rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `close` with fixed non-negative offsets (trailing EWMs, a one-prior-bar cross read) — no `request.*`, `security()`, `timeframe*`, `barstate.*`, volume, funding/OI/mark-price read, session/calendar call, second oscillator, or stop/limit order argument anywhere in the order-gating path (verified by the census above returning zero matches). The file ships only the scalar `generate_signal` path (no vectorized twin exists to diverge). The `compatible_regimes == {"TREND_UP", "TREND_DOWN"}` set is metadata never read by the signal path (which takes only `df`/`params`); treating the label as a gate would be a different, unpinned rule.

## Required data

- Completed `1h` bars of BTCUSDT: `close` only (the DEMA pair, the cross read, and the `price` echo). No `open`-series read, no bar `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. (The `atr(df, 14)` call reads `high`/`low`/`close` only to print the `atr_14` diagnostic and scale `confidence` — it conditions no order and its removal changes no trade event.)
- Single decision timeframe `1h` (the script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction).
- Warmup: the source ships its own guard — `min_bars = dema_slow*2+2 = 54` completed bars, shorter frames returning both-signals-false with `price=0.0` — adopted verbatim as the warmup floor, flat by record rule (predeclared: the guard *is* the seeding discipline for the double EWM stack; no researcher length is invented). No negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Each bar's close enters the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (the file names no venue; the roster pins `_asset BTC` — the Binance/BTCUSDT pin is a researcher market choice, disclosed, never presented as source-native).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted inside-bar, williams-ema-reclaim, linreg, zscore, adl, atr-volume, aroon, ema-rsi-pullback, double-bottom, vwap-cross, chaikin-mf, elder-ray, and adx-trend-pulse records establish same-bar-close as the pinned-compatible lane primitive for this exact repository family. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity, and entry/exit can never co-fire (proven above), so no intrabar ordering assumption is needed at all.
- Engine path for `1h` (gate 5, stated plainly): `1h` is a Binance-documented USDT-M kline interval; the derived rule needs only completed `1h` candles (`close` for orders, `high`/`low` for the confidence diagnostic) on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no volume tape, no funding/OI/mark-price leg. That is the same single-frame completed-bar path as the admitted `1h` siblings from this source family, minus even the volume-column order read the chaikin-mf and atr-volume records carry. Anything beyond that single-frame completed-bar path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: the source ships only a bare `leverage: 1.0` default with no capital, fee, slippage, funding, or margin assumption (quoted verbatim in census; the absences are disclosed, never read as zero cost) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior. Under the predeclared single-unit rule the sizing overlay changes no trade event.
- Concurrency: single-unit long-flat book — at most one open long; the reverse cross closes the whole unit, and re-entry is allowed on any qualifying cross-up bar after any exit (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (in-file DEMA helper `2*EMA(n) − EMA(EMA(n))`, 12/26 defaults, cross-up entry, cross-down exit, fixed long-only stance with the literal `"long"` direction token, its own 54-bar short-frame guard, no risk legs) and the `PREBUILT-DEMA-CROSS` roster pin. It ships no performance number of any kind — this record claims no source-reported performance, and no backtest figure is invented here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` — the sole position-closing path is the coded reverse crossover. The absence is coded (the signal block ends with the two cross comparisons and only the diagnostic return follows).
2. Variant menu fenced, stated plainly: the `parameter_space()` surface (`dema_fast` 8–16, `dema_slow` 20–34) is a documented search grid the code never runs — this record freezes the `12/26` defaults as written; adopting any grid point would be a different, unpinned rule.
3. Edge-trigger fires as written, stated plainly: entry prints only on the cross bar (strict prior/current inequalities), not on every bar holding the fast average above the slow one — adding a level-hold posture would be a different, unpinned rule.
4. No averaging down, stated plainly: the file is stateless (no position-aware branch exists to implement anything else) — an already-long book treats further entry bars as no-ops under the predeclared single-unit rule.
5. Regime/metadata/passenger quarantine, stated plainly: `confidence`, the three `indicators` fields (`dema_fast`, `dema_slow`, `atr_14`), and the `compatible_regimes == {"TREND_UP", "TREND_DOWN"}` set are returned inside diagnostic fields or class metadata and read by zero order-gating comparisons — treating any of them (including the regime label) as a gate, filter, or sizing input would be a different, unpinned rule. The `atr(df, 14)` call exists solely to print that diagnostic; deleting it changes no trade event.
6. Short-frame path fenced, stated plainly: frames shorter than 54 bars return both-signals-false with `price=0.0` by source code (lines 61–64) — flat by construction, and the returned zero price is a diagnostic echo, never a fill (frames are always full length on the declared venue).
7. Co-fire impossibility fenced with proof, stated plainly: entry requires `curr_fast > curr_slow`, exit requires `curr_fast < curr_slow` — no bar, including exact-equality boundaries and short frames (both signals false), can satisfy both. No tie-break, no ordering assumption, and no reviewer invention is required anywhere in this record.
8. Pool-cousin fence, stated plainly: `tema-dema-hma-cross-trend-two-sided-btcusdt-1d-2026-10-11.md` crosses TEMA(8) against DEMA(43) behind an HMA(52) rising/falling slope gate, two-sided with atomic reversal, from a TradingView script by a different author; `ema-20-50-cross-btcusdt-1h-2026-10-06.md` (Forven S01508 Pine demo) is a single-EMA 20/50 cross, long-only, from a different source file. This record crosses DEMA(12) against DEMA(26) — double-smoothed legs on both sides, no gate, no filter — with a reverse-cross exit, long-flat, on BTCUSDT `1h`, from immutable file `builtin/dema_cross.py` — different input construction × different trigger × different exit/posture × different source file. This record is therefore never evidence for those rules, and those records are never this rule's provenance.
9. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT market pin, the `1h` frame adoption, same-bar-close fills (with live intrabar behavior scoped out), and house sizing/costs — all predeclared above; the source's own 54-bar guard is adopted verbatim, not invented. The DEMA arithmetic, the cross pair, the order stance, and the risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, timing, input set, or the Forven engine's own execution semantics passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: DEMA12/DEMA26 cross pair / long-only / BTCUSDT `1h` / same-bar-close fills are frozen.

- F1 — Lag-reduction relevance: replacing both DEMA legs with single EMAs at the same 12/26 lengths (bare EMA12/26 cross, same exit) must not reproduce-or-beat net expectancy; fail ⇒ the double-smoothing adds nothing over the plain cross.
- F2 — Length relevance: replacing the 12/26 pair with the sibling 20/50 single-EMA construction must not improve net expectancy; fail ⇒ the faster lag-reduced pair is decoration on a generic cross.
- F3 — Exit-leg relevance: replacing the reverse-cross exit with a close-under-slow-DEMA level exit must not improve net expectancy; fail ⇒ the edge-triggered exit is dead code wearing a risk-leg label.

## Crypto portability

Pinned to BTCUSDT Binance futures `1h` under the house overlay (market pin is a researcher choice following the file's `_asset BTC` roster pin; the file itself is venue-agnostic). The order-gating rule reads no volume tape, no funding, and no calendar — only `close` — so venue volume-definition differences cannot move any print; stated plainly as a portability strength with its boundary: cross-venue porting without re-verification would still be a different, unpinned claim, disclosed. The rule is long-only with no stop leg, so a spot-only deployment expresses it fully, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating and no `open`-series read anywhere), so session-gap behavior needs no approximation — the double EWM stack simply spans the continuous tape. Extension to other house-universe assets or timeframes would be a different, unpinned claim.
