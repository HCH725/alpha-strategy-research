---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "FMZ 482670 multi-EMA RSI-gated ATR-stop/take-profit BTC spot 1h long-flat — independent derivative"
created: 2026-10-30
updated: 2026-10-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - fmz
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-02-19
sources:
  - https://www.fmz.com/strategy/482670
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FMZ 482670 multi-EMA trend with RSI/ATR gates and ATR stop/take-profit — BTC spot 1h independent research derivative

## Provenance

- **FMZ primary (first-party page, public, no login):** https://www.fmz.com/strategy/482670 — *Multi-EMA Trend Following with Dynamic ATR-Based Exit Strategy for Cryptocurrency Trading*, author **buffalobillcody**, type Common strategy, `Created: 2025-02-19 16:50:10`, `Copy: 2`, `Hits: 930`, tags `RSI,ATR,EMA,TP/SL,CRYPTO`. This cycle the page served **648,595 bytes** over HTTPS with HTTP 200; the complete 94-line Pine v6 program (© buffalobillcody, MPL 2.0 notice, `strategy("Backtest Last 2880 Baars Filers and Exits", ...)`) is embedded verbatim in the served stream and was decoded end to end (3,626 bytes, md5 `b7aeea8d183499536b9d841ae3fcf9e3`). No login-wall bypass was performed. Only rule tokens are normalized and cited here; no large source block is copied into this repository.
- **Declaration-line census on the verbatim program:** 1 `strategy(` (percent-of-equity 2%, `backtest_fill_limits_assumption=0`, no `pyramiding`/`process_orders_on_close`/`calc_on_every_tick`/`commission` args — Pine defaults govern: pyramiding 0, confirmed-bar calculation, next-bar-open fills); 2 `strategy.entry` (`"Buy"`/long, `"Sell"`/short, `qty=tradeSize`); 2 `strategy.exit` (limit/stop from entry-bar close, no `strategy.close` — these strategy.exit calls create stop/limit brackets, but the opposing strategy.entry calls can also reverse an existing position under Pine defaults; allowTrade is true after bar_index>10 and does not prevent reversal. This derivative deliberately disables short entries, reversals and opposite-signal exits); 0 `strategy.order`; 0 `input.*` (every coefficient is hardcoded — no hidden parameters); 0 `request.*`/`security(`/`timeframe.`; 0 `volume`; 0 `nz(`/`barstate`. The `/*backtest` header pins `period: 1h`, `basePeriod: 1h`, window 2015-02-22 → 2025-02-18, with no exchange line — venue/symbol transfer is a disclosed researcher choice.
- **Explicit independent derivative, and ONLY this derivative is proposed for HB_READY:** researcher keeps the exact EMA-9/20/50 crossover construction, RSI-14 band gates, ATR-14 distance gate, linreg-slope gates, one-entry-per-UTC-day counter and the default-branch 2.5×/3.5× ATR stop/take-profit, but trades Binance **BTCUSDT spot** UTC **1h** LONG/FLAT with fixed 0.001 BTC, 10,000 USDT cash, hypothetical 0.1% fee per side, completed-bar decisions with next-completed-close MARKET fills, intrabar limit/stop converted to bar-close-evaluated MARKET exits against entry-frozen SL/TP with stop-first priority (same conversion class as merged Alpha PR #590 / FMZ 482829 record), and warmup 100. Short leg, equity-percentage sizing, Pine next-bar-open fills and `backtest_fill_limits_assumption=0` are dropped as declared changes. These alter possible trade events and economics. No original backtest performance or source-native event equivalence is claimed; the page ships no Sharpe/win-rate/return figures (scanned this cycle — none present).
- **Immutable research identity:** `FMZ:482670|buffalobillcody|pinev6-94line-md5-b7aeea8d|derived-v1-20261030|BinanceSpot:BTCUSDT:UTC1h|EMA9x20-gt-EMA50|RSI45-70|ATRdist1.1|slope+-0.2|1perUTCday|SL2.5ATR-TP3.5ATR-frozen-stopfirst|t-to-tplus1-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-side|warmup100|no-DCA`.
- **Dedup, 2026-10-30:** `main` at `02d2b9ba`, 459 root strategy records / README 459; working-tree searches for `buffalobillcody`, `Filers and Exits`, `dailyTrade`, `allowTrade`, `emaSlope`, `isTrending`, `9-20-50` return no same-source record (`2880` hits are unrelated IDs/numbers; `atrSL`/`atrTP` hits are FMZ 442506 and the RVI record — different sources; `linreg` hits are passing mentions). All 11 open research PRs inspected by source/title/branch — none uses this FMZ URL or rule. Closest pool neighbors use different signal objects: `triple-ema-volstop-tp` crosses close against EMA-7/12/21 with a VolStop trail and 4% TP (no RSI band, no ATR-distance gate, no slope gate, no daily counter, 1d); `freqtrade-crossema-28-48-stochrsi` crosses EMA-28/48 with StochRSI thresholds (different lengths, different gate family, no ATR SL/TP, no day counter); `rvi-swma-cross-ema-stack-atr-stop-target` triggers on an RVI signal cross (different oscillator, different gate). This derivative's 9/20/50-cross + RSI-band + ATR-distance + linreg-slope + one-per-day + frozen-ATR-bracket conjunction is not a paraphrase or trivial parameter variant.

## Economic mechanism

### Source-reported

A 9/20/50 EMA stack identifies trend direction (bullish when short crosses above medium while price holds above the long leg); RSI-14 bands admit only mid-momentum entries; an ATR-distance requirement keeps entries out of dead-flat tape; a 5-bar linreg slope veto blocks counter-slope entries; one trade per day caps churn; entry-anchored ATR multiples (2.5× stop, 3.5× take-profit on crypto) cut losers and bank winners. This is a qualitative hypothesis, not independently validated profitability.

### Research interpretation

Test whether an hourly EMA-9/20 cross, admitted only when momentum (RSI), displacement (ATR distance) and slope (linreg) gates all agree above the EMA-50 regime line, predicts BTC appreciation to a 3.5×-ATR target before a 2.5×-ATR stop — with at most one entry per UTC day. The derivative measures only this frozen bracket; it cannot speak for the source's forex branches, short leg, equity sizing or Pine fill timing.

## Signal

- Input: strictly chronological, **completed** UTC Binance Spot BTC-USDT `1h` candles indexed `t=0,1,...`; use `O/H/L/C[t]`. Reject missing/duplicate/gapped hourly bars, nonfinite/nonpositive prices, or any candle with `H<max(O,C)`, `L>min(O,C)`, `L>H`. Reject/abort invalid research segment; never synthesize prices, forward-fill signals, or silently skip a broken bar. Volume is never read (source reads none).
- **Researcher-pinned arithmetic (own executable rule; Pine seed bit-identity not claimed):** `EMA_N` recursively with `α=2/(N+1)`, seeded by the SMA of the first N closes, first valid at index N−1 (`E9`,`E20`,`E50`). `RSI14` via Wilder RMA of gains/losses seeded by SMA, first valid at 14. `ATR14` via Wilder RMA of true range `max(H−L,|H−C[t−1]|,|L−C[t−1]|)`, first valid at 14. `LR[t]` = least-squares endpoint over `E50[t−4..t]`: slope `m=Σ(j−2)(x−x̄)/Σ(j−2)²`, `j=0..4`, endpoint `x̄+2m`. Any undefined input makes the dependent value undefined; a gate on undefined is false, never imputed.
- **Entry conjunction (all on completed bar `t`, strict inequalities — equality never fires):** FLAT, no pending, `t>=100`, UTC-date(`t`) ≠ last-entry-signal UTC date, `E9[t−1]<=E20[t−1]` and `E9[t]>E20[t]` (fresh cross), `45<RSI[t]<70`, `C[t]>E50[t]`, `C[t]>E20[t]`, `|C[t]−E50[t]|>1.1×ATR[t]`, `LR[t]>−0.2`. On fire: queue exactly one BUY of 0.001 BTC for `t+1`; freeze `SL=C[t]−2.5×ATR[t]`, `TP=C[t]+3.5×ATR[t]`; require finite `ATR[t]>0` and strict `TP>C[t]>SL`, else queue nothing. Record last-entry-signal UTC date at queue time (mirrors the source counter incrementing on the signal bar).
- **Exit (LONG, no pending, first eligible bar strictly after the BUY-fill bar):** on completed bar `t` with `u=t−1`: if `C[u]<=SL` queue one full-position SELL (stop, checked **first** — pinned stop-first priority when one close breaches both); else if `C[u]>=TP` queue the same SELL (take-profit). Fill at `t+1` completed close. No opposite-signal exit, no trailing (levels frozen at entry), no time exit.
- **Warmup:** bars `0..99` update indicators but cannot queue or fill. First eligible signal `t=100` (covers EMA-50 seed at 49, RSI/ATR at 14, linreg comparability at 53, with margin). First fill `t=101`.
- **State:** FLAT, BUY_PENDING, LONG, SELL_PENDING; exactly one position and one pending order at most. A queued action on `t` attempts one historical fill at `t+1` completed close; process that fill first and do **not** generate a new order on the fill bar, though indicators still update. On BUY fill enter LONG; on SELL fill become FLAT. No re-entry without a fresh cross after flat, no pyramiding, simultaneous positions, short, hedge, borrowing, DCA, safety orders, partial exits, dynamic sizing, independent cooldown beyond the UTC-day counter, or forced end-of-sample liquidation. An unfilled end-of-sample pending order remains unfilled and is reported as such.
- **Risk and disabled behavior:** no protective stop beyond the frozen 2.5×-ATR bracket, no trailing, no time exit, no discretionary override. The frozen bracket is the only risk mechanism; gap risk across hourly closes jumping over both levels is real and undisguised (sequential closes apply in order; a single close beyond both exits as a stop under pinned priority). Loss and indefinite holding (if neither level is ever close-breached) are possible; no hidden executor SL/TP defaults.
- **Pinned dead source elements (never decision-read, disclosed):** `atr50` (SMA-50 of ATR), `atrFilter=true`, `allowTrade` (≡ true once `bar_index>10`, always true post-warmup), equity-percentage `tradeSize`, `label.new`/`alert(`/`plot(` display calls, the five forex `switch` branches (BTCUSDT takes the `=>` default — no variant choice exists), the source `/*backtest` window/venue. The short-leg `sellCondition`/`"Sell"` entry and its mirrored bracket are disabled, not adopted.

## Required data

Single Binance Spot `BTC-USDT` UTC hourly OHLC series, validated for completeness and chronological availability. All gates derive from validated O/H/L/C only. Only completed-bar indicator values and the fixed-fee cash ledger are decision-critical. No funding, order book, open interest, volume, cross-market synchronization, alternate timeframe, or private feed is required. Historical MARKET fill prices must be actual validated next-bar close data, never the backtesting provider's missing-price fallback.

## Execution assumptions — demonstrated bounded pinned-engine research path

- **Pinned engine:** Hummingbot package `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. The pinned `hummingbot/VERSION`, Binance spot candles `constants.py` (993 bytes), `binance_spot_candles.py` (3,924 bytes), `order_executor_simulator.py` (3,913 bytes) and `backtesting_data_provider.py` (8,823 bytes) were byte-fetched and directly read at this pinned commit this cycle (sizes identical to prior independent review); `backtesting_engine_base.py` verified: `simulate_execution` prepares rows then advances `update_state(row)` before controller `determine_executor_actions()`; `BacktestPositionHold` nets buys/sells with gross realized PnL separate from fees. Prior independently reviewed representative primitive is Alpha PR #414; no wheel rehash or candidate-specific backtest was run.
- **Real data path:** `BinanceSpotCandles.INTERVALS` includes `1h`; Binance REST `/api/v3/klines` parser takes the actual Kline opening timestamp (`row[0]`). A candle's stored `timestamp=T[t]` is **open time**; its `H/L/C` are decision-available only after `T[t]+3600 seconds` for a complete UTC hour. The candidate's own controller must reject incomplete last bars, gaps and invalid prices **before** engine preparation/dropna; no missing-price `Decimal("1")` fallback (pinned `get_price_by_type` fallback re-verified this cycle and is **forbidden** here).
- **Controller/executor path:** the future dedicated controller (NOT yet implemented) will implement the EMA/RSI/ATR/linreg state, UTC-day counter and one-bar pending action. `OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),execution_strategy=MARKET,price=None,leverage=1,position_action=OPEN/CLOSE)`. SELL size equals the recorded base inventory. `OrderExecutorSimulator.simulate` for MARKET fills on the first supplied row at its actual `close`, sets `filled_amount_quote=amount*close`, `cum_fees_quote=trade_cost*filled_amount_quote`, and terminates `POSITION_HOLD`; `BacktestPositionHold` nets buy/sell and tracks gross realized PnL separately from fees. No limit/maker/intrabar fill or unverified cross-asset path is required.
- **Exact causal fill mapping:** decide at `T[t]+3600` using data through completed bar `t`; dispatch the stored order only on the `t+1` row, and model a retrospective full fill at actual `C[t+1]`, effective `T[t+1]+3600`. The row's opening timestamp is not misrepresented as fill availability. Do not use `C[t+1]` or indicators recomputed on `t+1` to decide at `t`; the `t+1` indicator state may update but does not create another action on the fill bar. This is an **idealized historical next-completed-close** convention, not live close-order timing or a live close-order guarantee. No claim equates any close with any neighboring open.
- **Exact modeled cash/inventory ledger:** initial cash `10000 USDT`, BTC inventory 0, fixed `Q=Decimal("0.001")`, hypothetical quote fee rate `f=Decimal("0.001")` per executed side (the source declares no commission; this fee is a researcher input, not a source fact). On BUY at actual close `P`, require `cash >= Q*P*(1+f)`; otherwise consume BUY intent without a fill, stay FLAT, require a new cross (the UTC-day stamp is still consumed — the source counter increments on the signal bar regardless of fill). Successful BUY: `cash -= Q*P*(1+f)`, `base += Q`. SELL requires `base==Q`; successful SELL: `cash += Q*P*(1-f)`, `base=0`. Invalid inventory or nonfinite/absent price aborts, not a fabricated fill. Round-trip fee-net quote PnL `Q*(Pexit-Pentry)-f*Q*(Pentry+Pexit)`. Controller ledger uses `Decimal` on original validated close strings, not native gross PnL as fee-net equity. On each full-fill-only modeled action pass `trade_cost=0.001` to pinned simulator; do not double-subtract fees.
- **Research economics boundary:** this is a **fixed idealized full-fill** historical Spot model. Research fee 0.1% per side is a declared hypothetical input, NOT verified Binance fee tier. Zero **modeled** spread/slippage is an explicit idealization, not an observed zero. Exchange-specific lot/tick rounding, min-notional, historical order acceptance, latency, partial fills, liquidity and live fee tier are not verified or claimed compatible. Do not call `quantize_order_amount` or assert real exchange-valid orders from this model. Spot has no perpetual funding/margin/liquidation leg; do not fabricate futures funding observations. PASS only concerns this precisely bounded historical model; actual trading would require separate validation and authorization.
- **Fail closed:** reject invalid candles, undefined indicators, insufficient warmup, nonpositive/nonfinite ATR at freeze time, degenerate `TP<=C/SL>=C` freezes, missing next close, price fallbacks and contradictory pending/position states. No paper/testnet/live order path, trading, Qlib run or Hummingbot run is authorized by this record.

## Evidence

### Source-reported

First-party FMZ page (strategy 482670, buffalobillcody): EMA-9/20/50 trend stack with short-over-medium cross confirmation above the long leg; RSI-14 45–70 buy / 30–55 sell bands; 1.1×-ATR displacement gate; ±0.2 linreg-5 slope gates; one trade per UTC day (`dailyTradeCount<1` with `dayofweek` reset); default-branch 2.5×-ATR stop / 3.5×-ATR take-profit from entry-bar close with `strategy.exit` limit/stop and no `strategy.close`; hardcoded coefficients (zero `input.*`); `period/basePeriod 1h` demo header. It provides no independently verified performance and no commission model.

### Independently reproduced

Not independently reproduced. No Pine trade sequence, candidate-specific Hummingbot execution, Qlib parity, profitability, OOS or Survivor status was reproduced. The full 94-line program was decoded and read verbatim this cycle; the pinned Hummingbot **source capability** paths were directly inspected at the pinned commit; existing independently accepted primitive evidence #414 is referenced without claiming the derivative controller exists.

### Negative evidence

Pine exact seed/float bit-identity, live fill quality and the source's forex-branch behavior were not obtained or adopted. The default 2.5×/3.5× branch is deterministic for BTCUSDT (no variant was chosen). Fixed sizing, close-fill timing, close-evaluated bracket exits, UTC-day pinning and dropped short/equity/limit semantics are explicitly researcher choices. Main and open PR dedup found no same FMZ strategy ID or materially identical nine-gate conjunction. Real exchange precision, fees, fill quality and partial executions are unverified.

## Six-gate assessment — Scout proposal, not independent audit

1. **Determinism:** hardcoded EMA-9/20/50, RSI-14 bands, ATR-14 1.1× displacement, linreg-5 ±0.2 slope veto, strict-inequality fresh-cross entry, UTC-day one-entry counter, frozen 2.5×/3.5× bracket, 100-bar warmup, na-seeded pinned arithmetic, no fitted parameters.
2. **Direction:** BTC-USDT Binance Spot LONG/FLAT; mirrored short leg explicitly disabled, no borrow/leverage.
3. **Entry/exit/risk:** nine-gate cross entry, frozen-bracket close-evaluated stop-first exits, all protective/trailing/time/opposite exits explicitly disabled or absent by construction.
4. **Position:** one fixed 0.001 BTC position, 10000 USDT ledger, one pending, fill-bar no-action, UTC-day counter plus fresh-cross re-entry, no DCA/pyramiding/cooldown.
5. **Pinned engine:** actual 1h Binance spot candles, pinned controller/action/MARKET close-fill/POSITION_HOLD and quote-fee model verified from source this cycle; bounded hypothetical full-fill research accounting only, not exchange-valid orders.
6. **Causality:** all gates use completed bars only (lookbacks `t−1..t−53` available at `T[t]+3600`), warmup precedes decisions, open timestamps corrected to close availability, `t` signal → `t+1` completed-close modeled fill, no future-data decision leakage, no close/open equality claim.

`hb_ready_status: PASS` is a **Scout research admission proposal** for this independent derivative only; independent Hermes Auditor decides exact-head PASS, source-verifiable remediation or NOT_LOSSLESS. It is not proof of source-native equivalence, profitability, Qlib parity, implementation, HB Certified survivor or live readiness.

## Falsification plan

Not executed: adversarial tests for ties on every strict gate (cross/RSI/bands/slope/displacement), zero/degenerate ATR freeze, single-bar gaps over both bracket levels (stop-first check), breakdown on BUY fill bar, UTC-midnight signal/fill straddle with consumed day stamp, insufficient cash, fees, missing next close and sample-end pending order. A later representative Qlib↔Hummingbot event-level primitive parity check is required before mass screening if this path is not already covered by validated evidence; candidate-specific performance research is separate.

## Crypto portability

BTC-USDT spot 1h is an independent study selection (the source header is itself 1h crypto; venue/symbol transfer disclosed), not an HB_READY whitelist. Applying this structure to other coins/timeframes, the forex switch branches, equity sizing, Pine fill timing, house BO/SO 6/6/6, futures leverage, or new fill conventions requires separately declared research assumptions and capability checks; it is not silently the original FMZ program.

## Limitations

No Pine replay bit-identity, live fill quality, or source commission model exists. Close-evaluated bracket exits can materially lag (or entirely miss, in a never-close-breached drift) the source's intrabar limit/stop behavior. No trailing or time exit; slow bleed inside the bracket and indefinite holding are possible. The hypothetical 0.1% fee and idealized full-fill/zero-modeled-slippage Spot ledger are not exchange-realistic order acceptance or canonical realized costs. No controller implementation, candidate-specific event parity, backtest, reproduced returns or deployment exists.

## Implementation status

`not-implemented`: no strategy-specific controller, Qlib recipe or executable deployment. HB_READY research admission is not implementation approval.

## Adoption boundary

`research-only`, `not-approved`; no Paper/Testnet/Live, capital authorization or Qlib/Hummingbot run. Only independent Hermes Auditor GitHub Webhook Review may remediate/review/merge or close; only the existing signed GitHub webhook receiver performs post-merge README count bookkeeping.

## Related Wiki records

None required; no separate registry or research artifact was created.

## Sources

- FMZ primary: https://www.fmz.com/strategy/482670 — buffalobillcody, *Multi-EMA Trend Following with Dynamic ATR-Based Exit Strategy for Cryptocurrency Trading*, complete Pine v6 listing inspected verbatim 2026-10-30 (page 648,595 bytes served, code md5 `b7aeea8d183499536b9d841ae3fcf9e3`).
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently reviewed execution primitive: https://github.com/HCH725/alpha-strategy-research/pull/414
- Same stop/limit→close-evaluated conversion class: merged Alpha FMZ 482829 record / PR #590
