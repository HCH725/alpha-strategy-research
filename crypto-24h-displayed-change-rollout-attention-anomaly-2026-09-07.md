---
schema: strategy-research-record-v1
title: "24h Displayed-Change Roll-Out Attention Anomaly in Crypto Perpetual Futures"
created: 2026-09-07
updated: 2026-09-07
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - behavioral
  - attention
  - microstructure
status: research-only
confidence: medium
source_as_of: 2026-07-23
sources:
  - "OctopusTakopi/24h-rollout-effect GitHub repository, commit 1963ae4cf1170b8b92d7770812a3697f5c921225 (Jul 23 2026): https://github.com/OctopusTakopi/24h-rollout-effect"
  - "Robot James (X/Twitter): https://x.com/therobotjames/status/2080281157246259663"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# 24h Displayed-Change Roll-Out Attention Anomaly in Crypto Perpetual Futures

## Provenance

- **GitHub repository:** https://github.com/OctopusTakopi/24h-rollout-effect
- **Full commit SHA:** `1963ae4cf1170b8b92d7770812a3697f5c921225` (Jul 23, 2026)
- **Original research:** Robot James (X/Twitter thread): https://x.com/therobotjames/status/2080281157246259663
- **FMZ Rust implementation:** https://blog.mathquant.com/2026/09/04/can-the-displayed-24h-change-affect-short-term-prices-implementing-a-roll-out-tradfi-strategy-in-fmz-rust.html
- **Source data as-of:** 2026-07-23 (Binance data snapshot)
- **Authors:** OctopusTakopi (independent researcher); original idea attributed to Robot James.
- **Primary source inspection:** The GitHub repository README, scripts, results, and figures were directly accessed and audited on 2026-09-07.

## Economic mechanism

### Source-reported

Every crypto exchange UI displays a rolling 24-hour percentage change for each asset. This number is a continuously moving window: when a large candle from exactly 24 hours ago drops out of the window, the displayed number moves on its own, regardless of what the current price is doing. The hypothesis is that traders who watch this displayed statistic — on gainers/losers lists, screeners, and mobile market pages — react to changes in the number itself, not just to price action. When the displayed number mechanically improves (because a large negative candle rolls out), attention-driven buying may push prices higher; when it mechanically declines (because a large positive candle rolls out), attention-driven selling may push prices lower.

### Research interpretation

This is a **behavioral/attention-driven alpha** grounded in the mechanical evolution of a displayed statistic. The core hypothesis is:

1. The displayed 24h percentage change is predictable in advance (it is a deterministic function of historical prices).
2. Market participants react to the displayed number rather than the underlying price process.
3. This reaction creates a short-horizon return predictable around roll-out events.

The mechanism is distinct from conventional momentum or mean-reversion: it is not about price trends or valuation, but about the predictable change in an attention-salient display statistic. The transmission chain is:

```
Predictable change in displayed 24h stat
↓
Changes in rankings, screeners, and trader attention
↓
Trading behavior changes (order flow)
↓
Short-horizon price drift
```

## Signal

### Formation timestamp
- Signal formed on each completed hourly candle (UTC-aligned).
- All inputs are known at the time of entry; no look-ahead.

### Lookback
- Uses the hourly candle from exactly 24 hours ago (`old_24h`) and the current hourly candle (`old_now`).
- The 5-minute and 30-minute forward lookback windows predict the mechanical evolution of the displayed stat.

### Long entry
- When `Shock(30) > 0`: the displayed 24h stat will mechanically improve over the next 30 minutes (a large negative candle is rolling out), so the displayed number will rise even if price is flat.
- Direction = LONG.

### Short entry
- When `Shock(30) < 0`: the displayed 24h stat will mechanically decline over the next 30 minutes (a large positive candle is rolling out), so the displayed number will fall even if price is flat.
- Direction = SHORT.

### Exit
- Hold for one hourly candle (1h), exit at next candle open.
- The public research finds the edge concentrates in the roll-out hour: +3.7 bps at 1h hold, -7.3 bps at 24h hold.

### Parameters
- `Shock(30)`: predicted mechanical change in displayed 24h stat over next 30 minutes (in percentage points).
- `Shock(5)`: predicted mechanical change over next 5 minutes (confirmation filter).
- Default gating: `|Current24hChange| >= 4%`, `|Shock(30)| >= 0.8`, `|Shock(5)| >= 0.8 × 0.08`.
- The `Shock(5)` filter confirms the first 5 minutes do not point in the opposite direction.

### Position sizing
- Not specified in the primary source beyond "sane bet sizes" for the surviving configurations.
- The concentrated full-capital variants produce inflated returns that dissolve under realistic sizing.

### Re-entry rules
- One non-overlapping position at a time per contract (default).

### Signal underspecification
- The 4% attention filter threshold, 0.8 shock intensity threshold, and 0.08 × 0.8 shock5 confirmation are research-defined parameters, not source-proven optimal values.
- The selection of which configuration to use (there are 135 tested) is itself fragile — different selection statistics yield different outcomes.

## Required data

- **Instrument:** All non-stablecoin Binance USDT-margined perpetual contracts (788 contracts including delisted ones in the study period).
- **Venue:** Binance Futures.
- **Market type:** USDT-margined perpetual futures.
- **Timeframe:** 1-hour candles (signal); 1-minute candles (event study and minute-level analysis).
- **Fields:** OHLCV (hourly and minute-level); 24h ticker data (current 24h percentage change); ticker start/end timestamps for the 24h window.
- **Point-in-time:** The 24h display window starts and end times are available from the ticker in real time; no look-ahead required.
- **Timestamp:** UTC, normalized from Binance data archives.
- **Missing data:** The primary source excludes stablecoin bases. Delisted contracts are included in the historical study but obviously not tradeable going forward.
- **Data source:** data.binance.vision, snapshot 2026-07-23, frozen manifests in the repository.

## Execution assumptions

- **Signal-to-order timing:** Signal formed on completed hourly candle; order placed at next candle open.
- **Order type:** The primary source studies both maker and taker fills. At maker fees (4 bps round trip), the edge is approximately -0.3 bps per trade. At taker fees (10 bps round trip), the edge is approximately -6.3 bps per trade.
- **Fill model:** The primary source uses realistic order-book data and maker-fill constraints for the FMZ implementation; the GitHub replication uses candle-level backtesting.
- **Fees:** Critical — the raw signal (4.75 bps/trade) is consumed by taker fees and eroded by maker fees. The surviving edge depends on maker fills.
- **Funding:** Not explicitly modeled in the GitHub replication; funding costs further erode the edge.
- **Slippage:** Not explicitly modeled in the public replication.
- **Capacity:** The primary source estimates capacity at "a few hundred thousand dollars, shared among everyone trading it."
- **Leverage/margin:** Not specified.
- **Latency:** The signal is hourly, so latency requirements are modest.

## Evidence

### Source-reported

All figures below trace directly to OctopusTakopi (GitHub repository `1963ae4`, 2026):

- **Full sample (2020–2026):** 1,165,160 signals, mean 1h return +4.75 bps, win rate 49.9%.
- **Trailing 4 years:** 991,147 signals, mean 1h return +3.66 bps, win rate 49.5%.
- **Per-contract daily edge:** 0.086% per active day (0.070% per listed day).
- **Annualized Sharpe (before costs):** approximately 2.1 over trailing 4 years.
- **Year-by-year (mean bps/trade):** 2020: +8.2, 2021: +10.7, 2022: +10.1, 2023: +3.5, 2024: +3.9, 2025: +4.2, 2026: +2.1.
- **Edge by trigger size:** Climbs from +0.5 bps below 1% to +39 bps above 20%.
- **Roll-out hour vs 24h:** +3.7 bps at 1h hold, -7.3 bps at 24h hold.
- **Placebo test (all 24 candle ages):** Ages 1–23 average -0.21 bps and scatter around zero; age 24 (the roll-out hour) stands apart at +1.87 bps with clustered t = 4.2. The edge survives correction for 24 comparisons.
- **After costs:** -6.3 bps per trade at 10 bps taker round trip; -0.3 bps at 4 bps maker round trip.
- **Since 2024:** The short side carries nearly all of the edge.

Source reports this has not been independently reproduced. The public replication covers 788 Binance USDT perpetual contracts from 2020–2026, including delisted contracts.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Fee sensitivity:** The raw edge (4.75 bps) is consumed by standard taker fees (10 bps round trip). Only maker fills preserve a marginal edge.
- **Decaying edge:** Year-by-year mean bps/trade shows declining trend: 2022 (+10.1 bps) → 2023 (+3.5 bps) → 2024 (+3.9 bps) → 2025 (+4.2 bps) → 2026 (+2.1 bps). The edge may be eroding as more participants discover it.
- **Capacity constraint:** Capacity estimated at a few hundred thousand dollars, shared among all participants.
- **Tail risk:** The surviving subset drew down half its starting capital within its 202-day showcase window. Parabolic short squeezes are a known hazard.
- **Selection fragility:** The same training grid yields a losing strategy or a stable +24 bps rule depending on the selection statistic used to pick the winner.
- **Path-timing artifacts:** Concentrated full-capital backtests producing six-figure percentage returns dissolve into fee and path-timing artifacts under realistic sizing.
- **Short-side dominance since 2024:** The edge concentrates on the short side, which carries asymmetric risk from short squeezes.

## Falsification plan

1. **Out-of-sample validation:** Extend the study to 2026 data not in the original sample (post Jul 23 2026). If the edge does not persist at statistically significant levels, the hypothesis is weakened.
2. **Fee sensitivity stress test:** Re-evaluate with realistic maker+fee+spread+slippage+impact model. If the edge is negative under any realistic cost scenario, the strategy is not tradable.
3. **Capacity analysis:** Model the impact of additional participants trading the same signal. If the edge disappears when realistic market impact is included, the capacity constraint is binding.
4. **Placebo test replication:** Replicate the 24-candle-age placebo test on independent data. If the edge appears at other candle ages, the effect is not specific to the roll-out mechanism.
5. **Regime breakdown:** Test separately in bull, bear, and sideways markets. If the edge disappears in one regime, the mechanism is regime-dependent.
6. **Failure threshold:** If the post-sample edge after costs is negative (below 0 bps per trade), abandon the hypothesis.
7. **Action on failure:** Retire the signal; consider whether the attention-driven mechanism is too crowded or too fragile to sustain.

## Crypto portability

**direct**

The signal is native to crypto perpetual futures on Binance. It depends on the specific UI convention of displaying a rolling 24h percentage change, which is standard across crypto exchanges (Binance, OKX, Bybit, etc.). Porting to other exchanges with the same UI convention is straightforward, though each venue's fee structure, liquidity, and participant mix may alter the edge.

**Crypto-specific risks:**
- Short squeezes on small-cap perpetuals can cause outsized losses.
- Funding rate costs erode the edge further on the hold period.
- Delisted contracts are not tradeable forward; survivorship bias affects historical results.
- 24/7 trading means the roll-out events occur continuously.

## Limitations

- **Source quality:** The primary source is an independent GitHub repository and a Twitter thread, not a peer-reviewed paper. The FMZ blog post is an implementation discussion, not an independent validation.
- **Not independently reproduced:** The anomaly has not been verified by a second party.
- **Fee sensitivity:** The edge is marginal or negative under realistic taker costs; only maker fills preserve it.
- **Decaying edge:** Year-over-year decline in mean bps/trade suggests the anomaly may be eroding.
- **Selection fragility:** The choice of which configuration to use significantly affects outcomes, creating overfitting risk.
- **Capacity constraint:** Very limited capacity (~$100k range).
- **Tail risk:** Concentrated drawdowns and short squeezes are known hazards.
- **Underspecified parameters:** The attention filter (4%), shock intensity (0.8), and confirmation (0.8 × 0.08) thresholds are research-defined, not proven optimal.
- **The transmission mechanism is unproven:** The link from displayed-number change → attention → order flow → price is a plausible pathway, not a demonstrated causal chain. The primary source explicitly states this.

## Implementation status

Not implemented in our research stack. The FMZ blog provides a Rust prototype implementation; the GitHub repository provides Python replication scripts. Neither constitutes validation in our own infrastructure.

## Adoption boundary

This record represents research material only. Its presence in this repository does not mean:
- The anomaly is profitable after costs.
- The signal has been validated.
- It is approved for implementation, paper trading, testnet, or live trading.
- The behavioral mechanism is proven.

The primary source itself warns that the anomaly is fragile, capacity-constrained, and subject to tail risk.

## Related Wiki records

- [[crypto-short-horizon-15min-mean-reversion-taker-flow-2026-09-01]] — Different mechanism (15-min microstructure mean reversion from taker flow) vs. this record's attention-driven display-statistic mechanism. Both are short-horizon in crypto but operate through distinct causal channels.
- [[crypto-intraday-sign-mean-reversion-15m-walk-forward-2026-09-01]] — Related 15-min mean reversion but from a different signal (sign-based reversal vs. displayed-statistic roll-out).

## Sources

1. OctopusTakopi. "The 24-Hour Roll-Out Effect in Binance Perpetual Futures." GitHub repository, commit `1963ae4cf1170b8b92d7770812a3697f5c921225` (Jul 23, 2026). https://github.com/OctopusTakopi/24h-rollout-effect
2. Robot James (X/Twitter). Original research thread on the 24h roll-out anomaly. https://x.com/therobotjames/status/2080281157246259663
3. FMZ Quant Blog. "Can the Displayed 24h Change Affect Short-Term Prices? — Implementing a Roll-Out TradFi Strategy in FMZ Rust." Sep 4, 2026. https://blog.mathquant.com/2026/09/04/can-the-displayed-24h-change-affect-short-term-prices-implementing-a-roll-out-tradfi-strategy-in-fmz-rust.html
