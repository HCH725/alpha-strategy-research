---
schema: strategy-research-record-v1
title: "Continuation-Aware PPO Inaction Audit: BTCUSDT Taker-Imbalance Override Under High Hold Probability"
created: 2026-09-14
updated: 2026-09-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - bitcoin
  - reinforcement-learning
  - ppo
  - policy-audit
  - order-flow
  - transaction-costs
  - btcusdt
status: research-only
confidence: medium
source_as_of: 2026-09-11
sources:
  - "Xingfei Zeng, Xin Zhong, Nanting Li, Ziyang Zhong, Lei Xiao, and Guanghui Lu, 'When Is Inaction a Mistake? Continuation-Aware Auditing of PPO Trading Policies', arXiv:2609.12536v1 [cs.CE], September 11, 2026. https://arxiv.org/abs/2609.12536"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Continuation-Aware PPO Inaction Audit: BTCUSDT Taker-Imbalance Override Under High Hold Probability

## Provenance

- **Source**: arXiv:2609.12536v1 [cs.CE]
- **Authors**: Xingfei Zeng, Xin Zhong, Nanting Li, Ziyang Zhong, Lei Xiao, Guanghui Lu (UESTC; The University of Tokyo)
- **Version**: v1, submitted September 11, 2026
- **DOI**: https://doi.org/10.48550/arXiv.2609.12536
- **URL**: https://arxiv.org/abs/2609.12536
- **Full text HTML**: https://arxiv.org/html/2609.12536v1
- **Code / frozen policy artifacts**: available from the authors upon request (no public GitHub commit SHA disclosed in the preprint)
- **BTCUSDT sample**: Binance USDT-margined BTCUSDT minute data; PPO training 2021–2023; intervention selection on 2024; frozen evaluation on 2025
- **Affiliations stated**: University of Electronic Science and Technology of China; The University of Tokyo

### Repository Deduplication Audit

Repository-wide search on 2026-09-14 found zero prior records citing `arXiv:2609.12536`, Zeng/Zhong/Li et al., continuation-aware PPO inaction audit, or the hold-probability + taker-imbalance override rule on BTCUSDT. Adjacent records:

- Multiple crypto RL records (`meta-rl-crypto-self-improving-meta-reward-trading-agent`, `fineft-risk-aware-ensemble-rl-vae-routing-crypto-futures`, `crypto-bitcoin-cvar-risk-aware-q-learning-adaptive-controller`) optimize policies; they do not publish this four-stage inaction audit or this cost-dominated override construction
- Order-flow imbalance records (e.g., `crypto-multilevel-order-flow-imbalance-intraday-2026-08-31.md`, `edgeflow-composite-lob-microstructure-alpha-binance-spot-2026-09-09.md`) use imbalance as a primary signal; here imbalance is a **conditional override of a frozen PPO hold**, not a standalone ranking factor
- LLM-agent production record (`llm-agent-population-scale-behavioral-null-volatility-blind-sizing-2026-09-10.md`) is a different agent class and measurement design

## Economic mechanism

### Source-reported

Proportional transaction costs create an optimal no-trade region. A frozen PPO policy may hold either because it faces costs, lacks informative observations, or follows a poor rule. The paper introduces a **four-stage post-hoc audit** without retraining:

1. **Full-belief audit** — where does the deployed policy disagree with a DP reference?
2. **Current-information projection** — does disagreement survive information matching?
3. **Incumbent-continuation audit** — would changing this action help if PPO resumes?
4. **Repeated restricted deployment** — does an observation-based rule used every step help?

In linear–Gaussian simulations at unit observation noise, occupancy-weighted projection reduces hard false-inactive labels from 49/50 to 38/50; **incumbent continuation reverses 99.3% of projected-hard missed-advantage mass**; yet **repeated projected-rule deployment improves all 50 policies** (mean gain 0.245 [0.205, 0.284]). Isolated-action and policy-replacement verdicts are therefore distinct.

On BTCUSDT, a **hand-specified intervention** is applied when PPO hold probability exceeds 0.9 and absolute taker-volume imbalance exceeds a training-quantile threshold: take the imbalance direction if it differs from inventory, hold for H minutes, then resume the hybrid rule.

### Research interpretation

The crypto-relevant claim is a **cost-dominated relative gain**: a frozen RL trader that almost always holds can be overridden by a simple order-flow condition, and the daily net improvement comes mainly from **lower turnover cost**, not from better gross signal. The audit formalizes why “oracle says trade but policy holds” is not automatically a defect: continuation assumptions flip most isolated trade advantages, while a different repeated rule can still improve deployment value.

## Signal

### Formation timestamp

Minute bars; daily episodes in UTC that start and end flat (`source-reported`). Signals use training-standardized causal inputs.

### Lookback

PPO features use training-window standardization. The frozen intervention itself is memoryless at decision time except for current inventory and the H-minute hold after override (`source-reported`).

### Entry (source-reported BTCUSDT intervention)

On each minute:

1. Observe frozen PPO action distribution.
2. If `p(hold) > 0.9` **and** `|taker-volume imbalance| > q`, where `q` is a quantile of training-data imbalance (selected among {0.75, 0.90, 0.95} on 2024):
3. If imbalance direction ≠ current inventory, take imbalance direction.
4. Hold that position for `H` minutes (`H ∈ {5, 15, 60}`; selected `H = 60`).
5. Then resume the hybrid (PPO + override) rule.

Selected on 2024: **q = 0.75 (threshold 0.3951), H = 60**. Frozen for all 50 policies in 2025 without retraining or reselection.

PPO training inputs (`source-reported`): taker-volume imbalance, returns, exponential moving average, volatility, volume, coverage — training-standardized, causal.

### Entry (research-proposed generalization)

`research-proposed`: treat high-probability-hold RL policies as candidates for a **sparse order-flow override**, but require (a) pre-period selection freeze, (b) gross-vs-cost decomposition, and (c) comparison to always-flat and passive hold baselines before any edge claim. This is methodology transfer, not a validated crypto strategy in our stack.

### Exit

Override positions exit after H minutes back into the hybrid rule (`source-reported`). Daily session ends flat (`source-reported`).

### Holding period

- Override: H = 60 minutes (selected)
- Episode: one UTC day, forced flat at session end (`source-reported`)
- Positions: {-1, 0, +1} (`source-reported`)

### Parameters

- Actions: {-1, 0, +1} (`source-reported`)
- Hold-probability gate: > 0.9 (`source-reported`)
- Imbalance quantile grid: {0.75, 0.90, 0.95}; selected 0.75 → threshold 0.3951 (`source-reported`)
- H grid: {5, 15, 60} minutes; selected 60 (`source-reported`)
- Turnover cost: 1.5 bp per unit (`source-reported`)
- PPO: two-layer 64-unit ReLU actor/critic, Adam 1e-4, clip 0.2, GAE λ=0.95, zero entropy in BTCUSDT arm (`source-reported`)
- Training steps (BTCUSDT): 30,720 on 2021–2023 (`source-reported`)

## Required data

- **Instrument**: BTCUSDT USDT-margined perpetual/minute series as used by the authors on Binance (`source-reported`)
- **Universe**: single-asset BTCUSDT (`source-reported`)
- **Venue**: Binance (`source-reported`)
- **Timeframe**: 1-minute (`source-reported`)
- **Fields**: open (for open-to-open log returns), taker-volume imbalance, returns, EMA, volatility, volume, coverage (`source-reported`)
- **Point-in-time**: causal training-standardized inputs; intervention selected on 2024 and frozen for 2025 (`source-reported`)
- **Timestamp**: UTC daily episodes (`source-reported`)
- **Missing-data / fees**: 1.5 bp unit turnover cost modeled; spread/impact/funding not separately stressed in the BTCUSDT intervention results

## Execution assumptions

- **Order type / fill**: next-open-to-open log returns on {-1,0,1}; replay integrates action probabilities exactly on each path (`source-reported`)
- **Latency**: not modeled beyond bar-timing convention
- **Liquidity / capacity**: not analyzed for BTCUSDT size
- **What the source assumes**: relative net reward vs frozen PPO and always-flat; **explicitly not** absolute profitability or superiority to buy-and-hold
- **What the Scout does not assume**: no live fillability, no funding treatment, no multi-venue robustness

## Evidence

### Source-reported

**Simulation (unit observation noise, 50 seeds)**:
- Full belief: 49/50 hard false-inactive; OAR 0.293 [0.253, 0.332]
- Current-info projection: 38/50 hard; G_cell = 0.193 [0.165, 0.220]
- Incumbent continuation: **99.3%** AMA-weighted reversal [0.989, 0.996]
- Repeated restricted rule: **+0.245** [0.205, 0.284]; **50/50** improve
- Kalman vs raw: hard 23/50 vs 49/50; AMA 0.127 vs 0.243; OAR 0.163 vs 0.293

**BTCUSDT frozen intervention (50 policies)**:
- Selection year 2024: daily net gain **159.11 bp**; 47/50 improve
- Frozen year 2025: daily net gain **135.03 bp**; **46/50** improve
- 2025 bootstrap (circular block, 2,000 reps): [125.50, 144.63] bp (7-day); [122.33, 148.09] bp (30-day)
- 2025 decomposition: gross reward **−3.71 bp/day**; costs **−138.74 bp/day** → **cost-dominated**
- Always-flat earns zero by definition; relative gains do not establish absolute profitability or buy-and-hold superiority (`source-reported` caveats)

### Independently reproduced

`not independently reproduced`

Code and frozen policy artifacts are available from the authors upon request; this Scout cycle did not re-run the pipeline.

### Negative evidence

- **Gross edge is not positive** on BTCUSDT 2025 for the override vs frozen PPO: gross reward change is −3.71 bp/day; the entire net gain is cost reduction
- **Isolated-action oracle flags are mostly misleading** under incumbent continuation (99.3% mass reversal in simulation)
- **Not a standalone alpha claim**: paper explicitly refuses absolute profitability and passive-hold superiority
- Capacity, funding, and multi-venue replication are absent
- Intervention grid is small (3 quantiles × 3 horizons) and selected on a single 2024 year

## Falsification plan

1. **Walk-forward freeze replication on later years**. Keep q=0.75 / H=60 / p(hold)>0.9 fixed; evaluate 2026+ BTCUSDT. **Research-defined falsification threshold**: if 2025-style net gain collapses below +20 bp/day median across a new 50-policy cohort, treat the 2024–2025 result as sample-specific.
2. **Gross-first test**. Recompute with zero costs. If gross remains ≈0 or negative while net is positive only via turnover cut, label the effect a **cost-management overlay**, not return alpha.
3. **Passive baselines**. Compare to buy-and-hold BTC and always-in-market 1x long after the same cost model. Reject any “edge” language if those baselines dominate.
4. **Imbalance-shuffle placebo**. Permute imbalance series within day while keeping PPO holds. If override still “helps,” the benefit is from forced diversification of hold times, not order-flow information.
5. **Gate sensitivity**. Vary p(hold) ∈ {0.8, 0.9, 0.95} and H ∈ {15, 30, 60, 120} without reselection. If only the 2024-selected cell works, report overfit-to-selection.
6. **Funding and spread stress**. Add 8h funding and half-spread; recompute net bp/day. **Research-defined falsification threshold**: net ≤ 0 after funding+spread.
7. **Audit-stage consistency on market data**. Apply stages 1–3 (full-belief, projection, incumbent continuation) to the BTCUSDT PPO cohort rather than only stage 4; if stages 1–3 already predict that most flags are continuation-reversed, stage-4 gains should be interpreted as policy replacement, not “fixed inaction.”

## Crypto portability

**Direct** for BTCUSDT Binance minute perps as studied; **adapted** for other liquid crypto perps.

- 24/7 continuous session: daily UTC episode flattening is a modeling choice, not a market close
- Taker-volume imbalance is available on major CEX perps
- Funding is **not** in the BTCUSDT intervention reward; any port must add funding when holding 60 minutes across funding windows
- Venue fragmentation: imbalance definitions differ by exchange; rebalance threshold 0.3951 is venue- and sample-specific
- Crypto portability is **not** authorization to trade

## Limitations

- **Cost-dominated relative result**, not absolute alpha
- Single asset, single venue, minute bars
- Small hyperparameter grid; 2024 selection / 2025 freeze is one holdout pair
- No funding, spread, or impact model in the headline BTCUSDT numbers beyond 1.5 bp unit cost
- PPO policies are frozen black boxes from the authors’ training run; reproducibility depends on author-supplied artifacts
- Simulation (linear–Gaussian) and market (BTCUSDT) stages answer related but not identical questions
- Preprint: arXiv v1; not peer-reviewed at capture time

## Implementation status

`not-implemented`

No PPO BTCUSDT policy, continuation-audit harness, or override rule exists in our research stack. No PyBroker/NautilusTrader strategy, no paper/testnet/live configuration.

## Adoption boundary

This record is research material only. Presence in this repository does not mean profitable, validated alpha, or approval for implementation, paper trading, testnet, or live trading. The authors themselves frame BTCUSDT results as relative, cost-dominated deployment gains.

## Related Wiki records

- [[quant/strategy-research-record-spec-v1]] — canonical schema
- `crypto-multilevel-order-flow-imbalance-intraday-2026-08-31.md` — order-flow imbalance family
- `edgeflow-composite-lob-microstructure-alpha-binance-spot-2026-09-09.md` — LOB composite signals on Binance
- `llm-agent-population-scale-behavioral-null-volatility-blind-sizing-2026-09-10.md` — different agent class (LLM), production measurement
- `crypto-hourly-bitcoin-walk-forward-cost-aware-execution-2026-09-01.md` — cost-aware BTC walk-forward family
- `binance-perpetual-order-flow-imbalance-horizon-decay-queue-imbalance-falsification-2026-09-13.md` — OFI horizon/cost falsification

## Sources

1. Xingfei Zeng, Xin Zhong, Nanting Li, Ziyang Zhong, Lei Xiao, and Guanghui Lu. "When Is Inaction a Mistake? Continuation-Aware Auditing of PPO Trading Policies." arXiv:2609.12536v1 [cs.CE], September 11, 2026. https://arxiv.org/abs/2609.12536
