---
schema: strategy-research-record-v1
title: "Mid-Tier Exchange Price Discovery Leadership and Intraday Funding Settlement Spread Patterns in Crypto Perpetual Futures"
created: 2026-09-21
updated: 2026-09-21
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - microstructure
  - market-structure
  - cross-venue
  - funding-rate
  - Granger-causality
status: research-only
confidence: medium
source_as_of: 2026-04-23
sources:
  - "https://doi.org/10.3390/ijfs14050103"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Mid-Tier Exchange Price Discovery Leadership and Intraday Funding Settlement Spread Patterns in Crypto Perpetual Futures

## Provenance

- **Paper:** Zhivkov, P., Todorov, V., & Georgiev, S. (2026). "Temporal Dynamics of Market Microstructure in Cryptocurrency Perpetual Futures: Econometric Evidence from Centralized and Decentralized Exchanges." *International Journal of Financial Studies*, 14(5), 103.
- **DOI:** https://doi.org/10.3390/ijfs14050103
- **Published:** 23 April 2026 (submission received 12 March 2026; revised 11 April 2026; accepted 16 April 2026)
- **Authors:** Petar Zhivkov (Bulgarian Academy of Sciences; "Angel Kanchev" University of Ruse; Centre of Excellence in Informatics and ICT, Bulgarian Academy of Sciences), Venelin Todorov (Bulgarian Academy of Sciences; Centre of Excellence in Informatics and ICT, Bulgarian Academy of Sciences), Slavi Georgiev (Bulgarian Academy of Sciences; "Angel Kanchev" University of Ruse)
- **Journal:** International Journal of Financial Studies, Special Issue "Mathematical Finance: Theory, Methods, and Applications"
- **Primary source checksum:** All figures below are verified from the published MDPI full text (Zhivkov et al. 2026, IJFS 14(5):103). This is a distinct paper from the same authors' earlier Mathematics 14(2):346 paper (already captured in this repo), extending the analysis with rolling-window temporal dynamics.

## Economic mechanism

### Source-reported

The authors apply rolling-window econometric methods to study how market integration in cryptocurrency perpetual futures evolves over time, rather than taking a static snapshot. Two key mechanisms emerge:

1. **Mid-tier exchange price discovery leadership:** Granger causality tests in bivariate VAR frameworks show that mid-tier exchanges lead the largest venue (Binance) more frequently than the reverse. This challenges the assumption that price discovery always originates at the largest venue. The economic interpretation is that mid-tier exchanges may have different participant mixes, lower latency for certain order types, or different incentive structures that allow them to incorporate information faster in some regimes.

2. **Intraday spread patterns linked to funding settlement:** Spreads peak approximately two hours after standard funding rate settlement times. This suggests that funding settlement creates transient liquidity imbalances or position-adjustment flows that widen spreads, creating a predictable intraday pattern.

### Research interpretation

The hypothesis is that the standard assumption — that Binance (the largest venue by volume) is always the primary price discovery venue — is incomplete. If mid-tier exchanges sometimes lead, then monitoring only Binance for price signals may cause a latency disadvantage. Two falsifiable sub-hypotheses:

1. **Mid-tier lead hypothesis:** Granger causality from mid-tier exchanges to Binance is statistically significant in a non-trivial fraction of rolling windows, and these lead periods are economically meaningful (i.e., the lead is large enough to be actionable after costs).
2. **Settlement spread hypothesis:** Funding rate settlement times create a predictable intraday spread widening pattern that could be exploited through limit-order placement or execution timing.

Note: The paper is primarily a descriptive econometric study, not a trading strategy proposal. The alpha hypothesis (exploitable signals from mid-tier lead and settlement spread patterns) is a research interpretation, not a source-reported trading strategy.

## Signal

### Sub-hypothesis 1: Mid-tier exchange lead

- **Formation timestamp:** Rolling 7-day window Granger causality test output.
- **Lookback:** 7-day rolling windows with 1-day step (53 overlapping windows in the study).
- **Signal:** When mid-tier exchange funding rates Granger-cause Binance funding rates (p < 0.05 in bivariate VAR), mid-tier is "leading."
- **Entry:** Research-proposed: enter a position on Binance after observing a mid-tier lead signal, in the direction suggested by the mid-tier price movement.
- **Exit:** Research-proposed: exit after a fixed holding period or when the lead signal dissipates.
- **Holding period:** Underspecified in source; the paper does not propose a specific holding period.
- **Parameters:** Research-defined: VAR lag order selected by information criteria; significance threshold p < 0.05; rolling window = 7 days.
- **Reconstruction status:** The signal is underspecified for direct reconstruction. The paper reports aggregate statistics (fraction of windows where mid-tier leads) but does not provide a per-window per-pair lead/lag signal table or timestamped output.

### Sub-hypothesis 2: Intraday settlement spread

- **Formation timestamp:** Time-of-day indexed; spreads measured relative to funding settlement times (00:00, 08:00, 16:00 UTC for 8-hour settlements).
- **Lookback:** Intraday spread patterns aggregated across the full sample.
- **Signal:** Spreads peak approximately 2 hours after settlement.
- **Entry:** Research-proposed: place limit orders or tighten execution timing to avoid the 2-hour post-settlement spread peak, or potentially provide liquidity at wider spreads during the peak.
- **Exit:** Research-proposed: close or reduce positions before the next settlement cycle.
- **Parameters:** Research-defined: "approximately 2 hours" is the reported timing; exact optimal offset is not specified.
- **Reconstruction status:** The paper reports the statistical significance of intraday spread patterns but does not provide per-observation spread data or a specific entry/exit rule.

## Required data

- **Instrument:** USDT-margined perpetual futures across 26 exchanges (11 centralized, 15 decentralized), 812 symbols.
- **Venue:** Binance (primary), plus Bybit, OKX, KuCoin, MEXC, Gate.io, Bitget, BingX, Phemex, Crypto.com, HTX (CEX), and Hyperliquid, Drift, Paradex, and others (DEX).
- **Market type:** Perpetual futures (USDT-margined).
- **Timeframe:** Hourly (9.1 million hourly observations); also intraday spread analysis at finer granularity (linked to settlement mechanics).
- **Fields:** Funding rate (bps), funding rate interval (1h, 4h, 8h), OI rank (liquidity proxy), timestamp with millisecond precision.
- **Sample period:** November 2025 through January 2026 (two months).
- **Point-in-time:** Data collected via exchange APIs and aggregation tools; exact availability lag not stated.
- **Missing data:** Minimum 2 exchanges per symbol required; 731 symbols with arbitrage potential after filtering.
- **Funding/fee/spread:** Funding rate dynamics are the primary variable; transaction costs and spread analysis are included in the arbitrage prevalence analysis.

## Execution assumptions

- **Signal-to-order timing:** Underspecified. The paper does not propose a specific trading strategy or execution model.
- **Fill model:** Not specified.
- **Fees:** Not explicitly modeled in the Granger causality or spread analysis; the paper focuses on econometric characterization rather than strategy P&L.
- **Slippage/spread:** Spread analysis is performed (intraday patterns documented) but not incorporated into a trading backtest.
- **Capacity:** Not assessed. The paper analyzes market structure dynamics, not strategy capacity.
- **Leverage/margin:** Not specified for strategy purposes.

## Evidence

### Source-reported

**Key findings from the published paper:**

1. **Integration gap dynamics:** The CEX-DEX integration gap ranges from −0.041 to 0.222 across rolling windows (integration gap = CEX-CEX correlation minus DEX-DEX correlation). The two-tiered structure persists qualitatively but varies substantially in magnitude. (Table/Figure: reported in the paper's rolling-window analysis section.)

2. **IGARCH in 24.5% of windows:** Near-integrated (IGARCH) volatility behavior appears in only 24.5% of rolling windows, concentrated in specific time periods. This contradicts previous reports of IGARCH as a general property of crypto perpetuals. (Source-reported from GARCH(1,1) estimation section.)

3. **Mid-tier price discovery leadership:** Granger causality tests show mid-tier exchanges lead Binance more frequently than the reverse. The paper reports this as challenging the "simple size-based price discovery hierarchy." (Source-reported from VAR Granger causality analysis section.) The exact fraction of windows where mid-tier leads is reported in the paper's results but the precise number should be verified from the full text.

4. **No discrete regime shifts:** Bai-Perron structural break detection finds no discrete regime shifts; the market evolves through gradual drift. CUSUM stability testing confirms this. (Source-reported.)

5. **Intraday spread patterns:** Spreads are statistically significant and linked to funding rate settlement mechanics, peaking approximately two hours after standard settlement times. (Source-reported from intraday analysis section.)

All results are source-reported and have not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed sources; absence is not evidence of no negative result. However, the paper itself notes limitations: the sample covers only two months (November 2025 through January 2026), which may not capture all market regimes. The gradual-drift finding (no discrete regime shifts) could be sample-period dependent.

## Falsification plan

1. **Out-of-sample replication:** Extend the rolling-window Granger causality analysis to a different time period (e.g., bull vs. bear regime) and verify whether mid-tier lead persists at similar rates.
2. **Per-pair lead signal quality:** For each exchange pair where mid-tier Granger-causes Binance, measure the forward return of a hypothetical trade that acts on the lead signal. If the lead is statistically significant but economically too small to cover costs after accounting for cross-venue transfer latency, the hypothesis fails.
3. **Settlement spread robustness:** Verify the 2-hour post-settlement spread peak across different assets, different settlement intervals (1h vs. 4h vs. 8h), and different market regimes. If the peak disappears in certain regimes or for certain assets, the hypothesis is weakened.
4. **Capacity stress test:** If mid-tier lead signals are acted upon by multiple participants, the lead should diminish (a standard adverse-selection/crowding test).
5. **Transaction cost sensitivity:** The gross edge from acting on mid-tier lead signals must exceed cross-venue transfer costs, settlement timing risk, and latency costs. If it does not, the signal is not tradeable.
6. **Baseline comparison:** Compare any hypothetical strategy against a simple "trade only on Binance" baseline. If the mid-tier lead signal does not improve risk-adjusted returns over the baseline, the signal has no incremental value.

Research-defined falsification threshold: If the mid-tier lead fraction falls below 30% of rolling windows in a new sample, or if the intraday spread peak timing shifts by more than 1 hour across regimes, the findings are materially weakened.

## Crypto portability

This study is natively crypto — it analyzes cryptocurrency perpetual futures across 26 exchanges. No porting is required.

Key crypto-specific considerations:
- The 24/7 trading structure means settlement cycles are continuous and differ from traditional market hours.
- DEX-specific frictions (blockchain settlement delays, gas fees, fragmented AMM liquidity) contribute to the integration gap.
- The study uses USDT-margined perps; results may differ for coin-margined or non-USDT-margined contracts.
- Exchange fragmentation is a defining feature of crypto derivatives markets, making cross-venue analysis uniquely relevant.

## Limitations

- **Short sample:** Two months (November 2025 – January 2026) is a limited window; results may not generalize across market regimes.
- **No strategy backtest:** The paper is purely descriptive econometric analysis. No trading strategy, P&L, or Sharpe ratio is reported. The alpha hypothesis (exploitable mid-tier lead signals) is a research interpretation, not a source claim.
- **Granger causality ≠ economic causality:** Statistical lead-lag relationships in funding rates do not guarantee that acting on them is profitable after costs.
- **Underspecified signal:** The paper reports aggregate statistics but does not provide a timestamped per-window lead/lag signal table that would allow direct strategy reconstruction.
- **Not independently reproduced:** The findings have not been replicated by independent researchers.
- **Settlement timing dependency:** The intraday spread pattern is linked to specific settlement times that vary by exchange; the pattern may not be stable if exchange settlement schedules change.
- **Potential overlap with existing records:** The same authors' earlier paper (Mathematics 14(2):346, already captured) covers related two-tiered structure findings; this record is distinct in its rolling-window dynamics, mid-tier lead finding, and intraday spread analysis.

## Implementation status

No implementation in our research stack. No backtest, prototype, or paper-trading verification has been performed.

## Adoption boundary

This record is research material only. Its presence in this repository does not mean:
- Passed Research Intake Review;
- Entered Hermes Wiki Brain;
- Entered the production candidate pool;
- Completed Qlib full-backtest validation;
- Became a frozen survivor or leaderboard entry;
- Profitable;
- Validated alpha;
- Approved for implementation;
- Approved for paper trading;
- Approved for testnet;
- Approved for live trading.

## Related Wiki records

- `[[crypto-two-tiered-cex-dominant-funding-discovery-structural-arbitrage-2026-09-12]]` — Zhivkov (2026), Mathematics 14(2):346. The earlier static-snapshot paper by the same authors. This record is distinct: it extends the analysis with rolling-window temporal dynamics, discovers mid-tier price discovery leadership (vs. Binance), documents IGARCH in only 24.5% of windows, and identifies intraday spread patterns linked to funding settlement mechanics.
- `[[crypto-cex-dex-cross-venue-funding-spread-carry-2026-08-31]]` — Related cross-venue funding analysis; distinct focus on carry trade risk decomposition.
- `[[cross-venue-funding-carry-patient-rebalance-vs-active-harvesting-2026-09-12]]` — Related cross-venue funding dynamics; distinct focus on carry strategy variants.

## Sources

1. Zhivkov, P., Todorov, V., & Georgiev, S. (2026). "Temporal Dynamics of Market Microstructure in Cryptocurrency Perpetual Futures: Econometric Evidence from Centralized and Decentralized Exchanges." *International Journal of Financial Studies*, 14(5), 103. DOI: https://doi.org/10.3390/ijfs14050103. Published 23 April 2026. Open access.
