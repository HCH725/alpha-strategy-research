---
schema: strategy-research-record-v1
title: "TradingView Multi-Band Crypto Strategy Source-Code Audit: Rolling Close-Quantile Minus Price-Stdev Threshold"
created: 2026-09-14
updated: 2026-09-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
  - crypto
  - quantile
  - source-code-audit
status: research-only
confidence: medium
source_as_of: 2026-09-14
sources:
  - "https://www.tradingview.com/script/bq0ELG1b-Multi-Band-Comparison-Strategy-CRYPTO/"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The publication describes Bollinger, quantile, and Power-Law band confluence, but the current Pine order logic uses only close relative to the lower standard-deviation line of the upper close-quantile band."
  - "The publication's January 2025 release notes describe a $1,000 initial account plus explicit commission, slippage, bar-magnifier, no-pyramiding, and margin settings; the current visible Pine strategy declaration sets $5,000 initial capital and does not include those claimed execution-cost/backtest settings."
  - "The source labels a rolling return-percentile projection as a Power-Law Band; the current Pine code does not fit a time-based power law, and this plotted band does not enter the order rule."
---

# TradingView Multi-Band Crypto Strategy Source-Code Audit: Rolling Close-Quantile Minus Price-Stdev Threshold

## Provenance

- **Primary source:** TradingView public open-source script, `Multi-Band Comparison Strategy (CRYPTO)`, by `garysebastianbrowniii`: https://www.tradingview.com/script/bq0ELG1b-Multi-Band-Comparison-Strategy-CRYPTO/
- **Publication identity:** public TradingView script ID `bq0ELG1b`; page shows initial publication on 2025-01-17 and updates through 2025-01-21.
- **Source inspected directly:** both the public description/release notes and the current 181-line Pine Script v6 source shown in TradingView's `Source code` tab were read on 2026-09-14.
- **Deduplication:** repository and Hermes Wiki Brain searches found no record containing `bq0ELG1b`, `Multi-Band Comparison Strategy`, or the exact `quant_upper_std_down` construction. Related quantile/funding records use materially different data and mechanisms.
- **Incremental value:** this record is primarily a source-code contradiction audit. It preserves a materially different conclusion from the publication narrative: the actual order rule is a single rolling close-quantile/stdev threshold, while Bollinger, so-called Power-Law, SMA, and EMA components are plotting/context features rather than order conditions.

## Economic mechanism

### Source-reported

The author describes the strategy as a crypto-oriented statistical-band framework combining Bollinger Bands, rolling quantile bands, a so-called Power-Law Band, and a standard-deviation trigger. The stated rationale is that crypto volatility creates recurring statistical extremes; requiring price to remain above or below the trigger for a configurable number of bars is intended to reduce noisy false breaks.

### Research interpretation

The current Pine source does **not** implement a multi-band confluence entry. The economically testable hypothesis is narrower: persistent closes above an adaptive threshold derived from the upper empirical quantile of recent price levels minus recent price-level standard deviation identify a bullish continuation state; falling back below that threshold terminates the state.

This is best interpreted as a **rolling distributional trend-state filter**, not as independent confirmation from Bollinger and Power-Law components. The purported Power-Law component is a rolling return-percentile projection and does not enter the order condition.

## Signal

### Current Pine rule reconstructed from source

- **Pine version:** v6.
- **Default lookback:** `length = 20` bars.
- **Upper quantile:** `0.95`.
- **Lower quantile:** `0.05` (calculated/plotted but not used in orders).
- **Rolling price sample:** a persistent array retains the most recent `length` close prices, including the current bar after the array update.
- **Percentile implementation:** copy the array, sort ascending, select the element at `round((N - 1) * quantile)`.
- **Price standard deviation:** `ta.stdev(close, length)`.
- **Trading threshold:**

  `trigger_t = rolling_95th_percentile(close, 20) - stdev(close, 20)`

- **Bullish state:** `close_t > trigger_t`.
- **Entry confirmation:** bullish state must persist for `entry_confirmBars` consecutive bars; default `1`.
- **Long entry:** if the entry counter is at least the confirmation setting and `strategy.position_size <= 0`, submit `strategy.entry("Long", strategy.long)`.
- **Exit confirmation:** non-bullish state must persist for `exit_confirmBars` consecutive bars; default `1`.
- **Exit:** if the exit counter is at least the confirmation setting and a long position exists, submit `strategy.close("Long")`.
- **Direction:** long-only in the current source; there is no short-entry rule.
- **Position size:** current visible `strategy()` declaration uses `strategy.percent_of_equity` with `default_qty_value = 10`.
- **Current visible initial capital:** `$5,000` in the source declaration.
- **Holding period:** no fixed maximum; hold until the exit-state confirmation occurs.
- **Re-entry:** allowed after exit when the bullish-state counter again satisfies the entry confirmation condition.

### Components that do not enter current order logic

The source also calculates/plots Bollinger Bands, rolling close quantiles, rolling return-percentile projections labeled Power-Law Bands, SMA, and EMA. In the current code, none of Bollinger, Power-Law, SMA, or EMA values is referenced by `strategy.entry` / `strategy.close` conditions.

### Specification status

The **signal calculation is reconstructable from the current source**, but the historical performance configuration is `underspecified` / contested because the publication's execution-setting claims do not match the current visible `strategy()` declaration and the exact reported backtest timeframe is not named beyond “lower timeframe.”

## Required data

- **Instrument:** source-reported backtest is BTC/USD; exact venue/feed for the reported metrics is not stated in the release notes.
- **Market type:** not explicitly identified as spot vs. derivative for the reported backtest.
- **Timeframe:** source says a “lower timeframe (short-term trading)” but does not provide the exact interval for the reported metrics; `underspecified`.
- **Fields required by actual order rule:** close prices only.
- **Additional plotted fields:** close-derived returns, SMA, and stdev; no volume, funding, open interest, order book, or alternative data enters the current order rule.
- **Timestamp/session:** chart-native bar timestamps; 24/7 crypto session convention is not separately specified.
- **Point-in-time constraint:** the rolling arrays and current-bar close must only become actionable after the current bar is finalized; reproductions must not treat the current close as known before bar completion.
- **Missing data:** source does not specify stale/missing-bar handling; `underspecified`.

## Execution assumptions

### Source-reported publication claims

The January 2025 release notes describe a backtest configured with:

- `$1,000` initial capital;
- 10% of equity per trade;
- 20 ticks of slippage;
- 0.005% commission per trade;
- no pyramiding;
- 0% long/short margin / fully funded exposure;
- TradingView Bar Magnifier enabled.

### Current-source contradiction

The currently visible Pine `strategy()` declaration sets 10% of equity and `$5,000` initial capital but does not include the publication-claimed commission, slippage, Bar Magnifier, margin, or explicit pyramiding settings in that declaration. Therefore the current script and the reported historical metrics cannot be assumed to share the same execution configuration.

Signal-to-order timing is also `underspecified` for independent reproduction: the source code does not explicitly set `process_orders_on_close`; a replication must lock TradingView broker-emulator semantics/platform version rather than silently assuming same-close fills.

Spread, liquidity, market impact, venue-specific tick size, partial fills, funding, borrow, latency, and order failures are not specified.

## Evidence

### Source-reported

For a BTC/USD backtest described as trading from 2024-01-01 through 2025-01-18, with backtest data beginning 2023-12-31, the publication reports:

- net profit: `4.28%`;
- total trades: `1,129`;
- percent profitable: `25.51%`;
- profit factor: `1.138`;
- maximum drawdown: `1.77%`;
- average trade: `+0.04%`;
- average trade duration: `8 bars`.

The same publication describes 10% equity sizing, 20-tick slippage, 0.005% commission, no pyramiding, and Bar Magnifier for those results. These figures are **source-reported only** and are contested by the current-source configuration mismatch above.

The author also explicitly warns in the 2025-01-21 release notes that the displayed result is a single backtest and is not necessarily indicative of performance on every asset under the same conditions.

### Independently reproduced

not independently reproduced

### Negative evidence

- The current Pine order rule does not use most of the advertised multi-band components, weakening the claimed “confluence” mechanism.
- The publication's `$1,000` / commission / slippage / Bar Magnifier configuration does not match the current visible Pine declaration, making the reported metrics non-reproducible from the current source without identifying the exact historical script/configuration snapshot.
- The exact timeframe used for the reported BTC/USD results is omitted.
- The reported average trade of `+0.04%` is small relative to execution assumptions, so venue/tick-size/fee interpretation is material; no independent cost audit exists.
- There is no source-reported walk-forward, frozen out-of-sample period, multi-venue replication, or independent reproduction.
- The source's own warning says the single backtest may not generalize across assets.

## Falsification plan

1. **Source-parity reconstruction test**
   - **Data/sample:** BTC/USD data spanning 2023-12-31 through 2025-01-18; identify the exact venue and lower timeframe used by the publication before accepting a parity result.
   - **Method:** reproduce both the current Pine rule and the publication-claimed execution settings.
   - **Metrics:** trade count, profit factor, net return, and maximum drawdown.
   - **Decision rule:** `research-defined falsification threshold` — if no plausible source-consistent timeframe/feed reproduces all four headline metrics within ±5% relative error after the execution configuration is matched, reject the publication metrics as reproducible evidence for the current rule.
   - **Action:** retain only the code-derived hypothesis; discard the headline performance claim from any later validation prior.

2. **Component-ablation identity test**
   - **Data/sample:** same BTC/USD sample and exact source configuration.
   - **Method:** remove Bollinger, Power-Law, EMA, SMA, and non-trigger plots while preserving `quant_upper_std_down` and confirmation counters.
   - **Metric:** ordered entry/exit timestamp identity.
   - **Decision rule:** `research-defined falsification threshold` — if the cleaned rule does not produce 100% identical order timestamps to the current source, this audit's “single effective trigger” interpretation is false.
   - **Action:** re-audit hidden state/dependencies before further research.

3. **Frozen forward out-of-sample test**
   - **Data/sample:** same resolved BTC/USD venue/timeframe from 2025-01-19 through 2026-09-14, with no parameter retuning.
   - **Metrics:** net return after explicit costs and profit factor.
   - **Decision rule:** `research-defined falsification threshold` — reject the alpha hypothesis if net return is ≤0 or profit factor is ≤1.0.
   - **Action:** classify the historical result as sample-specific and do not promote implementation.

4. **Cost stress test**
   - **Data/sample:** frozen forward sample above.
   - **Method:** baseline explicit costs, then 2× commission and 2× slippage separately and jointly.
   - **Metric:** net profit factor.
   - **Decision rule:** `research-defined falsification threshold` — if PF ≤1.0 at baseline or under a modest 2× cost stress, reject practical tradability at that cost tier.
   - **Action:** no implementation advancement.

5. **Parameter-perturbation test**
   - **Data/sample:** frozen forward sample.
   - **Grid:** lookback `{15, 20, 25}` and upper quantile `{0.90, 0.95, 0.99}` without selecting on the test period.
   - **Metric:** after-cost net return and PF.
   - **Decision rule:** `research-defined falsification threshold` — if positive performance appears only at the exact published/default `(20, 0.95)` point while the majority of neighboring settings are non-positive, treat the effect as parameter-fragile.
   - **Action:** reject robustness and stop retuning on the same OOS sample.

6. **Placebo / temporal-dependence test**
   - **Data/sample:** frozen forward return series.
   - **Method:** construct phase-randomized or block-shuffled return paths that preserve broad volatility while destroying the original sequence, then rebuild synthetic price paths and apply the unchanged rule.
   - **Metric:** median placebo PF versus real-sample PF.
   - **Decision rule:** `research-defined falsification threshold` — if the median placebo PF reaches ≥80% of the real PF, reject the interpretation that temporal trend persistence rather than distributional/path artifacts drives the result.
   - **Action:** treat the rule as non-causal descriptive filtering rather than alpha.

## Crypto portability

`direct` for the source's intended crypto use, but only `unproven` across venues/assets beyond the reported BTC/USD case.

Crypto-specific risks include 24/7 candle-boundary dependence, venue-specific tick size (critical to the claimed 20-tick slippage), spot-versus-perpetual differences, perpetual funding, fragmented liquidity, spread/slippage variation across tokens, stablecoin quote effects, and materially different liquidity across BTC versus altcoins.

## Limitations

- `contested`: current source code and publication narrative/configuration materially disagree.
- `not independently reproduced`.
- `underspecified`: exact reported backtest timeframe and venue/feed are not stated.
- Historical TradingView script revisions are not preserved here as immutable source snapshots; this record audits the source visible on 2026-09-14.
- The source calls a rolling return-percentile projection a Power-Law Band, but the current code does not estimate a conventional power-law model.
- The publication provides only a single reported historical test and no frozen OOS or walk-forward evidence.
- Performance claims cannot be treated as evidence for the current source until configuration parity is established.

## Implementation status

`not-implemented`. No PyBroker/Nautilus/runtime implementation, independent backtest, paper trade, testnet, or live execution was performed by this Scout.

## Adoption boundary

This is a `research-only` source-code audit. It is not evidence of validated profitability and does not authorize implementation, Paper, Testnet, or Live trading. `adoption: not-approved`; `approval_scope: research-only`.

## Related Wiki records

No stable matching Hermes Wiki Brain record was found for TradingView script `bq0ELG1b` or the exact rolling close-quantile-minus-stdev trigger during the pre-write search. Related repository records exist for other quantile signals, but their mechanisms/data dependencies are materially different.

## Sources

1. TradingView, `Multi-Band Comparison Strategy (CRYPTO)`, author `garysebastianbrowniii`, public open-source script ID `bq0ELG1b`, publication/update history 2025-01-17 through 2025-01-21; description, release notes, and current Pine Script v6 source inspected directly on 2026-09-14: https://www.tradingview.com/script/bq0ELG1b-Multi-Band-Comparison-Strategy-CRYPTO/
