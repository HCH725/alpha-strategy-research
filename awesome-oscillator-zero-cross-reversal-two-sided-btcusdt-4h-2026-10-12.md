---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Awesome Oscillator zero-cross reversal two-sided on BTCUSDT 4h bars
created: 2026-10-12
updated: 2026-10-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-03-12
sources:
  - https://github.com/EternaHybridExchange/tradingview-strategies/blob/01e4346df876f6fd124332e40a2cd62286174894/strategies/momentum/awesome_oscillator.pine
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Awesome Oscillator zero-cross reversal two-sided on BTCUSDT 4h bars

## Provenance

Primary source read end to end (raw file fetched live over HTTPS twice this cycle — floating `master` and pinned commit — byte-identical, 4,099 bytes, SHA-256 `89da2199a00933b7f552765788535914fada294a65368446e5d95a3ffe359fe3`):

- Repository: https://github.com/EternaHybridExchange/tradingview-strategies (`master` default branch; repo created 2026-03-12; open-source collection of executable Pine Script strategies with alert-JSON handoff for automated execution).
- Immutable pin: commit `01e4346df876f6fd124332e40a2cd62286174894` (2026-03-12T18:38:03Z, `Initial commit: 20 Pine Script strategies with Eterna MCP in`), path `strategies/momentum/awesome_oscillator.pine` (102 lines, `//@version=5`). Adopted `source_as_of` 2026-03-12 is that commit's date, disclosed here, never an authorship date.
- Strategy declaration (source-verbatim): `strategy("Awesome Oscillator - Eterna MCP", shorttitle="AO", overlay=false, default_qty_type=strategy.percent_of_equity, default_qty_value=100, initial_capital=1000)`. No `pyramiding`, no `process_orders_on_close`, no `calc_on_every_tick`, no `commission_*` argument ships — Pine language defaults govern the unfrozen timing, fenced below.
- Text census over the pinned 102-line file: 1 `strategy("` declaration / 2 `strategy.entry` (`"Long"` with `strategy.long` gated `strategy.position_size == 0` plus buy-alert payload, `"Short"` with `strategy.short` gated `strategy.position_size == 0` plus sell-alert payload, no price/qty/when order argument) / 2 `strategy.close` (`"Long"` on `sellSignal` while long, `"Short"` on `buySignal` while short) / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=` / 1 live `crossover(` (`ta.crossover(ao, 0)`) / 1 live `crossunder(` (`ta.crossunder(ao, 0)`) / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `time(` / 4 `input.` (2 live trading inputs frozen below plus leverage/position-size webhook-payload parameters, fenced below) / 4 `position_size` reads (two flat-gates, two exit-side checks) / 2 `alert(` (JSON execution-handoff strings only — no order-leg effect, disclosed) / 2 `ta.sma(` / 2 `0[1]` literal history-references inside the dead twin-peak branches (fenced in Negative evidence) / 0 `commission` / 0 `barstate` / 0 `nz(` / 0 `na(` / display tokens only: 1 `plot(` (AO histogram) plus 1 `hline` (zero line) plus 6 `plotshape` (buy/sell/twin-peak/saucer markers) plus 1 `bgcolor` — render only, cannot change any order.
- Two live trading inputs frozen (any other value is a different, unpinned rule): `fastLength = 5`, `slowLength = 34` (Bill Williams standard, matching the sibling README's `Standard (Bill Williams): Fast 5, Slow 34` row). `leverageSize = 5.0` and `positionSize = 0.01` parameterize only the webhook-JSON handoff strings, never an order leg — house sizing/capital/costs replace the absent source economics (see Execution assumptions). The sibling README's `For crypto: Fast 3, Slow 21` variant is disclosed here and deliberately not adopted — this record freezes the code defaults, never the crypto-retuned variant.
- No risk layer ships anywhere in the executable code: zero stop/target/trailing/time-exit order legs — the no-stop/no-target posture below is the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention. No commission, slippage, funding, or margin assumption ships anywhere in the file — quoted here as coded absence, never read as zero cost (see Execution assumptions).
- Sibling README (same pin, `strategies/momentum/README_awesome_oscillator.md`, fetched live this cycle): Recommended Timeframes `Primary: 4H, 1D` / `Secondary: 1H, 1W` / `Best for: Trend trading and momentum plays`; Parameters `Fast SMA Length 5 / Slow SMA Length 34 / Leverage 5 / Position Size 0.01`; Trading Patterns prose claims three trigger families (zero-line cross, twin peaks, saucer — the code admits only the first, fenced in Negative evidence, never repaired); the sample-free risk phrase (`Win rate: ~60-70% in trending markets`) ships with no sample, period, or trade count and is omitted per the exact-numbers rule. The `4H` frame token is adopted as the record's decision timeframe (source-table-faithful Primary token, disclosed here, not code-derived — the code takes no timeframe input and makes no `request.*`/`security(` call, so it is single-frame by construction).
- The README ships no example-backtest section with dated results — this record therefore quotes no source-reported performance of any kind and claims no reproduced performance.

Licence and rights: the pinned file carries no licence gate; this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly five: (1) market pin `BTCUSDT` Binance futures (the source is market-agnostic via `{{ticker}}` webhook templating — the code names no symbol; the sibling README's setup section is venue-agnostic); (2) decision timeframe `4h` per the sibling README's Primary list (`4H, 1D` — the code takes no timeframe input and makes no `request.*`/`security(` call, so it is single-frame by construction); (3) same-bar-close fills on completed-bar decisions (the source ships no `process_orders_on_close`/`calc_on_every_tick` argument, so its backtest fills next-bar by language default; this record freezes completed-bar evaluation with same-bar-close execution and scopes any live intrabar behavior out, see Limitations); (4) an adopted 50-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 35th completed bar — slow-SMA-34 seed plus one crossover-lookback bar — see Required data); (5) house sizing/capital/costs replacing the absent source economics (see Execution assumptions). The `5/34` signal inputs, the median-price SMA-spread arithmetic, the zero-line cross triggers, the flat-gated entries, the fixed `Long`/`Short` order IDs, the opposite-signal exits, the Pine-default no-pyramiding semantics, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-12): working-tree case-insensitive searches for `awesome` return zero strategy records using this source script, file, or mechanism — the first raw-AO record in the pool. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool record is a different mechanism class despite the shared Bill Williams lineage: `ac-accelerator-rise-fall-two-sided-btcusdt-1d` trades the second-difference residual (AO spread minus its own 5-bar SMA) on bar-to-bar rise/fall recursion from FMZ 435716 — its own record fences that its code never performs an AO zero-cross. Five-axis distinction: mechanism differs (first-difference median-price spread crossing its own zero line, not a smoothed residual's rise/fall regime), signal construction differs (no pool record evaluates `ta.sma(median,5) - ta.sma(median,34)` as the traded quantity with a fixed zero threshold), trigger differs (zero-line cross entries with opposite-cross exits, not consecutive-color or rise-holding legs), data differs (`high`/`low` via the median plus cross reads on a single `4h` frame — no second timeframe, no volume, no residual recursion), and source identity differs (Eterna `momentum/awesome_oscillator.pine` at the pinned commit, never before admitted).

## Economic mechanism

### Source-reported

Bill Williams momentum-spread reversal (sibling README: `measures market momentum by calculating the difference between 5-period and 34-period simple moving averages of median prices. It identifies momentum shifts before they appear in price action`): each completed bar prints the AO spread of fast versus slow median-price averages as a histogram around a zero line. A long leg fires when the spread crosses up through zero with no position open — median-price momentum reclaiming the bullish half. A short leg mirrors it on the cross down. The position closes on the opposite cross. There is deliberately no stop, no target, and no flat state past seeding — the order block ends with the two `strategy.close` guards and no risk leg ships anywhere, by design gap rather than by hidden leg. The README's twin-peak and saucer prose describes patterns the executable code provably never fires (see Negative evidence) — this record pins the computation, never the prose label.

### Research interpretation

Zero-line-cross momentum reversal, two-sided with opposite-cross exits — the first raw-AO record in the pool. Unlike the pool's AC record (which trades the acceleration residual's rise/fall and holds through zero), this rule trades only the spread's own zero crossing, so it fires strictly less often and only at regime-median transitions; unlike oscillator level/threshold rules (RSI/CCI/Stoch bands), the threshold is the spread's own arithmetic zero rather than a fitted overbought/oversold level, so there is no threshold parameter to defend; unlike moving-average-cross trend records, the averaged quantity is the bar median rather than the close and the cross is against a fixed zero rather than a second average, so flat-chop behavior differs structurally. The bet is on median-price momentum regime change at frozen `5/34` geometry, not on any volatility extreme, level break, calendar effect, or smoothed-derivative regime.

## Signal

Exact rule as pinned (`fastLength 5 / slowLength 34` frozen — any other value, including the README's `3/21` crypto variant, is a different, unpinned rule):

- Declaration (source-faithful): `strategy("Awesome Oscillator - Eterna MCP", shorttitle="AO", overlay=false, default_qty_type=strategy.percent_of_equity, default_qty_value=100, initial_capital=1000)` semantics preserved with the derived `BTCUSDT 4h` market/frame pin and same-bar-close execution adopted (see derived declaration) and house sizing/costs replacing the source economics (see Execution assumptions). Pine-default no-pyramiding semantics hold (no `pyramiding` argument ships) and both entries are additionally flat-gated in code (`strategy.position_size == 0`): at most one open position; same-direction refires while positioned are blocked twice over (gate plus language default).
- Indicators (pinned arithmetic — evaluated from the frozen inputs, not tuned): `medianPrice = (high + low) / 2` — completed-bar median, causal; `fastSMA = ta.sma(medianPrice, 5)` / `slowSMA = ta.sma(medianPrice, 34)` — causal SMAs on completed-bar medians; `ao = fastSMA - slowSMA` — the traded spread.
- Effective triggers (code-verified — the twin-peak and saucer branches are identically false on every bar, proved in Negative evidence, so the combined signals collapse exactly): `buySignal ≡ bullishZeroCross = ta.crossover(ao, 0)`; `sellSignal ≡ bearishZeroCross = ta.crossunder(ao, 0)`.
- Entry long: `buySignal and strategy.position_size == 0` then `strategy.entry("Long", strategy.long)` — completed-bar spread crosses up through zero while flat. Fires on completed bars with same-bar-close execution under the derived declaration.
- Entry short: `sellSignal and strategy.position_size == 0` then `strategy.entry("Short", strategy.short)` — mirrored on the cross down.
- Exits (coded, the sole position-closing path): `sellSignal and strategy.position_size > 0` then `strategy.close("Long")`; `buySignal and strategy.position_size < 0` then `strategy.close("Short")`. No stop, no target, no trailing exit leg, no time exit — pinned as written, explicitly none, not invented.
- Direction: two-sided with coded flat states (pre-signal seeding flat by record rule; post-exit flat until the next fresh cross — disclosed, not enabled). A cross event prints on exactly one bar, and the entry gate requires flat on that same bar, so an exit bar never re-enters the opposite side the same bar: exits resolve to flat and the next position opens only on the next fresh cross. Entry order in source (long `if` before short `if`, exits after entries): the two entries are mutually exclusive by construction (`crossover(ao,0)` and `crossunder(ao,0)` of one series cannot co-print), the two exits are mutually exclusive for the same reason, so at most one entry leg and at most one exit leg fire per bar.
- Display isolation: the `plot`/`plotshape`/`hline`/`bgcolor` calls render only and cannot change any order; the two `alert(` JSON strings are execution-handoff payloads with no order-leg effect. No order logic reads any display output. The `leverageSize`/`positionSize` inputs are transport/payload parameters with no order-leg effect, disclosed.

## Required data

- Completed `4h` bars of BTCUSDT: `high`/`low` (median-price construction `(high + low) / 2`, the sole price read feeding both SMAs and every cross) — no `close` read, no `open` read, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read anywhere.
- Single decision timeframe `4h` (sibling README Primary list `4H, 1D`; the script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction).
- Warmup: the slow leg `ta.sma(medianPrice, 34)` needs 34 completed `4h` bars for its first full window, the spread is full from bar 34, and `ta.crossover/crossunder` reads `ao[1]` — the first evaluable cross state is the 35th completed `4h` bar. The adopted warmup is the first 50 completed `4h` bars flat by record rule (predeclared researcher choice — structural seed plus margin; ≈8.3 days of `4h` history). No negative shift, no future reference, no full-sample normalization; one evaluation per completed bar under the derived freeze. Each bar's prints enter the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (the source names no market — `{{ticker}}` webhook templating is market-agnostic — so the venue/symbol pin is a researcher market choice, disclosed, never presented as source-native; the `4h` frame comes from the source sibling README's Primary list).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source ships no `process_orders_on_close`/`calc_on_every_tick` argument (quoted verbatim in census) — its backtest fills next-bar by language default; this record does not claim that source behavior. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. Source order is entries before exits (long `if`, short `if`, then the two close `if`s): entries and opposite-side exits resolving same-bar follow that order deterministically under the declared fill convention; the pin-time proof in Negative evidence shows same-side entry/exit co-prints are arithmetically impossible (one series cannot cross zero both ways on one bar), so no reversal-vs-flat ambiguity survives.
- Engine path for `4h` (gate 5, stated plainly): `4h` is a Binance-documented USDT-M kline interval; the derived rule needs only completed `4h` candles (`high`/`low` for the median) on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no funding/OI/mark-price leg. That is the same single-frame completed-bar path as the admitted `1h`/`2h`/`15m`/`30m`/`1d` records (the `1h/4h/1d` whitelist stands removed as an independent ban, and no ban is reinstated here by another name). The AO spread is a deterministic fold over the completed-bar median stream — computable from the same single-frame candle stream with no extra feed. Anything beyond that single-frame completed-bar path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: the source ships Pine-default economics (`percent_of_equity 100 / initial_capital 1000`) with no commission, slippage, funding, or margin assumption anywhere (quoted verbatim in census as coded absence), plus payload-only `leverageSize`/`positionSize` parameters with no order-leg effect — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: Pine-default single-position semantics hold, doubled by the coded flat-gates — at most one open position under the order IDs `Long`/`Short`; same-direction refires are blocked by gate and language default (no `pyramiding` argument), exits are opposite-cross closes, and re-placement is allowed on the next fresh cross after any close (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (frozen `5/34` inputs, `(high+low)/2` median, dual `ta.sma` spread, `ta.crossover/crossunder(ao, 0)` triggers, flat-gated `Long`/`Short` entries, opposite-signal `strategy.close` exits, fixed order IDs under Pine-default no-pyramiding semantics, zero risk legs, zero cost assumptions), the active `strategy("Awesome Oscillator - Eterna MCP", ...)` declaration, and the sibling README's timeframe table (`Primary: 4H, 1D`, honored here) with the `Standard (Bill Williams): Fast 5, Slow 34` parameter row. The README's sample-free risk phrase (`~60-70%` win rate) is omitted for want of provenance, and its `3/21` crypto variant is disclosed-but-not-adopted. This record claims no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=` — the sole position-closing path is the coded opposite-signal `strategy.close` pair. The absence is coded (the order block ends with the two close guards and only plotting follows).
2. Twin-peak branches provably dead, stated plainly: `twinPeakBullish` conjoins leading `ao < 0` with trailing `ao > 0[1]` (a literal history-reference equal to the literal on every bar — and na-false even under the strictest reading), so it is identically false on every bar; `twinPeakBearish` conjoins leading `ao > 0` with trailing `ao < 0[1]` and is identically false the same way. Neither branch can print on any bar, warmup or otherwise.
3. Saucer branches provably dead, stated plainly: `saucerBullish` conjoins `ao < ao[1]` with `ao > ao[1]` — a direct self-contradiction, identically false on every bar (na-false where the spread is still seeding); `saucerBearish` conjoins `ao > ao[1]` with `ao < ao[1]` and is identically false the same way. The `consecutiveGreen`/`consecutiveRed` color legs occur only inside these dead conjunctions and therefore never gate any order.
4. Effective-signal collapse, stated plainly: with both pattern families identically false, `buySignal ≡ ta.crossover(ao, 0)` and `sellSignal ≡ ta.crossunder(ao, 0)` exactly — verified by code reading this cycle, never by assuming the README prose. The README's three-family trigger claim is therefore narrowed to the single code-admitted family; substituting any twin-peak or saucer trigger would be a different, unpinned rule, disclosed.
5. Same-side entry/exit co-print impossibility, stated plainly: one series cannot cross its zero line both ways on one bar, so no long-entry/long-exit or short-entry/short-exit same-bar ambiguity exists; post-exit flat until the next fresh single-bar cross is the coded consequence of the flat-gate plus single-bar cross events, disclosed under Signal.
6. No future leakage in the stack, stated plainly: at decision bar `t`, the median, both SMAs, the spread, and both cross reads consume completed-bar prints through `t` and seeded priors only. No `security()`, no `request.*`, no negative index, no `open`/`close`/`volume` read, no `barstate.islast`-gated path; `plotshape`/`bgcolor` markers render the same confirmed prints and cannot repaint a confirmed bar.
7. Label-versus-code gap fenced (mirroring the pool's own AC-record precedent): prose calls three patterns live, but the code trades the raw-spread zero-cross only — never the residual, never the patterns. The record pins the computation; anyone citing the prose label alone would describe a different rule.
8. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT market pin, the README-table `4h` frame adoption, same-bar-close fills (with live intrabar behavior scoped out), the adopted 50-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the inputs, median arithmetic, spread construction, cross triggers, flat-gates, order IDs, exits, and risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, timing, input set (including the README's `3/21` crypto variant), the alert-JSON execution handoff, or the prose-claimed twin-peak/saucer patterns of the source pass.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `5/34` median-spread geometry / zero-cross entries / opposite-cross exits / flat-gated two-sided / `4h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Trigger relevance: replacing the zero-cross entries with spread color-change entries (enter long when `ao > ao[1]`, short when `ao < ao[1]`, same exits) must not improve net expectancy; fail ⇒ the coded zero-cross adds nothing over its color-change twin.
- F2 — Quantity relevance: replacing the raw spread with the pool AC record's residual (`spread - sma(spread, 5)`, same zero-cross structure) must not improve net expectancy; fail ⇒ the first-difference spread adds nothing over its second-difference twin.
- F3 — Exit-leg relevance: replacing the opposite-cross exits with same-cross re-entry holding (exit long only on the next long cross and vice versa, same entries) must not improve net expectancy; fail ⇒ the coded opposite-cross exit adds nothing over its holding twin.

## Crypto portability

Pinned to BTCUSDT Binance futures `4h` under the house overlay (market pin is a researcher choice on a market-agnostic source; the `4h` frame is README-table-faithful Primary). The `(high+low)/2` SMA-spread arithmetic ports across perpetual venues without structural change; venue print differences move the spread but the rule reads only zero crossings, never an absolute level — disclosed. The rule is two-sided with no stop leg, so a spot-only deployment expresses the long state and reversal mechanics only to the extent the venue permits shorting — full two-sided expression assumes a futures venue, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere). Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source ships no `process_orders_on_close`/`calc_on_every_tick` argument (backtest fills next-bar by language default); this record evaluates completed bars only and executes same-bar-close on `4h` BTCUSDT. Backtest economics of the timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance. Any live intrabar behavior is out of scope.
- Derived market pin: the code names no symbol (`{{ticker}}`-templated webhook) — BTCUSDT is a researcher market choice for the house universe, never a source claim.
- Source economics absent: beyond Pine defaults the source ships no commission, slippage, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind. The README's sample-free `~60-70%` phrase is omitted for want of traceable provenance; the README ships no dated example backtest to fence.
- Dead-pattern prose: the README advertises twin-peak and saucer triggers the code provably never fires — anyone deploying from the prose instead of the pinned computation would trade a different, unpinned rule, disclosed here.
- No price stop, no time stop, post-exit flat gaps: adverse excursion after placement has no guardrail beyond the opposite cross; after any exit the system sits flat through potentially long zero-avoiding stretches. This is the coded posture, disclosed as the record's principal risk.
- Seed bars: the slow SMA needs 34 completed bars and the cross needs one lookback bar; the first 50 `4h` bars are flat by record rule, so early-history signals never enter any evaluation.
- Alert-handoff quarantine: the two `alert(` JSON strings (Eterna webhook handoff with `leverageSize`/`positionSize` parameters) are payload text with no order-leg effect — treating them as order semantics would be a different, unpinned rule, disclosed here.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record; the six-gate claim is pinned-engine expressibility of the declared rule, never a profitability, parity, or trading authorization.

## Adoption boundary

Research-only, not approved. No live, Paper, or Testnet authorization follows from this record. Any downstream standardized overlay (house DCA/capital/leverage), Qlib screening, or Hummingbot re-validation is a separate, explicitly authorized step outside this record.

## Related Wiki records

None.

## Sources

- https://github.com/EternaHybridExchange/tradingview-strategies/blob/01e4346df876f6fd124332e40a2cd62286174894/strategies/momentum/awesome_oscillator.pine (primary source — executable `//@version=5` strategy, 102 lines, fetched live 2026-10-12 at pinned commit byte-identical to `master`, 4,099 bytes, SHA-256 `89da2199…359fe3`; sibling README timeframe table `Primary: 4H, 1D` honored, `5/34` standard params frozen with `3/21` crypto variant disclosed-but-not-adopted, sample-free win-rate phrase omitted, no dated example backtest shipped)
- https://www.tradingview.com/pine-script-reference/v5/ (Pine semantics reference for census terms — defaults only, never a source of strategy facts)
