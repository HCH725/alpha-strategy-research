---
schema: strategy-research-record-v1
title: "Gate.io TradFi Stock Perpetual Matrix Statistical Arbitrage: Low-Rank SVD Null-Space Mean Reversion with Q-Score / F-Shock Disambiguation"
created: 2026-09-15
updated: 2026-09-15
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - stat-arb
  - matrix-stat-arb
  - null-space
  - svd
  - multivariate-mean-reversion
  - tradfi-perpetual
  - gate-io
  - stock-perpetual
  - crypto-portability
status: research-only
confidence: medium
source_as_of: 2026-07-29
sources:
  - "FMZ strategy page and full source: 'TradFi 矩陣統計套利 v1.0' (TradFi Matrix Statistical Arbitrage v1.0), created 2026-07-29, last modified ~2026-08. https://www.fmz.com/strategy/546626"
  - "Author FMZ user page (ianzeng123): https://www.fmz.com/user/5b5af9ca45caa814184d2e80e1b1cf66"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Gate.io TradFi Stock Perpetual Matrix Statistical Arbitrage: Low-Rank SVD Null-Space Mean Reversion with Q-Score / F-Shock Disambiguation

## Provenance

- **Source URL**: https://www.fmz.com/strategy/546626
- **Title (source)**: TradFi 矩陣統計套利 v1.0 (monitoring + paper simulator)
- **Author**: FMZ community user `ianzeng123` (https://www.fmz.com/user/5b5af9ca45caa814184d2e80e1b1cf66)
- **Platform**: FMZ Quant (發明者量化)
- **Created / as-of**: strategy page created 2026-07-29; description last modified approximately one month before capture (2026-09-15). Capture date 2026-09-15.
- **Source type**: public FMZ strategy page with full Python source visible without login (login required only for platform backtest/copy).
- **Not a peer-reviewed paper**. No arXiv/SSRN identity. No immutable Git commit SHA is available for this FMZ artifact; stable identity is the FMZ strategy URL + page as-of date.
- **Related FMZ family (same author, not this record)**: EWY three-leg pairs (`ewy-samsung-sk-hynix-three-leg-pairs-stat-arb-stock-perpetual-2026-09-12.md`) is a *pair/three-leg* residual trade on Korean names. This record is a *matrix* null-space construction over a multi-name TradFi perpetual basket — mechanism and signal construction are materially different.

## Economic mechanism

### Source-reported

The source claims that a set of TradFi equity/index perpetual contracts (Gate.io `contract_type=stocks`, optionally `indices`) can be treated as driven by a small number of common factors. Stacking log prices into a time × asset matrix \(X\) and taking an SVD, the leading right singular vectors span the common-factor space; the trailing \(N-k\) right singular vectors span an approximate null space in which portfolio weights \(w\) yield approximately stationary \(Xw\). A single basket therefore supplies \(r = N-k\) orthogonal mean-reversion directions — "matrix statistical arbitrage" rather than pairwise cointegration.

Stability of that null space is claimed to be governed by the Davis–Kahan / Wedin \(\sin\Theta\) bound: subspace rotation under perturbation \(E\) satisfies \(\|\sin\Theta\| \le \|E\| / (\sigma_k - \sigma_{k+1})\). The source uses singular-value gap \(\sigma_k/\sigma_{k+1}\) and rolling principal angles as hard admission gates for tradable baskets.

### Scout interpretation

The reconstructable economic story is a *temporary structural mispricing* within a factor-driven basket: when the residual (null-space) projection of current log prices is extreme relative to the training-window residual covariance, but the *common-factor* scores have not jumped, the source treats the move as "structural misalignment" rather than "new information being priced," and bets on residual mean reversion. If factor scores also jump (F-shock), mean reversion is blocked as "catching a knife."

This is a multi-asset generalization of residual/pairs mean reversion, with an explicit gate that separates idiosyncratic mispricing from systematic repricing. The missing economic link (not proven by the source) is whether TradFi stock perpetuals — which cannot be physically delivered — actually enforce residual convergence through funding, inventory, and quoting habits rather than delivery arbitrage. The source itself flags this as the primary structural risk.

## Signal

### Formation / availability

- Formation is **online / continuous**: each poll cycle (default 60 s) refreshes universe (every 6 h), rebuilds baskets (every 12 h), and evaluates current prices against trained null-space models.
- No publication lag. Timezone: exchange UTC timestamps; intraday volatility seasonality is bucketed by UTC hour (`VOL_SLOTS=24`).
- Tradable immediately after a poll that produces an unblocked Q-score alarm; no bar-close-only convention.

### Lookback / training window

- Target training length `TRAIN_BARS = 2400` of 15-minute bars (`BAR_MINUTES=15`), with hard floor `MIN_TRAIN_BARS = 600` and dynamic reduction if history is short.
- Requires \(T/N \ge\) `TN_RATIO=20` for covariance reliability.
- Price matrix built on aligned log closes; bars where ≥98% of names have frozen mark price are dropped (`FREEZE_FRAC=0.98`).
- Warm-up: estimators/training must complete before monitoring is meaningful; source does not expose a separate warm-up trade lock beyond empty basket state.

### Basket construction (pre-signal)

1. **Universe**: Gate.io perpetual swaps with `contract_type=stocks` (default); exclude pre-IPO synthetic contracts; require OI ≥ 100k USDT, long+short users ≥ 40, OI ≥ 35th percentile, cap top 120 by OI. Drop near-duplicates (\(\rho \ge 0.97\)) preferring the lower-volatility (non-leveraged) variant if vol ratio ≥ 1.40.
2. **Clustering**: returns correlation → Ward hierarchical clustering; keep clusters with size in \([6, 14]\); kNN fallback if hierarchical candidates < 12. Max 150 candidates by average correlation.
3. **Admission gates (all four)**:
   - Factor count \(k\) via Marchenko–Pastur upper edge on the correlation matrix of returns.
   - Singular-value gap \(\sigma_k/\sigma_{k+1} \ge 1.30\).
   - Max principal angle between half-sample null spaces ≤ 20°.
   - Null-space residual portfolio: ADF t-stat ≤ −2.86 (5%, constant) on at least one null-space direction, and OU half-life ≤ 200 bars.
4. Keep at most 6 baskets (`MAX_BASKETS`).

### Entry

Trigger when **both**:

1. **Q-score** exceeds `ENTRY_Q_P = 0.995` training quantile: Mahalanobis distance of the current null-space residual vector \(r_t = (x_t - \mu) V_n\) using training residual covariance, then **divided by UTC-hour volatility slot scale** (intraday seasonality normalization).
2. **F-shock** is *below* `FSHOCK_P = 0.99` quantile: Mahalanobis distance of factor-score first differences (systemic move gate). If F-shock is also extreme, entry is blocked.

Additional blocks:

- Jump filter: if single-cycle Q jump > 0.60 × alarm threshold, treat as event gap and cool down 4 h (`JUMP_MULT`, `JUMP_COOL_S`).
- Max concurrent baskets = 3.
- Hedge fidelity: after integer contract rounding, cosine similarity of actual vs target weights must be ≥ 0.97 (`MIN_HEDGE_FID`); otherwise skip the trade.
- Direction and leg identity from **leave-one-out (LOO) attribution**: reconstruct asset \(i\) from the other \(N-1\); z of reconstruction residual vs training std selects the anomalous name and sign. Only LOO |z| ≥ 2.0 (`MIN_LOO_Z`) contribute.

Entry side: long the underperforming / overperforming leg as signed by LOO z, short the complementary basket legs to remain residual-mean-reverting (multi-leg, not single-name directional).

### Exit

Any of (first hit):

1. Q-score falls to `EXIT_Q_P = 0.80` training quantile (primary mean-reversion exit).
2. Holding time exceeds `HOLD_HL_MULT=3.0` × OU half-life.
3. Basket margin PnL ≤ −18% (`STOP_LOSS_PCT`).
4. Model invalid / Q uncomputable (basket removed).
5. Manual `flat:all`.

### Holding period

Expected: tens of 15-min bars up to ~3× half-life (half-life admission cap 200 bars ⇒ max hold ~600 bars ≈ 6.25 days at 15 m). Overlapping baskets allowed up to 3.

### Parameters (source defaults; fixed unless noted)

| Group | Key defaults |
|---|---|
| Universe | `stocks`; skip pre-IPO; MIN_OI_USDT=1e5; MIN_USERS=40; OI_PCTL=35; MAX_UNIVERSE=120; DEDUP_RHO=0.97; DEDUP_VOL_RATIO=1.40 |
| Cluster | MIN/MAX_BASKET=6/14; LINKAGE=ward; MAX_BASKETS=6 |
| Stability | MIN_GAP=1.30; MAX_ANGLE_DEG=20; ADF_CRIT=−2.86; MAX_HALFLIFE=200; TN_RATIO=20 |
| Monitor | ENTRY_Q_P=0.995; EXIT_Q_P=0.80; FSHOCK_P=0.99; MIN_LOO_Z=2.0; VOL_SLOTS=24; JUMP_MULT=0.60; JUMP_COOL_S=4h |
| Trade | LEVERAGE=3; GROSS_PER_TRADE=0.25; MAX_OPEN=3; HOLD_HL_MULT=3; STOP_LOSS_PCT=18; MIN_HEDGE_FID=0.97 |
| Costs | TAKER_FEE default 0.00075 (overridden per-contract from exchange Info); COST_MULT=1.0 |

All values are **source-fixed defaults**, not empirically optimized hyperparameters reported in a paper. Tuning status is unknown.

## Required data

- **Instrument**: Gate.io USDT-margined perpetual swaps on TradFi equity underlyings (`contract_type=stocks`). No physical delivery. Contract size / `CtVal` from exchange `Info`.
- **Universe**: live `GetMarkets()` filtered as above; survivorship handled only by liquidity gates and periodic rebuild (every 12 h), not by point-in-time listing history.
- **Venue**: Gate.io perpetual futures via FMZ adapter. Other venues with TradFi stock perps (Binance, etc.) are not tested in source.
- **Timeframe**: 15-minute OHLCV bars for training; live mark/ticker for monitoring (60 s poll).
- **Fields**: close (log), mark price for live Q, OI (`position_size`), long/short user counts, taker fee rate, funding rate and funding interval, contract multiplier, min qty / amount & price precision.
- **Point-in-time**: training uses only completed bars in the fetch window; live Q uses current mark. Look-ahead risk is limited to concurrent rebuild using the same window that also evaluates Q — rebuild and monitor share recent history (source does not purify this).
- **Timestamp**: exchange UTC; slot seasonality by `hour % 24`.
- **Missing data**: names with coverage < 95% of the aligned reference grid are dropped; only globally frozen bars dropped; thin sessions retained.
- **Funding / fees / spread**: taker fee + slippage multiplier modeled; **funding accrued by the second and does not cancel across long/short legs** (source: deterministic drift on the residual); no explicit bid-ask spread model beyond `COST_MULT`.

## Execution assumptions

### Source-reported

- Default `TRADE_MODE = paper`. Live mode is a placeholder and is **not implemented** in the published source.
- Integer contract rounding with cosine-fidelity gate ≥ 0.97; abandon trade if fidelity fails.
- Per-leg min notional ~3 USDT (`MIN_LEG_USDT`); budget = equity × leverage × 25%.
- Poll 60 s; heartbeat every 10 cycles; no latency model beyond poll cadence.
- Funding paid/accrued continuously on open residual baskets.

### Scout interpretation

Fillability of multi-leg residual baskets on thin TradFi perps is unknown. Partial fills would break the residual and the fidelity gate only checks *intended* integer weights, not *realized* fills. Queue position, maker vs taker, and one-legged failures are not modeled. Treat paper results as non-executable until fill-level evidence exists.

## Evidence

### Source-reported

- The FMZ page presents this as a **monitoring/research tool + paper validator**, not a claimed profitable live strategy. The dashboard's first screen is out-of-sample validation statistics: alert count, closed count, regression rate, median time-to-revert, max adverse excursion.
- Source self-declares the philosophy: "let correctness of conclusion yield to falsifiability of premise"; sample-out regression rate (not in-sample z reversion) is the sole objective validity criterion.
- **No numeric backtest returns, Sharpe, or sample-out regression rates are published** on the strategy page. The dashboard is designed to accumulate those numbers at runtime.
- Author-stated known risks:
  1. Gate.io TradFi perps cannot be physically delivered vs real equities — **no forced convergence mechanism**; only funding, dealer inventory, and quoting habits constrain prices (weaker than true arbitrage).
  2. Funding rates do not net across long/short legs; deterministic residual drift.
  3. Listing history is short; may not cover a full earnings cycle.
- Page metrics as of capture: ~225 hits, 13 copies, created 2026-07-29.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- Structural negative evidence is **stated by the source itself**: absence of delivery/convergence enforcement on TradFi stock perpetuals is the central identification risk.
- No third-party replication, no published failure study, and no long sample-out regression table were found on the FMZ page or in public discussion linked from it.
- Related literature on equity residual/pairs trading is abundant, but no paper was found that specifically validates SVD null-space baskets on *non-deliverable TradFi crypto perpetuals*.

## Falsification

Research-defined operational tests (not source-reported):

1. **Sample-out premise test (primary, source-aligned)**  
   - Data: rolling 15 m bars on the same Gate.io `stocks` universe, ≥ 6 months.  
   - Procedure: freeze training windows as the source does; after each Q alarm, track residual over `TRACK_BARS=192`.  
   - Metric: fraction of alarms that revert to EXIT_Q before max adverse excursion exceeds 3× half-life span.  
   - **Research-defined falsification threshold**: if closed-alarm regression rate < 0.60 after ≥ 20 closed alarms (source dashboard's own "premise in doubt" rule), reject the mean-reversion premise for this venue/universe. Action: mark family rejected; do not retune Q quantiles without a new pre-registration.

2. **F-shock gate necessity**  
   - Compare entry sets with F-shock gate on vs off, same Q threshold.  
   - If removing F-shock does not degrade sample-out regression rate or worsen MAE, the systemic/idiosyncratic disambiguation is not load-bearing — mechanism claim weakens.

3. **Gap / angle placebo**  
   - Admit baskets with gap < 1.30 or angle > 20° (shuffled admission).  
   - If low-stability baskets sample-out revert as well as gated baskets, Davis–Kahan gating is cosmetic.

4. **Funding-drift stress**  
   - Measure residual PnL before vs after funding over holding period.  
   - If median funding drag ≥ 50% of gross residual edge under default fees, economic edge is negative after costs.

5. **Deliverability control**  
   - Run the same matrix pipeline on a *deliverable* or tightly tracked underlier set (e.g., major crypto perps with known index arbitrage, or tokenized equity with redemption) vs TradFi-only perps.  
   - If TradFi-only residual half-lives are systematically longer / MAE larger, non-delivery is material.

6. **Leakage / rebuild audit**  
   - Rebuild baskets only on data strictly before monitor time; compare alarms to concurrent-rebuild design.  
   - Excess alarm quality under concurrent rebuild ⇒ mild look-ahead contamination.

## Crypto portability

**Portability: direct (already a crypto-native instrument) — with structural caveats.**

- The strategy already trades **crypto-margined TradFi equity perpetuals** on Gate.io. There is no equities-broker dependency.
- Spot/perpetual distinction: perpetual only; funding is first-order (does not cancel).
- 24/7 clock: yes, but underlying US equities have sessions; the source adds UTC-hour volatility slots and reference freeze detection is relevant if extended to hybrid baskets.
- Exchange fragmentation: single-venue (Gate.io). Cross-venue TradFi perp basis is unexplored.
- Listing/survivorship: short listing history; OI/user filters only.
- Custody/venue risk: concentrated on Gate.io TradFi product design, mark methodology, and delisting policy.
- On-chain data: not used.
- **Crypto extension (research-proposed, not source-reported)**: the same Q/F-shock null-space construction could be applied to liquid altcoin baskets or sector crypto baskets, where delivery does not exist either but funding/index arb is stronger. That extension is **unproven** and must not be treated as authorized.

Crypto portability is not authorization to trade.

## Limitations

- **No published performance or sample-out statistics** — only a runtime validator design. Evidence class is "hypothesis + open tool," not "validated edge."
- **No physical delivery / weak residual enforcement** on TradFi stock perps (source-stated).
- **Funding does not net** across residual legs; can systematically tax the basket.
- **Single venue**, short history, earnings-cycle coverage unknown.
- **Paper-only**; live path not implemented; multi-leg fill and partial-fill risk unmodeled.
- **Parameter defaults are design choices**, not paper-tuned optima; overfitting risk if operators retune Q quantiles post hoc.
- **Concurrent rebuild vs monitor** may introduce mild look-ahead.
- **FMZ community artifact**: not peer-reviewed; author identity is a platform handle; no immutable commit SHA.
- Incremental value vs existing repo pairs/factor records: multi-asset SVD null-space + Q/F-shock disambiguation + explicit non-delivery risk on TradFi perps is a **new signal family and new venue class**, not a paraphrase of EWY three-leg or generic Kalman pairs.

## Implementation status

- **Published source**: monitoring + paper simulator only (`TRADE_MODE` default `paper`; live is a placeholder).
- **Not implemented** in any production trading system reviewed here.
- **Not authorized** for Paper/Testnet/Live in the nautilus-quant-system pipeline. This record does not modify NautilusTrader, does not create a strategy family, and does not authorize execution.

## Adoption boundary

`status = research-only`. `adoption = not-approved`. `approval_scope = research-only`.

Presence of this record means only that a public FMZ research strategy was normalized with reconstructable signal, data, execution assumptions, and falsification tests. It is not strategy adoption, implementation authorization, or permission to run Paper/Testnet/Live. Any later adoption decision must be explicit, separately reviewed, and based on this record plus current/live sources (including sample-out regression evidence accumulated under the primary falsification test).

## Related Wiki / repo records

- `ewy-samsung-sk-hynix-three-leg-pairs-stat-arb-stock-perpetual-2026-09-12.md` — same TradFi-perp venue class and same FMZ author neighborhood, but pairwise/three-leg residual on Korean names; different mechanism (regression residual vs SVD null space).
- `crypto-perpetual-pairs-trading-kalman-cointegration-falsification-2026-09-11.md` — Kalman/cointegration pairs family; this record is multi-factor null-space, not pair OU on raw prices.
- Generic equity/ETF matrix and low-rank records in-repo (e.g. Nystrom cross-sectional) are machine-learning cross-sectional predictors, not tradable null-space residual baskets on perpetuals.

No Wiki Brain write was performed (scout boundary).

## Sources

1. FMZ strategy page + source: https://www.fmz.com/strategy/546626 (TradFi 矩陣統計套利 v1.0; created 2026-07-29; captured 2026-09-15).
2. Author page: https://www.fmz.com/user/5b5af9ca45caa814184d2e80e1b1cf66

Conceptual anchors named by the source (not independently verified here): Stock–Watson common-trends representation; Davis–Kahan / Wedin \(\sin\Theta\) theorem; Marchenko–Pastur noise eigenvalue bound; MSPC T²/Q contribution plots; Avellaneda–Stoikov inventory skew; OU half-life mean-reversion diagnostics.
