---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven ADL EMA-cross trend-gated long-flat on BTCUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/adl.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven ADL EMA-cross trend-gated long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, and `forven-zscore-mean-reversion` records, plus the S01508 Pine EMA-cross demo).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/adl.py`.
- GitHub blob SHA at the pinned commit: `b3b4be07a49fea41ba06da80593104e3a896fe56`, size 3148 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 3148 bytes, 108 lines, SHA-256 `66652745d15e839a6429925b2f1a92f12f24df9b10b9242bc8181057cfc9e4a7` — the entire file was retrieved and inspected; the order-gating rule lives entirely in this one file (ADL-vs-EMA cross plus a close-momentum gate).
- The file's own words (quoted for gate evidence, never extended): module docstring `Accumulation/Distribution Line strategy.`; class docstring `Entry: ADL crosses above its EMA AND close is trending up.` / `Exit: ADL crosses below its EMA.`; `describe()` returns `Enters when A/D line crosses above its 20-bar EMA and close is trending up. Exits when ADL crosses below EMA.`; `default_params` returns exactly `{ "ema_period": 20, "leverage": 1.0 }`; roster entry `("PREBUILT-ADL", ADLStrategy, {"_asset": "BTC"})`; `compatible_regimes` returns `{"TREND_UP"}`; `parameter_space()` returns `{ "ema_period": (10, 30, 5) }` (a documented search surface only — this record pins the default and runs no search).
- Full-file token census (verified by search over the 108 lines this cycle): 2 `direction` literals, both `"long"` (the no-signal guard plus the signal return — the sole order-direction token); 0 `short` / 0 `sell` (no short path anywhere); 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` (no order arguments, no risk legs); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 1.0` default); 0 `open` / 0 `time` / 0 `request` / 0 `security` / 0 `timeframe` / 0 `barstate` (order-gating reads are exactly four `df[` lines: `high`, `low`, `close`, `volume` — zero reads of any other column); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` (no position-aware state conditions any signal). The 4 `high` / 6 `low` / 3 `volume` lines are all inside the guarded money-flow-multiplier arithmetic and the cumsum below — no second feed. Imports are only `pandas` plus the local `BaseStrategy, Signal` base — no indicator facade, no external feed, no cross-asset import.
- OHLCV fence (quoted line identities): line 49 `high = df["high"]`, line 50 `low = df["low"]`, line 51 `close = df["close"]`, line 52 `volume = df["volume"]` — the complete set of `df[` reads in the file.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the money-flow-multiplier ADL construction, the ADL-vs-EMA20 cross edges, the 5-bar close-momentum gate, the long-only stance, and the no-stop posture — but ships no venue, no timeframe, no fill-timing flag, and no position-sizing rule inside this file. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue; the roster pins `_asset BTC` and the admitted sibling Forven records all execute Binance `BTC/USDT-1h` — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted S01508, inside-bar, williams-ema-reclaim, linreg, and zscore records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) an adopted 30-completed-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 22nd completed bar — the `ema_period + 2` length guard — plus margin for the recursive EMA/cumsum seeding; see Required data); (4) house sizing/capital/costs replacing the bare `leverage: 1.0` default (see Execution assumptions; sizing changes no event under the predeclared single-unit rule). The ADL arithmetic, the cross edges, the momentum gate, the long-only stance, the entry/exit mutual exclusivity, and the no-stop/no-target/no-time-exit posture are source-verbatim and unmodified.

Pre-write dedup (2026-10-17): working-tree filename/content search for `builtin/adl` / `PREBUILT-ADL` / `ADLStrategy` returns zero strategy records — no record cites this source file. Content search for ADL-family records returns only pool cousins fenced as different mechanisms in Negative evidence 7 (`obv-ema-crossover-trend`, `chaikin-oscillator-ad-zero-cross`, `cmf-velocity-zero-cross`, price EMA-cross S01508). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: an ADL-level-vs-own-EMA cross with a close-momentum gate is a different signal construction from an OBV cross, an ADL-MACD-spread cross, a CMF-velocity cross, or a price-EMA cross — not a threshold re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: an `Accumulation/Distribution Line strategy` that `Enters when A/D line crosses above its 20-bar EMA and close is trending up` and `Exits when ADL crosses below EMA`. No behavioural, structural, or risk-premium channel is claimed anywhere in the 108 lines. The file ships no performance number of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Volume-weighted accumulation fade-in, long-only, state-holding. The Money Flow Multiplier `((close - low) - (high - close)) / (high - low)` scores where the close sits inside the bar's range; multiplied by bar volume and cumulated, it is the classic Chaikin A/D line — persistent closes near the high on rising volume lift it, distribution near the low drags it. The rule buys only the moment this line crosses up through its own 20-bar EMA *while* price itself confirms (`close[-1] > close[-6]`): accumulation must agree with price momentum, so a flat-line EMA cross during a dead-cat drift does not fire. Unlike level systems there is no held-entry zone — the entry is a one-bar cross edge (first crossing bar only prints entry; the next bar, already above, prints nothing). The exit is the mirror edge: the first bar the line falls back below its EMA closes the whole unit. The failure mode is plain: chop that whips the ADL around its EMA prints repeated cross-up/cross-down round trips with no stop and no profit-taking leg, and a slow bleed where accumulation never reconfirms simply never enters (opportunity cost, disclosed).

## Signal

Exact rule as pinned (any other period, gate length, edge-vs-level treatment, exit leg, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own:

```text
mfm       = ((close - low) - (high - close)) / (high - low)   // zero-range bars guarded to 1e-10
adl       = cumsum(mfm * volume)                              // Chaikin A/D line, from first available bar
adl_ema   = ewm(adl, span=20, adjust=False)                   // recursive, causal
trend_up  = close[-1] > close[-1-5]                           // lookback is min(5, len-1); always 5 under the guard
cross_up  = (prev_adl <= prev_ema) and (curr_adl > curr_ema)
cross_dn  = (prev_adl >= prev_ema) and (curr_adl < curr_ema)
entry     = cross_up and trend_up
exit_     = cross_dn
```

- Trade events: `entry_signal=bool(entry)`, `exit_signal=bool(exit_)`, `direction="long"` (literal — no short emission exists anywhere in the file, verified by full-file search). A flat book enters one full unit on an entry bar; a long book exits the full unit on an exit bar. Entries while already long are no-ops under the predeclared single-unit rule (see position rule); exits while flat are deterministic no-ops. Because entry is a cross *edge* (not a level), consecutive above-EMA bars print entry exactly once — the crossing bar — with no refire until the line first falls back and re-crosses; coded edge behavior, disclosed, not a missing confirmation.
- Direction: long-only. The short side is absent by construction (0 `short` / 0 `sell` in the file) and recorded as explicitly disabled. Spot-compatible (no naked shorting required).
- Exits and risk (explicit): the ADL cross-down edge is the sole position-ending path. Opposite-signal exit is not applicable (no short leg exists). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence = 0.65` on entry bars (0.0 otherwise) and `indicators={adl, adl_ema, close_trending_up}` are diagnostic — none conditions any order line.
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further entry bars as no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops. Re-entry re-arms only after the line falls back to or below its EMA and a fresh cross-up with trend confirmation prints (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Conflict priority (provably irrelevant): entry and exit cannot fire on the same bar. Entry requires `curr_adl > curr_ema` with `prev_adl <= prev_ema`; exit requires `curr_adl < curr_ema` with `prev_adl >= prev_ema` — joint firing would need `prev_adl == prev_ema` together with `curr_adl` strictly above *and* strictly below `curr_ema`, impossible on every bar including the degenerate guard path (`len < 22` returns neither, coded). Hence every bar resolves to at most one of {entry, exit, neither}. No priority rule is needed and none is missing.
- Determinism note for the reviewer: the rule reads only completed-bar OHLCV with fixed non-negative offsets (`[-1]`, `[-2]`, `[-6]`), closed-form range arithmetic, one `cumsum`, and one recursive `ewm(span=20, adjust=False)` — no `request.*`, `security()`, `timeframe*`, `barstate.*`, funding/OI/mark-price read, session/calendar call, or stop/limit order argument anywhere in the file (verified by the census above returning zero matches). Under the `len < 22` guard the momentum lookback `min(5, len-1)` is identically 5 on every evaluated bar — no length-dependent branch survives into evaluation. The `compatible_regimes == {"TREND_UP"}` set is metadata never read by the signal path (which takes only `df`/`params`); the enforced trend gate is the coded close-vs-close-5 comparison, never the regime label — treating the label as a gate would be a different, unpinned rule.

## Required data

- `1h` bars of one pair: `high`, `low`, `close`, `volume` for the money-flow-multiplier, the cumsum, the EMA, the cross edges, and the momentum gate. No `open` read, no funding, OI, mark/index price, liquidation, trade/aggressor, L2/order-book, on-chain, options/Greeks, sentiment/news, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1h` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; every test reads trailing bars of the same series, never a second feed).
- Warmup: 30 completed `1h` bars flat by record rule — structural minimum is the 22nd completed bar (the `ema_period + 2` length guard; pre-seed bars return the explicit no-signal guard). The extra 8 bars are adopted margin for the recursive `ewm(adjust=False)` and the from-zero `cumsum` seeding to stabilize; pre-warmup bars are flat by record rule. Missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (every window reads completed bars only), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (the file names no venue; the roster pins `_asset BTC` — the Binance/BTCUSDT pin is a researcher market choice, disclosed, never presented as source-native).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted S01508, inside-bar, williams-ema-reclaim, linreg, and zscore records establish same-bar-close as the pinned-compatible lane primitive for this exact repository family. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. Entry and exit cannot co-fire (proven above), so no intrabar ordering assumption is needed at all.
- Engine path for `1h` (gate 5, stated plainly): `1h` is a Binance-documented USDT-M kline interval; the derived rule needs only completed `1h` candles (`high`/`low`/`close`/`volume`) on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no funding/OI/mark-price leg. That is the same single-frame completed-bar path as the admitted `1h` siblings from this source family. Anything beyond that single-frame completed-bar path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: the source ships only a bare `leverage: 1.0` default with no capital, fee, slippage, funding, or margin assumption (quoted verbatim in census; the absences are disclosed, never read as zero cost) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior. Under the predeclared single-unit rule the sizing overlay changes no trade event.
- Concurrency: single-unit long-flat book — at most one open long; same-direction refires are no-ops by record rule, the cross-down edge closes the whole unit, and re-entry is allowed only on a fresh qualifying cross after any exit (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (money-flow-multiplier formula with the `1e-10` zero-range guard, cumulative A/D line, `ewm(span=20, adjust=False)` smoothing, cross-up/cross-down edges, 5-bar close-momentum gate, fixed long-only stance with the literal `"long"` direction token, no risk legs) and the `PREBUILT-ADL` BTC roster pin. It ships no performance number of any kind — this record claims no source-reported performance, and no backtest figure is invented here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` — the sole position-closing path is the coded cross-down edge. The absence is coded (the signal block ends with the two edge comparisons and only the diagnostic return follows).
2. Variant menu fenced, stated plainly: the `parameter_space()` surface (`ema_period` 10–30 step 5) is a documented search grid the code never runs — this record freezes the `20` default as written; adopting any grid point would be a different, unpinned rule.
3. Edge-trigger fires as written, stated plainly: entry prints only on the crossing bar (`prev <= EMA`, `curr > EMA`) with no level-hold and no re-confirmation anywhere in the file — adding a hold-while-above posture, a second-bar confirmation, or dropping the trend gate would each be a different, unpinned rule. A line that rides above its EMA for fifty bars prints exactly one entry, not fifty.
4. No averaging down, stated plainly: the file is stateless (no position-aware branch exists to implement anything else) — an already-long book treats further entry bars as no-ops under the predeclared single-unit rule.
5. Regime/metadata quarantine, stated plainly: `confidence` (fixed 0.65), `adl`, `adl_ema`, `close_trending_up` diagnostics, and the `compatible_regimes == {"TREND_UP"}` set are returned inside diagnostic fields or class metadata and read by zero order-gating comparisons — treating any of them as a gate, filter, or sizing input would be a different, unpinned rule. The enforced uptrend test is the close-vs-close-5 arithmetic, never the regime label.
6. No future leakage in the stack, stated plainly: at decision bar `t`, the multiplier, the cumsum, the recursive EMA, the `[-1]`/`[-2]` edge reads, and the `[-6]` momentum read use completed-bar OHLCV through `t` with fixed non-negative offsets only. No `security()`, no `request.*`, no negative shift, no `open` read in any order leg; pre-seed bars return the explicit no-signal guard, never a forward read.
7. Pool-cousin fence (volume-family records), stated plainly: `obv-ema-crossover-trend-two-sided-btcusdt-1d-2026-10-10.md` crosses a *signed-volume* OBV against its EMA two-sided on `1d`; `chaikin-oscillator-ad-zero-cross-momentum-divergence-two-sided-btcusdt-4h-2026-10-12.md` crosses an ADL *MACD-spread* (fast-minus-slow) through zero with a momentum-divergence overlay two-sided on `4h`; `cmf-velocity-zero-cross-ema200-bracket-two-sided-btcusdt-1d-2026-10-10.md` crosses a 20-bar *CMF-ratio velocity* through zero inside an EMA200 price bracket two-sided on `1d`; `ema-20-50-cross-btcusdt-1h-2026-10-06.md` (Forven S01508) crosses *price* EMAs with no volume input at all. This record crosses the *raw ADL level* against its *single* EMA20 with a 5-bar close-momentum gate, long-flat, on `1h`, from immutable file `builtin/adl.py` — different input construction × different trigger × different gate × different direction scope × different frame × different source file on all five axes. This record is therefore never evidence for those rules, and those records are never this rule's provenance.
8. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT market pin, the `1h` frame adoption, same-bar-close fills (with live intrabar behavior scoped out), the adopted 30-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the MFM/ADL/EMA arithmetic, the cross edges, the momentum gate, the order stance, and the risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, timing, input set, or the Forven engine's own execution semantics passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `ema_period 20` / ADL-vs-EMA cross edges / 5-bar close gate / long-only / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Momentum-gate relevance: dropping the `close[-1] > close[-6]` gate (pure ADL cross-up entry, same exit) must not improve net expectancy; fail ⇒ the coded trend gate adds nothing over its ungated twin.
- F2 — Smoothing-length relevance: replacing the 20-bar ADL EMA with a 50-bar ADL EMA (same edges, same gate, same exit) must not improve net expectancy; fail ⇒ the coded 20-bar smoothing adds nothing over its slower twin.
- F3 — Exit-edge relevance: replacing the ADL cross-down exit with a price-under-EMA20 exit (`close < close.ewm(span=20)` first cross, same entries) must not improve net expectancy; fail ⇒ the coded ADL-mirror exit adds nothing over its price-based twin.

## Crypto portability

Pinned to BTCUSDT Binance futures `1h` under the house overlay (market pin is a researcher choice on a venue-agnostic source file; the `_asset BTC` roster pin is adopted as venue rationale, not as performance evidence). Unlike close-only siblings, this rule reads bar `volume`: venue volume-definition differences (futures trade volume vs spot volume, wash-filtering) can move the ADL print itself — cross-venue porting without re-verification would be a different, unpinned claim, disclosed. The rule is long-only with no stop leg, so a spot-only deployment expresses it fully, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the file returns the decision bar's own close but ships no explicit fill-timing flag; this record evaluates completed bars only and executes same-bar-close on `1h` BTCUSDT. Any live intrabar behavior is out of scope.
- Derived market pin: the file names no venue and no timeframe (roster pins `_asset BTC` only) — BTCUSDT `1h` is a researcher market/frame choice for the house universe, never a source claim.
- Source economics are leverage-only: beyond the bare `leverage: 1.0` default the source ships no capital sizing, no fee, no slippage, no funding, and no margin assumption — derived evaluation must carry the full house cost load (fees plus historical funding; no hypothetical zero funding claimed), and this record reports no net performance of its own.
- No price stop, no time stop: adverse excursion after placement has no guardrail beyond the cross-down edge; chop that whips the ADL around its EMA prints repeated entry-then-exit round trips by construction, and a waterfall where the line never re-crosses up simply never enters (opportunity cost, disclosed). This is the coded posture, disclosed as the record's principal risk.
- Volume-definition sensitivity: the signal cumulates `mfm × volume`, so the venue's volume tape is part of the signal — a venue with different volume semantics prints a different ADL and is a different, unpinned rule.
- Seed bars: the from-zero cumsum and the recursive `ewm(adjust=False)` seeding dominate early bars; the first 30 `1h` bars are flat by record rule, so early-history signals never enter any evaluation. Substituting a seeded/warm-started EMA would move every early print and is a different, unpinned rule.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record; the six-gate claim is pinned-engine expressibility of the declared rule, never a profitability, parity, or trading authorization.

## Adoption boundary

Research-only, not approved. No live, Paper, or Testnet authorization follows from this record. Any downstream standardized overlay (house DCA/capital/leverage), Qlib screening, or Hummingbot re-validation is a separate, explicitly authorized step outside this record.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/adl.py (primary source — executable Python strategy, 108 lines, fetched live 2026-10-17 at pinned HEAD commit, 3,148 bytes, SHA-256 `66652745…c8181057`; no performance figure ships anywhere in the file)
- https://github.com/judder659/Forven (repository home; HEAD verified `e9a6c09` by `git ls-remote` this cycle)
