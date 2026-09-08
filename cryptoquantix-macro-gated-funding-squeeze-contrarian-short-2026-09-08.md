---
schema: strategy-research-record-v1
title: "CryptoQuantix Macro-Gated Funding Squeeze Contrarian Short for BTC Perpetual"
created: 2026-09-08
updated: 2026-09-08
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - funding-rate
  - contrarian
  - macro-gate
  - BTC
  - Binance
  - Deribit
  - trend-following
  - multi-component
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - "CryptoQuantix/CryptoQuantix GitHub repository. Repository URL: https://github.com/CryptoQuantix/CryptoQuantix. Commit SHA: 6090c26c630aaa7cdb3bfcfe4788824c600f4662. File: src/strategies/funding_squeeze.py. Author: Antonio Trento. Submitted: 2026-06-11. Code co-authored with Claude (Anthropic)."
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# CryptoQuantix Macro-Gated Funding Squeeze Contrarian Short for BTC Perpetual

## Provenance

- **Repository:** https://github.com/CryptoQuantix/CryptoQuantix
- **Full commit SHA:** `6090c26c630aaa7cdb3bfcfe4788824c600f4662`
- **File path:** `src/strategies/funding_squeeze.py`
- **Relevant config:** `config.py` (FundingSqueezeConfig dataclass, same commit)
- **Author:** Antonio Trento (repo owner)
- **Submission date:** 2026-06-11
- **License:** Source-available dual license (free personal use, paid commercial)
- **Source as-of:** 2026-09-08 (verified from primary source code)

## Economic mechanism

### Source-reported

The author states that when longs pay funding at the exchange cap (0.01%/8h) during a macro downtrend, the long position is extremely crowded and likely to unwind via forced liquidations or voluntary capitulation. The strategy exploits this crowded long positioning by entering a contrarian short. The naive version (funding > 0.005% + price below SMA48h) suffered two failure modes over 4 years: (1) bleeding in bull phases where funding stays positive, and (2) trend transitions in 2025 where relief rallies hit wide stop losses. The author fixed both by requiring funding AT the exchange cap (0.01%/8h) AND a confirmed macro bear gate (SMA200d declining).

### Research interpretation

The mechanism is **crowded positioning + macro trend confirmation**. The hypothesis is:

1. **Regime filter (macro gate):** Daily close < SMA200d AND SMA200d slope negative (30-day lookback). This ensures the strategy is only active in confirmed downtrends, not in shallow dips or bull-phase noise.

2. **Primary signal (funding extreme):** Funding rate ≥ 0.01%/8h (the exchange cap on Binance/Bybit). At this level, longs are paying maximum carry, indicating extreme crowding on the long side. This is a proxy for leveraged long positioning reaching exhaustion.

3. **Confirmation:** Last closed 1h bar close < SMA48(1h), confirming the short-term trend is also down.

4. **Timing gate:** Entry only within 60 minutes after a funding settlement (00/08/16 UTC). The edge was validated on this specific event timing — entering well after settlement may dilute the signal.

The economic thesis is that funding-rate extremes at the cap, when combined with a confirmed macro downtrend, indicate a crowded long that is about to unwind — and the unwind is accelerated by liquidation cascades on perpetual futures venues.

## Signal

- **Formation timestamp:** Funding rate is observed at each 8h settlement (00:08/16 UTC). Signal is evaluated once per 1h bar, but only within 60 minutes after a funding settlement.
- **Lookback:** SMA48h (1h candles) for trend confirmation. SMA200d (daily candles) + SMA200d slope over 30 days for macro gate.
- **Long entry:** Not applicable — strategy is SHORT-only.
- **Short entry:** Within 60 minutes after funding settlement, ALL of: (a) funding rate ≥ 0.0001 (= 0.01%/8h, the exchange cap), (b) last closed 1h close < SMA48(1h), (c) daily close < SMA200d, (d) SMA200d current < SMA200d from 30 days ago. Market order, one position at a time.
- **Exit:** SL = entry + 2.0 × ATR(1h, 14). TP = entry − 2.0 × risk (2R). Time exit after 24h.
- **Holding period:** Maximum 24 hours. Expected hold varies with SL/TP hit timing.
- **Re-entry rules:** Cooldown of 8 hours after exit (one trade per funding window). One open trade at a time.
- **Parameters (all defaults from FundingSqueezeConfig):**
  - `funding_threshold`: 0.0001 (0.01%/8h = exchange cap)
  - `sma_h`: 48 (1h bars)
  - `atr_period`: 14
  - `sl_atr_mult`: 2.0
  - `tp_rr`: 2.0 (TP at 2R)
  - `max_hold_hours`: 24
  - `cooldown_hours`: 8
  - `macro_sma_days`: 200
  - `slope_days`: 30
  - `entry_window_min`: 60
- **Position sizing:** Risk-manager dynamic sizing based on entry price, SL distance, ATR percentile (50), regime (TREND_DOWN), model win rate (0.45). Minimum 10 USD notional (Deribit BTC-PERPETUAL step).

## Required data

- **Instrument:** BTCUSDT (Binance data), BTC-PERPETUAL (Deribit execution)
- **Venue:** Binance (data), Deribit (execution)
- **Market type:** Perpetual futures (USD-M)
- **Timeframe:** 1h candles (signal evaluation), daily candles (macro gate), 1m candles (backtest reference data)
- **Fields:** OHLCV (1h and 1d), funding rate (8h settlement)
- **Timestamp:** UTC, epoch-aligned to funding settlement schedule (00/08/16 UTC)
- **Missing-data:** If daily SMA200 cannot be computed (insufficient data), strategy stands aside. If funding data unavailable, strategy stands aside.

## Execution assumptions

- **Signal-to-order timing:** Market order immediately after signal generation (within the 60-minute entry window post-funding settlement).
- **Fill model:** Market order with guaranteed fill (Deribit BTC-PERPETUAL).
- **Fees:** 0.10% per side (0.20% roundtrip) used in backtest (source: config and backtest scripts).
- **Slippage:** Not explicitly modeled in backtest; source describes backtest as using "realistic costs" with 0.20% roundtrip.
- **Spread:** Not explicitly modeled.
- **Impact / capacity:** Not stated in source. Strategy is low-frequency (15 trades over 4 years), so capacity is unlikely to be binding for the source's capital base.
- **Leverage / margin:** Not explicitly stated; Deribit BTC-PERPETUAL supports up to 100x but sizing is risk-managed.
- **Latency:** Not stated. Assumes real-time funding rate and candle data.
- **Partial fills / failures:** Not modeled in backtest.

## Evidence

### Source-reported

The following are directly from the source code docstrings and commit message (commit `6090c26c630aaa7cdb3bfcfe4788824c600f4662`):

**4-year multi-cycle backtest (Jun 2022 – Jun 2026, BTCUSDT 1m, costs 0.20% roundtrip):**
- Final config: **+74 bps/trade**, PF 3.05, WR 60%, **15 trades** (low frequency by design).
- 2025 reduced to −1% (source attributes to regime transition).
- This is a deep-bear capitulation specialist — designed to be inactive for most of the market cycle.

**270-day IS/OOS (Sep 2025 – Jun 2026):**
- Top-quintile funding → next-24h returns: **−46 bps IS** (t = −2.1), **−102 bps OOS** (t = −3.4).
- This was the discovery dataset; the 4-year validation exposed failure modes that led to the macro gate refinement.

**Failure modes identified and fixed:**
1. Bull phases: funding stays positive → bleeding −23 bps/trade → fixed by macro bear gate.
2. Trend transitions (2025 −20%): funding stays positive early in downtrend, relief rallies hit wide SL → fixed by requiring funding AT the cap AND SMA200d slope negative.

**Source states PF ≥ 1.2 and robustness to neighboring parameters as validation gates (per the microevolutive pipeline defined in `microevolutive/PLAN_BULL_EVOLUTION.md`).** Live guardrails: rolling PF < 0.8 over ≥ 30 trades → deactivation; drawdown > 1.5× backtest maxDD → immediate deactivation.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Low trade count (15 over 4 years) raises statistical significance concerns — small-sample backtest results may reflect noise rather than robust alpha.
- The strategy was negative in 2025 (−1%), attributed to regime transition, but this is the most recent full year of data and may indicate the macro gate is insufficient in certain bear-to-bull transition regimes.
- The source acknowledges that without the macro gate, the strategy bleeds in bull phases and during trend transitions — the gate was added post-hoc to fix observed failures, which raises overfitting concerns.
- The 270-day IS/OOS discovery sample used a less restrictive threshold (top-quintile funding, not just cap-level), and the switch to cap-only threshold was made after observing failures on the 4-year data — this is a form of in-sample refinement that weakens OOS claims.
- Source reports no audited live-capital results; backtest only.

## Falsification plan

1. **Out-of-sample walk-forward test:** Partition the 4-year dataset into rolling 9-month IS / 3-month OOS windows. Verify the macro gate + funding cap combination holds across subperiods. **Failure threshold:** OOS Sharpe < 0 or PF < 1.0 over any two consecutive OOS windows. **Action:** Reject the strategy.
2. **Parameter perturbation:** Test funding threshold at 0.005%, 0.01%, and 0.015%. Test SMA200d slope_days at 15, 30, and 60. **Failure threshold:** No parameter combination yields PF > 1.5 with ≥ 10 trades. **Action:** Mark as unstable.
3. **Cost sensitivity:** Test at 0.10%, 0.20%, and 0.40% roundtrip. **Failure threshold:** Strategy becomes unprofitable (net PF < 1.0) at 0.30% roundtrip. **Action:** Mark as cost-sensitive.
4. **Venue generalization:** Test on ETH-PERP (Binance/Bybit) with the same parameters. **Failure threshold:** Net PF < 1.0 on ETH. **Action:** Mark as BTC-specific.
5. **Regime ablation:** Remove the macro gate entirely and test on the full 4-year sample. **Failure threshold:** Unfiltered version shows negative returns or PF < 0.8. **Action:** Confirm the gate is load-bearing (which the source already claims but it should be independently verified).
6. **Falsification metric:** If net PF < 1.0 after costs on any walk-forward OOS period, the strategy is falsified for that regime.

## Crypto portability

**Direct** — this strategy is already designed and implemented for crypto perpetual futures (BTC-PERPETUAL on Deribit, data from Binance). No porting required.

**Crypto-specific risks:**
- Funding rate schedules vary by venue (Binance 8h, Bybit 8h, OKX 8h, Hyperliquid per-second). The 0.01%/8h cap is Binance-specific; other venues may have different caps.
- 24/7 trading means funding settlements occur continuously; the entry-window timing gate (60 min post-settlement) is sensitive to venue-specific settlement timestamps.
- Liquidation cascades can amplify or dampen the signal unpredictably depending on venue-specific liquidation engine mechanics.

## Limitations

- **Low trade count:** 15 trades over 4 years. Statistical significance is weak; the PF 3.05 and WR 60% may not be robust.
- **Overfitting risk:** The macro gate (SMA200d + slope) was added post-hoc to fix observed failure modes in the naive version. This is a form of data snooping that weakens OOS reliability.
- **Backtest-only:** No paper, testnet, or live results reported.
- **Single-asset:** Only validated on BTC-PERPETUAL. Multi-asset generalization is untested.
- **Cost model:** Uses 0.20% roundtrip but does not explicitly model slippage, spread, or market impact.
- **No independent reproduction:** Source is a single GitHub repo with 1 star and no external validation.
- **2025 performance:** −1% in the most recent full year. The strategy may be entering a regime where its signal is less effective.
- **Source quality:** GitHub implementation (not peer-reviewed). Author is a solo developer. Code co-authored with Claude (Anthropic).

## Implementation status

Not implemented in our research stack. The strategy exists only as source code in the CryptoQuantix GitHub repository. No NautilusTrader, PyBroker, paper, testnet, or live implementation has been completed on our side.

## Adoption boundary

This record is research material only. Presence in this repository does NOT mean:
- The strategy is profitable
- The strategy is validated alpha
- The strategy is approved for implementation
- The strategy is approved for paper trading
- The strategy is approved for testnet
- The strategy is approved for live trading

## Related Wiki records

- [[quant/strategy-research-record-spec-v1]] (schema specification)

No directly related strategy research records were identified in the repository that share the same source identity or materially identical mechanism. The existing record `extreme-negative-funding-contrarian-btc-return-2026-09-06.md` (Memon et al. 2026) studies the opposite funding extreme (negative funding → contrarian long) and is academically sourced; it is mechanistically distinct from this source.

## Sources

1. CryptoQuantix/CryptoQuantix. Repository: https://github.com/CryptoQuantix/CryptoQuantix. Commit: `6090c26c630aaa7cdb3bfcfe4788824c600f4662` (2026-06-11). File: `src/strategies/funding_squeeze.py`. Author: Antonio Trento. Primary source verified from raw file and commit diff.
2. CryptoQuantix/CryptoQuantix. File: `config.py` (FundingSqueezeConfig dataclass, same commit). Backtest validation parameters and results embedded in config docstrings.
3. CryptoQuantix/CryptoQuantix. File: `scripts/backtest_new_strategies.py` (same commit). 4-year backtest pipeline and validation metrics.
4. CryptoQuantix/CryptoQuantix. File: `microevolutive/PLAN_BULL_EVOLUTION.md`. Validation pipeline definition (referenced in README and strategy docstrings).
