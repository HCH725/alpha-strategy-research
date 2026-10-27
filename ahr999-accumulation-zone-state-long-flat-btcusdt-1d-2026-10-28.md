---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "AHR999 accumulation-zone state long-flat BTCUSDT 1d (independent derivative)"
created: 2026-10-28
updated: 2026-10-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-28
sources:
  - https://ahr999.com/ahr999/ahr999_buy03.html
  - https://github.com/RuochenLyu/ahr999-dataset/blob/main/docs/methodology.md
  - https://ahr999.aix4u.com/faq
  - https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# AHR999 accumulation-zone state long-flat BTCUSDT 1d (independent derivative)

## Provenance

- **Originator:** Chinese investor 九神 (ahr999), who proposed the AHR999 hoarding index for long-term Bitcoin accumulators. The original exposition defines `ahr999 = (BTC price / 200-day DCA cost) x (BTC price / index-growth fitted value)` and gives folk zones: `<0.45` bargain (抄底), `0.45-1.2` DCA (定投), `1.2-5` wait-for-takeoff (等待起飞); above the top zone the author does not sell, so no exit is defined there: https://ahr999.com/ahr999/ahr999_buy03.html
- **Exact open mathematics:** RuochenLyu `ahr999-dataset` methodology pins `ma200_d = mean(close[d-199..d])` (arithmetic), `coin_age_days_d = floor((d - GENESIS)/1 day)` with `GENESIS = 2009-01-03`, `fitted_d = 10^(5.84*log10(coin_age_days_d) - 17.01)`, `ahr999_d = (c_d/ma200_d)*(c_d/fitted_d)`, null until 200 closes exist: https://github.com/RuochenLyu/ahr999-dataset/blob/main/docs/methodology.md
- **Zone corroboration:** the aix4u dataset FAQ restates the same product formula and the `<0.45 / 0.45-1.20 / 1.20-3.00 / >3.00` folk zones, explicitly noting the thresholds are heuristic, not part of the formal definition and not buy/sell signals: https://ahr999.aix4u.com/faq
- **Explicit independent derivative, NOT source-native or lossless:** the sources publish a valuation guide for discretionary DCA, not a trade system (the originator does not define an exit). This record separately identifies a fully specified executable derivative: (1) pins the **arithmetic** 200-day mean (original DCA-cost semantics; see ecosystem-split note below), (2) pins Binance BTCUSDT spot **1d** closes, (3) collapses bargain+DCA zones into one LONG state with the **1.2** boundary as the single state edge, (4) fixes quantity/cash/fees/fills/warmup/confirmation below, (5) disables SL/TP/trailing/time exits. Every changed or added decision rule is specified in Signal; source-native event equivalence is explicitly disclaimed.
- **Ecosystem-split disclosure:** some dashboards compute the 200-day leg as a geometric mean. This derivative pins arithmetic, per the originator's DCA-cost wording and the exact open implementation above. Independent corroboration (Evidence) shows the arithmetic leg reproduces a third-party publisher's value to the cent while the geometric leg misses by ~370 USDT, so the pin is evidenced, not arbitrary.
- **Immutable derivative identity:** `AHR999:jiushen:arith-ma200-200:fitA5.84-fitB-17.01-genesis2009-01-03|derived-v1-20261028|BinanceSpot:BTCUSDT:UTC1d:threshold1.2:tie-to-caution|LONG-below-1.2:FLAT-at-or-above-1.2|same-close-MARKET-confirm-next-tick:Q0.001BTC:fee0.001|warmup200`. Any altered mean variant, constant, genesis, threshold, tie rule, market, fill timing, size or cost is a different derivative.

## Economic mechanism

### Source-reported

AHR999 compresses two cheapness ratios into one scalar: price versus its own 200-day DCA cost basis, and price versus an age-anchored log-log trajectory. Low readings mean accumulation is historically cheap relative to both recent cost and the long-run curve; high readings mean the market runs hot. The zones are folk heuristics, not signals.

### Research interpretation

Falsifiable hypothesis only: holding spot BTC while the product sits below the caution boundary, and standing aside at or above it, may keep exposure in historically cheap regimes and avoid late-cycle heat. The derivative can hold for months, flip rarely (~53 edges in ~8.7 years of Binance history), enter late after a reclaim, and exit late after overheating begins. No expectancy, timing edge, or profitability is asserted.

## Signal — fully defined derived rules

- **Series:** exactly one Binance BTCUSDT **spot 1d** OHLCV series, zero-based bar index `t`. Bar `t` carries open timestamp `T[t]` (UTC midnight) and becomes completed/available at `E[t] = T[t] + 86400` seconds. Use only **completed** bars.
- **Validation (fail-closed):** require strictly increasing `T` spaced exactly 86400 seconds, finite OHLCV, `high>=max(open,close)>=min(open,close)>=low`, all prices `>0`, `volume>=0`. Any missing, duplicate, mis-spaced, NaN, or nonpositive-price bar **aborts the research run**; do not interpolate, forward-fill, or invent a price.
- **200-day leg:** `MA200[t] = sum(close[t-199..t])/200` (arithmetic mean, float64), defined only for `t>=199`; undefined earlier. Nonpositive inputs cannot occur after validation (all closes `>0`).
- **Fitted leg:** `d[t]` = UTC calendar date of `T[t]`; `age[t] = (d[t] - 2009-01-03)` in whole days (integer date difference; equals whole-day count for UTC-midnight bars); `FIT[t] = 10^(5.84*log10(age[t]) - 17.01)` with base-10 logarithm. The originator article's "2019-01-03" birthday line is a typo against its own fit and every open implementation; this derivative pins **2009-01-03**.
- **Index:** `AHR[t] = (close[t]/MA200[t]) * (close[t]/FIT[t])`, defined only for `t>=199`.
- **Zone:** `ACCUM[t] = (AHR[t] < 1.2)`; otherwise CAUTION. An exact `AHR[t] == 1.2` tie resolves to CAUTION (FLAT side). The `0.45` bargain sub-boundary is reported only; it creates no separate state, size, or order (both source zones are hold/accumulate, so the collapse is event-neutral within this derivative).
- **Warmup:** bars `t=0..198` (first 200 consecutive completed 1d bars) remain FLAT without evaluation or orders. No signal exists before `t=199`; warmup bars serve only as indicator inputs, never as signals.
- **Initial alignment (t=199 only):** if `ACCUM[199]` then BUY; else stay FLAT. This is an explicitly defined first-decision rule, not a carried-forward pre-warmup signal.
- **Edges (t>199 only):** `ENTER[t] = (NOT ACCUM[t-1]) AND ACCUM[t]`; `EXITedge[t] = ACCUM[t-1] AND (NOT ACCUM[t])`. Persistent zone state issues no order.
- **Entry:** when confirmed-state FLAT and `ENTER[t]`, emit exactly one BUY for **0.001 BTC** for simulated MARKET fill at completed bar `t`'s close (see Execution assumptions for the confirmation pipeline). The emission bar is not evaluated for exit.
- **Exit:** when confirmed-state LONG and `EXITedge[t]`, emit exactly one SELL of the full 0.001 BTC for simulated MARKET fill at completed bar `t`'s close.
- **Disabled:** stop-loss, take-profit, trailing, time exits, partial fills/TP, DCA/safety orders, pyramiding, cooldown timers, same-bar re-entry, forced terminal liquidation, intrabar/high-low-touch orders, maker/limit orders, leverage, margin, funding legs, multi-asset state, parameter search. No silent executor defaults.
- **Terminal:** if LONG at the last bar, mark the open 0.001 BTC to the last actual close for reporting only; no synthetic liquidation trade is fabricated.

## Required data

Only actual Binance spot BTCUSDT 1d open/high/low/close/volume, validated as above, plus UTC calendar dates derived from bar open timestamps (no external feed). No funding, order-book, on-chain, sentiment, or higher/lower-timeframe data. No synthetic candles, no imputed prices, no future bars. Warmup is exactly the first 200 consecutive completed bars; the first decision is `t=199`.

## Execution assumptions — demonstrated pinned-engine path and bounded model

**Pinned benchmark and verified code identity.** Policy baseline per current README: Hummingbot package `20260920`, `hummingbot/VERSION=dev-2.17.0`. First-hand verification (this run, via GitHub/contents/compare/raw APIs on `HCH725/hummingbot`):

1. `8b0e067e80ab62f10846d518dcb5a8218527ddb3` was authored **2026-09-20** (the package date); its `setup.py` still stamps the older `20260729` (stale stamp, disclosed, not hidden) and its `hummingbot/VERSION` is `dev-2.17.0`.
2. Its sole child `fac3a7f8c4adfd9f07f462cfaad9e2ed9e8b6467` (same date, "Update version number") differs by **exactly one file** (`setup.py`, per the compare API), so every engine code path below is byte-identical in both; `hummingbot/VERSION` is `dev-2.17.0` at both.
3. "Package 20260920" is therefore evidenced as the build of the 2026-09-20 code tree; all engine paths are read at that immutable tree. No image digest is published in-repo — declared boundary: correspondence rests on commit date + single-file compare + VERSION match at both commits. If the reviewer requires digest-level build provenance, this record declares that limit and must not PASS on Gate 5.

**Verified path (all read at the tree above; static capability evidence, not a strategy backtest):**

1. **Feed/clock:** `binance_spot_candles/constants.py` declares `1d`; `binance_spot_candles.py` `_parse_rest_candles` maps exchange `row[0]` open-time (via `ensure_timestamp_in_seconds`) and OHLCV `row[1..5]`. Decision time is `E[t] = T[t]+86400`, never candle open.
2. **Controller/action:** `backtesting_engine_base.py:simulate_execution` runs `update_state(row)` then `controller.determine_executor_actions()`; a `CreateExecutorAction` feeds `simulate_executor(config, processed_features.loc[i:max_ts])`. A minimal not-yet-implemented controller holds the FLAT/PENDING/LONG confirmed state plus last-zone bit and emits one `OrderExecutorConfig(connector_name="binance", trading_pair="BTC-USDT", side=BUY/SELL, amount=Decimal("0.001"), position_action=OPEN/CLOSE, execution_strategy=MARKET, leverage=1)`. This is a research expressibility argument, not a claim that the controller exists.
3. **Fill + confirmation timing (handles the engine reporting lag explicitly):** `order_executor_simulator.py` fills MARKET at the **first supplied row's close** (`amount_quote=float(amount)*close`, `cum_fees_quote=trade_cost*amount_quote`, `CloseType.POSITION_HOLD`, trimmed to fill timestamp). Per-tick ordering verified in `backtesting_engine_base.py`: `update_state` drains the previous tick's pending holds (Step 1) **before** `update_executors_info` routes this tick's terminations to the pending queue (Step 2), so a fill at tick `i` reaches `positions_held` only at tick `i+2`; `get_executor_info_at_timestamp` (`executor_simulator_base.py`) reports TERMINATED once the lookup timestamp passes the trimmed fill row. The derivative therefore: (a) instantiates the engine with **`terminated_executors_window=None`** (explicitly supported constructor argument, documented "Pass None to hand the controller the full history"), so fill evidence is never window-pruned; (b) treats an emitted order as filled **only** when a matching TERMINATED POSITION_HOLD executor (same config id, side, `filled_amount_quote>0`) is observed in `controller.executors_info` at tick `>=i+1`; (c) transitions PENDING->LONG / PENDING->FLAT and begins exit evaluation only at that confirmation tick — never on the emission bar, never from order placement alone; (d) **aborts** if the expected confirmation is absent at `i+1` or reports FAILED/EXPIRED; (e) never reads `positions_held` or native exact-zero flags for decisions (documents the `i+2` lag without depending on it). Same-close fills are a historical zero-latency modeling convention, not a live execution guarantee; no next-open, maker, or stop primitive is hidden here.
4. **Ledger:** start `cash=Decimal("10000")` USDT, `inventory=Decimal("0")` BTC, exact `Q=Decimal("0.001")`. Confirmed BUY: `cash -= Q*P*(1+f)`; `inventory += Q`. Confirmed SELL: `cash += Q*P*(1-f)`; `inventory -= Q`. `f=Decimal("0.001")` per side is an explicit **hypothetical** quote-notional fee, not a verified Binance tier; `trade_cost=0.001` is passed to the simulator. Engine gross/fees from each confirmed fill are reconciled against this Decimal ledger within **1e-10 BTC base / 1e-6 USDT quote**; larger deviation, negative modeled cash, or unaccounted fill **aborts**. `BacktestingDataProvider.get_price_by_type`'s `Decimal("1")` missing-price fallback is explicitly forbidden for this model (no missing prices are tolerated at all).
5. **Spot scope:** funding is not applicable (not a fabricated realized-zero funding stream); no margin/liquidation; no tick/lot/min-notional, liquidity, spread, real fee-tier, slippage, partial-fill, or live-acceptance verification. Simulator price impact/slippage absence is not evidence of zero real slippage.

## Evidence

### Source-reported

Originator article defines the product formula, fit constants `5.84/-17.01`, and folk zones; open methodology pins arithmetic MA200, 200-bar null rule, `GENESIS=2009-01-03`, and the same constants; aix4u FAQ restates formula+zones and warns zones are heuristic, not signals. No source trade events, fills, or returns are claimed or inherited.

### Independently reproduced

Researcher-run arithmetic checks over live Binance data (explicitly **not** a Hummingbot backtest, **not** Qlib parity, **not** performance evidence):

- **Third-party anchor (2026-09-29):** recomputation from Binance BTCUSDT 1d closes gives close `83663.66`, arithmetic MA200 `71237.64`, fitted `177343.43` (age 6478), AHR `0.5541` — matching the independent publisher's close, MA200 (to the cent), and index (to 4 decimals) exactly. The geometric-mean variant gives `70868.04`, missing by ~370 USDT.
- **Schedule tape:** 3359 consecutive completed daily bars (2017-08-17 to 2026-10-27), zero gaps; first valid index `t=199` = 2018-03-04; **27 ENTER / 26 EXIT** edges at the 1.2 boundary; terminal LONG (last AHR `0.4919`, last close `80850.01`, marked only); no exact `1.2` tie in-sample (tie rule still pinned).
- **Dual implementation:** float64 pipeline and an independent Decimal-summation MA200 path agree to the cent (`71237.64`); warmup-boundary, tie-branch, genesis-date, and log10-vs-ln branches covered in the falsification plan, not hand-verified here.

### Negative evidence

No original order fills, no source backtest statistics, no HB-executed run, no fee-tier verification. The originator never defines an exit; the 1.2 exit, fills, sizes, and timing are researcher-declared. Regime holds last months; whipsaw around 1.2 (e.g., repeated 2018 and July-August 2025 edges) compounds hypothetical fees with no protective stop.

## Six-gate evidence for independent auditor

1. **Determinism:** exact arithmetic MA200, fitted constants, genesis date, zone formula, 1.2 threshold with tie-to-caution, warmup count, initial-alignment vs edge rules with disjoint domains (`t=199` vs `t>199`), strict comparisons, validation/abort list, no ML/fit/seeds.
2. **Direction:** Binance BTCUSDT spot LONG/FLAT only; short, leverage, margin disabled.
3. **Entry/exit/risk:** edge-triggered BUY/SELL pair, full-size close, SL/TP/trailing/time/partial exits explicitly disabled, no hidden defaults.
4. **State:** exact 0.001 BTC, single position, no DCA/pyramiding/concurrency, PENDING gating, fresh-edge re-entry only, no same-bar round trip, no cooldown (explicitly none), terminal open marked not liquidated.
5. **Pinned compatibility:** `1d` declared in pinned feed constants; verified MARKET-first-close/POSITION_HOLD path; `terminated_executors_window=None` + TERMINATED-evidence confirmation timing that models the verified one-tick reporting lag; independent Decimal ledger with fail-closed tolerances; Decimal("1") fallback forbidden; spot funding n/a; reuse of the independently reviewed bounded MARKET/POSITION_HOLD lane (Alpha PRs #519/#529-#534/#536) with no new engine primitive.
6. **Causality:** completed 1d bars only, decision at `E[t]`, fills at verified simulator closes bounded as historical convention, 200-bar warmup, no future reads, repainting, full-sample fit, or synthetic prices.

## Dedup

Current-main snapshot at base `430e70b`: 393 root strategy records, README count 393. Code/title search for `ahr999`, `ahr-999`, `jiushen`, `nine-god`, `hoarding`, 200-day-cost x age-fitted product, and 1.2-threshold state returned **no record**. Nearest neighbor `mayer-multiple-below-2p4` is materially different (single arithmetic 200DMA ratio, 2.4 threshold, Trace Mayer lineage — no age-anchored fitted leg, no product, different author/source). All 10 open `research/*` PRs checked; none is this source or mechanism. Recent closed Scout PRs (Gartley/Juliano/MultiRSI/MACDRSI200/ChaikinVol) are history, not admission, and none overlaps.

## Falsification plan

Under separate future authorization only: MA200 window off-by-one (199 vs 200 closes), arithmetic-vs-geometric divergence log, tie-at-1.2 branch, genesis 2009 vs 2019 typo branch, log10-vs-ln branch, warmup-boundary first-decision vs no-carryforward consistency, initial-alignment branch, edge-vs-persistence (no repeated orders), emission-vs-confirmation gating (no same-tick exit, no placement-as-fill), missing/duplicate/mis-spaced bar abort, nonpositive-price abort, Decimal("1")-fallback absence, per-fill 1e-10/1e-6 reconciliation, last-bar pending/terminal handling, point-in-time prefix invariance. A genuinely new Qlib/HB execution primitive needs representative event-level parity before mass screening; none is introduced here.

## Crypto portability

Explicit BTCUSDT-only derivative. The fitted constants are age-anchored to Bitcoin's own trajectory and the zones are BTC folk heuristics; porting to any other asset without refit is disallowed by this record. No claim of source equivalence, live fill achievability, or cross-market generality.

## Limitations

The sources are a valuation guide, not a trade system; the exit, fills, sizes, and timing are declared researcher choices. The arithmetic/geometric ecosystem split is disclosed with anchor evidence for the chosen leg. Historical same-close MARKET fills are idealized and may be unavailable live; there is no stop protection, measured slippage, spread, real fee tier, or order-minimum validation. Slow regime holds concentrate risk for months; whipsaw near 1.2 churns hypothetical fees. The independent auditor must reject if any claimed pinned path is not substantiated, and must treat the package-correspondence boundary above as a Gate 5 input.

## Implementation status

`implementation_status: not-implemented`. Research-only specification; no dedicated controller, no Hummingbot/Qlib execution, no container, no trading or deployment performed. The Evidence numbers are local arithmetic checks, not engine runs.

## Adoption boundary

`status: research-only`; `adoption: not-approved`; `approval_scope: research-only`. Proposed `hb_ready_status: PASS` is a submission claim for the independent Hermes Auditor GitHub webhook review only; the Scout does not self-approve, merge, or close. README reconciliation belongs solely to the existing signed webhook receiver after a confirmed accepted merge.

## Related Wiki records

No new Wiki/registry entries; Mayer-Multiple and other valuation-ratio records are not asserted equivalent.

## Sources

- https://ahr999.com/ahr999/ahr999_buy03.html — 九神, AHR999 originator exposition: product formula, fit `Y = 5.84X - 17.01`, folk zones; read 2026-10-28.
- https://github.com/RuochenLyu/ahr999-dataset/blob/main/docs/methodology.md — exact open math (arithmetic MA200, 200-bar null rule, GENESIS 2009-01-03, constants, quantile method); read 2026-10-28.
- https://ahr999.aix4u.com/faq — formula + zone restatement with heuristic-not-signal warning; third-party anchor row 2026-09-29 (0.5541); read 2026-10-28.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned engine tree inspected (feed constants/parser, backtesting engine, order simulator, simulator base, data provider, setup.py, VERSION); compare `8b0e067...fac3a7f8c` (single-file setup.py-only delta) and VERSION at both commits verified 2026-10-28.
- https://github.com/HCH725/alpha-strategy-research/pull/519 — prior independently reviewed bounded MARKET/POSITION_HOLD primitive audit (precedent lane, not execution proof for this record).
