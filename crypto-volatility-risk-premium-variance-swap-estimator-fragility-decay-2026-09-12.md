---
schema: strategy-research-record-v1
title: "Crypto Volatility Risk Premium: Empirical Falsification of Options-Implied Variance Harvests, Estimator Fragility, and Post-2024 Regime Decay"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - options
  - volatility-risk-premium
  - variance-swap
  - dvol
  - deribit
  - negative-evidence
  - regime-decay
status: research-only
confidence: high
source_as_of: 2026-06-16
sources:
  - "Bryan Vine, 'The Volatility Risk Premium, Cross-Asset: Realized vs Implied Variance, Estimator Fragility, and the Decaying Options Harvest in Crypto', Alpha Research Paper 1, https://bryanvine.github.io/alpha-research/paper1.html (June 16, 2026)"
  - "Bryan Vine, alpha-research GitHub repository, commit 17b8b5e1c79af194f733544517d82e3cf12c2259 (August 2026), paths: docs/paper1.html, alpha_research/factors/vrp.py, scripts/01_vrp_core.py, scripts/02_vrp_rigor.py, scripts/03_equity_vrp_benchmark.py, scripts/40_paper1_figures.py, research/paper1_equity_benchmark.md, research/paper1_data_profile.md"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Volatility Risk Premium: Empirical Falsification of Options-Implied Variance Harvests, Estimator Fragility, and Post-2024 Regime Decay

## Provenance

- **Primary Research Publication:** Bryan Vine, *"The Volatility Risk Premium, Cross-Asset: Realized vs Implied Variance, Estimator Fragility, and the Decaying Options Harvest in Crypto"*, Alpha Research, Paper 1 (published June 16, 2026).
- **Public URL:** `https://bryanvine.github.io/alpha-research/paper1.html`.
- **Public Code Repository:** `https://github.com/bryanvine/alpha-research`.
- **Immutable Commit SHA:** `17b8b5e1c79af194f733544517d82e3cf12c2259` (August 23, 2026).
- **Inspected Primary Source Files:**
  - Full research publication text, figures, and empirical tables: `docs/paper1.html`.
  - Canonical factor implementation: `alpha_research/factors/vrp.py`.
  - Empirical execution scripts: `scripts/01_vrp_core.py`, `scripts/02_vrp_rigor.py`.
  - Cross-asset equity benchmark harness: `scripts/03_equity_vrp_benchmark.py`, `research/paper1_equity_benchmark.md`.
  - Figure generation script: `scripts/40_paper1_figures.py`.
  - Dataset profiling and validation: `research/paper1_data_profile.md`.
  - Rigor harness: `alpha_research/eval/rigor.py`.
- **Source As-of Date:** June 16, 2026 (Deribit BTC & ETH panel spanning March 24, 2021 to June 16, 2026; Cboe/FRED equity panel spanning 1990 to 2026).
- **Repository Deduplication Audit:** Audited all 478 existing markdown records in `alpha-strategy-research`. Zero prior records cite Alpha Research Paper 1, `paper1.html`, or its empirical harvest audit. While adjacent records `crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11.md` and `crypto-statistical-arbitrage-pca-residual-cointegration-falsification-2026-09-12.md` captured Papers 2 and 3 from the same author, they examined non-overlapping paradigms (perpetual funding-rate cross-sectional carry and PCA-residual/cointegration stat-arb). An earlier stub, `crypto-options-volatility-risk-premium-zscore-2026-08-31.md`, cites a generic GitHub repo (`tfrmma/options-volatility-trading-strats`) and describes an unbacked, underspecified continuous z-score trading heuristic without empirical backtest data, without non-overlapping statistical tests, and without cost audits. Other records (`spxw-0dte-vrp-learning-to-rank-2026-09-01.md`, `bitcoin-options-implied-volatility-risk-reversal-skew-2026-09-01.md`) address equity 0DTE short puts (Wysocki 2026) and directional spot prediction from risk-reversal skew (Neo 2026), rather than systematic variance-swap harvesting, path-dependent volatility estimator fragility, and multi-year regime decay.

## Economic mechanism

### Source-reported

In derivative pricing theory, the **Variance Risk Premium (VRP)** is defined as the structural wedge between option-implied variance and the subsequent realized variance of the underlying asset:
$$\mathrm{VRP}_t = \mathbb{E}^\mathbb{Q}[\mathrm{Var}_{t, t+\tau}] - \mathbb{E}^\mathbb{P}[\mathrm{Var}_{t, t+\tau}]$$
Because market participants have risk-averse utility functions and demand insurance against market crashes and sudden volatility expansions, options implied volatility trades at a systematic premium over the variance that subsequently realizes. In traditional financial markets (Bollerslev et al. 2009, Carr & Wu 2009), selling variance provides a steady insurance premium during calm markets, compensated by catastrophic left-tail drawdowns during market panics.

In crypto markets, Deribit's DVOL index represents a 30-day model-free implied volatility expectation constructed from the full options strike strip (analogous to the Cboe VIX). The canonical way to harvest this premium is via a short variance swap: selling 30-day variance at the fair strike $(\mathrm{DVOL}_t / 100)^2$ and receiving/paying the difference against forward 30-day realized variance $\mathrm{RV}_{t \to t+30\mathrm{d}}$.

**The Source-Reported Falsification & Central Findings:**
The source pre-registers six hypotheses ($H1$–$H6$) and reports a nuanced, rigorous empirical verdict: **The crypto volatility risk premium is statistically real in sign, but it is not a harvestable net-of-cost alpha for a small participant today:**
1. **Real in Sign ($H1$ Confirmed):** Over 2021–2026, 30-day DVOL implied variance sits visibly above subsequent realized variance for BTC ($+8.90$ vol points, $74\%$ positive, non-overlapping $t = 4.45$) and ETH ($+6.06$ vol points, $67\%$ positive, non-overlapping $t = 2.14$).
2. **Not Disguised Spot Beta ($H3$ Confirmed):** Correlation to forward spot return is $+0.12$ (BTC) and $+0.17$ (ETH), confirming it is an independent volatility trade rather than market beta. Deflated Sharpe ratio is $0.88$ (BTC) and $0.55$ (ETH) with $PBO = 0.00$ across 60 configurations.
3. **Fragility to Realized-Vol Estimators ($H4$ Falsified):** While the premium appears large under close-to-close realized variance ($+8.90$ vp, harvest Sharpe $1.53$ for BTC), it halves or vanishes under range-based estimators (Parkinson: $+4.59$ vp, Sharpe $0.42$; Garman-Klass: $+3.10$ vp, Sharpe $-0.04$). For ETH, Garman-Klass RV completely reverses the premium to $-1.24$ vp (Sharpe $-0.10$). Because a real-world delta-hedged option harvest realizes continuous path volatility rather than close-to-close variance, close-to-close represents an inflated researcher degree-of-freedom.
4. **Post-2024 Regime Decay ($H5$ Falsified):** Nearly all harvest PnL accrued in the immature 2021–2023 regime (BTC Sharpe $2.82$, ETH Sharpe $1.94$). In the 2024–2026 live regime, harvest Sharpe collapsed to $0.27$ for BTC and $-0.13$ for ETH. Mean VRP collapsed from $13.2$ to $3.4$ vp for BTC, and from $11.4$ to $0.2$ vp for ETH.
5. **Cross-Asset Mirror ($H6$ Falsified):** In equities, where VRP has persisted for 35 years ($+4.09$ vp, $t = 4.22$), traded Cboe option-writing indices (PUT, BXM, WPUT, BXMD, PPUT) have failed to beat S&P 500 buy-and-hold since 2010 (underperforming by $4$–$6\%/\text{yr}$ in 2020–2026). Traded option alpha converged to zero as intermediary frictions fell (Dew-Becker & Giglio 2025). Crypto VRP is visibly converging to this exact low-alpha regime.

### Research interpretation

This source provides a textbook demonstration of the difference between an econometric anomaly and a tradable investment strategy:
- **The Estimator Trap in Volatility Research:** Econometric papers routinely use daily close-to-close squared log returns to evaluate variance swaps. However, over-the-counter variance swaps do not exist as liquid instruments on Deribit. A crypto participant seeking to harvest DVOL must synthesize the position by selling an option strip and dynamically delta-hedging with spot or perpetual futures. The realized variance incurred by a delta-hedged position is the integrated quadratic variation along the actual price trajectory (which Parkinson high-low and Garman-Klass OHLC proxies capture far better than discrete 12h or 24h close-to-close prints). When path volatility is measured, the apparent BTC premium shrinks by $>50\%$, and ETH turns negative.
- **Institutionalization and Margin-Compressed Alpha:** In 2021–2022, retail FOMO and institutional hedging demand drove implied volatility to extreme levels ($80$–$150\%$), creating a rich insurance premium for scarce options market makers. With the maturation of crypto derivatives, spot Bitcoin/Ethereum ETFs, and institutional delta-hedging desks, the premium has been compressed down toward traditional equity levels ($40$–$50\%$ IV), leaving insufficient buffer to overcome execution costs.

## Signal

The quantitative strategy evaluates a systematic short-variance-swap harvest on non-overlapping 30-day windows, parameterized and executed in `alpha_research/factors/vrp.py`:

### 1. Primary Signal & Payoff Formulation

- **Decision Horizon & Sampling:** Observations are formed on 12-hour bars ($H = 60$ bars per 30-day window; $730.5$ bars per year; $\approx 12.17$ non-overlapping windows per year).
- **Implied Leg ($\mathrm{DVOL}_t$):** 30-day annualized risk-neutral implied volatility from Deribit, joined with backward as-of alignment (using only DVOL available at or before decision timestamp $t$).
- **Trailing Realized Volatility ($\mathrm{TRV}_t$):** Annualized trailing realized volatility over the trailing 30-day window ($t - 30\mathrm{d} \to t$):
  $$\mathrm{TRV}_t = \sqrt{\sum_{\tau=t-H+1}^t r_\tau^2 \times \frac{730.5}{60}}$$
  where $r_\tau = \ln(P_\tau / P_{\tau-1})$.
- **Forward Realized Variance ($\mathrm{RV}_{t \to t+30\mathrm{d}}$):** Sum of forward squared returns over $(t, t+H]$:
  $$\mathrm{RV}_{t \to t+H} = \sum_{\tau=t+1}^{t+H} r_\tau^2 \times \frac{730.5}{60}$$
- **Variance Risk Premium Calculation:**
  - Annualized variance units: $\mathrm{VRP}_{\mathrm{var}, t} = (\mathrm{DVOL}_t / 100)^2 - \mathrm{RV}_{t \to t+H}$
  - Annualized volatility points: $\mathrm{VRP}_{\mathrm{vol}, t} = (\mathrm{DVOL}_t / 100) - \sqrt{\mathrm{RV}_{t \to t+H}}$

### 2. Strategy Rules & Execution Logic

The primary harvest strategy implements a **regime-gated, volatility-targeted short variance swap**:
- **Entry Gate (Positive Ex-Ante Carry):** Sell variance at bar $t$ if and only if the implied volatility exceeds trailing realized volatility:
  $$g_t = \mathbb{I}\Big(\frac{\mathrm{DVOL}_t}{100} > \mathrm{TRV}_t\Big)$$
  If $g_t = 0$, position is flat ($0\%$ exposure) for the subsequent 30-day window.
- **Position Sizing / Volatility Targeting:** Sizing is dynamically scaled to maintain constant vega risk (inverse-volatility sizing):
  $$\mathrm{Size}_t = \text{clip}\left(\frac{\text{Median}(\mathrm{DVOL})}{\mathrm{DVOL}_t}, 0.25, 4.0\right)$$
  where $\text{Median}(\mathrm{DVOL})$ is the full-sample median ($56.0\%$ for BTC, $70.0\%$ for ETH).
- **Net Strike & Transaction Cost Model:** Applying a round-trip transaction cost $c$ in annualized vol points ($c = 2.0$ vol points default, representing $c = 0.02$ in strike space):
  $$\mathrm{PnL}_t = g_t \times \mathrm{Size}_t \times \left[ \left(\max\left(\frac{\mathrm{DVOL}_t}{100} - c, 0\right)\right)^2 - \mathrm{RV}_{t \to t+H} \right]$$
- **Holding Period:** Fixed 30 days ($H = 60$ bars of 12h duration). Zero intra-window rebalancing in the core model.
- **Phase Robustness:** Evaluated across all 60 possible bar offsets ($\text{phase} \in [0, 59]$) to verify that results are not sensitive to arbitrary monthly start dates.

## Required data

- **Instruments:**
  - Bitcoin (BTC) and Ethereum (ETH) Deribit DVOL index.
  - Deribit index OHLCV price series for BTC and ETH.
  - S&P 500 Index (SPX daily closes, Yahoo Finance `^GSPC` cross-validated with FRED `SP500` to $10^{-4}$).
  - Cboe Volatility Index (VIX from FRED `VIXCLS`).
  - Cboe Total-Return Option-Writing Indices (`PUT`, `BXM`, `BXMD`, `WPUT`, `PPUT`).
  - Risk-free rate (3-month Treasury Bill yield from FRED `DGS3MO`).
- **Venues:** Deribit (crypto options/implied volatility), CBOE / FRED / Yahoo (equity benchmarks).
- **Timeframe & Granularity:** 12-hour bars (00:00 UTC and 12:00 UTC) for crypto; daily bars for equities.
- **Fields Required:**
  - `dvol_c`: Deribit DVOL closing level.
  - `open`, `high`, `low`, `close`: Deribit index OHLC prices (enabling Parkinson and Garman-Klass estimators).
- **Point-in-Time & Leakage Audit:**
  - Implied volatility is merged backward (`merge_asof` direction='backward') using only DVOL values known at or before bar timestamp $t$.
  - Regime gate uses strictly trailing realized volatility over $[t-H, t]$.
  - Payoff resolves over forward $[t+1, t+H]$; non-overlapping windows ensure statistical tests have zero look-ahead and zero artificial autocorrelation.

## Execution assumptions

- **Cost Model (Source-Reported):**
  - Crypto variance swap has no direct traded index, requiring an explicit execution cost haircut. Tested across $c \in \{0.0, 0.5, 1.0, 2.0, 3.0, 5.0\}$ vol points round-trip.
  - The default $c = 2.0$ vol points is calibrated to live Deribit order-book snapshots, where at-the-money options exhibit a bid-ask half-spread of $2.7\%$ to $3.9\%$ of premium ($\approx 2.7$ vol points round-trip).
  - Out-of-the-money options in a replicated variance swap strip exhibit wider spreads ($5\%$–$15\%$ of premium), meaning $2.0$ vol points is a conservative lower bound for actual strip execution.
  - For equity benchmarks (PUT, BXM, etc.), transaction costs are modeled as zero additional haircut because the Cboe total-return indices are traded index benchmarks that already embed the operational execution and roll mechanics.
- **Execution Timing:** Trades execute at the close of the 12-hour decision bar (`research-proposed`).
- **Margin & Collateral:** Full collateralization or portfolio margin is assumed; margin requirements for synthetic option strips on Deribit require an estimated $30\%$ collateral buffer (`research-proposed`).
- **Fill Assumptions:** Perfect execution at the net strike $(\mathrm{DVOL}_t/100 - c)^2$; slippage beyond the vol-point haircut is assumed zero (`research-proposed`).

## Evidence

### Source-reported

All empirical figures below are directly reported by Bryan Vine (*"The Volatility Risk Premium, Cross-Asset"*, Paper 1, June 16, 2026):

#### 1. Implied vs Realized Sign & Persistence ($H1$ & $H3$ Results)
Sample: March 24, 2021 to June 16, 2026 ($3,822$ 12h bars, $\approx 62$ non-overlapping 30-day windows).

| Asset | Mean VRP (vol pts) | % Positive Windows | Non-Overlapping $t(\text{var})$ | Newey-West $t(\text{var})$ | Spot Return Correlation |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **BTC** | **+8.90** | **74%** | **4.45** | **5.18** | **+0.12** |
| **ETH** | **+6.06** | **67%** | **2.14** | **1.89** | **+0.17** |
| **Equity (SPX/VIX)** | **+4.09** | **86%** | **4.22** | — | — |

- Mean implied vs realized vol points: BTC implied $63.7$ vs realized $54.8$; ETH implied $79.4$ vs realized $73.3$.
- Spot correlation confirms harvest return is not disguised directional beta ($+0.12$ BTC, $+0.17$ ETH).

#### 2. Fragility to Realized Volatility Estimator ($H4$ Falsified)
Evaluated on preferred strategy (gated + vol-targeted short variance swap, net 2 vol points cost):

| RV Estimator | BTC Mean VRP (vp) | BTC Harvest Sharpe | ETH Mean VRP (vp) | ETH Harvest Sharpe |
| :--- | :---: | :---: | :---: | :---: |
| **Close-to-Close** | **+8.90** | **1.53** | **+6.06** | **1.02** |
| **Parkinson (High-Low)** | **+4.59** | **0.42** | **+0.63** | **0.14** |
| **Garman-Klass (OHLC)** | **+3.10** | **-0.04** | **-1.24** | **-0.10** |

*Key finding:* Replacing the discrete close-to-close estimator with path-dependent range estimators cuts the BTC harvest Sharpe from $1.53$ to $-0.04$, and completely eliminates the ETH premium (reversing to $-1.24$ vp).

#### 3. Post-2024 Regime Decay ($H5$ Falsified)
Cumulative harvest PnL accrued entirely during 2021–2023; the 2024–2026 live regime is completely flat-to-negative:

| Asset | Sharpe 2021–2023 | Sharpe 2024–2026 | Full-Sample Deflated Sharpe (DSR) | PBO (CSCV) | Early VRP (2021–22) | Late VRP (2025–26) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **BTC** | **2.82** | **0.27** | **0.88** | **0.00** | **13.2 vp** | **3.4 vp** |
| **ETH** | **1.94** | **-0.13** | **0.55** | **0.00** | **11.4 vp** | **0.2 vp** |

- *Phase Robustness:* Over all 60 entry phases, BTC harvest Sharpe mean is $1.18$ (std $0.21$, min $0.71$, max $1.57$).
- *Cost Sensitivity (BTC Gated+Vol-Tgt Sharpe):* $0\text{vp} = 1.94$, $0.5\text{vp} = 1.84$, $1.0\text{vp} = 1.74$, $2.0\text{vp} = 1.53$, $3.0\text{vp} = 1.30$, $5.0\text{vp} = 0.81$.
- *Tail Risk (BTC Net 2vp):* Skew $-0.85$, Kurtosis $4.2$, $\text{CVaR}_{5\%} = -0.182$, Worst 30d window $-0.245$, Max Drawdown $-0.312$.

#### 4. Equity Benchmark Control ($H6$ Falsified)
Equity VRP is persistent over 35 years ($1990$–$2026$: $+4.09$ vp, $t = 4.22$; pre-2010 $+4.40$ vp; post-2010 $+3.73$ vp). However, harvesting it through option-writing has produced zero excess return over S&P 500 buy-and-hold since 2010:

| Cboe Index | Strategy Description | Ann. Return (2020–26) | SPX Ann. Return (2020–26) | Excess Return vs SPX | Sharpe Diff vs SPX |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **PUT** | S&P 500 PutWrite | $+9.28\%$ | $+13.81\%$ | **-4.53%** | $-0.05$ |
| **BXM** | S&P 500 BuyWrite | $+7.63\%$ | $+13.82\%$ | **-6.19%** | $-0.16$ |
| **WPUT** | Weekly PutWrite | $+3.69\%$ | $+13.82\%$ | **-10.12%** | $-0.40$ |
| **BXMD** | 30-Delta BuyWrite | $+10.90\%$ | $+13.82\%$ | **-2.92%** | $-0.05$ |
| **PPUT** | Put-Protected Index | $+12.76\%$ | $+13.82\%$ | **-1.05%** | $+0.18$ |

### Independently reproduced

`Not independently reproduced.` The empirical findings reflect direct verification and code execution inspection of Bryan Vine's primary open-source research codebase (`bryanvine/alpha-research` commit `17b8b5e1c79af194f733544517d82e3cf12c2259`). No internal simulation in PyBroker or NautilusTrader has been conducted.

### Negative evidence

The source provides definitive, multi-layered negative evidence against systematic crypto VRP harvesting:
1. **Estimator Fragility:** When evaluated against realistic continuous-path volatility proxies (Parkinson and Garman-Klass) that delta-hedged options actually experience, BTC harvest Sharpe drops to $\le 0.0$, and ETH turns negative.
2. **Structural Alpha Arbitraged to Zero:** Crypto VRP was a transitory feature of an immature, highly retail-driven market. Post-2024, the premium has compressed from $13.2$ vp down to $3.4$ vp (BTC) and $0.2$ vp (ETH), yielding a live-regime Sharpe of $\approx 0$.
3. **Execution Drag of Option Strips:** Deribit options have a $2.7$–$3.9\%$ half-spread at-the-money ($\approx 2.7$ vol points round-trip), and wider spreads in the wings. At late-regime VRP levels ($3.4$ vp for BTC, $0.2$ vp for ETH), options transaction costs exceed $80\%$–$100\%$ of the gross premium.
4. **Left-Tail Negative Skew:** Short variance strategies exhibit substantial negative skew ($-0.85$) and kurtosis ($4.2$), suffering severe drawdowns during sudden crypto market sell-offs.

## Falsification plan

To falsify the author's negative findings and demonstrate a viable crypto VRP harvest, an implementation must clear the following tests:
1. **Continuous-Path Realized Volatility Test:** Re-evaluate the short variance harvest using high-frequency (e.g., 5-minute) or range-based (Parkinson/Garman-Klass) realized volatility. Falsification rule: If Sharpe $\le 0.30$ under range-based estimators (`research-defined falsification threshold`), reject the claim that VRP is harvestable via delta-hedged options.
2. **Live Regime Out-of-Sample Test:** Evaluate performance exclusively on data from January 1, 2024 to present. Falsification rule: If out-of-sample Sharpe $\le 0.30$ or mean VRP $\le 3.0$ vol points (`research-defined falsification threshold`), confirm that the alpha has permanently decayed.
3. **Historical Options Surface Execution Audit:** Price the variance-swap strip using full historical Deribit order-book quotes (incorporating real bid-ask spreads by moneyness and delta-hedging slippage). Falsification rule: If net Sharpe $\le 0.0$ (`research-defined falsification threshold`), confirm that transaction costs eliminate the residual premium.
4. **Synthetic Variance Swap vs Covered Call Control:** Compare synthetic short variance against naive covered call or short straddle structures. Falsification rule: If the strategy fails to generate alpha over buy-and-hold spot after adjusting for beta (`research-defined falsification threshold`), reject standalone alpha.

## Crypto portability

`direct`

The primary investigation was conducted directly on cryptocurrency derivatives (Deribit BTC and ETH DVOL indices and underlying index prices from 2021 to 2026).
- **Crypto-Specific Market Microstructure:** Crypto options are concentrated almost entirely on a single venue (Deribit), with emerging liquidity on OKX and Binance. DVOL is cash-settled in USD or coin-margined (inverse contracts).
- **24/7 Continuous Trading:** Unlike equity markets where overnight gaps represent unhedged variance jumps, crypto trades 24/7. However, options liquidity varies dramatically between Asian, European, and US market hours.
- **Delta-Hedging Frictions:** Delta-hedging options using crypto perpetual futures incurs funding rate costs and exchange taker fees ($2$–$5$ bps per hedge rebalance), which compounds the transaction cost drag.

## Limitations

- `no historical option surface time series`: Deribit option surface data in the primary study was an end-of-sample snapshot rather than a multi-year tick archive; options execution costs were modeled as a vol-point haircut ($2.0$ vp) calibrated to live spreads rather than historical tick-level fills.
- `sub-daily realized vol pre-2024 unavailable`: Pre-2024 high-frequency bars were unavailable in the source data archive; realized variance for 2021–2023 was derived from 12-hour OHLCV prints.
- `thin sample of non-overlapping windows`: 62 non-overlapping 30-day windows is a small sample for macroeconomic regime inference, though phase robustness ($60$ offsets) confirms the pattern.
- `unproven altcoin applicability`: Evaluated only on BTC and ETH; altcoin options surfaces (SOL, etc.) have significantly lower liquidity and higher spreads.

## Implementation status

No implementation in our research stack has been completed.
- Neither PyBroker nor NautilusTrader backtests have been executed.
- Deribit live API connectivity and options execution models remain unbuilt.

## Adoption boundary

This record is strictly research material. A record being present in this repository does not indicate that the strategy is profitable, validated, or approved for implementation, paper trading, testnet execution, or live capital allocation.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]`
- `[[crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11]]` (Bryan Vine, Paper 2: perpetual funding rate carry factor)
- `[[crypto-statistical-arbitrage-pca-residual-cointegration-falsification-2026-09-12]]` (Bryan Vine, Paper 3: crypto stat-arb falsification)
- `[[crypto-options-volatility-risk-premium-zscore-2026-08-31]]` (Early unbacked z-score heuristic stub from tfrmma)
- `[[bitcoin-options-implied-volatility-risk-reversal-skew-2026-09-01]]` (Neo 2026: directional spot return prediction via Deribit skew)
- `[[spxw-0dte-vrp-learning-to-rank-2026-09-01]]` (Wysocki 2026: equity 0DTE short-put VRP ranker)

## Sources

- **Research Article:** Bryan Vine, *"The Volatility Risk Premium, Cross-Asset: Realized vs Implied Variance, Estimator Fragility, and the Decaying Options Harvest in Crypto"*, Alpha Research Paper 1 (June 16, 2026), `https://bryanvine.github.io/alpha-research/paper1.html`.
- **Code Repository:** Bryan Vine, `alpha-research` repository, commit `17b8b5e1c79af194f733544517d82e3cf12c2259` (August 23, 2026), paths:
  - `docs/paper1.html`
  - `alpha_research/factors/vrp.py`
  - `scripts/01_vrp_core.py`
  - `scripts/02_vrp_rigor.py`
  - `scripts/03_equity_vrp_benchmark.py`
  - `scripts/40_paper1_figures.py`
  - `research/paper1_equity_benchmark.md`
  - `research/paper1_data_profile.md`
  - `alpha_research/eval/rigor.py`
- **Academic Literature Referenced in Primary Source:**
  - T. Bollerslev, G. Tauchen & H. Zhou (2009). *"Expected Stock Returns and Variance Risk Premia."* Review of Financial Studies 22(11).
  - P. Carr & L. Wu (2009). *"Variance Risk Premiums."* Review of Financial Studies 22(3).
  - I. Dew-Becker & S. Giglio (2025). *"The Decline of the Variance Risk Premium: Evidence from Traded and Synthetic Options."* Federal Reserve Bank of Chicago Working Paper 2025-17.
  - D. Bailey & M. López de Prado (2014). *"The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting and Non-Normality."* Journal of Portfolio Management.
  - D. Bailey, J. Borwein, M. López de Prado & Q. Zhu (2017). *"The Probability of Backtest Overfitting."* Journal of Computational Finance.
  - Deribit (2021). *"DVOL — Deribit Implied Volatility Index: Methodology."*
