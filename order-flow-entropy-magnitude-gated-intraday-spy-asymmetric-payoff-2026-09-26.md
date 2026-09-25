---
schema: strategy-research-record-v1
title: "Order-flow entropy magnitude gate with asymmetric payoff on SPY intraday trades (arXiv:2512.15720v1)"
created: 2026-09-26
updated: 2026-09-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - arxiv
  - market-microstructure
  - order-flow-entropy
  - volatility-state
  - intraday
  - magnitude-not-direction
  - walk-forward
  - asymmetric-payoff
  - falsification
  - negative-evidence
status: research-only
confidence: medium
source_as_of: 2026-09-26
sources:
  - "arXiv:2512.15720v1 [q-fin.TR], 'Hidden Order in Trades Predicts the Size of Price Moves', Mainak Singha (sole author); submitted Tue, 2 Dec 2025 23:20:46 UTC (545 KB); https://arxiv.org/abs/2512.15720 (abs read 2026-09-26)"
  - "https://arxiv.org/html/2512.15720v1 — pinned v1 HTML, 67,336 bytes, SHA-256 9c23681d61d79ec63ef4c246f0992e57d04e3250cca8ffb5f59ecc136ca806fd (retrieved 2026-09-25, re-fetched and re-hashed 2026-09-26 with identical hash); full body read end to end for this record"
  - "https://arxiv.org/pdf/2512.15720v1 — pinned v1 PDF, 898,319 bytes, SHA-256 bdd3689374f22596d13cd7bf384af95fbea524451ddcf015653b90ecd1acc85d (retrieved 2026-09-25, re-downloaded and re-hashed 2026-09-26 with identical hash)"
  - "https://doi.org/10.48550/arXiv.2512.15720 — DataCite DOI issued by arXiv (checked 2026-09-26 on abs)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions:
  - "Source-internal (pinned v1): the identical t-statistic t=12.41 (p<10^-4) is printed twice for two different quantities — once for the '<5th-percentile entropy conditioning' magnitude factor 2.89 (abstract and the Figure-1 results paragraph) and once for the pooled walk-forward Magnitude Ratio 2.17 in Table 1. The pinned text never states which test produced t=12.41. Our reconstruction of a one-sample t-test across the five printed fold ratios (2.41, 2.18, 2.31, 1.89, 2.06) gives mean 2.17 and t=12.77 against 1.0, which is close to but not equal to 12.41, so the provenance of the statistic is underspecified rather than demonstrably wrong."
  - "Source-internal (pinned v1): the same count 108/240 = 45.0% is printed both as binomial directional accuracy ('108/240 out-of-sample trades', Figure 2 paragraph, z=-1.55, p=0.12) and as the pooled Table 1 Win Rate over 240 trades. Summing the five printed fold win rates (71.9%, 33.3%, 44.2%, 41.7%, 40.2%) over their printed trade counts (32, 27, 77, 12, 92) gives 108.02 wins, i.e. exactly the same 108. The pinned text does not say whether 'directional accuracy' and 'win rate' are the same measurement; if they are, Figure 4's separate claim that direction contributes 0.0% of PnL rests entirely on the direction-randomization Monte Carlo and not on the binomial test, and the Table 1 caption's 'win rate below 50% confirms absence of directional edge' is a win-rate statement, not a direction statement. This record flags the ambiguity and does not silently reconcile it."
---

# Order-flow entropy magnitude gate with asymmetric payoff on SPY intraday trades (Hidden Order in Trades Predicts the Size of Price Moves, arXiv:2512.15720v1)

## Provenance

**Primary source.** arXiv:2512.15720**v1**, category `q-fin.TR` (cross-lists `q-fin.ST`, `stat.AP`, `stat.ME`), title *Hidden Order in Trades Predicts the Size of Price Moves*, complete author list exactly as printed: **Mainak Singha** (sole author), with the affiliation block printed as *Astrophysics Science Division, NASA Goddard Space Flight Center, 8800 Greenbelt Road, MD 20771* and *Department of Physics, The Catholic University of America, Washington, DC 20064*. The manuscript header line reads `November 2025`; the submission history shows a single version `[v1] Tue, 2 Dec 2025 23:20:46 UTC (545 KB)`. `https://arxiv.org/abs/2512.15720v2` and `https://arxiv.org/html/2512.15720v2` both return **HTTP 404** (checked 2026-09-26), so v1 is the sole and latest version as of 2026-09-26.

**Metadata / status.** The abs page carries a **Comments field** (the long one-sentence summary about hidden order predicting move size but not direction, 38.5M SPY trades, 5-fold walk-forward, z=14.4 placebo), **no journal-ref**, and **no publisher DOI** beyond the arXiv-issued DataCite DOI `10.48550/arXiv.2512.15720`. No peer-review or acceptance statement appears anywhere in the pinned body. License line in the pinned HTML: **CC BY 4.0**, so the text is cited and normalized here rather than reproduced at length. Publication status = **preprint only** (`not stated in source` for any journal).

**Pinned snapshots (re-verified this run).** Pinned HTML `https://arxiv.org/html/2512.15720v1` = **67,336 bytes, SHA-256 `9c23681d61d79ec63ef4c246f0992e57d04e3250cca8ffb5f59ecc136ca806fd`**; pinned PDF `https://arxiv.org/pdf/2512.15720v1` = **898,319 bytes, SHA-256 `bdd3689374f22596d13cd7bf384af95fbea524451ddcf015653b90ecd1acc85d`**. Both were first retrieved 2026-09-25 and re-fetched/re-hashed on 2026-09-26 with byte-identical hashes (idempotent pin). The stripped text of the pinned HTML is 195 lines / 14,636 characters of body (abstract, Sections 1–5-equivalent narrative, Empirical Results, Robustness, Limitations, **Methods (Data / State Space Construction / Entropy Computation / Signal Definition / Walk-Forward Protocol / Trading Rule / Statistical Tests / Code and Data Availability)**, Figure 1–4 captions, Table 1, References [1]–[11]); it was read end to end for this record. The paper is a short letter — there is no separate numbered Methods section heading, but the eight Methods sub-headings listed above exist and were read in full (this satisfies the Methods-level cost/execution read required for the transaction-cost judgment below).

**Code and data.** Methods §Code and Data Availability, verbatim in substance: *analysis code available upon request; data from commercial tick-data vendors, access requires appropriate licensing.* There is **no repository, no commit, no public dataset and no data-availability statement in a machine-checkable form**, so every reproducibility field is a `data gap` and this record cites no code SHA.

**Data as-of.** Trade sample **1 October 2025 – 19 November 2025, 36 trading days**. `source_as_of: 2026-09-26` is the date the primary source was pinned and re-verified.

**Repo-wide dedup (run 2026-09-26, before writing).** `git pull origin main` was *Already up to date* and `git status --porcelain --untracked-files=no` was **clean** before research began; `git log --oneline -20` was inspected as a convenience glance only. A hidden-inclusive ripgrep scan then walked **all 2,549 `*.md` files** in the repository (including `.mimo-worktrees`, `.agents`, `.hermes`) plus `coverage_manifest.csv` (5,808 lines), testing 15 source-identity patterns: `2512.15720`, `10.48550/arXiv.2512.15720`, `Hidden Order in Trades`, `Size of Price Moves`, `Time-Dependent Entropy`, `38,509,593`, `828,907`, `1,125.6`, `1126 bps`, `magnitude predictability`, `stationary-weighted`, `permutation invariance`, `15-state Markov`, `order-flow entropy`, `Mainak Singha`. **The first 14 patterns returned 0 files in `*.md` and 0 hits in `coverage_manifest.csv`** (combined `rg` exit 1 = no match). `Mainak Singha` resolved only to two *different* papers — `drift-regime-gated-cross-sectional-value-reversal-2026-09-05.md` (arXiv:2511.12490) and `forecast-to-fill-gold-futures-friction-adjusted-kelly-alpha-2026-09-02.md` (arXiv:2511.08571) — neither of which shares this source identity. Near-mechanism probes (`15-state`, `permutation invariance`, `entropy … volatility state`) cleared as unrelated: a CLMM position taxonomy and a TradingView entropy-gated RSI divergence script. No existing record for this source identity was found, so no material-distinction argument is required for creation; the four-axis distinction against the nearest *mechanism* neighbours is stated under **Related Wiki records**.

## Economic mechanism

### Source-reported

The source argues (abstract, theory paragraphs, Methods) that:

- **Directional unpredictability and magnitude predictability are different claims.** Weak-form efficiency constrains the *sign* of the next move, not its *size*; magnitude is a distinct forecasting target.
- **Informed trading leaves a sign-symmetric trace.** In the Kyle (1985) and Glosten–Milgrom (1985) frameworks an informed trader produces persistent order flow, i.e. a departure from random transitions in the transaction sequence, *regardless of direction*: "An informed buyer generates the same entropy signature as an informed seller."
- **The signal is a time-dependent order-flow entropy.** Each second the market is in one of `K = 15` states = sign of the second-over-second price change `{-1, 0, +1}` × volume quintile `{1..5}` (quintiles from the empirical CDF of volume over the trailing 120 s). A transition matrix is estimated over a rolling **120-second** window and entropy is the **stationary-distribution-weighted average of row entropies normalized to [0,1]** by `1/log 15`. Low entropy = structured/persistent transitions; high entropy = unpredictable.
- **Two formal predictions (Theorem 1 and Theorem 2).** `E[|r(t,t+Δ)| | H_t < H̲] > E[|r(t,t+Δ)|]` for sufficiently low `H̲`, and `E[sgn(r(t,t+Δ)) | H_t] = 0` when informed traders are equally likely to be buying or selling. The stated proofs rest on **entropy's invariance under label permutation**: swapping the buy/sell labels maps one transition matrix to another with identical entropy, so entropy cannot carry the sign.
- **The empirical claim.** On 38.5M SPY trades the source reports that conditioning on entropy below the 5th percentile raises subsequent 5-minute absolute returns to **15.3 bps versus an unconditional 5.29 bps (factor 2.89, t=12.41, p<10⁻⁴)** while directional accuracy stays at **45.0% (108/240, binomial z=−1.55, p=0.12)**; quintile means decline monotonically from **8.14 bps (Q1, low entropy) to 3.75 bps (Q5)**, ratio 2.17 (Figure 1).
- **The tradable claim.** A "simple asymmetric-payoff rule — entering when entropy is low and using tight stop-losses" produces **+1,126 bps cumulative out-of-sample PnL over 240 trades across five walk-forward folds**, with profit attributed **87.8% to timing, 12.2% to payoff structure, 0.0% to direction** (Figure 4, 10,000 random-entry Monte Carlo). The source explicitly frames entropy as a *volatility state variable* for intraday timing, not as a directional signal, and states the backtest is academic and not investment advice.

### Research interpretation

Two separable, falsifiable hypotheses are embedded in one strategy:

1. **State-variable hypothesis (mechanism):** transition-entropy of the second-level price-sign × volume-quintile chain is a real-time proxy for the latent intensity of informed/liquidation-driven flow, and therefore forecasts *absolute* 5-minute returns — a volatility/timing state, not an alpha sign. The permutation-symmetry argument makes this plausible a priori: any statistic invariant to sign labels cannot encode direction.
2. **Payoff hypothesis (mechanism, not alpha):** the printed PnL comes from *asymmetry* — a 5 bps stop against an unstated, training-frozen take-profit and a 300-second time stop — conditional on being in the state where large moves are more likely. The source's own attribution (87.8% timing / 12.2% payoff / 0.0% direction) says the edge is **when**, not **which way**.

Component roles (source-reported unless marked):

```text
Regime/state gate:     H_t < training-period 5th percentile of entropy (rolling 120 s, 15-state chain)
Confirmation filter 1: volume in the current second > 95th percentile
Confirmation filter 2: trailing 5-minute return between +5 and +20 bps (activity without the move already over)
Entry direction:       sign of the trailing 5-minute return (explicitly a "momentum heuristic")
Risk / exit:           5 bps stop-loss | 300-second timeout | fixed take-profit threshold frozen on training data (VALUE NOT PRINTED)
Cadence:               10 training days / 5 test days, 5 non-overlapping walk-forward folds, Oct 15 – Nov 18, 2025
```

Do not assume each component contributes: the source runs **no ablation** of the entropy gate against the volume and prior-move filters, so whether entropy adds anything beyond a volume-spike + range filter is an open question (falsification F4/F5). A simpler reading of the entry rule is "volume surge + modest prior drift, sized for a follow-through move", with the entropy gate possibly redundant — this is a competing explanation, not a source claim.

## Signal

All items below are **source-reported unless explicitly marked** `research-proposed` / `underspecified` / `data gap`.

- **Formation timestamp.** Per-second bars built from tick trades; entropy `H_t` uses the trailing 120 s. The tradable moment is "at signal" in the Trading Rule. **Timezone and session convention are `not stated in source`**; the sample counts `regular-hours trades: 34,083,179` of `38,509,593` total, implying extended-hours trades are excluded from that subtotal but the bar count (see Required data) is consistent with regular hours only. US equity regular-session hours are the obvious reading, but the pinned text never states a clock or timezone → `data gap`.
- **Lookback.** Rolling **120 seconds** for both the transition matrix and the volume empirical CDF; second-over-second price change for the sign state; **5 minutes** for the trailing return filter and the outcome horizon; **10 training days** for all percentile thresholds; **quintile/percentile thresholds frozen on training data** for the walk-forward (source-stated). Endpoint inclusivity (≤ vs <) is `underspecified`.
- **State definition.** `q_t = sgn(P_t − P_{t−1}) ∈ {−1,0,+1}`; `v_t = ceil(5 · F_{V,t}(V_t)) ∈ {1..5}` with `F_{V,t}` the trailing-120 s empirical CDF of volume; `S_t = (q_t, v_t)`, `|S| = 15`. Rows with no observed transitions are filled with `p_ij = 1/15`; stationary distribution `π` by eigendecomposition; `H_t = −(log 15)⁻¹ Σ_i π_i Σ_j p_ij log p_ij`.
- **Entry trigger (all three must hold).** `H_t < H_{0.05}` (5th percentile of `H` over the training period) **and** volume > 95th percentile **and** trailing 5-minute return ∈ [5, 20] bps. **The window over which the 95th-percentile volume threshold is computed is `underspecified`** (trailing 120 s, session-to-date, or training-frozen are all consistent with the text) → any replication must freeze this choice as `research-proposed`.
- **Entry direction.** Long if the trailing 5-minute return is positive, short if negative ("enter position in direction of trailing 5-minute return (momentum heuristic)"). **Short-side borrow/locate feasibility and cost are never mentioned** → `data gap`.
- **Exit (three-way, precedence not stated).** 5 bps stop-loss; 300-second timeout; or "a fixed take-profit threshold chosen ex ante in the training window". **The take-profit value is never printed anywhere in the pinned text**, and **the precedence rule when two exits coincide is not stated** → the payoff asymmetry that the source attributes 12.2% of PnL to cannot be reconstructed from the paper → `underspecified`.
- **Holding period.** Bounded above by the 300-second timeout, so positions are sub-5-minute. Overlapping positions: `underspecified` (no statement whether a new entry is permitted while a position is open).
- **Position sizing.** **Never stated** — no unit size, no notional, no fraction-of-capital, no volatility scaling, no leverage, no margin. The PnL column is in **bps**, so the aggregation convention (per-trade bps summed, as our arithmetic below confirms) is the only readable interpretation → `data gap`.
- **Parameters (all source-reported).** entropy 5th percentile; volume 95th percentile; 5–20 bps prior-move band; 120 s window; 15 states; 5 volume quintiles; 5-minute outcome horizon; 5 bps stop; 300 s timeout; 10/5-day walk-forward split; 5 folds; 0.57 bps round-trip cost; 1,000-trial label permutation; 1,000-trial temporal scrambling; 10,000-trial random entry; Bonferroni `α = 0.05/14 = 0.0036`; parameter sensitivity = **20 perturbations of ±50% on four parameters** (the four parameters are `not named` → `underspecified`).
- **Fully specified?** The **state construction, gate thresholds and walk-forward protocol are specified**; the **take-profit value, exit precedence, volume-percentile window, position sizing, session/timezone convention and the family of 14 Bonferroni tests are not.** A researcher can reproduce the *state variable* from the paper but cannot reproduce the *printed PnL* from the paper alone.

## Required data

- **Instrument / universe:** **SPY (SPDR S&P 500 ETF Trust) only**, single instrument, US equity ETF. No cross-section, no reconstitution, no survivorship handling (nothing to rebalance). The source does not justify instrument choice or claim generality beyond SPY.
- **Venue / market type / data vendor:** consolidated US equity trades; **vendor is named only as "commercial tick-data vendors"** with licensing required → `data gap`. Spot ETF, no derivatives, no crypto.
- **Timeframe:** tick trades aggregated to **1-second bars**. Sample totals: **38,509,593 trades** (of which **34,083,179 regular-hours**), **828,907 second bars** over **36 trading days (1 Oct – 19 Nov 2025)**. *Our count:* 828,907 / 36 = **23,025 bars per day**, which is **98.4% of the 23,400 seconds of a 6.5-hour regular session**, and 38,509,593 / 828,907 = **46.5 trades per bar**; the non-regular-hours share of trades is **11.49%** (4,426,414 trades). These are *our arithmetic inferences* — the pinned text never states the session window or timezone.
- **Fields required:** per-second closing price and total volume (Methods §Data states exactly these two fields per bar); the 5-minute trailing return derives from those closes. **Not required by the source:** order book/depth, aggressor-side flags, quotes/spreads (only a *typical* 0.17 bps quoted spread is cited for cost calibration, not as an input), open interest, funding, borrow rates, options, on-chain, sentiment.
- **Point-in-time:** the paper models **no publication lag, no revision handling and no look-ahead protection beyond the walk-forward freeze**; the state at `t` uses only data through `t` (trailing 120 s), which is mechanically point-in-time, but thresholds are training-frozen. Vendor tick reconstruction with restamped or revised prints is `data gap`.
- **Timestamp / clock:** `not stated in source` (timezone, millisecond vs microsecond precision, exchange vs consolidated clock, out-of-order/crossed-trade cleaning) → `data gap`. A replication must declare these as `research-proposed`.
- **Missing data:** no stale/suspension/partial-print handling is described; seconds with no trades simply do not appear as bars (implied by 23,025 < 23,400) → `underspecified`.
- **Funding / fee / spread needs:** equity ETF — **funding is not applicable**; spread and slippage enter only as the fixed cost model below; **borrow/short-loan cost for the short leg is never mentioned** → `data gap`.

## Execution assumptions

**Transaction-cost determination (Methods-level read, this run).** I read the eight Methods sub-sections of the pinned v1 body (Data, State Space Construction, Entropy Computation, Signal Definition, Walk-Forward Protocol, **Trading Rule**, Statistical Tests, Code and Data Availability) plus the Empirical Results, Robustness and Limitations paragraphs, then ran an occurrence scan over the 14,636-character body. Results:

| Term | Occurrences in pinned v1 body | Reading |
|---|---|---|
| `Transaction costs` / `slippage` / `spread` / `fees` | 1 / 1 / 3 / 1 | **all four occur inside the single Trading Rule cost sentence** |
| `turnover`, `market impact`, `participation`, `capacity`, `latency`, `ADV` (as participation), `leverage`, `margin`, `borrow`, `funding`, `liquidation`, `drawdown`, `net of` | **0 each** | no model, no number — every such field is `data gap`, never zero |
| `fill` / `fills` | 1 / 1 | only "execution assumptions (immediate fills, fixed costs) may not hold at scale" (Limitations) |
| `Sharpe` | 1 | **only inside reference [10] (Bailey & López de Prado)** — no Sharpe is reported for the rule |
| `stop-loss` / `take-profit` | 2 / 1 | exit rules; take-profit value not printed |

**The single cost sentence (source-reported, Methods §Trading Rule):** *"Transaction costs: 0.57 bps round-trip (half-spread entry + half-spread exit + 0.30 bps slippage + 0.10 bps exchange fees, calibrated to SPY's typical 0.17 bps quoted spread)."* Our check: 0.17 + 0.30 + 0.10 = **0.57** ✓ (one full spread across the round trip plus slippage plus fees).

Material assumptions, source vs. ours:

- **Signal-to-order timing / latency:** "enter at signal" — **no latency model, no queue position, no market-vs-limit choice** → `data gap`; source itself flags immediate fills as possibly unrealistic.
- **Fill model:** immediate fills at the trade price (implied), fixed 0.57 bps round trip; no partial fills, no rejections, no depth or participation cap.
- **Fees / spread / slippage:** as above — **fixed, calibrated once to a "typical" 0.17 bps quoted spread, not time-varying and not sampled from the realized spread distribution** → a material simplification for a rule that enters precisely when volume surges.
- **Impact / capacity:** **not modelled at all** → `data gap`. For a liquid ETF this is plausible at small size, but nothing in the source bounds size. *Our count:* 240 round trips × 0.57 bps = **136.8 bps of aggregate round-trip cost, equal to 12.15% of the printed 1,125.6 bps cumulative PnL** — so whether the printed PnL is gross or net materially changes the headline, and **the pinned text never says** ("net of" occurs 0 times) → `underspecified`.
- **Whether costs are applied:** the cost is listed inside the Trading Rule, which implies the printed PnL is net of it, but **no sentence states this** → `underspecified` (flagged in F3).
- **Borrow / shorting:** the direction rule can go short; **no borrow availability, locate, stock-loan fee or short-sell restriction is mentioned** → `data gap`.
- **Leverage / margin:** not stated → `data gap`.
- **Partial fills / failures:** not stated → `data gap`.
- **Sizing:** not stated (see Signal) → the bps-denominated PnL cannot be converted into capital efficiency, turnover, or a Sharpe without an assumption we would have to invent.

**Scout position:** nothing here is treated as tradable. The only source-specified cost is a fixed 0.57 bps round trip; everything else (`impact`, `capacity`, `borrow`, `latency`, `time-varying spread`, `net-vs-gross status`) is `data gap`/`underspecified` and is stress-tested as `research-defined` in F3/F9.

## Evidence

### Source-reported

All figures below are third-party claims from the pinned arXiv:2512.15720v1 and have **not** been independently reproduced. Provenance (Table/Figure/Section) is given for each.

**Magnitude claim (Figure 1 paragraph + abstract, full sample `n = 828,907` second bars, 36 days):**
- Unconditional mean |5-minute return| = **5.29 bps**; Q1 (lowest entropy quintile) = **8.14 bps**; Q5 = **3.75 bps**; Q1/Q5 ratio = **2.17** (our check: 8.14 / 3.75 = **2.171** ✓).
- Conditioning on entropy below the **5th percentile** → **15.3 bps**, factor **2.89** above unconditional (our check: 15.3 / 5.29 = **2.892** ✓), **t = 12.41, p < 10⁻⁴** (Welch's t-test, unequal variances, per Methods §Statistical Tests).
- Described as monotonic across entropy quintiles (Figure 1).

**Direction claim (Figure 2 paragraph):** directional accuracy **45.0% = 108/240 out-of-sample trades**, binomial test vs 50%: **z = −1.55, p = 0.12** (our check: (108−120)/√60 = **−1.549** ✓). Source reads this as no directional information, consistent with Theorem 2.

**Walk-forward protocol (Methods §Walk-Forward Protocol):** 10 training days → 5 test days, **non-overlapping** folds, thresholds estimated on training data only and frozen; **five folds covering Oct 15 – Nov 18, 2025**.

**Table 1 (walk-forward, source-reported, printed columns `Fold | Period | Trades | Win Rate | Magnitude Ratio | t-statistic | PnL (bps)`):**

| Fold | Period | Trades | Win rate | Magnitude ratio | t | PnL (bps) |
|---|---|---|---|---|---|---|
| 1 | Oct 15–21 | 32 | 71.9% | 2.41 | 8.7 | 179.9 |
| 2 | Oct 22–28 | 27 | 33.3% | 2.18 | 7.2 | 212.9 |
| 3 | Oct 29–Nov 4 | 77 | 44.2% | 2.31 | 12.1 | 433.2 |
| 4 | Nov 5–11 | 12 | 41.7% | 1.89 | 4.9 | 66.5 |
| 5 | Nov 12–18 | 92 | 40.2% | 2.06 | 9.3 | 233.1 |
| **Pooled** | | **240** | **45.0%** | **2.17** | **12.41** | **1,125.6** |

**Our arithmetic checks on Table 1:** trades sum **240** ✓; PnL sums **1,125.6 bps** ✓ (matches Figure 3's "+1,126 bps"); the five fold win rates imply **108.02 wins**, i.e. exactly the 108 used as "directional accuracy" (see frontmatter contradiction 2); fold 3 alone is **433.2 / 1,125.6 = 38.49%** of cumulative PnL, matching the source's own "October 29 alone contributed 38.5% of profits"; the mean of the five fold magnitude ratios is **2.17**, matching the pooled row.

**Figure 3:** cumulative out-of-sample **+1,126 bps** for the rule vs an SPY buy-and-hold line, **correlation 0.12**. **The buy-and-hold return value is never printed** → `data gap`, so no benchmark-relative excess return can be read off the source.

**Figure 4 (10,000 random-entry Monte Carlo):** **87.8% timing / 12.2% payoff structure / 0.0% direction**. *Our check:* the random-entry placebo mean of 137 bps / 1,126 bps = **12.17%** ✓ reproduces the 12.2% payoff share, so the decomposition is internally consistent.

**Robustness / placebos (§Robustness):**
1. Label permutation, 1,000 trials → magnitude ratio **1.02 ± 0.08**; observed 2.17 ⇒ **z = 14.4**, empirical p < 0.001.
2. Temporal scrambling, 1,000 trials → **z = 10.7**.
3. Random entry, 10,000 trials, identical payoff structure → mean PnL **137 ± 201 bps** vs observed **1,126 bps**, **z = 4.9** (our check: (1126−137)/201 = **4.92** ✓ — note this uses the *distribution* s.d., not the standard error of the mean).
4. Parameter sensitivity: **20 perturbations of ±50% on four (unnamed) parameters all remain profitable, worst case −40% of PnL** (our check: 1,125.6 × 0.6 = **675.4 bps**).

**Multiple testing (§Statistical Tests):** Bonferroni `α = 0.05/14 = 0.0036` (our check: 0.05/14 = **0.003571** ✓), "all primary results pass". **Which 14 tests form the family is not enumerated** → `underspecified`.

### Independently reproduced

**Not independently reproduced.** The Scout executed no backtest, recomputed no entropy series, and has no access to the licensed tick data; code is "available upon request" only. The only independent work performed is (a) arithmetic consistency checks on printed numbers, reported explicitly as *our count* above and in Negative evidence, and (b) byte-level pinning of the HTML/PDF snapshots.

### Negative evidence

1. **No risk-adjusted statistic exists for the rule.** `Sharpe` appears once in the whole pinned body — inside reference [10]. There is **no Sharpe, no drawdown, no volatility of the rule's return series, no annualization, no Calmar, no exposure**. A cumulative +1,125.6 bps over 240 trades cannot be compared with any benchmark on a risk basis from the source alone.
2. **Concentration.** *Our count:* fold 3 (Oct 29 – Nov 4) contributes **433.2 / 1,125.6 = 38.49%** of cumulative PnL, and the source separately states that "**October 29 alone** contributed 38.5% of profits". The two percentages are numerically identical, which means either the entire first fold week's profit came from its first session or the two statements are being conflated; **the pinned text prints no per-day breakdown**, so the true concentration is `underspecified`. Excluding fold 3 leaves **692.4 bps across the other four folds** (our arithmetic), i.e. the headline is heavily session-dependent either way.
3. **Sample size and window.** **36 trading days, one instrument, one 7-week window**, all folds inside a single volatility regime; the source itself lists this first among its limitations. Per-fold trade counts range from **12 to 92**.
4. **Regime restriction.** "VIX remained in the 14–22 range throughout; behavior during high-volatility regimes is unknown" (source-acknowledged). The mechanism is claimed to detect informed flow, yet the calmest tape of the period is the only tape tested.
5. **Net-vs-gross is unstated.** "net of" occurs 0 times. *Our count:* 240 × 0.57 bps = **136.8 bps = 12.15% of the printed PnL**, and average PnL per trade is only **4.69 bps** — so a misreading of cost treatment, or any cost above ~4.7 bps round trip, would erase the average trade. The printed PnL's cost status is `underspecified`, not confirmed.
6. **Cost model is a single fixed point.** No spread distribution, no impact, no participation, no capacity, no latency — despite the rule entering exactly when volume exceeds its 95th percentile, i.e. in the moments when spreads and depth are least "typical". The source concedes "immediate fills, fixed costs may not hold at scale".
7. **No baseline for the mechanism.** The paper never compares entropy against simpler volatility/flow predictors (realized vol, realized jump, volume z-score, Amihud illiquidity, quote-update intensity) and runs **no ablation** of the three entry conditions. The volume>95th-pct + 5–20 bps band alone may carry the entire effect → competing explanation, unresolved in source.
8. **The payoff component cannot be reconstructed.** The take-profit level, its precedence vs the stop, and the four perturbed parameters are not printed; the 12.2% payoff attribution therefore cannot be audited.
9. **The direction/win-rate identity.** The 108/240 count serves as both "directional accuracy" and "pooled win rate" (frontmatter contradiction 2); additionally the Table 1 caption asserts "win rate below 50% confirms absence of directional edge" while **fold 1's win rate is 71.9%**, so the caption does not hold fold-by-fold.
10. **Statistic provenance ambiguity.** `t = 12.41` is printed for both the 2.89× conditional factor and the 2.17 pooled ratio (frontmatter contradiction 1). Our own one-sample t over the five fold ratios gives **12.77**, and a one-sample t of the five fold PnLs against zero gives **3.79** — neither reproduces 12.41 exactly, so the printed t's construction is `underspecified`.
11. **Cross-record contrary evidence (different source, different market, stated as such).** The pre-registered study captured in `crypto-perpetual-order-flow-entropy-microstructure-taker-cost-falsification-2026-09-13` (yushingtoncity/market-entropy, pinned commit `06db3d1…`) found on Binance USDT perps that **trade-sign Shannon entropy adds ≈0 out-of-sample R² beyond plain order-flow variables** and that **taker costs exceed breakeven by an order of magnitude**. It tests a *different* entropy (sign entropy, directional target, crypto perps), so it does not refute this paper — but it is direct prior evidence that (a) entropy features can be redundant given flow features and (b) cost walls dominate on taker-executed intraday rules.
12. **Source-family / publication concern.** Preprint only, no journal-ref, no peer review, no code, no data. The same author's other captured preprints (arXiv:2511.12490, arXiv:2511.08571) are also unrefereed; **no independent group has replicated any of this author's claims**, and all headline numbers are self-reported.
13. **Selection/look-ahead on the window.** No justification is given for the Oct–Nov 2025 window beyond data availability, and the 5th/95th percentile thresholds are estimated on the training slice of the same 7 weeks — the strongest day (Oct 29) falls *inside* the test folds, which is correct protocol, but with 5 folds over 7 weeks there is no true untouched holdout beyond Nov 18.
14. **No inference on the trading result itself.** Beyond the random-entry z = 4.9, there is no confidence interval, no bootstrap, no drawdown distribution and no multiple-testing control applied to the **+1,125.6 bps** headline; the Bonferroni family (14 tests) is never enumerated.

## Falsification plan

Every threshold below is **`research-defined`** and every operational choice not printed in the source is **`research-proposed`**. Nothing here is a source claim. Data for all tests: point-in-time second bars of SPY (and, for F2/F7, the named extra instruments), thresholds fitted on training windows only, next-second execution assumed (`research-proposed`).

- **F1 — Independent data re-run.** Rebuild the entropy series from a *different* licensed tick feed (different vendor/consolidator from any used in the source) for ≥ 60 trading days with ≥ 2,000 signals. **Pass:** pooled magnitude ratio (mean |5-min return| conditioned on `H < p5` ÷ unconditional) ≥ **1.5** with a Welch **t ≥ 2.0**, and the ratio > 1.0 in ≥ 4 of 5 folds. **Fail:** ratio < 1.2 or t < 2.0 → reject the magnitude claim.
- **F2 — Multi-instrument / longer window.** Repeat on SPY + QQQ + IWM over ≥ 6 months spanning ≥ 2 volatility regimes (one with VIX ≥ 25). **Pass:** magnitude ratio > 1.0 in ≥ 2 of 3 instruments and in both regimes. **Fail:** effect present in only one instrument or only in the calm regime → mechanism claim (`informed-flow state`) is rejected as SPY/2025-specific.
- **F3 — Cost ladder and gross/net audit.** Re-run the printed rule at round-trip costs of **0, 0.57, 1, 2, 5, 10 bps**, and first *state explicitly* whether the source-style figure is gross or net. **Pass:** cumulative PnL > 0 at **2 bps** round trip and per-trade median PnL > 0 at **0.57 bps**. **Fail:** PnL ≤ 0 at 2 bps (≈ 0.5 bps above the source's own assumed SPY spread) → the rule's economics are an artifact of the cost assumption.
- **F4 — Entropy ablation (mechanism-critical).** Compare (a) full rule, (b) volume > 95th pct + 5–20 bps band **without** the entropy gate, (c) entropy gate alone, (d) volume-only, (e) random entry conditioned on the same two filters. **Fail the entropy mechanism claim** if (b) retains ≥ **80%** of (a)'s magnitude-ratio edge, or if (a) is not above the 95th percentile of (e) over 10,000 conditioned trials. This is the single most important test: the source runs no ablation.
- **F5 — Competing-predictor horse race.** Predict next-5-minute |return| from entropy alone vs. from {realized 5-min vol, 1-min realized jump, volume z-score, quote/trade count, Amihud |r|/volume} alone and jointly. **Fail** if entropy adds **< 10%** incremental out-of-sample R² over the best simple predictor, or if its standardized coefficient falls below **|t| = 2.0** in the joint model.
- **F6 — Concentration / leave-one-day-out.** Recompute cumulative PnL dropping each trading day in turn. **Fail** if the top day contributes **> 30%** of PnL (the source's own printed figure is 38.5%) *and* the remaining days' mean PnL is not > 0 at t ≥ 2.0, or if removing any single day flips the sign.
- **F7 — Regime split.** Split the sample at VIX = 22 (or into terciles by realized vol). **Fail** if the magnitude ratio < **1.0** in the high-volatility subsample — the source explicitly does not know this case, and a state variable that only works in calm tape cannot be a risk-state instrument.
- **F8 — Strengthened placebo.** Random-entry placebo **conditioned on the same entry filters** (same volume/return bands, same holds, same exits, shuffled only in *time within session*), 10,000 draws. **Fail** if the observed PnL is not above the **95th percentile** of the conditioned null. (The source's placebo matched payoff structure but does not state that it matched the entry filters → `research-proposed` tightening.)
- **F9 — Capacity / participation.** Cap each entry at **5%, 10%, 20%** of the trailing 1-second volume and add a depth-aware spread (top-of-book + 1 tick). **Fail** if PnL at **10% participation** falls below **50%** of the headline, or if the rule cannot be executed at all in the seconds it fires (volume-surge entries are exactly the congested ones).
- **F10 — Cost-vs-magnitude break-even.** Compute the round-trip cost at which cumulative PnL = 0 given the printed trade-level distribution. **Fail** if break-even cost < **2 bps** (i.e. the strategy dies on a spread move that SPY routinely shows), and record the number as the strategy's true margin of safety.
- **F11 — Multiplicity.** Enumerate the full family of reported tests (magnitude, direction, 5 folds, 3 placebos, 20 perturbations ⇒ ≥ 31 looks) and apply Benjamini–Hochberg at **q < 0.10** (and re-apply the source's own Bonferroni to its stated 14). **Fail** if the headline conditioning result does not survive.
- **F12 — Frozen forward window.** Freeze every parameter (percentiles, band, stop, take-profit, precedence rule declared `research-proposed`) on data through a fixed date, then run ≥ 3 untouched months. **Pass:** pooled magnitude ratio ≥ 1.5 at t ≥ 2.0 **and** positive cumulative PnL net of 2 bps. **Fail** on either → the hypothesis is weakened and the record is updated, not retuned.
- **F13 — Direction/win-rate disambiguation (repairs frontmatter contradiction 2).** Compute *directional accuracy* (sign of the 5-minute return vs. the entered side) and *win rate* (trade ended profitable) as two separate series on the same 240-trade set. **Fail the source's Theorem-2 claim** if out-of-sample directional accuracy is ≥ **52%** with |z| ≥ 1.96 (direction exists where the theory says none). **Fail the printed Figure-2/Table-1 numbers** if the separately computed counts do not reproduce 108/240 for both. Either outcome materially changes the interpretation of Figure 2.

**Action on failure:** F1/F2/F4/F5 failures kill the *mechanism* claim (record → negative evidence, no implementation); F3/F9/F10 failures kill the *economics* (cost wall); F12 failure retires the signal without retuning. None of these tests has been run.

## Crypto portability

**`unproven`.** The pinned source contains **zero** crypto content (`crypto`, `Bitcoin`, `funding`, `perpetual` all absent from the body) and never analyses anything but SPY. The mechanism is a *portable-in-principle, untested-in-practice* hypothesis:

- **What ports cleanly.** The entropy state needs only a signed price series and volume at ~1-second resolution, both available on any major venue; the 15-state chain, 120 s window and 5-minute outcome horizon are market-agnostic; the permutation-symmetry argument is pure mathematics. A crypto implementation would therefore be an *adapted port of a traditional-market microstructure hypothesis*, not crypto empirical evidence.
- **What breaks.** (1) **Cost scale:** the source's whole margin rests on a **0.57 bps** round trip; the cross-record study captured in this repository (`crypto-perpetual-order-flow-entropy-microstructure-taker-cost-falsification-2026-09-13`) reports, as its own source-reported figure, a lowest Binance retail taker tier of **4.0–5.0 bps** with institutional crossing above 2.0 bps — i.e. fees alone exceed this paper's *entire* assumed cost by roughly an order of magnitude, and the entry rule is inherently taker-side because it fires on volume bursts. (2) **24/7 clock:** percentile thresholds fitted on a 10-day window span weekend/Asia lulls and differ structurally from a 6.5-hour session; second bars exist only where trades print. (3) **Funding/mark price:** not applicable to a seconds-hold trade on spot, but on perps the funding cycle, mark/index price and auto-deleveraging introduce events the source never modelled. (4) **Venue fragmentation:** SPY's consolidated tape does not exist; volume quintiles computed on one venue are not the market's. (5) **Short leg:** shorting crypto perps is cheap but liquidation/funding/borrow semantics differ entirely from an ETF locate. (6) **Data quality:** wash trading and spoofed volume distort the volume-quintile state directly — a known risk documented in `crypto-microstructure-complexity-measures-wash-trading-filter-2026-09-01`.
- **Verdict:** label `unproven`. Before the mechanism question is even reachable in crypto, a port must show a break-even round-trip cost of at least **5 bps**, well above the ≥ 2 bps break-even that F10 demands for the equity case.

## Limitations

- `not independently reproduced` — every performance number here is a third-party claim from an unrefereed preprint; the Scout ran no code and has no tick data.
- `underspecified`: take-profit value, exit precedence, volume-percentile window, position sizing, session/timezone, gross-vs-net status of the printed PnL, the four perturbed parameters, and the 14-test Bonferroni family.
- `data gap`: market impact, capacity, participation, latency, borrow/short cost, leverage/margin, time-varying spread, partial fills, benchmark (buy-and-hold) return, vendor identity, code, raw data.
- **Sample risk:** 36 trading days, one instrument, one volatility regime (VIX 14–22), 240 trades total, one fold contributing ~38.5% of PnL. No evidence exists for high-vol regimes, other ETFs, other asset classes, other decades, or any crypto market.
- **Identification risk:** no ablation and no competing-predictor benchmark, so the incremental content of the entropy gate versus its own volume/prior-move filters is unknown; the strategy may be a volume-spike rule wearing an entropy label.
- **Reconstruction risk:** without the take-profit level and the precedence rule, the printed PnL is not reproducible from the paper; without the licensed vendor data, the entropy series itself is not reproducible at all (`code available upon request` only).
- **Publication-bias / source-quality risk:** single-author preprint, no peer review, no journal-ref, no independent replication of any paper by this author; headline statistics carry two internal ambiguities declared in `contradictions`.
- **Statistic risk:** one t-statistic is reused for two different ratios, and one 108/240 count is reused for two different metrics; both are flagged rather than repaired.
- **Interpretation risk:** `confidence: medium` reflects these ambiguities and the absence of any independently verified number — it is *not* a view on profitability and not authorization to trade.

## Implementation status

`implementation_status: not-implemented`. Nothing has been implemented in our research stack: no entropy series, no signal generator, no backtest, no NautilusTrader or Qlib run, no Paper/Testnet/Live. The Scout's only executed work was primary-source pinning, a full text read, repo-wide dedup scans, and arithmetic consistency checks on printed figures (all labeled *our count*). This record does not modify any engine and does not create a strategy family.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this record in the staging repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading, testnet, or live trading. Any later adoption or implementation decision is a separate, explicit, reviewed step based on this record plus current sources.

## Related Wiki records

Verified Wiki Brain pages found by `kb_search` this run (queries `order-flow entropy magnitude intraday volatility` → 3 hits; `intraday volatility timing absolute return prediction SPY` → 2 hits; `market microstructure informed trading volatility prediction` → 8 hits; `price volume binary entropy divergence Bernoulli`, `entropy regime gate intraday momentum stop loss`, `permutation entropy structure rank regime TradingView` → 0 hits). Only mechanism-adjacent verified pages are linked; nothing is fabricated:

- [[quant/crypto-perpetual-order-flow-entropy-microstructure-taker-cost-falsification-2026-09-13]] — **four-axis distinction:** different source identity (GitHub `yushingtoncity/market-entropy` @ `06db3d1…` vs arXiv:2512.15720v1); different mechanism (directional trade-sign Shannon entropy as a *refuted* alpha, plus a taker-cost-wall argument, vs. sign-invariant transition entropy as a *magnitude/volatility state*); different signal construction (trade-sign entropy ablation vs. 15-state price-sign × volume-quintile Markov entropy with a two-filter entry gate); different universe (Binance USDT perps BTC/ETH vs. SPY), different horizon (1–60 s directional vs. ≤300 s magnitude), different data dependency (Tardis tick archive vs. licensed consolidated equities ticks). Used here only as negative evidence, never as the same claim.
- [[quant/market-regime-routed-specialist-gbt-asymmetric-hysteresis-2026-09-12]] — adjacent only on "volatility-state routing"; different source, mechanism (gradient-boosted regime routing + dual-threshold hysteresis + volatility targeting), universe and horizon.

Repo records with **no Wiki page found** (referenced by filename only, no wiki link asserted): `tradingview-price-volume-binary-entropy-divergence-2026-09-24` (Bernoulli price-vs-volume entropy *divergence*, directional, TradingView — different source, signal construction and target), `tradingview-permutation-entropy-structure-rank-regime-2026-09-24` (permutation-entropy regime ranking — different construction), `drift-regime-gated-cross-sectional-value-reversal-2026-09-05` and `forecast-to-fill-gold-futures-friction-adjusted-kelly-alpha-2026-09-02` (**same author, different manuscripts**: arXiv:2511.12490 and arXiv:2511.08571, distinct mechanisms and universes), `crypto-microstructure-complexity-measures-wash-trading-filter-2026-09-01` (wash-trading caveat cited above).

## Sources

1. Mainak Singha, *"Hidden Order in Trades Predicts the Size of Price Moves"*, **arXiv:2512.15720v1 [q-fin.TR]**, submitted Tue, 2 Dec 2025 23:20:46 UTC; manuscript dated November 2025; sole version (v2 → HTTP 404, checked 2026-09-26); license CC BY 4.0; no journal-ref; DataCite DOI `10.48550/arXiv.2512.15720`. Stable URL: https://arxiv.org/abs/2512.15720 — read in full 2026-09-26.
2. Pinned v1 HTML: https://arxiv.org/html/2512.15720v1 — 67,336 bytes, SHA-256 `9c23681d61d79ec63ef4c246f0992e57d04e3250cca8ffb5f59ecc136ca806fd` (retrieved 2026-09-25; re-fetched and re-hashed 2026-09-26, identical).
3. Pinned v1 PDF: https://arxiv.org/pdf/2512.15720v1 — 898,319 bytes, SHA-256 `bdd3689374f22596d13cd7bf384af95fbea524451ddcf015653b90ecd1acc85d` (retrieved 2026-09-25; re-downloaded and re-hashed 2026-09-26, identical).
4. Cross-record negative evidence (distinct source, cited as such): `crypto-perpetual-order-flow-entropy-microstructure-taker-cost-falsification-2026-09-13`, GitHub `yushingtoncity/market-entropy` at pinned commit `06db3d1c6d5eb2d29d4bea94b0af704a80c8f557`.

No other source was used. No performance figure in this record comes from a secondary summary.





