---
schema: strategy-research-record-v1
title: "LLM-Distilled KOL Consensus — Capability-Factor Aggregation from Crypto Trader Experience"
created: 2026-09-18
updated: 2026-09-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - social-sentiment
  - consensus
  - LLM
  - KOL
  - factor-discovery
status: research-only
confidence: low
source_as_of: 2026-04-12
sources:
  - "GitHub: https://github.com/0xquqi/crypto-kol-quant, commit 39be26a816e1e34991bfc2a4b7a4791d52a8a001 (Apr 12, 2026)"
  - "FMZ implementation: https://www.fmz.com/bbs-topic/10943"
  - "DEV.to implementation writeup: https://dev.to/quant001/from-99-traders-to-one-signal-implementing-a-distilled-kol-consensus-strategy-on-fmz-n2a"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# LLM-Distilled KOL Consensus — Capability-Factor Aggregation from Crypto Trader Experience

## Provenance

- **GitHub repository:** https://github.com/0xquqi/crypto-kol-quant
- **Full commit SHA:** `39be26a816e1e34991bfc2a4b7a4791d52a8a001` (Apr 12, 2026 — only commit on main)
- **Author:** quqi (曲奇)
- **License:** MIT
- **Stars:** ~300 (as of Sep 2026)
- **FMZ implementation blog:** https://www.fmz.com/bbs-topic/10943
- **FMZ implementation writeup (dev.to):** https://dev.to/quant001/from-99-traders-to-one-signal-implementing-a-distilled-kol-consensus-strategy-on-fmz-n2a
- **Primary source inspection:** GitHub README, file structure, factor tables, and backtest claims were directly read on 2026-09-18. The FMZ implementation writeup was read for additional methodology details.

## Economic mechanism

### Source-reported

The project distills the trading experience of 99 selected crypto KOLs (key opinion leaders) into computable capability factors using LLMs. The pipeline is:

1. **Input:** 39,843 tweets (Jan 2024 – Apr 2026) and 17,657 chart screenshots (1.7 GB) from 99 S-tier traders selected from 1,000+ candidates through a three-round screening process.
2. **LLM distillation:** Each trader's public posts are analyzed to produce a profile containing 15–25 "capabilities" — quantifiable trading frameworks (e.g., "200-week MA mechanical buy," "4-year cycle distribution phase short," "false breakout reversal").
3. **Capability library:** 470 total capabilities extracted (70 seed + 400 emergent), mapped to 87 Python evaluators (quant factors).
4. **Factor evaluation:** Each evaluator is backtested against 832 days of daily OHLCV for BTC, ETH, SOL, DOGE, plus DXY, gold, US Treasury, and SPX. IC (information coefficient) is computed per factor.
5. **Trader trust scoring:** Each trader's distilled profile is evaluated by producing a composite signal from their capability factors and regressing against historical returns, yielding a per-trader IC.
6. **Consensus aggregation:** At each evaluation step, the current market state triggers a subset of capability factors. Each trader's personal signal is computed from their active capabilities. Final consensus is produced by IC-weighted or trust-adjusted aggregation across all 99 traders.

Source reports 87 factors evaluated, with 16 statistically significant. Top 5 factors by IC:

| Factor | IC | Asset | Source trader | Description |
|---|---|---|---|---|
| 200W MA value zone | +0.297 | SOL | @LedgerStatus | Price near 200-week MA = historically significant buy zone |
| 200W MA mechanical buy | +0.220 | BTC | @IvanOnTech | Buy on touch of 200-week MA unconditionally |
| 4-year cycle thesis | +0.201 | BTC | @rektcapital | 18 months post-halving = distribution/bear phase |
| OHLC anchor | +0.109 | — | @KillaXBT | Weekly open as intraday support/resistance |
| Strong downtrend | +0.098 | BTC | @DrProfitCrypto | Price below 200-day MA + death cross |

Source also reports two strong contrarian (inverse) factors: "gold safe haven" (IC −0.218 on SOL — gold rally does not predict BTC rally) and "strong uptrend" (IC −0.100 on BTC — trend-following long at cycle end is a top signal).

### Research interpretation

The hypothesized mechanism is:

1. **Expertise extraction via LLM:** Experienced traders develop implicit market models (structural, cyclical, indicator-based, macro). LLMs can extract and formalize these models from natural language + chart screenshots.
2. **Capability-factor mapping:** Each extracted "capability" becomes a condition-triggered factor that fires when specific market structures are detected. This is closer to regime/structure detection than traditional continuous factor scoring.
3. **IC-weighted consensus:** Individual trader signals are aggregated by historical predictive quality, not by popularity or loudness. This is a form of meta-learning: the system learns *which* experts to weight more heavily under which conditions (though the current implementation uses static IC weights, not dynamic).
4. **Cross-asset generalization:** Factors trained on BTC/ETH/SOL/DOGE daily bars are applied to generate consensus across all four assets, with macro context (DXY, gold, yields, SPX) providing additional conditioning.

This is conceptually related to "expert survey" or "prediction market" aggregation, but replaces human survey responses with LLM-extracted capability profiles. The key research question is whether the LLM distillation preserves genuine signal or introduces noise/overfitting.

## Signal

- **Signal formation timestamp:** Evaluated once per day (daily bars). The FMZ implementation also supports 5-minute scalping mode (daily direction filter + 5m entry).
- **Lookback window:** Factors use various lookback windows embedded in the 470 capabilities (e.g., 200-week MA, 200-day MA, 4-year cycle). The feature engine computes 88 features.
- **Long entry:** When consensus signal is bullish (majority of IC-weighted trader signals agree on long direction for a given asset).
- **Short entry:** When consensus signal is bearish.
- **Exit:** Not explicitly specified in the primary source; the FMZ implementation mentions exit on signal reversal or after a time-based holding period (underspecified in the GitHub repo).
- **Holding period:** Underspecified. The backtest claims use daily rebalancing (BTC daily bars) or 5-minute scalping with unspecified holding.
- **Re-entry rules:** Not explicitly specified.
- **Parameters:** IC thresholds for factor significance, trader selection criteria (3-round screening from 1000+ candidates), consensus aggregation method (IC-weighted or trust-adjusted).
- **Position sizing logic:** Not specified in the primary source.
- **Multi-timeframe dependencies:** The system supports both daily (macro direction) and 5-minute (entry timing) timeframes in scalping mode.
- **Fully specified / underspecified:** The core distillation pipeline and factor evaluation are specified. The consensus aggregation formula is specified. Entry/exit rules, position sizing, and risk management are underspecified.

## Required data

- **Instrument / universe:** BTC, ETH, SOL, DOGE (primary); DXY, gold, US Treasury yields, SPX (macro context).
- **Venue:** Binance (for OHLCV data and trading).
- **Market type:** Spot and perpetual futures (Binance USDT-M).
- **Timeframe:** Daily bars (primary); 5-minute bars (scalping mode).
- **OHLCV fields:** Required for all 4 crypto assets + 4 macro indicators.
- **Funding / OI / Greeks:** Not used in the current implementation; listed as potential extensions.
- **Timestamp and timezone:** UTC (Binance standard).
- **Point-in-time / availability:** KOL tweets are scraped from Twitter/X with timestamps; the distillation is done offline on historical data. For live use, tweet scraping would need to be ongoing.
- **Missing-data assumptions:** The system assumes daily bars are continuously available. Macro data (DXY, gold, yields, SPX) availability varies by source.

## Execution assumptions

- **Signal-to-order timing:** End-of-day signal for daily mode; 5-minute signal for scalping mode (underspecified which bar the signal applies to).
- **Next-bar vs same-bar execution:** Underspecified in the primary source.
- **Market / limit order:** Underspecified.
- **Fill model:** Underspecified.
- **Fees:** Not modeled in the backtest claims.
- **Spread:** Not modeled.
- **Slippage:** Not modeled.
- **Impact / capacity:** Not addressed. The strategy targets large-cap crypto assets (BTC, ETH, SOL, DOGE), which have high liquidity, but consensus signal timing is not stress-tested for capacity.
- **Funding:** Not modeled for perpetual futures.
- **Leverage / margin:** Not specified.
- **Latency:** Not relevant at daily frequency.
- **Partial fills / failures:** Not addressed.

## Evidence

### Source-reported

- **Factor IC evaluation:** 87 factors evaluated on 832 days of daily OHLCV. 16 factors reported as statistically significant. Top factor IC: +0.297 (200W MA value zone on SOL). Source-reported results have not been independently reproduced.
- **BTC 7-day directional backtest:** Following consensus signal direction on BTC daily bars over 7 days: win rate 57%, $1,000 → $1,079 (+7.9%). Source explicitly warns: "7-day sample is not statistically significant."
- **BTC 5-minute scalping backtest:** Daily consensus as direction filter + 5-minute entry: win rate improved from 50% to 59%, profit factor 1.28. Source reports this as directional-filter improvement, not standalone alpha.
- **Trader trust scores:** 58 traders with positive IC, 41 with negative IC, 21 with |IC| > 0.1. Top 5 by IC: @Yodaskk (+0.145), @dpuellARK (+0.110), @AnalysisElliott (+0.106), @Tree_of_Alpha (+0.103), @ToneVays (+0.099). Top 5 contrarians: @christiaandefi (−0.210), @shufen46250836 (−0.180), @WClementeIII (−0.158), @Engineercryptoo (−0.157), @GugaOnChain (−0.143).

All figures above are source-reported from the GitHub README and have not been independently reproduced by any third party.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The source explicitly states the 7-day sample is not statistically significant.
- IC values are computed on the same historical period used for factor extraction (in-sample only). No out-of-sample validation is reported.
- Trader profiles and IC values are static inputs; the system has not been tested with online/rolling re-evaluation.
- The FMZ implementation blog notes: "Trader profiles and IC values are still static inputs — the system hasn't yet entered an online-evolution phase."
- The contrarian factors (gold safe haven IC −0.218, strong uptrend IC −0.100) suggest that some of the KOL-extracted capabilities are systematically wrong in specific regimes.
- No transaction cost, slippage, or funding cost is modeled in any reported backtest.

## Falsification plan

- **Out-of-sample factor validation:** Compute IC on a rolling forward window (e.g., 6-month rolling) and compare with in-sample IC. If forward IC decays to noise for >50% of the "significant" factors, the distillation pipeline is not generating durable signal.
- **Ablation: remove LLM distillation layer:** Compare factor IC when factors are manually specified by the researcher (without LLM extraction) versus LLM-extracted factors. If manual factors perform similarly, the LLM adds no incremental value.
- **Ablation: remove consensus layer:** Test individual top-factor signals (e.g., 200W MA mechanical buy alone) versus the full consensus. If individual factors dominate, the aggregation adds no value.
- **Cost sensitivity:** Add realistic transaction costs (0.04% one-way, 0.08% round-trip for taker fees on Binance futures) and slippage. If the 7-day +7.9% result is eroded below significance, the alpha is not tradeable.
- **Temporal stability:** Test whether the same KOL profiles and factor ICs hold across different market regimes (bull 2024, bear 2022-2023, sideways).
- **Failure threshold (research-defined):** If rolling 90-day forward IC for the consensus signal drops below 0.03 (indistinguishable from noise), the hypothesis is materially weakened.
- **Action on failure:** Abandon the consensus aggregation approach; investigate whether individual high-IC factors (200W MA, 4-year cycle) have standalone value independent of the KOL distillation.

## Crypto portability

direct

The strategy is native to crypto markets (BTC, ETH, SOL, DOGE on Binance). The KOLs being distilled are crypto-specific traders, and the factor library is built on crypto price patterns. The macro context (DXY, gold, yields, SPX) is traditional-asset data used as conditioning, not as the primary trading universe.

Crypto-specific considerations:
- 24/7 market structure supports continuous daily bar availability.
- Perpetual futures funding rates are not currently modeled but could affect carry costs for longer-horizon signals.
- The 200-week MA factors are specific to crypto assets with sufficient history (BTC since 2010, ETH since 2015).
- The 4-year halving cycle factor is inherently crypto-specific.

## Limitations

- **In-sample only:** All factor ICs and trust scores are computed on the same data used for distillation. No out-of-sample or rolling-forward validation is reported.
- **Static profiles:** Trader capability profiles are frozen at the time of distillation. Trader views evolve over time; the system does not update.
- **Underspecified execution:** Entry/exit timing, position sizing, order type, and risk management are not specified in the primary source.
- **Tiny backtest sample:** The 7-day directional backtest is explicitly acknowledged as not statistically significant.
- **No cost modeling:** No transaction fees, slippage, spread, or funding costs are included in any reported result.
- **LLM distillation quality:** The fidelity of LLM-extracted capabilities to the actual trading methodology of each KOL is not validated. The system assumes LLMs can faithfully extract trading knowledge from tweets and chart screenshots, which is an unverified assumption.
- **Survivorship bias in KOL selection:** The 99 KOLs were selected from 1,000+ candidates through a three-round process. If selection was influenced by recent performance, survivorship bias could inflate reported IC.
- **Not independently reproduced:** No third-party has replicated these results.

## Implementation status

Not implemented in our research stack.

## Adoption boundary

This record is research material only. A record being present in this repository does not mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

The source explicitly warns that backtest results are not statistically significant and the system is an early prototype.

## Related Wiki records

- `[[quant/crowd-trading-signals-social-media-crypto-short-term-predictability-2026-09-11]]` — Related concept: social media trading signals for crypto, but uses explicit buy/sell crowd signals (Haase et al. 2025) rather than LLM-distilled KOL capability profiles. Different mechanism (crowd sentiment vs. expert methodology extraction).
- `[[quant/adaptive-multi-agent-bitcoin-verbal-feedback-2026-09-04]]` — Related concept: multi-agent verbal feedback for Bitcoin, but uses a different architecture (agent debate rather than KOL distillation).
- `[[quant/strategy-research-record-spec-v1]]` — Schema specification.

## Sources

1. quqi (曲奇). "crypto-kol-quant: 首个将99位加密KOL交易经验LLM蒸馏为可回测量化因子的开源项目." GitHub repository, commit `39be26a816e1e34991bfc2a4b7a4791d52a8a001` (April 12, 2026). https://github.com/0xquqi/crypto-kol-quant. MIT License.
2. FMZ Quant. "From 99 Traders to One Signal: Implementing a Distilled KOL Consensus Strategy on FMZ." FMZ BBS Topic 10943. https://www.fmz.com/bbs-topic/10943.
3. quant001. "From 99 Traders to One Signal: Implementing a Distilled KOL Consensus Strategy on FMZ." DEV Community, May 18, 2026. https://dev.to/quant001/from-99-traders-to-one-signal-implementing-a-distilled-kol-consensus-strategy-on-fmz-n2a.
