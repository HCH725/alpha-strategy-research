---
schema: strategy-research-record-v1
title: Prediction-Market LLM Confidence-Weighted Value Bet with Point-in-Time News and CLOB Execution
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - prediction-markets
  - polymarket
  - llm
  - value-bet
  - confidence-calibration
  - order-book
status: research-only
confidence: medium
source_as_of: 2026-04-03
sources:
  - https://arxiv.org/abs/2604.14199
  - https://arxiv.org/html/2604.14199v1
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Prediction-Market LLM Confidence-Weighted Value Bet with Point-in-Time News and CLOB Execution

## Provenance

Primary source: Pu Cheng, Juncheng Liu, and Yunshen Long, **“PolyBench: Benchmarking LLM Forecasting and Trading Capabilities on Live Prediction Market Data,”** arXiv:2604.14199v1 [q-fin.CP], submitted 2026-04-03, DOI `10.48550/arXiv.2604.14199`.

The source constructs a timestamp-locked Polymarket benchmark from 38,666 binary market snapshots spanning 4,997 events. Market states were collected from 2026-02-06 through 2026-02-12 and coupled with contemporaneous CLOB state, event metadata, resolution criteria, and Google News. The latest market resolution used in evaluation occurred on 2026-02-21. The study reports 36,165 LLM predictions under these point-in-time states.

Repository-wide source-identity checks on 2026-09-04 found no existing record matching arXiv `2604.14199`, the exact paper title, `PolyBench`, or the source's Confidence-Weighted Return construction. Broader mechanism search found multiple existing prediction-market records, including cross-venue BTC lead-lag, informed-wallet/order-flow, structural-volatility, and executable-arbitrage records, but none uses a point-in-time multimodal LLM posterior plus confidence-gated value betting against historical CLOB depth. This record is therefore distinct at the source, signal-construction, data-dependency, and execution-mechanism levels.

The source also publishes code and data at `https://github.com/PolyBench/PolyBench`, but this Scout record does not rely on a mutable GitHub snapshot for any empirical claim; all normalized claims below are traced to the versioned arXiv v1 paper. No GitHub implementation claim is made here.

## Economic mechanism

### Source-reported

The source frames decentralized prediction-market prices as market-implied probabilities that can be challenged when a forecasting agent combines information not fully reflected in the current CLOB price. Each LLM receives a timestamp-anchored market state containing the exact resolution rule, market/order-book information, and contemporaneous news. The prompt explicitly directs the model to look for `value_bet` opportunities when its posterior probability materially differs from the market-implied probability and to abstain when there is no positive expected-value opportunity or confidence is below 0.6.

The source also treats model confidence as economically meaningful. Its Confidence-Weighted Return (CWR) sizes the per-trade budget in proportion to declared confidence and executes the simulated purchase through historical CLOB asks rather than assuming unlimited fills at one price. The authors report that CWR exceeds the corresponding unweighted return for all seven tested models, but only two models produce positive overall CWR.

### Research interpretation

The falsifiable mechanism is **information aggregation plus calibration**: a forecasting model may earn a prediction-market edge only when its point-in-time posterior contains incremental information beyond the market price and when its confidence is sufficiently calibrated that higher declared confidence corresponds to larger true pricing errors in the model's favor.

This is not a generic “LLMs predict markets” claim. The hypothesized edge requires all of the following jointly:

1. strict point-in-time news and market-state availability;
2. correct interpretation of the contract's resolution rule;
3. a posterior probability that differs from the executable market price by enough to compensate for spread/slippage and other omitted costs;
4. calibrated confidence that is useful for abstention and sizing;
5. sufficient CLOB depth to execute without erasing the edge.

The source's severe negative performance in the Crypto event domain is evidence that the mechanism is domain-dependent rather than universally portable across event types.

## Signal

The paper defines a benchmark trading-agent procedure, not a frozen production strategy for one durable model. The source-specified components are:

- **Formation timestamp:** each decision is made from a historical, timestamp-locked snapshot. The prompt is anchored to the snapshot's `Current Date`; future news or later market states are not permitted.
- **Inputs:** event question and metadata, exact resolution criteria, contemporaneous market prices/CLOB information, and prefetched contemporaneous Google News.
- **Forecast output:** the model emits a structured prediction including the selected outcome, confidence `c_i in [0,1]`, rationale/strategy tag, and action compliance fields.
- **Confidence gate:** predictions with confidence below `0.6` are discarded / skipped under the source protocol.
- **Value-bet concept:** the prompt directs the model to identify positive-EV opportunities where its posterior deviates from market-implied odds; the source does not publish one universal numerical posterior-minus-price edge threshold beyond the confidence gate.
- **Sizing:** for executed trade `k`, the source sets budget `B_k = c_k * L`, where `L` is the base lot size. The main Table 5 comparison uses `L = $10`.
- **Execution:** simulated purchase sweeps the contemporaneous CLOB starting from the best ask; invested amount and acquired shares depend on available depth and slippage.
- **Settlement:** a correctly predicted purchased outcome pays according to the binary settlement; an incorrect outcome loses the invested amount. CWR aggregates realized profit divided by total invested capital.
- **Holding period:** from simulated purchase until the binary market resolves; duration varies by event.
- **Re-entry / repeated trading:** the paper evaluates snapshot-level predictions across many markets rather than specifying a stateful re-entry rule for repeatedly trading the same contract. This is **underspecified** for a production strategy.
- **Stops / take-profit:** not source-specified. The benchmark holds the simulated outcome exposure to resolution for payoff accounting.

Important ambiguity: the paper's benchmark maps the model's selected outcome to a purchasable binary position, but a general production implementation's exact YES-versus-NO token routing, order cancellation policy, partial-fill policy, and repeated-snapshot inventory netting are **underspecified** and must not be invented as source-reported rules.

A later executable alpha test may define an explicit edge threshold such as `model_posterior - executable_ask`, but any such threshold is **research-proposed**, not source-reported.

## Required data

For direct source reproduction:

- Polymarket binary event identifiers and exact resolution criteria;
- exact point-in-time snapshot timestamps;
- contemporaneous outcome prices and CLOB ask-side depth sufficient to replay marketable purchases;
- the paper's snapshot pipeline captures up to the top five order-book levels for the reported sizing stress;
- contemporaneous event metadata;
- timestamp-aligned Google News used by the benchmark;
- final market resolution / winning outcome;
- exact tested model/version and inference settings;
- emitted predicted outcome, confidence, strategy tag, and skip/action state;
- base lot `L` and execution-replay accounting.

Point-in-time requirements are first-order:

- no news item published after the snapshot timestamp may enter the prompt;
- no revised resolution wording or later market metadata may be backfilled into an earlier decision state unless the source snapshot contained it then;
- no later CLOB state may determine the historical fill;
- model versions and prompts must be immutable within a replication tranche, because provider-side model drift can otherwise contaminate comparisons;
- missing news or missing CLOB snapshots must remain explicit missingness rather than being silently reconstructed from later data.

For a modern live-like research replication, also record observed maker/taker fee schedule, spread, gas/relayer charges where applicable, API latency, rejected orders, partial fills, available balance/collateral, and market-specific fee rules. The arXiv text does not state a separate explicit trading-fee or gas deduction in the CWR formula, so these are a **data / cost gap** relative to a full net-trading return.

## Execution assumptions

Source-reported execution uses historical CLOB replay rather than flat-price fills. Budget is confidence-scaled, and purchases consume asks beginning at the best ask. The captured order-book pipeline is limited to the top five depth levels, and the authors cap their reported lot-size stress at `L = $1,000` to stay within captured depth.

The source directly demonstrates execution-capacity sensitivity: as `L` increases from $10 toward $1,000, wider effective execution prices materially reduce CWR. The paper states that alpha is mostly preserved for the top models at `L <= $100`; Gemini-3-Flash degrades materially as size grows, while MiMo-V2-Flash remains more resilient to about $500 before also succumbing to liquidity limits.

The following production details are **underspecified** in the source and must not be silently treated as zero-cost or perfectly fillable:

- explicit Polymarket trading fees for each market class;
- Polygon gas or relayer economics;
- signal-to-order inference and network latency;
- queue position and order races between snapshot and submission;
- market movement during LLM inference;
- partial-fill / stale-book failure handling outside the replay abstraction;
- capital tied up until resolution;
- cancellation and replacement rules;
- simultaneous exposure and portfolio concentration limits.

Any later live-like test should use only information available before order submission and should reprice the executable edge after inference latency. That is **research-proposed** execution discipline, not a source-reported result.

## Evidence

### Source-reported

The source reports the following for its 2026-02-06 to 2026-02-12 timestamp-locked collection and subsequent resolutions:

- 38,666 binary market snapshots across 4,997 events;
- 36,165 LLM predictions across seven tested models;
- Table 5, base lot `L = $10`: MiMo-V2-Flash reports `17.6%` CWR and `11.1%` unweighted return; Gemini-3-Flash reports `6.2%` CWR and `4.1%` unweighted return;
- the other five tested models report negative CWR: Grok-4.1-Fast `-12.1%`, GPT-OSS-120B `-17.8%`, DeepSeek-V3.2 `-11.4%`, Trinity-Large `-9.2%`, and MiniMax-M2.5 `-25.2%`;
- Table 6 reports MiMo-V2-Flash's `value_bet` subset at `19.2%` CWR and its `news_catalyst` subset at `50.0%` CWR; Gemini-3-Flash reports `7.2%` and `20.7%`, respectively. These are conditional source-reported benchmark results, not independently validated standalone strategy returns;
- the paper reports strong lot-size decay from order-book slippage as the base lot is scaled toward $1,000;
- the paper reports severe overconfidence and deep negative returns in the Crypto event category even though declared confidence remains roughly 0.8-0.9.

The paper's very large annualized APY figures are not used here as evidence of durable alpha because the evaluation window is extremely short and event durations are heterogeneous. The reported Sharpe values in Table 5 are also near zero for the two positive-CWR models (`0.02` for MiMo-V2-Flash and `0.01` for Gemini-3-Flash), which is important context against reading the headline CWR as a mature strategy verdict.

### Independently reproduced

not independently reproduced

### Negative evidence

- Five of seven tested LLMs lose money under the same benchmark despite high declared confidence; model selection is therefore a dominant fragility.
- The Crypto event category exhibits severe negative returns with persistent high confidence, directly contradicting any claim that text/news reasoning is sufficient across high-volatility crypto-linked binary markets.
- Returns decay sharply with larger base lots because top-of-book depth is finite; the edge is capacity-constrained.
- The benchmark sample is only about one week of snapshot collection in February 2026, followed by resolution through February 21; long-horizon regime stability is **unproven**.
- The reported benchmark uses a fixed historical snapshot and CLOB replay; real inference/network latency could move the book before an order arrives.
- Explicit per-market fees, gas/relayer costs, opportunity cost of locked collateral, and operational failures are not fully represented in the paper's CWR formula; net live profitability is therefore **unproven**.
- Conditional strategy labels such as `news_catalyst` are selected/emitted by the LLM within a common prompt and should not be treated as independently randomized strategy arms.

## Falsification

1. **Strict post-source OOS model freeze.** Data: new Polymarket snapshots collected only after 2026-02-21 with timestamp-locked news/CLOB state. Sample: at least 1,000 resolved markets across at least three calendar months, using a frozen model/version and frozen prompt per tranche. Metric: net CWR after all observed execution costs. **Research-defined falsification threshold:** reject the durable value-bet hypothesis for a model if net CWR `<= 0` or if a 95% event-clustered bootstrap interval includes a loss of `-2%` or worse. Action: do not promote that model-specific rule.

2. **Point-in-time leakage audit.** Data: original source snapshots, news publication timestamps, resolution-rule histories, and CLOB timestamps. Metric: fraction of prompt fields unavailable at formation time and change in CWR after purging leaks. **Research-defined falsification threshold:** if any future-resolving information is systematically present, or leakage-safe replay changes positive CWR to `<= 0`, classify the original trading interpretation as non-causal. Action: retain only the benchmark observation, not the alpha hypothesis.

3. **Market-price baseline / competing explanation.** Data: same OOS events. Baselines: executable market-implied probability, a no-news model, and a simple calibrated statistical forecast using only market price/order-book features. Metric: Brier score and net CWR difference. **Research-defined falsification threshold:** if the LLM does not improve Brier score and net CWR over the executable market-price baseline, reject incremental language-model alpha. Action: classify any apparent gain as market beta / pricing exposure rather than model information edge.

4. **Confidence ablation and calibration test.** Data: same model predictions. Compare confidence-sized CWR, equal-dollar sizing, and shuffled-confidence sizing. Metric: calibration error plus net return difference. **Research-defined falsification threshold:** if confidence-weighted sizing fails to beat equal-dollar sizing or shuffled confidence in at least two-thirds of OOS monthly blocks, reject confidence as an alpha-sizing variable. Action: separate forecasting skill from sizing claims.

5. **Threshold perturbation.** Data: frozen OOS predictions. Test confidence gates `0.55/0.60/0.65/0.70` without retuning the model. Metric: net CWR and trade count. **Research-defined falsification threshold:** if positive performance exists only at one isolated threshold and adjacent thresholds are non-positive, classify the rule as unstable. Action: reject threshold-specific promotion.

6. **Domain breakdown.** Data: OOS markets stratified by Politics, Macro/Economics, Sports, Crypto, and other sufficiently populated categories. Metric: category net CWR and calibration error. **Research-defined falsification threshold:** if aggregate profitability is driven by one category while a second major category loses more than `10%` CWR with high confidence, reject universal deployment and retain at most a domain-conditioned hypothesis. Action: require separate domain gates.

7. **Execution-latency and cost stress.** Data: tick/L2 CLOB replay with observed fees and inference-to-order latency. Stress additional delays of 1 s, 5 s, 30 s, and 60 s and realistic gas/relayer/fee schedules. Metric: net CWR and fill rate. **Research-defined falsification threshold:** if net CWR becomes `<= 0` at the measured real inference-plus-network delay or under the actual applicable fee schedule, reject tradeability. Action: keep as forecasting research only.

8. **Capacity stress.** Data: historical L2 depth. Test predeclared lots from $10 to $1,000 and participation caps. Metric: net CWR versus capital and realized average price impact. **Research-defined falsification threshold:** if positive expectancy disappears below `$100` base lot or before reaching a 1% share of available visible depth, classify the effect as economically capacity-limited. Action: do not generalize headline percentage returns to scalable capital.

9. **News placebo.** Data: same event/CLOB states. Replace contemporaneous news with timestamp-matched but event-mismatched news while preserving prompt length. Metric: OOS CWR and Brier score. **Research-defined falsification threshold:** if true-news performance does not exceed the 95th percentile of repeated placebo assignments, reject the news-information mechanism. Action: attribute any residual effect to market-state features or model priors instead.

## Crypto portability

`direct` for decentralized prediction-market contracts traded and settled through crypto infrastructure such as Polymarket; `unproven` for ordinary crypto spot/perpetual directional trading.

The source itself is a Polymarket study, so CLOB execution, tokenized binary claims, on-chain/relayer settlement, and crypto-native venue risks are direct. However, its strongest positive results occur in non-Crypto event categories such as Politics, while the Crypto category is a reported failure mode. Therefore this record must not be reinterpreted as evidence that an LLM can profitably forecast BTC/ETH spot or perpetual returns.

Crypto-specific implementation risks include venue/API rule changes, market-specific fees, Polygon/relayer availability, oracle/dispute resolution, USDC collateral exposure, fragmented liquidity, event-specific token structure, and 24/7 information arrival. A model/provider version can also change without a traditional software release, so point-in-time model identity is part of the data contract.

## Limitations

- **not independently reproduced**
- **short sample:** snapshot collection spans 2026-02-06 through 2026-02-12 only.
- **model/version dependence:** two of seven tested models are profitable and five are not.
- **domain dependence:** Crypto-category performance is a source-reported failure mode.
- **capacity limitation:** CWR degrades sharply as CLOB depth is consumed.
- **execution gap:** real inference/network latency is not identical to frozen-snapshot replay.
- **cost gap:** explicit fees, gas/relayer costs, collateral opportunity cost, and operational failures are not fully specified in CWR.
- **underspecified production inventory logic:** repeated signals, re-entry, cancellation, portfolio limits, and multi-market concentration are not a complete source-defined execution policy.
- **conditional-selection risk:** strategy-tag performance is observational within model outputs, not a randomized experiment proving that a named tag independently causes alpha.
- **annualization caution:** headline APY over a short, heterogeneous-duration event sample should not be treated as a durable expected return.
- **unproven post-publication persistence:** the paper does not establish performance after February 2026.

## Implementation status

No implementation has been completed in PyBroker, NautilusTrader, Paper, Testnet, or Live workflows.

`implementation_status: not-implemented`

This record documents research evidence and a falsification path only. It creates no implementation task and modifies no trading pipeline.

## Adoption boundary

`status: research-only`

`adoption: not-approved`

`approval_scope: research-only`

Presence in the Alpha Strategy Pool does not imply profitability, validated alpha, implementation approval, Paper approval, Testnet approval, or Live approval. The source benchmark's positive result for a specific February 2026 model/version is not authorization to use that model or to allocate capital.

## Related Wiki records

No Hermes Wiki Brain strategy record was modified or promoted in this Scout cycle.

Related Alpha Strategy Pool records used for mechanism-level deduplication/context include:

- `polymarket-binance-high-frequency-binary-lead-lag-2026-09-02.md` — Polymarket/Binance microsecond-to-second price-discovery lead-lag; materially different source, horizon, inputs, and negative OOS mechanism.
- `crypto-prediction-market-layered-informed-trading-skill-score-2026-09-01.md` — wallet/order-flow skill and informed-trader surveillance rather than model posterior/news value betting.
- `crypto-prediction-market-onchain-trade-misattribution-longshot-spread-2026-09-02.md` — prediction-market microstructure and spread phenomena rather than LLM forecasting.
- `prediction-market-structural-volatility-wright-fisher-glosten-milgrom-2026-09-02.md` — structural volatility/order-flow modeling rather than multimodal event forecasting.

No stable Hermes Wiki Brain link is asserted here beyond the canonical strategy-research specification read for this run.

## Sources

1. Pu Cheng, Juncheng Liu, and Yunshen Long, **“PolyBench: Benchmarking LLM Forecasting and Trading Capabilities on Live Prediction Market Data,”** arXiv:2604.14199v1 [q-fin.CP], submitted 2026-04-03. DOI: `10.48550/arXiv.2604.14199`. Stable abstract: https://arxiv.org/abs/2604.14199
2. Public full-text HTML for the same version, including Sections 4-6, Table 5, Table 6, and the position-sizing/slippage analysis: https://arxiv.org/html/2604.14199v1
