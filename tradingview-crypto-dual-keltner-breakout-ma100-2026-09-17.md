---
schema: strategy-research-record-v1
title: "TradingView Crypto Dual-Keltner Breakout with MA100 Trend Exit"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
  - crypto
  - trend-following
  - breakout
  - keltner-channel
status: research-only
confidence: medium
source_as_of: 2026-09-17
sources:
  - https://www.tradingview.com/script/4u46vHxV-KELTNER-BREAKOUT-STRATEGY-FOR-CRYPTO-ASSETS/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Crypto Dual-Keltner Breakout with MA100 Trend Exit

## Provenance

- **Source type:** public TradingView open-source strategy page.
- **Title:** `KELTNER BREAKOUT STRATEGY FOR CRYPTO ASSETS`.
- **Author:** `hushedDiamond97573`.
- **Stable URL:** https://www.tradingview.com/script/4u46vHxV-KELTNER-BREAKOUT-STRATEGY-FOR-CRYPTO-ASSETS/
- **TradingView page date label:** `Jan 31`; the public page text reviewed in this Scout run does not expose the year beside that label, so no publication year is inferred.
- **Source inspected as of:** 2026-09-17.
- The page is labeled **OPEN-SOURCE SCRIPT**. This Scout normalized the public description and did not copy the Pine source.
- GitHub dedup on current `main` found no record containing TradingView script ID `4u46vHxV`, this title, or this author/source identity.
- The closest repository-level TradingView record is `tradingview-keltner-ema200-adx-volume-volatility-breakout-2026-09-16.md`. That record uses a Keltner close-breakout plus EMA200 direction, ADX strength and volume confirmation. This source instead uses a **two-horizon Keltner state/trigger construction (KC100 + KC20)** and an **SMA100 exit**, with no ADX or volume gate in the reviewed description.

## Economic mechanism

### Source-reported

The author describes the strategy as a crypto-specific volatility-breakout system. The stated idea is that crypto can sustain large directional moves after price extends outside Keltner Channels, so an outside-band condition is treated as continuation rather than exhaustion. The author also states that the Keltner construction uses ATR rather than standard deviation and that a 100-period simple moving average acts as a macro trend anchor and trailing exit.

The public description distinguishes two Keltner horizons:

- `KC 100` defines whether the broader market is sufficiently extended in one direction to qualify as a macro trend state.
- `KC 20` supplies the actual entry breakout trigger inside that already-qualified state.

The source explicitly uses no fixed take-profit, with the stated intent of allowing large trends to continue until the 100-period moving-average exit is reached.

### Research interpretation

The falsifiable hypothesis is that **nested volatility horizons improve breakout selectivity**. A short-horizon breakout (`KC20`) is only acted on when price has already demonstrated longer-horizon directional expansion beyond `KC100`; the slower channel therefore functions as a regime/state gate rather than another independent entry signal.

The SMA100 exit is economically separate from the alpha trigger: it is a trend-persistence / risk-management rule intended to remain in the position until the broader directional structure reverses. The research question is therefore whether the long-horizon Keltner state adds incremental continuation information over a plain KC20 breakout, not whether an SMA exit alone predicts returns.

## Signal

### Source-reported long logic

- **Macro requirement:** price must be trading above the `KC 100` upper band.
- **Entry trigger:** price crosses above the `KC 20` upper band.
- **Mandatory exit:** price closes below the `MA 100`.

### Source-reported short logic

- **Macro requirement:** price must be trading below the `KC 100` lower band.
- **Entry trigger:** price crosses below the `KC 20` lower band.
- **Mandatory exit:** price closes above the `MA 100`.

### Source-reported risk / holding behavior

- **Take profit:** none.
- **Stop / trailing exit:** the source describes the `MA 100` as the trailing exit; no separate fixed stop is specified in the reviewed prose.
- The holding period is therefore endogenous to the MA100 exit condition.

### Parameter and timing boundary

- `KC 100`, `KC 20`, and `MA 100` lengths are explicitly stated in the source description.
- The moving-average anchor is explicitly described as a **100-period Simple Moving Average**.
- The exact Keltner basis calculation, ATR lookback, ATR multiplier, source price, and whether the two Keltner horizons share the same multiplier are **underspecified** in the reviewed prose and must not be invented.
- The phrase `price crosses` is source-reported for entry, while the exit explicitly says `price closes` across the MA100 condition. The public description does not resolve whether entries may trigger intrabar or only at confirmed bar close.
- Re-entry rules, pyramiding, position sizing, leverage, simultaneous reversal behavior, and any cooldown are **underspecified**.
- `research-proposed` causal convention for later testing: form all channel values from completed bars and execute no earlier than the next bar unless the public Pine source proves a different causal order. This is not source-reported.

## Required data

- **Asset class:** cryptocurrencies; the source presents the strategy as crypto-only / high-volatility focused.
- **Instrument / venue:** no single symbol or venue is mandated in the reviewed description.
- **Market type:** `underspecified` — the page does not restrict the rule to spot, perpetual, futures, or another crypto instrument type.
- **Timeframe:** `underspecified` in the reviewed public description.
- **Fields:** timestamped OHLC bars sufficient to calculate Keltner Channels and SMA100. ATR-derived Keltner construction requires high, low and close at minimum.
- **Volume:** not required by the stated rule.
- **Funding / basis / open interest / order book:** not required by the stated signal, but perpetual implementations may require funding and mark/index data for realistic evaluation.
- **Point-in-time requirement:** KC20, KC100 and SMA100 must be computed only from information available at the signal timestamp; no future bar data may enter channel or moving-average formation.
- **Timestamp / candle boundary:** venue-specific 24/7 candle boundaries can materially affect signals and must be fixed before reproduction.

## Execution assumptions

- **Signal-to-order timing:** `underspecified` for entries; exits are described using a close condition but exact fill timing is not stated.
- **Order type / fill model:** `underspecified`.
- **Fees, spread, slippage, latency and market impact:** not stated in the reviewed source.
- **Leverage / margin / liquidation:** `underspecified`.
- **Shorting:** short signals are explicitly part of the source rule; feasibility depends on the chosen crypto instrument.
- **Funding:** not discussed by the source. It must be modeled for perpetual-futures testing because long holding periods can make carry material.
- **No fixed take-profit:** source-reported. A later implementation should not silently add one and still claim exact source reproduction.

## Evidence

### Source-reported

The TradingView author presents the system as a volatility-breakout trend-following strategy designed specifically for cryptocurrencies and argues that crypto's high-volatility, parabolic behavior can sustain moves outside Keltner Channels. The reviewed public description gives the rule set but does **not** provide a traceable Sharpe ratio, CAGR, drawdown, profit factor, win rate, or other quantitative performance statistic that can be safely carried into this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The source's crypto-specific rationale is qualitative and has not been independently validated here.
- Exact Keltner construction parameters beyond the 20/100 channel lengths are missing from the reviewed prose.
- No explicit execution-cost model is reported.
- No source-reported regime, instrument, timeframe, or venue comparison was available in the reviewed text to establish robustness.
- A breakout beyond both long- and short-horizon channels can occur after substantial price extension, so late-entry / exhaustion risk is an explicit empirical question rather than assumed away.
- None of these limitations proves the strategy fails; they define what later research must test.

## Falsification plan

1. **Specification recovery:** recover the exact Keltner basis, ATR length/multiplier, source field, calculation timing and order semantics from the public Pine source before claiming exact reproduction. If unresolved, preserve them as `underspecified` or explicitly `research-proposed`.
2. **Primary baseline:** compare the complete `KC100 state gate + KC20 breakout` rule against a plain KC20 breakout using identical data, costs and MA100 exit. The nested-horizon thesis is weakened if KC100 does not improve out-of-sample continuation quality after accounting for reduced trade count.
3. **Exit ablation:** compare MA100 exit against a fixed holding period and a simple opposite KC20 break so the effect of the exit rule is not confused with entry alpha.
4. **Regime coverage:** test bull trends, bear trends, high-volatility ranges and low-volatility ranges across multiple crypto assets and venues.
5. **Cost sensitivity:** stress fees, spread and slippage; for perpetuals include funding. The hypothesis is rejected for a given implementation if cost-adjusted out-of-sample results lose the continuation edge relative to the simpler baseline.
6. **Direction split:** evaluate long and short legs independently because crypto's upside/downside trend structure and perpetual funding can be asymmetric.
7. **Parameter robustness:** once exact source parameters are recovered, test a small predeclared neighborhood around the channel lengths/multiplier rather than optimizing broadly after seeing results.

## Crypto portability

`direct` for the broad hypothesis because the cited TradingView source explicitly designs and describes the strategy for cryptocurrencies.

Portability to a particular implementation remains conditional on market structure:

- spot cannot execute the short leg without a borrowing/derivatives mechanism;
- perpetual futures introduce funding, mark/index pricing and liquidation mechanics;
- 24/7 candle boundaries vary by venue/data vendor;
- Keltner/ATR values can differ materially across fragmented crypto venues during volatile periods;
- liquidity and slippage can make apparent breakout continuation uneconomic on smaller assets.

## Limitations

- Exact Keltner ATR length, multiplier, basis/source and calculation details are `underspecified` in the reviewed public prose.
- Entry confirmation/fill timing is `underspecified`.
- Instrument, venue, market type and timeframe are `underspecified`.
- Position sizing, leverage, pyramiding and re-entry rules are `underspecified`.
- No traceable source-reported performance statistics were carried into this record.
- No independent Pine-source audit was performed in this Scout cycle.
- Not independently reproduced.
- Inclusion in this repository does not imply profitability or trading approval.

## Implementation status

`not-implemented`.

No PyBroker, Nautilus, paper, testnet or live implementation/validation was performed in this Scout cycle.

## Adoption boundary

Research material only. This record is not evidence of validated alpha and is not approval for implementation, paper trading, testnet or live trading.

## Related Wiki records

No stable Hermes Wiki Brain link was consulted or asserted in this GitHub-only Scout run.

Repository-level adjacent record used only for dedup context:

- `tradingview-keltner-ema200-adx-volume-volatility-breakout-2026-09-16.md` — also uses Keltner breakout logic but adds EMA200, ADX and volume confirmation; it does not use the source's nested `KC100 regime + KC20 trigger + SMA100 exit` construction.

## Sources

- TradingView — `hushedDiamond97573`, **KELTNER BREAKOUT STRATEGY FOR CRYPTO ASSETS**: https://www.tradingview.com/script/4u46vHxV-KELTNER-BREAKOUT-STRATEGY-FOR-CRYPTO-ASSETS/ (public open-source strategy page; reviewed 2026-09-17; page date label `Jan 31`).
