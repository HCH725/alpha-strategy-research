---
schema: strategy-research-record-v1
title: "Extreme Value Alpha and Crash Risk: Separating Structural Tails from Lottery Tails with LLM-Extracted Disclosure Networks"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - extreme-value-theory
  - lottery-stocks
  - max-anomaly
  - disclosure-networks
  - llm-information-extraction
  - tail-risk
  - crash-risk
  - cross-sectional-equity
status: research-only
confidence: medium
source_as_of: 2026-08-10
sources:
  - https://arxiv.org/abs/2608.09089
  - https://arxiv.org/html/2608.09089v1
  - https://doi.org/10.48550/arXiv.2608.09089
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Extreme Value Alpha and Crash Risk: Separating Structural Tails from Lottery Tails with LLM-Extracted Disclosure Networks

## Provenance

- **Primary Source:** Lin Zhang and Fan Yang, *"Extreme Value Alpha and Crash Risk: Separating Structural Tails from Lottery Tails with LLM-Extracted Disclosure Networks"*, arXiv preprint `arXiv:2608.09089v1 [q-fin.ST, q-fin.PM, cs.AI]`, submitted 10 August 2026. DOI: `10.48550/arXiv.2608.09089`. Stable URL: `https://arxiv.org/abs/2608.09089`. Full-text HTML: `https://arxiv.org/html/2608.09089v1`.
- **Underlying Measurement Framework:** Consumes the point-in-time latent graph measurement pipeline established in Fan Yang and Lin Zhang (2026), *"LLM latent edge measurement: Point-in-time economic graphs for quantitative investing from corporate disclosures"*, arXiv preprint `arXiv:2607.15640`.
- **Repository Deduplication:** Repository-wide inspection on 2026-09-04 confirmed that `arXiv:2608.09089`, `arXiv:2607.15640`, and authors Lin Zhang and Fan Yang do not appear in any existing record. Existing network and text records in the repository (`supply-chain-network-augmented-llm-text-embeddings-nale-2026-09-04.md`, `mingle-exposure-locality-factor-graph-portfolio-diversification-2026-09-02.md`) focus on supply-chain GNN embeddings or factor-graph covariance regularization. This record uniquely formalizes the decomposition of extreme return distributions (Extreme Value Theory upper-tail heat) into behavioral lottery vs. fundamental structural regimes via an exact birth/death/drift decomposition of corporate disclosure networks.

## Economic mechanism

### Source-reported

The authors address a fundamental tension between empirical asset pricing and historical growth anomalies:
1. **The Lottery Anomaly:** The lottery-stock literature (Bali, Cakici, & Whitelaw, 2011; Barberis & Huang, 2008) demonstrates that stocks with extreme recent upside (e.g., high maximum daily returns, MAX) systematically underperform. Cumulative prospect theory and preference for positive skewness lead retail investors to overpay for transient lottery payoffs, resulting in a persistent negative expected return (the MAX discount).
2. **The Structural Winner Anomaly:** In direct contrast, historical extreme multi-bagger winners (e.g., NVIDIA) almost universally exhibit persistent, heating upper return tails before and throughout their major expansionary runs. A strategy mechanically screening out all stocks with hot upper tails avoids lottery losers but simultaneously forfeits the market's defining secular winners.
3. **The Crash Signature Paradox:** Crash risk literature (Chen, Hong, & Stein, 2001; Hutton, Marcus, & Tehranian, 2009) links crashes to opacity and unreleased bad news. However, an elevated upper return tail is outwardly perceived as the opposite of a crash risk indicator. Consequently, crashes that follow hot runs (e.g., NVIDIA's drawdowns in 2018 and 2022) blindside price-only risk screens.

Zhang and Yang resolve this by proposing that return heaviness consists of two economically distinct, observationally pooled components:
$$\lambda^{+}_{i,t} = \underbrace{\lambda^{L}_{i,t}}_{\text{lottery: transient jump risk}} + \underbrace{\lambda^{S}_{i,t}}_{\text{structural: regime repricing}}$$

- **Lottery Tail ($\lambda^L_{i,t}$):** Arises from idiosyncratic, transient jump arrivals (news shocks, short squeezes, episodic retail attention) on an unchanged economic base. It possesses zero persistence in the conditional mean and deserves the MAX discount.
- **Structural Tail ($\lambda^S_{i,t}$):** Represents the statistical manifestation of a regime shift in the firm's real economic configuration (new counterparty dependencies, customer acquisitions, cloud/platform alliances, foundry agreements). The underlying business is experiencing persistent economic repricing.

Because market prices aggregate trades without distinguishing the underlying cause, investors discount pooled tail heat $\hat{\xi}^+_{i,t}$ uniformly as a lottery (Assumption A1). Furthermore, corporate disclosure text diffuses slowly into security prices (Assumption A2; Cohen, Malloy, & Nguyen, 2020). Therefore:
- When tail heat coincides with a **forming/intact network** (birth-dominated rewiring $B \gg D$), the asset trades at an unearned lottery discount. As the disclosed configuration becomes common knowledge through earnings and analyst coverage, an essential category-correction alpha premium is realized.
- When tail heat coincides with a **disintegrating network** (death-dominated rewiring $D \gg B$), the hot tail reflects an unwinding regime whose counterparty losses are already documented in SEC filings but not yet recognized by price screens, forecasting a severe crash.

### Research interpretation

The core mechanism is **slow-diffusing corporate disclosure topology resolving the behavioral mispricing of extreme asset returns**.

Price-only quantitative models operate with zero latency on OHLCV data, causing them to treat all heavy-tail return spikes identically (either chasing momentum or fading MAX). However, 10-K filings provide an orthogonal, low-frequency information channel. An LLM-extracted graph identifies structural reality ahead of financial comovement:
- **Death-side crash mechanism:** When major customer/supplier/platform edges vanish from a 10-K filing ($D > 0$) while trailing return momentum and tail index remain hot, the market is pricing past momentum while the enterprise foundation has structurally decayed. The interaction $\hat{\xi}^+ \times D$ serves as an explicit, early-warning exit/short signal.
- **Birth-side alpha mechanism:** When edge births ($B > 0$) expand into high-productivity partners without counterparty attrition ($D \approx 0$), the upper tail reflects structural innovation. Fading these names as "overextended lottery stocks" represents a systematic market error.

## Signal

The strategy operates by combining a rolling statistical tail-heat estimator with an annual 10-K disclosure-network rewiring decomposition.

### 1. Tail Heat Metric ($\hat{\xi}^+_{i,t}$)

For firm $i$ in month $t$, tail heat is estimated using the classical Hill estimator on positive daily market-excess log returns $r_{i,\tau} - r_{m,\tau}$ over a trailing window $W = 504$ trading days (2 calendar years):
$$\hat{\xi}^+_{i,t} = \frac{1}{k} \sum_{j=1}^{k} \ln\left( \frac{r_{(n - j + 1)}}{r_{(n - k)}} \right)$$
where $r_{(1)} \le \dots \le r_{(n)}$ are the sorted positive excess returns, and the order threshold is pre-specified as:
$$k = \max(10, \lceil 0.05 \cdot W \rceil) = 26$$
- Lower tail index $\hat{\xi}^-_{i,t}$ is symmetrically estimated on negative excess returns.
- Tail asymmetry is defined as $\Delta\hat{\xi}_{i,t} = \hat{\xi}^+_{i,t} - \hat{\xi}^-_{i,t}$.

### 2. Disclosure Network Rewiring Decomposition

From consecutive 10-K filing vintages $t-1$ and $t$, a directed, weighted economic adjacency graph $A_t$ is constructed where edge weights $w_{e,t} \in [0, 1]$ represent dependency intensity between firm $i$ and counterparty $j$ across dependency classes (supplier, customer, licensing, cloud, foundry, platform):
$$B_{i,t} + D_{i,t} + C_{i,t} = \sum_{e \in \mathcal{P}_i} \bigl| w_{e,t} - w_{e,t-1} \bigr|$$
where $\mathcal{P}_i$ denotes directed pairs involving firm $i$, and total rewiring decomposes into three non-negative scalar masses:
1. **Edge-Birth Mass ($B_{i,t}$):** Sum of weights for newly documented edges ($w_{e,t-1} = 0$, $w_{e,t} > 0$).
2. **Edge-Death Mass ($D_{i,t}$):** Sum of weights for lapsed/dissolved edges ($w_{e,t-1} > 0$, $w_{e,t} = 0$).
3. **Continuing Drift ($C_{i,t}$):** Absolute drift in weights for persistent relationships ($w_{e,t-1} > 0$, $w_{e,t} > 0$).

Total rewiring is measured in absolute volume rather than net drift (edge birth cannot be canceled out by continuing drift).

### 3. Combined Trading & Risk Signals

- **P1: Danger-Flag / Crash-Avoidance Overlay (Primary Confirmatory Endpoint):**
  A firm-vintage is flagged as an active crash candidate when its standardized interaction is strongly negative:
  $$\text{DangerFlag}_{i,t} = z(\hat{\xi}^+_{i,t}) \times z(D_{i,t})$$
  In discrete monitoring form: flag if trailing tail heat is elevated ($\hat{\xi}^+ \ge u^*$, where $u^* \in \{Q_{70}, Q_{80}, Q_{90}\}$) AND death mass is positive ($D_{i,t} > d^*$).
  *Action:* Liquidate long positions, eliminate equity beta, or enter systematic 6-month protective short/put hedges.

- **P2: Structural Winner Long Signal (Alpha Endpoint):**
  Identifies forward extreme winners ($R^{\text{abn}}_{12M} > +u$) via the joint double condition:
  $$\hat{\xi}^+_{i,t} \ge u^* \quad \text{AND} \quad D_{i,t} \le d^* \quad \left(\text{or birth share } \frac{B_{i,t}}{B_{i,t} + D_{i,t}} \ge \theta\right)$$
  *Parameters (calibrated walk-forward on validation period):*
  - Tail heat cutoff: $u^* \in \{Q_{70}, Q_{80}, Q_{90}\}$ of training-window $\hat{\xi}^+$.
  - Network condition: $D \le \text{median}$, $D \le Q_{75}$, $B/(B+D) \ge 0.50$, or $B/(B+D) \ge 0.75$.
  *Portfolio construction:* Rank qualifying names by composite score and hold top $k=20$ names equal-weighted or risk-weighted for 12 months.

## Required data

- **Equity Returns:**
  - Daily split- and dividend-adjusted closing prices and market-benchmark returns (e.g., CRSP value-weighted or S&P 500 index) with minimum 504 trading days of history.
  - Calculation of 1-month maximum daily return (MAX), 12-month momentum (12-2M), and 24-month rolling market beta $\beta_{i,t}$.
- **Corporate Filings (SEC EDGAR):**
  - Form 10-K annual filings (Items 1, 1A, and 7) and Form 10-K/A amendments.
  - Strict point-in-time timestamping: graph updates only become effective at market close on the SEC EDGAR official acceptance date. Amendments enter on their own acceptance dates and never retroactively alter prior history.
  - Staleness tracking: integer months elapsed since 10-K acceptance date.
- **Universe Definition (Scope-Conditioned):**
  - Ecosystem-coherent universe where counterparty disclosures are dense: S&P 1500 Information Technology, S&P 1500 Communication Services, S&P 1500 Aerospace & Defense, and a fixed telecom-infrastructure list.
  - Reconstituted annually each June point-in-time. Foreign private issuers filing Form 20-F are excluded.
  - Density gate prerequisite: Pre-test must confirm that at least 30% of firm-vintages have non-zero death mass ($D > 0$).

## Execution assumptions

- **Rebalancing Cadence:** Monthly reconstitution for risk monitoring; annual or bi-annual portfolio updates aligned with 10-K filing waves (February–April peak).
- **Execution Timing:** Signals formed at month-end using only filings accepted on or before month-end; trades executed at the next trading day's open or volume-weighted average price (VWAP) to eliminate look-ahead bias.
- **Transaction Costs & Turnover:**
  - US large/mid-cap equities: 5–15 bps round-trip transaction costs.
  - Long holding horizon (6 to 12 months) generates low portfolio turnover (<120% annualized), making execution capacity institutional-grade.
- **Shorting & Borrow Constraints:**
  - Danger-flag crash overlays can be implemented as outright long liquidations or cash allocations without borrow constraints.
  - For long-short implementations, borrowing fees and locate availability on high-MAX names must be explicitly modeled.

## Evidence

### Source-reported

All figures trace directly to Lin Zhang & Fan Yang (2026), *arXiv:2608.09089v1*, Sections 4–6 and Tables 1–3:

1. **Unconditional Lottery Baseline (24 US Technology Panel, 2014–2025, $N = 3,192$ firm-months):**
   - Forward 6-month abnormal returns across quintiles of $\hat{\xi}^+$ are essentially flat: **2.7%, 2.1%, 2.7%, 2.5%, 2.3%**.
   - In cross-sectional regression with controls, unconditional tail heat is economically and statistically zero: $b = +0.005$ per SD ($SE = 0.006$).
   - Raw MAX anomaly exhibits expected negative sign: $b = -0.007$ ($SE = 0.004, t \approx -1.8$).
   - Raw tail asymmetry ($\hat{\xi}^+ - \hat{\xi}^-$) quintiles slope toward underperformance (top two right-skewed quintiles earn 0.6%–1.4% vs 3.4%–3.7% for the rest), but attenuates with controls ($b = -0.004$ per SD, 95% CI $[-0.019, +0.011]$).

2. **Central Interaction Regression (Table 3, $N = 2,435$ firm-months, 200 firm-vintages):**
   - **Monthly Panel ($N = 2,435, R^2 = 0.028$):**
     - Tail heat $\hat{\xi}^+$: $b = +0.010$ ($SE = 0.008, t = +1.3$)
     - Birth mass $B$: $b = +0.015$ ($SE = 0.011, t = +1.4$)
     - Death mass $D$: $b = -0.009$ ($SE = 0.009, t = -1.0$)
     - **Tail heat $\times$ Death mass ($\hat{\xi}^+ \times D$): $b = -0.025$ ($SE = 0.009, t = -2.9$)**
     - Tail heat $\times$ Birth mass ($\hat{\xi}^+ \times B$): $b = -0.000$ ($SE = 0.007, t = -0.1$)
     - Momentum: $b = -0.009$ ($SE = 0.012, t = -0.7$)
     - Volatility: $b = +0.010$ ($SE = 0.010, t = +1.0$)
     - MAX: $b = -0.010$ ($SE = 0.005, t = -2.0$)
   - **Collapsed Firm-Vintage Panel ($N = 200, R^2 = 0.194$):**
     - Tail heat $\hat{\xi}^+$: $b = +0.013$ ($SE = 0.007, t = +1.9$)
     - Birth mass $B$: $b = +0.009$ ($SE = 0.007, t = +1.2$)
     - Death mass $D$: $b = -0.006$ ($SE = 0.007, t = -0.9$)
     - **Tail heat $\times$ Death mass ($\hat{\xi}^+ \times D$): $b = -0.028$ ($SE = 0.007, t = -3.9$)**
     - Tail heat $\times$ Birth mass ($\hat{\xi}^+ \times B$): $b = +0.005$ ($SE = 0.008, t = +0.7$)
     - MAX: $b = +0.040$ ($SE = 0.035, t = +1.2$)
   - **Inference Robustness for $\hat{\xi}^+ \times D$:**
     - Wild-cluster bootstrap (Rademacher weights, null imposed) on collapsed panel: **two-sided $p = 0.039$**.
     - Two-way (firm and month) clustered $t$-statistic on monthly panel: $t = -3.0$.
     - Leave-one-firm-out range: interaction coefficient spans $-0.029$ to $-0.015$ (dropping NVIDIA roughly halves the coefficient to $-0.015$, but sign remains strictly negative).
     - Distribution support: 73% of firm-vintages have $D > 0$ (median $D = 0.6$, maximum 7.0); 84% have $B > 0$.

3. **Event-Time Case Evidence:**
   - **NVIDIA 2022 Drawdown:** FY2022 10-K (accepted 2022-03-18) recorded acute death-dominated rewiring ($D = 7.0$ of $8.7$ total rewiring) while the trailing tail remained hot; forward 6-month abnormal return was **$-51\%$**.
   - **NVIDIA 2018 Crypto Crash:** Preceded by death-dominated rewiring under an elevated tail heat index.
   - **NVIDIA Expansionary Waves:** FY2020, FY2021, and FY2024 vintages were heavily birth-dominated under rising heat, preceding $+45\%$, $+32\%$, and $+34\%$ abnormal 6-month returns.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Pre-Registered Broad-Market Replication Failure (Stage B0):**
   - A pre-registered out-of-sample replication on 50 randomly sampled S&P 500 firms (FY2020–FY2024, 200 firm-vintages) **failed completely**:
     $$\hat{\xi}^+ \times D \text{ coefficient} = -0.001 \quad (t = -0.07, \text{one-sided wild-cluster } p = 0.49)$$
   - *Diagnostic cause:* Acute disclosure sparsity outside tech ecosystems. 83% of random S&P 500 firm-vintages had zero death mass ($D = 0$), compared to 27% in the pilot. Non-tech firms (utilities, REITs, consumer goods, healthcare) rarely name specific corporate counterparties in 10-K text.
   - Within the 6 dense tech firms of the random draw (24 firm-vintages), the interaction was $-0.001$ ($SE = 0.057$); across all 34 non-zero death firm-vintages, it was $-0.040$ ($SE = 0.053$), both statistically uninformative due to wide standard errors.
2. **Statistically Unresolved Alpha Side in Pilot:**
   - Tail heat interacted with birth mass ($\hat{\xi}^+ \times B$) is statistically indistinguishable from zero ($t = -0.1$ monthly, $t = +0.7$ collapsed). The claim of positive alpha for structural winners rests on event case studies and directional point estimates, awaiting confirmatory testing.
3. **Single-Firm Influence:**
   - Dropping NVIDIA reduces the collapsed interaction coefficient by nearly 50% (from $-0.028$ to $-0.015$), indicating that mega-cap idiosyncratic dynamics account for a substantial fraction of the measured variance in small panels.

## Falsification plan

The empirical hypothesis can be disproven by any of the following operational tests:

1. **Pre-Registration Density Gate (Re-Activation Hurdle):**
   - Execute a seeded 200-filing test on the proposed S&P 1500 tech/telecom/aerospace universe. If the proportion of firm-vintages with $D > 0$ is $< 30\%$, the disclosure graph lacks sufficient support; reject the universe construction.
2. **Primary Endpoint P1 Falsification (Crash Separation):**
   - In the frozen walk-forward test period (2020–2024, training 2010–2017, validation 2018–2019), estimate the firm-vintage collapsed regression on winsorized forward 6M abnormal returns.
   - If the wild-cluster bootstrap one-sided $p$-value for $\hat{\xi}^+ \times D$ fails to achieve $p < 0.05$ or if the coefficient is non-negative ($b \ge 0$), the danger-side separation hypothesis is falsified.
3. **Primary Endpoint P2 Falsification (Structural Winner Alpha):**
   - For the gatekept alpha test, measure precision-at-$k=20$ of the double-condition flag for positive-only extreme upside ($R^{\text{abn}}_{12M} > +u$) against four baseline screens (tail-only, low-MAX, momentum, low-volatility).
   - If the 5th percentile of the two-stage block-bootstrap difference between the flag and the maximum benchmark is $\le 0$, reject the hypothesis that structural tails deliver harvestable alpha over standard screens.
4. **Permuted Network Placebo Test:**
   - Randomly permute 10-K adjacency matrices across firms within the same filing year while preserving raw return time series. If the interaction $\hat{\xi}^+ \times D$ remains statistically significant under scrambled network pairings ($t < -2.0$), the observed effect is a statistical artifact of volatility clustering rather than genuine economic counterparty dissolution.

## Crypto portability

**Portability classification:** `adapted` / `unproven`.

The primary research is conducted strictly on US equities using annual SEC EDGAR 10-K corporate filings. Porting to cryptocurrency markets involves substantial structural translations:
1. **Absence of Regulatory Disclosures:** Decentralized cryptocurrency tokens do not file 10-Ks or mandated counterparty disclosures. A direct port is impossible.
2. **On-Chain Graph Adaptation:** An adapted hypothesis must replace 10-K corporate disclosure networks with **on-chain entity interaction graphs**:
   - *Edges:* Smart contract dependency calls, protocol treasury asset allocations, decentralized exchange (DEX) liquidity pool pairings, cross-chain bridge collateral links, or persistent multi-sig wallet clusters.
   - *Network Death Mass ($D$):* Documented dissolution of protocol integrations, major liquidity provider (LP) capital flight, removal of collateral support on lending platforms, or smart contract dependency deprecation.
3. **Crypto Tail Regimes:** Cryptocurrency returns exhibit extreme heavy-tailed distributions driven by retail meme cycles (lottery tails) vs. structural technological/ecosystem adoption (structural tails). If on-chain wallet/contract death mass is observed while trailing token returns remain in a speculative bubble, the crash-risk mechanism hypothesized by Zhang & Yang should translate with heightened severity.
4. **Execution Frictions:** Unlike US equities, crypto altcoins suffer from extreme illiquidity, DEX slippage, gas spikes, and negative funding rates on perpetual shorts, which could erode predictive margins.

## Limitations

- **Strict Scope Condition:** The mechanism completely fails outside densely disclosing corporate ecosystems (as demonstrated by the 83% zero-death rate in the random S&P 500 replication).
- **Annual Update Frequency:** 10-K filings update once per year. The network state remains static for 12 months, creating temporal staleness and making high-frequency timing impossible.
- **LLM Extraction Imperfections:** Single-pass LLM parsers suffer from recall gaps and parser span coverage limits (e.g., competitors mentioned outside Items 1/1A/7), necessitating complex multi-agent extraction architectures.
- **Winner Bias in Pilot:** The 24-firm tech pilot consists of large-cap tech survivors, introducing look-ahead survivorship bias into descriptive calibrations.

## Implementation status

`not-implemented`.

This document represents an external research capture. No code has been integrated into PyBroker, NautilusTrader, or any internal live execution infrastructure. No backtests, paper trading, testnet trials, or live trading authorizations have been conducted.

## Adoption boundary

`not-approved` / `research-only`.

This record is placed in the staging repository for research review. Presence in this repository does not constitute validation of alpha, risk approval, or authorization for capital deployment. Progression to implementation requires passing the pre-registered density gate, successful completion of the multi-agent extractor audit, and formal confirmatory validation.

## Related Wiki records

- `supply-chain-network-augmented-llm-text-embeddings-nale-2026-09-04.md`
- `mingle-exposure-locality-factor-graph-portfolio-diversification-2026-09-02.md`
- `agonalpha-prompt-economy-adversarial-review-agentic-alpha-discovery-2026-09-04.md`
- `solana-bonding-curve-sniper-cohort-contamination-adjusted-flow-2026-09-02.md`
- `crypto-dynamic-conditional-tail-dependence-husler-reiss-extremal-graph-2026-09-01.md`

## Sources

- Lin Zhang and Fan Yang, *"Extreme Value Alpha and Crash Risk: Separating Structural Tails from Lottery Tails with LLM-Extracted Disclosure Networks"*, arXiv preprint `arXiv:2608.09089v1 [q-fin.ST]`, submitted 10 August 2026. Stable URL: `https://arxiv.org/abs/2608.09089`. Full-text HTML: `https://arxiv.org/html/2608.09089v1`. DOI: `10.48550/arXiv.2608.09089`.
- Primary empirical tables and equations directly cited from source:
  - Equation (1): Exact rewiring decomposition ($B_{i,t} + D_{i,t} + C_{i,t} = \sum |w_{e,t} - w_{e,t-1}|$).
  - Equation (2): Decomposition of upper tail intensity ($\lambda^+ = \lambda^L + \lambda^S$).
  - Table 1: Reconciled Stage-A registered vs. executed parameters.
  - Table 3: Central empirical regression table for monthly ($N = 2,435$) and collapsed firm-vintage ($N = 200$) panels.
  - Section 4.1: Hill estimator parameters ($W = 504, k = 26$).
  - Section 5.1: Quintile abnormal returns and MAX anomaly controls.
  - Section 5.3: Wild-cluster bootstrap ($p = 0.039$), two-way clustering ($t = -3.0$), leave-one-out sensitivity, and NVIDIA event timelines (FY2022 10-K accepted 2022-03-18 with $D=7.0$ preceding $-51\%$ abnormal return).
  - Section 5.5: Pre-registered Stage B0 replication failure on 50 random S&P 500 firms ($b = -0.001, t = -0.07, p = 0.49; 83\% \text{ zero death mass}$).
  - Section 6: Confirmatory walk-forward schedule (Training 2010–2017, Validation 2018–2019, Test 2020–2024), gatekept endpoints P1 and P2, and power simulations.
- Additional background literature cited by the primary source:
  - Bali, T. G., Cakici, N., & Whitelaw, R. F. (2011). "Maxing out: Stocks as lotteries and the cross-section of expected returns." *Journal of Financial Economics*, 99(2), 427–446.
  - Barberis, N., & Huang, M. (2008). "Stocks as lotteries: The implications of probability weighting for security prices." *American Economic Review*, 98(5), 2066–2100.
  - Cohen, L., Malloy, C., & Nguyen, Q. (2020). "Lazy prices." *Journal of Finance*, 75(3), 1371–1415.
  - Hutton, A. P., Marcus, A. J., & Tehranian, H. (2009). "Opaque financial reports, R^2, and crash risk." *Journal of Financial Economics*, 94(1), 67–86.
  - Yang, F., & Zhang, L. (2026). "LLM latent edge measurement: Point-in-time economic graphs for quantitative investing from corporate disclosures." Working paper, arXiv:2607.15640.
