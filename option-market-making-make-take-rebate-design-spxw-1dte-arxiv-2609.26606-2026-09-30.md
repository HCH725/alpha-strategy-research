---
schema: strategy-research-record-v1
title: "Rebate-Designed Option Market Making: Make-Take Fee Inducement of Aggressive SPXW 1DTE Quotes (arXiv:2609.26606v1)"
created: 2026-09-30
updated: 2026-09-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - market-making
  - liquidity-provision
  - options
  - spxw
  - make-take-fees
  - rebate-design
  - limit-order-book
  - stochastic-control
  - hjbqvi
status: research-only
confidence: medium
source_as_of: 2026-09-22
sources:
  - "https://arxiv.org/abs/2609.26606v1"
  - "https://arxiv.org/pdf/2609.26606v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Rebate-Designed Option Market Making: Make-Take Fee Inducement of Aggressive SPXW 1DTE Quotes (arXiv:2609.26606v1)

## Provenance

**Primary source identity (all fields taken from the pinned primary source itself):**

- Title: *Liquidity Provision and Rebate Design in Option Markets*.
- Authors, exact order as printed on the PDF title page and in the arXiv `citation_author` block: Samuel N. Cohen; Lyndon Drake; Zihan Guo; Christoph Reisinger. Affiliations printed on the title page: Cohen (Mathematical Institute and Oxford-Man Institute, University of Oxford), Drake (Faculty of Theology and Religion, University of Oxford), Guo (marked "Primary Author", email block `zihan.guo@maths.ox.ac.uk`), Reisinger (Mathematical Institute, University of Oxford).
- Identifier: arXiv:2609.26606v1 [q-fin.MF]. Submission history from the arXiv abstract page: `[v1] Tue, 22 Sep 2026 15:42:56 UTC (1,957 KB)`, submitted by Zihan Guo.
- Abstract-page metadata: `citation_date` 2026/09/22, `citation_online_date` 2026/09/22, `citation_arxiv_id` 2609.26606, single subject class "Mathematical Finance (q-fin.MF)".
- Publication status: **preprint only**. The abstract page carries no Comments field, no journal-ref, and no DOI (`jref` and `doi` cells absent), so peer review, acceptance and venue are **not stated in source**.
- Licence: arXiv non-exclusive distribution licence (`arXiv.org/licenses/nonexclusive-distrib/1.0`, "Rights to this article: view license"); authors retain copyright. This record therefore cites and normalises the work and does not reproduce the manuscript.
- Data as-of: all calibration data are one regular trading session, **2023-10-23, 9:30 to 16:15** (Section 5.1); instrument expiries 2023-10-24. The source does not state a timezone for those clock times (data gap).

**Primary-source checksum (pinned artefacts used for every number in this record):**

- PDF: `https://arxiv.org/pdf/2609.26606v1` fetched 2026-09-30, **2,393,088 bytes**, SHA-256 `d38ee1cca55f6f86fa2985fb9319535a282c5650ac97a2a9718bc7021fc98bad`, **36 pages**, pypdf 6.16.2 text extraction **101,722 raw characters** / **101,725 characters** after ligature and dash normalisation, **2,799 lines**. Read end to end: title page and abstract; Section 1 Introduction including footnotes 1 to 5; Section 2 with 2.1, 2.2, 2.3, 2.4; Section 3 with 3.1, 3.2, 3.3, 3.4 and Remarks 1 to 4; Section 4 with 4.1, 4.2 and Algorithm 1; Section 5 with 5.1, 5.2, 5.3 and Remarks 5 and 6; Acknowledgements; Contributions; References [1] to [38]; Appendix A (Lemma A.1, Lemma A.2, Corollary A.3); Appendix B (B.1, B.2 with Table 2 and Table 3 in full); Appendix C; captions of Figures 1 to 7 and Tables 1 to 3 with every printed cell; and footnotes 6 to 22.
- Abstract page: `https://arxiv.org/abs/2609.26606v1` fetched 2026-09-30, **40,275 bytes**, SHA-256 `5891cec0095d112341a26f078515d2852bb573ea365659b9fa448e4b985f6ee3`, used for author order, dates, subjects, licence and the absence of comment/journal-ref/DOI.

**Funding, contributions and disclosure surface (verbatim-source summary):**

- Acknowledgements: research "supported by CBOE, through the EPSRC Centre for Doctoral Training in Mathematics of Random Systems: Analysis, Modelling and Simulation (EP/S023925/1)".
- Contributions statement: "SC, ZG and CR developed the modelling framework, numerical schemes, and wrote the paper. LD and ZG processed the raw CBOE PITCH data underlying the numerical section, and implemented the computational algorithm."
- The authors thank "Florian Huchede (CBOE), Leandro Sanchez Betancourt, and Alvaro Cartea for useful comments".
- There is **no conflict-of-interest statement, no data-availability statement, no code-availability statement and no limitations section** in the pinned text (whole-document `availability` = 0, `github` = 0, `limitation` appears only in ordinary prose about model scope). No third-party code was executed for this record.

**Search-provenance note:** the paper does not publish its implementation or the raw CBOE PITCH extract, so every model quantity below is either printed in Tables 1 to 3 or read off Sections 3 to 5 prose; quantities that exist only inside Figures 3, 4, 5, 6 and 7 are recorded as figure-only and therefore not numerically reproducible from the text (see Negative evidence item 7).

## Economic mechanism

### Source-reported

The source frames two nested problems on one options exchange that runs a continuous double auction with price-time priority (Section 2.1):

1. **Exchange side (principal).** Liquidity attraction, not fee income, is the objective. The exchange runs a *make-take fee system* that "redistributes the take fees (transaction fees) collected from the liquidity consumers as the make fees (fee rebates) offered to the liquidity providers" (Section 1). Because the exchange can observe the market maker's posted orders and net delta, the paper works in a **first-best** setting with *contractible effort* (Section 3.4), so the exchange can prescribe a rebate schedule and anticipate the market maker's best response, rather than solving the second-best principal-agent problem of Euch et al. cited in Section 1.
2. **Market maker side (agent).** A single market maker posts limit orders (make strategy, modelled as a continuous predictable control) and sends market orders (take strategy, modelled as an impulse control) in `M` European calls on a non-tradable underlying inside a local-stochastic-volatility market (Sections 2.1, 2.2). She maximises expected total PnL including cumulative rebate revenue, minus quadratic running and terminal penalties on residual portfolio delta and vega (Equation 11, Section 3.1).

The economic trade-off the source isolates: quoting **aggressively** (improve the best price by one tick) earns a smaller spread per fill but a higher execution intensity and a higher rebate; quoting **conservatively** (at the touch) earns the full spread but a lower intensity and a lower rebate (Sections 2.2, 3.3). Inventory pressure additionally switches sides off: limit-order intensities are gated by indicators that the portfolio delta and vega would remain inside the bands `[-Delta_bar, Delta_bar]` and `[-V_bar, V_bar]` (Section 2.3), which is how the model makes the market maker "skew" her make strategy.

The exchange's design claim is that a rebate schedule can be constructed so that the market maker's **optimal** make strategy is the exchange's target (Equation 34: quote aggressively whenever the spread exceeds one tick), while any other schedule would be at least as expensive: the three-step scheme of Section 3.4 computes, for every spread state and portfolio delta, the **least upper bound (LUB)** on the rebate payable for *conservative* quoting, and the **marginal fee rebate (MFR)** `F(1) - LUB` as the minimal extra reward required to buy aggressive quoting.

### Research interpretation

Stated as a falsifiable mechanism rather than an accepted fact: the strategy's economics are **liquidity-provision income (spread x fill intensity) plus a subsidy stream (rebates) minus explicit take fees and fixed order costs**, with inventory risk as a quadratic drag. There is no predictive signal of any kind anywhere in the source - no alpha factor, no order-flow forecast, no fair-value model error: the reference price is *assumed equal* to the arbitrage-free price process (Section 2.1) and the spread path is *exogenous* (the market maker is "small" and does not move ambient spreads, Section 2.2).

Component roles, labelled by this scout:

- **Regime:** spread state `d` in `{1,...,6}` ticks of a homogeneous continuous-time Markov chain, jointly with portfolio delta `Delta_pi` on `[-15, 15]`.
- **Primary signal (decision rule):** per side and per option, choose make regime `alpha in {0,1}` from the HJBQVI feedback functions (30) and (31): quote at the touch unless `d > delta_tick`, the inventory gate would still hold, and `H(1) + F(1) > H(0) + F(0)`.
- **Confirmation / constraint:** the delta (and, in the full LSV model, vega) band gates both admissibility and fill intensities.
- **Risk / exit:** impulse market-order trades only when the state leaves the continuation region `C` of Equation 32, with size given by the argmax of Equation 33, which trades off spread-plus-fee cost against the reduction of the quadratic delta penalty.
- **Subsidy overlay (the paper's actual contribution):** aggressive-quote rebate `F(1, d) = 0.1 * (d - tick)` dollars for `d > tick` and zero at one tick; conservative-quote rebate pinned to zero at one tick and otherwise only *bounded above* by the computed LUB (Section 5, step (a), and Equations 41, 42).

Research-proposed (not in source): the tradable hypothesis is that this feedback policy earns positive expected contribution per 10-second market-making window after the source's own fees (`epsilon = 1e-3` dollars per unit, `epsilon_tilde = 1e-5` dollars per market order) and that the LUB schedule induces `alpha = 1` whenever `d > tick`. The source never states or tests this profitability claim; it reports value-function and rebate-bound figures only (see Evidence).

## Signal

**Formation timestamp and update clock.** Continuous-time feedback policy. The market maker is small, so she "instantaneously updates her quotes only when the changes of the spreads are caused by the trading behavior of the other market participants" (Section 2.2); concretely quotes are re-evaluated at the jump times `T_n` of the spread chain and after every fill or impulse trade. Times are exchange clock times with no timezone stated in source (data gap). The numeric horizon is `T = 10` seconds (Table 1), so the *policy* is evaluated on a 10-second window even though calibration uses the whole session.

**Lookback.** None in the policy itself (it is model-based, not history-based). The only historical window in the source is the calibration sample: Level-1 best quotes over the single session 2023-10-23 9:30-16:15 (Section 5.1), used to estimate the spread-chain generator (Appendix B.1, Table 2) and the execution intensities (Appendix B.2, Table 3). No train/validation/test split exists (data gap; see Negative evidence item 2).

**Bid side (long entry in the inventory sense).** Post a limit buy at `pi_b = c - d/2 + delta_tick * alpha_b`, where `c` is the reference mid and `d` the current spread. `alpha_b = 1` (improve the best bid by one tick) iff all three hold (Equation 30): `d > delta_tick`; `Delta_pi + Delta_i <= Delta_bar`; and `H^{b,i}_d(1) + F^{b,i}_d(1) > H^{b,i}_d(0) + F^{b,i}_d(0)`. Otherwise `alpha_b = 0` (quote at the touch). When `d = delta_tick` only `alpha = 0` is admissible, because improving a one-tick spread would in fact be a market order (Section 2.2).

**Ask side (short entry in the inventory sense).** Symmetric: `pi_a = c + d/2 - delta_tick * alpha_a`, `alpha_a = 1` iff `d > delta_tick`, `Delta_pi - Delta_i >= -Delta_bar`, and the analogous ask-side inequality (Equation 31).

**Take (crossing) rule.** At the first time the state exits the continuation region `C` (Equation 32), send a market order of size `ell_hat` = argmax over `ell` in `E^M` with `Delta_pi + sum_i ell_i Delta_i` inside `[-Delta_bar, Delta_bar]` of `-sum_i (|ell_i| * (d_i/2 + epsilon) + epsilon_tilde * 1{ell_i != 0}) + phi(t, Delta_pi + sum_i ell_i Delta_i)` (Equation 33), with `E = {-3,...,3}` (`e_bar = 3`, Table 1).

**Exit and holding.** There is no inventory liquidation rule: the terminal term `-gamma' * (Delta_pi)^2` is explicitly *not* interpreted as a liquidation cost, but as a proxy for the market maker's risk preference beyond `T` (Section 3.1). Positions therefore persist past the window in the model's own reading.

**Parameters (all source-reported, Table 1).** Market parameters: `T = 10 s`; `sigma = 0.22`; `delta_tick = 0.01 dollars`; `m = 6` spread levels; `e_bar = 3` max market-order volume; `epsilon = 1e-3 dollars` per unit call; `epsilon_tilde = 1e-5 dollars` fixed brokerage per market order. Optimization parameters: `gamma = 5` (running delta risk aversion), `gamma' = 5` (terminal), `Delta_1 = 0.50`, `Delta_2 = 0.45` (Black-Scholes deltas from opening option and SPX prices, rounded to two decimals, Section 5.1). Discretization: `rho = 1` (penalty parameter), `N = 2000` time steps, `Delta_bar = 15` (delta risk limit). Rebate functions (Section 5): `F^b(0, .) = F^a(0, .) = 0` at `d = tick`; `F^b(1, .) = F^a(1, .) = 0.1 * (d - tick)` for `d > tick`; `F(0, .)` for `d > tick` left to be determined up to the LUB.

**Specification status.** The *decision rule* is fully specified (Equations 30 to 33 plus Table 1). What is **underspecified** for independent reconstruction: (i) the value function `phi` exists only as a numerical solution and no code or grid values are published; (ii) the conservative-quote rebate is only bounded, not pinned, so no single exchange schedule is given; (iii) the intensities and generator are printed but the underlying tick data are not released; (iv) the timezone, the venue fee schedule that `epsilon`/`epsilon_tilde` stand in for, and any margin/leverage rule are not stated.

## Required data

- **Instrument:** two one-day-to-expiry SPXW (SPX weekly) European-style call options, strikes `K_1 = 4225` and `K_2 = 4230`, both expiring 2023-10-24, tick size `$0.01` (Section 5.1). Underlying: SPX index, explicitly treated as non-tradable for delta-one hedging purposes (footnote 3: "physically nontradable, e.g. VIX options, or practically nontradable due to illiquidity and market frictions (transaction costs), e.g. SPXW options").
- **Venue:** a single options exchange running a central limit order book under price-time priority (Section 2.1); the raw feed is CBOE PITCH (Contributions statement), Level 1 best quotes.
- **Market type:** listed equity-index options (cash-settled style is **not stated in source**); no crypto, no perpetual, no spot.
- **Timeframe:** tick / Level-1 event data over one session, 9:30 to 16:15, 2023-10-23; spread series additionally resampled at second frequency for Figure 1, excluding spread values above ten ticks.
- **Fields required:** best bid and ask (hence spread) for both calls; best-quote volumes `V^b`, `V^a`; total market-order volumes arriving at the best prices between consecutive spread jumps `V^buy`, `V^sell`; VIX opening value (used as `sigma = 0.22`); opening SPX and option prices (used for the constant deltas 0.50 and 0.45).
- **Point-in-time:** no revisions or publication lags apply (exchange data), but there is **no point-in-time discipline in the research design**: the same session calibrates and evaluates the policy (data gap).
- **Missing data handling, as stated by the source:** spread states beyond six ticks are dropped from the state space because they "occur infrequently, and hence cannot be reliably calibrated" (Section 5.1, Figure 2); spreads above ten ticks are excluded from the Figure 1 resampling. Deltas are rounded to two decimals. Volatility is held at the VIX open for the whole window.
- **Fees and frictions as data needs:** `epsilon = 1e-3` dollars/unit and `epsilon_tilde = 1e-5` dollars/order are *modelling inputs*, not a disclosed venue tariff (the actual CBOE option fee/rebate schedule is **not stated in source** - data gap). The rebate `0.1 * (d - tick)` is likewise a hypothetical schedule chosen by the authors, not an observed exchange policy.

## Execution assumptions

Distinguishing what the source assumes from what remains open:

- **Signal-to-order timing:** quotes are updated instantaneously at spread jumps; the source notes in footnote 9 that trading on a single venue "can alleviate latency effect". No explicit latency is modelled; the penalty parameter `rho` is given a *latency interpretation* in Section 4.1 ("the larger the penalty parameter rho, the faster the market orders are executed, or in other words, the lower the latency effect") but is fixed at `rho = 1` and never calibrated. Latency = **underspecified**.
- **Order types:** limit orders only at the touch or one tick through (Section 2.2); market orders for the take leg. "limit order" occurs 41 times and "market order" 30 times in the pinned text; there is no other order type (no iceberg, no post-only, no stop).
- **Fill model:** Cox processes with state-dependent intensities `lambda^b_d(alpha)`, `lambda^a_d(alpha)` satisfying `lambda(0) <= lambda(1)` (Equation 3). Because the true execution processes are unobservable, Appendix B.2 fills them with **proxies**: an aggressive quote is credited a fill whenever the total counterparty volume between two jumps covers the virtual reference size `V_0 = 1` contract; a conservative quote is credited only when the volume *net of the volume already resting ahead* covers `V_0` (Equations 52 to 54). Partial fills are therefore not represented beyond this binary comparison; queue position enters only through that subtraction.
- **Fees:** take fees are explicit - market orders pay `h(ell, c, d) = ell*c + |ell|*(d/2 + epsilon) + epsilon_tilde*1{ell != 0}` (Equation 4), i.e. the half-spread plus `1e-3` per unit plus `1e-5` per order. Limit-order submission and cancellation are free (Section 2.2).
- **Spread:** paid when crossing, captured when providing (`d/2 - delta_tick*alpha` per fill in Equation 7). There is **no slippage term beyond the modelled half-spread** - `slippage` = 0 occurrences - so slippage is a data gap, not a zero.
- **Impact:** none. The market maker is assumed small with respect to ambient spreads (Section 2.2); `market impact` occurs exactly once, in the Section 1 literature review. Impact = data gap.
- **Adverse selection:** not modelled; `adverse selection` occurs exactly once, also in the Section 1 literature review.
- **Funding / borrow / margin / leverage:** not applicable to the stated options market-making setting and **not stated in source** (census `funding` = 0, `borrow` = 0); no margin or leverage rule appears anywhere.
- **Capacity:** not analysed (`capacity` = 0 occurrences); the model trades one contract at a time with a maximum market order of three contracts per option.
- **Failures / partial fills / cancellations:** no cancellation cost, no rejection or partial-fill logic (data gap).
- **Shorting:** n/a for options market making (no equity short leg anywhere).

## Evidence

### Source-reported

Every figure below is source-reported, traced to the pinned PDF; none has been independently reproduced.

**Parameters (Table 1, Section 5).** `T = 10 s`, `sigma = 0.22`, tick `$0.01`, `m = 6`, `e_bar = 3`, `epsilon = 1e-3`, `epsilon_tilde = 1e-5`, `gamma = 5`, `gamma' = 5`, `Delta_1 = 0.50`, `Delta_2 = 0.45`, `rho = 1`, `N = 2000`, `Delta_bar = 15`.

**Rebate schedule under test (Section 5, step (a)).** `F(0, .) = F(1, .) = 0` when `d = tick`; `F(1, .) = 0.1 * (d - tick)` when `d > tick`; `F(0, .)` for `d > tick` determined only through the LUB of Equations 41-42. Research-computed (arithmetic on the source's own formula): `F(1)` equals `$0.001` at `d = $0.02`, `$0.002` at `$0.03`, `$0.003` at `$0.04`, `$0.004` at `$0.05`, `$0.005` at `$0.06`.

**Estimated spread-chain generator (Appendix B.1, Table 2, "expressed in ticks and second^-1", 36 x 36).** Selected printed cells, row = spread pair before jump, column = after jump: row `(1,1)` diagonal `-24.11`, `(1,1)->(1,2) 8.18`, `(1,1)->(2,1) 12.96`, `(1,1)->(2,2) 2.63`, `(1,1)->(3,1) 0.20`; row `(2,2)` diagonal `-8.61`; row `(3,3)` diagonal `-13.65`; row `(4,4)` diagonal `-24.82`; row `(5,5)` diagonal `-23.49`; row `(6,6)` diagonal `-12.06` with off-diagonal entries `0.01, 0.01, 0.07, 0.01, 0.08, 0.03, 0.33, 0.04, 0.12, 0.04, 1.08, 0.13, 0.54, 1.76, 0.13, 0.72, 2.63, 4.35`. The full table is printed in the pinned PDF; the paper uses it to argue that joint spreads mean-revert at the microscopic scale (Figure 5 caption and Appendix B.1 prose).

**Estimated limit-order execution intensities (Appendix B.2, Table 3, "expressed in second^-1"), all 48 printed cells.** Columns are, in order: strike 4225 ask, strike 4225 bid, strike 4230 ask, strike 4230 bid, each split aggressive / conservative:

| Spread (USD) | 4225 ask agg | 4225 ask cons | 4225 bid agg | 4225 bid cons | 4230 ask agg | 4230 ask cons | 4230 bid agg | 4230 bid cons |
|---|---|---|---|---|---|---|---|---|
| 0.01 | 0.1821 | 0.0000 | 0.1252 | 0.0114 | 0.1484 | 0.0000 | 0.0691 | 0.0041 |
| 0.02 | 0.0075 | 0.0006 | 0.0087 | 0.0011 | 0.0100 | 0.0008 | 0.0074 | 0.0001 |
| 0.03 | 0.0019 | 0.0000 | 0.0014 | 0.0000 | 0.0016 | 0.0000 | 0.0005 | 0.0004 |
| 0.04 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0014 | 0.0000 | 0.0000 | 0.0000 |
| 0.05 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 0.06 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |

Source-reported reading of Table 3: at a one-tick spread the aggressive intensity is roughly 0.07 to 0.18 per second while the conservative intensity is 0.0000 to 0.0114 per second; by a four-tick spread intensities are zero (except strike 4230 ask, aggressive, `0.0014`).

**Optimal-policy interpretation (Section 3.3, prose after Equations 30-33).** "For the make strategy, when the spread exceeds one tick, it is optimal to quote aggressively if the resulting fee rebates fully offset the potential loss from improving the best price (unless a trade would lead the portfolio delta to exceed the bound); otherwise, it is optimal to quote conservatively. For the take strategy, it is optimal to send a market order only when the portfolio delta is reduced effectively after intervention, with an order size that simultaneously minimizes the transaction costs and the penalty on the residual portfolio delta."

**Value-function shape (Section 5.2, Figure 3).** `phi` "starts as a quadratic function at t = T" and "gradually bends downward as t approaches 0, forming an approximately quadratic shape"; dependence on the spread `d` is described as moderate, with Appendix C reporting that `phi_d` and `phi_d'` differ negligibly in the interior of the state space and mainly near the boundary (Figure 7, "truncation effects").

**Rebate bounds (Section 5.3, Figure 4, option C1 only, `d_1` in `2*delta` to `6*delta`).** Source-reported qualitative results: (i) the bid-side LUB is strictly positive when `Delta_pi` is strictly negative and the ask-side LUB strictly positive when `Delta_pi` is strictly positive, i.e. when the maker would narrow the spread anyway to reduce delta; (ii) for small spreads `2*delta` and `3*delta` the LUB becomes strictly **negative** at large-magnitude opposite-sign deltas, meaning "the exchange should effectively 'punish' the market maker if she fails to improve the best prices"; (iii) for large spreads `4*delta`, `5*delta`, `6*delta` the LUB "remains positive, and is indeed equal to the fee rebates for aggressive quotes", which the paper rationalises from Table 3: at spreads of at least four ticks the execution intensity is "(almost) zero on both sides regardless of aggressiveness", so "no liquidity taker arrives ... and thus no transactions occur".

**Data diagnostics (Section 5.1, Figures 1, 2, 5, 6).** "neither figure reveals any evident intraday seasonality effect, supporting the homogeneity assumption on the spread Markov chain"; "the first six spread levels dominate the empirical distribution"; joint transitions "quickly 'pull' the spreads back towards each other so that the joint spread process is mean reverting at the microscopic level"; Figure 6 plots affine interpolation of the estimated intensities.

**Caveats the source itself prints.** Footnote 22: the period of heightened spreads in the $4225 strike option "does suggest that there is a case for a model with longer memory, such as a regime switching model", omitted here. Remark 5: "The rebate policy proposed above is somewhat unrealistic as it involves negative fee rebate in some circumstances", with a proposed "lift" of the schedule that is not implemented or evaluated. Remark 6: bid/ask intensity asymmetry "may be attributed to the unbalanced or non-stationary price movement observed on the specific trading day used for calibration ... unlikely to be typical across trading days and should be interpreted with caution."

**Performance figures.** The source reports **no** PnL, Sharpe ratio, return, CAGR, drawdown, win rate, turnover, capacity or any other profitability statistic. Whole-document census of the pinned 101,725-character text: `sharpe` 0, `turnover` 0, `drawdown` 0, `cagr` 0, `win rate` 0, `capacity` 0, `net of cost` 0, `after-cost` 0, `p-value` 0, `bootstrap` 0, `newey` 0, `hac` 0, `benjamini` 0, `fdr` 0, `multiple test` 0, `deflated` 0, `walk-forward` 0, `point-in-time` 0, `survivorship` 0, `look-ahead` 0. Cost-model vocabulary: `transaction cost` 2 (footnote 3 and the Section 3.3 interpretation sentence - both prose, neither a measured cost), `trading cost` 0, `slippage` 0, `commission` 0, `friction` 1 (footnote 3), `market impact` 1 (Section 1 literature review), `adverse selection` 1 (Section 1), `latency` 3 (footnote 9 and two sentences in Section 4.1 about the penalty parameter), `queue` 1 (Section 2.2), `fill` 1 (as "filled", Appendix B.2), `funding` 0, `borrow` 0, `order type` 0, `participation` 0, `rebalance` 0, `github` 0, `availability` 0, `code` 1 (the verb "encode" in Section 3.1), and the substring `etf` 1 - inside "letf(n)" in the Lemma A.2 proof, never denoting an exchange-traded fund. The only cost model in the paper is the market-order cost function `h` of Equation (4) with `epsilon` and `epsilon_tilde`. Cryptographic and asset-class vocabulary: `crypto` 0, `bitcoin` 0, `ethereum` 0, `perpetual` 0, `24/7` 0.

### Independently reproduced

not independently reproduced.

Arithmetic and text-consistency checks only (no model re-execution, no third-party code run): the Table 2 rows satisfy `diagonal = -sum(off-diagonal)` to within printed rounding (row `(1,1)`: off-diagonals sum to `24.14` against printed `-24.11`, residual `0.03`; row `(6,6)`: sum `12.08` against printed `-12.06`, residual `0.02`; worst absolute row residual over all 36 rows `0.04`); all 24 aggressive/conservative intensity pairs in Table 3 satisfy the model's own required property `lambda(0) <= lambda(1)` (Equation 3); Table 3 is identically zero for strike 4225 at spreads `$0.04`, `$0.05`, `$0.06` on both sides under both strategies, which is exactly the premise used in Section 5.3; the rebate values implied by `0.1*(d - tick)` recompute to `0.001/0.002/0.003/0.004/0.005`; the census counts above were recomputed from the pinned PDF text; the PDF byte count, page count and SHA-256 were recomputed. These checks validate transcription and internal consistency, **not** the strategy's profitability.

### Negative evidence

1. **No performance evidence at all.** The paper never reports PnL, Sharpe, return, drawdown, turnover, win rate or capacity; its "numerical results ... validate the effectiveness of the proposed scheme" claim (abstract) rests on a value-function surface and rebate-bound curves only.
2. **No out-of-sample separation.** Calibration and evaluation use the same single session (2023-10-23); there is no train/validation/test split, no walk-forward, no frozen forward window.
3. **Sample of size one day, two contracts.** `M = 2` calls, one strike pair, one 1DTE expiry class, one trading day - and Remark 6 explicitly warns the estimated bid/ask asymmetry is a day-specific artefact risk.
4. **Fills are proxies, not observations.** Appendix B.2 concedes "no one precisely performs the proposed make strategy on the real-world order book, we cannot directly observe the actual execution processes"; the proxy assumes an aggressive quote captures *all* flow covering one contract while a conservative quote ranks behind all resting volume - a structural assumption that, if wrong, drives the entire aggressive-versus-conservative intensity gap that motivates the rebate.
5. **The strategy is inert exactly where the exchange most wants liquidity.** Table 3 shows zero intensity at spreads of `$0.05` and `$0.06` for every side and both strategies, and zero for strike 4225 from `$0.04`; Section 5.3's own explanation is that no taker arrives, so aggressive and conservative quoting are economically indistinguishable at wide spreads - yet wide spreads are the illiquid cases the rebate story targets.
6. **Figure-only headline results.** The LUB and MFR values (Figure 4) and the value function (Figure 3) are printed nowhere as numbers, so the paper's central quantitative claim cannot be checked against the text (data gap).
7. **The proposed schedule needs negative rebates and is admitted unrealistic.** Remark 5 concedes the policy "involves negative fee rebate in some circumstances" and suggests lifting the baseline; the lifted schedule is never computed, so no implementable rebate table is delivered (underspecified).
8. **No queue dynamics, no partial fills, no cancellation cost, no adverse selection, no impact, no latency** - each is either absent or appears once only in the literature review (see Execution assumptions and the census).
9. **Greeks frozen.** Constant-delta approximation over the window with deltas rounded to two decimals at the open (Section 2.3, footnote 17 concedes gamma risk is neglected), and the numerical section switches from the LSV framing to constant-volatility Black-Scholes, dropping vega entirely (Section 3.3, footnote 20).
10. **Reference-price perfection.** The best bid/ask are built from a reference mid assumed equal to the arbitrage-free price (Section 2.1); any fair-value error, and hence any true adverse-selection channel, is ruled out by assumption rather than measured.
11. **Homogeneous spread chain** despite visible non-stationarity (footnote 22 offers regime switching as the fix and does not implement it).
12. **Risk-neutral maker with zero short rate** and pricing measure = objective measure, so no risk premium is demanded for providing liquidity (Section 2.1); inventory risk enters only through quadratic penalties with `gamma = 5` chosen as a user parameter, not estimated.
13. **First-best assumption:** the exchange observes the maker's net delta and can condition rebates on it, and effort is contractible (Section 3.4). In practice rebate schedules are coarse and cannot punish a maker for failing to improve a quote; the paper's own "punishment" mechanism depends on this assumption.
14. **Single maker, price-taking.** No competitive interaction, no other market makers, no strategic replenishment; the maker is explicitly too small to move spreads.
15. **Unit-size quoting with `V_0 = 1`** and `e_bar = 3`: capacity is a couple of contracts per window; no ADV, participation or capacity analysis exists (`capacity` = 0).
16. **No statistical inference whatsoever.** Generator and intensity estimates are printed without standard errors, confidence intervals, p-values or block bootstrap; no multiplicity control anywhere in the paper (census above).
17. **No robustness across days, expiries, strikes or regimes**, and no subperiod split.
18. **No code and no data release.** `github` = 0, `availability` = 0; the CBOE PITCH extract is not published, so neither Table 2 nor Table 3 can be recomputed (data gap).
19. **Sponsor alignment.** Funding from CBOE, CBOE data, CBOE acknowledgement and CBOE-affiliated thanks, with no conflict-of-interest statement (Provenance).
20. **Preprint-only status**, v1, no DOI, no journal-ref, peer review not stated; the preprint was 8 days old at the time of this capture.
21. **No limitations section** in the source; scope caveats are scattered through footnotes and Remarks 5 and 6.
22. **Post-horizon inventory is unpriced.** The terminal delta penalty is explicitly not a liquidation cost (Section 3.1), so the model never pays to unwind.
23. **Instrument choice is favourable and asserted.** SPXW 1DTE options on one day where, per Remark 6, price moves were unbalanced; footnote 3 justifies non-tradability of the underlying by example, not by test.
24. **Zero crypto content** (`crypto`, `bitcoin`, `ethereum`, `perpetual`, `24/7` all zero), so nothing here is evidence about crypto venues.
25. **Editorial truncation in Section 3.4:** the sentence "we generalize this idea by enabling the exchange to Based on these targets, the exchange then designs individualized rebate policies" is broken in the pinned v1 PDF, i.e. a stated generalisation is not actually delivered (text defect, recorded rather than adjudicated).

## Falsification plan

All thresholds below are **research-defined falsification thresholds** chosen by this scout; none comes from the source. Each gate states data, sample/regime, metric, threshold, decision rule and action. A single failure is sufficient to weaken or reject the mechanism as stated.

- **F1 Printed-value reproduction.** Data: Tables 1 to 3 of the pinned PDF. Recompute the spread-chain generator, the 48 intensities and Algorithm 1's `phi` grid. *Fail* if the Section 5.3 sign pattern of `LUB(d_1)` for `d_1 = 2*delta ... 6*delta` is not reproduced for option C1, or if any Table 3 cell cannot be regenerated within `1e-4`. *Action:* mark the mechanism unreproducible and stop.
- **F2 Multi-day fill-gap replication.** Data: Level-1 quotes for at least 20 distinct 1DTE SPXW sessions. Metric: `Delta_lambda = lambda(1) - lambda(0)` at a one-tick spread, both sides. *Fail* if `Delta_lambda <= 0` on more than 25% of session-side cells. *Action:* reject the aggressive-quoting premise that the rebate is buying.
- **F3 Real fee schedule.** Replace `epsilon = 1e-3` and `epsilon_tilde = 1e-5` with the exchange's published option fee and per-contract charges for the relevant periods. *Fail* if expected net contribution per 10-second window, under the source's own intensities and rebates, is `<= 0`. *Action:* classify as economically non-viable under real fees.
- **F4 Rebate-sign gate.** Re-run the Section 3.4 scheme with a non-negative baseline lift as proposed in Remark 5. *Fail* if the only schedule that induces `alpha = 1` requires negative rebates on more than 50% of `(spread, Delta_pi)` cells. *Action:* withdraw the rebate-induction claim.
- **F5 Wide-spread inertness gate.** Metric: fraction of quoted time spent at spreads `>= 4*delta`. *Fail* if it exceeds 20% of the session (where Table 3 says nothing executes). *Action:* restrict any claim to `d <= 3*delta`.
- **F6 Latency ladder.** Insert quoting latency of 0, 50, 200 and 1000 ms into the simulation. *Fail* if the value advantage of the aggressive policy over the always-conservative policy becomes non-positive at 200 ms. *Action:* mark latency-fragile.
- **F7 Toxic-flow gate.** Add an adverse-selection channel (e.g. a VPIN-style signed-volume toxicity state that raises the taker's informed share) and re-solve. *Fail* if adverse-selection cost exceeds spread-plus-rebate income by 50% or more. *Action:* reject the mechanism under informed flow.
- **F8 Cost ladder.** Add a per-cancellation fee of 0, 0.1, 1 and 2 ticks-equivalent and an extra slippage of 0, 1 and 2 ticks beyond the modelled `d/2`. *Fail* if net contribution per session is `<= 0` at a one-tick slippage add-on. *Action:* mark cost-fragile.
- **F9 Cross-day holdout.** Calibrate on one day, evaluate on at least 19 other days with parameters frozen. *Fail* if the policy's net contribution is worse than the always-conservative baseline on a majority of days. *Action:* mechanism fails out of sample.
- **F10 Breadth gate.** At least 2 expiries x 10 days x 4 strikes. *Fail* if the sign of `Delta_lambda` at a one-tick spread is not consistent in at least 75% of instrument-days. *Action:* treat Table 3 as a day-specific artefact (the risk Remark 6 names).
- **F11 Inference gate.** Block bootstrap (1-second blocks, 1000 draws) confidence intervals for `lambda` and `q_jk`. *Fail* if the 95% interval for pooled `Delta_lambda` at one tick contains zero. *Action:* the fill gap is statistical noise.
- **F12 Multiplicity gate.** Benjamini-Hochberg at `q < 0.10` across the 36 generator rows and the 48 intensity cells. *Fail* if no entry survives. *Action:* treat the calibration as uninformative.
- **F13 Exchange cost-effectiveness gate.** Metric: total rebate paid under the induced `alpha = 1` policy divided by the reduction in quoted spread (in dollars per contract). *Fail* if the cost per unit of spread reduction exceeds 50% of the rebate-adjusted spread capture (research-defined willingness-to-pay). *Action:* the rebate scheme is not cost-effective for the exchange.
- **F14 Frozen forward window.** From 2026-10-01, at least 12 months of new 1DTE SPXW days with every parameter frozen. *Fail* if net contribution per session is `<= 0`, or if the sign of `Delta_lambda` flips on more than 33% of days. *Action:* reject.

**Global no-retuning rule.** Once any gate is attempted, freeze: `T = 10 s`; `sigma` sourced from the session's VIX open; tick `$0.01`; `m = 6` spread states with the same truncation rule; `e_bar = 3`; `epsilon = 1e-3`; `epsilon_tilde = 1e-5`; `gamma = gamma' = 5`; `Delta_bar = 15`; `rho = 1`; `N = 2000`; the two-strike 1DTE construction; the rebate slope `0.1`; the constant-delta approximation with two-decimal rounding; the Appendix B.2 proxy fill rule; and the LUB/MFR construction of Equations 41-42. A failed gate may not be rescued by retuning any of these; only a new record with a new source identity may re-open them.

## Crypto portability

**adapted** (mechanism ports mechanically; performance unproven).

- What ports: the make-take fee architecture itself. Crypto venues run maker/taker fee schedules and maker-rebate programmes, and the make/take split, the aggressive-versus-conservative quote decision and the inventory-gated intensity structure are venue-agnostic control objects.
- What does not port without re-derivation: the paper's underlying is a single non-tradable index, and the calibration window is one exchange session from 9:30 to 16:15. Crypto trades 24/7, so a homogeneous intra-session spread chain and a "one regular session" calibration design do not transfer (census: `24/7` = 0 in source).
- Contract-level differences: crypto option products, expiries, tick sizes and settlement differ from SPXW weeklies; funding, mark/index price, liquidation and ADL are **not addressed anywhere in the source** (`funding` = 0, `borrow` = 0) and would matter for any delta-hedged crypto book.
- Venue fragmentation and quote-selection risk are absent from the model (single venue by assumption, footnote 9); crypto is fragmented across many books with different rebate schedules.
- Evidence status: the source contains zero crypto content (`crypto`, `bitcoin`, `ethereum`, `perpetual` all zero), so nothing in it is crypto empirical evidence. Any crypto deployment would be a ported hypothesis requiring fresh calibration and the full F1-F14 programme; crypto trading performance is **unproven**.

## Limitations

- **underspecified:** the conservative-quote rebate (only LUB-bounded); timezone of the calibration session; venue fee tariff behind `epsilon`/`epsilon_tilde`; margin, leverage and capital rules; capacity and participation limits; slippage beyond the modelled half-spread; cancellation and failure handling.
- **data gap:** raw CBOE PITCH extract, implementation code, numerical values behind Figures 3 to 7, standard errors for Tables 2 and 3, any profitability statistic.
- **not independently reproduced:** every source-reported number; only transcription and arithmetic consistency were checked.
- **unproven:** preprint-only v1 with no journal-ref, DOI, acceptance or peer-review statement; effectiveness claimed from a single day and two contracts.
- **model risk:** constant-delta and constant-volatility reductions, exogenous spreads, perfect reference pricing, risk-neutral maker, first-best contractible effort, price-taking single maker - each is an assumption, not a measured property.
- **sponsor and disclosure risk:** CBOE funding, CBOE data, CBOE acknowledgement, no conflict-of-interest, data-availability or limitations statement.
- **incremental-write note:** this is a new source identity (arXiv:2609.26606v1) whose mechanism - exchange-side rebate design of maker quoting behaviour - is absent from the existing option-market-making records in this repository; it is not a reframing of any of them.
- The record contains no claim that the strategy works; it captures a mechanism, its calibration surface and the evidence needed to break it.

## Implementation status

`implementation_status: not-implemented`. Nothing has been implemented in our research stack: no HJBQVI solver, no SPXW data ingestion, no market-making simulation, no Qlib run, no Paper/Testnet/Live activity, and no market data of any kind was downloaded for this record. Third-party code was not executed (the source publishes none). This document is a research capture only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. The presence of this record does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. Any adoption decision is a separate, explicit review based on this record plus current sources.

## Related Wiki records

Verified existing Wiki Brain pages related by mechanism or instrument family:

- [[quant/deep-rl-market-making-regime-switching-bocpd-scenario-bandit-2026-09-11]] - market making under regime-switching order flow, but with no exchange fee schedule and a different (RL) control object.
- [[quant/performative-market-making-inventory-feedback-arbitrage-2026-09-02]] - inventory-feedback market making where the maker's own quotes move the book, the opposite of this source's price-taking maker.
- [[quant/spy-options-svi-surface-rv-falsification-adverse-selection-2026-09-12]] - options-market-maker economics anchored on an SVI fair-value surface with adverse selection, i.e. the channel this source rules out by assumption.

No other related page was returned by the Wiki Brain searches "option market making make-take fee rebate limit order book" (0 results) and "option market making hedging impact eSSVI" (0 results); no page was fabricated and no Wiki Brain write was performed.

## Sources

- Samuel N. Cohen, Lyndon Drake, Zihan Guo, Christoph Reisinger, *Liquidity Provision and Rebate Design in Option Markets*, arXiv:2609.26606v1 [q-fin.MF], submitted 22 Sep 2026 15:42:56 UTC. Abstract page: https://arxiv.org/abs/2609.26606v1 (40,275 bytes, SHA-256 5891cec0095d112341a26f078515d2852bb573ea365659b9fa448e4b985f6ee3, fetched 2026-09-30). PDF: https://arxiv.org/pdf/2609.26606v1 (2,393,088 bytes, SHA-256 d38ee1cca55f6f86fa2985fb9319535a282c5650ac97a2a9718bc7021fc98bad, 36 pages, fetched 2026-09-30). Licence: arXiv non-exclusive distribution licence (arXiv.org/licenses/nonexclusive-distrib/1.0).
- Data provenance as stated in that source: CBOE PITCH Level-1 best quotes, regular trading hours 9:30-16:15 on 2023-10-23, two SPXW 1DTE calls (strikes 4225 and 4230, expiring 2023-10-24); the raw feed is not released with the paper.
- Research support as stated in that source: EPSRC Centre for Doctoral Training in Mathematics of Random Systems EP/S023925/1, funded by CBOE.
