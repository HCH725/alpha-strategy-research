---
schema: strategy-research-record-v1
title: CEX-DEX Cross-Venue Funding-Spread Carry
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - funding
  - perpetual-futures
  - relative-value
  - cross-venue
status: research-only
confidence: medium
source_as_of: 2026-08-19
sources:
  - "Pindza (2026), Centralized-decentralized exchange funding rate arbitrage as a basis trade: risk decomposition, stress testing, and portfolio construction under venue uncertainty, Digital Finance 8:48, DOI 10.1007/s42521-026-00213-3 - https://doi.org/10.1007/s42521-026-00213-3"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# CEX-DEX Cross-Venue Funding-Spread Carry

## Provenance

- **Primary source:** Edson Pindza, "Centralized-decentralized exchange funding rate arbitrage as a basis trade: risk decomposition, stress testing, and portfolio construction under venue uncertainty."
- **Publication:** *Digital Finance*, volume 8, article 48 (2026); published 2026-08-19; DOI: https://doi.org/10.1007/s42521-026-00213-3.
- **Primary empirical input:** Binance Futures BTCUSDT, ETHUSDT, and SOLUSDT funding rates from January 2021 through December 2024, aligned at eight-hour funding intervals.
- **DEX treatment:** the full-sample experiment uses synthetic DEX funding rates designed to represent oracle lag, persistent cross-venue spread, and higher DEX-rate noise. The paper explicitly labels this a controlled scenario analysis rather than a direct backtest of one DEX protocol.
- **Observed-protocol robustness check:** public dYdX v4 BTC-USD, ETH-USD, and SOL-USD hourly funding histories over the common October 2023 through December 2024 window, aggregated into eight-hour windows for alignment with Binance.
- **Public-use status:** the article is open access under CC BY 4.0. This record normalizes the strategy and cites the source rather than reproducing the article.

## Economic mechanism
### Source-reported

The source frames CEX-DEX funding-rate arbitrage as a crypto basis/carry trade rather than risk-free arbitrage. Funding rates differ across centralized and decentralized perpetual venues because trader populations, liquidity provision, oracle/index construction, protocol rules, and funding-calculation timing differ. An arbitrageur maintains offsetting equal-notional perpetual positions, receiving funding on the venue with the higher funding rate and paying funding on the venue with the lower rate. The resulting carry is exposed to funding-spread compression or inversion, imperfect hedging/basis moves, transaction costs, liquidation, counterparty risk, and DEX settlement/oracle/smart-contract risk.

### Research interpretation

The alpha hypothesis is **cross-venue structural funding dispersion**: fragmented perpetual markets can sustain a funding-rate differential long enough for a delta-neutral pair of positions to harvest net carry. The predictive object is not outright asset direction; it is the persistence of the funding spread between two venues for the same underlying.

This is materially distinct from a theoretical perpetual-price no-arbitrage-bound strategy. Here the primary signal is the **observable cross-venue funding differential**, while price basis, volatility, liquidity, leverage, and venue risk determine whether that apparent carry survives implementation.

The paper also suggests a regime-dependent mechanism: funding spreads are persistent within regimes but can compress, invert, or become more volatile during stress. High volatility can simultaneously create larger gross funding spreads and larger hedge/liquidation risk, so the carry source and failure risk rise together.

## Signal

The source supports the following normalized research rule without inventing an entry threshold it does not specify.

1. **Universe:** same-underlying perpetual contracts traded on one CEX and one DEX. The paper's main assets are BTC, ETH, and SOL.
2. **Formation timestamp:** each aligned funding period. Binance observations are on an eight-hour funding interval; dYdX hourly rates are summed into aligned eight-hour windows for the observed-protocol robustness exercise.
3. **Funding spread:** for asset `i` and aligned funding time `t`, compute
   `s(i,t) = f_DEX(i,t) - f_CEX(i,t)`.
4. **Position construction:** hold equal-notional, offsetting perpetual positions across the two venues so the portfolio receives funding on the higher-rate venue and pays funding on the lower-rate venue while minimizing outright directional exposure. Under the conventional positive-funding rule where longs pay shorts, this generally means taking the funding-receiving side on the higher-rate venue and the opposite directional side on the lower-rate venue; venue-specific funding sign conventions must be verified before implementation.
5. **Gross funding-period carry:** source framework models the funding component approximately as `leverage × funding spread`, with direction chosen to earn the spread.
6. **Portfolio weighting:** the source aggregates BTC, ETH, and SOL sleeves using equal capital weights, one-third per asset.
7. **Baseline leverage:** 3x in the source simulation. The paper later identifies 2-3x as materially safer than higher leverage under its survival model; this is a risk assumption, not evidence that leverage itself creates alpha.
8. **Holding / rebalance:** positions are evaluated over each funding period. The source computes a return for each funding period from the funding spread less modeled costs. It does **not** provide a source-backed minimum spread threshold, mandatory number of consecutive periods, or a fully specified live entry/exit state machine.
9. **Volatility regime overlay:** the paper classifies conditional volatility into terciles using GARCH(1,1). It suggests reducing leverage from 3x to 2x when conditional volatility exceeds the historical 67th percentile. This is a source-discussed risk overlay, not a separately validated alpha filter.
10. **Specification boundary:** exact spread-entry threshold, minimum expected carry after costs, venue-switch rules, order sequencing, exit-on-spread-compression rule, and re-entry logic remain **underspecified** for a production strategy.

## Required data

- **Instrument:** perpetual futures / perpetual swaps for the same underlying on at least two venues.
- **Universe:** source-tested BTC, ETH, SOL; broader asset portability is unproven.
- **Venues:** source main CEX input is Binance Futures; observed DEX robustness input is dYdX v4. A live adaptation must use current contract specifications and funding conventions for each actual venue pair.
- **Funding data:** current and historically realized funding rate, exact funding timestamps, funding interval, and sign convention for every venue.
- **Price fields:** perpetual mark price, index/reference price, and executable bid/ask or trade prices on both venues; spot/reference price where required to normalize residual basis.
- **Volatility:** point-in-time return history sufficient for the chosen volatility-regime estimator; the source uses GARCH(1,1) terciles.
- **Liquidity:** top-of-book spread, depth, expected participation, trade size, and slippage/impact estimates on both venues.
- **Margin/liquidation:** leverage, initial margin, maintenance-margin tiers, collateral asset, cross/isolated margin mode, liquidation fee, mark-price trigger rules, and partial-liquidation behavior.
- **DEX-specific:** gas/transaction fees where applicable, oracle/index mechanics, protocol status, settlement/finality risk, and smart-contract/protocol-change information.
- **CEX-specific:** counterparty/venue availability, collateral and transfer constraints, fee tier, and operational outage information.
- **Timestamp:** all rates and prices must be aligned point-in-time without using a funding observation before it was knowable/tradable.
- **Missing data:** missing/stale funding or mark/index observations must not be imputed silently. Venue outages and protocol interruptions should be explicit states.

## Execution assumptions

### Source-reported assumptions

- Baseline notional: USD 100,000.
- Baseline leverage: 3x.
- Equal-notional offsetting CEX/DEX positions.
- Slippage: baseline coefficient of 5 bp per transaction, modeled as increasing with position size/volatility.
- DEX gas cost: average USD 50 per trade, amortized over the holding period.
- Portfolio: equal-capital weighting across BTC, ETH, and SOL.
- Funding-period return: funding spread times leverage, less slippage and amortized gas costs.
- The simplified liquidation framework uses cumulative adverse basis move relative to leverage rather than reproducing a venue's exact maintenance-margin engine.

### Implementation gaps

A live/research-stack reconstruction still requires exact order sequencing. Simultaneous execution is impossible; leg risk exists between fills. Market versus limit orders, maker/taker fees, partial fills, rejected orders, latency, transfer latency, collateral fragmentation, cross-margin contagion, funding cutoff eligibility, and DEX transaction finality must be modeled explicitly.

The source's 5 bp slippage and USD 50 gas assumptions are not universal current-market constants. They must be replaced by point-in-time venue- and size-specific costs before any independent validation.

## Evidence
### Source-reported

The paper reports the following for its controlled baseline design:

- approximately 4,378 aligned funding observations per asset over January 2021-December 2024;
- simulated annualized mean return around 100.11% and annualized volatility around 2.58%, producing an extremely high reported Sharpe around 38.82 under a zero risk-free-rate assumption;
- maximum drawdown around 2.45%, occurring during the November 2022 FTX-collapse stress window;
- PnL attribution in which funding carry dominates gross return, while slippage, gas costs, basis effects, and liquidation losses materially alter net results;
- approximately 2.88% annualized modeled slippage cost and about 4.56% annualized gas cost in its attribution;
- stronger liquidation hazard as leverage rises, with a nonlinear deterioration at higher leverage and a superadditive leverage × volatility effect;
- high-volatility regimes producing both the largest positive and largest negative funding-arbitrage returns;
- an observed dYdX v4 funding-rate robustness exercise that changes some tail-risk/allocation results relative to the synthetic DEX input while leaving leverage as the dominant liquidation-risk predictor.

These are **source-reported model/simulation results**, not independently reproduced performance. The headline return and Sharpe depend materially on the synthetic DEX spread design and should not be interpreted as executable expected returns.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source provides unusually strong negative/limiting evidence for its own headline results:

1. The full-sample DEX funding series is synthetic, so the baseline is a controlled scenario, not a realized historical DEX strategy backtest.
2. Expected return is especially sensitive to the assumed structural CEX-DEX funding spread; this is mechanically the carry source.
3. Lag/noise assumptions materially affect volatility and drawdown.
4. The November 2022 FTX collapse generated the largest source-reported drawdown, showing that delta neutrality does not neutralize venue/counterparty stress.
5. Funding spreads can compress or invert after dislocations.
6. Funding and residual market risk account for major variance contributions even when directional exposure is nominally hedged.
7. Transaction costs are material; gas and slippage consume a nontrivial part of gross carry.
8. Higher leverage sharply increases liquidation hazard, particularly in high-volatility regimes.
9. The observed dYdX robustness window begins only in October 2023 and therefore cannot validate the full 2021-2024 synthetic history or the FTX stress episode.
10. Venue outages, capital/borrow constraints, tax, changing protocol design, custody/counterparty failures, and exact live maintenance-margin schedules are not fully captured.

## Falsification plan

A source-faithful independent test should fail or materially weaken the hypothesis if any of the following occurs:

1. **Observed-only replication:** replace synthetic DEX rates with point-in-time observed funding histories from real CEX/DEX venue pairs. If cross-venue spread carry is not positive out of sample before leverage after realistic costs, reject the central carry hypothesis for that venue pair.
2. **Net-of-cost threshold:** include maker/taker fees, spread, slippage/impact, gas, funding eligibility, and legging costs. Reject any apparent opportunity whose expected funding spread does not exceed a conservative all-in cost buffer.
3. **Causal timing:** use only funding rates or predicted/announced rates that were knowable before position eligibility cutoff. Any performance that disappears under strict availability timing indicates look-ahead contamination.
4. **Spread persistence:** estimate how often a positive net spread survives to actual funding settlement. If spread sign/reward persistence is too low after accounting for rate resets and contract rules, the strategy is not reconstructably harvestable.
5. **Basis/hedge stress:** replay large basis and mark-price divergences. Reject the assumption of effective delta neutrality if residual basis PnL dominates funding carry.
6. **Leverage sensitivity:** test 1x, 2x, 3x, 5x, and higher leverage using real maintenance-margin tiers and liquidation rules. If modest leverage materially increases ruin probability or produces unacceptable tail loss, do not treat headline carry as usable alpha.
7. **Venue-event stress:** explicitly include exchange/protocol outages, oracle incidents, collateral de-pegs, withdrawal freezes, and counterparty failures. If one venue event overwhelms multi-year carry, classify the strategy as tail-risk compensation rather than stable arbitrage.
8. **Regime test:** segment low/medium/high volatility and funding-spread regimes. If net carry exists only in one historical episode or collapses after 2024, treat it as regime-bound rather than persistent structural alpha.
9. **Asset/venue breadth:** replicate across multiple majors and multiple real CEX-DEX pairs. Failure outside one venue pair weakens the claimed structural mechanism.
10. **Baseline comparison:** compare against single-venue spot-perpetual cash-and-carry and unlevered collateral yield after identical operational-cost and tail-risk assumptions. The cross-venue version should deliver genuine incremental compensation for its extra venue risk.

## Crypto portability

**direct** for cryptocurrency perpetual markets; **unproven** outside the specific source venue/asset design.

The funding mechanism is crypto-native and the strategy directly targets venue fragmentation in perpetual swaps. Portability is nevertheless highly venue-specific because funding formulas, settlement cadence, mark/index construction, collateral, margin schedules, gas/transaction fees, oracle architecture, liquidity, and protocol/counterparty risk differ across exchanges.

A Binance-to-dYdX implementation is closer to the observed robustness exercise than a generic CEX-to-any-DEX implementation, but even that would require current contract and protocol rules rather than assuming 2023-2024 mechanics persist.

## Limitations

- **not independently reproduced**;
- **synthetic-data dependence:** the headline full-sample CEX-DEX spread uses modeled DEX rates;
- **underspecified:** no source-backed minimum funding-spread entry threshold or complete live state machine;
- **execution gap:** exact order sequencing, fill model, funding-cutoff eligibility, and live legging risk are not fully specified;
- **venue-model gap:** simplified liquidation thresholds do not reproduce current tiered exchange maintenance-margin engines;
- **data gap:** observed dYdX robustness covers only October 2023-December 2024;
- **capacity unproven:** modeled cost coefficients do not establish executable size on modern CEX/DEX books;
- **tail risk:** counterparty, oracle, settlement, collateral, and protocol risks can dominate nominal delta neutrality;
- **regime dependency:** funding dispersion may compress structurally as arbitrage capital and venue integration increase;
- **headline-metric caution:** very high source-reported Sharpe is mechanically sensitive to the modeled spread and low simulated return variance and should not be treated as validated expected performance.

## Implementation status

not-implemented

No PyBroker, Nautilus, paper, testnet, demo, or live implementation has been performed by ChatGPT in this Scout cycle.

## Adoption boundary

research-only

This record is strategy-pool research material. It is not evidence of validated profitability and does not authorize implementation, paper trading, testnet/demo trading, leverage use, venue allocation, or live trading.

## Related Wiki records

No Hermes Wiki Brain record was read or written in this Scout cycle. Related strategy-pool records include:

- `crypto-perpetual-no-arbitrage-deviation-2026-08-31.md` — theoretical perpetual-price no-arbitrage-bound deviation; related but materially different signal.
- `crypto-futures-cross-sectional-basis-high-low-1d-2026-08-31.md` — dated-futures cross-sectional basis predictor; related basis family but not cross-venue perpetual funding carry.

## Sources

1. Pindza, E. (2026). "Centralized-decentralized exchange funding rate arbitrage as a basis trade: risk decomposition, stress testing, and portfolio construction under venue uncertainty." *Digital Finance*, 8, Article 48. Published 19 August 2026. DOI: https://doi.org/10.1007/s42521-026-00213-3
2. Springer Nature article page (open access, version of record): https://link.springer.com/article/10.1007/s42521-026-00213-3
3. dYdX Foundation historical funding/indexer documentation cited by the source for the observed-protocol robustness input: https://indexer.dydx.trade/docs/
