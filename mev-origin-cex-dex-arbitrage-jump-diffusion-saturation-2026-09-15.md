---
schema: strategy-research-record-v1
title: "MEV Origin: CEX–DEX Arbitrage Volume, Jump-Driven Mispricing and Market Saturation"
created: 2026-09-15
updated: 2026-09-15
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - ethereum
  - market-microstructure
  - amm
  - cex-dex
  - arbitrage
  - mev
  - jump-diffusion
  - block-building
status: research-only
confidence: medium
source_as_of: 2026-04-17
sources:
  - "Bence Ladóczki, Miklós Rásonyi, and János Tapolcai, 'Where Does MEV Really Come From? Revisiting CEX–DEX Arbitrage on Ethereum', arXiv:2604.15973v1 [cs.CR], submitted 2026-04-17; presented at Financial Cryptography and Data Security 2026 (FC 2026). https://arxiv.org/abs/2604.15973"
  - "Reference implementation (C++ SPD integrator plus fitting/estimation scripts): https://gitlab.com/jtapolcai/sde_amm — branch main, most recent commit as retrieved 2026-09-15: fc767aba289a41c79217087861c7efda100a03ae"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# MEV Origin: CEX–DEX Arbitrage Volume, Jump-Driven Mispricing and Market Saturation

## Provenance

- **Primary source:** Bence Ladóczki (BME and HUN-REN Information Systems Research Group, Budapest), Miklós Rásonyi (HUN-REN Alfréd Rényi Institute of Mathematics and Eötvös Loránd University), János Tapolcai (Budapest University of Technology and Economics), "Where Does MEV Really Come From? Revisiting CEX–DEX Arbitrage on Ethereum", arXiv:2604.15973v1 [cs.CR], submitted 2026-04-17. Presented at Financial Cryptography and Data Security 2026 (FC 2026). DOI: https://doi.org/10.48550/arXiv.2604.15973. URL: https://arxiv.org/abs/2604.15973.
- **Version pinned for this record:** v1 only (no later version exists as of 2026-09-15). Author list taken from the paper itself (PDF/LaTeX source: "Bence Ladóczki"); the arXiv metadata listing renders the first author as "Bence Ladóczk" (trailing character absent) — treated as a metadata typo, flagged here rather than silently corrected.
- **Code artifact:** https://gitlab.com/jtapolcai/sde_amm (C++ numerical integrator for the stationary misprice distribution; Python scripts for fitting and volume/profit estimation). Branch `main`; most recent commit as retrieved: fc767aba289a41c79217087861c7efda100a03ae.
- **Empirical windows used by the source:**
  - Uniswap V2 ETH–USDT pool `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` (~$86M TVL), blockchain data extracted with the authors' own execution client, 13–29 September 2025 (Table 1 averages).
  - CEX exchange rates at 1-second resolution during the same September 2025 window; best ask prices originate from Binance (84%), KuCoin (9%), Gate.io (7%); best bids from Binance (88%), KuCoin (5%), Gate.io (7%).
  - Binance Spot price API data, November–December 2024, used to motivate jump modelling (worked example: jump at 2024-12-09 22:06:29, $3542 → $3640 within one second).
  - Hourly log-return statistical tests on 12 cryptocurrencies (fil, btc, eth, arb, xch, 1inch, aave, ltc, beam, cro, sol, bnb), 2024-12-11 to 2025-01-15 (appendix Table 6).
- **Source-quality note:** FC 2026 conference paper with open code. This record captures the paper's economic claims about CEX–DEX arbitrage; it is not evidence that any specific trading strategy earns net profit.

## Economic mechanism

### Source-reported

The paper asks where MEV revenue on Ethereum originates and argues that CEX–DEX arbitrage is the dominant, undercounted component. The chain of argument, as stated by the authors:

1. Prior theoretical AMM models (Black–Scholes / geometric Brownian motion, continuous price paths) predicted only modest CEX–DEX arbitrage volumes and profits, while recent empirical studies show CEX–DEX arbitrage volumes exceed atomic arbitrage and sandwich attacks by orders of magnitude. The authors claim the discrepancy is caused by the continuous-path assumption: BS-type models ignore price jumps, "which are precisely the points at which arbitrage opportunities tend to arise."
2. They build an extended discrete-time AMM mispricing model whose CEX price process combines a diffusive term and a stochastic jump term with arbitrary noise distribution, prove the mispricing process is a uniformly ergodic Markov chain with a stationary probability distribution (SPD) computable by function iteration, and derive closed-form expected arbitrage profit and expected arb trading volume for a constant-product market maker (CPMM).
3. Calibrated on real ETH–USDT data, the model reproduces observed CEX–DEX arbitrage volume and profit an order of magnitude better than the BS benchmark, and the authors conclude: (i) the revenue sustaining PBS (proposer–builder separation) arises naturally from CEX–DEX arbitrages; (ii) a large amount of AMM volume may be attributable to arbitrage; (iii) arbitrage profits are comparable to measured MEV, suggesting the arbitrage market may be saturated (block builders choose among many competing arbitrageurs, forcing rebates of much of the profit); (iv) empirical heuristics used to label CEX–DEX arbitrage transactions may be overly restrictive; (v) shorter block times are unlikely to reduce MEV because opportunities primarily emerge from rapid price jumps.

### Research interpretation

Falsifiable reading: AMM pool prices are passive and only reprice when arbitrageurs trade against them. If external CEX prices move predominantly in discrete jumps, then each jump that breaches the pool's no-arbitrage fee band creates a discrete, capturable mispricing whose size distribution — not the smooth diffusion — determines arb volume and builder revenue. Two testable corollaries follow: (a) arbitrage flow and profit scale with jump frequency, so volume-based MEV attribution that assumes diffusion dynamics systematically undercounts CEX–DEX arbitrage (and over-attributes to sandwich/atomic MEV); (b) if the arb market is competitive and saturated, the marginal searcher's *net* take should be small even though gross arbitrage volume is large — the surplus accrues to block builders. The mechanism is a market-structure/infrastructure effect (PBS auction competition + jump-driven mispricing), not a risk premium. This record treats it as a hypothesis carrier for (i) MEV attribution methodology and (ii) the question of whether a *new* arbitrageur can earn net alpha in this market; the source does not demonstrate a net-of-fee profitable trading rule for a new entrant.

## Signal

The source defines a **mispricing signal** (model-level), not a fully specified trading system.

- **Mispricing definition:** the logarithmic misprice `z_t = ln(P_t / P̃_t)`, where `P_t` is the external CEX price and `P̃_t` is the AMM price; `P̃_t` inferred from swap events' amount-in/amount-out values. Time unit: seconds (Ethereum block time 12s).
- **Trigger band:** arbitrage is profitable when `z_t` leaves the no-arbitrage band `[-γ−, γ+]`, with `γ− = γ+ = γ + γ_CEX`, where `γ` is the AMM swap fee (in log units; 30 bp is used as the typical Uniswap V2 level) and `γ_CEX` is the effective CEX bid–ask spread. The arbitrageur (present with i.i.d. per-step probability `p`) trades **exactly enough to reset the pool price to the closest band boundary** `γ+` or `γ−`. Direction: for `z_t > γ+` the risky asset is bought on the AMM / sold at the higher CEX reference price; the mirror trade applies for `z_t < -γ−`. (Direction statement is our normalization of the paper's "sets it back to the boundary" rule; the paper states the reset and the profit formula, not order routing.)
- **Profit formula (source, Corollary 3):** expected profit per instant `= TVL · p · [ e^{γ/2} ∫_{γ}^{∞} (cosh((t−γ)/2) − 1) f*(t) dt + e^{−γ/2} ∫_{−∞}^{−γ} (cosh((t+γ)/2) − 1) f*(t) dt ]`, where `f*` is the stationary density of `z_t`.
- **Volume formula (source, Corollary 4):** expected arb trading volume has the analogous integral form `TVL · p · [∫_{γ}^{∞} (e^{γ/2} − e^{−t/2+γ}) f*(t) dt + ∫_{−∞}^{−γ} (e^{−γ/2} − e^{−t/2−γ}) f*(t) dt]`.
- **Fitted jump dynamics (source, Table 5, per-12s-step parameters):** e.g. τ=2.0 row: `σ=0.0234`, `μ=0.0677`, `μ_J=−0.2035`, `σ_J=0.1952`, `q=0.0411`. The main text (Section 4.1) instead quotes: daily volatility 1.9%, drift 0.023, jump probability `q=0.045` "per one-second step", jump mean −24.9%, jump standard deviation 15.7% "in log-return units" — these main-text values are **not reconcilable** with the appendix Table 5 row at the same τ=2.0; see Limitations. Do not quote the main-text jump parameters as if they were the table values.
- **Signal formation timestamp / execution window (source, calibration methodology):** the source aligns a 12-second window with CEX prices and assumes that if any monitored CEX offers a better price at any moment within the window, some arbitrageur captures the opportunity and submits a transaction. Blocks are estimated to arrive at the authors' node with ≈8-second delay (blocks are typically proposed within the first four seconds of a slot) and the window start is aligned accordingly.
- **Underspecified for trading (marked):** the source does not specify order types, order sizing beyond "reset to boundary", queue/fill mechanics, gas-price bidding strategy, capital requirements, or any entry/exit rule for the CEX leg. Any executable operationalization (sampling cadence, latency budget, priority-fee policy, abort thresholds) is therefore **research-proposed**, not source-reported.

## Required data

- **Instrument / universe:** Ethereum L1 CEX–DEX arbitrage on Uniswap V2 ETH–USDT pool `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852`; monitoring universe of CEX venues (Binance, KuCoin, Gate.io in the source's setup).
- **Venue / market type:** Ethereum L1 AMM (spot, CPMM) + centralized spot exchange rates; execution in the source's empirical setting is on-chain (DEX leg) against CEX reference prices.
- **Timeframe / fields:**
  - On-chain: swap events (amount-in, amount-out, pool reserves) per block; pool TVL; pool fee tier `γ`.
  - CEX: best bid and best ask at 1-second resolution across venues; timestamp alignment to 12-second block windows.
  - MEV chain data: priority fees and direct coinbase transfers of swaps (used for the empirical MEV estimate); block/slot timing.
- **Point-in-time requirements:** the mispricing construction uses contemporaneous CEX best quotes vs on-chain pool state; causal alignment between CEX observation and block inclusion is approximate in the source (≈8s assumed arrival delay), which is a look-ahead-sensitive boundary.
- **Missing-data assumptions:** not stated in the source beyond the described filtering/alignment; any interpolation of CEX quotes for gaps is a research-proposed step.
- **Parameter estimation inputs:** `σ` (diffusion vol), `μ` (drift), `q` (per-step jump probability), jump size `U ~ N(μ_J, σ_J²)`, estimated from spot price data with a fixed jump-classification threshold rule: absolute return `< τ ×` price volatility ⇒ classified GBM, otherwise jump; source rule-of-thumb `τ = 2.0` (≈4.55% of GBM observations misclassified under a Gaussian assumption).

## Execution assumptions

- **Signal-to-order timing (source, approximate):** 12-second observation window; the arb is assumed to submit within the block window; ~8s block arrival delay at the monitoring node; blocks proposed within the first ~4s of a slot. This is the source's calibration approximation and is sensitive to latency; it is not a validated execution model.
- **Competition / ordering (source):** arbitrageurs compete for inclusion; the winner is modeled as the one who can pay the highest transaction fee (priority fee + coinbase transfer) and therefore gets included on-chain. Implication used by the paper: gross arb profit is largely rebated to block builders (PBS), so the observable "MEV paid" is a close proxy for arb profit.
- **Fee / cost treatment (source):** AMM swap fee `γ` (30 bp used as typical for Uniswap V2); effective CEX spread `γ_CEX` folded into the trigger band (sensitivities computed at 0/10/20/30 bp, since the true spread is not precisely known); empirical MEV estimated from priority fees + direct coinbase transfers of single-swap transactions, scaled proportionally for bundles. Gas cost is **not** an explicit term in the analytic profit/volume formulas (data gap; treated via the fee-competition narrative instead). Slippage/market impact beyond the CPMM invariant is not modeled. No leverage, funding, or borrow components (the analyzed trade is spot DEX leg vs CEX reference).
- **Fill model:** deterministic reset to the fee-band boundary when an arbitrageur is present; no partial fills or queue priority in the model.

## Evidence

### Source-reported

All numbers below are as reported by arXiv:2604.15973v1; none are independently reproduced.

**1. Table 1 — average daily swaps/volumes/MEV for the Uniswap V2 ETH–USDT pool, 13–29 September 2025 (pool TVL ≈$86M):**

| Row | Category (USDT→WETH #swaps / volume; WETH→USDT #swaps / volume) | MEV / profit |
| --- | --- | --- |
| 1 | All swap transactions: 2,724 / $3,369,073 · 1,907 / $3,072,624 | ≈$2,030 |
| 2 | CEX–DEX arb (heuristic-based): 496 / $970,436 · 241 / $1,002,020 | (not reported) |
| 3 | Sandwich (avg): 0.2 / $25,345 · 0.2 / $64,443 | $414 |
| 4 | Atomic arb (avg): 3 / $10,515 · 2 / $34,562 | $136 |
| 5 | Black–Scholes SDE model estimate: 86 / $208,844 · 75 / $177,961 | $48 |
| 6 | This paper's model: 256 / $1,881,277 · 251 / $1,838,985 | $1,454 |

Context given by the authors: total DEX volume over the period ≈$462B (Uniswap ≈$106B). Their model yields an estimated arbitrage volume "roughly twice" the heuristic-classified on-chain arbitrage volume, while observed swap counts exceed model counts (explained by multiple competing arbitrageurs and spread widening after jumps).

**2. Figure 2 legend — model-fit vs empirical mispricing (same pool/window):** computed arb volume as a share of empirically measured total pool volume: 75% (γ_CEX=0 bp), 58% (10 bp), 46% (20 bp), 39% (30 bp); corresponding profit share vs MEV-based estimate: 93%, 72%, 57%, 48%; volume-to-profit ratio: 1312, 1264, 1264, 1267. A linear-combination spread mixture (weights w₀=19%, w₁₀=19%, w₂₀=28%, w₃₀=34%) gives 51% volume share, 63% profit share, ratio 1274.

**3. Section 4.2 cross-verification claims:** daily swap counts distribute roughly uniformly across the mispricing interval while volumes concentrate near the band boundaries; "the figures suggest that arbitrage accounts for approximately half of the volume"; γ_CEX is typically very small; swaps also occur at slightly negative γ_CEX, attributed by the authors to anticipation of imminent moves or slightly earlier jump information from free CEX APIs; the bounds on the volume/profit ratio "lie fairly close to each other", so the MEV paid out from swaps is only slightly lower than the profit generated when the pool is used exclusively by arbitrageurs — the basis of the saturation conjecture.

**4. Table 4 (appendix, model sensitivity):** arbitrage profits (proportion of `L√W`) increase significantly with jump probability `q` (cells compare q=0 vs q=0.2 across block times 10 min / 2 min / 12 s / 2 s and fee levels 1–100 bp); the authors note that at Ethereum's 12s blocks and 30 bp fee level, "jumps lead to orders of magnitude larger arbitrage profits."

**5. Publication status:** presented at FC 2026 (per arXiv comments field); no journal reference listed; open-source C++ implementation provided.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Saturation (source's own main caveat):** if arb profits ≈ measured MEV paid, then block builders capture a large fraction of the surplus and the marginal (non-winning) arbitrageur's net take is small; the paper explicitly conjectures the arbitrage market "is saturated". This cuts against any hypothesis that a new entrant can farm this flow at large gross margins.
- **Model-vs-observation mismatch:** the model overestimates arbitrage volume relative to heuristic-classified on-chain arb (≈2×) yet underestimates swap counts; the authors attribute the latter to multiple arbitrageurs and spread widening — i.e., the one-arbitrageur, one-trade reset abstraction is imperfect.
- **Parameter reporting inconsistency (discovered in this audit):** main text Section 4.1 quotes `q=0.045` per one-second step with jump mean −24.9% / sd 15.7%, while appendix Table 5 (τ=2.0) reports `q=0.0411` per 12-second step, `μ_J=−0.2035`, `σ_J=0.1952`; the pure-diffusion comparison values also differ between the two places (main text: 2.1% vol, 0.046 drift; Table 5 "–" row: σ=0.0234, μ=0.0234). Fitted jump parameters must therefore be treated as internally inconsistent until reconciled against the code.
- **Heuristic attribution problem:** empirical "CEX–DEX arb" rows rely on heuristic classifiers (e.g. Wu et al. 2025); the paper argues these heuristics are too restrictive (arbitrage can hide as apparent noise trades), which means both the empirical arb volume and the MEV/profit estimate of row 2 are lower bounds, not measurements.
- **Single-pool, single-window calibration:** all headline empirical comparisons come from one Uniswap V2 ETH–USDT pool over 17 days (13–29 Sep 2025); no cross-pool or cross-period replication is reported.
- **Model exclusions:** noise traders are omitted (volume-attribution share of arb is therefore an upper-bound statement, by the authors' own admission); L2/rollups and concentrated liquidity (v3) are out of scope; γ_CEX must be treated as an unknown sensitivity parameter — the volume-share claim swings from 75% to 39% purely over γ_CEX ∈ [0, 30] bp.
- **Tail evidence in the source's own sample:** hourly log-returns of 12 cryptocurrencies all reject normality (low KS p-values, kurtosis 5.8–14.4), confirming Gaussian diffusions are inadequate — this is negative evidence against BS-based MEV estimators, not evidence that the jump model is correctly specified.

## Falsification plan

Research-defined tests (thresholds chosen by this Scout unless stated; all are prospective, none run):

1. **Replication of Table 1 on a fresh window.** Fit the 7-parameter model on a new pool/window (e.g., Uniswap V2 USDC–WETH, six months 2026), recompute expected arb volume/profit, and compare against heuristic-classified on-chain arb. *Research-defined failure rule:* if the model's predicted arb volume falls more than 2× below or 3× above the heuristic benchmark on the new window (same tolerance direction as the source's own ≈2× overestimate), the jump-augmented claim fails to generalize.
2. **Jump-dominance test.** Split realized swap events into jump vs diffusion intervals using an independent jump detector (e.g., Lee–Mykland at 1% significance) and compare arb-attributable volume across both. *Research-defined falsification threshold:* if jump-interval arb volume is not at least 2× the diffusion-interval arb volume per unit time, the "jumps drive arbitrage" mechanism is materially weakened.
3. **Saturation audit.** Reconstruct builder payments (priority fees + coinbase transfers + bundle rebates) relative to gross arb profit across a sample of pools. *Research-defined falsification threshold:* if median builder payment / estimated gross arb profit is below 0.5, the saturation claim fails (arbitrageurs would be retaining most of the surplus).
4. **Block-time test.** Compare MEV-attributable arb volume on Ethereum L1 (12s) against L2 venues (2s) for the same pairs over an overlapping window. *Research-defined threshold:* a >50% reduction in per-day arb volume per unit TVL on the faster venue falsifies ("shorter block times unlikely to reduce MEV") as a general statement; a reduction <20% is consistent with it.
5. **Noise-trader confound.** Re-run the volume attribution adding an explicit exogenous noise-trade process (e.g., retail flow estimator); if most volume previously attributed to arbitrage is re-assigned to noise traders, the ≈50%-of-volume claim fails.
6. **Inconsistency reconciliation gate (applies before any further use of jump parameters).** Re-fit parameters from the authors' code on the same input data; if neither the main-text nor the Table 5 parameters can be reproduced, treat all jump parameters as unusable and rely only on the qualitative claims.
7. **What follows failure:** any failed test above sends the associated claim (attribution share, saturation, jump dominance, block-time invariance) back to wiki intake as contested; no strategy inference from this record may be promoted to implementation regardless, until an independent net-of-cost backtest exists.

## Crypto portability

`direct`

The source is crypto-native (Ethereum L1 AMM + centralized exchange reference prices). Portability notes:
- Spot AMM, CPMM (Uniswap V2 invariant); concentrated liquidity (v3+) changes the trade-size-versus-mispricing mapping and is explicitly out of scope.
- L2/rollup execution (lower fees, sequencer ordering) is out of scope in the source; MEV structure there (priority-fee auctions vs sequencer policies) differs materially from L1 PBS.
- The CEX leg is modeled only through the effective spread `γ_CEX`; cross-venue fragmentation, withdrawal/bridge frictions, and CEX-side adverse selection are not modeled.
- 24/7 trading and 12-second block timing are handled via a second-denominated discrete-time model — fine for L1, needs re-derivation for other block cadences.
- Funding/margin mechanics are not relevant to the modeled trade (no perpetual exposure).

## Limitations

- **Not independently reproduced.** All quantitative claims are source-reported.
- **data gap — parameter inconsistency:** Section 4.1 main-text jump parameters (q=0.045 per 1-second step; mean −24.9%; sd 15.7%) are not reconcilable with Table 5 (τ=2.0: q=0.0411 per 12-second step; μ_J=−0.2035; σ_J=0.1952). Until reconciled via the code, neither set should be used as calibrated values.
- **data gap — effective spread:** γ_CEX is "not precisely known"; headline volume/profit shares move materially across the authors' own 0–30 bp sensitivity grid.
- **Sample size:** one pool, 17 days of head-to-head empirical comparison; the jump-statistics window (Nov–Dec 2024) is a different period from the arb study (Sep 2025). Figure 6's caption says Nov–Dec 2024 while its body text says Nov–Dec 2025 — an internal inconsistency; both flagged, neither resolved.
- **underspecified:** transaction routing, order types, queue behavior, gas bidding, and the actual net PnL of a specific searcher are not specified; the paper's objects are expected values under stationarity.
- **Model class limits:** excludes noise traders; assumes a single representative arbitrageur per opportunity; assumes Gaussian jump-size fits to a heavy-tailed, skewed empirical distribution (appendix rejects normality); L1-only, V2-only.
- **Attribution risk:** the empirical arb rows depend on third-party heuristics and Dune-style queries; the paper's own thesis is that these mislabel a material share of trades, so both their input data and any concluder using them are estimates.
- **No net-of-fee, net-of-gas strategy result:** the paper does not present a tradable net PnL strategy for a marginal entrant; gross model profit and observed MEV are the reported objects.

## Implementation status

Not implemented. No PyBroker, NautilusTrader, paper, testnet, or live implementation in our stack; no code from gitlab.com/jtapolcai/sde_amm has been executed. No attempt made to reproduce the SPD integration or Table 1. `implementation_status: not-implemented`.

## Adoption boundary

Research material only. This record does not mean the CEX–DEX arbitrage mechanism is profitable, validated, approved for implementation, paper trading, testnet, or live trading. Any threshold, entry/exit rule, filter, latency budget, or sizing choice not present in the source is explicitly research-proposed. Adoption remains a separate explicit decision.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` (schema specification)
- `[[quant/crypto-cex-dex-arbitrage-subsecond-latency-risk-compression-2026-09-01]]` (related CEX-DEX topic; source identity: Adadurov et al., arXiv:2601.00738 — materially distinct: latency/subslot execution risk, not MEV attribution)
- `[[quant/crypto-cex-dex-priority-fee-stochastic-delay-mixed-control-2026-09-01]]` (related CEX-DEX topic; source identity: Bergault et al., arXiv:2602.10798 — materially distinct: mixed impulse-control execution with priority fees)
- `[[quant/defi-amm-jump-diffusion-lvr-decomposition-optimal-block-time-2026-09-01]]` (jump-diffusion AMM LVR from the LP/block-time perspective; source identity: Bundi, arXiv:2608.30321 — distinct hypothesis: planner block-time optimum vs arbitrageur-side MEV quantification)
- `[[quant/crypto-amm-loss-versus-rebalancing-lvr-toxic-arbitrage-2026-08-31]]` (LVR/toxic-arbitrage foundation)
- `[[quant/crypto-bounded-liquidity-lvr-harmonic-arbitrage-2026-09-01]]` (related LVR bounds)

Material-distinction statement for dedup: no existing repository record shares this source identity. The two closest CEX–DEX records above analyze execution/latency control for the same trade venue family but do not test the MEV-attribution and saturation hypotheses that are the core of this capture; the jump-diffusion AMM records quantify LP-side loss, not the arbitrageur/MEV side.

## Sources

1. Bence Ladóczki, Miklós Rásonyi, and János Tapolcai, "Where Does MEV Really Come From? Revisiting CEX–DEX Arbitrage on Ethereum", arXiv:2604.15973v1 [cs.CR], submitted 2026-04-17; presented at Financial Cryptography and Data Security 2026. https://arxiv.org/abs/2604.15973 · PDF: https://arxiv.org/pdf/2604.15973 (Table 1 p. 3; Table 4 and Figure 6 in appendix; Table 5 p. 27; Section 4.1 pp. 12–14; Section 4.2; Section 5).
2. LaTeX source of the same paper (used to verify Tables 1, 4, 5, Figure 2 legend values, and the author list): https://arxiv.org/e-print/2604.15973 (retrieved 2026-09-15).
3. Reference implementation: https://gitlab.com/jtapolcai/sde_amm (branch main; most recent commit fc767aba289a41c79217087861c7efda100a03ae, retrieved 2026-09-15).
4. Wu et al. (2025) heuristic CEX–DEX arbitrage classification used for the empirical benchmark rows of Table 1 (as cited by the source; not separately inspected).
