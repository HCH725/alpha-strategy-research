---
schema: strategy-research-record-v1
title: "Institutional Futures VoV Quad Multi-Alpha Composite: Systematic Trend, Carry, Skew, and Vol-of-Vol with Zero Fitted Parameters"
created: 2026-09-11
updated: 2026-09-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - multi-alpha
  - futures
  - trend-following
  - carry
  - skewness
  - volatility-of-volatility
  - portfolio-construction
status: research-only
confidence: high
source_as_of: 2026-05-26
sources:
  - "Lucas Joly, 'Trends Research — Systematic Momentum in Global Futures', MSc 2 Mémoire, INSEEC, GitHub repository Lucas-Joly-GH/trends-research (commit 4fb581c9866b031a55ad5e4cb14a684e0e60c10d, 2026)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Institutional Futures VoV Quad Multi-Alpha Composite: Systematic Trend, Carry, Skew, and Vol-of-Vol with Zero Fitted Parameters

## Provenance

- **Primary Source:** Lucas Joly (INSEEC MSc 2 Mémoire in Quantitative Finance, Academic Advisor: Georges Lionel), *"Trends Research — Systematic Momentum in Global Futures: A Master's-thesis research programme on serial autocorrelation and trend-persistence in linear derivatives"*, GitHub repository: `https://github.com/Lucas-Joly-GH/trends-research`.
- **Immutable Provenance:** Full Git commit SHA `4fb581c9866b031a55ad5e4cb14a684e0e60c10d`.
- **Key Source Paths:**
  - Architecture and strategy implementation: `flagship_S183/ig_strategy_183.py`
  - Statistical testing suite & ablation matrix: `flagship_S183/ig_testing_suite_183.py`
  - Standalone alpha library summary: `alpha_library/single_alpha_summary.csv`
  - Signal-shuffle null distribution test: `flagship_S183/robustness_runs/t17_signal_shuffle_result.json`
  - Instrument universe mapping and cost matrix: `Live/instrument_mapping.csv`
  - Readme and out-of-sample paper trading report: `README.md`
- **Source As-of Date:** May 26, 2026 (backtest spans 1990-01-01 to 2026-01-02 [9,341 trading days]; forward out-of-sample paper trading spans 2026-01-02 to 2026-05-26 [145 trading days]).
- **Deduplication Audit:** Verified against all existing records in `alpha-strategy-research`. Zero prior records cite Lucas Joly, repository `Lucas-Joly-GH/trends-research`, Strategy S183, or this specific 4-alpha composite.

## Economic mechanism

### Source-reported

The strategy investigates whether a multi-alpha futures portfolio constructed with zero backtest-fitted parameters—where every parameter is either derived from first principles or grounded in established literature—can survive adversarial multiple-testing corrections (Harvey & Liu BHY haircuts, White's Reality Check, and Bailey & López de Prado Deflated Sharpe Ratio).

The flagship strategy (S183, `IG VoV Quad Sharpened`) combines four equal-weighted ($25\%$ each) orthogonal alpha mechanisms across a liquid multi-asset futures universe:
1. **Time-Series & Cross-Sectional Trend ($25\%$):** Exploits serial autocorrelation in linear derivatives driven by slow information diffusion, risk-budgeting feedback loops, and persistent hedger rebalancing (Moskowitz, Ooi, & Pedersen 2012; Levine & Pedersen 2016). Formulated as a 50/50 blend of 3-speed Time-Series Exponential Weighted Moving Average Crossover (TS-EWMAC) and 256-day Cross-Sectional (XS) normalized price rank momentum.
2. **Structural Carry ($25\%$):** Harvests the convenience yield, term structure slope, and basis convergence premium across commodity, interest rate, FX, and equity index futures contracts (Koijen et al. 2018; Carver 2015).
3. **Inverted Rolling Skewness ($25\%$):** Capitalizes on the crash-risk premium (Harvey & Siddique 2000; Amaya et al. 2015). Investors exhibit lottery preferences (overpaying for positive-skew assets) and crash aversion (demanding higher expected returns for negatively skewed assets). Systematically going long negative-skew assets and short positive-skew assets harvests this asymmetry.
4. **Direction-Conditioned Volatility-of-Volatility ($25\%$):** Exploits volatility clustering and regime stability (Baltussen et al. 2018). Inverted volatility-of-volatility (VoV) measures volatility compression relative to its historical baseline. Low VoV signals a quiet, orderly regime where trends persist, while VoV spikes signal regime breakdown and forced liquidation. Crucially, the author discovers that inverted VoV is only an exposure-sizing amplifier; multiplying inverted VoV by the prevailing 64-day trend direction creates a potent, orthogonal directional alpha sleeve.

To harvest these sleeves without parameter fitting, the strategy employs:
- A **Universe-Pooled 4x4 Forecast Diversification Multiplier (FDM)** that scales risk dynamically according to empirical cross-alpha diversification, capped at the theoretical zero-correlation bound $\sqrt{N} = \sqrt{4} = 2.0$.
- A **First-Order IIR Forecast Smoother** whose half-life is structurally pinned to the daily position rebalancing cadence ($\tau = 1$ trading day, $\alpha = 0.5$, span $= 3$).
- **Soft Logistic Volatility and Drawdown Gates** whose trigger thresholds and steepness ($k = 2 / \sigma_{\text{target}} = 10.0$ at 20% annualized volatility target) are derived from the single global volatility budget without free curve-fitting parameters.

### Research interpretation

The S183 architecture represents a disciplined institutional template for combining orthogonal risk premia under structural risk budgeting:
1. **Orthogonality as Drawdown Protection:** Pure trend-following strategies suffer catastrophic drawdowns during choppy, mean-reverting, or macro-inflection regimes (e.g., post-2010 CTA headwinds, where pure EWMAC Sharpe dropped to 0.40). Standalone carry and skewness have near-zero average correlation with trend ($r \approx 0.02 - 0.11$). VoV with direction has an empirical correlation of $-0.012$ with the other alphas, functioning as an internal structural diversifier.
2. **The "Cliff-Edge" of VoV Direction Conditioning:** Standalone volatility-of-volatility possesses no inherent directional sign. Blindly buying low VoV assumes volatility compression is bullish, which fails during grinding bear markets. Conditioning VoV on the sign of the 64-day return creates an adaptive trend accelerator: it aggressively rides persistent trends during calm volatility regimes, but collapses exposure when volatility becomes unstable.
3. **Non-Parametric Risk Governance:** Traditional quantitative models optimize sizing parameters (e.g., lookback windows, stop-loss percentages) via in-sample grid search, creating severe selection bias. Deriving overlay parameters directly from the portfolio volatility target ($\sigma_{\text{target}} = 0.20 \implies k = 10.0, \text{Threshold}_{\text{DD}} = -\sigma_{\text{target}}/2 = -0.10$) eliminates backtest tuning degrees of freedom and establishes a mathematically consistent risk-floor response.

## Signal

The strategy runs on a daily end-of-day cadence across $M$ universe assets. All lookbacks adhere to a base-2 canonical calendar ($256$ trading days per year, $128$ half-year, $64$ quarter, $1280 = 5 \times 256$ warm-up).

### 1. Alpha Sleeve 1: Trend ($W_{\text{trend}} = 0.25$)
Trend is an equal sub-blend ($50\%$ TS, $50\%$ XS):
- **Time-Series EWMAC ($W_{\text{ts}} = 0.5$):**
  - Evaluates 3 canonical speed pairs from Levine & Pedersen (2016): $(16, 64)$, $(32, 128)$, and $(64, 256)$ days. Pair weights are uniform $1/3$ each.
  - Blended price volatility $\sigma_{\text{blended}, i, t}$ is calculated using Carver's rule: $0.70 \times \text{EWM}_{32}(\Delta P_{i, t}) + 0.30 \times \text{Rolling}_{2560}(\Delta P_{i, t})$.
  - For each pair $(f, s)$:
    $$\text{EWMAC}_{i, t}^{(f, s)} = \frac{\text{EMA}_f(P_{i, t}) - \text{EMA}_s(P_{i, t})}{\sigma_{\text{blended}, i, t}}$$
  - Each raw EWMAC is multiplied by its rolling forecast scalar (scaling factor ensuring rolling average absolute forecast equals $10.0$) and capped to $[-20.0, +20.0]$.
  - $\text{Forecast}_{\text{TS}, i, t} = \text{Cap}_{20}\left(\sum_{k=1}^3 \frac{1}{3} \text{ScaledEWMAC}_{i, t}^{(k)}\right)$.
- **Cross-Sectional Momentum ($W_{\text{xs}} = 0.5$):**
  - Normalized price series: $Z_{i, t} = \sum_{s=1}^t \frac{\Delta P_{i, s}}{\sigma_{\text{blended}, i, s}}$.
  - Raw XS momentum: $M_{i, t} = Z_{i, t} - Z_{i, t-256}$.
  - Cross-sectional z-score computed across all active universe assets on day $t$ (valid if active assets $N_t \ge 3$):
    $$z_{i, t} = \frac{M_{i, t} - \mu_{M, t}}{\sigma_{M, t}}$$
  - Scaled by rolling forecast scalar and capped to $[-20.0, +20.0]$: $\text{Forecast}_{\text{XS}, i, t}$.
- **Trend Blend:** $\text{Forecast}_{\text{Trend}, i, t} = \text{Cap}_{20}\left(0.5 \cdot \text{Forecast}_{\text{TS}, i, t} + 0.5 \cdot \text{Forecast}_{\text{XS}, i, t}\right)$.

### 2. Alpha Sleeve 2: Carry ($W_{\text{carry}} = 0.25$)
- Computes structural annualized futures roll yield from front and next contract settlement prices:
  $$\text{Carry}_{i, t} = \frac{P_{\text{front}, i, t} - P_{\text{next}, i, t}}{\Delta T \cdot \sigma_{\text{blended}, i, t}}$$
- Multiplied by rolling forecast scalar and capped to $[-20.0, +20.0]$: $\text{Forecast}_{\text{Carry}, i, t}$.

### 3. Alpha Sleeve 3: Inverted Skewness ($W_{\text{skew}} = 0.25$)
- Computes 256-day rolling sample skewness of daily price changes $\Delta P_{i, t}$ (min periods $128$):
  $$\text{Skew}_{i, t} = -\text{RollingSkew}_{256}(\Delta P_{i, t})$$
- Inversion sign ($-$) ensures long exposure to negatively skewed assets.
- Multiplied by rolling forecast scalar and capped to $[-20.0, +20.0]$: $\text{Forecast}_{\text{Skew}, i, t}$.

### 4. Alpha Sleeve 4: Direction-Conditioned Vol-of-Vol ($W_{\text{vov}} = 0.25$)
- Daily price volatility: $\sigma_{21, i, t} = \text{RollingStd}_{21}(\Delta P_{i, t})$ (min periods $10$).
- Volatility of volatility: $\text{VoV}_{i, t} = \text{RollingStd}_{64}(\sigma_{21, i, t})$ (min periods $21$).
- Trailing baseline VoV: $\overline{\text{VoV}}_{i, t} = \text{RollingMean}_{256}(\text{VoV}_{i, t})$ (min periods $64$).
- Inverted normalized VoV:
  $$\text{VoV}_{\text{norm}, i, t} = -\left(\frac{\text{VoV}_{i, t}}{\overline{\text{VoV}}_{i, t}} - 1.0\right)$$
- Medium-term trend direction sign:
  $$\text{Dir}_{i, t} = \text{sign}\left(\frac{P_{i, t}}{P_{i, t-64}} - 1.0\right) \in \{-1.0, +1.0\}$$
- Directional VoV signal: $\text{VoV}_{\text{raw}, i, t} = \text{Dir}_{i, t} \times \text{VoV}_{\text{norm}, i, t}$.
- Multiplied by rolling forecast scalar and capped to $[-20.0, +20.0]$: $\text{Forecast}_{\text{VoV}, i, t}$.

### 5. Quad Blend & Universe-Pooled FDM
- Raw 4-sleeve linear combination:
  $$\text{Blend}_{i, t} = 0.25 \cdot \text{Forecast}_{\text{Trend}, i, t} + 0.25 \cdot \text{Forecast}_{\text{Carry}, i, t} + 0.25 \cdot \text{Forecast}_{\text{Skew}, i, t} + 0.25 \cdot \text{Forecast}_{\text{VoV}, i, t}$$
- **Universe-Pooled 4x4 FDM Calculation:**
  - Computes cross-sectional mean series for each sleeve: $\bar{F}_{\text{sleeve}, t} = \frac{1}{M_t} \sum_{i=1}^{M_t} \text{Forecast}_{\text{sleeve}, i, t}$.
  - Estimates $4 \times 4$ correlation matrix $C_t$ via exponentially weighted moving correlation ($\text{span} = 512$ days, min periods $256$).
  - Blend variance: $\sigma_{\text{blend}, t}^2 = w^T C_t w$, where $w = [0.25, 0.25, 0.25, 0.25]^T$.
  - Theoretical zero-correlation cap: $\text{FDM}_{\text{cap}} = \sqrt{N} = \sqrt{4} = 2.0$. Floor $= 1.0$.
  - $\text{FDM}_t = \text{clip}\left(\frac{1}{\sqrt{\sigma_{\text{blend}, t}^2}}, 1.0, 2.0\right)$.
  - Amplified forecast: $\text{ScaledBlend}_{i, t} = \text{Cap}_{20}\left(\text{Blend}_{i, t} \times \text{FDM}_t \times \text{RollingScalar}_t\right)$.

### 6. Forecast Smoothing & Soft Logistic Risk Overlays
- **Cadence-Matched Smoothing:** Master forecast is filtered using an IIR smoother with half-life equal to the 1-day execution rebalance cadence ($\alpha = 0.5$, span $= 3$):
  $$\text{Forecast}_{\text{smooth}, i, t} = 0.5 \cdot \text{ScaledBlend}_{i, t} + 0.5 \cdot \text{Forecast}_{\text{smooth}, i, t-1}$$
- **Soft Logistic Risk Overlays:**
  - Derived steepness: $k = \frac{2.0}{\sigma_{\text{target}}} = \frac{2.0}{0.20} = 10.0$.
  - Risk floor: $\text{Dampen} = 0.50$ (half risk during extreme stress).
  - Realized Volatility Gate (64-day annualized volatility ratio):
    $$\text{Ratio}_{\text{vol}, i, t} = \frac{\text{RollingStd}_{64}\left(\frac{\Delta P_{i}}{P_{i}}\right) \times \sqrt{256}}{\sigma_{\text{target}}}$$
    $$\text{Gate}_{\text{vol}, i, t} = 1.0 - (1.0 - 0.50) \times \text{logistic}\left(10.0 \times (\text{Ratio}_{\text{vol}, i, t} - 1.0)\right)$$
  - Trailing Drawdown Gate (64-day return proxy, lagged 1 day):
    $$\text{DD}_{\text{proxy}, i, t} = \frac{P_{i, t-1}}{P_{i, t-65}} - 1.0$$
    $$\text{Threshold}_{\text{DD}} = -\frac{\sigma_{\text{target}}}{2} = -0.10 \quad (-10\%)$$
    $$\text{Gate}_{\text{dd}, i, t} = 1.0 - (1.0 - 0.50) \times \text{logistic}\left(10.0 \times (-0.10 - \text{DD}_{\text{proxy}, i, t})\right)$$
  - **Final Master Forecast:**
    $$\text{Forecast}_{\text{final}, i, t} = \text{clip}\left(\text{Forecast}_{\text{smooth}, i, t} \times \text{Gate}_{\text{vol}, i, t} \times \text{Gate}_{\text{dd}, i, t}, -20.0, +20.0\right)$$

## Required data

- **Universe:** 62 liquid global futures contracts across 6 asset classes:
  - FX: 6A (AUD), 6B (GBP), 6C (CAD), 6E (EUR), 6J (JPY), 6M (MXN), 6N (NZD), 6S (CHF), DX (US Dollar Index).
  - Short-Term Interest Rates (STIR): SR3 (3M SOFR), LEU9 (3M Euribor), SO3 (3M SONIA).
  - Government Bonds: ZT (US 2Y), ZF (US 5Y), ZN (US 10Y), ZB (US 30Y), UB (Ultra Bond), FGBS9 (Euro-Schatz 2Y), FGBM9 (Euro-Bobl 5Y), FGBL9 (Euro-Bund 10Y), LLG (UK Long Gilt 10Y), CGB (Canadian 10Y), YXT4 (ASX 10Y).
  - Equity Indices: ES (S&P 500), NQ (Nasdaq 100), EMD (S&P MidCap 400), RTY (Russell 2000), FESX9 (Euro STOXX 50), FDAX9 (DAX), FSMI9 (SMI), FDXM9 (Mini-DAX), NKD (Nikkei 225 USD), NIY (Nikkei 225 JPY), HSI (Hang Seng), SPI (ASX 200).
  - Commodities: CL (Crude Oil), NG (Natural Gas), B (Brent Crude), HO (Heating Oil), RB (RBOB Gasoline), GC (Gold), SI (Silver), HG (Copper), PL (Platinum), PA (Palladium), C (Corn), W (Wheat), S (Soybeans), SM (Soybean Meal), BO (Soybean Oil), LC (Live Cattle), LH (Lean Hogs), KC (Coffee), SB (Sugar), CC (Cocoa), CT (Cotton).
  - Volatility: VX (Cboe VIX Futures).
- **Vendor / Data Source:** NorgateData back-adjusted continuous Panama-adjusted price series.
- **Fields:** Open, High, Low, Close, Volume, Open Interest, individual contract expiry/roll cycle dates, daily USD FX rates for non-USD contracts, and US 3-Month Treasury Bill yield (`IRX`) for cash compounding benchmark.
- **Warm-up & Sample Gate:** Strict 5-year per-instrument out-of-sample quarantine gate (`OOS_START = 1280` trading days). No instrument enters portfolio allocation until 1,280 days of continuous historical price and volatility history have elapsed.

## Execution assumptions

- **Position Sizing Engine:** Carver (2015, 2023) forecast-to-position framework:
  $$\text{TargetContracts}_{i, t} = \frac{\text{Capital}_t \times \left(\frac{\sigma_{\text{target}}}{\sqrt{256}}\right)}{\sigma_{\text{price}, i, t} \times \text{FX}_{i, t} \times \text{PointSize}_i} \times \left(\frac{\text{Forecast}_{\text{final}, i, t}}{10.0}\right) \times \text{IDM}_t$$
  where $\text{IDM}_t$ is the Instrument Diversification Multiplier derived dynamically from active asset count $N_t$.
- **Buffer Band:** $10\%$ position buffer threshold (`buffer_fraction = 0.10`). Rebalancing trades are submitted only when $|\text{TargetContracts} - \text{CurrentContracts}| > 0.10 \times |\text{TargetContracts}|$, suppressing low-alpha execution churn.
- **Execution Timing & Fill Model:** Daily market orders executed at the next trading session open or close on exchange.
- **Execution Frictions & Slippage:** Explicit instrument-level round-turn transaction cost matrix (`Live/instrument_mapping.csv`), spanning e.g. $17.50/RT on ES, $10.00/RT on NQ, $12.81/RT on ZF, $15.00/RT on 6A, up to $80.00/RT on VX.
- **Operational Classification:** `research-proposed`: Execution timing on crypto perpetuals or futures at 00:00:00 UTC using TWAP taker/maker execution.

## Evidence

### Source-reported

All figures below are directly reported by Lucas Joly (2026, `README.md`, `flagship_S183/ig_strategy_183.py`, `ig_testing_suite_183.py`, and `alpha_library/single_alpha_summary.csv`):

#### 1. Flagship Strategy S183 Full-Sample Backtest (1990–2026, 9,341 Trading Days)
- **Raw Annualized Sharpe Ratio (excess of T-Bill):** **0.97** (full 36-year history).
- **BHY-Corrected Sharpe Ratio:** **0.78** (Harvey-Liu multiple-testing adjustment across $K = 118$ audited trials, controlling False Discovery Rate).
- **Deflated Sharpe Ratio (Bailey & López de Prado):** $z = 4.28$ ($p < 0.0001$).
- **CAGR:** 15.5%.
- **Annualized Volatility:** 12.9% (targeted at 20%, realized lower due to non-linear risk overlays and FDM damping).
- **Maximum Drawdown:** 21.6% (compounded equity).
- **Calmar Ratio:** 0.72.
- **Fama-French 5-Factor Alpha:** 10.6% annualized ($t = 3.21, p = 0.0013$).
- **Fung-Hsieh 7-Factor Trend Following Alpha:** 13.0% annualized ($t = 5.83$).
- **Decade Sharpe Consistency:**
  - 1990s: 0.90
  - 2000s: 1.02
  - 2010s: 1.19
  - 2020s: 0.74
- **Execution Delay Robustness:** Performance retained under T+1 execution lag is **98.1%** (zero decay from execution delay).

#### 2. Forward Out-of-Sample Paper Trading (Jan 2, 2026 – May 26, 2026, 145 Trading Days)
- Realized Sharpe Ratio (excess of T-Bill): **+0.44**.
- Realized Annualized Return: **+7.33%**.
- Realized Volatility: **8.56%**.
- Maximum Drawdown: **-4.33%**.
- Performance Context: During a strongly risk-on market window dominated by equity momentum and agricultural trend whipsaws, S183 achieved the lowest maximum drawdown in its CTA peer group (-4.33%) while generating positive net excess return.

#### 3. Standalone Alpha Sleeves vs. Quad Composite (Full Sample)
From `alpha_library/single_alpha_summary.csv` and S183 testing reports:
- **EWMAC Ensemble (Trend):** Sharpe 0.57, post-2010 Sharpe 0.40, CAGR 14.3%, Max DD 53.6%.
- **Carry:** Sharpe 0.48, post-2010 Sharpe 0.44, CAGR 9.6%, Max DD 40.1%.
- **Skewness:** Sharpe 0.48, post-2010 Sharpe 0.69, CAGR 10.6%, Max DD 47.8%.
- **Vol-of-Vol (Directional):** Sharpe 0.24, post-2010 Sharpe 0.40, CAGR 5.3%, Max DD 43.8%, Cross-Alpha Correlation -0.012.
- **S183 Quad Composite:** Sharpe **0.97** (vs best standalone 0.57), Max DD **21.6%** (vs best standalone 40.1%). Diversification cuts maximum drawdown in half and nearly doubles Sharpe ratio.

#### 4. T17 Time-Permuted Signal-Shuffle Null Test (100 Iterations)
- Real Strategy Sharpe: **0.9725**.
- Shuffled Signal Mean Sharpe: **-2.4404** (Standard Deviation: 0.147, Min: -2.858, Max: -2.122).
- Statistical Significance: Real strategy sits **> 23 standard deviations above the null distribution** ($z = 23.2, p < 10^{-50}$). With shuffled signals, transaction friction erodes capital rapidly.

### Independently reproduced

Not independently reproduced. All figures reflect third-party empirical backtests and live forward tracking reported by Lucas Joly.

### Negative evidence

- **Catastrophic Standalone Drawdowns:** Every single standalone alpha sleeve exhibits severe standalone drawdowns: EWMAC 53.6%, Skew 47.8%, VoV 43.8%, Carry 40.1%. Standalone deployment is commercially hazardous without multi-sleeve diversification.
- **Extreme Sensitivity to VoV Direction Conditioning:** Ablation variant `R_NO_VOVDIR` (removing the 64-day trend direction sign from the VoV sleeve) causes full-sample Sharpe to collapse by **-0.239**, the largest performance drop in the entire 70-variant ablation matrix. Standalone VoV without directional conditioning has near-zero predictive power.
- **Decade Degradation in the 2020s:** Strategy Sharpe declined from 1.19 (2010s) to 0.74 (2020s) and +0.44 in early 2026 paper trading, reflecting the macro regime shift toward higher interest rates, heightened geopolitical shocks, and rapid trend reversals in commodity complexes.
- **Severe Negative Results Across Classical Technical & Microstructure Factors:** The source's 45-alpha library revealed that many widely touted technical trading strategies produced catastrophic negative Sharpe ratios across the 1990-2026 futures panel:
  - Amihud Illiquidity: Sharpe **-0.79**, Max DD 98.1%
  - Tail Asymmetry: Sharpe **-0.69**, Max DD 97.2%
  - Intraday Momentum: Sharpe **-0.66**, Max DD 98.0%
  - Dispersion Timing: Sharpe **-0.64**, Max DD 99.3%
  - Overnight Momentum: Sharpe **-0.58**, Max DD 97.8%
  - Fast Mean Reversion: Sharpe **-0.54**, Max DD 99.6%
  - Volume Momentum: Sharpe **-0.40**, Max DD 80.5%
  - Open Interest Momentum: Sharpe **-0.31**, Max DD 65.5%
  - Value: Sharpe **-0.26**, Max DD 85.3%
  - Range Compression: Sharpe **-0.18**, Max DD 74.4%

## Falsification plan

1. **Walk-Forward Horizon Out-of-Sample Forward Tracking:**
   - Track live performance through December 2027 on liquid futures and crypto perpetuals.
   - `research-defined falsification threshold`: If the rolling 24-month out-of-sample Sharpe ratio drops below 0.35, or if realized maximum drawdown exceeds 25.0% under nominal 20% volatility targeting, reject the multi-alpha stability hypothesis.
2. **Sleeve Orthogonality Breakdown Audit:**
   - Monitor the rolling 256-day pairwise correlation matrix among Trend, Carry, Skew, and VoV.
   - `research-defined falsification threshold`: If the average pairwise correlation among the four sleeves exceeds 0.40 over any continuous 6-month window, reject the structural orthogonality hypothesis.
3. **FDM Cap Binding & Diversification Collapse Test:**
   - Stress-test the universe-pooled FDM under simulated liquidity crises (e.g., March 2020, October 2025).
   - `research-defined falsification threshold`: If the dynamic FDM fails to contract toward 1.0 during correlated market drawdowns, causing realized portfolio volatility to spike above 30%, falsify the FDM risk-dampening mechanism.
4. **Execution Friction & Transaction Cost Stress Test:**
   - Sweep round-turn execution costs from 1.0x to 3.0x baseline fees and apply 5 bps execution slippage.
   - `research-defined falsification threshold`: If net annualized Sharpe drops below 0.50 under 2.0x cost multiplier, reject the commercial feasibility of the daily buffered rebalancing model.
5. **Ablation of Soft Logistic Overlays:**
   - Run the portfolio across historical bear regimes with `use_overlays = False`.
   - `research-defined falsification threshold`: If the overlay-free variant achieves equal or lower maximum drawdown than the soft logistic gated model, falsify the derived steepness ($k = 10.0$) risk-gate thesis.

## Crypto portability

- **Portability Status:** Adapted / Unproven.
- **Primary Source Asset Class:** Multi-asset traditional linear futures (commodities, equity indices, sovereign bonds, STIR, FX, VIX).
- **Crypto-Specific Adaptation Requirements:**
  1. *Trend Sleeve (EWMAC 3-Speed + XS):* Ports directly to liquid crypto perpetuals (e.g., top 30 Binance/Hyperliquid perpetuals). The 3-speed configuration $(16, 64)$, $(32, 128)$, $(64, 256)$ is timescale-invariant, though high crypto volatility will naturally reduce nominal contract position sizes.
  2. *Carry Sleeve (Basis vs. Funding Rate):* In traditional futures, carry is calendar roll yield ($P_{\text{front}} - P_{\text{next}}$). In crypto perpetuals, calendar contracts are illiquid; the carry sleeve must be adapted to **perpetual funding rate carry** (harvesting negative funding on longs or positive funding on shorts) or spot-perpetual basis convergence.
  3. *Skewness Sleeve:* Ports directly using 256-day rolling price returns of crypto perpetuals. Given crypto's fat-tailed downside jumps (liquidation cascades), the crash-risk premium should theoretically be pronounced, but short-side exposure carries severe squeeze risk.
  4. *Vol-of-Vol Sleeve with Trend Direction:* Ports directly using daily realized volatility. The direction overlay ($64$-day return sign) is critical to prevent buying into collapsing altcoins during low-volatility bear grinds.
  5. *Execution Frictions & 24/7 Clock:* Traditional futures close daily; crypto trades 24/7. Daily rebalancing must be pinned to 00:00:00 UTC. Taker fees (2-5 bps on institutional tiers) and funding rate drags will alter net sleeve profitability.

## Limitations

- **Proprietary Data Panel:** The underlying continuous futures price panel (NorgateData Panama-adjusted) is private and not committed to the repository, precluding push-button external re-execution without vendor data.
- **Traditional Asset Focus:** Source backtest is conducted entirely on traditional futures contracts; empirical validity in cryptocurrency perpetuals remains unproven.
- **Model Simplification Assumptions:** Assumes fills at daily open/close without intra-bar slippage or market impact modeling for large trade sizes ($> \$50\text{M}$ AUM).
- **Macro Regime Sensitivity:** S183 shows noticeable performance moderation post-2020 (Sharpe 0.74 vs 1.19 in 2010s) and underperformed CTA peers in early 2026 paper trading due to agricultural trend reversals.
- **Carry Sleeve Translation Gap:** Converting futures calendar roll yield to crypto perpetual funding rate is a structural modification whose tracking error has not been evaluated in this source.

## Implementation status

Not implemented. Research capture only. No implementation in NautilusTrader, PyBroker, or live production.

## Adoption boundary

This record is research material only. It does not constitute:
- Trading authorization;
- Validated alpha approval;
- Permission for paper trading, testnet execution, or live capital allocation.

## Related Wiki records

- [[quant/alpha-combination-breadth-executable-bridge-2026-08-28]] — Formal framework for multi-alpha breadth, portfolio combination, and execution bridges.
- [[quant/alpha-transforms-decay-neutralization-2026-08-28]] — Alpha scaling, rolling forecast normalization, and cross-sectional rank transforms.
- [[quant/backtest-overfitting-pbo-cscv-2026-08-27]] — Probability of backtest overfitting, Deflated Sharpe Ratio, and multiple testing adjustments (Harvey & Liu).
- [[quant/continuous-cash-overlay-growth-defensive-slow-tail-vshape-max-cash-2026-09-03]] — Non-linear risk overlay architectures and drawdown-gating mechanisms.

## Sources

1. Lucas Joly, *"Trends Research — Systematic Momentum in Global Futures: A Master's-thesis research programme on serial autocorrelation and trend-persistence in linear derivatives"*, MSc 2 Mémoire, INSEEC (Advisor: Georges Lionel), 2026. GitHub repository: `https://github.com/Lucas-Joly-GH/trends-research` (Commit SHA: `4fb581c9866b031a55ad5e4cb14a684e0e60c10d`).
2. Robert Carver, *Systematic Trading: A unique new method for designing trading and investing systems*, Harriman House, 2015; and *Advanced Futures Trading Strategies*, 2023.
3. Corey Levine and Lasse Heje Pedersen, *"Which Trend Is Your Friend?"*, Financial Analysts Journal 72(3), 2016.
4. Tobias J. Moskowitz, Yao Hua Ooi, and Lasse Heje Pedersen, *"Time series momentum"*, Journal of Financial Economics 104(2), 2012.
5. Guido Baltussen, Sjoerd van Bekkum, and Bart van der Grient, *"Vol-of-Vol and the Cross-Section of Stock Returns"*, Journal of Financial and Quantitative Analysis, 2018.
6. Campbell R. Harvey and Yan Liu, *"Evaluating Trading Strategies: A New Multiple Testing Approach"*, Journal of Financial Economics, 2020.
