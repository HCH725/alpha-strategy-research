---
schema: strategy-research-record-v1
title: "ETH 2H Volatility-Squeeze Breakout with Volume Confirmation and Locked Adaptive Exit Regime"
created: 2026-09-14
updated: 2026-09-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-14
sources:
  - "https://www.tradingview.com/script/T3t4yoJx-ETH-Momentum-Breakout-Strategy-geektrade-online/"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# ETH 2H Volatility-Squeeze Breakout with Volume Confirmation and Locked Adaptive Exit Regime

## Provenance

- **Primary source:** public TradingView open-source strategy page, `ETH Momentum Breakout Strategy [geektrade.online]` by `grinaypps`.
- **Stable URL:** https://www.tradingview.com/script/T3t4yoJx-ETH-Momentum-Breakout-Strategy-geektrade-online/
- **TradingView publication date:** 2026-03-03 as shown on the public page.
- **Source as-of:** 2026-09-14.
- **Source access:** public and traceable; TradingView marks the strategy as open-source.
- **Public-use boundary:** this record normalizes the rule and links the source; it does not reproduce the Pine source code.

## Economic mechanism

### Source-reported

The author describes a crypto trend-following breakout system for ETH, BTC, SOL and other major tokens on 1H–8H bars. The intended setup begins with volatility compression, requires a directional breakout with strong candle body, positive momentum and an unusually large volume bar, then holds the move using ATR-scaled exits. A daily regime filter blocks entries during very extended price states or abnormal volatility. At entry, an adaptive HOT / NORMAL / COLD regime is classified and locked for the trade so exit distances and stagnation patience are widened in stronger regimes and tightened in weak/choppy regimes.

### Research interpretation

The falsifiable mechanism is a **conditional volatility-expansion continuation** hypothesis:

- **Compression:** Bollinger Bands inside Keltner Channels identify locally suppressed realized volatility.
- **Release:** price must clear the volatility envelope by an ATR margin, reducing marginal breakouts.
- **Participation:** a volume spike is treated as evidence that the move is supported by broad trading activity rather than a thin wick.
- **Directional force:** linear-regression momentum must be positive and accelerating for longs, mirrored for shorts.
- **Macro regime:** daily EMA distance and longer-run ATR state attempt to avoid parabolic or panic regimes where breakout entries may be late or unstable.
- **Trade management rather than entry alpha:** HOT/NORMAL/COLD classification changes TP, trailing-stop and stagnation horizons after entry; this should be tested separately from the entry signal because it may improve payoff shape without adding predictive information.

The main incremental value versus existing squeeze/trend records is the **volume-confirmed breakout construction plus a regime locked at entry that changes exit geometry and stagnation tolerance**, not another generic squeeze indicator stack.

## Signal

**Signal specification status:** `underspecified` in two material places: the public description does not expose the exact formulas for the source's `Vol Rank` percentile calculation or `Trend Score`, and it describes linear-regression momentum semantically without the complete Pine expression. All exposed thresholds below are source-reported; missing formulas are not guessed.

- **Recommended instrument / timeframe:** ETH on 2-hour bars; author states major crypto tokens such as BTC and SOL are also targets, with 1H–8H variants.
- **Formation timestamp:** conditions are described as bar-based TradingView strategy conditions. The public description does not explicitly state `calc_on_every_tick`, order-fill setting, or whether execution is same-close versus next-bar; treat exact signal-to-fill timing as underspecified.
- **Core squeeze:** Bollinger Bands length 20, multiplier 2.0 standard deviations; Keltner Channel length 20, multiplier 1.5 ATR. A squeeze requires BB inside KC for at least 3 bars on the recommended 2H setup.
- **Release window:** breakout must occur within 6 bars after squeeze release.
- **Long breakout:** close above upper Bollinger Band plus `0.3 × ATR`; candle body must be at least 40% of full high-low range.
- **Short breakout:** close below lower Bollinger Band minus `0.3 × ATR`; mirrored candle-conviction rule.
- **Momentum confirmation:** source reports linear regression of price deviation from SMA(12) must be positive and accelerating for longs; mirrored bearish state for shorts. Exact regression window/expression beyond the stated SMA(12) reference is underspecified.
- **Volume confirmation:** current volume must exceed `1.8 × SMA(volume, 20)` on the recommended 2H setup.
- **RSI filter:** RSI(14) < 75 for longs and > 25 for shorts, intended to avoid entering at extreme overbought/oversold readings.
- **Daily EMA-distance gate:** price must remain within 35% of daily EMA200. The exact percentage-distance formula and whether the test uses absolute distance are not explicitly shown in the reviewed description; underspecified.
- **Daily volatility regime gate:** ATR must be between `0.3×` and `1.5×` its 100-period average according to the source description. Exact ATR length for this regime statistic is not exposed in the reviewed page; underspecified.
- **Cooldown:** 12 bars after each exit on 2H.
- **Default direction:** source's suggested 2H setting is **long only**. The architecture also includes mirrored short logic.

### Locked adaptive trade-management regime

At entry, the strategy classifies one regime and keeps it fixed for that trade:

- **HOT:** `Vol Rank > 60th percentile` AND `Trend Score > 1.5 ATR`; TP, SL and trail distances multiplied by 1.35; stagnation patience 15 bars; stagnation threshold 0.3 ATR.
- **NORMAL:** all states not classified HOT or COLD; default exit multipliers; stagnation patience 10 bars.
- **COLD:** `Vol Rank < 30th percentile` OR `Trend Score < 0.5 ATR`; TP, SL and trail distances multiplied by 0.75; stagnation patience 7 bars.

The exact construction/lookback of `Vol Rank` and `Trend Score` is not exposed in the reviewed public description, so this regime classifier is **underspecified** and must not be independently implemented from this record alone.

### Exits

Five source-reported exit mechanisms operate independently:

1. **TP2:** full-position take profit at `3.5 × ATR` on default 2H settings; source reports about 4.7 ATR in HOT and 2.6 ATR in COLD after scaling.
2. **ATR trailing stop:** `2.5 × ATR` default, ratcheting only in the favorable direction.
3. **Breakeven:** after `1.2 × ATR` favorable excursion, stop moves to entry plus `0.2 × ATR`.
4. **Stagnation:** source states a trade that fails to move by a threshold within regime-dependent bars is closed; default NORMAL description uses 10 bars and separately reports 0.5 ATR as the generic stagnation move threshold, while HOT explicitly lists 0.3 ATR. This internal presentation is ambiguous, so the exact per-regime stagnation threshold is underspecified.
5. **Timeout:** maximum 100 bars on 2H, approximately 8 days.

Optional modules are off by default: partial TP at 1.5 ATR, runner mode after partial TP, higher-timeframe EMA trend filter, IntoTheBlock crypto-fundamental filters, and session filter.

## Required data

- **Instrument / universe:** source-recommended ETH plus major liquid crypto tokens; Bybit perpetual examples are explicitly named for portability (`BYBIT:BTCUSDT.P`, `BYBIT:SOLUSDT.P`). Exact source backtest symbol for the headline ETH result should be treated as not fully pinned from the public description alone.
- **Market type:** intended for crypto; the application notes explicitly reference Bybit perpetual symbols, but the headline 2H ETH performance block does not fully specify the exact venue/contract. Mark the empirical sample's contract identity as `underspecified`.
- **Timeframe:** recommended 2H; variants described for 1H, 4H and 8H. Daily bars are additionally required for the macro regime gate.
- **Fields:** OHLCV sufficient for BB, KC/ATR, candle-body ratio, SMA(12), linear-regression momentum, volume SMA, RSI, EMA200 and ATR-state calculations.
- **Optional alternative data:** IntoTheBlock active addresses, large transaction count and sentiment only if the optional fundamental module is enabled; off by default.
- **Point-in-time:** all indicator calculations must use only observations available by signal formation. Higher-timeframe daily features must use completed/available daily state rather than future daily close values. The public page does not state exact Pine `request.security()` lookahead behavior, so this requires audit before reproduction.
- **Timestamp / session:** crypto is 24/7; venue timezone and TradingView candle-boundary convention must be frozen for reproduction.
- **Missing data:** not specified by source. No imputation should be introduced without an explicit research protocol.
- **Funding / fees / spread:** source-reported suggested commission is 0.1%. Funding, spread, slippage, market impact and liquidation mechanics are not fully described in the reviewed page and must be modeled separately for perpetual reproduction.

## Execution assumptions

- **Signal-to-order timing:** underspecified; source describes bar-based entry conditions but does not explicitly state fill timing or Pine strategy order-processing settings.
- **Order type:** underspecified.
- **Commission:** source-reported suggested setting = 0.1%.
- **Spread/slippage:** not specified in the reviewed description.
- **Funding:** omitted from the reviewed performance description despite perpetual portability examples.
- **Position sizing / leverage:** not clearly specified in the reviewed public description; do not infer from TradingView defaults.
- **Liquidity / capacity / partial fills:** not assessed.
- **Exit precedence:** source lists five independent exits but does not formally specify precedence when multiple exits are touched in the same bar; underspecified.
- **Intrabar ambiguity:** TP, trailing stop and breakeven can coexist; a bar-only backtest needs an explicit conservative same-bar path rule before independent reproduction.

## Evidence

### Source-reported

For the author's **2H ETH** test over **October 2020 through February 2026**, the TradingView page reports:

- initial capital: $10,000;
- net profit: approximately $29,700 / 197%;
- CAGR: approximately 29%;
- Profit Factor: 3.08;
- win rate: 56%, with winners reported about 2.4× larger than losers;
- maximum drawdown: approximately $4,200 / 14% of peak;
- return / max-drawdown ratio: 7.1×;
- approximately 12 trades per year;
- profitable in 6 of 7 calendar years, with 2022 described as the negative year.

The same page's introductory summary says approximately 65% win rate and 2.4:1 win/loss ratio; later detailed performance says 56% win rate. Because the page contains this inconsistency, **56% is treated as the more specific detailed performance figure, while the 65% headline is flagged as contradictory source text rather than reconciled by the Scout**.

No independent verification of the TradingView Strategy Tester report or Pine execution semantics was performed in this Scout cycle.

### Independently reproduced

not independently reproduced

### Negative evidence

- **Internal source inconsistency:** the page's introductory text reports ~65% win rate while the detailed performance block reports 56% for the 2H ETH sample.
- **2022 regime failure:** source reports only 6 of 7 profitable years and identifies the 2022 bear market as negative, indicating regime dependence.
- **Low trade count:** approximately 12 trades/year implies only on the order of tens of trades over the stated multi-year sample; performance statistics may have wide uncertainty and strong dependence on a few large winners.
- **Execution gap:** 0.1% commission is stated, but funding, spread, slippage and same-bar exit ordering are not documented in the reviewed description.
- **Adaptive-regime reproducibility gap:** exact `Vol Rank` and `Trend Score` formulas are not exposed in the description, so the full system is not independently reconstructable from the page text alone.
- **No reviewed OOS / walk-forward evidence:** the page reports one long historical sample but does not provide a separately frozen out-of-sample window in the reviewed text.

## Falsification plan

1. **Exact-code parity / leakage audit**
   - Data: public Pine source plus the exact TradingView symbol and 2H chart settings.
   - Test: reconstruct every formula, especially `Vol Rank`, `Trend Score`, daily `request.security()` behavior, and order-processing settings.
   - **Research-defined falsification threshold:** if any headline result depends on higher-timeframe lookahead, same-bar future information, or unavailable data, reject the empirical performance claim for research adoption.

2. **Chronological OOS / walk-forward**
   - Freeze parameters on an early training window and reserve later crypto history for validation across ETH, BTC and SOL.
   - Metric: net expectancy and risk-adjusted return after costs.
   - **Research-defined falsification threshold:** OOS net expectancy ≤ 0 or materially negative OOS Sharpe rejects the alpha claim; no retuning after seeing the validation set.

3. **Entry-component ablation**
   - Compare squeeze release alone; squeeze + breakout margin; + volume spike; + momentum; + daily regime gate.
   - Metric: OOS Sharpe, expectancy, drawdown and trade count.
   - **Research-defined failure rule:** if the full entry stack does not materially outperform a simpler breakout baseline after correcting for reduced trade count, reject the claim that the extra filters add alpha.

4. **Exit-regime ablation**
   - Compare fixed 3.5 ATR TP / 2.5 ATR trail against the locked HOT/NORMAL/COLD management.
   - Metric: OOS return, downside risk and tail dependence.
   - **Research-defined failure rule:** if adaptive exit scaling does not improve OOS risk-adjusted return or drawdown versus fixed exits, classify it as complexity without evidence.

5. **Parameter perturbation**
   - Perturb squeeze duration, breakout ATR margin, volume threshold, ATR exit multipliers, RSI bounds, cooldown and regime cutoffs around source defaults.
   - **Research-defined failure rule:** profitability confined to a narrow parameter island indicates overfit.

6. **Cost / perpetual stress**
   - Apply venue-specific maker/taker fees, bid-ask spread, slippage and realized funding for a Bybit/Binance perpetual reproduction.
   - **Research-defined falsification threshold:** if net expectancy becomes ≤ 0 under realistic taker execution plus funding, reject tradability of the reported edge.

7. **Regime breakdown / 2022 challenge**
   - Test bull, bear, sideways and high-volatility subperiods separately.
   - **Research-defined failure rule:** if positive full-sample results arise almost entirely from bull-regime exposure and remain negative in bear/sideways states despite the daily filters, weaken the claimed regime adaptivity.

8. **Venue / asset portability**
   - Freeze settings and compare ETH/BTC/SOL on at least two major venues with point-in-time listings.
   - **Research-defined failure rule:** sign reversal or severe collapse outside the source symbol/venue indicates sample-specific rather than portable alpha.

## Crypto portability

**direct**, because the source strategy and empirical discussion are explicitly crypto-focused and the page provides Bybit perpetual examples.

Portability still requires venue-specific treatment of:

- 24/7 bar boundaries and daily higher-timeframe alignment;
- perpetual funding and mark/index price conventions;
- maker/taker fee schedules and spread;
- stablecoin quote differences (USDT/USDC);
- exchange fragmentation and symbol listing history;
- liquidity/impact for smaller tokens;
- liquidation and margin when leverage is introduced;
- optional IntoTheBlock fields if the fundamental filter is enabled.

Direct crypto origin does not mean the source's ETH 2H result transfers automatically to BTC, SOL, other venues or other timeframes.

## Limitations

- TradingView community publication rather than peer-reviewed research.
- Full system is `underspecified` from the public description because `Vol Rank`, `Trend Score`, exact linear-regression formula, daily higher-timeframe lookahead setting, order-fill timing, and same-bar exit precedence are not fully exposed in the reviewed text.
- Headline and detailed win-rate figures conflict (65% versus 56%).
- Exact headline ETH venue/contract is not pinned in the public description reviewed here.
- Low trade frequency increases statistical uncertainty and winner concentration risk.
- No independent reproduction.
- No separately documented OOS/walk-forward result reviewed.
- Funding, spread, slippage, market impact and liquidation are absent from the headline evidence.
- Optional on-chain inputs introduce vendor availability and point-in-time alignment risk if enabled.

## Implementation status

`not-implemented` in our research stack. This Scout cycle did not run a backtest, port Pine code, modify the quantitative runtime, or create implementation/Paper/Testnet/Live tasks.

## Adoption boundary

`research-only` / `not-implemented` / `not-approved` / `approval_scope: research-only`.

This record is a source-traceable research capture only. It is not evidence that the strategy is profitable in our environment and does not authorize implementation, Paper, Testnet or Live execution.

## Related Wiki records

No exact duplicate of TradingView source `T3t4yoJx` was found in the staging repository during the pre-write search.

Materially adjacent records reviewed for dedup/incremental value include:

- `btc-30m-wyckoff-squeeze-multilayer-trend-momentum-2026-09-14.md` — also uses volatility compression and trend/momentum confirmation, but differs materially through this source's explicit volume-spike breakout, daily regime gates, locked adaptive exit regime and stagnation exit.
- `bitget-perpetual-shuffled-null-falsification-cross-sectional-momentum-2026-09-13.md` — contains negative evidence that simple single-asset Donchian/EMA/z-score technical strategies can fail shuffled-null controls; useful competing evidence for any breakout claim.
- `crypto-perpetual-supertrend-wpr-trend-following-cost-gate-falsification-2026-09-12.md` — documents cost and multiple-testing failure modes for crypto trend-following indicator stacks.

No stable Hermes Wiki Brain path for these staging records was fabricated.

## Sources

- TradingView, `ETH Momentum Breakout Strategy [geektrade.online]`, author `grinaypps`, public open-source strategy page, published 2026-03-03, accessed/as-of 2026-09-14: https://www.tradingview.com/script/T3t4yoJx-ETH-Momentum-Breakout-Strategy-geektrade-online/
