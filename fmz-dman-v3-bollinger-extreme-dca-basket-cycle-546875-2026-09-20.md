---
schema: strategy-research-record-v1
title: "FMZ D-Man V3 Bollinger Extreme Mean-Reversion DCA with Vol-Scaled Basket Cycle (546875)"
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - mean-reversion
  - bollinger
  - dca
  - cycle-budget
  - basket-exit
  - fmz
status: research-only
confidence: low
source_as_of: 2026-08-04
sources:
  - "FMZ digest article: 'Implementing the D-Man V3 Bollinger Band Reversal DCA Strategy in Rust on FMZ', digest topic 11002, created 2026-08-04. https://www.fmz.com/digest-topic/11002"
  - "FMZ strategy page (source-linked from digest): strategy id 546875. https://www.fmz.com/strategy/546875"
  - "Hummingbot public framework (source-reported base): directional_trading.dman_v3 — cited by the FMZ article as the public implementation lineage."
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FMZ D-Man V3 Bollinger Extreme Mean-Reversion DCA with Vol-Scaled Basket Cycle (546875)

## Provenance

- **Source URL (article):** https://www.fmz.com/digest-topic/11002
- **Source URL (strategy):** https://www.fmz.com/strategy/546875
- **Source type:** Public FMZ digest with Rust implementation narrative, formulas, and default parameter table; companion public strategy page.
- **Platform:** FMZ / 发明者量化
- **Created (source-reported):** digest 2026-08-04
- **Source lineage (source-reported):** Based on Hummingbot’s publicly available `directional_trading.dman_v3` framework; FMZ Rust port discussed in the digest. **Hummingbot repository full commit SHA not captured this cycle** (`data gap` under GitHub provenance rule for the upstream lineage).
- **Source reviewed as of:** 2026-09-20 (full digest body + strategy URL identity)
- **Deduplication audit (2026-09-20; origin/main):** No prior record cites FMZ id `546875`, digest topic `11002`, or D-Man V3. Adjacent records are different:
  - `fmz-fractional-kelly-capital-budget-long-only-grid-perpetual-2026-09-19.md` — fractional Kelly capital budget on long-only grid; not BB% first-cross + BB-width DCA basket cycle.
  - FMZ TradFi vol-ranked grid (540030) — multi-symbol vol-rank inventory; not band-extreme mean reversion.
  - FMZ adaptive Kalman RLS-OU grid (545765) — different filter engine.
  - FMZ flywheel (542065) / risk parity (535843) — capital architectures, not this cycle construction.

## Economic mechanism

### Source-reported

Source-reported problems with fixed grids: distorted spacing under changing vol; averaging rules without locked total budget; orders/positions can disconnect (partial fills, restarts).

Source-reported D-Man V3 placement: one **cycle-management** framework where

1. **Bollinger %B** identifies statistical extreme (entry hypothesis),
2. **Bollinger half-width** sets DCA layer scale (volatility-adaptive grid),
3. **Filled layers exit as one basket** at average position price,
4. **Cycle budget** is fixed before entry.

Source-reported construction:

- `%B = (Close - Lower) / (Upper - Lower)` on **closed** candles only (second-to-last bar as current closed).
- Interface `BBLength = 100`; internal `BB_STD = 2.0`; `LONG_THRESHOLD = 0`; `SHORT_THRESHOLD = 1`; `REQUIRE_CROSS = true` (first cross into extreme only).
- `HalfWidthRatio = (Upper - Lower) / (2 × Middle)`; `ScaleRatio = clamp(HalfWidthRatio, 0.2%, 8%)`.
- Anchor = latest traded price at signal; long layers `Anchor × (1 − Factor[i] × ScaleRatio)`; short mirrored.
- Baseline **DCA distance factors:** `0.05, 0.35, 0.75, 1.25`.
- Baseline **amount weights:** `1, 1, 1.5, 2.5` (~16.7% / 16.7% / 25% / 41.7% of cycle budget).
- `CycleBudget = min(TotalCycleQuote, AccountEquity × MaxCycleEquityPct)`; defaults `TotalCycleQuote=1000`, `MaxCycleEquityPct=10%`.
- Exits (same ScaleRatio fixed at signal): stop `3.00 × ScaleRatio`; take-profit `1.00 × ScaleRatio`; trailing activate `0.80 × ScaleRatio`; pullback `0.25 × ScaleRatio`; middle-band exit if basket profit ≥ internal `MIN_PROFIT_PCT=0.15%`; time exit `MaxHoldingBars=192`.
- Defaults also: `SignalPeriodMinutes=15`; buy prices rounded **down**, sells **up**; reject cycle if any two layers quantize to same price or min/max notional violated.
- Order ownership + persistent cycle state machine; unknown ownership → HALT.

Source-reported risk notes: suited to liquid mean-reverting regimes; dangerous in persistent one-way markets; vol regime jumps vs historical half-width; cost/funding erosion; budget cap does not make countertrend expectancy positive.

Source-reported evaluation guidance: record per-cycle capital, layer fill contribution, MAE, holding, exit-type mix, fees/funding share of gross — **not** net profit alone. Backtest screenshots exist on the page; **no audited performance table** restated as validated edge in this capture.

### Research interpretation

This is **band-extreme mean-reversion inventory provision** with **volatility-scaled multi-layer DCA** and **pre-committed cycle capital** — risk/path control is explicit; predictive claim is thin (revisit from %B extreme toward mid-band).

Research interpretation:

1. **First-cross filter:** limits stacked countertrend exposure when price stays outside the band — capacity/risk control, not proof of edge.
2. **Half-width as scale:** hypothesizes adaptive spacing tracks realized vol better than fixed % grid — unproven vs fixed spacing in this source.
3. **Basket exit:** reduces fragmented TP management; average-entry still accumulates in trends.
4. **Budget lock:** rejects unlimited martingale-style budget expansion after losses.
5. **Boundary:** mean reversion + DCA is **not** new alpha family by itself; incremental value is **public reconstructable defaults + cycle/basket semantics + explicit falsification framing**, not a claim of profitability.

Component roles (normalized):

```text
Regime/context: liquid market assumed; not a formal regime filter
Primary signal: closed-candle first cross of BB% ≤ 0 (long) or ≥ 1 (short), BBLength=100, STD=2
Scale: Clamp((U-L)/(2M), 0.2%, 8%) × factors [0.05,0.35,0.75,1.25]
Budget: min(1000 quote, equity×10%); weights [1,1,1.5,2.5]
Exit: basket at avg price; SL 3×ScaleRatio; TP 1×ScaleRatio; trail 0.8/0.25; mid-band if ≥0.15% profit; MaxHoldingBars=192
Risk/ops: one cycle per symbol; ownership HALT; cancel remainder before basket close
```

## Signal

### Formation timestamp

Closed bar only: FMZ `GetRecords`; uses second-to-last candle as current closed; forming bar excluded. Timeframe default **15 minutes** (`SignalPeriodMinutes=15`). Timezone/exchange clock not fully specified (`underspecified`).

### Lookback

`BBLength = 100` closed bars for middle/upper/lower (STD=2). Need at least 100 closed bars before first signal.

### Long entry

1. Closed bar %B ≤ 0 **and** previous closed bar %B > 0 (first cross).
2. Anchor = latest traded price at signal.
3. Place post-only/limit-style DCA plan at four long prices using ScaleRatio × factors.
4. Layers fill as price continues down; cycle rejected if constraints fail.

### Short entry

Mirror: %B ≥ 1 with previous %B < 1; layers above anchor.

### Exit (basket)

All filled layers treated as one position at exchange average price:

- Hard SL when basket return ≤ −3.00 × ScaleRatio (direction-aware return formula).
- TP when basket return ≥ +1.00 × ScaleRatio.
- Trailing after activation at +0.80 × ScaleRatio with 0.25 × ScaleRatio pullback allowance.
- Mid-band exit if price returns to middle band **and** basket profit ≥ 0.15%.
- Time exit after `MaxHoldingBars=192` bars.
- Exit path: stop new exposure → cancel residual DCA orders → basket close of **actual** size → confirm zero twice.

### Holding period

Expected: short mean-revert cycle; max: 192 bars of the signal timeframe (~48 hours at 15m) unless SL/TP earlier.

### Parameters (source-reported public defaults)

| Parameter | Default | Role |
|-----------|---------|------|
| SignalPeriodMinutes | 15 | Bar grid |
| BBLength | 100 | Band lookback |
| BB_STD (internal) | 2.0 | Band std |
| LONG/SHORT_THRESHOLD (internal) | 0 / 1 | %B extremes |
| REQUIRE_CROSS (internal) | true | First-cross only |
| DCA_SCALE_MIN/MAX_PCT (internal) | 0.2% / 8% | Half-width clamp |
| DcaSpreadFactors | 0.05,0.35,0.75,1.25 | Layer distances × ScaleRatio |
| DcaAmountWeights | 1,1,1.5,2.5 | Budget share per layer |
| TotalCycleQuote | 1000 | Cycle quote budget |
| MaxCycleEquityPct | 10% | Equity cap on cycle |
| StopLossBandFactor | 3 | SL = 3×ScaleRatio |
| TakeProfitBandFactor | 1 | TP = 1×ScaleRatio |
| Trailing activate / pullback (internal) | 0.8 / 0.25 × ScaleRatio | Trail |
| MIN_PROFIT_PCT (internal) | 0.15% | Mid-band exit floor |
| MaxHoldingBars | 192 | Time exit |

**Underspecified:** full FMZ export login-gating; exact fee/funding model; Hummingbot upstream SHA; empirical win rates.

### Position sizing

Per-layer quote share of locked cycle budget; deeper layers get more notional but **no extra layers** beyond four; total commitment capped.

### Specification completeness

**High for signal + scale + basket exit + budget** from public digest defaults; live costs and upstream Git SHA incomplete.

## Required data

- **Instrument:** crypto perpetual (digest examples use ETH-style linear contracts); FMZ `GetMarkets()` contract metadata (CtVal, tick/lot, min notional).
- **Venue:** FMZ-connected exchange (Binance-like fields described).
- **Market type:** perpetual futures/spread products as configured.
- **Timeframe:** default 15m completed bars.
- **Fields:** OHLC for %B and half-width; last price for anchor; equity for cycle cap; orders/positions for cycle state.
- **Point-in-time:** closed bars only; no forming-bar signals (source explicitly fixed incomplete-bar bug class).
- **Timestamp:** FMZ bar times; exchange specifics not fully stated.
- **Missing data:** incomplete bars excluded; min data = BBLength + previous bar.
- **Costs:** source stresses fees + funding on multi-leg cycle; not modeled in defaults (`data gap` for quantified cost series).

## Execution assumptions

Source-reported:

- Limit/DCA orders at planned prices; quantize buy down / sell up.
- Exit after cancel confirmation; close **actual** position size.
- Unknown order outcome → pause, do not blind-resend.
- Unclear ownership / position mismatch → HALT.
- Leverage/position mode defined in advance, not optimized as strategy params.

Not established: queue priority, partial-fill economics, maker rebates, impact.

Research interpretation: path-dependent execution risk is material for multi-layer DCA; treat public defaults as reconstructable **research** rules, not fill proofs.

## Evidence

### Source-reported

All construction defaults in this record trace to FMZ digest **11002** (2026-08-04; reviewed 2026-09-20) and strategy **546875**:

- %B first-cross rule; BBLength 100; STD 2; ScaleRatio clamp 0.2–8%; factors and weights as table; budget min(1000, equity×10%); SL/TP/trail/mid-band/time exits; state-machine and HALT semantics.
- Source-reported **risk narrative** (one-way market, vol jump, cost erosion) — primary negative-adjacent content.
- Source reports screenshots of equity/logs on the page; **this capture does not treat them as independently validated performance**.
- Source framing: educational/research/software design; not investment advice.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- Source-reported structural risks: persistent trends + deeper DCA concentrate notional at max risk; historical half-width may miss event vol; multi-layer fees/funding can erase thin TP; budget cap limits size but does not flip negative expectancy.
- Research interpretation: %B first-cross is a weak predictor without regime confirmation; basket SL 3× vs TP 1× implies high win-rate dependency after costs.
- No independent re-run of 546875 this cycle.
- Absence of our replication is not evidence of failure — only unverified.

## Falsification plan

Research-proposed (not executed; not authorized):

1. **Dynamic vs fixed spacing (research-defined falsification threshold):** Same signals/budget/fees; ScaleRatio from half-width vs fixed % spacing of equal mean. Fail vol-adaptation claim if dynamic does not improve net cycle PnL per unit max DD in the sample.
2. **First-cross ablation:** Cross-only vs every-bar-while-outside; fail if cross-only does not reduce adverse stacking without destroying gross mean reversion.
3. **Basket vs per-layer exit:** Fail if basket exit is worse on net after partial-fill realism.
4. **Budget cap ablation:** Uncapped martingale weights vs locked cycle budget; document that unbounded DCA may show better path-dependent demos until tail failure — fail any claim that treats unbounded demos as safer.
5. **Regime split:** Range vs trend vs event jump subperiods; **fail long-term suitability** claims if all net edge concentrates in calm ranges and fails trend/event splits after costs.
6. **Cost grid:** 0 / maker-only / taker / taker+funding; fail if positive expectancy only at zero cost.
7. **Action on failure:** Keep `research-only`; do not treat FMZ 546875 or Hummingbot lineage as validated alpha.

## Crypto portability

**Portability: `direct` for venue packaging (crypto perps on FMZ-style APIs); `unproven` for net outcomes.**

- Mechanism is price-band mean reversion + DCA inventory — portable across crypto pairs in form.
- Risks: funding, liquidation, gaps, exchange failure, 24/7 event moves, contract CtVal pitfalls.
- Not portable as “safe grid” without cost/regime evidence.
- Crypto portability is not authorization to trade.

## Limitations

- **Risk/path structure ≠ predictive alpha.**
- **not independently reproduced**
- **No audited public performance table** used as evidence in this record.
- **underspecified / data gap:** Hummingbot commit SHA; live fees/funding series; full source export.
- Adjacent Kelly/grid records share capital-control themes but different signal construction — do not merge conclusions.
- Incremental value: **public reconstructable FMZ D-Man V3 defaults + basket cycle + explicit negative risk framing**, distinct from fractional Kelly budget and vol-ranked TradFi grids.

## Implementation status

No implementation in our research stack. Does not modify NautilusTrader/PyBroker; does not authorize Paper/Testnet/Live.

`implementation_status: not-implemented`

Source-side: FMZ hosts Rust strategy 546875; Hummingbot public dman_v3 cited without immutable SHA this cycle — **not** treated as our validation.

## Adoption boundary

Research-only. Presence here does **not** mean profitable, validated, or approved for implementation, paper, testnet, or live trading.

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

## Related Wiki records

No stable Hermes Wiki Brain path known at write time. Do not fabricate Wiki links.

In-repo related: fractional Kelly grid FMZ; TradFi vol-ranked grid 540030; Kalman RLS-OU grid 545765; flywheel 542065; risk-parity 535843 (different mechanisms).

## Sources

1. FMZ Quant. 「Implementing the D-Man V3 Bollinger Band Reversal DCA Strategy in Rust on FMZ.」 Digest topic 11002, created 2026-08-04. https://www.fmz.com/digest-topic/11002 (full article body reviewed 2026-09-20).
2. FMZ Quant strategy page. Strategy id 546875. https://www.fmz.com/strategy/546875 (identity preserved; linked from digest conclusion).
3. Hummingbot public framework lineage as cited by the FMZ article: `directional_trading.dman_v3` (full repository commit SHA not captured 2026-09-20).
