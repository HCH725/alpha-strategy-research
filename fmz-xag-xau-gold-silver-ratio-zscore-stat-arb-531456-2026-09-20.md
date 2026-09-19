---
schema: strategy-research-record-v1
title: "FMZ Gold–Silver Ratio Z-Score Statistical Arbitrage on XAG/XAU USDT Swaps (531456)"
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - pairs-trading
  - statistical-arbitrage
  - gold-silver-ratio
  - z-score
  - mean-reversion
  - fmz
  - precious-metals
status: research-only
confidence: low
source_as_of: 2026-03-12
sources:
  - "FMZ strategy page: 'Statistical Arbitrage Strategy' / Pine title 'Stat Arb(xag & xau)', strategy id 531456, author ianzeng123, created 2026-03-12. https://www.fmz.com/strategy/531456"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FMZ Gold–Silver Ratio Z-Score Statistical Arbitrage on XAG/XAU USDT Swaps (531456)

## Provenance

- **Source URL**: https://www.fmz.com/strategy/531456
- **Source type**: Public FMZ strategy page (Pine strategy banner + public description + parameter narrative). Full Pine source login-gated.
- **Author on page**: ianzeng123
- **Platform**: FMZ / 发明者量化
- **Pine title (source banner)**: `Stat Arb(xag & xau)`
- **Page tags (source)**: ZSCORE, RSI, ATR, SMA, EMA
- **Created (source-reported)**: 2026-03-12 11:50:47
- **Source-reviewed as of**: 2026-09-20
- **Deduplication audit (2026-09-20; origin/main)**: No prior record cites FMZ id `531456` or this exact XAG/XAU normalized-ratio + RSI50 + ATR 3:8 construction. Adjacent records are different:
  - `paxg-xaut-gold-token-pairs-percent-spread-zband-fmz-526812-2026-09-18.md` — **tokenized gold** pair (PAXG–XAUT percent spread); not gold–silver ratio.
  - EWY three-leg / TradFi matrix FMZ records — equity/perp residual stat-arb; different instruments.
  - FMZ median/MAD single-instrument reversion (549579) — not a two-asset ratio.
  - Cross-exchange spot spread FMZ 549412 — dual-venue same-asset inventory, not precious-metal ratio.
  - Funding-adjusted cross-exchange **perp** arb academic/FMZ family — different mechanism.

## Economic mechanism

### Source-reported

Source-reported thesis: **not** typical trend following; XAG/XAU statistical arbitrage assumes **gold and silver prices maintain a long-term mean-reverting relationship**. When **Z-Score breaks beyond ±2 standard deviations**, price deviation is statistically significant → reversion trade opportunities. Source claims (unverified) superior risk-adjusted returns in precious metals.

Source-reported ratio model:

- Use **20-period SMA** to standardize **XAG and XAU separately**.
- Compute their **ratio**, then smooth with **3-period EMA**.
- Source claims this is more stable than simple price ratios and filters short-term noise.
- When the **normalized ratio Z-Score** exceeds **±2**, deviation from historical mean is >2σ — framed as low-probability reversion entry timing.

Source-reported **RSI filter** (not classic overbought/oversold):

- **RSI = 50 as long/short filter**: **RSI < 50 allows long**; **RSI > 50 allows short**.
- Narrative: buy relative weakness expecting bounce; sell relative strength expecting pullback.
- Source claims this reduces counter-trend risk and improves signal quality.

Source-reported risk/reward:

- **Take profit 3× ATR**, **stop loss 8× ATR** → stated **1:2.67** risk-reward (source arithmetic: 8/3 ≈ 2.67 on the SL/TP wording as published — treat public “3:8 ATR” and “1:2.67” as **source-reported labels**; exact which leg is entry-to-TP vs entry-to-SL should be re-read in full Pine before any use).
- **14-period ATR** for adaptive stop/target.
- Source claims historical backtests show positive expected returns on precious-metals pair trading at this ratio.
- Risk note: statistical models fail; gold–silver ratios can shift with supply/demand and policy; recommend single-trade risk **≤2%** of capital.

Source-reported regime caveat: best in **sideways/ranging** markets; strong trends can extend deviation and cause large drawdowns; caution around major macro events.

Source-reported code banner (partial): Pine `strategy("Stat Arb(xag & xau)")`; `benchClose = request.security("XAG_USDT.swap", ...)` — **crypto-venue USDT swap** symbols appear in the public snippet (gold/silver perp-style contracts), not only OTC spot XAU/XAG. Full source login-gated.

Source-reported validation: marketing-style backtest language on the page; **no** public equity curve, sample window, or net-of-cost table on the description as of 2026-09-20.

### Research interpretation

This is a **two-asset precious-metals ratio mean-reversion** hypothesis implemented on **FMZ**, with Pine evidence pointing at **USDT-margined XAG/XAU swap** symbols (crypto venue packaging of metals).

Research interpretation:

1. **Structural ratio hypothesis:** Gold and silver share macro drivers but differ in industrial demand/elasticity; long-horizon ratio mean reversion is a classic RV thesis — **not proven** by this page.
2. **Operationalization:** Separate SMA-standardization + ratio + EMA smooth + z-score is a **specific filter stack**, not a raw price ratio; incremental research value is the public construction, not “pairs trading exists.”
3. **RSI50 directional gate:** Using RSI=50 as a **trend/relative-strength gate** (not OB/OS) is source-reported; whether it aligns with z-score side (e.g. long ratio when z low **and** RSI<50) is **partially underspecified** in English narrative vs code.
4. **Crypto-venue metals:** Trading XAG/XAU as USDT swaps adds funding, listing, and tracking risks absent from LBMA/spot metals pairs.

Component roles (normalized):

```text
Universe: XAG and XAU (page narrative + Pine request.security XAG_USDT.swap — crypto-venue metals perps/swaps research-proposed as primary instruments)
Ratio model: SMA20-standardize each leg → ratio → EMA3 smooth
Entry gate: |Z-Score| of normalized ratio ≥ 2 (source-reported)
Directional filter: RSI<50 allows long side; RSI>50 allows short side (source-reported; exact portfolio construction underspecified)
Risk: ATR(14)-based TP/SL with public "3 ATR / 8 ATR" labels; ≤2% account risk recommendation
Regime: source prefers range/chop; warns on strong trends
```

## Signal

### Formation timestamp

Not published. Research interpretation: closed-bar computation; tradable after bar close or on next bar (`underspecified`).

### Lookback

- **20** periods SMA for per-leg standardization (source-reported).
- **3**-period EMA on the ratio (source-reported).
- **14**-period ATR (source-reported).
- Z-score lookback for mean/std of the normalized ratio **not numerically published** on the public page (`underspecified` — may be implied same window or separate; must not invent).

### Long entry

Source-reported fragments:

- Z-score beyond **±2** as reversion setup.
- **RSI < 50 allows long**.
- Research interpretation of a coherent long book: buy the **undervalued** metal / sell the **overvalued** metal when ratio z is extreme **and** RSI filter permits — **exact leg mapping (long XAG vs long XAU vs long ratio) is underspecified** without full Pine.

### Short entry

- **RSI > 50 allows short**; paired with the opposite z-score extreme for reversion.

### Exit

Source-reported:

- **Take profit** at ATR multiple (page: 3× ATR).
- **Stop loss** at ATR multiple (page: 8× ATR) — note the unusual larger stop vs TP labeling; re-verify in source before any interpretation of expectancy.
- No time stop published.

### Holding period

Not published; implied multi-bar RV hold until TP/SL.

### Parameters (source-reported where stated)

| Item | Source-reported |
|------|-----------------|
| Per-leg standardize SMA | 20 |
| Ratio EMA | 3 |
| Entry \|Z\| | 2 |
| RSI filter | 50 midline |
| ATR length | 14 |
| TP / SL ATR mult. | 3 / 8 (page labels) |
| Single-trade risk cap | ≤2% (recommendation) |

**Underspecified:** z-score estimation window; which asset is “long”; portfolio notional; fees/funding; whether both legs are always hedged or single-sided; exact RSI length.

### Position sizing

Not published beyond ≤2% risk recommendation (`underspecified` notional/hedge ratio).

### Specification completeness

**Partially specified.** Public page gives ratio construction, z threshold, RSI50 gate, ATR multiples; hedge geometry and z window incomplete. Do not treat as complete executable blueprint.

## Required data

- **Instrument:** XAG and XAU — narrative precious metals; Pine banner shows **`XAG_USDT.swap`** (crypto-venue swap). Full pair symbol for XAU leg not visible in public snippet (`data gap` beyond banner).
- **Venue:** FMZ / connected exchange(s).
- **Market type:** Research interpretation: USDT-margined metal swaps/perps if following the Pine banner; source narrative also reads like classical metals RV.
- **Fields:** XAG and XAU prices; SMA/EMA ratio path; RSI; ATR(14); account equity.
- **Point-in-time / costs:** not specified; funding/fees material on swaps (`data gap`).

## Execution assumptions

Source-reported: ATR TP/SL; RSI/z gates. Not established: fill model, hedge simultaneity, borrow/short mechanics on metal swaps, funding PnL, capacity.

## Evidence

### Source-reported

- Public rule narrative: 20-SMA standardization, 3-EMA ratio, z≥±2, RSI50 filter, ATR14 3/8 multiples, regime caveats, ≤2% risk recommendation.
- Marketing-style claims of superior risk-adjusted returns / positive expectancy — **not independently verified**; no public sample metrics on the page.
- Pine banner symbol `XAG_USDT.swap` and helper `f_cov` fragment — partial code visibility only.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- Source-reported: ratio can **structurally shift**; strategies fail in strong trends; consecutive losses possible; statistical relationships need ongoing evaluation.
- Structural (research interpretation): gold–silver RV is well-known and competitive; z+RSI filter may lag; unusual public TP/SL labeling needs audit; swap funding can dominate; partial public source.
- Adjacent: PAXG–XAUT and other pairs records in-repo document cost/structure risks in crypto-packaged metals/pairs — caution, not a replication of 531456.

## Falsification plan

Research-proposed (not executed; not authorized):

1. **Ratio reversion test (research-defined falsification threshold):** On point-in-time XAG/XAU (venue-matched) data, over ≥80 z-extreme events, if mean forward reversion after fees/funding is **≤ 0**, reject the public mean-reversion entry hypothesis for that sample/venue.
2. **Construction ablation:** Raw price ratio vs SMA20-normalized+EMA3 ratio; if the source construction does not improve z-hit reversion vs raw ratio, the “more precise” claim fails.
3. **RSI50 ablation:** z-only vs z+RSI50; if RSI gate does not improve net expectancy or tail loss, it is non-load-bearing.
4. **Hedge vs one-leg:** If only one metal is traded, test vs true two-leg RV; single-leg may be commodity beta, not ratio alpha.
5. **Funding stress (swaps):** Include historical funding; fail if edge exists only without funding.
6. **Regime split:** Range vs trend subperiods pre-declared; if results live only in post-hoc range windows, mark regime-dependent.
7. **Action on failure:** Keep `research-only`; do not treat FMZ marketing language as validation.

## Crypto portability

**Portability: `direct` if instruments are crypto-venue XAG/XAU USDT swaps (as Pine banner suggests); `unproven` for net profitability; classical metals RV is `adapted` if ported from spot/LBMA literature.**

- Risks: funding, listing/delisting of metal swaps, tracking error vs spot gold/silver, 24/7 vs metals session gaps, USDT depeg, thin books on some venues.
- Not a prediction-market or DeFi LP strategy.
- Crypto portability is not authorization to trade.

## Limitations

- **underspecified:** z window, hedge geometry, RSI length, notional, costs.
- **not independently reproduced**
- **No public performance series**; marketing claims only.
- Full Pine source login-gated.
- Risk management (ATR stops) ≠ alpha; ratio RV may be crowded/cost-sensitive.
- Incremental value: **public reconstructable XAG/XAU ratio construction on FMZ/crypto-venue metal swaps**, not a novel economic discovery.

## Implementation status

No implementation in our research stack. Does not modify NautilusTrader/PyBroker; does not authorize Paper/Testnet/Live.

`implementation_status: not-implemented`

Source-side: FMZ hosts Pine strategy; **not** treated as our validation.

## Adoption boundary

Research-only. Presence here does **not** mean profitable, validated, or approved for implementation, paper, testnet, or live trading.

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

## Related Wiki records

No stable Hermes Wiki Brain path known at write time. Do not fabricate Wiki links.

In-repo related: `paxg-xaut-gold-token-pairs-percent-spread-zband-fmz-526812-2026-09-18.md`; EWY three-leg FMZ; FMZ 549412 cross-exchange spot; other pairs/stat-arb family records.

## Sources

1. FMZ Quant strategy page. "Statistical Arbitrage Strategy" (Pine: Stat Arb(xag & xau)). Author ianzeng123. Strategy id 531456. Created 2026-03-12. https://www.fmz.com/strategy/531456 (public description, tags, Pine banner fragment reviewed 2026-09-20; full source not accessed).
