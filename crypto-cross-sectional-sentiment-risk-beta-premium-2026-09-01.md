---
schema: strategy-research-record-v1
title: Crypto Cross-Sectional Sentiment Risk Beta and Non-Linear Mispricing
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - sentiment
  - fear-and-greed
  - asset-pricing
  - behavioral-finance
status: research-only
confidence: high
source_as_of: 2025
sources:
  - https://ideas.repec.org/a/eee/jbefin/v46y2025ics2214635024001098.html
  - https://doi.org/10.1016/j.jbef.2025.101043
  - https://alternative.me/crypto/fear-and-greed-index/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Cross-Sectional Sentiment Risk Beta and Non-Linear Mispricing

## Provenance

- **Primary Academic Source:** SeungOh Han, “Investor sentiment and cross-section of cryptocurrency returns,” *Journal of Behavioral and Experimental Finance*, Volume 46, 2025, Article 101043, doi:10.1016/j.jbef.2025.101043; RePEc: `RePEc:eee:jbefin:v:46:y:2025:i:c:s2214635024001098`.
- **Sample & Benchmark Data:** Cross-section of actively traded cryptocurrencies spanning November 2018 through July 2024, coupled with daily changes in the Alternative.me Crypto Fear and Greed Index (FGI).
- **Core Signal Concept:** Estimating cross-sectional return sensitivity ($\beta_{\text{Sent}}$) to systemic market sentiment shifts, identifying a negative sentiment risk premium at the extreme upper tail and non-linear outperformance for intermediate sentiment-beta assets.

## Economic mechanism

### Source-reported

In behavioral asset pricing, retail-dominated markets are heavily prone to sentiment swings that drive asset prices away from fundamental values. In cryptocurrency markets, where traditional cash-flow valuation anchors are absent, investor sentiment functions as a primary pricing driver.

Han (2025) defines **sentiment risk** as the sensitivity of an individual cryptocurrency's returns to innovations in the aggregate Crypto Fear and Greed Index ($\Delta\text{FGI}_t$). The author reports that:
1. **Negative Sentiment Risk Premium at the High End:** Cryptocurrencies exhibiting high positive sensitivity to market sentiment ($\beta_{\text{Sent}}$) deliver negative future risk-adjusted returns. The paper attributes this to retail investors overpaying for high-beta, "lottery-like" speculative tokens during bullish sentiment expansions, leading to severe subsequent price corrections.
2. **Intermediate Sentiment Advantage:** The relationship between sentiment beta and expected returns is non-linear (inverted U-shape). Cryptocurrencies categorized with **intermediate levels of sentiment risk** generate statistically significant higher risk-adjusted weekly returns (reported 3.57% spread) relative to low- or high-risk assets.

### Research interpretation

The strategy is a **cross-sectional behavioral mispricing and speculative tail-risk avoidance alpha**:
1. **Speculative Overheating in High-Beta Tokens:** High sentiment-beta tokens represent hyper-speculative meme coins, unbacked governance tokens, or narrative-driven altcoins. During market euphoria ($\text{FGI} > 75$), irrational optimism inflates their prices to unsustainable valuations. Once sentiment mean-reverts or stabilizes, these overextended tokens suffer disproportionately severe liquidations.
2. **Underperformance of Low-Beta Tokens:** Extreme low-beta or negative-beta tokens are frequently illiquid, neglected, or decaying legacy tokens that fail to capture capital inflows even during broad market rallies.
3. **The Intermediate Sweet Spot:** Intermediate-beta tokens correspond to established, liquid mid-to-large-cap protocol assets that participate in ecosystem growth without becoming vehicles for extreme retail mania, creating durable risk-adjusted outperformance when sorted against the extremes.

## Signal

The quantitative alpha strategy is structured as a weekly cross-sectional portfolio sorting and rebalancing model:

1. **Sentiment Innovation Calculation:**
   Using the daily Crypto Fear and Greed Index $\text{FGI}_t \in [0, 100]$:
   $$\Delta\text{FGI}_t = \text{FGI}_t - \text{FGI}_{t-1}$$

2. **Rolling Factor Sensitivity Estimation:**
   For each cryptocurrency $i$ in the liquid investable universe (minimum 30-day average daily volume $>\$1\text{M}$), estimate the following multi-factor regression over a rolling lookback window of $W = 60$ daily observations:
   $$R_{i, \tau} = \alpha_{i, t} + \beta_{\text{Mkt}, i, t} R_{\text{Mkt}, \tau} + \beta_{\text{Sent}, i, t} \Delta\text{FGI}_\tau + \epsilon_{i, \tau}, \quad \tau \in [t-W+1, t]$$
   where $R_{\text{Mkt}, \tau}$ is the value-weighted crypto market index return (or BTC return) and $\beta_{\text{Sent}, i, t}$ is the estimated sentiment beta.

3. **Cross-Sectional Portfolio Construction:**
   At weekly rebalance boundary $t$ (standardized at Sunday 23:59 UTC / Monday 00:00 UTC):
   - Sort the cross-section into quintiles based on $\beta_{\text{Sent}, i, t}$:
     - $Q1$: Lowest sentiment risk (lowest / negative $\beta_{\text{Sent}}$).
     - $Q2$: Low-intermediate sentiment risk.
     - $Q3$: Intermediate sentiment risk.
     - $Q4$: High-intermediate sentiment risk.
     - $Q5$: Highest sentiment risk (extreme speculative sensitivity).
   - **Long Leg:** Allocate equal or capitalization weights to assets in quintile $Q3$ (intermediate sentiment risk).
   - **Short Leg / Underweight Leg:** Allocate short exposure or underweight to quintiles $Q1$ and $Q5$ (the extreme ends of the sentiment spectrum).
   - **Rebalance Frequency:** Weekly, held for $K = 7$ days.

## Required data

- **Universe:** Top 100–300 actively traded cryptocurrencies by spot and perpetual trading volume.
- **Price & Return Data:** Daily OHLCV price series for all universe components from November 2018 onwards.
- **Sentiment Index:** Daily published values of the Alternative.me Crypto Fear and Greed Index (FGI).
- **Market Benchmark:** Value-weighted cryptocurrency market index return or BTC daily return.
- **Liquidity Filters:** Minimum daily dollar volume threshold ($\ge \$1\text{M}$) and minimum historical listing length ($> 90$ days) to eliminate survivor/delisting artifacts.
- **Point-in-Time Timing:** Daily FGI values finalized at 00:00 UTC, ensuring no lookahead bias into weekly rebalancing decisions.

## Execution assumptions

- **Execution Timing:** Weekly rebalance executed at Monday 00:05 UTC.
- **Execution Instruments:** Cross-sectional perpetual futures contracts on liquid centralized venues (e.g., Binance, Bybit, OKX).
- **Friction Model:**
  - Perpetual taker fees: 2 to 5 bps per trade.
  - Bid-ask spread: 2 to 10 bps depending on altcoin market cap.
  - Perpetual funding rate payments: 8-hour funding settlements accounted for across long and short legs.
  - Estimated weekly round-trip transaction drag: 20 to 40 bps.
- **Capacity:** Constrained by the borrow liquidity and perpetual open interest of altcoins in $Q1$ and $Q5$. Long-only implementation ($Q3$ vs. market cap benchmark) provides significantly higher capacity.

## Evidence

### Source-reported

- **Negative Sentiment Risk Premium:** Han (2025) demonstrates a statistically significant negative cross-sectional relationship between high $\beta_{\text{Sent}}$ and subsequent cryptocurrency returns in Fama–MacBeth regressions after controlling for market size, 1-week reversal, 30-day momentum, and Amihud illiquidity across the November 2018 – July 2024 sample.
- **Intermediate Quintile Outperformance:** The intermediate sentiment risk portfolio ($Q3$) achieved risk-adjusted weekly returns that were **3.57% higher** than those of the extreme risk portfolios ($Q1$ and $Q5$).
- **Lottery Preference Verification:** The author confirms that high-$\beta_{\text{Sent}}$ assets overlap heavily with tokens exhibiting high maximum daily return ($\text{MAX}$) and idiosyncratic volatility, verifying that retail lottery-seeking behavior drives the overpricing of extreme sentiment-sensitive tokens.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Short-Side Execution Frictions:** In practice, shorting extreme high-beta speculative altcoins in $Q5$ can be dangerous during parabolic bull runs; borrow rates can spike, and short squeeze cascades can cause severe drawdowns before the negative risk premium materializes.
- **FGI Index Formulation Opacity:** The Alternative.me FGI uses proprietary heuristic weightings (volatility 25%, market volume 25%, social media 15%, dominance 10%, Google Trends 10%), which may undergo undocumented methodology revisions over time.
- **Turnover Sensitivity:** Rolling 60-day regressions can produce rank switching among mid-cap altcoins, generating weekly portfolio turnover of 30% to 50%, which reduces net Sharpe ratio under high taker fee assumptions.

## Falsification plan

The sentiment risk factor hypothesis will be rejected if:
1. In an out-of-sample test from August 2024 onwards, the long $Q3$ / short $(Q1+Q5)/2$ portfolio generates an annualized net Sharpe ratio $< 0.3$ after accounting for 30 bps round-trip transaction costs and funding fees.
2. In Fama–MacBeth cross-sectional regressions, the $t$-statistic on $\beta_{\text{Sent}}$ drops below $|1.96|$ when controlling simultaneously for the CTREND factor and MAX daily return factor, indicating that sentiment beta is entirely subsumed by existing technical/lottery factors.
3. Permuting the publication timestamp of the FGI index produces indistinguishable cross-sectional alphas, confirming spurious correlation.

## Crypto portability

- **Direct:** The strategy and empirical evidence are natively derived from cryptocurrency cross-sectional market data and crypto-specific sentiment indicators.
- **Cross-Market Comparison (Adapted):** Similar non-linear sentiment effects have been documented in equity markets (e.g., Baker & Wurgler sentiment index), but crypto markets exhibit substantially larger economic magnitudes (3.57% weekly spread vs. ~0.5% monthly in equities).

## Limitations

- **Not independently reproduced.**
- **Sentiment Index Provider Risk:** Dependence on a single third-party index provider (Alternative.me); disruptions or API changes require fallback to synthetic multi-source sentiment models.
- **Asymmetric Shorting Costs:** High funding rates and liquidation risks on volatile altcoins make long/short dollar-neutral implementation risky; long-only tilt is more operationally robust.

## Implementation status

Not implemented in the research stack. No PyBroker, NautilusTrader, Paper, Testnet, or Live verification has been performed.

`implementation_status: not-implemented`

## Adoption boundary

This record is `research-only`, `not-implemented`, and `not-approved`. Presence in the repository does not constitute authorization for live trading, testnet, or capital allocation.

`status: research-only`
`adoption: not-approved`
`approval_scope: research-only`

## Related Wiki records

- `crypto-cross-sectional-abnormal-investor-attention-momentum-2026-08-31.md` — Investor attention and search volume momentum.
- `crypto-cross-sectional-max-daily-return-lottery-momentum-2026-08-31.md` — Maximum daily return lottery factor.
- `crypto-cross-sectional-abnormal-volume-disagreement-2026-08-31.md` — Investor disagreement and volume anomaly.
- `crypto-cross-sectional-factor-momentum-anomaly-portfolios-2026-08-31.md` — Cross-sectional factor momentum.

## Sources

1. SeungOh Han, “Investor sentiment and cross-section of cryptocurrency returns,” *Journal of Behavioral and Experimental Finance*, Volume 46, 2025, Article 101043, doi:10.1016/j.jbef.2025.101043.
2. RePEc IDEAS record: https://ideas.repec.org/a/eee/jbefin/v46y2025ics2214635024001098.html.
3. Alternative.me Crypto Fear and Greed Index Methodology & Historical Archive: https://alternative.me/crypto/fear-and-greed-index/.
