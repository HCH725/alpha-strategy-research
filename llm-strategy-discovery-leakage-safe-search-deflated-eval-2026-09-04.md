---
schema: strategy-research-record-v1
title: "What Survives Honest Evaluation? Leakage-Safe, Search-Aware Deflated Sharpe Assessment of LLM-Driven Trading Strategy Discovery"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - negative-result
  - llm-strategy-discovery
  - deflated-sharpe
  - leakage-safe
  - backtest-overfitting
  - multi-asset
  - us-equities
status: research-only
confidence: high
source_as_of: 2026-08-27
sources:
  - "https://arxiv.org/abs/2608.27734"
  - "https://doi.org/10.48550/arXiv.2608.27734"
  - "https://doi.org/10.5281/zenodo.21261868"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# What Survives Honest Evaluation? Leakage-Safe, Search-Aware Deflated Sharpe Assessment of LLM-Driven Trading Strategy Discovery

## Provenance

- **Author:** Eray Gençay (Independent Researcher, Stuttgart, Germany)
- **arXiv ID:** `arXiv:2608.27734v1 [q-fin.PM]`
- **Submission Date:** 2026-08-27T21:50:28Z
- **DOI:** [10.48550/arXiv.2608.27734](https://doi.org/10.48550/arXiv.2608.27734)
- **Code & Artifact Archive:** Zenodo DOI [10.5281/zenodo.21261868](https://doi.org/10.5281/zenodo.21261868) (Statistical evaluation engine, offline test suite, experiment configurations, canonical run manifests, and search traces)
- **Data Sources Cited:** Tiingo (daily OHLCV), SEC EDGAR, GDELT, FRED

**Primary Source Verification:** Full text HTML (`https://arxiv.org/html/2608.27734v1`) was retrieved and read directly. All empirical claims, experiment identifiers (E1–E6b), performance statistics, sample windows, transaction cost models, and mathematical definitions match the primary text without secondary summarization.

## Economic mechanism

### Source-reported

The paper investigates why LLM-driven trading strategy discovery frequently generates impressive backtest figures that fail out-of-sample or under live trading. The author identifies two structural failure modes prevalent in the machine-learning and LLM finance literature:
1. **Look-ahead leakage:** Generated code or unconstrained expressions access future information (e.g., end-of-day prices before close, misaligned corporate filings, or future target returns).
2. **Search-intensity inflation (Selection Bias):** Autonomous LLM agents propose, evaluate, and refine dozens to hundreds of strategy candidates in iterative loops. Reporting only the winning strategy without penalizing the trial count inflates performance via data mining.

The author argues that statistical deflation and leakage guardrails must be **structural** rather than procedural:
- A deliberately leaky oracle achieves an astronomical Sharpe ratio of 34.7 in-sample and survives statistical Deflated Sharpe Ratio (DSR = 1.00) testing, proving that statistical correction alone cannot catch look-ahead bias.
- Conversely, strict point-in-time hygiene cannot prevent selection luck when search intensity is high.
- Under an honest framework where the agent can only compose declarative plans via a type-safe registry tool surface and where every candidate evaluation increments an immutable trial ledger, the author evaluates classic factor baselines, autonomous LLM discoveries (across OpenAI `gpt-4.1` and Anthropic `claude-sonnet-5`), multi-asset ETF premia, and a human production trend-following rule engine on Gold (`GLD`).

### Research interpretation

This paper represents a rigorous empirical audit and negative-result benchmark for agentic alpha discovery. Key findings include:
- **Autonomous LLM Factor Discovery Fails Deflated Certification:** In an unconstrained 102-trial search on US equities, the agent discovers an interpretable contrarian book (RSI x volume z-score) with an attractive in-sample Sharpe ratio of 1.69. However, when deflated by its own trial count and candidate dispersion, its Deflated Sharpe Ratio is 0.86 (below the 0.95 significance threshold), and its out-of-sample Sharpe ratio collapses to 0.18 (+4.7% return vs. +40.8% buy-and-hold).
- **Classic Cross-Sectional Factors Fail Market-Neutral Cost Hurdles:** On a 453-stock universe (PIT top 200 liquid names) after realistic transaction costs, square-root market impact, and borrow fees, classic momentum, short-term reversal, and low-volatility market-neutral books fail to clear DSR significance (DSR <= 0.32, PBO = 0.83).
- **Human Production Rule System Regime Fragility:** A pre-registered production trend-following PineScript system on Gold (`GLD`) with 84 signal nodes, slope gating, and candle-anatomy filters was profitable across its 2007–2016 design decade (Sharpe 0.33, +34% return, PSR = 0.85), but collapsed out-of-sample in 2017–2025 (Sharpe -0.12, -13% return, paired bootstrap p < 0.001 vs. Gold buy-and-hold +257%), forfeiting the historic bull run due to its flat/short states.
- **Power Arithmetic Constraint:** Because a t-statistic on the Sharpe ratio scales as SR * sqrt(years), certifying a moderate edge (SR ~ 0.6) requires over a decade of held-out data or massive cross-sectional breadth. Four-year evaluation windows have near-zero power to distinguish real moderate alpha from noise.

## Signal

The paper defines strategies declaratively as **plans**, avoiding free-form code execution. A plan consists of:
1. **Feature specifications:** Strongly typed feature names with explicit parameters from an allow-listed registry (e.g., `momentum(window=252)`).
2. **Signal graph:** Directed acyclic graph of named nodes computing arithmetic, comparisons, rolling statistics, or non-negative lags (t - k, k >= 0).
3. **Signal combination:** Weighted sum of terminal signal nodes.
4. **Portfolio archetype:** Translates continuous signals or discrete conditions into target portfolio weights.

### Registered Archetypes

The primary source defines five portfolio archetypes:
1. `linear_tilt`: Continuous weight proportional to signal score.
2. `rank_long_short`: Cross-sectional rank long/short (top-k long, bottom-k short, equal-weighted within quantile, with re-ranking cadence parameter).
3. `volatility_targeting`: Scales base archetype weights by trailing realized volatility to meet a fixed portfolio volatility target.
4. `random_weights_null`: Deterministic random-weights baseline.
5. `rule_long_short`: Stateful execution engine reading four named condition nodes (`long_entry`, `long_exit`, `short_entry`, `short_exit`). Flat books enter on entry condition; positions hold until exit condition fires; same-bar entry and exit on the same side is blocked; supports decision cadence (e.g., weekly evaluation on daily bars).

### Evaluated Strategies

1. **Autonomous LLM Discovery (E3 - Headline find):**
   - **Hypothesis:** Contrarian reversal conditioned on volume expansion.
   - **Signal components:** Interaction between Relative Strength Index (RSI) and volume z-score.
   - **Archetype:** Cross-sectional rank long/short (`rank_long_short`), monthly re-ranking cadence.
   - **Specification status:** Parameter windows and exact node transforms are stored in the Zenodo run manifest `N=102`; general structure fully specified.
2. **Classic Factors Baseline (E2):**
   - **126-day Momentum:** Top/bottom rank long/short book on trailing 126-day cumulative return.
   - **Short-term Reversal:** Top/bottom rank long/short book on trailing short-term return (5-day).
   - **Low-Volatility:** Long low-volatility / short high-volatility rank book.
   - **Execution:** Market-neutral dollar-neutral long/short rebalanced on 21-day cadence.
3. **Multi-Seed LLM Consensus (E4):**
   - 5 independent `gpt-4.1` runs of 18 candidates each converged on the **volatility-breakout** family (combining realized volatility spikes with directional breakout triggers).
4. **Cross-Model LLM Replication (E4):**
   - `claude-sonnet-5` (100 candidates) explored 39 feature combinations; best candidate was a **price-to-moving-average spread** long/short signal.
5. **Multi-Asset Divergence Signal (E5):**
   - Pre-registered human hypothesis: Cross-asset price/oscillator divergence signal across 39 ETFs.
6. **Human Production Trend-Following Engine (E6b):**
   - Target instrument: SPDR Gold Shares (`GLD`).
   - Signal graph: 84 named nodes translating an original production PineScript system.
   - Core rules: Linear-regression slope trend filter, candle-anatomy filters (wick/body ratios), and an oscillator divergence hold/exit test inside a state machine (`rule_long_short`).
   - Timeframe: Discrete weekly decision cadence evaluated on daily bars.
   - Position state: All-in (+1.0), flat (0.0), or short (-1.0) [research-proposed interpretation of all-in/all-out state].

## Required data

### Universes

- **US Equities Universe (E1–E4):**
  - Scope: 453 liquid US large-capitalization equities plus `SPY` benchmark.
  - Source: Tiingo daily adjusted OHLCV bars (2015–2026).
  - Point-in-time selection: Tradeable universe dynamically restricted to the top 200 names by trailing 63-day dollar volume, re-selected every 21 trading days (eliminates universe-selection look-ahead).
  - Survivorship handling: Fixed modern constituent list (contains survivorship bias favoring active momentum/trend, making the null result conservative); includes eight names that delisted mid-sample.
- **Multi-Asset ETF Universe (E5–E6b):**
  - Scope: 39 multi-asset ETFs spanning country equities, sector equities, US Treasuries, corporate credit, gold (`GLD`), commodities, currencies, and Bitcoin (`BITO`/crypto-proxies) (2005–2026).
  - Timeframe: Daily bars; weekly decision cadence for E6b.

### Sample Partitions

- **Equities (E1–E4):**
  - Design (In-Sample Search): 2017-01-01 to 2021-12-31 (5 years).
  - Evaluation (Held-Out Test): 2022-01-01 to 2025-12-31 (4 years).
- **Multi-Asset ETFs (E5–E6b):**
  - Design (In-Sample): 2007-01-01 to 2016-12-31 (10 years).
  - Evaluation (Held-Out Test): 2017-01-01 to 2025-12-31 (9 years).

## Execution assumptions

All assumptions below are explicitly defined by the primary source in Section 5:
- **Execution Lag:** Signals formed at close of day t using data up to and including t are entered at day t+1 (global 1-day execution lag enforced by the backtest engine; no same-close fills).
- **Commission:** 1 basis point (0.01%) per trade.
- **Bid/Ask Spread:** 2 basis points (0.02%) per trade.
- **Market Impact:** Square-root market impact model calibrated against trailing 21-day average dollar volume: Impact proportional to sigma * sqrt(Order Size / ADV_21).
- **Short Borrow Financing:** 50 basis points (0.50%) annualized cost on short notional value.
- **Cost Sensitivity Grid (E4):** Halved costs (0.5x) and doubled costs (2.0x) evaluated to test robustness.
- **Fill Model:** Assumes full fills at daily bar execution price subject to impact and spread penalties [source-reported].
- **Intraday Latency / Fill Failure:** Not modeled on daily OHLCV bars [source gap noted].

## Evidence

### Source-reported

All figures below are transcribed directly from Tables 2, 3, 4, 5, 6, and 7 of arXiv:2608.27734v1:

#### Table 2: E1 Leakage vs. Deflation Test (453-stock US Equities, PIT top-200; Design 2017–2021, Eval 2022–2025)

| Arm | Design SR | Eval SR | DSR | Notes |
| :--- | :---: | :---: | :---: | :--- |
| **Look-ahead oracle (unsafe)** | 34.7 | 51.5 | 1.00 | Tomorrow return today; survives DSR completely |
| **Buy-and-hold (equal-weight)** | 1.15 | 0.60 | 0.99 | Passive risk premium certified |
| **SPY buy-and-hold** | 0.98 | 0.67 | 0.97 | Passive benchmark certified |
| **Random floor** | 0.06 | -0.09 | 0.46 | Noise floor |
| **Momentum L/S (safe)** | -0.07 | 0.01 | 0.35 | Market-neutral 126d momentum fails |

*Key finding:* A look-ahead contaminated signal with Sharpe 34.7 easily bypasses statistical DSR (DSR = 1.00), proving statistical deflation alone cannot substitute for structural execution guardrails.

#### Table 3: E2 Baseline Classic Price Factors (Same universe/windows, N=9 trials, PBO = 0.83)

| Arm | Design SR | Eval SR | DSR | Notes |
| :--- | :---: | :---: | :---: | :--- |
| **Buy-and-hold (equal-weight)** | 1.15 | 0.60 | 0.97 | Certified (DSR >= 0.95) |
| **SPY buy-and-hold** | 0.98 | 0.67 | 0.94 | Borderline certification |
| **Random floor** | 0.06 | -0.09 | 0.32 | Zero edge |
| **Short-term reversal L/S** | -0.04 | -0.20 | 0.25 | Fails cost hurdle |
| **Momentum L/S** | -0.07 | 0.01 | 0.22 | Fails cost hurdle |
| **Low-volatility L/S** | -0.58 | -0.78 | 0.03 | Severely negative net of costs |

#### Table 4: E3 Autonomous LLM Discovery (OpenAI `gpt-4.1`, N=102 recorded trials, PBO = 0.01)

| Arm | Design SR | Eval SR | Eval Total Return | DSR |
| :--- | :---: | :---: | :---: | :---: |
| **Agent Discovery (RSI x volume)** | 1.69 | 0.18 | +4.7% | 0.86 |
| **Buy-and-hold (equal-weight)** | 1.15 | 0.60 | +40.8% | 0.45 |
| **SPY buy-and-hold** | 0.98 | 0.67 | +51.5% | 0.31 |
| **Momentum reference** | -0.07 | 0.01 | -1.6% | 0.00 |
| **Random floor** | 0.06 | -0.09 | -1.0% | 0.01 |

*Evaporation dynamics:* The agent raw in-sample Sharpe rose from -0.07 to 1.69 over 102 trials. However, the selection threshold required by DSR rose to 1.21. With candidate variance, DSR reached only 0.86 (below 0.95), and out-of-sample performance collapsed to Sharpe 0.18 (+4.7% vs. +51.5% SPY).

#### Table 5: E4 Robustness of the Null

- **Cost halving (0.5x):** Best factor (reversal) DSR = 0.46; Buy-and-hold DSR = 0.96.
- **Cost doubling (2.0x):** Best factor (momentum) DSR = 0.14; Buy-and-hold DSR = 0.96.
- **Universe top-100 names:** Best factor (momentum) DSR = 0.62, Eval SR = 0.71; Buy-and-hold DSR = 0.73.
- **Universe top-300 names:** Best factor (reversal) DSR = 0.25, PBO = 0.91; Buy-and-hold DSR = 0.98.
- **Multi-Seed LLM Discovery (5 independent `gpt-4.1` runs, N=18 trials each):** 5/5 valid; all converged on the volatility-breakout family; Eval SR ranged 0.59–0.70 (+26% to +33% return); DSR ranged 0.15–0.29; **0/5 survived certification**.
- **Cross-Model Replication (`claude-sonnet-5`, 100 trials, 80/100 valid):** Explored 39 feature combinations. Best find was price-to-moving-average spread with design SR 0.44, collapsing to eval SR -0.33 (-29% return), DSR = 0.18, PBO = 0.51.

#### Table 6: E5 Fair Field Multi-Asset ETF Benchmark (39 ETFs; Design 2007–2016, Eval 2017–2025; N=20, PBO = 0.80)

| Arm | Design SR | Eval SR | Eval Return | Eval 95% Stationary-Bootstrap CI |
| :--- | :---: | :---: | :---: | :---: |
| **SPY buy-and-hold** | 0.42 | 0.85 | +249% | [+0.24, +1.53] (Certified) |
| **B&H (39 ETFs equal-weight)** | 0.33 | 0.71 | +108% | [+0.07, +1.46] (Certified) |
| **Time-Series Momentum (TSM long/flat)** | 0.42 | 0.49 | +55% | [-0.13, +1.24] (Under-powered) |
| **Cross-Sectional Momentum L/S** | 0.24 | 0.20 | +12% | [-0.39, +0.82] |
| **Divergence (Pre-registered Human)** | 0.34 | -0.15 | -13% | [-0.73, +0.56] |
| **Random floor** | -0.57 | 0.55 | +23% | [-0.06, +1.18] |
| **Agent discovery (LLM)** | 0.37 | -0.23 | -21% | [-0.82, +0.33] |

*Key finding:* Only passive risk premia (SPY and 39-ETF buy-and-hold) achieve 95% confidence intervals strictly excluding zero over the 9-year evaluation window. TSM returned +55%, but its t-statistic (t ~ 0.49 * sqrt(9) ~ 1.5) leaves the CI spanning zero.

#### Table 7: E6b Ported Human Production System on Gold (`GLD`, N=1 Pre-registered)

| Arm | Design SR / Return | Eval SR / Return | Eval 95% CI | Paired Bootstrap p-value vs. Gold |
| :--- | :---: | :---: | :---: | :---: |
| **Gold buy-and-hold** | 0.38 / +75% | 1.04 / +257% | [+0.42, +1.62] | — |
| **SPY buy-and-hold** | 0.42 / +92% | 0.85 / +249% | [+0.24, +1.53] | 0.94 |
| **Production System (PineScript port)** | 0.33 / +34% | -0.12 / -13% | [-0.77, +0.49] | **< 0.001** |

*Key finding:* The human rule engine achieved PSR = 0.85 during its development decade (2007–2016), holding positions only 33% of trading days. However, in the 2017–2025 evaluation window, its cash and short states missed the historic gold rally, generating -13% return vs. +257% for buy-and-hold, statistically rejected by paired bootstrap (p < 0.001).

### Independently reproduced

Not independently reproduced in our execution stack.

### Negative evidence

The paper is an extensive empirical negative-result study:
1. **0 of 100+ LLM-generated strategies survived search deflation:** Across two frontier models (`gpt-4.1` and `claude-sonnet-5`), multiple prompt hints, and 5 repeated seeds, zero agent-discovered strategies achieved DSR significance (DSR >= 0.95).
2. **Deflation does not catch leakage:** Statistical corrections (DSR, PBO) are completely blind to future look-ahead contamination, passing an intentional oracle at DSR = 1.00.
3. **Out-of-sample collapse of in-sample winners:** Strategies with in-sample Sharpe up to 1.69 degraded to near-zero (0.18) or negative out-of-sample Sharpe once subjected to realistic frictions and independent evaluation windows.
4. **Human timing system rejected by buy-and-hold:** The pre-registered PineScript trend system significantly lagged buy-and-hold (p < 0.001) due to regime switching and timing drag during persistent bull runs.

## Falsification plan

### Operational Tests

1. **Trial Ledger Completeness Test:**
   - Verify whether every evaluation call in the research loop is captured in the trial ledger N. If unrecorded iterations or exploratory backtests occurred, recompute DSR with the estimated true trial count N_total.
   - **Research-defined falsification threshold:** If true trial count N exceeds logged trials by >= 2x, downgrade DSR confidence to low; if adjusted DSR < 0.50, reject the candidate completely.
2. **Structural Information Leakage Audit:**
   - Invert the execution timestamp to same-bar close (t). If strategy performance surges by >= 3x Sharpe ratio, look-ahead leakage is active.
   - **Research-defined falsification threshold:** Any strategy whose Sharpe ratio drops by > 50% when moving from same-close fill (t) to next-bar open/close (t+1) is falsified as execution-leakage dependent.
3. **Out-of-Sample Power Verification:**
   - For any claimed SR ~ 0.6, require a minimum out-of-sample test duration T >= 4 / (SR^2) ~ 11 years to reach statistical significance (t >= 2.0).
   - **Research-defined falsification threshold:** Evaluation windows under 5 years are classified as statistically under-powered for moderate Sharpe strategies (SR <= 0.8).
4. **Cost Sensitivity Stress Test:**
   - Evaluate performance under 2x baseline costs (2 bp commission, 4 bp spread, doubled impact).
   - **Research-defined falsification threshold:** If net Sharpe drops below 0.0 or DSR drops below 0.50 under 2x costs, classify the strategy as a friction casualty.

## Crypto portability

**Portability Status: Adapted / Unproven.**

The mechanisms investigated in the paper originate strictly in traditional financial assets (US equities and multi-asset ETFs). Porting these findings to cryptocurrency perpetual and spot markets requires substantial adaptation:
- **Continuous 24/7 Session vs. Daily US Close:** US equity models rely on 16:00 EST market closes and overnight gaps. Crypto operates continuously; 24h rolling windows and arbitrary 00:00 UTC boundaries change signal autocorrelation and volatility clustering.
- **Funding Rates and Leverage Costs:** In equity long/short books, borrow cost is modeled at 50 bp annualized. In crypto perpetual futures, funding rates fluctuate wildly (often exceeding 20–50% APR during bull markets or negative during liquidations), which can rapidly erase short-side alpha in market-neutral books.
- **Liquidity and Microstructure Slippage:** The square-root market impact model calibrated to US equities (top 200 by ADV) does not account for fragmented order books across Binance, OKX, and Bybit, or toxic flow from MEV and liquidation cascades.
- **Higher Noise-to-Signal Ratio:** If autonomous LLMs overfit 453 liquid US stocks with PBO >= 0.80, the risk of overfitting higher-volatility crypto assets with shorter historical spans is substantially magnified.
- **Porting Recommendation:** Any implementation in crypto must be treated as research-proposed and unproven.

## Limitations

- **Fixed Current Constituent List (Survivorship Bias):** The 453-stock US universe is based on a modern constituent list with only eight mid-sample delistings, creating a positive survivorship bias that flatters active strategies (making the failure of LLM discovery even more pronounced).
- **Daily Bar Coarseness:** The evaluation uses daily OHLCV bars. Intraday price path extremes, queue priority, and slippage spikes during high-volatility sessions are omitted.
- **Constrained Action Space:** LLM discovery was restricted to a predefined registry of price/volume features; news sentiment and SEC fundamental features were excluded for reproducibility.
- **Convergence of LLM Sampling:** Multi-seed discovery runs under default temperatures showed high intra-model convergence (3 of 5 `gpt-4.1` seeds discovered near-identical strategies), limiting true diversity of the search space.
- **Bull Regime Window Dependence:** The 2017–2025 evaluation window was dominated by massive equity and gold bull markets, which structurally penalizes market-neutral, cash-overlay, or short-timing strategies relative to passive buy-and-hold.
- **E6b PineScript Fidelity:** The python port of E6b uses rolling 5-day trading weeks with notional sizing, whereas the original PineScript ran on calendar weeks with spot contracts and fixed lots.

## Implementation status

- `not-implemented`: No implementation exists in our PyBroker or NautilusTrader pipelines.
- Research material only.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

This record is an empirical research capture and methodological benchmark. It does not authorize strategy deployment, paper trading, testnet, or live execution.

## Related Wiki records

- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]` — Canonical Hermes Wiki Brain standard for leakage prevention, purging, embargoing, and combinatorial cross-validation.
- `[[quant/btc-perpetual-factor-mining-point-in-time-audit-negative-2026-09-04]]` — Companion negative-result study on BTC perpetual futures factor mining under strict point-in-time auditing (Zeng et al., arXiv:2608.25348).
- `[[quant/aeap-seads-llm-agentic-factor-discovery-formulaic-alpha-2026-09-03]]` — Agentic factor discovery architecture; subject to the search-deflation critique established here.
- `[[quant/alphar1-context-aware-alpha-screening-llm-reasoning-grpo-2026-09-03]]` — Reasoning-guided alpha screening; provides context on search spaces evaluated by LLMs.

## Sources

1. **Eray Gençay**, "What survives honest evaluation? Leakage-safe, search-aware assessment of LLM-driven trading strategy discovery," *arXiv preprint* `arXiv:2608.27734v1 [q-fin.PM]`, submitted August 27, 2026. DOI: [10.48550/arXiv.2608.27734](https://doi.org/10.48550/arXiv.2608.27734). Full text: https://arxiv.org/abs/2608.27734.
2. **Eray Gençay**, "Replication archive for 'What survives honest evaluation?'", *Zenodo Data Repository*, August 2026. DOI: [10.5281/zenodo.21261868](https://doi.org/10.5281/zenodo.21261868).
3. **David H. Bailey, Jonathan M. Borwein, Marcos López de Prado, Qiji Jim Zhu**, "Pseudo-mathematics and financial charlatanism: The effects of backtest overfitting on out-of-sample performance," *Notices of the AMS*, 61(5):458–471, 2014.
4. **David H. Bailey, Marcos López de Prado**, "The Deflated Sharpe Ratio: Correcting for selection bias, backtest overfitting, and non-normality," *Journal of Portfolio Management*, 40(5):94–107, 2014.
