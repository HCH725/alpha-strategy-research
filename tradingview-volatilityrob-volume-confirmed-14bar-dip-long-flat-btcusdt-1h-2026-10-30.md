---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "VolatilityRob 14-bar severe-dip and two-bar volume-surge long-flat — independent BTC-USDT spot 1h research derivative"
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
source_as_of: 2026-10-30
sources:
  - https://www.tradingview.com/script/9lGNg4ii-Buy-Dip-Multiple-Positions/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Volume-confirmed 14-bar severe dip — independently derived long-flat research strategy

## Provenance

**First-party TradingView source:** VolatilityRob, *Buy Dip Multiple Positions*, published 2025-07-16, public/open-source Pine Script **v5** strategy, stable TradingView script ID **9lGNg4ii**, https://www.tradingview.com/script/9lGNg4ii-Buy-Dip-Multiple-Positions/ ; first-party publication read 2026-10-30. The page gives three entry tests: current close below prior low times 0.998, current volume greater than 1.2 times mean of previous two volumes, and current close below a configurable percentage of the close N bars earlier (defaults **89%**, **N=14**). It also reports up to **20** simultaneous trades, trailing stop activation **two bars** after entry with a default **1%** per-bar rise, initial stop **85% of reversal low**, target **60% above reversal low**, and equity/risk-based sizing. Pine language version v5 is disclosed; an immutable Pine script revision hash and complete source bytes were **not** obtained. No original Pine order/fill equivalence or reported profitability is claimed.

**Explicit independent derivative, NOT source-native or a lossless Pine port.** Source-described entry thresholds and default 85%-of-reversal-low stop / 60%-above-reversal-low target *levels* are retained as research inspirations. Researcher-defined material alterations: Binance BTC-USDT unleveraged **spot UTC 1h**; LONG/FLAT only; **one** position instead of 20; fixed 0.001 BTC rather than dynamic equity/risk sizing; disable all original pyramiding and the two-bar-delayed 1%-per-bar trailing mechanism; evaluate source-inspired stop/target on **completed closes only** rather than resting/intrabar orders; signal on completed bar t, fill on the **next completed bar t+1 close** via pinned historical MARKET simulator; explicit warmup, cash ledger, hypothetical fee, failed-fill and re-entry behavior. This derivative materially changes source trade events and risk. Its PASS is **not** an assertion that the original multi-position/trailing strategy is expressible or reproduced.

**Frozen strategy identity:** TV:9lGNg4ii:VolatilityRob:2025-07-16:Pine-v5-public-prose-asof20261030 | independent-volume-dip14-close-bracket-v1:20261030 | BinanceSpot:BTC-USDT:UTC1h | C[t]<0.998*L[t-1] AND V[t]>1.2*mean(V[t-1:t-2]) AND C[t]<0.89*C[t-14] | LONG-FLAT:Q0.001BTC:cash10000USDT | signal-t:MARKET-close-t+1 | stop0.85*Lsetup:target1.60*Lsetup:close-only | no-trail:no-DCA | warmup80 | research-fee0.001/side. Any changed rule, cost, clock or market creates a distinct research revision.

**GitHub dedup snapshot:** main 16c6179b6c40793ab03653bcca4a75ebafd0e981 has a complete, nontruncated root tree of **463** strategy Markdown records; README static count **463**. Eighteen spread-across-tree strategy frontmatters were read individually, all PASS; **not** a claim of all-463 verification. Main GitHub searches for source ID 9lGNg4ii, VolatilityRob and the exact 0.998 / 0.89 thresholds returned no same-source record; all **11** open research PRs were enumerated, and open PR searches for source ID, author, and the exact 14-bar volume-confirmed dip mechanism returned none. Related admitted records differ materially: the FMZ Low-High dip strategy buys a **recovery crossover** above a prior 20-day lowest close with EMA200 and 8% target; the Coinrule dip strategy uses an MA100 gate and one-bar percentage change; the SpeculationLab outside-day fade uses a wide outside bar and three-bar time exit. This derivative instead requires a **simultaneous 14-bar >=11% fall, below-prior-low close and prior-two-bar volume surge**, followed by source-inspired reversal-low brackets. It is not a parameter-only clone.

## Economic mechanism

### Source-reported
The author proposes buying unusually sharp dips with volume confirmation and uses multi-entry, dynamic trailing risk management. The original publication does not provide independently reproduced trade-level statistics for this exact derivative.

### Research interpretation
A steep fourteen-hour decline with a fresh breakdown and relative volume spike may be an exhaustion event rather than a continuing trend. The independent long-only strategy tests whether a large upside recovery eventually compensates for infrequent, deeply adverse stop events. There is no profitability, Survivor, Qlib parity, or live-trading assertion.

## Signal

**Gate 1, reproducible signal.** Input is one genuine, contiguous, UTC-hourly Binance Spot BTC-USDT OHLCV stream, indexed t=0,1,...; O/H/L/C are finite positive numbers, H>=max(O,C), L<=min(O,C), and V is finite and >=0. Exchange timestamp T[t] is the **open** of bar t and must increase by exactly 3600 seconds; the completed candle becomes available only at E[t]=T[t]+3600. Missing, duplicated, invalid, incomplete or nonconsecutive rows abort the research run; never forward-fill, substitute a price, or let the engine's generic dropna silently conceal a gap.

For each **fully completed** bar t>=14, define:
- breakdown[t] := C[t] < 0.998 * L[t-1].
- volume_spike[t] := V[t] > 1.2 * (V[t-1]+V[t-2])/2.
- severe_dip[t] := C[t] < 0.89 * C[t-14].
- entry_signal[t] := breakdown[t] AND volume_spike[t] AND severe_dip[t].
All three comparisons are **strict**, equalities do not qualify, and only the specified current and past **completed** candles enter the decision. No smoothing, fitted parameters, alternate indicators, lookahead or intrabar condition. This exact interpretation of the published default surge percentage and prior-volume average is pinned for the derivative; the source Pine bytes were unavailable to establish identical implementation.

**Gate 6, warmup and causality.** Start FLAT with 10,000 USDT cash, 0 BTC, no pending orders and no inherited trade. The first 80 consecutive completed bars (indices 0..79) are observation-only; earliest eligible decision is t=80. No signal can execute before E[t], and a BUY generated by signal t is not historically filled until the **next complete bar t+1**, using its *observed* close C[t+1]. The fill is an idealized pinned-engine historical close-price MARKET simulation, not a promise of a tradable exchange closing auction. Do not inspect C[t+1] when deciding entry_signal[t].

## Required data

Only real Binance BTC-USDT Spot 1h O/H/L/C/base volume and exchange opening timestamps. No real taker delta, order book, secondary timeframe, cross-asset state, futures mark/index price, funding, leverage or trained model. Validate source timestamps and bar continuity **before** passing a normalized controller feature series to the pinned engine.

## Execution assumptions

**Gates 2/3/4, state and priorities.** LONG/FLAT only, no short/borrow/futures. Q=0.001 BTC per BUY, initial cash 10,000 USDT, one position maximum. States FLAT, BUY_PENDING, LONG, SELL_PENDING; one order maximum pending. No pyramiding, averaging, safety orders, BO/SO/DCA, concurrent positions, dynamic sizing, partial exits, trailing/breakeven, other stop or take-profit, time exit, leverage, margin, cooldown timer, re-entry on an exit bar, or forced sample-end liquidation. These omissions are **researcher alterations**, not source-native claims.

1. At a completed eligible t while FLAT, if entry_signal[t], queue one BUY of Q for historical close fill at completed t+1; no additional signals while pending. Record the **setup** reversal low L[t] as an immutable anchor. If no fill row exists, fail closed rather than assume an order.
2. At completed t+1, use the real C[t+1] as the idealized MARKET fill; require cash >= Q*C[t+1]*(1+f) with f=0.001. A successful full fill debits cash by that amount, sets LONG(Q), and freezes **stop = 0.85*L[t]**, **target = 1.60*L[t]**. Both are strictly positive; stop < target. If cash is insufficient or a fill is missing/rejected/partial/ambiguous, abort rather than invent financing or a fill. Even if the entry fill gaps outside the stop/target region, do not backdate a risk exit.
3. From the **next** completed bar t+2 onward while LONG, if C[j] <= stop queue one SELL Q for completed j+1 close; else if C[j] >= target queue one SELL Q for completed j+1 close; otherwise hold. Stop has priority over target (mutually exclusive for positive ordered levels). Equality triggers exit. These are **close-evaluated triggers** and **delayed close-price fills**, not guaranteed stop/limit prices or intrabar touches. Gaps can cause arbitrarily worse fills.
4. A confirmed full SELL at real C[j+1] credits cash by Q*C[j+1]*(1-f), realizes gross PnL Q*(sellClose-buyClose) and per-side research fees, and returns FLAT. Suppress any new entry on the sell-fill bar; the next completed bar may generate a fresh setup. Repeated signals while LONG are ignored. Any failed/partial/unresolved SELL aborts the research run; never assume the inventory disappeared.
5. At the predetermined sample end, an unclosed LONG is marked to the **actual** last completed close; do not fabricate a terminal sale or fee. Position, quote cash, realized/unrealized PnL and cumulative research fees are tracked deterministically and must reconcile to the executor ledger.

**Gate 5, real pinned model path.** Pinned Hummingbot distribution **20260920**, VERSION **dev-2.17.0**, immutable source **HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3**. Connected GitHub app read that commit's VERSION, Binance Spot candles constants/parser, BacktestingDataProvider, BacktestingEngineBase, OrderExecutorSimulator, and OrderExecutorConfig this cycle. BinanceSpotCandles constants include 1h; REST row[0] is **open timestamp**, rows[1..5] are actual O/H/L/C/V. BacktestingEngineBase.prepare_market_data uses historical candle rows and a backward feature merge, with dropna; input validation and close-availability normalization are required before it. Its simulate_execution updates the controller on each row and executes its CreateExecutorAction. OrderExecutorConfig supports MARKET with explicit side/amount/connector/pair; OrderExecutorSimulator MARKET fills at the first row of its supplied slice at that row's **actual close**, and books trade_cost*amount_quote. A controller must latch the t signal and submit its MARKET action on the t+1 completed row; merely supplying an unshifted t feature and filling t would violate this derivative. BacktestingEngineBase.BacktestPositionHold nets matching BUY and SELL Q, calculates matched realized PnL, remaining exposure and accumulated fees; the separate deterministic cash sufficiency guard is **researcher controller state**, not a claim that OrderExecutorSimulator automatically enforces spot wallet balances. Its price provider has a generic fallback price of 1: this path must instead take validated real close_bt, and must abort if missing; never accept that fallback. No position is opened through an unverified maker/intrabar path.

**Cost and market boundary:** f=0.001 per filled side is a **hypothetical fixed research cost**, not a verified Binance account fee, realized spread, slippage or fill. Simulator assumes full close-price fills; real exchange lot/tick filters, minimum notional, depth, latency, market impact and actual fee tier are **not verified**, and no real execution claim is made. Spot has no perpetual funding/margin cash flows; do not label absent perpetual funding as measured zero funding. Prior independently reviewed merged Alpha PR #414 records 902/902 source-to-package Python-file correspondence for package 20260920; this Scout checked the prior GitHub PR evidence but did **not** rehash the installed wheel, execute code, or claim independent package attestation. Auditor must reject Gate 5 if that provenance mapping or the effective-time/controller path cannot be corroborated.

## Evidence

### Source-reported
VolatilityRob, TradingView publication 2025-07-16, source ID 9lGNg4ii: three explicit dip/volume/lookback conditions and configurable defaults 0.998, 1.2, 89%, N=14, 85% stop level, 60%-above-low target, multi-position and trailing behavior. Source is public/open-source but complete Pine bytes and immutable revision were unavailable in the retrieved page.

### Independently reproduced
**No strategy backtest, no original-Pine event parity, no Qlib/Hummingbot run and no performance statistics independently reproduced.** Source-code inspection above is a bounded pinned-engine *capability* check, not an execution test. The six-gate PASS is this Scout's **research submission for independent Auditor verification**, not an independent audit decision.

### Negative evidence
Original strategy's 20-position exposure, equity sizing and two-bar-started 1%-per-bar trailing cannot be claimed reproduced here. Actual Binance MARKET fills/fee tier/precision and price impact are unverified. A 60%-above-low target may be very remote; the 15%-below-low close-stop may allow severe drawdown and delayed adverse exits.

## Falsification plan

Only after separate downstream authorization and an implemented, reproducible controller: (a) verify on a small fixed real-candle tape that all three strict inequalities, 80-bar warmup, t-to-t+1 fills, pending-order suppression and stop/target priority produce exact deterministic events; (b) reconcile each fill, spot cash debit/credit, fee and position hold with the pinned Hummingbot ledger; (c) confirm no missing-data or timestamp leakage; (d) compare representative Qlib/Hummingbot event-level parity for this execution path **before** large-scale Qlib screening if it is a new unverified capability. No such test is authorized or performed by this Scout.

## Crypto portability

BTC-USDT spot 1h is this version's only pinned market; seven-coin research, alternative timeframes, leverage 3x/5x and BO/SO 6/6/6 are **optional downstream campaigns**, not HB_READY entry requirements. Any adaptation that changes events, fills, risk or costs must be declared and verified separately.

## Limitations

This is not the original Pine implementation, not an assertion of a profitable strategy, and not a live-trading approval. Close-price historical fills after signal completion are a deliberate idealization. The 89%-of-14h-close severe-dip filter and 60%-above-setup-low target can make entries/exits rare. Missing real historical candles or invalid engine/model mapping fail closed.

## Implementation status

not-implemented — no dedicated controller, executable strategy, deployment, Qlib recipe or backtest is created in this Scout cycle. HB_READY research admission is distinct from later implementation materialization.

## Adoption boundary

research-only; adoption not-approved; approval_scope research-only. No Paper, Testnet, Live, leverage, automated trade, performance or Survivor certification.

## Related Wiki records

No new Wiki record; compare admitted FMZ Low-High dip recovery, Coinrule MA100 dip, and SpeculationLab outside-day fade for distinct signal mechanics.

## Sources

- First-party TradingView: https://www.tradingview.com/script/9lGNg4ii-Buy-Dip-Multiple-Positions/ (VolatilityRob, 2025-07-16; Pine v5; consulted 2026-10-30).
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 (VERSION, Binance Spot candles, BacktestingEngineBase, BacktestingDataProvider, OrderExecutorSimulator, OrderExecutorConfig).
- Prior source/package correspondence evidence (not independently rehashed here): https://github.com/HCH725/alpha-strategy-research/pull/414 .
