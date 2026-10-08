---
schema: strategy-research-record-v1
hb_ready_status: NOT_LOSSLESS
title: 'Asymmetric Volatility and Coherent Tail-Risk Optimization for Semiconductor-Concentrated ETFs: GJR-GARCH-t Modeling and Long-Short CVaR
  Allocation'
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
- https://arxiv.org/abs/2607.16450v1
- https://github.com/HCH725/alpha-strategy-research/blob/c405adc4795154334d9d50950795b4711f00445d/taiwan-semiconductor-etf-asymmetric-volatility-cvar-rachev-ratio-2026-09-02.md
- HCH725/validated-survivor-research commit 15c0a95162b60a664b43ac60157225c7300ad789
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Asymmetric Volatility and Coherent Tail-Risk Optimization for Semiconductor-Concentrated ETFs: GJR-GARCH-t Modeling and Long-Short CVaR Allocation

## Provenance

- Family identity：`taiwan-semiconductor-etf-asymmetric-volatility-cvar-rachev-ratio-2026-09-02`；本次 consolidation 只按原 baseline family_id，不依 Sharpe 重新排名／挑選。
- Primary source：https://arxiv.org/abs/2607.16450v1。
- 既有 source-backed 研究紀錄：commit `c405adc4795154334d9d50950795b4711f00445d`，`taiwan-semiconductor-etf-asymmetric-volatility-cvar-rachev-ratio-2026-09-02.md`，Git blob `170252e075a5f0d2ac85a06aeedce6a89ca60655`。 Wiki 明列這組 reviewed_commit/reviewed_blob；本輪已核對原 Git object。
- `quant/taiwan-semiconductor-etf-asymmetric-volatility-cvar-rachev-ratio-2026-09-02.md` 的 raw SHA-256 為 `acaf7f636d45e7857e5523b6508bc79ba1b1b7266883462594e5e5a8a4611a6e`；它在 review-state 的 `ingested_wiki_records` 中，state 最後審查 commit 為 `2799e34c5c7f8d6f7036e35d9ae7468832712c97`。這是 ingestion provenance，不是本輪 source parity 或逐檔新審查；Wiki bytes 不冒稱與原 Git blob 相同。
- Historical input：`HCH725/validated-survivor-research` commit `15c0a95162b60a664b43ac60157225c7300ad789` 的 `survivors/<survivor_id>/baseline.json`，本家族 3 筆，cohorts：`BNBUSDT/1d`, `BTCUSDT/1d`, `ETHUSDT/1d`。
- Derived leaderboard：同一 repo `leaderboard/leaderboard.json`，raw SHA-256 `e8fdd38c8468960eee5b574e93d27615635bcb266fe481ab8c1409720d96c42e`；它不是 frozen bundle 本身，也不是採用 gate。

- Source-to-legacy-Qlib mapping gap：family 名称、strategy flags/case IDs 或舊 PASS 不證明原文 source-native signal、模型 weights、universe、因果時序與執行機制一致。除本紀錄明列已釘選的程式規則外，沒有補造代碼對照。paper方法、研究解讀與historical DCA分層保留；尚未證明多個 legacy codes 對應不同完整 core mechanisms，故不任意拆成新策略。

## Economic mechanism

### Source-reported

來源比較 Taiwan-exposed ETFs 的 heavy tails、asymmetric conditional volatility 與 mean-variance/CVaR portfolio allocation；Sharpe/STARR 與 Rachev ratio 可給出不同排名，並不一致支持 CVaR 勝出。

### Research interpretation

這是方法／假說的普通研究封存，不是把歷史 survivor 標籤當成新 alpha。機制層分類與單筆 cohort 的 DCA 收益不同；statistical forecast、risk allocator 或負面 study 均不得被默換成已驗證的 crypto 交易規則。

## Signal

Tail diagnostics / GJR-GARCH conditional variance 與 scenario returns → mean-variance 或 CVaR constrained weights → portfolio risk comparisons。baseline cvar_alpha/short_budget 保留，但沒有證明參數、training windows 或 weight constraints 與原文完全一致；不得自創依 tail index 的 crypto entry rule。

## Required data

pinned 原文摘要明列 thirty US-listed ETFs、February 2015–February 2025；adjusted return panel、risk-free comparison 與 portfolio scenarios。舊 Wiki 的 31-ETF 數與該摘要不一致，這不是 crypto baseline universe。

Historical cohort resolution、parameters 與 data cutoff 以 Evidence 的原 JSON 為準，不補齊不存在的字段，不降採樣、不改 symbol。baseline 不含完整行情 manifest、signal arrays、model checkpoints 或逐筆 trade ledger；它不是可直接執行的策略定義。

## Execution assumptions

多 ETF 配重、long/short constraint 與成本/financing 需各自核實；crypto DCA 假定不是 source-native tail-risk allocator。

Historical DCA 參數只代表當時研究配置，並非 paper 原生規則，也不是目前 house overlay。未重新量測 fees、funding、margin/liquidation、slippage、intrabar path 或 fills；hash references 不是原資料 bytes 已重新驗證的宣告。

## Evidence

### Source-reported

本輪讀取 versioned primary landing 的 abstract，確認上述 method-level 主張；更細的 signal 配置以釘選原研究紀錄為轉錄來源，未宣稱已重新逐式審閱整篇 methods 或 source code。原文績效不是下列 crypto baseline metrics。

### Independently reproduced

Not independently reproduced. 本輪只驗 source identity／文件轉錄，沒有 Qlib rerun、Hummingbot reproduction、Paper 或 Testnet。

### Negative evidence

pinned 摘要指出 apparent squared-return long memory 主要可由 conditional heteroskedasticity 解釋，CVaR allocations 更 concentrated；舊 Wiki 的 genuine fractional-memory／通用尾部優勢措辭過強。本輪以原文限定表述，不承接那些結論。

### HISTORICAL QLIB SURVIVOR EVIDENCE — 非目前 Hummingbot reproduction

以下每個 baseline JSON 保留全部原鍵／數值／null／巢狀結構，唯一刪除 top-level `bundle_path` 的機器絕對路徑。bundle 邏輯定位仍可由 family_id / round_id / run_id 與 survivor ID 找到；不假裝本輪讀取已退役結果盤。每筆獨立列 raw baseline-file SHA-256，它與 `params_sha256`、`bundle_sha256`（檔案 bytes）、`bundle_identity_sha256`（歷史 identity recipe）互不相同。

鍵名 `net_pnl` / `sharpe` / `max_dd_pct` / `annualized_return` 原樣保留，不重命名成 ROI、不對 MDD 改 sign／比例／百分點、不跨 lineage 默認同一 annualization。baseline 欄位缺席不同於 null；不從另一層悄悄補值。`source_verdict: PASS` 與 `neighbourhood.passed` 都是 HISTORICAL，不能解讀成今日 efficacy、source parity 或 HB_READY PASS。

每筆另列 `leaderboard_snapshot`：`additional_fields` 為 derived index 額外欄位，`baseline_field_overrides` 為該 index 與 baseline 不同的完整 top-level 值；空 object 明示無差異。兩者都不回寫 baseline。僅非 null 的 `evidence_manifest_path` 去除原 results-root 絕對前綴，保留 `_survivors/...` 相對 locator；null 留 null。rank / top10 / package PRESENT / FROZEN_ONLY 只是當時 derived state，不能解讀為今天 evidence package bytes 存在或新 forward evidence。

#### sv-2cb1e0b9c14df2c6 — HISTORICAL

Baseline file SHA-256：`71a8dafaaa20a19535eadfba7507d808d2378a2bc994b4a44f3792a6766b5825`；archive locator：`survivors/sv-2cb1e0b9c14df2c6/baseline.json`。

```json
{"survivor_id":"sv-2cb1e0b9c14df2c6","family_id":"taiwan-semiconductor-etf-asymmetric-volatility-cvar-rachev-ratio-2026-09-02","round_id":"taiwan-semiconductor-etf-asymmetric-volatility-cvar-rachev-ratio-2026-09-02-r1","run_id":"taiwan-semiconductor-etf-asymmetric-volatility-cvar-rachev-ratio-2026-09-02-r1-u1","kanban_task_id":null,"cohort":"BTCUSDT/1d","symbol":"BTCUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"cvar_alpha":0.01,"short_budget":0.0},"dca_params":{"spacing_pct":0.02,"size_multiplier":1.0,"breakeven_tp_pct":0.01,"invalidation_pct":0.1},"params_sha256":"sha256:6f5e92fd292f5c3501b42c3b4a3be6b917be9ac9a3339e6940e5d211dd6c3e8d","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:5b2c0cc02bb2ea85114dec8fe6914b8ad8c5980a1e0c97c069a75577069c6119","bundle_identity_sha256":"sha256:8243f82e7b80f9dbdf35b914d474d459b1ca52922875f3cc7c4fbb80184acd76","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":78635.14483490455,"sharpe":2.133048439548541,"episodes":802,"max_dd_pct":29.798804048129085},"oos":{"net_pnl":16943.664506345984,"sharpe":1.6595353031496174,"episodes":254,"max_dd_pct":35.47891123775571},"full":{"net_pnl":95578.80934125057,"sharpe":2.0419829848960775,"episodes":1056,"max_dd_pct":29.798804048129085,"annualized_return":0.35623641692008223,"avg_trades_per_year":224.90029154518948},"robustness":{"fee_2x":{"net_pnl":77801.18938001711,"sharpe":1.7320904840442255,"max_dd_pct":30.836827313785374},"funding_2x":{"net_pnl":93695.31617709952,"sharpe":2.0161814443015227,"max_dd_pct":29.798804048129085},"entry_delay_1_bar":{"net_pnl":95488.90615163455,"sharpe":2.0366213581156574,"max_dd_pct":29.878090221889614},"slippage_2ticks":{"net_pnl":93700.70936796867,"sharpe":1.995017745849384,"max_dd_pct":29.804252583279695}},"robustness_stress_floor_net_pnl":77801.18938001711,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":7,"agreeing":7}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-2cb1e0b9c14df2c6","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":54,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-3fb17f06debe2a87 — HISTORICAL

Baseline file SHA-256：`6cedb7d84c9f3ea4dcd1054600123dbf9674711b7b49c98785372ed0a8a44b9d`；archive locator：`survivors/sv-3fb17f06debe2a87/baseline.json`。

```json
{"survivor_id":"sv-3fb17f06debe2a87","family_id":"taiwan-semiconductor-etf-asymmetric-volatility-cvar-rachev-ratio-2026-09-02","round_id":"taiwan-semiconductor-etf-asymmetric-volatility-cvar-rachev-ratio-2026-09-02-r1","run_id":"taiwan-semiconductor-etf-asymmetric-volatility-cvar-rachev-ratio-2026-09-02-r1-u1","kanban_task_id":null,"cohort":"ETHUSDT/1d","symbol":"ETHUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"cvar_alpha":0.05,"short_budget":0.3},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.0,"breakeven_tp_pct":0.02,"invalidation_pct":0.1},"params_sha256":"sha256:dc129c3cfdad9c69caab151d874526a68734531daa411f7e056edddebbbe12ba","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:5b2c0cc02bb2ea85114dec8fe6914b8ad8c5980a1e0c97c069a75577069c6119","bundle_identity_sha256":"sha256:8243f82e7b80f9dbdf35b914d474d459b1ca52922875f3cc7c4fbb80184acd76","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":249277.65884115087,"sharpe":2.890972305187222,"episodes":729,"max_dd_pct":23.349760271243767},"oos":{"net_pnl":77248.2212656702,"sharpe":3.0621293531383706,"episodes":216,"max_dd_pct":18.486279487530325},"full":{"net_pnl":326525.880106821,"sharpe":2.803175812230998,"episodes":945,"max_dd_pct":23.349760271243767,"annualized_return":0.6934939962072106,"avg_trades_per_year":201.26020408163262},"robustness":{"fee_2x":{"net_pnl":291921.3985513685,"sharpe":2.557881030940823,"max_dd_pct":24.897854587831407},"funding_2x":{"net_pnl":327798.4367477878,"sharpe":2.8083596621029883,"max_dd_pct":23.349760271243767},"entry_delay_1_bar":{"net_pnl":328777.4754379296,"sharpe":2.8304874707715193,"max_dd_pct":23.69930969843104},"slippage_2ticks":{"net_pnl":326377.1835278295,"sharpe":2.801923293775912,"max_dd_pct":23.293154501908948}},"robustness_stress_floor_net_pnl":291921.3985513685,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":0.8571428571428571,"passed":true,"neighbours":7,"agreeing":6}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-3fb17f06debe2a87","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":35,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-82183f837a94b6c2 — HISTORICAL

Baseline file SHA-256：`27985e7e0b201eaff4f689fefcb8ffe34ee038d6a41f5a4e0b339f0d8cf62327`；archive locator：`survivors/sv-82183f837a94b6c2/baseline.json`。

```json
{"survivor_id":"sv-82183f837a94b6c2","family_id":"taiwan-semiconductor-etf-asymmetric-volatility-cvar-rachev-ratio-2026-09-02","round_id":"taiwan-semiconductor-etf-asymmetric-volatility-cvar-rachev-ratio-2026-09-02-r1","run_id":"taiwan-semiconductor-etf-asymmetric-volatility-cvar-rachev-ratio-2026-09-02-r1-u1","kanban_task_id":null,"cohort":"BNBUSDT/1d","symbol":"BNBUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"cvar_alpha":0.05,"short_budget":0.3},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.0,"breakeven_tp_pct":0.02,"invalidation_pct":0.1},"params_sha256":"sha256:dc129c3cfdad9c69caab151d874526a68734531daa411f7e056edddebbbe12ba","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:5b2c0cc02bb2ea85114dec8fe6914b8ad8c5980a1e0c97c069a75577069c6119","bundle_identity_sha256":"sha256:8243f82e7b80f9dbdf35b914d474d459b1ca52922875f3cc7c4fbb80184acd76","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":170458.86125268275,"sharpe":2.0366377429108518,"episodes":605,"max_dd_pct":32.808569161811036},"oos":{"net_pnl":40223.375843898044,"sharpe":1.5463579991572491,"episodes":153,"max_dd_pct":67.65430138826315},"full":{"net_pnl":211531.9570626144,"sharpe":1.9379638467682752,"episodes":757,"max_dd_pct":32.808569161811036,"annualized_return":0.5588019674827964,"avg_trades_per_year":161.22113702623906},"robustness":{"fee_2x":{"net_pnl":185143.0046900072,"sharpe":1.7374623047665865,"max_dd_pct":33.8919122716035},"funding_2x":{"net_pnl":211548.12128394502,"sharpe":1.9396332081026133,"max_dd_pct":32.808569161811036},"entry_delay_1_bar":{"net_pnl":211342.40162270938,"sharpe":1.9322519471335726,"max_dd_pct":32.93760309011236},"slippage_2ticks":{"net_pnl":211287.21421593457,"sharpe":1.9365823246085119,"max_dd_pct":32.85006721818337}},"robustness_stress_floor_net_pnl":185143.0046900072,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":0.8571428571428571,"passed":true,"neighbours":7,"agreeing":6}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-82183f837a94b6c2","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":56,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
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

`hb_ready_status: NOT_LOSSLESS`。cross-asset ETF allocation、tail-risk optimizer/shared capital 與未確認 execution mapping 不符合單 pair OHLCV semantics。

Research-only、not-approved；不能進目前 Hummingbot/Qlib 績效下游，不是 Paper/Testnet/Live approval。普通 non-Scout reconstruction 紀錄可經獨立 provenance/research review 保留，並非 Scout one-file PASS admission。

## Related Wiki records

`quant/taiwan-semiconductor-etf-asymmetric-volatility-cvar-rachev-ratio-2026-09-02.md` — 本紀錄上列 hash 的原研究 provenance，未修改 Wiki。

## Sources

1. Primary：https://arxiv.org/abs/2607.16450v1
2. Pinned historical source：https://github.com/HCH725/alpha-strategy-research/blob/c405adc4795154334d9d50950795b4711f00445d/taiwan-semiconductor-etf-asymmetric-volatility-cvar-rachev-ratio-2026-09-02.md
3. Historical baseline/leaderboard archive：https://github.com/HCH725/validated-survivor-research/tree/15c0a95162b60a664b43ac60157225c7300ad789；commit 及 per-baseline raw digests 以上述 Provenance/Evidence 為準，並未聲稱所有 reference 可供匿名讀者直接下載。
