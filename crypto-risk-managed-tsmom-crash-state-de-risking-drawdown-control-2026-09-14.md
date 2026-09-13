---
schema: strategy-research-record-v1
title: "Risk-Managed Time-Series Momentum in Crypto Majors: Crash-State De-Risking and Drawdown Control"
created: 2026-09-14
updated: 2026-09-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - time-series-momentum
  - risk-management
  - drawdown-control
status: research-only
confidence: medium
source_as_of: 2026-07-30
sources:
  - "Joseph Howden and Maksim Aleksandrovich Andreev, 'Risk-Managed Time-Series Momentum in Crypto Majors: Crash-State De-Risking and Drawdown Control', SSRN 7115459, July 30, 2026. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7115459"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Risk-Managed Time-Series Momentum in Crypto Majors: Crash-State De-Risking and Drawdown Control

## Provenance

- **Source:** Joseph Howden (MIT Sloan School of Management, Students) and Maksim Aleksandrovich Andreev (Unaffiliated), "Risk-Managed Time-Series Momentum in Crypto Majors: Crash-State De-Risking and Drawdown Control," SSRN working paper 7115459, 6 pages, posted July 30, 2026; written July 14, 2026.
- **SSRN URL:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7115459
- **DOI:** Not assigned (SSRN working paper).
- **Verification:** The SSRN abstract page was directly accessed and the abstract text confirmed to match the search-indexed version. The paper is 6 pages. No PDF download was completed in this scout run due to SSRN access limitations; all empirical claims below are `source-reported` from the abstract. A full primary-source checksum of the PDF body is recommended before any adoption decision.
- **Deduplication Audit:** A comprehensive search of all `.md` records in `alpha-strategy-research` found zero existing records matching SSRN 7115459, "Howden," "Andreev," or "crash-state de-risking." Adjacent TSMOM records in the repository (`crypto-dynamic-time-series-momentum-volatility-impulse-2026-08-31.md`, `hyperliquid-vol-targeted-tsmom-drawdown-calibrated-ratchet-2026-09-12.md`) evaluate different mechanisms (dynamic vol-scaled TSMOM, ATR-based adaptive stop, vol-targeting on Hyperliquid perps) and do not share the same source identity or the specific crash-state de-risking overlay tested here.

## Economic mechanism

### Source-reported

The authors study a fixed-lookback (L = 30 day) long/cash time-series-momentum (TSMOM) sleeve on liquid crypto-majors (BTC, ETH, BNB, XRP, ADA, SOL, DOGE), overlaid with a market-drawdown-state de-risking rule. The construction follows Moskowitz, Ooi and Pedersen (2012): hold each asset only while its trailing 30-day cumulative log-return is positive, otherwise rotate that allocation to cash; then scale the whole book's gross exposure down (×0.5) when the aggregate crypto market is more than 15% off its trailing peak.

The authors are explicit: "The headline finding is a drawdown-control result, not an alpha result." The strategy is described as "risk-managed β—a documented trend premium with crash protection—not market-neutral alpha."

### Research interpretation

The mechanism decomposes into two components:

1. **Primary signal (TSMOM):** Classic Moskowitz-Ooi-Pedersen time-series momentum — long assets with positive 30-day cumulative returns, cash otherwise. This exploits intermediate-term trend persistence in crypto, consistent with behavioral and structural explanations (retail chasing, leveraged liquidation cascades, persistent order-flow autocorrelation).

2. **Risk overlay (crash-state de-risking):** When the aggregate crypto market is more than 15% below its trailing peak, reduce gross exposure to ×0.5. This is a regime-conditional volatility/drawdown targeting rule designed to cut tail-risk drawdowns during crypto crash events. The 15% threshold is a `research-defined` parameter.

The economic thesis is that trend-following in crypto captures a positive expected return (trend premium) but suffers catastrophic drawdowns during regime reversals; the crash-state overlay reduces these drawdowns by mechanically deleveraging during stress periods.

## Signal

The signal is a **long/cash TSMOM sleeve with crash-state de-risking overlay** (`source-reported`):

1. **Lookback:** 30-day trailing cumulative log-return for each asset (`source-reported`, fixed a priori).
2. **Long entry:** Enter long on asset when its trailing 30-day cumulative log-return is positive (`source-reported`).
3. **Exit to cash:** Rotate allocation to cash when trailing 30-day cumulative log-return is non-positive (`source-reported`).
4. **Crash-state overlay:** When aggregate crypto market is more than 15% below its trailing peak, scale gross exposure to ×0.5 (`source-reported`). The 15% threshold is `research-defined falsification threshold`.
5. **Universe:** 7 liquid crypto-majors: BTC, ETH, BNB, XRP, ADA, SOL, DOGE (`source-reported`).
6. **Rebalancing frequency:** Not explicitly stated in the abstract; the L = 30 lookback implies at least daily evaluation (`data gap`).
7. **Position sizing:** Equal-weight across the long book when in long positions (`data gap` — not stated in abstract whether equal-weight or vol-weighted).

Parameters: L = 30 days (fixed, `source-reported` as a "recorded, accepted sharp-parameter fragility"), drawdown threshold = 15% (`research-defined falsification threshold`), de-risk multiplier = ×0.5 (`source-reported`).

The authors note that "vol-targeting / Kelly sizing on top of this sleeve was tested and SETTLED NULL (it de-levers the payoff engine)" (`source-reported`).

## Required data

- **Instruments:** BTC, ETH, BNB, XRP, ADA, SOL, DOGE perpetual futures or spot (`source-reported`; venue not specified in abstract).
- **Venue:** Not specified in abstract (`data gap`). Given the 7-asset universe and crypto-majors focus, likely Binance or similar major CEX.
- **Market type:** Perpetual futures or spot (`data gap`).
- **Timeframe:** Daily or sub-daily bars sufficient for 30-day lookback (`data gap` — not specified in abstract).
- **Fields:** Closing prices (for cumulative log-return calculation), aggregate crypto market index (for drawdown-state calculation) (`source-reported`).
- **Universe construction:** 7 liquid crypto-majors selected by the authors (`source-reported`). Survivorship and selection criteria not stated in abstract (`data gap`).

## Execution assumptions

- **Signal-to-order timing:** Not specified in abstract (`data gap`).
- **Execution lag:** Not specified in abstract (`data gap`).
- **Order type:** Not specified in abstract (`data gap`).
- **Fees:** Net-of-25bps round-trip costs applied (`source-reported`).
- **Slippage:** Not specified separately from the 25bps cost assumption (`data gap`).
- **Funding:** Not specified in abstract (`data gap`); likely relevant if perpetual futures are used.
- **Leverage:** Gross exposure scaled to ×0.5 under crash state (`source-reported`); maximum exposure not specified (`data gap`).
- **Capacity:** Not addressed in abstract (`data gap`).

## Evidence

### Source-reported

All empirical figures are `source-reported` from the SSRN abstract (Howden & Andreev 2026, SSRN 7115459):

- **OOS walk-forward (L = 30, net of 25bps):** Sharpe = 1.41 (Harvey-Liu-Zhu t = 3.21) versus buy-and-hold Sharpe = 0.70 (t = 1.60).
- **Maximum drawdown:** −44.6% (TSMOM) versus −84.4% (buy-and-hold) — roughly halved.
- **With crash-state de-risk overlay (×0.5 beyond 15% off-peak):** Max drawdown further reduced to approximately −28%; Calmar ratio lifted from roughly 1.56 to 1.98 while holding Sharpe near 1.53 (t = 3.69).
- **Survivorship-hardened universe:** Effect survives a frozen long-history universe.
- **50bps round-trip cost assumption:** Effect survives.
- **Offline grid (96 configurations):** 100% of configurations produced smaller max drawdown than equal-weight buy-and-hold.
- **Author caveats (source-reported):** Absolute returns are "survivorship-inflated"; the forward Harvey t > 3 promotion bar has "NOT yet been cleared"; the L = 30 optimum is "a recorded, accepted sharp-parameter fragility"; the sleeve is "paper-only and forward-accruing."

### Independently reproduced

Not independently reproduced. All empirical findings reflect third-party results reported by Howden & Andreev (2026, SSRN 7115459).

### Negative evidence

- The authors explicitly state this is "risk-managed β—a documented trend premium with crash protection—not market-neutral alpha" (`source-reported`).
- The L = 30 parameter is acknowledged as a "sharp-parameter fragility" — the optimum was selected from a 96-configuration grid, and the authors do not claim the parameter is robust to alternative specifications (`source-reported`).
- Absolute returns are acknowledged as survivorship-inflated due to the 7-asset universe selection (`source-reported`).
- Vol-targeting / Kelly sizing on top of this sleeve was tested and "SETTLED NULL" — it de-levers the payoff engine (`source-reported`).
- The Harvey-Liu-Zhu t > 3 promotion bar for multiple-testing-corrected significance has not yet been cleared (`source-reported`).
- The strategy is paper-only and forward-accruing; no live or testnet deployment (`source-reported`).

## Falsification plan

1. **Parameter sensitivity:** Test L ∈ {10, 15, 20, 30, 60, 90} and drawdown threshold ∈ {10%, 15%, 20%, 25%}. If performance degrades sharply outside narrow parameter ranges, the L = 30 / 15% specification is overfit (`research-defined falsification threshold`).
2. **Universe expansion:** Test on top-20 or top-50 crypto assets by market cap, not just 7 majors. If the drawdown-control benefit disappears in a broader universe with more diversification, the crash-state mechanism may be an artifact of concentrated major-coin correlation (`research-defined falsification threshold`).
3. **De-risk threshold timing:** Test the drawdown-state trigger at different measurement windows (e.g., trailing 7-day peak vs. trailing 30-day peak). If the 15% threshold only works with a specific peak-measurement convention, the result is fragile (`research-defined falsification threshold`).
4. **Alternative de-risk mechanisms:** Compare against simple vol-targeting (e.g., target 15% annualized vol), ATR-based position sizing, or trailing-stop exit. If these alternatives achieve similar drawdown reduction without the crash-state overlay, the specific de-risk mechanism adds no incremental value (`research-defined falsification threshold`).
5. **Out-of-sample forward test:** The authors note the Harvey-Liu-Zhu t > 3 bar has not been cleared. Continue forward-accruing until sufficient OOS data accumulates (`research-defined falsification threshold`).
6. **Action on failure:** If the de-risk overlay does not reduce max drawdown by ≥20% relative to vanilla TSMOM across multiple universe/parameter specifications, reject the crash-state mechanism as a useful risk overlay.

## Crypto portability

`direct` — the strategy is natively designed for and evaluated on cryptocurrency assets.

Crypto-specific considerations:
- The 7-asset universe is heavily concentrated in large-caps, which may exhibit high correlation during crashes, limiting the diversification benefit of the TSMOM sleeve.
- The 15% drawdown threshold is calibrated to crypto's historically high volatility; in lower-vol regimes the threshold may be triggered too frequently, de-leveraging during normal corrections.
- The 25bps cost assumption is reasonable for major CEX taker fees but may be optimistic for smaller-cap assets or during high-volatility periods when spreads widen.
- Funding costs are not addressed in the abstract; if perpetual futures are used, negative funding carry during trend-aligned positions could erode returns.

## Limitations

- **6-page working paper:** Limited methodological detail available from the abstract alone; full primary-source verification of the PDF body is recommended before any adoption decision.
- **Not independently reproduced.**
- **Survivorship bias:** The 7-asset universe was selected ex post; absolute returns are acknowledged as survivorship-inflated (`source-reported`).
- **Sharp-parameter fragility:** L = 30 is acknowledged as the result of grid-search optimization and may not be robust (`source-reported`).
- **Multiple-testing caveat:** The 96-configuration offline grid inflates the probability of finding a good result; the authors acknowledge the Harvey-Liu-Zhu correction bar has not been cleared (`source-reported`).
- **Risk-managed β, not alpha:** The authors explicitly frame this as a trend premium with crash protection, not a market-neutral alpha source (`source-reported`).
- **No live/testnet deployment:** Paper-only and forward-accruing (`source-reported`).
- **Data gaps:** Rebalancing frequency, position-sizing method, venue, market type, and funding treatment are not specified in the abstract (`underspecified`).

## Implementation status

`not-implemented`. No implementation of this specific TSMOM + crash-state de-risking overlay exists in our research stack, PyBroker, or NautilusTrader.

## Adoption boundary

This record is research material only. Its presence in this repository does **not** constitute:
- evidence of profitability;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

The source explicitly frames this as risk-managed β, not alpha.

## Related Wiki records

- `[[crypto-dynamic-time-series-momentum-volatility-impulse-2026-08-31]]` — Academic analysis of dynamic TSMOM in crypto (Borgards 2021); shares the TSMOM family but uses a different volatility-impulse mechanism rather than crash-state de-risking.
- `[[hyperliquid-vol-targeted-tsmom-drawdown-calibrated-ratchet-2026-09-12]]` — Vol-targeted TSMOM on Hyperliquid perps; shares the risk-management-over-TSMOM theme but uses ATR-based adaptive stops rather than a discrete crash-state threshold.

## Sources

1. Joseph Howden and Maksim Aleksandrovich Andreev. "Risk-Managed Time-Series Momentum in Crypto Majors: Crash-State De-Risking and Drawdown Control." SSRN working paper 7115459, posted July 30, 2026; written July 14, 2026. 6 pages. Abstract available at https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7115459.
2. Moskowitz, Tobias J., Yao Hua Ooi, and Lasse Heje Pedersen. "Time Series Momentum." *Journal of Financial Economics* 104, no. 2 (May 2012): 228–250. (The foundational TSMOM framework this paper adapts.)
