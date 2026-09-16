---
schema: strategy-research-record-v1
title: "Retail Proprietary-Trading Evaluation Gate Design: Stage-Dependent Incentives, Cadence Pincer, and Expected-Value Falsification"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - retail-prop-trading
  - gate-design
  - falsification
  - execution-frictions
  - first-passage
  - adverse-selection
status: research-only
confidence: high
source_as_of: 2026-09-14
sources:
  - "https://doi.org/10.48550/arXiv.2609.14859"
  - "https://arxiv.org/abs/2609.14859"
  - "https://arxiv.org/pdf/2609.14859v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Retail Proprietary-Trading Evaluation Gate Design: Stage-Dependent Incentives, Cadence Pincer, and Expected-Value Falsification

## Provenance

- **Source:** Working paper preprint, arXiv:2609.14859v1 [q-fin.TR, q-fin.GN], version 23 draft dated 13 September 2026, submitted 14 September 2026.
- **Title:** *Gate Design and Stage-Dependent Incentives in Retail Proprietary-Trading Evaluations: Why Passing Is Not Standalone Evidence of Skill, and Why the Product Fails to Pay Under Measured Trading Constraints*
- **Author:** Nicholas Hall (`nhall@cantab.net`)
- **Canonical DOI:** [10.48550/arXiv.2609.14859](https://doi.org/10.48550/arXiv.2609.14859)
- **Stable URLs:** Abstract: https://arxiv.org/abs/2609.14859; Full-Text PDF: https://arxiv.org/pdf/2609.14859v1
- **Primary Source Inspection:** The full 40-page manuscript, comprising 27 empirical tables, 2 figures, analytical first-passage derivations, apparatus run manifests, and external cohort filings, was directly retrieved and examined.
- **Empirical Apparatus Scope:** 1,928 activity-log events across 8 autonomous research agents, 7,630,539 model tokens, and 127 formal strategy investigations conducted between 2 July and 21 July 2026 against continuous front-month CME index futures data (consuming $113 of market data against a $250 cap, with execution locked to prevent realized trading bias).
- **Target Universe:** Retail proprietary trading evaluation contracts across CME Micro E-mini (MES) and full E-mini (ES) futures, alongside retail CFD/FX firms. Deep rule sweeps cover Lucid Trading, Tradeify, TopOne Futures, and Apex Trader Funding, calibrated against cohort disclosure data from Topstep, Take Profit Trader, MyFundedFutures, Earn2Trade, FPFX Technology, FTMO, and The Funded Trader.
- **Repository Deduplication Audit:** A comprehensive audit of all records in `alpha-strategy-research` confirmed zero existing records citing `arXiv:2609.14859`, Nicholas Hall, or the retail prop evaluation gate design and cadence pincer mechanism. Adjacent falsification records in the repository (`retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11.md`, `retail-signal-three-gate-falsification-oscillator-volume-calendar-trend-2026-09-04.md`, `trend-fib-extension-mechanical-pivot-null-edge-falsification-2026-09-14.md`, and `mnq-intraday-ohlcv-signals-gross-edge-ceiling-falsification-2026-09-05.md`) examine retail indicator signals, order-flow heuristics, and bar-level edge ceilings, but do not analyze multi-stage contract barrier geometries, first-passage ratchet penalties, or prop-firm evaluation gate incentives. This record constitutes an independent research capture.

## Economic mechanism

### Source-reported

Retail proprietary-trading firms sell a two-stage financial product:
1. **Stage 1 (The Evaluation):** A paid challenge where the participant must reach a nominal profit target $T$ before breaching a maximum drawdown barrier $d$, typically tracked via an end-of-day (EOD) or intraday trailing high-water mark.
2. **Stage 2 (The Funded Account):** A simulated or live-funded account requiring the participant to trade a minimum duration (e.g., 5 qualifying days), satisfy daily loss limits, and comply with consistency rules (e.g., capping any single day's profit at 20% to 40% of total cumulative profit) before any profit split or payout can be extracted.

The paper demonstrates that this contract geometry generates severe structural distortions and adverse selection:
- **Zero-Skill Manufacturability:** In a driftless random walk ($\mu = 0$), the theoretical continuous first-passage pass probability is $d / (d + T) = 0.40$ (for a 50K account with $d = \$2,000$ and $T = \$3,000$). Because end-of-day trailing drawdowns do not ratchet intraday, participants who maximize position variance can manufacture an empirical pass rate of 0.36 to 0.47 without possessing any directional predictive edge. Consequently, an evaluation pass rate confounds true skill with aggressive sizing.
- **The Stage-Dependent Cadence Pincer:** Under EOD trailing, higher trade frequency intraday does not compound drawdown risk within the session, speeding evaluation resolution from 11.4 days (at 1 trade/day) to 1.6 days (at 20 trades/day) while leaving pass probability essentially flat (23.4% to 25.4%). However, in the funded stage, higher frequency is catastrophic: because the account must survive a 5-day minimum window, trading 20 times per day introduces 100 independent opportunities to breach the trailing floor, collapsing the payout rate from 34.8% to 3.9% (a 9-fold destruction in extraction probability at identical strategy parameters).
- **The Trailing-Ratchet Penalty:** Dynamic ratcheting of the drawdown floor to the running equity peak consumes 14.0 to 16.6 percentage points of pass probability relative to an equivalent static fixed barrier.
- **Consistency Rule Asymmetry:** The consistency rule acts as a severe constraint on lumpy equity curves. While costless for low-cadence, steady returns, a 20% consistency cap roughly halves the funded-stage payout rate (collapsing from 34.8% to 17.4% at a 40% win rate) for the exact high-variance, lumpy configurations required to clear Stage 1.
- **Shrouded Pricing Model:** The seller's contribution margin is bounded by the gap between perceived and actual gate probabilities (the probabilistic analogue of shrouding price components). Sellers market permeable, achievable evaluation pass rates or cumulative gross payout totals while shrouding conditional payout probabilities, recurring reset fees, activation fees, and monthly platform costs.

### Research interpretation

This paper provides an empirical and mathematical falsification of two pervasive industry beliefs:
1. **Evaluation Passing as a Proxy for Skill:** Passing an evaluation challenge is not valid standalone evidence of quantitative alpha. Because the evaluation contract has positive option value to the buyer (downside capped at the entry fee, upside unbounded to $T$), variance-seeking noise traders pass at rates equal to or higher than genuine low-edge systematic strategies.
2. **Prop Firm Accounts as Synthetic Leverage:** Evaluation accounts fail as an economically viable synthetic leverage vehicle for systematic alpha deployment. The measured market cost floor (round-turn commission plus slippage of 1.12 points / $2.24 on MES and $13.80 base on ES) exceeds the best gross bar-level edges (+0.32 points). When combined with activation fees ($149–$189) and trailing drawdown friction, all 127 tested quantitative strategy configurations produced negative net expected value per account.

## Signal

The signal architecture analyzed in the paper operates across two domains: (1) the mathematical contract barrier model governing challenge survival, and (2) the underlying alpha strategies tested against the gates.

### 1. Mathematical Contract Barrier Model

- **First-Passage Probability (Proposition 3):** For arithmetic Brownian motion $dX_t = \mu dt + \sigma dW_t$ with drift $\mu > 0$ and volatility $\sigma$, the probability of touching a fixed barrier $d$ below the start is:
  $$P\left(\inf_{t \ge 0} X_t \le -d\right) = \exp\left(-\frac{2\mu d}{\sigma^2}\right), \quad d > 0$$
- **Driftless Continuous Benchmark:**
  $$P(\text{pass}) = \frac{d}{d + T}$$
  For standard tiers ($d = \$2,000, T = \$3,000$), $P(\text{pass}) = 0.400$.
- **Expected Value per Account Evaluation:**
  $$\text{EV} = (\pi \times \beta \times \text{Payout}) - \text{Cost}$$
  where $\pi$ is evaluation-stage pass probability, $\beta$ is consistency-adjusted funded payout probability, $\text{Payout}$ is extracted dollars capped at the firm's split and per-cycle ceiling, and $\text{Cost}$ is the total cost including initial fee, monthly subscriptions, reset fees, and activation fees.

### 2. Strategy Candidate Specifications Evaluated

- **Cycle I (Bar-Level Edge Search):** 1-minute OHLCV bars on front-month index futures. Tested index reconstitution drift, quarterly-roll settlement flow, options-dealer gamma hedging around large OI strikes, and fair-price open reversion.
  - Signal formation: Bar close; 1-minute to daily lookbacks.
  - Entry/exit: Mechanical threshold triggers (e.g., morning open displacement, gamma flip level).
  - Empirical outcome: Zero net-positive out-of-sample survivors over 2021–2026.
- **Cycle II (Fair-Price Open Reversion):** NY morning open displacement reversion (20-contract morning-only configuration). Initial apparent out-of-sample pass rate of 28.5% and EV of +$362/account collapsed to net-negative (-$0.08 to +0.22 gross points vs $2.24 cost floor) once EOD trailing and daily loss limits were accurately modeled.
- **Cycle III (Tape-Level Order Flow):** Tick-resolution liquidity sweeps and closing auction imbalances:
  - *Sweep / Liquidation Cascade Fade:* Fading aggressive market order runs through resting liquidity. In-sample: -$9.49/RT, Sharpe -0.222 ($n=1,786$). Out-of-sample: -$27.61/RT, Sharpe -0.646 ($n=6,236$). Primary finding: liquidation cascades continue 57% of the time rather than mean-reverting.
  - *Closing Auction Pressure:* Directional positioning into market-on-close imbalances. In-sample: +$16.91/RT, Sharpe +1.011, 57.1% win rate. Out-of-sample: -$171.30/RT, Sharpe -12.097, 16.7% win rate ($n=6$). Complete out-of-sample inversion.
- **Adversarial Benchmark (Prominent Practitioner Displacement-Candle Rule Set):**
  - Fully specified, zero-discretion mechanical rule set: displacement candle with minimum body ratio, fair value gap / liquidity sweep anchor, fixed stop, and 1:1.5 reward-to-risk target.
  - Grid: 324 in-sample configurations (2,832 sessions to September 2021), evaluated on 1,217 out-of-sample sessions to June 2026.
  - Empirical outcome: Out-of-sample win rate of 38.5% at 1:1.5 (where 40.0% is a coin flip). Out-passed by a driftless coin flip across every account (coin pass rate 20.50% vs strategy 15.25%; EV -$15.10 to -$152.63 per account).

## Required data

- **Instrument:** CME Micro E-mini S&P 500 (MES) and E-mini S&P 500 (ES) futures; continuous front-month contracts; matched cross-firm CFD/FX equivalents for external comparisons.
- **Venues:** CME Globex (central limit order book); firm-simulated broker feeds (Rithmic, Tradovate, CQG).
- **Timeframe:** Tick-level trade and quote data, 1-minute OHLCV bars, and daily session settlement bars.
- **Fields:** Timestamp (microsecond precision for ticks), open, high, low, close, volume, bid, ask, trade size, tick aggressor side (Lee-Ready classified), open interest, and contract rollover schedules.
- **Friction & Cost Parameters (Source-Measured):**
  - Micro contract (MES): 1.12 points ($2.24 per round turn) all-in friction (commission plus measured slippage).
  - Full-size contract (ES): $13.80 per round turn base estimate; $28.80 per round turn at the 90th percentile stress level.
  - Tick size and point value: MES = 0.25 pt ($1.25/tick); ES = 0.25 pt ($12.50/tick).
- **Firm Contract Rules & Fee Schedules (Sourced 10 July 2026 / 31 August 2026):**
  - *Lucid Trading (Flex 50K):* $98 evaluation fee, $0 activation fee, $2,000 EOD trailing drawdown, $3,000 profit target, no consistency rule, no daily loss limit.
  - *Tradeify (50K):* $87 evaluation fee, $0 activation fee, $2,000 EOD trailing drawdown, $3,000 profit target, 20% consistency cap, $1,250 daily loss limit.
  - *TopOne Futures (Elite Access 50K):* $39 evaluation fee, $189 activation fee (true direct cost to funded: $228), $2,000 trailing drawdown, $3,000 profit target, 40% consistency cap.
  - *Apex Trader Funding (50K):* $30 evaluation fee (discounted), $2,500 trailing drawdown, $3,000 profit target, $1,000 per-cycle payout cap on early disbursements.

## Execution assumptions

- **Execution Timing:** Signals evaluated on completed bar close or tick event; order transmission assumes 50ms exchange round-trip latency (`research-proposed` operational latency assumption; paper executes against historical tape with zero-latency simulator calibrated to independent commercial backtesting engines within 1.3% profit-factor tolerance).
- **Order Types & Fill Models:** Limit orders modeled with strict queue priority; stop-loss and market orders incur measured slippage (1 tick base on MES, 1–2 ticks on ES). Same-bar simultaneous stop and target hits are scored as stops (conservative execution model).
- **Margin & Position Caps:** Maximum position size strictly enforced per firm tier (e.g., max 5 contracts on 50K accounts); daily loss limits enforce hard immediate liquidation upon breach.
- **Account Holding Limits:** Sourced firms cap concurrent accounts per individual at 5 to 10 accounts, bounding horizontal strategy repetition.
- **Overnight Financing / Rollover:** All positions closed before session settlement (17:00 ET); zero overnight margin holding permitted.

## Evidence

### Source-reported

All figures, tables, and statistics cited below trace directly to Nicholas Hall (*Gate Design and Stage-Dependent Incentives in Retail Proprietary-Trading Evaluations*, arXiv:2609.14859v1, September 2026):

#### 1. Apparatus Throughput and Null Control (Table 1, Section 2.2–2.4)
- Total activity-log events: 1,928 across 8 autonomous agents.
- Total tokens consumed: 814,037 input / 6,816,502 output.
- Strategy investigations: 127 total; zero net-positive out-of-sample survivors after verified execution friction.
- Total market data expenditure: $113 consumed against $250 cap.

#### 2. Barrier Geometry Degradation Across Account Tiers (Table 2, Section 3.3)
- 25K tier: Profit target $T = \$1,500$, Max DD $d = \$1,000 \implies d/(d+T) = 0.400$.
- 50K tier: $T = \$3,000, d = \$2,000 \implies d/(d+T) = 0.400$.
- 100K tier: $T = \$6,000, d = \$3,000–\$3,500 \implies d/(d+T) = 0.333–0.368$.
- 150K tier: $T = \$9,000, d = \$4,000–\$5,000 \implies d/(d+T) = 0.308–0.357$.
- Finding: Contract geometry becomes monotonically more difficult as nominal account size increases.

#### 3. Funded-Stage Payout Rate by Consistency Regime (Table 3, Section 3.4)
Evaluation of funded-stage payout rate ($\beta$) at lumpy daily sizing across consistency regimes:
- At 40.0% win rate (driftless baseline at 1:1.5 reward:risk):
  - No consistency rule: $\beta = 34.8\%$
  - 40% consistency cap: $\beta = 34.8\%$ (does not bind at steady sizing)
  - 20% consistency cap: $\beta = 17.4\%$ (halves the extraction probability)
- At 44.0% win rate: No consistency = 46.8%; 40% cap = 46.8%; 20% cap = 28.6%.

#### 4. The Trailing-Ratchet Penalty (Table 5, Section 4.3)
Comparison of analytic fixed barrier pass probability vs simulated trailing peak ratchet:
- Cell ($\mu=\$5, \sigma=\$100, f=10$ trades/day): Fixed = 0.871 vs Trailing = 0.731 $\implies \mathbf{-14.0\text{ pp}}$ penalty.
- Cell ($\mu=\$10, \sigma=\$150, f=5$ trades/day): Fixed = 0.841 vs Trailing = 0.691 $\implies \mathbf{-15.0\text{ pp}}$ penalty.
- Cell ($\mu=\$2, \sigma=\$80, f=20$ trades/day): Fixed = 0.746 vs Trailing = 0.580 $\implies \mathbf{-16.6\text{ pp}}$ penalty.

#### 5. Skill Gradient vs Sizing Optimization (Table 7, Section 5.4)
Pass probability evaluated against per-trade skill $q = \mu/\sigma$:
- At zero skill ($q = 0.00$):
  - Fixed sizing ($\sigma = \$90$): $P(\text{pass}) = 0.000$ (at $f=1$), $0.101$ (at $f=5$), $0.263$ (at $f=20$).
  - Optimized sizing: $P(\text{pass}) = 0.370$ (at $f=1$), $\mathbf{0.434}$ (at $f=5$).
- At genuine skill ($q = 0.05$):
  - Fixed sizing ($\sigma = \$90$): $P(\text{pass}) = 0.394$ (at $f=5$).
- Core finding: Moving from fixed sizing to optimized sizing at **zero skill** increases pass rate by 33.3 percentage points (from 0.101 to 0.434), which exceeds the 29.3 percentage point gain from adding a genuine statistical edge ($q = 0.05$) at fixed sizing.

#### 6. Expected Calendar Time to Clear $3,000 Account (Table 8, Section 5.5)
- Under best gross bar-level edge ever measured ($\mu = \$1.74$ gross, $\sigma = \$60, f = 5$ trades/day): granting this edge **for free with zero transaction costs** yields $P(\text{pass}) = 0.063$, requiring **1,376 days ($\approx 5.5$ years)** of continuous trading per cleared account.
- At realistic net edges ($\mu = \$0.50, \sigma = \$40, f = 10$): $P(\text{pass}) = 0.028$, requiring 3,139 days ($\approx 12.5$ years).

#### 7. The Cadence Pincer: Stage-Dependent Asymmetry (Tables 10 & 11, Section 6)
- **Evaluation Stage (Table 10):** Under EOD trailing, pass rate is invariant to cadence (23.4% at 1 trade/day, 24.9% at 5 trades/day, 25.4% at 20 trades/day), while resolution time collapses from 11.4 days to 1.6 days.
- **Funded Stage (Table 11):** At 40% win rate, payout rate collapses monotonically with cadence:
  - 1 trade/day: $\beta = 34.8\%$
  - 5 trades/day: $\beta = 23.4\%$
  - 10 trades/day: $\beta = 11.7\%$
  - 20 trades/day: $\beta = \mathbf{3.9\%}$
- **Joint Gate:** Running 20 trades/day across both stages yields a joint pass-and-payout rate of 1.0%. Splitting cadence (fast in evaluation, slow in funded) yields 8.8%—a 9-fold divergence under identical strategy drift and volatility.

#### 8. Break-Even Win Rate by Account Structure (Tables 12 & 13, Section 7)
At a standard 1:1.5 reward-to-risk ratio (driftless baseline = 40.0%):
- Lucid Flex 50K: Break-even win rate = 40.9% (+0.9 pp required edge net of costs). Expected value at 40% win rate = -$10/account; at 42% = +$42; at 44% = +$106.
- Tradeify 50K: Break-even win rate = 40.5% (+0.5 pp required edge). EV at 40% win rate = -$43; at 42% = -$10; at 44% = +$38.
- TopOne Elite Access 50K: Break-even win rate = 43.6% (+3.6 pp required edge, driven by $189 activation fee). EV at 40% win rate = -$140; at 42% = -$88; at 44% = -$24.

#### 9. Tick-Level Order Flow Candidates in Cycle III (Table 17, Section 8.3)
- *Sweep / Liquidation Cascade Fade:*
  - In-sample ($n=1,786$): -$9.49/round-turn, Sharpe -0.222, 43.6% win rate.
  - Out-of-sample ($n=6,236$): -$27.61/round-turn, Sharpe -0.646, 42.3% win rate.
  - Verdict: Falsified; liquidation cascades continue through book depth 57% of the time.
- *Closing Auction Pressure:*
  - In-sample: +$16.91/round-turn, Sharpe +1.011, 57.1% win rate.
  - Out-of-sample ($n=6$): -$171.30/round-turn, Sharpe -12.097, 16.7% win rate.
  - Verdict: Severe in-sample overfitting; edge completely reverses out-of-sample.

#### 10. Adversarial Test of Published Retail Rule Set (Table 19, Section 8.5)
Out-of-sample test of prominent displacement-candle mechanical strategy vs zero-edge coin control:
- Displacement-candle rule set: Out-of-sample win rate 38.5% at 1:1.5 (negative drift).
  - Lucid Flex: Pass rate 15.25%, Payout rate 16.16%, EV = **-$24.06/account**.
  - Tradeify: Pass rate 15.25%, Payout rate 16.16%, EV = **-$15.10/account**.
  - TopOne: Pass rate 15.25%, Payout rate 16.16%, EV = **-$152.63/account**.
- Driftless Coin Flip Control: Win rate 40.0%.
  - Pass rate = **20.50%** (beats the strategy by +5.25 pp across all accounts).
  - EV = -$21.12 (Lucid), -$12.25 (Tradeify), -$149.64 (TopOne).
- Finding: A pure coin flip out-passes the published retail rule set because random walk paths do not carry the negative drag of transaction friction.

#### 11. External Sector Cohort Disclosures (Tables 20 & 21, Section 9)
- **Topstep Full-Year 2025 Cohort (Table 20):**
  - Evaluations initiated that completed: 16.8% (accounts).
  - Participants advancing to funded at least once: 51.8% (individuals, accounting for repeated resets).
  - Funded participants receiving a payout: 33.3% (individuals). Matches Hall's two-stage model estimate of 34.8% almost exactly.
  - Funded participants reaching a live capital account: **0.71%** (individuals). Over 99.2% of funded participants fail before live capital transition.
- **Cross-Sector Disclosure Funnel (Table 21):**
  - FPFX Technology (300,000+ accounts across 10 firms, 2024): 14% pass rate, 45% payout rate $\implies$ 7% of buyers paid.
  - Velotrade independent review (6 firms, 2026): 7% of buyers paid.
  - FTMO: 9–10% two-step pass rate.
  - Take Profit Trader: 20.4% pass rate (2023).
  - Earn2Trade: 10.4% pass rate (2024).

#### 12. Hedged-Pair / Delta-Neutral Cross-Account Falsification (Table 24, Section 12)
- Testing cross-account hedging (long account A, short account B, which firms explicitly ban as abuse):
- At observed firm payout ceilings ($1,000 per initial disbursement cycle), the hedged pair earns only +$9 per $196 committed on Lucid Flex, and **loses -$93** under a 20% consistency rule.
- Finding: The binding constraint on cross-account arbitrage is not the firm's anti-hedging surveillance, but the contractual payout ceiling, which caps extraction below the joint fee cost.

### Independently reproduced

`Not independently reproduced.` All figures, empirical metrics, simulation tables, and cohort disclosures represent third-party research findings reported by Nicholas Hall (arXiv:2609.14859v1, September 2026). No independent execution on live CME or simulated broker feeds has been conducted within our research stack.

### Negative evidence

- **Universal Strategy Attrition:** Across 127 investigated strategy candidates spanning 3 orchestrated cycles (bar-level momentum/reversal, session open reversion, and tick-level order flow), **zero** candidates maintained positive net expected value out of sample under real friction.
- **Execution Cost Floor Dominance:** Sourced round-turn friction of 1.12 points ($2.24) on MES exceeds the maximum gross bar-level edge (+0.32 points) ever measured in the programme, rendering intraday bar-level strategies structurally net-negative.
- **Liquidation Cascade Non-Reversion:** Taker liquidity sweep cascades continue in the direction of the cascade 57% of the time, directly falsifying the retail hypothesis that liquidity sweeps represent immediate mean-reverting absorption.
- **Negative Drift in Prominent Retail Rules:** The widely publicized displacement-candle mechanical setup posted an out-of-sample win rate of 38.5% at 1:1.5, performing worse than a random coin toss (40.0%) and resulting in negative expected value on every account type tested (-$15 to -$152/account).
- **Extreme Cohort Attrition:** Only 0.71% of individual participants at a major reporting futures firm ever reach live-capital funding status, confirming that prop evaluation accounts operate as high-margin lottery-style option underwriting rather than viable commercial funding channels.

## Falsification plan

To falsify the author's core thesis that retail prop evaluation challenges cannot be systematically exploited by algorithmic strategies, the following operational tests are specified:

1. **Gross-Edge Friction Survival Test:**
   - *Protocol:* Deploy an algorithmic intraday futures strategy on 1-minute MES/ES bars over a minimum of 250 out-of-sample trading sessions (post-June 2026).
   - *Control:* Deduct full-turn execution friction of 1.12 points ($2.24) on MES or $13.80 on ES.
   - *Falsification Criterion:* If any candidate demonstrates a statistically significant out-of-sample net Sharpe ratio $> 1.0$ ($t\text{-stat} > 2.5$) after deducting all-in fees and measured slippage, the author's cost-floor claim is falsified (`research-defined falsification threshold`).

2. **Zero-Edge Evaluation Pass Rate Test:**
   - *Protocol:* Execute 10,000 simulated random-walk paths ($\mu = 0, \sigma = \$300/\text{day}$) against an EOD trailing 50K account ($d = \$2,000, T = \$3,000$).
   - *Falsification Criterion:* If the empirical pass rate falls below 35.0% or fails to exceed the cohort baseline of 16.8%, the author's proof that pass rates are manufacturable at zero skill is falsified (`research-defined falsification threshold`).

3. **Stage-Cadence Inversion Verification:**
   - *Protocol:* Run identical strategy parameters ($\mu = \$3/\text{trade}, \sigma = \$90, 40\%\text{ win rate}$) across high cadence (20 trades/day) vs low cadence (1 trade/day) across both stages.
   - *Falsification Criterion:* If the high-cadence configuration achieves a funded payout rate $> 15.0\%$ (vs source-reported 3.9%), or if splitting cadence does not produce at least a 5x improvement in joint gate probability, the cadence pincer thesis is weakened (`research-defined falsification threshold`).

4. **Independent Re-Solve of Break-Even Win Rate:**
   - *Protocol:* Implement an independent Monte Carlo two-stage solver incorporating exact firm rules (Lucid Flex, Tradeify, TopOne) under Student-$t(3)$ returns and 1:1.5 reward:risk.
   - *Falsification Criterion:* If the break-even win rate on Lucid Flex drops below 40.2% or rises above 42.2%, the author's reported break-even corridor of 40.9%–41.5% is rejected (`research-defined falsification threshold`).

## Crypto portability

**Portability Classification:** `unproven` / `adapted`.

The primary source explicitly evaluates traditional CME index futures (MES, ES) and retail CFD/FX firms. Porting this gate-design analysis to crypto markets requires accounting for structural differences:

- **Crypto Proprietary Firms and Perpetual Funding:**
  - Several retail crypto prop firms (e.g., funded account challenges on Binance, Bybit, or decentralized perpetual protocols like Hyperliquid and dYdX) have emerged using identical 2-stage evaluation and trailing drawdown contracts.
  - In crypto perpetual contracts, the **funding rate** operates as an additional continuous carry tax or yield. For high-variance positions held across 8-hour funding timestamps, adverse funding rate payments accelerate trailing drawdown breaches, further increasing the ratchet penalty.
- **Liquidation Cascade Dynamics in Crypto:**
  - Hall documents that equity futures liquidation sweeps continue 57% of the time rather than mean-reverting.
  - In crypto perpetuals, where leverage is higher and liquidations are programmatic and visible via public websocket streams, cascade continuation is hypothesized to be even stronger due to auto-deleveraging (ADL) and cascading margin calls (`research-proposed` hypothesis).
- **Execution Frictions & Spread Volatility:**
  - Crypto exchange maker fees (0.01%–0.02%) and taker fees (0.04%–0.06%) on perpetual contracts represent a substantial friction floor. At $100,000 BTC, a 0.05% taker fee represents $50 per side ($100 round-turn per coin), which exacerbates the cost-cadence pincer for any high-frequency challenge-passing attempt.
- **Venue & Counterparty Risk:**
  - Unlike CFTC-regulated futures clearinghouses, crypto prop firms frequently operate unregulated synthetic execution venues where simulated slippage, spread widening during news events, and unilateral rule adjustments are common, further degrading the actual payout probability.

## Limitations

- **Preprint Status:** The source is a working paper preprint (version 23 draft, September 2026); while mathematically rigorous and accompanied by full apparatus manifests, it has not undergone formal academic peer review.
- **External Payout Rate Sample Size:** The empirical payout rate data rests on disclosures from a limited number of publishing firms (Topstep, Take Profit Trader, MyFundedFutures, FPFX Tech), as the majority of retail prop firms refuse to publish audited funnel statistics.
- **Firm Rule Instability:** Retail prop firm rule surfaces change frequently; promotions, reset pricing, and payout terms observed in July–August 2026 may be modified by operators in response to trader exploitation.
- **Focus on Futures and CFDs:** Strategy sweeps were conducted primarily on index futures and FX; direct empirical testing of crypto-native perpetual challenge accounts was not conducted by the author.
- **Non-Inclusion of Discretionary Edge:** The study evaluates systematic, fully specified mechanical strategies and statistical arbitrage; it does not rule out the possibility that rare discretionary traders possessing exceptional regime-reading ability might clear the gates, though cohort statistics (0.71% reaching live capital) confirm such participants are vanishingly rare.
- **Not Independently Reproduced:** All findings remain unverified by internal simulation within our research infrastructure.

## Implementation status

`not-implemented`.

No component of this research capture has been implemented in `nautilus-quant-system`, PyBroker, or NautilusTrader. This document serves as a theoretical and empirical falsification reference for evaluation-account claims, synthetic leverage viability, and retail indicator strategies.

## Adoption boundary

This record is research material only. Its presence in this repository does **not** constitute:
- Validation of any proprietary-trading challenge strategy.
- Approval for deploying capital or trading algorithms within retail prop firm accounts.
- Authorization for paper, testnet, or live execution.

In accordance with repository standards, all findings remain `research-only`, `not-implemented`, and `not-approved`.

## Related Wiki records

- `[[crypto-retail-systematic-trading-null-result-adversarial-audit-2026-09-01]]` — Forensic null-result audit of retail systematic strategies against fee/slippage walls.
- `[[mnq-intraday-ohlcv-signals-gross-edge-ceiling-falsification-2026-09-05]]` — Gross-edge ceiling falsification on CME Micro index futures.
- `[[retail-signal-three-gate-falsification-oscillator-volume-calendar-trend-2026-09-04]]` — Three-gate falsification of retail technical indicators.
- `[[retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11]]` — Microstructure and order-flow pattern falsification under retail constraints.
- `[[signal-to-executable-pnl-costs-2026-08-28]]` — Core canonical handoff contract analyzing the degradation of theoretical signals into executable PnL under realistic market frictions.
- `[[trend-fib-extension-mechanical-pivot-null-edge-falsification-2026-09-14]]` — Mechanical pivot null-edge falsification.

## Sources

1. **Nicholas Hall**, *"Gate Design and Stage-Dependent Incentives in Retail Proprietary-Trading Evaluations: Why Passing Is Not Standalone Evidence of Skill, and Why the Product Fails to Pay Under Measured Trading Constraints"*, Working paper — version 23 draft, 13 September 2026; arXiv preprint `arXiv:2609.14859v1 [q-fin.TR, q-fin.GN]`, submitted 14 September 2026.
   - Stable URL: https://arxiv.org/abs/2609.14859
   - PDF URL: https://arxiv.org/pdf/2609.14859v1
   - Canonical DOI: https://doi.org/10.48550/arXiv.2609.14859
2. **Topstep LLC**, *Risk Disclosure & Full-Year 2025 Performance / Cohort Statistics*, published 2026, retrieved 31 August 2026 (cited in Hall 2026, Table 20).
3. **FPFX Technologies & Finance Magnates**, *Proprietary Trading Sector Survey & Funnel Statistics*, 2024 (cited in Hall 2026, Table 21).
4. **David H. Bailey and Marcos López de Prado**, *"The Strategy Approval Decision: A Quantitative Approach to Setting Stop-Out Levels"*, *Journal of Risk*, 2013 (cited in Hall 2026 for first-passage drawdown stop-out analytics).
