---
schema: strategy-research-record-v1
title: "Nuclear and Energy Equity Options Variance Risk Premium Harvest: Cash-Secured Systematic Put Writing with GARCH Volatility Filtering and Hard Risk Bounds"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - options
  - variance-risk-premium
  - short-put
  - nuclear-energy
  - garch
  - volatility-harvesting
  - risk-derisking
status: research-only
confidence: high
source_as_of: 2026-09-01
sources:
  - "Jilang Miao and Nonna Sorokina, 'Harvesting the Variance Risk Premium in Nuclear and Energy Equities: A Short-Put Portfolio Derisking Strategy', arXiv:2609.01183v1 [q-fin.PR, q-fin.ST], September 1, 2026. DOI: 10.48550/arXiv.2609.01183. https://arxiv.org/abs/2609.01183"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Nuclear and Energy Equity Options Variance Risk Premium Harvest: Cash-Secured Systematic Put Writing with GARCH Volatility Filtering and Hard Risk Bounds

## Provenance

- **Authors:** Jilang Miao (Pennsylvania State University) and Nonna Sorokina (Pennsylvania State University, `nls5200@psu.edu`)
- **Title:** "Harvesting the Variance Risk Premium in Nuclear and Energy Equities: A Short-Put Portfolio Derisking Strategy"
- **Identifier:** arXiv:2609.01183v1 [q-fin.PR, q-fin.ST]
- **Submission Date:** September 1, 2026 (listed September 2, 2026)
- **DOI:** [10.48550/arXiv.2609.01183](https://doi.org/10.48550/arXiv.2609.01183)
- **Stable URL:** https://arxiv.org/abs/2609.01183
- **Full Text HTML:** https://arxiv.org/html/2609.01183v1
- **License:** Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)
- **Data Universe:** 45 nuclear plant operators (utilities with material nuclear generation shares identified via U.S. Nuclear Regulatory Commission plant-ownership records) and constituents of nuclear-focused ETFs (uranium miners, small modular reactor developers, nuclear service contractors) across 2000–2024 (25 calendar years, 300 monthly periods), sourced from OptionMetrics IvyDB and the CRSP Daily Stock File. 39 tickers with sufficient option history entered the signal and backtest.

## Economic mechanism

### Source-reported

Private capital investment in nuclear energy is constrained by distinctive industry risks: multi-billion-dollar upfront capital requirements, decade-scale construction timelines, complex regulatory licensing, and political controversies. Firms in controversial industries face higher costs of equity (El Ghoul et al., 2011), and private financing remains limited (Weibezahn and Steigerwald, 2024).

Because equity markets continuously price high headline and political tail risk into nuclear-adjacent firms, options markets systematically price implied volatility ($IV$) above realized volatility ($RV$), generating a persistent, harvestable Variance Risk Premium ($VRP$). By systematically writing out-of-the-money cash-secured puts, institutional investors harvest elevated option premia as recurring income. This income offsets downside risk, compressing portfolio volatility and lowering the effective cost of holding nuclear exposure compared to holding raw equity.

### Research interpretation

The strategy is an equity-derivative volatility risk premium harvest combined with cross-sectional risk pooling:
1. **Negative Gamma Risk Premium:** The strategy acts as an unhedged seller of downside crash insurance. Implied volatility reflects the risk-neutral expectation $\mathbb{E}^{\mathbb{Q}}[RV]$ plus a premium for bearing jump/disaster risk, which systematically exceeds the physical expectation $\mathbb{E}^{\mathbb{P}}[RV]$ across single-stock equity options.
2. **Idiosyncratic Risk Diversification:** By distributing cash-secured short put positions across 30 to 43 qualifying names simultaneously (across utilities, miners, engineering contractors, and tech developers), idiosyncratic tail events (e.g., project delays, plant outages) are diversified cross-sectionally.
3. **Asymmetric Payoff Truncation:** Hard exit rules (a 50% take-profit decay and a strict 2.0x stop-loss multiple) truncate the left-tail exposure inherent to naked short put strategies, preventing single-stock catastrophic drawdowns from overwhelming the collected premium.

## Signal

### Formation timestamp & cadence
- Daily close evaluation ($t$).
- Contract selection and trade execution occur at market close on day $t$ (using closing bid/ask mid-prices).
- Timezone: US Eastern Time (ET).

### Lookback & volatility forecasting
- **ATM Implied Volatility ($IV_{\text{ATM}}$):** Calculated on date $t$ as the open-interest-weighted average IV of put options satisfying:
  $$|\delta| \in [0.40, 0.60], \quad \text{DTE} \in [15, 45]$$
- **Realized Volatility Forecast ($\hat{\sigma}_t$):** Estimated using a stationary GARCH(1,1) model on daily log returns $r_t$:
  $$\sigma_t^2 = \omega_i + \alpha \epsilon_{t-1}^2 + \beta \sigma_{t-1}^2$$
  with fixed consensus parameters:
  $$\alpha = 0.09, \quad \beta = 0.90$$
  and a stock-specific long-run variance anchor to prevent volatility collapse during quiet periods:
  $$\omega_i = \overline{r^2}_i (1 - \alpha - \beta)$$
  where $\overline{r^2}_i$ is the unconditional historical sample variance of stock $i$.
- **VRP Metric:** Evaluated as $IV_{\text{ATM}, t} - \hat{\sigma}_{t+21}^{\text{realized}}$, where $\hat{\sigma}_{t+21}^{\text{realized}}$ is the forward 21-day realized volatility.

### Contract selection
On each trading day, for every covered ticker, select the single put option contract that minimizes the distance score to a target of 0.30-delta and 45-day DTE:
$$\text{Score} = (|\delta| - 0.30)^2 + \left(\frac{\text{DTE} - 45}{100}\right)^2$$
subject to strict eligibility filters:
- Days-to-expiration: $\text{DTE} \in [35, 55]$ calendar days.
- Absolute delta: $|\delta| \in [0.20, 0.40]$.
- Minimum liquidity: Open interest $> 10$ contracts.

### Entry rules
1. **Unconditional (Always-On):** For every covered name with an eligible contract, sell one qualifying put contract.
2. **Conditional (GARCH-Filtered Threshold):** Enter only when the ratio of ATM implied volatility to GARCH realized volatility satisfies:
   $$\frac{IV_{\text{ATM}, t}}{\hat{\sigma}_t} \ge \theta$$
   tested at thresholds $\theta = 1.10$ and $\theta = 1.20$. Capital not allocated to qualifying options is held in cash.

### Position sizing & collateral
- 100% Cash-Secured: Notional capital allocated per option equals the put strike price $K$ ($\text{Notional} = K \times 100$).
- Capital is equally weighted across active names ($w_i = 1/N_t$).
- Cap variants:
  - **CAP-10:** Any single ticker is capped at a maximum of 10% of total portfolio capital (requires $\ge 10$ names for full investment).
  - **CAP-20:** Any single ticker is capped at a maximum of 5% of total portfolio capital (requires $\ge 20$ names for full investment).

### Exit rules (whichever triggers first)
1. **Take-Profit:** Premium decays to 50% of entry mid-price:
   $$\text{mid}_t \le 0.50 \times \text{mid}_{\text{entry}}$$
2. **Stop-Loss:** Option mid-price reaches twice the entry premium:
   $$\text{mid}_t \ge 2.00 \times \text{mid}_{\text{entry}}$$
3. **Time Exit / Early Roll:** Days-to-expiration drops to:
   $$\text{DTE} \le 15$$
   (avoiding high-gamma terminal expiration risk).

## Required data

- **Universe:** 45 U.S.-listed equities associated with the nuclear power lifecycle:
  - Nuclear utility operators (NRC-licensed plants): e.g., Constellation Energy (CEG), NextEra Energy (NEE), Southern Company (SO), American Electric Power (AEP), Duke Energy (DUK), Entergy (ETR), NRG Energy (NRG), Mirant (MIR).
  - Uranium miners & fuel cycle: Cameco (CCJ), Uranium Energy Corp (UEC), NexGen Energy (NXE), Energy Fuels (UUUU), Denison Mines (DNN), Lightbridge (LTBR).
  - SMR & reactor technology / engineering: BWX Technologies (BWXT), NuScale Power (SMR), Oklo Inc (OKLO).
  - 39 tickers possess sufficient continuous option chain coverage across the 2000–2024 window.
- **Option Data Source:** OptionMetrics IvyDB (closing best bid, best offer, mid-price, Black-Scholes implied volatility, delta, open interest, strike, expiration).
- **Equity Data Source:** CRSP Daily Stock File (closing prices, total returns adjusted for dividends/splits, daily trading volume, PERMNO identifiers).
- **Identifier Mapping:** OptionMetrics SECID to CRSP PERMNO bridge.

## Execution assumptions

- **Order Timing & Type:** Executed at daily market close using the quoted bid/ask mid-price:
  $$\text{Price}_{\text{entry}} = \frac{\text{Bid}_{\text{entry}} + \text{Ask}_{\text{entry}}}{2}, \quad \text{Price}_{\text{exit}} = \frac{\text{Bid}_{\text{exit}} + \text{Ask}_{\text{exit}}}{2}$$
- **Return Accounting:** Cash-secured trade return defined as:
  $$\text{Return}_{\text{trade}} = \frac{\text{PnL}}{\text{Strike}} = \frac{\text{Price}_{\text{entry}} - \text{Price}_{\text{exit}}}{K}$$
- **Transaction Costs & Slippage:** Omitted in baseline backtests (assumed zero bid-ask spread and zero exchange/clearing fees; noted as a material limitation).
- **Collateral Yield:** Cash collateral earns 0.0% interest (risk-free T-bill yield is excluded, understating total return in high-interest rate environments).
- **Exercise / Assignment:** Early exercise is assumed not to occur because puts are sold out-of-the-money ($0.30\delta$), making early exercise by option holders suboptimal.

## Evidence

### Source-reported

All figures trace directly to Miao and Sorokina (arXiv:2609.01183v1, Sections 3.1–4.4, Figures 1–5, Table 1):

1. **VRP Wedge & Statistical Significance:**
   - Mean $IV/RV$ ratio on entry days: 1.53 (equal-weighted across tickers), 1.44 (pooled across all entry-day observations).
   - Highest $IV/RV$ ratios occur in pure-play SMR and small-cap uranium names: DNN, LTBR, OKLO, UEC.
   - Lowest $IV/RV$ ratios occur in regulated, diversified utilities: SO, AEP, DUK, ETR.
   - 28 of 39 tickers exhibit statistically significant positive $VRP$ ($t > 2.0$ for mean $IV - \text{forward } RV$).
   - Top naive $t$-statistics: NRG ($t = 12.7$), NXE ($t = 12.1$), UUUU ($t = 10.0$), LTBR ($t = 9.4$), MIR ($t = 9.4$), UEC ($t = 8.9$).
   - Overlap-adjusted $t$-statistics (dividing by $\sqrt{21} \approx 4.6$ to account for 21-day overlapping forward windows): NRG ($t \approx 2.8$), NXE ($t \approx 2.6$), UUUU ($t \approx 2.2$).
   - VRP was positive in 19 out of 25 calendar years. The six negative VRP years were 2000, 2002, 2008 (largest deficit at $-6.2$ percentage points), 2011, 2018, and 2024.

2. **Portfolio Backtest Performance (2000–2024, 300 Months):**
   - **Unconditional EW Put Portfolio (64,514 trades):**
     - Annualized Return: **18.7%**
     - Annualized Volatility: **2.4%**
     - Sharpe Ratio: **7.8**
     - Maximum Drawdown: **~0.0%** (zero negative calendar months across the 300-month sample).
     - Overall Win Rate: **88.3%** across all 64,514 trades (annual win rates range from 84.6% in 2008 to 92.7% in 2004).
     - Calendar Year Consistency: Positive returns in **all 25 calendar years**, notably during severe equity bear markets: 2002 (+31%), 2008 (+26%), 2011 (+20%), and 2018 (+12%).
     - Cumulative Growth: \$1.00 invested in January 2000 grew to **\$102.00** by December 2024.
   - **Passive Equal-Weight Stock Benchmark:**
     - Annualized Return: **15.4%**
     - Annualized Volatility: **19.1%**
     - Sharpe Ratio: **0.81**
     - Maximum Drawdown: **47.0%** (2008 calendar return was $-37.0\%$).
     - Cumulative Growth: \$1.00 grew to **\$24.00**.
   - **Conditional GARCH-Filtered Put Portfolio ($\theta = 1.10$, 11,404 trades):**
     - Sharpe Ratio: **2.63**
     - Annualized Volatility: **4.2%**
     - Maximum Drawdown: **7.7%**
     - 2011 Return: **+5.5%**
     - Cumulative Growth: \$1.00 grew to **\$12.00**.
   - **Conditional GARCH-Filtered Put Portfolio ($\theta = 1.20$, 6,693 trades):**
     - Sharpe Ratio: **2.03**
     - Annualized Volatility: **5.3%**
     - Maximum Drawdown: **9.4%**
     - 2011 Return: **-1.2%**
   - **Concentration Caps (CAP-10 vs CAP-20):**
     - CAP-10 and Unconditional EW are virtually identical because the unconditional strategy holds 30–43 tickers per month (allocating 2.3%–3.3% per name, well below the 10% cap).
     - CAP-20 (5% cap) binds during earlier sample years when fewer than 20 names had option coverage, reducing annualized return by 1.4 percentage points.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Execution Cost Sensitivity:** All returns are reported at quoted bid/ask mid-prices. For small-cap, low-liquidity options (e.g., DNN, LTBR, OKLO, UUUU), the quoted bid-ask spread is frequently 10% to 30% of option premium. Crossing half the bid-ask spread on entry and exit would severely compress the 18.7% gross return.
2. **Negative VRP Regimes:** In 6 of the 25 years (2000, 2002, 2008, 2011, 2018, 2024), realized volatility exceeded implied volatility. While the unconditional portfolio remained profitable in those years due to prior high-premium positions expiring profitably, the 1.20 threshold strategy suffered a $-1.2\%$ loss in 2011.
3. **Overnight Gap / Jump Risk:** The stop-loss rule assumes execution at the exact 2.0x mid-price threshold on daily close. In the event of an overnight catastrophic regulatory shock (e.g., Fukushima disaster in March 2011) or unexpected earnings miss, option prices can gap to 5x–10x entry premium at the open, triggering losses far exceeding the modeled stop-loss boundary.
4. **Filtering Paradox:** The conditional GARCH filter ($\theta = 1.10$ and $1.20$) significantly reduced performance (Sharpe dropped from 7.8 to 2.63 and 2.03; MaxDD increased from 0% to 7.7% and 9.4%) because filtering reduced the active trade count from 64,514 to 11,404, concentrating risk in fewer names and destroying cross-sectional diversification.

## Falsification plan

1. **Transaction Cost & Spread Stress Test:** Apply realistic execution bid/ask slippage models:
   $$\text{Fill}_{\text{entry}} = \text{Bid}_{\text{entry}}, \quad \text{Fill}_{\text{exit}} = \text{Ask}_{\text{exit}}$$
   If the net Sharpe ratio drops below 1.5 across the 2000–2024 period, the hypothesis that VRP is commercially harvestable after frictional costs in single-stock energy options is falsified.
2. **Survivorship-Free Point-in-Time Reconstruction:** Re-run the universe selection strictly using point-in-time NRC utility license lists and historical ETF constituent files, restoring all delisted, bankrupt, or acquired nuclear firms (e.g., Westinghouse parent Toshiba, bankrupt utilities). If the Sharpe ratio drops by $>50\%$, the original result was driven by survivorship selection bias.
3. **Overnight Jump Gap Model:** Replace the daily mid-price stop-loss with next-day open execution following gap moves ($|r_{\text{open}} - r_{\text{close},-1}| > 3\sigma$). If maximum drawdown exceeds 25%, the stop-loss mechanism is invalid under realistic discontinuous jump conditions.
4. **Cross-Sector Placebo Test:** Apply the exact same contract selection, GARCH filtering, and exit rules to non-energy sectors (e.g., regional banks, biotech, consumer staples). If the performance differential between nuclear equities and other sectors is statistically insignificant ($p > 0.10$), the claim that nuclear equities possess a unique structural VRP premium is rejected.

## Crypto portability

- **Portability Status:** `adapted` / `unproven`.
- **Structural Differences & Risks:**
  - **Contract Architecture:** Traditional equity options have monthly/weekly Friday expirations, physical share delivery, and cash-settled margin in USD. Crypto options (predominantly traded on Deribit, Binance, OKX, Bybit, or on-chain protocols like Aevo/Lyra) feature inverse (coin-margined) or linear (USDC/USDT) settlement, European exercise, and 24/7 continuous trading.
  - **Volatility Dynamics & Vol of Vol:** Crypto assets exhibit substantially higher baseline volatility ($\sim 50\%–100\%$ annualized vs $25\%–40\%$ for nuclear equities) and extreme jump clustering. Selling $0.30\delta$ puts naked or cash-secured during crypto deleveraging cascades (e.g., May 2021, November 2022) produces severe tail drawdowns that can easily breach a 2x stop loss before execution is possible.
  - **Sector Equivalent:** There is no direct single-token nuclear equivalent in crypto. An adapted mechanism would target crypto infrastructure tokens (e.g., proof-of-work mining equities like MARA, CLSK, RIOT, or Layer-1 staking native tokens) where implied volatility on Deribit or CME futures options trades at an elevated premium relative to GARCH-forecasted realized volatility.
  - **Execution Feasibility:** Crypto option order books for altcoins have thin liquidity and wide spreads, limiting feasible execution to BTC and ETH options.

## Limitations

1. **Mid-Price Execution:** The paper assumes zero bid-ask spread costs on entry and exit, artificially flattering win rates and returns.
2. **Survivorship Bias:** Tickers were selected based on 2024 NRC operating records and current ETF holdings, excluding historical operators that went bankrupt or were dissolved.
3. **Omission of Risk-Free Yield:** Cash collateral earned 0% interest in the study. While this makes the gross return conservative relative to a modern 5% T-bill regime, it distorts Sharpe ratio comparisons against risk-free baselines.
4. **Fixed GARCH Parameters:** Parameters $\alpha = 0.09, \beta = 0.90$ were hardcoded from consensus values rather than fitted via out-of-sample MLE per asset.
5. **No Independent Replication:** Results rely exclusively on the reported backtest in arXiv:2609.01183v1.

## Implementation status

- `not-implemented` in our research stack.
- No PyBroker, NautilusTrader, paper trading, testnet, or live trading implementation has been conducted.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`
- This document captures normalized research findings from public academic literature. It does not constitute investment advice, an operational trading algorithm, or authorization for capital deployment.

## Related Wiki records

- `[[quant/spxw-0dte-vrp-learning-to-rank-2026-09-01]]`
- `[[quant/crypto-options-volatility-risk-premium-zscore-2026-08-31]]`
- `[[quant/option-implied-surface-cremers-weinbaum-skew-crash-regimes-2026-09-02]]`

## Sources

1. Jilang Miao and Nonna Sorokina, *"Harvesting the Variance Risk Premium in Nuclear and Energy Equities: A Short-Put Portfolio Derisking Strategy"*, arXiv preprint `arXiv:2609.01183v1 [q-fin.PR, q-fin.ST]`, submitted September 1, 2026, listed September 2, 2026. DOI: [10.48550/arXiv.2609.01183](https://doi.org/10.48550/arXiv.2609.01183). Full text: [https://arxiv.org/html/2609.01183v1](https://arxiv.org/html/2609.01183v1).
