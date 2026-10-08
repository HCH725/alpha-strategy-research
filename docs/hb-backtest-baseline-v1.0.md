# Hummingbot / Qlib Backtest Baseline v1.0

Effective: 2026-10-05 (UTC+8)

這份文件是目前**單策略量化研究 Campaign** 的 v1.0 execution target，不是 HB_READY 准入的市場／週期／資料／成交方式硬門檻。2026-10-08 六項 HB_READY 規範見 [Review Contract](../.github/HB_READY_REVIEW.md)。文件描述的目標能力必須經 pinned simulator 實測，不能把規劃視為實作已完成；不新增 pipeline、optimizer、manager 或治理層。

## 0. Big picture

Hummingbot 是 execution / backtest semantics 的 canonical benchmark。

Qlib 的定位是大量海選引擎。只有在 Qlib 與 Hummingbot 已經證明逐筆交易事件一致之後，Qlib 的大規模結果才可以被信任。

目前 intended flow：

```text
alpha-strategy-research
        ↓
HB_READY strategy
        ↓
standardized research overlay
        ↓
Qlib large-scale screening
        ↓
Annualized Net Return ≥ 10% AND Sharpe ≥ 1.0
        ↓
survivor candidates
        ↓
future Survivor Repo
        ↓
Hummingbot re-validation
        ↓
event-level parity confirmed
        ↓
Formal Survivor
        ↓
Testnet / later live workflow
```

這個 repo 的 `main` 只保存經獨立 HB_READY 六門審查的 PASS 策略；非 PASS 研究保留在既有非 main 分支、PR 或 Git 歷史。上面的 execution flow 是下游 contract，不代表自動 bridge 已經啟用。

## 1. House rule: every strategy uses DCA Safety Orders

本文件定義目前**選定 Campaign 的 DCA 研究實驗**；DCA 不是 HB_READY 准入條件。若加入 DCA 改變原來源策略交易事件，該執行方式須作為**獨立揭露的衍生策略／研究實驗**，不可稱 source-native 無損。

固定結構：

- Base Order = 初始本金的 6%
- Safety Order 1 = 初始本金的 6%
- Safety Order 2 = 初始本金的 6%
- 單策略最大配置 = 初始本金的 18%
- Safety Order 數量 = 2
- Safety Order 金額倍率 = 1.0（目前不做倍增）
- Margin mode = Isolated
- Leverage = 3× 與 5× 分開測
- 單策略階段不使用複利

### DCA spacing 是研究變數

Safety Order 的觸發距離不是預先固定的 house number。

Hermes 在研究每個策略時，依據該策略、幣種、timeframe、波動特性與市場條件提出合理的 DCA 參數研究空間，再依標準量化流程進行驗證。

這個 DCA overlay 是我們明確的 benchmark execution rule，不應被誤寫成 source-native strategy semantics。

## 2. Full-history research + standard OOS discipline

「全量回測」代表：

> 對每一個 symbol × timeframe，使用該回測 campaign 當下可取得的完整歷史 Kline 範圍，不 cherry-pick 特定行情區間。

完整歷史資料的使用仍必須遵守一般專業量化研究標準：

- 研究 / 選參數資料與最終 OOS 資料必須分離；
- 最終 OOS 不得被拿來回頭調參數；
- chronological split、validation 或 walk-forward 的具體方式，依資料長度與研究需求決定；
- 一旦該 campaign 開始，切分規則必須先固定，不能看完結果後才改。

本 repo 不硬編一個主觀的 70/30 或固定年份切法。

## 3. Strategy parameters and DCA parameters are research-defined

不先人工指定「最佳參數」。

Hermes 依下列條件提出研究空間：

- 策略原理；
- indicator 特性；
- symbol；
- timeframe；
- volatility；
- DCA behavior。

參數搜尋必須遵守：

- 不改寫策略核心因果邏輯；
- 在看到最終 OOS 成績前先決定研究空間與搜尋方法；
- 研究目標是找穩定區域，不是只找單一歷史最佳點；
- 不得因 OOS 不漂亮而事後擴張、縮窄或重定義搜尋空間來救結果。

## 4. Capital and transaction-cost model

### Capital

資金配置以初始本金百分比表示：

- 6% / 6% / 6%
- 單策略最大 18%
- 單策略階段不複利

絕對 USDT 本金屬每個 campaign 的 runtime input，必須在 run manifest 中 pin 住，並通過 Binance 的 min notional / min qty / step size 可成交性 preflight。不得因交易所最小下單限制而靜默漏單。

### Trading fees

使用該回測 campaign 所鎖定之 Binance USDⓈ-M Futures 一般普通用戶（non-VIP）標準手續費表。

每輪 campaign 必須把實際使用的 maker / taker rate 明確寫入 manifest；不自行美化或折扣成本。

### Funding

**Campaign 目標**是依正負方向、實際時間點使用 Binance USDT-M perpetual 歷史 Funding Rate；但目前 pinned Hummingbot V2 通用 backtesting simulator 尚未證明此項已實作。未經完整實作／測試前，不能宣稱正式績效已含歷史 Funding，也不得靜默以 0 取代。涉及 Funding 的策略須由六門中的引擎／成本相容門逐案判斷。

### Other execution semantics

slippage、rounding、margin、liquidation 及其他 execution semantics 以 Hummingbot 能實際重現的語意作 canonical reference，Qlib 必須跟隨同一規則。

## 5. Hummingbot ↔ Qlib parity is a hard prerequisite

Hummingbot 是 benchmark engine。

對同一份：

- Kline data
- strategy
- strategy parameters
- DCA overlay
- capital setup
- fee / funding assumptions

Qlib 與 Hummingbot 必須逐筆比對：

- signal timestamp
- entry timestamp
- entry price
- direction
- position size
- Safety Order 1
- Safety Order 2
- exit timestamp
- exit price
- position transition / close behavior

只有 event-level parity 才算引擎對齊。

> 最終 ROI、Sharpe、MDD 很接近，但 trade events 不一致，仍然算 **NOT ALIGNED**。

績效指標的 canonical semantics 也以 Hummingbot benchmark 為準；Qlib 的 ROI、Sharpe、MDD、trade count 等統計必須在同一事件流與同一成本模型上對齊。

在 parity 完成以前，不恢復正式的大規模 Qlib survivor production flow。

## 6. Base research matrix = 42 cells before parameter expansion

目前**Campaign** universe（非 HB_READY 准入白名單）：

- BTCUSDT
- ETHUSDT
- BNBUSDT
- SOLUSDT
- XRPUSDT
- DOGEUSDT
- LINKUSDT

目前**Campaign** timeframes（非 HB_READY 准入白名單）：

- 1h
- 4h
- 1d

Leverage：

- 3×
- 5×

所以每一個策略在尚未加入策略參數與 DCA 參數搜尋以前，最基本就是：

```text
7 symbols × 3 timeframes × 2 leverage settings = 42 base cells
```

每個 cell 都是獨立研究單元。

加入 strategy parameters 與 DCA parameters 後，run 數量可以快速擴大；這正是 Qlib 被用來做大量海選的原因，而不是異常。

## 7. Qlib screens; Hummingbot re-validates survivors

不要求每一個 Qlib candidate 都同步再跑一次 Hummingbot。

正式 intended sequence：

1. 先完成 Hummingbot ↔ Qlib engine parity。
2. Qlib 負責大量參數 / DCA / symbol / timeframe / leverage 海選。
3. 同一 run／樣本同時符合 `Annualized Net Return ≥ 10%` 與 `Sharpe ≥ 1.0` 的少量 survivor candidates 進入未來的 Survivor Repo；`Net Strategy ROI > 0` 不再是獨立硬門檻。
4. 只有這些 survivor candidates 再交給 Hummingbot 獨立重跑。
5. Hummingbot 與 Qlib 必須再次驗證逐筆 trade events 一致。
6. 一致後才可標成 Formal Survivor。
7. Formal Survivor 才能進後續 Testnet / live qualification workflow。

目前尚未建立新的 Survivor Repo；在兩個 engine parity 完成前，不需要急著建立或恢復舊 survivor production flow。

### 首輪績效門檻與統計口徑（2026-10-09 修訂）

上述兩項門檻只用於 **Qlib Research Survivor → Hummingbot 首輪績效篩選**，不加入 HB_READY 六項入庫審查，不改既有 PASS 狀態或 review gate。最終 OOS 不得用來調參或事後改動評估期間。

`Annualized Net Return` 必須基於同一 canonical Hummingbot 模型下，扣除可驗證手續費、滑價與資金成本後的**完整資金曲線**。使用固定、連續的可交易評估期間：從暖機完成後可產生第一個合法訊號的時點，到預先固定的 end；包括空倉／未交易時段，不得改從首次成交或第一筆贏利交易開始。與 Sharpe 必須是同一 run、樣本、成本模型及評估期間；run manifest 應鎖定指標公式、取樣頻率、年化慣例及 Sharpe 口徑，避免跨引擎同名異義。

無交易、起始權益為零／負值、無法確定評估期間，或成本未驗證的 run，均不得宣稱通過上述 Survivor 績效門檻；不得用零成本假設或局部交易收益冒充可驗證的年化淨報酬。報表仍保留 `Net Strategy ROI`（總淨 ROI）、MDD、PF、Sortino，以及年化淨報酬與 Sharpe。

這是**規劃中的統計 contract，不是已部署的指標實作**。年化淨報酬與 Sharpe 的公式／語意仍須在 pinned engine 上驗證；目前未驗證的歷史 Funding 等成本不得視為已納入。本次只有文件修訂，不啟動引擎、部署 pipeline 或新增執行 gate。

## 8. Run reproducibility

每個正式回測 campaign 至少保存：

- strategy file / commit identity
- Hummingbot version / commit
- Qlib version / commit
- data as-of 與實際 start / end
- symbol / timeframe
- leverage
- strategy parameters
- DCA parameters
- initial capital runtime value
- fee model
- funding model
- OOS / validation split rule
- fills / trade events
- equity curve
- summary metrics

這不是新的服務或 pipeline，只是讓之後的 survivor 可以被 Hummingbot 原樣重驗。

## 9. What remains intentionally out of scope

本次單策略 Campaign v1.0 不處理下列項目；但它們**不是 HB_READY 一律禁止研究的類型**，能否 PASS 以六項規則及 pinned Hummingbot 實際能力為準：

- multi-strategy portfolio construction
- correlation ranking
- capital competition between strategies
- portfolio compounding
- portfolio-level drawdown
- Testnet / Mainnet authorization
- automatic repo-to-engine deployment bridge
- portfolio optimizer
- arbitrary new governance stages

原則：先把單策略、雙引擎一致性與 Qlib 海選可信度做好，再往下一層走。
