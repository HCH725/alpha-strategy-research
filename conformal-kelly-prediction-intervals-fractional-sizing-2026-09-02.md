---
schema: strategy-research-record-v1
hb_ready_status: NOT_LOSSLESS
title: 'Conformal Kelly: Conformal Prediction Intervals as the Robust Scale in Fractional Kelly Position Sizing'
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
- https://arxiv.org/abs/2608.01494v1
- https://github.com/HCH725/alpha-strategy-research/blob/c405adc4795154334d9d50950795b4711f00445d/conformal-kelly-prediction-intervals-fractional-sizing-2026-09-02.md
- HCH725/validated-survivor-research commit 15c0a95162b60a664b43ac60157225c7300ad789
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Conformal Kelly: Conformal Prediction Intervals as the Robust Scale in Fractional Kelly Position Sizing

## Provenance

- Family identity：`conformal-kelly-prediction-intervals-fractional-sizing-2026-09-02`；本次 consolidation 只按原 baseline family_id，不依 Sharpe 重新排名／挑選。
- Primary source：https://arxiv.org/abs/2608.01494v1。
- 既有 source-backed 研究紀錄：commit `c405adc4795154334d9d50950795b4711f00445d`，`conformal-kelly-prediction-intervals-fractional-sizing-2026-09-02.md`，Git blob `ca8c9f606499767ca6d26095f031f615b82cdfd9`。 Wiki 明列這組 reviewed_commit/reviewed_blob；本輪已核對原 Git object。
- `quant/conformal-kelly-prediction-intervals-fractional-sizing-2026-09-02.md` 的 raw SHA-256 為 `37e4965d20b92c5f4980769f5c9f36d4b1701878cee1d92b63f70449f71d7c1a`；它在 review-state 的 `ingested_wiki_records` 中，state 最後審查 commit 為 `2799e34c5c7f8d6f7036e35d9ae7468832712c97`。這是 ingestion provenance，不是本輪 source parity 或逐檔新審查；Wiki bytes 不冒稱與原 Git blob 相同。
- Historical input：`HCH725/validated-survivor-research` commit `15c0a95162b60a664b43ac60157225c7300ad789` 的 `survivors/<survivor_id>/baseline.json`，本家族 2 筆，cohorts：`BTCUSDT/1d`, `SOLUSDT/1d`。
- Derived leaderboard：同一 repo `leaderboard/leaderboard.json`，raw SHA-256 `e8fdd38c8468960eee5b574e93d27615635bcb266fe481ab8c1409720d96c42e`；它不是 frozen bundle 本身，也不是採用 gate。

- Source-to-legacy-Qlib mapping gap：family 名称、strategy flags/case IDs 或舊 PASS 不證明原文 source-native signal、模型 weights、universe、因果時序與執行機制一致。除本紀錄明列已釘選的程式規則外，沒有補造代碼對照。paper方法、研究解讀與historical DCA分層保留；尚未證明多個 legacy codes 對應不同完整 core mechanisms，故不任意拆成新策略。

## Economic mechanism

### Source-reported

Conformal Kelly 將 conformal prediction interval 的寬度當作 fractional Kelly sizing 的 scale。來源摘要強調 rolling interval width 的穩定性及 gross leverage cap，而不是把 calibration coverage 當作收益保證。

### Research interpretation

這是方法／假說的普通研究封存，不是把歷史 survivor 標籤當成新 alpha。機制層分類與單筆 cohort 的 DCA 收益不同；statistical forecast、risk allocator 或負面 study 均不得被默換成已驗證的 crypto 交易規則。

## Signal

歷史研究紀錄的 forecasting 層為 expanding ridge、21/63/252-day momentum 與 EWMA volatility；已落地 forecast errors 才進 calibration pool。以 per-asset rolling quantiles 建 interval，轉成受 caps 約束的 portfolio sizing；不能以未來尚未落地的 error 校準當日決策。baseline arm_conf/arm_mad/arm_rstd/arm_frozen/arm_rvol20 與 cfg_* 保留原值，不擅自宣稱 survivor 是 conformal arm。

## Required data

原研究為多 ETF adjusted daily prices、先驗固定的 training/development/sealed test boundaries、landed target labels 與多資產 gross-cap accounting。

Historical cohort resolution、parameters 與 data cutoff 以 Evidence 的原 JSON 為準，不補齊不存在的字段，不降採樣、不改 symbol。baseline 不含完整行情 manifest、signal arrays、model checkpoints 或逐筆 trade ledger；它不是可直接執行的策略定義。

## Execution assumptions

歷史研究紀錄描述日頻 rebalance、implementation lag、21-day refit 與 portfolio leverage caps；這些配置會影響事件序列，並非可默認取代的 source-neutral house sizing。

Historical DCA 參數只代表當時研究配置，並非 paper 原生規則，也不是目前 house overlay。未重新量測 fees、funding、margin/liquidation、slippage、intrabar path 或 fills；hash references 不是原資料 bytes 已重新驗證的宣告。

## Evidence

### Source-reported

本輪讀取 versioned primary landing 的 abstract，確認上述 method-level 主張；更細的 signal 配置以釘選原研究紀錄為轉錄來源，未宣稱已重新逐式審閱整篇 methods 或 source code。原文績效不是下列 crypto baseline metrics。

### Independently reproduced

Not independently reproduced. 本輪只驗 source identity／文件轉錄，沒有 Qlib rerun、Hummingbot reproduction、Paper 或 Testnet。

### Negative evidence

原文摘要的 sealed 2022-onward evaluation 中 calibration 維持但 growth 未勝 passive benchmarks；200-configuration 開發搜尋亦須納入 selection-bias 解讀。兩個 baseline 的 arm flags 不足以證明原文 conformal mechanism 被測過。

### HISTORICAL QLIB SURVIVOR EVIDENCE — 非目前 Hummingbot reproduction

以下每個 baseline JSON 保留全部原鍵／數值／null／巢狀結構，唯一刪除 top-level `bundle_path` 的機器絕對路徑。bundle 邏輯定位仍可由 family_id / round_id / run_id 與 survivor ID 找到；不假裝本輪讀取已退役結果盤。每筆獨立列 raw baseline-file SHA-256，它與 `params_sha256`、`bundle_sha256`（檔案 bytes）、`bundle_identity_sha256`（歷史 identity recipe）互不相同。

鍵名 `net_pnl` / `sharpe` / `max_dd_pct` / `annualized_return` 原樣保留，不重命名成 ROI、不對 MDD 改 sign／比例／百分點、不跨 lineage 默認同一 annualization。baseline 欄位缺席不同於 null；不從另一層悄悄補值。`source_verdict: PASS` 與 `neighbourhood.passed` 都是 HISTORICAL，不能解讀成今日 efficacy、source parity 或 HB_READY PASS。

每筆另列 `leaderboard_snapshot`：`additional_fields` 為 derived index 額外欄位，`baseline_field_overrides` 為該 index 與 baseline 不同的完整 top-level 值；空 object 明示無差異。兩者都不回寫 baseline。僅非 null 的 `evidence_manifest_path` 去除原 results-root 絕對前綴，保留 `_survivors/...` 相對 locator；null 留 null。rank / top10 / package PRESENT / FROZEN_ONLY 只是當時 derived state，不能解讀為今天 evidence package bytes 存在或新 forward evidence。

#### sv-1e4d2489f16c2971 — HISTORICAL

Baseline file SHA-256：`8789b421e7f6a4f9eb5dfaf4b59bc73ae8f1a52344f16f8f27278b915b4675c3`；archive locator：`survivors/sv-1e4d2489f16c2971/baseline.json`。

```json
{"survivor_id":"sv-1e4d2489f16c2971","family_id":"conformal-kelly-prediction-intervals-fractional-sizing-2026-09-02","round_id":"conformal-kelly-prediction-intervals-fractional-sizing-2026-09-02-r1","run_id":"conformal-kelly-prediction-intervals-fractional-sizing-2026-09-02-r1-u1","kanban_task_id":"t_14a1a080","cohort":"SOLUSDT/1d","symbol":"SOLUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"arm_conf":0,"arm_mad":0,"arm_rstd":0,"arm_frozen":0,"arm_rvol20":1,"cfg_A":1,"cfg_B":0},"dca_params":{"spacing_pct":0.02,"size_multiplier":1.1,"breakeven_tp_pct":0.02,"invalidation_pct":0.1},"params_sha256":"sha256:51145a6c6a164aebf728e32d0598fb7142c3600c0b67d06777272973cca9a416","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:c27737bd51f6b9810b5d2c5b39c8bbabbd6dc34bed87f99bb3fe6f96c776040e","bundle_identity_sha256":"sha256:243f4b0411c762e8ca60e81d827e3782293ea89ba5c1341445640d435878513a","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":14444.644597,"sharpe":1.791357,"episodes":25,"max_dd_pct":-0.003188},"oos":{"net_pnl":4999.402131,"sharpe":1.748047,"episodes":6,"max_dd_pct":-0.01953},"full":{"net_pnl":19444.046728,"sharpe":1.781537,"episodes":31,"max_dd_pct":-0.01343,"annualized_return":0.13803572531366548},"robustness":{"fee_2x":{"net_pnl":18371.486513,"sharpe":1.768959,"max_dd_pct":-0.014045},"funding_2x":{"net_pnl":19360.536639,"sharpe":1.775359,"max_dd_pct":-0.013448},"entry_delay_1_bar":{"net_pnl":15294.283522,"sharpe":1.804233,"max_dd_pct":-0.011535},"slippage_2ticks":{"net_pnl":19366.28004,"sharpe":1.779944,"max_dd_pct":-0.013539}},"robustness_stress_floor_net_pnl":15294.283522,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":0.75,"passed":true,"neighbours":8,"agreeing":6}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-1e4d2489f16c2971","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":51,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{"full":{"net_pnl":19444.046728,"sharpe":1.781537,"episodes":31,"max_dd_pct":-0.01343,"annualized_return":0.13803572531366548,"avg_trades_per_year":6.602186588921282}},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-51c28bb1fad87264 — HISTORICAL

Baseline file SHA-256：`e3f75c8337dc4718c801b057ee1b1947d6db92122cf06c3d0922ea7f15ec44a9`；archive locator：`survivors/sv-51c28bb1fad87264/baseline.json`。

```json
{"survivor_id":"sv-51c28bb1fad87264","family_id":"conformal-kelly-prediction-intervals-fractional-sizing-2026-09-02","round_id":"conformal-kelly-prediction-intervals-fractional-sizing-2026-09-02-r1","run_id":"conformal-kelly-prediction-intervals-fractional-sizing-2026-09-02-r1-u1","kanban_task_id":"t_14a1a080","cohort":"BTCUSDT/1d","symbol":"BTCUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"arm_conf":0,"arm_mad":0,"arm_rstd":0,"arm_frozen":0,"arm_rvol20":1,"cfg_A":1,"cfg_B":0},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.0,"breakeven_tp_pct":0.01,"invalidation_pct":0.05},"params_sha256":"sha256:51f6c56c5495e3262feeed4694240c2e68ec7cfa50313b3a2065bb81f663741c","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:c27737bd51f6b9810b5d2c5b39c8bbabbd6dc34bed87f99bb3fe6f96c776040e","bundle_identity_sha256":"sha256:243f4b0411c762e8ca60e81d827e3782293ea89ba5c1341445640d435878513a","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":4356.218127,"sharpe":1.893903,"episodes":18,"max_dd_pct":0.0},"oos":{"net_pnl":2869.808961,"sharpe":3.211027,"episodes":12,"max_dd_pct":0.0},"full":{"net_pnl":7226.027088,"sharpe":2.210297,"episodes":30,"max_dd_pct":0.0,"annualized_return":0.05129847218483165},"robustness":{"fee_2x":{"net_pnl":6411.97762,"sharpe":2.212367,"max_dd_pct":0.0},"funding_2x":{"net_pnl":7167.168177,"sharpe":2.20619,"max_dd_pct":0.0},"entry_delay_1_bar":{"net_pnl":1928.560907,"sharpe":0.225881,"max_dd_pct":-0.144427},"slippage_2ticks":{"net_pnl":7224.963169,"sharpe":2.210306,"max_dd_pct":0.0}},"robustness_stress_floor_net_pnl":1928.560907,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":6,"agreeing":6}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-51c28bb1fad87264","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":33,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{"full":{"net_pnl":7226.027088,"sharpe":2.210297,"episodes":30,"max_dd_pct":0.0,"annualized_return":0.05129847218483165,"avg_trades_per_year":6.389212827988338}},"baseline_fields_absent_in_leaderboard":[]}}
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

`hb_ready_status: NOT_LOSSLESS`。跨資產 portfolio sizing、shared gross cap、訓練/label maturity 與 implementation lag 未獲目前 lossless proof。

Research-only、not-approved；不能進目前 Hummingbot/Qlib 績效下游，不是 Paper/Testnet/Live approval。普通 non-Scout reconstruction 紀錄可經獨立 provenance/research review 保留，並非 Scout one-file PASS admission。

## Related Wiki records

`quant/conformal-kelly-prediction-intervals-fractional-sizing-2026-09-02.md` — 本紀錄上列 hash 的原研究 provenance，未修改 Wiki。

## Sources

1. Primary：https://arxiv.org/abs/2608.01494v1
2. Pinned historical source：https://github.com/HCH725/alpha-strategy-research/blob/c405adc4795154334d9d50950795b4711f00445d/conformal-kelly-prediction-intervals-fractional-sizing-2026-09-02.md
3. Historical baseline/leaderboard archive：https://github.com/HCH725/validated-survivor-research/tree/15c0a95162b60a664b43ac60157225c7300ad789；commit 及 per-baseline raw digests 以上述 Provenance/Evidence 為準，並未聲稱所有 reference 可供匿名讀者直接下載。
