---
schema: strategy-research-record-v1
title: "Crypto Volatility Forecast Loss Choice vs Model Choice: Forecast-Level Alignment and Downstream Value-at-Risk Overlay (arXiv:2609.27024)"
created: 2026-09-25
updated: 2026-09-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - volatility-forecasting
  - loss-function
  - level-alignment
  - value-at-risk
  - risk-overlay
status: research-only
confidence: medium
source_as_of: "2026-09-22 (arXiv v1 submission date); empirical data through 2026-05-31"
sources:
  - https://arxiv.org/abs/2609.27024
  - https://arxiv.org/html/2609.27024v1
  - https://arxiv.org/pdf/2609.27024v1
  - https://doi.org/10.48550/arXiv.2609.27024
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Volatility Forecast Loss Choice vs Model Choice: Forecast-Level Alignment and Downstream Value-at-Risk Overlay (arXiv:2609.27024)

## Provenance

- **Primary Source:** Andrzej Tokajuk (`andrzej.tokajuk.stud@pw.edu.pl`) and Jarosław A. Chudziak (`jaroslaw.chudziak@pw.edu.pl`), Warsaw University of Technology, Warsaw, Poland.
- **Paper Title:** *"Loss Choice or Model Choice? The Role of Forecast Level in Cryptocurrency Volatility Forecasting"*.
- **Version & Identifiers:** `arXiv:2609.27024v1 [q-fin.CP]` (cross-listed to `cs.AI`, `cs.CE`, `q-fin.RM`), submitted Tuesday, 22 September 2026 20:08:43 UTC.
- **Publication Status:** Preprint on arXiv with author-declared acceptance in peer-reviewed conference proceedings: `Comments: Accepted for publication in the proceedings of ADMA 2026` (The 22nd International Conference on Advanced Data Mining and Applications). No publisher DOI or journal volume assigned as of capture.
- **Digital Object Identifier:** DataCite DOI [10.48550/arXiv.2609.27024](https://doi.org/10.48550/arXiv.2609.27024), resolves HTTP 302 to `https://arxiv.org/abs/2609.27024` (verified HTTP 200 on 2026-09-25).
- **License:** Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (`CC BY-NC-ND 4.0`). Text below is normalized, quoted, and analytically structured; no source text is copied wholesale.
- **Pinned Primary Snapshot:**
  - HTML full text: `https://arxiv.org/html/2609.27024v1`, 113,140 bytes, SHA-256 `65cdb911b0c30c5d1b4d11672cd2d8d52c3f1b57003493abae4b3cab196e7c79`, read in full on 2026-09-25 (Sections 1–7, Tables 1–4, Equations 1, References [1]–[17]).
  - PDF full text: `https://arxiv.org/pdf/2609.27024v1`, 368,410 bytes, SHA-256 `02e04ffa9761918a377b1f76e55e1f9cb58ae4d19b0d018440799da603b7b8a8`, verified matching version v1.
- **Code & Replication Package:** No public GitHub repository, GitLab link, or code availability statement is provided in the pinned text (`data gap`).
- **Data Vendor / Source:** Daily Binance USDT spot OHLCV data through 31 May 2026.
- **Pre-write Deduplication:** Audited repository working tree and `coverage_manifest.csv` via ripgrep on 2026-09-25 for `2609.27024`, `Tokajuk`, `Chudziak`, and `Loss Choice or Model Choice`. Exactly 0 matching records were found prior to this write.

## Economic mechanism

### Source-reported

In cryptocurrency markets, volatility forecasts are foundational inputs for position sizing, dynamic risk parity, volatility targeting, and Value-at-Risk (VaR) constraints. However, empirical literature routinely benchmarks predictive architectures (e.g., linear HAR vs. Deep Learning or Tree Ensembles) under a single arbitrary training loss, or compares training losses under an evaluation metric that inherently favors its own training target.

The authors prove and demonstrate empirically that different training loss functions target distinct statistical functionals of the conditional volatility distribution $\mathcal{F}_t$:
1. **Log-error losses** (MSE-log, Huber-log, Pinball) penalize proportional log errors, targeting conditional geometric means or medians ($\exp(m_\delta)$), which systematically under-forecast mean variance.
2. **Mean-targeting losses** (QLIKE, Patton-$b$) are Bregman divergences that target the conditional expected variance $\mathbb{E}[h_{t+1}|\mathcal{F}_t]$.
3. **Relative-error losses** (HMAE, HMSE) penalize under-predictions heavily, targeting $h$-weighted medians or variance-weighted second moments ($\mathbb{E}[h^2|\mathcal{F}_t] / \mathbb{E}[h|\mathcal{F}_t]$), systematically producing higher forecast levels.

Because of this functional divergence, raw comparative evaluations conflate:
- **Persistent forecast-level bias** (a static multiplicative scaling shift), and
- **Day-to-day dynamic ranking capability** (the model's ability to anticipate volatility expansions and contractions).

In linear autoregressive models (HAR, HAR-X), 85% to 89% of cross-loss variation is pure static level offset. For tree-based models (LightGBM), only 56% is level offset, indicating that loss function choice substantially alters daily rank sensitivity and threshold splits. Applying a single validation-based multiplicative alignment factor $c = \frac{1}{|V|} \sum_{t \in V} \frac{h_t}{f_t}$ removes 97% of cross-loss downstream VaR breach dispersion.

### Research interpretation

This paper provides an empirical foundation for a **volatility-timing risk overlay hypothesis**:
- Raw apparent outperformance of loss functions (e.g., QLIKE over MSE-log or HAR over LightGBM under QLIKE) in crypto volatility modeling is predominantly a static calibration artifact rather than dynamic timing alpha.
- When an out-of-sample level alignment factor $c$ is applied, cross-loss dispersion collapses, and the residual variation is dominated by model architecture rather than training loss.
- Specifically, linear models (HAR, HAR-X) possess rigid, loss-invariant dynamic trajectories that merely shift vertically; nonlinear tree ensembles (LightGBM) maintain genuinely distinct daily rank signals under different loss penalties.
- In a risk-controlled trading system, separating the static level multiplier (calibrated via walk-forward validation) from the dynamic rank predictor prevents spurious parameter churn and avoids uncalibrated VaR breaches during crypto regime shifts.

Component roles in a risk-managed strategy:
```text
Regime / Volatility Signal: Multi-factor GBDT (LightGBM) or HAR-X predicting next-day log variance.
Calibration Overlay:        Validation-estimated scalar multiplier c ensuring empirical mean alignment.
Dynamic Exposure Sizing:    Inverse-volatility position scaling w_t ∝ 1 / sqrt(c * f_t) with volatility targeting.
Risk Boundary / VaR Filter: 1-day 5% VaR barrier triggering de-risking or hedge activation when return breaches threshold.
```

## Signal

### Predictor & Target Formulation

- **Target Definition:** One-day-ahead unannualized Garman-Klass variance proxy ($h_{t+1}$):
  $$h_{t+1} = 0.5 \left(\log \frac{\mathrm{High}_{t+1}}{\mathrm{Low}_{t+1}}\right)^2 - (2\log 2 - 1) \left(\log \frac{\mathrm{Close}_{t+1}}{\mathrm{Open}_{t+1}}\right)^2$$
  Robustness targets evaluated: Parkinson variance (high-low range) and Rogers-Satchell variance (drift-independent).
- **Target Transformation:** All models predict log-variance $\hat{z}_{t+1} = \log h_{t+1}$, transformed to natural variance units via $f_{t+1} = \exp(\hat{z}_{t+1})$.
- **Predictor Sets:**
  - *HAR:* Daily ($h_t$), weekly ($\frac{1}{5}\sum_{i=0}^4 h_{t-i}$), and monthly ($\frac{1}{22}\sum_{i=0}^{21} h_{t-i}$) log variance.
  - *HAR-X:* HAR predictors plus daily returns, leverage interaction terms ($\min(R_t, 0)$), alternative proxies (Parkinson, Rogers-Satchell), volume, and lagged BTC variance for altcoins.
  - *NeuralHAR:* Neural network with identical HAR-X predictor set.
  - *DLinear:* Linear decomposition over 48-day target history.
  - *LightGBM:* Gradient boosting trees with identical HAR-X predictor set.
- **Training Loss Functions:**
  1. *MSE-log:* $L(h, f) = (\log h - \log f)^2$
  2. *Huber-log:* $\rho_\delta(u)$ with $\delta = 1.0$, where $u = \log h - \log f$
  3. *Pinball (median):* $L(h, f) = 0.5 |u|$
  4. *QLIKE:* $L(h, f) = \frac{h}{f} - \log \frac{h}{f} - 1$
  5. *Patton-$b$ ($b = -1$):* $L(h, f) = f - h + h (\log h - \log f)$
  6. *HMAE:* $L(h, f) = |\frac{h}{f} - 1|$
  7. *HMSE:* $L(h, f) = (\frac{h}{f} - 1)^2$

### Validation-Based Forecast-Level Alignment

- **Alignment Factor Estimation:** Estimated on validation set $V$:
  $$c = \frac{1}{|V|} \sum_{t \in V} \frac{h_t}{f_t}$$
- **Out-of-Sample Alignment:** Applied multiplicatively to out-of-sample test forecasts:
  $$f_{t+1}^{\mathrm{aligned}} = c \cdot f_{t+1}$$
  This scalar minimizes validation QLIKE with respect to constant scaling, adjusting the persistent level without altering daily rank ordering.

### Downstream Risk Overlay & Position Sizing (`research-proposed`)

The primary source evaluates statistical scores and 1-day 5% Gaussian Value-at-Risk:
$$\mathrm{VaR}_{t+1} = -q_{0.05} \sqrt{f_{t+1}} \approx -1.64485 \sqrt{f_{t+1}}$$
where $q_{0.05} \approx -1.64485$ is the 5th percentile of the standard normal distribution.

To convert this diagnostic into an operational risk-overlay signal (`research-proposed`):
1. **Dynamic Volatility Scaling:** Base exposure $w_{t+1}$ on target asset $i$ is scaled by target volatility $\sigma^*$:
   $$w_{t+1} = \min\left(w_{\max},\ \frac{\sigma^*}{\sqrt{f_{t+1, i}^{\mathrm{aligned}}}}\right)$$
   where $w_{\max} = 1.5$ (`research-proposed`), $\sigma^* = 0.40$ annualized ($\approx 0.021$ daily, `research-proposed`).
2. **Tail-Risk Brake:** If realized return $R_t < \mathrm{VaR}_t$, exposure is halved ($w_{t+1} \leftarrow 0.5 \cdot w_{t+1}$) for a 3-day cooldown period (`research-proposed`).
3. **Execution Timing:** Decision formed at daily close $t$; order executed on bar open $t+1$ (`research-proposed`). Timezone convention: UTC 00:00 (`research-proposed`, unstated by source).

## Required data

- **Universe:** 5 major cryptocurrencies: BTC, ETH, BNB, XRP, ADA.
- **Venue:** Binance spot market against USDT.
- **Time Horizon:** 5 October 2017 (BTC, ETH) or respective Binance listing dates (BNB, XRP, ADA) through 31 May 2026.
- **Data Granularity:** Daily OHLCV bars.
- **Required Fields:**
  - `open`, `high`, `low`, `close`, `volume`.
  - Derived Garman-Klass, Parkinson, and Rogers-Satchell variance proxies.
  - Lagged BTC volatility series broadcast to altcoin feature tables.
- **Availability / Point-in-Time:** Volatility proxies are computed strictly prior to lagging; all inputs for day $t+1$ are available at the close of day $t$. No lookahead leakage.
- **Timezone / Session Boundary:** Not explicitly specified by source (`data gap`; assumed UTC 00:00–23:59:59 standard Binance convention, `research-proposed`).

## Execution assumptions

- **Source Stance:** The primary paper is an empirical econometric and machine learning study of volatility forecasting and Value-at-Risk breach rates; it does **not** simulate portfolio P&L, transaction fees, slippage, or order-book market impact (`data gap`).
- **Signal-to-Execution Delay:** Daily bar close to next bar open (`research-proposed`).
- **Transaction Costs & Slippage (`research-proposed`):**
  - Binance spot taker fee: 7.5 to 10 bps.
  - Slippage model: 5 bps for BTC/ETH, 10 bps for BNB/XRP/ADA under normal liquidity.
  - Funding rate / borrow: Zero on spot (long-only or cash). If ported to perpetual futures, 8-hour funding rates must be deducted.

## Evidence

### Source-reported

All figures below are extracted directly from Tokajuk & Chudziak (arXiv:2609.27024v1, September 2026). Sample covers 5 crypto assets across 5 expanding walk-forward folds (25 asset-fold blocks), test windows ending 31 May 2026:

1. **RQ1: Raw Variation Across Losses vs. Models:**
   - Median loss-to-model score variation ratio $\Delta_L / \Delta_M = 2.91$ (95% stationary bootstrap CI $[2.27, 3.25]$), indicating cross-loss differences are ~2.9x larger than cross-model differences.
   - Under shared predictors: ratio is $2.73$ (95% CI $[2.01, 3.44]$).
   - Asset-level median ratio spans $1.44$ to $4.55$.
   - Alternative evaluation scores: ratio is $3.71$ under MSE-log and $3.98$ under HMAE.
   - Volatility proxy robustness: loss rankings have Spearman rank correlations of $1.000$ with Rogers-Satchell and $0.964$ with Parkinson proxies.
2. **RQ2: Table 1 (Table 2 in source) — Mean Test QLIKE Across 25 Blocks (lower is better):**
   - *MSE-log:* HAR 0.772, HAR-X 0.734, DLinear 0.751, NeuralHAR 0.718, LightGBM **0.684**.
   - *Huber-log:* HAR 0.812, HAR-X 0.771, DLinear 0.786, NeuralHAR 0.746, LightGBM **0.703**.
   - *Pinball:* HAR 0.836, HAR-X 0.785, DLinear 0.808, NeuralHAR 0.763, LightGBM **0.713**.
   - *QLIKE:* HAR 0.592, HAR-X 0.578, DLinear 0.594, NeuralHAR **0.576**, LightGBM 0.637.
   - *Patton-$b$:* HAR 0.597, HAR-X 0.591, DLinear 0.677, NeuralHAR **0.586**, LightGBM 0.625.
   - *HMAE:* HAR 0.728, HAR-X 0.704, DLinear **0.646**, NeuralHAR 0.709, LightGBM 0.649.
   - *HMSE:* HAR 1.243, HAR-X 1.178, DLinear 0.873, NeuralHAR 1.051, LightGBM **0.659**.
3. **RQ2: Table 2 (Table 3 in source) — LevelShare and Cross-Loss Log-QLIKE Variation Reduction:**
   - *HAR:* LevelShare = $89\%$, Raw variation = $0.322$, Aligned variation = $0.040$, Variation reduction = $88\%$.
   - *HAR-X:* LevelShare = $85\%$, Raw variation = $0.307$, Aligned variation = $0.049$, Variation reduction = $84\%$.
   - *NeuralHAR:* LevelShare = $80\%$, Raw variation = $0.246$, Aligned variation = $0.058$, Variation reduction = $76\%$.
   - *DLinear:* LevelShare = $71\%$, Raw variation = $0.186$, Aligned variation = $0.073$, Variation reduction = $61\%$.
   - *LightGBM:* LevelShare = $56\%$, Raw variation = $0.121$, Aligned variation = $0.050$, Variation reduction = $59\%$.
   - *Aggregate:* Level alignment reduces cross-loss variation by $77\%$ overall (95% CI $[72\%, 79\%]$).
   - Post-alignment loss-to-model ratio inverts from $2.91$ to $0.67$ (95% CI $[0.56, 0.99]$), placing the confidence interval strictly below 1.
4. **RQ3: Table 3 (Table 4 in source) — One-Day 5% Gaussian Value-at-Risk:**
   - *Pinball:* Raw magnitude vs. QLIKE = $-21.3\%$, Raw breach rate = $6.31\%$, Aligned breach rate = $3.60\%$.
   - *Huber-log:* Raw magnitude = $-20.6\%$, Raw breach rate = $6.23\%$, Aligned breach rate = $3.61\%$.
   - *MSE-log:* Raw magnitude = $-19.1\%$, Raw breach rate = $5.92\%$, Aligned breach rate = $3.57\%$.
   - *QLIKE:* Raw magnitude = $+0.0\%$, Raw breach rate = $3.68\%$, Aligned breach rate = $3.59\%$.
   - *Patton-$b$:* Raw magnitude = $+0.8\%$, Raw breach rate = $3.68\%$, Aligned breach rate = $3.57\%$.
   - *HMAE:* Raw magnitude = $+24.7\%$, Raw breach rate = $2.19\%$, Aligned breach rate = $3.48\%$.
   - *HMSE:* Raw magnitude = $+68.7\%$, Raw breach rate = $1.28\%$, Aligned breach rate = $3.55\%$.
   - Raw breach rates span $1.28\%$ to $6.31\%$ ($5.03$ percentage points range); alignment compresses breach rates into a narrow $3.48\%$ to $3.61\%$ band ($0.13$ percentage points range), removing $97\%$ of cross-loss breach-rate variation.
   - Kupiec unconditional coverage test: Rejects correct 5% coverage in 128 of 175 series before alignment, and in 109 of 175 series after alignment.

### Independently reproduced

`Not independently reproduced.` The figures above are third-party empirical findings reported by Tokajuk & Chudziak (arXiv:2609.27024v1). No internal simulation or re-estimation has been performed by this research scout.

### Negative evidence

1. **Failure of Gaussian Tail Calibration:** Despite removing 97% of cross-loss breach rate variation, aggregate aligned breach rates remain between 3.48% and 3.61%—significantly below the nominal 5.0% target. The Kupiec test rejects correct coverage in 109 of 175 series even after alignment, demonstrating that constant scaling cannot correct for crypto return leptokurtosis, jump clustering, or fat tails.
2. **Absence of Trading Cost & P&L Modeling:** The primary source omits portfolio execution, turnover, spread, and transaction fees entirely. While statistical QLIKE improves, there is no proof that aligned volatility forecasts yield net positive alpha or superior Sharpe ratios after realistic Binance trading frictions.
3. **Static Alignment Vulnerability during Structural Breaks:** Alignment factor $c$ is a constant estimated over the preceding validation window. In crypto market transitions (e.g., sudden shift from low-volatility summer grind to high-volatility liquidation cascade), a static multiplier will lag the new variance regime.
4. **Restricted Asset Universe:** Only 5 top-tier, highly liquid crypto assets (BTC, ETH, BNB, XRP, ADA) were evaluated. Mid-cap and low-cap tokens with frequent illiquid halts or extreme low-float wicks were not tested.

## Falsification plan

To falsify the hypothesis that validation-based level alignment isolates genuine dynamic ranking and stabilizes downstream risk overlays:

1. **F1 (Out-of-Sample Level Reduction Failure):** Replicate the 5-model, 7-loss walk-forward evaluation on out-of-sample Binance data from June 2026 to December 2026.
   - *Research-defined falsification threshold:* If validation-based level alignment fails to reduce cross-loss QLIKE variation by at least $50\%$ (against the source's $77\%$) on the new window, reject the universality of static level calibration.
2. **F2 (Downstream Volatility-Targeting Horse Race):** Construct an active volatility-targeted crypto portfolio on BTC and ETH, rebalanced daily with target volatility $\sigma^* = 40\%$, comparing unaligned vs. aligned LightGBM/HAR-X forecasts under 10 bps round-trip transaction costs.
   - *Research-defined falsification threshold:* If the net realized Sharpe ratio or maximum drawdown of the aligned portfolio is not statistically superior ($p > 0.05$) to a naive 20-day rolling realized volatility benchmark, falsify the economic utility of the complex ML volatility overlay.
3. **F3 (Dynamic Multiplier vs. Static Multiplier Test):** Test an exponentially weighted moving average (EWMA) tracking multiplier $c_t$ against the static validation scalar $c$.
   - *Research-defined falsification threshold:* If dynamic tracking reduces QLIKE by more than $15\%$ relative to static $c$, reject the hypothesis that a single static scalar captures sufficient level information.
4. **F4 (Fat-Tail / Student-$t$ VaR Rectification):** Replace the Gaussian quantile $q_{0.05}$ with an empirical filtered historical simulation or Student-$t$ quantile.
   - *Research-defined falsification threshold:* If Kupiec test failure rate does not drop below $20\%$ of series under fat-tailed specifications, conclude that volatility forecasting alone is insufficient for crypto tail-risk management without explicit jump modeling.

## Crypto portability

- **Status:** `direct`. The primary study is natively conducted on Binance spot cryptocurrency data (BTC, ETH, BNB, XRP, ADA) from 2017 to 2026.
- **Perpetual Futures Adaptation:** When porting the volatility forecast from spot to perpetual contracts:
  - Intraday funding-rate payment timestamps (every 8 hours on Binance) can generate localized volatility spikes not present in spot.
  - Liquidation cascades on perpetual venues produce extreme High-Low wicks that distort Garman-Klass variance; Rogers-Satchell or jump-filtered bipower variation may be required.
  - Basis dislocation between spot and perpetual prices during deleveraging events must be monitored.

## Limitations

- **No Implementation in Execution Engine:** Research capture only; no NautilusTrader or Qlib live execution adapter exists.
- **Unspecified Timestamp Cutoff:** Exact session boundary (e.g., UTC 00:00 vs. UTC 16:00) is omitted by the source (`data gap`).
- **Absence of Open-Source Code:** The authors have not published a public repository or replication script, preventing immediate byte-level verification (`data gap`).
- **Linear vs. Nonlinear Duality:** Level alignment resolves almost all cross-loss variation for linear models (HAR, HAR-X), but leaves 44% unresolved for LightGBM. This means tree-based models require loss-function-specific hyperparameter tuning that cannot be bypassed by simple post-hoc scaling.

## Implementation status

- `not-implemented`
- This record represents an upstream research capture of econometric and risk-overlay findings. No backtest script, live execution driver, or risk module has been deployed in Nautilus, Qlib, or live environments.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- Capturing this research does not constitute approval for live crypto allocation, automated capital sizing, or production risk management.

## Related Wiki records

- `[[quant/volrouter-state-conditioned-estimator-controller-routing-volatility-control-2026-09-25]]` — State-conditioned routing overlay over volatility estimators and exposure controllers.
- `[[quant/fear-moves-markets-sentiment-augmented-pomp-bitcoin-latent-volatility-fgi-2026-09-25]]` — POMP latent-volatility filter for Bitcoin with Fear-and-Greed sentiment regressors.
- `[[quant/asymmetric-long-memory-garch-sign-dependent-kernel-injection-2026-09-17]]` — Asymmetric volatility modeling in cryptocurrency markets.
- `[[quant/csi300-regime-augmented-harq-xgboost-low-vol-gated-2026-09-05]]` — Regime-augmented HARQ and XGBoost volatility forecasting.

## Sources

1. Andrzej Tokajuk and Jarosław A. Chudziak, *"Loss Choice or Model Choice? The Role of Forecast Level in Cryptocurrency Volatility Forecasting"*, arXiv preprint `arXiv:2609.27024v1 [q-fin.CP]`, submitted 22 September 2026 20:08:43 UTC, 12 pages.
   - Abstract: https://arxiv.org/abs/2609.27024
   - Pinned HTML full text: https://arxiv.org/html/2609.27024v1 (113,140 bytes, SHA-256 `65cdb911b0c30c5d1b4d11672cd2d8d52c3f1b57003493abae4b3cab196e7c79`)
   - Pinned PDF: https://arxiv.org/pdf/2609.27024v1 (368,410 bytes, SHA-256 `02e04ffa9761918a377b1f76e55e1f9cb58ae4d19b0d018440799da603b7b8a8`)
   - DOI: https://doi.org/10.48550/arXiv.2609.27024
2. Binance Spot Data: Daily OHLCV data for BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, ADAUSDT from 5 October 2017 to 31 May 2026.
