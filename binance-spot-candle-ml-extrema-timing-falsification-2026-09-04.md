---
schema: strategy-research-record-v1
hb_ready_status: NOT_LOSSLESS
title: 'Binance Spot Candle ML Extrema Timing Falsification: Predict-Then-Optimize Disconnect and Coverage Risk'
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
- https://arxiv.org/abs/2607.19453v1
- https://github.com/HCH725/alpha-strategy-research/blob/4721f59f4e3c2dda7ea30118dc509e8caab139ed/binance-spot-candle-ml-extrema-timing-falsification-2026-09-04.md
- HCH725/validated-survivor-research commit 15c0a95162b60a664b43ac60157225c7300ad789
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Binance Spot Candle ML Extrema Timing Falsification: Predict-Then-Optimize Disconnect and Coverage Risk

## Provenance

- Family identity：`binance-spot-candle-ml-extrema-timing-falsification-2026-09-04`；本次 consolidation 只按原 baseline family_id，不依 Sharpe 重新排名／挑選。
- Primary source：https://arxiv.org/abs/2607.19453v1。
- 既有 source-backed 研究紀錄：commit `4721f59f4e3c2dda7ea30118dc509e8caab139ed`，`binance-spot-candle-ml-extrema-timing-falsification-2026-09-04.md`，Git blob `8eff533c80069ff6f82b40bbccbdb76f63987d2c`。 本紀錄未捏造不存在的逐檔 reviewed_commit；採可回收的最初 root-record commit。
- `quant/binance-spot-candle-ml-extrema-timing-falsification-2026-09-04.md` 的 raw SHA-256 為 `1e55e4d4ad42ea210244948c9651fed0710c382e808575f14b33910c2d204b66`；它在 review-state 的 `ingested_wiki_records` 中，state 最後審查 commit 為 `2799e34c5c7f8d6f7036e35d9ae7468832712c97`。這是 ingestion provenance，不是本輪 source parity 或逐檔新審查；Wiki bytes 不冒稱與原 Git blob 相同。
- Historical input：`HCH725/validated-survivor-research` commit `15c0a95162b60a664b43ac60157225c7300ad789` 的 `survivors/<survivor_id>/baseline.json`，本家族 5 筆，cohorts：`BNBUSDT/1d`, `BTCUSDT/1d`, `BTCUSDT/5m`, `ETHUSDT/1d`, `ETHUSDT/5m`。
- Derived leaderboard：同一 repo `leaderboard/leaderboard.json`，raw SHA-256 `e8fdd38c8468960eee5b574e93d27615635bcb266fe481ab8c1409720d96c42e`；它不是 frozen bundle 本身，也不是採用 gate。

- Source-to-legacy-Qlib mapping gap：family 名称、strategy flags/case IDs 或舊 PASS 不證明原文 source-native signal、模型 weights、universe、因果時序與執行機制一致。除本紀錄明列已釘選的程式規則外，沒有補造代碼對照。paper方法、研究解讀與historical DCA分層保留；尚未證明多個 legacy codes 對應不同完整 core mechanisms，故不任意拆成新策略。

## Economic mechanism

### Source-reported

來源是對 candle-based ML 市場擇時的反證研究：能辨識局部極值或排序未來報酬，不代表因果入場、barrier exits 與成本之後仍有交易價值。原文摘要的後期證據為負面，並揭露曾被使用過的 holdout、未 purge 的標籤與 same-close 樂觀入場。

### Research interpretation

這是方法／假說的普通研究封存，不是把歷史 survivor 標籤當成新 alpha。機制層分類與單筆 cohort 的 DCA 收益不同；statistical forecast、risk allocator 或負面 study 均不得被默換成已驗證的 crypto 交易規則。

## Signal

研究紀錄列出 mandatory-daily 十幣排序、5-minute 局部極值偵測、daily extrema adaptation 與月度 rotation controls。局部極值的 centered-window / future-rebound 條件是訓練標籤，不能在交易時直接當已知訊號。不同實驗有各自模型、門檻、退出與成本；此處不把它們合成一條 crypto 訊號。baseline 的 strategy_case 只是舊實驗代碼，未回收可信的逐 case source-to-run 對照。

## Required data

來源涉及 Binance Spot 多幣 1-minute、5-minute、daily klines，並需 point-in-time 選幣、purged forward labels 與獨立 evaluation boundaries。baseline cohorts 的市場型態及資料來源不得僅由 USDT symbol 推論為原文 Spot。

Historical cohort resolution、parameters 與 data cutoff 以 Evidence 的原 JSON 為準，不補齊不存在的字段，不降採樣、不改 symbol。baseline 不含完整行情 manifest、signal arrays、model checkpoints 或逐筆 trade ledger；它不是可直接執行的策略定義。

## Execution assumptions

歷史研究紀錄描述 next-open 執行、barrier / timeout exits、同 bar adverse stop-first 與明列 round-trip cost；不是現行 same-bar-close house overlay。mandatory selection、Spot sell-to-cash 與 perpetual short 不等價。

Historical DCA 參數只代表當時研究配置，並非 paper 原生規則，也不是目前 house overlay。未重新量測 fees、funding、margin/liquidation、slippage、intrabar path 或 fills；hash references 不是原資料 bytes 已重新驗證的宣告。

## Evidence

### Source-reported

本輪讀取 versioned primary landing 的 abstract，確認上述 method-level 主張；更細的 signal 配置以釘選原研究紀錄為轉錄來源，未宣稱已重新逐式審閱整篇 methods 或 source code。原文績效不是下列 crypto baseline metrics。

### Independently reproduced

Not independently reproduced. 本輪只驗 source identity／文件轉錄，沒有 Qlib rerun、Hummingbot reproduction、Paper 或 Testnet。

### Negative evidence

原文摘要表示後期 selector / extrema policies 未建立正淨值，操作結論仍為 NO_TRADE。下列舊 survivor PASS 與這個負面原文不能直接互相推翻；映射未證實。

兩個 5m baseline 的 OOS 僅各 3 episodes，卻列 `sharpe=4195.01380305441` 與 `2655.029926074858`；另一筆僅 5 episodes。這些極端值原樣封存，但必須在 equity-marking、annualization、episode definitions 與成本／因果事件未核對前視為不可主張的歷史摘要，不能用 rank=1 或高 Sharpe 當強證據。

### HISTORICAL QLIB SURVIVOR EVIDENCE — 非目前 Hummingbot reproduction

以下每個 baseline JSON 保留全部原鍵／數值／null／巢狀結構，唯一刪除 top-level `bundle_path` 的機器絕對路徑。bundle 邏輯定位仍可由 family_id / round_id / run_id 與 survivor ID 找到；不假裝本輪讀取已退役結果盤。每筆獨立列 raw baseline-file SHA-256，它與 `params_sha256`、`bundle_sha256`（檔案 bytes）、`bundle_identity_sha256`（歷史 identity recipe）互不相同。

鍵名 `net_pnl` / `sharpe` / `max_dd_pct` / `annualized_return` 原樣保留，不重命名成 ROI、不對 MDD 改 sign／比例／百分點、不跨 lineage 默認同一 annualization。baseline 欄位缺席不同於 null；不從另一層悄悄補值。`source_verdict: PASS` 與 `neighbourhood.passed` 都是 HISTORICAL，不能解讀成今日 efficacy、source parity 或 HB_READY PASS。

每筆另列 `leaderboard_snapshot`：`additional_fields` 為 derived index 額外欄位，`baseline_field_overrides` 為該 index 與 baseline 不同的完整 top-level 值；空 object 明示無差異。兩者都不回寫 baseline。僅非 null 的 `evidence_manifest_path` 去除原 results-root 絕對前綴，保留 `_survivors/...` 相對 locator；null 留 null。rank / top10 / package PRESENT / FROZEN_ONLY 只是當時 derived state，不能解讀為今天 evidence package bytes 存在或新 forward evidence。

#### sv-05044d47b30fe3de — HISTORICAL

Baseline file SHA-256：`caf67ab9ca6b8462430cb5c34990e311dbab138fa94d067c34b375eb57a96ff6`；archive locator：`survivors/sv-05044d47b30fe3de/baseline.json`。

```json
{"survivor_id":"sv-05044d47b30fe3de","family_id":"binance-spot-candle-ml-extrema-timing-falsification-2026-09-04","round_id":"binance-spot-candle-ml-extrema-timing-falsification-2026-09-04-r1","run_id":"binance-spot-candle-ml-extrema-timing-falsification-2026-09-04-r1-u2","kanban_task_id":null,"cohort":"BNBUSDT/1d","symbol":"BNBUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"strategy_case":4},"dca_params":{"spacing_pct":0.04,"size_multiplier":1.0,"breakeven_tp_pct":0.01,"invalidation_pct":0.1},"params_sha256":"sha256:f906bafd8d50585c1782f75242807b546a5cb00545690af0515678ca3853b467","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:d9a18325ba129ea9f2bb570cf5f197ec31faa4e383f8e780a5eaf58139a72966","bundle_identity_sha256":"sha256:19c7b26f76743f3dfc4fda5a69f4373759c72103104534ba734c16e1bc7734ff","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":135.9006190418675,"sharpe":52.96393982787211,"episodes":11,"max_dd_pct":0.0},"oos":{"net_pnl":107.73043846468526,"sharpe":44.29215292493112,"episodes":5,"max_dd_pct":0.0},"full":{"net_pnl":243.63105750655274,"sharpe":37.93885715668628,"episodes":16,"max_dd_pct":0.0,"annualized_return":0.0017228856949309534,"avg_trades_per_year":3.4075801749271135},"robustness":{"fee_2x":{"net_pnl":216.49632391917316,"sharpe":37.908594228844535,"max_dd_pct":0.0},"funding_2x":{"net_pnl":244.92967384131393,"sharpe":37.716118873647574,"max_dd_pct":0.0},"entry_delay_1_bar":{"net_pnl":196.59865412018928,"sharpe":33.44871613807429,"max_dd_pct":0.0},"slippage_2ticks":{"net_pnl":243.09850179902296,"sharpe":37.885031053686184,"max_dd_pct":0.0}},"robustness_stress_floor_net_pnl":196.59865412018928,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":0.6,"passed":true,"neighbours":5,"agreeing":3}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-05044d47b30fe3de","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":5,"in_top10":true,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-3e4bdb2d38bb330c — HISTORICAL

Baseline file SHA-256：`42de1943bfbc9addca292a0909e9ba9e979b4fd896ef8c2457646edf5048280c`；archive locator：`survivors/sv-3e4bdb2d38bb330c/baseline.json`。

```json
{"survivor_id":"sv-3e4bdb2d38bb330c","family_id":"binance-spot-candle-ml-extrema-timing-falsification-2026-09-04","round_id":"binance-spot-candle-ml-extrema-timing-falsification-2026-09-04-r1","run_id":"binance-spot-candle-ml-extrema-timing-falsification-2026-09-04-r1-u2","kanban_task_id":null,"cohort":"BTCUSDT/5m","symbol":"BTCUSDT","timeframe":"5m","challenger_of":null,"strategy_params":{"strategy_case":4},"dca_params":{"spacing_pct":0.04,"size_multiplier":1.0,"breakeven_tp_pct":0.03,"invalidation_pct":0.1},"params_sha256":"sha256:7b5c980fb736c83d87aff8076fd0e98e73635a21f5b2a92ace34b9e0970e0352","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:d9a18325ba129ea9f2bb570cf5f197ec31faa4e383f8e780a5eaf58139a72966","bundle_identity_sha256":"sha256:19c7b26f76743f3dfc4fda5a69f4373759c72103104534ba734c16e1bc7734ff","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":661.2469608275804,"sharpe":43.81212322070701,"episodes":14,"max_dd_pct":0.0},"oos":{"net_pnl":86.30664206280369,"sharpe":4195.01380305441,"episodes":3,"max_dd_pct":0.0},"full":{"net_pnl":747.5536028903841,"sharpe":42.064346917649885,"episodes":17,"max_dd_pct":0.0,"annualized_return":0.005252090424918476,"avg_trades_per_year":3.620553935860058},"robustness":{"fee_2x":{"net_pnl":721.1636350949476,"sharpe":42.06665936614902,"max_dd_pct":0.0},"funding_2x":{"net_pnl":741.5615827032701,"sharpe":42.1097021615759,"max_dd_pct":0.0},"entry_delay_1_bar":{"net_pnl":748.0343284126404,"sharpe":42.07423265484089,"max_dd_pct":0.0},"slippage_2ticks":{"net_pnl":747.4892371277197,"sharpe":42.063873358741446,"max_dd_pct":0.0}},"robustness_stress_floor_net_pnl":721.1636350949476,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":0.8,"passed":true,"neighbours":5,"agreeing":4}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-3e4bdb2d38bb330c","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":1,"in_top10":true,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-3f1c393a304cb2a3 — HISTORICAL

Baseline file SHA-256：`c3239e519b3637639821b514e9fb19ab558b76d24a742f54505cc347a6bfd989`；archive locator：`survivors/sv-3f1c393a304cb2a3/baseline.json`。

```json
{"survivor_id":"sv-3f1c393a304cb2a3","family_id":"binance-spot-candle-ml-extrema-timing-falsification-2026-09-04","round_id":"binance-spot-candle-ml-extrema-timing-falsification-2026-09-04-r1","run_id":"binance-spot-candle-ml-extrema-timing-falsification-2026-09-04-r1-u2","kanban_task_id":null,"cohort":"ETHUSDT/1d","symbol":"ETHUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"strategy_case":1},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.0,"breakeven_tp_pct":0.01,"invalidation_pct":0.05},"params_sha256":"sha256:e55ee1186aa45624e7ae97a97de24453a7db09ffccae4a232c624c4e2a34aa76","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:d9a18325ba129ea9f2bb570cf5f197ec31faa4e383f8e780a5eaf58139a72966","bundle_identity_sha256":"sha256:19c7b26f76743f3dfc4fda5a69f4373759c72103104534ba734c16e1bc7734ff","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":68140.42313776918,"sharpe":8.58031229005245,"episodes":1364,"max_dd_pct":0.02964455741210078},"oos":{"net_pnl":14280.361527284867,"sharpe":8.547294310030555,"episodes":341,"max_dd_pct":0.08439197910663361},"full":{"net_pnl":82414.78253957965,"sharpe":8.54866341823181,"episodes":1706,"max_dd_pct":0.03324213471238414,"annualized_return":0.32464614136025394,"avg_trades_per_year":363.33323615160344},"robustness":{"fee_2x":{"net_pnl":77031.54905952039,"sharpe":8.16285732755188,"max_dd_pct":0.05545965759005178},"funding_2x":{"net_pnl":81745.83844067706,"sharpe":8.49718458692842,"max_dd_pct":0.0360975228085609},"entry_delay_1_bar":{"net_pnl":82416.74009522478,"sharpe":8.551916763429428,"max_dd_pct":0.03324155585439193},"slippage_2ticks":{"net_pnl":82372.45559064012,"sharpe":8.54599136809673,"max_dd_pct":0.033389435493862425}},"robustness_stress_floor_net_pnl":77031.54905952039,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":0.8333333333333334,"passed":true,"neighbours":6,"agreeing":5}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-3f1c393a304cb2a3","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":9,"in_top10":true,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-5e6ab397d1986280 — HISTORICAL

Baseline file SHA-256：`e22cd529386def9f9aa2d543a967576e327e4c25545d7fd9fd5e22461d5a064d`；archive locator：`survivors/sv-5e6ab397d1986280/baseline.json`。

```json
{"survivor_id":"sv-5e6ab397d1986280","family_id":"binance-spot-candle-ml-extrema-timing-falsification-2026-09-04","round_id":"binance-spot-candle-ml-extrema-timing-falsification-2026-09-04-r1","run_id":"binance-spot-candle-ml-extrema-timing-falsification-2026-09-04-r1-u2","kanban_task_id":null,"cohort":"ETHUSDT/5m","symbol":"ETHUSDT","timeframe":"5m","challenger_of":null,"strategy_params":{"strategy_case":2},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.0,"breakeven_tp_pct":0.01,"invalidation_pct":0.05},"params_sha256":"sha256:3d770d1960413a788e3474ffde2e73b772e0e5b03039c21d7e74b0580b497a6e","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:d9a18325ba129ea9f2bb570cf5f197ec31faa4e383f8e780a5eaf58139a72966","bundle_identity_sha256":"sha256:19c7b26f76743f3dfc4fda5a69f4373759c72103104534ba734c16e1bc7734ff","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":2523.9281603830977,"sharpe":1.9981144712189918,"episodes":338,"max_dd_pct":4.573027697448909},"oos":{"net_pnl":46.66568306833783,"sharpe":0.24006437632436234,"episodes":47,"max_dd_pct":1.8173552928772736},"full":{"net_pnl":2570.5938434514355,"sharpe":1.7618454425949437,"episodes":385,"max_dd_pct":4.539167231574387,"annualized_return":0.01765108588655573,"avg_trades_per_year":81.99489795918366},"robustness":{"fee_2x":{"net_pnl":1710.8579448235148,"sharpe":1.159989844515209,"max_dd_pct":4.977651670818336},"funding_2x":{"net_pnl":2529.1263296887573,"sharpe":1.7341400718928048,"max_dd_pct":4.544898423451718},"entry_delay_1_bar":{"net_pnl":2285.8098926097955,"sharpe":1.590651339359045,"max_dd_pct":2.8516930588079656},"slippage_2ticks":{"net_pnl":2565.0258703946774,"sharpe":1.757911578164526,"max_dd_pct":4.5412534701258656}},"robustness_stress_floor_net_pnl":1710.8579448235148,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":0.8333333333333334,"passed":true,"neighbours":6,"agreeing":5}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-5e6ab397d1986280","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":87,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-dfff537f0647c587 — HISTORICAL

Baseline file SHA-256：`0afb3e8c5ea3274b047eb20b511d3e3291e2d39d9af64d57d12e61bf28d00885`；archive locator：`survivors/sv-dfff537f0647c587/baseline.json`。

```json
{"survivor_id":"sv-dfff537f0647c587","family_id":"binance-spot-candle-ml-extrema-timing-falsification-2026-09-04","round_id":"binance-spot-candle-ml-extrema-timing-falsification-2026-09-04-r1","run_id":"binance-spot-candle-ml-extrema-timing-falsification-2026-09-04-r1-u2","kanban_task_id":null,"cohort":"BTCUSDT/1d","symbol":"BTCUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"strategy_case":4},"dca_params":{"spacing_pct":0.04,"size_multiplier":1.0,"breakeven_tp_pct":0.01,"invalidation_pct":0.05},"params_sha256":"sha256:8e053131c2094cc20af33089378c89f8ddd15115d32ef5fe04a57cd07cb3e436","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:d9a18325ba129ea9f2bb570cf5f197ec31faa4e383f8e780a5eaf58139a72966","bundle_identity_sha256":"sha256:19c7b26f76743f3dfc4fda5a69f4373759c72103104534ba734c16e1bc7734ff","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":107.60638067908377,"sharpe":72.02506070573105,"episodes":11,"max_dd_pct":0.0},"oos":{"net_pnl":27.03380029645207,"sharpe":2655.029926074858,"episodes":3,"max_dd_pct":0.0},"full":{"net_pnl":134.64018097553583,"sharpe":79.1307420379533,"episodes":14,"max_dd_pct":0.0,"annualized_return":0.000953490558757375,"avg_trades_per_year":2.981632653061224},"robustness":{"fee_2x":{"net_pnl":119.56519978390948,"sharpe":79.07879024028206,"max_dd_pct":0.0},"funding_2x":{"net_pnl":134.39295988997816,"sharpe":78.65184654403721,"max_dd_pct":0.0},"entry_delay_1_bar":{"net_pnl":32.734463746020396,"sharpe":1.535282159911478,"max_dd_pct":0.3394551650284234},"slippage_2ticks":{"net_pnl":134.60258355606535,"sharpe":79.14955450134582,"max_dd_pct":0.0}},"robustness_stress_floor_net_pnl":32.734463746020396,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":0.8,"passed":true,"neighbours":5,"agreeing":4}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-dfff537f0647c587","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":2,"in_top10":true,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

## Falsification plan

1. 先恢復 exact source-to-case / model / signal / timing 對照，若不能證明便維持 source-mapping gap；不得以調參 rescue 或另寫 proxy 宣稱復現原文。
2. 若將來另獲執行授權，先用 prefix/suffix perturbation、landed-label checks、formation-to-order timestamps 與 universe alignment 反證 look-ahead；再以同一事件模型核對 fills、funding、fee、margin 及 parameter sensitivity。
3. 保留負面 controls、成本壓力、完整 denominator 與未觀測欄位。對 forecasting / risk-control 主張，須各有 baseline/ablation，不能單靠一個 per-coin Sharpe 認定方法有效。
4. 以上僅是未來 research tests，不是這張 archival PR 已跑過的測試，也不授權 backtest、pipeline 或交易。

## Crypto portability

來源本身含 crypto evidence，但目標、成本、時間尺度與 policy mapping 不能由旧 survivors 自動證實。

## Limitations

- baseline 與 leaderboard 是 frozen/derived archival summaries，不包含完整 robustness grid 的所有未勝出 cases、鄰居逐筆結果、source-native code/model 或事件序列；現存四 stress grids 和 neighborhood summary 全保留，缺失資料不捏造。
- historical/OOS/full 的細分日期與 split recipe 未隨 baseline 提供；只保留 exact data cutoff 與原 identity，除有已回收 source 證據外不推論 slice endpoints。
- 存在 survivor selection、搜尋過的 evaluation periods、樣本數不足、資料／成本／模型身份尚未回收的限制；不因 baseline 帶 PASS 而移除。
- Metric definitions/units 可跨 engine lineage 不同；baseline 与 derived leaderboard 的補算差異各自保留，不混寫成新的績效真值。

## Implementation status

Not implemented in the current research/runtime stack. Historical code / baselines 在此只作 Provenance/Evidence；本輪未實作、修復、採用或部署策略。

## Adoption boundary

`hb_ready_status: NOT_LOSSLESS`。1m/5m 來源、跨幣 ranking、next-open 與 barrier path rules 不符合 pinned 單 pair／same-bar-close semantics；精確 case 映射也未恢復。

Research-only、not-approved；不能進目前 Hummingbot/Qlib 績效下游，不是 Paper/Testnet/Live approval。普通 non-Scout reconstruction 紀錄可經獨立 provenance/research review 保留，並非 Scout one-file PASS admission。

## Related Wiki records

`quant/binance-spot-candle-ml-extrema-timing-falsification-2026-09-04.md` — 本紀錄上列 hash 的原研究 provenance，未修改 Wiki。

## Sources

1. Primary：https://arxiv.org/abs/2607.19453v1
2. Pinned historical source：https://github.com/HCH725/alpha-strategy-research/blob/4721f59f4e3c2dda7ea30118dc509e8caab139ed/binance-spot-candle-ml-extrema-timing-falsification-2026-09-04.md
3. Historical baseline/leaderboard archive：https://github.com/HCH725/validated-survivor-research/tree/15c0a95162b60a664b43ac60157225c7300ad789；commit 及 per-baseline raw digests 以上述 Provenance/Evidence 為準，並未聲稱所有 reference 可供匿名讀者直接下載。
