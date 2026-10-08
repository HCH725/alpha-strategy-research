---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Ichimoku triple-confirmation MACD-trigger two-sided reversal system on ETHUSDT 1h bars
created: 2026-10-08
updated: 2026-10-08
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: high
source_as_of: 2022-08-18
sources:
  - https://www.tradingview.com/script/DtsAIRvK-Ichimoku-Cloud-with-MACD-By-Coinrule/
  - https://github.com/hasnocool/tradingview-pine-scripts/blob/69969aeaf271b2f7b5a7632a1bde43069a0cbe26/Ichimoku%20Cloud%20with%20MACD%20(By%20Coinrule).pine
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---
# Ichimoku triple-confirmation MACD-trigger two-sided reversal system on ETHUSDT 1h bars

## Provenance

Primary source read end to end (TradingView canonical strategy page, live browser read 2026-10-08):

- Canonical page: https://www.tradingview.com/script/DtsAIRvK-Ichimoku-Cloud-with-MACD-By-Coinrule/ (`Ichimoku Cloud with MACD (By Coinrule)`, Strategy by Coinrule, `OPEN-SOURCE SCRIPT`, updated Aug 18 2022, adopted as `source_as_of`).
- Page-chart context at read time: BINANCE ETHUSDT on a 30m chart — a display context, not a strategy rule (the script takes no symbol, timeframe, session, or venue input).
- Page-stated rules (verbatim substance): Long Position = Tenkan-Sen above Kijun-Sen, Chikou-Span above the close of 26 bars ago, close above the Kumo Cloud, MACD line crosses over the signal line. Short Position = the exact mirror (Tenkan below Kijun, Chikou below the close of 26 bars ago, close below the Kumo Cloud, MACD crosses under the signal line). Page further states the script is backtested from 1 June 2022, that each order uses 30% of available coins, that a 0.1% fee aligned to the Binance base fee is assumed, and that it works well on MATIC (1h), AVA (45m), and BTC (30m). The page carries no numeric performance table — no returns, win rate, drawdown, or trade-count figures anywhere in the prose (only qualitative "good returns" claims). The Aug 18 2022 release note reads "Removed stop loss code since it is not used".
- Immutable code provenance: hasnocool mirror file `Ichimoku Cloud with MACD (By Coinrule).pine` at pinned commit `69969aeaf271b2f7b5a7632a1bde43069a0cbe26` (verified still the remote HEAD via `git ls-remote` this run after a pristine shallow clone), blob `da95fe685232d8937f7e9617ad1b0630f971bf98`, 3674 bytes. The mirror header (`Script Name`, `Author: Coinrule`, Ichimoku/MACD description lead) matches the canonical page, and the embedded Pine v5 block implements exactly the page-stated rules with defaults (Tenkan 9 / Kijun 26 / Senkou-B 52 / Chikou offset 26 / cloud shift 26 / MACD 12-26-9 on close / 2022-06-01 floor / 30%-equity sizing / 0.1% commission — see Signal). The `2022-06-01` code floor is the same date as the page's "backtested from 1 June 2022" statement, and the release note's removed stop-loss corroborates the block's 0 `strategy.exit` census.
- Censuses over the pinned block: `strategy.entry` 2, `strategy.close` 2, `strategy.exit` 0, `strategy.order` 0, `strategy.close_all` 0, `request.*` 0, `security(` 0, `timeframe(` 0, `stop=` 0, `limit=` 0, `profit=` 0, `loss=` 0, `pyramiding` 0, `calc_on_every_tick` 0, `calc_on_order_fills` 0, `varip` 0, `volume` 0, `heikin` 0. Series read by order logic: `close`, `high`, `low` (inside the Donchian-midpoint components only) plus bar `time` inside the deterministic date floor (causal, never future). `open` and `volume` occur 0 times in any order-gating line. `plot`/`fill` lines are display-only and never gate an order.

Licence and rights: the canonical page is an open-source publication by Coinrule. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

Pre-write dedup (2026-10-08): working-tree searches for `DtsAIRvK`, `Ichimoku Cloud with MACD`, and `macd_histogram` return 0 strategy records using this source or signal. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long, FMZ 451075) and #49 (Gaussian channel StochRSI-gated breakout long, FMZ 482888), plus reconstruction-lane #58 — different mechanisms, indicators, and sources. Closed research PRs #17 (MACD histogram) and #20 (Ichimoku-RSI) never reached `main` and are different constructions in any case. Closest pool records are different mechanism classes: `ichimoku-rsi-gated-reversal-btcusdt-1d-2026-10-08.md` (Ichimoku position plus RSI-14 level gate, 0 crossovers anywhere, no MACD), `ichimoku-cloud-adx-trend-filter-btcusdt-1d-2026-10-06.md` (Ichimoku plus asymmetric DMI/ADX legs, 0 MACD occurrences, no series crossover), `octa-ema-ichimoku-trend-long-btcusdt-1d-2026-10-07.md` (8-EMA ribbon cross long-only with an Ichimoku-variant filter, no MACD, no short side). Five-axis distinction: mechanism differs (three Ichimoku confirmation legs AND-gated with a MACD line/signal crossover trigger, two-sided reversal-only exits), signal construction differs (no pool record fires on `ta.crossover/crossunder(macd, signal)`; the trigger leg is unique on `main`), exits differ (pure opposite-signal reversal, no level leg, no stop anywhere — the page's own release note confirms the stop was removed), source identity differs (Coinrule TV Aug-2022 `DtsAIRvK` plus hasnocool blob `da95fe6`), and research frame is ETHUSDT `1h` (the page's display context was ETHUSDT; MATIC itself is outside the house universe).

## Economic mechanism

### Source-reported

A trend-following entry timer: the Ichimoku triple confirmation (Tenkan above Kijun, Chikou above price 26 bars ago, price above the displaced cloud) establishes that a genuine directional regime is in place, and the MACD line crossing its signal line times the entry inside that regime rather than anticipating it. The short side mirrors the logic for downtrends. No stop, target, or time leg exists — the Aug 2022 release note states the stop-loss code was removed as unused, so positions end only when the opposite regime prints.

### Research interpretation

Regime-gated crossover timing with reversal-only bookkeeping. The three Ichimoku legs are slow, sticky state (trend alignment, 26-bar momentum displacement, displaced-cloud position), so chop that whips the MACD cannot fire without the regime's permission; the MACD cross is the fast trigger that converts a standing regime into an event. Because both `strategy.close` legs are dead at pinned defaults (see Signal), the book is always exactly long, short, or flat-before-first-entry — every exit is an opposite-regime reversal printed at the same bar close, which keeps the event sequence fully determined by completed bars. No leverage, sizing, or cost edge is embedded in the signal; the declaration carries only event-neutral accounting lines (1000 capital, 30%-of-equity sizing, 0.1% commission — the page's own 30%/0.1% framing confirms their accounting nature), so the house overlay supplies them (see Execution assumptions).

## Signal

Exact rule as pinned (Pine v5, defaults quoted — inputs unmodified; both `long_entry`/`short_entry` pinned true):

- Declaration: `strategy('Ichimoku Cloud with MACD (By Coinrule)', overlay=true, initial_capital=1000, process_orders_on_close=true, default_qty_type=strategy.percent_of_equity, default_qty_value=30, commission_type=strategy.commission.percent, commission_value=0.1)`. `calc_on_every_tick` is unset (default false); `pyramiding` is unset (v5 language default 0: no additional same-direction entry while positioned — the same default-convergence earlier PASS reviews accepted for Coinrule blocks, and it is load-bearing here, see Execution assumptions).
- Date floor: `timePeriod = time >= timestamp(syminfo.timezone, 2022, 6, 1, 0, 0)` — deterministic, causal (bar `time` only), true for every bar on/after 2022-06-01. Bars before the floor admit no entries and no closes by explicit rule (pinned, not invented); this is the code form of the page's "backtested from 1 June 2022" scope. `showDate = input(defval=true, title='Show Date Range')` is write-only display state, never read by any order condition.
- Ichimoku components: `middle(len) => math.avg(ta.lowest(len), ta.highest(len))` over high/low; `tenkan = middle(9)`, `kijun = middle(26)`, `senkouA = math.avg(tenkan, kijun)`, `senkouB = middle(52)`; displaced-cloud edges `ss_high = math.max(senkouA[25], senkouB[25])`, `ss_low = math.min(senkouA[25], senkouB[25])` (the `[ss_offset - 1]` = `[25]` back-shift exactly cancels the 26-bar forward plot displacement, so both edges are causal completed-bar values — no future reference).
- MACD: `[macd, macd_signal, macd_histogram] = ta.macd(close, 12, 26, 9)` (first-party v5 semantics: 12-bar fast EMA minus 26-bar slow EMA on `close`, 9-bar signal EMA; `macd_histogram` is computed but never read by any order condition).
- Bullish conjunction (all four on the same completed bar): `tk_cross_bull = tenkan > kijun` (strict; equality fires neither side); `cs_cross_bull = ta.mom(close, 25) > 0`, i.e. `close > close[25]` (the code form of "Chikou above the close of 26 bars ago"); `price_above_kumo = close > ss_high` (strict); `ta.crossover(macd, macd_signal)` (strict v5 edge semantics — a tie on either compared bar fires neither leg).
- Bearish conjunction (exact mirror): `tenkan < kijun`, `ta.mom(close, 25) < 0`, `close < ss_low`, `ta.crossunder(macd, macd_signal)`.
- Orders: `strategy.entry('Long', strategy.long, when=bullish and long_entry and timePeriod)`; `strategy.entry('Short', strategy.short, when=bearish and short_entry and timePeriod)`; `strategy.close('Long', when=bearish and not short_entry)`; `strategy.close('Short', when=bullish and not long_entry)`. At pinned defaults (`long_entry = short_entry = true`) both close legs are provably dead code — the sole exit path is opposite-signal reversal through the entry calls, recorded explicitly as the admitted no-signal-exit semantics, not repaired or removed.
- Direction: two-sided, explicitly. Both entries are live at pinned defaults; disabling either side would be a different, unpinned rule.
- Stop-loss / take-profit / trailing / time limit: explicitly none (0 `strategy.exit`, 0 `stop=`/`limit=`/`profit=`/`loss=`; the page's release note independently confirms the stop code was removed).
- Inert code, provably excluded: `showDate`, `macd_histogram`, all `plot`/`fill` lines, the Senkou/Chikou plot offsets (display displacement only; order logic reads the back-shifted causal edges).

## Required data

- Completed `1h` bars of ETHUSDT: `close` (MACD, Chikou displacement, cloud position, both cross edges), `high`/`low` (inside the Donchian-midpoint components only), plus bar `time` for the pinned date floor. No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1h`. The script takes no timeframe input and makes no live `request.*`/`security(`/`timeframe(` call, so it is single-frame by construction; `1h` is adopted as the in-lane research frame because it is source-listed applicability (MATIC 1h) while MATIC itself sits outside the house universe — `1h` is the explicitly labeled house-overlay instantiation, never presented as a source-declared frame (see Limitations).
- Warmup: longest causal chain is `senkouB[25]` (52-bar midpoint, first defined at bar 52, back-shifted read needs bar 77); the crossover prior-bar reference needs one further bar. First fully-defined evaluation at the 78th completed `1h` bar; no signal is evaluable before that. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: ETHUSDT under the house overlay (the canonical page's own display context was BINANCE ETHUSDT and ETH is inside the house universe; MATIC itself is outside the universe, so ETH is the closest source-faithful instantiation — never presented as source-native venue semantics; the rule reads OHLC only).
- Order timing: the declaration sets `process_orders_on_close = true` with `calc_on_every_tick` unset (default false): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. No next-bar-open, maker-touch, queue, or intrabar-path-dependent fill.
- Sizing/capital: the declaration's 30%-of-equity sizing, 1000 initial capital, and 0.1% commission lines are pure event-neutral accounting (the page's own 30%/0.1% framing confirms their accounting nature), replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions, never presented as source-native behavior.
- Concurrency: `pyramiding` is unset (v5 default 0: no same-direction add while positioned). The default is load-bearing here and therefore pinned explicitly: the sticky Ichimoku legs (Tenkan above Kijun, price above cloud) can persist across many bars while long, and repeat MACD crosses can print before any reversal — the admitted rule blocks every such add and holds. Re-entry is allowed immediately after any reversal whenever the four-leg conjunction fires again (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The canonical page ships prose only: qualitative claims (June-2022 scope, MATIC 1h / AVA 45m / BTC 30m applicability, 30% sizing, 0.1% Binance-aligned fee, stop code removed as unused) plus rule bullets that match the pinned block leg for leg. The page carries no numeric performance table — no returns, win rate, drawdown, or trade-count figures. Recorded as an explicit gap, not filled: this record claims no source-reported performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Same-bar mutual exclusivity is proven, not assumed: `bullish` needs `tenkan > kijun`, `mom > 0`, `close > ss_high`, MACD crossover; `bearish` needs the strict inverse of all four. No bar can satisfy both conjunctions, so the two entries never co-fire and no call-order priority is required. Boundary ties (`tenkan == kijun`, `mom == 0`, `close` inside the cloud, MACD touching without crossing) fire nothing on either side — ties hold, they never invent an order.
2. Dead-close determinism: at pinned defaults both `strategy.close` legs evaluate `... and not true` = false on every bar, so reversal is the only state transition; with no open position an entry leg opens exactly one side, never both.
3. Flat-book determinism: before the first conjunction the book is flat by construction; the date floor keeps pre-2022-06-01 bars flat by explicit source rule.
4. The floor and defaults are pinned, not removed: moving the 2022-06-01 floor, retuning any lookback, disabling a side, or adding a stop/target/cooldown would each be a different, unpinned rule — none is admitted here.
5. Display-code isolation: all `plot`/`fill` lines and the `showDate`/`macd_histogram` write-only values never enter any order condition, so display toggling cannot alter any admitted event.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: Tenkan 9 / Kijun 26 / Senkou-B 52 / 26-bar Chikou and cloud displacement / MACD 12-26-9 on close / four-leg AND per side / reversal-only exits / two-sided / `1h` ETHUSDT / same-bar-close fills are frozen.

- F1 — MACD-trigger relevance: entries on the three Ichimoku legs alone (MACD cross legs removed, first qualifying bar per regime takes the trade) must not improve net expectancy; fail ⇒ the trigger is decorative and the system is a pure Ichimoku-regime holder.
- F2 — Chikou-leg relevance: entries without the 26-bar momentum-displacement leg must not improve net expectancy; fail ⇒ the displacement check adds nothing over alignment plus cloud position.
- F3 — Cloud-position relevance: entries without the above/below-displaced-cloud leg must not improve net expectancy; fail ⇒ the cloud is decorative and the system is a Tenkan/Kijun-plus-MACD cross system.

## Crypto portability

Pinned to ETHUSDT under the house overlay. The OHLC-derived two-sided logic ports to perps or spot without structural change (spot deployment would need the short side disabled, which is a different, unpinned rule — this record stays two-sided). No funding-dependent leg, no stablecoin-specific assumption, no cross-venue state. Extension to other house-universe assets would be a different, unpinned claim.

## Limitations

- Source-frame transfer: the source lists MATIC 1h, AVA 45m, and BTC 30m; the `1h` ETHUSDT pin is an explicitly labeled research choice for a timeframe-agnostic script, not a source-declared frame — hourly ETH behavior is untested by the source.
- Warmup cost: the displaced Senkou-B leg needs 77 completed bars, so the system is blind for the first 77 bars of any evaluation window and reacts slowly to regime births on hourly bars.
- Sticky-leg persistence: the Ichimoku legs can hold one side for long stretches, so losing regimes are ridden until the full mirror conjunction prints; with the stop code removed by the source itself, there is no adverse excursion guard by construction.
- Reversal-only bookkeeping: every exit opens the opposite side, so the system is always in the market after the first signal — flat states exist only before the first entry and on pre-floor bars.

## Implementation status

- `implementation_status: not-implemented`.
- Normalized rule is fully specified above; no Hummingbot/Qlib/n8n/survivor/Paper/Testnet/Live work has been performed or is authorized by this record.

## Adoption boundary

- `adoption: not-approved`, `approval_scope: research-only`, `status: research-only`.
- This record is semantic normalization only. It is not profitability validation, not a survivor promotion, and not Paper/Testnet/Mainnet authorization. Only `hb_ready_status: PASS` records may enter the current Hummingbot/Qlib performance-research downstream, subject to that workflow's own gates.

## Related Wiki records

None.

## Sources

- Primary: https://www.tradingview.com/script/DtsAIRvK-Ichimoku-Cloud-with-MACD-By-Coinrule/ (Strategy by Coinrule, open-source, Aug 18 2022; page rules, June-2022 scope, pair/timeframe notes, 30%/0.1% accounting notes, stop-removal release note, and zero numeric performance claims all live-verified 2026-10-08; display context BINANCE ETHUSDT 30m).
- Immutable code mirror: https://github.com/hasnocool/tradingview-pine-scripts/blob/69969aeaf271b2f7b5a7632a1bde43069a0cbe26/Ichimoku%20Cloud%20with%20MACD%20(By%20Coinrule).pine (pinned HEAD verified as remote HEAD this run via pristine clone plus `git ls-remote`; blob `da95fe685232d8937f7e9617ad1b0630f971bf98`, 3674 bytes; header and Pine block match the canonical page leg for leg, code governs).
- Pine `strategy()` declaration semantics (first-party reference): https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
- Strategy execution model (broker emulator, `process_orders_on_close`): https://www.tradingview.com/pine-script-docs/concepts/strategies/
