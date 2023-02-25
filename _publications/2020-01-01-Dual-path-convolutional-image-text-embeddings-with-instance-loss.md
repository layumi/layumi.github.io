---
title: "Dual-path convolutional image-text embeddings with instance loss"
collection: publications
permalink: /publication/Dual-pat2020
date: 2020-01-01
doi: 10.1145/3383184
venue: 'ACM Transactions on Multimedia Computing, Communications, and Applications (TOMM)'
paperurl: 'https://zdzheng.xyz/files/TOMM20.pdf'
blog: 'https://zhuanlan.zhihu.com/p/33163432'
code: 'https://github.com/layumi/Image-Text-Embedding'
author: '<a href=&quot;https://zdzheng.xyz/authors/Zhedong-Zheng&quot;><strong>Zhedong Zheng</strong></a>, <a href=&quot;https://zdzheng.xyz/authors/Liang-Zheng&quot;>Liang Zheng</a>, <a href=&quot;https://zdzheng.xyz/authors/Michael-Garrett&quot;>Michael Garrett</a>, <a href=&quot;https://zdzheng.xyz/authors/Yi-Yang&quot;>Yi Yang</a>, <a href=&quot;https://zdzheng.xyz/authors/Mingliang-Xu&quot;>Mingliang Xu</a>, <a href=&quot;https://zdzheng.xyz/authors/Yi-Dong-Shen&quot;>Yi-Dong Shen</a>'
citation: ' Zhedong Zheng,  Liang Zheng,  Michael Garrett,  Yi Yang,  Mingliang Xu,  Yi-Dong Shen, &quot;Dual-path convolutional image-text embeddings with instance loss.&quot; ACM Transactions on Multimedia Computing, Communications, and Applications (TOMM), 2020. DOI: 10.1145/3383184'
abs: 'Matching images and sentences demands a fine understanding of both modalities. In this paper, we propose a new system to discriminatively embed the image and text to a shared visual-textual space. In this field, most existing works apply the ranking loss to pull the positive image / text pairs close and push the negative pairs apart from each other. However, directly deploying the ranking loss is hard for network learning, since it starts from the two heterogeneous features to build inter-modal relationship. To address this problem, we propose the instance loss which explicitly considers the intra-modal data distribution. It is based on an unsupervised assumption that each image / text group can be viewed as a class. So the network can learn the fine granularity from every image/text group. The experiment shows that the instance loss offers better weight initialization for the ranking loss, so that more discriminative embeddings can be learned. Besides, existing works usually apply the off-the-shelf features, i.e., word2vec and fixed visual feature. So in a minor contribution, this paper constructs an end-to-end dual-path convolutional network to learn the image and text representations. End-to-end learning allows the system to directly learn from the data and fully utilize the supervision. On two generic retrieval datasets (Flickr30k and MSCOCO), experiments demonstrate that our method yields competitive accuracy compared to state-of-the-art methods. Moreover, in language based person retrieval, we improve the state of the art by a large margin. The code has been made publicly available.'
pub_year: '2020'
bib: >
    @article{zheng2020dual,  
    author = "Zheng, Zhedong and Zheng, Liang and Garrett, Michael and Yang, Yi and Xu, Mingliang and Shen, Yi-Dong",  
    doi = "10.1145/3383184",  
    title = "Dual-path convolutional image-text embeddings with instance loss",  
    journal = "ACM Transactions on Multimedia Computing, Communications, and Applications (TOMM)",  
    volume = "16",  
    number = "2",  
    pages = "1--23",  
    year = "2020",  
    code = "https://github.com/layumi/Image-Text-Embedding",  
    blog = "https://zhuanlan.zhihu.com/p/33163432",  
    url = "https://zdzheng.xyz/files/TOMM20.pdf",  
    publisher = "ACM New York, NY, USA",  
    abs = "Matching images and sentences demands a fine understanding of both modalities. In this paper, we propose a new system to discriminatively embed the image and text to a shared visual-textual space. In this field, most existing works apply the ranking loss to pull the positive image / text pairs close and push the negative pairs apart from each other. However, directly deploying the ranking loss is hard for network learning, since it starts from the two heterogeneous features to build inter-modal relationship. To address this problem, we propose the instance loss which explicitly considers the intra-modal data distribution. It is based on an unsupervised assumption that each image / text group can be viewed as a class. So the network can learn the fine granularity from every image/text group. The experiment shows that the instance loss offers better weight initialization for the ranking loss, so that more discriminative embeddings can be learned. Besides, existing works usually apply the off-the-shelf features, i.e., word2vec and fixed visual feature. So in a minor contribution, this paper constructs an end-to-end dual-path convolutional network to learn the image and text representations. End-to-end learning allows the system to directly learn from the data and fully utilize the supervision. On two generic retrieval datasets (Flickr30k and MSCOCO), experiments demonstrate that our method yields competitive accuracy compared to state-of-the-art methods. Moreover, in language based person retrieval, we improve the state of the art by a large margin. The code has been made publicly available."
    }

---