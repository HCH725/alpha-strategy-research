---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: SuperTrend ATR-band flip trend-following long on BTCUSDT 1d bars
created: 2026-10-08
updated: 2026-10-08
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: high
source_as_of: 2026-02-11
sources:
  - https://www.tradingview.com/script/VLRj2sG9-SuperTrend-STRATEGY
  - https://www.tradingview.com/pine-script-reference/v6/#fun_strategy
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# SuperTrend ATR-band flip trend-following long on BTCUSDT 1d bars

## Provenance

Primary source read end to end (TradingView canonical strategy page, live browser read 2026-10-08):

- Canonical page: https://www.tradingview.com/script/VLRj2sG9-SuperTrend-STRATEGY/ (`SuperTrend STRATEGY`, Strategy by `holdon_to_profits`, `OPEN-SOURCE SCRIPT`, badge reads `Updated Feb 11` with no year displayed — adopted as `source_as_of` 2026-02-11; the in-code header comment credits `Slow Cow`, recorded here as-is without adjudicating authorship).
- Page-chart context at read time: BINANCE BTC/USDT PERPETUAL CONTRACT on a 1D chart — a display context, not a strategy rule (the script takes no symbol, timeframe, session, or venue input; its prose states it "works across all asset classes and timeframes").
- Page-stated rules (verbatim substance): streamlined long-only SuperTrend; ATR via SMA of True Range; long entry when SuperTrend flips bearish-to-bullish; position closed when it flips back to bearish; no short entries (framed as spot-friendly); "Buy"/"Close" labels are plotted for visual reference only; a customizable date-range backtest window is included.
- Release-note history (all dated Feb 11, newest first): current prose block pins ATR Period 10 / Multiplier 3.0 / hl2 / 0.015% commission; an older note pins Multiplier 8.5 / 0.01%; the earliest changelog records exactly one execution fix — `Added process_orders_on_close=true to the strategy() declaration` so that orders process at the current bar's close instead of the next bar's open. The live published Source-code tab read line-for-line this run (46 lines, `//@version=6`) carries `process_orders_on_close=true` in the declaration — the changelog fix is confirmed present in the admitted code.
- Executable code governs every pinned value (see the resolved prose-vs-code discrepancies under Negative evidence): `Periods = 10`, `src = hl2`, `Multiplier = 8.5`, `initial_capital = 10000000`, `default_qty_value = 100` (% of equity), `commission_value = 0.015`.
- Censuses over the pinned block: `strategy.entry` 1, `strategy.close` 1, `strategy.exit` 0, `strategy.order` 0, `strategy.close_all` 0, `request.*` 0, `security(` 0, `timeframe(` 0, `input.timeframe` 0, `stop=` 0, `limit=` 0, `profit=` 0, `loss=` 0, `pyramiding` 0, `calc_on_every_tick` 0, `varip` 0, `volume` 0, `heikin` 0, `timeframe.` 0. Series read by order logic: `high`, `low`, `close`, `hl2` plus bar `time` inside the deterministic date window (causal, never future). All `plot`/`plotshape` lines are display-only and never gate an order.

Licence and rights: the canonical page is an open-source publication. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

Pre-write dedup (2026-10-08): working-tree searches for `VLRj2sG9`, `holdon_to_profits`, and case-insensitive `supertrend` return no strategy record using this source or signal — the only `supertrend` hits on `main` are passing mentions inside Related-Wiki/prose lines of unrelated records (`gann-hilo-activator`, `vidya-cmo`, `monday-drift`, `bookstaber-atr`), none of which fires on a SuperTrend band flip. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long, FMZ 451075) and #49 (Gaussian channel StochRSI-gated breakout long, FMZ 482888), plus reconstruction-lane #58 — different mechanisms, indicators, and sources. Five-axis distinction: mechanism differs (volatility-band trailing-stop flip, not MA cross / RSI level / channel breakout), signal construction differs (no pool record evaluates `ta.sma(ta.tr, N)` bands or a `trend == 1 and trend[1] == -1` flip event), exits differ (reverse-flip signal close with zero price-level legs), source identity differs (TV `VLRj2sG9` by holdon_to_profits), and research frame is BTCUSDT `1d` (the page's own display context).

## Economic mechanism

### Source-reported

A volatility-trailing trend rider: the ATR band trails price as a moving stop-and-reversal line, so entries buy the moment the trend state flips bullish and exits admit the trend has failed the moment it flips bearish. The author frames the band itself as the stop (the prose notes a price stop is generally unnecessary because the ATR-based stop is built in), with no fixed target, trailing-percent, or time leg anywhere.

### Research interpretation

Single-state-machine trend following with the state doing all the work. The `trend` variable (1 / -1) is sticky regime state carried bar to bar; the flip edges are the only events that can move the book, and both legs are evaluated on completed bars with same-bar-close fills, so the whole position path is fully determined with no intrabar dependence. No leverage, sizing, or cost edge is embedded in the signal; the declaration carries only event-neutral accounting lines (10000000 capital, 100%-of-equity sizing, 0.015% commission, `currency.NONE`), so the house overlay supplies them (see Execution assumptions).

## Signal

Exact rule as pinned (Pine v6, defaults quoted — inputs unmodified):

- Declaration: `strategy("SuperTrend STRATEGY", overlay=true, initial_capital=10000000, default_qty_type=strategy.percent_of_equity, default_qty_value=100, commission_type=strategy.commission.percent, commission_value=0.015, currency=currency.NONE, process_orders_on_close=true)`. `calc_on_every_tick` is unset (default false); `pyramiding` is unset (language default 0: no additional same-direction entry while positioned — load-bearing here, see Execution assumptions).
- Volatility bands (all deterministic, causal, no variant/smoothing/source choice left open): `atrVal = ta.sma(ta.tr, Periods)` with `Periods = 10` pinned (plain SMA of True Range — the page's stated "more responsive" construction, not Wilder/RMA); `up = src - (Multiplier * atrVal)` and `dn = src + (Multiplier * atrVal)` with `src = hl2` and `Multiplier = 8.5` pinned; trailing locks `up := close[1] > up1 ? math.max(up, up1) : up` and `dn := close[1] < dn1 ? math.min(dn, dn1) : dn` with `nz` first-bar guards (`up1 = nz(up[1], up)`, `dn1 = nz(dn[1], dn)`).
- Trend state machine: `trend = 1` initial, `trend := nz(trend[1], trend)`, then `trend := trend == -1 and close > dn1 ? 1 : trend == 1 and close < up1 ? -1 : trend` (strict comparisons; touching a band without closing through it flips nothing).
- Events: `buySignal = trend == 1 and trend[1] == -1` (bullish flip edge), `sellSignal = trend == -1 and trend[1] == 1` (bearish flip edge). No other bar pattern, threshold, or confirmation gates either event.
- Date window: `FromYear/FromMonth/FromDay = 2020/1/1`, `ToYear/ToMonth/ToDay = 9999/1/1`, `start = timestamp(FromYear, FromMonth, FromDay, 00, 00)`, `finish = timestamp(ToYear, ToMonth, ToDay, 23, 59)`, `window() => time >= start and time <= finish` — deterministic, causal (bar `time` only), true for every bar of the research horizon. Input defaults pinned; altering them would be a different, unpinned rule.
- Entry: `if buySignal and window()` → `strategy.entry("BUY", strategy.long)`. Single long leg; no short entry exists anywhere — the short side is disabled by construction.
- Exit: `if sellSignal and window()` → `strategy.close("BUY")`. Pure reverse-flip signal close — no stop/limit order, no price level, no trailing-percent, no time limit. Every other exit/risk behavior is explicitly none/disabled.
- Direction: long-only, explicitly. Spot-compatible by construction (the author's stated design point).
- Inert code, provably excluded: both `plot` lines and both `plotshape` ("Buy"/"Close" labels) never enter any order condition — toggling display cannot alter any admitted event.

## Required data

- Completed `1d` bars of BTCUSDT: `high`, `low`, `close` (True Range and band comparisons), `hl2` (band source) plus bar `time` for the pinned date window. No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d`. The script takes no timeframe input and makes no live `request.*`/`security(`/`timeframe(` call, so it is single-frame by construction; `1d` is adopted as the research frame because it is the page's own display context (BINANCE BTC-perp 1D) — never presented as anything beyond that (see Limitations).
- Warmup: longest causal chain is `ta.sma(ta.tr, 10)` (first defined at the 10th completed bar) plus the `trend[1]` prior-bar reference. First fully-defined evaluation at the 10th completed `1d` bar; no signal is evaluable before that. No repainting, no negative shift, no future reference, no full-sample normalization. The initial `trend = 1` with the `nz` guard is deterministic: on bar 1 `trend[1]` is `na`, so neither flip edge can fire — no phantom entry is possible.

## Execution assumptions

- Research market: BTCUSDT under the house overlay (the canonical page's own display context was BINANCE BTC-perp 1D and BTC is inside the house universe — never presented as source-native venue semantics; the rule reads candle prices only and is contract-neutral).
- Order timing: the declaration sets `process_orders_on_close = true` with `calc_on_every_tick` unset (default false): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester — and the author's own changelog confirms this was a deliberate fix for next-bar-open drift. No next-bar-open, maker-touch, queue, or intrabar-path-dependent fill.
- Sizing/capital: the declaration's 100%-of-equity sizing, 10000000 initial capital, 0.015% commission, and `currency.NONE` lines are pure event-neutral accounting, replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions, never presented as source-native behavior.
- Concurrency: `pyramiding` is unset (language default 0: no same-direction add while positioned). The default is load-bearing here and therefore pinned explicitly: the bullish `trend == 1` state persists across many bars while long, but no new flip edge can print until a bearish flip closes the position first, so at most one entry per bullish regime is admitted by construction. Re-entry is allowed immediately at the next bullish flip after any reverse-flip close (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The canonical page ships prose plus release notes: long-only spot-friendly framing, ATR Period 10 / hl2 / SMA-of-TR construction notes, 100%-of-equity sizing and commission accounting notes, the customizable-window note, and the `process_orders_on_close` changelog. No numeric performance claim (no ROI, win rate, or trade count) is stated anywhere on the page — this record therefore carries zero source-reported performance figures and claims no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Multiplier prose-vs-code is resolved, not assumed: the current prose block says Multiplier 3.0 but the live published source block says `input.float(8.5, ...)`; an older release note also says 8.5. The same prose block says Initial Capital $10,000 while the code says `initial_capital=10000000` — proving the prose block is stale copy. The admitted value follows the executable on every input (8.5 / 10000000 / 0.015); the stale prose numbers are excluded and named here.
2. Commission prose conflict is accounting-only: notes cite 0.015% (current) and 0.01% (older); both are event-neutral accounting lines replaced by pinned house costs, so the conflict cannot move any trade event.
3. "Stop loss" prose names the band, not an order: 0 `strategy.exit`, 0 `stop=`/`limit=`/`profit=`/`loss=` anywhere in the block, so no price-triggered exit can exist by construction. The reverse-flip `strategy.close` is the only exit path.
4. Boundary ties flip nothing: `close` exactly on a band, and `trend[1]` equality cases, hold state rather than trade — ties never invent an order.
5. Display-code isolation: both `plot` lines and both `plotshape` labels never enter any order condition, so display toggling cannot alter any admitted event.
6. The trend seed is safe: `trend = 1` initial with `nz(trend[1], trend)` means bar 1 cannot print either flip edge (needs `trend[1] == ∓1`, which is `na`), so no position can exist before real causal evaluation.
7. The window inputs are pinned, not removed: moving the 2020-01-01 floor, retuning Periods/Multiplier/source, adding a side, or adding a stop/target/cooldown would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: SMA-of-TR 10 / hl2 / Multiplier 8.5 / flip-edge entry and reverse-flip exit / long-only / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Flip-edge relevance: entering on every bullish-state bar (state-holding instead of edge-triggered, first qualifying bar per regime takes the trade) must not improve net expectancy; fail ⇒ the flip trigger is decorative and the system is a pure regime holder.
- F2 — Reverse-flip exit relevance: holding each entry for a fixed research horizon instead of the bearish-flip close must not improve net expectancy; fail ⇒ the trailing-band exit adds nothing over timed holding.
- F3 — Band-width relevance: the 8.5-multiplier band must show regime-dependent behavior distinct from a naive close-vs-prior-close flip baseline; fail ⇒ the ATR band adds nothing over raw price direction.

## Crypto portability

Pinned to BTCUSDT under the house overlay. The candle-only long-only logic ports to perps or spot without structural change (no short side exists to disable). No funding-dependent leg, no stablecoin-specific assumption, no cross-venue state. Extension to other house-universe assets would be a different, unpinned claim; the source asserts cross-asset generality in prose but names no second market, so no multi-asset claim is admitted.

## Limitations

- Source-frame transfer: the source asserts all-asset/all-timeframe generality but demonstrates only its BTC-perp 1D display context; daily BTC behavior is asserted by the source, not proven to Hermes — backtest evidence stays absent until downstream reproduction.
- Wide-band latency: Multiplier 8.5 builds a very wide envelope, so flips arrive late after sharp reversals and the system can sit through deep adverse excursion with no price stop by construction.
- Whipsaw bleed: in prolonged sideways regimes the band flips repeatedly with no filter, so consecutive full-size round trips are admitted rule behavior, not an implementation artifact.
- Warmup cost: the SMA-10 chain needs 10 completed bars, so the system is blind for the first 10 bars of any evaluation window.

## Implementation status

- `implementation_status: not-implemented`.
- Normalized rule is fully specified above; no Hummingbot/Qlib/n8n/survivor/Paper/Testnet/Live work has been performed or is authorized by this record.

## Adoption boundary

- `adoption: not-approved`, `approval_scope: research-only`, `status: research-only`.
- This record is semantic normalization only. It is not profitability validation, not a survivor promotion, and not Paper/Testnet/Mainnet authorization. Only `hb_ready_status: PASS` records may enter the current Hummingbot/Qlib performance-research downstream, subject to that workflow's own gates.

## Related Wiki records

None.

## Sources

- Primary: https://www.tradingview.com/script/VLRj2sG9-SuperTrend-STRATEGY/ (Strategy by holdon_to_profits, open-source, badge `Updated Feb 11`; page rules, long-only framing, SMA-of-TR construction notes, window note, Feb-11 release history including the `process_orders_on_close` changelog, and BINANCE BTC-perp 1D display context all live-verified 2026-10-08; published Source-code tab read line-for-line this run: 46 lines, `//@version=6`, code governs).
- Pine `strategy()` declaration semantics (first-party reference): https://www.tradingview.com/pine-script-reference/v6/#fun_strategy
- Strategy execution model (broker emulator, `process_orders_on_close`): https://www.tradingview.com/pine-script-docs/concepts/strategies/
