---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven Ichimoku 9/26/52 Tenkan-Kijun cross cloud-gated long-flat on BTCUSDT 1h
created: 2026-10-23
updated: 2026-10-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-23
sources:
  - https://github.com/judder659/Forven/blob/05f026afa719536351e77b7a38afadab6391e3d2/forven/strategies/builtin/ichimoku.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven Ichimoku 9/26/52 Tenkan-Kijun cross cloud-gated long-flat on BTCUSDT 1h

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source Forven crypto strategy collection; the same lane that supplied the admitted `forven-ema-cross-adx-regime`, `forven-macd-cross-adx-regime`, `forven-donchian-regime`, `forven-rsi-s00139`, and `forven-stochastic-k20-recross` records — this is a further record in that lane, and the first pinned to this exact file).
- Pinned commit SHA: `05f026afa719536351e77b7a38afadab6391e3d2` (committer date `2026-10-23T00:37:40Z`, merge PR #266; verified via the GitHub commits API this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/ichimoku.py`.
- GitHub blob SHA at the pinned commit: `14fb8825e2ccfe041014db200441e89f9c8bd2c6`, size 5871 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 5871 bytes, 159 lines, SHA-256 `906207511ebb31e6bdb0cc48cd8e76291992013446f1f81d0eb4887d642cc2a4`, identical to the GitHub blob (`git hash-object` reproduces `14fb8825…f9c8bd2c6`) — the entire file was retrieved and inspected.
- Registration: the file defines class `IchimokuStrategy` with `TYPE_NAME = "ichimoku"` (line 7) and the `STRATEGIES` roster (lines 157–158) `[("PREBUILT-ICHIMOKU", IchimokuStrategy, {"_asset": "BTC"})]`. Identity here is class plus file path plus the pinned `PREBUILT-ICHIMOKU` roster leg, all unique. This record pins ONLY this file's literals below, and no reviewer repair may substitute a sibling constant, a sibling gate, or a sibling threshold.
- The file's own words (quoted for gate evidence, never extended): `default_params` are `tenkan_period: 9`, `kijun_period: 26`, `senkou_b_period: 52`, `leverage: 1.0` (lines 30–36); `generate_signals` is declared "the SINGLE source of entry/exit logic" (line 51); `tenkan = (high.rolling(9).max() + low.rolling(9).min()) / 2`, `kijun` the 26-bar mirror (lines 62–64); `senkou_a = ((tenkan + kijun) / 2).shift(26)`, `senkou_b = ((high.rolling(52).max() + low.rolling(52).min()) / 2).shift(26)` (lines 66–68); `cross_up = (prev_tenkan <= prev_kijun) & (tenkan > kijun)`, `cross_down = (prev_tenkan >= prev_kijun) & (tenkan < kijun)` (lines 78–79); `entry = cross_up & above_cloud`, `exit_ = cross_down` (lines 81–82), both ending in `.fillna(False)` (line 83); `generate_signal` delegates both flags from `generate_signals` (`entries.iloc[-1]`, `exits.iloc[-1]`) with the `direction="long"` literal (lines 123–135); the single-shot guard is `min_bars = senkou_b_p + kijun_p + 2` = 80 bars flat (line 97).
- Out-of-file call pinned (resolved by name through the lazy facade): `from forven.strategies.indicators import atr` (line 86) hits the `_FACADE_NAMES` set (lines 864–875, `"atr"` allowlisted) plus the PEP-562 `__getattr__` hook (lines 879–883), which re-exports the canonical `forven.scanner` implementation — a single implementation, never redefined. The resolved ATR feeds ONLY the `confidence` scalar and the `atr_14` indicator echo (lines 111–143) — it conditions no order-gating line anywhere (fenced in Negative evidence).
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` (12238 bytes, blob `27508a2a6b8c546e21adefdb97fc0144fabf881b` — reproduced via `git hash-object` this cycle) defines the `Signal` dataclass with `entry_signal: bool = False` / `exit_signal: bool = False` defaults, `direction: str = "long"` default, plus a `__post_init__` flag/direction normalization hook — flags arriving as strict booleans (as here, via `bool(...)`) pass through as booleans.
- Full-file token census (verified over the 159 lines this cycle): 2 `direction="long"` (the only direction literals) and 0 short-direction tokens; 0 `short` / 0 `enter_short` / 0 `exit_short` / 0 `can_short`; 0 `stop` / 0 `limit` / 0 `profit` / 0 `qty` / 0 `trail` (no order arguments, no risk legs of any kind); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the scoped-out `leverage: 1.0` default); 0 `volume` / 0 `funding` / 0 `mark_price` / 0 `request` / 0 `security` / 0 `open` (the gating path reads `high`/`low`/`close` only); 0 `pyramid` / 0 `position_size` / 0 `position_adjust` / 0 `opentrades` / 0 `cooldown` (no position-aware state conditions any signal); 0 `resample` / 0 `merge` / 0 `informative` / 0 `hyperopt` (no tuning surface, no second frame); 1 `parameter` (the `parameter_space` optimizer ranges, unused — like its lane siblings); 10 `shift` (the two +26 cloud displacements, the two 1-bar prev-lags, all causal — negative-shift count is zero); 2 `fillna` (the twin-leg `fillna(False)` pair).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Forven deployment. The source pins the textbook 9/26/52 Ichimoku construction, the Tenkan-above-Kijun edge-cross entry with its above-cloud conjunct, the Tenkan-below-Kijun cross-down single exit, the long-only stance, the 80-bar minimum-bars guard, and the no-stop/no-target/no-trailing/no-time-exit posture — but ships no venue spelling, no timeframe, no fill-timing flag, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market BTCUSDT on Binance perpetual under the house overlay (the file is pair-agnostic and venue-agnostic; `_asset` is a label only, and no source-market equivalence is claimed); (2) decision frame `1h` (the file names no timeframe — disclosed researcher choice, never a file semantic); (3) completed-bar decisions with same-bar-close market fills — the decision bar's own close (disclosed, never presented as the source harness's timing); (4) single-unit position pin with hold-no-op semantics (the file carries no position reference — disclosed, never presented as source-native behaviour) plus admission sizing/costs on the explicit house overlay. This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-23): working-tree filename/content search for `builtin/ichimoku.py`, `IchimokuStrategy`, and `PREBUILT-ICHIMOKU` returns zero strategy records citing this source file, class, or roster leg. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian band-ratio) trades a Tenkan-Kijun cross rule. The pool's four Ichimoku neighbours are fenced as different constructions in Negative evidence 8. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy when the 9-bar Tenkan-sen crosses up through the 26-bar Kijun-sen while the close stands above the 52-bar Ichimoku cloud; sell when Tenkan-sen crosses back down through Kijun-sen. The file ships no stop, no target, no trailing, no time exit, no sample, no window, no trade count, and no cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Textbook-cloud breakout machine with a displacement passport, long-only. Unlike state systems that stay long whenever Tenkan exceeds Kijun, this one buys only the *crossing* bar — a market that drifts sideways with Tenkan pinned above Kijun fires nothing after the first edge, and a market whose cross prints under the cloud is refused the passport no matter how sharp the angle. The cloud itself is a 26-bar-delayed construction (both spans read values projected 26 bars earlier), so the passport compares today's close against a cloud anchored in last month's tape — in a fast vertical tape the price outruns the stale cloud and every cross qualifies; in a chop the cloud catches up and gates entries out. The exit is impatient and ungated: any cross down closes the leg even with price still above the cloud. With no stop anywhere, the failure modes are plain: an entry whose Tenkan never crosses back down is held to the sample end, and a cross-up/ cross-down flicker across adjacent bars whipsaws the book with no cooldown to damp the round trips (disclosed as the principal friction).

## Signal

Exact rule as pinned (any other Tenkan/Kijun/Senkou-B period, displacement, gate, edge-vs-state pairing, exit leg, frame, or book is a different, unpinned rule). All variants are file literals, never library defaults:

```text
tenkan[t]   = (max(high[t-8..t]) + min(low[t-8..t])) / 2        // rolling 9, causal
kijun[t]    = (max(high[t-25..t]) + min(low[t-25..t])) / 2      // rolling 26, causal
senkou_a[t] = (tenkan[t-26] + kijun[t-26]) / 2                  // +26 displacement reads older bars only
senkou_b[t] = (max(high[t-77..t-26]) + min(low[t-77..t-26])) / 2 // 52-window ending 26 bars back
cloud_top[t]= max(senkou_a[t], senkou_b[t])                     // NaN spans fall back to close[t] (fenced)
above[t]    = (close[t] > cloud_top[t])
cross_up[t] = (tenkan[t-1] <= kijun[t-1]) & (tenkan[t] > kijun[t])   // fires FROM equality
cross_dn[t] = (tenkan[t-1] >= kijun[t-1]) & (tenkan[t] < kijun[t])
entry       = cross_up[t] & above[t]     // one-bar edge pair, strict
exit_       = cross_dn[t]               // one-bar edge, strict, cloud-ungated
floor       = leading-window bars: NaN comparisons false, then .fillna(False); first 80 bars flat
```

- Trade events: `entry` fires on the cross-up bar only when the close clears the displaced cloud (one-bar edge conjunction, not a persistent state — a book already positioned treats it as a hold-no-op under the position pin below); `exit_` fires on the cross-down bar only, with no cloud leg. `direction` long-only; the two `direction="long"` literals plus zero short-leg tokens is the complete direction set.
- Exact boundaries (pinned semantics): the cross-up FIRES from a tied prior bar (`prev_tenkan <= prev_kijun` — equality qualifies) into a strict exceed; the cross-down FIRES from a tied prior bar (`>=`) into a strict undercut. Touching the cloud edge (`close == cloud_top`) fires neither entry conjunct (strict `>`). Strictness preserved throughout, disclosed, never smoothed.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `tenkan[t] > kijun[t]` while any exit bar has `tenkan[t] < kijun[t]` — mutually exclusive on every bar, degenerate or otherwise, so entry and signal-exit never co-print on the same decision bar. No ordering assumption exists to verify.
- Displacement causality (pinned, not leakage): both `.shift(26)` calls move values to LATER row labels, i.e. each displaced span at bar `t` is computed exclusively from bars at or before `t-26` — a past reference with a 26-bar staleness, never a future reference. No negative shift, no `.shift(-n)`, no forward reference exists anywhere in the file.
- Earliest-fire arithmetic (coded, disclosed): `senkou_b[t]` is the last span to seed, defined for `t >= 77`; the cross needs one prior bar. The vectorized twin could therefore print no earlier than bar 77 — and the file's own single-shot `min_bars = 80` guard plus this record's 80-bar floor both dominate it (fenced in Negative evidence 5).
- Exits and risk (explicit): the cross-down signal leg is the complete position-closing set. No stop, no target, no trailing, no time exit — explicitly none further, matching the file's zero risk-leg census, not invented. No exit leg reads net profit, fees, or funding — fees change only the performance report, never whether an exit fires (disclosed).
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further cross-up bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats cross-down bars as no-ops; re-entry re-arms on any qualifying gated cross after any exit (no source cooldown exists — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low`/`close` with fixed non-negative offsets — two explicit one-bar lags, trailing rolling maxima/minima, and backward displacements, no forward reference. The ATR import resolves to the vendored scanner but feeds display echoes only. No funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `1h` bars of BTCUSDT: `high`/`low` (Donchian-midpoint legs and both cloud spans) and `close` (cloud comparison and fill). No `open` read, no bar `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1h` (researcher pin, disclosed — the file names no timeframe). One evaluation per completed bar; every window reads the decision bar's causal past only (plus the decision bar's own completed print); fills land on the decision bar's own close under the derived rule below.
- Warmup (source-native guard, adopted verbatim): the first 80 completed `1h` bars held flat (`min_bars = senkou_b_p + kijun_p + 2` — a file literal, never a researcher invention). Covers the 78-bar Senkou-B-plus-displacement seed with margin; rolling windows print NaN until seeded and every strict NaN comparison is false, so no leg can fire early in any case. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice of the `PREBUILT-ICHIMOKU` roster leg — the source roster pins `_asset BTC` for this leg; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills (`price=round(curr_close, 4)` — the decision bar's own close), compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same lane primitive the thirty admitted Forven-sibling records use. No maker-touch, queue, or intrabar-path-dependent fill: the only legs are bar-close-evaluated market entry/exit orders, and no bar ever co-fires both legs (see Signal), so no ordering assumption exists to verify. No connector-name literal is declared anywhere in this record — venue spelling resolves downstream, never as an unverified engine path.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its `leverage: 1.0` default is replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one long position at any time; same-side cross-up bars hold without adds; cross-down bars on a flat book are no-ops; any open long ends on the first cross-down bar regardless of cloud position. Re-entry after an exit needs only the next qualifying gated cross (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (159 lines: 9/26/52 literals, displaced cloud arithmetic, edge-cross pair with pinned equality semantics, above-cloud conjunct, long-only flags, 80-bar guard, roster, defaults) and the documented facade resolution to the canonical scanner ATR. It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: every rolling window prints NaN until seeded and every strict NaN comparison is false; `fillna(False)` holds all of them flat. The 80-bar record-rule floor additionally holds every pre-seed bar flat — the floor value itself is a source literal (`min_bars`), adopted verbatim, never misattributed.
2. NaN-fallback fence: where a Senkou span is still NaN, the code substitutes the decision bar's own close (`senkou_*_eff`, lines 71–72; same fallback in the per-bar path, lines 116–117) — during warmup `cloud_top == close` so `above_cloud` is deterministically False. The fallback can only narrow (never widen) entry eligibility, is coded behaviour disclosed as read, and is moot under the 80-bar floor either way.
3. Equality-strictness fence: cross-up fires from a tied prior bar but needs a strict exceed on the decision bar; cross-down mirrors it; `close == cloud_top` fires nothing. A tie on the decision bar itself (`tenkan == kijun`) fires neither leg. Strictness preserved throughout — disclosed, not smoothed.
4. No-state-confusion fence: both legs are one-bar cross edges with single-bar lags — converting either leg to a persistent Tenkan/Kijun positional state (or vice versa) would be a different, unpinned rule with different trade events (states would re-fire across consecutive bars; edges fire once).
5. Twin-divergence fence: the single-shot `generate_signal` returns flat for `len(df) < 80` while the vectorized `generate_signals` twin could in principle print at bar 77–79 — this record pins the VECTORIZED twin as the rule (honouring the file's own "SINGLE source" declaration) and floors the first 80 bars flat by record rule, which dominates both. No reviewer choice between twins is required.
6. Display-only fence: the resolved `atr`, the `confidence` scalar (including its `0.5` NaN-branch value), the six-key `indicators` echo dict, the `parameter_space` ranges, the `compatible_regimes` label set, the `describe()` prose, the `leverage: 1.0` default, and the `_asset` label gate nothing — none of them conditions any order-gating line under default params. The cloud is the only regime concept the rule reads, and it reads it as arithmetic, never as the label.
7. No-division fence: the entire gating path divides only by the constant 2 (midpoint halves) — no rolling divisor, no zero-range denominator, no `1e-9` floor is load-bearing here. Zero-range bars propagate deterministically through max/min comparisons with no NaN branch.
8. Cousin records fenced as different constructions (none trades a bare 9/26/52 Tenkan-Kijun edge-cross with an above-cloud conjunct and a cloud-ungated cross-down-only exit, long-flat, zero auxiliary gates): the admitted `ichimoku-cloud-adx-trend-filter` pool-mate trades a positional Tenkan> Kijun STATE (no edge) inside a five-leg conjunction with Chikou momentum, displaced-cloud position, ADX < 45 and +DI > −DI, two-sided on `1d` (a fresh cross under ADX 50 fires an entry here but nothing there; a held Tenkan-above-Kijun tape fires entries there but nothing here); the admitted `ichimoku-macd-triple-confirm` pool-mate adds a MACD-crossover gate and Chikou leg on the ETH `1h` roster, two-sided (a MACD-bearish cross-up fires here but nothing there); the admitted `ichimoku-rsi-gated` pool-mate adds an RSI-50 gate and Chikou leg, two-sided on `1d` (an RSI-60 cross-up fires here but nothing there); the admitted `octa-ema-ichimoku-trend` pool-mate trades an EMA(11/34) average against a displaced SenkouA with NO Tenkan/Kijun cross leg at all (different signal family outright). Not a re-tuning of any of them: moving any period, dropping the cloud conjunct, converting either edge to a state, adding any auxiliary gate, or enabling the short side would each be a different, unpinned rule — none is admitted here.
9. Sibling-file fence: `rsi_momentum.py`, `rsi_momentum_s00139.py`, `ema_cross.py`, `macd.py`, `supertrend.py`, `donchian_regime.py`, and every other Forven builtin are separate pins — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
10. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-perpetual market choice, the `1h` frame, the same-bar-close fills, the single-unit/no-add/no-cooldown position pin, and house sizing/costs held on the explicit overlay — all predeclared above. The 9/26/52 construction with its +26 displacements, the edge forms with pinned equality semantics, the above-cloud conjunct, the cross-down-only exit, the 80-bar guard, the long-only stance, and the no-risk-leg posture are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 9/26/52 periods with pinned displacements / edge forms with pinned equality semantics / above-cloud conjunct / cross-down-only exit / long-only single-unit / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Cloud-gate relevance: entering on every Tenkan-Kijun cross-up without the above-cloud conjunct (same exit otherwise) must not improve net expectancy; fail ⇒ the coded displacement passport adds nothing over its ungated twin.
- F2 — Exit-leg relevance: holding entries to sample end (no cross-down leg, same entries) must not improve net expectancy; fail ⇒ the coded cross-down exit adds nothing over buy-and-hold.
- F3 — Edge-vs-state relevance: entering on every bar printing Tenkan above Kijun as a persistent state (same cloud conjunct, same exit form) must not improve net expectancy; fail ⇒ the coded one-bar edge adds nothing over its state twin.

## Crypto portability

BTCUSDT Binance perpetual `1h` is the research pin (source names no market; the `1h` frame is a researcher choice on a timeframe-free source). Long-only with full-unit open/close expresses identically on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. Bar volume is never read, so venue volume-definition differences cannot move any leg. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- The `1h` frame is a researcher choice on a timeframe-free source — no novel-interval confirmation burden attaches beyond the admitted `1h` sibling lane, but other frames would produce different event streams and are different, unpinned evaluations (see Execution assumptions).
- The displaced cloud is stale by construction (26 bars): in a vertical tape the passport is permissive to the point of vacuity, in a chop it binds hard — disclosed as the record's principal regime behaviour, not repaired.
- A position whose cross-down print never arrives is held to sample-end truncation (bounded by nothing but the data end); a winning leg keeps running with no profit-taking leg. This is the coded posture (zero risk legs), disclosed as the record's principal risk.
- Consecutive-edge whipsaw (cross-up, cross-down, cross-up across adjacent bars) exits and re-enters with no cooldown — disclosed as the principal friction.
- Vendored indicator internals (rolling-window seeding, NaN propagation, the facade-resolved ATR echo) live outside the pinned strategy file — pinned by call where called, never re-derived; exact reproduction inherits that seeding alongside the 80-bar floor.
- No trailing, no stop, no target, no time exit, no short leg — all explicitly absent, never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/judder659/Forven/blob/05f026afa719536351e77b7a38afadab6391e3d2/forven/strategies/builtin/ichimoku.py
- https://github.com/judder659/Forven
