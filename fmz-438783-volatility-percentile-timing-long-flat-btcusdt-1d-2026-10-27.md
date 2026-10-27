---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "FMZ 438783 volatility-percentile tail-gate timing BTC-USDT spot 1d long-flat derivative"
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
source_as_of: 2026-10-27
sources:
  - https://www.fmz.com/strategy/438783
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "FMZ page prose says the filter computes SPY historical volatility over the past 100 days, but the verbatim code computes stdev over a literal 10-bar window of log returns; 100 appears only as a positive scale multiplier and as the percentile window. Code governs; prose is fenced as source-reported only."
  - "Page prose claims 28-year SPY buy-and-hold backtest statistics (7.95% vs 9.92% annualized, 50.79% vs 31.57% max drawdown). Those numbers belong to a different market, period and sizing regime and are NOT adopted; they are fenced as source-reported claims only."
  - "Original Pine authorship is Sunil Halai's SPY buy-and-hold regime-filter demo; the FMZ stanza ports it to Futures_Binance BTC_USDT 1d, and this record further adapts venue to Binance spot. Each leg of that chain is disclosed; no lossless cross-market equivalence is claimed."
  - "The FMZ public page requires login for the full Pine block, but its public text already exposes the rule tokens (author, percentile_nearest_rank, stdev(log, period 1d, Futures_Binance) and both parameter defaults. The verbatim code used here comes from the immutable mirror fmzquant/strategies@7853bb2 (blob 8f263210, 6,759 bytes, byte-verified), not from page scraping."
---

# Volatility-percentile tail-gate market timing — BTC-USDT spot 1d long-flat derivative

## Provenance

**FMZ primary source:** ChaoZhang, *基于历史波动率的市场定时策略 / Volatility-Filtered-Market-Timing-Strategy*, FMZ numeric ID **438783**, first-party page https://www.fmz.com/strategy/438783 . Inspected 2026-10-27: HTTP 200, 749,800 bytes, author ChaoZhang, last-modified 2024-01-15, public parameter panel showing `v_input_1 = 95` (Upper percentile filter) and `v_input_2 = 100` (Lookback period), and public page text containing the rule tokens (`Sunil Halai`, `Beat The Market`, `percentile_nearest_rank`, `stdev(log`, `period: 1d`, `Futures_Binance`). The full Pine block sits behind the FMZ login wall (same provenance shape as previously admitted FMZ records).

**Immutable verbatim code lineage:** mirror `fmzquant/strategies@7853bb2bf262c4567ac238d3552d97f0e50cb801`, file `基于历史波动率的市场定时策略Volatility-Filtered-Market-Timing-Strategy.md`, Git blob SHA `8f263210d6384b25810159b9c3c7761091990f07`, 6,759 bytes. Blob SHA and size confirmed via the GitHub contents API at the pinned commit AND by local `git hash-object` byte-equality. The file carries the complete Pine v4 program (lines 121-137): `@version=4` strategy `Simple way to beat the market [STRATEGY]` (MPL-2.0, `// @author Sunil Halai`), `initial_capital=100000`, `default_qty_type=strategy.percent_of_equity`, `default_qty_value=100`, `currency="USD"`, inputs `upperExtreme=95` / `lookbackPeriod=100`, `annual=365`, timeframe branch `per`, `hv = lookbackPeriod * stdev(log(close/close[1]), 10) * sqrt(annual/per)`, `filtered = hv >= percentile_nearest_rank(hv, 100, upperExtreme)`, and the `if(not(filtered)) strategy.entry("LONG", strategy.long) else strategy.close("LONG")` decision. Declaration line contains no `pyramiding`, `process_orders_on_close`, `calc_on_every_tick` or commission; body contains no `strategy.exit`, `strategy.order`, `strategy.short`, `stop=`, `limit=`, `crossover/crossunder`, `request.*`/`security(`, volume, or SMA/EMA calls (census-verified on the verbatim text). FMZ backtest stanza pins `period: 1d` on `Futures_Binance BTC_USDT` (2023-01-08 to 2024-01-14 window is provenance only, not adopted).

**Researcher-defined derivative v1, NOT source-native:** preserve the exact 10-bar log-return volatility construction, the 100-bar 95th-percentile nearest-rank gate, and the tail-gate long/flat decision, but trade Binance **BTC-USDT spot** UTC **1d** LONG/FLAT with fixed 0.001 BTC, 10,000 USDT cash, hypothetical 0.1% fee per side, and completed-bar signal to next completed-bar-close MARKET fills. This drops source futures leverage/funding, percent-of-equity sizing, and any Pine-default same-bar order semantics. These choices **materially change** original trade economics. Only the page's MIT-style/MPL-2.0 rule logic is normalized and cited; no large source block is copied into this repository.

**Frozen independent identity:** FMZ:438783|ChaoZhang|mirror-7853bb2-blob-8f263210|derived-v1-20261027|BinanceSpot-BTC-USDT-UTC1d|hv100xstdev10-logret-annual365-per1|pct95-nearest-rank-100|tailgate-entry-notfiltered-exit-filtered|t-to-tplus1-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-each-side|warmup109. Any decision-critical alteration creates a new derived version, not a silent update.

## Economic mechanism

A buy-and-hold long book is gated by the position of current 10-bar log-return volatility inside its own trailing 100-bar distribution. When volatility sits in the top 5% tail (at or above the 95th percentile), the position is closed; otherwise it is held or re-established. This tests whether exiting during volatility-tail regimes reduces drawdown versus passive holding. It is a variance-tail sensor, not a price-level breakout: no highest/lowest, channel, price band, or moving-average level is traded. No profitability assertion is made; an unprotected long book can suffer substantial losses, and tail-gate exits arrive one bar late by construction.

## Signal

1. **Input and availability:** one chronological, contiguous sequence of actual Binance BTC-USDT spot UTC **1d** candles indexed t=0,1,... . Native opening time T[t] must be UTC midnight-aligned and T[t+1]-T[t]=86400 seconds. Require finite positive O,H,L,C, H>=max(O,C), L<=min(O,C), and finite nonnegative base volume V. Reject duplicates, gaps, out-of-order bars, missing/zero/nonfinite observed close or incomplete candles; never interpolate or forward-fill. Completed bar t is available at E[t]=T[t]+86400, not T[t]. Use float64 chronological arithmetic with no intermediate rounding.
2. **Log returns:** r[i]=ln(C[i]/C[i-1]) for i>=1. If any C<=0 or nonfinite, abort the research segment.
3. **Volatility (t>=10):** s10[t]=population stdev of {r[t-9..t]} (10 values, Pine `stdev` biased convention dividing by N). hv[t]=100*s10[t]*sqrt(365/1). The `100` is the literal `lookbackPeriod` default and `1` is the `per` value of the fixed-1d branch (`timeframe.isdaily and multiplier==1`); both are positive scale multipliers, hence decision-inert, and are kept literally for source fidelity. If s10[t] is nonfinite or <=0, abort the segment.
4. **Percentile gate (t>=109):** Q95[t]=95th order statistic (1-based; zero-based index 94) of {hv[t-99..t]} sorted ascending (100 values, current bar included, matching Pine `percentile_nearest_rank` nearest-rank semantics ceil(95/100*100)=95). filtered[t]=(hv[t]>=Q95[t]); equality filters (closes/flat). This is a pure threshold comparison, not a cross function; no tie-break beyond the stated `>=`.
5. **Warmup:** bars t=0..108 are **109 completed-bar no-trade warmup** (hv needs t>=10; the 100-value percentile window needs t-99>=10, i.e. t>=109). First eligible decision is t=109.
6. **Entry:** when FLAT with no pending action, t>=109, t strictly later than the last SELL-fill bar, and !filtered[t], queue exactly one BUY. Dispatch on row t+1 only, independently of that row's signal, and model a full 0.001 BTC MARKET fill at its **actual observed completed close** C[t+1], effective E[t+1]. No t+1 price or indicator is used to decide at t. If row t+1 does not exist, leave unfilled. Require cash >=Decimal("0.001")*Decimal(str(C[t+1]))*(1+Decimal("0.001")); insufficient funds or ambiguous/missing fill aborts rather than assuming borrowing.
7. **Exit:** when confirmed LONG and no pending action, on the first eligible completed bar u after the BUY-fill bar with filtered[u], queue a full 0.001 BTC SELL for row u+1 at actual observed C[u+1], effective E[u+1]. No stop, target, trailing, time exit, MA/ADX confirmation filter, or protective intrabar order is present (the page's suggested MA/ADX add-ons are explicitly NOT adopted).
8. **State and priority:** exactly FLAT, BUY_PENDING, LONG, SELL_PENDING; one position and one pending action maximum. The source `if/else` makes entry and exit mutually exclusive on the same bar, so no tie-break is needed. On a pending/fill bar ignore new order signals but continue updating hv/Q95. On confirmed SELL, return to FLAT using the independent confirmed-fill inventory ledger and record last SELL-fill bar. Re-entry requires only a later !filtered bar while FLAT (no cooldown; the source re-enters whenever not filtered). Never BUY and SELL on the same bar. If a fill fails, is partial, duplicated, stale or cannot be reconciled, abort the segment. At sample end, an unfilled pending signal remains unfilled; open inventory is marked only to the last actual completed close and not fictitiously liquidated.
9. **Disabled:** source futures leverage/margin/funding, percent-of-equity sizing, Pine same-bar order semantics, short/borrow leg (none exists in source), stops/targets/trailing/time exits, suggested MA/ADX/ML add-on filters, pyramiding, DCA/safety orders, simultaneous markets/shared capital, partial exits, dynamic sizing/compounding, limit/maker/next-open fills, intrabar triggers, discretionary overrides, hidden executor risk defaults and forced end-of-sample close.

## Required data

Only one real Binance BTC-USDT spot 1d OHLCV feed, no fitted models, external symbols, cross-asset shared capital, funding, order book, non-OHLCV features, second timeframe or future extrema. All indicator inputs at decision t are from bars <=t completed by E[t]. A strict input validity and continuity check must precede the pinned engine's feature merge/dropna; if data cannot satisfy it, fail closed. Native Binance kline timestamp is the **open** time, never the completed-close availability or economic fill time.

## Execution assumptions

**Pinned source-code benchmark inspected via immutable raw files at HCH725/hummingbot commit 8b0e067e80ab62f10846d518dcb5a8218527ddb3 on 2026-10-27:** package label **20260920**, `hummingbot/VERSION` = **dev-2.17.0**. Tree-verified sizes (993 / 3,924 / 39,071 / 8,823 / 3,913 bytes) match prior independent review; raw contents re-verified this round.

- **Data:** pinned `BinanceSpotCandles` constants declare the **1d** interval and read Binance REST `/api/v3/klines` opening timestamp plus actual OHLCV. Strict full-bar availability/continuity must be enforced before any feature dropna; a missing price is never substituted.
- **Controller/action path:** `BacktestingEngineBase.simulate_execution` iterates completed rows, calls `update_state(row)`, then `controller.determine_executor_actions()`, simulating CreateExecutorAction. A future minimal candidate-specific controller (not yet materialized) must retain filtered/hv/Q95 state and FLAT/LONG/pending state and send the precommitted t signal on t+1 via OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY or SELL,amount=Decimal("0.001"),position_action=OPEN or CLOSE,execution_strategy=MARKET,price=None,leverage=1). The presence of this API is **not** alone the compatibility proof.
- **Observed fill primitive:** pinned OrderExecutorSimulator MARKET path uses the **first supplied row's actual close** (`first_close = df_filtered['close'].iloc[0]`), not next-open or a fabricated price, computes float(amount)*entry_price as filled quote and trade_cost*quote as fee, then returns CloseType.POSITION_HOLD. Dispatch at t+1 produces the declared idealized t+1 completed-close fill. It is not an achievable post-close live order guarantee; economic timestamp is E[t+1], even though native row timestamp is T[t+1].
- **Position and economics:** BacktestPositionHold aggregates BUY/SELL gross exposure and fees separately; native gross realized PnL is not net research PnL. Keep complete confirmed-executor history (terminated_executors_window=None or equivalent) and a separate Decimal research cash/inventory ledger independent of BacktestPositionHold.is_closed. Start cash=10000 USDT, BTC=0; each confirmed BUY: cash -= Q*P*(1+f), inventory +=Q; each confirmed SELL: cash +=Q*P*(1-f), inventory -=Q, with Q=Decimal("0.001") and f=Decimal("0.001"). Net roundtrip realized =Q*(Ps-Pb)-f*Q*(Pb+Ps); record fees separately. This **0.1% quote-notional fee per side is hypothetical**, not a verified Binance fee tier; spot funding is not applicable, not invented perpetual funding=0. No compounding.
- **Float/Decimal precision boundary:** native simulator computes quote in float; BacktestPositionHold re-derives base quantity from Decimal(quote)/price and checks net_amount_base==0 exactly. Opposite equal configured amounts can leave sub-atomic dust; its is_closed flag and positions_held are **not** used as the derivative's authoritative FLAT/LONG or cash ledger. Confirmed OrderExecutorConfig amount and full-fill evidence determine exact research inventory Q; compare engine-derived residual to expected inventory only diagnostically with absolute tolerance 1e-12 BTC and abort if greater. This tolerance is a **researcher-declared diagnostic**, not an engine patch, live lot precision, or silent rounding of an order. Earlier independently reviewed Alpha PRs #519/#529/#530 record bounded synthetic primitive exercises at Q0.001, fee 0.001 and 1e-12 diagnostic tolerance; this record reuses that bounded pure-research primitive. No candidate-specific backtest or new primitive test is claimed here.
- **Pure-research precision contract:** deliberately no exchange lot/tick/min-notional/available-live-balance acceptance gating is claimed. This is an idealized fixed-quantity historical model, not an exchange-acceptable order assertion. Exchange trading rules, liquidity, spread, actual slippage, live fee tiers and real fills are out of scope; they must be independently verified before any deployment. The engine's BacktestingDataProvider.get_price_by_type fallback Decimal("1") on missing prices (line 140, re-verified this round) is **forbidden**; missing/nonpositive actual close, ambiguous full-fill, unbounded dust or incomplete fee/position ledger aborts the research segment.

## Evidence

### Source-reported

FMZ page prose (100-day SPY volatility narrative; 28-year 7.95%-vs-9.92% return and 50.79%-vs-31.57% drawdown claims) is fenced as unverified vendor claims on a different market and sizing regime. It is **not** adopted as evidence for this BTC-USDT spot derivative. The FMZ backtest stanza window (2023-01-08 to 2024-01-14) is provenance only.

### Independently reproduced

No strategy backtest, Pine event parity, realized market fills, profits, Qlib parity, OOS, Survivor or HB Certified results. This cycle directly inspected the immutable pinned Hummingbot feed/controller/action/MARKET/POSITION_HOLD/fee source paths and reused prior independent primitive evidence (#519/#529/#530), not a candidate-specific test or installed-binary hash. Prior primitive validation does not imply that an unimplemented dedicated controller already exists.

### Six-gate proposed PASS — independent Hermes Auditor decides

1. **Determinism:** exact 10-bar log-return population-stdev volatility, literal 100x/365/per-1 scale, 100-bar 95th-percentile nearest-rank gate with stated `>=` equality, if/else mutual exclusion, float64, warmup and priority.
2. **Direction:** BTC-USDT spot LONG/FLAT; no short leg exists in source and none is added.
3. **Entry/exit/risk:** !filtered BUY, filtered SELL; no source stop/target/trailing/time leg exists and all hidden defaults are expressly disabled.
4. **Position:** cash10000/Q0.001/fee0.001, single pending and inventory ledger, fail-closed fill reconciliation, re-entry on any later !filtered bar, no DCA or concurrency.
5. **Pinned compatibility:** actual 1d Binance spot feed, controller/action/next-row MARKET actual close, POSITION_HOLD gross-plus-fees and independently declared Decimal net ledger, pure-research precision/dust boundary; no unsupported next-open, intrabar, MTF or futures funding claim.
6. **Causality:** t>=109 completed-bar decision on inputs from bars <=t, t+1 completed-close fill effective E[t+1], opening timestamp not mistaken for completed data, no future leakage or synthetic prices.

**Dedup:** current main at 653d5fe has 388 root strategy Markdown records; full-tree grep for `438783`, `percentile_nearest_rank`, `Sunil Halai`, `beat the market` and `volatility-filtered-market` returns zero same-source hits (the single `historical volatility` prose hit is an unrelated opening-range breakout record). Nearest pool relatives trade different objects: moreira-muir (continuous 1/sigma-squared monthly scaling, never flat), faber-gtaa (price vs 10-month SMA regime), forven-volatility-contraction (contraction breakout, two-sided), fmz-482890 (close-price quantile band, 1h), dual-thrust (opening-range breakout). None is a volatility self-percentile tail gate with explicit flat state. All ten open research/* PR titles/bodies plus GitHub PR search for the source ID were checked; none matched. Existing root records were not re-audited individually in this Scout; #530's independent 387/387 PASS census plus the compare from its base shows only reviewed PASS additions and README bookkeeping, with no other strategy changes.

## Falsification plan

With separate authorization only, materialize the minimal candidate-specific controller and test the t=10 hv onset, t=109 first decision, `>=` equality filtering, warmup-edge suppression, pending-bar gate freezes, exact t/t+1 timing, observed prices, quote fees, separate Decimal inventory, float residual tolerance and end-of-sample treatment. Before large-scale Qlib screening of any new execution path, obtain representative event-level Hummingbot/Qlib parity. No such execution, deployment or backtest occurs in this Scout.

## Crypto portability

Native venue is already BTC-USDT (FMZ stanza Futures_Binance); this derivative moves only the venue leg to Binance spot 1d with no leverage or funding. No asset substitution is made. Porting the 95/100 gate to other spot symbols would be a new derived version with its own evidence, not covered by this record.

## Limitations

Full FMZ Pine text sits behind a login wall; verbatim code comes from the byte-verified immutable mirror, and the page's public text independently exposes the rule tokens and both parameter defaults. The nearest-rank 95th-of-100 convention is researcher-pinned to Pine's documented ceil(95/100*100)=95 semantics and disclosed in the frozen identity. The pure-research close/full-fill/fee model is not a real exchange acceptance or executable strategy implementation. Tail-gate exits are one bar late by construction and the book is almost-always-long; no performance, survivor, live or Qlib parity claims.

## Implementation status

**implementation_status: not-implemented** — research record only. **status: research-only; adoption: not-approved; approval_scope: research-only.** The proposed PASS is not self-approval: independent Hermes Auditor GitHub Webhook Review alone owns source-fact review, exact-head PASS merge or NOT_LOSSLESS close. The existing signed webhook receiver alone owns post-merge README bookkeeping. This Scout does not approve, merge, close, modify main or change any trading/backtest/cron system.

## Adoption boundary

Research-only. Not approved for Paper, Testnet, Live, Qlib mass screening, or any deployment. Downstream use requires the independent PASS review plus separate implementation and authorization steps outside this record.

## Related Wiki records

None created by this Scout.

## Sources

- https://www.fmz.com/strategy/438783 — ChaoZhang, first-party public page (author/date/parameters/rule tokens publicly visible; full Pine behind login wall), inspected 2026-10-27.
- Immutable mirror `fmzquant/strategies@7853bb2bf262c4567ac238d3552d97f0e50cb801`, file `基于历史波动率的市场定时策略Volatility-Filtered-Market-Timing-Strategy.md`, blob `8f263210d6384b25810159b9c3c7761091990f07`, 6,759 bytes, byte-verified via API and local hash-object.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — immutable pinned engine paths inspected via raw files this round.
- https://github.com/HCH725/alpha-strategy-research/pull/519 — prior independent bounded MARKET/POSITION_HOLD synthetic primitive review.
- https://github.com/HCH725/alpha-strategy-research/pull/529 — prior independent bounded pure-research execution and PASS-only census evidence.
- https://github.com/HCH725/alpha-strategy-research/pull/530 — prior independent PASS census evidence (387/387).
