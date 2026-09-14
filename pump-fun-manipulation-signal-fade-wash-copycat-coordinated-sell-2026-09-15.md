---
schema: strategy-research-record-v1
title: "Pump.fun Manipulation Signal Fade: Wash Trading, Copycat, and Coordinated Sell Detection as Contrarian Alpha on Solana Meme Coins"
created: 2026-09-15
updated: 2026-09-15
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - on-chain
  - solana
  - pump.fun
  - meme-coins
  - manipulation-detection
  - wash-trading
  - copycat-coins
  - coordinated-sell
  - contrarian
  - fade
  - negative-evidence
status: research-only
confidence: medium
source_as_of: 2026-09-09
sources:
  - "Szwajcok, N., Tsuchiya, T., Liu, E., Soska, K., Payer, M., Christin, N. (2026). 'Meme Coin Factories: Uncovering Large-Scale Manipulations on pump.fun.' ACM CCS 2026. arXiv:2609.10246v1 [cs.CR]. https://arxiv.org/abs/2609.10246"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Pump.fun Manipulation Signal Fade: Wash Trading, Copycat, and Coordinated Sell Detection as Contrarian Alpha on Solana Meme Coins

## Provenance

- **Primary Source:** Nicolas Szwajcok (EPFL / ETH Zürich / CMU), Taro Tsuchiya (CMU), Enze Liu (CMU), Kyle Soska (Fullstack), Mathias Payer (EPFL), Nicolas Christin (CMU). *"Meme Coin Factories: Uncovering Large-Scale Manipulations on pump.fun"*, Proceedings of the 2026 ACM SIGSAC Conference on Computer and Communications Security (CCS'26). arXiv preprint `arXiv:2609.10246v1 [cs.CR]`, submitted September 9, 2026.
- **Canonical DOI:** [10.48550/arXiv.2609.10246](https://doi.org/10.48550/arXiv.2609.10246)
- **Abstract URL:** https://arxiv.org/abs/2609.10246
- **Full-text HTML:** https://arxiv.org/html/2609.10246v1
- **PDF:** https://arxiv.org/pdf/2609.10246
- **Primary Source Verification:** The complete PDF (CCS 2026 camera-ready) was directly retrieved and inspected. All quantitative claims below trace to Sections 4–8 and Tables/Figures of `arXiv:2609.10246v1`. The authors, affiliations, sample composition, manipulation class definitions, and key statistics were verified against the primary source text.
- **Deduplication Audit:** A comprehensive search of all records in `alpha-strategy-research` confirmed zero existing records citing `arXiv:2609.10246`, Szwajcok, Tsuchiya, or the "Meme Coin Factories" paper. The related pump.fun record `solana-bonding-curve-sniper-cohort-contamination-adjusted-flow-2026-09-02.md` (Kamat 2026, arXiv:2607.02795) studies sniper cohort detection via wallet clustering — a structurally distinct mechanism from the five manipulation classes (wash trading, creator obfuscation, coordinated sell, copycat coins, social media manipulation) and MMaaS infrastructure documented here.

## Economic mechanism

### Source-reported

The paper documents that pump.fun, the largest Solana meme-coin launchpad (15.2 million coins, January 2024–January 2026), is dominated by strategic actors who manipulate trading signals to attract inexperienced buyers and extract profits from unsustainable price pumps. Five manipulation classes are identified:

1. **Wash trading:** Buy-sell transactions between controlled accounts inflate volume. Identified lower bound: 4 million wash trading transactions (17% of all trading transactions). Wash trading can increase a coin's "graduation" probability (moving from bonding curve to external DEX) up to 10x.
2. **Creator address obfuscation:** Manipulators use different blockchain addresses to create coins, hiding ownership concentration. Top-1% of creator groups (funding-address clusters traced 3 hops back) create 58.6% of all coins.
3. **Coordinated sell:** Multiple addresses buy tokens, consolidate into a single address, then sell simultaneously. Nearly 8,000 instances identified under conservative criteria.
4. **Copycat coins:** Replicas of existing coins (same name, symbol, description, images) lure uninformed traders. At least 1.5 million copycat coins detected (>10% of all coins). Original coins are significantly more successful than copies.
5. **Social media manipulation:** Automated bots post promotional comments; social media posts drive coin creation. 3.5 million coins (23.5%) created after Twitter or Truth Social posts; 31 posts each generated ≥$1M for creators.

The paper further uncovers **Market-Manipulation-as-a-Service (MMaaS)**: third-party tools enabling non-technical users to perform these manipulations at scale, including custom smart contracts, low-latency nodes, address generators, CAPTCHA solvers, and proxy rotation.

### Research interpretation

The paper is a measurement and detection study, not a trading strategy. However, the documented manipulation patterns constitute a falsifiable alpha hypothesis:

**Contrarian fade hypothesis (research-proposed):** Coins exhibiting on-chain manipulation signatures — elevated wash trading volume (high buy-sell cycling between related addresses), creator obfuscation (funding-address clusters holding disproportionate supply), copycat metadata (duplicate name/symbol/image), or social-media-driven creation spikes — should underperform after initial price pumps, because the price increase is artificially sustained by manipulation rather than genuine demand.

The mechanism is a structural market-manipulation effect: manipulators inflate volume and price to attract uninformed buyers, then exit. The fade strategy would identify these manipulation signals in real-time and take contrarian positions (short after pump, or avoid long). This is not a risk premium — it is an adverse-selection/infrastructure-driven inefficiency in a fragmented, low-regulation on-chain venue.

## Signal

The paper does not propose or test a trading strategy. The following signal construction is **research-proposed** based on the manipulation detection methods described in the paper:

### Manipulation Detection Signals (research-proposed operationalization)

**Signal 1: Wash Trading Intensity**
- Lookback: Rolling 1-hour window of on-chain transactions for a given coin.
- Detection: Identify buy-sell transaction pairs where the same entity (or entity cluster) both buys and sells within a short window, with no net position change. The paper's "WT1" method identifies atomic wash events; an approximate variant relaxes atomicity to capture split buy-sell sequences.
- Threshold: Wash trading volume as a fraction of total volume exceeding a research-defined threshold (e.g., >20% of hourly volume). Source-reported baseline: 17% of all trading transactions on pump.fun are wash trades.
- Entry: Short (or avoid long) on coins with wash trading intensity above threshold.
- Exit: Time-based exit after a research-defined holding period, or when wash trading intensity drops below threshold.

**Signal 2: Creator Obfuscation Score**
- Lookback: Funding-address graph traced 3 hops backward from coin creator address.
- Detection: Identify coins where the creator address belongs to a funding-address cluster that has created multiple coins (top-1% clusters create 58.6% of all coins).
- Threshold: Creator cluster has created >N coins (research-defined). Source-reported: top-1% groups create 58.6% of all coins.
- Entry: Short coins created by high-output clusters.

**Signal 3: Copycat Detection**
- Detection: Compare coin metadata (name, symbol, description, image IPFS hash) against all previously created coins. Jaccard similarity above a threshold indicates copycat.
- Threshold: Metadata similarity exceeding a research-defined threshold (e.g., Jaccard > 0.8 on name+symbol+description). Source-reported: 1.5 million coins (>10%) are copies.
- Entry: Short or avoid copycat coins.

**Signal 4: Social Media Creation Spike**
- Detection: Monitor Twitter/Telegram for posts that precede pump.fun coin creation. The paper identifies 3.5 million coins (23.5%) created after social media posts.
- Threshold: Number of coins created within N minutes of a social media post exceeding a research-defined threshold.
- Entry: Short coins created in response to social media spikes.

### Important Caveats

- All thresholds above are **research-proposed** and not specified by the primary source.
- The paper does not backtest any trading strategy using these signals.
- Implementation would require real-time on-chain data infrastructure (Solana blockchain indexing, funding-address graph construction, metadata comparison, social media monitoring).
- The paper identifies that manipulators use low-latency nodes and custom smart contracts, creating a speed advantage that a retail fade strategy may not overcome.

## Required data

- **Instrument:** All tokens launched on pump.fun (Solana blockchain), bonding-curve stage and post-graduation DEX stage.
- **Universe:** 15.2 million coins launched January 14, 2024 – January 14, 2026. For signal construction, universe would be newly launched coins in real-time.
- **Venue:** pump.fun (Solana), Raydium, PumpSwap (post-graduation DEX venues).
- **Market type:** Spot (Solana SPL tokens on bonding curves and DEXes).
- **Timeframe:** Transaction-level on-chain data (sub-second granularity possible on Solana).
- **Fields:**
  - Full transaction history per coin (buyer/seller addresses, amounts, timestamps).
  - Coin metadata (name, symbol, description, image IPFS hash, creator address).
  - Creator funding-address graph (3-hop backward tracing).
  - Social media posts (Twitter/X, Telegram) mentioning coins or coin-related terms.
  - Bonding curve state (SOL reserves, graduation threshold ~85 SOL).
- **Point-in-time:** On-chain data is inherently point-in-time; social media data requires timestamp alignment.
- **Timestamp:** Solana block timestamps (UTC).
- **Missing-data:** Not explicitly addressed in the paper; on-chain data is complete for the Solana blockchain.
- **Transaction cost/slippage:** Not modeled in the paper. For a fade strategy on bonding curves, slippage on illiquid new tokens and bonding-curve price impact are material.

## Execution assumptions

The paper does not specify execution assumptions for a trading strategy. The following are **research-proposed**:

- **Signal-to-order timing:** Detect manipulation signal on-chain, enter short (or avoid long) in real-time. Requires low-latency on-chain monitoring.
- **Fill model:** Market order on bonding curve (buy-side liquidity may be thin for new tokens).
- **Fees:** pump.fun charges creation fees; DEX trading fees (Raydium/PumpSwap) are venue-specific.
- **Slippage:** Bonding curve price impact is deterministic but can be large for concentrated positions. Post-graduation DEX slippage depends on pool depth.
- **Capacity:** Extremely limited. Meme coins have very low liquidity; position sizing must be small.
- **Latency:** Manipulators use low-latency nodes and custom smart contracts; a fade strategy faces a structural speed disadvantage.
- **Leverage:** Not applicable for spot bonding-curve trading; possible on post-graduation DEX perpetuals if available.
- **Partial fills / failures:** On-chain transactions either succeed or fail atomically; no partial fills.

## Evidence

### Source-reported

The paper reports the following empirical findings from its measurement study:

- **Wash trading prevalence:** Lower bound of 4 million wash trading transactions (17% of all trading transactions). Source: Section 4,WT1 and WT2 detection methods.
- **Wash trading effect on graduation:** Wash trading can increase graduation probability up to 10x. Source: Section 4, causal analysis comparing wash-traded vs. non-wash-traded coins.
- **Creator concentration:** Top-1% of funding-address clusters (3-hop) create 58.6% of all coins. Source: Section 5, Table 8.
- **Coordinated sell instances:** Nearly 8,000 instances identified (4,402 in 1% sample, 3,510 in 5-day sample). Source: Section 6.
- **Copycat scale:** At least 1.5 million copycat coins (>10% of all coins). Original coins are significantly more successful. Source: Section 7.
- **Social media manipulation:** 3.5 million coins (23.5%) created after Twitter/Truth Social posts. 31 posts each generated ≥$1M for creators. Source: Section 8.
- **MMaaS existence:** Third-party tools commoditizing manipulation (address generation, copy-bot, social media bots, CAPTCHA solvers). Source: Section 9.

These are source-reported measurement findings, not trading strategy backtest results. The paper explicitly does not test any trading strategy.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The paper itself is primarily a measurement/detection study and does not report negative evidence against the fade hypothesis. However, several structural factors suggest the fade strategy faces significant challenges:

1. **Speed disadvantage:** Manipulators use low-latency nodes and custom smart contracts; they execute faster than retail fade participants.
2. **Liquidity constraints:** Bonding-curve tokens have limited liquidity; shorting may be impossible or extremely costly.
3. **Adverse selection:** If manipulation signals are well-known, sophisticated actors may adapt (e.g., slower wash trading, less obvious obfuscation).
4. **Platform evolution:** pump.fun may implement mitigations (the paper proposes several), which could eliminate the signal.

None identified in the reviewed sources beyond the structural challenges noted above; absence is not evidence of no negative result for the specific fade hypothesis.

## Falsification plan

1. **Wash trading fade test (research-defined):** On a sample of pump.fun coins with detected wash trading (WT1 method), measure post-pump returns for a short position entered after wash trading intensity exceeds threshold. **Failure rule:** If wash-traded coins do not underperform non-wash-traded coins after controlling for graduation status, the wash-trading fade hypothesis fails. Required sample: ≥500 wash-traded coins over ≥6 months. **Metric:** Difference in 24-hour post-pump return between wash-traded and non-wash-traded coins. **Threshold:** Significant negative difference (one-sided test, α = 0.05).
2. **Copycat fade test (research-defined):** Measure post-creation returns for copycat coins vs. original coins. **Failure rule:** If copycats do not underperform originals by a meaningful margin after controlling for timing, the copycat fade hypothesis fails.
3. **Creator cluster fade test (research-defined):** Measure post-creation returns for coins created by high-output clusters (>N prior coins) vs. first-time creators. **Failure rule:** If high-output-cluster coins do not underperform, the creator-obfuscation fade hypothesis fails.
4. **Cost sensitivity:** Model bonding-curve slippage, DEX trading fees, and potential MEV extraction. **Failure rule:** If transaction costs exceed the gross fade edge, the strategy is not tradable.
5. **Adversarial robustness:** Test whether manipulation patterns persist after the paper's publication and proposed mitigations. **Failure rule:** If pump.fun implements effective countermeasures that eliminate the manipulation signals, the strategy has no forward-looking edge.

## Crypto portability

**Direct** — the strategy is natively designed for crypto (Solana on-chain meme coins). However, the specific venue (pump.fun) and token type (meme coins on bonding curves) are highly specialized. Portability to other launchpads (e.g., CLS, Four.meme) or other chains is unproven and would require re-validation of manipulation patterns.

Crypto-specific risks:
- **Bonding curve mechanics:** Price impact is deterministic but non-linear; position sizing must account for bonding-curve shape.
- **Graduation risk:** Tokens may or may not graduate to external DEXes; post-graduation liquidity differs from bonding-curve stage.
- **MEV / sandwich attacks:** On Solana, validators and searchers may extract value from fade trades.
- **Platform risk:** pump.fun can change rules, implement mitigations, or shut down.
- **Regulatory risk:** The paper's findings may trigger regulatory action against pump.fun or manipulation tools.
- **Smart contract risk:** MMaaS tools and custom contracts may have bugs or be malicious.

## Limitations

- **Not a trading strategy:** The paper is a measurement/detection study. No trading strategy is proposed, backtested, or validated. The alpha hypothesis is entirely research-proposed.
- **No backtest results:** The paper does not report any trading performance, Sharpe ratio, or return metrics for a fade strategy.
- **Structural speed disadvantage:** Manipulators use low-latency infrastructure; retail fade participants face adverse timing.
- **Liquidity constraints:** Meme coins on bonding curves have limited liquidity; shorting may be impossible.
- **Data completeness:** The paper uses a 1% random sample for transaction analysis; full population inference requires extrapolation.
- **Sample period:** January 2024–January 2026; manipulation patterns may evolve.
- **Platform-specific:** Findings are specific to pump.fun on Solana; generalizability to other launchpads is untested.
- **MMaaS evolution:** As manipulation tools commoditize, counter-detection may also evolve, potentially closing the signal.
- **Publication effect:** The CCS 2026 publication may trigger platform mitigations that eliminate the documented manipulation patterns.

## Implementation status

Not implemented. No implementation in our research stack. The paper provides detection methods but no trading strategy implementation.

## Adoption boundary

This record is research material only. A record being present in this repository does **not** mean:
- The manipulation signals are tradeable;
- A fade strategy would be profitable;
- The alpha hypothesis has been validated;
- Any implementation has been approved;
- Paper, testnet, or live trading is authorized.

## Related Wiki records

- `[[solana-bonding-curve-sniper-cohort-contamination-adjusted-flow-2026-09-02]]` — Kamat (2026), arXiv:2607.02795. Sniper cohort detection on pump.fun via wallet clustering. Distinct mechanism: Kamat studies first-buyer-window sniper behavior and its contamination-adjusted buyer-flow lift; Tsuchiya et al. study five manipulation classes (wash trading, obfuscation, coordinated sell, copycats, social media) and MMaaS infrastructure. The two papers are complementary: sniper detection identifies who buys first; manipulation detection identifies how prices are artificially inflated.
- `[[crypto-binance-smallcap-pump-reversal-regime-gated-falsification-2026-09-13]]` — Agarwal (2026), GitHub. Binance perpetual small-cap pump reversal. Distinct: operates on Binance perps (centralized exchange), uses price-based regime gating; Tsuchiya et al. operate on Solana on-chain bonding curves with on-chain manipulation signals.
- `[[crypto-binance-smallcap-pump-reversal-regime-gated-falsification-2026-09-13]]` — related pump-and-dump fade research on centralized venues.

## Sources

1. Szwajcok, N., Tsuchiya, T., Liu, E., Soska, K., Payer, M., Christin, N. (2026). "Meme Coin Factories: Uncovering Large-Scale Manipulations on pump.fun." Proceedings of the 2026 ACM SIGSAC Conference on Computer and Communications Security (CCS'26). arXiv:2609.10246v1 [cs.CR]. https://arxiv.org/abs/2609.10246
