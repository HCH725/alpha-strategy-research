---
schema: strategy-research-record-v1
hb_ready_status: NOT_ASSESSED
title: "Crypto Multi-Factor Monthly Top-5 Rotation — concept, pending source rules and portfolio engine proof"
created: 2026-10-16
updated: 2026-10-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - multi-factor
  - cross-sectional
status: research-only
confidence: low
source_as_of: 2026-10-16
sources: []
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions: []
---

# Crypto Multi-Factor Monthly Top-5 Rotation — research concept

## Admission state

**NOT_ASSESSED. This candidate lives only on a non-main research branch and cannot merge into the PASS-only Alpha Research main.** It is intended to preserve the user's new strategy idea in the existing `strategy-research-record-v1` format without falsely asserting HB_READY. No Hummingbot/Qlib/n8n implementation, new runner, adapter, database, governance state, or unverified parity is authorized.

## Source and provenance

Primary inspiration is a user-shared screenshot from a 2026-10-16 conversation: a Taiwan-stock portfolio UI strategy titled **「台股四因子精選5檔」**. The image is a screenshot, not original Pine/Python strategy source and not an immutable public source URL; the full factor functions, dates/availability handling, fees and execution code were not supplied. A second user screenshot quotes separate FinLab/TEJ/CT financial articles and multiple other strategy examples; those **are not the source code for the first portfolio strategy**, and their reported returns cannot be imported as code or validated results.

### What the first screenshot ACTUALLY says

- Factors: **營收動能 (revenue momentum), 價格動能 (price momentum), ROE, 低波動 (low volatility)**. Rank each factor by percentiles, **sum** percentile scores, choose **top five holdings** and weight proportional to **score squared**. No screenshots of the exact underlying indicator functions, lengths, point-in-time fundamental releases or missing values exist in the supplied evidence.
- Monthly rebalance: on the **first trading day whose calendar day is >= 12**, determine the factors/rankings; **next trading day's open** executes selected purchases. Explicitly sell current holdings that fall out of top five and replace them with newcomers.
- Separate original stock-market corporate-action/liquidity rules: **持有中遇處置股，隔日開盤出場** (held security becomes a designated/disposition stock => exit at next trading-day open); exclude stocks whose 20-day average traded **cash value** is under **NT$30 million** from eligibility. **This is not a loss-cut stop**. There is no identified price-based stop-loss or take-profit rule.
- Screenshot historical backtest metrics (not independently verified and NOT applicable to crypto): total +2326.25%, annualized +34.53%, max drawdown -35.28%, Sharpe 1.43; these are NOT source formulas and have no bearing on HB_READY admission.
- No ability is claimed to reconstruct screenshot's 1,043 trades from these incomplete details.

## Economic mechanism

This is an **actual multi-asset, cross-sectional portfolio** rule: rank many liquid coins at the same confirmed decision timestamp, hold an ordered subset across multiple markets with **shared capital**, and periodically sell displaced constituents and rebalance target weights. **Do not reduce this to a single-pair RSI or momentum long-flat rule**, which would destroy its economic mechanism. One portfolio strategy may have five constituent coin holdings; the user portfolio's `maximum three concurrent strategies` is about independent strategy slots, NOT automatically a five-coin ban.

## Proposed crypto derivative — not yet frozen or approved

- Candidate research universe: the existing seven Binance USDT pairs `BTCUSDT, ETHUSDT, BNBUSDT, SOLUSDT, XRPUSDT, DOGEUSDT, LINKUSDT`, or their actually supported spot counterparts. Same membership for all rankings at decision time; exclude delisted/untradable/unavailable-history pairs without survivorship leakage.
- Preserve **one cross-sectional rebalance** monthly and the **top-5 + score-squared portfolio weights** to evaluate source-like selection rather than arbitrarily converting to top-1 or top-3. Important caveat: selecting 5 of 7 offers much weaker selection than top 5 in a broad stock universe. Whether to expand the universe is an experiment decision, not a backfilled claim about source.
- Crypto has NO corporate revenue or equity ROE. Candidate substitutes for future explicit design only (not a completed strategy): turnover/quote-volume growth as *trading-activity proxy* for revenue momentum; price return/trend strength for price momentum; risk-adjusted momentum or trend efficiency as *quality proxy* for ROE; realized volatility with reverse ranking as low-volatility factor. Proxies are *economically different* from fundamentals and must never be called original ROE or revenue.
- Required unspecified knobs, which must be defined before PASS: precise formulas/periods and factor monotonicity, scale/percentile normalization and tie-breaks, missing/zero-value handling, ranking universe eligibility, snapshot survivorship, when a coin is newly listed, top-5 replacement and reweight order, total capital fraction, fee/slippage/funding/precision assumptions, trading-day/calendar mapping (24/7 crypto has no stock market holidays), causality of quote-volume and available settlement price.
- Proposed calendar analogue, **not source-native**: compute signal after a fully closed daily candle on the 12th UTC day of each month and apply orders on a following deterministic candle/tick. The source uses a Taiwanese trading-day calendar and next-open, so equivalence must not be claimed. A 1d market-close timestamp and actual data availability are required, not a reused same-close assumption.
- Portability and risk: user campaign futures use isolated 3x/5x and BO/SO DCA as **separately disclosed downstream experiment**. This portfolio draft makes no assumption that these are free source-native features and no claim that all five market legs can share exposure/margin unmodified. The 60% three-strategy aggregate capital ceiling and single-strategy budget must still hold.

## HB_READY six-gate findings

1. **NOT_ASSESSED — signals incomplete.** Four factor names and a ranking aggregation are known, but source factor computations, their exact periods, and crypto proxies are not frozen. Cannot invent missing decision-critical rules or reuse stock ROE values on crypto.
2. **Partially known direction.** Original chooses long stock holdings; proposed long-only crypto portfolio, no short path. Venue/contract version undecided.
3. **Partially known entry/exit.** Monthly membership removal and disposition-stock exit known. Crypto's delisting/suspension analog, fills and risk/cost response under unavailable markets must be specified. Do not fabricate stop loss from the screenshot.
4. **Partially known multi-position/re-entry.** Top five and weights ∝ total_score² known; market synchronization, common capital ledger, simultaneous sell-then-buy, quantity rounding and cash shortfall handling not verified.
5. **ENGINEERING CAPABILITY GAP — not demonstrated.** Pinned Hummingbot package `20260920`, VERSION `dev-2.17.0`; matching source snapshot `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. `BacktestingEngineBase.initialize_backtesting_data_provider` can initialize controller-requested feeds for multiple instruments, and `BacktestingDataProvider.get_candles_df` uses per-connector/pair/interval keys. BUT the currently inspected `BacktestingEngineBase.prepare_market_data` advances the **controller primary** pair's feed, `update_state` sets `prices={primary_pair: row.close_bt}`, and the generic fallback `get_price_by_type` returns **Decimal('1')** when a pair price is missing. Existing `BacktestPositionHold` can key positions per connector+pair, but the recorded path has not demonstrated **synchronous per-leg prices, atomic cross-sectional decisions, shared portfolio cash/margin accounting, rebalance fills, position quantity and aggregate equity for five simultaneous legs**. A data API supporting multiple feeds is not by itself full portfolio backtest proof. Never silently treat missing prices as $1. One representative multi-pair capability validation using an already-existing engine path is sufficient before mass research; do not add a framework or second registry.
6. **NOT_ASSESSED — time availability.** Stock source fundamental updates must not leak release information into prior timestamps; crypto factor snapshots and rebalance timestamp are undefined. The 24/7 mapping and next-open/market fills need explicit versioned semantics.

## Direct repository integration path (no overengineering)

- Keep this research record ONLY on its existing non-main Git branch, status `NOT_ASSESSED`; it is **not** admitted into the root PASS-only pool. Do not open a Scout `research/*` PR pretending it is PASS; reviewer would correctly close it.
- Obtain either original first-party strategy code or a deliberately frozen, source-labeled **crypto-derived** specification of all factor formulas, selection/capital/risk rules. The screenshots alone do not supply it.
- Confirm the **one new actual engine capability**: synchronized multi-pair decision/fill/accounting and model costs under pinned Hummingbot benchmark. If missing, keep an `ENGINEERING_HOLD` under the **existing** workflow, not a new Gate or a strategy rejection. Do not adapt away the cross-sectional structure to rescue admission.
- Once source/derived rules and the single representative capability are proven, create the normal one-strategy `research/*` PR with `hb_ready_status: PASS`, independently audit the same six gates and only then exact-head merge to main. No direct write to Qlib/Hummingbot/n8n or production from this idea-record.

## Limitations

Historical +34.53% stock annualized return / Sharpe1.43 is UI-reported and does not survive porting to 24/7 cryptocurrencies; it must not appear as crypto backtest performance. Proxying fundamentals with price/volume changes the research hypothesis. Selecting 5 of 7 weakens cross-sectional selectivity. The current Hummingbot engine has only single-primary-pair simulation paths established, and actual five-leg portfolio execution is unverified. Absence of original factor code is a Gate 1 data/provenance gap. Neither issue should be concealed.

## Citations

- User-provided 2026-10-16 Taiwan-stock strategy screenshot, retained in this conversation; this GitHub text is a transcription, not a verified original first-party code artifact.
- Existing Alpha Repo policy: https://github.com/HCH725/alpha-strategy-research/blob/main/.github/HB_READY_REVIEW.md
- Pinned Hummingbot code: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
