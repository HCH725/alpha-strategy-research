---
schema: strategy-research-record-v1
title: "Telegram-Coordinated Pump-and-Dump Detection via Temporal Synchronization: Contrarian Fade of Anomalous Social Bursts"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - pump-and-dump
  - telegram
  - social-media
  - manipulation-detection
  - contrarian
  - microstructure
  - event-driven
status: research-only
confidence: medium
source_as_of: 2026-09-01
sources:
  - "Filipe Moura, Giordano Paoletti, Carlos H.G. Ferreira, and Jussara M. Almeida, 'Don't You Know, Pump it Up! Investigating Cryptocurrency Manipulation in Telegram-Driven Activity', arXiv preprint arXiv:2609.01176v1 [cs.SI], submitted September 1, 2026. Accepted at ICWSM 2027. https://arxiv.org/abs/2609.01176"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Telegram-Coordinated Pump-and-Dump Detection via Temporal Synchronization: Contrarian Fade of Anomalous Social Bursts

## Provenance

- **Primary Source:** Filipe Moura (Universidade Federal de Minas Gerais, Brazil, filipe.moura@dcc.ufmg.br), Giordano Paoletti (Politecnico di Torino, Italy, giordano.paoletti@polito.it), Carlos H.G. Ferreira (Universidade Federal de Ouro Preto, Brazil, chgferreira@ufop.edu.br), and Jussara M. Almeida (Universidade Federal de Minas Gerais, Brazil, jussara@dcc.ufmg.br), *"Don't You Know, Pump it Up! Investigating Cryptocurrency Manipulation in Telegram-Driven Activity"*, arXiv preprint `arXiv:2609.01176v1 [cs.SI]`, submitted September 1, 2026. Accepted at ICWSM 2027.
  - Stable arXiv URL: https://arxiv.org/abs/2609.01176
  - Full-text HTML: https://arxiv.org/html/2609.01176v1
  - Full-text PDF: https://arxiv.org/pdf/2609.01176v1
  - Canonical DOI: [10.48550/arXiv.2609.01176](https://doi.org/10.48550/arXiv.2609.01176)
  - Code: https://github.com/Filipey/investigating-cryptocurrency-manipulation-icwsm2027
  - Dataset: https://huggingface.co/datasets/filipeasm18/crytpo-related-labeling
  - Dictionary: https://doi.org/10.5281/zenodo.22116582
  - Model: https://huggingface.co/filipeasm18/roberta-binary-crypto-related-classifier
- **Sample Period:** July 2021 – July 2022 (12 months)
- **Universe:** 14,499 public Telegram channels, 20M+ messages, 17,000+ cryptocurrencies
- **Publication Status:** Accepted at ICWSM 2027 (21st International AAAI Conference on Web and Social Media)

## Economic mechanism

### Source-reported

The authors hypothesize that successful pump-and-dump schemes operate in two phases: a private coordination phase (closed groups) and a public amplification phase (open channels) to generate exit liquidity. Public Telegram channels carry a systematic, temporally compressed signal observable even without access to private orchestration chats. The authors document that coordinated shilling bursts on Telegram are characterized by **extreme temporal synchronization** across hundreds of channels, and that these synchronized bursts precede price movements by seconds. Critically, psycholinguistic analysis reveals that pump-and-dump messages are **linguistically indistinguishable from organic discussions** — text-based content analysis alone cannot distinguish manipulation from genuine interest. The distinguishing signal is temporal, not semantic.

### Research interpretation

The hypothesized mechanism is **coordinated social attention injection followed by retail herding and exit liquidity extraction**. The falsifiable alpha hypothesis: detect anomalous temporal synchronization of cryptocurrency mentions across public Telegram channels (via CA-CFAR signal processing on message volume), classify events as potential pump-and-dump vs. sustained market reactions using RDD+DiD quasi-experimental methods, and **fade confirmed P&D events** by entering short positions after the initial spike peaks (Reversal Ratio > 0.7 and Volume Decay < 0.3).

The signal construction is:
1. **Detection layer:** Fine-tuned RoBERTa classifier filters crypto-related messages (94% recall, 92.2% F1).
2. **Anomaly layer:** Cell-Average Constant False Alarm Rate (CA-CFAR) algorithm detects statistically anomalous spikes in daily cryptocurrency mention volume across all 17,000+ tracked coins.
3. **Classification layer:** RDD identifies instantaneous price/volume jumps at burst onset (T0); DiD using stablecoins and Bitcoin as control groups filters systemic noise; Reversal Ratio > 0.7 or Volume Decay < 0.3 classifies as P&D.
4. **Trading layer (research-proposed):** After P&D classification, fade the pump — enter short after the detected spike peaks.

The source does NOT propose a specific trading strategy. The trading signal described above is **entirely Scout-generated (research-proposed)**, derived from the paper's empirical findings about P&D event dynamics.

## Signal

- **Formation timestamp:** Real-time monitoring of Telegram public channels; anomaly detected at daily granularity (CA-CFAR), price classification at 1-minute resolution.
- **Lookback window:** CA-CFAR training cells: N=5 days on each side of the cutoff; guard cells: M=1 day on each side; false alarm probability Pf=0.05. RDD window: ±1.5 hours around T0 (first message burst timestamp).
- **Long entry:** Not applicable — this is a contrarian/short-side signal.
- **Short entry (research-proposed):** After confirmed P&D classification (RDD jump > 1%, p < 0.05, DiD significant, Reversal Ratio > 0.7 or Volume Decay < 0.3). Entry timing: research-proposed at T0 + 15 minutes (allowing the pump to peak).
- **Exit (research-proposed):** Time-based exit at T0 + 60 minutes, or when price reverts to pre-burst level (whichever first). Source-reported average dump duration is 32.1 minutes; average dump magnitude is -14.84%.
- **Holding period (research-proposed):** 15–60 minutes.
- **Parameters:** CA-CFAR thresholds (N=5, M=1, Pf=0.05); RDD bandwidth 1.5 hours; classification thresholds (Reversal Ratio > 0.7, Volume Decay < 0.3, jump > 1%, p < 0.05). All thresholds are source-reported for detection; entry/exit timing is research-proposed.
- **Position sizing (research-proposed):** Not specified by source; underspecified.
- **Market type:** Crypto spot and perpetual futures on exchanges where affected tokens trade.
- **Universe:** Low-to-mid cap altcoins (the 47 P&D events targeted coins with market caps substantially below Bitcoin/Ethereum).
- **Underspecified items:** Exact entry price/timing, position sizing, leverage, stop-loss, and capacity constraints are not specified by the source. The paper is a measurement/detection study, not a trading strategy proposal.

## Required data

- **Instrument:** 17,000+ cryptocurrencies tracked across exchanges (CoinDesk Data API used for market data).
- **Venue:** Data sourced from CoinDesk Data API (OHLCV at 1-minute resolution). Telegram data from TGDataset (14,499 public channels, 20M+ messages, July 2021 – July 2022).
- **Market type:** Crypto spot.
- **Timeframe:** 1-minute OHLCV for market data; daily aggregation for CA-CFAR anomaly detection.
- **Fields:** Message volume per cryptocurrency per day (from Telegram); OHLCV (1-minute); trading volume z-scores.
- **Point-in-time:** Telegram messages timestamped to the minute; market data from CoinDesk API. The paper uses historical data (2021-2022); real-time deployment would require live Telegram monitoring and exchange data feeds.
- **Missing-data assumptions:** Not all Telegram channels are captured; the dataset covers public channels only. The TGDataset is a snapshot, not a live feed. Exchange coverage is heterogeneous across the 17,000+ coins.
- **Funding/fee/spread needs:** Not modeled in the paper. The paper is a measurement study, not a trading backtest.

## Execution assumptions

- **Signal-to-order timing:** Not specified by source. The paper documents that social bursts precede price movements by seconds — extremely tight latency.
- **Fill model:** Not specified.
- **Fees:** Not modeled.
- **Spread/slippage:** Not modeled.
- **Impact/capacity:** Not modeled. The affected tokens are low-mid cap altcoins with potentially thin liquidity; capacity constraints are likely binding.
- **Leverage:** Not modeled.
- **Latency:** The paper shows bursts precede price movements by seconds; real-time detection and execution would require sub-second infrastructure.
- **Failure handling:** Not specified.

## Evidence

### Source-reported

1. **Detection scale:** 9,799 anomalous social bursts detected; 302 showed price/volume jumps (RDD); 120 validated after DiD filtering; 47 classified as P&D, 73 as Sustained Market Reaction (SMR).
2. **P&D economic impact (47 events):**
   - Cumulative financial volume: $234.8M
   - Average price increase during pump: +9.98%
   - Average price decrease during dump: -14.84%
   - Average pump duration: 14.6 minutes
   - Average dump duration: 32.1 minutes
3. **SMR economic impact (73 events):**
   - Cumulative financial volume: $828.8M
   - Average price increase: +18.56%
   - Average price decrease: -5.36%
4. **Temporal precedence:** Social bursts precede price movements by seconds (RDD jump at T0). Placebo test at T0-3h yielded only 1 statistically significant case out of 302, supporting the validity of T0 as a genuine sudden anomaly.
5. **Discriminative features:** P&D events are characterized by extreme temporal synchronization across hundreds of channels (43,675 messages, 2,391 unique channels), rapid volume decay (VD < 0.3), and high reversal (RR > 0.7). Psycholinguistic analysis shows P&D messages are linguistically indistinguishable from organic discussions — temporal synchronization, not content, is the signal.
6. **Classifier performance:** Fine-tuned RoBERTa-base: 94.0% recall, 92.2% F1 on crypto-related message classification; 4.78ms inference latency per message.

Source-reported figures trace to: Moura et al. (arXiv:2609.01176v1, Tables and text). The paper reports aggregate statistics across all 47 P&D events and 73 SMR events. No individual event-level backtest or trading simulation is provided.

### Independently reproduced

Not independently reproduced. All figures and performance metrics represent third-party reported findings from Moura et al. (arXiv:2609.01176v1).

### Negative evidence

- The paper is a measurement/detection study, not a trading strategy. No backtest of a contrarian fade strategy is provided.
- P&D messages are linguistically indistinguishable from organic discussions, limiting the utility of content-based detection.
- The paper does not test whether the detected signals are tradeable net of costs, slippage, or capacity constraints.
- Only 47 P&D events were validated out of 9,799 anomalous bursts — the vast majority of detected bursts do not translate into tradeable pump-and-dump events.
- The study covers a single year (July 2021 – July 2022); temporal stability across market regimes is unknown.
- None identified in the reviewed sources for the specific hypothesis of fading P&D events; absence is not evidence of no negative result.

## Falsification plan

1. **Out-of-sample replication:** Apply the CA-CFAR + RDD + DiD framework to a different time period (e.g., 2023-2024) and a different Telegram dataset. Expected: at least 30+ validated P&D events with similar average pump/dump magnitudes and durations.
2. **Contrarian fade backtest (research-defined):** Simulate a short entry at T0 + 15 min (after pump peak) with exit at T0 + 60 min or pre-burst price (whichever first), across all 47 P&D events. **Failure threshold:** if the mean trade return is ≤ 0 after 10 bps one-way cost, the contrarian hypothesis is falsified.
3. **False positive rate:** If more than 50% of CA-CFAR-detected bursts that pass RDD+DiD classification fail to produce a Reversal Ratio > 0.5 within 60 minutes, the classification thresholds are too loose.
4. **Capacity stress test:** Scale position sizes to 10% of the average 60-minute volume for the affected tokens. If slippage exceeds the average dump magnitude (-14.84%), the strategy is capacity-constrained.
5. **Regime stability:** Compare P&D frequency and magnitude across bull (2021 H2) vs. bear (2022 H1) regimes. If the detection rate drops below 20 events/year in bear markets, regime-dependent filtering is required.
6. **Action on failure:** If the contrarian fade fails, re-evaluate whether the signal is exploitable at all or whether it is a measurement artifact.

## Crypto portability

**direct** — the paper is already conducted on crypto markets (17,000+ cryptocurrencies across exchanges, Telegram as the social platform). The mechanism is specific to crypto's market structure: low-cap tokens with thin liquidity, 24/7 trading, social-media-driven retail participation, and fragmented venue coverage. The signal depends on Telegram, which is a crypto-native communication infrastructure.

Crypto-specific portability risks:
- **Liquidity:** The affected tokens are low-to-mid cap altcoins with potentially thin order books; shorting may require perpetual futures or margin availability that does not exist for many of these tokens.
- **Venue fragmentation:** The target tokens may trade on different exchanges with different liquidity profiles.
- **Telegram access:** Real-time monitoring of 14,499+ public Telegram channels requires significant infrastructure.
- **Regulatory:** Shorting low-cap altcoins may be restricted on certain venues or jurisdictions.

## Limitations

- The paper is a measurement/detection study, not a trading strategy proposal. The contrarian fade signal is **entirely Scout-generated (research-proposed)**.
- **Underspecified:** Entry/exit timing, position sizing, leverage, stop-loss, and capacity constraints are not specified by the source.
- **Data gap:** The paper does not model transaction costs, slippage, spread, funding, or market impact.
- **Data gap:** The paper does not provide individual event-level price data that would allow independent replication of the average pump/dump statistics.
- **Small sample:** Only 47 P&D events validated; statistical power for regime-dependent analysis is limited.
- **Single year:** July 2021 – July 2022 only; results may not generalize across market regimes.
- **Telegram data availability:** The TGDataset is a historical snapshot; real-time Telegram monitoring at this scale is a non-trivial engineering challenge.
- **Telegram's evolving ecosystem:** Telegram's user base, channel structure, and moderation policies evolve; the 2021-2022 snapshot may not represent current conditions.
- **not independently reproduced**
- **unproven** — the contrarian fade strategy has not been backtested.

## Implementation status

No implementation in our research stack. The paper provides code, a dataset, a dictionary, and a classifier model (links in Provenance), but no trading simulation.

## Adoption boundary

This record is research material only. A record being present in this repository does **not** mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

The contrarian fade signal is entirely Scout-generated and has not been backtested. The source paper is a measurement study, not a trading strategy.

## Related Wiki records

- `[[quant/crowd-trading-signals-social-media-crypto-short-term-predictability-2026-09-11]]` — different mechanism: explicit social media buy/sell signals vs. detection of coordinated manipulation bursts.
- `[[quant/crypto-cross-sectional-abnormal-investor-attention-momentum-2026-08-31]]` — related: social attention as a driver of crypto returns, but cross-sectional rather than event-driven.
- `[[quant/digital-twin-finfluencer-belief-elicitation-silent-region-cross-sectional-2026-09-06]]` — related: social media influence on crypto markets, but different detection methodology.

No directly related strategy research records share the same source identity or materially identical mechanism.

## Sources

1. Filipe Moura, Giordano Paoletti, Carlos H.G. Ferreira, and Jussara M. Almeida. *"Don't You Know, Pump it Up! Investigating Cryptocurrency Manipulation in Telegram-Driven Activity"*, arXiv preprint `arXiv:2609.01176v1 [cs.SI]`, submitted September 1, 2026. Accepted at ICWSM 2027. https://arxiv.org/abs/2609.01176
