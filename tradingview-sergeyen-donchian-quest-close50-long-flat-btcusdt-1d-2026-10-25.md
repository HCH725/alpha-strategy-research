---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "sergeyen Donchian Quest close-price 50/50 breakout — independent BTC-USDT spot daily long-flat derivative"
created: 2026-10-25
updated: 2026-10-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
  - donchian
status: research-only
confidence: medium
source_as_of: 2024-07-14
sources:
  - https://www.tradingview.com/script/YPQwKNF8-Donchian-Quest-Research/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Donchian Quest 50/50 close-price channel — independent daily spot long-flat derivative

## Provenance

- **Primary source:** TradingView, sergeyen, **Donchian Quest Research**, stable script ID **YPQwKNF8**, first published **2023-12-06**, last public release notes **2024-07-14**; source page directly read **2026-10-25**: https://www.tradingview.com/script/YPQwKNF8-Donchian-Quest-Research/
- **Source-native, publicly verifiable concept:** Two Donchian-like channels are calculated from **closing prices rather than highs/lows**. The source describes opening long when the latest close equals the maximum of the channel's closes, closing long at the minimum, and symmetric short/reversal rules. Its documented default opening/closing channel pair is **50/50**, with daily charts recommended. The page additionally describes ATR(20)-based equity-risk sizing, optional stops and breakeven/trailing variants, optional additional orders, both sides by default, and native 0.055%-per-side commission / zero slippage assumptions. Source text is sufficient to identify this close-price-channel *mechanism*; the full Pine program was not available in the inspected page text, so **no claim of a byte-for-byte, source-native or lossless Pine reconstruction** is made.
- **Explicit independent derivative:** The researcher freezes **BTC-USDT Binance spot 1d UTC**, LONG/FLAT only; uses strictly **greater-than prior 50 closes** for entry and strictly **less-than prior 50 closes** for exit (not the source's inclusive-current-bar equality wording); disables shorts, reversals, ATR/equity sizing, native stop variants, additional orders, and end-window closure; fixes one 0.001 BTC unit, 10000 USDT initial cash, a 60-completed-bar warmup, full-bar continuity checks, completed-close decisions, synthetic same-processed-row MARKET-close fills, and an assumed 0.1% fee per fill. All such timing, sizing, economic, tie and state choices are **researcher-designed and can change original trade events**. They are **not** attributed to sergeyen.
- **Immutable derivative identity:** TV:YPQwKNF8 | sergeyen:2024-07-14 | independent-derived-v1-close-only-prior50-maxmin-strict-longflat | BinanceSpot:BTC-USDT:1d:0.001BTC:MARKET-close | 2026-10-25. Changing channel input, length, strictness, side, fill timing, sizing or risk is a new research identity.

## Economic mechanism

A closing-price breakout above the preceding 50 daily closes is treated as a trend-continuation entry. The first closing-price breakdown below the preceding 50 daily closes ends the long. Unlike high/low Donchian channels, intrabar wick extremes do not set channel thresholds. This is a **hypothesis**, not a demonstrated edge or performance claim. There are no source statistics independently reproduced here.

## Signal

**Frozen data and formulas** (zero-based complete UTC daily candles, t is the most recent *completed* candle):

~~~text
N = 50
upper_t = max(close[t-50], ..., close[t-1])
lower_t = min(close[t-50], ..., close[t-1])
ready_t = (t >= 60) and contiguous_valid_complete_prefix
enter_t = ready_t and (close[t] > upper_t)
exit_t  = ready_t and (close[t] < lower_t)
~~~

- Only the 50 **previous** closes define either band. No current-bar high/low, volume, RSI, ATR, smoothing, interpolation, fitted model or future print is used by the signals. The source's default 50/50 length and close-price-only idea are retained; the prior-bar exclusion and strict inequalities are **derived choices**.
- Equality with either threshold is a **hold/no-action**. Missing, zero, negative, NaN, infinite, duplicate, out-of-order, gapped or incomplete candles fail the research run before signal evaluation; no gap fill, fabricated price or silent bar drop is permitted. For each daily UTC candle, OHLC must be finite and internally valid; only close and timestamp gate orders. A missing source interval does not become a compressed rolling window.
- Flat + enter_t: submit one BUY; Long + exit_t: submit one SELL for the exact held base quantity. Long + enter_t and Flat + exit_t are no-ops. The entry and exit predicates cannot co-occur: upper_t >= lower_t on any valid 50-close history, while strict close > upper and close < lower are mutually exclusive.
- There is **no** short signal, stop-loss, take-profit, trailing stop, breakeven, timeout, volatility filter, session restriction, time-window liquidation, margin liquidation, profit-triggered additional order, or other hidden exit. The 50-close lower-channel exit is the **only** closing rule. This can allow severe drawdowns.
- Position state is FLAT or LONG(0.001 BTC); maximum one position and one order per decision bar, no pyramiding, DCA, SO, rebalancing, compounding, concurrent symbols, or pending limit orders. No cooldown. After a completed exit, re-entry is permitted only on a **later** completed bar with a fresh enter_t condition. On unaffordable entry, remain flat; a later qualifying breakout may retry. End of data preserves the last open position without a fabricated closing fill.

## Required data

- Exactly one **Binance spot BTC-USDT** 1d UTC OHLCV series with original Binance candle-open timestamps and 86400-second cadence. Signals consume **close** only; open/high/low are validated for candle integrity, volume is feed metadata only. No funding, mark/index price, order book, non-OHLCV data, additional market, multi-timeframe alignment or external session calendar is needed.
- Warmup: 60 **complete contiguous** bars (indexes 0 through 59) must pass before the first eligible decision at index 60. The 50 prior closes are therefore already known; no warmup trade or warmup fill is allowed. The first eligible decision time is UTC opening timestamp of bar 60 **plus 86400 seconds**, never its opening timestamp.
- The source TradingView chart, any author's historical performance, and actual live-exchange price/fee/precision are **not** imported as verified backtest evidence.

## Execution assumptions — bounded pinned Hummingbot model

- **Exact engine pin:** Hummingbot distribution package **20260920**, VERSION **dev-2.17.0**, source **HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3**. The 902/902 wheel-to-commit Python-byte equivalence and package metadata were previously independently evidenced in accepted alpha research **PR #414** (2026-10-24); this Scout **did not independently rehash the wheel**. The pinned source's VERSION file was read this cycle; its setup.py static version label 20260729 is not treated as the distribution's wheel version.
- **Feed compatibility actually inspected at the pinned commit:** BinanceSpotCandles constants.py supports interval 1d; binance_spot_candles.py::_parse_rest_candles reads row[0] as opening timestamp and row[1..5] as OHLCV. BacktestingEngineBase.prepare_market_data exposes close_bt/close and timestamp_bt/timestamp. Its dropna() does **not** establish continuity, so the strict preflight above is necessary; only complete bar closes are decision inputs.
- **Controller/executor compatibility actually inspected:** BacktestingEngineBase.simulate_execution iterates processed rows, invokes update_state then controller.determine_executor_actions, and simulates CreateExecutorAction. OrderExecutorConfig supports connector_name=binance, trading_pair=BTC-USDT, side BUY/SELL, amount Decimal(0.001), execution_strategy MARKET, price=None, leverage=1. OrderExecutorSimulator.simulate on MARKET uses the **first supplied row's close**, creates a full-quantity POSITION_HOLD fill, records filled_amount_quote=amount*close and cum_fees_quote=trade_cost*filled_amount_quote. This is a **synthetic same-row close model** (effective economic timestamp = Binance opening label + 86400 seconds), **not** a guarantee that a live post-close MARKET order fills at that historical close.
- **Position and ledger:** BacktestPositionHold._process_order in backtesting_engine_base.py nets opposite-side base quantities, computes gross realized quote PnL and separately accumulates executor fees. A dedicated derived controller (not yet implemented) must retain its own confirmed-fill FLAT/LONG state and executor IDs, rather than infer position from a potentially lagged/pruned view of terminated executors. BUY/SELL action quantity is exactly 0.001 BTC; the second leg closes, never reverses or shorts.
- **Research-only cash and costs:** starting unborrowed cash 10000 USDT; a synthetic MARKET BUY is permitted only if cash >= 0.001*close_t*(1+0.001). BUY cash debit = 0.001*close_t*(1+0.001); SELL cash credit = 0.001*close_t*(1-0.001). Pass **trade_cost=0.001 per side** to the engine and keep the ledger's gross realized PnL and fee total separate: net closed-trade PnL = 0.001*(sell_close-buy_close) - 0.001*0.001*(sell_close+buy_close). This is a **fixed declared hypothetical research fee**, not actual exchange fees. The engine's MARKET close-price fills imply **zero additional modeled slippage** for this bounded simulation; they do not establish real zero slippage. No leverage/margin, borrowing or futures funding: **spot funding is not applicable**, not assumed-zero perpetual funding.
- **Model boundaries:** real venue tick/lot limits, fee tiers, spread, latency, depth, partial fills, production precision and live order rejection are **not validated**. The source's ATR-risk equity sizing, optional stops and add-on orders are **not modeled**. No real-money economics, execution deployment, Qlib parity, HB Certified or live readiness is asserted. This reuses an existing inspected spot 1d MARKET/hold capability; it introduces no new execution primitive.

## HB_READY six-gate evidence — Scout proposal, not independent verdict

1. **Determinism:** close-only prior-50 max/min with exact strict comparisons, frozen 50/50 inputs, no smoothing/ML, 60-bar warmup and invalid-data fail-closed rules.
2. **Direction:** Binance spot BTC-USDT LONG/FLAT; original short/reversal side explicitly disabled as a derived change.
3. **Entries/exits/risk:** precise prior-close breakout/breakdown, sole exit, no stops/targets/trailing/time exits or implicit defaults.
4. **State:** exactly one 0.001 BTC unit, affordability check, fill-confirmed FLAT/LONG controller memory, no SO/DCA/pyramiding/concurrency/cooldown; later-bar re-entry and terminal open-position handling pinned.
5. **Pinned Hummingbot path:** specific package/VERSION/commit, inspected 1d Binance candle feed, real MARKET executor close-fill/fee and BacktestPositionHold netting paths; explicit spot cash, cost, clock and real-execution limits. Prior PR #414 supplies package-to-commit distribution binding, not a claim of a new wheel rehash.
6. **Point-in-time:** previous 50 **completed** closes only, contiguous 60-bar warmup, opening-label + 86400s effective decision/fill clock, no future extrema, same-bar synthetic model explicitly disclosed.

**PASS here is a proposed six-gate research-expressibility assessment subject to independent Hermes Auditor exact-head review.** It is not profitability, historical survivor status, Qlib parity or authorization for Paper/Testnet/Live.

## Evidence

### Source-reported
- TradingView source description/release notes (as of 2024-07-14) identify 50/50 closing-price channel, symmetric long/short rules, optional risk/stop/add-on mechanics, and daily-chart recommendation. The full Pine code was not retrieved; native order precedence, current default add-on settings and exact Pine equality/fill details are **not** asserted.

### Independently inspected
- 2026-10-25 GitHub connector read of HCH725/hummingbot pinned commit: Binance spot 1d constants, REST timestamp/OHLCV parser, BacktestingEngineBase controller loop and candle mapping, OrderExecutorConfig MARKET, OrderExecutorSimulator MARKET fill/fees, BacktestPositionHold netting and Hummingbot VERSION. No local shell, Qlib/Hummingbot backtest or new primitive test was executed.
- Prior independent package/source equivalence is cited to merged alpha PR #414; **not** freshly reproduced this cycle.

### Negative evidence / dedup
- At pre-write main SHA **e56569b692053d5fce649efa84061b17db7cb941**, root-level strategy records **327**, README pool count **327**. Equality is **not** a claim of independently re-verifying every existing record's PASS frontmatter.
- GitHub code search on main found no script ID YPQwKNF8 or sergeyen; open research PR search found no same source. Existing Donchian-20/10, naked-20, Eterna-20 and regime-55/20 records use **high/low** bands and different triggers/exits; this independent **close-price-only 50/50** mechanism is materially distinct, not a trivial parameter variant.

## Falsification plan

Before any downstream screening, verify 50/50 close-only signals against an independently implemented causal reference on a complete daily tape, test equal-to-band ties, one-bar gap rejection, first eligible bar, immediate post-exit re-entry and fee-inclusive cash exhaustion. If selected for Qlib research, require a reproducible strategy-specific executable handoff and representative Qlib/Hummingbot event-level parity for any previously unverified execution path; do not claim parity or backtest results now.

## Crypto portability

Single-symbol spot long-only with 24/7 UTC daily bars; no futures leverage/funding or market-wide capital sharing. Other symbols/timeframes require an explicitly new frozen research configuration and validated data path; the 50/50 mechanism itself does not imply profitability.

## Limitations

Full original Pine unavailable; all deviations and disabled source-native features are disclosed. Synthetic same-close fills, assumed fees, absent real slippage and production precision make this a **bounded research execution model**, not a real fill simulation. Long-only without stop loss can suffer large drawdowns. No strategy-specific backtest, Qlib/Hummingbot parity, survivor result, or performance statistic is claimed.

## Implementation status

**not-implemented**: no dedicated Hummingbot controller or Qlib recipe was created. This is not a second admission gate; if later selected, use the existing IMPLEMENTATION_NEEDED route rather than modifying HB_READY status.

## Adoption boundary

**research-only / not-approved / approval_scope: research-only**. No trading, Paper/Testnet/Live, deployment, cron or workflow changes authorized.

## Related Wiki records

None added or modified in this Scout cycle.

## Sources

- https://www.tradingview.com/script/YPQwKNF8-Donchian-Quest-Research/
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- https://github.com/HCH725/alpha-strategy-research/pull/414
