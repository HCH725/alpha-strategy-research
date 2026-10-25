---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: LazyBear Trend Trigger Factor ±100 cross-trigger long-flat on BTCUSDT spot 1d derivative
created: 2026-10-25
updated: 2026-10-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2014-06-27
sources:
  - https://www.tradingview.com/script/wSMZKu7B-Indicator-Trend-Trigger-Factor/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# LazyBear Trend Trigger Factor ±100 cross-trigger long-flat — independent BTCUSDT spot 1d derivative

## Provenance

- **Primary TradingView publication:** *Indicator: Trend Trigger Factor*, **LazyBear**, stable public script ID **wSMZKu7B**, script numeric id **160** (`script_id_part PUB;160`): https://www.tradingview.com/script/wSMZKu7B-Indicator-Trend-Trigger-Factor/ . Page HTML fetched and read on **2026-10-25** (HTTP 200, 395,834 bytes): `<title>` confirms `Indicator: Trend Trigger Factor by LazyBear`; `og:title`/`og:description` confirm the script name, LazyBear authorship, and the author's rule lineage (`Introduced by M.H.Pee, Trend Trigger Factor is designed to keep the trader trading with the trend`); embedded JSON carries `"username":"LazyBear"`, `"publishedAt":"2014-06-27T23:27:42.279062+00:00"` (adopted as `source_as_of`), and `script_type study`. No performance number of any kind is transcribed from the page.
- **Pinned executable artifact (complete Pine block decoded end to end from the served page):** the page embeds the full script source in the `script.content` JSON field (982 bytes decoded, 34 lines, written out and read line by line this cycle). Census over the decoded block: 1 `study(` declaration (`Trend Trigger Factor [LazyBear]`, `shorttitle TTF_LB`) / 0 `strategy(` / 0 `strategy.entry` / 0 `strategy.exit` / 0 `strategy.order` / 0 `request.*` / 0 `security(` / 0 `volume` / 0 `open` / 0 `close` series reads (order logic reads `high` and `low` only) / 3 `input(` calls with pinned defaults `length=15`, `bt=100` (Buy Trigger), `st=-100` (Sell Trigger) plus display-only `markCrossovers=false` / 2 functions (`prev(s,i)` with `y=abs(round(i))`, so a negative offset can never become a future reference; `calc_ttf(periods)` returning `100*(bp-sp)/(0.5*(bp+sp))` where `bp = highest(high,periods) - prev(lowest(low,periods),-periods)` and `sp = prev(highest(high,periods),-periods) - lowest(low,periods)`). The `long_f`/`short_f` crossover flags drive plot color only — the script ships **no tradable order leg**, so entry/exit rules are taken from the author's cited rule origin below, never invented from the plot flags.
- **Rule-origin republication (prose + listings, fenced):** Stocks & Commodities December 2004 Traders' Tips page for M.H. Pee's *Trend Trigger Factor* (read via text mirror on 2026-10-25; direct fetch Cloudflare-walled, so no URL-body byte claim is made beyond the mirror read): the TradeStation EasyLanguage strategy listing pins `Length(15)`, `BuyPower = Highest(High,Length) - Lowest(Low,Length)[Length]`, `SellPower = Highest(High,Length)[Length] - Lowest(Low,Length)`, `TTF = ((BuyPower-SellPower)/(0.5*(BuyPower+SellPower)))*100`, with `if TTF crosses over 100 then Buy next bar at market else if TTF crosses under -100 then Sell short next bar at market`. The MetaStock system-test listing independently confirms the same four legs: buy order `Cross(ttf,100)`, sell-short order `Cross(-100,ttf)`, buy-to-cover `Cross(ttf,100)`, and the PaintBar prose confirms the state reading (`TTF > 100` uptrend green, `TTF < -100` downtrend red, between yellow consolidating). Formula, lengths, thresholds, and cross semantics agree exactly with the LazyBear Pine block.
- **Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly five: (1) market/frame pin `BTCUSDT` Binance **spot `1d`** (the article's bars are 15-day daily bars and neither source names a crypto market; the Pine names no market or timeframe); (2) the source short leg mapped to FLAT — the record is long-flat only, never short, never leveraged; (3) source next-bar-market fills converted to the disclosed same-bar-close research convention (see Execution assumptions); (4) an adopted **40-bar** warmup with pre-warmup bars flat by record rule (structural minimum is 31 completed bars — 30 for the first TTF value plus 1 prior TTF for the cross — see Signal); (5) fixed `0.001 BTC` spot sizing with research `trade_cost=0.001` per side replacing absent source economics. Length 15, thresholds ±100, strict cross semantics, the high/low-only feed, and the no-stop/no-target/no-trailing stance are source-native and unmodified.
- **Immutable identity:** `TV-wSMZKu7B-LazyBear-TTF-N15-xover100-xunder-100 | independently-derived-v1-longflat | BinanceSpot-BTC-USDT-1d | 2026-10-25`. Any change to signal, thresholds, market, clock, fill, or position state constitutes a different derivative.

## Economic mechanism

### Source-reported

Buy-power vs sell-power trend detection (author description plus S&C PaintBar prose): the range of the recent window (`bp`) is set against the range of the preceding adjacent window (`sp`); when fresh buying range dominates three-to-one or more the oscillator prints above +100 (uptrend), when fresh selling range dominates it prints below −100 (downtrend), and the middle band is consolidation. The tradable system is an always-in-the-market reversal: cross over +100 buys, cross under −100 sells short.

### Research interpretation

Hypothesis only: a TTF print crossing above +100 means the most recent 15-day high–low range exceeds three times the prior 15-day range on the buy side while lows hold firm — a fresh-range expansion that the source reads as trend ignition rather than exhaustion. Unlike level-breakout systems (pool `donchian-20-10`, which compares price against a prior high), this system compares **two adjacent non-overlapping window ranges against each other** and never compares price to a level; unlike normalized path-length oscillators (pool `vhf-trend-phase`, `(HH−LL)/sum|ΔC|` with a 0.4 threshold; pool `chop-zone`, ATR-sum over single-window range), no close-to-close path term exists anywhere — the construction is pure high/low range ratio with ±100 cross triggers. This is neither a tested edge nor a loss-limiting strategy: the source ships no stop, and this derivative holds a full underwater spot position through any decline that never prints a cross under −100.

## Signal

**Frozen independent derivative (Gates 1–4).** Single UTC-aligned, consecutive **86,400-second** Binance BTC-USDT spot OHLCV stream. Each bar `t` is labeled by its open timestamp `T[t]`; its complete OHLCV is available for decisions only at `T[t]+86400`. No other asset, time frame, order-book, or non-OHLCV feed.

- `Hi[t,a,b] = max(high[t-i], i=a..b)`, `Lo[t,a,b] = min(low[t-i], i=a..b)` (completed bars only).
- `BP[t] = Hi[t,0,14] - Lo[t,15,29]` (fresh 15-bar high range vs preceding 15-bar low anchor).
- `SP[t] = Hi[t,15,29] - Lo[t,0,14]` (preceding 15-bar high anchor vs fresh 15-bar low range).
- `TTF[t] = 100*(BP[t]-SP[t])/(0.5*(BP[t]+SP[t]))`. `BP+SP = 0` (all 30 highs equal all 30 lows) leaves TTF undefined for that bar — no signal, never an invented zero.
- **Entry, only if FLAT:** `TTF[t-1] <= 100 && TTF[t] > 100` (strict cross over; a print landing exactly on 100 is not an entry, and a bar already above 100 is not a re-entry).
- **Exit, only if LONG:** `TTF[t-1] >= -100 && TTF[t] < -100` (strict cross under; a print landing exactly on −100 is not an exit).
- **Same-bar exclusivity:** entry needs `TTF[t] > 100`, exit needs `TTF[t] < -100` — mutually exclusive on one bar by construction. The earliest exit is the bar after entry. Exactly one action maximum per bar; no reversal, no same-bar entry/exit.
- **State machine:** initially FLAT; first eligible decision after **40 consecutive valid completed 1d bars**. On each completed eligible bar, if FLAT test entry and create one simulated MARKET BUY of **0.001 BTC**; if LONG test exit and create one MARKET SELL of the full **0.001 BTC**. Otherwise HOLD. After a filled exit, the next eligible later cross-over may re-enter without cooldown; repeated above-100 prints while LONG are no-ops (single-position posture carried over from the always-in-market source).
- **Position/risk:** one spot LONG or FLAT, no short (source short leg mapped to flat by declared adaptation), leverage 1, no margin, no pyramiding, no DCA, no safety orders, no concurrency, no partial orders/fills, no portfolio allocation, no stop loss, no take profit, no trailing stop, no time exit, no liquidation, no maker/limit/intrabar orders, no forced final-bar liquidation. If LONG at end of dataset, hold 0.001 BTC and mark at last valid close without inventing a terminal SELL. No capital compounding.
- **Input validity:** every bar must have expected UTC 1d open-time spacing, finite positive O/H/L/C, `high >= max(open,close)`, `low <= min(open,close)`. Invalid/missing candles reset the 40-consecutive-bar warmup and suppress both entry and exit until 40 new contiguous valid completed candles; existing LONG exposure remains held, not liquidated at an invented fill. No forward filling, no price substitution, no silently spanning gaps. Indicator windows must be wholly within the current valid segment.

## Required data

Single Binance BTC-USDT spot 1d OHLCV series with exact open timestamps; the signal reads `high` and `low` only — `open`/`close` feed solely the validity gate, `volume` is read by no line. 30 completed bars for the first TTF value plus 1 prior TTF for the cross, plus margin: the conservative 40-bar consecutive warmup covers both. No cross-symbol synchronization, external model, training, future extrema, funding series, or secondary time frame.

## Execution assumptions

- **Pinned admission identifiers:** Hummingbot policy package label `20260920`, repository `hummingbot/VERSION=dev-2.17.0`; inspected **HCH725/hummingbot** at immutable commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3` (commit verified via the GitHub commits API this cycle; raw files read line-level this cycle, 2026-10-25). These are separate identifiers; no setup.py distribution version is claimed as a build digest or deployed-package proof. The claim is bounded to **the pinned commit's research simulation semantics**, not an installed container.
- **Actual data path:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` `INTERVALS` explicitly lists `1d` (line 24); `binance_spot_candles.py` line 82 parses Binance Kline `row[0]` as timestamp and `row[1..5]` as O/H/L/C/V. `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` processes rows through `update_state(row)` (`close_bt` pricing, lines 364–366) and `controller.determine_executor_actions()` with `CreateExecutorAction` routed to `simulate_executor` (lines 284–287). A strategy-specific controller/feature implementation **does not yet exist**; it must calculate the declared BP/SP/TTF formulas and preserve cross, state, and validity rules, rather than claim that the generic engine already contains this strategy.
- **Fill model:** `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` handles `ExecutionStrategy.MARKET` with the first supplied row's timestamp as fill time (lines 22–24) and that row's `close` as full-fill price (line 56), `filled_amount_quote = Q * close` (lines 59–60), `cum_fees_quote = trade_cost * filled_amount_quote` (line 62), and `CloseType.POSITION_HOLD` (lines 67–70). The intended controller issues exactly one `CreateExecutorAction` with `OrderExecutorConfig` for Binance BTC-USDT, `MARKET`, BUY/SELL, `Q=0.001 BTC`, leverage 1; the controller must maintain an immediate filled-position state rather than rely on delayed `positions_held` conversion to suppress duplicate orders.
- **Effective time and causal restriction:** the raw `timestamp_bt` is a **bar-open** label. The engine uses backward `merge_asof` and `dropna` in feature preparation (lines 466–478), which **alone do not establish data availability**. The required strategy-specific implementation must expose the current OHLCV only after the completed bar and normalize both effective decision and research fill event to `T[t]+86400`, while using the declared same-row close simulator fill. This is a **simulation convention**; it does not assert that a real order submitted after observing the closing range can execute at that exact close. A future deployment requiring next-open/intrabar/maker realism is a new, separately verified engine path.
- **Costs and position ledger:** fix research `trade_cost=0.001` (**0.1% per filled side**), full fill `Q=0.001 BTC`, with modeled BUY cash outflow `Q*P_buy*(1+0.001)` and SELL inflow `Q*P_sell*(1-0.001)`. Compute realized net PnL as gross matched SELL–BUY less **both** fill fees; mark open BTC at last valid close, carrying already paid buy fee. `BacktestPositionHold` (lines 38–70: netted base exposure, matched-volume realized PnL, accumulated fees) tracks gross position cost and accumulated fees, but native `summarize_results.net_pnl_quote` / `update_state.total_pnl` must **not** be mistaken for fee-inclusive cash/equity without reconstructing fills. The source ships no commission concept — the 0.1% rate is a researcher research-cost assumption, never a source fact. **Spot funding is not applicable**; no fictitious futures funding=0. The simulator has no separately applied slippage in this model; this means **zero modeled additional slippage**, not evidence of real zero slippage. Exchange min-notional/lot precision, partial fills, real spreads, latency, and realized commission are unverified and not represented as exchange-valid.
- **Reused representative capability:** admitted TradingView PR **#417** (ChartArt NR7, merged 2026-10-25) independently reviewed this exact pinned Binance spot 1d / MARKET-close / POSITION_HOLD research execution path, including fee-ledger limitations and event-time normalization; PRs **#421/#423** reviewed the same MARKET-close/POSITION_HOLD primitive, and PR **#433** (Coinrule MA100 dip, merged 2026-10-25) re-verified the identical 1d spot path on the same pinned commit. This is reusable **engine-path evidence only**, not proof that this new candidate was implemented, backtested, profitable, or Qlib/Hummingbot-parity tested. No novel execution primitive is introduced.

## Evidence

### Source-reported

TradingView `wSMZKu7B` page read 2026-10-25 (LazyBear authorship, 2014-06-27 publication, M.H. Pee lineage prose; full 34-line Pine block decoded from the served page: length 15, triggers ±100, adjacent-window BP/SP/TTF construction, high/low-only feed). S&C December 2004 Traders' Tips TTF section (mirror-read 2026-10-25): EasyLanguage `crosses over 100 → Buy next bar` / `crosses under -100 → Sell short next bar` with identical formulas, corroborated by the MetaStock `Cross(ttf,100)` / `Cross(-100,ttf)` system-test legs and the PaintBar state prose. No original numerical performance is transcribed or asserted.

### Independently reproduced

**None for this candidate.** The Gate-5 expressibility argument is static pinned-code inspection plus reusable independently reviewed engine-path evidence, not a strategy backtest, Qlib parity run, or independent reproduction of author metrics.

### Negative evidence

The Pine ships zero order legs — full rule provenance for entries/exits rests on the S&C article listings, not the indicator page. The S&C demo venue is TradeStation daily equities conventions, fenced and never adopted (no next-bar claim is carried into the crypto derivative). The source ships no commission, sizing, market, or crypto timeframe — all are disclosed researcher pins, never source claims. Source next-bar fills are converted to the disclosed same-bar-close research convention. The degenerate all-flat 30-bar window leaves TTF undefined by construction (recorded, not zero-filled). Research fills/fees are not real-world order economics; the strategy has no protective stop and may hold large unrealized losses while TTF oscillates inside the ±100 band.

## Falsification plan

Only after separate downstream approval, freeze this identity and compare against (a) the same ±100 cross entry with a state-hold exit (exit when `TTF[t] < 100` instead of the cross-under-−100 leg), and (b) the same construction with `length=30` and thresholds ±100, each on predetermined IS/OOS partitions without OOS tuning. Any new engine primitive requires representative Qlib/Hummingbot event-level validation before mass Qlib screening. **No backtest or trading was performed in this Scout cycle.**

## Crypto portability

Current declared instance is Binance BTC-USDT spot 1d only, without a universe restriction as an HB_READY prerequisite. A different pair/frame, derivatives funding/margin model, or BO/SO campaign overlay is a separately specified derivative or downstream research experiment; none is silently incorporated here.

## Limitations

PASS in frontmatter is a **proposed six-gate research admission claim pending independent Hermes Auditor review**, not an auditor's decision. No lossless source-native equivalence is claimed for market, frame, fills, sizing, or costs (all disclosed derivatives); no independently reproduced returns; no deployment build digest; no live fill precision or slippage validation; no Qlib parity; no survivor or production approval. Exact package identity remains a boundary; reviewer must not invent a package-to-commit mapping.

## Implementation status

`not-implemented`: strategy-specific controller and data-gap/feature logic are not committed or deployed. Pinned simulator primitives were read only.

## Adoption boundary

`status: research-only`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review alone owns source-fact remediation, exact-head PASS merge or NOT_LOSSLESS close. This record does not authorize Paper, Testnet, Live, Qlib/Hummingbot backtests, n8n, containers, cron, or other runtime changes.

## Related Wiki records

None asserted.

## Sources

- https://www.tradingview.com/script/wSMZKu7B-Indicator-Trend-Trigger-Factor/ — LazyBear, public indicator page read 2026-10-25 (title/authorship/publication-date prose; full 34-line Pine block decoded from served page HTML, 982 bytes).
- Stocks & Commodities December 2004 Traders' Tips, Trend Trigger Factor section (M.H. Pee rule origin; TradeStation EasyLanguage + MetaStock listings) — mirror-read 2026-10-25; direct page Cloudflare-walled, claimed only as mirror-read rule text, not byte-pinned.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned engine source read via raw-file fetch this cycle.
- https://github.com/HCH725/alpha-strategy-research/pull/417 — previously independently reviewed same 1d spot research execution primitive (merged 2026-10-25).
