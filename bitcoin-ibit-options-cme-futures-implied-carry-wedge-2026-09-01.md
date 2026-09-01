---
schema: strategy-research-record-v1
title: Bitcoin IBIT Options Implied Forward vs CME Futures Carry Wedge Arbitrage
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - bitcoin
  - etf-options
  - cme-futures
  - carry
  - basis
  - relative-value
  - limits-to-arbitrage
  - market-microstructure
status: research-only
confidence: medium
source_as_of: 2026-05-28
sources:
  - "Mallory, M. L. (2026). Implied ETF Carry Rates and the Limits of Arbitrage in Segmented Bitcoin Markets. arXiv preprint arXiv:2605.29309v1 [q-fin.PR]. https://arxiv.org/abs/2605.29309"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin IBIT Options Implied Forward vs CME Futures Carry Wedge Arbitrage

## Provenance

- **Primary source:** Mindy L. Mallory (Purdue University, Department of Agricultural and Consumer Economics), "Implied ETF Carry Rates and the Limits of Arbitrage in Segmented Bitcoin Markets", *arXiv preprint arXiv:2605.29309v1 [q-fin.PR]*, published May 28, 2026. URL: https://arxiv.org/abs/2605.29309.
- **Empirical sample:** 386 date-bucket paired observations spanning 2024 through 2026 following the listing and options trading rollout on spot Bitcoin exchange-traded funds.
- **Instruments:** Listed equity options on BlackRock's iShares Bitcoin Trust (IBIT), CME Bitcoin futures (front-month and deferred maturities), and the CME CF Bitcoin Reference Rate New York Variant (BRRNY, the benchmark index for IBIT).
- **Data normalization:** ETF share prices are mapped into underlying Bitcoin units using BlackRock's daily basket holdings disclosure (shares-per-bitcoin ratio) to ensure exact physical equivalence.
- **Public-use status:** Public academic preprint hosted on arXiv.

## Economic mechanism

### Source-reported

The source demonstrates that Bitcoin exposure has become accessible through multiple regulated institutional wrappers, specifically spot exchange-traded funds (such as IBIT), listed options on spot ETFs, and cash-settled futures traded on the Chicago Mercantile Exchange (CME). 

Under classical no-arbitrage pricing with frictionless capital mobility, the implied forward carry extracted from spot ETF options (via put-call parity) and the basis carry observed in CME Bitcoin futures should converge to the same risk-adjusted cost of carry. 

However, Mallory (2026) identifies a persistent, statistically significant carry discrepancy—termed the "wedge"—between IBIT option-implied forwards and CME Bitcoin futures. The paper attributes this wedge to structural market segmentation and limits to arbitrage:
1. **Segmented Clearing Systems:** IBIT options clear through the Options Clearing Corporation (OCC) under SEC equity margin rules, whereas CME Bitcoin futures clear through CME Clearing under CFTC derivatives margin rules.
2. **Absence of Unified Cross-Margining:** Market participants cannot offset margin requirements across the OCC and CME Clearing without bespoke bilateral arrangements at high-tier prime brokers, forcing arbitrageurs to maintain double gross margin collateral.
3. **Differential Clienteles and Access:** Retail and traditional equity options market makers dominate IBIT options flow, whereas institutional macro funds, hedge funds, and basis traders concentrate in CME futures.

### Research interpretation

The alpha hypothesis is **cross-market institutional basis carry dispersion**: persistent structural segmentation between equity option clearinghouses (OCC) and futures clearinghouses (CME) prevents full capital mobility, allowing a relative-value basis carry trade to harvest the premium differential.

The trade mechanism is not directional on Bitcoin price; rather, it is a relative-value carry convergence or spread harvest between:
- A synthetic short forward on CME futures (selling higher basis carry); and
- A synthetic long forward on IBIT via options (buying lower implied forward carry via long call + short put at identical strike and maturity) or holding spot IBIT shares financed against the synthetic forward.

The trade profits as the basis premium decays into expiration, provided the gross carry wedge exceeds the dual-margin financing hurdle, clearing frictions, and transaction costs.

## Signal

The normalized signal framework is structured as follows:

1. **Synthetic Forward Extraction (IBIT Options):**
   - For a given expiration date $T$ and strike $K$, identify paired IBIT European/American call ($C_t$) and put ($P_t$) quotes near at-the-money.
   - Using put-call parity adjusted for the risk-free rate $r$:
     $$F_{\text{IBIT}, t, T} = K + e^{r(T-t)} (C_t - P_t)$$
   - Convert ETF forward price into Bitcoin-denominated forward price using BlackRock's daily shares-per-BTC multiplier $M_t$:
     $$F_{\text{IBIT-BTC}, t, T} = F_{\text{IBIT}, t, T} \times M_t$$
   - Calculate the annualized implied carry rate:
     $$c_{\text{IBIT}, t, T} = \frac{F_{\text{IBIT-BTC}, t, T} - S_{\text{BRRNY}, t}}{S_{\text{BRRNY}, t}} \cdot \frac{365}{T - t}$$

2. **CME Futures Carry Calculation:**
   - For CME Bitcoin futures maturing at date $T$ with price $F_{\text{CME}, t, T}$ relative to benchmark spot $S_{\text{BRRNY}, t}$:
     $$c_{\text{CME}, t, T} = \frac{F_{\text{CME}, t, T} - S_{\text{BRRNY}, t}}{S_{\text{BRRNY}, t}} \cdot \frac{365}{T - t}$$

3. **Carry Wedge Construction:**
   $$Wedge_t(T) = c_{\text{CME}, t, T} - c_{\text{IBIT}, t, T}$$

4. **Entry Trigger:**
   - **Sell CME Basis / Buy IBIT Implied Forward:** Enter when $Wedge_t(T) > \text{Threshold}_{\text{entry}}$, where $\text{Threshold}_{\text{entry}}$ covers the round-trip dual-venue transaction costs, OCC/CME margin financing drag, and bid-ask spread.
   - **Position Allocation:**
     - Short 1 contract CME Bitcoin futures ($5\text{ BTC}$ notional equivalent).
     - Long synthetic forward in IBIT options: Buy 500 call contracts ($5\text{ BTC}$ equivalent) and Sell 500 put contracts ($5\text{ BTC}$ equivalent) at strike $K$, or hold long physical IBIT shares hedged by short put/long call.

5. **Exit Trigger:**
   - Hold until contract expiration $T$, where both derivatives settle to their terminal reference prices ($S_T$), realizing the locked-in carry wedge.
   - Early exit if $Wedge_t(T) \le \text{Threshold}_{\text{exit}}$ (e.g. $\le 0.25\%$) prior to expiration, releasing collateral.

6. **Specification Boundary:**
   - Exact numerical entry/exit threshold depends on the trading firm's specific prime-broker margin terms and borrowing rate. The source reports historical cross-sectional distributions but does not provide a fixed single trading threshold.

## Required data

- **IBIT Options Data:** Tick or daily closing bid/ask quotes, open interest, and implied volatilities for all listed strikes and expirations on IBIT.
- **IBIT ETF Daily Multiplier:** Daily BlackRock holdings disclosures reporting total net asset value (NAV), shares outstanding, and exact Bitcoin holdings (BTC per share ratio $M_t$).
- **CME Bitcoin Futures:** Tick/minute trade and settlement prices for active front-month and deferred CME standard ($5\text{ BTC}$) and micro ($0.1\text{ BTC}$) contracts.
- **Reference Benchmark Index:** CME CF Bitcoin Reference Rate New York Variant (BRRNY) published daily at 16:00 ET.
- **Interest Rate Benchmark:** SOFR (Secured Overnight Financing Rate) or US Treasury yield curve matching derivatives maturities.
- **Margin & Haircut Requirements:** Daily maintenance and initial margin parameters from OCC and CME Clearing.
- **Point-in-time Synchronization:** All quotes aligned strictly at 16:00 ET (US equity market close / BRRNY calculation window) without look-ahead bias.

## Execution assumptions

### Source-reported assumptions

- The empirical sample consists of 386 paired date-bucket observations.
- Uses BRRNY 16:00 ET benchmark for spot alignment across CME futures and IBIT options.
- Relies on daily ETF basket composition files published by BlackRock.

### Practical implementation assumptions

- **Dual-Venue Margin Drag:** Requires posting initial margin collateral at both OCC-cleared brokerages (typically 30–50% initial margin for equity options) and CME-clearing FCMs (typically 40–50% initial margin for Bitcoin futures), resulting in an effective unlevered capital requirement of 80–100% of notional unless cross-margining is secured.
- **Early Exercise Risk:** IBIT options are American-style; deep ITM options carry early-exercise risk that can disrupt synthetic forward parity prior to expiration.
- **Order Execution Latency:** Non-atomic leg execution between CME Globex and US equity options exchanges (CBOE, MIAX, BOX, Nasdaq Phlx), creating execution slippage risk.
- **Fees & Commissions:** CME exchange/clearing fees + FCM commissions, OCC options contract clearing fees, and broker equity commissions.

## Evidence

### Source-reported

Mallory (2026) reports the following empirical metrics from the 386 date-bucket observation sample:
- **Mean Carry Wedge:** $+2.58\%$ annualized percentage points (CME futures carry exceeds IBIT option-implied carry).
- **Median Carry Wedge:** $+2.52\%$ annualized percentage points.
- **Volatility of Carry:** CME futures carry exhibits significantly higher dispersion and variance across time than IBIT option-implied forward carry, which remains relatively anchored.
- **Limits to Arbitrage Confirmation:** The persistent positive wedge does not compress to zero in daily data, corroborating the hypothesis that capital frictions and lack of cross-margining prevent arbitrageurs from completely eliminating the basis difference.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Capital Inefficiency:** In the absence of institutional portfolio margin / cross-margining agreements between OCC and CME Clearing, the capital required to collateralize both legs severely depresses return on equity (ROE). A $2.58\%$ annualized wedge on gross notional yields only $\approx 1.29\%$ net ROE on a $200\%$ collateral requirement before fees.
- **American Exercise Premium:** For American-style ETF options, the standard put-call parity relationship is an inequality ($S - K \le C - P \le S - K e^{-rT}$), introducing a model discrepancy when estimating synthetic forward prices.
- **ETF Tracking Error and Fee Drag:** The $0.25\%$ annual sponsor fee on IBIT causes the spot ETF NAV to slowly decay relative to spot BTC, requiring continuous adjustment of the shares-to-BTC conversion factor.

## Falsification plan

The strategy hypothesis should be deemed falsified or commercially unviable if:
1. **Net Spread Compression:** Net of real-world OCC and CME initial margin financing costs, borrow fees, and execution slippage, the executable wedge drops below $0.50\%$ annualized across $> 80\%$ of trading days.
2. **Cross-Margining Implementation:** If OCC and CME introduce formal cross-margining for Bitcoin spot ETFs and futures, eliminating the capital friction and compressing the mean wedge to $< 0.30\%$.
3. **Execution Legging Risk:** Replaying historical high-frequency order book quotes demonstrates that leg execution latency across CME Globex and CBOE/options exchanges produces adverse execution slippage exceeding $0.75\%$ annualized.
4. **Subperiod Inversion:** Across a rolling 90-day window, CME carry persistently trades below IBIT implied carry without mean-reverting, invalidating the directional sign of the structural carry premium.

## Crypto portability

**Adapted / unproven** for unconstrained crypto execution; the underlying economic exposure is Bitcoin, but the trading instruments are strictly regulated TradFi derivatives wrappers (US listed options and CFTC futures).

Portability considerations:
- Direct implementation is restricted to institutional accounts with access to both US equity options exchanges (OCC cleared) and CME derivatives (FCM cleared).
- Cannot be executed purely via crypto-native decentralized exchanges or offshore centralized exchanges (Binance, Bybit) without introducing additional venue counterparty and basis risks.
- Provides a model for evaluating cross-venue pricing efficiency across segmented regulated crypto financial products.

## Limitations

- **not independently reproduced**;
- **underspecified execution threshold:** requires firm-specific margin financing rate calibration;
- **clearing segmentation barrier:** requires substantial balance sheet capacity across multiple clearinghouses;
- **sample length:** 386 date-bucket observations represent an initial post-ETF launch sample period (2024–2026);
- **American option approximation:** put-call parity inversions on American-style equity options introduce small early-exercise boundary approximations.

## Implementation status

not-implemented

No implementation in PyBroker, NautilusTrader, or internal trading pipelines has been performed.

## Adoption boundary

research-only

This record is research material only. It does not constitute investment advice, a validated profitable strategy, or authorization for Paper, Testnet, or Live trading execution.

## Related Wiki records

- [[quant/bitcoin-us-spot-etf-net-flow-next-day-drift-2026-09-01]]
- [[quant/crypto-futures-term-structure-roll-yield-carry-2026-08-31]]
- [[quant/crypto-cex-dex-cross-venue-funding-spread-carry-2026-08-31]]

## Sources

1. Mallory, M. L. (2026). "Implied ETF Carry Rates and the Limits of Arbitrage in Segmented Bitcoin Markets." *arXiv preprint arXiv:2605.29309v1 [q-fin.PR]*, published 28 May 2026. URL: https://arxiv.org/abs/2605.29309
2. CME Group (2024). "CME CF Bitcoin Reference Rate (BRR) & BRRNY Methodology." URL: https://www.cmegroup.com/trading/cryptocurrency-indices/cf-bitcoin-reference-rate.html
3. iShares by BlackRock (2024–2026). "iShares Bitcoin Trust ETF (IBIT) Daily Holdings Disclosures." URL: https://www.ishares.com/us/products/333011/ishares-bitcoin-trust
