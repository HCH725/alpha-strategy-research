---
schema: strategy-research-record-v1
title: "Bitcoin Option Expiry Gamma-Driven Intraday Spot Reversal"
created: 2026-09-21
updated: 2026-09-21
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - options
  - gamma-exposure
  - dealer-hedging
  - intraday-reversal
  - bitcoin
  - deribit
  - expiry
status: research-only
confidence: medium
source_as_of: 2026-09-21
sources:
  - "https://www.sciencedirect.com/science/article/pii/S1544612326008688"
  - "https://doi.org/10.1016/j.frl.2026.110340"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Option Expiry Gamma-Driven Intraday Spot Reversal

## Provenance

- **Primary Source:** Weiss, D., Gaudiosi, R., Zhou, Z. I., & Webb, R. I. (2026). "Bitcoin option expiration, gamma exposure, and intraday price reversals." *Finance Research Letters*, 107, 110340.
- **DOI:** 10.1016/j.frl.2026.110340
- **Journal:** Finance Research Letters (Elsevier), vol. 107(C), September 2026. Open access (Creative Commons license).
- **Sample Period:** 2021-01-01 to 2023-12-31 (2 years of high-frequency data).
- **Universe:** Deribit BTC options (all strikes and moneyness categories), Deribit perpetual futures, and spot exchanges used for Deribit settlement price.
- **Average Daily Activity:** ~14,000 option contracts expire daily, corresponding to ~$500M notional open interest on Deribit.
- **Source Date Accessed:** 2026-09-21.

## Economic mechanism

### Source-reported

Bitcoin prices exhibit a statistically and economically significant intraday return reversal around the daily expiration of Deribit options. The mechanism is:

1. **Dealer hedging pressure:** When cumulative gamma exposure (GEX) is negative, option market makers are net short gamma. To maintain delta-neutral positions, they must buy as price rises and sell as price falls — positive feedback trading.
2. **Expiry concentration:** This hedging pressure intensifies around daily option expiry (Deribit daily options expire at 08:00 UTC). As expiry approaches, gamma accelerates (gamma peaks for at-the-money options near expiry), forcing more aggressive dealer rebalancing.
3. **Price reversal:** A downward price move is observed for the top decile of open interest starting about one hour before option expiration. The price then reverses and stabilizes within the next 90 minutes around the initial pre-expiry price level.
4. **Conditioning:** The effect concentrates on days with elevated at-the-money open interest and is strongest when cumulative gamma exposure is negative.

### Research interpretation

The hypothesis is that dealer hedging flows around daily option expiry create a mechanical, predictable intraday price pattern: a directional move into expiry (driven by gamma-accelerated hedging) followed by a reversal (as hedging pressure subsides post-expiry and position unwinding occurs). This is a structural microstructure effect, not a directional alpha — it is a timing/event-driven reversal conditioned on GEX sign and OI level.

The mechanism is falsifiable: if the reversal does not concentrate on high-OI / negative-GEX days, or if it does not survive after controlling for regular intraday patterns, the hypothesis fails.

## Signal

- **Formation timestamp:** Deribit daily option expiry at 08:00 UTC.
- **Lookback:** Cumulative gamma exposure computed from Deribit options open interest by strike, using Black-Scholes gamma at current market conditions. Source does not specify exact lookback window for GEX computation beyond "cumulative."
- **Entry:** Short BTC spot or perpetual starting ~1 hour before expiry (approximately 07:00 UTC) on days when (a) ATM open interest is in the top decile and (b) cumulative GEX is negative. Source-reported: "A downward price move is observed for the top decile of open interest starting about one hour before option expiration."
- **Exit:** Close position ~90 minutes after expiry (approximately 09:30 UTC). Source-reported: "The price then reverses and stabilizes within the next 90 min around the initial 7 am price level."
- **Holding period:** ~2.5 hours (entry ~07:00 UTC, exit ~09:30 UTC).
- **Parameters:** ATM open interest top-decile threshold; negative cumulative GEX condition. Source does not specify exact GEX computation methodology beyond "cumulative gamma exposure" — mark data gap / underspecified for precise replication.
- **Position-sizing logic:** Not specified by source. Research-proposed: equal-weight or vol-scaled per-trade.
- **Re-entry rules:** Daily (once per expiry event). Research-proposed: only on days meeting both OI and GEX conditions.
- **Underspecified items:** Exact GEX computation methodology (which strikes included, how dealer vs. non-dealer OI is distinguished, exact formula for aggregation); exact entry/exit timestamps beyond "about one hour before" and "within 90 min"; position sizing.

## Required data

- **Instrument:** BTC perpetual futures (Deribit) and BTC spot (exchanges used for Deribit settlement price).
- **Venue:** Deribit (options), spot exchanges (BTC spot for settlement), Deribit perpetual futures.
- **Market type:** Options (Deribit daily BTC options), perpetual futures, spot.
- **Timeframe:** Intraday (sub-hourly recommended for precise entry/exit; source uses high-frequency transaction data).
- **Fields:** Options open interest by strike and expiry; options implied volatility; BTC spot prices; perpetual futures prices and volume; cumulative gamma exposure by strike.
- **Point-in-time:** Options OI and GEX must be known before entry (~07:00 UTC). Deribit publishes OI data with some delay — source does not specify exact availability lag. Data gap / underspecified.
- **Timestamp:** UTC (Deribit expiry is 08:00 UTC).
- **Missing-data:** Not specified by source.

## Execution assumptions

- **Signal-to-order timing:** Entry ~1 hour before expiry, exit ~90 minutes after. Source-reported timing.
- **Next-bar vs same-bar execution:** Source uses high-frequency data; assumed sub-hourly execution.
- **Market / limit order:** Not specified by source. Research-proposed: market order for entry, limit or market for exit.
- **Fill model:** Not specified by source. Assumed taker for both legs.
- **Fees:** Not specified by source. At 10 bps round-trip taker cost, the ~$50M annual wealth transfer implies the gross edge is meaningful but net edge requires careful cost accounting.
- **Spread:** Not specified by source.
- **Slippage:** Not specified by source. Source notes trading activity rises around expiry, which may imply wider spreads or higher impact during the expiry window.
- **Impact / capacity:** Source estimates ~$50M annual wealth transfer between option writers and holders. This sets an upper bound on aggregate strategy capacity. Per-strategy capacity is a fraction of this.
- **Funding:** If using perpetual futures for the short leg, funding payments around expiry may affect the carry. Not modeled by source.
- **Leverage / margin:** Not specified by source. Research-proposed: conservative (2x or less) given the intraday tail risk.
- **Latency:** Source uses high-frequency data but does not specify latency requirements. The 1-hour pre-expiry entry window is wide enough for non-HFT execution.

## Evidence

### Source-reported

- Statistically and economically significant return reversal around Deribit BTC option daily expiry.
- Effect concentrates on days with elevated ATM open interest (top decile).
- Effect is strongest when cumulative gamma exposure is negative.
- Trading activity rises around expiry in Deribit perpetual futures and spot exchanges.
- Annual wealth transfers of approximately USD 50 million between option writers and holders.
- Sample: 2 years (2021-2023), high-frequency data from Deribit and spot exchanges.
- Average daily expiring notional: ~$500M on Deribit (~14,000 contracts).

### Independently reproduced

Not independently reproduced.

### Negative evidence

Source-reported: The correlation is statistically significant only when options open interest reaches the top decile. On low-OI days, the effect is not significant. This is consistent with a mechanical hedging-pressure explanation rather than a robust directional alpha.

None identified in the reviewed sources beyond the OI conditioning; absence is not evidence of no negative result.

## Falsification plan

1. **Out-of-sample test:** Replicate on 2024-2026 data (post-sample of original study). The Deribit daily options market has grown significantly since 2023; test whether the effect persists at current OI levels.
2. **OI conditioning test:** Verify that the reversal does NOT occur on days below the top-decile OI threshold. If it occurs on all days, the mechanism is not gamma-specific.
3. **GEX sign test:** Verify that the reversal is stronger on negative-GEX days than positive-GEX days. If there is no difference in reversal magnitude by GEX sign, the gamma-hedging mechanism is not supported.
4. **Placebo test:** Test the same pattern on non-expiry hours. If similar reversals occur at random times, the expiry-specific mechanism is not supported.
5. **Fee sensitivity:** At 10 bps round-trip taker cost, does the net edge survive? The gross edge must exceed the cost threshold.
6. **Capacity test:** As OI grows, does the edge decay? Source notes the effect concentrates at top-decile OI; if the market becomes more efficient around expiry, the edge may shrink.
7. **Cross-venue test:** Does the pattern also appear on other Deribit-settled instruments or on exchanges with different expiry mechanics?

## Crypto portability

**Direct.** The mechanism is specific to crypto perpetual/options markets with daily expiry (Deribit). It is not directly portable to traditional markets with weekly or monthly expiry. However, the gamma-hedging mechanism is well-documented in equity options markets (e.g., S&P 500 monthly OPEX effects), suggesting the principle is portable even if the specific daily-expiry structure is crypto-specific.

Crypto-specific considerations:
- Deribit daily options have a specific expiry time (08:00 UTC) — the timing is venue-specific.
- Perpetual futures funding rates around expiry may add or subtract from the carry.
- 24/7 trading means the expiry effect interacts with overnight/session dynamics.
- Liquidity around expiry may differ from traditional markets.

## Limitations

- **Sample period:** 2 years (2021-2023). The Deribit daily options market was smaller in 2021-2022 than in 2023-2024. The effect may be regime-dependent.
- **GEX computation underspecified:** The exact methodology for computing cumulative GEX (which strikes, how dealer vs. non-dealer OI is distinguished) is not fully specified in the available abstract/summary. Replication requires access to the full paper.
- **Capacity:** The ~$50M annual wealth transfer is an aggregate estimate. Individual strategy capacity is limited by the OI concentration at specific strikes and the timing window.
- **Selection on top-decile OI:** The effect only appears on high-OI days, which are a subset of all trading days. The strategy would have limited trade frequency.
- **Intraday tail risk:** Shorting BTC 1 hour before expiry on high-OI days exposes the strategy to gap risk if a large move occurs.
- **Not independently reproduced.**
- **Data gap:** Exact GEX computation, entry/exit timestamps, and position sizing are underspecified in the available source summary.

## Implementation status

Not implemented. No implementation in our research stack has been completed.

## Adoption boundary

This record is research material only. Presence in this repository does not mean:
- Passed Research Intake Review
- Entered Hermes Wiki Brain
- Entered the production candidate pool
- Completed Qlib full-backtest validation
- Became a frozen survivor or leaderboard entry
- Profitable
- Validated alpha
- Approved for implementation, paper trading, testnet, or live trading

## Related Wiki records

- [[bitcoin-options-dealer-gamma-exposure-gex-regime-2026-09-01]] — related but materially distinct: that record uses aggregate GEX as a volatility regime filter; this record documents a specific intraday reversal event around daily expiry conditioned on GEX sign and OI level.
- [[crypto-perpetual-liquidation-cascade-early-warning-taker-flow-variance-2026-09-01]] — related microstructure mechanism (dealer/liquidation hedging flows) but different event type and signal.

## Sources

1. Weiss, D., Gaudiosi, R., Zhou, Z. I., & Webb, R. I. (2026). "Bitcoin option expiration, gamma exposure, and intraday price reversals." *Finance Research Letters*, 107, 110340. DOI: 10.1016/j.frl.2026.110340. URL: https://www.sciencedirect.com/science/article/pii/S1544612326008688
