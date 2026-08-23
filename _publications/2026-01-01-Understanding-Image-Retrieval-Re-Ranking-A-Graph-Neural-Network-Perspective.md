---
title: "Understanding Image Retrieval Re-Ranking: A Graph Neural Network Perspective"
collection: publications
permalink: /publication/Understa2026
date: 2026-01-01
doi: 10.1145/3803010
oral: 
keywords:  understanding image retrieval, image retrieval ranking, image retrieval, object re-identification, content-based retrieval
funding: 2025A1515012281, 202401035, FDCT/0043/2025/RIA1, University of Macau Advanced Research Institute in Hengqin
venue: 'ACM Transactions on Multimedia Computing, Communications, and Applications (TOMM)'
paperurl: 'https://zdzheng.xyz/files/2026/TOMM_GNN_Reranking.pdf'
blog: 'https://zhuanlan.zhihu.com/p/338777060'
code: 'https://github.com/Xuanmeng-Zhang/gnn-re-ranking'
author: '<a href="https://zdzheng.xyz/authors/Xuanmeng-Zhang" class="author"> <img src= "https://zdzheng.xyz/coauthors/xuanmeng-zhang.jpg" alt="xuanmeng-zhang" style="border-radius: 50%; height:20px; width:20px">Xuanmeng Zhang</a>, <a href="https://zdzheng.xyz/authors/Minyue-Jiang" class="author">Minyue Jiang</a>, <strong><a href="https://zdzheng.xyz/authors/Zhedong-Zheng" class="author">Zhedong Zheng</a></strong>, <a href="https://zdzheng.xyz/authors/Xiao-Tan" class="author">Xiao Tan</a>, <a href="https://zdzheng.xyz/authors/Errui-Ding" class="author"> <img src= "https://zdzheng.xyz/coauthors/errui-ding.jpeg" alt="errui-ding" style="border-radius: 50%; height:20px; width:20px">Errui Ding</a>, <a href="https://zdzheng.xyz/authors/Yi-Yang" class="author"> <img src= "https://zdzheng.xyz/coauthors/yi-yang.jpeg" alt="yi-yang" style="border-radius: 50%; height:20px; width:20px">Yi Yang</a>'
sqlauthor: '{"@type": "Person","name": "Xuanmeng Zhang"}, {"@type": "Person","name": "Minyue Jiang"}, {"@type": "Person","name": "Zhedong Zheng"}, {"@type": "Person","name": "Xiao Tan"}, {"@type": "Person","name": "Errui Ding"}, {"@type": "Person","name": "Yi Yang"}'
citation: ' Xuanmeng Zhang,  Minyue Jiang,  Zhedong Zheng,  Xiao Tan,  Errui Ding,  Yi Yang, &quot;Understanding Image Retrieval Re-Ranking: A Graph Neural Network Perspective.&quot; ACM TOMM, 2026. DOI: 10.1145/3803010'
pub_year: '2026'
bib: >
    @article{zhang2020understanding,<br>author = "Zhang, Xuanmeng and Jiang, Minyue and Zheng, Zhedong and Tan, Xiao and Ding, Errui and Yang, Yi",<br>title = "Understanding Image Retrieval Re-Ranking: A Graph Neural Network Perspective",<br>abstract = "The re-ranking approach leverages high-confidence retrieved samples to refine retrieval results, which have been widely adopted as a post-processing tool for image retrieval tasks. However, we notice one main flaw of re-ranking, i.e., high computational complexity, which leads to an unaffordable time cost for real-world applications. In this paper, we revisit re-ranking and demonstrate that re-ranking can be reformulated as a high-parallelism Graph Neural Network (GNN) function. In particular, we divide the conventional re-ranking process into two phases, i.e., retrieving high-quality gallery samples and updating features. We argue that the first phase equals building the k-nearest neighbor graph, while the second phase can be viewed as spreading the message within the graph. In practice, GNN only needs to concern vertices with the connected edges. Since the graph is sparse, we can efficiently update the vertex features. On the Market-1501 dataset, we accelerate the re-ranking processing from 89.2s to 9.4ms with one K40m GPU, facilitating the real-time post-processing. Similarly, we observe that our method achieves comparable or even better retrieval results on the other four image retrieval benchmarks, i.e., VeRi-776, Oxford-5k, Paris-6k and University-1652, with limited time cost. Our code is publicly available.",<br>journal = "ACM TOMM",<br>url = "https://zdzheng.xyz/files/2026/TOMM\_GNN\_Reranking.pdf",<br>code = "https://github.com/Xuanmeng-Zhang/gnn-re-ranking",<br>blog = "https://zhuanlan.zhihu.com/p/338777060",<br>funding = "2025A1515012281, 202401035, FDCT/0043/2025/RIA1, University of Macau Advanced Research Institute in Hengqin",<br>doi = "10.1145/3803010",<br>year = "2026"
    }

---