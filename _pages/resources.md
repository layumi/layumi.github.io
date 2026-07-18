---
layout: archive
title: "Resources"
seo_title: Drone Geo-Localization | Person Re-ID | Datasets & Code
permalink: /resources/
author_profile: true
classes: wide
---

<meta name="description" content="Open-source Code, Benchmarks and Datasets for UAV Geo-localization, Aerial Spatial Intelligence, Person Re-ID, Text-based Person Search and Anomaly Search"/>
<meta name="keywords" content="UAV, Drone, Geo-localization, Spatial Intelligence, BEV, Code and Dataset, Person Re-ID, Object Re-ID, Person Retrieval, Anomaly Search, Domain Adaptation, Person Search" />

<style>
/* ---- Card grid: soft cards with hover lift ---- */
table.cardtable {
  border-collapse: separate;
  border-spacing: 10px;
  table-layout: fixed;
  width: 100%;
  border: none;
}
table.cardtable td {
  border: 1px solid #e2e8f0;
  border-radius: 14px;
  background: #fbfcfe;
  padding: 18px 10px 14px;
  vertical-align: top;
  transition: transform .18s ease, box-shadow .18s ease, border-color .18s ease;
}
table.cardtable td:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 20px rgba(15, 23, 42, .08);
  border-color: #94a3b8;
  background: #ffffff;
}
table.cardtable td a {
  text-decoration: none;
}
table.cardtable h3 {
  margin: 0 0 6px;
  font-size: 26px;
  line-height: 1;
}
table.cardtable sub {
  color: #64748b;
  line-height: 1.5;
}

/* ---- Dataset table: light row dividers instead of a black grid ---- */
table.imgtable {
  border-collapse: separate;
  border-spacing: 0;
  border: 1px solid #e2e8f0;
  border-radius: 14px;
  overflow: hidden;
  width: 100%;
}
table.imgtable td {
  border: none;
  border-bottom: 1px solid #edf2f7;
  padding: 16px;
  vertical-align: middle;
}
table.imgtable tbody:last-child td {
  border-bottom: none;
}
table.imgtable code {
  background: #eef2ff;
  color: #4338ca;
  border-radius: 6px;
  padding: 1px 8px;
  font-size: 12px;
}
</style>

<p align="center">
  ⭐ If our datasets and code help your research, a <b>star on GitHub</b> is the best support! ⭐<br>
  <sub>🌟 We are always looking for self-motivated PhD students / RAs / visiting students — see <a href="https://www.zdzheng.xyz/">Join Us</a>.</sub>
</p>

---

## 🚁 UAV & Spatial Intelligence

<p><i>Benchmarks, code and datasets for low-altitude aerial perception: cross-view geo-localization, BEV understanding and aerial reasoning.</i></p>

<p align="center"><b>🎓 The University-1652 Family</b></p>

<div align="center">
  <table class="cardtable">
    <tr>
      <td align="center" width="33%">
        <a href="https://github.com/layumi/University1652-Baseline">
          <h3>🎓</h3>
          <b>University-1652</b>
        </a>
        <br><sub>Multi-view Multi-source Benchmark<br>Ground · Drone · Satellite · ACM MM'20</sub>
        <br><br>
        <a href="https://github.com/layumi/University1652-Baseline"><img src="https://img.shields.io/github/stars/layumi/University1652-Baseline.svg?style=social&label=Star" alt="GitHub stars"></a>
      </td>
      <td align="center" width="33%">
        <a href="https://github.com/wtyhub/MuseNet">
          <h3>🌦️</h3>
          <b>University-WX</b>
        </a>
        <br><sub>Multi-Weather Extension on the Fly<br>Pattern Recognition'24</sub>
        <br><br>
        <a href="https://github.com/wtyhub/MuseNet"><img src="https://img.shields.io/github/stars/wtyhub/MuseNet.svg?style=social&label=Star" alt="GitHub stars"></a>
      </td>
      <td align="center" width="33%">
        <a href="https://github.com/MultimodalGeo/GeoText-1652">
          <h3>💬</h3>
          <b>GeoText-1652</b>
        </a>
        <br><sub>Dense Text Extension<br>ECCV'24</sub>
        <br><br>
        <a href="https://github.com/MultimodalGeo/GeoText-1652"><img src="https://img.shields.io/github/stars/MultimodalGeo/GeoText-1652.svg?style=social&label=Star" alt="GitHub stars"></a>
      </td>
    </tr>
  </table>
</div>

<p align="center"><b>🚀 New Open-Source Releases</b></p>

<div align="center">
  <table class="cardtable">
    <tr>
      <td align="center" width="25%">
        <a href="https://github.com/YsongF/GeoFuse">
          <h3>🛣️</h3>
          <b>GeoFuse</b>
        </a>
        <br><sub>Road Maps as <b>Free</b> Geometric Priors<br>Weather-Invariant Drone Geo-Localization</sub>
        <br><br>
        <a href="https://github.com/YsongF/GeoFuse"><img src="https://img.shields.io/github/stars/YsongF/GeoFuse.svg?style=social&label=Star" alt="GitHub stars"></a>
      </td>
      <td align="center" width="25%">
        <a href="https://github.com/JT-Sun/UAVReason">
          <h3>🧠</h3>
          <b>UAVReason</b>
        </a>
        <br><sub>Aerial Scene Reasoning &amp; Generation Benchmark</sub>
        <br><br>
        <a href="https://github.com/JT-Sun/UAVReason"><img src="https://img.shields.io/github/stars/JT-Sun/UAVReason.svg?style=social&label=Star" alt="GitHub stars"></a>
      </td>
      <td align="center" width="25%">
        <a href="https://github.com/HaoDot/Video2BEV-Open">
          <h3>🗺️</h3>
          <b>Video2BEV</b>
        </a>
        <br><sub>Drone Video → Bird's-Eye-View</sub>
        <br><br>
        <a href="https://github.com/HaoDot/Video2BEV-Open"><img src="https://img.shields.io/github/stars/HaoDot/Video2BEV-Open.svg?style=social&label=Star" alt="GitHub stars"></a>
      </td>
      <td align="center" width="25%">
        <a href="https://github.com/YaxuanLi-cn/PairUAV">
          <h3>🚁</h3>
          <b>PairUAV</b>
        </a>
        <br><sub>Paired UAV Data for Matching</sub>
        <br><br>
        <a href="https://github.com/YaxuanLi-cn/PairUAV"><img src="https://img.shields.io/github/stars/YaxuanLi-cn/PairUAV.svg?style=social&label=Star" alt="GitHub stars"></a>
      </td>
    </tr>
  </table>
</div>

**Community & Ecosystem**
- 🛩️ Host of the **UAVM Workshop Series** on UAVs in Multimedia @ ACM Multimedia (2023–2026). <!-- TODO: 补上最新一届workshop的链接，例如 https://www.zdzheng.xyz/UAVM2026/ -->
- 📚 [Awesome Geo-localization](https://www.zdzheng.xyz/Awesome-Geo-localization): curated papers, datasets and leaderboards.
<!-- TODO: 数据集上传 Hugging Face 后，在此加一行 🤗 HF mirror 链接 -->

---

## 🔍 Person Re-ID & Text-based Retrieval

<div align="center">
  <table class="cardtable">
    <tr>
      <td align="center" colspan="3">
        <a href="https://github.com/layumi/Person_reID_baseline_pytorch">
          <h3>⛹️</h3>
          <b>Person re-ID Baseline (PyTorch)</b>
        </a>
        <br><sub>A <b>Tiny, Friendly &amp; Strong</b> PyTorch Baseline for Person / Vehicle Re-ID<br>with Hands-on Tutorial · The Community Standard since 2017</sub>
        <br><br>
        <a href="https://github.com/layumi/Person_reID_baseline_pytorch"><img src="https://img.shields.io/github/stars/layumi/Person_reID_baseline_pytorch.svg?style=social&label=Star" alt="GitHub stars"></a>
      </td>
    </tr>
    <tr>
      <td align="center" width="33%">
        <a href="https://github.com/layumi/3D-Magic-Mirror">
          <h3>🪞</h3>
          <b>3D Magic Mirror</b>
        </a>
        <br><sub>Clothing Reconstruction from a Single Image<br>via a Causal Perspective · npj AI'26</sub>
        <br><br>
        <a href="https://github.com/layumi/3D-Magic-Mirror"><img src="https://img.shields.io/github/stars/layumi/3D-Magic-Mirror.svg?style=social&label=Star" alt="GitHub stars"></a>
      </td>
      <td align="center" width="33%">
        <a href="https://github.com/NVlabs/DG-Net">
          <h3>✨</h3>
          <b>DG-Net</b>
        </a>
        <br><sub>Joint Generation + Re-ID Learning<br>CVPR'19 Oral · NVIDIA</sub>
        <br><br>
        <a href="https://github.com/NVlabs/DG-Net"><img src="https://img.shields.io/github/stars/NVlabs/DG-Net.svg?style=social&label=Star" alt="GitHub stars"></a>
      </td>
      <td align="center" width="33%">
        <a href="https://github.com/layumi/Person-reID_GAN">
          <h3>🎨</h3>
          <b>Person re-ID GAN</b>
        </a>
        <br><sub>GAN-based Augmentation (LSRO)<br>ICCV'17</sub>
        <br><br>
        <a href="https://github.com/layumi/Person-reID_GAN"><img src="https://img.shields.io/github/stars/layumi/Person-reID_GAN.svg?style=social&label=Star" alt="GitHub stars"></a>
      </td>
    </tr>
    <tr>
      <td align="center" width="33%">
        <a href="https://github.com/layumi/Image-Text-Embedding">
          <h3>📝</h3>
          <b>Language Person Search</b>
        </a>
        <br><sub>Text-based Person Retrieval<br>Dual-Path Embedding</sub>
        <br><br>
        <a href="https://github.com/layumi/Image-Text-Embedding"><img src="https://img.shields.io/github/stars/layumi/Image-Text-Embedding.svg?style=social&label=Star" alt="GitHub stars"></a>
      </td>
      <td align="center" width="33%">
        <a href="https://github.com/Shuyu-XJTU/APTM">
          <h3>🏷️</h3>
          <b>APTM</b>
        </a>
        <br><sub>Attribute Prompt Learning &amp; Text Matching<br>MALS Benchmark (1.5M pairs) · ACM MM'23</sub>
        <br><br>
        <a href="https://github.com/Shuyu-XJTU/APTM"><img src="https://img.shields.io/github/stars/Shuyu-XJTU/APTM.svg?style=social&label=Star" alt="GitHub stars"></a>
      </td>
      <td align="center" width="33%">
        <a href="https://github.com/Shuyu-XJTU/CMP">
          <h3>🚨</h3>
          <b>CMP</b>
        </a>
        <br><sub>Text-based Person <b>Anomaly</b> Search<br>PAB Benchmark (1M pairs) · ICCV'25 <b>Highlight</b></sub>
        <br><br>
        <a href="https://github.com/Shuyu-XJTU/CMP"><img src="https://img.shields.io/github/stars/Shuyu-XJTU/CMP.svg?style=social&label=Star" alt="GitHub stars"></a>
      </td>
    </tr>
    <tr>
      <td align="center" width="33%">
        <a href="https://github.com/nkuzjh/UATTA">
          <h3>🎯</h3>
          <b>UATTA</b>
        </a>
        <br><sub>Uncertainty-Aware Test-Time Adaptation<br>for Text-based Person Search · SIGIR'26</sub>
        <br><br>
        <a href="https://github.com/nkuzjh/UATTA"><img src="https://img.shields.io/github/stars/nkuzjh/UATTA.svg?style=social&label=Star" alt="GitHub stars"></a>
      </td>
      <td align="center" width="33%">
        <a href="https://github.com/layumi/person-reid-3d">
          <h3>🧊</h3>
          <b>3D Person re-ID</b>
        </a>
        <br><sub>Parameter-Efficient Re-ID<br>in the 3D Space (OG-Net)</sub>
        <br><br>
        <a href="https://github.com/layumi/person-reid-3d"><img src="https://img.shields.io/github/stars/layumi/person-reid-3d.svg?style=social&label=Star" alt="GitHub stars"></a>
      </td>
      <td align="center" width="33%">
        <a href="https://github.com/layumi/Pedestrian_Alignment">
          <h3>🚶</h3>
          <b>Pedestrian Alignment</b>
        </a>
        <br><sub>Pedestrian Alignment Network (PAN)<br>for Robust Re-ID</sub>
        <br><br>
        <a href="https://github.com/layumi/Pedestrian_Alignment"><img src="https://img.shields.io/github/stars/layumi/Pedestrian_Alignment.svg?style=social&label=Star" alt="GitHub stars"></a>
      </td>
    </tr>
  </table>
</div>

### Datasets

<table class="imgtable">
    <tbody><tr><td align="center">
	<img src="https://zdzheng.xyz/resource-img/PAB.jpg" alt="Pedestrian Anomaly Behavior " width="80%"> &nbsp;</td>
	<td align="left"> <strong> PAB Dataset </strong> <code>ICCV 2025 Highlight</code> <strong><a href="https://github.com/Shuyu-XJTU/CMP"> [website]</a></strong> 
    We propose a new task, text-based person anomaly search, locating pedestrians engaged in both routine or anomalous activities via text. To enable the training and evaluation of this new task, we construct a large-scale image-text Pedestrian Anomaly Behavior (PAB) benchmark, featuring a broad spectrum of actions, e.g., running, performing, playing soccer, and the corresponding anomalies, e.g., lying, being hit, and falling of the same identity. The training set of PAB comprises 1,013,605 synthesized image-text pairs of both normalities and anomalies, while the test set includes 1,978 real-world image-text pairs. 
	</td>
</tr></tbody>
	
	<tbody><tr><td align="center">
    <img src="https://zdzheng.xyz/resource-img/MALS.jpg" alt="MALS" width="80%"> &nbsp;</td>
    <td align="left"> <strong> MALS Dataset </strong> <code>ACM MM 2023</code> <strong><a href="https://github.com/Shuyu-XJTU/APTM"> [website]</a></strong> 
We present a large Multi-Attribute and Language Search dataset for text-based person retrieval, called MALS, and explore the feasibility of performing pre-training on both attribute recognition and image-text matching tasks in one stone. In particular, MALS contains 1, 510, 330 image-text pairs, which is about 37.5× larger than prevailing CUHK-PEDES, and all images are annotated with 27 attributes.
    </td>
</tr></tbody>

	<tbody><tr><td align="center">
<img src="https://zdzheng.xyz/resource-img/attribute.jpg" alt="Pedestrian Attribute" width="80%"> &nbsp; </td>
    <td align="left"> <strong> Market-1501 and DukeMTMC-reID Attribute Datasets</strong>   <strong><a href="https://vana77.github.io"> [website]</a></strong>
We manually annotate attribute labels for two large-scale re-ID datasets, and systematically investigate how person re-ID and attribute recognition benefit from each other. 
    </td>
</tr></tbody>
 
	<tbody><tr><td align="center">
<img src="https://zdzheng.xyz/resource-img/3DMarket.jpg" alt="3D Market" width="80%"> &nbsp;</td>
   <td align="left"> <strong> 3D Market-1501 Dataset</strong>  <strong><a href="https://github.com/layumi/person-reid-3d"> [website]</a></strong> 
You could find the point-cloud format Market-1501 Dataset at https://github.com/layumi/person-reid-3d.
    </td>
</tr></tbody>

	<tbody><tr><td align="center">
<img src="https://zdzheng.xyz/resource-img/DG-Market.jpg" alt="DG-Market" width="80%"> &nbsp;</td>
<td align="left"> <strong> DG-Market Dataset</strong>  We provide our generated images and make a large-scale synthetic dataset called DG-Market. This dataset is generated by our <a href="https://arxiv.org/abs/1904.07223">DG-Net</a> and consists of 128,307 images (613MB), about 10 times larger than the training set of original Market-1501 (even much more can be generated with DG-Net). It can be used as a source of unlabeled training dataset for semi-supervised learning. You may download the dataset from <a href="https://drive.google.com/file/d/126Gn90Tzpk3zWp2c7OBYPKc-ZjhptKDo/view?usp=sharing">[Google Drive]</a> (or <a href="https://pan.baidu.com/s/1n4M6s-qvE08J8SOOWtWfgw">[Baidu Disk]</a>) password: qxyh).
    </td>
</tr></tbody></table>

<details>
<summary><b>📦 Legacy Datasets & Tutorials</b> (click to expand)</summary>
<ul>
  <li>HQ-Market Super-resolution Dataset. <strong><a href="https://github.com/layumi/HQ-Market"> [website]</a></strong></li>
  <li>DukeMTMC-reID Dataset. <strong><a href="https://github.com/layumi/Duke_evaluation"> [website]</a></strong>  <strong><a href="https://github.com/layumi/Person_reID_baseline_pytorch/tree/master/leaderboard"> [SoTA]</a></strong></li>
  <li>DukeMTMC-Pose Dataset. <strong><a href="https://github.com/layumi/DukeMTMC-Pose"> [website]</a></strong></li>
  <li>UTS Person-reID Tutorial. <strong><a href="https://github.com/layumi/Person_reID_baseline_pytorch/tree/master/tutorial"> [website]</a></strong></li>
</ul>
</details>

---

### Awesome Lists
- [Awesome Geo-localization](https://www.zdzheng.xyz/Awesome-Geo-localization)
- [Awesome Vehicle Retrieval](https://github.com/layumi/Vehicle_reID-Collection)
- [Awesome Segmentation Domain Adaptation](https://github.com/layumi/Seg-Uncertainty/tree/master/awesome-SegDA)
- [Awesome Fools](https://github.com/layumi/Awesome-Fools)

---

## 🎓 For Students

### Motivations
![](https://zdzheng.xyz/files/optimizer.gif)
- [The illustrated guide to a Ph.D.](https://matt.might.net/articles/phd-school-in-pictures/)
-  <strong><a href="https://www.evernote.com/shard/s150/sh/3de79ff0-5778-417c-9bcb-6c0111a26694/29958003bb71992667ce3f42fd4ca875"> 熊辉: 为什么人前进的路总是被自己挡住 </a></strong> 
-  <strong><a href="https://zdzheng.xyz/files/road.pdf">陈海波: 一名系统研究者的攀登之路</a></strong> 
-  <strong><a href="https://www.douban.com/note/218498393/">勇气与真意——关于围棋的八卦</a></strong>
-  [山世光：致联系报考我免试研究生的同学们](https://blog.csdn.net/GarfieldEr007/article/details/51018552) 

### How to 
- [How to research? Jianxiong Xiao](https://zdzheng.xyz/files/lecture21_how2research.pdf)
- [How to have productive meetings with busy mentors?](http://kordinglab.com/2021/06/30/meeting-with-mentors.html)
- [How to start writing papers?](http://kordinglab.com/2016/01/14/writing-guide.html)
- [How to rebuttal? Devi Parikh](https://deviparikh.medium.com/how-we-write-rebuttals-dc84742fece1)

---

<p align="center">
  <sub><i>Last updated: July 2026. If you build something cool on top of our benchmarks, we are happy to feature it — drop us an email!</i></sub>
</p>