---
schema: strategy-research-record-v1
title: "FMZ Online Bar-by-Bar Learning Comparison: Update Speed vs Noise Chasing Negative Evidence (546440)"
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - online-learning
  - model-risk
  - turnover-cost
  - negative-evidence
  - methodology
  - fmz
status: research-only
confidence: medium
source_as_of: 2026-07-27
sources:
  - "FMZ digest article: 'Updating the Model on Every Bar: Is It Adapting to the Market, or Chasing Noise? An FMZ Rust Online Learning Comparison', digest topic 10997, created 2026-07-27. https://www.fmz.com/digest-topic/10997"
  - "FMZ strategy page: 'Online Bar-by-Bar Learning Comparison Experiment (Rust)', strategy id 546440. https://www.fmz.com/strategy/546440"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FMZ Online Bar-by-Bar Learning Comparison: Update Speed vs Noise Chasing Negative Evidence (546440)

## Provenance

- **Source URL (article):** https://www.fmz.com/digest-topic/10997
- **Source URL (strategy):** https://www.fmz.com/strategy/546440
- **Source type:** Public FMZ digest with methodology narrative, Rust code excerpts, and one published default-parameter backtest; companion public strategy page (shadow-account experiment; no live order placement).
- **Platform:** FMZ / 发明者量化
- **Created (source-reported):** digest 2026-07-27
- **Source reviewed as of:** 2026-09-20 (full digest body + strategy URL identity)
- **Deduplication audit (2026-09-20; origin/main):** No prior record cites FMZ id `546440`, digest topic `10997`, or this four-arm online-learning update-speed comparison. Adjacent records are different:
  - `crypto-order-flow-online-sgd-microstructure-horizon-cost-falsification-2026-09-13.md` — online SGD on order-flow microstructure; different features/target/mechanism.
  - `crypto-adaptive-anchored-vwap-online-logistic-reclaim-source-code-audit-2026-09-14.md` — online logistic on anchored VWAP reclaim; different signal family.
  - `market-making-online-lob-action-dependent-feedback-2026-09-02.md` / `recurrent-reinforcement-learning-funding-profit-perpetual-swap-2026-09-06.md` — MM/RRL systems; not a controlled update-speed ablation.
  - `look-ahead-bias-pretrained-financial-forecasting-pit-vintage-arxiv-2609.20554-2026-09-19.md` — foundation-model vintage/look-ahead; not online update cadence.

## Economic mechanism

### Source-reported

Source-reported research question: holding model structure, features, trading rules, and cost assumptions **completely constant**, how does the speed at which a model absorbs new samples affect out-of-sample loss, parameter stability, turnover, and simulated equity?

Source-reported framing: online learning is often justified by market non-stationarity; faster updates may help after breakdowns but can also write short-term noise into parameters, producing higher turnover, cost sensitivity, and path dependence.

Source-reported hypotheses (pre-declared, not assumed true):

1. Per-bar online updates may shorten recovery after regime change.
2. The same mechanism may amplify parameter fluctuations, signal reversals, and costs.
3. Performance may not improve monotonically with update frequency; intermediate speed may be more stable.

Source-reported design (one Rust process, four parallel models):

| Model | Update method |
|-------|----------------|
| Fixed | No updates after shared initialization |
| Per-bar online | One gradient step when each label becomes available |
| Rolling retraining | Reset + retrain on last window every N bars |
| Error-gated | Slow small-batch update when Log Loss EMA exceeds baseline × multiplier |

Source-reported controls: same init params, features, L2 logistic regression, long/short probability thresholds, return mapping, one-way turnover cost, synchronous settlement; **test-then-train** order; bar-completion corrected via `IsVirtual()` (backtest uses second-to-last bar); fixed standardizer fitted on first 80% of init samples only.

Source-reported public backtest (default params; **not** claimed as general proof):

```text
Instrument: ETH_USDT.swap
Timeframe: 15 minutes
Period: 2025-07-09 to 2026-06-21
Initialization samples: 320
OOS bars: 33333
Base learning rate: 0.02
Rolling window: 240; retrain every 32 bars
Error gate: loss EMA > 1.10 × baseline; batch 32; lr scale 0.25; cooldown 32 bars
Position map: p>=0.55 long; p<=0.45 short; else flat
Cost: CostBps default 5 (one-way per unit turnover)
```

Source-reported OOS table direction (accuracy / Log Loss / turnover / flips / net return):

- Fixed: 52.07% / 0.7094 / turnover 24755 / flips 4985 / net ≈ −100%
- Per-bar online: 51.44% / 0.7203 / turnover 21073 / flips 3619 / net ≈ −100%
- Rolling: 51.74% / 0.7301 / turnover 21271 / flips 4111 / net ≈ −100%
- Error-gated: 49.40% / 0.6986 / turnover 6190 / flips 142 / net ≈ −98%

Source-reported interpretation of that single run: naive Log Loss benchmark ≈ 0.6931; all four averaged worse; more frequent updates **did not** improve OOS probability forecasts; gating reduced noise reactions but did **not** create trading edge; fixed weights can still produce high turnover because features change every bar; equity near zero saturates return/DD metrics.

Source-reported conclusion: “If a model merely updates more frequently, moves its parameters farther, and trades more often—without persistently reducing out-of-sample loss—it has not adapted better to the market.”

### Research interpretation

This is **family-level methodology / negative-evidence** for the claim that “more frequent online updates = better market adaptation” on a crypto perpetual bar-forecasting stack — not a profitable strategy and not proof that online learning is useless elsewhere.

Research relevance:

1. **Update speed is a model-risk axis:** cadence itself confounds “adaptation” claims unless structure/features/costs are held fixed (source design).
2. **Turnover ≠ adaptation:** parameter displacement + rising flips without lower Log Loss is a noise-chasing signature (source metric set).
3. **Cost honesty:** stability without edge still fails after turnover costs — gating is not alpha.
4. **Boundary:** any future Scout capture asserting online/adaptive superiority must report Log Loss, turnover, parameter displacement, and multi-cost scenarios, not equity alone.

Component roles (normalized):

```text
Not a production alpha.
Evidence class: controlled update-speed ablation / negative evidence.
Required practice (research-proposed): test-then-train; completed-bar discipline; report gross vs net vs turnover; multi-cost (0/2/5/10 bps); neighboring hyperparameters; regime breakdown.
```

## Signal

Not a standalone alpha entry/exit for adoption. The experiment **does** define a reconstructable research mapping:

### Formation timestamp

Bar \(t\) close → features \(x_t\) → predict open-to-close direction of bar \(t+1\); assume entry near \(t+1\) open after completion check; label and return realized at \(t+1\) close; **evaluate previous prediction before any model update**.

### Lookback

- Features: current and previous bar (body/range/wicks/volume); 3-bar momentum; 5-bar realized volatility (eight features total in source design).
- Init: 320 supervised samples; first 80% batch epochs; last 20% predict-then-update for baseline loss; shared init state for all four models.
- Rolling model: last 240 samples, retrain every 32 new labels.

### Long entry

Research mapping (source code default): predicted probability \(p \ge 0.55\) → long at next-bar open (simulated).

### Short entry

\(p \le 0.45\) → short; else flat.

### Exit

Position change whenever probability crosses thresholds (including flip long↔short as turnover 2). No stop/take-profit ladder in the experiment.

### Holding period

One-bar open-to-close exposure path when in market; overlapping only in the sense that each bar’s position is re-decided from the current model (no multi-day hold ladder).

### Parameters (source-reported public defaults)

| Parameter | Default | Role |
|-----------|---------|------|
| Instrument | ETH_USDT.swap | Demo universe |
| Timeframe | 15m | Bar grid |
| Base lr | 0.02 | Shared; not optimized in-sample (source) |
| Rolling window / interval | 240 / 32 bars | Periodic retrain |
| Gate loss multiplier / batch / lr scale / cooldown | 1.10 / 32 / 0.25 / 32 bars | Error-gated arm |
| Long/short thresholds | 0.55 / 0.45 | Prob → position |
| CostBps | 5 | One-way per unit turnover (research demo, not any venue fee schedule) |
| Gradient clip | ±5 weights; ±1 bias | Stability, not claimed alpha |
| Standardizer | Fit on first 80% of init; fixed thereafter | Isolates update-speed effect |

**Underspecified:** exact feature formula completeness in the narrative for realized vol (code continues the window); live fee/funding/impact; other instruments/timeframes (source explicitly says single run cannot answer “is online learning better?”).

### Position sizing

Binary −1/0/+1 map only; no vol-target or Kelly in the experiment.

### Specification completeness

**High for the controlled comparison design** (features list, update rules, thresholds, cost parameter, test-then-train, bar-completion fix). **Not a production trading rule.**

## Required data

- **Instrument:** source demo `ETH_USDT.swap`; research framework is instrument-agnostic in principle.
- **Venue / market type:** FMZ-connected crypto perpetual bar data (simulation); no live orders in the strategy description.
- **Timeframe:** 15-minute completed bars (source demo).
- **Fields:** OHLCV per bar sufficient for the eight raw features (return, body, range, upper/lower wick ratios, volume change, 3-bar momentum, 5-bar realized vol).
- **Point-in-time:** features from bar \(t\) only; label from bar \(t+1\) after it completes; no same-bar close fill assumption (source narrative).
- **Timestamp:** FMZ bar times; backtest uses conservative second-to-last bar when `IsVirtual()`.
- **Missing data:** not deeply specified beyond epsilon guards in code snippets (`underspecified`).
- **Costs:** configurable one-way `CostBps` on turnover; **not** exchange fee schedules; funding omitted in the demo mapping.

## Execution assumptions

Source-reported simulation assumptions (explicit simplifications):

- Signal-to-order: predict after bar \(t\) close; enter near open of bar \(t+1\).
- Fill model: open-price approximation; no order-book, latency, or impact.
- Cost: `CostBps/10000` per unit turnover; default 5 bps one-way.
- Shadow accounts only; strategy “does not send orders to an exchange.”
- Source states a real order may not fill at next open; cost is a stress-test parameter, not a venue fee.

Research interpretation: results are **execution-model conditional**; they must not be read as live performance.

## Evidence

### Source-reported

All quantitative figures below trace to FMZ digest **10997** (created 2026-07-27; reviewed 2026-09-20) and companion strategy **546440**:

- Demo: ETH_USDT.swap 15m, 2025-07-09 to 2026-06-21, 320 init samples, 33333 OOS bars, lr 0.02, rolling 240/32, CostBps 5, thresholds 0.55/0.45.
- OOS label counts: 16644 up / 16689 non-up; 36 bars with open==close (code term **non-up**, `Close<=Open`).
- Accuracy / Log Loss / position rate / turnover / long-short flips / parameter displacement / net: Fixed 52.07% / 0.7094 / 65.2% / 24755 / 4985 / 0 / ≈−100%; Per-bar 51.44% / 0.7203 / 56.7% / 21073 / 3619 / 0.4409 / ≈−100%; Rolling 51.74% / 0.7301 / 64.6% / 21271 / 4111 / 0.5712 / ≈−100%; Error-gated 49.40% / 0.6986 / 18.3% / 6190 / 142 / 0.2989 / ≈−98%.
- Init reference Log Loss 0.6988; naive 0.5 predictor Log Loss ≈ 0.6931; all four OOS averages **above** 0.6931.
- Source: per-bar and rolling moved parameters but **worse** Log Loss than fixed; gating triggered **8** updates; earlier version’s near-100% accuracy was an incomplete-bar bug, not edge.
- Source explicitly: single backtest ≠ general conclusion; more frequent updates did not show stronger adaptation **under these conditions**.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- Source-reported **negative direction for “update more often = better adaptation”** on this single ETH 15m demo: OOS Log Loss not improved by faster updates; all arms deeply negative after costs; gating = stability without edge.
- Source-reported equity saturation near zero: net return/DD lose discriminating power under extreme turnover+cost — negative evidence for equity-only model selection.
- Research interpretation: not proof online learning fails on other assets/targets/models; deep models not covered (source limitation).
- No independent re-run of 546440 in our stack this cycle.
- Absence of our replication is not evidence that the FMZ table is wrong — only that we did not recompute it.

## Falsification plan

Research-proposed evaluation standards for future “online/adaptive superiority” claims (not source trading alpha):

1. **Adaptation gate (research-defined falsification threshold):** Claim of superior adaptation requires pre-declared **lower** OOS Log Loss (or proper scoring rule) vs fixed baseline **and** non-material turnover increase; fail if only equity/accuracy moves or Log Loss worsens while displacement/flips rise.
2. **Cost grid:** Evaluate 0 / 2 / 5 / 10 bps one-way; fail “trading edge” claims that exist only at 0 bps — write “more gross signals” instead.
3. **Test-then-train audit:** Fail any pipeline that updates on sample \(t\) before scoring prediction on \(t\); fail incomplete-bar labels.
4. **Shared-init control:** Fail comparisons where update arms start from different training histories.
5. **Neighboring hyperparameters:** lr 0.01/0.02/0.04; retrain 16/32/64; window 120/240/480; gate 1.05/1.10/1.20 — fail single-point-only advantages.
6. **Regime breakdown:** If faster update helps only in transitions while leaking in calm periods, report split results; fail aggregate-only promotion.
7. **Action on failure:** Keep adaptive-model strategy records `research-only`; do not treat FMZ 546440 as validated alpha or as a universal ban on online learning.

## Crypto portability

**Portability: `direct` for the evaluation domain (crypto perpetual bars); `not applicable` as a deployable trading port.**

- Demo is crypto-native (ETH USDT perp, 15m).
- Risks if misused as alpha: cost/funding omitted; open-fill approximation; single-instrument demo; logistic linear features may not transfer; 24/7 bars differ from session markets.
- Crypto portability is not authorization to trade.

## Limitations

- **Not a strategy edge** — controlled methodology experiment with shadow accounts.
- **not independently reproduced**
- **Single instrument/timeframe/period** in the published table; source itself says this cannot answer “is online learning better?” universally.
- **underspecified:** full live execution, funding, missing-data policy; realized-vol feature implementation only partially narrated.
- Error gate is **heuristic**, not a formal drift detector (source names ADWIN/DDM as future work).
- Fixed standardizer mixes relationship failure with scale mismatch (source limitation).
- Equity saturation under 5 bps reduces economic discrimination among arms.
- Incremental value: **public reconstructable FMZ update-speed ablation with negative OOS evidence** on crypto bars — distinct from online SGD/order-flow and VWAP-reclaim online logistic records.

## Implementation status

No implementation in our research stack. Does not modify NautilusTrader/PyBroker; does not authorize Paper/Testnet/Live.

`implementation_status: not-implemented`

Source-side: FMZ hosts Rust experiment 546440 (shadow only); **not** treated as our validation.

## Adoption boundary

Research-only. Presence here does **not** mean profitable, validated, or approved for implementation, paper, testnet, or live trading.

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

## Related Wiki records

No stable Hermes Wiki Brain path known at write time. Do not fabricate Wiki links.

In-repo related: `crypto-order-flow-online-sgd-microstructure-horizon-cost-falsification-2026-09-13.md`; `crypto-adaptive-anchored-vwap-online-logistic-reclaim-source-code-audit-2026-09-14.md`; look-ahead PIT-vintage record; other adaptive/online ML captures (different mechanisms).

## Sources

1. FMZ Quant. 「Updating the Model on Every Bar: Is It Adapting to the Market, or Chasing Noise? An FMZ Rust Online Learning Comparison.」 Digest topic 10997, created 2026-07-27. https://www.fmz.com/digest-topic/10997 (full article body reviewed 2026-09-20).
2. FMZ Quant strategy page. 「Online Bar-by-Bar Learning Comparison Experiment (Rust).」 Strategy id 546440. https://www.fmz.com/strategy/546440 (identity preserved; public code excerpts in digest; full export not independently audited this cycle).
