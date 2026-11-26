# 自动化执行记录：zdzheng.xyz 论文详情页 SEO/GEO 24h 复查

## 2026-11-26 14:00 GMT+8（首次执行）
- 确认线上已是 11-25 新版（ImageObject / abstract 均在），排除"部署未生效"分支。
- 逐项比对 30 项，写入 `/Users/zhengzhedong/Desktop/geo-recheck-2026-11-26.md`。
- 关键结论：
  - 源码/抓取层 5 项改动全部生效（meta desc=摘要开头、citation_* 全在 head/body 0、og:image→teaser、JSON-LD 补 image+abstract、sitemap lastmod=11-25）。
  - 排名四项全部 UNKNOWN：本环境取不到 Google/Bing/DDG SERP（Google 纯 JS 壳、Bing b_algo=0、DDG 202、Mojeek 0 结果），内置搜索接口是聚合器非 SERP。已拒绝据此判定升降。
  - 最大新发现（P0）：Can-Visi2026 站点标题 "Reason" + 无连字符，与 arXiv 2604.05377 v2 官方 "Can Vision-Language Models Think from the Sky?" 不一致；GitHub README 与 lacuna 均用 Think。
  - 其他未修复旧问题：H2=0（Abstract 是 p/strong）、description 硬切在词中、预印本 isPartOf 把 arXiv 编号当刊名、17/100 篇无 teaser（og 回退 logo 且 twitter:card 降为 summary）、可见正文 0 次 "University of Macau"、llms-full.txt 停在 09-16 缺 5 篇、PDF 20,587,838 B 未压缩。
- 下次执行建议：先确认是否能拿到 GSC/SERP 数据源；若仍不能，排名项直接标 UNKNOWN，把精力放在 llms-full.txt 重建与 17 篇 teaser 补齐的验证上。
