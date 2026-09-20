---
schema: strategy-research-record-v1
title: "FMZ TradFi Perpetual Multi-Symbol Vol-Ranked Long-Only Geometric Grid with Hysteresis Rebalance (540030)"
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - grid-trading
  - tradfi-perpetual
  - volatility-rank
  - hysteresis
  - mean-reversion
  - fmz
status: research-only
confidence: low
source_as_of: 2026-05-11
sources:
  - "FMZ strategy page: 'TradFi多品种网格（纯网格版）' / TradFi multi-symbol pure grid, strategy id 540030, author ianzeng123, created 2026-05-11. Public page includes substantial Python source with default parameters. https://www.fmz.com/strategy/540030"
  - "Companion FMZ article (source-linked): 'TradFi 品种上线：自适应网格策略' https://www.fmz.com/digest-topic/10951"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FMZ TradFi Perpetual Multi-Symbol Vol-Ranked Long-Only Geometric Grid with Hysteresis Rebalance (540030)

## Provenance

- **Source URL**: https://www.fmz.com/strategy/540030
- **Source type**: Public FMZ strategy page. **Substantial Python source is visible on the public page** (scan/score/grid/rebalance/stop logic and default parameter block); FMZ still gates “full source” login for copy/export.
- **Author on page**: ianzeng123
- **Platform**: FMZ / 发明者量化
- **Created (source-reported)**: 2026-05-11 15:02:11
- **Linked article**: https://www.fmz.com/digest-topic/10951 (identity preserved; body not required for defaults below)
- **Source reviewed as of**: 2026-09-20
- **Deduplication audit (2026-09-20; origin/main)**: No prior record cites FMZ id `540030` or this TradFi-perp vol-ranked long-only geometric grid + hysteresis rebalance construction. Adjacent records are different:
  - `binance-tradfi-equity-sector-long-short-momentum-rotation-fmz-549589-2026-09-18.md` — **sector long/short momentum rotation** on Binance TradFi equity perps; not vol-ranked grid inventory.
  - FMZ adaptive Kalman RLS-OU grid (545765 family) — crypto grid with recursive filters; different selection engine.
  - `fmz-fractional-kelly-capital-budget-long-only-grid-perpetual-2026-09-19.md` — capital-budget grid on crypto perps; not TradFi vol-rank multi-symbol.
  - FMZ delist-event short grid (535836) — event short grid; opposite thesis.
  - FMZ risk parity (535843) / flywheel (542065) — allocation architectures, not grid cells.
  - Concurrent QCML / CVaR / TV OI-flow records on origin/main as of this write — different sources and mechanisms.

## Economic mechanism

### Source-reported

Source-reported positioning: multi-symbol **pure grid** for **TradFi perpetual** contracts (equity indices, gold, oil, FX-style USDT perps). Does **not** predict direction or use complex indicators. Core slogan: **where volatility is highest, capital runs grids there.**

Source-reported rationale: TradFi underlyings are described as more fundamentally anchored than ordinary crypto, with lower extreme crash probability, allegedly better suited to range grid capture.

Source-reported construction (public Python):

1. **Universe scan:** `GetMarkets()`; keep symbols ending `USDT.swap` with `instCategory != 1` (source comment: category 1 = ordinary crypto perps; non-1 = TradFi). Optional `CATEGORY_FILTER` on `underlyingType`; `EXCLUDE_SYMBOLS` blacklist (default `NATGAS,CRCL`).
2. **Volatility score:** over last `KLINE_COUNT` **daily** bars,  
   `score = mean[(High - Low) / Close × 100%]`.
3. **Hard filter:** drop symbols with `avg_atr < GRID_RATIO × 100 × 1.5` (daily range must be at least 1.5× grid spacing percent).
4. **Selection:** top `TOP_N` by score (default **3**).
5. **Long-only geometric grid:** center near current price; range `[price×(1−LOWER_RANGE), price×(1+LOWER_RANGE)]` (public code uses **LOWER_RANGE only** for both sides in `build_grid`; panel also lists UPPER_RANGE — **asymmetry underspecified** vs code). Levels step by **`GRID_RATIO`** multiplicatively. Below current price: **buy open** limit; after fill: **sell close** at next higher grid; after TP: **re-place buy** at original level.
6. **Rebalance:** every `REBALANCE_HOURS` (default **48**); hysteresis — introduce a new symbol only if its ATR score **≥ weakest current ATR × (1 + HYSTERESIS)** (default hysteresis **0.20**). Rebalance cancels old grids, flattens old symbols, rebuilds on new names.
7. **Global stop:** if equity drawdown from initial equity **≥ STOP_LOSS_RATIO** (default **0.3** = 30%), cancel all, flatten, state `STOP`. `0` disables.
8. **Capital:** equal allocation across active symbols in narrative; each grid cell uses fixed **`GRID_VALUE` USDT** (default **50**).

Source-reported risk notes: grids suit ranging not one-way markets; price can fall through grid floor (inventory underwater); TradFi non-session liquidity can widen spreads; grid too tight → fee erosion; rebalance costs; leverage caution; global stop is last resort not complete protection.

Source-reported validation: public code + parameter panel; community question on performance left unanswered on page. **No published equity curve or net PnL series** on the public description as of 2026-09-20.

### Research interpretation

This is **volatility-ranked inventory provision** (long-only grid) on **crypto-venue TradFi perpetuals**, not directional alpha and not risk-parity allocation.

Research interpretation:

1. **Vol-rank → grid activity hypothesis:** Higher average daily range increases expected grid crossings per day; the source treats this as more TP opportunities. This is a **throughput** hypothesis, not a claim that expected return per unit risk is higher.
2. **Long-only grid = short gamma / short trend risk:** Profits if mean-reverting chop inside the band; inventory accumulates if price grinds down — source acknowledges this.
3. **Hysteresis as cost control:** Requiring +20% ATR improvement vs weakest held name reduces churn vs naive top-N refresh.
4. **TradFi packaging:** Same grid mechanics on SPY/XAU/CL-style USDT perps add session gaps, funding, and tracking vs cash markets.

Component roles (normalized from public source defaults):

```text
Universe: USDT.swap with instCategory != 1 (TradFi perps); exclude NATGAS,CRCL by default
Score: mean daily range % over KLINE_COUNT=20 bars
Gate: score ≥ 1.5 × GRID_RATIO×100
Hold: TOP_N=3 highest scores
Grid: geometric long-only; spacing GRID_RATIO=1.5%; cell size GRID_VALUE=50 USDT; band ~±LOWER_RANGE=10%
Rebalance: every 48h if new_score ≥ weakest_held × 1.20
Leverage: default 3× (SetMarginLevel)
Global stop: equity DD ≥ 30% → flatten and halt
Poll: LOOP_INTERVAL=30s
```

## Signal

### Formation timestamp

Public code uses completed daily bars for scoring (`GetRecords(..., PERIOD_D1, ...)`); grid sync polls live tickers every `LOOP_INTERVAL` seconds. Exact exchange timezone for “daily” bars **not published** (`underspecified`).

### Lookback

Source-reported default **`KLINE_COUNT = 20`** daily bars for average range score.

### Long entry

Source-reported: geometric **buy-open** limit at each grid level **below** current price; size `GRID_VALUE` USDT notional converted to contracts via `CtVal`/price; tick/lot/minSz alignment via exchange Info fields.

**No short grid** in public pure-grid code (long-only inventory).

### Short entry

None in source-reported pure-grid implementation.

### Exit / cell recycle

Source-reported per cell: after buy fill → **closebuy** limit at next higher grid level; after that fill → re-place buy at original level if still below price and state `RUN`. Symbol exit on rebalance or global stop via `close_all`.

### Holding period

Per cell: until next grid level is reached (unbounded in time). Portfolio: until rebalance replaces the name or global stop. No per-cell time stop in public code.

### Parameters (source-reported public defaults from Python block)

| Parameter | Default | Role |
|-----------|---------|------|
| TOP_N | 3 | Concurrent grid symbols |
| REBALANCE_HOURS | 48 | Rescan/rebalance interval |
| HYSTERESIS | 0.20 | New score ≥ weakest × 1.20 |
| LEVERAGE | 3 | Margin level |
| GRID_RATIO | 0.015 | 1.5% geometric spacing |
| GRID_VALUE | 50 | USDT per cell |
| LOWER_RANGE | 0.10 | ±10% band (code uses lower for both sides) |
| STOP_LOSS_RATIO | 0.3 | 30% equity DD halt |
| LOOP_INTERVAL | 30 | Seconds between sync loops |
| KLINE_COUNT | 20 | Daily bars for ATR score |
| CATEGORY_FILTER | ALL | Optional underlyingType filter |
| EXCLUDE_SYMBOLS | NATGAS,CRCL | Blacklist |

**Underspecified:** UPPER_RANGE vs code asymmetry; exact TradFi category taxonomy per venue; fees/funding model; fill priority under gaps; capacity.

### Position sizing

Equal narrative allocation across TOP_N names; fixed USDT per grid cell; leverage default 3×. Not vol-targeted beyond name selection.

### Specification completeness

**High for selection + grid + rebalance + stop** given public Python defaults; cost/funding/session details incomplete. Stronger reconstructability than many login-gated FMZ pages.

## Required data

- **Instrument:** exchange TradFi-classified USDT perpetuals (indices/metals/commodities/FX-style underlyings per venue metadata).
- **Venue:** FMZ-connected exchange with `instCategory` / `tickSz` / `lotSz` / `CtVal` metadata (public code reads these fields — Binance-like Info shape).
- **Timeframe:** D1 for scoring; intraday ticker poll for grid sync.
- **Fields:** daily OHLC; live last/tick; orders/positions; account equity.
- **Costs:** not modeled in public defaults; fees/slippage/funding material for grid throughput (`data gap`).

## Execution assumptions

Source-reported: limit buy/cancel/replace loop; order status polling; tick/lot alignment; leverage set at start. Not established: maker rebate vs taker on emergency exits, queue priority, partial fills under stress, funding PnL on held long inventory.

## Evidence

### Source-reported

- Public Python defaults and algorithms (scan, score, filter, grid build/sync, hysteresis rebalance, global stop) as listed above.
- Risk narrative (range suitability, floor breach, session liquidity, fee erosion).
- **No** source-reported Sharpe/CAGR/drawdown series on the public page; community performance question unanswered.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- Source-reported structural risks: one-way selloffs stack long inventory; fee/grid ratio tradeoff; rebalance costs; TradFi session liquidity; stop does not eliminate extreme loss.
- Research interpretation: vol-rank may select **event-risk** names (earnings, macro prints) where grids fail; long-only grid is short trend; 30% DD stop is late; no published live proof.
- Adjacent in-repo TradFi/grid records document different mechanisms and cost risks — not replications of 540030.

## Falsification plan

Research-proposed (not executed; not authorized):

1. **Vol-rank value (research-defined falsification threshold):** Compare TOP_N vol-ranked TradFi grids vs random or low-vol TradFi grids under identical cell size/spacing/fees; if high-vol selection does **not** increase net grid PnL per unit DD, the selection thesis fails for the sample.
2. **Grid vs buy-hold:** Same names/notional/band; if grid does not improve net vs buy-and-hold after costs in ranging subperiods, grid adds no value.
3. **Hysteresis ablation:** HYSTERESIS 0 vs 0.2 vs 0.5; if 0 does not destroy net after turnover costs, hysteresis is non-load-bearing.
4. **Fee stress:** GRID_RATIO 0.5% / 1.5% / 3% × taker/maker fee grid; fail if positive expectancy only at unrealistic zero fees.
5. **Session gap test:** Hold through TradFi closed-session gaps vs flatten before close (research-proposed); if gap risk dominates, session policy is first-order.
6. **Funding stress:** Include perpetual funding on long inventory.
7. **Action on failure:** Keep `research-only`; do not treat public code defaults as validated alpha.

## Crypto portability

**Portability: `direct` for venue packaging (already crypto-exchange TradFi perps); `unproven` for net outcomes.**

- Instruments are USDT perpetuals on a crypto venue — not cash equities.
- Risks: funding, tracking error, session liquidity, listing taxonomy (`instCategory` venue-specific), leverage liquidation at 3×, USDT depeg.
- Not portable as “pure TradFi cash grid” without re-validation.
- Crypto portability is not authorization to trade.

## Limitations

- **Risk/carry structure ≠ predictive alpha** — mechanism is grid inventory + vol selection.
- **not independently reproduced**
- **No public performance series.**
- **underspecified:** upper/lower band code vs panel; costs; capacity; venue category details.
- Full export still login-gated though public snippet is rich.
- Incremental value: **public reconstructable TradFi-perp vol-ranked long-only grid with numeric defaults**, distinct from sector-momentum TradFi records.

## Implementation status

No implementation in our research stack. Does not modify NautilusTrader/PyBroker; does not authorize Paper/Testnet/Live.

`implementation_status: not-implemented`

Source-side: FMZ hosts Python strategy; **not** treated as our validation.

## Adoption boundary

Research-only. Presence here does **not** mean profitable, validated, or approved for implementation, paper, testnet, or live trading.

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

## Related Wiki records

No stable Hermes Wiki Brain path known at write time. Do not fabricate Wiki links.

In-repo related: FMZ 549589 TradFi sector rotation; FMZ 545765 adaptive grid family; FMZ 535836 delist grid; risk-parity/flywheel FMZ records; Kelly grid family.

## Sources

1. FMZ Quant strategy page. 「TradFi多品种网格（纯网格版）」 / TradFi multi-symbol pure grid. Author ianzeng123. Strategy id 540030. Created 2026-05-11. https://www.fmz.com/strategy/540030 (public description + Python source/default block reviewed 2026-09-20).
2. FMZ article linked by the strategy page: 「TradFi 品种上线：自适应网格策略」 https://www.fmz.com/digest-topic/10951 (identity preserved; not used for performance claims this cycle).
