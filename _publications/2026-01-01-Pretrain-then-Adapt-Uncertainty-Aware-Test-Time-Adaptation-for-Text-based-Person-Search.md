---
title: "Pretrain-then-Adapt: Uncertainty-Aware Test-Time Adaptation for Text-based Person Search"
collection: publications
permalink: /publication/Pretrain2026
date: 2026-01-01
last_modified_at: 2026-08-23
doi: 3805712.3809598
oral: 
keywords:  based person search, person search, text based person, person re-id, person retrieval, person search, domain adaptation, uncertainty learning
funding: 2025A1515012281, SBZ20250900116, MYRG-GRG2024-00077-FST-UMDF, FDCT/0043/2025/RIA1
venue: 'ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR)'
paperurl: 'https://zdzheng.xyz/files/2026/SIGIR_Jiahao.pdf'
blog: 'https://zhuanlan.zhihu.com/p/2034741247034778727'
code: 'https://github.com/nkuzjh/UATTA'
author: '<a href="https://zdzheng.xyz/authors/Jiahao-Zhang" class="author">Jiahao Zhang</a>, <a href="https://zdzheng.xyz/authors/Shaofei-Huang" class="author"> <img src= "https://zdzheng.xyz/coauthors/shaofei-huang.jpg" alt="shaofei-huang" style="border-radius: 50%; height:20px; width:20px">Shaofei Huang</a>, <a href="https://zdzheng.xyz/authors/Yaxiong-Wang" class="author"> <img src= "https://zdzheng.xyz/coauthors/yaxiong-wang.jpeg" alt="yaxiong-wang" style="border-radius: 50%; height:20px; width:20px">Yaxiong Wang</a>, <strong><a href="https://zdzheng.xyz/authors/Zhedong-Zheng" class="author">Zhedong Zheng</a></strong>'
sqlauthor: '{"@type": "Person","name": "Jiahao Zhang"}, {"@type": "Person","name": "Shaofei Huang"}, {"@type": "Person","name": "Yaxiong Wang"}, {"@type": "Person","name": "Zhedong Zheng"}'
citation: ' Jiahao Zhang,  Shaofei Huang,  Yaxiong Wang,  Zhedong Zheng, &quot;Pretrain-then-Adapt: Uncertainty-Aware Test-Time Adaptation for Text-based Person Search.&quot; SIGIR, 2026. DOI: 3805712.3809598'
pub_year: '2026'
bib: >
    @inproceedings{zhang2026pretrain,<br>author = "Zhang, Jiahao and Huang, Shaofei and Wang, Yaxiong and Zheng, Zhedong",<br>title = "Pretrain-then-Adapt: Uncertainty-Aware Test-Time Adaptation for Text-based Person Search",<br>abstract = "Text-based person search faces inherent limitations due to data scarcity, driven by stringent privacy constraints and the high cost of manual annotation. To mitigate this, existing methods usually rely on a Pretrain-then-Finetune paradigm, where models are first pretrained on synthetic person-caption data to establish cross-modal alignment, followed by fine-tuning on labeled real-world datasets. However, this paradigm lacks practicality in real-world deployment scenarios, where large-scale annotated target-domain data is typically inaccessible. In this work, we propose a new Pretrain-then-Adapt paradigm that eliminates reliance on extensive target-domain supervision through an offline test-time adaptation manner, enabling dynamic model adaptation using only unlabeled test data with minimal post-train time cost. To mitigate overconfidence with false positives of previous entropy-based test-time adaptation, we propose an Uncertainty-Aware Test-Time Adaptation (UATTA) framework, which introduces a bidirectional retrieval disagreement mechanism to estimate uncertainty, i.e., low uncertainty is assigned when an image-text pair ranks highly in both image-to-text and text-to-image retrieval, indicating high alignment; otherwise, high uncertainty is detected. This indicator drives offline test-time model recalibration without labels, effectively mitigating domain shift. We validate UATTA on four benchmarks, i.e., CUHK-PEDES, ICFG-PEDES, RSTPReid, and PAB, showing consistent improvements across both CLIP-based (one-stage) and XVLM-based (two-stage) frameworks. Ablation studies confirm that UATTA outperforms existing offline test-time adaptation strategies, establishing a new benchmark for label-efficient, deployable person search systems. Our code is available at https://github.com/nkuzjh/UATTA.",<br>booktitle = "SIGIR",<br>url = "https://zdzheng.xyz/files/2026/SIGIR\_Jiahao.pdf",<br>blog = "https://zhuanlan.zhihu.com/p/2034741247034778727",<br>code = "https://github.com/nkuzjh/UATTA",<br>funding = "2025A1515012281, SBZ20250900116, MYRG-GRG2024-00077-FST-UMDF, FDCT/0043/2025/RIA1",<br>doi = "3805712.3809598",<br>year = "2026"
    }

---