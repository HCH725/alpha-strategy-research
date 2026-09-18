---
schema: strategy-research-record-v1
title: "Polymarket ETH 15-Minute LateAsk: Chainlink Displacement vs Late Binary Ask"
created: 2026-09-18
updated: 2026-09-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - ethereum
  - polymarket
  - prediction-market
  - event-contract
  - chainlink
  - late-window
  - binary-market
  - lead-lag
  - execution
status: research-only
confidence: medium
source_as_of: 2026-09-18
sources:
  - "FMZ Quant strategy platform, Polymarket ETH15 LateAsk v8.10, strategy id 545782, author 发明者量化-小小梦, created 2026-07-15, page last modified approx. 2 months before capture. https://www.fmz.com/strategy/545782"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Polymarket ETH 15-Minute LateAsk: Chainlink Displacement vs Late Binary Ask

## Provenance

Public FMZ strategy page: **Polymarket ETH15 LateAsk v8.10**, strategy id `545782`, author 发明者量化-小小梦. Canonical URL: https://www.fmz.com/strategy/545782. Created 2026-07-15; page reports last modification about two months before this capture. Source reviewed as of 2026-09-18.

Repository deduplication on current `main` found no record with FMZ source id `545782` or the same normalized LateAsk rule (late-window high-ask buy on the Polymarket ETH 15-minute binary when Chainlink same-direction displacement plus a conservative win-rate estimate still clears VWAP and fees). Existing Polymarket records cover tri-transformer market-making, Binance–Polymarket HF lead-lag, binary mean-reversion cost sensitivity, NegRisk conversion arb, protocol-finality redemption carry, and favorite-longshot bias — all materially different mechanisms.

## Economic mechanism

### Source-reported

The FMZ description treats Polymarket 15-minute ETH up/down event contracts as short-horizon binaries that settle against a Chainlink price reference. In the final portion of each 15-minute round, the strategy looks for the book-leading side whose ask remains in a high band (default 0.70–0.80) while Chainlink has already moved same-direction by at least a configured displacement floor. The stated data roles are:

1. Chainlink RTDS — official settlement source; capture Price-to-Beat and current price per round.
2. Binance spot WebSocket — lead residual, short momentum, and volatility estimation only (not the settlement source).
3. Polymarket CLOB WebSocket for monitoring; `GetDepth` immediately before order submission.

The source entry inequality is written as:

`conservativeProb - actualVWAP - entryFee >= MinNetEdge`

with default MinNetEdge reported as at least 2.5% after actual VWAP and entry fee. The source also lists displacement defaults of 0.15% (0.0015) at the 120-second mark and a near-settlement floor of 0.08% (0.0008), optional Binance-direction agreement, and optional hold-to-official-settlement.

### Research interpretation

The proposed economic channel is **incomplete late adjustment of Polymarket binary quotes to the official resolution source**. Near settlement, Chainlink displacement already prices a high probability that the current side will win, yet the CLOB ask on that side may still sit in a band that leaves positive expected edge after VWAP and fees under a *conservative* win-rate estimate. The strategy is therefore not a generic Polymarket market-making or continuous lead-lag system; it is a late-window directional purchase on one binary side when the settlement oracle path and the book ask disagree.

Scout interpretation only: the edge, if any, depends on (a) Chainlink remaining the binding settlement path, (b) Polymarket books not fully incorporating that path in the last 35–120 seconds, and (c) conservative win-probability calibration not being systematically optimistic. None of these are independently established by this Scout cycle.

## Signal

Source-specified reconstruction (research-normalized; values are source defaults, not Scout-tuned):

- Instrument: Polymarket ETH 15-minute up/down event contracts (each round is a separate binary market).
- Universe/venue: Polymarket CLOB for quotes and fills; Chainlink RTDS for settlement path; Binance spot ETH for auxiliary residual/momentum/vol only.
- Formation timestamp / tradability: per 15-minute round. Automated entry is gated to a late window measured in *seconds remaining* in the round; source parameters expose start and end seconds after round open (description: remaining 120 to 35 seconds). Signals evaluated on live book + Chainlink path; orders use Polymarket CLOB after a depth re-check.
- Lookback: Chainlink displacement measured from the 120-second reference point toward current settlement path; Binance short momentum uses a short window (source lists max adverse 5-second momentum as a filter); volatility used for conservative probability fallback.
- Entry: buy the book-leading side only when all of the following hold:
  1. Leading-side ask within source band (default 0.70–0.80; max book spread on target side configurable).
  2. Chainlink same-direction displacement ≥ threshold (default ≥0.15% at 120s; near-settlement floor default ≥0.08%).
  3. Optional: Binance spot direction agrees with Chainlink displacement.
  4. Optional continuous confirmations (source: consecutive confirmation count + minimum confirmation milliseconds).
  5. Edge test: conservative win probability minus actual VWAP minus entry fee (and exit reserve only if active-exit model enabled) ≥ MinNetEdge (default 2.5%).
  6. Filters: max adverse short-term Binance momentum; REST depth timestamp span limit; optional max buy price in fixed-amount mode.
- Exit: default automatic mode holds to official settlement; source also exposes manual/active exit paths, max slippage caps, and worst-case risk per trade. Exit precedence when both stop-like and settlement outcomes could apply is not fully specified beyond source risk parameters.
- Holding period: remaining seconds in the current 15-minute round (typically minutes), one position per round in fixed-amount mode.
- Parameters (source-exposed, not Scout-tuned): entry window seconds; displacement floors; ask band min/max; target-side max spread; MinNetEdge; confirmation count/ms; adverse 5s momentum cap; volatility-failure conservative fallback; fixed buy amount; max buy price; session drawdown stop; daily loss stop; consecutive-loss cooldown rounds; max unsettled positions; max fraction of visible depth consumed; optional Binance agreement; optional hold-to-settlement; SIM vs live.

Underspecified items that prevent treating this as fully reproducible evidence: exact conservative win-probability formula and calibration buckets; exact definition of “book-leading side” under crossed/locked books; precise treatment of partial fills and marketable-limit vs market orders; full exit-fee schedule when not holding to settlement.

## Required data

- Instrument: Polymarket ETH 15-minute binary event contracts; USDC collateral; settlement reference = Chainlink ETH price path for the round.
- Universe: ETH 15-minute Polymarket rounds only (not other underlyings or expiries on the page).
- Venue: Polymarket CLOB (quotes/fills); Chainlink RTDS (settlement); Binance spot ETH-USDT (auxiliary only).
- Timeframe: sub-minute book updates; strategy decision window in the last ~35–120 seconds of each 15-minute round; settlement at round end.
- Fields: Polymarket bid/ask/spread/depth for both binary sides; Chainlink Price-to-Beat and current price per round; Binance spot last/mid short-horizon returns; optional fee and VWAP diagnostics.
- Point-in-time: live streams; source requires pre-order depth re-check; no historical point-in-time book reconstruction is claimed on the FMZ page.
- Timestamp: exchange/oracle clocks; source exposes max depth timestamp span to limit mixed-book quotes.
- Missing-data: source provides volatility-failure conservative fallback and SIM default; full stale-oracle / exchange-outage semantics are not fully specified on the public page.
- Funding/fee/spread needs: Polymarket entry fee included in edge inequality; VWAP used for actual buy price; spreads capped via max target-side spread; no funding rate on the binary itself. Gas/bridge costs for USDC funding are not modeled on the page.

## Execution assumptions

Source-reported: SIM mode default; fixed-amount market-buy mode optional; max slippage parameters; consume-at-most a fraction of visible protective depth; session drawdown / daily loss / consecutive-loss cooldowns; max unsettled positions; one trade per round in fixed-amount mode (no arbitrary daily trade cap in that mode). Source explicitly states no promised returns and recommends simulation and small validation before live use.

Scout assumptions not established by source: fill probability at ask 0.70–0.80 in the final seconds; latency between Chainlink update, Polymarket book update, and order ack; whether adverse selection concentrates on the leading side exactly when displacement is large. Treat fillability as unknown.

## Evidence

### Source-reported

FMZ strategy page 545782 describes the LateAsk v8.10 rule set, parameter surface, data-source roles, and risk controls summarized above. The page and source comments state default SIM operation and do not present a validated live track record, sample-period table, or fee-adjusted performance series that this Scout cycle can cite as independent proof. Related FMZ public code comments on the page identify the script lineage as `fmz@polymarket_eth15m_alpha_v8` and restate the conservative-probability edge inequality. Full source code is gated behind FMZ login on the public page; this capture is based on the public description and visible parameter interface only.

### Independently reproduced

not independently reproduced

### Negative evidence

No peer-reviewed or exchange-official negative study of this exact FMZ LateAsk parameterization was identified in the reviewed public FMZ page. Related repository records already document cost sensitivity, latency adverse selection, and protocol-finality friction for *other* Polymarket strategies; those are adjacent negative context, not disproof of this specific late-window ask rule. Absence of a public live ledger on the page is not evidence of profitability.

## Falsification

Research-proposed falsification tests (not executed):

1. Walk-forward / holdout on immutable Polymarket ETH 15-minute book + Chainlink path snapshots: pre-declare failure if net edge after realistic taker fees and VWAP slippage is ≤0 on a held-out later period under the source-default 2.5% MinNetEdge.
2. Point-in-time / leakage audit: recompute leading-side ask and Chainlink displacement using only information available at decision timestamp; fail if any settlement-path look-ahead enters the conservative probability.
3. Placebo: randomize entry timestamps within the same late window while preserving ask-band filter; fail if realized edge is statistically indistinguishable from the true LateAsk timestamps.
4. Threshold perturbation: displace MinNetEdge, ask band, and Chainlink displacement floors ±20–50%; fail if sign of net edge is unstable across modest parameter moves.
5. Venue/underlying transfer: same rule on other Polymarket crypto binaries (e.g., BTC 15m) with independently calibrated displacement floors; fail if edge vanishes after re-calibration cost.
6. Cost/latency stress: add 50–200 ms signal-to-order delay and adverse selection on the leading side; fail if edge turns non-positive under plausible retail latency.
7. Fee/VWAP stress: replace mid-mark assumptions with observed VWAP including entry fee; fail if conservativeProb − VWAP − fee < MinNetEdge on most signals.
8. Oracle-risk counterfactual: exclude rounds where Chainlink path and Binance disagree beyond a pre-set residual; fail if edge exists only in oracle-disagreement rounds (would suggest data artifact rather than book lag).

Each test requires a pre-declared failure rule; unconstrained retuning to rescue performance counts as falsification.

## Crypto portability

Mark: **adapted / partial**.

The strategy is already crypto-native (ETH on Polymarket with Chainlink settlement). Portability notes:

- Spot/perpetual/futures/options: this is an event-contract binary, not a perpetual or option; do not port the 0.70–0.80 ask band to linear perps without a different payoff model.
- 24/7 timestamping: ETH and Polymarket crypto binaries trade continuously; no equity-session close filter.
- Funding/borrow: no funding on the binary; opportunity cost is locked USDC until settlement.
- Fragmentation: Polymarket is the trade venue; Chainlink is the binding settlement path. Other venues (e.g., Kalshi crypto events) have different oracles, tick sizes, and fee schedules — parameters would not transfer.
- Liquidity: late-window depth on one binary side can be thin; source depth-consumption cap is a partial mitigation only.
- On-chain/protocol dependencies: Polymarket CLOB and resolution process; Chainlink RTDS availability; USDC funding path.
- Crypto portability is not authorization to trade.

## Limitations

- Public page only; full Pine/JS source and backtest metrics behind login — signal internals for conservative probability are underspecified.
- No independent reproduction; no audited live PnL on the cited page.
- Short sample of product life relative to crypto regime shifts; Polymarket fee/resolution rules can change.
- Late-window binaries are capacity-constrained; thin books can erase theoretical edge.
- Conservative win-probability calibration is a research-defined gap — if systematically biased high, MinNetEdge is illusory.
- Adjacent Polymarket negative records (cost sensitivity, latency adverse selection, finality latency) raise the prior that naive late binary purchases fail after costs.
- Source author/community comments on related FMZ momentum systems note regime dependence; that commentary is not transferable evidence for this LateAsk rule.
- Ordinary repeated content is not claimed; this record exists because the LateAsk + Chainlink-displacement construction is materially distinct from existing Polymarket captures.

Incremental-write threshold: met via new family (late-window Chainlink-displacement vs high-ask binary), distinct venue/oracle data dependency, and explicit entry inequality with fee/VWAP terms.

## Implementation status

`not-implemented`. This research capture does not modify NautilusTrader, create a strategy family, authorize Paper/Testnet/Live execution, or write to Hermes Wiki Body / Wiki Brain. The FMZ script may exist as third-party platform code; this repository record does not implement, run, or endorse it.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence in this repository means only that the public source hypothesis was normalized for intake review. It is not strategy adoption, implementation authorization, or permission to run Paper/Testnet/Live.

## Related Wiki records

Adjacent repository records used for deduplication (paths on `main`):

- `polymarket-15m-crypto-tri-transformer-market-making-2026-09-13.md` — different mechanism (market-making / latency adverse selection).
- `polymarket-binance-high-frequency-binary-lead-lag-2026-09-02.md` — different mechanism (HF continuous lead-lag, OpenMarket lineage).
- `polymarket-binary-mean-reversion-cost-sensitivity-2026-09-14.md` — different mechanism (mean reversion / cost sensitivity).
- `polymarket-protocol-finality-redemption-latency-carry-arbitrage-falsification-2026-09-16.md` — different mechanism (resolution vs settlement carry).
- `polymarket-favorite-longshot-bias-crypto-politics-2026-09-14.md` — different mechanism (favorite-longshot bias).
- `kalshi-btc-event-contract-spot-hedge-2026-09-15.md` — different instrument and purpose (hedge overlay, not late ask).

No Hermes Wiki Brain write was performed. Future Scout runs must re-search before creating another Polymarket late-window record with the same FMZ id or the same normalized rule.

## Sources

- FMZ Quant, Polymarket ETH15 LateAsk v8.10, https://www.fmz.com/strategy/545782 (public description and parameter surface; captured 2026-09-18).
