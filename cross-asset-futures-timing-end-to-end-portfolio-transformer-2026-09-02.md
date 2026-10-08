---
schema: strategy-research-record-v1
hb_ready_status: NOT_LOSSLESS
title: 'End-to-End Parametric Portfolio Policies for Cross-Asset Futures Timing: Portfolio Transformer vs. LSTM Under Differentiable Sharpe Optimization'
created: '2026-10-08'
updated: '2026-10-08'
type: strategy-research-record
tags:
- quant
- strategy-research
- source-backed
status: research-only
confidence: medium
source_as_of: '2026-10-08'
sources:
- https://arxiv.org/abs/2607.00475v1
- https://github.com/HCH725/alpha-strategy-research/blob/c405adc4795154334d9d50950795b4711f00445d/cross-asset-futures-timing-end-to-end-portfolio-transformer-2026-09-02.md
- HCH725/validated-survivor-research commit 15c0a95162b60a664b43ac60157225c7300ad789
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# End-to-End Parametric Portfolio Policies for Cross-Asset Futures Timing: Portfolio Transformer vs. LSTM Under Differentiable Sharpe Optimization

## Provenance

- Family identity：`cross-asset-futures-timing-end-to-end-portfolio-transformer-2026-09-02`；本次 consolidation 只按原 baseline family_id，不依 Sharpe 重新排名／挑選。
- Primary source：https://arxiv.org/abs/2607.00475v1。
- 既有 source-backed 研究紀錄：commit `c405adc4795154334d9d50950795b4711f00445d`，`cross-asset-futures-timing-end-to-end-portfolio-transformer-2026-09-02.md`，Git blob `8da1c84fdba4580a8a7136b5c082146f71b82642`。 Wiki 明列這組 reviewed_commit/reviewed_blob；本輪已核對原 Git object。
- `quant/cross-asset-futures-timing-end-to-end-portfolio-transformer-2026-09-02.md` 的 raw SHA-256 為 `efd9d8c5f80a7b7e60c2956567e54ac9123bd4f2f021ab854f583d3fcbb0cfe9`；它在 review-state 的 `ingested_wiki_records` 中，state 最後審查 commit 為 `2799e34c5c7f8d6f7036e35d9ae7468832712c97`。這是 ingestion provenance，不是本輪 source parity 或逐檔新審查；Wiki bytes 不冒稱與原 Git blob 相同。
- Historical input：`HCH725/validated-survivor-research` commit `15c0a95162b60a664b43ac60157225c7300ad789` 的 `survivors/<survivor_id>/baseline.json`，本家族 4 筆，cohorts：`BNBUSDT/1d`, `BTCUSDT/1d`, `ETHUSDT/1d`, `SOLUSDT/1d`。
- Derived leaderboard：同一 repo `leaderboard/leaderboard.json`，raw SHA-256 `e8fdd38c8468960eee5b574e93d27615635bcb266fe481ab8c1409720d96c42e`；它不是 frozen bundle 本身，也不是採用 gate。

- Source-to-legacy-Qlib mapping gap：family 名称、strategy flags/case IDs 或舊 PASS 不證明原文 source-native signal、模型 weights、universe、因果時序與執行機制一致。除本紀錄明列已釘選的程式規則外，沒有補造代碼對照。paper方法、研究解讀與historical DCA分層保留；尚未證明多個 legacy codes 對應不同完整 core mechanisms，故不任意拆成新策略。

## Economic mechanism

### Source-reported

來源研究直接從跨資產 state 映射 portfolio weights，以 differentiable Sharpe objective 訓練 LSTM/Transformer，比較 equal weight、risk parity 與 time-series momentum。

### Research interpretation

這是方法／假說的普通研究封存，不是把歷史 survivor 標籤當成新 alpha。機制層分類與單筆 cohort 的 DCA 收益不同；statistical forecast、risk allocator 或負面 study 均不得被默換成已驗證的 crypto 交易規則。

## Signal

16 個 CME futures 的 return cross-section → trained end-to-end policy → signed/continuous allocations。歷史研究紀錄提到 temporal/cross-asset attention、multi-seed evaluation 與 feature ablations；baseline arm=2 尚無可信的 source-native architecture/weights 對照，不能由數字 2 宣稱已復現 Transformer。

## Required data

原文需 CME 跨 asset-class futures panel、rolling contracts、session/price normalization、frozen training windows 與 model weights；crypto 四幣 universe 不能替代真正跨 asset-class breadth。

Historical cohort resolution、parameters 與 data cutoff 以 Evidence 的原 JSON 為準，不補齊不存在的字段，不降採樣、不改 symbol。baseline 不含完整行情 manifest、signal arrays、model checkpoints 或逐筆 trade ledger；它不是可直接執行的策略定義。

## Execution assumptions

Portfolio target weights、daily rebalance、turnover costs 與多資產淨值為評估對象。原文 gross LSTM/Transformer 比較不等於交易成本後勝負。

Historical DCA 參數只代表當時研究配置，並非 paper 原生規則，也不是目前 house overlay。未重新量測 fees、funding、margin/liquidation、slippage、intrabar path 或 fills；hash references 不是原資料 bytes 已重新驗證的宣告。

## Evidence

### Source-reported

本輪讀取 versioned primary landing 的 abstract，確認上述 method-level 主張；更細的 signal 配置以釘選原研究紀錄為轉錄來源，未宣稱已重新逐式審閱整篇 methods 或 source code。原文績效不是下列 crypto baseline metrics。

### Independently reproduced

Not independently reproduced. 本輪只驗 source identity／文件轉錄，沒有 Qlib rerun、Hummingbot reproduction、Paper 或 Testnet。

### Negative evidence

原文摘要表示 learned policy 優勢並非所有 sleeves 均成立，交易成本亦讓 Transformer 與 LSTM 的排名分歧；舊 arm cohort metrics 不能證明原文 network 機制或 CME 結果可移植。

### HISTORICAL QLIB SURVIVOR EVIDENCE — 非目前 Hummingbot reproduction

以下每個 baseline JSON 保留全部原鍵／數值／null／巢狀結構，唯一刪除 top-level `bundle_path` 的機器絕對路徑。bundle 邏輯定位仍可由 family_id / round_id / run_id 與 survivor ID 找到；不假裝本輪讀取已退役結果盤。每筆獨立列 raw baseline-file SHA-256，它與 `params_sha256`、`bundle_sha256`（檔案 bytes）、`bundle_identity_sha256`（歷史 identity recipe）互不相同。

鍵名 `net_pnl` / `sharpe` / `max_dd_pct` / `annualized_return` 原樣保留，不重命名成 ROI、不對 MDD 改 sign／比例／百分點、不跨 lineage 默認同一 annualization。baseline 欄位缺席不同於 null；不從另一層悄悄補值。`source_verdict: PASS` 與 `neighbourhood.passed` 都是 HISTORICAL，不能解讀成今日 efficacy、source parity 或 HB_READY PASS。

每筆另列 `leaderboard_snapshot`：`additional_fields` 為 derived index 額外欄位，`baseline_field_overrides` 為該 index 與 baseline 不同的完整 top-level 值；空 object 明示無差異。兩者都不回寫 baseline。僅非 null 的 `evidence_manifest_path` 去除原 results-root 絕對前綴，保留 `_survivors/...` 相對 locator；null 留 null。rank / top10 / package PRESENT / FROZEN_ONLY 只是當時 derived state，不能解讀為今天 evidence package bytes 存在或新 forward evidence。

#### sv-48dba15dd162a5cb — HISTORICAL

Baseline file SHA-256：`5c87d2c861266effb97b92733d8715221cf7c46177d503c2cacb3db1b8441bf7`；archive locator：`survivors/sv-48dba15dd162a5cb/baseline.json`。

```json
{"survivor_id":"sv-48dba15dd162a5cb","family_id":"cross-asset-futures-timing-end-to-end-portfolio-transformer-2026-09-02","round_id":"cross-asset-futures-timing-end-to-end-portfolio-transformer-2026-09-02-r1","run_id":"cross-asset-futures-timing-end-to-end-portfolio-transformer-2026-09-02-r1-u4","kanban_task_id":"t_3ae0a358","cohort":"SOLUSDT/1d","symbol":"SOLUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"arm":2},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.0,"breakeven_tp_pct":0.02,"invalidation_pct":0.1},"params_sha256":"sha256:d4c868c99e386bb75af0b713ca9647671283aedb25c60a58ae95185532e2bc53","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:140d5168048139044b03f42e680cf7072fcddc03615fa7a2acecc994d3118ae7","bundle_identity_sha256":"sha256:f7872567c6d340ffcd1c25d47be8c0ef465bb7fc02fe02b3d34b1c005cdb4a13","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":125597.268359,"sharpe":4.582438,"episodes":198,"max_dd_pct":-0.076714},"oos":{"net_pnl":31801.071837,"sharpe":2.94304,"episodes":68,"max_dd_pct":-0.220973},"full":{"net_pnl":157398.340197,"sharpe":4.243741,"episodes":266,"max_dd_pct":-0.076714,"annualized_return":1.1173905492101863},"robustness":{"fee_2x":{"net_pnl":147054.353685,"sharpe":4.134783,"max_dd_pct":-0.081092},"funding_2x":{"net_pnl":157167.644263,"sharpe":4.234427,"max_dd_pct":-0.07683},"entry_delay_1_bar":{"net_pnl":118823.775196,"sharpe":1.644996,"max_dd_pct":-0.361951},"slippage_2ticks":{"net_pnl":155707.379572,"sharpe":4.212663,"max_dd_pct":-0.077279}},"robustness_stress_floor_net_pnl":118823.775196,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":0.857143,"passed":true,"neighbours":7,"agreeing":6}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-48dba15dd162a5cb","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":38,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{"full":{"net_pnl":157398.340197,"sharpe":4.243741,"episodes":266,"max_dd_pct":-0.076714,"annualized_return":1.1173905492101863,"avg_trades_per_year":56.65102040816326}},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-ac993061fb435d82 — HISTORICAL

Baseline file SHA-256：`edb37fcf98430e562a68c1ad494301745407b8f81aa56e9eda7c0ede18eb88a0`；archive locator：`survivors/sv-ac993061fb435d82/baseline.json`。

```json
{"survivor_id":"sv-ac993061fb435d82","family_id":"cross-asset-futures-timing-end-to-end-portfolio-transformer-2026-09-02","round_id":"cross-asset-futures-timing-end-to-end-portfolio-transformer-2026-09-02-r1","run_id":"cross-asset-futures-timing-end-to-end-portfolio-transformer-2026-09-02-r1-u4","kanban_task_id":"t_3ae0a358","cohort":"BTCUSDT/1d","symbol":"BTCUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"arm":2},"dca_params":{"spacing_pct":0.02,"size_multiplier":1.0,"breakeven_tp_pct":0.01,"invalidation_pct":0.1},"params_sha256":"sha256:4dfd10aee78a8a6175890f1e3a682c80f190fe061f031a8ebb78fc75681afaa4","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:140d5168048139044b03f42e680cf7072fcddc03615fa7a2acecc994d3118ae7","bundle_identity_sha256":"sha256:f7872567c6d340ffcd1c25d47be8c0ef465bb7fc02fe02b3d34b1c005cdb4a13","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":25505.525751,"sharpe":5.188132,"episodes":210,"max_dd_pct":-0.010139},"oos":{"net_pnl":5979.406941,"sharpe":2.222671,"episodes":69,"max_dd_pct":-0.087102},"full":{"net_pnl":31484.932693,"sharpe":4.252918,"episodes":279,"max_dd_pct":-0.049653,"annualized_return":0.2235154842748306},"robustness":{"fee_2x":{"net_pnl":26876.457858,"sharpe":3.855819,"max_dd_pct":-0.053737},"funding_2x":{"net_pnl":30628.671179,"sharpe":4.171294,"max_dd_pct":-0.050327},"entry_delay_1_bar":{"net_pnl":29463.295488,"sharpe":5.571227,"max_dd_pct":-0.017008},"slippage_2ticks":{"net_pnl":31474.396102,"sharpe":4.251856,"max_dd_pct":-0.049663}},"robustness_stress_floor_net_pnl":26876.457858,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":0.857143,"passed":true,"neighbours":7,"agreeing":6}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-ac993061fb435d82","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":42,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{"full":{"net_pnl":31484.932693,"sharpe":4.252918,"episodes":279,"max_dd_pct":-0.049653,"annualized_return":0.2235154842748306,"avg_trades_per_year":59.41967930029154}},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-ea8817f7dafaed34 — HISTORICAL

Baseline file SHA-256：`dec0f738ce309a1ccc05dc35e9de8aaf24ae6e5fe62cc151bee4e8cfb1d7f0ab`；archive locator：`survivors/sv-ea8817f7dafaed34/baseline.json`。

```json
{"survivor_id":"sv-ea8817f7dafaed34","family_id":"cross-asset-futures-timing-end-to-end-portfolio-transformer-2026-09-02","round_id":"cross-asset-futures-timing-end-to-end-portfolio-transformer-2026-09-02-r1","run_id":"cross-asset-futures-timing-end-to-end-portfolio-transformer-2026-09-02-r1-u4","kanban_task_id":"t_3ae0a358","cohort":"BNBUSDT/1d","symbol":"BNBUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"arm":4},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.0,"breakeven_tp_pct":0.01,"invalidation_pct":0.05},"params_sha256":"sha256:5100cbe837aa991c9babdfb94d0bab62fa895717f79c2a3e8f12508a177c8e84","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:140d5168048139044b03f42e680cf7072fcddc03615fa7a2acecc994d3118ae7","bundle_identity_sha256":"sha256:f7872567c6d340ffcd1c25d47be8c0ef465bb7fc02fe02b3d34b1c005cdb4a13","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":17726.109852,"sharpe":3.503502,"episodes":67,"max_dd_pct":-0.005292},"oos":{"net_pnl":4148.804086,"sharpe":3.861193,"episodes":16,"max_dd_pct":-0.001096},"full":{"net_pnl":21874.913938,"sharpe":3.510683,"episodes":83,"max_dd_pct":-0.005292,"annualized_return":0.15529275637916548},"robustness":{"fee_2x":{"net_pnl":19342.230123,"sharpe":3.483801,"max_dd_pct":-0.006528},"funding_2x":{"net_pnl":21917.776004,"sharpe":3.499789,"max_dd_pct":-0.005294},"entry_delay_1_bar":{"net_pnl":8776.643473,"sharpe":0.687039,"max_dd_pct":-0.164162},"slippage_2ticks":{"net_pnl":22204.633079,"sharpe":3.564793,"max_dd_pct":-0.002022}},"robustness_stress_floor_net_pnl":8776.643473,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":6,"agreeing":6}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-ea8817f7dafaed34","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":28,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{"full":{"net_pnl":21874.913938,"sharpe":3.510683,"episodes":83,"max_dd_pct":-0.005292,"annualized_return":0.15529275637916548,"avg_trades_per_year":17.6768221574344}},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-fd839be135026f9d — HISTORICAL

Baseline file SHA-256：`18952e1beaa7dbd2cbb07b9e5adef8942e42d79ffe1fbd7745de97a72952f613`；archive locator：`survivors/sv-fd839be135026f9d/baseline.json`。

```json
{"survivor_id":"sv-fd839be135026f9d","family_id":"cross-asset-futures-timing-end-to-end-portfolio-transformer-2026-09-02","round_id":"cross-asset-futures-timing-end-to-end-portfolio-transformer-2026-09-02-r1","run_id":"cross-asset-futures-timing-end-to-end-portfolio-transformer-2026-09-02-r1-u4","kanban_task_id":"t_3ae0a358","cohort":"ETHUSDT/1d","symbol":"ETHUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"arm":2},"dca_params":{"spacing_pct":0.02,"size_multiplier":1.0,"breakeven_tp_pct":0.01,"invalidation_pct":0.1},"params_sha256":"sha256:4dfd10aee78a8a6175890f1e3a682c80f190fe061f031a8ebb78fc75681afaa4","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:140d5168048139044b03f42e680cf7072fcddc03615fa7a2acecc994d3118ae7","bundle_identity_sha256":"sha256:f7872567c6d340ffcd1c25d47be8c0ef465bb7fc02fe02b3d34b1c005cdb4a13","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":33546.716849,"sharpe":5.933581,"episodes":190,"max_dd_pct":-0.003225},"oos":{"net_pnl":1524.602111,"sharpe":0.357155,"episodes":66,"max_dd_pct":-0.243118},"full":{"net_pnl":35071.318961,"sharpe":2.419107,"episodes":256,"max_dd_pct":-0.134659,"annualized_return":0.24897568999812622},"robustness":{"fee_2x":{"net_pnl":29951.033835,"sharpe":2.067461,"max_dd_pct":-0.145717},"funding_2x":{"net_pnl":35833.174198,"sharpe":2.470411,"max_dd_pct":-0.133205},"entry_delay_1_bar":{"net_pnl":37540.644019,"sharpe":6.307323,"max_dd_pct":-0.004292},"slippage_2ticks":{"net_pnl":35048.922492,"sharpe":2.417604,"max_dd_pct":-0.134704}},"robustness_stress_floor_net_pnl":29951.033835,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":0.857143,"passed":true,"neighbours":7,"agreeing":6}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-fd839be135026f9d","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":82,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{"full":{"net_pnl":35071.318961,"sharpe":2.419107,"episodes":256,"max_dd_pct":-0.134659,"annualized_return":0.24897568999812622,"avg_trades_per_year":54.521282798833816}},"baseline_fields_absent_in_leaderboard":[]}}
```

## Falsification plan

1. 先恢復 exact source-to-case / model / signal / timing 對照，若不能證明便維持 source-mapping gap；不得以調參 rescue 或另寫 proxy 宣稱復現原文。
2. 若將來另獲執行授權，先用 prefix/suffix perturbation、landed-label checks、formation-to-order timestamps 與 universe alignment 反證 look-ahead；再以同一事件模型核對 fills、funding、fee、margin 及 parameter sensitivity。
3. 保留負面 controls、成本壓力、完整 denominator 與未觀測欄位。對 forecasting / risk-control 主張，須各有 baseline/ablation，不能單靠一個 per-coin Sharpe 認定方法有效。
4. 以上僅是未來 research tests，不是這張 archival PR 已跑過的測試，也不授權 backtest、pipeline 或交易。

## Crypto portability

Adapted / unproven。來源股票／ETF／期貨方法與下列 crypto legacy cohorts 是不同層；替换 instrument、calendar、features、model、portfolio 或 fills 均可能改變 estimand。

## Limitations

- baseline 與 leaderboard 是 frozen/derived archival summaries，不包含完整 robustness grid 的所有未勝出 cases、鄰居逐筆結果、source-native code/model 或事件序列；現存四 stress grids 和 neighborhood summary 全保留，缺失資料不捏造。
- historical/OOS/full 的細分日期與 split recipe 未隨 baseline 提供；只保留 exact data cutoff 與原 identity，除有已回收 source 證據外不推論 slice endpoints。
- 存在 survivor selection、搜尋過的 evaluation periods、樣本數不足、資料／成本／模型身份尚未回收的限制；不因 baseline 帶 PASS 而移除。
- Metric definitions/units 可跨 engine lineage 不同；baseline 与 derived leaderboard 的補算差異各自保留，不混寫成新的績效真值。

## Implementation status

Not implemented in the current research/runtime stack. Historical code / baselines 在此只作 Provenance/Evidence；本輪未實作、修復、採用或部署策略。

## Adoption boundary

`hb_ready_status: NOT_LOSSLESS`。跨資產 policy inputs、shared portfolio weights/capital 與 learned model identity 不能 losslessly 變為單幣 OHLCV rule。

Research-only、not-approved；不能進目前 Hummingbot/Qlib 績效下游，不是 Paper/Testnet/Live approval。普通 non-Scout reconstruction 紀錄可經獨立 provenance/research review 保留，並非 Scout one-file PASS admission。

## Related Wiki records

`quant/cross-asset-futures-timing-end-to-end-portfolio-transformer-2026-09-02.md` — 本紀錄上列 hash 的原研究 provenance，未修改 Wiki。

## Sources

1. Primary：https://arxiv.org/abs/2607.00475v1
2. Pinned historical source：https://github.com/HCH725/alpha-strategy-research/blob/c405adc4795154334d9d50950795b4711f00445d/cross-asset-futures-timing-end-to-end-portfolio-transformer-2026-09-02.md
3. Historical baseline/leaderboard archive：https://github.com/HCH725/validated-survivor-research/tree/15c0a95162b60a664b43ac60157225c7300ad789；commit 及 per-baseline raw digests 以上述 Provenance/Evidence 為準，並未聲稱所有 reference 可供匿名讀者直接下載。
