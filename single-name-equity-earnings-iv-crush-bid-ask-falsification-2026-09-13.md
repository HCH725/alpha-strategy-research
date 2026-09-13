---
schema: strategy-research-record-v1
title: "Single-Name Equity Earnings Implied Volatility Crush: Empirical Falsification of Pre-Earnings Implied Volatility Overstatement Against Quoted Option Spreads and Tail Jump Risk"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equity-options
  - earnings-announcements
  - implied-volatility-crush
  - straddle-selling
  - bid-ask-spread
  - falsification
  - negative-results
  - jump-risk
status: research-only
confidence: high
source_as_of: 2026-09-08
sources:
  - "JonathanBeck1, 'A pre-registered falsification campaign across ~50 trading-strategy families — and the negative result it produced', GitHub repository 'JonathanBeck1/falsification-campaign', commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63, accessed 2026-09-13. https://github.com/JonathanBeck1/falsification-campaign"
  - "Primary audit decision record: JonathanBeck1, 'Decision: Single-Name Earnings IV Crush (T23)', research/earnings_iv_crush_decision.md (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/earnings_iv_crush_decision.md"
  - "Primary pre-registration: JonathanBeck1, 'Pre-registration — T23 Single-Name Earnings IV Crush', research/earnings_iv_crush_preregistration.md (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/earnings_iv_crush_preregistration.md"
  - "Primary empirical code: JonathanBeck1, 'src/trader/catalysts/earnings_iv_crush.py', 'scripts/run_earnings_iv_crush_study.py', and 'tests/financial/test_earnings_iv_crush.py' (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63)"
  - "Primary research synthesis: JonathanBeck1, 'The negative result: an empirical falsification of retail-accessible trading edges', research/PAPER_DRAFT.md, Section 7.2 and 7.5 (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/PAPER_DRAFT.md"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Single-Name Equity Earnings Implied Volatility Crush: Empirical Falsification of Pre-Earnings Implied Volatility Overstatement Against Quoted Option Spreads and Tail Jump Risk

## Provenance

- **Repository:** `https://github.com/JonathanBeck1/falsification-campaign` (`source-reported`).
- **Author / Research Lab:** Jonathan Beck (`JonathanBeck1`) (`source-reported`).
- **Canonical Immutable Commit SHA:** `79c3a2a21600cd3a0f9e242de5ce15173f512c63` (`source-reported`).
- **Commit Date:** 2026-09-08T21:47:53Z (`source-reported`).
- **Source As-Of Date:** 2026-09-08 (`source-reported`).
- **Primary Source Documents & Code Directly Audited:**
  - `research/earnings_iv_crush_preregistration.md`: Pre-registered research design establishing the hypothesis, universe of 24 mega-caps, put-call parity spot anchoring, event selection, controls (implied-vs-realized move decomposition, jump-variance correlation, non-earnings placebo), friction model (crossing quoted bid/ask + commission), 7-point gate, and kill criteria (`source-reported`).
  - `research/earnings_iv_crush_decision.md`: Decision record detailing the `KILL` verdict, full after-cost metrics across 414 events, gross crush gap decomposition, in-sample vs. out-of-sample breakdown, non-earnings placebo comparison, and tail loss analysis (`source-reported`).
  - `src/trader/catalysts/earnings_iv_crush.py`: Pure Python core implementing put-call parity spot anchoring (`parity_spot`), ATM strike selection (`atm_strike`), front-expiration selection (`select_front_expiration`), honest bid/ask straddle pricing (`straddle_quote`), event P&L computation (`compute_crush_event`), cohort aggregation (`aggregate`), tail reporting (`tail_report`), and gate evaluation (`evaluate_gate`) (`source-reported`).
  - `tests/financial/test_earnings_iv_crush.py`: 27 network-free unit tests asserting parity spot recovery, ATM selection, bid/ask execution mechanics, tail reporting, and gate evaluation (`source-reported`).
  - `scripts/run_earnings_iv_crush_study.py`: End-to-end runner orchestrating the study on the ThetaData EOD option lake and yfinance earnings calendars (`source-reported`).
  - `research/PAPER_DRAFT.md`: Research paper detailing the 39-family falsification campaign, positioning single-name option surface tests (§7.2, §7.5) within the Class 2 friction-scale taxonomy (`source-reported`).
- **Underlying Sample & Universe:** 24 mega-cap US equity underlyings: `AAPL`, `ADBE`, `AMAT`, `AMD`, `AMZN`, `AVGO`, `BKNG`, `COST`, `CSCO`, `GOOGL`, `HON`, `INTU`, `ISRG`, `LIN`, `LRCX`, `META`, `MU`, `NFLX`, `NVDA`, `PEP`, `QCOM`, `REGN`, `TMUS`, `TSLA`, `TXN`, `VRTX` (with `GOOG` omitted to prevent dual-class double-counting) across the 2022-01-03 to 2026-06-12 ThetaData EOD option lake (~1,115 trade days per name) (`source-reported`).
- **Usable Events:** 414 scheduled corporate earnings announcements with valid pre-earnings and post-earnings front straddles across all 24 names (`source-reported`).
- **Subperiods:** In-Sample (IS): 2022–2023 ($N = 183$); Out-of-Sample (OOS): 2024–2026 ($N = 231$) (`source-reported`).
- **Primary Venues:** US consolidated equity options exchanges (OPRA / Cboe / Nasdaq PHLX) via ThetaData EOD Option Lake (`source-reported`).
- **Repository Deduplication Audit:** A full grep across all existing strategy records in `alpha-strategy-research` confirmed zero prior records citing `JonathanBeck1`, commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`, single-name earnings IV crush, or pre-earnings straddle selling. Existing options records in the repository (`transformer-ddqn-straddle-option-volatility-trading-2026-09-05.md`, `spy-options-svi-surface-rv-falsification-adverse-selection-2026-09-12.md`, `spxw-0dte-vrp-learning-to-rank-2026-09-01.md`, `qqq-options-microstructure-ensemble-volatility-targeted-2026-09-04.md`) focus on index options or RL/SVI modeling, with no empirical evaluation of single-name earnings event volatility crush or option bid-ask friction.

## Economic mechanism

### Source-reported

1. **The Implied Volatility Overstatement Hypothesis:**
   - Prior to corporate earnings releases, equity option markets price heightened uncertainty, driving implied volatility (IV) sharply upward.
   - Retail lore and quantitative literature often hypothesize that pre-earnings at-the-money (ATM) implied volatility systematically overstates the subsequent realized overnight stock move ($\mathbb{E}[\text{priced move}] > \mathbb{E}[\text{realized move}]$).
   - Under this hypothesis, selling an ATM straddle (short call + short put) at the market close immediately preceding the scheduled earnings release and buying it back at the close immediately following the release should capture the "crush gap" as implied volatility collapses back toward baseline levels.

2. **The Falsification Findings:**
   - **The Gross Discrepancy is Real:** Across 414 events, the mean priced move (straddle mid divided by pre-announcement spot) is $7.06\%$, whereas the mean realized move ($|\text{post\_spot}/\text{pre\_spot} - 1|$) is only $5.47\%$. This leaves a positive gross crush gap of $+1.59\%$ of spot (median $+1.92\%$). Pre-earnings ATM IV genuinely overstates the average move.
   - **Execution Friction Erases the Edge:** Single-name option quoted bid-ask spreads are wide. Selling the straddle requires hitting the bid on both legs ($C_{\text{bid}} + P_{\text{bid}}$); buying back the straddle requires paying the ask on both legs ($C_{\text{ask}} + P_{\text{ask}}$). Crossing this two-sided spread twice plus standard brokerage commissions ($\$0.65$/contract/leg) consumes the entire $+1.59\%$ gross gap, transforming the net return into a statistically significant loss of $-0.593\%$ of spot ($t = -3.61$).
   - **Compensated Jump Variance, Not Alpha:** The return of the short straddle is heavily negatively correlated with the realized stock move ($\text{corr}(\text{P\&L}, \text{realized move}) = -0.843$). The losses are concentrated in extreme earnings gap events (e.g., Netflix $-23.2\%$, Broadcom $-16\%$, Meta $-14\%$). The gross premium is merely risk compensation demanded by option sellers for underwriting catastrophic jump risk.
   - **No Earnings-Specific Alpha Over Plain Short Volatility:** A non-earnings placebo test (selling a one-day straddle on random non-earnings dates across the same names, $N = 720$) yields $-0.448\%$ ($t = -13.18$). The earnings premium over the placebo is $-0.146\%$ (Welch $t = -0.87$), indicating that pre-earnings straddle selling does not outperform unconditional short-volatility exposure.

### Research interpretation

- The empirical results from JonathanBeck1 illustrate two fundamental failure modes in derivative alpha discovery: **Class 2 (Friction-Scale Signal Sign-Flip)** and **Class 7 (Compensated Jump Risk / Beta-in-Disguise)**.
- Evaluating option trading strategies using midpoint marks ($\text{mid} = (\text{bid} + \text{ask})/2$) manufactures an optical illusion of profitability. In single-name equities, the quoted bid-ask spread on front-month options represents $2\%$ to $5\%$ of underlying stock value across the four executed legs. The gross mispricing ($+1.59\%$) is smaller than the cost of liquidity immediacy.
- Market makers widen option spreads ahead of earnings specifically to protect against informed adverse selection and post-announcement gap risk. A liquidity taker crossing quoted spreads pays a structural penalty that exceeds the theoretical variance premium.
- Even if bid-ask spreads were partially mitigated through passive execution, the payoff distribution exhibits severe negative skewness: the five worst events destroy $-81.5\%$ of spot across the sample. Selling event volatility functions as a negative-skewed lottery ticket where occasional large shocks overwhelm regular small gains.

## Signal

- **Universe:** 24 mega-cap US equities (`source-reported`).
- **Entry Timing:** Market close ($16:00$ US/Eastern) on the trading day immediately prior to the earnings release (`source-reported`).
  - For After-Market-Close (AMC, scheduled $\ge 13:00$ ET or timestamp missing) announcements, entry is the close of the announcement date (`source-reported`).
  - For Before-Market-Open (BMO, scheduled $< 13:00$ ET) announcements, entry is the close of the preceding trading date (`source-reported`).
- **Exit Timing:** Market close ($16:00$ US/Eastern) on the first trading day on or after the session that prices the release (`source-reported`).
- **Holding Period:** Exactly 1 overnight session / 1 trading day (`source-reported`).
- **Front Expiration Filter:** Nearest available expiration date with calendar days to expiry $\ge 5$ days on the entry close (`MIN_FRONT_DAYS = 5`) that also exists in the post-earnings chain shard (`source-reported`). This avoids same-day 0DTE pin artifacts while remaining short-tenor enough to be event-dominated (`source-reported`).
- **Put-Call Parity Spot Anchor:** To prevent split-adjusted price mismatches against unadjusted historical option strikes, underlying spot $S$ is derived directly from contemporaneous option quotes via put-call parity:
  $$S \approx K^* + (C_{\text{mid}}(K^*) - P_{\text{mid}}(K^*))$$
  evaluated at the strike $K^*$ where $|C_{\text{mid}} - P_{\text{mid}}|$ is minimized across all two-sided strikes (`source-reported`).
- **ATM Strike Selection:** Strike $K$ closest to the parity-derived spot $S$ that carries two-sided quotes ($\text{bid} > 0, \text{ask} > 0$) for both call and put legs (`source-reported`).
- **Execution Order (Short Straddle):**
  - Entry: Sell 1 ATM call at $\text{call\_bid}$ and sell 1 ATM put at $\text{put\_bid}$ (`source-reported`).
    $$\text{sell\_proceeds} = C_{\text{bid}} + P_{\text{bid}}$$
  - Exit: Buy back 1 ATM call at $\text{call\_ask}$ and buy back 1 ATM put at $\text{put\_ask}$ (`source-reported`).
    $$\text{buy\_cost} = C_{\text{ask}} + P_{\text{ask}}$$
- **Return Calculation:**
  $$\text{Gross P\&L per share} = \text{sell\_proceeds} - \text{buy\_cost}$$
  $$\text{After-Cost Return} = \frac{\text{Gross P\&L per share}}{S_{\text{pre}}} - \frac{\text{Commission}}{S_{\text{pre}} \times 100}$$
  where $\text{Commission} = \$2.60$ per straddle round trip ($\$0.65$/leg $\times 2$ legs $\times 2$ open/close) (`source-reported`).
- **Outlier Filter:** Events with $|\text{after-cost return}| > 2.0$ ($200\%$ of underlying spot) are discarded as chain mispricing/data glitches (`MAX_ABS_EVENT_RETURN = 2.0`) (`source-reported`).
- **Position Sizing:** In the primary empirical study, trades are evaluated on a per-event percentage return normalized by spot (`source-reported`). Portfolio sizing across concurrent announcements (e.g., equal dollar notional or inverse-volatility weighting) is `research-proposed`.

## Required data

- **Instrument:** US single-name equity options and underlying common stocks (`source-reported`).
- **Universe:** 24 liquid US mega-cap equities: `AAPL`, `ADBE`, `AMAT`, `AMD`, `AMZN`, `AVGO`, `BKNG`, `COST`, `CSCO`, `GOOGL`, `HON`, `INTU`, `ISRG`, `LIN`, `LRCX`, `META`, `MU`, `NFLX`, `NVDA`, `PEP`, `QCOM`, `REGN`, `TMUS`, `TSLA`, `TXN`, `VRTX` (`source-reported`).
- **Venue:** US consolidated equity options markets via ThetaData EOD Option Lake (`source-reported`).
- **Market Type:** American-style physical delivery equity options (`source-reported`).
- **Timeframe:** End-of-Day (EOD) daily closing quotes (`source-reported`).
- **Fields:** `trade_date`, `expiration`, `strike`, `right` (C/P), `bid`, `ask`, `close`, `volume`, `open_interest` (`source-reported`).
- **Earnings Calendar:** Corporate earnings announcement dates and scheduled hours (AMC vs. BMO) obtained via yfinance (`source-reported`).
- **Point-in-Time Availability:** Earnings dates are pre-scheduled weeks in advance, ensuring causal entry at the pre-earnings close without look-ahead bias (`source-reported`). Option quotes and spot approximations use only data available at the respective close (`source-reported`).
- **Missing Data Handling:** Quotes with $\text{bid} \le 0$, $\text{ask} \le 0$, or $\text{mid} \le 0$ are rejected (`source-reported`). Events lacking two-sided quotes for both legs at entry or exit are discarded without imputation (`source-reported`).

## Execution assumptions

- **Execution Timing:** Pre-earnings close entry to post-earnings close exit (1 overnight hold) (`source-reported`).
- **Order Type:** Liquidity-taking market orders crossing the quoted bid-ask spread (`source-reported`).
- **Fill Pricing:** Sells executed at prevailing $\text{bid}$; buys executed at prevailing $\text{ask}$ (`source-reported`).
- **Slippage / Spread:** Quoted two-sided half-spread crossed on all four transaction legs (`source-reported`).
- **Commission:** Fixed fee of $\$0.65$ per contract leg ($\$2.60$ total round trip per straddle) (`source-reported`).
- **Margin / Financing:** Requires portfolio margin or reg-T margin for short straddles; margin interest and assignment financing are omitted by the source (`source-reported`) and classified as `research-proposed`.
- **Borrow / Shorting:** Cash-settled or covered delivery assumed; physical assignment risk on deep-ITM short options is not modeled by the source (`source-reported`) and classified as `research-proposed`.
- **Capacity:** Constrained by quoted depth in single-name options; executable at retail sizing (1–10 contracts), but subject to severe market impact at institutional scale (`research-proposed`).

## Evidence

### Source-reported

- **Sample Size:** 414 usable earnings announcements across 24 names between January 2022 and June 2026 (`source-reported`).
- **Priced vs. Realized Move Decomposition:**
  - Mean Priced Move: $7.06\%$ of spot (`source-reported`).
  - Mean Realized Move: $5.47\%$ of spot (`source-reported`).
  - Mean Crush Gap: $+1.59\%$ of spot (median $+1.92\%$) (`source-reported`).
- **After-Cost Performance (Quoted Bid/Ask Fills + Commission):**
  - Mean Return: $-0.593\%$ of spot (`source-reported`).
  - $t$-statistic: $-3.61$ (`source-reported`).
  - Median Return: $-0.040\%$ of spot (`source-reported`).
  - Win Rate: $49.3\%$ (`source-reported`).
  - Sharpe Ratio (per event): $-0.177$ (`source-reported`).
- **Subperiod Breakdown:**
  - In-Sample (2022–2023, $N = 183$): Mean $-0.397\%$ of spot, $t = -1.61$ (`source-reported`).
  - Out-of-Sample (2024–2026, $N = 231$): Mean $-0.749\%$ of spot, $t = -3.41$ (`source-reported`).
  - Both subperiods are consistently negative, confirming that the loss is stable and not a single-year regime anomaly (`source-reported`).
- **Mechanism and Placebo Controls:**
  - Jump-Variance Correlation: $\text{corr}(\text{P\&L}, \text{realized move}) = -0.843$ (`source-reported`).
  - Non-Earnings Placebo (1-day short straddle on random non-earnings dates, $N = 720$): Mean $-0.448\%$, $t = -13.18$ (`source-reported`).
  - Earnings Premium Over Placebo: Mean $-0.146\%$, Welch $t = -0.87$ ($p > 0.05$) (`source-reported`). The short straddle around earnings fails to outperform unconditional short-volatility carry.
- **Tail Risk and Loss Distribution:**
  - Worst Single Event: Netflix (`NFLX`) on 2022-04-19: $-23.2\%$ of spot (`source-reported`).
  - Sum of 5 Worst Events: $-81.5\%$ of spot (`source-reported`).
  - Mean Return Excluding 5 Worst Events: $-0.401\%$ of spot (`source-reported`).
  - `deaths_dominate`: False, because the strategy is unprofitable on average even when the 5 catastrophic jump events are completely removed from the sample (`source-reported`).

### Independently reproduced

- Not independently reproduced.

### Negative evidence

- The primary source documents a definitive negative result: pre-earnings implied volatility crush does not produce a viable trading strategy for liquidity takers.
- Quoted option spreads turn a $+1.59\%$ theoretical gross crush gap into a $-0.593\%$ net loss ($t = -3.61$).
- Negative skewness and extreme jump risk make the unhedged short straddle an uncompensated risk-premium harvest.

## Falsification plan

- **Pre-Registered Falsification Criteria (JonathanBeck1 T23 Gate):**
  - Usable sample size $N \ge 30$ (`source-reported`).
  - After-cost mean $> 0$ with $|t| \ge 2.0$ (`source-reported`).
  - Out-of-sample sign stability ($N \ge 10$ in IS and OOS, matching signs) (`source-reported`).
  - Earnings premium over non-earnings placebo at Welch $t \ge 2.0$ (`source-reported`).
  - Tail risk inspection: strategy must not depend on survivorship or suppressing tail losses (`source-reported`).
- **Gate Evaluation Outcomes:**
  - $N = 414 \ge 30$: `PASS` (`source-reported`).
  - After-cost mean $-0.593\%$, $t = -3.61$: `FAIL` (`source-reported`).
  - OOS sign stability: `PASS` perversely (stably negative across IS and OOS) (`source-reported`).
  - Placebo outperformance: Welch $t = -0.87 < 2.0$: `FAIL` (`source-reported`).
  - Overall Verdict: `KILL` (`source-reported`).
- **Research-Defined Falsification Thresholds for Candidate Variants:**
  - *Passive Midpoint Quoting Hypothesis:* If a researcher asserts that selling at the midpoint eliminates spread drag, the strategy must demonstrate a simulated or empirical fill rate $\ge 60\%$ on both legs without adverse selection exceeding $+0.50\%$ of spot, or the passive execution variant is killed (`research-defined falsification threshold`).
  - *Delta-Neutral Straddle Hedging Hypothesis:* If dynamic intraday delta-hedging is proposed to mitigate jump risk, after-cost returns including hedging transaction costs must achieve $t \ge 2.0$, or the hedged variant is killed (`research-defined falsification threshold`).
  - *Cross-Sectional IV Rank Screening:* If conditioning on extreme implied-to-realized volatility ratios is proposed, the filtered sub-cohort must achieve an out-of-sample after-cost $t \ge 2.0$ under Benjamini-Hochberg FDR control ($q \le 0.05$), or the screening rule is killed (`research-defined falsification threshold`).

## Crypto portability

- **Portability Classification:** `unproven` / `adapted` (`research-proposed`).
- **Structural Differences:**
  - Corporate earnings announcements do not exist in cryptocurrency assets (`research-proposed`).
  - Structural analogues in crypto include scheduled token unlocks, protocol hard forks, major network upgrades (e.g., Ethereum Dencun), and macroeconomic data releases (CPI/FOMC) (`research-proposed`).
- **Derivatives Market Structure:**
  - Crypto options liquidity is heavily concentrated in Deribit BTC and ETH contracts, with negligible or fragmented liquidity in altcoin options (`research-proposed`).
  - Quoted bid-ask spreads on Deribit altcoin or short-dated contracts are substantially wider than US equity mega-cap option spreads, typically exceeding $5\%$ to $15\%$ of contract premium (`research-proposed`).
  - Continuous 24/7 trading prevents clean "overnight" market closure captures; price discovery occurs continuously, and post-announcement volatility repricing can trigger sudden liquidation cascades on perpetual swap venues (`research-proposed`).
- **Porting Verdict:** Directly porting pre-event straddle selling to crypto options would encounter even more punitive bid-ask friction and unbounded liquidation tail risk than observed in US equities (`research-proposed`).

## Limitations

- **Holding Period Scope:** Evaluates only a single overnight hold (pre-close to post-close); multi-day post-earnings volatility decay dynamics were not evaluated (`source-reported`).
- **Universe Concentration:** Evaluates 24 US mega-cap equities; smaller-cap equities with lower liquidity and wider spreads are expected to face even higher execution drag (`source-reported`).
- **Execution Modeling:** Assumes $100\%$ liquidity-taking fills at quoted bid and ask prices; potential price improvement inside the spread was not modeled (`source-reported`).
- **Intraday Timing:** Uses daily EOD close marks; intraday timing optimizations (e.g., entering in the final 5 minutes of trading or exiting at the opening print) were not tested (`source-reported`).
- **Financing and Assignment:** Excludes option margin financing costs and early assignment friction on deep-ITM short options (`source-reported`).

## Implementation status

- `not-implemented`.
- No prototype or production implementation exists in PyBroker, NautilusTrader, paper trading, testnet, or live trading systems. Research capture only.

## Adoption boundary

- `not-approved`.
- `approval_scope: research-only`.
- A strategy record being present here does not constitute authorization for trading, implementation, or deployment. The empirical findings establish an explicit negative result and falsification.

## Related Wiki records

- `[[quant/option-implied-surface-cremers-weinbaum-skew-crash-regimes-2026-09-02]]`
- `[[quant/qqq-options-microstructure-ensemble-volatility-targeted-2026-09-04]]`
- `[[quant/spy-options-svi-surface-rv-falsification-adverse-selection-2026-09-12]]`
- `[[quant/spxw-0dte-vrp-learning-to-rank-2026-09-01]]`
- `[[quant/retail-signal-three-gate-falsification-oscillator-volume-calendar-trend-2026-09-04]]`

## Sources

- JonathanBeck1, *A pre-registered falsification campaign across ~50 trading-strategy families — and the negative result it produced*, GitHub repository `JonathanBeck1/falsification-campaign`, commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`, accessed 2026-09-13. URL: `https://github.com/JonathanBeck1/falsification-campaign`
- JonathanBeck1, *Decision: Single-Name Earnings IV Crush (T23)*, `research/earnings_iv_crush_decision.md`, commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`. URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/earnings_iv_crush_decision.md`
- JonathanBeck1, *Pre-registration — T23 Single-Name Earnings IV Crush*, `research/earnings_iv_crush_preregistration.md`, commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`. URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/earnings_iv_crush_preregistration.md`
- JonathanBeck1, *Python Implementation Core and Unit Tests*, `src/trader/catalysts/earnings_iv_crush.py` and `tests/financial/test_earnings_iv_crush.py`, commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`.
- JonathanBeck1, *The negative result: an empirical falsification of retail-accessible trading edges*, `research/PAPER_DRAFT.md`, Section 7.2 and 7.5, commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`. URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/PAPER_DRAFT.md`
