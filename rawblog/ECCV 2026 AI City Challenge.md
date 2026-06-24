# 【ECCV 2026】2026 AI City Challenge 奖项正式公布：冠军送 RTX 5080！附 Track 4 深度解析

随着人工智能向 Physical AI 和真实世界系统迈进，开放基准测试（Open Benchmarks）的重要性日益凸显。今年，**AI City Challenge 迎来了它的第十个年头**。

在此，我们很高兴地向全球研究者和从业者宣布：**2026 AI City Challenge 的奖项已正式确认**。
- 🥇 **各赛道冠军**：将获得 **NVIDIA GeForce RTX 5080** 显卡。
- 🥈 **各赛道亚军**：将获得 **Jetson Orin Nano Super Developer Kit**。

本届挑战赛共设有六个赛道，涵盖感知（Perception）、推理（Reasoning）、Sim2Real 迁移、视频理解（Video Understanding）以及生成式 AI（Generative AI）。我们期待看到来自全球的創新解决方案。

作为 **Track 4** 的负责人，我在此为大家详细解读本赛道的技术细节、挑战重点以及参赛指南。

---

## 🎯 Track 4: Text-Based Person Re-Identification (Sim2Real)
<img width="1808" height="930" alt="image" src="https://github.com/user-attachments/assets/639cf7b2-7371-4944-a537-652ae4a44020" />

Track 4 聚焦于**基于文本的行人重识别（Sim2Real）**。本赛道建立在近期相关基准测试(ICCV2025 Highlight Beyond Walking: A Large-Scale Image-Text Benchmark
for Text-based Person Anomaly Search)的基础之上，重点考察视觉与语言之间的**跨模态推理（Cross-modal reasoning）** 能力。

### 1. 任务定义
参赛者需要解决基于文本的行人检索问题。系统接收自然语言查询（Natural language queries），这些查询不仅描述目标的**外观特征（Appearance）**，还描述其**行为特征（Behaviors）**，甚至包括**异常动作（Anomalous actions）**。模型需要根据这些文本描述，在图像或视频库中准确检索出对应的行人。

### 2. 核心技术挑战：Sim2Real 迁移
本赛道最大的难点在于**合成数据到真实世界的迁移（Sim2Real transfer）**：
- **训练阶段**：模型将在**合成数据（Synthetic data）** 上进行训练。
- **评估阶段**：模型将在**真实世界测试集（Real-world test sets）** 上进行评估。

如何克服合成数据与真实物理世界之间的 Domain Gap（域偏移），是本赛道需要解决的核心科学问题。

### 3. 评估指标
本赛道的准确性将使用 **平均精度均值（mAP, mean Average Precision）** 进行衡量。

---

## 📅 关键时间节点 (Timeline)

目前，比赛已经进入关键阶段。请参赛团队务必关注以下时间节点（所有截止时间均为 **Anywhere on Earth, AoE**）：

- [x] **2026年4月20日**：发布训练集和验证集 *(已完成)*
- [x] **2026年5月28日**：发布评测服务器和测试集 *(已完成)*
- 🔴 **2026年7月10日**：**赛道提交截止 (Challenge track submissions due)**
- 📝 **2026年7月24日**：Workshop 论文提交截止 (Workshop papers due)
- 📩 **2026年8月1日**：录用通知 (Acceptance notification)
- 💻 **2026年8月7日**：获奖候选队伍开源代码提交截止 (Open source by awards candidates due)
- 📄 **2026年8月15日**：Camera-ready 论文提交截止
- 🏆 **2026年9月8日**：在 **ECCV 2026** 现场进行论文宣讲并举行颁奖典礼

> **特别提示**：距离 **7月10日** 的赛道提交截止已非常临近，请尚未提交最终结果的队伍抓紧时间调试模型并在评测服务器上刷榜。

---

## 🔗 参赛指南与资源获取

为了方便大家获取最新信息，以下是官方资源链接：

- **官方网站**：[AI City Challenge 2026 官网](https://www.aicitychallenge.org/)
- **Track 4 详细说明与数据集下载**：[Track 4 赛道主页](https://www.aicitychallenge.org/2026-track4/)
- **评测服务器 (Evaluation Server)**：[官方评测平台链接](https://www.aicitychallenge.org/2026-evaluation-system/) 
- **论文提交系统**：[ECCV 2026 Workshop 提交入口](https://www.aicitychallenge.org/2026-paper-submission/) 

---

## 💡 结语

AI City Challenge 能够走到第十年，离不开所有组织者、合作者以及广大参与者的持续支持。这不仅是一场算法的竞技，更是推动 AI 技术从实验室走向真实物理世界的重要契机。

无论你是高校的研究团队，还是企业的算法工程师，我们都热烈欢迎你的参与。

如果在 Track 4 的备赛过程中，关于数据集、评测规则或 Sim2Real 的技术实现有任何疑问，**欢迎在本文评论区留言交流**，我会尽量为大家解答。

预祝各参赛团队在 ECCV 2026 取得优异成绩！

---
*本文由 AI City Challenge 2026 Track 4 负责人撰写。欢迎转发分享给实验室的同学和同行的朋友。*
