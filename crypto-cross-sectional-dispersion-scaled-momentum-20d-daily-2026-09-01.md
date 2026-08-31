---
schema: strategy-research-record-v1
title: Crypto Cross-Sectional Dispersion-Scaled 20-Day Momentum
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - momentum
  - dispersion
  - regime-filter
status: research-only
confidence: medium
source_as_of: 2026-04-27
sources:
  - "https://ssrn.com/abstract=6648082"
  - "https://doi.org/10.2139/ssrn.6648082"
  - "https://www.quantconnect.com/terminal/cache/embedded_backtest_c423206646f74c75097459ef437d9b67.html"
  - "https://doi.org/10.1007/s11408-025-00474-9"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Related peer-reviewed evidence finds cryptocurrency momentum and volatility-managed momentum can be unstable or unattractive, so dispersion scaling should not be assumed to establish robust profitability."
---

# Crypto Cross-Sectional Dispersion-Scaled 20-Day Momentum

## Provenance

Primary research source: Cong Zhang and Olorato MacDonald Makgolo, *Cross-Sectional Dispersion and the State Dependence of Cryptocurrency Momentum*, SSRN working paper 6648082, posted 2026-04-25 and last revised 2026-04-27. Stable references: https://ssrn.com/abstract=6648082 and DOI https://doi.org/10.2139/ssrn.6648082.

The primary paper studies a dynamic, survivorship-aware cryptocurrency universe reconstructed from the contemporaneous CoinGecko top 500 with rolling eligibility screens. Its public abstract states that lagged cross-sectional dispersion predicts weaker subsequent momentum after controlling for Bitcoin realized volatility and average cross-asset correlation, with the effect concentrated in the upper tail of dispersion.

A public QuantConnect embedded implementation linked to the same strategy family is used only to preserve a concrete reconstruction of the signal and overlay. It is a third-party implementation, not the primary paper and not an independent reproduction by ChatGPT. It specifies a 20-day cumulative-log-return momentum signal, cross-sectional demeaning and unit-gross normalization, a dispersion scaling ratio relative to an expanding historical median, smoothing, and a one-day lag. Exact equivalence between every implementation detail and the authors' final research code is **unproven**.

Primary-paper data end date is **underspecified in the publicly accessible abstract reviewed in this cycle**. Do not infer it from publication date.

## Economic mechanism

### Source-reported

Zhang and Makgolo report that cryptocurrency cross-sectional momentum is state dependent. Their central result is that lagged cross-sectional dispersion, rather than generic Bitcoin volatility, is most closely associated with subsequent momentum breakdown. The relation is nonlinear and concentrated when dispersion enters its upper tail. They interpret high dispersion as a state in which cross-sectional rankings become less reliable.

The paper reports that dispersion-based exposure scaling improves full-sample drawdown and certainty-equivalent outcomes, while Bitcoin-volatility scaling performs better in post-2020 long-only implementation exercises. This distinction is important: dispersion is not reported as universally superior under every objective or subperiod.

### Research interpretation

The falsifiable hypothesis is that unusually wide disagreement in same-day returns across eligible cryptocurrencies contains information about the reliability of a recent-return ranking. When cross-sectional dispersion is high relative to its own historical distribution, recent winners and losers may increasingly reflect idiosyncratic jumps, fragmented narratives, liquidation events, or transient price dislocations rather than a common persistent trend process. Reducing gross momentum exposure in those states may improve the tail behavior of a momentum portfolio without changing the underlying ranking rule.

This is a **state-dependent exposure overlay**, not a new source of standalone directional alpha. The 20-day momentum score determines relative long/short direction; dispersion changes how much gross exposure is assigned to that score.

## Signal

The following reconstruction combines the primary paper's public description with the public QuantConnect implementation. Where the accessible primary source does not expose the exact detail, the implementation-derived item is identified as such.

1. **Universe:** begin from a broad CoinGecko top-500-derived candidate set and apply point-in-time eligibility screens. The public implementation comments describe minimum age of 90 days, market capitalization of USD 1 billion, 24-hour volume of USD 25 million, return-quality checks, and stablecoin exclusion. Exact primary-paper production filters should be checked against the full paper/code before claiming exact replication.
2. **Momentum formation:** for eligible asset `i`, compute a 20-day cumulative log-return score using only returns available through `t-1`:

   `S_raw(i,t) = sum_{k=1..20} r(i,t-k)`.

3. **Cross-sectional normalization:** demean scores and scale to unit gross exposure:

   `W0(i,t) = (S_raw(i,t) - mean_j(S_raw(j,t))) / sum_j |S_raw(j,t) - mean_j(S_raw(j,t))|`.

   Positive weights are relative winners; negative weights are relative losers.
4. **Dispersion state:** compute daily cross-sectional dispersion `D(t-1)` across eligible-asset returns using only information through `t-1`. The public implementation uses the cross-sectional standard deviation of the latest daily return.
5. **Historical target:** compute an expanding historical median `D*(t-1)` of dispersion available through `t-1`.
6. **Raw exposure multiplier:** the public implementation documents:

   `g_disp(t) = min(1, max(0.10, D*(t-1) / D(t-1)))`.

   Thus exposure is unchanged when current dispersion is at or below the historical target and is progressively reduced when dispersion rises above it, subject to a 10% floor.
7. **Smoothing:** apply the public implementation's recursive filter with `lambda = 0.80`:

   `g_smooth(t) = 0.80 * g_smooth(t-1) + 0.20 * g_disp(t)`.

8. **Target weight:**

   `W(i,t) = g_smooth(t) * W0(i,t)`.

9. **Timing:** fix signals and state variables using information through `t-1`; rebalance daily for the subsequent return interval. Same-close execution is not justified by the source reconstruction and should not be assumed.

**Specification status:** research-reconstructable but not canonical-production-ready. The broad economic rule is source-backed; exact universe history, return-quality screen, treatment of missing constituents, primary-paper dispersion definition, and exact order timestamp remain **underspecified / unproven** until checked against the complete research appendix or authors' code.

## Required data

- Point-in-time cryptocurrency universe membership, ideally contemporaneous CoinGecko top-500 history.
- Point-in-time market capitalization and trading-volume fields for eligibility screens.
- Asset age / first-observation date.
- Daily close prices with a consistent timezone and candle boundary.
- Stablecoin classification available point in time.
- At least 20 prior daily returns per eligible asset for momentum formation.
- Expanding history of cross-sectional daily dispersion.
- Delisting and missing-price handling that does not backfill future survivorship information.

Venue-specific implementation requires mapping the research universe into actually tradable spot or perpetual instruments without using future listings.

## Execution assumptions

The primary research abstract does not provide a complete executable fill model.

The public QuantConnect implementation rebalances daily and uses Binance margin-market assumptions, but this should be treated as an implementation example rather than evidence that the paper's economic results survive a specific production execution model.

Material assumptions that remain **underspecified** for adoption include:

- precise signal cutoff and order timestamp;
- next-bar open versus later execution window;
- maker/taker mix;
- bid-ask spread and slippage;
- market impact and capacity;
- borrow availability for shorts or perpetual-contract substitution;
- funding when perps are used;
- delisting/liquidation handling;
- partial fills and venue failures.

Any backtest must lag both universe fields and dispersion inputs to their real historical availability.

## Evidence

### Source-reported

The primary SSRN paper reports that lagged cross-sectional dispersion predicts weaker subsequent cryptocurrency momentum even after controlling for Bitcoin realized volatility and average correlation, that the effect is nonlinear and concentrated in high-dispersion states, and that dispersion-based scaling improves full-sample drawdown and certainty-equivalent outcomes.

The same abstract also reports an important qualification: Bitcoin-volatility scaling performs better in post-2020 long-only implementation exercises. Therefore, the evidence supports state dependence, not a universal claim that dispersion scaling dominates every alternative risk overlay.

A public QuantConnect implementation of the paper's strategy family encodes a concrete 20-day cross-sectional momentum signal and a dispersion multiplier based on the expanding historical median, with a 10% exposure floor and 0.80 recursive smoothing. These are implementation-reported details, not ChatGPT-verified paper equations.

### Independently reproduced

Not independently reproduced.

### Negative evidence

Grobys, Kolari, Sandretto et al., *Cryptocurrency momentum has (not) its moments*, *Financial Markets and Portfolio Management* 39 (2025), DOI 10.1007/s11408-025-00474-9, documents that cryptocurrency momentum and volatility-managed variants can exhibit unattractive drawdowns and do not consistently outperform the market. This is not a direct replication of Zhang-Makgolo dispersion scaling, but it is relevant contrary evidence against assuming that a risk-managed momentum overlay is inherently robust.

The Zhang-Makgolo abstract itself provides internal qualification because BTC-volatility scaling outperforms dispersion scaling in some post-2020 long-only exercises.

## Falsification plan

1. Reconstruct a point-in-time, survivorship-aware universe with no future listing, market-cap, volume, or delisting information.
2. Establish a plain 20-day cross-sectional momentum baseline with identical universe and execution assumptions.
3. Compare at minimum: no scaling, dispersion scaling, BTC realized-volatility scaling, and a placebo scaler constructed from shuffled or lag-misaligned dispersion.
4. Perform an ablation on the dispersion overlay: no smoothing, alternative smoothing values, no 10% floor, and fixed historical quantile/median regimes.
5. Test whether high lagged dispersion predicts weaker next-period momentum returns after controlling for BTC realized volatility and average cross-asset correlation.
6. Require the sign of the state-dependence relation to persist out of sample and across materially different market regimes. Failure to reproduce the negative dispersion-by-momentum interaction materially weakens the thesis.
7. Compare net-of-cost Sharpe, certainty-equivalent return, maximum drawdown, turnover, and tail loss against the unscaled baseline. If improvements disappear under realistic fees, spread, funding/borrow, and slippage, reject the economic value of the overlay even if the statistical interaction survives.
8. Test post-publication data separately. The paper/version date must not be treated as a substitute for a genuinely untouched OOS period.

## Crypto portability

**direct** for the research mechanism because the primary source studies cryptocurrency momentum directly.

Production portability remains venue-dependent. CoinGecko cross-sectional constituents do not map one-for-one to Binance spot or perpetual markets. Short availability, funding, listing dates, quote-currency changes, 24/7 UTC boundaries, stale prices, and exchange fragmentation can materially change both the momentum ranking and dispersion state.

## Limitations

- **not independently reproduced**.
- **working-paper risk:** SSRN version reviewed is a 2026 working paper rather than a peer-reviewed final publication.
- **data gap:** primary-paper sample end date was not established from the publicly accessible material reviewed in this cycle.
- **underspecified:** exact point-in-time universe reconstruction and return-quality filters require the full source appendix/code for canonical replication.
- **unproven:** the public QuantConnect implementation is useful for reconstructing the rule but is not proven identical to the authors' research code.
- Dispersion scaling may primarily be risk management rather than incremental alpha; its value should be judged against equal-turnover and equal-volatility baselines.
- Cross-sectional dispersion is sensitive to universe breadth. Small or changing eligible sets can mechanically alter the state variable.

## Implementation status

No implementation or validation in PyBroker, NautilusTrader, strategy registry, Paper, Testnet, or Live has been performed in this Scout cycle.

`implementation_status: not-implemented`

## Adoption boundary

This record is Alpha Strategy Pool research material only. Presence in this repository does not imply profitability, validated alpha, implementation approval, paper-trading approval, testnet approval, or live-trading approval.

`status: research-only`
`adoption: not-approved`
`approval_scope: research-only`

## Related Wiki records

No stable Hermes Wiki Brain link was verified in this Scout cycle. Do not fabricate one.

Repository-level related research families include cross-sectional momentum and volatility-managed momentum, but concept-level consolidation belongs to the separate Reviewer workflow.

## Sources

1. Cong Zhang and Olorato MacDonald Makgolo, *Cross-Sectional Dispersion and the State Dependence of Cryptocurrency Momentum*, SSRN working paper 6648082, posted 2026-04-25, revised 2026-04-27: https://ssrn.com/abstract=6648082 ; DOI: https://doi.org/10.2139/ssrn.6648082
2. Public QuantConnect embedded implementation / backtest associated with the strategy family, used for implementation-detail provenance only: https://www.quantconnect.com/terminal/cache/embedded_backtest_c423206646f74c75097459ef437d9b67.html
3. Klaus Grobys, John W. Kolari, Davide Sandretto, et al., *Cryptocurrency momentum has (not) its moments*, *Financial Markets and Portfolio Management* 39, 443-476 (2025), published 2025-03-27: https://doi.org/10.1007/s11408-025-00474-9
