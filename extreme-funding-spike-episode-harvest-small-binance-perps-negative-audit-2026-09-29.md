---
schema: strategy-research-record-v1
title: "Extreme Funding Spike Harvest on Small Binance USDT Perpetuals: a Pre-Declared Spot-Hedged Episode Rule, Reproduced Exactly and Negative Since 2023"
created: 2026-09-29
updated: 2026-09-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - funding-rate
  - delta-neutral
  - event-episode
  - capacity-constrained
  - negative-result
  - binance
status: research-only
confidence: medium
source_as_of: 2026-09-22
sources:
  - "https://github.com/stooq1/strategy-graveyard at tree 5d0341c665f6030acc3c756664427e712b8f5c39 (commit 2026-09-22T19:00:11Z, message 'README: MOEX block first, Binance 451 note, N=30 figures, collector snapshot'), files: README.md, funding_scan.py, posts/2026-09-funding-spikes.en.md, posts/2026-09-funding-spikes.md, results/funding_scan_by_year.csv, results/funding_scan_episodes.csv, results/README.md, docs/FINDINGS.md, docs/REVIEW.md, fetch_daily.py, LICENSE"
  - "https://dev.to/stooq1/i-tested-harvest-extreme-funding-on-small-perps-on-all-658-binance-perpetuals-it-died-in-2023-46mh (mirror of the EN write-up, linked from README.md at the pinned tree; not used as an independent source)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "README.md results row versus the write-up's own optimistic-entry table: README states the extreme-funding spike rule is 'negative even with optimistic entry at any threshold' in 2023, 2025 and 2026, but posts/2026-09-funding-spikes.en.md prints 2025 as +4.6 (% notional) at 200%/3-payments and +5.3 at 300%/2-payments, and our independent re-computation reproduces +4.6 and +5.3 exactly, so 2025 is positive at two of the three printed thresholds; 2023 has no episodes at all at the 200%/3 and 300%/2 settings (sum 0.0, neither negative nor positive)."
  - "Write-up 'From 2022 through 2026 the total is -$2,136 on the upper bound and -$515 in the simulation' versus its own by-year table: summing the printed by-year cells 2022-2026 inclusively gives +$8,357 upper bound (2023 -$513 + 2024 +$10,493 + 2025 -$773 + 2026 -$850) and -$231 simulation; the printed -$2,136 / -$515 only reconcile when 2024 is excluded (research-computed -$2,135 and -$515), so the stated window and the stated totals are inconsistent."
  - "Write-up 'January 2021 alone, summed across all hedgeable perps, would have paid more than $100,000 per $10,000-per-episode' versus our independent re-computation: episodes starting in 2021-01 are 157 with sum net +154.47% of notional = $15,447 at $10k-per-episode (gross +232.97%); the ~$100,103 figure is the FULL-YEAR 2021 take-all upper bound printed in results/funding_scan_by_year.csv (100102.6853), so as written the month-level claim contradicts the source's own yearly cell."
  - "Write-up 'The single-payment variant is shown too; it is worse everywhere' (RU: 'вариант с входом по первой выплате: он хуже везде'): the variant's numbers are printed nowhere in either post (data gap), and our re-computation at confirm=1 shows it is worse on every year and on the grand total under the $10k/3-slot simulation (total -$8,648 versus +$3,116) and worse on the grand summed net (982.5% versus 1,150.8%), but BETTER on the 2021 summed net (+1,158.1% versus +1,001.0% over 1,244 versus 615 episodes), so 'everywhere' only holds under the simulation reading."
  - "README control sentence 'the 16 majors alone ... episodes ... exist only in 2020-2021 and in a short burst in 2024 ... The $10,000 simulation on majors: +$364 per year on average, all of it from 2021' cannot be reconciled with a single confirm setting: with the repository's own 16-symbol constant (fetch_daily.py CRYPTO_SYMBOLS: BTC ETH BNB XRP ADA SOL DOGE LTC LINK DOT AVAX ATOM BCH ETC TRX XLM, which matches the printed prefix and reproduces the printed average) at confirm=3 we get episodes only in 2020 (66) and 2021 (136), simulation $339 + $2,215 = $2,554 over 7 years = $364.9/yr (printed +$364) but zero 2024 episodes and $339 of the total coming from 2020, while at confirm=1 we get the printed year pattern (2020: 234, 2021: 250, 2024: 22, none in 2022-2023/2025-2026) but only $250.6/yr; additionally the 16-symbol list itself is never printed in the source (inferred from fetch_daily.py)."
---

# Extreme Funding Spike Harvest on Small Binance USDT Perpetuals: a Pre-Declared Spot-Hedged Episode Rule, Reproduced Exactly and Negative Since 2023

## Provenance

- **Primary source identity:** public GitHub repository `https://github.com/stooq1/strategy-graveyard`, pinned at **full commit SHA `5d0341c665f6030acc3c756664427e712b8f5c39`** (commit author `stooq1 <331291698+stooq1@users.noreply.github.com>`, commit date **2026-09-22T19:00:11Z**, message `README: MOEX block first, Binance 451 note, N=30 figures, collector snapshot`). `git ls-remote ... HEAD` re-confirmed on 2026-09-29 that this SHA is still the repository's `main` HEAD.
- **Repository metadata read from the GitHub API on 2026-09-29:** created `2026-09-20T11:02:19Z`, last push `2026-09-22T19:00:11Z`, default branch `main`, license **MIT**, language Python, 0 stars, 0 forks, 0 open issues, not archived, description "Honest tests of retail trading edges on crypto perps and MOEX futures — order book, conductors, trend, funding — with the collector that produced them".
- **Authorship / author list exactly as the source states:** README.md §About: "Independent project by [@stooq1](https://github.com/stooq1), June–September 2026"; **sole human author**, no co-authors, no institutional affiliation, no ORCID printed. The same section discloses: "Large parts of the code and the journal were written with AI assistants (DeepSeek, Claude); every number in the tables was produced by the scripts in this repository and can be regenerated." Contact channel: Telegram `t.me/strategy_graveyard`.
- **Version / date / status:** four-month project window **June–September 2026** (README §About); **no DOI, no preprint identifier, no journal reference, no peer-review statement anywhere in the pinned tree** — publication status is therefore **not stated in source** beyond "public GitHub repository plus two Markdown write-ups (EN/RU) mirrored on dev.to". Code and text are MIT-licensed (`LICENSE` blob `745ea336ba263f51d9eceb4a3810686b5341917c`).
- **Primary-source files opened and checksum-verified at the pinned tree on 2026-09-29** (each file fetched from the pinned-SHA raw URL, then `git hash-object` compared with the tree entry — all 11 matched exactly):

  | file | bytes | git blob SHA (tree == our copy) |
  |---|---|---|
  | `README.md` | 14555 | `957a97a2d4e79dda2e41f9f06888d01565d8d0ac` |
  | `docs/FINDINGS.md` | 29811 | `f638d24af4feaa8c4f3afc0da893c848d41ce823` |
  | `docs/REVIEW.md` | 76427 | `ee44cae9683ba893879ff3b34115334d9b47e134` |
  | `funding_scan.py` | 14934 | `e972f42cf6ba4bf3a007a5e09742957983c8117e` |
  | `results/funding_scan_by_year.csv` | 646 | `8deefb8096410262851a6b5fac0d91e1fd84507c` |
  | `results/funding_scan_episodes.csv` | 159152 | `077a8db815a7769639c0d14c2cacd467adc1f2b7` |
  | `posts/2026-09-funding-spikes.en.md` | 7873 | `d3147dc5dfc4fb1b64ac5f2c2689f5ada5e96730` |
  | `posts/2026-09-funding-spikes.md` (RU) | 12241 | `024b248d71094286539d08d171907301561c7673` |
  | `results/README.md` | 2724 | `ef11ed632e132639199db32cb1d12cef22874f73` |
  | `fetch_daily.py` | 24344 | `ac34cf370628ee69737ca364e481e01d3915c59b` |
  | `LICENSE` | 1063 | `745ea336ba263f51d9eceb4a3810686b5341917c` |

  The whole tree was enumerated through `GET /repos/stooq1/strategy-graveyard/git/trees/5d0341c...?recursive=1` (`truncated: false`, 113 blobs and 12 trees), so file selection is complete and not cherry-picked.
- **Sample period as stated by the source:** full Binance USDT-M funding history **2019-09-10 to 2026-09-18** (posts EN §"What exactly was tested" → Data; RU post identical). Our independent fetch used window **2019-09-01 → 2026-09-18 UTC**, i.e. a superset of the source's stated start.
- **Universe as stated by the source:** current `fapi/v1/exchangeInfo` USDT perpetuals — **658 symbols, of which 364 have a USDT spot pair on the same venue** and only those are hedgeable/eligible (README row "658 perps, 364 hedgeable"; RU post line 3 identical).
- **Traceability gap (recorded, not repaired):** README.md line 29 claims "Full numbers, tables and the reasoning behind every closure are in the journal (docs/REVIEW.md, sections 4–6.11; docs/FINDINGS.md, sections 3–5)". Case-insensitive scans of both journal files at the pinned tree return **zero** occurrences of `IOTA`, `658`, `1125`, `кэрри`, `фандинг` (the only `funding` hit in FINDINGS.md is line 60 about the live collector), so **the journal carries no funding-spike section**; the funding row's primary documentation is the post, `funding_scan.py` and `results/`.
- **Secondary rendering:** the same EN write-up is mirrored at `https://dev.to/stooq1/i-tested-harvest-extreme-funding-on-small-perps-on-all-658-binance-perpetuals-it-died-in-2023-46mh` (linked from README.md §Write-ups). We read `devto.html` only to confirm the mirrored text matches the pinned post; **no claim in this record is sourced from the mirror alone**.
- **Data as-of:** source funding sample ends **2026-09-18**; source universe snapshot is whatever `exchangeInfo` returned on/around 2026-09-18; our independent universe snapshot is **2026-09-29**.
- **Pre-write source-identity dedup (hidden-inclusive, whole checkout):** `rg -uuu -i` over the entire repository working tree including `.git`, `.mimo-worktrees`, `.agents`, `.hermes`, `coverage_manifest.csv` (1,088,787 bytes) for `stooq1`, `strategy-graveyard`, `5d0341c665f6`, `funding_scan`, `funding_spikes`, `funding spike`, `funding-spike`, `Honest tests of retail`, `MOEX`, `graveyard|stooq|658 perpetual|1,125 episodes|harvest extreme funding|IOTA +15.3` → **zero source-identity hits**; the only two `graveyard` hits are unrelated (a Solana token-mint graveyard benchmark and an `elraffaello123-art/quant-research` killed-edges graveyard). Positive control `novy-marx` returned 25 files in the same session, so the search demonstrably reaches existing records. `git log --oneline -20` was used as a convenience glance only, never as dedup. Re-run after `git pull origin main` ("Already up to date") returned only this draft.

## Economic mechanism

### Source-reported

The author's stated rationale (README §Results row "Extreme-funding spike arbitrage on small perps"; posts EN §"The promise" and §"Why it died"):

- A hyped small perpetual trades at a **premium to spot**; leveraged longs pay shorts 0.5–2% per 8 hours, i.e. hundreds to thousands of percent annualized. **Short the perp, buy equal-size spot**, price risk is hedged, sit and collect the funding payments.
- **Funds cannot use this edge because the small perp has no capacity** — "even for a million dollars" — while "$10,000 has plenty", making this, in the author's words, "the one class of edge where small capital is an advantage".
- The author's own closure narrative: the phenomenon was "real, large and broad in 2021", returned "for a few months in 2024", and "has been negative under every reading of the data since", for a **structural** reason: from 2023 Binance moved volatile contracts from 8-hour to 4-hour funding, so the spike "collapses within one or two payments after it becomes visible" and "somebody harvests it faster than it can be confirmed to exist — ... bots for which the predicted next funding rate is a signal measured in seconds". The author adds: "structural causes do not revert on their own."

### Research interpretation

- **Mechanism class: crowded-positioning / funding-pressure carry with a capacity niche, i.e. a limits-to-arbitrage rent rather than a forecasting signal.** The payoff is the realized funding payment stream itself; the delta-neutral construction removes directional price risk so the trade is a bet that (a) extreme funding persists long enough to cover two taker round trips, and (b) institutional capital does not flow in because the notional is too small.
- **Component roles (hybrid):** *Regime/time filter*: none (calendar-free, payment-driven). *Entry trigger*: three consecutive funding payments each annualizing ≥ 100% using the actual payment interval. *Position*: short perp + long spot, equal notional (hedge, not alpha). *Exit trigger*: first payment annualizing < 30%. *Cost floor*: flat 50 bp of notional per episode. *Capacity layer*: $10k capital split into 3 equal slots, episodes taken in time order, skipped when all slots are busy.
- **Why it could have stopped working (falsifiable form):** as the funding grid shortens (8h → 4h) and market-making/arb bots shorten their reaction time, the *duration* of an extreme-funding episode falls below the confirmation latency of the rule (3 payments), so the rule systematically enters after the profitable tail has been consumed. This predicts: shrinking episode durations over calendar time, entry prices/timing that miss the payment stream, and non-positive post-2023 net after costs even at higher entry thresholds — all observable in the funding series alone.
- **What is NOT claimed:** no price-direction forecast, no basis model (the source explicitly ignores basis and argues doing so is conservative), and no claim that the hedge is frictionless (spot borrow/liquidity, short-margin and delisting risk are all named by the source as unmodelled).
- **Do not assume every component contributes alpha:** the entry threshold, confirmation count and exit threshold are the only candidate alpha-bearing choices; the hedge, slot cap and cost floor are risk/execution choices, and ablation is required (see Falsification).

## Signal

Everything in this section is **source-reported** unless explicitly labeled `research-proposed`.

- **Signal formation timestamp:** evaluated only at actual funding payment timestamps (Binance `fundingTime`, 8h, 4h or 1h grid depending on contract and era). Annualization for each payment: `ann = rate * 8760 / hours_to_previous_payment * 100`, with `hours` clamped to `[1, 8]` and the first payment of each series defaulted to 8 (`funding_scan.py::load_payments`, lines 100–109). There is **no bar sampling, no lookahead price data, no publication lag** — the funding rate for the *next* interval is visible in advance on Binance, which the source names as the reason its "enter after the payment" rule is a *conservative* approximation of what is executable.
- **Universe filter:** only perpetuals whose base asset has a `TRADING` USDT spot pair on Binance (`funding_scan.py::list_symbols`); `--all-symbols` exists but is not used for the published numbers.
- **Entry (`funding_scan.py::episodes`, confirm = 3):** walk the payment series; enter at payment index `i` when the **three consecutive payments `i-2, i-1, i` all have `ann ≥ 100` (% annualized)**. Scanning resumes at `j+1` after an episode closes (episodes are non-overlapping per symbol).
- **Position:** short perp + long spot of equal size; every subsequent payment with positive rate is received, every negative rate is paid (`gross = Σ rate` over payments `i+1 … j`).
- **Exit:** at the first payment `j > i` with `ann < 30` (% annualized); that payment is included in `gross`. If the series ends first, exit at the last payment (`j = min(j, n-1)`), and an episode that would receive zero payments is dropped (`if n_pay == 0: break`).
- **Cost:** flat **50 bp of notional per episode** subtracted once (`net = gross − 0.005`).
- **Year attribution:** the calendar year of the entry payment timestamp.
- **Parameters (all source-fixed, none tuned by us):** `--enter 100`, `--exit 30`, `--cost 50` (bp), `--confirm 3`, `--capital 10000`, `--slots 3`. Note the argparse **default** is `--confirm 1`; the published headline numbers are produced with `--confirm 3`, exactly as the README reproduce command `python funding_scan.py --fetch --scan --confirm 3` states.
- **Capital-constrained simulation:** $10,000 total, `size = 10000/3 = $3,333.33` per position, episodes sorted by `(start, -ann_entry)`, an episode is skipped when 3 positions are already open at its start, and slot release uses the episode end time (`funding_scan.py::simulate`).
- **Optimistic-entry bound (source, non-executable upper bound):** entry "on the *predicted* rate, i.e. one payment earlier than my rule allows, with the entry payment credited". Our reconstruction: identical detection, but the credited payment stream starts at index `i` instead of `i+1` (i.e. the confirming payment itself is collected). This interpretation reproduces **all 12 printed cells** (see Evidence).
- **Holding period:** from entry payment to exit payment; observed median 2.7 days overall, but 0.5–0.67 days in 2025–2026 (source-reported, reproduced).
- **Re-entry:** allowed only after the current episode closes; no overlapping episodes per symbol.
- **Position sizing logic:** fixed equal notional per slot; no vol targeting, no compounding, no leverage choice anywhere in the rule.
- **Multi-timeframe dependencies:** none.
- **Specified / underspecified:** the episode rule is **fully specified and reproducible** (we reproduced it bit-for-bit). **Underspecified:** the "16 majors" control list (never printed), the "single-payment variant" table (claimed to be "shown" but absent from both posts), and any venue-specific fee schedule behind the flat 50 bp.

## Required data

- **Instrument:** Binance USDT-M perpetual contracts (`contractType = PERPETUAL`, `quoteAsset = USDT`) plus the matching Binance USDT **spot** pairs for the hedge leg.
- **Universe:** live `exchangeInfo` USDT perps — **658 symbols at the source snapshot, 364 hedgeable**; our 2026-09-29 snapshot: **658 perps, 367 hedgeable** (3-symbol drift between 2026-09-18 and 2026-09-29), of which **365 returned funding history** in our run (2 non-ASCII symbols, `币安人生USDT` and `牛来USDT`, failed URL encoding in our client and were skipped).
- **Venue:** Binance only (`fapi.binance.com` for funding, `api.binance.com` for spot `exchangeInfo`).
- **Market type:** perpetual + spot (delta-neutral pair). No futures/options data.
- **Timeframe:** funding payment events (8h/4h/1h grid), not bars. No OHLCV is used by the published rule.
- **Fields:** `fundingTime`, `fundingRate` from `GET /fapi/v1/fundingRate` (full history, paginated at `limit=1000`); `onboardDate`, `status`, `baseAsset`, `quoteAsset`, `contractType` from `exchangeInfo`.
- **Point-in-time:** **the universe is a live snapshot, not point-in-time.** Delisted perps are absent by construction (the source says so explicitly: "exchangeInfo only lists live contracts. Delisted perps ... are not in the sample, so reality is worse than the numbers below, not better"). `onboardDate` is used only for the separate new-listing check.
- **Timestamp:** milliseconds since epoch, exchange clock, UTC; payment interval derived by consecutive-timestamp differences clamped to `[1, 8]` hours.
- **Missing-data:** our run: 2 of 367 hedgeable symbols failed to fetch (non-ASCII symbol encoding) and were skipped; the resulting episode set still equals the source's 1,125 exactly, so the two failures carried no episodes. No imputation anywhere (`funding_scan.py` never fills values; only the first interval defaults to 8h).
- **Funding/fee/spread needs:** funding **is** the return stream (observed, historical). Maker/taker fees and slippage are **not observed per venue** — they are collapsed into the flat 50 bp/episode figure. Spread, market impact, borrow, margin financing and liquidation are **not modelled** (see Execution assumptions).

## Execution assumptions

Cost determination was made from a Methods-level read of `funding_scan.py` (docstring lines 7–31 plus `episodes()`/`simulate()`/`scan()`), posts EN §"What exactly was tested" and §"Results", the final italic caveat paragraph of the post, and `results/README.md`'s column definitions — not from the abstract or README table alone.

- **Signal-to-order timing:** entry is instantaneous at the confirming payment's timestamp; no latency is modelled. The source notes the next funding rate is knowable in advance, so its rule is a conservative approximation.
- **Order type / fill model:** **not stated in source** for either leg — the rule prices two taker round trips but never states order type, partial fills, or queue behaviour (`data gap`).
- **Fees + slippage:** **source-reported flat 50 bp of notional per episode**, described as "two taker round trips (spot 10 bp + perp 5 bp per side) plus a slippage allowance for illiquid names". There is **no per-venue fee schedule, no tier ladder, no maker option, no volume-based discount** in the pinned tree.
- **Spread / impact / participation / capacity:** **not modelled at all** (`data gap`, never treat as zero). Capacity enters only implicitly through the fixed $3,333 slot size and the narrative claim that funds cannot fit.
- **Funding on the hedge legs, margin, leverage, borrow:** no leverage or margin requirement is specified; short-leg margin cost during rallies, spot borrow (not needed for a long spot leg) and liquidation are **not modelled** — the source lists "margin on the short leg during vertical rallies" among unmodelled items that make reality worse.
- **Basis:** explicitly **ignored**, with the source's reasoning recorded as source-reported: when funding is extreme the perp trades at a premium, so the short is opened rich and closed after the premium collapses — "a gain, not a loss". The source also lists "basis moving against the position when exiting before the premium collapses" as unmodelled and adverse, then states the favourable side "is smaller than the first".
- **Hedge legs / fills:** closing the spot leg in a thin book and delisting risk while an episode is open are named by the source as unmodelled and adverse.
- **Latency, partial fills, failure handling:** `data gap`.
- **Our own execution assumptions:** none added. This record introduces **no** Scout-chosen entry/exit/fee/sizing rule; every operational number above is source-reported. Only the falsification cutoffs in the next section are `research-defined`.

## Evidence

### Source-reported

All figures below are third-party claims from the pinned tree, all **not** independently verified beyond the reproduction described in the next subsection; every one traces to a specific file/section.

- **Universe and sample (posts EN §"What exactly was tested"; identical in RU):** 658 USDT perps, 364 hedgeable, full funding history 2019-09-10 → 2026-09-18, with the explicit survivorship caveat about delisted contracts.
- **Headline aggregates (posts EN §"Results", paragraph above the by-year table):** 1,125 episodes total, ~160 per year, **median duration 2.7 days**, **58% profitable after costs**, **median episode +0.20% of notional**, **mean +1.02%**, **top-5 episodes only 6% of the total**.
- **By-year table (posts EN §"Results"; identical numbers in `results/funding_scan_by_year.csv`, whose Russian column names are defined in `results/README.md`):**

  | year | episodes | profitable | median net % | sum net % | take-all at $10k (USD) | sim $10k / 3 slots (USD) |
  |---|---|---|---|---|---|---|
  | 2020 | 170 | 52% | +0.1 | +66 | +6,623 | +597 |
  | 2021 | 615 | 63% | +0.6 | **+1,001** | +100,103 | +2,750 |
  | 2022 | 0 | — | — | — | 0 | 0 |
  | 2023 | 37 | 22% | −0.2 | −5 | −513 | +26 |
  | 2024 | 233 | 68% | +0.3 | +105 | +10,493 | +284 |
  | 2025 | 43 | 21% | −0.3 | −8 | −773 | −258 |
  | 2026 (to Sep 18) | 27 | **4%** | −0.4 | −9 | −850 | −283 |

- **Named 2021 winners (posts EN §"Results"):** IOTA +15.3% of notional in 20 days ("61 consecutive payments at 104% annualized and above"), TRB +14.9%, ANKR +14.0%, EGLD +12.7%, YFI +12.6%, 1INCH +12.0%, all in Jan–Feb and Mar–Apr 2021; plus the January-2021 "$100,000 per $10,000" sentence (contradicted below).
- **Totals sentence (posts EN §"Results"):** "From 2022 through 2026 the total is −$2,136 on the upper bound and −$515 in the simulation. The last twelve months: −$293." (both under the label ambiguity described below).
- **Why-it-died diagnostics (posts EN §"Why it died"):** median payment interval inside episodes 8h in 2020–2021 vs 4h from 2023; median episode duration 3.0 days in 2021 and 2024, 0.67 days in 2025, 0.5 days in 2026; new-listing check over 361 listings giving **−53% annualized average** funding in the first 14 days, median +5%, above 100% in 5% of listings.
- **Optimistic-entry bound table (posts EN §"Maybe the rule is just slow?"; sum of net across all episodes of the year, % of notional):**

  | entry threshold | 2021 | 2024 | 2025 | 2026 |
  |---|---|---|---|---|
  | 100% annualized, 3 payments | +1,108 | +123 | −4.0 | −6.6 |
  | 200% annualized, 3 payments | +663 | +11 | +4.6 | −1.4 |
  | 300% annualized, 2 payments | +351 | +3.5 | +5.3 | −2.2 |

- **16-majors control (posts EN §"Maybe the rule is just slow?", final paragraph):** episodes ≥100% exist "only in 2020–2021 and in a short burst in 2024", none in 2022–2023 and 2025–2026; "$10,000 simulation on majors: +$364 per year on average, all of it from 2021".
- **Single-payment variant (posts EN line 23 / RU line 23):** "The single-payment variant is shown too; it is worse everywhere." — **the numbers are not printed anywhere in the pinned tree** (`data gap`).
- **Self-declared unmodelled items (posts EN final italic paragraph):** delisted perps (absent), delisting risk on an open position, inability to close spot in a thin book, basis moving against the position on early exit, short-leg margin during vertical rallies — all "making reality worse"; the entry premium — "making it better"; the source asserts the second is smaller than the first (`source-reported`, not verified).
- **README results row (README.md §Results, "Extreme-funding spike arbitrage on small perps"):** "658 perps, 364 hedgeable, full funding history 2019–2026", pre-declared episode rule "(enter after 3 payments ≥ 100%/yr, exit < 30%, 50 bp/episode), capital-constrained simulation, optimistic-entry bound", "1,125 episodes, 58% profitable", "2021: +1,000% of notional summed", "2024 burst", "**2023, 2025, 2026: negative even with optimistic entry at any threshold**", causal note "since 2023 funding settles every 4 h instead of 8, episodes last 0.5 days instead of 3".
- **Methodology claims for the whole project (README §"Methodology"):** event study before backtest, walk-forward with non-overlapping windows, concentration decomposition, own-momentum control, signal inversion, per-side cost modelling, no-lookahead rule, "pre-declared rules; sensitivity ≠ optimization", t-statistics over annualized Sharpe on short samples. **No t-statistic, p-value, Sharpe, drawdown or confidence interval is printed for the funding-spike row** — the source's own stated preference for t over Sharpe is not applied to this result (`data gap`).
- **Publication status:** no DOI / journal / preprint / peer-review statement (`not stated in source`); sole-author AI-assisted public repository with 0 stars and 0 forks at the pinned snapshot.

### Independently reproduced

Our own reproduction (script written by this Scout, run 2026-09-29, **not** a re-run of the source's code): `full_repro.py` re-fetches the complete `GET /fapi/v1/fundingRate` history for every currently hedgeable USDT perpetual (window 2019-09-01 → 2026-09-18 UTC, 365/367 symbols succeeded) and re-implements the episode rule from a line-level read of the pinned `funding_scan.py::episodes`/`simulate`; aggregation scripts then compare our output with the committed `results/*.csv`. Artefacts: `full_repro.json` (1,125 episodes), `full_repro_log.txt`, `full_repro_errors.json`, `raw_funding.json`, `listing_check.json`, plus the comparison scripts.

- **Exact episode-set match:** our independent run produced **exactly 1,125 episodes** (source: 1,125), and for **all six years** the four printed columns — episode count, share profitable, median net, summed net — match `results/funding_scan_by_year.csv` to **0.000000 difference**: 2020 `170 / 52.3529 / +0.0544 / +66.2275`, 2021 `615 / 62.9268 / +0.6425 / +1001.0269`, 2023 `37 / 21.6216 / −0.2113 / −5.1268`, 2024 `233 / 67.8112 / +0.3138 / +104.9247`, 2025 `43 / 20.9302 / −0.3280 / −7.7294`, 2026 `27 / 3.7037 / −0.3979 / −8.4977`; no 2022 row because there were no 2022 episodes.
- **Headline aggregates reproduced:** 57.9556% profitable (printed 58%), median +0.1993% (printed +0.20%), mean +1.0230% (printed +1.02%), median duration **2.6667 days** (printed 2.7), top-5 share of the total **6.0317%** (printed 6%), grand summed net **+1,150.83% of notional**.
- **Capital-constrained simulation reproduced:** episodes taken = **249** = `59+48+18+54+43+27`, and per-year USD = **+597 / +2,750 / +26 / +284 / −258 / −283**, matching `сим_usd` in the committed CSV exactly (total +$3,116).
- **Named winners reproduced:** IOTAUSDT episode `2021-02-02 08:00 → 2021-02-22 16:00`, **61 payments**, entry annualized **104.1%**, net **+15.30%** over **20.3 days**; then TRB +14.88%, ANKR +13.98%, EGLD +12.67%, YFI +12.58%, 1INCH +12.01%, RSR +11.80%, THETA +10.65% — all in Jan–Apr 2021 (printed values +14.9 / +14.0 / +12.7 / +12.6 / +12.0).
- **Optimistic-entry table reproduced 12/12 cells** under the interpretation "credited stream starts at the confirming payment": 100%/3 → `2021 +1108.4 | 2024 +123.4 | 2025 −4.0 | 2026 −6.6`; 200%/3 → `+662.7 | +10.6 | +4.6 | −1.4`; 300%/2 → `+350.9 | +3.5 | +5.3 | −2.2` (printed: 1108/123/−4.0/−6.6, 663/11/4.6/−1.4, 351/3.5/5.3/−2.2 — every cell agrees at printed precision). Two competing interpretations were tested and rejected: "enter one payment earlier without crediting" and "credit the extra earlier payment too" both miss multiple cells.
- **Payment-interval diagnostic reproduced:** median interval of payments *inside* episodes = **8.00h in 2020 (n=1,566) and 2021 (n=9,076)**, and **4.00h in 2023 (n=405), 2024 (n=4,320), 2025 (n=266), 2026 (n=171)** — exactly the source's 8h-vs-4h claim. Across *all* payments the shift is gradual rather than a 2023 step: 4-hour share is 0.0% (2019–2022), 7.1% (2023), 49.3% (2024), 68.3% (2025), 79.5% (2026), with the all-payings median staying 8h through 2024 and moving to 4h only in 2025.
- **Episode-duration diagnostic reproduced:** per-year medians 2021 **3.000**, 2024 **3.000**, 2025 **0.667**, 2026 **0.500** days (printed 3.0 / 3.0 / 0.67 / 0.5); also 2020 1.667 and 2023 1.167 days (not printed).
- **New-listing check reproduced within snapshot drift:** our independent recomputation with the source's own formula (`sum(rate)/sum(hours)*8760*100` over the first 14 days from `onboardDate`, ≥6 payments required) over **362** listings gives mean **−52.23%** (printed −53%), median **+4.94%** (printed +5%), **17/362 = 4.70%** above 100% (printed 5%), 43.6% negative.
- **"Last twelve months" figure:** for the window 2025-09-18 → 2026-09-18 our simulation gives **−$292** (46 taken episodes) against the printed **−$293**, so the sentence reproduces *as the simulation reading*; the take-all upper-bound reading of the same window gives **−$876**. The post does not label which of its two numbers the sentence uses (`label ambiguity`, not counted as a contradiction).
- **"From 2022 through 2026" totals:** research-computed **+$8,357** upper bound and **−$231** simulation when 2022–2026 are summed inclusively, versus **−$2,135** and **−$515** when 2024 is excluded — the printed −$2,136/−$515 match the *excl-2024* arithmetic (see contradiction 2).
- **Single-payment variant (confirm=1) re-computed:** summed net by year `2020 −11.6 | 2021 +1,158.1 | 2022 −1.5 | 2023 −64.9 | 2024 +88.6 | 2025 −124.4 | 2026 −61.8`, grand **+982.5%** vs confirm=3's **+1,150.8%**; episode counts `665/1,244/3/253/813/323/150`; $10k/3-slot simulation `−2,049 / +2,097 / −50 / −1,068 / −1,469 / −4,047 / −2,062`, total **−$8,648** vs confirm=3's **+$3,116** (see contradiction 4).
- **16-majors control re-computed** using the repository's own 16-symbol constant (see contradiction 5): confirm=3 → 2020 n=66 (+23.6%), 2021 n=136 (+193.92%), no other years, simulation `$339 (2020) + $2,215 (2021) = $2,554`, **$364.9/yr over 7 years** (printed +$364); confirm=1 → 2020 n=234, 2021 n=250, 2024 n=22, simulation `$250.6/yr`.
- **Universe drift noted:** 658 perps at both snapshots; hedgeable 364 (source, 2026-09-18) vs **367** (ours, 2026-09-29) — consistent with three new/renamed spot pairs appearing between the two dates; the episode count is nonetheless identical, so none of the three carries an episode.
- **Not reproduced / not attempted:** the source's causal story that bots harvest the spike "within one or two payments", the "funds cannot enter" capacity claim, any per-venue fee or spread model (none exists in the source), and any out-of-sample period after 2026-09-18; the January-2021 $100,000 sentence was *attempted and refuted* rather than left unreproduced (see contradiction 3).

### Negative evidence

1. The source's own conclusion is negative: the rule is **profitable only in 2020, 2021 and 2024**, and **net-negative in 2023, 2025 and 2026** at the headline threshold — reproduced exactly.
2. At the headline 100%/3 setting with the optimistic (non-executable) entry bound, **2023 −3.0%, 2025 −4.0%, 2026 −6.6%** are still negative (our re-computation) — i.e. the death is not purely an entry-timing artifact at that threshold.
3. **2026 share profitable is 3.70%** (1 of 27 episodes) and 2025 is 20.93% — a near-total failure rate in the live regime, reproduced.
4. The **capital-constrained simulation is negative in 2025 (−$258) and 2026 (−$283)** — the version a $10k trader could actually run loses in both recent years.
5. The **single-payment variant is far worse in simulation** (total −$8,648 vs +$3,116; 2025 −$4,047 vs −$258), confirming that entering faster does not rescue the rule even though one year's summed net improves.
6. **Survivorship is structural and adverse:** only live contracts are in the universe; the source states delisted perps "exactly the ones where things went worst" are missing, so measured results are biased **upward**.
7. **New listings are systematically short-funded:** mean first-14-day funding **−52.23% annualized** (reproduced over our 362-listing snapshot), median +4.94% but 43.6% negative — on the source's own listing check the crowd's "short the new listing" trade pays the longs on average (the source frames this as the 2024–2026 regime; the listing-date window of its 361-listing check is `not stated in source`).
8. **Concentration in one regime:** +1,001 of the +1,150.83pp grand total (87.0%, research-computed) comes from 2021 alone, and **Jan–Apr 2021 alone contributes +1,011.0pp** — essentially the entire seven-year edge is one first-quarter-2021 episode cluster.
9. **Cost model is a flat 50 bp guess**, not a measured fee+spread+impact model; there is no fee schedule, no spread series, no participation cap and no latency anywhere in the pinned tree, so every net figure inherits that single assumption (sensitivity untested by the source).
10. **Basis, margin financing of the short leg, delisting of an open position, and thin-book spot exits are all unmodelled**, and the source itself lists them as reality-worsening — the recorded net numbers are therefore not a full cost accounting.
11. **No statistical significance is reported for this result**: no t-statistic, p-value, standard error, bootstrap or confidence interval appears for the funding-spike row, despite the repository's own methodology section demanding t-statistics on short samples.
12. **Single venue, single market type, single instrument family** (Binance USDT-M perps + spot) — no cross-venue or cross-era replication exists in the source.
13. **Thin adversarial validation:** the source never runs a placebo (shuffled funding series), never tests a competing explanation (were the same episodes profitable from price moves rather than funding?), and never reports an ablation of the three-payment filter's effect year by year.
14. **Publication and scrutiny status:** non-peer-reviewed sole-author public repository, 0 stars / 0 forks, AI-assisted authorship disclosed, no independent citation or replication located; the dev.to mirror is the same text, not a second opinion.
15. **Internal traceability gap:** README points at journal sections that contain no funding-spike material, and two printed claims (the single-payment table, the 16-major list) have no printed source data behind them.
16. **Five unreconciled internal contradictions** are recorded in the frontmatter (README "any threshold" vs the post's own 2025 cells; the 2022–2026 totals; the January-2021 $100,000 sentence; "worse everywhere"; the 16-majors control).
17. **Sample ends 2026-09-18** — there is no forward test, and the rule's parameters were "written down before the run" only in the sense asserted by the author (no timestamped preregistration exists in the tree).
18. **Universe point-in-time dependence:** running the same code on a different date yields a different hedgeable set (364 → 367), so exact reproduction requires pinning both the commit and the snapshot date.
19. **Adjacency caveat:** none of the existing repository funding records replicates this source's episode-harvest rule; they study carry, cross-sectional ranks, price reversal after funding extremes, or venue design (see Related records and the distinction statements below).

## Falsification plan

Every threshold below is a **research-defined falsification threshold** chosen by this Scout, not by the source; every data choice not in the source is `research-proposed`. No test may be rescued by unconstrained retuning (see F14).

- **F1 — Printed-value reproduction gate.** Data: Binance funding history re-pulled for the pinned commit, same universe rule. Metric: per-year episode count, share profitable, median net, summed net vs `results/funding_scan_by_year.csv`. Threshold: every cell within **±0.01 pp** of notional and counts exact (research-defined). Action on failure: record marked `reproduction-failed`, no downstream use of any figure in this record. *(Currently PASSED for 2026-09-29, 0.000000 across all cells.)*
- **F2 — Frozen forward test.** Data: funding payments from **2026-10-01** for 12 months on the then-live hedgeable universe. Metric: summed net at 100%/3/50bp and simulated USD. Threshold: summed net **≥ 0** and simulated USD **≥ 0** (research-defined). Action: both negative ⇒ hypothesis "the edge can revive under the current 4h/1h regime" is rejected and the record's negative conclusion is locked; do not raise thresholds to manufacture a pass.
- **F3 — Delisted-universe recovery.** Data: rebuild the perp universe including contracts delisted since 2019 (Binance delivery/delisting notices, third-party archives). Metric: change in 2021 and 2024 summed net and in post-2023 summed net. Threshold: > **10%** relative change (research-defined) or post-2023 turning positive. Action: if exceeded, the source's survivorship caveat becomes a quantified bias and all by-year figures are re-stated as lower bounds.
- **F4 — Cost ladder.** Data: same episode sets. Metric: summed net per year at **0 / 10 / 25 / 50 / 75 / 100 bp** per episode (research-proposed ladder). Threshold: sign flips at **≤ 25 bp**. Action: if 2021/2024 flip at ≤25 bp, the "real 2021 edge" claim is weakened (it was cost-model-driven); if 2024 survives 100 bp but 2023/2025/2026 never turn positive at 0 bp, cost is not the explanation for the post-2023 death and the mechanism claim shifts to entry exhaustion.
- **F5 — Threshold-surface stability (structural-death test).** Data: full grid `enter ∈ {50,100,200,300}` × `confirm ∈ {1,2,3}` × `exit ∈ {20,30,50}` evaluated separately for 2023–2026 (research-proposed grid). Metric: summed net and episode count. Threshold: any cell with **≥ 30 episodes** and summed net **> +100 pp** of notional over 2023–2026 (research-defined). Action: if found, "the edge died structurally" is falsified and the cell must be labeled post-hoc and confirmed on F2's frozen window before any use.
- **F6 — Basis-inclusive recompute.** Data: per-episode entry/exit premium (perp mark vs spot mid, or perp vs index) at entry and exit. Metric: yearly change in summed net vs the basis-ignored baseline. Threshold: **> 20 pp** of notional in any year (research-defined). Action: if exceeded, the source's "basis ignored is conservative, and the favourable side is smaller" assertion is falsified in that year and net figures must be restated with basis included.
- **F7 — Interval-regime ablation.** Data: episodes split by payment grid actually observed (8h-dominant vs 4h/1h-dominant). Metric: mean net per episode and summed net within each regime, controlling for entry threshold (research-proposed). Threshold: 4h-era episodes at entry ≥ 300% annualized with **n ≥ 30** showing mean net **> 0** (research-defined). Action: if met, the claimed mechanism "4-hour funding killed the harvest" is unsupported and the explanation must be re-specified (competition, listing mix, or rate dispersion).
- **F8 — Capacity stress.** Data: same episodes, slot size scaled **$3,333 → $10,000 → $25,000** with a research-proposed square-root impact penalty calibrated to the symbol's median 1-minute range. Metric: change in 2021 summed net and simulated USD. Threshold: **> 30%** reduction at $25k/slot (research-defined). Action: if exceeded, the "$10k is an advantage" framing is narrowed to sub-$10k accounts only and capacity claims are dropped from any downstream summary.
- **F9 — Symbol-shuffle placebo.** Data: 1,000 draws of funding series randomly reassigned across hedgeable symbols, same rule, same years (research-proposed). Metric: rank of the observed 2021 summed net in the null distribution. Threshold: below the **95th percentile** (research-defined). Action: if below, the 2021 result is not distinguishable from cross-sectional artifact and the entire record is downgraded to `unproven` even for 2021.
- **F10 — Competing-explanation control (price vs funding).** Data: for each episode, mark-to-market P&L of the short-perp/long-spot pair excluding funding over the same window. Metric: ratio |price P&L| / |funding P&L|. Threshold: median ratio **> 1.0** (research-defined). Action: if exceeded, the mechanism label changes from "funding harvest" to "premium-compression/basis trade" and the record must be re-scoped, since the source ignores basis by construction.
- **F11 — Cross-venue replication.** Data: the same rule on Bybit and OKX USDT-margined perps with their own spot hedges, identical parameters (research-proposed). Metric: sign and magnitude of 2021 and 2023–2026 summed net. Threshold: same sign with **≥ 50%** of Binance's magnitude in **2 of 3 venues** (research-defined). Action: failure ⇒ single-venue finding only; the record stays Binance-scoped and may not be described as a market-wide effect.
- **F12 — Direction-flip test on listings.** Data: the source's own 14-day listing funding series (362 listings). Metric: one-sample t of annualized 14-day funding against 0 (research-proposed test). Threshold: mean **−52%** with **|t| ≥ 1.96** (research-defined). Action: if confirmed, the *opposite* trade (long perp / short-or-no-spot hedge on new listings, funding-only) becomes the candidate hypothesis and must be registered as a **new, separately reviewed** record — it may not be silently substituted into this one.
- **F13 — Multiplicity control.** Over the F5 grid (36 parameter cells × 6 year-blocks) apply **Benjamini-Hochberg at q < 0.10** (research-defined). Action: any "revival" cell failing correction is reported as expected-under-multiplicity and cannot support adoption.
- **F14 — Action-on-failure map (governs F1–F13).** F1 or F2 failure ⇒ record remains `research-only` and the hypothesis is marked **refuted**; F3/F4/F6/F7/F8 failures ⇒ mechanism narrative must be rewritten before any reuse; F9/F10/F11 failure ⇒ 2021 evidence downgraded to `unproven` / venue-specific; **no retuning of enter/exit/confirm/cost may be used to rescue a failed test** — any new parameter choice is a new hypothesis requiring a new frozen window (F2) and must be labeled `research-proposed`.

## Crypto portability

**direct.** The evidence is itself Binance USDT-M perpetual funding on live crypto markets, with a Binance spot hedge; nothing is ported from another asset class.

Residual portability risks that remain inside that `direct` setting:

- **Spot vs perpetual differences:** the hedge leg is Binance spot only; cross-venue spot (or a futures hedge) changes borrow, tick size and fee tier, and the source never tests it.
- **Funding:** the return stream *is* funding; 8h → 4h → 1h grid changes, contract-specific rateType and any switch to non-linear funding directly alter entry annualization (our annualization clamps intervals to [1,8] h exactly as the source does).
- **24/7 sessions:** no session boundary issues for funding, but liquidations and premium spikes cluster in thin hours, which the flat cost does not represent.
- **Venue fragmentation / single venue:** one exchange's rate schedule, listing policy and delisting policy drive every number (F11).
- **Liquidity / impact:** small-cap perps and their spot pairs can be < $1M deep; no depth or participation data is used anywhere.
- **Mark vs index price:** the delta-neutral pair's liquidation and margin behaviour depends on mark price, which is not modelled.
- **Contract specification:** tick size, lot size, minimum notional and whether the spot pair is `TRADING` all gate executability; not checked.
- **Timestamp / candle boundaries:** funding timestamps only; no candle alignment needed, but our client failed on 2 non-ASCII symbols — a mundane data-plumbing edge.
- **Listing/delisting survivorship:** live-only universe (F3) is the dominant sample bias.

Crypto portability is **not** authorization to trade.

## Limitations

- `underspecified`: the 16-majors control list, the single-payment-variant table, the fee/slippage build-up behind 50 bp, order type and fill model, and the label on the "last twelve months" figure.
- `data gap`: no t-statistics/p-values/CIs anywhere in this result; no spread, impact, participation, latency, margin or liquidation model; no delisted contracts; no out-of-sample window after 2026-09-18.
- `not independently reproduced`: the causal bot-competition story, the capacity claim about funds, the "pre-declared before the run" status (asserted, not timestamped), and every figure in README's methodology claims as applied to this row.
- `unproven`: any claim that the rule works in 2024-style bursts again, works on other venues, or survives a basis-inclusive/cost-measured accounting.
- Reproduction is **exact but not independent in data provenance**: we re-pulled the same public Binance endpoint, so a systematic vendor-side revision to historical funding would move both the source and our numbers together.
- Our universe snapshot is one day and three hedgeable symbols apart from the source's; the identical episode count is reassuring but shows the rule's output is sensitive to snapshot drift (18).
- The reproduction re-implements the rule rather than executing the source's script (its `fetch_daily.py` dependency chain and cache format were not run); the re-implementation was validated by exact agreement with the committed CSVs on 24 year×column cells plus the 12 optimistic cells.
- No Wiki Brain record, candidate-pool entry, backtest, implementation or Paper/Testnet/Live step is implied by this capture.

## Implementation status

`implementation_status: not-implemented`. Nothing from this record has been implemented in our research stack: no NautilusTrader/Qlib/Paper/Testnet/Live artifact, no dependency installed, no production card, no candidate-pool entry. What exists is (a) the public third-party code at the pinned commit and (b) this Scout's throwaway reproduction scripts in the local scratch cache, which are research verification only and are not a strategy implementation.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. The presence of this record does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet or live trading. `confidence: medium` describes only confidence in this research interpretation (the rule is fully specified and exactly reproduced, but five source-side contradictions and a cost model that is a flat assumption remain unresolved). Nothing in this record may promote itself by evidence count, reproduction exactness, or `contested` status.

## Related Wiki records

Adjacent pages returned by read-only Wiki Brain search on 2026-09-29 (linked as returned; no page was written or modified by this run):

- [[quant/crypto-cex-dex-cross-venue-funding-spread-carry-2026-08-31]]
- [[quant/btc-perp-single-venue-funding-carry-taker-fee-falsification-2026-09-14]]
- [[quant/crypto-cross-venue-funding-carry-negative-results-cost-decay-2026-09-13]]
- [[quant/crypto-spot-perpetual-dynamic-collateral-control-impulse-band-2026-09-02]]
- [[quant/crypto-two-tiered-cex-dominant-funding-discovery-structural-arbitrage-2026-09-12]]
- [[quant/defi-amm-delta-neutral-optimal-hedge-liquidation-constraint-2026-09-11]]

Four-axis distinction (mechanism / signal construction / universe / horizon) stated against the closest **repository** records, all confirmed to carry different source identities:

1. `crypto-funding-rate-arbitrage-event-driven-mvo-adaptive-interval-2026-09-23.md` — source is a peer-reviewed JSTKU article (DOI 10.56825/jstku.2026.1524724) on **event-driven mean-variance portfolio allocation** with volatility gating across a basket; ours is a **single-episode, fixed-size, threshold-triggered** harvest rule with no optimizer, no portfolio weights and a negative result. Source identity differs entirely.
2. `crypto-perpetual-funding-extreme-direction-conditional-reversal-2026-09-28.md` — source SSRN 7520320 studies **price-direction reversal after funding extremes** with a conditional-arbitrage-capacity state variable (event study on returns); ours never uses price direction — payoff is the **funding payment stream under a delta-neutral hedge**. Source identity and mechanism differ.
3. `crypto-funding-carry-fade-turnover-cost-dissipation-falsification-2026-09-12.md` — source JosephBerachah/crypto-fundingrate-alpha @ `9d26979a` is a **cross-sectional rank carry factor** with turnover/cost dissipation tests; ours is a **time-series extreme-spike episode rule** (enter/exit on the same symbol's own rate path) with capital-slot simulation. Source identity and signal construction differ.
4. `crypto-perpetual-funding-rate-extreme-reversion-volatility-expansion-gating-2026-09-13.md` — different source and a **price-reversion entry gated by volatility expansion**; ours has no price signal at all.

## Sources

- `https://github.com/stooq1/strategy-graveyard` — repository, pinned tree **`5d0341c665f6030acc3c756664427e712b8f5c39`** (2026-09-22T19:00:11Z), MIT license, sole author `stooq1`, created 2026-09-20, read 2026-09-29.
- `https://github.com/stooq1/strategy-graveyard/blob/5d0341c665f6030acc3c756664427e712b8f5c39/README.md` — results table row, methodology list, reproduce command, write-up index, About/authorship/AI disclosure.
- `https://github.com/stooq1/strategy-graveyard/blob/5d0341c665f6030acc3c756664427e712b8f5c39/posts/2026-09-funding-spikes.en.md` — primary write-up: rule definition, sample, by-year table, optimistic table, why-it-died diagnostics, unmodelled-items paragraph.
- `https://github.com/stooq1/strategy-graveyard/blob/5d0341c665f6030acc3c756664427e712b8f5c39/posts/2026-09-funding-spikes.md` — Russian original of the same write-up (used to disambiguate the single-payment-variant sentence).
- `https://github.com/stooq1/strategy-graveyard/blob/5d0341c665f6030acc3c756664427e712b8f5c39/funding_scan.py` — executable rule: `list_symbols`, `load_payments`, `episodes`, `simulate`, `scan`, argparse defaults (`--enter 100 --exit 30 --cost 50 --capital 10000 --slots 3 --confirm 1`), docstring cost/limitation notes.
- `https://github.com/stooq1/strategy-graveyard/blob/5d0341c665f6030acc3c756664427e712b8f5c39/results/funding_scan_by_year.csv` — committed by-year table (Russian column names), the target of our reproduction.
- `https://github.com/stooq1/strategy-graveyard/blob/5d0341c665f6030acc3c756664427e712b8f5c39/results/funding_scan_episodes.csv` — all 1,125 committed episodes (159,152 bytes).
- `https://github.com/stooq1/strategy-graveyard/blob/5d0341c665f6030acc3c756664427e712b8f5c39/results/README.md` — column definitions for the two funding CSVs, statement that raw market data is not in the repository.
- `https://github.com/stooq1/strategy-graveyard/blob/5d0341c665f6030acc3c756664427e712b8f5c39/fetch_daily.py` — `CRYPTO_SYMBOLS` (the inferred 16-majors list) and the shared funding fetcher.
- `https://github.com/stooq1/strategy-graveyard/blob/5d0341c665f6030acc3c756664427e712b8f5c39/docs/FINDINGS.md` and `https://github.com/stooq1/strategy-graveyard/blob/5d0341c665f6030acc3c756664427e712b8f5c39/docs/REVIEW.md` — checked for a funding-spike section (none found; traceability gap recorded).
- `https://github.com/stooq1/strategy-graveyard/blob/5d0341c665f6030acc3c756664427e712b8f5c39/LICENSE` — MIT.
- `https://dev.to/stooq1/i-tested-harvest-extreme-funding-on-small-perps-on-all-658-binance-perpetuals-it-died-in-2023-46mh` — mirror of the EN write-up, linked from the pinned README; read only for cross-checking, not used as an independent source.
- Independent data pulls for reproduction (Scout-run, 2026-09-29): `GET https://fapi.binance.com/fapi/v1/fundingRate` (paginated full history per symbol), `GET https://fapi.binance.com/fapi/v1/exchangeInfo`, `GET https://api.binance.com/api/v3/exchangeInfo` — public endpoints, no keys.
