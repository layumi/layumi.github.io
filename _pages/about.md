---
permalink: /
title: "Zhedong Zheng (郑哲东)"
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
---


<head> 
	<style>
		.paper-card {
		  background-color: #f9f9f9; /* 淡灰色背景 */
		  padding: 16px;
		  border-radius: 12px;
		  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05); /* 初始轻微阴影 */
		  margin-bottom: 16px;
		  transition: all 0.25s ease-in-out;
		}
		
		.author {
			text-decoration: none !important;
			color: #333333;
		}
	    a.code-link {
	      color: #181717 !important;
	    }

	    a.zhihu-link {
	      color: #0084FF !important;
	    }

	    a.video-link {
	      color: #FF0000 !important;
	    }

	    a.pdf-link {
	      color: #E41F26 !important;
	    }
		.oral-tag {
		  color: orange;
		}

	    /* 可选 hover 效果 */
	    a.code-link:hover {
	      color: #333 !important;
	    }

	    a.zhihu-link:hover  {
	      color: #006ddf !important;
	    }

	    a.video-link:hover {
	      color: #cc0000 !important;
	    }

	    a.pdf-link:hover{
	      color: #b51a1f !important;
	    }
		.author:hover {
			text-decoration: underline;
			color: #0066cc;
		}
		/* 悬停时的弹起效果 */
		.paper-card:hover {
		  transform: translateY(-4px); /* 微微上移 */
		  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15); /* 增强阴影 */
		}
	</style>
</head>


<meta name="description"
  content="Zhedong Zheng is  a tenure-track assistant professor with the University of Macau, specializing in person re-identification (reID). He obtained his Ph.D. from UTS's ReLER Lab, mentored by Prof. Yi Yang and Dr. Liang Zheng. With a strong foundation from Fudan University, he has collaborated with leading experts at Nvidia and Baidu. His focus on reID underscores his dedication to advancing this vital field.">  
<meta name="keywords" content="Zhedong Zheng, Person Re-ID, Object Re-ID, Person Retrieval, Person Search" />
		   
Hi! I am currently a tenure-track assistant professor with the [University of Macau](https://www.fst.um.edu.mo/people/zhedongzheng/). Prior to this, I was a postdoctoral research fellow at School of Computing, National University of Singapore with <a href="https://www.chuatatseng.com">Prof. Tat-Seng Chua</a> and <a href="https://www.comp.nus.edu.sg/~ayao/">Prof. Angela Yao</a>. I received Ph.D. from the <a href="https://reler.net/">ReLER Lab</a>, <a href="https://www.uts.edu.au/">University of Technology Sydney (UTS) </a>, under the supervision of <a href="https://scholar.google.com/citations?user=RMSuNFwAAAAJ">Prof. Yi Yang</a> and <a href="https://zheng-lab.cecs.anu.edu.au/">Dr. Liang Zheng</a> (co-supervisor). 
Before that, I completed my Bachelor's degree from <a href="https://www.fudan.edu.cn">Fudan University</a> in 2016, under the supervision of <a href="https://scholar.google.com.au/citations?user=DTbhX6oAAAAJ&hl=en">Prof. Xiangyang Xue</a>. 
Throughout my academic journey, I have been fortunate to collaborate with several talented researchers, <a href='https://xiaodongyang.org/'>Xiaodong Yang</a> (Nvidia), <a href='https://chrisding.github.io/'>Zhiding Yu</a> (Nvidia), <a href='https://jankautz.com/'>Jan Kautz</a> (Nvidia), <a href='https://github.com/miraclebiu'>Minyue Jiang</a> (Baidu) and <a href='https://scholar.google.com/citations?user=R1rVRUkAAAAJ'>Xiao Tan</a> (Baidu). I have published 50+ papers <a href='https://scholar.google.com/citations?user=XT17oUEAAAAJ'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Flayumi%2Flayumi.github.io@google-scholar-stats%2Fgs_data_shieldsio.json&labelColor=f6f6f6&color=9cf&style=flat&label=citations" alt="googlescholar" ></a> at top-tier conferences and journals.

Open-source projects can be found at my <a href='https://github.com/layumi'>[Github]</a>, and publications can be found at  [SCI](https://www.webofscience.com/wos/author/record/434956), [SCOPUS](https://www.scopus.com/authid/detail.uri?authorId=57200174037), or [Google Scholar](https://scholar.google.com/citations?hl=en&user=XT17oUEAAAAJ). <strong>More details can be found in my [[CV]]({{ site.url }}{{ site.baseurl }}/files/zhedong-resume.pdf). </strong>

<hr>

<h2><i class="fa-solid fa-bullhorn fa-beat"></i> Open Positions</h2>
<p style="color: #CD853F;">I am actively looking for self-motivated Ph.D. and Master students at University of Macau. PhD students will be fully funded with fellowships. For more information, pls visit <a href="https://www.zdzheng.xyz/recruitment/" style="color: #CD853F;">Join Us</a>.</p>
<!---
<ul>
<li> <mark>If you are a NUS Undergraduate / Master student who is interested in doing research/project with me, please contact me via email with your CV. My current email address is zdzheng AT nus.edu.sg . We will have at least two mentors to guide you and provide gpu resource supports.</mark></li> 
</ul>
-->	
<hr>



<h2><i class="fa-regular fa-compass fa-shake"></i> Research Statement</h2>

My work focuses on multi-view [object re-identification](https://scholar.google.com.sg/citations?view_op=search_authors&hl=zh-CN&mauthors=label:object_re_identification), [AIGC](https://scholar.google.com.sg/citations?view_op=search_authors&hl=zh-CN&mauthors=label:aigc) and [data-centric AI](https://scholar.google.com.sg/citations?view_op=search_authors&hl=zh-CN&mauthors=label:data_centric_ai), under a multi-camera scenario, e.g., swarm robotics, self-driving car, and smart city.

The child understands a 3D object, not from a still image, but from multiple modalities (images / videos / audio) capturing the target of interest from different viewpoints.


<!---
Big data is the primary part of training data-driven models. There remain three scientific questions. 

- Data Generation:  How to obtain more data? Due to the annotation costs and privacy concerns,  we usually could not access the large-scale data easily.  

- Prior Knowledge:  Does more data mean a better model? Deep learning also demands a deep understanding of data (robustness and explainability).

- Efficiency:  How to train on million-scale data? What data matters most? Efficient training and inference is needed.  

AI is not when a computer can write poetry. AI is when a computer want to write poetry. 
-->
<hr>


<h2><i class="fa-solid fa-mug-hot fa-bounce"></i> News</h2>
<ul>
  <li><strong>ACM MM 2025:</strong> 2 papers — 
    <a href="https://www.zdzheng.xyz/publication/UniAD-In2025"> Anomaly Detection</a>, 
    <a href="https://www.zdzheng.xyz/publication/Domain-A2025"> Neural Painting - BNI Track <span class="oral-tag">(<i class="fas fa-star"></i>Oral)</span></a>, 
  </li>
  
  <li><strong>ICCV 2025:</strong> 3 papers — 
    <a href="https://www.zdzheng.xyz/publication/Video2BE2025">Video2BEV</a>, 
    <a href="https://www.zdzheng.xyz/publication/Beyond-W2025">Anomaly Retrieval <span class="oral-tag">(<i class="fas fa-star"></i>Highlight)</span></a>, 
    <a href="https://www.zdzheng.xyz/publication/Harnessi2025">3D Detection</a>
  </li>

  <li><strong>ICLR 2025:</strong> <a href="https://www.zdzheng.xyz/publication/Ctrl-u-R2025">Conditional Generation</a></li>
  <li><strong>ACM WWW 2025:</strong> <a href="https://www.zdzheng.xyz/publication/From-Dat2025">Text-based Person Search</a></li>
  <li><strong>ACM MM 2024:</strong> <a href="https://www.zdzheng.xyz/publication/Transfer2024">Domain Adaptation <span class="oral-tag">(<i class="fas fa-star"></i>Oral)</span></a></li>

  <li><strong>ECCV 2024:</strong> 3 papers — 
    <a href="https://www.zdzheng.xyz/publication/Towards-2024">Text-guided Geolocalization</a>, 
    <a href="https://www.zdzheng.xyz/publication/Depth-aw2024">Blind Image Decomposition</a>, 
    <a href="https://www.zdzheng.xyz/publication/Approach2024">Unsupervised 3D Object Detection</a>
  </li>

  <li><strong>ACM MM 2025 Workshop:</strong> Aerial-view Imaging 
    <a href="https://www.zdzheng.xyz/ACMMM2025Workshop-UAV/">[Call for Papers]</a>
  </li>
</ul>

<details>
  <summary>--View More--</summary>
  <ul>
    <li><strong>ACM MM 2024 Workshops:</strong> 
      <a href="https://www.zdzheng.xyz/ACMMM2024Workshop-UAV/">Aerial-view Imaging</a>, 
      <a href="https://videorelation.nextcenter.org/MMGR24/">Multimodal Learning</a>
    </li>
    <li><strong>ICLR 2024:</strong> 
      <a href="https://www.zdzheng.xyz/publication/Composed2024">Compositional Retrieval</a> 
      <a href="https://github.com/Monoxide-Chen/uncertainty_retrieval">[code]</a>
    </li>
    <li><strong>ACM ICMR 2024 Workshop:</strong> Multimedia Object Re-ID 
      <a href="https://www.zdzheng.xyz/MORE2024/">[Call for Papers]</a>
    </li>
    <li><strong>ACM MM 2023:</strong> 2 papers — 
      <a href="https://www.zdzheng.xyz/publication/Towards-2023">Text-image Re-ID</a>, 
      <a href="https://www.zdzheng.xyz/publication/PiPa-Pix2023">Domain Adaptation</a>
    </li>
    <li><strong>CVPR 2023:</strong> 2 papers — 
      <a href="https://www.zdzheng.xyz/publication/Context-2023">Weather Removal</a>, 
	  <a href="https://www.zdzheng.xyz/publication/Are-Bina2023">Video Moment Retrieval</a>
	</li>  
    <li><strong>IJCV 2022:</strong> <a href="https://zdzheng.xyz/publication/U-turn-C2022">Adversarial Retrieval</a></li>
    <li><strong>TNNLS 2022:</strong> <a href="https://zdzheng.xyz/publication/Paramete2022">3D Human Re-ID</a></li>
    <li><strong>TIP 2022:</strong> 2 papers — 
      <a href="https://zdzheng.xyz/publication/Adaptive2022">AdaBoost Adaptation</a>, 
      <a href="https://zdzheng.xyz/publication/Joint-Re2022">Drone Geolocalization</a>
    </li>
    <li><strong>CVPR 2022:</strong> <a href="https://zdzheng.xyz/publication/Multi-Vi2022">NeRF</a></li>
    <li><strong>ICME 2022:</strong> Special Session on Responsible Retrieval 
      <a href="https://zdzheng.xyz/ICME2022SS/">[Call for Papers]</a>
    </li>
    <li><strong>Ph.D. Thesis:</strong> Chancellor’s List</li>
    <li><strong>Award:</strong> 2021 IEEE CAS Outstanding Young Author Award 
      <a href="https://ieee-cas.org/award/outstanding-paper-awards/outstanding-young-author-award#recipients">[link]</a>
    </li>
    <li><strong>IJCV 2021:</strong> 
      <a href="https://zdzheng.xyz/publication/Recti2021">Uncertainty</a> 
      <a href="https://github.com/layumi/Seg_Uncertainty">[code]</a>
    </li>
    <li><strong>ACM MM 2020:</strong> Drone-view Dataset 
      <a href="https://zdzheng.xyz/publication/Unive2020">[PDF]</a> 
      <a href="https://github.com/layumi/University1652-Baseline">[Dataset]</a> 
      <a href="https://www.youtube.com/embed/dzxXPp8tVn4?vq=hd1080">[Video]</a> 
      <a href="https://zdzheng.xyz/files/ACM-MM-Talk.pdf">[Slide]</a>
    </li>
  </ul>
</details>


<!---	
<li><strong>PI</strong>, FDCT/0043/2025/RIA1, “Robust Long-Tail Anomaly Recognition via Multi-Modality Learning”, 2025–2028 MOP 2.13 million (≈ USD 260K)</li>
<li> People live in a 3D world. Why not conduct representation learning in the 3D space? <a href="https://arxiv.org/abs/2006.04569">[arXiv]</a> <a href="https://github.com/layumi/person-reid-3d">[code]</a></li>
<li> We have achieved the <strong>1st</strong> place in AICity Challenge Vehicle Re-id Track, CVPR 2020. <a href="https://github.com/layumi/AICIty-reID-2020">[code] </a></li>
<li> Two papers to appear at IJCAI 2020. <a href="https://zdzheng.xyz/publication/Unsup2020">[PDF1]</a><a href="https://github.com/layumi/Seg_Uncertainty">[code1]</a><a href="https://zdzheng.xyz/publication/Real-2020">[PDF2]</a>
	<a href="https://github.com/huangzhikun1995/IPM-Net">[code2]</a></li>
<li> One paper to appear at CVPR 2019 as oral presentation. <a href="https://zdzheng.xyz/publication/Joint2019">[PDF]</a><a href="https://www.youtube.com/watch?v=ubCrEAIpQs4">[3-min video]</a> <a href="https://github.com/NVlabs/DG-Net">[code]</a></li>
<li> One paper to appear at ECCV 2018. <a href="https://arxiv.org/abd/1807.08260">[arXiv]</a> <a href="https://github.com/RoyalVane/MMAN">[code]</a> </li>
<li> One paper to appear at CVPR 2018. <a href="https://arxiv.org/abs/1711.10295">[arXiv]</a> <a href="https://github.com/zhunzhong07/CamStyle">[code]</a> </li>
<li> One paper to appear at ICCV 2017 as spotlight presentation. <a href="https://arxiv.org/abs/1701.07717">[arXiv]</a> <a href="https://github.com/layumi/Person-reID_GAN"> [code]</a> </li>
-->

<hr>


<h2><i class="fa-solid fa-palette fa-beat"></i> Others</h2>
<ul>
<li>  <a href="https://www.youtube.com/watch?v=kI3Oc-sxSoA">Shanghai</a> is my hometown, and it is a lovely place to have a sightseeing tour. </li>
<li>  I was a poster maker when I studied at Fudan University. You may check out <a href="https://www.zdzheng.xyz/poster_page">my posters</a>.</li>
<li>  I sometimes write Chinese blogs and share insights at <a href="https://www.zhihu.com/people/zhengzhedong">Zhihu</a>.</li>
</ul>
Do not press the red button!

<a href="https://zdzheng.xyz/redbutton.html"> <img src="https://zdzheng.xyz/images/red.webp" alt="red" width="50" height="50"></a>
<a href="https://zdzheng.xyz/greenbutton.html"> <img src="https://zdzheng.xyz/images/green.webp" alt="green" width="50" height="50"> </a>




  


