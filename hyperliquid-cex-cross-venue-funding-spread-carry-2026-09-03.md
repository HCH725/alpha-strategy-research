---
schema: strategy-research-record-v1
title: "Hyperliquid-CEX Cross-Venue Perpetual Funding Spread Carry"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - funding
  - relative-value
  - cross-venue
  - market-neutral
status: research-only
confidence: medium
source_as_of: 2026-07-17
sources:
  - "Tony Lau (2026), 'The Funding Carry and a Cross-Venue Spread on Perpetual Futures: A Significance-Tested Study of Hyperliquid and Centralized Venues', SSRN 6993978, posted 17 July 2026. https://ssrn.com/abstract=6993978"
  - "Lau, Tony (2026), replication package, Zenodo v1, DOI 10.5281/zenodo.20938723, published 26 June 2026. https://doi.org/10.5281/zenodo.20938723"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Hyperliquid-CEX Cross-Venue Perpetual Funding Spread Carry

## Provenance

Primary paper: Tony Lau, **"The Funding Carry and a Cross-Venue Spread on Perpetual Futures: A Significance-Tested Study of Hyperliquid and Centralized Venues"**, SSRN `6993978`, posted 17 July 2026, date written 25 June 2026.

Primary reproducibility artifact: Zenodo replication package v1, DOI `10.5281/zenodo.20938723`, published 26 June 2026. The package contains the manuscript, cached hourly public inputs, analysis scripts, and frozen outputs. Relevant paths inside the package include `analysis/cross_venue.py`, `analysis/realistic_cross_venue.py`, `results/realistic_cross_venue.out.txt`, and `papers/cross_venue_carry.tex`. The archived ZIP is `projectresearch_replication_v1.0.zip` with Zenodo-displayed MD5 `349a2ffd5922859338a3ba59fbcb40df`.

The source studies BTC, ETH, SOL, and DOGE for the cross-venue leg using Hyperliquid and Binance full-history funding data from roughly mid-2023 to mid-2026; the paper also checks Bybit over a comparable full-history span and shorter recent histories from OKX and Bitget.

Repository and Wiki Brain source-identity searches before writing found no record matching SSRN `6993978`, Zenodo DOI `10.5281/zenodo.20938723`, the exact paper title, or the distinctive static `short Hyperliquid perpetual + long CEX perpetual on the same coin` funding-spread construction. Existing funding-aware market-making and single-venue funding records are materially different mechanisms.

## Economic mechanism

### Source-reported

The source reports that Hyperliquid realized funding has been persistently higher than major centralized venues on the same assets despite broadly similar funding formulas and interest anchors. The paper attributes the differential to a higher realized Hyperliquid perpetual premium, consistent with stronger net long-side demand on the DEX and limits to arbitrage.

The proposed trade is cross-venue and delta-neutral in first-order price exposure: short the higher-funding Hyperliquid perpetual and long the lower-funding centralized-exchange perpetual on the same underlying coin. The position receives Hyperliquid funding and pays CEX funding, collecting the difference while bearing cross-venue basis, liquidation, venue, margin-fragmentation, and execution risks.

The source emphasizes that the premium should not be interpreted as a free lunch. Margin cannot be netted across venues, Hyperliquid-specific operational/oracle/withdrawal risks remain, and the funding differential is time-varying.

### Research interpretation

The falsifiable alpha hypothesis is a **persistent cross-venue limits-to-arbitrage funding premium**: when two perpetual contracts reference the same crypto asset but one venue carries structurally stronger long-side demand, the higher-funding venue may compensate short-side capital enough to create a positive market-neutral carry after basis and execution costs.

The strongest source-backed version is the **static carry**, not an adaptive sign-timing strategy. The source reports that a dynamic variant that flips direction based on recent spread signs is materially more cost-sensitive and can become negative after realistic turnover.

## Signal

**Status:** the core static construction is source-specified; some live execution details remain `underspecified`.

### Source-reported construction

- **Universe:** BTC, ETH, SOL, DOGE in the headline cross-venue tests.
- **Venues:** short Hyperliquid perpetual; long Binance perpetual on the same coin. Bybit is used as an independent CEX robustness venue; OKX and Bitget have shorter source histories.
- **Direction:** always short the Hyperliquid perpetual and long the lower-funding CEX perpetual for the same underlying in the static baseline.
- **Notional:** equal underlying notional per leg so first-order directional exposure is approximately neutral.
- **Funding signal:** daily Hyperliquid funding is the sum of 24 hourly rates; Binance funding is the sum of 8-hour settlement rates. The collected daily spread is `HL funding - CEX funding`.
- **Basis accounting:** the realistic construction adds daily mark-to-market P&L from changes in the cross-venue perpetual premium/basis: for short-HL/long-CEX, `basis_pnl = -Δ(HL premium - CEX premium)`.
- **Net daily P&L on notional:** `funding_spread + basis_pnl`, before the source's capital/leverage accounting.
- **Holding rule:** static/continuous hold is the preferred source-reported construction; the paper states that the trade is best held statically because the spread is persistently positive and turnover is costly.
- **Exit:** source does not specify a predictive exit threshold for the static trade. Closing at the end of the evaluation horizon is implicit in the backtest. A live de-risking/exit rule is therefore `underspecified`.
- **Leverage:** source analyzes approximately 2x, 3x, 5x, and 8x per-leg leverage for return-on-capital/liquidation sensitivity and describes 2–3x as prudent. This is source-reported risk/capital analysis, not an alpha threshold.

### Source-reported rejected variant

`analysis/cross_venue.py` also tests a dynamic position equal to the sign of the trailing 7-day mean funding spread, shifted one day to avoid look-ahead. The source reports that this higher-turnover variant deteriorates sharply with transaction costs and is not the preferred edge.

### Research-proposed live test convention

For future validation only, not as a source claim:

- Rebalance notionals once daily at a fixed UTC time to restore approximate delta neutrality if leg notionals drift materially.
- Do not change trade direction based on same-day funding unless a separately predeclared branch is tested.
- Any live spread-entry threshold, minimum expected carry, funding-persistence filter, stop, emergency unwind rule, or venue-risk veto must be labeled `research-proposed`; none is specified as the core alpha rule by the source.

## Required data

- **Instruments:** same-underlying USDC/USDT-margined perpetual futures on Hyperliquid and one or more CEXs; exact contract specifications and quote/settlement currencies must be normalized before comparison.
- **Universe:** source headline set BTC, ETH, SOL, DOGE; any larger universe requires point-in-time listing/liquidity rules.
- **Venues:** Hyperliquid plus Binance for the primary test; Bybit as a robustness venue; optional recent-history OKX/Bitget checks.
- **Timeframe:** hourly raw funding/premium inputs aggregated to UTC day for the source's main spread analysis.
- **Fields:** realized funding rate and settlement timestamps on both venues; Hyperliquid premium; CEX premium index or equivalent; underlying/perpetual prices for basis and liquidation analysis; high/open prices for intraday liquidation stress.
- **Point-in-time:** only funding and premium values known by the decision timestamp may be used. Backtests must not use end-of-day totals to make same-day decisions.
- **Timestamp:** UTC with exact venue settlement conventions; Hyperliquid hourly versus Binance/Bybit typically 8-hour funding must be aligned by realized cash-flow time, not nominal label.
- **Missing data:** no silent imputation. Missing venue funding, premium, or price observations should make that asset-day ineligible under a predeclared rule.
- **Costs:** fees, spread/slippage, basis mark-to-market, withdrawal/transfer or rebalancing frictions where applicable, and venue-specific funding cash flows.
- **Margin/liquidation:** per-venue initial/maintenance margin rules and liquidation engine behavior are required for leverage tests because cross-venue positions cannot rely on unified margin.

## Execution assumptions

### Source-reported

- Core trade uses two perpetual legs on the same coin across separate venues.
- The realistic analysis books cross-venue basis mark-to-market rather than treating the funding spread as riskless.
- The source applies transaction-cost sensitivity and models capital as margin required on both venues.
- The paper states that static holding minimizes turnover; dynamic weekly-like flipping becomes unattractive at higher round-trip costs.
- The source's liquidation analysis treats each venue leg as separately margined and therefore vulnerable to directional coin moves even when portfolio delta is approximately neutral across venues.

### Underspecified / research-proposed

- Exact live order type, passive/aggressive execution choice, latency, participation cap, partial-fill handling, API failure handling, and synchronized two-leg execution are `underspecified` by the paper.
- A future implementation should use atomic-or-near-atomic legging controls and reject one-sided fills beyond a predeclared exposure duration. This is `research-proposed`.
- Any transfer/rebalancing between venues must include withdrawal delays, chain congestion, stablecoin settlement risk, and venue downtime; these are not fully modeled in the source backtest.

## Evidence

### Source-reported

For the source's approximately three-year Hyperliquid/Binance sample, the manuscript and frozen replication output report:

- ETH funding spread APR about **7.08%**, realistic net APR about **7.07%**, NET Sharpe **9.00**, NET max drawdown **-1.15%**.
- BTC funding spread APR about **7.15%**, realistic net APR about **7.13%**, NET Sharpe **8.87**, NET max drawdown **-1.89%**.
- SOL funding spread APR about **7.50%**, realistic net APR about **7.49%**, NET Sharpe **6.47**, NET max drawdown **-3.63%**.
- DOGE funding spread APR about **9.27%**, realistic net APR about **9.27%**, NET Sharpe **5.49**, NET max drawdown **-11.28%**.
- The paper reports the Hyperliquid-minus-Binance funding differential as positive on roughly 70–80% of days, with Newey-West HAC t-statistics roughly **4–8** and 4–5 of 5 walk-forward folds positive depending on asset/test.
- Against Bybit, the source reports a comparable full-history structural Hyperliquid premium of roughly 6–8% annualized; shorter recent OKX/Bitget histories show smaller spreads in the compressed 2026 regime.
- The paper reports that the spread peaked around 2024 and had fallen to roughly 2% by the 2025–26 walk-forward fold, remaining positive but materially smaller than the full-sample average.
- In the source's ETH+BTC capital analysis, approximately 2x and 3x per-leg leverage map to roughly **7.1%** and **10.65%** annual return on deployed capital under its simplified liquidation/capital model.

These are third-party/source-reported results from the author's reproducibility package. They are not evidence that this repository has independently validated the strategy.

### Independently reproduced

not independently reproduced

### Negative evidence

- The source reports substantial time variation: the cross-venue spread was much larger in 2024 and had compressed materially by 2026.
- The dynamic trailing-7-day sign variant is cost-sensitive; the source's cost table shows a weekly-flip approximation becoming negative beyond roughly 20 bp round-trip.
- DOGE has materially worse drawdown/tail behavior than BTC/ETH in the source's realistic results.
- Cross-venue delta neutrality does not remove liquidation risk because each leg is margined independently.
- Venue, oracle, withdrawal, smart-contract, bridge, stablecoin, and operational risks are not captured by ordinary return volatility and may dominate historical Sharpe metrics.
- The sample spans only roughly one post-FTX market cycle, limiting inference about long-run structural persistence.
- The source itself warns that very high historical Sharpe estimates are partly a low-volatility carry illusion that may understate catastrophic tails.

## Falsification plan

1. **Strict forward OOS:** test a later sample not used in the source. Metric: net daily cross-venue P&L after realized funding, observed basis changes, fees, and slippage. **research-defined falsification threshold:** reject the core carry hypothesis if the predeclared BTC/ETH basket has net APR <= 0 over the OOS horizon.
2. **Spread persistence:** measure the fraction of days with `HL funding - CEX funding > 0`. **research-defined falsification threshold:** materially weaken the structural-premium interpretation if the OOS fraction is <= 50% and the mean spread is not significantly positive under HAC inference.
3. **Venue replication:** repeat Hyperliquid-vs-Binance and Hyperliquid-vs-Bybit with identical methodology. **research-defined falsification threshold:** reject a venue-general structural interpretation if only one CEX comparison remains positive while the other is non-positive after costs.
4. **Basis-risk audit:** include observed cross-venue basis mark-to-market at the actual rebalance frequency. Reject the tradeability claim if basis losses plus costs erase funding carry.
5. **Cost stress:** predeclare round-trip cost grid and synchronized-leg slippage. **research-defined falsification threshold:** fail practical alpha if a conservative executable-cost assumption drives expected net carry <= 0.
6. **Leverage/liquidation stress:** replay intraday wicks under venue-specific maintenance-margin rules. Do not accept a leverage recommendation if historical liquidation frequency or expected liquidation loss overwhelms incremental return on capital.
7. **Funding-regime breakdown:** split bull/bear and high-/low-leverage-demand regimes using ex-ante rules. If profitability is confined to one historical regime, reject claims of unconditional persistence.
8. **Dynamic-variant negative control:** reproduce the source's trailing-7-day sign flip as a negative control. It should not be substituted for the static baseline after seeing results.
9. **Competing explanation:** test whether the observed spread is fully explained by persistent cross-venue basis/premium differences, funding formula/cap asymmetries, stablecoin financing, or stale/availability mismatches. If so, reinterpret the edge as compensation for those risks rather than independent alpha.
10. **Operational tail scenario:** simulate one-venue halt, withdrawal freeze, oracle dislocation, or forced liquidation while the opposite hedge remains open. If required capital buffers make risk-adjusted net return unattractive, reject implementability despite positive historical carry.

## Crypto portability

**direct.** The source is explicitly about crypto perpetual futures and the trade itself is cross-venue crypto relative value.

Portability is nevertheless venue-specific rather than universal. Funding formulas, caps, settlement frequency, margin assets, liquidation engines, index/oracle construction, maker/taker fees, withdrawal mechanics, and stablecoin collateral differ across venues. A spread observed on Hyperliquid versus Binance/Bybit should not be assumed to exist on other DEX/CEX pairs without direct measurement.

The 24/7 market requires precise UTC settlement alignment, and cross-venue capital fragmentation is a first-order implementation constraint rather than a minor operational detail.

## Limitations

- `not independently reproduced`
- `underspecified`: exact live entry threshold, exit/de-risking rule, order type, leg synchronization, and failure-handling logic are not fully specified by the source.
- `data gap`: no independent verification in this Scout cycle of the author's cached raw venue data against exchange APIs.
- `data gap`: venue outage, withdrawal, oracle, bridge, smart-contract, stablecoin depeg, and legal/custody risks are not adequately represented by historical Sharpe or max drawdown.
- Historical edge magnitude is demonstrably time-varying and materially lower in 2026 than in 2024.
- Cross-venue basis is small on average in the source but can become discontinuous during stress.
- Separate margin pools mean portfolio delta neutrality does not imply liquidation neutrality.
- The author's replication package discloses AI-assisted code implementation under author review; this is a source-quality consideration, not evidence of error.

## Implementation status

Not implemented. This Scout cycle did not modify PyBroker, Nautilus, the strategy-family registry, data pipelines, Kanban, Paper, Testnet, Live, credentials, or execution authorization.

## Adoption boundary

This record is research material only. It does not establish validated alpha, profitability, implementation approval, leverage approval, paper/testnet/live approval, or authorization to move capital across venues. Any `research-proposed` operational choices exist only to make future validation explicit and falsifiable.

## Related Wiki records

- [[quant/funding-aware-market-making-perpetual-dex-2026-08-31]] — related use of perpetual funding, but a market-making/inventory-control mechanism rather than cross-venue carry.

No canonical Wiki record with the same SSRN/Zenodo identity or materially identical static short-Hyperliquid/long-CEX funding-spread rule was found during the pre-write search.

## Sources

1. Lau, T. (2026). "The Funding Carry and a Cross-Venue Spread on Perpetual Futures: A Significance-Tested Study of Hyperliquid and Centralized Venues." SSRN 6993978. Posted 17 July 2026. https://ssrn.com/abstract=6993978
2. Lau, T. (2026). Replication package for the paper above. Zenodo v1. DOI: https://doi.org/10.5281/zenodo.20938723. Published 26 June 2026. Relevant archived paths: `analysis/cross_venue.py`, `analysis/realistic_cross_venue.py`, `results/realistic_cross_venue.out.txt`, `papers/cross_venue_carry.tex`.
