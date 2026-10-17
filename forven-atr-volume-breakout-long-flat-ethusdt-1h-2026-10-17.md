---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven ATR volume-confirmed breakout long-flat on ETHUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/atr_volume_breakout.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven ATR volume-confirmed breakout long-flat on ETHUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, and `forven-adl-ema-cross` records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/atr_volume_breakout.py`.
- GitHub blob SHA at the pinned commit: `1d3561c76d31966e101a0cdca44fa1f54aaca78d`, size 4193 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 4193 bytes, 118 lines, SHA-256 `1ff4ed8b9d703b287157537d3ca4f7e1a2b5972187bb31473bd9aa6d4e6698ce` — the entire file was retrieved and inspected; the order-gating rule lives in this one file plus exactly one pinned pure helper (the ATR call below).
- The file's own words (quoted for gate evidence, never extended): module docstring `ATR breakout strategy confirmed by expanding volume.`; class docstring `Entry: price breaks above previous close + atr_mult * ATR (breakout confirmation)` — the coded entry is the Donchian-high-plus-ATR form below, which is the stricter, pinned rule; `describe()` returns `Breakout continuation using ATR(14) and volume expansion above 1.2x the 20-bar average.`; `default_params` returns exactly `{ "atr_period": 14, "atr_multiplier": 0.7, "volume_period": 20, "volume_multiplier": 1.2, "breakout_lookback": 20, "exit_ema": 12, "leverage": 2.0 }`; roster entry `("PREBUILT-ATR-VOLUME-BREAKOUT-ETH", ATRVolumeBreakoutStrategy, {"_asset": "ETH"})`; `compatible_regimes` returns `{"TREND_UP", "HIGH_VOL"}`; `parameter_space()` returns `{ "atr_multiplier": (0.5, 1.5, 0.2), "volume_multiplier": (1.0, 2.0, 0.2), "breakout_lookback": (10, 30, 5) }` (a documented search surface only — this record pins the defaults and runs no search).
- ATR helper provenance (the file's only out-of-file call): line 49 `from forven.strategies.indicators import atr` resolves through that module's PEP-562 `__getattr__` facade (`_FACADE_NAMES` includes `"atr"`) to `forven/scanner.py:1946` `def atr(df, period=14)`: true range `max(high - low, |high - prev_close|, |low - prev_close|)` with `ATR = TR.rolling(14).mean()` — a simple rolling mean, not Wilder smoothing. The helper is pure pandas over the passed frame (no DB, no network, no global state in the quoted body); `scanner.py` at the pinned commit is 464565 bytes, blob `9a1d77b90bf214c03aa230a5f46775aab94748bd`, SHA-256 `ad57b37f2d8187c190f4d29941912b830921d2121ae3d9f7d7576e146e313889`. Both layers were read this cycle; the formula above is the complete ATR definition this record uses.
- Full-file token census (verified by search over the 118 lines this cycle): 1 `direction` literal, `"long"` (hardcoded on every return — the sole order-direction token); 0 `short` / 0 `sell` (no short path anywhere); 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` (no order arguments, no risk legs); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 2.0` default); 0 `open` / 0 `time` / 0 `request` / 0 `security` / 0 `timeframe` / 0 `barstate` / 0 `funding` (order-gating reads are `close`, `high`, `volume`, plus `high`/`low`/`close` inside the quoted ATR helper — zero reads of any other column); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` (no position-aware state conditions any signal). Imports are only `pandas` plus the local `BaseStrategy, Signal` base — no cross-asset import, no second feed.
- OHLCV fence (quoted line identities): `close = df["close"]`, `high = df["high"]`, `volume = df.get("volume", pd.Series(1.0, index=df.index, dtype=float))`, `rolling_high = high.shift(1).rolling(20).max()`, `volume_ma = volume.rolling(20).mean()`, `exit_ema = close.ewm(span=12, adjust=False).mean()` — the complete indicator set; `low` is read only inside the pinned ATR helper quoted above.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the ATR-buffered Donchian entry, the 1.2x volume-expansion conjunction, the EMA12 exit, the long-only stance, and the no-stop posture — but ships no venue, no timeframe, no fill-timing flag, and no position-sizing rule inside this file. Researcher-declared adaptations are exactly five: (1) research market/timeframe `ETHUSDT` `1h` (the file names no timeframe and no venue; the roster pins `_asset ETH` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(close, 4)` — the decision bar's own close — and the admitted S01508, inside-bar, williams-ema-reclaim, linreg, zscore, and adl records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) an adopted 30-completed-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 21st completed bar — the `shift(1)` + 20-bar rolling high — plus margin for the ATR/volume-ma seeding; see Required data); (4) house sizing/capital/costs replacing the bare `leverage: 2.0` default (see Execution assumptions; sizing changes no event under the predeclared single-unit rule); (5) a deterministic exit-wins tie-break for the pathological co-fire corner fenced in Negative evidence 7 (disclosed, never source-native). The ATR arithmetic, the entry conjunction, the EMA exit, the long-only stance, and the no-stop/no-target/no-time-exit posture are source-verbatim and unmodified.

Pre-write dedup (2026-10-17): working-tree filename/content search for `builtin/atr_volume` / `PREBUILT-ATR-VOLUME` / `ATRVolumeBreakout` returns zero strategy records — no record cites this source file. Content search for ATR-breakout-family records returns only pool cousins fenced as different mechanisms in Negative evidence 8 (Bookstaber ATR sign-test, pure Donchian 20/10, ALMA-cross-plus-volume-oscillator, engulfing-plus-EMA-plus-volume, STARC/Keltner band breakouts). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: a Donchian-high-plus-ATR-buffer entry *conjoined* with a volume-expansion gate and an EMA-level exit is a different signal construction from a bare channel breakout, a sign-test breakout, or a moving-average cross — not a threshold re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: an `ATR breakout strategy` of `Breakout continuation using ATR(14) and volume expansion above 1.2x the 20-bar average`. No behavioural, structural, or risk-premium channel is claimed anywhere in the 118 lines. The file ships no performance number of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Breakout-with-participation, long-only, state-holding. The entry demands three things at once on the same completed bar: price must clear not just the prior 20-bar high but that high *plus* a 0.7×ATR volatility buffer (so a marginal poke above the level in dead chop does not fire), and the bar's volume must exceed 1.2× its 20-bar average (the push must arrive with expanding participation, not on thin air). The exit is deliberately dumber than the entry — any close back below the 12-bar EMA closes the whole unit — so winners are held through chop above the short average while losers are cut without waiting for a full round trip to the breakdown level. Unlike edge-triggered cross systems there is no one-bar entry event: every bar that holds above the buffered level with volume prints entry, and the predeclared single-unit rule turns refires into no-ops. The failure mode is plain: a level that keeps getting re-tested prints repeated entry-then-EMA-exit round trips with no stop and no profit-taking leg, and a slow grind-up on thin volume never enters at all (opportunity cost, disclosed).

## Signal

Exact rule as pinned (any other buffer, multiplier, lookback, average variant, exit leg, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own:

```text
tr              = max(high - low, |high - prev_close|, |low - prev_close|)
atr             = tr.rolling(14).mean()                              // simple mean, NOT Wilder smoothing
rolling_high    = high.shift(1).rolling(20).max()                    // prior 20 bars, causal
breakout_level  = rolling_high + 0.7 * atr
volume_ok       = volume >= 1.2 * volume.rolling(20).mean()
exit_ema        = close.ewm(span=12, adjust=False).mean()             // recursive, causal
entry           = (close > breakout_level) and volume_ok
exit_           = (close < exit_ema)
```

- Trade events: `entry_signal=bool(entry)`, `exit_signal=bool(exit_)`, `direction="long"` (hardcoded literal — no short emission exists anywhere in the file, verified by full-file search). A flat book enters one full unit on an entry bar; a long book exits the full unit on an exit bar. Entries while already long are no-ops under the predeclared single-unit rule (see position rule); exits while flat are deterministic no-ops. Because entry and exit are *levels* (not edges), a bar that holds above the buffered level prints entry on every such bar — refires are no-ops by record rule, not extra units; coded level behavior, disclosed, not a missing confirmation.
- Direction: long-only. The short side is absent by construction (0 `short` / 0 `sell` in the file) and recorded as explicitly disabled. Spot-compatible (no naked shorting required).
- Exits and risk (explicit): the close-below-EMA12 level is the sole position-ending path. Opposite-signal exit is not applicable (no short leg exists). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence=round(min(1.0, volume / max(volume_ma, 1.0) / 2.0), 4)` and `indicators={rolling_high, atr, breakout_level, volume_ma, volume_ok, exit_ema}` are diagnostic — none conditions any order line.
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further entry bars as no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops. Re-entry re-arms on any qualifying bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Conflict priority (predeclared researcher pin for a fenced theoretical corner only): entry and exit are *nearly* exclusive — the breakout level sits at or above the prior-20-bar high while the 12-bar EMA is a convex combination of closes that normally sits at or below it — but a pathological print (an ancient spike far above the recent range keeping the long-memory EMA elevated while a bar pokes just above the buffered level) could satisfy both strict comparisons on one bar (see Negative evidence 7). On any such bar, **exit wins and the entry is suppressed**: a flat book stays flat, a long book ends flat. The pin is deterministic, disclosed here, and changes no event on any non-pathological bar; no priority rule is missing.
- Determinism note for the reviewer: the rule reads only completed-bar OHLCV with fixed non-negative offsets (`shift(1)`, trailing rolling windows, one recursive `ewm(span=12, adjust=False)`) — no `request.*`, `security()`, `timeframe*`, `barstate.*`, funding/OI/mark-price read, session/calendar call, or stop/limit order argument anywhere in the file (verified by the census above returning zero matches). The singular `generate_signal` path ships no length guard, but every pre-seed window prints NaN and every NaN strict comparison is false, so pre-seed bars deterministically print neither signal — identical to the vectorized `generate_signals` twin's `.fillna(False)` behavior (both paths implement the same conjunction, verified line-for-line this cycle). The `compatible_regimes == {"TREND_UP", "HIGH_VOL"}` set is metadata never read by the signal path (which takes only `df`/`params`); treating the label as a gate would be a different, unpinned rule.

## Required data

- `1h` bars of one pair: `high` (rolling-high level and ATR), `low` and `close` (ATR true range; `close` also for the breakout test and the EMA exit), `volume` (expansion gate). No funding, OI, mark/index price, liquidation, trade/aggressor, L2/order-book, on-chain, options/Greeks, sentiment/news, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line. No `open` read anywhere.
- Single decision timeframe `1h` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; every test reads trailing bars of the same series, never a second feed).
- Warmup: 30 completed `1h` bars flat by record rule — structural minimum is the 21st completed bar (the `shift(1)` + 20-bar rolling high is the longest seed; ATR needs 14, the volume average needs 20). The extra 9 bars are adopted margin for the recursive `ewm(adjust=False)` seeding to stabilize; pre-warmup bars are flat by record rule. Missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (every window reads completed bars only), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar. The `df.get("volume", 1.0-constant)` fallback never triggers on the declared Binance venue (volume is always present); if it ever did, the constant tape would force `volume_ok` false and suppress all entries deterministically (see Negative evidence 6).

## Execution assumptions

- Research market: ETHUSDT Binance futures under the house overlay (the file names no venue; the roster pins `_asset ETH` — the Binance/ETHUSDT pin is a researcher market choice, disclosed, never presented as source-native).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The file returns `price=round(close, 4)` — the decision bar's own close — and the admitted S01508, inside-bar, williams-ema-reclaim, linreg, zscore, and adl records establish same-bar-close as the pinned-compatible lane primitive for this exact repository family. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. Entry and exit co-fire only in the fenced pathological corner, resolved by the predeclared exit-wins pin above — no intrabar ordering assumption is needed beyond it.
- Engine path for `1h` (gate 5, stated plainly): `1h` is a Binance-documented USDT-M kline interval; the derived rule needs only completed `1h` candles (`high`/`low`/`close`/`volume`) on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no funding/OI/mark-price leg. That is the same single-frame completed-bar path as the admitted `1h` siblings from this source family. Anything beyond that single-frame completed-bar path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: the source ships only a bare `leverage: 2.0` default with no capital, fee, slippage, funding, or margin assumption (quoted verbatim in census; the absences are disclosed, never read as zero cost) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior. Under the predeclared single-unit rule the sizing overlay changes no trade event.
- Concurrency: single-unit long-flat book — at most one open long; same-direction refires are no-ops by record rule, the EMA12 level closes the whole unit, and re-entry is allowed on any qualifying bar after any exit (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (SMA-based ATR(14) via the pinned helper, prior-20-bar high plus 0.7×ATR buffer, 1.2× 20-bar volume-expansion conjunction, EMA12 exit level, fixed long-only stance with the literal `"long"` direction token, no risk legs) and the `PREBUILT-ATR-VOLUME-BREAKOUT-ETH` roster pin. It ships no performance number of any kind — this record claims no source-reported performance, and no backtest figure is invented here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` — the sole position-closing path is the coded EMA12 level. The absence is coded (the signal block ends with the two comparisons and only the diagnostic return follows).
2. Variant menu fenced, stated plainly: the `parameter_space()` surface (`atr_multiplier` 0.5–1.5 step 0.2, `volume_multiplier` 1.0–2.0 step 0.2, `breakout_lookback` 10–30 step 5) is a documented search grid the code never runs — this record freezes the `0.7` / `1.2` / `20` defaults as written; adopting any grid point would be a different, unpinned rule. `atr_period`, `volume_period`, and `exit_ema` are not even searchable — frozen constants.
3. Level-trigger fires as written, stated plainly: entry prints on *every* bar holding above the buffered level with volume (not just the first breakout bar) — adding an edge-only-first-bar posture would be a different, unpinned rule. Under the predeclared single-unit rule the refires are deterministic no-ops, so level-vs-edge changes no event here; the distinction is fenced so the reviewer never mistakes this for a cross-edge system.
4. No averaging down, stated plainly: the file is stateless (no position-aware branch exists to implement anything else) — an already-long book treats further entry bars as no-ops under the predeclared single-unit rule.
5. Regime/metadata quarantine, stated plainly: `confidence`, the six `indicators` fields, and the `compatible_regimes == {"TREND_UP", "HIGH_VOL"}` set are returned inside diagnostic fields or class metadata and read by zero order-gating comparisons — treating any of them as a gate, filter, or sizing input would be a different, unpinned rule. Quirk disclosed: on pre-seed NaN bars `min(1.0, NaN)` evaluates to `1.0` in Python semantics, so the diagnostic confidence can print `1.0` while entry/exit print false — a passenger artifact that conditions nothing.
6. Volume-fallback path fenced, stated plainly: `df.get("volume", <1.0-constant>)` means a venue without a volume column would feed a flat 1.0 tape, for which `1.0 >= 1.2 * 1.0` is false on every bar — entries deterministically impossible, never a fabricated signal. On the declared Binance venue the column is always present and this path is dormant.
7. Co-fire corner fenced with the predeclared pin, stated plainly: entry needs `close > rolling_high + 0.7·ATR`, exit needs `close < EMA12`. On ordinary prints the buffered level sits above the short average and both cannot hold; a pathological print (a far-ancient spike keeping the infinite-memory EMA12 elevated above a depressed 20-bar range while one bar pokes just over the buffer) could satisfy both. The contribution math makes this vanishingly narrow (a 20-bar-old spike contributes ~0.5% of its size to a span-12 EMA), and any such bar resolves deterministically via the predeclared exit-wins pin in Signal — no ordering ambiguity is left open, and no reviewer invention is required.
8. Pool-cousin fence (breakout/volume-family records), stated plainly: `donchian-20-10-breakout-btcusdt-1h-2026-10-06.md` is a *bare* 20-high/10-low channel breakout with no ATR buffer, no volume leg, and a channel-low exit on BTCUSDT `1h`; `bookstaber-atr-momentum-breakout-reversal-btcusdt-1d-2026-10-05.md` is an ATR-normalized one-bar close-change sign test, two-sided with opposite-signal exits and no volume or Donchian leg, on `1d` from an FMZ source; `alma-cross-volume-gate-btcusdt-1d-2026-10-09.md` trades an ALMA 60/120 cross gated by a volume-momentum oscillator with fixed-percentage TP/SL on both sides, on `1d` from an FMZ source; `dual-ema-engulfing-volume-long-btcusdt-1h-2026-10-07.md` requires a bullish-engulfing pattern over dual-EMA alignment with volume confirmation and exits on bearish engulfing, on BTCUSDT `1h` from an FMZ source; STARC/Keltner band-breakout records use SMA/EMA-centered ATR bands, not a Donchian-high-plus-buffer with a volume conjunction. This record conjoins a *buffered Donchian level* with a *volume-expansion gate* and exits on an *EMA level*, long-flat, on ETHUSDT `1h`, from immutable file `builtin/atr_volume_breakout.py` — different input construction × different trigger × different gate × different exit × different direction scope × different asset × different source file. This record is therefore never evidence for those rules, and those records are never this rule's provenance.
9. Derivation boundary fenced: the only non-source-native behaviors in this record are the ETHUSDT market pin, the `1h` frame adoption, same-bar-close fills (with live intrabar behavior scoped out), the adopted 30-bar warmup with record-rule pre-warmup flat, house sizing/costs, and the exit-wins tie-break for the fenced corner — all predeclared above; the ATR arithmetic, the entry conjunction, the EMA exit, the order stance, and the risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, timing, input set, or the Forven engine's own execution semantics passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `0.7` ATR buffer / `1.2` volume gate / 20-bar high / EMA12 exit / long-only / ETHUSDT `1h` / same-bar-close fills are frozen.

- F1 — Volume-gate relevance: dropping the `volume_ok` conjunction (pure buffered-Donchian entry, same exit) must not improve net expectancy; fail ⇒ the coded participation gate adds nothing over its ungated twin.
- F2 — Buffer relevance: replacing the `+ 0.7·ATR` buffer with the bare prior-20-bar high (same volume gate, same exit) must not improve net expectancy; fail ⇒ the coded volatility buffer adds nothing over its unbuffered twin.
- F3 — Exit-level relevance: replacing the EMA12 exit with the prior-20-bar-low channel exit (same entries) must not improve net expectancy; fail ⇒ the coded EMA exit adds nothing over its Donchian-mirror twin.

## Crypto portability

Pinned to ETHUSDT Binance futures `1h` under the house overlay (market pin is a researcher choice following the file's `_asset ETH` roster pin; the file itself is venue-agnostic). Unlike close-only siblings, this rule reads bar `volume`: venue volume-definition differences (futures trade volume vs spot volume, wash-filtering) can move both the expansion gate and the average itself — cross-venue porting without re-verification would be a different, unpinned claim, disclosed. The rule is long-only with no stop leg, so a spot-only deployment expresses it fully, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the file returns the decision bar's own close but ships no explicit fill-timing flag; this record evaluates completed bars only and executes same-bar-close on ETHUSDT `1h`. Any live intrabar behavior is out of scope.
- Derived market pin: the file names no venue and no timeframe (roster pins `_asset ETH` only) — ETHUSDT `1h` is a researcher market/frame choice for the house universe, never a source claim.
- Source economics are leverage-only: beyond the bare `leverage: 2.0` default the source ships no capital sizing, no fee, no slippage, no funding, and no margin assumption — derived evaluation must carry the full house cost load (fees plus historical funding; no hypothetical zero funding claimed), and this record reports no net performance of its own.
- No price stop, no time stop: adverse excursion after placement has no guardrail beyond the EMA12 level; a level that keeps getting re-tested prints repeated entry-then-exit round trips by construction, and a grind-up on thin volume never enters (opportunity cost, disclosed). This is the coded posture, disclosed as the record's principal risk.
- Volume-definition sensitivity: the signal gates on `volume >= 1.2 × volume_ma(20)`, so the venue's volume tape is part of the signal — a venue with different volume semantics prints different gates and is a different, unpinned rule.
- Seed bars: the 20-bar rolling windows and the recursive `ewm(adjust=False)` seeding dominate early bars; the first 30 `1h` bars are flat by record rule, so early-history signals never enter any evaluation. Substituting a seeded/warm-started average would move every early print and is a different, unpinned rule.
- Theoretical co-fire corner: see Negative evidence 7 — resolved by the predeclared exit-wins pin; on all ordinary prints entry and exit are mutually exclusive by construction.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record; the six-gate claim is pinned-engine expressibility of the declared rule, never a profitability, parity, or trading authorization.

## Adoption boundary

Research-only, not approved. No live, Paper, or Testnet authorization follows from this record. Any downstream standardized overlay (house DCA/capital/leverage), Qlib screening, or Hummingbot re-validation is a separate, explicitly authorized step outside this record.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/atr_volume_breakout.py (primary source — executable Python strategy, 118 lines, fetched live 2026-10-17 at pinned HEAD commit, 4,193 bytes, SHA-256 `1ff4ed8b…6d4e6698ce`; ATR helper `forven/scanner.py:1946` read at the same commit, 464,565 bytes, blob `9a1d77b9`, SHA-256 `ad57b37f…13889`; no performance figure ships anywhere in either file)
- https://github.com/judder659/Forven (repository home; HEAD verified `e9a6c09` by `git ls-remote` this cycle)
