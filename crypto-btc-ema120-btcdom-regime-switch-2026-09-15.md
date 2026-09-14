---
schema: strategy-research-record-v1
title: "BTC 120-Day EMA / BTCDOM Perpetual Regime Switch"
created: 2026-09-15
updated: 2026-09-15
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-15
sources:
  - "https://www.tradingview.com/script/F8w5LhQp-BTC-vs-EMA120-BTCDOM-Switch/"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# BTC 120-Day EMA / BTCDOM Perpetual Regime Switch

## Provenance

- **Primary source:** TradingView public open-source script, `BTC vs EMA120 / BTCDOM Switch`, author `zhangyixiangece`.
- **Stable public URL:** https://www.tradingview.com/script/F8w5LhQp-BTC-vs-EMA120-BTCDOM-Switch/
- **TradingView publication date shown:** 2026-04-28.
- **Source inspected directly:** 2026-09-15.
- The source is public and traceable. No private, paid, invite-only, or restricted source material is used here.
- Repository-wide and Hermes Wiki Brain pre-write searches found no record using the same `BTCUSDT` 120-day EMA state to rotate between BTC and `BTCDOMUSDT.P`. Existing records mention BTC dominance only as a contextual factor or generic regime feature, not this normalized two-asset switching rule.

## Economic mechanism

### Source-reported

The author frames the rule as a simple crypto regime switch. When Bitcoin is above its long-term trend, the strategy holds BTC to participate in directional upside. When Bitcoin is below the long-term trend, it rotates into Binance's Bitcoin-dominance perpetual (`BTCDOMUSDT.P`) on the premise that BTC dominance has historically tended to strengthen during altcoin-led drawdowns.

The source explicitly describes the script as a research backtest rather than a signal service and warns that the available `BTCDOMUSDT.P` history begins only in mid-2021, covering one broad BTC cycle.

### Research interpretation

This is a cross-asset crypto regime-allocation hypothesis, not merely an EMA timing rule. The proposed mechanism is:

1. **BTC trend state:** a 120-day EMA separates stronger BTC trend regimes from weaker BTC regimes.
2. **Relative crypto beta rotation:** below the BTC trend filter, capital stress may fall disproportionately on altcoins, causing Bitcoin's share of total crypto capitalization to rise.
3. **Tradable proxy:** `BTCDOMUSDT.P` converts that relative-performance state into a directly tradeable Binance perpetual exposure.

The key falsifiable claim is that the BTCDOM sleeve adds incremental risk-adjusted value versus simply going to cash when BTC is below its 120-day EMA. If the BTCDOM sleeve does not outperform a cash or BTC-only timing control after funding and switching costs, the distinct cross-asset mechanism is not supported.

## Signal

**Source-reported rule:**

- **Chart / reference instrument:** `BINANCE:BTCUSDT`, daily bars.
- **Secondary instrument:** Binance `BTCDOMUSDT.P` perpetual, fetched by the script with `request.security(..., lookahead=barmerge.lookahead_off)`.
- **Trend parameter:** EMA length = `120` daily bars by default.
- **Backtest start:** `2021-06-01` by default, matching the source's stated BTCDOM perpetual listing date.
- **Initial equity:** `100` by default; this is only a reporting normalization and is not alpha.
- **Formation timestamp:** after daily bar `t-1` is complete, compare `BTC close[t-1]` with `EMA120[t-1]`.
- **Position for day `t`:**
  - if `BTC close[t-1] > EMA120[t-1]`, allocate 100% to BTC;
  - otherwise allocate 100% to `BTCDOMUSDT.P`.
- **Shorting / flat state:** none. The source is always 100% allocated to exactly one of the two assets.
- **Return accounting:** the source manually compounds the close-to-close return of whichever asset is selected for the current day.
- **Switch condition:** a change in the lagged EMA state changes the held asset for the next daily return interval.
- **Holding period:** one day minimum; positions persist across days until the EMA state changes.
- **Rebalance cadence:** daily.
- **Overlapping positions:** none; one sleeve at a time.
- **Tie handling:** the source condition is strict `close[1] > ema[1]`; equality therefore falls into the BTCDOM sleeve.
- **Warm-up:** at least 120 daily BTC observations are needed for the EMA to be fully formed; exact Pine warm-up behavior before full initialization is not separately documented by the author.

**Execution-boundary caveat:** the source's manual equity curve applies the selected asset's current close-to-close return after forming the state from the previous completed daily close. This is causal at the signal level, but it implicitly assumes the portfolio can switch at the boundary used to start the next close-to-close return. The exact live fill timestamp, order type, spread, and first-tradable-price convention are not specified. A causal implementation should therefore treat next-bar open / first executable price as `research-proposed`, not source-reported.

## Required data

- **BTC reference market:** Binance BTC/USDT daily OHLC, at minimum close.
- **Dominance sleeve:** Binance `BTCDOMUSDT.P` daily close series and contract metadata.
- **Derived field:** 120-day EMA of BTC close.
- **Timeframe:** daily.
- **Timestamp convention:** TradingView/Binance daily-bar boundary; an implementation must explicitly lock the timezone/session convention used by the data feed.
- **Point-in-time requirement:** only completed day `t-1` BTC close and EMA may decide the sleeve for day `t`. `lookahead_off` is required for the secondary series.
- **Missing data:** source does not specify stale/missing BTCDOM observations, exchange outages, or contract interruptions. No imputation should be assumed.
- **Funding:** historical `BTCDOMUSDT.P` funding is required for realistic reproduction because the source explicitly states funding is omitted from its equity curve.
- **Costs:** BTC trading fees, BTCDOM perpetual fees, bid-ask spread, slippage, and any funding settlement during BTCDOM holding periods are required for a tradable test.

## Execution assumptions

### Source-reported

- Portfolio is always fully allocated to BTC or BTCDOM.
- The published research curve assumes **zero commission, zero slippage, and zero funding**.
- `BTCDOMUSDT.P` funding settles every 8 hours according to the source description, so omitted carry is economically material.

### Research-proposed for validation only

- Execute a state change at the first executable price after the completed daily signal bar rather than assuming frictionless same-boundary switching.
- Compare at least next-bar-open and short-latency market-order variants.
- Apply observed maker/taker fees, bid-ask spread, realized slippage, and exact historical BTCDOM funding.
- No leverage beyond 1x notional in the baseline test.
- Failed or missing BTCDOM market data should force no new BTCDOM entry for that interval rather than forward-filling returns.

## Evidence

### Source-reported

The TradingView source reports the exact two-sleeve rule, the 120-day EMA default, `2021-06-01` default backtest start, lagged signal construction, `lookahead_off` for BTCDOM data, and the fact that its displayed equity curves omit transaction costs, slippage, and funding. It also states that the sample covers only one broad BTC cycle and has not been validated out of sample on a fundamentally different regime.

The reviewed public page describes dashboard metrics including total return, maximum drawdown, CAGR, switch count, and yearly breakdowns, but it does **not** provide stable numeric performance figures in the textual source inspected here. No numeric return, Sharpe, CAGR, drawdown, or win-rate claim is therefore captured as evidence.

### Independently reproduced

not independently reproduced

### Negative evidence

- The source itself states the available `BTCDOMUSDT.P` sample begins in mid-2021 and covers only one broad BTC cycle.
- Transaction costs, slippage, and perpetual funding are omitted from the displayed research curve.
- The author explicitly states there is no out-of-sample validation on a fundamentally different regime.
- The 120-day EMA is a single fixed parameter; stability around nearby lengths is unverified.
- `BTCDOMUSDT.P` is an exchange-specific derivatives proxy for Bitcoin dominance, not the same object as a spot market-cap dominance index. Funding, basis, contract design, and venue-specific behavior can materially alter realized returns.

## Falsification plan

1. **BTCDOM incremental-value test.** Compare three causal daily strategies over identical dates: `(A)` source rule BTC↔BTCDOM, `(B)` BTC-above-EMA / cash-below-EMA, `(C)` BTC buy-and-hold. Use exact historical fees, spreads, slippage, and BTCDOM funding. `research-defined falsification threshold`: reject the distinct BTCDOM sleeve if A's net OOS Sharpe does not exceed B by at least `0.20` and A does not improve maximum drawdown by at least `5%` relative.
2. **Walk-forward / regime split.** Freeze EMA length before each test segment and evaluate expanding or rolling OOS windows, including bull, bear, high-volatility, low-volatility, and alt-led risk-on/off regimes. `research-defined falsification threshold`: reject broad robustness if more than half of OOS calendar/regime blocks have non-positive excess return versus control B.
3. **Parameter perturbation.** Test EMA lengths `90, 105, 120, 135, 150`. `research-defined falsification threshold`: reject parameter robustness if the 120-day setting is the only profitable net configuration or if median neighboring-length OOS Sharpe is `<= 0`.
4. **Execution-timing audit.** Compare source-style close-to-close accounting with first-executable next-bar fills. `research-defined falsification threshold`: reject the reported construction as practically reproducible if the sign of total net excess return versus control B flips under causal next-fill execution.
5. **Funding/cost stress.** Reproduce exact BTCDOM funding where available and stress additional round-trip friction at 5, 10, and 20 bps on switches. `research-defined falsification threshold`: reject practical tradability if net OOS Sharpe is `<= 0` at 10 bps round-trip switching friction plus realized funding.
6. **Dominance-proxy test.** Compare `BTCDOMUSDT.P` returns with an independently constructed point-in-time BTC market-cap dominance series. `research-defined falsification threshold`: weaken the stated dominance mechanism if rolling 90-day return correlation is below `0.60` for more than 25% of the common sample or if contract basis/funding explains most of the strategy's excess return.
7. **Placebo state test.** Circularly shift the BTC EMA state within calendar quarters while preserving each asset's return sequence. `research-defined falsification threshold`: reject the timing mechanism if the true net Sharpe fails to exceed the 95th percentile of placebo-state outcomes.

## Crypto portability

**direct** for the source-defined Binance instruments, because both signal and traded sleeve are crypto-native.

Material portability risks remain:

- `BTCDOMUSDT.P` is Binance-specific and may not have an equivalent contract or identical economics on other venues.
- Perpetual funding can dominate a low-turnover regime sleeve over multi-day holds.
- BTC dominance is a market-share concept while the traded contract is a derivative proxy with basis and liquidity effects.
- Crypto trades 24/7, so the daily candle boundary must be fixed explicitly; changing the UTC/session boundary can change EMA crossings and switches.
- Venue outages, delistings, contract specification changes, stablecoin quote risk, and Binance-specific liquidity all affect reproducibility.

## Limitations

- `not independently reproduced`
- No stable numeric performance results were available in the reviewed TradingView text.
- The source omits fees, spread, slippage, and BTCDOM funding from its research equity curve.
- The exact executable switch price is underspecified; close-to-close accounting is not automatically equivalent to a live fill.
- Only one broad BTC cycle is available after the BTCDOM listing date stated by the source.
- No independent out-of-sample validation is reported.
- The strategy is exchange- and contract-specific.
- The economic premise that BTC dominance rises specifically when BTC is below its 120-day EMA remains a hypothesis, not established causal evidence.

## Implementation status

`not-implemented`

No implementation in the quantitative runtime, no historical reproduction in the local research stack, and no Paper/Testnet/Live deployment has been performed by this Scout.

## Adoption boundary

This record is research material only. Presence in the repository does not mean the strategy is profitable, validated, approved for implementation, or authorized for Paper, Testnet, or Live trading.

## Related Wiki records

No Hermes Wiki Brain record with the same `BTCUSDT` 120-day EMA → BTC/`BTCDOMUSDT.P` rotation rule was found in the pre-write search. Repository records containing BTC-dominance concepts use them as contextual factors or broader regime variables rather than this two-asset switching construction.

## Sources

1. zhangyixiangece, **BTC vs EMA120 / BTCDOM Switch**, TradingView public open-source script, published 2026-04-28, directly inspected 2026-09-15: https://www.tradingview.com/script/F8w5LhQp-BTC-vs-EMA120-BTCDOM-Switch/
