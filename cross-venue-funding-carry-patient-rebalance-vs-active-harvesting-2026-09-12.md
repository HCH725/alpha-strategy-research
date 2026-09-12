---
schema: strategy-research-record-v1
title: "Cross-Venue Funding Rate Carry: Patient Rebalancing vs Active Harvesting Under Execution Costs"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - funding-rate
  - carry-trade
  - execution-costs
  - mean-reversion
status: research-only
confidence: medium
source_as_of: 2026-09-12
sources:
  - "https://github.com/DavidAyusoPita/funding-carry-analysis (commit e990265ee3e193afcb2c7aff3c07a615cce5e22d, 2026-09-12)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Venue Funding Rate Carry: Patient Rebalancing vs Active Harvesting Under Execution Costs

## Provenance

- **Repository:** DavidAyusoPita/funding-carry-analysis
- **Repository URL:** https://github.com/DavidAyusoPita/funding-carry-analysis
- **Full commit SHA:** `e990265ee3e193afcb2c7aff3c07a615cce5e22d`
- **Key files:** `src/analysis.py`, `src/fetch.py`, `notebooks/01_funding_carry_analysis.ipynb`
- **Author:** David Ayuso Pita
- **Data source as-of:** July 2024 – July 2026 (two years, 18,208 hourly observations per asset-venue pair)
- **Universe:** BTC, ETH, SOL across four venues: Binance, Bybit, OKX (CEX), and Hyperliquid (on-chain DEX)
- **Data:** Public REST endpoints only; no API keys or authenticated access required

## Economic mechanism

### Source-reported

The author investigates whether the structural funding-rate spread between centralized exchanges (CEX) and decentralized perpetual DEXs (specifically Hyperliquid) represents a tradable carry opportunity. The core question: a delta-neutral position (long perpetual on the venue paying lower funding, short on the venue paying higher funding) earns the spread, but how much survives execution costs?

Key findings from the author:
1. **The spread is a genuine structural bias, not noise.** Hyperliquid pays more than CEX venues in 65–72% of hours, worth 8.5–11.4% annualized in absolute terms. A CEX-vs-CEX control shows no persistent bias (41–47% sign stability, centered on zero).
2. **The level mean-reverts within hours.** AR(1) half-life of the exchange-versus-DEX spread is 1.5–3.5 hours, while one round trip costs ~13 bps and needs 100–135 hours of holding to break even.
3. **Active trading destroys value.** A threshold rule entering when trailing spread > 10% annualized earns the most gross income but finishes at −9% to −15% annualized after costs.
4. **The patient rule works.** Holding continuously and revisiting only which venue to short on a 30-day clock returned +2.7% to +5.4% annualized net on notional with 1–5 round trips over two years, max drawdown under 2%.
5. **The margin is shrinking.** Spread averaged 20–35% less in the second year vs. the first, and sits 45–60% below late-2024 peak.

### Research interpretation

The hypothesized mechanism is **structural CEX-DEX funding-rate dislocation driven by incomplete cross-venue integration and differing demand/supply dynamics for perpetual leverage**. On-chain perpetual venues (Hyperliquid) may command higher funding rates due to (a) higher retail leverage demand, (b) lower institutional arbitrage capital, and (c) protocol-specific funding mechanisms. The directional bias persists for months (regime-level), but the level mean-reverts within hours (noise-level). This separation of regime persistence from level noise explains why active harvesting destroys value while patient holding captures the structural bias.

The result is a cautionary carry-trade finding: the spread exists, is structurally real, but the cost of harvesting it exceeds the edge for any active frequency. Only ultra-low-frequency rebalancing (monthly) captures net value, and even that is thin and decaying.

## Signal

### Cross-venue funding spread (directional regime)

- **Formation timestamp:** Hourly; funding rate observed at each venue's settlement timestamp.
- **Lookback:** 720 hours (30 days) trailing mean for the patient rule; 8 hours for the active rule.
- **Long entry:** Hold perpetual on the venue paying lower funding (i.e., short the venue paying higher funding).
- **Short entry:** Inferred from the sign of the trailing mean spread. Side chosen at entry is held for the life of the position.
- **Exit:** Patient rule: never exits (permanent hold); only revisits which venue to short on a 30-day rebalance clock. Active rule: exits when trailing spread decays below 3% annualized.
- **Holding period:** Patient rule: effectively permanent (1–5 round trips over 2 years). Active rule: varies with spread dynamics.
- **Parameters:** 30-day lookback and rebalance for patient rule; 8-hour lookback, 10% annualized entry threshold, 3% annualized exit threshold, 0.7 minimum consistency for active rule. All parameters `research-proposed` (author's chosen values, not source-derived from a theoretical model).
- **Position sizing:** Equal notional on both legs (delta-neutral). Returns reported on notional, not on margin/deployed capital.

## Required data

- **Instruments:** BTC, ETH, SOL perpetual futures
- **Venues:** Binance Futures, Bybit, OKX, Hyperliquid
- **Market type:** Perpetual futures (both CEX and on-chain DEX)
- **Timeframe:** Hourly funding rate observations; 8-hour and 1-hour settlement intervals depending on venue
- **Fields:** Funding rate (per-hour normalized), OHLCV prices (for cross-venue price basis measurement)
- **Point-in-time:** Funding rates are settlement-time stamped; backward-aligned (rate at 08:00 covers window 00:00–07:00)
- **Timestamp:** UTC throughout
- **Missing data:** OKX publishes only 3 months of history; excluded from two-year comparisons. Binance moves volatile symbols to 4-hour funding schedule; interval inferred from timestamps rather than assumed.
- **Funding/fee/spread:** Round-trip cost modeled as 4 market crosses (2 legs × open/close). Four cost profiles tested: retail taker/taker (~22 bps), maker/taker mixed (~14 bps), maker/maker passive (~7 bps), on-chain DEX rebate tier (~4 bps). Cross-venue price basis measured from data (median 1.0–1.5 bps, 99th percentile ~10 bps).

## Execution assumptions

- **Signal-to-order timing:** Funding rates observed at settlement; position held continuously.
- **Fill model:** Not simulated; returns computed from observed funding rates minus modeled costs.
- **Fees:** Four cost profiles ranging from retail taker (4.5 bps per leg per side) to on-chain maker (0.5 bps per leg per side).
- **Slippage:** Separated from fees; assumed at 0.5–1.0 bps per leg per side depending on profile. Cross-venue price basis measured from data (median 1.0–1.5 bps).
- **Funding:** This IS the funding strategy; funding earned is the signed spread between venues.
- **Liquidation:** NOT modeled. Both legs post margin independently; margin is not fungible across venues. A sharp move can liquidate the losing leg while the winning one is still open — the dominant tail risk, explicitly excluded from these numbers.
- **Capacity:** Not assessed. Returns are on notional, not on deployed capital.
- **Partial fills / failures:** Not modeled.

## Evidence

### Source-reported

All figures from DavidAyusoPita/funding-carry-analysis (commit `e990265`, analysis.py, notebook):

- **Cross-venue spread bias:** Hyperliquid pays more than CEX in 65–72% of hours. Annualized absolute spread: 8.5–11.4%. CEX-vs-CEX control: centered on zero, 41–47% sign stability.
- **Half-life:** AR(1) half-life of exchange-versus-DEX spread: 1.5–3.5 hours.
- **Break-even holding:** ~100–135 hours for a 13 bps round trip at average spread.
- **Active rule (threshold > 10% annualized):** Finishes at −9% to −15% annualized after costs. Execution consumed ~3× gross income.
- **Patient rule (30-day rebalance):** +2.7% to +5.4% annualized net on notional, 1–5 round trips over 2 years, max drawdown < 2%.
- **Decay:** Spread averaged 20–35% less in year 2 vs. year 1; 45–60% below late-2024 peak.
- **Cost sensitivity:** Patient rule tolerates round-trip cost up to ~250 bps before breaking even. Active rule dies above ~8 bps.
- **Price basis:** Median cross-venue price gap: 1.0–1.5 bps; 99th percentile: ~10 bps.

The author notes: "The cost assumptions and the decision-rule structure come from operating a live implementation of this strategy; that system is private and none of it is in this repository."

### Independently reproduced

Not independently reproduced. All empirical findings are from the single repository analysis.

### Negative evidence

- Active harvesting strategies (threshold-based entry) consistently lose money after costs across all four fee profiles.
- The spread is mean-reverting at the level (half-life 1.5–3.5 hours) while only the directional regime persists for months — confusing the two is the core trap identified by the author.
- The spread is decaying over time (20–35% year-over-year decline), suggesting competitive pressure is eroding the opportunity.
- No liquidation modeling means tail risk is entirely unmeasured; cross-venue margin non-fungibility creates directional exposure during sharp moves.

## Falsification plan

1. **Out-of-sample extension:** Extend the sample beyond July 2026. If the spread continues to compress at 20–35% per year, the patient rule's edge approaches zero within 2–3 years (`research-defined falsification threshold`: if annualized spread mean drops below 3%, the carry thesis is falsified).
2. **Liquidation stress test:** Model cross-venue liquidation risk explicitly. If the tail loss from uncorrelated liquidation events exceeds the patient rule's annual carry, the strategy is not viable on capital basis (`research-defined falsification threshold`: if simulated 99th-percentile liquidation loss > 2× annual carry, reject).
3. **Capital-basis restatement:** Restate returns on deployed capital (margin required for both legs) rather than notional. If return on capital drops below risk-free rate, the carry is not compensating for venue/protocol/liquidation risk.
4. **Venue expansion:** Test on less liquid assets where spread is wider but book is thinner. If execution costs on thinner books exceed the wider spread, the opportunity does not scale.
5. **Decay continuation:** If the quarterly decay trend continues, re-evaluate whether the structural bias is being competed away permanently.

## Crypto portability

**Direct.** The strategy is designed for and tested on crypto perpetual futures across both CEX and on-chain DEX venues. The mechanism (structural funding-rate dislocation between venue types) is specific to crypto perpetual markets.

Crypto-specific risks:
- Cross-venue margin non-fungibility (dominant tail risk, unmodeled)
- Exchange failure / smart contract risk (correlated with conditions that widen the spread)
- Funding rate caps on venues (truncating extreme observations)
- Survivorship bias (only listed, liquid instruments tested)
- 24/7 trading with continuous funding accrual

## Limitations

- **No liquidation modeling.** The dominant tail risk — cross-venue margin non-fungibility causing directional exposure during sharp moves — is entirely unmeasured. This is the most significant limitation.
- **Returns on notional, not capital.** Both legs must be collateralized; return on deployed capital depends on margin regime and leverage, which amplifies liquidation risk.
- **No counterparty or protocol risk.** Exchange failure and smart contract failure are real, undiversifiable, and correlated with exactly the conditions that make the spread widest.
- **Single historical path.** Two years, three assets, one regime. Nothing establishes out-of-sample persistence.
- **Decaying opportunity.** Spread averaged 20–35% less in year 2 vs. year 1, suggesting competitive erosion.
- **Slippage assumed, not observed.** Real fills depend on book depth at execution; the measured price basis is a proxy.
- **Funding caps ignored.** Venues bound their rates, truncating extremes the strategy would most like to capture.
- **Survivorship and selection.** Only the three most liquid assets tested; smaller assets show wider spreads but thinner books.
- **One regime.** Sample spans mid-2024 to mid-2026, which may not represent all market conditions.
- **Author operated a live implementation** (private) that informed the cost assumptions and decision rules; the public analysis may benefit from hindsight in parameter selection (`data gap`).

## Implementation status

Not implemented in our research stack. The repository provides a complete, reproducible analysis pipeline (fetch, analysis, plotting, notebook) but no live trading infrastructure.

## Adoption boundary

This record captures research material only. Its presence does not constitute evidence of profitability, validated alpha, or authorization for deployment in paper trading, testnet, or live trading systems. The author explicitly notes that the analysis is built around checks "that a return figure on its own would hide" — the findings are cautionary, not promotional.

## Related Wiki records

- `[[crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11]]` — Cross-sectional funding rate carry factor across Binance perps; different mechanism (cross-sectional sorting vs. cross-venue bilateral carry).
- `[[crypto-hyperliquid-momentum-funding-carry-combo-2026-09-12]]` — Momentum + funding carry hybrid on Hyperliquid; different mechanism (cross-sectional momentum ranking vs. bilateral venue-spread carry).
- `[[funding-aware-market-making-perpetual-dex-2026-08-31]]` — Funding-aware market making HJB on Hyperliquid; different mechanism (liquidity provision vs. carry harvesting).
- `[[crypto-two-tiered-cex-dominant-funding-discovery-2026-09-12]]` — Two-tiered funding rate market structure (Zhivkov 2026); complementary finding on CEX-DEX information flow asymmetry.
- `[[retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11]]` — Falsification of retail CVD and funding rate signals; adjacent negative-evidence context.

## Sources

1. David Ayuso Pita, *funding-carry-analysis*, GitHub repository. https://github.com/DavidAyusoPita/funding-carry-analysis. Commit `e990265ee3e193afcb2c7aff3c07a615cce5e22d` (latest as of 2026-09-12). Key files: `src/analysis.py`, `src/fetch.py`, `notebooks/01_funding_carry_analysis.ipynb`, `README.md`.
2. All quantitative figures trace directly to the repository analysis pipeline (analysis.py functions: `venue_spread`, `spread_halflife`, `backtest_spread`, `backtest_slow_side`, `breakeven_table`, `quarterly_profile`, `backtest_summary`, `sweep_costs`). No secondary summaries or search snippets were used.
