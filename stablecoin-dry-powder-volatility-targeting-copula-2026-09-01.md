---
schema: strategy-research-record-v1
title: "Stablecoin Dry Powder Volatility Targeting via Copula-Based Risk Transmission"
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - stablecoins
  - volatility-targeting
  - copula
  - risk-transmission
  - cross-asset
  - regime
status: research-only
confidence: medium
source_as_of: 2026-03-24
sources:
  - "Elliot Jones, Toshiko Matsui, William Knottenbelt, 'Stablecoins as Dry Powder: A Copula-Based Risk Analysis of Cryptocurrency Markets', arXiv:2603.23480v1 [cs.CE], March 24 2026. https://arxiv.org/abs/2603.23480"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Stablecoin Dry Powder Volatility Targeting via Copula-Based Risk Transmission

## Provenance

- **Source:** "Stablecoins as Dry Powder: A Copula-Based Risk Analysis of Cryptocurrency Markets" by Elliot Jones, Toshiko Matsui, William Knottenbelt
- **Venue:** arXiv:2603.23480v1 [cs.CE], March 24, 2026
- **URL:** https://arxiv.org/abs/2603.23480
- **Authors:** Department of Computing, Imperial College London, United Kingdom
- **Data source:** Investing.com daily OHLCV data
- **Sample period:** 2020-01-01 to 2025-01-01 (5 years daily)
- **No GitHub repository identified**

## Economic mechanism

### Source-reported

Stablecoins serve as the fundamental infrastructure for DeFi, acting as the primary bridge between fiat currencies and the digital asset ecosystem. The authors hypothesize that stablecoin volume and upside volatility function as "dry powder" — capital parked in stablecoins awaiting deployment into risk assets. When stablecoin upside volatility increases, it signals liquidity flowing into the stablecoin layer, either as a safe-haven during poor market conditions or as dry powder waiting for an impending rally. This creates a lead-lag relationship where stablecoin volatility dynamics predict broader cryptocurrency market volatility.

The authors demonstrate in-sample copula-based Granger causality from stablecoin factors to cryptocurrency factors across daily, weekly, and monthly horizons. Specifically:
- Stablecoin downside volatility causes cryptocurrency downside volatility at all horizons (p < 0.005)
- Stablecoin upside volatility causes cryptocurrency upside volatility at daily and weekly horizons (p < 0.005)
- Stablecoin volume causes cryptocurrency volatility at monthly horizons (p < 0.005), suggesting gradual dry powder accumulation

### Research interpretation

The hypothesized mechanism is **liquidity reservoir / dry powder effect**: stablecoins act as a staging area for capital entering or exiting crypto markets. Increases in stablecoin volume and upside volatility indicate capital accumulation that eventually flows into risk assets, creating predictable volatility patterns.

The economic channel is:
- Regime: Stablecoin market activity levels (dry powder availability)
- Primary signal: Asymmetric volatility spread between upside and downside components
- Confirmation: Stablecoin volume as long-term accumulation signal
- Risk management: Volatility targeting with confidence-scaled exposure

This is a **cross-asset lead-lag** mechanism, not a direct alpha signal. The stablecoin factors serve as a regime/macro indicator for positioning in the broader crypto market.

## Signal

### Formation timestamp

- Daily bars, UTC timezone
- Signal formed at end of day t (23:59:59 UTC), tradable at next market open (00:00:00 UTC day t+1)
- Model trained on expanding window; out-of-sample test on final year (2024)

### Lookback

- Rogers-Satchell upside/downside volatility computed from daily OHLCV
- E-GARCH filtering on PCA factors
- Rolling 60-day window for signal z-score computation
- Expanding training window (4 years train, 1 year test)

### Entry

- **Net Volatility Signal** S_{t+1} = (forecasted upside vol - forecasted downside vol) / (forecasted upside vol + forecasted downside vol)
- Positive signal → buy position (upside variance dominates, indicating dry powder deployment)
- Negative signal → no position (research-defined; source does not explicitly specify short entry)

### Exit

- Signal flips sign (research-defined threshold: S crosses zero)
- Volatility target reached (risk management override)
- Maximum holding period: 1 day (daily rebalance)

### Position sizing and risk management

- Volatility targeting framework with annualized volatility target (σ_target)
- Base exposure: Exp_base = σ_target / forecasted annualized volatility
- Confidence multiplier: Multiplier = 1 + tanh(z_S), where z_S is 60-day rolling z-score of signal
- Total exposure: Exp_total = Exp_base × Multiplier
- Portfolio weighting: Assets weighted by ratio of upside-to-downside PCA loadings (tilt toward assets more sensitive to upside volatility)

### Parameters

- Volatility target: 20% and 50% annualized (research-defined)
- GARCH model: E-GARCH with Skewed Student-t distribution
- XGBoost hyperparameters: tuned via expanding window (source does not specify exact values)
- PCA: First principal component retained for each factor category
- Winsorization: 1% and 99% quantiles on training data only

### Underspecified items

- Exact XGBoost hyperparameters not specified
- Entry/exit timing granularity beyond daily not specified
- Short entry rules not specified (source only describes long positions)
- Portfolio rebalancing frequency assumed daily but not explicitly stated

## Required data

- **Instruments:** BTC, ETH, BNB, XRP (cryptocurrencies); DAI, USDC, USDT (stablecoins)
- **Venue:** Data from Investing.com; strategy applicable to any major crypto exchange
- **Market type:** Spot prices and volumes
- **Timeframe:** Daily bars (OHLCV)
- **Fields:** Open, High, Low, Close, Volume for each asset
- **Timestamp:** UTC, daily session 00:00:00–23:59:59
- **Point-in-time:** Daily close data; no look-ahead issues for daily signals
- **Missing-data:** No explicit handling described; data assumed complete
- **Funding/fee/spread:** Not modeled in backtest

## Execution assumptions

- **Signal-to-order timing:** Next-day execution (signal formed at close, executed at next open)
- **Order type:** Market order (assumed)
- **Fill model:** Assumed full fill at next-day open
- **Fees:** Not included in reported results
- **Slippage:** Not included in reported results
- **Spread:** Not included in reported results
- **Leverage:** Determined by volatility targeting framework (can exceed 1x at 50% target)
- **Funding:** Not applicable for spot; not modeled for perpetuals

Source-reported results do not account for transaction costs. The Sortino ratios reported (up to 3.38) may degrade materially after fees.

## Evidence

### Source-reported

- **Causality testing:** Copula-based Granger causality test shows significant stablecoin → cryptocurrency causality across multiple factor pairs and horizons. Bootstrap-validated at 95th percentile with 200 synthetic datasets.
- **Statistical backtest:** Challenger model (crypto + stablecoin factors) achieves lower MSE than Benchmark (crypto only) in out-of-sample test. Diebold-Mariano test with HLN correction confirms statistical significance.
- **Volatility targeting performance (2024 out-of-sample):**
  - Buy & Hold: 89.0% ann. return, 51.4% ann. vol, -33.0% max DD, 2.47 Sortino
  - Benchmark (20% target): 40.8% return, 24.3% vol, -15.8% DD, 1.96 Sortino
  - Challenger (20% target): 46.6% return, 22.3% vol, -12.9% DD, 2.77 Sortino
  - Naive (20% target): 16.6% return, 19.7% vol, -18.6% DD, 1.10 Sortino
  - Benchmark (50% target): 95.8% return, 46.1% vol, -26.9% DD, 3.04 Sortino
  - Challenger (50% target): 100.4% return, 44.7% vol, -24.1% DD, 3.38 Sortino
  - Naive (50% target): 54.0% return, 38.9% vol, -30.2% DD, 2.00 Sortino
- All results are source-reported from a single out-of-sample year (2024) and have not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The authors note that stablecoin downside volatility does not lead cryptocurrency upside volatility at daily timescales, contrary to the expectation that dry powder deployment should be visible. They attribute this to the daily resolution — the effect likely occurs intra-day.
- The causal relationship is in-sample; the out-of-sample backtest covers only one year (2024), which includes specific market conditions (post-FTX recovery, ETF approval rally).
- The paper acknowledges that the regulatory landscape (GENIUS Act, Stablecoin Ordinance) may alter stablecoin dynamics in the future.

## Falsification plan

1. **Out-of-sample extension:** Replicate on 2025+ data with different market regimes (bear, sideways, high-volatility). Failure threshold: Challenger Sortino < 1.5 over any rolling 6-month period.
2. **Parameter perturbation:** Test sensitivity to volatility target (10%, 30%, 70%), z-score window (30-day, 90-day), and PCA component count (PC1 vs PC1+PC2). Failure: Rank reversal of Challenger vs Benchmark.
3. **Ablation:** Remove stablecoin volume factor; remove upside volatility factor; remove confidence multiplier. Each ablation should degrade performance relative to full model.
4. **Transaction cost stress:** Apply 5–10 bps round-trip costs. Failure: Challenger Sortino drops below Benchmark Sortino after costs.
5. **Regime breakdown:** Split sample into pre-ETF (2020–2023) and post-ETF (2024). Test causality and strategy performance separately.
6. **Alternative universe:** Test on mid-cap crypto universe (SOL, AVAX, LINK, MATIC) to assess generalizability.
7. **Competing explanation:** Test whether the effect is driven by overall market volume rather than stablecoin-specific dynamics by replacing stablecoin factors with aggregate crypto volume.

## Crypto portability

**Adapted**

The paper uses spot prices from Investing.com. Portability to perpetual futures requires:
- **Funding rate:** Not modeled; funding costs could erode returns on leveraged positions
- **Spot vs perpetual basis:** The strategy targets volatility, not basis; basis effects may distort position sizing
- **24/7 session:** Daily bars at UTC boundaries may miss intra-day stablecoin dynamics (acknowledged limitation by authors)
- **Venue fragmentation:** Data from Investing.com may not reflect exchange-specific dynamics
- **Liquidity:** BTC, ETH, BNB, XRP are highly liquid; mid-cap stablecoins (DAI) may have thinner markets
- **Stablecoin selection:** USDe was excluded due to 2024 launch; newer stablecoins may change the dynamic
- **On-chain data:** The paper uses CEX price data; on-chain stablecoin flows (minting, burning, bridge transfers) could provide richer signals

The mechanism (stablecoin dry powder → crypto volatility) is native to crypto and does not require adaptation from traditional markets.

## Limitations

- **Single out-of-sample year:** Results cover only 2024; insufficient for regime robustness
- **Daily resolution:** Intra-day stablecoin dynamics (the actual dry powder deployment) are not captured
- **No transaction costs:** Reported Sharpe/Sortino ratios ignore fees, slippage, and spread
- **In-sample causality:** The copula-based Granger causality is in-sample; out-of-sample causality not tested
- **PCA dimensionality:** Only first principal component retained; may miss idiosyncratic stablecoin signals
- **Winsorization:** Training data winsorized at 1%/99%; sensitivity to winsorization bounds not tested
- **Model complexity:** GARCH-Copula-XGBoost pipeline is non-trivial to implement and maintain
- **Data source:** Investing.com data may have quality issues vs direct exchange feeds
- **Publication bias:** Single paper from Imperial College London; no independent replication
- **Regulatory risk:** GENIUS Act and similar regulations may change stablecoin market structure

## Implementation status

not-implemented

No implementation in our research stack (PyBroker/Nautilus). The paper provides no public code repository.

## Adoption boundary

research-only

This record represents normalized research material from an external source. It does not imply:
- Profitable alpha
- Validated strategy
- Approved for implementation
- Approved for paper trading
- Approved for testnet
- Approved for live trading

## Related Wiki records

- `quant/bitcoin-stablecoin-supply-ratio-ssr-oscillator-2026-09-01.md` — Related stablecoin factor research (SSR oscillator)
- `quant/crypto-stablecoin-minting-issuance-inflow-momentum-shock-2026-09-01.md` — Related stablecoin flow research (minting shocks)
- `quant/crypto-usdt-severe-depeg-next-day-rebound-100d-3sigma-2026-09-01.md` — Related stablecoin event research (depeg rebound)
- `quant/crypto-cross-sectional-systematic-liquidity-risk-beta-2026-08-31.md` — Related liquidity risk transmission research

## Sources

- Elliot Jones, Toshiko Matsui, William Knottenbelt, "Stablecoins as Dry Powder: A Copula-Based Risk Analysis of Cryptocurrency Markets", arXiv:2603.23480v1 [cs.CE], March 24, 2026. https://arxiv.org/abs/2603.23480
