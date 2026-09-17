---
schema: strategy-research-record-v1
title: "Apparent Alpha in Daily Bitcoin Short Strangles: Strike-Distance Choice and SPA Correction"
created: 2026-09-18
updated: 2026-09-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto-options
  - negative-result
  - bitcoin
  - volatility-selling
status: research-only
confidence: medium
source_as_of: 2026-09-18
sources:
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7066609"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Apparent Alpha in Daily Bitcoin Short Strangles: Strike-Distance Choice and SPA Correction

## Provenance

- **Authors:** Hongzhe Wen (Olin Business School, Washington University in St. Louis), Xitian Yu (Washington University in St. Louis)
- **Title:** "Apparent Alpha in Daily Bitcoin Short Strangles: Strike-Distance Choice and SPA Correction"
- **Source type:** SSRN working paper (preprint, not peer-reviewed)
- **SSRN ID:** 7066609
- **Posted:** 6 Jul 2026
- **Pages:** 9
- **URL:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7066609
- **Primary data:** Deribit BTC option transactions, Binance BTC spot data, Deribit settlement prices, from 2020 onward
- **Panel:** 1,800 eligible options; daily panel constructed under listed-strike tolerance rules, bid-side entry proxies, taker fees, settlement exits, liquidity filters, fallback treatment, and no-trade handling

## Economic mechanism

### Source-reported

The authors investigate whether strike-distance choice (moneyness offset from ATM) generates statistically reliable outperformance in systematic one-day Bitcoin short strangles. The paper constructs a realistic backtest panel with listed-strike tolerance rules, bid-side entry proxies, taker fees, settlement exits, liquidity filters, fallback treatment, and no-trade handling — then evaluates fixed-distance, rolling best-fixed, and state-dependent rules using Hansen's Superior Predictive Ability (SPA) test with stationary bootstrap.

Fixed-distance results show that strike placement is economically meaningful: mean returns, positive-return rates, tail risk, pair availability, and fallback usage vary across moneyness. The strongest uncorrected candidate is the 5.0% fixed distance.

However, the consistent SPA p-value is 0.2543, so no tested rule is statistically superior to ATM at the 10% level.

### Research interpretation

This is a **negative/decomposition result**: the apparent alpha observed in systematic short-dated Bitcoin short strangle backtests may reflect implementation choices (strike-distance selection, liquidity treatment, fallback rules) rather than a stable economic edge. The paper contributes a methodological warning: in crypto options volatility-selling strategies, backtest outperformance can emerge from specification search and data-snooping rather than genuine risk premia harvesting.

The economic mechanism being tested is the **volatility risk premium (VRP)** — the tendency for implied volatility to exceed realized volatility, allowing systematic option sellers to collect premium. This paper finds that while VRP may exist in Bitcoin options, the specific implementation of a short strangle strategy (particularly strike-distance choice) can create apparent alpha that does not survive rigorous multiple-testing correction.

## Signal

- **Strategy type:** Systematic daily short strangle on BTC options (Deribit)
- **Holding period:** 1 day (settlement exit)
- **Strike selection:** Fixed-distance from ATM (tested distances include 5.0% and others)
- **Entry:** Bid-side proxy under listed-strike tolerance rules
- **Exit:** Settlement (Deribit settlement prices)
- **Liquidity filters:** Applied; fallback treatment for illiquid strikes
- **No-trade handling:** Explicit
- **Evaluation:** Hansen's SPA test with stationary bootstrap for data-snooping correction

**Parameter source:** All parameters and implementation details are source-reported from the paper's abstract. Full parameter details require reading the 9-page paper.

**Underspecified:** Exact strike distances tested beyond 5.0%, exact rolling/state-dependent rule specifications, exact fee model beyond "taker fees", exact liquidity filter thresholds — all require full-text access.

## Required data

- **Instrument:** BTC options on Deribit (listed strikes, American-style implied tolerance)
- **Venue:** Deribit (options), Binance (spot reference)
- **Market type:** Crypto options (Deribit settlement)
- **Timeframe:** Daily panel
- **Fields:** Option transaction prices (bid-side), BTC spot prices (Binance), Deribit settlement prices
- **Sample period:** 2020 onward (exact end date not stated in abstract)
- **Universe:** 1,800 eligible BTC options

## Execution assumptions

- **Signal-to-order timing:** Bid-side entry proxy (conservative)
- **Fees:** Taker fees applied (exact rate not stated in abstract)
- **Slippage/spread:** Bid-side entry assumes execution at bid (conservative for sellers)
- **Fill model:** Not stated in abstract; full-text required
- **Liquidity:** Liquidity filters and fallback treatment applied
- **Settlement:** Deribit settlement prices used for exit
- **Leverage/margin:** Not stated in abstract

## Evidence

### Source-reported

- Fixed-distance results show that strike placement is economically meaningful: mean returns, positive-return rates, tail risk, pair availability, and fallback usage vary across moneyness (source-reported from abstract)
- The strongest uncorrected candidate is the 5.0% fixed distance (source-reported from abstract)
- Hansen's SPA test with stationary bootstrap: consistent SPA p-value = 0.2543 (source-reported from abstract)
- No tested rule is statistically superior to ATM at the 10% level (source-reported from abstract)

All performance figures above are from the paper's abstract only. Full-table performance breakdowns (returns, hit rates, CVaR, fallback rates by strike distance) require reading the full 9-page paper.

### Independently reproduced

Not independently reproduced.

### Negative evidence

This paper IS the negative evidence. Its core finding is that apparent alpha in short-dated crypto option backtests can reflect liquidity treatment and specification search rather than genuine economic edge. The SPA p-value of 0.2543 (well above any conventional significance threshold) means the apparent outperformance of fixed-distance short strangles over ATM does not survive data-snooping correction.

## Falsification plan

- **Out-of-sample test:** Apply the same SPA-corrected framework to a genuinely out-of-sample period (post-publication data) to confirm that the null (no rule superior to ATM) holds
- **Fee sensitivity:** Stress-test with higher taker fees, wider spreads, and realistic slippage to see if the already-null result worsens
- **Strike-distance sweep:** Extend the moneyness grid beyond the tested distances to confirm that no distance consistently survives SPA correction
- **Regime breakdown:** Test whether VRP harvesting (short strangles) performs differently in high-vol vs. low-vol regimes; if alpha is regime-dependent, it may be too fragile to trade
- **Alternative options strategies:** Compare short strangles against short strangles, iron condors, and put spreads to determine if the null result is specific to the strangle structure or general to all short-vol strategies on BTC

## Crypto portability

direct — This study is already conducted on crypto (BTC options on Deribit). The results are directly applicable to crypto options markets.

Key crypto-specific considerations:
- Deribit is the dominant BTC options venue; liquidity and settlement rules may differ from other venues
- The 24/7 crypto market structure means daily settlement cycles differ from traditional options
- BTC options skew and term structure may differ from equity options, affecting strangle construction

## Limitations

- **Abstract-only access:** Full 9-page paper not read; detailed parameter specifications, exact sample period end date, exact fee rates, full performance tables, and detailed liquidity filter rules are underspecified
- **Single asset:** Results are for BTC only; generalizability to ETH or other crypto options is not established
- **Single venue:** Results are for Deribit only; venue-specific liquidity and settlement rules may affect generalizability
- **Working paper:** Not peer-reviewed; methodology and conclusions may change upon revision
- **Short sample:** "2020 onward" — sample period may be too short for robust conclusions about regime-dependent VRP
- **No independent reproduction:** Results are source-reported only

## Implementation status

not-implemented. This is a research-only capture of a negative/decomposition result. No implementation in our research stack.

## Adoption boundary

This record is research-only. Its presence does not mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

The paper's core message is cautionary: apparent alpha in short-dated crypto option backtests may be an artifact of implementation choices rather than genuine edge.

## Related Wiki records

- [[quant/bitcoin-options-volatility-risk-premium-zscore-2026-08-31]] — Related VRP-based crypto options strategy; this paper's negative finding is directly relevant to VRP harvesting strategies
- [[quant/bitcoin-options-implied-volatility-risk-reversal-skew-2026-09-01]] — Related BTC options implied volatility research
- [[quant/crypto-options-dvol-iv-premium-shock-spot-predictor-2026-09-13]] — Related crypto options IV premium research

## Sources

1. Wen, H. & Yu, X. (2026). "Apparent Alpha in Daily Bitcoin Short Strangles: Strike-Distance Choice and SPA Correction." SSRN Working Paper, SSRN 7066609. Posted 6 Jul 2026. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7066609
