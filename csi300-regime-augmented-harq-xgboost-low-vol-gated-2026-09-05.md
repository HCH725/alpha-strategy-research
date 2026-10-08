---
schema: strategy-research-record-v1
hb_ready_status: NOT_LOSSLESS
title: 'CSI 300 Regime-Augmented HARQ and Walk-Forward XGBoost: Low-Volatility Gated Signal-by-Risk Allocation under Implementation Frictions'
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
- https://arxiv.org/abs/2606.09478v1
- https://github.com/HCH725/alpha-strategy-research/blob/8385e242d1f240219f7f74eb6884da6ea8fad9b1/csi300-regime-augmented-harq-xgboost-low-vol-gated-2026-09-05.md
- HCH725/validated-survivor-research commit 15c0a95162b60a664b43ac60157225c7300ad789
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# CSI 300 Regime-Augmented HARQ and Walk-Forward XGBoost: Low-Volatility Gated Signal-by-Risk Allocation under Implementation Frictions

## Provenance

- Family identity：`csi300-regime-augmented-harq-xgboost-low-vol-gated-2026-09-05`；本次 consolidation 只按原 baseline family_id，不依 Sharpe 重新排名／挑選。
- Primary source：https://arxiv.org/abs/2606.09478v1。
- 既有 source-backed 研究紀錄：commit `8385e242d1f240219f7f74eb6884da6ea8fad9b1`，`csi300-regime-augmented-harq-xgboost-low-vol-gated-2026-09-05.md`，Git blob `3bef347d7c63a7d07184259f3ca542f1d45e910b`。 本紀錄未捏造不存在的逐檔 reviewed_commit；採可回收的最初 root-record commit。
- `quant/csi300-regime-augmented-harq-xgboost-low-vol-gated-2026-09-05.md` 的 raw SHA-256 為 `3f955a19ebf8e5895c9ccba3b3887a62592bd21ebb0d9ccfb93fb527dcc1ca1a`；它在 review-state 的 `ingested_wiki_records` 中，state 最後審查 commit 為 `2799e34c5c7f8d6f7036e35d9ae7468832712c97`。這是 ingestion provenance，不是本輪 source parity 或逐檔新審查；Wiki bytes 不冒稱與原 Git blob 相同。
- Historical input：`HCH725/validated-survivor-research` commit `15c0a95162b60a664b43ac60157225c7300ad789` 的 `survivors/<survivor_id>/baseline.json`，本家族 1 筆，cohorts：`BTCUSDT/1d`。
- Derived leaderboard：同一 repo `leaderboard/leaderboard.json`，raw SHA-256 `e8fdd38c8468960eee5b574e93d27615635bcb266fe481ab8c1409720d96c42e`；它不是 frozen bundle 本身，也不是採用 gate。

- Source-to-legacy-Qlib mapping gap：family 名称、strategy flags/case IDs 或舊 PASS 不證明原文 source-native signal、模型 weights、universe、因果時序與執行機制一致。除本紀錄明列已釘選的程式規則外，沒有補造代碼對照。paper方法、研究解讀與historical DCA分層保留；尚未證明多個 legacy codes 對應不同完整 core mechanisms，故不任意拆成新策略。

## Economic mechanism

### Source-reported

HARQ / Markov-switching GJR-GARCH 的 regime-aware volatility forecasts，進一步餵入 walk-forward XGBoost return prediction。來源強調弱且低波動 regime 集中的方向訊息，需 frictions-aware implementation 才有 defensive value。

### Research interpretation

這是方法／假說的普通研究封存，不是把歷史 survivor 標籤當成新 alpha。機制層分類與單筆 cohort 的 DCA 收益不同；statistical forecast、risk allocator 或負面 study 均不得被默換成已驗證的 crypto 交易規則。

## Signal

5-minute intraday realized variance/quarticity/jump measures → regime-augmented HARQ volatility forecast → return/regime features → XGBoost → low-volatility gating/scaling/turnover control。baseline strategy_case=0 未與完整 two-stage / regime / threshold 證據對齊，不把其單一數字當已驗證規則。

## Required data

來源 CSI 300 high-frequency Chinese equity data，2005–2023；需 session-aware 5-minute realized measures、daily features、point-in-time walk-forward model training。

Historical cohort resolution、parameters 與 data cutoff 以 Evidence 的原 JSON 為準，不補齊不存在的字段，不降採樣、不改 symbol。baseline 不含完整行情 manifest、signal arrays、model checkpoints 或逐筆 trade ledger；它不是可直接執行的策略定義。

## Execution assumptions

Cash index 不等於可直接交易的 futures/ETF；forecast-to-weight、calibrated thresholds 與 turnover controls 有實質影響。原文方法與 daily crypto DCA execution 不能默認相同。

Historical DCA 參數只代表當時研究配置，並非 paper 原生規則，也不是目前 house overlay。未重新量測 fees、funding、margin/liquidation、slippage、intrabar path 或 fills；hash references 不是原資料 bytes 已重新驗證的宣告。

## Evidence

### Source-reported

本輪讀取 versioned primary landing 的 abstract，確認上述 method-level 主張；更細的 signal 配置以釘選原研究紀錄為轉錄來源，未宣稱已重新逐式審閱整篇 methods 或 source code。原文績效不是下列 crypto baseline metrics。

### Independently reproduced

Not independently reproduced. 本輪只驗 source identity／文件轉錄，沒有 Qlib rerun、Hummingbot reproduction、Paper 或 Testnet。

### Negative evidence

來源摘要指出 naive predictive trades 在 realistic costs 後通常失敗，方向預測弱且 state-dependent；較佳 defensive allocation 不等於 unconditional alpha。

唯一 baseline 的 OOS 僅 `episodes=4`，摘要 `sharpe=57.62405574583328`；樣本供給與 metric construction 尚未核對，不能用極高摘要 Sharpe 補足 statistical confidence 或 source mapping。

### HISTORICAL QLIB SURVIVOR EVIDENCE — 非目前 Hummingbot reproduction

以下每個 baseline JSON 保留全部原鍵／數值／null／巢狀結構，唯一刪除 top-level `bundle_path` 的機器絕對路徑。bundle 邏輯定位仍可由 family_id / round_id / run_id 與 survivor ID 找到；不假裝本輪讀取已退役結果盤。每筆獨立列 raw baseline-file SHA-256，它與 `params_sha256`、`bundle_sha256`（檔案 bytes）、`bundle_identity_sha256`（歷史 identity recipe）互不相同。

鍵名 `net_pnl` / `sharpe` / `max_dd_pct` / `annualized_return` 原樣保留，不重命名成 ROI、不對 MDD 改 sign／比例／百分點、不跨 lineage 默認同一 annualization。baseline 欄位缺席不同於 null；不從另一層悄悄補值。`source_verdict: PASS` 與 `neighbourhood.passed` 都是 HISTORICAL，不能解讀成今日 efficacy、source parity 或 HB_READY PASS。

每筆另列 `leaderboard_snapshot`：`additional_fields` 為 derived index 額外欄位，`baseline_field_overrides` 為該 index 與 baseline 不同的完整 top-level 值；空 object 明示無差異。兩者都不回寫 baseline。僅非 null 的 `evidence_manifest_path` 去除原 results-root 絕對前綴，保留 `_survivors/...` 相對 locator；null 留 null。rank / top10 / package PRESENT / FROZEN_ONLY 只是當時 derived state，不能解讀為今天 evidence package bytes 存在或新 forward evidence。

#### sv-dc22afb6013dc7c3 — HISTORICAL

Baseline file SHA-256：`7d3ab0a494aa5a248264770aa806cf05737bb9b7e8e117eefeab7750c55eeaf7`；archive locator：`survivors/sv-dc22afb6013dc7c3/baseline.json`。

```json
{"survivor_id":"sv-dc22afb6013dc7c3","family_id":"csi300-regime-augmented-harq-xgboost-low-vol-gated-2026-09-05","round_id":"csi300-regime-augmented-harq-xgboost-low-vol-gated-2026-09-05-r1","run_id":"csi300-regime-augmented-harq-xgboost-low-vol-gated-2026-09-05-r1-u3","kanban_task_id":null,"cohort":"BTCUSDT/1d","symbol":"BTCUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"strategy_case":0},"dca_params":{"spacing_pct":0.04,"size_multiplier":1.0,"breakeven_tp_pct":0.01,"invalidation_pct":0.1},"params_sha256":"sha256:94738e8dca3551593e59358f736aa0ca7249c9acc5d8f3d8d4ca2ed8911a9ed6","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:a11da954da50a868db61978857f29054532116d5c166bc7f9a4923b9ce2ffeb4","bundle_identity_sha256":"sha256:5350dc2c24d47bb72f8b5c5d31e710a8ff33cb6c97c578508aecdf786d71cfc1","source_disposition_band":"SURVIVOR_FOUND","source_verdict":"PASS","historical":{"net_pnl":263.71198958302386,"sharpe":46.5504965934024,"episodes":22,"max_dd_pct":0.0},"oos":{"net_pnl":44.588002517016825,"sharpe":57.62405574583328,"episodes":4,"max_dd_pct":0.0},"full":{"net_pnl":308.2999921000407,"sharpe":47.57740740370327,"episodes":26,"max_dd_pct":0.0,"annualized_return":0.0021783694825598943,"avg_trades_per_year":5.537317784256559},"robustness":{"fee_2x":{"net_pnl":272.1600103902963,"sharpe":48.79163550661641,"max_dd_pct":0.0},"funding_2x":{"net_pnl":292.7915819750479,"sharpe":55.50201638357661,"max_dd_pct":0.0},"entry_delay_1_bar":{"net_pnl":252.18813665696456,"sharpe":21.6485327817058,"max_dd_pct":0.0947496426940466},"slippage_2ticks":{"net_pnl":308.24844489207595,"sharpe":47.57917098495451,"max_dd_pct":0.0}},"robustness_stress_floor_net_pnl":252.18813665696456,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":0.75,"passed":true,"neighbours":4,"agreeing":3}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-dc22afb6013dc7c3","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":4,"in_top10":true,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
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

`hb_ready_status: NOT_LOSSLESS`。intraday-to-daily realized measures、regime/model state 與 cash-index-to-tradable-instrument mapping 尚不能 losslessly 落於 pinned 單 pair OHLCV lane。

Research-only、not-approved；不能進目前 Hummingbot/Qlib 績效下游，不是 Paper/Testnet/Live approval。普通 non-Scout reconstruction 紀錄可經獨立 provenance/research review 保留，並非 Scout one-file PASS admission。

## Related Wiki records

`quant/csi300-regime-augmented-harq-xgboost-low-vol-gated-2026-09-05.md` — 本紀錄上列 hash 的原研究 provenance，未修改 Wiki。

## Sources

1. Primary：https://arxiv.org/abs/2606.09478v1
2. Pinned historical source：https://github.com/HCH725/alpha-strategy-research/blob/8385e242d1f240219f7f74eb6884da6ea8fad9b1/csi300-regime-augmented-harq-xgboost-low-vol-gated-2026-09-05.md
3. Historical baseline/leaderboard archive：https://github.com/HCH725/validated-survivor-research/tree/15c0a95162b60a664b43ac60157225c7300ad789；commit 及 per-baseline raw digests 以上述 Provenance/Evidence 為準，並未聲稱所有 reference 可供匿名讀者直接下載。
