---
schema: strategy-research-record-v1
title: "Cross-Venue Perpetual Funding-Rate Carry: Negative-Results Study on Cost Destruction and Spread Decay"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - funding
  - carry
  - cross-venue
  - negative-result
  - execution-costs
  - decay
status: research-only
confidence: high
source_as_of: 2026-07-30
sources:
  - "David Ayuso Pita, 'Funding Rate Carry: what survives execution costs?', GitHub repository, commit e990265ee3e193afcb2c7aff3c07a615cce5e22d, created 2026-07-29, accessed 2026-09-13. https://github.com/DavidAyusoPita/funding-carry-analysis"
  - "Primary analysis notebook: https://github.com/DavidAyusoPita/funding-carry-analysis/blob/main/notebooks/01_funding_carry_analysis.ipynb"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Venue Perpetual Funding-Rate Carry: Negative-Results Study on Cost Destruction and Spread Decay

## Provenance

- **Repository:** https://github.com/DavidAyusoPita/funding-carry-analysis
- **Full commit SHA:** `e990265ee3e193afcb2c7aff3c07a615cce5e22d` (main branch, only commit lineage)
- **Primary analysis file:** `notebooks/01_funding_carry_analysis.ipynb`
- **Source code files:** `src/fetch.py`, `src/analysis.py`, `src/plots.py`, `src/pipeline.py`
- **Author:** David Ayuso Pita
- **License:** MIT
- **Created:** 2026-07-29
- **Data period:** July 2024 — July 2026 (2 years)
- **Universe:** BTC, ETH, SOL perpetual futures
- **Venues:** Binance, Bybit, OKX (centralised), Hyperliquid (on-chain DEX)
- **Data volume:** 18,208 hourly funding-rate observations per asset-venue pair
- **Data source:** Public REST endpoints (no API keys required)
- **All data and figures are git-ignored or generated; the notebook is committed with outputs.**

## Economic mechanism

### Source-reported

The author frames the study around a specific question: perpetual futures pay periodic funding between longs and shorts, so a delta-neutral position (long one venue's perpetual, short another's) is directionally flat yet collects the funding-rate difference. The study asks how much of that structural spread survives execution costs and what risk is actually being compensated.

### Research interpretation

This is a **negative-results study**, not an alpha-strategy claim. The economic mechanism under test is: cross-venue funding-rate spreads represent a harvestable structural carry. The study finds the mechanism is real but the harvesting cost exceeds the carry for all but the most passive approaches, and the spread itself is decaying. The study is designed with three methodological safeguards: (1) an exchange-versus-exchange control where no structural difference should exist; (2) a cost ladder across four execution profiles; (3) a quarterly decay check. The key insight is that the signal's *direction* is a regime lasting months, but its *level* mean-reverts within hours, making active harvesting self-defeating.

## Signal

### Source-reported

Two decision rules are tested:

1. **Active rule (threshold entry):** Enter when the trailing CEX-vs-DEX funding spread exceeds 10% annualized. This maximizes gross income but is destroyed by costs.

2. **Patient rule (low-frequency rebalance):** Hold the delta-neutral carry position continuously, revisiting only *which* venue to short, on a 30-day rebalance clock. This barely trades (1–5 round trips over 2 years).

Parameters are research-defined decision rules, not optimised thresholds. The 10% threshold for the active rule and the 30-day rebalance for the patient rule are not derived from the data; they are structural choices to test two extremes of harvesting frequency.

### Research interpretation

The signal tested is the **cross-venue funding-rate spread** (CEX vs DEX), not a directional price signal. The two rules represent extremes: maximum harvesting frequency vs minimum frequency. The result is that frequency is the dominant determinant of net return, not the spread level itself.

## Required data

- **Instruments:** BTC, ETH, SOL perpetual futures
- **Venues:** Binance, Bybit, OKX (CEX), Hyperliquid (DEX)
- **Market type:** USDT-margined perpetual futures
- **Timeframe:** Hourly funding-rate observations (funding settlement timestamps aligned backwards)
- **Fields:** Funding rate (per period), funding settlement timestamp, spot/perpetual mid-price (for spread measurement)
- **Point-in-time:** Funding rates are public and settlement-aligned; the author normalizes rates to per-hour fractions and aligns by settlement window (not forward-fill)
- **Timestamp:** UTC, aligned by settlement time (rate stamped 08:00 pays for window ending at 08:00)
- **Missing-data:** OKX publishes only 3 months of history; excluded from two-year comparisons. Binance moves volatile symbols to 4-hour funding schedules; the code infers the interval from timestamps rather than assuming a constant.
- **Data availability:** All data from public REST endpoints; no API keys needed. Cached locally.

## Execution assumptions

### Source-reported

- **Round-trip cost:** 13 bps across four crossings (open + close on each leg, CEX + DEX)
- **Cost ladder:** Four execution profiles tested — retail taker fees, mid-tier, maker tier, and on-chain maker tier
- **Break-even holding period for active rule:** 100–135 hours (given 13 bps round-trip)
- **Margin/leverage:** Not modeled; returns are stated on notional, not on deployed capital
- **Liquidation:** Not modeled; the author explicitly notes this as a limitation
- **Slippage:** Modeled as the observed price gap between venues at execution; additional slippage beyond the gap is assumed, not observed
- **Funding caps:** Not modeled; venues bound their rates, truncating extreme observations
- **Counterparty/protocol risk:** Not modeled; exchange failure and contract failure are real but excluded

### Research interpretation

The cost model is deliberately conservative for the active rule (assumes taker fees) and deliberately generous for the patient rule (assumes minimal trading). The 13 bps round-trip is a realistic estimate for a four-crossing trade (CEX open, DEX open, CEX close, DEX close) with mixed maker/taker fills. The key finding is robust to the cost ladder: the active rule loses money at every cost profile except the most optimistic, and even then barely breaks even.

## Evidence

### Source-reported

**Finding 1 — Structural bias is real:**
- On-chain venue (Hyperliquid) pays more than CEX in 65–72% of hours
- Annualized absolute spread: 8.5–11.4%
- Exchange-vs-exchange control: centered on zero, sign is a coin flip (41–47% stability)
- Source: README Findings section, confirmed in notebook outputs

**Finding 2 — Mean-reversion destroys timing:**
- AR(1) half-life of CEX-vs-DEX spread: 1.5–3.5 hours
- Round-trip cost: 13 bps requires 100–135 hours of holding to repay
- Source: README Findings section, confirmed in notebook

**Finding 3 — Active trading destroys carry:**
- Threshold entry at 10% annualized trailing spread: earns most gross income of any rule tested
- Net annualized return: −9% to −15% (after costs)
- Execution consumed roughly 3× the gross income
- Source: README Findings section

**Finding 4 — Patient rule barely works:**
- 30-day rebalance: +2.7% to +5.4% annualized net on notional
- 1–5 round trips over 2 years
- Maximum drawdown: under 2%
- Break-even round-trip cost tolerance: above 250 bps
- Source: README Findings section

**Finding 5 — Spread is decaying:**
- Average spread 20–35% lower in year 2 vs year 1
- 45–60% below late-2024 peak
- Source: README Findings section, confirmed in decay figure

**Finding 6 — Cost ladder:**
- Active rule: dies above 8 bps round-trip (no room for bad fills or fee-tier changes)
- Patient rule: tolerates round-trip cost above 250 bps before break-even
- Cheaper execution buys "permission to be wrong about frequency" — drags active rule from −24%/yr to roughly break-even, which is not an edge
- Source: README cost ladder figure and analysis

### Independently reproduced

Not independently reproduced. This is a single-source study using public data. The analysis is reproducible from the committed notebook and code.

### Negative evidence

This entire record is a negative-result study. The primary finding is that cross-venue funding carry, while structurally real, is almost entirely untradable after costs when actively harvested. The spread is decaying over time, suggesting competitive compression. The only rule that survives net of costs is one that barely trades (1–5 round trips over 2 years), and even then the return is thin (2.7–5.4% annualized on notional, not on capital) and uncompensated for venue, protocol, and liquidation risk.

## Falsification plan

This record is itself a falsification study. The falsification framework built into the source is:

1. **Control test:** Exchange-vs-exchange spread should be centered on zero with random sign — confirmed. Without this control, the CEX-vs-DEX bias could be measurement noise.
2. **Cost ladder:** Every rule run at four execution profiles — a conclusion that survives only at one fee assumption is not a conclusion. The active rule fails at every profile except the most optimistic.
3. **Decay check:** Two-year average split by quarter — a market being competed away looks profitable on average right up until it isn't. Confirmed: spread is decaying.
4. **Holding-period break-even:** The active rule requires 100–135 hours of holding to repay costs, but the spread's half-life is 1.5–3.5 hours — structural impossibility of profitable active harvesting.

**What would weaken the negative finding:**
- Discovery that the patient rule's +2.7–5.4% annualized is material after accounting for capital deployment, margin requirements, and opportunity cost
- Evidence that the decay trend reverses or stabilizes
- Identification of sub-assets or sub-venues where the spread is wider and more persistent
- Realized slippage measured from order-book snapshots rather than assumed price gaps

## Crypto portability

direct

The study is conducted entirely on crypto perpetual futures across CEX and DEX venues. The findings are native to crypto market structure (funding-rate mechanism, 24/7 settlement, cross-venue fragmentation).

**Crypto-specific considerations:**
- Funding-rate mechanism is specific to perpetual futures; no TradFi equivalent
- 24/7 settlement means funding accrues continuously
- CEX vs DEX venue fragmentation creates the structural spread
- Cross-venue capital transfer friction is a real cost not fully captured
- Venue counterparty risk and protocol risk are real but excluded from the model
- The decay trend may accelerate as more participants enter the carry trade

## Limitations

- **Returns on notional, not on capital:** Both legs must be collateralised; return on deployed capital depends on margin regime and leverage, which amplifies liquidation risk
- **No liquidation modeling:** Exchange failure and forced liquidation are real, undiversified, and correlated with conditions that make the spread widest
- **Slippage beyond measured price gap is assumed, not observed:** Real fills depend on book depth at execution
- **Funding caps ignored:** Venues bound their rates, truncating extreme observations the strategy would most like to capture
- **Survivorship and selection:** Only three most-liquid assets tested; smaller assets show wider spreads and thinner books (trade-off not measured)
- **OKX history limited to 3 months:** Excluded from two-year comparisons
- **One historical path:** 2 years, 3 assets, 1 regime; nothing establishes out-of-sample persistence
- **Data gap:** The author notes that real fills depend on book depth at the instant of execution, which is not modeled
- **The patient rule tolerates high costs but is barely tested:** 1–5 round trips over 2 years is too few trades for statistical confidence in the positive finding

## Implementation status

not-implemented. No implementation in our research stack. The source itself is a research analysis, not a trading system.

## Adoption boundary

This record documents a negative result: cross-venue funding carry is structurally real but almost entirely untradable after costs. The record being present in this repository does not mean:

- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

The primary value of this record is as a cost-awareness reference and a methodological template for evaluating carry trades.

## Related Wiki records

- [[crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11]] — Tests cross-sectional funding carry factor with net-of-costs evidence; complementary but different mechanism (cross-sectional vs cross-venue)
- [[hyperliquid-cex-cross-venue-funding-spread-carry-2026-09-03]] — Studies the statistical significance of the Hyperliquid-CEX funding spread; the present record tests whether that spread is tradable
- [[crypto-two-tiered-cex-dominant-funding-discovery-structural-arbitrage-2026-09-12]] — Studies CEX-dominant funding price discovery; complementary microstructure perspective

## Sources

1. David Ayuso Pita. "Funding Rate Carry: what survives execution costs?" GitHub repository. Commit `e990265ee3e193afcb2c7aff3c07a615cce5e22d`. Created 2026-07-29. Accessed 2026-09-13. https://github.com/DavidAyusoPita/funding-carry-analysis
2. Primary analysis notebook: https://github.com/DavidAyusoPita/funding-carry-analysis/blob/main/notebooks/01_funding_carry_analysis.ipynb (committed with outputs)
3. Cost ladder figure: https://github.com/DavidAyusoPita/funding-carry-analysis/blob/main/figures/cost_ladder.png
4. Strategy comparison figure: https://github.com/DavidAyusoPita/funding-carry-analysis/blob/main/figures/strategies.png
5. Spread bias figure: https://github.com/DavidAyusoPita/funding-carry-analysis/blob/main/figures/spread_bias.png
6. Decay figure: https://github.com/DavidAyusoPita/funding-carry-analysis/blob/main/figures/decay.png
