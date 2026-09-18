---
schema: strategy-research-record-v1
title: "FMZ Adaptive Dynamic Grid: Online Kalman Trend + RLS-OU Residual Width"
created: 2026-09-18
updated: 2026-09-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - grid-trading
  - mean-reversion
  - kalman
  - rls
  - ornstein-uhlenbeck
  - cointegration
  - regime-switching
  - avellaneda-stoikov
  - perpetual-futures
  - fmz
status: research-only
confidence: medium
source_as_of: 2026-09-18
sources:
  - "FMZ Quant strategy platform, 通用网格策略（数学自适应版v4.1） / Mathematical Adaptive Dynamic Grid v4.2, strategy id 545765, author ianzeng123, created 2026-07-14, page last modified approx. 2 months before capture. https://www.fmz.com/strategy/545765"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FMZ Adaptive Dynamic Grid: Online Kalman Trend + RLS-OU Residual Width

## Provenance

Public FMZ strategy page: **通用网格策略（数学自适应版v4.1）**, description labels the logic **数学自适应动态网格策略（V4.2）**. Strategy id `545765`, author ianzeng123. Canonical URL: https://www.fmz.com/strategy/545765. Created 2026-07-14; page last modified about two months before this capture. Source reviewed as of 2026-09-18 (public description and visible parameter surface; full source behind FMZ login).

Repository deduplication on current `main` found no record with FMZ id `545765` or the same normalized rule (perpetual grid whose range width, direction mode, trend gates, and take-profit decay are driven by **online recursive estimates** — Kalman local level/slope + RLS-AR(1)/OU on cointegration residuals — rather than fixed lookback windows). Adjacent record `crypto-dynamic-grid-trading-adaptive-boundary-resets-2026-09-02.md` is a different academic construction (adaptive boundary resets); other Kalman/OU records concern pairs trading, portfolio MACD, or ETH Kalman breakouts, not this grid stack.

## Economic mechanism

### Source-reported

The FMZ description states that traditional grids suffer from hand-picked parameters, bag-holding in one-way trends, and under-earning in ranges. The design principle is:

> **Time scale is an estimated output, not a human-chosen window.**

All key states (trend, volatility, mean-reversion half-life, equilibrium amplitude) update online on each closed bar. The page names three estimators plus inventory-aware risk:

1. **Kalman local level + slope** on price → instantaneous trend slope and volatility σ; dimensionless trend strength `z = slope / σ`; observation noise adapted online (no fixed N-bar window).
2. **RLS-AR(1) / OU** fitted to **cointegration residual ε** (not raw price) → mean-reversion half-life `H` and equilibrium std `σ_eq`. Grid width scales with `σ_eq`; forgetting factor is set self-consistently from estimated H.
3. **Optional cross-asset cointegration confirmation** — reference contracts; EWMA β on aggregated returns (anti-Epps); distinguish **systemic trend** (confirmed by references → block counter-trend entries) from **idiosyncratic noise** (target moves alone → harvest). Reference freeze/stale detection falls back to target-only z when references are closed.
4. **Inventory-aware discrete Avellaneda-Stoikov-style ceiling/floor**: long inventory accumulation presses the effective upper grid bound down; short inventory mirrors on the lower bound.

Five gates before opening a new grid leg (source order): trend gate; hard net-exposure cap; inventory-skew ceiling/floor; equity drawdown breaker; and **k×H take-profit decay** — if inventory age exceeds `k` estimated half-lives without reversion, TP price decays toward current price (still covering fees); adverse-regime ages count double. σ_drift rebuild recreates the range when width ratio leaves ~[0.75, 1.33] after cooldown. Auto direction mode switches long/short/both by Kalman z with hysteresis (enter trend at ±T, exit to range at ±T/2); old positions are not force-flattened — trend gate stops adds and TP decay exits.

Grid count maximization (v4.2): subject to (1) step ≥ bilateral fees × coverage multiplier and (2) per-grid capital ≥ exchange min qty/notional; take the min of the two constraints; equal capital per grid.

### Research interpretation

The falsifiable research hypothesis is **not** “grids print money.” It is narrower:

> In crypto perpetuals that alternate between range and trend, a grid whose **width, side, and exit clock** are set by **online** estimates of trend z and residual OU half-life/σ_eq should (a) reduce counter-trend inventory in confirmed systemic trends and (b) avoid fixed-window mis-calibration of grid spacing when volatility/regime shifts, relative to a fixed-parameter grid on the same instrument.

Secondary channel: cointegration-confirmed systemic vs idiosyncratic decomposition — only reference-confirmed trends block mean-reversion entries, so idiosyncratic spikes can still be harvested.

Scout interpretation: the page discloses engineering rules, not validated performance. No public live ledger or walk-forward table is claimed on the FMZ description. Treat the economic hypothesis as untested research material.

## Signal

Source-specified reconstruction (research-normalized; source defaults where exposed):

- Instrument: crypto perpetual futures on FMZ (description targets contract markets; example backtest snippet on the page references OKX SPACEX_USDT — treat symbol as illustrative).
- Bars: closed bars only for estimator updates; last incomplete bar skipped.
- Formation/entry timing: grid limit orders rest at computed levels; new entries only if all gates pass at order-check time.
- Lookback: **none fixed by design** — Kalman/RLS recursive state; source exposes warmup bar count (`EST_WARMUP`) and adaptive rates rather than N-bar momentum windows. Reference β uses aggregated multi-bar returns (`BETA_AGG_BARS`) to mitigate Epps bias.
- Entry (grid mechanics):
  - Long grid: bid below grid price, TP at previous grid level (or configured step).
  - Short grid: offer above grid price, TP at next lower grid.
  - Both/auto: range mid splits long below / short above, or side selected by regime.
  - Auto side: z ≥ +T → long-biased grid; z ≤ −T → short-biased; |z| small → both; hysteresis + cooldown on switches.
- Exit:
  - Primary: grid take-profit at adjacent level when price mean-reverts one step.
  - Secondary: **k×H TP decay** when age > `K_EXIT_HALFLIFE × H` without fill of TP; decay toward price ± fee cover; adverse z doubles effective age.
  - Risk flatten: drawdown breaker, manual close-all, net-exposure repair paths in code.
  - Range rebuild / direction switch cancels **open entry** orders only; existing inventory held until TP decay/trend gate exit logic.
- Holding period: from fill to adjacent-grid TP or decay exit; expected duration tied to estimated OU half-life (source exit clock uses H in bars, clamped to [HL_MIN_BARS, HL_MAX_BARS], fallback HL_FALLBACK=240).
- Parameters (source-exposed families, not Scout-tuned): direction mode (long/short/both/auto); initial price / range width %; shift step %; breakout trigger %; leverage; fee rate; fee coverage multiplier; Kalman responsiveness / Q ratio; vol adapt rate; trend-z threshold; OU memory; width σ multiplier and floor/cap; reference symbols; β aggregate bars; max net exposure mult; inventory skew; drawdown breaker %; exit half-life multiplier; capital fraction; grid count derived not hand-set when estimators ready.

Underspecified for bit-exact reproduction without full source: numeric defaults for several estimator gains; exact fee values; full state machine edge cases under partial fills; live `REF_SYMBOLS` lists.

## Required data

- Instrument: single perpetual contract target + optional reference perps for systemic confirmation.
- Venue: FMZ-connected exchange futures API (page example OKX-style; product-agnostic in description).
- Timeframe: 1-minute-class closed bars in visible code comments (`PERIOD_M1` / records); estimator updates on new closed bars.
- Fields: OHLC closes for Kalman; log returns for β; positions/equity for inventory and drawdown gates; exchange min qty/notional for grid sizing.
- Point-in-time: closed-bar only for estimators; no claim of tick-level lookahead protection beyond that.
- Timestamp: exchange bar times; reference stale if lag > `REF_STALE_BARS` bars.
- Missing-data: reference freeze detection; OU half-life unestimable → last valid H or fallback; grid not built if range/capital constraints fail.
- Funding/fees: fee rate parameter used in min-step and TP-decay fee cover; funding not modeled as alpha input in the public description.

## Execution assumptions

Source-reported: limit-order grid placement; cancel-open-entries-only on rebuild/switch; equal capital per grid; min notional/qty respected; optional manual range buttons; learning/research disclaimer — not investment advice; full backtest before live. Page does not present a validated live track record.

Scout assumptions not established by source: fill probability at grid bids in fast trends; queue position; maker vs taker fee actuals; liquidation behavior under leverage during one-way moves despite gates.

## Evidence

### Source-reported

FMZ page 545765 discloses the online estimator stack (Kalman level+slope, RLS-OU on cointegration residual, optional reference confirmation with Epps-aware aggregation, inventory ceiling/floor, k×H TP decay, σ_eq width rebuild, auto direction with hysteresis, five risk gates, v4.2 grid-count rule). A code-comment backtest header on the page shows a short OKX SPACEX_USDT example window (2026-05-07 to 2026-05-19) as platform metadata — not a research-grade performance study. Source text is educational/research-oriented with risk warnings.

### Independently reproduced

not independently reproduced

### Negative evidence

No independent replication of this FMZ parameterization was identified. Adjacent repository records already document null/fragile results for many fixed-parameter grids, funding-carry cost decay, and mean-reversion overfit — relevant priors, not disproof of the online-estimator construction. Absence of a public live PnL on the page is not evidence of profitability. Source-community comments on related FMZ momentum systems note regime dependence; not transferable proof for this grid.

## Falsification

Research-proposed falsification tests (not executed):

1. Paired walk-forward: same perpetual, same period — fixed-width grid vs this adaptive stack; research-defined falsification threshold: fail if adaptive net-of-fees return is ≤ fixed baseline on a majority of held-out windows, or if adaptive drawdown is not improved when the stated goal is regime robustness.
2. Estimator ablation: freeze Kalman z / freeze OU H at sample medians; fail the “online estimates matter” claim if ablated performance is equal or better.
3. Reference ablation: remove cointegration confirmation; fail the systemic-vs-idiosyncratic claim if trend-gate benefit vanishes or reverses.
4. Parameter perturbation: ±20–50% on trend threshold, width σ mult, k in k×H; fail if edge sign is unstable.
5. Placebo references: shuffle reference symbols; fail if real references outperform shuffled only in-sample.
6. Cost/latency stress: taker fees + adverse selection on decay exits; fail if net edge non-positive.
7. Trend-regime holdout: pure one-way quarters; fail if gates do not reduce counter-trend inventory loss versus ungated grid.
8. Leakage audit: recompute H/σ_eq/z only from closed bars available at decision time; fail if any incomplete-bar input is used.

Unconstrained retuning to rescue performance counts as falsification.

## Crypto portability

Mark: **direct / adapted** — already a crypto perpetual construction.

- Perp vs spot: inventory, leverage, and funding matter; description is contract-oriented.
- 24/7: continuous bars; reference “closed market” stale logic relevant if TradFi-linked refs used.
- Fragmentation: single-venue grid in the public description; cross-venue port not specified.
- On-chain data: not required.
- Crypto portability is not authorization to trade.

## Limitations

- Public page + partial code comments; full source gated.
- `not independently reproduced`.
- Grid + leverage remains vulnerable to gaps/liquidations despite gates.
- Estimator identification is weakly constrained (H, σ_eq can be unstable near unit root).
- Research degrees of freedom: many exposed parameters invite overfit if someone “optimizes” later.
- Adjacent adaptive-boundary grid record is a different mechanism — do not treat as duplicate update of that file.
- Incremental-write threshold: met via new signal construction (online Kalman+RLS-OU residual width + systemic confirmation + k×H decay) distinct from fixed-window grids and from boundary-reset grids.

## Implementation status

`not-implemented`. This capture does not modify NautilusTrader, create a strategy family, or authorize Paper/Testnet/Live. Third-party FMZ code may exist; this record does not implement or endorse it.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

## Related Wiki records

- `crypto-dynamic-grid-trading-adaptive-boundary-resets-2026-09-02.md` — different adaptive-grid construction.
- `crypto-perpetual-pairs-trading-kalman-cointegration-falsification-2026-09-11.md` and other Kalman/OU pairs records — different use of Kalman/OU (pairs, not single-name grid).
- `tradingview-rsi-box-volume-weighted-grid-breakout-2026-09-16.md` — breakout-in-grid TV script, different signal.

No Hermes Wiki Brain write was performed.

## Sources

- FMZ Quant, 通用网格策略（数学自适应版v4.1）/ V4.2 adaptive dynamic grid, https://www.fmz.com/strategy/545765 (public description; captured 2026-09-18).
