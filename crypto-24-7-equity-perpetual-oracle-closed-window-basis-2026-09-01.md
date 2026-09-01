---
schema: strategy-research-record-v1
title: 24/7 Equity-Perpetual Oracle Closed-Window Observational Equivalence and Cash-Reopen Basis Convergence
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - equity-perpetuals
  - oracle-pricing
  - price-discovery
  - basis-arbitrage
  - market-microstructure
  - closed-window-mark
status: research-only
confidence: high
source_as_of: 2026-08-10
sources:
  - https://arxiv.org/abs/2608.09188
  - https://doi.org/10.48550/arXiv.2608.09188
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# 24/7 Equity-Perpetual Oracle Closed-Window Observational Equivalence and Cash-Reopen Basis Convergence

## Provenance

- **Primary Academic Source:** Donghwa Seo, Doohwi Cha, Seunghan Son, Juyeong Lee, Minjae Lee, and Minsuk Sung, "When Cross-Venue Agreement Is Not Price Discovery: Disclosure Frontiers for 24/7 Equity-Perpetual Oracles," *arXiv preprint arXiv:2608.09188v1* [q-fin.TR / q-fin.CP], August 10, 2026. DOI: [10.48550/arXiv.2608.09188](https://doi.org/10.48550/arXiv.2608.09188).
- **Data Sample:** An eight-week panel of continuous high-frequency order-book and mark data for crypto-listed 24/7 equity perpetual futures (e.g., synthetic US single-stock and index contracts) across multiple crypto derivative venues during deep-closed cash market windows (overnight, weekends, market holidays) and cash market reopenings.

## Economic mechanism

### Source-reported

Seo et al. (2026) investigate the pricing and oracle mechanics of **24/7 equity perpetual futures** traded on cryptocurrency platforms while primary cash equity exchanges (NYSE / Nasdaq) are closed:
1. **The Closed-Window Oracle Problem:** When underlying cash markets are closed, crypto exchanges must construct "mark prices" (used for funding rate calculations, margin valuation, and liquidation triggers) in the absence of continuous spot price discovery.
2. **Oracle Operator Fixed Point:** The authors mathematically model the closed-window mark price as the fixed point of an oracle operator $T$:
   $$M_t = T(M_t) = W_{\text{ext}} P_{\text{anchor}} + W_{\text{peer}} M_t + \epsilon_t$$
   which linearly combines stale external cash market anchors $P_{\text{anchor}}$ (e.g., Friday close prices) with self- and peer-derivative exchange references $W_{\text{peer}} M_t$.
3. **Observational Equivalence & Failure of Price Discovery Estimators:** The authors prove that from observed mark prices and public proxies alone, external anchoring and peer circular referencing are observationally equivalent. Standard empirical price discovery metrics—such as Hasbrouck Information Share (IS), Gonzalo-Granger Permanent-Transitory (PT) components, and lead-lag Granger causality—fail because the reduced-form covariance matrices admit an infinite family of structural topology decompositions.
4. **Illusion of Cross-Venue Consensus:** High cross-venue correlation and tight bid-ask alignment during closed windows do **not** reflect genuine informed price discovery. Rather, they represent an artifact of circular oracle coupling.
5. **Cash-Reopen Validation:** Upon cash market reopening (Monday 09:30 EST / pre-market 04:00 EST), true fundamental price discovery resolves the equivalence class, triggering sharp basis adjustments and exposing closed-window mark distortions.

### Research interpretation

This finding motivates a **Closed-Window Oracle Mispricing & Cash-Reopen Basis Arbitrage Strategy**:
1. **Circular Consensus Exploitation:** During weekend and overnight closed windows, retail and automated sentiment flows push crypto equity perpetuals into excessive premiums or discounts relative to fundamental news, amplified by circular peer oracle averaging.
2. **Predictable Cash-Reopen Basis Convergence:** Because the closed-window mark is an unanchored fixed point, the spread between the crypto perpetual price $P_{\text{perp},t}$ and the true expected cash opening price $E[P_{\text{cash},\text{open}}]$ (estimated via after-hours index futures, correlated ADRs, or overnight macro proxies) represents pure mispricing.
3. **Pre-Reopen Position Accumulation & Post-Reopen Convergence:** Taking contrarian positions against extreme closed-window perpetual deviations yields high-Sharpe basis convergence upon cash market opening bell, capturing the sudden collapse of artificial oracle basis.

## Signal

The trading signal identifies structural divergence between circular closed-window equity perpetual marks and external overnight macro-asset proxies:

1. **Closed-Window Regime Indicator:**
   - Define trading session state:
     $$S_{\text{session}}(t) = \begin{cases} 1 & \text{if primary cash equity market is CLOSED (Weekends, 20:00 - 04:00 EST weekdays, holidays)} \\ 0 & \text{if primary cash equity market is OPEN} \end{cases}$$

2. **Synthetic Fundamental Proxy Estimation ($P_{\text{proxy},t}$):**
   - During $S_{\text{session}}(t) = 1$, construct an independent benchmark for the underlying equity $i$ using continuous 24/5 CME E-mini futures ($F_{\text{ES}}, F_{\text{NQ}}$) and international correlated proxies:
     $$\hat{P}_{\text{fund},i,t} = P_{\text{close},i} \cdot \left( 1 + \beta_{i,\text{index}} \cdot r_{\text{index},t} + \Delta_{\text{macro},t} \right)$$
     where $r_{\text{index},t}$ is the return of the relevant index future since cash market close.

3. **Closed-Window Oracle Basis Spread ($Z_{\text{basis},t}$):**
   - Compute the standardized percentage basis between the crypto equity perp price $P_{\text{perp},i,t}$ and the fundamental proxy:
     $$\text{Basis}_{i,t} = \frac{P_{\text{perp},i,t} - \hat{P}_{\text{fund},i,t}}{\hat{P}_{\text{fund},i,t}}$$
     $$Z_{\text{basis},i,t} = \frac{\text{Basis}_{i,t} - \mu_{\text{basis},W}}{\sigma_{\text{basis},W}}$$
     over rolling lookback window $W = 72\text{ hours}$.

4. **Entry and Exit Logic:**
   - **Short Perp Entry:** If $S_{\text{session}}(t) = 1$ and $Z_{\text{basis},i,t} > +2.0$ (crypto perp trading at artificial circular premium):
     - Sell crypto equity perpetual $i$ at market/TWAP.
     - (Optional) Long equivalent CME index future or correlated proxy to maintain delta neutrality.
   - **Long Perp Entry:** If $S_{\text{session}}(t) = 1$ and $Z_{\text{basis},i,t} < -2.0$ (crypto perp trading at artificial circular discount):
     - Buy crypto equity perpetual $i$ at market/TWAP.
   - **Exit / Convergence:**
     - Primary exit occurs at $t_{\text{reopen}} + 15\text{ min}$ following primary cash market open (09:45 EST).
     - Stop-loss: $|Z_{\text{basis},i,t}| > 3.5$ or cumulative loss $> 2.5\%$.

## Required data

- **Instruments:** 24/7 crypto-listed equity perpetuals (e.g., NVDA-PERP, AAPL-PERP, TSLA-PERP, SPY-PERP) and CME E-mini equity index futures (ES, NQ).
- **Venues:** Crypto perpetual exchanges (e.g., Hyperliquid, dYdX, Binance, Bybit) + CME Globex market feed for after-hours futures.
- **Timeframe:** 1-minute and 5-minute OHLCV, order-book depth, and mark price feeds.
- **Fields:** Crypto perp mark price, perp index price, funding rate, CME Globex index futures prices, primary exchange official closing prices ($P_{\text{close}}$).

## Execution assumptions

- **Timing:** Position entry accumulated during closed-market hours (Friday night through Sunday night); execution closed within 15–30 minutes of Monday morning cash open.
- **Order Types:** TWAP / limit orders during low-liquidity weekend sessions; market-on-open (MOO) or immediate TWAP exit upon cash reopen.
- **Transaction Costs:** 2 to 5 bps per trade on crypto perpetual venues; perpetual funding rate paid/received over weekend holding period.
- **Slippage / Liquidity:** Conservative slippage buffer of 10 to 20 bps for thin weekend crypto equity perp books.

## Evidence

### Source-reported

All empirical and analytical findings below are directly reported by Seo, Cha, Son, Lee, Lee, and Sung (arXiv:2608.09188v1, 2026):
1. **Observational Equivalence Theorem:** Formally proved that mark prices generated by linear oracle combinations of external anchors and peer derivatives are observationally equivalent to infinitely many distinct network topologies, invalidating unconstrained lead-lag price discovery metrics during closed windows.
2. **Empirical Panel Analysis:** Across an 8-week panel of crypto equity perpetuals during deep-closed windows, cross-venue mark correlations exceeded 0.98, yet these shared movements decoupled significantly from after-hours fundamental proxies.
3. **Cash-Reopen Basis Correction:** At the exact moment of primary cash market reopening, closed-window basis spreads experienced rapid mean-reversion, validating that weekend cross-venue consensus was driven by oracle feedback rather than authentic information discovery.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- None identified in the reviewed source; absence is not evidence of no negative result.
- Crypto equity perpetual contracts on certain venues have capped position limits and higher maintenance margin requirements over weekends, which can restrict position sizing.

## Falsification plan

1. **Ablation vs Random Walk Reopen:** Test whether the direction of the weekend basis spread $\text{Basis}_{i,t}$ predicts the sign and magnitude of the cash market reopening return gap. If the basis does not predict cash reopen convergence with $t\text{-stat} > 2.5$ across $> 50$ weekend reopen events, the oracle mispricing hypothesis is falsified.
2. **Funding Cost Erosion Test:** Measure net strategy returns after subtracting cumulative weekend funding rate fees paid on the perpetual leg. If funding payments exceed the reopening basis convergence margin, the strategy is unviable.
3. **Disclosure Frontier Verification:** If crypto exchanges adopt fully transparent, non-circular oracle architectures with dynamic proxy weighting, the closed-window basis mispricing will compress to zero.

## Crypto portability

- **Direct:** The strategy specifically exploits the unique market structure of 24/7 crypto perpetual exchanges offering synthetic contracts on traditional off-chain assets with restricted cash trading hours.
- **Crypto-specific factors:** 24/7 continuous trading in crypto directly conflicts with 09:30–16:00 EST traditional equity market hours, creating structural oracle lag and feedback loops unique to crypto derivative venues.

## Limitations

- **Emerging Asset Class:** 24/7 crypto equity perpetuals are a rapidly evolving instrument category with lower liquidity than standard crypto native assets (BTC, ETH).
- **Exchange Rule Changes:** Venues may adjust oracle mark calculation formulas, funding interval caps, or weekend leverage limits dynamically.
- **Gap Risk:** Severe corporate news events (e.g., unexpected weekend earnings or regulatory announcements) can produce large fundamental gaps that exceed normal proxy estimation bounds.

## Implementation status

No implementation in our research stack has been completed. Not implemented in PyBroker or NautilusTrader.

## Adoption boundary

Research material only. A record being present in this repository does not mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

## Related Wiki records

- `commodity-perpetual-oracle-roll-funding-arbitrage-2026-09-01.md`
- `crypto-cross-platform-binary-threshold-mispricing-polymarket-binance-2026-09-01.md`
- `crypto-perpetual-spot-cross-venue-lead-lag-vecm-2026-09-01.md`
- `crypto-futures-cross-sectional-basis-momentum-slope-2026-08-31.md`

## Sources

1. Donghwa Seo, Doohwi Cha, Seunghan Son, Juyeong Lee, Minjae Lee, and Minsuk Sung, "When Cross-Venue Agreement Is Not Price Discovery: Disclosure Frontiers for 24/7 Equity-Perpetual Oracles," *arXiv preprint arXiv:2608.09188v1* [q-fin.TR / q-fin.CP], August 10, 2026.
   - DOI: https://doi.org/10.48550/arXiv.2608.09188
   - arXiv: https://arxiv.org/abs/2608.09188
