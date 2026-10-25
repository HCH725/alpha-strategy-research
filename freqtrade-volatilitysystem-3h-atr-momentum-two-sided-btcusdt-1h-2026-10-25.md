---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade VolatilitySystem 3h-block absolute-momentum vs 2xATR14 level-state two-sided on BTCUSDT 1h bars
created: 2026-10-25
updated: 2026-10-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-02-06
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/futures/VolatilitySystem.py
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade VolatilitySystem 3h absolute-momentum level-state two-sided on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade user-strategy collection).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (repository HEAD verified via `git ls-remote` during this cycle; commit date 2026-09-08).
- Exact file path: `user_data/strategies/futures/VolatilitySystem.py`.
- GitHub blob SHA at the pinned commit: `15ce2473f3f60bd33c4a67b0b8b228e379850f19`, size 6432 bytes — byte-identical to the raw file fetched this cycle (157 lines, 6432 bytes, SHA-256 `10a32ea131fb8f4684741b48cd3eae70aa4d4990319b49a7acb7a2f9c7c8a672`).
- Staleness: the commits API shows exactly two commits ever touched this path; the last touch is `40e3a13e981058e586a0407b1fde6e7960a9551a` (2023-02-06, `Amend some additions from #288`) — the signal rule has not changed since 2023; record `source_as_of` is that last-touch date, never a fetch date.
- Class identity: `VolatilitySystem(IStrategy)`, `INTERFACE_VERSION = 3`, `timeframe = '1h'`, `can_short = True`. No `startup_candle_count`, no `informative_pairs`, no `protections`, no `trailing_*`, no `use_custom_stoploss` anywhere in the 157 lines — the absences below are coded absences, never researcher invention.
- The file's own words (quoted for gate evidence, never extended): docstring `Volatility System strategy.` plus `Based on https://www.tradingview.com/script/3hhs0XbR/` (file-level attribution only — the TradingView page itself was not opened and no TV fact is asserted); `Leverage is optional but the lower the better to limit liquidations` (prose caution, not an order leg). `resample_int = 60 * 3`; `resampled['atr'] = ta.ATR(resampled, timeperiod=14) * 2.0`; `resampled['close_change'] = resampled['close'].diff()`; `resampled['abs_close_change'] = resampled['close_change'].abs()`; `resampled_merge(dataframe, resampled, fill_na=True)`; entry `dataframe['close_change'] * 1 > dataframe['atr'].shift(1)` sets `enter_long`, mirrored `* -1` sets `enter_short` (the two commented-out `qtpylib.crossed_above` lines are dead comments — the live legs are sustained levels, disclosed); exits mirror entries (`enter_long == 1` sets `exit_short` and vice versa); `minimal_roi = {"0": 100}` (effectively disabled); `stoploss = -1` (disabled); `position_adjustment_enable = True` with `adjust_trade_position` (averaging machinery — fenced below); `custom_stake_amount` returns `proposed_stake / 2` (sizing hint — fenced below); `leverage()` returns `2.0` (magnitude hint — fenced below).
- Full-file token census (verified over the 157 lines this cycle): 1 `populate_indicators` / 1 `populate_entry_trend` (2 live `.loc` legs) / 1 `populate_exit_trend` (2 mirror `.loc` legs) / 0 `crossed_above` live (2, both inside `#` comments) / 1 `ta.ATR` / 0 `request.*` / 0 `security` / 0 `informative_pairs` / 0 `merge_informative_pair` / 0 `hyperopt` / 0 `IntParameter`/`DecimalParameter`/`CategoricalParameter` live (3 names appear only in the unused import line) / 0 `buy_params` / 0 `sell_params` / 0 `trailing` / 0 `protections` / 0 `CooldownPeriod` / 0 `funding` / 0 `mark_price` / 0 `order_types` / 0 `pyramid` / 0 `cooldown`. The only multi-bar constructs are the 3h resample, the block ATR/diff, and the one-bar `.shift(1)`.
- Resample mechanics corroborated against the called library (`technical/util.py`, read at floating master this cycle): `resample_to_interval(df, 180)` aggregates with `open:first / high:max / low:min / close:last / volume:sum` on `label="left"` minute bins with `.dropna()`; `resampled_merge` maps each resampled row to `date_merge = block_date + 180min - 60min` (the open time of the block's last 1h bar), left-merges, then forward-fills (`fill_na=True`). The derived arithmetic below freezes exactly this behavior in self-contained form, so the record never depends on a floating library pin.

Licence and rights: the repository is ISC-licensed open source; this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Freqtrade deployment. The source pins the `1h` frame, the `can_short` two-sided stance, the 3h-block ATR14x2.0 / block-close-diff construction, the sustained-level (non-edge) long/short legs, the opposite-leg exits, and the disabled ROI/stoploss/trailing posture — but ships no pair, no fill-timing flag, and no portable sizing. Researcher-declared adaptations are exactly five: (1) research market `BTCUSDT` Binance futures (the file names no pair); (2) completed-bar decisions with same-bar-close MARKET fills (the file returns per-candle flags with no fill-timing flag; derivation disclosed, never presented as the Freqtrade engine's own timing); (3) position averaging DISABLED — `adjust_trade_position` (up to 2 same-side entries) is fenced out and entries while positioned are hold-no-ops, so this record is single-unit where the source file can double (event-changing by construction, disclosed); (4) house sizing/capital/costs replacing `custom_stake_amount` (50% stake hint) and the `2.0` leverage hint (both disclosed-but-not-adopted; leverage magnitude moves no signal line); (5) an adopted 72-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 46th completed bar — see Required data — plus margin) and a gap fail-closed rule stricter than the source's partial-bin aggregation (disclosed). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-25): working-tree filename/content search for `VolatilitySystem`, `volatilitysystem`, `3hhs0XbR`, and `abs_close_change` returns zero strategy records citing this source file or this rule. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas, #350 ClucMay72018, #353 Heracles) trades a 3h-momentum-vs-ATR rule; the sole closed volatility PR (#291, Forven volatility-contraction) is a different source and mechanism. Closest pool records are different mechanism classes: `wilder-volatility-system-sic-stop-reverse` trades Welles Wilder's SAR-style SIC stop-and-reverse ladder (different construction, different legs); `bookstaber-atr-momentum-breakout-reversal` trades a daily ATR-channel breakout with reversal exits (different frame, edge-triggered breakout, no resampled momentum level); `dual-thrust-open-range-breakout` trades prior-day-range fractions (different basis, no ATR); the three `volatility-contraction-breakout` records trade contraction-then-expansion patterns (opposite trigger philosophy). Five-axis distinction: source identity differs (freqtrade-strategies immutable commit plus `futures/VolatilitySystem.py` path), mechanism differs (sustained absolute block-momentum level vs ATR, held true across bars, not an edge cross), signal construction differs (UTC-day-anchored 3h resample with date_merge+ffill merge and one-hour ATR shift), exits differ (exact opposite-level mirror, no stop/time leg), and horizon differs (`1h` source-native frame with 3h-derived features).

## Economic mechanism

### Source-reported

The file advances no economic thesis beyond its docstring title (`Volatility System strategy.`) and the leverage-caution prose. The coded bet is mechanical: a 3-hour block whose absolute close-to-close displacement exceeds twice its own 14-block average true range is treated as a directional impulse worth riding; the mirror condition ends it. No thesis, sample, or performance phrase of any kind ships anywhere in the 157 lines.

### Research interpretation

Impulse-persistence timer, two-sided, level-held, with symmetric reversal exits — the first 3h-resampled-momentum record in the pool. Unlike edge-cross systems that fire once per crossing, these legs stay true for every bar the impulse condition holds, so the state machine (not the edge) decides: the first level-true bar after flat enters, later level-true bars merely hold, and only the opposite level exits. Unlike pure breakout systems keyed to price extremes, the trigger is displacement-versus-volatility, so a slow grind that never stretches beyond 2xATR prints nothing while a single violent 3h block can flip the book. Note the pinned asymmetry, stated plainly: the entry threshold reads the CURRENT block's displacement against the PREVIOUS hourly bar's ATR reference (`.shift(1)`), so a displacement that decays mid-block still holds the level until the reference catches up or the mirror prints — chop that alternates sub-threshold blocks whipsaws nothing (flat stays flat), but chop that alternately exceeds in both directions flips the book with no cooldown and no stop. The bet is on 3h-impulse persistence at frozen `180min/14/2.0` geometry, not on any extreme, volume print, calendar effect, or second asset.

## Signal

Exact rule as pinned (any other resample width, ATR length, multiplier, shift, frame, fill, book, or risk posture is a different, unpinned rule). `HH/HL` below are trailing block extremes; all indices are completed-bar:

```text
Bin(k)      = 1h bars with UTC hour in {3k, 3k+1, 3k+2} (day-anchored: 00-02, 03-05, ..., 21-23)
BO(k)/BH(k)/BL(k)/BC(k) = first open / max high / min low / last close over Bin(k)
TR(k)       = BH(k)-BL(k) for k=0 else max(BH(k)-BL(k), |BH(k)-BC(k-1)|, |BL(k)-BC(k-1)|)
ATR(k)      = 2.0 * WilderRMA14(TR)(k)   // TA-Lib ATR(14) x2; first defined at k=14
CC(k)       = BC(k) - BC(k-1)            // NaN for k=0
REF(i)      = largest k with (start(k)+2h) <= date(i), NaN if none   // date_merge+ffill freeze
cc(i)       = CC(REF(i));  at(i) = ATR(REF(i));  atP(i) = ATR(REF(i-1))
enterL(i)   = cc(i) > atP(i);  enterS(i) = -cc(i) > atP(i)   // strict, sustained levels
exitL(i)    = enterS(i);       exitS(i)  = enterL(i)         // exact opposite-leg mirror
```

- Trade events: `enterL` on any bar whose referenced block displacement strictly exceeds the prior-bar ATR reference; `enterS` mirrored. Both legs are sustained levels (true on consecutive bars while the inequality holds), not one-shot edges — refires require nothing beyond continued truth, but the book admits only the first bar after flat (see state machine).
- Exact boundaries (pinned semantics): strict `>` on both legs exactly as coded — equality holds the prior state. NaN in either operand (warmup, leading ffill vacuum, gap suspension) forces both legs false. `abs_close_change` is a diagnostic echo read by zero order-gating line (fenced, never promoted).
- Mutual-exclusion proof (no tie-break pin required): `enterL` needs `cc > A`, `enterS` needs `-cc > A`, jointly implying `A < -|cc| <= 0`; ATR is non-negative by construction and NaN forces false — co-print is unsatisfiable on every bar, degenerate or otherwise. Empirically confirmed this cycle: the exact rule over a 300-bar synthetic tape (flat/sharp-up/flat/sharp-down/flat) prints 25 long-level bars (first idx 101) and 19 short-level bars (first idx 182) with zero co-print bars. The reviewer is never asked to invent an ordering.
- Direction: two-sided, `can_short = True` as coded. The short leg requires margin-short permission, realistic on the pinned perpetual venue (see Crypto portability).
- Exits and risk (explicit): the opposite level is the sole position-ending path (`minimal_roi {"0": 100}` and `stoploss -1` are coded disables; no trailing/protections/timeout ship anywhere). Stop loss, take profit, ROI ladder, trailing stop, and time limit are absent in source and recorded as explicitly disabled, never defaulted — adverse excursions have no guardrail besides the eventual mirror print (disclosed principal risk). No exit leg reads net profit, fees, or funding — costs change only the performance report, never whether an exit fires (disclosed).
- Position rule (predeclared researcher pin): single-unit (`0.001` BTC fixed quantity), at most one open position; a positioned book treats further same-side level-true bars as hold-no-ops — no pyramiding, no averaging (the file's `adjust_trade_position` second-entry path is fenced out by record rule, disclosed above); a flat book treats exit-leg bars as no-ops; opposite-level prints close to flat same-bar with re-entry from the next qualifying bar (no same-bar flip — researcher pin mirroring the admitted two-sided idiom, disclosed); re-entry re-arms on any later level-true bar (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `open/high/low/close` (block construction) with fixed non-positive references (block lags, one-hour `.shift(1)`, merge references to settled-or-forming blocks at or before the decision bar); the decision bar's own `volume` is never read (only `sum`med into an unread block field). No funding/OI/mark-price read, no second pair, no `request.*`/`security()`, no calendar/session call, no hyperopt parameter, no stop/limit order argument anywhere in the gating path. The forming block's inclusion of the decision bar's own OHLC is causal (inputs available at that bar's close) — no future bar is ever read.

## Required data

- Completed `1h` bars of BTCUSDT: `open/high/low/close` (block construction, decisions) — `volume` aggregated but unread by any gating line. No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1h` (source-native `timeframe = '1h'`); the 3h features are arithmetically derived from the same 1h stream (UTC-day-anchored bins, no second subscription — the same derivation idiom as the admitted R-Breaker record's daily levels from hourly bars).
- Warmup: TA-Lib ATR(14) carries a 14-period lookback (first defined at the 15th 3h block); its `date_merge` lands on the third 1h bar of that block (1h index 44, zero-based) and the one-hour `.shift(1)` needs one more bar — the structural minimum is the 46th completed `1h` bar. The adopted warmup is the first 72 completed `1h` bars flat by record rule (predeclared researcher choice — structural need plus 26 bars of margin, so seeding-convention detail cannot move the first admissible signal). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar.
- Gaps (fail-closed, stricter than the source's partial-bin aggregation, disclosed): a missing 1h timestamp, invalid OHLCV (`high >= max(open,close) > 0`, `low <= min(open,close)`, `low > 0`), or non-86400/3600-second spacing defect suspends signals until a fresh contiguous run of 72 valid completed bars rebuilds every referenced bin; no signal or synthetic fill during suspension. If already positioned, the book holds without inventing a protective liquidation; trading resumes only after the fresh run. No future bar repairs the gap.

## Execution assumptions — pinned Hummingbot compatibility

**Pinned benchmark:** package `20260920`, VERSION `dev-2.17.0`, immutable `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. This cycle independently re-verified the previously reviewed model capability it reuses (single completed-candle signal + same-row-close MARKET OrderExecutor + one netted POSITION_HOLD slot, both-side fees — the same primitive independently reviewed for the admitted 1h records); no per-candidate performance/parity proof is claimed here. A dedicated controller is **not yet implemented**; the claim is model expressibility using this inspected path, not that an executable recipe already exists.

- **Real data path:** Binance 1h klines expose the OHLCV columns the block fold consumes; a strategy-specific controller computes the frozen UTC-day-anchored 3h bins, Wilder ATR14x2.0, block diffs, and the date_merge+ffill references deterministically from that single stream. The input-validation/gap policy above runs on the original 1h timestamp series **before** any binning could hide a gap.
- **Controller/action path:** `BacktestingEngineBase.simulate_execution()` iterates rows and dispatches `CreateExecutorAction` to `simulate_executor`; `OrderExecutorConfig` supports the perpetual venue pair, BUY/SELL, fixed-quantity MARKET legs, and 2.0x-or-house leverage magnitudes as configuration (leverage magnitude moves no signal line). Sizing here is the record's single `0.001` BTC unit under the house capital framing — the file's 50%-stake hint and second-entry averaging are fenced out by record rule (disclosed derivative).
- **Fill semantics:** declared research close-fill convention on completed 1h bars (same-row close MARKET), with downstream timestamps normalized to the decision bar's close time — not a claim that a live order sent after seeing the close receives that price. No next-open/maker/intrabar capability is assumed.
- **State/accounting:** one netted POSITION_HOLD slot; immediate simulated fill-confirmed FLAT/LONG/SHORT state kept in controller memory; `Decimal` position/cash records. Exit-first same-bar resolution with next-bar re-entry is the record's explicit tiebreak (disclosed, never presented as the Freqtrade engine's own same-candle semantics).
- **Declared economics:** the file ships only disabled economics (`minimal_roi {"0": 100}`, `stoploss -1`, no fee/slippage/funding term — absences disclosed, never read as zero cost). Derived evaluation carries the full house cost load (fees plus historical funding; no hypothetical zero funding claimed) under the house overlay; the file's `2.0` leverage hint is disclosed-but-not-adopted. Simulator adds no spread/impact/slippage; zero *additional modeled* slippage is a stated limitation, not a market observation. Lot/tick rounding, exchange minimums, partial fills, actual spreads, latency, and liquidation mechanics remain unverified and are **not** represented as live-compatible.
- **Primitive boundary:** single-frame completed-bar level signal + same-row-close MARKET OrderExecutor + one netted futures slot is the previously independently reviewed model capability; the 3h fold is deterministic arithmetic over the same 1h array (no second feed, no shared capital, no cross-asset sync, no funding leg in the signal). Any later Qlib large-scale screening must reuse a verified representative execution primitive; no per-candidate performance/parity proof is claimed here.

## Evidence

### Source-reported

The file ships the full construction (3h resample width, TA-Lib ATR14x2.0, block-close diff, ffill merge, sustained-level long/short legs, exact opposite-leg exits, disabled ROI/stoploss, `can_short`, `1h` frame) and zero performance numbers: no return, no Sharpe, no win rate, no trade count, no backtest table or figure — this record claims no source-reported performance of any kind. The docstring's TradingView attribution (`3hhs0XbR`) is repeated as file prose only; no TV-page fact is asserted.

### Independently reproduced

**Not independently reproduced.** This cycle performed read-only primary-file inspection (pinned + floating bytes compared), library corroboration reads, and a stdlib-only reachability/specification check of the frozen derived rule (25 long-level / 19 short-level / 0 co-print bars over a 300-bar synthetic impulse tape; structural-minimum/warmup arithmetic confirmed) — not a Freqtrade run, Hummingbot backtest, Qlib parity run, profitability calculation, or live trade.

### Negative evidence

Pool-nearest records use different constructions: Wilder SIC (SAR ladder, not momentum-vs-ATR), Bookstaber (daily edge breakout), Dual-Thrust (prior-day-range fractions), volatility-contraction family (contraction-then-expansion, opposite philosophy), SuperTrend-flip open PR #63 (ATR-band state machine, no resampled momentum level). The shared words `volatility`, `ATR`, and `momentum` are vocabulary overlap only — none evaluates `|BC(k)-BC(k-1)| > 2*ATR14(k)` on UTC-day-anchored 3h blocks with date_merge+ffill references. The commented-out `crossed_above` lines were verified dead (inside `#` comments) so no edge-triggered twin of this rule exists in the file. The averaging path (`adjust_trade_position`, `position_adjustment_enable`, `custom_stake_amount`, `leverage()`) was read in full and fenced out of the record's event path with disclosure, never silently adopted or silently dropped.

## Falsification plan

Downstream only, if independently admitted and formally selected: freeze the above exact derivative and compare its level-held entries against an edge-triggered twin (enter only on the first level-true bar after a level-false bar — the commented-out `crossed_above` semantics), using the same fees, fill model, and contiguous IS/OOS periods. A separate model-consistent execution/parity capability check is needed if any **new** primitive is introduced. No experiment was run in this Scout cycle.

## Crypto portability

Pinned to BTCUSDT Binance futures `1h` (declared market choice; the file names no pair). The OHLC arithmetic ports across perpetual venues without structural change; the 24/7 market needs no session approximation beyond the UTC-day bin anchoring, which is fully specified above. Both sides are explicit coded legs (`can_short = True`), so a spot-only deployment expresses the long half only while every flip-to-short stays venue-gated (short permission unused, never silently converted) — a spot-only variant would be a different, unpinned claim. No funding-dependent leg, no stablecoin-specific assumption, no cross-venue state. Extension to other house-universe assets, other resample widths, or the file's averaging/sizing hints would each be a different, unpinned claim.

## Limitations

- Derived averaging removal: the file can hold two same-side entries via `adjust_trade_position`; this record holds one by rule. Event paths differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the file's averaged configuration.
- Derived fill timing and gap strictness: same-bar-close fills and fail-closed gaps are researcher pins; backtest economics differ from any live Freqtrade deployment by construction. Any live intrabar behavior is out of scope.
- Derived market pin: the file names no symbol — BTCUSDT is a researcher market choice for the house universe, never a source claim.
- No source cost declaration beyond disabled ROI/stoploss: no fee, slippage, or funding assumption ships anywhere usable — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Level-held exposure: while a level stays true the book holds through every bar with no profit-taking leg; alternating super-threshold chop flips the book with no cooldown. Adverse drift between mirror prints is held in full — the coded trade, disclosed, not smoothed.
- Seed bars: block ATR needs 15 settled 3h blocks and every trigger needs the one-hour ATR lookback; the first 72 `1h` bars are flat by record rule, so early-history signals never enter any evaluation.
- Library corroboration, not dependence: the `technical` resample/merge behavior was read at floating master to corroborate the frozen arithmetic; the record's math is self-contained and needs no library pin to evaluate.

## Implementation status

`not-implemented`: no dedicated Hummingbot controller or Qlib executable recipe was added. After independent admission, downstream selection may require a minimal strategy-specific implementation (3h fold + level state machine on the pinned path); this is not a second HB_READY admission gate.

## Adoption boundary

`research-only`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor must verify the exact PR head, all six gates and PASS-only main invariant before any merge. Scout does not approve, merge, trade, backtest or deploy.

## Related Wiki records

None asserted.
