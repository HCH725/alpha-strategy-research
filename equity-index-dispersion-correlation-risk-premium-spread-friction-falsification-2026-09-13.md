---
schema: strategy-research-record-v1
title: "Equity Index Dispersion and Correlation Risk Premium: Realized Spread Friction Falsification in QQQ Options"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - options
  - dispersion-trading
  - correlation-risk-premium
  - volatility-arbitrage
  - qqq
  - empirical-falsification
  - negative-result
  - friction-scale-noise
status: research-only
confidence: medium
source_as_of: 2026-06-17
sources:
  - "https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/brain/decisions/2026-06-17-index-dispersion-kill.md"
  - "https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/index_dispersion_preregistration.md"
  - "https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/src/trader/catalysts/index_dispersion.py"
  - "https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/tests/financial/test_index_dispersion.py"
  - "https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/scripts/run_index_dispersion_study.py"
  - "https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/PAPER_DRAFT.md"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Equity Index Dispersion and Correlation Risk Premium: Realized Spread Friction Falsification in QQQ Options

## Provenance

- **Primary Repository:** `https://github.com/JonathanBeck1/falsification-campaign`
- **Full Commit SHA:** `79c3a2a21600cd3a0f9e242de5ce15173f512c63`
- **Author:** Jonathan Beck (`JonathanBeck1`), independent quantitative researcher
- **Primary Source Documents:**
  - Decision Record: `brain/decisions/2026-06-17-index-dispersion-kill.md` (`source-reported` empirical decision memo for strategy family T22)
  - Pre-Registration Specification: `research/index_dispersion_preregistration.md` (`source-reported` pre-analysis plan frozen prior to empirical execution)
  - Pure Pricing & Allocation Engine: `src/trader/catalysts/index_dispersion.py` (`source-reported` pure core implementing implied/realized correlation inversion, Black-Scholes vega-neutral allocation, and gate diagnostics)
  - Test Suite: `tests/financial/test_index_dispersion.py` (`source-reported` 19 deterministic unit tests for mathematical correctness and split protections)
  - Study Runner: `scripts/run_index_dispersion_study.py` (`source-reported` execution script evaluating ThetaData option quotes)
  - Research Synthesis: `research/PAPER_DRAFT.md` (Sections 1, 4.2, 7) and `research/CAMPAIGN_SCOREBOARD.md`
- **Historical Data Core:** ThetaData End-of-Day (EOD) National Best Bid and Offer (NBBO) option quote database covering QQQ and 26 constituent equities from 2022-01-03 through 2026-06-12.
- **Deduplication Audit:** Full text search across all existing records in `alpha-strategy-research` confirmed zero prior records addressing equity index dispersion trading, correlation risk premium harvesting in US equities, or strategy family T22. Adjacent option records (`crypto-options-implied-correlation-dispersion-2026-08-31.md`, `cross-asset-reconfiguration-premium-subdominant-eigenspace-vrp-2026-09-02.md`, `single-name-equity-earnings-iv-crush-bid-ask-falsification-2026-09-13.md`) investigate crypto implied correlation or single-name earnings event volatility; none evaluate equity index-constituent straddle baskets under realized bid-ask friction.

## Economic mechanism

### Source-reported

Index implied variance embeds an implied average correlation among underlying constituents that is structurally higher than the correlation that subsequently realizes. Under the portfolio variance decomposition:

$$\sigma_{\text{index}}^2 = \sum_i w_i^2 \sigma_i^2 + \rho \sum_{i \neq j} w_i w_j \sigma_i \sigma_j$$

the market-implied average correlation $\rho_{\text{imp}}$ can be solved directly from index and constituent implied volatilities:

$$\rho_{\text{imp}} = \frac{\sigma_{\text{index}}^2 - \sum_i w_i^2 \sigma_i^2}{\left(\sum_i w_i \sigma_i\right)^2 - \sum_i w_i^2 \sigma_i^2}$$

The documented correlation risk premium (CRP) asserts that market participants overpay for index options relative to single-name constituent options because index puts provide portfolio crash insurance during systematic market panics when pairwise correlations spike toward 1.0. 

A classic dispersion trade attempts to monetize this premium by establishing a vega-neutral long-dispersion / short-correlation book: selling the expensive index straddle and buying a vega-matched basket of single-name constituent straddles. The trade generates positive gross returns when individual equities move idiosyncratically more than implied by option prices (realized correlation $\rho_{\text{real}} < \rho_{\text{imp}}$). 

In pre-registration (`research/index_dispersion_preregistration.md`), the author declared a falsification hypothesis: the correlation risk premium is structurally capacity-limited and expensive to harvest. Because the long leg requires executing 26 distinct single-name straddles (52 option legs) whose quoted bid-ask spreads are substantially wider than the index's, retail execution will suffer friction costs that consume or exceed the entire gross volatility premium.

### Research interpretation

This study provides a definitive empirical falsification of retail-accessible dispersion trading. It demonstrates the critical distinction between a theoretical asset pricing anomaly and an executable trading edge:

1. **Theoretical Reality vs. Execution Feasibility:** The underlying economic anomaly is real: implied correlation runs persistently above realized correlation ($\Delta \rho = +0.031$), producing an idealized gross return of $+5.36\%$ per period ($t = +1.98$, 58% win rate). However, institutional trading desks harvest this premium via direct market maker quoting, cross-margined exchange clearing, internalization of retail flow, and creation/redemption arbitrage against the cash basket. 
2. **The Retail Friction Barrier:** A taker strategy crossing quoted bid-ask spreads on 26 individual equity options incurs round-trip friction equal to $365\%$ of the gross volatility edge. 
3. **Absence of Tail Compensation:** The losses are not driven by catastrophic correlation-crash events: the regression beta to index market moves is statistically negligible ($\text{corr} = +0.03$), demonstrating that the strategy failure is entirely caused by transaction cost dissipation rather than unhedged market exposure.

## Signal

- **Signal Formation Timing:** Evaluated at EOD market close on a fixed 21-trading-day non-overlapping rebalance cycle (`REBALANCE_STEP = 21`, `source-reported`).
- **Contract Tenor:** Identifies options expiring nearest to a 30-day target horizon (`ATM_TARGET_DAYS = 30.0`, `source-reported`).
- **Strike Selection:** At-the-money (ATM) strike where absolute distance $|K - S|$ is minimized at the entry date for QQQ and each constituent (`source-reported`).
- **Basket Sizing & Vega Neutrality (`source-reported`):**
  - Sell 1 QQQ index straddle (1 ATM call + 1 ATM put).
  - Buy an equal-weighted basket of constituent straddles ($w_i = 1 / N$).
  - For each constituent $i$, determine the contract allocation $n_i$ to ensure exact vega neutrality against the short index position:
    $$n_i = w_i \cdot \frac{\text{Vega}_{\text{index}}}{\text{Vega}_i}$$
    such that $\sum_{i=1}^N n_i \text{Vega}_i = \text{Vega}_{\text{index}}$.
- **Holding Period:** Fixed 10 trading days (`HOLD_DAYS = 10`, approximately 14 calendar days, `source-reported`).
- **Exit Logic:** The exact same option contracts (identical strike $K$ and expiration $T$) are repriced at close on day $t + 10$ using actual market quotes (`source-reported`).
- **Corporate Action / Stock Split Guard (`source-reported`):** Any constituent whose underlying equity return $|S_{\text{exit}} / S_{\text{entry}} - 1| > 0.50$ is flagged as a stock-split artifact (e.g., historical splits in NVDA, AVGO, AMZN, GOOGL, TSLA) and dropped from that period's basket to prevent spurious straddle P&L calculations.
- **Minimum Basket Breadth (`source-reported`):** Requires at least 5 priceable constituents (`MIN_BASKET_NAMES = 5`) for a rebalance period to be considered valid.
- **Operational Rules Not Fixed by Source (`research-proposed`):**
  - Execution timestamp convention: 15:55 EST market close snapshot (`research-proposed`).
  - Position sizing / Margin model: 1.0x total portfolio capital allocated, reserving $2.0\times$ straddle entry premium as collateral for the short index straddle margin requirement (`research-proposed`).
  - Cash re-investment: Uninvested collateral held in short-term US Treasury bills earning the risk-free rate (`research-proposed`).

## Required data

- **Index Asset:** Invesco QQQ Trust ETF options (`source-reported`).
- **Constituent Assets:** 26 mega-cap Nasdaq-100 equities (`source-reported`):
  - AAPL, ADBE, AMAT, AMD, AMZN, AVGO, BKNG, COST, CSCO, GOOGL, HON, INTU, ISRG, LIN, LRCX, META, MU, NFLX, NVDA, PEP, QCOM, REGN, TMUS, TSLA, TXN, VRTX.
  - Note: GOOG excluded to prevent double-counting dual-class shares; MSFT excluded due to historical collection boundaries in Beck's primary lake (`source-reported proxy limitation`).
- **Venue:** US Equity Options Exchanges (OPRA consolidated NBBO quotes via ThetaData, `source-reported`).
- **Market Type:** Physically-settled, American-style equity and ETF options.
- **Timeframe:** Daily End-of-Day (EOD) quote bars.
- **Fields:** Strike, expiration, call/put bid, call/put ask, spot price (derived via put-call parity to ensure internal consistency across the surface), and Black-Scholes implied volatility.
- **Data Quality Protections:** Two-sided NBBO quotes required; zero/negative bids discarded; extreme IV outliers outside valid numerical bounds dropped (`source-reported`).

## Execution assumptions

- **Order Execution:** Quoted market crossing (taker execution).
- **Spread & Friction Model (`source-reported`):**
  - Entry friction: Charged the realized dollar half-spread:
    $$\text{Cost}_{\text{entry}} = 0.5 \times \left[(\text{Ask}_{\text{call}} - \text{Bid}_{\text{call}}) + (\text{Ask}_{\text{put}} - \text{Bid}_{\text{put}})\right]$$
  - Exit friction: Charged the realized dollar half-spread at exit for all open contracts.
  - Total friction: Sum of index straddle friction and all 26 constituent straddle frictions crossed at both entry and exit.
- **Fee Omission:** Exchange transaction fees, OCC clearing fees, and broker commissions omitted (`source-reported gap`). Net performance would degrade further if these explicit fees were included.
- **Execution Fill Model:** Immediate fill at the prevailing national ask for buys and national bid for sells (`source-reported`).
- **P&L Normalization (`source-reported`):** Total period dollar P&L divided by index straddle entry value ($V_{\text{index\_entry}}$) to yield standardized, comparable period returns:
  $$\text{Return}_{\text{period}} = \frac{\text{Gross P&L} - \text{Friction Cost}}{V_{\text{index\_entry}}}$$

## Evidence

### Source-reported

All empirical results are directly cited from Jonathan Beck's frozen evaluation records (`2026-06-17-index-dispersion-kill.md`, `index_dispersion_preregistration.md`, `PAPER_DRAFT.md`):

- **Sample Size:** $N = 53$ non-overlapping monthly rebalances from 2022-01-03 to 2026-06-12.
- **Mechanism Verification:**
  - Mean Implied Correlation ($\rho_{\text{imp}}$): $+0.380$
  - Mean Realized Correlation ($\rho_{\text{real}}$): $+0.349$
  - Net Correlation Risk Premium ($\rho_{\text{imp}} - \rho_{\text{real}}$): $+0.031$ (statistically positive correlation wedge).
- **Gross Performance (Frictionless):**
  - Gross Mean Return: $+0.0536$ (+5.36% of index premium per period)
  - Gross $t$-statistic: $+1.98$ (marginally significant, confirms literature mechanism)
  - Gross Win Rate: $58\%$
- **Transaction Friction:**
  - Mean Friction Cost: $+0.1955$ per period (+19.55% of index premium)
  - Friction Ratio: **$365\%$ of the gross edge** (realized single-name spreads are $3.65\times$ larger than the gross volatility alpha).
- **Net Performance (After Realized Spreads):**
  - Net Mean Return: **$-0.1419$** (-14.19% of index premium per period)
  - Net $t$-statistic: **$-5.03$** (decisively rejected)
  - Net Win Rate: $21\%$
  - Annualized Net Return: $-1.70$ (-170% normalized index premium loss per annum)
  - Worst Period Return: $-0.686$
  - Maximum Cumulative Drawdown: $-7.02$
- **In-Sample vs. Out-of-Sample Stability:**
  - In-Sample ($\le 2024-03-31$, $N = 27$): Net mean $-0.1172$, $t = -3.36$
  - Out-of-Sample ($\ge 2024-04-01$, $N = 26$): Net mean $-0.1675$, $t = -3.73$
  - Sign Stability: Strongly negative in both subperiods (no regime dependence).
- **Control Regressions:**
  - Incremental Alpha over Short Index Volatility: $\alpha = -0.1344$ per period ($t = -5.47$). The dispersion basket adds substantial negative alpha relative to simply selling the index straddle alone.
  - Correlation with Index Market Move: $\text{corr}(\text{Net Return}, \Delta \text{QQQ}) = +0.03$. The losses do not stem from crash compensation.
- **Placebo Test:**
  - Permutation Sign-Flip Test ($k = 2,000$ iterations): $p = 1.0000$. The net drag is so severe that zero randomized sign permutations generate an outcome worse than or equal to the actual strategy.
- **Verdict:** ❌ **KILL** — categorized as Class #2 Friction-Scale Noise.

### Independently reproduced

`Not independently reproduced.` Captured directly from primary code, pre-registration specifications, and empirical decision records in public repository `https://github.com/JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`).

### Negative evidence

- The bid-ask spread on 26 constituent single-name straddles represents $365\%$ of the gross dispersion edge.
- Net win rate collapses from $58\%$ gross to $21\%$ net.
- Both in-sample ($t = -3.36$) and out-of-sample ($t = -3.73$) periods exhibit statistically significant capital destruction.
- The dispersion book generates negative incremental alpha ($\alpha = -13.44\%$, $t = -5.47$) compared to an unhedged short index straddle.

## Falsification plan

To further stress-test or potentially falsify this negative verdict, the following operational tests are defined:

1. **Spread Compression / Maker Execution Stress Test:**
   - **Hypothesis:** Executing constituent legs passively as a liquidity provider (capturing half-spreads or paying zero spread) could restore strategy profitability.
   - **Protocol:** Re-simulate the 53 rebalance periods scaling realized half-spreads by a compression parameter $\lambda \in [0.0, 1.0]$.
   - `research-defined falsification threshold`: The breakeven spread multiplier is $\lambda^* = 1 / 3.65 \approx 0.274$. If strategy after-cost return remains negative when single-name spreads are compressed by $50\%$ ($\lambda = 0.50$, net return $-0.044$, $t < 0$), the hypothesis that maker rebates rescue retail dispersion is falsified.
2. **Cap-Weighted Full-Universe Replication:**
   - **Hypothesis:** The 26 equal-weighted constituent proxy without MSFT under-represents index variance concentration, artificially widening tracking error.
   - **Protocol:** Expand the basket to the top-50 Nasdaq-100 constituents weighted strictly by market capitalization, including Microsoft.
   - `research-defined falsification threshold`: If the net annualized return remains below $-50\%$ with $t \le -3.0$, the proxy-mismatch hypothesis is falsified.
3. **Liquidity-Tiered Selective Dispersion:**
   - **Hypothesis:** Limiting constituent straddles to the top-5 ultra-liquid names (AAPL, NVDA, AMZN, META, TSLA) minimizes friction while capturing the dominant idiosyncratic variance.
   - **Protocol:** Run the dispersion engine using only the 5 tightest-spread constituents.
   - `research-defined falsification threshold`: If the top-5 basket fails to achieve an after-cost Sharpe ratio $> 0.50$ across 2022–2026, liquidity filtering is falsified as a solution for retail dispersion.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`
- **Research Interpretation:** 
  - Centralized crypto index options (e.g., options on a broad market index like CMC200 or DeFi Index) do not exist on major liquid venues. 
  - Single-name options liquidity in cryptocurrency is almost entirely concentrated in BTC and ETH (via Deribit, OKX, and Binance). Liquid options on altcoin constituents are virtually non-existent or trade with astronomical bid-ask spreads ($10\%-40\%$ wide).
  - Porting an index dispersion trade to crypto would require constructing a synthetic index straddle (e.g., via a weighted BTC/ETH basket or perpetual futures variance swaps) against a basket of altcoin options. Given that altcoin option spreads are an order of magnitude wider than US equity options, the friction consumption problem documented here will be vastly magnified in crypto.
  - Furthermore, crypto options introduce margin collateral denomination risks (coin-margined inverse contracts vs. stablecoin linear contracts) and non-stop 24/7 gamma risk without daily closing auctions.

## Limitations

- **Proxy Basket Limitation (`source-reported`):** The 26 equal-weighted constituent basket omits MSFT and smaller constituents, serving as a mega-cap proxy rather than a perfect cap-weighted QQQ replication.
- **Execution Realism (`source-reported`):** Relies on EOD quoted spreads; does not simulate intraday mid-market fills, auction imbalances, or maker queue priority.
- **Fee Understatement (`source-reported gap`):** Direct exchange execution fees, clearing fees, and financing costs for margin collateral were omitted, making actual retail implementation even less favorable.
- **Non-Crypto Asset Class:** Results derived entirely from US equity options; conclusions regarding crypto portability represent theoretical research extrapolation.

## Implementation status

- `not-implemented`
- This record represents an external research capture and forensic falsification of an equity index dispersion strategy. No code has been developed for or integrated into PyBroker, NautilusTrader, paper trading, testnet, or live execution engines.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`
- This record serves as negative research knowledge regarding the unfeasibility of retail options dispersion trading under quoted bid-ask spreads. It does not authorize strategy development, backtest promotion, or capital allocation.

## Related Wiki records

- `[[crypto-options-implied-correlation-dispersion-2026-08-31]]`
- `[[cross-asset-reconfiguration-premium-subdominant-eigenspace-vrp-2026-09-02]]`
- `[[single-name-equity-earnings-iv-crush-bid-ask-falsification-2026-09-13]]`
- `[[put-call-parity-implied-borrow-dividend-confounding-falsification-2026-09-13]]`
- `[[sp500-statistical-arbitrage-johansen-ou-ablation-multiple-testing-2026-09-12]]`

## Sources

1. **Jonathan Beck (`JonathanBeck1`), "Decision: Index Dispersion / Correlation Risk Premium (T22)"**, `brain/decisions/2026-06-17-index-dispersion-kill.md` in `JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`), dated 2026-06-17. URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/brain/decisions/2026-06-17-index-dispersion-kill.md`
2. **Jonathan Beck (`JonathanBeck1`), "Pre-registration — T22 Index Dispersion / Correlation Risk Premium"**, `research/index_dispersion_preregistration.md` in `JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`), dated 2026-06-14. URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/index_dispersion_preregistration.md`
3. **Jonathan Beck (`JonathanBeck1`), "Python Implementation Core: index_dispersion.py"**, `src/trader/catalysts/index_dispersion.py` in `JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`). URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/src/trader/catalysts/index_dispersion.py`
4. **Jonathan Beck (`JonathanBeck1`), "Unit Test Suite: test_index_dispersion.py"**, `tests/financial/test_index_dispersion.py` in `JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`). URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/tests/financial/test_index_dispersion.py`
5. **Jonathan Beck (`JonathanBeck1`), "End-to-End Runner: run_index_dispersion_study.py"**, `scripts/run_index_dispersion_study.py` in `JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`). URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/scripts/run_index_dispersion_study.py`
6. **Jonathan Beck (`JonathanBeck1`), "Does Any Accessible Edge Survive Rigorous Testing? A Pre-Registered Falsification Campaign Across ~50 Strategy Families"**, `research/PAPER_DRAFT.md` in `JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`), Sections 1, 4.2, 7. URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/PAPER_DRAFT.md`
7. **Jonathan Beck (`JonathanBeck1`), "Campaign Scoreboard — Master Results Table"**, `research/CAMPAIGN_SCOREBOARD.md` in `JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`). URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/CAMPAIGN_SCOREBOARD.md`
