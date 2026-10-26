---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "FMZ 500323 dual-CCI(50/5) zero-cross episode-latch — independent BTC-USDT spot 1d long-flat derivative"
created: 2026-10-27
updated: 2026-10-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - fmz
status: research-only
confidence: medium
source_as_of: 2025-07-03
sources:
  - https://www.fmz.com/strategy/500323
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FMZ 500323 dual-CCI(50/5) zero-cross episode-latch — independent BTC-USDT spot 1d long-flat derivative

## Provenance

**First-party FMZ publication inspected 2026-10-27:** ianzeng123, *Dual-Timeframe Momentum CCI Trend Following Trading Strategy*, FMZ stable strategy ID **500323**, created **2025-07-03**, https://www.fmz.com/strategy/500323 . The public page (readable without login; 743531 bytes fetched live over HTTPS during this cycle) states the complete prose rule set: a 50-period long CCI sets the primary trend while a 5-period short CCI times momentum; long entry requires long CCI(50) current **and** previous values both above 0 with short CCI(5) crossing above the zero line, with only one signal per trend cycle tracked through state variables `inPositiveCciLongCycle`, `firstCrossoverOccurred` and `firstCrossunderOccurred`; long exit is long CCI(50) crossing below the zero line; a mirrored short setup applies only when short selling is enabled. The page's risk section lists profit-taking / sensitivity exits only as future optimization directions, not as current rules. The page carries no performance numbers of any kind (no adopted statistics). The full strategy source below the description is login-gated (`Login to view full source` renders in place of the remainder); no source bytes, indicator input series, averaging convention, or revision hash beyond the description is claimed as a source fact.

**Explicitly independent derived executable strategy, NOT source-native/lossless:** This record selects Binance BTC-USDT **spot UTC 1d**, LONG/FLAT only, a researcher-pinned standard CCI on typical price TP=(H+L+C)/3 with arithmetic SMA plus mean absolute deviation and the 0.015 constant, an explicit false-to-true episode plus first-cross edge formalization of the described single-entry-per-cycle, fixed 0.001 BTC full-size orders, a one-completed-bar delayed MARKET close-fill model, **pure signal exits** (no stop, target, trailing, ROI ladder, or time exit of any kind), a 100-completed-bar warmup, and a hypothetical 0.1% fee per filled side. All additions/changes are researcher-defined and may change trade events. The original short side, original position sizing (page describes fixed-proportion capital use), original execution timing, original backtest economics and any unobserved Pine/JS defaults are **not** reproduced.

**Immutable strategy identity:** FMZ:500323 | ianzeng123 | source-publication:2025-07-03 | independent-derivative-v1:2026-10-27 | binance:BTC-USDT:spot:UTC1d | CCI50(TP)>0-trend-gate + CCI5(TP)-zero-cross-first-per-episode | false-to-true entry edge | opposite-zero-cross signal exit | signal-completed-bar s -> next bar s+1 modeled CLOSE fill | 0.001 BTC | 100-bar warmup | modeled fee=0.001 per side. Any alteration of signal, risk, fill clock or size changes this derivative identity.

**Dedup at main SHA 548f2ad41f0d4a75d2377eaaab0c5917143a965d:** Full-tree searches for `500323` return zero hits outside this branch (no admitted rule uses this source). Searches for the described state variables `inPositiveCciLongCycle` / `firstCrossoverOccurred` return zero hits. Open research/* PRs (10 listed: #48, #49, #63, #89, #92, #251, #304, #331, #350, #353) contain no dual-CCI record; the nearest, #304, is a forven **single-length** CCI oversold-recross with no 50/5 dual structure and no episode latch. Main records by the same FMZ author are materially distinct mechanisms: the Balance-of-Power record (FMZ 483504) trades a single-bar `(close-open)/(high-low)` pressure ratio on ±0.8 threshold crosses; FMZ 482833 trades CMO14/BB20 crossunder oversold; FMZ 482890 trades a quantile band trigger. Main CCI records are all single-length or threshold-reversal constructions (`cci-threshold-extreme-reversal`, `cci-ema-rsi-cross-trailing-stop`, `freqtrade-macd-cci-dip-state`, `freqtrade-macd-cross-cci-edge`, `freqtrade-strategy004`, `freqtrade-swinghightosky-cci-rsi`, `tradingview-vlenarcic-volume-cci-stoch-vwap-cross`) — none combines a CCI50 positivity trend gate with a CCI5 zero-cross first-per-episode latch and a pure opposite-zero-cross exit. No claim that a simple CCI parameter variant constitutes a new family.

## Economic mechanism

### Source-reported

The author describes a trend-plus-momentum dual confirmation: the slow CCI(50) regime filter keeps trading aligned with the primary trend while the fast CCI(5) zero-line cross times entries early in the move, with a one-entry-per-cycle latch suppressing overtrading in oscillations. No source performance number is adopted.

### Research interpretation

The independent derivative tests whether the **first** fast-CCI momentum ignition inside a **newly established** slow-CCI up regime (rather than every persistent positive bar) has positive fee-net expectancy under fixed, delayed completed-close signal exits. The zero line is a nominal decision threshold on a researcher-pinned CCI; nothing here asserts the pinned CCI equals the author's unobserved implementation.

## Signal

All clauses below are the complete **researcher-authored derivative v1**; source-native facts are separated above.

1. Use one chronological, gap-free Binance BTC-USDT spot **UTC 1d** OHLCV sequence indexed t=0,1,..., with finite strictly positive O,H,L,C, finite V>=0, L<=min(O,C)<=max(O,C)<=H. Validate each observed bar's opening timestamp T[t] is UTC midnight and T[t+1]-T[t]=86400 seconds, with no duplicates. No interpolation, forward-fill, synthetic prices, unseen final incomplete bar, or full-sample fitted parameters. Calculate indicators sequentially in float64 without interim rounding; use Decimal for modeled fills, cash and fees.
2. Typical price TP[t]=(H[t]+L[t]+C[t])/3. For window n in {50, 5}: SMA_n[t]=arithmetic mean(TP[t-n+1..t]), valid at t>=n-1; MD_n[t]=arithmetic mean(|TP[i]-SMA_n[t]|) over i in t-n+1..t. CCI_n[t]=100*(TP[t]-SMA_n[t])/(0.015*MD_n[t]) when MD_n[t]>0; define CCI_n[t]=0.0 when MD_n[t]==0 (researcher-defined flat-market fallback, not an alleged source default). The TP input series, arithmetic SMA/MD convention, 0.015 constant and zero fallback are derivative pins. Strict comparisons only: trend-positive means CCI50[t]>0 strictly; equality fails.
3. Zero-cross primitives on completed bars: crossAbove(X)[t]=(X[t-1]<=0 AND X[t]>0); crossBelow(X)[t]=(X[t-1]>=0 AND X[t]<0). Equality on the prior bar counts as crossed (standard edge semantics); a bar that merely touches zero without crossing (X[t]==0) is neither.
4. Up-episode state: episode E opens at the first completed bar t with crossAbove(CCI50)[t]; it stays open for every later bar while CCI50>0 strictly, and closes at the first bar with CCI50<=0. Each episode carries a `consumed` flag initially false. Entry event E[t]=episode-open[t] AND (CCI50[t]>0 AND CCI50[t-1]>0) AND crossAbove(CCI5)[t] AND NOT consumed AND FLAT AND no pending order AND t strictly later than the last exit-fill bar AND t>=100. The both-positive trend gate plus first-cross edge plus per-episode latch is the declared derivative formalization of the described single-entry-per-cycle; it is not claimed to byte-match the author's unobserved state code. Warmup bars t=0..99 are NO-TRADE, initially FLAT with zero BTC; the first eligible signal decision is t=100. Missing/invalid required data aborts the entire segment rather than silently skipping a bar.
5. When FLAT, with no pending order and t strictly later than the last exit-fill bar, an eligible completed-bar E[t] schedules **one** BUY at the *next* full bar t+1 and marks the episode consumed at scheduling time. The pinned historical OrderExecutor MARKET simulation fills exactly Q=Decimal("0.001") BTC at the **actual observed C[t+1]**, effective no earlier than T[t+1]+86400; signal t must not read O/H/L/C/V[t+1]. If there is no t+1 bar, leave the signal unfilled, with no phantom trade. Reject insufficient cash, missing price, invalid fill or unverified trading rules; never invent a fill.
6. On confirmed full BUY fill at bar f=t+1 with actual simulated entry price P=C[f], set LONG with quantity Q. No stop, target, trailing, ROI, or time-exit levels are created. No exit is evaluated on entry-fill bar f. Intrabar high/low touches are never used for exits.
7. On a later completed bar u>f while LONG and with no pending order, if crossBelow(CCI50)[u], schedule full-quantity SELL at bar u+1 close (reason TREND_EXIT); else HOLD. The next-bar fill is C[u+1] even if it gaps; it is not filled at the zero-crossing level. The original short-side signals and every other exit type are disabled; there is exactly one exit condition.
8. After a full SELL fill, set FLAT and record the exit-fill bar. Do not enter on the same bar as an exit fill. A new entry requires a **new** up-episode (a fresh crossAbove(CCI50)) plus a new crossAbove(CCI5) on a later completed bar t>exit_fill_bar; an unconsumed episode can never survive an exit because any exit closes only via CCI50<=0, which also closes the episode. Entry edges while LONG or pending are ignored, not queued. At most one pending order and one long position; no pyramiding, Safety Orders, DCA, partial fills, scaling, cooldown timer, concurrent markets or portfolio allocation. On partial, rejected, duplicate, missing or ambiguous fills **abort** the research segment instead of fabricating state. A pending exit is never silently retried.
9. At sample end, discard unfillable pending signals; mark any open inventory at the final **observed completed** close, reporting unrealized value separately. No invented final liquidation, fee, price or realized PnL. A segment restart resets FLAT, clears the episode/consumed state, and requires the full 100-bar warmup, never carries unobserved inventory.

**Position/cash and costs:** Initial modeled cash=Decimal("10000") USDT, inventory=0 BTC, no compounding/leverage. BUY only if cash>=Q*P*(1+f), with f=Decimal("0.001") per filled side; cash -= Q*P*(1+f). SELL exactly filled Q, cash += Q*P*(1-f). Net realized round-trip PnL = Q*(sell_price-buy_price)-f*Q*(buy_price+sell_price). Maintain persistent filled-quantity, pending, entry P, episode/consumed state, last fill-bar, cash and fee ledger. One pair only; no shared-capital synchronization. The research fee is hypothetical, not an asserted Binance tier or source fee. Spot funding is **not applicable**, not an invented zero-funding series.

**Disabled:** short/borrow, margin/perpetuals, leverage, liquidation, maker/limit/next-open fills, intrabar stops, fixed stop/target, trailing, ROI ladders, time exits, opposite-signal short entries, rebalancing, multiple pairs, DCA, Safety Orders, discretionary overrides and hidden controller defaults.

## Required data

One **real**, contiguous, completed Binance BTC-USDT spot UTC daily candle feed with O/H/L/C/V and raw Binance open timestamp. The only external requirement is that historical candles are actually retrievable; if not, this derivative is unexecutable on that segment. CCI50, CCI5 and all crosses use no non-OHLCV, multi-timeframe, order-book, funding or future data. Every signal at bar t uses only <=t and is available at **T[t]+86400**. The bar t+1 close fill becomes economically known only at **T[t+1]+86400**, even though the native simulator labels its row with open timestamp T[t+1]. Reject timestamp misuse, gaps, unobserved prices and unverified price/amount precision; never treat a missing-price fallback as market data.

## Execution assumptions

**Pinned actual engine inspected via GitHub API 2026-10-27:** HCH725/hummingbot at immutable commit **8b0e067e80ab62f10846d518dcb5a8218527ddb3** (committer date 2026-09-20, staging v2.17 sync), Hummingbot package label **20260920**, repository `hummingbot/VERSION` = **dev-2.17.0**. The package/source mapping and prior 902/902 byte-identity check were reported in independently merged Alpha PR #414 and reused by merged Alpha PR #503; this Scout verified the pinned commit object and the `1d` entry in `binance_spot_candles/constants.py` directly but **did not rehash an installed wheel** or execute its tests.

- **Real data path:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` includes `1d` (verified at the pinned commit this cycle); `binance_spot_candles.py` REST parser maps Binance kline row[0] to opening timestamp and row[1..5] to O/H/L/C/V. `BacktestingDataProvider` can initialize `binance_BTC-USDT_1d` candles. Validate completeness and actual prices **before** `BacktestingEngineBase.prepare_market_data()` merges features with backward `merge_asof` and `dropna`; otherwise missing bars/features can disappear silently.
- **Controller/action path:** `BacktestingEngineBase.run_backtesting(controller_config,start,end,backtesting_resolution="1d",trade_cost=0.001)` initializes connector trading rules and the candle feed; `simulate_execution` visits rows, calls `update_state(row)`, then `controller.determine_executor_actions()`, and dispatches `CreateExecutorAction(OrderExecutorConfig)` to `OrderExecutorSimulator`. A **future minimal candidate-specific controller** must calculate the stated CCI/episode state and use strictly prior completed signal features for any delayed action; **no such controller exists yet** and a generic controller is not misrepresented as implementing it.
- **Exact execution primitive:** `OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),position_action=OPEN/CLOSE,execution_strategy=MARKET,price=None,leverage=1)`. In pinned `order_executor_simulator.py`, MARKET fills on the **first supplied candle** at its actual `close`, `filled_amount_quote=Q*close`, `cum_fees_quote=trade_cost*notional`, and returns `CloseType.POSITION_HOLD`. It is an idealized full-fill close-price research model, **not** a real post-close executable market price, next-open order, slippage model or stop order.
- **Causality guard:** `update_state(row)` already exposes the current row close, and the simulator stamps the fill with that row's **open timestamp**. For a signal at completed t, the future controller may emit only the stored t decision at row t+1 and must never use t+1 values for that decision. Record modeled fill effective time as the **t+1 close availability**, not the raw open timestamp. The simulator's row timestamp is a historical index, not evidence that C[t+1] was available at its opening. Do not let a newly filled order trigger another same-bar action.
- **Position/cost compatibility:** `BacktestPositionHold._process_order` in `backtesting_engine_base.py` nets opposite BUY/SELL base quantities and computes **gross** matched realized PnL; `add_executor` accumulates fees separately. Reconcile cash, net realized PnL and final marked inventory explicitly from full-fill ledger; do not call gross realized PnL fee-net. Preserve complete fills/position state (e.g. `terminated_executors_window=None`) rather than relying on a one-hour controller view across daily bars. The engine performs final-tick ledger flush.
- **Fail-closed constraints:** `BacktestingDataProvider.get_price_by_type` has a `Decimal("1")` missing-price fallback: it is explicitly **forbidden** for this derivative. Validate real C before every action; abort if unavailable. Binance spot trading-rule initialization and amount quantization exist, but real minimum notional, precision, spread, liquidity, partial fills, exchange fees and live order acceptance are **not proven** by the backtester. A future materialization must check these instead of assuming market execution. Funding/margin accounting is outside this unleveraged spot-only version.

**Gate 5 boundary:** Verified reusable primitives are one real Binance spot 1d OHLCV feed, deterministic one-order-per-event MARKET historical close fills, explicit modeled fee accumulation and POSITION_HOLD netting — the identical primitive set already reviewed in merged PRs #414/#503. No claim that the unimplemented candidate controller or actual live trading path is verified. This bounded strategy uses no additional unverified engine primitive (no trailing, no ROI ladder, no multi-asset sync, no intrabar fills). A new execution capability needs one representative Hummingbot/Qlib event-level validation before mass Qlib screening, not a new strategy-admission gate.

## Evidence

### Source-reported

The 2025-07-03 first-party FMZ page reports the CCI50 trend gate (current and previous >0), the CCI5 zero-cross timing trigger, the single-entry-per-cycle latch variables, the CCI50 zero-cross long exit, the optional mirrored short, and risk exits as future work only. No source backtest statistics of any kind are represented as independently reproduced.

### Independently reproduced

**Not independently reproduced.** No source replay, candidate-specific Hummingbot/Qlib backtest, event-level parity, installed-package rehash, real fills, profitability, OOS, Survivor status or HB Certified result. Pinned Hummingbot source compatibility was inspected; historical PR #414's separate engine test evidence is cited only as prior primitive evidence.

### Negative evidence

Unobserved login-gated source implementation, hence no source-native equivalence claim for the CCI input series, averaging internals, or exact latch code. The TP=(H+L+C)/3 series, arithmetic SMA/MD, 0.015 divisor, MD=0 zero fallback, cross edge semantics, episode formalization, next-bar-close timing, spot long-only restriction, fixed amount, nominal fee and pure-signal exit are explicit researcher choices. Exits realize the next close after the cross bar, so realized moves can exceed the cross-bar move. Real Binance fills/precision/costs and futures funding are unverified.

### Six-gate HB_READY proposal (independent Auditor must decide)

1. **Determinism:** exact TP/SMA/MD/CCI formulas with seeds and ties, strict gates, standard cross edges, explicit episode/consumed state machine, no fitting, fixed warmup.
2. **Direction:** Binance BTC-USDT spot LONG/FLAT; original short explicitly disabled.
3. **Entries/exits/risk:** first-cross-per-episode entry; single opposite-zero-cross signal exit; all stops/targets/trailing/ROI/time-exits explicitly disabled with source backing (page lists them as future work).
4. **Position/state:** fixed 0.001 BTC, fee/cash accounting, one pending full-fill order, no DCA, concurrency or same-bar re-entry, new episode required after exit.
5. **Pinned engine:** directly inspected Binance spot 1d feed, controller/action dispatch, MARKET close-fill, POSITION_HOLD netting, fee accumulation, missing-price guard and effective timestamp limitation at immutable 20260920/dev-2.17.0 source; no new primitive beyond merged #414/#503.
6. **Point-in-time:** contiguous completed daily bars, 100-bar warmup, t signal -> t+1 modeled close fill, no future inputs or early open-timestamp claims.

`hb_ready_status: PASS` is a **Scout submission**, not self-approval; independent Hermes Auditor controls exact-head admission.

## Falsification plan

If separately authorized for implementation, compare page predicates against the derivative's explicit TP/SMA/MD/CCI pins and seeds, strict equality handling, MD=0 fallback, initial warmup, episode-open/close/consumed transitions, rejected/partial fill abort, cash/fee netting, next-bar close-effective timestamp, no same-bar re-entry and final open inventory. Before broad Qlib screening on an unverified execution path, demonstrate representative Hummingbot/Qlib event-level parity including prices, sizes, fills and costs. A negative fee-net expectation or unexplained event mismatch falsifies downstream hypotheses. **No test or backtest run here.**

## Crypto portability

BTC-USDT spot 1d is a declared **research choice**, not a source-tested crypto claim or admission whitelist. Other coins, shorter bars, isolated 3x/5x futures, BO6/SO6/SO6 or different fills are optional separately specified research derivatives and require appropriate engine/economic verification. No automatic DCA overlay is asserted event-neutral.

## Limitations

Page description is not complete source; original strategy and this independent derivative can trade differently. Zero-cross signals are not protective exchange orders. Historical next-bar-close full fills ignore actual spread, slippage, partial fills, latency and fee tiers. No Qlib materialization, realized funding, backtest profitability, OOS, survivor certification or live approval is implied.

## Implementation status

**not-implemented.** The record is an inspectable, immutable research specification; there is no dedicated Hummingbot controller, Qlib recipe, deployed bot or strategy replay. Downstream selection may require minimal strategy-specific materialization, without a second eligibility registry.

## Adoption boundary

**status: research-only; adoption: not-approved; approval_scope: research-only.** Independent Hermes Auditor GitHub Webhook Review owns source-fact remediation, exact-head PASS merge or NOT_LOSSLESS close. The existing signed webhook receiver alone owns post-merge README count synchronization. Scout does not approve/merge/close, touch main/README, run a backtest or trade.

## Related Wiki records

None created or modified. No private Wiki material or private user data is included.

## Sources

- ianzeng123, *Dual-Timeframe Momentum CCI Trend Following Trading Strategy*, FMZ first-party public page, strategy ID 500323, created 2025-07-03, inspected 2026-10-27: https://www.fmz.com/strategy/500323
- Immutable pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independent pinned engine evidence (not this candidate's backtest): https://github.com/HCH725/alpha-strategy-research/pull/414
- Same-primitive merged precedent (not this candidate's backtest): https://github.com/HCH725/alpha-strategy-research/pull/503
- Canonical review contract: https://github.com/HCH725/alpha-strategy-research/blob/548f2ad41f0d4a75d2377eaaab0c5917143a965d/.github/HB_READY_REVIEW.md
