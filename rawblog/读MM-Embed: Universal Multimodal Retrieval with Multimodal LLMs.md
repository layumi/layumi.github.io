# MM-Embed: Universal Multimodal Retrieval with Multimodal LLMs 

发表于ICLR2025

论文链接：https://arxiv.org/abs/2411.02571

代码 https://huggingface.co/nvidia/MM-Embed 


## What 
1. 本文研究通过大模型 来实现多模态检索。
2. 首先 在10个数据集16种任务上，finetune了一个 MLLM。 作者发现MLLM处理 challenging queris（比如query包含图文两种模态的）比较好 ，但是一般的cross-modality 任务 比不过 小的clip模型。
3. 作者说这是引文 modality bias。 （我理解是 大模型对文本生成和reasoning考虑太多。）
4. 为了解决这个问题，作者提出 一个 modality-aware的 hard negative mining
5. 其次，作者提出了 **continuously** fine-tuning the universal multimodal retriever （好像没什么差别。）在 M-BEIR 和 MTEB等检索benchmark上达到了 sota。
6. 最后，作者尝试了通过prompt 作为zero-shot reranker，可以进一步提升，特别是 图文组合query。 


## How
<img width="2470" height="1396" alt="image" src="https://github.com/user-attachments/assets/385a8ca2-efaa-4945-b67d-ac45edbb7f5a" />

1. 如上图，作者有多种训练的 instruction，（1）图搜文   （2）图搜图 （3）图+文 搜图 （4）还是图搜文 （5,6）VQA （7）文搜图
通过finetune 基础的MLLM （LLaVa-Next） 得到 MM-Embed。需要注意这一步是没有文搜文。

2. 如上图下方，给出 top-3 candidates， 做一个 binary的预测， Prompt用的是 “Does the answer correctly answer the question, True or False”. 给出概率进行rerank。

3. 方法上，主要的loss（公式1） 类似infoNCE loss， 拉近 （query+instruction， 对应的candidate）。

4. negative sampling 貌似和传统的方法差不多，就是infoNCE 外接了一个batch的hard negatives。

5. 这边4.1.2的开头M^hard出现比较突然，没有定义。M^rand 定义了，是一开始infoNCE fine-tuned model 没有hard negative的。所以我猜M^hard是hard negative训练完的。

6. 关于 continuous，作者又回去 训练文到文（QA之类的）了，这边negative是通过NV-Embed-v1来mine。然后negative也有用M^hard 来选择的。 

7. 最后 reranking 其实就是 回答 binary True or False。按照Ture和False token的logits 做了Softmax。


# 实验
1. 作者训练的数据集还是比较多的 。
- M-BEIR 混合了我们常见的 MSCOCO （图文互搜），FashionIQ（图+文搜图），Fashion200k（图+文搜图），Visual News，WebQA（文搜文），OVEN，CIRR（图+文搜图），NIGHTS，InfoSeek，EDIS。 其中 1.1M训练queries ， 190K测试queries， 5.6M gallery 。

<img width="2236" height="1200" alt="image" src="https://github.com/user-attachments/assets/3fbf51b9-066b-4a41-9a60-425f3e351255" />

2. 我们 2025年TMM论文 https://www.zdzheng.xyz/files/2025/TMM25-Scale.pdf 用的是BLIP2 作为backbone。 FashionIQ 平均R10是 54.99； CIRR的 recall@5 是 84.92%，recall@10是91.74% 。

3. 作者这边 FashionIQ是25.7 recall@10， CIRR是50.00% recall@5 。 那确实 不如blip2.

4. 然后 MSCOCO 这个结果我也比较熟悉。 感觉也没到SOTA？

<img width="1426" height="626" alt="image" src="https://github.com/user-attachments/assets/96744ba5-172f-4b9a-aea2-3b01e18a4770" />

5. 如上图，作者还给了一个ablation study，关于图文互搜，在hard negatives 以后 M^hard 效果就好了。


