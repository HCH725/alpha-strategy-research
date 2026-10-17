---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven linear regression channel breakout long-flat on BTCUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/linear_regression.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven linear regression channel breakout long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation` and `forven-williams-ema-reclaim` records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/linear_regression.py`.
- GitHub blob SHA at the pinned commit: `c9c9f0c6e2172e8f0b9a8931de05387269b90533`, size 4162 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 4162 bytes, 127 lines, SHA-256 `cb640f167bc50948b3cca32dc27983a44aec74c0d9e57ad958ff1a312505acd2` — the entire file was retrieved and inspected; the order-gating rule lives entirely in this one file (ordinary-least-squares channel on `close` only).
- The file's own words (quoted for gate evidence, never extended): module docstring `Linear Regression Channel strategy.`; class docstring `Entry: Price breaks above the upper channel (regression line + num_std * std).` / `Exit: Price drops below the regression line.`; `describe()` returns `Enters when price breaks above the {period}-bar linear regression channel (+{num_std} std). Exits when price drops below the regression line.`; `default_params` returns exactly `{ "period": 50, "num_std": 2.0, "leverage": 1.0 }`; roster entry `("PREBUILT-LINREG", LinearRegressionStrategy, {"_asset": "BTC"})`; `compatible_regimes` returns `{"TREND_UP"}`; `parameter_space()` returns `{ "period": (30, 80, 10), "num_std": (1.5, 3.0, 0.5) }` (a documented search surface only — this record pins the defaults and runs no search).
- Full-file token census (verified by search over the 127 lines this cycle): 1 `direction` literal `"long"` (the sole order-direction token); 0 `short` / 0 `sell` (no short path anywhere); 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` (no order arguments, no risk legs); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 1.0` default); 0 `volume` / 0 `open` / 0 `time` / 0 `request` / 0 `security` / 0 `timeframe` / 0 `barstate` (only `close` is read by any order-gating line); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` (no position-aware state conditions any signal). The single `atr` import (see fence below) feeds a diagnostic passenger only.
- ATR-import fence (quoted, never order-gating): line 50 `from forven.strategies.indicators import atr` resolves through that module's lazy PEP-562 facade (`__getattr__` re-exporting the canonical `forven.scanner.atr`; facade file `forven/strategies/indicators.py`, blob `fdda8b77429e133372482e25cdff8ea31bd59b2a`, 35784 bytes at the pinned commit). The computed `atr_14` value is returned only inside the `indicators={... "atr_14": ...}` diagnostic dict — it appears in zero entry/exit comparisons, so its smoothing variant cannot move a single trade event under this record (see Negative evidence 5).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the 50-bar OLS regression-line construction, the population-σ upper-channel construction, the strict close-cross breakout entry, the below-regression-line exit, the long-only stance, and the no-stop posture — but ships no venue, no timeframe, no fill-timing flag, and no position-sizing rule inside this file. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue; the roster pins `_asset BTC` and the admitted sibling Forven records all execute Binance `BTC/USDT-1h` — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the close — and the admitted S01508, inside-bar, and williams-ema-reclaim records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) an adopted 60-completed-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 52nd completed bar — 50-bar regression seed plus the one-bar previous-window shift plus the decision bar — plus margin; see Required data); (4) house sizing/capital/costs replacing the bare `leverage: 1.0` default (see Execution assumptions; sizing changes no event under the predeclared single-unit rule). The breakout entry, the midline exit, the long-only stance, the entry/exit mutual exclusivity, and the no-stop/no-target/no-time-exit posture are source-verbatim and unmodified.

Pre-write dedup (2026-10-17): working-tree filename/content search for `builtin/linear_regression` / `PREBUILT-LINREG` / `LinReg ` returns zero strategy records — no record cites this source file. The pool cousin `linreg-channel-band-touch-two-sided-btcusdt-1d-2026-10-12.md` (Eterna source, two-sided slope-gated band-touch mean-reversion entries at 100/2.0/50 on `1d`) is fenced as a different mechanism in Negative evidence 7. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: a long-only regression-channel breakout chase is a different signal construction from a two-sided slope-gated band-touch fade, not a threshold re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its three sentences print: a `Linear Regression Channel strategy` that `breaks above the upper channel (regression line + num_std * std)` to enter and `drops below the regression line` to exit. No behavioural, structural, or risk-premium channel is claimed anywhere in the 127 lines. The file ships no performance number of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Regression-channel momentum breakout, long-only, edge-triggered. The 50-bar ordinary-least-squares line through `close` is the fair-value spine; its population-σ envelope (×2.0) is the channel. A close crossing strictly up through the upper rail is bought as trend-acceleration evidence — unlike the pool's Eterna cousin, which fades rail touches back toward the line inside a slope-gated trend, this rule chases the break *away* from the line and holds until price falls back *through* the line itself. There is no trend pre-gate (no EMA, no slope, no ADX): any upper-rail cross-up fires, even from a flat or falling regression. Unlike band-breakout systems there is no volatility denominator from a second indicator — the rail is the regression residual's own dispersion. The failure mode is plain: a rail touch that crosses by a tick and sinks straight back prints a full round-trip loss, and a vertical extension far above the rail is held with no profit-taking leg until the long walk back to the line.

## Signal

Exact rule as pinned (any other period, multiplier, gate polarity, exit leg, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own:

```text
window      = close[-50:]                  // trailing 50 closes, decision bar inclusive
x           = [0..49]
slope, intercept = polyfit(x, window, 1)   // OLS, degree 1
reg_line    = slope * x + intercept
residuals   = window - reg_line
std_dev     = std(residuals)               // population σ (numpy default ddof=0)
reg_value   = reg_line[-1]
upper       = reg_value + 2.0 * std_dev
(prev window shifts everything one bar back: close[-51:-1])
prev_upper  = prev_reg_value + 2.0 * prev_std
entry       = (prev_close <= prev_upper) and (curr_close > upper)
exit_       = (curr_close < reg_value)
```

- Trade events: `entry_signal=bool(entry)`, `exit_signal=bool(exit_)`, `direction="long"` (literal — no short emission exists anywhere in the file, verified by full-file search). A flat book enters one full unit on an entry bar; a long book exits the full unit on an exit bar. Entries while already long are no-ops under the predeclared single-unit rule (see position rule); exits while flat are deterministic no-ops.
- Direction: long-only. The short side is absent by construction (0 `short` / 0 `sell` in the file) and recorded as explicitly disabled. Spot-compatible (no naked shorting required).
- Exits and risk (explicit): the below-regression-line cross is the sole position-ending path. Opposite-signal exit is not applicable (no short leg exists). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence` (a deterministic passenger of distance above the line) and `indicators={reg_value, upper_channel, lower_channel, slope, std_dev, atr_14}` are diagnostic — none conditions any order line.
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further entry bars as no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops. Re-entry re-arms on the next breakout bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Conflict priority (provably irrelevant): entry and exit cannot fire on the same bar. `upper = reg_value + 2.0 * std_dev` with `std_dev >= 0` always, so entry implies `curr_close > reg_value`; exit requires `curr_close < reg_value` — strict inequalities on the same print, mutually exclusive on every bar including the degenerate `std_dev == 0` case (entry then needs `curr_close > reg_value`, still exclusive). Hence every bar resolves to at most one of {entry, exit, neither}. No priority rule is needed and none is missing.
- Determinism note for the reviewer: the rule reads only `close` with two fixed trailing windows (`close.iloc[-period:]`, `close.iloc[-(period+1):-1]`), closed-form `np.polyfit`/`np.std` arithmetic, and one `.iloc[-2]` previous-close read — no `request.*`, `security()`, `timeframe*`, `barstate.*`, volume-weighted logic, session/calendar call, or stop/limit order argument anywhere in the file (verified by the census above returning zero matches). The `min_bars = period + 2` guard plus the `price=0.0` short-circuit return only NaN-free full windows to the arithmetic. The `compatible_regimes` set is metadata never read by the signal path (which takes only `df`/`params`), so no regime model gates any order.

## Required data

- `1h` bars of one pair: `close` only for every order-gating line (regression windows, residual σ, both cross legs). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade/aggressor, L2/order-book, on-chain, options/Greeks, sentiment/news, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line. (`high`/`low` enter only the diagnostic `atr_14` passenger through the quarantined facade import — never an order leg; see Provenance fence.)
- Single decision timeframe `1h` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; every test reads trailing closes of the same series, never a second feed).
- Warmup: 60 completed `1h` bars flat by record rule — structural minimum is the 52nd completed bar (50-bar regression seed, plus the one-bar previous-window shift, plus the decision bar; pre-seed bars return the explicit no-signal guard, verified in code). Pre-warmup bars are flat by record rule; missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (every window reads completed bars only), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (the file names no venue; the roster pins `_asset BTC` — the Binance/BTCUSDT pin is a researcher market choice, disclosed, never presented as source-native).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted S01508, inside-bar, and williams-ema-reclaim records establish same-bar-close as the pinned-compatible lane primitive for this exact repository family. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. Entry and exit cannot co-fire (proven above), so no intrabar ordering assumption is needed at all.
- Engine path for `1h` (gate 5, stated plainly): `1h` is a Binance-documented USDT-M kline interval; the derived rule needs only completed `1h` candles (`close`) on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no funding/OI/mark-price leg. That is the same single-frame completed-bar path as the admitted `1h` siblings from this source family. Anything beyond that single-frame completed-bar path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: the source ships only a bare `leverage: 1.0` default with no capital, fee, slippage, funding, or margin assumption (quoted verbatim in census; the absences are disclosed, never read as zero cost) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior. Under the predeclared single-unit rule the sizing overlay changes no trade event.
- Concurrency: single-unit long-flat book — at most one open long; same-direction refires are no-ops by record rule, the midline cross closes the whole unit, and re-entry is allowed immediately on the next qualifying breakout bar after any exit (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (frozen `period 50 / num_std 2.0` inputs, dual-window OLS regression with population-σ rails, strict close-cross breakout entry, below-line exit, fixed long-only stance with the literal `"long"` direction token, no risk legs) and the `PREBUILT-LINREG` BTC roster pin. It ships no performance number of any kind — this record claims no source-reported performance, and no backtest figure is invented here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` — the sole position-closing path is the coded below-regression-line `exit_`. The absence is coded (the signal block ends with the single `exit_` comparison and only the diagnostic return follows).
2. Variant menus fenced, stated plainly: the `parameter_space()` surface (`period` 30–80, `num_std` 1.5–3.0) is a documented search grid the code never runs — this record freezes the `50/2.0` defaults as written; adopting any grid point would be a different, unpinned rule.
3. Ungated entries fire as written, stated plainly: any strict close-cross above the upper rail fires with no EMA, slope, ADX, or volume gate anywhere in the file — adding any such gate would be a different, unpinned rule. Flat-slope and counter-trend crosses are traded, not vetoed.
4. No averaging down, stated plainly: consecutive breakout bars while already long are no-ops under the predeclared single-unit rule, matching the file's stateless signal (no position-aware branch exists to implement anything else).
5. ATR/metadata quarantine, stated plainly: `atr_14`, `slope`, `lower_channel`, and `confidence` are returned inside `indicators`/diagnostic fields and read by zero order-gating comparisons — treating any of them as a gate, filter, or sizing input would be a different, unpinned rule. The `compatible_regimes == {"TREND_UP"}` set is likewise metadata never read by `generate_signal`.
6. No future leakage in the stack, stated plainly: at decision bar `t`, both OLS windows and the previous-close read use completed-bar closes through `t` with fixed non-negative offsets only (`close.iloc[-50:]`, `close.iloc[-51:-1]`, `close.iloc[-2]`). No `security()`, no `request.*`, no negative index, no `open`/`high`/`low`/`volume` read in any order leg, no `barstate.islast`-gated path; pre-seed bars return the explicit no-signal guard, never a forward read.
7. Pool-cousin fence (Eterna linreg record), stated plainly: `linreg-channel-band-touch-two-sided-btcusdt-1d-2026-10-12.md` trades the same OLS-channel family but is a different mechanism on five axes — different source (Eterna immutable Pine commit vs Forven immutable Python commit here), different entry class (slope-plus-EMA-gated rail-touch fade toward the line vs ungated upper-rail breakout chase away from it), different direction (two-sided vs long-only here), different geometry (`ta.linreg(close,100,0)` + EMA50 + 5-bar slope gate on `1d` vs `polyfit`-50 with no gates on `1h` here), different horizon. This record is therefore never evidence for that rule, and that record is never this rule's provenance.
8. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT market pin, the `1h` frame adoption, same-bar-close fills (with live intrabar behavior scoped out), the adopted 60-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the OLS arithmetic, σ construction, breakout entry, midline exit, order stance, and risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, timing, input set, or the Forven engine's own execution semantics passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `50/2.0` channel / ungated breakout entry / midline exit / long-only / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Breakout-vs-touch relevance: replacing the upper-rail breakout entry with a lower-rail touch-fade entry (same channel, same midline exit) must not improve net expectancy; fail ⇒ the coded breakout-chase entry adds nothing over its touch-fade twin.
- F2 — Midline-exit relevance: replacing the below-line exit with an opposite-rail touch exit (same entries) must not improve net expectancy; fail ⇒ the coded cross-back-through-fair-value exit adds nothing over its opposite-touch twin.
- F3 — No-gate relevance: adding an EMA200 trend gate to the entry (same channel, same exit) must not improve net expectancy; fail ⇒ the coded ungated posture adds nothing over its trend-gated twin.

## Crypto portability

Pinned to BTCUSDT Binance futures `1h` under the house overlay (market pin is a researcher choice on a venue-agnostic source file; the `_asset BTC` roster pin is adopted as venue rationale, not as performance evidence). The channel arithmetic ports across perpetual venues without structural change — it reads completed-bar `close` only, so venue volume-definition differences cannot move the channel at all, disclosed. The rule is long-only with no stop leg, so a spot-only deployment expresses it fully, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the file returns the decision bar's own close but ships no explicit fill-timing flag; this record evaluates completed bars only and executes same-bar-close on `1h` BTCUSDT. Any live intrabar behavior is out of scope.
- Derived market pin: the file names no venue and no timeframe (roster pins `_asset BTC` only) — BTCUSDT `1h` is a researcher market/frame choice for the house universe, never a source claim.
- Source economics are leverage-only: beyond the bare `leverage: 1.0` default the source ships no capital sizing, no fee, no slippage, no funding, and no margin assumption — derived evaluation must carry the full house cost load (fees plus historical funding; no hypothetical zero funding claimed), and this record reports no net performance of its own.
- No price stop, no time stop: adverse excursion after placement has no guardrail beyond the midline cross; a breakout that reverses without ever reclaiming the line is held with no stop, and a winning extension far above the rail keeps running with no profit-taking leg. This is the coded posture, disclosed as the record's principal risk.
- Whipsaw at the rail: a cross-up by a tick followed by an immediate sink prints a full round-trip loss by construction; chop around the upper rail prints repeated entry-then-exit round trips, disclosed.
- Seed bars: the 50-bar dual-window seed dominates early bars; the first 60 `1h` bars are flat by record rule, so early-history signals never enter any evaluation.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record; the six-gate claim is pinned-engine expressibility of the declared rule, never a profitability, parity, or trading authorization.

## Adoption boundary

Research-only, not approved. No live, Paper, or Testnet authorization follows from this record. Any downstream standardized overlay (house DCA/capital/leverage), Qlib screening, or Hummingbot re-validation is a separate, explicitly authorized step outside this record.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/linear_regression.py (primary source — executable Python strategy, 127 lines, fetched live 2026-10-17 at pinned HEAD commit, 4,162 bytes, SHA-256 `cb640f16…5acd`; no performance figure ships anywhere in the file)
- https://github.com/judder659/Forven (repository home; HEAD verified `e9a6c09` by `git ls-remote` this cycle)
