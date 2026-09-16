---
schema: strategy-research-record-v1
title: "Kronos Open K-line Foundation Model Multi-Sample Quantile Band Trend Overlay (FMZ 537215)"
created: 2026-09-15
updated: 2026-09-15
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - foundation-model
  - kronos
  - kline-foundation-model
  - quantile-band
  - multi-sample
  - trend-overlay
  - risk-defined-exit
  - fmz
status: research-only
confidence: low
source_as_of: 2026-04-17
sources:
  - "FMZ strategy page and full Python source: 'Kronos AI 预测策略', created 2026-04-17, last modified ~2026-04/05. https://www.fmz.com/strategy/537215"
  - "Kronos foundation-model repository: https://github.com/shiyu-coder/Kronos commit 67b630e67f6a18c9e9be918d9b4337c960db1e9a (2026-04-13). Relevant paths: model Kronos/KronosTokenizer/KronosPredictor; Hugging Face weights NeoQuasar/Kronos-Tokenizer-base and NeoQuasar/Kronos-{ModelSize}."
  - "Author FMZ page (official FMZ account 发明者量化-小小梦): https://www.fmz.com/user/105ed6e51bcc97792c610fdbb7e2a1d6"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Kronos Open K-line Foundation Model Multi-Sample Quantile Band Trend Overlay (FMZ 537215)

## Provenance

- **Source URL**: https://www.fmz.com/strategy/537215
- **Title**: Kronos AI 预测策略
- **Author**: FMZ official/community account `发明者量化-小小梦` (https://www.fmz.com/user/105ed6e51bcc97792c610fdbb7e2a1d6)
- **Created / as-of**: 2026-04-17; capture 2026-09-15. Full Python source visible on the FMZ page.
- **External dependency (GitHub)**: https://github.com/shiyu-coder/Kronos at full commit SHA `67b630e67f6a18c9e9be918d9b4337c960db1e9a` (2026-04-13). Paths of interest: package providing `Kronos`, `KronosTokenizer`, `KronosPredictor`; HF weights `NeoQuasar/Kronos-Tokenizer-base`, `NeoQuasar/Kronos-{ModelSize}`.
- **Source-reported model claim**: Kronos is described as the first open-source financial K-line foundation model, trained on 12B+ K-lines. This is **source-reported** (FMZ page / model authors); not independently verified here.

## Economic mechanism

### Source-reported

The strategy treats Kronos as a probabilistic next-window K-line forecaster. It samples multiple future close paths, extracts endpoint quantiles (P10/P50/P90) and path-direction consistency, and trades a **one-shot trend overlay**: enter when the median endpoint implies enough profit space and sample paths agree on direction; take profit at the predicted median; stop at the opposite quantile band edge (with a minimum stop distance); force-flatten after `PredLen` bars or on a reverse consistent signal.

### Scout interpretation

The operational hypothesis is that an open K-line foundation model's multi-sample predictive distribution contains **short-horizon directional information** beyond naive persistence, and that a mechanical TP/SL/maturity overlay can harvest it without discretionary discretion. This is a **forecast-to-fill overlay**, not a new microstructure mechanism. Missing links: calibration of the predictive intervals, whether endpoint median is a valid TP, and whether path-consistency adds signal beyond the median move. None of these are established by the FMZ page.

## Signal

### Formation / availability

- On each **new closed bar** of `KlinePeriod` (configurable: 1m–1d), after excluding the forming bar (`records[:-1]`).
- Context window: last `Lookback` closed bars (default 400), OHLCV.
- Multi-sample: `SampleCount` independent `predictor.predict(..., sample_count=1)` calls (default 5) with temperature `T` and top-p.
- Predict horizon: `PredLen` bars (default 24).
- Dedup on bar timestamp so prediction does not re-fire within the same closed bar.

### Entry

Let \(c\) be last close; endpoints \(\{e_i\}\) of sampled paths; \(m=\mathrm{median}(e)\); \(p_{10},p_{90}\) percentiles.

- Expected move: \(\mathrm{pct} = (m-c)/c\).
- Consistency: share of paths on the majority side of \(c\).
- **Long** if \(\mathrm{pct} > \mathrm{SignalThreshold}/100\) and consistency \(\ge \mathrm{ConsistencyThreshold}/100\).
- **Short** if \(\mathrm{pct} < -\mathrm{SignalThreshold}/100\) and consistency \(\ge\) threshold (**futures only**; spot is long-only).
- Cooldown: require `bars_since_close >= CooldownBars` after a flatten (default 1).
- Size: risk-parity style — max loss at stop = `RiskPerTrade%` of equity, capped by `MaxPositionPct%` of equity.
- Fill: limit with small marketable offset (±0.2% in source) or paper equivalent.

### Exit

1. **Take profit**: price reaches predicted median target.
2. **Stop**: long stop = min(P10, \(c - \mathrm{MinStopPct}\%\)); short stop = max(P90, \(c + \mathrm{MinStopPct}\%)).
3. **Maturity**: `bars_held >= PredLen` → force close.
4. **Reverse signal**: opposite direction with consistency ≥ threshold.
5. **Halt**: max drawdown or consecutive-loss circuit breakers (no new entries until manual `cmdUnhalt`).

One position at a time; full flatten on any exit.

### Parameters (UI/source defaults; several numeric defaults not printed on the page and must be read from the strategy parameter panel at deploy time)

| Param | Role | Noted default |
|---|---|---|
| ModelSize | Kronos-{small\|...} | small (25M, context 512) listed |
| KlinePeriod | bar interval | e.g. 1m–1d |
| Lookback / PredLen / SampleCount | context / horizon / paths | 400 / 24 / 5 |
| SignalThreshold / ConsistencyThreshold | entry gates | threshold % / 60% |
| RiskPerTrade / MaxPositionPct / MinStopPct | size & stop floor | panel-set |
| MaxDrawdownPct / MaxConsecutiveLoss / CooldownBars | circuit breakers | panel-set / 5 / 1 |
| TradeMode | paper vs live | paper default in copy |

## Required data

- **Instrument**: any FMZ-supported spot or perpetual/futures pair (user `Symbol`).
- **Venue**: FMZ local host + exchange adapter; Kronos inference on local CPU/CUDA/MPS.
- **Fields**: OHLCV bars only for the model; ticker Last for fill/mark; account equity/balance/positions.
- **Timeframe**: closed bars of `KlinePeriod`; no order-book microstructure.
- **Point-in-time**: only completed bars enter the context; look-ahead risk limited to forming-bar exclusion (source does drop `records[:-1]`).
- **Missing data**: insufficient bars → wait; position sync failure → skip close or clear local state (live path).
- **Funding/fees/spread**: not modeled in paper path (0.1% paper haircut on fills in source); live path uses exchange orders without explicit fee model in the script.

## Execution assumptions

### Source-reported

- Paper mode with virtual balance; live mode with exchange marketable limits.
- Futures: long/short; spot: long only.
- Persistent state store (`_G`) for crash recovery; optional reset on start.
- Position reconciliation every 300s in live mode.

### Scout interpretation

- Paper fills at ticker with 0.1% haircut **understate** taker fees + adverse selection on thin alts.
- One-shot full-size risk bets on foundation-model noise can pathologically hit SL before TP; no partial exits.
- Local inference latency (seconds) is acceptable on bar-close but not for HFT.

## Evidence

### Source-reported

- FMZ page presents design, full source, and deployment notes; **no published backtest table, hit rate, or calibration metrics** on the page.
- Model card / Kronos repo (external) may report forecasting benchmarks; those are **model** claims, not live trading PnL for this overlay.
- Page metrics as of capture: ~821 hits, 42 copies.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- None identified on the FMZ page; absence is not evidence of no negative result.
- Research-proposed risk: foundation-model price path samples can be miscalibrated in tails; TP at median systematically truncates winners while SL at band edge can be hit first — a structural **negative skew** candidate that must be measured.

## Falsification

Research-defined tests (not source-reported):

1. **Walk-forward net-of-cost edge**  
   - Same lookback/predlen/sample settings on a crypto pair; paper vs taker fees 5–10 bps + 5 bps slippage.  
   - **Research-defined falsification threshold**: if net Sharpe ≤ 0 or net mean trade return ≤ 0 over ≥ 200 closed trades, reject the overlay as an alpha. Action: keep model as research object only.

2. **Median-TP vs no-TP ablation**  
   - Compare TP-at-median vs hold-to-maturity vs trailing.  
   - If TP-at-median does not improve expectancy, the quantile-band exit is not load-bearing.

3. **Consistency-gate placebo**  
   - Shuffle path directions or drop the consistency filter.  
   - If entry quality is unchanged, the multi-sample agreement is cosmetic.

4. **Foundation-model vs naive baselines**  
   - Same exits on random walk / last-return extrapolation / GARCH quantiles.  
   - Kronos must beat these; otherwise the "foundation model" label is not the edge.

5. **Calibration audit**  
   - Empirical coverage of P10/P90 vs nominal 80% interval.  
   - Severe undercoverage rejects using the band as a stop.

## Crypto portability

**Direct** for any liquid FMZ-listed crypto spot or perp. Notes:

- 24/7 bars; no session gap logic in source.
- Funding on perps not handled (treated as separate cost).
- Alts with sparse history may fail Lookback or produce unstable samples.
- Requires local GPU/CPU for Kronos inference — operational dependency.

Crypto portability is not authorization to trade.

## Limitations

- **No published trading performance** on the FMZ page; confidence **low**.
- Overlay is only as good as Kronos calibration on the chosen venue/period; training domain (12B K-lines, claim) may not match live crypto microstructure shifts.
- Paper-mode cost model is optimistic.
- Several critical thresholds (SignalThreshold, RiskPerTrade, etc.) are panel parameters with defaults not fully listed in the prose — reconstruction must pin them from the strategy parameter schema.
- Single position, no portfolio netting.
- FMZ artifact; Kronos SHA pinned but HF weight tags can drift unless hash-locked.

## Implementation status

- FMZ script + public Kronos repo; **not implemented** in the nautilus-quant-system research stack reviewed here.
- **Not authorized** for Paper/Testnet/Live. This record does not modify NautilusTrader, create a strategy family, or authorize execution.

## Adoption boundary

`status = research-only`. `adoption = not-approved`. `approval_scope = research-only`.

This record is a research capture of a public foundation-model trading overlay. It is not strategy adoption, implementation authorization, or permission for Paper/Testnet/Live.

## Related Wiki / repo records

- Existing transformer/TFT/forecast-to-fill records (e.g. adaptive TFT, forecast-to-fill gold, TabFM-adjacent) study different model families or venues; this record is specifically **open Kronos multi-sample quantile-band** on FMZ.
- No prior record in this repository cites `shiyu-coder/Kronos` or FMZ 537215 (searched 2026-09-15).

## Sources

1. FMZ strategy + source: https://www.fmz.com/strategy/537215 (captured 2026-09-15).
2. Kronos GitHub: https://github.com/shiyu-coder/Kronos at `67b630e67f6a18c9e9be918d9b4337c960db1e9a`.
3. HF weights (referenced by source): `NeoQuasar/Kronos-Tokenizer-base`, `NeoQuasar/Kronos-{ModelSize}`.
