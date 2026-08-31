---
schema: strategy-research-record-v1
title: Fused Encoder Networks for Cross-Sectional Momentum
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cross-sectional
  - momentum
  - machine-learning
status: research-only
confidence: high
source_as_of: 2022-08-21
sources:
  - "https://arxiv.org/abs/2208.09968 (DOI: 10.48550/arXiv.2208.09968)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Fused Encoder Networks for Cross-Sectional Momentum

## Provenance

- **Source:** "Transfer Ranking in Finance: Applications to Cross-Sectional Momentum with Data Scarcity" by Daniel Poh, Stephen Roberts, Stefan Zohren
- **Venue:** arXiv:2208.09968, https://arxiv.org/abs/2208.09968
- **Target:** Top 10 cryptocurrencies by market capitalization

## Economic mechanism
### Source-reported
The paper identifies that standard neural architectures for cross-sectional momentum fail in data-scarce environments like cryptocurrencies, producing over-fitted models. They introduce Fused Encoder Networks, a hybrid parameter-sharing transfer ranking model. It uses an encoder-attention module pre-trained on a data-rich source dataset, fused with a similar module trained on the scarce target dataset. The self-attention mechanism captures interactions among instruments at inference time, ranking the cross-section of returns.

### Research interpretation
The underlying alpha mechanism is cross-sectional momentum (relative winner/loser persistence) in cryptocurrencies, where top-performing assets tend to continue outperforming the bottom assets in the near term. The innovation is purely in the signal generation method: transferring learned market structure from mature, data-rich asset classes to the data-poor crypto cross-section to mitigate overfitting, and using self-attention to explicitly rank assets relative to each other rather than scoring them independently.

## Signal

- **Source setup:** Daily closing prices are downsampled to weekly observations (Wednesday). The target crypto model uses raw and volatility-normalized cryptocurrency returns over the previous 1, 2, and 3 weeks.
- **Signal formation:** The Fused Encoder Network produces a cross-sectional ranking score for the fixed cryptocurrency universe using a target encoder in parallel with a pre-trained source encoder.
- **Portfolio construction:** Rebalance weekly; hold an equally weighted long portfolio in the top 2 ranked cryptocurrencies and an equally weighted short portfolio in the bottom 2.
- **Exit / holding:** Positions are replaced at the next weekly rebalance according to the new ranking.
- **Model-training detail:** The source encoder is trained on the paper's FX source dataset before its learned representation is fused with the target crypto encoder.

## Required data

- **Target universe:** The paper fixes 10 cryptocurrencies selected by market capitalization at end-Dec-2019 with sufficient history: BTC, ETH, DOGE, DGB, LTC, XLM, XRP, XMR, XEM, DASH.
- **Target fields/frequency:** Daily closing prices from CoinMarketCap, downsampled to weekly observations; raw and volatility-normalized 1-, 2-, and 3-week returns are target predictors.
- **Target sample:** 2016-01-01 through 2021-12-31 in the reported study.
- **Source dataset:** BIS daily FX data for 30 currency pairs spanning May-2000 to Dec-2021, downsampled weekly, used to train the upstream/source encoder.

## Execution assumptions

- **Rebalance cadence:** Weekly, matching the paper's portfolio construction.
- **Signal-to-fill timing:** The paper defines weekly observations/rebalancing but the exact within-rebalance order timestamp and order type are underspecified; implementation must choose and test a causal convention.
- **Transaction costs:** The paper explicitly studies turnover/cost sensitivity. Its crypto cost assumption is 26 bps per trade, and it reports positive FEN Sharpe persisting to roughly 29 bps. These are source-reported study assumptions, not our validated execution costs.

## Evidence
### Source-reported
The paper reports a three-fold boost in the Sharpe ratio over classical momentum and a ~50% improvement over the best benchmark model without transaction costs. It claims the model continues to outperform baselines even after accounting for high transaction costs in crypto.

### Independently reproduced
Not independently reproduced.

### Negative evidence
None identified in the reviewed sources; absence is not evidence of no negative result.

## Falsification plan

- First reproduce the paper's fixed 10-crypto universe, weekly Wednesday sampling, 1/2/3-week return predictors, top-2/bottom-2 equal-weight portfolio, FX-source pretraining, and reported transaction-cost convention.
- Compare FEN against classical cross-sectional momentum and the paper's non-transfer benchmark models on a strictly held-out period.
- Then test a later point-in-time crypto sample without changing the source-defined signal construction; failure to retain incremental performance over the non-transfer benchmarks falsifies the transfer-learning contribution.

## Crypto portability

direct

The strategy is explicitly designed for and tested on the cryptocurrency market as its primary use case for data scarcity.

## Limitations

- The reported source dataset is fixed FX data; whether that upstream domain remains useful for later crypto regimes is unproven.
- not independently reproduced.

## Implementation status

not-implemented

## Adoption boundary

research-only

## Related Wiki records


## Sources
- Poh, Roberts, Zohren, "Transfer Ranking in Finance: Applications to Cross-Sectional Momentum with Data Scarcity", https://arxiv.org/abs/2208.09968
