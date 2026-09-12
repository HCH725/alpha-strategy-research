---
schema: strategy-research-record-v1
title: "Funding-Rate Feedback Regime and Capital-Dependent Stability Band in Crypto Perpetual Futures"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - funding-rate
  - market-microstructure
  - limits-to-arbitrage
  - regime-conditional
status: research-only
confidence: medium
source_as_of: 2026-09-05
sources:
  - "Tianyang Zhang, 'A Shared Template Without Shared Feedback: Funding Rates in Cryptocurrency Perpetual Futures', SSRN 6185958, Zhongnan University of Economics and Law (August 30, 2026; last revised September 5, 2026). DOI: 10.2139/ssrn.6185958"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Funding-Rate Feedback Regime and Capital-Dependent Stability Band in Crypto Perpetual Futures

## Provenance

- Author: Tianyang Zhang, Zhongnan University of Economics and Law, Wuhan, China.
- Title: "A Shared Template Without Shared Feedback: Funding Rates in Cryptocurrency Perpetual Futures."
- Source: SSRN working paper 6185958, 59 pages.
- Date written: August 30, 2026. Posted: February 25, 2026. Last revised: September 5, 2026.
- DOI: 10.2139/ssrn.6185958.
- Empirical universe: 200 Binance USDT-margined perpetual futures.
- Sample period: Not specified in abstract; evidence from 200 Binance perpetuals is referenced.
- No code repository identified.

## Economic mechanism

### Source-reported

The paper develops a continuous-time equilibrium model with four participant types: extrapolative traders (momentum speculators), capital-constrained arbitrageurs, liquidity suppliers, and a piecewise funding rule imposed by the exchange. The model yields a **capital-dependent stability band** for the perpetual-spot basis. The feedback mechanism works as follows:

1. **Weak feedback** (low speculative demand or high arbitrageur capital): Price gaps between perpetual and spot persist because the funding transfer is too small to motivate corrective positions. The basis remains outside the band for extended periods.

2. **Intermediate feedback** (moderate speculative demand): Funding stabilizes the basis, with the perpetual price reverting toward spot either by crossing spot or settling within the band. This is the regime where the funding mechanism is "working as intended."

3. **Strong feedback** (high speculative demand relative to available arbitrageur capital): The funding payment becomes large enough that liquidation events cascade — the paper identifies **directional liquidation** as a key driver of basis reversals. Losses and liquidation reduce future corrective capacity, making stabilization infeasible. Too-strong feedback generates expanding reversals rather than stabilization.

Additional structural effects:
- **Leverage constraints** prevent arbitrageurs from expanding positions even when funding becomes attractive, creating an upper bound on corrective capacity.
- **Pre-settlement trading and interval averaging**: Pre-settlement trading distorts the funding rate observed at settlement, and interval averaging (8-hour TWAP) further dampens the signal.
- **Piecewise funding rule**: The flat region (funding near zero) and capped region (funding capped at ±0.03% per interval on Binance) separate the nominal funding template from the effective funding response. Rate caps accompany persistent price gaps when feedback should be stronger.
- **Nominal vs. effective feedback**: The paper's central finding is that a shared funding template does not guarantee shared feedback — different perpetuals experience very different effective feedback regimes depending on participant composition, leverage, and capital availability.

### Research interpretation

The paper provides a falsifiable theoretical framework for understanding why funding rates behave differently across perpetuals despite sharing the same nominal rule. The testable implications are:

1. Cross-sectional variation in funding-rate effectiveness (basis convergence speed) is predicted by open interest composition, leverage utilization, and liquidation frequency — not by the funding rate itself.
2. Assets where funding is capped (hitting ±0.03% limits) should exhibit persistent basis gaps that do not converge until speculative demand weakens or arbitrageur capital expands.
3. Directional liquidation events should predict basis reversals — forced selling (or buying) creates a predictable correction pattern.
4. The capital-dependent stability band implies a nonlinear relationship between funding rate magnitude and basis convergence: increasing funding beyond a threshold does not improve convergence and may trigger instability.

These hypotheses are testable with public Binance perpetual data (funding history, open interest, liquidation events, basis data).

## Signal

The paper proposes a regime-conditional framework rather than a single directional signal. The trading-relevant hypotheses are:

### Regime detection (research-proposed operationalization)
- **Funding-capped regime**: Identify perpetuals where the funding rate is at the ±0.03% cap for consecutive settlement intervals. Source-reported: rate caps accompany persistent price gaps.
- **Liquidation-driven reversal regime**: After a cluster of directional liquidations (source-reported: basis reversals are associated with directional liquidation), the basis should predictably revert. Research-proposed entry: enter opposing the liquidation direction once liquidation volume exceeds a threshold.
- **Weak-feedback persistence regime**: When funding is near zero (flat region) and the basis remains wide, the gap is expected to persist. Research-proposed: avoid taking convergence trades in this regime.

### Signal details (research-proposed where not source-specified)
- **Formation timestamp**: End of each 8-hour funding settlement interval.
- **Lookback**: Research-proposed: monitor funding rate for consecutive cap-hits over the last 3-5 intervals; monitor liquidation events over the last 1-2 intervals.
- **Entry**: Research-proposed: (a) In funding-capped regime — enter contrarian to the persistent basis direction once cap has been hit for ≥3 consecutive intervals. (b) In liquidation regime — enter opposite to liquidation direction after liquidation volume exceeds a threshold (specific threshold not source-specified).
- **Exit**: Research-proposed: exit when funding rate moves away from the cap by ≥50% of the cap width, or when basis reverts to within a threshold of zero (specific threshold not source-specified).
- **Holding period**: Research-proposed: 1-5 funding intervals (8-40 hours), depending on regime persistence.
- **Parameters**: All specific thresholds are research-proposed; the paper does not provide operational trading parameters.
- **Position sizing**: Not specified by source. Research-proposed: scale by inverse of the asset's liquidation propensity (open interest / leverage distribution), as higher liquidation propensity increases regime volatility.

## Required data

- Instrument: USDT-margined perpetual futures on Binance (200 pairs per source).
- Venue: Binance Futures.
- Market type: Perpetual futures (USDT-margined).
- Timeframe: 8-hour funding settlement intervals; intraday liquidation data if available.
- Fields: Funding rate (paid/received), mark price, index price, basis (mark - index), open interest, leverage distribution (if available), liquidation events (type, direction, volume), number of consecutive funding intervals at cap.
- Point-in-time: Funding rates and liquidation data must be timestamped at settlement. Pre-settlement trading data is relevant but requires high-frequency access.
- Timestamp: UTC. Funding settlement times on Binance are 00:00, 08:00, 16:00 UTC.
- Missing-data: Liquidation data granularity varies; Binance public API may not provide full liquidation history. Basis calculation requires consistent mark/index price sources.

## Execution assumptions

- Signal-to-order timing: Order placed after funding settlement and basis observation. Source does not specify execution timing relative to settlement.
- Fill model: Not specified by source. Research-proposed: assume next-interval mid price execution.
- Fees: Binance maker/taker fee schedule applies. Source does not model transaction costs explicitly.
- Slippage/spread: Not specified by source. Research-proposed: account for basis widening during volatile liquidation periods.
- Funding: The strategy is explicitly about exploiting mispriced funding — funding payments are part of the P&L, not a cost.
- Leverage: Source identifies leverage constraints as a binding constraint on arbitrageur behavior. Research-proposed: use conservative leverage (2-3x) to avoid being subject to the same liquidation dynamics being exploited.
- Liquidation risk: Not specified by source. Research-proposed: maintain position sizes well below liquidation thresholds, as the strategy itself depends on observing others' liquidation events.

## Evidence

### Source-reported

The paper provides theoretical model predictions and empirical evidence from 200 Binance USDT-margined perpetuals. The following claims are source-reported:

1. **Capital-dependent stability band**: The model derives a stability band whose width depends on arbitrageur capital, speculative demand, and the funding rule parameters. (Source: theoretical model, Section not specified.)
2. **Nominal funding rule ≠ effective feedback**: The paper documents that different perpetuals experience very different feedback regimes despite sharing the same funding template. (Source: empirical evidence from 200 Binance perpetuals.)
3. **Basis reversals associated with directional liquidation**: The empirical evidence supports the model prediction that basis reversals are associated with directional liquidation events. (Source: empirical evidence, Section not specified.)
4. **Rate caps accompany persistent price gaps**: When the funding rate hits the ±0.03% cap, price gaps between perpetual and spot persist. (Source: empirical evidence from 200 Binance perpetuals.)
5. **Weak feedback → persistent gaps; intermediate feedback → stabilization; strong feedback → expanding reversals**: The three feedback regimes are derived from the model. (Source: theoretical model, Section not specified.)

No specific Sharpe ratios, win rates, drawdowns, or other quantitative performance metrics are reported in the abstract or available secondary sources. The paper is a working paper with 59 pages; specific performance numbers may exist in the full text but could not be verified from the abstract alone.

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed sources; absence is not evidence of no negative result.

The paper itself notes limitations of the funding mechanism:
- Leverage constraints can prevent arbitrageurs from expanding corrective positions.
- Losses and liquidation reduce future corrective capacity.
- Pre-settlement trading and interval averaging distort the nominal funding signal.
- Rate caps create persistent gaps that do not converge.

These are structural limitations of the funding mechanism itself, not failures of the paper's model.

## Falsification plan

1. **Basis convergence speed test**: Rank perpetuals by their average funding-rate cap-hitting frequency. If the model is correct, high cap-hitting frequency should predict slower basis convergence. Research-defined threshold: if Spearman correlation between cap-hitting frequency and basis persistence (half-life of basis decay) is not significantly positive (p < 0.05), the hypothesis is weakened.

2. **Liquidation-reversal test**: After clustering directional liquidation events (research-defined: ≥3 consecutive intervals with net directional liquidation), test whether the basis reverses within the next 1-3 intervals. Research-defined failure: if the hit rate for basis reversal within 3 intervals does not exceed 50% after liquidation clusters, the liquidation-reversal hypothesis is weakened.

3. **Cross-sectional regime decomposition**: Test whether the three feedback regimes (weak, intermediate, strong) are distinguishable in cross-sectional data. Research-defined: if k-means or similar clustering on (funding rate, basis persistence, liquidation frequency) does not yield three separable clusters, the regime taxonomy may not be empirically grounded.

4. **Out-of-sample regime persistence**: Test whether regime classifications are stable over time. Research-defined failure: if regime labels flip frequently (e.g., >50% of perpetuals change regime every month), the framework may not be actionable.

5. **Fee sensitivity**: The gross basis convergence edge must exceed transaction costs. Research-defined: test at fee levels of 0.02%, 0.04%, and 0.06% per round trip.

## Crypto portability

**Direct** — the paper is already written for crypto perpetual futures on Binance.

Crypto-specific considerations:
- The funding mechanism is specific to perpetual futures; spot and dated futures have different convergence mechanisms.
- The ±0.03% funding rate cap is Binance-specific; other exchanges (OKX, Bybit, Hyperliquid) have different caps or no caps.
- The 8-hour funding interval is Binance-specific; some exchanges use 1-hour or 4-hour intervals.
- Cross-venue analysis would require normalizing the funding rule parameters.
- On-chain perpetual futures (Hyperliquid, dYdX) have different funding mechanisms that may not exhibit the same feedback dynamics.

## Limitations

- **Full text inaccessible for verification**: The abstract provides the model structure and key findings, but specific equations, parameter values, sample period details, and quantitative results could not be verified from the primary source. Specific performance numbers (if any) are marked as data gap.
- **Sample period not specified in abstract**: The paper covers 200 Binance perpetuals but the exact time window is not stated in the abstract. This is a data gap.
- **No performance metrics in abstract**: No Sharpe ratio, win rate, drawdown, or other quantitative backtest results are available from the abstract. The paper may contain these in the full text.
- **Not independently reproduced**: The theoretical model and empirical evidence have not been independently verified.
- **Model assumptions**: The model assumes a continuous-time equilibrium with specific participant types; real markets have discrete-time funding, async execution, and heterogeneous participants beyond the four types modeled.
- **Single-venue evidence**: Evidence is from Binance only; cross-venue generalizability is not tested.

## Implementation status

No implementation in our research stack has been completed. This is research-only material from an external working paper.

## Adoption boundary

This record is research material only. Its presence in this repository does **not** mean:
- The strategy is profitable;
- The model's predictions are validated;
- The strategy is approved for implementation;
- The strategy is approved for paper trading, testnet, or live trading.

The paper provides a theoretical framework and empirical evidence about funding-rate dynamics. Translating this into a tradeable strategy requires additional research, including: (a) operationalizing the regime detection rules, (b) backtesting with realistic transaction costs, and (c) validating the signal's economic significance.

## Related Wiki records

- [[quant/strategy-research-record-spec-v1]] (schema specification)
- `crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11.md` (related: funding rate as carry factor, but different mechanism — cross-sectional carry vs. regime-conditional feedback dynamics)
- `crypto-perpetual-futures-self-benchmarked-factor-alpha-2026-09-01.md` (related: perpetual futures factor investing, but different mechanism)
- `crypto-cross-sectional-stat-arb-funding-binding-cost-negative-2026-09-09.md` (related: funding as binding cost in stat arb, complementary negative evidence)
- `crypto-hyperliquid-momentum-funding-carry-combo-2026-09-12.md` (related: momentum-funding carry, different mechanism)

No directly related strategy research records share the same source identity or materially identical mechanism. The paper's feedback-regime taxonomy and capital-dependent stability band are distinct from existing funding-rate carry or momentum-funding strategies in the repository.

## Sources

1. Tianyang Zhang. "A Shared Template Without Shared Feedback: Funding Rates in Cryptocurrency Perpetual Futures." SSRN working paper 6185958, Zhongnan University of Economics and Law. August 30, 2026; last revised September 5, 2026. DOI: 10.2139/ssrn.6185958. 59 pages. Abstract available at https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6185958.

2. Additional context from citation in arxiv:2605.10400v1 ("Resolution-Aware Perpetual Futures on Binary Prediction Markets"), which describes Zhang 2026 as treating "the funding rate as an algorithmic feedback rule rather than a passive transfer, deriving stability conditions in a continuous-time equilibrium with risk-constrained arbitrageurs and momentum speculators."
