---
title: "Approaching Outside: Scaling Unsupervised 3D Object Detection from 2D Scene"
collection: publications
permalink: /publication/Approach2024
date: 2024-01-01
doi: 
oral: 
keywords:  scaling unsupervised 3d, unsupervised 3d object, 3d object detection
funding: SRG2024-00002-FST
venue: 'European conference on computer vision (ECCV)'
paperurl: 'https://zdzheng.xyz/files/2024/ECCV24-Approach.pdf'
blog: 'https://www.zhihu.com/question/660698707/answer/3575967153'
code: 'https://github.com/Ruiyang-061X/LiSe'
author: '<a href="https://zdzheng.xyz/authors/Ruiyang-Zhang" class="author">Ruiyang Zhang</a>, <a href="https://zdzheng.xyz/authors/Hu-Zhang" class="author"> <img src= "https://zdzheng.xyz/coauthors/hu-zhang.jpg" alt="hu-zhang" style="border-radius: 50%; height:20px; width:20px">Hu Zhang</a>, <a href="https://zdzheng.xyz/authors/Hang-Yu" class="author"> <img src= "https://zdzheng.xyz/coauthors/hang-yu.jpg" alt="hang-yu" style="border-radius: 50%; height:20px; width:20px">Hang Yu</a>, <strong><a href="https://zdzheng.xyz/authors/Zhedong-Zheng" class="author">Zhedong Zheng</a></strong>'
sqlauthor: '{"@type": "Person","name": "Ruiyang Zhang"}, {"@type": "Person","name": "Hu Zhang"}, {"@type": "Person","name": "Hang Yu"}, {"@type": "Person","name": "Zhedong Zheng"}'
citation: ' Ruiyang Zhang,  Hu Zhang,  Hang Yu,  Zhedong Zheng, &quot;Approaching Outside: Scaling Unsupervised 3D Object Detection from 2D Scene.&quot; European conference on computer vision (ECCV), 2024.'
pub_year: '2024'
bib: >
    @inproceedings{LiSe,<br>author = "Zhang, Ruiyang and Zhang, Hu and Yu, Hang and Zheng, Zhedong",<br>title = "Approaching Outside: Scaling Unsupervised 3D Object Detection from 2D Scene",<br>abstract = "The open-world 3D object detection is to accurately detect objects in unstructured environments with no explicit supervisory signals. This task, given sparse LiDAR point clouds, often results in compromised performance for detecting small or distant objects due to the inherent sparsity and limited spatial resolution. In this paper, we are among the early attempts to integrate LiDAR data with 2D images for open-world 3D detection and introduce a new method, dubbed LiDAR-2D Self-paced Learning (LiSe). We argue that RGB images serve as a valuable complement to LiDAR data, offering precise 2D localization cues, particularly when scarce LiDAR points are available for certain objects. Considering the unique characteristics of both modalities, our framework devises a self-paced learning pipeline that incorporates adaptive sampling and weak model aggregation strategies. The adaptive sampling strategy dynamically tunes the distribution of pseudo labels during training, countering the tendency of models to overfit on easily detected samples, such as nearby and large-sized objects. By doing so, it ensures a balanced learning trajectory across varying object scales and distances. The weak model aggregation component consolidates the strengths of models trained under different pseudo label distributions, culminating in a robust and powerful final model. Experimental evaluations validate the efficacy of our proposed LiSe method, manifesting significant improvements of +7.1\\% AP-BEV and +3.4\\% AP-3D on nuScenes compared to existing techniques.",<br>booktitle = "European conference on computer vision (ECCV)",<br>code = "https://github.com/Ruiyang-061X/LiSe",<br>url = "https://zdzheng.xyz/files/2024/ECCV24-Approach.pdf",<br>blog = "https://www.zhihu.com/question/660698707/answer/3575967153",<br>funding = "SRG2024-00002-FST",<br>year = "2024"
    }

---