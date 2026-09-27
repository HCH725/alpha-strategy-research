---
schema: strategy-research-record-v1
title: "Backtest-to-Live Gap Anatomy of an LLM-Emitted Directional Signal on Binance Perpetual Futures (SSRN 7353678)"
created: 2026-09-27
updated: 2026-09-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - negative-result
  - crypto
  - perpetual-futures
  - backtest-overfitting
  - live-vs-backtest
  - llm-signal
  - execution-adverse-selection
  - permutation-test
status: research-only
confidence: medium
source_as_of: 2026-08-27
sources:
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7353678"
  - "https://doi.org/10.2139/ssrn.7353678"
  - "https://papers.ssrn.com/sol3/Delivery.cfm/7353678.pdf?abstractid=7353678&mirid=1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Backtest-to-Live Gap Anatomy of an LLM-Emitted Directional Signal on Binance Perpetual Futures (SSRN 7353678)

## Provenance

- **Primary source:** SSRN preprint, `abstract_id=7353678`, DOI [`10.2139/ssrn.7353678`](https://doi.org/10.2139/ssrn.7353678). Landing page: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7353678>.
- **Exact titles.** Landing-page title: `A Real Edge that Loses: Anatomy of a Backtest-to-Live Gap in Cryptocurrency Perpetual Futures`. PDF title block: `A Real Edge That Loses: Anatomy of a Backtest-to-Live Gap in Cryptocurrency Perpetual Futures`, subtitle `How a directional signal that passes a permutation test still lost money in deployment`.
- **Author (name recorded exactly as each surface prints it; the two surfaces disagree).** SSRN author line: **Alexandr Dashyan**, affiliation `Independent Researcher`. PDF title block: **Aleksandr Dashyan**, `Independent Researcher, Yerevan, Armenia`, correspondence address printed on p.1. The `Alexandr` / `Aleksandr` spelling difference is a source-level discrepancy and is not reconciled here.
- **Dates (both printed; not reconciled).** SSRN landing page: `Posted: 27 Aug 2026`, `Date Written: July 10, 2026`. PDF cover (p.1): `Working paper. Preliminary. Comments welcome. This version: August 2026.` The audit that produced the paper's numbers is dated `2026-07-18` (PDF, Data and Code Availability, p.23).
- **Publication / peer-review status.** PDF cover states `Working paper. Preliminary.`; the SSRN landing page for this item shows no journal or issue assignment and prints no peer-review statement, so peer-review status is `not stated in source`.
- **Reference metadata discrepancy.** The SSRN landing page prints `0 References` / `0 Citations`; the PDF itself carries a 16-item reference list (pp.24–25). Recorded as a source-metadata discrepancy, not repaired.
- **License tension (not reconciled).** The SSRN landing page displays a Creative Commons `Attribution-NonCommercial-NoDerivatives 4.0` badge, while the PDF cover states `Copyright 2026 Aleksandr Dashyan. All rights reserved ... may not be reproduced, distributed, quoted at length, or used, in whole or in part, without the author's prior written permission.` Because the two statements conflict, this record only normalises the source's own claims, printed values and section references and does not reproduce the source's prose at length.
- **Landing-page statistics at read time (2026-09-27):** 33 downloads, 110 abstract views, 0 citations.
- **Pinned primary source.** PDF obtained 2026-09-27 through the SSRN `Open PDF in Browser` delivery link (a `download.ssrn.com` presigned object), **626,354 bytes, 25 pages**, SHA-256 `3a7f96498714a3e2a3e6b8e73155940de0b0d207de58b305a1b26cc7dd40409c`. Text was extracted page by page (`pypdf`); all 25 pages carry a text layer and every page of the pinned file was read in full before this record was written.
- **Methods-level read.** Fields for transaction cost, slippage, spread, funding, leverage, fill model and capacity were taken from the PDF's `3. The Setting` (pp.5–6), `4. The Two Numbers` (pp.6–7), `6.2 Frictions the simulation never paid` (pp.14–15), `9. A Checklist` (pp.20–21) and `10. Discussion and Limitations` (pp.21–22), not from the abstract or the landing page.
- **Code / data.** `Data and Code Availability` (p.23): scripts, audit report, live and replay records and figure code are `available from the author on reasonable request`, with `a companion code repository in preparation`. **No public repository, commit or file path exists at read time**, so immutable-commit provenance is `data gap`.
- **Companion papers.** The source cites Dashyan (2026a, 2026b, 2026c) as `Working paper` items (References [5]–[7], p.24) with no DOI, SSRN id or URL printed; their identity is `not stated in source`.
- **AI/tooling disclosure (source-reported, p.23).** Research questions, design, hypotheses, methodology and interpretation are declared the author's own; all software (account simulator, readiness gate and ledger, permutation and reconstruction tests, bracket resolver and cost models, multi-agent audit harness, scripts, figures) was written in Python `with the assistance of Claude`, used as a coding assistant and multi-agent audit tool, explicitly `not an author`.
- **Pre-write source-identity dedup (whole repository, hidden-inclusive, executed 2026-09-27).** `rg` over the repository including `.mimo-worktrees/`, `.agents/`, `.hermes/` for `7353678`, `10.2139/ssrn.7353678`, `Real Edge that Loses`, `Dashyan`, `backtest-to-live gap` returned three files, all matching only the generic phrase `Backtest-to-live gap` inside `alphacrafter-harness-multi-agent-cross-sectional-equity-alpha-2026-09-03.md` (line 158) and its two worktree copies — **zero DOI, zero title, zero author matches**. `coverage_manifest.csv` (1,088,787 bytes) returned zero matches for `7353678|Dashyan|Real Edge`. `git log --oneline -20` was read only as a convenience glance and was not used to complete dedup.

## Economic mechanism

### Source-reported

The source's thesis is that a backtest return is a stack of optimistic assumptions rather than one number, and it decomposes a single deployed program that reported about 170% in backtest while the live account trading the same rulebook over the same calendar lost 21.6% (Abstract, p.1; §1, pp.2–3; Figure 1, p.4). Its mechanism claims are:

1. **The direction map is genuinely informative.** A Monte Carlo permutation test that holds fire times, coins, capital sequencing and one-minute tapes fixed, re-grades the readiness gate causally, re-applies the chase filter, and randomises only each fire's side, never reproduces the observed result (2,000 runs; §5, pp.7–9, Table 2).
2. **The magnitude is manufactured by selection, annualisation and a small effective sample** — an argmax over 100+ configurations on one window, a Sharpe computed on traded days only, one ISO week supplying most of the win-rate margin, and mean trade uniqueness of 0.213 implying roughly 40 independent bets rather than 190 (§6.1, pp.10–13, Figures 4–7, Table 1).
3. **The account then pays frictions the simulation never charged** — funding on a book that is about two thirds short, drawdown measured on closed equity while peak notional approaches 600% of equity, and price-improved limit entries that are anti-correlated with their own alpha (§6.2, pp.14–15).
4. **The risk-control mechanism was inert.** The readiness gate graduates cells at the rate a fair coin would, and the trades it removes are of the same quality as the trades it keeps; its ledger was contaminated by foreign-strategy rows (§6.3, pp.15–17, Figure 8).
5. **The traded signal lives inside the model that emitted it.** A deterministic reconstruction of the same inputs collapses to a coin flip, so the edge is real but not reproducible outside the language model (§6.4, pp.17–18, Figure 9).

Stated economic channels named by the source: limits-to-arbitrage-style selection inflation (Bailey/Borwein/Lopez de Prado/Zhu; Harvey/Liu/Zhu), implementation shortfall (Perold), crypto-specific frictions and segmentation (Makarov–Schoar), Sharpe-ratio annualisation error (Lo), and perpetual-specific funding and auto-deleveraging exposure that equity backtests do not contain (§2, pp.4–5).

### Research interpretation

- **Hypothesis H1 (falsifiable):** an hourly, multi-source, LLM-voted long/short signature over ~20 Binance USD-margined perpetuals carries a small positive directional edge that survives side randomisation but is dominated in magnitude by configuration selection on a single short window.
- **Hypothesis H2 (falsifiable):** under a price-improved limit entry, fill censoring is adversely selected — winners are missed and losers are taken — so realised entry fills are systematically worse than the clean-open fills a bracket resolver assumes.
- **Hypothesis H3 (falsifiable):** a graduation gate of the form `>=5 resolved trades and last-10 win rate >=56%` has near-zero information content and functions as an exposure dial rather than a quality filter.
- **Hypothesis H4 (falsifiable):** a side signal emitted by a language model and consumed through recorded votes is not reproducible by a deterministic rule over the same inputs, so the reported edge is a property of one model at one point in time.
- Competing explanation the source itself keeps alive: the whole result could still be selection-plus-luck whose permutation test is only a weak bar (a blind short on the same fires already makes +14.6%; §5, p.9). A correlation of the observed return with a favourable window is **not** treated here as proof of any mechanism.

## Signal

Normalised from PDF §3 (pp.5–6), §4 (pp.6–7), §6.3 (pp.15–17). Third-party construction, reported as source-reported; anything I supply is labelled.

- **Formation timestamp:** once per hour, a language model policy reads a large multi-source snapshot of each coin and emits per-lane votes; the votes are reduced to a compact signature; the signature plus a coarse market-regime label selects a side (long/short) for any coin whose cell has graduated the readiness gate. Timezone, calendar and snapshot cut-off are `not stated in source` (data gap).
- **Universe:** twenty `Binance USD margined perpetual contracts`. The 20 symbols, the inclusion rule and the as-of date are `not stated in source` (data gap).
- **Lookback / warm-up:** not printed as explicit windows; warm-up rows are excluded from the walk-forward (§8, p.19). Exact lookbacks are `underspecified`.
- **Readiness gate (source-reported):** a cell = coin × side × regime may trade only after at least **5 resolved trades** and a **win rate over the last 10 of at least 56%**. The parameter `K` is the number of trades required (§6.3, p.15).
- **Entry:** `price improved limit order` (§6.2, p.14). Order type, price offset, time-in-force, partial-fill and rejection handling are `underspecified`.
- **Exit:** independent first-touch resolution against fixed brackets on **one-minute prices**; when both barriers fall inside one minute **the stop is taken first**; gaps are priced at the gapped open. Deployed geometry: **take profit +2.1%, stop -1.9%**, which breaks even at a **50.25%** realised win rate on fees alone (§3, pp.5–6).
- **Overlays:** a `chase filter` (intended to block chasing a hot tape; it `fails open at exactly the moments the tape is hot`) and a per-fire `carry veto` (left at its original side value in the permutation harness rather than recomputed; §5, p.8; §6.2, p.15). Both are `underspecified` — no numeric trigger is printed.
- **Holding period:** determined by bracket first-touch; up to **six funding settlements per trade** are implied for held positions (§6.2, p.14). Maximum holding time is `not stated in source`.
- **Position sizing (source-reported):** 15% margin and 8× leverage = **120% of equity in notional per position**, under a **95% capital cap**, at most **one open position per coin**, up to **five concurrent same-side positions** (peak notional near **600% of equity**), about **6% of the full Kelly fraction**, roughly **28 consecutive losses** needed to halve the account (§3, p.6; §6.2, p.14).
- **Baseline comparisons named by the source:** blind short on the same fires **+14.6%**; random-side null mean **+21.9%**; naive baseline later adopted by the program = simply holding the lowest-volatility coin, a test the deployed card predates and was never put to (§5, p.9).
- **Reproducibility status of the rule:** `underspecified`. The side of each trade comes from LLM-emitted per-lane votes, not a written formula; a deterministic reconstruction over 34,000 scan-and-coin rows agreed with the model's own signature on **0.2%** of cases, produced **87** distinct signatures against the model's **1,654**, and found no content at all in the crowd and news lanes (§6.4, p.17).

## Required data

- **Instrument / market type:** Binance USD-margined perpetual futures (linear USDT-margined perps); funding settlements on held positions (up to six per trade).
- **Universe:** 20 unnamed perpetual contracts; symbol list, point-in-time membership and survivorship handling `data gap`.
- **Venue:** single venue (Binance); no cross-venue data; no alternate vendor robustness in this paper.
- **Timeframe:** hourly signal cadence; one-minute price resolution for bracket fills; six-week card window (2026-06-01 to 07-13, 43 calendar days of which about 28 carried trades) and live window from 2026-06-18 (§3, p.6).
- **Fields:** multi-source snapshot per coin (features `not stated in source`), per-lane votes, compact signature, coarse regime label, one-minute OHLC for resolution, fee schedule, funding settlements, margin/liquidation state.
- **Point-in-time:** the source states the walk-forward was genuinely causal, graduation decisions used only information available strictly before the day they applied, warm-up rows were excluded, and an independent leak audit held (§8, p.19). The deeper question the source says remains open is whether the recorded model votes contain information unavailable at decision time (§10, p.22) — flagged `data gap`.
- **Timestamp / timezone:** `not stated in source` (data gap).
- **Missing data / fills:** simulation fills every fire at a clean open price and resolves it on an undisturbed tape (§6.2, p.14); no imputation rule is printed.
- **Costs:** flat **0.11% round-trip fee on notional** modelled (§3, p.6). **Funding explicitly not modelled** (§6.2, p.14). Spread, slippage, market impact and borrow: no modelled line is printed anywhere in the pinned PDF, so their treatment is `not stated in source` / `data gap`, and the only stated fill assumption is the clean open price.

## Execution assumptions

Source-reported unless labelled otherwise.

- **Signal-to-order:** hourly decision cycle; entry via a price-improved limit order; protection on a fresh fill arrives after a measured window of about **3.4 minutes** rather than instantly (§6.2, p.15).
- **Fill model in the backtest:** every fire fills at a clean open price on an undisturbed one-minute tape; gaps priced at the gapped open; stop takes precedence when both barriers fall in the same minute (§3, p.6; §6.2, p.14).
- **Fill model in the account (reconstructed):** of the **11 live entries** reconstructed from the tape, the price-improved limit is anti-correlated with its own alpha — winners missed, losers filled — while trades that reach full size are chased at market; summarised by the audit as `good trades small, bad trades full` (§6.2, pp.14–15). The source explicitly cautions this channel is reconstructed from a small set of live entries and is **not** measured as a return, and that a later deployment using a different order type showed no gap between intended and realised entry prices on the trades examined (§6.2, p.15).
- **Fees:** 0.11% round trip on notional, charged in simulation; breakeven win rate 50.25% at the deployed geometry.
- **Funding:** not charged in the card; a real and often adverse cash flow for a book that is about two thirds short (§6.2, p.14). No funding figure is printed anywhere → `data gap`.
- **Spread / impact / slippage:** no modelled line printed → `not stated in source`.
- **Leverage / margin:** 8×, 15% margin, 95% capital cap, one position per coin; leverage capped in code, drawdown breaker with an immovable ceiling, withdrawal never exposed (§3, p.6; §8, p.20).
- **Liquidation / auto-deleveraging:** the source names auto-deleveraging exposure as a real crypto-specific risk with no equity counterpart (§2, p.5) but states no liquidation or ADL rule → `not stated in source` (data gap).
- **Capacity / participation:** `not stated in source`; no volume, depth or participation cap appears in the pinned PDF (data gap).
- **Latency / partial fills / failures:** `underspecified` beyond the 3.4-minute protection window and the fail-open chase filter.

## Evidence

### Source-reported

Every figure below is from the pinned PDF (SSRN 7353678, SHA-256 `3a7f9649…`); all are third-party claims and none has been reproduced by us.

**Headline contradiction (Abstract p.1; §1 p.2; Figure 1 p.4).** Backtest of the deployed configuration over the six weeks it was trained/selected on: **about 170%**. Live account over the same calendar span: **-21.6%**, a loss of **10.86 dollars on 50.29 dollars** of deposited capital across **96 closed trades** from 2026-06-18. Over the live window, the same eleven configurations returned between **125% and 179%** in simulation (Figure 1 caption, p.4).

**Table 1, p.7 — the deployed card as reported and as qualified (values in the left column are the card's own claims).**

| Field | As reported on the card | What the audit says it conceals |
|---|---|---|
| Window | 2026-06-01 to 07-13, about 28 trading days | the exact span the card was selected on |
| Trades | 190 fires, 110 taken | about 40 independent bets (mean uniqueness 0.213) |
| Size | 15% margin, 8× leverage = 120% notional | verified in code, not on the live box |
| Geometry | TP +2.1% / SL -1.9%, 0.11% round-trip fee | funding not modelled; the book is about 66% short |
| dirWR | 65.3% | flat across all 11 configs (62.9 to 65.3): K adds nothing |
| realWR | 69.1% | about 59% excluding one week; then p = 0.155 |
| ROI | +158.8% (compounded, leveraged, $1000) | argmax of 100+ configs; non-monotone in K |
| maxDD | 14.1% | closed equity only; peak notional near 600% |
| Sharpe | 12.66 | 10.81 with flat days restored; a small-sample artifact |
| Baseline | none | blind short on the same fires already makes +14.6% |

**Table 2, p.8 — side-randomisation permutation test (2,000 runs, pipeline held fixed).** Observed real-side book: ROI **+158.8%**, realWR **69.1%**, maxDD **14.1%**, n = 190. Null mean **+21.9%** with realWR **55.2%**; null median **+20.5%**, p95 **+60.6%**, p99 **+80.2%**, null maximum **+131.5%**; empirical p-value **0.0** (0 of 2,000 null runs reached +158.8%). The non-zero null mean is attributed to the window being a net down market while the book leans short.

**Selection / sample (§6.1, pp.10–13; Figures 4–7).** Readiness sweep on the deployed admission rule: **K=2 → 179.6%**, **K=3 → 174.9%**, **K=4 → 145.6%**, **K=5 (deployed) → 158.8%**, **K=6 → 136.6%**; K=5 was chosen for the lowest drawdown (**14.1%** vs **22.5%** at K=2), an advantage the audit traces to a single loss cluster; later-half window K=2 **162.9%** vs K=5 **137.2%** (§10, p.21). Sharpe **12.66** as reported → **10.81** with flat days restored, both annualised by √365 over about 40 days; under a deflated-Sharpe accounting the reported Sharpe fails beyond an honest trial count of about **164** (§6.1, p.11; Figure 5, p.12). One ISO week holds **50 of 190** trades and wins at **82.0%**; excluding it drops directional win rate **65.3% → 59.3%** and realised win rate to about **59%**, at which point the gap to the 50.25% breakeven is not significant (**p = 0.155**); a separate estimate excluding the lucky week still puts per-trade return at about **0.45%** with bootstrap interval **0.13 to 0.75** (§6.1, pp.12–13; Figure 6). Mean trade uniqueness **0.213** ⇒ roughly **40 independent bets** (§6.1, p.13; Figure 7).

**Frictions (§6.2, pp.14–15).** Funding: book about **two thirds short**, held across up to **six funding settlements per trade**, card charges **no funding**. Unrealised risk: reported maxDD **14.1%** is closed-equity only; up to **five** concurrent same-side positions at 8× ⇒ peak notional near **600%** of equity, so a 2% correlated adverse move is a 12% unrealised swing invisible to the closed-equity curve. Execution: **11** live entries reconstructed; limit anti-correlated with alpha; protection arrives after about **3.4 minutes**; chase filter fails open on hot tape; backtest fills at a clean open price.

**Learning gate (§6.3, pp.15–17; Figure 8, p.16).** Graduation rule = ≥5 resolved trades and last-10 win rate ≥56%; under a fair coin it passes about half the time at 5 trades and never below a quarter; expected graduated cells among **105** eligible = **47.5** vs observed **47**, **p = 0.92**; gate information content `under half a bit`; three of five advisers reached this independently. Raising K from 2 to 5 removes **60 trades** whose directional win rate (**63.3%**) is indistinguishable from the kept trades (**65.3%**), **p = 0.78**. Ledger contamination: the collector selected every executor row whose action merely contained `entry` with no version filter and no date lower bound, so about **88%** of the collected union was foreign-strategy fires; the union labelled real trades with the replay's synthetic 48-hour bracket; the fix collapsed the union from **252 rows to 11**.

**Signal reproducibility (§6.4, pp.17–18; Figure 9).** Deterministic voter over **34,000** scan-and-coin rows agrees with the model signature on **0.2%** of cases, yields **87** vs **1,654** distinct signatures, and finds no content in crowd/news lanes. Rebuilt into the same book pipeline with the chase and carry overlays stripped from both: model signal **+42%** return with **59.4%** directional win rate (explicitly an in-sample backtest figure on the card window, not a live result) vs deterministic signal **-14.7%** with **49.8%**.

**Prior version, same shape (§7, pp.18–19).** One iteration earlier deployed on a backtest of about **102%**; its honest full walk-forward card showed realised win rate **53.2%** against breakeven **54.8%**, return **-13.68%**, drawdown **61.9%**. A labelling experiment: rescoring with labels aligned to how live trades actually exit dropped realised win rate to about **46%** and return to **-22.98%**, tripping both pre-committed kill thresholds, while the original 24-hour mark-to-market label had shown a positive return and win rate near **56%**.

**What was sound (§8, pp.19–20).** Causal walk-forward with no look-ahead leak and an independent leak audit that held; honest bracket accounting whose breakeven reconciled exactly when recomputed independently; capital cap and one-position-per-coin faithfully modelled, with an independent replay reproducing the taken trade count to the exact number; sizing at about 6% of full Kelly; leverage capped in code; drawdown breaker ceiling immovable; withdrawal never exposed; live-vs-replay signature fidelity **97.3%**.

**Checklist (§9, Table 3, pp.20–21).** Seven gaps: selection, sample size, funding, unrealised risk, execution, learning gate, signal source.

**Status of the source's own claim.** The paper's conclusion is narrow: `a real directional edge of unknown and probably modest magnitude, not yet shown to survive its own execution` (§10, p.22). It is a negative result about a live deployment written by the person who deployed it, a vantage the source itself flags as having both a bias to guard against and access to claim (§10, p.22).

### Independently reproduced

Not independently reproduced.

No public repository exists at read time (`Data and Code Availability`, p.23: available from the author on reasonable request; companion repository `in preparation`), so the permutation test, the K sweep, the gate statistics and the live reconciliation could not be re-executed. Nothing in this record has been validated by us.

### Negative evidence

1. The live account lost **21.6%** over the same calendar span in which eleven backtest configurations of the same rulebook returned **125%–179%** (Figure 1, p.4) — a sign change, not a slippage difference.
2. The headline **+158.8%** is an argmax over **100+** configurations on one window, chosen for low drawdown rather than return (§6.1, p.10).
3. The deployed K=5 is never the highest-earning setting: K=2 (**179.6%**) and K=3 (**174.9%**) both exceed it, full window and later half alike (§6.1, p.10; §10, p.21).
4. The drawdown advantage that justified deployment (14.1% vs 22.5%) is traced to a **single loss cluster** in a 43-day sample, identical to a tenth of a percent across K=5 and K=6 and across different admission rules (§6.1, pp.10–11).
5. Sharpe **12.66** is computed with flat days dropped and annualised over about 40 days; restoring flat days gives **10.81** (§6.1, p.11; Figure 5).
6. Under a deflated-Sharpe accounting the reported Sharpe fails beyond about **164** trials (§6.1, p.11).
7. **~40 independent bets**, not 190 (mean uniqueness 0.213) (§6.1, p.13; Figure 7).
8. One ISO week supplies 50 of 190 trades at 82.0% wins; excluding it leaves ~59% realised win rate, statistically indistinguishable from breakeven (**p = 0.155**) (§6.1, pp.12–13).
9. The directional win rate is **flat across all 11 configurations** (62.9%–65.3%), so the readiness parameter adds nothing to it (Table 1, p.7).
10. A **blind short** on the same fires already returns **+14.6%**, and the random-side null averages **+21.9%** — much of the card's level is short beta in a falling window (§5, p.9; Figure 3, p.10).
11. **Funding is not modelled** on a book that is about two thirds short, held across up to six settlements per trade (§6.2, p.14).
12. Max drawdown **14.1%** is closed-equity only while peak notional approaches **600%** of equity, so margin risk is invisible in the reported risk number (§6.2, p.14).
13. Price-improved limit entries are **anti-correlated with their own alpha** on the 11 reconstructed live entries — winners missed, losers filled; `good trades small, bad trades full` (§6.2, pp.14–15).
14. That execution channel is reconstructed from **11 entries** and is not measured as a return, and a later deployment with a different order type showed no such gap on its examined trades (§6.2, p.15) — the size of the channel remains unquantified.
15. Protection on a fresh fill arrives about **3.4 minutes** late, and the chase filter fails open precisely when the tape is hot (§6.2, p.15).
16. The readiness gate graduates at the fair-coin rate: **47 observed vs 47.5 expected, p = 0.92** (§6.3, p.16; Figure 8).
17. Trades removed by raising K are of the same quality as those kept: **63.3% vs 65.3%, p = 0.78** — the gate is an exposure dial, removing ~24% of exposure, not losers (§6.3, pp.15–16).
18. The gate's training ledger was **~88% foreign-strategy fires**, with real trades mislabelled by a synthetic 48-hour bracket (union 252 rows → 11 after the fix) (§6.3, pp.16–17).
19. A deterministic reconstruction of the signal collapses to a coin flip: agreement **0.2%**, return **+42% → -14.7%**, win rate **59.4% → 49.8%** (§6.4, pp.17–18; Figure 9).
20. The signal therefore cannot be studied, attributed or trusted as anything but a property of one model at one point in time, and that model can be changed or retired by a third party (§6.4, p.18).
21. The prior version shows the same shape: **102%** backtest vs honest walk-forward **-13.68%** with **61.9%** drawdown (§7, p.18).
22. In the prior version the apparent edge was an artefact of the label: aligned labels gave ~**46%** win rate and **-22.98%**, tripping both pre-committed kill thresholds (§7, p.19).
23. The permutation test validates neither magnitude nor execution: it fixes the readiness parameter and resolves every fire on a clean tape, and beating random side assignment is a weak bar in its own right (§5, p.9; §10, p.21).
24. Single program, twenty instruments, two windows of a few weeks, 96 live trades, no public code, working-paper status, self-authored negative result, and no third-party replication identified (§10, pp.21–22; Provenance).

## Falsification plan

All thresholds below are **research-defined falsification thresholds** and all operationalisations are **research-proposed**; none of them is specified by the source except where explicitly attributed.

- **F1 — Frozen forward replication.** Freeze the rulebook and the K sweep now; run 24 months of forward paper trades from **2026-10-01** on the same 20-contract universe. *Failure:* forward net return fails to exceed the blind-short baseline on the same fires (research-defined: net excess ≤ 0).
- **F2 — Selection-inflation test.** Re-run the full configuration sweep on a window disjoint from 2026-06-01→07-13 (the source states its own history does not reach far enough back, §10 p.21). *Failure:* the deployed K=5 does not land in the top tercile of the out-of-sample sweep (research-defined).
- **F3 — Deflated-Sharpe gate.** Require the reported Sharpe to clear a deflated-Sharpe threshold at an honest trial count of at least **164** (the source's own figure). *Failure:* it does not clear (research-defined).
- **F4 — Permutation replication on fresh data.** Re-run the 2,000-draw side randomisation on a fresh window with the carry veto recomputed per flipped side (the source documents it as left at its original value). *Failure:* empirical p ≥ 0.05 (research-defined).
- **F5 — Naive-baseline excess return.** Add the stricter test the program itself later adopted: same-scan excess over blind short and over holding the lowest-volatility coin, net of the 0.11% round trip. *Failure:* excess ≤ 0 after costs (research-defined).
- **F6 — Funding-inclusive restatement.** Add realised funding settlements (up to six per trade) to the card economics. *Failure:* restated return falls more than 50% below the reported +158.8% (research-defined).
- **F7 — Execution realism.** Replay the strategy against its own realised fills (and against a next-available-price fill model) instead of a clean open. *Failure:* realised entry slippage + missed-winner censoring consumes ≥ 20% of gross edge, or the fill-winner-miss rate exceeds the fill-loser rate at binomial p < 0.05 (research-defined).
- **F8 — Exposure and margin audit.** Re-state drawdown on peak notional (~600% of equity) rather than closed equity, including an ADL/liquidation rule. *Failure:* probability of a margin event at deployed sizing exceeds 1% over the test window (research-defined).
- **F9 — Effective-sample honesty.** Block-bootstrap with the observed mean uniqueness of 0.213 so that inference runs on ~40 independent bets. *Failure:* the 95% interval for per-trade edge includes 0 (research-defined; source's own exclusion-week estimate is 0.45% with CI 0.13–0.75, §6.1 p.12).
- **F10 — Lucky-week removal.** Recompute win rate excluding the worst/largest ISO week each period. *Failure:* win rate ≤ breakeven + 2 percentage points (research-defined: ≤ 52.25% against the source's 50.25% breakeven).
- **F11 — Learning-gate validity.** Re-test graduation counts against a fair-coin null and removed-vs-kept trade quality. *Failure:* both tests remain non-informative (research-defined: p ≥ 0.10 on both, matching the source's p = 0.92 and p = 0.78).
- **F12 — Signal reproducibility.** Publish a deterministic reconstruction from the written rule and compare with recorded votes. *Failure:* agreement with recorded votes < 90% and the reconstructed book does not beat the random-side null (research-defined; source: 0.2% agreement, -14.7%).
- **F13 — Ledger hygiene.** Rebuild the readiness ledger with strategy-version filtering, a date lower bound, and realised P&L labels. *Failure:* any foreign-strategy row or bracket-mislabelled trade remains (research-defined: contamination > 1%; source: 88%).
- **F14 — Robustness and reproduction gate.** Three subperiods plus a second venue, and independent re-execution of the audit scripts to ±10% on every headline figure. *Failure:* sign flip, >50% magnitude loss, or reproduction outside ±10% (research-defined).

Action on failure: the record stays `research-only`, `not-implemented`, `not-approved`; no implementation, paper, testnet or live step follows, and the hypothesis is marked weakened or rejected in a later record rather than retuned.

## Crypto portability

**direct.**

The evidence base is itself crypto: Binance USD-margined perpetual futures, hourly cadence, one-minute bracket resolution, 24/7 markets. Porting questions that remain `data gap` inside this direct setting:

- **Spot vs perpetual:** the program trades perpetuals only; no spot leg, so basis and spot-market comparison are absent.
- **Funding:** identified by the source as a real cost but never charged in the card — any crypto deployment must model it (up to six settlements per trade were held).
- **Liquidation / auto-deleveraging:** named by the source as crypto-specific exposure, but no liquidation or ADL rule is printed.
- **24/7 session structure and timezone:** signal cadence is `once an hour` with no timezone, calendar or candle-boundary convention stated.
- **Venue fragmentation:** single-venue evidence; no cross-venue fill, index/mark price or fragmented-liquidity treatment.
- **Contract specification / mark price:** margin, leverage and capital caps are stated; mark-price basis, tick size, minimum notional and contract adjustments are `not stated in source`.
- **Custody / withdrawal:** the source states withdrawal was never exposed in the execution layer (§8, p.20); custody risk is otherwise unaddressed.

Crypto portability is not authorization to trade.

## Limitations

- `underspecified`: snapshot feature set, per-lane vote semantics, signature reduction, regime-label definition, chase-filter and carry-veto triggers, entry limit offset, maximum holding time, the 20 symbols, timezone.
- `data gap`: no public code or data (author-on-request only, repository `in preparation`), no funding figure, no spread/slippage/impact model line, no capacity/volume analysis, no liquidation rule, no point-in-time universe rule.
- `not stated in source`: peer-review status, reference count on SSRN (0) versus the PDF's 16 references, capacity, venue alternatives.
- Source-level discrepancies left unreconciled: author spelling `Alexandr` (SSRN) vs `Aleksandr` (PDF); `Posted 27 Aug 2026` vs `Date Written July 10, 2026` vs PDF `This version: August 2026`; SSRN CC BY-NC-ND badge versus the PDF's all-rights-reserved notice; abstract `roughly 170 percent` versus the card's `+158.8%` (the ~170% figure sits inside the 125%–179% eleven-configuration range).
- `not independently reproduced`: every quantitative claim in this record is third-party, source-reported.
- `unproven`: H1–H4 are hypotheses raised by the source's case study on one program, twenty instruments and two windows of a few weeks; the source itself says the specific numbers are illustrative and only the structure of the gap generalises (§10, p.21).
- Bias framing: a negative result written by the deployer, with the access and the salvage-temptation that implies (§10, p.22).
- Incremental-write check: this is a new source identity with a materially distinct mechanism (live-versus-backtest anatomy with a positive permutation result, execution-fill reconstruction, gate-validity statistics and an LLM-emitted non-reproducible signal); it is not a reframing of an existing record.

## Implementation status

`implementation_status: not-implemented`.

No implementation exists in our research stack. We did not run a backtest, a permutation test, a replay or any NautilusTrader/Qlib/Paper/Testnet/Live step. Nothing in this record implies Research Intake Review, Wiki Brain ingestion, production-candidate-pool entry, Qlib validation, survivor status, or Paper/Testnet/Live approval.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

Presence of this record in the staging repository means only normalised, source-traceable research material. The source's own conclusion is that a real directional edge is necessary but nowhere near sufficient, and that this particular program's edge is of unknown and probably modest magnitude, not yet shown to survive its own execution (§10, p.22). That conclusion, and this record, are not an endorsement.

## Related Wiki records

A Wiki Brain `kb_search` for `backtest to live gap execution adverse selection permutation test crypto perpetual` returned 7 adjacent pages and **no page for this source**; a second search for `deflated Sharpe backtest overfitting selection bias multiplicity live deployment` returned **0 pages**. No exact-mechanism page exists, so no canonical page is linked as the record's identity. Verified adjacent pages returned by the first search (exist, read-only):

- [[quant/retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11]]
- [[quant/crypto-smc-fvg-bpr-liquidity-retracement-random-walk-falsification-2026-09-12]]
- [[quant/crypto-perpetual-pairs-trading-cointegration-hurst-halflife-walkforward-2026-09-12]]

Distinctions against adjacent repository records (source identity and mechanism differ in every pair):

- `crypto-retail-systematic-trading-null-result-adversarial-audit-2026-09-01.md` — SSRN **7085378**, Castellanos Macias: pre-registered adversarial audit of retail systematic rules 2018–2026 with a null result and **no live deployment**; this record is a **live-account** reconciliation with a positive permutation result, fill reconstruction and gate-validity statistics.
- `llm-strategy-discovery-leakage-safe-search-deflated-eval-2026-09-04.md` — arXiv **2608.27734**, Gençay: rejects LLM-discovered strategies on US equity/ETF universes by trial-count deflation; this record is a single deployed **crypto-perp** program whose failure channels are funding, unrealised exposure, execution censoring and a contaminated gate.
- `rejected-post-only-order-flow-directional-predictor-hyperliquid-2026-09-14.md` — mechanism is post-only fill probability; this record's mechanism is program-level backtest-to-live decomposition of an LLM side signal.
- `bitcoin-semivolatility-upside-downside-exposure-timing-2026-09-27.md` — SSRN **7226305**: exposure-timing by semivolatility ratio; no overlap in source, signal construction or horizon.

## Sources

- Aleksandr / Alexandr Dashyan, *A Real Edge that Loses: Anatomy of a Backtest-to-Live Gap in Cryptocurrency Perpetual Futures*, SSRN preprint, `abstract_id=7353678`, DOI [10.2139/ssrn.7353678](https://doi.org/10.2139/ssrn.7353678), landing page <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7353678>, `Posted: 27 Aug 2026`, `Date Written: July 10, 2026`, 25 pages; pinned PDF retrieved 2026-09-27 via the SSRN `Open PDF in Browser` delivery link, 626,354 bytes, SHA-256 `3a7f96498714a3e2a3e6b8e73155940de0b0d207de58b305a1b26cc7dd40409c`, read page by page.
- Companion works cited **by the source** but with no identifier printed (identity `not stated in source`): Dashyan (2026a) *Short-horizon directional non-predictability in cryptocurrency perpetual futures: a multi-method negative result under adversarial verification*; Dashyan (2026b) *Adversarial backtest verification: catching overfitting, beta, collinearity, and look-ahead in a live trading-research program*; Dashyan (2026c) *Risk control as the durable edge: loss filtering, profit-armed ratchets, and market-neutral carry when direction fails* — all `Working paper` (PDF References [5]–[7], p.24).
- Methodological works referenced by the source for its own tests (listed as the source lists them, pp.24–25): Bailey/Borwein/Lopez de Prado/Zhu (2014, 2017), Bailey & Lopez de Prado (2014), Harvey & Liu (2015), Harvey/Liu/Zhu (2016), Lo (2002), Lopez de Prado (2018), Makarov & Schoar (2020), Novy-Marx & Velikov (2016), Perold (1988), Sullivan/Timmermann/White (1999), White (2000), Arnott/Harvey/Markowitz (2019).
