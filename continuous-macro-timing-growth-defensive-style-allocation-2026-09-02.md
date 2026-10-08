---
schema: strategy-research-record-v1
hb_ready_status: NOT_LOSSLESS
title: 'Continuous Timing Signals for Growth-Defensive Style Allocation: Macro Conditioning, Risk Matching, and Walk-Forward Evidence'
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
- https://arxiv.org/abs/2605.20636v2
- https://github.com/HCH725/alpha-strategy-research/blob/c405adc4795154334d9d50950795b4711f00445d/continuous-macro-timing-growth-defensive-style-allocation-2026-09-02.md
- HCH725/validated-survivor-research commit 15c0a95162b60a664b43ac60157225c7300ad789
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Continuous Timing Signals for Growth-Defensive Style Allocation: Macro Conditioning, Risk Matching, and Walk-Forward Evidence

## Provenance

- Family identity：`continuous-macro-timing-growth-defensive-style-allocation-2026-09-02`；本次 consolidation 只按原 baseline family_id，不依 Sharpe 重新排名／挑選。
- Primary source：https://arxiv.org/abs/2605.20636v2。
- 既有 source-backed 研究紀錄：commit `c405adc4795154334d9d50950795b4711f00445d`，`continuous-macro-timing-growth-defensive-style-allocation-2026-09-02.md`，Git blob `b0d7eac7fa09dbbe8c683bc94c1a07d542b95219`。 Wiki 明列這組 reviewed_commit/reviewed_blob；本輪已核對原 Git object。
- `quant/continuous-macro-timing-growth-defensive-style-allocation-2026-09-02.md` 的 raw SHA-256 為 `b55e3218e4b5b18f6cdb7924dff92abd4db7043a5e8ec3385bd733a8eaba4e5b`；它在 review-state 的 `ingested_wiki_records` 中，state 最後審查 commit 為 `2799e34c5c7f8d6f7036e35d9ae7468832712c97`。這是 ingestion provenance，不是本輪 source parity 或逐檔新審查；Wiki bytes 不冒稱與原 Git blob 相同。
- Historical input：`HCH725/validated-survivor-research` commit `15c0a95162b60a664b43ac60157225c7300ad789` 的 `survivors/<survivor_id>/baseline.json`，本家族 4 筆，cohorts：`BNBUSDT/1d`, `BTCUSDT/1d`, `ETHUSDT/1d`, `SOLUSDT/1d`。
- Derived leaderboard：同一 repo `leaderboard/leaderboard.json`，raw SHA-256 `e8fdd38c8468960eee5b574e93d27615635bcb266fe481ab8c1409720d96c42e`；它不是 frozen bundle 本身，也不是採用 gate。

- Source-to-legacy-Qlib mapping gap：family 名称、strategy flags/case IDs 或舊 PASS 不證明原文 source-native signal、模型 weights、universe、因果時序與執行機制一致。除本紀錄明列已釘選的程式規則外，沒有補造代碼對照。paper方法、研究解讀與historical DCA分層保留；尚未證明多個 legacy codes 對應不同完整 core mechanisms，故不任意拆成新策略。

## Economic mechanism

### Source-reported

此來源配置既有 growth-versus-defensive style exposures，以連續 macro-market score 取代離散 regime rules；作者不將 G-D 視為新獨立 alpha anomaly。

### Research interpretation

這是方法／假說的普通研究封存，不是把歷史 survivor 標籤當成新 alpha。機制層分類與單筆 cohort 的 DCA 收益不同；statistical forecast、risk allocator 或負面 study 均不得被默換成已驗證的 crypto 交易規則。

## Signal

Growth / defensive ETF baskets；rate relief、SPY drawdown、VIX stress 與 crowding conditioning → softplus interactions → tanh weights → EWMA smoothing。baseline var_full/var_core/var_rate、sm_ewma/sm_none 是舊變體身份；var_rate 不能被重命名為完整 macro policy，缺少外部 rate-series 映射時更不能默換為價格。

## Required data

需要原文 ETF baskets、rate/yield、SPY、VIX 與 point-in-time macro release/price alignment；不是只需要某一 crypto 的 OHLCV。

Historical cohort resolution、parameters 與 data cutoff 以 Evidence 的原 JSON 為準，不補齊不存在的字段，不降採樣、不改 symbol。baseline 不含完整行情 manifest、signal arrays、model checkpoints 或逐筆 trade ledger；它不是可直接執行的策略定義。

## Execution assumptions

來源摘要是成本後的 G/D allocation 比較；配重、smoothing、turnover 與 portfolio benchmarks 是主體，不是 per-coin long/short DCA。

Historical DCA 參數只代表當時研究配置，並非 paper 原生規則，也不是目前 house overlay。未重新量測 fees、funding、margin/liquidation、slippage、intrabar path 或 fills；hash references 不是原資料 bytes 已重新驗證的宣告。

## Evidence

### Source-reported

本輪讀取 versioned primary landing 的 abstract，確認上述 method-level 主張；更細的 signal 配置以釘選原研究紀錄為轉錄來源，未宣稱已重新逐式審閱整篇 methods 或 source code。原文績效不是下列 crypto baseline metrics。

### Independently reproduced

Not independently reproduced. 本輪只驗 source identity／文件轉錄，沒有 Qlib rerun、Hummingbot reproduction、Paper 或 Testnet。

### Negative evidence

原文摘要承認 selected policy 未在 raw CAGR 上勝過 100% G 或最佳高 G static portfolios。舊 Wiki 的來源長標題含 Bond/Credit Extension，與 pinned v2 landing title 不同；以版本 URL 為準，不把後續擴充內容默認納入 v2。

### HISTORICAL QLIB SURVIVOR EVIDENCE — 非目前 Hummingbot reproduction

以下每個 baseline JSON 保留全部原鍵／數值／null／巢狀結構，唯一刪除 top-level `bundle_path` 的機器絕對路徑。bundle 邏輯定位仍可由 family_id / round_id / run_id 與 survivor ID 找到；不假裝本輪讀取已退役結果盤。每筆獨立列 raw baseline-file SHA-256，它與 `params_sha256`、`bundle_sha256`（檔案 bytes）、`bundle_identity_sha256`（歷史 identity recipe）互不相同。

鍵名 `net_pnl` / `sharpe` / `max_dd_pct` / `annualized_return` 原樣保留，不重命名成 ROI、不對 MDD 改 sign／比例／百分點、不跨 lineage 默認同一 annualization。baseline 欄位缺席不同於 null；不從另一層悄悄補值。`source_verdict: PASS` 與 `neighbourhood.passed` 都是 HISTORICAL，不能解讀成今日 efficacy、source parity 或 HB_READY PASS。

每筆另列 `leaderboard_snapshot`：`additional_fields` 為 derived index 額外欄位，`baseline_field_overrides` 為該 index 與 baseline 不同的完整 top-level 值；空 object 明示無差異。兩者都不回寫 baseline。僅非 null 的 `evidence_manifest_path` 去除原 results-root 絕對前綴，保留 `_survivors/...` 相對 locator；null 留 null。rank / top10 / package PRESENT / FROZEN_ONLY 只是當時 derived state，不能解讀為今天 evidence package bytes 存在或新 forward evidence。

#### sv-722a1e576fcc44d1 — HISTORICAL

Baseline file SHA-256：`503f0acc24a6f439f08cab4d4582addacff06ccdc0f1f4dd0f5785543ca74745`；archive locator：`survivors/sv-722a1e576fcc44d1/baseline.json`。

```json
{"survivor_id":"sv-722a1e576fcc44d1","family_id":"continuous-macro-timing-growth-defensive-style-allocation-2026-09-02","round_id":"continuous-macro-timing-growth-defensive-style-allocation-2026-09-02-r2","run_id":"continuous-macro-timing-growth-defensive-style-allocation-2026-09-02-r2-u3","kanban_task_id":"t_20bec925","cohort":"SOLUSDT/1d","symbol":"SOLUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"var_full":0,"var_core":0,"var_rate":1,"sm_ewma":0,"sm_none":1},"dca_params":{"spacing_pct":0.04,"size_multiplier":1.0,"breakeven_tp_pct":0.02,"invalidation_pct":0.1},"params_sha256":"sha256:1a3b1c79c627b4eaa9ec7372a553bf6c6dad3cd8e944ec61492807c29b59c67e","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:a2fc618d43845bf12f70c293fe3cec830f9a3f696ebcd91a88e91390b675b34a","bundle_identity_sha256":"sha256:6f5471a23d3f87aa3d18deeba8f034415e70bf221fd2f3d02a0f12c4aba563f2","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":35668.871572,"sharpe":2.960556,"episodes":146,"max_dd_pct":-0.100811},"oos":{"net_pnl":8929.482251,"sharpe":3.492191,"episodes":47,"max_dd_pct":-0.037779},"full":{"net_pnl":44984.506448,"sharpe":2.979899,"episodes":193,"max_dd_pct":-0.100811,"annualized_return":0.3193506507323934},"robustness":{"fee_2x":{"net_pnl":41960.852833,"sharpe":2.84814,"max_dd_pct":-0.102943},"funding_2x":{"net_pnl":45685.435443,"sharpe":3.133381,"max_dd_pct":-0.091417},"entry_delay_1_bar":{"net_pnl":37659.422999,"sharpe":2.020478,"max_dd_pct":-0.081222},"slippage_2ticks":{"net_pnl":45606.80052,"sharpe":2.980801,"max_dd_pct":-0.10161}},"robustness_stress_floor_net_pnl":37659.422999,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":0.833333,"passed":true,"neighbours":6,"agreeing":5}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-722a1e576fcc44d1","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":31,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{"full":{"net_pnl":44984.506448,"sharpe":2.979899,"episodes":193,"max_dd_pct":-0.100811,"annualized_return":0.3193506507323934,"avg_trades_per_year":41.10393586005831}},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-8d7b3b52605d27f4 — HISTORICAL

Baseline file SHA-256：`ffa41ef2061c2c1d900385b6620f7450c0f7c120b283a7ee42b93beda171e16d`；archive locator：`survivors/sv-8d7b3b52605d27f4/baseline.json`。

```json
{"survivor_id":"sv-8d7b3b52605d27f4","family_id":"continuous-macro-timing-growth-defensive-style-allocation-2026-09-02","round_id":"continuous-macro-timing-growth-defensive-style-allocation-2026-09-02-r2","run_id":"continuous-macro-timing-growth-defensive-style-allocation-2026-09-02-r2-u3","kanban_task_id":"t_20bec925","cohort":"ETHUSDT/1d","symbol":"ETHUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"var_full":0,"var_core":1,"var_rate":0,"sm_ewma":0,"sm_none":1},"dca_params":{"spacing_pct":0.02,"size_multiplier":1.1,"breakeven_tp_pct":0.01,"invalidation_pct":0.1},"params_sha256":"sha256:e9745629906243a5796ae24ccf586bc60dae2d133c6ee5d52522caadf9867e20","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:a2fc618d43845bf12f70c293fe3cec830f9a3f696ebcd91a88e91390b675b34a","bundle_identity_sha256":"sha256:6f5471a23d3f87aa3d18deeba8f034415e70bf221fd2f3d02a0f12c4aba563f2","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":12398.295022,"sharpe":2.744102,"episodes":73,"max_dd_pct":-0.002321},"oos":{"net_pnl":4841.076983,"sharpe":4.352443,"episodes":27,"max_dd_pct":-0.000603},"full":{"net_pnl":17239.372005,"sharpe":2.995313,"episodes":100,"max_dd_pct":-0.002321,"annualized_return":0.12238446306608469},"robustness":{"fee_2x":{"net_pnl":15182.93533,"sharpe":2.978243,"max_dd_pct":-0.002513},"funding_2x":{"net_pnl":17128.523971,"sharpe":2.955799,"max_dd_pct":-0.002368},"entry_delay_1_bar":{"net_pnl":15247.460118,"sharpe":3.424145,"max_dd_pct":-0.00331},"slippage_2ticks":{"net_pnl":17227.455425,"sharpe":2.995453,"max_dd_pct":-0.002323}},"robustness_stress_floor_net_pnl":15182.93533,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":7,"agreeing":7}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-8d7b3b52605d27f4","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":23,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{"full":{"net_pnl":17239.372005,"sharpe":2.995313,"episodes":100,"max_dd_pct":-0.002321,"annualized_return":0.12238446306608469,"avg_trades_per_year":21.29737609329446}},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-c5ace37234e40ab4 — HISTORICAL

Baseline file SHA-256：`5554a16e07859e72d17f41072d3649f10902ca447a65494446ca3832db958021`；archive locator：`survivors/sv-c5ace37234e40ab4/baseline.json`。

```json
{"survivor_id":"sv-c5ace37234e40ab4","family_id":"continuous-macro-timing-growth-defensive-style-allocation-2026-09-02","round_id":"continuous-macro-timing-growth-defensive-style-allocation-2026-09-02-r2","run_id":"continuous-macro-timing-growth-defensive-style-allocation-2026-09-02-r2-u3","kanban_task_id":"t_20bec925","cohort":"BNBUSDT/1d","symbol":"BNBUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"var_full":1,"var_core":0,"var_rate":0,"sm_ewma":0,"sm_none":1},"dca_params":{"spacing_pct":0.03,"size_multiplier":1.0,"breakeven_tp_pct":0.01,"invalidation_pct":0.1},"params_sha256":"sha256:d8810fa5fda638d95599e886ef699c83ea1a85a5c574c881a468afdd9fdc8db2","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:a2fc618d43845bf12f70c293fe3cec830f9a3f696ebcd91a88e91390b675b34a","bundle_identity_sha256":"sha256:6f5471a23d3f87aa3d18deeba8f034415e70bf221fd2f3d02a0f12c4aba563f2","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":4461.329185,"sharpe":2.622978,"episodes":33,"max_dd_pct":-0.00286},"oos":{"net_pnl":2607.594391,"sharpe":2.917569,"episodes":27,"max_dd_pct":-0.012258},"full":{"net_pnl":7068.923575,"sharpe":2.600303,"episodes":60,"max_dd_pct":-0.010738,"annualized_return":0.050183174653523635},"robustness":{"fee_2x":{"net_pnl":6184.957798,"sharpe":2.465688,"max_dd_pct":-0.011929},"funding_2x":{"net_pnl":7090.257154,"sharpe":2.59166,"max_dd_pct":-0.010841},"entry_delay_1_bar":{"net_pnl":6193.242323,"sharpe":2.412699,"max_dd_pct":-0.00698},"slippage_2ticks":{"net_pnl":6871.645358,"sharpe":2.522713,"max_dd_pct":-0.010818}},"robustness_stress_floor_net_pnl":6184.957798,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":7,"agreeing":7}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-c5ace37234e40ab4","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":39,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{"full":{"net_pnl":7068.923575,"sharpe":2.600303,"episodes":60,"max_dd_pct":-0.010738,"annualized_return":0.050183174653523635,"avg_trades_per_year":12.778425655976676}},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-e344aacf000aa5bf — HISTORICAL

Baseline file SHA-256：`20bfab11f749afc0b1e3d1e60d62749951c155adbc8ac48a72233642cc7ae7b5`；archive locator：`survivors/sv-e344aacf000aa5bf/baseline.json`。

```json
{"survivor_id":"sv-e344aacf000aa5bf","family_id":"continuous-macro-timing-growth-defensive-style-allocation-2026-09-02","round_id":"continuous-macro-timing-growth-defensive-style-allocation-2026-09-02-r2","run_id":"continuous-macro-timing-growth-defensive-style-allocation-2026-09-02-r2-u3","kanban_task_id":"t_20bec925","cohort":"BTCUSDT/1d","symbol":"BTCUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"var_full":0,"var_core":0,"var_rate":1,"sm_ewma":0,"sm_none":1},"dca_params":{"spacing_pct":0.02,"size_multiplier":1.0,"breakeven_tp_pct":0.01,"invalidation_pct":0.1},"params_sha256":"sha256:faf8978d4a5317caa83eb053461311600fee69bf5bf2f0811953315779b39dc9","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:a2fc618d43845bf12f70c293fe3cec830f9a3f696ebcd91a88e91390b675b34a","bundle_identity_sha256":"sha256:6f5471a23d3f87aa3d18deeba8f034415e70bf221fd2f3d02a0f12c4aba563f2","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":20552.159417,"sharpe":4.604031,"episodes":146,"max_dd_pct":-0.009634},"oos":{"net_pnl":5406.554787,"sharpe":4.048324,"episodes":47,"max_dd_pct":-0.016199},"full":{"net_pnl":25958.714204,"sharpe":4.499752,"episodes":193,"max_dd_pct":-0.009829,"annualized_return":0.1842841664319172},"robustness":{"fee_2x":{"net_pnl":22633.805244,"sharpe":4.337589,"max_dd_pct":-0.011172},"funding_2x":{"net_pnl":25424.418816,"sharpe":4.474807,"max_dd_pct":-0.010068},"entry_delay_1_bar":{"net_pnl":14217.18326,"sharpe":0.682629,"max_dd_pct":-0.291703},"slippage_2ticks":{"net_pnl":26042.742636,"sharpe":4.517973,"max_dd_pct":-0.009815}},"robustness_stress_floor_net_pnl":14217.18326,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":6,"agreeing":6}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-e344aacf000aa5bf","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":25,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{"full":{"net_pnl":25958.714204,"sharpe":4.499752,"episodes":193,"max_dd_pct":-0.009829,"annualized_return":0.1842841664319172,"avg_trades_per_year":41.10393586005831}},"baseline_fields_absent_in_leaderboard":[]}}
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

`hb_ready_status: NOT_LOSSLESS`。macro inputs、VIX/rates、多 ETF baskets 與跨資產 capital allocation 不符合 OHLCV-only single-pair 限制。

Research-only、not-approved；不能進目前 Hummingbot/Qlib 績效下游，不是 Paper/Testnet/Live approval。普通 non-Scout reconstruction 紀錄可經獨立 provenance/research review 保留，並非 Scout one-file PASS admission。

## Related Wiki records

`quant/continuous-macro-timing-growth-defensive-style-allocation-2026-09-02.md` — 本紀錄上列 hash 的原研究 provenance，未修改 Wiki。

## Sources

1. Primary：https://arxiv.org/abs/2605.20636v2
2. Pinned historical source：https://github.com/HCH725/alpha-strategy-research/blob/c405adc4795154334d9d50950795b4711f00445d/continuous-macro-timing-growth-defensive-style-allocation-2026-09-02.md
3. Historical baseline/leaderboard archive：https://github.com/HCH725/validated-survivor-research/tree/15c0a95162b60a664b43ac60157225c7300ad789；commit 及 per-baseline raw digests 以上述 Provenance/Evidence 為準，並未聲稱所有 reference 可供匿名讀者直接下載。
