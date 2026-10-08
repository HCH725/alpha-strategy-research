# alpha-strategy-research

[English](README.md) | **繁體中文**

## 📌 目前回測基準

**v1.0 研究 Campaign — 2026-10-05（不是 HB_READY 准入限制）**

- 目前 Campaign 幣種（不是 PASS 白名單）：`BTCUSDT`、`ETHUSDT`、`BNBUSDT`、`SOLUSDT`、`XRPUSDT`、`DOGEUSDT`、`LINKUSDT`
- 目前 Campaign 週期（不是 PASS 白名單）：`1h` / `4h` / `1d`
- 基礎矩陣：`7 幣 × 3 timeframe × 2 槓桿 = 42 cells`，尚未計入策略與 DCA 參數擴張
- 全量回測：每個 symbol × timeframe 使用當次 campaign 可取得的完整歷史 Kline，不 cherry-pick 行情
- 目前 Campaign DCA 實驗：Base Order `6%` + Safety Order `6%` + Safety Order `6%`，最大 `18%`；不是 HB_READY 前置條件。若改變來源交易事件，需建立明示衍生策略
- DCA 間距與策略參數由 Hermes 研究決定；最終 OOS 不得拿來回頭調參數
- Futures：Binance USDT-M perpetual、Isolated、分別測 `3×` / `5×`，單策略階段不複利
- 成本：Campaign 目標採 Binance non-VIP 費率與歷史 Funding；目前通用模擬器尚未證明歷史 Funding 計價實作，未驗證前不能宣稱已納入真實 Funding
- Engine：Hummingbot 是 canonical benchmark；Qlib 只有在逐筆事件對齊後才負責大量海選
- Promotion：Qlib 大量海選後，只有 survivor candidates 才交給 Hummingbot 逐筆復驗
- 第一層門檻維持 `ROI > 0`、`Sharpe ≥ 1.0`；績效統計語意以 Hummingbot benchmark 為準
- [Backtest Baseline v1.0 →](docs/hb-backtest-baseline-v1.0.md)
- [歷史視覺版 v0.1 →](docs/hb-backtest-baseline-v0.1.html)

這是一個公開的 canonical strategy-research corpus，保存標準化且有來源依據的策略研究紀錄。**HB_READY 六門引擎可表達資格**是每筆紀錄自己的狀態，不是保留在 `main` 的先決條件。

## 目前規則

自 **2026-10-08（UTC+8）** 更新六項准入條件；舊研究紀錄與 PASS 標記不自動重新分類：

- `main` 是 canonical strategy-research corpus，不是只收 PASS 的策略池。
- root-level strategy record 代表已正規化、具來源依據的研究；出現在 `main` 不會自動代表 HB_READY。
- 每筆紀錄以 `hb_ready_status: PASS | NOT_LOSSLESS | NOT_ASSESSED` 標示 HB_READY 狀態，應讀取此欄位判斷。
- 只有 `PASS` 紀錄可進入目前 Hummingbot/Qlib 績效研究下游。`NOT_LOSSLESS` 與 `NOT_ASSESSED` 仍是 `main` 上有效的研究紀錄，不得只因目前 Hummingbot 無法無損表達就丟棄。
- 排程 Scout 先篩選 HB_READY 候選，並維持同 repo 的 `research/*` 自動准入 PR；自動 Scout PR 必須是 `PASS` 才能 merge，`NOT_LOSSLESS` 候選仍會關閉。
- 重建或 legacy 研究紀錄走非 Scout branch，例如 `reconstruction/*` 或 `maintenance/*`，經獨立 provenance／研究審查後，即使狀態為 `NOT_LOSSLESS` 或 `NOT_ASSESSED` 也可 merge。它仍是一般 root-level strategy record，不會自動進入下游；branch 差異只區分流程，不區分內容類別。
- 歷史 survivor/Qlib 證據自然放在一般 Provenance 與 Evidence sections，並標示為歷史證據，不得寫成目前 Hummingbot 重現。同一策略家族的 survivor 變體原則上合併為一筆策略家族紀錄，附多筆歷史證據；除非證據證明 core mechanism 有實質差異。不需要特殊 survivor 資料夾、類別或標籤。
- 自動 Scout **不得直接把策略 push 到 `main`**。
- 對自動 Scout 准入而言，Hermes Auditor 的 GitHub Webhook Review 執行 HB_READY 六項門檻。若缺漏事實可由 primary source 明確查證，可在同一 PR branch 補正並重新審查；source 無法支持無損語意時，不得由此流程以 PASS merge。
- 通過的 Scout 策略 PR 才 squash merge 進 `main`。不另建 validated-strategy repo；下游 eligibility 由 `hb_ready_status: PASS` 決定，而非只看紀錄是否在 `main`。

完整 Reviewer 規則見 [`.github/HB_READY_REVIEW.md`](.github/HB_READY_REVIEW.md)。

### 目前鎖定的准入基準

目前自動 Scout HB_READY 准入依據：

- Hummingbot package：`20260920`
- Hummingbot VERSION：`dev-2.17.0`

未來 Hummingbot 更新，不代表 eligibility 自動放寬。只有在准入 contract 明確重新審查並更新後，才能使用新的 engine semantics。

## 這個 repo 代表什麼

本 repo 是標準化、具來源依據的策略研究 canonical corpus。root-level record 存在於 `main`，代表研究已按一般策略紀錄格式保存；單憑此事不代表 HB_READY。

每筆紀錄的 `hb_ready_status` 定義目前 engine expressibility：

- `PASS`：明確宣告的原始或衍生策略符合六項完整性、因果性及指定 Hummingbot 引擎相容要求；可進入目前 Hummingbot/Qlib 績效研究下游，不代表已驗 Qlib parity 或必然獲利。
- `NOT_LOSSLESS`：必要交易規則、資料或執行能力不完整、未驗證或與指定 Hummingbot 模型不相容；仍是 `main` 上有效研究，但不得進入該下游。
- `NOT_ASSESSED`：尚未完成目前六項 HB_READY 審查；仍是 `main` 上有效研究，但不得進入該下游。

不得只因目前 Hummingbot 無法無損表達，就丟棄非 PASS 紀錄。`PASS` **不代表**：

- 策略一定獲利；
- source-reported 績效已經被我們獨立重現；
- 策略已成為 survivor；
- 已通過 Hummingbot 或 Qlib 績效驗證；
- 已核准 Paper、Testnet、Mainnet 或任何 live trading。

除非後續流程明確改變狀態，所有紀錄仍維持 research-only。

## 目前流程

```text
公開 primary source
        ↓
排程 Scout（先篩選 HB_READY）
        ↓
research/<scout>-<slug>-<YYYYMMDD-HHMM>
        ↓
自動 Scout PR review
        ↓
PASS → exact-head squash merge；NOT_LOSSLESS → 關閉 Scout PR

legacy／重建研究
        ↓
reconstruction/* 或 maintenance/* PR
        ↓
獨立 provenance + 研究審查
        ↓
一般 root-level record（PASS / NOT_LOSSLESS / NOT_ASSESSED）

main = canonical strategy-research corpus
        ↓
目前 Hummingbot/Qlib 績效研究只取 PASS
```

自動 Scout 策略 PR 不允許永久停在 `REQUEST_CHANGES` 無人處理。非 Scout legacy／重建路徑採一般研究審查，不適用 Scout 自動關閉，也不會形成另一種紀錄類別。

## HB_READY 准入：六項必要條件

**取消四項獨立硬限制**：不再因「非單一交易對」、「不是 1h／4h／1d」、「訊號使用非 OHLCV 資料」、「不是同根收盤成交」就直接淘汰。這不表示 Hummingbot 自動支援全部模式；**第五項仍需以指定版本的真實執行與資料能力證明**。

可以是**原始策略**，也可以是**明確標示的衍生可執行策略**。衍生版保留獨立身分，透過現有 `Provenance`、`Signal`、`Execution assumptions` 與 `Limitations` 揭露來源及研究者自行定義的訊號、執行與風控差異；不能把衍生版 PASS 冒充原論文已重現。Reviewer 只能從可靠來源補正原始事實，不得暗中發明策略來救 PR。

每筆 `hb_ready_status: PASS` 必須符合下列六項：

### 1. 訊號可決定、可重現
完整揭露公式／模型、來源資料、指標版本、參數、平滑、比較、狀態切換與優先順序；ML 必須鎖定模型、前處理、訓練截止時間及推論當時已可用的特徵。不得猜測缺少的交易核心規則。

### 2. 交易方向明確
Long／Short 規則明確，或清楚停用其中一側；方向與標的／合約實際可交易性一致。

### 3. 進出場與風險完整
Entry、訊號出場／反向出場、SL、TP、Trailing Stop、Time Limit 或明確停用均有具體規則；不能依賴未揭露的 Hummingbot 預設行為。

### 4. 持倉、加碼、再進場完整
Pyramiding、同向持倉數量、Cooldown、再進場、DCA、資金及其他影響事件順序的狀態必須明確。統一 DCA 若會改變進出場，應列為研究者宣告的**衍生執行實驗**，不可稱為原始策略無損重現。

### 5. 指定版本引擎與資料、成本模型實際相容
依實際 Hummingbot image/commit、Controller、Executor、Connector、資料來源、訊號可用時點、成交與成本模型審查。市場可跨幣、週期可低於 1h、資料可非 OHLCV、成交可不是 Close，**前提是完整證明該路徑真的能模擬所有必要交易事件與經濟成本**；僅有 API／K 線間隔／Executor 名稱不算證明。不得虛構缺失價格或把未知 Funding 偷當零。來源忠實性只評估原生版；衍生版對自己完整宣告的規則負責，不能冒稱原文無損。

### 6. 預熱、資訊可用時間及因果性
Lookback、Warmup 必須可導出，禁止 Repainting、Future leak、未來極值、全樣本洩漏，以及在高週期 K 線結束前讀取其完整收盤訊號；成交順序與同根歧義需有明確且可模擬的定義。

**PASS 是可進入明確模型的績效研究，不是獲利、原論文績效重現、Qlib parity、Survivor 或 Paper／Testnet／Live 核准。** 淨收益與風險指標應在後續正式回測與 OOS 判斷，不能當 HB_READY 事前硬門檻。新執行路徑在啟用 Qlib 大量篩選前需要逐事件對齊，但不能強迫每份策略入庫前先做雙引擎回測。

六項任何一項不完整、不具證據或引擎不支援，Scout `research/*` PR 仍為 `NOT_LOSSLESS` 並說明原因後關閉；非 Scout 一般研究經獨立審查可用非 PASS 狀態保留 `main`。沿用三狀態及 `strategy-research-record-v1`，不新增資料夾或資格系統；既有 20 家族／92 筆歷史證據不得因刪除四項限制就自動變 PASS。

## GitHub Review 與自動補正

對自動 Scout `research/*` 准入 PR，Reviewer 只有在缺少／錯誤的資料能由 primary source 明確驗證時，才可以直接補正策略，例如：

- 公開 Pine / source code；
- immutable GitHub implementation；
- paper methods / tables / figures；
- 官方 first-party strategy documentation。

允許補正的例子：

- 漏掉的 indicator length；
- threshold；
- source price；
- timeframe；
- `process_orders_on_close`；
- pyramiding；
- explicit direction；
- source 明確定義的 stop / target；
- source 明確定義的 execution / cost assumption。

Reviewer **不可以**：

- 自己發明參數；
- 從幾種合理版本中自行挑一種；
- 自己加 stop / target / cooldown；
- 把 next-bar-open 改成 same-bar-close；
- 刪除不相容的資料依賴；
- 為了通過 HB_READY 而重新設計策略。

### 最終 Review 結果

`HB_READY: AUTO_REMEDIATED`

- Reviewer 只補 source 可以證實的資料；
- 只修改同一 PR branch 的 strategy file；
- commit 後停止；
- `synchronize` webhook 會觸發新的完整 review。

`HB_READY: PASS`

- 目前 immutable PR head 通過所有條件；
- 紀錄設定 `hb_ready_status: PASS`；
- Reviewer 留下 evidence；
- merge 必須鎖定 exact reviewed head SHA；
- squash merge 到 `main`。

`HB_READY: NOT_LOSSLESS`

- source 本身 underspecified、不相容，或需要自行發明策略；
- Reviewer 留下明確 blocker；
- 關閉自動 Scout `research/*` 准入 PR。

非 Scout legacy／重建策略紀錄使用非 `research/*` branch，並經獨立 provenance／研究審查；可用 `NOT_LOSSLESS` 或 `NOT_ASSESSED` merge，且不得自動進入下游。branch 差異不代表內容類別不同。README、文件、設定等 maintenance PR 也採一般 review，不會被 Scout HB_READY policy 自動 merge 或 close。

## Scout 規則

目前啟用中的自動研究：

- **ChatGPT TradingView HB-Ready Scout** — Asia/Taipei 每小時 `:14`；只研究 TradingView。
- **Hermes HB-Ready Quant Research Scout** — Asia/Taipei 每小時 `:35`；研究較廣泛的公開來源。

Antigravity 與 MiMo 的自動策略研究目前維持停用。

每輪 Scout：

1. 先讀最新 `README.md` 與 `.github/HB_READY_REVIEW.md`；
2. 查看目前 `main`；
3. 同時對 `main` 與 open `research/*` PR 做 dedup；
4. 直接讀 primary source；
5. 先篩選 HB_READY 候選，再用六項條件審查，不能恢復已取消的市場／週期／資料／時序固定禁令；
6. 每輪最多建立 **1 個** candidate PR；
7. 自動 Scout PR 只有 `hb_ready_status: PASS` 才能 merge；`NOT_LOSSLESS` 候選會關閉；
8. 找不到合格候選時，0 筆就是成功；
9. 不得為了 cadence 降低門檻。

### PR-only 寫入規則

Scout 找到一筆合格候選時：

1. 在同一 repo 建立 `research/*` branch；
2. branch 名應保持唯一，通常包含 Scout、strategy slug 與 Asia/Taipei timestamp；
3. 只新增 **1 個** root-level strategy Markdown；
4. 不得夾帶無關修改；
5. 開 PR 到 `main`；
6. 驗證 PR 後停止。

Scout 不可以：

- 直接 push strategy 到 `main`；
- 自己 approve；
- 自己 merge；
- 自己 close；
- 繞過 GitHub Review；
- 寫入 Hummingbot、Qlib、n8n、survivor、Paper、Testnet 或 Live 系統。

## 公開來源規則

可使用的來源包含：

- TradingView 公開 strategy / idea / script；
- GitHub implementations；
- FMZ；
- papers / preprints；
- 高品質公開研究；
- 公開技術文件。

下列來源應跳過：

- private；
- paid-only / invite-only；
- 無法取得實際規則；
- 純行銷內容；
- 沒有 reconstructable rules 的 generic explainer；
- materially underspecified strategy source。

### Provenance

GitHub source 必須保存：

- repository URL；
- full commit SHA；
- exact file path；
- relevant source URL。

TradingView 必須保存 stable public URL 與 source/as-of date。可以讀公開 Pine/source logic，但不要把大量 copyrighted source code 複製進 repo。

Paper 的 quantitative claim，應盡量保留 stable paper identity、version/date，以及 exact Table/Figure/Section provenance。

## Dedup

開 PR 前必須搜尋目前 `main` 與 open `research/*` PR。

相同 canonical source identity + materially identical normalized rule，不得重複建 candidate。

exact duplicate、paraphrase、trivial parameter variant 都不算新策略。

只有當同一來源真的包含 materially distinct 的 mechanism、signal construction、market/universe、horizon/regime 或 material data dependency，才有理由形成另一筆獨立紀錄。

同一策略家族的 survivor 變體通常應合併成一筆策略家族紀錄，並在一般 Evidence section 保留多筆歷史證據；除非證據證明 core mechanism 有實質差異。歷史 survivor/Qlib 證據放在一般 Provenance／Evidence sections，標示為歷史證據，不得稱為目前 Hummingbot 重現。不需要特殊 survivor 資料夾、類別或標籤。

## Strategy record schema

目前使用：

```yaml
schema: strategy-research-record-v1
```

Schema 維持 `strategy-research-record-v1`；`hb_ready_status` 是新增欄位，不是 schema version 變更。

Required frontmatter：

```yaml
---
schema: strategy-research-record-v1
hb_ready_status: PASS | NOT_LOSSLESS | NOT_ASSESSED
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
  - <traceable public source>
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---
```

`confidence` 代表我們對 research interpretation 的信心，不代表預期獲利能力。

### Required document structure

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

如果某項資料無法取得，保留 section 並明確標記，不要把 required section 刪掉。

新研究一般應寫：

```text
Not independently reproduced.
```

除非真的已完成獨立重現。

### 策略關鍵缺口

若 `hb_ready_status` 是 `NOT_LOSSLESS` 或 `NOT_ASSESSED`，研究紀錄可以保留 strategy-critical gap；仍有此類缺口時不得標記為 `PASS`。自動 Scout 准入仍要求 PASS，並會關閉 NOT_LOSSLESS 候選。

例如：

- indicator length 不明；
- threshold 不明；
- entry timing 模糊；
- exit rule 模糊；
- direction 不明；
- pyramiding / re-entry 在會影響結果時不明；
- execution convention 會改變交易 timing；
- 需要 unsupported data。

對自動 Scout 准入，這類候選必須先從 primary source 補齊才可標記 PASS；否則該 Scout PR 會以 `NOT_LOSSLESS` 關閉。一般非 Scout 研究紀錄經獨立審查後可在 `main` 保留缺口，但必須使用非 PASS 狀態。

## File naming

使用 lowercase、hyphen-separated、無空白檔名。

建議：

```text
<strategy-or-topic-slug>-<YYYY-MM-DD>.md
```

不要使用 `latest`、`final`、`new` 這類模糊 suffix。

## Downstream 邊界

這個 repo 只負責：

> **research normalization + 明確的逐筆 HB_READY status**。自動 Scout lane 只准入 PASS；其他有來源依據的研究可經一般獨立審查後保留在 `main`。

目前預期的 downstream：

```text
alpha-strategy-research/main
        ↓
篩選：hb_ready_status == PASS
        ↓
標準化 research execution overlay
(DCA: 6% + 6% + 6%、Isolated、3× / 5×)
        ↓
Qlib 大規模海選
        ↓
survivor candidates
        ↓
未來的新 Survivor Repo
        ↓
Hummingbot 復驗
        ↓
逐筆 event-level parity
        ↓
Formal Survivor
        ↓
後續 Testnet / live qualification
```

Hummingbot 是 canonical backtest / execution semantics benchmark。Qlib 大量海選前，必須針對**明確宣告的原始或衍生策略**、資料、執行成本與鎖定假設完成逐筆事件一致驗證；不要求每筆策略入庫前都先做 Qlib 回測。

對 PASS 紀錄而言，HB_READY 審查的是該筆**原生或明示衍生的可執行規則**與鎖定版 Hummingbot 的相容性，而非獲利或來源忠實性一律成立。DCA／capital／leverage 是下游研究 Campaign 的獨立實驗，**不是 HB_READY 准入必要條件**；若加入 DCA 改變原始 trade events，就必須另列完整衍生策略及證據，不可把新交易行為冒充原文。

Parity 不是看最終 ROI 或 Sharpe 接近就算通過。Signal、entry / exit 時間、方向、價格、相同 house overlay 下的 position size、Safety Orders 與 close transition 都必須逐筆一致。

**目前 README 不宣稱 repo → Hummingbot/Qlib 的自動執行 bridge 已經啟用。** 新的 Survivor Repo 也尚未建立；正式大量海選需等 Hummingbot ↔ Qlib parity 完成後才恢復。

舊的 Research Intake Review → Wiki ingestion → preparation backlog → n8n → Qlib-first 自動流程已 deprecated，不再是目前 admission 或 execution contract。

## Public repo hygiene

這是 public repository。

不得 commit：

- credentials、tokens、API keys、secrets；
- private account / wallet / portfolio；
- private chats；
- paid/private research；
- 本機 secrets 或 private Hermes config；
- 不適合再散布的 copyrighted source material。

應以 normalize + cite 的方式保存策略，不要直接大量複製 source passages。

## 核心原則

這個 repo 應保持簡單：

> **若 `hb_ready_status: PASS`，代表策略通過六項指定引擎可表達性審查（非已完成 Qlib parity 或實盤驗證）；單純存在於 `main` 只代表研究得以保存。**

這就是本 repo 現在的用途。
