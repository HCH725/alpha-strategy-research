---
schema: strategy-research-record-v1
title: Crypto Medium-Term Cross-Sectional Reversal (8–10 Week LMW)
created: 2026-09-11
updated: 2026-09-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - reversal
  - contrarian
  - liquidity-provision
status: research-only
confidence: medium
source_as_of: 2026-06-01
sources:
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6703978"
  - "https://patrickkiefer.substack.com/p/the-cryptocurrency-reversal-cycle"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Medium-Term Cross-Sectional Reversal (8–10 Week LMW)

## Provenance

Primary source: Patrick Kiefer (Protean Technologies) and Michael Nowotny, **"Reversal in Cryptocurrency Returns,"** SSRN working paper 6703978, posted May 3, 2026, last revised June 1, 2026. 30 pages.

- **SSRN abstract URL:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6703978
- **Supplementary source (first-author Substack):** https://patrickkiefer.substack.com/p/the-cryptocurrency-reversal-cycle
- **Authors:** Patrick Kiefer (Protean Technologies), Michael Nowotny (affiliation not provided)
- **Date written:** May 3, 2026
- **Last revised:** June 1, 2026
- **Publication status:** SSRN working paper; not peer-reviewed at time of recording
- **Source-identity deduplication:** Searched entire repository for SSRN 6703978, author names "Kiefer" and "Nowotny," exact title, and mechanism "8-week" / "10-week" cross-sectional reversal in crypto. Zero prior records matched. The existing `crypto-low-price-anchor-cross-sectional-reversal-2026-09-01.md` (Nakagawa & Sakemoto, 2025, DOI 10.1016/j.frl.2025.107800) uses a materially distinct mechanism (lowest-price anchoring decomposition) and a different sample. This record is independent.

**Primary-source checksum (verified from SSRN abstract page + first-author Substack):**
- (a) Complete author list: Patrick Kiefer, Michael Nowotny — confirmed from SSRN page.
- (b) Version/date: Posted 2026-05-03, revised 2026-06-01 — confirmed from SSRN page.
- (c) Sample period: 2021 through early 2026 — confirmed from Substack post; abstract says "2021–2026."
- (d) Universe: ~70 Binance USDT spot pairs — confirmed from Substack post; abstract says "Binance USDT spot pairs (2021–2026)" across seven universes.
- (e) Transaction cost/slippage: Robust to 50 bps round-trip — confirmed from Substack post by first author; abstract does not specify cost assumption.
- (f) Core performance numbers: Full universe Sharpe ~0.96 (Substack); high-volatility conditioning Sharpe 1.19–1.35, Newey-West t up to 3.31 (abstract); excluding mega-caps Sharpe 1.38, t = 3.44 (abstract); bootstrap mean Sharpe 1.38, 95th percentile > 0.67 (abstract); annualized return 39.6% full universe (Substack). All numbers traced to their respective source (abstract vs. Substack).
- (g) Publication status: SSRN working paper — confirmed from SSRN page.

## Economic mechanism

### Source-reported

The source documents cross-sectional reversal in cryptocurrency returns at 8- to 10-week formation horizons. A contrarian strategy buys recent losers and sells recent winners (the standard Jegadeesh-Titman 1993 LMW portfolio construction), earning high mean returns and high Sharpe ratios that are nearly orthogonal to the market. The effect is concentrated in volatile mid-cap tokens and is robust to mark-to-next delisting accounting.

The source discusses several economic mechanisms:
1. **Discretionary treasury selling:** Past winners sell off on average after rallies, driven by treasury managers who liquidate positions into strength.
2. **Liquidity provision compensation:** Reversal compensates liquidity providers who absorb order-flow imbalances, consistent with Nagel (2012).
3. **Supply-side explanation:** The pattern favors a supply-side explanation over purely behavioral channels. The authors note that past losers rebound episodically on macro news while past winners sell off systematically, which is more consistent with supply-side dynamics.

### Research interpretation

The hypothesis is a **cross-sectional mean-reversion (contrarian) effect in crypto spot returns at the 8–10 week horizon**. The economic claim is that over 8–10 week horizons, past winners exhibit systematically lower future returns than past losers, and this differential is large enough to generate meaningful risk-adjusted alpha after costs.

Falsifiable sub-mechanisms:
- **Momentum decay:** Crypto momentum at 1–4 week horizons (Liu et al., 2022) decays and reverses at 8–10 weeks, suggesting that the initial momentum is driven by temporary price pressure rather than information diffusion.
- **Liquidity provision premium:** The reversal concentrates in volatile mid-caps where liquidity provision is most needed and most compensated, consistent with limits-to-arbitrage theory.
- **Orthogonality to market:** The strategy is nearly uncorrelated with the broad crypto market return, suggesting the effect is driven by cross-sectional relative performance rather than time-series market exposure.

## Signal

**Formation period:** 8–10 weeks (the source tests both and finds the effect robust across this range).

**Signal formation:**
1. Compute cumulative return for each token over the trailing 8–10 week formation window.
2. Rank tokens by cumulative return within the universe.
3. Long the bottom quintile / tercile (past losers).
4. Short the top quintile / tercile (past winners).
5. Dollar-neutral (or equal-weight long-short).

**Portfolio construction:**
- Jegadeesh-Titman (1993) overlapping portfolios.
- Seven universe definitions tested (details of each not fully available from abstract/Substack alone).

**Rebalancing frequency:** Weekly or monthly overlapping rebalancing (consistent with Jegadeesh-Titman overlapping construction; exact cadence not fully specified in abstract alone).

**Holding period:** Not fully specified in abstract; consistent with monthly or multi-week rebalancing.

**Parameters:**
- Formation window: 8–10 weeks (source-reported range; exact optimal window not specified as a single fixed value).
- Volatility conditioning: Filter to high-volatility tokens for enhanced Sharpe (details of volatility filter threshold: not fully specified from abstract/Substack; treat as research-proposed if operationalized by Scout).

**Data gap:** The exact universe inclusion/exclusion rules, the precise formation and holding period combinations tested, and the detailed portfolio-weighting scheme (equal-weight vs. other) are not fully available from the abstract and Substack alone. These are labeled `underspecified`.

## Required data

- **Instrument:** ~70 liquid Binance USDT-margined spot cryptocurrency pairs.
- **Venue:** Binance (spot market, USDT-denominated).
- **Market type:** Spot.
- **Timeframe:** Daily close-to-close returns, aggregated over 8–10 week windows.
- **Fields:** Daily close prices, volume (for universe filtering and liquidity).
- **Universe:** ~70 tokens with mark-to-next delisting accounting; seven universe definitions tested (exact membership not fully specified from abstract/Substack).
- **Point-in-time:** Standard daily close availability; no point-in-time concerns for prices.
- **Missing-data:** Mark-to-next delisting accounting implies delisted tokens remain in the universe at their last observed price until the next delisting is observed (no survivorship bias).

## Execution assumptions

- **Signal-to-order timing:** Weekly or monthly rebalancing (overlapping portfolios). Exact timing not specified in abstract alone.
- **Order type:** Market order (spot).
- **Fill model:** Assumed immediate at close; no explicit fill model specified.
- **Transaction costs:** Robust to 50 bps round-trip (confirmed from first-author Substack post). This is generous relative to Binance spot taker fees (~10–15 bps round-trip at standard tier) but accounts for slippage.
- **Slippage:** Not explicitly modeled beyond the 50 bps robustness check.
- **Funding:** Spot strategy; no funding or borrowing costs.
- **Leverage:** Not specified; assumed unlevered.
- **Shorting:** For short leg, requires spot borrowing or perpetual futures overlay. Spot borrowing availability for altcoins on Binance is limited; a perpetual futures overlay is the practical implementation (adds funding cost risk).
- **Capacity:** ~70 tokens suggests limited capacity; market-impact costs for large positions are not addressed.

## Evidence

### Source-reported

- Full universe LMW Sharpe: ~0.96 (from first-author Substack, annualized return ~39.6%).
- High-volatility-conditioned Sharpe: 1.19–1.35, Newey-West t-stat up to 3.31 (from abstract).
- Excluding largest mega-caps: Sharpe 1.38, t = 3.44 (from abstract).
- Circular block bootstrap (nonparametric): mean Sharpe 1.38, 95% of bootstrap Sharpe ratios above 0.67 (from abstract).
- Strategy is described as "nearly orthogonal to the market" (from abstract).
- Robust to mark-to-next delisting accounting (from abstract).
- Robust to 50 bps round-trip costs (from first-author Substack).

All source-reported. None independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed sources; absence is not evidence of no negative result. Note that the paper is an SSRN working paper that has not been peer-reviewed at time of recording. Several independent backtests of crypto cross-sectional momentum (which operates at shorter horizons) have shown decay or failure out of sample (e.g., Stratproof.com replication finding Sharpe 0.37 vs. literature-reported 1.1–1.5; prams2104 GitHub replication showing out-of-sample failure). Whether this specific 8–10 week reversal signal exhibits similar decay is unknown.

## Falsification plan

1. **Out-of-sample test:** Replicate the 8–10 week LMW strategy on Binance USDT spot pairs from 2024 onward using the same universe and delisting accounting, with 50 bps round-trip costs. Failure metric: net Sharpe below 0.5 (research-defined falsification threshold).
2. **Horizon sensitivity:** Test formation windows of 4, 6, 8, 10, 12, and 16 weeks to confirm the effect peaks in the 8–10 week range. Failure metric: Sharpe degrades monotonically outside the claimed range without a structural explanation.
3. **Size/liquidity decomposition:** Separate the effect by market-cap quintile to verify the concentration in mid-caps. Failure metric: effect is evenly distributed across size quintiles (contradicting the mid-cap concentration claim).
4. **Momentum-reversal orthogonality:** Test whether the 1–4 week momentum signal and the 8–10 week reversal signal are truly orthogonal. Failure metric: correlation above |0.3| between the two signals.
5. **Cost sensitivity:** Sweep round-trip costs from 10 bps to 100 bps. Failure metric: strategy becomes unprofitable below 30 bps (suggesting the edge is too thin to survive realistic costs for sub-50-bp-capable participants).
6. **Regime dependence:** Test the strategy separately in bull (2021, 2024) and bear (2022) markets. Failure metric: Sharpe is significantly negative in bear markets (suggesting the effect is not regime-robust).

## Crypto portability

**Direct** — the strategy is native to crypto spot markets on Binance.

Crypto-specific considerations:
- **Shorting mechanism:** The short leg requires either spot borrowing (limited on Binance for most altcoins) or a perpetual futures overlay. A perp overlay introduces funding cost risk, especially during positive-funding environments where shorts pay longs. This could erode the reversal premium if funding is elevated during the formation period.
- **Spot vs. perpetual basis:** The strategy is tested on spot returns. If implemented via perpetuals, basis dynamics could distort the signal.
- **24/7 session:** No impact; the strategy operates at weekly/monthly horizons.
- **Venue fragmentation:** Tested only on Binance; portability to other venues (Bybit, OKX) is untested.
- **Delisting risk:** The mark-to-next delisting accounting is a strength but implies the strategy may hold delisted tokens briefly, creating realized losses.

## Limitations

- **Working paper status:** Not peer-reviewed at time of recording. Results should be treated with caution.
- **Publication bias:** SSRN working papers may report favorable results; independent replication is essential.
- **Universe detail gaps:** The seven universe definitions are not fully specified from the abstract/Substack alone. The exact token inclusion criteria and universe composition are `underspecified`.
- **Cost model simplicity:** The 50 bps round-trip robustness check is generous relative to Binance spot taker fees but does not account for partial fills, slippage in thin mid-cap books, or market impact for larger positions. The actual cost for the volatile mid-cap universe may be higher than 50 bps.
- **Shorting feasibility:** Spot shorting availability for mid-cap altcoins is limited; a perpetual futures overlay changes the economics.
- **Mega-cap exclusion:** The highest Sharpe (1.38) is achieved by excluding mega-caps, which is also the least liquid part of the universe, creating a capacity/liquidity tension.
- **Temporal stability:** The strategy is tested on 2021–2026 data, which includes both a full bull-bear cycle and a structural change in market microstructure (increased institutional participation, ETF-driven flows). Whether the effect persists in future regime changes is unknown.
- **Independent replication absent:** No third-party replication of this specific 8–10 week reversal signal has been found.

## Implementation status

`not-implemented`. No implementation in the NautilusTrader research stack or PyBroker. This record is research material only.

## Adoption boundary

This record represents normalized external research material only. It does not constitute:
- Validation of profitability
- Approval for implementation
- Approval for paper trading, testnet, or live trading
- A confirmed alpha signal

Any future implementation must proceed through the standard validation pipeline (PyBroker experiment → NautilusTrader historical verdict → Paper → Testnet → Live).

## Related Wiki records

- `[[crypto-low-price-anchor-cross-sectional-reversal-2026-09-01]]` — Different mechanism (lowest-price anchoring decomposition by Nakagawa & Sakemoto 2025) operating at a different horizon and using different behavioral hypotheses. Independent record.
- `[[crypto-short-horizon-15min-mean-reversion-taker-flow-2026-09-01]]` — Short-horizon (15-minute) mean reversion from taker flow. Different horizon (15 min vs. 8–10 weeks), different mechanism (microstructure liquidity provision vs. cross-sectional contrarian), different data (intraday tick vs. daily close). Independent record.
- `[[crypto-liquidity-provision-reversal-premium-cross-market-2026-09-01]]` — Cross-market liquidity provision reversal premium. Related in theme (reversal = liquidity provision compensation) but different methodology and horizon.

## Sources

1. Patrick Kiefer and Michael Nowotny, "Reversal in Cryptocurrency Returns," SSRN working paper 6703978, posted May 3, 2026, last revised June 1, 2026. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6703978
2. Patrick Kiefer, "The Cryptocurrency Reversal Cycle," first-author Substack post, 2026. https://patrickkiefer.substack.com/p/the-cryptocurrency-reversal-cycle (provides additional universe detail, cost robustness, and performance numbers not in the abstract.)
