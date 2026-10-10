---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Alligator displaced-SMMA stack long-flat on BTCUSDT 1d bars
created: 2026-10-11
updated: 2026-10-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-05-17
sources:
  - https://www.fmz.com/strategy/451731
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/Alligator-%E9%95%BF%E6%9C%9F%E8%B6%8B%E5%8A%BF%E8%B7%9F%E8%B8%AA%E4%BA%A4%E6%98%93%E7%AD%96%E7%95%A5-Alligator-Long-Term-Trend-Following-Trading-Strategy.md
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Alligator displaced-SMMA stack long-flat on BTCUSDT 1d bars

## Provenance

Primary source read end to end (canonical FMZ page fetched live in-browser plus its immutable public mirror file, both verified 2026-10-11):

- Canonical page: https://www.fmz.com/strategy/451731 (page title `Alligator Long-Term Trend Following Trading Strategy`, publisher account `ChaoZhang`, `Created: 2024-05-17 15:40:13` stamp on the page, `Hits: 1197`, `Copy: 10`). Fetched live over HTTPS during this cycle and read in full: prose states the full rule twice (strategy-principles section plus overview) — Jaw 13-period SMMA shifted 8 bars, Teeth 8-period SMMA shifted 5 bars, Lips 5-period SMMA shifted 3 bars; long when the mouth opens upward (Jaw bottom, Teeth middle, Lips top) with price above the Alligator; close the long when price breaks below the Jaw. The page-embedded `/*backtest*/` header reads `start: 2023-05-11 00:00:00`, `end: 2024-05-16 00:00:00`, `period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`. The risks section states verbatim that the strategy has no fixed risk management (`Lack of fixed risk management`). Full Pine below the preview is login-gated on the canonical page (`Login to view full source` wall renders in place of the remainder); the executable detail below comes from the immutable mirror, whose prose description is consistent with the page text (adopted as `source_as_of` 2024-05-17 from the page creation stamp, matching the mirror's `> Last Modified` 2024-05-17 15:40:13).
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit date 2025-04-30 11:10:28 +0800, subject `update`; repository head verified via the GitHub commits API — the same head pin as the merged Darvas, FRAMA, Fibonacci, BOP and sibling admissions), exact file path `Alligator-长期趋势跟踪交易策略-Alligator-Long-Term-Trend-Following-Trading-Strategy.md` (non-ASCII filename preserved verbatim; percent-encoded blob URL in Sources). File 11836 bytes, blob SHA `0285ec49cb9b05dbffa0dc9084865036c736e891` (verified against the GitHub contents API). The mirror prints `> Detail` = https://www.fmz.com/strategy/451731. The mirror's `[trans]` prose (13/8/5 SMMA with 8/5/3 shifts, mouth-open long, close-below-Jaw exit, no fixed risk management) matches the canonical page text quoted above.
- Full `//@version=5` block read in full (code lines from `/*backtest` through the final `barcolor(barcolor)` display line, strategy declaration `strategy(title="Alligator Long Term Trend Following Strategy [Skyrex.io]", shorttitle="Alligator Strategy [Skyrex.io]", overlay=true, format=format.inherit, pyramiding=1, calc_on_order_fills=false, calc_on_every_tick=true, default_qty_type=strategy.percent_of_equity, default_qty_value=100, initial_capital=10000, currency=currency.NONE, commission_type=strategy.commission.percent, commission_value=0.1, slippage=5)`). The executable order block is exactly two guarded calls: `if (longCondition)` → `strategy.entry(id="entry1", direction=strategy.long, ...)` and `if close < jaw` → `strategy.close(id="entry1", ...)`, where `longCondition = is_LowAboveAlligator(jaw, teeth, lips) and is_AlligatorHungry(jaw_o, teeth_o, lips_o)` with `jaw = smma(hl2, 13)[8]`, `teeth = smma(hl2, 8)[5]`, `lips = smma(hl2, 5)[3]` and undisplaced `jaw_o/teeth_o/lips_o = smma(hl2, 13/8/5)`. Everything after the order block is display-only (`barcolor` assignment and plot — feeding no order condition); the alert-message JSON strings inside the order calls carry bot-webhook fields only.
- Text census over the pinned code block: 1 `strategy.entry` (long-only market entry, no price argument) / 1 `strategy.close` (full close of entry ID `entry1`, no quantity qualifier) / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `time(` / 0 `volume` (the rule reads `high`/`low`/`close` only; `hl2` is `(high+low)/2`) / exactly 2 `input(` (bot `sourceUuid`/`secretToken` webhook strings — no numeric strategy input; all lengths and shifts are hard literals) / `process_orders_on_close` unset (Pine default: signals evaluate per completed bar, fills on the next bar) / `pyramiding` explicitly `1` (no same-direction adds). `commission_value=0.1` percent plus `slippage=5` ship in the declaration (recorded as the source cost stub — see Execution assumptions).
- No risk layer ships anywhere in the source: zero stop/target/trailing/time-exit order legs, and the prose admits no fixed risk management. The close-below-Jaw posture below is therefore the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention.
- Page/mirror performance language is absent entirely (no table, figure, or number) — this record claims no source-reported performance and no reproduced performance.

Licence and rights: the pinned code block carries `// This Pine Script™ code is subject to the terms of the Mozilla Public License 2.0` with `© Skyrex`. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly three: (1) market/frame pin `BTCUSDT 1d` — this one is near-lossless (the source executable `/*backtest*/` header already backtests `period: 1d` on `Futures_Binance BTC_USDT`; only the venue spelling and house-universe framing are normalized, disclosed here, never presented as a different claim); (2) same-bar-close fills (the source ships no execution-timing argument — Pine default fills evaluate per completed bar and fill on the next bar; no `process_orders_on_close` ships anywhere, quoted verbatim in census); (3) an adopted 25-bar warmup with pre-warmup bars flat by record rule (covers the 13-bar SMMA seed plus the 8-bar displacement plus the 5-bar mouth-gate reference with margin — see Required data) and house sizing/capital replacing the source economics stub (`strategy.percent_of_equity` 100% with `commission_value=0.1` percent and `slippage=5` — see Execution assumptions). The hl2-SMMA formulas, the `13/8/5` lengths, the `8/5/3` displacements, the whole-bar `low`-above-all-lines condition, the mouth-open inequality gate, the `entry1` order ID, the close-below-Jaw leg, the long-only direction handling, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-11): working-tree case-insensitive search for `alligator` returns zero hits anywhere — no admitted rule uses this source, author strategy, indicator, or mechanism. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closed research PRs contain no Alligator record. Closest pool records are different mechanism classes: `flying-dragon-offset-ma-band-trend` is an offset-MA band touch system (never triple Wilder-SMMA with whole-bar containment plus a mouth-open inequality gate); `gann-hilo-activator-state-flip-trend` is a HiLo-activator stop-flip system (never SMMA); moving-average-cross records (`ema-20-50-cross`, `golden-cross-sma-regime-gated`, `hull-ema-crossover`, `rsi-ma-crossover`, `dpo-ema-crossover`, `macd-signal-cross-reversal`) cross two averages of closes (never test whole-bar containment above three displaced hl2 SMMAs, never gate on a three-inequality mouth state, never exit on a close-below-displaced-Jaw leg). Five-axis distinction: mechanism differs (displaced-SMMA stack containment with mouth-state gate and Jaw-break exit, long-flat — versus average crosses, band touches, or stop flips), signal construction differs (no pool record computes Wilder SMMA on `hl2` with `13/8/5` lengths and `8/5/3` backward displacements), trigger differs (whole-bar `low`-above-all-lines plus mouth-open conjunction for entry; `close`-below-Jaw for exit), and source identity differs (fmzquant pin `7853bb2` port of ChaoZhang 451731, 2024-05-17).

## Economic mechanism

### Source-reported

Alligator-mouth trend capture (mirror Overview/Principles plus code, no performance section ships): three Wilder-smoothed averages of different speeds form the beast's Jaw (slow), Teeth (middle), and Lips (fast), each displaced forward so the plotted lines describe the trend's awning rather than its trailing edge. When the mouth opens upward — Lips on top, Teeth in the middle, Jaw at the bottom — and the entire bar floats above all three lines, the trend is confirmed hungry and the system goes long. It holds that single long until the bar's close falls back through the Jaw, which means the slow spine of the trend itself has been lost. There is deliberately no stop, no target, and no short side: the design bets that confirmed Alligator trends pay for the give-back between the Jaw break and any earlier top, and the prose admits fixed risk management is absent by design rather than by omission.

### Research interpretation

State-gated containment breakout, long-only with an explicit flat state. Unlike two-average cross systems that trade the moment one line passes another, this rule never trades a cross at all: entry demands a conjunction — the whole bar (via its `low`) must clear all three displaced lines AND the undisplaced mouth must currently read open (three strict inequalities). That conjunction is rarer and later than any single cross, which is the point: it waits for the stack to agree. Unlike always-in-market flip systems, the rule rests flat before the first conjunction and after every Jaw-break exit, and it never shorts — weak or inverted mouths only keep it flat. The price of the conjunction is late entry after the stack aligns and late exit at the Jaw (the slowest line): a trend that dies fast gives back most of the move before the close prints below the Jaw, and chop that repeatedly lifts the bar's low above the stack then drops the close under the Jaw prints full round trips at the worst prints of each swing. The bet is on displaced-stack persistence, not on any cross timing, band, volume print, or calendar effect.

## Signal

Exact rule as pinned (`13/8/5` lengths, `8/5/3` displacements, `hl2` source frozen — any other value is a different, unpinned rule):

- Declaration (derived): `strategy(title="Alligator Long Term Trend Following Strategy [Skyrex.io]", ..., pyramiding=1, ...)` semantics preserved with the derived `BTCUSDT 1d` market/frame pin and same-bar-close execution adopted (no such timing argument ships in the source) and house sizing replacing the source economics stub (see Execution assumptions). `calc_on_every_tick=true` ships in the source: on historical bars this still evaluates exactly once per completed bar (intrabar recalculation affects only realtime intrabar repainting of the current forming bar, never a closed bar's print); this record decides on completed bars only, predeclared.
- Smoothed lines (pinned): `smma(src, length)` is the Wilder recursion `smma := na(smma[1]) ? ta.sma(src, length) : (smma[1] * (length - 1) + src) / length` on `hl2 = (high + low) / 2`. Displaced trading lines `jaw = smma(hl2, 13)[8]`, `teeth = smma(hl2, 8)[5]`, `lips = smma(hl2, 5)[3]` — Pine `[N]` indexes N bars into history, so each displaced line at bar `t` is the SMMA value computed through bar `t-N`: strictly causal, no future reference (see Negative evidence). Undisplaced gate lines `jaw_o = smma(hl2, 13)`, `teeth_o = smma(hl2, 8)`, `lips_o = smma(hl2, 5)`.
- Entry long: `strategy.entry("entry1", strategy.long)` under `if (longCondition)` with `longCondition = low > jaw and low > teeth and low > lips and lips_o > jaw_o[5] and lips_o > teeth_o[2] and teeth_o > jaw_o[3]` — fires on any completed bar whose `low` strictly clears all three displaced lines while the mouth reads open, with same-bar-close execution under the derived declaration. `pyramiding=1` makes refires while already long no-ops (no adds).
- Exit: `strategy.close("entry1")` under `if close < jaw` — full close of the long on any completed bar closing strictly below the displaced Jaw, with same-bar-close execution under the derived declaration. No stop, no target, no trailing, no time exit — pinned as written, explicitly none, not invented.
- Direction: long-only with an explicit flat state (the sole entry leg passes `strategy.long`; no short leg exists anywhere — the `is_HighBelowAlligator` helper is defined but never called by any order line, quoted verbatim in census; the short side is therefore absent by code, disclosed, not enabled). Before the SMMA seed plus displacement history exists, `smma` evaluates `na` and every comparison is false by construction (no trade). On a spot venue the rule expresses unchanged (see Crypto portability).
- Display isolation: the `barcolor(...)` assignment and plot render only and cannot change any order; order logic reads exactly the two `if` lines. The `alert_message` JSON strings name bot-webhook fields and change no economics.

## Required data

- Completed `1d` bars of BTCUSDT: `high` (hl2 input, containment test), `low` (hl2 input, containment test), `close` (exit test). No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (derived pin following the source executable header's `period: 1d`; the script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction).
- Warmup: the SMMA seed needs 13 completed `1d` bars (`ta.sma` fallback on the first bar), the Jaw displacement reads 8 bars back, and the mouth gate reads `jaw_o[5]` — binding constraint is bar index ≥ 20 before every referenced value is non-`na`. The adopted warmup is the first 25 completed `1d` bars flat by record rule (predeclared researcher choice — covers seed, displacement, gate reference, and margin). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Each bar's OHLC enters the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (derived pin; the source executable header already backtests `Futures_Binance BTC_USDT` at `period: 1d` — venue transfer and symbol spelling are disclosed here, never presented as a different claim).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar fill (no execution-timing argument ships anywhere — quoted verbatim in census); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. Entry and exit legs are evaluated in source order (entry block before exit block): on a bar where both `longCondition` and `close < jaw` hold (possible — a bar can clear all three lines by its low yet close below the Jaw only if the Jaw sits above the bar's low but below... precisely: `low > jaw` and `close < jaw` cannot both hold since `close >= low`; entry-then-exit on the same bar is therefore impossible when flat, and when already long the entry leg is a pyramiding no-op while the exit leg closes — deterministic under either evaluation order, see Negative evidence).
- Sizing/capital/costs: the source economics stub is `strategy.percent_of_equity` 100% with `commission_type=strategy.commission.percent`, `commission_value=0.1`, `slippage=5` (quoted verbatim — no capital, funding, or margin assumption beyond that stub) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: `pyramiding=1` ships explicitly — at most one long unit under the fixed order ID `entry1`; entry refires while already long are no-ops by the pinned setting, the exit leg closes in full, an exit while flat is a no-op, and re-entry is allowed immediately on the next qualifying bar after any flat (no cooldown specified — explicitly none, not invented). Single engine position; no short side exists to conflict; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The mirror ships the full construction (Wilder `smma()` on `hl2`, `13/8/5` lengths, `8/5/3` backward displacements, `low`-above-all-lines plus three-inequality mouth gate under fixed ID `entry1`, close-below-Jaw full close, `pyramiding=1`, `commission_value=0.1` percent, `slippage=5`, display-only barcolor), the active `strategy(...)` declaration, the `Alligator Long Term Trend Following Strategy [Skyrex.io]` title, and the `/*backtest*/` header (2023-05-11→2024-05-16, `1d`, `Futures_Binance BTC_USDT`). It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=` — the sole position-closing path is the coded `strategy.close("entry1")` on `close < jaw`. The absence is coded (the order block ends with the close leg and only display code follows it in evaluation order) and admitted in prose (`Lack of fixed risk management`).
2. No future leakage in the displacements, stated plainly: `jaw = smma(hl2, 13)[8]` reads the SMMA value computed through 8 bars ago — at decision bar `t` every input (`hl2` through `t-8` for the Jaw, through `t-5`/`t-3` for Teeth/Lips, through `t-5`/`t-2`/`t-3` for the gate references) is a completed historical bar. The `8/5/3` forward-shift prose describes plot displacement; the code implements it as backward indexing, which is the causal direction. No `security()`, no `request.*`, no negative index, no `barstate.islast`-gated repainting path.
3. Same-bar entry/exit ordering fenced: when flat, `longCondition` requires `low > jaw` while the exit requires `close < jaw` — since `close >= low` on every bar, both cannot hold simultaneously, so no same-bar double-fill ordering exists. When already long, the entry leg is a `pyramiding=1` no-op and only the exit leg can act. Deterministic under either fill convention.
4. Short side provably absent: `is_HighBelowAlligator` is defined but zero order lines call it — the file's only `strategy.long` call is the entry and no `strategy.short` appears anywhere. The long-only posture is coded, not assumed.
5. Jaw-break lag, admitted plainly: the exit waits for the slowest displaced line, so a trend that reverses sharply gives back the distance from the top to the Jaw before the close prints below it — there is no stop, no time exit, and no opposite-signal exit (no short side exists). This is the coded posture, disclosed as the record's principal risk.
6. Chop sensitivity, admitted plainly: bars whose `low` flickers above and below the displaced stack print alternating entries and Jaw-break exits at the worst prints of each swing; the mouth gate filters but does not eliminate this. Disclosed, not filtered.
7. The `13/8/5` lengths, the `8/5/3` displacements, the `hl2` source, the strict whole-bar containment (via `low`, not `close`), the three-inequality mouth gate, the fixed `entry1` order ID, the long-only posture, the full close leg, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning any length or shift, converting containment into a cross, smoothing further, adding a stop/target/filter/cooldown, or enabling a short side would each be a different, unpinned rule — none is admitted here.
8. Derivation boundary fenced: the only non-source-native behaviors in this record are the `BTCUSDT 1d` market/frame pin, same-bar-close fills, the adopted 25-bar warmup with record-rule pre-warmup flat, and house sizing — all predeclared above; the SMMA formulas, lengths, displacements, containment condition, mouth gate, order ID, close leg, and risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, or timing of the source passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: hl2-Wilder-SMMA / `13/8/5` / `8/5/3` displacements / whole-bar containment plus mouth gate / close-below-Jaw exit / long-only / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Gate relevance: replacing the three-inequality mouth gate with entry on containment alone (`low` above all three displaced lines, same exit leg) must not improve net expectancy; fail ⇒ the mouth-state conjunction adds nothing over raw stack containment.
- F2 — Exit relevance: replacing the close-below-Jaw exit with a close below the faster Teeth line (same entry leg) must not improve net expectancy; fail ⇒ waiting for the slowest spine is dominated by exiting with the middle line.
- F3 — Displacement relevance: replacing the displaced lines (`[8]`/`[5]`/`[3]`) with undisplaced SMMAs (same lengths, same containment and gate roles) must not improve net expectancy; fail ⇒ the forward-displacement construction adds nothing over a plain SMMA stack.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (derived pin from an already-Binance-`1d`-backtested source). The high/low/close arithmetic ports across perpetual venues without structural change; the rule is long-only with no short leg, so a spot-only deployment expresses it unchanged. No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source fills next-bar on a `1d` Binance backtest with no timing argument; this record executes same-bar-close on `1d` BTCUSDT. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- Derived market spelling: the source header backtests `Futures_Binance BTC_USDT`; this record pins `BTCUSDT` under the house overlay. Venue-transfer differences are real — the adaptation is disclosed, and this record makes no claim about any other venue's performance.
- `calc_on_every_tick=true` ships in the source: on closed historical bars this changes nothing (one print per completed bar), but a live deployment recomputing intrabar could flash entry/exit states mid-bar that the closed-bar print later reverses. This record decides on completed bars only — the restriction is predeclared, and intrabar behavior is not claimed.
- No price stop, no time stop: adverse excursion after entry has no guardrail beyond the close-below-Jaw leg; a position whose close never prints below the Jaw is held indefinitely. This is the coded posture, disclosed as the record's principal risk.
- Chop sensitivity: containment flicker at the displaced stack prints full round trips in ranging markets, and Jaw-break exits structurally sell the give-back. The conjunction-plus-slow-exit construction is the coded design, disclosed, not smoothed.
- No full source cost declaration: beyond the `commission_value=0.1` percent stub and `slippage=5` the source ships no capital, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- FMZ canonical strategy page (ChaoZhang, 2024-05-17): https://www.fmz.com/strategy/451731
- Immutable mirror file at pinned commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (blob `0285ec49cb9b05dbffa0dc9084865036c736e891`, 11836 bytes): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/Alligator-%E9%95%BF%E6%9C%9F%E8%B6%8B%E5%8A%BF%E8%B7%9F%E8%B8%AA%E4%BA%A4%E6%98%93%E7%AD%96%E7%95%A5-Alligator-Long-Term-Trend-Following-Trading-Strategy.md
- Pine strategy semantics (order calls, default execution, history-referencing semantics): https://www.tradingview.com/pine-script-reference/v5/
