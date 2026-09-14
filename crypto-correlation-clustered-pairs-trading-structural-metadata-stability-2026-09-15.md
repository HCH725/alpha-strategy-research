---
schema: strategy-research-record-v1
title: "Correlation-Clustered Crypto Pairs Trading with Structural Metadata and Stability Diagnostics (Stoikov et al. 2026)"
created: 2026-09-15
updated: 2026-09-15
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - pairs-trading
  - statistical-arbitrage
  - correlation-clustering
  - crypto-perpetuals
  - mean-reversion
  - market-neutral
  - live-trading
status: research-only
confidence: medium
source_as_of: 2026-02-25
sources:
  - "Sasha Stoikov, Dora Xu, Shijie Shao, Yourui Wang, Tongshu Zhang, Jinxuan Hu, Federico Cardoso, 'Pairs Trading in Crypto', Cornell University / Hummingbot, SSRN 6188418, posted February 25, 2026 (written December 12, 2025). https://ssrn.com/abstract=6188418"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Correlation-Clustered Crypto Pairs Trading with Structural Metadata and Stability Diagnostics (Stoikov et al. 2026)

## Provenance

- **Primary Source:** Sasha Stoikov, Dora Xu, Shijie Shao, Yourui Wang, Tongshu Zhang, Jinxuan Hu, and Federico Cardoso, "Pairs Trading in Crypto", Cornell University / Hummingbot, SSRN working paper 6188418, posted February 25, 2026 (written December 12, 2025). DOI: https://dx.doi.org/10.2139/ssrn.6188418. URL: https://ssrn.com/abstract=6188418.
- **Author Affiliation:** Cornell Financial Engineering Manhattan (Sasha Stoikov, contact author); Cornell University (Dora Xu, Shijie Shao, Yourui Wang, Tongshu Zhang, Jinxuan Hu); Hummingbot (Federico Cardoso).
- **Source Type:** SSRN working paper, 36 pages.
- **Primary Source Access:** SSRN abstract and metadata verified. Full PDF access restricted (SSRN paywall). Performance figures below are drawn from the abstract and publicly available summaries; specific backtest tables, parameter values, and detailed methodology sections are not verifiable without full PDF access and are therefore marked as data gaps where applicable.
- **Repository Deduplication Audit:** Comprehensive grep across all existing `.md` records in `alpha-strategy-research` confirmed zero prior records citing SSRN 6188418, Stoikov "Pairs Trading in Crypto", or the Hummingbot-sponsored correlation clustering pairs framework. Existing pairs trading records (Kalman cointegration, copula CMI, DTW/OCP clustering, and other approaches) address fundamentally different methodologies.

## Economic mechanism

### Source-reported

The authors develop a multi-stage selection framework for cryptocurrency pairs trading that identifies stable relative-value relationships across assets and executes mean-reversion strategies in real time. The framework combines:

1. **Correlation clustering** to group assets with co-moving price behavior.
2. **Structural metadata** filtering to exclude pairs with structural differences (e.g., different sector, utility, or market microstructure).
3. **Stability diagnostics** to isolate pairs exhibiting persistent relative-value behavior rather than transient correlation.

The hypothesis is that a disciplined multi-stage funnel improves signal quality and stability across regimes relative to naive pairs selection, and that the resulting market-neutral strategy produces consistent returns while revealing challenges around liquidity, convergence reliability, and execution costs.

### Research interpretation

The falsifiable alpha hypothesis is that **a correlation-clustering plus structural-metadata plus stability-diagnostics selection pipeline identifies crypto perpetual pairs with sufficiently stable mean-reverting spread dynamics to generate positive risk-adjusted returns net of realistic execution costs, funding, and slippage**. This is a relative-value / mean-reversion mechanism: when two structurally similar crypto assets diverge beyond their historical norm, the spread is expected to revert, and the strategy profits from convergence. The multi-stage selection is the hypothesized edge-enhancement mechanism — filtering out structurally dissimilar or unstable pairs that would produce false signals.

## Signal

### Source-reported

- **Formation timestamp:** Hourly data resolution. The authors use 2 years of hourly data for 500+ coins (`source-reported`).
- **Lookback window:** Not specified in the abstract; the full paper's methodology section is not accessible (`data gap`).
- **Entry:** Multi-stage funnel: (1) correlation clustering identifies candidate pairs, (2) structural metadata filters out dissimilar pairs, (3) stability diagnostics isolate pairs with persistent relative-value behavior. Entry thresholds, holding rules, and risk controls were fine-tuned through backtesting before live deployment (`source-reported`). Exact entry threshold (e.g., z-score, standard deviation band) is not specified in the abstract (`data gap`).
- **Exit:** Mean-reversion exit when spread converges to historical norm. Risk controls and holding rules are fine-tuned (`source-reported`). Exact exit rules not specified in the abstract (`data gap`).
- **Holding period:** Not specified in the abstract (`data gap`).
- **Parameters:** The full parameter set (correlation window, clustering threshold, metadata filters, stability diagnostic thresholds, entry/exit z-scores, holding limits, stop-loss) is described as "fine-tuned" but not enumerated in the abstract (`data gap`).
- **Execution platform:** Hummingbot open-source market-making and trading bot. The strategy was deployed on Hummingbot for both backtesting and live trading (`source-reported`).
- **Re-entry rules:** Not specified in the abstract (`data gap`).
- **Position-sizing logic:** Not specified in the abstract (`data gap`).

**Underspecified items:** The paper's full methodology, parameter values, and exact signal construction are not accessible from the abstract alone. An independent researcher cannot fully reconstruct the strategy from available public information.

## Required data

- **Instrument / universe:** 500+ cryptocurrency perpetual futures contracts (`source-reported`). Exact universe construction rules not specified in the abstract (`data gap`).
- **Venue:** Not specified in the abstract; Hummingbot supports multiple exchanges (Binance, KuCoin, Gate.io, etc.) (`data gap`).
- **Market type:** Perpetual futures (based on Hummingbot integration and perpetuals being the dominant crypto derivatives instrument) (`source-reported`).
- **Timeframe:** Hourly bars (`source-reported`).
- **Fields:** OHLCV (implied by hourly data and correlation-based analysis). Funding rates, open interest, and order book data requirements not specified (`data gap`).
- **Point-in-time:** 2 years of hourly data through the paper's writing date (December 2025) (`source-reported`).
- **Timestamp requirements:** Hourly resolution, timezone not specified (`data gap`).
- **Missing-data assumptions:** Not specified in the abstract (`data gap`).

## Execution assumptions

- **Signal-to-order timing:** Hourly signal formation; exact order timing relative to signal not specified (`data gap`).
- **Next-bar vs same-bar execution:** Not specified (`data gap`).
- **Market / limit order:** Not specified; Hummingbot primarily uses limit orders for market making (`data gap`).
- **Fill model:** Not specified in the abstract (`data gap`).
- **Fees:** Execution costs are described as a challenge but not quantified in the abstract (`data gap`).
- **Spread:** Not specified (`data gap`).
- **Slippage:** Described as a challenge for convergence reliability (`source-reported`); not quantified (`data gap`).
- **Impact / capacity:** Not specified in the abstract. The authors note liquidity as a key challenge (`source-reported`).
- **Funding:** Perpetual futures funding rates are a material holding cost for mean-reversion pairs positions. The paper acknowledges execution costs and convergence reliability as challenges (`source-reported`). Funding cost modeling details not accessible (`data gap`).
- **Leverage / margin:** Not specified in the abstract (`data gap`).
- **Latency:** Not specified (`data gap`).
- **Partial fills / failures:** Not specified (`data gap`).

## Evidence

### Source-reported

- **Backtest performance:** The authors report "consistent market-neutral returns" through extensive backtesting and live trading on selected pairs (`source-reported`, abstract). No specific Sharpe ratio, CAGR, maximum drawdown, win rate, or other quantitative performance metric is provided in the abstract or publicly accessible summaries (`data gap` for all specific performance numbers).
- **Live trading:** The strategy was deployed on Hummingbot for live trading on selected pairs (`source-reported`). No live performance figures are provided in the abstract (`data gap`).
- **Sample period:** 2 years of hourly data for backtesting; live trading dates not specified (`data gap`).
- **Cost treatment:** The authors acknowledge execution costs, liquidity challenges, and convergence reliability as material issues (`source-reported`). Whether "consistent market-neutral returns" are net or gross of costs is not stated in the abstract (`data gap`).

### Independently reproduced

`Not independently reproduced.` All metrics reported are source-reported from Stoikov et al. (SSRN 6188418). No internal simulation in PyBroker, NautilusTrader, or Hummingbot has been conducted.

### Negative evidence

- The authors themselves acknowledge "important challenges related to liquidity, convergence reliability, and execution costs" (`source-reported`, abstract). This suggests the strategy faces material real-world frictions.
- Existing repository evidence documents that many pairs trading approaches fail on crypto perpetuals after realistic costs: `crypto-perpetual-pairs-trading-kalman-cointegration-falsification-2026-09-11.md` (Kalman cointegration failed), `copula-cmi-crypto-perpetual-pairs-trading-market-overlay-2026-09-07.md` (copula CMI negative net returns), and `crypto-spot-perpetual-dynamic-collateral-control-impulse-band-2026-09-02.md` (basis trading challenges).
- The Mykola-Quant retail crypto alpha negative-results study (`retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11.md`) found no tradeable signal edge for retail-accessible microstructure signals after realistic costs on crypto, suggesting the broader signal landscape is cost-dominated.

## Falsification plan

To falsify the correlation-clustered crypto pairs trading hypothesis:

1. **Out-of-sample walk-forward test:** Run the multi-stage selection pipeline on a rolling 6-month training / 1-month test window across 2023–2026 data. If the out-of-sample Sharpe ratio is below 0.3 or the strategy loses money in 3+ consecutive test windows, reject the hypothesis (`research-defined falsification threshold`).
2. **Cost sensitivity stress test:** Re-run with round-trip costs of 0.10%, 0.20%, and 0.30% (covering Binance taker fees plus varying slippage). If the strategy becomes unprofitable below 0.20% round-trip cost, the edge is fragile (`research-defined falsification threshold`).
3. **Liquidity filter ablation:** Remove the structural metadata and stability diagnostic filters, running only raw correlation clustering. If the unfiltered version loses money while the filtered version profits, the selection funnel is the edge — not the mean-reversion itself. If both lose money, the mechanism is fragile (`research-proposed`).
4. **Funding rate cost injection:** Model 8-hour perpetual funding payments explicitly. If the strategy is consistently short high-funding-rate assets (which is the typical pairs trade direction), net-of-funding returns may be substantially worse than reported. Falsification threshold: if net-of-funding Sharpe drops below 0.2, reject (`research-defined falsification threshold`).
5. **Survivorship and data snooping audit:** Verify that the 500+ coin universe was fixed at the start of the sample, not backfilled with coins that only later became liquid. If survivorship bias is present, reject (`research-proposed`).

## Crypto portability

`direct` — the strategy is natively designed for cryptocurrency perpetual futures markets and was deployed live on Hummingbot.

Crypto-specific considerations:
- **Perpetual funding:** Mean-reversion pairs positions can bleed if the spread component held long has persistently high funding (longs pay) and the short leg has low/negative funding. The paper acknowledges this implicitly via the "execution costs" challenge (`source-reported`).
- **Liquidity fragmentation:** Different crypto perpetuals have vastly different order-book depth. The 500+ coin universe likely includes many illiquid contracts where slippage dominates (`research-proposed`).
- **24/7 session structure:** Pairs signals can trigger at any hour; convergence may take longer during low-liquidity periods (weekends, Asian session) (`research-proposed`).
- **Venue fragmentation:** Crypto perpetuals trade on dozens of venues; the Hummingbot integration supports multiple exchanges, but cross-venue execution adds complexity (`source-reported`).

## Limitations

- **Data gap on performance numbers:** The abstract and publicly accessible summaries do not provide specific Sharpe ratio, CAGR, maximum drawdown, win rate, or other quantitative metrics. All performance claims are qualitative ("consistent market-neutral returns").
- **Data gap on methodology details:** Exact signal construction, entry/exit thresholds, parameter values, holding rules, and risk controls are not accessible from the abstract alone. Full reconstruction requires the complete 36-page paper.
- **Data gap on cost treatment:** Whether reported returns are net or gross of transaction costs, funding, and slippage is not stated in the abstract.
- **Data gap on live trading performance:** No live trading performance figures are provided.
- **Not independently reproduced.** The strategy has not been tested in our research stack.
- **Source quality:** SSRN working paper, not peer-reviewed. Cornell affiliation (Sasha Stoikov) provides credibility but does not substitute for peer review.
- **Execution platform dependency:** The strategy depends on Hummingbot, which has its own execution characteristics (latency, fill rates, order management) that may differ from production trading systems.

## Implementation status

`not-implemented`. No implementation in our research stack (PyBroker, NautilusTrader, Hummingbot, or any other execution engine) has been completed. The source paper describes deployment on Hummingbot, but this is the source's own execution, not ours.

## Adoption boundary

This record is research material only. Its presence in this repository does **not** mean:
- Profitable
- Validated alpha
- Approved for implementation
- Approved for paper trading
- Approved for testnet
- Approved for live trading

## Related Wiki records

- `[[crypto-perpetual-pairs-trading-kalman-cointegration-falsification-2026-09-11]]` — Kalman-filter cointegration pairs trading on crypto perpetuals (negative result). Different methodology (Engle-Granger + Kalman vs. correlation clustering + structural metadata).
- `[[copula-cmi-crypto-perpetual-pairs-trading-market-overlay-2026-09-07]]` — Copula CMI pairs trading on crypto perpetuals (negative net result). Different methodology (copula vs. correlation clustering).
- `[[crypto-spot-perpetual-dynamic-collateral-control-impulse-band-2026-09-02]]` — Spot-perpetual basis trading with dynamic collateral control. Related carry/relative-value mechanism but different trade structure.
- `[[crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11]]` — Cross-sectional funding-rate carry factor (positive OOS edge). Related in that both exploit relative-value across crypto perpetuals, but different signal (funding cross-section vs. price pairs).
- `[[dtw-ocp-clustering-pairs-trading-regime-falsification-2026-09-13]]` — DTW/OCP clustering pairs trading (equities). Different asset class and clustering methodology.

## Sources

1. Sasha Stoikov, Dora Xu, Shijie Shao, Yourui Wang, Tongshu Zhang, Jinxuan Hu, and Federico Cardoso, "Pairs Trading in Crypto", Cornell University / Hummingbot, SSRN working paper 6188418, posted February 25, 2026 (written December 12, 2025). DOI: https://dx.doi.org/10.2139/ssrn.6188418. URL: https://ssrn.com/abstract=6188418.
