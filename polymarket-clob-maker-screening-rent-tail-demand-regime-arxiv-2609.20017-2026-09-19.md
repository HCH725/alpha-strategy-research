---
schema: strategy-research-record-v1
title: "Polymarket CLOB Maker Screening Rent: Settlement-Carried Tail Demand with Regime-Conditional Calibration Gaps"
created: 2026-09-19
updated: 2026-09-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - bitcoin
  - polymarket
  - prediction-market
  - clob
  - market-making
  - screening-rent
  - tail-demand
  - regime-conditional
  - calibration-gap
  - lmsr
  - multi-outcome-premium
  - microstructure
  - negative-evidence
status: research-only
confidence: medium
source_as_of: 2026-09-17
sources:
  - "Chengqi Zang, Gabriel P. Andrade, and Tomoyuki Nakajima, 'Who Aggregates Information? Screening, Rent, and the Coexistence of CLOB and AMM Prediction Markets', arXiv:2609.20017v1 [econ.GN], September 17, 2026. https://arxiv.org/abs/2609.20017"
  - "Full-text HTML reviewed 2026-09-19: https://arxiv.org/html/2609.20017v1 (Abstract; §1.1 Stylized Facts; §3–§5 model; §B.1 regime/calibration construction; Tables 1–4)"
  - "Cited empirical bases used by the source (not independently re-read this cycle beyond the paper's summaries): Akey et al. (2026) Polymarket Users record (588M trades / $67B volume); Dai et al. (2026) on depth withdrawal near short-horizon resolution; Bartlett and O'Hara (2026) Kalshi maker inventory-to-resolution evidence"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Polymarket CLOB Maker Screening Rent: Settlement-Carried Tail Demand with Regime-Conditional Calibration Gaps

## Provenance

- **Source**: arXiv:2609.20017v1 [econ.GN]
- **Authors**: Chengqi Zang (Gensyn AI; University of Tokyo), Gabriel P. Andrade (Gensyn AI), Tomoyuki Nakajima (University of Tokyo)
- **Version**: v1, submitted September 17, 2026
- **DOI**: https://doi.org/10.48550/arXiv.2609.20017
- **URL**: https://arxiv.org/abs/2609.20017
- **Full text**: https://arxiv.org/html/2609.20017v1 (reviewed 2026-09-19)
- **Primary crypto transaction sample (source)**: Polymarket Bitcoin five-minute up/down claims — **738,393 trades**, **275 markets**, ~**24 hours**, **$10.38M** notional, **15,134 accounts** sorted into makers vs retail by quoting behavior
- **Platform-wide PnL context (source, via Akey et al. 2026)**: 588M trades, $67B volume across Polymarket categories
- **Fee context (source)**: takers pay **1.8%**; makers pay **nothing** and receive no rebate; maker profit measured **after** fees

### Repository Deduplication Audit

Repository-wide search on 2026-09-19 found **zero** prior records citing `arXiv:2609.20017`, Zang/Andrade/Nakajima, CLOB screening rent, or settlement-carried maker tail demand. Adjacent prediction-market records are materially different:

- `polymarket-favorite-longshot-bias-crypto-politics-2026-09-14.md` — FLB as a **directional taker** bias (longshot losses / favorite gains) on Polymarket; does **not** normalize the CLOB **maker screening-rent** mechanism, nor the **regime sign-flip** of calibration gaps
- `polymarket-binary-mean-reversion-cost-sensitivity-2026-09-14.md` — taker mean-reversion on named contracts under cost stress
- `polymarket-binance-high-frequency-binary-lead-lag-2026-09-02.md` — cross-venue lead-lag, not maker inventory to settlement
- `polymarket-btc15-adaptive-conditional-probability-terminal-distance-uncertainty-fmz-11020-2026-09-18.md` — taker EV architecture on BTC 15m binaries
- `polymarket-btc15-two-leg-completeness-hedge-sum-under-one-fmz-529152-2026-09-18.md` — two-leg YES/NO completeness
- `defi-prediction-market-uniform-loss-amm-lvr-dynamic-liquidity-2026-09-02.md` — AMM/LMSR LP LVR, not CLOB maker screening rent
- `prediction-market-optimal-market-making-latent-belief-hjb-2026-09-01.md` — theoretical MM control, different construction
- `crypto-prediction-market-high-frequency-combinatorial-arbitrage-2026-09-01.md` — combinatorial arb, not regime-conditional maker carry

This capture is a **maker microstructure + regime-conditional calibration** family: classical noise-trader financing is absent on prediction-market shares; viable CLOB makers earn **screening rent by carrying the under-priced side to settlement**, with the under-priced side’s identity **flipping by price-path regime**.

## Economic mechanism

### Source-reported

Prediction-market shares (Polymarket/Kalshi-style) lack consumption value, cash flow, or a pre-resolution reference price. Classical Glosten–Milgrom delta-neutral CLOB market making requires payoff-uninformative noise flow to finance spreads; that flow is largely absent. The paper’s replacement is **state-contingent tail demand**: informed flow moves price to the informative posterior first; uninformed traders then overpay or underpay relative to that posterior.

Model implications (source):

1. A CLOB quote posted **before** a common signal that sits **inside** the post-shock signal band is **picked off**. Competitive makers therefore quote **outside** the band, **screen informed traders out of the book**, and earn rent by **carrying the complementary claim to resolution**.
2. When a CLOB coexists with an LMSR/CF-AMM on the same event, the usual hierarchy inverts: **informed flow routes to the LMSR**; the **CLOB survives on behavioral (tail-demand) rent**. AMM depth moves the CLOB premium with sign set by maker-side contestability (contestable books widen premium as depth grows; committed books compress it).
3. With **n ≥ 3** outcomes, binary-book CLOBs pin **switch** prices but leave the **level** (displayed belief) indeterminate along a gauge; assembling every YES leg costs more than $1, with excess concentrated in **committed markups**, not mids. LMSR prices the simplex coherently.

Three transaction-level facts on Polymarket (source §1.1):

| Fact | Source-reported content |
| --- | --- |
| **Fact 1 — earn at settlement** | **91.4%** of persistent makers’ profit arrives **at settlement**; **under 9%** from buying/selling before it. Makers end **+$45.3K**; retail **−$66.7K** in the BTC 5m sample. Platform-wide: winning accounts post limit orders that end on the winning side; losing accounts hit those orders. Near-call five-minute markets, makers **cut depth** (Dai et al.). |
| **Fact 2 — one-sided inventory** | Almost all maker profit comes from **buying (≈+$70K)** rather than selling (≈+$2.6K), concentrated **above the midpoint**: **+$52.4K** in (0.50, 0.80], **+$24.8K** in (0.80, 1.00], and **−$0.5K** from selling above 0.80. Maker holdings resolve in the maker’s favor **56.8%** of the time. Akey et al. conclude insider trading is unlikely to explain top-winner returns; the paper reads the edge as **screening**, not private information. |
| **Fact 3 — regime sign flip** | Calibration gap := **execution price − empirical resolution frequency of that side** (positive ⇒ side **overpriced**). Pooled mid-band gaps are small/mixed. Conditioning on path regime **reverses signs**: longshot band **+0.225** trending vs **−0.071** flippy; favorite band **−0.205** trending vs **+0.066** flippy. A side priced near **$0.29** wins ~**7%** when trending vs ~**37%** when flippy. Extreme tail remains asymmetric: ~$0.982 price vs 98.4% frequency (calibrated); ~$0.024 price vs 1.4% frequency (**longshot tail stays overpriced**). |

**Regime classifier (source §B.1)**: within-window price paths are labeled **trending** vs **flippy** with a **run-based classifier** — paths dominated by a **single directional run** are trending; paths with **frequent sign reversals** are flippy. Exact numeric run-count/reversal thresholds are **not fully restated** in the HTML sections reviewed; treat the qualitative rule as source-reported and the numeric cutoff as **underspecified** for bit-exact replication.

### Research interpretation

Reconstructable research hypothesis (MiMo interpretation; not a source trading mandate):

> On short-horizon prediction-market CLOBs (especially Polymarket crypto binaries), classical spread-making is not the financing model. A viable maker-like or passive-accumulation hypothesis is to **avoid the informed band**, **identify the regime-conditional under-priced side** (negative calibration gap), and **carry that side to settlement**, accepting that profit is **resolution-contingent** rather than spread-contingent. Simple fixed FLB (always fade longshots) is **incomplete**: mid-band gap signs **flip** with path regime, while only the **extreme longshot tail** shows persistent overpricing in the reviewed sample.

This is **not** authorization to market-make live. Screening rent is an equilibrium explanation of observed maker PnL, not a validated implementable strategy with capacity, adverse-selection, and fee nets beyond the paper’s sample.

## Signal

Source-specified pieces (reconstructable where stated; gaps marked):

### Formation timestamp

- **Crypto sample**: Polymarket BTC **5-minute** up/down markets; ~24-hour transaction window; trade-level timestamps as published by Polymarket/public reconstructions (Akey et al. lineage).
- **Platform PnL facts**: whole Polymarket historical record through the Akey et al. sample end used by the paper.
- Exact exchange timezone convention for the 5m windows is **not restated** beyond platform-native stamps — **underspecified** for bit-exact replication.

### Lookback / regime state

- Source: within-market price path over the observation window, classified **trending vs flippy** by the run-based rule in §B.1.
- Calibration gaps computed from **execution price vs empirical resolution frequency** of that side (band-level and regime-conditional tables).
- Exact numeric thresholds for “single directional run” vs “frequent sign reversals” — **underspecified** in reviewed HTML; `research-proposed` operationalizations must pre-register their own run/reversal cutoffs and not attribute them to the source.

### Entry (source-reported empirical maker behavior — not a live rule)

- Post **both sides**, but profitability comes from **buying** the side that is under-priced relative to empirical resolution frequency and **holding to settlement**.
- Quotes that would sit **inside** the common-signal band are picked off in the model; viable quotes sit **outside** that band (Lemma 1 no-pickoff floor in the paper’s model language).
- Near hard-to-call short-horizon closes, makers **reduce depth** (source cites Dai et al.).

### Entry (`research-proposed` operationalization — labeled)

`research-proposed` taker/passive-accumulation translation for research falsification only:

1. On a short-horizon crypto binary (e.g., Polymarket BTC 5m/15m), at a pre-registered formation clock, classify path regime with a **pre-registered** run/reversal rule (source qualitative rule; numeric cutoffs research-defined).
2. Estimate empirical resolution frequency for price bands using only **point-in-time** prior settled markets in a locked lookback.
3. Compute calibration gap = executable ask/mid for the side − empirical frequency.
4. Candidate accumulate side = **negative gap** side (under-priced): `research-proposed` mapping from source Fact 3 — **trending → favorite/mid-high band**; **flippy → longshot/lower band**.
5. Optional maker-style filter: only consider passive bids **outside** a pre-registered “signal band” proxy; skip when depth collapses near resolution.
6. Size: `research-proposed` small fixed fraction; paper does **not** publish a Kelly/sizing rule for this mechanism.

### Exit (source-reported)

- Terminal: **0/1 settlement**. Source mechanism earns **at resolution**, not via a mean-reversion exit.
- No source stop-loss/take-profit ladder for the screening-rent agent.
- `research-proposed` research exits if needed: (a) hold to settlement only; (b) mark-to-market abort if gap sign flips and gap magnitude exceeds a pre-registered threshold; (c) depth-abort if top-of-book size falls below a pre-registered floor.

### Holding period

- Expected: **from accumulation to market resolution** (minutes to hours on BTC 5m/15m families; longer on other Polymarket events).
- Overlapping positions across many concurrent short-horizon markets are possible; paper does not publish a portfolio-level constraint set.

### Parameters (source-reported)

| Parameter | Source value / statement |
| --- | --- |
| Taker fee | 1.8% |
| Maker fee / rebate | 0 / none |
| BTC 5m sample trades / markets / notional / accounts | 738,393 / 275 / $10.38M / 15,134 |
| Maker profit share at settlement | 91.4% |
| Pre-settlement maker profit share | under 9% |
| Maker vs retail sample PnL | +$45.3K vs −$66.7K |
| Buy vs sell maker profit | ≈+$70K vs ≈+$2.6K |
| Profit in (0.50,0.80] / (0.80,1.00] / sell above 0.80 | +$52.4K / +$24.8K / −$0.5K |
| Maker win frequency on holdings | 56.8% |
| Longshot gap trending / flippy | +0.225 / −0.071 |
| Favorite band gap trending / flippy | −0.205 / +0.066 |
| Pooled longshot / favorite mid-band gaps | +0.043 / −0.037 |
| Near-$0.29 side win rate trending / flippy | ~7% / ~37% |
| Upper-tail price vs frequency | ≈$0.982 vs 98.4% |
| Lower-tail price vs frequency | ≈$0.024 vs 1.4% |
| Multi-outcome YES-set premium slope on log n | +0.060 (p under 0.001); ~96% committed-markup term |
| NO-side set premium slope | +0.048; ~105% markup |
| Premium executable at size q≥100 shares | slope → ~0 (n.s.) |

Underspecified for bit-exact replication: numeric trending/flippy cutoffs; full book-level “signal band” construction; account classification algorithm details beyond “sorted by how they quote”; capacity and inventory limits.

## Required data

- **Instrument**: Polymarket binary event tokens (YES/NO); focal crypto sample = BTC 5-minute up/down; platform facts cover all Polymarket categories in Akey et al.
- **Universe**: Short-horizon crypto binaries for the regime-conditional hypothesis; multi-outcome events for the set-premium measurement.
- **Venue**: Polymarket CLOB (public trades/books). Model also studies LMSR coexistence; **transaction samples contain no AMM** (source limitation).
- **Timeframe**: Tick/trade-level; 5-minute crypto market clocks; settlement at event resolution.
- **Fields**: Trade price/size/side/timestamp; maker vs taker classification; market path; resolution outcome; optional depth; fees (taker 1.8%).
- **Point-in-time**: Regime label and calibration frequencies must use only data available before the decision clock; paper’s empirical gaps are **ex post** measurement objects — any live translation must rebuild them PIT.
- **Timestamp**: Platform-native; timezone convention underspecified in reviewed HTML.
- **Missing-data**: Not specified.
- **Funding/fee/spread**: Taker 1.8% included in source maker-profit framing (makers not charged); slippage/latency/queue not modeled for a live screener.

## Execution assumptions

### Source-reported

- Maker profit measured **after** fees; makers pay no fee and get no rebate.
- Model: makers post at t=0, cannot cancel after; informed trade first at t=1; tail demand second; settlement t=2.
- Empirical maker-rent facts are **descriptive**, not a backtested live execution stack.
- Multi-outcome premium **vanishes at size** (q≥100 shares/leg) — not a size arb.

### Research interpretation

Treat screening rent as **resolution-carry inventory risk** with severe adverse selection if quotes sit inside the informed band. Any research translation is **paper-only** until depth, latency, fill queues, and 1.8% taker economics (if taking rather than making) are stress-tested. Do not treat +$45.3K sample PnL as capacity evidence.

## Evidence

### Source-reported

- Transaction-level Polymarket BTC 5m sample + platform-wide Akey et al. PnL decomposition (Facts 1–2 hold platform-wide per source).
- Regime-conditional calibration gaps (Fact 3) documented on the short-horizon binary sample that has price paths.
- Multi-outcome set-premium reconstruction: 16,036 validated events, outcome counts 2–10; premium slope on log n; robustness to staleness, reweighting, category drops; placebo bundles of unrelated binaries reproduce **markup** channel but not book-center channel.
- Model results on pickoff screening, LMSR/CLOB coexistence, contestable vs committed books, n≥3 gauge indeterminacy, Θ(n/log n) collateral comparison for LMSR.
- Cited corroboration (source summaries, not re-read this cycle): Bartlett & O’Hara — Kalshi makers earn ~2× per contract in single-name markets and **accumulate the unpopular side to resolution**; Dai et al. — depth withdrawal near short-horizon resolution.

### Independently reproduced

`not independently reproduced`

### Negative evidence

1. **No AMM in transaction samples** — venue-choice/coexistence predictions are model + multi-outcome reconstruction, not direct dual-venue flow tests (source-stated limit).
2. **Regime facts are short-horizon-binary specific** — source says Fact 3 is documented on one contract type; do not generalize to all Polymarket categories without new tests.
3. **Multi-outcome premium is not a size arb** — slope collapses when every leg’s last trade is ≥100 shares; lives in thin far-from-center quotes.
4. **Placebo bundles reproduce markup channel** — much of the set-premium is per-leg committed markup, not multi-outcome economics.
5. **Persistent extreme-longshot overpricing** (≈$0.024 vs 1.4%) — buying deep longshots is **not** supported by the calibration table even when mid-band longshots look cheap in flippy regimes.
6. **Informed-flow pickoff** — any quote inside the signal band is model-predicted to lose; naive two-sided tight markets on short-horizon binaries are the failure mode the mechanism describes.
7. **FLB incompleteness / partial contradiction** — pooled favorite-longshot style rules can be wiped out or reversed when path regime flips; this record’s Fact 3 is **strengthening-with-caveat** evidence relative to `polymarket-favorite-longshot-bias-crypto-politics-2026-09-14.md`, not a wholesale rejection of FLB at the extreme tail.
8. Preprint; ~24h crypto path sample for Fact 3; account classification and run-threshold details incomplete in reviewed HTML.

## Falsification

Research-proposed falsification tests (not executed):

1. **PIT regime-stratified carry.** Rebuild calibration gaps PIT on a locked crypto-binary sample; trade only the negative-gap side to settlement. **Research-defined falsification threshold:** reject if net settlement PnL after taker fees/slippage is ≤ 0 versus always-hold-favorite and always-hold-longshot baselines on held-out periods.
2. **Regime ablation.** Disable trending/flippy split (use pooled gaps only). Fail the “regime-conditional” claim if pooled rule matches or beats the split rule OOS.
3. **Fixed-FLB baseline.** Always buy favorites (or always fade longshots) vs regime-mapped side. Fail incremental regime claim if fixed FLB equals or beats regime mapping OOS.
4. **Pickoff / band stress.** Compare passive bids inside vs outside a pre-registered band proxy. Fail screening story if inside-band bids are **not** worse at settlement.
5. **Depth filter.** Trade only when top-of-book size ≥ floor vs unrestricted. Fail implementability if edge exists only when depth is effectively zero.
6. **Horizon transport.** BTC 5m → 15m → daily crypto events → non-crypto. Fail crypto-short-horizon specificity if sign pattern does not hold on the declared family; fail generalization if it only works on the original 24h sample.
7. **Fee stress.** If the research agent **takes** liquidity, apply 1.8% taker fee; if it makes, model queue/fill probability. Fail if edge vanishes under the executed fee regime.
8. **Maker-win-rate audit.** Recompute “holdings resolve in your favor” frequency for the research rule; fail if the rule does not approach the source’s 56.8% class of outcomes on comparable bands.
9. **Multi-outcome size placebo.** Attempt YES-set completion at increasing size caps. Fail any “arb” reading if slope is zero at realistic size (source already suggests this).
10. **Insider/competing explanation.** Control for wallet-level skill clusters / copy flow; fail screening-rent attribution if a thin set of informed wallets explains the same PnL.

## Crypto portability

**Direct** for the empirical facts on Polymarket crypto binaries (BTC 5m is already crypto).

- **Adapted** for Kalshi crypto events, Polymarket ETH/SOL short horizons, and other CLOB prediction venues if fee schedules, tick sizes, and resolution oracles are re-specified.
- **Unproven** for AMM-only prediction venues (different LP problem; see LVR family records).
- **Not applicable** as a direct port to linear crypto perps/options without a binary/event settlement object.
- 24/7 crypto clocks vs venue resolution schedules; stablecoin collateral and venue risk apply.
- Crypto portability is **not** authorization to trade.

## Limitations

- Preprint; model + descriptive microstructure, not a validated live strategy.
- Fact 3 path sample is short-horizon and limited (~24h / 275 BTC 5m markets in the transaction slice).
- Trending/flippy numeric thresholds underspecified in reviewed HTML.
- No independent reproduction; Akey/Dai/Bartlett–O’Hara inputs not re-audited this cycle.
- Screening rent requires carrying inventory to **0/1 settlement** — path risk is total loss on the carried side, not mark-to-market noise.
- Multi-outcome premium evidence is **negative** for size-executable set arb.
- Relation to existing FLB record is complementary/partially tensioning, not duplicate.
- Incremental-write threshold: **met** via new maker screening-rent mechanism, new crypto-binary transaction evidence (settlement share, one-sided buy inventory), new regime-conditional calibration sign flips, and new multi-outcome size negative evidence.

## Implementation status

`not-implemented`

No Polymarket connector, regime classifier, screening-rent quoter, or settlement-carry inventory system exists in our research runtime. This record does not modify NautilusTrader, create a strategy family, or authorize Paper/Testnet/Live.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

Research capture only. Presence in this repository is not profitability evidence, not validation, and not permission to market-make or take liquidity on Polymarket/Kalshi or any venue.

## Related Wiki records

- [[quant/strategy-research-record-spec-v1]] — canonical schema
- `polymarket-favorite-longshot-bias-crypto-politics-2026-09-14.md` — FLB taker bias (related behavioral family; different agent and construction)
- `polymarket-binary-mean-reversion-cost-sensitivity-2026-09-14.md`
- `polymarket-binance-high-frequency-binary-lead-lag-2026-09-02.md`
- `polymarket-btc15-adaptive-conditional-probability-terminal-distance-uncertainty-fmz-11020-2026-09-18.md`
- `polymarket-btc15-two-leg-completeness-hedge-sum-under-one-fmz-529152-2026-09-18.md`
- `polymarket-eth15-lateask-chainlink-displacement-fmz-545782-2026-09-18.md`
- `defi-prediction-market-uniform-loss-amm-lvr-dynamic-liquidity-2026-09-02.md`
- `prediction-market-optimal-market-making-latent-belief-hjb-2026-09-01.md`
- `crypto-prediction-market-high-frequency-combinatorial-arbitrage-2026-09-01.md`
- `kalshi-btc-event-contract-spot-hedge-2026-09-15.md` — different venue/purpose (hedge overlay)

## Sources

1. Chengqi Zang, Gabriel P. Andrade, Tomoyuki Nakajima. "Who Aggregates Information? Screening, Rent, and the Coexistence of CLOB and AMM Prediction Markets." arXiv:2609.20017v1 [econ.GN], September 17, 2026. https://arxiv.org/abs/2609.20017
2. Full-text HTML: https://arxiv.org/html/2609.20017v1 (reviewed 2026-09-19)
3. Empirical bases cited by the source (summaries only this cycle): Akey et al. (2026) Polymarket Users; Dai et al. (2026) depth withdrawal; Bartlett and O'Hara (2026) Kalshi maker inventory.
