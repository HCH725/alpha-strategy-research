---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: MFI-gated ATR-trailing AlphaTrend reversal long/short on BTCUSDT 4h bars
created: 2026-10-08
updated: 2026-10-08
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: high
source_as_of: 2022-05-30
sources:
  - https://www.tradingview.com/script/jVZbfu5m-AlphaTrend-For-ProfitView/
  - https://github.com/hasnocool/tradingview-pine-scripts/blob/69969aeaf271b2f7b5a7632a1bde43069a0cbe26/AlphaTrend%20For%20ProfitView.pine
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# MFI-gated ATR-trailing AlphaTrend reversal long/short on BTCUSDT 4h bars

## Provenance

Primary source read end to end (TradingView canonical strategy page, live browser read 2026-10-08):

- Canonical page: https://www.tradingview.com/script/jVZbfu5m-AlphaTrend-For-ProfitView/ (`AlphaTrend For ProfitView`, Strategy by treigen, `OPEN-SOURCE SCRIPT`, `Updated May 30, 2022`, adopted as `source_as_of`; release note on the same page: "Add option to only allow longs").
- Page-chart context at read time: BITSTAMP BTC/USD on a 4h chart — a display context, not a strategy rule (the script takes no symbol, timeframe, session, or venue input).
- Page-stated lineage (verbatim substance): "This strategy is based on the AlphaTrend indicator by KivancOzbilgic"; "It is now a backtestable strategy"; "Updated alert trigger logic"; "Easy integration with ProfitView to use this algorithm for automated trading". No performance figure of any kind appears in the page prose (no ROI, no win rate, no trade count) — this record therefore cites zero source-reported performance.
- Live source-code tab verification this run: the published block's declaration (`strategy('AlphaTrend For ProfitView', overlay=true, calc_on_every_tick=true, process_orders_on_close=true, default_qty_type=strategy.percent_of_equity, default_qty_value=100, commission_type=strategy.commission.percent, commission_value=0.1, initial_capital=1000)`), the trailing construction (`upT = low - ATR * coeff`, `downT = high + ATR * coeff`), the coefficient gate (`ta.mfi(hlc3, AP) >= 50`), both signal lines (`buySignalk = ta.crossover(AlphaTrend, AlphaTrend[2])`, `sellSignalk = ta.crossunder(AlphaTrend, AlphaTrend[2])`), the confirmed-bar order gate (`barstate.isconfirmed and timeCond`), and all three order calls (`strategy.entry("Long", strategy.long)`, `strategy.entry("Short", strategy.short, when=canshort)`, `strategy.close("Long", when=not canshort)`) are character-identical to the pinned mirror file below. A live-text census of the published block returns 0 `strategy.exit`, 0 `strategy.order`, 0 `strategy.stop`, 0 `stop=`/`limit=`, 0 `request.*`, 0 `security(`.
- Immutable code provenance: hasnocool mirror file `AlphaTrend For ProfitView.pine` at pinned commit `69969aeaf271b2f7b5a7632a1bde43069a0cbe26` (verified still the remote HEAD via `git ls-remote` this run), blob `7a0b6b24e1db6b392f3afa9da378023c77c9adfe`, 4481 bytes, 117 lines. The mirror header (`Script Name: AlphaTrend For ProfitView`, `Author: treigen`, KivancOzbilgic lineage in Description) matches the canonical page, and the embedded Pine v5 block matches the live page's published Source-code tab on every gate-critical line as read this run (declaration, 1.5/15 inputs, ATR construction, MFI/RSI coefficient gate, ratchet formula, both signal lines, confirmed-bar order block — code governs).

Licence and rights: the canonical page is an open-source publication by treigen (derivative strategy conversion of KivancOzbilgic's indicator, ProfitView alert additions by treigen). This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

Pre-write dedup (2026-10-08): working-tree searches for `alphatrend`, `kivanc`, `KivancOzbilgic`, and `ta.mfi`/`mfi(` return 0 strategy records using this source, author, or signal. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long, FMZ 451075), #49 (Gaussian channel StochRSI-gated breakout long, FMZ 482888), and #63 (SuperTrend ATR-flip trend long, TV VLRj2sG9) — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: #63's SuperTrend flips on `trend == 1 and trend[1] == -1` with `ta.sma(ta.tr, 10)` bands and no volume or momentum coefficient anywhere, while this record fires only on a 2-bar-delayed self-cross `ta.crossover(AlphaTrend, AlphaTrend[2])` of an MFI-volume-gated ratchet (no pool record reads volume through `ta.mfi`, and no pool record crosses any series against its own lag-2); `triple-ema-volstop-tp-long-btcusdt-1d-2026-10-08.md` trails an ATR stop but entries are triple-EMA conjunction breakouts with fixed 4% closes — no trailing-level self-cross signal; `cci-ema-rsi-cross-trailing-stop-btcusdt-1h-2026-10-08.md` is a CCI/EMA/RSI cross system with close-evaluated trailing exits — no ATR ratchet, no MFI, no self-cross. Five-axis distinction: mechanism differs (volume-money-flow-gated ATR ratchet with delayed self-cross reversal, both directions live), signal construction differs (no pool record computes `ta.mfi(hlc3, 15) >= 50` or `ta.crossover(X, X[2])`), exits differ (pure reversal netting plus a long-only-mode close — no threshold close, no price level, no stop order), source identity differs (treigen TV May-2022 `jVZbfu5m` plus hasnocool blob `7a0b6b2`), and research frame is BTCUSDT `4h` (the page's own display context).

## Economic mechanism

### Source-reported

A volatility-adaptive trend-following reversal: the MFI (money-flow) coefficient decides whether buyers or sellers own the tape, and the ATR ratchet then trails the extreme of the dominant side — rising under price in up-moves, pressing down on price in down-moves. A cross of the trail against its own 2-bar-ago value confirms the flip with a delay that filters single-bar whipsaws. The author ships no stop, no target, no trailing order: the opposite flip is the entire risk control. The ProfitView/alert layer is automation plumbing, not signal.

### Research interpretation

Regime ratchet with delayed self-confirmation. The `ta.mfi(hlc3, 15) >= 50` gate is a volume-weighted breadth switch (up-money vs down-money over 15 bars); the `1.5 * ta.sma(ta.tr, 15)` ratchet is sticky state that only advances in the direction of the dominant side, so the trail cannot chase adverse wicks. The `X vs X[2]` cross demands the flip survive two bars before an event prints — a structural whipsaw filter, not a lag accident. Because exits are pure reversal netting evaluated on confirmed bars, the whole book is fully determined by completed bars with no intrabar path dependence. No leverage, sizing, or cost edge is embedded in the signal; the declaration carries only event-neutral accounting lines (1000 capital, 100%-of-equity sizing, 0.1% commission), so the house overlay supplies them (see Execution assumptions).

## Signal

Exact rule as pinned (Pine v5, defaults quoted — inputs unmodified):

- Declaration: `strategy('AlphaTrend For ProfitView', overlay=true, calc_on_every_tick=true, process_orders_on_close=true, default_qty_type=strategy.percent_of_equity, default_qty_value=100, commission_type=strategy.commission.percent, commission_value=0.1, initial_capital=1000)`. `pyramiding` is unset (v5 language default 0: no additional same-direction entry while positioned — corroborated by the `strategy.position_size <= 0` / `>= 0` guards, and load-bearing here, see Execution assumptions). `calc_on_order_fills` is unset (default false).
- `calc_on_every_tick=true` is neutralized by construction: the entire order block sits under `if barstate.isconfirmed and timeCond`, so orders can only be placed on confirmed (completed) bars; intrabar recalculations move no order. Combined with `process_orders_on_close=true`, the admitted semantics is exactly completed-bar decision with same-bar-close execution — no next-bar-open, no intrabar fill.
- Trailing construction (inputs pinned): `coeff = 1.5` (Multiplier), `AP = 15` (Common Period); `ATR = ta.sma(ta.tr, AP)` (explicit SMA-of-TR, not Wilder); `upT = low - ATR * coeff`; `downT = high + ATR * coeff`.
- Coefficient gate (input pinned): `novolumedata = false` (default: volume path live) → the ratchet advances up iff `ta.mfi(hlc3, AP) >= 50`, else presses down. The `ta.rsi(close, AP) >= 50` leg is live code only when a researcher flips `novolumedata` — at pinned defaults it is dead, recorded as such, never admitted.
- Ratchet (exact): `AlphaTrend := (gate) ? (upT < nz(AlphaTrend[1]) ? nz(AlphaTrend[1]) : upT) : (downT > nz(AlphaTrend[1]) ? nz(AlphaTrend[1]) : downT)`. Seed `AlphaTrend = 0.0`; `nz` maps the leading `na` to 0 — deterministic (first down-gated bars hold 0.0 until an up-gate or a sub-zero downT, which cannot print a cross event by itself, see Negative evidence).
- Signals: `buySignalk = ta.crossover(AlphaTrend, AlphaTrend[2])` (strict: trail crosses strictly above its own 2-bar-ago value); `sellSignalk = ta.crossunder(AlphaTrend, AlphaTrend[2])` (strict mirror). Touches without crossing fire nothing.
- Orders (all inside the confirmed-bar gate): `strategy.entry("Long", strategy.long)` when `strategy.position_size <= 0 and buySignalk`; `strategy.entry("Short", strategy.short, when=canshort)` when `strategy.position_size >= 0 and sellSignalk`; `strategy.close("Long", when=not canshort)` on the same sell bar. At the pinned default `canshort = true`, the live behavior is: longs and shorts entered on their respective delayed self-crosses, opposite signals reversing through standard Pine netting (a Short entry while long flattens-then-shorts; no separate close leg needed). The `when=not canshort` close is live only in non-default long-only mode — recorded, not admitted as default behavior.
- Date window: `i_startTime = timestamp("01 Jan 2014 00:00 +0000")`, `i_endTime = timestamp("01 Jan 2100 23:59 +0000")`, `timeCond = (time > i_startTime) and (time < i_endTime)` — deterministic, causal (bar `time` only), true for every bar of the research horizon. Input defaults pinned; altering them would be a different, unpinned rule.
- Direction: both sides live at defaults (`canshort = true`, input pinned). The short side is explicitly enabled, not inferred; long-only mode exists in code but is not the admitted rule.
- Inert code, provably excluded: both `plot` lines plus `k1`/`k2` handles (display only; never read by any order condition); all six `pv_*` inputs and `exsym` (alert-text plumbing only — no `alert_message` on any order call, and `alert()` itself moves no position); `pv_alert_test` block (manual alert preview, no orders); `benchmark`-style logic does not exist in this file (no `security(`, no `request.*`, no second symbol anywhere — verified by full read and live-text census).

## Required data

- Completed `4h` bars of BTCUSDT: `high`/`low`/`close` (ATR ratchet bands), `hlc3` + `volume` (MFI coefficient gate), plus bar `time` for the pinned date window. No `open`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session, or cross-venue state is read by any order-gating line.
- Single decision timeframe `4h`. The script takes no timeframe input and makes no live `request.*`/`security(`/`timeframe(` call, so it is single-frame by construction; `4h` is adopted as the research frame because it is the page's own display context (BITSTAMP BTC/USD 4h) and a campaign timeframe — never presented as anything beyond that (see Limitations).
- Warmup: longest causal chain is `ta.sma(ta.tr, 15)` / `ta.mfi(hlc3, 15)` (first defined at the 15th completed bar) plus the `AlphaTrend[2]` lag and the crossover prior-bar reference. First fully-defined signal evaluation at the 18th completed `4h` bar; no signal is evaluable before that. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT under the house overlay (the canonical page's own display context was BTC/USD 4h and BTC is inside the house universe — never presented as source-native venue semantics; the rule reads OHLCV only).
- Order timing: `process_orders_on_close = true` with the order block further gated by `barstate.isconfirmed`: completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. No next-bar-open, maker-touch, queue, or intrabar-path-dependent fill. `calc_on_every_tick = true` changes nothing about fills — it is fenced off from every order call by the confirmed-bar gate (admitted as written, not smoothed over).
- Sizing/capital: the declaration's 100%-of-equity sizing, 1000 initial capital, and 0.1% commission lines are pure event-neutral accounting, replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions, never presented as source-native behavior.
- Concurrency: `pyramiding` is unset (v5 default 0: no same-direction add while positioned). The default is load-bearing here and therefore pinned explicitly: the ratchet can hold one side for long stretches while fresh same-side self-crosses cannot reprint (a cross is a one-bar event), and the `position_size <= 0` / `>= 0` guards independently block adds. Re-entry is allowed immediately after any reversal whenever the opposite delayed self-cross fires (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The canonical page ships prose plus one release note only: KivancOzbilgic lineage, "backtestable strategy" conversion note, alert/ProfitView plumbing notes, and the "Add option to only allow longs" release note. Zero performance figures appear anywhere in the page prose — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order`, 0 `strategy.stop`, 0 `stop=`/`limit=`/`profit=`/`loss=` in the live published block and the pinned mirror alike — the opposite delayed self-cross (via netting) is the sole exit path by construction, and the prose promises nothing else.
2. `calc_on_every_tick=true` is fenced, not hand-waved: every order call sits inside `if barstate.isconfirmed and timeCond`; Pine evaluates the block for order placement only on the confirmed-bar pass. Intrabar recalculation can repaint the displayed trail mid-bar but cannot place, move, or fill any order. The admitted rule is close-evaluated end to end.
3. Dead RSI leg named: at pinned `novolumedata=false` the `ta.rsi(close, AP) >= 50` branch is unreachable; flipping it would be a different, unpinned rule (a no-volume adaptation), not this record.
4. Dead long-only plumbing named: `strategy.close("Long", when=not canshort)` is inert at the pinned default (`canshort=true`); the admitted default rule reverses via Short entries, never via that close.
5. Seed cannot print a ghost: `AlphaTrend` seeds at 0.0 with `nz` mapping leading `na` to 0; a crossover event additionally requires the trail strictly above its own 2-bar-ago value on a confirmed bar — the seed flatline satisfies no cross by itself.
6. Boundary ties fire nothing: strict `ta.crossover`/`ta.crossunder` (touch without cross), `ta.mfi == 50` failing the `>=` gate on neither side change, `time` exactly on a window edge failing the strict `>`/`<` — ties never invent an order.
7. Display/alert isolation: `plot`/`k1`/`k2`, all `pv_*` inputs, `exsym`, and every `alert()` call never enter any order condition; toggling alerts, exchange/symbol strings, or test-alert mode cannot alter any admitted event.
8. The window and coefficient inputs are pinned, not removed: moving the 2014/2100 bounds, retuning 1.5/15, flipping `novolumedata`/`canshort`, or adding a stop/target/cooldown would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 1.5 multiplier / AP 15 / SMA-of-TR / MFI(hlc3,15)>=50 gate / trail-vs-lag-2 self-cross / both-sides reversal / `4h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Delay relevance: signals on the undelayed flip (`ta.crossover(AlphaTrend, AlphaTrend[1])` semantics) must not improve net expectancy; fail ⇒ the 2-bar confirmation delay is decorative and the system is a plain trail-flip holder.
- F2 — Volume-gate relevance: the ratchet with the MFI gate replaced by a directionless rule (always advance the nearer band) must not improve net expectancy; fail ⇒ the money-flow coefficient adds nothing over a plain ATR trail.
- F3 — Reversal relevance: holding each entry until the opposite delayed self-cross versus exiting at the first adverse trail stall (trail flat for N bars, research-defined) must not improve net expectancy; fail ⇒ pure reversal holding adds nothing over stall exits.

## Crypto portability

Pinned to BTCUSDT under the house overlay. The OHLCV-only long/short logic ports to perps or spot without structural change (short side explicitly enabled at defaults; spot-only deployment would be a different, unpinned claim). No funding-dependent leg, no stablecoin-specific assumption, no session, no cross-venue state. Extension to other house-universe assets or timeframes would be a different, unpinned claim; the BITSTAMP BTC/USD 4h display context is provenance, not an admitted multi-venue claim.

## Limitations

- Source-frame transfer: the source's display context is BITSTAMP BTC/USD 4h (spot, one venue); hourly-4h BTC behavior is asserted by the source's display, not proven to Hermes — backtest evidence stays absent until downstream reproduction.
- Volume dependence: the live coefficient leg is `ta.mfi(hlc3, 15)`, so faithful replay requires point-in-time per-bar volume; a volume-free venue feed would force the unpinned `novolumedata` variant, which is explicitly not this record.
- Warmup cost: the AP-15 chain plus lag-2 self-cross needs ~18 completed bars, so the system is blind for the first ~3 days of any 4h evaluation window and reacts to newborn trends only after the delay confirms.
- Always-in-the-market: at defaults the rule holds a position on every in-window bar (long or short, reversing on flips); sideways chop reverses repeatedly with no flat state and no price stop by construction — adverse excursion has no guardrail beyond the opposite flip.
- Alert plumbing is not execution: ProfitView/alert integration affects live automation messaging only; it changes no backtest event and is relied upon for nothing in this record.

## Implementation status

Not implemented. No Hummingbot controller/executor, no Qlib screening, no Paper/Testnet/Live run has been performed from this record. Admission claims pinned-engine expressibility only (see Execution assumptions), subject to independent six-gate review.

## Adoption boundary

Research-only. Not approved for any downstream screening, parity run, or trading authorization. Only a `PASS` under the live six-gate contract may merge this record into `main`; any `NOT_LOSSLESS` finding closes the PR lane without promotion.

## Related Wiki records

None.

## Sources

- Canonical strategy page (read live 2026-10-08): https://www.tradingview.com/script/jVZbfu5m-AlphaTrend-For-ProfitView/
- Pinned mirror at commit `69969aeaf271b2f7b5a7632a1bde43069a0cbe26`, blob `7a0b6b24e1db6b392f3afa9da378023c77c9adfe`: https://github.com/hasnocool/tradingview-pine-scripts/blob/69969aeaf271b2f7b5a7632a1bde43069a0cbe26/AlphaTrend%20For%20ProfitView.pine
- Lineage indicator by KivancOzbilgic (as cited by the strategy page): https://www.tradingview.com/v/o50NYLAZ/
- Pine v5 strategy semantics (declaration defaults, order calls, confirmed-bar execution): https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
- Pine strategy concepts: https://www.tradingview.com/pine-script-docs/concepts/strategies/
