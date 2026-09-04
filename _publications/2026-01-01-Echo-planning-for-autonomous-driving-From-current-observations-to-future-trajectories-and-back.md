---
title: "Echo planning for autonomous driving: From current observations to future trajectories and back"
collection: publications
permalink: /publication/Echo-pla2026
date: 2026-01-01
last_modified_at: 2026-08-24
doi: 10.1109/TMM.2026.3713776
oral: 
keywords:  echo planning autonomous, echo planning, planning autonomous driving
funding: FDCT/0043/2025/RIA1, 2025A1515012281, BZ2025029
venue: 'IEEE Transactions on Multimedia (TMM)'
paperurl: 'https://zdzheng.xyz/files/2026/TMM_jintao_planning.pdf'
author: '<a href="https://zdzheng.xyz/authors/Jintao-Sun" class="author">Jintao Sun</a>, <a href="https://zdzheng.xyz/authors/Hu-Zhang" class="author"> <img src= "https://zdzheng.xyz/coauthors/hu-zhang.jpg" alt="hu-zhang" style="border-radius: 50%; height:20px; width:20px">Hu Zhang</a>, <a href="https://zdzheng.xyz/authors/Gangyi-Ding" class="author">Gangyi Ding</a>, <strong><a href="https://zdzheng.xyz/authors/Zhedong-Zheng" class="author">Zhedong Zheng</a></strong>'
sqlauthor: '{"@type": "Person","name": "Jintao Sun"}, {"@type": "Person","name": "Hu Zhang"}, {"@type": "Person","name": "Gangyi Ding"}, {"@type": "Person","name": "Zhedong Zheng"}'
citation: ' Jintao Sun,  Hu Zhang,  Gangyi Ding,  Zhedong Zheng, &quot;Echo planning for autonomous driving: From current observations to future trajectories and back.&quot; TMM, 2026. DOI: 10.1109/TMM.2026.3713776'
pub_year: '2026'
bib: >
    @article{sun2026echo,<br>author = "Sun, Jintao and Zhang, Hu and Ding, Gangyi and Zheng, Zhedong",<br>title = "Echo planning for autonomous driving: From current observations to future trajectories and back",<br>abstract = "Modern end-to-end autonomous driving systems suffer from a critical limitation: their planners lack mechanisms to enforce temporal consistency between predicted trajectories and evolving scene dynamics. This absence of self-supervision allows early prediction errors to compound catastrophically over time. We introduce Echo Planning (EchoP), a new self-correcting framework that establishes an end-to-end Current - Future - Current (CFC) cycle to harmonize trajectory prediction with scene coherence. Our key insight is that plausible future trajectories should be bi-directionally consistent, i.e., not only generated from current observations but also capable of reconstructing them. The CFC mechanism first predicts future trajectories from the Bird's-Eye-View (BEV) scene representation, then inversely maps these trajectories back to estimate the current BEV state. By enforcing consistency between the original and reconstructed BEV representations through a cycle loss, the framework intrinsically penalizes physically implausible or misaligned trajectories. Experiments on nuScenes show that the proposed method yields competitive performance, reducing L2 error (Avg) by -0.04 m and collision rate by -0.12\\% compared to one-shot planners. Moreover, EchoP seamlessly extends to closed-loop evaluation, i.e., Bench2Drive, attaining a 26.54\\% success rate. Notably, EchoP requires no additional supervision: the CFC cycle acts as an inductive bias that stabilizes long-horizon planning. Overall, EchoP offers a simple, deployable pathway to improve reliability in safety-critical autonomous driving.",<br>url = "https://zdzheng.xyz/files/2026/TMM\_jintao\_planning.pdf",<br>doi = "10.1109/TMM.2026.3713776",<br>funding = "FDCT/0043/2025/RIA1, 2025A1515012281, BZ2025029",<br>journal = "TMM",<br>year = "2026"
    }

---