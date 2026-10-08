---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: RSI-50-gated SMA 100/150 crossover two-sided reversal trend system on BTCUSDT 1d bars
created: 2026-10-08
updated: 2026-10-08
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: high
source_as_of: 2023-10-09
sources:
  - https://www.fmz.com/strategy/428799
  - https://github.com/fmzquant/strategies/blob/master/RSI与SMA组合交易策略RSI-and-SMA-Combination-Trading-Strategy.md
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# RSI-50-gated SMA 100/150 crossover two-sided reversal trend system on BTCUSDT 1d bars

## Provenance

Primary source read end to end (FMZ strategy page live plus GitHub mirror cross-check):

- FMZ strategy: https://www.fmz.com/strategy/428799 (`RSI and SMA Combination Trading Strategy`, Pine title `RSI and SMA`, `//@version=5`, page uploader `ChaoZhang`, code header `© Coinrule` under MPL-2.0).
- FMZ backtest block pinned on the page: `start: 2022-10-02 00:00:00`, `end: 2023-10-08 00:00:00`, `period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]` — single pair; the `1d` figure is the script decision timeframe adopted as the research frame.
- Live re-verification (2026-10-08): the FMZ page returns HTTP 200 (764,717 bytes); the page title, the full embedded Pine block (declaration with `process_orders_on_close=true`, the `timePeriod` floor, `ta.rsi(close, 14)`, `ta.sma(close, 100)` / `ta.sma(close, 150)`, the `bullish`/`bearish` conjunctions, the two `strategy.entry` lines and the two `strategy.close("Exit", …)` lines), and the backtest header all match the mirror line for line. No live-page fact contradicts the mirror.
- Mirror: `fmzquant/strategies` file `RSI与SMA组合交易策略RSI-and-SMA-Combination-Trading-Strategy.md` (carries the same Pine block and a `Detail` link back to FMZ 428799; mirror page `Last Modified 2023-10-09`, adopted as `source_as_of`).
- Censuses over the pinned block: `strategy.entry` 2, `strategy.close` 2, `strategy.exit` 0, `strategy.order` 0, `request.*` 0, `security(` 0, `timeframe(` 0, `volume` 0, `stop=` 0, `limit=` 0, `profit=` 0, `loss=` 0, `pyramiding` 0, `calc_on_every_tick` 0, `varip` 0, `input.time` 0. Series read: `close` only, plus bar `time` inside the deterministic date floor (causal, never future). `plot`/`plotshape` lines never execute trading logic.

Licence and rights: the pinned block carries an MPL-2.0 header (`© Coinrule`). This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

Pre-write dedup (2026-10-08): working-tree searches for `428799` and `RSI and SMA` return 0 strategy records; pool FMZ-id census (23 ids) contains no `428799`. Open `research/*` PRs: only #48 (Larry Williams 3-EMA channel streak long, FMZ 451075) and #49 (Gaussian channel StochRSI-gated breakout long, FMZ 482888) plus the non-Scout #36 (QuantaAlpha price-volume family, no volume read here) — different mechanisms, indicators, and sources. Closed Scout PRs #10 (golden/dead cross, FMZ 435513, bare MA cross with no regime gate) and #17 (MACD histogram, FMZ 433919) concern different constructions and sources. Closest pool records are different mechanism classes: `ema-20-50-cross-btcusdt-1h-2026-10-06.md` (bare EMA20/50 close-cross, Forven GitHub source, no oscillator gate), `rsi-ma-crossover-reversal-btcusdt-1d-2026-10-07.md` (RSI crossing its own SMA — oscillator-vs-average, no price-average cross), `ema-cloud-7-20-trend-btcusdt-1d-2026-10-07.md` (close-vs-fast plus fast-vs-slow alignment conjunctions, 0 crossover calls), `triple-ema-volstop-tp-long-btcusdt-1d-2026-10-08.md` (triple-EMA simultaneous-cross conjunction), `hull-ema-crossover-reversal-btcusdt-1d-2026-10-08.md` (contemporaneous Hull-vs-EMA cross, no gate). Five-axis distinction: mechanism differs (slow price-average cross that only fires inside the matching RSI-50 regime, two-sided immediate reversal), signal construction differs (`ta.crossover(ta.sma(close,100), ta.sma(close,150)) AND ta.rsi(close,14) > 50` — the RSI conjunction vetoes crosses that print on the wrong side of 50, so it alters trade events rather than merely retuning a length), exits differ (reversal entries plus the event-inert `close("Exit")` pair, proven below), timeframe/market frame is `1d` BTCUSDT futures under the house overlay.

## Economic mechanism

### Source-reported

A slow-trend reversal system: two long price averages (SMA 100 fast, SMA 150 slow) define the trend, and the RSI-50 regime check acts as the trigger guard — longs only print when momentum is already above its midpoint, shorts only when below. The cross gives the turn, the RSI level refuses counter-regime crosses.

### Research interpretation

Gated slow-average reversal with no filter beyond the gate and no risk leg. The 100/150-bar averages move glacially on daily bars, so raw crosses are rare; the RSI-50 conjunction further vetoes crosses that arrive while momentum disagrees, which is the record's only whipsaw defence. Both legs are live at all times once the date floor passes; the system is always positioned after its first gated cross except on bars where a series is still `na`. No leverage, sizing, or cost edge is embedded in the signal; the declaration carries only event-neutral accounting lines (30% equity sizing, 0.1% commission, 1000 capital), so the house overlay supplies them (see Execution assumptions).

## Signal

Exact rule as pinned (Pine v5, defaults quoted — inputs unmodified):

- Declaration: `strategy('RSI and SMA', overlay = true, initial_capital = 1000, process_orders_on_close = true, default_qty_type = strategy.percent_of_equity, default_qty_value = 30, commission_type = strategy.commission.percent, commission_value = 0.1)`. `calc_on_every_tick` is unset (default false); `pyramiding` is unset (v5 language default: no additional same-direction entry while positioned — the same default-convergence earlier PASS reviews accepted, and it is load-bearing here, see Execution assumptions).
- Date floor: `timePeriod = time >= timestamp(syminfo.timezone, 2022, 1, 1, 0, 0)` — deterministic, causal (bar `time` only), true for every bar on/after 2022-01-01. Bars before the floor admit no entries by explicit rule (pinned, not invented).
- Oscillator: `rsi = ta.rsi(close, 14)` on `close`. First-party deterministic builtin; no script-level data-dependent division exists anywhere in the chain (the only divisions are inside `ta.rsi`/`ta.sma` guarded builtins with defined edge semantics).
- Averages: `fastEMA = ta.sma(close, 100)` (name is the source's; it is an SMA), `slowEMA = ta.sma(close, 150)`, both on `close`. First-party deterministic builtins, no variant/smoothing/source choice left open.
- Signals (strict v5 crossover semantics — a tie on either bar fires neither leg, see Negative evidence): `bullish = ta.crossover(fastEMA, slowEMA) and rsi > 50`; `bearish = ta.crossover(slowEMA, fastEMA) and rsi < 50`. An exact `rsi == 50` fires neither leg.
- Long leg: `strategy.entry("Long", strategy.long, when = bullish and timePeriod)`; `strategy.close("Exit", when = bearish)`.
- Short leg: `strategy.entry("Short", strategy.short, when = bearish and timePeriod)`; `strategy.close("Exit", when = bullish)`.
- Direction: two-sided. Both entries are explicit; neither side is disabled.
- Stop-loss / take-profit / trailing / time limit: explicitly none (0 `strategy.exit`, 0 `stop=`/`limit=`/`profit=`/`loss=`). Opposite-signal logic is the sole exit path.
- Inert code, provably excluded: `notInTrade` (defined once, never read by any `when`/order condition — write-only like the dead state in the Hull-MA/EMA record), `showDate` (display input, never read), and all `plot`/`plotshape` lines.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (RSI, both SMAs, both crosses) plus bar `time` for the pinned date floor. No `open`, no `high`/`low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session, or cross-venue state is read by any executable line.
- Single decision timeframe `1d` (backtest `period: 1d`). `basePeriod: 1h` is FMZ demo-execution granularity; with 0 intrabar orders and close-gated evaluation it cannot alter any admitted event.
- Warmup: longest live window is 150 bars (`ta.sma(close, 150)`); the `crossover` prior-bar reference needs one further bar (`ta.rsi` needs 14, absorbed). First fully-defined evaluation at 151 completed `1d` bars; no signal is evaluable before that. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT under the house overlay (source venue is Binance USDT-M BTC futures; the house overlay runs Isolated futures at 3×/5×, two-sided for this record since both directions are coded — no naked-spot construction needed).
- Order timing: the declaration sets `process_orders_on_close = true` with `calc_on_every_tick` unset (default false): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. No next-bar-open, maker-touch, queue, or intrabar-path-dependent fill.
- Sizing/capital: the declaration's 30%-of-equity sizing, 1000 initial capital, and 0.1% commission are pure event-neutral accounting, replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3×/5×) and pinned house cost assumptions, never presented as source-native behavior.
- Concurrency: `pyramiding` is unset (v5 default: no same-direction add while positioned). The default is load-bearing here and therefore pinned explicitly: a second same-side gated cross can in principle recur while holding that side (e.g. the fast average dips below the slow and re-crosses while RSI never leaves that side, so the opposite leg never fires), and the admitted rule blocks the add and holds. Opposite-direction entries always reverse first (standard broker-emulator netting; pyramiding limits same-side adds only). Single engine position; re-entry is allowed immediately after any close whenever the gated conjunction fires again (no cooldown specified — explicitly none, not invented). No shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The FMZ page and mirror ship prose only: qualitative claims ("decent returns even in a bear market", "could improve win rate") plus risk disclosures (reversal failure, trend disruption, fee drag, sizable drawdown). The live page carries no numeric performance table for this strategy — the only `收益`-family hits on the page are site-chrome (unrelated-strategy listings) and the qualitative risk prose quoted above; likewise `年化`/`胜率`/`回撤`/`drawdown`/`win rate` hits are chrome or prose, with zero figures attached. Recorded as an explicit gap, not filled: this record claims no source-reported performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Flat-book determinism: with no open position both `strategy.close("Exit", …)` legs are deterministic no-ops under either ID-matching reading; only a genuine gated cross can open.
2. Same-bar mutual exclusivity is proven, not assumed: `bullish` needs `fast[1] <= slow[1]` with `fast > slow` plus `rsi > 50`; `bearish` needs the mirror plus `rsi < 50`. Both can never hold on one bar (exact prior-bar equality admits at most one strict current-bar inequality, and `rsi > 50` / `rsi < 50` are disjoint; `na` on any series makes both false). Entry and exit therefore never co-fire — no call-order priority is required.
3. The `close("Exit", …)` pair is event-inert under either reading of unmatched-ID `strategy.close` semantics, so no interpretation is invented: reading A (unmatched ID is a no-op) leaves exits to the opposite entries, which reverse the position; reading B (close exits any open position) fires the close on the same bar before/after the opposite entry in script order and nets to the identical flip. Enumerated bar-by-bar (flat/long/short × bullish/bearish/neither), both readings produce the same position after every bar: always positioned after the first gated cross, flipping only on gated crosses, holding through same-side repeats (blocked adds) and through pre-floor bars.
4. Boundary ties are defined: `fastEMA == slowEMA` on either compared bar fires neither `ta.crossover` leg (strict v5 semantics), and `rsi == 50` satisfies neither conjunction — ties hold position, they never invent an order.
5. The date floor and dead state are pinned, not removed: moving the 2022-01-01 floor, switching the averages to EMA, reviving `notInTrade`, or retargeting the `close("Exit")` IDs would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `ta.sma(close, 100)` vs `ta.sma(close, 150)` contemporaneous cross gated by `ta.rsi(close, 14)` vs 50, two-sided immediate reversal, `1d` BTCUSDT, same-bar-close fills are frozen.

- F1 — Gate relevance: the gated rule must beat its bare-cross ablation (RSI conjunctions removed, crosses kept) net of costs; fail ⇒ the RSI-50 gate earns no keep and the system is a plain slow-cross system wearing a gate costume.
- F2 — Slow-leg relevance: the (100, 150) set must not be dominated net of costs by both the (50, 200) and (20, 50) neighbor sets with the gate kept; fail on both sides ⇒ the set choice is arbitrary rather than structural.
- F3 — Short-leg relevance: the two-sided rule must beat its long-only ablation (short entries removed, long exits on the bearish leg kept as closes) net of costs; fail ⇒ the short side earns no keep.
- F4 — Exit relevance: replacing the opposite-signal reversal with a fixed 50-bar time exit (entries kept, opposite leg removed) must not improve net expectancy; fail ⇒ the reversal exit leg is decorative.

## Crypto portability

Pinned to BTCUSDT (Binance USDT-M lineage) under the house overlay. The close-derived two-sided logic ports to perps without structural change; no funding-dependent leg, no stablecoin-specific assumption, no cross-venue state. Spot deployment would require dropping the short leg, which is a different, unpinned rule — not admitted here.

## Limitations

- Glacial signals: SMA 100/150 on daily bars cross a few times per regime; entries arrive months late to major turns and the system rides the full adverse excursion until the reverse cross prints.
- Gate veto risk: the RSI-50 conjunction can veto exactly the cross that marks the turn (cross prints while RSI is a fraction on the wrong side), leaving the system stranded on the wrong side by construction.
- No adverse-stop protection: exits print only on the reverse gated cross, so an adverse drift that never re-crosses is ridden indefinitely; the source's own risk section concedes sizable drawdown and whipsaw losses.
- Date-floor nuance: under full-history house evaluation, bars before 2022-01-01 are flat by explicit source rule — a pinned property of this record, not missing data.
- Single-exchange lineage: the rule reads only closes, but the pinned demo venue is Binance USDT-M BTC futures; other venues' closes are an untested substitution.

## Implementation status

- `implementation_status: not-implemented`.
- Normalized rule is fully specified above; no Hummingbot/Qlib/n8n/survivor/Paper/Testnet/Live work has been performed or is authorized by this record.

## Adoption boundary

- `adoption: not-approved`, `approval_scope: research-only`, `status: research-only`.
- This record is semantic normalization only. It is not profitability validation, not a survivor promotion, and not Paper/Testnet/Mainnet authorization. Only `hb_ready_status: PASS` records may enter the current Hummingbot/Qlib performance-research downstream, subject to that workflow's own gates.

## Related Wiki records

None.

## Sources

- Primary: https://www.fmz.com/strategy/428799 (live page re-verified 2026-10-08, HTTP 200, 764,717 bytes; backtest block 2022-10-02 → 2023-10-08, `period: 1d`, Binance USDT-M BTC).
- Mirror: https://github.com/fmzquant/strategies/blob/master/RSI与SMA组合交易策略RSI-and-SMA-Combination-Trading-Strategy.md (same Pine block line for line, links back to FMZ 428799; mirror page Last Modified 2023-10-09).
- Pine `strategy()` declaration semantics (first-party reference): https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
- Strategy execution model (broker emulator, `process_orders_on_close`): https://www.tradingview.com/pine-script-docs/concepts/strategies/
