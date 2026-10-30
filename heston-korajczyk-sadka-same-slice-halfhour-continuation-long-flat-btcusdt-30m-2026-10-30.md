---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Heston-Korajczyk-Sadka same-slice half-hour continuation BTC spot 30m long-flat — independent derivative"
created: 2026-10-30
updated: 2026-10-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-30
sources:
  - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1107590
  - https://insight.kellogg.northwestern.edu/article/picking_up_pennies_for_profit
  - https://www.kellogg.northwestern.edu/academics-research/research/detail/2010/intraday-patterns-in-the-cross-section-of-stock-returns/
  - https://doi.org/10.1111/j.1540-6261.2010.01573.x
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Heston-Korajczyk-Sadka same-slice half-hour continuation — BTC spot 30m independent research derivative

## Provenance

- **Primary paper (canonical identity):** Steven L. Heston, Robert A. Korajczyk, Ronnie Sadka, *Intraday Patterns in the Cross-Section of Stock Returns*, Journal of Finance 65(4):1369-1407 (August 2010), DOI `10.1111/j.1540-6261.2010.01573.x`; working-paper posting SSRN abstract `1107590` (posted 2009-06-17, revised 2010-05-27, 59 pages), DOI `10.2139/ssrn.1107590`.
- **Source facts verified first-hand this cycle (2026-10-30) from two first-party Northwestern/Kellogg pages read in full:** (a) Kellogg research detail page states the authors, the abstract finding ("significant continuation of returns at half-hour intervals that are exact multiples of a trading day, and this effect lasts for forty trading days"), that volume/order-imbalance/volatility/spread patterns do not explain it, that continuation "is more pronounced for, but not restricted to, the first and last half-hour periods", that it is not driven by firm size/systematic risk/S&P membership, and the citation `Journal of Finance (4)1369-1407`; (b) Kellogg Insight article *Picking Up Pennies for Profit* (2009-06-01) states the design (every NYSE trade 2001-2005 aggregated into half-hour intervals; each 9:30-16:00 day broken into thirteen half-hour intervals; ~1,700 stocks; 16,000+ intervals), the exact lag structure ("returns preceding in multiples of exactly thirteen intervals (e.g., 13, 26, 39, 52, etc.) showed significant correlation to the return over the current interval", e.g. yesterday 3:00-3:30 predicts today 3:00-3:30), persistence up to forty trading days with decay, the 2009 Crowell Prize (PanAgora), and the authors' own cost warnings (see Negative evidence).
- **SSRN abstract page and Wiley article page could NOT be fetched directly this cycle** (both return bot-challenge walls to unauthenticated fetches); their canonical URLs/DOIs and abstract wording are corroborated by the search-visible abstract record and fully consistent with the two Kellogg pages read in full. No PDF-only detail (regression tables, t-statistics, microstructure return construction) is used anywhere in this record; nothing below depends on an unread page.
- **Explicit independent derivative, and ONLY this derivative is proposed for HB_READY:** researcher transports the paper's documented same-clock-slice continuation to a single-asset 24/7 crypto grid (48 UTC half-hour slices/day instead of the paper's 13-slice 9:30-16:00 equity day), keeps ONLY the first documented lag (one day: 48 bars, the crypto analogue of the paper's lag-13 bar), uses simple bar return `C/O-1` (the paper aggregates transaction-price interval returns; not claimed identical), trades LONG/FLAT only (the paper is cross-sectional long-short deciles; short disabled), holds exactly one slice with a same-bar-close exit, and uses fixed 0.001 BTC / 10000 USDT / 0.1%-per-side hypothetical economics. Lag choice, slice grid, return definition, tie handling, warmup, sizing, fee, fill clock and disabled short leg are **researcher-designed**, not source-native. These alter possible trade events. No source-native event equivalence and no profitability is claimed.
- **Immutable research identity:** `HKS2010|JF65(4)1369-1407|SSRN1107590|same-slice-30m-lag48-long-flat-v1-20261030|BinanceSpot:BTC-USDT:UTC30m|samebar-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-side|warmup96|no-DCA-stop`.
- **Dedup, 2026-10-30:** `main` at `c9453ed0e44939265d8cd5635dfa395f40a2c808`, 458 root strategy records; repo-wide search for `korajczyk`, `sameslice`, `same-slice` finds only `heston-sadka-seasonal-same-month-long-flat-btcusdt-1d` (Heston-Sadka 2008 **monthly** cross-sectional seasonality on a 1d grid — different paper, different horizon, different rail). All 11 open research PRs inspected (closest: #48 Larry-Williams streak, #304 forven CCI oversold-recross — neither uses clock-slice predictors). No closed PR ever cites HKS 2010. Nearest merged shape, `bitcoin-intraday-first-last-halfhour-momentum-timing` (Gao-Han-Li-Zhou 2018), predicts the **last** half-hour from the **first** half-hour (cross-slice rail, 2 decisions/day, two-sided); this derivative predicts **each** slice from **its own** slice one day earlier (same-slice rail, up to 48 decisions/day, long-flat, 1-slice hold). Different source, different rail construction, different horizon and cadence — not a paraphrase or parameter variant.

## Economic mechanism

### Source-reported
The authors' stated hypothesis (per the verified Kellogg pages) is that autocorrelated institutional fund flows and investors' daily demands for immediacy at the same times each day induce predictable same-clock-slice return continuation; the effect decays but persists ~40 trading days and is not explained by volume, order imbalance, volatility, spreads, size, beta or index membership. The authors explicitly warn the magnitudes are tiny versus execution costs for small traders (see Negative evidence). This is a qualitative hypothesis, not validated profitability.

### Research interpretation
Test whether yesterday's same-clock-slice BTC return sign predicts today's slice return on a 24/7 30m grid, trading only the predicted-positive slices long and sitting out the rest. The derivative deliberately discards the paper's cross-section, lags beyond one day, short leg and equity session structure; its results would not measure the paper's decile-spread effect.

## Signal

- Input: strictly chronological Binance Spot BTC-USDT UTC `30m` candles indexed `t=0,1,...` with open timestamps `T[t]`. Use raw `open[t]`, `high[t]`, `low[t]`, `close[t]`. **Sample-level validity gate (fail closed, void run on any violation):** timestamps strictly increase by exactly 1800 seconds each step; every `T[t] mod 1800 == 0`; all O/H/L/C finite and positive; `high >= max(open,close)`; `low <= min(open,close)`; `low <= high`; volume finite and non-negative. Never synthesize prices, forward-fill, or skip a broken bar.
- **Slice clock:** slice `s(t) = ((T[t] mod 86400) div 1800)` in `0..47` (UTC day; no DST). Predictor return for bar `t` is `r(t-48) = C(t-48)/O(t-48) - 1` computed with Decimal on validated strings; additionally require the hard alignment `T[t-48] == T[t] - 86400` exactly, otherwise the predictor for bar `t` is MISSING (never fall back to another lag).
- **Bias (decided for bar `t` from data complete long before it):** if predictor missing → FLAT-bias; else if `r(t-48) > 0` → LONG-bias; else (negative or exact zero) → FLAT-bias. The exact-zero tie rule is pinned researcher choice. No division beyond `C/O` with validated `O > 0`; no smoothed/seeded indicator anywhere (pure per-bar arithmetic plus a `t-48` lookup).
- **Warmup:** decision rows `t_dec < 96` are silent (grid validation and predictor history still enforced). First eligible decision is the close of row 96 (two full UTC days of history; deliberately conservative, not a paper value).
- **Entry:** at the close of eligible row `i >= 96`, if state is FLAT, bias for bar `i+1` is LONG, cash `>= Q*P*(1+f)` with `P = C[i]`, and row `i+1` exists in the validated sample, queue exactly one BUY filled at `C[i]` (= `O[i+1]`). If cash is insufficient, skip that slice with no retry; the next row re-evaluates. If row `i+1` does not exist, skip (a paired exit venue must exist; no stranded LONG is ever created).
- **Exit:** at the close of row `i`, if state is LONG, queue one full-position SELL filled at `C[i]` (one-slice hold; the exit IS the time exit). SELL requires recorded base `== Q`; any other inventory aborts the run. Exit fill is processed before the same-row entry evaluation, so a row may legally carry both fills at the same price (sell-then-buy ledger); at most one position is ever held.
- **State:** FLAT or LONG only. Dispatch fills on the decision row's own close, so no cross-bar pending state exists. No re-entry except a fresh LONG-bias slice after flat; no repeated entry while LONG; no pyramiding, simultaneous positions, short, hedge, borrowing, DCA, safety orders, partial exits, dynamic sizing, independent cooldown or forced end-of-sample liquidation.
- **Risk and disabled behavior:** no protective stop-loss, take-profit, trailing stop, alternative time exit, automatic liquidation, session filter (all 48 daily slices trade under one rule, weekends included) or discretionary override. The 1-slice signal exit is the only exit. Loss and adverse selection on every slice are possible; no hidden executor SL/TP defaults.

## Required data

Single Binance Spot `BTC-USDT` UTC 30m OHLCV candle series satisfying the sample-level validity gate above. Only completed slice returns (predictor) and validated close prices (ledger fills) are decision-critical. No funding, order book, open interest, volume-derived input, cross-market synchronization, alternate timeframe or private feed is required. Historical MARKET fill prices must be actual validated decision-row close data, never the backtesting provider's missing-price `Decimal("1")` fallback (verified present in `get_price_by_type`, hence explicitly rejected here).

## Execution assumptions — demonstrated bounded pinned-engine research path

- **Pinned engine:** Hummingbot package `20260920` (retained as a label only; no package-to-commit mapping is invented — see binding note below), VERSION `dev-2.17.0` (verified from the pinned tree's `hummingbot/VERSION` this cycle), source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. The following files were directly read from the pinned commit this cycle: `data_feed/candles_feed/binance_spot_candles/constants.py` and `binance_spot_candles.py`, `strategy_v2/backtesting/backtesting_engine_base.py`, `backtesting_data_provider.py`, `backtesting/executors_simulator/order_executor_simulator.py`, `strategy_v2/executors/order_executor/data_types.py`. Prior independently reviewed representative primitive is Alpha PR #414; no candidate-specific backtest was run.
- **Real data path:** `BinanceSpotCandles.INTERVALS` includes `30m` (verified); REST `/api/v3/klines` parser takes the actual Kline opening timestamp (`row[0]` via `ensure_timestamp_in_seconds`) with O/H/L/C/V. A row stamped `T` covers `[T, T+1800)`; its OHLC is decision-available only at `T+1800`. The candidate's own controller must reject incomplete last bars, gaps, dupes, misaligned stamps and invalid prices **before** engine preparation/dropna; `prepare_market_data` additionally applies `merge_asof(backward)` plus `dropna`, which the controller must not rely on to repair rejected rows.
- **Controller/executor path:** `BacktestingEngineBase.simulate_execution` prepares rows then, per row, runs `update_state(row)` followed by controller `determine_executor_actions()`, dispatching each `CreateExecutorAction` via `simulate_executor` on `processed_features.loc[i:max_ts]` (verified lines 269-300). The future dedicated controller (NOT yet implemented) implements the slice clock, `t-48` predictor, FLAT/LONG ledger and per-row exit-then-entry dispatch. `OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),execution_strategy=MARKET,price=None,leverage=1,position_action=OPEN/CLOSE)` (fields verified in `data_types.py`). SELL size equals the recorded base inventory. `OrderExecutorSimulator.simulate` for MARKET fills on the first supplied row at its actual `close`, sets `filled_amount_quote=amount*close`, `cum_fees_quote=trade_cost*filled_amount_quote`, and terminates `POSITION_HOLD`; `BacktestPositionHold` nets buy/sell with gross realized PnL tracked separately from fees (verified file). No limit/maker/intrabar fill or unverified cross-asset path is required.
- **Exact causal fill mapping:** decide at row `i`'s close `T[i]+1800` using data complete through row `i` (predictor bar `i+1-48` completed a day earlier); dispatch exit and/or entry on row `i`; model retrospective full fills at actual `C[i]`. Entry for bar `i+1` therefore captures `[O[i+1], C[i+1]]` with `O[i+1] == C[i]` on a valid grid, and exits at `C[i+1]`. This fill convention **is** the simulator's native first-row-close behavior (dispatch row = fill row), not an extra delay idealization and not original paper timing or a live fill guarantee. Never use bar `i+1` data to decide at row `i`.
- **Exact modeled cash/inventory ledger:** initial cash `10000 USDT`, BTC inventory 0, fixed `Q=Decimal("0.001")`, hypothetical quote fee rate `f=Decimal("0.001")` per executed side. On BUY at actual close `P`: require `cash >= Q*P*(1+f)` else skip the slice; successful BUY: `cash -= Q*P*(1+f)`, `base += Q`. On SELL at actual close `P`: require `base == Q`; successful SELL: `cash += Q*P*(1-f)`, `base=0`. Invalid inventory or nonfinite/absent price aborts, not a fabricated fill. Round-trip fee-net quote PnL `Q*(Pexit-Pentry)-f*Q*(Pentry+Pexit)`. Ledger uses `Decimal` on original validated close strings. On each full-fill-only modeled action pass `trade_cost=0.001` to the pinned simulator; do not double-subtract fees.
- **Research economics boundary:** this is a **fixed idealized full-fill** historical Spot model. Research fee 0.1% per side is a declared hypothetical input, NOT a verified Binance fee tier. Zero **modeled** spread/slippage is an explicit idealization, not an observed zero. Exchange lot/tick rounding, min-notional, historical order acceptance, latency, partial fills, liquidity and live fee tier are not verified or claimed compatible. Do not call `quantize_order_amount` or assert real exchange-valid orders from this model (`initialize_trading_rules`/`get_trading_rules` load connector-side rule snapshots the pinned commit cannot fix, so no historical validity premise is available). Spot has no perpetual funding/margin/liquidation leg; do not fabricate futures funding observations. PASS only concerns this precisely bounded historical model; actual trading would require separate validation and authorization.
- **Gate-5 binding note (bounded-commit semantics):** engine evidence above binds the pinned commit's research-simulation semantics only: (a) line-level row path re-verified this cycle (`simulate_execution` order → `CreateExecutorAction` → MARKET `OrderExecutorSimulator` first-row-close with `POSITION_HOLD` netting); (b) reuses the independently reviewed representative primitive (#414) with no novel execution primitive; (c) pins per-side `trade_cost`, rebuilds fills/cash/fees explicitly, declares spot no-funding; (d) retains policy package label `20260920` as a label only with no invented mapping. Sibling PASS records are engine-path evidence only, never proof of this candidate.
- **Fail closed:** reject invalid grids, insufficient warmup, missing predictors (entry side), missing next row (entry side), missing-price fallbacks and contradictory position states. No paper/testnet/live order path, trading, Qlib run or Hummingbot run is authorized by this record.

## Evidence

### Source-reported
Heston-Korajczyk-Sadka (2010), JF 65(4):1369-1407: same-clock-slice (multiples-of-13-lags: 13/26/39/52) half-hour return continuation persisting ~40 trading days on 2001-2005 NYSE data (~1,700 stocks, 16,000+ half-hour intervals, thirteen 9:30-16:00 slices/day); volume/imbalance/volatility/spread do not explain it; strongest (but not exclusive) in first/last slices; not size/beta/S&P driven; 2009 Crowell Prize. All points verified in the two Kellogg first-party pages named in Provenance. The paper provides no single-asset rule, no crypto grid, no threshold beyond lag structure, and no performance promise.

### Independently reproduced
Not independently reproduced. No paper regression, candidate-specific Hummingbot execution, Qlib parity, profitability, OOS or Survivor status was reproduced — deliberately: any empirical count on a truncated sample risks certifying not-yet-eligible events, so this proposal carries no sample statistics at all. The pinned Hummingbot **source capability** paths were directly inspected; existing independently accepted primitive evidence #414 is referenced without claiming the derivative controller exists.

### Negative evidence
SSRN abstract page and Wiley article page are bot-walled for direct fetch (disclosed above; no PDF-only fact is used). The authors themselves warn magnitudes are tiny versus costs: Korajczyk, "This isn't useful to retail investors given the small fluctuations in returns" and "it would be difficult to profit by trading based solely on these intra-day fluctuations" — timing value accrues to large execution programs ("like picking up pennies"). The paper is cross-sectional long-short; single-asset transportability to BTC is an untested researcher assumption, stated as such. The paper's 13-slice equity day vs this derivative's 48-slice 24/7 crypto day, simple `C/O-1` vs transaction-price interval returns, and lag-48-only vs 40-day decay are disclosed breaks from the source. Up to 48 round trips/day makes the 0.1%/side research fee schedule punitive by construction. Real exchange precision, fees, fill quality and partial executions are unverified. Main plus open-PR plus closed-PR dedup found no same-paper or same-rail candidate.

## Six-gate assessment — Scout proposal, not independent audit

1. **Determinism:** contiguous-1800s UTC grid gate, `s(t)` slice arithmetic with exact `T[t-48]==T[t]-86400` predictor alignment, `C/O-1` sign with pinned zero-tie to FLAT, 96-bar warmup, no seeded/smoothed/fitted element.
2. **Direction:** BTC-USDT Binance Spot LONG/FLAT; short/borrow/margin/leverage disabled.
3. **Entry/exit/risk:** per-slice LONG-bias entry at slice open (decision-row close), full exit at slice close (1-slice signal time exit); all protective/alternative exits explicitly disabled.
4. **Position:** one fixed 0.001 BTC position, 10000 USDT ledger, FLAT/LONG only with no cross-bar pending, cash-gated skip, next-row-exists rule (no stranded LONG), fresh bias needed for re-entry, no DCA/pyramiding/cooldown.
5. **Pinned engine:** actual 30m Binance spot candles, pinned controller/action/MARKET same-bar-close-fill/POSITION_HOLD and quote-fee model verified line-level from the pinned commit; bounded hypothetical full-fill research accounting only with the #424 (a)-(d) binding disclosure, not exchange-valid orders.
6. **Causality:** open-stamp corrected to close availability (`T+1800`), predictor completed a day before use, decision-row fills only, completed-bar warmup, void-on-invalid-grid, no future-data decision leakage.

`hb_ready_status: PASS` is a **Scout research admission proposal** for this independent derivative only; independent Hermes Auditor decides exact-head PASS, source-verifiable remediation or NOT_LOSSLESS. It is not proof of source-native equivalence, profitability, Qlib parity, implementation, HB Certified survivor or live readiness.

## Falsification plan

Not executed: predictor-alignment off-by-one (wrong-day same slice), grid gap/dupe/misaligned-stamp voids, midnight slice-47→0 predictor continuity, exact-zero tie handling, missing-predictor skip, insufficient-cash skip, sample-end next-row rule (no stranded LONG), Decimal ledger arithmetic (e.g. 0.001 BTC buy 30000 / sell 31000 → gross 1.0, fees 0.061, net 0.939), fee single-counting against `trade_cost=0.001`, `Decimal("1")` fallback rejection, and 48-decisions/day fee drag. A later representative Qlib↔Hummingbot event-level primitive parity check is required before mass screening if this path is not already covered by validated evidence; candidate-specific performance research is separate.

## Crypto portability

BTC-USDT spot 30m is an independent study selection, not an HB_READY whitelist. Applying this structure to other coins/timeframes, house BO/SO 6/6/6, futures leverage, lag-averaging over 40 days, or new fill conventions requires separately declared research assumptions and capability checks; none of it is the Heston-Korajczyk-Sadka paper's strategy.

## Limitations

No paper PDF regression detail was used (and none is needed for the disclosed derivative). The 48-slice crypto day, lag-48-only predictor, `C/O-1` return, tie/warmup/cash/next-row rules, sizing, fill clock, fee and disabled short leg are researcher choices that can materially differ from any faithful paper implementation. Single-asset transport of a cross-sectional effect is assumed, not shown. No protective stop or forced liquidation; rapid same-day round trips compound the hypothetical fee drag. The hypothetical 0.1% fee and idealized full-fill/zero-modeled-slippage Spot ledger are not exchange-realistic order acceptance or canonical realized costs. No controller implementation, candidate-specific event parity, backtest, reproduced returns or deployment exists.

## Implementation status

`not-implemented`: no strategy-specific controller, Qlib recipe or executable deployment. HB_READY research admission is not implementation approval.

## Adoption boundary

`research-only`, `not-approved`; no Paper/Testnet/Live, capital authorization or Qlib/Hummingbot run. Only independent Hermes Auditor GitHub Webhook Review may remediate/review/merge or close; only the existing signed GitHub webhook receiver performs post-merge README count bookkeeping.

## Related Wiki records

None required; no separate registry or research artifact was created.

## Sources

- SSRN working-paper posting (canonical paper identity): https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1107590 — Heston/Korajczyk/Sadka, posted 2009-06-17, revised 2010-05-27 (abstract record corroborated; page bot-walled for direct fetch, disclosed above).
- Kellogg Insight first-party article (design, lags, prize, cost warnings — read in full 2026-10-30): https://insight.kellogg.northwestern.edu/article/picking_up_pennies_for_profit
- Kellogg first-party research record (abstract, authors, citation — read in full 2026-10-30): https://www.kellogg.northwestern.edu/academics-research/research/detail/2010/intraday-patterns-in-the-cross-section-of-stock-returns/
- Published version (citation corroborated; page bot-walled for direct fetch, disclosed above): https://doi.org/10.1111/j.1540-6261.2010.01573.x
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently reviewed execution primitive: https://github.com/HCH725/alpha-strategy-research/pull/414
