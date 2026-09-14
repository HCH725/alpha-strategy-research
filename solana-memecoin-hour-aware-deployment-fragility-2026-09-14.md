---
schema: strategy-research-record-v1
title: "Solana Memecoin Hour-Aware Deployment Fragility: Rejection-Tracker Drawdowns and Top-Trade Concentration"
created: 2026-09-14
updated: 2026-09-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - solana
  - memecoin
  - dex
  - falsification
  - negative-evidence
  - deployment-audit
  - microstructure
status: research-only
confidence: medium
source_as_of: 2026-08-03
sources:
  - "Arati Uday Kamat, 'Hour-Aware Adaptive Risk Management for Autonomous Memecoin Trading on Solana DEXs: Evidence, Theory, and Design Lessons from a 15-Day Deployment', arXiv:2606.08232v3 [q-fin.TR, q-fin.CP, q-fin.RM, q-fin.ST], June 6, 2026 (v3 August 3, 2026). https://arxiv.org/abs/2606.08232"
  - "Companion dataset (Zenodo concept DOI): https://doi.org/10.5281/zenodo.20043301"
  - "SSRN 6564803 (as stated by source)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Solana Memecoin Hour-Aware Deployment Fragility: Rejection-Tracker Drawdowns and Top-Trade Concentration

## Provenance

- **Source**: arXiv:2606.08232v3 [q-fin.TR, q-fin.CP, q-fin.RM, q-fin.ST]
- **Author**: Arati Uday Kamat
- **Versions**: v1 submitted June 6, 2026; v3 last revised August 3, 2026 (Ledger #632 revision)
- **DOI**: https://doi.org/10.48550/arXiv.2606.08232
- **URL**: https://arxiv.org/abs/2606.08232
- **Deployment window**: March 29 to April 12, 2026 (15 days), paper-traded
- **Sample**: 190 trades on Solana decentralized exchanges (AMM memecoin venue)
- **Counterfactual rejection tracker**: 4,874 forward-sample observations across 184 rejection events
- **Data / audit**: Companion Zenodo concept DOI 10.5281/zenodo.20043301; assertion-based reproduction script (MIT) deposited by the author; trade log and rejection-sample corpus CC-BY-4.0
- **SSRN**: 6564803 (as stated by source)

### Repository Deduplication Audit

Repository-wide search on 2026-09-14 found zero prior records citing `arXiv:2606.08232`, Kamat's 15-day Solana memecoin hour-aware deployment, or the paired rejection-tracker corpus for this venue. Adjacent records:

- `crypto-binance-smallcap-pump-reversal-regime-gated-falsification-2026-09-13.md` — Binance small-cap pump-reversal falsification (different venue, different construction)
- `solana-bonding-curve-sniper-cohort-contamination-adjusted-flow-2026-09-02.md` — Solana bonding-curve sniper cohort (related venue family, different mechanism: contamination-adjusted buyer-flow lift)
- `telegram-coordinated-pump-dump-detection-contrarian-fade-2026-09-13.md` — Telegram P&D detection (social coordination, not DEX hour-aware deployment)
- `crypto-binance-smallcap-pump-reversal...` and other falsification records do not include this 190-trade paper-deployment log with hour-of-day Mann–Whitney and rejection-event drawdown tracking

## Economic mechanism

### Source-reported

The paper frames a 15-day autonomous memecoin paper-trading deployment on Solana DEXs as a **controlled measurement** of three microstructure questions:

1. Time-of-day return patterns on a 24/7 permissionless venue
2. Whether decision-time filter stacks are net-positive against counterfactual returns of **rejected** tokens
3. Whether small-sample cumulative-return statistics on a heavy-tailed venue are structurally robust or fragile

Headline deployment stats: 40.5% win rate; mean per-trade return +0.62%; cumulative +117.7%; skewness −1.21; excess kurtosis 6.61.

Hour-of-day: three exploratorily identified worst entry hours (n=17, mean −11.60%) vs all others (n=173, mean +1.82%); Mann–Whitney U **p = 0.5634** — directional only, **non-confirmatory**.

Rejection tracker: of 48 rejection events observed ≥6 hours, **27 (56.25%)** reached a 50% drawdown from reference; full-cohort 17.9% is a censored lower bound.

Fragility: **removing the top three trades (1.6% of sample) flips cumulative return unprofitable**.

### Research interpretation

This is primarily a **negative / design-lesson** capture: on a heavy-tailed memecoin DEX, (a) hour-of-day filters are not statistically established at this sample size, (b) most sufficiently observed rejections still collapse, and (c) headline cumulative return is dominated by a few trades (deflated-Sharpe / Bailey–López de Prado fragility). The paper's own principal contribution is measurement infrastructure and design lessons, not a promoted profitable strategy.

## Signal

### Formation timestamp

Paper-traded autonomous decisions on Solana DEX memecoin listings during March 29–April 12, 2026 (`source-reported` deployment window). Exact decision-time filter stack internals are described in the paper body; this record does not restate undocumented proprietary thresholds beyond what the source reports.

### Lookback

Hour-of-day analysis uses entry-hour labels on the 190-trade sample (`source-reported`). Rejection tracker uses forward windows after each rejection event (observed ≥6 hours for the 56.25% subset) (`source-reported`).

### Entry (source-reported)

Autonomous memecoin trading decisions under the author's filter stack; not a standalone public entry formula in the abstract. The paper measures realized trades and separately tracks **rejected** candidates as a counterfactual corpus.

### Entry (research-proposed operationalization)

`research-proposed` for research use only: treat this study as a **fragility and counterfactual-rejection audit template** for memecoin DEX strategies — require (1) top-trade concentration tests, (2) hour-of-day non-confirmation disclosure, and (3) rejection-event drawdown tracking before any memecoin edge claim. Do not treat +117.7% cumulative as validated alpha.

### Exit

Not specified as a public rule in the abstract; deployment used the author's risk management stack over a 15-day paper window.

### Holding period

Per-trade holding not fully specified in the abstract; rejection tracker follows events for at least six hours in the reported subset (`source-reported`).

### Parameters

- Deployment length: 15 days (`source-reported`)
- Trades: 190 (`source-reported`)
- Worst-hour exploratory set: 3 hours, n=17 (`source-reported`)
- Rejection events: 184; 48 observed ≥6 hours (`source-reported`)
- Drawdown threshold in tracker: 50% from reference (`source-reported`)
- Top-trade ablation: remove top 3 trades (1.6%) (`source-reported`)

## Required data

- **Instrument**: Solana DEX memecoin tokens (AMM venue)
- **Universe**: Autonomous decision-time candidates and rejections during the 15-day window
- **Venue**: Solana decentralized exchanges
- **Timeframe**: Trade-level log over March 29–April 12, 2026
- **Fields**: Trade outcomes, entry hour, rejection events with forward price path for drawdown tracking
- **Point-in-time**: Paper-traded decisions; companion Zenodo deposit and audit script for reproduction
- **Funding/fee/spread**: Paper-trade setting; AMM fees/slippage not restated in abstract as a cost model — read paper before any cost claim

## Execution assumptions

- **Order type / fill**: Paper-traded autonomous deployment (`source-reported`); not live fills
- **What the source assumes**: measurement of outcomes and counterfactual rejections, not capital deployment
- **What the Scout does not assume**: no claim that paper-trade paths equal live AMM fills, priority fees, or MEV

## Evidence

### Source-reported

- 190 trades; win rate 40.5%; mean per-trade +0.62%; cumulative **+117.7%**
- Skewness −1.21; excess kurtosis 6.61
- Worst 3 entry hours (n=17): mean −11.60% vs others (n=173) +1.82%; **MWU p = 0.5634** (non-confirmatory)
- Rejection tracker: 4,874 observations / 184 events; **27/48 (56.25%)** of ≥6h events reached −50% drawdown; full-cohort 17.9% censored lower bound
- **Top 3 trades (1.6%) removal flips cumulative return unprofitable**
- Author deposits trade log, rejection corpus (CC-BY-4.0), assertion-based audit script (MIT), Zenodo DOI 10.5281/zenodo.20043301

### Independently reproduced

`not independently reproduced`

The author provides an assertion-based reproduction script that exits zero iff every headline number reproduces from deposited CSVs. This Scout cycle did not run that script.

### Negative evidence

- Hour-of-day effect is **not** statistically confirmed (p = 0.5634)
- Cumulative return is **fragile** to removing 1.6% of trades
- Majority of sufficiently observed rejections still hit deep drawdowns (56.25% at −50%)
- Heavy tails (negative skew, high kurtosis) undermine small-sample mean claims
- Paper-trade only; 15-day window; no out-of-sample continuation reported in the abstract

## Falsification plan

1. **Replicate audit script on Zenodo deposit**. Run the author's assertion script; if any headline fails to reproduce, mark this record contested.
2. **Walk-forward extension**. Apply the same decision stack and rejection tracker on a later Solana memecoin window. **Research-defined falsification threshold**: if cumulative return sign flips under equal trade count without the original top-3 trades, treat original +117.7% as sample-specific.
3. **Hour-of-day pre-registration**. Pre-register hour buckets without exploratory selection. Reject hour-aware risk management if MWU remains non-significant at n≥200.
4. **Rejection-tracker survival analysis**. Kaplan–Meier on time-to-−50% for all 184 events with proper censoring. If survival improves dramatically after a later date, document regime change.
5. **Fee/MEV stress**. Replay trades with priority fees, slippage, and sandwich-adjusted fills. **Research-defined falsification threshold**: net cumulative ≤ 0 after AMM + priority cost model.
6. **Concentration robustness**. Report trimmed means and deflated Sharpe (Bailey–López de Prado) as primary metrics, not raw cumulative return.
7. **Venue portability**. Same stack on another Solana DEX router or a non-Solana memecoin venue; if results are venue-idiosyncratic, do not generalize.

## Crypto portability

**Adapted** for Solana DEX memecoins; **unproven** for CEX-listed majors.

- 24/7 permissionless listing without equity-style sessions; hour-of-day effects may still exist via global retail clocks but are **not confirmed** here
- AMM / bonding-curve microstructure differs from CEX LOB; priority fees and MEV are first-order
- Token quality, rug risk, and liquidity rugs dominate tails — consistent with observed kurtosis
- Portability to CEX perps or blue-chip spot is **not** established
- Crypto portability is **not** authorization to trade

## Limitations

- **Paper-trade** only
- **15-day** window; 190 trades
- Exploratory hour selection inflates false-positive risk; paper already reports non-confirmation
- Headline cumulative is **top-trade dependent**
- Abstract does not fully specify the autonomous filter stack; reconstruction requires paper body / code
- No live capital, no AMM fill model in abstract
- Preprint (arXiv); revision history shows methodology expansion (v3)

## Implementation status

`not-implemented`

No Solana memecoin agent, hour-aware risk stack, or rejection tracker exists in our research stack. This record is research capture of deployment evidence and design lessons only.

## Adoption boundary

This record is research material only. Presence in this repository does not mean profitable, validated alpha, or approval for implementation, paper trading, testnet, or live trading. The source itself emphasizes measurement infrastructure and fragility, not a production strategy claim.

## Related Wiki records

- [[quant/strategy-research-record-spec-v1]] — canonical schema
- `solana-bonding-curve-sniper-cohort-contamination-adjusted-flow-2026-09-02.md` — Solana bonding-curve sniper cohort (related venue)
- `crypto-binance-smallcap-pump-reversal-regime-gated-falsification-2026-09-13.md` — Binance small-cap falsification family
- `telegram-coordinated-pump-dump-detection-contrarian-fade-2026-09-13.md` — Telegram P&D family
- `crypto-retail-systematic-trading-null-result-adversarial-audit-2026-09-01.md` — retail systematic nulls
- `crypto-walk-forward-window-optimization-double-oos-momentum-2026-09-04.md` — walk-forward / double-OOS discipline

## Sources

1. Arati Uday Kamat. "Hour-Aware Adaptive Risk Management for Autonomous Memecoin Trading on Solana DEXs: Evidence, Theory, and Design Lessons from a 15-Day Deployment." arXiv:2606.08232v3 [q-fin.TR], June 6, 2026 (v3 August 3, 2026). https://arxiv.org/abs/2606.08232
2. Companion dataset: https://doi.org/10.5281/zenodo.20043301 (Zenodo concept DOI, as deposited by the author)
