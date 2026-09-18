---
schema: strategy-research-record-v1
title: "Synthetic Black-Scholes Gamma Scalping on BTC Futures: HV/IV Regime + Delta-Band Hedge"
created: 2026-09-18
updated: 2026-09-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - bitcoin
  - gamma-scalping
  - volatility-risk-premium
  - synthetic-straddle
  - delta-hedging
  - black-scholes
  - futures-overlay
  - regime-filter
  - fmz
status: research-only
confidence: medium
source_as_of: 2026-09-18
sources:
  - "FMZ Quant strategy platform, Black-Scholes Gamma Scalping Strategy: Quantitative Wisdom from Options Market Makers, strategy id 523268, author ianzeng123, created 2026-01-04, page last modified approx. 8 months before capture. https://www.fmz.com/strategy/523268"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Synthetic Black-Scholes Gamma Scalping on BTC Futures: HV/IV Regime + Delta-Band Hedge

## Provenance

Public FMZ strategy page: **Black-Scholes Gamma Scalping Strategy: Quantitative Wisdom from Options Market Makers**, strategy id `523268`, author ianzeng123. Canonical URL: https://www.fmz.com/strategy/523268. Created 2026-01-04; page last modified about eight months before capture. Visible Pine backtest header: Binance `BTC_USDT` futures-style market, daily bars, 2025-01-04 to 2026-01-02. Source reviewed as of 2026-09-18 (public description + parameter surface; full Pine source gated).

Repository deduplication on current `main` found no record with FMZ id `523268` or the same normalized rule (synthetic BS straddle Greeks computed on BTC **futures** price path; enter/hedge overlay when HV/IV exceeds a long-vol threshold; gamma-trigger via ATR move; rebalance when synthetic net Delta leaves a band). Adjacent option VRP / dvol / Deribit records trade **listed crypto options** or option-implied surfaces — different data and instruments. This capture is a **model-overlay on futures**, not listed-option market-making.

## Economic mechanism

### Source-reported

The page frames the strategy as simulating options market-maker behavior: construct a **synthetic long straddle**, use **gamma** for dynamic hedging, and capture profits through volatility arbitrage — “make mathematics work for us.” Five Greeks named: Delta, Gamma, Theta (cost to overcome), Vega. Source states gamma trading profits cover time decay only when **realized volatility exceeds implied volatility**.

Three-layer signal filter (source):

1. **Volatility regime**: Historical Volatility / Implied Volatility. Source: when **HV/IV > 1.2**, actual volatility exceeds options pricing expectations — “ideal environment for gamma scalping.”
2. **Gamma scalping trigger**: trade when price movement exceeds **ATR multiples** (avoid overtrading).
3. **Delta hedge bands**: hedge when synthetic straddle net Delta deviates from neutral beyond set thresholds (simulate MM delta-neutrality).

Innovation claimed: migration of options Greeks calculations to **stock/futures trading**; dynamic vol-regime ID; multi-dimensional confirmation. Limitations claimed: cost sensitivity; BS assumptions may fail in extremes; complexity needing thorough backtest. Page positions the script as an **educational case**, not guaranteed profit. Parameter panel exposes strike offset from spot %, DTE, annual IV input, risk-free rate, dividend yield, HV lookback, HV/IV long/short vol thresholds, gamma ATR mult, delta hedge band %, vol-regime filter toggle, max concurrent positions, ATR stop/take-profit, max drawdown pause.

### Research interpretation

The research hypothesis (not source performance claim):

> On BTC, a **synthetic** BS straddle overlay that only rebalances futures exposure when (a) HV/IV is elevated and (b) price has moved enough ATR units can harvest a **realized-versus-implied style** edge via buy-low/sell-high delta rebalancing, without holding listed options.

Critical Scout caveat: the page computes Greeks from **assumed** option parameters (strike offset, DTE, user IV) applied to **BTC futures** prices. There is **no listed-option fill, no option bid/ask, and no true market gamma/theta** unless the trader separately holds options. Therefore this is a **pseudo-gamma futures overlay**, not true gamma scalping on Deribit/Binance options. Economic interpretation must keep that separation; any “VRP” language is model-implied, not exchange-implied.

## Signal

Source-specified reconstruction (defaults not fully numeric on public blurb — mark parameter values as underspecified where absent):

- Instrument: BTC USDT futures (page backtest header Binance BTC_USDT, **1d** bars).
- Synthetic option: strike = current price ± `Strike Offset %`; DTE parameter; annual IV user input; BS Greeks via normal CDF (Abramowitz–Stegun per source text).
- Lookback: HV period parameter (bars) for historical vol; ATR for move trigger and stops.
- Entry / overlay activation:
  - Regime: HV/IV ratio above long-vol threshold (source example **> 1.2**); optional short-vol threshold also exposed.
  - Trigger: underlying move > `Gamma Scalp Threshold` × ATR.
  - Delta: |synthetic net Delta| > `Delta Hedge Band %` → hedge/rebalance toward neutrality (buy/sell futures per sign).
- Exit / risk:
  - ATR-multiple stop loss and take profit
  - Max drawdown % pause
  - Max concurrent positions
  - Theta/time-value exit mentioned in prose (exact rule underspecified on public page)
- Holding period: rebalance-style; not fixed; position limits apply.
- Parameters: as listed in FMZ parameter panel above; **numeric defaults for HV window, ATR mult, bands, IV level are not fully stated in the public description** — exact replication requires gated source.

Underspecified: exact BS parameterization used for synthetic straddle payoff on futures; whether “positions” are futures-only directional legs; fee model; how IV is chosen if not from a live options feed (page shows annual IV as **input**, not necessarily Deribit IV).

## Required data

- Instrument: BTC USDT perpetual/futures OHLC (page header daily).
- Synthetic option metadata: strike offset, DTE, IV, r, q — **inputs**, not necessarily market option chains.
- Fields: close/high/low for ATR and HV; computed Delta/Gamma/Theta/Vega.
- Point-in-time: rolling HV and ATR on closed bars; no options surface required if IV is static input.
- Funding/fees: futures taker/maker costs not detailed on page; source warns cost sensitivity.

## Execution assumptions

Source-reported: futures market orders/position management in Pine `strategy()`; percent-of-equity sizing in code header; concurrent position cap; drawdown pause. No real options leg is implied by the public description. Fill/latency model not specified beyond standard TradingView/FMZ strategy simulation caveats on the page.

## Evidence

### Source-reported

FMZ page 523268 discloses the three-layer filter (HV/IV > 1.2 example, ATR gamma trigger, delta bands), educational framing, risk stack (ATR SL/TP, drawdown pause, position limits), parameter panel, and a Binance BTC_USDT daily backtest window (2025-01-04–2026-01-02). Page states strategy cannot guarantee every trade profits and is a learning case. Full Pine source and any equity curve metrics are behind login; this cycle did not treat page prose as validated performance.

### Independently reproduced

not independently reproduced

### Negative evidence

No independent replication identified. Source itself lists cost sensitivity, BS model failure in extremes, and complexity risk. Adjacent repository option-VRP and vol-surface records document fragility of VRP estimates — relevant priors for **real** option VRP, not automatic disproof of this futures overlay. **Structural negative (Scout interpretation):** synthetic Greeks on futures without listed options do not earn option theta/gamma PnL unless hedged against real option inventory; HV/IV with a **user-entered IV** can be tautological if IV is not market-implied.

## Falsification

Research-proposed falsification tests (not executed):

1. Replace user IV with live Deribit/Binance BTC IV series; research-defined falsification threshold: fail if overlay edge disappears when IV is market-implied rather than fixed input.
2. Compare to true listed-option long straddle + delta hedge on same period; fail “MM simulation” claim if synthetic overlay is not related to real option VRP.
3. Ablate HV/IV filter vs always-on gamma bands; fail if regime filter does not improve net after costs.
4. Parameter perturbation on ATR mult and delta band; fail if edge sign unstable.
5. Cost stress: futures fees + slippage on every hedge; fail if net ≤ 0.
6. Placebo IV: constant IV = historical mean; fail if HV/IV gate is not better than placebo.
7. Timeframe stress: replicate on 1h vs 1d; fail if only one untested bar size works.
8. Holdout year after 2026-01-02; fail if sample-only.

## Crypto portability

Mark: **adapted / direct for BTC futures overlay; unproven for listed-option parity**.

- Already on crypto futures (BTC_USDT).
- 24/7 continuous trading; ATR/HV windows are bar-based.
- No options funding; perp funding of futures hedge legs not modeled on page.
- Porting to real Deribit options requires different execution, IV surface, and margin — not the same strategy.
- Crypto portability is not authorization to trade.

## Limitations

- Public description + gated source; numeric defaults incomplete.
- `not independently reproduced`.
- **Synthetic, not listed, options** — mechanism label “gamma scalping” is pedagogical; economic edge is unproven futures rebalancing under an HV/IV gate.
- User-supplied IV can dominate results.
- Daily bar backtest header may not represent intraday hedge reality.
- Adjacent real-option VRP records are complementary context, not duplicates.
- Incremental-write threshold: met via distinct construction (BS Greeks overlay + HV/IV + ATR trigger + delta bands on crypto futures) vs listed-option VRP captures.

## Implementation status

`not-implemented`. No runtime change; no Wiki Brain write; third-party FMZ/Pine code not endorsed.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

## Related Wiki records

- `crypto-options-volatility-risk-premium-zscore-2026-08-31.md` and related Deribit/option VRP records — listed options, different instruments.
- `crypto-options-dvol-iv-premium-shock-spot-predictor-2026-09-13.md` — option IV shocks, different.
- `crypto-bitcoin-option-dynamic-hedging-whalley-wilmott-no-trade-band-2026-09-01.md` — real option hedging theory, different.

## Sources

- FMZ Quant, Black-Scholes Gamma Scalping Strategy, https://www.fmz.com/strategy/523268 (public description and parameters; captured 2026-09-18).
