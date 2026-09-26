---
schema: strategy-research-record-v1
title: "TradingView Crypto ADX–Range Initial-Balance Breakout"
created: 2026-09-26
updated: 2026-09-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-26
sources:
  - https://www.tradingview.com/script/vw22RuyW-Volatility-IB-Strategy-v6-crypto/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Crypto ADX–Range Initial-Balance Breakout

## Provenance

Public TradingView protected-source strategy **Volatility IB Strategy v6 crypto**, published by `montekristo78`, stable URL https://www.tradingview.com/script/vw22RuyW-Volatility-IB-Strategy-v6-crypto/. TradingView script identity: `vw22RuyW`. The reviewed public page shows the date label `Feb 10`; the year is not inferred because the page does not expose it unambiguously. Source reviewed 2026-09-26.

The source code is protected, so this record uses only the public strategy description and does not reproduce Pine code. GitHub dedup against current `main` found no record containing the canonical script identity `vw22RuyW` or author `montekristo78`; normalized-signal search also found no materially same record combining ADX-low, narrow-range, minimum-duration consolidation with an Initial Balance breakout and optional volume confirmation.

## Economic mechanism
### Source-reported

The author describes a breakout strategy that first identifies consolidation through low ADX, a narrow recent price range, and a minimum persistence requirement. The consolidation high and low become Initial Balance (IB) levels. A close beyond an IB boundary, optionally confirmed by volume, triggers a directional trade.

### Research interpretation

The falsifiable hypothesis is **volatility expansion after persistent low-directionality compression**. ADX below a threshold is a directionality/regime gate; the narrow 20-bar range is the compression state; the minimum five-bar duration rejects transient one-bar contractions; and the IB high/low supplies the breakout boundary. Optional volume confirmation is a separate participation filter, not assumed to add alpha.

For crypto, the mechanism is plausible as a time-series hypothesis because 24/7 markets repeatedly transition between low-volatility consolidation and directional expansion, but the source provides no independent evidence that this rule survives realistic crypto execution costs.

## Signal

Source-reported normalized logic:

- Consolidation gate: ADX below a configurable threshold; source default is **25**.
- Range gate: recent price range is below a configurable percentage; source default is **<2% over 20 bars**.
- Persistence gate: consolidation lasts at least a configurable number of bars; source default is **5 bars**.
- IB formation: consolidation high and low are marked as the Initial Balance levels.
- Long entry: **close above IB High**, with volume confirmation when the optional volume filter is enabled.
- Short entry: **close below IB Low**, with volume confirmation when the optional volume filter is enabled.

Underspecified by the public source:

- exact ADX length and smoothing method;
- exact algebra/denominator used for the “<2% over 20 bars” range test;
- whether IB levels freeze immediately after the minimum duration or continue updating until breakout;
- exact volume-confirmation formula and defaults;
- re-entry behavior after a failed breakout;
- stop-loss mechanics beyond the source's general statement that enhanced stop-loss mechanisms exist;
- profit target, trailing logic, holding period, and other exit rules;
- pyramiding / concurrent-position behavior;
- signal-to-order and fill timing.

No missing rule is silently supplied. Any later operational choice for these fields must be labeled `research-proposed`.

## Required data

Source-supported minimum:

- crypto price series;
- OHLC data sufficient to compute the 20-bar range and ADX;
- close for breakout confirmation;
- volume if the optional volume-confirmation filter is enabled;
- ordered timestamps and a declared candle timeframe.

Data gaps:

- the source does not identify a specific crypto instrument, venue, spot/perpetual market type, or required timeframe;
- timezone / candle-boundary convention is not stated;
- missing-bar and missing-volume handling is not stated;
- point-in-time availability must ensure the breakout uses only a completed bar's close and already-formed consolidation state.

## Execution assumptions

The source specifies close-based breakout conditions but does not state whether an order is filled at the breakout close, next bar open, or another price. Order type, spread, fees, slippage, impact, latency, partial fills, capacity, leverage, margin, funding, borrow/short constraints, liquidation treatment, and position sizing are not stated.

A leakage-safe implementation must not treat a bar close as both an observed signal and a guaranteed same-price fill unless that convention is explicitly modeled as `research-proposed`.

## Evidence
### Source-reported

The reviewed public description provides the strategy logic and defaults above but does not provide traceable Sharpe, CAGR, drawdown, win rate, trade count, sample window, venue, instrument, or after-cost performance figures.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No empirical negative result is reported on the reviewed page. The protected source prevents direct code-level verification of the exact formulas and execution semantics. Absence of reported negative evidence is not evidence that no negative result exists.

## Falsification plan

1. Freeze the source-supported core rule before testing: ADX threshold 25, range threshold 2%, range lookback 20 bars, minimum consolidation duration 5 bars. Recover any still-missing formula from a public source before implementation; otherwise label the operationalization `research-proposed`.
2. Compare against a plain 20-bar breakout with identical universe, execution, and costs. **research-defined falsification threshold:** reject incremental value if the ADX/range/persistence gates do not improve held-out net Sharpe or expectancy relative to that baseline.
3. Ablate ADX, narrow-range, minimum-duration, and volume confirmation separately. **research-defined falsification threshold:** do not attribute alpha to a component whose removal does not materially weaken held-out results.
4. Use chronological train/validation/test splits spanning bull, bear, crash, and quiet crypto regimes; do not optimize on the held-out period.
5. Stress plausible fees, spread, slippage, and one-bar execution latency. **research-defined falsification threshold:** reject tradability if net expectancy is non-positive under conservative executable costs.
6. Test BTC and ETH and, where data permits, at least two independent venue feeds. **research-defined falsification threshold:** weaken a general crypto-alpha claim if positive after-cost expectancy exists only on one asset or one venue.
7. Perturb the source defaults around nearby values only after the exact range formula is recovered. **research-defined falsification threshold:** treat the edge as parameter-fragile if sign or economic magnitude collapses under small neighboring changes.

## Crypto portability

**direct, but unproven.** The source explicitly presents the strategy as crypto-oriented. Portability across crypto market types remains unproven because the source does not specify spot versus perpetuals or venue. Perpetual implementations additionally require funding, mark/index-price, liquidation, and contract-specification treatment. Crypto's 24/7 structure also makes candle-boundary choice material.

## Limitations

- Protected source: exact Pine implementation cannot be audited from the public page.
- `underspecified`: ADX implementation, range-percentage algebra, volume filter, IB freeze/update semantics, exits, re-entry, sizing, and fills.
- `data gap`: instrument, venue, market type, timeframe, timezone, costs, funding, spread, slippage, and capacity.
- `not independently reproduced`.
- `unproven`: no source-reported sample statistics establish profitability or robustness.

## Implementation status

Not implemented in our research stack. No Qlib full backtest or independent reproduction has been performed.

## Adoption boundary

Research-only, not implemented, and not approved. Presence in this repository does not mean the strategy passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, is profitable or validated alpha, or is approved for Paper, Testnet, or Live trading.

## Related Wiki records

None linked; no stable Hermes Wiki Brain page was verified in this GitHub-only run.

## Sources

- TradingView — `montekristo78`, **Volatility IB Strategy v6 crypto**: https://www.tradingview.com/script/vw22RuyW-Volatility-IB-Strategy-v6-crypto/ (public protected-source strategy page; reviewed 2026-09-26; page date label `Feb 10`; script identity `vw22RuyW`).
