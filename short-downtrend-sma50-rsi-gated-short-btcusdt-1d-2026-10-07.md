---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Short-in-downtrend SMA50 plus RSI-gated short system on BTCUSDT 1d bars
created: 2026-10-07
updated: 2026-10-07
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: high
source_as_of: 2023-11-07
sources:
  - https://www.fmz.com/strategy/431428
  - https://www.tradingview.com/pine-script-reference/v4/#fun_strategy
  - https://www.tradingview.com/pine-script-reference/v4/#fun_strategy{dot}entry
  - https://www.tradingview.com/pine-script-reference/v4/#fun_strategy{dot}close
  - https://www.tradingview.com/pine-script-reference/v4/#fun_sma
  - https://www.tradingview.com/pine-script-reference/v4/#fun_rsi
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The prose says entries trigger 'below the 100-day simple moving average' (100日简单移动平均线), but the pinned code computes MA = sma(close, inSignal) with inSignal default 50. The code governs: SMA(50), not SMA(100)."
  - "The prose describes gradual scaling ('逐步建立短仓头寸', 'multiple sequential sell orders' on Coinrule), but the pinned Pine declares no pyramiding (language default: single same-side position) and carries exactly one short entry id. The code governs: one short position, no scaling, no sequential adds."
  - "The prose describes attached stop-loss / take-profit orders per trade, but the code contains zero strategy.exit / stop / limit orders — the 3%/2% levels are evaluated once per bar on the close inside strategy.close. The code governs: bar-close signal exits only; an intrabar pierce of either level exits nothing until the bar closes."
  - "The prose suggests a 1:1.5 stop/take ratio 'could work', but the pinned code fixes +3% stop distance and -2% take distance from the average entry price. The code governs: 3% / 2%."
---

# Short-in-downtrend SMA50 plus RSI-gated short system on BTCUSDT 1d bars

## Provenance

Primary source read end to end (FMZ strategy page mirror plus live re-verification):

- FMZ strategy: https://www.fmz.com/strategy/431428 (`下跌趋势短线交易策略Short-Trading-Strategy-in-Downtrend`, page author ChaoZhang; Pine strategy title `Short In Downtrend Below MA100`, `//@version=4`, `// © Coinrule`).
- Last modified (as printed on the page): 2023-11-07 17:06:59.
- FMZ backtest block pinned on the page: `start: 2022-10-31 00:00:00`, `end: 2023-11-06 00:00:00`, `period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]` — single pair, 1d decision timeframe.
- Live re-verification (2026-10-07): the FMZ page returns HTTP 200 (777358 bytes); the page title (`Short Trading Strategy in Downtrend | FMZ`), the author (ChaoZhang), the Pine title (`Short In Downtrend Below MA100`), `process_orders_on_close=true`, `inSignal=input(50, title='MASignal')`, `MA= sma(close, inSignal)`, `RSI = rsi(close, lengthRSI)`, the exact entry line (`strategy.entry(id=\"short\", long = false, when = close < MA and RSI > 30)`), the exact exit line (`strategy.close(\"short\", when = close > shortStopPrice or close < shortTakeProfit and window())`), and the last-modified stamp (2023-11-07 17:06:59) all match the mirror. No live-page fact contradicts the mirror.
- Mirror executable block: one `strategy()` declaration (`process_orders_on_close=true`, no `calc_on_every_tick`, no `pyramiding`, no `max_bars_back`), dead date inputs behind a hardcoded `window() => true`, `inSignal = 50`, `lengthRSI = 14`, `MA = sma(close, inSignal)`, `RSI = rsi(close, lengthRSI)`, and exactly two live order calls: one `strategy.entry(id="short", long = false, when = close < MA and RSI > 30)`, one `strategy.close("short", when = close > shortStopPrice or close < shortTakeProfit and window())` with `shortStopPrice = strategy.position_avg_price * (1 + 0.03)` and `shortTakeProfit = strategy.position_avg_price * (1 - 0.02)`.
- Censuses over the pinned block: `request.*` 0, `security(` 0, `strategy.exit` 0, `strategy.order` 0, `strategy.close_all` 0, `stop=` 0, `limit=` 0, `qty_percent` 0, `crossover` 0, `crossunder` 0, `ta.cross` 0, `strategy.long` 0 live occurrences, `high`/`low`/`open`/`volume` 0 occurrences in trading logic.

Licence and rights: this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

Pre-write dedup (2026-10-07): working-tree searches for `431428`, `Short In Downtrend`, and `Short-Trading-Strategy-in-Downtrend` returned 0 matches; no MA100-regime record and no fixed-percentage bar-close-exit short record exists on `main`. Closest records: `ibs-mean-reversion-short-ethusdt-1h-2026-10-06.md` (1h IBS fade short on ETHUSDT) and `rsi-classic-level-reversal-btcusdt-1h-2026-10-07.md` (Coinrule RSI 30/60 level-reversal, 1h). Five-axis distinction: mechanism differs (daily close holding below an SMA50 downtrend line with an RSI-above-30 bear-market gate and ±3%/2%-from-entry bar-close exits, versus intraday IBS fades and RSI level-cross reversals), signal construction differs (regime inequality plus avg-price-relative exits, no oscillator cross anywhere), horizon differs (1d versus 1h), source identity differs (FMZ 431428 versus FMZ 482784 / 441161), direction handling is short-only by code (`long = false`, zero live long calls). Closed research PRs contain no 431428 submission (full closed list reviewed: #6 WaveTrend, #10 golden/dead cross, #17 MACD histogram, #20 Ichimoku-RSI and merged family records — none is this source). `gh pr list --state open` shows only PR #36 (reconstruction lane, no `research/*` collision).

## Economic mechanism

### Source-reported

A downtrend short system: it waits until the market is judged to be in a falling trend (close under a slow moving average, confirmed by RSI not being oversold), opens a short, and lets each trade breathe inside a wider-than-target stop band (+3% stop versus −2% take) so normal volatility does not shake it out. Exits when the close escapes above the stop line or reaches below the take line.

### Research interpretation

Bear-regime short harvesting with asymmetric patience: the `close < SMA50` leg keeps the system sidelined in uptrends, the `RSI > 30` leg refuses to chase deeply oversold waterfall bars, and the +3%/−2% close-evaluated exits cut losers slower than they bank winners — the opposite asymmetry of a tight-stop trend system. No leverage, sizing, or cost edge is embedded in the signal; the source `percent_of_equity 100%` line is capital configuration replaced event-neutrally by the house overlay (see Execution assumptions).

## Signal

Exact rule as pinned (Pine v4, defaults quoted — inputs unmodified):

- Inputs: `inSignal = 50`, `lengthRSI = 14` (`minval=1` guard never binds at 14).
- Indicators: `MA[t] = sma(close, 50)[t]` (simple mean of the last 50 closes including bar `t`); `RSI[t] = rsi(close, 14)[t]` (Pine v4 built-in Wilder RMA-based RSI on close).
- Entry (short-only): `entry[t] = (close[t] < MA[t]) and (RSI[t] > 30)`, live via `strategy.entry(id="short", long = false, when = entry[t])`. Strict inequalities on both legs: exact equality on either leg (`close == MA`, `RSI == 30`) fires nothing — the tie case is defined, not ambiguous. The rule contains 0 `crossover`/`crossunder` calls, so the prior-bar tie-semantics blocker that closed PR #6 cannot arise here.
- Exit levels (fixed per open position): `shortStopPrice = avg_entry * 1.03`, `shortTakeProfit = avg_entry * 0.98`, where `avg_entry` is `strategy.position_avg_price` (single-position book, so exactly the entry fill price).
- Exit (full close of the one short): `exit[t] = (close[t] > shortStopPrice) or (close[t] < shortTakeProfit and window())`. Pine `and` binds tighter than `or`, and `window()` is identically `true` (hardcoded `window() => true`; the seven date inputs are dead), so the live condition reduces exactly to `(close[t] > avg_entry * 1.03) or (close[t] < avg_entry * 0.98)`, evaluated once per bar on the close. While flat, `position_avg_price` is `na` and both comparisons are falsy — the exit is inert with no position, deterministically.
- Mutual exclusivity: entry and exit can be true on the same bar only when flat-plus-entry ordering matters; Pine evaluates the entry first in source order and the exit's `na`-levels are falsy on the entry bar (avg price unavailable until the entry-bar close), so the entry bar can never self-exit — deterministic by language semantics, no priority choice required.
- Re-entry: after an exit the book is flat, so the next bar with `entry[t]` true opens a fresh short. While short, further entry signals are rejected under the default single-position declaration. No cooldown is declared and none is needed: re-entry requires the flat state plus a fresh true evaluation, so cooldown semantics are provably irrelevant rather than missing.
- Opposite-signal exit: not applicable — there is no long side (zero live long calls); the short is exited only by the ±% rule above.
- Stop loss / take profit / trailing / time limit as orders: explicitly none (0 `strategy.exit`, 0 `stop=`/`limit=`). The 3%/2% levels are bar-close signal exits, not stop/limit orders: an intrabar pierce of either level exits nothing — the close must confirm beyond the level on a completed bar. No silent Hummingbot defaults are relied upon.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only. `open`, `high`, `low`, `volume` occur 0 times in the trading logic; no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, or cross-venue state is read.
- Single decision timeframe `1d`. The script is timeframe-agnostic (0 `request.*`, 0 `security(`, 0 `timeframe` references), so `basePeriod: 1h` in the FMZ block carries no cross-timeframe dependency and no causal alignment is owed.
- Warmup: `sma(close, 50)` is defined from the 50th bar; `rsi(close, 14)` seeds over its first 14 bars. First possible signal at bar index 50 (the 51st completed bar). No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT under the house overlay (source venue is Binance USDT-M BTC futures, which natively supports the short side — no naked-spot-short construction is required or assumed).
- Order timing: the two live order calls are market entry/close with `process_orders_on_close=true` and no `calc_on_every_tick` (language default false, recorded as source-declared-by-default): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. No next-bar-open, maker-touch, queue, or intrabar-path-dependent fill exists anywhere in the rule.
- Sizing/capital: source `default_qty_type = strategy.percent_of_equity, default_qty_value = 100` and `initial_capital = 1000` are event-neutral capital configuration, replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3×/5×) and never presented as source-native behavior. Source declares no commission rate (no `commission_*` fields), so the pinned house cost assumptions apply as pure accounting.
- Concurrency: at most one open short (single entry id, default single-position declaration); no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The FMZ page and its embedded description carry no numeric performance claims — no ROI, Sharpe, win rate, drawdown, or trade-count figures appear anywhere in the artifact (a regex sweep for `%`-figures, Sharpe, profit-factor and trade counts returns zero performance statements). Recorded as an explicit gap, not filled: this record claims no source-reported performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Entry-bar self-exit is impossible (`position_avg_price` is `na` until the entry-bar close; both exit comparisons are falsy there) — verified by language semantics, not by backtest.
2. Exact-equality bars (`close == MA`, `RSI == 30`, `close == stop/take level`) fire neither leg — strict inequalities throughout, so ties are defined.
3. The `and window()` suffix and all seven date inputs are dead code (`window() => true`); they change no event and are excluded from the normalized rule as written, not repaired.
4. `MASignal` default is 50 while every prose line says 100-day: any 100-day reading would be a different, unpinned rule.
5. Prose-described Coinrule sequential scaling and per-trade stop/limit orders have no Pine expression: a scaled or stop-order variant would be a different, unpinned rule.
6. Short side requires a venue that supports shorting (source venue does); a spot-only port would be lossy by construction.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `SMA(50)`, `RSI(14)`, `RSI > 30` gate, `+3% / −2%` close-evaluated exits, short-only, `1d` BTCUSDT, same-bar-close fills are frozen.

- F1 — Regime relevance: on full-history 1d BTCUSDT, shorts opened while `close < SMA50` must show worse buy-and-hold-relative drift than unconditional short entries; fail ⇒ the regime leg adds nothing.
- F2 — Gate relevance: entries with `RSI ≤ 30` excluded by the gate must underperform included entries net of the house overlay; fail ⇒ the RSI leg is decorative.
- F3 — Exit asymmetry: replacing the +3%/−2% exits with a symmetric ±2.5% pair must not improve net expectancy; fail ⇒ the asymmetry is arbitrary.
- F4 — Intrabar discipline: evaluating the same ±% levels on intrabar pierce (stop-order semantics) must produce a materially different trade list; pass ⇒ confirms the record's bar-close-only claim is load-bearing and correctly pinned.

## Crypto portability

Pinned to BTCUSDT (Binance USDT-M lineage) under the house overlay. The short side ports only to venues with native short support (perps/margin); spot ports are excluded by construction, not by parameter choice. No cross-venue state, no funding-dependent leg, no stablecoin-specific assumption.

## Limitations

- Fixed ±3%/2% bands do not adapt to volatility: calm markets may never reach either level (unbounded holds), violent markets may gap past both in one bar (exit at the next close, slippage uncapped by any order).
- Single-regime system: produces zero trades for entire bull years while `close > SMA50`; the book sits flat, not hedged.
- The `RSI > 30` gate is a blunt oversold veto, not a timing edge; V-reversals against the short are the source-stated primary risk.
- Source backtest window is one year (2022-10-31 → 2023-11-06); full-history behavior is unreported by the source and unclaimed here.
- `strategy.percent_of_equity 100` compounding in the source is replaced event-neutrally by the house overlay; expectancy comparisons must use the overlay, never the source sizing.

## Implementation status

- `implementation_status: not-implemented`.
- Normalized rule is fully specified above; no Hummingbot/Qlib/n8n/survivor/Paper/Testnet/Live work has been performed or is authorized by this record.

## Adoption boundary

- `adoption: not-approved`, `approval_scope: research-only`, `status: research-only`.
- This record is semantic normalization only. It is not profitability validation, not a survivor promotion, and not Paper/Testnet/Mainnet authorization. Only `hb_ready_status: PASS` records may enter the current Hummingbot/Qlib performance-research downstream, subject to that workflow's own gates.

## Related Wiki records

None.

## Sources

- Primary: https://www.fmz.com/strategy/431428 (mirror + live page re-verified 2026-10-07; last modified 2023-11-07 17:06:59).
- Pine v4 `strategy()` declaration semantics (first-party reference): https://www.tradingview.com/pine-script-reference/v4/#fun_strategy
- Pine v4 `strategy.entry` semantics: https://www.tradingview.com/pine-script-reference/v4/#fun_strategy{dot}entry
- Pine v4 `strategy.close` semantics: https://www.tradingview.com/pine-script-reference/v4/#fun_strategy{dot}close
- Pine v4 `sma` / `rsi` built-ins: https://www.tradingview.com/pine-script-reference/v4/#fun_sma and https://www.tradingview.com/pine-script-reference/v4/#fun_rsi
- Strategy execution model (broker emulator, `process_orders_on_close`): https://www.tradingview.com/pine-script-docs/concepts/strategies/
