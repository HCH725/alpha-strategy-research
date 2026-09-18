---
schema: strategy-research-record-v1
title: "Polymarket BTC 15m Adaptive Conditional Probability: Terminal-Distance Model with Stage Uncertainty Discount"
created: 2026-09-18
updated: 2026-09-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - bitcoin
  - polymarket
  - prediction-market
  - binary-market
  - conditional-probability
  - terminal-distance
  - bayesian-framing
  - expected-value
  - uncertainty-discount
  - openmarket
  - negative-evidence
  - fmz
status: research-only
confidence: medium
source_as_of: 2026-09-18
sources:
  - "FMZ Digest article, Adaptive Conditional Probability Modeling: A Practical Exploration and Implementation for Binary Markets, author 发明者量化-小小梦, created 2026-08-26. https://www.fmz.com/digest-topic/11020"
  - "FMZ strategy linked from the article: OpenMarket BTC 15-Minute Logistic Regression Prediction Strategy / adaptive conditional-probability implementation, strategy id 548121. https://www.fmz.com/strategy/548121"
  - "Gregory Young, OpenMarket GitHub project cited in the article: https://github.com/gregyoung14/openmarket"
  - "OpenMarket paper cited in the article: arXiv:2607.26245, 'OpenMarket: A Synchronized Polymarket-Binance Dataset for High-Frequency Prediction-Market Research' (cited by source; not independently re-read this cycle beyond the digest's summary of its conclusions)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Polymarket BTC 15m Adaptive Conditional Probability: Terminal-Distance Model with Stage Uncertainty Discount

## Provenance

Public FMZ Digest article: **Adaptive Conditional Probability Modeling: A Practical Exploration and Implementation for Binary Markets**, author 发明者量化-小小梦, created 2026-08-26. Canonical URL: https://www.fmz.com/digest-topic/11020. Article links implementation strategy id `548121` on FMZ. Source reviewed as of 2026-09-18.

The article also cites Gregory Young’s OpenMarket GitHub (https://github.com/gregyoung14/openmarket) and paper arXiv:2607.26245, and summarizes that paper’s **out-of-sample negative result** (43-feature public model does not consistently beat Polymarket book-implied probability after fees/spreads/slippage). That paper was not independently re-read this cycle beyond the digest’s summary — treat paper-level numbers as source-reported via the digest.

Repository deduplication on current `main` found no record with FMZ id `548121`, digest-topic `11020`, or the same normalized rule (terminal-distance Gaussian conditional probability for Polymarket BTC 15m, multi-horizon vol blend, drift shrinkage, **stage-uncertainty discounted tradable probability**, fee/VWAP EV gate, persistent entry evidence, and binary-book round-trip cost check). Adjacent Polymarket records: ETH LateAsk (late high-ask + Chainlink displacement), BTC two-leg completeness (sum of asks < 1), football path-convergence basket, tri-transformer market-making, Binance–Polymarket HF lead-lag (OpenMarket-adjacent but different signal family). This capture is a **probability-model + execution-cost architecture**, not those rules.

## Economic mechanism

### Source-reported

The article reframes binary-market trading from direction to **conditional probability**:

\[
P(Y=\mathrm{Up}\mid X_t)
\]

where \(Y\) is settlement above the official benchmark \(K\), and \(X_t\) includes current BTC vs \(K\), remaining time \(\tau\), multi-horizon volatility, short-term drift, path, and information quality.

Separation of quantities (source):

- \(p_t = P(Y=\mathrm{Up}\mid X_t)\) — model terminal probability
- \(q_t\) — **actual executable cost** via order-book VWAP + fees + slippage (not best ask alone)

Expected value per token (source formula and Rust snippet):

\[
EV_t = p_t(1-f) - (\mathrm{VWAP}_t + s)(1+f)
\]

Current entry threshold: **0.025** (2.5 cents expected edge per token after frictions).

**Anti-circularity** (source): Binance market data + official Price-to-Beat generate the probability; Polymarket book is used **only** for trading prices/depth/execution cost — market price is not an input feature used to claim market price is wrong.

**Terminal-distance baseline** (source):

\[
z_t = \frac{\ln(S_t/K)+\tilde{\mu}_t\tau}{\hat{\sigma}_t\sqrt{\tau}}, \quad p_{\mathrm{center},t}\approx\Phi(z_t)
\]

Volatility: one-second closes from Binance trade WS; blend realized vol over **60s / 5m / 15m / 30m** with weights **0.15 / 0.25 / 0.30 / 0.30** when ≥75% of window available; conservative floor on per-second vol.

Drift: 60s mean return shrunk by reliability \(n/(n+300)\); total drift contribution **clamped to ±0.25 × remaining sigma**.

Early-round confidence: first five minutes reduce log-odds confidence as stage data incompletes; confidence returns toward 1 as information quality improves.

**Stage-uncertainty discount** (source — core “adaptive” step):

\[
p_{\mathrm{trade},t}=\max(0.001,\, p_{\mathrm{center},t}-z_u u_t), \quad z_u=1
\]

\(u_t\) combines: recent volatility of the probability sequence; early-stage information deficiency; amount of vol history available. Same price distance does **not** carry the same credibility at second 30 vs minute 13.

Source cites OpenMarket paper conclusion: public 43-feature model **does not consistently outperform** Polymarket book-implied probability OOS after costs — negative evidence retained, not packaged as arb success. Implementation still **logs** 43 stage features every 5s + settlement labels for later stage-bucketed training; fixed feature weights **do not** drive live probability yet (feature-window meaning changes within a round).

**Execution / risk layer** (source):

- Entry evidence: candidate direction stable, net EV > threshold for **≥1.2s**, **≥5** valid updates; reset on direction change / EV loss / book check fail
- Pre-order book reload: binary complement sanity `Ask_up+Ask_down ≥ 0.98`, `Bid_up+Bid_down ≤ 1.02`
- Fee-adjusted round-trip loss if buy-then-sell entire position immediately: **max 4%** allowed
- Position size: **1/5 Kelly**, capped **0.1%–3% of equity**
- Holding exit (prediction): hold EV < **-0.005** AND decline ≥ **0.025** vs prior, confirmed **3×** over ≥**600ms** → `PREDICTED_EV_SHOCK_NEGATIVE`
- Price backstop: fixed stop `StopPrice = max(EntryVWAP − 0.50, 0.35)` (not moved); fixed TP **0.95** as catastrophe protection
- Four price concepts kept distinct: Binance trade, Chainlink reference, TWAP60, **official openPrice / Price-to-Beat** (terminal event uses official K only)
- State persistence via FMZ DB; paper vs live same state machine
- Author framing: **practical research experiment / paper-trading platform**, not validated live edge

### Research interpretation

The reconstructable research hypothesis is:

> For Polymarket BTC 15m binaries, a **transparent terminal-distance** conditional probability, after (a) multi-horizon vol and shrunk drift, (b) **stage-uncertainty discount**, and (c) **executable VWAP+fee EV gate**, can identify paper-tradeable moments more reliably than either raw direction indicators or uncalibrated early-round certainty — while OpenMarket-style public feature models may fail OOS against the book.

Scout interpretation: incremental value is the **architecture separating forecast credibility from executable monetization**, plus explicit OpenMarket negative context. The article does **not** claim stable live profitability.

## Signal

Source-specified reconstruction (defaults from digest; some code constants research-visible):

- Instrument: Polymarket BTC 15-minute Up/Down (`btc-updown-15m-{start}` slug assembly from UTC).
- Formation: continuous; terminal probability ~every 200ms; main loop ~50ms; feature snapshots every 5s (research only).
- Lookback: vol blend 60s/5m/15m/30m; drift 60s with n/(n+300); no Polymarket price in probability inputs.
- Entry: buy side when \(p_{\mathrm{trade}}\) vs VWAP yields net EV ≥ **0.025**, evidence ≥5 updates and ≥1.2s, book complement + ≤4% immediate RT loss pass; size 1/5 Kelly in [0.1%, 3%] equity.
- Exit: predicted-EV shock rule and/or fixed stop/TP as above; PnL measured on executable full-position liquidation VWAP.
- Holding period: until EV-shock exit, stop/TP, or settlement; not fixed clock.
- Parameters: EV threshold 0.025; z_u=1; drift clamp 0.25σ; stop formula; TP 0.95; RT max 4%; Kelly 0.2; evidence 5 / 1.2s.

Underspecified for bit-exact replication: full uncertainty-term formula for \(u_t\); exact confidence ramp in first 5 minutes; full 43-feature list (OpenMarket project); live fee constant \(FEE_RATE\); paper fill model details beyond “VWAP + slippage + estimated fees.”

## Required data

- Instrument: Polymarket BTC 15m binaries; USDC.
- Venue: Polymarket CLOB + Gamma API; Binance BTC/USDT public trade WS; Polymarket RTDS Chainlink/TWAP.
- Timeframe: sub-second book/probability; 1s Binance closes for vol; 15m settlement cycles.
- Fields: official openPrice K; S_t; both-side books; fees/slippage constants; optional 43 stage features.
- Point-in-time: official K required for terminal event; alternative prices research-only.
- Missing-data: incomplete vol history → lower \(p_{\mathrm{trade}}\) via uncertainty, not hard no-trade.

## Execution assumptions

Source-reported: paper default mindset; evidence persistence; RT-loss gate; 1/5 Kelly caps; binary book sanity; state recovery after restart. No claimed live fill quality or latency guarantee.

## Evidence

### Source-reported

FMZ digest 11020 discloses the conditional-probability framing, EV formula, terminal-distance model, multi-horizon vol weights, drift shrinkage/clamp, uncertainty-discounted tradable probability, anti-circularity split, evidence/RT-loss/Kelly/stop/exit rules, and OpenMarket paper citation with **negative OOS vs book-implied probability after costs**. Simulated log example: at 15s, central Down ~49.75% vs ask 0.43 looked like large edge; after VWAP/costs and uncertainty discount, net EV fell below 0.025 (or negative with thin vol history) — trade rejected at probability layer.

### Independently reproduced

not independently reproduced

### Negative evidence

OpenMarket public-feature OOS failure (as summarized in the digest) is **negative evidence** against “rich feature sets automatically beat Polymarket books.” Source also documents circularity risk if market price is both feature and benchmark. Adjacent repository Polymarket cost/finality/latency records are complementary negative context. Author states system remains for paper trading and data collection; logical completeness ≠ statistical validation.

## Falsification

Research-proposed falsification tests (not executed):

1. Stage-bucketed walk-forward on stored features + settlements: research-defined falsification threshold: fail if uncertainty-discounted EV gate does **not** improve paper net returns vs always-trade-at-center-p vs book-price-only baselines on held-out periods.
2. Calibration: reliability diagrams / Brier / Log Loss by stage; fail if \(\Phi(z)\) is systematically miscalibrated after claimed vol/drift controls.
3. Anti-circularity audit: recompute with market price removed vs included as feature; fail if edge only appears when circular.
4. Uncertainty ablation: z_u=0 vs 1; fail “adaptation” claim if discount does not reduce early-round losses.
5. Threshold sensitivity: EV 0.025 ± 50%; fail if sign of net edge unstable.
6. Execution stress: wider slippage, thinner books, 4% RT rule binding often; fail if paper edge vanishes at realistic costs.
7. Placebo K: perturb official benchmark slightly; fail if probabilities/trades are not sensitive to terminal definition (would indicate implementation bug).
8. OpenMarket feature gate: only admit stage features that add OOS skill **beyond book-implied probability**; fail production-feature claim if none qualify.

## Crypto portability

Mark: **direct for this product; unproven for other binaries**.

- Already crypto-native (BTC 15m Polymarket + Binance).
- Architecture (p vs executable q, uncertainty discount) portable in spirit to other crypto event contracts; K definition and venue rules must be re-specified.
- Not a perp/options strategy.
- Crypto portability is not authorization to trade.

## Limitations

- Digest-level capture; full strategy source gated; OpenMarket paper not re-read in full this cycle.
- `not independently reproduced`.
- Author explicitly non-validated for live edge.
- Early-round uncertainty and feature-window non-stationarity remain open research problems.
- Adjacent Polymarket records are different mechanisms — not duplicates.
- Incremental-write threshold: met via distinct terminal-distance + stage-uncertainty + EV-architecture family, with explicit OpenMarket negative-evidence linkage.

## Implementation status

`not-implemented`. Research capture only; no runtime change; no Wiki Brain write; third-party FMZ/OpenMarket code not endorsed.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

## Related Wiki records

- `polymarket-eth15-lateask-chainlink-displacement-fmz-545782-2026-09-18.md`
- `polymarket-btc15-two-leg-completeness-hedge-sum-under-one-fmz-529152-2026-09-18.md`
- `polymarket-binance-high-frequency-binary-lead-lag-2026-09-02.md`
- `polymarket-15m-crypto-tri-transformer-market-making-2026-09-13.md`
- `polymarket-football-path-convergence-poisson-basket-fmz-543788-2026-09-18.md`

## Sources

- FMZ Digest 11020, https://www.fmz.com/digest-topic/11020 (captured 2026-09-18)
- FMZ strategy 548121, https://www.fmz.com/strategy/548121 (linked implementation pointer)
- OpenMarket, https://github.com/gregyoung14/openmarket ; arXiv:2607.26245 (cited via digest)
