---
schema: strategy-research-record-v1
title: "FMZ Multi-Asset Risk Parity on Crypto-Venue Perpetuals (BTC/XAU/SPY/CL, EWMA ERC + Vol Target)"
created: 2026-09-19
updated: 2026-09-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - risk-parity
  - portfolio-construction
  - ewma
  - equal-risk-contribution
  - volatility-target
  - fmz
  - multi-asset
status: research-only
confidence: low
source_as_of: 2026-04-07
sources:
  - "FMZ strategy page: 'RWA大类资产风险平价策略' (Multi-Asset Risk Parity; 'RWA' here means major asset classes, not Real-World-Asset tokens), strategy id 535843, author ianzeng123, created 2026-04-07. https://www.fmz.com/strategy/535843"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FMZ Multi-Asset Risk Parity on Crypto-Venue Perpetuals (BTC/XAU/SPY/CL, EWMA ERC + Vol Target)

## Provenance

- **Source URL**: https://www.fmz.com/strategy/535843
- **Source type**: Public FMZ strategy page (Common strategy). Full JavaScript source is login-gated; this capture uses only the publicly visible rationale, formulas, parameters, and architecture notes.
- **Author on page**: ianzeng123
- **Platform**: FMZ / 发明者量化
- **Title note**: Page title 「RWA大类资产风险平价策略」 uses **RWA = 大类资产 (major asset classes)** in the Chinese financial sense. It is **not** a Real-World-Asset tokenization strategy. Do not conflate with RWA-token records.
- **Created (source-reported)**: 2026-04-07 14:28:16
- **Source reviewed as of**: 2026-09-19
- **Deduplication audit (2026-09-19)**: Repository-wide search found **zero** prior records citing FMZ id `535843` or this exact BTC/XAU/SPY/CL EWMA-ERC + vol-target construction on FMZ. Adjacent records are related families, not duplicates:
  - Academic EVaR / tempered-stable risk-parity papers (`entropic-value-at-risk-parity-tempered-stable-returns-2026-09-11.md`, EVaR-deviation records) — different risk measure and source identity.
  - HRP / Black-Litterman regime records (`forecast-vol-targeting-student-t-hmm-hrp-regime-momentum-tilt-2026-09-13.md`) — hierarchical risk parity + factor tilts; different backbone and sources.
  - Cross-sectional meme momentum risk-parity **within-leg** sizing — portfolio construction detail of a different alpha thesis.
  - FMZ 548843 APFF — factor-lifecycle long/short on crypto perps; not multi-asset ERC risk parity.
  - RWA-token / on-chain RWA records — different instrument class.
  - Concurrent TV / SSRN VoV records on origin/main as of this write — different sources and mechanisms.

## Economic mechanism

### Source-reported

Source-reported positioning: multi-asset quantitative portfolio system based on **risk parity**, on FMZ, supporting live and paper modes; aimed at **risk-balanced diversification** rather than return maximization; medium-to-long-term allocation.

Source-reported asset pool (perpetual-style symbols on the platform):

| Label | Contract | Class |
|-------|----------|--------|
| BTC | `BTC_USDT.swap` | Crypto |
| XAU | `XAU_USDT.swap` | Precious metal (gold) |
| SPY | `SPY_USDT.swap` | Equity index |
| OIL | `CL_USDT.swap` | Commodity (oil) |

Source-reported core logic:

1. **Risk-parity weights:** equalize each asset’s marginal risk contribution  
   \(RC_i = w_i \cdot (\Sigma w)_i / \sigma_p = \sigma_p / N\). Numerical iteration, max **2000** steps, convergence tolerance **< 1e-12**. High-vol assets get lower weights; low-vol higher.
2. **EWMA covariance:** \(\hat\sigma_{ij}\) with decay **λ = 0.94** (RiskMetrics-style), **15-minute** log returns, default lookback **60** bars; mild regularization for numerical stability.
3. **Long/short direction:** compute covariance of each asset with an **equal-volatility reference portfolio**:  
   \(\mathrm{CovWithPortfolio}_i = \sum_j w_j^{\mathrm{eqvol}} \Sigma_{ij}\). Negative → **short**; positive → **long**. Single-asset short weight cap **0.5**.
4. **Leverage adaptation:**  
   \(\mathrm{Leverage} = \min(\sigma_{\mathrm{target}} / (\sigma_{\mathrm{portfolio}} \cdot \sqrt{8760}),\ \mathrm{MaxLeverage})\). Default target annual vol **15%**, max leverage **3×**.
5. **Rebalance triggers:** first run; timer (default **24h**); weight drift **>15%** relative; any direction flip; manual.
6. **Risk controls:** emergency cut if single-asset adverse price move **>5%** → reduce that position **50%**; vol-adaptive poll interval (ann. vol >50% → 15 min; 30–50% → 30 min; <30% → 60 min); use **95%** equity (5% cash buffer); min rebalance **5 USDT**.
7. **Default mode:** `TRADE_MODE = paper` (simulation); live optional per source.

Source-reported validation status: public page documents architecture and v2.5 code-fix notes; **no** long-horizon performance series, Sharpe, or live track record is published on the public page. Author comment (community Q&A) only addresses venue symbol mapping (OKX), not PnL.

### Research interpretation

This is **risk-budget portfolio construction**, not a predictive alpha signal. The hypothesized economic effect is **risk-balanced exposure** across weakly related asset classes on a **crypto exchange’s perpetual instrument set**, with optional leverage to hit a volatility target and covariance-sign long/short tilts.

Research interpretation (falsifiable claims, not source-proven profit):

1. **Equal risk contribution:** If cross-asset correlations remain imperfect, ERC can reduce concentration of portfolio risk versus equal-capital allocation — a risk effect, not guaranteed return alpha.
2. **EWMA responsiveness:** λ=0.94 on 15m bars (~60 bars lookback) emphasizes recent covariances; weights may turn over faster than monthly sample-cov parity.
3. **Covariance-sign direction:** Using sign of Cov(asset, eqvol portfolio) as long/short is a **relative-to-portfolio tilt**, not a standalone forecast; in stress, correlations often rise and shorts may fail as diversifiers.
4. **Venue packaging:** Trading SPY/XAU/CL/BTC as USDT perps on one venue adds funding, tracking, and session effects absent from textbook multi-asset risk parity on cash markets.

Per operating rules, **risk management ≠ alpha**: this record documents a reconstructable allocation rule and its data/execution assumptions. It does **not** claim ERC produces positive expected return after costs.

Component roles (normalized):

```text
Universe: BTC, XAU, SPY, CL USDT perpetuals (source default pool)
Covariance: EWMA λ=0.94 on 15m log returns, lookback 60 bars (+ mild regularization)
Allocation: numeric ERC equal risk contribution; tol < 1e-12; max 2000 iters
Direction: long/short by sign Cov(asset, equal-vol reference portfolio); short cap 0.5
Leverage: vol-target 15% ann., max 3×; √8760 annualization (24/7 crypto-hour convention)
Rebalance: 24h | drift 15% | direction flip | manual
Risk: 5% adverse move → cut 50% of that position; 95% equity use; vol-adaptive polling
Mode: paper default; live optional (source)
```

## Signal

Not a directional entry/exit alpha in the predictive sense. Reconstructable **allocation** rule:

### Formation timestamp

Research interpretation: weights formed when the main loop runs (poll interval 15/30/60 min by realized vol; rebalance decisions per triggers above). Exact timezone not published; FMZ bar stamps typically exchange/UTC — **underspecified** on the public page.

### Lookback

- Source-reported: **60** bars of **15-minute** log returns for EWMA covariance (≈15 hours of bars at default settings).
- Endpoints inclusive/exclusive not specified (`underspecified`).

### Long entry / Short entry

- **Long:** asset \(i\) if \(\mathrm{CovWithPortfolio}_i > 0\) under ERC/equal-vol reference construction.
- **Short:** if \(\mathrm{CovWithPortfolio}_i < 0\), subject to short weight cap **0.5**.
- Notional follows ERC weights × leverage × **95%** equity, subject to min rebalance **5 USDT**.
- Exact fill model (market vs limit) not published (`underspecified`).

### Exit / Rebalance

- Portfolio rebalance on timer/drift/direction-flip/manual; emergency **50%** cut on **5%** adverse single-asset move; optional close-all via console (source-reported UI).
- No per-asset profit target or stop beyond the emergency rule in the public description.

### Holding period

Continuous multi-asset book; expected hold until next rebalance or emergency cut — not a fixed trade horizon.

### Parameters (source-reported public defaults)

| Parameter | Default |
|-----------|---------|
| TRADE_MODE | paper |
| INIT_CAPITAL | 10,000 USDT (paper) |
| LOOKBACK | 60 bars |
| EWMA_LAMBDA | 0.94 |
| Bar interval | 15 minutes (log returns) |
| TARGET_VOL | 15% annualized |
| MAX_LEVERAGE | 3× |
| REBALANCE_HOURS | 24 |
| DRIFT_THRESHOLD | 15% |
| POSITION_RATIO | 95% |
| MIN_REBAL_USDT | 5 |
| Short weight cap | 0.5 |
| Emergency adverse move | 5% → cut 50% |
| ERC max iter / tol | 2000 / 1e-12 |
| Annualization | √8760 |

**Underspecified:** exact ERC numerical solver beyond iteration count/tol; regularization magnitude; funding treatment; fee/slippage; symbol mapping across venues; whether `CL_USDT.swap` tracks WTI continuously.

### Position sizing

ERC weights → vol-target leverage → 95% equity; short cap 0.5. Not return-forecast sizing.

### Multi-timeframe dependencies

Covariance on 15m bars; rebalance calendar 24h; poll 15–60m.

### Specification completeness

**Mostly specified for allocation math and defaults**; execution/fill/cost/funding details incomplete. Do not treat as a complete live blueprint.

## Required data

- **Instrument:** four USDT-margined perpetual contracts as listed above (or venue equivalents per author comment).
- **Venue:** FMZ-connected exchange(s); source page implies a unified perp book (e.g. Binance-style TradFi+crypto perps). Exact venue not hardcoded on the public text beyond contract codes.
- **Market type:** perpetual futures/swaps (crypto venue), including TradFi-underlying perps for SPY/XAU/CL.
- **Timeframe:** 15-minute bars for covariance; intraday poll for risk.
- **Fields:** mid/last prices for returns and adverse-move checks; full return history for EWMA Σ; equity/cash; positions.
- **Point-in-time:** causal bars only (research expectation); source does not document PIT audit.
- **Funding/fees:** **not** detailed on the public page; multi-asset perp books have funding that textbook risk parity ignores (`data gap` / research-proposed caution).

## Execution assumptions

Source-reported: paper default; live mode switch; rebalance engine; emergency cut; UI controls (rebalance now, close all).

Not established: maker/taker fees, slippage, latency, partial fills, funding PnL, capacity, tracking error of TradFi underlyings outside cash-session hours.

## Evidence

### Source-reported

- Public documentation of ERC formula, EWMA λ=0.94, lookback 60×15m, vol target 15%, max lev 3, rebalance/drift/emergency parameters, asset pool, paper default.
- **No** source-reported Sharpe, CAGR, drawdown, or live track record on the public page as of 2026-09-19.
- Community comment: author advises mapping analogous contracts on other venues (e.g. OKX) — operational note, not performance.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- Source provides **no** performance evidence; absence is not proof of loss.
- Academic in-repo caution: variance-based risk parity treats upside/downside symmetrically and can fail under correlation spikes (EVaR literature in repo) — adjacent theoretical critique, not a replication of FMZ 535843.
- Structural risks (research interpretation): funding drag on perps; session gaps on TradFi underlyings vs 24/7 crypto; short-leg liquidation if vol-target leverage rises into a correlated selloff; 5% emergency cut may lag gap risk.
- Spec rule: allocation/risk controls are not themselves validated alpha.

## Falsification plan

Research-proposed (not executed; not authorized):

1. **Risk-contribution balance check (research-defined falsification threshold):** After ≥50 rebalances on point-in-time data, if max–min |RC_i − σ_p/N| / (σ_p/N) remains **> 25%** median absolute deviation, the public ERC solver/implementation does not equalize risk as claimed in production settings.
2. **ERC vs equal-capital control:** Same universe/costs; if ERC does not reduce portfolio vol or tail risk vs equal-capital, the risk-parity claim is non-load-bearing for this sample.
3. **Funding-adjusted book:** Include historical funding; if net-of-funding vol-target error or return path degrades materially vs no-funding backtest, mark funding as first-order.
4. **Correlation-stress window:** Test pre-declared crisis subperiods; if shorts and longs become jointly adverse and emergency rules dominate PnL, document regime dependence.
5. **λ / lookback grid:** Pre-declare λ ∈ {0.90, 0.94, 0.97} × lookback ∈ {30, 60, 120} on train, evaluate holdout; if only one cell works, flag overfit.
6. **Venue portability:** Map symbols per author guidance; if ERC weights change materially under different CL/XAU roll specs, venue packaging is load-bearing.
7. **Action on failure:** Keep `research-only`; do not treat paper-mode dashboards as validation.

## Crypto portability

**Portability: `direct` for venue packaging (crypto perps), `unproven` for net risk-adjusted outcomes.**

- Instruments already sit on a crypto exchange perpetual stack (BTC + TradFi-underlying perps).
- Risks: funding, mark/index, 24/7 vs equity session for SPY, commodity roll/contract mapping for CL, stablecoin USDT depeg, leverage liquidation vs 3× cap, venue listing risk.
- Not portable as “RWA token” exposure; not a prediction-market or DeFi LP strategy.
- Crypto portability is not authorization to trade.

## Limitations

- **No source performance series**; research-only allocation capture.
- **underspecified:** fees, funding, fills, regularization, solver details.
- **not independently reproduced**
- **Risk management ≠ alpha** — ERC/vol-target may improve risk shape without positive expected return.
- Full source login-gated; public formulas used only.
- Title “RWA” may mislead intake (major asset classes, not tokenized RWA).

## Implementation status

No implementation in our research stack. Does not modify NautilusTrader/PyBroker; does not authorize Paper/Testnet/Live.

`implementation_status: not-implemented`

Source-side: page documents paper/live switch and UI; **not** treated as our validation or as a verified live track record.

## Adoption boundary

Research-only. Presence here does **not** mean profitable, validated, or approved for implementation, paper, testnet, or live trading.

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

## Related Wiki records

No stable Hermes Wiki Brain path known for this FMZ capture at write time. Do not fabricate Wiki links.

In-repo related: EVaR risk-parity papers; HRP/BL vol-target records; APFF FMZ 548843; crypto cross-sectional equal-vol mixes.

## Sources

1. FMZ Quant strategy page. 「RWA大类资产风险平价策略」 / Multi-Asset Risk Parity. Author ianzeng123. Strategy id 535843. Created 2026-04-07. https://www.fmz.com/strategy/535843 (public description, formulas, parameters reviewed 2026-09-19; full source not accessed).
