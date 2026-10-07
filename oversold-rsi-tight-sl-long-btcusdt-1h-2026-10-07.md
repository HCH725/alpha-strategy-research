---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Oversold-RSI tight-stop mean-reversion long system on BTCUSDT 1h bars
created: 2026-10-07
updated: 2026-10-07
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: high
source_as_of: 2023-12-22
sources:
  - https://www.fmz.com/strategy/436250
  - https://www.fmz.com/strategy/427892
  - https://www.tradingview.com/pine-script-reference/v4/#fun_strategy
  - https://www.tradingview.com/pine-script-reference/v4/#fun_strategy{dot}entry
  - https://www.tradingview.com/pine-script-reference/v4/#fun_strategy{dot}close
  - https://www.tradingview.com/pine-script-reference/v4/#fun_rsi
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The mirror's Strategy Arguments table lists v_input_9 default 'true', but the pinned code declares the stop leg as Stop_loss = ((input (1))/100) and every prose line (Chinese and English) states a 1%-below-entry stop. The code governs: stop distance 1% (0.01), take distance 7% (0.07)."
  - "The FMZ demo backtest header prints period 3m (436250) / 15m (427892), neither in the admission set. The pinned script is timeframe-agnostic (zero request/security/timeframe calls), so the record pins 1h as the explicitly labeled research decision timeframe under the house overlay — nearest admissible standard timeframe preserving the source's short-horizon character, not a source-declared timeframe."
---

# Oversold-RSI tight-stop mean-reversion long system on BTCUSDT 1h bars

## Provenance

Primary source read end to end (FMZ strategy page mirror plus live re-verification):

- FMZ strategy: https://www.fmz.com/strategy/436250 (`反转突破RSI超卖策略Reversal-Breakout-Oversold-RSI-Strategy`, page author ChaoZhang; Pine strategy title `Oversold RSI with tight SL Strategy (by Coinrule)`, `//@version=4`, `// © brodieCoinrule`).
- Last modified (as printed on the page): 2023-12-22 15:00:48.
- FMZ backtest block pinned on the page: `start: 2023-12-14 00:00:00`, `end: 2023-12-18 19:00:00`, `period: 3m`, `basePeriod: 1m`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]` — single pair; the `3m`/`1m` figures are FMZ demo-execution scope only (see decision-timeframe note below), not signal rules.
- Live re-verification (2026-10-07): the FMZ page returns HTTP 200 (790006 bytes); the page title (`反转突破RSI超卖策略 | 发明者量化`), the author (ChaoZhang), the Pine title (`Oversold RSI with tight SL`), `process_orders_on_close`, `rsi(close, lengthRSI)` with `lengthRSI = 14`, the exact entry line (`strategy.entry(id=\"long\", long = true, when = RSI< oversold and window())`), the exact exit line (`strategy.close(\"long\", when = close < longStopPrice or close > longTakeProfit and window())`) with `Stop_loss = ((input (1))/100)` and `Take_profit = ((input (7)/100))`, and the last-modified stamp (2023-12-22) all match the mirror. No live-page fact contradicts the mirror.
- Mirror executable block: one `strategy()` declaration (`shorttitle='Oversold RSI with tight SL'`, `overlay=true`, `process_orders_on_close=true`, no `calc_on_every_tick`, no `pyramiding`, no `max_bars_back`), date-window inputs defaulting to 2020-01-01 → 2112-01-01, `lengthRSI = 14`, `RSI = rsi(close, lengthRSI)`, `oversold = input(30)`, and exactly two live order calls: one `strategy.entry(id="long", long = true, ...)`, one `strategy.close("long", ...)`.
- Censuses over the pinned block: `request.*` 0, `security(` 0, `timeframe` 0, `strategy.exit` 0, `strategy.order` 0, `strategy.close_all` 0, `stop=` 0, `limit=` 0, `crossover` 0, `crossunder` 0, `ta.cross` 0, `strategy.short` 0 live occurrences, `high`/`low`/`open`/`volume` 0 occurrences in trading logic. `perc_change(lkb)` is defined once and called zero times — dead code excluded from the normalized rule as written, not repaired.
- Corroborating duplicate mirror: https://www.fmz.com/strategy/427892 (`超跌RSI追涨策略Oversold-RSI-Breakout-Strategy`, last modified 2023-09-26 16:11:55) carries the byte-identical Pine block (same title, same entry/exit lines, same 1%/7% levels) under a `15m` demo header — confirming the script itself is timeframe-agnostic and the header periods are demo scope, not signal.

Licence and rights: this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

Pre-write dedup (2026-10-07): working-tree searches for `436250`, `427892`, `Oversold RSI with tight SL`, and `tight SL` returned 0 matches. Closed research PRs (#6 WaveTrend, #10 golden/dead cross, #17 MACD histogram, #20 Ichimoku-RSI, plus all merged family records) contain no oversold-RSI fixed-percentage-exit long system. Closest record: `rsi-classic-level-reversal-btcusdt-1h-2026-10-07.md` (FMZ 441161, same Coinrule RSI family, same `RSI(14) < 30` long entry) — but its exit is a signal exit (`RSI > 60`), while this record's exit is fixed ±percentage-from-entry bar-close levels (`-1% / +7%`) with no oscillator exit anywhere: the holding/exit leg is a different mechanism class, so the normalized trade-event sequences differ materially. Five-axis distinction: mechanism differs (oversold entry plus asymmetric fixed-percentage risk exits versus level-reversal signal exits), signal construction differs (avg-price-relative close comparisons, no second RSI threshold), horizon is `1h` BTCUSDT long-only, source identity differs (FMZ 436250 versus 441161; distinct Pine titles), direction handling is long-only by code (`long = true` sole entry, zero short calls). `gh pr list --state open` shows only #36 (reconstruction lane, no `research/*` collision).

## Economic mechanism

### Source-reported

An oversold mean-reversion long: it waits until RSI(14) prints below 30 (prior decline judged exhausted), opens a long, and holds inside a tight asymmetric risk band — a close 1% adverse move stops out, a close 7% favorable move banks profit. Tight stop, wide target: small frequent losses against occasional large wins.

### Research interpretation

Short-horizon snap-back harvesting with inverted risk asymmetry: the `RSI < 30` leg buys only washed-out bars, the `-1%` stop leg refuses to let losers breathe, and the `+7%` take leg demands a full recovery leg before banking. No leverage, sizing, or cost edge is embedded in the signal; the source `percent_of_equity 50%` line is capital configuration replaced event-neutrally by the house overlay (see Execution assumptions).

## Signal

Exact rule as pinned (Pine v4, defaults quoted — inputs unmodified):

- Inputs: `oversold = 30`, stop `(1)/100 = 0.01`, take `(7)/100 = 0.07` (anonymous `input` defvals corroborated by bilingual prose; code governs over the one anomalous arguments-table cell).
- Indicators: `RSI[t] = rsi(close, 14)[t]` (Pine v4 built-in Wilder RMA-based RSI on close, lookback 14).
- Entry (long-only): `entry[t] = (RSI[t] < 30) and window()[t]`, live via `strategy.entry(id="long", long = true, when = entry[t])`. Strict inequality: `RSI == 30` fires nothing — the tie case is defined, not ambiguous. The rule contains 0 `crossover`/`crossunder` calls, so the prior-bar tie-semantics blocker that closed PR #6 cannot arise here.
- Exit levels (fixed per open position): `longStopPrice = avg_entry * 0.99`, `longTakeProfit = avg_entry * 1.07`, where `avg_entry` is `strategy.position_avg_price` (single-position book, so exactly the entry fill price).
- Exit (full close of the one long): `exit[t] = (close[t] < longStopPrice) or ((close[t] > longTakeProfit) and window()[t])` — Pine `and` binds tighter than `or`, preserved exactly as written. With defaults, `window()[t]` is true for every bar from 2020-01-01 to 2112-01-01, so over the entire evaluable crypto history the live condition is exactly `(close[t] < avg_entry * 0.99) or (close[t] > avg_entry * 1.07)`, evaluated once per bar on the close. While flat, `position_avg_price` is `na` and both comparisons are falsy — the exit is inert with no position, deterministically.
- Window asymmetry is provably inert: the stop leg lacks its own `and window()`, but no position can exist outside the window (entries require it), so the unwindowed stop leg can never fire on a real book. No priority choice is required: the entry bar can never self-exit (`na` levels are falsy on the entry bar).
- Re-entry: after an exit the book is flat, so the next bar with `entry[t]` true opens a fresh long. While long, further entry signals are rejected under the default single-position declaration. No cooldown is declared and none is needed: re-entry requires the flat state plus a fresh true evaluation, so cooldown semantics are provably irrelevant rather than missing.
- Opposite-signal exit: not applicable — there is no short side (zero short calls); the long is exited only by the −1%/+7% rule above. No oscillator-based signal exit exists (no `RSI > 60` leg anywhere, unlike FMZ 441161).
- Stop loss / take profit / trailing / time limit as orders: explicitly none (0 `strategy.exit`, 0 `stop=`/`limit=`). The 1%/7% levels are bar-close signal exits, not stop/limit orders: an intrabar pierce of either level exits nothing — the close must confirm beyond the level on a completed bar. No silent Hummingbot defaults are relied upon.

## Required data

- Completed `1h` bars of BTCUSDT: `close` only. `open`, `high`, `low`, `volume` occur 0 times in the trading logic; no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, or cross-venue state is read.
- Single decision timeframe `1h` (explicitly labeled research timeframe under the house overlay; the script is timeframe-agnostic with 0 timeframe references, so no cross-timeframe dependency and no causal alignment is owed). The `window()` date gate uses bar `time`, which is known at the completed-bar decision point — causal, no future reference.
- Warmup: `rsi(close, 14)` seeds over its first 14 bars. First possible signal at bar index 14 (the 15th completed bar). No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT under the house overlay (source venue is Binance USDT-M BTC futures; the system is long-only, so no naked-spot-short construction is required or assumed).
- Order timing: the two live order calls are market entry/close with `process_orders_on_close=true` and no `calc_on_every_tick` (language default false, recorded as source-declared-by-default): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. No next-bar-open, maker-touch, queue, or intrabar-path-dependent fill exists anywhere in the rule.
- Sizing/capital: source `default_qty_type = strategy.percent_of_equity, default_qty_value = 50` and `initial_capital = 1000` are event-neutral capital configuration, replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3×/5×) and never presented as source-native behavior. Source declares `commission_type = strategy.commission.percent, commission_value = 0.1`; the pinned house cost assumptions apply as pure accounting and do not alter signal, timing, direction, or exits.
- Concurrency: at most one open long (single entry id, default single-position declaration); no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The FMZ page and its embedded description carry no numeric performance claims — no ROI, Sharpe, win rate, drawdown, or trade-count figures appear anywhere in the artifact. Recorded as an explicit gap, not filled: this record claims no source-reported performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Entry-bar self-exit is impossible (`position_avg_price` is `na` until the entry-bar close; both exit comparisons are falsy there) — verified by language semantics, not by backtest.
2. Exact-equality bars (`RSI == 30`, `close == stop/take level`) fire neither leg — strict inequalities throughout, so ties are defined.
3. The `and window()` suffixes gate only pre-2020 bars under defaults (all crypto data in evaluable scope passes); they change no in-scope event and are preserved as written, not repaired or removed.
4. `perc_change(lkb)` is defined but never called: any percent-change reading would be a different, unpinned rule.
5. `MASignal`-style prose/code mismatches seen in sibling Coinrule mirrors do not occur here: bilingual prose (1% stop / 7% take) and code (`input (1)` / `input (7)`) agree; only the arguments-table cell is anomalous and the code governs.
6. No oscillator exit exists: a bar printing `RSI > 60` (or any high RSI) while long exits nothing — only the ±% close rule exits.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `RSI(14)`, `RSI < 30` entry, `−1% / +7%` close-evaluated exits, long-only, `1h` BTCUSDT, same-bar-close fills are frozen.

- F1 — Entry relevance: on full-history 1h BTCUSDT, longs opened while `RSI < 30` must show better forward drift than unconditional longs net of the house overlay; fail ⇒ the oversold leg adds nothing.
- F2 — Stop relevance: widening the stop to −3% must not improve net expectancy; fail ⇒ the tight stop is decorative.
- F3 — Take relevance: narrowing the take to +3% must not improve net expectancy; fail ⇒ the wide-target asymmetry is arbitrary.
- F4 — Intrabar discipline: evaluating the same ±% levels on intrabar pierce (stop-order semantics) must produce a materially different trade list; pass ⇒ confirms the record's bar-close-only claim is load-bearing and correctly pinned.

## Crypto portability

Pinned to BTCUSDT (Binance USDT-M lineage) under the house overlay. Long-only logic ports to spot or perps without structural change; no funding-dependent leg, no stablecoin-specific assumption, no cross-venue state.

## Limitations

- Fixed −1%/+7% bands do not adapt to volatility: calm markets may never reach the take leg (unbounded holds until a 1% adverse close), violent markets may gap past both in one bar (exit at the next close, slippage uncapped by any order).
- Single-trigger system: produces zero trades while `RSI >= 30`; the book sits flat through entire rallies, not hedged.
- The `RSI < 30` gate buys falling knives by construction; waterfall continuation past the stop is the source-stated primary risk.
- Source demo window is five days (2023-12-14 → 2023-12-18); full-history behavior is unreported by the source and unclaimed here.
- `strategy.percent_of_equity 50` sizing in the source is replaced event-neutrally by the house overlay; expectancy comparisons must use the overlay, never the source sizing.

## Implementation status

- `implementation_status: not-implemented`.
- Normalized rule is fully specified above; no Hummingbot/Qlib/n8n/survivor/Paper/Testnet/Live work has been performed or is authorized by this record.

## Adoption boundary

- `adoption: not-approved`, `approval_scope: research-only`, `status: research-only`.
- This record is semantic normalization only. It is not profitability validation, not a survivor promotion, and not Paper/Testnet/Mainnet authorization. Only `hb_ready_status: PASS` records may enter the current Hummingbot/Qlib performance-research downstream, subject to that workflow's own gates.

## Related Wiki records

None.

## Sources

- Primary: https://www.fmz.com/strategy/436250 (mirror + live page re-verified 2026-10-07; last modified 2023-12-22 15:00:48).
- Corroborating duplicate mirror (byte-identical Pine block): https://www.fmz.com/strategy/427892 (last modified 2023-09-26 16:11:55).
- Pine v4 `strategy()` declaration semantics (first-party reference): https://www.tradingview.com/pine-script-reference/v4/#fun_strategy
- Pine v4 `strategy.entry` semantics: https://www.tradingview.com/pine-script-reference/v4/#fun_strategy{dot}entry
- Pine v4 `strategy.close` semantics: https://www.tradingview.com/pine-script-reference/v4/#fun_strategy{dot}close
- Pine v4 `rsi` built-in: https://www.tradingview.com/pine-script-reference/v4/#fun_rsi
- Strategy execution model (broker emulator, `process_orders_on_close`): https://www.tradingview.com/pine-script-docs/concepts/strategies/
