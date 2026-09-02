---
schema: strategy-research-record-v1
title: "Bitcoin Halving Clock: Time-Based Cycle-Top Timing via Post-Halving Regularity"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - bitcoin
  - halving
  - cycle-timing
  - time-based-signal
  - structural-pattern
  - power-law
  - on-chain
status: research-only
confidence: medium
source_as_of: 2026-07-28
sources:
  - "Molnar (2026), 'Bitcoin Runs on a Clock: Why Every Price Indicator Dies and the Halving Clock Doesn't', arXiv:2607.26188v1 [q-fin.ST], July 28, 2026. https://arxiv.org/abs/2607.26188"
  - "GitHub: BitcoinDaily/bitcoin-runs-on-a-clock, commit c5d4a6e60ae1ab020db88b758fcb7c1f997e6e89 (v1.6, July 30, 2026)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Halving Clock: Time-Based Cycle-Top Timing via Post-Halving Regularity

## Provenance

- **Primary Paper:** Molnar (2026), "Bitcoin Runs on a Clock: Why Every Price Indicator Dies and the Halving Clock Doesn't," arXiv:2607.26188v1 [q-fin.ST], July 28, 2026. DOI: [10.48550/arXiv.2607.26188](https://doi.org/10.48550/arXiv.2607.26188). Full text: https://arxiv.org/abs/2607.26188.
- **GitHub Repository:** BitcoinDaily/bitcoin-runs-on-a-clock, commit SHA `c5d4a6e60ae1ab020db88b758fcb7c1f997e6e89` (v1.6, July 30, 2026). URL: https://github.com/BitcoinDaily/bitcoin-runs-on-a-clock.
- **Data Sources:** Coin Metrics community series (CapMVRVCur, IssTotUSD); Bitstamp daily BTC/USD price data.
- **Paper Stats:** 32 pages, 11 figures.
- **Author:** Molnar (name from GitHub repository description).
- **Note:** The paper includes two public, platform-timestamped YouTube antecedents (January 2025) that applied the 18-months-after-halving heuristic before the paper's analysis was completed, and a GitHub audit trail predating the arXiv submission.

## Economic mechanism

### Source-reported

Molnar argues that Bitcoin's cycle tops are primarily governed by a time-based clock (days since halving) rather than by price-based thresholds. The central observation: across three "mature" Bitcoin halving cycles (2017, 2021, and 2025 peaks), cycle tops cluster within a 21-day window on the halving clock — 525, 546, and 534 days after each respective halving. By contrast, every widely followed price-anchored indicator (Pi Cycle, MVRV, Mayer Multiple, Puell Multiple) has progressively failed as cycle-callers, exhibiting a predictable death sequence: precise → early → silent.

The paper attributes this to a "damped oscillation" dynamic: Bitcoin's price deviation from its adoption trend (a power law) compresses monotonically with each cycle, so price-based thresholds set from past amplitude become permanently unreachable, while the halving schedule — being no one's inefficiency — is not arbitraged.

### Research interpretation

The hypothesized mechanism is a **structural time anchor**: the Bitcoin halving event acts as a Schelling point (coordination device) for market participants, creating a self-reinforcing cycle where the fixed supply reduction schedule structures expectations and market timing around a fixed temporal coordinate. Two causal channels are plausible but observationally indistinguishable at N=3:

1. **Real supply economics:** The halving mechanically reduces new supply issuance, creating a supply-demand imbalance that peaks at a predictable lag.
2. **Coordination/Schelling point:** The halving schedule is publicly known code; participants coordinate around it, creating self-fulfilling timing regularity.

The paper does not claim to distinguish these channels. The alpha hypothesis is that tops are more predictable in time (days since halving) than in price, and that monitoring the halving clock provides a structural edge over price-based indicators.

## Signal

### Source-reported

The paper defines a two-coordinate state description — the "Satoshi Clock":

1. **CLOCK:** Days (or blocks) since the most recent Bitcoin halving. This is the timing coordinate.
2. **SPRING:** Causal power-law deviation — the standardized residual of Bitcoin's price from a fitted power law with exponent n ≈ 5.6. Specifically, the daily price is compared against a power-law trend anchored to issuance data; the deviation is standardized by its expanding mean and standard deviation to produce a z-score.

**Cycle tops** cluster in the CLOCK dimension (tight temporal band) but diverge in the SPRING dimension (compressing amplitude). The three mature tops show:
- CLOCK: 525, 546, 534 days (range = 21 days)
- SPRING at tops: +2.85 → +2.69 → +1.29 (monotonically declining)

**Cycle bottoms** show the opposite: partial but incomplete clustering in CLOCK, with no consistent SPRING pattern.

### Signal formation and tradeability

- **Formation timestamp:** The clock value (days since halving) is observable continuously and instantaneously — the halving date is fixed protocol data.
- **Entry:** Research-proposed: enter a short (or reduce long exposure) when CLOCK enters a "danger zone" near 525–546 days post-halving AND SPRING is elevated. The specific SPRING threshold for entry is underspecified in the paper — the paper notes that moderate entry thresholds (z < 0 or +0.25) are needed for the timing signal to cross positive on a risk-adjusted basis, while deeper thresholds (z << 0) underperform.
- **Exit:** Research-proposed: exit after the observed top cluster window (approximately 525–546 days) or upon SPRING compression below a threshold. The paper does not specify an exact exit rule.
- **Holding period:** The signal is designed for cycle-scale (multi-year) positioning, not intraday or short-term trading.
- **Parameters:** The clock thresholds (525–546 days) are observed from 3 mature cycles. The power-law exponent n ≈ 5.6 is fitted from historical data (converges on expanding estimation). The SPRING z-score uses expanding-window standardization.
- **Underspecified items:** The exact SPRING entry/exit thresholds, position sizing rules, and whether the signal should be used as a binary filter or a continuous allocation input are not fully specified by the source. The paper focuses on timing validation rather than constructing a complete trading strategy.

## Required data

- **Instrument:** BTC (Bitcoin).
- **Universe:** Single-asset Bitcoin analysis. No cross-sectional component.
- **Venue:** Bitstamp (price data); Coin Metrics (on-chain metrics: MVRV, issuance).
- **Market type:** Spot price data used; the signal is designed for spot or long-only perpetual positioning.
- **Timeframe:** Daily bars. The clock coordinate is continuous (not bar-dependent).
- **Fields:** Daily close price (BTC/USD), halving dates (protocol-defined, fixed), MVRV ratio (CapMVRVCur), daily issuance value (IssTotUSD).
- **Point-in-time:** Halving dates are fixed protocol events with no look-ahead. Price and on-chain data are point-in-time daily closes.
- **Timestamp:** UTC daily.
- **Missing-data:** Coin Metrics community data has some historical gaps; paper addresses this with cross-source replication (Bitstamp vs Coin Metrics).
- **Funding/fee/spread:** Not explicitly modeled. The paper focuses on timing validation rather than execution.

## Execution assumptions

The paper is primarily a timing validation study, not an execution-focused strategy paper. Key execution assumptions:

- **Signal-to-order timing:** Daily bar close; next-bar open execution (paper states "any trade-structure evaluation enters at the next bar's open").
- **Order type:** Not specified; assumed market order for simplicity.
- **Fill model:** Not specified.
- **Fees/spread/slippage:** Not modeled. The paper's IC framework and timing tests do not deduct transaction costs. Given the multi-year holding period of the signal, single-trade costs are negligible relative to the cycle-scale returns, but opportunity costs and funding during extended holding are material.
- **Leverage:** Not specified.
- **Capacity:** Not a binding constraint for a single-asset BTC strategy.

## Evidence

### Source-reported

- **Cycle-top clustering:** Three mature tops cluster within 21 days on the halving clock (525, 546, 534 days). A full-variant permutation grid (no cell hidden) yields p ≈ 10^-3 to 10^-5 for the top-timing regularity, depending on specification.
- **Four-year clock placebo:** None of 2,000 random four-year clocks produces a top cluster as tight as the halving clock, confirming the regularity is halving-specific, not generic four-year periodicity.
- **Indicator death sequence:** Price-anchored indicators (Pi Cycle, MVRV 3.7, Mayer 2.4, Puell 4.0/5) progressively fail in a predictable order, consistent with damped oscillation.
- **Power-law convergence:** The causal power-law exponent converges to n ≈ 5.6 across expanding estimation, consistent across Bitstamp (5.61) and Coin Metrics (5.67).
- **Out-of-sample crossover:** The SPRING signal's IC rises monotonically across epochs and crosses positive on a risk-adjusted basis in the most recent epoch.
- **Pre-registered predictions:** Two public YouTube antecedents (January 2025) applied the 18-months-after-halving rule before the paper's analysis; the realized cycle top (October 6, 2025) fell within the predicted window.
- **Buy-and-hold comparison:** A SPRING-filtered holdout (2021–2026) shows cumulative performance crossing buy-and-hold in the current epoch, with approximately 50× terminal wealth over full history vs buy-and-hold.

### Independently reproduced

Not independently reproduced. Results depend on the author's own analysis with code published on GitHub (commit `c5d4a6e6`). Reproducibility is supported by the published audit trail and seeded scripts.

### Negative evidence

- **Bottom timing fails:** The paper's own demoted bottom statistic shows no clock evidence for cycle bottoms (process-intrinsic drawdown null reproduces bottom clustering in ~38% of null paths).
- **Amplitude compression:** SPRING at tops declines monotonically (+2.85 → +2.69 → +1.29), meaning each successive cycle's peak is smaller in deviation terms — a structural constraint on future cycle alpha.
- **Post-hoc window choice:** The null test was designed after the clustering was observed; the paper mitigates this with a full sensitivity grid but cannot eliminate post-hoc-ness.
- **N=3 mature cycles:** The fundamental sample limitation. Per-epoch inference is explicitly disclaimed as unreliable (persistent-regressor calibration caveat).
- **Single-author analysis:** The paper is self-authored; no independent peer review yet.

## Falsification plan

1. **Prospective test (pre-registered):** The paper pre-registers the claim that the next Bitcoin cycle top will fall within a similar 525–546-day window post-halving. Falsification: if the next mature top occurs outside a ±30-day band around535 days post-halving, the timing regularity is materially weakened.
2. **Bottom timing null:** Already falsified by the paper's own analysis — bottom clustering is not distinguishable from random drawdown process. This result should be confirmed.
3. **Amplitude compression continuation:** If the next cycle's SPRING at top does NOT compress (i.e., exceeds +1.29), the damped-oscillation thesis is weakened.
4. **Four-year clock placebo:** Already tested — halving-specific regularity survives, generic four-year clock does not. Should be re-tested with each new cycle.
5. **Cross-asset replication:** Paper claims the framework applies to Ethereum. If Ethereum's post-merge supply dynamics do not produce analogous timing regularity, the mechanism is Bitcoin-specific (halving-dependent) rather than a general crypto market structure effect.
6. **Fee/cost sensitivity:** If realistic trading costs, funding rates, or position-sizing constraints erode the out-of-sample crossover result, the strategy's practical edge is diminished. This test is not performed by the paper.
7. **Block-height replication:** The paper shows that expressing the clock in block height (the protocol's native unit) preserves the top-timing regularity while partially rescuing bottom timing. Falsification: if block-height clock fails to replicate the day-based result, the regularity is an artifact of day-counting rather than protocol structure.

## Crypto portability

**Not applicable.** This strategy is Bitcoin-specific. The halving mechanism is unique to Bitcoin's proof-of-work protocol; proof-of-stake chains (Ethereum, Solana, etc.) do not have analogous fixed-supply-reduction events. The paper claims the framework may apply to Ethereum post-merge, but no empirical evidence is provided.

Portability to other Bitcoin-denominated products (perpetuals, options, ETFs) is conceptually direct — the clock coordinate is identical — but the SPRING deviation may differ depending on the product's tracking of spot price.

## Limitations

- **N=3 mature cycles:** The single most critical limitation. Three data points cannot establish statistical robustness. The paper explicitly acknowledges this and uses descriptive rather than inferential claims for per-epoch results.
- **Post-hoc window choice:** The danger zone (525–546 days) was identified after observing the pattern. The full variant grid mitigates but does not eliminate this degrees-of-freedom concern.
- **Amplitude compression limits future alpha:** If SPRING continues to compress, the risk-reward of cycle-top timing deteriorates — the clock becomes more predictable but the payoff smaller.
- **No execution layer:** The paper validates timing but does not construct a tradeable strategy with entry/exit rules, position sizing, or cost accounting.
- **Single-author, no peer review:** The paper has not been independently reviewed or replicated.
- **Bottom timing unconfirmed:** The clock provides no actionable signal for cycle bottoms, limiting it to a partial (top-only) timing tool.
- **data gap:** The paper does not report Sharpe ratio, maximum drawdown, or other standard strategy metrics for a hypothetical timing strategy.
- **data gap:** The paper does not model funding, spread, slippage, or execution constraints for perpetual futures.
- **data gap:** The paper's power-law exponent fitting uses expanding estimation; the sensitivity of results to the fitted exponent is not fully explored.

## Implementation status

Not implemented. No PyBroker, Nautilus, or live trading components have been created. This is a research-only capture of the Molnar (2026) timing framework.

## Adoption boundary

This record is research material only. A record being present in this repository does NOT mean:
- The halving clock timing signal is profitable
- The signal has been validated for live trading
- The signal is approved for implementation
- The signal is approved for paper trading or testnet

The signal's practical value is constrained by: (1) N=3 cycles, (2) amplitude compression reducing future alpha, (3) no execution/cost analysis, and (4) single-author provenance.

## Related Wiki records

- [[bitcoin-onchain-mvrv-zscore-cycle-reversal-2026-08-31]] — MVRV Z-score is one of the price-anchored indicators the paper shows has failed. The halving clock provides a time-based complement.
- [[bitcoin-onchain-nupl-macro-cycle-2026-09-01]] — NUPL is another price-based cycle indicator that the paper's amplitude-compression thesis predicts will degrade.
- [[bitcoin-intraday-time-series-momentum-volume-session-2026-08-31]] — Contrasts with the paper's multi-year cycle timing: this record addresses intraday momentum, a different timescale.
- [[crypto-mofe-fourier-neural-operator-mixture-of-experts-crypto-forecasting-2026-09-01]] — Also references halving cycle as a frequency component; the Molnar paper argues the halving is a time anchor, not just a frequency.

## Sources

1. Molnar (2026), "Bitcoin Runs on a Clock: Why Every Price Indicator Dies and the Halving Clock Doesn't," arXiv:2607.26188v1 [q-fin.ST], July 28, 2026. DOI: [10.48550/arXiv.2607.26188](https://doi.org/10.48550/arXiv.2607.26188). URL: https://arxiv.org/abs/2607.26188.
2. GitHub repository: BitcoinDaily/bitcoin-runs-on-a-clock, commit SHA `c5d4a6e60ae1ab020db88b758fcb7c1f997e6e89` (v1.6, July 30, 2026). URL: https://github.com/BitcoinDaily/bitcoin-runs-on-a-clock.
3. Coin Metrics community data series: CapMVRVCur (MVRV ratio), IssTotUSD (daily issuance value).
