---
schema: strategy-research-record-v1
title: "PRICE: Parameter-Efficient LoRA Adaptation with Recursive CTF Prompting for Hourly Bitcoin Price Forecasting"
created: 2026-09-16
updated: 2026-09-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-04
sources:
  - "https://arxiv.org/abs/2609.05235"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# PRICE: Parameter-Efficient LoRA Adaptation with Recursive CTF Prompting for Hourly Bitcoin Price Forecasting

## Provenance

- **Primary Source:** Maryam Fakhari (`m.fakhari@ec.iut.ac.ir`) and Mehran Safayani (`safayani@iut.ac.ir`), Department of Electrical and Computer Engineering, Isfahan University of Technology, Isfahan, Iran.
- **Paper Title:** *"PRICE: A Systematic Study of LLM Adaptation Choices for Bitcoin Price Forecasting"*, arXiv preprint `arXiv:2609.05235v1 [cs.LG, cs.AI]`, submitted September 4, 2026.
- **Canonical Identifier / Stable URL:** https://arxiv.org/abs/2609.05235
- **Canonical DOI:** [10.48550/arXiv.2609.05235](https://doi.org/10.48550/arXiv.2609.05235)
- **Full-Text HTML Source:** https://arxiv.org/html/2609.05235v1
- **Full-Text PDF Source:** https://arxiv.org/pdf/2609.05235v1
- **Source Verification:** The complete HTML publication text and data tables were directly retrieved and audited. All experimental setups, numerical results, and ablation metrics in this record trace directly to Sections 3, 4, 5 and Tables 1–8 of `arXiv:2609.05235v1`.
- **Repository Deduplication Audit:** Pre-write search across all records in `alpha-strategy-research` confirmed zero existing records citing `arXiv:2609.05235`, Maryam Fakhari, Mehran Safayani, or the PRICE framework. Adjacent LLM/foundation model records (`exaone-finance-attention-free-causal-conv-group-pooling-2026-09-16.md`, `alphacrafter-harness-multi-agent-cross-sectional-equity-alpha-2026-09-03.md`, `raml-regime-aware-multimodal-bitcoin-sentiment-fusion-2026-09-04.md`) study different architectures (attention-free SSM/Conv foundation models, multi-agent factor mining harnesses, multimodal sentiment fusion); none systematically isolate the interaction of integer tokenization, one-step LoRA supervision, recursive autoregression, and CTF prompt framing on cryptocurrency price forecasting.

## Economic mechanism

### Source-reported

Cryptocurrency markets feature extreme volatility, structural regime shifts, and non-stationary dynamics that frequently degrade classical linear time-series predictors (e.g., AR/ARIMA) and specialized deep learning architectures. Large Language Models (LLMs) possess vast internal representations and sequential pattern-processing capabilities acquired from broad pretraining, but their direct deployment for numerical time series is hindered by token fragmentation of decimal values, stochastic generation, instruction ambiguity, and the mismatch between continuous price distributions and discrete token vocabularies.

The authors propose **PRICE**, which systematically aligns a 4-bit quantized open-weights LLM (`LLaMA-3 8B-Instruct`) to financial time series through five complementary engineering components:
1. **P (Parameter-Efficient Fine-Tuning):** Supervised adaptation using Low-Rank Adaptation (LoRA) on selected linear layers with a one-step-ahead prediction objective (`pred_len=1`), avoiding expensive full-parameter fine-tuning.
2. **R (Recursive Multi-Step Inference):** Generating multi-step forecasts (`pred_len=8`) via autoregressive recursion (predicting $t+1$, appending it to the input window, and dropping the oldest bar) rather than direct multi-step output, which preserves structural output validity.
3. **I (Integer-Rounded Numerical Representation):** Rounding raw price floats to the nearest integer, which eliminates long decimal token splits while preserving global price scale and relative magnitude.
4. **C (Context-Task-Format Prompting):** Structuring prompts into explicit Context (asset, frequency, data type), Task (analytical forecasting directive), and Format (strict numeric output constraint) components, eliminating verbose natural language responses.
5. **E (Exact Zero-Temperature Decoding):** Enforcing deterministic decoding ($T=0.0$), eliminating stochastic sampling drift during multi-step recursive rollouts.

### Research interpretation

At the financial economics and market microstructure level, an LLM fine-tuned on integer-tokenized price sequences acts as a non-linear autoregressive filter that extracts temporal momentum, mean-reversion tendencies, and local support/resistance geometry from historical price trajectories without requiring explicit technical indicator transformations.

The key falsifiable hypothesis is that:
1. Integer rounding acts as an adaptive denoising filter that reduces tokenization entropy and aligns financial numbers with the LLM tokenizer's high-frequency vocabulary.
2. One-step supervised LoRA fine-tuning conditions the model's self-attention layers to prioritize short-term price momentum while recursive generation preserves output structural integrity over direct multi-step sequence generation.
3. However, because the primary paper evaluates forecasting accuracy (MAE, MSE, MAPE, SMAPE) rather than economic net trading profit, any excess predictive accuracy over baseline models constitutes an alpha candidate only if the directional forecast sign ($E[r_{t+h}] > 0$) reliably overcomes exchange taker fees, slippage, and spread.

## Signal

The primary paper specifies the exact forecasting pipeline. Because the paper defines an econometric forecasting model rather than an operational trade-execution strategy, the operational trade triggers below are categorized into source-reported model components and research-proposed execution rules.

### Source-Reported Forecasting Pipeline

- **Target Instrument:** BTC/USDT hourly closing price (`source-reported`).
- **Observation History (Lookback Window):** Exactly $seq\_len = 96$ hourly bars (4 days of continuous hourly close prices), sampled with stride 1 (`source-reported`).
- **Data Transformation / Tokenization:** Every hourly close price $P_t$ is rounded to the nearest integer: $P_t^{\text{round}} = \text{round}(P_t)$ (`source-reported`). Example sequence: `69340, 69570, 69695, 69519, 69543, 69505, ..., 64304, 64438` (`source-reported`).
- **Prompt Structure (CTF - Context, Task, Format):**
  ```text
  Using the following hourly Bitcoin closing prices, predict the next closing price based on comprehensive technical analysis.
  Return only one predicted number -- no explanation, no text.
  -- input series --
  <integer-rounded price sequence separated by commas>
  ```
  (`source-reported`, Section 5.1.3 Figure 8).
- **Inference Mechanism:** Autoregressive recursive generation. The model generates one-step forecast $\hat{y}_1$. The input context is updated to $[x_2, x_3, \dots, x_{96}, \hat{y}_1]$ and the model predicts $\hat{y}_2$. This is repeated for $pred\_len = 8$ steps (`source-reported`, Section 3.2).
- **Decoding Configuration:** Deterministic greedy decoding with temperature $T = 0.0$ (`source-reported`, Section 3.5).
- **Model Backbone & Adaptation:** `unsloth/llama-3-8b-Instruct-bnb-4bit` (4-bit quantized), adapted via LoRA (`lora_target` on selected linear layers, `learning_rate = 5e-5`, `lr_scheduler = cosine`, `warmup_ratio = 0.1`, `epochs = 2`, `effective_batch_size = 4`, `lora_alpha / rank ratio (LoRA++ lambda)` = 16.0, `training_precision = FP16`) (`source-reported`, Section 4.2 Table 3).

### Research-Proposed Directional Trading Rules

To translate the 8-hour price forecast vector $[\hat{P}_{t+1}, \dots, \hat{P}_{t+8}]$ into an operational strategy, the following execution rules are `research-proposed`:
- **Signal Formation Timestamp:** Formed immediately at the close of hourly bar $t$ ($T_{\text{close}}$, e.g., XX:00:00 UTC) (`research-proposed`).
- **Expected Return Metric:** Compute cumulative predicted return over the 8-hour horizon:
  $$\hat{R}_{t, 8} = \frac{\hat{P}_{t+8} - P_t}{P_t}$$
  (`research-proposed`).
- **Long Entry Trigger:** Enter long if $\hat{R}_{t, 8} > +\theta_{\text{entry}}$, where $\theta_{\text{entry}}$ is a positive threshold calibrated to exceed round-trip taker fees and expected slippage (e.g., $\theta_{\text{entry}} = +0.0035$ or 35 bps) (`research-proposed`).
- **Short Entry Trigger:** Enter short if $\hat{R}_{t, 8} < -\theta_{\text{entry}}$ (e.g., $\theta_{\text{entry}} = -0.0035$ or -35 bps) for perpetual futures (`research-proposed`).
- **Neutral / Filter Zone:** If $|\hat{R}_{t, 8}| \le \theta_{\text{entry}}$, hold flat (cash or zero perpetual delta) (`research-proposed`).
- **Exit Trigger:** Primary exit occurs at the expiration of the 8-hour horizon ($t+8$) (`research-proposed`). Position may exit early if predicted return direction flips sign on the next hourly re-computation (`research-proposed`).
- **Position Sizing:** Fixed fraction of equity or volatility-scaled sizing (e.g., 10% annual volatility target) with a maximum leverage cap of $1.0\times$ spot or $2.0\times$ perpetual (`research-proposed`).

## Required data

- **Asset / Instrument:** BTC/USDT spot or perpetual contract (`source-reported` uses Binance BTC/USDT).
- **Venue:** Binance (collected via CCXT library in primary paper; `source-reported`).
- **Market Type:** Spot market was used for empirical training; perpetual futures applicable for shorting (`research-proposed`).
- **Granularity / Timeframe:** Hourly OHLCV aggregated from 1-minute trades (`source-reported`). The primary model requires only the `Close` series; High, Low, Volume, and Open are collected but discarded by the univariate forecasting prompt (`source-reported`, Section 4.1).
- **Historical Sample Period:**
  - Full archive: 2018 to 2024 collected (`source-reported`).
  - Active experiment window: March 2023 to December 2024 (`source-reported`, Section 4.1 Table 2).
  - Training split (80%): 2023-03-06 01:00 UTC to 2024-08-01 16:00 UTC (`source-reported`).
  - Validation split (10%): 2024-08-01 16:00 UTC to 2024-10-05 00:00 UTC (`source-reported`).
  - Test split (10%): 2024-10-05 00:00 UTC to 2024-12-08 08:00 UTC (`source-reported`).
- **Point-in-Time Hygiene:** Strict chronological partition with 80/10/10 split to prevent lookahead bias or future leakage (`source-reported`).
- **Missing Data Handling:** Timestamp normalization, duplicate removal, and missing value interpolation (`source-reported`, Section 4.1).

## Execution assumptions

- **Inference Latency Budget:** Autoregressive 8-step generation with a 4-bit LLaMA-3 8B model on a single GPU requires approximately 200–500 ms per forecast. The trade must be scheduled for execution at $t+1$ second following candle close (`research-proposed`).
- **Execution Order Type:** Limit order at the prevailing mid-price or market/taker order with fee modeling (`research-proposed`).
- **Fee Model:** Spot taker fee 0.05% to 0.10% (5–10 bps) per side, or perpetual maker/taker fee 0.02%/0.05% (`research-proposed`).
- **Slippage & Spread:** Assumed 1–2 bps spread and 1–2 bps slippage on Binance BTC/USDT top-of-book liquidity (`research-proposed`).
- **Funding Rate Impact:** For perpetual futures implementation, 8-hour funding intervals (00:00, 08:00, 16:00 UTC) must be tracked and subtracted from net yield (`research-proposed`).
- **Source Omissions:** The primary paper does not model execution latency, trading fees, borrow costs, market impact, or fill mechanics; all execution parameters above are `research-proposed`.

## Evidence

### Source-reported

All empirical figures below are directly extracted from Fakhari & Safayani (arXiv:2609.05235v1, Tables 4–8). Performance metrics include Mean Absolute Error (MAE), Mean Squared Error (MSE), Mean Absolute Percentage Error (MAPE, %), Symmetric MAPE (SMAPE, %), Normalized Root Mean Squared Error (NRMSE), and Valid Number of Predictions (VNP out of 1,441 total test instances). Scale-dependent metrics (MAE, MSE) in the cross-model benchmark are standardized using training set statistics:

#### 1. Ablation: Input Representation (Zero-Shot, Minimal Prompt, Validation Set; Table 4)
- **Rounded Integer:** MAPE = 3.01%, SMAPE = 3.05%, NRMSE = 0.05, VNP = 1,441 (lowest errors across all representations).
- **Raw Floats:** MAPE = 4.23%, SMAPE = 5.42%, NRMSE = 0.12, VNP = 1,441.
- **Standard Normalization:** MAPE = 9.43%, SMAPE = 9.39%, NRMSE = 0.16, VNP = 1,441.
- **Instance Normalization:** MAPE = 548.36%, SMAPE = 132.19%, NRMSE = 1.41, VNP = 1,441 (severe performance collapse).

#### 2. Ablation: Paradigm & Strategy (Validation Set; Table 5)
- **Fine-tuned + Multi-Step (Autoregressive):** MAE = 445.60, MSE = 423,562.43, VNP = 1,441 (optimal configuration).
- **Fine-tuned + Single-Step (Direct 8-step):** MAE = 534.85, MSE = 3,263,720.91, VNP = 1,440.
- **Zero-Shot + Multi-Step:** MAE = 1,779.88, MSE = 9,264,283.10, VNP = 1,441.
- **Zero-Shot + Single-Step:** MAE = 2,063.62, MSE = 7,405,313.89, VNP = 1,182 (259 invalid/malformed outputs).
- *Observation:* Fine-tuning reduces MAE by ~75% compared to zero-shot inference.

#### 3. Ablation: Prompt Engineering Strategy (Validation Set; Table 6)
- **Fine-Tuned LLaMA + CTF (Context-Task-Format):** MAE = 432.83, MSE = 402,655.83, VNP = 1,441 (strongest overall).
- **Fine-Tuned LLaMA + iCoT (Implicit CoT):** MAE = 436.68, MSE = 412,852.85, VNP = 1,441.
- **Fine-Tuned LLaMA + Basic Prompt:** MAE = 445.60, MSE = 423,562.43, VNP = 1,441.
- **Zero-Shot GPT-mini + CTF:** MAE = 519.12, MSE = 562,296.72, VNP = 1,441.
- **Zero-Shot GPT-mini + CoT:** MAE = 537.81, MSE = 3,425,467.31, VNP = 1,441.
- **Zero-Shot GPT-nano + CoT:** MAE = 958.17, MSE = 2,243,561.01, VNP = 1,434.
- **Zero-Shot LLaMA + Few-Shot:** MAE = 3,296.07, MSE = 1.72×10⁷, VNP = 1,441 (anchoring distortion).
- **Zero-Shot LLaMA + CoT:** MAE = 13,559.24, MSE = 7.06×10⁸, VNP = 1,403.

#### 4. Ablation: Decoding Temperature (Fine-Tuned Multi-Step CTF, Validation Set; Table 7)
- $T = 0.0$: MAE = 415.89, MSE = 385,195.52, VNP = 1,441 (lowest error).
- $T = 0.2$: MAE = 417.32, MSE = 386,571.30, VNP = 1,441.
- $T = 0.6$: MAE = 422.83, MSE = 391,328.30, VNP = 1,441.
- $T = 0.8$: MAE = 426.77, MSE = 397,966.41, VNP = 1,441.
- $T = 0.95$: MAE = 432.48, MSE = 404,533.49, VNP = 1,441.
- $T = 1.0$: MAE = 434.25, MSE = 405,248.15, VNP = 1,441.
- $T = 1.9$: MAE = 611.14, MSE = 743,941.20, VNP = 1,441.
- *Observation:* Near-monotonic error reduction as temperature approaches zero; $T=0.0$ improves MAE by 3.8% over the default $T=0.95$.

#### 5. Cross-Model Benchmark Comparison (Multi-Step $pred\_len=8$; Table 8)
- **Validation Set Results:**
  - **PRICE (Ours):** MAE = **0.02**, MSE = **0.0014**, MAPE = **2.19%**, SMAPE = **2.19%**, NRMSE = **0.03** (best across all metrics).
  - PatchTST: MAE = 0.03, MSE = 0.0022, MAPE = 2.23%, SMAPE = 2.23%, NRMSE = 0.03.
  - Chronos: MAE = 0.03, MSE = 0.0017, MAPE = 2.52%, SMAPE = 2.52%, NRMSE = 0.03.
  - TimesNet: MAE = 0.04, MSE = 0.0032, MAPE = 2.79%, SMAPE = 2.83%, NRMSE = 0.04.
  - Pyraformer: MAE = 0.04, MSE = 0.0030, MAPE = 2.77%, SMAPE = 2.74%, NRMSE = 0.04.
  - Transformer: MAE = 0.05, MSE = 0.0045, MAPE = 3.57%, SMAPE = 3.51%, NRMSE = 0.04.
  - Autoformer: MAE = 0.09, MSE = 0.0100, MAPE = 6.08%, SMAPE = 6.08%, NRMSE = 0.08.
  - DeepSeek: MAE = 0.10, MSE = 0.0189, MAPE = 9.71%, SMAPE = 9.39%, NRMSE = 0.13.
  - Lag-Llama: MAE = 0.11, MSE = 0.0200, MAPE = 9.89%, SMAPE = 9.76%, NRMSE = 0.12.
  - Crossformer: MAE = 0.12, MSE = 0.0200, MAPE = 8.57%, SMAPE = 8.07%, NRMSE = 0.10.

- **Test Set Results (Held-Out 2024-10-05 to 2024-12-08):**
  - **PRICE (Ours):** MAE = **0.03**, MSE = **0.0029**, MAPE = **1.53%**, SMAPE = **1.53%**, NRMSE = **0.02** (best across all metrics).
  - PatchTST: MAE = 0.04, MSE = 0.0035, MAPE = 1.78%, SMAPE = 1.79%, NRMSE = 0.03.
  - Chronos: MAE = 0.04, MSE = 0.0040, MAPE = 1.77%, SMAPE = 1.78%, NRMSE = 0.03.
  - TimesNet: MAE = 0.04, MSE = 0.0038, MAPE = 1.82%, SMAPE = 1.83%, NRMSE = 0.03.
  - Autoformer: MAE = 0.10, MSE = 0.0178, MAPE = 4.78%, SMAPE = 4.85%, NRMSE = 0.06.
  - DeepSeek: MAE = 0.13, MSE = 0.0344, MAPE = 5.77%, SMAPE = 5.97%, NRMSE = 0.08.
  - Lag-Llama: MAE = 0.16, MSE = 0.0500, MAPE = 7.09%, SMAPE = 7.38%, NRMSE = 0.09.
  - Transformer: MAE = 0.29, MSE = 0.1700, MAPE = 9.97%, SMAPE = 10.90%, NRMSE = 0.18.
  - Pyraformer: MAE = 0.35, MSE = 0.2300, MAPE = 11.71%, SMAPE = 12.99%, NRMSE = 0.21.
  - Crossformer: MAE = 0.65, MSE = 0.7800, MAPE = 22.74%, SMAPE = 27.60%, NRMSE = 0.38.

### Independently reproduced

Not independently reproduced. All figures and performance metrics represent third-party reported findings from Fakhari & Safayani (arXiv:2609.05235v1).

### Negative evidence

1. **Instance Normalization Failure:** Instance normalization completely destabilized LLM price forecasting (validation MAPE 548.36%, SMAPE 132.19%, Table 4), demonstrating that standard deep-learning normalization primitives fail when tokenized as text.
2. **Zero-Shot Few-Shot Anchoring:** Few-shot prompting produced severe forecasting degradation (validation MAE 3,296.07 vs. zero-shot minimal prompt MAE 1,779.88, Table 6), as historical price demonstrations anchored the model to stale price regimes.
3. **Reasoning Distortion (CoT):** Unconstrained zero-shot Chain-of-Thought prompting degraded performance (LLaMA CoT MAE 13,559.24, Table 6) and increased output formatting failures (VNP fell to 1,403).
4. **Economic Viability Gap:** The paper does not report directional accuracy (hit rate / sign accuracy), Sharpe ratio, Sortino ratio, max drawdown, or transaction-cost profitability. A lower SMAPE (1.53% vs 1.79%) does not guarantee a profitable trading strategy after bid-ask spread and taker fees.

## Falsification plan

To falsify the hypothesis that PRICE provides actionable directional alpha in cryptocurrency markets, execute the following pre-declared operational tests:

1. **Directional Sign Test:** Measure 8-hour directional hit rate $\text{sign}(\hat{P}_{t+8} - P_t) == \text{sign}(P_{t+8} - P_t)$. Reject the hypothesis if directional accuracy is $\le 51.5\%$ ($p > 0.05$ against binomial null) over an out-of-sample period of at least 6 months (`research-defined falsification threshold`).
2. **Transaction-Cost Net Profitability Gate:** Backtest the directional rule with 5 bps taker fee and 2 bps slippage on Binance BTC/USDT. Reject the strategy if annualized net Sharpe ratio is $< 1.0$ or net profit factor is $< 1.15$ (`research-defined falsification threshold`).
3. **Autoregressive Lead-Lag Placebo Test:** Shuffle input sequence order or substitute random walk price paths. If the model produces similar forecast errors or "apparent" edges on shuffled data, reject the model as fitting tokenizer frequency bias rather than causal temporal dependence (`research-defined falsification threshold`).
4. **Regime Stress Test:** Evaluate performance across distinct macro regimes (bull expansion, bear drawdown, low-volatility consolidation). Reject if test-set drawdown exceeds 25% or if directional edge collapses during high-volatility liquidation cascades (`research-defined falsification threshold`).
5. **Alternative Crypto Universes:** Test the identical PRICE architecture on ETH/USDT and SOL/USDT without asset-specific prompt retuning. If predictive edge collapses entirely, classify the Bitcoin findings as asset-specific sample overfitting (`research-defined falsification threshold`).

## Crypto portability

`direct`

The primary paper was explicitly developed and evaluated on cryptocurrency data (Binance BTC/USDT hourly market from 2023 to 2024).

Crypto-specific operational considerations include:
- **24/7 Continuous Trading:** Unlike traditional equities with session opens/closes, cryptocurrency markets trade continuously; the 96-hour input context advances seamlessly across weekends.
- **Perpetual Funding Drift:** When executing long/short trades on USDT perpetual futures, 8-hour funding rates must be factored into the holding cost.
- **Volatility Spikes & Token Length Drift:** If Bitcoin price moves from 5-digit to 6-digit territory (e.g., $99,000 to $105,000), integer token length changes from 5 digits to 6 digits, which could alter tokenizer chunking behavior.
- **Venue Fragmentation:** Binance spot and perp prices may diverge from Coinbase or Bybit during sudden liquidity drains; model inputs must strictly adhere to the target execution venue's tape.

## Limitations

- `no-economic-backtest`: The primary source is purely an econometric forecasting paper; it contains zero trading backtests, Sharpe ratios, drawdown analyses, or fee stress tests.
- `univariate-only`: The model consumes only hourly closing prices, ignoring volume, order-flow imbalance, funding rates, and open interest.
- `hardware-latency-dependency`: Fine-tuned 8B LLM requires GPU inference infrastructure (minimum 11 GB VRAM for 4-bit inference) and introduces 200–500 ms computational latency per bar.
- `underspecified-trade-rules`: Entry thresholds, position sizing, risk management, and stop losses are completely absent from the source paper and must be supplied via `research-proposed` definitions.
- `not independently reproduced`.
- `unproven`: Commercial viability and net profitability after exchange fees remain unproven.

## Implementation status

No implementation in our research stack has been completed. No PyBroker, Nautilus, paper, testnet, or live verification is implied.

## Adoption boundary

Research material only. Presence in this repository does not mean profitable, validated alpha, approved for implementation, or approved for paper, testnet, or live trading.

## Related Wiki records

- `[[quant/exaone-finance-attention-free-causal-conv-group-pooling-2026-09-16]]` — EXAONE Finance: Attention-free foundational architecture for multi-asset financial time-series forecasting.
- `[[quant/alphacrafter-harness-multi-agent-cross-sectional-equity-alpha-2026-09-03]]` — AlphaCrafter: Multi-agent LLM framework for alpha discovery and execution.
- `[[quant/raml-regime-aware-multimodal-bitcoin-sentiment-fusion-2026-09-04]]` — RAML: Regime-aware multimodal Bitcoin forecasting combining sentiment and price.
- `[[quant/trading-r1-curricular-reinforcement-learning-llm-reasoning-2026-09-05]]` — Trading-R1: Reinforcement learning reasoning models for trading decisions.
- `[[quant/hybrid-lstm-xgboost-multi-horizon-composite-scoring-2026-09-16]]` — Hybrid multi-horizon forecasting with classical machine learning models.

## Sources

1. Maryam Fakhari and Mehran Safayani, *"PRICE: A Systematic Study of LLM Adaptation Choices for Bitcoin Price Forecasting"*, arXiv preprint `arXiv:2609.05235v1 [cs.LG, cs.AI]`, submitted September 4, 2026.
   - Stable URL: https://arxiv.org/abs/2609.05235
   - HTML version: https://arxiv.org/html/2609.05235v1
   - PDF version: https://arxiv.org/pdf/2609.05235v1
   - DOI: [10.48550/arXiv.2609.05235](https://doi.org/10.48550/arXiv.2609.05235)
2. Hugging Face repository: `unsloth/llama-3-8b-Instruct-bnb-4bit` (4-bit quantized base model cited in Section 4.2).
3. LLaMA-Factory repository: `https://github.com/hiyouga/LLaMA-Factory` (fine-tuning framework cited in Section 4.2).
4. Time-Series-Library (TSLib) benchmark: `https://github.com/thuml/Time-Series-Library` (baseline evaluation repository cited in Section 4.2).
