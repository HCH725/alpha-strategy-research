---
schema: strategy-research-record-v1
title: "Predatory Trading on Leveraged ETF Closing Rebalances: Equilibrium Manipulation, Overnight Reversal Alpha, and Predetermined Flow Exploitation"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - leveraged-etf
  - predatory-trading
  - market-microstructure
  - closing-auction
  - overnight-reversal
  - price-impact
  - order-flow
  - loop-gain
  - korean-equities
status: research-only
confidence: medium
source_as_of: 2026-08-04
sources:
  - "https://arxiv.org/abs/2608.03703"
  - "https://doi.org/10.48550/arXiv.2608.03703"
  - "https://arxiv.org/html/2608.03703v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Predatory Trading on Leveraged ETF Closing Rebalances: Equilibrium Manipulation, Overnight Reversal Alpha, and Predetermined Flow Exploitation

## Provenance

- **Canonical Academic Source:** Yinhong Zhao (Princeton University, Department of Economics; `yinhongz@princeton.edu`), *"Preying on Leveraged ETFs"*, arXiv preprint `arXiv:2608.03703v1 [econ.GN / q-fin.TR / q-fin.MF]`, submitted August 4, 2026. DOI: [10.48550/arXiv.2608.03703](https://doi.org/10.48550/arXiv.2608.03703). Full HTML text: [https://arxiv.org/html/2608.03703v1](https://arxiv.org/html/2608.03703v1).
- **Core Research Dataset:** Korea Exchange (KRX) daily stock panel covering 15,108 stock-days from January 2, 2024 through July 21, 2026; native KRX one-minute intraday bars with quote midpoints, bid-ask spreads, and signed volume from May 4 through June 30, 2026 (39 trading days: 15 pre-launch, 24 post-launch); KRX single-stock futures tick/bar files from April 1 through June 30, 2026; and international benchmark panels covering U.S. single-stock leveraged ETFs (NVDA, AMD, MSTR, TSLA, COIN, PLTR, META, AMZN) and U.S. index complexes (SPY, QQQ, IWM, DIA).
- **Pre-Write Deduplication Audit:** Repository-wide grep verified zero matches for `2608.03703`, `Yinhong Zhao`, `Preying on Leveraged ETFs`, or `predatory trading` in equity rebalances. While companion work by Jihwan Woo (`arXiv:2608.22768v1`, documented in `loop-gain-matrix-letf-rebalancing-crypto-closing-pressure-2026-09-02.md`) focuses on the scalar-versus-matrix stability monitoring blind spot across multi-asset ETP complexes (Korean LETFs vs. MSTR-BTC-COIN) and reports a null for crypto cross-asset spillover, Zhao (`arXiv:2608.03703v1`) investigates an entirely distinct, microfounded game-theoretic and empirical question: an equilibrium model of predatory trading and price manipulation on single-stock closing auctions, deriving an exact implementable trading rule (Appendix D.5), measuring the manipulation share of pre-close price drift, and tracking the complete next-day and overnight return reversal dynamics.

## Economic mechanism

### Source-reported

Leveraged exchange-traded funds (LETFs) and inverse ETFs promise investors a constant multiple $L$ of an underlying asset's daily return ($+2\times$ for double-long, $-2\times$ for double-inverse). To maintain constant leverage from one trading day to the next, funds must rebalance their exposure before the market close:
$$d_t = A (L^2 - L) r_t$$
where $A$ is net asset value and $r_t$ is the return of the underlying asset over the day.

Four structural properties govern this flow:
1. **Momentum Directionality:** Because $L^2 - L > 0$ for all $L \notin [0, 1]$ ($L^2 - L = 2$ for $+2\times$, and $L^2 - L = 6$ for $-2\times$), both long and inverse funds trade in the same direction as the day's move. On an up day, both must buy; on a down day, both must sell. Rebalancing capital aggregates across products:
   $$K = \sum_i A_i |L_i^2 - L_i|$$
   Long and inverse flows never net out. In the Korean laboratory, same-day creation and redemption offset absorbs 25% to 29% of gross flow, leaving 71% to 75% of mandated net flow hitting the market.
2. **Deterministic Predictability:** Every input ($A$, $L$, and the intraday return $r_t$) is publicly observable. Market participants can calculate the precise mechanical order arriving at the close minutes before the auction.
3. **Upward-Sloping Demand Curve at a Self-Referential Price:** In modern equity markets, LETF NAV is struck at the official closing call auction print, and the fund executes within that very auction. If the closing print clears higher by $\varepsilon$, the fund's contractual purchase is larger by $K \varepsilon$. The demand schedule submitted into the single-price call auction is strictly upward-sloping: the higher the price, the more the fund is forced to buy.
4. **Predatory Trading and Order Manufacturing:** Strategic arbitrageurs anticipate the closing rebalance flow. Facing upward-sloping mechanical demand, arbitrageurs pre-accumulate inventory during continuous afternoon trading (e.g., 15:10–15:20 KST) in the direction of the expected order. By pushing the closing print higher, an arbitrageur's trade at the print enlarges the fund's contractual order by:
   $$m \ell = \frac{\ell}{1 - \ell}$$
   shares per share purchased, where $\ell = \Lambda_c K$ is the loop gain and $m = 1 / (1 - \ell)$ is the price multiplier. When $\ell > 0.5$, the automaton more than replaces each share purchased at the print ($m\ell > 1$). The strategic trader unloads into the very demand they manufactured.
5. **Overnight and Next-Day Reversal Chaining:** The closing print over-weights public news by an overshoot factor $\Pi_0 - 1$ ($\hat{\Pi}_0 \approx 1.96$). Because the closing price is displaced away from fundamentals, deep capital reprices the stock toward fair value overnight. The following day's open gaps back ($g_+ = \varepsilon_+ - \theta e_t$, where $\theta \approx 0.68$ is the empirical correction speed). The mechanical fund, forced to rebalance on the reversal it helped create, buys high and sells low every cycle, generating an echo loading of $-\Pi_0(\Pi_0 - 1)$ on the initial news shock over the next cycle (a ~75% reversal of the first-day move).

### Research interpretation

This paper models and empirically demonstrates a predatory front-running and manipulation alpha mechanism exploiting contractual execution constraints.

The falsifiable core hypothesis is: **When a leveraged ETP or constant-leverage derivative complex achieves high rebalancing saturation relative to closing auction liquidity ($\ell = \Lambda_c K > 0.20$ or saturation ratio $S_t = |\hat{d}^{pre}_t| / W^{auc}_t > 0.5$), rational counterparties pre-position ahead of the close in the direction of the mechanical order, driving the closing print to a transient, non-fundamental overshoot. This generates a two-part exploitable effect: (1) an intraday trade holding into the closing auction print fails because execution friction and market-maker warehousing concessions destroy profit; whereas (2) taking the side of predetermined demand before close and holding overnight to the next open, or fading the displaced closing print overnight, captures an economically large mean-reversion alpha.**

Key economic boundaries and distinctions:
- **Predation vs. Mere Anticipation:** Pure front-running (anticipation) provides liquidity to an invariant order and stabilizes prices. In contrast, under self-referential closing execution, traders push the reference price to artificially inflate the counterparty's contractual order size (manipulation share reaches ~80% at $\ell = 0.73$).
- **Absence of Same-Day Price Push:** The distortion is not an instantaneous price jump occurring strictly within the 10-minute call auction ($R^2 = 0.001$ on news inside the auction); it is an information loading built gradually during the continuous session (by 15:20 KST) that overshoots fundamentals and unwinds overnight.
- **Retail Wealth Transfer:** Retail investors holding the leveraged products bear the cost (~KRW 3.96 trillion lost across 8 weeks in SK Hynix products), which is completely invisible in traditional tracking error metrics because NAV is struck at the displaced print itself.

## Signal

The trading logic is specified in normalized form based on the model's closed-form equilibrium and the empirical implementable rule evaluated in Appendix D.5.

### 1. Target Universe & Regimes
- **Underlyings:** Stocks or liquid crypto assets referenced by large constant-leverage ETPs, leveraged tokens, or delta-hedging swap complexes.
- **Regime Filter (Saturation Threshold):** Calculate the predetermined demand at 10 minutes prior to the closing auction:
  $$\hat{d}^{pre}_t = K_{t-1} \cdot r^{pre}_t$$
  where $K_{t-1}$ is disclosed aggregate rebalancing capital net of estimated creation/redemption offset (0.72 $\times$ gross capital), and $r^{pre}_t = (P_{t, 15:10} - P_{t-1, close}) / P_{t-1, close}$.
- **Activation Gate:** The strategy fires only on high-saturation days where $S_t = |\hat{d}^{pre}_t| / \bar{W}^{auc} \ge 0.50$ (where $\bar{W}^{auc}$ is the 20-day median closing auction value) or estimated loop gain $\ell_t \ge 0.20$. In low-saturation regimes ($S_t < 0.20$, typical of U.S. index complexes), the signal is inactive.

### 2. Primary Implementable Trading Rule (Appendix D.5)
- **Formation Timestamp:** Formed at 15:10 KST (10 minutes before the 15:20 call auction cutoff).
- **Directional Trigger:**
  - If $\hat{d}^{pre}_t > 0$ (day-to-15:10 return is positive $\implies$ mechanical fund must buy): **Long Entry**.
  - If $\hat{d}^{pre}_t < 0$ (day-to-15:10 return is negative $\implies$ mechanical fund must sell): **Short Entry**.
- **Execution Timing:** Enter at the close of the first continuous price-forming bar at or after 15:11 KST (e.g., 15:11:00 to 15:11:59 bar close), paying half quoted spread.
- **Holding Period & Exit Logic (Two Horizons):**
  - **Horizon 1 (Same-Day Auction Exit - Evaluated & Refuted in D.5):** Exit at the 15:30 closing call auction print. *Empirical finding: Loses -11.9 bps gross and -16.8 bps net.*
  - **Horizon 2 (Overnight Holding - The Verified Implementable Edge):** Hold the position across the close and exit at the next day's opening print (09:00 KST). *Empirical finding: Earns +122 bps gross ($t = 1.78$, $N = 46$, hit rate 61%) compared to +49 bps in the pre-launch placebo.*

### 3. Complementary Echo Reversal Rule (Fading the Closing Overshoot)
- **Formation Timestamp:** Formed at 15:25 KST based on confirmed significant daily move ($|r^{pre}_t| \ge 1.0\%$).
- **Entry Trigger:** Fade the closing print by trading against the mechanical direction:
  - If $r^{pre}_t > +1.0\%$: Enter **Short** at the 15:30 closing auction print.
  - If $r^{pre}_t < -1.0\%$: Enter **Long** at the 15:30 closing auction print.
- **Exit Logic:** Exit at the next morning's open print (09:00 KST) to capture the overnight correction leg ($-0.38$ to $-0.94$ return loading), or hold to next-day close (15:30 KST) to capture the full $-0.93$ to $-1.85$ one-cycle echo reversal.
- **Methodological Rule (Gapped Marks - Appendix D.6):** Any test or execution signed by $s_t = \text{sign}(\hat{d}^{pre}_t)$ must commence strictly after the observation window and share no common price mark with the sign-formation window, preventing spurious bid-ask or measurement-error covariance.

## Required data

- **Instrument / Universe:** Cash equities (Samsung Electronics 005930.KS, SK Hynix 000660.KS), single-stock futures, and comparison control baskets (KOSPI large-cap non-eligible controls, semiconductor chain peers).
- **Venue:** Korea Exchange (KRX) Cash Equities (KRX-KOSPI) and KRX Derivatives Market (single-stock futures).
- **Market Type:** Spot equity and single-stock futures.
- **Timeframe & Fields:**
  - Daily: Official closing price, opening price, high, low, daily volume, and closing call auction cleared value ($W^{auc}_t$).
  - Intraday: 1-minute OHLCV bars with end-of-interval quote midpoints, quoted bid-ask spread, and signed trade volume.
  - Product Disclosures: Daily fund AUM and shares outstanding for all domestic Korean LETFs/inverse ETFs and offshore products (Hong Kong CSOP, U.S. ADR products).
  - External Macro/Sector News Proxies: U.S. session closing returns (closing at ~05:00 KST) for VanEck Semiconductor ETF (SMH), Invesco QQQ Trust (QQQ), and SPDR S&P 500 ETF (SPY).
- **Point-in-Time Availability:** Fund AUM is published prior to trading; U.S. overnight shocks are fixed 4 hours before local open; predetermined demand $\hat{d}^{pre}_t$ is computable at 15:10 KST using only data realized through 15:10.

## Execution assumptions

- **Order Timing & Type:**
  - Front-running entry: Market/marketable limit orders at 15:11 KST continuous bar close.
  - Auction exit / entry: Market-on-Close (MOC) or limit orders submitted prior to the 15:20 KST batch auction freeze.
  - Opening exit: Market-on-Open (MOO) orders participating in the 08:30–09:00 KST opening call auction.
- **Transaction Costs & Spread:** Quoted half-spread paid at entry; continuous half-spread averaged 3 to 5 bps for treated names; batch auction clearing fee is standard exchange fee without continuous spread crossing.
- **Short-Selling & Borrow Constraints:** Short sales in Korean equities are subject to strict regulatory constraints and potential borrow availability bottlenecks, especially on acute down days (introducing empirical asymmetry between long and short legs).
- **Capacity / Saturation:** The strategy operates against an institutional flow of KRW 100 billion to KRW 500 billion per day; strategic capacity is bounded by the competitive arbitrageur parameter ($N \approx 4$ to $5$ counterparties).

## Evidence

### Source-reported

1. **Rebalancing Dose and Auction Saturation:**
   - On SK Hynix, median post-launch predetermined demand saturation ratio was $S_t = 1.02$: on half of all trading days, the mechanical order exceeded the entire value cleared by the 10-minute closing auction (max $S_t = 2.51$; $S_t > 1.0$ on 12 of 24 post-launch days).
   - Flow-weighted loop gain evaluated at the automaton's true order size on native tape was $\ell = 0.732$ for SK Hynix and $\ell = 0.245$ for Samsung Electronics, roughly 3 times the most extreme U.S. single-stock complex (MSTR at ~0.18) and an order of magnitude above U.S. index complexes (~0.001 to 0.05).
2. **Price Echo and One-Cycle Reversal:**
   - Regressing next-day close-to-close returns on pre-open U.S. news shocks: the treated-post cell (Samsung and SK Hynix after May 27, 2026) exhibits a coefficient of $-0.93$ ($t = -3.53$) on SMH semiconductor shocks, $-1.85$ ($t = -2.98$) on QQQ broad tech shocks, and $-3.30$ on SPY market shocks (all $p < 0.01$).
   - Stacked triple difference (shock $\times$ treated $\times$ post): $-0.96$ ($t = -5.34$) on SMH.
   - Exact randomization inference across all 66 possible pairs of 12 Korean stocks: the true treated pair produces the most negative estimate of all 66 pairs ($p = 0.015$, the theoretical minimum p-value).
   - Placebo launch dates: 0 of 47 placebo launch dates in the pre-period matches the true estimate ($p < 0.001$), sitting ~13 placebo standard deviations below the median.
   - Comparison cells (U.S. NVDA and AMD with listed $2\times$ products facing the identical SMH shock in the identical weeks) show $+0.04$ ($t = 0.30$), with zero reversal.
3. **Overnight Correction Timing:**
   - The reversal begins immediately overnight: next-day open return loading on the prior shock is $-0.38$ (SMH), $-0.94$ (QQQ), and $-2.31$ (SPY).
   - Intraday tracking shows the news loading builds to ~0.45 at the 15:30 print, is ~0.00 at next open, and reaches $-0.15$ by next close (randomization $p = 0.004$ across 4,278 intraday placebo pair assignments).
4. **Size and Sign Asymmetry:**
   - Splitting by shock magnitude: reversal loads entirely on large-shock days ($-0.99$, $t = -4.64$) versus small-shock days ($+0.84$, $t = 1.63$).
   - Down shocks show larger point estimates ($-1.50$, $t = -5.40$) than up shocks ($-0.83$, $t = -1.15$), consistent with short-sale frictions and dealer withdrawal during selloffs.
5. **Conditional Volatility & Trading Migration:**
   - Each percentage point of overnight U.S. shock generates $+0.67$ ($t = 2.80$) percentage points of additional next-day absolute return against large-cap controls, and $+0.85$ ($t = 2.90$) against tech peers.
   - Treated single-stock futures closing-call share of session traded value quadrupled from 0.3% to 1.3% ($+0.85$ pp, $t = 5.9$, $p = 0.022$).
6. **Welfare Loss and Structural Replay:**
   - Setting $\ell = 0$ in the structural model replay indicates the loop added 46.9 percentage points of annualized volatility to SK Hynix (realized 121.2% vs. counterfactual 74.1%).
   - Transferred KRW 3.96 trillion (US$2.61 billion) from SK Hynix product holders over 8 weeks (~17.6% of initial retail investment lost to the loop alone).
7. **Implementable Rule PnL (Appendix D.5):**
   - Entering at 15:11 KST continuous bar close and exiting at 15:30 closing print: **$-11.9$ bps gross, $-16.8$ bps net**.
   - Entering at 15:11 KST continuous bar close and exiting at next open (09:00 KST): **$+122$ bps gross ($t = 1.78$, $N = 46$, hit rate 61%)** vs. $+49$ bps pre-launch placebo.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Failure of Same-Day Auction PnL:** Taking the side of predetermined demand at 15:11 and exiting at the 15:30 closing auction loses $-16.8$ bps net. There is no instantaneous positive price push between 15:11 and 15:30 to harvest at the auction print; alpha requires holding across the overnight repricing window.
2. **Flat Auction-Window News Loading:** The auction-window return (15:20 to 15:30) carries no incremental loading on news ($-0.03$, randomization $p = 0.18$), refuting the hypothesis that the distortion is generated by chaos inside the 10-minute auction.
3. **Signed Same-Day Reference Jump Null:** On native auction data, the treated-post signed reference jump is $-6.7$ bps ($t = -0.42$, $p = 0.48$), and $-15.0$ bps ($t = -1.10$, $p = 0.34$) net of contemporaneous futures moves.
4. **Refutation of Liquidity-Provider Disparity Blowout:** An earlier theoretical conjecture that market maker withdrawal would blow out the ETF price-to-NAV disparity was empirically refuted: disparity averaged ~1.0%, peaked at 1.35% in June (before the July crash), and showed no relationship to volatility.
5. **Samsung Calibration Discrepancy:** The structural model calibrated to measured primitives ($\ell = 0.245$) reproduces SK Hynix's overshoot ($\Pi_0 = 1.96$ at $N = 4.4$), but cannot generate Samsung's observed $-0.94$ reversal at any competition level, representing an open provenance/fitting gap.

## Falsification plan

1. **Placebo Testing on Low-Loop-Gain Complexes:**
   - Run the exact identical D.5 trading rule and echo regression on U.S. single-stock LETF underlyings (NVDA, TSLA, AAPL) where $\ell < 0.05$.
   - *Falsification criteria:* If low-dose complexes exhibit statistically significant next-day reversals ($\beta < -0.30$, $t < -2.0$) or overnight rule returns $> +50$ bps, the observed Korean effect is driven by an unmodeled omitted variable rather than rebalancing loop gain.
2. **Pre- versus Post-Regulatory Intervention Test:**
   - Evaluate the KOSPI single-stock LETF panel after the July 16, 2026 regulatory restrictions (minimum deposit increased to KRW 30M, new listings frozen, trading unit minimums).
   - *Falsification criteria:* If the next-day echo loading does not attenuate proportionally to the reduction in daily rebalancing capital $K_t$, the mechanical hypothesis is weakened.
3. **Auction Depth & Friction Inversion:**
   - If market-on-close execution costs or overnight gap risk exceed the +122 bps gross margin (e.g. widening bid-ask spreads $> 30$ bps or overnight gap slippage $> 100$ bps), the net realizable strategy alpha collapses to zero.
4. **Shuffled Flow & Clock-Shift Placebo:**
   - Form pseudo-predetermined demand at 11:00 KST or 13:00 KST, or randomly shuffle the sign $s_t$.
   - *Falsification criteria:* If shifted formation times produce similar overnight return splits, the mechanism is an artifact of unconditional intraday momentum or diurnal seasonality rather than closing auction rebalance flow.

## Crypto portability

**Portability Status:** Adapted / Unproven.

The mechanism is ported from traditional Korean equity markets to cryptocurrency markets as a research hypothesis. The empirical claims in the paper derive strictly from KRX equities and do not constitute crypto empirical proof.

### Portability Mechanics & Crypto Adaptation:
1. **Binance / Bybit Leveraged Tokens (BLVT / Leveraged Tokens):**
   - Centralized crypto exchanges offer leveraged tokens (e.g., BTCUP, BTCDOWN, ETH3L, ETH3S) that rebalance dynamically or daily at fixed times (typically 00:00 UTC or upon reaching threshold intraday leverage drift).
   - *Structural difference:* Crypto exchanges do not run a 10-minute centralized batch call auction at 00:00 UTC; instead, automated rebalancing algorithms execute via continuous market/limit orders across continuous order books. This eliminates the self-referential single-price call auction feedback, significantly reducing the "manufactured order" multiplier.
2. **CME Bitcoin & Ether Futures Closing Auctions:**
   - CME cryptocurrency futures execute a daily volume-weighted or fix closing price (16:00 London or 16:00 New York), which is used to benchmark crypto ETFs (e.g., BITO, ProShares $2\times$ Ether ETFs).
   - To the extent that U.S.-listed spot or futures-based leveraged crypto ETFs (e.g. $2\times$ Bitcoin ETFs) grow to represent a substantial fraction of CME closing volume, closing pressure and next-day reversals may manifest on CME futures.
3. **Perpetual Funding Settlement (8-Hour Cycles):**
   - Constant-leverage vaults, automated basis strategies, and delta-neutral yield aggregators often rebalance on 8-hour funding intervals (00:00, 08:00, 16:00 UTC).
   - If collective automated rebalancing flow creates an upward-sloping demand curve against a specific TWAP or mark price print, predatory front-running during the 15 minutes preceding funding settlement could replicate the dynamics documented by Zhao.
4. **Portability Risks:**
   - 24/7 continuous trading without an overnight market closure: the "overnight" correction leg in crypto must occur continuously over subsequent 2- to 8-hour blocks rather than in a discrete gap.
   - Lack of short-selling bans in crypto perps makes negative liquidity shocks more symmetric than in Korean cash equities.

## Limitations

- **Small Sample Size for High-Dose Episode:** The high-dose treated regime comprises only 24 trading days of native intraday data (May 27–June 30, 2026) and 38 post-launch daily observations through July 21, 2026. While randomization inference over 66 pairs confirms significance at the $p = 0.015$ floor, structural power is constrained.
- **Samsung Fitting Failure:** The structural model accounts cleanly for SK Hynix's overshoot and volatility at $N = 4.4$ counterparties, but underpredicts Samsung's observed $-0.94$ reversal, suggesting that cross-stock contagion, index pass-through, or unmodeled foreign swap dealer behavior contributed to Samsung's pricing error.
- **Short-Sale Execution Friction:** Capturing the short leg of the echo reversal in cash equities requires borrow access, which became scarce and expensive during the Korean market collapse.
- **Vendor Data Truncation Trap (Appendix D.7):** Commercial data vendors often truncate Korean intraday feeds at 15:00 KST, omitting the 15:20–15:30 closing auction. Splicing commercial 15:00 prices with official 15:30 closes produces spurious corporate-action artifacts ($t = 37$ ghost anomalies). Research must use native exchange auction records.
- **Research Only Boundary:** This record represents market microstructure research into mechanical order flow predation and does not constitute an operational trading strategy or investment recommendation.

## Implementation status

- `not-implemented`: No implementation exists in our PyBroker or NautilusTrader repositories.
- No historical backtest has been performed within our internal backtest engines.
- This research capture does not authorize paper trading, testnet deployment, or live capital allocation.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- Research capture is strictly for theoretical understanding of mechanical ETP closing rebalance feedback and predatory front-running alpha. Any future implementation or deployment would require explicit review and separate validation.

## Related Wiki records

- `[[loop-gain-matrix-letf-rebalancing-crypto-closing-pressure-2026-09-02]]` (Jihwan Woo, arXiv:2608.22768v1; multi-asset loop-gain matrix and MSTR-crypto null)
- `[[crypto-short-horizon-prediction-market-settlement-push-reversal-2026-09-01]]` (Predatory settlement push and reversal in binary prediction markets)
- `[[quant/strategy-research-record-spec-v1]]` (Authoritative specification for strategy research records)

## Sources

1. **Primary Working Paper:**
   - Author: Yinhong Zhao (Princeton University)
   - Title: *"Preying on Leveraged ETFs"*
   - Identifier: arXiv:2608.03703v1 [econ.GN / q-fin.TR / q-fin.MF]
   - Date: August 4, 2026
   - Stable URLs:
     - Abstract: [https://arxiv.org/abs/2608.03703](https://arxiv.org/abs/2608.03703)
     - DOI: [https://doi.org/10.48550/arXiv.2608.03703](https://doi.org/10.48550/arXiv.2608.03703)
     - Full Text HTML: [https://arxiv.org/html/2608.03703v1](https://arxiv.org/html/2608.03703v1)
2. **Key Exhibits and Sections Cited:**
   - Section 2.1–2.4: Rebalance arithmetic, saturation ratio $S_t = |\hat{d}^{pre}_t| / W^{auc}_t$, and loop gain $\ell = \Lambda_c K$.
   - Section 3.1–3.3: Equilibrium model, Proposition 1 (auction pass-through), Proposition 2 (equilibrium loadings), Proposition 3 (chaining ratio identity), Proposition 4 (threshold ladder), Proposition 5 (manufactured order rate $m\ell$ and manipulation share), Proposition 6 (holder loss).
   - Table 1 (Main text): Echo regressions of next-day returns and overnight returns on pre-open public U.S. shocks (SMH, QQQ, SPY).
   - Section 5.1–5.2 & Table 2: Model calibration ($\hat{\ell} = 0.732$, $\hat{\rho}^g = 0.43$, $\hat{N} = 4.4$, $\hat{\Pi}_0 = 1.96$), excess volatility replay (+46.9 pp for SK Hynix), and KRW 3.96T holder toll.
   - Appendix D.5: Table A18, *"The implementable rule"* (+122 bps gross overnight, $-16.8$ bps net auction exit).
   - Appendix D.6: *"The shared-mark rule"* for signed test econometrics.
