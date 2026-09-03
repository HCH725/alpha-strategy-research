---
schema: strategy-research-record-v1
title: "BTC-to-Small-Cap Altcoin 1-Minute Liquidity-Lag LightGBM Entry/Hold Strategy"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - lead-lag
  - liquidity
  - small-cap
  - high-frequency
  - lightgbm
status: research-only
confidence: medium
source_as_of: 2025-03-01
sources:
  - https://doi.org/10.1007/s10690-026-09589-z
  - https://link.springer.com/article/10.1007/s10690-026-09589-z
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# BTC-to-Small-Cap Altcoin 1-Minute Liquidity-Lag LightGBM Entry/Hold Strategy

## Provenance

Primary source: Tomoki Kurihara and Takuji Matsumoto, **"Price Transmission from Bitcoin to Altcoins: High-Frequency Evidence and Implications for Trading Strategy"**, *Asia-Pacific Financial Markets* (2026). DOI: `10.1007/s10690-026-09589-z`. Version of record published 2026-03-10; accepted 2025-12-31.

The source is open access and uses Binance API data at 1-minute frequency. The main analysis studies four deliberately selected regimes: Bull (2024-02-25 to 2024-03-25), Bear (2024-06-22 to 2024-07-19), Sideways (2024-08-24 to 2024-09-24), and Crash (2025-01-30 to 2025-03-01). For each regime used in trading simulation, the first three weeks are in-sample and the final week is out-of-sample. Appendix 1 adds Bull (2024-10-24 to 2024-11-22) and Bear (2024-04-02 to 2024-05-01) subsamples using the same three-week / one-week split.

The detailed focal universe contains BTC, ETH, LTC and five low-trade-count small-cap assets selected from Binance: QKC, GNO, PIVX, CITY and BIFI. The authors also use 369 cryptocurrencies in the Bull regime and 381 in the Bear regime for the liquidity-versus-response-speed hypothesis test.

Repository-wide source-identity checks on 2026-09-04 found no existing record containing DOI `10.1007/s10690-026-09589-z` or the exact paper title. Existing records on crypto lead-lag effects are related but materially distinct. In particular, `crypto-cross-cryptocurrency-lead-lag-adaptive-lasso-10m-2026-09-01.md` uses adaptive-LASSO cross-coin forecasting up to ten minutes, while `crypto-cross-asset-seesaw-lead-lag-rotation-2026-08-31.md` focuses on negative large-cap-to-small-cap cross-predictability and daily capital rotation. This record instead captures a positive one-minute BTC-to-low-liquidity-altcoin delayed-response mechanism, a two-feature LightGBM classifier, and separate entry/hold decision rules.

## Economic mechanism

### Source-reported

The authors report that low-liquidity altcoins incorporate BTC price information more slowly than large- and medium-cap cryptocurrencies. They define an Immediate Sensitivity Indicator (ISI):

`ISI = rho_0 - (1/5) * sum_{i=1..5}(rho_{-i})`

where `rho_0` is the contemporaneous BTC/ALT return correlation and negative lags represent BTC leading the ALT. A higher ISI indicates more immediate adjustment, while a lower ISI indicates more delayed response.

Across the Bull and Bear regimes, the source reports positive correlations between log trade count and ISI: 0.561 in the Bull regime and 0.483 in the Bear regime, both statistically significant at the stated 5% one-sided level. The authors therefore interpret low trade count as being associated with slower information incorporation.

The source also reports one-minute Granger-causality evidence running predominantly from BTC to ALTs, with the reverse direction usually absent, and VAR / impulse-response results indicating that small-cap altcoins retain delayed responses to BTC shocks for several minutes while ETH and LTC react much more contemporaneously.

### Research interpretation

The falsifiable mechanism is **liquidity-constrained information diffusion**. BTC incorporates common crypto-market information quickly because it has deep liquidity and concentrated attention. Thinly traded altcoins may need one or more additional minutes for arbitrageurs and directional traders to transmit the same shock into their prices. If this mechanism is real, the lag should be strongest in lower-trade-count assets and should weaken as trade intensity rises.

This is not generic cross-sectional momentum. The focal predictive edge is a causal-timing hypothesis: after BTC moves in minute `t-1`, a sufficiently slow small-cap altcoin may still have residual same-direction adjustment left in minute `t`.

## Signal

### Source-reported construction

- **Timeframe:** 1-minute logarithmic returns.
- **Features at `t-1`:**
  - BTC 1-minute log return `r_BTC,t-1`;
  - focal ALT 1-minute log return `r_ALT,t-1`.
- **Model:** LightGBM binary classification.
- **Two classifiers per ALT:**
  - `f_entry(x_{t-1})` for deciding whether to enter when currently flat;
  - `f_hold(x_{t-1})` for deciding whether to continue holding when already long.
- **Labels:** whether the next-period ALT return exceeds a predefined profitability threshold. The source predicts threshold exceedance rather than the continuous next return.
- **Position state:** `omega_t` is binary: 1 = holding, 0 = flat. Initial state is flat.
- **Entry rule:** if flat at `t-1` and the entry classifier predicts 1, become long at `t`.
- **Hold rule:** if long at `t-1` and the hold classifier predicts 1, remain long at `t`; otherwise exit to flat.
- **No source-reported short leg.** The strategy is long-or-flat.
- **Parameter search:**
  - entry threshold grid: `{-0.0001, 0, 0.0001, 0.0002}`;
  - hold threshold grid: `{-0.0002, -0.0001, 0, 0.0001}`.
- **Optimization objective:** maximize average lag-strategy cumulative return across `{QKC, GNO, PIVX, CITY, BIFI}` during the in-sample period.
- **Selected thresholds:** source reports `theta_hold = -0.0001` for all main regimes; `theta_entry = 0` for Bull and Crash, and `theta_entry = 0.0001` for Sideways.
- **ETH/LTC transfer test:** ETH and LTC use the small-cap-optimized parameters rather than separately tuned thresholds.

### Underspecified items

The paper does not fully specify all details required for a production-grade reconstruction:

- exact LightGBM hyperparameters and random seeds;
- exact classifier training/validation protocol within each three-week in-sample window;
- whether class weights, early stopping or calibration are used;
- the exact timestamp convention for Binance 1-minute bars;
- whether model inference occurs exactly at minute close or after a processing delay;
- exact executable entry/exit price;
- whether the source return accounting implicitly assumes access to the next minute at its opening boundary without spread/slippage;
- partial fills, queueing and stale-bar treatment.

These items are `underspecified` and must not be silently invented as source-reported rules.

## Required data

- **Venue:** Binance.
- **Market type:** source uses Binance cryptocurrency price data; exact spot-pair contract mapping for every asset should be verified before replication.
- **Quote/reference:** BTC is discussed in USDT terms; pair-level quote currency for each ALT must be reconstructed from the source/data snapshot.
- **Frequency:** 1-minute.
- **Fields:** 1-minute closing prices and trade count are explicitly source-required; realistic replication additionally needs bid/ask or trade data for executable spread/slippage estimates.
- **Universe:** BTC, ETH, LTC, QKC, GNO, PIVX, CITY, BIFI for the detailed strategy study; broader 369/381-asset cross-sections for liquidity-response analysis.
- **Point-in-time requirements:** listing status, symbol mapping and market availability must be known at each timestamp. The five small-cap assets were selected using low trade count during the Bull regime; a modern replication must avoid using future liquidity information to preselect assets.
- **Timestamp:** source uses 1-minute data but does not fully specify timezone/candle-boundary details in the reviewed article text; this is a `data gap` that must be resolved before causal replication.
- **Missing data:** no silent imputation. Stale, missing or zero-trade minutes need an explicit policy because the hypothesis is directly about low trade activity.
- **Costs:** source models a fee rate of 0.02% per buy or sell state change. Spread, slippage and market impact require additional observed or modeled data.

## Execution assumptions

### Source-reported

The source charges a 0.02% fee whenever the holding state changes because of a buy or sell. Buy-and-hold pays fees at initial purchase and final exit. Lag-strategy cumulative return is accumulated only while `omega_t = 1` and subtracts the stated fee on each state transition.

The reported strategy is long-or-flat; it does not require margin borrowing, perpetual funding or a short leg.

### Research interpretation

The central execution risk is **one-minute causal timing**. The model uses information from `t-1` to earn ALT return at `t`, but the exact source fill convention is not fully stated. A leakage-safe implementation must form the feature vector only after all `t-1` data are observable, then execute no earlier than the first genuinely tradeable timestamp after model inference.

Any replication using the close of minute `t-1` as both the final feature price and the guaranteed fill price is `research-proposed` and must be stress-tested against delayed execution. Spread, slippage, latency and market impact are especially important because the targeted assets are intentionally low-liquidity.

No leverage, stop-loss, take-profit, position sizing overlay or shorting rule is specified by the source. Adding any of these would be `research-proposed`.

## Evidence

### Source-reported

The source reports the following:

- In both Bull and Bear regimes, lower trade count is associated with slower immediate BTC-response speed; the trade-count/ISI correlation is 0.561 and 0.483 respectively, with the stated null of no positive correlation rejected at the 5% level.
- One-minute BTC returns improve prediction of ALT returns in Granger tests for all tested pairs in the stated analysis, while reverse ALT-to-BTC relationships are generally absent.
- For the five small-cap assets, delayed one-minute BTC response is visible in cross-correlation, VAR and impulse-response analysis; large/medium-cap ETH and LTC are much more contemporaneous.
- The selected hold threshold is `-0.0001` across the main Bull, Sideways and Crash strategy regimes. Entry thresholds are 0 for Bull/Crash and `0.0001` for Sideways.
- During the main final-week out-of-sample tests, the authors report that the lag strategy ends with higher cumulative returns than buy-and-hold for the small-cap cryptocurrencies across the evaluated regimes; ETH and LTC perform relatively poorly under the small-cap-tuned thresholds.
- Appendix 1 reports similar directional results in additional Bull and Bear subsamples, with lag trading outperforming buy-and-hold for all tested cryptocurrencies except LTC and ETH.
- Trading fees are modeled at 0.02% per buy/sell state change.

These are third-party source-reported findings. The source itself notes that the primary asset set is limited, that the signal may decay as market participation improves, and that cross-exchange generalization remains unverified.

### Independently reproduced

not independently reproduced

### Negative evidence

- Large- and medium-cap ETH/LTC exhibit little useful lag and relatively low strategy cumulative returns when the small-cap parameters are transferred to them.
- The Sideways regime produces the lowest lag-strategy cumulative returns among the reported main regimes, which the source associates with inconsistent trends and gradual price changes.
- The main trading evaluation uses only one final week as OOS per regime, so the effective independent test horizon is short.
- Five focal small-cap assets are hand-selected after examining trade-count characteristics during the Bull regime; this creates a serious selection / generalization concern even though final-week testing is held out within each regime.
- The source does not report a complete market-impact or spread/slippage reconstruction, despite intentionally targeting low-liquidity assets.
- Cross-venue evidence is absent.

## Falsification

1. **Strict post-publication OOS test** — Recreate the source signal on point-in-time Binance data after 2025-03-01 without reusing the source's asset selection or thresholds for tuning. `research-defined falsification threshold`: materially reject the hypothesis if the low-trade-count ALT basket does not produce positive net incremental return over buy-and-hold / flat baselines after realistic fees and spread in a predeclared 2025-2026 holdout.
2. **Liquidity-gradient test** — Form point-in-time trade-count deciles and estimate one-minute BTC-to-ALT lag response by decile. `research-defined falsification threshold`: reject the liquidity-delay mechanism if lag coefficients / predictive IC do not become systematically stronger toward lower-liquidity deciles or if the gradient reverses across most independent subperiods.
3. **Own-return control** — Compare `[BTC_{t-1}, ALT_{t-1}]` LightGBM against an ALT-own-return-only model. `research-defined falsification threshold`: reject incremental BTC information if the BTC feature does not improve OOS log loss / AUC and net trading return beyond sampling error.
4. **BTC shuffle placebo** — Randomly permute BTC one-minute returns within day while preserving ALT chronology. `research-defined falsification threshold`: if shuffled BTC produces comparable OOS classifier and trading performance, treat the claimed BTC information channel as falsified.
5. **Execution-delay stress** — Delay fills by 1, 5, 15 and 30 seconds after the minute boundary using quote/trade data. `research-defined falsification threshold`: if the edge is non-positive after a plausible operational delay plus observed spread/slippage, classify the strategy as statistically interesting but operationally untradeable.
6. **Parameter perturbation** — Test nearby entry/hold thresholds without selecting the best values on the final test set. `research-defined falsification threshold`: materially weaken the claim if profitability exists only at the exact source grid optimum and changes sign under small neighboring threshold changes.
7. **Universe selection audit** — Replace ex-post named assets with a point-in-time low-trade-count universe reconstituted at each training window. `research-defined falsification threshold`: reject general low-liquidity portability if the effect is confined to QKC/GNO/PIVX/CITY/BIFI and disappears in contemporaneous low-liquidity peers.
8. **Venue robustness** — Repeat on at least one other sufficiently liquid CEX with synchronized 1-minute data. `research-defined falsification threshold`: treat the effect as Binance-specific if the BTC lead signal is absent or opposite on independent venues after clock alignment.
9. **Regime breakdown** — Predeclare Bull/Bear/Sideways/Crash classification without future information. `research-defined falsification threshold`: reject any claim of regime-general robustness if net performance is positive only in one regime or only after ex-post regime labeling.

## Crypto portability

**direct**

The source is natively cryptocurrency research using Binance 1-minute data. The primary portability question is not asset-class translation but **market-structure persistence**: whether the same low-liquidity delayed-response effect still exists on modern Binance and on other venues after faster market making, cross-venue arbitrage and improved infrastructure.

Perpetual-futures implementation is not source-reported. Any adaptation to perpetuals is `research-proposed` and would require funding, mark/index price, liquidation, contract-availability and derivatives-liquidity modeling.

## Limitations

- `not independently reproduced`.
- Small focal strategy universe: only five low-trade-count small-cap assets, plus ETH/LTC transfer tests.
- Very short OOS window: one week per reported regime split.
- Asset selection may embed regime-specific selection bias.
- Main regime definitions are tied to notable historical BTC events; generality outside event-driven regimes is unproven.
- Exact LightGBM hyperparameters and training controls are `underspecified` in the reviewed public article text.
- Exact signal-to-fill timestamp and executable price are `underspecified`.
- Spread, slippage and market impact are not reconstructed at order-book level in the source-reported strategy accounting.
- Trade count is a coarse liquidity proxy and may not represent executable depth.
- Binance-only evidence; cross-venue persistence is `unproven`.
- One-minute lead-lag alpha may decay structurally as arbitrage competition improves.

## Implementation status

No implementation has been performed in PyBroker, NautilusTrader or any other internal research/trading stack in this Scout cycle.

`implementation_status: not-implemented`

This record creates no implementation task and makes no change to any strategy registry, data pipeline, Kanban, Paper, Testnet or Live workflow.

## Adoption boundary

This record is research material only. Presence in the Alpha Strategy Pool means only that the source has been normalized for later intake review.

It does not mean the strategy is profitable, validated, approved for implementation, approved for paper trading, approved for testnet, or approved for live trading.

`status: research-only`

`adoption: not-approved`

`approval_scope: research-only`

## Related Wiki records

No Hermes Wiki Brain strategy record was used or modified in this Scout cycle beyond read-only resolution of the canonical strategy-research specification.

Related Alpha Strategy Pool records reviewed for deduplication:

- `crypto-cross-cryptocurrency-lead-lag-adaptive-lasso-10m-2026-09-01.md`
- `crypto-cross-asset-seesaw-lead-lag-rotation-2026-08-31.md`

## Sources

1. Kurihara, Tomoki; Matsumoto, Takuji. **"Price Transmission from Bitcoin to Altcoins: High-Frequency Evidence and Implications for Trading Strategy."** *Asia-Pacific Financial Markets* (2026). DOI: https://doi.org/10.1007/s10690-026-09589-z. Published 2026-03-10. Version of record 2026-03-10. Public full text: https://link.springer.com/article/10.1007/s10690-026-09589-z. Data source in the paper: Binance API; main data through 2025-03-01.
