---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TD Sequential setup-9 perfected exhaustion long with fixed stop on BTCUSDT 1h bars
created: 2026-10-12
updated: 2026-10-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/29209cbf9c2428cdb64cc5b946c8e28c14537ef8/user_data/strategies/berlinguyinca/TDSequentialStrategy.py
  - https://hackernoon.com/how-to-buy-sell-cryptocurrency-with-number-indicator-td-sequential-5af46f0ebce1
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TD Sequential setup-9 perfected exhaustion long with fixed stop on BTCUSDT 1h bars

## Provenance

Primary source read end to end (raw file fetched live over HTTPS three times this cycle — floating `master`, pinned commit, and a re-fetch — all byte-identical, 6,711 bytes, 151 lines, SHA-256 `c146c1fa3d5d8ad5f87dd32f921d036a0a5ca95acc3109afdbf4689faf44e5b5`):

- Repository: https://github.com/freqtrade/freqtrade-strategies (`master` default branch; community strategy collection for the open-source Freqtrade crypto bot; each file is an executable strategy class with entry/exit columns, risk attributes, and engine settings).
- Immutable pin: commit `29209cbf9c2428cdb64cc5b946c8e28c14537ef8` (2026-09-08T08:15:10Z; latest commit touching this file, a docstring/comment-only correction — the signal logic is untouched by it), path `user_data/strategies/berlinguyinca/TDSequentialStrategy.py` (151 lines, `INTERFACE_VERSION = 3`, class `TDSequentialStrategy(IStrategy)`, credited in-docstring to `@bmoulkaf`). Adopted `source_as_of` 2026-09-08 is that commit's date, disclosed here, never an authorship date. The pinned bytes are byte-identical to the floating-`master` raw fetch this run, so no newer file revision exists to diverge from.
- Rule lineage stated in the file's own docstring: `source: https://hackernoon.com/how-to-buy-sell-cryptocurrency-with-number-indicator-td-sequential-5af46f0ebce1` with `Buy trigger: When you see 9 consecutive closes "lower" than the close 4 bars prior. An ideal buy is when the low of bars 6 and 7 in the count are exceeded by the low of bars 8 or 9` and the mirrored sell trigger. The article page was re-fetched live this run (129,662 bytes HTML) and states the same rule verbatim (`a series of nine candles where each close higher/lower than its 4th predecessor candle's close value`; `An ideal buy is when the low of bars 6 and 7 in the count are exceeded by the low of bars 8 or 9`; perfection discussion). The article is rule exposition only — it carries no traceable performance table, so no performance figure of any kind is kept from it.
- Text census over the pinned 151-line file: 3 `populate_*` methods (`populate_indicators` / `populate_entry_trend` / `populate_exit_trend`) plus 1 `informative_pairs` returning `[]` (no second pair, no second timeframe — single-frame by construction) / 2 `enter_long` tokens (zero-init plus one set-to-1 leg) / 2 `exit_long` tokens (zero-init plus one set-to-1 leg) / 0 `enter_short` / 0 `exit_short` (long-only is the coded posture, never an omission) / 2 `.shift(4)` (the two close-vs-close-4 comparisons) plus 2 `.shift()` (the two run-length group keys, non-negative) / 0 negative shifts / 0 `.iloc[-1]` / 0 `.mean()`-over-frame / 0 `.resample` / 0 `.merge` / 0 `volume` reads / 0 `open` reads (signal path reads `close`, `low`, `high` only) / 0 `position_adjustment` / 0 `adjust_trade_position` / 0 `custom_stoploss` / 0 `custom_exit` / 0 `leverage` / 0 `trading_mode` / 0 `can_short` (spot long-only engine default governs) / 3 signal-path imports present-but-dead (`talib.abstract as ta`, `scipy.signal`, `qtpylib` — zero `ta.`/`scipy.`/`qtpylib.` call sites anywhere, so the signal path is pure pandas run-counting plus low/high comparisons, never a library indicator).
- Frozen engine attributes (any other value is a different, unpinned rule): `timeframe = '1h'` / `startup_candle_count = 30` / `stoploss = -0.05` (fixed 5% stop) / `minimal_roi = {'0': 5}` (a +500% profit target — coded but economically inert, fenced below) / `trailing_stop = False` / `use_exit_signal = True` / `exit_profit_only = False` (signal exits fire even at a loss) / `ignore_roi_if_entry_signal = False` / `order_types = {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False}` / `order_time_in_force = {'entry': 'gtc', 'exit': 'gtc'}`. No fee, funding, slippage, or capital assumption ships in the file — Freqtrade applies the exchange default fee at runtime (project-documented behavior, `bot-basics`: `For Backtesting / Hyperopt / Dry-run modes, the exchange default fee is used`), so the absences here are disclosed, never read as zero cost.
- Freqtrade project documentation verified live this run from the pinned project's own docs tree: `process_only_new_candles` defaults `true` (completed-candle evaluation governs unless the strategy overrides — this file does not); `stoploss`/`minimal_roi` are strategy-overridable risk attributes (this file overrides both); on colliding signals `freqtrade will do nothing and ignore the entry signal` (`enter_long` colliding with `exit_long`/`enter_short` — quoted from `strategy-customization`; the mutual-exclusion proof below shows this file never collides, so the rule is a backstop, never a live path).

Licence and rights: the repository is open-source (MIT-licensed community collection); this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source backtest. Researcher-declared adaptations are exactly four: (1) market pin `BTCUSDT` on Binance (the source is pair-agnostic — Freqtrade whitelist-driven, no symbol anywhere in the file); (2) same-bar-close fills on completed-bar decisions (the source trades `limit` GTC orders filled on later candles; this record freezes completed-bar evaluation with same-bar-close execution and scopes live/limit-order behavior out, see Limitations); (3) an adopted 50-bar warmup with pre-warmup bars flat by record rule (covers the source `startup_candle_count = 30` plus run-count/indexing margin; see Required data); (4) house sizing/capital/costs replacing the absent source economics (see Execution assumptions). The `1h` frame, the close-vs-close-4 run counting, the bar-6/7-vs-8/9 perfection legs, the `seq > 8` gates, the long-only posture, the signal-exit pair, the fixed 5% stop, the inert 500% ROI target, the disabled trailing, and the exit-even-at-loss setting are source-native and unmodified.

Pre-write dedup (2026-10-12): working-tree case-insensitive searches for `sequential`, `seq_buy`, `close[4]`, and `demark` return zero pool records using this source file, run-count construction, or methodology — the single `demarker` token in the tree is a prose mention inside the mass-index record's own dedup paragraph (a different Donald-Dorsey range-expansion latch that reads no close and counts nothing). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources; no open, merged, or closed PR touches TD Sequential, DeMark counting, or this file. A same-night FMZ-sourced TD S/R-plus-MA two-sided draft exists only as local scratch (never a PR, never merged) and is a different source with a different mechanism (support/resistance levels plus MA filter/stop, two-sided) — no part of it is adopted here. Closest pool records are different mechanism classes: `three-down-three-up-consec-close-long` (consecutive-close runs, but direction-continuation with no 4-bar offset, no perfection leg, no exhaustion logic); `connors-rsi2-ma70-fade` / `double-seven-connors-pullback-long` (Connors pullback family — RSI/streak-based, never close-vs-close-4 counting); `dmi-swings-contrarian-adx` (exhaustion philosophy, but DI-level persistence, never sequential counting). Five-axis distinction: source identity differs (freqtrade-strategies immutable commit plus `berlinguyinca/TDSequentialStrategy.py` path), mechanism differs (nine-bar close-vs-close-4 sequential exhaustion with bar-6/7-vs-8/9 perfection, long-only), signal construction differs (no pool record computes run-length counts against a 4-bar-offset close), exits differ (asymmetric signal exit plus fixed 5% stop plus inert 500% ROI target), and data differs (close/low/high only; no volume, open, or multi-frame read).

## Economic mechanism

### Source-reported

Sequential-exhaustion reversal (code docstring plus referenced article): a buy setup is nine consecutive closes below the close four bars earlier — sustained one-sided pressure measured against its own offset echo — and the *ideal* (perfected) buy requires the lows of count-bars 8 or 9 to undercut the lows of count-bars 6 or 7, i.e. the decline must still be making lower lows into the ninth bar. The strategy buys only the perfected setup and exits on the mirror sell-side print (sell-setup count past 8, or sell-side perfection) — with a fixed 5% stop as the only price-based guardrail and an exit signal that fires even at a loss. There is deliberately no short leg, no trailing, no profit-taking leg (the 500% ROI target is coded but unreachable in practice), and no flat state beyond pre-signal bars.

### Research interpretation

Perfected-exhaustion long — the pool's first sequential-counting record and its first Freqtrade-sourced record. Unlike the pool's consecutive-close records, the comparison is not bar-to-bar but bar-to-4-bars-ago, so the count measures persistence against an offset echo rather than a streak: alternating chops reset both counts, while a grinding decline that keeps printing below its own 4-bar-ago prints accumulates. Unlike the pool's Connors pullbacks, there is no oscillator, no moving average, and no streak-of-lows leg — the entire signal is three raw price columns. Two asymmetries are stated plainly. First, entry is stricter than exit: longs require count ≥ 9 *and* perfection, while the exit fires on an unperfected sell count ≥ 9 *or* sell-side perfection alone (even at count 8) — the system is quicker to leave than to enter. Second, the 5% stop can cut a perfected setup that would have resolved favorably, while a setup that never reaches −5% but never reverses is held until the sell-side print, however long that takes — no time exit exists. The bet is on offset-echo exhaustion resolving upward at frozen setup-9/perfection geometry on `1h` BTCUSDT, not on oscillators, bands, volume prints, calendar effects, or any second timeframe.

## Signal

Exact rule as pinned (any other threshold, offset, or perfection definition is a different, unpinned rule):

- Construction (pinned arithmetic — run-length counts on completed bars, evaluated oldest-to-newest): `seq_buy_raw = close < close.shift(4)`; `seq_buy` = consecutive-True run length of `seq_buy_raw` (1-based within each run; equality `close == close[4]` is False and resets both counts — coded, never a researcher tie-break); `seq_sell_raw = close > close.shift(4)`; `seq_sell` = consecutive-True run length of `seq_sell_raw`. Perfection flags on bar `t` with count `c`: buy-side, if `c == 8`: `exceed_low = (low[t] < low[t-2]) or (low[t] < low[t-1])`; if `c > 8`: `exceed_low = (low[t] < low[t-3-(c-9)]) or (low[t] < low[t-2-(c-9)])`, and additionally at `c == 9` the bar-8 flag persists (`exceed_low[t] |= exceed_low[t-1]`). Sell-side mirrored on `high` into `exceed_high`. Both flags default False every bar and are set only under the stated count conditions.
- Entry long: `enter_long = exceed_low and (seq_buy > 8)` — i.e. count ≥ 9 with perfection on the entry bar. Fires on completed bars with same-bar-close execution under the derived declaration.
- Exits (coded, the complete position-closing set): signal exit `exit_long = exceed_high or (seq_sell > 8)` (sell-side perfection alone, even at count 8, or any sell count ≥ 9 — asymmetric with entry by code, disclosed); fixed stop −5% from entry (`stoploss = -0.05`); ROI target +500% (`minimal_roi = {'0': 5}` — coded but economically inert, disclosed as inert, never as a live profit-taking leg); trailing explicitly `False`; signal exits honored even at a loss (`exit_profit_only = False`); ROI/entry-signal interaction unblocked (`ignore_roi_if_entry_signal = False`, moot given the inert target).
- Direction: long-only. Zero `enter_short`/`exit_short` tokens ship anywhere — no short state exists to gate or exit, disclosed, not enabled.
- Seed bars: comparisons against unavailable history are False, counts start at 0, both perfection flags stay False — no leg can print before real history accumulates, and the adopted warmup below holds the record flat well past seeding anyway.

## Required data

- Completed `1h` bars of BTCUSDT: `close` (both 4-bar-offset comparisons and both run counts), `low` (buy-side perfection), `high` (sell-side perfection). No `open`, no volume, no funding/OI/mark-price, no order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any signal line — census-verified.
- Single decision timeframe `1h` (source-native `timeframe = '1h'`; `informative_pairs` returns `[]`, so the file is single-frame by construction).
- Warmup: the source requires `startup_candle_count = 30` valid candles before signalling. The adopted warmup is the first 50 completed `1h` bars flat by record rule (predeclared researcher choice — source 30 plus margin covering run counts into the mid-40s and the perfection index-back reach). References for still-longer runs always read real completed bars (causal, merely older than the formal warmup), disclosed. No negative shift, no future reference, no full-sample normalization; one evaluation per completed bar (`process_only_new_candles` defaults true and the file does not override it). Each bar's print enters the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT on Binance, long side only (the source is pair-agnostic and venue-agnostic — no symbol, no venue, no `trading_mode`, no `can_short` anywhere, so the market/venue pin is a researcher choice, disclosed, never presented as source-native; the `1h` frame is source-native and unmodified).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source trades `limit` GTC orders filled on later candles with `stoploss_on_exchange = False`; this record does not claim that source behavior. No maker-touch, queue, or intrabar-path-dependent fill: the only price-contingent leg beyond the close is the fixed 5% stop, evaluated bar-to-bar without intrabar sequencing claims (see Limitations). Entry and signal-exit can never co-print (proven: entry needs `seq_buy > 8`, which forces current `close < close[4]`, which forces `seq_sell == 0` and `exceed_high == False` since `exceed_high` is set only under `seq_s >= 8`; the mirror holds for exits) — at most one net position change per bar, and the project-documented collide rule (entry ignored on collision) is a backstop that never activates, disclosed.
- Engine path for `1h` (gate 5, stated plainly): `1h` is a Binance-documented spot and USDT-M kline interval; the derived rule needs only completed `1h` candles on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no funding/OI/mark-price leg, no cross-sectional state. That is the same single-frame completed-bar path as the admitted `1h`/`30m`/`15m`/`2h`/`4h`/`1d` records (the `1h/4h/1d` whitelist stands removed as an independent ban, and no ban is reinstated here by another name). Fixed-percentage stops of this form already model inside admitted records (fixed-RR and ATR stop-target precedents), and the stop here needs no intrabar extreme — bar-close sequencing only. Anything beyond that single-frame completed-bar path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: the file ships no sizing, no capital, and no fee/slippage/funding/margin assumption beyond the exchange-default-fee runtime behavior documented by the project (quoted in Provenance; the absences are disclosed, never read as zero cost) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: the file defines no averaging/pyramiding hook (`position_adjustment`/`adjust_trade_position` absent — census-verified), so one open position per pair under stock engine semantics; same-direction refires while positioned cannot open a second position, opposite legs do not exist, and re-placement is allowed on the next qualifying bar after any exit (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (close-vs-close-4 run counts, bar-6/7-vs-8/9 perfection legs with the count-9 persistence term, `seq > 8` gates, `enter_long = exceed_low-and-count≥9`, `exit_long = exceed_high-or-sell-count≥9`), the long-only posture (zero short columns), the complete risk attribute set (`stoploss = -0.05`, `minimal_roi = {'0': 5}`, `trailing_stop = False`, `use_exit_signal = True`, `exit_profit_only = False`), and the engine settings (`timeframe = '1h'`, `startup_candle_count = 30`, limit/GTC order types, empty informative pairs). The referenced article restates the setup-9/perfection rule verbatim. Neither the code nor the article carries a traceable performance table, and this record keeps strictly zero performance figures — source-reported or otherwise. This record claims no reproduced performance of any kind.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden legs: 0 `enter_short`, 0 `exit_short`, 0 `position_adjustment`, 0 `custom_stoploss`, 0 `custom_exit`, 0 `leverage`, 0 `trading_mode` — the position-closing set is exactly the signal exit plus the fixed 5% stop plus the inert 500% ROI target. The absence of a profit-taking leg is coded (the ROI target is set five-fold above any plausible single-trade move), disclosed as inert rather than deleted.
2. No countdown, no TDST, no recycling: DeMark's 10–13 countdown phase, TDST support/resistance, setup recycling, and related machinery appear nowhere in the 151-line file — this implementation is Setup-9 plus perfection only, and importing any of that machinery would be a different, unpinned rule.
3. Perfection gate fenced: a count-9 buy setup whose lows never undercut count-bars 6/7 prints nothing — relaxing entry to unperfected counts would be a different, unpinned rule.
4. Exit asymmetry fenced: the signal exit fires on sell-side perfection at count 8 or any sell count ≥ 9, with no perfection requirement on the count leg — symmetrizing entry and exit (perfected-only both sides, or count-only both sides) would be a different, unpinned rule.
5. No future leakage in the stack, stated plainly: at decision bar `t`, both 4-bar-offset comparisons, both run counts, and both perfection legs read completed-bar prints through `t` with non-negative offsets only (`.shift(4)`/`.shift()` plus label indexing at `t-1`, `t-2`, `t-3-(c-9)` — all strictly backward on the ordered RangeIndex). No negative shift, no `.iloc[-1]`, no frame-wide normalization, no second timeframe, no `open`/`volume` read; seed bars degrade to False/0-hold, never to a forward read. The project's own lookahead guidance (no negative shifts, no absolute positions, no full-frame statistics) is satisfied line by line.
6. Same-bar determinism fenced: entry and signal-exit are provably mutually exclusive on every bar (proof in Execution assumptions); the documented engine collide rule therefore never activates. At most one net position change per bar.
7. Long-only posture provably complete: both signal columns that exist are long-side (`enter_long`, `exit_long`); no third direction exists. No flat state is coded after the first signal — always-in-market past seeding unless the sell-side print or the 5% stop closes the leg, disclosed.
8. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT market pin, same-bar-close fills (with live/limit-order behavior scoped out), the adopted 50-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the frame, run-count arithmetic, perfection legs, gates, order columns, exits, stop, and risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, timing, input set, or the source's limit-order live behavior passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: close-vs-close-4 run counting / bar-6/7-vs-8/9 perfection / `seq > 8` gates / perfected-only entries / asymmetric signal exits / fixed 5% stop / long-only / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Perfection-gate relevance: entering on any buy count ≥ 9 without the perfection conjunct (same exits otherwise, same stop) must not improve net expectancy; fail ⇒ the coded perfection leg adds nothing over its unperfected twin.
- F2 — Exit-asymmetry relevance: exiting only on the mirror-perfected sell setup (perfected sell print alone, same entries, same stop) must not improve net expectancy; fail ⇒ the coded count-leg/sell-perfection exit adds nothing over its symmetric twin.
- F3 — Stop relevance: removing the fixed 5% stop while keeping entries and signal exits (same fills otherwise) must not improve net expectancy; fail ⇒ the coded stop adds nothing over its unstopped twin.

## Crypto portability

Pinned to BTCUSDT on Binance `1h` under the house overlay (market pin is a researcher choice on a pair-agnostic source; the `1h` frame is source-native). The arithmetic ports across spot and perpetual venues without structural change — it reads completed-bar `close`/`low`/`high` only, so venue volume-definition differences cannot move any leg, disclosed. The rule is long-only with no stop-leg beyond the fixed 5%, so a spot-only deployment expresses it fully and a futures venue expresses the same long side — no short-side approximation is needed or claimed, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read, so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source trades `limit` GTC orders filled on later candles with `stoploss_on_exchange = False`; this record evaluates completed bars only and executes same-bar-close on `1h` BTCUSDT. Backtest economics of the timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance. Any live/limit-order/queue behavior is out of scope.
- Derived market pin: the file names no symbol or venue — BTCUSDT on Binance is a researcher market choice for the house universe, never a source claim.
- The 5% stop is bar-sequenced, not intrabar-sequenced: within a bar that gaps through the stop level, this record claims no intrabar ordering or touch semantics — evaluation follows the declared bar-close convention only, disclosed.
- Inert ROI target: `minimal_roi = {'0': 5}` is kept as coded (a +500% target) and classified inert — treating it as a live profit-taking leg would misread the file, disclosed here.
- Source economics are runtime-default-only: beyond the project-documented exchange-default-fee behavior the file ships no capital sizing, no slippage, no funding, and no margin assumption — derived evaluation must carry the full house cost load (fees plus historical funding; no hypothetical zero funding claimed), and this record reports no net performance of its own. The referenced article carries no performance table, so no figure is kept or transferred.
- No time exit, no trailing, no flat state: a leg whose sell-side print never arrives is held indefinitely (bounded only by the 5% stop); a winning leg keeps running with no profit-taking leg. This is the coded posture, disclosed as the record's principal risk.
- Unperfected setups are untraded: a count-9 buy setup without the bar-6/7-vs-8/9 undercut fires nothing — long flat stretches in grinding-but-not-perfecting declines are the coded posture, disclosed; whipsaw of the sell-side print around count 8/9 can exit and re-enter across consecutive bars, disclosed as the principal friction.
- Seed bars: the 4-bar offset plus run-count seeding dominate early bars; the first 50 `1h` bars are flat by record rule, so early-history signals never enter any evaluation.
- Dead-import quarantine: `talib`/`scipy`/`qtpylib` are imported but never called in the signal path — treating them as signal dependencies would be a different, unpinned rule, disclosed here.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record; the six-gate claim is pinned-engine expressibility of the declared rule, never a profitability, parity, or trading authorization.

## Adoption boundary

Research-only, not approved. No live, Paper, or Testnet authorization follows from this record. Any downstream standardized overlay (house DCA/capital/leverage), Qlib screening, or Hummingbot re-validation is a separate, explicitly authorized step outside this record.

## Related Wiki records

None.

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/29209cbf9c2428cdb64cc5b946c8e28c14537ef8/user_data/strategies/berlinguyinca/TDSequentialStrategy.py (primary source — executable Freqtrade strategy class, 151 lines, fetched live 2026-10-12 at pinned file-touching commit byte-identical to `master`, 6,711 bytes, SHA-256 `c146c1fa…5b5`; `timeframe = '1h'` source-native; rule-exposition article linked in-docstring re-fetched live with verbatim rule match and no performance table)
- https://hackernoon.com/how-to-buy-sell-cryptocurrency-with-number-indicator-td-sequential-5af46f0ebce1 (secondary rule exposition referenced by the primary source — setup-9/perfection rule confirmed verbatim, no traceable performance figures kept)
- https://github.com/freqtrade/freqtrade (engine-semantics reference for project-documented defaults only — `process_only_new_candles` default true, exchange-default-fee runtime behavior, collide-signal entry-ignore rule; never a source of strategy facts)
