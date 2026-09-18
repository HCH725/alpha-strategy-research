---
schema: strategy-research-record-v1
title: "Binance TradFi Equity Sector Long/Short Momentum Rotation"
created: 2026-09-18
updated: 2026-09-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - tradfi
  - binance
  - equity-perpetual
  - cross-sectional
  - sector-momentum
  - long-short
  - rotation
  - inverse-volatility
  - basket-execution
status: research-only
confidence: medium
source_as_of: 2026-09-18
sources:
  - "FMZ Quant strategy platform, TradFi Equity Sector Long/Short Rotation Strategy, strategy id 549589, author ianzeng123, created 2026-09-16, page last modified approx. 17 hours before capture. https://www.fmz.com/strategy/549589"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Binance TradFi Equity Sector Long/Short Momentum Rotation

## Provenance

Public FMZ strategy page: **TradFi Equity Sector Long/Short Rotation Strategy**, strategy id `549589`, author ianzeng123. Canonical URL: https://www.fmz.com/strategy/549589. Created 2026-09-16; page last modified about 17 hours before this capture. Source reviewed as of 2026-09-18.

Repository deduplication on current `main` found no record with FMZ id `549589` or the same normalized sector-basket long/short rotation on Binance TradFi equity perpetuals. The adjacent record `gateio-tradfi-matrix-null-space-stat-arb-q-score-fshock-2026-09-15.md` concerns Gate.io TradFi perpetual residual mean-reversion via low-rank matrix null-space projection — a different venue, signal family (stat-arb residual vs sector momentum rank), and portfolio construction. Other equity sector-pairs records are cash-equity residual PCA, not Binance TradFi equity perps.

## Economic mechanism

### Source-reported

The FMZ description frames the product as Binance USDT-margined TradFi **equity perpetual contracts**, not actual shares. The stated hypothesis is cross-sectional sector momentum: compare relative strength across user-defined equity sectors; buy every valid member of the strongest sector and short every valid member of the weakest sector with equal long/short target notional, seeking continued outperformance of strong versus weak sectors while reducing broad market direction exposure.

The page explicitly warns that these perpetuals involve leverage, funding fees, liquidity risk, tracking error, off-hours price divergence, and liquidation risk; that long and short legs are submitted sequentially and cannot be guaranteed to fill simultaneously; and that fast markets may leave the portfolio temporarily incomplete.

### Research interpretation

The proposed economic channel is **cross-sectional momentum at the sector layer**, not single-name alpha: if sector-level information (semiconductors vs financials vs consumer vs healthcare in the source defaults) persists over a multi-day horizon on TradFi equity perps, a market-neutral-ish long strongest / short weakest basket can harvest relative strength. A secondary channel is **crypto-venue packaging of TradFi equity risk**: the same sector bet is expressed on a 24/7 perpetual venue, so funding, basis, and off-session price dynamics become part of the trade even when the underlying equity market is closed.

Scout interpretation only: the mechanism is not established by the page. Source validation status reports syntax/XML checks and offline Node tests on synthetic FMZ stubs only — not FMZ import, backtest, paper, or live results.

## Signal

Source-specified default rule (research-normalized; values are source defaults, not Scout-tuned):

- Instrument universe: Binance USDT-margined TradFi equity perpetual contracts listed in `SectorConfig`.
- Default sectors (source): Semiconductors, Financials, Consumer, Healthcare; each requires ≥2 valid members; no symbol duplicated across groups.
- Formation: at each evaluation, use closed 4H bars for every symbol. Lookback default `LookbackBars=30` (min 6) four-hour bars.
- Momentum: each stock’s return over the lookback window; sector momentum = arithmetic mean of member returns (only sectors with ≥2 valid members enter ranking).
- Ranking: order all valid sectors strongest → weakest.
- Entry gate: open only if momentum gap between strongest and weakest sectors ≥ `MinGapPct` (default 8 percentage points). If gap too small → remain flat / close managed positions. Fewer than two valid sectors → no target.
- Portfolio construction:
  - Buy **every** valid member of the top-ranked sector.
  - Short **every** valid member of the bottom-ranked sector.
  - Equal target notional per side (`PerSideNotional` default 100 USDT is side total, not per stock).
  - Within each side: reserve minimum quantity notional first, then allocate remaining budget **inversely proportional to each member’s volatility of 4H returns** (lower vol → larger weight).
- Rebalance / exit:
  - Re-evaluate rankings every `RebalanceHours` (default 24).
  - If strongest and weakest sectors unchanged and position directions still match stored target → hold without weight rebalance for price/vol drift.
  - If either target sector changes → close old basket, open new basket.
  - If momentum gap falls below threshold → close all managed positions → cash.
  - Portfolio stop: if combined unrealized loss on managed positions reaches `PortfolioStopPct` (default 5%) of current total gross notional → flatten and stop state; manual resume required.
  - Net exposure repair: missing/wrong-side/extra legs or long/short notional deviation above `NetExposureMaxPct` (default 10%) → attempt full flatten and re-evaluate.
- Execution mode: `EnableTrading=false` signal-only; `true` sets leverage (`Leverage` default 1) and submits market orders sequentially after canceling open orders and closing the previous basket. Partial open failure → attempt unwind of partially established basket.

Underspecified for full independent reproduction: exact member contract codes in the live `SectorConfig`; volatility window definition beyond “volatility of four-hour returns”; precise bar alignment/timezone convention for Binance TradFi equity perps; funding-rate treatment in the strategy logic (mentioned in risk text, not as a signal input); fill model for sequential multi-leg market orders.

## Required data

- Instrument: Binance USDT-margined TradFi equity perpetual contracts (source: not actual shares).
- Universe: symbols inside user `SectorConfig`; ≥2 sectors × ≥2 members; no cross-sector duplicates.
- Venue: Binance (FMZ `Futures` interface style for equity perps).
- Timeframe: closed 4H bars for momentum/vol; rebalance evaluation every 24 hours by default.
- Fields: close/return path for momentum; 4H return series for inverse-vol weights; live positions/orders for basket repair; gross notional for portfolio stop.
- Point-in-time: source uses closed bars; no look-ahead on incomplete 4H bars claimed.
- Timestamp: exchange timestamps on Binance TradFi products; off-hours divergence explicitly flagged by source risk text.
- Missing-data: members with insufficient history invalid; sectors need ≥2 valid members; full stale-bar handling not fully specified.
- Funding/fees/spread: source risk text lists funding fees, liquidity, tracking error; strategy parameters expose leverage and notional but not an explicit fee/funding model. Execution uses market orders — taker costs not parameterized on the page.

## Execution assumptions

Source-reported: default `EnableTrading=false`; market orders when enabled; sequential legs; cancel-then-close-then-open rotation; repair rounds `MaxRepairRounds=3`; net exposure and portfolio stop flatten rules; contracts in `SectorConfig` must not be shared with other strategies. Companion tests are offline synthetic only.

Scout assumptions not established by source: simultaneous two-sided fill probability; off-session basis risk size; whether sector membership on Binance TradFi perps is stable enough for multi-week rotation. Treat fillability and off-hours basis as unknown risks, not source-proven properties.

## Evidence

### Source-reported

FMZ page 549589 states the sector-momentum long/short rule, defaults (4H × 30 bars lookback, 24h rebalance, 8pp min gap, 100 USDT per side, inverse-vol weights, 10% net exposure cap, 5% portfolio stop), and validation status: JavaScript syntax, FMZ XML/parameter-JSON checks, and 28 offline Node.js tests on deterministic synthetic markets and FMZ API stubs covering ranking, whole-sector direction, budget, inverse-vol allocation, rotation, rollback, net exposure, portfolio stop, state recovery, and paper/live interface separation. The page explicitly states that FMZ import verification, FMZ backtesting, online paper operation, and small-size live trading have **not** been completed.

### Independently reproduced

not independently reproduced

### Negative evidence

No independent live or backtest ledger for this strategy was identified on the public FMZ page. Source itself flags funding, tracking error, off-hours divergence, sequential-leg incomplete baskets, and sector reversals as unresolved risks. Adjacent repository records already document cost/fill failures for multi-leg crypto stat-arb and TradFi residual strategies; those are adjacent negative context, not disproof of this sector-momentum construction. Absence of a public track record is not evidence of profitability.

## Falsification

Research-proposed falsification tests (not executed):

1. Walk-forward on immutable Binance TradFi equity-perp 4H panels: pre-declare failure if long-strongest/short-weakest sector basket net of taker fees and funding has non-positive mean return on a held-out later period under source defaults (30×4H lookback, 8pp gap).
2. Point-in-time audit: form sector ranks only from closed 4H bars available at rebalance timestamp; fail if any incomplete bar or equity-cash-session look-ahead enters momentum.
3. Placebo: randomize sector labels or shuffle member-to-sector mapping while preserving basket sizes; fail if real sector ranks are not better than shuffled.
4. Min-gap sensitivity: vary `MinGapPct` (e.g., 4/8/12/16); fail if sign of net edge is unstable or only the most extreme gap works in-sample.
5. Weight ablation: equal-weight vs inverse-vol within baskets; fail if edge appears only under one weighting after costs (would weaken the stated risk-allocation claim).
6. Funding/off-hours stress: add realistic funding and Binance-vs-cash off-session basis shocks; fail if edge is fully explained by funding/basis rather than sector momentum.
7. Execution/incompleteness stress: inject sequential-leg partial fills and 10% net exposure triggers; fail if realized equity curve collapses relative to complete-basket assumption.
8. Venue transfer: same sector definitions on cash equities or another TradFi-perp venue; fail if effect is unique to one venue’s listing set without a structural reason.

Each test requires a pre-declared failure rule; unconstrained retuning counts as falsification.

## Crypto portability

Mark: **adapted / partial — already crypto-venue-native**.

- Product type: Binance USDT-margined TradFi **equity perpetuals**, not spot equities or equity options. The signal is sector momentum on these synthetic perps.
- 24/7: contracts may trade continuously while underlying cash equities do not; off-hours price discovery and basis are first-order risks named by the source.
- Funding/borrow: perpetual funding applies to both legs; net funding is a return component not modeled as a signal on the public page.
- Fragmentation/listing: universe is whatever Binance lists as TradFi equity perps in `SectorConfig`; membership and liquidity can change.
- Crypto-specific data dependency: FMZ/Binance perpetual market data only — no on-chain fields required.
- Crypto portability is not authorization to trade.

## Limitations

- Public page + source header only; full implementation behind FMZ login.
- No independent reproduction; no FMZ backtest or live results claimed by source.
- Offline stub tests do not establish market efficacy.
- Sector definitions are user-configured defaults — researcher degrees of freedom.
- Multi-leg sequential market execution on equity perps is capacity- and latency-sensitive.
- Funding, off-hours basis, and tracking error can dominate or reverse paper sector-momentum edge.
- Related Gate.io TradFi null-space record is a different mechanism; do not treat this as a duplicate update.
- Incremental-write threshold: met via new venue/product family (Binance TradFi equity perps), sector-level momentum rank + whole-basket construction, and inverse-vol weighting — distinct from residual stat-arb TradFi captures.

## Implementation status

`not-implemented`. This research capture does not modify NautilusTrader, create a strategy family, authorize Paper/Testnet/Live, or write to Hermes Wiki Brain. Third-party FMZ code may exist on the platform; this repository record does not implement, run, or endorse it.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence here means only that the public hypothesis was normalized for intake review.

## Related Wiki records

Adjacent repository paths used for deduplication:

- `gateio-tradfi-matrix-null-space-stat-arb-q-score-fshock-2026-09-15.md` — different venue and residual null-space mechanism.
- `sp500-sector-pairs-causal-residual-pca-area-asymmetry-2026-09-12.md` — cash-equity residual pairs, not Binance TradFi perps.
- `crypto-cross-sectional-meme-momentum-funding-dynamic-rotation-2026-09-14.md` — crypto meme cross-section, not TradFi equity sectors.

No Hermes Wiki Brain write was performed.

## Sources

- FMZ Quant, TradFi Equity Sector Long/Short Rotation Strategy, https://www.fmz.com/strategy/549589 (public description and parameters; captured 2026-09-18).
