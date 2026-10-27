---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "FMZ 501679 Livermore six-state pivot trend BTC-USDT spot 1d long-flat derivative"
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
  - https://www.fmz.com/strategy/501679
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Page prose describes 'six market trend states'; the verbatim code declares seven enum constants (NONE=0 plus six named states). Code governs; prose is fenced as source-reported only."
  - "Page prose suggests adding stop-loss, short-selling and dynamic-parameter enhancements as future improvements. None of those exist in the verbatim code and none is adopted here; the page itself lists 'Lack of Stop-Loss Mechanism' as a current risk."
  - "The FMZ backtest stanza pins Futures_Binance BTC_USDT 1d (2024-07-16 to 2025-07-12 window, balance 200000) as provenance only; this record adapts venue to Binance spot with fixed 0.001 BTC sizing. No lossless cross-venue equivalence is claimed."
---

# Livermore six-state pivot trend — BTC-USDT spot 1d long-flat derivative

## Provenance

**FMZ primary source:** ianzeng123, *Livermore Key Pivot Breakout Quantitative Long Strategy*, FMZ numeric ID **501679**, first-party page https://www.fmz.com/strategy/501679 . Inspected 2026-10-28: HTTP 200, ~745,301 bytes, author ianzeng123, created 2025-07-16, backtest stanza `start: 2024-07-16, end: 2025-07-12, period: 1d, basePeriod: 1d, Futures_Binance BTC_USDT, balance 200000`. The complete Pine v6 program is embedded verbatim in the page's public `source` field (no login needed for the embedded field): `//@version=6`, `strategy("Trading strategy Jesse Livermore", overlay=true)` (MPL-2.0, `// © bozhang_ox`), six inputs with visible defaults (`pivot_distance_percentage=0.5`, `major_pivot_multiplier=6`, `minor_pivot_multiplier=3`, `use_atr_pivot_distance=false`, `atr_period=14`, `atr_pivot_multiplier=1`), the full seven-state transition ladder, and the `strategy.entry("Long Entry", strategy.long)` / `strategy.close("Long Entry")` decision block. Declaration-line census on the verbatim text: no `pyramiding`, `process_orders_on_close`, `calc_on_every_tick`, `initial_capital`, `default_qty_*` or commission. Body census: 1 `strategy.entry`, 1 `strategy.close`, 0 `strategy.short`, 0 `strategy.exit`, 0 `strategy.order`, 0 `strategy.cancel`, 0 `stop=`/`limit=`, 0 `crossover`/`crossunder`, 0 `request.*`/`security(`, no volume, no SMA/EMA calls. Only large-scale rule tokens are normalized and cited here; no large source block is copied into this repository.

**Researcher-defined derivative v1, NOT source-native:** preserve the exact seven-state close-vs-close pivot machine, the 0.5%/6x/3x thresholds with the ATR branch pinned OFF, and the two-bar MAIN_UP/MAIN_DOWN confirmation decision, but trade Binance **BTC-USDT spot** UTC **1d** LONG/FLAT with fixed 0.001 BTC, 10,000 USDT cash, hypothetical 0.1% fee per side, and completed-bar signal to next completed-bar-close MARKET fills. This drops Pine-default next-bar-open semantics, futures margin, and default quantity semantics. These choices **materially change** original trade economics. The `ta.atr(14)` computation exists in source but is dead code under the pinned `use_atr_pivot_distance=false` default (ratio is the constant 0.005); it is declared disabled, not removed silently.

**Frozen independent identity:** FMZ:501679|ianzeng123|bozhang_ox-pinev6|derived-v1-20261028|BinanceSpot-BTC-USDT-UTC1d|pivot0.5pct-major6-minor3-atrOFF|7state-close-only|entry-2bar-MAINUP-exit-2bar-MAINDOWN|t-to-tplus1-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-each-side|warmup30. Any decision-critical alteration creates a new derived version, not a silent update.

## Economic mechanism

A Livermore-style trend-classification machine partitions every close into one of six named regimes (plus NONE at startup) using only the current close, the prior close, running major/minor extrema, and two fixed percentage-of-prior-close distances (3.0% major, 1.5% minor). A long position is held only while the machine confirms a major uptrend across two consecutive bars; a confirmed major downtrend closes it. This tests whether a discrete multi-state pivot taxonomy filters whipsaws better than a single-threshold trend flip. It is a regime taxonomy, not a price-level breakout: no highest/lowest channel, band, or moving-average level is traded. No profitability assertion is made; regime exits arrive bars late by construction and the book carries no protective stop (the source page states this risk explicitly).

## Signal

1. **Input and availability:** one chronological, contiguous sequence of actual Binance BTC-USDT spot UTC **1d** candles indexed t=0,1,... . Native opening time T[t] must be UTC midnight-aligned and T[t+1]-T[t]=86400 seconds. Require finite positive O,H,L,C, H>=max(O,C), L<=min(O,C), and finite nonnegative base volume V. Reject duplicates, gaps, out-of-order bars, missing/zero/nonfinite observed close or incomplete candles; never interpolate or forward-fill. Completed bar t is available at E[t]=T[t]+86400, not T[t]. Use float64 chronological arithmetic with no intermediate rounding. Only C is consumed by the decision; O/H/L/V serve validity checks only.
2. **Constants (researcher-pinned to source defaults):** PIV=0.005, MAJ=6, MIN=3, ATR branch OFF. Major distance D1[t]=C[t-1]*PIV*MAJ (3.0% of prior close); minor distance D2[t]=C[t-1]*PIV*MIN (1.5% of prior close).
3. **States:** NONE=0, MAIN_DOWN=1, NATURAL_REBOUND=2, SECONDARY_RETRACEMENT=3, SECONDARY_REBOUND=4, NATURAL_RETRACEMENT=5, MAIN_UP=6. State variables S[t], P1[t]=S[t-1], P2[t]=S[t-2]; running extrema Umax (main_up_max, init -1e10), Dmin (main_down_min, init 1e10), Rmax (natural_rebound_max, init -1e10), Rmin (natural_retracement_min, init 1e10), exactly per source `na()`-init semantics.
4. **Transitions (evaluated in source order, t>=1):** NONE: C[t]>C[t-1] -> MAIN_UP (Umax=C[t]), else MAIN_DOWN (Dmin=C[t]). MAIN_UP: C[t]>C[t-1] or (Umax-C[t]<D1[t]) -> stay MAIN_UP (Umax=max), else NATURAL_RETRACEMENT (Rmin=C[t]). MAIN_DOWN: C[t]<C[t-1] or (C[t]-Dmin<D1[t]) -> stay MAIN_DOWN (Dmin=min), else NATURAL_REBOUND (Rmax=C[t]). NATURAL_REBOUND: if C[t]>C[t-1]: if C[t]<=Umax: (C[t]-Rmax<=D2[t]) ? stay (Rmax=max) : MAIN_UP (Umax=C[t]); else MAIN_UP (Umax=C[t]); else: (Rmax-C[t]<=D1[t]) ? stay : (C[t]<Rmin ? NATURAL_RETRACEMENT (Rmin=C[t]) : SECONDARY_RETRACEMENT). NATURAL_RETRACEMENT is the exact mirror (down/UP, min/Rmax-Rmin roles swapped, terminal SECONDARY_REBOUND). SECONDARY_REBOUND: inside [Rmin,Rmax] -> stay; C[t]<Rmin -> NATURAL_RETRACEMENT (Rmin=C[t]); else NATURAL_REBOUND (Rmax=C[t]). SECONDARY_RETRACEMENT is the mirror. All comparisons are strict `>`/`<` with stated `<=`/`>=` only where the source writes them; equality therefore routes deterministically with no tie-break needed.
5. **Warmup:** bars t=0..29 are **30 completed-bar no-trade warmup** (researcher-declared; sidesteps bar-0 `close[1]` na semantics and lets recursive extrema settle). First eligible decision is t=30.
6. **Entry:** when FLAT with no pending action, t>=30, t strictly later than the last SELL-fill bar, and P1[t]!=P2[t] and S[t]==MAIN_UP and P1[t]==MAIN_UP (i.e. the second consecutive MAIN_UP bar after a change), queue exactly one BUY. Dispatch on row t+1 only, independently of that row's signal, and model a full 0.001 BTC MARKET fill at its **actual observed completed close** C[t+1], effective E[t+1]. No t+1 price or indicator is used to decide at t. If row t+1 does not exist, leave unfilled. Require cash >=Decimal("0.001")*Decimal(str(C[t+1]))*(1+Decimal("0.001")); insufficient funds or ambiguous/missing fill aborts rather than assuming borrowing.
7. **Exit:** when confirmed LONG and no pending action, on the first eligible completed bar u after the BUY-fill bar with P1[u]!=P2[u] and S[u]==MAIN_DOWN and P1[u]==MAIN_DOWN, queue a full 0.001 BTC SELL for row u+1 at actual observed C[u+1], effective E[u+1]. No stop, target, trailing, time exit, or protective intrabar order exists in source; all are expressly disabled, not hidden defaults. The page's suggested stop-loss/short/dynamic-parameter add-ons are explicitly NOT adopted.
8. **State and priority:** exactly FLAT, BUY_PENDING, LONG, SELL_PENDING; one position and one pending action maximum. The source `if/else if` makes entry and exit mutually exclusive on the same bar, so no tie-break is needed. Source default pyramiding=0 gives a single unit with no adds. On a pending/fill bar ignore new order signals but continue updating states/extrema. On confirmed SELL, return to FLAT using the independent confirmed-fill inventory ledger and record last SELL-fill bar. Re-entry requires a fresh two-bar MAIN_UP confirmation while FLAT (no cooldown). Never BUY and SELL on the same bar. If a fill fails, is partial, duplicated, stale or cannot be reconciled, abort the segment. At sample end, an unfilled pending signal remains unfilled; open inventory is marked only to the last actual completed close and not fictitiously liquidated.
9. **Disabled:** Pine next-bar-open order semantics, futures leverage/margin, default quantity semantics, the ATR-distance branch (`use_atr_pivot_distance=false` pinned; `atr_period`/`atr_pivot_multiplier` inert), short/borrow leg (none exists in source), stops/targets/trailing/time exits, suggested add-on filters, pyramiding, DCA/safety orders, simultaneous markets/shared capital, partial exits, dynamic sizing/compounding, limit/maker fills, intrabar triggers, discretionary overrides, hidden executor risk defaults and forced end-of-sample close.

## Required data

Only one real Binance BTC-USDT spot 1d OHLCV feed, no fitted models, external symbols, cross-asset shared capital, funding, order book, non-OHLCV features, second timeframe or future extrema. All decision inputs at t are C[t], C[t-1] and recursive state/extrema from bars <=t completed by E[t]. A strict input validity and continuity check must precede the pinned engine's feature merge/dropna; if data cannot satisfy it, fail closed. Native Binance kline timestamp is the **open** time, never the completed-close availability or economic fill time.

## Execution assumptions

**Pinned source-code benchmark inspected via immutable raw files at HCH725/hummingbot commit 8b0e067e80ab62f10846d518dcb5a8218527ddb3 on 2026-10-28:** package label **20260920**, `hummingbot/VERSION` = **dev-2.17.0**. Tree-verified sizes (993 / 3,924 / 39,071 / 8,823 / 3,913 bytes) match prior independent review; raw contents re-verified this round.

- **Data:** pinned `BinanceSpotCandles` constants declare the **1d** interval and read Binance REST `/api/v3/klines` opening timestamp plus actual OHLCV. Strict full-bar availability/continuity must be enforced before any feature dropna; a missing price is never substituted.
- **Controller/action path:** `BacktestingEngineBase.simulate_execution` iterates completed rows, calls `update_state(row)`, then `controller.determine_executor_actions()`, simulating CreateExecutorAction. A future minimal candidate-specific controller (not yet materialized) must retain the seven-state/extrema state and FLAT/LONG/pending state and send the precommitted t signal on t+1 via OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY or SELL,amount=Decimal("0.001"),position_action=OPEN or CLOSE,execution_strategy=MARKET,price=None,leverage=1). The presence of this API is **not** alone the compatibility proof.
- **Observed fill primitive:** pinned OrderExecutorSimulator MARKET path fills at the first supplied candle with entry price taken from that row's actual close (`entry_price = df_filtered.loc[fill_timestamp, 'close']`), not a fabricated price, computes float(amount)*entry_price as filled quote and trade_cost*quote as fee, then returns CloseType.POSITION_HOLD. Dispatch at t+1 produces the declared idealized t+1 completed-close fill. It is not an achievable post-close live order guarantee; economic timestamp is E[t+1], even though native row timestamp is T[t+1].
- **Position and economics:** BacktestPositionHold aggregates BUY/SELL gross exposure and fees separately; native gross realized PnL is not net research PnL. Keep complete confirmed-executor history (terminated_executors_window=None or equivalent) and a separate Decimal research cash/inventory ledger independent of BacktestPositionHold.is_closed. Start cash=10000 USDT, BTC=0; each confirmed BUY: cash -= Q*P*(1+f), inventory +=Q; each confirmed SELL: cash +=Q*P*(1-f), inventory -=Q, with Q=Decimal("0.001") and f=Decimal("0.001"). Net roundtrip realized =Q*(Ps-Pb)-f*Q*(Pb+Ps); record fees separately. This **0.1% quote-notional fee per side is hypothetical**, not a verified Binance fee tier; spot funding is not applicable, not invented perpetual funding=0. No compounding.
- **Float/Decimal precision boundary:** native simulator computes quote in float; BacktestPositionHold re-derives base quantity from Decimal(quote)/price and checks net_amount_base==0 exactly. Opposite equal configured amounts can leave sub-atomic dust; its is_closed flag and positions_held are **not** used as the derivative's authoritative FLAT/LONG or cash ledger. Confirmed OrderExecutorConfig amount and full-fill evidence determine exact research inventory Q; compare engine-derived residual to expected inventory only diagnostically with absolute tolerance 1e-12 BTC and abort if greater. This tolerance is a **researcher-declared diagnostic**, not an engine patch, live lot precision, or silent rounding of an order. Earlier independently reviewed Alpha PRs #519/#529/#530 record bounded synthetic primitive exercises at Q0.001, fee 0.001 and 1e-12 diagnostic tolerance; this record reuses that bounded pure-research primitive. No candidate-specific backtest or new primitive test is claimed here.
- **Pure-research precision contract:** deliberately no exchange lot/tick/min-notional/available-live-balance acceptance gating is claimed. This is an idealized fixed-quantity historical model, not an exchange-acceptable order assertion. Exchange trading rules, liquidity, spread, actual slippage, live fee tiers and real fills are out of scope; they must be independently verified before any deployment. The engine's BacktestingDataProvider.get_price_by_type fallback Decimal("1") on missing prices (line 140, re-verified this round) is **forbidden**; missing/nonpositive actual close, ambiguous full-fill, unbounded dust or incomplete fee/position ledger aborts the research segment.

## Evidence

### Source-reported

FMZ page prose (Livermore philosophy narrative, six-state summary, suggested stop-loss/short/dynamic-parameter improvements, 2024-07-16 to 2025-07-12 Futures_Binance backtest stanza) is fenced as unverified vendor description on a different venue and sizing regime. It is **not** adopted as evidence for this BTC-USDT spot derivative. The page's own risk section ("Lack of Stop-Loss Mechanism") is adopted only as provenance that no protective leg exists in source.

### Independently reproduced

No strategy backtest, Pine event parity, realized market fills, profits, Qlib parity, OOS, Survivor or HB Certified results. This cycle directly inspected the embedded verbatim Pine v6 source on the public FMZ page plus the immutable pinned Hummingbot feed/controller/action/MARKET/POSITION_HOLD/fee source paths, and reused prior independent primitive evidence (#519/#529/#530), not a candidate-specific test or installed-binary hash. Prior primitive validation does not imply that an unimplemented dedicated controller already exists.

### Six-gate proposed PASS — independent Hermes Auditor decides

1. **Determinism:** seven-state machine with literal enum values, fixed 0.5%/6x/3x thresholds, pinned ATR-OFF default, ordered transitions with stated strict/non-strict comparisons, running-extrema init values, two-bar confirmation rule, float64, warmup and priority.
2. **Direction:** BTC-USDT spot LONG/FLAT; no short leg exists in source and none is added; source is pure-long so no side needs disabling.
3. **Entry/exit/risk:** two-bar MAIN_UP BUY, two-bar MAIN_DOWN SELL; no source stop/target/trailing/time leg exists and all hidden defaults are expressly disabled, with the page's own no-stop-loss admission cited.
4. **Position:** cash10000/Q0.001/fee0.001, single pending and inventory ledger, fail-closed fill reconciliation, re-entry only on fresh confirmation, no DCA or concurrency.
5. **Pinned compatibility:** actual 1d Binance spot feed, controller/action/next-row MARKET actual close, POSITION_HOLD gross-plus-fees and independently declared Decimal net ledger, pure-research precision/dust boundary; no unsupported next-open, intrabar, MTF or futures funding claim.
6. **Causality:** t>=30 completed-bar decision on C[t]/C[t-1] plus recursive state from bars <=t, t+1 completed-close fill effective E[t+1], opening timestamp not mistaken for completed data, no future leakage or synthetic prices.

**Dedup:** current main at 8f03b31 has 390 root strategy Markdown records (README pool count 390, verified equal); full-tree grep for `501679`, `livermore`, `jesse`, `MAIN_UP`, `main_up_max`, `secondary_rebound` and `six-state` returns zero same-source hits. Nearest pool relatives trade different objects: pivot-point-breakout-kaufman (price-level breakout), forven-pivot-s1-bounce-r1-exit (S1 bounce/R1 exit levels), camarilla-r1-s1-rail-cross (Camarilla rails), rsi-divergence-pivot-oscillator (oscillator divergence). None is a close-vs-close multi-state Livermore trend taxonomy with two-bar confirmation. All ten open research/* PR titles were checked; none is FMZ-sourced or pivot-state-machine based. Existing root records were not re-audited individually in this Scout; the 390/390 count census plus the merged-base diff shows only reviewed PASS additions and README bookkeeping, with no other strategy changes.

## Falsification plan

With separate authorization only, materialize the minimal candidate-specific controller and test the NONE-branch first-bar routing, MAIN_UP/MAIN_DOWN maintenance inequalities at the exact 3.0% boundary, minor 1.5% rebound/retracement routing, secondary-state containment bands, the two-bar confirmation (no fire on single-bar state, no refire while unchanged), warmup-edge suppression, pending-bar gate freezes, exact t/t+1 timing, observed prices, quote fees, separate Decimal inventory, float residual tolerance and end-of-sample treatment. Before large-scale Qlib screening of any new execution path, obtain representative event-level Hummingbot/Qlib parity. No such execution, deployment or backtest occurs in this Scout.

## Crypto portability

Native venue is already BTC-USDT (FMZ stanza Futures_Binance); this derivative moves only the venue leg to Binance spot 1d with no leverage or funding. No asset substitution is made. Porting the 0.5%/6x/3x taxonomy to other spot symbols would be a new derived version with its own evidence, not covered by this record.

## Limitations

Verbatim code comes from the page's public embedded `source` field (byte-inspected this round); no login-wall bypass or paid content was accessed. The seven-vs-six state count follows the code, not the prose. The pure-research close/full-fill/fee model is not a real exchange acceptance or executable strategy implementation. Confirmation exits are bars late by construction and the book has no protective stop; no performance, survivor, live or Qlib parity claims.

## Implementation status

**implementation_status: not-implemented** — research record only. **status: research-only; adoption: not-approved; approval_scope: research-only.** The proposed PASS is not self-approval: independent Hermes Auditor GitHub Webhook Review alone owns source-fact review, exact-head PASS merge or NOT_LOSSLESS close. The existing signed webhook receiver alone owns post-merge README bookkeeping. This Scout does not approve, merge, close, modify main or change any trading/backtest/cron system.

## Adoption boundary

Research-only. Not approved for Paper, Testnet, Live, Qlib mass screening, or any deployment. Downstream use requires the independent PASS review plus separate implementation and authorization steps outside this record.

## Related Wiki records

None created by this Scout.

## Sources

- https://www.fmz.com/strategy/501679 — ianzeng123, first-party public page (author/date/parameters/verbatim Pine v6 source/backtest stanza publicly visible), inspected 2026-10-28.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — immutable pinned engine paths inspected via raw files this round.
- https://github.com/HCH725/alpha-strategy-research/pull/519 — prior independent bounded MARKET/POSITION_HOLD synthetic primitive review.
- https://github.com/HCH725/alpha-strategy-research/pull/529 — prior independent bounded pure-research execution and PASS-only census evidence.
- https://github.com/HCH725/alpha-strategy-research/pull/530 — prior independent PASS census evidence.
