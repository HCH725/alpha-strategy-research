---
schema: strategy-research-record-v1
title: "China A-Share Level 3 Eaten-Order Age Imbalance: Intraday Directional Falsification and Sunk-Cost Parent Execution Timing Recovery"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - china-a-shares
  - szse-l3
  - market-microstructure
  - order-flow
  - event-clock
  - order-age-imbalance
  - directional-falsification
  - execution-timing
  - twap-overlay
status: research-only
confidence: medium
source_as_of: 2026-09-13
sources:
  - "https://github.com/BreevoZ/Quant_Research/tree/ca2e72fa96e85c96b3414c51dc9b25103a3cfaab/ashare/l3_factor"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# China A-Share Level 3 Eaten-Order Age Imbalance: Intraday Directional Falsification and Sunk-Cost Parent Execution Timing Recovery

## Provenance

- **Author:** Yihong Zhou (GitHub: BreevoZ / Cornell University)
- **Repository:** https://github.com/BreevoZ/Quant_Research
- **Full Commit SHA:** `ca2e72fa96e85c96b3414c51dc9b25103a3cfaab`
- **As-of Date:** 2026-09-13 (commit date: 2026-09-13T02:39:03Z; research reports dated 2026-07-07, 2026-07-17, 2026-07-18, and clean out-of-sample validation completed 2026-07-25)
- **Primary Source File Paths:**
  - `ashare/l3_factor/docs/REPORT_20260707.md` (Level 3 order ID arithmetic factor evaluation, single-day cross-sectional baseline)
  - `ashare/l3_factor/docs/REPORT_S123.md` (A-share intraday directional strategy six-month adjudication and structural cost falsification)
  - `ashare/l3_factor/docs/REPORT_EXEC_TIMING.md` (Controlled experiment of parent order execution timing overlay)
  - `ashare/l3_factor/FACTOR_BOOK.md` (Longitudinal 124-day in-sample and 90-day clean out-of-sample factor handbook across 2023–2025)
  - `ashare/l3_factor/factors/factor_id.py` (Implementation of `eat_age_imb`, `eat_age_med`, `old_eat_imb`, `cxl_life_med`)
  - `ashare/l3_factor/factors/factor_uniq.py` (Implementation of `kept_rem_imb`, `chain_imb`, `agg_hhi`, `book_age_imb`)
  - `ashare/l3_factor/backtest/exec_timing.py` (Three-arm controlled trial runner for TWAP vs Random vs Signal-timed allocation)
  - `ashare/l3_factor/bt/exec_timing_detail.csv` (Micro-execution log across 1,200 parent orders)
- **Primary Source Verification:** Directly inspected source code, factor calculation routines, backtest driver scripts, and empirical report logs from commit `ca2e72fa96e85c96b3414c51dc9b25103a3cfaab`. All empirical claims, formulas, IC statistics, t-ratios, and execution basis-point differentials trace directly to these primary files.

## Economic mechanism

### Source-reported

1. **The Event-Clock Arithmetic of Level 3 Order Sequence Numbers:**
   In the Shenzhen Stock Exchange (SZSE), Level 3 market data provides raw order sequence numbers (`ApplSeqNum`). When normalized by stripping the channel prefix (`seqNo % 10^12`), sequence numbers are strictly monotonic and globally shared across all order and cancellation events within a given matching channel. The numeric difference between two sequence numbers corresponds exactly to the number of market events that elapsed between them. This establishes an intrinsic "event clock" that automatically scales with market intensity, bypassing the arbitrary time-dilation distortions inherent in wall-clock bar aggregation.

2. **Resting Order Age Imbalance as an Exhaustion Indicator (`eat_age_imb`):**
   In SZSE execution messages (`actionType == 2`), the trade record contains both `buyId` and `sellId`. The order with the higher ID arrived later and represents the aggressive taker that crossed the spread; the order with the lower ID was the passive maker already resting in the limit order book. The difference `|buyId - sellId|` measures the resting age (in elapsed market events) of the consumed quote.
   The primary feature, `eat_age_imb` (eaten order age imbalance), computes the volume-weighted average log-age of resting asks consumed by aggressive buyers versus resting bids consumed by aggressive sellers:
   $$\text{eat\_age\_imb} = \frac{\overline{\ln(1 + \text{age}_B)} - \overline{\ln(1 + \text{age}_S)}}{\overline{\ln(1 + \text{age}_B)} + \overline{\ln(1 + \text{age}_S)}}$$
   The economic intuition is that old resting limit orders represent the patient inventory of liquidity providers. When aggressive market buyers chew through these deep, long-standing limit orders, it indicates aggressive, late-stage buying exhaustion or momentum chasing. Consequently, assets experiencing high positive `eat_age_imb` undergo systematic short-term mean reversion over the subsequent 1 to 2 minutes, generating a robust negative rank information coefficient ($\text{IC} < 0$).

3. **Intraday Directional Strategy Falsification (Alpha Ceiling vs. Cost Floor):**
   Despite strong statistical significance in cross-sectional rank IC ($\text{IC} = -0.0491$, $t = -51.3$ over 124 trading days in 2026H1; out-of-sample $\text{IC} = -0.031$, $t = -47$ over 90 trading days in 2023–2025), deploying this signal as a standalone intraday directional strategy fails completely. Backtested across 126 trading days in 2026H1 using realistic queue matching (`vsim`), every strategy variant (from single-factor baseline to multi-signal and cost-optimized execution packs) produced negative net PnL ($-11.04$ to $-8.36$ bps per round trip), resulting in zero profitable days (0/126 winning days).
   The structural failure stems from an irreconcilable horizon mismatch:
   - The signal's alpha ceiling is capped at 8–11 bps, decaying almost entirely within 1 to 2 minutes.
   - Chinese A-share trading incurs a mandatory friction floor of ~25 bps (5 bps stamp duty + 4 bps two-way commission + 15+ bps crossing spread and market impact).
   - Because microstructural order-flow imbalances dissipate rather than compound over longer horizons, lengthening the holding period (e.g., to 8 minutes) destroys the predictive power before entry queues can even clear.

4. **Sunk-Cost Recovery via Parent Order Execution Timing:**
   While independent directional trading is economically unviable, the author demonstrates that institutional parent orders (e.g., executing a 1,000,000 RMB block across 30 1-minute slices) represent a structural outlet:
   - For a mandatory parent order, the 25 bps execution friction (stamp duty, commission, and baseline bid-ask spread) is an unavoidable **sunk cost** because the trade must occur regardless of alpha.
   - The microstructural signal is therefore relieved of paying an incremental round-trip entry ticket.
   - By modulating slice weights dynamically (accelerating purchases when prices are predicted to rise, and deferring when predicted to fall), the signal's sub-minute predictive power converts directly into execution price improvement relative to a standard TWAP benchmark.

### Research interpretation

This source documents a textbook structural falsification and recovery case study in quantitative finance:
- **De-biasing Microstructural Illusions:** Many high-frequency order-flow anomalies published in academic literature boast enormous t-statistics ($t > 10$ or $t > 50$) that tempt researchers into building unfillable high-frequency directional strategies. This study rigorously shows that without a zero-friction institutional exchange structure, such alpha cannot exist as a standalone business.
- **Factor Subsumption:** Controlling for `eat_age_imb`, classical trade volume imbalance (`trd_imb`) collapses from $t = -10.2$ to $t = -0.06$ (partial IC drops to $-0.0002$), proving that order lifetime/depth dynamics completely subsume raw aggressor volume metrics at the 1-minute horizon.
- **Component Roles in the Composite Execution Signal:**
  - `eat_age_imb` (eaten order age imbalance): Primary mean-reversion anchor; penalizes buying into exhausted aggressive surges.
  - `kept_rem_imb` (unfilled residual sweep retention): Fast momentum component ($t = +11.2$ instant IC); rewards buying when aggressive sweeps leave unfilled resting limit orders (unsatisfied urgent demand).
  - `chain_imb` (order splitting chain imbalance): Institutional footprint detector ($t = +11.7$ instant IC); identifies consecutive order IDs ($gap \le 64$) with identical size and direction representing algorithmically sliced parent orders.
  - Slicing allocator: Largest-remainder integer lot allocation ensuring strict volume parity against uniform TWAP.

## Signal

### Formation timestamp

- Computed at 1-minute non-overlapping bar boundaries during continuous auction sessions (09:30–11:30 and 13:00–14:57 CST).
- Cross-sectional z-scores are calculated across the active eligible universe at minute close.
- Execution orders for slice $k$ are dispatched at second $t = (k \times 60) + 1$ (1,000 ms lookahead buffer after bucket close), strictly preventing forward-looking bias.

### Lookback

- Rolling 60-second window for Level 3 event aggregation.
- In-flight order age lookback: event-distance differences between order submission sequence number and execution sequence number within the trading session.

### Entry / Allocation logic

For an institutional parent order of total volume $V$ executed over $K = 30$ one-minute slices:
1. **Cross-Sectional Factor Normalization:**
   At each minute $b$, standardize the three underlying factors cross-sectionally:
   $$z(f) = \frac{f - \mu_b(f)}{\sigma_b(f)}$$
2. **Composite Signal Score:**
   $$\text{score}_b = z(\text{kept\_rem\_imb}_b) + z(\text{chain\_imb}_b) - z(\text{eat\_age\_imb}_b)$$
   Missing values are imputed with cross-sectional median.
3. **Slice Weight Modulation:**
   - For Buy parent orders: $w_k = 1 + \lambda \cdot \text{score}_{k-1}$
   - For Sell parent orders: $w_k = 1 - \lambda \cdot \text{score}_{k-1}$
   - Weight clipping: $w_k \in [w_{\min}, w_{\max}] = [0.3, 2.0]$
   - Parameter: $\lambda = 0.5$ (`source-reported`)
4. **Lot Quota Allocation:**
   To guarantee exact total volume match against the TWAP benchmark, raw continuous weights $w_k$ are discretized into integer 100-share lots using the largest remainder method (`alloc()` in `backtest/exec_timing.py`).
5. **Execution Trigger:**
   Dispatched as marketable limit orders with a $\pm 2.0\%$ price protection cap against the reference price, ensuring instantaneous matching against resting book liquidity.

### Exit

- Slices are executed as single-shot marketable orders at minute $k$; there is no multi-minute order holding period within the execution overlay.
- In the falsified directional setup (`v1a` to `S3`): fixed 8-minute holding period exit using crossing spread.

### Holding period

- Standalone directional research: 8 minutes (`source-reported`; falsified).
- Execution timing overlay: 30-minute total parent duration, comprised of 30 discrete 1-minute non-overlapping slice executions.

### Parameters

- `bucket`: 60 seconds (`source-reported`)
- `CHAIN_GAP`: 64 channel events (`source-reported`)
- `CHAIN_MINLEN`: 3 orders (`source-reported`)
- `KEEP_GAP`: 5,000 channel events (`source-reported`)
- `CROSS`: 0.02 (2% marketable limit cap) (`source-reported`)
- `CLIP`: [0.3, 2.0] (`source-reported`)
- `lambda`: 0.5 (`source-reported`)
- Universe size: 60 liquid stocks per session (`source-reported`)
- Parent notional: 1,000,000 RMB (`source-reported`)
- Alternative lookback windows (e.g., 30s or 120s): `research-proposed`
- Dynamic volatility-scaled $\lambda$: `research-proposed`

## Required data

- **Instrument:** Shenzhen Stock Exchange (SZSE) A-share equities.
- **Venue:** SZSE (Channelized binary tick data feed, replayed via `vsim`).
- **Market Type:** Spot equity (cash market).
- **Timeframe:** Tick-by-tick Level 3 order and trade messages (`actionType` 0=New Order, 1=Cancel, 2=Execution), aggregated to 60-second non-overlapping bars.
- **Data Fields:**
  - `seqNo`: Monotonic channel event sequence number (`ApplSeqNum`).
  - `sysid`: Original order sequence number being modified or cancelled.
  - `actionType`: Event category (0=Order, 1=Cancel, 2=Trade).
  - `buyId`: Order sequence number of the buyer.
  - `sellId`: Order sequence number of the seller.
  - `price`: Order or execution price.
  - `volume`: Order or executed quantity.
  - `direction`: Order side ('B'=Buy, 'S'=Sell).
  - `timeSeconds`: Wall-clock arrival timestamp.
- **Point-in-Time Integrity:**
  - Sequence numbers are inherently strictly causal.
  - Slice $k$ uses exclusively factor states computed from minute $k-1$, placed at second $+1$ of minute $k$.
  - Per-stock daily threshold quantiles (`med_age`, `q10_life`, `thr_big`) used in exploratory scripts contain minor end-of-day lookahead; the author notes this as an acknowledged exploratory convenience, while the longitudinal and execution backtests operate strictly point-in-time.
- **Missing-Data Handling:** Cross-sectional median imputation applied when a stock has no order-book activity during a 1-minute bucket.

## Execution assumptions

- **Fill Model:** Tested in `vsim`, an event-driven C++ Level 3 matching simulator that reconstructs the full limit order book, parses individual queue priorities, and matches against incoming virtual orders.
- **Marketable Limit Orders:** Slices are submitted with a 2% protection offset above the ask (for buys) or below the bid (for sells). Across all 1,200 simulated parent orders, the fill rate was 99.8% across TWAP, Random, and Signal arms, confirming that price discrepancies represent true timing gains rather than unexecuted slippage.
- **Friction Model (Directional Falsification):**
  - Stamp duty: 5 bps (seller pays).
  - Exchange and broker commission: 4 bps round-trip.
  - Bid-ask spread and crossing impact: 15+ bps.
  - Total friction floor: ~24–25 bps.
- **Sunk-Cost Framework (Execution Timing):**
  - Incremental trading fees: 0 bps (all commissions and stamp taxes are identical across TWAP and Signal arms because identical share quantities are transacted).
  - Market impact: Modulated by shifting volume between high-liquidity and low-liquidity minutes.

## Evidence

### Source-reported

All figures below are directly extracted from primary documentation reports (`REPORT_20260707.md`, `REPORT_S123.md`, `REPORT_EXEC_TIMING.md`, `FACTOR_BOOK.md`) and verified against `exec_timing_detail.csv`.

#### 1. Factor Information Coefficient and Out-of-Sample Persistence

Longitudinal evaluation across 2,891 SZSE stocks comparing in-sample (2026H1, 124 trading days) and clean out-of-sample (2023–2025, 90 trading days):

| Factor | Description | 2026H1 In-Sample `ret_next` IC (t) | 2026H1 In-Sample `ret_skip` IC (t) | 2023–2025 Out-of-Sample `ret_skip` IC (t) | Sign Consistency |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`eat_age_imb`** | Eaten order log-age imbalance | **-0.0491 (t = -51.3)** | **-0.0235 (t = -49.6)** | **-0.0310 (t = -47.0)** | **100% (124/124 days)** |
| `old_eat_imb` | Eaten orders with age $\ge$ median | -0.0524 (t = -48.8) | -0.0168 (t = -32.7) | -0.0250 (t = -37.0) | 99% |
| `trd_imb` | Classical aggressive trade imbalance | -0.0361 (t = -31.9) | -0.0114 (t = -26.7) | -0.0170 (t = -29.0) | 98% |
| `kept_rem_imb` | Swept residual retained in book | +0.0876 (t = +11.2) | +0.0029 (t = +1.2) | N/A (5-day exploratory) | 80% |
| `chain_imb` | Algorithmic split order chain imbalance | +0.0332 (t = +11.7) | -0.0019 (t = -0.9) | N/A (5-day exploratory) | 60% |
| `flash_cxl_imb` | Flash cancellation imbalance (Trap) | +0.0204 (t = +28.9) | +0.0007 (t = +1.6) | **-0.0050 (t = -11.0, sign reversed)** | 51% (Coin flip) |

*Partial IC verification:* On single-day cross-section (2026-07-07), controlling for `trd_imb`, `eat_age_imb` preserves its partial IC at $-0.066$ ($t = -15.2$), whereas controlling for `eat_age_imb`, `trd_imb` collapses to $-0.0002$ ($t = -0.06$).

#### 2. Standalone Directional Intraday Strategy Falsification

Six-month backtest (2026H1, 126 trading days, 28,000 real queue-matched trades, 5-minute trigger, holding 8 minutes, inventory T+0):

| Strategy Configuration | Net PnL per Round-Trip (bps) | Cumulative Net PnL (RMB) | Daily Win Rate |
| :--- | :--- | :--- | :--- |
| `v1a` Baseline (`eat_age` single factor, aggressive entry, crossing exit) | -11.04 bps | -2,905,000 RMB | 0 / 126 days (0.0%) |
| `S1` Signal Pack (`kept_rem + chain - eat_age`) | -10.60 bps (+0.44 bps vs baseline) | -2,869,000 RMB | 0 / 126 days (0.0%) |
| `S2` Execution Pack (Stock price $\ge 15$ RMB + two-stage exit) | -8.68 bps (+2.36 bps vs baseline) | -2,090,000 RMB | 0 / 126 days (0.0%) |
| `S3` Full Combined (Signal Pack + Execution Pack) | **-8.36 bps (+2.69 bps vs baseline)** | -2,110,000 RMB | **0 / 126 days (0.0%)** |

#### 3. Controlled Experiment: Parent Order Execution Timing Overlay

Experimental evaluation across 20 trading days $\times$ 60 liquid stocks = 1,200 parent orders (10:00–10:30, 1M RMB notional, 600 Buy / 600 Sell):

| Trial Arm | Execution Improvement vs. TWAP (bps) | Daily t-statistic | Parent Order Win Rate | Positive Days Ratio |
| :--- | :--- | :--- | :--- | :--- |
| **Random Weights vs. TWAP (`rand`)** | **-0.06 bps** | **-0.24** | 50.0% | 45.0% (9 / 20 days) |
| **Signal Timing vs. TWAP (`sig`)** | **+2.83 bps** | **+5.35** | **64.0%** | **90.0% (18 / 20 days)** |

- **Directional Symmetry:** Buy parent orders improved by **+2.69 bps** ($n = 600$); Sell parent orders improved by **+2.97 bps** ($n = 600$).
- **Distributional Robustness:** Mean = +2.83 bps, Median = +2.19 bps, 5% Trimmed Mean = +2.82 bps (rejecting outlier distortion). Distribution percentiles: $p_{25} = -2.2$ bps, $p_{50} = +2.2$ bps, $p_{75} = +7.6$ bps.
- **Economic Scale:** A +2.83 bps execution improvement on 1,000,000 RMB notional yields ~283 RMB savings per parent order. Across an institutional annual execution volume of 1,000,000,000 RMB, this equates to ~2,830,000 RMB annual execution savings without incurring additional transaction costs.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Standalone Directional Strategy Infeasibility:** 126 consecutive unprofitable trading days confirm that sub-minute order-flow signals cannot overcome retail-market friction (stamp tax and crossing spread) as an independent trading strategy.
- **Horizon Decay:** The raw predictive signal decays by over 70% within the first 60 seconds of post-formation time; it provides zero positive predictive power at holding horizons beyond 4 minutes.
- **Spurious Indicator Traps:** Features such as `large_share` (large order volume share) and `flash_cxl_imb` (flash cancellation imbalance) exhibit deceptively high contemporaneous t-statistics ($t = 7.5$ and $t = 28.9$), but collapse to zero or reverse sign in out-of-sample skip-1 testing, representing unfillable microstructural noise.

## Falsification plan

1. **Out-of-Sample Parent Execution Degradation:**
   If the execution timing overlay (`sig vs twap`) fails to achieve a statistically significant execution improvement ($\text{improvement} < +0.50$ bps or daily $t < 1.96$; `research-defined falsification threshold`) over a fresh out-of-sample sample of 1,000 parent orders, the execution alpha hypothesis is falsified.
2. **Order Size Capacity / Market Impact Penalty:**
   If the parent order notional is scaled from 1M RMB to 5M RMB (or $> 2.5\%$ of ADV) and the adverse market impact of heavily weighted slices causes net VWAP to underperform TWAP by more than $-1.0$ bps (`research-defined falsification threshold`), the capacity assumption of the execution overlay is falsified.
3. **Signal Component Ablation:**
   If an ablation test removing `eat_age_imb` from the three-factor composite score reduces execution improvement by less than 0.5 bps (`research-defined falsification threshold`), the hypothesis that resting order age specifically drives execution timing is rejected.
4. **Passive Maker Queue Adverse Selection:**
   If the execution overlay is adapted to use passive limit orders rather than marketable orders, and the maker fill rate during high-score minutes drops below 60% due to adverse selection (`research-defined falsification threshold`), passive liquidity provision adaptation is falsified.

## Crypto portability

**Status:** adapted / unproven

- **Level 3 Data Availability Barriers:** Most cryptocurrency spot and perpetual derivatives exchanges (e.g., Binance, OKX, Bybit) provide Level 2 order book snapshots and public trade feeds, but omit unique matching-engine sequence numbers linking individual limit orders to executions. Without native `buyId` and `sellId` tracking, the exact event-clock age of consumed orders cannot be reconstructed directly on public feeds.
- **Venue Exceptions:** Certain exchanges (such as Hyperliquid or Coinbase market data feeds with individual order life events, or direct private FIX/websocket execution streams) expose order tracking IDs that could permit an adapted event-clock formulation.
- **Friction Structure Inversion:** Unlike Chinese A-shares (with a 5 bps stamp tax and 25 bps round-trip friction floor), crypto perpetual futures feature no transaction stamp tax, lower maker fees (often 0.00% to -0.01% rebates), and taker fees of 2.0 to 5.0 bps. In low-fee crypto perpetual markets, the structural cost floor is substantially lower (~5–10 bps), though volatility and spread crossing remain material.
- **Execution Overlay Applicability:** Institutional crypto execution algorithms (e.g., executing large BTC or ETH TWAP orders on Binance or Hyperliquid) can directly adopt the three-factor slice-weighting architecture (`kept_rem_imb`, `chain_imb`, and proxy order-age imbalance) as a parent order execution optimizer. This adaptation remains an unproven research hypothesis in crypto markets until tested on crypto tick data.

## Limitations

- **Single Exchange Microstructure:** Primary evidence is derived entirely from the Shenzhen Stock Exchange (SZSE) continuous auction session. Generalizability to the Shanghai Stock Exchange (SSE), which uses a distinct order reporting protocol (where 41% of trades lack direct order ID links), is unproven without synthetic order reconstruction.
- **Selection-Level Leakage:** The three-factor composite was identified on 2026H1 data, which overlaps with the 20-day sample used in the initial execution timing experiment. Although the individual factor `eat_age_imb` was cleanly verified on 90 out-of-sample days across 2023–2025, the multi-factor execution weighting overlay requires replication on fully independent years.
- **Restricted Execution Horizon:** Tested exclusively in a 30-minute morning window (10:00–10:30 CST) on liquid large-cap names. Performance during opening/closing auctions, lunch session transitions, or highly illiquid small-cap stocks remains untested.
- **Marketable Fill Assumption:** The experiment utilizes marketable orders with a 2% price collar. While this eliminates queue execution risk, it does not evaluate passive limit order queue placement or adverse selection against aggressive flow.

## Implementation status

`not-implemented`

No implementation in our internal research stack (`nautilus-quant-system` or PyBroker). All reported results originate from the author's C++ Level 3 matching engine (`vsim`) and Python analytical pipeline.

## Adoption boundary

This document represents research-only material. Its inclusion in this repository does not constitute validation of trading profitability, strategy adoption, or authorization for deployment in paper trading, testnet, or live production environments.

The standalone directional trading strategy is explicitly classified as **falsified**. Any downstream application of the parent order execution timing overlay requires independent replication, execution architecture integration, and strict compliance reviews.

## Related Wiki records

- `[[china-ashare-limit-up-momentum-unfillable-execution-falsification-2026-09-13]]` — A-share limit-up execution falsification and liquidity queue barriers.
- `[[m2-alpha-micro-macro-attention-a-share-deep-learning-ranking-2026-09-13]]` — Cross-sectional A-share deep learning ranking on daily features.
- `[[order-flow-imbalance-predictive-decoupling-cost-falsification-2026-09-12]]` — Microstructure order flow imbalance and transaction cost boundary falsification.

## Sources

1. **Repository:** https://github.com/BreevoZ/Quant_Research
2. **Immutable Commit:** `ca2e72fa96e85c96b3414c51dc9b25103a3cfaab`
3. **Author:** Yihong Zhou (BreevoZ, Cornell University)
4. **Primary Research Documents:**
   - `ashare/l3_factor/docs/REPORT_20260707.md`
   - `ashare/l3_factor/docs/REPORT_S123.md`
   - `ashare/l3_factor/docs/REPORT_EXEC_TIMING.md`
   - `ashare/l3_factor/FACTOR_BOOK.md`
5. **Primary Code Artifacts:**
   - `ashare/l3_factor/factors/factor_id.py`
   - `ashare/l3_factor/factors/factor_uniq.py`
   - `ashare/l3_factor/backtest/exec_timing.py`
   - `ashare/l3_factor/bt/exec_timing_detail.csv`
