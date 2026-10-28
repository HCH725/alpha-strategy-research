---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "FMZ 482873 pivot-breakout tolerance-retest long-flat BTCUSDT 1d derivative"
created: 2026-10-29
updated: 2026-10-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-02-20
sources:
  - https://www.fmz.com/strategy/482873
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The Pine declaration names the program 'SR Breakout & Retest Strategy (4hr)' but the FMZ machine backtest header pins period: 1d / basePeriod: 1d. Code header governs; this record adopts 1d and treats '(4hr)' as a label-only discrepancy."
  - "The page/mirror title advertises 'Multi-Level' ('多级') levels, but the verbatim code keeps exactly one live candidate per side (the latest confirmed pivot overwrites the prior). This record specifies the single-candidate machine as written, never a stacked multi-level book."
---
# Pivot-breakout tolerance-retest — independent long-flat derivative

## Provenance

**Primary source (directly read 2026-10-29):** FMZ public strategy **482873**, *基于支撑阻力位突破和回测的多级量化趋势交易策略 / SR Breakout & Retest Strategy (4hr)*, author handle **ianzeng123**, 创建日期 **2025-02-20 16:00:35**, https://www.fmz.com/strategy/482873 . Live page fetched this cycle over HTTPS (HTTP 200, 722,976 bytes, saved as `fmz482873_page.html`): the author span pins `ianzeng123`, the meta span pins `创建日期: 2025-02-20 16:00:35`, and the FMZ backtest header pins `period: 1d`, `basePeriod: 1d`, `exchanges: [{"eid":"Binance","currency":"ETH_USDT"}]`, window 2024-02-21 → 2025-02-18. The page carries a login-wall button, but the complete Pine v5 program is embedded in the served page JSON blob without any login: it was JSON-decoded twice from the page stream (outer page JSON, then the inner escaped `source` field cut before the `MA,Trend,Pivot,SR,BREAKOUT,RETEST` tag trailer), yielding a 2,831-byte program with SHA-256 `bc7e60d92294121caedd9c6d5a89b21cbcd8573f60c68315686df15dd932c15a` (saved as `fmz482873_livecode.pine`; the fingerprint fixes this cycle's content version, not a claim the page never changes). Decision-critical literals verified in the live blob this cycle: `leftBars = input.int(3`, `rightBars = input.int(3`, `tolerance = input.float(0.005`, `ta.pivotlow(low, leftBars, rightBars)`, `ta.pivothigh(high, leftBars, rightBars)`, the four `var` candidate/flag lines, the break lines (`low < candidateSupport`, `high > candidateResistance`), the two tolerance retest predicates, `strategy.entry("Long_Support", strategy.long)`, `strategy.entry("Short_Resistance", strategy.short)`, and the two `plot(` lines. Comment-stripped census over the live code: 2 `strategy.entry` / 0 `strategy.close` / 0 `strategy.exit` / 0 `strategy.order` / 0 `strategy.cancel` / 0 `pyramiding` / 0 `process_orders_on_close` / 0 `request.` / 0 `security(` / 0 `crossover` / 0 `crossunder` / 0 `ta.cross` / 1 `ta.pivotlow` / 1 `ta.pivothigh` / 0 `calc_on_every_tick` / 0 `input.timeframe` / 0 `timeframe.` / 0 `barstate` / 0 `nz(`. The absences mean Pine documented defaults apply to the source (single same-direction entry, later default fills); none is relied upon below, because the derivative pins its own state machine and fill timing.

**Mirror cross-check (not provenance):** the local FMZ mirror copy of this page holds a code block whose full 1,067-token stream is a verified contiguous subsequence of this cycle's live decoded program (1,067 live tokens over the header→plots span — token-identical). The mirror is corroboration only; every rule citation below comes from the live page.

**Independent derived strategy, NOT source-native reconstruction:** preserve the source's pivot-confirmed candidate levels (`ta.pivotlow/high`, 3/3 bars), the break-then-tolerance-retest two-step state machine with its exact 0.005 tolerance, source evaluation order (candidate-update → break-check → retest-check, long block before short block), and the one-shot-per-candidate latch (flags reset only on a newly confirmed pivot). Researcher-defined alterations: (a) disable the short leg entirely (LONG/FLAT only — the source short-retest event becomes the long exit signal, preserving source exit timing since Pine reversal would close the long on that bar anyway); (b) move Binance spot ETH 1d to Binance BTC-USDT **spot** 1d (spot-to-spot symbol transfer, no perpetual, no funding leg by construction); (c) evaluate signals on the fully completed prior bar and simulate MARKET fills at the current completed bar's close, rather than Pine's default later fills; (d) fix size at 0.001 BTC over 10,000 USDT cash with a hypothetical 0.1% per-side fee, a 60-bar warmup, explicit pending/fill state conventions, and an exit-priority tie-break for same-bar co-firing retest events. The source's `default_qty_type=strategy.percent_of_equity, default_qty_value=10` economics is explicitly not adopted.

**Immutable derivative identity:** `FMZ:482873|ianzeng123:2025-02-20|independent-derived-v1-pivot33-tol0005|BinanceSpot:BTC-USDT:1d|0.001BTC|prior-complete-signal-next-complete-close-MARKET|fee0.001|warmup60|2026-10-29`. Changing any formula, threshold, timing, market, risk, cost or direction creates a different derivative.

## Economic mechanism

### Source-reported

The page prose (Chinese + English) describes exactly this record's mechanism: confirmed pivot highs/lows anchor candidate support/resistance, a close beyond the level marks the breakout, and a return touch within tolerance marks the retest that triggers the trade — long on support retests, short on resistance retests. No source performance metric is adopted.

### Research interpretation

This is a **two-step break-then-retest ambush with a one-shot latch**, not a plain breakout chase. The pivot-confirmation gate (3 bars each side) means levels are admitted late but never repaint; the break leg alone never trades — price must come back and touch the broken level within 0.5% while closing back on the friendly side. The per-candidate latch (retested flag, reset only by a fresher pivot) makes each level fire at most once, so the machine cannot pyramid into a level that keeps getting tagged. The failure mode is plain: a level that breaks and never retests is a missed trade by construction, and aCascade of fresh pivots in a trend keeps resetting the latch so the machine watches breakouts sail away without ever firing. No profitability is asserted.

## Signal

**Gate 1 — exact researcher-pinned arithmetic.** Index completed UTC daily bars by `t=0,1,...`. Use real Binance BTC-USDT spot `O[t],H[t],L[t],C[t]`; reject incomplete/malformed bars; never interpolate.

1. Constants (researcher-pinned to source defaults): `LB=3`, `RB=3`, `TOL=0.005`.
2. Confirmed pivots on completed bars: `pLow[t] = L[t-3]` iff `L[t-3]` is the **strict unique minimum** of `L[t-6..t]` (seven completed closes, ties yield `na` — researcher pin where Pine tie detail is silent; the derivative is assessed on this rule, not as source float-parity); else `na`. `pHigh[t] = H[t-3]` iff `H[t-3]` is the strict unique maximum of `H[t-6..t]`; else `na`. Pivots therefore lag the extreme by exactly 3 completed bars and never revise — no repainting, no negative shift.
3. Registers (persist across bars, init `candidateSupport=na, supportBroken=false, supportRetested=false`, mirror for resistance): on simulator bar `t` **only after its close**, evaluate with the already-completed **previous** bar `u = t-1`, in this exact order:
   a. Candidate update: if `pLow[u]` non-na → `candidateSupport := pLow[u]`, `supportBroken := false`, `supportRetested := false`. If `pHigh[u]` non-na → same for resistance.
   b. Break check: if `candidateSupport` non-na and not `supportBroken` and `L[u] < candidateSupport` → `supportBroken := true`. If `candidateResistance` non-na and not `resistanceBroken` and `H[u] > candidateResistance` → `resistanceBroken := true`.
   c. Retest check (same bar, after break-check, so a wick-through-and-recover fires immediately): `LONG_SIGNAL` iff `candidateSupport` non-na and `supportBroken` and not `supportRetested` and `C[u] >= candidateSupport` and `|L[u]-candidateSupport| <= candidateSupport*TOL` (candidate is a positive price, so the band is well-defined); on fire set `supportRetested := true`. `SHORT_SIGNAL` mirrors with `H[u]`, `C[u] <= candidateResistance`, `|H[u]-candidateResistance| <= candidateResistance*TOL`, setting `resistanceRetested := true`.
   d. Long block (b–c) is evaluated before the short block each bar — source order, pinned.
4. Derived orders: if confirmed FLAT and not pending, `LONG_SIGNAL` (and not `SHORT_SIGNAL` on the same `u`) creates one BUY of 0.001 BTC at simulated `C[t]` subject to warmup/affordability. If confirmed LONG and not pending, `SHORT_SIGNAL` creates one SELL of the confirmed 0.001 BTC at simulated `C[t]` — the source short-retest event is the exit; no short position is ever opened. `C[t]` is solely the modeled fill price and cash check; no current-bar `t` indicator may influence the action.
5. Same-bar co-fire tie-break (researcher pin, disclosed): if `LONG_SIGNAL` and `SHORT_SIGNAL` fire on the same `u`, the exit wins — when LONG, SELL with no BUY; when FLAT, no trade. The source's sequential legs would open-then-reverse on such a bar; the FLAT outcome preserves the long-book close without inventing a short.
6. There is no short leg, no stop/target/trailing/time exit, no safety order, no scale-out, no end-of-sample forced liquidation. An unclosed final position remains open, marked at the last observed valid price only. The one-shot latch means a candidate never re-fires; re-entry needs a fresh confirmed pivot → break → retest chain while FLAT (no cooldown).

**Gate 2:** LONG/FLAT on Binance BTC-USDT **spot**, leverage 1, short side explicitly disabled. **Gate 3:** complete retest-gated entry, opposite-signal exit with pinned co-fire priority, and intentionally absent further risk legs as specified above.

## Required data

**Gate 6:** require at least **60 consecutive fully completed** UTC 1d OHLCV bars before the first signal/fill; the structural minimum is ~8 (7-bar pivot seed plus the one-bar lag). A Binance daily bar opening at `T[t]` is not complete before `T[t]+86400 seconds`. Predicates computed on completed bar `u=t-1` (whose pivot reads reach back to `u-6`, all completed) are known before bar `t` completes; the modeled fill at `C[t]` is assigned **effective time** `T[t]+86400`, never the raw Kline opening label `T[t]`. A completed-close MARKET simulator fill is a bounded historical modeling convention, **not** a claim that a live order can execute at a known historical close. No future prices, higher-timeframe partial bars, repainting pivots, full-sample fitted values, negative shifts, hindsight optimization or imputed candles.

Every bar must have a strictly consecutive UTC daily timestamp and valid OHLCV. On a missing/invalid/out-of-sequence bar, generate no new signal or fill, freeze all registers/flags, reset the 60-bar contiguous warmup, and **retain** any confirmed existing spot position; do not synthesize an exit. After continuity is restored, resume decisions only after a fresh warmup. The controller must never use the current bar's still-forming close to construct a signal.

## Execution assumptions

**Gate 5 — actual inspected pinned engine path (re-verified this cycle, not a generic API assertion):** admission package `20260920` (policy label, see disclosure), Hummingbot VERSION `dev-2.17.0`, source commit `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. This cycle fetched the pinned tree (non-truncated) and raw file bytes: `backtesting_engine_base.py` (39,071 bytes), `executors_simulator/order_executor_simulator.py` (3,913 bytes), `backtesting_data_provider.py` (8,823 bytes), `data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py` (3,924 bytes), `.../binance_spot_candles/constants.py` (993 bytes), `controllers/controller_base.py` (38,335 bytes), `VERSION` (`dev-2.17.0`). No claim is made about a different engine build.

- **Market/data:** `BinanceSpotCandles` reads `/api/v3/klines` (pinned constants) and exposes `1d`, with timestamp and O/H/L/C/V parsed from actual Kline fields (pinned feed lines 82/99–108). Pin `connector_name="binance"`, `trading_pair="BTC-USDT"`, one 1d feed, no secondary timeframe, cross-asset join, funding, mark price or order-book requirement.
- **Controller:** a strategy-specific `ControllerBase` implementation (not yet written) computes the exact pivot/break/retest arithmetic and prior-bar predicates on completed candles. `BacktestingEngineBase.run_backtesting` (pinned line 221, `trade_cost` parameter at line 225) runs `simulate_execution` (line 269), which per row calls `update_state` then `determine_executor_actions` (lines 283–284) and dispatches `CreateExecutorAction` with `OrderExecutorConfig(side=BUY/SELL, position_action=OPEN/CLOSE, amount=Decimal("0.001"), execution_strategy=MARKET, leverage=1)`. The generic executor does **not** compute pivots or implement this controller automatically.
- **Fill/clock:** inspected `OrderExecutorSimulator.simulate` (line 10) sets MARKET fill timestamp to the **first supplied row** (lines 24/27) and fill price to that row's **close** (line 56); `cum_fees_quote = trade_cost * amount_quote` (line 62); `CloseType.POSITION_HOLD` is emitted on fill (line 70). Here row `t` uses only signal inputs from `t-1`, and the simulator's fill `C[t]` is effective only at `T[t]+86400`. The engine's raw `timestamp_bt` and backward `merge_asof` (lines 466–470) are bar-**open** labels; interpreting them as completed-bar decision or fill times would be future leakage. An implementation failing to normalize effective close times is **not** compliant.
- **Fill-confirmed position:** the engine nets opposite BUY/SELL base fills into a hold ledger with weighted entry cost, gross realized PnL and `cum_fees_quote` (verified pattern in the inspected simulator). The default terminated-executor controller visibility is bounded (pinned engine line 319 `terminated_executors_window` handling); use `BacktestingEngineBase(terminated_executors_window=None)` or a durable equivalent plus a controller-side pending/fill ledger. `positions_held` can lag an executor's fill by a controller tick; no duplicate BUY/SELL while a prior MARKET fill is pending reconciliation. Never infer a fill from action creation alone. The exit maps to a plain MARKET close on a completed bar — no stop/limit legs, no intrabar ordering, no position-executor TP/SL machinery, hence no novel execution primitive beyond the representative MARKET OrderExecutor path reviewed in merged Alpha PR #414.
- **Cash/fees:** `run_backtesting(trade_cost=0.001)` is a **hypothetical 0.1% fee on each filled side**, charged in quote currency as `trade_cost * amount * fill_close`. For buy price `Pb`, sell `Ps` and `Q=0.001`, modeled net realized quote PnL = `Q*(Ps-Pb) - 0.001*Q*(Pb+Ps)`; quote cash is decremented by buy notional plus fee and credited by sell notional minus fee. Gross PnL and fee accumulators are separate, so a gross PnL series is **not** fee-inclusive net equity. This fee is **not** the source's, user's or Binance account's realized tariff.
- **No fabricated economics:** spot has no perpetual funding payment; this is **not** a claim of zero perpetual funding. The inspected MARKET simulator does not independently reproduce order-book spread, impact, slippage, latency, partial fills or exchange minimums. Those remain unverified real costs and execution constraints, not assumed real-world zeros. `BacktestingDataProvider.get_price_by_type` falls back to `Decimal("1")` when price is missing (pinned lines 132–140): this fallback must be explicitly rejected for BTC price/cash/fill accounting. Use actual positive finite `C[t]` only. Maintain Decimal ledger quantities and reconcile any simulator float roundoff; no fabricated prices.

**Capability boundary and package disclosure:** a single spot daily candle feed and MARKET completed-close fill model with a position-hold ledger is supported by the pinned inspected path. The source's ETH symbol, its Pine-default later fills, exact Pine float semantics and real fills are **not** claimed. The `20260920` package label is retained as a policy label only: this cycle verified behavior at source commit `8b0e067` (whose tree predates that label) and invents no package-to-commit mapping; sibling PASS records are engine-path evidence only, never proof of this derivative. This derivative is not a source-native equivalence assertion.

## Evidence

### Source-reported

FMZ 482873, ianzeng123, 2025-02-20: pivot-confirmed candidate support/resistance (`ta.pivotlow/high`, 3/3 bars); break legs (`low < candidateSupport`, `high > candidateResistance`); tolerance retest legs (`close` back on the friendly side with `|wick - level| <= level*0.005`); one-shot latch per candidate (flags reset only on a fresher pivot); `Long_Support` / `Short_Resistance` entries, no close/exit/stop/target legs, no MTF, no cross functions. Original venue Binance spot ETH 1d, demo window 2024-02-21 → 2025-02-18. No source performance metric adopted.

### Independently reproduced

**No independent performance or Pine-parity backtest reproduced.** This cycle read the live FMZ page blob (double-JSON-decoded program, fingerprinted) and the pinned Hummingbot sources, and ran the mirror-vs-live token cross-check, but ran no Qlib/Hummingbot backtest, no market replay, and no strategy controller. Six-gate PASS is the Scout's **proposed research admission assessment**, subject to the independent Hermes Auditor; it is not an auditor verdict, Survivor designation, economic performance claim or trading approval.

### Negative evidence

Exact Pine float bit-identity with `ta.pivotlow/high` internals is not reproduced here; the derivative pins the stated strict-unique-extremum rule as its own executable definition. Actual Binance fees, lot/tick constraints, real partial fills, package wheel byte identity, and future implementation correctness remain unverified. Any controller that reads bar `t` pivots while claiming a `t-1` decision, treats raw bar-open labels as close timestamps, silently uses a missing-price fallback, double-counts position holds, or converts the retest predicates into intrabar stop/limit orders fails the stated Gate 5/6 contract. The short leg, ETH symbol, Pine later fills and Pine float exactness are explicitly out of scope, not silently preserved.

**Six-gate summary:** (1) pinned 3/3-bar confirmed pivots, 0.005 tolerance retest, break→retest order with one-shot latch and pinned tie semantics; (2) spot LONG/FLAT, shorts disabled; (3) exact entry, opposite-signal exit with co-fire priority, deliberately disabled further legs; (4) fixed one-unit, fill-confirmed pending state, frozen registers, no DCA/pyramiding; (5) inspected pinned spot daily candle → custom controller → MARKET OrderExecutor → POSITION_HOLD and quote-fee ledger with price/time guards, no novel primitive; (6) 60 contiguous completed bars, one-bar lag, no future-data use.

## Falsification plan

Pre-write dedup at `main` SHA `9fa4fe54` (423 root records, README 423): no record cites FMZ `strategy/482873` or this pivot-break-tolerance-retest identity, and no open `research/*` PR covers it. The same author handle (ianzeng123) appears on main only under different strategy IDs with different mechanisms (486567 log-z, 483504 balance-of-power, 482833 CMO-BB, 482890 quantile-band, 483087 triple-bollinger, 501679 Livermore pivot, 521670 wavelet slope, 482784 IBS) — same author, different sources, no identity collision. Closest mechanism neighbours, all fenced as different: `support-resistance-fractal-trailing-breakout-two-sided-btcusdt-4h-2026-10-11.md` (fractal-averaged trailing levels with a persistent latch — entries on latch-gated breakouts, no retest leg, no one-shot latch); `fmz-501679-livermore-pivot-trend-long-flat-btcusdt-1d-2026-10-28.md` (close-only regime taxonomy, no price-level breakout at all); `fmz-felipemiransan-priceaction-sr16-pattern-bracket-long-flat-btcusdt-1h-2026-10-26.md` (16-candle-pattern bracket entries, not pivot break-retest); `forven-pivot-s1-bounce-r1-exit-long-flat-btcusdt-1h-2026-10-18.md` (pivot-point S1 bounce entry with R1 exit — bounce, not break-then-retest); `pivot-point-breakout-kaufman-btcusdt-1d-2026-10-05.md` (Kaufman-smoothed pivot breakout, no retest state machine). None requires a confirmed break followed by a tolerance-banded retest touch with a per-candidate single-fire latch. Open `research/*` PRs cover Williams-channel, Gaussian-StochRSI, SuperTrend, Chandelier, SSL, Swift-MA, CCI, AdxSmas, ClucMay and Heracles lanes — different mechanisms and sources.

Skipped same-funnel neighbours (fenced, not proposed): 483022 sentiment (hardcoded 8-value demo array cycled by modulo — no real point-in-time data); 473319 KNN (distance loop is degenerate — features equal the window itself so all distances are zero — claimed ML mechanism is false); 473134 CMO(9) ±50 (trivial parameter variant of pooled CMO-80); 489296 Heikin-Ashi triple (synthetic-series kill); 477606 plain engulfing (engulfing cluster); 489133 BTST (equity-market clock screening, not crypto-portable); 475595 trendlines (three-way calcMethod + backpaint variants — reviewer must not choose); 488536 liquidity-shift (three-way mode input + pip-denominated risk); 474055 double-bottom/SR (zero-default SR level makes the short leg near-always-true); 471696/488417 SAR legs (SAR cluster); 468349/473235/469615 BB legs (BB cluster); 474705 CMO (CMO cluster); 471698 123-pattern (123 cluster); 473356 gap (gap cluster); 471718 time-rotation (clock-shape cluster).

Future tests (not performed): hand-calculate pivot confirmation, break and retest transitions on frozen consecutive bars; test tie-window (non-unique extremum → na) handling, same-bar break+retest firing, same-bar co-fire exit priority, missing-bar register freeze, warmup reset and cash guard; reconcile fill effective timestamps, BUY/SELL sides, position netting and each fee against the pinned simulator. Only after representative Hummingbot/Qlib event-level execution-path parity may this strategy path enter mass Qlib screening. This is **not** a new admission gate or a requirement for each candidate to rerun generic primitive validation.

## Crypto portability

Binance spot BTC-USDT 1d OHLCV only — no sentiment feed, no screener, no equity session clock, no futures margin, no second timeframe. The rule consumes H/L/C of completed daily bars; the 0.5% tolerance band scales with price, so the BTC symbol transfer changes no rule constant. Real-world BTC minimums, tick precision, spread and gap risk across daily closes remain unverified and undisguised.

## Limitations

This is an independent derived hypothesis, not a faithful reproduction of the FMZ Pine source. It inherits the pivot lag: levels confirm 3 bars late, and fast V-reversals complete the break-and-retest before any candidate exists. Each level fires at most once, so clustered retests of an unlucky first touch are watched, not traded. A completed-close MARKET simulator is a bounded research abstraction; real gaps across daily closes bypass the modeled touch band with no slippage accounting. No positive return, real trading viability, Qlib parity, OOS result, Survivor/HB Certified status, Paper/Testnet/Live authorization or deployment is asserted. Optional campaign coins/timeframes, DCA BO/SO 6/6/6 and futures leverage are not entry requirements and are not part of this derivative.

**Implementation status:** `not-implemented`. **Adoption:** `not-approved`. **Approval scope:** `research-only`. Independent Hermes Auditor GitHub Webhook Review alone owns source-fact remediation, exact-head PASS merge or NOT_LOSSLESS closure. This Scout does not approve, merge or alter `main`.

## Implementation status

`not-implemented` — no controller, backtest, replay or deployment artifact exists for this derivative. See Limitations for the adoption boundary.

## Adoption boundary

`not-approved`, `research-only`. No Paper/Testnet/Live authorization is asserted or requested. Merge into `main` requires the independent Hermes Auditor's exact-head PASS verdict; otherwise this PR stays unmerged and the research remains on its branch.

## Related Wiki records

None.

## Sources

- FMZ primary source: https://www.fmz.com/strategy/482873 (ianzeng123; 创建日期 2025-02-20; backtest header 1d/basePeriod 1d/Binance ETH_USDT; full Pine text in served page blob double-JSON-decoded and fingerprinted `bc7e60d9…5df15` 2026-10-29).
- Pinned Hummingbot engine: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting (VERSION `dev-2.17.0`; `backtesting_engine_base.py`, `executors_simulator/order_executor_simulator.py`, `backtesting_data_provider.py`, `data_feed/candles_feed/binance_spot_candles/` feed + constants, `controllers/controller_base.py` directly inspected this cycle).
- Prior independently merged pinned-engine capability evidence: https://github.com/HCH725/alpha-strategy-research/pull/414 (engine-path evidence only, not proof of this derivative's signals or performance).
