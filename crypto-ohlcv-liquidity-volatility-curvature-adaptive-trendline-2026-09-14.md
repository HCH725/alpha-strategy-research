---
schema: strategy-research-record-v1
title: Adaptive Liquidity-Volatility Curvature Trendline with Impact-Efficiency Gain (TradingView FFTL)
created: 2026-09-14
updated: 2026-09-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
  - trend-following
  - volume
  - volatility
  - adaptive-filter
status: research-only
confidence: medium
source_as_of: 2026-09-14
sources:
  - https://www.tradingview.com/script/Bgceb4if-FluxVector-Liquidity-Universal-Trendline/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Adaptive Liquidity-Volatility Curvature Trendline with Impact-Efficiency Gain (TradingView FFTL)

## Provenance

- Primary source: exlux, **FluxVector Liquidity Universal Trendline / FFTL**, public TradingView open-source strategy, published 2025-10-26 21:25 UTC (TradingView page renders 2025-10-27 in some local-time views).
- Stable public URL: https://www.tradingview.com/script/Bgceb4if-FluxVector-Liquidity-Universal-Trendline/
- Source reviewed through the public description and full 102-line Pine Script v6 source on 2026-09-14.
- License header in the public source identifies Mozilla Public License 2.0 and © exlux. This record normalizes the method and does not reproduce the Pine script.
- Repository deduplication on 2026-09-14 found no existing record containing the TradingView identity `Bgceb4if`, `FluxVector Liquidity`, or `Directional Liquidity Pulse`. Related repository research uses Kalman-like filters, but not this combination of candle-flow pressure, realized-volatility curvature, impact efficiency, and one-bar state projection.

## Economic mechanism

### Source-reported

The author presents FFTL as an adaptive trendline intended to reduce false flips from shock candles and chop. The claimed design fuses three observable components: a **Directional Liquidity Pulse** from candle body/wick geometry and normalized volume, **realized-volatility curvature** from the second difference of rolling realized volatility, and **impact efficiency** measuring price change relative to bar range and participation. Their standardized combination controls the gain of a one-dimensional state filter. A one-bar slope projection is then used to anticipate whether price/trend configuration is likely to flip.

### Research interpretation

The falsifiable hypothesis is that trend persistence is more reliable when directional candle pressure and participation agree while volatility curvature and price-impact efficiency imply an information-bearing move rather than noisy range expansion. The adaptive gain should react faster during high-information states and slower during weak/noisy states. The predictive content, if any, therefore comes from the interaction of signed OHLCV pressure, volatility-state change, and impact efficiency; the Kalman-like recursion is primarily a state estimator rather than independent alpha.

## Signal

**Source-reported construction (Pine v6):**

- Price source default: `close`.
- Flow window default: 34 bars; allowed 5–500.
- Realized-volatility window default: 55 bars; allowed 5–500.
- Energy z-score window default: 34 bars; allowed 10–500.
- Adaptive gain bounds default: `k_min = 0.04`, `k_max = 0.68`.
- The publication text gives general tuning guidance of roughly 20–80 bars for flow and energy and 30–120 bars for volatility. These guidance ranges are distinct from the code defaults.

For each bar, define range `R = max(high-low, eps)`, body imbalance `(close-open)/R`, and wick imbalance `((high-close)-(close-low))/R`. Normalize volume by its `len_flow` SMA. The Directional Liquidity Pulse combines 60% body imbalance and 40% inverse wick imbalance, multiplies by normalized volume, then divides by the square root of normalized volume to stabilize the participation effect.

Realized volatility is the rolling standard deviation of log returns over `len_vol`; curvature is its second finite difference. Impact efficiency is the absolute source-price change divided by bar range, scaled by the square root of normalized volume.

Each component is rolling-z-scored over `len_energy`. The energy state is:

`z(DLP) + z(liquidity_density) - z(volatility_curvature)`.

A logistic transform maps energy into a bounded adaptive gain, further modulated by a logistic transform of impact efficiency. A smoothed DLP velocity creates a flow push in price units. The recursive trend state moves from its prior value toward current price plus 25% of that flow push using the adaptive gain.

The one-bar projection is `trend + (trend - trend[1])`.

**Entry / reversal:**

- Long condition: completed-bar `close < trend` and one-bar projection `> trend`.
- Short condition: completed-bar `close > trend` and one-bar projection `< trend`.
- On the short condition the code explicitly closes the named long entry and submits a short entry. An opposite `strategy.entry` in TradingView normally reverses an existing opposite position; exact broker-emulator reversal semantics must be preserved in reproduction.
- No stop-loss, take-profit, fixed time exit, or separate maximum holding period is defined. Positions persist until the opposite condition/reversal.
- Pyramiding is reported as 0 in the publication properties.

**Formation / availability:**

- The source states the gain uses only current and previous observations and is lookahead-off.
- The publication reports `calc_on_every_tick` off and warns that visual shapes can move during an open bar; conservative use should therefore act on completed bars.
- `process_orders_on_close` is reported off. Historical order-fill timing is therefore dependent on TradingView broker-emulator semantics rather than an explicit custom fill model; reproduction must audit the exact signal-bar versus next-tick/next-bar fill convention.
- There is no explicit warm-up gate in the code. `research-proposed`: use at least 90 completed bars under the default windows before permitting orders, then verify this conservative warm-up against Pine `na` propagation. This is not source-reported.

The algorithm is reconstructable from the public source, but the exact first tradable bar and broker-emulator fill timestamp remain platform-semantic details that must be reproduced explicitly.

## Required data

- OHLCV bars for the traded instrument.
- Source claims applicability across major FX, index futures, large-cap equities, liquid crypto, and major ETFs, from 1-minute through daily timeframes.
- Default publication demonstration: SPY 30-minute bars; this is not crypto empirical validation.
- Fields: open, high, low, close (or chosen price source), volume, timestamp.
- Rolling calculations must be point-in-time and use only current/past completed bars.
- Timestamp/session convention follows the chart exchange. `research-proposed`: for crypto reproduction, use continuous 24/7 bars with an explicitly frozen UTC candle boundary.
- Missing/stale volume is not handled explicitly by the source. `research-proposed`: fail closed for bars with missing/invalid OHLCV rather than impute.

## Execution assumptions

### Source-reported

The publication exposes strategy properties of USD 25,000 initial capital, USD base currency, 0.03% commission, slippage value 5, 3% of equity order sizing, pyramiding 0, process-orders-on-close off, calc-on-every-tick off, and recalculate-after-fill off. The source explicitly says orders are simulated on standard candles only and makes no performance claim.

### Research interpretation

The meaning of TradingView `slippage = 5` is instrument tick-size dependent, so it cannot be translated into a universal basis-point cost without the symbol specification. No explicit spread, market impact, participation cap, funding, borrow, liquidation, leverage, partial-fill, latency, or venue-failure model is supplied. Crypto perpetual evaluation therefore requires those items as separate observed or modeled costs; none should be silently inferred from the source.

## Evidence

### Source-reported

The source provides the complete open Pine implementation, default parameters, execution-property settings, intended market/timeframe scope, and qualitative failure modes. It explicitly states **no performance claims**. No Sharpe ratio, CAGR, win rate, drawdown, out-of-sample result, or statistically tested crypto result is reported on the page reviewed.

### Independently reproduced

not independently reproduced

### Negative evidence

- The author states sudden gaps and thin liquidity can still cause rapid flips.
- Very quiet regimes reduce feature contrast and may require slower settings.
- Visual shapes can move intrabar before settling at bar close, so intrabar alert use can differ from completed-bar behavior.
- No reported out-of-sample study, cross-venue test, parameter-stability test, or crypto-specific performance evidence was found on the reviewed source.
- The source combines several transformations and adaptive parameters; without ablation, it is unknown whether DLP, volatility curvature, impact efficiency, or merely generic trend persistence drives any apparent result.

## Falsification plan

All test protocols below are `research-proposed`; numeric pass/fail cutoffs are `research-defined falsification threshold` values, not source-reported strategy parameters.

1. **Walk-forward crypto test.** Use BTCUSDT, ETHUSDT, and SOLUSDT on at least two liquid venues, with frozen UTC bar boundaries and strict train/validation/test separation. Metric: net Sharpe and net return after all costs. `research-defined falsification threshold`: reject the crypto-alpha hypothesis if median out-of-sample net Sharpe across assets/venues is `<= 0`.
2. **Adaptive-gain ablation.** Compare full FFTL against (a) fixed-gain recursion, (b) no DLP, (c) no volatility-curvature term, and (d) no impact-efficiency modulation. `research-defined falsification threshold`: if the full model fails to improve out-of-sample net Sharpe over fixed gain on at least two of three assets, reject the claim that the feature fusion adds incremental predictive value.
3. **Parameter perturbation.** Perturb `len_flow`, `len_vol`, `len_energy`, `k_min`, and `k_max` by approximately ±25% without re-optimizing by test segment. `research-defined falsification threshold`: if sign of net return flips for more than half of neighboring configurations, classify the strategy as parameter-fragile.
4. **Cost/turnover stress.** Evaluate observed maker/taker fees, bid-ask spread, 5/10/20 bps round-trip slippage stresses, and perpetual funding where applicable. `research-defined falsification threshold`: if the strategy is net negative at 10 bps round-trip friction on liquid majors, reject practical short-horizon tradability at that cadence.
5. **Causal timing audit.** Recompute every feature from data available at or before the completed signal bar; compare TradingView-equivalent next-fill execution against an intentionally same-bar optimistic control. Any material performance advantage that disappears under causal next-fill timing is a leakage/execution falsification.
6. **Placebo test.** Circularly shift DLP/volume or randomly permute its sign within volatility-regime blocks while preserving price autocorrelation. `research-defined falsification threshold`: if the true strategy's net Sharpe does not exceed the 95th percentile of placebo outcomes, reject the feature-specific mechanism.
7. **Regime breakdown.** Report trend/range, high/low volatility, weekend/weekday, bull/bear, and venue subperiods separately. Reject claims of universal robustness if profitability is concentrated in a single narrow regime without a pre-declared regime gate.

## Crypto portability

**unproven**.

The source explicitly lists liquid crypto among intended markets and the signal only requires OHLCV, so mechanical portability is straightforward. However, the reviewed publication demonstrates SPY 30-minute settings and provides no crypto-specific empirical result. Crypto evaluation must separately handle 24/7 bar boundaries, fragmented venue volume, spot-versus-perpetual volume differences, funding, mark/index price, tick size, fee tiers, liquidation/margin, and exchange outages. Volume normalization may not be comparable across venues or between spot and perpetual contracts.

## Limitations

- not independently reproduced
- no source-reported performance evidence
- crypto empirical validity unproven
- exact historical fill/reversal behavior depends on TradingView broker-emulator semantics
- no explicit spread/impact/funding/borrow/latency/capacity model
- no explicit missing-volume handling
- no source-defined maximum holding period or protective stop
- multi-component adaptive construction creates material ablation and overfitting risk
- publication chart settings visible at review time differ from code defaults; this record treats Pine source defaults as the canonical parameter defaults and does not infer performance from the displayed chart

## Implementation status

`not-implemented`. No PyBroker, NautilusTrader, paper, testnet, or live implementation or validation was performed in this Scout cycle. This record only normalizes the public source for research review.

## Adoption boundary

`research-only`; `adoption: not-approved`; `approval_scope: research-only`.

Presence in this staging repository does not mean the method is profitable, validated alpha, approved for implementation, or authorized for Paper/Testnet/Live trading.

## Related Wiki records

No stable Hermes Wiki Brain related-record path was verified during this run, so no Wiki link is fabricated. Materially adjacent staging-repository research includes `forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05.md`, which uses a different Kalman-stabilized multi-feature signal and documents regime/turnover fragility; it is related cautionary evidence rather than a duplicate of FFTL.

## Sources

1. exlux, **FluxVector Liquidity Universal Trendline — FFTL**, TradingView open-source Pine Script v6 strategy, published 2025-10-26 21:25 UTC; source and page reviewed 2026-09-14. https://www.tradingview.com/script/Bgceb4if-FluxVector-Liquidity-Universal-Trendline/
