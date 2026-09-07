---
schema: strategy-research-record-v1
title: "Adaptive Copula-Based Pairs Trading with Market Overlay for Crypto Perpetuals"
created: 2026-09-07
updated: 2026-09-07
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - relative-value
  - copula
  - pairs-trading
  - negative-evidence
status: research-only
confidence: high
source_as_of: 2026-06-11
sources:
  - "https://doi.org/10.3934/QFE.2026016"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions:
  - "crypto-pairs-trading-copula-cointegration-2026-08-31.md (Tadi & Witzany 2023 reported positive copula pairs trading returns on crypto; Pindza & Mba 2026 find negative net returns after realistic costs on perpetual futures)"
---

# Adaptive Copula-Based Pairs Trading with Market Overlay for Crypto Perpetuals

## Provenance

- **Authors:** Edson Pindza (Department of Decision Sciences, University of South Africa) and Jules Clement Mba (School of Economics, University of Johannesburg)
- **Title:** "Adaptive copula-based pairs trading with market overlay: An enhanced framework for cryptocurrency markets"
- **Published:** Quantitative Finance and Economics, 10(2), 378–404, 2026. DOI: [10.3934/QFE.2026016](https://doi.org/10.3934/QFE.2026016)
- **Access:** Open access (CC BY 4.0)
- **Data period:** January 2021 – December 2023 (26,257 hourly observations per asset)
- **Universe:** Ten Binance USDT perpetual futures: BTC, ETH, BNB, ADA, SOL, XRP, DOT, LTC, LINK, DOGE

## Economic mechanism

### Source-reported

The strategy combines cointegration-based pair selection with copula-modeled nonlinear dependence to generate trading signals via a Copula Mispricing Index (CMI). When two cointegrated assets deviate from their historical joint distribution (as captured by the copula), the CMI quantifies the degree of mispricing. An Alpha Overlay variant relaxes strict market neutrality by maintaining full market exposure while allocating a sleeve to pairs trading.

### Research interpretation

**Mechanism:** Liquidity provision / relative-value mean reversion. The hypothesis is that cointegrated crypto perpetual pairs exhibit transient mispricings in their joint distribution that can be exploited via copula-conditional probabilities. The CMI provides a probabilistic signal that is more flexible than simple Z-score thresholds because it captures nonlinear and tail-dependent relationships.

**Components:**
- Regime filter: Cointegration test (ADF + KSS nonlinear) with half-life < 30 days
- Primary signal: Copula Mispricing Index (CMI) = h₁|₂(U₁|U₂) − 0.5, where h₁|₂ is the conditional CDF from the fitted copula
- Copula selection: Student-t dominates (89.9% of formation periods), consistent with tail dependence in crypto
- Position sizing: Fixed fraction (2–3% of equity), capped by risk budget
- Risk management: Stop-loss (1.5–2.5%), profit target (0.8–1.5%), max holding period (72–144 bars)
- Alpha Overlay variant: 100% market exposure + 30% capital to pairs trading sleeve

**Key finding (negative):** Market-neutral copula strategies achieve low drawdowns (<20%) but generate NEGATIVE net returns (−14% to −16%) after realistic transaction costs and funding payments. The Alpha Overlay is nearly indistinguishable from buy-and-hold.

## Signal

- **Formation timestamp:** Rolling 90-day (2,160-hour) formation window; copula re-estimated each cycle.
- **Trading window:** 14-day (336-hour) trading period following each formation.
- **Lookback:** 90 days of hourly prices for cointegration testing, copula fitting, and parameter estimation.
- **Cointegration tests:** Engle-Granger (ADF on residuals) and Kapetanios-Shin-Snell (KSS nonlinear unit root). Both must reject unit root; half-life of mean reversion required < 30 days.
- **Copula fitting:** Five candidate families (Gaussian, Student-t, Clayton, Gumbel, Frank). Selected by AIC, validated by Rosenblatt-transform GOF (KS and CvM tests, bootstrap p-values ≥ 5%).
- **CMI signal construction:**
  - Transform prices to pseudo-observations via empirical marginal CDFs
  - Compute conditional CDF h₁|₂(U₁|U₂) under the fitted copula
  - CMI_t = h₁|₂(U₁_t|U₂_t) − 0.5 ∈ [−0.5, 0.5]
  - Closed-form expressions provided for each copula family (Eqs. 15–19)
- **Entry:** Open long Asset 1 / short Asset 2 when CMI < −t_o AND open short Asset 1 / long Asset 2 when CMI > t_o. Entry threshold t_o grid-searched at 0.20, 0.25, 0.30, 0.35, 0.40.
- **Exit:** CMI reversion (|CMI| < t_c), profit target, stop-loss, or max holding period.
- **Hedge ratio:** Beta-weighted from OLS regression during formation period.
- **Parameters:** Fully specified by the source (Table 2 of paper).

## Required data

- **Instrument:** Binance USDT perpetual futures (BTC, ETH, BNB, ADA, SOL, XRP, DOT, LTC, LINK, DOGE)
- **Venue:** Binance (spot API for price data)
- **Market type:** Perpetual futures (USDT-margined)
- **Timeframe:** Hourly bars
- **Fields:** Hourly close prices; 8-hourly funding rate payments for perpetual contracts
- **Point-in-time:** Fixed universe at study start (no survivorship bias); no look-ahead in formation periods
- **Timestamp:** UTC; hourly resolution
- **Missing-data:** All ten assets continuously traded throughout sample; no imputation needed
- **Funding/fee needs:** Exchange taker fees (0.04% per side), bid-ask spread (0.02% per leg), 8-hourly funding payments. Total baseline round-trip cost: 0.12%.

## Execution assumptions

- **Signal-to-order timing:** Same-bar execution assumed (hourly)
- **Order type:** Market orders
- **Fill model:** Full fill assumed at bar close
- **Fees:** 0.04% taker per side (0.08% round-trip)
- **Spread:** 0.02% per leg (0.04% round-trip)
- **Slippage:** Conservative bid-ask spread model; no explicit slippage model beyond spread
- **Funding:** 8-hourly perpetual funding payments deducted/credited for open positions
- **Leverage:** Not explicitly stated; position sizing based on equity fraction
- **Impact:** Not modeled; assumed negligible for the universe size
- **Partial fills / failures:** Not modeled

## Evidence

### Source-reported

**Market-neutral variants (Conservative/Balanced/Moderate):**
- Total return: −14.3% to −16.3% over 3 years (net of all costs)
- Annualized return: −5.0% to −5.8%
- Sharpe ratio: −2.64 to −3.67
- Max drawdown: −15.2% to −17.2%
- Win rate: 49.5% to 51.9%
- Trade count: 5,490 to 9,058

**Alpha Overlay variant:**
- Total return: +41.1% (vs. buy-and-hold +46.1%)
- Sharpe: 0.15 (vs. buy-and-hold 0.17)
- Max drawdown: −78.3% (vs. buy-and-hold −77.2%)
- Tracking error vs. buy-and-hold: 0.43% annualized

**P&L decomposition (Moderate strategy, per trade):**
- Average gross return: +0.15%
- Average trading cost: −0.12%
- Average funding impact: −0.18%
- Average net return: −0.15%

**Transaction cost sensitivity (Moderate):**
- 0.04% round-trip: total return −9.4%, Sharpe −1.88
- 0.08% round-trip: total return −15.4%, Sharpe −2.64
- 0.20% round-trip: total return −31.6%, Sharpe −4.91

**Pair-level heterogeneity:** Top 5 pairs by net P&L are all positive (SOL/DOT: +9,209; XRP/BNB: +6,749; BTC/DOGE: +6,116; LTC/XRP: +4,065; BNB/ADA: +1,820), but aggregate is negative due to many unprofitable pairs.

**Copula selection:** Student-t copula selected in 89.9% of formation periods, consistent with tail dependence in crypto returns.

**Market exposure:** β = 0.08 for Moderate strategy, confirming near-zero market exposure.

**Risk metrics (Moderate, daily):** VaR₉₉ = 0.52%, ES₉₉ = 0.83%, ES/VaR = 1.59.

### Independently reproduced

Not independently reproduced.

### Negative evidence

This paper IS a negative result. Key negative findings:
1. **Net alpha is negative after realistic costs:** The core mean-reversion signal generates a small positive gross edge (+0.15% per trade) but this is insufficient to overcome trading costs (−0.12%) and funding impact (−0.18%).
2. **Funding payments are a dominant cost:** The −0.18% average funding impact per trade is larger than the trading cost drag, highlighting that perpetual futures funding erodes pairs trading profitability.
3. **Entry threshold sensitivity does not rescue profitability:** Raising the entry threshold from 0.20 to 0.40 reduces trades but does not restore positive net returns.
4. **Alpha Overlay adds no measurable alpha:** The overlay's Sharpe and return are virtually identical to buy-and-hold, indicating the pairs component contributes negligible excess return.
5. **Even at 0.04% round-trip costs (aggressive), net returns remain negative** (−9.4% total).

## Falsification plan

1. **Transaction cost stress:** Test at 0.01% and 0.00% round-trip costs to identify the breakeven cost threshold (research-proposed). If net returns remain negative below realistic maker rebates, reject the copula CMI hypothesis.
2. **Regime conditioning:** Partition sample into bull (2021), bear (2022), and recovery (2023) regimes. If the CMI signal is profitable in one regime but dominated by losses in another, the mechanism is regime-dependent.
3. **Alternative copula families:** Force Clayton (lower tail dependence only) or Frank (no tail dependence) across all pairs. If performance changes materially, the Student-t dominance is doing the explanatory work.
4. **Simpler baseline comparison:** Run a Z-score mean-reversion signal on the same cointegration residuals with the same entry/exit thresholds. If the simpler signal performs comparably, the copula layer adds no incremental value.
5. **Cross-venue replication:** Replicate on Deribit or OKX perpetuals with different fee structures and funding mechanisms.
6. **Walk-forward with adaptive copula:** Allow copula re-estimation within the trading window (not just at formation boundaries). If this improves net returns, the static-within-window assumption is the binding constraint.

## Crypto portability

**Direct** — the paper is already designed for and tested on Binance USDT perpetual futures.

Crypto-specific considerations:
- **Funding payments:** The paper demonstrates that 8-hourly funding is a dominant cost for pairs held across funding epochs. This is a first-order consideration absent from equity pairs trading.
- **24/7 operation:** Hourly bars with no session breaks; continuous formation and trading windows.
- **Venue fragmentation:** Tested only on Binance; cross-exchange pairs not explored.
- **Perpetual vs. spot:** The paper explicitly models perpetual-specific costs (funding), making it directly relevant to perpetual futures trading.
- **Liquidity:** Top-10 perpetuals are highly liquid; spread assumption (0.02% per leg) is reasonable for these instruments.

## Limitations

- **Negative net result:** The primary finding is that copula CMI pairs trading does not generate positive alpha net of realistic costs on crypto perpetuals. This is a limitation of the strategy, not the paper.
- **Constant cost assumption:** Transaction costs are fixed at 0.04% per side; actual costs vary with market conditions and order size.
- **Bivariate copulas only:** No vine copula extension for multi-asset relationships.
- **No comparison to simpler baselines:** The paper does not benchmark against Z-score mean-reversion or distance-based pairs trading, so the incremental value of the copula layer is unquantified.
- **Fixed universe:** Ten assets selected at study start; no dynamic universe management.
- **Code not publicly released:** "Code is available upon request" rather than open-source.
- **Sample period:** Jan 2021 – Dec 2023; does not cover 2024–2026 market regimes.
- **data gap:** The paper notes that regime shifts may cause dependency structure changes that the copula model fails to capture, but does not provide a formal regime-detection overlay.

## Implementation status

Not implemented. No implementation in our research stack.

## Adoption boundary

This record is research material only. Its presence in this repository does not mean:
- Profitable
- Validated alpha
- Approved for implementation
- Approved for paper trading
- Approved for testnet or live trading

The paper's primary finding is NEGATIVE: copula-based pairs trading generates negative net returns on crypto perpetuals after realistic costs. This serves as important negative evidence against the hypothesis that copula CMI signals can overcome perpetual futures transaction costs and funding payments.

## Related Wiki records

- `[[crypto-pairs-trading-copula-cointegration-2026-08-31]]` — Copula-based pairs trading on crypto (Tadi & Witzany 2023); reports positive results on spot futures, but without perpetual funding cost modeling. This record provides critical negative evidence under more realistic cost assumptions.

## Sources

1. Edson Pindza and Jules Clement Mba, "Adaptive copula-based pairs trading with market overlay: An enhanced framework for cryptocurrency markets," Quantitative Finance and Economics, 10(2), 378–404, 2026. DOI: [10.3934/QFE.2026016](https://doi.org/10.3934/QFE.2026016). Open access (CC BY 4.0).
2. Full text: [https://www.aimspress.com/journal/QFE](https://doi.org/10.3934/QFE.2026016)
