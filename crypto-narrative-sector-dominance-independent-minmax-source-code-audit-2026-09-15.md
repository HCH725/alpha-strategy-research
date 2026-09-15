---
schema: strategy-research-record-v1
title: Crypto Narrative Sector Dominance Independent Min-Max Rotation — Source-Code Audit
created: 2026-09-15
updated: 2026-09-15
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-15
sources:
  - https://www.tradingview.com/script/98yiT7we/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The page describes seven sectors built from 40 top altcoins and explicitly lists FLOKI in Memecoins, while the inspected 101-line Pine source contains 39 dominance inputs in total and the Memecoins sum contains six inputs with no FLOKI series."
  - "The page calls the outputs relative strength and says their crossings reveal real capital rotation, but each sector is independently min-max normalized against its own 5,000-daily-bar history; cross-sector level comparisons therefore do not share a common scale or benchmark."
---

# Crypto Narrative Sector Dominance Independent Min-Max Rotation — Source-Code Audit

## Provenance

- Public TradingView open-source indicator: **Sector Rotation ULTIMATE: 7 Narrativas Independientes**, author **leanzambra100**, published 2025-12-23.
- Stable source URL: https://www.tradingview.com/script/98yiT7we/
- Source inspected directly on 2026-09-15: public description plus complete 101-line Pine Script v6 exposed by TradingView.
- Repository and Hermes Wiki Brain pre-write searches found generic sector-rotation, dominance, cross-sectional momentum, and BTC-dominance material, but no record for source `98yiT7we` or this specific construction/audit.
- The source is public and open-source on TradingView. This record normalizes the logic and does not redistribute the full Pine script.

## Economic mechanism

### Source-reported

The author frames the indicator as a crypto narrative-rotation tool. It groups large crypto assets into Layer 1, Enterprise, DeFi, Memecoins, AI, L2/Scalability, and RWA+Infrastructure sectors, sums each group's market-cap dominance, independently normalizes the sector series to 0–100, and interprets changing leadership/crossings as evidence of capital rotating between narratives. The page says the tool is useful for altseason, sector rotation, and entry timing.

### Research interpretation

The falsifiable hypothesis is that changes in sector-level market-cap share contain information about subsequent relative returns of constituent sectors. This is a **capital-share / narrative momentum** hypothesis, not evidence of alpha by itself.

The inspected implementation materially weakens the page's cross-sector interpretation. Every sector is transformed using its own rolling minimum and maximum, so equal oscillator values do not represent equal dominance, equal percentile rank, equal momentum, or equal capital flow across sectors. A crossing can be caused by one sector moving within a narrow historical range while another moves within a much wider range. The display is therefore better interpreted as seven independently scaled dominance-state oscillators than as a directly comparable relative-strength ranking.

## Signal

**Source executable construction:**

- Formation data: TradingView `CRYPTOCAP:<asset>.D` daily dominance closes requested at fixed timeframe `D`, regardless of host-chart timeframe.
- Sector raw value: arithmetic sum of the constituent dominance closes assigned to that sector.
- Transform: for each sector separately, `100 * (sector_sum - rolling_low) / (rolling_high - rolling_low + epsilon)`, with a 5,000-daily-bar rolling high/low window and `1e-10` denominator stabilizer.
- Display: seven independently normalized lines plus horizontal references at 20, 50, and 80. Adjacent line fills are visual only.
- Source does **not** implement orders, portfolio weights, explicit long/short entry, exit, holding period, rebalance rule, stop, take-profit, or position sizing.
- The source description suggests using leadership/crossings for entry timing, but does not define an executable trading rule. Therefore the trading signal is **underspecified**.
- Formation availability is also **underspecified** for intraday use: the code requests daily series but the source does not define whether decisions must wait for the daily bar to close or may use the developing daily value.

**Source-code audit:** the comments/page characterize Memecoins as seven coins and the page explicitly names FLOKI, but the inspected source sums only SHIB, DOGE, PEPE, WIF, PUMPF, and BONK. With the other groups containing 8 + 6 + 8 + 5 + 4 + 2 inputs, the executable source uses 39 dominance inputs, not the advertised 40.

No Scout-proposed entry/exit rule is silently substituted for the missing source rule.

## Required data

- TradingView CRYPTOCAP daily market-cap dominance series for every hard-coded constituent.
- Fixed daily aggregation; host chart may be intraday but the requested inputs remain daily.
- At least the available historical observations needed to evaluate the 5,000-bar extrema; constituent listing/history lengths differ materially.
- Point-in-time constituent availability and historical symbol continuity are required for causal research.
- A future tradability test would additionally need point-in-time constituent prices, venue/listing history, volume/liquidity, spreads, fees, slippage, and—if perpetuals are used—funding/mark/index data.
- Missing-data handling is not specified by the source. Because sector values are arithmetic sums, unavailable constituent observations can affect sector availability; this must be audited rather than imputed.

## Execution assumptions

The source is an indicator, not a TradingView strategy, and specifies no executable order model. Order type, signal-to-order delay, fill convention, fees, spread, slippage, market impact, capacity, leverage, funding, short availability, partial fills, and failure handling are all **underspecified**.

For causal use, a completed daily dominance observation should not be treated as known before its daily bar closes unless a separately specified intraday point-in-time construction is used. That convention is a research requirement, not a source-reported trading rule.

## Evidence

### Source-reported

The page states that independently normalized sector lines reveal capital rotations and are useful for spotting altseason, sector rotations, and entry timing. It reports no backtest, Sharpe ratio, CAGR, drawdown, hit rate, transaction-cost analysis, or out-of-sample evidence.

### Independently reproduced

not independently reproduced

### Negative evidence

- **Constituent-count contradiction:** advertised 40 top altcoins / seven Memecoins including FLOKI versus 39 executable dominance inputs / six Memecoin inputs and no FLOKI in the inspected source.
- **Scale-comparability problem:** each sector is independently min-max normalized over its own history. Crossings do not establish that capital is literally flowing from one sector to another, because the transformed levels lack a shared denominator or cross-sectional normalization.
- **Survivorship/history problem:** the baskets are hard-coded current narratives and include assets with very different listing dates. The source provides no point-in-time sector membership reconstruction.
- **No tradable rule or empirical validation:** the page's entry-timing claim is not paired with exact orders or performance evidence.
- No independent replication was performed in this Scout cycle.

## Falsification plan

1. **Cross-sector comparability test.** Reconstruct daily point-in-time sector market caps and compare source oscillator crossings with actual changes in each sector's share of total eligible sector capitalization. **research-defined falsification threshold:** reject the "crossing = capital rotation" interpretation if crossing direction agrees with the next-day change in pairwise sector share less than 55% of the time out of sample.
2. **Forward-return test.** At each completed UTC daily close, rank sectors by the source oscillator and test next 1d/7d constituent-basket excess return versus an equal-weight eligible-sector benchmark. **research-defined falsification threshold:** reject predictive leadership if top-minus-bottom net OOS mean return is non-positive or its block-bootstrap 95% confidence interval includes zero at both horizons.
3. **Common-scale ablation.** Compare independent min-max normalization with a shared cross-sectional normalization of contemporaneous sector market shares. **research-defined falsification threshold:** treat the source transform as non-incremental if it fails to improve OOS rank IC or net Sharpe over the common-scale control.
4. **Point-in-time membership test.** Compare the hard-coded current basket against historically eligible constituents. **research-defined falsification threshold:** classify the apparent effect as survivorship-sensitive if the sign of top-minus-bottom OOS return flips or Sharpe changes by more than 0.25.
5. **Timing/leakage audit.** Compare completed-daily-bar signals with any intraday host-chart interpretation. **research-defined falsification threshold:** reject intraday portability if apparent edge disappears when daily inputs are lagged until first causally tradable observation.
6. **Cost/capacity stress.** For a research-proposed tradable sector basket only, apply point-in-time liquidity filters plus 5/10/20 bps round-trip friction and realized funding where relevant. **research-defined falsification threshold:** reject practical alpha if net OOS Sharpe is <= 0 at 10 bps plus funding.

## Crypto portability

**direct** — the source is crypto-native and uses TradingView CRYPTOCAP dominance series. Portability to an executable portfolio remains unproven because market-cap dominance is not itself a tradable instrument. Spot/perpetual implementation introduces venue fragmentation, funding, stablecoin quote risk, listing/delisting, liquidity and market-impact differences. Crypto's 24/7 market also requires an explicit UTC/session boundary for daily signal availability.

## Limitations

- Trading rule **underspecified**: no exact entry, exit, holding, rebalance, or sizing rule.
- No source-reported performance evidence and **not independently reproduced**.
- Hard-coded narrative membership creates survivorship and taxonomy drift.
- Independent 5,000-day min-max transforms are not a common cross-sectional scale.
- Newer constituents have materially shorter histories than the nominal normalization window.
- Market-cap dominance can change through price moves, supply changes, listings/delistings, or denominator changes; it is not a direct measure of fund flow.
- The source-code constituent-count contradiction makes the descriptive "40 top altcoins" label contested.

## Implementation status

`not-implemented`. No implementation, historical backtest, Paper, Testnet, or Live work was performed by this Scout.

## Adoption boundary

Research material only. Presence in this staging repository does not establish profitability, validated alpha, implementation approval, or authorization for Paper/Testnet/Live trading. `adoption: not-approved`; `approval_scope: research-only`.

## Related Wiki records

Repository and Hermes Wiki Brain searches found adjacent sector-rotation, BTC-dominance, and cross-sectional-momentum concepts, but no stable Wiki record with the same TradingView source or independently min-max-normalized seven-sector dominance construction. No Wiki link is fabricated.

## Sources

- TradingView, leanzambra100, **Sector Rotation ULTIMATE: 7 Narrativas Independientes**, published 2025-12-23; public open-source Pine Script v6, inspected 2026-09-15: https://www.tradingview.com/script/98yiT7we/
