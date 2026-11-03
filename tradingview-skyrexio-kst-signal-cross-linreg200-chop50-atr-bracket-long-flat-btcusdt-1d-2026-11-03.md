---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TradingView Skyrexio KST signal-cross linreg200 chop50 ATR-bracket long-flat on BTCUSDT 1d
created: 2026-11-03
updated: 2026-11-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-06-27
sources:
  - https://www.tradingview.com/script/Pv1GvUVs-KST-Strategy-Skyrexio/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Skyrexio KST signal-cross linreg200 chop50 ATR-bracket long-flat on BTCUSDT 1d

## Provenance

Primary source identity verified end to end (page opened live and Pine read line by line this cycle, 2026-11-03):

- TradingView strategy `KST Strategy [Skyrexio]` by publisher `Skyrexio`, stable URL `https://www.tradingview.com/script/Pv1GvUVs-KST-Strategy-Skyrexio/` (script ID part `Pv1GvUVs`). Browser page title pins `KST Strategy [Skyrexio] by Skyrexio — TradingView`. Page markers confirm `OPEN-SOURCE SCRIPT` with `Skyrexio` authorship and a Jun-27-2025 publication stamp (record `source_as_of` is that stamp, never a fetch date).
- Full Pine source read verbatim this cycle through the page's `Source code` tab (Pine v6 `//@version=6`, ~136 lines, MPL-2.0 `© Skyrexio`). Pinned declaration: `strategy(title = "KST Strategy [Skyrexio]", shorttitle = "KST", overlay = true, pyramiding = 1, calc_on_order_fills = false, calc_on_every_tick = false, default_qty_type = strategy.percent_of_equity, default_qty_value = 60, initial_capital = 10000, currency = currency.NONE, commission_type = strategy.commission.percent, commission_value = 0.1, slippage = 5, use_bar_magnifier = true)` — no `process_orders_on_close` anywhere. Order census over the captured text this cycle: 1 `strategy.entry` (id `entry1`, `strategy.long`), 1 `strategy.close` (id `entry1`, `immediately = true`), 0 `strategy.exit`, 0 `strategy.order`, 0 `strategy.close_all`, 0 `request.*`, 0 `security(`. Entries therefore fill next-bar-open market by Pine default; the single close leg is intrabar (`immediately = true`).
- Pinned inputs (frozen defaults): trading window `2023-01-01T00:00:00` → `2025-05-01T00:00:00`; `ATR Stop Loss 1.5` (1.0–4.0); `ATR Take Profit 3.5` (1.0–7.0); filter MA type `Least Squares MA` (8 options), filter length `200` (30–200); `Enable Choppiness Index Filter = true`, threshold `50.0` (30–70), length `14`; KST ROC lengths `10/15/20/30`, SMA lengths `10/10/10/15`, signal length `9`. ATR length `14` is hard-coded. Bot-integration strings (`sourceUuid`/`secretToken` placeholders) are alert-payload wiring only.
- Licence and rights: this record cites and normalizes the rule (short phrases and definitional recurrence only) and reproduces no extended prose, figures, or performance numbers. The page's `Strategy report` tab was never opened; no author backtest number is adopted anywhere in this record.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the source's KST-cross construction ported to BTCUSDT 1d with fixed sizing and next-open entries plus post-hoc bracket resolution — not a lossless reproduction of the author's chart-tester setup. Researcher-declared adaptations are exactly eight: (1) single-asset BTCUSDT Binance USDT-M perpetual 1d venue (the source ships no venue pin); (2) the absolute tester date window is dropped — entries are eligible on every post-warmup bar (the shipped window ended 2025-05-01, so keeping it would make the derivative vacuous; the window is tester scope, never signal logic — disclosed); (3) fixed 0.01 BTC 1x isolated sizing replacing the author's 60%-of-equity compounding (tester economics, never ported); (4) exits resolved post-hoc by first-touch against completed-bar high/low with the pinned stop-first same-bar rule — the declared conversion of the author's `immediately = true` intrabar close into the admitted latched-bracket resolution class (entries stay source-native next-bar-open market — no conversion there); (5) display/bot drop (plots plus the `sourceUuid`/`secretToken` alert JSON) and no bar magnifier (tester precision device, never strategy logic); (6) filter-MA type pinned to the source default `Least Squares MA` and the chop filter pinned ON (the other seven MA options are dead code under the pin — disclosed, never deleted from the source); (7) structural 300-completed-bar warmup (the source ships none — first fully defined signal needs bars 0..199; the margin absorbs SMA/RMA/SMMA seeding); (8) explicit research cost overlay: 0.05% taker fee per filled side plus modeled funding from realized settlements while open; slippage unmodeled by declaration (the source's 5-tick TV slippage does not port). The KST 1-2-3-4 weighting, all nine lengths, the `close > filter AND close > jaw AND chop` triple gate, the strict cross predicate, the 1.5x/3.5x ATR latch arithmetic, the `opentrades == 0` latch guard, pyramiding 1, long-only book, and bracket-only exits are source-faithful. This record is therefore never evidence that the author's script passes.

Pre-write dedup (2026-11-03): working-tree base is current `main@c062ce1b` (537 root strategy records, READMEs excluded; the README pool-count line still reads 486 — count lag outside this PR's touch boundary, never edited here). Case-insensitive content searches for `Pv1GvUVs`, `Skyrexio`, `Know Sure Thing`, `Summed Rate of Change`, `smaroc` return zero same-source/same-construction hits. Chop-name hits (`chop-zone-dmi-psar`, `bullbyte-wpr14`, `bvlabs-alpha-supertrend`, `thefuturesplaybook-chopflow`, Donchian/FVG/Gann-Hilo/Vidya-CMO records) are all different machines with no KST leg; the Alligator record (`alligator-smma-stack`) is an SMMA stack with no KST cross; ATR-bracket records (Simons/dual-EMA9-21/FMZ-445467/FMZ-434428/MACD-zero-cross-SMA50) carry no KST gate. All 17 open `research/*` PRs enumerated by number/title/branch (#48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708, #725) — none is this script, publisher, or construction. Five-axis distinction: no pool record and no open PR conditions entries on a KST(10/15/20/30, SMA 10/10/10/15, weights 1-2-3-4, signal 9) cross-over gated by linreg-200 level AND SMMA-jaw level AND CHOP(14) < 50, exited only by a latched 1.5x/3.5x ATR bracket with pyramiding 1.

## Economic mechanism

### Source-reported

Four smoothed momentum cycles (10/15/20/30-bar ROC, each SMA-smoothed, weight-emphasized toward slower cycles) summed into one composite; a 9-bar SMA signal line times the turn. The triple gate (long-run regression level, Alligator jaw, sub-50 chop) admits only KST turns that print inside an already-established, non-choppy up-move; the 1.5x-stop/3.5x-target bracket then holds the pullback-capture leg without any oscillator re-read. (Author's framing; never adopted as a crypto claim.)

### Research interpretation

Gated snapback-capture, long-only, daily cadence. Unlike oscillator-cross records there is no cross-and-go: the cross is necessary but never sufficient — the linreg-200 level kills counter-trend turns, the jaw kills sub-trend wiggles, and the chop gate kills range churn, so the signal set is the intersection of four independent conditions. Unlike bracket records with fresh levels every bar, the 1.5x/3.5x box is latched once per position at first-fill values and never trails, re-arms, or tightens; the second pyramiding unit (if any) rides the first unit's box. Unlike reversal records there is no opposite leg at all — a cross-under while holding does nothing; only a box touch or nothing ends the trade. The bet, as derived, is purely that this four-way intersection plus fixed-ratio box ports arithmetically to BTCUSDT daily bars — with the economics of that port fenced off as a limitation, and no tuning inside this record.

## Signal

Exact rule as pinned (daily decision on completed `1d` bars; entries next-bar-open market; exits post-hoc first-touch; long-flat — any other window, grid, sizing, fill, or cost is a different, unpinned rule):

- R1 — Measure grid: completed `1d` bars of BTCUSDT only. Continuous calendar days (weekends included); no session template, no holiday skip.
- R2 — KST composite (source formula, pinned): `ROC(n)[i] = 100·(close[i] − close[i−n]) / close[i−n]`; `smaroc(a,b)[i] = SMA(ROC(a), b)[i]`; `KST[i] = smaroc(10,10)[i] + 2·smaroc(15,10)[i] + 3·smaroc(20,10)[i] + 4·smaroc(30,15)[i]`; `SIG[i] = SMA(KST, 9)[i]`. First fully defined at bar index 52. (Pinned cross predicate: `KST[i−1] ≤ SIG[i−1] AND KST[i] > SIG[i]` — prior-bar equality fires, current-bar equality never fires; the builtin-`crossover` convention, pinned explicitly.)
- R3 — Jaw (source formula, pinned): custom `smma(src,13)` seeded with `SMA(src,13)` on its first definable bar then Wilder recursion `(prev·12 + src)/13`; `jaw[i] = smma(hl2, 13)[i−8]`. First fully defined at bar index 20. Teeth/lips are computed in the source but never read — dead code under the pin (disclosed).
- R4 — Chop gate (source formula, pinned): `CI[i] = 100·log10(sum(TR,14)[i] / (highest(high,14)[i] − lowest(low,14)[i])) / log10(14)` with `TR` the Wilder true range; gate `CI[i] < 50.0` (chop filter pinned ON — adaptation 6). Zero-range stretches (`highest == lowest`) print na and hold — explicit holds, not missing rules.
- R5 — Trend filter (source default, pinned): `filter[i] = linreg(close, 200, 0)[i]` (OLS fitted value at the current bar over the trailing 200 closes). First fully defined at bar index 199.
- R6 — Entry gate (strict conjunction, pinned): flat-or-one-unit book and `cross[i] AND close[i] > filter[i] AND close[i] > jaw[i] AND CI[i] < 50` → market long entry effective at the next bar's open. Equality on any leg holds (never fires). A second qualifying bar while holding one unit adds the second and final unit at its next open (pyramiding 1 pinned, never a third); a qualifying bar at the two-unit cap is an explicit no-op.
- R7 — Bracket latch (pinned arithmetic, source-faithful): when a signal bar `s` fires while flat, `SL = low[s] − 1.5·ATR14[s]`, `TP = close[s] + 3.5·ATR14[s]` (ATR14 is Wilder-RMA ATR, SMA-seeded). The latch runs only under the source's `opentrades == 0` guard — a pyramiding add never moves the box. Levels never trail after arming.
- R8 — Bracket resolution (declared post-hoc conversion, adaptation 4): the armed pair is eligible from bar `s+1` onward (orders created at the signal close cannot fill on the signal bar itself — pinned). Each held bar resolves the latched box first-touch against the bar's `H/L` with the stop-first same-bar rule (both touched → the SL price wins — explicit researcher pin in the admitted bracket class). Fills print at touch prices before fees. The entry bar itself (`s+1`, filled at its open) is resolution-eligible. After a full close the stale latched levels persist as inert numbers — an exit evaluation while flat is an explicit no-op, never a trade.
- R9 — Risk legs (pinned absences, not invented): no take-profit beyond the 3.5x box, no trailing, no time exit, no opposite-gate exit, no cooldown — explicitly none, matching the shipped code (zero `strategy.exit`). `closeTradeCondition` (lagged-level probe) is computed but never read — dead code (disclosed).
- R10 — Position state: at most two 0.01-BTC units, long side only; the single `strategy.close("entry1")` leg always closes the whole `entry1` book (full flat, no partials). After any bracket exit the next qualifying bar may re-enter on schedule with freshly latched levels (re-entry explicitly allowed; no cooldown — explicitly none, not invented).
- R11 — Warmup and gaps: flat until 300 completed `1d` bars (structural need is bars 0..199 — the linreg-200 leg dominates KST 52 / jaw 20 / chop 13 / ATR 13; the 101-bar margin absorbs SMA/RMA/SMMA seeding per the admitted precedent chain). Missing-bar stretches freeze evaluation at the prior target — never backfilled, never forced flat.
- R12 — Invariant identifier: `TV:skyrexio-Pv1GvUVs|KST10152030_SMA10101015_sig9_linreg200_chop14lt50_ATR1.5x3.5x_pyr1|longOnly|independent-derived-v1|BinanceFutures:BTC-USDT:1d|LONG-FLAT|nextopen-MARKET+bracket-posthoc-stopfirst|fee0.0005|lev1x|size0.01|warmup300|2026-11-03` (any constant, window, direction, sizing, fill, or cost change is a different derivative).

## Required data

- Completed `1d` bars of BTCUSDT only: `open` (entry fills), `high`/`low` (jaw via hl2, ATR/CHOP/bracket touches), `close` (KST, filter, TP arithmetic, cross predicate). No volume (the pinned filter is Least-Squares; the VWMA option is dead under adaptation 6), no funding/OI/mark-index read gates on any order, no sentiment/macro/on-chain/cross-venue state.
- Single decision grid: one signal evaluation per completed daily-bar close; entries land at the next bar's open; bracket touches resolve post-hoc against completed-bar extremes. No provisional intrabar value is ever used.
- Warmup: flat until 300 completed bars (structural). No repainting, no negative shift, no future reference, no full-sample normalization (every leg is a trailing statistic; boundaries are constants). The `[8]` jaw offset reads a past-confirmed SMMA value — point-in-time clean.

## Execution assumptions

- Research market: BTCUSDT Binance USDT-M perpetual, 1x isolated, fixed 0.01 BTC per unit, at most two units, no compounding. The short side is explicitly disabled (the source has no short leg under any input combination — the sole entry is `strategy.long`). 1x posture: no liquidation path exists inside a −100% move short of total loss; no margin-call/forced-close event can pre-empt the bracket (disclosed). Fills are never conditional on equity, funding, or buying power.
- Order timing (entries source-native, exits declared post-hoc): signal-bar-close decision; entries fill at the next bar's open market (Pine default under no `process_orders_on_close` — no conversion); the latched 1.5x/3.5x box resolves first-touch post-hoc with the stop-first pin — the same resolution class admitted records in `main` use for ATR brackets. No maker-touch, queue, or intrabar-path-dependent fill is claimed. The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Sizing/capital/costs (all fixed this cycle): fixed 0.01 BTC per unit (≈770.3 USDT at the cycle's last close 77,028.8 — above the cycle-verified Binance USDT-M BTCUSDT `MIN_NOTIONAL 50`, `LOT_SIZE minQty/stepSize 0.001/0.001`, `MARKET_LOT_SIZE minQty 0.001`, `PRICE_FILTER tickSize 0.10`; 0.01 is an exact multiple of the step). Explicit research cost overlay: 0.05% taker fee per filled side; modeled funding = sum of realized BTCUSDT-perp settlements (00:00/08:00/16:00 UTC, realized period rate on full notional, sign as settled) while a position is open — a defined, reproducible research model, never hypothetical zero funding and never realized/canonical funding; slippage unmodeled by declaration (the source's 5-tick TV slippage does not port). Any run missing settlement inputs is void, never zero-filled.
- Concurrency: at most one two-unit long book (`pyramiding = 1` pinned — source-faithful, never simplified to single-unit); re-entry after a bracket exit is explicitly allowed on the next qualifying bar with fresh levels; no cooldown — explicitly none, not invented. Single engine position; no shared portfolio state, no multi-pair logic. Safety orders: explicitly none.
- Pinned-engine path (re-verified against local checkout `2dbc844` this cycle, `VERSION=2.17.0`; remote `origin` is `HCH725/hummingbot`, and pinned source `8b0e067e80ab62f10846d518dcb5a8218527ddb3` verified an ancestor of this checkout via `merge-base --is-ancestor`): `data_feed/candles_feed/binance_perpetual_candles/constants.py:24` maps `1d → 86400`; `strategy_v2/backtesting/backtesting_engine_base.py` iterates completed rows and calls `controller.determine_executor_actions()` (`strategy/strategy_v2_base.py`-family `controller_base.py:465`, verified ×2 occurrences this cycle) feeding completed-row windows into `simulate_executor`; `strategy_v2/backtesting/executors_simulator/order_executor_simulator.py:22-30` fills MARKET at the first window row's `close`. Hence a completed-bar-`s` decision fills at the next row's open in the next-open lane — the coded timing. The KST/jaw/chop/linreg arithmetic, the `opentrades == 0` latch, the two-unit cap, and the flat/add/close branches are deterministic controller logic over completed klines; no external feed is required. A strategy-specific, not-yet-implemented `DirectionalTradingControllerBase` child must compute exactly R2–R10; the generic executor does not calculate the strategy. Admitted ATR-bracket lane precedent in `main` (Simons/dual-EMA9-21/FMZ-445467/FMZ-434428/MACD-zero-cross-SMA50 records) shows latched-box post-hoc resolution with the stop-first pin on this engine class; sibling PASS records are path evidence only, never proof of this candidate.

## Evidence

### Source-reported

The script page and header ship every adopted headline fact quoted in Provenance: the KST/Alligator/MA/ATR/Choppiness construction, the MPL-2.0 licence, the 60%-equity sizing, the 0.1% commission, the 5-tick slippage, the bar magnifier, next-bar-open fills, pyramiding 1, the 2023-01-01→2025-05-01 window, and all nine indicator lengths. It ships zero adopted performance numbers for this record: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from the page, header, or reference engine is adopted anywhere — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

No strategy backtest, event-level Qlib/Hummingbot parity, code execution comparison, live order, testnet/paper trade, wheel rehash, deployment, or profitability experiment occurred. Pinned engine file inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifacts this run are researcher self-checks of the Pine-faithful signal/latch/bracket pipeline (ROC/SMA chain, SMA-seeded custom SMMA, Wilder-RMA ATR14, CHOP14, OLS linreg-200, strict cross predicate, triple gate, `opentrades == 0` latch, two-unit cap, stop-first post-hoc resolution, 300-bar warmup), run in scratch (never committed):

- Synthetic drift tape (seeded, 700 bars): first-defined indices KST 44 / SIG 52 / jaw 20 / CI 13 / linreg-filter 199 / ATR 13 — matching the structural analysis exactly; 2 post-warmup signals (first at bar 252) driving 1 OPEN / 1 SL-touch close, ending FLAT (digest `94ceefddcda5`); two independent runs identical.
- Live microstructure (Binance futures 1d klines fetched live this cycle, 1000 completed bars, verified contiguous at 86400s steps, last close 77,028.8): 7 post-warmup-capable signals driving 5 OPENs / 2 TP-touches / 3 SL-touches (0 cap-skips), ending FLAT (digest `9d7a0fbc7bf0`); two independent runs identical. Signal bars are predicate prints, never trade counts. 0.01 BTC ≈ 770.3 USDT notional at window close.
- Logic checks are verification of the coded rule chain only — not a backtest, not parity, not profitability.

### Negative evidence

1. Fill-conversion fenced: derived bracket exits resolve post-hoc against completed-bar extremes while the author's tester fills intrabar with bar-magnifier precision — touch-bar timing and touch-vs-gap economics differ on every exit by construction. This is the coded trade, disclosed, not a tunable parameter here.
2. Window-drop fenced: the source's 2023-01-01→2025-05-01 eligibility window is removed, not re-denominated — the derivative trades any post-warmup regime while the author's tester never does. The signal set is its own object, never the author's tester output.
3. Sizing-removal fenced: the source's 60%-of-equity compounding is replaced by fixed 0.01 BTC — multi-unit and multi-trade equity paths diverge from the author's tester by construction. No equity curve is claimed here for exactly this reason.
4. Number silence fenced: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from the script page, header, or reference engine is adopted anywhere, and any dispute over exact magnitudes is decided against this record, never patched by inference.
5. Derivation boundary fenced: the only non-author behavior is the eight declared adaptations (venue, window drop, fixed sizing, post-hoc bracket resolution, display/bot/magnifier drop, default pins, 300-bar warmup, cost overlay); the KST weights, all nine lengths, the triple gate, the strict cross predicate, the 1.5x/3.5x latch arithmetic, the `opentrades == 0` guard, pyramiding 1, the long-only book, and the bracket-only exit stance are source-faithful. This record is therefore never evidence that the author's script passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: KST `10/15/20/30 + SMA 10/10/10/15 + sig 9` / linreg `200` / chop `14 < 50` / jaw `SMMA(hl2,13)[8]` / `1.5x/3.5x` ATR14 / strict cross / long-flat / pyramiding 1 / next-open entries / post-hoc stop-first bracket / fixed 0.01 BTC 1x / BTCUSDT `1d` / 300-bar warmup are frozen.

- F1 — Chop relevance: a chop-blind twin (gate removed, same grid/entries/bracket/fills) must not improve net expectancy; fail ⇒ the sub-50 chop filter adds nothing over the KST+level intersection.
- F2 — Filter relevance: a filter-blind twin (linreg-200 leg removed, same rest) must not improve net expectancy; fail ⇒ the 200-bar regression level is fee-burning decoration.
- F3 — Bracket relevance: a width twin (1.0x stop / 2.0x target, same entries/fills) must not improve net expectancy by more than the pinned box's declared tolerance; fail ⇒ the author's 1.5x/3.5x ratio destroys more expectancy than its source authority justifies.
- F4 — Oscillator relevance: a cross-blind twin (enter on the triple gate alone whenever flat, same bracket/fills) must not improve net expectancy; fail ⇒ the KST cross is decoration on three level filters.
- F5 — Pyramiding relevance: a single-unit twin (cap 1, same rest) must not improve net expectancy; fail ⇒ the second unit buys nothing but fee drag.

## Crypto portability

Pinned to BTCUSDT Binance USDT-M perpetual (decision grid completed `1d` bar closes; entries at next opens; bracket touches resolved post-hoc; no venue-specific read). The arithmetic ports across perpetual venues without structural change (no corporate-action or calendar adjustment exists to recheck; weekends trade continuously — no equity-calendar port artifact). Extension to other house-universe assets, timeframes, windows, levels, coefficients, grids, or unit counts would be a different, unpinned claim.

## Limitations

- Single-asset port: the author's evidence is chart-tester context on the author's own symbols; BTCUSDT 1d gated-cross behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Conversion lag: post-hoc bracket resolution deviates from the author's intrabar magnifier fills on every exit — the derived event set is its own object, never the author's tester output.
- Window removal: dropping the absolute tester window exposes the derivative to regimes the author never ran — pinned artifact of keeping the strategy executable, not a market claim.
- Seeding: Pine SMA/RMA/SMMA seeding transients are absorbed by the 300-bar warmup; an implementation using a different seed must still hold pre-warmup bars flat — flagged as an implementation obligation, not strategy behavior.
- Crossover equality: prior-bar equality fires the cross by explicit pin (builtin convention); an implementation using strict prior inequality would print a different event set — flagged, never silently interchangeable.
- Stale-level holds: post-close retained SL/TP numbers are inert while flat; zero-range chop stretches hold by construction — fenced, never traded around.

## Implementation status

Not implemented. No Hummingbot controller, Qlib recipe, or backtest artifact exists for this record; `hb_ready_status: PASS` admits it to model-consistent research only.

## Adoption boundary

Research-only. Not approved for Paper, Testnet, or Live trading. Any execution requires a separate downstream authorization plus the `IMPLEMENTATION_NEEDED` materialization route; this record carries no executable recipe.

## Related Wiki records

None.

## Sources

- TradingView OPEN-SOURCE STRATEGY by Skyrexio (script ID `Pv1GvUVs`), page opened and Pine read live 2026-11-03: https://www.tradingview.com/script/Pv1GvUVs-KST-Strategy-Skyrexio/
- Exchange verification (fetched live 2026-11-03): Binance futures `fapi/v1/exchangeInfo` (BTCUSDT `PERPETUAL`, `tickSize 0.10`, `LOT_SIZE minQty/stepSize 0.001/0.001`, `MARKET_LOT_SIZE minQty 0.001`, `MIN_NOTIONAL 50`) plus `fapi/v1/klines` 1d microstructure probes (1000 completed contiguous bars, last close 77,028.8; 7 signals → 5 opens / 2 TP / 3 SL, plant digest `94ceefddcda5`, live digest `9d7a0fbc7bf0`)
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 (verified ancestor of local checkout `2dbc844`, `VERSION=2.17.0`, this cycle)
- Prior independently merged pinned package/source evidence: https://github.com/HCH725/alpha-strategy-research/pull/414 (path evidence only, never proof of this candidate)
- Same-lane siblings (resolution-class evidence only, different mechanisms): Simons / dual-EMA9/21 / FMZ-445467 / FMZ-434428 / MACD-zero-cross-SMA50 ATR-bracket records on `main`
- Pine reference: `ta.roc` / `ta.sma` / `ta.rma` / `ta.atr` / `ta.crossover` / `ta.linreg` / `ta.highest` / `ta.lowest` causal semantics (v6); code-governs over prose throughout
