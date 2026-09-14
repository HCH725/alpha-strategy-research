---
schema: strategy-research-record-v1
title: "Polymarket Favorite-Longshot Bias: Longshot Losses and Favorite Gains Robust in Crypto and Politics"
created: 2026-09-14
updated: 2026-09-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - prediction-market
  - polymarket
  - favorite-longshot-bias
  - binary-contract
  - event-structure
  - trader-heterogeneity
status: research-only
confidence: medium
source_as_of: 2026-09-11
sources:
  - "Marcos Cardozo and José Ignacio Rivero-Wildemauwe, 'The Favorite-Longshot Bias in Prediction Markets: Evidence from Polymarket', arXiv:2609.12878v1 [econ.GN], September 11, 2026. https://arxiv.org/abs/2609.12878"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Polymarket Favorite-Longshot Bias: Longshot Losses and Favorite Gains Robust in Crypto and Politics

## Provenance

- **Source**: arXiv:2609.12878v1 [econ.GN]
- **Authors**: Marcos Cardozo, José Ignacio Rivero-Wildemauwe (Universidad Católica del Uruguay)
- **Version**: v1, submitted September 11, 2026
- **DOI**: https://doi.org/10.48550/arXiv.2609.12878
- **URL**: https://arxiv.org/abs/2609.12878
- **Full text HTML**: https://arxiv.org/html/2609.12878v1
- **Sample period**: November 11, 2022 through March 29, 2026
- **Data**: Polymarket Users dataset version 1.3 (Akey et al. 2026; Grégoire 2026) — reconstructed completed trades from Polymarket public records; 588 million trades by 2.48 million wallets
- **Instruments**: Polymarket YES/NO binary event tokens; analysis restricted to two-outcome child markets with known resolution by March 29, 2026
- **Funding**: Not stated as externally funded in the preprint

### Repository Deduplication Audit

Repository-wide search on 2026-09-14 found zero prior records citing `arXiv:2609.12878`, Cardozo, Rivero-Wildemauwe, or the Polymarket favorite-longshot bias with parent-event aggregation. Adjacent Polymarket records cover materially different constructions:

- `crypto-cross-platform-binary-threshold-mispricing-polymarket-binance-2026-09-01.md` — option-implied binary fair value vs Polymarket Yes price (Portnaya 2026)
- `polymarket-binance-high-frequency-binary-lead-lag-2026-09-02.md` — high-frequency lead-lag between venues
- `polymarket-binary-mean-reversion-cost-sensitivity-2026-09-14.md` — mean-reversion on three named speculative contracts under cost stress (Vojtko & Dujava 2026)
- `prediction-market-proper-betting-accuracy-profit-conversion-2026-09-02.md` — converting forecasting accuracy into profit under scoring rules
- `prediction-market-llm-confidence-weighted-value-bet-2026-09-04.md` — LLM confidence-weighted value bets

None of these normalize the classic favorite-longshot bias at both price tails, nor the parent-event vs child-market aggregation sensitivity that is the paper's central measurement result.

## Economic mechanism

### Source-reported

The favorite-longshot bias (FLB) is the longstanding empirical regularity that bets on unlikely outcomes earn lower average returns than bets on more likely ones. Cardozo and Rivero-Wildemauwe document FLB at both price tails on Polymarket and show that the measured longshot return depends on the unit of aggregation:

1. **Equal child-market weight**: purchases below 10 cents lose 6.30%; purchases at or above 90 cents earn 0.277% (both significant at the 0.1% level).
2. **Dollar-weighted (pooled) returns**: longshots lose 19.35% and favorites earn 0.83%. The pooled longshot estimate is economically large; its 95% confidence interval includes zero.
3. **Equal parent-event weight**: longshots earn +4.09%, while favorites continue to earn positive returns.

The reversal is driven by two forms of concentration: parent events with many child markets tend to have lower longshot returns (explaining the equal-child-market negative), and parent events attracting the most longshot spending also tend to have lower returns (explaining the pooled negative).

Category heterogeneity is material: Crypto and Politics display longshot losses and favorite gains under both primary calculations. Sports is the clearest exception — longshots earn positive returns under both calculations and favorite returns are not consistently positive. Finance, Culture, Tech, and Weather results depend on weighting; Weather longshot returns change sign.

Longshot losses persist across wallet experience levels, purchase methods (including maker-posted offers), markets without reported fees, and events with shared collateral. Recurrent longshot buyers (top decile by past longshot demand) account for 26.6% of next-month low-price purchases but earn similar returns to others. Recurrent favorite buyers account for 15.1% of next-month high-price purchases but earn less than other favorite buyers.

### Research interpretation

The economic channel is a combination of probability misperception and/or risk-love / lottery preference concentrated in low-price binary claims, with an event-structure measurement trap: parent events that spawn many near-mutually-exclusive child markets (e.g., multi-candidate elections) mechanically create many longshot tickets, and equal-weighting those child markets overstates how often the aggregate longshot portfolio "should" lose relative to a parent-event-level view. For a research-proposed trading interpretation, the robust across-primary-calculations two-sided pattern in **Crypto and Politics** is the portable edge candidate: systematically avoid buying longshots (price < 0.10) and/or prefer favorites (price ≥ 0.90) within those categories. The Sports counterexample is important negative evidence that FLB is not a universal property of all binary event claims.

This is not a mechanical arbitrage: the source is descriptive of realized purchase-to-resolution returns, not a net-of-fees executable strategy. Liquidity, early exit, and settlement delay are not modeled as a strategy.

## Signal

### Formation timestamp

Signals are formed from Polymarket completed purchase records and market metadata as of each trade time. No additional lookback beyond prior wallet trading history is required for the core price-tail classification. Classification of a wallet as a recurrent longshot/favorite buyer uses only purchases completed before the measurement month (point-in-time prospective design).

### Lookback

- **Core FLB measurement**: no lookback. Each resolved purchase is classified by the average purchase price relative to the 10-cent / 90-cent tails.
- **Wallet tail-demand classification**: previous calendar months only; top decile by past share of dollars spent on longshots (or favorites). Experience group uses purchase dollars, active months, distinct child markets traded, and days since first observed trade over the preceding six calendar months.

### Entry (source-reported measurement construction)

For each completed purchase f in a resolved two-outcome child market:

- Price paid per token: p_f ∈ (0, 1)
- Final payoff: y_f ∈ {0, 1}
- Return: r_f = (y_f − p_f) / p_f

Longshot definition: purchases with average price below 10 cents. Favorite definition: purchases at or above 90 cents (symmetric tail thresholds; endpoint exclusions discussed in Appendix A).

### Entry (research-proposed operationalization)

A research-proposed long-only favorite tilt in Polymarket Crypto and Politics categories:

1. At decision time, among open two-outcome child markets in Crypto or Politics with adequate book depth, compute mid or last purchase price for YES and NO sides.
2. **Longshot filter (research-proposed)**: do not buy any ticket with purchase price < 0.10.
3. **Favorite preference (research-proposed)**: if taking a binary position, prefer sides priced ≥ 0.90, subject to depth and expected hold-to-resolution capacity.
4. Prefer parent-event-normalized evaluation when sizing or scoring: equal-weight parent events, not child markets, when measuring portfolio-level longshot exposure.

This operationalization is research-proposed. The source does not specify a standalone trading rule.

### Exit

The source measures hold-to-resolution returns. A research-proposed exit is hold to resolution for favorites with near-certain settlement, or exit when mid price leaves the favorite band (≥ 0.90) by a pre-specified margin. The source does not specify exit rules; early-exit liquidation risk and bid-ask costs are unmodeled.

### Holding period

Variable: from purchase to market resolution. Markets have heterogeneous time-to-resolution. Returns are not annualized and do not adjust for time to resolution (`source-reported`).

### Parameters

- **Longshot threshold**: price < 0.10 (`source-reported` measurement definition)
- **Favorite threshold**: price ≥ 0.90 (`source-reported` measurement definition)
- **Buyer wash filter**: exclude purchases where buyer counterparty Herfindahl-Hirschman index ≥ 0.5 (`source-reported`)
- **Market restriction**: two-outcome child markets only (`source-reported`)
- **Resolution cutoff**: markets resolved by March 29, 2026 (`source-reported`)
- **Research-proposed category gate**: Crypto and Politics only; exclude Sports (`research-proposed`)

## Required data

- **Instrument**: Polymarket YES/NO binary event tokens (USDC-denominated during sample)
- **Universe**: Resolved two-outcome child markets; parent-event labels; category labels (Sports, Crypto, Finance, Politics, Tech, Culture, Weather, Untagged)
- **Venue**: Polymarket (CLOB prediction market)
- **Timeframe**: Transaction-level completed trades (not full order-book quotes)
- **Fields**: trade timestamp, market/token id, price, quantity, buyer/seller wallet, maker flag, market wording/category/parent event, open/close dates, winning token
- **Point-in-time**: Wallet tail-demand and experience classifications use only pre-month information; wash filter uses counterparty HHI on buyer side
- **Timestamp**: As recorded by Polymarket public records in the reconstructed Users dataset v1.3
- **Missing-data**: Markets unresolved by March 29, 2026 excluded from return sample (~5% of amount paid). Some token creation/redemption/transfer paths are not in the completed-trade data (`source-reported`)
- **Funding/fee/spread needs**: Reported fees and shared-collateral metadata partially covered; strategy-level fee/slippage modeling not provided by the source

## Execution assumptions

- **Order type / fill model**: Not modeled as a strategy. Source analyzes completed purchases only.
- **Latency**: Not modeled.
- **Signal-to-order delay**: Not modeled for a trading rule.
- **Liquidity / capacity**: Longshot dollars are relatively small ($273.6M resolved longshot purchases vs multi-billion favorite purchases). Parent-event concentration implies capacity is limited and uneven.
- **Fees / slippage / spread**: Source tests whether losses persist in markets without reported fees and with shared collateral; they do. A net executable strategy still requires live book and fee assumptions not provided by the paper.
- **What the source assumes**: Hold-to-resolution return identity r = (y−p)/p on observed purchase prices.
- **What the Scout independently assumes for research-proposed entry**: that a pre-declared favorite tilt and longshot filter can be implemented with limit orders that fill at or better than the paper's observed purchase prices — this is unverified.

## Evidence

### Source-reported

All figures from Cardozo & Rivero-Wildemauwe (arXiv:2609.12878v1, September 11, 2026):

**Sample construction (Table 1)**:
- Observed transactions: 588,287,492; amount paid $24.63B
- After transaction/market/wash restrictions: 586.1M purchases, $23.67B
- Resolved return sample: 560.9M purchases, $22.49B (95.0% of amount paid)

**Primary return estimates**:
- Equal child-market weight: longshots −6.30%, favorites +0.277% (p < 0.001 both)
- Dollar-weighted: longshots −19.35%, favorites +0.83%
- Equal parent-event weight: longshots +4.09%; favorites positive
- Excluding largest 1 / 5 / 10 parent events: pooled longshot return moves from −19.35% to −15.8% / −14.5% / −10.6%

**Category (primary calculations)**:
- Crypto and Politics: longshot losses and favorite gains under both primary calculations
- Sports: longshots positive under both calculations; favorites not consistently positive
- Finance, Culture, Tech, Weather: depend on weighting; Weather longshot sign flips

**Wallet heterogeneity (Section 6)**:
- Top-decile past longshot buyers: 26.6% of next-month low-price purchases; returns similar to other longshot buyers
- Top-decile past favorite buyers: 15.1% of next-month high-price purchases; earn less than other favorite buyers

**Trading-condition robustness (Section 5)**:
- Longshot losses appear at every experience level and under all purchase methods, including maker-posted offers
- Persist in markets without reported fees and in events with shared collateral

**Hold-to-resolution vs later sale (Appendix F Table 25, longshots)**:
- All resolved longshots: $273.577M paid, −$52.930M terminal, −19.35%
- Buyer later sells same token: $173.864M paid, +0.12% terminal
- No later recorded sale: $99.713M paid, −53.30% terminal

**Category dollar shares (Table 2)**: Crypto 67.2% of purchases / 25.2% of dollars; Sports+Politics 25.4% of purchases / 65.3% of dollars.

### Independently reproduced

`not independently reproduced`

The paper reports an independent reconstruction of resolved signed terminal PnL for a deterministic sample of 9,781 wallets (Spearman 0.9926 with released wallet summary; sign agreement for every wallet in the top 1% by absolute reconstructed profit/loss; reconciles within $1 for 96.4% of the sample). That is an internal data-quality reconciliation of the Users dataset, not a Scout-independent reproduction of the FLB return estimates.

### Negative evidence

- **Sports category**: two-sided FLB absent; longshots earn positive returns under both primary calculations. This is direct source-reported counterexample to a universal FLB claim.
- **Aggregation sensitivity**: equal parent-event weighting flips longshot returns from negative to +4.09%. Any naive equal-child-market portfolio interpretation is measurement-fragile.
- **Pooled longshot CI**: 95% confidence interval for the dollar-weighted longshot estimate includes zero (null-imposed Webb-bootstrap p = 0.184 for longshots; 0.001 for favorites).
- **Recurrence does not identify losers**: recurrent longshot buyers do not earn disproportionately worse returns than other longshot buyers; a simple "stable group of especially loss-prone longshot bettors" account is weakened.
- **Capacity / concentration**: excluding the largest parent events substantially shrinks the pooled longshot loss, indicating the aggregate effect is concentrated in a few large multi-child events.
- **No net-of-cost strategy evaluation**: the paper does not claim an executable favorite-longshot trading strategy after fees, slippage, and early-exit liquidity.

## Falsification plan

1. **Out-of-sample post-March-2026 holdout**. Freeze the 10c/90c tail definitions and Crypto+Politics category gate. On newly resolved Polymarket markets after 2026-03-29, test whether longshot dollar-weighted returns remain negative and favorite returns remain positive. **Research-defined falsification threshold**: if either tail reverses sign for two consecutive quarterly cohorts, reject the proposed category-gated FLB edge.
2. **Aggregation pre-registration**. Pre-declare primary unit as parent-event equal weight and secondary as dollar weight. If the edge only appears under equal child-market weight, treat it as event-structure artifact, not alpha.
3. **Placebo: Sports FLB**. Run the identical pipeline on Sports. If Sports longshots turn reliably negative with the same thresholds, the category gate is misspecified; if they stay positive, the gate is informative.
4. **Fees / spread stress**. Reprice using executable bid/ask rather than trade price, and add any platform fees/rewards. **Research-defined falsification threshold**: favorite edge ≤ 0 after half-spread and fees; longshot avoid benefit persists only as avoided loss, not positive alpha.
5. **Parent-event size ablation**. Recompute returns excluding the top 1 / 5 / 10 parent events by longshot dollars. If the sign of the dollar-weighted longshot loss is unstable, do not claim a broad FLB, only event-concentrated losses.
6. **Wash-trading filter sensitivity**. Vary counterparty HHI threshold (0.3 / 0.5 / 0.7). If tail returns flip under reasonable wash filters, the result is measurement-sensitive.
7. **Wallet-split pseudo-live test**. Use only pre-cutoff wallet history to select favorite-side tickets, trade forward without using contemporaneous wallet classifications. Reject if the prospective portfolio does not reproduce the descriptive tail ranking.
8. **Competing explanation: settlement-time lottery**. Condition on time-to-resolution at purchase. If FLB is concentrated only in very short-dated or very long-dated contracts, the mechanism may be maturity-specific rather than a stable price-tail bias.

## Crypto portability

**Direct** for Polymarket Crypto-category binary contracts; **adapted** for other crypto prediction venues.

- The source is already a crypto-native prediction market. Crypto is the largest category by purchase count (67.2%) and shows the two-sided FLB pattern robustly under both primary calculations.
- Spot/perpetual/futures/options distinction: this is a **binary event claim**, not a linear perpetual. Settlement is 0/1 at event resolution; funding, mark-price, and liquidation engines do not apply in the same way as perps.
- 24/7 timestamping: Polymarket trades continuously; no equity session gaps.
- Venue fragmentation: Kalshi and other prediction markets may exhibit different FLB (the paper cites Bürgi et al. 2026 documenting FLB variation across makers/takers on Kalshi). Cross-venue portability is unproven without re-measurement.
- Shared collateral / NegRisk multi-outcome events change the economics of taking the opposite side of a longshot; the paper finds losses persist even when collateral can be shared.
- Liquidity and impact: longshot tickets are thinner; the $273.6M resolved longshot notional is small relative to CEX perp volume.
- Crypto portability is **not** authorization to trade.

## Limitations

- **Descriptive, not a strategy backtest**: hold-to-resolution returns ignore early exit, book depth, and maker/taker fee schedules as a live rule.
- **Aggregation dependence**: headline longshot loss is not invariant to parent-event vs child-market weighting.
- **Concentration**: pooled longshot loss is driven substantially by a few large parent events.
- **Sports counterexample**: undermines any universal FLB claim.
- **Wallet ≠ person**: multiple wallets per person and shared wallets prevent trader-level causal identification.
- **Dataset reconstruction**: relies on Polymarket Users dataset v1.3; some token create/redeem/transfer paths are missing.
- **Recent sample truncation**: markets near March 2026 have less time to resolve, creating coverage bias toward fast-resolving events at the end of the sample.
- **Preprint**: arXiv v1; not peer-reviewed at capture time.
- **Selection on resolution**: return sample includes only markets resolved by the cutoff.

## Implementation status

`not-implemented`

Nothing has been implemented in our research stack. No Polymarket connector, parent-event normalization module, or favorite-tilt portfolio construction code exists here. This record is research capture only.

## Adoption boundary

This record is research material only. Presence in this repository does not mean profitable, validated alpha, or approval for implementation, paper trading, testnet, or live trading. Any later adoption decision must be explicit, separately reviewed, and based on the record plus current live sources.

## Related Wiki records

- [[quant/strategy-research-record-spec-v1]] — canonical schema
- `crypto-cross-platform-binary-threshold-mispricing-polymarket-binance-2026-09-01.md` — different mechanism (option-implied fair value vs prediction-market price)
- `polymarket-binance-high-frequency-binary-lead-lag-2026-09-02.md` — different mechanism (cross-venue lead-lag)
- `polymarket-binary-mean-reversion-cost-sensitivity-2026-09-14.md` — different signal (price-path mean reversion on three contracts) and cost-sensitivity focus
- `prediction-market-proper-betting-accuracy-profit-conversion-2026-09-02.md` — different problem (accuracy-to-profit conversion under scoring rules)
- `prediction-market-llm-confidence-weighted-value-bet-2026-09-04.md` — different signal source (LLM confidence)
- `kalshi-prediction-market-pricing-wedge-executable-spread-falsification-2026-09-13.md` — related venue family (Kalshi), different mechanism

## Sources

1. Marcos Cardozo and José Ignacio Rivero-Wildemauwe. "The Favorite-Longshot Bias in Prediction Markets: Evidence from Polymarket." arXiv:2609.12878v1 [econ.GN], September 11, 2026. https://arxiv.org/abs/2609.12878
