---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Balance-of-Power 0.8/-0.8 cross long-flat on BTCUSDT 1d bars
created: 2026-10-11
updated: 2026-10-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-02-24
sources:
  - https://www.fmz.com/strategy/483504
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E5%8A%A8%E9%87%8F%E9%98%88%E5%80%BC%E9%A9%B1%E5%8A%A8%E7%9A%84%E5%B9%B3%E8%A1%A1%E5%8A%9B%E9%87%8F%E4%BA%A4%E6%98%93%E7%AD%96%E7%95%A5-Momentum-Threshold-Driven-Balance-of-Power-Trading-Strategy.md
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Balance-of-Power 0.8/-0.8 cross long-flat on BTCUSDT 1d bars

## Provenance

Primary source read end to end (immutable public mirror file plus its recorded FMZ canonical page, fetched 2026-10-11):

- Canonical page: https://www.fmz.com/strategy/483504 (page title carrying `Balance of Power`, publisher account `ianzeng123`, `Created: 2025-02-24 09:35:40` stamp on the page, `Hits: 775`, `Copy: 3`). Fetched live over HTTPS during this cycle (708692 bytes). The page text states the full rule in prose twice (Chinese original plus English translation): core formula `(收盘价-开盘价)/(最高价-最低价)` measuring buyer/seller force balance, entry long when the Balance of Power indicator crosses up through `0.8`, flat exit when it crosses down through `-0.8`, dynamic equity-based sizing with adjustable leverage. The page-embedded `/*backtest*/` header reads `start: 2024-02-25 00:00:00`, `end: 2025-02-22 08:00:00`, `period: 1d`, `basePeriod: 1d`, `exchanges: [{"eid":"Binance","currency":"SOL_USDT"}]`. The visible declaration preview shows `strategy(title="Balance of Power for US30 4H", ... commission_value=0.01, ...)` and the single input `leverage = input.float(5, "Leverage 1:", ...)` in the strategy-parameters form. Page-wide order-call counts read `strategy.entry` 1 / `strategy.close` 1 / `strategy.exit` 0 / `strategy.order` 0, with zero `stop=` / `limit=` anywhere. Word-boundary counts over the whole landing HTML: `Net Profit` 0, `Profit Factor` 0, `Sharpe` 0, `Max Drawdown` 0, `Win Rate` 0, `Annualized` 0 — the page ships no performance numbers of any kind (adopted as `source_as_of` 2025-02-24 from the page creation stamp). Full Pine below the preview is login-gated on the canonical page (`Login to view full source` wall renders in place of the remainder); the executable detail below comes from the immutable mirror, whose prose description is byte-consistent with the page text.
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit date 2025-04-30 11:10:28 +0800, subject `update`; repository head verified via the GitHub commits API — the same head pin as the merged Darvas, Double-Seven, DPO-EMA, KST, Schaff, TRIX, SQZMOM-LB, Aroon, Qstick, AC, Elder-ray, ActionZone, Fibonacci and FRAMA admissions), exact file path `动量阈值驱动的平衡力量交易策略-Momentum-Threshold-Driven-Balance-of-Power-Trading-Strategy.md` (non-ASCII filename preserved verbatim; percent-encoded blob URL in Sources). File 7224 bytes, blob SHA `9ac1983ed941814da04ec67284cf29a0faeeb9ce` (verified against the GitHub contents API at the pinned commit — size and SHA both match). The mirror prints `> Detail` = https://www.fmz.com/strategy/483504 and `> Last Modified` = 2025-02-27 16:50:22. The mirror's `[trans]` prose (formula, 0.8 long entry, -0.8 close exit, equity sizing, leverage) matches the canonical page text quoted above.
- Full `//@version=5` block read in full (code lines from `/*backtest` through the final `box.new`/`line.new` display block, strategy declaration `strategy(title="Balance of Power for US30 4H", format=format.price, precision=2, default_qty_type=strategy.percent_of_equity, default_qty_value=100, overlay=true, commission_value=0.01, max_labels_count=500, max_lines_count = 500)`). The executable order block is four lines: `p = (close - open) / (high - low)`, `qty = strategy.equity * leverage / close`, `if ta.crossover(p, 0.8)` → `strategy.entry("L", strategy.long, qty=qty)`, `if ta.crossunder(p, -0.8)` → `strategy.close("L")`. Everything after the order block is display-only (`label.new` position-change markers, `tradeEntryPrice`/`tradeEntryBar` bookkeeping vars, `box.new`/`line.new` trade-range rendering — feeding no order condition).
- Text census over the pinned code block: 1 `strategy.entry` (`strategy.entry("L", strategy.long, qty=qty)` — long-only market entry, no price argument) / 1 `strategy.close` (`strategy.close("L")` — full close of that entry ID, no quantity qualifier) / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `time(` / 0 `volume` (the rule reads `open`/`high`/`low`/`close` only) / exactly 1 `input(` (`leverage = input.float(5, ...)` — pinned at default 5) / `pyramiding`, `process_orders_on_close`, `calc_on_every_tick`, `slippage` unset throughout (Pine language defaults apply — v5 `calc_on_every_tick` defaults false: exactly one evaluation per completed bar; default `pyramiding` 0: no same-direction adds). `commission_value=0.01` ships in the declaration (percent-of-trade default commission type, recorded as the source cost stub — see Execution assumptions).
- No risk layer ships anywhere in the source: zero stop/target/trailing/time-exit order legs. The cross-down-through-`-0.8` close posture below is therefore the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention.
- Page/mirror performance language is absent entirely (no table, figure, or number) — this record claims no source-reported performance and no reproduced performance.

Licence and rights: the canonical page is a public FMZ strategy publication by ianzeng123; the pinned code block carries no licence header of its own (the FMZ page is the publication vehicle). This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) market/frame pin `BTCUSDT 1d` — the source is frame-ambiguous (title and prose say `US30 4H` while the executable `/*backtest*/` header says executable `period: 1d` on `SOL_USDT`; this record follows the executable header's `1d` and the house universe's `BTCUSDT`, disclosed here, never presented as source-native); (2) same-bar-close fills (the source ships no execution-timing argument — Pine default fills evaluate per completed bar and fill on the next bar; no `process_orders_on_close` ships anywhere, quoted verbatim in census); (3) an adopted 5-bar warmup with pre-warmup bars flat by record rule (covers the 1-bar oscillator plus the 1-bar cross reference with margin — see Required data); (4) house sizing/capital replacing the source economics stub (`strategy.percent_of_equity` 100% × `leverage` 5 with `commission_value=0.01` — see Execution assumptions). The `(close-open)/(high-low)` formula, the `0.8` / `-0.8` literals, the `ta.crossover` / `ta.crossunder` triggers, the `"L"` order ID, the long-only direction handling, the full close leg, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-11): working-tree case-insensitive searches for `balance-of-power`, `balance of power`, word-boundary `bop`, and `483504` return zero hits anywhere — no admitted rule uses this source, author strategy, indicator, or mechanism. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closed research PRs (#1–#114 reviewed by title) contain no Balance-of-Power record. Closest pool records are different mechanism classes: `chande-momentum-80-cross-reversal` builds momentum from N-bar summed up/down closes (never the single-bar `(close-open)/(high-low)` body-to-range ratio); `cmf-velocity-zero-cross-ema200-bracket` and `klinger-volume-oscillator-trigger-flip` are volume-flow oscillators (this rule reads no volume); `elder-ray-123reversal-combo` measures bull/bear power as distances from a 13-EMA (never the bar's own body-to-range fraction); RSI/Williams-%R/Ultimate-Oscillator records use close-anchored or multi-bar accumulations (never open-anchored single-bar pressure). Five-axis distinction: mechanism differs (single-bar body-to-range pressure ratio with fixed ±0.8 cross triggers and long-flat state — versus accumulated, volume-flow, EMA-distance, or close-anchored oscillators), signal construction differs (no pool record computes `(close-open)/(high-low)` with `ta.crossover(p, 0.8)` / `ta.crossunder(p, -0.8)`), trigger differs (threshold-cross entry plus opposite-threshold full close on one long-only unit), and source identity differs (fmzquant pin `7853bb2` port of ianzeng123 483504, 2025-02-24).

## Economic mechanism

### Source-reported

Single-bar buying-vs-selling pressure capture (mirror Overview/Logic plus code, no performance section ships): the ratio of the bar's body (`close-open`) to its full range (`high-low`) reads where the close settled inside the bar's travelled ground. A print above `0.8` means buyers owned the bar almost end to end (close pinned near the high with little lower wick); the system buys that confirmed pressure. A print below `-0.8` means sellers owned the bar; the system goes flat rather than fading it. Between the rails the system holds whatever state it has — patience by construction, with at most one long unit and no short side. The design bets that bars closing at the extreme edge of their own range resolve further in the same direction often enough to pay for the flat waits, while the symmetric exit rail admits the pressure reversed.

### Research interpretation

Threshold-cross momentum riding with an explicit flat state, long-only. Unlike accumulated oscillators (RSI, Chande, Ultimate) that smooth many bars into a 0–100 memory, this rule has no memory at all: each bar's pressure is judged alone, and only the cross event (not the level) trades — holding above `0.8` without a fresh cross adds nothing, and drifting between the rails changes nothing. Unlike always-in-market flip systems, the rule rests flat before the first cross and after every exit, and it never shorts: seller-dominated bars only flatten, never reverse. The price of memorylessness is whipsaw at the rails (a `0.79 → 0.81 → 0.79` stutter can print entry, no exit, then a dead cross days later) and the exit rail's symmetry means a slow bleed that never prints below `-0.8` is held indefinitely. The bet is on single-bar edge-settlement persistence, not on any average, band, volume print, or calendar effect.

## Signal

Exact rule as pinned (`0.8` / `-0.8` frozen — any other value is a different, unpinned rule):

- Declaration (derived): `strategy(title="Balance of Power for US30 4H", ...)` semantics preserved with the derived `BTCUSDT 1d` market/frame pin and same-bar-close execution adopted (no such timing argument ships in the source) and house sizing replacing the source economics stub (see Execution assumptions). `calc_on_every_tick` is unset (defaults false: exactly one evaluation per completed bar). The source cost stub is `commission_value=0.01` with default percent commission type — pinned as the stub, with house costs applying to the derived evaluation (see Execution assumptions).
- Pressure oscillator (pinned): `p = (close - open) / (high - low)`, recomputed every bar from that completed bar's OHLC. Bounded in `[-1, 1]` on any bar with nonzero range; on a degenerate zero-range bar (`high == low`) the quotient is `na` in Pine (division by zero yields `na`, not an exception) and both cross functions evaluate false — deterministic, disclosed, not guarded (see Negative evidence).
- Entry long: `strategy.entry("L", strategy.long, qty=qty)` under `if ta.crossover(p, 0.8)` — fires on the single bar where `p` crosses strictly up through `0.8` (`p[1] <= 0.8 < p`), with same-bar-close execution under the derived declaration.
- Exit: `strategy.close("L")` under `if ta.crossunder(p, -0.8)` — full close of the long on any bar where `p` crosses strictly down through `-0.8` (`p[1] >= -0.8 > p`), with same-bar-close execution under the derived declaration. No stop, no target, no trailing, no time exit — pinned as written, explicitly none, not invented.
- Direction: long-only with an explicit flat state (the sole entry leg passes `strategy.long`; no short leg exists anywhere). Before two bars exist both cross functions are `na`/false by construction (no trade). On a spot venue the rule expresses unchanged (see Crypto portability).
- Display isolation: all `label.new` / `box.new` / `line.new` calls and the `tradeEntryPrice` / `tradeEntryBar` bookkeeping vars render or record only and cannot change any order; order logic reads exactly the two `if` lines.

## Required data

- Completed `1d` bars of BTCUSDT: `open` (pressure numerator), `high` (numerator anchor and range), `low` (range), `close` (numerator and settlement). No `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (derived pin following the source executable header's `period: 1d`; see derived declaration for the `4H` prose ambiguity). The script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction.
- Warmup: the oscillator needs 1 completed `1d` bar and each cross reads one prior bar; `ta.crossover`/`ta.crossunder` against `na` never fire. The adopted warmup is the first 5 completed `1d` bars flat by record rule (predeclared researcher choice — covers the 1-bar oscillator, the 1-bar cross reference, and margin). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. The current bar's OHLC enters the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (derived pin; the source executable header backtests `SOL_USDT` on `Binance` at `1d` while the title/prose say `US30 4H` — venue transfer and symbol spelling are disclosed here, never presented as source-native).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar fill (no execution-timing argument ships anywhere — quoted verbatim in census); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. Entry and exit legs are evaluated in source order (entry block before exit block): the two triggers are mutually exclusive by the strict cross definitions (see Negative evidence), so no same-bar double-fill ordering exists.
- Sizing/capital/costs: the source economics stub is `strategy.percent_of_equity` 100% × `leverage` input default 5 with `commission_value=0.01` (quoted verbatim — no capital, fee, slippage, funding, or margin assumption beyond that stub) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: no `pyramiding` ships anywhere, pinning the language default of no same-direction adds — at most one long unit under the fixed order ID `L`; entry refires while already long are no-ops by the language default, the exit leg closes in full, an exit while flat is a no-op, and re-entry is allowed immediately on the next `0.8` cross after any flat (no cooldown specified — explicitly none, not invented). Single engine position; no short side exists to conflict; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The mirror ships the full construction (`(close-open)/(high-low)` pressure ratio, `ta.crossover(p, 0.8)` long entry under fixed ID `L`, `ta.crossunder(p, -0.8)` full close, `leverage` 5 default, `commission_value=0.01`, display-only markers), the active `strategy(...)` declaration, the `Balance of Power for US30 4H` title, and the `/*backtest*/` header (2024-02-25→2025-02-22, `1d`, `Binance SOL_USDT`). It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=` — the sole position-closing path is the coded `strategy.close("L")` on the `-0.8` cross. The absence is coded (the order block ends with the close leg and only display code follows it in evaluation order).
2. Same-bar coincidence is impossible by construction, stated plainly: `ta.crossover(p, 0.8)` requires `p[1] <= 0.8` and `ta.crossunder(p, -0.8)` requires `p[1] >= -0.8`; both demand `p` strictly beyond opposite rails on the same bar (`p > 0.8` and `p < -0.8` simultaneously), which no single print satisfies — entry and exit legs are mutually exclusive on every bar, so no same-bar double-fill ordering exists under either fill convention.
3. Zero-range determinism fenced: on a bar with `high == low` (limit-locked or otherwise degenerate), `p` evaluates to `na` and both cross functions return false — the bar can neither enter nor exit, and the position state carries over unchanged. Deterministic, disclosed, not guarded.
4. Between-the-rails holding, admitted plainly: a long entered on a `0.8` cross is held through any number of bars while `p` stays inside `(-0.8, 0.8]`, including slow adverse drift that never prints at or below `-0.8` — there is no stop, no time exit, and no opposite-signal exit (no short side exists). This is the coded posture, disclosed as the record's principal risk.
5. Rail-stutter whipsaw, admitted plainly: because only the cross event trades (not the level), a `p` oscillating across `0.8` prints at most one entry per crossing bar (pyramiding 0 makes refires while long no-ops), but alternating `0.8`-up / `-0.8`-down crosses in chop print full round trips at the worst prints of each swing. Disclosed, not filtered.
6. The `0.8` / `-0.8` thresholds, the strict cross (not touch) triggers, the single-bar memoryless construction, the `open`-anchored numerator, the fixed `"L"` order ID, the long-only posture, the full close leg, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning either threshold, converting a cross into a touch, smoothing `p`, adding a stop/target/filter/cooldown, or enabling a short side would each be a different, unpinned rule — none is admitted here.
7. Derivation boundary fenced: the only non-source-native behaviors in this record are the `BTCUSDT 1d` market/frame pin, same-bar-close fills, the adopted 5-bar warmup with record-rule pre-warmup flat, and house sizing — all predeclared above; the pressure formula, both literals, both cross triggers, the order ID, the close leg, and the risk posture are source-verbatim. This record is therefore never evidence that the original `US30 4H` / `SOL_USDT 1d` source itself passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `(close-open)/(high-low)` / `0.8` / `-0.8` / strict crosses / long-only / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Threshold relevance: replacing the `0.8` cross entry with a `0.0` (midline) cross entry (same exit leg) must not improve net expectancy; fail ⇒ the extreme-pressure trigger adds nothing over a midline cross.
- F2 — Exit relevance: replacing the `-0.8` cross exit with a symmetric `0.8` cross-down exit (flattening as soon as pressure leaves the entry rail) must not improve net expectancy; fail ⇒ holding through mid-pressure decay is dominated by exiting with the entry edge.
- F3 — Memorylessness relevance: replacing the single-bar ratio with a 14-bar SMA of the same ratio (same thresholds and cross roles) must not improve net expectancy; fail ⇒ the memoryless single-bar construction adds nothing over a smoothed pressure average.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (derived pin from a Binance-backtested source). The open/high/low/close arithmetic ports across perpetual venues without structural change; the rule is long-only with no short leg, so a spot-only deployment expresses it unchanged. No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation — with the caveat that zero-range `1d` bars are rarer in crypto than in the source's US30 framing, making the `na` path an edge case rather than a regime (see Negative evidence). Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source fills next-bar on a `1d` Binance backtest with no timing argument; this record executes same-bar-close on `1d` BTCUSDT. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- Derived market/frame: the source title and prose frame the rule as `US30 4H` while its executable header backtests `SOL_USDT 1d`; this record pins `BTCUSDT 1d`. Cross-market and cross-frame behavior differences are real — the adaptation is disclosed, and this record makes no claim about the source market/frame's performance.
- No price stop, no time stop: adverse excursion after entry has no guardrail beyond the `-0.8` cross; a position whose pressure never prints at or below `-0.8` is held indefinitely. This is the coded posture, disclosed as the record's principal risk.
- Chop sensitivity: the memoryless cross-only triggers print full round trips on alternating rail crosses in ranging markets, and rail stutter at `0.8` can enter just before pressure collapses mid-range. The memorylessness is the coded construction, disclosed, not smoothed.
- No full source cost declaration: beyond the `commission_value=0.01` percent stub the source ships no capital, fee, slippage, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- FMZ canonical strategy page (ianzeng123, 2025-02-24): https://www.fmz.com/strategy/483504
- Immutable mirror file at pinned commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (blob `9ac1983ed941814da04ec67284cf29a0faeeb9ce`, 7224 bytes): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E5%8A%A8%E9%87%8F%E9%98%88%E5%80%BC%E9%A9%B1%E5%8A%A8%E7%9A%84%E5%B9%B3%E8%A1%A1%E5%8A%9B%E9%87%8F%E4%BA%A4%E6%98%93%E7%AD%96%E7%95%A5-Momentum-Threshold-Driven-Balance-of-Power-Trading-Strategy.md
- Pine strategy semantics (order calls, default execution, built-in cross functions): https://www.tradingview.com/pine-script-reference/v5/
