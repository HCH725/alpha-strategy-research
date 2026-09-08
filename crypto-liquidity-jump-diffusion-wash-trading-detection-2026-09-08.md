---
schema: strategy-research-record-v1
title: "Liquidity Jump–Diffusion Joint Signal for Crypto Wash Trading Detection and Avoidance"
created: 2026-09-08
updated: 2026-09-08
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - microstructure
  - wash-trading
  - liquidity
  - market-quality
  - contrarian
status: research-only
confidence: medium
source_as_of: 2026-11-30
sources:
  - "https://arxiv.org/abs/2411.05803v4"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Liquidity Jump–Diffusion Joint Signal for Crypto Wash Trading Detection and Avoidance

## Provenance

- Paper: Qi Deng and Zhong-guo Zhou, "Liquidity Jump, Liquidity Diffusion, and Crypto Wash Trading"
- arXiv: `2411.05803v4` (v4, 2024-11-08; latest revision accessed 2026-09-08)
- PDF: https://arxiv.org/pdf/2411.05803v4
- Authors: Qi Deng (College of Artificial Intelligence, Hubei University of Automotive Technology; Cofintelligence Financial Technology Ltd.), Zhong-guo Zhou (Department of Finance, Financial Planning, and Insurance, Nazarian College of Business and Economics, California State University Northridge)
- Publication status: Working paper (arXiv preprint); JEL: C55, D82, G12, G14, G18
- Sample period: Minute-level data, January 2021–May 2024 (approximately 1,577 trading days for crypto, 2,652 for US stocks)
- Universe (crypto): ADA, AVAX, BCH, BTC, ETC, ETH, LTC, SOL, UNI, XRP on Binance
- Universe (benchmark): 15 US large-cap stocks (AAPL, AMZN, ATI, CMA, CRS, EME, GOOG, IBKR, LII, MLI, MSFT, NVDA, TPL, VFC, WSO)
- Dataset and code: https://doi.org/10.5281/zenodo.17830943 (referenced in paper)

## Economic mechanism

### Source-reported

The authors propose that short-term price jumps in crypto assets result from wash trading-induced liquidity fluctuation. They construct two complementary liquidity measures:

1. **Liquidity jump (β_t^ℓ)**: Ratio of regular return to liquidity-adjusted return at the daily level — captures the **size** of liquidity fluctuation. Assets with low liquidity tend to have more days with high liquidity jump (β_t^ℓ > 1), indicating frequent large swings in daily liquidity.

2. **Liquidity diffusion (β_t^σ_ℓ)**: Ratio of regular volatility to liquidity-adjusted volatility at the daily level — reflects the **intraday volatility** of liquidity fluctuation. Assets with erratic or sporadic trading volume induced by manipulative trades see higher values (β_t^σ_ℓ > 1).

The theoretical model posits that manipulative traders (wash traders) amplify **both** the level and variance of price pressure, whereas passive investors affect only the level. Therefore, the **joint elevation** of both liquidity jump and liquidity diffusion (both ≥ 1) is the behavioral signature of wash trading. Large-volume trades that exhibit high liquidity jump but low liquidity diffusion are more likely legitimate high-demand transactions.

A simulated regulatory treatment that removes likely wash trades confirms this: it reduces liquidity diffusion significantly while leaving liquidity jump largely unaffected, supporting the interpretation that diffusion captures the manipulation-specific component.

### Research interpretation

The falsifiable hypothesis is: assets with jointly elevated liquidity jump (β_t^ℓ ≥ 1) and liquidity diffusion (β_t^σ_ℓ ≥ 1) are more likely subject to wash trading, and this condition predicts subsequent price dislocations (artificial pumps followed by dumps or rug pulls). The alpha angle is **negative screening**: avoid or reduce exposure to crypto assets exhibiting the joint LJ-LD signal, particularly in smaller-cap tokens where wash trading prevalence is highest.

This is a market-quality filter rather than a direct directional alpha signal. Its value lies in **risk avoidance** — identifying assets whose apparent liquidity and volume are artificially inflated — and potentially in **contrarian positioning** after the manipulation is detected.

## Signal

### Formation timestamp

- Daily-level signal, computed at end-of-day using minute-level intraday data.
- Signal becomes available at market close (T+0 end-of-day for 24/7 crypto markets).
- Timezone: UTC (Binance data).

### Lookback

- Minute-level Amihud-style liquidity ratio ℓ_τ = |r_τ| / A_τ computed for each minute τ in the trading day.
- Daily liquidity-adjusted return r_t^ℓ formed by aggregating minute-level liquidity-adjusted returns over the full trading day (T = 1,440 minutes for crypto).
- Daily liquidity jump β_t^ℓ = |r_t / r_t^ℓ| (Equation 6 in paper).
- Daily liquidity diffusion β_t^σ_ℓ = σ_t / σ_t^ℓ (Equation 7 in paper).
- Normalization: minute-level liquidity ratio ℓ_τ is normalized by daily trading volume; daily normalization factor η_t ensures cross-asset comparability.

### Entry / signal trigger (research-proposed)

**Source does not specify explicit trading entry/exit rules.** The following is a research-proposed operationalization:

- **Filter signal**: On day t, compute β_t^ℓ and β_t^σ_ℓ.
- **Wash trading flag**: If β_t^ℓ ≥ 1 AND β_t^σ_ℓ ≥ 1 → asset flagged as likely wash-traded on that day.
- **Threshold**: β_t^ℓ ≥ 1 and β_t^σ_ℓ ≥ 1 (these are the paper's own classification thresholds for "high" liquidity fluctuation/volatility, but the paper does not prescribe them as trading triggers).

### Exit / hold period (research-proposed)

- **Not specified by source.** Research-proposed: monitor daily; remove flag when both metrics fall below 1 on a sustained basis (e.g., 3 consecutive days).
- No directional entry/exit is proposed — this is a screening/avoidance signal.

### Position sizing (research-proposed)

- **Not specified by source.** Research-proposed: binary filter (exclude flagged assets from universe) or weight reduction proportional to joint LJ-LD severity.

### Parameters

- β_t^ℓ ≥ 1 and β_t^σ_ℓ ≥ 1 as "high" thresholds (paper's classification, not trading triggers).
- Maximum values capped at 10 in the paper's descriptive statistics.
- All parameters are as reported in the paper; no additional tuning was performed by the Scout.

## Required data

- **Instrument**: Crypto spot/perpetual on Binance (paper uses spot-equivalent OHLCV).
- **Universe**: Broad crypto universe; paper tests 10 large/mid-cap assets. Signal applicability to smaller-cap tokens is hypothesized but not tested.
- **Venue**: Binance (paper's primary data source); US stocks as benchmark.
- **Timeframe**: Minute-level bars (1-minute resolution).
- **Fields**: OHLCV (open, high, low, close, volume in USD). No order book, funding, or on-chain data required.
- **Timestamp**: UTC, minute-level precision.
- **Point-in-time**: No look-ahead issues — signal is computed from day-t data at day-t close.
- **Missing data**: Paper does not address missing data handling explicitly. Zero-volume minutes assigned a random value two magnitudes smaller than the daily average return to correct singularity in the Amihud ratio.
- **Data vendor**: Binance public API (paper's source); alternative sources possible.

## Execution assumptions

- **Signal-to-order timing**: End-of-day signal → next-day execution (research-proposed).
- **Order type**: Market order (research-proposed).
- **Fill model**: Not specified by source. Research-proposed: assume instant fill at next open for avoidance trades.
- **Fees**: Not modeled in the paper. Research-proposed: include standard maker/taker fees for crypto spot.
- **Slippage / spread**: Not modeled. The paper's analysis is purely diagnostic — it does not backtest a trading strategy.
- **Impact / capacity**: Not addressed. The signal is designed for asset-level screening, not high-frequency execution.
- **Leverage / margin**: Not applicable for avoidance screen. For contrarian shorting, leverage and funding considerations apply (not modeled).
- **Shorting**: Not addressed by paper. Research-proposed: contrarian shorting of flagged assets would require perpetual futures availability and funding cost modeling.
- **Latency**: Not applicable for daily-frequency signal.

## Evidence

### Source-reported

**Descriptive statistics (Table 2, Table 3 in paper):**

Without treatment on wash trading (raw data):
- Crypto assets show substantially higher mean liquidity jump than US stocks (e.g., ADA mean β_t^ℓ = 1.88 vs. AAPL mean 1.20).
- Crypto assets show higher mean liquidity diffusion (e.g., ADA mean β_t^σ_ℓ = 0.97 vs. AAPL mean 0.76).
- Joint elevation (β_t^ℓ ≥ 1 AND β_t^σ_ℓ ≥ 1) prevalence:
  - ADA: 16.23% of days
  - AVAX: 21.81%
  - BCH: 34.56%
  - BTC: 0.51%
  - ETC: 32.53%
  - ETH: 3.36%
  - LTC: 10.53%
  - SOL: 13.89%
  - UNI: 33.61%
  - XRP: 4.19%
  - US stocks: range 0.00%–0.57% (median ~0.04%)

With treatment (wash trades removed):
- Joint elevation drops significantly: BCH from 34.56% to 6.02%, UNI from 33.61% to 4.25%, BTC from 0.51% to 0.00%.
- Liquidity diffusion drops substantially (e.g., ADA from 0.97 to 0.77, BCH from 1.15 to 0.86).
- Liquidity jump drops moderately (e.g., ADA from 1.88 to 1.51, BCH from 1.99 to 1.59).
- This asymmetry (diffusion drops more than jump) confirms that wash trading primarily inflates the diffusion component.

**ANOVA pairwise tests (Table 4):**
- After treatment, crypto liquidity diffusion becomes statistically comparable to or lower than US stock levels for BTC and ETH (p < 0.001 for most pairs), confirming that wash trading is the primary driver of elevated diffusion in crypto.

**Key finding**: Smaller-cap crypto assets (BCH, ETC, UNI) show joint elevation on 30–35% of days; large-cap assets (BTC, ETH) show <4%. This concentration pattern suggests wash trading is disproportionately prevalent in smaller-cap tokens.

**No Sharpe, CAGR, or backtested trading returns are reported.** The paper is diagnostic/forensic, not a strategy backtest.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The paper acknowledges that large-volume legitimate trades can also produce high liquidity jump (β_t^ℓ ≥ 1) without wash trading. The joint condition (both metrics ≥ 1) is designed to filter these out, but false positives may still occur.
- The paper uses only 10 crypto assets; generalizability to the broader universe of thousands of tokens is untested.
- The simulated regulatory treatment is a heuristic, not a ground-truth wash-trading label. The paper does not have verified wash-trading ground truth.
- No out-of-sample or walk-forward validation of the detection framework is reported.
- The paper does not test whether the LJ-LD signal predicts subsequent returns or drawdowns.

## Falsification plan

1. **Out-of-sample walk-forward test**: Compute β_t^ℓ and β_t^σ_ℓ on a held-out sample (e.g., 2024–2025) and test whether joint elevation still predicts subsequent price dislocations. **Failure threshold**: If the joint signal does not predict subsequent 7-day or 30-day negative returns beyond a control universe, the detection framework has limited alpha value.
2. **Cross-exchange validation**: Test whether the signal holds on exchanges with different wash-trading profiles (e.g., regulated exchanges like Coinbase vs. unregulated). **Failure threshold**: If the signal is specific to Binance data characteristics, portability is limited.
3. **Ground-truth validation**: Compare LJ-LD flags against known wash-trading cases (e.g., exchange-reported wash trading, regulatory enforcement actions, or on-chain wash-trading detection). **Failure threshold**: If the false positive rate exceeds 50% against any reasonable ground truth, the signal is too noisy.
4. **Cap sensitivity**: Test whether the β_t^ℓ cap at 10 distorts results for extreme outliers. **Failure threshold**: If uncapped analysis materially changes the joint elevation frequencies, the capping introduces bias.
5. **Ablation**: Test whether liquidity diffusion alone (without liquidity jump) provides equivalent wash-trading detection. **Failure threshold**: If diffusion alone performs as well, the liquidity jump component adds no incremental information.
6. **Return prediction test**: Backtest a simple portfolio strategy: long assets with jointly low LJ-LD, short/avoid assets with jointly high LJ-LD. **Failure threshold**: If the long-short portfolio does not generate positive risk-adjusted returns after fees and slippage, the alpha angle is weak.

## Crypto portability

**Direct** — the paper is already designed for and tested on crypto assets (Binance spot). However:

- The paper uses spot-equivalent data. For perpetual futures, funding rates and mark prices introduce additional dynamics not captured by the LJ-LD framework.
- The 24/7 crypto session structure means the "trading day" is 1,440 minutes (vs. 390 for US stocks), which the paper accounts for.
- Exchange fragmentation: the signal is tested only on Binance. Other exchanges may have different wash-trading patterns.
- Smaller-cap tokens on DEXs (e.g., Uniswap, Raydium) may exhibit different liquidity dynamics than CEX-listed tokens.
- On-chain wash trading (e.g., through smart contracts) may not be captured by OHLCV-based liquidity measures.

## Limitations

- **Not a trading strategy**: The paper proposes a detection framework, not a backtested alpha signal. No returns, Sharpe ratios, or portfolio constructions are reported.
- **Diagnostic, not predictive**: The paper documents that wash trading elevates LJ-LD, but does not test whether detecting wash trading predicts future returns.
- **Small universe**: Only 10 crypto assets tested. Generalizability to the broader crypto universe (including DeFi tokens, meme coins, and small-cap altcoins) is untested.
- **No ground truth**: Wash-trading labels are inferred from the LJ-LD framework itself (circular) or from a simulated regulatory treatment. No independently verified wash-trading ground truth is available.
- **Capping at 10**: Both β_t^ℓ and β_t^σ_ℓ are capped at 10 in descriptive statistics, which may obscure extreme values.
- **Daily frequency only**: The signal is daily; intraday wash-trading detection is not addressed.
- **No transaction cost modeling**: The paper does not model trading costs, slippage, or market impact.
- **Single venue**: Binance only. Cross-exchange portability untested.
- **Sample period**: January 2021–May 2024. Performance in different market regimes (e.g., prolonged bear markets) is untested.
- **Data gap**: The paper does not specify whether volume includes both maker and taker trades, or whether wash trades are identifiable from the raw data before applying the LJ-LD framework.

## Implementation status

Not implemented. No code, backtest, or prototype has been built in our research stack. The paper provides code and data at https://doi.org/10.5281/zenodo.17830943, but this has not been independently executed.

## Adoption boundary

This record is research material only. Its presence does not mean:

- The LJ-LD signal is profitable
- Wash trading detection is validated alpha
- The signal is approved for implementation
- Any portfolio has been constructed, backtested, paper-traded, or live-traded using this framework

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` (schema specification)

No directly related strategy research records were identified in the repository that share the same source identity or materially overlap with this liquidity-jump-diffusion wash-trading detection framework.

## Sources

1. Qi Deng and Zhong-guo Zhou. "Liquidity Jump, Liquidity Diffusion, and Crypto Wash Trading." arXiv preprint `arXiv:2411.05803v4 [q-fin.RM, q-fin.CP, q-fin.ST, q-fin.TR]`, 2024-11-08. https://arxiv.org/abs/2411.05803v4
2. Dataset and code: https://doi.org/10.5281/zenodo.17830943
