---
schema: strategy-research-record-v1
title: "Funding Rates as a Cross-Sectional Factor in Perpetual Futures: Survivorship-Free Regime Flip and Carry Residue"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - funding-rate
  - cross-sectional
  - perpetual-futures
  - carry
  - regime
  - survivorship-free
status: research-only
confidence: high
source_as_of: 2026-09-13
sources:
  - "OctopusTakopi, 'Funding Rates as a Cross-Sectional Factor in Perpetual Futures,' GitHub repository, https://github.com/OctopusTakopi/funding-rate-alpha (2026)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Funding Rates as a Cross-Sectional Factor in Perpetual Futures: Survivorship-Free Regime Flip and Carry Residue

## Provenance

**Primary source:** OctopusTakopi, "Funding Rates as a Cross-Sectional Factor in Perpetual Futures," GitHub repository, https://github.com/OctopusTakopi/funding-rate-alpha (2026). The repository is public and frozen by manifest; data archives are public Binance USDT-margined perpetual funding settlements, hourly klines, and open-interest metrics.

**Data scope:** 791 contracts (including every delisted one), 2.43 million funding settlements from 2020-01 through 2026-06, hourly prices through 2026-07, 5-minute open-interest metrics for 421 contracts, extended to 6.1 million settlements across three venues (Binance plus two additional venues with 1.14M and 2.55M settlements).

**Universe:** Survivorship-free union of 421 liquid USDT-margined perpetual contracts on Binance, filtered to a trailing 90-day mean daily quote volume of at least USD 5M evaluated at each decision time. Open-interest analyses further restrict to the top 150 by trailing 365-day volume.

**Dedup status:** The existing repository contains `crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11.md` (Bryan Vine, Alpha Research Paper 2) and `crypto-perpetual-funding-rate-carry-spot-perp-2026-08-31.md` (traditional academic papers). This source is materially distinct: different author, different methodology (survivorship-free venue-complete data vs. Vine's analysis), different findings (regime flip, failure of open-interest cross-validation), and broader scope (3 venues, 791 contracts).

## Economic mechanism

### Source-reported

The funding rate is a clipped average of the premium index (how rich a perpetual trades against spot). The raw level is a carry trade far more than a price signal: the dollar-neutral decile book collects 11.6 bps per day of funding, two thirds from the long leg (contracts paying deeply negative funding where shorts pay longs) rather than from shorting crowded contracts. The price coefficient changes sign between a 2020-21 reversal regime (high funding preceded reversals) and a 2023-26 continuation regime (high funding preceded continuation). Open interest builds into and through high-funding settlements, refuting a flow reading and leaving the rate as a measurement of the basis.

### Research interpretation

The hypothesis is that the cross-sectional funding level captures a persistent basis property of each contract (how rich it trades relative to spot), not crowding or positioning. The regime flip implies that the direction of the basis-price relationship is not stationary: in early market periods, high funding preceded mean-reversion (crowding unwinds), but as markets matured and the interest-rate peg stopped binding (share of contract-days pinned at peg fell from 61% in 2023 to 7% in 2026), high funding began to predict continuation (the basis is informationally valid). The practical implication is that any cross-sectional funding strategy must be regime-aware or accept regime-dependent returns.

## Signal

### Formation timestamp

Decision times are 00:00 UTC daily. The funding rate at each decision time is the most recent settlement rate for each contract. Forward returns are computed from the close of the candle opening one hour earlier.

### Lookback

- **Funding z-score:** Rolling 90-day window of each contract's own settlements, then cross-sectional rank.
- **Tradability filter:** Trailing 90-day mean daily quote volume ≥ USD 5M, evaluated causally at each decision time.
- **Minimum cross-section:** At least 20 tradable names per day (drops 77 of 2281 days, all in 2020).

### Entry (research-defined)

Sort contracts on the 90-day z-scored funding rate. Long the bottom decile (lowest/ negative funding, where shorts pay longs), short the top decile (highest funding, where longs pay shorts). This is a dollar-neutral decile long-short book.

### Exit / holding period (research-defined)

- **Swing variant (preferred):** Rebalance every 3 days, hold 3 days. Cuts costs from 4.8 to 1.8 bps per day.
- **Daily variant:** Rebalance daily. Higher Sharpe but higher turnover.
- **Additive composite:** Top/bottom 20% on additive rank composite of open-interest change, reversal, and funding z-score, on 3-day swing.

### Parameters

- Z-score window: 90 days (research-proposed; raw level outperforms z-score at 24h horizon but z-score is more regime-stable).
- Decile / quintile legs: Top/bottom decile (full sample) or quintile (peak Sharpe in risk-managed analysis).
- One-way fee reference: 4 bps taker (varying the fee shows breakeven at 23.4 bps for swing variant).

### Holding period

3-day swing (research-proposed; Section 6 shows predictability decays to zero by 24 hours pooled, but the swing buys lower drawdown and lower turnover cost).

### Re-entry rules

Rebalance at each decision time (00:00 UTC every 3 days for swing variant).

### Position sizing (research-defined)

Equal-weighted across legs. No vol-scalling, no factor hedging (both tested and found not to improve the book).

## Required data

- **Instrument:** USDT-margined perpetual futures on Binance (primary), extended to two additional venues.
- **Universe:** All 791 listed USDT perpetuals including delisted contracts (survivorship-free). Tradable subset: 421 liquid contracts meeting the volume filter.
- **Venue:** Binance (primary), with cross-venue analysis on two additional venues.
- **Timeframe:** 8-hour funding settlements (or sub-8h where applicable), hourly klines, 5-minute open-interest snapshots aggregated to hourly.
- **Fields:** Funding settlement rate, premium index (1h and 8h), hourly OHLCV, open interest, long/short account ratio of top traders.
- **Point-in-time:** All archives public and frozen by manifest. Funding settlements verified against premium index archives at 0.61 bps median error.
- **Timestamp:** UTC throughout. Decision time 00:00 UTC daily.
- **Missing-data:** Open-interest coverage uneven: 2% in 2020, 11% in 2021, 99% in 2022, 72-85% thereafter. Missing rows dropped, not filled.
- **Funding/fee:** Reference schedule 4 bps one-way taker; breakeven analysis across the full fee curve.

## Execution assumptions

- **Signal-to-order timing:** Decision at 00:00 UTC, execution at the decision-time close.
- **Order type:** Market order (taker fee assumed).
- **Fill model:** Full fill assumed at close price; no partial fills modeled.
- **Fees:** 4 bps one-way taker reference; breakeven at 23.4 bps for swing variant.
- **Slippage:** Not separately modeled; included implicitly in the close-price execution assumption.
- **Funding:** Carry collected from settlements falling strictly inside the holding window, positive to a short.
- **Capacity:** Limited by smallest holding at ~USD 17M per leg (median trailing volume USD 9.3M/day for the smallest decile member). Raising the liquidity floor removes the price leg rather than scaling it.
- **Leverage/margin:** Not specified; implicit in dollar-neutral construction.
- **Liquidation:** Not modeled. A 36-position book of alt perpetuals at 23% annualized volatility with a -10% worst day carries unmodeled margin risk.

## Evidence

### Source-reported

- **Tradeable residue (z-score deciles, 3-day swing):** Net +8.9 bps/day, +32% annualized, Sharpe 1.42, maximum drawdown -40%, positive in 6 of 7 calendar years. Block bootstrap p(mean ≤ 0) < 0.001. Front-loaded: ~2/3 of cumulative net return from 2020-21.
- **Daily rebalance variant:** Net +10.4 bps/day, Sharpe 1.55. Paired difference vs. swing: +1.5 bps/day (t = 0.61, p = 0.27). Drawdown -44.8%.
- **Breakeven fee:** 23.4 bps one-way for swing variant (Table 4).
- **Capacity constraint:** At liquidity floors of 5/25/50/100M, price leg runs +5.7/+4.0/+2.5/-0.5 bps/day; Sharpe falls 1.42→1.02→0.71→0.35.
- **Regime flip (Table 3):** Yearly Spearman IC of raw funding level vs. next-24h return: -3.9% (2020), -3.1% (2021), +0.0% (2022), +0.6% (2023), +1.6% (2024), +3.4% (2025), +2.0% (2026).
- **One-hour effect:** Raw rate scores +1.89% IC at 1h (t = 6.26), +1.04% at 8h (t = 4.0), gone by 24h (+0.23%, t = 0.79). Pooled result averages two opposite regimes.
- **Open-interest cross-validation failure:** Pooled +34 vs +6 bps/day collapses to +7.0 at t = 0.35 once cohorts compared within same day.
- **Cross-venue index:** OI-weighted global index correlates with dominant venue's own rate at 0.975; weighting by OI makes index worse, not better.
- **Carry-to-risk trap:** Carry-to-risk ratio IC = +4.0% (t = 12.9), but inverse volatility alone scores +8.7% (t = 17.7); demeaning inside vol deciles leaves +0.3% (t = 1.3).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The result is front-loaded: excluding 2020-21, the swing variant nets +3.7 bps/day at Sharpe 0.77 (t = 1.63), not clearing a conventional threshold.
- The z-score preprocessing removes the only component with short-horizon predictability (the raw level), without creating new predictability.
- No cross-validation prescription (open interest, price, cross-venue index, dispersion) survives a within-day control.
- Carry-to-risk ranking, inverse-volatility sizing, and factor hedging all fail to improve the book.
- Holding only across the settlement timestamp fails on 1.73M settlements because price moves against the collector by more than the payment.
- The swing variant spends 85% of days >1% below high water mark, 46% >10% below, 22% >20% below.
- Variance ratio at 21 days is 1.23 (swing) and 1.68 (daily), deflating quoted Sharpe to 1.28 and 1.85.

## Falsification plan

1. **Regime stability:** If the 2023+ continuation regime reverts to the 2020-21 reversal pattern, the cross-sectional funding factor loses its short-horizon predictability. Test: rolling 252-day Spearman IC of funding level vs. 24h return; failure if IC turns persistently negative for >6 months.
2. **Capacity test:** Deploy at increasing liquidity floors (25M, 50M, 100M per leg); failure if price-leg Sharpe drops below 0.5 at any floor the strategy claims to trade at.
3. **Fee sensitivity:** At one-way fees above 23 bps, the swing variant's mean net return reaches zero; at fees above 9.7 bps, net Sharpe falls below 1.0.
4. **Regime-conditional performance:** Split sample at 2024; if the post-2024 effect decays to insignificance (t < 2.0) on a forward 12-month window, the regime flip hypothesis is weakened.
5. **Ablation of z-score:** If the raw level consistently outperforms the z-score on a traded basis (not just IC), the z-score preprocessing is unnecessary overhead.
6. **Out-of-sample on additional venues:** If the carry does not transfer to venues not in the original 3-venue analysis, the result may be venue-specific.

## Crypto portability

**Direct.** The study is conducted entirely on crypto perpetual futures (Binance USDT-margined). The mechanism (funding rate as basis measurement) is native to perpetual futures markets.

Crypto-specific considerations:
- **Funding settlement schedule:** 8-hour default but 541 of 791 contracts run on sub-8h schedules; the study works from the actual event stream.
- **Interest-rate peg:** The structural baseline (+0.01% per 8h, ~10.95% annualized paid by longs) is venue-specific. Other venues may have different pegs or no peg.
- **Venue fragmentation:** Cross-venue analysis shows OI-weighted index is dominated by the largest venue (correlation 0.975); multi-venue diversification does not help.
- **Liquidity:** Capacity is limited by the smallest holding in the decile book (~USD 17M per leg); alt perpetuals in the decile have thin markets.
- **Liquidation risk:** Not modeled; a 36-position book of alt perpetuals carries material unmodeled margin risk.
- **24/7 trading:** The study uses 00:00 UTC decision times; intraday decay of the one-hour effect is not characterized.

## Limitations

- **Front-loaded result:** ~2/3 of cumulative net return from 2020-21; excluding those years, the effect is below conventional significance.
- **Not independently reproduced:** All results are from the single GitHub repository.
- **Regime-dependent:** The 2020-21 and 2023+ regimes have opposite signs; pooled results average two regimes and are not actionable without regime detection.
- **Regime detection is unreliable:** Regressing daily IC on its own trailing average gives slope +0.65-0.78 (t = 5.7-6.6), but trading the sign of the trailing coefficient earns only +1.9-2.8 bps/day (t = 0.64-0.88, bootstrap p = 0.19-0.29).
- **Capacity binding:** At practical size, the price leg exists only in contracts too small to hold the position.
- **Liquidation not modeled:** Alt perpetual books carry margin risk not captured by return clips.
- **Carry-to-risk is a trap:** The ratio imports low-volatility alpha through its denominator.
- **One-hour effect mechanism unclear:** The settlement clock matters but is not the sole driver; the effect is concentrated in 00:00 UTC but not confined to settlement hours.
- **Open-interest coverage uneven:** 2% in 2020, 11% in 2021; open-interest-dependent analyses measured on subset.
- **Standard carry trade, not alpha:** The source explicitly states the tradeable residue is carry harvesting, not a price signal; the carry is an accrual at portfolio level and not per name.

## Implementation status

Not implemented. This is a research-only capture from a public GitHub repository.

## Adoption boundary

This record is research material only. It does not mean:
- Profitable;
- Validated alpha;
- Approved for implementation;
- Approved for paper trading;
- Approved for testnet;
- Approved for live trading.

The source explicitly frames the tradeable residue as carry harvesting (not alpha), with regime-dependent returns and capacity constraints that limit practical deployment.

## Related Wiki records

- [[crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11]] (Bryan Vine, different source, different methodology)
- [[crypto-perpetual-funding-rate-carry-spot-perp-2026-08-31]] (traditional academic papers on funding rate carry)
- [[crypto-funding-rate-feedback-regime-capital-stability-band-2026-09-12]] (Zhang 2026, SSRN, theoretical model of funding rate feedback)

## Sources

1. OctopusTakopi, "Funding Rates as a Cross-Sectional Factor in Perpetual Futures," GitHub repository, https://github.com/OctopusTakopi/funding-rate-alpha (2026). Survivorship-free test on 6.1M settlements across three venues, 2020-2026.
