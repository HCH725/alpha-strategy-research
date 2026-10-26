---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TradingView Channel Reversion System Donchian50 lower-quartile SMA200 ATR14 long-flat — independent BTC-USDT spot 1d derivative
created: 2026-10-26
updated: 2026-10-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-08-19
sources:
  - https://www.tradingview.com/script/XRZCjbFr-Channel-Reversion-System/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Channel Reversion System: Donchian lower-quartile entry, midline/ATR/regime exit — independently derived BTC-USDT spot strategy

## Provenance

**TradingView primary source:** *Channel Reversion System* (CRS), author **mateosandoval1025**, public script identity **XRZCjbFr**, published **2026-08-19**; canonical first-party page https://www.tradingview.com/script/XRZCjbFr-Channel-Reversion-System/ (read 2026-10-26). TradingView labels it an **open-source strategy**, but the full Pine code was **not retrieved**; the author's publicly readable description is the source of verified facts below. No immutable Pine revision hash, exact original order-emission behavior or original intrabar-fill parity is claimed.

**Source-native facts verified from author prose:** prior-bar high/low **50-day Donchian channel**; lower **25%** accumulation zone; price above **SMA200** required for long entry; close below SMA200 forces regime exit; target at channel midpoint; protective stop **one ATR14 below channel floor**; author's sample market **QQQ/SPY daily ETFs**, with **$10,000** initial cash, **0.05% commission per side**, **1 tick slippage**, and close fills. Author provides in-sample ETF performance claims, not independently reproduced here.

**Independent derivative, NOT a lossless Pine port:** This record ports the idea to **Binance BTC-USDT spot UTC daily candles**; fixes all arithmetic and boundary conventions, an entry *cross into* the prior-bar lower-quartile zone, dynamic channel-based exit levels, a close-triggered (not intrabar stop-order) risk exit, close-only profit-taking, a 250-bar warmup, single 0.001 BTC full-fill state, zero modeled slippage instead of the author's 1-tick setting, and an explicitly declared Hummingbot historical MARKET-close execution/cash model. The precise choices are researcher-defined, not attributed to the author. Material changes in signal, entry crossing, stop behavior, market, clock, size, costs or engine form a **different derivative**.

**Frozen research identity:** TradingView:XRZCjbFr:mateosandoval1025:2026-08-19 | independent-derived-v1:2026-10-26 | Binance BTC-USDT spot UTC 1d | prior-50 Donchian lower-quartile entry cross / close>SMA200 | dynamic midline/ATR14-below-floor/SMA200 close exits | 250 valid bars | 0.001 BTC | Hummingbot package 20260920 VERSION dev-2.17.0 | idealized MARKET-close model.

**Dedup at main facf215583cbbe98ac915052f476ec2dcc146157:** GitHub connected-code search for source ID XRZCjbFr and PR search across open/all PRs found no existing record. Current main root filenames and open research/* PR titles/bodies were checked. Closest families differ materially: tradeviZion lower-*candle*-20%/SMA5/100 mean reversion has no prior-50 Donchian structural support or ATR-floor risk exit; Donchian breakout and Donchian midline state strategies use breakout/crossing mechanisms rather than lower-quartile accumulation inside SMA200 regime. This is not merely a threshold or timeframe variant.

## Economic mechanism

### Source-reported

The author proposes buying near the bottom quarter of a trailing 50-day range **within** a positive 200-day moving-average regime, seeking mean reversion to the range midpoint while limiting downside below structural support. This is a hypothesis and author-reported design, not independently established profitability. The author's reported QQQ/SPY backtest returns, win rates and drawdowns are **not** imported as this BTC derivative's evidence.

### Research interpretation

The derivative requires a fresh close crossing *into* the prior-50 range's bottom quarter, rather than buying every candle already within it. It uses **close-confirmed** exits at a moving midline, moving ATR-offset floor, or failed SMA200 regime. Consequently a large intrabar drop can exceed the nominal stop before the next completed close; this is **not** a protective intrabar stop order.

## Signal

**Market/feed:** Binance spot BTC-USDT, exactly one stream of completed, UTC-aligned 1d OHLCV bars. Let t be the zero-based bar index and T[t] its UTC opening epoch. Accept only finite strictly positive O/H/L/C, high >= max(open,close), low <= min(open,close), finite nonnegative volume, strictly increasing timestamps separated by exactly 86,400 seconds. Missing, duplicated, noncontiguous or invalid bars cause the research run to **abort**, even while holding, rather than fill forward, silently drop bars or fabricate prices.

**Prior-bar Donchian (not current-bar self-reference):** for t >= 50, H50[t] = max(high[t-50],...,high[t-1]); L50[t] = min(low[t-50],...,low[t-1]); W50[t] = H50[t]-L50[t]; Q25[t] = L50[t]+0.25*W50[t]; MID[t] = L50[t]+0.50*W50[t]. If W50[t] <= 0, both entry and channel-target/stop predicates are suppressed and a held position can still exit on SMA200 failure; no division by zero.

**Trend:** SMA200[t] is arithmetic mean of close[t-199..t], defined only from t>=199. Strict trend gate: close[t] > SMA200[t]; equality is not bullish. Regime exit is close[t] < SMA200[t] (strict); equality alone is not an exit.

**ATR14:** TR[0]=high[0]-low[0]. For t>=1, TR[t]=max(high[t]-low[t],abs(high[t]-close[t-1]),abs(low[t]-close[t-1])). ATR14[13]=mean(TR[0..13]); for t>=14, ATR14[t]=(13*ATR14[t-1]+TR[t])/14 (Wilder/RMA, arithmetic seed). Only completed observed OHLC data enter this recursion; no rolling-window lookahead.

**Entry:** At eligible completed bar t, only if FLAT, W50[t]>0, close[t]>SMA200[t], close[t-1]>Q25[t-1], and close[t]<=Q25[t], emit one BUY. The prior-bar upper-side strict comparison and current lower-side inclusive comparison define a crossing *into* the zone. Prior Q25 must be valid. A close already inside the zone without a fresh crossing does not repeatedly enter; if a signal is missed because of no cash, a later new crossing is required. This crossing interpretation is **researcher-defined**, not claimed to be the original Pine predicate.

**Exit, LONG only, single action per bar in this priority:** (1) REGIME when close[t]<SMA200[t]; else (2) STOP when W50[t]>0 and close[t]<=L50[t]-ATR14[t]; else (3) TARGET when W50[t]>0 and close[t]>=MID[t]; otherwise HOLD. All are evaluated on the **current completed close**, with prior-50 range and ATR recomputed each day. Dynamic moving levels, the equality boundaries and the regime>stop>target priority are researcher-defined. The author's phrase "hard stop" must NOT be interpreted as an intrabar order in this derivative.

**Warmup:** require 250 **consecutive valid completed** daily bars (first eligible t=249), exceeding SMA200, Donchian prior-50/current-and-previous and Wilder ATR14 initialization. Ignore earlier signals and initialize FLAT; never retroactively execute a pre-warmup entry.

**State:** FLAT -> PENDING_BUY -> LONG only after a confirmed full MARKET fill; LONG -> PENDING_SELL -> FLAT only after a confirmed full SELL fill. No new action while pending. Exactly 0.001 BTC bought/sold per position, one position, no concurrent orders/markets, no pyramiding, no safety orders, no BO/SO/DCA, no compounding, no partial fill in the chosen historical simulator. On BUY, require available modeled cash >= 0.001*observed_close*(1+0.0005); if insufficient, remain FLAT and wait for a **fresh** entry cross. A failed SELL or missing actual price is a run-stopping model failure, not a fabricated fill. Re-entry is permitted from the next later qualifying completed bar, with no cooldown; never exit and re-enter on the same bar.

**Explicitly disabled:** SHORT, margin, leverage, perpetuals/funding, multi-asset capital, limit/maker/next-open/intrabar execution, intrabar stop, fixed entry-price bracket, trailing, partial exits, discretionary exits, independent time stop, terminal forced liquidation, and any additional oscillator/volume gates. If still LONG at sample end, retain 0.001 BTC and mark it to the final **observed** valid close; do not manufacture a SELL.

## Required data

One native Binance BTC-USDT **spot 1d** OHLCV feed; derived previous-50 Donchian, close SMA200 and Wilder ATR14 only. No extra markets, cross-timeframe sync, order-book, ML, fundamental, futures funding or assumed synthetic candles. Raw Binance kline row[0] is **opening** timestamp, not the time at which row[4] close was knowable.

## Execution assumptions

**Pinned source examined through GitHub connector 2026-10-26:** HCH725/hummingbot commit **8b0e067e80ab62f10846d518dcb5a8218527ddb3**, hummingbot/VERSION **dev-2.17.0**, policy package label **20260920**. Package label, VERSION and source commit are different identifiers; no wheel/image digest is independently revalidated in this Scout. Earlier independent representative engine-path review **Alpha PR #421** is supporting evidence, not a substitute for an actual deployed package digest or candidate backtest.

**Actual data path:** BinanceSpotCandles in hummingbot/data_feed/candles_feed/binance_spot_candles/{constants.py,binance_spot_candles.py} supports interval 1d and /api/v3/klines, parsing row[0] as opening timestamp and rows[1..5] as OHLCV. Validate all candles and availability **before** feature merge; BacktestingEngineBase.prepare_market_data uses backward merge_asof/dropna and does not itself guarantee that a feature based on the day's final close is available at the day's opening timestamp.

**Actual controller/executor path:** BacktestingEngineBase.simulate_execution calls update_state -> controller.determine_executor_actions -> CreateExecutorAction -> OrderExecutorConfig -> OrderExecutorSimulator. Required config: connector_name=binance, trading_pair=BTC-USDT, side BUY/SELL, amount Decimal("0.001"), position_action OPEN/CLOSE, execution_strategy MARKET, price None, leverage 1. The pinned OrderExecutorSimulator MARKET branch uses the first supplied historical row's **observed close** as a **full fill**, sets filled_amount_quote=amount*close, cum_fees_quote=trade_cost*filled_amount_quote, and CloseType.POSITION_HOLD. A future strategy-specific controller would implement the specified rules; no controller or backtest is claimed to have been built/run this cycle.

**Causality/effective time:** for UTC daily candle with raw T[t], all signals are available **no earlier than T[t]+86400**. A model-consistent implementation must prevent pre-close action and report the decision, idealized close fill and ledger as **close-effective T[t]+86400**; native open-labeled timestamps and backward merge_asof are not sufficient by themselves. This is the already-used completed-bar MARKET-close **historical simulator convention**, not a physically achievable guaranteed fill placed after observing the close. If the pinned implementation cannot enforce completed-bar availability and effective timestamps, Gate 5/6 fails and the independent Auditor must reject.

**Position and costs:** BacktestPositionHold in backtesting_engine_base.py nets BUY/SELL base quantities, tracks weighted average entry and **gross** realized PnL, with cumulative fees recorded **separately**. Fix research trade_cost=0.0005 (0.05% **per filled side**, matching the author's stated rate as a hypothetical simulation input); cash starts at 10,000 USDT, no borrowing. BUY cash delta = -Q*close*(1+0.0005); SELL cash delta = +Q*close*(1-0.0005); realized net = Q*(sell_close-buy_close)-both-side fees. Unclosed equity = cash+Q*last_observed_close. Do not treat a gross native PnL field as fee-net equity; reconstruct the fill ledger. **One-tick slippage from the author's ETF setup is NOT modeled** by this MARKET simulator: the derivative intentionally assumes no **additional modeled slippage**, not real-world zero slippage. Spot funding is **inapplicable**, not an invented realized funding series. Real exchange fees, tick sizes, min-notional, rounding, latency, spreads, partial fills and market impact are unverified and are not certified by PASS. Never accept BacktestingDataProvider.get_price_by_type's fallback Decimal("1") as a valid missing price; fail closed. Use fill-confirmed state/position holds rather than assuming order creation equals a fill; controller history may require terminated_executors_window=None to retain relevant fills.

## Evidence

### Source-reported

First-party TradingView author page, 2026-08-19, documents the 50-day prior-bar channel, lower-quarter location, SMA200 filter, midpoint target, ATR14 below-floor stop, ETF/daily scope and hypothetical backtest setup. Source's ETF returns are **author-reported only** and not independently reproduced.

### Independently reproduced

**Not independently reproduced.** No Pine-code parity, strategy backtest, Qlib/Hummingbot event-level parity, performance, real fills, fees or funding series were executed or independently reproduced in this Scout. Pinned engine source-path inspection and previous representative path evidence support only **bounded historical model expressibility**, not trading authorization.

### Negative evidence

The full Pine source tab was not retrieved, so original precise crossing, stop-order timing, moving-versus-frozen stop and fill details are **not** asserted. This record is intentionally an independently defined derivative. No source performance numbers are transferred. Existing channel-breakout records, candle-range lower-20% reversion and EMA cross records have materially different entry/risk mechanisms. No matching TradingView XRZCjbFr source identity was found in main or open research PRs. A source-native claim would be unjustified.

## Falsification plan

Before any mass Qlib screening on a **new** execution primitive, independently exercise one representative pinned Hummingbot historical daily spot controller/event path, comparing exact entry cross, priority exit, 250-bar warmup, effective close timestamps, BUY/SELL fill quantities and fees against a deterministic fixture. Then validate Qlib/Hummingbot **representative event-level parity** for the execution path. Do not promote performance or survivor claims from this record. Test equality boundaries, dynamic stop movement, data gaps, flat-to-long-to-flat state, cash insufficiency and end-of-sample open inventory.

## Crypto portability

This is a declared **BTC-USDT spot daily** derivative, not evidence the author's QQQ/SPY ETF edge survives on crypto. Later seven-coin, 1h/4h/1d and BO/SO experiments are optional downstream **separately declared derivatives** when they alter signals, sizing or events, not admission requirements. No futures funding, leverage or perpetual accounting is validated here.

## Limitations

No original Pine bytes, exact source-native order equivalence, live tradeability, liquidity/minimum-notional proof, realized fee/slippage, candidate-specific Hummingbot execution, Qlib parity, out-of-sample testing, profit claim or strategy certification. The close-based stop is materially different from an intrabar hard stop; gaps and overnight moves can cause worse outcomes. Package-to-source digest remains a separate independent-review concern. No new engine capability is inferred from an API name.

## Implementation status

**not-implemented**: this Markdown defines a six-gate proposed model-compatible research strategy; it is not an executable Qlib or Hummingbot controller. Any downstream implementation must follow the existing implementation-needed path, not create a second HB_READY eligibility flag.

## Adoption boundary

**research-only / not-approved**. HB_READY PASS is a **proposal for independent exact-head Hermes Auditor verification** before main admission, not approval to merge, Qlib profitability screening without the required execution-path evidence, Paper/Testnet/Live trading or capital allocation. Scout does not approve, merge or edit README; the existing signed webhook receiver owns post-merge count bookkeeping.

## Related Wiki records

None asserted. No private Wiki, credentials or user data copied into this public record.

## Sources

- Primary public TradingView page: https://www.tradingview.com/script/XRZCjbFr-Channel-Reversion-System/ — mateosandoval1025, 2026-08-19.
- Pinned Hummingbot source reference: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — relevant VERSION, BinanceSpotCandles, BacktestingEngineBase, OrderExecutorSimulator, OrderExecutorConfig and BacktestingDataProvider files inspected via connected GitHub.
- Repository policy: README.md and .github/HB_READY_REVIEW.md on main SHA facf215583cbbe98ac915052f476ec2dcc146157.
