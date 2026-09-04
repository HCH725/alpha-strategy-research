---
schema: strategy-research-record-v1
title: "Ethereum Whale Deposit Asymmetric Sell Signal: Long-Horizon Edge, Withdrawal Decay, and Bull-Bear Regime Dependence"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - ethereum
  - onchain
  - whale
  - event-study
  - directional
  - cross-sectional
status: research-only
confidence: medium
source_as_of: 2026-09-04
sources:
  - "https://github.com/zty05070242/whale-signals (commit f0972c6ef6b214ce3faa8cb5521dc3a7b19b262c, 2026-09-04)"
  - "https://crypto-whale-signals-and-sentiment-lkhygb3594bbrogn23qbps.streamlit.app/"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - Withdrawal (buy) signals showed positive edge in 2023-2024 but decayed to zero or negative by 2025-2026; the study documents this as evidence of DeFi maturation diluting the buy signal.
  - The initially reported 78.3% hit rate for $10M+ deposits during extreme greed at 24h was retracted by the authors as clustering-driven and not confirmed under closer scrutiny.
---

# Ethereum Whale Deposit Asymmetric Sell Signal: Long-Horizon Edge, Withdrawal Decay, and Bull-Bear Regime Dependence

## Provenance

- **Repository:** https://github.com/zty05070242/whale-signals
- **Commit SHA:** `f0972c6ef6b214ce3faa8cb5521dc3a7b19b262c` (2026-09-04)
- **Key files:** `scripts/run_event_study.py`, `scripts/build_dashboard_data.py`, `app/dashboard.py`
- **Live dashboard:** https://crypto-whale-signals-and-sentiment-lkhygb3594bbrogn23qbps.streamlit.app/
- **Author:** Fred Zheng (2026)
- **Study type:** GitHub-hosted research project with public code, data pipeline, and interactive dashboard. Not peer-reviewed.
- **Sample:** 646,442 whale transactions (>$1M USD) on Ethereum, Jan 2023 – Jul 2026 (3.5 years).
- **Data sources:** Dune Analytics (whale transactions), Binance API (ETH/USDT hourly prices, ETH funding rates), alternative.me (Fear & Greed Index), Kaggle (BTC news headlines), GitHub open-source wallet labels (52,768 labels).

Source/data as-of date: 2026-09-04 (latest commit).

## Economic mechanism

### Source-reported

Large Ethereum holders ("whales") make informed directional decisions about ETH. When whales deposit ETH to exchanges, this signals intent to sell — the primary reason to deposit to an exchange is to sell. The study finds that whale deposits (sell signals) show a persistent, growing edge that strengthens with time horizon: +1.3% at 24h, +4.8% at 1 month, +12.4% at 6 months. Whale sellers are described as thinking in weeks and months, not hours — they see structural shifts ahead of the market.

In contrast, whale withdrawals (buy signals) showed positive edge in 2023-2024 (especially during negative funding: +4.7% to +10.1%) but decayed to zero or negative by 2025-2026. The study hypothesises this is due to DeFi maturation: withdrawals increasingly represent staking, liquidity provision, and L2 bridging rather than directional buying.

The study also finds that deposit edge is stronger in bear markets (+3.9% to +4.9% at 1-week) than bull markets (+0.5% to +2.2%), and that conditioning on extreme greed only helps at 24h (edge +1.3% to +2.2%) but hurts at longer horizons (up to -17.3% at 6 months).

### Research interpretation

The core hypothesis is that large Ethereum exchange deposits carry informational content reflecting informed selling pressure, and that this informational edge is more durable than the corresponding buy signal because the semantic meaning of deposits (intent to sell) has not changed, while the meaning of withdrawals has been diluted by non-directional DeFi activity.

**Hypothesized mechanisms:**
1. **Informed selling:** Large holders with structural views exit positions before long-horizon declines.
2. **Asymmetric information decay:** Sell signals (deposits) retain informational value because the meaning of "deposit to exchange" hasn't changed; buy signals (withdrawals) lose value because "withdraw from exchange" now encompasses staking, LP provision, and L2 bridging.
3. **Crowding asymmetry:** Whale-watching tools may amplify bullish activity (withdrawals) more than bearish activity (deposits), leaving sell signals less crowded and less arbitraged.
4. **Regime dependence:** In bear markets, whale selling reflects genuine recognition of further downside; in bull markets, selling is more often routine profit-taking with less informational content.

**Component roles (hybrid):**
- Signal: whale exchange deposit (>$1M threshold)
- Regime filter: bull/bear market (20%+ drawdown/rally from recent peak/trough)
- Sentiment context: Fear & Greed Index, funding rate (tested but mixed results)
- Holding horizon: 1 week to 6 months (edge grows with horizon)

## Signal

### Signal definition

- **Formation timestamp:** Upon block confirmation of a whale transaction (>$1M) classified as an exchange deposit. Block confirmation ~12 seconds after broadcast; monitoring/processing/execution adds further delay (source-reported limitation).
- **Direction:** Price expected to decline (sell signal for existing longs, or potential short entry).
- **Lookback:** Event-triggered; no lookback window for the primary signal.
- **Entry:** Upon whale exchange deposit detection (>$1M ETH to a known exchange address).
- **Exit:** At end of holding period (1h, 6h, 24h, 3 days, 1 week, 2 weeks, 1 month, 3 months, or 6 months — tested across all horizons).
- **Transaction classification:** Deposits = ETH sent TO a known exchange address (181,105 events, 28.0% of classified transactions). Withdrawals = ETH withdrawn FROM a known exchange address (124,772, 19.3%). Wallet-to-wallet (321,257, 49.7%) and DeFi interactions (19,308, 3.0%) are excluded from the primary signal.
- **Thresholds tested:** $1M+, $2M+, $5M+, $10M+ (USD notional at time of transaction).
- **Position sizing:** Not specified (event study, not a backtested strategy with sizing rules).
- **Holding period:** 1 hour to 6 months. Edge grows monotonically with horizon (deposit signal): 1h (+0.4%), 6h (+0.4%), 24h (+1.3%), 3 days (+1.4%), 1 week (+1.6%), 2 weeks (+1.8%), 1 month (+4.8%), 3 months (+8.0%), 6 months (+12.4%).

### Source-reported edge by horizon (deposits, unconditional, $1M+)

| Horizon | N | Hit Rate | Base Rate | Edge | Mean Return |
|---------|---|----------|-----------|------|-------------|
| 1h | 180,963 | 49.5% | 49.1% | +0.4% | +0.00% |
| 6h | 180,963 | 49.3% | 48.9% | +0.4% | +0.01% |
| 24h | 180,963 | 50.5% | 49.1% | +1.3% | +0.05% |
| 3 days | 180,880 | 49.9% | 48.5% | +1.4% | +0.09% |
| 1 week | 180,483 | 50.8% | 49.2% | +1.6% | +0.14% |
| 2 weeks | 179,833 | 52.9% | 51.1% | +1.8% | +0.12% |
| 1 month | 177,925 | 56.0% | 51.2% | +4.8% | +0.34% |
| 3 months | 170,165 | 55.0% | 46.9% | +8.0% | +1.16% |
| 6 months | 157,120 | 58.5% | 46.1% | +12.4% | +1.56% |

Source: GitHub README, Section 5 (Long-Horizon Analysis), full dataset, unconditional deposits.

### Source-reported edge by year (deposits, unconditional, $1M+)

| Horizon | 2023 Edge | 2024 Edge | 2025 Edge |
|---------|-----------|-----------|-----------|
| 24h | -0.2% | +0.9% | +1.8% |
| 1 week | +0.0% | -0.7% | +3.0% |
| 1 month | -3.8% | +4.4% | +3.6% |
| 6 months | +1.6% | +7.6% | +6.9% |

Source: GitHub README, Section 6. Deposit edge absent in 2023 (bear-to-bull transition), emerged in 2024, strengthened in 2025.

### Maximum Adverse Excursion (MAE) on eventually-correct deposit trades

| Horizon | N | Mean MAE | Median MAE | P90 MAE |
|---------|---|----------|------------|---------|
| 1 week | 91,764 | 2.7% | 2.0% | 6.2% |
| 1 month | 99,620 | 6.0% | 5.2% | 12.9% |
| 6 months | 92,904 | 20.1% | 13.3% | 54.4% |

Source: GitHub README, Section 7. Even correct deposit signals require surviving substantial adverse moves before payoff.

### Withdrawal (buy) signal — documented decay

Unconditional withdrawal edge at 24h: +0.4% (2023), -1.0% (2024), -1.7% (2025), -3.3% (2026). Negative funding-conditioned: +4.7% (2023), +10.1% (2024), +0.1% (2025), -3.9% (2026). At 6-month horizon, withdrawals are -12.9% wrong.

Source: GitHub README, Sections 3 and 5.

### Parameters

All parameters (thresholds, horizons, regime definitions, sentiment splits) are research-defined; none are described as tuned. However, the study acknowledges that thresholds are fixed USD values that may dilute over time as ETH price rises (~833 ETH at $1M in 2023 vs ~250 ETH at $1M in 2026).

## Required data

- **Instrument:** ETH (Ethereum native token), spot market.
- **Universe:** All Ethereum whale transactions >$1M USD, classified by destination/source address type (exchange deposit, exchange withdrawal, wallet-to-wallet, DeFi interaction).
- **Venue:** Binance API for ETH/USDT hourly prices and 8-hourly funding rates. Dune Analytics for on-chain whale transaction data. alternative.me for Fear & Greed Index.
- **Timeframe:** Hourly price data. 8-hourly funding rate data. Block-level transaction data (~12 second granularity).
- **Fields:** ETH/USDT OHLCV (hourly), ETH perpetual funding rate (8-hourly), Fear & Greed Index (daily), whale transaction amount (USD notional), wallet address labels (52,768 labels from open-source source).
- **Classification data:** Wallet address labels (open-source GitHub labels, 52,768 addresses) used to classify transactions as exchange deposit, exchange withdrawal, wallet-to-wallet, or DeFi interaction.
- **Point-in-time:** Whale transactions available after block confirmation (~12 seconds). Dune Analytics query latency adds further delay. Price data from Binance API. Wallet labels from a snapshot (version not specified).
- **Timestamp:** ETH block timestamps (UTC). Binance hourly candles aligned to UTC. Funding rate settlement every 8 hours (00:00, 08:00, 16:00 UTC).
- **Missing-data:** Not explicitly addressed in the source. The study does not discuss how Dune Analytics handles reorgs, label accuracy, or transaction classification errors beyond the 3% DeFi interaction category.
- **Funding/fee/spread:** Not modelled. The study reports raw hit rates and mean returns without deducting trading costs, slippage, or spread.

## Execution assumptions

- **Signal-to-order delay:** Block confirmation (~12 seconds) + monitoring/processing/execution delay (not quantified).
- **Order type:** Not specified (event study only, not a backtested strategy).
- **Fill model:** Not specified.
- **Fees:** Not modelled. Raw returns and hit rates are reported without fee deduction.
- **Slippage:** Not modelled.
- **Spread:** Not modelled.
- **Impact:** Not modelled.
- **Funding:** Not modelled for perpetual positions.
- **Leverage:** Not specified.
- **Shorting:** The sell signal could be implemented as closing a long position or entering a short; the study does not specify.
- **Latency:** Block confirmation ~12 seconds, plus monitoring latency (not quantified).
- **Capacity:** Not assessed. The study uses historical data without modelling market impact of large whale-driven moves.

All execution assumptions are gaps — the study is an event study, not a backtested strategy with execution modelling.

## Evidence

### Source-reported

1. **Deposit edge by horizon (unconditional, $1M+, full dataset):** Edge grows monotonically from +0.4% (1h) to +12.4% (6 months). Hit rate 58.5% at 6 months vs 46.1% base rate. Source: GitHub README, Section 5.

2. **Deposit edge by year (unconditional, $1M+):** Absent in 2023 (-0.2% at 24h), emerged in 2024 (+0.9%), strengthened in 2025 (+1.8% at 24h, +6.9% at 6 months). 2026 out-of-sample: +3.9% at 24h. Source: GitHub README, Section 6.

3. **Threshold stability:** Deposit edge stable across $1M+ to $10M+ thresholds and growing over time. 2026 edge: +2.9% to +3.9% across all four thresholds. Source: GitHub README, Section 4.

4. **Extreme greed conditioning:** Helps at 24h (+1.3% to +2.2% depending on threshold) but hurts at longer horizons (up to -17.3% at 6 months). Source: GitHub README, Section 5.

5. **Bull vs bear regimes:** At 1-week horizon, deposit edge is stronger in bear markets (+3.9% to +4.9%) than bull markets (+0.5% to +2.2%), consistent across all four thresholds. Source: GitHub README, Section 8.

6. **Withdrawal decay:** Unconditional withdrawal edge at 24h: +0.4% (2023) → -3.3% (2026). At 6 months: -12.9% wrong. Source: GitHub README, Sections 3 and 5.

7. **MAE:** Eventually-correct deposit trades at 6 months require surviving mean 20.1% adverse move, P90 of 54.4%. Source: GitHub README, Section 7.

8. **Classification:** 181,105 exchange deposits (28.0%), 124,772 withdrawals (19.3%), 321,257 wallet-to-wallet (49.7%), 19,308 DeFi interactions (3.0%). Source: GitHub README, Section 2.

All source-reported figures are from the GitHub README at commit `f0972c6ef6b214ce3faa8cb5521dc3a7b19b262c` (2026-09-04).

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Withdrawal (buy) signal failure:** Withdrawal edge decayed from +4.7%-10.1% (2023-2024, negative funding condition) to near zero or negative by 2025-2026. At 6 months, withdrawals are -12.9% wrong. Source: GitHub README, Sections 3 and 5.

2. **78.3% claim retracted:** The initially reported 78.3% hit rate for $10M+ deposits during extreme greed at 24h was retracted by the authors as clustering-driven (transactions concentrated in ~10 calendar days). Source: GitHub README, Discussion.

3. **Short-horizon weakness:** Deposit edge at 1h and 6h is negligible (+0.4%), indistinguishable from random. Source: GitHub README, Section 5.

4. **2023 deposit failure:** Deposit edge was absent or negative in 2023 during the bear-to-bull transition. Source: GitHub README, Section 6.

5. **Round-tripping contamination:** 24.1% of deposits see the same address withdraw within 24 hours, 29.1% within a week — inconsistent with a persistent multi-month directional view for a meaningful minority of events. Source: GitHub README, Limitations.

6. **Overlapping-observations problem:** At 1-month and longer horizons, thousands of whale events measure the same price move. Binomial p-values overstate significance. The study does not implement calendar-time portfolio or Kolari-Pynnönen adjusted test statistics. Source: GitHub README, Limitations.

7. **No cost/drawdown modelling:** Raw hit rates and mean returns without fee, slippage, or spread deduction. MAE analysis shows substantial adverse moves even on correct trades. Source: GitHub README, Sections 7 and Limitations.

## Falsification plan

1. **Out-of-sample extension:** Test the deposit signal on ETH price data from August 2026 onward using the same thresholds, horizons, and classification rules. **Failure rule:** If the deposit edge at 24h or 1 week falls below zero for any year after 2026, the signal is decaying. `research-defined falsification threshold`.

2. **Walk-forward yearly split:** Repeat the yearly analysis (Sections 3 and 6) with expanding-window or rolling-window train/test splits rather than the current in-sample (2023-2025) / out-of-sample (2026) split. **Failure rule:** If the deposit edge is not stable across at least 3 of 4 independent yearly samples at 1-week or longer horizons, the signal is unstable. `research-defined`.

3. **Calendar-time portfolio adjustment:** Implement the Kolari-Pynnönen (2010, 2018) adjusted test statistic or calendar-time portfolio method to correct for overlapping-observations. **Failure rule:** If adjusted p-values for the deposit edge exceed 0.05 at 1-month or longer horizons, the signal may be an artifact of event clustering. `research-defined`.

4. **ETH-denominated threshold:** Replace fixed USD thresholds with ETH-denominated thresholds (e.g., >500 ETH) to eliminate the dilution effect of rising ETH price. **Failure rule:** If the deposit edge disappears under ETH-denominated thresholds, the signal may be driven by composition effects rather than information. `research-defined`.

5. **Transaction cost sensitivity:** Model minimum execution costs (taker fee ~0.04-0.1%, slippage ~0.05-0.2% per side, spread ~0.01-0.05%) and test whether the 24h deposit edge (+1.3%) survives net of costs. **Failure rule:** If net-of-cost edge at 24h falls below zero, the short-horizon signal is not tradable. `research-defined`.

6. **Cross-venue replication:** Test the same signal on whale transactions across OKX, Bybit, or Coinbase, not just Binance-classified addresses. **Failure rule:** If the deposit edge does not replicate on at least one additional venue, the signal may be Binance-specific. `research-defined`.

7. **DeFi dilution test:** Trace post-withdrawal on-chain activity (did ETH go to a staking contract, LP pool, or cold wallet?) to validate or falsify the DeFi maturation hypothesis for withdrawal decay. **Failure rule:** If withdrawals to cold wallets still show positive edge, the DeFi dilution hypothesis is weakened. `research-defined`.

## Crypto portability

**Adapted**

The study is conducted entirely on Ethereum (ETH/USDT on Binance) using on-chain whale transaction data. The core mechanism — informed large holders moving assets to exchanges to sell — is specific to crypto markets where on-chain data is transparent and exchange addresses are identifiable.

**Crypto-specific portability considerations:**
- **On-chain transparency:** The signal depends on the availability of wallet address labels and exchange address identification. This is unique to crypto (blockchain-native data) and does not exist in traditional markets.
- **Exchange fragmentation:** The study uses Binance as the price venue but Dune Analytics for transaction data. Whale deposits to non-Binance exchanges may not be captured.
- **ETH vs BTC:** The study is ETH-only. The same mechanism could apply to BTC or other assets, but the specific edge magnitudes are unknown.
- **24/7 trading:** The study operates on 24/7 continuous data without session boundaries.
- **Perpetual funding:** Funding rate is used as a sentiment proxy but is not part of the primary signal.
- **Wallet label accuracy:** The study uses 52,768 open-source wallet labels. Accuracy and coverage of these labels is not validated.
- **DeFi-specific dynamics:** The withdrawal decay hypothesis is specific to Ethereum's DeFi ecosystem (staking, LP, L2 bridging). Other chains may have different dynamics.

## Limitations

- **Not peer-reviewed.** This is a GitHub-hosted research project with public code but no external peer review. The methodology and findings have not been independently validated by the academic community.
- **No cost modelling.** Raw hit rates and mean returns are reported without deducting fees, slippage, spread, or funding costs. The 24h deposit edge (+1.3%) may not survive transaction costs.
- **Overlapping-observations problem.** At 1-month and longer horizons, thousands of whale events measure the same price move. Binomial p-values overstate significance. The study does not implement standard corrections (Kolari-Pynnönen adjusted statistic, calendar-time portfolio). `underspecified` — the statistical significance of long-horizon results is not rigorously established.
- **Fixed USD threshold dilution.** A $1M threshold captured ~833 ETH in 2023 but ~250 ETH in 2026 as ETH price rose. The pool of "whales" diluted over time. `data gap` — the study does not test ETH-denominated thresholds.
- **Round-tripping contamination.** 24.1% of deposits see the same address withdraw within 24 hours, suggesting not all deposits reflect a persistent directional view. The aggregate pattern may still hold, but the "whale sellers think in months" narrative is weakened. `data gap` — no analysis of post-deposit activity is provided.
- **DeFi dilution hypothesis untested.** The study hypothesises that withdrawal edge decayed due to DeFi maturation but does not trace post-withdrawal on-chain activity to validate this. `not independently reproduced`.
- **Wallet label reliability.** The classification depends on 52,768 open-source wallet labels. Accuracy, completeness, and temporal stability of these labels are not validated. `data gap`.
- **On-chain latency.** Whale transactions are visible after block confirmation (~12 seconds), but monitoring, processing, and execution add further delay. The study does not quantify total signal-to-execution latency. `underspecified`.
- **Single asset, single venue.** ETH/USDT on Binance only. Cross-asset and cross-venue replication is not tested. `data gap`.
- **78.3% claim retracted.** The initially reported 78.3% hit rate was retracted by the authors as clustering-driven. This demonstrates the overlapping-observations problem can generate misleading headline statistics. Source: GitHub README, Discussion.

## Implementation status

**not-implemented**

No implementation in our research stack (PyBroker, Nautilus, or paper trading). The study provides public code (Python, Streamlit dashboard) but no execution-ready strategy. The source does not backtest a concrete trading strategy with entry/exit rules, sizing, risk management, or cost modelling — it is an event study measuring directional hit rates and mean returns at fixed horizons.

## Adoption boundary

**research-only**

This record is research material only. The presence of this record does not mean:
- The strategy is profitable.
- The edge survives transaction costs.
- The signal has been validated for live trading.
- The signal is approved for implementation, paper trading, testnet, or live trading.

The edge documented here (+1.3% at 24h, +12.4% at 6 months) is source-reported and has not been independently reproduced or validated net of costs.

## Related Wiki records

- `[[quant/ethereum-exchange-net-inflow-bearish-drift-1h-6h-2026-09-01]]` — Studies ETH exchange net inflow as a return predictor at 1-6 hour horizons using regression methodology on different data (Chi, Chu & Hao, arXiv:2411.06327). The current record is materially distinct: event study on whale deposits, different horizons (1h to 6 months), different methodology (hit rates vs. regression), different data source (Dune Analytics whale transactions vs. exchange net flow), and different key finding (deposit signal grows with horizon, withdrawal signal decays).
- `[[quant/ethereum-exchange-net-inflow-conditioned-call-selling-2026-09-03]]` — Same primary source as the above but different hypothesis (options selling conditioned on extreme inflows). Distinct from the current record.
- `[[quant/usdt-exchange-net-inflow-buy-side-liquidity-drift-1h-2h-2026-09-03]]` — Studies USDT deposits as buy-side liquidity predicting positive drift. Distinct: different asset (USDT vs ETH), different direction (buy vs sell), different horizon (1-2h vs 1h-6m).
- `[[quant/crypto-open-interest-crash-rebound-flow-gap-2026-09-03]]` — Open interest crash dynamics. Somewhat related to liquidation/forced selling but different mechanism and signal.

## Sources

1. Fred Zheng, "Are Ethereum Whales Smart Money? An Event Study of On-Chain Signals and Sentiment", GitHub repository https://github.com/zty05070242/whale-signals, commit `f0972c6ef6b214ce3faa8cb5521dc3a7b19b262c` (2026-09-04).
2. Live dashboard: https://crypto-whale-signals-and-sentiment-lkhygb3594bbrogn23qbps.streamlit.app/
3. Dune Analytics whale transaction data (free tier), 646,442 transactions, Jan 2023 – Jul 2026.
4. Binance API ETH/USDT hourly prices and 8-hourly funding rates, Jan 2023 – Jul 2026.
5. alternative.me Crypto Fear & Greed Index, Feb 2018 – Jul 2026.
