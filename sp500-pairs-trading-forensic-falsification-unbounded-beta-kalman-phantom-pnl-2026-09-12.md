---
schema: strategy-research-record-v1
title: "Forensic Deconstruction and Live Falsification of Cointegration-Based Pairs Trading: Unbounded Hedge Ratios, Phantom Kalman P&L, and Regime Fragility"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - pairs-trading
  - cointegration
  - kalman-filter
  - look-ahead-bias
  - live-paper-audit
  - hedge-ratio-falsification
  - deflated-sharpe
status: research-only
confidence: high
source_as_of: 2026-09-10
sources:
  - "https://github.com/Duyanh090205/pairs-trading-engine (commit 30311352348c0a4939c237b5ef57d57c353e29b8, 2026-09-10)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forensic Deconstruction and Live Falsification of Cointegration-Based Pairs Trading: Unbounded Hedge Ratios, Phantom Kalman P&L, and Regime Fragility

## Provenance

- **Author:** Duy Anh Nguyen (`Duyanh090205`), with audit review assistance noted in repo metadata (`source-reported`).
- **Repository:** `Duyanh090205/pairs-trading-engine`
- **Repository URL:** [https://github.com/Duyanh090205/pairs-trading-engine](https://github.com/Duyanh090205/pairs-trading-engine)
- **Canonical Immutable Commit SHA:** `30311352348c0a4939c237b5ef57d57c353e29b8` (`source-reported`)
- **Commit Date:** September 10, 2026 (`source-reported`)
- **Key Files Examined Directly:**
  - Root Documentation & Retractions: `README.md`
  - Week 6 Production Engine & Forensic Log: `Week 6/README.md`, `Week 6/documents/log.md`, `Week 6/engine_daily/engine_daily.py`, `Week 6/engine_daily/carry_forward.py`
  - Dynamic Kalman Hedge-Ratio Research: `Week 6/scripts/research/dynamic_beta/README.md`, `Week 6/scripts/research/dynamic_beta/FINAL_FINDINGS.md`, `Week 6/scripts/research/dynamic_beta/arms.py`, `Week 6/scripts/research/dynamic_beta/audit_b1.py`, `Week 6/scripts/research/dynamic_beta/analyze.py`
  - Look-Ahead Bias Injection Framework: `Week 3/README.md`, `Week 3/scripts/deliverable1.py`, `Week 3/scripts/engine.py`
  - Dynamic Friction & Overfitting Diagnostics: `Week 5/README.md`, `Week 5/reports/net_of_fees_report.md`
  - Live Broker Submission Logs: `Week 6/submission_data/` (Alpaca paper trading order and position logs, May–July 2026)
- **Sample Period:** January 2022 to July 2026 (incorporating 45/39 walk-forward folds from 2023 to March 2026, and live execution auditing from May 28, 2026 to July 24, 2026) (`source-reported`).
- **Primary Source Integrity:** All quantitative figures, parameter bounds, failure rates, and code invariants below were extracted directly from the raw commit code and Markdown reports. No search snippets or secondary model summaries were used.

## Economic mechanism

### Source-reported

The classical theoretical premise of statistical arbitrage pairs trading is that economically linked assets share common stochastic trends; when their price spread diverges beyond equilibrium due to temporary liquidity shocks or retail overreaction, risk-neutral arbitrageurs step in, causing the spread to mean-revert to its long-run cointegrating relationship.

The primary author conducted a systematic 6-week research campaign and forensic self-audit that falsified the existence of actionable net alpha in this setup across S&P 500 equities. The author demonstrated that apparent historical profitability in cointegration pairs trading stems from three distinct methodological artifacts rather than genuine market inefficiency:
1. **Unbounded Hedge Ratio Artifact:** In unconstrained OLS or Johansen regressions, pairs with extreme betas ($|\beta| \gg 1$) disguise directional single-stock bets as market-neutral spreads. A tiny universe of numerical outliers accounts for over 100% of reported backtest gains.
2. **Phantom Kalman P&L Accounting Fiction:** When dynamic Kalman filters update the hedge ratio $\beta_t$ at each bar, calculating portfolio mark-to-market returns using the updated $\beta_t$ injects a spurious accounting drift term ($\Delta \beta_t \cdot b_t$) into the spread return. This creates an illusion of extraordinary Sharpe lift (+11.5 in initial tests) that completely disappears when P&L is accounted for using entry-locked hedge ratios.
3. **Cointegration Instability & Forced-Close Attrition:** The vast majority (75.2%) of statistically cointegrated pairs lose cointegration during the very 21-day trading window in which they are traded. Imposing calendar month-end force-closes liquidates 81% of positions at a substantial loss before mean reversion can complete.
4. **Regime Filter Overfitting:** Volatility and correlation regime filters that appear to improve backtest metrics (e.g., boosting mean fold Sharpe from 0.66 to 1.28 by halting 31% of months) suffer catastrophic false alarms during prospective live deployment, halting during profitable periods and incurring losses when active.

### Research interpretation

This study provides a definitive, end-to-end econometric falsification of classical cointegration pairs trading on large-cap US equities. The critical insight is that cointegration is a long-memory property ($I(1)$ levels with stationary $I(0)$ residuals) requiring substantial historical samples (12–24 months) to detect, but idiosyncratic equity relationships in modern electronic markets exhibit dynamic structural breaks. By the time a pair passes cointegration screening (even with Benjamini-Hochberg FDR control), the relationship is frequently at the end of its stationary regime.

Furthermore, the mathematical distinction between **signal generation** and **position accounting** in dynamic hedging is vital: a Kalman filter can validly update the perceived equilibrium level for trading signal Z-scores, but physical capital deployed at entry is committed at the initial hedge ratio. Updating the capital weighting post-entry requires physical rebalancing transactions; failing to account for those rebalancing cash flows converts mathematical re-labeling into phantom paper alpha.

## Signal

The strategy signal operates across two distinct architectures evaluated in the repository: the V4 Daily Production Engine and the Dynamic-Beta Kalman Variant.

### V4 Daily Production Engine (Locked Reference)

- **Formation Lookback:** 12 months (252 trading days), rolling monthly (`source-reported`).
- **Factor Projection:** 5-component PCA on universe return panel, Avellaneda-Lee style; residuals computed by orthogonalizing raw returns against the 5 PCA factors (`source-reported`).
- **Pair Discovery Screening:**
  - Pairwise Johansen trace test on PCA residual series (`source-reported`).
  - Multiple testing correction: Benjamini-Hochberg False Discovery Rate (BH-FDR) at $q = 0.05$ (`source-reported`).
  - Half-life filter: Ornstein-Uhlenbeck estimated half-life constrained to $HL \in [5, 30]$ trading days (`source-reported`).
  - Hedge ratio bound: $|\beta| \le 5.0$ hard constraint during discovery (`source-reported`). Pairs with $|\beta| > 5.0$ are rejected as numerical instabilities (`source-reported`).
- **Alpha Refit:** Static $\beta$ inherited from Johansen formation; constant $\alpha$ refit via OLS on the last 60 daily bars of formation residuals at the start of each trading month (`source-reported`).
- **Signal Formation:**
  - Spread calculation: $S_t = A_t - \alpha - \beta \cdot B_t$ (`source-reported`).
  - Residual handling: Path A re-anchor, where trading residual continues from the last formation value (`source-reported`).
  - Rolling Z-score: 60-day rolling window of $S_t$, initialized using the tail of the formation window (`source-reported`).
  - Z-score equation: $Z_t = \frac{S_t - \mu_{60}(S)}{\sigma_{60}(S)}$ (`source-reported`).
- **Entry Logic:**
  - Long Pair (Long A, Short B): $Z_t \le -3.0$ (`source-reported`).
  - Short Pair (Short A, Long B): $Z_t \ge +3.0$ (`source-reported`).
  - Timing: Close-to-close daily frequency; order generated on bar close, executed at next-day open or modeled daily close (`source-reported`).
- **Exit Logic:**
  - Mean-reversion take-profit: Zero-crossing exit at $Z_t = 0$ (`source-reported`).
  - Hard stop-loss: $|Z_t| \ge 5.0$ (immediate liquidation upon catastrophic divergence) (`source-reported`).
  - Calendar exit: Mandatory force-close at end-of-month (EOM) for any remaining open positions (`source-reported`).
- **Regime Filter:**
  - Composite Z-Score Simple Binary Halt: Compute trailing 252-day composite market stress metric (`source-reported`). If `stress_z(t*) > q_67` (67th percentile of trailing 252 days), halt all pair entries for the entire upcoming month (`source-reported`).

### Dynamic-Beta Kalman Architecture (Arm B1c_hl30)

- **State Space Model:**
  - Observation equation: $A_t = \alpha_t + \beta_t \cdot B_t + \epsilon_t$, $\epsilon_t \sim \mathcal{N}(0, R)$ (`source-reported`).
  - State transition equation: $\begin{bmatrix} \alpha_t \\ \beta_t \end{bmatrix} = \begin{bmatrix} \alpha_{t-1} \\ \beta_{t-1} \end{bmatrix} + \eta_t$, $\eta_t \sim \mathcal{N}(0, Q)$ (`source-reported`).
  - Noise parameterization: $R$ set to variance of formation OLS residuals; $Q = \delta \cdot R \cdot I_2$, with $\delta = \left(\frac{\ln 2}{HL_\beta}\right)^2$ (`source-reported`).
  - Target parameter: $HL_\beta = 30$ trading days ($\delta \approx 5.3 \times 10^{-4}$) (`source-reported`).
- **Kalman Guardrails (Arm B1c):**
  - Innovation outlier gate: Skip Kalman state update if measurement innovation $|\nu_t| > 4.0 \cdot \sigma_{innov}$ (Wang 2022 robust filter convention) (`source-reported`).
  - Posterior beta clamp: Enforce $\beta_{post, t} \in \left[\frac{\beta_{init}}{3.0}, 3.0 \cdot \beta_{init}\right]$ to prevent explosive filter divergence (`source-reported`).
- **Locked-Beta Accounting Invariant (Critical Architectural Separation):**
  - **Signal Spread (for Z-score):** $S_{signal, t} = A_t - \alpha_{prior, t} - \beta_{prior, t} \cdot B_t$ (`source-reported`).
  - **P&L Spread (for capital accounting):** $S_{pnl, t} = A_t - \alpha_{entry} - \beta_{entry} \cdot B_t$ (`source-reported`).
  - Positions are sized and settled strictly on $\beta_{entry}$ to eliminate phantom re-labeling P&L (`source-reported`).

## Required data

- **Universe:** S&P 500 equity universe (504 constituents in January 2022, expanding to 526 by March 2026) (`source-reported`).
- **Venues:** US National Market System (NMS) cash equities; Alpaca Paper Trading (IEX routing) for live deployment verification (`source-reported`).
- **Market Type:** Cash Equities (Long/Short margin accounts) (`source-reported`).
- **Timeframe:**
  - Primary production engine: Daily bars (close-to-close) (`source-reported`).
  - Intraday research and cost modeling: 1-minute OHLCV bars across standard regular trading hours (09:30–15:59 ET) (`source-reported`).
- **Fields Required:**
  - Price: Open, High, Low, Close (`source-reported`).
  - Volume: Bar trading volume (`source-reported`).
  - Microstructure Quote Panel: 1-minute L1 bid/ask prices and sizes (212,975,144 rows; modeled spread series calibrated to empirical levels) (`source-reported`).
- **Point-in-Time Integrity:**
  - Strict monthly walk-forward fold separation: 12-month formation window strictly precedes 1-month trading window (`source-reported`).
  - End-of-day execution: $t$ signal evaluated at daily close; execution occurs on next available print (`source-reported`).
- **Missing Data Handling:** Pairs with missing ticker data during the formation window or trading window are cleanly dropped from that fold's candidate set (`source-reported`).

## Execution assumptions

- **Order Types:** Market-on-Open (MOO) or immediate marketable limit orders executed at bar boundary (`source-reported`).
- **Dynamic Three-Component Friction Model:** Total cost $C_{total}(t) = C_{spread}(t) + C_{impact}(t) + C_{borrow}(t) + C_{comm}$ (`source-reported`):
  - **Half-Spread:** $C_{spread}(t) = \text{half\_spread\_l1\_bps}(t)$, varying by ticker and time of day (`source-reported`). Median L1 spread for Tier 1: ~10 bps; SPY: ~4.7 bps (`source-reported`).
  - **Market Impact:** $C_{impact}(t) = \kappa \cdot \text{spread\_std\_1d}(t)$ (`source-reported`).
    - Tight Liquidity Tier ($\kappa = 0.3$): Median spread $< 8$ bps (e.g., AAPL, MSFT, SPY) (`source-reported`).
    - Medium Liquidity Tier ($\kappa = 0.5$): Median spread 8–20 bps (majority of S&P 500) (`source-reported`).
    - Wide Liquidity Tier ($\kappa = 0.8$): Median spread $> 20$ bps (e.g., VTRS, T, UBER) (`source-reported`).
  - **Short Borrow Fee:** 50 bps annualized default rate accrued daily via calendar day convention: $\frac{0.0050}{365} \times \text{short\_notional}$ (`source-reported`).
  - **Brokerage Commission:** 2.0 bps per executed order ($4.0$ bps round-trip) (`source-reported`).
  - **Overall Round-Trip Cost:** Measured mean dynamic round-trip friction of 45.29 bps (against a naive flat benchmark of 90.87 bps) (`source-reported`).
- **Position Sizing:** Volatility-targeted sizing allocating $200/day expected dollar risk per pair, with a floor of $10,000 and a ceiling of $40,000 notional per pair (`source-reported`).
- **Live Paper Trading Fill Model:** Real-time Alpaca API paper broker execution on live IEX order book (`source-reported`).

## Evidence

### Source-reported

All quantitative performance claims trace directly to verified analysis logs and clean result files at commit `30311352348c0a4939c237b5ef57d57c353e29b8`:

1. **Unbounded Hedge Ratio Falsification:**
   - In unconstrained V4 backtesting across 39 folds, 27 outlier pairs with $|\beta| \in [50, 2708]$ generated 103% of total portfolio P&L (`source-reported`, `Week 6/documents/log.md`).
   - The single largest winning trade ran at $\beta = -24.04$ with both legs long, functioning as an unhedged directional semiconductor bet (`source-reported`).
   - Enforcing a realistic bound of $|\beta| \le 5.0$ collapsed the strategy's annualized Sharpe ratio from **+0.66 to −0.45**, and total compounded return from **+248.6% to −6.6%** (`source-reported`).
2. **Cointegration Lifetime & Trading Window Mismatch:**
   - Diagnostic testing revealed that **75.2% of selected pairs lost cointegration** during the very 21-day window in which they were traded (`source-reported`).
   - 77% of cointegrated pairs appeared in only a single 1-month fold (`source-reported`).
   - **81% of all trades were force-closed at month-end** prior to mean-reversion completion; this force-closed cohort lost $565,000, while the 10% of trades that successfully completed zero-crossing reversion earned $541,000 (`source-reported`).
3. **Phantom Kalman P&L Accounting Bug:**
   - An unconstrained per-bar Kalman filter (updating $\beta_t$ dynamically) initially produced a spurious mean fold Sharpe lift of **+11.5 across 6/6 test folds** (`source-reported`, `Week 6/scripts/research/dynamic_beta/FINAL_FINDINGS.md`).
   - Auditing confirmed that computing portfolio P&L using dynamic $\beta_t$ booked phantom returns $\Delta \beta_t \cdot B_t$ from hedge-ratio re-labeling (`source-reported`).
   - When corrected to entry-locked P&L accounting ($S_{pnl} = A_t - \alpha_{lock} - \beta_{lock} \cdot B_t$), the Sharpe lift collapsed to +0.54 at $HL=10$, and +1.48 at $HL=30$ across 39 folds (`source-reported`).
   - Bootstrap 95% confidence interval on the Sharpe lift spanned zero (range −5 to +7) due to high per-fold return variance (`source-reported`).
4. **Deliberate Look-Ahead Bias Injection Experiments (Week 3):**
   - 4 bias mechanisms evaluated across 6 contamination levels (5% to 50%) totaling 24 flawed datasets (`source-reported`, `Week 3/README.md`):
     - **H1 (Future Close Leakage):** Only method that artificially inflated Sharpe under zero-cost conditions (`source-reported`).
     - **H2 (Timestamp Backdating), H3 (Spread-Level Lead), H4 (Full-Sample Normalization Leak):** All decreased Sharpe under realistic transaction costs (`source-reported`).
     - Normalization leak (H4) caused 47% of prices to become negative, corrupting cointegration rather than inflating alpha (`source-reported`).
5. **Overfitting Diagnostics (Week 5):**
   - Across 50 evaluated strategy variants, the expected maximum Sharpe under null hypothesis $E[\max(SR)] = 2.05$ (Bailey & López de Prado 2014) (`source-reported`).
   - Observed gross Sharpe of 0.5031 and dynamic net Sharpe of 0.4428 yielded a Deflated Sharpe Ratio (DSR) p-value of **0.0000 across all regimes**, failing statistical significance screens (`source-reported`, `Week 5/reports/net_of_fees_report.md`).
   - Probability of Backtest Overfitting (PBO) was measured at 12.3% (`source-reported`).
   - Static negative control pairs passed in 36.4% of folds (8 of 22 folds), failing as a discriminant false-positive screen (`source-reported`).
6. **Live Deployment Falsification (Week 6):**
   - Deployed on Alpaca paper trading from 2026-05-28 to 2026-07-24 (`source-reported`).
   - First week produced 5 trades, all force-closed at month-end, losing **−$313.05** on a $100,000 account (`source-reported`).
   - Cumulative paper trading P&L reached **−$457.99** before 13 consecutive sessions were frozen by a stale-reconciliation state halt (`source-reported`). Engine was permanently stopped (`source-reported`).
   - Regime filter live failure: In historical backtesting, the composite stress filter yielded +1.279 mean fold Sharpe; when replayed live across April–July 2026, the filter lost **−$1,189**, whereas trading unfiltered generated **+$11,304** (`source-reported`).

### Independently reproduced

Not independently reproduced. All empirical results, metrics, and diagnostic logs represent primary-source findings from the repository audit.

### Negative evidence

- Unconstrained cointegration pairs trading is completely unviable after removing extreme beta leverage artifacts ($|\beta| \le 5.0$ reduces total return to −6.6%).
- 75.2% of cointegrated relationships break down within 21 trading days, causing massive month-end forced liquidation losses.
- Dynamic Kalman filtering introduces severe accounting vulnerabilities; without entry-locked P&L invariants, paper returns are dominated by phantom re-labeling gains.
- Real-time live execution encountered state reconciliation freezes and negative net P&L.
- Walk-forward composite regime filters demonstrated severe out-of-sample fragility, suppressing profitable trading months and participating in drawdown months.

## Falsification plan

To establish whether any modified variant of equity cointegration stat-arb can generate true positive expectancy, an independent research system must evaluate:
1. **Mandatory Beta Boundary:** Enforce a strict pre-trade filter $|\beta| \le 2.0$ (`research-defined falsification threshold`). If the strategy's gross Sharpe fails to exceed 0.0 under $|\beta| \le 2.0$, reject the cointegration thesis entirely.
2. **Dynamic Holding Period / Carry-Forward Verification:** Replace arbitrary calendar month-end force-closes with cointegration persistence testing at fold boundaries (Johansen $p < 0.05$ on updated rolling window) (`research-proposed`). If zero-crossing completion remains below 40% (`research-defined falsification threshold`), confirm that stationary duration is insufficient to amortize execution costs.
3. **Locked-Beta Accounting Audit:** Implement unit invariant assertions verifying that `pnl[t] == a[t] - alpha_entry - beta_entry * b[t]` on every bar (`research-proposed`). If any dynamic filter updates capital weights without booking explicit rebalance transactions, fail the backtest immediately.
4. **Out-of-Sample Prospective Gate:** Require minimum 6 months of prospective, live forward-paper execution without human intervention (`research-proposed`). Rejection threshold: cumulative net P&L $< 0$ after 50 completed round-trip trades (`research-defined falsification threshold`).

## Crypto portability

**Adapted / Unproven.** The primary source investigates US cash equities exclusively. Porting this cointegration stat-arb architecture to cryptocurrency markets represents a theoretical adaptation (`research-proposed`):

Crypto-specific operational and structural friction differences:
1. **Perpetual Basis vs Cointegration:** In crypto perpetual futures, synthetic pairs (e.g., SOL/USDT vs AVAX/USDT) rarely share true cointegration; apparent co-movements are dominated by Bitcoin market-wide beta and liquidity regime shifts.
2. **Funding Rate Carry Asymmetry:** Holding an unhedged cointegrated pair for multi-day horizons incurs continuous 8-hour funding rate payments. If the long leg is in positive funding and the short leg is in negative funding, the net funding drag rapidly erodes any statistical reversion margin.
3. **Margin Non-Fungibility & Cross-Liquidation:** On crypto exchanges, isolated margin accounts or asymmetric leverage liquidation cascades can liquidate one leg during sudden market spikes, leaving an unhedged directional exposure.
4. **24/7 Session Structure:** Unlike equity markets with 09:30 open spread widening and 16:00 close auctions, crypto liquidity operates 24/7 with weekend liquidity thinning and sudden weekend basis divergence.
5. **Portability Classification:** `unproven`. Unless verified on cointegrated spot/perpetual basis pairs with explicit funding-cost accounting, equity pairs trading methodology must not be assumed viable in crypto.

## Limitations

- **Simulated Microstructure Depth:** The 213M-row order book panel used for cost modeling was constructed from 1-minute close prices plus a modeled spread series with synthetic L2/L3 levels; it is not vendor-measured raw tick depth (`source-reported`).
- **Short Live Sample:** The live Alpaca paper trading deployment spanned only two months (May 28, 2026 to July 24, 2026) with 5 initial trades before engine shutdown (`source-reported`).
- **Survivorship Bias:** Universe construction used trailing S&P 500 membership lists (504–526 tickers), introducing mild survivorship bias estimated by the author at approximately −0.20 Sharpe drag (`source-reported`).
- **High Parameter Variance:** Dynamic Kalman beta comparisons exhibited wide bootstrap 95% confidence intervals spanning zero across the 39 folds (`source-reported`).

## Implementation status

`not-implemented`. This record captures research and forensic falsification findings only. No code or configuration has been implemented in PyBroker, NautilusTrader, paper trading, testnet, or live production environments.

## Adoption boundary

`research-only`. This record is cataloged strictly for research documentation, risk control design, and algorithmic falsification awareness. It does **not** authorize implementation, paper trading, testnet deployment, or live capital allocation.

## Related Wiki records

- `[[statistical-arbitrage-methodology-degradation-ladder-falsification-2026-09-12]]` — Grant J. Kim's 8-rung degradation ladder isolating look-ahead bias and O-U half-life proxy effects.
- `[[pairs-trading-adf-stationarity-filter-walk-forward-falsification-2026-09-12.md]]` — Walk-forward ADF filtering across ETF pairs demonstrating formation-window variance compression.
- `[[johansen-cointegration-etf-pairs-friction-asymmetry-falsification-2026-09-12.md]]` — Multi-asset Johansen cointegration with execution friction asymmetry.
- `[[crypto-perpetual-pairs-trading-kalman-cointegration-falsification-2026-09-11]]` — One-sided Kalman filtering on crypto perpetuals.
- `[[retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11]]` — Microstructure and order flow signal decay under realistic costs.

## Sources

1. **Primary Source Codebase:** Duy Anh Nguyen (`Duyanh090205`), *Pairs Trading Engine: Statistical arbitrage pipeline that found no edge*, GitHub repository `Duyanh090205/pairs-trading-engine`, commit `30311352348c0a4939c237b5ef57d57c353e29b8`, September 10, 2026. Stable URL: [https://github.com/Duyanh090205/pairs-trading-engine](https://github.com/Duyanh090205/pairs-trading-engine).
2. **Core Audit Logs & Documentation:**
   - Root README and Retraction Notices: `README.md`
   - Week 6 Production & Audit Log: `Week 6/documents/log.md`
   - Dynamic Beta Findings: `Week 6/scripts/research/dynamic_beta/FINAL_FINDINGS.md`
   - Dynamic Beta Implementation & Tests: `Week 6/scripts/research/dynamic_beta/arms.py`, `Week 6/scripts/research/dynamic_beta/audit_b1.py`
   - Look-Ahead Bias Experiments: `Week 3/README.md`
   - Dynamic Cost & Overfitting Report: `Week 5/reports/net_of_fees_report.md`
   - Paper Trading Reconciliation: `Week 6/submission_data/`
