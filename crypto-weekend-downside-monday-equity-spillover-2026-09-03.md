---
schema: strategy-research-record-v1
title: Crypto Weekend Downside to Monday U.S. Equity Spillover
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-market
  - event-driven
  - weekend
  - spillover
status: research-only
confidence: medium
source_as_of: 2025-06-01
sources:
  - "Mathis Mourey, Mohamad H. Shahrour, Florentina Şoiman, 'A crypto-stock weekend effect: Predicting Monday stock returns using weekend cryptocurrency returns', Finance Research Letters 86 (2025), 108661, DOI: 10.1016/j.frl.2025.108661"
  - "ScienceDirect open-access article: https://www.sciencedirect.com/science/article/pii/S1544612325019154"
  - "HAL post-print record: https://hal.science/hal-05415054v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Weekend Downside to Monday U.S. Equity Spillover

## Provenance

Primary source: Mathis Mourey, Mohamad H. Shahrour and Florentina Şoiman, *A crypto-stock weekend effect: Predicting Monday stock returns using weekend cryptocurrency returns*, *Finance Research Letters* 86 (December 2025), article 108661, DOI `10.1016/j.frl.2025.108661`. The publisher article is marked open access.

The source studies 20 large cryptocurrencies — BTC, ETH, BNB, SOL, XRP, ADA, AVAX, DOT, LINK, LTC, BCH, XLM, TRX, TON, CRO, HBAR, WBTC, ICP, NEAR and FIL — alongside the S&P 500, with Nasdaq, Russell 2000, S&P sector indices and the S&P Crypto Index used as robustness benchmarks. The stated sample runs from 2021-01-01 through 2025-06-01. The source also uses VIX and Fama-French SMB/HML controls.

Repository-wide source-identity checks on 2026-09-03 found no existing Alpha Strategy Pool record containing DOI `10.1016/j.frl.2025.108661`, the exact paper title, or the distinctive mechanism `negative weekend cryptocurrency return -> following Monday U.S. equity downside`. Read-only Wiki Brain search likewise found no matching record. Existing records on crypto seasonality, intraday spillovers, lead-lag, momentum, ETF flows and cross-asset signals do not normalize this same weekend-to-Monday cross-market construction.

This is a predictive research paper, not a source-specified executable trading strategy. Any concrete trade timing, threshold, instrument choice or holding rule below that is not explicitly stated by the source is labeled `research-proposed`.

## Economic mechanism

### Source-reported

The authors argue that cryptocurrencies trade continuously while U.S. equities close over the weekend, creating an information-discovery window in which crypto can incorporate global risk information before cash equities reopen. They report a pronounced asymmetry: negative weekend crypto returns predict negative Monday U.S. equity returns, whereas positive weekend crypto returns generally do not have comparable predictive power.

The source relates the asymmetry to stronger investor reaction to adverse information and documents a stronger crypto-to-equity transmission after the May 2022 LUNA collapse. A time-varying Kalman-filter analysis and an HMM regime exercise are used to characterize this post-LUNA strengthening.

### Research interpretation

The falsifiable mechanism is a **closed-market information spillover**:

1. adverse global information arrives while U.S. cash equities are closed;
2. continuously traded cryptocurrencies incorporate part of that information first;
3. broad negative weekend crypto performance becomes a proxy for latent global risk repricing;
4. the repricing is transmitted into U.S. equities when they next become tradable.

The mechanism is materially different from a generic crypto momentum or weekday-seasonality effect because the hypothesized alpha comes from a **market-hours mismatch across asset classes**, not from return continuation within crypto itself.

A critical distinction is that statistical predictability of a Monday daily return is not automatically tradable. If the source's Monday return includes the Friday-close-to-Monday-open gap, a cash-equity trade entered at the Monday open cannot capture the already-realized gap. This causal-timing issue is a primary falsification requirement, not a minor implementation detail.

## Signal

### Source-reported predictor

- **Predictor family:** weekend cryptocurrency return, separated into positive and negative cases.
- **Primary dependent variable:** Monday S&P 500 return.
- **Universe:** 20 large cryptocurrencies analyzed individually; BTC and ETH are highlighted as important transmitters.
- **Controls:** weekend crypto volatility, previous-week stock-index momentum, prior-Friday VIX, SMB and HML.
- **Volatility measure:** Parkinson high-low estimator; Garman-Klass is used as a robustness check.
- **Model:** Bayesian linear regression for static inference, then time-varying coefficients via Kalman filtering; an HMM is used to identify a structural regime shift around the LUNA collapse.
- **Directional finding:** negative weekend returns predict negative Monday equity returns; positive weekend crypto returns generally lack comparable predictive content.

### Source underspecification relevant to trading

The reviewed public article text does not provide an exact-enough executable definition for all of the following, so the source signal is **underspecified for direct trading reproduction**:

- exact timezone and start/end timestamps used to calculate `weekend cryptocurrency return`;
- exact close convention used for the Monday stock-index return;
- whether the dependent Monday return is close-to-close, open-to-close or another convention in the final data construction;
- a source-specified trading entry price, order type or holding-period rule;
- a source-specified return threshold beyond the sign split between positive and negative weekend returns;
- a source-specified aggregation rule combining multiple crypto assets into one tradable signal.

These gaps must not be silently filled and are central to whether the published predictability survives causal execution.

### Research-proposed executable hypotheses

The following are **research-proposed** branches for falsification only; they are not source-reported rules.

**Branch A — cash-equity continuation after the open**

- **Formation timestamp:** Monday 09:25 America/New_York, using only crypto prices observed through that time. `research-proposed`.
- **Weekend/closed-window return:** BTC log return from Friday 16:00 America/New_York to Monday 09:25 America/New_York. `research-proposed`.
- **Trigger:** if the closed-window BTC return is `< 0`, classify the session as downside-risk. `research-proposed`.
- **Entry:** short SPY at the first executable quote after Monday 09:30 America/New_York. `research-proposed`.
- **Exit:** cover at the Monday 16:00 closing auction or last executable quote before the close. `research-proposed`.
- **Holding period:** one U.S. cash session. `research-proposed`.
- **Purpose:** test whether any predictive content remains **after** the opening gap has already occurred.

**Branch B — pre-cash-open futures transmission**

- **Instrument:** front E-mini S&P 500 futures or Micro E-mini equivalent. `research-proposed`.
- **Formation timestamp:** Sunday immediately before the CME equity-index futures reopen. `research-proposed`.
- **Crypto observation window:** Friday 16:00 America/New_York to the latest causally available timestamp before futures entry. `research-proposed`.
- **Trigger:** negative BTC return over that closed-equity window. `research-proposed`.
- **Entry:** short ES/MES at the first causally executable futures quote after reopen. `research-proposed`.
- **Exit:** Monday cash close. `research-proposed`.
- **Purpose:** test whether the spillover is captured before the Monday cash opening gap rather than after it.

Any alternate threshold such as `BTC return < -1%`, volatility gating, BTC/ETH confirmation or a composite of multiple cryptocurrencies is a separate `research-proposed` branch and must be pre-registered rather than tuned retrospectively.

## Required data

- **Crypto instruments:** BTC and, for robustness, ETH plus the source's wider 20-coin set.
- **Crypto market type:** source uses cryptocurrency market prices; exact vendor/venue construction was not fully resolved in the reviewed public text. A modern replication should use a documented spot composite or fixed venue and must not mix spot/perpetual returns silently.
- **Equity instruments:** S&P 500 index for source replication; SPY for cash execution tests; ES/MES for pre-open futures tests are `research-proposed` adaptations.
- **Equity robustness benchmarks:** Nasdaq, Russell 2000, S&P sector indices and S&P Crypto Index as in the source.
- **Timeframe:** at least minute bars for causal timing tests; daily/high-low fields are sufficient for the source-style regression but not for gap decomposition.
- **Fields:** OHLC for crypto and equities; exact open/close timestamps; bid/ask or executable quotes for implementation tests; VIX; SMB; HML; prior-week index returns.
- **Volatility fields:** crypto weekend high and low for Parkinson; open/high/low/close for Garman-Klass robustness.
- **Point-in-time:** all crypto, VIX and factor information used for a Monday decision must be available before the trade timestamp; no Monday close information may enter formation features.
- **Timestamp:** normalize all feeds to UTC internally while preserving `America/New_York` cash/futures session boundaries and DST rules.
- **Missing data:** do not forward-fill stale crypto or futures prices across exchange outages. Missing weekend bars, stale quotes or market-closure anomalies must be marked missing rather than imputed without a pre-declared rule.
- **Universe integrity:** the source's stated 20 large cryptocurrencies should not be reconstructed using a current 2026 market-cap ranking and backfilled historically; that would create survivorship/selection contamination.
- **Costs:** observed/modeled spread, commissions, slippage and futures roll effects are required for executable testing.

## Execution assumptions

### Source-reported

The source reports predictive regressions and time-varying spillover evidence. It does **not** provide a directly executable cash-equity or futures strategy in the reviewed public text. Therefore there is no source-reported order type, fill model, latency assumption, leverage rule, position-sizing rule, stop, take-profit or transaction-cost backtest to inherit.

### Research-proposed for falsification

- Use the first causally available post-signal bid/ask rather than a same-bar close. **research-proposed**.
- For SPY, assume taker-style execution at or immediately after the Monday open and include observed opening spread/slippage. **research-proposed**.
- For ES/MES, enter only after the official futures reopen and use observed executable quotes; do not assume a fill at a pre-open theoretical price. **research-proposed**.
- Use fixed notional sizing for the first falsification pass; no volatility targeting or leverage optimization. **research-proposed**.
- Treat exchange outages, stale weekend crypto prints, delayed openings, holiday Mondays and futures limit states as explicit execution states rather than deleting observations. **research-proposed**.
- Separate the Friday-close-to-Monday-open gap P&L from Monday-open-to-close P&L so predictive information is not confused with executable alpha. **research-proposed**.

## Evidence

### Source-reported

- Publication: *Finance Research Letters* 86 (2025), article 108661, DOI `10.1016/j.frl.2025.108661`.
- Sample: 2021-01-01 through 2025-06-01.
- Universe: 20 large cryptocurrencies representing approximately 85% of crypto market capitalization in the source description.
- Main asymmetry: the source reports that negative weekend cryptocurrency returns significantly predict Monday S&P 500 declines, while positive weekend cryptocurrency returns generally do not.
- Breadth: 16 of the 20 cryptocurrencies are reported to show significant downside transmission in the negative-return analysis.
- BTC: the source reports a statistically significant weekend-return coefficient with posterior probability above 95% in the negative-return specification.
- ETH: the source reports significance for both weekend return and weekend volatility in the negative-return analysis.
- Robustness: the reported pattern remains across Nasdaq, Russell 2000, S&P sector indices and the S&P Crypto Index.
- Stablecoin placebo: stablecoins such as USDT/DAI are reported not to show the same predictive relationship.
- Regime dependence: the source reports stronger transmission after the May 2022 LUNA collapse, supported by time-varying Kalman-filter coefficients and an HMM structural-break exercise.

All figures above are **source-reported**. They have not been independently reproduced by ChatGPT and should not be interpreted as verified trading profitability.

### Independently reproduced

not independently reproduced

### Negative evidence

1. **No source trading P&L:** the paper establishes predictive regressions, not net executable strategy returns.
2. **Opening-gap ambiguity:** if the Monday dependent return includes the Friday-close-to-Monday-open gap, a Monday-open cash strategy may miss a material fraction of the reported effect.
3. **Weekend-definition sensitivity:** related literature shows crypto/equity Monday inference can change depending on whether Friday, Saturday, Sunday or another weekend reference is used; the exact source endpoint convention was not fully resolved in the public text reviewed here.
4. **Post-LUNA concentration:** the source itself reports a structural strengthening after May 2022, implying meaningful regime dependence rather than a stable unconditional coefficient.
5. **Short sample:** 2021-2025 spans only a few major crypto/equity regimes and relatively few weekly observations.
6. **Universe-selection risk:** the stated 20-coin set may embed ex-post large-cap selection if not reconstructed point-in-time.
7. **Multiple predictors:** analyzing 20 cryptocurrencies, multiple indices and regimes creates multiplicity risk even though the paper reports broad robustness.
8. **Tradability mismatch:** U.S. cash equities are closed during much of the signal window, while equity futures reopen Sunday evening; the exact tradable market-hours mismatch is therefore narrower than a simplistic `crypto trades / equities closed all weekend` narrative.
9. **No independent replication:** no source code/data reproduction was performed in this Scout cycle.

## Falsification plan

1. **Return-clock audit** — Reconstruct the paper's exact crypto weekend-return endpoints and Monday equity-return definition from the final article/supplement before any performance claim. **research-defined falsification threshold:** if the published directional result cannot be reproduced under the documented source clocks, reject the normalized source hypothesis as unresolved.
2. **Gap decomposition** — Decompose Monday S&P/SPY return into Friday-close→Monday-open and Monday-open→Monday-close components. **research-defined falsification threshold:** if predictive power exists only in the opening gap and Monday-open→close conditional mean is statistically indistinguishable from zero after costs, reject cash-open tradability while retaining only the pre-open information-spillover interpretation.
3. **Pre-open futures test** — Use ES/MES quotes after Sunday reopen with only crypto information available before entry. **research-defined falsification threshold:** if negative crypto returns have no negative conditional expectancy from first executable futures entry to Monday close after costs, reject the futures-translation hypothesis.
4. **Strict OOS continuation** — Freeze specification on 2021-2025 and test 2025-06 onward without retuning. **research-defined falsification threshold:** reject persistence if the sign of the negative-weekend coefficient reverses or the pre-registered executable branch has non-positive net mean return with no statistically credible downside separation.
5. **Clock perturbation** — Shift crypto formation endpoints by ±30/60 minutes and test Friday-close, Saturday, Sunday and pre-open definitions without optimizing. **research-defined falsification threshold:** downgrade to clock-fragile if the effect survives only one narrow arbitrary timestamp convention.
6. **BTC versus ETH versus broad basket** — Compare BTC-only, ETH-only and an equal-weight top-liquid-crypto basket with fixed point-in-time membership. **research-defined falsification threshold:** if the effect is driven by a single asset and disappears in the broader risk basket, classify the mechanism as asset-specific rather than systemic.
7. **Stablecoin placebo** — Repeat with USDT/USDC/DAI returns where meaningful. **research-defined falsification threshold:** if stablecoins generate equal or stronger predictive power absent depeg events, the proposed speculative-risk information channel is weakened.
8. **Regime split** — Evaluate pre-LUNA, LUNA/FTX stress, 2023 recovery, 2024 ETF regime and 2025-2026 periods. **research-defined falsification threshold:** reject generality if the effect is positive only in one crisis cluster or flips sign across two or more major regimes.
9. **Controls and competing explanations** — Add Friday VIX, prior-week equity momentum, futures overnight return and major weekend macro/news controls. **research-defined falsification threshold:** if crypto weekend return loses incremental predictive information once already-tradable equity-futures repricing is included, classify crypto as a coincident proxy rather than unique alpha source.
10. **Cost and opening-liquidity stress** — Apply observed SPY/ES spreads, commissions and slippage, especially around Monday open/Sunday reopen. **research-defined falsification threshold:** reject executable viability if expected net return becomes non-positive under median observed friction plus a 2x cost stress.
11. **Multiplicity control** — Pre-register assets, benchmarks and horizons and apply family-wise or false-discovery correction. **research-defined falsification threshold:** reject broad cross-market alpha if significance is not robust after pre-declared multiplicity adjustment.
12. **Universe point-in-time audit** — Reconstruct weekly eligible crypto assets without using future market-cap membership. **research-defined falsification threshold:** if broad significance disappears under point-in-time membership, classify the original breadth claim as selection-sensitive.

All cutoffs and decisions in this section are **research-defined falsification thresholds**, not source-reported acceptance criteria.

## Crypto portability

**Direct as a crypto-information source; adapted as a trading strategy.** The predictor itself is natively cryptocurrency-based, but the target asset is traditional U.S. equities. The source therefore provides direct evidence for a crypto-to-equity predictive relationship, not direct evidence for a crypto-only trading strategy.

Crypto-specific considerations:

- 24/7 crypto trading makes timestamp choice part of the signal definition.
- Spot venue fragmentation means `BTC weekend return` can differ across exchange/reference feeds during stressed weekends.
- Stablecoin quote depegs can contaminate USD-equivalent crypto returns.
- Perpetual funding, liquidation and mark/index effects are irrelevant to a pure spot predictor unless perps are substituted; any such substitution is **research-proposed**.
- Crypto market structure changed materially after 2022 and again after U.S. spot Bitcoin ETF adoption; the source's post-LUNA regime finding should not be assumed stationary through 2026.
- The weekend information advantage relative to U.S. equities is partly reduced once CME equity futures reopen Sunday evening, so a modern causal test must distinguish cash-equity closure from futures availability.

## Limitations

- **not independently reproduced:** ChatGPT did not reproduce the source regression or any trading branch in this cycle.
- **underspecified:** exact source weekend return endpoints/timezone and exact Monday-return clock were not fully resolved from the reviewed public article text.
- **unproven:** no net tradable alpha has been established from Monday cash-open or Sunday futures entry.
- **data gap:** the exact vendor snapshots and source data-processing code were not independently obtained.
- **causal timing limitation:** some or all predictive content may arrive in the Monday opening gap before a cash-equity trade is executable.
- **regime limitation:** the source reports a post-LUNA structural strengthening, indicating coefficient instability.
- **sample limitation:** 2021-2025 provides a modest number of weekly observations and includes exceptional crypto stress events.
- **selection limitation:** a fixed modern top-20 list cannot be backfilled without survivorship bias.
- **economic-mechanism limitation:** crypto may be a timely proxy for global risk news rather than a causal transmitter of information to equities.
- **execution limitation:** opening/reopen spreads, gaps and futures liquidity can materially alter a short-horizon strategy even when the regression is correct.

## Implementation status

No PyBroker, NautilusTrader, strategy registry, data pipeline, Kanban, Paper, Testnet or Live implementation has been created or modified by this Scout cycle.

`implementation_status: not-implemented`

## Adoption boundary

This record is Alpha Strategy Pool research material only. It captures a source-backed falsifiable hypothesis and does not establish profitable execution, implementation approval or permission for Paper/Testnet/Live trading.

`status: research-only`

`adoption: not-approved`

`approval_scope: research-only`

## Related Wiki records

No Hermes Wiki Brain record was written or modified in this Scout cycle. Read-only source-identity search found no matching Wiki record for this paper or distinctive weekend-crypto-to-Monday-equity mechanism. The canonical `strategy-research-record-v1` specification was read only to resolve the required schema.

## Sources

1. Mourey, M., Shahrour, M. H., and Şoiman, F. *A crypto-stock weekend effect: Predicting Monday stock returns using weekend cryptocurrency returns*. Finance Research Letters 86 (2025), 108661. DOI: https://doi.org/10.1016/j.frl.2025.108661
2. ScienceDirect open-access final article: https://www.sciencedirect.com/science/article/pii/S1544612325019154
3. HAL post-print record, version 1: https://hal.science/hal-05415054v1
4. EconPapers metadata/post-print index: https://econpapers.repec.org/RePEc:hal:journl:hal-05415054
