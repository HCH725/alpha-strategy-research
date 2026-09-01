---
schema: strategy-research-record-v1
title: "Bitcoin Options Dealer Gamma Exposure (GEX) Volatility Regime Signal"
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - options
  - gamma-exposure
  - dealer-hedging
  - volatility-regime
  - bitcoin
  - deribit
status: research-only
confidence: medium
source_as_of: 2026-09-01
sources:
  - https://github.com/VedantUpasani46/Alpha-Research-Discovery/blob/master/alpha_27_dealer_gex.py
  - Garleanu, Pedersen & Poteshman (2009) "Demand-Based Option Pricing" — RFS
  - SpotGamma Research (2021) "The GEX Framework"
  - Dew-Becker et al. (2021) "Variance, Skewness, and the Cross-Section"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Options Dealer Gamma Exposure (GEX) Volatility Regime Signal

## Provenance

- **Primary Source:** VedantUpasani46/Alpha-Research-Discovery, alpha_27_dealer_gex.py, master branch, GitHub.
- **Academic References:** Garleanu, Pedersen & Poteshman (2009) "Demand-Based Option Pricing" (RFS); SpotGamma Research (2021) "The GEX Framework"; Dew-Becker et al. (2021) "Variance, Skewness, and the Cross-Section."
- **Data Source:** Deribit BTC options open interest by strike, combined with Black-Scholes gamma computation at current market conditions.
- **Source-reported Concept:** Options market makers (dealers) mechanically hedge their gamma exposure by buying as price rises (when short gamma) or selling as price rises (when long gamma), creating predictable volatility regimes.

## Economic mechanism

### Source-reported

When a dealer SELLS a call option to a client:
- The dealer is SHORT gamma (convex loss exposure)
- To hedge: dealer BUYS as price rises, SELLS as price falls
- This is AMPLIFYING — dealers chase price moves, increasing volatility
- Short gamma regime: higher volatility, trending behavior

When a dealer BUYS a call option from a client (sells a put):
- The dealer is LONG gamma (convex profit exposure)
- To hedge: dealer SELLS as price rises, BUYS as price falls
- This is DAMPENING — dealers push price back toward strike levels
- Long gamma regime: lower volatility, mean-reverting behavior, PINNING

The GEX (Gamma Exposure) signal quantifies this:
- Positive GEX → dealers are long gamma → they suppress volatility → BUY signal (vol compression → carry)
- Negative GEX → dealers are short gamma → they amplify moves → FADE signal (trend exhaustion risk)

### Research interpretation

This is a **structural volatility regime signal** derived from options market microstructure:

1. **Dealer Hedging Flows as Predictable Force:** Unlike directional sentiment, dealer gamma hedging is mechanical and deterministic — dealers MUST hedge to remain delta-neutral. This creates predictable buy/sell pressure that amplifies or dampens price moves depending on the gamma regime.

2. **Volatility Regime Classification:** The GEX signal classifies the market into two regimes:
   - **Long Gamma (Positive GEX):** Dealers suppress volatility, creating mean-reverting, range-bound conditions. Favor mean-reversion strategies, range trading, and short volatility positions.
   - **Short Gamma (Negative GEX):** Dealers amplify volatility, creating trending, breakout conditions. Favor momentum strategies, trend following, and long volatility positions.

3. **Pin Risk at Expiration:** Near options expiration, large open interest strikes act as "gravitational attractors" — dealers mechanically hedge toward these levels, causing price to pin near high-OI strikes. This is exploitable for short-horizon mean reversion.

4. **Crypto-Specific Adaptation:** Bitcoin options on Deribit represent >90% of global crypto options open interest. The GEX signal can be computed from Deribit's public API without authentication, making it accessible for systematic trading.

## Signal

The normalized quantitative signal:

1. **GEX Computation:**
   At daily snapshot timestamp $t$ (08:00 UTC Deribit settlement cutoff):
   $$GEX_t = \sum_i \left[ OI_{call,i} \times \Delta_{call,i} \times \Gamma_{call,i} - OI_{put,i} \times \Delta_{put,i} \times \Gamma_{put,i} \right] \times 100 \times S_t$$
   where:
   - $S_t$ = current BTC price (dollar-weighted)
   - $\Gamma$ = Black-Scholes gamma at current market conditions
   - $OI$ = open interest by strike
   - $\Delta$ = option delta

2. **Proxy Computation (when full strike-level OI unavailable):**
   $$GEX_{proxy} = OI_{call,ATM} \times \Gamma_{ATM} \times S - OI_{put,ATM} \times \Gamma_{ATM} \times S$$

3. **Signal Formation:**
   $$GEX_{7dEMA} = EMA(GEX_{daily}, span=7)$$
   $$\alpha_{GEX} = sign(GEX_{7dEMA}) \times rank(|GEX_{7dEMA}|)$$

4. **Trading Rule:**
   - **Positive GEX (Long Gamma):** Dealers suppress volatility → regime filter for mean-reversion strategies; reduce position sizing for trend strategies.
   - **Negative GEX (Short Gamma):** Dealers amplify volatility → regime filter for momentum/trend strategies; increase position sizing for breakout signals.
   - **GEX Magnitude:** Rank cross-sectionally to determine relative conviction across assets (if multi-asset).

5. **Holding Horizon:** Daily rebalance at 08:00 UTC; signal persistence typically 3-7 days.

6. **Pin Risk Signal (near expiry):**
   When days-to-expiry < 3 and large OI concentration exists at a strike:
   $$PinSignal_t = \frac{|S_t - K_{maxOI}|}{ATR_t}$$
   Small values indicate price is being pinned → fade moves away from $K_{maxOI}$.

## Required data

- **Venue:** Deribit options market.
- **Instrument Set:** BTC European cash-settled options across the full expiration schedule.
- **Data Fields:**
  - Open interest by strike and expiration (from Deribit public API: `GET /public/get_book_summary_by_currency`)
  - Implied volatility by strike (from Deribit order book: `GET /public/get_order_book`)
  - Underlying BTC spot/index price
  - Option Greeks (gamma, delta) computed via Black-Scholes from IV and strike
- **Timeframe:** Daily snapshots at 08:00 UTC (Deribit settlement cutoff).
- **Timestamp:** UTC required; Deribit uses UTC natively.
- **Missing-Data Assumptions:** Full strike-level OI may not be available for all expirations; proxy computation using ATM options is a fallback.

## Execution assumptions

- **Signal-to-Order Timing:** Signal computed at 08:00 UTC; execution at next available liquidity window.
- **Execution Model:** Signal is a volatility regime filter, not a direct directional signal. It overlays other alpha signals to adjust sizing or strategy selection.
- **Fees:** Deribit taker fee ~0.04%; maker rebate ~0.02%.
- **Slippage:** Minimal for BTC options on Deribit (deep liquidity for ATM and near-ATM strikes).
- **Capacity:** GEX is a regime signal, not a position-taking signal — capacity is not directly constrained by GEX computation.
- **Leverage:** Not applicable (regime filter).
- **Latency:** Daily computation; no HFT requirements.
- **Partial Fills:** Not applicable.

## Evidence

### Source-reported

- SpotGamma (2021) reports that GEX accurately classified volatility regimes in US equity options from 2019-2021, with positive GEX periods showing 30-50% lower realized volatility than negative GEX periods.
- Garleanu, Pedersen & Poteshman (2009) provide theoretical foundation showing that demand-based option pricing creates predictable hedging flows.
- Dew-Becker et al. (2021) document that variance and skewness are priced in the cross-section, supporting the idea that volatility regime signals have alpha.
- The source code (alpha_27_dealer_gex.py) implements the full pipeline but does not report specific backtest results for crypto.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The GEX signal is a volatility regime classifier, not a directional return predictor. It may not generate standalone alpha without combination with other signals.
- In crypto, options market structure differs from equities: Deribit is a single dominant venue, and dealer hedging may be less mechanical than in equity markets where market makers have obligations.
- The proxy computation (ATM-only) may miss significant GEX from deep OTM options.
- Near expiry, GEX computation becomes sensitive to rapid OI changes.

## Falsification plan

1. **Regime Classification Test:** Compute realized volatility under positive vs negative GEX regimes over 2021-2025. Positive GEX should show statistically significantly lower realized vol (one-sided t-test, p < 0.05).
2. **Lead-Lag Regression:** Regress next-day realized vol on current GEX level. Negative coefficient expected (higher GEX → lower future vol).
3. **Crisis Test:** Verify GEX went sharply negative before major BTC drawdowns (e.g., March 2020, May 2021, November 2022).
4. **Ablation:** Test GEX as standalone signal vs. as regime filter for other strategies. If GEX alone has no alpha, it confirms the signal is a regime classifier, not a return predictor.
5. **Out-of-Sample:** Walk-forward validation across 2021-2025 with annual retraining.
6. **Cost Sensitivity:** Test whether regime-filtered strategies outperform unfiltered strategies after 0.1% round-trip costs.

## Crypto portability

adapted

The GEX concept originates from equity options market structure (Citadel Securities, SpotGamma). Crypto adaptation via Deribit is plausible because:
- Deribit represents >90% of global crypto options OI
- BTC options have sufficient liquidity for meaningful GEX computation
- Dealer hedging mechanics are similar (delta-neutral market makers)

Crypto-specific portability risks:
- Deribit is a single venue (no cross-venue GEX aggregation)
- BTC options have fewer expirations than equity index options
- Crypto market makers may hedge differently (e.g., via perpetual futures rather than spot)
- 24/7 trading means GEX regime can shift intraday
- Funding rate dynamics on perps may interact with GEX signals

## Limitations

- not independently reproduced
- underspecified (proxy computation details for full strike-level GEX from Deribit API need implementation)
- The signal is a volatility regime classifier, not a standalone alpha generator
- Crypto options market structure differs from equities — dealer hedging mechanics may be less mechanical
- Near-expiry pin risk signal requires high-frequency OI data

## Implementation status

not-implemented

## Adoption boundary

This record is research material only. A record being present in this repository does not mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

## Related Wiki records

- [[bitcoin-options-implied-volatility-risk-reversal-skew-2026-09-01]]
- [[crypto-convolutional-vae-volatility-surface-completion-anomaly-2026-09-01]]
- [[crypto-options-implied-correlation-dispersion-2026-08-31]]
- [[crypto-options-volatility-risk-premium-zscore-2026-08-31]]

## Sources

1. VedantUpasani46/Alpha-Research-Discovery, alpha_27_dealer_gex.py, master branch. https://github.com/VedantUpasani46/Alpha-Research-Discovery
2. Garleanu, N., Pedersen, L.H. & Poteshman, A.M. (2009). "Demand-Based Option Pricing." Review of Financial Studies, 22(10), 4259-4299.
3. SpotGamma Research (2021). "The GEX Framework." https://spotgamma.com
4. Dew-Becker, I., Giglio, S., Kelly, B. & Stroebel, J. (2021). "Variance, Skewness, and the Cross-Section of Stock Returns." Working Paper.
5. Deribit Public API Documentation. https://docs.deribit.com
