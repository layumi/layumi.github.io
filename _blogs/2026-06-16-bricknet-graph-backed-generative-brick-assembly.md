---
title: 读BrickNet:Graph-Backed Generative Brick Assembly
date: '2026-06-16'
permalink: /blog/bricknet-graph-backed-generative-brick-assembly
tags:
- 是什么 基于graph 匹配部件么
- 基于graph 匹配部件么 先检索部件
- 基于graph 匹配部件么
- 但没细说 graph 部件作为node
- graph 部件作为node 连接作为edge
- 读bricknet graph
---

<img width="960" height="640" alt="image" src="https://github.com/user-attachments/assets/288b97a2-214d-4a27-96d1-d07a0a5ceda4" />


论文地址：https://arxiv.org/pdf/2604.22984

发表于 CVPR2026

代码和数据集 还没放。

<img width="1052" height="516" alt="image" src="https://github.com/user-attachments/assets/32c0f398-5e38-4e02-a743-688be233251e" />


## 读前疑问:

1.  题目中的 Graph-backed 是什么？ 基于Graph 匹配部件么？
2.  先检索部件，再安上？ 那就是2步了，**检索+回归**。是这样么？
3.  如果检索，那pool里几种部件？
4.  如果回归部件位置，那对应的维度是几个？6DoF？
5.  最后，即使回归出位置，怎么拼接？信息量是否足够？是不是还要对应块接触点的 位置回归。
6.  是否是一步完成的？ 还是分了几个部分 再拼接到一起？

注：stud特指lego砖上的凸点，tube是 砖后面的凹点。

## What:

<img width="791" height="172" alt="image" src="https://github.com/user-attachments/assets/dc63e8bf-9349-474f-a63a-1a19261fba76" />

1.  训练一个 language model来生成 Lego 砖的建筑顺序。
2.  之前的工作是 离散，基于voxel的 tower，如上图，本文考虑了 更一般的 构件 + 5种连接方式，可以组成 成千上万的部件。
3.  收集了一个数据集 有超过 100k的 人工设计的 LDraw 砖和场景。

（注：LDraw 是一个专门给乐高的 免费 设计软件）

4\. 有一些挑战：（a）符合物理规律 ；（b）预测block位置简单，但是预测顺序很难；（c）重点在part和part之间的空间关系。

5\. 所以作者提出了一个 graph-based program representation，通过 connectivity 来参数化结构。 先根据connectivity建graph，然后再生成安装的顺序（autoregress的过程，不断生成下一步）。

<img width="1297" height="283" alt="image" src="https://github.com/user-attachments/assets/1d96f020-1ce9-4de5-a27f-402a9841d82b" />


## How：

1.  数据集 320,808 样本, 9743 部件。 一共累计 40M块砖。 所以每个建筑平均 126.4 块砖。每个部件之间的连接形式（5种）都标注了。
2.  借助 LDraw，有超过 24k个CAD复制，单位是LDU，1LDU 约等于 0.4mm。
3.  定义了5种连接方式。 比如：最后一种fixed，是正好扣住没有freedom的。标注的话，就是检查凸点（stud）的类型和旋转矩阵，基本就能推理出来。
4.  还做了 冲突（collision）检查，但是不好弄。（a）作者说，实际上拼lego，也是用力按上的 ，所以collision不太好评估；（b）因为lego建筑物不要求water-tight，作者说一些 VHACD 方法不好用（我猜是一些整体的 convex检测？看有没有缝隙的）。 最终，作者是设计了一个pipline ， render the part library watertight 等等做了一个过滤，但没细说。
5.  graph，部件作为node，连接作为edge 。从任意起点，可以采样一个建筑顺序，和怎么连接的方式+ 6DoF。如下图。

<img width="1040" height="591" alt="image" src="https://github.com/user-attachments/assets/3f61509a-6f71-45f0-a802-e9fb1fbe5ec6" />

6. 数据集划了有overlap的 两个训练集和，BrickNet-PT（pretrain）和 BrickNet-SFT （fiinetuning）。

BrickNet-SFT小一些 ， 67k样本 。质量比较高，是没有collisition的。 用Gemini2.5 标注了caption。其中，留了 512个 样本作为evalation。

BrickNet-PT 就是混合了SFT和 剩下所有的样本。

---

其实截止目前 （Section4结束） 都没怎么说方法，都在说 数据 / 数据结构 / 标注。

## 实验：

### 1\. Unconditional Generation

给个\[Start\]这种开始的token，让模型 autoregress一个 物理上合理的，没有穿模的 结构。

（1）作者用了 Brick-PT，然后每个序列采样了序列。每个序列最多有100个pieces。 finetune了不同大小的 Qwen3 instruct 模型 ，序列长度限制在4096个token。

loss用的是最基础的 下一步的 cross-entropy loss。

（2）**但是**，作者发现 这些模型 如果tempature 不限制，测试的时候 ， 生成 的长序列（2的16次方token）不太行。因为 即使 你有0.1%的 错误， 那你能生成完整4096个token序列的概率是 小于1.7%

所以作者说还是要按 a top-k of 20 and top-p of 0.95来采样。（简单说，要高置信度，限制一下多样性。）

（3）作者主要对比的是不同大小的 Qwen 模型，在生成长序列时候，连接有效性 和 避免冲突。 平均的 成功step 直到failure。 AS就是全温度采样，NS就是限制top采样。可以看到， 其实不同大小模型差距不大。 也就多走2-3步。 表里 pose是 naive 直接预测的，graph是本文的数据结构方法。

<img width="857" height="655" alt="image" src="https://github.com/user-attachments/assets/09b52c1c-62b9-46d0-883e-4b4fa3d428e7" />


### 2\. Text-conditioned Generation

这就用到了 小的 BrickNet-SFT 数据划分，带文本的。

finetune了一下前一 步 我们pretrain模型。 在 512 个 hold-out的样本上册。

用的是 文本到图像的一些指标。 其实模型大小差别也不大，比BrickGPT效果好。

<img width="683" height="438" alt="image" src="https://github.com/user-attachments/assets/96e925b0-21eb-4c56-8a92-d2c40b4b9abb" />


作者还测了Perplexity （这边作者没说怎么算的， 其实就是auto-regress模型 在预测 一个序列的时候 概率乘积）。直观理解的话 ，也是类似 反向的confidence。**Perplexity（困惑度）越低 = 模型越有 Confidence（自信）。像conditional generation肯定低。**

<img width="555" height="490" alt="image" src="https://github.com/user-attachments/assets/ff3fbfd1-3218-4d79-8215-7c6d089bfbd4" />


可视化效果还是比较好的（上面是sft的模型 下面是 之前BrickGPT）。 但也可能是 训练数据集里有类似的？还是需要真的跑一下他们的数据集验证一下 。

<img width="1361" height="877" alt="image" src="https://github.com/user-attachments/assets/dec33ee4-57d7-4e95-9fec-9fae3ecf4ce0" />


## 遗留问题：

1.  我看这个 sequence 里也没有6DoF。还是没有这个问题，其实他就 插上 也不管坐标系了。但是插哪一个孔 （比如我就插一半的孔，像拱桥一样）好像也没给出来。

2\. 这个graph 在大模型训练 / 测试的时候没有用到，就在preprare数据的时候用到了？？

---
本文首发于郑哲东个人主页：
https://www.zdzheng.xyz/blog/bricknet-graph-backed-generative-brick-assembly

转载请注明出处。
