# alpha-strategy-research

[English](README.md) | **繁體中文**

這是一個公開的策略研究暫存 repository，用來把外部 alpha 策略研究整理成可直接供 Hermes Wiki Brain 吸收的標準化格式。

## 用途

本 repository 是 **三個獨立 Research Scout（ChatGPT / Hermes / Antigravity）** 與 **ChatGPT Research Intake Review / Wiki Brain ingestion** 之間的交接層。

運作流程：

```text
外部公開來源
（GitHub / FMZ / TradingView / papers / blogs / public research）
        ↓
ChatGPT / Hermes / Antigravity（獨立平行的 Research Scout）
尋找 alpha 想法 → 理解 → 標準化 → push 到這裡
        ↓
ChatGPT
Research Intake Review
（PASS / PASS-WITH-CAVEAT / REMEDIATE / REJECT）
        ↓
ChatGPT 將通過 intake 的知識直接寫入 Hermes Wiki Brain
        ↓
Hermes 使用這些知識進行研究、組合與後續驗證
```

三個 Scout 的有效公開來源契約：GitHub / FMZ / TradingView / papers / blogs / public research。TradingView 僅限公開、可追溯的 strategy/idea/script/research URL，須保留 stable URL 與 as-of date；private/paid/invite-only 不可用。

**任何 Scout 都不得直接寫入 Hermes Wiki Brain。** 每個 Scout 唯一的輸出管道是本 repository。Push 到這裡的 artifact 應該已經是 Wiki Brain-native 格式，讓 ChatGPT 可以完成 Research Intake Review 後直接 ingest，而不需要再做一次翻譯或重新整理。

## 本 repository 在整體系統中的位置

本 repository 是整體量化工作流中的**上游策略研究與知識交接層**。它本身不負責正式策略驗證，也不負責交易執行。

經過 ChatGPT Research Intake Review 與 Wiki Brain ingestion 後，Hermes 可以使用已接受的知識來組合、推演可測試的策略假說。這些假說之後可以進入 [`nautilus-quant-system`](https://github.com/HCH725/nautilus-quant-system)，由 PyBroker 進行隔離式策略研究，再由 NautilusTrader 提供正式歷史 verdict 與 canonical accounting layer。

```text
外部公開來源
（GitHub / FMZ / TradingView / papers / blogs / public research）
        ↓
ChatGPT / Hermes / Antigravity 研究 Scout（獨立平行）
        ↓
alpha-strategy-research
        ↓
ChatGPT Research Intake Review
        ↓
Hermes Wiki Brain
        ↓
Hermes hypothesis / synthesis ── Loop A（low-frequency, theory/evidence-driven；每輪一個研究假說／策略族 → 有限有意義分支 → experiment spec）
        ↓
nautilus-quant-system
PyBroker Experiment & Attrition Loop（Loop B：deterministic campaign expansion → N provisional candidates → batch screens → dedupe/invalid/reject/pass 記帳；high-throughput，無 LLM per candidate；淘汰不進 Nautilus）→ Gate（signal parity, fail-closed）→ NautilusTrader high-fidelity historical verdict（僅 survivors）
        ↓
feedback / lineage / reuse ── outer evidence-based feedback（survivor summary / failure taxonomy / information gain → stop / refine / new batch；非固定回測次數）
        ↓
後續經 gate 進入 Paper → Binance Demo/Testnet → Live
```

*因此，一筆策略紀錄出現在本 repository，只代表它是已標準化的**研究素材**。這**不代表**該策略已通過 PyBroker/Nautilus 驗證、Paper Trading、Testnet 或 Live Trading 授權。在正典 pipeline 中，本 repository 餵給 **Loop A（Hermes Research Loop）**。*

---

## Research Scout：每次研究前都必須先閱讀本 README

你的工作是從公開外部來源搜尋可能有價值的 **alpha 策略或 alpha 假說**，然後把每一個值得保留的項目轉換成下方規定的研究紀錄格式，再 push 到本 repository。

你是三個獨立平行 Research Scout（ChatGPT / Hermes / Antigravity）之一。每個 Scout 自主運作，指向同一個 repository。不要重複或覆蓋其他 Scout 已有的 artifact；產出新紀錄前請先 inspect 近期 commits。

有效公開來源：GitHub / FMZ / TradingView / papers / blogs / public research。TradingView 僅限公開、可追溯的 strategy/idea/script/research URL，須保留 stable URL 與 as-of date；private/paid/invite-only 不可用。

Scout dedup 契約：同 canonical source identity + 實質相同的 normalized rule => 不得新建 artifact；同 source 但 hypothesis/signal/horizon/mechanism 實質不同則可獨立（僅當核心假說在 mechanism、signal construction、universe/market type、horizon/regime、material data dependency 任一處實質不同時，才視為獨立）。

策略可以是：

- 單一訊號策略；
- 多訊號策略；
- 複合／混合策略；
- regime + signal + confirmation 組合；
- cross-sectional、time-series、relative-value、spread、basis、funding、volatility、order-flow、market-microstructure 或其他具備合理論證的 alpha 想法。

混合策略是有效的策略形式。若一個策略的經濟假說本來就依賴多個元件共同作用，**不要**強迫把它拆成多筆獨立紀錄；應該在 `Economic mechanism` 與 `Signal` 中清楚保留每個元件的角色。

有效的混合策略結構例如：

```text
regime filter
+ entry signal
+ confirmation filter
+ exit / risk logic
```

不要把任意堆疊技術指標視為更強的證據。若一套複雜規則缺乏一致的經濟或行為機制，應如實描述這個問題。

---

## Canonical Wiki Brain schema

策略研究 contract 以版本化 specification 的方式保存在 Hermes Wiki Brain。以本 README 更新當下而言，目前的 canonical specification 是：

```text
quant/strategy-research-record-spec-v1.md
schema: strategy-research-record-v1
```

上面的 `v1` 只代表**目前**的 canonical 版本，不是永久寫死的 contract。每次本機排程 Scout 執行前，都必須先解析並讀取 Wiki Brain 中目前有效的 `quant/strategy-research-record-spec-v*.md` versioned specification，並使用該 specification 宣告的 `schema` 與必要結構。若已有較新的 canonical specification，應以新版為準，而不是繼續照本 README 裡的舊版範例。若無法確認 canonical specification，應 fail closed，不要自行猜測。

不要另外發明新的 candidate schema，也不要默默把舊紀錄搬成新版。既有紀錄仍依建立當時的 schema version 保持有效，除非另外存在明確的 versioned migration rule。

### 必要 frontmatter

下方範例反映目前的 v1 specification。新紀錄必須使用每次執行時實際解析到的 canonical specification 所要求的完整 frontmatter：

```yaml
---
schema: strategy-research-record-v1
title: <strategy title>
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: low | medium | high
source_as_of: <source/data as-of date>
sources:
  - <traceable source URL or repository reference>
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---
```

對於新發現的外部策略，除非我們自己的研究系統中已經存在可獨立驗證的證據，否則以下預設值是強制要求：

```yaml
status: research-only
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
```

`confidence` 描述的是對**研究解讀是否正確**的信心，不是對策略獲利能力的信心，也不代表任何交易授權。

---

## 必要文件結構

每一筆策略紀錄都必須使用以下結構。若某項資訊無法取得，仍然保留該 section，並清楚標示缺口，不要直接刪除。

```markdown
# <Title>

## Provenance

## Economic mechanism
### Source-reported
### Research interpretation

## Signal

## Required data

## Execution assumptions

## Evidence
### Source-reported
### Independently reproduced
### Negative evidence

## Falsification plan

## Crypto portability

## Limitations

## Implementation status

## Adoption boundary

## Related Wiki records

## Sources
```

### 1. Provenance

必須記錄足夠資訊，使研究來源可以被重新定位與重現。

對 GitHub 來源，需保留：

- repository URL；
- **完整 commit SHA**；
- 精確 file path；
- 對應 source URL。

若可以取得固定 commit，不要只使用 `main`、`master`、`latest`、tag 或縮短版 SHA。

對 TradingView 來源，僅限公開、可追溯的 strategy/idea/script/research URL，須保留 stable URL 與 as-of date；private/paid/invite-only 不可用。對 papers、blogs、FMZ 或其他公開來源，保留最穩定的 URL 與 source/data as-of date。

### 2. Economic mechanism

要把原始來源的主張與我們的標準化解讀分開。

`Source-reported` 應描述原作者提出的理由，不要把作者的說法升級成已確認事實。

`Research interpretation` 應用可被證偽的方式描述假設中的機制，例如：

- trend persistence；
- liquidity provision / mean reversion；
- volatility expansion after compression；
- crowded positioning / funding pressure；
- cross-sectional momentum；
- basis convergence；
- order-flow imbalance；
- behavioral or structural market effects。

對混合策略，需明確指出每個元件的角色，例如：

```text
Regime: 200 EMA trend filter
Primary signal: Donchian breakout
Confirmation: volume expansion
Risk / exit: ATR stop
```

不要預設每一個元件都會貢獻 alpha；後續研究可能需要進行 ablation tests。

### 3. Signal

將交易邏輯標準化到研究人員能理解，並在可能的情況下能獨立重建。

視策略需要，應包含：

- signal formation timestamp；
- lookback window；
- long entry；
- short entry；
- exit；
- holding period；
- re-entry rules；
- parameters；
- position-sizing logic；
- multi-timeframe dependencies；
- 規則是否 fully specified 或 underspecified。

當標準化規則已足夠描述策略時，不要貼大量來源程式碼。保留 source link / commit / path 供 audit 即可。

### 4. Required data

清楚列出策略真正需要的資料，視情況包含：

- instrument / universe；
- venue；
- market type（spot / perpetual / futures / options）；
- timeframe；
- OHLCV fields；
- funding；
- mark / index / basis data；
- trades / aggressor side；
- order book / depth；
- open interest；
- options surface / Greeks；
- timestamp 與 timezone requirements；
- point-in-time / availability requirements；
- missing-data assumptions。

### 5. Execution assumptions

需記錄重要執行假設，例如：

- signal-to-order timing；
- next-bar vs same-bar execution；
- market / limit order；
- fill model；
- fees；
- spread；
- slippage；
- impact / capacity；
- funding；
- leverage / margin；
- borrow / shorting；
- latency；
- partial fills / failures。

若來源沒有提供，就明確寫出缺失，不要自行補想像中的設定。

### 6. Evidence

三種 evidence 必須分開記錄。

#### Source-reported

第三方提供的 backtest、Sharpe、win rate、CAGR、drawdown 或 profitability claims 應放在這裡。

不要把來源聲稱的績效改寫成我們已驗證的結果。

每一個 source-reported 的績效數字、參數、門檻、勝率、Sharpe、t-statistic、CAGR、drawdown 或其他量化主張，都必須能逐項追溯到 `## Sources` 中的明確來源（例如 stable URL/DOI、commit SHA、頁碼或表格）。若無法追溯該精確數字，就應刪除它或明確註記 provenance 缺口，不能自行補出精確值。若數字來自股票、商品、傳統期貨或其他非 crypto 樣本，必須標明該資產類別，不能當成 crypto 實證結果。

對每一個 source-reported empirical claim，都必須確認引用的作者、paper title、sample / universe、methodology 與 reported result 確實屬於同一篇來源。不得僅因多篇研究主題相近，就把另一篇論文的樣本、方法、統計數字或研究發現拼接進來。若同一筆 research record 使用多篇論文，每一項主張都必須明確歸屬到各自的來源。

例如：

```text
Source reports Sharpe 2.1 over the stated sample. This result has not been independently reproduced.
```

#### Independently reproduced

對新發現的 Scout 研究，通常應填：

```text
Not independently reproduced.
```

只有在我們自己的 evidence 真實存在而且可追溯時，才可以記錄為 independently reproduced。

#### Negative evidence

記錄任何已知失敗、相反結果、不穩定 regime、交易成本敏感度、資料問題，或其他會削弱策略假說的證據。

若沒有找到，可寫類似：

```text
None identified in the reviewed sources; absence is not evidence of no negative result.
```

### 7. Falsification plan

說明什麼條件會推翻或明顯削弱這個假說。

優先記錄具體項目，例如：

- required sample；
- relevant regimes；
- baseline / control；
- 混合策略的 ablation tests；
- cost sensitivity；
- out-of-sample requirement；
- failure metric 或 threshold；
- 若失敗後應採取的動作。

### 8. Crypto portability

適用時使用以下其中一種判定：

```text
direct
adapted
unproven
not applicable
```

若策略機制源自傳統資產研究，除非引用來源本身已在 crypto 市場直接驗證該機制，否則不得標示為 `direct`。應使用 `adapted` 或 `unproven`，並在 Research interpretation 明確說明這是移植假說，不是 crypto empirical evidence。

並說明任何 crypto-specific portability risks，尤其是：

- spot vs perpetual differences；
- funding；
- 24/7 session structure；
- venue fragmentation；
- liquidity；
- mark / index price；
- contract specification；
- timestamp / candle boundaries。

### 9. Limitations

保留不確定性，不要自己補出不存在的確定性。

建議使用明確標記，例如：

```text
underspecified
not independently reproduced
data gap
unproven
```

### 10. Implementation status

對新研究的外部資料，通常應明確說明尚未在我們的研究 stack 中完成 implementation。

除非真的已經完成，否則不要暗示已通過 PyBroker、Nautilus、Paper、Testnet 或 Live 驗證。

### 11. Adoption boundary

所有新收集的外部策略都只能視為 research material。

一筆紀錄存在於本 repository，**不代表**：

- profitable；
- validated alpha；
- approved for implementation；
- approved for paper trading；
- approved for testnet；
- approved for live trading。

### 12. Related Wiki records

若已知有相關概念或 strategy family，可連結到相關 Wiki 紀錄。當 Hermes Wiki Brain 中存在穩定頁面時，可使用 Wiki-style link，例如：

```markdown
[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]
```

不要自行捏造不存在的 Wiki link。

### 13. Sources

列出這筆紀錄實際使用的所有公開來源。

---

## 檔案命名

使用全小寫、hyphen-separated、無空格的 filename。

具體 research capture 建議格式：

```text
<strategy-or-topic-slug>-<YYYY-MM-DD>.md
```

例如：

```text
bitcoin-negative-funding-contrarian-reversal-2026-08-31.md
volatility-compression-volume-breakout-2026-08-31.md
cross-sectional-crypto-momentum-2026-08-31.md
```

避免使用含糊 suffix，例如：

```text
latest
final
new
v2-final-final
```

除非該文件本身就是版本化 specification。

---

## Research Scout 研究規則

1. **搜尋 alpha，不是搜尋行銷績效。** 高報酬聲稱本身不是 alpha thesis。
2. **單一策略與混合策略都允許。** 保留真正有意義的元件結構。
3. **Push 前先標準化。** Push 到這裡的檔案必須已符合執行時解析到的 current canonical Wiki Brain strategy-research schema。
4. **保留 provenance。** 所有外部主張都必須可以追溯到來源。
5. **不要宣稱不存在的獨立驗證。**
6. **不要偷偷補完缺失資訊。** 缺口必須明確標示。
7. **不要不必要地複製大量 source code。** 優先使用標準化邏輯加 source references。
8. **不要把風險管理誤認為 alpha。** Stops、sizing、leverage、DCA、grid、martingale 等規則應與 predictive signal 分開辨識。
9. **不要把複雜度誤認為品質。** 多指標組合必須有一致的 thesis，而且在正式測試前都仍然是 unvalidated。
10. **不要直接寫入 Hermes Wiki Brain。** 將標準化 research artifact push 到本 repository，由 ChatGPT 執行 Research Intake Review；若接受，再由 ChatGPT 直接寫入 Wiki Brain。

---

## Public repository 衛生規則

這是一個 public repository。只可以使用公開研究材料與 public-safe 的標準化紀錄。

不要 commit：

- API keys、tokens、credentials 或 secrets；
- 私人帳戶、wallet 或 portfolio 資訊；
- private Telegram / Discord / paid-source content；
- Hermes private configuration；
- local-machine secrets；
- 無合法再散布權的 copyrighted source material。

若再散布權不明確，應引用來源並標準化策略想法，而不是大量複製原始作品。

---

## Push workflow

任何 Scout 都可以使用本機 GitHub CLI / Git tooling 更新本 repository。

每一次 research run：

1. 閱讀本 README。
2. 從公開外部來源搜尋值得研究的 alpha candidates。
3. 先解析 current canonical Wiki Brain strategy-research specification，再依其宣告的 schema 將每一個值得保留的 candidate 標準化。
4. 保留 source provenance，並把所有第三方結果標示為 source-reported。
5. Commit 產生的 Markdown record(s)。
6. Push 到本 repository。
7. 到此停止。ChatGPT 會另外進行 Research Intake Review 與直接 Wiki Brain ingestion。

目標很簡單：

> **Scout output 應該直接等於 Wiki Brain-ready input。**

如此可以降低 Scout、ChatGPT 與 Hermes 之間重複理解、重複摘要與不必要的 token 消耗。

---

## Scheduled Research Scouts

每一個 Research Scout 都有自己的排程，整體設計刻意採用**高頻率、低產出**。目標是持續尋找高品質研究，不是為了湊數量。

Scheduled Antigravity Scout 每一輪都必須從最新 `origin/main` 建立全新的 detached temporary Git worktree。一般 checkout 只作 coordinator，即使其中存在其他流程留下的 unrelated local dirt，也不得因此污染或阻塞 Antigravity；Antigravity 不得 inspect、修改、stage 或清理 coordinator 的 dirt，而某一輪失敗也不得傳染後續排程。

每一次 scheduled run：

1. 研究前先同步並檢查最新的 `origin/main`。不得覆蓋或隨意改寫其他 Scout 已有的 artifact。
2. 每次都完整閱讀本 README 以掌握 workflow contract，並另外解析、讀取目前 canonical 的 versioned Wiki Brain strategy-research specification，作為 record schema 的唯一依據。
3. 從公開且可追溯的來源（GitHub / FMZ / TradingView / papers / blogs / public research；TradingView 僅限公開、可追溯的 strategy/idea/script/research URL 並須保留 stable URL 與 as-of date，private/paid 不可用）搜尋新的 alpha 策略或可被證偽的 alpha 假說。建立任何 Markdown 紀錄前，必須直接閱讀 primary source 本身（論文／全文、官方研究，或精確的公開 implementation/code path）。搜尋結果摘要、snippet、二手摘要與模型生成摘要只能作為 discovery aid，不得用來補寫策略規則或 empirical claim。
4. 建立新檔案前，先檢查 repository 中既有紀錄與來源。Scout dedup：同 canonical source identity + 實質相同的 normalized rule => 不得新建 artifact；同 source 但 hypothesis/signal/horizon/mechanism 實質不同則可獨立（僅當核心假說在 mechanism、signal construction、universe/market type、horizon/regime、material data dependency 任一處實質不同時）。Exact duplicate、只有措辭不同的 paraphrase、或實質相同的 capture 都不應產生新 artifact。
5. 每輪預設**最多 1 筆**新策略紀錄。**0 筆完全是有效且成功的結果，不得為了配額硬湊候選。** 只有當第 2 或第 3 個候選在 dedup 判準下彼此明確獨立，而且每一筆都經過直接 primary-source verification 並各自 source-complete 時，才允許例外產出。3 筆仍是絕對上限，不是目標。
6. 若策略 thesis 本身依賴多個元件，必須保留 hybrid/composite 結構，不要只留下最顯眼的一個 indicator。
7. 若 strategy identity、signal semantics、causal timing、required data、provenance 或 public-use rights 仍有重大不確定性，不要猜。這次直接略過該 candidate。凡 primary source 未明確指定的 threshold、entry/exit trigger、execution timestamp 或 fill model、fee/slippage assumption、capacity claim、universe/liquidity filter、crypto-porting rule、position-sizing choice 或其他 operational rule，都必須標成 `research-proposed`；凡由 Scout 自行設定的 acceptance/failure/falsification cutoff，都必須標成 `research-defined falsification threshold`。若任何重大欄位無法明確判定為 source-reported 或 research-proposed，直接略過該 candidate。
8. 每一筆輸出的 artifact 都必須符合 current canonical strategy-research schema，並維持 `research-only`、`not-implemented`、`not-approved` 邊界。Commit 前必須 read back 該 artifact，確認上述 operational fields 的 source-vs-research 標籤正確；不得默默補完來源本身 underspecified 的缺口。
9. 只 commit 本次刻意建立或修正的 artifact。若沒有 candidate 通過品質門檻，不得建立 empty commit。
10. 明確 push 並確認 remote 已包含該 commit 後停止。Antigravity 的 detached worktree 必須使用 `git push origin HEAD:main`，不得 force-push；若研究期間其他 Scout 已先推進 `origin/main` 而造成 non-fast-forward，僅讓本輪 fail closed，下一輪再從新的 remote head 重新開始。不得寫入 Hermes Wiki Brain、PyBroker、Nautilus、Paper、Testnet 或 Live workflow。
11. 若 **active isolated run worktree 本身**出現 unrelated dirt、merge/rebase conflict、repository sync failure、source/provenance failure、secret/public-safety 問題或 push failure，必須 fail closed。Separate coordinator checkout 的 dirt 本身不是 blocker，也不得被 stage、清理或帶入本輪。回報真正的 block，不得另外建立 fallback artifact。

Scheduled Scouts 與 ChatGPT Research Intake Review 是刻意分離的兩個流程。Scout 成功 push 只代表 research artifact 進入公開 staging pool，**不代表**已通過 Research Intake Review 或已進入 Wiki Brain。

**任何 Scout 都不得直接 promote 或寫入 Hermes Wiki Brain。** 所有 Wiki Brain ingestion 僅透過 ChatGPT Research Intake Review 進行。
