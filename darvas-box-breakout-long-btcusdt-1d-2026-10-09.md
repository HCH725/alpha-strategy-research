---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Darvas Box breakout long with box-bottom exit on BTCUSDT 1d bars
created: 2026-10-09
updated: 2026-10-09
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-07-29
sources:
  - https://www.fmz.com/strategy/458041
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/Darvas-Box-Breakout-and-Risk-Management-Strategy-Darvas-%E7%9B%92%E5%AD%90%E7%AA%81%E7%A0%B4%E4%B8%8E%E9%A3%8E%E9%99%A9%E7%AE%A1%E7%90%86%E7%AD%96%E7%95%A5.md
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Darvas Box breakout long with box-bottom exit on BTCUSDT 1d bars

## Provenance

Primary source read end to end (immutable public mirror file plus its recorded FMZ canonical page, fetched 2026-10-09):

- Canonical page: https://www.fmz.com/strategy/458041 (page title `Darvas Box Breakout and Risk Management Strategy | FMZ`, publisher account `ChaoZhang` with 2 page hits, `Created: 2024-07-29 14:22:29`, equal to the mirror `Last Modified`). Fetched over HTTPS during this cycle (749874 bytes): the page embeds the full `/*backtest ... */` header quoted below, the active `strategy("Darvas Box Strategy", overlay=true, ...)` declaration, and the complete order block (`1 strategy.entry` / `1 strategy.close` / `0 strategy.exit` / `0 strategy.order` in the code state; page-wide word-boundary counts read `strategy.entry` 4 / `strategy.close` 4 because the block is embedded twice — preview plus page state — with zero `strategy.exit` / `strategy.order` anywhere). Word-boundary counts over the whole landing HTML: `Net Profit` 0, `Profit Factor` 0, `Sharpe` 0, `Max Drawdown` 0, `Win Rate` 0, `Annualized` 0 — the page ships no performance numbers of any kind (adopted as `source_as_of` 2024-07-29 from the page Created stamp, which equals the mirror `Last Modified`).
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit date 2025-04-30 11:10:28 +0800, subject `update`; verified repository head at research time via the GitHub commits API — the same head pin as the merged Double-Seven, DPO-EMA, KST, Schaff, TRIX, SQZMOM-LB, Aroon, Qstick, AC, Elder-ray and ActionZone admissions), exact file path `Darvas-Box-Breakout-and-Risk-Management-Strategy-Darvas-盒子突破与风险管理策略.md` (non-ASCII filename preserved verbatim; percent-encoded blob URL in Sources). File 15480 bytes, blob SHA `97380215b7d41532858c63c07d26f7fcd179551f` (verified against the GitHub contents API at the pinned commit — size and SHA both match; content bytes re-downloaded at the pin are byte-identical, sha256 `03fcd4aca60ddd498e52e6e4f8940327b03c73689bb338717572ca7a3c1ea1c5`). The mirror prints `> Detail` = https://www.fmz.com/strategy/458041 and `> Last Modified` = 2024-07-29 14:22:29 (equal to the page Created stamp). The prose program description agrees with the coded rule on box construction and box-edge entry/exit (quoted in Economic mechanism); prose-only extras (moving-average/MACD/RSI confirmation, percent stop, risk-reward ratio) are NOT coded anywhere and are fenced in Negative evidence, never admitted.
- Full `//@version=5` block read in full (code lines from `/*backtest` through the final `plotshape`, strategy declaration `strategy("Darvas Box Strategy", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=100)`). The page-embedded `/*backtest*/` header (`start: 2023-07-23 00:00:00`, `end: 2024-07-28 00:00:00`, `period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`) is byte-present on both the canonical page preview (2 hits each for `period: 1d`, `basePeriod`, `BTC_USDT`) and the mirror block — market (`BTC_USDT` Binance futures) and decision frame (`1d`, 1h execution granularity) are therefore source-native, never researcher-chosen. With market entry and full-close legs only (no stop/limit/intrabar legs anywhere), the 1h base granularity is immaterial to fills (24 native 1h bars per 1d bar on a 24/7 venue); this record keeps the source-native 1d/1h frame with no frame derivation.
- Text census over the pinned code block: 1 `strategy.entry` (`strategy.entry("Buy", strategy.long)`, inside `if (Buy)`, no `when=`, no price argument — market entry) / 1 `strategy.close` (`strategy.close("Buy")`, inside `if (Sell)`, no `when=`, no quantity qualifier — unconditional full close) / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=`/`qty` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `time(` / 0 `volume` / 0 `open` (the rule reads `high`/`low`/`close` only) / exactly 1 `input.*` (`boxp = input.int(defval=5, title="Length", minval=1, maxval=500)` — the sole parameter, pinned at its default 5). `pyramiding`, `process_orders_on_close`, `calc_on_every_tick`, `initial_capital`, `commission_*` and `slippage` are unset throughout (Pine language defaults apply — quoted verbatim in census). The 2 `plot` calls (box rails), 2 `plotshape` calls and 2 `alertcondition` calls feed no order condition; order logic reads exactly the two signal booleans.
- No risk layer ships anywhere in the source: zero stop/target/trailing/time-exit order legs. The prose section names percentage stops and risk-reward ratios only as uncoded description (no such call exists) — the box-bottom close posture below is therefore the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention.
- Page/mirror performance language is absent entirely (no table, figure, or number; the prose adjectives carry no quantity) — this record claims no source-reported performance and no reproduced performance.

Licence and rights: the canonical page is a public FMZ strategy publication by ChaoZhang; the pinned code block carries no licence header of its own (the FMZ page is the publication vehicle). This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly three: (1) same-bar-close fills (the source fills next-bar-open — no `process_orders_on_close` ships anywhere, quoted verbatim in census); (2) an adopted 30-bar warmup with pre-warmup bars flat by record rule plus the structural na-guard (no box yet ⇒ no trade — see Required data); (3) house sizing/capital replacing the source 100%-equity sizing (`default_qty_type=strategy.percent_of_equity, default_qty_value=100` ships verbatim — see Execution assumptions). Market (BTCUSDT Binance futures), decision frame (`1d`, 1h base), the pinned `boxp=5` literal, box-formation arithmetic, entry/exit triggers, order IDs, direction handling, the unconditional close leg, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-09): working-tree case-insensitive searches for `darvas`, `458041`, `TopBox`, and `BottomBox` return zero admitted rules using this source, author strategy, or mechanism — the only `box` hits anywhere are the English words "out of the box" / "black-box" inside `p-signal-erf-dead-band-reversal-btcusdt-1h-2026-10-05.md`, `drm-dynamic-rsi-momentum-btcusdt-1d-2026-10-06.md` and `rsi-ma-crossover-reversal-btcusdt-1d-2026-10-07.md` (unrelated prose, never a box-breakout rule). Same-publisher ChaoZhang records exist (Double-Seven FMZ 473246, DPO-EMA FMZ 474030, KST FMZ 436493, Schaff FMZ 365905, TRIX FMZ 428683, Aroon FMZ 438795, Qstick FMZ 439854, AC FMZ 435716, Elder-ray FMZ 432762, Low-High FMZ 432972, ActionZone FMZ 448778) but carry different canonical identities, different indicator families, and different order sets. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long — single file verified), #49 (Gaussian channel StochRSI-gated breakout long — single file verified), #58 (ML/reconstruction batch — file list verified, no box-breakout record), and #63 (SuperTrend ATR-flip trend long — single file verified) — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `donchian-20-10-breakout-btcusdt-1h` trades a raw 20-bar highest-high breakout with a 10-bar low exit (no consolidation-formation state); `low-high-dip-tp-long-btcusdt-1d` buys a recovery cross back *over* the prior 20-bar low under an EMA200 gate with a fixed 8% take-profit (mean-reversion dip, never a box); `pivot-point-breakout-kaufman-btcusdt-1d` trades Kaufman-efficiency pivot levels (a different level construction with no box state). Five-axis distinction: mechanism differs (box-consolidation formation requires a new-high event confirmed `boxp-2` bars later with falling short-window highs, then trades the frozen box rails — never a rolling extreme), signal construction differs (`ta.valuewhen`/`ta.barssince` state rails with `crossover`/`crossunder` on `close` vs rolling `highest`/`lowest` or pivot formulas), exit differs (opposite box rail, no fixed target), direction posture differs (long-only with structural flat before the first box), warmup differs (formation-gated plus 30-bar record rule).

## Economic mechanism

### Source-reported

Darvas-box consolidation breakout (mirror `策略原理`, corroborated line-for-line by the code): sideways consolidation prints a box — the top rail freezes the new-high print, the bottom rail freezes the box-period low; a close pushing up through the top rail buys the emergent uptrend, and the first close breaking down through the bottom rail ends the trade. The design bets that genuine breakouts out of multi-day consolidation resolve upward before the box bottom gives the signal back.

### Research interpretation

Formation-gated breakout with an explicit flat state, long-only. Unlike raw-extreme systems (Donchian) that buy every new N-bar high, this system buys only highs that survive a consolidation filter: the high must stand unexceeded for `boxp-2` bars while the short-window highs decay (`k3 < k2`), freezing a horizontal top rail — a strictly rarer, more selective entry at the cost of later fills and missed V-shaped recoveries that never consolidate. Unlike dip-recovery systems (Low-High record) that buy weakness, this system buys confirmed strength above a frozen rail. Unlike always-in-market holders, the system rests flat before the first box ever forms and after every box-bottom exit, and it never shorts: breakdowns while flat are no-ops. The bet is on continuation *out of* short-horizon consolidation (~5 daily bars) rather than on any oscillator level, volatility band, or calendar effect.

## Signal

Exact rule as pinned (`boxp=5` frozen — the sole input at its default; any other value is a different, unpinned rule):

- Declaration (derived): `strategy("Darvas Box Strategy", overlay=true)` with same-bar-close execution adopted for the derived record (no such argument ships in the source) and house sizing replacing the source 100%-equity sizing (see Execution assumptions). `calc_on_every_tick` is unset (defaults false: exactly one evaluation per completed bar). No commission, margin, or capital assumption ships anywhere — pinned as absent, with house costs applying to the derived evaluation (see Execution assumptions).
- Box arithmetic (pinned, `boxp=5`): `LL = ta.lowest(low, 5)`; `k1 = ta.highest(high, 5)`; `k2 = ta.highest(high, 4)`; `k3 = ta.highest(high, 3)`; `NH = ta.valuewhen(high > k1[1], high, 0)` (most recent new 5-bar high); `box1 = k3 < k2` (short-window highs decaying); box-formation bar = `ta.barssince(high > k1[1]) == 3 and box1`; `TopBox = ta.valuewhen(<formation>, NH, 0)`; `BottomBox = ta.valuewhen(<formation>, LL, 0)` — both rails hold their last frozen values (step functions) until the next formation bar re-freezes them.
- Entry long: `if (Buy) strategy.entry("Buy", strategy.long)` with `Buy = ta.crossover(close, TopBox)` — fires on the single bar where the close crosses strictly up through the frozen top rail, with same-bar-close execution under the derived declaration.
- Exit: `if (Sell) strategy.close("Buy")` with `Sell = ta.crossunder(close, BottomBox)` — unconditional full close of the long on any bar whose close crosses strictly down through the frozen bottom rail (no `when=`, no quantity qualifier), with same-bar-close execution under the derived declaration. No stop, no target, no trailing, no time exit — pinned as written, explicitly none, not invented.
- Direction: long-only with an explicit flat state. No short leg exists anywhere; before the first box forms both rails are `na` so both signals are `na` (no trade by construction). On a spot venue the rule expresses unchanged (see Crypto portability).
- Display isolation: the 2 `plot` calls (box rails), 2 `plotshape` calls and 2 `alertcondition` calls render/announce only and cannot change any order.

## Required data

- Completed `1d` bars of BTCUSDT: `high` (box windows, new-high detection, `NH`), `low` (box-period low rail), `close` ( rail crosses, both triggers). No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (source-native per the page-embedded `period: 1d` header; `basePeriod: 1h` equals native 1h execution granularity — 24 1h bars per 1d bar on a 24/7 venue — and with market-entry/full-close legs only, no intrabar path exists for the base to affect). The script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction.
- Warmup: the indicator windows need 5 completed `1d` bars; box formation needs one new-high event plus 3 confirming bars on top. The adopted warmup is the first 30 completed `1d` bars flat by record rule (predeclared researcher choice — covers 6× the 5-bar window plus several formation cycles), reinforced by the structural na-guard (rails are `na` until the first formation bar, and `crossover`/`crossunder` against `na` never fires). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (source-native per the header's `Futures_Binance BTC_USDT`; venue transfer from `BTC_USDT` to `BTCUSDT` spot-symbol spelling is naming only, never presented as a market change).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar-open (no execution-timing argument ships anywhere — quoted verbatim in census); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. Entry and exit legs are evaluated as separate `if` statements in source order (entry first, then exit): on the rare bar where a box update makes both conditions true at once (see Negative evidence), the derived execution fills the entry at the close and closes it at the same close, ending flat; no ordering resolution beyond source order is required.
- Sizing/capital/costs: the source ships `default_qty_type=strategy.percent_of_equity, default_qty_value=100` (100% equity per entry, quoted verbatim) with no commission, fee, slippage, or margin assumption anywhere — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) replace the source sizing here, never presented as source-native behavior.
- Concurrency: no `pyramiding` ships anywhere, pinning the language default of no same-direction adds — at most one long unit under the fixed order ID `Buy`; entry refires while already long are no-ops by the language default, the box-bottom close exits in full, an exit while flat is a no-op, and re-entry is allowed immediately on the next box-top cross after any flat (no cooldown specified — explicitly none, not invented). Single engine position; no short side exists to conflict; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The mirror ships the full construction (5-bar low/high windows, new-high detection, decaying-highs formation filter, frozen `TopBox`/`BottomBox` rails, `crossover` entry, `crossunder` exit, fixed `Buy` order ID), the active `strategy(...)` declaration, the `Darvas Box Strategy` title, and the page-embedded 1d/1h July-2023→July-2024 backtest header. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`qty` — the sole position-closing path is the coded box-bottom `strategy.close("Buy")` leg. The absence is coded (the order block ends with the close leg and only display calls follow).
2. Prose-only claims fenced out: the mirror prose additionally names moving-average/MACD/RSI confirmation, percentage stops, and risk-reward ratios — none of these words appears in any order-gating line (census: no `sma`/`ema`/`macd`/`rsi`/`stop=`/`limit=` in code). This record follows the code only; the prose extras are never admitted as rules.
3. The entry buys confirmed strength above a frozen rail, never weakness: a V-shaped recovery that never prints a qualifying consolidation box is missed by code, not by venue choice — disclosed, not repaired.
4. Exit-leg conditionality, admitted plainly: a long opened on a box-top cross exits only on the next box-bottom crossunder. A market that grinds sideways between the rails, or that tops without ever crossing under the frozen bottom rail, never exits until the rail breaks — there is no stop, no time-stop, and no opposite-signal exit beyond the bottom rail (a fresh box-top cross while long only refires a no-op entry). This is the coded trade, disclosed, not a tunable parameter here.
5. Degenerate dual-leg bars via box updates: because both rails re-freeze on formation bars, a bar that simultaneously prints a new frozen box *inside* the prior close (old close inside the old box, new close inside the new narrower box with `close > TopBox` and `close < BottomBox` while `close[1]` satisfies both priors) can satisfy `Buy` and `Sell` together; source order (entry block before exit block) fills the long at the close and closes it at the same close, ending flat with two fills and no overnight exposure. This is the coded ordering, disclosed as the record's principal microstructure edge case.
6. The `boxp=5` literal, the 5/4/3-bar window set, the `boxp-2` confirmation count, the decaying-highs filter, the frozen-rail semantics, the strict cross (not touch) triggers, the fixed order ID, the long-only posture, the unconditional close leg, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning the length, converting the cross into a touch, adding a stop/target/filter/cooldown, enabling a short side, or exiting on a fresh top-rail touch would each be a different, unpinned rule — none is admitted here. (`boxp` values 1–2 would additionally pass non-positive lengths to `ta.highest`; the UI `minval=1` bound does not make them reviewed — the reviewed version freezes `boxp=5`.)
7. Derivation boundary fenced: the only non-source-native behaviors in this record are same-bar-close fills, the adopted 30-bar warmup with record-rule pre-warmup flat, and house sizing — all predeclared above; market, timeframe, every literal, the box arithmetic, both triggers, the close leg, and the risk posture are source-verbatim. This record is therefore never evidence that the original next-bar-open 1d/1h source itself passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `boxp=5` / formation filter / frozen rails / cross-up entry / cross-down exit / long-only / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Formation-filter relevance: replacing the formation-gated rails with raw rolling extremes (buy `crossover(close, highest(high,5)[1])`, exit `crossunder(close, lowest(low,5)[1])`) must not improve net expectancy; fail ⇒ the Darvas consolidation filter adds nothing over the naked Donchian-style extreme.
- F2 — Entry relevance: replacing the box-top cross entry with the always-live box-state hold (long whenever the last rail signal was a top cross, flat otherwise — i.e. the rule without the cross timing) must not improve net expectancy; fail ⇒ the cross timing adds nothing over holding the box state.
- F3 — Exit relevance: removing the box-bottom close leg (holding the long through bottom-rail breaks — buy-and-hold from the first qualifying breakout, since no opposite signal exists) must not improve net expectancy; fail ⇒ the explicit box exit is dominated by simply staying positioned.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (source-native venue family). The high/low/close arithmetic ports across perpetual venues without structural change; the rule is long-only with no short leg, so a spot-only deployment expresses it unchanged. No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source fills next-bar-open on a 1d-decision/1h-base Binance-futures backtest; this record executes same-bar-close on `1d` BTCUSDT. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- No price stop, no time stop: adverse excursion after entry has no guardrail beyond the frozen bottom rail, which ratchets only on new formation bars and may sit far below the entry in a tall box; a close that never crosses under the rail is held indefinitely. This is the coded posture, disclosed as the record's principal risk.
- No source cost declaration: no commission, fee, slippage, or funding assumption ships anywhere in the source — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Formation lag at trend turns: a fresh trend leg must first print a new high, wait `boxp-2` bars, and satisfy the decaying-highs filter before any rail exists to trade — early-trend moves are missed by code while late boxes can trigger just before exhaustion. The lag is the coded filter, disclosed, not smoothed.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- FMZ canonical strategy page (ChaoZhang, Created 2024-07-29): https://www.fmz.com/strategy/458041
- Immutable mirror file at pinned commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (blob `97380215b7d41532858c63c07d26f7fcd179551f`, 15480 bytes): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/Darvas-Box-Breakout-and-Risk-Management-Strategy-Darvas-%E7%9B%92%E5%AD%90%E7%AA%81%E7%A0%B4%E4%B8%8E%E9%A3%8E%E9%99%A9%E7%AE%A1%E7%90%86%E7%AD%96%E7%95%A5.md
- Pine strategy semantics (order calls, default execution, built-in averages): https://www.tradingview.com/pine-script-reference/v5/
