---
title: "Video2BEV: Transforming Drone Videos to BEVs for Video-based Geo-localization"
collection: publications
permalink: /publication/Video2BE2025
date: 2025-01-01
doi: 
oral: 
keywords:  video2bev transforming drone, transforming drone videos, drone videos bevs, visual geo-localization, spatial intelligence
funding: 2025A1515012281, 202401035, MYRG-GRG2024-00077-FST-UMDF
venue: 'IEEE/CVF International Conference on Computer Vision (ICCV)'
paperurl: 'https://zdzheng.xyz/files/2025/Juhao_Video2BEV.pdf'
blog: 'https://mp.weixin.qq.com/s/JttE911pNsUHzdkL3B3l5g'
code: 'https://github.com/HaoDot/Video2BEV-Open'
author: '<a href="https://zdzheng.xyz/authors/Hao-Ju" class="author">Hao Ju</a>, <a href="https://zdzheng.xyz/authors/Shaofei-Huang" class="author"> <img src= "https://zdzheng.xyz/coauthors/shaofei-huang.jpg" alt="shaofei-huang" style="border-radius: 50%; height:20px; width:20px">Shaofei Huang</a>, <a href="https://zdzheng.xyz/authors/Si-Liu" class="author"> <img src= "https://zdzheng.xyz/coauthors/si-liu.jpeg" alt="si-liu" style="border-radius: 50%; height:20px; width:20px">Si Liu</a>, <strong><a href="https://zdzheng.xyz/authors/Zhedong-Zheng" class="author">Zhedong Zheng</a></strong>'
sqlauthor: '{"@type": "Person","name": "Hao Ju"}, {"@type": "Person","name": "Shaofei Huang"}, {"@type": "Person","name": "Si Liu"}, {"@type": "Person","name": "Zhedong Zheng"}'
citation: ' Hao Ju,  Shaofei Huang,  Si Liu,  Zhedong Zheng, &quot;Video2BEV: Transforming Drone Videos to BEVs for Video-based Geo-localization.&quot; ICCV, 2025.'
pub_year: '2025'
bib: >
    @inproceedings{ju2024video2bev,<br>author = "Ju, Hao and Huang, Shaofei and Liu, Si and Zheng, Zhedong",<br>title = "Video2BEV: Transforming Drone Videos to BEVs for Video-based Geo-localization",<br>abstract = "Existing approaches to drone visual geo-localization predominantly adopt the image-based setting, where a single drone-view snapshot is matched with images from other platforms. Such task formulation, however, underutilizes the inherent video output of the drone and is sensitive to occlusions and environmental constraints. To address these limitations, we formulate a new video-based drone geo-localization task and propose the Video2BEV paradigm. This paradigm transforms the video into a Bird's Eye View (BEV), simplifying the subsequent matching process. In particular, we employ Gaussian Splatting to reconstruct a 3D scene and obtain the BEV projection. Different from the existing transform methods, e.g., polar transform, our BEVs preserve more fine-grained details without significant distortion. To further improve model scalability toward diverse BEVs and satellite figures, our Video2BEV paradigm also incorporates a diffusion-based module for generating hard negative samples, which facilitates discriminative feature learning. To validate our approach, we introduce UniV, a new video-based geo-localization dataset that extends the image-based University-1652 dataset. UniV features flight paths at 30 and 45 elevation angles with increased frame rates of up to 10 frames per second (FPS). Extensive experiments on the UniV dataset show that our Video2BEV paradigm achieves competitive recall rates and outperforms conventional video-based methods. Compared to other methods, our proposed approach exhibits robustness at lower elevations with more occlusions.",<br>booktitle = "ICCV",<br>url = "https://zdzheng.xyz/files/2025/Juhao\_Video2BEV.pdf",<br>code = "https://github.com/HaoDot/Video2BEV-Open",<br>blog = "https://mp.weixin.qq.com/s/JttE911pNsUHzdkL3B3l5g",<br>funding = "2025A1515012281, 202401035, MYRG-GRG2024-00077-FST-UMDF",<br>year = "2025"
    }

---