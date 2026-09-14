---
schema: strategy-research-record-v1
title: "Commodity Seasonal Trading Null: DVR/SSA/RLSSA Fail to Beat Equal-Weight Long After Costs"
created: 2026-09-14
updated: 2026-09-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - commodities
  - seasonality
  - singular-spectrum-analysis
  - dummy-variable-regression
  - falsification
  - negative-evidence
  - transaction-costs
status: research-only
confidence: medium
source_as_of: 2026-09-10
sources:
  - "Ralph Kosch and Robin Forsberg, 'Seasonal Trading in Commodity Futures: Evidence from Regression and Singular Spectrum Signals', arXiv:2609.12227v1 [q-fin.PM, q-fin.ST], September 10, 2026. https://arxiv.org/abs/2609.12227"
  - "https://github.com/RPKosch/Seasonal-Trading-in-Commodity-Markets-Preprint-Version (HEAD ca66dc66bfb1abf05cd6a993cccab899a67d3bb4 at capture)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Commodity Seasonal Trading Null: DVR/SSA/RLSSA Fail to Beat Equal-Weight Long After Costs

## Provenance

- **Source**: arXiv:2609.12227v1 [q-fin.PM, q-fin.ST]
- **Authors**: Ralph Kosch (University of Zurich), Robin Forsberg (University of Zurich / University of Helsinki)
- **Version**: v1, submitted September 10, 2026
- **DOI**: https://doi.org/10.48550/arXiv.2609.12227
- **URL**: https://arxiv.org/abs/2609.12227
- **Full text HTML**: https://arxiv.org/html/2609.12227v1
- **Code repository**: https://github.com/RPKosch/Seasonal-Trading-in-Commodity-Markets-Preprint-Version
- **Repository commit SHA at capture**: `ca66dc66bfb1abf05cd6a993cccab899a67d3bb4`
- **Sample**: 15 liquid commodity futures; monthly delivery-avoidance returns; model estimation from January 2006; out-of-sample evaluation January 2016–December 2024
- **Universe (tickers)**: CC, CF, CO, CP, CT, GD, HE, HO, LE, NG, SU, SV, ZC, ZS, ZW
- **Raw histories attributed by source to**: TradingCharts (https://futures.tradingcharts.com/), accessed 2025-09-09

### Repository Deduplication Audit

Repository-wide search on 2026-09-14 found zero prior records citing `arXiv:2609.12227`, Kosch, Forsberg, RLSSA, or this unified DVR/SSA/RLSSA seasonal-trading comparison. Adjacent commodity seasonal records are materially different constructions:

- `crude-oil-crack-spread-seasonally-adjusted-mean-reversion-stop-lockout-2026-09-12.md` — 3:2:1 crack-spread cointegration with expanding harmonic deseasonalization
- `commodity-soybean-crush-spread-cointegration-stat-arb-2026-09-12.md` — crush-spread cointegration with monthly seasonal dummies
- `coffee-commodity-weather-stress-lagged-overlay-2026-09-12.md` — satellite weather-stress overlay on coffee
- `cwt-wavelet-bandpass-mean-reversion-hmm-stress-overlay-2026-09-12.md` — CWT band-pass reconstruction + HMM stress overlay on WTI
- `crypto-cross-sectional-same-weekday-seasonality-20w-daily-2026-08-31.md` — crypto weekday seasonality, different asset class and signal

None implement a side-by-side OOS comparison of dummy-variable regression, classical SSA, and robust L1 SSA under one rolling monthly trading design with delivery-avoidance contracts, transaction costs, an equal-weight long benchmark, and Maximum Entropy Bootstrap path assessment.

## Economic mechanism

### Source-reported

Commodity returns may embed calendar structure from harvest cycles, planting decisions, storage dynamics, weather shocks, extraction schedules, transport bottlenecks, and seasonal demand. The paper tests whether recurring structure survives as implementable out-of-sample trading profit after costs relative to a transparent equal-weight long benchmark.

Three model families are compared under identical rolling windows:

1. **Dummy-variable regression (DVR)**: calendar-month dummy `D_m`; long if `β̂_i,m > 0` and Newey–West `p ≤ 0.10`; short if `β̂_i,m < 0` and `p ≤ 0.10`. The 10% threshold is an explicit trading screen, not a cross-sectional discovery test.
2. **Singular Spectrum Analysis (SSA)**: Hankel embedding `L=36`, retain rank `r=12`, diagonal averaging, recurrent one-step forecast.
3. **Robust low-rank SSA (RLSSA)**: Hawkins alternating L1 SVD (AL1) for the first 12 sequentially deflated components, then re-Hankelise and ordinary SVD for the same recurrent forecast; same `N=120`, `L=36`, `r=12` as classical SSA.

A volatility-normalised specification standardizes returns by an in-window EWMA (`λ=0.97`) before estimation. Liquidity is screened before OOS using minimum monthly average daily volume ≥ 1,000 contracts over 2006–2015.

### Research interpretation

The source's headline is a **negative result**: under a unified implementable design, seasonal model portfolios do not robustly beat a simple equal-weight long commodity benchmark. Classical SSA looks strongest on average means but has negative median cumulative returns and deep drawdowns — a path-sensitivity signature, not a durable edge. Volatility normalisation helps DVR shorts on average but weakens SSA portfolios. The economic interpretation for research capture is: calendar/spectral seasonality that is statistically visible in-sample is not automatically a cost-surviving OOS strategy family. That is material negative evidence against treating commodity seasonal signals as default alpha without benchmark-relative, cost-adjusted, path-aware evaluation.

Crypto portability of the **harvest/storage mechanism** is not applicable; the **evaluation discipline** (unified OOS design, pre-OOS liquidity freeze, costs, equal-weight long benchmark, MEB path assessment) is portable as a research template.

## Signal

### Formation timestamp

For each commodity `i` and evaluation month `t`, the signal is estimated only on the preceding 120 monthly log returns (January `t-120` through December `t-1`). The first OOS signal is for January 2016 using January 2006–December 2015. Signals for month `t+1` never use that month's realised return (`source-reported`).

### Lookback

- **Estimation window**: fixed 120 months (10 years), rolled forward one month at a time (`source-reported`)
- **SSA/RLSSA embedding**: `L=36` months (~3 annual cycles); retained rank `r=12` fixed across all contracts and windows (`source-reported`)
- **DVR inference**: Newey–West HAC, Bartlett kernel, lag `max{1, floor(0.75 T^{1/3})}` → 3 lags when `T=120` (`source-reported`)

### Entry (source-reported portfolio formation)

- Monthly rebalance on delivery-avoidance contracts (expire at least two calendar months after observation month; price coverage through at least 14 days after month-end; nearest eligible expiry).
- Long side: rank eligible contracts by positive seasonal forecast / positive DVR `β̂`; short side: negative forecast / negative `β̂`.
- DVR: only contracts with `p ≤ 0.10` are eligible; if none eligible on a side, that portfolio holds cash and earns zero before and after costs.
- Raw forecasts are scaled comparably across contracts; volatility-normalised specification estimates on standardized returns.

### Entry (research-proposed operationalization for future crypto-seasonality tests)

`research-proposed`: apply the same pre-OOS liquidity freeze, 120-month rolling signal, and equal-weight long benchmark discipline if any crypto calendar/spectral seasonal family is proposed. Do not treat in-sample seasonal detection as alpha without OOS cost-adjusted benchmark comparison. This is a methodology transfer, not a crypto signal from this paper.

### Exit

Monthly repositioning implied by the design; positions are reset each month according to the new seasonal ranking/eligibility. No stop-loss or take-profit rules are specified (`source-reported` design implication).

### Holding period

One calendar month per rebalance; overlapping estimation windows but non-overlapping monthly strategy returns in the evaluation (`source-reported`).

### Parameters

- Estimation window `N=120` months (`source-reported`, fixed design)
- SSA/RLSSA: `L=36`, `r=12` (`source-reported`, fixed design, not retuned per contract)
- DVR significance screen: two-sided Newey–West `p ≤ 0.10` (`source-reported` trading filter)
- EWMA volatility: `λ=0.97` for monthly data (`source-reported`, RiskMetrics-style)
- Liquidity screen: min monthly ADV ≥ 1,000 contracts over 2006–2015, universe frozen before OOS (`source-reported`)
- AL1 convergence: squared-vector threshold `1e-10`, max 50,000 iterations per component; error if non-convergence (`source-reported`)
- MEB assessment: 500 Maximum Entropy Bootstrap paths (`source-reported`)

## Required data

- **Instrument**: Commodity futures (energy, metals, softs, grains, livestock)
- **Universe**: 15 tickers after pre-OOS liquidity screen; palladium/platinum excluded for early-sample illiquidity
- **Venue**: Futures markets as represented in TradingCharts continuous/contract histories
- **Timeframe**: Monthly simple returns (open-to-close of first/last trading day of month) on delivery-avoidance nearest eligible expiry; log returns for estimation
- **Fields**: Contract expiry, daily open/close coverage, monthly ADV for screen
- **Point-in-time**: Liquidity universe frozen using 2006–2015 only; rolling estimation uses only trailing 120 months; December 2024 fixed study endpoint
- **Timestamp**: Calendar months; delivery-avoidance rule prevents front-month roll artifacts
- **Missing-data**: Not fully specified beyond eligibility rules; contracts without sufficient coverage drop out of the eligible set for that month
- **Funding/fee/spread needs**: Transaction costs are included in the trading evaluation (`source-reported`); exact cost model details are in the paper's portfolio/return aggregation sections

## Execution assumptions

- **Order type / fill model**: Monthly strategy returns after transaction costs; not tick-level execution
- **Latency / participation**: Not modeled at microstructure level
- **Liquidity**: Pre-OOS ADV ≥ 1,000 contracts screen; palladium/platinum excluded
- **What the source assumes**: Implementable monthly rebalance on delivery-avoiding liquid contracts with stated transaction costs
- **What the Scout does not assume**: No claim of institutional capacity, no claim of fillability at marked prices beyond the paper's cost model

## Evidence

### Source-reported

**Benchmark (equal-weight long) across 500 MEB paths**:
- Cumulative return: 16.81%
- Sharpe ratio: 0.191
- Maximum drawdown: −0.414
- Strongest average full-period profile among compared strategies

**Model comparison (abstract / results)**:
- Classical SSA has the strongest average model outcomes
- SSA negative median cumulative returns and deep drawdowns → substantial path sensitivity
- Volatility normalisation reduces average DVR short loss but generally weakens SSA-based portfolios
- RLSSA does not consistently improve on classical SSA under fixed `r=12`
- **None of the 18 approximate paired MEB Sharpe tests rejects after within-family Holm adjustment**
- Strongest gains concentrated in particular subperiods rather than sustained across 2016–2024
- Evidence does **not** establish robust benchmark outperformance
- MEB preserves each contract's temporal rank ordering → assessment is conditional on observed timing, not a timing-randomised seasonal null (`source-reported` limitation)

**Universe / heterogeneity examples (Figure 1 descriptive)**:
- Heating oil total return +105.62% (CAGR 3.05%) vs WTI −18.30% (CAGR −0.84%) over the representative long window
- Natural gas near-complete drawdown (−99.96% total); cocoa +1,448.69% total late-sample surge
- Soybeans +208.55% vs wheat −91.82% — cross-section is not a uniform commodity block

### Independently reproduced

`not independently reproduced`

The paper releases code and derived monthly panels on GitHub (`RPKosch/Seasonal-Trading-in-Commodity-Markets-Preprint-Version`, commit `ca66dc66bfb1abf05cd6a993cccab899a67d3bb4` at capture). Complete 500-run artifacts are available from the authors. This Scout cycle did not re-run the pipeline.

### Negative evidence

This entire record **is** a negative-evidence capture relative to naive commodity seasonal alpha claims:

- After within-family Holm adjustment, no paired MEB Sharpe test rejects against the equal-weight long benchmark.
- DVR shorts lose money on average under both raw and volatility-normalised specifications.
- SSA average means coexist with negative medians and deep drawdowns (path fragility).
- RLSSA does not consistently dominate classical SSA at fixed rank.
- Gains are subperiod-concentrated, not full-window stable.
- Prior literature cited by the source also reports weakening commodity return seasonality in more recent periods (Li et al. 2024) and heterogeneous evidence for specific calendar rules (Degenhardt & Auer 2018).

## Falsification plan

1. **Reproduce the published OOS path** on the released code/panel at commit `ca66dc66bfb1abf05cd6a993cccab899a67d3bb4`. **Research-defined falsification threshold**: if paired MEB Sharpe differences vs equal-weight long reverse sign or become large and Holm-significant in favor of a seasonal model, update this record from null toward candidate.
2. **Timing-randomised seasonal null** (source acknowledges MEB preserves temporal rank ordering). Construct a month-permuted or circularly shifted placebo that breaks calendar alignment while preserving each contract's return distribution. Reject any residual seasonal claim that does not clear this null.
3. **Cost stress**: double the paper's transaction costs; if any seasonal model turns sharply worse while the long benchmark is relatively stable, the family is cost-fragile.
4. **Subperiod split**: evaluate 2016–2019 vs 2020–2024 separately. **Research-defined falsification threshold**: if a model only wins in one macro regime (e.g., COVID/energy-shock years), do not treat it as a structural seasonal alpha.
5. **Rank sensitivity**: re-run SSA/RLSSA with `r ∈ {6, 12, 24}`. If the null depends on the fixed `r=12` choice, report rank fragility rather than a general SSA conclusion.
6. **Contract-roll alternative**: replace delivery-avoidance nearest-eligible with a standard constant-maturity roll. If results flip, the effect is construction-sensitive.
7. **Crypto adaptation test (research-proposed, not from source)**: if any crypto calendar/spectral seasonal family is proposed later, apply the same pre-OOS liquidity freeze, rolling window, costs, and equal-weight long (or equal-weight crypto long) benchmark before calling it alpha.

## Crypto portability

**Not applicable** for the harvest/storage/weather mechanism (no biological crop calendar, no physical storage convenience yield cycle analogous to grains/softs in crypto spot/perps).

**Adapted** for the evaluation methodology:

- Pre-OOS universe freeze prevents look-ahead liquidity selection.
- Rolling 120-window + monthly rebalance is a transferable design.
- Equal-weight long benchmark discipline is transferable (e.g., equal-weight BTC/ETH or broad crypto long).
- MEB/path-sensitivity assessment is transferable when returns are path-dependent.
- Crypto-specific caveats if someone ports "seasonality" naively: 24/7 sessions, no delivery months, funding cycles (8h), halving clocks, and weekday/hour effects already covered by other repository records (`bitcoin-turn-of-15min-candle-seasonality-1m-2026-08-31.md`, `crypto-cross-sectional-same-weekday-seasonality-20w-daily-2026-08-31.md`, `crypto-intraday-utc-return-seasonality-tea-time-2026-09-03.md`) — those are different mechanisms and are not strengthened by this commodity null, except as a general warning that calendar structure ≠ cost-surviving alpha.

Crypto portability is **not** authorization to trade.

## Limitations

- **Null is conditional on observed timing**: MEB preserves temporal rank ordering; the paper does not run a timing-randomised seasonal null.
- **Fixed SSA rank `r=12`**: may understate or overstate robust SSA relative to tuned alternatives.
- **15-contract universe**: broad sectors but not exhaustive; palladium/platinum excluded.
- **Single data provider attribution** (TradingCharts) for raw histories.
- **Monthly horizon only**: intraday or weekly seasonal families are out of scope.
- **Preprint**: arXiv v1; not peer-reviewed at capture time.
- **Transaction-cost model**: included, but exact sensitivity grid should be read from the paper before treating magnitudes as binding.
- **No crypto empirical results** in the source.

## Implementation status

`not-implemented`

No implementation in our research stack. No commodity seasonal DVR/SSA/RLSSA strategy family, no PyBroker/NautilusTrader strategy, and no live/paper/testnet configuration exists for this family. This record is research capture of a negative OOS comparison.

## Adoption boundary

This record is research material only. Presence in this repository does not mean profitable, validated alpha, or approval for implementation, paper trading, testnet, or live trading. The primary research value is negative evidence and evaluation discipline, not an implementable seasonal commodity strategy.

## Related Wiki records

- [[quant/strategy-research-record-spec-v1]] — canonical schema
- `crude-oil-crack-spread-seasonally-adjusted-mean-reversion-stop-lockout-2026-09-12.md` — different mechanism (cointegrated refinery margin with harmonic deseasonalization)
- `commodity-soybean-crush-spread-cointegration-stat-arb-2026-09-12.md` — different mechanism (crush-spread cointegration)
- `coffee-commodity-weather-stress-lagged-overlay-2026-09-12.md` — different mechanism (weather-stress overlay)
- `cwt-wavelet-bandpass-mean-reversion-hmm-stress-overlay-2026-09-12.md` — related decomposition family (CWT) but different signal and HMM stress overlay
- `bitcoin-turn-of-15min-candle-seasonality-1m-2026-08-31.md` — crypto calendar seasonality, different asset/mechanism
- `crypto-cross-sectional-same-weekday-seasonality-20w-daily-2026-08-31.md` — crypto weekday seasonality, different construction

## Sources

1. Ralph Kosch and Robin Forsberg. "Seasonal Trading in Commodity Futures: Evidence from Regression and Singular Spectrum Signals." arXiv:2609.12227v1 [q-fin.PM, q-fin.ST], September 10, 2026. https://arxiv.org/abs/2609.12227
2. Code and derived monthly panels: https://github.com/RPKosch/Seasonal-Trading-in-Commodity-Markets-Preprint-Version (commit `ca66dc66bfb1abf05cd6a993cccab899a67d3bb4` at capture time)
