---
schema: strategy-research-record-v1
title: "FMZ Flywheel Capital Architecture: Reserve Floor + Core DCA + Alpha MA Roll + One-Way Profit Recycle (542065)"
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - portfolio-construction
  - capital-allocation
  - dca
  - trend-following
  - flywheel
  - fmz
  - risk-budget
status: research-only
confidence: low
source_as_of: 2026-05-29
sources:
  - "FMZ strategy page: '飞轮量化系统' (Flywheel Quant System), strategy id 542065, author ianzeng123, created 2026-05-29. https://www.fmz.com/strategy/542065"
  - "Companion FMZ article (source-linked): 'X 上爆火的飞轮交易系统，从量化角度复现成策略？' https://www.fmz.com/digest-topic/10959"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FMZ Flywheel Capital Architecture: Reserve Floor + Core DCA + Alpha MA Roll + One-Way Profit Recycle (542065)

## Provenance

- **Source URL**: https://www.fmz.com/strategy/542065
- **Source type**: Public FMZ strategy page (Common strategy). Full JavaScript source is login-gated; this capture uses the public architecture description, parameter **names**, risk notes, and linked article identity.
- **Author on page**: ianzeng123
- **Platform**: FMZ / 发明者量化
- **Created (source-reported)**: 2026-05-29 14:32:33
- **Linked article**: https://www.fmz.com/digest-topic/10959 (source-listed as strategy write-up; article body not fully re-audited this cycle beyond the strategy page’s summary)
- **Source reviewed as of**: 2026-09-20
- **Deduplication audit (2026-09-20)**: Repository-wide search found **zero** prior records citing FMZ id `542065`, 飞轮量化系统, or this cash/core/alpha one-way recycle architecture. Adjacent records are different mechanisms:
  - `fmz-fractional-kelly-capital-budget-long-only-grid-perpetual-2026-09-19.md` — capital budget on a **grid**; no DCA core sleeve or alpha→core one-way recycle.
  - `fmz-multi-asset-risk-parity-btc-xau-spy-cl-ewma-erc-535843-2026-09-19.md` — ERC multi-asset risk parity; different allocation engine.
  - APFF FMZ 548843 — factor-lifecycle long/short factory; not flywheel capital architecture.
  - Meme momentum FMZ 548617 — cross-sectional alpha family; not reserve/DCA/core recycle.
  - Generic MA/grid/DCA teaching records — lack this three-wheel capital-closure thesis and one-way profit rule.

## Economic mechanism

### Source-reported

Source-reported origin: quantitative recreation of a “flywheel trading system” popularized on X. Three parts form a **capital closed loop**: cash flow, core asset, and Alpha — not isolated modules.

Source-reported loop: **reserve funds ensure survival; DCA accumulates core assets; Alpha seeks high returns with small capital; Alpha profits feed back into core assets.**

Source-reported emphasis: not market prediction or one-shot windfall, but **long-term compounding discipline** executed by code — do not lightly sell core assets; do not let Alpha losses damage principal; do not let the account lose the ability to continue in extreme markets.

Source-reported components:

1. **Cash-flow wheel — reserve line:** Real cash flow cannot be created ex nihilo; the code reproduces its role — avoid forced selling of core in stress. Set an account reserve (e.g. fraction of equity). **Before each order**, if post-order balance would fall below the reserve line, **skip** the operation.
2. **Core-asset wheel — DCA:** Periodic fixed-amount buys of core (e.g. BTC). **Buy-only**; goal is long-term share accumulation, not short-term trading.
3. **Alpha wheel — coin screener + MA roll trend:**
   - **Screener:** volume filter on top USDT perps; multi-MA-parameter backtest score (win rate, profit factor, drawdown, signal count); bonus for ATR vol percentile and recent volume surge; whitelist of top names.
   - **Trade:** short MA crosses above long MA → long; crosses below → short (if `Allow Short`); hard stop → flat; trail take-profit locks profit; if trend remains after TP → **re-enter / roll (滚仓)**.
   - Source-reported goal of roll structure: **asymmetric returns** — hard stop caps losses; trail + roll let profits run.
4. **One-way capital recycle:** When Alpha cumulative **realized** profit reaches `Alpha Sweep Min`, transfer that profit into core-asset DCA. Source-stated key rule: **Alpha profits may buy core assets; core assets do not subsidize Alpha losses.**

Source-reported risk notes (selected): strategy is an ideational recreation, **not** a stable-profit model; DCA core can sit in prolonged drawdown; Alpha can string small stops in chop; good screener backtests ≠ future validity; leverage, fees, funding, slippage matter; recycle presupposes Alpha can be long-run positive; reserve only reduces forced-selling probability; author recommends paper/small-capital observation before live.

Source-reported validation: public page documents architecture and parameter panel; code banner shows an FMZ backtest header (`2023-06-01`–`2024-06-01`, `1h`, `BTC_USDT`, `balance: 10000`) but **no performance series is published** on the public description. Full source login-gated.

### Research interpretation

This is a **capital-architecture / risk-budget** hypothesis with a **generic MA trend Alpha sleeve**, not a novel predictive factor.

Research interpretation (falsifiable):

1. **Survival constraint as first gate:** Reserve-floor pre-trade checks can reduce forced liquidation of core inventory in drawdowns — a risk/capacity effect, not guaranteed alpha.
2. **One-way recycle as compounding discipline:** Routing only Alpha **realized** profits into core (never the reverse) creates an asymmetric capital path; the economic bet is that disciplined small-risk trend bets can stock a long-horizon core without principal bleed.
3. **Alpha sleeve is replaceable:** MA cross + volume/ATR screening is a **research-proposed placeholder** implementation of “small high-elasticity risk capital”; the source’s distinctive claim is the **loop**, not MA edge.
4. **In-sample screening risk:** Multi-MA backtest scoring for whitelist membership is vulnerable to overfitting unless held out of sample (source acknowledges past screener performance ≠ future).

Component roles (normalized):

```text
Reserve: pre-trade equity floor; skip orders that breach it (Reserve Floor Ratio)
Core: DCA buy-only on Core Symbol (interval, amount, max total, optional Core Leverage)
Alpha budget: capped fraction/cap of equity (Alpha Max Ratio / Alpha Budget Cap / Alpha Leverage)
Alpha signal: MA cross long/short + hard stop % + trail activate % + optional re-entry roll
Alpha universe: volume-rank USDT perps + MA backtest score + vol/volume surge bonus → whitelist
Recycle: Alpha realized profit ≥ Alpha Sweep Min → into core DCA (one-way)
Discipline: core not sold to rescue Alpha; Alpha losses do not draw core
```

## Signal

### Formation timestamp

Research interpretation: DCA on calendar interval; Alpha screens on `Screen Interval Hours`; MA signals on configured `KLine Length` bars (exact timeframe not fixed in public text — `underspecified`). Timezone not published.

### Lookback

- DCA: calendar days (`DCA Interval Days`).
- Alpha MA: multi-parameter sets via `MA Params` + `KLine Length` for scoring — **numeric defaults not published** on the public page.
- Screener history for win-rate/PF/DD scores: `KLine Length` bars per MA set.

### Long entry (Alpha)

Source-reported: short MA **crosses above** long MA on whitelist symbols, within Alpha budget/cap/leverage, after reserve check.

### Short entry (Alpha)

Source-reported: short MA **crosses below** long MA **only if** `Allow Short` enabled; same budget/reserve constraints.

### Exit

Source-reported Alpha exits:

- Hard stop loss (`Alpha Stop Loss %`) → immediate flat
- Trail take-profit conditions (`Trail Activate %`) → lock profit
- After TP, if trend remains → **re-open / roll** (source-reported; exact re-entry spacing underspecified)

Core DCA: **no sell exit** in source design (buy-only accumulation). Account-level “exit” is not specified beyond user discretion.

### Holding period

- Core: open-ended accumulation (DCA max total may cap lifetime contributions).
- Alpha: trend-holding until stop/trail/roll; no fixed max hold published.

### Parameters (source-reported **names**; numeric defaults mostly unpublished)

| Parameter | Role (source) |
|-----------|----------------|
| Core Symbol | DCA instrument |
| Core Leverage | Core leverage |
| DCA Interval Days / DCA Amount / DCA Max Total | DCA schedule & cap |
| Reserve Floor Ratio | Equity safety floor |
| Alpha Leverage / Alpha Max Ratio / Alpha Budget Cap | Alpha capital envelope |
| Alpha Stop Loss % / Trail Activate % / Allow Short | Alpha risk/entry policy |
| Alpha Sweep Min | Min realized Alpha profit to recycle |
| Screen Interval Hours / Top Volume N / MA Params / KLine Length | Screener |
| Whitelist Size / Min Signals / Min Win Rate / Min Profit Factor / Max Drawdown % / Vol Surge Bonus | Screener gates |
| Goal Amount | Display/target only (source) |

**Underspecified:** almost all numeric defaults; MA period sets; exact trail formula; fee/funding treatment; fill model; screener score formula weights.

### Position sizing

- DCA: fixed notional per interval until `DCA Max Total`.
- Alpha: fraction/cap of equity with leverage; not vol-targeted in the public text.
- Recycle: realized Alpha PnL above sweep threshold → core DCA budget (source-reported flow).

### Specification completeness

**Architecture mostly specified; Alpha numeric rules and defaults underspecified.** Treat as research material, not a complete executable blueprint.

## Required data

- **Instrument:** core symbol (e.g. BTC USDT perp/spot as configured) + Alpha whitelist from **USDT perpetual** universe (source-reported volume screen).
- **Venue:** FMZ-connected futures/perp exchange (backtest banner references Futures_Binance BTC_USDT — source-reported header only).
- **Fields:** equity/cash balances; DCA schedule state; OHLC(V) for MA + ATR/volume scores; order/fill state for Alpha book.
- **Funding/fees/slippage:** named in risk notes as material; **not** modeled in public defaults (`data gap`).

## Execution assumptions

Source-reported: pre-trade reserve check; DCA market-style periodic buys; Alpha MA-cross orders with stop/trail; profit sweep to core.

Not established: maker vs taker, latency, partial fills, funding PnL, liquidation engine vs Core/Alpha leverage, capacity of Alpha whitelist names.

## Evidence

### Source-reported

- Public architecture: three-wheel loop, one-way recycle rule, reserve skip rule, screener dimensions, MA roll structure, risk disclaimers, parameter panel.
- FMZ backtest comment header (dates/symbol/balance) on the code banner — **not** a published equity curve or Sharpe on the description page.
- Companion article URL listed; not used to invent performance numbers this cycle.
- **No** source-reported live track record or net-of-cost performance series on the public strategy page as of 2026-09-20.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- Source-reported: not a stable-profit model; DCA underwater risk; Alpha chop losses; screener in-sample optimism; fees/funding/slippage; recycle needs positive Alpha expectancy.
- Structural (research interpretation): MA trend Alpha is generic and regime-dependent; whitelist scoring can overfit; one-way recycle stalls if Alpha expectancy ≤ 0; reserve floor cannot prevent gap risk.
- Spec: capital architecture ≠ validated alpha; MA sleeve is not independently evidenced here.

## Falsification plan

Research-proposed (not executed; not authorized):

1. **Loop integrity (research-defined falsification threshold):** In a pre-declared multi-regime sample, if core equity path under flywheel rules is **not** better than pure DCA-only control after identical total net contributions (including recycled Alpha), the recycle/alpha sleeve is non-load-bearing for capital growth.
2. **Reserve ablation:** With vs without reserve floor under the same Alpha stops; if forced core sells / ruin rate does not fall without the floor, the survival claim fails.
3. **One-way rule stress:** Compare source one-way recycle vs two-way (core subsidizes Alpha). If two-way does not destroy accounts in the sample, the asymmetric discipline claim is weaker; if both fail, MA Alpha is the binding constraint.
4. **Screener leakage:** Fit MA scores on train window only; evaluate whitelist on holdout. If holdout Alpha PF ≤ 1 after costs, reject screener-based Alpha edge.
5. **MA placebo:** Random MA params vs source-scored params; if no difference, scoring layer is cosmetic.
6. **Funding/fee stress:** Include perp funding + taker fees; if Alpha recycle stops firing after costs, the compounding story is cost-fragile.
7. **Action on failure:** Keep `research-only`; do not treat FMZ paper UI or backtest header as validation.

## Crypto portability

**Portability: `direct` for venue/instrument packaging (crypto perps DCA + Alpha); `unproven` for net outcomes.**

- Designed around crypto USDT perps and a core crypto asset.
- Risks: funding, liquidation under Core/Alpha leverage, 24/7 gaps, meme/perp universe instability in the screener, USDT depeg, venue risk.
- Not a prediction-market, TradFi-perp, or DeFi LP strategy.
- Crypto portability is not authorization to trade.

## Limitations

- **underspecified:** numeric defaults for nearly all Alpha/screener/risk parameters; trail math; cost model.
- **not independently reproduced**
- **No published performance series** on the public page.
- **Risk/capital design ≠ alpha** — MA sleeve is generic; distinctive claim is the capital loop.
- Full source login-gated; only public description used.
- Companion article not fully audited this cycle for extra numbers.

## Implementation status

No implementation in our research stack. Does not modify NautilusTrader/PyBroker; does not authorize Paper/Testnet/Live.

`implementation_status: not-implemented`

Source-side: FMZ hosts code + optional backtest UI; **not** treated as our validation.

## Adoption boundary

Research-only. Presence here does **not** mean profitable, validated, or approved for implementation, paper, testnet, or live trading.

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

## Related Wiki records

No stable Hermes Wiki Brain path known for this FMZ capture at write time. Do not fabricate Wiki links.

In-repo related: fractional Kelly grid FMZ; multi-asset risk parity FMZ 535843; APFF 548843; meme momentum 548617; various DCA/grid teaching records (different architecture).

## Sources

1. FMZ Quant strategy page. 「飞轮量化系统」 / Flywheel Quant System. Author ianzeng123. Strategy id 542065. Created 2026-05-29. https://www.fmz.com/strategy/542065 (public description, parameter names, risk notes reviewed 2026-09-20; full source not accessed).
2. FMZ article linked by the strategy page: 「X 上爆火的飞轮交易系统，从量化角度复现成策略？」 https://www.fmz.com/digest-topic/10959 (identity preserved; body not used for performance claims this cycle).
