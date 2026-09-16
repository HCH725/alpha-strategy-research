---
schema: strategy-research-record-v1
title: "[Algoros] BTC/ETH Sentiment Trader — Multi-Regime SOPR + Premium + USDT Dominance Daily Strategy"
created: 2026-09-16
updated: 2026-09-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
  - regime-filter
  - on-chain
  - derivatives
  - macro
status: research-only
confidence: medium
source_as_of: 2026-09-16
sources:
  - "TradingView public strategy page: https://www.tradingview.com/script/EaOTZsaH-Algoros-BTC-ETH-Sentiment-Trader/"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# [Algoros] BTC/ETH Sentiment Trader — Multi-Regime SOPR + Premium + USDT Dominance Daily Strategy

## Provenance

- **Source type:** TradingView public strategy (closed-source Pine Script, freely available for use)
- **Author:** algoros (TradingView profile: "We build Bitcoin and crypto algorithms with the intention to outperform")
- **Strategy name:** [Algoros] BTC/ETH Sentiment Trader — Sentiment Trader v4.1 Strategy
- **Source URL:** https://www.tradingview.com/script/EaOTZsaH-Algoros-BTC-ETH-Sentiment-Trader/
- **Source/data as-of:** Primary source page read 2026-09-16. Publication date stated as "Mar 7" on the page; exact year not explicitly stated — likely March 2025 or March 2026 based on version context. data gap.
- **Script type:** Protected/closed-source (TradingView protected source script), freely usable
- **Backtest period:** Not explicitly stated on the strategy page. The page reports "119 trades over the tested dataset" with "average holding time of about 30 days per trade." data gap — exact sample window not specified.

## Economic mechanism

### Source-reported

The strategy is described as a "rules-based BTC/ETH daily strategy that combines multiple market regime inputs." The author states it uses:

1. **Spot/Perp Premium model:** Tracks "crowd leverage and overheating" via the premium/discount between major perpetual futures (Binance, Bybit, OKX, Bitget) and spot markets. Elevated premium "tends to support short/risk-off setups"; compressed premium/discount "supports long/risk-on setups."
2. **SOPR filter:** Uses on-chain Spent Output Profit Ratio (Glassnode BTC_SOPR / ETH_SOPR) as a "profit-realization stress filter." High realized-profit regimes "can increase reversal risk"; reset/loss-absorption regimes "can improve long-entry quality."
3. **USDT Dominance:** Uses CRYPTOCAP:USDT.D to factor in "broader crypto market liquidity and risk-on/risk-off flows."
4. **Trend zone + context gating:** "Trend zone logic and context gates decide whether long or short candidates are allowed before an entry triangle is printed."

### Research interpretation

This is a **multi-input daily regime filter** combining three orthogonal market state variables:

1. **Derivatives leverage state** (spot/perp premium): Measures whether the market is overleveraged (positive premium = longs paying = crowding risk) or underleveraged (discount = potential capitulation). This is a positioning/crowding signal.
2. **On-chain profit realization state** (SOPR): Measures whether market participants are distributing profits (SOPR > 1, potential exhaustion) or absorbing losses (SOPR < 1, potential accumulation). This is a behavioral/flow signal.
3. **Macro liquidity state** (USDT dominance): Measures whether capital is flowing into stablecoins (risk-off, USDT.D rising) or out of them (risk-on, USDT.D falling). This is a capital-flow/regime signal.

The hypothesis is that combining these three regime dimensions produces a more robust daily trend-following signal than any single input alone. The economic thesis is: when leverage is moderate, on-chain participants are not excessively profitable (reducing distribution pressure), and capital flows are risk-on, long entries have higher expectancy;反之, when leverage is excessive, SOPR signals profit-taking, and USDT.D is rising, short entries have higher expectancy.

## Signal

- **Formation timestamp:** End-of-day (daily close). The strategy evaluates entries/exits on daily bar data.
- **Lookback:** Not explicitly specified. Trend zone logic and context gates are described but exact lookback windows are not disclosed (closed-source script).
- **Long entry:** Blue triangle below candle. Triggered when regime + trend gating allows long candidates and entry conditions are met. Specific entry rules are not disclosed (closed-source).
- **Short entry:** Pink/red triangle above candle. Triggered when regime + trend gating allows short candidates and entry conditions are met. Specific entry rules are not disclosed.
- **Exit:** Trailing-stop based exits. Close markers (X) print when stop/close conditions are met. Exact trailing stop parameters are not disclosed.
- **Holding period:** Average approximately 30 days per trade (source-reported, 119 trades over tested dataset).
- **Parameters:** Not fully disclosed (closed-source script). The three regime inputs (premium, SOPR, USDT.D) and trend zone logic are described conceptually but exact thresholds, lookback windows, and weighting are proprietary.
- **Position sizing:** 40% of equity per trade (backtest default setting).
- **Multi-timeframe dependencies:** Daily timeframe only. No multi-timeframe dependencies described.
- **Fully specified:** No — the script is closed-source; exact entry/exit rules, regime thresholds, and weighting are not publicly available. The strategy is underspecified for independent reconstruction.

## Required data

- **Instrument:** BTC/USD (BITSTAMP:BTCUSD required), ETH/USD (BITSTAMP:ETHUSD required)
- **Venue:** Bitstamp spot data for price; perpetual futures data from Binance, Bybit, OKX, Bitget for premium calculation
- **Market type:** Spot (price data) + Perpetual (premium calculation)
- **Timeframe:** Daily (1D)
- **Fields:**
  - OHLCV (daily candles from Bitstamp)
  - Spot/perp premium (computed from multiple exchange perp vs. spot)
  - SOPR (Glassnode: BTC_SOPR, ETH_SOPR)
  - USDT dominance (CRYPTOCAP:USDT.D)
- **Point-in-time:** SOPR and USDT.D are point-in-time available; premium requires real-time multi-exchange data
- **Timestamp:** Daily close, timezone implicitly UTC (TradingView default)
- **Missing-data:** If SOPR or USDT.D data is unavailable for a given day, the regime filter likely degrades (not specified in source)
- **Funding/fee/spread:** Not explicitly modeled in the source description; backtest uses 0.05% commission and 1 tick slippage

## Execution assumptions

- **Signal-to-order timing:** Daily close execution. Signals evaluated on daily bar data.
- **Next-bar vs same-bar execution:** data gap — not specified whether entries are on the same close or next open.
- **Market / limit order:** data gap — not specified.
- **Fill model:** data gap — not specified beyond 1 tick slippage.
- **Fees:** 0.05% commission per trade (backtest setting).
- **Slippage:** 1 tick (backtest setting).
- **Impact / capacity:** data gap — not specified. At 40% equity allocation on BTC/ETH daily, likely manageable for retail-size accounts.
- **Funding:** Not explicitly modeled in the backtest description.
- **Leverage / margin:** 1% margin for long and short positions in backtest settings (TradingView default, not indicative of actual leverage used).
- **Borrow / shorting:** Short positions are enabled in the strategy.
- **Latency:** Not material for daily timeframe.
- **Partial fills / failures:** data gap — not specified.

## Evidence

### Source-reported

From the TradingView strategy page (BTC/USD preset, backtest settings: $1000 initial capital, 40% equity per trade, 0.05% commission, 1 tick slippage):

- **Win rate:** 68.91%
- **Profit factor:** 3.551
- **Maximum equity drawdown:** 18.20%
- **Total trades:** 119
- **Average holding time:** ~30 days per trade
- **Average losing trade:** 8.06% on position (~3.2% on equity at 40% allocation)
- **Largest losing trade:** 10.54% on position (~4.2% on equity)
- **Comparison:** "Over the same dataset, this drawdown was lower than a simple buy-and-hold approach."

The ETH/USD preset is included as an additional option but its results are not represented in the BTC/USD statistics.

All figures are source-reported from the TradingView strategy page. The exact backtest period (start/end dates) is not stated on the page. data gap.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The script is closed-source; no independent verification of the claimed metrics is possible without recreating the regime logic.
- The exact backtest period is not stated, making it impossible to assess whether the results span sufficient market regimes (bull, bear, sideways).
- No out-of-sample or walk-forward results are reported.
- No transaction cost sensitivity analysis is reported (single fee assumption of 0.05%).
- No comparison against a risk-adjusted benchmark (e.g., Sharpe, Sortino) is reported — only win rate, profit factor, and max drawdown.

## Falsification plan

- **Required sample:** Reproduce the regime logic with公開可得的 data (SOPR from Glassnode, USDT.D from CRYPTOCAP, premium from exchange APIs) on a holdout period not used in the original backtest.
- **Relevant regimes:** Test across bull (2020-2021), bear (2022), and sideways (2023) regimes to verify the regime filter's robustness.
- **Baseline / control:** Compare against (a) buy-and-hold BTC, (b) simple trend-following (e.g., 50-day MA crossover) without regime filters, and (c) each regime input in isolation (SOPR-only, premium-only, USDT.D-only) to verify the marginal contribution of each component.
- **Ablation tests:** Test each regime input independently: (a) SOPR filter only, (b) premium filter only, (c) USDT.D filter only, (d) all three combined. `research-defined falsification threshold`: if any single input alone achieves comparable win rate and profit factor, the multi-input combination adds no measurable value.
- **Cost sensitivity:** Re-run at 0.10% and 0.20% commission to assess fee sensitivity. `research-defined falsification threshold`: if profit factor drops below 2.0 at 0.10% commission, the edge is fee-sensitive.
- **Out-of-sample requirement:** Walk-forward validation with rolling 12-month train / 3-month test windows.
- **Failure metric:** `research-defined falsification threshold`: if out-of-sample Sharpe < 0.5 or win rate drops below 55%, the regime filter hypothesis is materially weakened.
- **Action following failure:** If ablation shows one dominant input, simplify to that single input and test whether the other two add value.

## Crypto portability

**Direct** — the strategy is already designed for crypto (BTC and ETH perpetual/spot markets).

Crypto-specific considerations:
- The strategy uses daily timeframe, which avoids most intraday microstructure issues.
- SOPR is Bitcoin-specific on-chain data; ETH SOPR availability may be less reliable.
- USDT dominance is a crypto-native macro indicator.
- Spot/perp premium calculation requires multi-exchange data aggregation.
- The 30-day average holding period means funding rate costs are material but not dominant.
- Strategy is long/short, so funding costs affect both legs.

## Limitations

- **Closed-source script:** The exact entry/exit rules, regime thresholds, and weighting are not publicly available. Independent reconstruction is not possible.
- **Unspecified backtest period:** The exact start/end dates of the backtest are not stated, making it impossible to assess regime coverage.
- **No out-of-sample results:** Only in-sample backtest metrics are reported.
- **No risk-adjusted metrics:** Sharpe, Sortino, and other risk-adjusted metrics are not reported.
- **Single asset class tested:** BTC/USD results are reported; ETH/USD results are not included in the published statistics.
- **No walk-forward or robustness analysis:** No parameter sensitivity, walk-forward, or Monte Carlo results are reported.
- **Data gap:** Exact publication date (year) not confirmed from source page.
- **Data gap:** Exact backtest sample window not stated.
- **Data gap:** Next-bar vs same-bar execution not specified.
- **Not independently reproduced.**

## Implementation status

`not-implemented` — No implementation in our research stack has been completed. The script is closed-source and would require reverse-engineering the regime logic from the described inputs (premium, SOPR, USDT.D) and trend zone gating.

## Adoption boundary

This record is research material only. Presence in this repository does not mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

## Related Wiki records

- No directly related strategy research records share the same source identity or materially identical mechanism.
- Adjacent records that investigate similar regime inputs:
  - `[[quant/bitcoin-onchain-sopr-spent-output-profit-ratio-macro-cycle-2026-08-31]]` — uses SOPR as a standalone cycle indicator, not as a regime filter combined with premium and USDT.D.
  - `[[quant/bitcoin-options-implied-volatility-risk-reversal-skew-2026-09-01]]` — uses derivatives pricing data but focuses on options vol surface rather than spot/perp premium.

## Sources

1. algoros, "[Algoros] BTC/ETH Sentiment Trader," TradingView strategy page. Published "Mar 7" (year not explicitly stated on page). https://www.tradingview.com/script/EaOTZsaH-Algoros-BTC-ETH-Sentiment-Trader/. Accessed 2026-09-16.
