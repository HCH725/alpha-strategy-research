---
schema: strategy-research-record-v1
title: Coffee Commodity Weather-Stress Lagged Futures Overlay
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - commodities
  - soft-commodities
  - arabica-coffee
  - weather-stress
  - era5-reanalysis
  - volatility-targeting
  - ewma
status: research-only
confidence: medium
source_as_of: 2026-09-10
sources:
  - "Liam Son, 'Coffee Commodity Alpha: weather-stress measurement and futures overlays', GitHub repository Liam-Son/coffee-commodity-alpha, commit 34ccd268aa95a9942a794858f2371062a46a59ea, published September 2026, as-of 2026-09-10"
  - "Liam Son, 'Engine Test Results — 2015-01 → 2025-12', results/engine_test_2015_2025.md, commit 34ccd268aa95a9942a794858f2371062a46a59ea"
  - "Liam Son, 'Deflated Sharpe Ratio — registered overlay', results/deflated_sharpe_2015_2025.md, commit 34ccd268aa95a9942a794858f2371062a46a59ea"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Coffee Commodity Weather-Stress Lagged Futures Overlay

## Provenance

- **Author / Research Desk:** Liam Son (2026), working paper repository and empirical research codebase.
- **Title:** *Coffee Commodity Alpha: weather-stress measurement and futures overlays*.
- **Canonical Repository:** `https://github.com/Liam-Son/coffee-commodity-alpha`
- **Immutable Commit SHA:** `34ccd268aa95a9942a794858f2371062a46a59ea`
- **Source As-Of Date:** 2026-09-10
- **Primary Code Paths:**
  - Signal & execution entry point: `strategies/weather_stress_long.py`
  - Weather measurement engine: `src/weather_data.py`
  - Feature index library: `src/weather_indices.py`
  - Backtesting & vol targeting: `src/backtest.py`
  - Data loaders & publication lag alignment: `src/data_loaders.py`
  - Econometric yield & price specifications: `src/yield_price_models.py`
  - Evaluation & Deflated Sharpe: `src/evaluation.py`
  - Backtest results log: `results/engine_test_2015_2025.md`
  - Deflated Sharpe analysis: `results/deflated_sharpe_2015_2025.md`
  - Formal methodology & design: `docs/RESEARCH_DESIGN.md`, `docs/METHODOLOGY.md`, `docs/LIMITATIONS.md`
- **Licence & Rights:** Code is open-source under the MIT License (Copyright 2026 Liam Son); weather reanalysis data from Open-Meteo / ERA5 under CC BY 4.0; price data via Yahoo Finance terms. No proprietary or private invite-only scripts involved.
- **Deduplication Audit:** Repository-wide inspection confirms zero existing records for `coffee`, `KC`, `Arabica`, `weather-stress`, `ERA5`, `EHD`, `HDD`, or author `Liam Son`. Existing commodity records focus on crude oil crack spreads (`crude-oil-crack-spread-seasonally-adjusted-mean-reversion-stop-lockout-2026-09-12.md`), cross-asset momentum, or calendar spreads, leaving agricultural soft-commodity weather-stress supply shocks completely unrepresented.

## Economic mechanism

### Source-reported

Arabica coffee (*Coffea arabica*) yields are physiologically sensitive to thermal and hydrologic stress during phenological stages including flowering (September–November in the Southern Hemisphere) and bean filling (December–March). Brazil is the world's dominant exporter of Arabica coffee, and ICE Arabica futures (ticker `KC`) serve as the benchmark pricing contract for physical supply. 

The author hypothesizes that:
1. Publicly available reanalysis weather (ECMWF ERA5 / ERA5-Land) can be aggregated over the core Brazilian Arabica growing belt (Southern Minas Gerais, Cerrado Mineiro, and Mogiana) into a composite stress index capturing Extreme Heat Days (EHD) and precipitation deficits.
2. Because agricultural supply shocks manifest with biological delays and official harvest/crop reports (such as CONAB or USDA attributions) are published with substantial reporting lags, financial futures prices do not instantaneously absorb reanalysis weather information contemporaneously.
3. Therefore, a strictly lagged weather-stress index contains incremental predictive content for subsequent Arabica futures returns, enabling a sparse directional overlay that selectively goes long during severe drought/heat stress, short during benign/surplus conditions, and remains flat otherwise.

### Research interpretation

This strategy represents a **fundamental physical supply-shock transmission overlay** on an agricultural commodity futures contract. The underlying economic anomaly stems from **information-processing latency and delayed biological transmission**:
- Financial market participants continuously price visible macro factors, currency fluctuations (USD/BRL), and headline crop reports, but real-time spatial weather aggregation across regional microclimates requires non-trivial processing.
- When extreme thermal stress (Tmax $\ge 31^\circ\text{C}$) combines with negative precipitation anomalies in key Brazilian growing districts, flower abortion and stunted bean development induce structural crop loss that cannot be mitigated before harvest.
- Rather than attempting high-turnover directional forecasting, the strategy behaves as a **sparse regime overlay** (~71.7% flat): it exposes capital to Arabica futures only during structural weather extremes, capturing asymmetric upward supply squeezes while applying an exponentially weighted moving average (EWMA) volatility targeting budget to prevent excessive tail risk during commodity volatility surges.

## Signal

### Formation timestamp

Monthly weather indices are computed at the conclusion of calendar month $t$. To prevent any contemporaneous measurement look-ahead, the composite stress series is strictly shifted forward by **one calendar month** (`lag_months = 1` via `build_lagged_stress`). The monthly lagged observation is then forward-filled onto daily trading days. 

Trading positions are updated on daily closes with **next-bar execution** (`position_lag = 1`), meaning a signal evaluated at date $T$ is executed at the close of $T+1$.

### Lookback & Weather Indices

- **Spatial points:** Equal-weighted average of 5 representative coordinates across the Brazilian Arabica belt:
  - `sul_de_minas` (-21.55, -45.43)
  - `sul_minas_2` (-21.15, -44.95)
  - `cerrado_mineiro` (-18.92, -46.99)
  - `cerrado_2` (-19.45, -46.55)
  - `mogiana` (-22.25, -46.75)
- **Extreme Heat Days (EHD):** Monthly count of days where daily maximum temperature $T^{\max}_d \ge 31^\circ\text{C}$:
  $$\mathrm{EHD}_m = \sum_{d \in m} \mathbf{1}\{T^{\max}_d \ge 31^\circ\text{C}\}$$
- **Harmful Degree Days (HDD):** Monthly thermal accumulation above $30^\circ\text{C}$:
  $$\mathrm{HDD}_m = \sum_{d \in m} \max(T^{\max}_d - 30.0, 0.0)$$
- **Precipitation Anomaly ($A_m$):** Standardized monthly precipitation sum relative to trailing 12-month rolling mean and standard deviation (minimum 6 months):
  $$A_m = \frac{P_m - \bar{P}_{m, 12}}{s_{m, 12}}$$
- **Composite Stress Score ($S_m$):** A priori weighted combination of standardized components:
  $$S_m = 0.35 \cdot z(\mathrm{EHD}_m) + 0.25 \cdot z(\mathrm{HDD}_m) + 0.40 \cdot (-A_m)$$
  where $z(x) = (x - \bar{x}) / s_x$. The composite score is clipped to $[-2.5, 4.0]$ and lagged by 1 month.

### Directional Triggers

The raw directional signal is formed from lagged stress $S$:
- **Long Entry:** $S > 0.8 \implies \text{signal} = +1.0$ (severe drought / extreme heat stress).
- **Short Entry:** $S < -0.6 \implies \text{signal} = -0.4$ (cool, wet, highly favorable growing conditions; sized asymmetrically at 40% short exposure).
- **Flat / Exit:** $-0.6 \le S \le 0.8 \implies \text{signal} = 0.0$ (neutral / normal weather conditions).

### Volatility Targeting & Position Sizing

The strategy applies an optional EWMA volatility targeting mechanism to determine final position size:
1. Estimate daily price return variance using EWMA with span $30$ ($\lambda \approx 0.9355$, min periods 10):
   $$\sigma^2_t = \mathrm{EWMA}_{30}(r^2_t)$$
2. Annualize volatility using factor 252 and lag by 1 day to block look-ahead:
   $$\hat{\sigma}_t = \sqrt{252 \cdot \sigma^2_{t-1}}$$
3. Compute target weight with clipping between $[0.25, 2.0]$:
   $$w_t = \mathrm{clip}\left(\frac{\sigma^\star}{\hat{\sigma}_t}, 0.25, 2.0\right)$$
   where default annualised target volatility $\sigma^\star = 0.10$ (10%).
4. Final executed position:
   $$\text{position}_t = \text{signal}_{t-1} \cdot w_{t-1}$$

### Parameters

| Parameter | Value | Classification |
|---|---|---|
| EHD temperature threshold | $31.0^\circ\text{C}$ | Source-reported |
| HDD base temperature | $30.0^\circ\text{C}$ | Source-reported |
| EHD composite weight | $0.35$ | Source-reported |
| HDD composite weight | $0.25$ | Source-reported |
| Precip anomaly composite weight | $0.40$ | Source-reported |
| Precip lookback window | 12 months (min 6) | Source-reported |
| Stress publication lag | 1 month | Source-reported |
| Long threshold | Stress $> 0.8$ | Source-reported |
| Short threshold | Stress $< -0.6$ | Source-reported |
| Short position scale | $-0.4$ | Source-reported |
| Volatility target ($\sigma^\star$) | $10.0\%$ annualized | Source-reported |
| EWMA volatility span | 30 bars ($\lambda \approx 0.94$) | Source-reported |
| Leverage floor / ceiling | $[0.25, 2.0]$ | Source-reported |
| Volatility forecast lag | 1 bar | Source-reported |
| Position execution lag | 1 bar (next-bar close) | Source-reported |
| Transaction cost | 5.0 bps on absolute turnover | Source-reported |
| Order type / fill convention | Market-on-close / daily close | `research-proposed` |
| Maximum portfolio risk budget | 1x commodity book allocation | `research-proposed` |

## Required data

- **Instruments:** ICE Arabica Coffee futures (front-month / continuous series `KC=F`).
- **Venue:** Intercontinental Exchange (ICE Futures US); continuous price proxy via Yahoo Finance.
- **Market Type:** Physical agricultural commodity deliverable futures.
- **Timeframe:** Daily close prices for execution; monthly aggregated weather indices (derived from hourly/daily weather records).
- **Required Fields:**
  - Market data: Daily close price `price` (adjusted for contract level).
  - Weather data: Daily maximum 2m air temperature `temperature_2m_max`, daily minimum 2m temperature `temperature_2m_min`, daily total precipitation `precipitation_sum`.
- **Weather Data Source:** ECMWF ERA5 / ERA5-Land reanalysis via Open-Meteo Historical Weather Archive.
- **Timezone:** `America/Sao_Paulo` (UTC-3) for Brazilian weather observations; UTC / NY close for ICE futures.
- **Point-in-Time Availability:** The 1-month publication lag enforces that month $m$'s weather is only used starting on the first trading day of month $m+1$, preventing same-month revision look-ahead.
- **Missing Data Handling:** Forward-fill monthly stress onto daily price dates; missing daily values backfilled to zero if at inception.

## Execution assumptions

- **Execution Timing:** Next-bar daily close execution (`position_lag = 1`). Orders placed following signal generation at close $T$ are executed at close $T+1$.
- **Order Type:** Assumed executed at daily settlement / close price via Market-on-Close (MOC) (`research-proposed`).
- **Transaction Costs:** Flat 5.0 basis points ($0.05\%$) deducted from gross strategy returns on every unit of absolute turnover:
  $$\text{cost}_t = 0.0005 \cdot |\text{position}_t - \text{position}_{t-1}|$$
- **Slippage & Market Impact:** Not separately modeled beyond the 5 bp flat cost; coffee futures intraday limit moves or liquidity gaps during freeze/frost events are unmodeled (`research-proposed`).
- **Borrow / Shorting:** Agricultural futures allow symmetric long and short positions through margin accounts; no stock borrow fee applies, though margin requirements and variation margin financing apply.
- **Roll Model:** Source uses Yahoo Finance auto-adjusted continuous futures (`KC=F`), which omits formal roll calendar rules, calendar spread costs, and roll yield dynamics (`research-proposed`).
- **Capacity:** Underspecified by source; Arabica futures open interest supports institutional desk execution up to tens of millions USD, but concentrated weather-driven order flow during crisis windows faces wider bid-ask spreads (`research-proposed`).

## Evidence

### Source-reported

All quantitative performance figures are directly extracted from Liam Son's registered engine test (`results/engine_test_2015_2025.md`) and Deflated Sharpe analysis (`results/deflated_sharpe_2015_2025.md`), evaluated over the 11-year sample period from **2015-01-01 to 2025-12-31** ($N = 2,767$ daily trading bars):

#### Headline Backtest Results (2015–2025)

| Metric | Vol-Target 10% | No Vol Target | Buy & Hold KC | Source Attribution |
|---|---|---|---|---|
| **CAGR** | **+1.8%** | **+5.8%** | +12.7% | Son (2026), `engine_test_2015_2025.md` |
| **Annualized Volatility** | **4.6%** | **13.0%** | 33.6% | Son (2026), `engine_test_2015_2025.md` |
| **Sharpe Ratio (annualized)** | **0.40** | **0.45** | 0.38 | Son (2026), `engine_test_2015_2025.md` |
| **Maximum Drawdown** | **−14.8%** | **−29.9%** | −51.9% | Son (2026), `engine_test_2015_2025.md` |
| **Hit Rate** | **14.2%** | **14.2%** | 49.4% | Son (2026), `engine_test_2015_2025.md` |
| **Terminal Multiple ($1.00 $\to$)** | **1.21×** | **1.72×** | 2.17× | Son (2026), `engine_test_2015_2025.md` |

#### Portfolio Exposure Profile
- **Mean Vol-Weight:** $0.33$ (range $0.25$ to $1.00$, indicating 10% target vol severely de-levers against KC's 33.6% native volatility).
- **Average Absolute Position $|\text{position}|$ (with VT):** $0.054$ (highly defensive).
- **Time in Market:**
  - Long: **8.9%** of trading days
  - Short: **19.3%** of trading days
  - Flat (Neutral): **71.7%** of trading days

#### Multiple Testing & Deflated Sharpe Ratio (Bailey & López de Prado 2014)
From `results/deflated_sharpe_2015_2025.md` ($N = 2,767$ daily observations, daily Sharpe = annualised / $\sqrt{252}$):
- **Overlay (No Vol Target, 8 trials):** Annual Sharpe 0.45, Daily Sharpe 0.028, Expected Max Sharpe 0.44 $\implies$ **DSR = 0.51**.
- **Overlay (No Vol Target, 20 trials):** Annual Sharpe 0.45, Daily Sharpe 0.028, Expected Max Sharpe 0.57 $\implies$ **DSR = 0.34**.
- **Overlay (Vol Target 10%, 8 trials):** Annual Sharpe 0.40, Daily Sharpe 0.025, Expected Max Sharpe 0.44 $\implies$ **DSR = 0.45**.
- **Buy & Hold (1 trial null):** Annual Sharpe 0.38, Daily Sharpe 0.024 $\implies$ DSR = 0.90.

The author explicitly notes that under 8 to 20 evaluated parameter configurations, a DSR of 0.34–0.51 indicates the Sharpe of 0.45 is indistinguishable from the expected maximum of noise trials, refusing a discovery claim.

### Independently reproduced

Not independently reproduced. The empirical metrics above are source-reported by Liam Son (2026).

### Negative evidence

The primary source explicitly details extensive negative and cautionary findings:
1. **Lower Raw Compound Return:** The strategy CAGR (+1.8% with vol targeting, +5.8% without) severely underperforms passive buy-and-hold (+12.7%), because the overlay is out of the market 71.7% of the time and misses sustained non-weather bull trends.
2. **Deflated Sharpe Insignificance:** DSR is only 0.34–0.51 when accounting for modest parameter trials, demonstrating lack of statistical significance over the 2015–2025 sample.
3. **Severe Event Dominance:** Performance is heavily dependent on single catastrophic weather events (specifically the July 2021 Brazilian frost and drought crisis); removing 2021 reduces performance substantially.
4. **Initial Specification Failure:** An initial higher EHD threshold of $33.0^\circ\text{C}$ yielded only 30 stress days over 11 years, forcing a post-hoc downward calibration to $31.0^\circ\text{C}$ (indicating threshold data-snooping risk).
5. **Lack of Yield Micro-foundation:** Regressions of weather onto official municipal coffee yields (CONAB/IBGE) were specified but could not be estimated due to lack of official panel datasets in the repository.

## Falsification plan

To falsify the weather-stress alpha transmission hypothesis:
1. **Out-of-Sample Window Test:** Evaluate the exact frozen rule over post-2025 data (2026–2028).
2. **Leave-One-Crisis-Out Test:** Exclude the calendar year 2021 (the historic Brazilian frost/drought anomaly). If strategy Sharpe without 2021 drops below 0.0 or underperforms cash risk-free rate, the hypothesis of a stable persistent alpha mechanism is rejected.
3. **Placebo Shuffled-Weather Test:** Permute the monthly weather stress series across time while preserving KC price return series (1,000 Monte Carlo draws). If the historical strategy Sharpe falls within the 90% confidence band of shuffled-weather returns, the weather-to-price transmission is falsified.
4. **Alternative Production Belts Test:** Replace Brazilian weather with weather from Vietnam (the dominant Robusta producer) or Colombia. If Brazilian Arabica futures respond more strongly to Vietnamese weather than Brazilian weather for KC contracts, the regional agronomic transmission mechanism is invalid.
5. **Research-Defined Falsification Threshold:** The strategy hypothesis shall be considered falsified if:
   - Out-of-sample annualized Sharpe drops below $0.15$ over any rolling 36-month period; OR
   - Maximum drawdown under the 10% vol-targeted model exceeds $-25.0\%$; OR
   - The Deflated Sharpe Ratio under a full walk-forward parameter audit fails to exceed $0.80$ ($p > 0.20$).

## Crypto portability

**Portability Classification: Adapted / Unproven.**

The strategy operates on physical agricultural commodity futures and relies on satellite reanalysis weather data over Brazilian agrarian coordinates. It has no native presence in cryptocurrency spot or perpetual markets:
- **Synthetic & Tokenized Commodity Perps:** Decentralized perpetual exchanges (e.g., Synthetix, Hyperliquid, dYdX, Drift) or centralized exchanges (e.g., Binance, Bybit) occasionally list tokenized commodity indices or synthetic commodity perpetuals. If an Arabica coffee perpetual contract is listed, the signal could technically be ported to trade crypto commodity synthetics.
- **Crypto Portability Risks:**
  - **Oracle Basis & Desync:** Crypto synthetic commodities rely on Pyth or Chainlink price feeds that may suffer latency or liquidity disconnects from the underlying ICE futures during volatile CME/ICE halts.
  - **Funding Rate Distortion:** In perpetual markets, funding rates fluctuate wildly based on crypto retail sentiment rather than physical storage and financing costs, potentially eroding the modest +1.8% to +5.8% strategy CAGR.
  - **24/7 vs Session Windows:** ICE KC trades within strict market hours (04:15 to 13:30 NY time), whereas crypto perpetuals trade 24/7. Executing daily close signals across fragmented weekend sessions requires custom session alignment rules (`research-proposed`).
  - **On-chain Parametric Weather Contracts:** The weather index engine could theoretically settle on-chain parametric agricultural insurance or prediction market contracts (e.g., Polymarket, Arbol), but this remains an adapted concept with zero demonstrated empirical evidence.

## Limitations

- **Continuous Contract Distortion:** Tested on Yahoo Finance continuous auto-adjusted futures (`KC=F`) rather than an institutional back-adjusted front-month roll contract with explicit calendar roll rules.
- **Unweighted Spatial Average:** Simple equal-weighted 5-point coordinate average does not reflect true production-weighted Brazilian municipal output (e.g., Cerrado vs Sul de Minas yield disparities).
- **Sparse Signal & Low Capacity Utilization:** Signal is active only 28.3% of trading days (71.7% flat), producing low annualized compound growth (+1.8% at 10% vol target) despite drawdown dampening.
- **High Sensitivity to Single Crisis:** Dominated by the 2021 frost/drought regime; vulnerable to regime shifts under climate change or shifting global Robusta substitution.
- **No Transaction-Cost Calibration for Stressed Sessions:** Assumes a flat 5 bp cost, which severely underestimates bid-ask spreads during limit-up weather shock sessions.
- **Underspecified Intra-day Execution:** Daily close fills ignore intra-day volatility and execution slippage.

## Implementation status

`not-implemented`. No implementation exists within our NautilusTrader, PyBroker, paper trading, testnet, or live production stack. This capture documents upstream academic research only.

## Adoption boundary

`research-only` / `not-approved`. 
This record is cataloged strictly for research knowledge handoff. Ingestion of this document does not constitute:
- Verification of positive expected net economic alpha;
- Approval for portfolio inclusion or capital allocation;
- Authorization for paper trading, testnet deployment, or live order execution.

Any future consideration requires primary testing on research-grade roll-adjusted ICE futures data, production-weighted spatial grids, and formal walk-forward significance testing.

## Related Wiki records

- `[[crude-oil-crack-spread-seasonally-adjusted-mean-reversion-stop-lockout-2026-09-12]]` — Commodity mean-reversion with seasonal adjustment and lockout stops.
- `[[commodity-futures-hierarchical-graph-learning-calendar-spread-2026-09-02]]` — Graph-based calendar spread modeling in commodity futures.
- `[[commodity-futures-network-momentum-lead-lag-graph-learning-2026-09-02]]` — Cross-commodity network momentum and lead-lag dynamics.
- `[[futures-trend-following-autocorrelation-drift-decomposition-2026-09-02]]` — Drift decomposition and trend following in futures markets.
- `[[futures-volatility-normalized-tick-size-trend-following-filter-2026-09-02]]` — Volatility-normalized tick filtering in futures execution.

## Sources

1. **Liam Son (2026).** *Coffee Commodity Alpha: weather-stress measurement and futures overlays*. GitHub repository `Liam-Son/coffee-commodity-alpha`, commit `34ccd268aa95a9942a794858f2371062a46a59ea`, dated 2026-09-10. Open-source under MIT License. URL: https://github.com/Liam-Son/coffee-commodity-alpha
2. **Liam Son (2026).** *Engine Test Results — 2015-01 → 2025-12*. `results/engine_test_2015_2025.md`, commit `34ccd268aa95a9942a794858f2371062a46a59ea`. Reports headline backtest statistics on KC=F across 2015–2025.
3. **Liam Son (2026).** *Deflated Sharpe Ratio — registered overlay*. `results/deflated_sharpe_2015_2025.md`, commit `34ccd268aa95a9942a794858f2371062a46a59ea`. Evaluates Bailey & López de Prado (2014) multiple testing statistics across 8–20 trial configurations.
4. **Liam Son (2026).** *Research Design & Methodology*. `docs/RESEARCH_DESIGN.md` and `docs/METHODOLOGY.md`, commit `34ccd268aa95a9942a794858f2371062a46a59ea`. Formalizes identification assumptions, EHD/HDD mathematical definitions, and limitation disclosures.
5. **ECMWF / Copernicus Climate Change Service (C3S).** *ERA5: Fifth generation of ECMWF atmospheric reanalyses of the global climate*. Accessed via Open-Meteo Historical Weather Archive API under CC BY 4.0 license.
