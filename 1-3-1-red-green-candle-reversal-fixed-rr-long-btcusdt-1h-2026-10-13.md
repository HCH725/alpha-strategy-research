---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: 1-3-1 red-green candlestick reversal with fixed 1R bracket long on BTCUSDT 1h bars
created: 2026-10-13
updated: 2026-10-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-10-27
sources:
  - https://www.fmz.com/strategy/430364
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/1-3-1-红绿K线反转策略1-3-1-Red-Green-Candlestick-Reversal-Strategy.md
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# 1-3-1 red-green candlestick reversal with fixed 1R bracket long on BTCUSDT 1h bars

## Provenance

Primary source read end to end (immutable public mirror file plus its recorded FMZ canonical page, fetched 2026-10-13):

- Canonical page: https://www.fmz.com/strategy/430364 (fetched live over HTTPS during this cycle with HTTP 200, 688130 bytes of landing HTML). Title token `1-3-1` × 20; porter token `ChaoZhang` × 2; Pine-author token `Genma01` × 2; executable-order tokens `strategy.entry` × 1 and `strategy.exit` × 1; bracket token `Take Profit` × 2; French-title token `Bougie Rouge` × 2; stanza venue tokens `Futures_Binance` × 2 and `BTC_USDT` × 2. The ZH/EN prose states the rule plainly: 1 red bar (close below open) followed by 3 green bars (close above open) whose closes rise in sequence, long at the pattern completion, stop at the red bar's low, target at entry plus the entry-to-stop distance (fixed 1R). The prose ships no quantified performance of any kind — only the qualitative remark that backtests were "good" (see Evidence).
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (verified as the repository HEAD via `git ls-remote` during this cycle — the same head pin as the merged Inside-Bar-Failure, Percent-B-MFI, Bollinger-breakout, PVT-EMA, KDJ, STARC, T3-Tillson, WaveTrend, Qstick, Aroon, SQZMOM-LB, TRIX, Schaff, KST, OBV-EMA and further admissions), exact file path `1-3-1-红绿K线反转策略1-3-1-Red-Green-Candlestick-Reversal-Strategy.md` (8671 bytes, non-ASCII filename quoted verbatim, no encoding ambiguity). The mirror prints `> Name` = `1-3-1-红绿K线反转策略1-3-1-Red-Green-Candlestick-Reversal-Strategy`, `> Author` = `ChaoZhang` (mirror porter; the Pine block itself credits `//by Genma01`), `> Detail` = https://www.fmz.com/strategy/430364, `> Last Modified` = `2023-10-27 16:00:41` (date part adopted as `source_as_of`), the `[trans]` ZH/EN prose matching the canonical page rule quoted above, and the complete executable Pine block.
- Full `//@version=5` block read in full (the entire 8671-byte file was retrieved; order-affecting lines are the three condition definitions, the stop/target assignments, the single `strategy.entry` leg, and the single `strategy.exit` leg; everything else is declaration, display, or porter plumbing). The `/*backtest*/` stanza prints verbatim `start: 2023-09-26 00:00:00`, `end: 2023-10-26 23:59:00`, `period: 1h`, `basePeriod: 15m`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]` — quoted here exactly as printed, never normalized into a claim (see Execution assumptions for the adopted research frame; `basePeriod: 15m` is FMZ execution granularity, not a signal frame).
- Text census over the pinned code block: 1 `strategy(` (French title `Stratégie tradosaure 1 Bougie Rouge suivi de 3 Bougies Vertes` / `overlay=true` / `default_qty_type = strategy.percent_of_equity, default_qty_value = 100` sizing stub — no capital, cost, timing, or pyramiding argument ships anywhere in the declaration) / 1 `strategy.entry` (`"Long"`/`strategy.long`, no `qty=`/`limit=`/`stop=`/`when=` qualifiers, gated on `strategy.position_size == 0`) / 1 `strategy.exit` (`"Take Profit/Stop Loss"`, `stop=` + `limit=`, no trailing qualifier) / 0 `strategy.close` / 0 `strategy.order` / 0 `strategy.short` / 0 `ta.*` / 0 `math.*` / 0 indicator calls of any kind (pure OHLC shape logic) / 0 `security(` / 0 `request.*` / 0 `timeframe(` / 0 `volume` / 0 `high` (only `open`/`close`/`low` series are read) / 0 `pyramiding` / 0 `process_orders_on_close` / 0 `initial_capital` / 0 `commission` / 0 `calc_on_every_tick`. No portable economics beyond the percent-of-equity sizing stub ships anywhere — recorded as an absent-economics stub, never as zero-cost evidence.
- Licence and rights: the mirror block ships no licence header line; this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.
- Prose-vs-code timing note (code governs): the ZH prose step 4 loosely says the long goes in "at the red candle's close", but the code evaluates the full conjunction on the third green bar's close (`redCandle` reads `close[3]`/lows `[3..0]`, `greenCandles`/`higherClose` read bars `[2..0]`), so the pattern only completes — and the entry only fires — on the third rising green's close. This record pins the coded timing, disclosed here, never the loose prose paraphrase.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) market/frame pin `BTCUSDT 1h` (the executable stanza itself backtests `Futures_Binance BTC_USDT` at `period: 1h` — the `1h` decision frame is therefore source-native; `basePeriod: 15m` granularity is disclosed as FMZ execution plumbing, not a second signal frame); (2) completed-bar decisions with same-bar-close fills (the source ships no execution-timing argument — Pine default evaluates per completed bar and fills on the next bar; no `process_orders_on_close` ships anywhere, quoted verbatim in census — this record pins completed-bar evaluation with same-bar-close fills and claims no next-bar timing, disclosed here); (3) an adopted 10-bar warmup with pre-warmup bars flat by record rule (covers the `[3]` seed with margin — see Required data); (4) house sizing/capital/costs replacing the percent-of-equity stub (see Execution assumptions). The red-plus-three-rising-greens conjunction, the lowest-low anchor, the flat-only gate, the red-low stop, the fixed 1R limit arithmetic, the single-position book, the long-only stance, and the bracket-only exit posture are source-native and unmodified. No tie-break had to be invented: there is exactly one entry leg and one exit leg, and the stop-first same-bar rule resolves the only ordering question (see Negative evidence).

Pre-write dedup (2026-10-13): working-tree case-insensitive filename search for `1-3-1` and content search for `tradosaure` / `Bougie Rouge` return zero strategy records; the only `red/green` pool hit is a bar-coloring remark in the KVO evidence prose (`klinger-volume-oscillator-trigger-flip-two-sided-btcusdt-1d-2026-10-10.md` — a Klinger-oscillator trigger-flip machine, not a candle-pattern rule). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `double-seven-connors-pullback-long-btcusdt-1d-2026-10-09.md` buys a 7-close pullback under a 200-day regime average with a channel-maximum signal exit (streak pullback, no red-green alternation, no fixed bracket); `dual-ema-engulfing-volume-long-btcusdt-1h-2026-10-07.md` requires an engulfing bar plus dual-EMA alignment plus a volume gate (two-bar engulf, not a 4-bar alternation; no stop/target arithmetic); `catching-the-bottom-rsi-dip-reversal-long-ethusdt-1h-2026-10-08.md` is an RSI-gated dip buy (oscillator gate, not candle geometry); `elder-ray-123reversal-combo-two-sided-btcusdt-1h-2026-10-09.md` couples Elder-Ray power with a 123 pivot structure (pivot highs/lows, not open-vs-close color sequence); `williams-fractal-ema-band-fixed-rr-two-sided-btcusdt-1d-2026-10-10.md` shares only the fixed-RR bracket idiom (1.5R off fractal pivots, two-sided) with a wholly different pivot/EMA-band signal. Five-axis distinction: no pool record and no open PR conditions entries on a red bar anchoring the 4-bar lowest low followed by exactly three rising green closes, and none pairs that alternating-color confirmation with a red-low stop and a fixed 1R limit, long-only, bracket-or-nothing. Not a trivial parameter variant.

## Economic mechanism

### Source-reported

Dip-anchored reversal confirmation off a four-bar color alternation: a red bar prints the local wash (its low must be the lowest of the whole 4-bar window — the sellers exhausted themselves there), and three subsequent green bars with strictly rising closes confirm the buyers have retaken the tape in sequence rather than in one lucky print. The design buys only the completed confirmation (never the red bar itself, never the first or second green), then brackets the trade at exactly 1R: stop under the proven wash low, target one full risk-distance above entry. The premise is that a wash low that holds through three rising closes keeps holding long enough to pay one unit of its own risk, while any print back under the wash low invalidates the pattern in full. The prose ships no trailer, no partial, no second entry, no opposite-side leg: the bracket plus the flat-only gate are the entire risk control.

### Research interpretation

Four-bar alternating-color confirmation machine, event-driven, long-only, bracket-or-nothing. Unlike every streak-pullback record in the pool (Double-Seven, Connors-RSI2) this system demands color alternation, not continuation: four same-color bars fire nothing by construction, and the entry requires the sequence to resolve red-first-then-three-green in that exact order. Unlike oscillator-gated dip buys there is no level, no smoothing, no band: the signal is pure open/close color plus one low anchor. Unlike stop-carrying trend records the stop is not volatility-scaled but pattern-anchored (the red bar's own low), and the target is not trailing but a hard 1R cap — winners can never run, losers always pay the full wash distance. The edge, if any, lives in the documented tape intuition that an exhaustion low confirmed by three sequentially higher closes tends to see at least one more risk-unit of follow-through before failing — a bet on hours-scale post-wash drift, not on any trend, level, indicator, calendar effect, or second timeframe.

## Signal

Exact rule as pinned (no inputs exist — any added parameter is a different, unpinned rule):

- Declarations (derived): long-only long/flat machine over `BTCUSDT 1h` with same-bar-close execution and house sizing/costs (see Execution assumptions). State ∈ {flat, long}; no short leg exists anywhere.
- Red anchor, pinned verbatim, evaluated on completed bar `t`: `redCandle(t)` = `close[t-3] < open[t-3]` (red three bars ago) and `low[t-3] < low[t-2]` and `low[t-3] < low[t-1]` and `low[t-3] < low[t]` (the red bar's low is the strict lowest low of the 4-bar window including the current bar — a tie on any low fires nothing).
- Green confirmation, pinned verbatim: `greenCandles(t)` = `close[t] > open[t]` and `close[t-1] > open[t-1]` and `close[t-2] > open[t-2]` (three consecutive green closes; the red bar itself is excluded from this leg by construction).
- Rising-close chain, pinned verbatim: `higherClose(t)` = `close[t] > close[t-1]` and `close[t-1] > close[t-2]` (strictly ascending closes across the three greens; any flat step fires nothing).
- Entry long, pinned verbatim: `if (redCandle and greenCandles and higherClose) and strategy.position_size == 0` → `strategy.entry("Long", strategy.long)`, evaluated on the completed-bar close with same-bar-close execution under the derived declaration. Setups printing mid-trade are discarded unseen (flat-only gate, explicitly no queue, no add).
- Bracket, pinned verbatim: on the signal bar, `stopLossPrice := low[3]` (the red bar's low) and `takeProfitPrice := close + (close - stopLossPrice)` (entry-bar close plus exactly one risk distance — fixed 1R, no multiplier input exists). While positioned, `strategy.exit("Take Profit/Stop Loss", stop=stopLossPrice, limit=takeProfitPrice)` holds the resting OCO pair; first-touch resolution with the stop-first same-bar rule (see Execution assumptions). No trailing, no partial, no breakeven move, no time exit — pinned as written, explicitly none, not invented.
- Display isolation: the block's `plotshape`/`plot` calls render entry triangles and the stop/target lines only and cannot change any order condition.

## Required data

- Completed `1h` bars of BTCUSDT: `open` (color legs), `close` (color legs, rising chain, 1R arithmetic), `low` (wash-low anchor and stop level). No `high`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1h`. The script takes no timeframe input and makes no live `request.*`/`security(`/`timeframe(` call, so it is single-frame by construction; `basePeriod: 15m` in the FMZ stanza is execution granularity, never a signal input, disclosed here.
- Warmup: each setup reads bars `t` through `t-3`, so the first signal-eligible bar is the 4th completed `1h` bar; the stop/target arithmetic reads the same window (pure history reference, no future). This record adopts a 10-bar warmup with pre-warmup bars flat by record rule, covering the seed with margin. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT under the house overlay (the rule reads completed-bar open/close/low only; venue transfer is never presented as source-native semantics). Long-only, so the rule expresses unchanged on spot or perps with no short permission needed.
- Order timing (predeclared derivation): completed-bar decisions with same-bar-close market entries and a resting stop+limit OCO pair armed from the bar after entry, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar-open by Pine default; this record does not claim source fills. No maker-touch, queue, or intrabar-path-dependent fill beyond first-touch bracket resolution with the pinned stop-first same-bar rule. Zero `strategy.close`/`strategy.order` calls, hence no close-vs-exit ordering ambiguity anywhere in the rule.
- Sizing/capital/costs: the block's percent-of-equity sizing stub ships no portable economics — the explicit house overlay (Base 6% + Safety 6% + Safety 6% capital framing, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) replace it here, never presented as source-native behavior. No safety-order layering is admitted: entries while positioned are blocked by code, so any DCA add would change trade events and would be a different, unpinned strategy.
- Concurrency: at most one long position at any time; the bracket is the sole closer; re-entry on the next completed setup after resolution with no cooldown specified — explicitly none, not invented. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (porter header with author/porter credits, ZH/EN prose with the six numbered rule steps, the `/*backtest*/` stanza, the versioned Pine block with the three named condition legs, the `low[3]` stop assignment, the `close + (close - stop)` 1R limit arithmetic, the flat-gated entry leg, the always-armed stop+limit exit leg, and the display-only plots). It ships zero quantified performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — only the prose's unquantified "good backtest" remark, which this record does not adopt as evidence. This record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Strictly positive risk on every setup, proved: the anchor forces `low[t-3] <= low[t] <= close[t]`, and equality `close[t] == low[t-3]` would force every intermediate print equal, contradicting the strict rising-close chain — so the 1R bracket always has nonzero distance and the OCO can never collapse to a flat scratch. Structural, pinned, not assumed.
2. No hidden exits or second legs: 0 `strategy.close`, 0 `strategy.order`, 0 short-direction calls — the stop+limit bracket is the sole position-ending path by construction, and the prose promises no trailer, no partial, no time exit.
3. Flat-state determinism: the exit leg is guarded by `position_size > 0` and the entry by `position_size == 0`; with no open position both legs are deterministic no-ops, and the seed bars satisfy no order condition by themselves (every leg needs bars `t-1` through `t-3`).
4. Same-bar stop/limit determinism: the only ordering question in the rule is a bar that first-touches both bracket arms — resolved by the record's pinned stop-first same-bar rule, never guessed per-trade.
5. Ties are dead bars, pinned: equality on any color comparison, any rising-close step, or any low-anchor comparison fires nothing; a zero-range red bar (`close[t-3] == open[t-3]`) fails the strict red test outright.
6. The 4-bar window, the lowest-low anchor, the three-green requirement, the rising-close chain, the `low[3]` stop, the 1R limit arithmetic, the flat-only single-position book, the long-only direction, and the bracket-or-nothing posture are pinned, not removed: dropping the rising chain, widening the anchor to touches, retuning the target multiple, adding a trailer/cooldown/session filter, or enabling the mirror short would each be a different, unpinned rule — none is admitted here.
7. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT-`1h` research frame (against the stanza's verbatim `period: 1h` / `basePeriod: 15m` labels), same-bar-close fills, the 10-bar warmup, and house sizing/costs — all predeclared above; every color leg, anchor, chain, gate, stop/limit arithmetic, ordering, and risk posture is source-verbatim. This record is therefore never evidence that the original next-bar-open source itself passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: red-then-three-rising-greens / lowest-low anchor / `low[3]` stop / fixed 1R limit / long-only / flat-only book / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Rising-chain relevance: admitting any three greens (dropping `higherClose`) instead of the strictly ascending closes must not improve net expectancy; fail ⇒ the sequential-confirmation chain adds nothing over a plain color count.
- F2 — Anchor relevance: admitting any red-then-three-green shape (dropping the lowest-low anchor) instead of the wash-low requirement must not improve net expectancy; fail ⇒ the exhaustion-low anchor adds nothing over unanchored alternation trading.
- F3 — Bracket relevance: holding each entry a fixed 5-bar clock instead of the coded 1R stop+limit bracket must not improve net expectancy; fail ⇒ the pattern-anchored 1R bracket adds nothing over time-boxed holding of the same setups.

## Crypto portability

Pinned to BTCUSDT under the house overlay. The open/close/low-only long-only logic ports to perps or spot without structural change; no short leg exists, so no short-capable venue is required. No funding-dependent leg, no stablecoin-specific assumption, no session, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read beyond the printed open/close color, so session-gap behavior is simply absent rather than approximated. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source fills next-bar-open; this record executes same-bar-close. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- One-month stanza window: the FMZ stanza prints a single 2023-09-26→2023-10-26 month; nothing here is calibrated, fitted, or tuned to any window, and no window performance is claimed.
- Bracket-or-nothing rigidity: winners cap at exactly 1R with no trailer and no partial — a trend hour that runs 5R keeps 1R; losers always pay the full wash distance. This is the coded posture, disclosed, not a tunable parameter here.
- Setup drought by construction: the four-bar conjunction (strict red + lowest-low anchor + three greens + rising chain + flat book) fires infrequently, and setups printing mid-trade are discarded unseen — long flat stretches and skipped signals are the coded trade, disclosed, not smoothed.
- Single-position fragility: one bracket holds the whole book; a vertical-against move pays the full stop with no early-abort leg beyond the stop itself.
- Performance evidence is absent: the canonical page reports no numbers at all; nothing here is calibrated, fitted, or tuned to any backtest.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Event-level Qlib/Hummingbot parity on the declared stop+limit route must be demonstrated before any mass screening use.

## Adoption boundary

Research-only. Not approved for any live, Paper, or Testnet deployment. Admission here means model-consistent expressibility under the pinned engine only — not profitability, not Qlib parity, not source-native equivalence for the timing derivation, and not trading authorization.

## Related Wiki records

None.

## Sources

- https://www.fmz.com/strategy/430364 (canonical FMZ page, fetched HTTP 200 during this cycle)
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/1-3-1-红绿K线反转策略1-3-1-Red-Green-Candlestick-Reversal-Strategy.md (immutable mirror file at pinned HEAD, 8671 bytes)
- https://www.tradingview.com/pine-script-reference/v5/#fun_strategy (Pine v5 order-semantics reference for `strategy.entry` / `strategy.exit` defaults cited in gate reasoning)
