---
schema: strategy-research-record-v1
title: "Median/MAD Two-Stage Mean Reversion with Frozen Target Center (FMZ Teaching 549579)"
created: 2026-09-19
updated: 2026-09-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - mean-reversion
  - median-mad
  - robust-statistics
  - fmz
  - teaching-strategy
  - state-machine
status: research-only
confidence: low
source_as_of: 2026-09-16
sources:
  - "FMZ strategy page: 'Mean-Reversion Teaching Strategy (Median/MAD)', created 2026-09-16, author ianzeng123. https://www.fmz.com/strategy/549579"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Median/MAD Two-Stage Mean Reversion with Frozen Target Center (FMZ Teaching 549579)

## Provenance

- **Source URL**: https://www.fmz.com/strategy/549579
- **Source type**: Public FMZ strategy page (Common strategy; labeled teaching strategy). Full JavaScript source is login-gated; this capture uses only the publicly visible rationale, formulas, state machine, parameters, and validation notes.
- **Author on page**: ianzeng123 (FMZ community author; same page-author neighborhood as 549380 / 549412 / 548617, **different mechanism**)
- **Platform**: FMZ / 发明者量化
- **Created (source-reported)**: 2026-09-16 11:33:42
- **Source reviewed as of**: 2026-09-19
- **Deduplication audit (2026-09-19)**: Repository-wide search found **zero** prior records citing FMZ id `549579` or this exact median/MAD arm–confirm–frozen-center construction. Adjacent records are materially different:
  - Generic RSI/BB mean-reversion teaching or TV records — different signal family (oscillator/band vs robust location/scale z).
  - `crypto-perp-crowded-flush-reversal-microstructure-2026-09-12.md` — uses median/MAD **cross-sectional z-scores** as factor inputs in a multi-signal flush-reversal microstructure design; not a single-instrument two-stage mean-reversion state machine with frozen target center.
  - FMZ 549412 cross-exchange spot spread — dual-venue inventory convergence, not single-venue statistical reversion.
  - FMZ 549380 Robinhood LP — DEX fee-cost LP inventory.
  - FMZ 548617 meme momentum+funding — cross-sectional momentum, not mean reversion.
  - Three-channel breakout teaching (549476) — breakout channels, opposite directional family.

## Economic mechanism

### Source-reported

Source risk warning (public page): the strategy only detects deviations from a recent statistical price regime. It does **not** estimate intrinsic value and does **not** guarantee reversion. Persistent trends, structural changes, limited liquidity, fees, and slippage can all cause losses. Parameters must be revalidated for each instrument and timeframe.

Source-reported rationale: mean reversion is split into two stages. When price first moves far from its recent regime, the program **only records the extreme**. A trade becomes eligible only after the absolute deviation **contracts for several completed bars** and returns inside the confirmation zone.

Source-reported statistical reference:

```text
dynamic center = median(log(close))
robust scale = 1.4826 × MAD
deviation z = (log(current close) - dynamic center) / robust scale
```

Source-reported entry: reaching the extreme z threshold only **arms** the setup. Entry requires a configured number of consecutive contractions in `|z|`, a return inside the confirmation threshold, limited center drift, and enough distance to the frozen target to cover estimated round-trip costs. Downside deviation + reentry → long; upside deviation + reentry → short. All calculations use **completed bars**.

Source-reported exit design: the **target center is frozen at entry** so a moving reference cannot follow a persistent trend and falsely report completed reversion. Exit on any of: price reaches frozen center or remaining distance contracts to configured ratio; deviation expands beyond the extreme recorded during observation; live center drifts too far from frozen target; maximum holding time; fixed stop vs fill price.

Source-reported validation status: JavaScript `node --check` syntax validation passed; offline logic checks passed for odd/even medians, MAD direction, robust-center behavior, cost-distance filter, and arm–confirm–enter–exit–cooldown transitions; importable FMZ XML generated. **FMZ backtesting, paper trading, and live small-size validation have not been performed.** Backtest dates/symbol stored in XML are import settings, not reported results.

### Research interpretation

This is a **robust location/scale mean-reversion hypothesis** with an explicit **two-stage confirmation state machine** and a **frozen reversion target**, applied as a teaching/single-instrument contract strategy.

Hypothesized mechanism (research interpretation):

1. **Overreaction then partial retracement:** Extreme short-horizon price displacement relative to a robust rolling center is hypothesized to mean-revert at least partially when the displacement begins to contract (not merely when |z| is large).
2. **Confirmation as adverse-selection filter:** Requiring consecutive |z| contractions + reentry inside a tighter threshold aims to avoid catching a still-expanding move (knife-catch) and to wait for observable loss of extremity.
3. **Frozen center as anti-trend-tracking device:** Freezing the target at entry prevents the reference from drifting with a new trend and “completing” a false reversion; exits on center drift / renewed extremity are structural invalidation, not profit targets alone.
4. **Cost-aware arming:** Source requires distance to frozen target to cover estimated round-trip costs before entry — a fee-aware gate, though cost estimates themselves are not fully published.

This is **not** evidence that median/MAD mean reversion is profitable on any crypto instrument. The source is explicitly a teaching artifact with **no FMZ backtest/paper/live results**.

Component roles (normalized):

```text
Reference: median of previous N log closes (default N=120 completed bars)
Scale: 1.4826 × MAD of same window
Arm: |z| ≥ extreme threshold (default 2.5) — observation only
Confirm: consecutive |z| contractions + |z| ≤ reentry threshold (default 2.0) + limited center drift + cost-distance check
Entry: long after downside extreme+confirm; short after upside extreme+confirm; completed bars only
Size: fixed contract quantity (default 1); leverage default 1
Exit: frozen center / remaining-distance ratio | renewed extreme | live-center drift vs frozen target | max hold | fixed stop vs fill (default 4%, 0 disables)
Invalidation during observation: reference invalid → no entry
```

Exact numeric values for consecutive-contraction count, observation timeout, center-drift limit, remaining-distance exit ratio, max holding bars, cost estimate formula, and cooldown are described as **fixed teaching settings in the code** and are **not fully published** on the public page (`underspecified` beyond the defaults listed below).

## Signal

### Formation timestamp

Research interpretation from public description: all calculations use **completed bars** on the strategy’s configured timeframe (timeframe **not stated** on the public page — `underspecified`). Signal becomes actionable only after arm + confirm conditions on completed bars; no intra-bar repainting is claimed. Timezone/clock source not specified.

### Lookback

- Source-reported default lookback: **120 bars** for log-price median and MAD.
- Warm-up: at least 120 completed bars required before z is defined; source does not publish exact warm-up handling for partial windows.
- Endpoints inclusive/exclusive not specified (`underspecified`).

### Entry

Source-reported entry path:

1. On completed bars, compute center, MAD scale, z.
2. If `|z| ≥ 2.5` (default extreme), **arm** observation; record extreme.
3. Require configured consecutive contractions in `|z|`, return to `|z| ≤ 2.0` (default reentry), limited center drift, and remaining distance to **frozen-at-entry** target covering estimated round-trip costs.
4. Downside path → **long**; upside path → **short**.
5. Observation invalidated if reference invalid → no trade.
6. Fixed order size (default 1 contract); one instrument; one directional position at a time (teaching scope).

### Exit

Source-reported exit precedence not fully ordered; any of:

- Price reaches **frozen** center, or remaining distance contracts to configured ratio
- Deviation expands beyond extreme recorded during observation
- Live center drifts too far from frozen target
- Maximum holding time reached
- Fixed stop vs fill price (default **4%**; zero disables)

Plus source-described cooldown after trades (numeric cooldown `underspecified`).

### Holding period

Variable. Source publishes no numeric max holding default on the public page (teaching setting in code). Intended horizon is short-to-medium statistical reversion after an extreme; exact expected hold not source-reported.

### Parameters (source-reported public defaults)

| Parameter | Default | Description |
|-----------|---------|-------------|
| Lookback (参照周期) | 120 | Bars for log-price median and MAD |
| Extreme z (极端偏离线) | 2.5 | Arms observation setup |
| Reentry z (回靠确认线) | 2.0 | Must return inside this threshold |
| Order size | 1 contract | Fixed quantity |
| Leverage | 1 | Contract account leverage |
| Fixed stop | 4% | Vs fill price; 0 disables |

**Underspecified public gaps:** consecutive contraction count, observation timeout, center-drift limit, remaining-distance exit ratio, max holding time, cost/slippage estimate, cooldown, instrument universe, bar timeframe, exact MAD population definition (window endpoints).

### Position sizing

Fixed contract count (default 1), not vol- or z-scaled. No capacity claim.

### Multi-timeframe dependencies

None published; single lookback reference.

### Specification completeness

**Partially specified.** Core formulas, arm/confirm thresholds, frozen-center exit concept, and several defaults are public. Numeric teaching constants and venue/timeframe are not. Do not treat as a complete executable blueprint.

## Required data

- **Instrument / universe:** Source does not publish a fixed universe; page is a teaching template for a single contract instrument. Crypto portability is `unproven` for any specific perp/spot (research interpretation).
- **Venue:** FMZ-connected exchange as configured by the user; not specified on page.
- **Market type:** Contract account (source uses 张 / contract quantity); spot vs perpetual not fixed on the public page (`underspecified`).
- **Timeframe:** Completed bars; interval not published.
- **Fields:** Completed-bar closes (log close for median/MAD). No funding, OI, or order-book fields in the public rule.
- **Point-in-time:** Completed bars only (source-reported); no look-ahead claim beyond that design choice.
- **Timestamp:** Not specified.
- **Missing-data:** Not specified; offline tests mention odd/even medians but not null/stale bar policy.
- **Costs:** Entry requires distance to frozen target to cover **estimated** round-trip costs; estimation method not published. Fees/slippage not quantified in source-reported results (none reported).

## Execution assumptions

Source-reported / implied:

- Completed-bar decisions; fixed contract size; one directional position; teaching-scale leverage default 1.
- Offline state-machine and syntax checks only.
- **No FMZ backtest, paper, or live validation** (source-reported).

Not established:

- Fill model, latency, partial fills, margin mode, instrument liquidity, realistic fees
- Whether default 2.5/2.0 z thresholds are calibrated for any crypto vol regime
- Capacity

Research-proposed notes:

- Any choice of timeframe, universe, contraction count, or cost buffer not on the public page is **research-proposed** if used in later work.
- Porting to crypto perpetuals would add funding, mark/index, and 24/7 session issues **not present** in the source description.

## Evidence

### Source-reported

- Syntax validation (`node --check`) and offline logic checks for medians, MAD direction, robust center, cost-distance filter, and state transitions (public page as of 2026-09-19).
- FMZ XML generated with six teaching parameters; embedded source verified against standalone JS file (source-reported).
- **Explicit source-reported gap:** FMZ backtesting, paper trading, and live small-size validation **not performed**; XML backtest dates/symbol are import settings, not results.
- **No Sharpe, win rate, return series, or sample period performance is published.** This record claims no quantitative profitability figure.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- Source-reported: no backtest/paper/live; teaching scope; intrinsic value not modeled; trends/structural breaks/fees/slippage can lose.
- Related in-repo caution: cross-sectional MAD-based flush research and broader mean-reversion records document regime fragility of reversion rules — adjacent evidence, not a replication of 549579.
- Frozen-center design is itself an implicit negative acknowledgment that **moving** mean-reversion targets can fail in trends.
- No independent live audit of 549579 found this cycle. Absence of results is not evidence of profit or loss.

## Falsification plan

Research-proposed tests (not executed; not authorized):

1. **Cost-adjusted reversion test (research-defined falsification threshold):** On a pre-declared crypto instrument/timeframe, over ≥100 armed-and-confirmed setups, if median exit PnL after fees+slippage is **≤ 0**, reject the hypothesis that the published arm–confirm–frozen-center rule selects cost-positive mean-reversion entries in that sample.
2. **Confirmation ablation:** Compare (a) enter immediately at |z|≥2.5 vs (b) published two-stage confirm vs (c) confirm without frozen center (trail live median). If (b) does not dominate (a) on net outcomes, the confirmation layer is not load-bearing.
3. **Placebo z-shuffle:** Shuffle z series while preserving marginal distribution; if similar hit rates appear, the rule is not using temporal contraction information.
4. **Regime split:** Trending vs ranging subperiods (pre-declared). If edge exists only in a post-hoc selected regime, mark regime-dependent / not robust.
5. **Threshold perturbation:** Extreme 2.0/2.5/3.0 × reentry 1.5/2.0/2.5 grid on a **training** window; evaluate on holdout. If only a single spike works, flag overfit.
6. **Venue/instrument portability:** Same defaults on BTCUSDT perp vs a liquid alt perp vs spot. If results flip sign, mark `unproven` portability.
7. **Action on failure:** Reject for tested regime; do not retune without a new pre-declared rule.

## Crypto portability

**Portability: `unproven`.**

- Source is a generic FMZ contract teaching template, not crypto-empirical evidence.
- If adapted to crypto perps (research-proposed), material differences:
  - Funding and mark/index can dominate multi-hour holds
  - 24/7 sessions change “recent regime” meaning vs session-bound TradFi
  - Extreme meme/perp z-scales differ; 2.5/2.0 defaults are not calibrated
  - Contract step, leverage, and liquidation interact with 4% stop
  - Exchange downtime / gap bars vs completed-bar assumption
- Do **not** label `direct` crypto alpha; the source provides no crypto sample results.

Crypto portability is not authorization to trade.

## Limitations

- **underspecified:** timeframe, universe, several teaching constants, cost model.
- **not independently reproduced**
- **data gap:** no source performance series; full source login-gated.
- **source quality:** explicitly a **teaching** strategy; not peer-reviewed; author presents mechanism for learning.
- **mechanism generality:** robust mean reversion is a well-known family; incremental value of this capture is the **public two-stage arm/confirm + frozen-center exit construction and explicit unvalidated status**, not a novel economic discovery.
- **capacity / execution:** unknown; teaching defaults are 1 contract / 1× leverage.
- Ordinary generic mean-reversion indicator stacks would not clear the bar; this record exists because the public page publishes a **specific reconstructable state machine** with frozen-target invalidation logic.

## Implementation status

No implementation in our research stack. This capture does not modify NautilusTrader, PyBroker, or any quantitative runtime; it does not authorize Paper, Testnet, or Live execution.

`implementation_status: not-implemented`

Source-side (third-party only): syntax/offline logic checks only; FMZ backtest/paper/live **not** performed per public page.

## Adoption boundary

Research-only staging material. Presence here does **not** mean profitable, validated alpha, or approved for implementation, paper, testnet, or live trading.

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

## Related Wiki records

No stable Hermes Wiki Brain path is known for this FMZ capture at write time. Do not fabricate Wiki links.

In-repository related records for intake/dedup:

- `crypto-perp-crowded-flush-reversal-microstructure-2026-09-12.md` (MAD z as factor inputs; different construction)
- `fmz-binance-okx-cross-exchange-spot-spread-hedging-549412-2026-09-19.md`
- `fmz-robinhood-chain-v3v4-active-pool-lp-fee-cost-coverage-549380-2026-09-19.md`
- `crypto-cross-sectional-meme-momentum-funding-dynamic-rotation-2026-09-14.md`

## Sources

1. FMZ Quant strategy page. "Mean-Reversion Teaching Strategy (Median/MAD)." Author ianzeng123. Created 2026-09-16. https://www.fmz.com/strategy/549579 (public rationale, formulas, parameters, validation notes reviewed 2026-09-19; full source not accessed).
