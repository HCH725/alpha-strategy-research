---
schema: strategy-research-record-v1
title: "ETH-Leader WMA Cross-Asset Altcoin Following — TradingView Source-Code Audit"
created: 2026-09-15
updated: 2026-09-15
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
  - crypto
  - cross-asset
  - lead-lag
status: research-only
confidence: medium
source_as_of: 2026-09-15
sources:
  - "https://www.tradingview.com/script/2JLkUO07-Correlation-Strategy/"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The page says 'when WMA is falling, we go short', but the public Pine shortCondition additionally requires strategy.position_size > 0; from flat the script therefore cannot initiate a short and can only reverse an existing long."
---

# ETH-Leader WMA Cross-Asset Altcoin Following — TradingView Source-Code Audit

## Provenance

- **Primary source:** TradingView public open-source script, *Correlation Strategy*.
- **Author/page identity:** `levieux`.
- **Stable URL:** https://www.tradingview.com/script/2JLkUO07-Correlation-Strategy/
- **Published:** 2021-12-15.
- **Source inspected:** public TradingView description and the complete 165-line Pine Script v5 source exposed by the page on 2026-09-15.
- **Source license marker:** the Pine header identifies Mozilla Public License 2.0; this record does not redistribute the full script and instead normalizes the trading rules.
- **Dedup check:** repository search on 2026-09-15 found related cross-asset, lead-lag, pairs/stat-arb, BTC-dominance, and crypto information-diffusion records, but no record for TradingView source `2JLkUO07` or this specific construction: direction in the chart asset driven solely by the slope state of a 200-period WMA on a separate support asset, with support-asset-referenced exits.

## Economic mechanism

### Source-reported

The author describes a leader/follower hypothesis: a comparatively important crypto asset can be used as a directional support signal for correlated altcoins. With defaults, ETH/USDT is the support symbol and the strategy is intended for 4-hour charts. The page says that several altcoins may follow large ETH moves and reports qualitatively good backtest results on examples including DENT/USDT, BTT/USDT, FTT/USDT, and DOT/USDT; no precise performance statistics or fixed sample are supplied on the publication page.

### Research interpretation

This is a **cross-asset directional information-transfer hypothesis**, not pairs trading. The chart asset is the traded follower; ETH is the default leader. A slowly moving 200-bar WMA on the leader suppresses short-lived noise, while a persistent five-bar rise/fall state is treated as evidence that directional information in ETH should carry into the follower.

The distinct mechanism is falsifiable: if follower returns conditional on the causal ETH-WMA state do not outperform the same follower's own-price trend control, then the separate leader series adds no incremental information. The support-asset-referenced TP/SL also creates a second hypothesis—whether exit timing tied to leader displacement is useful for managing follower exposure—which must be tested separately from the entry signal.

## Signal

**Source-reported / source-code-audited defaults:**

- **Host timeframe:** source recommends 4h; the Pine requests the support symbol at `timeframe.period`, so support and chart series use the same host timeframe.
- **Support symbol:** `ETHUSDT` by default. TradingView resolves the selected public symbol through `request.security`.
- **Support source:** `hlc3`.
- **Lookback:** 200 host bars for the WMA.
- **Point-in-time setting:** `request.security(..., lookahead=barmerge.lookahead_off)`.
- **Trend state:** long condition uses `ta.rising(supportLine, 5)`; short condition uses `ta.falling(supportLine, 5)`.
- **Long entry:** within the configured test window, rising support WMA for five bars and current strategy position `<= 0` triggers `strategy.entry('Long', strategy.long)`.
- **Short entry — source-code contradiction:** the page says a falling WMA goes short, but executable `shortCondition` additionally requires `strategy.position_size > 0`. Consequently, a short cannot be opened from flat; it is reachable only while a long exists, where the short entry reverses the long.
- **Entry reference for exits:** on a long or short signal the code stores the contemporaneous `supportTicker` value, i.e. the leader's HLC3, not the chart asset's execution price.
- **Long TP:** close long when support ticker rises more than 20% above the stored support reference.
- **Long SL:** close long when support ticker falls more than 10% below the stored support reference.
- **Short TP:** close short when support ticker rises more than 15% above the stored support reference.
- **Short SL:** close short when support ticker falls more than 4% below the stored support reference.
- **Important source-code semantic issue:** the labels `takeprofitShort` and `stoplossShort` are economically inverted relative to a conventional short position. A rise in ETH triggers the code's short "take profit", while a fall triggers its short "stop loss". Because P&L is earned/lost on the chart asset rather than ETH, neither label guarantees the corresponding chart-position outcome.
- **Position size:** 100% of strategy equity.
- **Commission:** 0.1% configured in the strategy declaration.
- **Test-window defaults:** 2016-01-01 00:00 UTC through 2050-12-31 23:59 UTC.
- **Holding period:** no fixed maximum. Position persists until a qualifying reversal or support-asset TP/SL condition closes it.
- **Re-entry:** long may be entered from flat or short; short cannot be entered from flat under the inspected source.

The source is sufficiently explicit to reconstruct the executable Pine rule, but the intended economic short rule is **contested** because the page narrative and executable predicate disagree.

## Required data

- **Traded instrument:** the current TradingView chart symbol; source examples are crypto/USDT altcoins.
- **Leader/support instrument:** default `ETHUSDT`; exact venue is user-resolved in TradingView and therefore must be pinned in any reproduction rather than relying on an unqualified ticker.
- **Market type:** not fixed by the source. Spot versus perpetual is underspecified and materially affects fees, funding, and symbol identity.
- **Timeframe:** 4h recommended; other timeframes are permitted by the page but require a different support length according to the author, with no mapping supplied.
- **Fields:** chart-symbol OHLC for Strategy Tester accounting; support-symbol HLC3 for the WMA and all exit thresholds.
- **Timestamp:** 24/7 bar boundaries follow the TradingView symbol/session definition. Reproduction must pin exchange, timezone, and 4h candle boundary.
- **Point-in-time:** support series is requested with `lookahead_off`; no external publication lag is involved.
- **Missing data:** source does not specify behavior for support-symbol gaps, venue outages, delistings, or stale bars.
- **Costs:** source models 0.1% commission but does not model spread, slippage, funding, borrow, market impact, or liquidation.

## Execution assumptions

- Pine uses market `strategy.entry` / `strategy.close` calls and does not enable `process_orders_on_close`; exact Strategy Tester fill timing should therefore be reproduced using the Pine/TradingView execution semantics applicable to this script version rather than silently assuming same-close fills.
- Signal state and exit thresholds are calculated from the support asset, while actual P&L and fills occur on the chart asset. This **signal/execution instrument split** is central to the strategy.
- The support ticker is captured when the signal is generated; the chart asset's actual fill can occur at a different time/price.
- No slippage, spread, funding, borrow, latency, impact, partial-fill, leverage/margin, or liquidation model is specified beyond the 0.1% commission and 100%-of-equity sizing.
- For perpetual-futures reproduction, funding and liquidation mechanics must be added as research assumptions; they are not source-reported.

## Evidence

### Source-reported

The TradingView author qualitatively states that default ETH/USDT support parameters show good backtest results on several follower symbols including DENT/USDT, BTT/USDT, FTT/USDT, and DOT/USDT. The page supplies no precise return, Sharpe, drawdown, trade count, fixed evaluation period, slippage assumption, or out-of-sample protocol, so no quantitative performance claim is recorded here.

### Independently reproduced

not independently reproduced

### Negative evidence

- The executable short condition contradicts the prose rule: from flat, falling ETH WMA does **not** initiate a short because `strategy.position_size > 0` is required.
- Short TP/SL labels are directionally inverted with respect to ETH movement and do not map cleanly to profit/loss on the follower asset.
- Exit thresholds are measured on ETH rather than the traded asset, so a 20% ETH rise or 10% ETH fall can be a very long-horizon event on 4h data and need not correspond to the follower's realized P&L.
- The source provides only qualitative backtest language, no immutable result table or OOS evidence.
- Example `FTT/USDT` illustrates survivorship/delisting risk in follower selection; the source does not define a point-in-time universe.
- The leader ticker is unqualified by venue, creating reproducibility risk if TradingView resolves a different ETHUSDT feed.

## Falsification plan

1. **Leader incremental-value test.** Data: point-in-time 4h BTC/ETH and liquid-altcoin spot/perp bars across at least two venues. Compare the source ETH-WMA state with a follower-own 200-WMA five-bar state and a BTC-leader control. **Research-defined falsification threshold:** reject the cross-asset leader claim if ETH conditioning fails to improve net OOS Sharpe by at least 0.10 over the stronger control and the bootstrap 95% CI for incremental mean return includes zero.
2. **Narrative-vs-code short ablation.** Compare inspected executable rule (short only as long reversal) against the prose-consistent rule allowing shorts from flat. **Research-defined falsification threshold:** if conclusions change sign or Sharpe differs by >0.25, treat published qualitative performance as implementation-sensitive and not evidence for the prose strategy.
3. **Exit-instrument ablation.** Compare source ETH-referenced exits with identical percentage thresholds on the traded follower and with reversal-only exits. **Research-defined falsification threshold:** if ETH-referenced exits do not improve net OOS Sharpe or drawdown relative to both controls, reject the exit-timing component.
4. **Point-in-time universe / survivorship test.** Reconstruct historical listings and delistings rather than selecting current survivors. **Research-defined falsification threshold:** reject broad altcoin portability if median follower OOS net return is non-positive or fewer than 55% of eligible followers show positive net expectancy.
5. **Cost and venue stress.** Apply spot and perpetual fee schedules, bid/ask spread, slippage, and funding where relevant on at least two venues. **Research-defined falsification threshold:** reject practical tradability if net Sharpe is <= 0 or the strategy loses positive expectancy at 2x observed median execution costs.
6. **Parameter perturbation.** Test WMA lengths 160/180/200/220/240 and rise/fall persistence 3/4/5/6/7 bars without retuning exits. **Research-defined falsification threshold:** reject robustness if the 200/5 setting is an isolated positive island and the majority of neighboring configurations have non-positive net expectancy.

Failure means the record remains research-only and should not be promoted through implementation or adoption based on the TradingView publication.

## Crypto portability

**direct** — the source itself is designed for cryptocurrency pairs and explicitly uses ETH/USDT as the default leader for altcoin followers.

Portability is nevertheless venue- and instrument-sensitive. Spot and perpetual ETH feeds can diverge; perpetual followers incur funding and liquidation risk; crypto trades 24/7 so 4h boundary selection must be fixed; altcoin listing/delisting and venue fragmentation create survivorship and missing-data hazards; and the strength of ETH leadership may vary materially across market regimes as BTC dominance and sector leadership rotate.

## Limitations

- `contested`: prose short-entry semantics conflict with executable source.
- `not independently reproduced`.
- No precise source-reported performance figures or OOS protocol.
- Unqualified `ETHUSDT` venue identity is a reproducibility gap.
- Spot/perpetual market type is underspecified.
- No follower-universe construction, liquidity threshold, delisting rule, or capacity analysis.
- No maximum holding period.
- No slippage, spread, funding, borrow, impact, or liquidation model.
- 100% equity sizing confounds signal quality with aggressive exposure and is risk management, not alpha.
- The source's qualitative examples are vulnerable to selection and publication bias.

## Implementation status

`not-implemented`. This Scout inspected and normalized the public TradingView source only. No PyBroker/Nautilus/runtime implementation, historical reproduction, paper trading, testnet, or live execution was performed.

## Adoption boundary

`research-only`; `adoption: not-approved`; `approval_scope: research-only`.

This record is a staging research capture. It does not establish profitable alpha, authorize implementation, or permit Paper/Testnet/Live execution. The source-code contradictions must be resolved as explicit experiment variants before any later implementation decision.

## Related Wiki records

No stable Hermes Wiki Brain path was fabricated. Repository dedup search identified materially adjacent research families including crypto cross-sectional price-delay/information diffusion, cross-venue lead-lag, BTC-dominance regime switching, and crypto pairs/stat-arb records; none used the same TradingView source or this specific ETH-WMA leader-to-follower construction with leader-referenced exits.

## Sources

1. levieux, *Correlation Strategy*, TradingView, published 2021-12-15, public open-source Pine Script v5, source inspected 2026-09-15: https://www.tradingview.com/script/2JLkUO07-Correlation-Strategy/
