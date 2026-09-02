---
schema: strategy-research-record-v1
title: Prediction Market Lead-Lag Trading with LLM Semantic Risk Filtering
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - prediction-markets
  - lead-lag
  - granger-causality
  - llm-risk-manager
  - kalshi
status: research-only
confidence: medium
source_as_of: 2026-02-04
sources:
  - https://arxiv.org/abs/2602.07048
  - https://arxiv.org/pdf/2602.07048
  - https://doi.org/10.48550/arXiv.2602.07048
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Prediction Market Lead-Lag Trading with LLM Semantic Risk Filtering

## Provenance

- **Primary Source:** Sumin Kim, Minjae Kim, Jihoon Kwon, Yoon Kim, Nicole Kagan, Joo Won Lee, Oscar Levy, Alejandro Lopez-Lira, Yongjae Lee, and Chanyeol Choi (LinqAlpha, Massachusetts Institute of Technology, Kalshi, Arrowpoint Investment Partners, University of California Berkeley, University of Florida, and UNIST), *"LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets"*, arXiv preprint `arXiv:2602.07048v1 [q-fin.RM, q-fin.ST]`, submitted February 4, 2026.
- **Identifier:** arXiv:2602.07048v1 [q-fin.RM, q-fin.ST]
- **DOI:** [10.48550/arXiv.2602.07048](https://doi.org/10.48550/arXiv.2602.07048)
- **Stable URL:** [https://arxiv.org/abs/2602.07048](https://arxiv.org/abs/2602.07048)
- **Full Text HTML:** [https://arxiv.org/html/2602.07048v1](https://arxiv.org/html/2602.07048v1)
- **Empirical Dataset:** Daily price time series from Kalshi prediction markets in the "Economics" category spanning October 2021 to November 2025. After filtering contracts with insufficient activity or negligible price variation, $N = 554$ event markets are retained.
- **Evaluation Protocol:** Rolling-window protocol with 60-day training windows and 30-day testing windows, yielding 18 non-overlapping out-of-sample test periods.

## Economic mechanism

### Source-reported

Real-world macroeconomic and financial events rarely occur in isolation; information regarding one event alters expectations about subsequent events (e.g., an inflation surprise alters expectations of future central bank policy decisions or growth trajectories). In prediction markets, where contract prices represent market-implied event probabilities, these inter-event dependencies manifest as directional lead-lag relationships where price movements in a "leader" contract systematically precede price movements in a "follower" contract.

However, relying solely on pairwise statistical discovery methods such as Granger causality produces significant fragility: in large panels, pairwise screening generates numerous spurious correlations due to selection luck, multiple testing, and non-stationary structural breaks. These statistically significant but brittle links frequently fail out of sample, causing severe downside losses.

The authors hypothesize that Large Language Models (LLMs) can act as a **semantic risk manager** on top of statistical discovery. Because prediction market contracts are defined by natural-language event descriptions and economic rulebooks, an LLM prompted with the event pair can assess whether a credible, plausible real-world economic transmission mechanism connects the leader to the follower. By re-ranking statistically screened candidate pairs using LLM semantic plausibility scores, the system filters out fragile, spurious correlations and truncates severe downside losses under changing market regimes.

### Research interpretation

The falsifiable mechanism is an information diffusion delay and economic transmission screen across event-driven prediction markets:
1. **Information Diffusion Asymmetry:** Macroeconomic signals propagate non-synchronously across prediction markets. Primary or high-salience event contracts (e.g., headline CPI, GDP, or major regional economic indicators) reprice rapidly, whereas downstream or cross-border follower contracts reprice with a lag of 1 to several days due to market segmentation, thinner liquidity, or bounded participant attention.
2. **Asymmetric Risk Management Channel:** The dominant value of semantic LLM filtering is not generating outlier winning trades or predicting price spikes, but **truncating the left tail (downside risk)**. In financial and prediction markets, spurious statistical correlations typically fail because the underlying co-movement was co-incidental; when the market experiences a stress regime or discrete shock, the follower moves contrary to the naive correlation, generating catastrophic losses. Semantic filtering deprioritizes relationships that lack causal transmission channels, reducing average loss severity by 46.5% while leaving average win sizes largely unchanged.
3. **Competing Explanations & Ablations:**
   - *Trivial Lexical Overlap:* The authors demonstrate that the loss reduction persists for genuinely distinct event pairs (48.1% loss reduction) just as strongly as for same-event threshold pairs (42.9% loss reduction).
   - *Lookahead / Pretraining Leakage:* A post-cutoff evaluation on test periods after May 31, 2024 (past the LLM's public training data cutoff) confirms that loss reduction persists at 40.3% ($-\$700$ down to $-\$418$) and total PnL improves by +89%, indicating the mechanism relies on generalized reasoning about economic linkages rather than memorized historical market trajectories.

## Signal

### Source-reported construction

The strategy operates via a two-stage hybrid screening and signal-triggered execution protocol:

#### 1. Preprocessing & Log-Odds Transformation
- For each event contract $i$, observe the daily YES price $p_{i,t} \in [0, 100]$ (cents, representing implied probability in percent) at time $t$ over an observation window $T$.
- Transform prices into unbounded log-odds signals:
  $$\ell_{i,t} = \log\left(\frac{p_{i,t}}{100 - p_{i,t}}\right) \in \mathbb{R}$$
  This mitigates probability compression near 0 and 100 and renders probability innovations additive.
- Stationarity testing: Perform Augmented Dickey-Fuller (ADF) unit-root tests within each 60-day training window; apply first-differencing when non-stationarity is detected.

#### 2. Statistical Discovery Stage (Granger Causality Screening)
- For every unordered event pair $\{i, j\}$ in the active universe, test both directed orientations $(i \to j)$ and $(j \to i)$ using bivariate Vector Autoregressive (VAR) models:
  $$y_t = \alpha_0 + \sum_{k=1}^p \alpha_k y_{t-k} + \sum_{k=1}^p \beta_k x_{t-k} + \varepsilon_t$$
- Lag parameter sweep: $p \in \{1, 2, 3, 4, 5\}$ days.
- Evaluate the null hypothesis $H_0: \beta_1 = \dots = \beta_p = 0$ via F-test / Wald test. Retain the lag length and direction exhibiting the strongest statistical evidence (lowest $p$-value).
- Directional sign of co-movement: Compute Pearson correlation on the stationary series:
  $$s(L \to F) = \mathrm{sgn}(\mathrm{corr}(x_{L,t}, x_{F,t})) \in \{-1, +1\}$$
  where $s = +1$ denotes aligned co-movement and $s = -1$ denotes opposing movement.
- Candidate set selection: Retain the top $K = 100$ directed leader-follower pairs $(L \to F)$ ranked by statistical significance ($p$-value).

#### 3. Semantic Filtering Stage (LLM Re-Ranking)
- Prompt a frozen large language model (`GPT-5-nano` in baseline, `GPT-5-mini` in robustness check) with the candidate pair's event titles and descriptions:
  ```text
  Analyze this prediction market event pair for causal relationship:
  Leader: {Leader Event Title}
  Follower: {Follower Event Title}

  Assess:
  1. Is there a real economic/causal mechanism (not just correlation)?
  2. Strength: high/medium/low/none
  3. Sign: positive (same direction) or negative (opposite)

  Respond in JSON:
  {
    "has_mechanism": true/false,
    "strength": "high/medium/low/none",
    "sign": "positive/negative",
    "reason": "brief explanation"
  }

  Be skeptical - many statistical correlations are spurious.
  ```
- Re-rank the $K = 100$ candidate pairs using the semantic plausibility scores and mechanism validity, selecting the top $M = 20$ directed pairs to form the active trading portfolio.

#### 4. Signal-Triggered Trade Execution
- **Step 1: Leader Trigger:** At day $t$, compute the one-day relative price change of the leader event:
  $$r_{L,t} = \frac{p_{L,t} - p_{L,t-1}}{p_{L,t-1}}$$
  A trade signal is triggered if $|r_{L,t}| > \theta$, where $\theta \ge 0$ is a predefined threshold (default $\theta = 0$, evaluating all non-zero repricings; also evaluated at discrete moves $\ge 5$ pt and $\ge 10$ pt).
- **Step 2: Follower Entry:** At day $t+1$, enter a position in follower event $F$ with direction:
  $$d_t = \mathrm{sign}(r_{L,t}) \times s(L \to F)$$
  If $d_t = +1$, buy YES contracts (long exposure to follower event probability). If $d_t = -1$, sell YES contracts (or buy NO contracts, short exposure to follower event probability).
- **Position Sizing:** Fixed position size of 100 contracts per trade.
- **Step 3: Holding Period & Exit:** Mechanically hold the position for a fixed horizon of $h$ days, exiting at time $t + h + 1$ at the prevailing market price. Realized PnL equals the follower price change multiplied by position size and trade direction. Default $h = 7$ days; ablated across $h \in \{1, 3, 5, 7, 10, 14, 21\}$.

### Underspecified source details

The source explicitly details the conceptual algorithm, statistical pipeline, prompt, and trading results, but leaves several execution mechanics underspecified:
- **Exact Numeric Re-Ranking Function:** While the prompt outputs `has_mechanism`, `strength` (high/medium/low/none), and `sign`, the exact algebraic formula used to sort the top $K=100$ into the final $M=20$ portfolio (e.g., whether ties in `strength` fall back to the Granger $p$-value) is described qualitatively rather than by an explicit mathematical tie-breaking formula.
- **Overlapping Signal Policy:** When a leader fires signals on multiple consecutive days, the paper does not specify whether follower positions are stacked up to a maximum leverage limit or whether subsequent signals are ignored while a position is already open.
- **Order Execution Frictions:** Trades are evaluated at daily closing/settlement prices; bid-ask spreads, order book depth, execution slippage, and exchange transaction fees are not subtracted in the reported PnL tables.

### Research-proposed testable operationalization

To independently reconstruct this strategy in a rigorous, leakage-safe environment:
1. **Deterministic Tie-Breaking Metric:** Construct an explicit scalar semantic score:
   $$\text{Score}(L \to F) = \mathbf{1}_{\{\text{has\_mechanism}=\text{true}\}} \times w_{\text{strength}} \times \mathbf{1}_{\{\text{LLM\_sign} = s(L \to F)\}} - \lambda \cdot \text{Rank}_{\text{Granger}}$$
   where $w_{\text{strength}} \in \{3, 2, 1, 0\}$ for `{high, medium, low, none}`, verifying semantic alignment with the empirical correlation sign.
2. **Single-Position Lockout:** Disallow position stacking; if contract $F$ currently has an open position, ignore new entry triggers for $F$ until the $h$-day horizon expires.
3. **Execution Modeling:** Apply Kalshi's exact taker fee schedule and deduct a mandatory 1-cent to 2-cent half-spread penalty upon entry and exit.

## Required data

- **Venue:** Kalshi (CFTC-regulated prediction market).
- **Universe:** 554 active contracts within the Kalshi "Economics" category (e.g., inflation/CPI, Fed policy, GDP growth, recession markers, employment, oil production, delinquency rates).
- **Time Series Fields:** Daily implied probability / YES settlement prices $p_{i,t} \in [0, 100]$.
- **Metadata Fields:** Contract titles, natural language market descriptions, resolution criteria, and expiry dates.
- **Point-in-Time & Lag Requirements:**
  - Training window: 60 days strictly preceding the test window.
  - Entry delay: Signal evaluated at close of day $t$; execution strictly at day $t+1$ to eliminate look-ahead leakage.
  - Prompt integrity: Event descriptions provided to the LLM must only contain contract specifications and economic definitions, never historical market performance, trading statistics, or realized settlement outcomes.
- **Missing Data & Filtering:** Markets with insufficient trading activity or negligible price variation over the lookback window are excluded from the candidate pool prior to VAR estimation.

## Execution assumptions

### Source-reported

- **Execution Cadence:** Daily close-to-close evaluation; trade triggered at day $t$, entered at day $t+1$, and exited mechanically at day $t+h+1$.
- **Position Sizing:** Fixed allocation of 100 contracts per active trade.
- **Transaction Costs & Spread:** Assumed zero in primary reported backtest tables (gross price change evaluation).

### Research interpretation

- **Spread Friction:** Real-world prediction market order books on Kalshi frequently feature wide bid-ask spreads (1¢ to 5¢ on 100¢ contracts). Because average win per trade is $\$636$ on 100 contracts ($\approx 6.36$ cents/contract) and average loss is $-\$347$ ($\approx 3.47$ cents/contract), crossing a 2-cent spread on both entry and exit (4 cents round-trip) would absorb a substantial portion of the trading edge.
- **Capacity:** With fixed sizing of 100 contracts (approx. $\$10$ to $\$90$ capital at risk per contract depending on probability), the paper operates well within Kalshi retail liquidity; however, scaling the strategy to institutional size would encounter severe liquidity constraints and market impact in niche economic contracts.

## Evidence

### Source-reported

All figures below trace directly to Sumin Kim et al. (arXiv:2602.07048v1, February 2026), evaluated across 18 rolling 30-day out-of-sample test windows from October 2021 to November 2025:

#### 1. Primary Portfolio Performance (Default: $h = 7$ days, $\theta = 0$, $M = 20$, Table 1)
- **Win Rate:**
  - Statistical Approach (Granger only): **51.4%**
  - Hybrid Approach (Granger + LLM): **54.5%** (+3.1 percentage points)
- **Average Win:**
  - Statistical Approach: **$724**
  - Hybrid Approach: **$636** (-12%)
- **Average Loss (Downside Control):**
  - Statistical Approach: **-$649**
  - Hybrid Approach: **-$347** (**+46.5% reduction in loss magnitude**)
- **Total PnL:**
  - Statistical Approach: **$4,100**
  - Hybrid Approach: **$12,500** (**+205% improvement**)

#### 2. Downside Loss Reduction Decomposition (Table 2)
- **Same-Event Pairs (different strikes/thresholds):**
  - Statistical Approach Avg Loss: **-$700**
  - Hybrid Approach Avg Loss: **-$400** (Loss Reduction: **42.9%**)
- **Different-Event Pairs (genuinely distinct economic series):**
  - Statistical Approach Avg Loss: **-$642**
  - Hybrid Approach Avg Loss: **-$333** (Loss Reduction: **48.1%**)

#### 3. Win Rate by Leader Move Magnitude (Table 3)
- **5–10 pt leader move:** Statistical WR **57.1%** vs. Hybrid WR **66.7%** (+9.5 pp, Hybrid outperforming)
- **10+ pt leader move:** Statistical WR **53.8%** vs. Hybrid WR **71.4%** (+17.6 pp, Hybrid outperforming)

#### 4. Representative High-Value Rescued Pairs (Table 4)
- *China 2022 GDP Growth >5% $\to$ World 2022 GDP Growth >3%:* Statistical Rank #23 $\to$ Hybrid Rank #17, PnL **+$1,100**
- *Japan 2026 Recession $\to$ US Q1 2025 GDP Growth >2%:* Statistical Rank #71 $\to$ Hybrid Rank #5, PnL **+$700** (LLM inferred negative cross-border trade/financial spillover mechanism despite weak Granger $p$-value)
- *US 2025 Oil Prod. >14.5M bbl/day $\to$ Brazil 2025 Inflation >5.5%:* Statistical Rank #24 $\to$ Hybrid Rank #15, PnL **+$600**
- *India 2026 Recession $\to$ CRE Delinq. Q4 2024 >3%:* Statistical Rank #51 $\to$ Hybrid Rank #3, PnL **+$200**

#### 5. Holding Horizon Ablation ($h \in \{1, \dots, 21\}$ days, Table 5)
- **1 day:** Stat WR 56.0%, Hybrid WR 66.7%; Stat Loss -$536, Hybrid Loss -$283 (Loss Reduction: **47.2%**)
- **3 days:** Stat WR 44.7%, Hybrid WR 62.8%; Stat Loss -$773, Hybrid Loss -$469 (Loss Reduction: **39.4%**)
- **5 days:** Stat WR 47.5%, Hybrid WR 66.0%; Stat Loss -$745, Hybrid Loss -$500 (Loss Reduction: **32.9%**)
- **7 days:** Stat WR 51.4%, Hybrid WR 54.5%; Stat Loss -$649, Hybrid Loss -$347 (Loss Reduction: **46.5%**)
- **10 days:** Stat WR 51.4%, Hybrid WR 56.9%; Stat Loss -$497, Hybrid Loss -$371 (Loss Reduction: **25.3%**)
- **14 days:** Stat WR 49.5%, Hybrid WR 56.1%; Stat Loss -$661, Hybrid Loss -$400 (Loss Reduction: **39.5%**)
- **21 days:** Stat WR 47.3%, Hybrid WR 53.1%; Stat Loss -$973, Hybrid Loss -$753 (Loss Reduction: **22.6%**)
- **Mean Across Horizons:** Stat WR $\sim 50\%$, Hybrid WR $\sim 59\%$; Stat Loss -$689, Hybrid Loss -$446 (Mean Loss Reduction: **36.2%**)

#### 6. Post-Cutoff Lookahead Audit (Entry Date > May 31, 2024, Table 6)
- Statistical Approach: WR 61.8%, Avg Win $614, Avg Loss -$700, Total PnL **$3,800**
- Hybrid Approach: WR 62.1%, Avg Win $656, Avg Loss -$418, Total PnL **$7,200** (**+89% improvement**, loss reduction: **40.3%**)

### Independently reproduced

`not independently reproduced`

### Negative evidence

- **Fragility of Pure Statistical Granger Discovery:** The paper demonstrates that relying on statistical Granger causality alone produces an out-of-sample win rate of only 51.4% and an average loss ($-\$649$) nearly matching the average win ($\$724$), yielding a meager gross profit of $\$4,100$ across 18 evaluation periods that would likely turn negative after realistic execution fees and bid-ask spreads.
- **Horizon Decay:** At extended holding horizons ($h = 21$ days), loss reduction degrades to 22.6% and average losses expand significantly ($-\$753$), as unmodeled macro events and contract expiry convergence inject noise that dilutes the initial lead-lag transmission.
- **Omission of Friction in Empirical Claims:** Because all reported figures are gross of exchange fees and bid-ask spread crossing, the true net tradability on Kalshi remains unproven.

## Falsification plan

1. **Transaction Cost & Spread Stress Test:** Apply Kalshi's regulatory fee structure and simulate crossing a 1¢, 2¢, and 3¢ half-spread upon entry and exit.
   - *Falsification Threshold:* Reject tradability if net Sharpe ratio becomes non-positive or if total net PnL across the 18 rolling windows falls below zero at a 1.5-cent half-spread.
2. **Placebo Semantic Scoring Ablation:** Replace LLM plausibility scores with:
   - (a) uniform random ranking;
   - (b) purely lexical text overlap (BM25 or character n-gram cosine similarity);
   - (c) inverted semantic scores (prioritizing pairs deemed "no mechanism" or "spurious").
   - *Falsification Threshold:* Reject the semantic causal transmission hypothesis if random or lexical screening matches or exceeds the loss reduction of the LLM hybrid approach.
3. **Causal Sign Inversion Test:** Mechanically invert the sign $s(L \to F)$ so the strategy trades against the identified direction.
   - *Falsification Threshold:* If inverted sign trading yields positive PnL or higher win rates, the directional mechanism is falsified.
4. **Non-Economic Event Generalization:** Evaluate the hybrid pipeline on non-macro event categories (e.g., sports, entertainment, weather).
   - *Falsification Threshold:* Materially weaken the claim of general causal reasoning if the LLM cannot differentiate plausible lead-lag relationships in other structured domains.
5. **Execution Latency Audit:** Vary execution timing from $t+1$ to $t+2$ and $t+3$.
   - *Falsification Threshold:* Reject if the predictive advantage is entirely consumed within 24 hours of signal generation.

## Crypto portability

**adapted / unproven**

While Kalshi is a regulated US event exchange, prediction markets also exist natively on decentralized blockchains (e.g., Polymarket on Polygon, Limitless on Base, Azuro on Arbitrum). Porting this strategy to crypto prediction markets is an adapted research hypothesis:
- **Market Structure & Settlement:** Polymarket operates a central limit order book (CLOB) settled in USDC, with binary outcome tokens ERC-1155 redeemable at $\$1.00$ or $\$0.00$. The underlying log-odds transformation and directional lead-lag mechanics map conceptually to crypto prediction markets.
- **Oracle & Resolution Dynamics:** Unlike Kalshi's internal regulatory settlement, crypto prediction markets rely on decentralized oracles (e.g., UMA Optimistic Oracle), introducing resolution dispute risks, bonding delays, and oracle lag.
- **Liquidity & Spread Frictions:** Crypto prediction markets outside high-profile political or top-tier crypto events exhibit fragmented liquidity and wide spreads, increasing execution drag.
- **24/7 Trading vs. Macro Release Alignment:** Macro-focused Kalshi contracts trade around scheduled US government data releases (CPI, Non-Farm Payrolls, FOMC). Decentralized crypto prediction markets trade 24/7 globally, meaning leader repricings can occur at arbitrary UTC timestamps, requiring continuous sub-hourly monitoring rather than daily closing bars.
- Portability of this mechanism to crypto prediction markets or cross-market crypto spot/perpetuals remains **unproven** until verified on decentralized order book archives.

## Limitations

- **underspecified:** exact algebraic rank score for tie-breaking and overlapping position handling are omitted.
- **data gap:** lack of bid-ask spread, order book depth, and transaction fee integration in reported empirical PnL.
- **not independently reproduced:** findings rely exclusively on the reported results in arXiv:2602.07048v1.
- **closed-source LLM dependency:** reliance on proprietary models (`GPT-5-nano` / `GPT-5-mini`) creates reproducibility and model-drift risks across API updates.
- **sample limitation:** restricted to 554 contracts in the Kalshi Economics category over a 4-year period (2021-2025).

## Implementation status

`not-implemented`

No PyBroker, Nautilus, live bot, paper, or testnet trading system has been implemented in our research stack.

## Adoption boundary

This record is `research-only`, `not-implemented`, and `not-approved`. It represents normalized research material staged for subsequent ChatGPT Research Intake Review. It does not authorize capital allocation, implementation, paper trading, testnet verification, or live trading.

## Related Wiki records

- `[[quant/crypto-kalshi-prediction-market-macro-repricing-volatility-forecasting-2026-09-01]]` — uses Kalshi macro contract repricing to forecast crypto realized volatility; contrasts with within-market lead-lag directional trading.
- `[[quant/polymarket-binance-high-frequency-binary-lead-lag-2026-09-02]]` — high-frequency cross-venue lead-lag between prediction markets and crypto spot/perpetuals; contrasts with macro contract-to-contract lead-lag.
- `[[quant/crypto-time-dependent-weighted-directed-network-granger-causality-2026-09-01]]` — rolling Granger causality network for cryptocurrency tokens; contrasts with hybrid LLM semantic filtering.
- `[[quant/retail-agent-structured-adverse-timing-contrarian-alpha-2026-09-02]]` — behavioral LLM trading dynamics.

## Sources

1. Sumin Kim, Minjae Kim, Jihoon Kwon, Yoon Kim, Nicole Kagan, Joo Won Lee, Oscar Levy, Alejandro Lopez-Lira, Yongjae Lee, and Chanyeol Choi, *"LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets"*, arXiv preprint `arXiv:2602.07048v1 [q-fin.RM, q-fin.ST]`, submitted February 4, 2026. DOI: [10.48550/arXiv.2602.07048](https://doi.org/10.48550/arXiv.2602.07048). Stable URL: [https://arxiv.org/abs/2602.07048](https://arxiv.org/abs/2602.07048). Full text HTML: [https://arxiv.org/html/2602.07048v1](https://arxiv.org/html/2602.07048v1).
2. arXiv:2602.07048v1 primary LaTeX source files, including `ICLR_main.tex`, `table_main_decomp_movement/tab_main.tex`, `tab_decomp.tex`, `tab_movement.tex`, `table/tab_ablation.tex`, `table/tab_representative_pairs.tex`, `table/tab_training_cutoff.tex`, and `plots/prompt_hybrid.png`.
