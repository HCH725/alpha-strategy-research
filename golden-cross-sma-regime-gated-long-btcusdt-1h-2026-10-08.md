---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Golden-cross SMA 9/50 regime-gated long-only trend system on BTCUSDT 1h bars
created: 2026-10-08
updated: 2026-10-08
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: high
source_as_of: 2020-09-16
sources:
  - https://www.tradingview.com/script/pUu7bWV5-Golden-Cross-Optimised-For-Reversal-by-Coinrule/
  - https://github.com/hasnocool/tradingview-pine-scripts/blob/69969aeaf271b2f7b5a7632a1bde43069a0cbe26/Golden%20Cross%20Optimised%20For%20Reversal%20(by%20Coinrule).pine
  - https://www.tradingview.com/pine-script-reference/v4/#fun_strategy
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Golden-cross SMA 9/50 regime-gated long-only trend system on BTCUSDT 1h bars

## Provenance

Primary source read end to end (TradingView canonical strategy page, live browser read 2026-10-08):

- Canonical page: https://www.tradingview.com/script/pUu7bWV5-Golden-Cross-Optimised-For-Reversal-by-Coinrule/ (`Golden Cross Optimised For Reversal (by Coinrule)`, Strategy by Coinrule, `OPEN-SOURCE SCRIPT`, Sep 16 2020, adopted as `source_as_of`).
- Page-chart context at read time: BITSTAMP BTC/USD on a 15-minute chart — a display context, not a strategy rule (the script takes no timeframe, symbol, session, or venue input).
- Page-stated rules (verbatim substance): Buy signal = MA(9) crosses above MA(50) while MA(50) is below MA(100); Sell signal = MA(9) crosses below MA(50). Page further states the system "works significantly better on lower time frames" and was "backtested mostly on cryptocurrencies". The page carries zero numeric performance claims (no returns, win rate, drawdown, or trade-count figures anywhere in the prose).
- Immutable code provenance: hasnocool mirror file `Golden Cross Optimised For Reversal (by Coinrule).pine` at pinned commit `69969aeaf271b2f7b5a7632a1bde43069a0cbe26` (verified still the remote HEAD via `git ls-remote` this run), blob `c9aa2b4a2cdbc987a82ad0bd410c9b4733f321e8`, 3558 bytes. The mirror header (`Script Name`, `Author: Coinrule`, description lead) matches the canonical page verbatim, and the embedded Pine block implements exactly the page-stated rules (entry gate `slow > normal`, cross pair, cross-under close — see Signal).
- Corroboration only (not adopted): FMZ strategy 435864 embeds the identical Pine block title verbatim (`Golden Cross, SMA 100, Moving Average Strategy (by Coinrule)`); its `Futures_Binance` exchange header is explicitly not adopted as source semantics — this record's venue/market comes from the TV primary plus the house overlay, so the instrument-identity gap that closed Scout PR #10 does not transfer.
- Censuses over the pinned block: `strategy.entry` 1, `strategy.close` 1, `strategy.exit` 0, `strategy.order` 0, `request.*` 0, `security(` 0, `timeframe(` 0, `volume` 0, `high` 0 / `low` 0 in any order-gating line, `stop=` 0, `limit=` 0, `profit=` 0, `loss=` 0, `pyramiding` 0, `calc_on_every_tick` 0, `varip` 0, `input.time` 0. Series read by order logic: `close` only, plus bar `time` inside the deterministic date window (causal, never future). `barcolor`/`plot`/`bgcolor` lines are display-only and never gate an order.

Licence and rights: the canonical page is an open-source publication by Coinrule; the mirror block carries an MPL-2.0 lineage. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

Pre-write dedup (2026-10-08): working-tree searches for `pUu7bWV5`, `Golden_Cross`, and `Golden Cross` return 0 strategy records. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long, FMZ 451075) and #49 (Gaussian channel StochRSI-gated breakout long, FMZ 482888) — different mechanisms, indicators, and sources. Closed Scout PR #10 (golden/dead cross, FMZ 435513: SMA 3/19 cross, rising-SMA100 gate, +3%-profit-gated exit, FMZ mirror source) differs on all five axes: different canonical source (Coinrule TV Sep-2020 vs FMZ mirror), different cross pair (9/50 vs 3/19), different gate polarity and form (level gate `SMA100 > SMA50` at the cross bar vs rising-SMA100 trend gate), different exit (unconditional signal close vs profit-gated close that can never cut a loss), and different research frame (1h vs 1d). Closest pool records are different mechanism classes: `rsi-sma-gated-cross-reversal-btcusdt-1d-2026-10-08.md` (SMA 100/150 cross gated by RSI-50, two-sided immediate reversal), `ema-20-50-cross-btcusdt-1h-2026-10-06.md` (bare EMA 20/50 close-cross, no regime gate), `short-downtrend-sma50-rsi-gated-short-btcusdt-1d-2026-10-07.md` (SMA50-plus-RSI short-only), `hull-ema-crossover-reversal-btcusdt-1d-2026-10-08.md` (Hull-vs-EMA cross, no gate), `triple-ema-volstop-tp-long-btcusdt-1d-2026-10-08.md` (triple-EMA simultaneous-cross conjunction with ATR stop). Five-axis distinction: mechanism differs (fast/medium cross that fires only while the slow average holds above the medium — a level-regime gate, long-only, exit on the plain reverse cross), signal construction differs (`crossover(sma(close,9), sma(close,50)) AND sma(close,100) > sma(close,50)` — the level conjunction vetoes crosses that print when the slow regime disagrees, altering trade events rather than retuning a length), exits differ (unconditional `strategy.close` on the reverse cross, no stop/target/trailing/time leg), timeframe/market frame is `1h` BTCUSDT under the house overlay, and source identity differs in all cases.

## Economic mechanism

### Source-reported

A filtered golden-cross trend system: a fast/medium average cross gives the turn, and a slow-average level gate refuses crosses that arrive against the prevailing regime — longs print only while SMA100 already sits above SMA50, so the system buys early-regime turns rather than every cross. The reverse cross alone closes the trade; there is no stop, target, or time leg by construction.

### Research interpretation

Regime-gated fast-cross trend riding with no risk leg. The 9/50 cross reacts within days on hourly bars while the 100-bar level gate moves glacially, so entries cluster at regime birth and the system holds through the whole excursion until the fast leg re-crosses down. Both the gate and the exit are pure close-derived level/cross logic, so the full event sequence is reproducible from completed bars alone. No leverage, sizing, or cost edge is embedded in the signal; the declaration carries only event-neutral accounting lines (1000 capital, 100%-of-equity sizing), so the house overlay supplies them (see Execution assumptions).

## Signal

Exact rule as pinned (Pine v4, defaults quoted — inputs unmodified):

- Declaration: `strategy("Golden Cross, SMA 100, Moving Average Strategy (by Coinrule)", shorttitle="Golden_Cross_Strat_MA100_optimized", overlay=true, initial_capital = 1000, process_orders_on_close=true, default_qty_type = strategy.percent_of_equity, default_qty_value = 100)`. `calc_on_every_tick` is unset (default false); `pyramiding` is unset (v4 language default 0: no additional same-direction entry while positioned — the same default-convergence earlier PASS reviews accepted for v4 Coinrule blocks in #12/#21/#22/#23, and it is load-bearing here, see Execution assumptions).
- Date window: `start = timestamp(2020, 1, 1, 00, 00)`, `finish = timestamp(2112, 1, 1, 23, 59)`, `window() => time >= start and time <= finish` — deterministic, causal (bar `time` only), true for every bar of the research horizon. Bars outside the window admit no entries and no closes by explicit rule (pinned, not invented).
- Averages (all first-party deterministic `sma` on `close`, no variant/smoothing/source choice left open): `movingaverage_fast = sma(close, 9)`, `movingaverage_slow = sma(close, 100)`, `movingaverage_normal = sma(close, 50)`.
- Signals (strict v4 crossover semantics — a tie on either compared bar fires neither leg, see Negative evidence): `bullish_cross = crossover(movingaverage_fast, movingaverage_normal)`; `bearish_cross = crossunder(movingaverage_fast, movingaverage_normal)`.
- Long leg: `strategy.entry("long", strategy.long)` inside `if bullish_cross and window() and movingaverage_slow > movingaverage_normal`. The `slow > normal` level gate is evaluated on the same completed bar as the cross.
- Exit leg: `strategy.close("long", when = bearish_cross and window())` — unconditional signal close, no profit/price condition.
- Direction: long-only, explicitly. No short entry exists anywhere in the block; the short side is disabled by construction.
- Stop-loss / take-profit / trailing / time limit: explicitly none (0 `strategy.exit`, 0 `stop=`/`limit=`/`profit=`/`loss=`). The reverse-cross close is the sole exit path; otherwise the position is held.
- Inert display code, provably excluded: `switch1/2/3` (bar-color/plot toggles), `bartrendcolor`/`barcolor`, all three `plot` lines, `bgcolor(showDate and window() ...)`, `fromMonth/fromDay/...` inputs other than through `window()` — none is read by any order condition.

## Required data

- Completed `1h` bars of BTCUSDT: `close` only (all three SMAs, both crosses, the level gate) plus bar `time` for the pinned date window. No `open`, no `high`/`low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1h`. The script takes no timeframe input and makes no `request.*`/`security(`/`timeframe(` call, so it is single-frame by construction; `1h` is adopted as the in-lane research frame because the source states the system works significantly better on lower time frames and was tested mostly on cryptocurrencies (the page display context is a 15m BTC/USD chart — context only, not a rule).
- Warmup: longest live window is 100 bars (`sma(close, 100)`); the crossover prior-bar reference needs one further bar. First fully-defined evaluation at the 101st completed `1h` bar; no signal is evaluable before that. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT under the house overlay (source chart context is BITSTAMP BTC/USD spot and the source reports crypto backtests; the rule reads closes only, so the explicitly labeled BTCUSDT research market is the house-overlay instantiation — never presented as source-native venue semantics).
- Order timing: the declaration sets `process_orders_on_close = true` with `calc_on_every_tick` unset (default false): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. No next-bar-open, maker-touch, queue, or intrabar-path-dependent fill.
- Sizing/capital: the declaration's 100%-of-equity sizing and 1000 initial capital are pure event-neutral accounting, replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3×/5×) and pinned house cost assumptions, never presented as source-native behavior.
- Concurrency: `pyramiding` is unset (v4 default 0: no same-direction add while positioned). The default is load-bearing here and therefore pinned explicitly: a second gated cross can recur while long (fast leg dips below the medium and re-crosses up with the slow gate still holding, the reverse cross never printing), and the admitted rule blocks the add and holds. Re-entry is allowed immediately after any close whenever the gated conjunction fires again (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The canonical page ships prose only: qualitative claims (better on lower time frames, tested mostly on cryptocurrencies, fewer false signals than a conventional cross) plus the plain MA-cross risk alluded to by the "false signals" discussion. The page carries no numeric performance table — no returns, win rate, drawdown, or trade-count figures. Recorded as an explicit gap, not filled: this record claims no source-reported performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Flat-book determinism: with no open position the `strategy.close("long", …)` leg is a deterministic no-op; only a genuine gated cross can open.
2. Same-bar mutual exclusivity is proven, not assumed: `bullish_cross` needs `fast[1] <= normal[1]` with `fast > normal`; `bearish_cross` needs `fast[1] >= normal[1]` with `fast < normal`. Both can never hold on one bar (an exact prior-bar tie admits at most one strict current-bar inequality; `na` on any series makes both false). Entry and exit therefore never co-fire — no call-order priority is required.
3. Gate-boundary ties are defined: `slow == normal` on the cross bar blocks the entry (strict `>` fails) while still permitting the exit leg — ties hold flat, they never invent an order. `fast == normal` on either compared bar fires neither cross leg.
4. The date window is pinned, not removed: moving the 2020-01-01 floor, switching any average to EMA, reviving a short leg, or adding a stop/target/cooldown would each be a different, unpinned rule — none is admitted here.
5. Display-code isolation: `bartrendcolor` reads `close` and `change(slow)` but feeds only `barcolor`; it is never read by any order condition, so display toggling cannot alter any admitted event.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `crossover(sma(close,9), sma(close,50))` gated by `sma(close,100) > sma(close,50)`, unconditional cross-under close, long-only, `1h` BTCUSDT, same-bar-close fills are frozen.

- F1 — Gate relevance: the gated rule must beat its bare-cross ablation (level conjunction removed, 9/50 crosses kept) net of costs; fail ⇒ the SMA100 level gate earns no keep and the system is a plain fast-cross system wearing a gate costume.
- F2 — Length relevance: the (9, 50, 100) set must not be dominated net of costs by both the (9, 21, 50) and (12, 26, 100) neighbor sets with the gate form kept; fail on both sides ⇒ the set choice is arbitrary rather than structural.
- F3 — Exit relevance: replacing the cross-under close with a fixed 50-bar time exit (entries kept, reverse-cross leg removed) must not improve net expectancy; fail ⇒ the signal-exit leg is decorative.

## Crypto portability

Pinned to BTCUSDT under the house overlay. The close-derived long-only logic ports to perps or spot without structural change (no short leg exists to drop); no funding-dependent leg, no stablecoin-specific assumption, no cross-venue state. Source lineage is BTC/USD spot (BITSTAMP display context) with crypto backtests, so the BTCUSDT research market stays inside the source's stated applicability.

## Limitations

- Whipsaw clustering at regime seams: the 9/50 cross fires repeatedly while the fast leg oscillates around the medium leg inside a flat slow regime, and each gated cross opens a fresh long that the next cross-under closes at a loss.
- Gate-lag cost: the slow level gate moves glacially, so entries arrive late to genuine turns and the system can sit out the first leg of a new regime while `slow <= normal` still holds.
- No adverse-stop protection: exits print only on the reverse cross, so an adverse drift that never re-crosses is ridden indefinitely; the source's own "false signals" discussion concedes exactly this failure mode.
- Window nuance: under full-history house evaluation, bars before 2020-01-01 are flat by explicit source rule — a pinned property of this record, not missing data.
- Single-family lineage: the rule reads only closes, but cross lengths tuned on 2020-era crypto volatility are an untested transfer to other volatility regimes.

## Implementation status

- `implementation_status: not-implemented`.
- Normalized rule is fully specified above; no Hummingbot/Qlib/n8n/survivor/Paper/Testnet/Live work has been performed or is authorized by this record.

## Adoption boundary

- `adoption: not-approved`, `approval_scope: research-only`, `status: research-only`.
- This record is semantic normalization only. It is not profitability validation, not a survivor promotion, and not Paper/Testnet/Mainnet authorization. Only `hb_ready_status: PASS` records may enter the current Hummingbot/Qlib performance-research downstream, subject to that workflow's own gates.

## Related Wiki records

None.

## Sources

- Primary: https://www.tradingview.com/script/pUu7bWV5-Golden-Cross-Optimised-For-Reversal-by-Coinrule/ (Strategy by Coinrule, open-source, Sep 16 2020; page rules, lower-timeframe/crypto test notes, and zero numeric performance claims all live-verified 2026-10-08; display context BITSTAMP BTC/USD 15m).
- Immutable code mirror: https://github.com/hasnocool/tradingview-pine-scripts/blob/69969aeaf271b2f7b5a7632a1bde43069a0cbe26/Golden%20Cross%20Optimised%20For%20Reversal%20(by%20Coinrule).pine (pinned HEAD verified as remote HEAD this run; blob `c9aa2b4a2cdbc987a82ad0bd410c9b4733f321e8`, 3558 bytes; header and Pine block match the canonical page).
- Pine `strategy()` declaration semantics (first-party reference): https://www.tradingview.com/pine-script-reference/v4/#fun_strategy
- Strategy execution model (broker emulator, `process_orders_on_close`): https://www.tradingview.com/pine-script-docs/concepts/strategies/
