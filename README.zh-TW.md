# alpha-strategy-research

[English](README.md) | **繁體中文**

## 📌 新版 Hummingbot 單引擎研究設定（2026-11-10，規劃中）

**狀態：待技術驗證與部署，不代表現役回測流程已可執行。** 舊版 Qlib＋n8n＋Node01–13 流水線已退役；可沿用其研究基準，但不得把舊流程、績效認證或整合狀態當作目前已啟用。

- **策略來源：** `main` 僅收錄六門 `hb_ready_status: PASS`；PASS 是研究准入，不等於獲利、已有可執行策略或實盤授權。
- **Campaign 幣種（不是 HB_READY 白名單）：** `BTCUSDT`、`ETHUSDT`、`BNBUSDT`、`SOLUSDT`、`XRPUSDT`、`DOGEUSDT`、`LINKUSDT`。
- **時間框（不是 HB_READY 白名單）：** `1h`／`4h`／`1d`；Binance USDT-M 永續合約、逐倉、分別測 `3×`／`5×`，單策略研究階段不複利。
- **基礎覆蓋：** 每個凍結版本 `7 幣 × 3 週期 × 2 槓桿 = 42 組獨立測試`，不先乘參數搜尋域；每組使用可取得的完整歷史 K 線，不挑選有利區間。須先驗證 Hummingbot／Condor 對週期、資料、合約及帳務的實際支援，缺資料或不支援的組合必須明示。
- **可選且需揭露的 DCA 實驗：** Base `6%`＋Safety `6%`＋Safety `6%`（初始本金百分比），單策略最多 `18%`；2 次 Safety Order、金額倍率 `1.0`，加碼距離由研究定義。**不是 HB_READY 前置條件**；若改變來源策略交易事件，須另行明示衍生版本。
- **每輪鎖定的設定：** 初始 USDT 本金、來源及策略版本、引擎 image/commit、幣種／週期、資料起訖與可用時點、暖機、訊號／成交語意、手續費、滑價、Funding 假設及限制，並預查交易所最小下單與精度；不得把未知 Funding 假裝是零成本實測。
- **研究紀律：** 事前區分 IS 研究／選模與最終 OOS；OOS 前凍結版本、資料及切分。Hermes 每輪提出一組可證偽修正（迭代次數上限待核定），重新調度完整 Hummingbot 回測或淘汰；**不得用 OOS 結果回頭調參**。
- **調度方向：** Hermes 透過既有 Condor／Hummingbot MCP 連線（須對新安裝的引擎實測）操作 Hummingbot。每輪將假設、參數、逐筆事件、資金曲線、成本、績效、淘汰／修正原因沉澱至 Wiki Brain，並連結不可變的 GitHub 策略與版本；Wiki Brain 不取代策略版本來源。
- **績效晉級門檻：** 舊版 Qlib Campaign 記載 `年化淨報酬 ≥ 10%`、`Sharpe ≥ 1.0`；另曾討論 8% 目標。**新版 Hummingbot-only 門檻尚待核定**，不能將任一數字當作現役自動晉級規則，也不能放入 HB_READY 准入六門。
- [歷史雙引擎 v1.0 回測基準 →](docs/hb-backtest-baseline-v1.0.md) 與 [歷史視覺版 v0.1 →](docs/hb-backtest-baseline-v0.1.html) 僅供追溯，不作為新架構執行指令。

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

**PASS 即下游明確模型研究的准入，不是獲利、原論文績效重現、Qlib parity、Survivor 或 Paper／Testnet／Live 核准。** 淨收益與風險指標應在後續正式回測與 OOS 判斷，不能當 HB_READY 事前硬門檻。已驗引擎能力可重用；新的 execution primitive／data requirement 才在使用前做一次代表性驗證。這是工程能力檢查，不是第二次策略准入。

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

`implementation_status` 僅描述策略專用可執行成品，不決定 HB_READY 准入。`not-implemented` 不撤銷已獨立審查的 PASS。被選中的策略若缺少可重現的 Hummingbot 執行實作或設定綁定，應先補最小策略專用實作並驗證引擎／資料能力；這是工程缺口，不是自動淘汰或第二資格狀態。不得新增 `QLIB_READY`、第二准入 registry 或通用 Markdown→策略編譯器。原 Qlib／Node02–03 的說法僅屬歷史記錄。

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

`main` 僅保存**獨立 HB_READY 六門審查通過的 PASS 策略紀錄**；非 PASS 研究仍保留於既有非 main 分支、PR 或 Git 歷史。鎖定版本的 HB_READY 准入規範與既有審核自動化不變。

**新版下游研究閉環（尚待實測及部署）：**

```text
alpha-strategy-research/main（HB_READY PASS-only）
        ↓
Hermes 選策略、鎖定研究設定／資料／版本
        ↓
Hermes → 既有 Condor／Hummingbot MCP → Hummingbot 回測
        ↓
Hermes 分析交易事件／權益／成本／風險，同步寫入 Wiki Brain
        ↓
 淘汰／停止  |  提出一組可證偽修正  |  凍結 IS 候選策略
                      ↓                      ↓
             Hermes 再經 MCP 調度        單次最終 OOS
                      └──→ Hummingbot         ↓
                                          僅作研究判斷
```

**修正分支必須由 Hermes 經 MCP 再次回到 Hummingbot 回測。** Wiki Brain 在每一輪分析與修正同步沉澱經驗，但不得取代可重現的回測證據、GitHub 版本歷史與獨立 OOS 驗證。任何改變來源策略重要交易事件的研究修正，都須揭露為衍生策略／實驗，不得冒稱原生 PASS。

每輪應保存策略來源／commit、執行成品、凍結設定與 hash、Hummingbot 版本、資料來源與區間、IS/OOS 邊界、初始本金、幣種／週期／槓桿、可選 DCA、成交及成本假設、逐筆事件、權益曲線、績效、修正理由及結論。`42 組` 是每個凍結 baseline 的完整覆蓋，不是隱含全部調參組合；失敗或不支援的組合不能隱藏。

舊版 **Qlib 大量海選、n8n 調度、Node01–13 關卡、MLflow 證據與雙引擎逐筆一致性／認證流程已不再是現役執行要求**。歷史研究需保留來源標示，不得假稱為新版 Hummingbot 重現結果或認證。歷史 `10% / Sharpe 1.0` 與曾討論的 `8%` 門檻**尚未決定如何套用於新版**，自動晉級前需先核定指標與 OOS 規格；本規劃不授權 Testnet／Mainnet 或自動實盤。文件規劃不代表既有 MCP 或新裝的 Hummingbot 引擎已通過功能驗證；本次僅修改文件，不部署程式。

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
