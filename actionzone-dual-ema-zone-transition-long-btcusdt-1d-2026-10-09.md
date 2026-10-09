---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: ActionZone dual-EMA zone-transition trend long on BTCUSDT 1d bars
created: 2026-10-09
updated: 2026-10-09
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-04-18
sources:
  - https://www.fmz.com/strategy/448778
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/MACD-Crossover-Strategy-MACD-%E4%BA%A4%E5%8F%89%E7%AD%96%E7%95%A5.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# ActionZone dual-EMA zone-transition trend long on BTCUSDT 1d bars

## Provenance

Primary source read end to end (immutable public mirror file plus its recorded FMZ canonical page, fetched 2026-10-09):

- Canonical page: https://www.fmz.com/strategy/448778 (page title `MACD Crossover Strategy | FMZ`, publisher account `ChaoZhang` with 2 page hits, `Created: 2024-04-18 17:56:23`, equal to the mirror `Last Modified`). Fetched over HTTPS during this cycle (767644 bytes): the page embeds the full `/*backtest ... */` header quoted below, the active `strategy('Advance EMA Crossover Strategy', overlay=true, precision=6)` declaration, and the complete order block (`1 strategy.entry` / `1 strategy.close` / `0 strategy.exit` / `0 strategy.order` in page state, counted verbatim). Word-boundary counts over the whole landing HTML: `Net Profit` 0, `Profit Factor` 0, `Sharpe` 0, `Max Drawdown` 0, `Win Rate` 0, `win rate` 0, `Annualized` 0 — the page ships no performance numbers of any kind (adopted as `source_as_of` 2024-04-18 from the page Created stamp, which equals the mirror `Last Modified`).
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit date 2025-04-30 11:10:28 +0800, subject `update`; verified repository head at research time via the GitHub commits API — the same head pin as the merged DPO-EMA, KST, Schaff, TRIX, SQZMOM-LB, Aroon, Qstick, AC and Elder-ray admissions), exact file path `MACD-Crossover-Strategy-MACD-交叉策略.md` (non-ASCII filename preserved verbatim; percent-encoded blob URL in Sources). File 8197 bytes, blob SHA `56fbff01e9ab578394d6d7f4a50eadea379428bf` (verified against the GitHub contents API at the pinned commit — size and SHA both match). The mirror prints `> Detail` = https://www.fmz.com/strategy/448778 and `> Last Modified` = 2024-04-18 17:56:23 (equal to the page Created stamp). The prose program description (both the Chinese original and the English `[trans]`) describes exactly the coded zone-transition rule (bull-zone/bear-zone definitions plus transition entries, quoted in Economic mechanism), so prose and code agree on the mechanism; the two residual prose/code gaps (prose says "sell", code closes flat; prose filename says MACD, code is a dual-EMA zone) are fenced in Limitations.
- Full `//@version=5` block read in full (code lines from `/*backtest` through the final `plotshape`, strategy declaration `strategy('Advance EMA Crossover Strategy', overlay=true, precision=6)` where `precision=6` is display-only). The page-embedded `/*backtest*/` header (`start: 2023-04-12 00:00:00`, `end: 2024-04-17 00:00:00`, `period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`) is byte-present on both the canonical page preview (2 hits each for `period: 1d`, `basePeriod`, `BTC_USDT`, `start: 2023`) and the mirror block — market (`BTC_USDT` Binance futures) and decision frame (`1d`) are therefore source-native, never researcher-chosen. `basePeriod: 1h` is the FMZ execution granularity, not a second decision frame: the script takes no timeframe input and makes no live multi-timeframe call (see census).
- Text census over the pinned code block: 1 `strategy.entry` (`strategy.entry("Buy", strategy.long)`) / 1 `strategy.close` (`strategy.close("Buy")`, no `when=`, unconditional on its bar) / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=`/`qty_percent` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `time(` / 0 `volume` / 0 `open`/`high`/`low`/`hl2` outside the inert source-price option list (the words `high|low|open|hl2|hlc3|hlcc4|ohlc4` occur only inside the `Source Data` input option menu; the pinned default is `close` and no order-gating line reads anything but the defaulted series). `pyramiding`, `process_orders_on_close`, `calc_on_every_tick`, `calc_on_order_fills`, `commission`, `initial_capital` and `default_qty_*` are unset throughout. The two `plotshape` calls and the `barcolor`/`plot` calls feed no order condition; order logic reads exactly the two zone-transition booleans.
- No risk layer ships anywhere in the source: zero stop/target/trailing/time-exit order legs, and the mirror's own optimization list names ATR stops and ADX filters only as future work (`策略优化方向`), confirming none ships. The bear-zone-transition close posture below is therefore the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention.
- Page/mirror performance language is absent entirely (no table, figure, or number; the prose adjectives carry no quantity) — this record claims no source-reported performance and no reproduced performance.
- Filename-versus-code note, pinned without repair: the mirror filename and FMZ page title say MACD, but the executed block contains no MACD line, no signal line, no histogram — it is a dual-EMA (12/26) zone system in the CDC ActionZone family (`FastMA = ta.ema(xPrice, 12)`, `SlowMA = ta.ema(xPrice, 26)`). This record pins the computation, never the label; anyone searching the pool for a MACD record will not find one here (see dedup).

Licence and rights: the canonical page is a public FMZ strategy publication by ChaoZhang. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly three: (1) same-bar-close fills (the source fills next-bar-open — no `process_orders_on_close` ships anywhere, quoted verbatim in census); (2) an adopted 100-bar warmup with pre-warmup bars flat by record rule (earliest evaluable transition is the 2nd completed bar — see Required data); (3) house sizing/capital replacing the language-default sizing (no `default_qty_*` ships anywhere — see Execution assumptions). Market (BTCUSDT Binance futures), decision frame (`1d`), pinned input defaults (`close` / 12 / 26 / smoothing 1), zone definitions, transition triggers, order IDs, direction handling, the unconditional close leg, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-09): working-tree case-insensitive searches for `actionzone`, `action-zone`, `action zone`, `bullzone`, `bearzone`, `448778`, and `advance ema` return zero strategy records using this source, author strategy, or mechanism. Same-publisher ChaoZhang records exist (DPO-EMA FMZ 474030, KST FMZ 436493, Schaff FMZ 365905, TRIX FMZ 428683, Aroon FMZ 438795, Qstick FMZ 439854, AC FMZ 435716, Elder-ray FMZ 432762, MACD-file ActionZone FMZ 448778 is this record) but carry different canonical identities, different indicator families, and different order sets. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #58 (ML/reconstruction batch — file list verified, no zone-transition record), and #63 (SuperTrend ATR-flip trend long) — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `ema-20-50-cross-btcusdt-1h` (Forven S01508) fires a plain always-live fast-over-slow EMA inequality on every bar with same-bar-close execution declared in-source; `ema-cloud-7-20-trend-btcusdt-1d` holds level conditions live on every bar (`close > fastEMA and fastEMA > slowEMA` re-tested each bar, two-sided with a close-vs-fast exit leg); `golden-cross-sma-regime-gated-long-btcusdt-1h` is a regime-gated SMA cross; `rsi-ma-crossover-reversal-btcusdt-1d` crosses an oscillator against its own average; `alma-cross-volume-gate-btcusdt-1d` crosses two ALMAs under a volume gate. Five-axis distinction: mechanism differs (edge-triggered zone *transitions* — an order fires only on the single bar where the zone boolean flips, never on persistence — versus level rules re-tested every bar), signal construction differs (triple conjunction `FastMA > SlowMA AND xPrice > FastMA` evaluated as a transition event, with the price-above-fast leg able to delay entry bars after the average cross), exits differ (bear-zone-transition unconditional `strategy.close("Buy")` flat leg with an explicit gray-zone hold state where neither zone holds and the position is kept, versus close-vs-fast or opposite-cross exits), source identity differs (FMZ 448778 Apr-2024 CDC-ActionZone-family dual-EMA versus Forven Pine v6, TV cloud authors, or FMZ 380250 ALMA), and direction handling differs (pure long-only with an explicit flat state versus the two-sided cloud record).

## Economic mechanism

### Source-reported

Dual-EMA zone trend capture (mirror `策略原理`, corroborated line-for-line by the code): the fast EMA12 rides above the slow EMA26 with the smoothed price above the fast leg only when buying pressure dominates at both the ordering scale and the level scale; the first bar of that joint state is the long entry. The mirror state-transition clause (`当从空头区域转换为多头区域时买入,当从多头区域转换为空头区域时卖出`) is the coded `BullZone and not BullZone[1]` / `BearZone and not BearZone[1]` pair. The prose "sell" is the exit-flat marker (see Limitations): the code never opens a short.

### Research interpretation

Edge-triggered zone system with an explicit flat state and an explicit gray hold state, long-only. Unlike always-live level holders (the 7/20 cloud record) that re-test their inequalities every bar, this system fires at most one entry per zone visit: a 20-bar BullZone persistence produces exactly one entry on its first bar, and bars 2–20 are no-ops by code (`not BullZone[1]` fails). Unlike plain average crosses (20/50, golden-cross records) that enter the moment the averages flip, the price-above-fast conjunction can delay entry past the average cross — fast crossing above slow while price still sits below fast is not an entry; the entry waits for the joint state. Unlike always-in-market holders that must be long or short after warmup, this system rests flat whenever the last transition was a bear-zone close, and holds through gray bars (fast above slow but price below fast, or any other neither-zone print) without exiting. The bet is on joint ordering-plus-level persistence at the ~2–4-week scale (12/26 daily EMAs), not on any oscillator level, volatility band, or calendar effect.

## Signal

Exact rule as pinned (input defaults pinned — every value below is the code `defval`, corroborated by the mirror Strategy Arguments table except the noted smoothing-table quirk):

- Declaration (derived): `strategy('Advance EMA Crossover Strategy', overlay=true, precision=6)` with same-bar-close execution adopted for the derived record (no such argument ships in the source) and house sizing replacing the unset language-default sizing (see Execution assumptions). `calc_on_every_tick` and `calc_on_order_fills` are unset (both default false: exactly one evaluation per completed bar). No commission, margin, or capital assumption ships anywhere — pinned as absent, with house costs applying to the derived evaluation (see Execution assumptions). `precision=6` is chart display only and feeds no order.
- Inputs (pinned defaults): `xsrc = close` (Source Data option menu lists `close|high|low|open|hl2|hlc3|hlcc4|ohlc4` but the code `defval=close` governs; order logic at defaults reads `close` only); `xprd1 = 12` (Fast EMA period); `xprd2 = 26` (Slow EMA period); `xsmooth = 1` (Smoothing period — the mirror Arguments table renders this row as `true`, an FMZ extraction quirk; the code `input(title='Smoothing period (1 = no smoothing)', defval=1)` governs, so `xPrice = ta.ema(close, 1)` equals `close`). Display toggles (`fillSW`/`fastSW`/`slowSW`/`plotSigsw`, all default true) feed only `barcolor`/`plot`/`plotshape` and no order. Changing any pinned default would be a different, unpinned rule.
- Smoothing (pinned): `xPrice = ta.ema(xsrc, 1)` = `close` at pinned defaults (no-op smoothing, no variant choice left open).
- Averages (pinned): `FastMA = ta.ema(xPrice, 12)`; `SlowMA = ta.ema(xPrice, 26)`.
- Zones (pinned): `BullZone = FastMA > SlowMA and xPrice > FastMA`; `BearZone = FastMA < SlowMA and xPrice < FastMA`. Strict inequalities: exact equality on either leg satisfies neither zone — the tie case holds prior state by code, never fires.
- Entry long: `if (BullZone and not BullZone[1]) strategy.entry("Buy", strategy.long)` — fires only on the single transition bar into the joint bull state, with same-bar-close execution under the derived declaration.
- Exit: `if (BearZone and not BearZone[1]) strategy.close("Buy")` — unconditional close of the long on the single transition bar into the joint bear state (no `when=`, no quantity qualifier: the whole position), with same-bar-close execution under the derived declaration. No stop, no target, no trailing, no time exit — pinned as written, explicitly none, not invented.
- Gray state (pinned): bars satisfying neither zone (e.g. `FastMA > SlowMA` but `xPrice < FastMA`) fire no leg — an open long is held, flat stays flat. The hold-through-gray is coded behavior (both `if` conditions false), not a gap.
- Direction: long-only with an explicit flat state. The bear-zone leg never opens a short; on a spot venue the rule expresses unchanged (see Crypto portability).
- Display isolation: `barcolor`, the two average `plot`s, and the two `plotshape` signal markers render only; the toggle inputs feeding them cannot change any order.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only at pinned defaults (smoothed series, both averages, both zone conjunctions, both transition pairs). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line. The source-price option menu is pinned to its `close` default (see Signal).
- Single decision timeframe `1d` (source-native per the page-embedded `period: 1d` header; `basePeriod: 1h` is the FMZ execution granularity, not a signal input). The script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction.
- Warmup: `ta.ema` seeds from the first bar, so the zone booleans are first evaluable on the 2nd completed `1d` bar (the `[1]` transition lag is the only structural lag); the 12/26 averages need tens of bars to settle statistically. The adopted warmup is the first 100 completed `1d` bars flat by record rule (predeclared researcher choice). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (source-native per the header's `Futures_Binance BTC_USDT`; venue transfer from `BTC_USDT` to `BTCUSDT` spot-symbol spelling is naming only, never presented as a market change).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar-open (no execution-timing argument ships anywhere — quoted verbatim in Provenance); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill. With no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. The two transition booleans are mutually exclusive every bar past warmup (a zone cannot transition into bull and bear on the same bar — `BullZone` and `BearZone` are disjoint by construction since they require opposite strict orderings), so no ordering resolution is required.
- Sizing/capital/costs: no `default_qty_*`, commission, or margin assumption ships anywhere (quoted verbatim in census) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) replace the unset language defaults here, never presented as source-native behavior.
- Concurrency: no `pyramiding` ships anywhere, pinning the language default of no same-direction adds — at most one long unit under the fixed order ID `Buy`; persistence bars inside a BullZone are no-ops by the transition guard, the bear-zone close exits in full, and re-entry is allowed immediately on the next bull transition after any flat (no cooldown specified — explicitly none, not invented). Single engine position; no short side exists to conflict; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The mirror ships the full construction (EMA12/EMA26 pair, no-op smoothing at default 1, triple-conjunction zone definitions, strict transition pair, fixed `Buy` order ID, unconditional close leg), the active `strategy(...)` declaration, the `Advance EMA Crossover Strategy` title, and the page-embedded 1d/1h April-2023→April-2024 backtest header. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=`/`qty_percent` — the sole position-closing path is the coded bear-zone-transition `strategy.close("Buy")` leg. The absence is coded (the order block ends with the close leg and no order call follows), and the mirror's optimization prose proposes ATR stops and ADX filters as future work, corroborating that none ships — fenced in Limitations for the reviewer rather than upgraded into a source claim.
2. Entry and exit legs are mutually exclusive on every bar past warmup by zone disjointness (`BullZone` requires `FastMA > SlowMA and xPrice > FastMA`; `BearZone` requires the strict opposite on both legs), so no single bar can satisfy both transition guards even though they sit in separate `if` statements.
3. Exit-leg conditionality, admitted plainly: a long opened on a bull transition exits only on the next bear transition. A market that keeps the joint bull state (or drifts into gray and stays there) never exits until a full bear transition prints — there is no time-stop to cut a stale trend, and oscillation that repeatedly prints fresh bull transitions after each bear close can whipsaw the system in and out of flat with consecutive small losses. This is the coded trade, disclosed, not a tunable parameter here.
4. Long-only flat stretches earn nothing: while the last transition was a bear close the system holds no position by code, not by choice of venue — disabling nothing, since no short leg exists to disable.
5. Boundary ties hold, never fire: exact equality on any zone leg satisfies neither zone (strict inequalities), and a re-print of an already-held zone satisfies neither transition guard (`not BullZone[1]` / `not BearZone[1]` fail); warmup bars are flat by record rule.
6. The `close` source default, EMA12/EMA26 lengths, no-op smoothing, strict-conjunction zones, transition guards, fixed order ID, long-only posture, unconditional close leg, gray hold, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning a length, adding a stop/target/filter/cooldown, switching source series, dropping the price-above-fast conjunction into a plain average cross, enabling a short side, or relabeling the system MACD would each be a different, unpinned rule — none is admitted here.
7. Derivation boundary fenced: the only non-source-native behaviors in this record are same-bar-close fills, the adopted 100-bar warmup with record-rule pre-warmup flat, and house sizing — all predeclared above; market, timeframe, every default, zone, transition, close leg, gray hold, and risk posture are source-verbatim. This record is therefore never evidence that the original next-bar-open 1d/1h source itself passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `close` source / EMA12 / EMA26 / no-op smoothing / strict zone conjunctions / transition guards / unconditional bear-transition close / long-only / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Price-gate relevance: replacing the joint bull zone with the plain average cross (`FastMA` crossed above `SlowMA`, same lengths, no price leg) must not improve net expectancy; fail ⇒ the price-above-fast conjunction adds nothing over a plain dual-EMA cross.
- F2 — Transition relevance: replacing the edge-triggered entry with the always-live level rule (long whenever `BullZone` holds, flat otherwise) must not improve net expectancy; fail ⇒ the transition guard adds nothing over holding the level.
- F3 — Exit relevance: removing the bear-transition close leg (holding the long through bear transitions — buy-and-hold from the first bull transition, since no opposite signal exists) must not improve net expectancy; fail ⇒ the explicit flat state is dominated by simply staying positioned.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (source-native venue family). The close-only arithmetic ports across perpetual venues without structural change; the rule is long-only with no short leg, so a spot-only deployment expresses it unchanged. No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read, so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source fills next-bar-open on a 1d-decision/1h-base Binance-futures backtest; this record executes same-bar-close on `1d` BTCUSDT. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- Prose-versus-code gaps (pinned to code): the prose and arrows advertise a "sell" signal, but the coded leg is `strategy.close("Buy")` — exit-flat, never a short. The filename and page title say MACD, but the code ships no MACD construction of any kind. The record pins the computation; anyone citing the label or the prose verb alone would describe a different rule.
- Smoothing-table quirk (pinned to code): the mirror Arguments table renders the smoothing row as `true`; the code `input(title='Smoothing period (1 = no smoothing)', defval=1)` governs, so smoothing is a no-op at pinned defaults. If the table rendering is ever read as a boolean flag, that reading is rejected here in favor of the code default.
- No price stop and no time stop: adverse excursion after entry has no guardrail beyond the bear-zone close, which may arrive late (and gray stretches delay it further); oscillation around the zone boundary can compound consecutive whipsaw losses. This is the coded posture, disclosed as the record's principal risk.
- No source cost declaration: no commission, fee, slippage, or funding assumption ships anywhere in the source — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- FMZ canonical strategy page (ChaoZhang, Created 2024-04-18): https://www.fmz.com/strategy/448778
- Immutable mirror file at pinned commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (blob `56fbff01e9ab578394d6d7f4a50eadea379428bf`, 8197 bytes): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/MACD-Crossover-Strategy-MACD-%E4%BA%A4%E5%8F%89%E7%AD%96%E7%95%A5.md
- Pine strategy semantics (order calls, default execution, built-in averages): https://www.tradingview.com/pine-script-reference/v5/
