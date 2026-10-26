---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "LookIntoBitcoin Pi Cycle 111DMA/2x350DMA top-regime long-flat — independent BTC-USDT spot 1d derivative"
created: 2026-10-27
updated: 2026-10-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
  - derived
status: research-only
confidence: medium
source_as_of: 2024-07-17
sources:
  - https://www.tradingview.com/script/9FFFBAOa-LIB-Pi-Cycle-Top-Indicator/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# LookIntoBitcoin Pi Cycle 111DMA/2x350DMA top-regime long-flat — independent BTC-USDT spot 1d derivative

## Provenance

**Primary first-party TradingView source:** LookIntoBitcoin, *LIB: Pi Cycle Top Indicator*, stable script ID **9FFFBAOa**, page dated **2024-07-17**: https://www.tradingview.com/script/9FFFBAOa-LIB-Pi-Cycle-Top-Indicator/ . Public description page fetched and read directly **2026-10-27** (no login required; full description text visible). The author describes: the 111-day moving average (111DMA) and a multiple of the 350-day moving average (350DMA x 2); the multiple applies to the **price values** of the 350DMA, not the number of days; when the 111DMA moves up and **crosses** the 350DMA x 2 it has coincided with Bitcoin peaking; 350/111 = 3.153 ≈ Pi; and an overheated market where the 111DMA has reached 2x the 350DMA has historically been "a very good time to sell Bitcoin". The page carries open-source flags, but complete Pine bytes, Pine version, exact daily input convention (exchange Tract/session) and any alert/plot settings were **not retrieved**. Those unknowns are not attributed to the author.

**Originator lineage (corroborated secondary fact, not directly fetched):** the Pi Cycle Top construction is credited to Philip Swift (LookIntoBitcoin), April 2019. This lineage is reported consistently across independent secondary pages and is used here only for attribution, never as a substitute for the fetched TradingView description above.

**Independent derivative, NOT source-native or a Pine reconstruction.** The source publishes an overheated/top indicator with a sell indication, not a complete executable strategy (no entry rule, no sizing, no fill timing, no re-entry rule). The researcher separately fixes: Binance BTC-USDT **spot UTC 1d**, LONG/FLAT only; target position as a **pure function of the current bar's top regime** (LONG iff not-top, FLAT iff top); arithmetic SMA definitions with strict-inequality regime and equality convention; 350-bar warmup; same-completed-bar historical MARKET close-fill model; one fixed 0.001 BTC position; no SL/TP/trailing/DCA; 10,000 USDT starting modeled cash; and 0.1% hypothetical fee per filled side. Each is a researcher-authored decision, may define a trade-event set the source never specified, and is never described as an original indicator default.

**Immutable research identity:** TV:9FFFBAOa | LookIntoBitcoin | page:2024-07-17 | independent-derivative-v1:2026-10-27 | Binance:BTC-USDT:spot:UTC1d | SMA111 vs 2xSMA350 strict regime | LONG-iff-not-top/FLAT-iff-top | 0.001BTC | 350-bar warmup | historical-completed-close MARKET | fee=0.001 per side. Any change to a decision-critical element is a different revision, not a silent edit.

**Dedup, current main snapshot b89f23c2cbd64d78385b078b2d4420c734cc9f9c:** full-tree filename and content search found no `pi-cycle`, `picycle`, `111dma` or `350dma` strategy record on main; open `research/*` PR titles contain no Pi Cycle source (closest is #251, a Swift 2-year-MA multiplier **zone-state** strategy — a different construction: 2-year-MA bands versus this record's 111/350 cross regime). Closest main families are moving-average-regime records with different constructions: *mayer-multiple-below-2p4-regime-long-flat-btcusdt-1d-2026-10-16.md* (200DMA price-ratio regime — and that record itself explicitly names the 111/350 Pi pair as a **different, unpinned** indicator family); *golden-cross-sma-regime-gated-long-btcusdt-1h-2026-10-08.md* (short/fast SMA cross regime, different windows and no doubling multiple). This candidate's **SMA111 versus doubled-SMA350 strict cross-regime** with LONG-iff-not-top mapping produces a materially different entry-event set; not a mere rename, timeframe change or parameter tweak. Code search is not a proof of exhaustive absence of all paraphrases. Main tree had 375 root strategy Markdown records at snapshot; sample PASS frontmatter reads do not constitute a fresh audit of every existing record.

## Economic mechanism

### Source-reported

The author attempts to identify Bitcoin cycle tops by the moment the faster 111-day average crosses up through twice the slower 350-day average, arguing the market is then so overheated that selling has historically been advantageous. The author's sell indication and peak-coincidence claims are source description, **not** the executable strategy proposed below. No source backtest result is treated as independently reproduced.

### Research interpretation

This derivative tests whether holding spot BTC except during the precisely defined doubled-long-average top regime improves fee-net expectancy versus unconditional buy-and-hold at identical costs. Because 350-bar averages cross rarely, the strategy is buy-and-hold most of the time with infrequent multi-month FLAT spells; any edge comes solely from skipping the post-cross drawdown windows the source describes, at the cost of whipsaw exits when a cross resolves without a major top.

## Signal

All clauses below are the frozen, independent derivative specification; none is a claim about uninspected Pine internals.

1. **Data:** chronological completed Binance BTC-USDT spot UTC **1d** OHLCV candles indexed t=0,1,...; use close C[t] for indicators and simulated fills. Each bar has finite positive O/H/L/C with L<=min(O,C)<=max(O,C)<=H and finite nonnegative volume. Consecutive Binance open timestamps differ by exactly 86400 seconds; missing, duplicated, partial, zero-priced or invalid rows abort the segment before feature merge, with no forward-fill/interpolation/dropna gap concealment.
2. **Averages:** SMA_n[t] = arithmetic mean of C[t-n+1..t], first valid at index n-1. F[t] = SMA_111[t], valid from t=110. S[t] = 2 * SMA_350[t], where SMA_350 is the plain 350-bar mean of closes (valid from t=349) and the factor 2 multiplies the **average price value** — never a 700-bar average. All arithmetic chronological float64, no rounding of indicator values.
3. **Top regime (pure function, no latch):** top[t] iff F[t] > S[t], evaluated only when both F[t] and S[t] are valid. Equality (F[t] == S[t]) is **not** top. There is no episode flag, no consumed marker, no pending-order state and no cross-counting memory: the target position on bar t depends only on top[t].
4. **Transitions (diagnostic labels only):** crossUp[t] iff top[t] AND !top[t-1]; crossDn[t] iff !top[t] AND top[t-1]. These labels describe regime changes; they carry no independent memory and cannot contradict clause 3.
5. **Warmup:** bars t=0..349 are completed-data warmup, with FLAT initial state, no inferred pre-window inventory, no simulated orders. First eligible decision is t=350, requiring valid F/S pairs at both t and t-1.
6. **Target position:** on every eligible completed bar t, target[t] = FLAT if top[t], else LONG. Position management is a pure function of the current bar; re-entry needs no extra condition beyond clause 7.
7. **Entry:** on eligible completed bar t, if FLAT, no pending order, !top[t] AND cash sufficient for Q*C[t]*(1+f), issue one MARKET BUY of Q=Decimal("0.001") BTC. Full historical simulated fill at the observed completed close C[t]; never earlier than the close-availability instant E[t]. An entry rejected for cash/invalid price is skipped and never queued or fabricated. This fires on crossDn bars and on any later flat non-top bar identically — there is no episode that must be "fresh", so no pending-fill versus signal-state divergence of the kind that closed prior episode-latch research can arise.
8. **Exit:** if LONG from a **prior** bar and top[t], issue one MARKET SELL of the entire filled 0.001 BTC at the observed completed close C[t]. No RSI, stop-loss, take-profit, trailing, time limit, volatility cap, trend exit or short order is active. A long can remain underwater for years until a top-regime bar; that is an explicit risk, not an implicit stop.
9. **Priority and state:** exit first, entry second, but top[t] and !top[t] are mutually exclusive booleans, so both can never fire on the same bar; no same-bar round-trip by construction. Once SELL fully fills, state returns FLAT; a later !top bar may buy again with no cooldown and no stale-signal veto. A !top bar while LONG is a hold-no-op, a top bar while FLAT is a no-op, and neither is queued. At most one pending order, and because fills complete on the same bar they are issued, no order ever survives into the next bar's decision. An unresolved partial/rejected/ambiguous fill stops that research segment rather than assuming a fill, balance or subsequent position.
10. **End:** final open position is marked at the last actually observed completed close with unrealized PnL reported separately; no invented liquidation or future-bar fee. No lookahead, centered filters, repainting, intrabar high/low stop assumptions, negative shifts, future extrema, ML artifact, cross-market alignment or higher-timeframe candle dependencies.

**Direction/disabled behavior:** Binance unleveraged BTC-USDT spot LONG/FLAT only. Short/borrow/perpetual funding/margin/leverage, DCA/safety orders, pyramiding, averaging, scale-in/out, partial exits, simultaneous positions, multi-pair shared capital, maker queue, intrabar order execution, stops/targets, cooldown timers and discretionary re-entry are disabled. No hidden Hummingbot controller defaults are adopted.

**Cash/cost ledger:** begin with 10,000 USDT and zero BTC. On full BUY at observed price P debit Q*P*(1+f), on full SELL credit Q*P*(1-f), where Q=0.001 BTC and f=0.001 each side. Track full precision Decimal cash/quantity/fees, entry price, realized and unrealized gross PnL and separately fee-net PnL. A SELL never creates negative BTC. No reinvested/percentage-of-equity position sizing. Actual exchange tick/lot/min-notional validation is not claimed; reject unsupported precision or missing trading-rule data for any future executable path rather than silently rounding into a different order.

## Required data

Only the pinned Binance SpotCandles BTC-USDT **1d** historical OHLCV feed; close is a real observed value, never a default/placeholder. REST kline timestamp T[t] is **bar open**, not when the close was available. Define decision and historical simulated fill effective time E[t]=T[t]+86400 seconds after the full candle completes. Validate strictly monotone contiguous timestamps and exclude any incomplete final candle. Historical close fill at E[t] is a bounded research-model convention, **not** a claim a live order sent after E[t] could execute at C[t]. Controller/ledger event timestamps based on T[t] must be normalized to E[t] before event-level comparisons. Restarted segments reset FLAT and require fresh 350-bar warmup.

## Execution assumptions

**Pinned engine/source actually inspected through connected GitHub app 2026-10-27:** Hummingbot package **20260920**, VERSION **dev-2.17.0**, source commit **HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3**. Inspected pinned VERSION; BinanceSpotCandles constants and REST parser; strategy_v2/backtesting/backtesting_engine_base.py and backtesting_data_provider.py; executors_simulator/order_executor_simulator.py; executors/order_executor/data_types.py. Prior independent reviewed PR #414 reports 902/902 wheel/source byte identity and a representative validation for this pinned package, **not freshly reproduced this cycle**.

**Bounded model path:** BinanceSpotCandles INTERVALS contains **1d**; its REST parser maps row[0] to **open timestamp** and row[1..5] to actual O/H/L/C/V. BacktestingDataProvider requests historical candles with an explicit interval; prevalidate continuity/price before BacktestingEngineBase.prepare_market_data(), which can otherwise merge_asof/dropna and conceal invalid data. BacktestingEngineBase.simulate_execution() iterates prepared rows, update_state(row) sets current observed close and features, then controller.determine_executor_actions() emits CreateExecutorAction with OrderExecutorConfig. This proposed derivative requires a **not-yet-implemented minimal strategy-specific controller** for the declared SMA-regime/state machine; an API accepting a config does not mean that controller exists.

**Order and accounting path:** OrderExecutorConfig: connector_name="binance", trading_pair="BTC-USDT", side=BUY or SELL, amount=Decimal("0.001"), execution_strategy=MARKET, price=None, leverage=1, explicit OPEN/CLOSE position_action. The pinned OrderExecutorSimulator MARKET branch fills on the first supplied historical candle at its **actual close**, sets filled_amount_quote=Q*close and cum_fees_quote=trade_cost*Q*close, and terminates with CloseType.POSITION_HOLD. BacktestPositionHold nets opposing BUY/SELL, uses weighted cost for same-direction additions (disabled here), tracks gross realized PnL and accumulates quote fees separately. Use trade_cost=0.001 per filled side, with independent cash/fee reconciliation and durable position/fill state. The default one-hour terminated-executor view can expire between bars; use a durable position-hold/ledger or the pinned terminated_executors_window=None option rather than infer FLAT from an expired view. Pinned final-tick executor/position flush exists.

**Boundaries:** Spot funding is **not applicable**; no fabricated zero-funded futures accounting. 0.1% per-side fee is an explicit hypothetical research parameter, not a verified Binance customer tier. No modeled slippage/spread, maker queue, partial fills, market impact, exchange lot/precision or real order-book liquidity is claimed. The native historical close-fill model and raw-open-timestamp caveat are explicit. BacktestingDataProvider.get_price_by_type has a Decimal("1") fallback: it **must not** be used to fill missing data; reject absent/invalid actual close. No strategy backtest, paper/testnet/live trading, or Qlib parity is claimed. Before a new execution primitive is used in mass screening, representative event-level Qlib/Hummingbot capability parity must be established separately.

### Six-gate HB_READY assessment — Scout-proposed PASS, independent audit required

1. **Deterministic:** arithmetic SMA111 versus doubled SMA350, strict-inequality regime with explicit equality convention, prior-bar transition labels, 350-bar warmup, pure-function position with no latch/memory, no fitted or hidden state.
2. **Direction:** BTC-USDT spot LONG/FLAT; short leg explicitly disabled.
3. **Entry/exit/risk:** !top-regime BUY; top-regime full SELL; no SL/TP/trailing/time or other exits, with multi-year underwater exposure acknowledged.
4. **Position/state:** one 0.001 BTC position, 10,000 USDT cash ledger, no DCA/concurrency/cooldown/pending carryover, same-bar fills only, re-entry identical on every flat non-top bar with no episode boundary to contradict.
5. **Pinned compatibility:** directly inspected immutable 1d Binance spot data path, OrderExecutor MARKET historical close-fill, POSITION_HOLD netting, per-side fee accounting, raw timestamp and precision limits; missing data fail closed.
6. **Causality:** 350 completed bars warmup, prefix-only recursive-free arithmetic means, bar-open timestamps explicitly normalized to completion time, no future input or intrabar fill claim.

**PASS in frontmatter is a Scout proposal only.** Independent Hermes Auditor must independently verify the source facts, six gates and exact PR head before any merge.

## Evidence

### Source-reported

LookIntoBitcoin's TradingView page (script 9FFFBAOa, dated 2024-07-17, description directly read 2026-10-27) reports the 111DMA/350DMA-x-2 construction, the value-multiple convention, upward-cross peak coincidence, the 350/111 ≈ Pi note, and the overheated-market sell indication. Complete Pine code, exact native daily input feed, fill timing, source sizing and commission were **not available** in the inspected public page. No original strategy performance statistics are reproduced.

### Independently reproduced

**None.** No Pine replay, Hummingbot/Qlib backtest, profitability estimate, Sharpe, drawdown, OOS, Survivor or HB Certified result. This Scout inspected the pinned Hummingbot **source code path**, not installed wheel bytes or executed controller tests; prior independent package mapping is cited, not rerun.

### Negative evidence

No original Pine source/version bytes; no claim that the indicator's sell indication was ported losslessly (it was not — the LONG-iff-not-top mapping, venue/timeframe, SMA arithmetic convention, warmup, sizing and fees are **independent researcher choices**, not facts invented about the author); no production controller or actual market fill, cost, exchange precision proof; no claim that the same-completed-close model is a tradable post-close price; no Qlib event parity. By construction the strategy holds through all non-top history including deep multi-year drawdowns, and a top-regime exit can whipsaw if price continues higher. No historical cross dates, counts or peak-proximity statistics are claimed here.

## Falsification plan

Under separate downstream authorization, replay a representative pinned Hummingbot and Qlib tape with equal-SMA111-versus-doubled-SMA350 ties, crossUp/crossDn edges, 350-bar warmup boundary, missing candle, fee-net ledger, insufficient cash, end-of-run inventory and timestamp normalization. Compare regime-gated holding versus unconditional buy-and-hold at the same costs. Any unexplained event divergence blocks downstream parity/certification; fee-net underperformance versus buy-and-hold falsifies the research hypothesis. **No such replay was run here.**

## Crypto portability

BTC-USDT spot 1d is a deliberate independent research scope, not an author-verified crypto setting or HB_READY whitelist. ETH/other pairs, 1h/4h, short, isolated futures 3x/5x, and BO/SO 6/6/6 are optional separately specified downstream experiments, **not admission prerequisites**. The 111/350 windows were designed around Bitcoin cycle history; transfer to other assets would be a separately declared research revision, not presumed portability.

## Limitations

No full original Pine bytes or source revision hash were retrieved. The 350-bar warmup consumes roughly the first year of any data window. Top-regime exits are rare by construction, so most history is indistinguishable from buy-and-hold while still paying exit/re-entry fees on whipsaws. Close-only top exits offer no protective stop, and modeled close fills are idealized. The record is a precise independently derived **research-only** specification, not an executable Hummingbot controller, profitability assertion or approval for trading.

## Implementation status

**not-implemented.** Minimal strategy-specific controller and reproducible execution artifact may be required only after downstream selection. HB_READY admission is not Qlib implementation admission; no new registry, compiler, runner or control plane is introduced.

## Adoption boundary

**research-only; adoption: not-approved; approval_scope: research-only.** Hermes Auditor GitHub Webhook Review alone owns source-fact remediation, exact-head PASS merge or NOT_LOSSLESS close. The existing signed webhook receiver alone owns post-merge README count reconciliation. No merge, approval, README edit, Qlib/Hummingbot execution, container change, trading or cron action is authorized by this record.

## Related Wiki records

None created or modified. Existing moving-average-regime family records cited in Provenance are dedup comparisons, not dependencies.

## Sources

- First-party TradingView: https://www.tradingview.com/script/9FFFBAOa-LIB-Pi-Cycle-Top-Indicator/ (LookIntoBitcoin, page dated 2024-07-17; description inspected 2026-10-27).
- Immutable Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independent pinned package/source mapping: https://github.com/HCH725/alpha-strategy-research/pull/414
- Canonical policy: https://github.com/HCH725/alpha-strategy-research/blob/b89f23c2cbd64d78385b078b2d4420c734cc9f9c/.github/HB_READY_REVIEW.md
