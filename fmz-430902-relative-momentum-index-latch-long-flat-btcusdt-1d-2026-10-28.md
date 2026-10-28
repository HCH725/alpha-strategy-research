---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "FMZ 430902 Altman RMI-20 40/70 latch BTC-USDT spot 1d long-flat derivative"
created: 2026-10-28
updated: 2026-10-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - fmz
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-28
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/动量反转指数策略Relative-Momentum-Index-Strategy.md
  - https://www.fmz.com/strategy/430902
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Altman RMI-20 40/70 latch — BTC-USDT spot 1d long-flat derivative

## Provenance

- **Primary source (official FMZ mirror, immutable):** `fmzquant/strategies` commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (verified this cycle via GitHub API as the repository's `master` HEAD, committed 2025-04-30), file `动量反转指数策略Relative-Momentum-Index-Strategy.md` (7,325 bytes, fetched raw and read in full this cycle). The file carries the complete Pine v2 program (`//@version=2`, `strategy(title="Relative Momentum Index", shorttitle="RMI")`, `Copyright by HPotter v1.0 19/10/2017`), four inputs with visible defaults (`Length=20`, `BuyZone=40`, `SellZone=70`, `reverse=false`), the exact Wilder-style recursion with `nz()` seeds, the `pos` state latch, the two `strategy.entry` calls, and the venue stanza (`Futures_Binance BTC_USDT`, `period: 2h`, `basePeriod: 15m`, 2023-10-02 to 2023-10-21). Author `ChaoZhang`; `> Detail` links the first-party page below. Only rule tokens are normalized and cited here; no large source block is copied into this repository.
- **First-party page corroboration (no bypass):** https://www.fmz.com/strategy/430902 (HTTP 200 this cycle; title `动量反转指数策略`, author `ChaoZhang`, created 2023-11-02 17:21:45, 1 copy, 1,404 hits). The page's public prose states the identical `xMom/xMU/xMD/RM/RMI` formula and the BuyZone/SellZone long/short semantics. The page gates the full code listing behind login; no login-wall bypass was performed — the verbatim program comes solely from the public immutable mirror above.
- **Declaration-line census on the verbatim program:** 2 `strategy.entry` (`"Long"`/`strategy.long`, `"Short"`/`strategy.short`), 0 `strategy.exit`, 0 `strategy.close`, 0 `strategy.order`, 0 `strategy.cancel`, 0 `stop=`/`limit=`, 0 `pyramiding`, 0 `process_orders_on_close`, 0 `calc_on_every_tick`, 0 `initial_capital`, 0 `default_qty_*`, 0 commission, 0 `request.*`/`security(`, 0 volume/SMA/EMA calls. Display-only `barcolor`/`plot`/`hline` (commented out) are not adopted.
- **Researcher-defined derivative v1, NOT source-native:** preserve the exact Altman RMI(20) recursion, the 40/70 latch, and `reverse=false`, but trade Binance **BTC-USDT spot** UTC **1d** LONG/FLAT with fixed 0.001 BTC, 10,000 USDT cash, hypothetical 0.1% fee per side, Pine-default next-tick semantics adapted to next completed-bar-close MARKET fills, and the source short-latch state reused as the LONG exit (never a short entry). This drops futures margin, 2h multi-timeframe base period, and default-quantity semantics. These choices **materially change** original trade economics.
- **Frozen independent identity:** FMZ:430902|ChaoZhang|HPotter-pinev2|derived-v1-20261028|BinanceSpot-BTC-USDT-UTC1d|RMI20-Buy40-Sell70-reverseOFF|pos-latch-close-only|entry-pos1-level-exit-pos-1-level|t-to-tplus1-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-each-side|warmup60. Any decision-critical alteration creates a new derived version, not a silent update.

## Economic mechanism

### Source-reported

The Relative Momentum Index (Roger Altman) replaces RSI's close-to-close changes with momentum differences against the close `Length` bars ago, smoothed Wilder-style, normalized to 0–100. Readings below `BuyZone` (40) mark oversold (long), above `SellZone` (70) overbought (short); the `pos` latch holds the last extreme through the neutral zone, so the book stays positioned rather than whipsawing mid-range. The page claims RMI reacts earlier than RSI and is less affected by consolidation, while warning that strong trends can overrun entries and that parameters need per-instrument validation. No profitability assertion ships with the file.

### Research interpretation

This derivative holds a long only while the Altman latch sits at `+1` (a completed bar printed RMI below 40 more recently than above 70) and exits to flat when the latch flips to `-1` — a level-based, two-threshold regime hold, not an edge-triggered cross and not a midline exit. It uses no moving average, volume, multi-timeframe, or order-book input. Because the source program contains no stop/target/time leg, an adverse move that never prints an opposite-latch bar leaves the position exposed indefinitely; the only risk control is the opposite-latch close exit. Latch events on daily bars are sparse by construction.

## Signal

1. **Input and availability:** one chronological, contiguous sequence of actual Binance BTC-USDT spot UTC **1d** candles indexed t=0,1,... . Native opening time T[t] must be UTC midnight-aligned and T[t+1]-T[t]=86400 seconds. Require finite positive O,H,L,C, H>=max(O,C), L<=min(O,C); volume is unused and unchecked. Reject duplicates, gaps, out-of-order bars, missing/zero/nonfinite observed close or incomplete candles; never interpolate or forward-fill. Completed bar t is available at E[t]=T[t]+86400, not T[t]. Float64 chronological arithmetic, no intermediate rounding. Only C is consumed by the decision; O/H/L serve validity checks only.
2. **Constants (researcher-pinned to source defaults):** LEN=20, BUY=40.0, SELL=70.0, `reverse=false` pinned (the source `reverse` input would swap sides; it is frozen OFF, not removed silently).
3. **Pine-faithful recursion (all bars, closes only):** `xMom[t]=C[t]-C[t-20]` for t>=20; for t=0..19 the unavailable lag makes `xMom=na`. Define `nz(v,s)` as v when defined, otherwise s. If `xMom>=0`, `xMU=nz(xMU[t-1],1)-nz(xMU[t-1],1)/20+xMom`; otherwise `xMU=nz(xMU[t-1],1)`. If `xMom<=0`, `xMD=nz(xMD[t-1],1)-nz(xMD[t-1],1)/20+abs(xMom)`; otherwise `xMD=nz(xMD[t-1],0)`. The xMD nonpositive-momentum branch uses fallback **1**, whereas its other branch uses fallback **0**; these are distinct literal source defaults. An undefined momentum takes the otherwise branches, so bars t=0..19 hold xMU=1 and xMD=0, not two undefined smoothers. Invalid observed prices abort under rule 1 rather than entering the recursion. `RM[t]=xMU[t]/xMD[t]`; zero xMD yields Pine `na`, never an invented value or an exception. `RMI[t]=100*(RM[t]/(1+RM[t]))`, na-propagating. On a flat tape xMU remains positive (decaying by 19/20 from t=20), xMD stays zero, and RMI remains na; this is positive/zero, not 0/0.
4. **Latch `pos[t]`:** `RMI[t]<40.0` → `1`; else `RMI[t]>70.0` → `-1`; else hold `pos[t-1]` (seed `0`, the source `nz(pos[1],0)`). Strict inequalities: `RMI==40.0` or `==70.0` fires nothing. `na` RMI holds. `pos` takes values in `{-1,0,1}` only; `+1`/`-1` are mutually exclusive by single-value construction.
5. **Warmup:** bars t=0..59 are **60 completed-bar no-trade warmup** (researcher-declared, 3× Length; covers the 20-bar momentum seed plus Wilder-seed transient). First eligible decision is t=60.
6. **Entry:** when FLAT with no pending action, t>=60, t strictly later than the last SELL-fill bar, and `pos[t]==1` (level-based, faithful to the source `if (possig == 1) strategy.entry("Long")` under default pyramiding=0), queue exactly one BUY. Dispatch on row t+1 only, independently of that row's signal, and model a full 0.001 BTC MARKET fill at its **actual observed completed close** C[t+1], effective E[t+1]. No t+1 price or indicator is used to decide at t. If row t+1 does not exist, leave unfilled. Require cash >=Decimal("0.001")*Decimal(str(C[t+1]))*(1+Decimal("0.001")); insufficient funds or ambiguous/missing fill aborts rather than assuming borrowing.
7. **Exit:** when confirmed LONG and no pending action, on the first eligible completed bar u after the BUY-fill bar with `pos[u]==-1` (the source short-latch state, reused as the LONG exit only — never a short entry), queue a full 0.001 BTC SELL for row u+1 at actual observed C[u+1], effective E[u+1]. No stop, target, trailing, time exit, or protective intrabar order exists in source; all are expressly disabled, not hidden defaults.
8. **State and priority:** exactly FLAT, BUY_PENDING, LONG, SELL_PENDING; one position and one pending action maximum. `pos` is single-valued so entry and exit levels can never co-fire on one bar; no tie-break is needed. Source default pyramiding=0 gives a single unit with no adds. On a pending/fill bar ignore new order signals but keep the latch updating. On confirmed SELL, return to FLAT using the independent confirmed-fill inventory ledger and record last SELL-fill bar. Re-entry requires FLAT plus `pos==1` on a future bar (no cooldown). Never BUY and SELL on the same bar. If a fill fails, is partial, duplicated, stale or cannot be reconciled, abort the segment. At sample end, an unfilled pending signal remains unfilled; open inventory is marked only to the last actual completed close and not fictitiously liquidated.
9. **Disabled:** Pine next-tick-open order semantics, futures leverage/margin, default quantity semantics, the `reverse=true` side-swap, short/borrow leg (no short entry exists in this derivative), stops/targets/trailing/time exits, pyramiding, DCA/safety orders, simultaneous markets/shared capital, partial exits, dynamic sizing/compounding, limit/maker fills, intrabar triggers, the 2h/`basePeriod: 15m` multi-timeframe stanza, discretionary overrides, hidden executor risk defaults and forced end-of-sample close.

## Required data

Only one real Binance BTC-USDT spot 1d OHLC feed, no fitted models, external symbols, cross-asset shared capital, funding, order book, non-OHLCV features, second timeframe or future extrema. All decision inputs at t are C[t], C[t-20] and recursive smoother/latch state from bars <=t completed by E[t]. A strict input validity and continuity check must precede the pinned engine's feature merge/dropna; if data cannot satisfy it, fail closed. Native Binance kline timestamp is the **open** time, never the completed-close availability or economic fill time.

## Execution assumptions

**Pinned source-code benchmark inspected at HCH725/hummingbot commit 8b0e067e80ab62f10846d518dcb5a8218527ddb3 on 2026-10-28 (read from the pinned tree this round):** package label **20260920**, `hummingbot/VERSION` = **dev-2.17.0**. Tree-verified sizes (993 / 3,924 / 39,071 / 8,823 / 3,913 bytes) match prior independent review; raw contents re-verified this round.

- **Data:** pinned `BinanceSpotCandles` constants declare the **1d** interval and read Binance REST `/api/v3/klines` opening timestamp plus actual OHLCV. Strict full-bar availability/continuity must be enforced before any feature dropna; a missing price is never substituted.
- **Controller/action path:** `BacktestingEngineBase.simulate_execution` iterates completed rows, calls `update_state(row)`, then `controller.determine_executor_actions()`, simulating CreateExecutorAction. A future minimal candidate-specific controller (not yet materialized) must retain the RMI smoother/latch state and FLAT/LONG/pending state and send the precommitted t signal on t+1 via OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY or SELL,amount=Decimal("0.001"),position_action=OPEN or CLOSE,execution_strategy=MARKET,price=None,leverage=1). The presence of this API is **not** alone the compatibility proof.
- **Observed fill primitive:** pinned OrderExecutorSimulator MARKET path fills at the first supplied candle with entry price taken from that row's actual close (`entry_price = df_filtered.loc[fill_timestamp, 'close']`), not a fabricated price, computes float(amount)*entry_price as filled quote and trade_cost*quote as fee, then returns CloseType.POSITION_HOLD. Dispatch at t+1 produces the declared idealized t+1 completed-close fill. It is not an achievable post-close live order guarantee; economic timestamp is E[t+1], even though native row timestamp is T[t+1].
- **Position and economics:** BacktestPositionHold aggregates BUY/SELL gross exposure and fees separately; native gross realized PnL is not net research PnL. Keep complete confirmed-executor history (terminated_executors_window=None or equivalent; the pinned default is only 3600 seconds) and a separate Decimal research cash/inventory ledger independent of BacktestPositionHold.is_closed. Start cash=10000 USDT, BTC=0; each confirmed BUY: cash -= Q*P*(1+f), inventory +=Q; each confirmed SELL: cash +=Q*P*(1-f), inventory -=Q, with Q=Decimal("0.001") and f=Decimal("0.001"). Net roundtrip realized =Q*(Ps-Pb)-f*Q*(Pb+Ps); record fees separately. This **0.1% quote-notional fee per side is hypothetical**, not a verified Binance fee tier; spot funding is not applicable, not invented perpetual funding=0. No compounding.
- **Float/Decimal precision boundary:** native simulator computes quote in float; BacktestPositionHold re-derives base quantity from Decimal(quote)/price and checks net_amount_base==0 exactly. Opposite equal configured amounts can leave sub-atomic dust; its is_closed flag and positions_held are **not** used as the derivative's authoritative FLAT/LONG or cash ledger. Confirmed OrderExecutorConfig amount and full-fill evidence determine exact research inventory Q; compare engine-derived residual to expected inventory only diagnostically with absolute tolerance 1e-12 BTC and abort if greater. This tolerance is a **researcher-declared diagnostic**, not an engine patch, live lot precision, or silent rounding of an order. Earlier independently reviewed Alpha PRs #519/#529/#530 record bounded synthetic primitive exercises at Q0.001, fee 0.001 and 1e-12 diagnostic tolerance; this record reuses that bounded pure-research primitive. No candidate-specific backtest or new primitive test is claimed here.
- **Pure-research precision contract:** deliberately no exchange lot/tick/min-notional/available-live-balance acceptance gating is claimed. This is an idealized fixed-quantity historical model, not an exchange-acceptable order assertion. Exchange trading rules, liquidity, spread, actual slippage, live fee tiers and real fills are out of scope; they must be independently verified before any deployment. The engine's BacktestingDataProvider.get_price_by_type fallback Decimal("1") on missing prices (line 140, re-verified this round) is **forbidden**; missing/nonpositive actual close, ambiguous full-fill, unbounded dust or incomplete fee/position ledger aborts the research segment.

## Evidence

### Source-reported

Official FMZ mirror file at `fmzquant/strategies@7853bb2` (immutable, read in full): Altman RMI with `xMom=C-C[20]`, Wilder-style `xMU/xMD` recursion with xMU `nz` default 1 and branch-specific xMD defaults 1 (nonpositive momentum) / 0 (otherwise), `RMI=100*(RM/(1+RM))`, latch `pos` at 40/70 with `nz(pos[1],0)` seed, `reverse=false` default, two `strategy.entry` calls and no exit/stop/order leg, `Futures_Binance BTC_USDT 2h` stanza. First-party page prose corroborates the formula and thresholds. No sizing, warmup-cause, cost model, or profitability claim exists in the source file; all such settings here are researcher-declared.

### Independently reproduced

No strategy backtest, Pine event parity, realized market fills, profits, Qlib parity, OOS, Survivor or HB Certified results. This cycle directly inspected the verbatim Pine v2 source in the immutable mirror plus the immutable pinned Hummingbot feed/controller/action/MARKET/POSITION_HOLD/fee source paths, and reused prior independent primitive evidence (#519/#529/#530), not a candidate-specific test or installed-binary hash. Prior primitive validation does not imply that an unimplemented dedicated controller already exists.

- **Rule-logic self-check (stdlib only, not a backtest):** the frozen recursion/latch plus the FLAT/LONG state machine were executed over hand-constructed boundary cases and 5,000 seeded random walks — all pass: threshold-equality (`RMI==40.0`, `RMI==70.0`) fires nothing; `na` (zero-width/div0) RMI holds; flat-price tapes stay at latch 0 crash-free; warmup bars 0–59 stay silent; latch domain is exactly `{-1,0,1}`; identical inputs give identical outputs. Fuzz legs: entry-latch reachable in 3,393/5,000 walks, exit-latch in 2,858/5,000 — both legs provably reachable. A monotonic-crash-then-moon tape latches `+1` then `-1` in order.
- **Rule computability on real public data (availability check, not a backtest — no PnL, no returns computed):** 1,999 fully completed Binance BTCUSDT spot `1d` bars (2021-05-08 → 2026-10-27; the still-forming 2026-10-28 candle excluded) verified contiguous at exact 86400-second open steps with zero invalid OHLC bars; post-warmup evaluation yields 2 entry-latch bars and 3 exit-latch bars under the frozen rules. Worked latches: EXIT 2021-10-19 (C 64280.59, RMI 70.9316), ENTRY 2022-05-16 (C 29874.01, RMI 39.7493), EXIT 2023-01-27 (C 23074.16, RMI 70.0345), ENTRY 2025-11-16 (C 94261.44, RMI 38.0554), EXIT 2026-08-29 (C 78230.00, RMI 70.3143). Terminal latch is the exit side (last RMI 69.8816) — no long held at the sample end. The candidate's trade events, Qlib/Hummingbot parity, and net returns have **not** been independently reproduced. No backtest was executed.

### Six-gate proposed PASS — independent Hermes Auditor decides

1. **Determinism:** Altman RMI(20) recursion with literal `nz` seeds, fixed 40/70 thresholds, pinned `reverse=false`, ordered latch comparisons with strict inequalities, warmup and priority.
2. **Direction:** BTC-USDT spot LONG/FLAT; the source short-latch state is reused as the exit only and no short entry exists in this derivative.
3. **Entry/exit/risk:** level-based `pos==1` BUY, level-based `pos==-1` SELL; no source stop/target/trailing/time leg exists and all hidden defaults are expressly disabled (zero stop/order/exit census).
4. **Position:** cash10000/Q0.001/fee0.001, single pending and inventory ledger, fail-closed fill reconciliation, re-entry only on a future bar while FLAT, no DCA or concurrency.
5. **Pinned compatibility:** actual 1d Binance spot feed, controller/action/next-row MARKET actual close, POSITION_HOLD gross-plus-fees and independently declared Decimal net ledger, pure-research precision/dust boundary; no unsupported next-open, intrabar, MTF or futures funding claim.
6. **Causality:** t>=60 completed-bar decision on C[t]/C[t-20] plus recursive state from bars <=t, t+1 completed-close fill effective E[t+1], opening timestamp not mistaken for completed data, no future leakage or synthetic prices.

**Dedup:** current main at `a329033` has 398 root strategy Markdown records (README pool count 398, verified equal); full-tree grep for `430902`, `altman`, `relative-momentum`, `relative momentum index`, `BuyZone`, `xMom`, `shorttitle=.RMI.` returns zero same-source hits (the sole `momentum-index` substring hit is `imi-50-midline-cross`, the Intraday Momentum Index — open/close-ratio construction, a different oscillator family). Nearest pool relatives trade different objects: `cumulative-rsi-dual-threshold` (close-to-close RSI accumulation), `forven-connors-rsi-oversold-recross` (Connors RSI), `double-seven-connors-pullback` (Connors pullback), `forven-rsi-*` (plain-RSI gates) — none is an Altman momentum-difference (C vs C[20]) Wilder-smoothed 40/70 latch. All ten open research/* PR titles were checked (#353 Heracles KCD, #350 ClucMay72018, #331 AdxSmas, #304 forven CCI, #251 Swift 2yMA, #92 SSL channel, #89 Chandelier Exit, #63 SuperTrend flip, #49 Gauss StochRSI, #48 Larry Williams streak); none is FMZ-sourced or RMI-based. Existing root records were not re-audited individually in this Scout; the 398/398 count census plus the merged-base diff shows only reviewed PASS additions and README bookkeeping, with no other strategy changes.

## Falsification plan

With separate authorization only, materialize the minimal candidate-specific controller and test the `nz`-seed first bars, the `xMD==0` division hold, flat-tape silence, the exact 40.0/70.0 boundary routing, latch memory through long neutral stretches, level-based re-entry after an exit while the latch still reads `+1`, warmup-edge suppression at bars 59/60, pending-bar gate freezes, exact t/t+1 timing, observed prices, quote fees, separate Decimal inventory, float residual tolerance and end-of-sample treatment. Before large-scale Qlib screening of any new execution path, obtain representative event-level Hummingbot/Qlib parity. No such execution, deployment or backtest occurs in this Scout.

## Crypto portability

Native venue is already BTC-USDT (FMZ stanza Futures_Binance); this derivative moves only the venue leg to Binance spot 1d with no leverage or funding. No asset substitution is made. Porting the RMI(20) 40/70 latch to other spot symbols would be a new derived version with its own evidence, not covered by this record.

## Limitations

Verbatim code comes from the FMZ organization's public immutable mirror at a pinned commit (byte-inspected this round: 7,325 bytes, md5 `7bb44761f7b970bb9f9035bddececc18`); the live first-party page corroborates identity and formula but gates its code listing, and no login-wall bypass was performed. The pure-research close/full-fill/fee model is not a real exchange acceptance or executable strategy implementation. Latch exits are bars late by construction and the book has no protective stop; latch events are sparse (5 transitions per ~2,000 daily bars in the availability check; both legs proven reachable in fuzz and on real data). No performance, survivor, live or Qlib parity claims.

## Implementation status

**implementation_status: not-implemented** — research record only. **status: research-only; adoption: not-approved; approval_scope: research-only.** The proposed PASS is not self-approval: independent Hermes Auditor GitHub Webhook Review alone owns source-fact review, exact-head PASS merge or NOT_LOSSLESS close. The existing signed webhook receiver alone owns post-merge README bookkeeping. This Scout does not approve, merge, close, modify main or change any trading/backtest/cron system.

## Adoption boundary

Research-only. Not approved for Paper, Testnet, Live, Qlib mass screening, or any deployment. Downstream use requires the independent PASS review plus separate implementation and authorization steps outside this record.

## Related Wiki records

None created by this Scout.

## Sources

- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/动量反转指数策略Relative-Momentum-Index-Strategy.md — FMZ-organization immutable mirror carrying the verbatim Pine v2 RMI program (inputs, recursion, latch, entries, venue stanza), inspected 2026-10-28.
- https://www.fmz.com/strategy/430902 — ChaoZhang, first-party public page (identity/formula/threshold corroboration), inspected 2026-10-28.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — immutable pinned engine paths inspected via the pinned tree this round.
- https://github.com/HCH725/alpha-strategy-research/pull/519 — prior independent bounded MARKET/POSITION_HOLD synthetic primitive review.
- https://github.com/HCH725/alpha-strategy-research/pull/529 — prior independent bounded pure-research execution and PASS-only census evidence.
- https://github.com/HCH725/alpha-strategy-research/pull/530 — prior independent PASS census evidence.
