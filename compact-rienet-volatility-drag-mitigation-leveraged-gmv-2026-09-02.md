---
schema: strategy-research-record-v1
hb_ready_status: NOT_LOSSLESS
title: 'Compact-RIEnet: Neural Network-Driven Volatility Drag Mitigation and Liquidation Delay under Aggressive Portfolio Leverage'
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
- https://arxiv.org/abs/2607.23068v1
- https://github.com/HCH725/alpha-strategy-research/blob/c405adc4795154334d9d50950795b4711f00445d/compact-rienet-volatility-drag-mitigation-leveraged-gmv-2026-09-02.md
- HCH725/validated-survivor-research commit 15c0a95162b60a664b43ac60157225c7300ad789
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Compact-RIEnet: Neural Network-Driven Volatility Drag Mitigation and Liquidation Delay under Aggressive Portfolio Leverage

## Provenance

- Family identity：`compact-rienet-volatility-drag-mitigation-leveraged-gmv-2026-09-02`；本次 consolidation 只按原 baseline family_id，不依 Sharpe 重新排名／挑選。
- Primary source：https://arxiv.org/abs/2607.23068v1。
- 既有 source-backed 研究紀錄：commit `c405adc4795154334d9d50950795b4711f00445d`，`compact-rienet-volatility-drag-mitigation-leveraged-gmv-2026-09-02.md`，Git blob `662396c71f631000232f85afc59dec3e30d0334a`。 Wiki 明列這組 reviewed_commit/reviewed_blob；本輪已核對原 Git object。
- `quant/compact-rienet-volatility-drag-mitigation-leveraged-gmv-2026-09-02.md` 的 raw SHA-256 為 `06e0de200e8d701b6510073d54a2b5a5e40b5ecb1fb1ca89ee02d41fc236703d`；它在 review-state 的 `ingested_wiki_records` 中，state 最後審查 commit 為 `2799e34c5c7f8d6f7036e35d9ae7468832712c97`。這是 ingestion provenance，不是本輪 source parity 或逐檔新審查；Wiki bytes 不冒稱與原 Git blob 相同。
- Historical input：`HCH725/validated-survivor-research` commit `15c0a95162b60a664b43ac60157225c7300ad789` 的 `survivors/<survivor_id>/baseline.json`，本家族 2 筆，cohorts：`BNBUSDT/1d`, `BTCUSDT/1d`。
- Derived leaderboard：同一 repo `leaderboard/leaderboard.json`，raw SHA-256 `e8fdd38c8468960eee5b574e93d27615635bcb266fe481ab8c1409720d96c42e`；它不是 frozen bundle 本身，也不是採用 gate。

- Source-to-legacy-Qlib mapping gap：family 名称、strategy flags/case IDs 或舊 PASS 不證明原文 source-native signal、模型 weights、universe、因果時序與執行機制一致。除本紀錄明列已釘選的程式規則外，沒有補造代碼對照。paper方法、研究解讀與historical DCA分層保留；尚未證明多個 legacy codes 對應不同完整 core mechanisms，故不任意拆成新策略。

## Economic mechanism

### Source-reported

Compact-RIEnet 是多資產 global-minimum-variance risk allocator：以較精簡的 lag transformation、BiGRU spectral cleaning 與 marginal volatility network 降低組合變異與槓桿下的 volatility drag。它不是單資產方向預測器。

### Research interpretation

這是方法／假說的普通研究封存，不是把歷史 survivor 標籤當成新 alpha。機制層分類與單筆 cohort 的 DCA 收益不同；statistical forecast、risk allocator 或負面 study 均不得被默換成已驗證的 crypto 交易規則。

## Signal

來源摘要的主體是 return-panel → covariance/inverse-covariance estimation → constrained GMV weights。歷史研究紀錄包含 five-parameter hyperbolic lag weighting、saturating transform、spectral eigencleaning 與 long-only weight constraints。baseline 的 cl_raw/cl_shrink/cl_mp 與 lb_* 為舊分支標籤；不能由這些 one-hot flags 推定神經網路已按原文訓練、weights 相同或 source parity 成立。

## Required data

來源需要多股票 adjusted daily return panel、歷史 universe、模型訓練及 simulator margin/corporate-action inputs；crypto cohort 的單一績效列不包含整個原文 portfolio。

Historical cohort resolution、parameters 與 data cutoff 以 Evidence 的原 JSON 為準，不補齊不存在的字段，不降採樣、不改 symbol。baseline 不含完整行情 manifest、signal arrays、model checkpoints 或逐筆 trade ledger；它不是可直接執行的策略定義。

## Execution assumptions

原文涉及 long-only 組合、leverage 與 simulator margin-call dynamics；daily allocation 的交易時點、financing、constraints 與 liquidations 必須保持 portfolio 層語意，不能轉成單幣 DCA 的原生規則。

Historical DCA 參數只代表當時研究配置，並非 paper 原生規則，也不是目前 house overlay。未重新量測 fees、funding、margin/liquidation、slippage、intrabar path 或 fills；hash references 不是原資料 bytes 已重新驗證的宣告。

## Evidence

### Source-reported

本輪讀取 versioned primary landing 的 abstract，確認上述 method-level 主張；更細的 signal 配置以釘選原研究紀錄為轉錄來源，未宣稱已重新逐式審閱整篇 methods 或 source code。原文績效不是下列 crypto baseline metrics。

### Independently reproduced

Not independently reproduced. 本輪只驗 source identity／文件轉錄，沒有 Qlib rerun、Hummingbot reproduction、Paper 或 Testnet。

### Negative evidence

降變異或容許較高槓桿不等於已證明 crypto alpha。歷史 runner 的 covariance cleaning 分支是否實作完整 Compact-RIEnet 尚未逐式證實。原文 arXiv v1 submission 是 2026-07-25，舊 Wiki 寫 2026-07-26；本輪採 versioned landing identity。

### HISTORICAL QLIB SURVIVOR EVIDENCE — 非目前 Hummingbot reproduction

以下每個 baseline JSON 保留全部原鍵／數值／null／巢狀結構，唯一刪除 top-level `bundle_path` 的機器絕對路徑。bundle 邏輯定位仍可由 family_id / round_id / run_id 與 survivor ID 找到；不假裝本輪讀取已退役結果盤。每筆獨立列 raw baseline-file SHA-256，它與 `params_sha256`、`bundle_sha256`（檔案 bytes）、`bundle_identity_sha256`（歷史 identity recipe）互不相同。

鍵名 `net_pnl` / `sharpe` / `max_dd_pct` / `annualized_return` 原樣保留，不重命名成 ROI、不對 MDD 改 sign／比例／百分點、不跨 lineage 默認同一 annualization。baseline 欄位缺席不同於 null；不從另一層悄悄補值。`source_verdict: PASS` 與 `neighbourhood.passed` 都是 HISTORICAL，不能解讀成今日 efficacy、source parity 或 HB_READY PASS。

每筆另列 `leaderboard_snapshot`：`additional_fields` 為 derived index 額外欄位，`baseline_field_overrides` 為該 index 與 baseline 不同的完整 top-level 值；空 object 明示無差異。兩者都不回寫 baseline。僅非 null 的 `evidence_manifest_path` 去除原 results-root 絕對前綴，保留 `_survivors/...` 相對 locator；null 留 null。rank / top10 / package PRESENT / FROZEN_ONLY 只是當時 derived state，不能解讀為今天 evidence package bytes 存在或新 forward evidence。

#### sv-212015d640a03702 — HISTORICAL

Baseline file SHA-256：`37a9d596840775bf01d1f468a10c45303a0d86a04399b202f88a0d7af9737d16`；archive locator：`survivors/sv-212015d640a03702/baseline.json`。

```json
{"survivor_id":"sv-212015d640a03702","family_id":"compact-rienet-volatility-drag-mitigation-leveraged-gmv-2026-09-02","round_id":"compact-rienet-volatility-drag-mitigation-leveraged-gmv-2026-09-02-r1","run_id":"compact-rienet-volatility-drag-mitigation-leveraged-gmv-2026-09-02-r1-u3","kanban_task_id":"t_54d4eaf1","cohort":"BNBUSDT/1d","symbol":"BNBUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"cl_raw":0,"cl_shrink":1,"cl_mp":0,"lb_250":1,"lb_500":0,"lb_750":0,"lb_1200":0},"dca_params":{"spacing_pct":0.02,"size_multiplier":1.0,"breakeven_tp_pct":0.01,"invalidation_pct":0.1},"params_sha256":"sha256:bc12346c4b2110c80ed96065c46a390a84a3923420b5d4555819ce65ca6cbf32","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:df1bd71eb92afe0c4465019818ab354263c2449994bc3e2819d4cf41b6d7861f","bundle_identity_sha256":"sha256:1e1fdf1491008a8bd3b4bf92a35b90accab93e391fbcc687d54e4150ce10762d","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":7164.687045,"sharpe":3.09553,"episodes":46,"max_dd_pct":-0.003231},"oos":{"net_pnl":2319.083884,"sharpe":3.312014,"episodes":15,"max_dd_pct":-0.000914},"full":{"net_pnl":9483.770929,"sharpe":3.140777,"episodes":61,"max_dd_pct":-0.003231,"annualized_return":0.0673264787506673},"robustness":{"fee_2x":{"net_pnl":8438.582111,"sharpe":3.125952,"max_dd_pct":-0.003411},"funding_2x":{"net_pnl":9635.095138,"sharpe":3.131273,"max_dd_pct":-0.003219},"entry_delay_1_bar":{"net_pnl":9287.101847,"sharpe":2.852845,"max_dd_pct":-0.011372},"slippage_2ticks":{"net_pnl":9461.41455,"sharpe":3.140447,"max_dd_pct":-0.003245}},"robustness_stress_floor_net_pnl":8438.582111,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":0.714286,"passed":true,"neighbours":7,"agreeing":5}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-212015d640a03702","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":32,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{"full":{"net_pnl":9483.770929,"sharpe":3.140777,"episodes":61,"max_dd_pct":-0.003231,"annualized_return":0.0673264787506673,"avg_trades_per_year":12.99139941690962}},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-5730b84e7cdcaa00 — HISTORICAL

Baseline file SHA-256：`ae4ab8743f03637474110fd431151d4830947cf4e9ef4c73772aaef026a61f5e`；archive locator：`survivors/sv-5730b84e7cdcaa00/baseline.json`。

```json
{"survivor_id":"sv-5730b84e7cdcaa00","family_id":"compact-rienet-volatility-drag-mitigation-leveraged-gmv-2026-09-02","round_id":"compact-rienet-volatility-drag-mitigation-leveraged-gmv-2026-09-02-r1","run_id":"compact-rienet-volatility-drag-mitigation-leveraged-gmv-2026-09-02-r1-u3","kanban_task_id":"t_54d4eaf1","cohort":"BTCUSDT/1d","symbol":"BTCUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"cl_raw":0,"cl_shrink":0,"cl_mp":1,"lb_250":1,"lb_500":0,"lb_750":0,"lb_1200":0},"dca_params":{"spacing_pct":0.02,"size_multiplier":1.0,"breakeven_tp_pct":0.01,"invalidation_pct":0.1},"params_sha256":"sha256:880cf7c8ceadd388c673ee4684b4ad8216ca91db6c4276023d38db2e43aa7b28","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:df1bd71eb92afe0c4465019818ab354263c2449994bc3e2819d4cf41b6d7861f","bundle_identity_sha256":"sha256:1e1fdf1491008a8bd3b4bf92a35b90accab93e391fbcc687d54e4150ce10762d","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":10217.957975,"sharpe":3.664655,"episodes":74,"max_dd_pct":-0.002478},"oos":{"net_pnl":2776.05086,"sharpe":3.517709,"episodes":16,"max_dd_pct":-0.006492},"full":{"net_pnl":12994.008835,"sharpe":3.634338,"episodes":90,"max_dd_pct":-0.004941,"annualized_return":0.09224609770472707},"robustness":{"fee_2x":{"net_pnl":11516.660687,"sharpe":3.587458,"max_dd_pct":-0.005236},"funding_2x":{"net_pnl":12769.070196,"sharpe":3.611348,"max_dd_pct":-0.004967},"entry_delay_1_bar":{"net_pnl":12094.261993,"sharpe":2.763788,"max_dd_pct":-0.017123},"slippage_2ticks":{"net_pnl":12990.30677,"sharpe":3.634333,"max_dd_pct":-0.004942}},"robustness_stress_floor_net_pnl":11516.660687,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":7,"agreeing":7}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-5730b84e7cdcaa00","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":30,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{"full":{"net_pnl":12994.008835,"sharpe":3.634338,"episodes":90,"max_dd_pct":-0.004941,"annualized_return":0.09224609770472707,"avg_trades_per_year":19.167638483965014}},"baseline_fields_absent_in_leaderboard":[]}}
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

`hb_ready_status: NOT_LOSSLESS`。多資產 covariance／GMV／shared capital／margin dynamics 是重要機制，不能無損縮成單 pair candle controller。

Research-only、not-approved；不能進目前 Hummingbot/Qlib 績效下游，不是 Paper/Testnet/Live approval。普通 non-Scout reconstruction 紀錄可經獨立 provenance/research review 保留，並非 Scout one-file PASS admission。

## Related Wiki records

`quant/compact-rienet-volatility-drag-mitigation-leveraged-gmv-2026-09-02.md` — 本紀錄上列 hash 的原研究 provenance，未修改 Wiki。

## Sources

1. Primary：https://arxiv.org/abs/2607.23068v1
2. Pinned historical source：https://github.com/HCH725/alpha-strategy-research/blob/c405adc4795154334d9d50950795b4711f00445d/compact-rienet-volatility-drag-mitigation-leveraged-gmv-2026-09-02.md
3. Historical baseline/leaderboard archive：https://github.com/HCH725/validated-survivor-research/tree/15c0a95162b60a664b43ac60157225c7300ad789；commit 及 per-baseline raw digests 以上述 Provenance/Evidence 為準，並未聲稱所有 reference 可供匿名讀者直接下載。
