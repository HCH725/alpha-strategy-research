---
schema: strategy-research-record-v1
title: "Regret-Driven Portfolios: Greedy Follow-the-Leader Allocation with Fear-and-Greed Gating and LLM-Guided Sector Hedging"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - portfolio-optimization
  - no-regret-learning
  - follow-the-leader
  - sentiment-analysis
  - fear-and-greed
  - large-language-models
  - sector-etfs
status: research-only
confidence: medium
source_as_of: 2026-01-16
sources:
  - "Muhammad Aarash and Dr. Hassan Jaleel, 'Regret-Driven Portfolios: LLM-Guided Smart Clustering for Optimal Allocation', Proceedings of the 6th ACM International Conference on AI in Finance (ICAIF '25), Singapore, November 15–18, 2025; arXiv:2601.17021v1 [q-fin.PM], submitted January 16, 2026. DOI: 10.48550/arXiv.2601.17021. https://arxiv.org/abs/2601.17021"
  - "Anonymous Open Science Repository: no-regret-paper-62CA, https://anonymous.4open.science/r/no-regret-paper-62CA"
  - "Fear and Greed Index historical dataset repository, https://github.com/gman4774/Fear_and_Greed_Index"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Regret-Driven Portfolios: Greedy Follow-the-Leader Allocation with Fear-and-Greed Gating and LLM-Guided Sector Hedging

## Provenance

- **Primary Academic Paper:** Muhammad Aarash and Dr. Hassan Jaleel, *"Regret-Driven Portfolios: LLM-Guided Smart Clustering for Optimal Allocation"*, Proceedings of the 6th ACM International Conference on AI in Finance (ICAIF '25), ACM, Singapore, November 15–18, 2025; arXiv preprint `arXiv:2601.17021v1 [q-fin.PM]`, submitted 16 Jan 2026.
- **Canonical DOI:** [10.48550/arXiv.2601.17021](https://doi.org/10.48550/arXiv.2601.17021).
- **Traceable Paper URLs:**
  - Abstract: [https://arxiv.org/abs/2601.17021](https://arxiv.org/abs/2601.17021)
  - Full Text HTML: [https://arxiv.org/html/2601.17021v1](https://arxiv.org/html/2601.17021v1)
  - Full Text PDF: [https://arxiv.org/pdf/2601.17021](https://arxiv.org/pdf/2601.17021)
- **Primary Open-Source Implementation & Data Provenance:**
  - Source Code Repository: [https://anonymous.4open.science/r/no-regret-paper-62CA](https://anonymous.4open.science/r/no-regret-paper-62CA) [source-reported in footnote 2].
  - Sentiment Index Repository: [https://github.com/gman4774/Fear_and_Greed_Index](https://github.com/gman4774/Fear_and_Greed_Index) [source-reported in footnote 3].
- **Authors & Affiliation:**
  - Muhammad Aarash (`25100330@lums.edu.pk`) and Dr. Hassan Jaleel (`hassan.jaleel@lums.edu.pk`), Department of Electrical Engineering / Computer Science, Lahore University of Management Sciences (LUMS), Lahore, Pakistan.
- **Pre-Write Deduplication Audit:**
  - A repository-wide inspection on 2026-09-05 confirmed zero existing records referencing `2601.17021`, `Aarash`, `Jaleel`, `no-regret`, or `follow-the-leader`.
  - Existing sentiment records in the repository (`crypto-fear-greed-weekly-ar1-innovation-risk-premium-2026-09-04.md`, `crypto-macro-sentiment-contrarian-fear-greed-ema-2026-09-03.md`, `raml-regime-aware-multimodal-bitcoin-sentiment-fusion-2026-09-04.md`) evaluate high-frequency crypto momentum or single-asset BTC timing.
  - This record is structurally and mechanically independent: it formulates multi-asset portfolio rebalancing through a greedy Follow-the-Leader (FTL) no-regret optimization over candidate single-asset weight perturbations, augmented by a dual-threshold CNN Fear & Greed macro volatility gate and an upstream LLM sector pseudo-hedging module.

## Economic mechanism

### Source-reported

The authors argue that professional active management faces a persistent structural challenge:
1. **Passive Outperformance vs. Risk-Adjusted Mandates:** From 2014 to 2024, approximately 93.4% of hedge funds underperformed the S&P 500 on a nominal return basis (Buffett 2007 wager; Gehringer & Pauli 2025). However, institutional asset managers (e.g., pension funds, endowments) cannot simply track 100% equity indices due to strict drawdown tolerance, fiduciary hedging mandates, and vulnerability to catastrophic tail drawdowns (e.g., the 2020 COVID crash or 2022 inflationary shock).
2. **Failure of Static Convex Optimization:** Classical static models—including Markowitz mean-variance (1952), Mean Absolute Deviation (MAD, Konno & Yamazaki 1991), and Conditional Value-at-Risk (CVaR, Rockafellar & Uryasev 2000)—assume distributional stationarity and exhibit extreme parameter sensitivity, leading to severe out-of-sample estimation error under structural regime shifts.
3. **Online Learning & Follow-the-Leader (FTL):** Online portfolio selection algorithms (Cover 1991 Universal Portfolio; Helmbold et al. 1998 Hedge multiplicative weights) guarantee that average regret relative to the best fixed constant rebalanced portfolio vanishes asymptotically ($\lim_{T \to \infty} \frac{1}{T} \text{Regret}(\mathbf{a}^*, T) = 0$). The authors introduce a deterministic, performance-driven variant of the Follow-the-Leader strategy that greedily selects the historical allocation maximizing a target risk-adjusted objective (Calmar, Sharpe, Sortino) over a lookback window $k$.
4. **Behavioral Macro Conditioning & LLM Pseudo-Hedging:**
   - Investor sentiment exhibits regime-dependent predictability. CNN's Fear & Greed Index reflects retail overreaction, risk aversion, and liquidity contraction.
   - Rather than deploying LLMs for direct return forecasting or asset picking—which the authors empirically prove degrades returns by 34% to 37%—LLMs are prompted strictly as an **upstream pseudo-hedging filter**. The LLM receives temporal sentiment context and identifies complementary, non-correlated sectors (e.g., utilities, consumer staples, treasuries) to provide structural downside protection.

### Research interpretation

The framework operates as a 4-tiered hierarchical risk-budgeting system:
- **Regime Gating (Level 1):** The CNN Fear & Greed Index acts as an operational circuit breaker. Bounded absolute thresholds ($10 \le \text{F\&G} \le 90$) and a 5-day delta cap ($|\Delta \text{F\&G}_{5\text{d}}| \le 20\%$) prevent rebalancing during panic panics or euphoric momentum climaxes, defaulting to cash preservation when sentiment transitions violently.
- **Investable Universe Construction & Hedging (Level 2):** Upstream LLM prompting expands the active investment pool with orthogonal sector ETFs. By prompting for sector-level rather than ticker-level hedges, the strategy neutralizes equity-specific name bias while ensuring structural decorrelation.
- **Constrained Action Simplex Perturbation (Level 3):** Rather than performing unbounded continuous convex optimization across all $N$ assets—which invites extreme portfolio turnover and estimation error—the algorithm explores a discrete set of single-asset weight perturbations ($\Delta a_i$) around the incumbent allocation. This enforces an implicit Cardinality-1 turnover penalty that curbs transaction drag.
- **Greedy FTL Risk-Adjusted Selection (Level 4):** By greedily evaluating candidate perturbed portfolios against trailing Calmar or Sharpe ratios over lookback window $k$, the policy exploits medium-term persistence in sector trends (captured at quarterly rebalancing cadences) while explicitly penalizing trailing downside variance.

## Signal

### Mathematical Formulation & Optimization Objective

Let $\mathbf{a}(t) = [a_1(t), a_2(t), \dots, a_n(t)]$ denote the portfolio allocation vector across $n$ assets at rebalancing time $t$, subject to the simplex constraints [source-reported]:
$$0 \le a_i(t) \le 1 \quad \forall i \in \{1, \dots, n\}, \quad \sum_{i=1}^{n} a_i(t) = 1$$

The algorithm selects the allocation $\mathbf{a}(t) \in \mathcal{A}$ that maximizes an empirical objective function $O \in \mathcal{O}$ over historical lookback window $k$ [source-reported]:
$$\mathbf{a}(t) = \arg\max_{\mathbf{a} \in \mathcal{A}} O(\mathbf{a}, k)$$
where the admissible objective set $\mathcal{O}$ includes [source-reported]:
$$\mathcal{O} = \{\text{Annualized Return}, \text{Sharpe Ratio}, \text{Sortino Ratio}, \text{Calmar Ratio}\}$$

### Candidate Action Simplex Generation (Algorithm 1)

Candidate portfolio vectors $\mathcal{A}$ are generated by systematically perturbing the baseline allocation $\mathbf{a}_{\text{base}}$ [source-reported]:
1. **Baseline Initialization:** $\mathbf{a}_{\text{base}}$ is initialized to 100% cash ($a_{\text{cash}} = 1.0, a_i = 0$). At subsequent rebalancing timesteps, $\mathbf{a}_{\text{base}}$ is set to the prevailing portfolio allocation immediately prior to rebalancing [source-reported].
2. **Single-Asset Perturbation Loop:**
   - For each asset $i \in \{1, \dots, n\}$:
     - Vary candidate allocation $a'_i$ over allowable bounds $[a_{\min}, a_{\max}]$ with step size $\Delta a$ [source-reported].
     - Compute required weight shift: $\Delta a_i = a'_i - a_i$ [source-reported].
     - Offset $\Delta a_i$ across non-target assets:
       - *Uniform Adjustment Mechanism (active):* The change $\Delta a_i$ is distributed proportionally across all other currently invested assets to maintain $\sum_{j=1}^n a'_j = 1$ [source-reported].
       - *Cash Residual Mechanism (inactive):* Shift residual exclusively to/from cash reserves [source-reported].
     - If all weights satisfy $0 \le a'_j \le 1$, append candidate vector $\mathbf{a}'$ to action set $\mathcal{A}$ [source-reported].

### Sentiment Gating & Macro Volatility Circuit Breaker

Before rebalancing is authorized on date $t$, the prevailing Fear & Greed Index $\text{F\&G}_t \in [0, 100]$ must satisfy two independent risk gates [source-reported]:
1. **Absolute Level Bounds:**
   $$10 \le \text{F\&G}_t \le 90$$
   If $\text{F\&G}_t < 10$ (extreme panic) or $\text{F\&G}_t > 90$ (extreme euphoria), rebalancing is blocked, and portfolio capital is optionally converted 100% to cash to eliminate severe tail risk [source-reported].
2. **Delta Volatility Threshold:**
   $$|\text{F\&G}_t - \text{F\&G}_{t-5}| \le 20 \text{ points}$$
   If the absolute 5-day shift exceeds 20 points ($20\%$ change over 5 trading sessions), rebalancing is suppressed to prevent whipsawing on sentiment shocks [source-reported].

### LLM Upstream Sector Selection & Pseudo-Hedging Pipeline

When dynamic sector conditioning is activated [source-reported]:
1. **Temporal Context:** A 12-month trailing daily time series of the Fear & Greed Index is passed to the LLM [source-reported].
2. **Ensemble Voting:** The LLM is queried 5 independent times to recommend the 3 most promising economic sectors; the final selection is determined by majority vote across the 5 responses [source-reported].
3. **Pseudo-Hedging Query:** The LLM is prompted without historical dates (to prevent temporal lookahead and familiarity bias) to generate complementary, non-correlated hedging sectors for each selected cluster [source-reported].
4. **Universe Augmentation:** The identified hedging sector ETFs are injected into the investable asset pool for the FTL optimization step [source-reported].

### Operational Parameters & Trading Rules

- **Signal Formation Timestamp:** Evaluated at the close of each calendar quarter ($t_{\text{rebal}} \approx 63$ trading days) [source-reported].
- **Rebalancing Cadence:** Quarterly schedule ($Q$) [source-reported; 71% of SPY-beating models utilized quarterly frequency].
- **Evaluation Lookback Horizon ($k$):**
  - Standalone FTL: $k = 30$ trading days [source-reported, Table 1].
  - FTL with LLM Hedging: $k = 120$ trading days [source-reported, Table 1].
- **Optimization Metric:** Calmar Ratio ($\frac{R_{\text{annual}}}{\text{Max Drawdown}}$) or Sortino Ratio [source-reported].
- **Universe Breadth:** Full unconstrained asset universe (percentile filtering disabled, as empirical tests confirmed broader universes yield higher Sharpe ratios) [source-reported].
- **Execution Fill Model:** Next-day market-on-open (MOO) order execution [`research-proposed` standard operational model].
- **Position Limits:** $a_{\min} = 0.0$, $a_{\max} = 0.40$ per asset [`research-proposed` diversification bound].
- **Holding Period:** 1 quarter ($\approx 63$ trading days), held until the next quarterly rebalancing window [source-reported].

## Required data

- **Asset Universes:**
  - **COCKROACH Universe (4 assets):** SPY (S&P 500 ETF), Gold (spot/bullion pricing), 10-Year U.S. Treasury Bonds, and Cash ($1.00 constant value) [source-reported].
  - **SECTOR-ETFs Universe (55 assets):** 51 sector-specific ETFs representing 20 granular economic classifications (sourced from Vanguard, iShares, and SPDR families), plus SPY, Gold, 10-Year U.S. Treasury Bonds, and Cash [source-reported].
- **Primary Data Sources:**
  - Cash & 10-Year Treasury Yields: `investing.com` (Treasury yields converted to daily synthetic bond prices via zero-coupon yield curve stripping) [source-reported].
  - Gold: World Gold Council daily spot pricing [source-reported].
  - Equity & Sector ETFs: Yahoo Finance daily adjusted close prices [source-reported].
  - Sentiment Index: CNN Fear & Greed Index daily time series (`github.com/gman4774/Fear_and_Greed_Index`) [source-reported].
- **Point-in-Time & Survivorship Handling:**
  - Asset-specific entry and exit dates are explicitly tracked [source-reported].
  - Non-trading days and unlisted periods are assigned a sentinel value of $-1$; assets priced at $-1$ on rebalancing dates are strictly excluded from the optimization simplex [source-reported].
  - If a held asset is delisted mid-quarter, it is immediately liquidated to cash and blacklisted from future allocations [source-reported].
  - Missing weekend/holiday prints are forward-filled [source-reported].

## Execution assumptions

- **Order Timing & Execution:** Quarterly rebalancing orders formed at market close and filled at the opening auction of the next trading day (`MOO`) [`research-proposed` standard execution assumption].
- **Transaction Costs & Fees:** Simulated using a flexible fee model supporting percentage-based commissions; fees subtracted directly from cash balance on each rebalancing date [source-reported]. Assumed execution drag of 5 bps to 10 bps per trade [`research-proposed` realistic institutional ETF cost model].
- **Slippage & Market Impact:** Negligible market impact assumed due to high secondary market liquidity of major sector ETFs (SPDR/Vanguard/iShares) and quarterly turnover constraints [source-reported].
- **Borrow & Leverage Constraints:** Strictly long-only ($a_i \ge 0$), unleveraged ($\sum a_i = 1.0$) [source-reported].
- **Cash Drag & Yield:** Unallocated portfolio weight held in Cash at constant $1.00 face value; zero interest credit assumed as a conservative friction [`research-proposed`].

## Evidence

### Source-reported

The authors evaluated the framework across two historical backtest windows:
- **COCKROACH:** January 3, 2000 – May 31, 2024 (24.4 years) [source-reported].
- **SECTOR-ETFs:** January 1, 2011 – June 30, 2024 (13.5 years, grid search) [source-reported, Table 1].

Comprehensive empirical performance across parameter configurations and benchmark references from Table 1 of the primary paper:

| Strategy / Objective | Rebal. Freq. | Sector Cluster | F&G Bounds | F&G $\Delta$ Filter (5d) | Lookback $k$ (Days) | LLM Hedge | Annual Return (%) | Volatility ($\sigma$) | Max Drawdown | Sharpe Ratio | Sortino Ratio | Calmar Ratio |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **NRL (Calmar-Opt)** | **Q** | **All** | **10–90** | **20% / 5d** | **30** | **N** | **18.91%** | **0.15** | **0.16** | **1.03** | **1.3460** | **1.1965** |
| NRL (Return-Opt) | Q | All | 10–90 | 20% / 5d | 30 | N | 16.81% | 0.17 | 0.22 | 0.80 | 1.0816 | 0.7504 |
| NRL (Sortino-Opt) | Q | All | 10–90 | 20% / 5d | 30 | N | 16.04% | 0.15 | 0.15 | 0.89 | 1.1916 | 1.0502 |
| NRL (Sortino-Opt) | Q | All | 10–90 | 20% / 5d | 10 | N | 15.24% | 0.15 | 0.19 | 0.84 | 1.1333 | 0.8035 |
| NRL (Calmar-Opt) | Y | Dynamic (LLM) | 10–90 | - | 90 | N | 11.46% | 0.14 | 0.28 | 0.61 | 0.7477 | 0.4063 |
| NRL (Return-Opt) | Y | Dynamic (LLM) | 10–90 | 20% / 5d | 30 | N | 11.54% | 0.13 | 0.23 | 0.64 | 0.6317 | 0.4936 |
| **NRL (LLM-Hedged)** | **Q** | **Dynamic (LLM)** | **10–90** | **20% / 5d** | **120** | **Y** | **13.08%** | **0.12** | **0.18** | **0.83** | **1.0335** | **0.7390** |
| NRL (LLM-Hedged) | Q | Dynamic (LLM) | 10–90 | - | 60 | Y | 12.43% | 0.12 | 0.22 | 0.77 | 0.9832 | 0.5704 |
| *Benchmark: Online MAD* | - | - | - | - | - | - | 13.56% | 0.14 | 0.24 | 0.74 | 0.9500 | 0.5800 |
| *Benchmark: Online Hedge* | - | - | - | - | - | - | 17.09% | 0.19 | 0.26 | 0.76 | 1.0000 | 0.6500 |
| *Benchmark: SPY Buy-Hold* | - | - | - | - | - | - | 11.21% | 0.17 | 0.34 | 0.47 | 0.5800 | 0.3300 |
| *Benchmark: Gold Buy-Hold*| - | - | - | - | - | - | 3.91% | 0.16 | 0.45 | 0.06 | 0.0800 | 0.0900 |

Key Reported Findings:
- **Drawdown Compression:** The top NRL configuration achieved a maximum drawdown of 16%, compared to 34% for SPY (a 47% reduction in peak-to-trough decline) and 45% for Gold [source-reported].
- **Risk-Adjusted Outperformance:** Over the 2011–2024 period, NRL Calmar-optimized delivered an annualized return of 18.91% (vs. SPY 11.21%, a +68.6% cumulative outperformance) and a Sharpe ratio of 1.03 (vs. SPY 0.47, a 119% improvement) [source-reported].
- **Rebalancing Cadence Dominance:** 71% of all SPY-beating parameter configurations used a quarterly rebalancing cadence [source-reported].
- **LLM Hedging Efficacy:** Adding LLM-generated sector hedges increased Sharpe ratios by 31% on average across all configurations, and by 63% under quarterly rebalancing [source-reported].

### Independently reproduced

Not independently reproduced.

### Negative evidence

The authors document critical empirical failures and counterintuitive behaviors:
1. **Failure of LLM Dynamic Sector Selection:** Utilizing LLMs to dynamically select promising sectors based on temporal Fear & Greed patterns directly degraded performance: cumulative returns and Sharpe ratios were on average 34% and 37% lower, respectively, than unconstrained full-universe baselines [source-reported, Section 4.3]. LLMs proved incapable of predicting sector outperformance from sentiment alone.
2. **Pathology of Tight Sentiment Bands:** Constraining trading to neutral sentiment regimes (e.g., F&G 30–70) severely damaged returns and Sharpe ratios by artificially suppressing participation in high-momentum market regimes [source-reported, Section 4.3].
3. **Objective Function Misalignment:** Optimizing directly for Calmar ratio yielded higher raw returns (18.91%) than optimizing directly for raw return (16.81%), demonstrating non-convex objective instability in historical FTL search [source-reported, Section 5].
4. **Theoretical Guarantee Forfeiture:** Greedily selecting the single best historical allocation departs from the weighted probability distributions of classical no-regret algorithms (e.g., Hedge), thereby forfeiting formal sublinear regret guarantees in adversarial market regimes [source-reported, Section 3.4.2].

## Falsification plan

To falsify the hypothesis that greedy FTL with sentiment gating and LLM hedging generates genuine, persistent economic edge over passive indexation, execute the following operational stress tests:
1. **Out-of-Sample Walk-Forward Test:**
   - *Data:* Post-sample US equity sector ETF data from July 1, 2024 to current date (minimum 8 quarters).
   - *Benchmark:* SPY Buy-and-Hold and Equal-Weight 51 Sector ETFs.
   - *Falsification Condition:* If the strategy achieves a Sharpe ratio lower than SPY or suffers a maximum drawdown exceeding 25% over the holdout window, reject the hypothesis that quarterly FTL adapts robustly to out-of-sample regimes `[research-defined falsification threshold]`.
2. **Placebo Sentiment Gate Test:**
   - *Data:* Replace the true Fear & Greed Index with (a) synthetic white-noise sentiment $\mathcal{N}(50, 15^2)$ and (b) temporally shuffled F&G index series.
   - *Falsification Condition:* If the placebo sentiment gate produces risk-adjusted returns within 5% of the true F&G gate, reject the claim that the Fear & Greed index possesses genuine macro regime-conditioning power `[research-defined falsification threshold]`.
3. **Ablation of Single-Asset Perturbation Constraint:**
   - *Test:* Replace Algorithm 1's single-asset perturbation with an unconstrained continuous convex solver across all 51 assets at each quarterly rebalance.
   - *Falsification Condition:* If unconstrained rebalancing suffers fee-induced degradation greater than 300 bps annualized while Algorithm 1 remains stable, confirm the hypothesis that single-asset perturbation functions as an essential turnover regularizer `[research-defined falsification threshold]`.
4. **Transaction Cost & Liquidity Stress Test:**
   - *Test:* Scale simulated two-way transaction costs from 5 bps up to 30 bps per trade across all constituent ETFs.
   - *Falsification Condition:* If net annualized return falls below SPY under fees of $\le 15$ bps, classify the strategy as an artifact of friction-free rebalancing `[research-defined falsification threshold]`.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Porting Mechanism & Structural Divergence:**
  - The core thesis—combining online regret-minimization over asset weights with macro sentiment circuit breakers—can be adapted to a basket of liquid cryptocurrency perpetuals or spot tokens (e.g., BTC, ETH, SOL, AVAX, LINK, UNI) using crypto-specific sentiment (e.g., Alternative.me Crypto Fear & Greed Index).
  - *Risk-Free Asset & Bond Absence:* Traditional portfolio optimization relies heavily on 10-year Treasury bonds to anchor downside volatility. In crypto, no risk-free sovereign yield exists; cash equivalents consist of centralized stablecoins (USDT, USDC) or tokenized yield (e.g., USDe, sDAI), which introduce protocol credit risk and depeg tail risk.
  - *Rebalancing Horizon Mismatch:* Quarterly rebalancing ($Q \approx 63$ days) is tailored to traditional macroeconomic business cycles and institutional reporting. In crypto, where market cycles compress by an order of magnitude and volatility is 3–5x higher, quarterly rebalancing would suffer catastrophic intermediate drawdown before triggering a portfolio adjustment. Crypto adaptation requires shortening the cadence to weekly or bi-weekly (`research-proposed`).
  - *Perpetual Funding Rate Drag:* Holding long positions in crypto perp tokens incurs dynamic 8-hour funding rates. In sustained bull regimes, funding costs can exceed 20–40% annualized, completely eroding the FTL allocation edge unless spot tokens are held.

## Limitations

- **Underspecified LLM Implementation:** The primary source omits the exact model version (e.g., GPT-4 vs. GPT-3.5 vs. Claude 3), system prompt text, temperature settings, and token latency costs used in the 5-query voting ensemble.
- **Lookahead Audit Required on Sentiment Index:** Historical CNN Fear & Greed data from third-party scrapers (`github.com/gman4774/Fear_and_Greed_Index`) frequently suffers from retroactive revisions, timestamp misalignments, or schema changes that must be audited for point-in-time integrity.
- **Limited Decision Sample Size:** Operating on a quarterly rebalancing cadence over a 13.5-year evaluation window produces only $\approx 54$ total rebalancing decisions, increasing susceptibility to small-sample selection bias.
- **Objective Instability:** The counterintuitive finding that Calmar optimization outperformed return optimization on raw return highlights severe local-optima sensitivity in the discrete perturbation search.

## Implementation status

- **Current Status:** `not-implemented`.
- No prototype or production implementation exists in our NautilusTrader, PyBroker, paper trading, testnet, or live environments.

## Adoption boundary

- **Current Boundary:** `research-only`, `not-approved`.
- This record serves solely as a normalized research capture. It does not authorize capital deployment, strategy prototyping, or automated trading. Any future progression toward PyBroker screening or NautilusTrader validation requires formal Research Intake Review and independent out-of-sample replication.

## Related Wiki records

- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`
- `[[quant/point-in-time-feature-engineering-2026-08-28]]`
- `[[crypto-macro-sentiment-contrarian-fear-greed-ema-2026-09-03]]`
- `[[sentiment-vader-technical-indicator-mean-variance-crypto-portfolio-2026-09-04]]`

## Sources

- Muhammad Aarash and Dr. Hassan Jaleel, *"Regret-Driven Portfolios: LLM-Guided Smart Clustering for Optimal Allocation"*, in *Proceedings of the 6th ACM International Conference on AI in Finance (ICAIF '25)*, ACM, Singapore, November 15–18, 2025; arXiv preprint `arXiv:2601.17021v1 [q-fin.PM]`, submitted January 16, 2026. DOI: [10.48550/arXiv.2601.17021](https://doi.org/10.48550/arXiv.2601.17021). [https://arxiv.org/abs/2601.17021](https://arxiv.org/abs/2601.17021).
- Muhammad Aarash and Dr. Hassan Jaleel, Open-Source Code Repository `no-regret-paper-62CA`, Anonymous GitHub: [https://anonymous.4open.science/r/no-regret-paper-62CA](https://anonymous.4open.science/r/no-regret-paper-62CA).
- Historical Fear and Greed Index Dataset Repository, [https://github.com/gman4774/Fear_and_Greed_Index](https://github.com/gman4774/Fear_and_Greed_Index).
- Malcolm Baker and Jeffrey Wurgler, *"Investor Sentiment in the Stock Market"*, *Journal of Economic Perspectives*, 21(2): 129–152, 2007. DOI: [10.1257/jep.21.2.129](https://doi.org/10.1257/jep.21.2.129).
- Thomas M. Cover, *"Universal Portfolios"*, *Mathematical Finance*, 1(1): 1–29, 1991.
- David P. Helmbold, Robert E. Schapire, Yoram Singer, and Manfred K. Warmuth, *"On-Line Portfolio Selection Using Multiplicative Updates"*, *Mathematical Finance*, 8(4): 325–347, 1998.
- Hiroshi Konno and Hiroaki Yamazaki, *"Mean-Absolute Deviation Portfolio Optimization Model and Its Applications to Tokyo Stock Market"*, *Management Science*, 37(5): 519–531, 1991. DOI: [10.1287/mnsc.37.5.519](https://doi.org/10.1287/mnsc.37.5.519).
- Harry M. Markowitz, *"Portfolio Selection"*, *The Journal of Finance*, 7(1): 77–91, 1952.
- R. Tyrrell Rockafellar and Stanislav Uryasev, *"Optimization of Conditional Value-at-Risk"*, *The Journal of Risk*, 2(3): 21–42, 2000.
