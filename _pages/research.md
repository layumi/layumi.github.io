---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
redirect_from: 
---

<style>
.pyramid-wrap {
  font-family: var(--font-sans);
  padding: 1.5rem 0.5rem 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0;
}
.tier {
  display: flex;
  justify-content: center;
  align-items: stretch;
  gap: 10px;
  width: 100%;
}
.connector-row {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 32px;
  position: relative;
  width: 100%;
}
.node {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  border-radius: var(--border-radius-lg);
  padding: 12px 14px;
  text-decoration: none;
  border: 1.5px solid;
  cursor: pointer;
  transition: filter 0.15s;
  line-height: 1.35;
}
.node:hover { filter: brightness(0.95); }
.node-title {
  font-size: 13px;
  font-weight: 500;
  display: block;
}
.node-sub {
  font-size: 11px;
  display: block;
  margin-top: 3px;
  opacity: 0.75;
}
.badge {
  font-size: 10px;
  font-weight: 500;
  padding: 2px 8px;
  border-radius: 20px;
  display: inline-block;
  margin-top: 5px;
}

/* Root */
.n-root {
  background: #E6F1FB;
  border-color: #185FA5;
  color: #0C447C;
  max-width: 240px;
  width: 100%;
  padding: 14px 20px;
}
.n-root .node-title { font-size: 15px; color: #042C53; }
.n-root .node-sub { color: #185FA5; }

/* Methods tier */
.n-aigc {
  background: #FAECE7;
  border-color: #993C1D;
  color: #712B13;
  flex: 1;
  max-width: 260px;
}
.n-aigc .node-title { color: #4A1B0C; }
.n-aigc .node-sub { color: #993C1D; }
.n-aigc .badge { background: #F5C4B3; color: #712B13; }

.n-unc {
  background: #EEEDFE;
  border-color: #534AB7;
  color: #3C3489;
  flex: 1;
  max-width: 260px;
}
.n-unc .node-title { color: #26215C; }
.n-unc .node-sub { color: #534AB7; }
.n-unc .badge { background: #CECBF6; color: #3C3489; }

/* Task tier */
.n-reid {
  background: #FAEEDA;
  border-color: #854F0B;
  color: #633806;
  flex: 1;
}
.n-reid .node-title { color: #412402; }
.n-reid .node-sub { color: #854F0B; }
.n-reid .badge { background: #FAC775; color: #633806; }

.n-da {
  background: #EAF3DE;
  border-color: #3B6D11;
  color: #27500A;
  flex: 1;
}
.n-da .node-title { color: #173404; }
.n-da .node-sub { color: #3B6D11; }
.n-da .badge { background: #C0DD97; color: #27500A; }

.n-sp {
  background: #E1F5EE;
  border-color: #0F6E56;
  color: #085041;
  flex: 1;
}
.n-sp .node-title { color: #04342C; }
.n-sp .node-sub { color: #0F6E56; }
.n-sp .badge { background: #9FE1CB; color: #085041; }

/* SVG connectors */
svg.conn { width: 100%; overflow: visible; display: block; }

/* more link */
.more-link {
  font-size: 12px;
  color: var(--color-text-secondary);
  text-align: center;
  margin-top: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 4px;
}
.more-link a {
  color: #185FA5;
  text-decoration: none;
  font-weight: 500;
}
.more-link a:hover { text-decoration: underline; }

/* Mobile: stack method nodes vertically if narrow */
@media (max-width: 480px) {
  .tier-methods { flex-direction: column; align-items: center; }
  .tier-methods .n-aigc,
  .tier-methods .n-unc { max-width: 100%; width: 100%; }
  .tier-tasks { flex-direction: column; align-items: center; }
  .tier-tasks .n-reid,
  .tier-tasks .n-da,
  .tier-tasks .n-sp { max-width: 100%; width: 100%; }
  svg.conn { display: none; }
  .connector-row { height: 8px; }
}
</style>

<div class="pyramid-wrap">

  <div class="tier" style="margin-bottom:0">
    <a class="node n-root" href="https://scholar.google.com/citations?view_op=search_authors&mauthors=label:data_centric_ai" target="_blank">
      <span class="node-title">Data-Centric AI</span>
      <span class="node-sub">Root framework</span>
    </a>
  </div>

  <div class="connector-row" style="max-width:520px;width:100%">
    <svg class="conn" height="32" viewBox="0 0 520 32" preserveAspectRatio="none">
      <line x1="260" y1="0" x2="100" y2="32" stroke="#185FA5" stroke-width="1.5" stroke-dasharray="4 3"/>
      <line x1="260" y1="0" x2="420" y2="32" stroke="#185FA5" stroke-width="1.5" stroke-dasharray="4 3"/>
    </svg>
  </div>

  <div class="tier tier-methods" style="gap:10px;max-width:540px;width:100%">
    <a class="node n-aigc" href="https://scholar.google.com/citations?view_op=search_authors&mauthors=label:aigc" target="_blank">
      <span class="node-title">AIGC</span>
      <span class="node-sub">Generative data synthesis</span>
      <span class="badge">Data scarcity</span>
    </a>
    <a class="node n-unc" href="https://scholar.google.com/citations?view_op=search_authors&mauthors=label:uncertainty_estimation" target="_blank">
      <span class="node-title">Uncertainty estimation</span>
      <span class="node-sub">Pseudo &amp; weak labels</span>
      <span class="badge">Label scarcity</span>
    </a>
  </div>

  <div class="connector-row" style="max-width:660px;width:100%">
    <svg class="conn" height="32" viewBox="0 0 660 32" preserveAspectRatio="none">
      <line x1="185" y1="0" x2="100"  y2="32" stroke="#993C1D" stroke-width="1.2" stroke-dasharray="3 3"/>
      <line x1="185" y1="0" x2="330"  y2="32" stroke="#185FA5" stroke-width="1.2" stroke-dasharray="3 3"/>
      <line x1="475" y1="0" x2="330"  y2="32" stroke="#185FA5" stroke-width="1.2" stroke-dasharray="3 3"/>
      <line x1="475" y1="0" x2="560"  y2="32" stroke="#534AB7" stroke-width="1.2" stroke-dasharray="3 3"/>
    </svg>
  </div>

  <div class="tier tier-tasks" style="gap:8px;width:100%">
    <a class="node n-reid" href="https://scholar.google.com/citations?view_op=search_authors&mauthors=label:object_re_identification" target="_blank">
      <span class="node-title">Object Re-identification</span>
      <span class="node-sub">Person, vehicle, 3D</span>
      <span class="badge">AIGC</span>
    </a>
    <a class="node n-da" href="https://scholar.google.com/citations?view_op=search_authors&mauthors=label:domain_adaptation" target="_blank">
      <span class="node-title">Domain adaptation</span>
      <span class="node-sub">Segmentation, Re-ID</span>
      <span class="badge">Uncertainty</span>
    </a>
    <a class="node n-sp" href="https://scholar.google.com/citations?view_op=search_authors&mauthors=label:spatial_intelligence" target="_blank">
      <span class="node-title">Spatial intelligence</span>
      <span class="node-sub">Geo-loc, 3DGS, UAV</span>
      <span class="badge">AIGC</span>
    </a>
  </div>

  <div class="more-link">
    <i class="ti ti-external-link" aria-hidden="true" style="font-size:13px"></i>
    <a href="https://www.zdzheng.xyz/research" target="_blank">See Research page for more details</a>
  </div>

</div>

## [AIGC](https://www.zdzheng.xyz/tag/aigc)
![](https://zdzheng.xyz/resource-img/rainbow_github.webp)
This research area is about generate diverse and high-fidelity data. Some methods focus on the generation quality, while others further focus on the recognition performance based on the generated data.
- 2D Human [ICCV'17](https://zdzheng.xyz/publication/Unlabele2017), [ECCV'18](https://zdzheng.xyz/publication/Macro-mi2018), [TIP'18](https://zdzheng.xyz/publication/Multi-ps2018), [CVPR'19](https://www.zdzheng.xyz/publication/Joint-di2019), [TMM'22](https://zdzheng.xyz/publication/SPG-VTON2022)
- 2D to 3D Human [npj AI'26](https://zdzheng.xyz/publication/3D-Magic2026)
- Text to Human [ACM MM'23](https://www.zdzheng.xyz/publication/Towards-2023)
- Text to 3D [TOMM'26](https://www.zdzheng.xyz/publication/Progress2026)
- Face [IJCAI'20](https://zdzheng.xyz/publication/Real-Wor2020), [TCYB'20](https://zdzheng.xyz/publication/Unsuperv2020), [CVPR'22](https://zdzheng.xyz/publication/Multi-Vi2022)
- Sign Language [TOMM'24](https://zdzheng.xyz/publication/Jointly-2024) 
- Hand-Object Interaction [ICRA'26](https://zdzheng.xyz/publication/TIGeR-Te2026)
- Painting [ACM MM'25 BNI](https://www.zdzheng.xyz/publication/Domain-A2025)


## [Uncertainty Estimation](https://www.zdzheng.xyz/tag/uncertainty-learning) 
- Large Models [arXiv'24](https://www.zdzheng.xyz/publication/VL-Uncer2024), [ICLR'26](https://www.zdzheng.xyz/publication/SketchTh2026) 
- Domain Adaptation [IJCV'21](https://zdzheng.xyz/publication/Rectifyi2021)
- Depth Completion [PR'24](https://www.zdzheng.xyz/publication/Self-Ens2024)
- Composed Retrieval [ICLR'24](https://www.zdzheng.xyz/publication/Composed2024)
- Active Learning [CVPR'23](https://www.zdzheng.xyz/publication/Are-Bina2023)
- 3D Bbox Detection [ICCV'25](https://www.zdzheng.xyz/publication/Harnessi2025)
- Conditional Generation [ICLR'25](https://www.zdzheng.xyz/publication/Ctrl-u-R2025)

## [Object Re-identification](https://www.zdzheng.xyz/tag/object-re-identification) 
![](https://zdzheng.xyz/resource-img/3DMarket.jpg)
This research area is to retrieval the relevant multi-media data including cross-view, cross-modality or other challenging cases. 
- 2D Human [TOMM'18](https://zdzheng.xyz/publication/A-discri2018), [TCSVT'19](https://zdzheng.xyz/publication/Pedestri2018), [PR'19](https://zdzheng.xyz/publication/Improvin2019), [AAAI'21](https://zdzheng.xyz/publication/Decouple2021), [TPAMI'22](https://zdzheng.xyz/publication/DMRNet-L2022), [TCYB'22](https://zdzheng.xyz/publication/Soft-Per2022), [TMM'23](https://zdzheng.xyz/publication/Progress2023)
- 2D Vehicle [TMM'20](https://zdzheng.xyz/publication/VehicleN2020), [CVPRW'21](https://zdzheng.xyz/publication/Robust-V2021)
- 3D Human / Objects [TNNLS'22](https://zdzheng.xyz/publication/Paramete2022), [TMM'22](https://zdzheng.xyz/publication/Self-sup2022)
- Cross Modality (Image,Text, Video) [TOMM'20](https://zdzheng.xyz/publication/Dual-pat2020), [CVPRW'21](https://zdzheng.xyz/publication/Connecti2021), [TMM'22](https://zdzheng.xyz/publication/Align-an2022), [ACM MM'23](https://www.zdzheng.xyz/publication/Towards-2023), [ICLR'24](https://www.zdzheng.xyz/publication/Composed2024) 
- Sign Language [TOMM'24](https://zdzheng.xyz/publication/StepNet-2024)
- Adversarial Examples [IJCV'22](https://zdzheng.xyz/publication/U-turn-C2022)


## [Domain Adaptation](https://www.zdzheng.xyz/tag/domain-adaptation) 
![](https://zdzheng.xyz/resource-img/pipeline.png)
This research area is to minimize the gap between the generated data / simulation system with the real-world data / scenario during deployment. 
- Person Re-ID [CVPR'18](https://zdzheng.xyz/publication/Camera-s2018), [TIP'19](https://zdzheng.xyz/publication/Camstyle2019)
- Semantic Segmenetation [IJCAI'20](https://zdzheng.xyz/publication/Unsuperv2020), [IJCV'21](https://zdzheng.xyz/publication/Rectifyi2021), [TIP'22](https://zdzheng.xyz/publication/Adaptive2022), [ACM MM'23](https://zdzheng.xyz/publication/PiPa-Pix2023), [ACM MM'24](https://www.zdzheng.xyz/publication/Transfer2024)

## [Spatial Intelligence](https://www.zdzheng.xyz/tag/spatial-intelligence)
- Cross View (Drone, Satellite, Ground) [ACM MM'20](https://zdzheng.xyz/publication/Universi2020), [TCSVT'21](https://zdzheng.xyz/publication/Each-par2021), [TIP'22](https://zdzheng.xyz/publication/Joint-Re2022), [TGRS'24](https://www.zdzheng.xyz/publication/Learning2024)
- Multi-weather [PR'24](https://zdzheng.xyz/publication/Multiple2024), [NeurIPS'25](https://www.zdzheng.xyz/publication/WeatherP2025)
- Cross Modality [ECCV'24](https://www.zdzheng.xyz/publication/Towards-2024) 
- Video + 3DGS [ICCV'24](https://www.zdzheng.xyz/publication/Video2BE2025)