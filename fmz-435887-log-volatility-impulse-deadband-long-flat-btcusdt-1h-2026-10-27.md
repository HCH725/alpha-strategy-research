---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "FMZ 435887 log-volatility impulse deadband state long-flat BTC-USDT spot 1h independent derivative"
created: 2026-10-27
updated: 2026-10-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - fmz
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-12-19
sources:
  - https://www.fmz.com/strategy/435887
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Log-Volatility Impulse Deadband — FMZ 435887 state long-flat research derivative

## Provenance

**Primary publication (read 2026-10-27):** FMZ strategy **435887**, *Volatility Finite Volume Elements Strategy* (shorttitle `FVI`): https://www.fmz.com/strategy/435887. The page (`Created: 2023-12-19 15:23:59`, 771,896-byte HTML fetched 2026-10-27 without login) embeds the complete 64-line Pine v2 block (`//@version=2`, `Copyright by HPotter v1.0 22/08/2017` header, through the `plot(xMA, color=blue, title="VBF EMA")` line). The page JSON shows the handle `ChaoZhang`, but authorship is not independently confirmed, so this record identifies the source by FMZ ID + title + URL only. No license statement was found on the page and none is claimed. No source-native trade equivalence or independently reproduced performance is claimed.

**Verified source-code facts:** fixed inputs `Samples=22`, `AvgLength=50`, `AlertPct=70`, `Cintra=0.1`, `Cinter=0.1`, `reverse=false`. Per completed bar t with `hl2=(H+L)/2` and `hlc3=(H+L+C)/3`: `xIntra=log(high)-log(low)`; `xInter=log(hlc3[t])-log(hlc3[t-1])`; `xStDevIntra=stdev(xIntra,22)` and `xStDevInter=stdev(xInter,22)` (Pine biased/N-normalized stdev); `CutOff=0.1*Vintra+0.1*Vinter`; `MF=close-hl2+hlc3-hlc3[1]`; `pos=+1 iff MF>CutOff*close, -1 iff MF<-CutOff*close, else nz(pos[1],0)` (hysteresis latch, initial flat); `possig=pos` under `reverse=false`; `strategy.entry("Long")` on `possig==1`, `strategy.entry("Short")` on `possig==-1`. Text census over the pinned 64-line block: 2 `strategy.entry` / 0 `strategy.exit` / 0 `strategy.close` / 0 `strategy.order` / 0 `pyramiding` / 0 `process_orders_on_close` / 0 `request.*` / 0 `security(` / 0 `commission`. `AlertPct` occurs exactly once (its own `input` declaration: dead input) and `AvgLength` only feeds the `xMA` plot. `volume` occurs only in comments, `xVolume=volume`, `sma(xVolume,50)` and its plot: the executable order rules never read volume, so the page title's "volume" narrative is plotting/commentary, not a tradable input. The author's `/*backtest ... */` demo header (`1d` period, `1h` basePeriod, `Futures_Binance BTC_USDT`, 2022-12-12 to 2023-12-18) is provenance only, not a binding window.

**Independently derived, NOT source-native:** Retain the source's **log-range/log-typical-price 22-bar stdev cutoff**, **close-position-plus-typical-change impulse MF**, and **strict-inequality hysteresis latch** exactly. Independently freeze **Binance BTC-USDT spot 1h**, **LONG/FLAT** (source SHORT leg explicitly disabled, no borrowing, no leverage), **0.001 BTC** fixed size, **10,000 USDT** unborrowed initial cash, **100-bar** warmup, **completed-bar signal to next completed-bar close MARKET fill** (substituting for the source Pine next-tick fill), and hypothetical 0.1% fee per filled side. Source futures market, two-sided entries and Pine fill timing are excluded. These researcher choices **materially change trade events and economics**; do not attribute them to the page author or call this a lossless port.

**Frozen derived identity:** `FMZ:435887|2023-12-19|independent-v1:2026-10-27|BinanceSpot:BTC-USDT:1h|LN-RNG22|LN-TYP22|CO-0p1-0p1|MF-C-hl2-dhlc3|LATCH-strict-hysteresis-flat0|t-signal-to-tplus1-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-per-side|warmup-t100`. A change to any decision-critical rule defines a new derivative, not a silent update to this identity.

## Economic mechanism

### Source-reported

The author scales a bar-level price impulse (where the close sits inside its own range plus the typical-price change) against a volatility cutoff built from log-range and log-typical-change dispersion, entering with the impulse only when it exceeds the adaptive band and otherwise holding the previous state, so chop inside the band produces no new orders.

### Research interpretation

This independent derivative tests a unit-free impulse-versus-volatility latch: both MF and CutOff scale with price, so the comparison is quote-unit invariant. The hysteresis band is the entire risk control — there is no stop, target or timer — which makes the state machine fully describable but leaves drawdowns to be ended only by an opposite impulse. No performance assertion is made.

## Signal

1. **Inputs and clock:** one contiguous, chronological real Binance BTC-USDT spot **1h** OHLCV sequence indexed t=0,1,...; each opening timestamp T[t] must be hour-aligned and T[t+1]-T[t]=3600 seconds. Require finite O,H,L,C>0, H>=max(O,C), L<=min(O,C), H>=L, and finite V>=0 for every row (volume validated but never signal-read). Abort on gaps, duplicates, missing prices, malformed bars, unavailable last candle or out-of-order timestamps. No interpolation, synthetic price, full-sample fitting or partial candles. Bar t's completed values become available only at E[t]=T[t]+3600, not at T[t].
2. **Typical prices:** `hl2[t]=(H[t]+L[t])/2`, `hlc3[t]=(H[t]+L[t]+C[t])/3`. Float64, no intermediate rounding.
3. **Log components (natural log):** `xIntra[t]=ln(H[t])-ln(L[t])`; `xInter[t]=ln(hlc3[t])-ln(hlc3[t-1])`, requiring t>=1 and strictly positive H, L, hlc3. Any non-positive log argument invalidates bar t and aborts the research segment rather than fabricating a value.
4. **Volatility cutoff (researcher-specified closed form, Pine-biased semantics):** population standard deviation (divide by N, matching Pine v2 `stdev`) over trailing 22 values: `Vintra[t]=pstdev(xIntra[t-21..t])`, `Vinter[t]=pstdev(xInter[t-21..t])`. `CutOff[t]=0.1*Vintra[t]+0.1*Vinter[t]`. This pins the biased convention explicitly rather than inheriting any library default.
5. **Impulse:** `MF[t]=(C[t]-hl2[t])+(hlc3[t]-hlc3[t-1])`, requiring t>=1.
6. **Hysteresis latch:** `pos[t]=+1` iff `MF[t]>CutOff[t]*C[t]` (strict); `-1` iff `MF[t]<-CutOff[t]*C[t]` (strict); else `pos[t-1]`; `pos` before the first valid bar is 0 (flat, matching source `nz(pos[1],0)`). Equality on either boundary holds the prior state; it never forces a flip.
7. **Warmup/entry:** start FLAT, zero BTC and 10,000 USDT. No trading for t=0..99; first possible completed-bar decision is **t=100** (researcher-conservative; the 22-bar statistics are first exactly valid at t=22, and 100 also covers any feed-seed transient). Indicators may be computed earlier but must never backfill a position before t=100.
8. **BUY scheduling:** if FLAT, no pending order, t>=100, and t is strictly later than any prior exit-fill bar, an entry event is `pos` transitioning to a value of `+1` from a non-+1 state at completed bar t. Store exactly one BUY instruction from the t signal. Dispatch at row t+1 only; idealized historical MARKET full fill uses **observed** Close[t+1] with economic effective time E[t+1]. Never use any t+1 values to decide the t entry. If t+1 is absent, no fill. Require actual positive close, valid size/rules and cash >=Q*price*(1+f), Q=Decimal("0.001") BTC and f=Decimal("0.001"); otherwise abort the research segment rather than invent a fill.
9. **No bracket:** there is no stop/target/trailing/time exit in this derivative, matching the source block's census-verified complete absence of any risk leg. Absence here is an explicit disclosed choice, not a hidden default.
10. **Exit and priority:** while LONG and no pending order, at each later completed bar u (never on the BUY fill bar), `pos` transitioning to `-1` from a non-(-1) state schedules a full SELL at row u+1 with idealized MARKET fill at its actual observed close effective E[u+1]; deadband bars (no transition) mean HOLD. Strict inequalities on opposite sides are mutually exclusive, so no same-bar ordering assumption exists. No same-bar roundtrip.
11. **Order and re-entry state:** one position and at most one pending order. A confirmed full SELL returns to FLAT, records its fill bar and clears state; any later completed bar with a fresh transition to `+1` may re-enter, with no cooldown and no DCA. Rejected/partial/duplicate/ambiguous BUY or SELL fills, missing price, or insufficient actual data abort the research segment, not silently mutate inventory. A last-row signal without a subsequent observed candle is unfilled; at sample end mark open inventory only at last actual completed close, separately from realized PnL, with no fabricated forced liquidation.
12. **Explicitly disabled:** short/borrow, futures/perpetuals, margin/leverage/funding, pyramiding, DCA/safety orders, concurrent markets/shared capital, partial exits, dynamic sizing/compounding, maker/limit/next-open orders, intrabar stops, trailing, time exit, source Pine fill timing, volume-gated triggers, and hidden executor defaults. No simultaneous or hedged positions.

## Required data

One real Binance BTC-USDT spot 1h OHLCV feed; only O/H/L/C are signal inputs (volume is continuity-validated, never read by the rules). No external symbols, order book, futures funding, non-OHLCV data, secondary timeframes, fitting or future extrema. Validate candle continuity and all observed fill prices **before** the pinned engine's feature merge/dropna. Decisions occur at E[t], fills at E[t+1] in the idealized historical model, regardless of the native feed's opening timestamp. All indicators use only <=t completed data. Non-positive prices abort.

## Execution assumptions

**Pinned GitHub-inspected benchmark (2026-10-27):** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, package label `20260920`, `hummingbot/VERSION=dev-2.17.0`. Immutable raw-file inspection this run of `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` (993 bytes; INTERVALS declares `1h` and `1d`), `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` (MARKET path fills at the first candle's row with `entry_price` taken from that row's actual close, `filled_amount_quote`/`cum_fees_quote` accumulate, returns `CloseType.POSITION_HOLD`), `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` (`BacktestPositionHold`, `simulate_execution` calling `controller.determine_executor_actions()` with `CreateExecutorAction`), and `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py` (line 140 `get_price_by_type` missing-price fallback). Prior Alpha PR #414 reports independent package/source correspondence; no wheel/image digest rehash in this run.

- **Actual feed:** pinned BinanceSpotCandles declares `1h`; Binance REST row[0] is **opening timestamp**, row[1..5] supplies real OHLCV. No synthetic candles, inferred fill prices, or silent forward filling. `BacktestingEngineBase.prepare_market_data` can merge features and drop missing rows; a pre-engine strict continuity/validity check is mandatory.
- **Actual action path:** `BacktestingEngineBase.simulate_execution` calls `update_state(row)`, then `controller.determine_executor_actions()`, and simulates `CreateExecutorAction`. A future minimal candidate-specific controller (not yet implemented) must preserve t's latch/pending state, delay dispatch to t+1, and issue `OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),position_action=OPEN/CLOSE,execution_strategy=MARKET,price=None,leverage=1)`; no API name alone is asserted to implement this strategy.
- **Actual bounded fill:** MARKET dispatch on t+1 yields an idealized **t+1 close** fill at that row's actual close, not the source Pine next-tick fill and not an achievable live post-close market price. Native fill row timestamp is an **opening** timestamp; economic effective fill time must be normalized to E[t+1], never reported as T[t+1].
- **Position and fee ledger:** pinned `BacktestPositionHold` nets opposite BUY/SELL base quantities and reports gross realized PnL while fees accumulate separately. Maintain a persistent confirmed-fill ledger (`terminated_executors_window=None` or equivalent) and explicit research cash/inventory: BUY cash `-=Q*Pb*(1+f)`, SELL cash `+=Q*Ps*(1-f)`, net realized round-trip `Q*(Ps-Pb)-f*Q*(Pb+Ps)`. The fee `f=0.001` is a **hypothetical 0.1% quote-notional fee per filled side**, not a verified Binance fee tier. Engine float-ledger internals are not asserted equal to research-side Decimal bookkeeping; any fill/ledger ambiguity aborts the segment instead of being rounded into a fill. Never call gross engine PnL net. Spot funding is **not applicable**, not fabricated zero perpetual funding.
- **Fail-closed boundaries:** `BacktestingDataProvider.get_price_by_type` can return `Decimal("1")` on a missing price; explicitly **forbid** that fallback. Reject absent/nonpositive observed closes, invalid trading rules, unsupported precision/min-notional, partial fills and ambiguous position accounting rather than inventing economics. Simulator's idealized full fill does not prove real spread, slippage, liquidity, live minimum order/precision, dynamic fee or latency. The future controller, real execution and package binary are **not** independently validated; this record claims only the bounded pinned historical close-fill primitive.

## Evidence

### Source-reported

FMZ 435887 (2023-12-19): log-range and log-typical-change 22-bar stdev cutoff at 0.1/0.1 weights, close-position-plus-typical-change impulse, strict-inequality hysteresis latch with flat start, long entry on `possig==1` and short entry on `possig==-1`, no risk leg, dead `AlertPct` input, plotting-only `AvgLength`/volume. No original backtest result is adopted.

### Independently reproduced

**None for strategy events, profits or outcomes.** No Pine parity run, candidate-specific Hummingbot run, Qlib backtest, event-level parity, actual fills, installed package hash, OOS, Survivor or HB Certified claim. Only the **page HTML payload and the existing pinned source-code engine/data/executor/fee paths** were directly inspected via the stable FMZ URL and immutable raw files at the pinned commit. Alpha PR #414 is prior correspondence evidence, not a claim of re-execution this cycle.

### Negative evidence

Source futures market, two-sided entries and Pine next-tick fill timing are **explicitly replaced**, not source-native rules. The page title's "volume" narrative does not survive the code census: no executable rule reads volume. Idealized close fills and assumed fees do not prove exchange execution. No realistic live fills or funding are asserted.

**Six-gate proposal, pending independent Hermes Auditor:**
1. Determinism: pinned Pine v2 formulas, fixed inputs (22/0.1/0.1/false), biased-stdev closed form, strict-inequality latch with flat seed, dead/plotting-only inputs disclosed, t=100 warmup.
2. Direction: Binance BTC-USDT spot LONG/FLAT; the source short leg is explicitly disabled in the derivative.
3. Entry/exit/risk: latch transition to +1 enters, transition to -1 fully exits, deadband holds; census-verified absence of any risk leg.
4. State: fixed 0.001 BTC, one pending order/position, cash and fees, no DCA/concurrency, fresh transition after exit, abort on ambiguous fills.
5. Pinned model: directly inspected actual 1h feed, controller/action, MARKET close fill, POSITION_HOLD and fee paths; no unsupported intrabar/funding/volume assumption.
6. Causality: 100-bar warmup, t completed signal -> t+1 completed-close economic fill, inputs only <=t (plus t-1 typical), no future bars, opening timestamp never misrepresented as close availability.

**Dedup snapshot:** at `main=4853ba14c096d16cddc95026237698866f81afee`, README static pool count and root Markdown strategy count were both **384** (excluding two READMEs). Repo-wide `grep -rilE` over root `*.md` returned zero for `435887`, `xStDev`, `Cintra`, `Cinter`, `finite volume elements`, `log(high) - log(low)`, `gaussian_kde`, `find_peaks`, `kernel density`, `prominence`, `HourBased`, `buy_hour`, `dt\.hour`; `CutOff` matches were English-prose "cutoff(s)" only, verified individually. All ten open `research/*` PR titles/bodies were checked for source identity with no match (Heracles KCD-ratio, ClucMay72018, AdxSmas, forven CCI, Swift 2YMA, SSL channel, Chandelier Exit, SuperTrend flip, Gaussian StochRSI, Larry Williams). Nearest pool neighbors differ in mechanism: `p-signal-erf-dead-band-reversal` (FMZ 440338) is an erf-ratio **reversal** with slope gate, while this candidate is a log-volatility-scaled impulse **continuation latch** with no erf, no slope gate, no channel and no centerline; cumulative-flow records (`obv-ema`, `pvt-ema`, `cmf-velocity`) use volume-against-average constructions this candidate provably lacks. Existing 384 strategies were **not** exhaustively re-audited for PASS frontmatter; count equality is not represented as a full admission census.

## Falsification plan

With separate authorization, materialize only a minimal candidate-specific controller, validate the strict t/t+1 clock and actual close inputs, population-stdev window validity and boundary cases (`MF==+CutOff*C` and `MF==-CutOff*C` both hold state), positive-price log requirement, deadband HOLD persistence, post-exit re-entry, fail-closed invalid fills and fee-net position accounting. Before large-scale Qlib screening on a newly unverified execution path, obtain representative Hummingbot/Qlib event-level parity for signals, fills, fees and states. Separately assess fee-net IS/OOS performance; no such test is run by this Scout.

## Crypto portability

BTC-USDT spot 1h is researcher-selected, not an author-validated outcome or admission whitelist. Any futures, 3x/5x, DCA BO/SO 6/6/6, other coin or execution model is downstream optional research requiring a separately specified derivative and verified execution/cost/funding path. No implied transfer of results.

## Limitations

No Pine parity run; source-native equivalence unverified. Spot market, long-flat sidedness, next-close fill, fixed quantity and hypothetical fees materially differ from the source page. Idealized close fills and assumed fees do not prove exchange execution. No installed package rehash, strategy backtest, Qlib parity, profitability or live authorization. Latch-held positions have no stop: adverse trends exit only on an opposite impulse.

## Implementation status

`not-implemented`: research specification only. No controller, Qlib recipe, trading deployment, backtest, container, n8n or cron changes.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. `hb_ready_status: PASS` is **Scout-proposed**, not self-approved. Independent Hermes Auditor GitHub Webhook Review owns source-fact remediation, exact-head PASS merge or NOT_LOSSLESS close. The existing signed webhook receiver alone owns README bookkeeping after an accepted merge. Scout does not approve, merge, close or write main.

## Related Wiki records

None created or modified.

## Sources

- https://www.fmz.com/strategy/435887 — FMZ, *Volatility Finite Volume Elements Strategy* (shorttitle FVI), page created 2023-12-19; 64-line Pine v2 block inspected 2026-10-27 from the public page payload.
- https://raw.githubusercontent.com/HCH725/hummingbot/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — immutable pinned engine source (feed constants, order executor simulator, backtesting engine base, data provider), inspected through immutable raw files 2026-10-27.
- https://github.com/HCH725/alpha-strategy-research/pull/414 — earlier package/source correspondence evidence; not re-run here.
