---
schema: strategy-research-record-v1
title: "Kalshi BTC Event Contracts as Option-Like Hedges for Spot Crypto Exposure"
created: 2026-09-15
updated: 2026-09-15
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - bitcoin
  - kalshi
  - prediction-market
  - hedging
  - portfolio-construction
  - event-contracts
status: research-only
confidence: low
source_as_of: 2026-09-13
sources:
  - "Prashanth Bhaskara and Aadit Jerfy, 'Public Opinion as an Option: Leveraging Prediction Markets to Hedge Exposure to Spot Crypto Volatility', arXiv:2609.14267v1 [cs.CE, q-fin.TR], September 13, 2026. https://arxiv.org/abs/2609.14267"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Kalshi BTC Event Contracts as Option-Like Hedges for Spot Crypto Exposure

## Provenance

- **Source**: arXiv:2609.14267v1 [cs.CE, q-fin.TR]
- **Authors**: Prashanth Bhaskara, Aadit Jerfy
- **Version**: v1, submitted September 13, 2026
- **DOI**: https://doi.org/10.48550/arXiv.2609.14267
- **URL**: https://arxiv.org/abs/2609.14267
- **Length**: 9 pages, 6 figures
- **Proof of concept**: Bitcoin spot + Kalshi crypto event contracts
- **MSC**: 91G20

### Repository Deduplication Audit

Repository-wide search on 2026-09-15 found zero prior records citing `arXiv:2609.14267`, Bhaskara, Jerfy, or Kalshi event contracts used as **option-like hedges against spot BTC volatility**. Adjacent Kalshi / prediction-market records cover different constructions:

- `kalshi-prediction-market-macro-repricing-volatility-forecasting-2026-09-01.md` — macro repricing / vol forecasting, not hedge overlay
- `kalshi-prediction-market-pricing-wedge-executable-spread-falsification-2026-09-13.md` — pricing wedge / spread falsification
- `crypto-kalshi-prediction-market-macro-repricing-2026-09-01.md` — macro repricing family
- Polymarket FLB / lead-lag / settlement records — different venue and mechanism

This record is a **portfolio hedge overlay** using Kalshi BTC price-event contracts as synthetic options against spot, not a standalone arb or prediction-market mispricing trade.

## Economic mechanism

### Source-reported

Bhaskara and Jerfy treat Kalshi crypto event contracts on Bitcoin's future price as **option-like claims** and construct portfolio allocations that hedge spot BTC volatility without abandoning spot exposure. The paper analyzes three Kalshi event contracts corresponding to different underlying market regimes (bullish, bearish, flat) and reports risk profiles per regime.

The authors state that a **dynamic Kalshi/Bitcoin hedging strategy outperforms more simplistic portfolios across all regimes**. They discuss fees as a future profit-erosion risk and leave directions for further research.

### Research interpretation

The structural idea is: binary event contracts on BTC price thresholds can be combined with spot BTC to create a payoff profile similar to holding spot plus call/put-like protection, at retail-accessible sizes. The claim is hedging efficacy / regime robustness of the mixed portfolio, not a pure alpha long entry. Crypto-native because the hedge leg and the underlying are both BTC-linked event/spot exposure on Kalshi + spot venues.

## Signal

### Formation timestamp

Not specified as a public trading clock in the abstract. The paper constructs allocations from Kalshi event-contract terms and regime analysis; exact decision timestamps should be read from the paper body before any live use.

### Lookback

Not specified in the abstract. Regime classification (bullish / bearish / flat) is used to choose among three event contracts; the regime detection rule is not restated in the abstract.

### Entry (source-reported)

Resource allocation into Kalshi crypto event contracts combined with spot BTC holdings. Three event contracts are analyzed, each tied to a different market regime. A **dynamic** Kalshi/Bitcoin allocation is compared to simpler portfolios.

### Entry (research-proposed operationalization)

`research-proposed`: at each rebalance, (1) classify BTC regime using a pre-registered rule, (2) buy the Kalshi event-contract leg that matches the regime (price-above / price-range / price-below style thresholds as available), (3) hold a residual spot BTC sleeve, (4) size so that hedge notional is a fixed fraction of spot notional. This operationalization is research-proposed; the source paper's exact thresholds, contract IDs, and weight grids must be read from the 9-page body before reconstruction.

### Exit

Event contracts settle at their Kalshi resolution; spot sleeve remains held or is rebalanced on a periodic calendar. Exact exit / rebalance cadence not specified in the abstract.

### Holding period

Event-contract horizon is contract-specific (Kalshi crypto events are typically daily/weekly/monthly windows). Spot sleeve can be held indefinitely. Abstract does not pin a single holding period.

### Parameters

- Hedge instrument: Kalshi crypto event contracts on BTC future price
- Regimes analyzed: bullish, bearish, flat (three contracts)
- Strategy type: dynamic mixed Kalshi + spot allocation vs static/simple portfolios
- Proof of concept: Bitcoin only
- Fees: discussed as future profit erosion; not a full cost model in the abstract

## Required data

- **Instrument**: Spot BTC + Kalshi BTC price event contracts
- **Universe**: Three named Kalshi event contracts (specific IDs in paper body)
- **Venue**: Kalshi (event contracts) + spot BTC venue(s)
- **Timeframe**: Event-contract horizons (short-term retail windows)
- **Fields**: Kalshi mid/last prices for YES/NO legs, spot BTC price
- **Point-in-time**: Regime label and contract selection must be causal; paper body required for exact rule
- **Funding/fee/spread**: Kalshi fees mentioned as eroding future profits; not fully modeled in abstract

## Execution assumptions

- **Order type**: Market orders on Kalshi CLOB + spot
- **Fill model**: Not specified in abstract
- **Latency**: Not specified
- **What the source assumes**: Retail can buy event contracts and hold spot; hedge improves risk profile across three regimes
- **What the Scout does not assume**: No claim of institutional capacity, no full fee/slippage model, no multi-cycle walk-forward validation visible in abstract

## Evidence

### Source-reported

- Three Kalshi event contracts analyzed (bullish / bearish / flat regimes)
- Dynamic Kalshi/Bitcoin hedging strategy **outperforms more simplistic portfolios across all regimes** (source claim)
- Comprehensive risk profile provided per regime (figures in paper)
- Fees discussed as future profit erosion
- Length: 9 pages — exploratory proof-of-concept scale

### Independently reproduced

`not independently reproduced`

### Negative evidence

- Abstract notes fees can **erode profits in the future**
- Only Bitcoin proof of concept; no multi-asset replication in the paper as described
- Short paper; regime definition, contract selection, and walk-forward design not visible from abstract alone
- Event-contract liquidity and Kalshi market depth not analyzed in abstract

## Falsification plan

1. **Regime-blind placebo**. Replace the dynamic regime→contract mapping with a fixed always-hold one contract. **Research-defined falsification threshold**: if fixed contract matches or beats dynamic allocation out-of-sample, reject the regime-adaptive hedge claim.
2. **Fee stress**. Apply full Kalshi fee schedule + spot spread. If net risk-adjusted improvement over spot-only vanishes, treat as pre-fee artifact.
3. **Walk-forward freeze**. Select contracts and weights on period A; freeze for period B. Reject if B's hedge effect does not replicate.
4. **Event-contract depth**. Cap position size to top-of-book depth. Reject if implementable notional cannot hedge a meaningful spot sleeve.
5. **Alternative venue**. Use Polymarket or Deribit options as hedge leg with the same spot sleeve. If only Kalshi works, document venue-specificity.
6. **No-hedge baseline**. Compare to spot-only BTC and to cash-treasury mix. The hedge must improve a pre-registered risk metric (max DD / CVaR), not only multi-regime narrative scores.

## Crypto portability

**Direct** for BTC spot + Kalshi BTC events; **adapted** for other Kalshi crypto events (ETH etc.) if contract terms are comparable.

- 24/7 crypto spot vs Kalshi event resolution clocks — settlement timing mismatch must be modeled
- Kalshi is US-regulated prediction venue; access and fees differ from crypto CEX options
- Event contracts are binary, not linear options — payoff is 0/1, so hedge ratio is nonlinear in price
- No funding rate on Kalshi legs; spot funding on perp sleeve would be a separate adaptation
- Crypto portability is **not** authorization to trade

## Limitations

- Short exploratory paper (9 pages)
- Bitcoin only proof of concept
- Regime / contract selection rules not restated in abstract
- No independent reproduction
- Fee/slippage analysis incomplete
- No institutional capacity or multi-cycle validation visible from abstract
- Preprint (arXiv v1)

## Implementation status

`not-implemented`

No Kalshi connector, regime classifier, or event-contract hedge portfolio exists in our research stack.

## Adoption boundary

This record is research material only. Presence in this repository does not mean profitable, validated alpha, or approval for implementation, paper trading, testnet, or live trading.

## Related Wiki records

- [[quant/strategy-research-record-spec-v1]] — canonical schema
- `kalshi-prediction-market-macro-repricing-volatility-forecasting-2026-09-01.md` — Kalshi macro/vol family
- `kalshi-prediction-market-pricing-wedge-executable-spread-falsification-2026-09-13.md` — Kalshi pricing wedge
- `crypto-kalshi-prediction-market-macro-repricing-2026-09-01.md` — Kalshi macro repricing
- `prediction-market-llm-confidence-weighted-value-bet-2026-09-04.md` — prediction-market value bets
- `polymarket-favorite-longshot-bias-crypto-politics-2026-09-14.md` — Polymarket FLB (different venue/mechanism)

## Sources

1. Prashanth Bhaskara and Aadit Jerfy. "Public Opinion as an Option: Leveraging Prediction Markets to Hedge Exposure to Spot Crypto Volatility." arXiv:2609.14267v1 [cs.CE, q-fin.TR], September 13, 2026. https://arxiv.org/abs/2609.14267
