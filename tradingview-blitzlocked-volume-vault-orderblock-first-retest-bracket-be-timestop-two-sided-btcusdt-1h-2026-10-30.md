---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TradingView blitz_locked Volume Vault displacement order-block first-retest bracket stop break-even time-stop two-sided BTCUSDT 1h derivative
created: 2026-10-30
updated: 2026-10-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-11
sources:
  - https://www.tradingview.com/script/ouvmvItR-Volume-Vault-Volume-Order-Block-Retest-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Volume Vault displacement order-block first-retest — independent BTCUSDT perpetual 1h two-sided derivative

## Provenance

**First-party publication:** blitz_locked, *Volume Vault | Volume Order Block Retest Strategy*, public TradingView open-source strategy, script ID **ouvmvItR**, page badge **OPEN-SOURCE SCRIPT**, dated **Oct 11** (page `<time>` reads Sat 10 Oct 2026 17:37:02 GMT = Oct 11 Asia/Taipei; no separate revision date shown), default chart symbol **BTCUSD**, inspected end to end **2026-10-30**: https://www.tradingview.com/script/ouvmvItR-Volume-Vault-Volume-Order-Block-Retest-Strategy/ . No paid/invite-only gate; the full Pine source renders in the public Source code tab.

**Pine source read verbatim this cycle (all 201 lines, `//@version=6`):** strategy declaration `strategy("Volume Order Block Retest Strategy", overlay=true, max_boxes_count=100, max_labels_count=100, initial_capital=10000, pyramiding=0, default_qty_type=strategy.percent_of_equity, default_qty_value=10, commission_type=strategy.commission.percent, commission_value=0.05, slippage=2)`. Token census over the rendered source: 1 `strategy(` declaration / 2 `strategy.entry` (`"Long"`/`strategy.long`, `"Short"`/`strategy.short`) / 2 `strategy.exit` (`"XL"` from `"Long"` with `stop=`+`limit=`, `"XS"` mirror) / 1 `strategy.close_all` (time stop) / 0 `strategy.order(` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `barstate` / 3 `ta.` (`ta.atr(atrLen)`, `ta.sma(volume, volLen)`, `ta.ema(close, emaLen)`) / 8 `volume` reads / 2 `syminfo.mintick` (both in the `risk > syminfo.mintick` entry guards) / 1 `box.new` / 2 `label.new` / 27 `input.*` (9 detection + 10 entry-filter + 5 risk + 3 visual). No `process_orders_on_close` argument ships (Pine default false: signals on bar close, orders fill next bar — the author states exactly this on the page). No `calc_on_every_tick` argument ships (default false: one evaluation per completed bar).

**Frozen source inputs (any other value is a different, unpinned rule):** `atrLen=14`, `dispMult=0.8`, `volLen=20`, `impVolMult=1.0`, `needOpp=false`, `needBreak=false`, `bodyZone=false`, `maxZones=15`, `maxAge=300`, `firstTouch=true`, `needCandle=true`, `useRejection=false`, `wickPct=25.0`, `useRetestVol=false`, `retestVolMax=1.0`, `useTrend=false`, `emaLen=100`, `allowLong=true`, `allowShort=true`, `slBuf=0.2`, `rrTarget=1.5`, `useBE=true`, `beAtR=1.0`, `maxBars=60`. The five optional filter branches (`needOpp`, `needBreak`, rejection wick, retest volume dry-up, EMA trend) are disclosed here and deliberately not adopted — this record freezes the default machine only. `bodyZone=false` pins full prior-bar high/low zones, never body-only. Visual inputs (`bullCol`, `bearCol`, `showZones`) have no order-leg effect.

**Independently derived, not source-native/lossless:** This version retains the literal displacement qualification, zone geometry, youngest-first first-retest consumption, candle-confirmation gate, ATR-buffered stop, 1.5R target, 1R break-even ratchet, 60-bar time stop, two-sided flat-gated posture, and `pyramiding=0` single-position semantics. It independently pins venue **BTCUSDT Binance USDT-M perpetual 1h**, completed-bar-close decisions with **next-bar-close** MARKET fills (the source backtest fills next-bar-open by language default), fixed **0.01 BTC** sizing (the source compounds 10% of equity), 1× isolated margin, 0.05%-per-side modeled fee, and a 150-bar warmup. The source's 2-tick slippage setting is **not** reproduced by the pinned simulator (disclosed gap). These alterations change fill prices, equity path, and tradable universe; the original TradingView strategy is **not** asserted to pass HB_READY.

**Frozen identity:** TV:ouvmvItR:blitz_locked:2026-10-11 | independent-derived-v1:2026-10-30 | body>=0.8*ATR14[1] vol>=1.0*SMA20[1] | prior-bar H/L zone, 15 FIFO, age 300 | youngest-first first-retest + directional close | SL zone-edge+-0.2*ATR / TP 1.5R / BE@1R / time 60 | next-close MARKET | BinancePerp:BTCUSDT:1h:TWO-SIDED:0.01BTC:1x:fee0.0005. Any change to formula, state, timing, fees, sizing, or market creates a new version.

**Pre-write dedup:** working tree at base `45bf1135d8b97d56d7d19997b1c5efa3467cdb20` holds **454** root `.md` files = **452** strategy records + 2 READMEs. Case-insensitive fixed-string sweeps for `orderblock`, `order-block`, `volume.vault`, `ouvmvItR`, `blitz_locked`, `blitzlocked`, `supply.zone`, `demand.zone`, `zone retest`, `first retest`, `smartmoney`, `SMC` return **zero** SMC order-block / supply-demand-zone records — remaining `displacement`/`order block` hits are prose about code blocks or unrelated displacement oscillators, verified by line inspection. All 11 open `research/*` PRs listed (#593 Vinicius Supertrend, #353 Heracles KCD, #350 ClucMay72018, #331 AdxSmas, #304 Forven CCI, #251 Swift 2yma, #92 SSL, #89 Chandelier, #63 SuperTrend flip, #49 Gauss StochRSI, #48 Larry Williams) — none is an order-block / displacement-zone / first-retest mechanism. Nearest pool neighbors differ in mechanism class: `fair-value-gap-breakout-*` (stateless two-bar gap print, no zone storage, no volume qualification, no SL/TP state); `forven-engulfing-body-cover-volume-*` (single-bar engulfing plus volume, no zone memory, no ATR buffer, no bracket exits); `ut-bot-atr-trailing-stop-flip` (ATR trailing-stop flip state, no displacement qualification, no zones, no volume); `fmz-486567-log-price-zscore-dynamic-stop` (z-score band fade, no zones, no volume impulse). Five-axis distinction: no pool record and no open PR stores volume-displacement-qualified prior-bar zones with youngest-first single-consumption first-retest entries plus an ATR-buffered bracket with break-even ratchet and bar-count time stop, two-sided.

## Economic mechanism

### Source-reported

Large-body, high-volume candles ("displacement") mark institutional participation; the candle before the impulse is the order block (demand/supply zone); the first return to the zone with directional confirmation offers a defined-risk entry with the stop beyond the zone plus an ATR buffer and a fixed R-multiple target. The author warns that backtests are simplified, real fills/spreads/slippage differ, stops and targets can be hit in the same bar, volume varies by venue, and entries fill a full bar after the signal. No profitability or portability conclusion is adopted from the author's claims.

### Research interpretation

A volume-confirmed displacement zone that survives (no close through its far side) may act as a short-horizon reference level; fading the first retest with a zone-anchored bracket tests whether that memory persists one touch. This is a researcher hypothesis, **not** the author's tested system and not evidence of positive expected returns. The youngest-first priority plus single-consumption makes the system trade each zone at most once — a deliberately decaying opportunity set, disclosed.

## Signal

**Data and effective clock:** One observed Binance USDT-M perpetual BTCUSDT **1h OHLCV** sequence (base-asset volume). Raw exchange candle timestamp T[t] denotes **bar opening**; the complete candle is available no earlier than T[t]+3600 seconds. Require consecutive T increments of exactly 3600 seconds, finite O/H/L/C > 0, H >= max(O,C), L <= min(O,C), finite V >= 0, and actual observed closing prices. No synthetic candles, forward fill, partial bars, alternative timeframes, external feeds, or future information. If any required bar is absent/invalid, fail the research run rather than bridge the gap.

**Arithmetic discipline (single pinned rule):** The entire signal path is **IEEE-754 binary64** (`float`), the same width as Pine `float` — no alternative precision reading. `Decimal` appears only in engine-plumbing quantity constants, and every ledger conversion from an observed price P uses `Decimal(str(P))` verbatim. There is no "float or Decimal" optionality anywhere in this record.

**Researcher-frozen deterministic setup (completed-bar closes only):** For each completed bar t:
- `ATR[t] = ta.atr(14)` (RMA-seeded), `VSMA[t] = SMA20(volume)`, `EMA[t] = ta.ema(close, 100)`.
- `BODY[t] = abs(C[t]-O[t])`; `BIGBODY[t] = BODY[t] >= ATR[t-1]*0.8`; `BIGVOL[t] = V[t] >= VSMA[t-1]*1.0`.
- `BULL_IMP[t] = (C[t]>O[t]) AND BIGBODY[t] AND BIGVOL[t]`; `BEAR_IMP[t] = (C[t]<O[t]) AND BIGBODY[t] AND BIGVOL[t]`. (The `needOpp`/`needBreak` conjuncts are frozen false and contribute nothing.)
- Zone store (array, max 15, FIFO shift-out oldest on overflow): before creating any new zone from bar t, first sweep existing zones newest-to-oldest: a bull zone dies iff `C[t] < bottom`, a bear zone dies iff `C[t] > top`, any zone dies iff `t - bornBar > 300` (all strict; equality survives). A surviving zone is *touched* iff `H[t] >= bottom AND L[t] <= top`. If touched while FLAT with no pending fill and not (`firstTouch` and already used), evaluate long-first for bull zones (`C[t]>O[t]` AND `C[t] > bottom`, `allowLong`) then short for bear zones (`C[t]<O[t]` AND `C[t] < top`, `allowShort`); the **first** (hence youngest, newest-to-oldest order) qualifying zone sets the signal and is marked **used immediately per code behavior** (see Negative evidence 1). At most one signal per bar; long checked before short per frozen code order (mutually exclusive in practice: `C[t]>O[t]` vs `C[t]<O[t]` cannot co-hold).
- New zones are created from bar t only after the sweep: if `t > max(14,20)+1 = 22` (source gate, structural minimum) and `BULL_IMP[t]`, store `[L[t-1], H[t-1]]` as a bull zone (full-range pin; `bodyZone=false`); mirror for bear. Overlapping same-direction zones are discarded, never merged. A zone born at t is first tradable at t+1 by construction.
- Entry (flat gate, `pyramiding=0` parity): on signal bar t, long `STOP = bottom - ATR[t]*0.2`, `RISK = C[t] - STOP`; submit **only if `RISK > tickSize`** (code-behavior pin of the `syminfo.mintick` guard), else consume the signal and stay flat. `TP = C[t] + RISK*1.5`. Short mirror: `STOP = top + ATR[t]*0.2`, `RISK = STOP - C[t]`, `TP = C[t] - RISK*1.5`. The MARKET order is submitted only on the **t+1 row** and fills at the **t+1 completed close** (next-bar-close pin; see Execution assumptions).
- Break-even ratchet (completed-bar evaluation, causal: uses the finished bar's high/low known at its close): while long, if `H[t] >= AVG + RISK*1.0` then `STOP := max(STOP, AVG)`; while short, if `L[t] <= AVG - RISK*1.0` then `STOP := min(STOP, AVG)`. Ratchet applies from the next bar onward.
- Bracket exits (close-trigger pin of Pine intrabar `strategy.exit`): at each completed bar t while positioned, evaluate on the finished bar: long exits iff `C[t] <= STOP` (stop leg) or `C[t] >= TP` (limit leg); if both legs print on the same bar, the **stop leg wins** (conservative pin; the source itself warns both can be hit in one bar). The exit MARKET order is submitted only on the t+1 row and fills at the t+1 completed close. Short mirror.
- Time stop: record entry fill-bar index b (the bar whose close filled the entry); at the first completed bar t with `t - b >= 60`, submit `close_all` equivalent (full-quantity MARKET CLOSE), filled at the t+1 completed close.
- One position, one pending action: entries require FLAT with no pending fill; no entry on any fill/confirmation bar; no same-bar entry after exit; no adds/pyramiding/DCA; fresh entry after a confirmed exit requires a new later signal, otherwise zero additional cooldown.

**Warmup:** structural minimum is the 23rd completed bar for zone creation plus EMA100 seeding for the (frozen-off) trend input; the adopted warmup is the first **150** completed 1h bars flat by record rule (predeclared researcher margin covering ATR RMA seed, SMA20 seed, and EMA100 stabilization; ≈6.25 days). Start FLAT with 10,000 USDT equity, no inherited position, no pending action. Never infer a position from pre-sample data.

**Explicitly disabled:** `needOpp`/`needBreak`/wick/rejection/volume-dry-up/EMA-trend optional filters, body-only zones, SHORT-or-LONG leg removal (both legs source-default true and both adopted), pyramiding, BO/SO/DCA, compounding, multiple concurrent positions, partial fills, maker/limit/next-open/intrabar order models, trailing stop, discretionary exits, portfolio sharing, dynamic equity-risk sizing, and any hidden controller risk defaults.

## Required data

Only historical **real** Binance BTCUSDT perpetual 1h O/H/L/C/V (base-asset volume) with exchange opening timestamps and complete candle availability. No lower-timeframe reconstruction, order book, funding/mark/index series as signal inputs, external calendar, fitted model, or multi-asset alignment. The historical engine's next-close fill convention is idealized, not a promise of real market execution. Perpetual funding is **not** a signal input; its accounting boundary is flagged under Execution assumptions, never fabricated as zero.

## Execution assumptions

**Pinned benchmark:** Hummingbot package **20260920**, VERSION **dev-2.17.0** per repository admission contract; source **HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3** (merge commit verified by object read this cycle; `hummingbot/VERSION` at the pin reads `dev-2.17.0`). The following paths were read at that exact commit this cycle (local object store, no floating branch):

- **Feed:** `hummingbot/data_feed/candles_feed/binance_perpetual_candles/constants.py` — REST `https://fapi.binance.com` + `/fapi/v1/klines`, `INTERVALS` bidict includes **`1h` = 3600**, `MAX_RESULTS_PER_CANDLESTICK_REST_REQUEST = 1500`. `binance_perpetual_candles.py::_parse_rest_candles` maps exchange `row[0]` to open-timestamp seconds and `row[1..5]` to O/H/L/C/V (base volume), `row[7]` quote volume. Preflight contiguous 3600-second timestamps and complete/finite prices **before** `BacktestingEngineBase.prepare_market_data()`, whose `dropna` could otherwise hide missing rows.
- **Controller/executor:** a future strategy-specific controller can maintain the above zone-array state machine and issue `CreateExecutorAction` with `OrderExecutorConfig(connector_name="binance_perpetual", trading_pair="BTC-USDT", side=BUY/SELL, amount=Decimal("0.01"), position_action=OPEN/CLOSE, execution_strategy=MARKET, price=None, leverage=1)` (`hummingbot/strategy_v2/executors/order_executor/data_types.py`: MARKET needs no limit price; validators require non-empty connector, directional side, positive amount, leverage >= 1). `BacktestingEngineBase.simulate_execution` updates state per row, then determines actions and dispatches the actual `OrderExecutorSimulator`. **No dedicated implementation has been written.**
- **Fill semantics:** `OrderExecutorSimulator.simulate` fills MARKET at the **first supplied row's actual close** with full base amount, `filled_amount_quote = amount × close`, `cum_fees_quote = trade_cost × quote notional`, terminating as `POSITION_HOLD`. For a t signal the order is submitted only on the t+1 row, producing the **t+1 close** research fill; bracket/time exits likewise fill at the close after their trigger bar. Raw engine timestamps are candle **opens**; every decision/fill reported externally must use the effective **completed-close timestamp T+3600**, and bar-index scheduling (300-bar age, 60-bar time stop) must not rely on the engine's raw `_time` for elapsed-time arithmetic. This is retrospective close-price research, **not** executable live close-auction timing. A controller that consumes a current incomplete bar, executes entry on t itself, or treats raw T as close availability is nonconforming.
- **Position ledger:** entries are flat-gated and bracket/time legs always return to flat, so opposing legs never coexist — no cross-side netting is invoked. Reconcile from actual executor fill/termination ledger, not merely order intents; use `terminated_executors_window=None` (or equivalent complete ledger) to avoid losing confirmations. The `BacktestingDataProvider` price fallback `Decimal("1")` is **forbidden**: actual finite close or data-incomplete failure.
- **Cash and costs:** 10,000 USDT equity, isolated, 1× (no leverage modeling beyond the pinned `leverage=1` field). Fixed **0.01 BTC** per signal; pre-trade check requires equity ≥ notional + modeled fees, else consume the signal and stay flat with no invented fill. Explicit research `trade_cost = 0.0005` (0.05% of each filled side, = source `commission_value=0.05` percent term), a **hypothesis** not an independently verified Binance fee tier. The source's 2-tick slippage is **not** modeled by the close-fill simulator (disclosed gap, see Limitations). Precision: quantize prices/amounts down to the venue `PRICE_FILTER.tickSize` / `LOT_SIZE.stepSize` read from `binance_perpetual_derivative.py` exchange-info handling; a failed market/order validation or unavailable price is never silently filled.
- **Funding posture:** USDT-M perpetual positions accrue real funding; the pinned backtest simulator prices fills/fees only and **does not settle historical funding** — funding is an unevaluated economic term here, flagged and carried to downstream research cost modeling, never recorded as realized zero.
- **Limits:** simulator assumes full-size historical close fills and has no observed bid/ask spread, latency, impact, partial fills, real slippage, fee tier, order-book depth, or live exchange minimum-notional guarantee. Its zero extra price-impact **model** must never be described as actual zero slippage.

## Evidence

### Source-reported

TradingView's first-party public page identifies blitz_locked, script ID ouvmvItR, OPEN-SOURCE SCRIPT badge, Oct-11 date, BTCUSD default symbol, the displacement-plus-volume zone concept with per-zone volume-ratio labels, first-retest entries with directional confirmation, ATR-buffered stops, fixed-R targets, optional break-even and time stop, 10%-of-equity sizing, 0.05% commission, 2-tick slippage, and the author's warnings (simplified backtests, same-bar stop/target ambiguity, next-bar fills, venue-dependent volume). Those are author claims, not independently replayed results. No source-reported backtest number with a traceable sample is transferred to this derivative (the page carries no performance table).

### Independently reproduced

**No strategy backtest, TradingView signal replay, Qlib/Hummingbot event-level parity, profitability test, Paper/Testnet/Live order, or Survivor result was performed.** This Scout read the full 201-line Pine source verbatim and independently read the pinned Hummingbot feed/parser/engine/executor/connector paths above to bound the available single-perp-market, 1h, full-size MARKET next-close and POSITION_HOLD fee research model. It is not proof of production trading or original Pine equivalence.

### Negative evidence

1. Code-vs-description defect fenced (found by line reading, not inferred): the page and the `firstTouch` input label claim "a zone is only marked as used when a trade actually fires", but the code sets `z.used := true` at signal detection while the entry block separately gates on `risk > syminfo.mintick`. This record pins the **code behavior** (consumed at signal; entry only if the guard passes), never the prose. At BTCUSDT 1h scale the guard never binds (risk spans zone height plus buffer, orders above tickSize), disclosed.
2. Fill-timing derivation fenced: the source backtest fills next-bar-open by Pine default; this record fills next-bar-close on the pinned simulator — one bar-close later by construction, disclosed, with no equivalence claim.
3. Intrabar-bracket derivation fenced: Pine stop/limit legs trigger intrabar; this record triggers on completed-bar closes with stop-priority on same-bar ambiguity and next-close fills — a coarser, conservative transcription, disclosed.
4. Slippage gap fenced: the source's 2-tick slippage has no simulator counterpart; only the 0.05%-per-side fee is modeled, disclosed.
5. Sizing derivation fenced: fixed 0.01 BTC replaces compounding 10%-of-equity; signal/exit event times are invariant to this change but the equity path differs, disclosed.
6. No future leakage in the stack: every input at bar t is contemporaneous (`O/H/L/C/V[t]`, current-bar `ATR[t]`/`VSMA` via `[1]`-lagged seeds, zone edges from `t-1` bars) or lagged; zone management precedes creation so newborn zones trade no earlier than t+1; no `request.*`/`security(`/negative shift/full-sample normalization/`barstate`/`timenow`; one evaluation per completed bar.

**Scout six-gate submission (pending independent Auditor):** (1) exact displacement/zone/priority/confirmation/bracket/BE/time-stop arithmetic with strict comparisons and frozen inputs; (2) two-sided LONG/SHORT with legs source-default true, perpetual venue realistic; (3) complete entry, stop/target/BE/time exits plus explicit disabled list; (4) one 0.01 BTC confirmed position, one pending action, FIFO/age/consumption state, cash checks, failure/confirmation/re-entry semantics, no DCA; (5) actual pinned Binance perpetual 1h candle/parser, MARKET OrderExecutorSimulator, POSITION_HOLD fee model, precision/funding/cash rules, and explicitly corrected effective-close clock, with economic limits disclosed; (6) completed bars only, 150-bar warmup, no future inputs at signal, delayed next-close fills, precommitted bracket/time exits. **PASS here is a research Scout claim requiring independent review, not approval or HB Certified status.**

## Falsification plan

After independent admission and separate downstream selection only: test equality boundaries for body-vs-ATR, volume-vs-SMA, close-vs-zone-edge, invalidation inequalities, and the `maxAge`/`maxBars` counts; zero-volume bars (VSMA seed zero ⇒ `nz` guard path); newborn-zone t+1 eligibility; youngest-first priority under stacked zones; used-consumption with blocked entry; stop-priority on dual-leg bars; BE ratchet one-bar delay; t-to-t+1 order timing; end-of-sample pending state; rejected entries on insufficient equity; failed exits; fee-inclusive ledger netting; and the raw-open versus effective-close timestamp distinction. If a new unverified execution primitive is required, establish representative Hummingbot/Qlib event-level parity before mass Qlib screening; do not demand new parity for an already verified primitive.

## Crypto portability

Frozen to **BTCUSDT Binance perpetual 1h**. Single-pair, hourly, and OHLCV-plus-base-volume-only are choices, not HB_READY whitelist restrictions. The displacement filter is relative (body vs own ATR, volume vs own SMA), hence scale-invariant across venues — but cross-venue volume-definition differences (spot vs perp prints) can move zone formation, disclosed. Shorting assumes a futures venue; a spot-only deployment expresses the long leg only. Other pairs, leveraged margin, portfolio capital sharing, or different candle calendars require separate capability and economic verification, not silent inheritance of this PASS claim.

## Limitations

Volume-qualified zones can still fail consecutively in trends that never look back; the bracket caps each loss at ~1R plus the one-bar trigger-to-fill gap, not at the idealized stop print. First-retest consumption deliberately discards later touches. Next-close fills trail the source's next-open fills by construction. Historical close-MARKET full fills are idealized; slippage, spread, impact, funding, fee tier, precision enforcement, and live minimums are unproven. HB_READY does not establish expected returns, Qlib parity, Survivor qualification, or trading authorization.

## Implementation status

Research-only record. Dedicated strategy controller, execution artifact, Qlib recipe, and backtest are **not implemented**. Any future implementation must reproduce the frozen event state and pinned engine path or fail validation; no automatic admission of changed semantics.

## Adoption boundary

**Not approved** for Qlib campaign execution, Hummingbot deployment, Paper/Testnet/Live, or capital allocation merely by this Scout submission. Independent Hermes Auditor GitHub Webhook Review alone decides exact-head PASS merge or NOT_LOSSLESS closure. README bookkeeping remains the signed receiver's job.

## Related Wiki records

None required for this isolated research submission. Compare existing fair-value-gap breakout, engulfing-body volume, and ATR trailing-stop flip families only as distinct mechanism neighbors.

## Sources

- blitz_locked, *Volume Vault | Volume Order Block Retest Strategy*, TradingView public open-source strategy, script ID ouvmvItR, 2026-10-11, https://www.tradingview.com/script/ouvmvItR-Volume-Vault-Volume-Order-Block-Retest-Strategy/ (full 201-line Pine v6 source read verbatim 2026-10-30).
- HCH725/hummingbot pinned source commit 8b0e067e80ab62f10846d518dcb5a8218527ddb3 (VERSION dev-2.17.0): `data_feed/candles_feed/binance_perpetual_candles/constants.py` + `binance_perpetual_candles.py`, `strategy_v2/backtesting/backtesting_engine_base.py`, `backtesting_data_provider.py`, `executors_simulator/order_executor_simulator.py`, `executors/order_executor/data_types.py`, `connector/derivative/binance_perpetual/binance_perpetual_derivative.py` — all read at the pinned commit 2026-10-30.
- HCH725/alpha-strategy-research README.md and .github/HB_READY_REVIEW.md at main 45bf1135d8b97d56d7d19997b1c5efa3467cdb20, policy effective 2026-10-08.
