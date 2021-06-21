---
title: "Rectifying Pseudo Label Learning via Uncertainty Estimation for Domain Adaptive Semantic Segmentation"
collection: publications
permalink: /publication/2021-01-01-Rectifying-Pseudo-Label-Learning-via-Uncertainty-Estimation-for-Domain-Adaptive-Semantic-Segmentation
date: 2021-01-01
doi: 10.1007/s11263-020-01395-y
venue: 'International Journal of Computer Vision (IJCV)'
paperurl: 'https://zdzheng.xyz/files/Zheng-Yang2021_Article_RectifyingPseudoLabelLearningV.pdf'
code: 'https://github.com/layumi/Seg-Uncertainty'
author: '<strong>Zhedong Zheng</strong>,  Yi Yang'
citation: ' Zhedong Zheng,  Yi Yang, &quot;Rectifying Pseudo Label Learning via Uncertainty Estimation for Domain Adaptive Semantic Segmentation.&quot; International Journal of Computer Vision (IJCV), 2021. DOI: 10.1007/s11263-020-01395-y'
abs: 'This paper focuses on the unsupervised domain adaptation of transferring the knowledge from the source domain to the target domain in the context of semantic segmentation. Existing approaches usually regard the pseudo label as the ground truth to fully exploit the unlabeled target-domain data. Yet the pseudo labels of the target-domain data are usually predicted by the model trained on the source domain. Thus, the generated labels inevitably contain the incorrect prediction due to the discrepancy between the training domain and the test domain, which could be transferred to the final adapted model and largely compromises the training process. To overcome the problem, this paper proposes to explicitly estimate the prediction uncertainty during training to rectify the pseudo label learning for unsupervised semantic segmentation adaptation. Given the input image, the model outputs the semantic segmentation prediction as well as the uncertainty of the prediction. Specifically, we model the uncertainty via the prediction variance and involve the uncertainty into the optimization objective. To verify the effectiveness of the proposed method, we evaluate the proposed method on two prevalent synthetic-to-real semantic segmentation benchmarks, i.e., GTA5 -> Cityscapes and SYNTHIA -> Cityscapes, as well as one cross-city benchmark, i.e., Cityscapes -> Oxford RobotCar. We demonstrate through extensive experiments that the proposed approach (1) dynamically sets different confidence thresholds according to the prediction variance, (2) rectifies the learning from noisy pseudo labels, and (3) achieves significant improvements over the conventional pseudo label learning and yields competitive performance on all three benchmarks.'
pub_year: '2021'
bib: >
    ```br
    @article{Zheng_2021,  
    author = "Zheng, Zhedong and Yang, Yi",  
    doi = "10.1007/s11263-020-01395-y",  
    year = "2021",  
    month = "jan",  
    publisher = "Springer",  
    volume = "129",  
    number = "4",  
    pages = "1106--1120",  
    title = "Rectifying Pseudo Label Learning via Uncertainty Estimation for Domain Adaptive Semantic Segmentation",  
    code = "https://github.com/layumi/Seg-Uncertainty",  
    url = "https://zdzheng.xyz/files/Zheng-Yang2021\_Article\_RectifyingPseudoLabelLearningV.pdf",  
    journal = "International Journal of Computer Vision (IJCV)",  
    abs = "This paper focuses on the unsupervised domain adaptation of transferring the knowledge from the source domain to the target domain in the context of semantic segmentation. Existing approaches usually regard the pseudo label as the ground truth to fully exploit the unlabeled target-domain data. Yet the pseudo labels of the target-domain data are usually predicted by the model trained on the source domain. Thus, the generated labels inevitably contain the incorrect prediction due to the discrepancy between the training domain and the test domain, which could be transferred to the final adapted model and largely compromises the training process. To overcome the problem, this paper proposes to explicitly estimate the prediction uncertainty during training to rectify the pseudo label learning for unsupervised semantic segmentation adaptation. Given the input image, the model outputs the semantic segmentation prediction as well as the uncertainty of the prediction. Specifically, we model the uncertainty via the prediction variance and involve the uncertainty into the optimization objective. To verify the effectiveness of the proposed method, we evaluate the proposed method on two prevalent synthetic-to-real semantic segmentation benchmarks, i.e., GTA5 -> Cityscapes and SYNTHIA -> Cityscapes, as well as one cross-city benchmark, i.e., Cityscapes -> Oxford RobotCar. We demonstrate through extensive experiments that the proposed approach (1) dynamically sets different confidence thresholds according to the prediction variance, (2) rectifies the learning from noisy pseudo labels, and (3) achieves significant improvements over the conventional pseudo label learning and yields competitive performance on all three benchmarks."
    }
    ```

---