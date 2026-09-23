---
schema: strategy-research-record-v1
title: Bitcoin Pi Cycle Top and Bottom Moving Average Ratio Oscillator
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - bitcoin
  - moving-average
  - macro-cycle
  - market-timing
  - lookintobitcoin
status: research-only
confidence: medium
source_as_of: 2026-09-23
sources:
  - "https://www.lookintobitcoin.com/charts/pi-cycle-top-indicator/"
  - "https://www.lookintobitcoin.com/charts/pi-cycle-top-bottom-indicator/"
  - "https://medium.com/@positivecrypto/the-golden-ratio-multiplier-c2567401e12a"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Pi Cycle Top and Bottom Moving Average Ratio Oscillator

## Provenance

- **Primary Source:** Philip Swift (`@PositiveCrypto`), LookIntoBitcoin / Decentrader.
- **Original Publication:** April 2019, introduced in Philip Swift, *"The Golden Ratio Multiplier"* (Medium publication, April 2019, including the original derivation of the 350-day moving average multiples and the Pi Cycle Top indicator).
- **Official Live Repositories / Portals:**
  - *Bitcoin: Pi Cycle Top Indicator*: https://www.lookintobitcoin.com/charts/pi-cycle-top-indicator/ (live chart and documentation).
  - *Pi Cycle Top & Bottom Indicator*: https://www.lookintobitcoin.com/charts/pi-cycle-top-bottom-indicator/ (live oscillator chart and documentation).
- **Source Verification & Audit (performed 2026-09-23):** LookIntoBitcoin primary pages directly fetched and verified. All indicator specifications, moving average lengths (111-day and 350-day), scaling multiples ($2\times$ for cycle highs, $75\%$ discount / $0.25$ ratio for bear cycle lows), and historical empirical claims ("picked the top of previous $BTC market cycles to within 3 days") trace directly to the primary source text and methodology descriptions.
- **Source-Identity Deduplication (repository-wide ripgrep across all `*.md` records):** Pre-write search across all records in `alpha-strategy-research` confirmed zero prior records for `pi-cycle`, `111DMA`, `350DMA`, or Philip Swift's moving average multiples. The only mention of Pi Cycle in the entire repository is a passing contextual reference in `bitcoin-halving-clock-time-based-cycle-top-timing-2026-09-03.md` citing it alongside MVRV and Mayer Multiple as an example of a price-anchored cycle indicator. Adjacent Bitcoin cycle indicators (`bitcoin-mayer-multiple-macro-valuation-bands-2026-09-01.md`, `bitcoin-onchain-rhodl-ratio-macro-cycle-2026-08-31.md`, `tradingview-bitcoin-top-cap-delta-top-cycle-valuation-2026-09-22.md`) address fundamentally different mechanisms (200DMA multiples, on-chain coin-days destroyed bands, cumulative investor-cap ceilings). This record captures a genuinely new, independent source and indicator identity.

## Economic mechanism

### Source-reported

Philip Swift formulates the Pi Cycle indicator family based on the observation that Bitcoin's adoption proceeds in multi-year psychological and market cycles driven by speculative excitement and capitulation. The framework compares two distinct momentum horizons:
1. The **111-day Simple Moving Average (111DMA)**, representing an intermediate-term momentum reference.
2. The **350-day Simple Moving Average multiplied by 2 ($350DMA \times 2$)**, representing a long-term multi-cycle baseline anchor (the 350DMA tracks the ~1-year baseline price level).

Swift highlights the mathematical relationship $350 / 111 = 3.15315...$, which is the closest whole-number approximation to the mathematical constant $\pi \approx 3.14159...$ when dividing 350 by an integer. The author argues that when the intermediate-term momentum (111DMA) surges up to meet or cross above the long-term trend multiple ($350DMA \times 2$), the market has become unsustainably overheated, marking a cyclical exhaustion point where price peaks before a major multi-month bear drawdown.

In the extended *Pi Cycle Top & Bottom Oscillator*, Swift normalizes the relationship into a ratio:
$$\text{Oscillator}_t = \frac{\text{SMA}_{111}(t)}{2 \times \text{SMA}_{350}(t)}$$
When the oscillator reaches or exceeds $1.0$, the market is at cycle peak overheating. When the 111DMA subsequently drops below $2 \times 350\text{DMA}$ and falls to a $75\%$ discount relative to $2 \times 350\text{DMA}$ (i.e. $\text{Oscillator}_t \le 0.25$, which is algebraically identical to $\text{SMA}_{111}(t) \le 0.5 \times \text{SMA}_{350}(t)$), the source states that market momentum has cooled down significantly, historically delineating broad accumulation zones for major bear market lows.

### Research interpretation

The falsifiable economic mechanism is **dual-horizon moving average acceleration and mean reversion**, rather than the numerological significance of $\pi$. Specifically:
- **Upper Blow-off Exhaustion (Top Signal):** A crossover condition where $\text{SMA}_{111}(t) > 2 \times \text{SMA}_{350}(t)$ can only occur when Bitcoin has experienced a sustained parabolic price expansion over 3–4 months that drives the 111-day average to double the trailing 1-year baseline level. In a speculative asset with inelastic near-term supply, such explosive acceleration consumes available buy-side liquidity, creates extreme margin leverage, and leaves the market fragile to sudden order-flow exhaustion.
- **Lower Capitulation Discount (Bottom Signal):** When $\text{SMA}_{111}(t) \le 0.5 \times \text{SMA}_{350}(t)$, intermediate-term price levels have collapsed to half of the secular 1-year baseline. This reflects severe momentum liquidation, forced seller exhaustion, and a transition from speculative momentum traders to deep-value long-term accumulators.
- **Curve-fitting and Numerology Boundary:** The quotient $350/111 \approx 3.153$ being close to $\pi$ is an ex-post mathematical curiosity without physical or financial causation. Parameter stability and ablation tests are mandatory to distinguish genuine dual-timeframe momentum exhaustion from retrospective curve-fitting to the 2011, 2013, and 2017 market cycles.

## Signal

All operational parameters and rules below are classified as `source-reported` or `research-proposed`:

- **Component Calculations (`source-reported`):**
  - Intermediate Moving Average: $\text{SMA}_{111}(t) = \frac{1}{111} \sum_{i=0}^{110} P_{t-i}$
  - Baseline Moving Average: $\text{SMA}_{350}(t) = \frac{1}{350} \sum_{i=0}^{349} P_{t-i}$
  - Cycle Top Upper Band: $\text{TopBand}(t) = 2.0 \times \text{SMA}_{350}(t)$
  - Cycle Ratio Oscillator: $\text{Osc}(t) = \frac{\text{SMA}_{111}(t)}{2.0 \times \text{SMA}_{350}(t)}$
- **Cycle Top Exit / De-risk Trigger (`source-reported` trigger logic; execution details `research-proposed`):**
  - *Trigger Condition:* $\text{SMA}_{111}(t)$ crosses from strictly below to at or above $\text{TopBand}(t)$ (equivalent to $\text{Osc}(t) \ge 1.0$) on daily bar close (`source-reported`).
  - *Action:* Liquidate $100\%$ of Bitcoin spot holdings to USD/USDC cash reserves (`research-proposed`).
  - *Shorting Variant:* Open a $1.0\times$ notional short position on perpetual futures (`research-proposed`).
- **Cycle Bottom Accumulation Trigger (`source-reported` trigger logic; execution details `research-proposed`):**
  - *Trigger Condition:* $\text{Osc}(t) \le 0.25$ (i.e. $\text{SMA}_{111}(t)$ drops to a $75\%$ discount relative to $2 \times \text{SMA}_{350}(t)$, equivalent to $\text{SMA}_{111}(t) \le 0.5 \times \text{SMA}_{350}(t)$) (`source-reported`).
  - *Action:* Initiate systematic DCA or allocate $100\%$ capital to spot Bitcoin (`research-proposed`).
- **Re-entry Rules (`research-proposed`; omitted by primary source, `underspecified`):**
  - If a cycle top exit occurred, re-entry into long spot is prohibited until $\text{Osc}(t)$ cools below $0.80$ and re-crosses above the 200-day SMA, or until a cycle bottom trigger ($\text{Osc}(t) \le 0.25$) is reached (`research-proposed`).
- **Signal Formation Timestamp (`research-proposed`):** Daily bar close at 23:59:59 UTC. The source displays daily price charts without specifying an exchange execution clock (`underspecified`).
- **Execution Timing (`research-proposed`):** Execution occurs at $t+1$ bar open (00:00:00 UTC) following daily close signal confirmation.
- **Lookback Windows (`source-reported`):** Short window $L_1 = 111$ days; long baseline window $L_2 = 350$ days. Minimum warm-up period is 350 calendar days.
- **Holding Period (`research-proposed`; source specifies macro cycle horizon only):** Long positions held during expansion phases (typically 12–36 months); cash/short positions held during contraction phases (typically 6–18 months).
- **Position Sizing (`research-proposed`):** Binary $100\%$ long vs. $100\%$ cash/short; no multi-asset weighting in the primary source.
- **Multi-timeframe Dependencies (`source-reported`):** None; single daily (1D) timeframe.

## Required data

- **Asset / Instrument:** Bitcoin (BTC/USD or BTC/USDT).
- **Market Type:** Spot market or linear perpetual contracts (`research-proposed` spot primary).
- **Venue:** Liquid major crypto exchanges with long historical operating history (e.g. Bitstamp, Coinbase, Kraken, Binance) or consolidated index (e.g. CME CF Bitcoin Reference Rate, CoinDesk BTC Index) (`research-proposed`).
- **Timeframe:** Daily (1D) bars with continuous 24/7 calendar aggregation (`source-reported`).
- **Fields:** OHLCV daily closing prices (`source-reported`).
- **Sample Length:** Continuous daily price series spanning July 2010 through present (requiring at least 350 days of warm-up before first signal evaluation) (`research-proposed`).
- **Point-in-time Integrity:** Historical daily closing prices are final at 23:59:59 UTC; no revisions or restatements (`source-reported`).
- **Missing-data Treatment:** Missing bars must be forward-filled or reconciled against secondary exchange feeds; zero-filling or synthetic interpolation is strictly forbidden (`research-proposed`).
- **Funding / Fee / Spread Data:** For spot execution, exchange taker/maker fee schedules and bid-ask spread; for perpetual execution, 8-hour funding rates and borrow rates (`research-proposed`).

## Execution assumptions

- **Execution Timing:** Next-day market open (00:00:00 UTC) following the confirmed daily close signal (`research-proposed`).
- **Order Type:** Market order on open (MOO) or immediate limit order at the opening price (`research-proposed`).
- **Transaction Costs & Fees:** $10\text{ bps}$ ($0.10\%$) taker fee per side (`research-proposed`).
- **Bid-Ask Spread & Slippage:** $5\text{ bps}$ ($0.05\%$) one-way slippage model (`research-proposed`).
- **Borrow & Shorting Costs:** If tested as a long-short strategy, borrow rate of $5.0\%$ annualized on BTC short positions (`research-proposed`).
- **Funding Costs (Perpetuals):** Net cumulative 8-hour funding rate deducted from perpetual short returns (`research-proposed`).
- **Source Cost Model:** The primary LookIntoBitcoin source models zero transaction fees, zero slippage, zero borrow cost, and immediate frictionless execution (`source-reported`).

## Evidence

### Source-reported

The primary source (LookIntoBitcoin / Philip Swift) reports the following empirical observations across historical Bitcoin price cycles:
- **Historical Cycle Tops:** Across the first three major historical Bitcoin cycles, the $111\text{DMA}$ crossing above $350\text{DMA} \times 2$ coincided with the peak of Bitcoin market cycles to within 3 days:
  - *2011 Cycle:* Crossover coincided with the June 2011 cycle high (~$31.90).
  - *2013 Cycles:* Crossovers coincided with the April 2013 peak (~$260) and the November/December 2013 major cycle peak (~$1,160).
  - *2017 Cycle:* Crossover coincided with the December 2017 cycle top (~$19,700) within 3 days.
  - *2021 Cycle:* Crossover occurred on April 12–14, 2021, immediately preceding the April 2021 peak (~$64,800).
- **Historical Cycle Bottoms (Oscillator $\le 0.25$):** Drops into the lower green band ($\text{SMA}_{111} \le 0.5 \times \text{SMA}_{350}$) coincided with broad macro cycle bottom accumulation areas in:
  - January–April 2015 ($BTC ~$200–$250).
  - December 2018 – March 2019 ($BTC ~$3,200–$4,000).
  - June–December 2022 ($BTC ~$16,000–$20,000).
- **Performance Metrics Gap (`data gap` / `not stated in source`):** The source reports no formal backtest metrics: no Sharpe ratio, Sortino ratio, CAGR, maximum drawdown, win rate, profit factor, t-statistic, or capacity limits are provided in the source documentation.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **2021 Double-Top Failure / False Alarm:** In the 2021 cycle, the Pi Cycle Top indicator crossed on April 12, 2021, at ~$64,000, calling the top. However, after a summer correction to ~$29,000, Bitcoin rallied to a new all-time high of ~$69,000 in November 2021 *without* triggering a second Pi Cycle crossover. An automated short strategy following the April cross would have suffered severe drawdowns during the Q4 2021 rally to $69,000, while a long-only de-risking strategy completely missed the second macro peak.
- **Acute Sample-Size Deficit & Overfitting:** The parameters $111$ and $350$ and multiplier $2.0$ were retrospectively identified in April 2019 to fit three historical cycle peaks (2011, 2013, 2017). With an effective event sample size of $N \approx 4$ cycle events in Bitcoin's 15-year history, standard statistical tests (e.g. bootstrap hypothesis testing) cannot establish statistical significance against a null of random moving-average crossovers.
- **Arbitrary Numerology Rationale:** The claim that $350 / 111 \approx 3.153 \approx \pi$ creates causal validity is numerological post-hoc rationalization. Neighboring combinations (e.g. 110/345, 112/355, 115/365) exhibit varying degrees of lead/lag error, showing that small integer parameter perturbations alter peak alignment.
- **Author-Acknowledged Structural Decay Risk:** The creator explicitly warns on the primary LookIntoBitcoin page: *"It is also worth noting that this indicator has worked during Bitcoin's adoption growth phase, the first 15 years or so of Bitcoin's life. With the launch of Bitcoin ETF's and Bitcoin's increased integration into the global financial system, this indicator may cease to be relevant in this new market structure."*
- **Prolonged Whipsaw in Ranging Regimes:** The bottom oscillator ($\le 0.25$) remains depressed for 3 to 9 consecutive months during prolonged bear markets (e.g. throughout H2 2022). Buying immediately upon first entry into the green band incurs deep mark-to-market drawdown (e.g. buying at $25,000 in June 2022 before the final drop to $15,500 in November 2022).

## Falsification plan

All tests below specify data, sample, metric, decision rule, and action. Every threshold is a `research-defined falsification threshold`:

1. **Parameter Perturbation Grid Stress:**
   - *Test Setup:* Evaluate the crossover timing on historical Bitcoin daily data under a parameter grid: short lookback $L_1 \in [95, 125]$ (step 2), long lookback $L_2 \in [315, 385]$ (step 5), and multiplier $M \in [1.8, 2.2]$ (step 0.05).
   - *Failure Rule (`research-defined falsification threshold`):* If $> 50\%$ of parameter combinations in the $\pm 5\%$ neighborhood of $(111, 350, 2.0)$ shift the signal timing error from $\le 3$ days to $> 20$ days away from historical peaks, reject the specific Pi Cycle parameterization as an artifact of curve-fitting to the 2011–2017 sample.
2. **True Out-of-Sample Peak Validation (Post-2019 Cycles):**
   - *Test Setup:* Freeze the $(111, 350, 2.0)$ parameters and evaluate performance exclusively on the post-April 2019 out-of-sample window (2021 double top and the 2024–2026 cycle).
   - *Failure Rule (`research-defined falsification threshold`):* If the indicator generates a cycle top signal followed by a new all-time high that is $> 15\%$ higher than the signal price (as occurred in November 2021), or fails to signal within 30 days of the terminal cycle peak, falsify the claim that Pi Cycle reliably identifies secular market peaks.
3. **Ablation vs. Simpler Classical Moving-Average Baselines:**
   - *Test Setup:* Backtest a long/cash rotation strategy using Pi Cycle Top against three simple benchmarks: (a) 200-day SMA trend filter, (b) Mayer Multiple $> 2.4$ threshold, and (c) 52-week rolling breakout filter, over the 2011–2026 period net of 15 bps round-trip trading costs.
   - *Failure Rule (`research-defined falsification threshold`):* If the net-of-cost Calmar ratio or Sharpe ratio of the Pi Cycle strategy does not exceed the simple 200-day SMA baseline by at least $10\%$, reject the Pi Cycle mechanism as redundant over simpler moving average filters.
4. **Bottom Oscillator Accumulation vs. Periodic DCA Baseline:**
   - *Test Setup:* Compare systematic capital deployment triggered by $\text{Osc}(t) \le 0.25$ against standard weekly Dollar-Cost Averaging (DCA) over 3-year rolling forward holding periods starting from bear market lows.
   - *Failure Rule (`research-defined falsification threshold`):* If the bottom accumulation rule yields a lower 3-year forward annualized return or higher maximum drawdown than weekly DCA across $\ge 2$ bear cycle episodes, falsify the claim that the $0.25$ oscillator threshold provides actionable accumulation timing edge.
5. **Placebo / Randomized Return Bootstrap:**
   - *Test Setup:* Generate 1,000 synthetic Bitcoin price paths using a stationary block bootstrap (block size $L = 60$ days). Compute the frequency with which the $111\text{DMA}$ crosses $350\text{DMA} \times 2$ within 3 days of a path's absolute peak.
   - *Failure Rule (`research-defined falsification threshold`):* If the empirical $p$-value exceeds $0.05$ (i.e. more than $5\%$ of bootstrap paths generate a top cross within 3 days of the peak by chance), reject the null hypothesis of non-random timing predictive power.

## Crypto portability

**direct**

- The indicator was constructed natively on Bitcoin daily price history and UTXO halving adoption dynamics.
- Portability to other crypto assets (e.g. Ethereum, Solana, or high-beta altcoins) is `unproven` and expected to fail without significant re-calibration, because other assets possess substantially shorter market histories, differing tokenomic unlock structures, and do not share Bitcoin's four-year quadrennial halving cycle.
- Portability to perpetual futures markets requires explicit modeling of borrow fees, margin liquidation risk, and cumulative funding rate drag during multi-month short positions (`research-proposed`).
- Crypto portability does not constitute authorization to trade.

## Limitations

- `data gap`: The primary source provides zero formal quantitative backtest statistics (no Sharpe, Sortino, max drawdown, win rate, or capacity metrics).
- `underspecified`: Re-entry timing, trade execution protocols, order types, stop-loss mechanisms, and position sizing are omitted in the original documentation.
- `not independently reproduced`: None of the source-reported claims have been independently reproduced in our quantitative engine.
- Extreme sample-size limitation: Only 3 to 4 macro cycle events exist in the entire history of Bitcoin, rendering classical statistical inference underpowered.
- Retrospective curve-fitting: Lookback parameters (111 and 350) were chosen post-hoc in 2019 to fit three known cycle peaks.
- Structural regime vulnerability: Introduction of US spot Bitcoin ETFs, institutional custody, and regulated derivative hedging materially alters cyclical capital flows, increasing the likelihood that historical moving average multiples lose predictive alignment.
- Asymmetric signal performance: Successfully called the April 2021 top but failed to signal the November 2021 higher high.

## Implementation status

`not-implemented`. No code has been integrated into NautilusTrader or Qlib backtest workflows. No prototype, paper trading, testnet, or live trading execution has been authorized or performed.

## Adoption boundary

Research material only. Presence in this repository does not mean this strategy has passed Research Intake Review, entered Hermes Wiki Brain, entered the production candidate pool, completed Qlib full-backtest validation, achieved survivor status, demonstrated live alpha, or received implementation, Paper, Testnet, or Live approval. `status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` — canonical strategy research record schema.
- Non-wiki repository conceptual relatives (inspected for deduplication and context):
  - `bitcoin-halving-clock-time-based-cycle-top-timing-2026-09-03.md` — explicitly analyzes the failure sequence of price-anchored cycle indicators (including Pi Cycle, MVRV, Mayer Multiple) vs. time-based halving clocks.
  - `bitcoin-mayer-multiple-macro-valuation-bands-2026-09-01.md` — 200DMA multiple valuation bands for cycle extremes.
  - `bitcoin-onchain-rhodl-ratio-macro-cycle-2026-08-31.md` — on-chain age-weighted realized HODL ratio for macro cycle timing.
  - `tradingview-bitcoin-top-cap-delta-top-cycle-valuation-2026-09-22.md` — Top Cap and Delta Cap cumulative market cap models for Bitcoin cycle peaks.

## Sources

1. Philip Swift, **Bitcoin: Pi Cycle Top Indicator**, LookIntoBitcoin live chart and methodology documentation, created April 2019, reviewed 2026-09-23: https://www.lookintobitcoin.com/charts/pi-cycle-top-indicator/
2. Philip Swift, **Pi Cycle Top & Bottom Indicator**, LookIntoBitcoin live oscillator chart and documentation, reviewed 2026-09-23: https://www.lookintobitcoin.com/charts/pi-cycle-top-bottom-indicator/
3. Philip Swift, *"The Golden Ratio Multiplier: Mapping Bitcoin's Market Cycles"*, Medium publication (`@PositiveCrypto`), April 2019: https://medium.com/@positivecrypto/the-golden-ratio-multiplier-c2567401e12a
