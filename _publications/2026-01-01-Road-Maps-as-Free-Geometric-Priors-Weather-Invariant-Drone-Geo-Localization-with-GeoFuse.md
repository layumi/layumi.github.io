---
title: "Road Maps as Free Geometric Priors: Weather-Invariant Drone Geo-Localization with GeoFuse"
collection: publications
permalink: /publication/Road-Map2026
date: 2026-01-01
last_modified_at: 2026-08-24
doi: 
oral: 
keywords:  drone geo localization, geometric priors weather, invariant drone geo, visual geo-localization, spatial intelligence
funding: 
venue: 'arXiv:2605.14925'
paperurl: 'https://zdzheng.xyz/files/2026/Roadmap_Yunsong.pdf'
code: 'https://github.com/YsongF/GeoFuse'
author: '<a href="https://zdzheng.xyz/authors/Yunsong-Fang" class="author">Yunsong Fang</a>, <a href="https://zdzheng.xyz/authors/Tingyu-Wang" class="author"> <img src= "https://zdzheng.xyz/coauthors/tingyu-wang.jpeg" alt="tingyu-wang" style="border-radius: 50%; height:20px; width:20px">Tingyu Wang</a>, <strong><a href="https://zdzheng.xyz/authors/Zhedong-Zheng" class="author">Zhedong Zheng</a></strong>'
sqlauthor: '{"@type": "Person","name": "Yunsong Fang"}, {"@type": "Person","name": "Tingyu Wang"}, {"@type": "Person","name": "Zhedong Zheng"}'
citation: ' Yunsong Fang,  Tingyu Wang,  Zhedong Zheng, &quot;Road Maps as Free Geometric Priors: Weather-Invariant Drone Geo-Localization with GeoFuse.&quot; arXiv:2605.14925, 2026.'
pub_year: '2026'
bib: >
    @article{fang2026road,<br>author = "Fang, Yunsong and Wang, Tingyu and Zheng, Zhedong",<br>title = "Road Maps as Free Geometric Priors: Weather-Invariant Drone Geo-Localization with GeoFuse",<br>abstract = "Drone-view geo-localization aims to match a query drone image, often captured under adverse weather conditions (e.g., rain, snow, fog), against a gallery of geo-tagged satellite images. Weather-induced degradations in the drone view, such as noise, reduced visibility, and partial occlusions, severely exacerbate the intrinsic cross-view domain gap. While prior methods predominantly rely on weather-specific architectures or data augmentations, they have largely overlooked road map data, a readily available modality that provides strong, inherently weather-invariant geometric layout cues (e.g., road networks and building footprints) at negligible additional cost. We introduce GeoFuse, a cross-modal fusion framework that integrates precisely aligned road map tiles with satellite imagery to yield more discriminative and weather-resilient representations. We first augment the existing University-1652 and DenseUAV benchmarks with geo-aligned road maps, supplying structural priors robust to meteorological variations. Building on this, we propose a flexible fusion module that combines satellite and road map features via token-level and channel-level interactions, with a lightweight dynamic gating mechanism that adaptively weights modality contributions per instance. Finally, we employ class-level cross-view contrastive learning to promote robust alignment between weather-degraded drone features and the fused satellite-roadmap representations. Extensive experiments under diverse weather conditions show that GeoFuse consistently outperforms state-of-the-art methods, achieving +3.46\\% and +23.18\\% Recall@1 accuracy on the University-1652 and DenseUAV benchmarks, respectively.",<br>journal = "arXiv:2605.14925",<br>url = "https://zdzheng.xyz/files/2026/Roadmap\_Yunsong.pdf",<br>code = "https://github.com/YsongF/GeoFuse",<br>year = "2026"
    }

---