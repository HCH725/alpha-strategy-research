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
- Qlib Research Survivor → Hummingbot 首輪硬門檻：同一 run／樣本的 `Annualized Net Return ≥ 10%` 與 `Sharpe ≥ 1.0`；`Net Strategy ROI` 只保留報表，不再是獨立硬門檻。這是下游績效標準，不是 HB_READY 六門准入條件
- 年化淨報酬採同一 canonical Hummingbot 模型下扣除可驗證手續費、滑價與資金成本的完整資金曲線；評估期間從暖機後可產生第一個合法訊號起，到預定 end，固定且連續、包括空倉時間，不得從第一筆贏利交易才算。無效 run 排除、保留指標與尚待驗證的統計實作邊界見 v1.0
- [Backtest Baseline v1.0 →](docs/hb-backtest-baseline-v1.0.md)
- [歷史視覺版 v0.1 →](docs/hb-backtest-baseline-v0.1.html)

**Alpha Research 的 `main` 是 HB_READY 六門 PASS-only 策略池。** 非 PASS 歷史研究保留在同 Repo 的非 main 分支、PR 或 Git 歷史，不以改標 PASS 方式湊數。

## 目前規則

**2026-10-08 起正式改為 `main` 100% HB_READY PASS，歷史重建與人工合併均無例外。**

- `main` 每一筆根目錄策略 Markdown（不包含 `README.md`、`README.zh-TW.md`）的 frontmatter 必須是經獨立六門審核的 `hb_ready_status: PASS`；缺失、`NOT_LOSSLESS`、`NOT_ASSESSED` 或未完成審查者全部不得 Merge。
- `NOT_LOSSLESS`／`NOT_ASSESSED` 仍是合法的**審查結果**，但只可留在 PR、非 `main` 分支或既有 Git 歷史；保留研究，不得為了達標假造 PASS。
- 每小時 Scout 仍透過 `research/*` 提交單筆策略，只有六門 PASS 可 Merge；來源可驗證的缺漏可於同一 PR 修復再重審，無法補正則關閉該 Scout PR。
- **撤銷歷史策略與非 Scout PR 的准入例外**：`reconstruction/*` 等凡新增／修改策略者，同樣必須通過六門 PASS；不合格的保留分支或 PR，不得合併 `main`。目前 PR #58 的非 PASS 策略不可原樣合併。
- 文件、設定與維護 PR 仍採 COMMENT-only Review，不自動合併，但也不能藉維護 PR 偷渡非 PASS 紀錄。移出舊非 PASS 前須先確認可回溯的 Git Branch／歷史。
- 已有三筆非 PASS（AEAP／SEADS、QuantaAlpha、Wasserstein）事先保存在同一 Repo 的 `archive/non-pass-research-20261008` 分支；PR #58 的 17 家族仍在未合併分支。不新增 Repo、資料夾、資格狀態或額外流程。
- `main` 全數 PASS 只代表策略規則與指定 Hummingbot 模型經 HB_READY 准入審查，**不代表**已驗證獲利、Qlib parity、歷史 Survivor 績效或交易權限。README PASS 數量應等於 `main` 策略總數。

詳細規範：[.github/HB_READY_REVIEW.md](.github/HB_READY_REVIEW.md)。

### 目前鎖定的准入基準

目前自動 Scout HB_READY 准入依據：

- Hummingbot package：`20260920`
- Hummingbot VERSION：`dev-2.17.0`

未來 Hummingbot 更新，不代表 eligibility 自動放寬。只有在准入 contract 明確重新審查並更新後，才能使用新的 engine semantics。

## 這個 Repo 與審核流程

`main` 只放具獨立六門審查證據的 `hb_ready_status: PASS` 策略。PASS 代表該筆原始或明示衍生策略可依指定版本 Hummingbot 模型因果地表達；不是獲利、Qlib parity 或實盤授權。

流程：公開來源 → `research/*` 或 `reconstruction/*` 候選 PR → 六門獨立 Audit → **只有 PASS 可合併 `main`**。其餘研究保留在既有 Archive Branch、PR 或歷史中，不進 `main`。文件／維護 PR 仍是 COMMENT-only，不得繞過 PASS-only 規則。已存在的 PASS 紀錄不因本次改動重新標記，但若有新的錯誤證據仍須另行重審。

所有策略仍維持 `status: research-only`、`adoption: not-approved`。

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

六門任何一項不完整、缺證據或引擎不支援，**無論 Scout、歷史重建、非 Scout 或人工 PR，策略都不得進入 `main`**。Scout 未通過者關閉 PR；其他研究可保留非 main 分支／PR。沿用三種審查結果與 `strategy-research-record-v1` 格式，不額外建立資格系統；20 家族／92 筆歷史研究不能自動升級 PASS。

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

非 Scout／legacy／重建策略 PR 同樣需要獨立六門 HB_READY PASS 才能 merge 到 `main`。非 PASS 僅留非 main 分支或 PR；maintenance／文件 PR 維持 COMMENT-only，但仍須符合 main 100% PASS 的完整性檢查。

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

非 main 的草稿或歸檔研究可使用 `NOT_LOSSLESS`／`NOT_ASSESSED` 保留策略缺口；**main 不得保留這類未通過的紀錄**。Scout 不合格者仍關閉 PR。

例如：

- indicator length 不明；
- threshold 不明；
- entry timing 模糊；
- exit rule 模糊；
- direction 不明；
- pyramiding / re-entry 在會影響結果時不明；
- execution convention 會改變交易 timing；
- 需要 unsupported data。

所有策略 PR 都須先有可靠來源補證或獨立明示衍生策略的完整規則，達六門 PASS 才能進 `main`。Scout 不能補正者以 `NOT_LOSSLESS` 關閉；一般研究可留在非 main 分支。

## File naming

使用 lowercase、hyphen-separated、無空白檔名。

建議：

```text
<strategy-or-topic-slug>-<YYYY-MM-DD>.md
```

不要使用 `latest`、`final`、`new` 這類模糊 suffix。

## Downstream 邊界

這個 repo 的 `main` 只保存**經獨立 HB_READY 六門審查的 PASS 策略紀錄**。任何未完整審查／非 PASS 研究只能保留在非 main 分支、PR 或既有 Git 歷史，不得合併進 `main`。

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
Annualized Net Return ≥ 10% 且 Sharpe ≥ 1.0
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

> **main 上每個策略都必須經獨立 HB_READY 六門審查為 PASS。歷史重建／人工合併不再享有豁免；PASS 並非已證明獲利、Qlib parity 或實盤授權。**

這就是本 repo 現在的用途。
