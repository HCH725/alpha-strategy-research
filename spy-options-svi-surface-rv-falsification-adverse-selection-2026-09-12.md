---
schema: strategy-research-record-v1
title: "SPY Options SVI Surface Relative-Value Falsification and Market-Making Adverse Selection Boundary"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - options
  - implied-volatility
  - svi-surface
  - relative-value
  - market-making
  - adverse-selection
  - falsification
status: research-only
confidence: high
source_as_of: 2026-09-11
sources:
  - "https://github.com/palashpawar/spy-vol-surface-mm (commit 77af508b0da4a0207b477193b36bdb23604abb7e, September 2026)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# SPY Options SVI Surface Relative-Value Falsification and Market-Making Adverse Selection Boundary

## Provenance

- **Primary Source Codebase:** Palash Pawar (`palashpawar`), *volsurface-mm: An implied-volatility surface for SPY, built from real option quotes, and a market-making simulator that trades on it*.
- **Canonical Source Identity:** GitHub repository `palashpawar/spy-vol-surface-mm` at immutable commit `77af508b0da4a0207b477193b36bdb23604abb7e`, dated 2026-09-11 18:33:32 UTC.
- **Repository URL:** [https://github.com/palashpawar/spy-vol-surface-mm](https://github.com/palashpawar/spy-vol-surface-mm)
- **Primary Research Files in Repository:**
  - `README.md` — Project specification, headline empirical figures, and negative findings summary.
  - `src/vsmm/surface/prep.py` — Raw quote filtering, forward extraction via put-call parity, inverse vega-width weighting.
  - `src/vsmm/surface/svi.py` — Gatheral raw SVI parametric calibration with analytical no-arbitrage constraints (butterfly and calendar non-crossing).
  - `src/vsmm/signal/relative_value.py` — Relative-value residual signal construction, local model bias detrending, and liquidity/cost gating.
  - `src/vsmm/mm/quoting.py` — SVI fair-value anchored quoting in vol points, inventory skew, and tick floor.
  - `src/vsmm/mm/market.py` — Spot path and implied volatility surface dynamics, sticky-strike spot-vol beta calibration.
  - `src/vsmm/mm/simulator.py` — Exact P&L attribution (spread capture, delta, gamma, skew, vega, theta, residual, hedging costs), markout analysis, and adverse selection breakeven sweep.
  - `scripts/build_figures.py` — End-to-end execution script reproducing all figures, tables, and diagnostics from committed data.
  - `data/raw/cboe_spy_2026-09-10.json.gz` — Full committed snapshot of CBOE SPY delayed option quotes on 2026-09-10 post-close.
- **Source Data As-Of:** 2026-09-10 post-close market snapshot.
- **Repository Deduplication Audit:** Audited all existing markdown records in `alpha-strategy-research`. Zero prior records cite `palashpawar`, `spy-vol-surface-mm`, or the specific SVI relative-value residual falsification and delta-hedged market maker adverse selection boundary model documented here. Related option records (`spxw-0dte-vrp-learning-to-rank-2026-09-01.md`, `option-implied-surface-cremers-weinbaum-skew-crash-regimes-2026-09-02.md`, `crypto-deribit-options-volatility-of-volatility-vov-realized-quarticity-2026-09-01.md`) evaluate directional volatility risk premia or skew crash predictors, none address arbitrage-free SVI surface residual detrending or market-maker adverse selection boundaries on index options.

## Economic mechanism

### Source-reported

The primary research investigates two distinct hypotheses on index option markets:

1. **The Relative-Value Residual Alpha Hypothesis:** Option contracts whose market implied volatilities deviate from a smooth, arbitrage-free parametric implied volatility surface (Gatheral's SVI) represent local mispricings driven by segmented supply and demand imbalances. Selling rich contracts and buying cheap contracts, while delta-hedging the underlying, should capture mean-reverting relative-value edge.
   - *Source finding:* **The hypothesis is falsified.** Across 1,748 contracts exhibiting non-zero residuals from the fitted SVI surface, 95.6% of the residual variance is shared across neighboring strikes—it is smooth SVI model underfit (inability of 5 parameters to bend to the true market smile), not idiosyncratic mispricing. When local model bias is detrended and the physical cost of crossing the bid-ask spread is charged, only 49 contracts survive; after standard liquidity gates, only 5 contracts remain, each yielding a negligible 2 to 3 cents. Trading raw SVI residuals amounts to systematically buying contracts that SVI underfits.
2. **The Market-Making Liquidity Provision Hypothesis:** Because predictability in surface residuals is an illusion, alpha does not reside in predicting where the surface should sit; rather, economic return is earned by being paid the bid-ask spread to provide liquidity around the arbitrage-free surface, provided inventory risk is controlled and adverse selection from informed flow is bounded.
   - *Source finding:* A delta-hedged market maker quoting around SVI fair value captures ~$54,000/session from pure spread in the absence of informed flow. Adverse selection imposes a cost of ~$42,000 per unit of informed fraction ($22,370 ± $8,162 at 60% informed flow). The quoted spread absorbs up to 60% informed order flow before the book becomes unprofitable.

### Research interpretation

The primary source provides a foundational falsification of one of the most common heuristics in retail and semi-institutional options trading—fitting a parametric smile (SVI or SABR) and treating positive/negative residuals as "cheap/rich" trading signals:

- **Parametric Rigidity vs. Market Microstructure:** SVI guarantees absence of static arbitrage (non-negative probability density and absence of calendar arbitrage across total variance slices), but its five degrees of freedom per expiry cannot flex around local clustering of open interest, dealer hedging pockets, or strike-specific hedging demand. The residual is therefore almost purely model specification error. Taking positions against these residuals is negative alpha: the trader is selling options that the model mis-specifies, not options the market misprices.
- **Microstructure Bid-Ask Spread as Information Boundary:** The quoted bid-ask spread in implied volatility space ($iv\_ask - iv\_bid$) represents the market's collective uncertainty about contract value. Attempting to trade discrepancies smaller than the half-spread guarantees negative expected return.
- **Decomposition of Market Maker Economics:** True market making around an arbitrage-free surface relies on three distinct pillars:
  - *Fair value anchor:* The fitted SVI surface provides an unmanipulated baseline unaffected by the last trade or transient quote flickers.
  - *Vol-denominated quoting:* Quoting spreads in volatility points rather than dollars ensures consistent risk pricing across deep OTM wings (low dollar price, high vega sensitivity) and ATM straddles (high dollar price).
  - *Inventory skew & dynamic delta hedging:* Shifting quotes away from accumulated inventory protects against toxic one-sided flow. Markout metrics overestimate adverse selection by a factor of 40 ($273k markout damage vs $6.5k actual paired P&L impact at 15% informed flow) because inventory skew sheds toxic positions well before a standard 30-minute markout window completes.

## Signal

### Relative-Value Signal Construction (Falsified Alpha Signal)

#### Formation Timestamp
- Signal evaluated at post-close option chain snapshot (CBOE delayed quote feed convention, as of 2026-09-10 close) `[source-reported]`.

#### Lookback & Fitting Procedure
- Calibrated cross-sectionally per expiry slice $T$ on out-of-the-money options (puts for $k < 0$, calls for $k > 0$, where log-moneyness $k = \ln(K/F)$) `[source-reported]`.
- Gatheral Raw SVI formulation for total variance $w(k) = \sigma^2(k) \cdot T$:
  $$w(k) = a + b \cdot \left(\rho (k - m) + \sqrt{(k - m)^2 + s^2}\right)$$
  subject to no-arbitrage constraints:
  - $a + b s \sqrt{1 - \rho^2} \ge 0$ (non-negative total variance)
  - $b (1 + |\rho|) < 2$ (Roger Lee wing slope moment formula bounds)
  - $w_{T_1}(k) \le w_{T_2}(k)$ for all $T_1 < T_2$ (calendar non-crossing constraint) `[source-reported]`.
- Weighting: Each empirical IV point is weighted by inverse variance of quote uncertainty: $w_i = \frac{1}{(iv\_ask_i - iv\_bid_i)^2}$ `[source-reported]`.

#### Signal Logic & Detrending
1. **Raw Surface Residual:**
   $$residual\_vol_{i} = iv_i - fitted\_iv_i$$
2. **Local Model Bias Component:**
   $$local\_bias_{i} = \text{rolling\_median}_{window=5}(residual\_vol, \text{ordered by } k)$$
   where `detrend_window = 5` strikes `[source-reported]`.
3. **Idiosyncratic Residual:**
   $$idio\_vol_{i} = residual\_vol_{i} - local\_bias_{i}$$
4. **Normalized Z-score (Relative to Quote Precision):**
   $$z_i = \frac{idio\_vol_i}{\max(iv\_spread_i / 2, 10^{-4})}$$
5. **Cost of Crossing Spread:**
   $$cost\_vol_i = cost\_fraction \times iv\_spread_i$$
   where `cost_fraction = 0.5` `[source-reported]`.
6. **Net Edge After Cost:**
   $$edge\_after\_cost_i = \text{sign}(idio\_vol_i) \times \max(|idio\_vol_i| - cost\_vol_i, 0.0)$$

#### Execution & Tradeability Criteria
An option contract is classified as tradeable only if all gates pass simultaneously:
- $|edge\_after\_cost| > 0$ `[source-reported]`
- $|z| \ge 2.0$ (`min_abs_z = 2.0`) `[source-reported]`
- $vega \ge 5.0$ (`min_vega = 5.0`) `[source-reported]`
- $open\_interest \ge 100$ (`min_open_interest = 100`) `[source-reported]`
- $iv\_spread \le 0.05$ (5 vol points maximum width, `max_iv_spread = 0.05`) `[source-reported]`.

*Empirical verdict:* Only 5 contracts in the entire SPY chain satisfy these conditions, producing an expected edge of only $0.02–$0.03 per contract. The signal is rejected as an economically viable standalone alpha strategy `[source-reported]`.

---

### Market-Maker Liquidity-Provision Signal (Validated Strategy Model)

#### Quoting Engine
- **Fair Value Anchor:** Fitted SVI implied volatility $iv_{fair}(k)$ `[source-reported]`.
- **Half-Spread Specification:** Quoted in volatility points:
  $$half\_spread_{vol} = \text{calibrated from competitor market spreads}$$
  Converted to dollar terms via contract vega: $\Delta P = half\_spread_{vol} \times vega \times 100$, floored at minimum exchange tick ($0.01) `[source-reported]`.
- **Inventory Skew:**
  $$iv_{mid} = iv_{fair} - \gamma_{skew} \times \text{inventory}$$
  Shifting the quote downwards when long vega to deter incoming buy orders and encourage sells `[source-reported]`.
- **Delta Hedging Rule:**
  - Net book delta monitored continuously `[source-reported]`.
  - Rebalancing trigger: When $|\Delta_{net}| > 200$ shares of underlying SPY (`hedge_delta_threshold = 200.0`), rebalance to delta-neutral using underlying shares `[source-reported]`.
  - Hedging cost: 0.5 bps of traded underlying notional (`hedge_cost_bps = 0.5`) `[source-reported]`.

## Required data

- **Instruments:** SPY (SPDR S&P 500 ETF Trust) listed options and underlying SPY equity shares `[source-reported]`.
- **Universe:**
  - *Full surface calibration:* All listed strike prices and expiration dates on SPY options `[source-reported]`.
  - *Market-making quoting universe:* Top 200 contracts ranked by observed trading volume satisfying $vega \ge 5.0$ and time to expiry $T \le 1.0$ year (`universe_size = 200`, `min_vega = 5.0`, `max_T = 1.0`) `[source-reported]`.
- **Venue:** CBOE (Chicago Board Options Exchange) `[source-reported]`.
- **Market Type:** Centralized exchange-traded equity options (American-style options; early exercise boundary verified near the money) and equity shares `[source-reported]`.
- **Timeframe:** Snapshot post-close for calibration; 1-minute time steps for simulated intraday session `[source-reported]`.
- **Fields:**
  - Options: Strike ($K$), expiration date ($T$), call/put bid, ask, bid size, ask size, volume, open interest, implied volatility `[source-reported]`.
  - Underlying: SPY spot price ($S_t$), forward price curve ($F_t$), discount factor curve ($D_t$) `[source-reported]`.
  - Macro / Rates: US Treasury Constant Maturity Treasury (CMT) yield curve for risk-free rates $r(T)$ `[source-reported]`.
- **Missing Data & Cleaning Assumptions:**
  - Drop quotes without valid positive bids/asks or where $bid \ge ask$ `[source-reported]`.
  - Invert implied volatility strictly from out-of-the-money options: puts for $K < F$, calls for $K \ge F$; deep ITM options are discarded to avoid numerical instability and intrinsic-value domination `[source-reported]`.
  - Exclude wing quotes where normalized moneyness exceeds 4 standard deviations `[source-reported]`.

## Execution assumptions

- **Order Types:**
  - *Relative-value strategy:* Aggressive market orders crossing the bid-ask spread (paying $0.5 \times iv\_spread$) `[source-reported]`.
  - *Market maker:* Passive limit orders posted at bid and ask; underlying delta hedge executed via aggressive market orders at 0.5 bps transaction cost `[source-reported]`.
- **Fill Model:**
  - Fills occur according to Poisson arrival processes calibrated to empirical contract activity (volume and open interest) `[source-reported]`.
  - Fill probability conditioned on whether the posted quote improves or matches prevailing market quotes `[source-reported]`.
- **Adverse Selection Flow Parameterization:**
  - Order flow is partitioned into uninformed liquidity-demanding flow (random direction) and informed flow (orders positioned in the direction of subsequent 30-minute spot and implied volatility moves) `[source-reported]`.
  - Informed fraction parameter $\alpha_{inf} \in [0.0, 0.60]$ evaluated across 12 independent simulation paths `[source-reported]`.
- **Underlying Market Dynamics & Spot-Vol Beta:**
  - Underlying path generated with sticky-strike implied volatility behavior: a 2.08% decline in spot price moves implied volatilities down by 1.9 vol points along the downward-sloping skew `[source-reported]`.
- **Capacity & Limits:**
  - Net delta constrained by 200-share rebalancing band `[source-reported]`.
  - Gross vega exposure constrained by inventory skew; without inventory skew, single-minute smile shifts of 0.1 vol point can inflict $90,000 drawdown on a 30,000-contract book `[source-reported]`.

## Evidence

### Source-reported

All metrics below trace directly to Palash Pawar's repository (`palashpawar/spy-vol-surface-mm`, commit `77af508b0da4a0207b477193b36bdb23604abb7e`, `README.md`, `scripts/build_figures.py`, `src/vsmm/signal/relative_value.py`, `src/vsmm/mm/simulator.py`):

1. **Option Chain & Forward Extraction Diagnostics (SPY Snapshot 2026-09-10):**
   - Raw quotes received: **13,296**.
   - Clean usable quotes after filtering: **4,535**.
   - Expiries calibrated: **32 slices**, spanning 4 days to 2.3 years.
   - Near-the-money call-put IV gap ($|k| < 0.08, vega > 25$): **−0.0035 vol points** median, confirming unbiased forward price identification.
   - SVI calibration fit error: **0.127 vol points** median RMSE, **0.326 vol points** maximum RMSE.
   - Static arbitrage violations: **0 butterfly arbitrage violations**, **0 calendar arbitrage violations**.

2. **Relative-Value Surface Residual Falsification:**
   - Total contracts evaluated: 1,748.
   - **Local model bias share:** **95.6%** of residual variance is shared with neighboring strikes ($window = 5$), proving residuals represent parametric SVI stiffness rather than market mispricing.
   - Contracts with raw positive edge: 1,748.
   - Contracts surviving spread crossing cost ($cost = 0.5 \times iv\_spread$): **49 contracts** (2.8% survival rate).
   - Contracts surviving full liquidity and statistical gates ($|z| \ge 2.0$, $vega \ge 5.0$, $OI \ge 100$, $spread \le 0.05$): **5 contracts** (0.29% of universe).
   - Expected economic edge on surviving contracts: **$0.02 to $0.03 per contract** (falsified as economically unviable after real-world execution frictions).

3. **Market-Making Simulator & Adverse Selection Attribution:**
   - Baseline performance (0% informed flow): Book earns **~$54,000 per session**, driven almost entirely by spread capture ($spread\_capture$).
   - Adverse selection cost rate: **~$42,000 per unit of informed fraction**.
   - Performance at 60% informed flow: Adverse selection costs **$22,370 ± $8,162**, absorbing virtually all quoted spread.
   - **Breakeven boundary:** The quoted spread supports up to **~60% informed flow** before the market-making strategy turns structurally net-negative.
   - **Markout divergence:** At 15% informed flow, standard 30-minute markout suggests $273,000 of damage, whereas actual paired session P&L difference is only **$6,500** (markout overstates true damage by a factor of 40 because inventory skew sheds toxic positions rapidly).

### Independently reproduced

`Not independently reproduced.` All quantitative findings, calibration statistics, and simulation results represent primary research published by Palash Pawar in GitHub repository `palashpawar/spy-vol-surface-mm` (commit `77af508b0da4a0207b477193b36bdb23604abb7e`). No internal reproduction on our own execution engine has been performed.

### Negative evidence

- **Decisive Falsification of Relative-Value SVI Residual Alpha:** Gathering residuals from parametric volatility surface fitting does not produce tradable alpha. 95.6% of residual variance is shared local error; only 5 contracts out of 1,748 survive trading frictions, with negligible cents-level edge.
- **Competitor Quote Freeze Distortion:** In naive backtesting setups where competitor market quotes remain fixed while theoretical fair value moves with spot, simulated makers artificially generate thousands of fictitious fills.
- **Oversized Inventory Skew Inversion:** Setting absolute inventory skew too wide relative to quoted half-spread causes the maker to quote straight through fair value, generating arithmetically negative spread capture.
- **Informed Flow Definition Trap:** Defining informed flow as "buying contracts worth more in 30 minutes" causes informed agents to simply sell the entire chain due to dominant theta decay, turning adverse selection into an artificial profit driver unless properly conditioned on underlying direction.
- **Spot-Vol Leverage Effect Requirement:** Neglecting spot-vol correlation (sticky-strike downward skew) inverts vega P&L during sell-offs, causing a short-put position to report an illusory vega profit.

## Falsification plan

To further stress-test or potentially overturn the conclusions of this research, the following empirical tests are proposed:

1. **Multi-Horizon Residual Persistence & Time-Series Auto-Correlation Test (research-proposed):**
   - *Test:* Collect daily post-close SPY option chains over a 12-month rolling window (252 sessions). Track the 5 candidate contracts flagged as having idiosyncratic edge.
   - *Decision Rule:* If the idiosyncratic residual $idio\_vol$ exhibits an AR(1) auto-correlation $< 0.10$ and cumulative trading P&L net of exchange fees is $\le 0$, the rejection of relative-value residual alpha is confirmed `[research-defined falsification threshold]`.
2. **Flexible Non-Parametric Surface Specification (research-proposed):**
   - *Test:* Re-fit the volatility surface using Surface SVI (SSVI) or a Neural SDE / spline with penalty constraints that allow local curvature while preserving no-arbitrage bounds.
   - *Decision Rule:* If a more flexible surface reduces the local model bias from 95.6% to $< 10\%$ without increasing the count of tradeable contracts beyond 10, confirm that the original residuals were 100% parametric artifacts `[research-defined falsification threshold]`.
3. **Severe Adverse Selection Stress Test (research-proposed):**
   - *Test:* Stress-test the market-making engine under a 75% informed order flow regime with jump-diffusion spot paths.
   - *Decision Rule:* If net session P&L drops below −$15,000 per session across $\ge 80\%$ of simulated paths, the market-making quoting rules are falsified as insufficiently defensive for stressed volatility regimes `[research-defined falsification threshold]`.

## Crypto portability

- **Portability Status:** `adapted` / `unproven`
- **Research Interpretation:** The core findings originate from traditional US equity index options (CBOE SPY) and must not be treated as empirical crypto evidence without explicit verification on cryptocurrency derivatives.
- **Crypto-Specific Considerations for Deribit BTC/ETH Options:**
  - *Contract Specification (European vs American):* Deribit options are European-style, which actually simplifies SVI calibration by eliminating early exercise boundaries and American put discounts.
  - *Inverse / Coin-Margined Settlement:* Deribit BTC and ETH options settle in the underlying cryptocurrency rather than USD or stablecoins. This introduces an inherent non-linear currency risk (underlying coin value changes while holding option inventory), requiring continuous crypto-to-USD basis hedging that does not exist in SPY.
  - *Wider Bid-Ask Spreads:* Deribit option chains exhibit substantially wider bid-ask spreads (frequently 2.0 to 8.0 vol points wide, compared to 0.1–0.5 vol points on SPY). Because 95.6% of SVI residuals are inside the spread even on SPY, relative-value SVI residual trading on crypto options is virtually certain to be completely extinguished by bid-ask friction.
  - *24/7 Session & Jumps:* Absence of market closes means crypto options do not have distinct overnight auction marks; continuous jump risk and weekend illiquidity create extreme adverse selection risks for automated market makers.
  - *Fragmented Liquidity:* Crypto options liquidity is dominated by Deribit (~80% market share), with smaller fragments on Binance, OKX, and decentralized protocols (e.g., Derive, Aevo).

## Limitations

- **Single Snapshot Limitation:** The empirical surface fit and relative-value residual diagnostics are derived from a single comprehensive post-close snapshot (`2026-09-10`). While all 4,535 contracts across 32 expiries are evaluated, multi-day temporal stability cannot be measured from a single cross-section.
- **Simulated Intraday Flow:** The market-making simulation relies on synthetic order flow and simulated spot paths calibrated to snapshot parameters rather than a tick-by-tick order book tape (OPRA/CBOE Level 3 feed).
- **Assumed Market Dynamics:** Intraday vol-of-vol, realized-to-implied ratio, and informed flow fractions are parameter assumptions rather than directly observed quantities.
- **Capacity & Prime Brokerage Frictions:** Margin requirements under Portfolio Margin (OCC) vs Reg-T, financing rates, and exchange clearing fees are simplified.

## Implementation status

`not-implemented`. No implementation in our research stack (PyBroker, NautilusTrader, or live execution engines) has been conducted.

## Adoption boundary

This record is research material only. Presence in this repository does not indicate:
- Strategy profitability;
- Validated alpha;
- Approval for implementation;
- Approval for paper trading, testnet, or live trading.

## Related Wiki records

- `[[quant/option-implied-surface-cremers-weinbaum-skew-crash-regimes-2026-09-02]]` — Evaluates options implied volatility surface skew for directional equity crash regimes; contrasting use of implied volatility surface (directional macro risk vs relative-value arbitrage).
- `[[quant/spxw-0dte-vrp-learning-to-rank-2026-09-01]]` — Evaluates short-dated index option volatility risk premium; operational differences between 0DTE directional selling and multi-tenor delta-hedged market making.
- `[[quant/crypto-deribit-options-volatility-of-volatility-vov-realized-quarticity-2026-09-01]]` — Evaluates Deribit crypto options volatility-of-volatility mispricings; relevant for adapting SVI calibration to crypto options.
- `[[quant/options-statistical-arbitrage-graph-learning-synthetic-long-2026-09-02]]` — Evaluates graph neural network statistical arbitrage on options; contrasting non-parametric machine learning approaches against parametric SVI surface fitting.
- `[[quant/crypto-perpetual-pairs-trading-kalman-cointegration-falsification-2026-09-11]]` — Precedent for rigorous empirical falsification of common quantitative trading heuristics after transaction costs.

## Sources

1. **Primary Codebase & Research:** Palash Pawar (`palashpawar`). *volsurface-mm: An implied-volatility surface for SPY, built from real option quotes, and a market-making simulator that trades on it*, GitHub repository `palashpawar/spy-vol-surface-mm`, commit `77af508b0da4a0207b477193b36bdb23604abb7e`, dated 2026-09-11 18:33:32 UTC. URL: [https://github.com/palashpawar/spy-vol-surface-mm](https://github.com/palashpawar/spy-vol-surface-mm).
2. **Empirical Dataset:** CBOE SPY Option Chain Snapshot, 2026-09-10 post-close, committed in repository at `data/raw/cboe_spy_2026-09-10.json.gz`.
3. **Parametric Formulation Reference:** Jim Gatheral (2004), *A parsimonious arbitrage-free implied volatility parameterization with application to the valuation of volatility derivatives*, presentation at Global Derivatives 2004; Gatheral & Jacquier (2014), *Arbitrage-free SVI volatility surfaces*, Quantitative Finance 14(1): 59–71.
