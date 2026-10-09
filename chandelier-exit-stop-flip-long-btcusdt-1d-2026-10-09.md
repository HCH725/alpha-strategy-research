---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Chandelier Exit dual-stop state-flip long on BTCUSDT 1d bars
created: 2026-10-09
updated: 2026-10-09
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-01-05
sources:
  - https://www.fmz.com/strategy/437792
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E5%90%8A%E7%81%AF%E5%87%BA%E5%9C%BA%E7%AD%96%E7%95%A5Chandelier-Exit-Strategy.md
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Chandelier Exit dual-stop state-flip long on BTCUSDT 1d bars

## Provenance

Primary source read end to end (immutable public mirror file plus its recorded FMZ canonical page, fetched 2026-10-09):

- Canonical page: https://www.fmz.com/strategy/437792 (page title `Chandelier Exit Strategy | FMZ`, publisher account `ChaoZhang`, `Created: 2024-01-05 15:57:51`). Page prose states the full construction in words: 22-day ATR times a coefficient (default 3) sets long/short stop lines from highest high / lowest low; long entry triggers when price breaks above the previous long stop; exit closes the long when price falls below the short stop; long-only (`It only performs buy operations`). The page's own Risk Analysis admits `No stop loss in place after buying` and `No profit taking mechanism` — the no-stop/no-target posture is source-declared, not inferred. No return, Sharpe, win-rate, profit-factor, drawdown, or trade-count number ships anywhere in the fetched prose (adopted as `source_as_of` 2024-01-05 from the mirror `Last Modified` stamp, which matches the page Created date).
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (verified repository head at research time via `git ls-remote` — the same head pin as the merged MACD, Darvas, Double-Seven, DPO-EMA, KST, Schaff, TRIX, SQZMOM-LB, Aroon, Qstick, AC, Elder-ray and ActionZone admissions), exact file path `吊灯出场策略Chandelier-Exit-Strategy.md` (non-ASCII filename preserved verbatim; percent-encoded blob URL in Sources). File 7876 bytes, blob SHA `43879c254b088fcd4ba9906ea9df9989e4366816` (verified against the GitHub contents API at the pinned commit — size and SHA both match; content bytes re-downloaded at the pin are byte-identical, sha256 `73a8f546e6c771a5ea643fbaf368cfa94753b1d55d5c34570f9b27f2a8b7e893`). The mirror prints `> Detail` = https://www.fmz.com/strategy/437792 and `> Last Modified` = 2024-01-05 15:57:51. The mirror's `[trans]` prose is the canonical page text verbatim, so there is no prose/code divergence to fence — prose and code agree on 22 / 3.0 / long-only / reversal exit.
- Text census over the pinned Pine v5 block: `//@version=5` plus `strategy("Chandelier Exit Strategy", overlay=true)` (no `pyramiding`, no `process_orders_on_close`, no `calc_on_every_tick`, no capital/commission/slippage argument — Pine language defaults apply throughout) / exactly 5 `input.*` (`length` 22, `mult` 3.0 float, `showLabels` true, `useClose` true, `highlightState` true — all pinned at defaults; any other value is a different, unpinned rule) / 1 `strategy.entry` (`strategy.entry("Buy", strategy.long, qty = initial_capital / close)` with `initial_capital = 25`, inside `if buySignal`) / 1 `strategy.close` (`strategy.close("Buy")`, inside `if sellSignal`) / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `time(` / 0 `volume` / 0 `open`. Order-gating lines read `close` only; `high`/`low` enter solely inside `ta.atr(length)` true-range arithmetic (unavoidable and pinned — the ATR needs the range). The embedded `/*backtest*/` header reads `start: 2023-12-28 00:00:00`, `end: 2024-01-04 00:00:00`, `period: 10m`, `basePeriod: 1m`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]` — one 8-day 10m sample window, kept as provenance only; this record claims no source-reported performance and no reproduced performance.
- Display isolation: `showLabels` gates `plotshape` Buy/Sell text labels only; `highlightState` feeds no order line; all `plot`/`plotshape`/`alertcondition` calls render or notify only and cannot change any order.

Licence and rights: the canonical page is a public FMZ strategy publication by ChaoZhang; the pinned code block carries no licence header of its own (the FMZ page is the publication vehicle). This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly five: (1) decision-frame port from the header's `10m` to `1d` (the 22-bar / 3.0 bar-count literals are kept verbatim — only the bar meaning changes); (2) same-bar-close fills (the source fills next-bar-open — no execution-timing argument ships anywhere); (3) an adopted 50-bar warmup with pre-warmup bars flat by record rule (covers the 22-bar extremum plus Wilder-ATR seeding margin — see Required data); (4) house sizing/capital/costs replacing the source's fixed `$25`-notional sizing (`qty = 25 / close`, no commission/fee/slippage/margin assumption ships anywhere — see Execution assumptions); (5) venue naming carried as `BTCUSDT` Binance perpetual (the header venue is already `Futures_Binance BTC_USDT` — same venue class, frame change only, never presented as source-native). Stop arithmetic, ratchet logic, state-machine priority, both flip triggers, order IDs, long-only posture, and the no-stop/no-target risk stance are source-native and unmodified.

Pre-write dedup (2026-10-09): working-tree case-insensitive searches for `437792`, `Chandelier`, and `吊灯` return zero admitted rules using this source, author publication, or mechanism — the sole `chandelier` hit anywhere is an incidental kill-note inside `donchian-20-10-breakout-btcusdt-1h-2026-10-06.md` recording that a v4 TV-mirror Chandelier file from a different mirror source was killed pre-write in a prior cycle (never merged, never an open PR; different canonical identity and different program semantics from this v5 FMZ-437792 record). Same-publisher ChaoZhang records do not exist in the pool. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #58 (ML/reconstruction batch — file list verified, no Chandelier record), and #63 (SuperTrend ATR-flip trend long) — verified by file list; none shares this source or signal. Closest pool-adjacent record is open PR #63, a different mechanism in the same trailing-stop family. Five-axis distinction: anchor arithmetic differs (this record anchors both stops to 22-bar highest/lowest *close extremums* with one-sided ratcheting, versus #63 anchoring bands to median price `hl2` — extremum-anchored versus median-anchored stops flip on different bars by construction, so the trade-event sets differ); volatility estimator differs (Wilder-RMA `ta.atr(22)` times 3.0 versus plain-SMA `ta.sma(ta.tr, 10)` times 8.5 — different smoothing, length, and multiplier); state machine differs (dual ratcheted stop lines with an explicit close-vs-prior-stop priority ternary, versus a single `trend` int with strict band-touch rule); source identity differs (FMZ 437792 / ChaoZhang / blob `43879c25` versus a TradingView `VLRj2sG9` script); frame provenance differs (derived 1d port from a 10m source header, predeclared, versus #63's native 1d). Pool `psar-flip-stop-reverse` is a parabolic-SAR flip — a third, structurally different trailing-stop construction. No duplicate, paraphrase, or trivial parameter variant is created here.

## Economic mechanism

### Source-reported

ATR-anchored trailing-stop trend capture, long-only. The Chandelier hangs both stop lines off recent price extremes minus/plus a volatility multiple: sustained advances drag the long stop up behind price (ratcheted, never retreating while closes hold above it), so a close through the opposite line is read as trend failure. The design bets that 22-bar-extremum distance scaled by 3 ATRs separates genuine daily-frame trend rotation from ordinary volatility expansion, and that sitting out the short side avoids shorting blind momentum.

### Research interpretation

Extremum-anchored dual-stop state machine with no level, band, cloud, oscillator, or confirmation leg — long/flat only, never short, never leveraged-direction agnostic. Unlike median-anchored trailing systems (SuperTrend on `hl2`), every stop here is nailed to a printed 22-bar highest/lowest close, so stops jump only when a new extremum prints and otherwise creep only via ATR decay — entries fire strictly later after V-turns than median-band flips, at the cost of fewer fake flips inside ranges. Unlike oscillator-cross systems (MACD, KST, Fisher, Schaff, Qstick), no momentum rotation can trigger anything: only a close through a ratcheted volatility line flips state, so flat chop that never reaches either line produces no trade at all. Unlike breakout systems (Donchian, Darvas), the entry is not a fresh-range breakout but a state flip after the opposite line gives way — the long stop is the trailing risk line and the entry trigger in one object. The bet is on volatility-scaled extremum persistence on the daily frame, never on momentum rotation, a level break, a squeeze release, or mean reversion.

## Signal

Exact rule as pinned (22 / 3.0 / useClose=true frozen — the inputs at defaults; any other value is a different, unpinned rule):

- Declaration (derived): `strategy("Chandelier Exit Strategy", overlay=true)` with no timing/pyramiding/cost arguments (all pinned as absent); v5 builtins observed. Same-bar-close execution, 1d frame, and house sizing adopted for the derived record (none ships in the source). `calc_on_every_tick` is unset (defaults false: exactly one evaluation per completed bar). `showLabels`/`highlightState` are display-only and read by no order line.
- Stop arithmetic (pinned): `atr = 3.0 * ta.atr(length)` with `length = 22` (Wilder-RMA ATR — the v5 `ta.atr` smoothing, not SMA); `longStop = ta.highest(close, 22) - atr`; `shortStop = ta.lowest(close, 22) + atr` (`useClose = true` pinned — extremums are closes, never wicks).
- Ratchets (pinned, causal): `longStopPrev = nz(longStop[1], longStop)` then `longStop := close[1] > longStopPrev ? math.max(longStop, longStopPrev) : longStop` (the long line may only step up while closes hold above it); mirror logic steps the short line only down. All index reads are `[1]` prior-bar — no current-bar mutation, no repaint path.
- State machine (pinned, total priority): `var int dir = 1` initial, then `dir := close > shortStopPrev ? 1 : close < longStopPrev ? -1 : dir` — the long-side comparison is evaluated first, so a close satisfying both (possible only when `shortStopPrev < longStopPrev`) resolves to 1 by code, never ambiguous; otherwise the prior state holds. Strict comparisons: touching a line without closing through it flips nothing.
- Entry long: `buySignal = dir == 1 and dir[1] == -1` → `strategy.entry("Buy", strategy.long, qty = initial_capital / close)` — fires on the single bar where the state flips bearish-to-bullish on a confirmed close, with same-bar-close execution under the derived declaration (the source's own fill is next-bar-open — predeclared, never claimed as close).
- Exit: `sellSignal = dir == -1 and dir[1] == 1` → `strategy.close("Buy")` — the sole position-closing path. No stop, no target, no trailing beyond the stop lines themselves, no time exit — pinned as written, explicitly none, not invented.
- Direction: long-only by code (one long entry ID, one close leg, zero short legs; the page prose confirms buy-only). Before the first flip the system is flat (no position by construction); the initial `var dir = 1` means a bearish open prints its first `sellSignal` against no position — a no-op close, disclosed, never a phantom fill.

## Required data

- Completed `1d` bars of BTCUSDT: `close` (extremums, comparisons, sizing), plus `high`/`low` solely inside `ta.atr(22)` true-range arithmetic. No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (derived port from the header's `10m` — predeclared; the script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction; with market-entry/close legs only and no stop/limit legs anywhere, no intrabar path exists for a base granularity to affect).
- Warmup: the extremum windows need 22 completed `1d` bars and the Wilder ATR needs seeding on top. The adopted warmup is the first 50 completed `1d` bars flat by record rule (predeclared researcher choice — covers 22 plus RMA-seeding margin); no signal before bar 51 may trade. No repainting (all `[1]` references are completed prior bars; `dir` resolves on the completed close), no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (decision frame derived `1d` ported from the header's `10m`; venue class unchanged from the header's `Futures_Binance BTC_USDT` — predeclared derivation, never presented as source-native).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar-open (no execution-timing argument ships anywhere); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with one market entry leg and one close leg and flip-gated triggers, there is no same-bar ordering ambiguity of any kind.
- Sizing/capital/costs: the source ships a fixed `$25`-notional sizing (`initial_capital = 25`, `qty = 25 / close`) and no commission, fee, slippage, or margin assumption anywhere — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: no `pyramiding` ships anywhere, pinning the language default of no same-direction adds — at most one unit under the fixed order ID `Buy`; a `buySignal` can only print on a bearish-to-bullish flip, at which point no long exists (any prior long was closed by the intervening `sellSignal`), so same-side refires while positioned are impossible by state construction, not by convention; re-entry is allowed immediately on the next flip (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. Long-only needs no margin beyond the house isolated setting.

## Evidence

### Source-reported

The mirror ships the full construction (22 / 3.0 / close-extremum inputs, Wilder-ATR stop arithmetic, one-sided ratchets with `nz` first-bar guards, priority-ordered `dir` ternary, flip-only `buySignal`/`sellSignal`, fixed `Buy` order ID, `$25`-notional sizing, long-only close-to-flat exit), the 10m/1m December-2023→January-2024 backtest header, and the `吊灯出场策略Chandelier-Exit-Strategy` title with ChaoZhang authorship. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=` — the sole position-closing path is the bearish flip closing to flat, and the page's own Risk Analysis confesses `No stop loss in place after buying` and `No profit taking mechanism`. The absence is coded and source-admitted.
2. Long/flat with unbounded adverse excursion: after entry, nothing but the opposite flip exits — a market that grinds down without ever closing through the short-stop line is held the whole way; a market that chops across both lines flips repeatedly with full exposure each leg. This is the coded trade, disclosed, not a tunable parameter here.
3. Whipsaw is the source-admitted structural cost (`sensitive to volatility expansion which may cause false signals`): ATR expansion pushes both stops outward, so the flip arrives strictly after the move that caused it — late entries into completed moves followed by late exits are the coded smoother, disclosed, not shortened.
4. Initial-state bias fenced: `var int dir = 1` opens the state bullish with no position, so the first bearish flip prints a no-op close and only the first bullish flip can open — no phantom fill is claimable before the first `buySignal`.
5. Derivation boundary fenced: the only non-source-native behaviors in this record are the 10m→1d frame port, same-bar-close fills, the adopted 50-bar warmup with record-rule pre-warmup flat, house sizing/costs, and the BTC_USDT→BTCUSDT venue naming — all predeclared above; literals, stop arithmetic, ratchets, state-machine priority, both triggers, the order ID, long-only handling, and the risk posture are source-verbatim. This record is therefore never evidence that the original next-bar-open 10m source itself passes.
6. The `22` / `3.0` literals, the close-extremum construction (`useClose = true`), the strict flip (not touch) triggers, the prior-bar ratchet guards, the fixed `Buy` ID, the long-only posture, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning any literal, switching extremums to wicks, converting a flip into a touch or a level hold, adding a stop/target/filter/cooldown/gate, adding a short leg, or exiting to anything but flat would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `22/3.0` / close-extremum Wilder-ATR stops / one-sided ratchets / priority-ordered flip state machine / long-only / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Flip-timing relevance: replacing the flip-gated triggers with the always-live stop side (long whenever `dir == 1`, flat whenever `dir == -1`, evaluated every bar) must not improve net expectancy; fail ⇒ the flip timing adds nothing over holding the stop state.
- F2 — Long-only relevance: adding the mirror short leg (short on bearish flip, cover on bullish flip) must not improve net expectancy; fail ⇒ the source's long-only stance is dominated by the two-sided state machine on this market.
- F3 — Parameter relevance: replacing the pinned `22/3.0` pair with any adjacent classic pair must not improve net expectancy; fail ⇒ the pinned defaults carry no advantage over neighboring scalings and the record's literal choice is arbitrary.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision frame derived `1d`; venue class unchanged from the header's `Futures_Binance BTC_USDT`). The close-extremum plus true-range arithmetic ports across perpetual venues without structural change. Long-only needs no short venue permission. No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing and frame: the source fills next-bar-open on a `10m`-decision/`1m`-base backtest; this record executes same-bar-close on `1d` BTCUSDT perpetual. Backtest economics of the two timings and frames differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- No price stop, no time stop, no short side: adverse excursion after entry has no guardrail beyond the bearish flip, which may arrive many bars later or after deep excursion; a market that trends against the position without printing the opposite flip is held indefinitely. This is the coded posture, disclosed as the record's principal risk.
- No source cost declaration: no commission, fee, slippage, margin, or funding assumption ships anywhere in the source (only the `$25`-notional sizing) — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- RMA-seeding approximation: the adopted 50-bar warmup is a researcher choice covering the 22-bar extremum plus Wilder-ATR seeding margin, not a source-shipped warmup — pre-warmup bars are flat by record rule.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- FMZ canonical strategy page (ChaoZhang): https://www.fmz.com/strategy/437792
- Immutable mirror file at pinned commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (blob `43879c254b088fcd4ba9906ea9df9989e4366816`, 7876 bytes): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E5%90%8A%E7%81%AF%E5%87%BA%E5%9C%BA%E7%AD%96%E7%95%A5Chandelier-Exit-Strategy.md
- Pine strategy semantics (order calls, default execution, built-in averages): https://www.tradingview.com/pine-script-reference/v5/
