---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: IBS internal-bar-strength mean-reversion short system on ETHUSDT 1h bars
created: 2026-10-06
updated: 2026-10-06
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-02-20
sources:
  - https://www.fmz.com/strategy/482784
  - https://www.tradingview.com/pine-script-reference/v6/#fun_strategy
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The FMZ page prose states entries fire only 'within the specified trading window' and that the system is 'specifically designed for daily timeframe trading in stocks and ETF markets', but the pinned Pine block contains 0 `hour(`, 0 `time(`, 0 `timestamp(`, 0 `input.time` and 0 `input.session` calls, and the FMZ backtest header pins `period: 1h` / `basePeriod: 1h` on `ETH_USDT` (2024-06-01 to 2025-02-18). Code plus executable header govern: there is no time gate and the pinned evaluation frame is 1h crypto, not daily stocks. The prose is recorded as contradicted, not repaired."
  - "The page prose presents the time-window restriction as one of three entry conditions, yet no such input or clock read exists anywhere in the 30-line executable block. A chart user cannot enable what the code does not declare, so the record pins 'no time gate' as source semantics and F2 forces any replay to confirm entries fire on every qualifying bar regardless of wall-clock time."
---

# IBS internal-bar-strength mean-reversion short system on ETHUSDT 1h bars

## Provenance

Primary source read end to end (FMZ public strategy page artifact, via the pinned local mirror of that page):

- FMZ strategy page: https://www.fmz.com/strategy/482784 (`High-Position-Internal-Bar-Strength-Based-Mean-Reversion-Short-Strategy`), author `ianzeng123`, last modified `2025-02-20 15:00:16`.
- Executable artifact inside the page: a 30-line `//© Botnet101` MPL-2.0 `//@version=6` Pine block with one live `strategy()` declaration, two `input.float` threshold declarations, one IBS assignment, two boolean condition assignments, two `if` order blocks, and three display-only `plot` calls.
- FMZ backtest header printed verbatim in the artifact: `start: 2024-06-01 00:00:00`, `end: 2025-02-18 08:00:00`, `period: 1h`, `basePeriod: 1h`, `exchanges: [{"eid":"Binance","currency":"ETH_USDT"}]`. This header is the source's own executable scope (not a signal rule) and is the sole source of the pinned `1h` decision timeframe; downstream must declare its own evaluation window rather than silently re-tuning it.
- Mirror bytes pinned 2026-10-06: file 8102 bytes, SHA-256 `f6e2402f38c7aec0019af08acec9bcbc22b288c2c3d881419f864fde9993be8d`. The mirror is the FMZ page scrape (`fmz-strat` corpus); no second immutable host (GitHub blob) exists for this strategy, so provenance is the FMZ stable URL plus these bytes — traceable and public, but without commit-SHA immutability, which is stated rather than hidden.

Pre-write dedup (2026-10-06): word-boundary search of the working tree for `internal bar strength`, `internalBarStrength`, `IBS`, and `482784` returned 0 matches in any strategy record; `gh pr list --state open` shows only #36 (`reconstruction/legacy-family-quantaalpha`, a non-Scout QuantaAlpha family record — different source, different mechanism); the closed research PRs (#6 WaveTrend, #10 golden/dead cross, #17 MACD histogram, #20 Ichimoku-RSI, plus merged #5 Gann, #7 P-Signal, #9 VIDYA, #12 Bookstaber, #21 Kaufman pivot, #22 EHMA, #23 DMI, #25 Ichimoku-ADX, #28 DRM, #29 Monday-drift, #31 Donchian, #32 Flying-Dragon, #34 EMA-cross, #35 Stochastic-OTT) contain no IBS, no short-only mean-reversion, and no `close>high[1]`-confirmed oscillator-fade rule. Five-axis distinction: mechanism differs (single-bar close-position fade — short the bar that closes in the top decile of its own range after taking out the prior high, cover when a close lands in the bottom three deciles — versus dual-OTT trails, ATR breakouts, Hull bands, DMI crosses, erf dead-bands, Donchian channels, calendar holds, or oscillator crosses), signal construction differs (raw `(close-low)/(high-low)` ratio with no smoothing, no moving average of any kind, zero `ta.*` calls), horizon is `1h` on ETH (no other record runs ETH; the 1h records on `main` are BTCUSDT EMA-cross, Donchian, P-Signal and VIDYA, all different mechanisms), source identity differs (FMZ 482784 versus all prior FMZ IDs, TV scripts and Forven pines), and direction handling is short-only with no direction input versus two-sided or long-only records.

## Economic mechanism

### Source-reported

- Premise, as printed: when IBS `(Close-Low)/(High-Low)` reads at or above 0.9 the close sits near the bar's high (overbought); when it reads at or below 0.3 the close sits near the bar's low (oversold). Fading the overbought print captures the pullback after exhaustion.
- Entry confirmation, as printed: the fade is taken only when the close also exceeds the previous bar's high (`close>high[1]`), framed as breakout confirmation that the exhaustion bar is genuinely extended.
- Risk stance, as printed: the source admits there is no stop-loss mechanism and that trend regimes can produce continuous losses — the edge claimed is purely the statistical tendency of an extreme single-bar close position to revert, not any risk-managed structure.

### Research interpretation

- Falsifiable mechanism hypothesis: on 1-hour crypto bars, a close printed in the top decile of its own range immediately after violating the prior bar's high marks a locally overextended tape (late buyers lifting into resistance); the subsequent few bars carry a statistically negative drift as that inventory is absorbed. The exit at IBS 0.3 or below is the symmetric capitulation print where the fade has played out. The bet is single-bar positional exhaustion, not multi-bar trend or volatility-regime persistence.
- The `close>high[1]` leg matters: without it the rule would short every high-close bar including quiet grinds; with it the rule selects only bars that demonstrably pushed into new one-bar-high territory before fading the close. Both legs are independently falsifiable (F1 splits entry legs; F2 checks boundary behavior).

## Signal

Exact executable semantics, read from the pinned block (nothing inferred, nothing added):

- Indicator variant: Internal Bar Strength, `internalBarStrength = (close - low) / (high - low)`. No smoothing, no lookback beyond the current bar, no `ta.*` function anywhere in the file (0 occurrences), no Heikin-Ashi, no volume, no external feed.
- Source prices: `close`, `low`, `high` of the decision bar plus `high[1]` (previous completed bar's high). All causal; no negative shift, no future reference.
- Thresholds: `upperThresholdInput = input.float(defval=0.9, maxval=1)`, `lowerThresholdInput = input.float(defval=0.3, minval=0)`. Pinned evaluation uses defaults 0.9 / 0.3; the inputs are user-tunable on a chart, but the record pins the defaults and any retune is a different rule.
- Entry: `shortCondition = internalBarStrength >= upperThresholdInput and close>high[1]` → `if shortCondition` then `strategy.entry('short', strategy.short)`. Plain `>=` / `>` comparisons — no `crossover`/`crossunder`/`ta.cross` anywhere (0 occurrences), so the #6 tie-semantics precedent does not apply; a bar exactly at IBS 0.9 with close exactly above the prior high is a deterministic entry.
- Exit: `exitCondition = internalBarStrength <= lowerThresholdInput` → `if exitCondition` then `strategy.close_all()`. Full flatten, both directions (only a short can exist). The two conditions are mutually exclusive on one bar (IBS cannot be simultaneously ≥0.9 and ≤0.3), so the code order (entry block before exit block) never double-fires; evaluation order is documented as immaterial.
- Direction: short-only, explicitly. The title is `[SHORT ONLY]`, the only order-creating call is `strategy.entry('short', strategy.short)`, and no direction/mode/long-short input exists. Long is disabled by construction (DMI-record pattern: one-sided at pinned code with no direction input).
- Risk semantics: no stop loss, no take profit, no trailing stop, no time exit — 0 `strategy.exit`, 0 `strategy.stop`, 0 `strategy.order`, 0 `limit`/`stop` order arguments. Recorded as explicitly absent per the source's own risk admission, never as silent defaults.
- Zero-range bar: if `high == low` (flat 1h bar), the IBS division is `0/0`, i.e. `na` under documented Pine division semantics; `na` never satisfies an `if` gate, so both blocks skip and the rule holds (no entry, no exit). Deterministic hold-on-na; F2 forces the replay to demonstrate it rather than raising or inventing a fill.
- Warmup: exactly 2 bars (`high[1]` is the deepest reference; IBS itself needs only the current bar). No seeding recursion exists anywhere (no `ta.rma`/`ta.ema` family, no self-referenced series), so no Bookstaber-style seed-convergence question arises.

## Required data

- 1h bars of one pair: `open/high/low/close` (signal reads `close`, `low`, `high`, `high[1]`; `open` and `volume` are never read). `time` is never read — no date gate exists in code.
- No funding, OI, mark/index price, liquidation feed, trade/aggressor feed, L2/order book, on-chain, options/Greeks, sentiment/news, macro, or cross-venue state is referenced or required.
- Instrument: `ETHUSDT` on a margined venue (the rule shorts, so spot-cash cannot run it — naked shorting is out of scope, P-Signal/Bookstaber pattern). Research market is explicitly labeled house choice: `ETHUSDT` 1h perpetual under the standard downstream overlay. Source ran Binance spot `ETH_USDT` 1h; the spot→perpetual basis on the same coin's 1h OHLC is recorded as `data gap`, immaterial to the OHLCV-only signal definition (formulas, thresholds and comparisons are identical on either feed) exactly as the merged P-Signal and Bookstaber records treat their residual contract-identity gaps — never as source semantics, and pinned before any execution work.
- Single pair, single instrument, no basket, no ranking, no cross-sectional step, no shared portfolio state.

## Execution assumptions

- Timing: `process_orders_on_close=true` is code-declared in the live `strategy()` declaration → completed-bar decision with same-bar-close fills. No `calc_on_every_tick=true` (unset → language default false), no intrabar logic, no next-bar-open semantics. Compatible with the pinned Hummingbot completed-bar/same-close convention; never approximated.
- Declaration, code-read verbatim: `strategy('[SHORT ONLY] Internal Bar Strength (IBS) Mean Reversion Strategy', overlay=false, default_qty_value=100, default_qty_type=strategy.percent_of_equity, margin_long=5, margin_short=5, process_orders_on_close=true, precision=4)`.
- Maximum same-side concurrency: 1. `pyramiding` is not written, so the value comes from the language default: the v6 reference (`#fun_strategy`, via its mirrored text) states "The maximum number of entries allowed in the same direction. If the value is 0, only one entry order in the same direction can be opened, and additional entry orders are rejected … The default is 0", converging with both official v5 statements quoted in the merged Bookstaber record. Recorded as source-declared-by-language-default with that convergence stated; F3 forces the executing engine to confirm "one open same-side entry, no adds".
- Re-entry/cooldown: no cooldown is declared (0 occurrences of any delay/counter input) → explicitly none. After `close_all()` flattens, the next bar's qualifying print re-enters; while a short is open, repeated same-side signals are rejected by the pyramiding default, not accumulated. No `position_size`/`opentrades`/`position_avg_price` read exists, so no position-aware state conditions any signal.
- Sizing: code declares 100 percent-of-equity compounding (`default_qty_value=100`, `default_qty_type=strategy.percent_of_equity`). Replaced downstream by the explicit house overlay (6% + 6% + 6%, isolated) — event-neutral here because exits always flatten the whole position and same-side adds are rejected, so notional never changes signal, timing, direction, or exits. Never presented as source-native.
- `margin_long=5` / `margin_short=5` are code-declared (5% margin requirement); downstream leverage (3×/5× isolated) is the house overlay. Liquidation mechanics are not part of the signal; a liquidation-only-after-extreme-drawdown divergence is recorded as `data gap` (tradeability, not signal), Bookstaber pattern.
- Commission, slippage, `initial_capital`, `currency`, `calc_on_*` flags, `close_entries_rule`, `max_bars_back`, `backtest_fill_limits_assumption`, `use_bar_magnifier` are unset in code → Pine v6 language defaults, each confirmed end to end by F3 rather than asserted here. `overlay=false` and the three `plot` calls are display-only.
- Costs: the source declares no fee/funding model (event-neutral omission — neither enters any rule). Downstream applies pinned Binance non-VIP USDⓈ-M fees plus realized funding as pure accounting; funding accrues only while short and changes no event. F4 checks cost-dependence.

## Evidence

### Source-reported

- No traceable numeric performance is cited: the page shows two backtest-chart images with no readable table, figure, or section numbers recoverable from the artifact, so no ROI/Sharpe/win-rate/trade-count from the source is reproduced here. Anything beyond "the page displays backtest chart images over 2024-06-01→2025-02-18 on ETH 1h" would be invention.
- Source-admitted negative facts (kept as boundary, not signal): no stop-loss; continuous-loss risk in strong trends; single-indicator false signals; no volume/volatility filter.

### Independently reproduced

- Not independently reproduced.

### Negative evidence

- Mean-reversion fades are regime-fragile by the source's own admission (trend persistence inverts the edge). F1/F5 are designed to surface exactly this: absence of entries, or exits that never trigger, on ETH 1h history fails the record back to research-only.

## Falsification plan

- **F1 — Signal presence and leg split.** Threshold (research-defined): at least 30 short entries and at least 10 IBS-0.3 exits on `1h` ETHUSDT perpetual bars from 2022-01-01, with each entry leg (`IBS>=0.9` alone, `close>high[1]` alone, conjunction) contributing at least 5 entries. Fail ⇒ the rule never trades this instrument/timeframe (or one leg is dead code in practice); record stays research-only.
- **F2 — Boundary and contradiction audit.** Threshold: replay must demonstrate (a) a bar with IBS exactly 0.9 and `close>high[1]` enters, (b) a zero-range bar (`high==low`) holds with no order and no error, (c) entries fire on qualifying bars regardless of wall-clock hour/session (prose time-window disproven in code), and (d) no long order exists on any bar. Fail on any deviation ⇒ pin the discrepancy in writing, research-only, no adoption.
- **F3 — Engine-default audit gate.** Threshold (research-defined): the executing engine must confirm end to end — fill at the decision bar's close, once-per-bar evaluation, one open same-side entry with further same-side entries rejected while short, full flatten on the IBS-0.3 print, immediate re-entry eligibility the next bar, and every unset declaration reading its Pine v6 language default. Fail if any recorded value differs ⇒ pin the discrepancy, research-only.
- **F4 — Cost ladder.** Threshold (research-defined): apply 0 / 1 / 2 / 5 / 10 bps per side plus a funding-accrual leg for the short side; fail if net annualized return turns non-positive at 2 bps per side or net Sharpe falls to 0 or below at 5 bps per side ⇒ the edge is cost-dependent, research-only, never proposed for adoption.
- **F5 — Cross-instrument generalization.** Threshold (research-defined): run the identical frozen rule on BTCUSDT perpetual 1h and on one further major perpetual chosen before inspection; fail if 0 of 2 produce positive net return after costs at 2 bps per side ⇒ single-asset overfit diagnosis.

## Crypto portability

- Native crypto rule in its own backtest (Binance ETH 1h, 24/7 tape) — no equity-session adjustment needed; the contradicted "daily stocks" prose is explicitly not followed.
- 1h ETH bars are continuous (no close auction, no overnight gap concept); the `close>high[1]` confirmation reads naturally on a 24/7 series. Prior-bar-high violation frequency differs by venue/contract feed (spot vs perpetual basis), which is why the spot→perpetual basis is a declared `data gap` rather than a silent substitution.
- Short-only requires a margined venue; under the house USDT-M perpetual overlay this is native. Any spot-only downstream must state a long-only restriction as its own overlay choice, never as source semantics — and with no long leg defined, such a restriction would leave no strategy at all.

## Limitations

1. Single-indicator fade with no trend filter and no stop-loss (source-admitted); trend regimes are the known killer.
2. Spot-vs-perpetual 1h feed basis on ETH (`data gap`, immaterial to the rule definition, must be pinned before execution).
3. No immutable commit-SHA provenance (FMZ page + mirror bytes only); if the author edits the page, this record's bytes no longer match live — re-verify before any downstream use.
4. Unrealistic 100%-equity compounding in code is replaced by the house overlay; any consumer replaying raw code defaults instead of the overlay misstates notional.
5. `precision=4`, `overlay=false`, plots: display-only, no event effect.
6. F-gates above are research tests, never substitutes for the (complete) source rules.

## Implementation status

- Not implemented. No Hummingbot/Qlib/n8n/Paper/Testnet/Live work has been performed or is authorized by this record.

## Adoption boundary

- Research-only. Not approved for Paper, Testnet, Mainnet, or live trading. Only a `PASS` downstream selection plus satisfied F-gates may advance this toward screening, and satisfying F-gates is screening evidence, not trading approval.

## Related Wiki records

- None (no Wiki write was performed for this record).

## Sources

- https://www.fmz.com/strategy/482784 — primary source (code, header, prose, images all read from this page's artifact).
- https://www.tradingview.com/pine-script-reference/v6/#fun_strategy — Pine v6 `strategy()` declaration reference (pyramiding default and order-function semantics).
- https://www.tradingview.com/pine-script-docs/concepts/strategies/ — strategy calculation/execution concepts (completed-bar evaluation, `process_orders_on_close`).
