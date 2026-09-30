---
schema: strategy-research-record-v1
title: "Not All LPs Are Equal: LP-Side Active-Passive Markout Decomposition of Uniswap Liquidity Provision and Passive-Markout Pool Selection"
created: 2026-09-30
updated: 2026-09-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-29
sources:
  - https://arxiv.org/abs/2609.37963
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Table 7's column is labelled 'active LIFO volume (%)' but its values are Table 5's 'active exact volume (%)' column: all 17 shared rows match the exact column to the printed 2 decimals, and 12 of 17 rows differ from Table 5's own active-LIFO column (Base USDC-WETH 5 bps 3.56 vs 3.82, Arbitrum USDC-WETH 5 bps 0.01 vs 0.03, Ethereum USDC-WETH 5 bps 1.30 vs 1.36, USDT-WETH Ethereum 5 bps 1.16 vs 1.23, USDC-WBTC Ethereum 5 bps 1.78 vs 1.90, USDT-WBTC Ethereum 5 bps 1.14 vs 1.25, and six more). Section 5.1's sentence 'The biggest active share in v3 is Base USDC-WETH 5 bps with 3.56%' inherits the exact-method value under an LIFO label."
  - "Table 5 covers 19 Uniswap v3 pools while Table 3 (main results) and Table 7 (descriptive statistics) cover 17. The two extra rows are USDC-WBTC Ethereum 1 bps (active LIFO 0.06, active exact 0.03, passive LIFO -2.962705, passive exact -2.960789) and USDT-WBTC Ethereum 1 bps (active LIFO 1.05, active exact 0.97, passive LIFO -4.239112, passive exact -4.263411), two of the most negative passive markouts in the paper, with no explanation for their exclusion from the main and descriptive tables."
  - "The cross-table identity total($)/overall(bps) = descriptive total volume holds for 38 of the 39 printed pool rows (maximum relative error 0.00320) and fails for exactly one: Uniswap v2 USDC-WETH Base 30 bps, where Table 2's 173,731 USD and 20.822100 bps imply 83,435,869 USD against Table 6's 515.67M (relative error 0.838); equivalently 515.67M x 20.8221 bps = 1,073,730 USD, not 173,731. Which of the three cells is wrong cannot be decided from the source."
  - "Section 5.2 states the active-passive gap in v3 'is most prominent in Ethereum pools, especially at the 5 bps tier' and Section 6 repeats 'the largest gaps on Ethereum and at the 5bps tier', but Table 3's Ethereum 1 bps pools carry larger gaps than every 5 bps pool (USDC-WETH 1 bps +0.474251 and USDT-WETH 1 bps +0.501639 against a maximum 5 bps gap of +0.453938, recomputed from the printed cells). The 1 bps pools are excluded from the figures as 'extreme outliers' in Section 5.2, but that exclusion is never carried into the Section 5.2 or Section 6 prose claims."
  - "The same pool is labelled 'USDC-WBTC' and 'USDT-WBTC' in Tables 3, 4, 5, 6, 7 and 8 but 'WBTC-USDC' and 'WBTC-USDT' in Table 9 and in the legends of Figures 1, 2 and 3, so row identity across the robustness table, the figures and the main results must be reconstructed by token set rather than by label."
---

# Not All LPs Are Equal: LP-Side Active-Passive Markout Decomposition of Uniswap Liquidity Provision and Passive-Markout Pool Selection

## Provenance

**Primary source (pinned this run, 2026-09-30):** arXiv:2609.37963v1 `[q-fin.TR]`.

- Abstract page: `https://arxiv.org/abs/2609.37963` -- HTTP 200, **44,106 bytes**, SHA-256 `3b350a9b993cde0c945936ee82876a5001e9de6cf8f6d0abf18dad750856f61f`.
- PDF: `https://arxiv.org/pdf/2609.37963` -- HTTP 200, **1,966,973 bytes**, SHA-256 `8041263ff3dd8312ddeaef317a284b76bc902bbc15e50476f92e7e3294683d66`, extracted with pypdf 6.16.2 into **33 pages and 85,936 characters of page text, written out as an 86,230-byte / 1,534-line file with page separators and read end to end**: the title page and Abstract, Sections 1 through 6, the 17-item Bibliography, Tables 1 through 9 (every cell parsed), the Figure 1 through Figure 6 captions, and Appendices A through I. PDF metadata: `/Title` byte-identical to the printed title, `/Author` = `Agathe Sadeghi; Dingyue Liu; Ciamac Moallemi; Xin Wan; Brian Zhu`, `/arXivID` = `https://arxiv.org/abs/2609.37963v1`, `/DOI` = `https://doi.org/10.48550/arXiv.2609.37963`, `/License` = `http://creativecommons.org/licenses/by/4.0/`.
- arXiv API: `https://export.arxiv.org/api/query?id_list=2609.37963` -- **3,422 bytes**, SHA-256 `b329bf354a017f852fd7f51d20d084a59f26b79449c37aa31a7fc746f0f6d2b7`.

**Title (exactly as printed on page 1, in the abstract page and in `citation_title`):** *Not All LPs Are Equal: The Active-Passive Gap in Automated Market Maker Liquidity Provision*.

**Authors (exactly as printed, page 1 and the five `citation_author` meta tags):** `Agathe Sadeghi`, `Dingyue Liu`, `Ciamac Moallemi`, `Xin Wan`, `Brian Zhu`. Affiliations printed on page 1: `1 Uniswap Labs`, `2 Columbia University`; the author block assigns Sadeghi `1`, Liu `1`, Moallemi `2,1`, Wan `1`, Zhu `2`, i.e. **four of five authors carry a Uniswap Labs affiliation** and Moallemi carries both. No ORCID, no author email (`orcid` = 0 occurrences in the pinned text).

**Version / date:** abstract dateline `[Submitted on 29 Sep 2026]`; submission history `[v1] Tue, 29 Sep 2026 16:34:10 UTC (1,695 KB)`; arXiv API `<published>2026-09-29T16:34:10Z</published>` and `<updated>2026-09-29T16:34:10Z</updated>` (single version, no v2); `citation_date` and `citation_online_date` both `2026/09/29`; PDF first-page footer `arXiv:2609.37963v1 [q-fin.TR] 29 Sep 2026`. The `1,695 KB` submission-history figure is the arXiv source-package size, not the served 1,966,973-byte PDF (**data gap**, not a contradiction).

**Subjects:** `Trading and Market Microstructure (q-fin.TR)` -- single subject, primary, no cross-lists.

**Comments field:** cell absent from the abstract page and `<arxiv:comment>` absent from the API record -- **no page/figure/table count is stated by arXiv** (the PDF itself carries 6 numbered figures and 9 numbered tables).

**Publication / licence status:** `journal-ref` cell absent; API `<arxiv:journal_ref>` absent; API `<arxiv:doi>` absent; the abstract page's DOI cell carries only the arXiv-issued value with the tooltip `arXiv-issued DOI via DataCite (pending registration)`; `peer` = 0 occurrences in the pinned text, so there is **no peer-review statement** -- **preprint only, no publisher DOI**. Licence: the abstract page `div.abs-license` links `view license` to `http://creativecommons.org/licenses/by/4.0/` and the PDF metadata `/License` carries the same URL (**CC BY 4.0**). Together with the linkifier-artefact href quoted under the rendering note below, these are the only two non-HTTPS strings in this record and both are preserved literally from the source.

**Rendering artefact observed on the landing page (not treated as a contradiction):** the abstract page's `blockquote` renders the sentence fragment `aggregate pool profitability. In Uniswap v2` as `aggregate pool <a href="http://profitability.In">this http URL</a> Uniswap v2`, i.e. arXiv's linkifier fired on `profitability.In`. Both `<meta name="description">` copies on the same page and the pinned PDF read `aggregate pool profitability. In Uniswap v2`, so the artefact is confined to the landing-page blockquote and the PDF wording is authoritative.

**Code / data availability:** `repository` = 0, `github` = 0, `code` = 0, `data availability` = 0, `declaration` = 0, `declarations` = 0, `acknowledg` = 0, `competing` = 0, `interest` = 0, `conflict` = 0, `orcid` = 0 occurrences in the pinned 85,936-character text. There is **no competing-interests statement, no funding statement, no acknowledgments, no data-availability statement, no code-availability statement and no repository URL** -- all **data gap**. The only named data inputs are `Allium` (1 occurrence: "we collect version specific Uniswap event logs from Allium. We do not operate independent nodes on any of the chains") and `Binance` spot order-book prices (4 occurrences); neither was fetched this run.

**Sample period / universe (Section 3.2):** "Our dataset covers Ethereum Mainnet, Arbitrum, and Base over the period from February 1st to November 30th, 2025." Pools are selected to share the benchmark assets `WETH, USDC, USDT, WBTC and cbBTC`, across fee tiers "mainly 5 bps and 30 bps, and 1 bps where available on Ethereum", excluding "pools with total sample-period volume below $10 million". Table 2 reports 5 Uniswap v2 pools, Table 3 reports 17 v3 pools, Table 4 reports 16 v4 pools (**38 pool rows in the main results**), while Table 5 reports 19 v3 pools. Robustness runs use "a data vintage extending through December 1st, 2025" (footnote 6) and omit the Ethereum 1 bps pools.

**Transaction-cost treatment (determined at Methods level):** Section 1 states that "profitability means fee-inclusive, short-horizon LP profit and loss measured through markout" and that "Markout also excludes gas, liquidity-management, and capital costs and inventory revaluation outside the horizon - second-order for passive positions, though material for the realized profit of active strategies"; Section 4.1 restates "the markout is from the LP perspective and includes fees but excludes gas costs". So the **only** modelled friction is the pool fee tier inside a fee-inclusive markout, and gas, liquidity-management and capital costs are **explicitly excluded by the source** rather than left unstated. Full census in Execution assumptions.

**Source-identity deduplication (whole repository, before writing, 2026-09-30):** `rg -uuu -F` across the entire checkout including `.git`, `.mimo-worktrees`, `.agents`, `.hermes` and `coverage_manifest.csv`.

- `2609.37963` -> **0 files**; `10.48550/arXiv.2609.37963` -> **0 files**; `Not All LPs Are Equal` -> **0 files**; `NotAllLPs` -> **0 files**; `Active-Passive Gap` -> **0 files**; `active-passive gap` -> **0 files**; `Dingyue Liu` -> **0 files**; `LIFO subtraction` -> **0 files**; `infinitesimal LP` -> **0 files**; `markout-based framework` -> **0 files**.
- `Agathe Sadeghi` -> **3 files before this write and 4 after**: `defi-cpmm-oracle-liquidation-dynamics-fee-oev-protection-2026-09-10.md`, whose source is Sadeghi & Feinstein, *Liquidation Dynamics in DeFi and the Role of Transaction Fees*, arXiv:2602.12104 -- a different paper by the same first author -- plus its two `.mimo-worktrees` copies; the fourth file is this record.
- `Ciamac Moallemi` -> **1 file before this write and 2 after**: `vol-conditional-liquidity-provision-reversal-micro-price-execution-overlay-2026-09-23.md`, whose sources are Bryan Vine's GitHub alpha-research paper 5 -- a different source that merely cites Moallemi; the second file is this record.
- `Sadeghi` -> **6 files before this write and 7 after**: the two records above (one top-level markdown plus two `.mimo-worktrees` copies each), `oracle-parametrized-cfmm-ga-lvr-depth-pareto-spy-nbbo-arxiv-2609.33799-2026-09-30.md` (Amini & Feinstein, another different source), two `.git` log files, and this record.
- `coverage_manifest.csv` (5,808 lines) -> **0** for `2609.37963`, `Not All LPs`, `Sadeghi`, `active-passive`, `LIFO subtraction`, `infinitesimal`.
- Positive control `novy-marx` -> **46 files** whole checkout / **43 markdown files** before this write, and **47 / 44** after, the sole increment being this record's own dedup sentence.
- **Post-write re-scan:** each of the ten identity probes above (`2609.37963`, `Not All LPs Are Equal`, `NotAllLPs`, `Active-Passive Gap`, `active-passive gap`, `Dingyue Liu`, `LIFO subtraction`, `infinitesimal LP`, `markout-based framework`, `10.48550/arXiv.2609.37963`) returns **exactly this record and nothing else**, and a top-level `*.md` scan for `2609.37963` returns only this record; the six `coverage_manifest.csv` probes still return 0, so the manifest has no row for this source.
- `git log --oneline -20` was inspected as a convenience glance only and does **not** by itself satisfy dedup. `git pull origin main` at run start returned `Already up to date` at `164b1bf`, and was re-run before commit.

**Conclusion:** no existing record has this source identity, so a new record is admissible under the dedup contract.

## Economic mechanism

### Source-reported

The source is an **LP-side measurement paper**, not a directional-return paper. Its stated mechanism has three linked parts.

1. **Aggregate pool statistics conflate heterogeneous LP outcomes.** Existing empirical work "largely focused on trader-side flow toxicity ... The LP-side decomposition - how these losses are distributed across different types of liquidity providers - remains underexplored." Because "aggregate LP profitability statistics conflate the returns of sophisticated active strategies with those of passive capital, potentially masking the true economic costs faced by the majority of liquidity providers", a pool-level markout number is not the markout a passive LP actually earns.

2. **Adverse selection in AMMs is a specific, measurable channel.** Classical theory has liquidity providers "earn the spread from uninformed traders but lose to better-informed ones"; in AMMs "arbitrageurs trade against deterministically stale on-chain prices whenever the external market moves, a cost formalized as loss-versus-rebalancing (LVR)". Concentrated liquidity (Uniswap v3, preserved in v4) "opened a spectrum of strategies around this cost": at one extreme JIT providers "mint a position immediately before a swap and burn it immediately after", at the other passive LPs "supply liquidity continuously and absorb informed and uninformed flow indiscriminately". The paper defines dollar markout `M_s = q_s,in * p_in,h - q_s,out * p_out,h` and raw markout `mu_s = (p_s,b,h - p_e) / p_s,b,h`, where `p_e` is the execution price and `p_b,h` the benchmark ratio from CEX quotes at horizon `h`; "A positive markout means the pool received more value than it delivered when both legs are valued at subsequent reference prices, and is favorable to the LP; a negative markout is a short-horizon adverse-selection loss."

3. **Two complementary estimators of the passive component.** (a) **LIFO subtraction**: identify *active* liquidity as positions whose burn equals their mint inside a matching horizon `T = 20 seconds` on all chains, stack outstanding additions per position tuple `(Chain, Pool, tau_l, tau_u, LP)` and match each removal last-in-first-out, then attribute each swap's markout to legs by the liquidity-share weight `w_act_{s,a} = L_{s,a}/L_s`, with the passive component the residual `w_pass_s = 1 - sum_a w_act_{s,a}`. (b) **Infinitesimal LP benchmark**: simulate a hypothetical full-range LP contributing infinitesimal liquidity whose token flows follow directly from the constant-product reserve change between the pre- and post-swap pool prices, divided by `1-f` for v3/v4 fee handling and treated separately for v2 where the fee is embedded in reserves; this method "makes no assumptions about active LP behavior". The two estimators are constructed from different objects (one removes identified active liquidity ex post, the other simulates an idealized passive LP along the realized price path), and the source reads their directional agreement as evidence that "the gap is a feature of the data rather than an artifact of a single identification strategy."

**Stated empirical pattern (Sections 5, 6 and Appendices F, I):** in v2, where "active LP behavior" is not identified, aggregate and passive markouts coincide; in v3 and v4 "a systematic active-passive gap opens up: passive LPs systematically underperform pool-aggregate markouts, with the largest gaps on Ethereum and at the 5bps tier"; the gap "is wider on Ethereum than on L2s, consistent with shorter L2 block times reducing the adverse selection rents active LPs can capture"; and "passive LPs perform better on higher fee pools". The source explicitly frames the cross-chain comparison as "descriptive rather than causal" and offers "block times, gas costs, liquidity depth, user and flow composition, MEV infrastructure and the set of active LPs participating on each chain" as unreconciled channels.

**Stated operational uses (Appendix I, verbatim in substance):** a "rolling-window pool monitor" that computes the infinitesimal passive markout "over a trailing day or week" and treats "the lower bound of the associated confidence band as a decision threshold for exiting a position"; the inverse procedure for "pool selection ex ante, ranking candidate pools, fee tiers, and chains by realized passive markout per dollar of TVL over a recent reference window"; and, for the active-versus-passive capital decision, "the realized gap between active and passive markout from the LIFO decomposition gives an estimate of the rent available to strategic provision."

### Research interpretation

This record captures a **liquidity-allocation hypothesis**, not a price-direction premium. Two falsifiable claims are separated because they can fail independently.

- **H1 (LP-side measurement hypothesis).** In concentrated-liquidity AMMs, the aggregate pool markout systematically overstates the markout earned by a passive, always-in-range LP, because short-lived actively repositioned liquidity absorbs a disproportionate share of the favourable side of the flow. If true, pool selection and LP monitoring must be run on a passive-only estimator, and any pool-screening rule built on aggregate markout is biased. Mechanism class: **adverse-selection rent distribution across LP activity classes**, i.e. a microstructure/measurement channel, not a risk premium.
- **H2 (chain-structure hypothesis).** The size of that gap is governed by the execution environment: chains with faster block times and cheaper repositioning (L2) show a smaller gap than Ethereum mainnet, because active LPs there capture less timing rent. If true, the gap is a predictable function of block time and gas rather than an idiosyncratic pool property. Mechanism class: **market-structure / latency-of-repositioning**.

Component roles, with source-vs-research labels:

```text
Regime:            chain and fee tier -- Ethereum vs Arbitrum vs Base, and the 1/5/30 bps
                   fee tiers (source-reported, Sections 5.2, 6, Appendix F)
Primary signal:    rolling-window passive markout (infinitesimal estimator) per dollar of
                   TVL, used to rank pools ex ante and to set an exit threshold on the
                   lower confidence bound (source-reported, Appendix I)
Secondary signal:  overall minus passive LIFO markout, used as the estimated "rent
                   available to strategic provision" before committing capital to active
                   management (source-reported, Appendix I)
Identification:    LIFO mint-burn matching at T = 20 s (robustness T = 60 s and FIFO) for
                   the active component; infinitesimal full-range benchmark for the
                   passive component (source-reported, Section 4.2, Appendices C, G)
Risk / exit:       "lower bound of the associated confidence band" as a decision threshold
                   for exiting a position (source-reported, Appendix I; the confidence
                   level is 95% by Appendix C)
Cost layer:        fee-inclusive markout only; gas, liquidity-management and capital costs
                   are EXCLUDED by the source (source-reported, Sections 1 and 4.1);
                   any gas/MEV/rebalance cost ladder below is research-proposed
```

**Alpha translation.** The executable content of the source is a **capital-allocation rule**: choose which pools to provide liquidity to, when to withdraw, and whether the rent from active repositioning justifies its cost. There is **no short leg and no directional price view** -- the "position" is long-only pool liquidity, and the bet is on which pool's passive capital earns the better fee-net-of-adverse-selection outcome. Every threshold, window length, ranking tie-break, position size and cost input that is not quoted in Appendix I is `research-proposed`, and every pass/fail cutoff in the falsification plan is `research-defined`.

## Signal

Everything in this section is `source-reported` unless explicitly prefixed `research-proposed`.

**Formation timestamp and tradability**

- The unit of observation is an on-chain `Swap` event, ordered "lexicographically by block number, transaction index, and log index", so execution sequence inside a block is preserved even when timestamps collide. "The swap timestamp used in the markout calculation is the canonical block timestamp as provided by the data source. It is not a transaction receipt timestamp."
- The markout is evaluated at `t + h` against the "last quote at or before `t+h`" from a second-level Binance USDT top-of-book mid per token; "We remove the swaps for which no admissible quote is available" (Section 3.2).
- The exit/entry decisions of Appendix I are **retrospective** for the LIFO estimator ("best treated as retrospective rather than real-time tools") and **block-by-block capable** for the infinitesimal estimator ("can be computed block-by-block from any Ethereum or L2 RPC with negligible overhead").

**Lookback windows**

- Markout horizon `h = 15 seconds` across all chains, "measured in elapsed time rather than blocks". Appendix H re-estimates at `0 s, 15 s, 1 m, 5 m, 1 h, 4 h, 6 h` and states the profile "is flat from 0 seconds out to roughly one hour" with `4 h` and `6 h` points "noise-dominated".
- Matching horizon `T = 20 seconds` on all chains; robustness at `T = 60 seconds` and with a FIFO queue instead of a LIFO stack (Appendix G).
- Monitor window: "a trailing day or week" for the rolling monitor; "a recent reference window" for ex-ante ranking. **The source offers two window lengths and never chooses between them, and never defines "recent" -- `underspecified`.**
- Sample: `2025-02-01` to `2025-11-30` (inclusive as stated), with robustness runs on a vintage "extending through December 1st, 2025".

**Estimator construction (all `source-reported`)**

- Active identification: a position `(wallet, pool, price range)` is active if "the total liquidity level burnt equals the total liquidity level minted in a given price range on a given pool, and all mint and burn transactions occur within `T` seconds".
- Position tuples: v2 `(Chain, Pool, LP)`, v3 `(Chain, Pool, tau_l, tau_u, LP)`, v4 `(Chain, Pool, tau_l, tau_u, salt)`; v4 `ModifyLiquidity` signed `LiquidityDelta` plays the role of mint/burn.
- Coverage: a leg `a` covers swap `s` iff `o(mint_a) < o(s) < o(burn_a)` in on-chain order and (v3/v4) `tau_l,a <= tau_s < tau_u,a`; weight `w_act_{s,a} = L_{s,a}/L_s`.
- Passive aggregate = total minus active, aggregated at swap level before the volume-weighted mean is taken; reported as `M_pass = sum(M_s^pass) / sum(V_s^pass)` in bps.
- Infinitesimal: reserve-change derivation with `q_in = delta/(1-f)` for v3/v4, full-input treatment for v2, unit liquidity `L = 1`, **excluding** swaps whose absolute internal pool price movement exceeds `20%` and **excluding** standard and same-transaction sandwich attacker legs and their victim swaps.
- Uncertainty: volume-weighted mean with ratio-estimator standard error, reported as `m +/- 1.96 SE(m)`; the difference `D = m_all - m_pass` is linearized directly through per-swap influence contributions `d_s` and reported as `D +/- 1.96 SE(D)`; Appendix H additionally reports a calendar-day cluster bootstrap with **5,000 replicates** and 2.5/97.5 percentiles.

**Decision rules (Appendix I, source-reported but qualitative)**

| Role | Rule as printed | Status |
|---|---|---|
| Exit | compute the trailing-window infinitesimal passive markout and "treat the lower bound of the associated confidence band as a decision threshold for exiting a position" | object source-reported; window, confidence band choice and sizing `underspecified` |
| Entry / selection | "ranking candidate pools, fee tiers, and chains by realized passive markout per dollar of TVL over a recent reference window" | ranking statistic source-reported; window, tie-break, TVL source and minimum rank depth `underspecified` |
| Active-vs-passive capital decision | "the realized gap between active and passive markout from the LIFO decomposition gives an estimate of the rent available to strategic provision" | gap source-reported; the comparison against the cost of active management is **not performed by the source** |
| Position sizing | none printed | **absent** -- any sizing is `research-proposed` |
| Re-entry / cooldown / rebalance cadence | none printed | **absent** |
| Short leg | not applicable; liquidity provision is long-only | n/a |

**Underspecified in the source:** the monitor window (`day` vs `week`), what "recent" means, whether the exit band is the analytical normal interval or the day-block bootstrap band, whether the ranking is by level or by a lower confidence bound, the TVL source, measurement time and definition, the handling of the Ethereum 1 bps pools in any live monitor, position sizing, rebalance cadence, and any rule for switching fee tiers or chains. **No parameter-tuning protocol, no train/test split and no out-of-sample selection procedure are printed** (`walk-forward` = 0, `holdout` = 0, `hold-out` = 0, `seed` = 0).

## Required data

- **Instrument / universe:** liquidity positions in Uniswap v2, v3 and v4 pools over the pairs `USDC-WETH`, `USDT-WETH`, `USDC-cbBTC`, `USDC-WBTC`, `USDT-WBTC`, with `WETH, USDC, USDT, WBTC and cbBTC` named as the benchmark asset set; fee tiers "mainly 5 bps and 30 bps, and 1 bps where available on Ethereum"; pools with sample-period volume below `$10 million` excluded. Reported set: 5 v2 + 17 v3 + 16 v4 = **38 pool rows** in Tables 2-4, 19 v3 rows in Table 5.
- **Venue / market type:** decentralized, on-chain AMM pools on **Ethereum Mainnet, Arbitrum and Base**; no CEX order book is traded. The external reference is a CEX.
- **Timeframe:** `Swap`, `Mint` and `Burn` (v2/v3) and `ModifyLiquidity` (v4) event logs at block/transaction/log granularity over `2025-02-01` to `2025-11-30`, plus robustness vintage to `2025-12-01`.
- **Fields actually used (Section 3.2, all `source-reported`):** chain, pool/contract identifier, block number, block timestamp, transaction hash, transaction index, log index, and version-specific event fields (amounts, tick ranges, liquidity deltas, fee tier, in-range liquidity recorded on the swap event); external `Binance` spot order-book top-of-book bid and ask per token at one-second granularity, converted to a USDT mid and then to a cross-token benchmark ratio; chain and block-time context (Ethereum ~12 s, Arbitrum ~250 ms, Base ~2 s plus ~200 ms flash-block preconfirmations).
- **Fields required but not sourced by the paper:** **TVL**, which Appendix I's ranking rule needs ("per dollar of TVL") and which the paper uses three times (Sections 6 and I) but **never defines, never dates and never cites a source for** -- `data gap`.
- **Fields NOT used:** no order book on the venue itself, no depth on the AMM, no trades with aggressor side, no open interest, no funding rate, no mark/index/basis, no options surface/Greeks, no borrow, no on-chain sentiment or governance data, no CEX perpetual data.
- **Point-in-time / availability:** events are read in on-chain order with the canonical block timestamp, which "is not a transaction receipt timestamp"; the benchmark is "the last quote at or before `t+h`". There is no publication-vintage problem for on-chain events, but **swaps with no admissible Binance quote are dropped, and the size and composition of that dropped set are never reported** -- `data gap`.
- **Timestamp / timezone:** block timestamps are used as given; no timezone, clock-source, precision or out-of-order policy is stated beyond the lexicographic ordering rule -- `data gap`.
- **Missing data:** no null, stale, partial or bad-print rule is printed beyond the no-admissible-quote exclusion; imputation policy not specified -- `data gap`.
- **Cost / fee / spread fields:** the pool fee rate `f` is required (and is). There is **no** gas price, no liquidity-management cost, no capital cost, no slippage, no impact and no funding input anywhere in the data requirements; the source states these are excluded from markout.
- **Third-party data actually used:** version-specific Uniswap event logs from **Allium** (commercial vendor; "We do not operate independent nodes on any of the chains") and **Binance** spot order-book data. Neither was fetched this run; their exact contents, filters and access path are `data gap`.

## Execution assumptions

Determined at Methods level from Sections 1, 3.2, 4.1, 4.2, 5.2, Appendices C, G, H, I and Tables 1-9, plus a substring and word-boundary census of the pinned 85,936-character text layer.

- **Signal-to-order timing:** the measurement is retrospective per swap (`t + h`, `h = 15 s`); the Appendix I monitor is described as real-time capable for the infinitesimal estimator and "retrospective rather than real-time" for the LIFO estimator. No latency model is built.
- **Order type / fill model:** **not applicable in the source's own terms** -- LP actions are on-chain mint/burn transactions, not resting orders. `limit order` = 1 occurrence, and that single occurrence is the theoretical remark that "AMMs replace discrete limit orders with deterministic pricing curves"; `market order` = 0, `order type` = 0, `fill` = 0, `taker` = 0, `queue` = 0, `participation` = 0.
- **Fees:** the pool fee tier (`1/5/30` bps) is **included** in markout by construction ("fee-inclusive"; the infinitesimal method divides the curve-implied input by `1-f` for v3/v4 and treats v2's embedded fee separately). `fee` = 61 substring hits, `fees` = 21 -- all pool fee tiers, fee revenue or fee-tier design, never an exchange fee schedule.
- **Gas / capital / management cost:** **explicitly excluded** (Sections 1 and 4.1), and the source itself says the exclusion is "material for the realized profit of active strategies". `gas` = 10 occurrences, all discussion of gas as a chain property or a confound, never as a cost input.
- **Slippage / spread / impact / commission / bid-ask / funding / leverage / borrow / liquidation / turnover / capacity / latency:** `slippage` = **1**, inside the cited statement that JIT liquidity "reduces trader slippage"; `spread` = **3**, all classical-microstructure prose ("earn the spread", "the spread compensating for adverse selection", "the empirical analogue of a realized spread") and never a bid-ask or price-spread measurement; `market impact` = **0**; `impact` = **1** ("it does not impact the price changes caused by on-chain swaps"); `commission` = **0**; `bid-ask` = **0**; `transaction cost` = **0**; `funding` = **0**; `leverage` = **0**; `borrow` = **0**; `liquidation` = **1**, inside a related-work sentence about DEX liquidations; `turnover` = **0**; `capacity` = **0**; `latency` = **1**, describing chain latency as sample variation; `maker` = **11**, all inside "automated market maker(s)" or "market-maker", never a maker/taker fee. **Conclusion: the only modelled friction is the pool fee tier inside a fee-inclusive markout; gas, liquidity-management and capital costs are excluded by declaration; every other monetary friction is a `data gap` and must not be read as zero-cost evidence.**
- **Capacity / impact:** `capacity` = 0 and `turnover` = 0; nothing in the source addresses how much passive capital a pool can absorb or whether the reported bps are achievable at size -- `data gap`.
- **Leverage / margin / shorting / borrow:** not applicable to the source's long-only LP framing; no leverage modelled; `margin` = 6 occurrences, all the word "marginal" in "marginal LP" -- **not stated**.
- **Partial fills / failures:** not modelled; a mint either lands in a block or it does not, and no failure or reorg policy is printed -- `data gap`. Note also that the paper relies on canonical block timestamps and does not discuss reorg handling.
- **What the source assumes vs what a researcher must assume:** a `20 s` matching horizon, a `15 s` markout horizon, a full-range infinitesimal LP, sandwich and >20% price-move exclusions, a `$10M` pool floor, the benchmark-asset set and the Binance USDT numeraire are **source-assumed**; any gas ladder, MEV cost, TVL source, window choice, ranking tie-break, position size or exit confidence level used later is **research-proposed**.

## Evidence

### Source-reported

All figures below are read from the pinned 1,966,973-byte PDF and are **third-party claims**. Sample `2025-02-01` to `2025-11-30` unless a table's own note says otherwise. Universe: 38 Uniswap pools on Ethereum, Arbitrum and Base. **All markout numbers are fee-inclusive and gross of gas, liquidity-management and capital costs.** A positive gap means the passive LP does worse than the pool aggregate.

**Table 1 -- method comparison (attribute x method).** Rows: `Profiles passive LPs` Yes/Yes; `Profiles active LPs` Yes/No; `LP decomposition granularity` Swap-level / Swap-level passive only; `Passive markout CI` Yes/Yes; `Active markout CI` Yes/No; `Dollar scale of passive P&L` Yes / "No; only normalized P&L"; `Assumptions on active LP behavior` Yes/No; `Robust to sandwiches` Yes/No; `Data required to compute` "Mint, burn, and swap history" / "Time series of pool spot prices".

**Table 2 -- Uniswap v2 (5 pools; total dollar markout, overall bps, passive LIFO bps, infinitesimal bps, then the two 95% CIs).**

| Pool | Total ($) | Overall (bps) | Passive LIFO (bps) | Infinitesimal (bps) | Passive LIFO CI | Infinitesimal CI |
|---|---|---|---|---|---|---|
| USDC-WETH Base 30 bps | 173,731 | 20.822100 | 20.822080 | 20.866623 | [18.87, 22.78] | [19.01, 22.73] |
| USDC-WETH Arbitrum 30 bps | 22,013 | 19.153800 | 19.153833 | 18.283203 | [9.33, 28.98] | [9.15, 27.42] |
| USDC-WETH Ethereum 30 bps | 901,955 | 9.320400 | 9.320412 | 8.6150225 | [3.23, 15.41] | [3.5, 13.73] |
| USDT-WETH Arbitrum 30 bps | 22,895 | 21.486400 | 21.486375 | 17.455259 | [-1.78, 44.75] | [9.76, 25.15] |
| USDT-WETH Ethereum 30 bps | 973,349 | 9.329900 | 9.329889 | 7.6290297 | [-7.18, 25.85] | [-7.93, 23.19] |

Recomputed overall-minus-passive differences: `0.000020`, `0.000033`, `0.000012`, `0.000025`, `0.000011` bps -- consistent with Section 5's "overall and passive LIFO markouts are nearly identical" for v2, although Section 1's stronger "so aggregate and passive markouts **coincide** there" is only true to rounding while Table 6 prints `0.00` active share for all five pools.

**Table 3 -- Uniswap v3 (17 pools).** `Gap` is `overall - passive LIFO`, recomputed from the printed cells.

| Pool | Total ($) | Overall | Passive LIFO | Infinitesimal | Passive LIFO CI | Infinitesimal CI | Gap |
|---|---|---|---|---|---|---|---|
| USDC-WETH Base 5 | -1,476,525 | -0.681176 | -0.706874 | -0.990307 | [-0.81, -0.6] | [-1.79, -0.19] | +0.025698 |
| USDC-WETH Arbitrum 5 | -4,477,895 | -0.732521 | -0.769710 | -1.670802 | [-6.08, 4.54] | [-1.95, -1.4] | +0.037189 |
| USDC-WETH Ethereum 1 | 1,052,140 | 0.473692 | -0.000559 | -1.755563 | [-18.38, 18.38] | [-2.52, -0.99] | +0.474251 |
| USDC-WETH Ethereum 5 | -5,388,028 | -1.150404 | -1.506019 | -1.229423 | [-2, -1.02] | [-2.27, -0.19] | +0.355615 |
| USDC-WETH Ethereum 30 | -438,047 | -0.707246 | -0.866415 | 0.171106 | [-2.63, 0.9] | [-5.31, 5.66] | +0.159169 |
| USDT-WETH Base 5 | -5,256 | -0.574968 | -0.574969 | -1.011193 | [-1.34, 0.19] | [-2.22, 0.2] | +0.000001 |
| USDT-WETH Arbitrum 5 | -368,878 | -0.449665 | -0.449636 | -1.350178 | [-0.86, -0.04] | [-1.74, -0.96] | -0.000029 |
| USDT-WETH Ethereum 1 | 1,097,440 | 0.362955 | -0.138684 | -1.756175 | [-6.87, 6.59] | [-2.69, -0.83] | +0.501639 |
| USDT-WETH Ethereum 5 | -1,546,285 | -0.910758 | -1.309165 | -1.535256 | [-4.42, 1.8] | [-2.61, -0.46] | +0.398407 |
| USDT-WETH Ethereum 30 | 1,464,532 | 1.185598 | 1.001649 | 2.047672 | [-0.71, 2.71] | [-5.5, 9.6] | +0.183949 |
| USDC-cbBTC Base 5 | -252,298 | -0.568330 | -0.568331 | -0.625847 | [-0.77, -0.37] | [-1.32, 0.06] | +0.000001 |
| USDC-WBTC Arbitrum 5 | -354,545 | -0.589463 | -0.589305 | -1.474014 | [-12.73, 11.55] | [-2.51, -0.44] | -0.000158 |
| USDC-WBTC Ethereum 5 | 24,703 | 0.045536 | -0.408402 | -1.278491 | [-5.49, 4.67] | [-2.76, 0.21] | +0.453938 |
| USDC-WBTC Ethereum 30 | 481,238 | 0.524304 | 0.209764 | 9.906399 | [-1.4, 1.82] | [-1.72, 21.54] | +0.314540 |
| USDT-WBTC Arbitrum 5 | -384,921 | -0.722053 | -0.722146 | -1.279479 | [-0.85, -0.6] | [-1.71, -0.85] | +0.000093 |
| USDT-WBTC Ethereum 5 | 151,553 | 0.190694 | -0.254329 | -0.247134 | [-1.76, 1.29] | [-2.69, 2.19] | +0.445023 |
| USDT-WBTC Ethereum 30 | 649,333 | 2.705426 | 2.519784 | 3.164769 | [0.51, 4.53] | [-2.29, 8.62] | +0.185642 |

Recomputed from the printed cells: **15 of 17 gaps are positive** (median `+0.183949`, recomputed); the two non-positive rows are both Arbitrum and both are smaller than `0.0002` bps in magnitude. Section 5.2's two worked examples reproduce exactly: "USDC-WETH 5 bps goes from -1.15 bps overall to -1.51 bps for passive LIFO and USDT-WETH 5 bps goes from -0.91 bps to -1.31 bps".

**Table 4 -- Uniswap v4 (16 pools).**

| Pool | Total ($) | Overall | Passive LIFO | Infinitesimal | Passive LIFO CI | Infinitesimal CI | Gap |
|---|---|---|---|---|---|---|---|
| USDC-WETH Base 5 | -51,811 | -0.977900 | -0.977859 | -0.868197 | [-1.13, -0.82] | [-1.14, -0.6] | -0.000041 |
| USDC-WETH Arbitrum 5 | -288,235 | -1.431700 | -1.431670 | -1.875089 | [-1.5, -1.37] | [-2.16, -1.59] | -0.000030 |
| USDC-WETH Ethereum 1 | -17,974 | -0.042800 | -0.427445 | -2.612735 | [-15.61, 14.76] | [-5.42, 0.2] | +0.384645 |
| USDC-WETH Ethereum 5 | -3,054,024 | -3.032900 | -3.070001 | -2.826631 | [-3.99, -2.15] | [-3.97, -1.68] | +0.037101 |
| USDC-WETH Ethereum 30 | -101,573 | -0.876000 | -0.909249 | -1.908843 | [-7.63, 5.81] | [-10.23, 6.41] | +0.033249 |
| USDT-WETH Arbitrum 5 | -85,126 | -1.716000 | -1.972888 | -1.918914 | [-2.32, -1.62] | [-2.51, -1.32] | +0.256888 |
| USDT-WETH Ethereum 1 | 2,412 | 0.074800 | -0.084154 | -8.306552 | [-48.2, 48.03] | [-11.77, -4.84] | +0.158954 |
| USDT-WETH Ethereum 5 | -1,322,337 | -1.615100 | -1.756679 | -2.235749 | [-2.29, -1.23] | [-3.21, -1.26] | +0.141579 |
| USDT-WETH Ethereum 30 | -87,112 | -3.020300 | -3.044381 | -7.365738 | [-4.1, -1.98] | [-11.24, -3.49] | +0.024081 |
| USDC-cbBTC Base 5 | -19,013 | -0.912100 | -0.365854 | -1.204660 | [-0.83, 0.1] | [-3.71, 1.3] | -0.546246 |
| USDC-WBTC Arbitrum 5 | -182,076 | -1.287200 | -1.287180 | -1.716737 | [-1.51, -1.06] | [-2.37, -1.06] | -0.000020 |
| USDC-WBTC Ethereum 5 | -187,952 | -0.993700 | -1.278666 | -0.922808 | [-3.99, 1.43] | [-2.58, 0.74] | +0.284966 |
| USDC-WBTC Ethereum 30 | -82,145 | -2.003400 | -2.020871 | -3.119593 | [-6.02, 1.98] | [-17.11, 10.87] | +0.017471 |
| USDT-WBTC Arbitrum 5 | -30,895 | -2.470600 | -2.788936 | -3.304469 | [-3.16, -2.42] | [-4.24, -2.37] | +0.318336 |
| USDT-WBTC Ethereum 5 | -4,452 | -0.186100 | -1.147261 | -6.655240 | [-6.75, 4.46] | [-10.23, -3.08] | +0.961161 |
| USDT-WBTC Ethereum 30 | 15,042 | 0.126500 | 0.016537 | -0.340322 | [-2.38, 2.42] | [-34.75, 34.07] | +0.109963 |

Recomputed: **12 of 16 v4 gaps are positive**; the three near-zero negatives coincide with a printed `0.00` active share in Table 8, and the one material negative is `USDC-cbBTC Base 5` at `-0.546246`, where Table 8 prints an active LIFO share of `84.08%` (passive better than aggregate by a wide margin).

**Table 5 -- LIFO vs exact subtraction on Uniswap v3 (19 pools).**

| Pool | Active LIFO (%) | Active exact (%) | Passive LIFO (bps) | Passive exact (bps) |
|---|---|---|---|---|
| USDC-WETH Base 5 | 3.82 | 3.56 | -0.706874 | -0.707497 |
| USDC-WETH Arbitrum 5 | 0.03 | 0.01 | -0.769710 | -0.769485 |
| USDC-WETH Ethereum 1 | 0.33 | 0.32 | -0.000559 | 0.002104 |
| USDC-WETH Ethereum 5 | 1.36 | 1.30 | -1.506019 | -1.521428 |
| USDC-WETH Ethereum 30 | 0.68 | 0.67 | -0.866415 | -0.863497 |
| USDT-WETH Base 5 | 0.00 | 0.00 | -0.574969 | -0.574969 |
| USDT-WETH Arbitrum 5 | 0.00 | 0.00 | -0.449636 | -0.550026 |
| USDT-WETH Ethereum 1 | 0.44 | 0.42 | -0.138684 | -0.137273 |
| USDT-WETH Ethereum 5 | 1.23 | 1.16 | -1.309165 | -1.300011 |
| USDT-WETH Ethereum 30 | 0.93 | 0.92 | 1.001649 | 1.001035 |
| USDC-cbBTC Base 5 | 0.00 | 0.00 | -0.568331 | -0.568547 |
| USDC-WBTC Arbitrum 5 | 0.00 | 0.00 | -0.589305 | -0.589479 |
| USDC-WBTC Ethereum 1 | 0.06 | 0.03 | -2.962705 | -2.960789 |
| USDC-WBTC Ethereum 5 | 1.90 | 1.78 | -0.408402 | -0.395788 |
| USDC-WBTC Ethereum 30 | 1.54 | 1.51 | 0.209764 | 0.221894 |
| USDT-WBTC Arbitrum 5 | 0.00 | 0.00 | -0.722146 | -0.722148 |
| USDT-WBTC Ethereum 1 | 1.05 | 0.97 | -4.239112 | -4.263411 |
| USDT-WBTC Ethereum 5 | 1.25 | 1.14 | -0.254329 | -0.231116 |
| USDT-WBTC Ethereum 30 | 0.84 | 0.79 | 2.519784 | 2.535369 |

Two rows (USDC-WBTC Ethereum 1 bps, USDT-WBTC Ethereum 1 bps) are **absent from Tables 3 and 7** -- see contradiction 2. Recomputing the gap against Table 3's printed overall column using Table 5's exact-subtraction passive markout instead of LIFO **flips the sign** for `USDT-WETH Arbitrum 5` (from `-0.000029` to `+0.100361`) and for `USDC-WBTC Arbitrum 5` (from `-0.000158` to `+0.000016`), so under exact subtraction **all 17 shared v3 pools have a positive gap** (recomputed from the printed cells), against 15 of 17 under LIFO.

**Tables 6, 7, 8 -- descriptive statistics (5 v2, 17 v3, 16 v4 rows).** Columns: number of trades, number of liquidity events, total volume ($), sandwich volume (%), active LIFO volume (%). Research-computed sums over the printed cells: **38 pools, 66,452,648 trades, 301.92646 B USD of volume** (v2 3,779,141 trades / 2.54554 B; v3 53,646,362 / 266.64141 B; v4 9,027,145 / 32.73951 B). Largest pools by printed volume: Arbitrum v3 USDC-WETH 5 bps `61.13B`, Ethereum v3 USDC-WETH 5 bps `46.84B`, Ethereum v3 USDT-WETH 1 bps `30.24B`, Ethereum v3 USDC-WETH 1 bps `22.21B`, Base v3 USDC-WETH 5 bps `21.68B`. Sandwich volume `>= 50%` in exactly four rows: v3 Ethereum USDC-WETH 1 bps `55.94`, v3 Ethereum USDT-WETH 1 bps `52.60`, v4 Ethereum USDT-WETH 1 bps `76.12`, and (just below) v4 Ethereum USDC-WETH 1 bps `47.65`. Largest printed active shares: v4 Base USDC-cbBTC `84.08`, v4 Arbitrum USDT-WBTC `69.42`, v4 Arbitrum USDT-WETH `41.99`, v3 Base USDC-WETH `3.56` (Table 7 column; see contradiction 1).

**Table 9 -- matching-convention and matching-horizon robustness (15 v3 pools; Ethereum 1 bps omitted; vintage through 2025-12-01).** Values are passive LIFO bps with the 95% CI; the three variants are `LIFO T=20s`, `LIFO T=60s`, `FIFO T=60s`.

| Pool | LIFO T=20s | CI | LIFO T=60s | CI | FIFO T=60s | CI |
|---|---|---|---|---|---|---|
| USDC-WETH Base 5 | -0.709 | [-0.81, -0.61] | -0.740 | [-0.84, -0.64] | -0.740 | [-0.84, -0.64] |
| USDC-WETH Arbitrum 5 | -0.770 | [-6.08, 4.54] | -0.769 | [-6.08, 4.54] | -0.769 | [-6.08, 4.54] |
| USDC-WETH Ethereum 5 | -1.505 | [-2.00, -1.01] | -1.505 | [-2.00, -1.01] | -1.505 | [-2.00, -1.01] |
| USDC-WETH Ethereum 30 | -0.866 | [-2.63, 0.90] | -0.866 | [-2.63, 0.90] | -0.866 | [-2.63, 0.90] |
| USDT-WETH Base 5 | -0.575 | [-1.34, 0.19] | -0.575 | [-1.34, 0.19] | -0.575 | [-1.34, 0.19] |
| USDT-WETH Arbitrum 5 | -0.450 | [-0.86, -0.04] | -0.449 | [-0.86, -0.04] | -0.449 | [-0.86, -0.04] |
| USDT-WETH Ethereum 5 | -1.309 | [-4.42, 1.80] | -1.309 | [-4.42, 1.80] | -1.309 | [-4.42, 1.80] |
| USDT-WETH Ethereum 30 | 1.002 | [-0.71, 2.71] | 1.002 | [-0.71, 2.71] | 1.002 | [-0.71, 2.71] |
| USDC-cbBTC Base 5 | -0.568 | [-0.77, -0.37] | -0.568 | [-0.77, -0.37] | -0.568 | [-0.77, -0.37] |
| WBTC-USDC Arbitrum 5 | -0.589 | [-12.73, 11.55] | -0.589 | [-12.73, 11.55] | -0.589 | [-12.73, 11.55] |
| WBTC-USDC Ethereum 5 | -0.407 | [-5.49, 4.67] | -0.407 | [-5.49, 4.67] | -0.407 | [-5.49, 4.67] |
| WBTC-USDC Ethereum 30 | 0.210 | [-1.40, 1.82] | 0.210 | [-1.40, 1.82] | 0.210 | [-1.40, 1.82] |
| WBTC-USDT Arbitrum 5 | -0.722 | [-0.85, -0.60] | -0.722 | [-0.85, -0.60] | -0.722 | [-0.85, -0.60] |
| WBTC-USDT Ethereum 5 | -0.230 | [-1.75, 1.29] | -0.230 | [-1.75, 1.29] | -0.230 | [-1.75, 1.29] |
| WBTC-USDT Ethereum 30 | 2.520 | [0.51, 4.53] | 2.520 | [0.51, 4.53] | 2.520 | [0.51, 4.53] |

Source's own reading: FIFO and LIFO "agree to four or more decimal places in every pool" (the table prints only three), and widening `T` from 20 s to 60 s "moves the estimate visibly only in the pool with the largest active share (Base USDC-WETH 5 bps, from -0.709 to -0.740 bps)".

**Figure-level claims (captions and Section 5.2 / Appendix F prose; numeric point values are not printed in the text layer).** Figure 1 plots `Overall - Passive LIFO (bps)` against `Active LIFO Volume (%)` for v3 (linear x, 0 to 3.5) and v4 (log x, `10^-5` to `10^2`), with `L1 / L2 / Fitted line` legends. Figure 2 plots passive LIFO bps by fee tier within chain for v2/v3/v4. Figure 3 plots `Overall - Passive LIFO (bps)` by chain with a volume-weighted mean marker and the caption "Positive values indicate that passive LPs underperform the pool aggregate." Figure 4 plots `|passive LIFO - infinitesimal|` against the infinitesimal CI range on log-log axes with a `y=x` reference and the caption "Points below the 45-degree line are pools where the disagreement between the two methods is smaller than the statistical uncertainty of the infinitesimal estimate." Figures 5 and 6 plot the passive-LIFO markout term structure over `0 s .. 6 h` at `T = 20 s` and `T = 60 s` with analytical and day-block-bootstrap bands. Recomputing Figure 4's criterion from the printed Table 3 cells gives **15 of 17 pools below the 45-degree line**, with the two exceptions `USDC-WETH Arbitrum 5` (`|diff| 0.901092` vs CI width `0.550000`) and `USDC-WETH Ethereum 1` (`1.755004` vs `1.530000`) -- consistent with the source's "Almost all pools fall below this line" (research-computed).

**Uncited headline number:** "Uniswap alone has facilitated over $4.4 trillion in cumulative trading volume" is the only occurrence of `4.4 trillion` and carries no citation.

### Independently reproduced

not independently reproduced

The only checks performed this run are checksum, literal-tracing and arithmetic checks on the pinned artefact itself: both pinned file digests recomputed, the API digest recomputed, printed-literal tracing of Tables 1-9, the cross-table identity `total($)/overall(bps) = descriptive volume` over all 39 printed rows, the gap arithmetic over Tables 3 and 4, the LIFO-versus-exact gap recomputation over Table 5, the Figure 4 criterion over Table 3, the Table 7 versus Table 5 column comparison, the sandwich-share threshold check and the term censuses. No on-chain data was downloaded, no Binance quote was fetched, no LP simulation was run, no markout was recomputed from raw events, and no third-party code was executed.

### Negative evidence

1. **The measured quantity is gross of exactly the costs that distinguish active from passive LPs.** Gas, liquidity-management and capital costs are excluded by declaration (Sections 1 and 4.1), and the source itself says the exclusion is "material for the realized profit of active strategies". The active-passive gap is therefore a **pre-cost** gap; whether active repositioning is worth its gas cannot be read off any number in this paper.
2. **No return, risk or capacity metric exists anywhere in the source.** `sharpe` = 0, `cagr` = 0, `drawdown` = 0, `win rate` = 0, `backtest` = 0, `annualized`/`annualised` = 0, `turnover` = 0, `capacity` = 0, `information ratio` = 0, `sortino` = 0, `cvar` = 0, `var` = 0 occurrences. Every number is a bps markout or a dollar total; nothing is stated about LP return per unit of capital, per unit of time, or per unit of gas.
3. **No statistical significance machinery.** `significan*` = 0, `p-value` = 0, `t-stat` = 0, `regression` = 0, `benjamini` = 0, `fdr` = 0, `bonferroni` = 0, `multiple testing` = 0 occurrences; `hypothesis test` occurs exactly **once** and that occurrence is the disclaimer "we read the directional agreement between the two estimators as cross-method evidence rather than a formal hypothesis test". Uncertainty is a normal-approximation interval or a 5,000-replicate day-block bootstrap only, and no per-pool gap is ever tested against zero.
4. **"Systematic" rests on a small, selected, single-window cross-section.** 15 of 17 v3 and 12 of 16 v4 gaps are positive (recomputed), but the sample is one window (`2025-02-01..2025-11-30`, plus a one-day-vintage robustness variant), 38 high-volume pools above a `$10M` floor restricted to five benchmark pairs, with `walk-forward` = 0, `holdout` = 0, `hold-out` = 0, `seed` = 0, `monte carlo` = 0 occurrences and no second period or second market.
5. **Author interest and zero governance disclosure.** Four of five authors carry a Uniswap Labs affiliation, and Uniswap Labs develops the protocol whose pools are measured. There is no competing-interests, funding, acknowledgments, data-availability, code-availability or declaration statement of any kind (`competing` = 0, `interest` = 0, `acknowledg` = 0, `conflict` = 0, `declaration` = 0, `orcid` = 0).
6. **No independent reproduction path.** Data comes from the commercial vendor Allium and the paper states "We do not operate independent nodes on any of the chains"; there is no repository (`repository` = 0, `github` = 0, `code` = 0), no immutable commit, no environment and no seed.
7. **Uncited headline scale figure.** The `$4.4 trillion` cumulative-volume claim has no citation.
8. **Address-level identification is explicitly a lower bound.** The source's own Limitations: "Our LIFO classification operates at the on-chain address level, so multi-address strategies and pooled vaults are misclassified and the LIFO active share is a lower bound on strategic provision."
9. **The passive benchmark is a floor, not the passive LP's actual outcome.** Source's own Limitations: "The infinitesimal benchmark corresponds to a full-range position; finite-width passive LPs face more adverse selection per unit of liquidity, making the estimate a floor on their markout cost." Most real v3/v4 positions are finite-width.
10. **The cross-chain comparison is confounded by construction.** Source's own Limitations and Appendix F: Ethereum, Arbitrum and Base "differ in gas, MEV infrastructure, block times, and LP composition, channels we do not separate", and the paper explicitly offers two opposing mechanisms on L2s (shorter block times narrow the gap, lower gas widens it) without adjudicating.
11. **The fee-tier effect is not separable from chain and protocol version.** Within v3 and v4, the 30 bps tier exists only on Ethereum (Tables 3 and 4 contain no Arbitrum or Base 30 bps row); the 30 bps Arbitrum and Base points visible in Figure 2 come from v2 pools, which by construction have no active LPs at all. "High-fee pools are generally better for passive LPs" therefore mixes a fee effect with a chain effect and a version effect.
12. **The single pool with the largest measured active share has essentially no gap.** `Base USDC-WETH 5 bps` carries `3.56%` (exact) / `3.82%` (LIFO) active share, the highest in v3, yet its recomputed gap is only `+0.025698` bps, while pools with roughly a third of that active share show gaps of `+0.35` to `+0.45` bps (research-computed from printed cells). The "gap grows with active participation" reading of Figure 1 is not supported by that point.
13. **Implied active-LP markouts are extreme and never printed.** From the identity `overall = (1-a)*passive + a*active` applied to Tables 4 and 8 (research-computed, with the active share rounded to two decimals in the source), v4 `USDT-WETH Ethereum 1 bps` implies an active markout in roughly `[1060, 3179]` bps and v4 `USDT-WBTC Ethereum 5 bps` roughly `[915, 1012]` bps, against printed fee tiers of 1 bps and 5 bps. The source reports no active-side markout table for v4 and never reconciles these magnitudes.
14. **Sandwich contamination is admitted and only partly handled.** Four Ethereum 1 bps rows carry sandwich volume shares of `47.65` to `76.12%`; the infinitesimal estimator drops sandwiches but the LIFO estimator does not, and the Ethereum 1 bps pools are excluded from the figures while remaining in Table 3.
15. **Method choice can flip the sign of the headline quantity.** Recomputing the gap against Table 5's exact-subtraction passive markout flips `USDT-WETH Arbitrum 5` from `-0.000029` to `+0.100361` and `USDC-WBTC Arbitrum 5` from `-0.000158` to `+0.000016` (research-computed); and the largest LIFO-versus-exact difference, `0.100390` bps on `USDT-WETH Arbitrum 5`, is 55% of the median v3 gap of `0.183949` bps (research-computed). The Section 4.2 claim that the exact method produces estimates "very close to the LIFO estimates throughout our sample" is therefore not uniformly negligible relative to the effect being measured.
16. **The two estimators disagree materially on some pools.** `|passive LIFO - infinitesimal|` exceeds the infinitesimal CI width in 2 of 17 v3 pools (research-computed), and the level disagreement can be very large: v4 `USDT-WETH Ethereum 1 bps` reports passive LIFO `-0.084154` against infinitesimal `-8.306552`.
17. **The robustness table's own precision claim is uncheckable.** Appendix G asserts FIFO and LIFO "agree to four or more decimal places in every pool", but Table 9 prints three decimals, so the claim cannot be verified from the printed artefact.
18. **Five source-internal contradictions** are recorded in the frontmatter: the Table 7 column label, the Table 5 pool-set mismatch, the single cross-table identity failure, the "5 bps tier" claim against the excluded 1 bps rows, and the `USDC-WBTC` versus `WBTC-USDC` label flip.
19. **No evidence either way for anything outside the window or above the `$10M` floor.** Absence of a negative result is not evidence of no negative result; the long tail of small pools, any period after `2025-11-30`, any non-Uniswap AMM and any order-book venue are entirely untested.

## Falsification plan

Two hypotheses are tested separately. Every threshold, grid, metric and action below is **`research-defined falsification threshold` / `research-proposed`** -- none of it is in the source. **No-retuning rule:** once a gate is run, the 38-pool set, `T = 20 s`, `h = 15 s`, the `20%` price-move filter, the sandwich filter, the `$10M` floor, the benchmark-asset set, the fee-tier set and every threshold in this section are frozen; a failed gate may not be re-run with a loosened cut, and any change requires a new record version. Gates **F3, F4, F5 and F14 are marked `currently failing` on the pinned artefact and are terminal for any reproducibility claim.**

**H1 -- aggregate pool markout overstates the passive LP's markout.**

- **F1 (`research-defined`, printed-value reproduction).** Every source-reported number quoted in this record must appear verbatim in the pinned 1,966,973-byte PDF text layer. *Action on failure:* delete the number; if a headline claim loses its anchor, set `confidence: low`.
- **F2 (`research-defined`, provenance integrity).** arXiv `2609.37963` must still resolve to a single version `v1` with the pinned digests. *Action on failure:* re-pin the new version, re-read end to end, and re-run F1.
- **F3 (`research-defined`, cross-table identity -- **currently failing in 1 of 39 rows**).** For every printed pool, `total($) / (overall bps / 10000)` must equal the descriptive total volume within `1%` **`research-defined`**. Printed data: 38 of 39 pass (max relative error `0.00320`), `v2 USDC-WETH Base 30 bps` fails at `0.838`. *Action on failure:* no dollar or bps figure from the failing row may be cited; if a second row fails, set `confidence: low`.
- **F4 (`research-defined`, label integrity -- **currently failing in 12 of 17 rows**).** For every pool, the column Table 7 labels `active LIFO volume (%)` must equal Table 5's `active LIFO` value within `0.005` percentage points **`research-defined`**. Printed data: all 17 rows instead equal Table 5's `active exact` column, and 12 rows differ from the LIFO column. *Action on failure:* every `active LIFO` figure in this record is treated as ambiguous between the two conventions, and no statement about active-share magnitude may be made without naming the convention.
- **F5 (`research-defined`, pool-set completeness -- **currently failing**).** Tables 3, 5 and 7 must report the identical v3 pool set. Printed data: 17 / 19 / 17. *Action on failure:* the two extra Ethereum 1 bps WBTC rows are excluded from all headline statements and marked as appendix-only.
- **F6 (`research-defined`, gap-sign gate -- the core test of H1).** Recompute `overall - passive` on the source's own 38 pools under both matching conventions. **H1 is supported** if the share of pools with a positive gap is `>= 0.70` under LIFO **and** `>= 0.90` under exact subtraction **and** the volume-weighted mean gap on Ethereum exceeds that on Arbitrum and Base. **H1 is falsified** if the positive share is `<= 0.50` under either convention, or if the L2 mean gap is as large as the Ethereum mean gap. *Printed-data reading:* LIFO `15/17 = 0.882` for v3 and `12/16 = 0.750` for v4; exact `17/17 = 1.000` for the shared set -- the gate passes on printed data but the Ethereum-versus-L2 mean comparison is **not printed** and must be computed. *Action on failure:* drop the word "systematic" from every downstream description of this record.
- **F7 (`research-defined`, active-share monotonicity gate).** Regress the per-pool gap on `log(1 + active share)` with chain fixed effects, and compute Spearman `rho` between active share and gap, over the v3 and v4 pools separately. **H1's mechanism reading is falsified** if `rho <= 0.30` in either version or if the slope is non-positive. *Known stress point:* `Base USDC-WETH 5 bps` has the largest active share and a gap of only `+0.025698`. *Action on failure:* restate the mechanism as chain-driven (H2) and abandon any active-share-based screening rule.
- **F8 (`research-defined`, estimator-agreement gate).** `|passive LIFO - infinitesimal| < infinitesimal CI width` must hold for at least `15 of 17` v3 pools **`research-defined`**. *Printed-data reading:* exactly 15 of 17 (research-computed). *Action on failure:* treat the two estimators as disagreeing and withdraw the cross-method robustness claim; the monitor must then name which estimator it uses.
- **F9 (`research-defined`, matching-convention invariance gate).** Under the source's own three Table 9 variants, the change from `T = 20 s` to `T = 60 s` and from LIFO to FIFO must stay inside the reported 95% CI half-width for every pool. *Printed-data reading:* only `Base USDC-WETH 5 bps` moves visibly (`-0.709` to `-0.740`), still inside `[-0.84, -0.64]`. *Action on failure:* the identification convention is material, and every gap must be re-derived under both conventions before any use.
- **F10 (`research-defined`, horizon-stability gate).** Passive markout at `0 s, 15 s, 1 m, 5 m, 1 h` must agree within the source's day-block bootstrap band; the source asserts the term structure "is flat from 0 seconds out to roughly one hour". *Action on failure:* markout-based pool selection becomes horizon-dependent and the Appendix I monitor is not usable as specified.

**H2 -- the gap is governed by execution environment (chain structure).**

- **F11 (`research-defined`, chain-ordering gate).** On a frozen re-estimate over the same 38 pools, the volume-weighted mean gap must satisfy `Ethereum > Arbitrum` and `Ethereum > Base`. **H2 is falsified** if either inequality reverses in two consecutive months **`research-proposed`, monitoring cadence monthly`**. *Action on failure:* record the chain result as a single-window artefact and remove every block-time interpretation.
- **F12 (`research-defined`, out-of-window replication gate).** Freeze `T = 20 s`, `h = 15 s`, the `20%` filter, the sandwich filter, the `$10M` floor, the benchmark assets and the fee-tier set, and re-estimate on `2025-12-01` onward **`research-proposed`** on the same 38 pools. **Falsified** if the Ethereum-versus-L2 ordering reverses or if the positive-gap share falls below `0.50`. *Action on failure:* H1 and H2 are both marked `single-window`.
- **F13 (`research-defined`, fee-tier confound gate).** Re-estimate the fee-tier comparison **within chain and within protocol version only**, i.e. only on the four Ethereum v3 pairs that have both 5 bps and 30 bps rows, and additionally require at least one non-Ethereum chain to contain both tiers. **The fee-tier claim is falsified** if the Ethereum within-version contrast loses its sign, or if the cross-chain requirement cannot be met. *Action on failure:* the fee-tier statement is downgraded to "Ethereum v3 only" in every downstream document.

**Economic and evidence gates (all cost inputs `research-proposed`).**

- **F14 (`research-defined`, code/data gate -- **currently failing**).** A public artefact (repository plus immutable commit, or a reproducible Allium extract plus the Binance quote set) must become available before any number here is treated as reproducible. Printed data: `repository` = 0, `github` = 0, `code` = 0, `data availability` = 0. *Action on failure:* the record stays `research-only` permanently and no number may be described as reproduced.
- **F15 (`research-defined`, cost-inclusion ladder -- `research-proposed`).** Re-rank pools after adding gas and liquidity-management cost at `0 / 1 / 5 / 20 USD per liquidity event` **`research-proposed`**, applied to active events only, plus a capital-cost ladder of `0 / 2 / 5 / 10 % annualized` **`research-proposed`**. **The selection rule is not cost-robust** if the pool ranking changes at three or more ladder points for any chain, or if the sign of the active-minus-passive rent turns negative before the second ladder point. *Action on failure:* no net-of-cost claim may be inherited from this record and the Appendix I rent statement must be labelled gross-of-gas.
- **F16 (`research-defined`, multiplicity gate).** Apply Benjamini-Hochberg at `q < 0.10` **`research-proposed`** across the family of per-pool `D +/- 1.96 SE(D)` tests implied by Appendix C over all 38 pools. *Action on failure:* drop every per-pool significance statement and keep only the volume-weighted aggregate.
- **F17 (`research-defined`, contamination gate).** Re-run the gap with every pool whose sandwich volume share exceeds `10%` **`research-proposed`** removed, and separately with the Ethereum 1 bps pools excluded entirely (the source excludes them only from figures). *Action on failure:* if the headline gap moves by more than `30%` **`research-defined`** of its printed value, mark the result as sandwich-driven.

**Boundary gate.** No adoption, sizing or venue-diversification statement may be added to this record until F14 passes and F15 shows a net-of-gas rent; until then the record remains a measurement hypothesis about passive markout, not a tradable liquidity-provision strategy.

## Crypto portability

`direct`

The source is entirely crypto-native: it measures Uniswap v2, v3 and v4 pools on Ethereum Mainnet, Arbitrum and Base, uses Binance USDT spot top-of-book as the external numeraire, and quotes `ethereum` 105 times, `binance` 4, `usdt` 41 and `crypto` 2 (one of the two inside the word "Cryptology"); `bitcoin` = 0 and `perpetual` = 0. Nothing needs to be ported from a traditional-asset setting -- the mechanism, the venue, the data and the decision rule are all already on-chain.

What is *not* covered, and must be re-derived before any use:

- **Venue generality:** only Uniswap pools on three chains. No Curve, no Balancer, no non-EVM AMM, no CEX order book. Porting to a limit-order-book liquidity provision setting is `unproven`, not `direct`.
- **Perpetual / futures LP:** `perpetual` = 0; there is no funding-rate, mark-index or liquidation analogue in this record, so applying the passive-markout monitor to a CEX perpetual market-making book is `unproven`.
- **Cost structure:** gas is excluded by the source, but gas *is* the cost that makes L2 repositioning cheap and Ethereum repositioning expensive -- the very channel H2 invokes. Any crypto deployment must reintroduce gas, MEV/sandwich exposure and rebalance cadence explicitly (F15).
- **Custody and venue risk:** not addressed; no withdrawal, bridge or sequencing-risk treatment appears in the pinned text.
- **24/7 session structure and candle boundaries:** the source works in elapsed seconds from block timestamps rather than session boundaries, so session conventions are largely irrelevant here -- but the absence of a stated timezone/clock policy is still a `data gap`.
- **Stablecoin and numeraire risk:** the benchmark is USDT-denominated on Binance; USDT de-peg or venue-specific basis would move every markout simultaneously. Not addressed in the source.

## Limitations

- `underspecified`: monitor window (`day` vs `week`), the meaning of "recent", the choice between the analytical and bootstrap confidence band for the exit rule, ranking tie-breaks, TVL source/date/definition, position sizing, rebalance cadence, fee-tier switching, reorg handling, timestamp timezone and clock policy, missing-data policy, and the composition of swaps dropped for having no admissible quote.
- `data gap`: every numeric value behind Figures 1-6 (the text layer carries axis ticks and legends only, so the fitted lines, the volume-weighted chain means in Figure 3 and the full horizon term structures in Figures 5-6 are not recoverable from the pinned artefact); the Allium extract; the Binance quote set; the active-side markout table for v4 (no exact-subtraction analogue of Table 5 is printed for v2 or v4); the reason two v3 pools appear only in Table 5; which of the three cells in the v2 Base row is wrong.
- `not independently reproduced`: every markout, gap, share and confidence interval.
- `unproven`: any profitability statement, any capacity statement, any statement about pools below the `$10M` floor, any period after `2025-11-30`, and any non-Uniswap venue.
- **Single-artefact dependence.** Everything here is read from one preprint PDF plus its abstract page and API record; the arXiv HTML rendering (`https://arxiv.org/html/2609.37963v1`) exists but was not fetched this run, so all cross-surface checks are PDF-versus-landing-page only.
- **Text-layer artefacts.** pypdf merges some adjacent words (for example `Apositive markoutmeans`, `profit ofactive strategies`, `T able 3`, `WBTC-USDC` line breaks); quoted sentences in this record are de-merged for readability and no merged token was silently reinterpreted. Figure legends are read from the text layer, so a missing legend entry (the v4 panel of Figure 1 lists four pairs while Table 4 contains a fifth, `USDC-cbBTC`, which Section 5.2 explicitly names as an outlier in that figure) may be a genuine legend omission **or** an extraction gap -- `data gap`, deliberately not recorded as a contradiction.
- **Interpretive layers.** The `Gap` columns in the Tables 3-4 blocks, the cross-table identity check, the Figure 4 criterion, the LIFO-versus-exact sign flips, the implied active markouts, the trade/volume sums and the median gap are all **research-computed arithmetic on printed cells**, not source-printed quantities; each is labelled where used.
- **Publication bias / source quality:** preprint only, no journal reference, no publisher DOI, no peer-review statement (`peer` = 0), four of five authors affiliated with the protocol's developer, and no competing-interests, funding, data or code disclosure of any kind.
- **The paper is measurement, not a strategy.** Its own Limitations section calls the cross-chain result descriptive and declines a formal hypothesis test; using any number here as a tradable rule requires the research-proposed steps in F15 and the F14 data gate.
- **Incremental-write check:** this capture adds a new family (LP-side active/passive markout decomposition and passive-markout pool selection) that no existing record in this repository covers; the nearest neighbours differ in source identity and in mechanism, signal construction and material data dependency, and are distinguished in `Related Wiki records`.

## Implementation status

`implementation_status: not-implemented`

Nothing has been implemented in our research stack. No on-chain event was downloaded, no Binance quote was fetched, no markout was recomputed, no LP position was simulated, no pool monitor was built, no market data was downloaded, no dependency was installed, and no third-party code was executed. The checks performed this run are limited to file digests, printed-literal tracing and arithmetic identities on the pinned artefact. This record does **not** imply Qlib full-backtest validation, Paper, Testnet or Live verification of anything.

## Adoption boundary

`status: research-only` | `adoption: not-approved` | `approval_scope: research-only`

The presence of this record in the staging repository means only that normalized research material was pushed. It does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading.

## Related Wiki records

Three read-only `kb_search` queries were run against Hermes Wiki Brain this run (`Uniswap liquidity provision markout active passive` -> 0 pages; `concentrated liquidity AMM adverse selection LVR` -> 8 pages; `liquidity provider profitability pool selection monitoring` -> 0 pages). No Wiki page was written this run. From the 8-page result, two verified existing pages are linked with an explicit mechanism distinction:

- `[[quant/crypto-clmm-path-dependent-liquidity-provision-win-score-early-exit-2026-09-02]]` -- also about concentrated-liquidity LP outcomes, but its unit of analysis is the **individual position** (a win-score area metric and an early barrier exit over a 15-position taxonomy), whereas this record's unit of analysis is the **swap-level markout decomposed between active and passive liquidity**; different source, different signal construction, different decision (exit timing within a position vs which pool to be in at all).
- `[[quant/defi-amm-jump-diffusion-lvr-decomposition-optimal-block-time-2026-09-01]]` -- also decomposes LVR, but as a **theoretical jump-diffusion model** that derives an optimal block time, whereas this record is an **empirical LP-side decomposition across observed pools and chains**; different source, different mechanism (modelled rebalancing loss vs measured adverse-selection rent), different data dependency (price process assumptions vs Mint/Burn/Swap event logs plus CEX quotes).

Repository-adjacent records distinguished here (five axes each -- source identity, mechanism, signal construction, universe/stage, material data dependency -- differ in every pair):

1. `ml-optimized-tau-reset-clmm-liquidity-provision-2026-09-06.md` (arXiv:2505.15338, Urusov et al.) -- **closest neighbour.** Different source; that record captures a *rebalancing-policy optimization* (when to reset the range) while this record captures a *measurement decomposition* of who earns what inside a pool; different signal construction (policy objective vs markout attribution), different universe (its own CLMM simulation/backtest vs 38 observed Uniswap pools on three chains), different data dependency.
2. `crypto-clmm-path-dependent-liquidity-provision-win-score-early-exit-2026-09-02.md` (arXiv:2604.22069) -- different source, position-level win-score and barrier exit rather than swap-level markout attribution; different decision object.
3. `defi-concentrated-liquidity-amm-dynamic-fee-staleness-proxy-lvr-compensation-2026-09-02.md` (arXiv:2606.23070) -- different source and a **protocol-level intervention** (fee schedule design in an agent-based model) rather than an LP-level allocation rule; different stage entirely.
4. `fmz-robinhood-chain-v3v4-active-pool-lp-fee-cost-coverage-549380-2026-09-19.md` (FMZ strategy page 549380) -- different source, a **fee-income-versus-gas-cost coverage screen** on Robinhood Chain rather than a markout decomposition; different universe, different signal construction, different cost treatment.
5. `vol-conditional-liquidity-provision-reversal-micro-price-execution-overlay-2026-09-23.md` (Bryan Vine, GitHub `d94009a6...`) -- different source (it merely cites Moallemi), a CEX micro-price execution overlay rather than on-chain LP attribution; different venue class and different market stage.
6. `crypto-perpetual-touch-quoting-entry-markout-adverse-selection-ssrn-7461901-2026-09-28.md` -- shares only the word `markout`: different source, different side of the book (taker touch-quoting on a CEX perpetual), different market type, different horizon and different data dependency.
7. `defi-cpmm-oracle-liquidation-dynamics-fee-oev-protection-2026-09-10.md` (Sadeghi & Feinstein, arXiv:2602.12104) and `oracle-parametrized-cfmm-ga-lvr-depth-pareto-spy-nbbo-arxiv-2609.33799-2026-09-30.md` (Amini & Feinstein, arXiv:2609.33799) -- share only an author (Sadeghi, respectively Moallemi/Feinstein adjacency); different sources, different mechanisms (liquidation dynamics; oracle-parameterized pricing rules) and different universes (one on CPMM liquidations, one on one-second SPY NBBO).

## Sources

- Agathe Sadeghi, Dingyue Liu, Ciamac Moallemi, Xin Wan and Brian Zhu, *Not All LPs Are Equal: The Active-Passive Gap in Automated Market Maker Liquidity Provision*, arXiv:2609.37963v1 `[q-fin.TR]`, submitted 29 Sep 2026 16:34:10 UTC -- abstract page `https://arxiv.org/abs/2609.37963` (44,106 bytes, SHA-256 `3b350a9b993cde0c945936ee82876a5001e9de6cf8f6d0abf18dad750856f61f`) and PDF `https://arxiv.org/pdf/2609.37963` (1,966,973 bytes, SHA-256 `8041263ff3dd8312ddeaef317a284b76bc902bbc15e50476f92e7e3294683d66`), both fetched 2026-09-30.
- arXiv API record `https://export.arxiv.org/api/query?id_list=2609.37963` (3,422 bytes, SHA-256 `b329bf354a017f852fd7f51d20d084a59f26b79449c37aa31a7fc746f0f6d2b7`), giving `published` and `updated` both `2026-09-29T16:34:10Z`, single subject `q-fin.TR`, no comment, no journal reference, no DOI.
- Licence cell as printed: `http://creativecommons.org/licenses/by/4.0/` (preserved literally from the source; CC BY 4.0; one of only two non-HTTPS strings in this record, the other being the landing-page linkifier artefact quoted under Provenance).
- Named third-party data inputs **read about but not fetched this run**: Uniswap event logs from Allium; Binance spot order-book data. Their exact contents and access paths are `data gap`.
- Works cited *inside* the source (attributed to its own 17-item reference list, **not independently read** this run): Glosten & Milgrom (1985); Kyle (1985); Adams et al. (2021) Uniswap v3 core; Angeris & Chitra (2020); Fan et al. (2023) strategic liquidity provision in Uniswap v3; Wan & Adams (2022) SSRN 4382303; Xiong, Wang, Knottenbelt & Huth (2023) ePrint 2023/973; Capponi, Jia & Zhu (2024) SSRN 4648055; Trotti et al. (2025) AFT 2025; Milionis, Moallemi, Roughgarden & Zhang (2022) arXiv:2208.06046 (LVR); Milionis, Wan & Adams (2023) arXiv:2306.09421 (FLAIR); Heimbach, Schertenleib & Wattenhofer (2022) AFT; Lehar & Parlour (2025) *Journal of Finance* 80; Hasbrouck, Rivera & Saleh (2025) *Management Science*; Fritsch & Canidio (2024) arXiv:2404.05803; Qin, Zhou & Gervais (2022) IEEE S&P; Zhu, Liu, Wan, Liao, Moallemi & Bachu (2024) arXiv:2410.19107.
