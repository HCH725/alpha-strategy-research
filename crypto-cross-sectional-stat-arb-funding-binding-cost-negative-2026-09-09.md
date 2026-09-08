---
schema: strategy-research-record-v1
title: "Cross-Sectional Statistical Arbitrage on Crypto Perpetuals: 22 Pre-Registered Hypotheses, Funding as Binding Cost — Complete Negative Result"
created: 2026-09-09
updated: 2026-09-09
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - statistical-arbitrage
  - funding-rate
  - transaction-costs
  - negative-result
  - cross-sectional
  - market-microstructure
status: research-only
confidence: high
source_as_of: 2026-08-25
sources:
  - "https://github.com/ssanin82/dtc-stat-arb (commit 2f809280ba92b874d5cc71775c3bc687422dfa01, 2026-08-22)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Sectional Statistical Arbitrage on Crypto Perpetuals: Funding as Binding Cost

## Provenance

- **Repository**: https://github.com/ssanin82/dtc-stat-arb
- **Full commit SHA**: `2f809280ba92b874d5cc71775c3bc687422dfa01` (2026-08-22)
- **Key files**: `docs/cost-screen.md`, `docs/signal-test.md`, `docs/funding-book.md`, `docs/signal-test-PREREGISTRATION.md`
- **Author**: ssanin82 (Delta Tech Systems)
- **Date range**: 2026-08-20 to 2026-08-25 (repository creation to final commit)
- **Source type**: Open-source research repository with full methodology, pre-registration, and data pipeline
- **License**: Repository is public; individual files use standard open-source licenses
- **Note**: This is a rigorous negative-result study. The author registered 22 hypotheses in advance, tested all of them, and withdrew 17 claims along the way — every withdrawal logged rather than quietly corrected.

## Economic mechanism

### Source-reported

The study asks whether cross-sectional statistical arbitrage is viable on crypto perpetual futures after accounting for measured costs (fees, slippage, and funding). The founding hypothesis is that a dollar-neutral cross-sectional book can earn net positive returns after all costs. The study finds that **cost is viable at 1d/1w horizons but dead at 1h/4h**, and that **no signal clears the economic bar after measured costs**. The key finding is that **funding — not fees or slippage — is the binding cost term** that kills candidate strategies.

### Research interpretation

This is a **negative-result** study, not a positive alpha proposal. The economic mechanism identified is:

1. **Cross-sectional cost penalty**: A dollar-neutral book requires IC 1.6–6.2× larger than a cost-free book at daily/weekly horizons, and 16–100× at hourly/4h horizons.
2. **Funding as the binding drag**: For any signal that sorts by cross-sectional characteristics, the incidental funding loading (long the low-funding names, short the high-funding names) creates a funding cash flow that can exceed trading costs. This is signal-dependent — `carry_funding` earns +5.0–5.3 bp/day from funding; `lowvol` pays −3.24 bp/day.
3. **Gross predictability is plentiful; net tradability is scarce**: Signals like `rev_1d` have statistically significant IC (t = 2.1–2.8) but lose money after costs. Three signals are significant at |t| ≈ 5 and lose money.
4. **Published funding omission errors**: A referenced paper (Fayez Junior 2026, SSRN 6701738) ranks on funding but omits the funding term from its return equation, flipping the sign of net Sharpe from +0.74 to −0.49.

## Signal

### Source-reported (22 pre-registered hypotheses across 4 pre-registrations)

**Daily signals tested** (10 signals, Bybit/Binance/OKX):

| Signal | Description | Net Sharpe (Bybit) | Net Sharpe (Binance) | IC | t(IC) |
|---|---|---|---|---|---|
| `rev_1d` | 1-day reversal | −1.64 | −1.34 | 0.016–0.018 | 2.1–2.8 |
| `rev_5d` | 5-day reversal | −0.42 | −0.34 | 0.017–0.023 | 2.3–3.3 |
| `mom_20d` | 20-day momentum | −0.52 | −0.77 | −0.012–−0.016 | −1.7–−2.4 |
| `mom_60d` | 60-day momentum | −0.91 | −0.81 | −0.015–−0.019 | −2.5–−2.7 |
| `mom_20d_volscaled` | Vol-scaled 20d momentum | −0.29 | −0.51 | −0.006–−0.007 | −1.0–−1.3 |
| `carry_funding` | Funding carry (long low-funding) | 0.49 | 0.74 | −0.035–−0.036 | −5.3–−5.9 |
| `oi_chg_5d` | 5-day OI change | −1.47 | — | 0.011 | 1.9 |
| **`lowvol`** | **−σ_20 (long low-vol)** | **1.77** | **1.95** | **0.049–0.051** | **6.9–7.6** |
| `turnover_shock` | Turnover shock | −0.47 | −0.37 | 0.015–0.018 | 2.7–3.4 |
| `illiq` | Illiquidity | −0.21 | −0.02 | −0.016 | −5.0–−5.2 |

**`lowvol` hold-out result** (2022–2024 held out): Net Sharpe ~1.05 (Bybit), ~0.85 after removing market beta. First-half Sharpe 0.80–0.96, below the pre-registered ≥1.0 threshold in both halves → **a lead, not a finding**.

**Reversal signals** (separately pre-registered): IC 0.015–0.021 on three venues, but funding eats 46% of gross edge → also null.

**Cost penalty multiples** (required IC for net Sharpe 1.0):

| Horizon | OKX | Bybit |
|---|---|---|
| 1h | 63× | 100× |
| 4h | 16× | 25× |
| 1d | 5.1× | 6.2× |
| 1w | 1.6× | 1.8× |

### Research interpretation

The signal construction is well-specified and reproducible. The key operational insight is that **statistical significance is not the test** — `rev_1d` is significant at t = 2.8 and loses money. The economic bar (required IC) is far above the detection threshold. The `lowvol` signal survives initial tests but fails the pre-registered stability criterion (Sharpe ≥ 1.0 in both halves), and its outperformance in 2025–26 is approximately half market dispersion and half genuine IC rise.

## Required data

- **Universe**: Top 50 USDT perpetuals by 30-day quote turnover per venue (Bybit, OKX, Binance)
- **Exclusions**: Tokenised equities, commodities, RWA (classifier based on fee-group differences)
- **Market type**: USDT perpetual futures
- **Timeframe**: Daily (primary), with 1h/4h/1w cost screens
- **Fields**: OHLCV (daily close), funding rate history (88–91 days per venue), L2 book depth (1,132 sweeps × 150 symbols = 169,800 snapshots over 24h cycle), trade tape, fee tier per symbol
- **Timestamp**: UTC
- **Point-in-time**: Universe re-ranked on true 30d turnover from daily klines (not 24h alone)
- **Missing data**: OKX funding coverage only 9% (backfills ~95 days rather than to listing); delisted perpetuals retrievable from Binance archive

## Execution assumptions

- **Signal-to-order timing**: Daily rebalance
- **Execution**: Taker only (passive execution measured and found to be ~2× more expensive than crossing)
- **Fill model**: Cross at decision time; measured against mid at snapshot instant
- **Universe size**: $5,000 per name, 50 names, $250k target book
- **Slippage**: Measured from live L2 book walks — Bybit 6.07 bp one-way, OKX 4.62 bp, Binance 4.03 bp (at $5k/name)
- **Fees**: Bybit PRO-3 (2.82 bp taker), OKX VIP5 (2.50 bp taker), Binance VIP0 (5.00 bp taker, unverified)
- **Round-trip cost**: Bybit 17.8 bp, OKX 14.2 bp, Binance 18.1 bp (including slippage)
- **Funding**: Cross-sectional dispersion 22.7 bp/day (Bybit), 6.0 (OKX), 26.9 (Binance); market-wide level −3.82 bp/day (Bybit)
- **Capacity**: $250k target is ~15× inside the flow ceiling; capacity is not the constraint
- **Leverage/margin**: Not specified (dollar-neutral book)
- **Partial fills/failures**: 86% fill rate; 14% unfilled orders moved 111–118 bp on average

## Evidence

### Source-reported

- **22 pre-registered hypotheses**: All fail to clear the pre-committed economic bar after measured costs
- **17 claims withdrawn**: Every withdrawal logged in `docs/research-log.md`
- **`lowvol`**: Net Sharpe 1.77–1.97 (full sample) → 0.49–0.82 (size-neutral, beta-removed, 2025–26 held out), t = 0.90–1.20 — not statistically distinguishable from noise
- **`carry_funding`**: Net Sharpe +0.49–+0.74, but the entire P&L comes from funding cash flow (+5.0–5.3 bp/day), not price prediction (gross price return is negative −0.58–−1.04 bp/day)
- **Funding omission test**: Dropping funding from the return equation flips `carry_funding` net Sharpe from +0.74 to −0.49 (Binance) and +0.49 to −0.63 (Bybit)
- **`rev_1d`**: Statistically significant IC (t = 2.1–2.8) but earns 1.07 bp/day gross against 9.17 bp/day to trade it
- **Passive execution trap**: Naive passive arithmetic says negative cost (−1.51 bp); measured passive is 15.36 bp (Bybit), roughly 2× taker
- **Fee tier is second-order**: Repricing at retail schedules changes required IC by only 8–36% and does not flip a single verdict

### Independently reproduced

Not independently reproduced.

### Negative evidence

This entire repository IS negative evidence. Specific findings:

- All 10 daily signals fail after costs
- 1h and 4h horizons are dead on cost alone (16–100× penalty)
- `lowvol` fails the pre-registered stability test (Sharpe < 1.0 in first half)
- The Grinold-style IC→return mapping (`E[r] = E|z|·IC·σ`) misprices these books by ~2.1× due to kurtosis effects (verified algebra but the proposed correction failed on four counts)
- Three signals are statistically significant at |t| ≈ 5 and lose money
- Time-of-day variation in slippage is 1–7% (not the 100% feared)
- Regime variation in costs remains unmeasured (single calendar day)

## Falsification plan

The study itself is a falsification exercise with pre-registered kill criteria. What would change the answer (per the source):

1. A signal materially stronger than anything tested here, on data this study has not seen
2. NOT a better fee tier (worth 8–36% of the bar)
3. NOT passive execution (twice as expensive as crossing)
4. NOT more capacity (15× headroom)
5. NOT a different hour of the day (1–7% effect)

**Unresolved rather than settled**:
- **Regime**: Everything rests on one calendar day of book data and five years of a falling alt market
- **Funding-neutrality constraint**: Would be mandatory for a weekly book but untested

## Crypto portability

direct

This study is conducted entirely on crypto perpetual futures (USDT-denominated) across Bybit, OKX, and Binance. The findings are directly applicable to crypto perps.

**Crypto-specific considerations identified**:
- Funding rate is the binding cost, not fees — this is specific to perpetual futures (spot has no funding)
- Venue fragmentation matters: OKX costs 33% less than Bybit at daily horizon, driven by slippage not fees
- Cross-sectional funding dispersion is 6–27 bp/day across venues — large enough to dominate P&L
- 24/7 trading means cost measurement must cover full diurnal cycle (Asian-hours worry is falsified — 00:00–06:00 UTC runs similar to mean)
- Delisted perpetuals are retrievable from exchange archives (measured on Binance)

## Limitations

- **Single calendar day of cost measurement**: Regime variation in costs is unmeasured and is now the larger uncertainty
- **One account tier**: Bybit PRO-3 and OKX VIP5; retail tiers tested analytically and do not flip verdicts, but live measurement at retail is absent
- **OKX funding coverage only 9%**: OKX funding history backfills ~95 days rather than to listing; OKX net figures understate funding drag on most signals
- **Falling alt market bias**: Five years of a generally declining alt market; regime variation unknown
- **No delisting/settlement handling** beyond what venue price series encodes
- **Survivorship**: Measured at ±0.03 Sharpe on `lowvol` (small); not measured for momentum family
- **Cost is August 2026 cost**: Historical books were thinner; fast signals are if anything more dead than shown
- **One researcher, one account**: No independent replication

## Implementation status

not-implemented

No implementation in our research stack. This is a negative-result study — the finding is that the strategies tested do not work after costs. The cost measurement framework and funding analysis methodology could inform our own cost modeling.

## Adoption boundary

research-only

This record documents a **negative result** — a rigorous demonstration that cross-sectional stat arb on crypto perpetuals fails after measured costs. It is research material for understanding cost structures and funding dynamics, not a positive alpha proposal. The cost penalty multiples (1.6–100× depending on horizon) and the funding-as-binding-cost finding are the transferable insights.

## Related Wiki records

- [[quant/strategy-research-record-spec-v1]] (schema specification)
- No directly related strategy research records share the same source identity. The study does reference SSRN 6701738 (Fayez Junior 2026) on funding-based cross-sectional screening, which is a distinct source with a different methodology and a funding omission error.

## Sources

1. ssanin82, "dtc-stat-arb: Cross-sectional statistical arbitrage on crypto perpetuals," GitHub repository, commit `2f809280ba92b874d5cc71775c3bc687422dfa01` (2026-08-22). https://github.com/ssanin82/dtc-stat-arb
2. Fayez Junior (2026), "Cross-Sectional Funding-Rate Carry in Crypto Perpetual Futures," SSRN working paper, SSRN 6701738. Referenced in `docs/funding-book.md` as the motivating paper for the funding omission analysis. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6701738
