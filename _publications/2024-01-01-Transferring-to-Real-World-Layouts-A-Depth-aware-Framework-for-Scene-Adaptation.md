---
title: "Transferring to Real-World Layouts: A Depth-aware Framework for Scene Adaptation"
collection: publications
permalink: /publication/Transfer2024
excerpt: 'Oral Presentation'
date: 2024-01-01
doi: 
oral: Oral Presentation
keywords:  framework scene adaptation, depth aware framework, scene adaptation, domain adaptation
funding: SRG2024-00002-FST
venue: 'ACM International Conference on Multimedia (ACM MM)'
paperurl: 'https://zdzheng.xyz/files/2024/ACMMM24-Layout.pdf'
code: 'https://github.com/chen742/DCF'
author: '<a href="https://zdzheng.xyz/authors/Mu-Chen" class="author"> <img src= "https://zdzheng.xyz/coauthors/mu-chen.jpeg" alt="mu-chen" style="border-radius: 50%; height:20px; width:20px">Mu Chen</a>, <strong><a href="https://zdzheng.xyz/authors/Zhedong-Zheng" class="author">Zhedong Zheng</a></strong>, <a href="https://zdzheng.xyz/authors/Yi-Yang" class="author"> <img src= "https://zdzheng.xyz/coauthors/yi-yang.jpeg" alt="yi-yang" style="border-radius: 50%; height:20px; width:20px">Yi Yang</a>'
sqlauthor: '{"@type": "Person","name": "Mu Chen"}, {"@type": "Person","name": "Zhedong Zheng"}, {"@type": "Person","name": "Yi Yang"}'
citation: ' Mu Chen,  Zhedong Zheng,  Yi Yang, &quot;Transferring to Real-World Layouts: A Depth-aware Framework for Scene Adaptation.&quot; ACM Multimedia, 2024.'
abs: 'Scene segmentation via unsupervised domain adaptation (UDA) enables the transfer of knowledge acquired from source synthetic data to real-world target data, which largely reduces the need for manual pixel-level annotations in the target domain. To facilitate domain-invariant feature learning, existing methods typically mix data from both the source domain and target domain by simply copying and pasting pixels. Such vanilla methods are usually sub-optimal since they do not take into account how well the mixed layouts correspond to real-world scenarios. Real-world scenarios are with an inherent layout. The model suffers from confusion in predicting the target domain due to the unrealistic mixing. For instance, it is not reasonable to directly paste the near pedestrian pixels into the remote sky area. Based on such observation, we propose a depth-aware framework to explicitly leverage depth estimation to mix categories and facilitate two complementary tasks, i.e., segmentation and depth learning in an end-to-end manner. Besides, several public datasets do not provide depth annotation. Therefore, we leverage the off-the-shelf depth estimation network to obtain the pseudo depth. Extensive experiments show that our methods, even with pseudo depth, achieve competitive performance, i.e., 77.7 mIoU on GTA to Cityscapes and 69.3 mIoU on Synthia to Cityscapes.'
last_modified_at: 2026-09-04
pub_year: '2024'
bib: >
    @inproceedings{chen2024transferring,<br>author = "Chen, Mu and Zheng, Zhedong and Yang, Yi",<br>title = "Transferring to Real-World Layouts: A Depth-aware Framework for Scene Adaptation",<br>abstract = "Scene segmentation via unsupervised domain adaptation (UDA) enables the transfer of knowledge acquired from source synthetic data to real-world target data, which largely reduces the need for manual pixel-level annotations in the target domain. To facilitate domain-invariant feature learning, existing methods typically mix data from both the source domain and target domain by simply copying and pasting pixels. Such vanilla methods are usually sub-optimal since they do not take into account how well the mixed layouts correspond to real-world scenarios. Real-world scenarios are with an inherent layout. The model suffers from confusion in predicting the target domain due to the unrealistic mixing. For instance, it is not reasonable to directly paste the near pedestrian pixels into the remote sky area. Based on such observation, we propose a depth-aware framework to explicitly leverage depth estimation to mix categories and facilitate two complementary tasks, i.e., segmentation and depth learning in an end-to-end manner. Besides, several public datasets do not provide depth annotation. Therefore, we leverage the off-the-shelf depth estimation network to obtain the pseudo depth. Extensive experiments show that our methods, even with pseudo depth, achieve competitive performance, i.e., 77.7 mIoU on GTA to Cityscapes and 69.3 mIoU on Synthia to Cityscapes.",<br>code = "https://github.com/chen742/DCF",<br>url = "https://zdzheng.xyz/files/2024/ACMMM24-Layout.pdf",<br>booktitle = "ACM Multimedia",<br>funding = "SRG2024-00002-FST",<br>note = "Oral Presentation",<br>year = "2024"
    }

---