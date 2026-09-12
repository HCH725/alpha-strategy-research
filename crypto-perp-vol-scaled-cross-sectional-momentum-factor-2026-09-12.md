---
schema: strategy-research-record-v1
title: "Crypto Perpetual Vol-Scaled Cross-Sectional Momentum Factor"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual
  - momentum
  - cross-sectional
status: research-only
confidence: medium
source_as_of: 2026-09-12
sources:
  - "https://github.com/AbdullaE100/perp-quant-lab (commit 104dc669084b7f0d0a99748a0f4300950b49930d, 2026-07-07 to 2026-09-12)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Perpetual Vol-Scaled Cross-Sectional Momentum Factor

## Provenance

- **Primary Source:** AbdullaE100, *perp-quant-lab* GitHub repository. Quantitative research lab for perpetual futures with out-of-sample backtesting.
- **Repository URL:** https://github.com/AbdullaE100/perp-quant-lab
- **Full Commit SHA (latest):** `104dc669084b7f0d0a99748a0f4300950b49930d`
- **Key research files:**
  - `research/backtest.py` — initial cross-sectional factor sweep (raw momentum, reversal)
  - `research/backtest2.py` — vol-scaling, blends, cost sensitivity, sub-period robustness
  - `research/backtest3.py` — leg decomposition, market-neutrality, equity curve export
  - `research/README.md` — results summary and caveats
- **License:** MIT
- **Source data as-of:** 2026-09-12 (repository current as of latest commit)
- **Author:** AbdullaE100 (GitHub; no academic affiliation stated)

**Repository Deduplication Audit:** Full audit of all `.md` records in `alpha-strategy-research` confirmed zero existing records cite this repository, AbdullaE100, or this specific vol-scaled cross-sectional momentum construction. Related momentum records exist (e.g., `crypto-hyperliquid-momentum-funding-carry-combo-2026-09-12.md` for cross-sectional momentum+funding carry on Hyperliquid, `crypto-dynamic-time-series-momentum-volatility-impulse-2026-08-31.md` for time-series momentum with vol impulse) but none evaluate this specific 14-day vol-normalized cross-sectional rank signal across 40 liquid perps with the 70/30 IS/OOS split.

## Economic mechanism

### Source-reported

The author states that dividing cross-sectional momentum by trailing volatility (risk-adjusting the factor) materially lifts the out-of-sample Sharpe from 0.86 (raw momentum) to 1.62 (vol-scaled), while the long leg alone has a Sharpe of only 0.05 — the alpha lives entirely in the long-minus-short spread. The author notes that 30-day momentum overfits (best IS Sharpe, dead OOS) and that short-term reversal at daily frequency inverts (continues rather than reverts).

### Research interpretation

The hypothesized mechanism is **cross-sectional risk-adjusted momentum continuation** in crypto perpetual futures markets. Specifically:

1. **Cross-sectional momentum persistence:** Assets that outperform their peers over a trailing window tend to continue outperforming (and vice versa) at the daily frequency in crypto perps, contrary to short-term reversal patterns found in equities.
2. **Volatility normalization as signal quality filter:** Dividing momentum by realized volatility removes the confound that high-volatility assets naturally produce larger raw returns. The resulting signal isolates "momentum per unit of risk," which is more stable across regimes and reduces concentration in volatile, low-liquidity names.
3. **Market-neutrality through dollar-neutral construction:** The long-short, rank-weighted, dollar-neutral portfolio construction eliminates directional beta (verified: beta to BTC = −0.02), extracting pure cross-sectional spread.

The mechanism is consistent with behavioral inertia / underreaction in crypto markets (retail-dominated, slow information diffusion across fragmented venues) combined with the specific structure of perpetual futures (continuous funding creates carry costs that incentivize momentum continuation in the funded direction).

## Signal

### Formation timestamp
- Signal formed daily at daily bar close (timezone: UTC, inferred from Binance data).
- Weights aligned with next-day returns (position held from close_t to close_{t+1}).

### Lookback
- **Momentum window:** 14 calendar days (14 daily bars).
- **Volatility window:** 30-day rolling realized volatility (standard deviation of daily returns).
- **Signal construction** (verified from `backtest2.py` line `sig_xsmom_vs`):
  ```
  signal_{i,t} = (price_{i,t-1} / price_{i,t-15} - 1) / vol_{i,t-1}
  ```
  where `vol_{i,t} = std(daily_returns_{i, t-29:t})` (30-day rolling).
- **1-day skip:** signal uses prices lagged by 1 day (formation at close_t, tradable at close_{t+1}).

### Entry
- Cross-sectional rank of signal across all N assets each day.
- Demean ranks to achieve dollar-neutrality.
- Weights = demeaned_rank / sum(|demeaned_rank|) × 2.0, so sum|w| = 2.0 (gross exposure of 2).
- Long the top-ranked assets, short the bottom-ranked assets.

### Exit
- Daily rebalance: positions re-ranked and reweighted each trading day.
- No stop-loss, take-profit, or time-based exit rules (factor-level only).

### Holding period
- 1 day (daily rebalance).

### Parameters (research-proposed unless noted)
- Momentum lookback: 14 days (source-reported as the optimal lookback from sweep over 7/14/30/60/90/120 days).
- Volatility lookback: 30 days (source-reported, fixed in code).
- Skip: 1 day (source-reported, avoids same-day reversal).
- Weighting: rank-weighted, dollar-neutral, gross exposure 2 (source-reported).

### Position sizing
- Dollar-neutral long/short, rank-weighted. Sum of absolute weights = 2.0.
- No explicit position sizing beyond dollar-neutrality.

## Required data

- **Instrument:** ~40 liquid cryptocurrency perpetual futures (currently listed; specific list from `universe.json`).
- **Universe:** Survivorship-biased (currently-listed perps only). Author explicitly acknowledges this caveat.
- **Venue:** Binance Futures (USDT-M perpetuals).
- **Market type:** Perpetual futures.
- **Timeframe:** Daily bars.
- **Fields:** Close price (for momentum and volatility computation).
- **Missing data:** Author does not specify handling; standard dropna/fillna assumed from code inspection.
- **Funding/fee:** 5 bps per side taker cost modeled. Funding costs excluded (author caveat: "Costs exclude funding and alt slippage").

## Execution assumptions

- **Signal-to-order timing:** Next-day close execution (signal formed at close_t, position at close_{t+1}).
- **Order type:** Market order assumed (taker cost of 5 bps per side).
- **Fill model:** Assumed full fill at close price.
- **Fees:** 5 bps per side (Binance Futures taker fee, realistic for retail).
- **Slippage:** Not modeled beyond the 5 bps taker fee. Author caveat: "Costs exclude funding and alt slippage."
- **Funding:** Not modeled. Author explicitly lists this as a caveat.
- **Leverage:** Not specified for the factor strategy (dollar-neutral, 2x gross).
- **Capacity:** Not assessed. Universe of ~40 perps; author notes alpha is concentrated in the long-short spread, not individual legs.

## Evidence

### Source-reported

All figures below are from AbdullaE100 (perp-quant-lab, commit `104dc669`, research/README.md, backtest2.py, backtest3.py):

- **Vol-scaled XS momentum 14d (the winning factor):**
  - In-sample Sharpe: 1.21
  - Out-of-sample Sharpe: **1.62**
  - Full-sample Sharpe: 1.32, t-statistic: 2.68
  - Beta to BTC: −0.02 (genuinely market-neutral)
  - Long leg alone OOS Sharpe: 0.05 (alpha is in the spread, not individual legs)
  - Total return: ~5× vs BTC ~2× over 2022–2026

- **Comparison factors (OOS):**
  - Raw XS momentum 14d: OOS Sharpe 0.86
  - XS momentum 30d: OOS Sharpe 0.01 (overfit)
  - Short-term reversal 1d: OOS Sharpe −3.04 (inverted)

- **Cost sensitivity (from backtest2.py):**
  - Sharpe at 0 bps: reported but not individually stated in README (code available for reproduction).
  - Sharpe at 5 bps: 1.62 (primary result).
  - Sharpe at 10 bps: code available, not individually stated.

- **Single-coin sweep:** 936 configurations across 6 coins × 4 timeframes × 8 signal families. Zero configs paired Sharpe > 1 with drawdown shallower than −40%. Zero survived 10× leverage without liquidation.

- **LLM prediction experiment:** Anonymized snapshots: 48.4% hit-rate, Sharpe 0.88. Labeled snapshots: 53.9% hit-rate, Sharpe 1.84. Momentum baseline: Sharpe 1.41. Pre-cutoff recall: 56% hit-rate. Post-cutoff (genuinely unseen 2026 data): exactly 50% (coin-flip).

### Independently reproduced

Not independently reproduced. All results are source-reported from AbdullaE100.

### Negative evidence

- The winning factor was "in a drawdown at the end of the sample" (author caveat).
- Universe is survivorship-biased (currently-listed perps only; delisted/liquidated perps are excluded).
- Costs exclude funding and alt slippage — real-world perpetual holding incurs funding costs that could erode the edge, especially for positions held in the paying direction.
- 30-day momentum overfits in-sample and dies OOS, suggesting regime sensitivity to lookback choice.
- Short-term reversal inverts at daily frequency in crypto perps (continues rather than reverts), which is the opposite of equity microstructure findings.
- Single-coin directional strategies universally fail at realistic leverage, confirming the edge is purely cross-sectional.

None identified in the reviewed sources beyond the above; absence is not evidence of no additional negative result.

## Falsification plan

1. **Extended out-of-sample (research-proposed):** Reproduce on 2020–2026 data with the same 70/30 split, or use walk-forward expanding window. **Failure rule (research-defined):** If OOS Sharpe drops below 0.5, the edge is not temporally robust beyond the current sample.

2. **Funding cost sensitivity (research-proposed):** Add realistic funding costs (mean ± 1 std of historical funding rates for the universe) to the backtest. **Failure rule (research-defined):** If the OOS Sharpe drops below 1.0 after funding, the edge is not robust to the primary cost of holding perpetual positions.

3. **Universe expansion / survivorship correction (research-proposed):** Include historically delisted perps and re-run. **Failure rule (research-defined):** If survivorship bias accounts for > 30% of the OOS Sharpe, the factor is not robust to realistic universe construction.

4. **Lookback perturbation (research-proposed):** Test 10d, 12d, 16d, 18d momentum lookbacks and 20d, 40d volatility lookbacks. **Failure rule (research-defined):** If OOS Sharpe is unstable (>0.5 std across nearby parameter choices), the edge depends on precise parameter tuning.

5. **Sub-period regime breakdown (research-proposed):** Split OOS into yearly sub-periods. **Failure rule (research-defined):** If any single year contributes > 80% of the total OOS Sharpe, the edge is regime-concentrated.

## Crypto portability

**Direct.** The strategy is designed for and tested exclusively on cryptocurrency perpetual futures (Binance USDT-M perps). The underlying mechanism — cross-sectional momentum continuation in a retail-dominated, fragmented market — is well-documented in crypto.

Crypto-specific considerations:
- **Funding rate exposure:** Long positions in assets with positive funding receive payments; short positions pay. The dollar-neutral construction partially offsets this but does not eliminate it, as funding rates are asset-specific and time-varying. This is the primary portability risk.
- **24/7 session:** Daily bars at UTC close align with Binance's candle convention; no session-boundary issues.
- **Venue fragmentation:** Tested only on Binance; cross-venue liquidity and listing differences may affect the factor.
- **Liquidity:** ~40 liquid perps selected; less liquid perps may have wider spreads and higher slippage.
- **Leverage:** Factor strategy uses 2x gross leverage (dollar-neutral); no liquidation risk at this leverage.

## Limitations

- **Survivorship bias:** Universe includes only currently-listed perps. Delisted or liquidated contracts are excluded, which may inflate returns.
- **Funding cost omission:** The primary cost of holding perpetual positions (funding) is not modeled. Author explicitly acknowledges this.
- **Slippage omission:** Only 5 bps taker fee modeled; alt-coin slippage on less liquid perps may be materially higher.
- **Regime dependence:** The factor was in a drawdown at end of sample. 30-day lookback overfits, suggesting sensitivity to regime and parameter choice.
- **Single-venue:** Tested only on Binance Futures; cross-venue generalization unknown.
- **No capacity analysis:** Author does not assess how the factor performs at different capital scales.
- **Author credibility:** Single GitHub repository with 0 stars, 2 commits; no academic or institutional affiliation stated. Results are well-documented but not peer-reviewed.
- **Forward-looking bias in universe:** The 40-coin universe is defined at the current point in time; historically, the set of "liquid perps" has changed. This is a form of look-ahead bias in universe construction.

## Implementation status

Not implemented. No implementation in our research stack (PyBroker, Nautilus, or otherwise) has been completed.

## Adoption boundary

This record is research material only. Presence in this repository does not mean:
- Profitable
- Validated alpha
- Approved for implementation
- Approved for paper trading
- Approved for testnet
- Approved for live trading

## Related Wiki records

- `[[quant/crypto-hyperliquid-momentum-funding-carry-combo-2026-09-12]]` — Cross-sectional momentum combined with funding rate carry on Hyperliquid; different mechanism (funding carry component vs. pure vol-scaled momentum), different universe (30 assets on Hyperliquid vs. 40 on Binance).
- `[[quant/crypto-dynamic-time-series-momentum-volatility-impulse-2026-08-31]]` — Time-series momentum with volatility impulse filter; different mechanism (single-asset TSMOM vs. cross-sectional ranking).
- `[[quant/crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01]] — Pindza 2026 found microstructure signals do not survive at retail fee levels; this factor operates at daily frequency (not microstructure) and survives 5 bps taker costs.

## Sources

1. AbdullaE100, *perp-quant-lab*, GitHub repository. https://github.com/AbdullaE100/perp-quant-lab. Commit `104dc669084b7f0d0a99748a0f4300950b49930d` (latest as of 2026-09-12). Research files: `research/README.md`, `research/backtest.py`, `research/backtest2.py`, `research/backtest3.py`.
2. Signal construction verified from source code: `research/backtest2.py` (`sig_xsmom_vs` function), `research/backtest3.py` (leg decomposition, market-neutrality tests).
