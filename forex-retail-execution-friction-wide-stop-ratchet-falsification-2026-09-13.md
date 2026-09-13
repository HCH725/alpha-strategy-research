---
schema: strategy-research-record-v1
title: "Retail Forex Price Edges vs. Execution Friction: 16-Year Pre-Registered Walk-Forward Falsification of Wide-Stop Ratchet, Directional Scalping, and First-Passage Scale-In Grids"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - forex
  - retail-execution
  - transaction-costs
  - walk-forward
  - falsification
  - negative-results
  - oanda
  - ratchet-exit
  - slippage-decay
status: research-only
confidence: high
source_as_of: 2026-09-13
sources:
  - "Brock (BrockStar3540) & Claude Code, 'Mr. Scrooge V6: Open-source algorithmic forex trading bot for OANDA (Python) — cell-based execution, wide-stop ratchet exits, and full backtesting research program', GitHub repository 'BrockStar3540/mr-scrooge-v6', commit efbe634fa8249027adcee81cde5be4d958dfed37, accessed 2026-09-13. https://github.com/BrockStar3540/mr-scrooge-v6"
  - "Primary empirical paper (H6 walk-forward): Brock & Claude Code, 'H6, Tested: A Pre-Registered Walk-Forward Falsification of the Wide-Stop Thesis', docs/papers/PAPER_h6_walkforward_2026-07-16.md (commit efbe634fa8249027adcee81cde5be4d958dfed37). https://github.com/BrockStar3540/mr-scrooge-v6/blob/efbe634fa8249027adcee81cde5be4d958dfed37/docs/papers/PAPER_h6_walkforward_2026-07-16.md"
  - "Primary empirical paper (Edge hunt 5-family falsifications): Brock & Claude Code, 'Edge Hunt: Falsifying Five Price-Edge Families and the Wide-Stop Turn', docs/papers/PAPER_edge_hunt_falsifications_2026-07-14.md. https://github.com/BrockStar3540/mr-scrooge-v6/blob/efbe634fa8249027adcee81cde5be4d958dfed37/docs/papers/PAPER_edge_hunt_falsifications_2026-07-14.md"
  - "Primary empirical paper (Party Package scale-in): Brock & Claude Code, 'The Party Package: Scale-In Grids, First-Passage Fairness, and a Live Forward Test', docs/papers/PAPER_party_package_scale_in_2026-07-19.md. https://github.com/BrockStar3540/mr-scrooge-v6/blob/efbe634fa8249027adcee81cde5be4d958dfed37/docs/papers/PAPER_party_package_scale_in_2026-07-19.md"
  - "Primary empirical paper (Cost-aware exit classes): Brock & Claude Code, 'Cost-Aware Exit Classes: Brackets, Ratchets, and ATR Scaling', docs/papers/PAPER_cost_aware_exit_classes_2026-07-05.md. https://github.com/BrockStar3540/mr-scrooge-v6/blob/efbe634fa8249027adcee81cde5be4d958dfed37/docs/papers/PAPER_cost_aware_exit_classes_2026-07-05.md"
  - "Standing program research docket: docs/RESEARCH_PROGRAM.md"
  - "Autonomous gating and promotion engine: docs/GOVERNOR.md"
  - "Step-trail ratchet execution manager: modules/management/ratchet.py"
  - "Scale-in tranche execution module: modules/management/party_package.py"
  - "Cell setup and portfolio definitions: modules/cells/cell.py, modules/cells/portfolio.py, and config/cells/*.json"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Retail Forex Price Edges vs. Execution Friction: 16-Year Pre-Registered Walk-Forward Falsification of Wide-Stop Ratchet, Directional Scalping, and First-Passage Scale-In Grids

## Provenance

- **Repository:** `https://github.com/BrockStar3540/mr-scrooge-v6` (`source-reported`).
- **Authors / Research Lab:** Brock (`BrockStar3540`) & AI co-researchers Claude Code / Claude Fable 5 (`source-reported`).
- **Canonical Immutable Commit SHA:** `efbe634fa8249027adcee81cde5be4d958dfed37` (`source-reported`).
- **Commit Date:** 2026-09-13T00:15:21Z (`source-reported`).
- **Source As-Of Date:** 2026-09-13 (`source-reported`).
- **Primary Source Documents Directly Audited:**
  - `README.md`: Institutional program framing, five-family edge-hunt falsification overview, $10,000 challenge criteria, live cutover record, and the version freeze notice.
  - `docs/papers/PAPER_h6_walkforward_2026-07-16.md`: Decisive pre-registered walk-forward trial of the wide-stop thesis H6 (train 2019–2022, test 2023–2026), 0%-deviation engine reproduction test, per-pair/per-tier train selection table, main run metrics (Sharpe 0.03 vs 1.26 no-slip), flat-slippage sweep identifying the ~0.4 pips/trade knife-edge, and three consecutive addenda (stale-exit mechanism failure, red-rate denominator analysis, wider-engage t20 material positive).
  - `docs/papers/PAPER_edge_hunt_falsifications_2026-07-14.md`: Systematic falsification of five structurally distinct retail price-edge families across 8–16 years on OANDA majors: M5 scalping, single-pair daily trend, diversified retail time-series momentum (TSM), symmetric dual-ratchet straddles, and tight-stop-and-reverse (SAR) on lopsided cells.
  - `docs/papers/PAPER_party_package_scale_in_2026-07-19.md`: 10 simulation rounds testing adverse scale-in grids ("The Party Package"), proving the first-passage fairness property of FX majors across lock heights (greens supplied exactly balance greens needed to break even against kills), and demonstrating that re-arming popper grids act as structural fee machines.
  - `docs/RESEARCH_PROGRAM.md`: The program's standing falsification doctrine, 0/144 signed-direction finding, broker-truth hierarchy, and open/closed research dockets.
  - `docs/GOVERNOR.md`: Operational architecture of the autonomous evidence-gated Bar Governor.
  - `modules/management/ratchet.py` & `modules/management/party_package.py`: Concrete algorithmic implementations of the step-trail ratchet manager and scale-in tranche execution engine.
  - `modules/cells/cell.py` & `config/cells/*.json`: Production configuration schemas for per-pair session cells, setup conditions, and exit parameters.
- **Underlying Sample & Universe:** 16-year historical corpus (2010–2026) and 8-year granular M5/H1 leak-clean truth matrix across eight OANDA major and cross currency pairs: `EUR_USD`, `GBP_USD`, `USD_JPY`, `AUD_USD`, `USD_CAD`, `NZD_USD`, `USD_CHF`, `EUR_JPY` (`source-reported`). Complementary 47-instrument diversified CTA universe (FX, metals, index, energy, agriculture, rates) evaluated for time-series momentum (`source-reported`).
- **Venue & Broker Context:** OANDA Retail Forex Brokerage API (v20 REST/streaming) (`source-reported`).
- **Repository Deduplication Audit:** A comprehensive grep across all existing Markdown records in `alpha-strategy-research` confirmed zero prior records citing `BrockStar3540`, `mr-scrooge`, or commit `efbe634fa8249027adcee81cde5be4d958dfed37`. The repository currently holds zero records examining OANDA retail execution mechanics, the first-passage fairness theorem in retail currency pairs, or walk-forward falsification of wide-stop step-trail ratchets.

## Economic mechanism

### Source-reported

1. **The Retail Friction Ceiling (The "Toll at the Door" Law):**
   - The primary research program undertook a five-month empirical investigation to answer whether an automatable retail price-prediction edge exists net of execution friction on major currency pairs.
   - The authors established two foundational empirical baselines from 963 live broker fills on paper money:
     - Major currency pairs telegraph *when* and *how far* price moves occur, but provide zero net forecastability on *which direction* price will break (demonstrated by a 0/144 signed-direction test across diverse feature signatures).
     - Approximately 83% of the net drawdown suffered across strategy iterations was directly attributable to execution toll (spread, commission equivalents, and stop-out slippage).
   - On OANDA majors, average round-trip transaction costs span ~1.0 to 1.5 pips. At short intraday horizons (M5 bars, 1-hour holding period), transaction costs consume ~19% of the average asset move. This fraction declines to 3.6% at 1-day holding periods and 1.8% at 4-day holding periods. Because retail predictive models produce average gross trade edges of only +0.8 to +1.3 pips/trade, the gross edge is identically the same size as the transaction toll, rendering directional scalping structurally untradeable.

2. **The Wide-Stop Ratchet Hypothesis (H6) and Survivorship in Stop-Tuning:**
   - Early retail bot architectures employed tight stops (e.g., 5 to 15 pips) derived from "winners' Maximum Adverse Excursion (MAE) p75" rules. The authors uncovered that this standard practice is contaminated by severe survivorship bias: measuring adverse excursion exclusively on trades that survived to win guarantees that stops are tuned inside the noise envelope of the market, causing normal random oscillations to prematurely truncate winning positions.
   - Hypothesis H6 proposed widening initial stops to session-scale dimensions (40 to 60 pips, sized via session median range) while deploying an asymmetric step-trail ratchet exit (e.g., initial stop at −40p to −60p, ratchet trigger at +7.5p to lock +5p, followed by a trailing stop of 2.5p).
   - In preliminary in-sample simulations on a hand-selected 6-cell portfolio (2019–2026), the wide-stop mechanism flipped portfolio performance from account destruction under tight stops (Sharpe −3.54, −93%/yr CAGR) to apparent profitability (Sharpe +1.05, +25.4%/yr CAGR).
   - However, when subjected to pre-registered walk-forward validation (training 2019–2022, testing 2023–2026) with realistic execution slippage (0.8–1.2p round-trip), test-window Sharpe collapsed from +1.26 (frictionless) to **+0.03**, decisively failing the pre-registered Sharpe ≥ 0.70 pass bar.
   - The empirical root cause: while 95.8% of entries reach +7.5p before reaching −60p, the asymmetric penalty of rare wide stop-outs (−40p to −60p plus stop-out slippage) mathematically overwhelms the accumulated small ratchet wins (+6p to +8p net) once realistic execution friction is deducted.

3. **First-Passage Fairness Theorem in Retail Currency Markets:**
   - In subsequent testing of adverse scale-in grids ("The Party Package" / V6.1), the authors tested whether adding tranches every −10p to −15p of adverse excursion could capture oscillating tape ("waves") while riding wide stops.
   - Replay across 223,642 episodes on 2018–2026 leak-clean data revealed that major currency pairs exhibit **exact first-passage fairness**:
     $$\text{Greens Supplied per Kill} \approx \text{Greens Needed per Kill}$$
     Across lock-in triggers from 12.5p to 50p, the market balances the ratio of locked-in winners to catastrophic kill stop-outs to the exact decimal:
     - Trigger 12.5p: 4.7 greens supplied vs. 5.0 needed (kill rate 17.4%).
     - Trigger 20.0p: 3.0 greens supplied vs. 3.1 needed (kill rate 24.8%).
     - Trigger 25.0p: 2.4 greens supplied vs. 2.4 needed (kill rate 29.1%).
     - Trigger 30.0p: 2.0 greens supplied vs. 2.0 needed (kill rate 32.8%).
     - Trigger 40.0p: 1.5 greens supplied vs. 1.5 needed (kill rate 39.4%).
     - Trigger 50.0p: 1.3 greens supplied vs. 1.2 needed (kill rate 44.1%).
   - The authors concluded that retail currency markets are first-passage martingales with respect to barrier levels: gross harvest and execution costs rise proportionally, causing scale-in grids to act as structural fee machines (harvesting +100 to +150 pips gross while paying 130 to 190 pips in spread and slippage).

4. **The Wider-Engage Geometry Discovery (Trigger 20):**
   - Through systematic joint grid exploration over the frozen walk-forward books, the authors identified a singular structural configuration that cleared blind out-of-sample testing: widening the ratchet engagement trigger from 7.5p to **20.0p** (lock at +17.5p, trail 2.5p, holding initial stops at 40–60p).
   - By demanding substantially greater directional confirmation before arming the ratchet, average winning trade size increased from +8.08p to +21.97p, achieving a test net Sharpe of **+0.566** (+0.40p mean net per trade) with zero overfit gap (+0.489 train $\to$ +0.566 test) across a stable 0.49–0.57 parameter plateau.

### Research interpretation

- The empirical results from the *Mr. Scrooge* research program constitute a rigorous textbook falsification of retail technical trading heuristics. The fundamental flaw across retail strategy engineering is the failure to model execution friction as an endogenous structural barrier rather than a minor post-hoc deduction.
- When an asset's price dynamics approximate a martingalian random walk with zero gross directional drift at intraday scales, any asymmetric exit rule (such as stop-loss vs. take-profit or ratchet trailing) simply samples from the distribution of first-passage times. Under Dynkin's lemma and optional stopping for continuous martingales, the expected gross payoff of any bounded exit boundary is identically zero.
- Consequently, the net expected return is governed strictly by the execution toll:
  $$\mathbb{E}[R_{\text{net}}] = -\left(\text{Spread} + \text{Slippage}_{\text{entry}} + \text{Slippage}_{\text{exit}}\right) < 0$$
- Strategies attempting to bypass this constraint via wider stops merely trade high win rate for catastrophic negative tail risk. The only way an exit rule can generate genuine positive expectation is if the underlying price process possesses non-zero structural drift (such as macro carry, structural funding asymmetry, or institutional flow imbalance) that exceeds the venue's effective bid-ask wedge.

## Signal

### Pre-Registered Walk-Forward Architecture (H6 Wide-Stop System)

1. **Formation Timestamp & Scheduling:**
   - Evaluated on 5-minute (M5) and 1-hour (H1) bar closes across three distinct trading sessions:
     - Asia Session: 00:00 to 08:00 UTC (`source-reported`).
     - London Session: 08:00 to 13:00 UTC (`source-reported`).
     - New York Session: 13:00 to 21:00 UTC (`source-reported`).
   - Signal evaluation occurs at bar close; trades enter at market on the open of the subsequent bar (`source-reported`).
   - Rollover blackout: between 20:45 and 21:15 UTC, all order entry is prohibited due to institutional spread blowout (spreads expand 4× to 10× at 21:00 UTC rollover) (`source-reported`). Any resting stop located within 10.0 pips of market price is flattened at market prior to 20:55 UTC (`source-reported`).

2. **Session Cell Candidate Universe:**
   - The strategy space is partitioned into 29 discrete "cells" combining a currency pair, a session, and a structural entry condition (`source-reported`).
   - Exemplar setup specifications audited in `config/cells/*.json`:
     - `USD_JPY / london / timing_lean_30`: Long entry when price exhibits structural lean above session VWAP with volatility compression (`source-reported`).
     - `AUD_JPY / ny / regime_short_240`: Short entry on 4-hour trend-exhaustion breakdown with negative momentum (`source-reported`).
     - `EUR_JPY / asia / box_pdl_short`: Short entry on breakdown of previous day low (PDL) during Asian consolidation (`source-reported`).
     - `USD_JPY / asia / kc_breakout_long_t20s`: Long entry when price crosses above upper Keltner Channel band (`kc_up_dist_pips >= 0`), conditioned on relative hourly ATR (`atr_h1_relative <= 1.05`) and clearance from previous day low (`pdl_dist >= 63.0` pips) (`source-reported`).

3. **Range-Sized Stop Loss Assignment Rule (`range_sized_sl`):**
   - Measured strictly on the in-sample training window (2019–2022) using session median trading range (`source-reported`):
     $$\text{Initial Stop (SL)} = \begin{cases} 40.0 \text{ pips}, & \text{if Session Median Range} < 35.0 \text{ pips} \\ 50.0 \text{ pips}, & \text{if } 35.0 \le \text{Session Median Range} < 48.0 \text{ pips} \\ 60.0 \text{ pips}, & \text{if Session Median Range} \ge 48.0 \text{ pips} \end{cases} \quad (\text{source-reported})$$

4. **Exit Mechanics & Step-Trail Ratchet Gear:**
   - **Baseline Ratchet (t7.5):**
     - Initial hard server-side stop placed at `SL` pips from entry (`source-reported`).
     - Evaluated every 30 seconds (`step_cadence_min = 0.5`) (`source-reported`).
     - Engagement trigger: `step_trigger_pips = 7.5` pips of peak favorable excursion (`source-reported`).
     - Lock-in level: on reaching trigger, stop loss is immediately moved to `+5.0` pips (`source-reported`).
     - Trailing rule: as price advances beyond trigger, stop trails peak price by `step_trail_pips = 2.5` pips in discrete steps of `step_size_pips = 2.5` pips (`source-reported`).
     - Stop only moves forward, never backward (`source-reported`).
     - Maximum holding period horizon: 12 hours force-close at market if neither stop nor trailing stop has triggered (`source-reported`).
   - **Wider-Engage Variant (t20, Discovered in Addendum 3):**
     - Initial hard server-side stop at `SL` pips (40–60p) (`source-reported`).
     - Engagement trigger: `step_trigger_pips = 20.0` pips (`source-reported`).
     - Lock-in level: moved to `+17.5` pips (`source-reported`).
     - Trailing distance: `step_trail_pips = 2.5` pips (`source-reported`).
     - Horizon exit: extended to 5 days (120 hours) for slow-moving trends (`source-reported`).

5. **Scale-In Re-Arming Grid Mechanics ("The Party Package"):**
   - Primary parent position enters on cell signal (`source-reported`).
   - Tranche ("popper") additions: every additional −15.0 pips of adverse movement from parent entry, an independent tranche is placed at market (`source-reported`).
   - Tranche sizing: 10% of equity per tranche (`source-reported`).
   - Maximum active tranches: capped at 8 concurrent positions (~80% total margin exposure) (`source-reported`).
   - Tranche exit gear: independent server-side stop at 60.0 pips from fill, with independent ratchet trigger at +8.5p $\to$ lock +6.0p $\to$ trail 2.5p (`source-reported`).
   - Re-arming rule: if a popper locks green and exits, the price level re-arms once market price re-crosses the −15p marker (`source-reported`).

## Required data

- **Instruments & Universe:**
  - Primary universe: Eight OANDA major and cross currency pairs: `EUR_USD`, `GBP_USD`, `USD_JPY`, `AUD_USD`, `USD_CAD`, `NZD_USD`, `USD_CHF`, `EUR_JPY` (`source-reported`).
  - Secondary CTA universe: 47 continuous futures/CFD instruments across 6 asset sectors (FX majors, precious/base metals, equity indices, energy, agricultural commodities, sovereign rates) (`source-reported`).
- **Venue:** OANDA Corporation (Retail FX Brokerage / CFD platform) (`source-reported`).
- **Timeframe & Resolution:** 5-minute (M5), 1-hour (H1), and daily (D) OHLCV bars (`source-reported`).
- **Data Fields Required:**
  - Open, High, Low, Close, Tick Volume (`source-reported`).
  - Bid/Ask quote streams for real-time spread calculation (`source-reported`).
  - Previous Day High (PDH), Previous Day Low (PDL), 20-period Keltner Channels (KC), 14-period Average True Range (ATR M5 and H1) (`source-reported`).
  - Session boundaries: UTC timestamps matching Asia, London, and New York official trading hours (`source-reported`).
- **Point-in-Time Integrity:**
  - Evaluated on the `v5-truth-matrix.tar.gz` leak-clean corpus (`source-reported`).
  - All feature transforms strictly enforce trailing-window boundaries; zero future bars or daily look-ahead permitted (`source-reported`).
  - Target labels rebuilt post-Bug-B-078 to ensure complete isolation of formation timestamps from execution bars (`source-reported`).

## Execution assumptions

- **Order Types & Routing:**
  - Entry orders: Market orders executed at the open price of the bar immediately following signal qualification (`source-reported`).
  - Initial Stop-Loss orders: Hard resting server-side stop orders placed natively at the broker (`OANDA API`) upon order fill confirmation (`source-reported`).
  - Ratchet modifications: Dynamic trailing updates transmitted via API order update requests upon cadence check (`source-reported`).
- **Spread Model:**
  - Exact historical bid-ask spread charged once per round trip (`buy-ask / sell-bid`) on every trade (`source-reported`).
  - Historical OANDA majors spread averages:
    - `EUR_USD`: ~1.0 pip (`source-reported`).
    - `USD_JPY`: ~1.1 pips (`source-reported`).
    - `GBP_USD`: ~1.4 pips (`source-reported`).
    - `AUD_USD`: ~1.2 pips (`source-reported`).
    - `EUR_JPY`: ~1.5 pips (`source-reported`).
- **Slippage Model (Pre-Registered Tiered Specification):**
  - In the decisive walk-forward trial, slippage is applied deterministically to both training selection and out-of-sample testing (`source-reported`):
    - Entry slippage: `0.4` pips charged on every market entry (`source-reported`).
    - Exit slippage on normal trailing/horizon exits: `0.4` pips (`source-reported`).
    - Stop-out exit slippage scaled by stop-loss tier (modeling fast market breakouts during adverse moves) (`source-reported`):
      $$\text{Stop-Out Slippage} = \begin{cases} 0.4 \text{ pips}, & \text{for SL40} \\ 0.6 \text{ pips}, & \text{for SL50} \\ 0.8 \text{ pips}, & \text{for SL60} \end{cases} \quad (\text{source-reported})$$
    - Total round-trip slippage penalty: ~0.8 pips (calm exit) to ~1.2 pips (loud stop-out), paid *in addition* to the full bid-ask spread (`source-reported`).
- **Portfolio Sizing & Constraints:**
  - Risk-normalized position sizing: fixed at 1.0% equity risk per trade, where position size scales inversely with initial stop distance ($w \propto 1 / \text{SL}$) (`source-reported`).
  - Concurrent position cap: strictly limited to 3 concurrent active trades across the portfolio (`source-reported`).
  - Account compounding: real equity compounding recomputed daily (`source-reported`).
  - Margin & leverage: retail leverage capped at 30:1 (major pairs) / 20:1 (minor pairs) per regulatory guidelines (`research-proposed`).

## Evidence

### Source-reported

#### 1. Pre-Registered Decisive Walk-Forward Trial (H6 Wide-Stop System)

The formal walk-forward evaluation protocol was frozen prior to execution:
- **Training Window:** 2019-01-01 to 2022-12-31 (4.0 years) (`source-reported`).
- **Test Window:** 2023-01-01 to 2026-07-03 (3.5 years; 7,582 trades evaluated) (`source-reported`).
- **Pre-Registered Acceptance Thresholds:**
  - Net test-window Sharpe $\ge 0.70$: hypothesis confirmed research-grade (`source-reported`).
  - Net test-window Sharpe $0.30 \le \text{SR} < 0.70$: hypothesis weakened (`source-reported`).
  - Net test-window Sharpe $< 0.30$: **hypothesis falsified** (`source-reported`).

##### Train Selection Stage (2019–2022)
From 29 initial cell candidates across the 8-pair universe, only **3 cells** passed the train-only filter (`train net expectancy > 0.0` and $n \ge 40$ under spread + slippage) (`source-reported`):
1. `AUD_JPY / ny / regime_short_240`: Short side, SL50, $n_{\text{train}} = 1,298$, train net expectancy = $+0.321$ pips (`source-reported`).
2. `USD_JPY / london / timing_lean_30`: Long side, SL40, $n_{\text{train}} = 2,055$, train net expectancy = $+0.278$ pips (`source-reported`).
3. `EUR_JPY / asia / box_pdl_short`: Short side, SL50, $n_{\text{train}} = 4,586$, train net expectancy = $+0.089$ pips (`source-reported`).
The remaining 26 candidate cells exhibited negative net train expectancies ranging from −0.06 to −1.92 pips, confirming that under realistic costs the candidate universe was already heavily unprofitable (`source-reported`).

##### Out-of-Sample Test Window Results (2023–2026)
Across 7,582 executed test trades, the frozen 3-cell book delivered the following performance metrics (`source-reported`):

| Metric | Pre-Registered Pass Bar | Test Result (+ Slippage) | Twin Baseline (No Slippage) |
|---|---|---|---|
| **Annualized Sharpe Ratio** | $\ge \mathbf{0.70}$ | **+0.03** (**FALSIFIED**) | **+1.26** |
| **Annualized CAGR** | $> 0.0\%$ | **−2.1%** | **+32.1%** |
| **Maximum Drawdown** | $< 25.0\%$ | **−50.9%** | **−25.3%** |
| **Calmar Ratio** | $> 0.50$ | **−0.04** | **+1.27** |
| **Total Test Trades ($n$)** | $\ge 1,000$ | **7,582** | **7,582** |
| **Win Rate (% Green)** | — | **84.5%** | **84.5%** |
| **Average Win (Green)** | — | **+8.08 pips** | **+8.88 pips** |
| **Average Loss (Red)** | — | **−45.46 pips** | **−44.66 pips** |
| **Per-Year Returns (23/24/25/26)** | Consistent | **+18% / +20% / −33% / −6%** | **+88% / +88% / +7% / +7%** |

#### 2. The Slippage Sensitivity Knife-Edge Sweep

To locate the exact threshold where the strategy breaks down, the authors conducted a flat per-trade round-trip slippage sweep on the registered 3-cell book across the 2023–2026 test window (`source-reported`):

| Round-Trip Slippage (pips/trade) | Test Sharpe Ratio | Test CAGR (%) | Final Equity Multiple | Interpretation / Status |
|---:|---:|---:|---:|---|
| **0.0 pips** | **1.26** | **+32.1%** | **4.10×** | Frictionless theoretical ceiling |
| **0.2 pips** | **0.98** | **+23.2%** | **2.88×** | Institutional / prime execution quality |
| **0.4 pips** | **0.70** | **+15.0%** | **2.03×** | **Pass Bar Knife-Edge ($\text{SR} = 0.70$)** |
| **0.6 pips** | **0.41** | **+7.3%** | **1.43×** | Weakened region |
| **0.8 pips** | **0.12** | **+0.1%** | **1.00×** | **Net Break-Even Line** |
| **1.0 pips** | **−0.16** | **−6.6%** | **0.71×** | Typical retail stop-fill reality |
| **1.2 pips** | **−0.45** | **−12.9%** | **0.50×** | Stressed retail rollover/news execution |

The empirical findings prove that the strategy clears the research pass bar only if total round-trip slippage is $\le 0.4$ pips (0.2 pips per fill). Because empirical retail stop fills on OANDA exhibit a median of ~0p during calm markets but reach 0.8p at the 90th percentile (and several pips during news/rollover), realistic retail execution lands between 0.8p and 1.0p round-trip, where the strategy is dead.

#### 3. Summary of the Five Preceding Price-Edge Falsifications

Prior to testing H6, the authors conducted full-sample leak-clean evaluations across five standard retail trading paradigms (`source-reported`):
1. **M5 Directional Scalping:** Gross trade edge (+0.8 to +1.3 pips) matches round-trip transaction costs (~1.0 to 1.5 pips). Net Sharpe is zero or negative across 131 live broker round trips (`source-reported`).
2. **Single-Pair Daily Trend Following:** Over 7.5 years across 8 currency majors, forward return conditional on 1-day SMA trend alignment produced hit rates pinned at 49.0%–50.0%. Across 32 distinct technical regime gates (ADX, Chop index, Hurst exponent, VHF), zero filters achieved year-by-year consistency; the textbook trend-persistence regime (ADX-high + Hurst-high) was positive in 0 out of 6 test years (`source-reported`).
3. **Diversified Retail Time-Series Momentum (TSM):** Canonical volatility-targeted ensemble across 47 instruments over 16 years (2010–2026): gross Sharpe was +0.08, collapsing to net Sharpe **−0.22** after CFD retail spread and daily turnover costs. The authors observed that retail CFD accounts lack the cross-asset breadth (100–300 futures) required for CTA diversification benefits (`source-reported`).
4. **Symmetric Dual-Ratchet Straddle:** Entering simultaneous long and short positions on 8 currency pairs over 16 years with ratchet gear: net expectancy was −0.9 to −2.6 pips per straddle, positive in 0 out of 8 test years. Because a 50/50 pair guarantees that the losing leg hits its stop, the winning leg must capture $> \text{Stop} + 2 \times \text{Spread}$ (~14.5 pips) every time, which trailing ratchets systematically failed to achieve (`source-reported`).
5. **Tight-Stop-and-Reverse (SAR) on "Lopsided" Cells:** Entering favorable out-of-sample sides with tight stops (5 pips) and reversing on stop: net expectancy was −1.56 pips generic and −1.74 pips at structural levels (0 out of 24 cells net positive). Crucially, the training asymmetry metric `asym_train = 0.0` was identically zero across all cells, demonstrating that perceived historical cell asymmetry was merely realized direction rather than an exploitable stationary property (`source-reported`).

#### 4. The First-Passage Fairness Theorem in Scale-In Grids

In ten simulation rounds evaluating the "Party Package" re-arming scale-in grid across 223,642 episodes (2018–2026), the authors discovered that major currency pairs price the race between locked greens and stop kills to exact martingale fairness (`source-reported`):
- Across triggers from 12.5p to 50p, greens supplied per kill matched greens needed to break even to within $\pm 0.1$ pips (`source-reported`).
- Re-arming grids generated 44.6 green poppers per signal averaging +8.9 pips net (+395 pips banked), but suffered 7.28 stop kills averaging −57.2 pips (−416 pips lost), producing an overall net loss of −21.6 pips per signal (`source-reported`).
- Across grid step spacings (−10p, −15p, −20p, −30p), net performance declined monotonically toward zero: the grid harvested ~+100 to +150 pips gross while paying ~130 to 190 pips in spread and slippage, operating purely as a commission/spread churner (`source-reported`).

#### 5. The Lone Material Positive: The Wider-Engage (t20) Discovery

In Addendum 3, the authors evaluated a joint grid varying stop-loss width (40 to 120 pips) and ratchet engagement triggers (7.5 to 20 pips) (`source-reported`):
- Widening stops from 40 to 120 pips failed to rescue the strategy: pre-engage stop-out rate fell only 2.9× (from 14.8% to 5.1%), keeping the stop-out rate above the break-even threshold (`source-reported`).
- Widening the trigger from 7.5p to **20.0p** (with initial stops held at 40–60p, lock at +17.5p, trail 2.5p) achieved:
  - Blind test net Sharpe: **+0.566** (risk-normalized) and **+0.558** (fixed-size) (`source-reported`).
  - Mean net return per trade: **+0.40 pips** (`source-reported`).
  - Average winning trade: increased from +8.08p to **+21.97 pips** (`source-reported`).
  - Win rate: dropped from 84.5% to **68.4%** (red rate 31.6%) (`source-reported`).
  - Train-to-test overfit gap: $+0.489 \to +0.566$ (out-of-sample test was superior to in-sample training) (`source-reported`).
  - Status: Classified as **Material ($\text{SR} \ge 0.30$) but not a full revival ($\text{SR} < 0.70$)**; retained on shadow tape without live capital allocation (`source-reported`).

### Independently reproduced

Not independently reproduced. All empirical findings, parameter sensitivities, trade counts, and statistical tables reflect primary-source code execution and audited documentation from GitHub repository `BrockStar3540/mr-scrooge-v6` at commit `efbe634fa8249027adcee81cde5be4d958dfed37`.

### Negative evidence

- **Structural Slippage Asymmetry:** Stop-market orders placed at the broker during adverse volatility spikes experience asymmetric positive slippage penalty (fills occur worse than the stop price), whereas trailing take-profit limit fills cannot compensate for this deficit.
- **Regime Fragility & Performance Decay:** Even in the absence of slippage, the strategy exhibited substantial temporal decay: annual returns fell from +88% in 2023 and 2024 to +7% in 2025 and 2026, indicating macro volatility compression or structural regime shift in G10 currency markets.
- **Survivorship in Heuristic Stop-Loss Sizing:** Standard retail methodologies that calibrate stop-loss thresholds using the Maximum Adverse Excursion (MAE) of winning historical trades inherently select for surviving paths, creating an illusion of precision that collapses upon out-of-sample forward execution.
- **Martingale First-Passage Invariance:** Attempting to engineer pseudo-alpha through complex trade management (such as scale-in grids, martingale tranche additions, or breakeven ratchets) does not alter the fundamental expected value of a martingalian price process; it merely redistributes outcome variance into catastrophic negative tail events while multiplying transaction costs.

## Falsification plan

To further evaluate or disconfirm the empirical conclusions of the *Mr. Scrooge* research program across other venues or asset classes, the following falsification protocol is defined:

1. **Broker-Truth Realized Slippage Audit:**
   - *Test:* Deploy a non-directional synthetic order harness executing simultaneous paired buy/sell orders at random intervals on live broker infrastructure.
   - *Metric:* Measure realized fill price minus mid-quote at order submission timestamp ($S_{\text{realized}}$) across market regimes.
   - *Research-defined falsification threshold:* If mean round-trip execution slippage on retail majors is demonstrated to be $\le 0.30$ pips across $\ge 500$ live fills, the central thesis that retail execution friction exceeds gross strategy edge is falsified for that specific broker.

2. **First-Passage Barrier Ratio Invariance Test:**
   - *Test:* For any target market, construct a continuous grid of barrier pairs $(+B_{\text{win}}, -B_{\text{loss}})$ and compute the empirical passage probability $P(+B_{\text{win}} \text{ before } -B_{\text{loss}})$.
   - *Research-defined falsification threshold:* If the empirical ratio of wins to losses deviates from the theoretical martingale odds by $> 3.0$ standard errors under Newey-West HAC correction, the assumption of first-passage fairness is rejected, indicating the presence of exploitable local price drift.

3. **Wider-Engage Ratchet Out-of-Sample Holdout:**
   - *Test:* Evaluate the t20 wider-engage configuration (trigger 20.0p, lock 17.5p, trail 2.5p, stop 40–60p) across an uninspected historical sample (2010–2018) or forward 2026–2027 live paper tape.
   - *Research-defined falsification threshold:* If the out-of-sample net Sharpe drops below 0.30 or the average trade net expectancy falls below 0.0 pips over $\ge 1,000$ trades, the wider-engage edge is confirmed to be an artifact of multi-grid selection and is classified as permanently rejected.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven` (`research-proposed`).
- **Transferability Assessment:** The primary research investigated G10 currency spot/CFD contracts on OANDA; the findings have not been demonstrated in cryptocurrency perpetual or spot markets by the primary author. Porting to cryptocurrency assets represents a research hypothesis subject to substantial structural differences:
  1. **Bid-Ask Spread vs. Tick Size:** Major crypto perpetual pairs (e.g., `BTCUSDT`, `ETHUSDT` on Binance) exhibit substantially tighter relative bid-ask spreads (~0.5 to 1.0 basis points) compared to retail forex (1.0 to 1.5 pips on `EUR_USD` represents ~1.0 to 1.5 bps, but crosses like `EUR_JPY` represent 1.5 to 2.5 bps). However, altcoin perpetual contracts carry bid-ask spreads and market impact that dramatically exceed retail forex, making scalping even more unviable.
  2. **Exchange Fee Structure:** Unlike retail forex brokers that monetize primarily via the bid-ask spread without separate ticket fees, crypto derivatives exchanges charge explicit maker/taker fees (e.g., 2.0 to 5.0 bps taker). A strategy executing frequent market orders into crypto perpetuals would face fee drag far exceeding the OANDA toll.
  3. **Volatility & Barrier Distance:** Cryptocurrency daily ATR typically spans 3% to 6%, compared to 0.5% to 1.0% in G10 currencies. A 40–60 pip forex stop represents approximately 0.4% to 0.6% in price distance. In crypto, a 0.5% stop is located deep inside the sub-hourly noise threshold and would suffer instant liquidation cascades. Sizing must be scaled by ATR (`research-proposed`).
  4. **Funding Rate Carry & Liquidation Engines:** Crypto perpetuals incur continuous 8-hour funding rates. Holding wide-stop positions across multiple days exposes the portfolio to adverse funding carry and exchange auto-deleveraging (ADL) mechanics that do not exist in OTC spot forex.

## Limitations

- **Grey-Box Candidate Dialing (Pre-Optimization Impurity):** While cell selection and stop-loss tiers were determined strictly on in-sample training data (2019–2022), the underlying indicator thresholds for the 29 candidate setups were originally calibrated across full historical data in earlier program iterations (`source-reported`). This impurity favors the strategy by flattering historical backtests; the fact that the system still failed out-of-sample reinforces the robustness of the falsification.
- **Venue-Specific Retail Execution:** The empirical cost models reflect OANDA's retail pricing and execution engine. Institutional ECN venues (e.g., EBS, Currenex, Hotspot) offer substantially tighter raw spreads and lower slippage, though they impose explicit commission schedules.
- **Simulated Slippage Model:** Although calibrated against empirical stop-fill distributions from broker logs, the walk-forward results rely on a deterministic tiered slippage model rather than millisecond-level tick order-book queue matching (`source-reported`).
- **Small Cell Breadth:** The surviving candidate book contained only 3 currency cells, concentrating performance in Yen cross-rates (`AUD_JPY`, `USD_JPY`, `EUR_JPY`) during an aggressive Japanese Yen macro depreciation cycle (`source-reported`).
- **Absence of Independent Confirmation:** The findings have not been reproduced on an independent institutional research stack (e.g., PyBroker, NautilusTrader).

## Implementation status

`not-implemented`. No implementation of this strategy or execution model exists within our internal research environment. This record is a public research capture of third-party empirical findings.

## Adoption boundary

`not-approved`. This document serves strictly as research documentation. It does not constitute approval for strategy implementation, paper trading, testnet validation, or live capital allocation.

## Related Wiki records

- `[[quant/sp500-avellaneda-lee-residual-reversion-implementability-falsification-2026-09-13]]`
- `[[quant/crypto-perpetual-linear-inverse-quanto-convexity-bjork-identity-falsification-2026-09-13]]`
- `[[quant/retail-signal-three-gate-falsification-oscillator-volume-calendar-trend-2026-09-04]]`
- `[[quant/order-flow-imbalance-predictive-decoupling-cost-falsification-2026-09-12]]`

## Sources

1. **Brock (`BrockStar3540`) & Claude Code.** (2026). *Mr. Scrooge V6: Open-source algorithmic forex trading bot for OANDA (Python) — cell-based execution, wide-stop ratchet exits, and full backtesting research program*. GitHub repository `BrockStar3540/mr-scrooge-v6`, commit `efbe634fa8249027adcee81cde5be4d958dfed37` (accessed 2026-09-13). URL: https://github.com/BrockStar3540/mr-scrooge-v6
2. **Brock & Claude Code.** (2026-07-16). *H6, Tested: A Pre-Registered Walk-Forward Falsification of the Wide-Stop Thesis*. Research Monograph `docs/papers/PAPER_h6_walkforward_2026-07-16.md`, GitHub repository `BrockStar3540/mr-scrooge-v6`. URL: https://github.com/BrockStar3540/mr-scrooge-v6/blob/efbe634fa8249027adcee81cde5be4d958dfed37/docs/papers/PAPER_h6_walkforward_2026-07-16.md
3. **Brock & Claude Code.** (2026-07-14). *Edge Hunt: Falsifying Five Price-Edge Families and the Wide-Stop Turn*. Research Monograph `docs/papers/PAPER_edge_hunt_falsifications_2026-07-14.md`, GitHub repository `BrockStar3540/mr-scrooge-v6`. URL: https://github.com/BrockStar3540/mr-scrooge-v6/blob/efbe634fa8249027adcee81cde5be4d958dfed37/docs/papers/PAPER_edge_hunt_falsifications_2026-07-14.md
4. **Brock & Claude Code.** (2026-07-19). *The Party Package: Scale-In Grids, First-Passage Fairness, and a Live Forward Test*. Research Monograph `docs/papers/PAPER_party_package_scale_in_2026-07-19.md`, GitHub repository `BrockStar3540/mr-scrooge-v6`. URL: https://github.com/BrockStar3540/mr-scrooge-v6/blob/efbe634fa8249027adcee81cde5be4d958dfed37/docs/papers/PAPER_party_package_scale_in_2026-07-19.md
5. **Brock & Claude Code.** (2026-07-05). *Cost-Aware Exit Classes: Brackets, Ratchets, and ATR Scaling*. Technical Report `docs/papers/PAPER_cost_aware_exit_classes_2026-07-05.md`, GitHub repository `BrockStar3540/mr-scrooge-v6`. URL: https://github.com/BrockStar3540/mr-scrooge-v6/blob/efbe634fa8249027adcee81cde5be4d958dfed37/docs/papers/PAPER_cost_aware_exit_classes_2026-07-05.md
6. **Brock.** (2026). *Mr. Scrooge Research Program Docket and Methodological Axioms*. Technical Specification `docs/RESEARCH_PROGRAM.md`, GitHub repository `BrockStar3540/mr-scrooge-v6`. URL: https://github.com/BrockStar3540/mr-scrooge-v6/blob/efbe634fa8249027adcee81cde5be4d958dfed37/docs/RESEARCH_PROGRAM.md
7. **Brock.** (2026). *The Bar Governor: Autonomous Promotion and Demotion Engine*. Architecture Document `docs/GOVERNOR.md`, GitHub repository `BrockStar3540/mr-scrooge-v6`. URL: https://github.com/BrockStar3540/mr-scrooge-v6/blob/efbe634fa8249027adcee81cde5be4d958dfed37/docs/GOVERNOR.md
8. **Mr. Scrooge Engine Implementation Modules.** (2026). *Step-trail ratchet and scale-in tranche execution modules*. Source files `modules/management/ratchet.py`, `modules/management/party_package.py`, `modules/cells/cell.py`, and `config/cells/*.json`, GitHub repository `BrockStar3540/mr-scrooge-v6`. URL: https://github.com/BrockStar3540/mr-scrooge-v6/tree/efbe634fa8249027adcee81cde5be4d958dfed37/modules
