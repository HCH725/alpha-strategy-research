---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven EMA-RSI pullback reclaim long-flat on SOLUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/ema_rsi_pullback.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven EMA-RSI pullback reclaim long-flat on SOLUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, `forven-adl-ema-cross`, `forven-atr-volume-breakout`, and `forven-aroon-up-down-cross` records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/ema_rsi_pullback.py`.
- GitHub blob SHA at the pinned commit: `19ea6406397215b9f18e36b75a4a28852e51c5b0`, size 4039 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 4039 bytes, 115 lines, SHA-256 `18e68f60ff0162d6ff719418d4c9761129c7486308b3ac44cdf9373d561e4e23`, identical to the GitHub blob (`git hash-object` reproduces `19ea6406…52e51c5b0`) — the entire file was retrieved and inspected; the order-gating rule lives in this one file plus exactly one pinned pure helper (the RSI call below, a same-commit passenger).
- The file's own words (quoted for gate evidence, never extended): module docstring `EMA trend pullback strategy confirmed by RSI recovery.`; `describe()` returns `Buy a pullback inside an EMA uptrend when RSI(14) reclaims 45; exit when RSI loses 62 or price loses the slow EMA.`; `default_params` returns exactly `{ "ema_fast": 12, "ema_slow": 34, "rsi_period": 14, "rsi_entry": 45, "rsi_exit": 62, "leverage": 2.0 }`; roster entry `("PREBUILT-EMA-RSI-PULLBACK-SOL", EMARSIPullbackStrategy, {"_asset": "SOL"})`; `compatible_regimes` returns `{"TREND_UP", "RANGE_BOUND"}`; `parameter_space()` returns `{ "ema_fast": (8, 20, 2), "ema_slow": (21, 55, 5), "rsi_entry": (40, 55, 5), "rsi_exit": (55, 70, 5) }` (a documented search surface only — this record pins the defaults and runs no search).
- RSI helper provenance (the file's only out-of-file call): line 48 `from forven.strategies.indicators import rsi` resolves through that module's PEP-562 `__getattr__` facade (`_FACADE_NAMES` includes `"rsi"`, verified at lines 864–880 of `indicators.py` at the pinned commit) to `forven/scanner.py` `def rsi(series, period=14)`: Wilder's RSI — `delta.clip` gain/loss with `ewm(alpha=1/n, adjust=False, min_periods=n)` smoothing, `rs = gain / loss.clip(lower=1e-9)`, `100 - 100/(1+rs)` (quoted body read this cycle; the scanner docstring states it matches TradingView/Binance `ta.rsi` and the canonical `indicators._rsi`). The helper is pure pandas over the passed series (no DB, no network, no global state in the quoted body); `scanner.py` at the pinned commit is 464565 bytes, blob `9a1d77b90bf214c03aa230a5f46775aab94748bd` (`git hash-object` verified this cycle). The call `rsi(close, 14)` matches the helper signature `(series, period)` positionally.
- Full-file token census (verified by search over the 115 lines this cycle): 1 `direction` literal, `"long"` (hardcoded on the single-bar return — the sole order-direction token); 0 `short` / 0 `sell` (no short path anywhere, case-insensitive); 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` / 0 `trail` (no order arguments, no risk legs); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 2.0` default); 0 `open` / 0 `time` / 0 `request` / 0 `security` / 0 `barstate` / 0 `timeframe` / 0 `funding` (order-gating reads are `close` only — the EMAs, the RSI, and every comparison derive from the close series alone; zero reads of `high`, `low`, `volume`, or any other column); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` / 0 `cooldown` (no position-aware state conditions any signal). Imports are `__future__`, `pandas`, the local `BaseStrategy, Signal` base, plus the single pinned `rsi` helper — no cross-asset import, no second feed.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the EMA(12/34) stack, the close-above-fast filter, the RSI(14) reclaim-of-45 entry, the RSI-rollover-below-62 / slow-EMA-loss dual exit, the long-only stance, and the no-stop posture — but ships no venue, no timeframe, no fill-timing flag, and no position-sizing rule inside this file. Researcher-declared adaptations are exactly four: (1) research market/timeframe `SOLUSDT` `1h` (the file names no timeframe and no venue; the roster pins `_asset SOL` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(close, 4)` — the decision bar's own close — and the admitted S01508, inside-bar, williams-ema-reclaim, linreg, zscore, adl, atr-volume, and aroon records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) an adopted 60-completed-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 36th completed bar — the 34-bar slow-EMA seeding plus the RSI `min_periods=14` stabilization plus the one-prior-bar edge read — plus margin; see Required data); (4) house sizing/capital/costs replacing the bare `leverage: 2.0` default (see Execution assumptions; sizing changes no event under the predeclared single-unit rule). No tie-break pin is needed: entry and exit are provably mutually exclusive on every bar (see Signal). The EMA construction, the reclaim entry, the dual exit, the long-only stance, and the no-stop/no-target/no-time-exit posture are source-verbatim and unmodified.

Pre-write dedup (2026-10-17): working-tree filename/content search for `builtin/ema_rsi_pullback` / `PREBUILT-EMA-RSI` / `EMARSIPullback` returns zero strategy records — no record cites this source file. Content search for pullback-family records returns only pool cousins fenced as different mechanisms in Negative evidence 8 (`double-seven-connors-pullback`, a 3-component Connors-RSI regime pullback; `catching-the-bottom-rsi-dip-reversal`, an RSI dip-buy without any EMA-stack gate or dual exit). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: an EMA-stack-gated Wilder-RSI reclaim entry with an RSI-rollover/slow-EMA-loss dual exit is a different signal construction from a Connors-RSI pullback or an ungated RSI dip-buy — not a threshold re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: an `EMA trend pullback strategy confirmed by RSI recovery` that will `Buy a pullback inside an EMA uptrend when RSI(14) reclaims 45; exit when RSI loses 62 or price loses the slow EMA.` No behavioural, structural, or risk-premium channel is claimed anywhere in the 115 lines. The file ships no performance number of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Uptrend-pullback capture with momentum confirmation, long-only, state-holding. The EMA(12/34) stack plus the close-above-fast filter asks that the pullback happen inside an intact short-term uptrend (not a breakdown masquerading as a dip); the RSI reclaim through 45 asks that the bounce already show measurable momentum recovery rather than a falling knife still accelerating down. The exit is the mirror discipline with two independent legs: momentum rollover (RSI losing 62 — the reclaim failed to extend) or structural loss (close under the slow EMA — the uptrend itself broke), so a position survives mid-range RSI chop between 45 and 62 and closes only on demonstrated failure. Unlike level-hold systems there is no repeated-entry pressure: the reclaim is a one-bar edge event, and the predeclared single-unit rule turns any same-side refire into a no-op. The failure mode is plain: a grind-down that keeps RSI pinned under 45 never enters at all (opportunity cost, disclosed), while a whipsaw that reclaims 45 then rolls under 62 prints repeated reclaim-then-rollover round trips with no stop and no profit-taking leg (disclosed).

## Signal

Exact rule as pinned (any other EMA pair, RSI length, reclaim/rollover level, exit leg, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own:

```text
ema_fast    = EMA(close, 12)                    // adjust=False
ema_slow    = EMA(close, 34)                    // adjust=False
rsi         = WilderRSI(close, 14)              // scanner.rsi, min_periods=14
trend_ok    = (ema_fast > ema_slow) and (close >= ema_fast)
rsi_reclaim = (prev_rsi < 45) and (curr_rsi >= 45)
rsi_rollover= (prev_rsi >= 62) and (curr_rsi < 62)
entry       = trend_ok and rsi_reclaim
exit_       = rsi_rollover or (close < ema_slow)
```

- Trade events: `entry_signal=bool(entry)`, `exit_signal=bool(exit_)`, `direction="long"` (hardcoded literal — no short emission exists anywhere in the file, verified by full-file search). A flat book enters one full unit on an entry bar; a long book exits the full unit on an exit bar. Entries while already long are no-ops under the predeclared single-unit rule (see position rule); exits while flat are deterministic no-ops. The reclaim is a one-bar edge event (strict inequalities on the prior/current pair), so no level-refire pressure exists by construction.
- Mutual-exclusion proof (no tie-break pin required): exit via the slow-EMA leg implies `close < ema_slow`, while entry implies `close >= ema_fast > ema_slow` — jointly unsatisfiable. Exit via the rollover leg requires `prev_rsi >= 62`, while entry requires `prev_rsi < 45` — jointly unsatisfiable on the same prior bar. No single bar satisfies both, including exact-equality boundaries (strict comparisons fire nothing on ties) and NaN seed bars (all strict comparisons false). The reviewer is never asked to invent an ordering.
- Direction: long-only. The short side is absent by construction (0 `short` / 0 `sell` in the file, case-insensitive) and recorded as explicitly disabled. Spot-compatible (no naked shorting required).
- Exits and risk (explicit): the RSI-rollover / slow-EMA-loss pair is the sole position-ending path (either leg alone closes the full unit). Opposite-signal exit is not applicable (no short leg exists). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence=min(1, rsi/100)` on every bar and the `indicators={ema_fast, ema_slow, rsi, trend_ok}` dict are diagnostic — none conditions any order line.
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further entry bars as no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops. Re-entry re-arms on any qualifying reclaim after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `close` with fixed non-negative offsets (trailing EMAs, a trailing Wilder RSI, plus a one-prior-bar edge read) — no `request.*`, `security()`, `timeframe*`, `barstate.*`, high/low/volume, funding/OI/mark-price read, session/calendar call, or stop/limit order argument anywhere in the file (verified by the census above returning zero matches). The file ships no `len(df) < N` guard on the single-bar path (`previous` falls back to `current` on a 1-bar frame); every pre-seed window prints NaN and every NaN strict comparison is false, so pre-seed bars deterministically print neither signal — the record-rule 60-bar warmup additionally holds them flat. The vectorized `generate_signals` batch path encodes the identical edge pair (`trend_ok & rsi_reclaim` entries; `rsi_rollover | close < slow` exits, `fillna(False)`) — the two code paths agree bar-for-bar, disclosed as corroboration, never as a second rule. The `compatible_regimes == {"TREND_UP", "RANGE_BOUND"}` set is metadata never read by the signal path (which takes only `df`/`params`); treating the label as a gate would be a different, unpinned rule.

## Required data

- `1h` bars of one pair: `close` only (EMA-12/34 path, Wilder-RSI(14) path, and every comparison read the close series alone). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade/aggressor, L2/order-book, on-chain, options/Greeks, sentiment/news, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1h` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; every test reads trailing bars of the same series, never a second feed).
- Warmup: 60 completed `1h` bars flat by record rule — structural minimum is the 36th completed bar (the 34-bar slow-EMA seeding plus RSI `min_periods=14` stabilization plus the one-prior-bar edge read). The extra 24 bars are adopted margin covering Wilder-RSI settling; pre-warmup bars are flat by record rule. Missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (every window reads completed bars only), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: SOLUSDT Binance futures under the house overlay (the file names no venue; the roster pins `_asset SOL` — the Binance/SOLUSDT pin is a researcher market choice, disclosed, never presented as source-native).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The file returns `price=round(close, 4)` — the decision bar's own close — and the admitted S01508, inside-bar, williams-ema-reclaim, linreg, zscore, adl, atr-volume, and aroon records establish same-bar-close as the pinned-compatible lane primitive for this exact repository family. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity, and entry/exit can never co-fire (proven above), so no intrabar ordering assumption is needed at all.
- Engine path for `1h` (gate 5, stated plainly): `1h` is a Binance-documented USDT-M kline interval; the derived rule needs only completed `1h` candles (`close` alone) on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no high/low/volume/funding/OI/mark-price leg. That is the same single-frame completed-bar path as the admitted `1h` siblings from this source family. Anything beyond that single-frame completed-bar path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: the source ships only a bare `leverage: 2.0` default with no capital, fee, slippage, funding, or margin assumption (quoted verbatim in census; the absences are disclosed, never read as zero cost) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior. Under the predeclared single-unit rule the sizing overlay changes no trade event.
- Concurrency: single-unit long-flat book — at most one open long; either exit leg closes the whole unit, and re-entry is allowed on any qualifying reclaim after any exit (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (EMA-12/34 stack with close-above-fast filter, Wilder-RSI(14) reclaim-of-45 entry, RSI-rollover-below-62 / slow-EMA-loss dual exit, fixed long-only stance with the literal `"long"` direction token, no risk legs) and the `PREBUILT-EMA-RSI-PULLBACK-SOL` roster pin. It ships no performance number of any kind — this record claims no source-reported performance, and no backtest figure is invented here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` / 0 `trail` — the sole position-closing path is the coded rollover/slow-EMA-loss pair. The absence is coded (the signal block ends with the two comparisons and only the diagnostic return follows).
2. Variant menu fenced, stated plainly: the `parameter_space()` surface (`ema_fast` 8–20 step 2, `ema_slow` 21–55 step 5, `rsi_entry` 40–55 step 5, `rsi_exit` 55–70 step 5) is a documented search grid the code never runs — this record freezes the `12` / `34` / `45` / `62` defaults as written; adopting any grid point would be a different, unpinned rule.
3. Edge-trigger fires as written, stated plainly: entry prints only on the reclaim bar (strict prior/current inequalities), not on every bar holding RSI above 45 inside the stack — adding a level-hold posture would be a different, unpinned rule.
4. No averaging down, stated plainly: the file is stateless (no position-aware branch exists to implement anything else) — an already-long book treats further entry bars as no-ops under the predeclared single-unit rule.
5. Regime/metadata/passenger quarantine, stated plainly: `confidence`, the four `indicators` fields, and the `compatible_regimes == {"TREND_UP", "RANGE_BOUND"}` set are returned inside diagnostic fields or class metadata and read by zero order-gating comparisons — treating any of them as a gate, filter, or sizing input would be a different, unpinned rule.
6. Short-frame path fenced, stated plainly: the single-bar path ships no `len(df) < N` guard (a 1-bar frame falls back to `previous = current`, and the short-frame `len(df) < N` concept from sibling files is absent here) — every pre-seed comparison is NaN-false so no signal can print, and the record-rule 60-bar flat covers seeding plus stabilization regardless.
7. Co-fire impossibility fenced with proof, stated plainly: entry requires `close >= ema_fast > ema_slow` and `prev_rsi < 45`; either exit leg contradicts one of those conjuncts — no bar, including exact-equality boundaries and NaN seed bars (all strict comparisons false), can satisfy both. No tie-break, no ordering assumption, and no reviewer invention is required anywhere in this record.
8. Pool-cousin fence (pullback/RSI-family records), stated plainly: `double-seven-connors-pullback-long-btcusdt-1d-2026-10-09.md` trades a 3-component Connors-RSI (price RSI + streak RSI + percent-rank) regime pullback on BTCUSDT `1d` from a book-derived source; `catching-the-bottom-rsi-dip-reversal-long-ethusdt-1h-2026-10-08.md` buys an ungated RSI dip reversal on ETHUSDT `1h`. This record gates a Wilder-RSI(14) reclaim through the fixed `45` line on an EMA(12/34) stack with a close-above-fast filter and exits on RSI rollover under `62` or slow-EMA loss, long-flat, on SOLUSDT `1h`, from immutable file `builtin/ema_rsi_pullback.py` — different input construction × different trigger × different gate × different exit × different source file. This record is therefore never evidence for those rules, and those records are never this rule's provenance.
9. Derivation boundary fenced: the only non-source-native behaviors in this record are the SOLUSDT market pin, the `1h` frame adoption, same-bar-close fills (with live intrabar behavior scoped out), the adopted 60-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the EMA arithmetic, the reclaim entry, the dual exit, the order stance, and the risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, timing, input set, or the Forven engine's own execution semantics passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: EMA(12/34) stack / close-above-fast filter / RSI(14) reclaim-of-45 / rollover-62-or-slow-loss exit / long-only / SOLUSDT `1h` / same-bar-close fills are frozen.

- F1 — Gate relevance: dropping the EMA-stack gate (pure RSI reclaim entry, same dual exit) must not improve net expectancy; fail ⇒ the coded trend gate adds nothing over its ungated twin.
- F2 — Edge relevance: replacing the reclaim-edge entry with a level-hold entry (every in-stack bar with RSI above 45, same exit) must not improve net expectancy; fail ⇒ the coded edge adds nothing over its level twin.
- F3 — Construction relevance: replacing the RSI reclaim with a same-structure fast/slow EMA cross (same edge entry shape, same dual exit) must not reproduce-or-beat net expectancy; fail ⇒ the record is a moving-average-cross variant wearing a momentum label.

## Crypto portability

Pinned to SOLUSDT Binance futures `1h` under the house overlay (market pin is a researcher choice following the file's `_asset SOL` roster pin; the file itself is venue-agnostic). The rule reads no `high`/`low`/`volume` tape and no funding/OI/mark-price leg — only the `close` series — so venue volume-definition differences cannot move any gate (there is no volume read at all, stronger than the close-only Aroon sibling) — stated plainly as a portability strength with a boundary: cross-venue porting without re-verification would still be a different, unpinned claim, disclosed. The rule is long-only with no stop leg, so a spot-only deployment expresses it fully, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the file returns the decision bar's own close but ships no explicit fill-timing flag; this record evaluates completed bars only and executes same-bar-close on SOLUSDT `1h`. Any live intrabar behavior is out of scope.
- Derived market pin: the file names no venue and no timeframe (roster pins `_asset SOL` only) — SOLUSDT `1h` is a researcher market/frame choice for the house universe, never a source claim.
- Source economics are leverage-only: beyond the bare `leverage: 2.0` default the source ships no capital sizing, no fee, no slippage, no funding, and no margin assumption — derived evaluation must carry the full house cost load (fees plus historical funding; no hypothetical zero funding claimed), and this record reports no net performance of its own.
- No price stop, no time stop: adverse excursion after placement has no guardrail beyond the dual exit; a reclaim-then-rollover whipsaw prints repeated entry-then-exit round trips by construction, and a grind-down that pins RSI under 45 never enters (opportunity cost, disclosed). This is the coded posture, disclosed as the record's principal risk.
- Seed bars: the 34-bar slow-EMA seeding plus Wilder-RSI `min_periods=14` stabilization dominate early bars; the first 60 `1h` bars are flat by record rule, so early-history signals never enter any evaluation. Substituting a seeded/warm-started average would move every early print and is a different, unpinned rule.
- Single-bar-frame fallback: `previous = current` on a 1-bar frame is coded behavior that prints no signal (all strict comparisons fail on identical values) — disclosed in Negative evidence 6; on the declared venue frames are always full length.
- No co-fire corner exists: see Negative evidence 7 — entry and exit are mutually exclusive by construction on every bar, so no tie-break pin was adopted.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record; the six-gate claim is pinned-engine expressibility of the declared rule, never a profitability, parity, or trading authorization.

## Adoption boundary

Research-only, not approved. No live, Paper, or Testnet authorization follows from this record. Any downstream standardized overlay (house DCA/capital/leverage), Qlib screening, or Hummingbot re-validation is a separate, explicitly authorized step outside this record.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/ema_rsi_pullback.py (primary source — executable Python strategy, 115 lines, fetched live 2026-10-17 at pinned HEAD commit, 4,039 bytes, SHA-256 `18e68f60…4e23`; RSI helper `forven/scanner.py::rsi` read at the same commit, 464,565 bytes, blob `9a1d77b9`, pure-Wilder passenger; no performance figure ships anywhere in either file)
- https://github.com/judder659/Forven (repository home; HEAD verified `e9a6c09` by `git ls-remote` this cycle)
