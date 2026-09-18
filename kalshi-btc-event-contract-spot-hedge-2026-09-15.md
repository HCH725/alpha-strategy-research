---
schema: strategy-research-record-v1
title: "Kalshi BTC Event Contracts as Option-Like Hedges for Spot Crypto Exposure"
created: 2026-09-15
updated: 2026-09-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - bitcoin
  - kalshi
  - prediction-market
  - hedging
  - portfolio-construction
  - event-contracts
  - black-scholes-proxy
  - mispricing-signal
  - fee-erosion
  - negative-evidence
status: research-only
confidence: low
source_as_of: 2026-09-13
sources:
  - "Prashanth Bhaskara and Aadit Jerfy, 'Public Opinion as an Option: Leveraging Prediction Markets to Hedge Exposure to Spot Crypto Volatility', arXiv:2609.14267v1 [cs.CE, q-fin.TR], September 13, 2026. https://arxiv.org/abs/2609.14267"
  - "Full text HTML reviewed 2026-09-19: https://arxiv.org/html/2609.14267v1 (Methodology §§2.1–2.4, Results §3, Tables 1–2, market URLs in References [2]–[4])"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Kalshi BTC Event Contracts as Option-Like Hedges for Spot Crypto Exposure

## Provenance

- **Source**: arXiv:2609.14267v1 [cs.CE, q-fin.TR]
- **Authors**: Prashanth Bhaskara, Aadit Jerfy (University of Chicago)
- **Version**: v1, submitted September 13, 2026
- **DOI**: https://doi.org/10.48550/arXiv.2609.14267
- **URL**: https://arxiv.org/abs/2609.14267
- **Full text**: https://arxiv.org/html/2609.14267v1 (reviewed 2026-09-19)
- **Length**: 9 pages, 6 figures; MSC 91G20
- **Proof of concept**: Bitcoin spot + three Kalshi BTC price-event contracts
- **Update note (2026-09-19)**: material update of the 2026-09-15 capture. Same source identity and same hedge-overlay mechanism; this revision fills signal construction, probability formula, contract IDs, fee schedule, regime results, and negative evidence that the prior record correctly marked as unavailable from the abstract alone.

### Named Kalshi markets (source-reported References [2]–[4])

| Regime label (paper) | Market question | Kalshi market / series ID | Source-stated sample window | Source-stated BTC return |
| --- | --- | --- | --- | --- |
| Bullish | Will BTC max reach $100k+ by Dec 31 2024? | `kxbtcmaxy-24dec31` (series `kxbtcmaxy`) | Mar–Dec 2024 | +36.23% |
| Moderate/flat | Will BTC close above $100k by December 31 2025? | `kxbtc2025100-25dec31` (series `kxbtc2025100`) | Nov–Dec 2025 | −3.58% |
| Bearish | How high will Bitcoin get in January? / BTC monthly one-touch | `kxbtcmaxmon-btc-26jan31` (series `kxbtcmaxmon`) | Jan 2026 | −26.02% |

Public market URLs preserved from the paper references:
- https://kalshi.com/markets/kxbtcmaxy/how-high-will-bitcoin-get-this-year/btcmaxy-24dec31
- https://kalshi.com/markets/kxbtc2025100/will-bitcoin-reach-100k-again-this-year-/kxbtc2025100-25dec31
- https://kalshi.com/markets/kxbtcmaxmon/bitcoin-monthly-one-touch/kxbtcmaxmon-btc-26jan31

### Repository Deduplication Audit

Same source identity (`arXiv:2609.14267`) already exists as `kalshi-btc-event-contract-spot-hedge-2026-09-15.md`. Per the canonical deduplication rule, this cycle **updates that record** rather than creating a parallel artifact. Adjacent prediction-market records remain different mechanisms:

- `kalshi-prediction-market-macro-repricing-volatility-forecasting-2026-09-01.md` — macro repricing / vol forecasting
- `kalshi-prediction-market-pricing-wedge-executable-spread-falsification-2026-09-13.md` — pricing wedge / spread
- `crypto-kalshi-prediction-market-macro-repricing-2026-09-01.md` — macro repricing family
- Polymarket FLB / lead-lag / settlement / binary EV records — different venue and different normalized rules

This record remains a **portfolio hedge / active event-contract overlay** using Kalshi BTC price-event contracts as synthetic options against spot BTC, not a standalone arb.

## Economic mechanism

### Source-reported

Bhaskara and Jerfy treat Kalshi crypto event contracts on Bitcoin’s future price as **option-like claims** and construct a two-fund portfolio of spot BTC plus Kalshi contracts, rebalanced to hedge spot volatility without abandoning spot exposure.

Motivation (source): retail BTC hedging via futures/CFDs faces basis risk, margin, and US access friction; listed options face high premiums and low liquidity. Kalshi crypto events, launched from early 2024, aggregate public opinion into derived spot forecasts and are framed as leveraged hedging instruments.

The paper’s structural claim is that **market-implied probability** (Kalshi contract price in cents) can diverge from a **theoretical risk-neutral ITM probability**, and that actively trading that differential while holding spot improves risk metrics across bullish, flat, and bearish regimes versus unhedged spot and a static short hedge.

### Research interpretation

The reconstructable hypothesis is not “Kalshi always hedges,” but:

> For BTC-linked Kalshi one-touch / threshold events, a transparent modified Black-Scholes ITM probability minus Kalshi-implied probability defines a mispricing signal; a dynamic spot + event-contract portfolio rebalanced on that signal can modestly improve return/drawdown/Sharpe versus buy-and-hold or a static hedge, **conditional on fees, liquidity, and latency remaining manageable**.

Scout interpretation: the economic channel is **sentiment-driven binary prices vs model risk-neutral probability**, with the event contract used as a nonlinear hedge/overlay on spot — not linear futures basis and not a pure alpha long entry. Crypto-native because both legs are BTC-linked (spot USDT + Kalshi BTC events).

## Signal

### Source-reported (full paper body; replaces the prior abstract-only gap)

**Formation / sampling (source):**
- Binance BTC/USDT 1-minute OHLCV via API for spot path (paper sample covers 2024, 2025, and January 2026).
- Kalshi 1-minute-level pricing for the three binary outcome contracts listed above.
- Signals are **computed every minute**, but Strategy C **trades only at the start of each rebalancing period**; between rebalances the position is held constant from the last rebalance.
- Rebalance intervals tested by the source: monthly, weekly, daily, 12h, 6h, **1h**. Source reports 1h generally performed better; Results exclusively use 1h rebalancing portfolios.
- Timezone / publication clock for Kalshi minute prints is not restated beyond “1-minute-level pricing data”; treat exact feed timezone as **underspecified** for bit-exact replication.

**Theoretical probability (source, Eq. 1):**

\[
p_i=\begin{cases}
1, & \text{if } \exists j\le i \text{ such that } \mathrm{BTC}_j\ge K,\\[4pt]
\Phi\!\left(\dfrac{\ln(S_i/K)-\tfrac12\sigma^2 T}{\sigma\sqrt{T}}\right), & \text{otherwise.}
\end{cases}
\]

- \(S_i\): BTC spot at time \(i\); \(K\): event strike from the Kalshi question; \(T\): time to event expiry; \(\Phi\): standard normal CDF.
- **One-touch lock-in (source):** if spot **ever** breached \(K\) before \(i\), theoretical probability is set to **1** (not a vanilla European terminal probability).
- **Volatility (source):** annualized historical BTC volatility computed **monthly**; each event contract uses BTC volatility of the **month prior to that market’s open**.
- **Model choice (source):** modified **vanilla** Black-Scholes ITM probability, **not** a barrier one-touch derivation — the authors state vanilla is preferred for relative mispricing because barrier models add parameter sensitivity, and limited liquidity impedes continuous repricing after threshold breaches.

**Market-implied probability (source):** Kalshi contract price in cents converted to a decimal probability (e.g., 65¢ → 0.65).

**Mispricing differential (source):**

\[
D = p_{\text{theoretical}} - p_{\text{implied}}
\]

**Five-level signal and position sizes (source; $100k initial capital per strategy):**

| Level | Condition | Action | Contract size |
| --- | --- | --- | --- |
| +2 | \(D > 15\%\) | Strong buy (Yes) | +5000 |
| +1 | \(D > 5\%\) | Weak buy (Yes) | +3000 |
| 0 | \(\lvert D\rvert < 2\%\) | Neutral / close position | 0 |
| −1 | \(D < -5\%\) | Weak short | −3000 (buy NO) |
| −2 | \(D < -15\%\) | Strong short | −5000 (buy NO) |

Source note: a short equates to **buying the NO contract** for the event.

**Three portfolio constructions (source):**

- **Strategy A**: unhedged buy-and-hold BTC spot.
- **Strategy B**: static hedge — long BTC spot + a single short of **1000** Kalshi Yes contracts entered at period start and held to expiry.
- **Strategy C**: long BTC spot + **active** Kalshi trading on the five-level \(D\) signals, rebalanced at the fixed interval (reported: 1h).

**Exit / holding (source):** position held until the next rebalance signal or neutral zone close; event contracts settle at Kalshi resolution; no separate stop/target ladder beyond the neutral band and period-end settlement is described.

**Parameters (source-reported, fixed unless noted):**

- Signal thresholds: 15% / 5% / 2% on \(D\)
- Sizes: 5000 / 3000 / 0 contracts by level; static hedge 1000
- Rebalance used in Results: **1 hour**
- Capital: **$100k** per strategy instance
- Vol: prior-month annualized historical vol (monthly update)
- Fees (source, Eq. 2): \(\mathrm{Fee}=\lceil 0.07\, C\, P (1-P)\rceil\), \(C=\) contracts, \(P=\) entry price in probability units

### Research interpretation / operationalization notes

`research-proposed` items **not** fully pinned by the source and required before any faithful reconstruction:

1. Exact Kalshi minute-feed timezone and whether 1-minute bars are exchange-native or resampled.
2. Whether mid, last, or a specific book level is used as \(P\) in the fee formula when computing paper performance.
3. How overlapping open events are handled when more than one Kalshi market is live (paper analyzes three **separate** single-market episodes, not a joint multi-event book).
4. Whether \(D\) uses pre-breach vanilla value only, or also logs post-breach \(p=1\) (post-breach implied should already be near 1; signal should be ~0 — confirm in any replication).
5. Point-in-time availability of Kalshi prints vs Binance 1m closes at rebalance timestamps.

The five-level rule itself is source-reported and reconstructable; the gaps above are **data/convention** gaps, not missing thresholds.

## Required data

- **Instrument**: Spot BTC (paper: BTC/USDT Binance) + Kalshi BTC price-event contracts (three named markets).
- **Universe**: The three event contracts above; not a cross-sectional crypto universe.
- **Venue**: Binance (spot OHLCV) + Kalshi (binary contract prices). Paper does not model multi-venue spot or Kalshi depth ladders.
- **Timeframe**: 1-minute bars for both legs; event horizons as defined by each Kalshi market’s expiry.
- **Fields**: BTC 1m OHLCV; Kalshi YES/NO prices; contract size \(C\); strike/question level \(K\); event expiry \(T\); fee schedule parameters.
- **Point-in-time**: Prior-month vol must be computed only from data available before market open; \(D\) at rebalance must use information available at that rebalance. Paper does not publish a formal PIT audit.
- **Timestamp**: Binance API timestamps; Kalshi minute stamps not restated — **underspecified**.
- **Missing-data**: not specified in source.
- **Funding/fee/spread**: Kalshi quadratic fee included in reported Strategy C “w/ fees” rows; latency, book liquidity, and slippage **not** modeled (source acknowledges).

## Execution assumptions

### Source-reported

- Aggressive order quantities used “to minimize profit erosion from transaction costs.”
- Fees integrated into performance calculations via Eq. 2.
- Latency and market liquidity **not** taken into account in the framework; authors posit future institutional/retail adoption could mitigate this and “converge results.”
- No partial-fill model, no queue priority, no Kalshi depth cap in the paper.

### Research interpretation

Treat all Strategy C P&L as **paper-style, fee-aware but friction-incomplete**. Binary 0/1 payoff plus unmodeled depth means implementable hedge ratios can differ materially from the 3000/5000 contract grid. Do not treat source Sharpe as executable Sharpe.

## Evidence

### Source-reported

Results use **1h rebalancing** for Strategy C; figures include fees unless labeled “no fees.”

**Total return (Table 1, source):**

| Regime | Strategy A (spot) | Strategy C (dynamic, as reported) |
| --- | --- | --- |
| Bullish 2024 | +36.23% | +38.69% |
| Moderate/flat Dec 2025 | −3.58% | narrative/table inconsistency (see Negative evidence) |
| Bearish Jan 2026 | −26.02% | narrative/table inconsistency (see Negative evidence) |

**Risk metrics with fees (Table 2, source, selected):**

| Market | Strategy | Sharpe | Max DD | Fee % Gross |
| --- | --- | --- | --- | --- |
| 2024 $100k max | A unhedged | 1.20 | −31.73% | — |
| 2024 | B static | 1.19 | −31.40% | — |
| 2024 | C dynamic w/ fees | 1.27 | −29.90% | **25.2%** |
| Dec ’25 | A | −0.76 | −10.59% | — |
| Dec ’25 | B | −0.63 | −10.15% | — |
| Dec ’25 | C w/ fees | **−0.10** | −9.26% | **16.8%** |
| Jan ’26 | A | −5.88 | −38.51% | — |
| Jan ’26 | B | −5.81 | −37.89% | — |
| Jan ’26 | C w/ fees | −5.55 | −37.17% | **25.2%** |

Source qualitative claims:
- Strategy C outperforms A and B across reported risk metrics **even with Kalshi fees**.
- Strategy C achieves roughly a **3% reduction in exposure** vs unhedged BTC in each regime (source wording).
- Bullish outperformance credited to 1h rebalancing capturing volatility/sentiment deviation.
- Implied and model probabilities compress as event expiry approaches.

### Independently reproduced

`not independently reproduced`

### Negative evidence

Source-reported cost/scaling negatives (now explicit from full text):

1. **Fee erosion**: across all regimes, roughly **20% of Strategy C’s gains** are eroded by Kalshi transactions; Table 2 shows Fee % Gross of **16.8%–25.2%** on Strategy C.
2. **High-frequency non-viability**: authors state fees make **high-frequency mispricing arbitrage non-viable**; an initial deployment with **hundreds of trades saw complete erosion of P&L**.
3. **Cost-benefit gate**: source stresses expected profit per trade must outweigh fees on the order of the quadratic schedule (~7% coefficient on \(C P(1-P)\)); trading activity requires explicit cost-benefit analysis.
4. **Latency and liquidity omitted**: paper acknowledges results can deviate in real markets; scalability “still limited by liquidity.”
5. **Narrative vs Table 1 inconsistency (scout-identified; not source-flagged)**: §3 narrative states Dec 2025 Strategy C returned **−0.96%** and Jan 2026 **−24.17%**, while Table 1 lists **−3.04%** and **−22.96%** for the same labels. Bullish row is consistent at +38.69%. Treat regime return magnitudes for flat/bear as **internally inconsistent in the source** until authors clarify; Sharpe/DD columns in Table 2 remain the more detailed risk evidence.
6. **Only three single-event episodes**, Bitcoin only; no multi-strike joint book; no walk-forward beyond choosing 1h among a small rebalance menu **using the same episodes** (selection on test is a methodological concern — scout interpretation).
7. Preprint, short paper, no public code repository cited.

## Falsification

Research-proposed falsification tests (not executed):

1. **Regime-blind / signal-blind baselines.** Compare Strategy C to (a) always-long spot, (b) always-hold static 1000 Yes/NO, (c) random \(D\)-threshold placebo with same trade count. **Research-defined falsification threshold:** if C does not beat the best simple baseline on out-of-sample net Sharpe after Eq. 2 fees, reject the adaptive-hedge claim.
2. **Fee schedule stress.** Re-run with fees = 0, paper Eq. 2, and 2× Eq. 2. **Research-defined falsification threshold:** reject tradable interpretation if net edge vs spot-only is non-positive at paper fees or flips sign under 2× fees.
3. **Rebalance menu locked ex ante.** Pre-register 1h only (source’s chosen interval) without peeking at other horizons on the same episodes; or evaluate all horizons on a **held-out** event not used to pick 1h. Fail adaptive-frequency claim if 1h advantage does not replicate OOS.
4. **Probability-model ablation.** (i) vanilla BS without one-touch lock \(p=1\); (ii) barrier/one-touch proper; (iii) book-implied only (no model \(D\)). Fail “model mispricing” claim if vanilla-with-lock is not better than book-only after costs.
5. **Vol window ablation.** Prior-month vol vs 30d realized vs EWMA. Fail if signal is an artifact of one vol choice.
6. **Liquidity cap.** Cap order size to observed Kalshi top-of-book / volume percentile. Fail implementability if grid sizes (3000/5000) are routinely unfillable or move price beyond paper assumptions.
7. **Venue substitution.** Same \(D\)-style rule on Polymarket BTC threshold markets or Deribit options hedge. Fail Kalshi-specificity claim only if mechanism is claimed portable; if only Kalshi works, document as venue-bound.
8. **Internal consistency audit.** Reconcile Table 1 vs §3 narrative returns before citing regime-level outperformance magnitudes.
9. **Leakage audit.** Ensure prior-month \(\sigma\) and \(S_i\) at rebalance use only data available at that timestamp; fail if any future print enters \(p_i\).
10. **Neutral-band sensitivity.** Perturb \(\lvert D\rvert<2\%\) close threshold; fail if results are knife-edge on that band.

## Crypto portability

**Direct** for BTC spot + the three named Kalshi BTC events; **adapted** for other Kalshi crypto events (ETH, etc.) if strike/threshold semantics and one-touch vs close-above rules are re-specified carefully.

- Spot is 24/7; Kalshi event resolution and trading hours are venue-specific — **clock mismatch** must be modeled.
- Two of three source markets are **max / one-touch** style (“max reach $100k+”); one is **close above**. Payoff semantics differ; the paper’s Eq. 1 one-touch lock is appropriate for max-touch questions but **mis-specified** if applied unchanged to close-above contracts without modification.
- Kalshi is a US-regulated prediction venue: access, fees, and KYC differ from crypto CEX options/perps.
- Event contracts are **binary (0/1)**, not linear options — hedge ratio is nonlinear in spot; no funding rate on Kalshi legs.
- Stablecoin/USDT quote effects apply to the Binance spot leg only.
- Crypto portability is **not** authorization to trade.

## Limitations

- Short exploratory preprint (9 pages); Bitcoin only; three single-event case studies.
- Signal thresholds and fee formula are now known from full text; feed timezone, fill convention, and multi-event book rules remain underspecified.
- **not independently reproduced**.
- Fees materially erode edge; paper itself rejects high-frequency use.
- Latency, depth, and slippage unmodeled; aggressive size assumption is optimistic.
- Internal inconsistency between §3 narrative returns and Table 1 for flat/bear regimes.
- Rebalance interval selected after inspecting the same episodes (methodological caution — scout interpretation).
- No public code; Kalshi historical 1m prints may be hard to obtain point-in-time.
- Incremental-write threshold for this 2026-09-19 revision: **met** via new reconstructable signal construction, new execution/cost evidence (fee schedule + erosion magnitudes), and new negative evidence (HF P&L destruction, liquidity limits, table/narrative conflict) that the 2026-09-15 abstract-level record could not carry.

## Implementation status

`not-implemented`

No Kalshi connector, BS event-probability engine, five-level \(D\) trader, or spot+event hedge portfolio exists in our research runtime. This update changes research documentation only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

This record remains research material. Presence here does **not** mean profitable, validated alpha, or approval for implementation, paper trading, testnet, or live trading. No record may promote itself by wording or evidence count.

## Related Wiki records

- [[quant/strategy-research-record-spec-v1]] — canonical schema
- `kalshi-btc-event-contract-spot-hedge-2026-09-15.md` — this file (prior abstract-level version; same path updated in place)
- `kalshi-prediction-market-macro-repricing-volatility-forecasting-2026-09-01.md`
- `kalshi-prediction-market-pricing-wedge-executable-spread-falsification-2026-09-13.md`
- `crypto-kalshi-prediction-market-macro-repricing-2026-09-01.md`
- `prediction-market-llm-confidence-weighted-value-bet-2026-09-04.md`
- `polymarket-favorite-longshot-bias-crypto-politics-2026-09-14.md`
- `polymarket-btc15-adaptive-conditional-probability-terminal-distance-uncertainty-fmz-11020-2026-09-18.md` — different venue/mechanism (Polymarket 15m EV architecture)
- `crypto-options-volatility-risk-premium-zscore-2026-08-31.md` / BTC options VRP family — linear/options alternatives, not Kalshi binaries

## Sources

1. Prashanth Bhaskara and Aadit Jerfy. "Public Opinion as an Option: Leveraging Prediction Markets to Hedge Exposure to Spot Crypto Volatility." arXiv:2609.14267v1 [cs.CE, q-fin.TR], September 13, 2026. https://arxiv.org/abs/2609.14267
2. Full-text HTML: https://arxiv.org/html/2609.14267v1 (reviewed 2026-09-19 for signal, fees, results, market URLs)
3. Kalshi market pages cited by the paper (public URLs listed under Provenance); access state as of paper references dated February 2026.
