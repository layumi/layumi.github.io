---
title: "Self-Ensembling Depth Completion via Density-aware Consistency"
collection: publications
permalink: /publication/Self-Ens2024
date: 2024-01-01
last_modified_at: 2026-08-24
doi: 10.1016/j.patcog.2024.110618
oral: 
keywords:  ensembling depth completion, self ensembling depth, completion density aware
funding: 
venue: 'Pattern Recognition (PR)'
paperurl: 'https://zdzheng.xyz/files/2024/PR_SEED.pdf'
author: '<a href="https://zdzheng.xyz/authors/Xuanmeng-Zhang" class="author"> <img src= "https://zdzheng.xyz/coauthors/xuanmeng-zhang.jpg" alt="xuanmeng-zhang" style="border-radius: 50%; height:20px; width:20px">Xuanmeng Zhang</a>, <strong><a href="https://zdzheng.xyz/authors/Zhedong-Zheng" class="author">Zhedong Zheng</a></strong>, <a href="https://zdzheng.xyz/authors/Minyue-Jiang" class="author">Minyue Jiang</a>, <a href="https://zdzheng.xyz/authors/Xiaoqing-Ye" class="author">Xiaoqing Ye</a>'
sqlauthor: '{"@type": "Person","name": "Xuanmeng Zhang"}, {"@type": "Person","name": "Zhedong Zheng"}, {"@type": "Person","name": "Minyue Jiang"}, {"@type": "Person","name": "Xiaoqing Ye"}'
citation: ' Xuanmeng Zhang,  Zhedong Zheng,  Minyue Jiang,  Xiaoqing Ye, &quot;Self-Ensembling Depth Completion via Density-aware Consistency.&quot; Pattern Recognition, 2024. DOI: 10.1016/j.patcog.2024.110618'
pub_year: '2024'
bib: >
    @article{zhang2024seed,<br>author = "Zhang, Xuanmeng and Zheng, Zhedong and Jiang, Minyue and Ye, Xiaoqing",<br>title = "Self-Ensembling Depth Completion via Density-aware Consistency",<br>abstract = "Depth completion can predict a dense depth map by taking a sparse depth map and the aligned RGB image as input, but the acquisition of ground truth annotations is labor-intensive and non-scalable. Therefore, we resort to semi-supervised learn- ing, where we only need to annotate a few images and leverage massive unlabeled data without ground truth labels to facilitate model learning. In this paper, we propose SEED, a SElf-Ensembling Depth completion framework to enhance the generalization of the model on unlabeled data. Specifically, SEED contains a pair of the teacher and student models, which are given high-density and low-density sparse depth maps as input respectively. The main idea underpinning SEED is to enforce the density-aware consistency by encouraging consistent prediction across different-density input depth maps. One empirical challenge is that the pseudo- depth labels produced by the teacher model inevitably contain wrong depth values, which would mislead the convergence of the student model. To resist the noisy labels, we propose an automatic method to measure the reliability of the gener- ∗Zhedong Zheng is the corresponding author. (Email address: zhedongzheng@um.edu.mo) Preprint submitted to Pattern Recognition May 31, 2024 ated pseudo-depth labels adaptively. By leveraging the discrepancy of prediction distributions, we model the pixel-wise uncertainty map as the prediction variance and rectify the training process from noisy labels explicitly. To our knowledge, we are among the early semi-supervised attempts on the depth completion task. Ex- tensive experiments on both outdoor and indoor datasets demonstrate that SEED consistently improves the performance of the baseline model by a large margin and even is on par with several fully-supervised methods.",<br>journal = "Pattern Recognition",<br>url = "https://zdzheng.xyz/files/2024/PR\_SEED.pdf",<br>doi = "10.1016/j.patcog.2024.110618",<br>year = "2024"
    }

---