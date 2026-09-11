---
schema: strategy-research-record-v1
title: Crypto Cross-Sectional Continuation with Frozen Holdout (Three-Implementation Ensemble)
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - continuation
  - momentum
  - walk-forward
  - frozen-validation
status: research-only
confidence: medium
source_as_of: 2026-08-17
sources:
  - "https://github.com/owensimonfive/crypto-alpha-across-horizons (commit 4efb5a288516053dfc588a1d1dbae6d0c5fe674f, 2026-08-17)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Cross-Sectional Continuation with Frozen Holdout (Three-Implementation Ensemble)

## Provenance

Primary source: Owen Simon, **"Crypto Alpha Across Horizons"**, GitHub repository `owensimonfive/crypto-alpha-across-horizons`, latest commit `4efb5a288516053dfc588a1d1dbae6d0c5fe674f` (2026-08-17). Public research project with six curated notebooks, frozen result artifacts, and reproducibility documentation.

- **Repository URL:** https://github.com/owensimonfive/crypto-alpha-across-horizons
- **Full commit SHA (HEAD):** `4efb5a288516053dfc588a1d1dbae6d0c5fe674f`
- **Author:** Owen Simon (GitHub: owensimonfive)
- **Research deck:** PDF at `presentation/crypto_alpha_across_horizons_research_presentation.pdf`
- **Universe:** Point-in-time monthly top-25 liquid Binance spot USDT pairs
- **Data source:** Binance 4h bars (processed into 1h panels for shorter-horizon variants)
- **Development period:** 2020-04-01 to 2022-11-06 (in-sample parameter selection)
- **Evaluation period:** 2023-01-01 to 2024-11-06 (frozen validation)
- **Final holdout:** 2025-01-01 to 2026-08-01 (untouched, exclusive)
- **Publication status:** Public GitHub repository, not peer-reviewed; research presentation PDF included
- **Source-identity deduplication:** Searched entire repository for `owensimonfive`, `crypto-alpha-across-horizons`, `cross-sectional continuation`, `multi-week continuation`, and the exact finalist names (ECON/BAL/SHARP). Zero prior records matched. The existing `crypto-cross-sectional-volatility-managed-momentum-2026-08-31.md` (Ao Yang 2025) uses a different source (academic paper), different mechanism (volatility management overlay), and different sample. The existing `crypto-medium-term-cross-sectional-reversal-lmw-2026-09-11.md` (Kiefer & Nowotny 2026) documents the opposite directional effect (reversal/contrarian at 8-10 week horizons) from a different source. This record is independent.

**Primary-source checksum (verified from repository README, `results/tables/frozen_finalists.csv`, `results/tables/final_holdout_metrics.csv`, and `results/tables/pre2025_reproduction_gate.csv`):**
- (a) Author: Owen Simon — confirmed from GitHub commits.
- (b) Version/date: HEAD commit 2026-08-17, repository created 2026-08-17 — confirmed from GitHub API.
- (c) Sample period: Development 2020-04 to 2022-11; Evaluation 2023-01 to 2024-11; Final holdout 2025-01 to 2026-08 — confirmed from frozen CSVs.
- (d) Universe: Point-in-time monthly top-25 Binance spot USDT pairs — confirmed from README.
- (e) Transaction cost/slippage: Constant 20 bps per unit of turnover (full L1 turnover proportional costs); break-even costs computed for each finalist — confirmed from CSVs and README.
- (f) Core performance numbers (final holdout, from `final_holdout_metrics.csv`):
  - ECON: mean IC 0.0484, gross Sharpe 0.33, net-20 Sharpe 0.10, break-even cost 28.5 bps, 536 observations
  - BAL: mean IC 0.0466, gross Sharpe 0.79, net-20 Sharpe 0.41, break-even cost 42.0 bps, 261 observations
  - SHARP: mean IC 0.0368, gross Sharpe 1.13, net-20 Sharpe 0.42, break-even cost 31.7 bps, 1564 observations
- (g) Publication status: Public GitHub repository, not peer-reviewed — confirmed.

## Economic mechanism

### Source-reported

The repository documents an end-to-end research project testing whether **relative past crypto performance predicts relative future performance across horizons**. The initial cross-sectional momentum signal (standard Jegadeesh-Titman formation/holding) failed its frozen 2023–2024 validation. This failure became the catalyst for a redesign using only pre-2025 information, which uncovered a distinct **multi-week cross-sectional continuation** architecture.

The three finalist implementations represent different tradeoffs between economic resilience, balance, and risk-adjusted performance, but are explicitly described as "different expressions of the same continuation factor rather than independent alphas." The authors hypothesize that the continuation effect reflects information diffusion and trend persistence at multi-week horizons, where relative performance information is gradually incorporated into prices rather than being immediately arbitraged away.

### Research interpretation

The economic hypothesis is **cross-sectional return continuation (momentum) in crypto spot markets at 1–8 week formation horizons with 6–8 week holding periods**. The mechanism is that relative past winners continue to outperform relative past losers over multi-week horizons, driven by:

1. **Gradual information diffusion:** Information about asset quality or demand shocks propagates slowly through the fragmented crypto market, creating predictable continuation.
2. **Behavioral underreaction:** Retail and institutional underreaction to cross-sectional performance signals allows continuation to persist beyond what efficient markets would permit.
3. **Limits to arbitrage:** Short-sale constraints, borrow costs, and execution friction prevent full arbitrage of the continuation effect, allowing it to persist in the cross-section.

**Key design features:**
- Point-in-time universe construction to avoid survivorship bias
- Exact elapsed-price endpoints (not shifted bars)
- Full-L1 turnover and turnover-proportional costs
- No return or price forward-filling across missing exchange timestamps
- Broad-surface / neighboring-parameter interpretation rather than single-cell optimization
- Failed validation preserved in the research record

## Signal

**Three finalist implementations (all frozen before untouched holdout):**

### ECON (Economic resilience)
- **Formation horizon:** 2 weeks
- **Holding horizon:** 6 weeks
- **Decision cadence:** 24 hours
- **Portfolio mapping:** Continuous rank
- **Entry:** Rank assets by cumulative return over trailing 2-week formation window. Long top-ranked (winners), short bottom-ranked (losers) using continuous rank mapping.
- **Exit:** Rotate at 24-hour cadence; positions expire after 6-week holding window.
- **Universe:** Monthly top-25 Binance spot USDT pairs by volume.
- **Rebalance:** Full L1 turnover at each 24h decision point.

### BAL (Balanced)
- **Formation horizon:** 3 days
- **Holding horizon:** 8 weeks (56 days)
- **Decision cadence:** 48 hours
- **Portfolio mapping:** Equal-weight terciles
- **Entry:** Rank assets by cumulative return over trailing 3-day formation window. Long top tercile, short bottom tercile, equal-weighted within each basket.
- **Exit:** Rotate at 48-hour cadence; positions expire after 8-week holding window.
- **Universe:** Monthly top-25 Binance spot USDT pairs by volume.

### SHARP (Higher Sharpe)
- **Formation horizon:** 1 day
- **Holding horizon:** 8 weeks (56 days)
- **Decision cadence:** 8 hours
- **Portfolio mapping:** Equal-weight terciles
- **Entry:** Rank assets by cumulative return over trailing 1-day formation window. Long top tercile, short bottom tercile, equal-weighted within each basket.
- **Exit:** Rotate at 8-hour cadence; positions expire after 8-week holding window.
- **Universe:** Monthly top-25 Binance spot USDT pairs by volume.

**Position sizing:** Dollar-neutral long-short. No volatility targeting or leverage scaling described. Weights are determined by portfolio mapping (continuous rank or equal-weight terciles).

**Parameters:** All formation/holding horizons, cadences, and portfolio mappings were selected during the development period (2020-04 to 2022-11) and frozen before the evaluation and holdout periods. No post-holdout parameter rescue, beta hedge, asset exclusion, or ensemble fitting.

**Underspecified items:**
- Exact portfolio weight computation within continuous rank mapping (ECON) — underspecified in public README; details likely in notebook 04.
- Handling of ties or simultaneous signals — not stated in source.
- Exact rebalancing implementation (market vs limit orders) — not stated.

## Required data

- **Instrument:** Binance spot USDT pairs (e.g., BTCUSDT, ETHUSDT, SOLUSDT, etc.)
- **Universe:** Point-in-time monthly top-25 by trailing volume; universe membership is re-evaluated monthly using only data available at that point.
- **Venue:** Binance spot only.
- **Timeframe:** 4h OHLCV bars (primary); 1h bars used for shorter-horizon variants.
- **Fields:** Open, High, Low, Close, Volume (standard OHLCV).
- **Funding/fee data:** Not used in the signal; flat 20 bps cost model applied post-hoc.
- **Point-in-time:** Universe construction is explicitly point-in-time to avoid survivorship bias.
- **Missing data:** No forward-filling across missing exchange timestamps; incomplete P&L rows are tracked separately (visible in CSVs).
- **Timestamp:** UTC (Binance standard).

## Execution assumptions

- **Order type:** Research assumes market orders at decision-point close prices.
- **Fill model:** Assumed perfect fill at close; no partial fills or failures modeled.
- **Fees:** Constant 20 bps per unit of turnover (full L1 turnover proportional). This is the primary cost assumption; break-even costs are computed for each finalist.
- **Slippage:** Included in the 20 bps flat assumption; not separately modeled.
- **Spread:** Not separately modeled; assumed captured within the 20 bps flat assumption.
- **Impact:** Not separately modeled; the 20 bps flat assumption is a proxy for all execution frictions.
- **Leverage/margin:** Dollar-neutral long-short; no leverage described.
- **Borrow/shorting:** Assumed available at no cost; this is a material assumption for a spot long-short strategy.
- **Latency:** Not modeled; research assumes instantaneous execution at decision-point prices.
- **Signal-to-order timing:** Decision made at end of bar period; execution assumed at same bar close.

**Material gaps:** The 20 bps flat cost model is a simplification. Real execution costs vary across assets, time periods, and market conditions. The source acknowledges this limitation explicitly. Short availability and borrow costs for spot crypto are not modeled.

## Evidence

### Source-reported

**Failed initial validation (2023-2024):** A promising cross-sectional momentum signal failed its frozen 2023–2024 evaluation. The source reports this failure directly and preserves it in the research record. The exact failure metrics for the initial signal are available in `results/tables/` but the key point is that the initial momentum hypothesis did not survive the frozen evaluation period.

**Pre-2025 redesign results (from `pre2025_reproduction_gate.csv`):**

| Finalist | Period | Mean IC | Gross Sharpe | Net-20 Sharpe | Break-even (bps) |
|----------|--------|---------|--------------|---------------|-------------------|
| BAL | Development (2020-04 to 2022-11) | 0.0438 | 1.45 | 1.17 | 102.3 |
| BAL | Evaluation (2023-01 to 2024-11) | 0.0435 | 1.42 | 1.03 | 73.0 |
| ECON | Development (2020-04 to 2022-11) | 0.0349 | 0.79 | 0.59 | 81.0 |
| ECON | Evaluation (2023-01 to 2024-11) | 0.0539 | 0.92 | 0.68 | 79.0 |
| SHARP | Development (2020-04 to 2022-11) | 0.0342 | 2.13 | 1.55 | 73.1 |
| SHARP | Evaluation (2023-01 to 2024-11) | 0.0429 | 1.94 | 1.30 | 60.9 |

All three finalists passed the frozen reproduction gate (pre-2025 period) with near-identical IC, Sharpe, and break-even cost values between frozen and reproduced runs.

**Final holdout results (2025-01-01 to 2026-08-01, from `final_holdout_metrics.csv`):**

| Finalist | Mean IC | IC HAC t-stat | Gross Sharpe | Net-20 Sharpe | Break-even (bps) | Gross MDD | Net-20 MDD | Observations |
|----------|---------|---------------|--------------|---------------|-------------------|-----------|------------|--------------|
| ECON | 0.0484 | 1.21 | 0.33 | 0.10 | 28.5 | -16.9% | -18.5% | 536 |
| BAL | 0.0466 | 2.27 | 0.79 | 0.41 | 42.0 | -11.0% | -12.8% | 261 |
| SHARP | 0.0368 | 2.59 | 1.13 | 0.42 | 31.7 | -14.0% | -16.6% | 1,564 |

All three finalists passed the predeclared survival rule (direction positive, gross economics positive, break-even cost above 20 bps).

**Degradation from evaluation to holdout:** Net-20 Sharpe degraded materially for all three finalists (e.g., BAL from 1.03 to 0.41; SHARP from 1.30 to 0.42). The source acknowledges this: "Realized economic strength was weaker than in the pre-2025 evaluation."

**Additional diagnostics (from README):**
- Typical portfolios held 29–31 active names
- No single asset exceeded ~6.6% of absolute contribution
- Performance was materially stronger in 2025 than Jan–Jul 2026
- Dollar-neutral portfolios exhibited moderate negative realized crypto-market beta in the final holdout
- The three finalists are highly correlated and represent one continuation factor, not three independent alphas

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Initial momentum signal failed frozen 2023-2024 validation.** The source reports this directly and preserves the failed hypothesis in the research record.
2. **Material degradation from evaluation to holdout.** All three finalists showed substantially weaker net-of-cost performance in the 2025-2026 holdout compared to the 2023-2024 evaluation period.
3. **SHARP (highest gross Sharpe) is most turnover-sensitive.** SHARP has the highest annualized turnover (~115x) and its net Sharpe is much lower than its gross Sharpe, indicating high sensitivity to execution costs.
4. **ECON is marginally profitable after costs in the holdout.** ECON's net-20 Sharpe of 0.10 is barely above zero; the continuation effect after realistic costs is thin for this implementation.
5. **Short holdout period.** The untouched holdout covers approximately 19 months (2025-01 to 2026-08), which is a limited out-of-sample window.
6. **Negative market beta.** Dollar-neutral portfolios exhibited moderate negative realized crypto-market beta in the final holdout, suggesting the strategy may partly be a latent short-beta trade.

None identified as contradicting the continuation thesis beyond the above; absence is not evidence of no negative result.

## Falsification plan

1. **Extended holdout monitoring:** Continue tracking the three finalists through future periods (2026-09 onward) without parameter modification. Failure threshold: net-20 Sharpe drops below 0.0 for any 6-month rolling window. Action: flag for review, do not trade.
2. **Ablation: formation horizon:** Test whether the continuation effect is concentrated in specific formation horizons (1d vs 3d vs 2w) by zeroing out each horizon independently. Research-defined threshold: if any horizon's removal increases net Sharpe, that horizon is likely noise.
3. **Ablation: holding horizon:** Test whether 6w vs 8w holding produces materially different results. Research-defined threshold: if holding horizon extension adds < 0.05 IC, the longer horizon is not adding value.
4. **Cost sensitivity stress test:** Increase cost assumption from 20 bps to 30, 40, 50 bps and re-evaluate net Sharpe. Research-defined threshold: if net-20 Sharpe drops below 0.0 at 30 bps for all three finalists, the strategy is not cost-robust.
5. **Universe stability:** Test whether the continuation effect survives expansion beyond top-25 pairs (e.g., top-50 or top-100) or contraction to top-10. Research-defined threshold: if Sharpe drops > 50% when expanding universe, the effect is concentrated in a small set of liquid names.
6. **Regime conditioning:** Test whether the effect is conditional on BTC market regime (bull vs bear). Research-defined threshold: if net Sharpe is negative in any 6-month regime window, the effect is regime-dependent.

## Crypto portability

**Direct** — the strategy is natively designed for and tested on Binance crypto spot markets.

**Crypto-specific considerations:**
- Spot only — no perpetual funding, no basis, no leverage in the base strategy
- 24/7 market structure — decision cadence (8h, 24h, 48h) aligns with continuous trading
- Monthly universe reconstitution — handles delistings and new listings
- Cross-exchange applicability is untested — the strategy uses Binance data only; venue fragmentation may affect execution on other exchanges
- Liquidity assumptions — the top-25 monthly universe filter provides some liquidity floor, but market impact at rebalance is not modeled

## Limitations

- **Constant cost model:** The 20 bps flat assumption does not capture time-varying execution costs, asset-specific spread differences, or market impact at different participation rates.
- **Spot borrow/shorting assumed free:** The long-short portfolio assumes short positions are available at no cost; in practice, spot borrowing may be constrained or costly for some crypto assets.
- **Limited holdout duration:** The 19-month final holdout (2025-01 to 2026-08) is a relatively short out-of-sample window; a longer holdout is needed for high confidence.
- **Degradation from evaluation to holdout:** All three finalists showed materially weaker net performance in the holdout, raising questions about whether the evaluation period overfit the continuation signal.
- **Small universe:** The top-25 monthly universe limits breadth; the strategy may not scale to larger allocations.
- **Single venue:** All data and execution assumptions are Binance-specific; cross-venue robustness is untested.
- **Not independently reproduced:** The results have not been independently verified.
- **Turnover-sensitive:** SHARP and BAL have high annualized turnover (38x and 60x respectively), making them sensitive to execution quality.

## Implementation status

Not implemented. No implementation in our research stack. The source provides a public repository with notebooks and frozen result artifacts; the research logic is frozen and documented for reproducibility.

## Adoption boundary

This record is research material only. It does not indicate:
- profitable strategy
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet trading
- approved for live trading

The research documents both a failed initial hypothesis and a surviving redesign. The surviving effect shows positive but degraded performance in the final holdout. The strategy should be treated as a hypothesis requiring further validation before any implementation decision.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` (schema specification)
- `[[quant/crypto-medium-term-cross-sectional-reversal-lmw-2026-09-11]]` (related cross-sectional crypto research, but documents the opposite directional effect: reversal at 8-10 week horizons vs. continuation at 1-8 week horizons; different source and mechanism)
- `[[quant/crypto-cross-sectional-volatility-managed-momentum-2026-08-31]]` (related cross-sectional crypto momentum research, but different source [Ao Yang 2025], different focus [volatility management overlay], and different sample)

## Sources

1. Owen Simon, "Crypto Alpha Across Horizons", GitHub repository `owensimonfive/crypto-alpha-across-horizons`, commit `4efb5a288516053dfc588a1d1dbae6d0c5fe674f` (2026-08-17). https://github.com/owensimonfive/crypto-alpha-across-horizons
2. Frozen result artifacts: `results/tables/frozen_finalists.csv`, `results/tables/final_holdout_metrics.csv`, `results/tables/pre2025_reproduction_gate.csv` — accessed via raw GitHub content on 2026-09-12.
