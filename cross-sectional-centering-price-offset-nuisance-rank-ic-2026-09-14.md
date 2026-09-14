---
schema: strategy-research-record-v1
title: "Centering Drives Cross-Sectional Rank IC: Price-Offset Nuisance Removal in Intraday Bar Models"
created: 2026-09-14
updated: 2026-09-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - china-ashare
  - cross-sectional
  - feature-engineering
  - normalization
  - ranking
  - intraday
  - representation-learning
status: research-only
confidence: medium
source_as_of: 2026-09-07
sources:
  - "Mingju Chen, Qianhui Liu, Yui Lo, and Yuanhang Liu, 'Centering Drives Normalization Gains: Price-Offset Nuisances in Cross-Sectional Return Prediction', arXiv:2609.07122v1 [cs.CE], September 7, 2026. https://arxiv.org/abs/2609.07122"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Centering Drives Cross-Sectional Rank IC: Price-Offset Nuisance Removal in Intraday Bar Models

## Provenance

- **Source**: arXiv:2609.07122v1 [cs.CE]
- **Authors**: Mingju Chen, Qianhui Liu, Yui Lo, Yuanhang Liu
- **Version**: v1, submitted September 7, 2026
- **DOI**: https://doi.org/10.48550/arXiv.2609.07122
- **URL**: https://arxiv.org/abs/2609.07122
- **Full text HTML**: https://arxiv.org/html/2609.07122v1
- **Universe**: CSI 300 constituents
- **Timeframe**: five-minute intraday bars, point-in-time panel
- **Task**: cross-sectional return ranking (not single-asset price forecasting)

### Repository Deduplication Audit

Repository-wide search on 2026-09-14 found zero prior records citing `arXiv:2609.07122`, Chen/Liu/Lo/Liu, or the price-offset / centering-vs-scale-only isolation design. Adjacent records:

- `cryptol-scale-balanced-multivariate-ohlc-physics-loss-2026-09-12.md` — crypto multivariate OHLC forecasting with Two-Phase RevIN and physics-constrained candle loss; single/multi-asset **forecasting MSE**, not cross-sectional **rank IC**; does not isolate centering vs scale-only as the causal channel
- `china-ashare-mask-first-upstream-contamination-adjusted-mse-2026-09-04.md` — leakage/mask-first methodology on A-share ML, different mechanism
- `china-ashare-xgboost-treeshap-behavioral-factor-decomposition-2026-09-04.md` — tree-SHAP factor decomposition, different signal family
- `strata-selective-state-space-intraday-raw-bars-cross-sectional-ranking-2026-09-02.md` — cross-sectional ranking on raw bars, but state-space architecture rather than normalization ablation

The present record's incremental value is a **parameter-free ladder** that separates identity / scale-only / centering / last-value referencing / differencing / standardization, and shows that **centering (price-offset removal), not amplitude scaling**, is the reliable IC-gaining channel.

## Economic mechanism

### Source-reported

Cross-sectional return prediction from raw intraday bars is sensitive to each instrument's price level. Under a return-ranking hypothesis, absolute price is an **additive nuisance**: ranking models that see uncentered prices can learn price-level proxies that do not transfer to return ranks. The paper tests whether removing this offset (centering), rather than rescaling amplitudes or changing the encoder architecture, explains IC gains on a point-in-time CSI 300 five-minute panel.

Eight parameter-matched encoders are evaluated with and without RevIN normalization. A parameter-free ladder then isolates: identity, scale-only, centering, last-value referencing, differencing, and standardization across all fields and restricted channels.

### Research interpretation

The structural claim is that in cross-sectional ranking, **levels are not information; demeaned levels (or equivalent offset removal) are**. Scale-only normalization does not help because it leaves the additive price offset intact. Centering removes it. Price-only standardization retains 93–101% of the all-field gain, indicating the effect lives primarily in the transformed price channel.

This is a representation / feature-construction insight, not a complete trading strategy. Research-proposed use in crypto: any multi-asset ranker spanning instruments with heterogeneous price scales (BTC vs mid/low-price alts) should demean or otherwise remove price-level offset before ranking, and should not assume Vol/price rescaling alone is sufficient.

## Signal

### Formation timestamp

Point-in-time CSI 300 five-minute panel (`source-reported`). Exact tradeable timestamp alignment (bar close → signal available for next bar) is not fully specified in the abstract; treat availability lag as requiring paper-level confirmation before any implementation claim.

### Lookback

Encoder context window is architecture-dependent. The **normalization ladder is parameter-free** and applied on the input window used by each encoder (`source-reported` design).

### Entry (source-reported measurement)

Not a standalone entry rule. The paper measures **raw rank IC** of model scores against forward returns, with Holm correction across eight paired encoder comparisons, after style residualization, and after additionally residualizing on short-term reversal.

### Entry (research-proposed operationalization)

`research-proposed` for crypto cross-sectional rankers:

1. At each rebalance timestamp, for each eligible asset and each input feature channel, compute the context-window mean and subtract it (centering). Optionally apply price-channel standardization after centering.
2. Feed the centered (or price-only standardized) series into the same encoder used in the uncentered baseline.
3. Rank assets by predicted score; form a long-short or long-top / short-bottom portfolio at a pre-specified quantile.
4. Compare rank IC and net performance of centered vs identity vs scale-only variants under identical encoders and dates.

This operationalization is research-proposed. The source does not provide a crypto trading entry/exit rule.

### Exit

Not specified by the source (ranking/IC study).

### Holding period

Horizon tied to the CSI 300 five-minute forward return used as the ranking target (`source-reported`); exact forward window should be read from the paper body before any hold-period claim.

### Parameters

- Universe: CSI 300 (`source-reported`)
- Bar: five-minute (`source-reported`)
- Encoders: eight parameter-matched architectures, with/without RevIN (`source-reported`)
- Ladder transforms: identity, scale-only, centering, last-value referencing, differencing, standardization (`source-reported`)
- Channels: all fields vs restricted (price-only) (`source-reported`)
- Inference: Holm correction; style residualization; short-term-reversal residualization (`source-reported`)

## Required data

- **Instrument**: CSI 300 constituent equities (source); crypto portability would require a liquid multi-asset crypto universe with heterogeneous price scales
- **Universe**: CSI 300 (`source-reported`); crypto adaptation `research-proposed` (e.g., top-N liquid perps/spot by ADV)
- **Venue**: Chinese A-share cash market (`source-reported`)
- **Timeframe**: five-minute bars (`source-reported`)
- **Fields**: raw intraday bar channels used by the encoders; price channel is the primary offset channel of interest
- **Point-in-time**: stated as point-in-time CSI 300 five-minute panel (`source-reported`)
- **Timestamp / missing-data**: not detailed in the abstract; implementation would need paper-level specification
- **Funding/fee/spread**: IC study does not claim net-of-cost strategy returns

## Execution assumptions

- **Order type / fill / latency**: not modeled (IC / ranking study)
- **What the source assumes**: ranking quality of encoder scores after controlled normalization ablations
- **What the Scout does not assume**: no claim that CSI 300 IC 0.08–0.09 transfers to crypto after costs

## Evidence

### Source-reported

From Chen et al. (arXiv:2609.07122v1, abstract):

- **Centering** drives the reliable effect; **scale-only** normalization does not help
- All **eight** paired effects are positive and survive **Holm correction** on:
  - raw rank IC
  - IC after style residualization
  - IC after additionally residualizing on short-term reversal
- Among six stronger encoders: normalized IC **0.0830–0.0939**; gains **0.0376–0.0567**
- **Price-only** standardization retains **93–101%** of the all-field gain
- Conclusion: main effect is transformed **price-channel offset removal**, not amplitude scaling or encoder choice

### Independently reproduced

`not independently reproduced`

### Negative evidence

- **Scale-only is a negative result**: amplitude rescaling without centering does not produce reliable gains
- **Encoder choice is not the main driver**: gains survive across eight parameter-matched encoders when centering is applied
- The paper is **not** a net-of-cost trading strategy study; IC ≠ implementable alpha after fees, turnover, and borrow (if shorting)
- Source market is A-share CSI 300; crypto transfer is untested in this paper

## Falsification plan

1. **Crypto cross-section replication (research-proposed)**. On a pre-registered liquid crypto universe (e.g., top 50 by ADV), compare identity vs scale-only vs centering vs price-only standardization under one fixed encoder and dates. **Research-defined falsification threshold**: if centering fails to improve rank IC over identity in two of three yearly cohorts, reject crypto portability of the offset-removal claim.
2. **Price-scale placebo**. Randomly permute price levels across assets while keeping return ranks; if centered and uncentered models become indistinguishable, the mechanism is price-offset specific. If they remain different, another channel is at work.
3. **Style residualization**. Residualize scores on size, beta, short-term reversal, and liquidity; centered gains should persist. If they vanish after reversal residualization only, the effect may be a restatement of reversal, not a new orthogonal signal.
4. **Turnover / cost stress**. Convert top/bottom quantile rankings into portfolios with half-spread + fees. **Research-defined falsification threshold**: if centered models' extra IC does not survive cost adjustment relative to identity, treat as statistical not economic.
5. **Alt-only vs BTC/ETH-only splits**. If centering only helps the long tail of low-price names, report a size/price interaction rather than a universal rule.
6. **Encoder swap**. Repeat with a non-transformer baseline (e.g., linear ranker on the same centered features). If centering still helps, the effect is representation-agnostic (as claimed); if it only helps deep encoders, narrow the claim.

## Crypto portability

**Adapted**

The source is CSI 300 equities, not crypto. Portability rationale:

- Crypto cross-sections routinely mix instruments whose absolute price levels differ by orders of magnitude (BTC vs low-priced alts), making additive price-offset nuisance **more severe**, not less
- 24/7 continuous bars replace session-based five-minute grids; centering remains a parameter-free window operation
- No equity-style shorting/borrow rules apply if the crypto implementation uses linear perps; spot short constraints still matter
- Funding, fees, and taker spreads are crypto-specific cost channels absent from the IC study
- Adjacent crypto normalization work (CryptoL TP-RevIN) targets forecasting distortion and candle geometry, not cross-sectional rank IC — mechanisms are complementary, not duplicates

Crypto portability is **not** authorization to trade.

## Limitations

- **IC study, not strategy**: no portfolio construction, costs, or live evidence in the abstract-level claims
- **A-share only** empirical setting
- **Exact bar-to-trade lag**, forward horizon, and encoder architectures require full-text confirmation before reimplementation
- **Preprint**: arXiv v1; not peer-reviewed at capture time
- **Restricted channels**: price-only retaining 93–101% of gain is strong, but other fields may still matter in other universes
- **Point-in-time panel claimed**, but leakage controls beyond residualizations are not described in the abstract

## Implementation status

`not-implemented`

No implementation in our research stack. No CSI 300 or crypto centering pipeline, no encoder training run, and no NautilusTrader/PyBroker strategy exists for this family.

## Adoption boundary

This record is research material only. Presence in this repository does not mean profitable, validated alpha, or approval for implementation, paper trading, testnet, or live trading.

## Related Wiki records

- [[quant/strategy-research-record-spec-v1]] — canonical schema
- `cryptol-scale-balanced-multivariate-ohlc-physics-loss-2026-09-12.md` — crypto OHLC forecasting normalization (different objective)
- `strata-selective-state-space-intraday-raw-bars-cross-sectional-ranking-2026-09-02.md` — cross-sectional ranking on intraday bars (different architecture focus)
- `china-ashare-mask-first-upstream-contamination-adjusted-mse-2026-09-04.md` — A-share ML methodology, different leakage mechanism
- `crypto-cross-sectional-return-rank-mlp-decay-portfolio-2026-09-03.md` — crypto cross-sectional ML ranking family

## Sources

1. Mingju Chen, Qianhui Liu, Yui Lo, and Yuanhang Liu. "Centering Drives Normalization Gains: Price-Offset Nuisances in Cross-Sectional Return Prediction." arXiv:2609.07122v1 [cs.CE], September 7, 2026. https://arxiv.org/abs/2609.07122
