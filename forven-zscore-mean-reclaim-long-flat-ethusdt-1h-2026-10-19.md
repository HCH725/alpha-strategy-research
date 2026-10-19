---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven z-score mean-reclaim washout-recross long-flat on ETHUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/zscore_mean_reclaim.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven z-score mean-reclaim washout-recross long-flat on ETHUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-zscore-mean-reversion`, `forven-ttm-squeeze-momentum-release`, `forven-bb-squeeze-breakout`, `forven-chandelier-exit-long-stop-cross`, and thirty-four other admitted Forven records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`, verified via the GitHub commits API this cycle; verified as the repository HEAD via `git ls-remote` against both `HEAD` and `refs/heads/main` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/zscore_mean_reclaim.py`.
- GitHub blob SHA at the pinned commit: `236f60a19c32d049934a57782b925571cb39dccc`, size 3864 bytes.
- Byte-identity check: the file retrieved from `raw.githubusercontent.com` at the pinned commit is 3864 bytes, 104 lines, SHA-256 `71076562f0f0497f25a382cb017f48b127d4d2a4005716d9ae6f8adae695e4a7`, and `git hash-object` reproduces the GitHub blob (`236f60a1…39dccc`) — the entire file was retrieved twice and inspected (both fetches byte-identical, matching the local cache).
- Registration: the file self-registers via `STRATEGY_CLASS = ZScoreMeanReclaimStrategy`, `TYPE_NAME = "zscore_mean_reclaim"`, and the `STRATEGIES = [("PREBUILT-ZSCORE-MEAN-RECLAIM-ETH", ZScoreMeanReclaimStrategy, {"_asset": "ETH"})]` roster pin. Repo-wide, no other builtin file carries this `TYPE_NAME` or roster name; working-tree search for `zscore_mean_reclaim` / `PREBUILT-ZSCORE-MEAN-RECLAIM` / `ZScoreMeanReclaimStrategy` returns zero strategy records citing this source file.
- The file's own words (quoted for gate evidence, never extended): module docstring `Z-score rebound strategy with EMA context.`; `describe()` returns `Fade a washout when z-score(20) rebounds through -1.5 and price is reclaiming the short-term mean; exit near 0.3.`; `default_params` returns exactly `{ "zscore_window": 20, "zscore_entry": -1.5, "zscore_exit": 0.3, "ema_period": 34, "leverage": 1.5 }`; `compatible_regimes` returns `{"RANGE_BOUND", "HIGH_VOL"}` (metadata never read by the signal path); `parameter_space()` returns `{ "zscore_window": (10, 40, 5), "zscore_entry": (-2.5, -1.0, 0.25), "zscore_exit": (-0.25, 0.75, 0.25) }` (a documented search surface only — this record pins the defaults and runs no search). No performance phrase of any kind ships anywhere in the 104 lines — this record adopts no source-reported performance (see Evidence).
- Twin decision paths, verified lockstep: `generate_signal()` (per-bar) and `generate_signals()` (vectorized) are the only two signal methods — both compute from the single shared `_indicator_frame()` helper (trailing 20-bar rolling mean, trailing 20-bar rolling sample std, lin `zscore = (close - rolling_mean) / rolling_std`, `close.ewm(span=34, adjust=False)` EMA). The per-bar path reads `indicators.iloc[-1]` / `iloc[-2]` (falling back to `current` itself on a degenerate 1-bar frame); the vectorized path reads the same frame with `.shift(1)` and `.fillna(False)`. For every frame with `len > 1`, `iloc[-2]` ≡ `shift(1)` row-for-row, and the entry/exit booleans are algebraically identical; on degenerate frames both paths emit all-`False` (per-bar: the `previous is current` fallback makes the recross conjunction unsatisfiable on one print and single-bar EWM equals close so `close > ema` is `False`; vectorized: shift-NaN → `fillna(False)`). No second construction, no facade import, no `indicators.py` dependency anywhere in the file. This record pins the per-bar `generate_signal` as canonical and the twin as lockstep-equivalent — never two rules to choose between.
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` (12238 bytes, blob `27508a2a6b8c546e21adefdb97fc0144fabf881b`, identical to the blob pinned by the admitted `forven-ttm-squeeze-momentum-release`, `forven-bb-squeeze-breakout`, and `forven-zscore-mean-reversion` records) defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults and `direction: str = "long"` default with direction normalization.
- Full-file token census (verified by search over the 104 lines this cycle): `def generate_signal` once plus `def generate_signals` once (the lockstep twins above — no third path); `direction` on one code line only (the `direction="long"` literal — the sole `short` token anywhere is the `describe()` prose fragment `short-term mean`, never a side); 0 `open` / 0 `volume` reads (the rule consumes `close` only); 0 `rsi` / 0 `macd` / 0 `stoch` / 0 `supertrend` / 0 `ichimoku` / 0 `vwap` / 0 `adx` (no second indicator, no regime filter — the only indicator beside the z-score is the EMA34 exit leg); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 1.5` default, replaced by the house overlay — see Execution assumptions); 0 `funding` / 0 `mark_price` / 0 `request.` / 0 `security(` / 0 `barstate` / 0 `timeframe` in any line; 0 `isna` / 0 `isnull` guards (NaN behaviour disclosed in Negative evidence 3, never invented); 0 `pyramid` / 0 `position_` / 0 `opentrades` / 0 `openprofit` / 0 `cooldown` (no position-aware state conditions any signal); 0 `len(df)` (no length guard ships — the `len(indicators) > 1` ternary plus the 40-bar researcher floor below cover it); `.rolling(` twice (mean + std), `.ewm(` once (EMA34), `.shift(` twice (vectorized twin only), `.fillna(` once (vectorized twin only), `.std()` once — the pandas sample estimator (`ddof=1`, the library default the code does not override), pinned as written; a population denominator would be a different, unpinned rule.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the 20-bar sample-σ z-score, the −1.5 washout-recross entry with the up-day reclaim gate, the dual exit (`z ≥ 0.3` OR `close > EMA34`), and the no-stop long-only posture — but ships no venue spelling beyond the `_asset ETH` roster pin, no timeframe, no fill-timing flag, no warmup guard, no co-fire priority, and no position-sizing rule. Researcher-declared adaptations are exactly five: (1) research market/timeframe `ETHUSDT` `1h` (the roster pins `_asset ETH`; the ETHUSDT lane follows the admitted Forven `1h` siblings including the existing ETHUSDT record — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(float(current["close"]), 4)` — the decision bar's own close — and the thirty-plus admitted Forven records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) single-unit long-flat position pin with hold-no-op semantics plus a 40-bar researcher warmup floor (an already-positioned book treats further recross bars as hold-no-ops, a flat book treats dual-exit bars as no-ops, re-entry re-arms on any qualifying recross bar after any exit with no cooldown, pre-warmup bars flat by record rule — the 40-bar floor covers the 20-bar z-score seed, the EMA34 seeding transient, and the absent length guard in one disclosed rule); (4) exit-priority tie-break on co-fire bars (any bar with `exit_ == True` resolves as exit; entry is processed only when `exit_` is `False` — the exit leg firing means the washout discount is already gone, so the risk-off resolution is to close/skip rather than open; fully specified below, never a source claim); (5) house sizing/capital/costs replacing the bare `leverage: 1.5` default (see Execution assumptions; sizing changes no event under the predeclared single-unit rule). No other behaviour is added, and the z-score arithmetic, the recross-plus-reclaim entry, the dual exit, and the risk posture are source-verbatim.

Pre-write dedup (2026-10-19): working-tree filename/content search for `zscore_mean_reclaim` / `PREBUILT-ZSCORE-MEAN-RECLAIM` / `ZScoreMeanReclaimStrategy` / `TYPE_NAME = "zscore_mean_reclaim"` returns zero strategy records citing this source file. No open `research/*` PR carries this source file (open PRs are only #48/#49/#63/#89/#92/#251/#304 — different mechanisms, indicators, and sources; #304 is the Forven `cci.py` sibling, a different oscillator file with no reclaim gate and no EMA exit leg). Not a duplicate, paraphrase, or trivial parameter variant: a washout-recross-plus-reclaim machine with a dual z/EMA exit is a different signal construction from an oversold level-hold machine — different trigger × different gate × different exit × different immutable source file (see Negative evidence 7 for the five-axis fence against the admitted `zscore_reversion` sibling).

## Economic mechanism

### Source-reported

The source claims only what its sentences print: a `Z-score rebound strategy with EMA context` that fades a washout when the 20-bar z-score rebounds through −1.5 with price reclaiming the short-term mean, exiting near 0.3 (or above the 34-bar EMA). No behavioural, structural, or risk-premium channel is claimed anywhere in the 104 lines. The file ships no backtest numbers of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Washout-rebound timing with trend-confirmation exit, long-only, state-holding. Unlike its admitted level-hold sibling (which buys every bar printed below −2.0 and holds to the mean), this machine buys only the single rebound bar — the washout must first print below −1.5 and then reclaim back through −1.5 on an up-day — so a grinding bleed that never bounces prints nothing, and a V-recovery that gaps straight through fires exactly once. The exit is dual: either the z-score reaches 0.3 (near fair value) or price rises above the 34-bar EMA (trend reclaimed), whichever prints first, so the trade holds the snap-back leg but never rides a re-extension. The failure mode is plain: a dead-cat bounce that reclaims −1.5 on one up-day and immediately rolls over is bought with no stop and no cooldown; a slow bleed that mean-reverts without ever printing below −1.5 is never entered; chop around −1.5 with alternating up-days prints repeated recross entries.

## Signal

Exact rule as pinned (any other z-score window, entry threshold, exit threshold, EMA period, std estimator, reclaim polarity, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own; `_indicator_frame` is the single construction both twins share:

```text
mean      = rolling_mean(close, 20)      // pandas trailing mean, decision bar inclusive
std       = rolling_std(close, 20)       // pandas trailing SAMPLE std, ddof=1 (library default), decision bar inclusive
z         = (close - mean) / std
ema34     = close.ewm(span=34, adjust=False).mean()
reclaim   = (close(t) >= close(t-1))     // up-day gate, flat day counts, pinned as written
entry     = (z(t-1) < -1.5) & (z(t) >= -1.5) & reclaim
exit_     = (z(t) >= 0.3) | (close(t) > ema34(t))
```

- Trade events: `entry_signal=bool(entry)`, `exit_signal=bool(exit_)`, `direction="long"` (literal on the single code line — no short emission exists anywhere in the file; the sole `short` token is `describe()` prose). A flat book enters one full unit on an entry bar; a long book exits the full unit on an exit bar. Entries while already long are hold-no-ops under the predeclared single-unit rule (no pyramiding, no averaging); exits while flat are deterministic no-ops. Re-entry re-arms on the next qualifying recross bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Direction: long-only. The short side is absent by construction (0 `sell`, 0 order-side switch) and recorded as explicitly disabled. Spot-compatible (no naked shorting required).
- Conflict priority (predeclared researcher pin, exit-priority): entry and exit CAN co-fire (a violent rebound bar can print `z(t-1) < -1.5` with `z(t) >= 0.3`, and an up-day reclaim bar very often already prints `close > ema34`). Every such bar resolves as exit: a long book closes the full unit, a flat book stays flat (the exit leg firing means the washout discount is already gone, so opening fresh exposure is the strictly worse resolution). Entry is therefore processed only when `exit_` is `False`. The rule is exhaustive — every bar resolves to exactly one of {enter, exit/close, hold/no-op} — and no priority beyond this sentence is needed or missing.
- Exits and risk (explicit): the dual exit above is the sole position-ending path. Opposite-signal exit is not applicable (no short leg exists). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence = min(1.0, |z| / 3.0)` and `indicators={zscore, rolling_mean, ema, reclaim}` are diagnostic — none conditions any order line.
- Determinism note for the reviewer: the rule reads only `close` with one trailing 20-bar moment window, one 34-bar EWM seed, and one-bar comparisons — no `request.*`, `security()`, `timeframe*`, `barstate.*`, volume-weighted logic, session/calendar call, high/low/open read, or stop/limit order argument anywhere in the file (verified by the census above returning zero matches). The `compatible_regimes == {"RANGE_BOUND", "HIGH_VOL"}` set is metadata never read by the signal path (which takes only `df`/`params`), so no regime model gates any order. The `parameter_space()` grid is a documented search surface the code never runs — this record freezes the `20 / -1.5 / 0.3 / 34` defaults as written; adopting any grid point would be a different, unpinned rule.

## Required data

- `1h` bars of one pair: `close` only for every order-gating line (rolling mean, rolling sample std, EMA34, both recross/exit legs, the up-day compare). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade/aggressor, L2/order-book, on-chain, options/Greeks, sentiment/news, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1h` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; every test reads trailing closes of the same series, never a second feed).
- Warmup: 40 completed `1h` bars flat by record rule (predeclared researcher floor — structural minimum is the 20th completed bar for the z-score seed plus the EMA34 seeding transient plus the absent length guard; pre-window z prints NaN which can only ever evaluate entry-`False`, while a pre-window `close > ema` exit print is suppressed by the floor, both verified in code). Pre-warmup bars are flat by record rule; missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (every window reads completed bars only), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: ETHUSDT Binance futures under the house overlay (the file names no venue; the roster pins `_asset ETH` — the Binance/ETHUSDT pin is a researcher market choice following the admitted Forven `1h` ETHUSDT lane, disclosed, never presented as source-native).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The file returns `price=round(float(current["close"]), 4)` — the decision bar's own close — and the thirty-plus admitted Forven records establish same-bar-close as the pinned-compatible lane primitive for this exact repository family. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity, and the exit-priority pin above fully determines the single co-fire ordering case.
- Engine path for `1h` (gate 5, stated plainly): `1h` is a Binance-documented USDT-M kline interval; the derived rule needs only completed `1h` candles (`close`) on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no funding/OI/mark-price leg. That is the same single-frame completed-bar path as the admitted `1h` siblings from this source family. Anything beyond that single-frame completed-bar path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: the source ships only a bare `leverage: 1.5` default with no capital, fee, slippage, funding, or margin assumption (quoted verbatim in census; the absences are disclosed, never read as zero cost) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior. Under the predeclared single-unit rule the sizing overlay changes no trade event.
- Concurrency: single-unit long-flat book — at most one open long; same-direction refires are hold-no-ops by record rule, the dual exit closes the whole unit (exit-priority on co-fire bars), and re-entry is allowed immediately on the next qualifying recross bar after any exit (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (frozen `20 / -1.5 / 0.3 / 34` inputs, trailing close rolling-mean with sample-σ z-score, washout-recross entry with up-day reclaim gate, dual z/EMA exit, fixed long-only stance with the literal `"long"` direction token, no risk legs) and the `PREBUILT-ZSCORE-MEAN-RECLAIM-ETH` roster pin. It ships no performance number of any kind — this record claims no source-reported performance, and no backtest figure is invented here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` — the sole position-closing path is the coded dual exit. The absence is coded (the signal block ends with the two comparisons and only the diagnostic return follows).
2. Variant menus fenced, stated plainly: the `parameter_space()` surface (`zscore_window` 10–40, `zscore_entry` −2.5–−1.0, `zscore_exit` −0.25–0.75) is a documented search grid the code never runs — this record freezes the `20 / -1.5 / 0.3 / 34` defaults as written; adopting any grid point would be a different, unpinned rule.
3. NaN/seed behaviour disclosed, stated plainly: pre-window z prints NaN, and NaN `< -1.5` / `>= -1.5` / `>= 0.3` evaluate `False` in the per-bar path (the twin path applies `.fillna(False)` to the same effect) — the only pre-window `True`-capable leg is `close > ema`, which the 40-bar floor suppresses by record rule. The file ships no `isna`/`isnull` guard and no `len(df)` guard; the floor plus the `len(indicators) > 1` ternary cover every degenerate frame, verified above. Treating any pre-floor bar as tradable would be a different, unpinned rule.
4. Co-fire resolved by predeclared pin, stated plainly: unlike the level-hold sibling (whose strict-inequality legs are provably exclusive), this file's recross entry and dual exit overlap — a violent rebound bar or an already-above-EMA reclaim bar fires both. The exit-priority pin (exit wins; entry processed only when `exit_` is `False`) is a researcher adaptation disclosed in Provenance, never presented as source-native. Inverting the priority would be a different, unpinned rule.
5. No averaging down, stated plainly: consecutive recross bars while already long are hold-no-ops under the predeclared single-unit rule, matching the file's stateless signal (no position-aware branch exists to implement anything else).
6. Regime/metadata quarantine, stated plainly: `confidence`, `zscore`, `rolling_mean`, `ema`, `reclaim`, and the `compatible_regimes == {"RANGE_BOUND", "HIGH_VOL"}` set are returned inside diagnostic fields or class metadata and read by zero order-gating comparisons — treating any of them as a gate, filter, or sizing input would be a different, unpinned rule.
7. Sibling fence (admitted `forven-zscore-mean-reversion`), stated plainly: `forven-zscore-mean-reversion-long-flat-btcusdt-1h-2026-10-17.md` trades the same z-score word but is a different mechanism on five axes — different trigger (oversold LEVEL `z < -2.0` firing on every deep bar vs washout RECROSS `prev < -1.5 & curr >= -1.5` firing only the rebound bar here), different gate (none vs the up-day `reclaim` conjunction here), different exit (single mean level `z > 0.0` vs dual `z >= 0.3` OR `close > EMA34` here), different thresholds (`-2.0 / 0.0` vs `-1.5 / 0.3 / 34` here), different source (immutable `zscore_reversion.py` vs immutable `zscore_mean_reclaim.py` here, different `TYPE_NAME` and roster name). A deep bleed fires entries on every bar there and nothing here until the bounce; a shallow −1.6 washout with an up-day reclaim fires entry here and nothing there. This record is therefore never evidence for that rule, and that record is never this rule's provenance.
8. Neighbour fences, stated plainly: open PR #304 (Forven `cci.py` oversold-recross) is a different oscillator file (CCI vs sample-σ z-score) with no reclaim gate and no EMA exit leg; `qrs-penalized-rsrs-zscore-timing` trades regression-slope statistics on `1d`, not trailing close moments; `forven-rsi-s00139-washout-cross` and `forven-rsi-boundary-rejection` trade RSI-threshold machines, not z-scores; none shares this file, trigger, gate, or exit.
9. Derivation boundary fenced: the only non-source-native behaviors in this record are the ETHUSDT market pin, the `1h` frame adoption, same-bar-close fills (with live intrabar behavior scoped out), the exit-priority co-fire pin, the adopted 40-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the z-score/sample-σ arithmetic, the recross-plus-reclaim entry, the dual exit, the order stance, and the risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, timing, input set, tie treatment, or the Forven engine's own execution semantics passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `20 / -1.5 / 0.3 / 34` z-score / recross-plus-reclaim entry / dual exit / exit-priority / long-only / `1h` ETHUSDT / same-bar-close fills are frozen.

- F1 — Reclaim-gate relevance: dropping the up-day `reclaim` conjunction (entry = pure `prev < -1.5 & curr >= -1.5` recross, same exits) must not improve net expectancy; fail ⇒ the coded reclaim gate adds nothing over its ungated twin.
- F2 — EMA-exit relevance: dropping the `close > EMA34` exit leg (exit = `z >= 0.3` only, same entry) must not improve net expectancy; fail ⇒ the coded trend-reclaim exit adds nothing over its z-only twin.
- F3 — Recross-vs-level relevance: replacing the recross entry with the sibling-style level entry (`z < -1.5`, same dual exit, same exit-priority) must not improve net expectancy; fail ⇒ the coded rebound-timing entry adds nothing over its level-hold twin.

## Crypto portability

Pinned to ETHUSDT Binance futures `1h` under the house overlay (market pin is a researcher choice on a venue-agnostic source file; the `_asset ETH` roster pin is adopted as venue rationale, not as performance evidence). The z-score arithmetic ports across perpetual venues without structural change — it reads completed-bar `close` only, so venue volume-definition differences cannot move the signal at all, disclosed. The rule is long-only with no stop leg, so a spot-only deployment expresses it fully, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the file returns the decision bar's own close but ships no explicit fill-timing flag; this record evaluates completed bars only and executes same-bar-close on `1h` ETHUSDT. Any live intrabar behavior is out of scope.
- Derived market pin: the file names no venue and no timeframe (roster pins `_asset ETH` only) — ETHUSDT `1h` is a researcher market/frame choice for the house universe, never a source claim.
- Derived co-fire priority: the source fires entry and exit booleans independently with no ordering rule; the exit-priority resolution is a researcher pin (disclosed, risk-off). The opposite priority would trade a different event set.
- Source economics are leverage-only: beyond the bare `leverage: 1.5` default the source ships no capital sizing, no fee, no slippage, no funding, and no margin assumption — derived evaluation must carry the full house cost load (fees plus historical funding; no hypothetical zero funding claimed), and this record reports no net performance of its own.
- No price stop, no time stop: adverse excursion after placement has no guardrail beyond the dual exit; a regime break that pins `z` deeply negative is held with no stop while the anchor slides, and a partial recovery that never reaches `z = 0.3` or the EMA is held indefinitely with no profit-taking leg. This is the coded posture, disclosed as the record's principal risk.
- Dead-cat whipsaw: a one-day reclaim through −1.5 followed by an immediate roll prints a full round-trip loss by construction with no cooldown to slow the next re-entry; chop around −1.5 with alternating up-days prints repeated recross entries, disclosed.
- Seed bars: the 20-bar rolling seed and the EMA34 seeding transient dominate early bars; the first 40 `1h` bars are flat by record rule, so early-history signals never enter any evaluation.
- Sample-std pin: the rolling dispersion is the pandas sample estimator (`ddof=1`); a population denominator would move every `z` print and is a different, unpinned rule.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record; the six-gate claim is pinned-engine expressibility of the declared rule, never a profitability, parity, or trading authorization.

## Adoption boundary

Research-only, not approved. No live, Paper, or Testnet authorization follows from this record. Any downstream standardized overlay (house DCA/capital/leverage), Qlib screening, or Hummingbot re-validation is a separate, explicitly authorized step outside this record.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/zscore_mean_reclaim.py (primary source — executable Python strategy, 104 lines, fetched live 2026-10-19 at pinned HEAD commit, 3,864 bytes, SHA-256 `71076562…d2a695e4`; no performance figure ships anywhere in the file)
- https://github.com/judder659/Forven (repository home; HEAD verified `e9a6c09` by `git ls-remote` this cycle)
