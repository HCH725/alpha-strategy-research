---
schema: strategy-research-record-v1
title: "Cross-Sectional Crypto Residual Momentum with Rolling Market-Beta Neutralization"
created: 2026-09-11
updated: 2026-09-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional-momentum
  - residual-momentum
  - market-neutral
  - execution-cost-aware
  - out-of-sample-validated
status: research-only
confidence: medium
source_as_of: 2026-08-24
sources:
  - "https://github.com/FionaNi-DS/crypto-residual-momentum"
  - "https://github.com/FionaNi-DS/crypto-residual-momentum/blob/2c5cfd216d63c0c0546ed7f26e538bb5b89b9edd/01_data.ipynb"
  - "https://github.com/FionaNi-DS/crypto-residual-momentum/blob/2c5cfd216d63c0c0546ed7f26e538bb5b89b9edd/02_signal_search.ipynb"
  - "https://github.com/FionaNi-DS/crypto-residual-momentum/blob/2c5cfd216d63c0c0546ed7f26e538bb5b89b9edd/03_portfolio_construction.ipynb"
  - "https://github.com/FionaNi-DS/crypto-residual-momentum/blob/2c5cfd216d63c0c0546ed7f26e538bb5b89b9edd/04_out_of_sample.ipynb"
  - "https://github.com/FionaNi-DS/crypto-residual-momentum/blob/2c5cfd216d63c0c0546ed7f26e538bb5b89b9edd/05_validation.ipynb"
  - "https://github.com/FionaNi-DS/crypto-residual-momentum/blob/2c5cfd216d63c0c0546ed7f26e538bb5b89b9edd/net_return_oos.csv"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Sectional Crypto Residual Momentum with Rolling Market-Beta Neutralization

## Provenance

- **Repository:** https://github.com/FionaNi-DS/crypto-residual-momentum
- **Full Commit SHA:** `2c5cfd216d63c0c0546ed7f26e538bb5b89b9edd` (committed 2026-08-24T15:00:27Z by FionaNi)
- **Relevant Files:**
  - `README.md` — Project overview, methodology summary, headline development vs out-of-sample metrics, and HAC validation results
  - `01_data.ipynb` — Data loading (`crypto_hourly_clean_2020_2025.csv`), distribution summary statistics, pairwise hourly return correlations (~0.63 mean)
  - `02_signal_search.ipynb` — Equal-weight crypto market factor calculation, 30-day (720-hour) rolling OLS beta estimation, residual return extraction, 12-combination IC grid search
  - `03_portfolio_construction.ipynb` — Long 2 / Short 2 portfolio construction, data coverage sensitivity (fixing gap with 95% minimum observation threshold), turnover tracking, 7 bps transaction cost model, development backtest (2020–2023)
  - `04_out_of_sample.ipynb` — Parameter freeze, out-of-sample evaluation on untouched 2024–2025 hourly data, net return export, Newey-West t-statistic
  - `05_validation.ipynb` — Development vs OOS comparison, year-by-year Sharpe analysis, Newey-West HAC statistical significance test on `net_return_oos.csv`
  - `net_return_oos.csv` — Full 105-observation weekly net strategy return time-series for 2024–2025 OOS
- **Data Source:** Cleaned hourly cryptocurrency spot market data from Binance (`crypto_hourly_clean_2020_2025.csv`), covering 2020-01-01 00:00:00+00:00 through 2025-12-31 23:00:00+00:00 (52,577 hourly bars per asset, 420,616 total rows).
- **Source Quality:** Public GitHub research repository with complete, executed Jupyter notebooks containing code, intermediate data prints, outputs, and validation tables. The full raw CSV is omitted due to size, but full execution logs, exact parameters, and the OOS net return series (`net_return_oos.csv`) are provided.

## Economic mechanism

### Source-reported

Cryptocurrencies exhibit strong common co-movement: the author reports average pairwise hourly return correlation of approximately 0.63 in development data, and individual asset correlations with the equal-weighted crypto market return range from 0.663 (DOGE) to 0.894 (ETH). Because of this high market exposure, conventional total-return momentum in crypto tends to reflect broad market beta rather than idiosyncratic relative strength.

The source proposes removing the common market component via a rolling market beta:
$$r_{i,t} = \alpha_i + \beta_{i,t} r_{m,t} + \epsilon_{i,t}$$
where $r_{i,t}$ is the hourly return of asset $i$, $r_{m,t}$ is the equal-weight market return across the 8 tokens, and $\beta_{i,t}$ is estimated over a 30-day (720-hour) rolling window. After residualization, individual asset correlations with the market factor collapse from 0.663–0.894 down to -0.038 to +0.047. The author hypothesizes that accumulating residual returns ($\epsilon_{i,t}$) isolates token-specific momentum that persists over subsequent multi-day horizons.

### Research interpretation

This strategy adapts the equity residual momentum literature (e.g., Blitz, Pang, and van Vliet, 2011) to cryptocurrency markets. In total-return momentum, strategies suffer from severe momentum crashes when market regimes suddenly pivot, because winners are loaded on high-beta assets during bull markets and low-beta assets during bear markets.

By orthogonalizing asset returns against the cross-sectional mean return:
1. **Beta neutralization:** The rolling OLS regression removes contemporaneous market-wide sentiment and liquidity tides.
2. **Idiosyncratic trend persistence:** Token-specific alpha drivers (such as project upgrades, ecosystem adoption, tokenomic changes, or retail attention) manifest in the residual series $\epsilon_{i,t}$ with less macro market noise.
3. **Relative-value dollar-neutrality:** Longing the top 2 residual performers and shorting the bottom 2 residual performers constructs a dollar-neutral long/short book ($+0.50$ long, $-0.50$ short), substantially attenuating directional crypto beta.

## Signal

- **Signal formation timestamp:** Evaluated every 168 hours (7 days / weekly) at the close of hourly candle $t$. First development rebalance occurs at `2020-02-12 01:00:00+00:00`; first OOS rebalance occurs at `2024-01-01 00:00:00+00:00`.
- **Market factor:** Equal-weighted average of hourly returns across all available universe assets at hour $t$:
  $$r_{m,t} = \frac{1}{N} \sum_{i=1}^N r_{i,t}$$
- **Rolling market beta estimation:**
  $$\beta_{i,t} = \frac{\text{Cov}_{W_\beta}(r_{i}, r_m)}{\text{Var}_{W_\beta}(r_m)}$$
  - Beta window: $W_\beta = 720$ hours (30 days).
  - Minimum coverage threshold: 95% of window ($W_\beta \times 0.95 = 684$ valid hourly observations required).
- **Hourly residual return:**
  $$\epsilon_{i,t} = r_{i,t} - \beta_{i,t} \cdot r_{m,t}$$
- **Cumulative residual momentum signal:**
  $$S_{i,t} = \sum_{k=0}^{W_{\text{sig}}-1} \epsilon_{i,t-k}$$
  - Formation window: $W_{\text{sig}} = 336$ hours (14 days).
  - Minimum coverage threshold: 95% of window ($W_{\text{sig}} \times 0.95 = 319$ valid hourly observations required).
- **Cross-sectional ranking & portfolio weights:**
  - Rank all $N=8$ assets by $S_{i,t}$ in descending order.
  - Top 2 assets (highest residual momentum): weight $w_{i,t} = +0.25$ each ($+0.50$ gross long).
  - Bottom 2 assets (lowest residual momentum): weight $w_{i,t} = -0.25$ each ($-0.50$ gross short).
  - Middle 4 assets: weight $w_{i,t} = 0.0$.
  - Gross portfolio leverage: $1.0$ (100%). Net dollar exposure: $0.0$.
- **Execution & holding period:**
  - Positions are held for $H = 168$ hours (7 days / weekly).
  - Trades execute on the next bar following signal calculation, holding for $t+1 \dots t+168$ (`future_168 = rolling(168).shift(-168)`).
- **Parameters:**
  - $W_\beta = 720$ hours (source-fixed).
  - $W_{\text{sig}} = 336$ hours (selected from development grid search over $[24, 72, 168, 336]$ hours based on Spearman IC).
  - $H = 168$ hours (selected from development grid search over $[24, 72, 168]$ hours based on Spearman IC).
  - $N_{\text{long}} = 2, N_{\text{short}} = 2$ (source-fixed portfolio breadth).
  - Coverage ratio = 0.95 (source-calibrated to prevent data gaps from discarding rebalance periods).

## Required data

- **Instrument:** Spot crypto assets paired against USDT (ADAUSDT, BNBUSDT, BTCUSDT, DOGEUSDT, ETHUSDT, LINKUSDT, LTCUSDT, XRPUSDT).
- **Universe:** 8 large-cap cryptocurrencies available continuously across the 2020–2025 window. (Static universe, survivor-biased).
- **Venue:** Binance Spot (`crypto_hourly_clean_2020_2025.csv`).
- **Timeframe:** 1-hour candles.
- **Fields:** `open_time`, `open`, `high`, `low`, `close`, `volume`, `ret_1h = close / open - 1`.
- **Timestamp:** UTC hourly timestamps.
- **Missing-data handling:** A 95% observation threshold is enforced for both rolling beta and rolling signal windows. Missing hours below the 5% tolerance are dropped; if missing hours exceed 5%, no signal is formed for that asset. No imputation is used.

## Execution assumptions

- **Rebalance cadence:** Exactly every 168 hours (7 calendar days).
- **Order timing / fill model:** Evaluated using compounded hourly returns starting at $t+1$ (`shift(-168)` relative to signal at $t$). The model assumes fill at bar close/open without explicit intraday execution delay (`research-proposed fill model`: next-bar open market orders).
- **Transaction costs:** 7 bps (0.07%) per unit of portfolio turnover (`cost_bps = 7`, deduction = $\text{turnover} \times 0.0007$). Turnover is defined as $\sum_{i} |w_{i,t} - w_{i,t-1}|$. (Source-specified cost model).
- **Slippage / market impact:** Not explicitly modeled separately from the 7 bps flat turnover fee. For large-cap tokens (BTC, ETH, BNB), 7 bps is comparable to VIP/taker fee levels, but on thinner assets or higher AUM it is an optimistic lower bound (`research-proposed execution caveat`).
- **Borrow / shorting costs:** The backtest assumes zero borrow fee on the short leg and unconstrained short capacity on Binance spot. In real spot execution, borrowing crypto incurs hourly interest (5%–20%+ APR), or requires executing via perpetual futures (`research-proposed operational requirement`: margin borrow or perpetual futures execution required).
- **Funding payments:** Zero funding payment modeled (since evaluated on spot prices). If executed on perpetual swaps, funding payments would apply.

## Evidence

### Source-reported

All figures below are taken directly from the executed Jupyter notebooks in `FionaNi-DS/crypto-residual-momentum` (commit `2c5cfd216d63c0c0546ed7f26e538bb5b89b9edd`):

#### 1. Cross-Sectional Information Coefficient (IC) Grid (Development Period 2020–2023, Notebook `02_signal_search.ipynb`)

Spearman rank correlation between residual momentum signals and subsequent forward returns:

| Formation Window ($W_{\text{sig}}$) | Target Horizon ($H$) | Mean IC | IC Std | Positive IC % | Number of Observations |
|:---|:---|:---|:---|:---|:---|
| 24h (1d) | 24h (1d) | -0.0034 | 0.4063 | 48.50% | 25,524 |
| 24h (1d) | 72h (3d) | -0.0002 | 0.4050 | 49.11% | 25,044 |
| 24h (1d) | 168h (7d) | +0.0113 | 0.4055 | 50.50% | 24,084 |
| 72h (3d) | 24h (1d) | -0.0119 | 0.4090 | 48.18% | 25,044 |
| 72h (3d) | 72h (3d) | -0.0044 | 0.3976 | 48.79% | 24,564 |
| 72h (3d) | 168h (7d) | +0.0031 | 0.3912 | 48.69% | 23,624 |
| 168h (7d) | 24h (1d) | +0.0017 | 0.4121 | 49.24% | 24,084 |
| 168h (7d) | 72h (3d) | +0.0048 | 0.4061 | 49.79% | 23,624 |
| 168h (7d) | 168h (7d) | -0.0027 | 0.3979 | 49.21% | 22,760 |
| 336h (14d) | 24h (1d) | -0.0044 | 0.4044 | 48.46% | 22,544 |
| 336h (14d) | 72h (3d) | +0.0125 | 0.3988 | 50.46% | 22,160 |
| **336h (14d)** | **168h (7d)** | **+0.0212** | **0.3983** | **51.54%** | **21,556** |

The 336h formation / 168h target combination yielded the highest mean IC (+0.0212) and positive IC percentage (51.54%) in the development sample and was selected as the locked specification.

#### 2. Development Performance (2020–2023, 203 Rebalance Periods, Notebook `03_portfolio_construction.ipynb`)

- **Gross performance:**
  - Annualised Return: 44.14% (0.4414)
  - Annualised Volatility: 38.01% (0.3801)
  - Gross Sharpe Ratio: 1.1614
  - Maximum Drawdown: -22.34% (-0.2234)
- **Turnover:**
  - Mean turnover per rebalance: 1.0197 (101.97%)
  - Median turnover: 1.0000
  - Average transaction cost per rebalance at 7 bps: 0.000714 (0.0714%)
- **Net performance (after 7 bps transaction costs):**
  - Net Annualised Return: 40.42% (0.4042)
  - Net Annualised Volatility: 38.01% (0.3801)
  - Net Sharpe Ratio: 1.0635
  - Net Maximum Drawdown: -23.91% (-0.2391)
  - Mean weekly net return: 0.007752 (0.7752%)
  - Newey-West HAC t-statistic (maxlags=7): $t = 1.9562$, $p = 0.0504$
- **Development Year-by-Year Net Performance:**
  - 2020: 47 periods, Annual Return 35.68%, Volatility 29.41%, Sharpe 1.2130, Max Drawdown -15.03%
  - 2021: 52 periods, Annual Return 107.82%, Volatility 58.10%, Sharpe 1.8557, Max Drawdown -17.38%
  - 2022: 52 periods, Annual Return 19.42%, Volatility 28.55%, Sharpe 0.6801, Max Drawdown -11.63%
  - 2023: 52 periods, Annual Return -1.69%, Volatility 24.85%, Sharpe -0.0679, Max Drawdown -23.91%
- **Equal-weight crypto benchmark (2020–2023, 188 periods):**
  - Annual Return: 110.08%, Volatility: 94.29%, Sharpe: 1.1675, Max Drawdown: -74.45%

#### 3. Untouched Out-of-Sample Performance (2024–2025, 105 Rebalance Periods, Notebooks `04_out_of_sample.ipynb` & `05_validation.ipynb`)

Parameters locked prior to evaluation; no OOS re-tuning:

| Metric | Development (2020–2023) | Out-of-Sample (2024–2025) | Delta |
|:---|:---:|:---:|:---:|
| Annualised Return | 40.42% | **41.55%** (README: 41.6%) | +1.13% |
| Annualised Volatility | 38.01% | **28.95%** (README: 29.0%) | -9.06% |
| Net Sharpe Ratio | 1.0635 | **1.4352** (README: 1.44) | +0.3717 |
| Maximum Drawdown | -23.91% | **-19.91%** (README: -19.9%) | +4.00% |
| Mean Weekly Net Return | 0.7752% | **0.7968%** | +0.0216% |
| Average Turnover | 1.0197 | **1.0524** | +0.0327 |
| Average Cost per Rebalance | 0.0714% | **0.0737%** | +0.0023% |
| Newey-West HAC t-stat | 1.9562 ($p=0.0504$) | **1.9019** ($p=0.0572$) | - |

- **OOS Year-by-Year Net Performance:**
  - 2024: 53 periods, Annual Return 60.86%, Volatility 34.30%, Sharpe 1.7744, Max Drawdown -19.91%
  - 2025: 52 periods, Annual Return 21.87%, Volatility 22.24%, Sharpe 0.9834, Max Drawdown -16.18%

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Statistical significance threshold failure:** The author explicitly highlights that under Newey-West / HAC standard errors (maxlags=1), the OOS t-statistic is 1.9019 with a two-sided $p$-value of 0.0572. This fails the conventional 5% significance cutoff ($p < 0.05$). In the development sample, $t = 1.9562$ ($p = 0.0504$), also failing 5%.
- **Severe regime instability in 2023:** In 2023, the strategy lost money (-1.69% annual return) with a negative Sharpe ratio (-0.0679) and suffered its deepest development drawdown (-23.91%). Residual momentum is therefore not regime-invariant and experienced a complete year-long drawdown during the 2023 range-bound/choppy market.
- **Year-by-year IC instability:** In `02_signal_search.ipynb`, yearly IC for the 336h/168h combination was +0.1807 in 2020, but flipped negative in 2021 (-0.0615) and was flat in 2023 (-0.0017).
- **Failure of short-horizon residual reversal:** Candidate B (72h formation / 24h holding residual reversal) collapsed completely: annual return -54.30%, Sharpe -1.1303, maximum drawdown -68.4%.
- **Contrasting literature on raw momentum:** External studies on crypto cross-sectional momentum (e.g., Grobys et al., 2026; `modern27/momentum-after-costs`; `Animalsciao/crypto-cross-sectional-momentum`) document that total-return crypto momentum produces negative or zero excess returns after realistic transaction costs on wider universes.

## Falsification plan

1. **Universe expansion and survivorship audit:** Test whether the residual momentum alpha survives when expanding the universe from 8 static survivor assets to a dynamic rolling top-30 universe including delisted or fallen tokens (e.g., LUNA, FTT, SRM).
   - *Falsification threshold (`research-defined falsification threshold`):* Strategy net Sharpe drops below 0.50 or maximum drawdown exceeds 35% on the survivorship-bias-free dynamic universe.
2. **Borrow fee / funding rate carry stress test:** Incorporate realistic short-side financing costs (Binance margin borrow rates of 8%–15% APR on short positions, or 8-hour perpetual funding payments).
   - *Falsification threshold (`research-defined falsification threshold`):* Net annual return drops below 10% or net Sharpe drops below 0.60 after financing costs.
3. **Transaction cost and slippage sensitivity:** Re-evaluate net performance under 15 bps and 25 bps cost per unit turnover (representing retail taker fees of 0.05%–0.08% per side plus 0.02%–0.05% slippage).
   - *Falsification threshold (`research-defined falsification threshold`):* Net Sharpe ratio falls below 0.60 at 15 bps or turns negative at 25 bps.
4. **Market factor specification placebo test:** Replace the 8-token equal-weight market return with BTC hourly return ($r_{\text{BTC},t}$) or an external capitalization-weighted index.
   - *Falsification threshold (`research-defined falsification threshold`):* OOS Spearman IC drops below 0.005 or t-statistic drops below 1.0.
5. **Rebalance timing and execution delay jitter:** Perturb the weekly rebalance execution time by +1 hour, +6 hours, and +12 hours to test vulnerability to bar-boundary execution timing.
   - *Falsification threshold (`research-defined falsification threshold`):* Sharpe ratio degrades by more than 40% under arbitrary intraday rebalancing phase shifts.

## Crypto portability

**Direct** for crypto spot with margin trading; **Adapted** for crypto perpetual futures.

Crypto-specific implementation and risk considerations:
- **Spot shorting mechanics:** The source was tested on spot pairs (USDT quote). Shorting on spot requires margin borrowing, collateral allocation, and daily interest payments.
- **Perpetual swap adaptation:** Porting to perpetual futures eliminates spot borrow mechanics but introduces funding rate exposure. If the short leg selects heavily shorted tokens with negative funding rates, the strategy must pay funding every 8 hours, generating funding drag.
- **24/7 market operation:** Weekly rebalances occur continuously without weekend market closes. The 168-hour holding period spans low-liquidity weekend intervals where slippage may widen.
- **Stablecoin counterparty risk:** All quote currency is USDT, assuming parity.

## Limitations

- **Small, survivorship-biased universe:** The universe is restricted to 8 major tokens that survived and remained liquid from 2020 to 2025. This introduces material survivorship bias.
- **Marginal statistical significance:** The out-of-sample Newey-West HAC t-statistic is $t = 1.9019$ ($p = 0.0572$), which does not clear the standard two-tailed 5% significance barrier.
- **High turnover:** Average weekly turnover is ~102%–105% (equivalent to ~5300% annualized turnover), making the strategy sensitive to fee tiers and execution quality.
- **Unmodeled financing costs:** The backtest omits borrow interest for the short leg and perpetual funding carry.
- **Coarse lookback grid:** The 14-day formation / 7-day holding selection was chosen from a small 12-cell grid search; sensitivity to non-integer weekly boundaries remains unexamined.
- **Single exchange data:** Evaluated solely on Binance spot data.

## Implementation status

Not implemented in our research stack (`nautilus-quant-system`, PyBroker, or NautilusTrader). This document is a research capture and specification only.

## Adoption boundary

This record is research material only. The source-reported results have not been independently reproduced. A record being present in this repository does not mean the strategy is profitable, validated, approved for implementation, approved for paper trading, approved for testnet, or approved for live trading.

## Related Wiki records

- `crypto-weekly-momentum-survivor-liquidity-fragility-2026-09-04.md` — Studies survivor bias and liquidity fragility in crypto cross-sectional momentum, finding raw momentum fails on survivor coins.
- `crypto-cross-sectional-momentum-30d-top-quintile-7d-2026-08-31.md` — Baseline cross-sectional momentum formulation on cryptocurrency spot universes.
- `retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11.md` — Microstructure and funding rate falsification methodology for crypto market-neutral signals.

## Sources

1. FionaNi-DS. *Crypto Residual Momentum Strategy*. GitHub repository: https://github.com/FionaNi-DS/crypto-residual-momentum. Full commit SHA: `2c5cfd216d63c0c0546ed7f26e538bb5b89b9edd`. Committed 2026-08-24. Accessed 2026-09-11.
2. Signal research and IC grid: `02_signal_search.ipynb` (same commit). Formations $[24, 72, 168, 336]$ hours, targets $[24, 72, 168]$ hours, 336h/168h selected with mean IC +0.0212 and positive IC % 51.54%.
3. Portfolio construction and development backtest: `03_portfolio_construction.ipynb` (same commit). 95% coverage window fix, 7 bps transaction cost model, development Net Sharpe 1.0635, Max Drawdown -23.91%, Newey-West $t = 1.9562$ ($p = 0.0504$).
4. Out-of-sample backtest: `04_out_of_sample.ipynb` (same commit). Locked parameter evaluation on 2024–2025 data, Net Sharpe 1.4352, Max Drawdown -19.91%, Newey-West $t = 1.9019$ ($p = 0.0572$).
5. Out-of-sample weekly net returns: `net_return_oos.csv` (same commit). 105 weekly return records covering 2024-01-01 to 2025-12-29.
