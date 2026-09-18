---
schema: strategy-research-record-v1
title: "Polymarket Football Path-Convergence Basket: Win + Low-Score Protection with Poisson Edge Filter"
created: 2026-09-18
updated: 2026-09-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - polymarket
  - prediction-market
  - football
  - soccer
  - path-convergence
  - basket-construction
  - poisson-goals
  - structured-prediction
  - early-exit
  - fmz
status: research-only
confidence: medium
source_as_of: 2026-09-18
sources:
  - "FMZ Quant strategy platform, Polymarket 足球路径收敛策略, strategy id 543788, author ianzeng123, created 2026-06-17, page last modified approx. 3 months before capture. https://www.fmz.com/strategy/543788"
  - "FMZ digest article, 在套利和预测之间：一次世界杯路径收敛策略的朴素实验, https://www.fmz.com/digest-topic/10973 (linked from strategy page; not independently used beyond the strategy-page summary)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Polymarket Football Path-Convergence Basket: Win + Low-Score Protection with Poisson Edge Filter

## Provenance

Public FMZ strategy page: **Polymarket 足球路径收敛策略**, strategy id `543788`, author ianzeng123. Canonical URL: https://www.fmz.com/strategy/543788. Created 2026-06-17; page last modified about three months before capture. Companion digest linked from the page: https://www.fmz.com/digest-topic/10973. Source reviewed as of 2026-09-18 — public description, parameters, and substantial Python source visible on the page (Gamma API, Poisson model, λ grid-fit, basket entry/exit).

Repository deduplication on current `main` found no record with FMZ id `543788` or the same normalized rule (Polymarket football multi-outcome basket: target-team win Yes + exact-score protection legs, Poisson cover-probability edge filter, exit on real basket bid convergence rather than settlement). Existing Polymarket records are crypto binaries, NegRisk conversion, finality carry, or market-making — different instruments and mechanisms.

## Economic mechanism

### Source-reported

Source frames the strategy as **neither risk-free arbitrage nor pure match prediction**, but a protective structured combination between the two. For one football match event on Polymarket it buys Yes on:

1. Target team win (main path),
2. Exact score 0-0 (protection if the match stays closed),
3. Exact score 0-1 (protection if the underdog scores once and the target side is temporarily behind).

The basket is **incomplete** — it does not cover all scores (source risk list: 1-1, 0-2, 2-2, etc. can lose). Stated goal: capture **in-match convergence of basket bid value** to a profit target, not necessarily hold to full-time settlement.

Entry filter (source):
- Basket ask cost = sum of leg asks ≤ `ENTRY_MAX_COST` (page default 0.92).
- Poisson goals model with λ_home, λ_away estimates model cover probability  
  `P(target win) + P(0-0) + P(0-1)` (mutually exclusive paths handled in code; overlapping configured scores would be netted).
- Require `model_cover − market_cost ≥ SAFETY_MARGIN` (page default 0.01).
- λ can be manual or calibrated from exact-score market quotes (grid search 0.05–5.00 step 0.05 on visible Python; also 0-0/0-1 closed-form fallback in code).

Live management (source Python):
- Polymarket Gamma event API for score, elapsed, ended.
- In-play Poisson re-estimation scales λ by remaining match time ratio.
- Exit when **sum of leg bids × shares ≥ entry cost + `TARGET_PROFIT` × shares** (default profit 0.02 per share) and bid depth ≥ `MIN_BID_SIZE`.
- After match end, stop active trading and wait redeem; management window buffer after kickoff.

### Research interpretation

Research hypothesis (not source-performance claim):

> On football Polymarket events where the favorite’s win ask is elevated but low-score exact paths remain cheap, an incomplete win+protection basket can (a) reduce single-path fragility versus long win-only, and (b) harvest **transient joint bid appreciation** during the match before settlement, if a transparent goals model still shows cover-probability edge over basket cost.

Scout interpretation: this is **prediction-market portfolio construction** with a simple structural model, not crypto alpha. Crypto portability is limited (see below). The disclosed Python makes the rule largely reconstructable; economic validity is untested by this Scout cycle.

## Signal

Source-specified reconstruction (defaults from visible FMZ Python):

- Instrument: Polymarket football event markets (page example slug `fifwc-aut-jor-2026-06-17`, win suffix e.g. `jor`/`aut`).
- Legs: `{EVENT_SLUG}-{WIN_SUFFIX}` Yes + `{EVENT_SLUG}-exact-score-0-0` + `...-0-1` (configurable `PROTECT_SCORES`).
- Formation: pre-match window `PRE_MATCH_ENTRY_WINDOW_S` (default 3600s before kickoff); no initial entry once live (`should_enter` rejects live/ended).
- Lookback/model: Poisson independent goals; `MAX_GOALS` default 10; `MODEL_MATCH_MINUTES` default 90; λ defaults home 2.2 / away 0.8; optional market calibration via exact-score samples `0-0,0-1,1-0,1-1,2-0,2-1,3-0`.
- Entry: basket asks depth ≥ `SHARES` (default 5); cost ≤ 0.92; model cover − cost ≥ 0.01; buy each leg at ask + `BUY_SLIPPAGE` (default 0.002).
- Exit: sell all legs when basket bid value ≥ cost + 0.02×SHARES and depth ok; sell at bid − `SELL_SLIPPAGE`; after `ended`, stop and redeem.
- Holding period: pre-match entry to in-play convergence (minutes–hours) or to settlement if target not reached; not a fixed horizon.
- Parameters: `EVENT_SLUG`, `WIN_SUFFIX`, `SHARES`, `ENTRY_MAX_COST`, `TARGET_PROFIT`, `SAFETY_MARGIN`, λ flags, `DRY_RUN`, slippage, timeouts, `MIN_BID_SIZE`.

Underspecified for universal transfer: selection rule for which matches/events to trade (source suggests favorites with cheap protection legs); λ calibration quality; exact-score slug naming across all Polymarket football templates.

## Required data

- Instrument: Polymarket football Yes contracts (team win + exact scores).
- Venue: Polymarket CLOB via FMZ; Gamma API for event state.
- Timeframe: pre-match entry; in-play minutes via Gamma `elapsed`/`score`.
- Fields: leg ask/bid/size; event score/time/ended; optional exact-score quotes for λ fit.
- Point-in-time: live quotes only; model inputs are pre-match λ or market-implied λ at decision time.
- Missing-data: incomplete depth blocks entry/exit; API delays noted as risk.

## Execution assumptions

Source-reported: sequential leg market/limit buys with slippage caps; rollback if a leg fails mid-basket (`close_all`); `DRY_RUN` mode; depth checks; redeem after end. Not risk-free; incomplete outcome coverage.

## Evidence

### Source-reported

FMZ page 543788 discloses the basket definition, cost and Poisson edge filters, λ calibration paths, live bid-value exit, parameter defaults, risk warnings (uncovered scores, simplified Poisson, liquidity, API issues), and links a digest essay explaining the “between arb and prediction” framing. Visible Python implements Gamma fetch, Poisson PMF/win sums, grid λ fit, and state machine WATCHING→ENTERING→HOLDING→CLOSING→DONE.

### Independently reproduced

not independently reproduced

### Negative evidence

No independent live track record identified on the public page. Source itself lists structural negatives: incomplete path coverage can lose; Poisson ignores red cards, injuries, tactics, VAR; thin books; model edge can be illusory if λ mis-specified. Absence of public PnL is not evidence of profitability.

## Falsification

Research-proposed falsification tests (not executed):

1. Walk-forward on archived Polymarket football books + settlement: fail if basket net of fees/slippage does not beat win-only baseline on held-out matches under source defaults.
2. Model placebo: shuffle λ or use equal-strength λ; fail if true Poisson filter does not improve entry quality.
3. Incomplete-coverage audit: measure loss rate on uncovered scores (1-1, 0-2, etc.); fail “protective” claim if uncovered-path losses dominate edge.
4. Exit-only ablation: hold to settlement vs bid-convergence exit; fail convergence thesis if early exit is not superior after costs.
5. λ calibration ablation: manual vs market-fit λ; fail if calibration does not change selection quality.
6. Liquidity stress: widen slippage / reduce depth; fail if edge dies under realistic books.
7. Leakage: entry only with pre-match information available at decision time; fail if in-play score used for initial entry.
8. Event-selection robustness: extend beyond one tournament template; fail if edge exists only on the demo slug.

## Crypto portability

Mark: **not applicable / limited**.

- Underlying is football match outcomes on Polymarket, not crypto prices.
- Portable **ideas**: incomplete multi-outcome baskets, model-cost edge filters, exit on joint bid convergence — could inspire crypto multi-outcome event packages (e.g. multi-strike or multi-window crypto binaries), but contracts, liquidity, and λ analogs differ.
- No crypto funding/perp mechanics.
- Crypto portability is not authorization to trade; this record is primarily prediction-market structure research.

## Limitations

- Sports event contracts; weak direct crypto alpha value — retained for prediction-market construction and falsification design.
- `not independently reproduced`.
- Poisson independence is a strong simplification.
- Basket incomplete; not an arb.
- Single-author FMZ implementation; selection bias in published examples.
- Incremental-write threshold: met via new family (football path-convergence basket + Poisson cover filter + bid-convergence exit) distinct from crypto Polymarket records.

## Implementation status

`not-implemented`. No Nautilus/runtime change; no Wiki Brain write.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

## Related Wiki records

- `polymarket-btc15-two-leg-completeness-hedge-sum-under-one-fmz-529152-2026-09-18.md` — completeness arb on crypto binaries (different).
- `polymarket-favorite-longshot-bias-crypto-politics-2026-09-14.md` — bias, not path baskets.
- `prediction-market-llm-confidence-weighted-value-bet-2026-09-04.md` and related prediction-market records — different filters/instruments.

## Sources

- FMZ Quant, Polymarket football path-convergence strategy, https://www.fmz.com/strategy/543788 (description + public Python; captured 2026-09-18).
- FMZ digest, https://www.fmz.com/digest-topic/10973 (linked companion essay; captured as provenance pointer 2026-09-18).
