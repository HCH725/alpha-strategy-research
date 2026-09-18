---
schema: strategy-research-record-v1
title: "FMZ SVD Basket Discovery: Automated Relative-Value Screening via Matrix Decomposition with Stability Gates"
created: 2026-09-18
updated: 2026-09-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - stat-arb
  - relative-value
  - svd
  - matrix-decomposition
  - basket-discovery
  - marchenko-pastur
  - principal-angle
  - automated-screening
  - tradfi-perpetual
  - gate-io
status: research-only
confidence: medium
source_as_of: 2026-08-26
sources:
  - "FMZ Quant blog article: 'From Pairs to Matrices: Let the Machine Find the Arbitrage Basket', published 2026-08-26. https://blog.mathquant.com/2026/08/26/from-pairs-to-matrices-let-the-machine-find-the-arbitrage-basket.html"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FMZ SVD Basket Discovery: Automated Relative-Value Screening via Matrix Decomposition with Stability Gates

## Provenance

- **Source URL**: https://blog.mathquant.com/2026/08/26/from-pairs-to-matrices-let-the-machine-find-the-arbitrage-basket.html
- **Title (source)**: "From Pairs to Matrices: Let the Machine Find the Arbitrage Basket"
- **Author**: FMZ Quant platform blog (blog.mathquant.com), published 2026-08-26
- **Platform**: FMZ Quant (發明者量化)
- **Source type**: Public blog article with full Python source code. Not a peer-reviewed paper. No arXiv/SSRN identity. Stable identity is the blog URL + as-of date.
- **Not a strategy page**: This is a methodology article describing a general-purpose screening workflow. The source provides Python code and a Gate.io-configured paper-mode implementation.
- **Related but distinct from**: `gateio-tradfi-matrix-null-space-stat-arb-q-score-fshock-2026-09-15.md` (a specific strategy implementation by FMZ community user `ianzeng123` using SVD null-space on Gate.io TradFi perpetuals). The current record covers the general-purpose screening methodology article from the platform blog, which is a different source with different scope (general basket discovery vs. a specific strategy implementation).

## Economic mechanism

### Source-reported

The source argues that the ceiling of traditional pair trading is not return but human cognitive bandwidth: a human can only manually examine a limited number of instrument relationships at once. The proposed solution is to automate basket discovery using SVD on a log-price matrix, separating common-factor movements from residual relative-value deviations.

The workflow:
1. Arrange log prices as a T×N matrix (time × instruments).
2. Compute SVD to separate leading common-trend directions (k) from residual subspace (N-k dimensions).
3. Use Marchenko-Pastur upper-edge rule as a heuristic for choosing k.
4. Apply singular-value gap ratio and principal-angle stability tests to reject unstable baskets.
5. Monitor residual-subspace displacement (Q-score) while blocking entries during factor-space repricing (F-shock).
6. Use leave-one-out regression for per-instrument attribution.

The source explicitly states this is **statistical arbitrage**, not physical arbitrage: convergence is probabilistic, not guaranteed, especially for TradFi perpetual contracts that cannot be physically delivered.

### Research interpretation

The hypothesized mechanism is **temporary structural mispricing within a factor-driven basket**: when the residual (null-space) projection of current log prices is extreme relative to training-window residual covariance, but common-factor scores have not jumped, the move is treated as structural misalignment rather than new information, and the system bets on residual mean reversion. If factor scores also jump (F-shock), mean reversion is blocked.

This is a multi-asset generalization of residual/pairs mean reversion, with an explicit gate that separates idiosyncratic mispricing from systematic repricing. The key innovation over manual pair selection is automated basket discovery via matrix decomposition, enabling monitoring of multiple orthogonal residual directions simultaneously.

The missing economic link (not proven by the source): whether TradFi stock perpetuals — which cannot be physically delivered — actually enforce residual convergence through funding, inventory, and quoting habits rather than delivery arbitrage.

## Signal

### Formation timestamp
- Signal formed at each bar close (default: 15-minute bars).
- Timezone: exchange-local (Gate.io UTC).
- Formation and tradability are simultaneous (signal → immediate order).

### Lookback
- Training window: configurable (default appears to be several hundred bars on 15-minute data).
- Warm-up: requires minimum common K-lines across all instruments (default: 490) before any calculation.
- The Marchenko-Pastur factor count adapts automatically via q = N/T.

### Entry
- **Q-score alarm**: Residual-subspace Mahalanobis distance exceeds χ²(0.995, r) threshold (99.5th percentile).
- **F-shock block**: Factor-space Mahalanobis distance of first-difference exceeds limit → entry blocked.
- Entry condition: `alarm == True AND blocked == False`.
- Direction: determined by sign of residual displacement (which instrument is expensive/cheap relative to basket).
- Order type: market/limit (source provides paper-mode maker-fill simulation).

### Exit
- **Q-score exit**: Residual displacement falls below χ²(0.80, r) threshold (80th percentile).
- **Holding period**: configurable max hold (source mentions OU half-life of ~18 bars / 4.5 hours on 15-minute data for one example basket).
- Exit direction: flatten all legs.

### Holding period
- Expected: several hours (OU half-life ~18 bars on 15-min data for the example basket).
- Maximum: configurable.

### Parameters
- `k` (factor count): determined by Marchenko-Pastur upper-edge rule (not manually tuned).
- `MIN_GAP`: minimum singular-value ratio for subspace stability (default: 1.30). **research-proposed**.
- `MAX_ANGLE_DEG`: maximum principal angle between half-sample residual subspaces (default: 20°). **research-proposed**.
- `q_entry`: χ²(0.995, r) for Q-score entry threshold. **research-proposed** (distribution-based, not empirically calibrated).
- `q_exit`: χ²(0.80, r) for Q-score exit threshold. **research-proposed**.
- `f_limit`: F-shock blocking threshold. **research-proposed** (value not specified in article).
- `MIN_LOO_Z`: minimum leave-one-out z-score for attribution (default: 2.0). **research-proposed**.

### Position sizing
- Not explicitly specified in the source. Research-proposed: equal-notional or risk-parity across legs.

### Multi-timeframe dependencies
- Default: 15-minute bars.
- The approach is timeframe-agnostic in principle.

### Specification status
- The signal is reconstructable from the source code and article description.
- Several thresholds (MIN_GAP, MAX_ANGLE_DEG, q_entry, q_exit, f_limit, MIN_LOO_Z) are research-proposed defaults, not empirically validated on the target universe.

## Required data

- **Instrument**: TradFi perpetual contracts (Gate.io `contract_type=stocks`, optionally `indices`). The example universe includes AMD, ARM, ASML, INTC, MRVL, NVDA, TSM, QQQ, SPY, and others.
- **Venue**: Gate.io (default configuration). Adaptable to other exchanges with symbol/metadata/fee adaptations.
- **Market type**: USDT-margined linear perpetual contracts.
- **Timeframe**: 15-minute K-lines (default).
- **Fields**: Close prices (log-transformed). SVD operates on demeaned returns derived from log prices.
- **Timestamp**: Exchange-local time.
- **Missing data**: Strategy requires aligned timestamps across all instruments. If any leg has zero, negative, or non-numeric price, the entire cycle is invalidated. At least 490 common K-lines required.

## Execution assumptions

- **Signal-to-order timing**: Immediate at bar close.
- **Order type**: Maker orders (paper-mode fill simulation using real order-book data).
- **Fill model**: Paper-mode maker fill simulation; not validated on live execution.
- **Fees**: Not explicitly specified; source provides fee-adaptable code structure.
- **Slippage**: Not explicitly modeled; source flags execution as a key open question.
- **Spread**: Not explicitly modeled.
- **Funding**: Not explicitly modeled in the screening workflow; acknowledged as a cost for TradFi perpetuals.
- **Leverage**: Not specified.
- **Latency**: Not specified.
- **Partial fills**: Not explicitly handled.
- **Multi-leg execution risk**: Source explicitly flags that the three legs cannot fill simultaneously, creating leg risk. This is identified as a key limitation.

## Evidence

### Source-reported

- The source provides one worked example: a semiconductor-related basket where SVD found k=1 common factor, singular-value ratio ~4.5, principal angle ~12° between half-samples, and estimated reversion half-life ~18 bars (4.5 hours on 15-min data).
- Six retained residual directions passed stationarity screening in the example.
- No backtest performance figures (Sharpe, return, drawdown) are reported.
- The source explicitly states: "Accumulate enough out-of-sample evidence before discussing live capital."
- No reversion rate or hit rate is reported for the forward validation table (it shows "—" for all fields).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Source explicitly identifies four key limitations:
  1. No forced convergence mechanism (TradFi perpetuals cannot be physically delivered).
  2. Sample length is the largest weakness (many contracts have short histories).
  3. Filters only raise probability of forward validity, not guarantee it.
  4. Large-scale screening creates multiple-testing risk.
- Source notes that baskets passing visual correlation inspection often fail the principal-angle stability test (examples: 49.6°, 87.0°, 80.0° rotation between half-samples).
- Source warns that high correlation ≠ stable tradable relationship.

## Falsification plan

1. **Forward reversion rate**: Track Q-score alerts and measure actual reversion rate. Threshold: if reversion rate < 50% with sufficient sample, stop. **research-defined falsification threshold**.
2. **Principal-angle stability**: Monitor rolling principal angles; if angles consistently exceed 20°, the basket structure is unstable. **research-defined falsification threshold**.
3. **Singular-value gap**: If gap ratio consistently falls below 1.30, subspace separation is insufficient. **research-defined falsification threshold**.
4. **F-shock filter effectiveness**: Compare returns with and without F-shock blocking; if blocking does not improve risk-adjusted returns, the filter is not useful.
5. **Multiple-testing correction**: Track number of baskets/directions screened and apply Bonferroni or FDR correction to forward reversion rates.
6. **Cost sensitivity**: Model realistic fees, slippage, and funding costs; if net-of-cost reversion rate < 50%, the strategy is not viable.
7. **Out-of-sample period**: Require minimum 3 months of forward data before any performance claim.

## Crypto portability

**adapted**

The methodology is asset-class agnostic (works on any price matrix). The source applies it to Gate.io TradFi perpetual contracts, which are crypto-native instruments referencing traditional assets. For pure crypto perpetuals (BTC, ETH, etc.), the approach could be applied directly, but:

- Crypto perpetuals have funding rates that create asymmetric carry costs.
- 24/7 trading removes session-boundary effects present in TradFi.
- Crypto markets have higher volatility clustering, which may affect SVD stability.
- The absence of physical delivery for all perpetual contracts means convergence is purely statistical.
- Venue fragmentation across crypto exchanges may complicate multi-leg execution.

## Limitations

- **No performance evidence**: The source provides zero backtest metrics. The forward validation table is empty.
- **Paper-mode only**: Implementation runs in paper/simulation mode; no live or testnet validation.
- **Sample length insufficient**: Many TradFi perpetual contracts have short histories (listed in 2026); cannot establish stability across earnings cycles or regime changes.
- **Multiple-testing risk**: The screening process evaluates many clusters, baskets, directions, and thresholds. Best-looking survivors may appear significant purely due to search breadth.
- **Marchenko-Pastur is a heuristic**: Financial returns are not independent Gaussian noise; temporal dependence, heavy tails, and volatility clustering can change the empirical eigenvalue spectrum.
- **Execution not validated**: Multi-leg execution risk, slippage, fees, and funding costs are flagged but not modeled.
- **Leg risk**: The three legs cannot fill simultaneously; per-leg circuit breakers damage hedge structure (source acknowledges this).
- **Leave-one-out attribution limitations**: OLS residual orthogonality does not ensure live factor neutrality.
- **Data gap**: F-shock blocking threshold (`f_limit`) value not specified in article.
- **Data gap**: Position sizing logic not specified.

## Implementation status

No implementation in our research stack. The source provides Python code configured for Gate.io paper mode. No backtest, paper trading, testnet, or live validation has been completed by the source.

## Adoption boundary

This record is research material only. It does not mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

The source itself explicitly states: "Accumulate enough out-of-sample evidence before discussing live capital."

## Related Wiki records

- [[gateio-tradfi-matrix-null-space-stat-arb-q-score-fshock-2026-09-15]] — Related SVD null-space stat arb implementation on Gate.io TradFi perpetuals by a different author (ianzeng123), with Q-Score/F-Shock disambiguation. Same conceptual family, different source and scope.
- [[crypto-perpetual-pca-factor-residual-reversion-falsification-2026-09-12]] — PCA-based factor residual reversion on crypto perpetuals; related spectral decomposition approach.
- [[sp500-statistical-arbitrage-johansen-ou-ablation-multiple-testing-2026-09-12]] — Statistical arbitrage with multiple-testing controls; relevant falsification methodology.

## Sources

- FMZ Quant blog article: "From Pairs to Matrices: Let the Machine Find the Arbitrage Basket", published 2026-08-26. https://blog.mathquant.com/2026/08/26/from-pairs-to-matrices-let-the-machine-find-the-arbitrage-basket.html
