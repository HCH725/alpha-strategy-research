# alpha-strategy-research

[English](README.md) | **繁體中文**

## 📌 目前回測基準

**v1.0 — 2026-10-05**

- Universe：`BTCUSDT`、`ETHUSDT`、`BNBUSDT`、`SOLUSDT`、`XRPUSDT`、`DOGEUSDT`、`LINKUSDT`
- Timeframes：`1h` / `4h` / `1d`
- 基礎矩陣：`7 幣 × 3 timeframe × 2 槓桿 = 42 cells`，尚未計入策略與 DCA 參數擴張
- 全量回測：每個 symbol × timeframe 使用當次 campaign 可取得的完整歷史 Kline，不 cherry-pick 行情
- House execution overlay：所有績效研究策略都使用 Base Order `6%` + Safety Order `6%` + Safety Order `6%`，單策略最大 `18%`
- DCA 間距與策略參數由 Hermes 研究決定；最終 OOS 不得拿來回頭調參數
- Futures：Binance USDT-M perpetual、Isolated、分別測 `3×` / `5×`，單策略階段不複利
- 成本：鎖定 Binance 一般 non-VIP USDⓈ-M 手續費，Funding 使用歷史實際值
- Engine：Hummingbot 是 canonical benchmark；Qlib 只有在逐筆事件對齊後才負責大量海選
- Promotion：Qlib 大量海選後，只有 survivor candidates 才交給 Hummingbot 逐筆復驗
- 第一層門檻維持 `ROI > 0`、`Sharpe ≥ 1.0`；績效統計語意以 Hummingbot benchmark 為準
- [Backtest Baseline v1.0 →](docs/hb-backtest-baseline-v1.0.md)
- [歷史視覺版 v0.1 →](docs/hb-backtest-baseline-v0.1.html)

這是一個公開的 canonical strategy-research repository，只保存已通過目前 **LOSSLESS HB_READY** GitHub 准入審查的策略研究紀錄。

## 目前規則

自 **2026-10-05（UTC+8）** 起：

- `main` 是正式准入後的 canonical strategy pool。
- 只要 root-level strategy Markdown 存在於 `main`，就代表已通過目前 Hummingbot 語意下的 **LOSSLESS HB_READY** GitHub Review。
- 自動 Scout **不得直接把策略 push 到 `main`**。
- 所有新策略一律先進 same-repository 的 `research/*` PR。
- OpenCode GitHub Review 就是 admission gate。
- 如果缺少的是 primary source 可以明確查到的事實，Reviewer 可以直接補正同一個 PR branch，再觸發重新審查。
- 如果 source 本身不足以形成完整、無損的策略規則，PR 直接關閉。
- 通過的策略 PR 才 squash merge 進 `main`。
- 不另外建立 validated-strategy repo，merge 後也不再做第二次「這策略能不能給 Hummingbot」的語意適用性審查。

完整 Reviewer 規則見 [`.github/HB_READY_REVIEW.md`](.github/HB_READY_REVIEW.md)。

### 目前鎖定的准入基準

現行策略准入依據：

- Hummingbot package：`20260920`
- Hummingbot VERSION：`dev-2.17.0`

未來 Hummingbot 更新，不代表 eligibility 自動放寬。只有在准入 contract 明確重新審查並更新後，才能使用新的 engine semantics。

## 這個 repo 代表什麼

本 repo 現在刻意維持很窄的職責。

策略只要存在於 `main`，代表：

> 來源策略的規則已完整、因果關係明確，而且目前 pinned Hummingbot backtester 可以在**不做 material approximation** 的前提下 1:1 表達。

這**不代表**：

- 策略一定獲利；
- source-reported 績效已經被我們獨立重現；
- 策略已成為 survivor；
- 已通過 Hummingbot 或 Qlib 績效驗證；
- 已核准 Paper、Testnet、Mainnet 或任何 live trading。

所有正式准入紀錄仍維持 research-only，除非後續流程明確改變其狀態。

## 目前流程

```text
公開 primary source
        ↓
ChatGPT / Hermes Scout
        ↓
research/<scout>-<slug>-<YYYYMMDD-HHMM>
        ↓
GitHub Pull Request
        ↓
OpenCode LOSSLESS HB_READY Review
        ├─ 缺的是 source 可查證事實
        │      ↓
        │  補正同一 PR branch
        │      ↓
        │  synchronize → 重新 review
        │
        ├─ HB_READY: PASS
        │      ↓
        │  exact-head squash merge
        │
        └─ HB_READY: NOT_LOSSLESS
               ↓
             close PR
        ↓
main = canonical HB_READY strategy pool
```

自動策略 PR 不允許永久停在 `REQUEST_CHANGES` 無人處理。

## LOSSLESS HB_READY 硬門檻

每一筆正式准入的策略，都必須符合所有適用條件。

### 1. 市場結構

- 每次回測只處理一個 trading pair；
- spot / perpetual 適用性必須由 primary source 明確指出，或能從來源確定判讀；
- 不接受 cross-sectional ranking；
- 不接受 pair spread；
- 不接受跨 symbol 共用 portfolio capital 的策略；
- 不接受 multi-pair shared state；
- spot 策略不得需要 naked short。

### 2. 時間框

- 目前 decision timeframe 必須是 `1h`、`4h` 或 `1d`；
- 現階段 Scout 應優先收 single decision timeframe；
- multi-timeframe 不屬一般 Phase-1 lane，除非能證明 causal alignment 完整且不改變 source semantics。

### 3. 資料依賴

核心交易訊號必須能由目前 Hummingbot backtester 可取得的 candle data 計算：

- OHLCV；
- 由 candle deterministic、causal 地衍生的 indicators。

如果策略 edge 必須依賴下列資料，現階段不得准入：

- funding；
- open interest；
- mark / index price；
- liquidation feed；
- trade / aggressor feed；
- L2 / order book；
- on-chain；
- options / IV / Greeks；
- sentiment / news；
- macro data；
- cross-venue state。

### 4. 訊號必須 deterministic

所有會影響交易的規則，都要完整到讓兩個不同實作者可以產生同一份 causal signal logic。

依策略需要，必須明確保存：

- indicator / formula variant；
- source price；
- lookback；
- smoothing；
- threshold；
- crossover / comparison semantics；
- AND / OR 邏輯；
- state transition；
- conflict priority。

策略關鍵參數缺失時，不得自行發明。

### 5. Direction

- long 與 short 規則都要明確；或
- 明確標示其中一側 disabled。

### 6. Entry / Exit / Risk

來源策略所有適用行為都必須明確：

- entry；
- signal exit；
- opposite-signal exit；
- stop loss；
- take profit；
- trailing stop；
- time limit；
- no-exit / disabled。

不得依賴 Hummingbot silent defaults。

### 7. Execution timing

目前 LOSSLESS 准入必須相容：

```text
completed bar
    ↓
signal decision
    ↓
same-bar close execution
```

現階段不接受 materially 依賴：

- next-bar-open；
- maker-touch / queue；
- intrabar path ordering；
- 其他目前 pinned Hummingbot backtester 無法 1:1 重現的 fill convention。

不得拿 close 去近似 next-open。

### 8. Position / Re-entry / Gating

只要會影響交易，都必須明確，或能證明對結果無關：

- sizing；
- fixed vs compounding；
- pyramiding / repeated entry；
- max same-side concurrency；
- cooldown；
- re-entry。

如果模糊處可能改變 trade count、timing、direction 或 amount，就不是 LOSSLESS。

### 9. Cost / Engine model 相容性

策略 edge 不能 materially 依賴目前 backtester 無法 lossless 模擬的行為，例如：

- maker / taker asymmetry；
- spread capture；
- queue priority；
- partial fills；
- unsupported slippage / impact；
- funding PnL；
- liquidation / margin mechanics；
- 目前 backtester 無法重現的 leverage effect。

如果 source 沒有說明 cost model，而且成本不是 signal 或 trade-sequence semantics 的一部分，可以明確標記 data gap。之後使用的 benchmark fee 是 runtime assumption，不得冒充 source-reported strategy rule。

### 10. Warmup / Causality

- 所有 indicator lookback 都要已知，才能推導 warmup；
- 不得 repaint；
- 不得 future-bar reference；
- 不得用 negative shift 取得未來資訊；
- 不得 future extrema；
- 不得 full-sample normalization 造成 future leakage；
- 不得有其他 look-ahead leakage。

### 准入原則

只要**任何 material strategy rule 需要 approximation、自己補創語意、或仍有 unresolved interpretation**，就是 `NOT_LOSSLESS`，不得 merge。

## GitHub Review 與自動補正

Reviewer 只有在缺少／錯誤的資料能由 primary source 明確驗證時，才可以直接補正 PR，例如：

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
- Reviewer 留下 evidence；
- merge 必須鎖定 exact reviewed head SHA；
- squash merge 到 `main`。

`HB_READY: NOT_LOSSLESS`

- source 本身 underspecified、不相容，或需要自行發明策略；
- Reviewer 留下明確 blocker；
- close PR。

README、文件、設定等 maintenance PR 不屬於 strategy admission PR。它們只做一般 review，不會被 HB_READY strategy policy 自動 merge 或 close。

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
5. 寫入前先套用 LOSSLESS HB_READY hard gate；
6. 每輪最多建立 **1 個** candidate PR；
7. 找不到合格候選時，0 筆就是成功；
8. 不得為了 cadence 降低門檻。

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

## Strategy record schema

目前使用：

```yaml
schema: strategy-research-record-v1
```

Required frontmatter：

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

研究紀錄可以保留非關鍵 provenance limitations，但正式准入策略不能留下 unresolved strategy-critical gap。

例如：

- indicator length 不明；
- threshold 不明；
- entry timing 模糊；
- exit rule 模糊；
- direction 不明；
- pyramiding / re-entry 在會影響結果時不明；
- execution convention 會改變交易 timing；
- 需要 unsupported data。

這類候選必須先從 primary source 補齊，否則 close 為 `NOT_LOSSLESS`。

## File naming

使用 lowercase、hyphen-separated、無空白檔名。

建議：

```text
<strategy-or-topic-slug>-<YYYY-MM-DD>.md
```

不要使用 `latest`、`final`、`new` 這類模糊 suffix。

## Downstream 邊界

這個 repo 只負責：

> **research normalization + HB_READY admission**

目前預期的 downstream：

```text
alpha-strategy-research/main
        ↓
HB_READY core strategy semantics
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

Hummingbot 是 canonical backtest / execution semantics benchmark。Qlib 只有在兩個 engine 已經針對同一份 data、strategy、parameters、DCA overlay、capital setup 與 costs 證明逐筆事件一致後，才作為大量海選引擎。

HB_READY 保留來源策略的 core signal 與 causal semantics。所有策略都會在下游績效研究階段套上我們明確的 **DCA / capital / leverage research execution overlay**；這層不能被誤寫成來源策略原生的行為。

Parity 不是看最終 ROI 或 Sharpe 接近就算通過。Signal、entry / exit 時間、方向、價格、position size、Safety Orders 與 close transition 都必須逐筆一致。

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

> **只要 strategy record 在 `main`，downstream 就可以信任它已通過目前 LOSSLESS HB_READY source-semantics admission。**

這就是本 repo 現在的用途。
