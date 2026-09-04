---
schema: strategy-research-record-v1
title: "Retail Signal Three-Gate Falsification: Oscillator, Volume, Calendar, Candlestick, and Trend Families"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - negative-result
  - falsification
  - technical-analysis
  - retail-trading
status: research-only
confidence: high
source_as_of: 2026-07-22
sources:
  - "arXiv:2607.20093v1 [q-fin.ST], July 22 2026. https://arxiv.org/abs/2607.20093"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Retail Signal Three-Gate Falsification: Oscillator, Volume, Calendar, Candlestick, and Trend Families

## Provenance

- **Author:** Adam Darmanin (Hecatus Research, Malta)
- **Paper:** "Retail Trader's Ruin: An Anatomy of Popular Signal Failure"
- **arXiv:** 2607.20093v1 [q-fin.ST]
- **Published:** July 22, 2026
- **URL:** https://arxiv.org/abs/2607.20093
- **PDF:** https://arxiv.org/pdf/2607.20093v1
- **Code/Reproducibility:** Replication code accompanying the paper; source code to be made available at a permanent public archival location upon publication. Licensed market data are not redistributed.
- **Data period:** Full available sample for each family (earliest: 2000 for momentum; earliest: 2007 for volume; latest: 2025/2026)
- **Data source:** Licensed market data (NASDAQ-100, Russell 3000 point-in-time, SPY, S&P 500 point-in-time, EU country ETFs, STOXX 600, commodity/bond/crypto ETFs)

## Economic mechanism

### Source-reported

The paper tests whether five widely promoted retail technical signal families (trend, oscillator, candlestick, volume, calendar) deliver a positive, economically meaningful, net-of-cost, and survivable edge. Practical viability is defined as the conjunction of three predeclared gates: (a) statistical edge after multiplicity correction, (b) economic viability after trading costs, and (c) finite-bankroll survival under leverage. The author's hypothesis (H1) is that at least one of the five families is SUPPORTED on all three gates.

### Research interpretation

This is a falsification study, not an alpha-proposal study. The paper establishes a rigorous benchmark for what constitutes a viable retail signal and then tests the most promoted member of each family. The key mechanism being tested is whether commonly marketed technical analysis signals provide exploitable edge after accounting for:

1. **Multiple testing** — hierarchical Benjamini-Yekutieli FDR control across families and rule variants
2. **Transaction costs** — 10bps round-trip retail cost (5bps/leg) with 5–20bps sensitivity
3. **Leverage/ruin** — Monte Carlo simulation under FINRA and ESMA margin regimes

The paper's contribution is the composition of these three gates and the claim-exclusion framework: a family is REFUTED only when the confidence interval genuinely excludes the declared materiality threshold, not when a point estimate is merely non-significant.

## Signal

The paper does not propose a new trading signal. It evaluates five existing signal families:

### 1. Trend (Golden/Death Cross)
- **Universe:** NASDAQ-100
- **Rule:** 50-day/200-day SMA crossover
- **Parameters:** Golden cross = buy, death cross = sell
- **Horizon:** Full available sample (NASDAQ-100 constituent period)

### 2. Oscillator (RSI)
- **Universe:** NASDAQ-100
- **Rule:** RSI(14, 30/70) — buy when RSI < 30, sell when RSI > 70
- **Parameters:** 14-period RSI, 30/70 thresholds

### 3. Volume (On-Balance Volume)
- **Universe:** Russell 3000 point-in-time, 5,313 stocks / 228 months (2007–2025)
- **Rule:** OBV(3,12) — on-balance volume with 3-period and 12-period smoothing
- **Cross-sectional:** Monthly rebalance

### 4. Calendar (Sell-in-May)
- **Universe:** SPY
- **Rule:** Sell-in-May (best of Bonferroni + Benjamini-Yekutieli battery)
- **Horizon:** Full available sample (8,358 days)

### 5. Candlestick (7-Pattern Battery)
- **Universe:** Russell 3000 point-in-time, 4,152 stocks
- **Rule:** 7-pattern event study (Bonferroni + BY correction)
- **Horizon:** Full available sample

### Momentum Calibration Benchmark
- **Universe:** S&P 500 point-in-time, 1,130 stocks / 312 months (2000–2026)
- **Rule:** Jegadeesh–Titman 12-1 momentum, top decile, dollar-volume-weighted
- **Purpose:** Active comparator (clinical-trial-style) to test the pipeline's discriminating power

## Required data

- **Instruments:** NASDAQ-100 constituents, Russell 3000 point-in-time, SPY, S&P 500 point-in-time, EU country ETFs (Germany/France/UK/Spain/Italy/Switzerland), STOXX 600 constituents, commodity/bond/crypto ETFs
- **Fields:** OHLCV (daily for index-level; monthly for cross-sectional), point-in-time index membership, delisting returns
- **Timeframe:** Daily for trend/oscillator/calendar; monthly for volume/momentum
- **Survivorship:** Point-in-time membership with Shumway (2001) delisting correction (−30%/year delisting-month return)
- **Data vendor:** Licensed market data (not publicly available for redistribution)

## Execution assumptions

- **Signal-to-order timing:** Assumed same-bar execution for index-level; next-month for cross-sectional
- **Cost model:** 10bps round-trip retail cost (5bps/leg), with 5–20bps sensitivity grid
- **Order type:** Assumed market orders at next available opportunity
- **Fill model:** Assumed full fill at mid-price minus half-spread (Roll 1984 spread-based cost proxy)
- **Leverage scenarios:**
  - EQ-US-FINRA (headline): 25% maintenance margin, 2:1 initial cap (FINRA Rule 4210)
  - EQ-EU-CFD: 20% initial margin, 5:1 cap, 10% maintenance (ESMA 2018)
  - THIN-CFD-STRESS: 2% maintenance margin (stress case)
- **Capacity:** Not explicitly bounded; families tested on large-cap US equity universes
- **Latency:** Not explicitly modeled

## Evidence

### Source-reported

All results below are directly reported by Darmanin (arXiv:2607.20093v1, July 2026):

**Gate (a) — Statistical edge (Sharpe gap vs. exposure-matched benchmark, δS = 0.20):**

| Family | Sharpe gap, 95% CI | Verdict |
|--------|-------------------|---------|
| Trend (golden/death cross) | [−0.234, 0.265] | INCONCLUSIVE (CI straddles δS) |
| Oscillator (RSI) | [−0.608, −0.175] | REFUTED (significantly negative) |
| Volume (OBV) | [−0.193, 0.175] | REFUTED (material exclusion: US < δS) |
| Calendar (Sell-in-May) | [−0.618, 0.000] | REFUTED (material exclusion: US < δS) |
| Candlestick (7-pattern) | max \|d\| = 0.026 vs. δd = 0.2 | REFUTED (tightly estimated below δd) |
| Momentum (calibration) | [−0.295, 0.548] | INCONCLUSIVE (CI straddles δS) |

**Gate (b) — Economic viability (CAGR gap, δR = 0.01):**

| Family | CAGR gap, 95% CI | Verdict |
|--------|------------------|---------|
| Trend | [−0.081, 0.024] | INCONCLUSIVE |
| Oscillator | [−0.149, −0.044] | REFUTED (significantly negative) |
| Volume | [−0.086, 0.013] | INCONCLUSIVE |
| Calendar | [−0.131, −0.026] | REFUTED (significantly negative) |
| Candlestick | 1/7 sign-preserving at 5bps | REFUTED |
| Momentum | [−0.044, 0.130] | INCONCLUSIVE |

**Gate (c) — Survival (quarterly forced-liquidation probability, EQ-US-FINRA, 2× leverage):**

| Family | P(liquidation), 95% CI | Verdict |
|--------|------------------------|---------|
| Trend | 0.009 [0.0065, 0.0124] | survives |
| Oscillator | 0.013 [0.0097, 0.0167] | survives |
| Volume | 0.000 [0.000, 0.001] | survives |
| Calendar | 0.003 [0.0019, 0.0056] | survives |
| Momentum | 0.004 [0.0023, 0.0062] | survives |

**Joint verdict:** 4 REFUTED (oscillator, volume, calendar, candlestick), 2 INCONCLUSIVE (trend, momentum), 0 SUPPORTED. H1 rejected.

**Sensitivity to δS:** Across δS ∈ {0.10, 0.20, 0.30}, the REFUTED count ranges from 3 to 5. No family ever flips between REFUTED and SUPPORTED — only REFUTED↔INCONCLUSIVE.

**EU replication:** 18-cell grid (6 EU country ETFs × 3 indicators) finds 4/18 cells with bootstrap CI excluding zero (all negative), zero BY rejections. Individual-EU-stock arm (567 STOXX 600 constituents, 2005–2026): zero BY-significant.

**Crypto ETF tests:** A 62-cell grid (11 sectors × OBV; 17 instruments × 3 indicators, spanning equities, bonds, commodities, and crypto ETFs) finds zero BY-significant cells out of 62. The single strongest raw cell (RSI on HYG, p = 0.004) does not survive BY adjustment (padj = 0.248).

**Momentum benchmark crash diagnostics:** Max drawdown 46.4% (unlevered), 76% at 2×, 93% at 3×. Worst 12-month return −35.4%. Gate (c) detects real tail risk.

**Gate (a) power analysis:** Observed CI implies SE ≈ 0.215 Sharpe-gap units, minimum detectable effect ≈ 0.60 at 80% power — larger than most published diversified-momentum Sharpe gaps. Gate (a) is underpowered at n = 312 months for typical momentum effect sizes.

### Independently reproduced

Not independently reproduced. The EU replication arm within the same paper provides cross-market corroboration but is not an independent reproduction by a different research group.

### Negative evidence

- **Oscillator (RSI):** Sharpe gap significantly negative; CAGR gap significantly negative. RSI timing significantly underperforms its own exposure-matched benchmark.
- **Calendar (Sell-in-May):** CAGR gap significantly negative — the opposite of the folklore claim.
- **Volume (OBV):** Statistical gate CI upper bound sits below δS = 0.20 (material exclusion).
- **Candlestick:** Raw significance on 7/7 patterns but effect size (max Cohen's d = 0.026) is ≪ materiality floor δd = 0.2. Only 1/7 patterns sign-preserving after 5bps cost.
- **Trend (golden/death cross):** Underpowered on this sample — CI straddles all thresholds in the sensitivity grid. Not refuted but not supported.
- **Momentum benchmark:** Underpowered at n = 312 months. INCONCLUSIVE (never REFUTED), which validates the pipeline's discriminating power.
- **Crypto ETFs:** Zero significant signals across all tested instruments and indicators after multiplicity correction.
- **EU markets:** Zero BY-significant cells across 18-cell grid and individual-stock arm.

## Falsification plan

This paper IS the falsification study. The three-gate framework is itself a falsification protocol:

1. **Statistical gate:** Stationary-bootstrap 95% CI on Sharpe gap vs. δS = 0.20. REFUTED if upper CI bound < δS.
2. **Economic gate:** Stationary-bootstrap 95% CI on CAGR gap (net of 10bps) vs. δR = 0.01. REFUTED if upper CI bound < δR.
3. **Survival gate:** Monte Carlo leverage/margin simulation (4,000 bootstrap paths). FAILS if liquidation probability upper CI > 10%.

**Research-defined falsification thresholds:** δS = 0.20 (sensitivity {0.10, 0.20, 0.30}), δR = 0.01 (sensitivity {0.005, 0.01, 0.02}), survival threshold 10% quarterly forced-liquidation probability.

**For applying this framework to crypto:**
- Port the three-gate composition to crypto-perpetual or crypto-spot universes
- Use observed crypto spread/fee/funding as the cost model (not retail equity 10bps)
- Use crypto-appropriate leverage scenarios (e.g., Binance 1–125× perpetual leverage)
- Test whether the same signal families fail or survive in crypto microstructure

## Crypto portability

**Adapted**

The paper explicitly tests crypto ETFs within a 62-cell grid and finds zero significant signals after multiplicity correction. This is direct evidence that the tested retail signal families do not provide exploitable edge on crypto ETFs.

However, the crypto ETF tests are limited:
- Tested instruments are crypto ETFs (e.g., BITO, ETHE), not native crypto perpetual/spot markets
- Cost model is equity-oriented (10bps round-trip), not calibrated to crypto-specific fees/funding
- Leverage scenarios are equity margin regimes, not crypto perpetual leverage
- Signal families are equity-optimized (e.g., 50/200 SMA for trend); crypto may require different parameters

**Crypto-specific portability risks:**
- Crypto markets have different microstructure (24/7, higher volatility, funding rates on perpetuals)
- Retail signal families may perform differently under crypto's higher noise and fat tails
- The three-gate framework itself is portable and could be applied to crypto-native signals
- The multiplicity-correction methodology is directly applicable to crypto factor/signal mining

**Key implication for our research:** This paper provides a rigorous baseline for what DOES NOT work. Any proposed crypto alpha strategy should demonstrate edge beyond what this falsification framework would reject.

## Limitations

- **No pristine holdout:** Data and rule definitions examined in prior work; all intervals are stationary bootstrap of full sample, not out-of-sample tests
- **Universe heterogeneity:** Families evaluated on different universes by necessity (index-level vs. cross-sectional)
- **No margin/borrow-rate data:** Cost model uses parametric fixed-bps convention, not observed bid-ask/liquidity
- **Momentum benchmark underpowered:** Gate (a) cannot resolve typical momentum effect sizes at n = 312 months
- **Candlestick excluded from survival gate:** Event-study design, no continuous return series
- **No external peer review:** Results reported as computed from replication code
- **Licensed data:** Market data not publicly available for independent replication
- **Crypto ETF coverage limited:** Only ETF wrappers tested, not native crypto perpetual/spot markets
- **Not independently reproduced**

## Implementation status

not-implemented. No implementation in our research stack. The paper provides the falsification framework and replication code, but we have not applied it to our own crypto strategy universe.

## Adoption boundary

This record is research material only. A record being present in this repository does not mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

The paper's primary value is as a **falsification baseline**: it establishes what does NOT work and provides a rigorous methodology for testing whether proposed signals clear a meaningful bar. Any crypto alpha strategy we develop should be tested against this framework.

## Related Wiki records

- `[[quant/btc-perpetual-factor-mining-point-in-time-audit-negative-2026-09-04]]` — Independent negative-result study on crypto perpetual factor mining; complementary falsification evidence from a different methodology
- `[[quant/crypto-retail-systematic-trading-null-result-adversarial-audit-2026-09-01]]` — Null-result record on retail systematic trading in crypto; thematically adjacent but different methodology

## Sources

1. Adam Darmanin, "Retail Trader's Ruin: An Anatomy of Popular Signal Failure," arXiv:2607.20093v1 [q-fin.ST], July 22, 2026. https://arxiv.org/abs/2607.20093
