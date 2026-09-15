---
schema: strategy-research-record-v1
title: "ViperQ: Auction Market Theory State Representation for RL Trading via Balance/Imbalance Regime Detection"
created: 2026-09-15
updated: 2026-09-15
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - reinforcement-learning
  - microstructure
  - auction-market-theory
  - order-flow
status: research-only
confidence: medium
source_as_of: 2026-09-12
sources:
  - "Rares-Mihail Neagu and Jugal Kalita, 'ViperQ: Order Flow Pattern Recognition via Auction Market Theory for Reinforcement Learning Trading', arXiv:2609.13825v1 [cs.AI, q-fin.TR], submitted September 12, 2026. https://arxiv.org/abs/2609.13825"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# ViperQ: Auction Market Theory State Representation for RL Trading via Balance/Imbalance Regime Detection

## Provenance

- **Primary Source:** Rares-Mihail Neagu (affiliation not explicitly stated in paper) and Jugal Kalita (affiliation not explicitly stated in paper), *"ViperQ: Order Flow Pattern Recognition via Auction Market Theory for Reinforcement Trading"*, arXiv preprint `arXiv:2609.13825v1 [cs.AI, q-fin.TR]`, submitted September 12, 2026.
  - Abstract URL: https://arxiv.org/abs/2609.13825
  - Full-Text HTML: https://arxiv.org/html/2609.13825v1
  - Full-Text PDF: https://arxiv.org/pdf/2609.13825v1
  - Canonical DOI: [10.48550/arXiv.2609.13825](https://doi.org/10.48550/arXiv.2609.13825)

- **Verification Integrity:** The complete full-text HTML of `arXiv:2609.13825v1` was directly retrieved and inspected. All reported equations, state dimensions, reward function components, hyperparameters, performance figures, ablation observations, and limitations trace directly to Sections 3–8, Tables 1–5, and the reference list of the paper. No secondary summaries were used to formulate strategy mechanics or empirical claims.

- **Repository Deduplication Audit:** A comprehensive search of all `.md` records in `alpha-strategy-research` using ripgrep confirmed zero existing records matching `arXiv:2609.13825`, the paper title, Rares-Mihail Neagu, Jugal Kalita, or the ViperQ AMT state representation framework. Related records (`deep-rl-market-making-regime-switching-bocpd-scenario-bandit-2026-09-11.md`, `hawkes-order-flow-imbalance-self-excitation-microstructure-2026-09-12.md`, `adaptive-anchored-vwap-online-learning-audit-2026-09-12.md`) investigate different microstructure mechanisms (Bayesian change-point detection for market making, Hawkes self-excitation, VWAP tracking) and do not overlap with AMT-based RL state construction.

## Economic mechanism

### Source-reported

The source frames ViperQ as the first peer-reviewed RL trading system whose state representation is built explicitly from Steidlmayer–Dalton Auction Market Theory (AMT) primitives. AMT posits that intraday price discovery oscillates between two regimes: (1) *balance* states, where two-sided trade establishes consensus on fair value within a value area (mean-reverting); and (2) *imbalance* states, where one-sided aggression creates a liquidity vacuum and price moves to find a new value area (trending). The agent's core task is detecting the transition from balance to imbalance to enter directional positions at the onset of price discovery, and remaining flat during balance regimes. The state vector encodes VPOC (Volume Point of Control), Value Area position, Low Volume Node flags, Cumulative Volume Delta divergence, tape velocity, and order-flow imbalance as computational analogues of AMT constructs.

### Research interpretation

The hypothesized alpha mechanism is: AMT features provide a structured mid-frequency signal that captures the onset of directional price discovery by detecting the shift from mean-reverting balance to one-sided aggression in order flow. This is a microstructure-regime classification mechanism, not a price-prediction mechanism per se. The alpha source is the informational content of order-flow imbalance and volume distribution shape as leading indicators of directional moves, filtered through the AMT balance/imbalance framework. The 20-dimensional engineered state acts as an inductive prior that encodes three decades of practitioner microstructure pattern recognition into a format consumable by PPO.

Components:
- **Regime detection:** AMT balance vs. imbalance classification from volume distribution shape (VPOC, Value Area, LVN)
- **Flow aggression signal:** CVD slope, CVD divergence flag, tape velocity, order-flow imbalance ratio
- **Position memory:** Unrealized PnL, time-in-trade (dynamic state)
- **Price memory:** 9 lagged log-returns (no recurrence needed)

## Signal

### Formation timestamp

Observations are formed at 1-second resolution on institutional tick data. The state vector is recalculated every second. All execution is priced at the next bar's open to eliminate look-ahead bias.

### Lookback

- VWAP/VPOC window: 3600 seconds (1 hour rolling)
- Microstructure window (dist_to_wall, CVD divergence, trade_size_z): 300 seconds (5 min)
- CVD slope / tape velocity: 60 seconds (1 min)
- Lag depth: 9 steps (9 seconds of lagged log-returns)

### Long entry

The PPO agent selects action = BUY from a discrete action space {HOLD, BUY, SELL}. Entry occurs at next bar's open price. Position sizing uses volatility-adjusted sizing: shares = floor(conviction × equity / (ATR × share_price)), with a cash clamp preventing leverage. A 300-second minimum hold constraint is enforced during training. A synthetic transaction fee ($0.50/share) during training suppresses sub-tick scalping and forces the agent toward high-conviction setups.

### Short entry

Short positions are disabled (action space is {HOLD, BUY, SELL} only; SELL closes a long position).

### Exit

- **Volatility stop:** 2 × ATR from entry price (forced exit if breached)
- **Time decay:** After 3600 seconds in a position, a per-step penalty is applied
- **Drawdown shock:** Continuous per-step penalty when portfolio drawdown exceeds threshold; episode terminates at episode-limit drawdown
- **EOD flatten:** All positions flattened at 15:55 ET
- **Agent-driven:** The agent may also exit via SELL action based on learned policy

### Holding period

Minimum 300 seconds (5 minutes) during training. Maximum governed by time-decay penalty onset at 3600 seconds and EOD flatten at 15:55 ET. No explicit maximum hold is hard-coded beyond these mechanisms.

### Parameters

All numerical constants are classified by selection mechanism (Table 3 of paper):
- **VAL (validation-selected):** PnL scaling, synthetic fee ($0.50/share), hold gain branch, trend bonus, time-decay rate, stop-loss penalty, drawdown shock, lag depth
- **CONV (industry convention):** Trend threshold (5% of capital), time-decay onset (3600s), stop-loss threshold (2× ATR), drawdown threshold (prop daily-loss limit), EOD flatten (15:55 ET), VWAP/VPOC window (3600s), microstructure window (300s), CVD/velocity window (60s), min hold (300s), per-trade risk, ATR stop multiplier
- **TH (theory-derived):** Hold loss branch (Tversky–Kahneman loss-aversion coefficient λ ≈ 2.25)
- **LIT (library default):** PPO architecture (Stable-Baselines3 defaults)

### Position sizing

Volatility-adjusted: shares = floor(conviction × equity / (ATR_t × price)), clamped by available cash. Leverage is structurally impossible due to the cash clamp. Daily loss limit of a fraction of starting equity locks trading until next session.

### Underspecified items

- The exact value of the PnL scaling factor is validated on the validation slice but the precise numeric is not stated in the paper text (listed as VAL in Table 3).
- The exact conviction-to-dollar-risk mapping function is not fully specified.
- The NVDA-specific held-winner bonus value is validated but the precise numeric is not stated.

## Required data

- **Instrument:** US-listed equities (TSLA, NVDA); single-name, long-only
- **Universe:** Two highly volatile US large-cap equities. Generalisation to lower-volatility names, non-US markets, or other intraday regimes is untested.
- **Venue:** Institutional tick data from Databento (January 2020 – February 2026)
- **Timeframe:** 1-second OHLCV bars augmented with Delta (signed aggressive volume) and trade count; aggregated from nanosecond institutional ticks
- **Fields:** Open, High, Low, Close, Volume, Delta (aggressive buy volume minus aggressive sell volume), trade count
- **Point-in-time:** 80/20 chronological train/test split; final 12 months held out. No look-ahead in state construction.
- **Timestamp:** US Eastern Time; EOD flatten at 15:55 ET
- **Missing-data:** Not discussed in the source; assumed clean institutional-grade data with no gaps

## Execution assumptions

- **Signal-to-order timing:** Next-bar execution (action taken at second t, filled at second t+1 open)
- **Order type:** Market order (implied by next-bar-open execution model)
- **Fill model:** Deterministic next-bar open; no partial fills, no queue position modeling
- **Fees:** Regulatory fees of $0.00/share charged at evaluation time; synthetic training fee of $0.50/share active only during training. No commission or exchange fee modeling beyond regulatory fees.
- **Slippage:** Not modeled; next-bar open is used as fill price
- **Spread:** Not modeled
- **Impact:** Not modeled
- **Funding:** Not applicable (long-only, no leverage)
- **Leverage / margin:** Zero; cash clamp makes leverage structurally impossible
- **Borrow / shorting:** Not applicable (short positions disabled)
- **Latency:** 1-second resolution; no explicit latency modeling
- **Partial fills / failures:** Not modeled
- **Capacity:** Not assessed; high trade count (27,019 trades on TSLA over 12 months) suggests meaningful capacity constraints may exist

## Evidence

### Source-reported

All empirical figures trace directly to Neagu & Kalita (`arXiv:2609.13825v1`, Table 4, Section 6):

- **TSLA:** +163.6% ROI, -27.5% maximum drawdown, 27,019 trades, final balance $26,364.87 from $10,000 initial, zero leverage, regulatory fees included. Test period: 33.4M 1-second bars (held-out 12-month partition).
- **NVDA:** +116.5% ROI, -47.8% maximum drawdown, 12,892 trades, final balance $21,652.86 from $10,000 initial, zero leverage, regulatory fees included. Test period: 16.5M 1-second bars (held-out 12-month partition).
- **Sharpe-style metrics intentionally omitted** by the authors: at 1-second resolution, the standard annualisation factor amplifies microstructure noise rather than isolating signal, producing non-comparable values.
- **Behavioural divergence:** The same AMT state representation supports two distinct profitable policies (TSLA = high-frequency scalper; NVDA = trend-following risk-averse agent) based on reward-function configuration differences.

Ablation observations (Section 6.3, qualitative, not formal one-factor-at-a-time):
- Synthetic training fee is necessary to prevent degenerate sub-tick scalping policy
- Removing 300-second minimum hold causes TSLA policy to collapse into rapid scalping that fails to capture momentum
- Continuous drawdown shock is what differentiates the NVDA risk-averse policy

### Independently reproduced

Not independently reproduced. All empirical findings reflect direct extraction from Neagu & Kalita (`arXiv:2609.13825v1`, 2026).

### Negative evidence

None identified in the reviewed sources; absence is not evidence of no negative result. The authors explicitly acknowledge three limitations (Section 7):
1. Evaluation restricted to two highly volatile US equities over a single temporal split; generalisation untested.
2. No formal one-factor-at-a-time ablation of reward components or hyperparameter sensitivity sweep.
3. NVDA maximum drawdown (-47.8%) is materially higher than typical portfolio-rebalancing RL systems; ViperQ is not Pareto-superior to conservative portfolio systems and would be inappropriate for capital-preservation mandates.

## Falsification plan

1. **Cross-asset generalisation:** Apply the same 20-dimensional AMT state + PPO architecture to lower-volatility equities, non-US markets, and crypto perpetuals. If the AMT state representation fails to produce positive out-of-sample returns on assets with different microstructure dynamics, the generalisability of the AMT inductive prior is falsified `[research-defined falsification threshold]`.
2. **Cost sensitivity:** Re-run evaluation with realistic spread, slippage, and commission models (not just regulatory fees). If net-of-full-cost ROI is negative or MDD exceeds a threshold where the Sharpe is no longer positive, the alpha does not survive execution costs `[research-defined falsification threshold]`.
3. **Ablation of AMT features:** Replace the 20-dimensional AMT state with raw OHLCV features or standard technical indicators of equivalent dimensionality. If the raw-feature agent matches or exceeds AMT-agent performance, the AMT encoding provides no incremental value over simpler representations `[research-defined falsification threshold]`.
4. **Parameter perturbation:** Sweep VWAP/VPOC window, microstructure window, CVD window, and minimum hold constraints. If performance is highly sensitive to these practitioner-convention parameters (e.g., >50% ROI degradation on 20% perturbation), the robustness of the AMT prior is weakened.
5. **Out-of-sample temporal extension:** Extend the test period beyond 12 months or use walk-forward evaluation. If performance collapses outside the single held-out window, overfitting to the specific test regime is indicated.

## Crypto portability

**adapted**

The AMT balance/imbalance regime framework is highly relevant to crypto perpetual markets:
- Crypto perpetuals on major venues (Binance, Bybit, Hyperliquid) have continuous 24/7 order books with institutional-grade tick data, making 1-second or sub-second resolution feasible.
- CVD divergence, tape velocity, and order-flow imbalance are standard features in crypto microstructure analysis and are directly computable from trade tape data on crypto venues.
- The balance/imbalance distinction maps naturally to crypto intraday sessions: Asian/European/US session transitions often produce AMT-style regime shifts.

Crypto-specific portability risks:
- **Spread and slippage:** Crypto perpetual spreads are wider and more volatile than US equities; the paper's omission of spread/slippage modeling is more consequential in crypto.
- **Funding rate:** The long-only, zero-leverage design avoids funding costs; a crypto adaptation using perpetuals would need to account for funding rate exposure on held positions.
- **24/7 session structure:** The EOD flatten at 15:55 ET is equity-specific; crypto adaptation requires a different session structure or continuous operation.
- **Venue fragmentation:** Crypto order flow is fragmented across venues; AMT features computed on a single venue may not capture cross-venue dynamics.
- **Market manipulation:** Crypto markets are more susceptible to spoofing, wash trading, and layering, which could distort CVD and order-flow imbalance signals.
- **Liquidation cascades:** Crypto perpetuals have automatic liquidation mechanics not present in equities; the 2× ATR stop may be insufficient during cascading deleveraging events.

## Limitations

- **Two-asset evaluation:** Only TSLA and NVDA tested; both are highly volatile US large-caps. Generalisation is untested.
- **Single temporal split:** 80/20 chronological split with a single held-out 12-month window; no walk-forward or cross-validation.
- **No formal ablation:** Reward component ablation and hyperparameter sensitivity are reserved for future work; current evidence is qualitative.
- **High drawdowns:** NVDA -47.8% MDD is extreme; unsuitable for capital-preservation mandates.
- **Execution model optimistic:** Next-bar-open fill with no spread, slippage, or market impact; regulatory fees only.
- **Capacity not assessed:** 27,019 trades on TSLA over 12 months at 1-second resolution; capacity constraints at scale are unknown.
- **Not independently reproduced**
- **Data gap:** Author affiliations are not explicitly stated in the paper; submitter (Asser Moustafa) differs from listed authors (Neagu, Kalita).
- **Data gap:** PnL scaling factor and conviction-to-dollar-risk mapping exact values are not fully specified in the paper text.

## Implementation status

not-implemented. No implementation in our research stack (PyBroker, NautilusTrader, or paper trading) has been completed.

## Adoption boundary

This record captures theoretical and empirical research published in `arXiv:2609.13825v1`. Its presence in this repository does not constitute evidence of profitability, validated alpha, or authorization for deployment in paper trading, testnet, or live trading systems.

## Related Wiki records

- `[[quant/deep-rl-market-making-regime-switching-bocpd-scenario-bandit-2026-09-11]]` — Deep RL market making under regime-switching order flow; uses Bayesian change-point detection rather than AMT features for regime classification.
- `[[quant/hawkes-order-flow-imbalance-self-excitation-microstructure-2026-09-12]]` — Hawkes-process order flow imbalance; adjacent microstructure signal family but different mechanism.
- `[[quant/adaptive-anchored-vwap-online-learning-audit-2026-09-12]]` — VWAP-based signal; ViperQ uses VWAP as one component (VPOC) but the overall framework is fundamentally different.
- No directly related strategy research records share the same source identity or materially identical mechanism.

## Sources

1. Rares-Mihail Neagu and Jugal Kalita, *"ViperQ: Order Flow Pattern Recognition via Auction Market Theory for Reinforcement Learning Trading"*, arXiv preprint `arXiv:2609.13825v1 [cs.AI, q-fin.TR]`, submitted September 12, 2026.
   - Abstract URL: https://arxiv.org/abs/2609.13825
   - Full-Text HTML: https://arxiv.org/html/2609.13825v1
   - Full-Text PDF: https://arxiv.org/pdf/2609.13825v1
   - Canonical DOI: [10.48550/arXiv.2609.13825](https://doi.org/10.48550/arXiv.2609.13825)
