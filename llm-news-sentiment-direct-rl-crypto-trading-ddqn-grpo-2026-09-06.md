---
schema: strategy-research-record-v1
title: "LLM News-Sentiment Direct RL Trading for Crypto: Feature-Free Sequential Decision with DDQN and GRPO (Lan et al. 2025)"
created: 2026-09-06
updated: 2026-09-06
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - reinforcement-learning
  - large-language-models
  - news-sentiment
  - bitcoin
  - DDQN
  - GRPO
  - LSTM
  - feature-free
  - sequential-decision
status: research-only
confidence: medium
source_as_of: "2025-10-22"
sources:
  - "Qing-Yu Lan, Zhan-He Wang, Jun-Qian Jiang, Yu-Tong Wang, and Yun-Song Piao. 'News-Aware Direct Reinforcement Trading for Financial Markets'. arXiv preprint arXiv:2510.19173v1 [q-fin.CP], submitted October 22, 2025. Stable URL: https://arxiv.org/abs/2510.19173. PDF: https://arxiv.org/pdf/2510.19173."
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# LLM News-Sentiment Direct RL Trading for Crypto: Feature-Free Sequential Decision with DDQN and GRPO (Lan et al. 2025)

## Provenance

- **Source:** Lan, Q.-Y., Wang, Z.-H., Jiang, J.-Q., Wang, Y.-T., & Piao, Y.-S. (2025). *News-Aware Direct Reinforcement Trading for Financial Markets*. arXiv:2510.19173v1 [q-fin.CP].
- **Author affiliation:** School of Physical Sciences, University of Chinese Academy of Sciences, Beijing 100049, China.
- **Submission date:** October 22, 2025.
- **Version:** v1 (initial).
- **Paper type:** Preprint (not peer-reviewed at time of capture).
- **Primary source verified:** Author list, submission date, abstract, and results confirmed from the arXiv landing page and PDF.

## Economic mechanism

### Source-reported

Financial markets are driven not only by price and volume but also by news events, which deliver information shocks and trigger regime changes. Leaving out news makes market condition partially observable and increases non-stationarity. The authors hypothesize that LLM-derived sentiment and risk scores from financial news, when directly combined with raw OHLCV data and processed through sequence-based RL agents, can produce superior trading performance versus market benchmarks without relying on handcrafted technical features or manually designed rules.

### Research interpretation

The hypothesized alpha mechanism is **news-driven information asymmetry capture**: LLMs extract structured sentiment signals from unstructured financial news, and these signals contain predictive content about short-term price movements that raw price/volume alone do not fully capture. The RL agent learns to combine news sentiment with price/volume as a unified time-series state, enabling end-to-end decision making that implicitly adapts to news-driven regime shifts.

Component roles:
- **LLM sentiment extraction:** Gemini-2.5-flash processes Yahoo Finance Bitcoin news, producing sentiment scores (1–5) and risk scores (1–5) per news item. Scores are held constant until the next news item appears.
- **State representation:** 1-minute OHLCV data merged with LLM sentiment/risk scores as a multi-channel time-series input.
- **RL decision agent:** DDQN (off-policy) or GRPO (on-policy variant of PPO) with LSTM or Transformer backbone processes the merged time-series and outputs discrete actions: short, long, or hold.
- **Risk management:** Simple stop-loss/take-profit threshold of 0.1% to simulate practical constraints.

## Signal

### Formation timestamp

- News sentiment scores are assigned by LLM at the time of news processing (batched). Each score persists until the next news item is published.
- Market data is 1-minute OHLCV from Binance.
- The RL agent observes the merged state at each minute and outputs an action.

### Lookback

- Sequence model window size: tuned between 10 and 50 minutes (log scale).
- LSTM hidden dimensions: 32, 64, or 128.
- LSTM layers: 1 or 2; Transformer layers: 1 to 3.
- Transformer attention heads: 2 or 4; feedforward dimension: 32, 64, or 128.

### Long entry

- RL agent selects "long one BTC" action.

### Short entry

- RL agent selects "short" action.

### Exit / risk management

- Stop-loss/take-profit threshold: 0.1% (research-defined operationalization, not specified by source as a tuned parameter).
- No additional exit rules specified.

### Holding period

- Actions are generated at 1-minute frequency. Actual holding period is determined by the RL policy; no explicit maximum holding period is specified.

### Parameters

- All hyperparameters are tuned via Optuna (TPE algorithm) on the validation set, with early stopping if best validation return does not improve for 5 consecutive evaluations.
- Key tuned ranges: learning rate (2e-6 to 1e-3), batch size (32, 128, 512), gradient clipping norm (0.1 to 4.0), discount factor (0.90 to 0.995), exploration rate for DDQN (0.005 to 0.125), epsilon decay rate (0.99995, 0.99999, 0.999999), GAE parameter for PPO (0.9 to 0.99), clip ratio for PPO (0.1 to 0.2).
- All parameters are research-defined (tuned); none are source-calibrated to a specific market regime.

### Fully specified?

Underspecified. The paper provides the full hyperparameter tuning ranges but does not specify the exact final hyperparameter values selected for the best agents. The RL policy itself is learned end-to-end; the signal is the learned policy, not a fixed formula.

## Required data

- **Instrument:** BTC/USDT (single asset).
- **Venue:** Binance Exchange.
- **Market type:** Spot (1-minute OHLCV from Binance data portal).
- **Timeframe:** 1-minute bars.
- **Fields:** Open, High, Low, Close, Volume (OHLCV).
- **News data:** Bitcoin-related news text scraped from Yahoo Finance (via HuggingFace dataset: edaschau/bitcoin news).
- **Sentiment features:** LLM-derived sentiment score (1–5) and risk score (1–5) from Gemini-2.5-flash.
- **Time range:** 2019-12-31 00:00:00 to 2024-01-24 21:48:00.
- **Split:** 70% train / 15% validation / 15% test (chronological).
- **Point-in-time:** News sentiment scores are assigned at processing time and held constant until the next news item; no look-ahead bias in sentiment assignment.
- **Missing data:** Not discussed; sentiment scores are interpolated by holding the last value until the next news item.

## Execution assumptions

- **Action space:** Discrete (short, long one BTC, hold) — binary position.
- **Execution timing:** Agent acts at each 1-minute bar; execution model not specified (presumed next-bar market order).
- **Stop-loss/take-profit:** 0.1% threshold (research-defined).
- **Fees:** Not explicitly modeled in the backtest.
- **Slippage:** Not explicitly modeled.
- **Spread:** Not explicitly modeled.
- **Funding:** Not applicable for spot; funding not discussed.
- **Capacity:** Not discussed; single-asset BTC study.
- **Fill model:** Not specified; presumed perfect fill at bar close.
- **Latency:** Not discussed.

## Evidence

### Source-reported

**Table 1 — Averaged cumulative returns (USDT) over 3,000-minute test periods (256 sampled periods):**

| Algorithm | Network | Top1 | Top10 |
|-----------|---------|------|-------|
| DDQN | MLP | 80.6 | 153 |
| DDQN | LSTM | **329.8** | **338** |
| DDQN | Transformer | 307.1 | 223.8 |
| GRPO | MLP | 203.2 | 151.5 |
| GRPO | LSTM | **447.5** | 289.5 |
| GRPO | Transformer | 227 | 219.4 |
| DDQN | LSTM (no LLM) | 201.9 | 118.1 |
| DDQN | Transformer (no LLM) | 283.8 | 199.3 |
| GRPO | LSTM (no LLM) | 135.4 | 265.9 |
| GRPO | Transformer (no LLM) | 272.1 | 224.9 |

**Table 2 — Full backtest cumulative returns (% change) over entire test period (baseline BTC return: 56%):**

| Algorithm | Network | Top1 | Top10 |
|-----------|---------|------|-------|
| DDQN | MLP | 114.9% | 91% |
| DDQN | LSTM | **124.5%** | **119%** |
| DDQN | Transformer | 112% | 95.8% |
| GRPO | MLP | 59.9% | 83.7% |
| GRPO | LSTM | **124.5%** | 106.8% |
| GRPO | Transformer | 79.1% | 92.2% |
| DDQN | LSTM (no LLM) | 47% | 67.8% |
| DDQN | Transformer (no LLM) | 131.8% | 66.7% |
| GRPO | LSTM (no LLM) | 68.3% | 89% |
| GRPO | Transformer (no LLM) | 54.4% | 69.2% |

Source reports that adding LLM news sentiment to LSTM-based agents consistently raises cumulative returns versus the no-LLM ablation. Sequence-based agents (LSTM, Transformer) consistently outperform MLP-based agents. The best single agent (GRPO:LSTM Top1) achieves 447.5 USDT average return over 3,000-minute periods and 124.5% cumulative return over the full test period, both exceeding the 56% BTC baseline. These results have not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Transformer-based agents show weaker news contribution than LSTM; the authors suggest this is because their Transformer is not tailored for time-series modeling.
- The paper is a proof-of-concept with simplified action space (3 discrete actions), simple risk management (0.1% SL/TP), and no fee/slippage modeling.
- The test period covers only approximately 7 months (July 2023 to February 2024).
- Hyperparameter tuning on validation set introduces potential overfitting risk; the authors acknowledge this is a proof-of-concept.
- The Top1 agent selection is based on validation performance, which may not generalize.
- No Sharpe ratio, maximum drawdown, or win rate is reported; only cumulative return is provided.
- No significance testing or bootstrap confidence intervals are reported.

## Falsification plan

1. **Out-of-sample validation:** Re-run on a completely held-out period (e.g., 2024–2025) with the same pipeline. The source uses a chronological split but the test window is short.
2. **Fee and slippage stress test:** Re-run with 10 bps, 20 bps, and 50 bps round-trip costs to determine if profitability survives transaction costs.
3. **News source sensitivity:** Replace Yahoo Finance news with alternative sources (e.g., CryptoPanic, CoinDesk) to test robustness of LLM sentiment extraction.
4. **LLM model sensitivity:** Replace Gemini-2.5-flash with other LLMs (GPT-4, FinBERT) to test whether sentiment extraction quality matters.
5. **Multi-asset generalization:** Extend to ETH, SOL, and other major crypto assets.
6. **Walk-forward validation:** Use expanding or rolling windows instead of a single train/val/test split.
7. **Ablation on news timing:** Test whether the timing of news arrival (intraday clustering, overnight gaps) affects performance.
8. **Failure threshold:** If the fee-adjusted Sharpe ratio drops below 0.5 on a 12-month OOS period, the hypothesis is materially weakened.

## Crypto portability

Direct — the study is conducted on BTC/USDT spot on Binance. However, the following portability considerations apply:

- The study uses spot market data, not perpetual futures; funding rate dynamics are absent.
- 24/7 crypto market structure means news arrives at all hours; the score-holding mechanism (last score persists until next news) may create stale signals during quiet periods.
- Exchange fragmentation: the study uses only Binance; venue-specific effects are untested.
- Liquidity: the study does not model market impact or partial fills for large orders.
- The action space is extremely simple (long/short/hold with binary sizing); real deployment would need position sizing, leverage, and more granular risk management.
- Yahoo Finance Bitcoin news coverage may differ from crypto-native news feeds in timeliness and relevance.

## Limitations

- **Proof-of-concept only:** The authors explicitly state this is a proof-of-concept with simplified action space, risk management, and evaluation.
- **No transaction costs modeled:** Fees, slippage, and spread are not included; profitability may not survive realistic execution costs.
- **Short test window:** Full backtest covers approximately 7 months (July 2023 – February 2024), which includes a strong BTC bull market (BTC rose from ~$26,000 to ~$50,000).
- **No risk metrics reported:** No Sharpe, Sortino, maximum drawdown, or win rate is provided; only cumulative return.
- **Hyperparameter tuning risk:** Extensive Optuna-based tuning on validation set with many hyperparameter dimensions creates overfitting risk.
- **Single asset:** BTC only; no multi-asset or cross-sectional evidence.
- **No news timeliness modeling:** Sentiment scores are held constant until next news item; no decay or freshness weighting.
- **Not independently reproduced.**
- **Preprint status:** Not peer-reviewed at time of capture.

## Implementation status

Not implemented. No code or implementation artifacts are provided by the authors.

## Adoption boundary

This record represents research material only. It does not mean:
- Profitable
- Validated alpha
- Approved for implementation
- Approved for paper trading
- Approved for testnet
- Approved for live trading

## Related Wiki records

- `[[quant/llm-news-probing-excess-return-sentiment-timing-2026-09-06]]` — Kirtac & Germano (2024): LLM news sentiment for equity return prediction. Different universe (equity vs crypto), different mechanism (sentiment probing vs RL trading), different scope (factor research vs end-to-end trading).
- `[[quant/finsmart-market-aligned-reinforcement-learning-sentiment-alpha-2026-09-02]]` — Iacovides et al. (2026): GRPO-based market-aligned sentiment optimization for cross-sectional equity. Different universe (equity vs crypto), different mechanism (RL optimizes sentiment extraction itself vs LLM-extracted sentiment as RL input).
- `[[quant/crypto-news-peer-overreaction-reversal-4w-2026-09-03]]` — Schwenkler & Zheng (2025): News-driven peer co-movement reversal in crypto. Different mechanism (cross-sectional event-driven reversal vs time-series RL with news sentiment).

## Sources

1. Lan, Q.-Y., Wang, Z.-H., Jiang, J.-Q., Wang, Y.-T., & Piao, Y.-S. (2025). News-Aware Direct Reinforcement Trading for Financial Markets. arXiv:2510.19173v1 [q-fin.CP]. https://arxiv.org/abs/2510.19173. Submitted October 22, 2025.
