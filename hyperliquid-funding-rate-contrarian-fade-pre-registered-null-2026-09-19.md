---
schema: strategy-research-record-v1
title: "Hyperliquid Funding-Rate Contrarian Fade: Pre-Registered 8-Month Null Result with Bootstrap Inference"
created: 2026-09-19
updated: 2026-09-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - funding-rate
  - contrarian
  - perpetual-futures
  - hyperliquid
  - negative-result
  - pre-registered
  - bootstrap
status: research-only
confidence: high
source_as_of: 2026-01-24
sources:
  - "https://github.com/Paris0t/midas-funding-bot (MIT; single commit on main branch; created 2026-01-24)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Hyperliquid Funding-Rate Contrarian Fade: Pre-Registered 8-Month Null Result with Bootstrap Inference

## Provenance

- **GitHub repository:** https://github.com/Paris0t/midas-funding-bot
- **License:** MIT
- **Author:** Nathan P. (Paris0t)
- **Default branch:** main (single commit; no commit SHA available for immutable pinning)
- **Created:** 2026-01-24
- **Platform:** Hyperliquid perpetual futures
- **Universe:** ~230 Hyperliquid perpetual contracts (full universe scanned once per minute)
- **Data period:** ~8 months of continuous paper trading (approximately January–August 2026)
- **Primary source inspection:** The repository README, source file structure, and methodology documentation were directly accessed and audited on 2026-09-19. The codebase was not run; all performance claims are source-reported from the README.

## Economic mechanism

### Source-reported

Perpetual funding rates are periodic payments between longs and shorts that tether the perpetual price to spot. When funding is deeply positive, longs are crowded and paying to hold; when deeply negative, shorts are crowded. The hypothesis: extreme funding marks over-positioning, so **fade the crowd** — go long when funding is deeply negative (shorts are overcrowded), short when deeply positive (longs are overcrowded) — and earn both the eventual mean-reversion and the funding itself while the crowd unwinds.

### Research interpretation

This is a **crowded-positioning mean-reversion** hypothesis. The core mechanism is:

1. Extreme funding rates indicate crowded directional positioning.
2. Crowded positions are vulnerable to forced unwinding (liquidations, stop-outs).
3. The contrarian side captures the mean-reversion AND collects funding while the crowd exits.

The hypothesis is economically reasonable and well-documented in market microstructure literature (Brunnermeier & Pedersen 2009 on funding-liquidity spirals). The question is whether it survives execution costs at retail size.

The existing repo record `crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11` (Bryan Vine, Paper 2) finds the cross-sectional funding factor is real but modest (~0.4 OOS Sharpe). This record tests a different mechanism: **contrarian fading of extreme funding** (not cross-sectional ranking). The mechanisms are related but distinct — the cross-sectional factor exploits relative-value dispersion, while the contrarian fade exploits crowded-positioning mean-reversion.

## Signal

### Formation timestamp
- Scanned once per minute on live Hyperliquid data.
- No historical backtest; all signals are real-time paper trades.

### Lookback
- Trailing funding rate for each of ~230 perpetuals.
- Entry when |annualized funding| exceeds an adaptive threshold (exact threshold not specified in README).

### Long entry
- When funding rate is deeply negative (shorts crowded): go long the perpetual.
- Entry gates include: OI, volume, ADX, momentum, signal persistence, premium/funding alignment, cross-exchange confirmation, amplitude, time-of-day, z-score spike-vs-structural.

### Short entry
- When funding rate is deeply positive (longs crowded): go short the perpetual.
- Same entry gate suite as long entry.

### Exit
- Asymmetric exit ladder (priority order):
  1. ATR stop (3× ATR)
  2. Hard max-loss (−2%)
  3. Breakeven arm after +1% peak
  4. Partial take-profit (50% at +2%)
  5. Trailing stop at +3%
  6. 7-day timeout

### Position sizing
- Dynamic Kelly sizing (exact formula not specified in README).
- Capital rotation across signals.

### Parameters
- All entry thresholds, exit levels, and gating parameters are research-proposed (source does not disclose exact values).
- The adaptive funding threshold, entry gate thresholds, and exit ladder levels are underspecified in the source.

### Signal underspecification
- The exact entry threshold for extreme funding is not disclosed.
- The entry gate parameters (OI, volume, ADX, momentum thresholds) are not disclosed.
- The Kelly sizing formula parameters are not disclosed.
- This is a prototype/research system; exact parameters may be proprietary or unfinalized.

## Required data

- **Instrument:** ~230 Hyperliquid perpetual contracts (full universe).
- **Venue:** Hyperliquid.
- **Market type:** USDC-margined perpetual futures.
- **Timeframe:** 1-minute scanning cadence; signal evaluation on live data.
- **Fields:** Funding rate, open interest, volume, ADX, momentum indicators, premium/funding alignment, cross-exchange reference prices (Coinbase + Kraken websockets).
- **Point-in-time:** Live paper trading; no look-ahead.
- **Timestamp:** Real-time WebSocket data from Hyperliquid.
- **Missing data:** Not applicable for live trading; the system handles data gaps via its streaming architecture.

## Execution assumptions

- **Signal-to-order timing:** Signal scanned every 60 seconds; GTC limit orders with native stop-loss triggers.
- **Order type:** Maker entries (ALO — Post-Only limit orders).
- **Fill model:** Paper trading against live market data; no real fills.
- **Fees:** Paper-trading mode does not explicitly model fees in the signal, but the methodology documentation notes that the result is after execution considerations.
- **Funding:** Funding accrual is modeled and tracked.
- **Slippage:** Not explicitly modeled in paper trading.
- **Capacity:** Not assessed; paper trading only.
- **Leverage:** Not specified (paper trading).
- **Latency:** 60-second scanning cadence; suitable for hourly-scale signals.

## Evidence

### Source-reported

All figures trace directly to Paris0t/midas-funding-bot (README, 2026):

- **Total closed trades:** 766 over ~8 months of continuous paper trading.
- **Profit factor (raw):** ≈ 0.86.
- **Profit factor (funding-accrual-corrected):** ≈ 0.92.
- **Bootstrap 95% CI for profit factor:** [0.80, 1.56] — straddles 1.0, meaning the edge is statistically indistinguishable from zero.
- **Per-segment analysis:** One segment (50–75% APY, long side) looked strong in-sample (PF > 3). Deployed as a pre-registered live variant with falsifier (PF < 1.3 at n=30). **Failed** out-of-sample: n=45, PF 1.08.
- **Post-settlement reversion:** Two pre-registered hypotheses tested. **Both failed** at verdict day.
- **Cross-venue funding divergence:** Tested across Hyperliquid / OKX / dYdX. Pre-registered bar (t > 2 in ≥5/10 assets and the pool). **Failed** — 1/10 assets cleared it.
- **Machine learning (XGBoost):** AUC 0.557 — barely above coin flip. Reported honestly as "pipeline proven, not deployable."
- **Multi-instance A/B testing:** Parallel instances with frozen baseline, loose-gate labeling factory, and segment-gated variant. All results separable by instance_id.

Source reports this as a negative result. The research discipline (pre-registration, falsifiers, bootstrap inference, honest reporting) is the primary deliverable, not the strategy itself.

### Independently reproduced

Not independently reproduced. This is a single-author paper-trading study on Hyperliquid.

### Negative evidence

This entire record IS negative evidence. The core finding: **funding-rate contrarian fading does not produce a statistically detectable edge at retail size on Hyperliquid after execution considerations.**

Additional negative findings:
- Per-segment overfitting: in-sample strength (PF > 3) did not survive out-of-sample deployment (PF 1.08).
- Post-settlement microstructure reversion: both pre-registered hypotheses failed.
- Cross-venue funding divergence: signal did not generalize across venues.
- ML augmentation: XGBoost AUC 0.557 — no predictive power beyond noise.

## Falsification plan

The source itself implements a rigorous falsification framework:

1. **Pre-registered success bars:** Each hypothesis locked a success criterion (e.g., PF < 1.3 at n=30) before data examination.
2. **Bootstrap inference:** Day-blocked bootstrap of the equity curve produces a confidence interval for profit factor. The CI [0.80, 1.56] straddling 1.0 is the primary falsification result.
3. **Anti-anchoring:** Failed hypotheses were not re-sliced; new hypotheses required new forward data.
4. **No-edge gate:** Once the aggregate CI spanned 1.0, further parameter tuning was forbidden to prevent tuning into a false positive.
5. **Multi-instance A/B testing:** Parallel instances with frozen baselines prevent contamination.

For our own falsification of this negative result:
1. **Out-of-sample extension:** If someone replicates on fresh Hyperliquid data (post-August 2026) and finds a statistically significant edge, this null result is weakened.
2. **Venue generalization:** If the edge appears on a different venue (e.g., Drift on Solana) with different participant mix, the finding may be venue-specific.
3. **Regime dependency:** If the edge appears only in specific volatility or funding regimes, the blanket null may be too strong.
4. **Failure threshold:** If a replication finds PF > 1.2 with bootstrap CI excluding 1.0 at n > 500, the null is overturned.
5. **Action on failure:** If the null is overturned, the original entry gate suite and exit ladder should be re-examined for what changed.

## Crypto portability

**direct**

The strategy is native to crypto perpetual futures on Hyperliquid. Funding-rate mechanics are standard across all crypto perpetual venues (Binance, OKX, Bybit, Drift, etc.). The finding — that contrarian funding fading does not survive retail execution costs — may generalize to other venues, but this is untested.

**Crypto-specific risks:**
- Short squeezes on low-liquidity perps can cause outsized losses on the short leg.
- Funding rate spikes can be driven by genuine information (not just crowding), making the contrarian bet fundamentally wrong.
- Hyperliquid's specific fee structure, liquidity profile, and participant mix may differ from CEX venues.
- 24/7 trading means funding-settlement events occur continuously.
- Paper-trading fill assumptions may not match live execution.

## Limitations

- **Paper trading only:** No real capital was at risk. Fill assumptions may be optimistic.
- **Single author, no peer review:** The methodology is rigorous but the study has not been independently verified.
- **Single commit repository:** No version history; impossible to verify that results were not retroactively modified.
- **Undisclosed parameters:** Exact entry thresholds, gating parameters, and Kelly sizing formula are not public.
- **Hyperliquid-specific:** Results may not generalize to CEX venues with different participant mixes and fee structures.
- **Sample size:** 766 trades over 8 months is moderate; the bootstrap CI is wide enough to encompass both small positive and small negative edges.
- **Survivorship in universe:** The ~230-perp universe may include newly listed or low-liquidity contracts that affect fill quality.
- **Not independently reproduced:** No second party has replicated this study.
- **ML pipeline underpowered:** XGBoost with AUC 0.557 suggests the feature set lacks predictive power, but does not rule out that a different model or feature set might perform better.

## Implementation status

Not implemented in our research stack. The source is a paper-trading prototype on Hyperliquid. No backtesting infrastructure, no live execution, no validation in our own system.

## Adoption boundary

This record represents research material only. Its presence in this repository does not mean:
- The funding-rate contrarian fade has been disproven (the null result is venue- and period-specific).
- The negative finding applies to all funding-rate strategies (cross-sectional funding factors may still work, per Bryan Vine Paper 2).
- The methodology is approved for use in our own research.
- The result has been independently verified.

The primary value of this record is **methodological**: it demonstrates how to run a pre-registered, falsifiable, bootstrap-validated search for edge and honestly report a negative result. This methodology is directly applicable to our own future strategy research.

## Related Wiki records

- [[crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11]] — Bryan Vine Paper 2: cross-sectional funding factor is real but modest (~0.4 OOS Sharpe). Different mechanism (relative-value vs. contrarian fade) but related question (is funding-rate alpha harvestable?).
- [[btc-perp-single-venue-funding-carry-taker-fee-falsification-2026-09-14]] — santzmr: single-venue funding carry is cost-bound (taker fees kill it). Related finding but different source and mechanism (level harvest vs. contrarian fade).
- [[crypto-cross-sectional-stat-arb-funding-binding-cost-negative-2026-09-09]] — Cross-sectional stat arb on crypto perpetuals fails. Related negative evidence but different methodology and signal set.

## Sources

1. Paris0t (Nathan P.). "MIDAS: A funding-rate collection bot for Hyperliquid perpetuals — and an 8-month, pre-registered search for edge that honestly concluded there wasn't one." GitHub repository, MIT license, created 2026-01-24. https://github.com/Paris0t/midas-funding-bot
