---
schema: strategy-research-record-v1
title: "Crypto Adjacent-Futures Weekly Basis-Return Reversal"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-05-12
sources:
  - https://ssrn.com/abstract=5250499
  - https://doi.org/10.2139/ssrn.5250499
  - https://www.linkedin.com/posts/alberto-rossi-5b34a22_finance-assetpricing-futures-activity-7338952205510553602-n4tg
  - https://www.cmegroup.com/trading/ether-futures.html.html
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Adjacent-Futures Weekly Basis-Return Reversal

## Provenance

Primary research source: Alberto G. Rossi, Yingguang Zhang, and Yandi Zhu, *Short-Term Basis Reversal*, FEB-RN Research Paper No. 85/2025 / Georgetown McDonough School of Business Research Paper No. 5250499. SSRN states that the paper was posted 14 May 2025 and last revised 12 May 2026. Stable identifiers: SSRN 5250499 and DOI `10.2139/ssrn.5250499`.

The source is traditional-futures research, not cryptocurrency evidence. The authors describe a previously undocumented short-term reversal in the return spread between adjacent futures maturities. Alberto Rossi's public author post states that the anomaly appears week-to-week across commodities and also in stock-index futures, Treasuries, and corporate bonds, and reports simple trading strategies with annual returns up to 18% and Sharpe ratios as high as 1.5. Those performance figures are source-reported author claims and have not been independently reproduced here.

For crypto portability, CME Ether futures are a concrete currently listed term-structure venue: CME states that ETH futures use monthly contracts for six consecutive months plus additional quarterly contracts, so adjacent-expiry return spreads are directly observable. The present record does not claim that the commodity-futures result already holds in CME crypto futures.

Source-identity deduplication performed before writing: repository and Hermes Wiki Brain searches found no record containing SSRN `5250499`, the exact paper title, or the same distinctive mechanism of **weekly reversal in the return spread between adjacent maturities**. Existing basis-level and basis-momentum records are related but materially different signals.

## Economic mechanism

### Source-reported

The authors attribute short-term basis reversal to differential speed and sensitivity with which adjacent maturities incorporate new information. Front and deferred futures do not react identically to news; temporary relative-price dislocations therefore emerge in the return spread and subsequently reverse. The source reports that the effect is stronger for futures with higher return volatility, more autocorrelated individual-contract returns, and lower return correlation across maturities. The paper frames the evidence as consistent with preferred-habitat and limits-to-arbitrage mechanisms rather than ordinary single-contract short-term reversal.

### Research interpretation

The falsifiable crypto hypothesis is a **relative-value term-structure overreaction** effect. If the near contract temporarily overreacts relative to the next contract, the weekly first-minus-second return spread should show negative serial dependence. A spread trader should therefore take the opposite side of the prior week's relative return shock rather than a directional view on the underlying crypto asset.

This mechanism is distinct from:

- static futures basis/carry, which trades the level of futures-versus-spot mispricing;
- basis momentum, which trades persistence in changes in the curve or basis;
- single-contract short-term reversal, which fades an outright return rather than a cross-maturity return differential.

The crypto extension is `adapted`, not source-reported. Crypto-specific limits-to-arbitrage could arise from different liquidity, margin, roll demand, institutional participation, and expiry-specific hedging pressure across adjacent BTC/ETH futures.

## Signal

### Source-normalized core

- **Observed quantity:** weekly return spread between adjacent futures maturities, conceptually `SRet_t = R(F1)_t - R(F2)_t`, where `F1` is the nearest eligible maturity and `F2` the second-nearest eligible maturity.
- **Source direction:** the spread exhibits negative week-to-week autocorrelation; a positive spread in week `t` tends to be followed by a negative spread in week `t+1`, and vice versa.
- **Holding horizon:** one week is directly supported by the author's public description of a week-to-week reversal effect.
- **Underlying exposure:** relative-value between adjacent maturities, not outright crypto direction.

### Crypto test operationalization

The source does not provide crypto-specific contract-selection or execution rules. The following are therefore **research-proposed** for testability and are not source-reported:

1. At a fixed weekly formation timestamp, identify the nearest two non-expired, sufficiently liquid dated futures on the same underlying and venue.
2. Exclude a front contract inside a predefined expiry buffer to avoid expiry-settlement contamination; the exact buffer must be pre-registered in the experiment.
3. Compute simple or log returns for `F1` and `F2` over the immediately preceding seven-day formation window using synchronized prices.
4. Define `SRet_t = R(F1)_t - R(F2)_t`.
5. Trade the next week in the opposite relative direction:
   - if `SRet_t > 0`, **research-proposed** position: short `F1`, long `F2`;
   - if `SRet_t < 0`, **research-proposed** position: long `F1`, short `F2`.
6. Size the two legs to be approximately delta/notional neutral at entry; exact hedge ratio is **research-proposed** and must be fixed before testing.
7. Exit at the next weekly rebalance or earlier only for contract-roll/expiry safety rules defined ex ante.

No source-reported stop-loss, take-profit, leverage, volatility target, rank cutoff, or position-size rule is available for the crypto adaptation. Any such parameter is `research-proposed`.

## Required data

- **Instrument:** dated Bitcoin and/or Ether futures with at least two simultaneously listed maturities on the same venue. Perpetual swaps alone are insufficient because the hypothesis requires an expiry term structure.
- **Universe:** initially BTC and ETH dated futures; extension to other crypto futures only when two adjacent liquid maturities coexist reliably.
- **Venue:** CME is directly suitable because it lists multiple monthly/quarterly Ether futures maturities. Other venues may be tested separately but must not be pooled without venue-specific normalization.
- **Timeframe:** synchronized daily or finer settlement/mark/mid observations sufficient to construct weekly returns; intraday data are required if formation and execution are separated causally.
- **Fields:** contract identifier, expiry, bid/ask or executable quotes, trade/settlement price, volume, open interest, contract multiplier, tick size, fees, margin specification, and reference-index/settlement information.
- **Point-in-time:** contract listings, expiry status, liquidity, and eligible front/second contract must be determined using information available at the formation timestamp only.
- **Timestamp:** one explicit timezone and weekly cutoff must be fixed across both maturities; mismatched closes are not allowed.
- **Missing-data:** do not interpolate missing contract prices. If either leg is stale or unavailable at formation/execution, skip the observation.
- **Funding/fee/spread needs:** dated futures have no perpetual funding payment, but commissions, bid-ask spread, slippage, roll costs, and margin financing/opportunity cost must be modeled.

## Execution assumptions

The original source's public summary does not specify a crypto execution model. For the adapted hypothesis:

- signal calculation and order placement must be causally separated;
- use executable bid/ask or next-available quote, not same-timestamp mid, for cost-aware tests;
- both legs should be treated as one spread trade with explicit legging-risk handling;
- market, limit, or exchange-listed calendar-spread execution must be evaluated separately;
- commissions, spread, slippage, and exchange-specific calendar-spread tick rules must be included;
- position sizing should control gross notional and margin, not use unbounded leverage;
- expiry/roll handling must be deterministic and pre-registered;
- if one leg cannot fill, the trade must fail closed rather than leave an unintended naked directional position.

Any specific entry threshold, volatility scaling, liquidity cutoff, or expiry buffer introduced in testing is **research-proposed** unless separately supported by a source.

## Evidence

### Source-reported

SSRN `5250499` reports that the return spread between adjacent commodity futures maturities exhibits systematic negative autocorrelation and that the effect is independent of ordinary short-term reversal in the individual contracts. The source further reports stronger reversal where contract returns are more volatile, more individually autocorrelated, and less correlated across maturities; it also reports analogous reversal in other term-structured assets including stock-index futures, corporate bonds, and Treasuries.

In a public author post, Alberto Rossi states that their simple trading strategies produce annual returns up to 18% and Sharpe ratios as high as 1.5. The public post does not establish that those maxima apply to a crypto sample, and this record does not interpret them as crypto evidence.

CME currently lists multiple Ether futures maturities, making the adjacent-maturity construction mechanically portable to a crypto futures curve, but CME provides product availability rather than evidence that the reversal alpha exists.

### Independently reproduced

not independently reproduced

### Negative evidence

No crypto-specific replication of this exact adjacent-maturity weekly return-spread reversal was identified in the reviewed sources. This is a major evidence gap, not evidence of absence.

The source result originates in traditional futures and other term-structured assets. Crypto futures curves may differ materially because of shorter history, concentrated BTC/ETH liquidity, exchange-specific margining, expiry effects, 24/7 underlying spot trading, and potentially low independent cross-sectional breadth.

The strongest source-reported statistics are author-reported and could be sensitive to portfolio construction, contract rolling, multiple testing, and transaction costs. Those details require direct reproduction before any conclusion about net alpha.

## Falsification

1. **Primary serial-dependence test.** On a fully held-out crypto sample, estimate the lag-1 coefficient of weekly adjacent-maturity spread returns. **research-defined falsification threshold:** reject the adapted hypothesis if the coefficient is non-negative or if its 95% confidence interval includes zero across both BTC and ETH after a pre-specified HAC treatment.
2. **Tradable spread-PnL test.** Run the opposite-spread position using causal next-quote execution and all observable costs. **research-defined falsification threshold:** reject tradability if aggregate held-out net return is non-positive or net Sharpe is `<= 0`.
3. **Cost stress.** Double measured commissions plus spread/slippage relative to the base model. **research-defined falsification threshold:** if the sign of cumulative net PnL turns negative under modest two-times friction, classify the effect as execution-fragile.
4. **Expiry contamination test.** Re-run after excluding observations within multiple pre-registered front-contract expiry buffers. **research-defined falsification threshold:** if the effect exists only in the narrowest expiry window and disappears outside it, reinterpret as expiry microstructure rather than general basis-return reversal.
5. **Outright-reversal control.** Include lagged `R(F1)` and `R(F2)` separately. **research-defined falsification threshold:** if the spread-reversal coefficient loses sign and significance after controlling for outright return reversal, reject the distinct relative-value mechanism.
6. **Basis-level and basis-momentum controls.** Control for futures-versus-spot basis level and change in curve slope. **research-defined falsification threshold:** if the reversal signal is subsumed by those existing factors, reject incremental alpha status.
7. **Parameter perturbation.** Repeat with pre-registered formation/holding windows around one week. **research-defined falsification threshold:** if only one exact weekly clock works while nearby windows reverse sign or collapse, classify as unstable/data-mined.
8. **Venue robustness.** Where data permit, compare CME with another dated-futures venue. **research-defined falsification threshold:** if the effect is opposite-signed across venues without a clear market-structure explanation, mark portability `unproven`.
9. **Liquidity/capacity audit.** Measure spread depth, legging slippage, and open interest. **research-defined falsification threshold:** if realistic executable size sufficient for the research target cannot be traded without materially erasing the gross edge, reject implementation suitability.
10. **Strict OOS rule.** All crypto-specific thresholds and contract-selection rules must be frozen before the held-out test. Any rescue by post-hoc retuning invalidates the OOS claim.

## Crypto portability

`adapted`

The mechanism is structurally portable because BTC/ETH dated futures have simultaneous adjacent expiries, so the same return-spread object can be constructed. CME's Ether futures listing cycle explicitly provides multiple concurrent monthly/quarterly maturities.

Portability risks are material:

- crypto spot trades effectively 24/7 while some regulated futures venues have maintenance/session conventions;
- front and deferred crypto futures can have sharply different liquidity and open interest;
- expiry and settlement-index mechanics may dominate short samples;
- the crypto curve may be driven by collateral, leverage, ETF/hedging demand, and exchange-specific capital constraints rather than the same preferred-habitat forces as commodities;
- BTC/ETH alone provide little cross-sectional breadth compared with the source commodity universe;
- perpetual futures are not a substitute for `F1/F2` dated contracts because they lack adjacent expiries.

Crypto portability is therefore a testable hypothesis, not trading authorization.

## Limitations

- **unproven:** no independent crypto replication was identified.
- **not independently reproduced:** source results were not rerun by this Scout.
- **underspecified:** the public primary-source material reviewed here does not expose every implementation detail of the paper's portfolio construction, roll convention, cost model, or exact source-table statistics.
- **data gap:** robust historical bid/ask data for adjacent crypto futures maturities may be less available than settlement data.
- **sample limitation:** crypto dated-futures history is short relative to the source's traditional futures samples.
- **breadth limitation:** a BTC/ETH-only adaptation cannot directly reproduce a 22-market commodity cross-section.
- **execution risk:** two-legged futures spreads face legging, margin, and roll costs that gross backtests can understate.
- **publication/selection risk:** the author reports strong maxima for simple strategies; exact model-selection breadth and net-of-cost robustness must be independently checked.

## Implementation status

`not-implemented`

No PyBroker, Nautilus, strategy-registry, data-pipeline, Paper, Testnet, or Live implementation was created or modified in this Scout cycle. No crypto backtest has been run for this record.

## Adoption boundary

`research-only`

Presence in the Alpha Strategy Pool means only that this is a source-backed, normalized hypothesis suitable for later Research Intake Review. It is not evidence of profitability, validated alpha, implementation approval, Paper approval, Testnet approval, or Live authorization. `adoption: not-approved` and `approval_scope: research-only` remain binding.

## Related Wiki records

- [[quant/crypto-futures-cross-sectional-basis-high-low-1d-2026-08-31]] — related term-structure family, but it trades the level of crypto futures basis rather than week-to-week reversal of an adjacent-maturity return spread.

No existing Wiki Brain record with the exact SSRN source or the same adjacent-maturity weekly basis-return-reversal construction was found in the pre-write search.

## Sources

1. Rossi, Alberto G.; Zhang, Yingguang; Zhu, Yandi. *Short-Term Basis Reversal*. FEB-RN Research Paper No. 85/2025; Georgetown McDonough School of Business Research Paper No. 5250499. Posted 14 May 2025; last revised 12 May 2026. SSRN: https://ssrn.com/abstract=5250499 . DOI: https://doi.org/10.2139/ssrn.5250499 .
2. Alberto Rossi, public author post announcing *Short-Term Basis Reversal* and summarizing the week-to-week adjacent-maturity reversal plus author-reported strategy performance. https://www.linkedin.com/posts/alberto-rossi-5b34a22_finance-assetpricing-futures-activity-7338952205510553602-n4tg .
3. CME Group, *Ether futures* product page / contract specifications, used only to establish current crypto dated-futures term-structure availability and listing cycle. https://www.cmegroup.com/trading/ether-futures.html.html .
