---
schema: strategy-research-record-v1
title: "The Bounce Has No Direction: Fourier-Residue Identity and Microstructure Return Autocorrelation Decomposition"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - market-microstructure
  - return-autocorrelation
  - variance-ratio
  - fejer-identity
  - fourier-residue-identity
  - bid-ask-bounce
  - nonsynchronous-trading
  - partial-price-adjustment
  - negative-evidence
  - equity-etf
status: research-only
confidence: high
source_as_of: 2026-06-19
sources:
  - "Victoria Portnaya, 'The Bounce Has No Direction: Sign, Magnitude, and the Microstructure of Equity Return Predictability: Fourier-Residue Identities, Fejér Sums, and Evidence from US Equity and Cross-Asset Markets, 1993–2026', arXiv:2606.29591v1 [q-fin.ST], June 2026. https://arxiv.org/abs/2606.29591"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# The Bounce Has No Direction: Fourier-Residue Identity and Microstructure Return Autocorrelation Decomposition

## Provenance

- **Primary Source:** Victoria Portnaya (Kyiv School of Economics, contact: `vportnaia@kse.org.ua`), *"The Bounce Has No Direction: Sign, Magnitude, and the Microstructure of Equity Return Predictability: Fourier-Residue Identities, Fejér Sums, and Evidence from US Equity and Cross-Asset Markets, 1993–2026"*, arXiv preprint `arXiv:2606.29591v1 [q-fin.ST]`, published June 2026.
- **Stable URLs:**
  - Abstract: [https://arxiv.org/abs/2606.29591](https://arxiv.org/abs/2606.29591)
  - Full Text HTML: [https://arxiv.org/html/2606.29591v1](https://arxiv.org/html/2606.29591v1)
  - PDF: [https://arxiv.org/pdf/2606.29591v1](https://arxiv.org/pdf/2606.29591v1)
- **Primary Data Window:** Daily log returns from 1993-01-01 to 2026-06-19 ($N=8{,}403$ daily observations for SPY).
- **Underlying Data Engine:** Daily split- and dividend-adjusted closing prices via Yahoo Finance (`yfinance` package, `auto_adjust=True`).
- **Pre-Write Deduplication Audit:** Comprehensive repository-wide full-text search confirmed zero prior records referencing `arXiv:2606.29591`, "Fourier-Residue Identity", "Fejér sum", or Victoria Portnaya's autocorrelation decomposition. While `conditioning-sign-on-magnitude-return-decomposition-csm-2026-09-04.md` explores monthly macro-predictive regressions conditioning sign on Weibull-MEM magnitude (Brou and Luger, 2026), the present research addresses high-frequency daily/weekly market microstructure, the Roll bid-ask bounce, non-synchronous trading staleness, and the spectral decomposition of variance ratios across equity and crypto panels.

## Economic mechanism

### Source-reported

Broad US equity index ETFs exhibit statistically significant daily return autocorrelation. Specifically, the SPDR S&P 500 ETF (SPY) displays a lag-1 return autocorrelation of $\hat{\rho}(1) = -0.081$ ($z = -7.39$, more than 7 standard errors below zero; $p < 10^{-12}$), and a two-day variance ratio $VR(2) = 0.919$ ($z^* = -3.47, p < 0.001$). 

The conventional variance-ratio (VR) test of Lo and MacKinlay (1988) tests the random-walk null $VR(q) = 1$, where $VR(q) < 1$ indicates net mean reversion. However, the scalar VR test conflates three economically distinct mechanisms:
1. **Bid-Ask Bounce (Roll, 1984; Ho and Stoll, 1981):** Successive transaction prices alternate between bid ($P^* - s$) and ask ($P^* + s$) quotes as buyer-initiated and seller-initiated orders arrive. Under independent order arrival, the transaction price exhibits negative serial covariance $\gamma(1) = -s^2$, even when the true fundamental price $P^*$ follows an exact martingale. Crucially, the Roll bounce operates exclusively through the magnitude channel: a large move tends to be followed by a smaller move (volatility shrinkage), but the next transaction is equally likely to be a buy or a sell ($p_{1,0} \to 0.50$). It provides no directional information.
2. **Non-Synchronous Trading and Constituent Staleness (Scholes and Williams, 1977; Lo and MacKinlay, 1990):** Equity index ETFs represent baskets of constituent equities. When the index closing price is recorded at 16:00 ET, illiquid constituent stocks may not have traded for minutes or hours. Consequently, contemporaneous market-wide information is only partially reflected in the stale constituent quotes, inducing an apparent negative moving-average autocorrelation in the composite index. Like the bounce, non-synchronous staleness is a magnitude effect: it dampens the apparent index move without creating directional continuation or reversal ($p_{1,0} \approx 0.50$).
3. **Partial Price Adjustment and Information Asymmetry (Glosten and Milgrom, 1985; Amihud and Mendelson, 1987):** Market makers update quotes sequentially in response to order flow. If dealers initially underreact or overreact to informed order flow, full price discovery requires multiple trading periods. If adjustment overshoots, prices must reverse direction in subsequent periods. Unlike bounce or constituent staleness, this mechanism contains true directional content: the sign of today's return predicts the sign of tomorrow's return ($p_{m,0} \ne 0.50$).

Portnaya introduces the **Fourier-Residue Identity (FRI)** to formally decouple the directional (sign, $k=2$) channel from the magnitude ($k=4$) channel:
- At lag 1, the FRI sign test on SPY yields $z_{\text{sign}} = -1.59$ ($p = 0.11$, continuation frequency $p_{1,0} \approx 0.496$), proving that lag-1 return autocorrelation is driven entirely by magnitude shrinkage, with zero statistically reliable directional predictability.
- Applying the Roll (1984) spread estimator $\hat{s} = \sigma \sqrt{|\hat{\rho}(1)|}$ to SPY ($\sigma_{\text{daily}} \approx 1\%$) yields an implied half-spread of $\hat{s} \approx 28\text{ bps}$. However, SPY's actual effective half-spread measured from TAQ data is only $1\text{ to }3\text{ bps}$. Thus, the Roll bounce accounts for at most $\approx 7\%$ of SPY's observed autocorrelation; the remaining $\approx 93\%$ is generated by non-synchronous constituent staleness across the 503 S&P 500 stocks.
- At lag 3, the scalar autocorrelation test shows $\hat{\rho}(3) = -0.007$ ($p = 0.50$, indistinguishable from noise), yet the FRI sign test isolates a statistically significant directional reversal ($z_{\text{sign}} = -2.32, p = 0.02, \hat{\rho}_{\text{sign}}(3) \approx -0.02$). This detects a multi-day partial price adjustment channel operating over a 3-day window that is completely masked by magnitude noise in conventional autocorrelation tests.

### Research interpretation

This research yields a critical quantitative falsification of naive mean-reversion trading:
1. **Falsification of 1-Day Contrarian Equity Strategies:** The intuitive strategy of "buying down days and shorting up days" in broad equity ETFs (SPY, IWM, QQQ) has zero statistical warrant at lag 1 ($p = 0.11$). The statistically massive autocorrelation ($z = -7.39$) is an artifact of magnitude compression (bid-ask bounce and index constituent staleness). A trader executing a directional lag-1 contrarian strategy pays double the bid-ask spread and execution slippage while harvesting no directional drift.
2. **Identification of 3-Day Delayed Directional Channel:** The statistically significant lag-3 directional signal ($p = 0.02$) confirms that directional overreaction corrections in equity markets do not occur on the next trading day, but over a multi-day window (lag 3), consistent with institutional order-flow assimilation. However, the expected return edge is small ($\approx \sigma \times 0.02 \approx 2\text{ bps}$ per trade, or $\approx 20\text{ bps}$ annualized pre-cost), making it marginal for standalone alpha after institutional execution frictions ($2\text{ to }5\text{ bps}$).
3. **Negative Evidence in Cryptocurrency:** The cross-asset panel reveals that Bitcoin (BTC) and Ether (ETH) are the purest random walks in the entire 21-instrument panel (no Bonferroni VR rejection, $R_N \approx \sqrt{2} \approx 1.41$). Because cryptocurrencies are single assets (no constituent staleness), trade 24/7 without market closes (no overnight gap staleness), and utilize continuous algorithmic market makers rather than inventory-smoothing specialists, the microstructure mechanisms that create equity mean reversion are physically absent in crypto.

## Signal

### Source-Reported Mathematical Definitions

1. **Log Returns:**
   $$r_t = \log P_t - \log P_{t-1}$$
   where $P_t$ is the dividend- and split-adjusted daily closing price.

2. **Fejér Representation of the Variance Ratio:**
   Portnaya proves (Proposition 2.2) that under second-order stationarity:
   $$VR(q) = \frac{\widehat{\text{Var}}(r_t^q)}{q \widehat{\text{Var}}(r_t)} = 1 + 2 \mathcal{C}_q$$
   where $\mathcal{C}_q$ is the Fejér-kernel weighted autocorrelation sum:
   $$\mathcal{C}_q = \sum_{m=1}^{q-1} \left(1 - \frac{m}{q}\right) \hat{\rho}(m)$$
   The triangular weights $w_m = 1 - m/q$ represent Fejér spectral smoothing at zero frequency.

3. **Fourier-Residue Identity (FRI) Autocorrelation:**
   Let returns be coded as a $k$-ary discrete symbol $s_t \in \{0, \dots, k-1\}$ using the cyclic group $\mathbb{Z}/k\mathbb{Z}$ characters with $\omega = e^{2\pi i / k}$. The $A$-th FRI autocorrelation at lag $m$ is:
   $$\gamma_{A,k}(m) = \frac{1}{n-m} \sum_{t=1}^{n-m} \omega^{A(s_t - s_{t+m})}$$
   
4. **Binary Sign Channel ($k=2$):**
   Coding $s_t = \mathbf{1}[r_t > 0] \in \{0, 1\}$ with $\omega = -1$:
   $$\gamma_{1,2}(m) = p_{m,0} - (1 - p_{m,0}) = 2 p_{m,0} - 1 = \hat{\rho}_{\text{sign}}(m)$$
   where $p_{m,0} = \hat{\Pr}(s_t = s_{t+m})$ is the continuation frequency.
   Test statistic under $H_0: p_{m,0} = 0.50$:
   $$z_{\text{sign}}(m) = (2 p_{m,0} - 1) \sqrt{n-m} \sim \mathcal{N}(0, 1)$$

5. **Magnitude Channel ($k=4$):**
   Returns partitioned at the sample median of $|r_t|$ into four ordered buckets:
   $$s_t \in \{\text{large-down (0)}, \text{small-down (1)}, \text{small-up (2)}, \text{large-up (3)}\}$$
   Evaluated with $\omega = i$ to measure magnitude persistence independent of sign.

6. **Subsample Persistence Diagnostic:**
   $$R_N = \frac{G_{N/2}}{G_N}, \quad G_N = \max_{1 \le m \le M} |\hat{\rho}_N(m)|$$
   - IID noise benchmark: $R_N \xrightarrow{p} \sqrt{2} \approx 1.41$ (sampling noise decays as $N^{-1/2}$).
   - Structural serial dependence: $R_N \xrightarrow{p} 1.00$ (signal does not decay with sample size).

### Operational Strategy Rules

- **Strategy 1: Naive Directional Lag-1 Contrarian [Source-Evaluated / Statistically Rejected]:**
  - Formation: Day $t$ close ($16:00\text{ ET}$).
  - Long trigger: $r_t < 0$.
  - Short trigger: $r_t > 0$.
  - Holding period: 1 trading day ($t+1$ close).
  - Status: Statistically rejected by source ($z_{\text{sign}} = -1.59, p = 0.11$, $p_{1,0} = 0.496$).

- **Strategy 2: Lag-3 Directional Partial-Adjustment Contrarian [Source-Reported Alpha Hypothesis]:**
  - Formation: Day $t$ close ($16:00\text{ ET}$).
  - Signal variable: Return at lag 3 ($r_{t-2}$).
  - Long entry trigger: $r_{t-2} < 0$ (`source-reported` hypothesis; entry execution at day $t$ close or day $t+1$ open is `research-proposed`).
  - Short entry trigger: $r_{t-2} > 0$ (`source-reported` hypothesis; entry execution at day $t$ close or day $t+1$ open is `research-proposed`).
  - Position sizing: Unit weight (`research-proposed`).
  - Exit rule: Close position at day $t+1$ close (1-day holding period, `research-proposed`).
  - Parameter source: Fixed lag $m=3$, derived from empirical FRI sign significance ($z_{\text{sign}} = -2.32, p = 0.02$).

- **Strategy 3: Magnitude-Shrinkage Volatility Overlay [Source-Supported Hypothesis]:**
  - Formation: Day $t$ close.
  - Sizing logic: Since lag-1 autocorrelation is driven purely by magnitude shrinkage ($\hat{\rho}(1) = -0.081, p < 10^{-12}$), sizing should scale inversely with $|r_t|$ (`research-proposed` rule: $w_{t+1} \propto 1 / \max(\sigma_{\text{rolling}}, |r_t|)$).

## Required data

- **Instruments Studied:**
  - Primary equity ETFs: SPY (S&P 500), QQQ (Nasdaq-100), IWM (Russell 2000).
  - Primary single-stock equities: AAPL, MSFT.
  - Commodity benchmark: GLD (SPDR Gold Shares).
  - Extended 21-instrument cross-asset panel:
    - Equities: 10 US sector/style ETFs + 3 international ETFs (including EEM).
    - Fixed Income: TLT (20+ Yr Treasury), IEF (7-10 Yr Treasury), LQD (IG Corporate Bond), HYG (High Yield Bond).
    - Commodities: GLD, SLV (Silver), DBC (Broad Commodity), USO (Crude Oil).
    - Foreign Exchange: UUP (US Dollar Bullish), FXY (Japanese Yen), FXE (Euro Currency Trust).
    - Cryptocurrencies: BTC (Bitcoin), ETH (Ether).
- **Timeframe & Sampling:** Daily log returns computed from split- and dividend-adjusted closing prices (`yfinance` with `auto_adjust=True`). Weekly series sampled on Wednesday close to avoid holiday and day-of-week distortions.
- **Data Points:** $N = 8{,}403$ daily observations for SPY (1993-01-01 to 2026-06-19).
- **Point-in-Time Integrity:** Standard end-of-day closing prices. No forward-looking information used in recursive or subsample estimation.

## Execution assumptions

- **Timing & Latency:** Signal formed at daily market close ($16:00\text{ ET}$). Implementation assumes execution at the closing print via Market-on-Close (MOC) orders or at next-day Market-on-Open (MOO) (`research-proposed`).
- **Transaction Costs & Spread:**
  - SPY institutional round-trip costs: $2\text{ to }5\text{ bps}$ (`source-reported` based on effective spread $1\text{ to }3\text{ bps}$ and modest market impact).
  - Lag-3 directional expected edge: $\approx \sigma \times 0.02 \approx 0.02\%$ per trade ($\approx 20\text{ bps}$ annualized pre-cost for SPY) (`source-reported`).
  - Net profitability verdict: At $2\text{ to }5\text{ bps}$ per round trip, institutional transaction costs consume the majority or entirety of the $2\text{ bps}$ per-trade edge, rendering standalone unhedged execution economically unviable (`source-reported`).
- **Shorting & Borrow:** Standard ETF borrow assumed available for SPY, QQQ, and IWM at general collateral rates (`research-proposed`).

## Evidence

### Source-reported

All figures below are directly extracted from Victoria Portnaya (arXiv:2606.29591v1, June 2026):

1. **Full-Sample Variance Ratios and Statistics (1993–2026, $N=8{,}403$ for SPY):**
   - **SPY (S&P 500 ETF):**
     - Lag-1 autocorrelation: $\hat{\rho}(1) = -0.081, z_\rho = -7.39$ ($p < 10^{-12}$).
     - Two-day variance ratio: $VR(2) = 0.919, z^* = -3.47$ ($p < 0.001$).
     - Multi-horizon VRs: $VR(5) = 0.837$; $VR(20) = 0.742$ (Fejér sum $\mathcal{C}_{20}^{\text{SPY}} = -0.129$); $VR(60) = 0.66$ (quarterly variance 34% below random walk).
     - Bonferroni minimum $p^* = 5.2 \times 10^{-4}$ at $q=2$ (joint rejection at 5%).
   - **IWM (Russell 2000 ETF):**
     - $VR(2) = 0.924, z^* = -3.28$ ($p < 0.005$). Strongest non-synchronous gradient due to 2,000 small-cap constituents.
   - **MSFT (Microsoft Corp.):**
     - $VR(2) = 0.952, z^* = -2.14$ ($p < 0.05$). Rejects random walk via bid-ask bounce without constituent staleness.
   - **AAPL (Apple Inc.):**
     - $VR(2) = 0.979, z^* = -0.91$ ($p > 0.10$). Does not jointly reject random walk across horizons ($VR(20) = 1.022$).
   - **GLD (SPDR Gold Shares):**
     - $VR(2) = 0.991, z^* = -0.38$ ($p > 0.50$). Near-random walk benchmark.

2. **FRI Directional vs. Magnitude Diagnostic for SPY (Table 5):**
   - Lag 1: $z_\rho = -7.39$ ($p < 10^{-12}$) vs. FRI sign test $z_{\text{sign}} = -1.59$ ($p = 0.11$, continuation frequency $p_{1,0} \approx 0.496$). Predictability is 100% magnitude, 0% direction.
   - Lag 2: $z_\rho = -1.14$ ($p = 0.25$) vs. $z_{\text{sign}} = -0.42$ ($p = 0.67$). Both neutral.
   - Lag 3: $z_\rho = -0.67$ ($\hat{\rho}(3) = -0.007, p = 0.50$) vs. FRI sign test $z_{\text{sign}} = -2.32$ ($p = 0.02, \hat{\rho}_{\text{sign}}(3) \approx -0.02$). Clean directional reversal isolated.
   - Lag 4: $z_\rho = +0.81$ ($p = 0.42$) vs. $z_{\text{sign}} = +0.95$ ($p = 0.34$).

3. **Two-Channel Variance Ratios ($VR_2$ Sign vs. $VR_4$ Magnitude, Table 6):**
   - SPY ($q=20$): $VR_2(20) \approx 1.00$, $VR_4(20) \approx 1.00$ (short-horizon bounce/staleness averaged out).
   - IWM ($q=20$): $VR_2(20) = 0.967, VR_4(20) = 0.976$ (constituent staleness persists over weeks).
   - QQQ ($q=20$): $VR_2(20) = 1.185, VR_4(20) = 1.069$ (strong sign momentum in technology names).
   - AAPL ($q=20$): $VR_2(20) = 1.081, VR_4(20) = 0.994$ (pure directional sign momentum, flat magnitude).
   - Long horizon ($q=60$, quarterly):
     - QQQ: $VR_2(60) = 1.74, VR_4(60) = 1.41$ (directional trend dominates magnitude clustering).
     - AAPL: $VR_2(60) = 1.31, VR_4(60) = 1.10$.

4. **Subsample Persistence Diagnostic ($R_N = G_{N/2} / G_N$, Table 7):**
   - Equity indices: SPY decay exponent $\alpha = 0.15$; half-period ratios $R_N \in \{0.82, 1.13, 1.26, 1.30\}$, all well below the IID sampling noise benchmark $\sqrt{2} \approx 1.41$, confirming structural market dependence.
   - Gold: GLD decay exponent $\alpha = 0.56 \approx 0.50$; $R_N = 1.71 > \sqrt{2}$, confirming sampling noise / random walk.

5. **Cross-Asset Panel (21 Instruments Across 7 Classes):**
   - Equities: All 13 equity ETFs show $VR(5) < 1$. Emerging markets (EEM) show strongest reversal ($VR(5) = 0.799, z^* < -3$) due to Asian constituents closing 12–14 hours before 16:00 ET.
   - Fixed Income: Treasuries show mean reversion (TLT $VR(5) = 0.874$; IEF $0.905$) driven by continuous dealer inventory quotes. Corporate credit ETFs (LQD, HYG) are indistinguishable from random walks due to OTC matrix pricing eliminating bounce and staleness.
   - Commodities: GLD, SLV, DBC are near random walks (centralized limit-order futures). USO shows mild momentum ($VR(5) = 1.040$).
   - FX: EUR/USD is a clean random walk; USD (UUP) and JPY (FXY) exhibit weak mean reversion.
   - Cryptocurrencies: BTC and ETH are the cleanest random walks in the entire panel (no Bonferroni rejection, no significant VR deviation, $R_N \approx \sqrt{2}$).

6. **Estimator & Statistical Verification:**
   - 27 unit tests passed.
   - Numerical verification of Fejér identity: $|VR(q) - (1 + 2\mathcal{C}_q)| < 10^{-12}$ on synthetic data; $< 10^{-3}$ on all empirical market series (SPY $q=20$ residual: $3.6 \times 10^{-5}$).
   - Monte Carlo simulation (1,000 replications under GARCH): Homoskedastic $z$ over-rejects at $10\text{ to }12\%$, while heteroskedastic-robust $z^*$ maintains correct $5\%$ nominal size.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Direct Negative Evidence on 1-Day Equity Contrarianism:** The paper definitively refutes the hypothesis that daily down closes in SPY, QQQ, or IWM predict positive subsequent returns. The lag-1 continuation frequency $p_{1,0} = 0.496$ is statistically indistinguishable from a fair coin ($p = 0.11$).
- **Direct Negative Evidence on Cryptocurrency Mean Reversion:** Neither BTC nor ETH exhibits statistically detectable mean reversion at daily or weekly horizons. The absence of constituent staleness, 24/7 continuous trading, and algorithmic order-book market making render crypto prices consistent with the random walk hypothesis.
- **Direct Negative Evidence on OTC Corporate Credit Reversion:** Despite holding illiquid corporate bonds, LQD and HYG do not exhibit daily price mean reversion due to OTC matrix pricing.

## Falsification plan

To falsify or confirm the FRI decomposition and partial-adjustment mechanisms, the following operational tests are defined:

1. **Out-of-Sample Walk-Forward Stability on Post-2026 Equity Data:**
   - Sample: SPY, QQQ, and IWM daily returns from 2026-06-20 onward.
   - Null Hypothesis: Lag-1 FRI sign test remains insignificant ($p > 0.05$), while lag-1 scalar autocorrelation remains negative ($\hat{\rho}(1) < -0.04$).
   - Falsification Rule: If the post-2026 FRI sign test rejects the null with $z_{\text{sign}} < -2.00$ ($p < 0.05$), the hypothesis of pure magnitude bounce is falsified (`research-defined falsification threshold`).

2. **Lag-3 Directional Reversal Persistence Audit:**
   - Sample: Expanding window on SPY, QQQ, and IWM.
   - Metric: Empirical continuation probability $p_{3,0}$ and $z_{\text{sign}}(3)$.
   - Falsification Rule: If $z_{\text{sign}}(3)$ drops to $|z_{\text{sign}}| < 1.00$ ($p > 0.30$) over a 3-year out-of-sample window, the 3-day partial-adjustment channel is declared a sample-dependent artifact (`research-defined falsification threshold`).

3. **Intraday TAQ High-Frequency Attribution Test:**
   - Data: Tick-by-tick Trade and Quote (TAQ) data for SPY constituents.
   - Metric: Serial covariance of trade signs vs. mid-quote returns.
   - Falsification Rule: If mid-quote returns (free of bid-ask bounce) exhibit lag-1 autocorrelation within 10% of transaction-price returns, the non-synchronous staleness attribution is falsified (`research-defined falsification threshold`).

4. **Cryptocurrency High-Frequency Friction Stress Test:**
   - Data: Binance and Coinbase 1-minute and 5-minute BTC/USDT, ETH/USDT, and SOL/USDT bars.
   - Metric: Variance ratio $VR(q)$ and subsample diagnostic $R_N$.
   - Falsification Rule: If high-frequency crypto returns exhibit $VR(2) < 0.90$ ($z^* < -2.50$) with $R_N \to 1.00$, the claim that crypto is immune to microstructure mean reversion is falsified (`research-defined falsification threshold`).

## Crypto portability

- **Portability Classification:** `not applicable` / `negative evidence`.
- **Reason:** The primary source empirically tests cryptocurrency (BTC and ETH) within its 21-instrument cross-asset panel and demonstrates that crypto is the purest random walk among all evaluated assets:
  1. **Absence of Constituent Staleness:** Bitcoin and Ether are single instruments, not composite baskets of illiquid underlying equities.
  2. **Continuous 24/7 Trading:** Crypto exchanges never close. There is no 16:00 ET closing auction, no overnight trading halt, and no session-boundary price staleness.
  3. **Absence of Specialist Dealer Smoothing:** Liquidity provision on centralized and decentralized crypto exchanges is conducted by competitive algorithmic market makers without NYSE-style designated market maker (DMM) inventory-smoothing obligations.
  4. **Subsample Persistence:** BTC and ETH display $R_N \approx \sqrt{2}$, the exact theoretical rate for IID sampling noise.
- **Porting Verdict:** Attempting to port equity ETF lag-1 or lag-3 mean-reversion strategies to spot or perpetual crypto markets is unproven and directly contradicted by the empirical findings of the cited source.

## Limitations

1. **End-of-Day Data Aggregation:** The primary research uses daily closing prices rather than intraday tick or quote data. While mathematical proofs isolate the magnitude vs. sign channels, exact intraday attribution of constituent trade timing requires high-frequency TAQ data.
2. **Marginal Economic Capacity of Lag-3 Directional Alpha:** The expected edge of the lag-3 directional reversal is small ($\approx 2\text{ bps}$ per trade), which is approximately equal to institutional execution costs ($2\text{ to }5\text{ bps}$) in SPY. The signal is valuable as a structural market-timing filter or execution delay tool rather than a standalone unhedged trading strategy.
3. **Fixed Median Magnitude Partitioning:** The $k=4$ magnitude channel partitions returns at the static sample median of $|r_t|$. In non-stationary volatility regimes (e.g., 2008 GFC, 2020 COVID), dynamic rolling quantile thresholds may provide superior resolution.
4. **Multiple Testing Adjustments:** Bonferroni corrections are applied within horizons ($m=7$), but cross-sectional correlation across the 21 panel assets is addressed conservatively rather than via full False Discovery Rate (FDR) modeling.

## Implementation status

- `not-implemented`.
- No prototype, backtest, or execution model has been implemented in `nautilus-quant-system`, PyBroker, or any trading stack.
- Research capture only; does not authorize paper, testnet, or live trading.

## Adoption boundary

- `research-only`.
- `adoption: not-approved`.
- `approval_scope: research-only`.
- Presence of this record indicates only that the research has been normalized into canonical Wiki Brain format. It does not constitute verification of alpha, profitability, or permission to trade.

## Related Wiki records

- `[[quant/conditioning-sign-on-magnitude-return-decomposition-csm-2026-09-04]]` (non-copula return decomposition conditioning sign on macro-predicted Weibull magnitude)
- `[[quant/microstructure-mean-reversion-optimal-symmetric-band-waiting-option-2026-09-02]]` (optimal trading of microstructure mean reversion net of transaction costs)
- `[[quant/futures-trend-following-autocorrelation-drift-decomposition-2026-09-02]]` (trend following and spectral autocorrelation decomposition in futures)
- `[[quant/crypto-cross-platform-binary-threshold-mispricing-polymarket-binance-2026-09-01]]` (Portnaya 2026 study of crypto options vs. prediction markets)

## Sources

- **Primary Preprint:** Victoria Portnaya, *"The Bounce Has No Direction: Sign, Magnitude, and the Microstructure of Equity Return Predictability: Fourier-Residue Identities, Fejér Sums, and Evidence from US Equity and Cross-Asset Markets, 1993–2026"*, arXiv preprint `arXiv:2606.29591v1 [q-fin.ST]`, submitted June 2026. Available at: [https://arxiv.org/abs/2606.29591](https://arxiv.org/abs/2606.29591), full HTML text at: [https://arxiv.org/html/2606.29591v1](https://arxiv.org/html/2606.29591v1).
- **Foundational Microstructure References Cited:**
  - Amihud, Y., & Mendelson, H. (1987). "Trading mechanisms and stock returns: An empirical investigation." *Journal of Finance*, 42(3), 533–553.
  - Glosten, L.R., & Milgrom, P.R. (1985). "Bid, ask and transaction prices in a specialist market with heterogeneously informed traders." *Journal of Financial Economics*, 14(1), 71–100.
  - Ho, T., & Stoll, H.R. (1981). "Optimal dealer pricing under transactions and return uncertainty." *Journal of Financial Economics*, 9(1), 47–73.
  - Lo, A.W., & MacKinlay, A.C. (1988). "Stock market prices do not follow random walks: Evidence from a simple specification test." *Review of Financial Studies*, 1(1), 41–66.
  - Lo, A.W., & MacKinlay, A.C. (1990). "An econometric analysis of nonsynchronous trading." *Journal of Econometrics*, 45(1–2), 181–211.
  - Roll, R. (1984). "A simple implicit measure of the effective bid-ask spread in an efficient market." *Journal of Finance*, 39(4), 1127–1139.
  - Scholes, M., & Williams, J. (1977). "Estimating betas from nonsynchronous data." *Journal of Financial Economics*, 5(3), 309–327.
  - Stoll, H.R. (1989). "Inferring the components of the bid-ask spread: Theory and empirical tests." *Journal of Finance*, 44(1), 115–134.
