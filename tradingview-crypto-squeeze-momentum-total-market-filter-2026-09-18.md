---
schema: strategy-research-record-v1
title: "TradingView Crypto Squeeze-Momentum with Total-Market Regime Filter"
created: 2026-09-18
updated: 2026-09-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2021-05-31
sources:
  - https://www.tradingview.com/script/9cxy1Yu9-Crypto-momentum-strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Crypto Squeeze-Momentum with Total-Market Regime Filter

## Provenance

Public TradingView open-source strategy `Crypto momentum strategy` by `echepata`, stable script URL `https://www.tradingview.com/script/9cxy1Yu9-Crypto-momentum-strategy/`. The page was published 2021-05-24 and its described market-filter update is dated 2021-05-31. Source as-of date: 2021-05-31.

The source credits LazyBear's Squeeze Momentum indicator as the momentum basis. This record normalizes the TradingView author's strategy description; it does not reproduce or redistribute the Pine source.

## Economic mechanism

### Source-reported

The author describes a long-only crypto momentum strategy that seeks turning points in a Squeeze-Momentum-style oscillator, but accepts long entries only when the traded asset is in an upward 50-EMA trend. A later update optionally adds a broad crypto-market regime filter using `CRYPTOCAP:TOTAL`: the total-market close must be above its 50 EMA and that EMA must be rising. The author states that this market filter was intended to help lesser-known coins that are strongly influenced by the overall crypto market, while potentially hurting Bitcoin and Ethereum where the filter is less appropriate.

### Research interpretation

The falsifiable hypothesis is that a local momentum trough/upswing has higher continuation probability when both the asset and, for smaller crypto assets, the aggregate crypto market are already in positive medium-term trend regimes. Component roles are:

- Regime: asset close above rising 50 EMA.
- Primary signal: turning point from a valley in a Squeeze-Momentum-style oscillator.
- Optional cross-market regime: `CRYPTOCAP:TOTAL` close above rising 50 EMA.
- Exit signal: momentum-oscillator peak/downswing used as the sell signal.

The potentially distinctive alpha question is whether conditioning an altcoin's local momentum signal on aggregate crypto-market direction adds out-of-sample information beyond the asset-only trend filter.

## Signal

Source-described normalized logic:

- Direction: long-only.
- Asset trend gate: current candle close must be above the asset's 50-period EMA, and the 50 EMA must be trending upward.
- Primary entry trigger: the Squeeze-Momentum-derived momentum trend shifts at a valley; the exact Boolean definition of a valley/shift is not fully specified in the prose description.
- Optional broad-market gate, added 2021-05-31: poll `CRYPTOCAP:TOTAL`; its close must be above its 50 EMA and that EMA must be trending upward. The author recommends this gate for lesser-known coins and recommends disabling it for Bitcoin and Ethereum.
- Exit: the strategy describes momentum peaks as sell signals; exact exit Boolean/timing is underspecified in the prose.
- Re-entry, exact oscillator parameters, EMA-slope definition, same-bar versus next-bar fill, and any minimum holding period are underspecified.

No missing Boolean details are invented here. A future implementation must derive them from an auditable source or label any chosen operationalization `research-proposed`.

## Required data

- Traded crypto asset OHLC data.
- At least close data sufficient to compute the asset 50 EMA and its slope/direction.
- Data sufficient to compute the referenced Squeeze-Momentum-style oscillator; exact inputs/parameters require source-level reconstruction before implementation.
- When the optional market gate is enabled: point-in-time `CRYPTOCAP:TOTAL` close data and its 50 EMA.
- Timeframe: source says the strategy works with crypto on day/week charts; exact preferred timeframe is otherwise not fixed.
- Timestamp alignment between the traded asset and `CRYPTOCAP:TOTAL` is material when the cross-market gate is used.

## Execution assumptions

The public description does not specify order type, fill model, fees, spread, slippage, latency, position sizing beyond a release note stating 100% of equity in each trade, or exchange/venue. Same-bar versus next-bar execution is also underspecified. These omissions must not be silently filled during validation.

The broad-market filter must use only `CRYPTOCAP:TOTAL` information available at the traded asset's signal timestamp. Any candle-boundary or data-publication mismatch must be handled point-in-time.

## Evidence

### Source-reported

The author states that the strategy works well with crypto on day/week charts and reports an average profit ratio of 4:1 with roughly half of trades profitable. These are TradingView-author claims from the cited page, not independently verified results. The page also reports that the optional aggregate-market filter improved performance on lesser-known coins but had an adverse effect on large-cap Bitcoin and Ethereum.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself reports that the optional aggregate-market filter can adversely affect Bitcoin and Ethereum. This is useful negative evidence against treating the cross-market gate as universally beneficial.

No additional independent negative evidence was established in this Scout cycle; absence is not evidence of no negative result.

## Falsification plan

1. Reconstruct the exact oscillator turning-point and EMA-slope rules without look-ahead; reject the record for implementation if those rules cannot be made point-in-time and deterministic.
2. Compare three predeclared variants on the same altcoin universe: primary momentum signal only; + asset 50-EMA trend gate; + asset gate and `CRYPTOCAP:TOTAL` gate.
3. Run the same ablation separately for BTC/ETH and for smaller liquid crypto assets. The aggregate-market mechanism is weakened if the TOTAL gate fails to improve net OOS risk-adjusted performance or drawdown behavior for the smaller-asset cohort.
4. Require chronological out-of-sample or walk-forward evaluation and include realistic fees/slippage. Do not tune the market-filter choice per asset using the test sample.
5. Stress timestamp alignment and candle-boundary conventions between each asset and `CRYPTOCAP:TOTAL`; reject any result that depends on unavailable same-bar aggregate-market information.
6. Test sensitivity around the 50-EMA regime length and slope definition rather than accepting a single optimized point. Material instability weakens the hypothesis.

## Crypto portability

direct

The source is explicitly a crypto strategy and explicitly uses the aggregate crypto-market capitalization series as an optional regime dependency. Portability risks remain: `CRYPTOCAP:TOTAL` construction/history can differ from venue-specific tradable universes; 24/7 candle boundaries matter; smaller-coin liquidity and slippage can dominate; and a market-cap aggregate partly contains the traded asset itself, especially for large-cap coins.

## Limitations

- Not independently reproduced.
- Exact Squeeze-Momentum turning-point Boolean logic is underspecified in the prose description.
- Exact EMA-slope definition is underspecified.
- Execution timing and transaction-cost assumptions are underspecified.
- The source-reported performance claims are not independently verified and lack a fully specified sample in the page description.
- `CRYPTOCAP:TOTAL` is a non-tradable aggregate series and introduces cross-series point-in-time alignment and composition concerns.
- The source is from 2021; current-market robustness is unproven.

## Implementation status

Not implemented in our research stack. No backtest, reproduction, parameter verification, or runtime integration was performed in this Scout cycle.

## Adoption boundary

Research material only. Presence in this repository does not establish profitability, validated alpha, implementation approval, paper/testnet approval, or live-trading approval.

## Related Wiki records

No stable Hermes Wiki Brain record was resolved in this GitHub-only cycle; no Wiki link is fabricated.

## Sources

- TradingView — `Crypto momentum strategy`, author `echepata`: https://www.tradingview.com/script/9cxy1Yu9-Crypto-momentum-strategy/ (published 2021-05-24; relevant update 2021-05-31; accessed/as reviewed 2026-09-18).
